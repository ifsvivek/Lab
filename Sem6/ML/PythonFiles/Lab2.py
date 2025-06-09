import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("housing.csv")

# Basic info
print(f"Shape: {df.shape}")
print(df.describe())

# Correlation matrix
corr_matrix = df.corr(numeric_only=True)
print(f"\nHighest correlations with target:")
print(corr_matrix['target'].sort_values(ascending=False))

# Visualize correlation
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()

# Display the correlation matrix
print("\nCorrelation Matrix:")
print(corr_matrix)

# Create heatmap of correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

# Create pairplot for all features
sns.pairplot(df)
plt.suptitle('Pairplot of All Features', y=1.02)
plt.show()
