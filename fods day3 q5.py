import numpy as np
from scipy import stats

# Sample dataset: daily temperatures
temperatures = np.array([72, 75, 78, 73, 74, 80, 85, 100, 90, 76, 77, 81, 69])

# Calculate the variance of the temperatures
variance = np.var(temperatures)

# Method 2: Identify outliers using IQR
Q1 = np.percentile(temperatures, 25)
Q3 = np.percentile(temperatures, 75)
IQR = Q3 - Q1
outliers_iqr = temperatures[(temperatures < (Q1 - 1.5 * IQR)) | (temperatures > (Q3 + 1.5 * IQR))]

print(f"Variance of Daily Temperatures: {variance:.2f}")
print(f"Outliers using IQR Method: {outliers_iqr}")
