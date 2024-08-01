import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Create a DataFrame for better visualization
df = pd.DataFrame(X, columns=feature_names)
df['Species'] = y
print("Sample data:")
print(df.head())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Function to predict the species of a new flower
def predict_species(model):
    # Input features from the user
    print("Enter the measurements of the new flower:")
    sepal_length = float(input("Sepal Length (cm): "))
    sepal_width = float(input("Sepal Width (cm): "))
    petal_length = float(input("Petal Length (cm): "))
    petal_width = float(input("Petal Width (cm): "))
    
    # Create a DataFrame for the new flower
    new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
    # Predict the species
    predicted_class = model.predict(new_flower)[0]
    predicted_species = target_names[predicted_class]
    
    # Display the results
    print(f"The predicted species of the flower is: {predicted_species}")

# Predict the species for a new flower
predict_species(model)
