
## Linear Regression Categories,Encapsulated through categories (Class)

import numpy as np

class ManualLinearRegression:
    """
    A manual implementation of Linear Regression using Gradient Descent.
    This class supports multiple features and encapsulates the training process.
    """
    def __init__(self, learning_rate=0.01, iterations=1000):
        """
        Initialize the model with hyperparameters.
        :param learning_rate: The step size at each iteration for gradient descent.
        :param iterations: The number of times to iterate through the training set.
        """
        self.lr = learning_rate
        self.iterations = iterations
        self.theta = None       # Model weights (including intercept)
        self.cost_history = []  # To track the Mean Squared Error (MSE) over time

    def fit(self, X, y):
        """
        Train the model using the provided training data.
        :param X: Feature matrix (numpy array).
        :param y: Target values (numpy array).
        """
        m = len(y)
        
        # Add a column of ones to X to account for the intercept (bias term)
        # This transforms the equation to: y = theta0 * 1 + theta1 * x1 + ...
        X_final = np.c_[np.ones(X.shape[0]), X]
        
        # Initialize weights (theta) as zeros. 
        # The size is equal to the number of features + 1 (for the intercept).
        self.theta = np.zeros(X_final.shape[1])

        for i in range(self.iterations):
            # 1. Calculate predictions: h(x) = X * theta
            predictions = np.dot(X_final, self.theta)
            
            # 2. Calculate errors: (h(x) - y)
            errors = predictions - y
            
            # 3. Calculate gradients: (1/m) * X.T * errors
            # This points in the direction of the steepest increase of the cost function
            gradient = (1 / m) * np.dot(X_final.T, errors)
            
            # 4. Update weights: Move in the opposite direction of the gradient
            self.theta = self.theta - self.lr * gradient
            
            # 5. Compute cost (MSE) for monitoring convergence
            # Using (1/2m) as it simplifies the derivative during the gradient calculation
            current_cost = (1 / (2 * m)) * np.sum((np.dot(X_final, self.theta) - y) ** 2)
            self.cost_history.append(current_cost)
            
            # Optional: Print progress every 100 iterations
            if i % 100 == 0:
                print(f"Iteration {i}: Cost = {current_cost:.6f}")

    def predict(self, X):
        """
        Make predictions using the trained linear model.
        :param X: New feature matrix for prediction.
        :return: Predicted target values.
        """
        # Ensure the input X also has the intercept column added
        X_final = np.c_[np.ones(X.shape[0]), X]
        
        # Return the dot product of data and learned weights
        return np.dot(X_final, self.theta)