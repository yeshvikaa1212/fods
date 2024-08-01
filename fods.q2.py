import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Example data frame
data = {
    'SmokingHabits': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'LungCancerRates': [5, 15, 20, 40, 50, 55, 60, 75, 85, 95]
}
df = pd.DataFrame(data)

# Display the first few rows of the dataset
print(df.head())

# Calculate the correlation coefficient
correlation, _ = pearsonr(df['SmokingHabits'], df['LungCancerRates'])
print(f'Correlation coefficient between smoking habits and lung cancer rates: {correlation:.2f}')

# Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='SmokingHabits', y='LungCancerRates', data=df)
plt.title('Scatter Plot of Smoking Habits vs Lung Cancer Rates')
plt.xlabel('Smoking Habits (Cigarettes per Day)')
plt.ylabel('Lung Cancer Rates (Per 1000 People)')
plt.grid(True)
plt.show()
