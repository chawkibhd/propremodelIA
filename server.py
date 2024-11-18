from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://10.0.2.2:8000",
    "http://192.168.1.100:8000",  # Replace with your local IP address
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Charger le modèle pré-entraîné
model = joblib.load('simple_linear_regression_model.pkl')

class PredictionRequest(BaseModel):
    superficie: float

class PredictionResponse(BaseModel):
    predicted_price: float

@app.post("/predict/", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    # Faire des prédictions en utilisant le modèle pré-entraîné
    X_new = np.array([[request.superficie]])
    predicted_price = model.predict(X_new)[0]
    return PredictionResponse(predicted_price=predicted_price)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)