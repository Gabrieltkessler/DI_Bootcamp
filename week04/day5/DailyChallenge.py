import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

#load dataset
df = pd.read_csv('datascience_salaries.csv')
#print(df.head())
#print(df.info())

#normalizing salary
scaler = MinMaxScaler()
df['normalized_salary'] = scaler.fit_transform(df[['salary']])
#print(df[['salary', 'normalized_salary']].head())

#Preparing PCA
numeric_df = df.select_dtypes(include=np.number)
numeric_df = numeric_df.fillna(numeric_df.mean())

pca = PCA(n_components=2)
pca_result = pca.fit_transform(numeric_df)

pca_df = pd.DataFrame(
    pca_result,
    columns=["PC1", "PC2"]
)
print(pca_df.head())

salary_stats = df.groupby("experience_level")["salary"].agg(
    ["mean", "median"]
)
print(salary_stats)