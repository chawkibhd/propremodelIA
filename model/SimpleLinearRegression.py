import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        self.slope = None  # Coefficient (b1)
        self.intercept = None  # Intercept (b0)

    def fit(self, X, y, max_steps=100, learning_rate=0.1):
        X = np.array(X)
        y = np.array(y)
        
        # Normalize X and y
        X_mean = np.mean(X)
        X_std = np.std(X)
        y_mean = np.mean(y)
        y_std = np.std(y)

        X = (X - X_mean) / X_std
        y = (y - y_mean) / y_std

        theta = np.zeros((2,))  # Initialize parameters

        def hypothesis(x, theta):
            return theta[0] + theta[1] * x

        def gradient(X, Y, theta): 
            m = X.shape[0]
            grad = np.zeros((2,))
            for i in range(m):
                x = X[i]
                y_ = hypothesis(x, theta)
                y = Y[i]
                grad[0] += (y_ - y)
                grad[1] += (y_ - y) * x
            return grad / m

        def cost_function(X, Y, theta):
            m = X.shape[0]
            total_error = 0.0
            for i in range(m):
                y_pred = hypothesis(X[i], theta)
                total_error += (y_pred - Y[i]) ** 2
            return total_error / m

        for step in range(max_steps):
            grad = gradient(X, y, theta)
            theta[0] -= learning_rate * grad[0]
            theta[1] -= learning_rate * grad[1]
        
            # Calculate cost for debugging or visualization
            cost = cost_function(X, y, theta)
            if step % 100 == 0:  # Print cost every 100 steps
                print(f"Step {step}: Cost = {cost}")

        self.intercept = theta[0] * y_std + y_mean
        self.slope = theta[1] * (y_std / X_std)


    def predict(self, X):
        """
        Predict the target values using the fitted model.
        X: array-like, shape (n_samples,)
        Returns: array-like, predicted values
        """
        X = np.array(X)
        return self.slope * X + self.intercept

    def score(self, X, y):
        """
        Calculate the R-squared value to evaluate the model.
        X: array-like, shape (n_samples,)
        y: array-like, shape (n_samples,)
        Returns: float, R-squared value
        """
        y_pred = self.predict(X)
        ss_total = np.sum((y - np.mean(y)) ** 2)
        ss_residual = np.sum((y - y_pred) ** 2)
        return 1 - (ss_residual / ss_total)

    @staticmethod
    def r2_score(Y, Y_):
        """
        Calculate the R-squared value for given true and predicted values.
        Y: array-like, true values
        Y_: array-like, predicted values
        Returns: float, R-squared value
        """
        num = np.sum((Y - Y_) ** 2)
        denom = np.sum((Y - np.mean(Y)) ** 2)
        return (1 - num / denom) * 100


