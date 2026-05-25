# Mini-project: Advanced Statistical Analysis of Apple Inc. Stock Data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#loading dataset via pandas
df = pd.read_csv(r'C:\Users\gabri\Documents\Practice files\Apple Stock Prices From 1981 to 2023\Apple Stock Prices (1981 to 2023).csv')
print(df.head())