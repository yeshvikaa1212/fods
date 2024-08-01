import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
import numpy as np

# Sample data: Replace with your actual dataset
data = {
    'Annual Spending ($)': [500, 1500, 2000, 800, 1200, 2200, 1700, 3000, 1000, 2500],
    'Frequency of Purchase': [5, 15, 20, 8, 12, 22, 18, 30, 10, 25],
    'Average Basket Size ($)': [50, 100, 150, 70, 90, 200, 120, 250, 80, 180]
}

# Create DataFrame
df = pd.DataFrame(data)

# Define the number of clusters
n_clusters = 3  # Adjust based on your analysis

# Create and fit the K-Means model
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('kmeans', KMeans(n_clusters=n_clusters, random_state=42))
])

# Fit the model on the data
pipeline.fit(df)

# Function to assign a new customer to an existing segment
def assign_segment(pipeline):
    # Input features from the user
    print("Enter the details of the new customer:")
    annual_spending = float(input("Annual Spending ($): "))
    frequency_of_purchase = float(input("Frequency of Purchase: "))
    avg_basket_size = float(input("Average Basket Size ($): "))
    
    # Create DataFrame for the new customer
    new_customer = pd.DataFrame([[annual_spending, frequency_of_purchase, avg_basket_size]], 
                                columns=['Annual Spending ($)', 'Frequency of Purchase', 'Average Basket Size ($)'])
    
    # Predict the segment
    segment = pipeline.predict(new_customer)[0]
    cluster_centers = pipeline.named_steps['kmeans'].cluster_centers_
    center = cluster_centers[segment]
    
    # Display results
    print(f"The new customer is assigned to Segment {segment}.")
    print(f"Cluster Center for Segment {segment}: {center}")

# Assign a new customer to a segment
assign_segment(pipeline)
