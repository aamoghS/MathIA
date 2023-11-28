import numpy as np
from tabulate import tabulate

x_values = np.array([60,69, 75, 76, 77, 83, 84, 90, 91, 97, 98, 103, 104, 105, 110, 111, 115, 117, 118, 120, 124, 125, 129, 131, 132, 138, 145])
y_values = np.array([85,97, 105, 110, 101, 129, 121, 130, 130, 129, 140, 150, 150, 154,150, 160, 160, 170, 170, 176, 180, 180, 178, 181, 189, 187, 200])

def equation(x):
    return 1.16 * x + 19.7

predicted_values = equation(x_values)

residuals = y_values - predicted_values

table_data = list(zip(predicted_values, residuals))
headers = ["Predicted values", "Residuals"]
table = tabulate(table_data, headers=headers, tablefmt="pipe")

print(table)
