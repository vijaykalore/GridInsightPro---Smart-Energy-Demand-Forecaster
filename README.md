# GridInsightPro - Smart Energy Demand Forecaster

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)](https://nodejs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-green.svg)](https://fastapi.tiangolo.com)
[![Next.js](https://img.shields.io/badge/Next.js-15+-black.svg)](https://nextjs.org)

A comprehensive web application for energy providers to forecast demand using big data and AI. Built with modern technologies and designed for scalability.

## 🌟 Features

- **📊 Data Upload & Validation** - Secure upload of CSV/Excel files up to 10GB
- **📈 Interactive Visualization** - Real-time charts with Chart.js and D3.js
- **🤖 AI-Powered Forecasting** - Machine learning models for demand prediction
- **🔍 Anomaly Detection** - Automated identification of unusual consumption patterns
- **📋 Collaborative Planning** - Scenario planning and team collaboration tools
- **🔐 Role-Based Access** - Admin, Analyst, and Viewer permissions
- **📱 Responsive Design** - Works seamlessly on desktop and mobile devices

## 🚀 Live Demo

The application is currently running and can be accessed at:
- **Frontend**: [http://localhost:3001](http://localhost:3001)
- **Backend API**: [http://localhost:8000](http://localhost:8000)
- **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## 📖 Overview

GridInsightPro enables energy providers to:
- Upload and validate large datasets (up to 10GB) in CSV/Excel formats
- Visualize regional and temporal consumption trends
- Receive AI-driven demand forecasts with high accuracy
- Detect anomalies in consumption patterns
- Collaborate on grid management strategies
- Access role-based permissions and audit logs

## 🏗️ Architecture

The application follows a modern microservices architecture:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Next.js       │    │   FastAPI       │    │   PostgreSQL    │
│   Frontend      │◄──►│   Backend       │◄──►│   Database      │
│                 │    │   API           │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Chart.js      │    │   ML Models     │    │   Cloud Storage │
│   Visualization │    │   (Scikit-learn)│    │   (GCP/AWS)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Technology Stack

### Frontend
- **Framework**: Next.js 15+ with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Charts**: Chart.js, React-Chart.js-2
- **HTTP Client**: Axios

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.8+
- **ML/AI**: Scikit-learn, Pandas, NumPy
- **File Handling**: python-multipart
- **CORS**: python-multipart

### DevOps & Deployment
- **Containerization**: Docker (planned)
- **CI/CD**: GitHub Actions (planned)
- **Cloud**: GCP (BigQuery, Cloud Storage, Cloud Run)
- **Version Control**: Git

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- **Python 3.8 or higher**
- **Node.js 18 or higher**
- **Git**
- **Virtual Environment** (recommended)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/vijaykalore/GridInsightPro---Smart-Energy-Demand-Forecaster.git
cd GridInsightPro---Smart-Energy-Demand-Forecaster
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the backend server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Frontend Setup
```bash
# Open new terminal and navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

## 📖 Usage

### 1. Access the Application
- Open your browser and go to: **http://localhost:3001**

### 2. Upload Data
1. Click **"Choose File"** button
2. Select a CSV file with columns: `region`, `timestamp`, `value`
3. Click **"Upload"** button
4. Wait for successful upload confirmation

### 3. Explore Features
- **Load Data**: Click to fetch and display consumption data
- **View Charts**: Interactive line charts show consumption patterns
- **Get Forecast**: AI-powered demand predictions
- **Detect Anomalies**: Identify unusual consumption patterns

### 4. API Testing
Access the interactive API documentation at: **http://localhost:8000/docs**

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/upload` | Upload consumption data files |
| GET | `/api/data` | Retrieve consumption data |
| GET | `/api/forecast?region=<region>&period=<period>` | Get demand forecast |
| GET | `/api/anomalies` | Get detected anomalies |
| POST | `/api/scenarios` | Create planning scenario |
| GET | `/api/users` | List users and roles |

## 📁 Project Structure

```
GridInsightPro---Smart-Energy-Demand-Forecaster/
├── frontend/                 # Next.js React application
│   ├── src/
│   │   ├── app/             # Next.js app router pages
│   │   └── components/      # React components
│   ├── public/              # Static assets
│   └── package.json         # Frontend dependencies
├── backend/                  # FastAPI Python server
│   ├── main.py              # Main application file
│   ├── requirements.txt     # Python dependencies
│   └── venv/                # Virtual environment
├── ml/                      # Machine learning models
│   ├── train_models.py      # Model training script
│   └── models/              # Trained model files
├── docs/                    # Documentation
│   ├── PRD.md              # Product Requirements Document
│   ├── HLD.md              # High Level Design
│   └── LLD.md              # Low Level Design
├── data_processing/         # Data processing scripts
├── sample_energy_data.csv   # Sample dataset
└── README.md               # This file
```

## 📸 Screenshots

*Add your screenshots here showing the application in action*

### Dashboard View
![Dashboard](screenshots/dashboard.png)

### Data Upload
![Data Upload](screenshots/upload.png)

### Visualization
![Visualization](screenshots/charts.png)

### Forecast Results
![Forecast](screenshots/forecast.png)

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you have any questions or need help:

- 📧 **Email**: [your-email@example.com]
- 🐛 **Issues**: [GitHub Issues](https://github.com/vijaykalore/GridInsightPro---Smart-Energy-Demand-Forecaster/issues)
- 📖 **Documentation**: Check the `/docs` folder

## 🎯 Roadmap

- [ ] Docker containerization
- [ ] Database integration (PostgreSQL)
- [ ] User authentication and authorization
- [ ] Real-time data streaming
- [ ] Advanced ML models (TensorFlow)
- [ ] Cloud deployment (GCP/AWS)
- [ ] Mobile application
- [ ] API rate limiting and security

---

**Built with ❤️ for the energy sector**

⭐ Star this repository if you find it useful!
