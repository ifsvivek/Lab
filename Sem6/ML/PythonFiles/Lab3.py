import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load data
df = pd.read_csv('iris.csv')
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = pd.Categorical(df['species']).codes

# Apply PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Visualize
plt.figure(figsize=(8, 6))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='viridis')
plt.title('PCA on Iris Dataset')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()

# Print the principal components
print("\nPrincipal Components:")
print("PC1:", pca.components_[0])
print("PC2:", pca.components_[1])
