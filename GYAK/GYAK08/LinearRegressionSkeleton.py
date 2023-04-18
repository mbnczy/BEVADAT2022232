import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
from matplotlib import pyplot as plt

class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        # Building the model
        self.m = 0
        self.c = 0

        self.L = lr  # The learning Rate
        self.epochs = epochs  # The number of iterations to perform gradient descent
    

    def fit(self, X: np.array, y: np.array) -> list: 
        # Split the data into training and testing sets
        #self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        n = float(len(X)) # Number of elements in X

        # Performing Gradient Descent 
        losses = []
        for i in range(self.epochs):
            y_pred = self.m*X + self.c  # The current predicted value of Y

            residuals = y_pred - y
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(X * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            self.m = self.m + self.L * D_m  # Update m
            self.c = self.c + self.L * D_c  # Update c

    def predict(self, X):
        pred = []
        for x in X:
            y_pred = self.m*x + self.c
            pred.append(y_pred)
        return pred
