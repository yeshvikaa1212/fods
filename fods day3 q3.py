import numpy as np
from collections import Counter

# Sample purchase amounts (in dollars)
purchase_amounts = [20.99, 35.50, 12.00, 20.99, 45.00, 20.99, 12.00, 60.75, 35.50, 20.99]

# Calculate the mean (average) purchase amount
mean_purchase = np.mean(purchase_amounts)

# Identify the mode of the purchase amounts
count = Counter(purchase_amounts)
mode_purchase, mode_frequency = count.most_common(1)[0]

print(f"Mean (Average) Purchase Amount: ${mean_purchase:.2f}")
print(f"Mode of Purchase Amounts: ${mode_purchase:.2f}, Frequency: {mode_frequency}")
