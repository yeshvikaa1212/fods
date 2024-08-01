import numpy as np

# Sample dataset: rows are cities, columns are daily temperatures over a year
# Example data: Each row represents a city with 365 temperature readings
temperature_data = np.array([
    # City 1
    [30, 31, 29, 32],  # Replace with actual daily temperatures for City 1
    # City 2
    [25, 26, 24, 28],  # Replace with actual daily temperatures for City 2
    # Add more cities as needed
])

# Calculate the mean temperature for each city
mean_temperatures = np.mean(temperature_data, axis=1)

# Calculate the standard deviation of temperature for each city
std_devs = np.std(temperature_data, axis=1)

# Determine the city with the highest temperature range
temperature_ranges = np.ptp(temperature_data, axis=1)  # Peak-to-peak (range) = max - min
city_highest_range = np.argmax(temperature_ranges)

# Find the city with the most consistent temperature (lowest standard deviation)
city_most_consistent = np.argmin(std_devs)

# Output results
print(f"Mean Temperature for Each City: {mean_temperatures}")
print(f"Standard Deviation of Temperature for Each City: {std_devs}")
print(f"City with Highest Temperature Range: City {city_highest_range + 1} (Range: {temperature_ranges[city_highest_range]:.2f})")
print(f"City with Most Consistent Temperature: City {city_most_consistent + 1} (Standard Deviation: {std_devs[city_most_consistent]:.2f})")
