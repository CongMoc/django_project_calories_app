import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            y_predicted = np.dot(X, self.weights) + self.bias

            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1/n_samples) * np.sum(y_predicted - y)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted

# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.array([[1, 2, 3, 4, 5]]).T
    y = np.array([2, 4, 5, 4, 5])

    # Create a LinearRegression object and fit the model
    model = LinearRegression(learning_rate=0.01, n_iterations=1000)
    model.fit(X, y)

    # Make predictions
    X_test = np.array([[6, 7, 8]]).T
    predictions = model.predict(X_test)
    print(predictions)