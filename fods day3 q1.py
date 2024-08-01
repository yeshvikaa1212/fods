import numpy as np

# Sample response times (in milliseconds)
response_times = [120, 135, 150, 145, 160, 175, 130, 140, 155, 165, 170, 180, 190, 200]

# Calculate percentiles
percentile_25th = np.percentile(response_times, 25)
percentile_50th = np.percentile(response_times, 50)
percentile_75th = np.percentile(response_times, 75)

print(f"25th Percentile: {percentile_25th} ms")
print(f"50th Percentile: {percentile_50th} ms")
print(f"75th Percentile: {percentile_75th} ms")
