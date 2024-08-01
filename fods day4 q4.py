import pandas as pd

# Sample sales data
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [25, 30, 22, 30, 25, 40, 22, 25, 35, 30],
    'PurchaseAmount': [100, 150, 200, 150, 100, 250, 200, 100, 300, 150]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate frequency distribution of ages
age_distribution = df['Age'].value_counts()

print("Frequency Distribution of Ages:")
print(age_distribution)
