import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#1. Data Import and Cleaning:
df = pd.read_csv('Airplane_Crashes_and_Fatalities_Since_1908_t0_2023.csv', encoding='latin1')
df['Date'] = pd.to_datetime(df['Date'])

numeric_cols_to_impute = [
    'Aboard', 'Aboard Passangers', 'Aboard Crew',
    'Fatalities', 'Fatalities Passangers', 'Fatalities Crew',
    'Ground'
]

for col in numeric_cols_to_impute:
    if col in df.columns:
        if df[col].isnull().any(): # Check if there are any missing values
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            print(f"Filled missing values in '{col}' with median: {median_val}")

# Categorical/Text columns to impute
categorical_cols_to_impute = [
    'Time', 'Operator', 'Flight #', 'Route', 'AC Type',
    'Registration', 'cn/ln', 'Summary', 'Location'
]

for col in categorical_cols_to_impute:
    if col in df.columns:
        if df[col].isnull().any():
            # For some columns like 'Operator' or 'Location', filling with mode might be better.
            # For others like 'Flight #', 'Route', 'Registration', 'cn/ln', 'Summary', 'Time' 'Unknown' is a reasonable placeholder
            if col in ['Operator', 'Location']:
                mode_val = df[col].mode()[0] # mode() returns a Series, take the first if multiple modes
                df[col] = df[col].fillna(mode_val)
                print(f"Filled missing values in '{col}' with mode: {mode_val}")
            else:
                df[col] = df[col].fillna('Unknown')
                print(f"Filled missing values in '{col}' with 'Unknown'")

print("\nMissing values after imputation:")
print(df.isnull().sum())

#2. Exploratory Data Analysis:
crash_count = len(df)
fatal_count = df['Fatalities'].sum()
survivor_count = df['Aboard'].sum() - df['Fatalities'].sum()

survival_rate = (survivor_count / (survivor_count + fatal_count) * 100)

print(f"crash count is {crash_count}")
print(f"fatal count is {fatal_count}")
print(f"survivor count is {survivor_count}")
print(f"The survival rate for each crash on average is {survival_rate:.0f}%")

# crash count is 4998
# fatal count is 111732.0
# survivor count is 43912.0
# The survival rate for each crash on average is 28%

year_range = df['Year'].max() - df['Year'].min()
crash_frequency = crash_count / year_range
fatal_frequency = fatal_count / year_range
survival_frequency = survivor_count / year_range

print(f"The data covers a range of {year_range} years.")
print(f"The crash frequency over {year_range} years is {crash_frequency:.0f} crashes per year on average")
print(f"The fatality frequency is {fatal_frequency:.0f} souls per year")
print(f"The survival frequency is {survival_frequency:.0f} survivors per year")

# The data covers a range of 115 years.
# The crash frequency over 115 years is 43 crashes per year on average
# The fatality frequency is 972 souls per year
# The survival frequency is 382 survivors per year

#3. Statistical Analysis:
start_year = int(df['Year'].min())
end_year = int(df['Year'].max())

decade_fatalities = []

current_decade_start = start_year
while current_decade_start <= end_year:
    decade_end = current_decade_start + 9 # Inclusive end for 10-year period
    if decade_end > end_year:
        decade_end = end_year

    # Filter data for the current decade
    decade_df = df[(df['Year'] >= current_decade_start) & (df['Year'] <= decade_end)]

    total_fatalities_decade = decade_df['Fatalities'].sum()
    num_years_in_decade = (decade_end - current_decade_start) + 1

    # Calculate average fatalities per year for this decade
    average_fatalities_per_year = total_fatalities_decade / num_years_in_decade if num_years_in_decade > 0 else 0

    decade_fatalities.append({
        'Decade': f"{current_decade_start}-{decade_end}",
        'Total Fatalities': total_fatalities_decade,
        'Average Fatalities Per Year': average_fatalities_per_year
    })

    current_decade_start += 10 # Move to the next decade

# Display the results in a DataFrame for better readability
decade_fatalities_df = pd.DataFrame(decade_fatalities)
display(decade_fatalities_df)

#4. Visualization:
import matplotlib.pyplot as plt

plt.scatter(decade_fatalities_df['Decade'], decade_fatalities_df['Average Fatalities Per Year'])
plt.xlabel('Decade')
plt.ylabel('Average Fatalities Per Year')
plt.xticks(rotation=90)
plt.title('Average Fatalities Per Year Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()

#5. Insight and Report:
# Throughout this analysis, I used pandas to load and preprocess the dataset. I also used numpy and scipy to perform statistical analysis and uncover interesting insights into airplane crashes over the last 115 years.
# I found that between 1908 and 2023 there were:

# 4,998 crashes
# 111,723 fatalities
# 43,912 survivors

# This results in an overall survival rate of 28%, which was higher than I expected.
# On average, aviation accidents caused approximately 972 deaths per year, while around 382 people survived crashes annually.
# After breaking down the statistics by decade and visualizing the data using matplotlib, I found that the period from 1968 to 1987 was the deadliest era in aviation history.
# Since then, fatalities have decreased significantly, from 20,278 deaths during that 20 year period to just 1,974 in recent years.
# Overall, the data shows that flying has become safer with each passing decade.


