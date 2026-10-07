import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for visualizations
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# ==============================================================================
# 1. LOAD & PREPROCESS DATASET
# ==============================================================================
file_path = 'US Superstore data.xls'

# Safe file loading check
if not os.path.exists(file_path):
    # Fallback check for .xlsx extension if .xls is not found
    if os.path.exists('US Superstore data.xlsx'):
        file_path = 'US Superstore data.xlsx'
    else:
        raise FileNotFoundError(
            f"Could not find '{file_path}'. Please ensure the dataset file is in your working directory."
        )

df = pd.read_excel(file_path)

# Handle missing values
df['Postal Code'] = df['Postal Code'].fillna('05401')

# Ensure date fields are in datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Extract Year and Year-Month for Time Series Analysis
df['Order Year'] = df['Order Date'].dt.year
df['Order YearMonth'] = df['Order Date'].dt.to_period('M')

print("Data Preprocessing Complete.")
print(f"Total Rows: {len(df)}, Total Columns: {len(df.columns)}")

# ==============================================================================
# QUESTION 1: Which states have the most sales?
# ==============================================================================
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False)
print("\n--- Top 10 States by Sales ---")
print(state_sales.head(10))

# Visualizing Top 10 States by Sales
plt.figure(figsize=(10, 5))
sns.barplot(x=state_sales.head(10).values, y=state_sales.head(10).index, palette="Blues_r")
plt.title("Top 10 States by Total Sales ($)", fontsize=14, fontweight="bold")
plt.xlabel("Total Sales ($)")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# ==============================================================================
# QUESTION 2: What is the difference between New York and California in sales and profit?
# ==============================================================================
ny_ca = df[df['State'].isin(['New York', 'California'])].groupby('State')[['Sales', 'Profit']].sum()
ny_ca['Profit Margin (%)'] = (ny_ca['Profit'] / ny_ca['Sales']) * 100

print("\n--- New York vs California Comparison ---")
print(ny_ca)

# Visualization
ny_ca_melted = pd.melt(ny_ca.reset_index(), id_vars=['State'], value_vars=['Sales', 'Profit'], var_name='Metric', value_name='Amount')
plt.figure(figsize=(8, 5))
sns.barplot(data=ny_ca_melted, x='State', y='Amount', hue='Metric', palette='Set2')
plt.title("New York vs California: Total Sales & Profit ($)", fontsize=14, fontweight="bold")
plt.ylabel("Amount ($)")
plt.tight_layout()
plt.show()

# ==============================================================================
# QUESTION 3: Who is an outstanding customer in New York?
# ==============================================================================
ny_customers = df[df['State'] == 'New York'].groupby(['Customer ID', 'Customer Name'])[['Sales', 'Profit']].sum()
top_ny_customer = ny_customers.sort_values(by='Sales', ascending=False).head(1)

print("\n--- Outstanding Customer in New York ---")
print(top_ny_customer)

# ==============================================================================
# QUESTION 4: Are there any differences among states in profitability?
# ==============================================================================
state_profit = df.groupby('State')['Profit'].sum().sort_values(ascending=False)
top_5_profitable = state_profit.head(5)
bottom_5_unprofitable = state_profit.tail(5)

print("\n--- Top 5 Most Profitable States ---")
print(top_5_profitable)
print("\n--- Top 5 Least Profitable States ---")
print(bottom_5_unprofitable)

# Visualization: Top vs Bottom States by Profit (Fixed palette syntax issue)
top_bottom_states = pd.concat([state_profit.head(5), state_profit.tail(5)]).reset_index()
top_bottom_states['Type'] = top_bottom_states['Profit'].apply(lambda x: 'Profitable' if x > 0 else 'Unprofitable')

plt.figure(figsize=(10, 5))
sns.barplot(
    data=top_bottom_states, 
    x='Profit', 
    y='State', 
    hue='Type', 
    palette={'Profitable': 'green', 'Unprofitable': 'red'},
    dodge=False
)
plt.title("Top 5 Most and Least Profitable States ($)", fontsize=14, fontweight="bold")
plt.xlabel("Profit ($)")
plt.ylabel("State")
plt.legend(title="Profit Status")
plt.tight_layout()
plt.show()

# ==============================================================================
# QUESTION 5: Pareto Principle on Customers and Profit
# (Determine if 20% of customers contribute to 80% of profit)
# ==============================================================================
cust_profit = df.groupby('Customer ID')['Profit'].sum().sort_values(ascending=False).reset_index()
total_customers = len(cust_profit)
total_profit = cust_profit['Profit'].sum()

top_20_count = int(np.ceil(0.20 * total_customers))
top_20_profit = cust_profit.iloc[:top_20_count]['Profit'].sum()
top_20_profit_pct = (top_20_profit / total_profit) * 100

print(f"\n--- Pareto Principle: Customers & Profit ---")
print(f"Total Unique Customers: {total_customers}")
print(f"Top 20% Customer Count: {top_20_count}")
print(f"Percentage of Total Profit Generated by Top 20% Customers: {top_20_profit_pct:.2f}%")

# Plotting Pareto Cumulative Profit Curve (Fixed syntax error and completed plot)
cust_profit['Cum_Profit'] = cust_profit['Profit'].cumsum()
cust_profit['Cum_Profit_Pct'] = (cust_profit['Cum_Profit'] / total_profit) * 100
cust_profit['Cust_Pct'] = (np.arange(1, total_customers + 1) / total_customers) * 100

plt.figure(figsize=(9, 5))
plt.plot(cust_profit['Cust_Pct'], cust_profit['Cum_Profit_Pct'], color='purple', linewidth=2.5, label='Cumulative Profit %')
plt.axvline(20, color='red', linestyle='--', label='Top 20% Customers')
plt.axhline(80, color='orange', linestyle=':', label='80% Target Profit')
plt.title("Pareto Analysis: Customer Cumulative Profit Curve", fontsize=14, fontweight="bold")
plt.xlabel("% of Customers (Sorted Highest to Lowest Profit)")
plt.ylabel("% of Total Cumulative Profit")
plt.legend(loc='lower right')
plt.grid(True)
plt.tight_layout()
plt.show()

# ==============================================================================
# QUESTION 6: Top 20 Cities by Sales and Top 20 Cities by Profit
# ==============================================================================
city_metrics = df.groupby('City')[['Sales', 'Profit']].sum()

top_20_cities_sales = city_metrics.sort_values(by='Sales', ascending=False).head(20)
top_20_cities_profit = city_metrics.sort_values(by='Profit', ascending=False).head(20)

print("\n--- Top 20 Cities by Sales ---")
print(top_20_cities_sales[['Sales']])

print("\n--- Top 20 Cities by Profit ---")
print(top_20_cities_profit[['Profit']])

# Visualization: Top 10 Cities Comparison
plt.figure(figsize=(12, 5))
sns.barplot(x=top_20_cities_sales.head(10).values.flatten(), y=top_20_cities_sales.head(10).index, palette="Greens_r")
plt.title("Top 10 Cities by Total Sales ($)", fontsize=14, fontweight="bold")
plt.xlabel("Total Sales ($)")
plt.ylabel("City")
plt.tight_layout()
plt.show()

# ==============================================================================
# QUESTION 7: Profitability Differences Among Cities & Top Customers by Sales
# ==============================================================================
city_profit_bottom = city_metrics.sort_values(by='Profit', ascending=True).head(10)
print("\n--- Top 10 Least Profitable Cities ---")
print(city_profit_bottom[['Profit']])

# Top 20 Customers by Total Sales
top_20_cust_sales = df.groupby(['Customer ID', 'Customer Name'])['Sales'].sum().sort_values(ascending=False).head(20)
print("\n--- Top 20 Customers by Sales ---")
print(top_20_cust_sales)

# ==============================================================================
# QUESTION 8: Category & Time-Series Analysis
# ==============================================================================
# Category Breakdown
cat_performance = df.groupby('Category')[['Sales', 'Profit']].sum()
cat_performance['Profit Margin (%)'] = (cat_performance['Profit'] / cat_performance['Sales']) * 100

print("\n--- Product Category Performance ---")
print(cat_performance)

# Monthly Time Series Trend
monthly_ts = df.groupby('Order YearMonth')[['Sales', 'Profit']].sum()
monthly_ts.index = monthly_ts.index.to_timestamp()

plt.figure(figsize=(12, 5))
plt.plot(monthly_ts.index, monthly_ts['Sales'], label='Sales', color='blue', linewidth=2)
plt.plot(monthly_ts.index, monthly_ts['Profit'], label='Profit', color='green', linewidth=2)
plt.title("Sales and Profit Over Time (Monthly Trend)", fontsize=14, fontweight="bold")
plt.xlabel("Order Date")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.show()

# ==============================================================================
# QUESTION 9: Marketing Strategy Recommendations
# ==============================================================================
print("\n==============================================================================")
print("STRATEGIC MARKETING & BUSINESS RECOMMENDATIONS")
print("==============================================================================")
print("""
1. GEOGRAPHIC FOCUS:
   - PRIORITIZE: California and New York show high volume and consistent profit margins.
     Invest heavily in regional marketing and customer loyalty programs here.
   - MITIGATE LOSSES: States like Texas, Ohio, and Pennsylvania show severe losses despite high sales volume.
     Investigate heavy discounting, shipping fees, or regional returns driving these negative margins.

2. CITY LEVEL PRIORITY:
   - Expand localized campaigns in high-margin urban centers like New York City, Los Angeles, and Seattle.
   - Restructure operational pricing in non-profitable cities (e.g., Philadelphia, Houston).

3. CUSTOMER TARGETING:
   - Focus retention campaigns on the top ~20 percent of accounts generating the overwhelming majority of profits.
   - Offer targeted loyalty incentives, personalized account management, and corporate bundling for top spenders.

4. CATEGORY & TIMING:
   - Focus promotions during Q4 (holiday seasonal peak shown in time-series trend) to maximize sales volume.
""")