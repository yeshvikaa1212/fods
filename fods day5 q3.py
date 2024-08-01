import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Sample data
data = {
    'Age': [45, 50, 35, 40, 60, 55],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male'],
    'BloodPressure': [120, 130, 110, 140, 125, 135],
    'Cholesterol': [200, 220, 180, 210, 230, 190],
    'Outcome': ['Good', 'Bad', 'Good', 'Bad', 'Good', 'Bad']
}

# Create DataFrame and preprocess
df = pd.DataFrame(data)
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Outcome'] = df['Outcome'].map({'Good': 1, 'Bad': 0})

# Features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predictions and evaluation
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print('\nClassification Report:\n', classification_report(y_test, y_pred, zero_division=0))
