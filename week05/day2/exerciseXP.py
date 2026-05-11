# Exercise 1: Basic Usage of SciPy
import scipy
print(scipy.__version__)

# Exercise 2: Descriptive Statistics
import numpy as np
from scipy import stats

data = [12, 15, 13, 12, 18, 20, 22, 21]

mean_data = np.mean(data)
print(f"The mean is {mean_data}")

median_data = np.median(data)
print(f"The median is {median_data}")

var_data = np.var(data)
print(f"The variance is {var_data}")

std_data = np.std(data)
print(f"The standard deviation is {std_data}")


mean = stats.tmean(data)
median = stats.scoreatpercentile(data, 50)
variance = stats.tvar(data)
std_dev = stats.tstd(data)

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std_dev)