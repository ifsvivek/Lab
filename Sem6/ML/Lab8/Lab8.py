"""Converted from Lab8.ipynb"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

data = load_breast_cancer()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
elf = DecisionTreeClassifier(random_state=42)
elf.fit(X_train, y_train)
y_pred = elf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy :{accuracy*100:.2f}%")
new_sample = np.array([X_test[0]])
prediction = elf.predict(new_sample)
prediction_class = "Benign" if prediction == 1 else "Malignant"
print(f"predicted class for the new sample is {prediction_class}")
plt.figure(figsize=(12, 8))
tree.plot_tree(
    elf, filled=True, feature_names=data.feature_names, class_names=data.target_names
)
plt.title("Decision Tree-Breast Cancer Dataset")
plt.show()