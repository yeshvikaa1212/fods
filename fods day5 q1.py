import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'CustomerID': [1, 1, 2, 2, 3, 3, 4, 4],
    'AmountSpent': [120, 150, 80, 90, 200, 210, 50, 60],
    'ItemsPurchased': [5, 6, 2, 3, 8, 9, 1, 2]
}

# Aggregate and standardize data
df = pd.DataFrame(data).groupby('CustomerID').sum().reset_index()
scaled_data = StandardScaler().fit_transform(df[['AmountSpent', 'ItemsPurchased']])

# K-Means clustering with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# Visualize clusters
sns.scatterplot(x='AmountSpent', y='ItemsPurchased', hue='Cluster', data=df, palette='viridis')
plt.title('Customer Segments')
plt.xlabel('Total Amount Spent')
plt.ylabel('Total Items Purchased')
plt.show()
