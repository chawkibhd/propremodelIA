import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin

class MultiLinearRegression(BaseEstimator, RegressorMixin):
    def __init__(self, max_steps=1000, learning_rate=0.01):
        self.max_steps = max_steps
        self.learning_rate = learning_rate
        self.intercept_ = None
        self.coefficients_ = None

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y).flatten()
        
        # Normalize features and target variable
        self.x_mean_ = np.mean(X, axis=0)
        self.x_std_ = np.std(X, axis=0)
        self.y_mean_ = np.mean(y)
        self.y_std_ = np.std(y)

        X_normalized = (X - self.x_mean_) / self.x_std_
        y_normalized = (y - self.y_mean_) / self.y_std_

        m_samples, n_features = X_normalized.shape
        parameters = np.zeros(n_features + 1)

        def hypothesis(features, params):
            return params[0] + np.dot(features, params[1:])

        def compute_gradient(features, targets, params):
            predictions = hypothesis(features, params)
            errors = predictions - targets
            gradient = np.zeros_like(params)
            gradient[0] = np.sum(errors) / m_samples
            gradient[1:] = np.dot(errors, features) / m_samples
            return gradient

        for step in range(self.max_steps):
            gradients = compute_gradient(X_normalized, y_normalized, parameters)
            parameters -= self.learning_rate * gradients

        self.intercept_ = self.y_std_ * parameters[0] + self.y_mean_ - np.dot(parameters[1:], self.x_mean_ * self.y_std_ / self.x_std_)
        self.coefficients_ = (parameters[1:] * self.y_std_) / self.x_std_

        return self

    def predict(self, X):
        X = np.array(X)
        return np.dot(X, self.coefficients_) + self.intercept_

    def score(self, X, y):
        y_pred = self.predict(X)
        ss_total = np.sum((y - np.mean(y)) ** 2)
        ss_residual = np.sum((y - y_pred) ** 2)
        return 1 - (ss_residual / ss_total)

    def get_params(self, deep=True):
        """Get parameters for this estimator."""
        return {"max_steps": self.max_steps, "learning_rate": self.learning_rate}

    def set_params(self, **params):
        """Set parameters for this estimator."""
        for key, value in params.items():
            setattr(self, key, value)
        return self
