"""Converted from Lab3.ipynb"""

# Develop a program to implement Principal Component Analysis (PCA) for reducing the dimensionality of
# the Iris dataset from 4 features to 2. 

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


iris = load_iris()

print("iris data")
print(iris.data)
print("\n iris target")
print(iris.target)

plt.figure(figsize=(8, 6))
X_reduced = PCA(n_components=2).fit_transform(iris.data)
scatter = plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=iris.target)
plt.title("PCA on Iris Dataset (4 -> 2)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

handles, labels = scatter.legend_elements()
plt.legend(handles, iris.target_names, title="Classes")
plt.grid()
plt.show()