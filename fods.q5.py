import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame with monthly sales data
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [200, 220, 250, 270, 300, 310, 320, 330, 340, 360, 380, 400]
})

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(data['Month'], data['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
plt.bar(data['Month'], data['Sales'], color='skyblue')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
