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

#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using [Python] to model Salary based on Years of Experience.

# Read the dataset

# In[3]:


import pandas as pd
dataset = pd.read_csv("regression_data-1.csv")


# Create a scatter plot

# In[5]:


import matplotlib.pyplot as plt
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


# Fit a linear model

# In[7]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# Overlay the regression line

# In[10]:


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
# plt.show removed for clean output

# Evaluate the model

# In[16]:


model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared


# Plotting R_squared

# In[40]:


r_squared = model.score(dataset[["YearsExperience"]], dataset[["Salary"]])
plt.annotate(f"R² = {r_squared:.3f}", xy=(0.05,0.95), xycoords="axes fraction", fontsize=12,)
# plt.show removed for clean output

# In[ ]:

plt.savefig("linear_regression_python_output.png")
plt.show()


