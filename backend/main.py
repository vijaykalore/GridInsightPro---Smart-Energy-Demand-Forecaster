from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest
import uuid
from datetime import datetime
from typing import List, Optional
import os

app = FastAPI(title="GridInsightPro API", version="1.0.0")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://127.0.0.1:3000", "http://127.0.0.1:3001"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage (for demo, use DB in production)
users_db = {}
consumption_data_db = {}
forecasts_db = {}
anomalies_db = {}
scenarios_db = {}
audit_logs_db = []

# Simple ML models
try:
    import joblib
    forecast_model = joblib.load('../ml/models/forecast_model.pkl')
    anomaly_model = joblib.load('../ml/models/anomaly_model.pkl')
    print("Loaded trained models")
except:
    print("Using mock models")
    forecast_model = LinearRegression()
    anomaly_model = IsolationForest(contamination=0.1, random_state=42)

# Mock data for demo
mock_data = pd.DataFrame({
    'timestamp': pd.date_range('2023-01-01', periods=100, freq='H'),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'value': np.random.normal(100, 20, 100)
})

# Train models on mock data
X = mock_data[['timestamp']].astype(int) // 10**9
y = mock_data['value']
forecast_model.fit(X, y)
anomaly_model.fit(mock_data[['value']])

@app.get("/")
async def root():
    return {"message": "Welcome to GridInsightPro API"}

@app.post("/api/upload")
async def upload_data(file: UploadFile = File(...)):
    if not file.filename.endswith(('.csv', '.xlsx')):
        raise HTTPException(status_code=400, detail="Invalid file format")
    
    # Save file
    file_id = str(uuid.uuid4())
    file_path = f"uploads/{file_id}_{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # Process data (mock processing)
    try:
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
        
        print(f"Loaded dataframe with shape: {df.shape}")
        print(f"Columns: {df.columns.tolist()}")
        
        # Validate schema
        required_cols = ['region', 'timestamp', 'value']
        if not all(col in df.columns for col in required_cols):
            raise HTTPException(status_code=400, detail=f"Missing required columns. Found: {df.columns.tolist()}, Required: {required_cols}")
        
        print(f"Data validation passed. Processing {len(df)} rows...")
        
        # Store data
        for _, row in df.iterrows():
            data_id = str(uuid.uuid4())
            consumption_data_db[data_id] = {
                'id': data_id,
                'region': row['region'],
                'timestamp': row['timestamp'],
                'value': row['value'],
                'file_id': file_id
            }
        
        print(f"Successfully stored {len(df)} data points")
        
        # Log audit
        audit_logs_db.append({
            'id': str(uuid.uuid4()),
            'user_id': 'mock_user',
            'action': 'upload',
            'target_id': file_id,
            'timestamp': datetime.now()
        })
        
        return {"message": "Data uploaded successfully", "file_id": file_id, "records_processed": len(df)}
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@app.get("/api/forecast")
async def get_forecast(region: str, period: str):
    # Mock forecast
    future_timestamps = pd.date_range(datetime.now(), periods=24, freq='H')
    X_future = pd.DataFrame({'timestamp': future_timestamps}).astype(int) // 10**9
    predictions = forecast_model.predict(X_future)
    
    forecast_id = str(uuid.uuid4())
    forecasts_db[forecast_id] = {
        'id': forecast_id,
        'region': region,
        'period': period,
        'predicted_value': predictions.mean(),
        'model_version': '1.0'
    }
    
    return {"forecast": forecasts_db[forecast_id]}

@app.get("/api/anomalies")
async def get_anomalies():
    # Mock anomaly detection
    data_values = mock_data[['value']]
    scores = anomaly_model.decision_function(data_values)
    anomalies = anomaly_model.predict(data_values)
    
    anomaly_list = []
    for i, pred in enumerate(anomalies):
        if pred == -1:  # Anomaly
            anomaly_id = str(uuid.uuid4())
            anomalies_db[anomaly_id] = {
                'id': anomaly_id,
                'data_id': str(i),
                'type': 'consumption_anomaly',
                'severity': int(abs(scores[i]) * 10),
                'detected_at': datetime.now()
            }
            anomaly_list.append(anomalies_db[anomaly_id])
    
    return {"anomalies": anomaly_list}

@app.post("/api/scenarios")
async def create_scenario(name: str, data_refs: List[str]):
    scenario_id = str(uuid.uuid4())
    scenarios_db[scenario_id] = {
        'id': scenario_id,
        'name': name,
        'owner_id': 'mock_user',
        'data_refs': data_refs,
        'comments': []
    }
    return {"scenario": scenarios_db[scenario_id]}

@app.get("/api/users")
async def get_users():
    return {"users": list(users_db.values())}

@app.get("/api/data")
async def get_data(region: Optional[str] = None):
    data = list(consumption_data_db.values())
    if region:
        data = [d for d in data if d['region'] == region]
    return {"data": data}
