import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        self.slope = None  #(b1)
        self.intercept = None  #(b0)

    def fit(self, X, y, max_steps=1000, learning_rate=0.01):
        X = np.array(X).flatten()
        y = np.array(y).flatten()
        
        # Normalize X and y
        X_mean = np.mean(X)
        X_std = np.std(X)
        y_mean = np.mean(y)
        y_std = np.std(y)

        X_norm = (X - X_mean) / X_std
        y_norm = (y - y_mean) / y_std

        theta = np.zeros((2,))  

        def hypothesis(x, theta):
            return theta[0] + theta[1] * x

        def gradient(X, Y, theta): 
            m = X.shape[0]
            grad = np.zeros((2,))
            for i in range(m):
                x = X[i]
                y_pred = hypothesis(x, theta)
                y = Y[i]
                grad[0] += (y_pred - y)
                grad[1] += (y_pred - y) * x
            return grad / m

        def cost_function(X, Y, theta):
            m = X.shape[0]
            total_error = 0.0
            for i in range(m):
                y_pred = hypothesis(X[i], theta)
                total_error += (y_pred - Y[i]) ** 2
            return total_error / m

        for step in range(max_steps):
            grad = gradient(X_norm, y_norm, theta)
            theta[0] -= learning_rate * grad[0]
            theta[1] -= learning_rate * grad[1]
        
            cost = cost_function(X_norm, y_norm, theta)
            if step % 100 == 0: 
                print(f"Step {step}: Cost = {cost}")

        self.intercept = y_std * theta[0] + y_mean - theta[1] * X_mean * y_std / X_std
        self.slope = theta[1] * y_std / X_std

    def predict(self, X):
        X = np.array(X).flatten()
        return self.slope * X + self.intercept

    def score(self, X, y):
        y_pred = self.predict(X)
        ss_total = np.sum((y - np.mean(y)) ** 2)
        ss_residual = np.sum((y - y_pred) ** 2)
        return 1 - (ss_residual / ss_total)

    @staticmethod
    def r2_score(Y, Y_):
        #sce e pour expliquer
        num = np.sum((Y - Y_) ** 2)
        #sct t pour totale
        denom = np.sum((Y - np.mean(Y)) ** 2)
        return (1 - num / denom) * 100


