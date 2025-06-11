import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

data = pd.read_csv("breast_cancer.csv")
X, y = data.drop("diagnosis", axis=1), data["diagnosis"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
clf = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)

accuracy = accuracy_score(y_test, clf.predict(X_test))
print(f"Model accuracy: {accuracy*100:.2f}%")

prediction_class = "Benign" if clf.predict([X_test.iloc[0]]) == 1 else "Malignant"
print(f"Predicted class for sample: {prediction_class}")

plt.figure(figsize=(12, 8))
tree.plot_tree(
    clf, filled=True, feature_names=X.columns.tolist(), class_names=sorted(y.unique())
)
plt.title("Decision Tree - Breast Cancer Dataset")
plt.show()
