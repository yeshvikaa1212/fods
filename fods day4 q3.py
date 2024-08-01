from collections import Counter

# Sample dataset
weather_data = [
    ('Sunny', 120),
    ('Rainy', 85),
    ('Cloudy', 100),
    ('Snowy', 30),
    ('Windy', 60)
]

# Create a Counter object directly from the dataset
count = Counter(weather_data)

# Find the most common weather type
most_common_weather = count.most_common(1)[0]

print(f"Most Common Weather Type: {most_common_weather[0]}")
print(f"Number of Occurrences: {most_common_weather[1]}")
