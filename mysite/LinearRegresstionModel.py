import numpy as np

class LinearRegression:
    def __init__(self):
        self.coefficients = None
        self.intercept = None
        self.age = 0.0

    def fit(self, X, y):
        ones_column = np.ones((X.shape[0], 1))
        X = np.concatenate((ones_column, X), axis=1)
        self.coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
        self.intercept = self.coefficients[0]

    def Check_Age(self,age,gender):
        if gender == 1:
            self.age = age * 6.755
        else:
            self.age = age *4.6756

    def predict(self, X):
        ones_column = np.ones((X.shape[0], 1))
        X = np.concatenate((ones_column, X), axis=1)
        return X.dot(self.coefficients) - self.age

    def get_coefficients(self):
        return self.coefficients
    
    def get_intercept(self):
        return self.intercept
