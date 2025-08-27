import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
import joblib
import os

def generate_mock_data():
    """Generate mock consumption data for training"""
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=1000, freq='H')
    data = pd.DataFrame({
        'timestamp': dates,
        'region': np.random.choice(['North', 'South', 'East', 'West'], 1000),
        'consumption': np.random.normal(100, 20, 1000) + 10 * np.sin(np.arange(1000) * 2 * np.pi / 24)
    })
    return data

def train_forecast_model(data):
    """Train a simple linear regression model for forecasting"""
    data['timestamp_num'] = data['timestamp'].astype(int) // 10**9
    X = data[['timestamp_num']]
    y = data['consumption']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mape = mean_absolute_percentage_error(y_test, predictions)
    print(f"MAPE: {mape:.2%}")
    
    return model

def train_anomaly_model(data):
    """Train an isolation forest for anomaly detection"""
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(data[['consumption']])
    return model

def save_models(forecast_model, anomaly_model):
    """Save trained models"""
    os.makedirs('models', exist_ok=True)
    joblib.dump(forecast_model, 'models/forecast_model.pkl')
    joblib.dump(anomaly_model, 'models/anomaly_model.pkl')

def load_models():
    """Load trained models"""
    forecast_model = joblib.load('models/forecast_model.pkl')
    anomaly_model = joblib.load('models/anomaly_model.pkl')
    return forecast_model, anomaly_model

if __name__ == "__main__":
    data = generate_mock_data()
    forecast_model = train_forecast_model(data)
    anomaly_model = train_anomaly_model(data)
    save_models(forecast_model, anomaly_model)
    print("Models trained and saved!")
