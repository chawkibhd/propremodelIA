from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = joblib.load('./simple_linear_regression_model.pkl')

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

handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)