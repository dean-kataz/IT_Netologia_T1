# -*- coding: windows-1251 -*-
# ������ ����������� ���������
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# �������� �������� iris
iris = load_iris()
X = iris.data[:, :2]  # ���������� ������ ��� ��������: sepal_length � sepal_width
y = iris.target       # ������� ����������

# ���������� ������ �� ��������� � �������� �������
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ���������� ������ LDA
lda = LDA()
lda.fit(X_train, y_train)
y_pred = lda.predict(X_test)

# ������ ������� accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of LDA model: {accuracy:.2f}")

if accuracy > 0.7:
    print("Accuracy is greater than 0.7, which meets the criterion.")
else:
    print("Accuracy does not meet the criterion.")

# ������������ ������������ � ������� �������
plt.figure(figsize=(10, 6))
colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
    plt.scatter(X_test[y_test == i, 0], X_test[y_test == i, 1], color=color, label=f'Class {i} (True)')
    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1], color=color, marker='x', label=f'Class {i} (Predicted)')

# ������ �������
class_centers = lda.means_
plt.scatter(class_centers[:, 0], class_centers[:, 1], color='black', marker='o', s=100, label='Class Centers')

plt.title('LDA Classification')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.grid(True)
plt.show()

# ������������ ������� ���������� ��� �������������
X = iris.data[:, :2]  # ��� ��������: sepal_length � sepal_width

# ������ ������������ ����� ��������� � �������������� ���������� �������
silhouette_scores = []
k_values = range(2, 10)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    score = silhouette_score(X, kmeans.labels_)
    silhouette_scores.append(score)

# ������������ ���������� �������
plt.figure(figsize=(10, 6))
plt.plot(k_values, silhouette_scores, marker='o')
plt.title('Silhouette Analysis')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.grid(True)
plt.show()

# ����� ������������ ����� ��������� (������������ �������� ���������� ������������)
optimal_k = k_values[np.argmax(silhouette_scores)]
print(f'Optimal number of clusters: {optimal_k}')

if optimal_k == len(np.unique(y)):
    print("The optimal number of clusters matches the number of classes in the target variable.")
else:
    print("The optimal number of clusters does not match the number of classes in the target variable.")

# ������������� � ����������� ������ ���������
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(X)

# ������������ �������������
plt.figure(figsize=(10, 6))
for i in range(optimal_k):
    plt.scatter(X[kmeans.labels_ == i, 0], X[kmeans.labels_ == i, 1], label=f'Cluster {i}')

# ������ ���������
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black', marker='x', s=100, label='Cluster Centers')

plt.title('KMeans Clustering')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.grid(True)
plt.show()