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
df_4 = pd.DataFrame(np.random.randint(0, 100, size=(5, 3)), columns=['A', 'B', 'C'])
for row in df_4.values:
    for num in row:
        if num % 2 == 0:
            print(num)
sum_df_4 = np.sum(df_4)
print('Sum of DF_4: ', sum_df_4)
mean_df_4 = np.mean(df_4)
print('Mean of DF_4: ', mean_df_4.round())

#Exercise 5 : Image Representation
#An image is composed of a grid of tiny points called pixels (short for picture elements) arranged in rows and columns.
#Because a NumPy array is also organized as a grid of numbers, it serves as the perfect tool for storing these pixel values.
#The structure of the array adapts to the type of image being processed.
#In a grayscale image, each pixel is represented by a single number that indicates its brightness, usually ranging from black to white.
#In a color image, that same pixel is instead represented by three separate numbers corresponding to its Red, Green, and Blue (RGB) color channels.
#By storing these individual values across a structured grid, a NumPy array can efficiently represent and manipulate an entire digital image.

# Black = 0, White = 255, Shades of Grey = all the values inbetween.
import numpy as np
gray_image = np.array([
    [  0,  50, 100, 150, 200],
    [ 25,  75, 125, 175, 225],
    [ 50, 100, 150, 200, 250],
    [ 75, 125, 175, 225, 255],
    [100, 150, 200, 225, 255]
])
print(gray_image)

#Exercise 6 : Basic Hypothesis Testing
import numpy as np
from scipy import stats

np.random.seed(42)
# Productivity scores of employees before the training program
productivity_before = np.random.normal(loc=50, scale=10, size=30)
# Productivity scores of the same employees after the training program
productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)

t_statistic, p_value = stats.ttest_rel(productivity_after, productivity_before, alternative='greater')

print(f"t_statistic: {t_statistic:.4f}\n p_value: {p_value:.4e}")

alpha = 0.05

print("\n --Hypothesis Test Conclusion--")
if p_value < alpha:
    print("reject null hypothesis")
    print("There is significant evidence that the training program helps.")
else:
    print("reject null hypothesis")
    print("There is no significant evidence that the training program helps.")

#Exercise 7 : Complex Array Comparison
import numpy as np
array_one = np.array([1, 2, 30, 4, 50, 6, 7, 80, 9])
array_two = np.array([10, 20, 3, 40, 5, 60, 70, 8, 90])
comparison = array_one < array_two
print(comparison)

#Exercise 8 : Time Series Data Manipulation
import numpy as np
import pandas as pd
dates = np.arange('2023-01', '2023-12', dtype='datetime64[D]')
print(dates)

mask_1 = (dates >= np.datetime64('2023-01')) & (dates <= np.datetime64('2023-03'))
jan_mar = dates[mask_1].astype('datetime64')
print('All dates between January and March: \n', jan_mar)

mask_2 = (dates >= np.datetime64('2023-04')) & (dates <= np.datetime64('2023-06'))
apr_jun = dates[mask_2].astype('datetime64')
print('All dates between April and June: \n',apr_jun)

mask_3 = (dates >= np.datetime64('2023-07')) & (dates <= np.datetime64('2023-09'))
jul_sep = dates[mask_3].astype('datetime64')
print('All dates between July and September: \n',jul_sep)

mask_4 = (dates >= np.datetime64('2023-10')) & (dates <= np.datetime64('2023-12'))
oct_dec = dates[mask_4].astype('datetime64')
print('All dates between October and December: \n',oct_dec)

#Exercise 9 : Data Conversion
import numpy as np
import pandas as pd

array_9 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array_9)

df_9 = pd.DataFrame(array_9)
print(df_9)

#Exercise 10 : Basic Visualization
import numpy as np
import matplotlib.pyplot as plt
import random

dataset_10 = pd.DataFrame(np.random.randint(0, 100, size=(10, 3)), columns=['A', 'B', 'C'])
print(dataset_10)

plt.plot(dataset_10)
plt.xlabel('A')
plt.ylabel('B')
plt.title('Basic Visualization')
plt.legend()
plt.show()
