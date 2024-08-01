import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Sample data: Replace with your actual dataset
data = {
    'Symptom1': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    'Symptom2': [0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    'Symptom3': [1, 1, 0, 0, 1, 0, 1, 1, 0, 1],
    'Condition': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
X = df.drop('Condition', axis=1)
y = df['Condition']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the KNN model
k = 3  # Default value for k, can be changed by the user
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train_scaled, y_train)

# Predict the condition for a new patient
def predict_condition(model, scaler):
    # Input features from the user
    print("Enter the symptoms of the new patient:")
    symptom1 = float(input("Symptom1 (0 or 1): "))
    symptom2 = float(input("Symptom2 (0 or 1): "))
    symptom3 = float(input("Symptom3 (0 or 1): "))

    # Create DataFrame for the new patient
    new_patient = pd.DataFrame([[symptom1, symptom2, symptom3]], 
                               columns=['Symptom1', 'Symptom2', 'Symptom3'])
    
    # Standardize the new patient features
    new_patient_scaled = scaler.transform(new_patient)
    
    # Predict the condition
    predicted_condition = model.predict(new_patient_scaled)[0]
    
    # Display the results
    condition = "has the condition" if predicted_condition == 1 else "does not have the condition"
    print(f"The patient {condition}.")

# Allow user to input k value
k = int(input("Enter the number of neighbors (k): "))
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train_scaled, y_train)

# Predict the condition for a new patient
predict_condition(model, scaler)
