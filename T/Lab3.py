import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

iris = pd.read_csv("iris.csv")
X = iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = pd.Categorical(iris["species"]).codes

plt.figure(figsize=(8, 6))
X_reduced = PCA(n_components=2).fit_transform(X)
scatter = plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap="viridis")
plt.title("PCA on Iris Dataset (4 -> 2)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

handles, labels = scatter.legend_elements()
plt.legend(handles, iris["species"].unique(), title="Classes")
plt.grid()
plt.show()
