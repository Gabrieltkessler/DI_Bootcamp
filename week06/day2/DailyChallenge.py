import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

temp = np.random.uniform(low=-5, high=35, size=(10, 12))
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
city = ["NYC", "Tel Aviv", "Tokyo", "Jerusalem", "Miami", "Berlin", "Athens", "Rome", "Los Angeles", "Melbourne"]

df = pd.DataFrame(temp, index = city, columns = month)
# print(df)

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

temp = np.random.uniform(low=-5, high=35, size=(10, 12))
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
city = ["NYC", "Tel Aviv", "Tokyo", "Jerusalem", "Miami", "Berlin", "Athens", "Rome", "Los Angeles", "Melbourne"]

df = pd.DataFrame(temp, index = city, columns = month)
# print(df)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

for city in df.index:
    plt.plot(df.columns, df.loc[city], label=city)

plt.title("Monthly Temperature for All Cities")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.legend(title="City", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

temp_mean = df.mean(axis=1)
temp_min = df.min(axis=1)
temp_max = df.max(axis=1)

print("Average Temperature:\n", temp_mean)
print("\nMinimum Temperature Month:\n", temp_min.round(1))
print("\nMaximum Temperature Month:\n", temp_max.round(1))