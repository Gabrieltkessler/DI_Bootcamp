# Mini-project: Advanced Statistical Analysis of Apple Inc. Stock Data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
from scipy import stats

# loading dataset via pandas
df = pd.read_csv(r'C:\Users\gabri\Documents\Practice files\Apple Stock Prices From 1981 to 2023\Apple Stock Prices (1981 to 2023).csv')
print(df.head())
# checking for null values
df_null = df.isnull().sum()
print('null values: ', df_null)

# Visualizing the data

import pandas as pd
import mplfinance as mpf

df = pd.read_csv(r'C:\Users\gabri\Documents\Practice files\Apple Stock Prices From 1981 to 2023\Apple Stock Prices (1981 to 2023).csv')

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df.set_index('Date', inplace=True)
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

mpf.plot(
    df.tail(500),
    type='candle',
    volume=True,
    style='yahoo',
    figsize=(12, 8)
)

# Statistical Analysis

avg_close= df['Close'].mean()
median_close= df['Close'].median()
std_close= df['Close'].std()
print('Average Close price: ',avg_close.round(2))
print('Median Close price: ',median_close.round(2))
print('Standard Deviation of Close price: ',std_close.round(2))

df['MA_3'] = df['Close'].rolling(window=3).mean()

print("\nData with Moving Average:")
print(df)

# Hypothesis Testing

import pandas as pd
from scipy import stats

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df["Year"] = df["Date"].dt.year

close_2020 = df[df["Year"] == 2020]["Close"].dropna()
close_2023 = df[df["Year"] == 2023]["Close"].dropna()

t_stat, p_value = stats.ttest_ind(close_2020, close_2023, equal_var=False)

print("T-statistic:", t_stat)
print("P-value:", p_value)

import matplotlib.pyplot as plt

df["Return"] = df["Close"].pct_change()

plt.hist(df["Return"], bins=50)
plt.title("Daily Returns Distribution")
plt.show()