import numpy as np

# Sample sales_data array (replace this with the actual data)
# Each row represents the sales for a different product
sales_data = np.array([
    [10.99, 15.99, 20.99],
    [8.99, 12.99, 14.99],
    [13.99, 18.99, 22.99]
])

# Calculate the average price of all the products sold in the past month
average_price = np.mean(sales_data)

# Output the result
print(f"The average price of all the products sold in the past month is ${average_price:.2f}")
