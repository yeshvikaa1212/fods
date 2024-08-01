import numpy as np

# Sample recovery times (in days)
recovery_times = [7, 8, 5, 12, 9, 10, 6, 11, 13, 4, 15, 3, 8, 14, 9]

# Calculate percentiles
percentile_10th = np.percentile(recovery_times, 10)
percentile_50th = np.percentile(recovery_times, 50)
percentile_90th = np.percentile(recovery_times, 90)

print(f"10th Percentile: {percentile_10th} days")
print(f"50th Percentile: {percentile_50th} days")
print(f"90th Percentile: {percentile_90th} days")
