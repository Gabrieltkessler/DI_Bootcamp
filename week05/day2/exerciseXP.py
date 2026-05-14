from scipy import stats
import numpy as np


# Exercise 1: Basic Usage of SciPy
print(scipy.__version__)


# Exercise 2: Descriptive Statistics
# Using numpy
data = [12, 15, 13, 12, 18, 20, 22, 21]

mean_data = np.mean(data)
print(f"The mean is {mean_data:.0f}")

median_data = np.median(data)
print(f"The median is {median_data:.0f}")

var_data = np.var(data)
print(f"The variance is {var_data:.0f}")

std_data = np.std(data)
print(f"The standard deviation is {std_data:.0f}")

# Using scipy
mean = stats.tmean(data)
median = stats.scoreatpercentile(data, 50)
variance = stats.tvar(data)
std_dev = stats.tstd(data)

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std_dev)


# Exercise 3: Understanding Distributions
# Task: Generate a normal distribution using SciPy with a mean of 50 and a standard deviation of 10. Plot this distribution.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean = 50
std_dev = 10

x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)

# Generate the normal distribution (PDF)
y = norm.pdf(x, mean, std_dev)

# Plot the distribution
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Normal Distribution', color='blue')
plt.title('Normal Distribution (mean=50, std=10)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)

plt.show()

# Exercise 4: T-Test Application

data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 10, 100)

t_stat,p_value = stats.ttest_ind(data1, data2)

print(f"T-statistic:, {t_stat}")
print(f"P-value:, {p_value}")

# Exercise 5: Linear Regression Analysis

house_sizes = np.array([50, 70, 80, 100, 120])
house_prices = np.array([150000, 200000, 210000, 250000, 280000])

slope, intercept = np.polyfit(house_sizes, house_prices, 1)

print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")

predicted_price = slope * 90 + intercept

print(f"The price prediction for a 90 square-foot house is: ${predicted_price:.2f}")

import matplotlib.pyplot as plt

plt.scatter(house_sizes, house_prices, label='Data Points')
plt.plot(house_sizes, slope * house_sizes + intercept, color='red', label='Linear Regression Line')
plt.xlabel('House Size (sq. ft.)')
plt.ylabel('House Price ($)')
plt.title('Linear Regression Analysis')
plt.legend()

plt.show()

# Exercise 6: Understanding ANOVA

fertilizer_1 = [5, 6, 7, 6, 5]
fertilizer_2 = [7, 8, 7, 9, 8]
fertilizer_3 = [4, 5, 4, 3, 4]

f_value, p_value = stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)

print(f"F-statistic: {f_value}")
print(f"P-value: {p_value:.10f}")