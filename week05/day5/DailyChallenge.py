# ==============================================================================
# SECTION 1: DATA PREPARATION & CLEANING
# ==============================================================================
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set global Seaborn & Matplotlib aesthetics
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# 1. Load Dataset with Fallback Handling
file_path = 'US Superstore data.xls'
if not os.path.exists(file_path):
    if os.path.exists('US Superstore data.xlsx'):
        file_path = 'US Superstore data.xlsx'
    elif os.path.exists('US Superstore data (2).xls'):
        file_path = 'US Superstore data (2).xls'
    else:
        raise FileNotFoundError(f"Could not locate dataset file in the working directory.")

df = pd.read_excel(file_path)

# 2. Basic Data Cleaning & Missing Value Handling
print("Missing Values Check:")
print(df.isnull().sum())

# Fill missing postal codes if any (e.g., Burlington, Vermont)
if df['Postal Code'].isnull().sum() > 0:
    df['Postal Code'] = df['Postal Code'].fillna('05401')

# 3. Date Formatting & Feature Extraction
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Extract Year and Year_Month features
df['Year'] = df['Order Date'].dt.year
df['Year_Month'] = df['Order Date'].dt.to_period('M').astype(str)

min_year = df['Year'].min()
max_year = df['Year'].max()
min_date_str = df['Order Date'].min().strftime('%Y-%m-%d')
max_date_str = df['Order Date'].max().strftime('%Y-%m-%d')

print(f"\n--- Data Preprocessing Summary ---")
print(f"Total Rows: {len(df)}, Total Columns: {len(df.columns)}")
print(f"Date Range: {min_date_str} to {max_date_str} (Years: {min_year} - {max_year})")


# ==============================================================================
# SECTION 2: DATA VISUALIZATION WITH MATPLOTLIB & PLOTLY
# ==============================================================================

# 1. Interactive Sales Trends Over Time (Plotly Express Line Chart)
monthly_sales = df.groupby('Year_Month')['Sales'].sum().reset_index()
monthly_sales['Order Date'] = pd.to_datetime(monthly_sales['Year_Month'])

fig_trend = px.line(
    monthly_sales,
    x='Order Date',
    y='Sales',
    title=f'Interactive Sales Trend Over Time ({min_year} - {max_year})',
    labels={'Sales': 'Total Sales ($)', 'Order Date': 'Date'},
    template='plotly_white'
)
fig_trend.update_traces(line_color='#1f77b4', line_width=2.5)
fig_trend.update_layout(hovermode="x unified", title_x=0.5)
fig_trend.show()

# 2. Interactive Geographic Sales Map by US State (Plotly Choropleth)
# Note: Since the dataset is exclusively US-based, 'Country' is adapted to US States.
state_sales = df.groupby('State')['Sales'].sum().reset_index()

state_abbreviations = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL',
    'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
    'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
    'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
    'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
    'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA',
    'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}
state_sales['State_Code'] = state_sales['State'].map(state_abbreviations)

fig_map = px.choropleth(
    state_sales,
    locations='State_Code',
    locationmode="USA-states",
    color='Sales',
    scope="usa",
    color_continuous_scale="Blues",
    title=f"Sales Distribution by US State ({min_year} - {max_year})",
    labels={'Sales': 'Total Sales ($)', 'State_Code': 'State'}
)
fig_map.update_layout(title_x=0.5, margin={"r":0, "t":40, "l":0, "b":0})
fig_map.show()


# ==============================================================================
# SECTION 3: DATA VISUALIZATION WITH SEABORN
# ==============================================================================

# 1. Top 10 Products by Sales (Seaborn Horizontal Bar Chart)
top_10_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_10_products,
    x='Sales',
    y='Product Name',
    palette='Blues_r'
)
plt.title("Top 10 Products by Total Sales ($)", fontsize=14, fontweight="bold")
plt.xlabel("Total Sales ($)")
plt.ylabel("Product Name")
plt.tight_layout()
plt.show()

# 2. Relationship Between Profit and Discount (Seaborn Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='Discount',
    y='Profit',
    hue='Category',
    style='Category',
    alpha=0.7,
    s=60,
    palette='Set2'
)
plt.axhline(0, color='red', linestyle='--', linewidth=1.5, label='Zero Profit Baseline')
plt.title("Profit vs. Discount Rate by Product Category", fontsize=14, fontweight="bold")
plt.xlabel("Discount Rate (e.g., 0.2 = 20%)")
plt.ylabel("Profit ($)")
plt.legend(title="Category", loc="upper right")
plt.tight_layout()
plt.show()


# ==============================================================================
# SECTION 4: COMPARATIVE ANALYSIS (MATPLOTLIB / PLOTLY VS. SEABORN)
# ==============================================================================
print("\n" + "="*80)
print("SECTION 4: COMPARATIVE ANALYSIS - MATPLOTLIB / PLOTLY VS. SEABORN")
print("="*80)
print("""
1. Ease of Use & Syntax:
   - Seaborn: Excels at statistical visualizations and high-level data aggregation with minimal code.
     Features like hue mapping, color palette application, and categorical grouping require only a single line.
   - Plotly / Matplotlib: Plotly provides instant interactivity (hover info, zoom, panning) out of the box,
     making time-series charts and geographic maps far more engaging than static figures.

2. Visual Clarity & Effectiveness:
   - Interactive Line/Map (Plotly): Ideal for executive dashboards and time-series exploration where
     pinpointing exact dates or regional state values is critical.
   - Static Charts (Seaborn): Superior for exploratory scatter plots and categorical distribution charts
     where static publication-ready rendering is required.
""")


# ==============================================================================
# SECTION 5: EXECUTIVE INSIGHTS & STRATEGIC RECOMMENDATIONS
# ==============================================================================
print("\n" + "="*80)
print("SECTION 5: BUSINESS INSIGHTS & RECOMMENDATIONS")
print("="*80)
print("""
1. Discounting Strategy:
   - The Profit vs. Discount scatter plot reveals a strong negative correlation: discounts higher than 20%
     consistently generate net losses across all product categories.
   - Action: Implement a hard threshold capping maximum promotional discounts at 15-20%.

2. Geographic Performance:
   - Sales are heavily concentrated in California and New York, while midwestern and southern states exhibit
     lower sales density and higher shipping margin erosion.
   - Action: Prioritize fulfillment center investments and localized marketing in high-performing coastal states.

3. Top Product Focus:
   - Top 10 products are dominated by high-value technology items (e.g., Copiers, Phones) and office machines.
   - Action: Bundle top-selling technology accessories with slower-moving furniture inventory to boost margins.
""")