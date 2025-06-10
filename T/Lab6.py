import numpy as np
import matplotlib.pyplot as plt


def gaussian_kernel(x, x_query, tau):
    return np.exp(-((x - x_query) ** 2) / (2 * tau**2))


def locally_weighted_regression(X, y, x_query, tau):
    X_b = np.c_[np.ones((len(X))), X]
    x_query_b = np.array([1, x_query])
    W = np.diag(gaussian_kernel(X, x_query, tau))
    theta = np.linalg.inv(X_b.T @ W @ X_b) @ X_b.T @ W @ y
    return x_query_b @ theta


X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 3, 2, 4, 3.5, 5, 6, 7, 6.5, 9])

X_query = np.linspace(1, 10, 100)
tau = 1.0
y_lwr = np.array([locally_weighted_regression(X, y, xq, tau) for xq in X_query])


plt.figure(figsize=(8, 6))
plt.scatter(X, y, color="blue", label="Training Data")
plt.plot(X_query, y_lwr, color="red", label="LWR Prediction")
plt.title("Locally Weighted Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
