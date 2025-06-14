"""Converted from Lab7.ipynb"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

dataset = fetch_california_housing(as_frame=True)
df = pd.DataFrame(dataset.data)

x = df[["MedInc"]] 
y = dataset.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42) 

from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)
y_pred = linear_reg.predict(X_test)

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

poly = make_pipeline(PolynomialFeatures(degree=3), LinearRegression())
poly.fit(X_train, y_train)
y_pred_poly = poly.predict(X_test)

plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test["MedInc"], y_pred, color='red', label='Predicted')
plt.title("Linear Regression")
plt.legend()
plt.show()

plt.scatter(X_test, y_test, color='blue', label="Actual")
plt.scatter(X_test, y_pred_poly, color='red', label="Predicted")
plt.title("Polynomial Regression")
plt.legend()
plt.show()
