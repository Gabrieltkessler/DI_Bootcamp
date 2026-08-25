import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('US Superstore data.xls')

# Task number 1: Which states have the most sales?
states_array = df['State'].values

states, counts = np.unique(states_array, return_counts=True)

plt.figure(figsize=(12,6))
plt.bar(states, counts, color=['red'])
plt.xticks(rotation=90)
plt.xlabel('States')
plt.ylabel('Sales')
plt.title('Which State Has The Most Sales')
plt.show()

# task number 2: Find difference between New York and California in terms of sales and profit

ny_sales = df[df['State'] == 'New York']['Sales'].sum()
ca_sales = df[df['State'] == 'California']['Sales'].sum()

ny_profit = df[df['State'] == 'New York']['Profit'].sum()
ca_profit = df[df['State'] == 'California']['Profit'].sum()

ny_diff_sales = ny_sales - ca_sales
ny_diff_profit = ny_profit - ca_profit

absolute_ny_diff_sales = abs(ny_diff_sales)
absolute_ny_diff_profit = abs(ny_diff_profit)

print(f"Difference between New York and California in terms of sales:, {absolute_ny_diff_sales:.2f}")
print(f"Difference between New York and California in terms of profit:, {absolute_ny_diff_profit:.2f}")

# Difference between New York and California in terms of sales:, 146811.36
# Difference between New York and California in terms of profit:, 2342.84

# task number 3: Find an outstanding customer in New York.

outstanding_customer = df[df['State'] == 'New York'].groupby('Customer Name')['Profit'].sum().idxmax()
outstanding_customer_profit = df['Profit'].sum().max()
print(f"The outstanding customer in New York is: {outstanding_customer} \n He brought the company ${outstanding_customer_profit:.2f} USD in profit")

# The outstanding customer in New York is: Tom Ashbrook
#  He brought the company $286397.02 USD in profit

# Are there any differences among states in profitability?
# Are there any differences among states in profitability?

state_profit = df.groupby('State')['Profit'].sum()

plt.figure(figsize=(12,6))
plt.bar(state_profit.index, state_profit)
plt.xticks(rotation=90)
plt.xlabel('States')
plt.ylabel('Profit')
plt.title('Profitability Among States')
plt.show()

