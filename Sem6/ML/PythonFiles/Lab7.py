import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

# Load data
df = pd.read_csv('housing.csv')
X = df[['MedInc']]
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Linear regression
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)
y_pred_linear = linear_reg.predict(X_test)

# Polynomial regression
poly_reg = make_pipeline(PolynomialFeatures(2), LinearRegression())
poly_reg.fit(X_train, y_train)
y_pred_poly = poly_reg.predict(X_test)

# Results
print(f"Linear MSE: {mean_squared_error(y_test, y_pred_linear):.3f}")
print(f"Polynomial MSE: {mean_squared_error(y_test, y_pred_poly):.3f}")

# Visualize
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_test, y_test, alpha=0.5)
plt.scatter(X_test, y_pred_linear, alpha=0.5)
plt.title('Linear Regression')

plt.subplot(1, 2, 2)
plt.scatter(X_test, y_test, alpha=0.5)
plt.scatter(X_test, y_pred_poly, alpha=0.5)
plt.title('Polynomial Regression')

plt.show()
