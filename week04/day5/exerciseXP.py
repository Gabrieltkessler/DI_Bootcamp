# Exercise 1: Duplicate Detection and Removal
import pandas as pd

df = pd.read_csv('train.csv')
titanic_data = df.drop_duplicates()
print(titanic_data.duplicated().sum())

# Exercise 2: Handling Missing Values
from sklearn.impute import SimpleImputer
import pandas as pd

df = pd.read_csv('train.csv')
missing_data = df.isnull()
#print(missing_data.head())
#print(df.isnull().sum())

df = df.dropna()
print(df.isnull().sum())

# Exercise 3: Feature Engineering
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("train.csv")

# Create Family Size
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Extract Title
df["Title"] = df["Name"].str.split(",").str[1].str.split(".").str[0].str.strip()

# One hot encode categorical variables
df = pd.get_dummies(df, columns=["Sex", "Embarked", "Title"])

print(df.head())

# Exercise 4: Outlier Detection and Handling
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("train.csv")

plt.hist(df['Age'].dropna(), bins=20)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.boxplot(df['Age'])
plt.title('Age Boxplots')
plt.show()

plt.hist(df['Fare'].dropna(), bins=20)
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

plt.boxplot(df['Fare'])
plt.title('Age Boxplots')
plt.show()

Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
print(outliers)

upper_cap = df['Fare'].quantile(0.98)

df['Fare_capped'] = np.where(df['Fare'] > upper_cap, upper_cap, df['Fare'])

df_removed = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]

plt.boxplot(df["Fare"])
plt.title("Original Fare")
plt.show()

plt.boxplot(df["Fare_capped"])
plt.title("Capped Fare")
plt.show()

# Exercise 5: Data Standardization and Normalization
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
import numpy as np

standard_cols = ["Age"]

minmax_cols = ["Fare"]

df["Age"] = df["Age"].fillna(df["Age"].median())

standard_scaler = StandardScaler()

df[standard_cols] = standard_scaler.fit_transform(df[standard_cols])

minmax_scaler = MinMaxScaler()

df[minmax_cols] = minmax_scaler.fit_transform(df[minmax_cols])

print(df[["Age", "Fare"]].head())

# Exercise 6: Feature Encoding
import pandas as pd

df = pd.read_csv("train.csv")

df["Embarked"] = df["Embarked"].fillna("Unknown")

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

df["Title"] = (
    df["Name"]
    .str.split(",")
    .str[1]
    .str.split(".")
    .str[0]
    .str.strip()
)

print(df.select_dtypes(include="object").columns)

df = pd.get_dummies(
    df,
    columns=["Sex", "Embarked", "Cabin"]
)

# Check result
print(df.head())

# Exercise 7: Data Transformation for Age Feature

import pandas as pd

# Ensure Age has no missing values
df["Age"] = df["Age"].fillna(df["Age"].median())

# Create age groups
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 60, 100],
    labels=["Child", "Teen", "Adult", "Senior"]
)

# One hot encode
df = pd.get_dummies(df, columns=["AgeGroup"])

print(df.head())
