import numpy as np

# Sample dataset: daily sales figures over the past month
# Example data: 30 days of sales data
daily_sales = np.array([200, 210, 190, 220, 230, 250, 240, 220, 210, 200,
                        210, 215, 225, 230, 240, 245, 235, 220, 210, 200,
                        210, 220, 230, 240, 250, 260, 270, 280, 290, 300,
                        310, 320, 330, 340, 350, 360, 370, 380, 390, 400])

# Calculate the variance of the daily sales
variance = np.var(daily_sales)

print(f"Variance of Daily Sales: {variance:.2f}")
