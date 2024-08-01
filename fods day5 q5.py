import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Sample data: Features include Mileage, Age, Brand, EngineType, and Price (in thousands)
data = {
    'Mileage': [15000, 25000, 35000, 45000, 55000, 65000],
    'Age': [2, 3, 4, 5, 6, 7],
    'Brand': ['Toyota', 'Honda', 'Ford', 'Toyota', 'Honda', 'Ford'],
    'EngineType': ['Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol', 'Diesel'],
    'Price': [20, 18, 15, 17, 16, 14]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
X = df.drop('Price', axis=1)
y = df['Price']

# Define preprocessing for categorical features and feature scaling
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), ['Brand', 'EngineType']),
        ('num', StandardScaler(), ['Mileage', 'Age'])
    ]
)

# Create and train the model within a pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', DecisionTreeRegressor(random_state=42))
])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Function to input new car features and predict price
def predict_car_price(model):
    # Input features from the user
    mileage = float(input("Enter Mileage: "))
    age = int(input("Enter Age: "))
    brand = input("Enter Brand (Toyota, Honda, Ford): ")
    engine_type = input("Enter Engine Type (Petrol, Diesel): ")
    
    # Create DataFrame for the new car
    new_car = pd.DataFrame([[brand, engine_type, mileage, age]], 
                           columns=['Brand', 'EngineType', 'Mileage', 'Age'])
    
    # Predict price
    predicted_price = model.predict(new_car)[0]
    
    # Display results
    print(f"The predicted price of the car is: {predicted_price:.2f} thousand dollars")
    
    # Display decision tree
    print("\nDecision Tree:")
    print(export_text(model.named_steps['regressor'], feature_names=model.named_steps['preprocessor'].get_feature_names_out()))

# Predict the price for a new car
predict_car_price(model)
