import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


df = pd.read_csv(r'Breast_Cancer_Diagnostic.csv')
df = df.dropna(axis=1, how='all')

x = df.drop(['id', 'diagnosis'], axis=1)
y = df['diagnosis']

sns.countplot(data=df,x='diagnosis')
# plt.show()

# print(df['diagnosis'].unique())

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Implement logistic regression and print the accuracy.
lr_model = LogisticRegression(max_iter=5000, random_state=42)
lr_model.fit(X_train_scaled, y_train)
lr_acc = accuracy_score(y_test, lr_model.predict(X_test_scaled))
print(f'Logistic Regression Accuracy: {lr_acc:.4f}')

# Implement K Nearest Neighbours and print the accuracy.
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)
knn_acc = accuracy_score(y_test, knn_model.predict(X_test_scaled))
print(f'KNN Accuracy: {knn_acc:.4f}')

# Implement Random Forests and print the accuracy.
rfc_model = RandomForestClassifier(n_estimators=100, random_state=42)
rfc_model.fit(X_train, y_train)
rfc_acc = accuracy_score(y_test, rfc_model.predict(X_test))
print(f'Random Forest Accuracy: {rfc_acc:.4f}')

# Implement Support Vector Machines (SVM) and print the accuracy.
svc_model = SVC(random_state=42)
svc_model.fit(X_train_scaled, y_train)
svc_acc = accuracy_score(y_test, svc_model.predict(X_test_scaled))
print(f'SVC Accuracy: {svc_acc:.4f}')

# Which is the best model ?
#SVC came back with the highest accuracy score (0.9825), making it the best model for this dataset.
