import pandas as pd
import matplotlib.pyplot as plt

# Sample data frame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature': [30, 32, 35, 37, 40, 42, 45, 44, 40, 38, 34, 31],
    'Rainfall': [2.5, 2.0, 1.5, 1.2, 1.0, 0.8, 0.5, 0.7, 1.2, 1.5, 2.0, 2.3]
})

# Display the first few rows of the data frame
print(data.head())

# Generate line plot for Temperature
plt.figure(figsize=(10, 5))
plt.plot(data['Month'], data['Temperature'], marker='o', linestyle='-', color='b', label='Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Generate line plot for Rainfall
plt.figure(figsize=(10, 5))
plt.plot(data['Month'], data['Rainfall'], marker='o', linestyle='-', color='g', label='Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (cm)')
plt.title('Monthly Rainfall')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Generate scatter plot for Temperature vs Rainfall
plt.figure(figsize=(10, 5))
plt.scatter(data['Temperature'], data['Rainfall'], color='r', label='Temperature vs Rainfall')
plt.xlabel('Temperature (°C)')
plt.ylabel('Rainfall (cm)')
plt.title('Temperature vs Rainfall')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
