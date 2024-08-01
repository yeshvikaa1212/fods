import numpy as np

sales_data = np.array([10000, 15000, 20000, 25000])
total_sales = np.sum(sales_data)

first_quarter_sales = sales_data[0]
fourth_quarter_sales = sales_data[3]

percentage_increase = ((fourth_quarter_sales - first_quarter_sales) / first_quarter_sales) * 100

print(f"Total sales for the year: ${total_sales:.2f}")
print(f"Percentage increase in sales from the first quarter to the fourth quarter: {percentage_increase:.2f}%")
