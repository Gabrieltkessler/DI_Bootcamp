import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Exercise 1 : Matrix Operations
matrix_one = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
determinant = np.linalg.det(matrix_one)
print(determinant)
# inv_matrix = np.linalg.inv(matrix_one)
# print(inv_matrix) #can't find the inverse because the determinant is 0.

#Exercise 2 : Statistical Analysis
import random
from scipy import stats

array_one = random.sample(range(50), 50)
mean_array_one = np.mean(array_one)
median_array_one = np.median(array_one)
std_array_one = np.std(array_one)

print("Mean: \n", mean_array_one)
print("Median: \n", median_array_one)
print("Standard Deviation: \n", std_array_one.round(2))

#Exercise 3 : Date Manipulation
jan_dates = np.arange('2023-01-01','2023-02-01', dtype='datetime64')
print(jan_dates)

new_format = jan_dates.astype('str')
new_format = np.char.replace(new_format,'-', '/')
print(new_format)

#Exercise 4 : Data Manipulation with NumPy and Pandas
