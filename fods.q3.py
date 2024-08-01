import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'data' is the given data frame containing the sales data

# Sample DataFrame for illustration
data = pd.DataFrame({
    'OrderID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'CustomerID': [101, 102, 103, 101, 102, 103, 104, 105, 106, 107],
    'ProductID': [1001, 1002, 1003, 1001, 1002, 1003, 1004, 1005, 1006, 1007],
    'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'A', 'C'],
    'Quantity': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'TotalPrice': [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
})

# Aggregate total sales by category
category_sales = data.groupby('Category')['TotalPrice'].sum().reset_index()

# Line Plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=category_sales, x='Category', y='TotalPrice', marker='o')
plt.title('Total Sales by Category (Line Plot)')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=category_sales, x='Category', y='TotalPrice', s=100)
plt.title('Total Sales by Category (Scatter Plot)')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()

# Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=category_sales, x='Category', y='TotalPrice')
plt.title('Total Sales by Category (Bar Plot)')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()
