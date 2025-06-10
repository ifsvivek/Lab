import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing.csv")

print(f"Dataset Shape: {df.shape}")
print(f"\nDataset Description:")
print(df.describe())

corr_matrix = df.corr(numeric_only=True)
print(f"\nHighest correlations with target:")
print(corr_matrix["target"].sort_values(ascending=False))

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0, square=True, fmt=".2f")
plt.title("Correlation Matrix - California Housing Dataset")
plt.tight_layout()
plt.show()

sns.pairplot(df, diag_kind="kde")
plt.suptitle("Pairwise Relationships - California Housing Dataset", y=1.02)
plt.tight_layout()
plt.show()
