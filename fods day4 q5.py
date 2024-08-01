import pandas as pd

# Sample dataset with user interaction data
data = {
    'PostID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Likes': [10, 15, 20, 15, 10, 25, 20, 10, 30, 15]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate frequency distribution of likes
likes_distribution = df['Likes'].value_counts()

print("Frequency Distribution of Likes:")
print(likes_distribution)
