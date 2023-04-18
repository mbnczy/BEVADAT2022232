# %%
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from matplotlib import pyplot as plt

# %%
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
X = df['petal length (cm)'].values
y = df['petal width (cm)'].values
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
from LinearRegressionSkeleton import LinearRegression
lr = LinearRegression()

# %%
lr.fit(X_train,y_train)

# %%
y_preds = lr.predict(X_test)

# %%
# Making predictions
plt.scatter(X_test, y_test)
plt.plot([min(X_test), max(X_test)], [min(y_preds), max(y_preds)], color='red') # predicted
plt.show()


