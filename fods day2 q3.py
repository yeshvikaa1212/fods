import numpy as np
house_data = np.array([
    [3, 2000, 350000],
    [4, 2500, 450000],
    [5, 3000, 550000],
    [6, 3500, 650000],
    [4, 2200, 400000],
    [5, 2800, 500000]
])
houses_more_than_four_bedrooms = house_data[house_data[:, 0] > 4]
if houses_more_than_four_bedrooms.size > 0:
    average_sale_price = np.mean(houses_more_than_four_bedrooms[:, 2])
    print(f"The average sale price of houses with more than four bedrooms is ${average_sale_price:.2f}")
else:
    print("There are no houses with more than four bedrooms in the dataset.")
