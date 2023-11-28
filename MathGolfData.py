import numpy as np
import matplotlib.pyplot as plt

data = [
    (50, 85), (60, 75), (69, 107), (75, 95), (76, 110),
    (77, 111), (83, 119), (84, 130), (90, 125), (91, 140),
    (97, 129), (98, 135), (103, 110), (104, 145), (105, 160),
    (110, 145), (111, 140), (115, 150), (117, 110), (118, 140),
    (120, 170), (124, 180), (125, 160), (129, 190), (131, 181),
    (132, 189), (138, 187), (145, 170)
]

x_values, y_values = zip(*data)

mean_x = np.mean(x_values)
mean_y = np.mean(y_values)
std_dev_x = np.std(x_values)
std_dev_y = np.std(y_values)
correlation_coefficient = np.corrcoef(x_values, y_values)[0, 1]
slope, intercept = np.polyfit(x_values, y_values, 1)
regression_line = np.polyval([slope, intercept], x_values)
r_squared_regression = np.corrcoef(x_values, regression_line)[0, 1] ** 2

# Print results
print(f"Mean of x: {mean_x}")
print(f"Mean of y: {mean_y}")
print(f"Standard Deviation of x: {std_dev_x}")
print(f"Standard Deviation of y: {std_dev_y}")
print(f"Correlation Coefficient: {correlation_coefficient}")
print(f"Overall r^2: {correlation_coefficient**2}")
print(f"Linear Regression: y = {slope:.2f}x + {intercept:.2f}")
