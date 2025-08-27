# GridInsightPro - Smart Energy Demand Forecaster

A web application for energy providers to forecast demand using big data and AI.

## Overview

GridInsightPro enables energy providers to:
- Upload and validate consumption data (CSV/Excel)
- Visualize regional and temporal trends
- Receive AI-driven demand forecasts
- Detect anomalies in consumption patterns
- Collaborate on planning scenarios

## Architecture

- **Frontend**: Next.js, React, Chart.js, Tailwind CSS
- **Backend**: FastAPI, Python
- **ML/AI**: scikit-learn, IsolationForest for anomaly detection, LinearRegression for forecasting
- **Data Processing**: Pandas for data manipulation
- **Deployment**: Designed for GCP (Cloud Run, BigQuery, Cloud Storage)

## Setup

### Prerequisites
- Node.js 18+
- Python 3.8+
- Git

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### ML Models
```bash
cd ml
python train_models.py
```

## Usage

1. Start the backend server on `http://localhost:8000`
2. Start the frontend on `http://localhost:3000`
3. Upload CSV/Excel files with columns: region, timestamp, value
4. View visualizations, forecasts, and anomalies

## API Endpoints

- `POST /api/upload` - Upload consumption data
- `GET /api/forecast?region=<region>&period=<period>` - Get demand forecast
- `GET /api/anomalies` - Get detected anomalies
- `POST /api/scenarios` - Create planning scenario
- `GET /api/users` - List users
- `GET /api/data?region=<region>` - Get consumption data

## Features

- Data upload and validation
- Interactive dashboards with charts
- AI-powered demand forecasting
- Anomaly detection
- Collaborative planning tools
- Role-based access (planned)

## Development

This project is built with modern web technologies and follows best practices for scalability and maintainability.

## License

This project is for demonstration purposes.
