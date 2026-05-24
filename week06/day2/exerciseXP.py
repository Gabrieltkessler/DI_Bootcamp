#Exercise 1 : Array Creation and Manipulation
import numpy as np
array_1 = np.arange(0,10)
print(array_1)

#Exercise 2 : Type Conversion and Array Operations
list_1 = [3.14, 2.17, 0, 1, 2]
array_2 = np.array(list_1)
print(array_2)

#Exercise 3 : Working with Multi-Dimensional Arrays
array_3 = np.arange(1,10)
array_3 = array_3.reshape(3,3)
print(array_3)

#Exercise 4 : Creating Multi-Dimensional Array with Random Numbers
import random
array_4 = np.random.random(20)
print(array_4)

array_4 = array_4.reshape(4,5)
print(f"4x5 array: \n{array_4}")

#Exercise 5 : Indexing Arrays
array_5 = np.arange(1,21)
array_5 = array_5.reshape(4,5)
print(array_5)
print(array_5[1])

#Exercise 6 : Reversing elements
array_6 = np.arange(1,21)
print(array_6[::-1])

#Exercise 7 : Identity Matrix
array_7 = np.arange(1,17)
array_7 = array_7.reshape(4,4)
print(array_7)
print(array_7.shape)

#Exercise 8 : Simple Aggregate Funcs
array_8 = np.arange(1,17)
array_sum = np.sum(array_8)
array_mean = np.mean(array_8)
print(array_8)
print(array_sum)
print(array_mean)

#Exercise 9 : Create Array and Change its Structure
array_9 = np.arange(1,21)
array_9 = array_9.reshape(4,5)
print(array_9)

#Exercise 10 : Conditional Selection of Values

array_10 = np.arange(1,21)
array_odd_num = array_10[array_10 % 2 != 0]
print(array_odd_num)