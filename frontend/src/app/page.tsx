'use client'

import { useState } from 'react'
import axios from 'axios'
import { Line } from 'react-chartjs-2'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

export default function Home() {
  const [file, setFile] = useState<File | null>(null)
  const [uploadStatus, setUploadStatus] = useState('')
  const [forecast, setForecast] = useState<any>(null)
  const [anomalies, setAnomalies] = useState<any[]>([])
  const [data, setData] = useState<any[]>([])

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = event.target.files?.[0]
    if (selectedFile) {
      setFile(selectedFile)
    }
  }

  const uploadFile = async () => {
    if (!file) return

    const formData = new FormData()
    formData.append('file', file)

    try {
      setUploadStatus('Uploading...')
      const response = await axios.post('http://localhost:8000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      setUploadStatus('File uploaded successfully!')
      console.log('Upload response:', response.data)
    } catch (error: any) {
      setUploadStatus(`Upload failed: ${error.response?.data?.detail || error.message}`)
      console.error('Upload error:', error)
      console.error('Error response:', error.response?.data)
    }
  }

  const getForecast = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/forecast?region=North&period=24h')
      setForecast(response.data.forecast)
    } catch (error) {
      console.error(error)
    }
  }

  const getAnomalies = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/anomalies')
      setAnomalies(response.data.anomalies)
    } catch (error) {
      console.error(error)
    }
  }

  const getData = async () => {
    try {
      setUploadStatus('Loading data...')
      const response = await axios.get('http://localhost:8000/api/data')
      setData(response.data.data)
      setUploadStatus('Data loaded successfully!')
      console.log('Data response:', response.data)
    } catch (error: any) {
      setUploadStatus(`Failed to load data: ${error.response?.data?.detail || error.message}`)
      console.error('Data loading error:', error)
      console.error('Error response:', error.response?.data)
    }
  }

  const chartData = {
    labels: data.map(d => d.timestamp),
    datasets: [
      {
        label: 'Consumption',
        data: data.map(d => d.value),
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
      },
    ],
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-600 text-white p-4">
        <h1 className="text-2xl font-bold">GridInsightPro - Smart Energy Demand Forecaster</h1>
      </header>
      
      <div className="flex">
        <nav className="w-64 bg-gray-800 text-white p-4">
          <ul>
            <li className="mb-2"><a href="#" className="block p-2 hover:bg-gray-700">Dashboard</a></li>
            <li className="mb-2"><a href="#" className="block p-2 hover:bg-gray-700">Upload Data</a></li>
            <li className="mb-2"><a href="#" className="block p-2 hover:bg-gray-700">Visualization</a></li>
            <li className="mb-2"><a href="#" className="block p-2 hover:bg-gray-700">Forecast</a></li>
            <li className="mb-2"><a href="#" className="block p-2 hover:bg-gray-700">Anomalies</a></li>
          </ul>
        </nav>
        
        <main className="flex-1 p-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="bg-white p-6 rounded-lg shadow">
              <h2 className="text-xl font-semibold mb-4">Data Upload</h2>
              <input type="file" accept=".csv,.xlsx" onChange={handleFileUpload} className="mb-4" />
              <button onClick={uploadFile} className="bg-blue-500 text-white px-4 py-2 rounded">Upload</button>
              <p className="mt-2">{uploadStatus}</p>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow">
              <h2 className="text-xl font-semibold mb-4">Actions</h2>
              <button onClick={getData} className="bg-green-500 text-white px-4 py-2 rounded mr-2">Load Data</button>
              <button onClick={getForecast} className="bg-purple-500 text-white px-4 py-2 rounded mr-2">Get Forecast</button>
              <button onClick={getAnomalies} className="bg-red-500 text-white px-4 py-2 rounded">Detect Anomalies</button>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow md:col-span-2">
              <h2 className="text-xl font-semibold mb-4">Consumption Visualization</h2>
              {data.length > 0 ? (
                <Line data={chartData} />
              ) : (
                <p>No data loaded. Click "Load Data" to fetch consumption data.</p>
              )}
            </div>
            
            {forecast && (
              <div className="bg-white p-6 rounded-lg shadow">
                <h2 className="text-xl font-semibold mb-4">Forecast</h2>
                <p>Region: {forecast.region}</p>
                <p>Predicted Value: {forecast.predicted_value.toFixed(2)}</p>
              </div>
            )}
            
            <div className="bg-white p-6 rounded-lg shadow">
              <h2 className="text-xl font-semibold mb-4">Anomalies ({anomalies.length})</h2>
              {anomalies.length > 0 ? (
                <ul>
                  {anomalies.slice(0, 5).map((anomaly, index) => (
                    <li key={index}>Anomaly detected at data point {anomaly.data_id}, severity: {anomaly.severity}</li>
                  ))}
                </ul>
              ) : (
                <p>No anomalies detected.</p>
              )}
            </div>
          </div>
        </main>
      </div>
    </div>
  )
}
