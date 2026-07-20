import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

data = pd.read_csv(filename)
model = LinearRegression()
model = model.fit(data[[x_col]], data[[y_col]])

plt.scatter(data[[x_col]], data[[y_col]], color='red')
plt.plot(data[[x_col]], model.predict(data[[x_col]]), color='blue')
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)


import pandas as pd
dataset = pd.read_csv("regression_data-1.csv")


import matplotlib.pyplot as plt
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model = model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")


model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared


x = dataset["YearsExperience"]
y = dataset["Salary"]
y_pred = model.predict(dataset[["YearsExperience"]])


from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err = linregress(x, y)


from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y, y_pred)


plt.plot(x, y_pred, label='Fitted line')
plt.text(x.min(), y.max(), f"y = {slope:.2f}x + {intercept:.2f}\nr = {r_value:.2f}", verticalalignment="top")


results = pd.DataFrame({"Mertric": ["Slope", "Y-intercept", "r", "R²", "MSE"],
            "Value": [slope, intercept, r_value, r_value ** 2, mse]})

plt.show()
print(results)

