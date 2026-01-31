"""
Scenario 3: Missing Value Handling
Task: A dataset has missing values in the "income" column. Write code to:
1. Replace missing values with the median if the data is normally distributed.
2. Replace with the mode if skewed. Use Pandas and a skewness threshold of 0.5.
"""

import pandas as pd
import numpy as np

# Example input data
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"],
    "income": [50000, 60000, np.nan, 55000, np.nan, 52000, 58000]
}

df = pd.DataFrame(data)

# Calculate skewness
skewness = df['income'].skew()

# Check skewness and replace missing values
if abs(skewness) <= 0.5:
    # Data is normally distributed, use median
    fill_value = df['income'].median()
    df['income'].fillna(fill_value, inplace=True)
    print(f"Skewness: {skewness:.2f} - Using Median: {fill_value}")
else:
    # Data is skewed, use mode
    fill_value = df['income'].mode()[0]
    df['income'].fillna(fill_value, inplace=True)
    print(f"Skewness: {skewness:.2f} - Using Mode: {fill_value}")

# Output
print("\nDataFrame after filling missing values:")
print(df)
