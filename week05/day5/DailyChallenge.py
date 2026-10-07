import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Load Dataset
df = pd.read_excel('US Superstore data.xls')

# 1. Check Missing Values & Data Integrity
print("Missing Values:\n", df.isnull().sum())

# Clean missing postal code (e.g., Burlington, Vermont)
df['Postal Code'] = df['Postal Code'].fillna('05401')

# 2. Date Formatting
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# 3. Extract Date Features
df['Year'] = df['Order Date'].dt.year
df['Year_Month'] = df['Order Date'].dt.to_period('M').astype(str)

print(f"Data Date Range: {df['Order Date'].min().date()} to {df['Order Date'].max().date()}")

# Aggregate sales by Year-Month
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum().reset_index()
monthly_sales['Order Date'] = monthly_sales['Order Date'].dt.to_timestamp()

# Interactive Line Chart with Plotly / Matplotlib integration
fig_trend = px.line(
    monthly_sales, 
    x='Order Date', 
    y='Sales', 
    title='Interactive Sales Trend Over Time (2014 - 2017)'
)