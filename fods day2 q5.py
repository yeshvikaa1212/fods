import numpy as np

# Example fuel_efficiency array (replace this with your actual fuel efficiency data)
fuel_efficiency = np.array([25, 30, 35, 40, 45])

# Calculate the average fuel efficiency
average_fuel_efficiency = np.mean(fuel_efficiency)

# Specify the indices of the two car models you want to compare
car_model_1_index = 0  # Example: first car model
car_model_2_index = 4  # Example: fifth car model

# Get the fuel efficiencies of the two car models
fuel_efficiency_model_1 = fuel_efficiency[car_model_1_index]
fuel_efficiency_model_2 = fuel_efficiency[car_model_2_index]

# Calculate the percentage improvement in fuel efficiency between the two car models
percentage_improvement = ((fuel_efficiency_model_2 - fuel_efficiency_model_1) / fuel_efficiency_model_1) * 100

# Output the results
print(f"Average fuel efficiency: {average_fuel_efficiency:.2f} miles per gallon")
print(f"Percentage improvement in fuel efficiency from car model {car_model_1_index + 1} to car model {car_model_2_index + 1}: {percentage_improvement:.2f}%")
