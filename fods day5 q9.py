import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np

# Sample data: Replace with your actual dataset
data = {
    'Area (sq ft)': [1500, 2500, 1800, 2200, 1600, 2700, 3000, 2300, 1700, 2600],
    'Bedrooms': [3, 4, 3, 4, 2, 5, 4, 3, 2, 4],
    'Location': ['Urban', 'Suburban', 'Urban', 'Urban', 'Suburban', 'Urban', 'Suburban', 'Urban', 'Suburban', 'Urban'],
    'Price (k$)': [300, 450, 320, 400, 280, 500, 470, 350, 290, 460]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert categorical feature 'Location' into numerical values
df['Location'] = df['Location'].map({'Urban': 1, 'Suburban': 0})

# Features and target
X = df.drop('Price (k$)', axis=1)
y = df['Price (k$)']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])
pipeline.fit(X_train, y_train)

# Function to predict the price of a new house
def predict_price(pipeline):
    # Input features from the user
    print("Enter the features of the new house:")
    area = float(input("Area (sq ft): "))
    bedrooms = int(input("Number of Bedrooms: "))
    location = input("Location (Urban or Suburban): ").capitalize()
    
    # Convert location to numerical value
    location_encoded = 1 if location == 'Urban' else 0
    
    # Create DataFrame for the new house
    new_house = pd.DataFrame([[area, bedrooms, location_encoded]], 
                             columns=['Area (sq ft)', 'Bedrooms', 'Location'])
    
    # Predict the price
    predicted_price = pipeline.predict(new_house)[0]
    
    # Display the result
    print(f"The predicted price of the house is: ${predicted_price * 1000:.2f}")

# Predict the price for a new house
predict_price(pipeline)
