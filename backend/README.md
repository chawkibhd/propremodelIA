# Backend README

## Overview

This backend application is a machine learning service built with **Python** that provides predictions for land prices using both **single-feature** and **multi-feature regression models**. It supports training, serving, and using pre-trained models via APIs. The project utilizes **FastAPI** for the backend server, **joblib** for model serialization, and includes necessary tools for preprocessing and training.

---

## Project Structure

```plaintext
backend/
├── data/                      # Data files used for training and testing
│   ├── Combined_DataSets.xlsx
│   ├── DataSets_01.xlsx
│   ├── DataSets_02.xlsx
│   ├── Prix-Moyen-Au-m²-Algerie.xlsx
│
├── experimental/              # Jupyter notebooks for model training and experimentation
│   ├── multi_feature_training.ipynb
│   ├── single_feature_training.ipynb
│
├── model/                     # Python modules for machine learning models
│   ├── __init__.py
│   ├── MultiLinearRegression.py
│   ├── SimpleLinearRegression.py
│
├── trained_model/             # Pre-trained regression models
│   ├── multi_linear_regression_model.pkl
│   ├── simple_linear_regression_model.pkl
│
├── .gitignore                 # Ignored files/folders for Git
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
```

---

## Features

### 1. **Single-Feature Regression**
- Predicts land prices based on a single feature: `superficie`.
- Model trained using `SimpleLinearRegression`.

### 2. **Multi-Feature Regression**
- Predicts land prices based on multiple features: `superficie` and `secteur`.
- Model trained using `MultiLinearRegression`.

### 3. **APIs**
- Exposes endpoints via **FastAPI** for single-feature and multi-feature predictions:
  - **Single Feature**: `/predict-single`
  - **Multi-Feature**: `/predict-multi`

---

## Models Explained

### 1. **SimpleLinearRegression**
#### Overview:
This is a custom implementation of a linear regression model built from scratch. It is designed to handle a single input feature (`superficie`) and predict the target variable (`prix`).

#### Formula:
The model predicts the price using the equation:
\[
y = b_0 + b_1x
\]
Where:
- \(y\): Predicted price.
- \(b_0\): Intercept (bias term).
- \(b_1\): Slope (weight for `superficie`).
- \(x\): Input feature (`superficie`).

#### Training:
- Uses **gradient descent** to minimize the mean squared error (MSE) between predicted and actual prices.
- Normalizes data to improve optimization stability.

#### Advantages:
- Lightweight and easy to interpret.
- Custom-built, providing complete control over the training process.

---

### 2. **MultiLinearRegression**
#### Overview:
This model is an extension of linear regression that can handle multiple input features, such as `superficie` and `secteur`. It predicts the target variable using a weighted sum of the input features.

#### Formula:
The model predicts the price using the equation:
\[
y = b_0 + b_1x_1 + b_2x_2
\]
Where:
- \(y\): Predicted price.
- \(b_0\): Intercept (bias term).
- \(b_1, b_2\): Coefficients (weights) for `superficie` and `secteur`.
- \(x_1, x_2\): Input features (`superficie`, `secteur`).

#### Training:
- Uses **gradient descent** for optimization.
- Requires preprocessing to encode categorical features (e.g., `secteur` is encoded as `0` for "campagne" and `1` for "ville").
- Trains the model to minimize prediction errors.

#### Advantages:
- Can model relationships involving multiple features.
- Provides flexibility for more complex datasets.

---

## APIs

### Single Feature Prediction

**Endpoint**: `/predict-single`  
**Method**: `POST`  
**Request Body**:
```json
{
    "superficie": 120.5
}
```

**Response**:
```json
{
    "predicted_price": 2500000.0
}
```

---

### Multi-Feature Prediction

**Endpoint**: `/predict-multi`  
**Method**: `POST`  
**Request Body**:
```json
{
    "superficie": 120.5,
    "secteur": "ville"
}
```

**Response**:
```json
{
    "predicted_price": 3000000.0
}
```

---

## How to Use

### Prerequisites
1. Install **Python 3.8+**.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Start the FastAPI Server
```bash
uvicorn app:app --reload
```
- Server will run at `http://127.0.0.1:8000`.

### Access Swagger UI
Open your browser and navigate to:
```
http://127.0.0.1:8000/docs
```

---

## Model Training

### **Jupyter Notebooks**
- Use `experimental/single_feature_training.ipynb` for single-feature model training.
- Use `experimental/multi_feature_training.ipynb` for multi-feature model training.

### **Model Saving**
Models are serialized using `joblib` and stored in the `trained_model/` folder:
```python
joblib.dump(model, './trained_model/simple_linear_regression_model.pkl')
joblib.dump(model, './trained_model/multi_linear_regression_model.pkl')
```