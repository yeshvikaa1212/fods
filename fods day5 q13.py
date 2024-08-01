import numpy as np
from scipy import stats

# Sample data: Replace these arrays with your actual conversion rate data
conversion_rates_A = np.array([0.12, 0.15, 0.14, 0.13, 0.16, 0.14, 0.15, 0.13, 0.15, 0.14])
conversion_rates_B = np.array([0.18, 0.20, 0.19, 0.21, 0.22, 0.20, 0.19, 0.21, 0.23, 0.22])

# Perform an independent t-test
t_stat, p_value = stats.ttest_ind(conversion_rates_A, conversion_rates_B, equal_var=True)

# Display results
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpretation
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: There is a statistically significant difference between the conversion rates of design A and design B.")
else:
    print("Fail to reject the null hypothesis: There is no statistically significant difference between the conversion rates of design A and design B.")
