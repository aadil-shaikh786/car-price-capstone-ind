# 🚗 Car Price Prediction API

This project demonstrates a full machine learning deployment pipeline for predicting car prices using customer and vehicle data. It includes model training, Dockerization, deployment to Google Cloud Run, and serving predictions via a FastAPI endpoint.

---

## 📌 Project Overview

- **Objective**: Predict the price of a car based on features like company, model, engine type, transmission, and customer demographics.
- **Tools & Frameworks**:
  - Python (Pandas, NumPy, TensorFlow/Keras, Scikit-learn)
  - FastAPI for API serving
  - Docker for containerization
  - Google Cloud Run for deployment
  - Google Container Registry (GCR) for image storage

---

## 🧠 Machine Learning Model

- **Model**: Neural Network built with Keras
- **Input Features**: Car company, model, engine, transmission, color, region, customer income, gender
- **Target**: Car Price (USD)
- **Artifacts**:
  - `car_price_model.keras`
  - `scaler.pkl` (for feature scaling)

---

## 🧪 API Usage

Once deployed, send a POST request to the `/predict` endpoint.

### Sample Payload

```json
{
  "features": [
    [65000, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
  ]
}
```

### Sample Response

```json
{
  "predictions": [20999.87]
}
```

---

## 🚀 Deployment Pipeline

### Architecture

```text
Local Dev → Docker Image → GCR → Cloud Run → Public API
```

![Deployment Architecture](assets/deployment_diagram.png)

---

## 🛠️ Local Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/aadil-shaikh786/car-price-capstone-ind.git
cd car-price-capstone-ind
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Locally

```bash
uvicorn app:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI

---

## 🐳 Docker Instructions

### Build the Docker Image

```bash
docker build -t car-price-api .
```

### Run the Container

```bash
docker run -p 8080:8080 car-price-api
```

---

## ☁️ Google Cloud Deployment

### 1. Authenticate with Google Cloud

```bash
gcloud auth login
gcloud config set project carprice-capstone-ind
```

### 2. Build & Push Image

```bash
gcloud builds submit --tag gcr.io/carprice-capstone-ind/car-price-api
```

### 3. Deploy to Cloud Run

```bash
gcloud run deploy car-price-api   --image gcr.io/carprice-capstone-ind/car-price-api   --platform managed   --region us-central1   --allow-unauthenticated   --memory 1Gi
```

---

## 🌐 Live API Endpoint

**🔗 URL**: [https://car-price-api-481594874299.us-central1.run.app](https://car-price-api-481594874299.us-central1.run.app)

---

## 📷 Screenshots

Add the following images in a folder named `assets/` in your repo:
- `deployment_diagram.png` – architecture diagram
- Screenshot of Swagger UI
- Screenshot of API test response

---

## 📈 Future Improvements

- Add authentication for secure API access
- Deploy frontend UI to interact with the API
- Use Vertex AI or Cloud Functions for scalability
- Monitor usage with Google Cloud Logging & Monitoring

---

## 👨‍💻 Author

**Mohammed Aadil Shaikh**  
Graduate Certificate in AI – Seneca Polytechnic  
[LinkedIn](https://www.linkedin.com/in/mohammedaadilshaikh) | [GitHub](https://github.com/aadil-shaikh786)