import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Load data from CSV
data = pd.read_csv("housing.csv")
X, y = data[["MedInc"]], data["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train models
linear_pred = LinearRegression().fit(X_train, y_train).predict(X_test)
poly_pred = make_pipeline(PolynomialFeatures(3), LinearRegression()).fit(X_train, y_train).predict(X_test)

# Visualize results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(X_test, y_test, color='blue', label='Actual', alpha=0.6)
ax1.plot(X_test, linear_pred, color='red', label='Predicted')
ax1.set_title('Linear Regression')
ax1.legend()

ax2.scatter(X_test, y_test, color='blue', label='Actual', alpha=0.6)
ax2.scatter(X_test, poly_pred, color='red', label='Predicted', alpha=0.6)
ax2.set_title('Polynomial Regression')
ax2.legend()

plt.tight_layout()
plt.show()
