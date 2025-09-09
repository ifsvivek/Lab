"""Converted from Lab9.ipynb"""

# Program - 9
# Develop a program to implement the Naive Bayesian
# classifier considering Olivetti face data set for
# training. Compute the accuracy of the classifier,
# considering a few test datasets.

from sklearn.datasets import fetch_olivetti_faces
faces = fetch_olivetti_faces()
import matplotlib.pyplot as plt

x = faces.data
y = faces.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x_train, y_train)
y_pred = gnb.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)

# Code from the second image
print(f"Accuracy of Naive Bayes Classifier on Olivetti faces dataset: {accuracy*100:.2f}%")

# code to display faces 
n_samples=10
plt.figure(figsize=(60,10))

for i in range(n_samples):
    ax= plt.subplot(2, n_samples, i + 1)
    plt.imshow(x_test[i].reshape(64, 64), cmap=plt.cm.gray)
    plt.title(f"Predicted: {y_pred[i]}\nTrue: {y_test[i]}")
    plt.axis('off')
plt.show()