import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data: CustomerID, TotalAmountSpent, VisitFrequency
data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'TotalAmountSpent': [500, 1500, 800, 2000, 1000],
    'VisitFrequency': [10, 30, 15, 40, 20]
}

# Create a DataFrame and standardize the data
df = pd.DataFrame(data)
scaled_data = StandardScaler().fit_transform(df[['TotalAmountSpent', 'VisitFrequency']])

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Assuming 3 clusters
df['Cluster'] = kmeans.fit_predict(scaled_data)

# Visualize the clusters
sns.scatterplot(x='TotalAmountSpent', y='VisitFrequency', hue='Cluster', data=df, palette='viridis')
plt.title('Customer Segments')
plt.xlabel('Total Amount Spent')
plt.ylabel('Visit Frequency')
plt.show()
