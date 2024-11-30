from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

# Create the FastAPI app
app = FastAPI()

# Allow specific origins for CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://10.0.2.2:8000",
    "http://192.168.1.100:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the pre-trained regression models
single_feature_model = joblib.load('./trained_model/simple_linear_regression_model.pkl')
multi_feature_model = joblib.load('./trained_model/multi_linear_regression_model.pkl')

# Define the input structure for the single-feature API
class SingleFeatureRequest(BaseModel):
    superficie: float  # Single input feature

class SingleFeatureResponse(BaseModel):
    predicted_price: float

# Define the input structure for the multi-feature API
class MultiFeatureRequest(BaseModel):
    superficie: float  # Feature 1
    secteur: int       # Feature 2

class MultiFeatureResponse(BaseModel):
    predicted_price: float

# Define the single-feature prediction endpoint
@app.post("/predict-single/", response_model=SingleFeatureResponse)
async def predict_single(request: SingleFeatureRequest):
    """
    Predict the price based on a single input feature (superficie).
    """
    # Prepare the input array for the model
    X_new = np.array([[request.superficie]])
    
    # Make predictions using the single-feature model
    predicted_price = single_feature_model.predict(X_new)[0]
    
    # Return the result
    return SingleFeatureResponse(predicted_price=predicted_price)

# Define the multi-feature prediction endpoint
@app.post("/predict-multi/", response_model=MultiFeatureResponse)
async def predict_multi(request: MultiFeatureRequest):
    """
    Predict the price based on multiple input features (superficie and secteur).
    """
    # Prepare the input array for the model
    X_new = np.array([[request.superficie, request.secteur]])
    
    # Make predictions using the multi-feature model
    predicted_price = multi_feature_model.predict(X_new)[0]
    
    # Return the result
    return MultiFeatureResponse(predicted_price=predicted_price)

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
