import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import joblib

# Load a sample dataset (replace this with your actual data loading method)
def load_data():
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df, data.feature_names, 'target'

# Load the trained model (replace with your actual model path)
def load_model():
    # For demonstration, we use a RandomForest model trained on the Iris dataset
    model = RandomForestClassifier(random_state=42)
    df, _, target_name = load_data()
    X = df.drop(target_name, axis=1)
    y = df[target_name]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    return model, X_test, y_test

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    # Predict the target
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    # Display results
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")

# Main function to load data, model, and evaluate
def main():
    # Load dataset and model
    df, feature_names, target_name = load_data()
    model, X_test, y_test = load_model()
    
    # Display available features and target
    print("Available features:", feature_names)
    print("Target variable:", target_name)
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)

# Run the main function
if __name__ == "__main__":
    main()
