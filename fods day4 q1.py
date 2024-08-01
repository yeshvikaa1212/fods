import pandas as pd
import scipy.stats as stats
import numpy as np

# Sample dataset
data = {
    'product_title': ['Pineapple slicer', 'Levis Jeans Pant', 'Wallet', 'Salwar'],
    'product_category': ['Apparel', 'Apparel', 'Apparel', 'Apparel'],
    'star_rating': [4, 5, 5, 5],
    'review_headline': ['Really good', 'Perfect Dress', 'Love it', 'Awesome'],
    'review_date': ['2013-01-14', '2014-04-22', '2015-07-28', '2015-06-12']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Filter for the specific product category
apparel_reviews = df[df['product_category'] == 'Apparel']

# Calculate the mean and standard deviation of star ratings
mean_rating = apparel_reviews['star_rating'].mean()
std_rating = apparel_reviews['star_rating'].std(ddof=1)
n = len(apparel_reviews)

# Calculate the confidence interval
confidence_level = 0.95
alpha = 1 - confidence_level
df = n - 1

t_critical = stats.t.ppf(1 - alpha/2, df)
margin_of_error = t_critical * (std_rating / np.sqrt(n))

confidence_interval = (mean_rating - margin_of_error, mean_rating + margin_of_error)

print(f"Mean Rating: {mean_rating}")
print(f"Confidence Interval: {confidence_interval}")
