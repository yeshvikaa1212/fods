import pandas as pd

# Sample dataset
data = {
    'DISEASE_NAME': ['Common Cold', 'Diabetes', 'Bronchitis', 'Influenza', 'Kidney Stones'],
    'DIAGNOSED_PATIENTS': [320, 120, 100, 150, 60]
}

# Create DataFrame
df = pd.DataFrame(data)

# Find the most common disease
most_common_disease = df.loc[df['DIAGNOSED_PATIENTS'].idxmax()]

print(f"Most Common Disease: {most_common_disease['DISEASE_NAME']}")
print(f"Number of Diagnosed Patients: {most_common_disease['DIAGNOSED_PATIENTS']}")
