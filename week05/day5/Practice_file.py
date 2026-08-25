import numpy as np

# first_array = np.array([1, 2, 3, 4, 5])
# print(first_array)

# array_1d = np.array([1, 2, 3, 4, 5])
# print("1D_array: ", array_1d)
#
# array_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print("This is a 2d array: \n", array_2d)
#
# print(array_1d.shape)
# print(array_2d.shape)
# print("data type: ", array_1d.dtype)
#
# print(array_2d.size)

# array_1d = np.array([1,2,3,4,5])
# print(array_1d)
# print(array_1d.shape)
# print(array_1d.size)
# print(array_1d.dtype)
#
# array_2d = np.arange(6).reshape(2,3)
# print(array_2d)
# print(array_2d.shape)
# print(array_2d.size)
# print(array_2d.dtype)

# new_array = np.array([1,2,3], dtype=float)
# print(new_array.dtype)

#array_2d = np.array([[1, 2, 3],
#                      [4, 5, 6],
#                      [7, 8, 9]])
# print("Element at row 1, column 2:", array_2d[1, 2])
# print("second row: ", array_2d[1,:])
# print("Third column: ", array_2d[:,2])

# array_2d = np.array([[1, 2, 3],
#                      [4, 5, 6],
#                      [7, 8, 9]])
#
# print("Slice of the array:", array_2d[0:2, 1:3])

# array = np.array([10, 20, 30, 40, 50])
# print("First element:", array[0])
# print("First three elements:", array[:3])

# array = np.array([1,2,3,4,5,6,7,8,9,10])
# print(array[2:8])

# array = np.array([12,23,54,35,46,57])
# print(array[array > 30])
#
# print(array[1:7:2])

import random

# rand = np.random.randint(10, 50, 6)
# print(rand[rand>30])

# x = np.array([1,2,3,4,5,6,7])
# new = np.random.permutation(x)
# print(x)
# print(new)

# two = np.array([[1,2], [3,4], [5,6]])
# newer = np.random.permutation(two)
# print(newer)

import numpy as np

# a = np.array([1,2,3])
# b = np.array([4,5,6])
#
# print(a * 3)

# a = np.array([1, 2, 3])
# result = a + 5
# print(result)

# a = np.array([0, 1, 2])
# b = np.array([[0, 1, 2], [3, 4, 5]])
#
# result = a + b
#
# print("1D Array:", a)
# print("2D Array:", b)
# print("Broadcasted Addition:", result)

# a = np.array([[1], [2], [3]])
# b = np.array([1, 2, 3])
#
# result = a + b
#
# print("Array a:", a)
# print("Array b:", b)
# print("Broadcasted Addition:", result)

import numpy as np

# # Creating two incompatible arrays
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([1, 2])
#
# try:
#     result = a + b
# except ValueError as e:
#     print("Error:", e)

import numpy as np
# # Movie ratings matrix (5 viewers, 3 movies)
# movie_ratings = np.array([
#     [5, 1, 4],  # Viewer 1
#     [4, 4, 2],  # Viewer 2
#     [4, 3, 5],  # Viewer 3
#     [1, 1, 5],  # Viewer 4
#     [3, 2, 1]   # Viewer 5
# ])
#
#
# print("\n--- Movie Ratings Analysis ---")
# print("Ratings Matrix (rows=viewers, cols=movies):\n", movie_ratings)
#
# # 1. Average Rating Calculation (average across viewers, i.e., along axis=0)
# avg_ratings = np.mean(movie_ratings, axis=0)
# print("\n1. Average Rating per Movie:")
# for i, avg in enumerate(avg_ratings):
#     print(f"   Movie {i + 1}: {avg:.1f}")
#
# # 2. Viewer Preference Analysis (highest rated movie per viewer, i.e., along axis=1)
# favorite_movies = np.argmax(movie_ratings, axis=1) + 1  # +1 for 1-based movie numbering
# print(favorite_movies)
# print("\n2. Viewer Preferences (highest-rated movie):")
# for i, movie in enumerate(favorite_movies):
#     print(f"   Viewer {i + 1}: Movie {movie}")
#
# large_array = np.arange(1000000)
# print("C-contiguous:", large_array.flags['C_CONTIGUOUS'])
# print("F-contiguous:", large_array.flags['F_CONTIGUOUS'])
#
# result = large_array + large_array
#
# print(result)
#
# array = np.array([[1,2,3],[4,5,6],[7,8,9]])
#
# print("Mean: ", np.mean(array))
# print("Variance: ", np.var(array))
# print("Standard Deviation: ", np.std(array))
# print("Min: ", np.min(array))
# print("Max: ", np.max(array))
# print("Median: ", np.median(array))
# print("sum: ", np.sum(array))
# print("Count: ", np.count_nonzero(array))



# add_array = array1 + array2
# print("added arrays",add_array)
#
# sub_array = array1 - array2
# print("subtracted arrays",sub_array)
#
# mult_array = array1 * array2
# print("multiplied arrays",mult_array)
#
# div_array = array1 / array2
# print("divided arrays",div_array)
#
# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])
#
# sum_array = np.sum(array1)
# print("sum of array 1: ", sum_array)
# mean_array = np.mean(array1)
# print("mean of array 1: ", mean_array)
# min_array = np.min(array1)
# print("min of array 1: ", min_array)
# max_array = np.max(array1)
# print("max of array 1: ", max_array)
#
# sum_array = np.sum(array2)
# print("sum of array 2: ", sum_array)
# mean_array = np.mean(array2)
# print("mean of array 2: ", mean_array)
# min_array = np.min(array2)
# print("min of array 2: ", min_array)
# max_array = np.max(array2)
# print("max of array 2: ", max_array)
#
# print("Scaled array: ",array2 * 5)
#
# array = np.arange(1, 11)
#
# reshaped_array = array.reshape(5, 2)
# print(reshaped_array)
#
# transposed_array = reshaped_array.transpose()
# print(transposed_array)

# array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print("Array: ", array)
#
# reshaped_array = array.reshape(2,6)
# print("Reshaped Array: ", reshaped_array)
#
# transposed_array = reshaped_array.T
# print("Transposed Array: ", transposed_array)
#
# reshaped_array = array.reshape(3,4)
# print(reshaped_array)
#
# transposed_array = reshaped_array.T
# print(transposed_array)
#
# reshape2 = transposed_array.reshape(-1,order = 'F')
# print(reshape2)
import random

#matrix = np.random.rand(10, 10)
# reshaped_matrix = matrix.reshape(5, 20)
#
# print(reshaped_matrix)

# A = np.array([[1, 2], [3, 4]])
# B = np.array([5, 6])
# product = A.dot(B.transpose())
#
# print(product)

import pandas as pd
import numpy as np

# data = np.array([
#     [5,4,4,1,3],[1,4,3,1,2],[4,2,5,5,1]
# ])
#
# df = pd.DataFrame(data,
#                   index = ["Movies 1", "Movies 2", "Movies 3"],
#                   columns = ["Viewer 1", "Viewer 2", "Viewer 3", "Viewer 4", "Viewer 5"])
#
# print(df)
#
# ave_rate = df.mean(axis=1)
# print(ave_rate)
# max_rate = df.idxmax(axis=0)
# print(max_rate)

# matrix_B = np.array([[2, 3],
#                      [4, 5]])
# matrix_C = np.array([[1, 1],
#                      [1, 1]])
#
# sum_matrix = np.add(matrix_B, matrix_C)
# diff_matrix = np.subtract(matrix_B, matrix_C)
# print(sum_matrix)
# print(diff_matrix)

matrix_1 = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])

matrix_2 = np.array([[10,12,13],
                     [14,15,16],
                     [17,18,19]])

# add_matrix = np.add(matrix_1,matrix_2)
# print(add_matrix)
# subtract_matrix = np.subtract(matrix_1,matrix_2)
# print(subtract_matrix)
# prod_matrix = np.dot(matrix_1,matrix_2)
# print(prod_matrix)
#
# data_1 = np.array([
#     [10,15],[12,18]])
#
# df_1 = pd.DataFrame(data_1, columns=['Product 1','Product 2'])
# print(df_1)
#
# price_matrix = np.array([[10, 15],
#                          [12, 18]])
# quantity_matrix = np.array([[30, 40],
#                             [25, 35]])
#
# # Multiplying matrices to get total sales
# total_sales_matrix = np.dot(price_matrix, quantity_matrix.T)
#
# print("Total Sales Matrix:\n", total_sales_matrix)
# print(quantity_matrix.T)

# data_2 = np.array([
#     [27,24,23,22],[20,18,23,29],[15,20,27,23],[18,17,25,16],[26,19,16,20],[18,22,21,24],[22,21,22,28]
#                    ])
#
# df_2 = pd.DataFrame(data_2,
#                     index= ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'],
#                     columns= ['City 1', 'City 2', 'City 3', 'City 4'])
# print(df_2)
#
# avg_temp = df_2.mean(axis=0)
# print(avg_temp.round(1))
# max_temp_by_day = df_2.idxmax(axis=0)
# print("These days had the highest temp:\n", max_temp_by_day.round(1))
# max_temp_by_city = df_2.idxmax(axis=1)
# print("These cities had the highest temp:\n", max_temp_by_city.round(1))

# sum_day_1 = df_2.loc["Day 1"].sum()
# print(sum_day_1)
# sum_day_7 = df_2.loc["Day 7"].sum()
# print(sum_day_7)
# day_1_day_7_diff = sum_day_1 - sum_day_7
# print(day_1_day_7_diff)

# Annual returns of the investment
# returns = np.array([0.08, 0.12, -0.05, 0.10, 0.07])
#
# # Calculating variance
# variance = np.var(returns)
# print("Variance of the investment returns:", variance * 100)
#
# dates = np.arange('2020-01', '2020-02', dtype='datetime64[D]')
# # print("January 2020 Dates:\n", dates)
#
# ts_data = pd.Series(np.random.randn(100), index=pd.date_range('today', periods=100))
# rolling_mean = ts_data.rolling(window=5).mean()
# print("Rolling Mean:\n", rolling_mean)
#
# # Example: Applying a window function
# window_sum = ts_data.rolling(window=5).sum()
# print("Window Sum:\n", window_sum)
# import numpy as np
# import pandas as pd
# import time
#
# import numpy as np
# import pandas as pd
# import time
#
# # Creating a large DataFrame
# data = pd.DataFrame(np.random.rand(100000, 4), columns=['A', 'B', 'C', 'D'])
#
# # Timing Pandas operations
# start_time = time.time()
# result_pandas = data[(data['A'] > 0.5) & (data['B'] < 0.5)].mean()
# end_time = time.time()
# print("Pandas Conditional Mean:\n", result_pandas)
# print("Pandas Operation Time: {:.5f} seconds".format(end_time - start_time))
#
# Timing equivalent NumPy operations
# numpy_data = data.to_numpy()
# start_time = time.time()
# result_numpy = np.mean(numpy_data[(numpy_data[:, 0] > 0.5) & (numpy_data[:, 1] < 0.5)], axis=0)
# end_time = time.time()
# print("NumPy Conditional Mean:\n", result_numpy)
# print("NumPy Operation Time: {:.5f} seconds".format(end_time - start_time))
#
# import matplotlib.pyplot as plt
#
# # Plotting with NumPy arrays
# plt.plot(data['A'], data['B'], alpha=0.5)
# plt.title("Custom Scatter Plot")
# plt.xlabel("A")
# plt.ylabel("B")
# plt.show()

large_array = np.arange(1000000)

# Inspect memory layout
print("Array size:", large_array.size)
print("Item size:", large_array.itemsize)
print("Memory usage (bytes):", large_array.size * large_array.itemsize)