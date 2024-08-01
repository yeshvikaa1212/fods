import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Sample data: HouseSize (in square feet), Price (in thousand dollars)
data = {
    'HouseSize': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200],
    'Price': [300, 320, 340, 360, 380, 400, 420, 440]
}

# Create DataFrame
df = pd.DataFrame(data)

# Bivariate analysis: Plot HouseSize vs. Price
plt.scatter(df['HouseSize'], df['Price'])
plt.xlabel('House Size (sq ft)')
plt.ylabel('Price (thousands $)')
plt.title('House Size vs. Price')
plt.show()

# Features and target
X = df[['HouseSize']]
y = df['Price']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate model performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae:.2f}')
print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'R-squared: {r2:.2f}')

# Plot regression line and data points
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('House Size (sq ft)')
plt.ylabel('Price (thousands $)')
plt.title('Linear Regression: House Size vs. Price')
plt.show()
