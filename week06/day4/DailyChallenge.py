import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ==========================================
# 1. DATA IMPORT AND CLEANING
# ==========================================

# Import the dataset
df = pd.read_csv('global_power_plant_database.csv', low_memory=False)

# Identify numerical columns for analysis
num_cols = ['capacity_mw', 'latitude', 'longitude', 'commissioning_year', 'generation_gwh_2017']

# Use NumPy/Pandas to convert relevant columns to numeric types
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Check missing values count
missing_summary = df.isnull().sum()
print("--- Missing Values Summary ---")
print(missing_summary[missing_summary > 0].head(10))

# Clean commissioning year by masking unrealistic values (keeping 1900-2020)
df_clean = df.copy()
df_clean.loc[(df_clean['commissioning_year'] < 1900) | (df_clean['commissioning_year'] > 2020), 'commissioning_year'] = np.nan


# ==========================================
# 2. EXPLORATORY DATA ANALYSIS
# ==========================================

# Summarize key statistics (mean, median, standard deviation) using Pandas/NumPy
eda_stats = pd.DataFrame({
    'Mean': np.nanmean(df_clean[num_cols], axis=0),
    'Median': np.nanmedian(np.where(np.isnan(df_clean[num_cols]), np.nan, df_clean[num_cols]), axis=0),
    'Std Dev': np.nanstd(df_clean[num_cols], axis=0)
}, index=num_cols)

print("\n--- Key Numerical Statistics ---")
print(eda_stats)

# Explore power plants distribution by country and primary fuel type
top_countries = df_clean['country_long'].value_counts().head(10)
fuel_distribution = df_clean['primary_fuel'].value_counts()

print("\n--- Top 10 Countries by Plant Count ---")
print(top_countries)

print("\n--- Distribution by Primary Fuel Type ---")
print(fuel_distribution)


# ==========================================
# 3. STATISTICAL ANALYSIS & HYPOTHESIS TESTING
# ==========================================

# Group capacity (MW) array by primary fuel using NumPy arrays
unique_fuels = df_clean['primary_fuel'].dropna().unique()
fuel_capacity_groups = [
    df_clean[df_clean['primary_fuel'] == fuel]['capacity_mw'].dropna().values
    for fuel in unique_fuels
]

# Calculate mean & std capacity per fuel type using NumPy
print("\n--- Mean & Std Capacity (MW) by Fuel Type ---")
for fuel, group in zip(unique_fuels, fuel_capacity_groups):
    if len(group) > 0:
        print(f"{fuel:12s} -> Mean: {np.mean(group):8.2f} MW | Std: {np.std(group):8.2f} MW | Count: {len(group)}")

# Hypothesis Testing: One-Way ANOVA across fuel types
# Null Hypothesis (H0): Mean power plant capacity is equal across all fuel types.
# Alternative Hypothesis (H1): At least one fuel type has a significantly different mean capacity.
f_stat, p_val_anova = stats.f_oneway(*fuel_capacity_groups)
kw_stat, p_val_kw = stats.kruskal(*fuel_capacity_groups)

print("\n--- Hypothesis Testing Results ---")
print(f"One-Way ANOVA Test:       F-Statistic = {f_stat:.4f}, p-value = {p_val_anova:.4e}")
print(f"Kruskal-Wallis Rank Test: H-Statistic = {kw_stat:.4f}, p-value = {p_val_kw:.4e}")


# ==========================================
# 4. TIME SERIES ANALYSIS
# ==========================================

# Analyze commissioning trends over decades using NumPy vector operations
df_time = df_clean.dropna(subset=['commissioning_year']).copy()
df_time['decade'] = (np.floor(df_time['commissioning_year'] / 10) * 10).astype(int)

# Pivot table to explore evolution of fuel mix over time
top_5_fuels = ['Solar', 'Wind', 'Hydro', 'Gas', 'Coal']
fuel_evolution = df_time[df_time['primary_fuel'].isin(top_5_fuels)].groupby(['decade', 'primary_fuel']).size().unstack(fill_value=0)

print("\n--- Power Plant Commissioning Evolution (1950 - 2020) ---")
print(fuel_evolution.loc[1950:2020])


# ==========================================
# 5. MATRIX OPERATIONS IN REAL-WORLD CONTEXT
# ==========================================

# Select complete numeric attributes for matrix transformations
matrix_cols = ['capacity_mw', 'latitude', 'longitude', 'commissioning_year']
matrix_data = df_clean[matrix_cols].dropna().values

# Standardize feature matrix using NumPy operations: Z = (X - mu) / sigma
X_mean = np.mean(matrix_data, axis=0)
X_std = np.std(matrix_data, axis=0)
X_scaled = (matrix_data - X_mean) / X_std

# Compute Covariance Matrix: Cov = (1 / (N - 1)) * X_scaled^T * X_scaled
cov_matrix = np.cov(X_scaled, rowvar=False)

# Compute Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("\n--- Covariance Matrix ---")
print(np.round(cov_matrix, 4))

print("\n--- Eigenvalues ---")
print(np.round(eigenvalues, 4))

print("\n--- Eigenvectors (Principal Components Matrix) ---")
print(np.round(eigenvectors, 4))


# ==========================================
# 6. INTEGRATED VISUALIZATIONS (MATPLOTLIB & SEABORN)
# ==========================================

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Plot 1: Top 10 Primary Fuels by Plant Count
top_10_fuels = fuel_distribution.head(10)
sns.barplot(
    ax=axes[0, 0],
    x=top_10_fuels.values,
    y=top_10_fuels.index,
    palette="viridis"
)
axes[0, 0].set_title("Top 10 Fuel Types by Number of Power Plants", fontsize=13, fontweight='bold')
axes[0, 0].set_xlabel("Number of Power Plants")
axes[0, 0].set_ylabel("Primary Fuel")

# Plot 2: Average Capacity (MW) by Fuel Type
avg_cap = df_clean.groupby('primary_fuel')['capacity_mw'].mean().loc[top_10_fuels.index].sort_values(ascending=False)
sns.barplot(
    ax=axes[0, 1],
    x=avg_cap.values,
    y=avg_cap.index,
    palette="magma"
)
axes[0, 1].set_title("Average Installed Capacity (MW) by Fuel Type", fontsize=13, fontweight='bold')
axes[0, 1].set_xlabel("Mean Capacity (MW)")
axes[0, 1].set_ylabel("Primary Fuel")

# Plot 3: Evolution of Fuel Types Over Decades (Time Series)
fuel_evolution.loc[1950:2020].plot(
    kind='line',
    ax=axes[1, 0],
    marker='o',
    linewidth=2
)
axes[1, 0].set_title("Power Plant Commissioning Trends (1950–2020)", fontsize=13, fontweight='bold')
axes[1, 0].set_xlabel("Decade")
axes[1, 0].set_ylabel("Plants Commissioned")
axes[1, 0].legend(title="Fuel Type")

# Plot 4: Geographical Distribution (Latitude & Longitude Map)
sns.scatterplot(
    ax=axes[1, 1],
    data=df_clean,
    x='longitude',
    y='latitude',
    hue='primary_fuel',
    hue_order=['Solar', 'Hydro', 'Wind', 'Gas', 'Coal'],
    alpha=0.4,
    s=12
)
axes[1, 1].set_title("Global Geographical Distribution of Power Plants", fontsize=13, fontweight='bold')
axes[1, 1].set_xlabel("Longitude")
axes[1, 1].set_ylabel("Latitude")
axes[1, 1].legend(title="Fuel Type", loc="lower left")

plt.tight_layout()
plt.show()