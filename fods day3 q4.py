import numpy as np

# Sample dataset: rows are departments, columns are monthly expenses
expenses = np.array([
    [1200, 1300, 1400, 1500, 1600],
    [1100, 1200, 1300, 1400, 1500],
    [1000, 1100, 1200, 1300, 1400]
])

# Calculate the variance for each department (row)
variance = np.var(expenses, axis=1)

# Calculate the covariance matrix for all departments
covariance_matrix = np.cov(expenses, rowvar=True)

print(f"Variance of Monthly Expenses for Each Department: {variance}")
print(f"Covariance Matrix of Monthly Expenses: \n{covariance_matrix}")
