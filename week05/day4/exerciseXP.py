# Exercise 1: Understanding Data Visualization
# Data Visualization is incredibly important in data analysis because it puts discovered insights into perspective in a way that can be observed and understood by others. Charts, graphs, and dashboards make complex data easier to interpret. Without visualization, an analyst’s insights remain purely analytical information that may be difficult to interpret or apply.
# In data visualization, line graphs are used to demonstrate change and changes over time.
# for example, to predict what a specific output will be based on the current starting point, input, and rate of change.

# Exercise 2: Creating a Line Plot for Temperature Variation
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Exercise 1: Understanding Data Visualization
# Data visualization is incredibly important in data analysis because it puts discovered insights into perspective in a way that can be observed and understood by others. Charts, graphs, and dashboards make complex data easier to interpret. Without visualization, an analyst’s insights remain purely analytical information that may be difficult to interpret or apply.
# In data visualization, line graphs are used to demonstrate change and changes over time.
# for example, to predict what a specific output will be based on the current starting point, input, and rate of change.

# Exercise 2: Creating a Line Plot for Temperature Variation
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temps = [72, 74, 76, 80, 82, 78, 75]

plt.plot(days, temps, marker='o')
plt.xlabel('Day of the Week')
plt.ylabel('Temperature (F)')
plt.xticks(rotation=45)
plt.title('Temperature Variation Over the Week')
plt.show()

# Exercise 3: Visualizing Monthly Sales with a Bar Chart
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_amount =  [5000, 9000, 5500, 6200, 8700, 7000, 7500, 4000, 5700, 6500, 2300, 12000]

plt.bar(month, sales_amount, color='red', edgecolor='black', linewidth=2)
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.title('Monthly Sales')
plt.show()

# Exercise 4: Visualizing the Distribution of CGPA
gpa_range = df['What is your CGPA?'].sort_values()

sns.histplot(gpa_range, bins=10, color='orange', edgecolor='black')
plt.xlabel('CGPA')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.title('Distribution of CGPA')
plt.show()

#Exercise 5: Comparing Anxiety Levels Across Different Genders
