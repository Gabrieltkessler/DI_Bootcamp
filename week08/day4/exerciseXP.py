import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc

# Loading in the dataset using the whole local path
df = pd.read_csv(r'C:\Users\gabri\Documents\Practice files\Diabetes prediction dataset\diabetes_prediction_dataset.csv')
# We are going to try a Logistic Regression model for this problem because it is great for binary classification like Diabetes or not.

# Doind some one_hot_encoding
df = pd.get_dummies(df, columns=['gender', 'smoking_history'])

X = df[['bmi', 'blood_glucose_level']]
Y = df['diabetes']
X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

# Doing some scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Training the model
model = LogisticRegression()
model.fit(X_train, Y_train)

# defining the plotting area
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1

# creating the drid of points
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 200),
    np.linspace(y_min, y_max, 200)
)

# Flattening the grid and predict
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# The plotting

plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X_train[:, 0], X_train[:, 1], c=Y_train, edgecolor='k')
plt.show()

# Adding the curve
fpr, tpr, thresholds = roc_curve(Y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6,5))

plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0, 1], [0, 1], linestyle="--")  # random model line

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()

plt.show()

# print(df.shape)
# print(df.head(10))
# print(df.dtypes)
# print("Missing per column:")
# print(df.isna().sum().sort_values(ascending=False))
# print(df.describe())
# print(df['diabetes'].sum(), "positive cases")
# print((df['diabetes'] == 0).sum(), "negative cases")
