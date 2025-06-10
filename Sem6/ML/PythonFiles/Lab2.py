import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load California Housing dataset
df = pd.read_csv("housing.csv")

# Basic dataset information
print(f"Dataset Shape: {df.shape}")
print(f"\nDataset Description:")
print(df.describe())

# Compute correlation matrix
corr_matrix = df.corr(numeric_only=True)
print(f"\nHighest correlations with target:")
print(corr_matrix['target'].sort_values(ascending=False))

# Visualize correlation matrix using heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, fmt='.2f')
plt.title('Correlation Matrix - California Housing Dataset')
plt.tight_layout()
plt.show()

# Create pairplot to visualize pairwise relationships
sns.pairplot(df, diag_kind='kde')
plt.suptitle('Pairwise Relationships - California Housing Dataset', y=1.02)
plt.tight_layout()
plt.show()
