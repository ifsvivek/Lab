"""Converted from Lab10.ipynb"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.datasets import load_breast_cancer
import warnings

warnings.filterwarnings("ignore")

# Load the breast cancer dataset instead of CSV
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

# Use all features except target for clustering
x = df.iloc[:, 0:-1]

# Fix the variable naming - use one consistent name
kmeans = KMeans(n_clusters=2, random_state=42)

kmeans.fit(x)
pred = kmeans.predict(x)

print(x.iloc[:, 0])
print(x.iloc[:, 1])

plt.scatter(x.iloc[:, 0], x.iloc[:, 1], c=pred, cmap="viridis", marker="o")
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=100,
    c="red",
    marker="*",
)

plt.xlabel("mean radius")
plt.ylabel("mean texture")
plt.show()