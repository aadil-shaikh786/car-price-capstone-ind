from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os
from tensorflow.keras.models import load_model

# Load model and scaler from /models
model = load_model("models/car_price_model.keras")
scaler = joblib.load("models/scaler.pkl")

# Init app
app = FastAPI(title="Car Price Prediction API")

# Input format
class CarFeatures(BaseModel):
    annual_income: float
    engine: float
    gender: int
    transmission: int
    dealer_region: int

@app.post("/predict")
def predict(features: CarFeatures):
    try:
        input_data = np.array([[features.annual_income, features.engine, features.gender,
                                features.transmission, features.dealer_region]])
        scaled_data = scaler.transform(input_data)
        prediction = model.predict(scaled_data)
        return {"predicted_price": round(float(prediction[0][0]), 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
