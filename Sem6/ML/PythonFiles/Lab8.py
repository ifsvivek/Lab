import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load data
df = pd.read_csv('breast_cancer.csv')
X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train decision tree
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.3f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Feature importance
feature_importance = clf.feature_importances_
top_features = sorted(zip(X.columns, feature_importance), key=lambda x: x[1], reverse=True)[:5]

plt.figure(figsize=(10, 6))
features, importance = zip(*top_features)
plt.barh(features, importance)
plt.title('Top 5 Feature Importance')
plt.xlabel('Importance')
plt.show()