from collections import Counter
import re

# Sample customer reviews
reviews = [
    "Great product! Really enjoyed using it.",
    "Not bad, but could be improved. The product is okay.",
    "Excellent quality and value for money.",
    "I did not like it. It was not what I expected.",
    "Great! Will definitely recommend it to others."
]

# Preprocess and tokenize words
words = re.findall(r'\b\w+\b', ' '.join(reviews).lower())

# Calculate frequency distribution
word_counter = Counter(words)

# Print frequency distribution
print("Frequency Distribution of Words:")
for word, frequency in word_counter.items():
    print(f"Word: '{word}', Frequency: {frequency}")
