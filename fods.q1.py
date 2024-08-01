import pandas as pd

# Assuming 'df' is the given data frame containing the customer orders dataset
# For example purposes, let's create a sample data frame:
data = pd.DataFrame({
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 103, 104, 105],
    'ProductID': [1001, 1002, 1003, 1004, 1005],
    'Quantity': [1, 2, 3, 4, 5],
    'TotalPrice': [10.0, 20.0, 30.0, 40.0, 50.0]
})

# Step 1: Explore the dataset
print(data.head())  # Display the first few rows of the dataset
print(data.info())  # Get a summary of the dataset
print(data.describe())  # Get descriptive statistics

# Step 2: Clean the data
# Check for missing values
print(data.isnull().sum())

# Handle missing values (example: fill with 0)
data.fillna(0, inplace=True)

# Check for duplicates
print(data.duplicated().sum())

# Remove duplicates
data.drop_duplicates(inplace=True)

# Step 3: Analyze the data
# Example analysis: Total sales by customer
total_sales_by_customer = data.groupby('CustomerID')['TotalPrice'].sum().reset_index()
print(total_sales_by_customer)

# Example analysis: Most popular product by quantity sold
most_popular_product = data.groupby('ProductID')['Quantity'].sum().reset_index().sort_values(by='Quantity', ascending=False)
print(most_popular_product)

# Example analysis: Average order value
average_order_value = data['TotalPrice'].mean()
print(f'Average Order Value: ${average_order_value:.2f}')
