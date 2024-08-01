import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample data: Replace with your actual dataset
data = {
    'Usage Minutes': [100, 200, 150, 300, 250, 400, 350, 500, 220, 280],
    'Contract Duration (months)': [12, 24, 12, 36, 24, 36, 24, 36, 12, 24],
    'Customer Age': [25, 45, 35, 50, 30, 55, 40, 60, 28, 42],
    'Churn': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), X.columns)
    ]
)

# Create and train the Logistic Regression model
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

# Function to predict churn for a new customer
def predict_churn(pipeline):
    # Input features from the user
    print("Enter the details of the new customer:")
    usage_minutes = float(input("Usage Minutes: "))
    contract_duration = int(input("Contract Duration (months): "))
    customer_age = float(input("Customer Age: "))
    
    # Create DataFrame for the new customer
    new_customer = pd.DataFrame([[usage_minutes, contract_duration, customer_age]], 
                                columns=['Usage Minutes', 'Contract Duration (months)', 'Customer Age'])
    
    # Predict churn probability
    churn_probability = pipeline.predict_proba(new_customer)[0][1]
    churn_prediction = pipeline.predict(new_customer)[0]
    
    # Display results
    print(f"Probability of Churn: {churn_probability:.2f}")
    if churn_prediction == 1:
        print("The customer is predicted to churn.")
    else:
        print("The customer is predicted to not churn.")

# Predict churn for a new customer
predict_churn(pipeline)
