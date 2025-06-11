import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("breast_cancer.csv")

df = data.copy()
x = df.iloc[:, 0:-1]

kmeans = KMeans(n_clusters=2, random_state=42).fit(x)

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
