

# Module 3: Exploratory Data Analysis
## Exploratory Data Analysis (EDA) using Python
Exploratory Data Analysis (EDA) is an essential step in understanding and summarizing the main characteristics of a dataset. It helps uncover relationships between variables and identifies key factors impacting the target variable.
### 1. Descriptive Statistics
Descriptive statistics provide a summary of the data's main characteristics. It includes measures like mean, median, mode, and standard deviation.
### 2. GroupBy Operations
GroupBy operations allow us to group data based on categorical variables and perform aggregations or transformations.
### 3. Data Visualization Commands in Python
Visualizations play a key role in data analysis. Various forms of graphs and plots can be created with data in Python to aid in visualizing and analyzing data effectively. The two major libraries used for this purpose are matplotlib and seaborn.
### 4. Correlation Analysis
Correlation analysis measures the relationship between variables. It helps identify how changes in one variable are associated with changes in another.
### 5. Advanced Correlation Methods (**Correlation Statistics)**
#### **5.1 Pearson Correlation**
Pearson correlation coefficient measures the linear relationship between two variables. It ranges from -1 to 1, where 1 indicates a strong positive correlation, -1 indicates a strong negative correlation, and 0 indicates no linear correlation.
#### **5.2 Correlation Heatmaps**
Correlation heatmaps provide a visual representation of the correlation matrix. They use color gradients to indicate the strength and direction of correlations between variables
![insert_image_url_here](insert_image_url_here)
___
## 1. Descriptive Statistics in Data Analysis
Descriptive statistics are a crucial first step in exploring your data before building complex models. They provide a summary of your dataset, helping you understand its basic features and distribution.
### Descriptive Statistical Analysis
Descriptive statistical analysis helps describe the basic features of a dataset, offering a summary of the sample and measures of the data
### Using `describe` Function
The `describe` function in pandas computes basic statistics for all numerical variables in your data frame, including:
- Mean
- Total number of data points
- Standard deviation
- Quartiles
- Extreme values
NaN values are automatically skipped in these statistics.
```python
df.describe()
```
#### Example Output
```plain text
**             price  engine-size  horsepower     length      width
**count      5.00000     5.000000    5.000000   5.000000   5.000000
mean   15329.00000   132.600000  118.400000  170.100000  64.480000
std     1570.38349    17.782794   21.800460   7.928386   0.396108
min    13495.00000   109.000000  102.000000  157.300000  63.900000
25%    13950.00000   130.000000  110.000000  168.800000  64.100000
50%    15250.00000   136.000000  111.000000  171.200000  64.800000
75%    16500.00000   136.000000  115.000000  176.600000  64.800000
max    17450.00000   152.000000  154.000000  176.600000  64.800000
```
### Categorical Variables
Categorical variables can be divided into different categories or groups and have discrete values. For example, the drive system in a car dataset may consist of categories like forward wheel-drive, rear wheel-drive, and four wheel-drive.
#### Summarizing Categorical Data
The `value_counts` function summarizes categorical data.
```python
df['drive-wheels'].value_counts()
```
#### Example Output of `value_counts` Function
```plain text
front-wheel-drive    118
rear-wheel-drive      75
four-wheel-drive       8
Name: drive-wheels, dtype: int64
```
### Box Plots
Box plots visualize numeric data distributions and highlight the following features:
- Median
- Upper quartile (75th percentile)
- Lower quartile (25th percentile)
- Inter-quartile range (IQR)
- Lower and upper extremes (calculated as 1.5 times the IQR above the 75th percentile and below the 25th percentile)
- Outliers
Box plots help compare distributions between groups.
```python
import seaborn as sns
sns.boxplot(x='drive-wheels', y='price', data=df)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BV7ALWM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQDwpYMgBX%2FuHtqVjevHEcPoYuyyrZa6kCeu3ROih1Xq5gIhAJlQBb1XeFGNrEpa2cGC6S0kyM8P%2BQTKkfrpMf%2Fqxa0aKv8DCC4QABoMNjM3NDIzMTgzODA1IgxFLXuEJ%2Bgj5oXY7AYq3AOa4LcSjBl4rAZcZGI70NDs5eQbTqjt0mqmTMgIzQpwBVOLUOc50LXV8%2BxZng7HDB%2FpUQzXgZnrwuCgaTEl3tuxliHxs2fPXprYiXlBZ54njPt51tuWtu9T3VRvxwOimpfZdV9W7GmEyzvJpXQkKJTYqYdhE2jETopoClhDgBfV7XQuwSj7fuVwdVJydea%2BQjbWIwSNO1YTcQ%2FYlyBDcPq7F4Kx%2FhYhKVvZnbwYtlm8yS7c%2BMdyGvb4orrhsa1GyjPSW85%2FcqV%2FC87Xwy9k2Z3GzWdrkvFMGu%2FtwxIu5zeMFiUf7CuzzkYX5iB2%2Bqy%2BaIcAJYEHC5Z12Dz97k0Nesczjr%2FMBnR7qzpf8wvI4U0necEdippzjX%2BeMikFgQNcUPnzWFL5Nr7lhGVjxG9tg7vyXjC9IyFwakrTZeyxPXmamYD3qJDPm8K9MWj0kLJSqcfex6imJ1K9dLYprDcCQ15wPr8tlsndf%2FDt4CA%2FwJpPcREkBZwJKZJdzLN4FWWpNvFKh7tTIN3J9Smg9ckxvP8LwUeBbO4qJeUT5%2F%2Fi1yBRCFwL754LTqG%2Bb5peHC1TptkFC0k%2FOppBvi49csuPqKRH4K0hg398jpeISgpiDWeNZi84l0hEoWdxC4OEQzDanYi9BjqkAT2UuXUNImZxVOS9LTmAKfmqOyB9eEH0Id7dT6VMZKUXFDypkuxUZvvTKULemMv2pYhN7OSXGm%2BkuAURGmLjB2ADpU58ry3nbYADkw3z0BX4L6f%2Bzlzt2xEPurEx%2BrnFJTL1zhU7XLRbHqBgpYKOavK0%2FElY%2FwGF%2FlHW6KvJCDbbGSRodAtgm5qZCeCGeXa4gRKbK6yY32l3opuybH7Txg8K05Vu&X-Amz-Signature=d518738066035c6ea2d51aada06bc6352f58d3c17b41f24bd40f811fe8946200&X-Amz-SignedHeaders=host&x-id=GetObject)
### Scatter Plots
Scatter plots visualize the relationship between two continuous variables. They help identify how changes in one variable are associated with changes in another.
- **Predictor Variable:** The variable used to predict an outcome (e.g., engine size).
- **Target Variable:** The variable being predicted (e.g., car price).
In a scatter plot:
- Predictor variable is plotted on the x-axis.
- Target variable is plotted on the y-axis.
```python
import matplotlib.pyplot as plt

plt.scatter(df['engine-size'], df['price'])
plt.xlabel('Engine Size')
plt.ylabel('Price')
plt.title('Scatterplot of Engine Size vs Price')
plt.show()
```
![insert_image_url_here](insert_image_url_here)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BV7ALWM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQDwpYMgBX%2FuHtqVjevHEcPoYuyyrZa6kCeu3ROih1Xq5gIhAJlQBb1XeFGNrEpa2cGC6S0kyM8P%2BQTKkfrpMf%2Fqxa0aKv8DCC4QABoMNjM3NDIzMTgzODA1IgxFLXuEJ%2Bgj5oXY7AYq3AOa4LcSjBl4rAZcZGI70NDs5eQbTqjt0mqmTMgIzQpwBVOLUOc50LXV8%2BxZng7HDB%2FpUQzXgZnrwuCgaTEl3tuxliHxs2fPXprYiXlBZ54njPt51tuWtu9T3VRvxwOimpfZdV9W7GmEyzvJpXQkKJTYqYdhE2jETopoClhDgBfV7XQuwSj7fuVwdVJydea%2BQjbWIwSNO1YTcQ%2FYlyBDcPq7F4Kx%2FhYhKVvZnbwYtlm8yS7c%2BMdyGvb4orrhsa1GyjPSW85%2FcqV%2FC87Xwy9k2Z3GzWdrkvFMGu%2FtwxIu5zeMFiUf7CuzzkYX5iB2%2Bqy%2BaIcAJYEHC5Z12Dz97k0Nesczjr%2FMBnR7qzpf8wvI4U0necEdippzjX%2BeMikFgQNcUPnzWFL5Nr7lhGVjxG9tg7vyXjC9IyFwakrTZeyxPXmamYD3qJDPm8K9MWj0kLJSqcfex6imJ1K9dLYprDcCQ15wPr8tlsndf%2FDt4CA%2FwJpPcREkBZwJKZJdzLN4FWWpNvFKh7tTIN3J9Smg9ckxvP8LwUeBbO4qJeUT5%2F%2Fi1yBRCFwL754LTqG%2Bb5peHC1TptkFC0k%2FOppBvi49csuPqKRH4K0hg398jpeISgpiDWeNZi84l0hEoWdxC4OEQzDanYi9BjqkAT2UuXUNImZxVOS9LTmAKfmqOyB9eEH0Id7dT6VMZKUXFDypkuxUZvvTKULemMv2pYhN7OSXGm%2BkuAURGmLjB2ADpU58ry3nbYADkw3z0BX4L6f%2Bzlzt2xEPurEx%2BrnFJTL1zhU7XLRbHqBgpYKOavK0%2FElY%2FwGF%2FlHW6KvJCDbbGSRodAtgm5qZCeCGeXa4gRKbK6yY32l3opuybH7Txg8K05Vu&X-Amz-Signature=83af9ca4979f5d440772deaae6de156a0092a6829ea5dfa1d3f36c78952c9877&X-Amz-SignedHeaders=host&x-id=GetObject)
From the scatter plot, you can observe that as engine size increases, the price of the car also increases, indicating a positive linear relationship.
![insert_image_url_here](insert_image_url_here)
___
## 2. Exploring GroupBy and Pivot Tables in Pandas
### Overview
This guide covers the basics of grouping data and transforming datasets using Pandas. The focus is on understanding the relationship between different types of drive systems (forward, rear, and four-wheel drive) and the price of vehicles. It explores the `groupby` method, creating pivot tables, and visualizing data using heatmaps.
### Grouping Data with GroupBy
The `groupby` method in Pandas is used to group data based on categorical variables, allowing for comparison of different categories by aggregating data. This example demonstrates how to group data by drive wheels and body style to find the average price of vehicles.
**Example Code**
```python
import pandas as pd

# Selecting relevant columns
df_group = df[['drive-wheels', 'body-style', 'price']]

# Grouping by 'drive-wheels' and 'body-style', then calculating the mean price
grouped_test1 = df_group.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
grouped_test1 = grouped_test1[['drive-wheels', 'body-style', 'price']]
grouped_test1.head()
```
#### Example Output
```plain text
    drive-wheels   body-style   price
0  4wd           hatchback     7603.0
1  fwd           convertible   11595.0
2  fwd           hardtop       8249.0
3  fwd           hatchback     8396.4
4  fwd           sedan         9811.5
```
![placeholder_for_image](placeholder_for_image)
### Creating Pivot Tables
To make grouped data easier to understand, it can be transformed into a pivot table. A pivot table displays one variable along the columns and another variable along the rows, making the data easier to visualize and interpret.
#### **Example Code**
```python
# Creating a pivot table
grouped_pivot = grouped_test1.pivot(index='drive-wheels', columns='body-style', values='price')
```
#### **Example Output**
```plain text
             price				
body-style   convertible    hardtop    hatchback    sedan     wagon
drive-wheels
4wd              NaN         NaN       7603.0       NaN       NaN
fwd           11595.0      8249.0      8396.4      9811.5    9997.8
rwd           23949.6     15645.0     14364.4     21711.0    16994.2
```
![placeholder_for_image](placeholder_for_image)
### Visualizing Data with Heatmaps
Heatmaps provide a graphical representation of data where individual values are represented by colors, helping in identifying patterns and relationships in the data.
#### **Example Code**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Creating a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(grouped_pivot, cmap='RdBu', annot=True)
plt.title('Title')
plt.show()
```
#### **Example Output**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BV7ALWM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQDwpYMgBX%2FuHtqVjevHEcPoYuyyrZa6kCeu3ROih1Xq5gIhAJlQBb1XeFGNrEpa2cGC6S0kyM8P%2BQTKkfrpMf%2Fqxa0aKv8DCC4QABoMNjM3NDIzMTgzODA1IgxFLXuEJ%2Bgj5oXY7AYq3AOa4LcSjBl4rAZcZGI70NDs5eQbTqjt0mqmTMgIzQpwBVOLUOc50LXV8%2BxZng7HDB%2FpUQzXgZnrwuCgaTEl3tuxliHxs2fPXprYiXlBZ54njPt51tuWtu9T3VRvxwOimpfZdV9W7GmEyzvJpXQkKJTYqYdhE2jETopoClhDgBfV7XQuwSj7fuVwdVJydea%2BQjbWIwSNO1YTcQ%2FYlyBDcPq7F4Kx%2FhYhKVvZnbwYtlm8yS7c%2BMdyGvb4orrhsa1GyjPSW85%2FcqV%2FC87Xwy9k2Z3GzWdrkvFMGu%2FtwxIu5zeMFiUf7CuzzkYX5iB2%2Bqy%2BaIcAJYEHC5Z12Dz97k0Nesczjr%2FMBnR7qzpf8wvI4U0necEdippzjX%2BeMikFgQNcUPnzWFL5Nr7lhGVjxG9tg7vyXjC9IyFwakrTZeyxPXmamYD3qJDPm8K9MWj0kLJSqcfex6imJ1K9dLYprDcCQ15wPr8tlsndf%2FDt4CA%2FwJpPcREkBZwJKZJdzLN4FWWpNvFKh7tTIN3J9Smg9ckxvP8LwUeBbO4qJeUT5%2F%2Fi1yBRCFwL754LTqG%2Bb5peHC1TptkFC0k%2FOppBvi49csuPqKRH4K0hg398jpeISgpiDWeNZi84l0hEoWdxC4OEQzDanYi9BjqkAT2UuXUNImZxVOS9LTmAKfmqOyB9eEH0Id7dT6VMZKUXFDypkuxUZvvTKULemMv2pYhN7OSXGm%2BkuAURGmLjB2ADpU58ry3nbYADkw3z0BX4L6f%2Bzlzt2xEPurEx%2BrnFJTL1zhU7XLRbHqBgpYKOavK0%2FElY%2FwGF%2FlHW6KvJCDbbGSRodAtgm5qZCeCGeXa4gRKbK6yY32l3opuybH7Txg8K05Vu&X-Amz-Signature=bca0b161a81ba0d11e068bce29bb9dae12e940c1fd0dee1e76aec5055e7b903b&X-Amz-SignedHeaders=host&x-id=GetObject)
![placeholder_for_image](placeholder_for_image)

Using the `groupby` method, pivot tables, and heatmaps provides valuable insights into the relationships between different variables in the dataset.
___
## 3. Data Visualization commands in Python
Visualizations play a key role in data analysis. This section introduces various forms of graphs and plots that you can create with your data in Python, aiding in visualizing data for better analysis.
The two major libraries used to create plots are Matplotlib and Seaborn. We will learn the prominent plotting functions of both these libraries as applicable to Data Analysis.
### Importing Libraries
You can import the libraries as shown below.
#### Matplotlib
```python
from matplotlib import pyplot as plt
```
Alternatively, the command can also be written as:
```python
import matplotlib.pyplot as plt
```
Most of the plots of interest are contained in the `pyplot` subfolder of the package. Matplotlib functions return a plot object which requires additional statements to display. While using Matplotlib in Jupyter Notebooks, it is essential to add the following 'magic' statement after loading the library to display graphs inside the notebook interface.
```python
%matplotlib inline
```
#### **Seaborn**
Seaborn is usually imported using the following statement:
```python
import seaborn as sns
```
### Matplotlib Functions
#### 1. Standard Line Plot
The simplest and most fundamental plot is a standard line plot. The function expects two arrays as input, `x` and `y`, both of the same size. `x` is treated as an independent variable and `y` as the dependent one. The graph is plotted as the shortest line segments joining the `x, y` point pairs ordered in terms of the variable `x`.
**Syntax:**
```python
plt.plot(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPV53F2V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDuPtWDbIRqHbIz1R4cNm2waXdS2B%2FRvnBZQhD5yEXxFgIgd2dXmiT9f9hWqR%2BxZKDDd7FLG4PT%2FOenfIOpCMb9Sjwq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDEzinPv78kAs8yTqlircA1Zpw5JH%2BStPBLvGOJnzNS867K9Lf1u%2BU%2FndJ4ykqnuYzBeFWTB1RH0UorxMjayMZPpTcdZApID0EbX4Sk21oStZbT25oFi%2BSo7vZF0bpsIoaZkQYNdZyN9eRQ5O3oOtRK2uSy%2FTC4iMcFC7mh7bEWGZmICxDu1JITQjbZxx4KV%2F272m5mfa44dPlaDXvS%2F32%2Bzn2gEzy1ZdKCV5oyTpdgs5HidXn8RJi2GYq38sZ1UL6KjzHijHbbX%2Bo1oEoEHX9aYSonQ4tFLhcA2LlIf62N4twEWVr4UkOiu%2Fi9Z5VE6XkYxOsb6NYvgvQRU6UBlUNmN8GryefJpUa%2BbEUjzAwcH5bKnfvrvClKPp5wlnN%2B5e02VvFGJQADm1G%2FLYMlcix3wuK6R0ej2nqE4i3LZufFqxmkgTptraBzC0mJ%2F1dWJsHSLhKkrX%2Br9XGaSb%2BOtAuR7jwrC09DgJ5V%2B7diOT2STtMIAFF6zWnjhS4F805NCPYTUX2ZO9aZgnQzBYIoJ%2B6OU55GgCZAfO3vrcFAzJ%2Fbt2z8AYp3qv49LhFzZ%2B9tpakcp0WFUDq7qoM5BFvrR%2F8rZ28DGc3ak8beBjJJHyOkfRDldpF7QR2eWy2%2FgZcSuDqquckb%2FGD7W%2Fzo8oMIKeiL0GOqUBg7b2kkDosMRBTddA0Nu679t9KkPLkqlkABFLkWMbu1e9mq7u0iI4ipVy7Q6BY8cxZLGW0KJbwn55UuBT2XYYlFIHDT30ZlNtRl3dmmQ16pM%2FQQ%2Fz63veAKFOQ1WIzeP%2FuMSe7GMqgi6594%2B9GEVaZj0z1FnjokzxDiT1uJUhiGLJT0za4ONWYSqdI8plNvy45geLgFwfiVrgVbR%2BdXRcfisdjSxn&X-Amz-Signature=9ef097c36bb2244b89b74f186a6e4a4eeeec338feb3d4ab4a4c88c790383fcf9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPV53F2V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDuPtWDbIRqHbIz1R4cNm2waXdS2B%2FRvnBZQhD5yEXxFgIgd2dXmiT9f9hWqR%2BxZKDDd7FLG4PT%2FOenfIOpCMb9Sjwq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDEzinPv78kAs8yTqlircA1Zpw5JH%2BStPBLvGOJnzNS867K9Lf1u%2BU%2FndJ4ykqnuYzBeFWTB1RH0UorxMjayMZPpTcdZApID0EbX4Sk21oStZbT25oFi%2BSo7vZF0bpsIoaZkQYNdZyN9eRQ5O3oOtRK2uSy%2FTC4iMcFC7mh7bEWGZmICxDu1JITQjbZxx4KV%2F272m5mfa44dPlaDXvS%2F32%2Bzn2gEzy1ZdKCV5oyTpdgs5HidXn8RJi2GYq38sZ1UL6KjzHijHbbX%2Bo1oEoEHX9aYSonQ4tFLhcA2LlIf62N4twEWVr4UkOiu%2Fi9Z5VE6XkYxOsb6NYvgvQRU6UBlUNmN8GryefJpUa%2BbEUjzAwcH5bKnfvrvClKPp5wlnN%2B5e02VvFGJQADm1G%2FLYMlcix3wuK6R0ej2nqE4i3LZufFqxmkgTptraBzC0mJ%2F1dWJsHSLhKkrX%2Br9XGaSb%2BOtAuR7jwrC09DgJ5V%2B7diOT2STtMIAFF6zWnjhS4F805NCPYTUX2ZO9aZgnQzBYIoJ%2B6OU55GgCZAfO3vrcFAzJ%2Fbt2z8AYp3qv49LhFzZ%2B9tpakcp0WFUDq7qoM5BFvrR%2F8rZ28DGc3ak8beBjJJHyOkfRDldpF7QR2eWy2%2FgZcSuDqquckb%2FGD7W%2Fzo8oMIKeiL0GOqUBg7b2kkDosMRBTddA0Nu679t9KkPLkqlkABFLkWMbu1e9mq7u0iI4ipVy7Q6BY8cxZLGW0KJbwn55UuBT2XYYlFIHDT30ZlNtRl3dmmQ16pM%2FQQ%2Fz63veAKFOQ1WIzeP%2FuMSe7GMqgi6594%2B9GEVaZj0z1FnjokzxDiT1uJUhiGLJT0za4ONWYSqdI8plNvy45geLgFwfiVrgVbR%2BdXRcfisdjSxn&X-Amz-Signature=e0b8414a395b4e8e8438a67ea33509a425ce9c75daf268d6e89959374395de2b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPV53F2V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDuPtWDbIRqHbIz1R4cNm2waXdS2B%2FRvnBZQhD5yEXxFgIgd2dXmiT9f9hWqR%2BxZKDDd7FLG4PT%2FOenfIOpCMb9Sjwq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDEzinPv78kAs8yTqlircA1Zpw5JH%2BStPBLvGOJnzNS867K9Lf1u%2BU%2FndJ4ykqnuYzBeFWTB1RH0UorxMjayMZPpTcdZApID0EbX4Sk21oStZbT25oFi%2BSo7vZF0bpsIoaZkQYNdZyN9eRQ5O3oOtRK2uSy%2FTC4iMcFC7mh7bEWGZmICxDu1JITQjbZxx4KV%2F272m5mfa44dPlaDXvS%2F32%2Bzn2gEzy1ZdKCV5oyTpdgs5HidXn8RJi2GYq38sZ1UL6KjzHijHbbX%2Bo1oEoEHX9aYSonQ4tFLhcA2LlIf62N4twEWVr4UkOiu%2Fi9Z5VE6XkYxOsb6NYvgvQRU6UBlUNmN8GryefJpUa%2BbEUjzAwcH5bKnfvrvClKPp5wlnN%2B5e02VvFGJQADm1G%2FLYMlcix3wuK6R0ej2nqE4i3LZufFqxmkgTptraBzC0mJ%2F1dWJsHSLhKkrX%2Br9XGaSb%2BOtAuR7jwrC09DgJ5V%2B7diOT2STtMIAFF6zWnjhS4F805NCPYTUX2ZO9aZgnQzBYIoJ%2B6OU55GgCZAfO3vrcFAzJ%2Fbt2z8AYp3qv49LhFzZ%2B9tpakcp0WFUDq7qoM5BFvrR%2F8rZ28DGc3ak8beBjJJHyOkfRDldpF7QR2eWy2%2FgZcSuDqquckb%2FGD7W%2Fzo8oMIKeiL0GOqUBg7b2kkDosMRBTddA0Nu679t9KkPLkqlkABFLkWMbu1e9mq7u0iI4ipVy7Q6BY8cxZLGW0KJbwn55UuBT2XYYlFIHDT30ZlNtRl3dmmQ16pM%2FQQ%2Fz63veAKFOQ1WIzeP%2FuMSe7GMqgi6594%2B9GEVaZj0z1FnjokzxDiT1uJUhiGLJT0za4ONWYSqdI8plNvy45geLgFwfiVrgVbR%2BdXRcfisdjSxn&X-Amz-Signature=e980959f517bddce278d39b6c11352007594db54e2d7b1d45015964555647010&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
Use an additional argument, `edgecolor`, for better clarity of plot.
___
#### 4. Bar Plot
A bar plot is used for visualizing categorical data. The y-axis represents the number of values belonging to each category, while the x-axis represents the different categories.
**Syntax:**
```python
plt.bar(x, height)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPV53F2V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDuPtWDbIRqHbIz1R4cNm2waXdS2B%2FRvnBZQhD5yEXxFgIgd2dXmiT9f9hWqR%2BxZKDDd7FLG4PT%2FOenfIOpCMb9Sjwq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDEzinPv78kAs8yTqlircA1Zpw5JH%2BStPBLvGOJnzNS867K9Lf1u%2BU%2FndJ4ykqnuYzBeFWTB1RH0UorxMjayMZPpTcdZApID0EbX4Sk21oStZbT25oFi%2BSo7vZF0bpsIoaZkQYNdZyN9eRQ5O3oOtRK2uSy%2FTC4iMcFC7mh7bEWGZmICxDu1JITQjbZxx4KV%2F272m5mfa44dPlaDXvS%2F32%2Bzn2gEzy1ZdKCV5oyTpdgs5HidXn8RJi2GYq38sZ1UL6KjzHijHbbX%2Bo1oEoEHX9aYSonQ4tFLhcA2LlIf62N4twEWVr4UkOiu%2Fi9Z5VE6XkYxOsb6NYvgvQRU6UBlUNmN8GryefJpUa%2BbEUjzAwcH5bKnfvrvClKPp5wlnN%2B5e02VvFGJQADm1G%2FLYMlcix3wuK6R0ej2nqE4i3LZufFqxmkgTptraBzC0mJ%2F1dWJsHSLhKkrX%2Br9XGaSb%2BOtAuR7jwrC09DgJ5V%2B7diOT2STtMIAFF6zWnjhS4F805NCPYTUX2ZO9aZgnQzBYIoJ%2B6OU55GgCZAfO3vrcFAzJ%2Fbt2z8AYp3qv49LhFzZ%2B9tpakcp0WFUDq7qoM5BFvrR%2F8rZ28DGc3ak8beBjJJHyOkfRDldpF7QR2eWy2%2FgZcSuDqquckb%2FGD7W%2Fzo8oMIKeiL0GOqUBg7b2kkDosMRBTddA0Nu679t9KkPLkqlkABFLkWMbu1e9mq7u0iI4ipVy7Q6BY8cxZLGW0KJbwn55UuBT2XYYlFIHDT30ZlNtRl3dmmQ16pM%2FQQ%2Fz63veAKFOQ1WIzeP%2FuMSe7GMqgi6594%2B9GEVaZj0z1FnjokzxDiT1uJUhiGLJT0za4ONWYSqdI8plNvy45geLgFwfiVrgVbR%2BdXRcfisdjSxn&X-Amz-Signature=cf0a038ec70a310d0abcd3dc3be2e2be6aa123696e3205b41d248ccbf44ee12e&X-Amz-SignedHeaders=host&x-id=GetObject)
Here, `x` is the categorical variable, and `height` is the number of values belonging to the category. You can adjust the width of each bin using an additional `width` argument in the function.
![](#)
___
#### 5. Pseudocolor Plot
A pseudocolor plot displays matrix data as an array of colored cells (known as faces). This plot is created as a flat surface in the x-y plane. The surface is defined by a grid of x and y coordinates that correspond to the corners (or vertices) of the faces. Matrix `C` specifies the colors at the vertices.
**Syntax:**
```python
plt.pcolor(C)
```
You can define an additional `cmap` argument to specify the color scheme of the plot.
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPV53F2V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDuPtWDbIRqHbIz1R4cNm2waXdS2B%2FRvnBZQhD5yEXxFgIgd2dXmiT9f9hWqR%2BxZKDDd7FLG4PT%2FOenfIOpCMb9Sjwq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDEzinPv78kAs8yTqlircA1Zpw5JH%2BStPBLvGOJnzNS867K9Lf1u%2BU%2FndJ4ykqnuYzBeFWTB1RH0UorxMjayMZPpTcdZApID0EbX4Sk21oStZbT25oFi%2BSo7vZF0bpsIoaZkQYNdZyN9eRQ5O3oOtRK2uSy%2FTC4iMcFC7mh7bEWGZmICxDu1JITQjbZxx4KV%2F272m5mfa44dPlaDXvS%2F32%2Bzn2gEzy1ZdKCV5oyTpdgs5HidXn8RJi2GYq38sZ1UL6KjzHijHbbX%2Bo1oEoEHX9aYSonQ4tFLhcA2LlIf62N4twEWVr4UkOiu%2Fi9Z5VE6XkYxOsb6NYvgvQRU6UBlUNmN8GryefJpUa%2BbEUjzAwcH5bKnfvrvClKPp5wlnN%2B5e02VvFGJQADm1G%2FLYMlcix3wuK6R0ej2nqE4i3LZufFqxmkgTptraBzC0mJ%2F1dWJsHSLhKkrX%2Br9XGaSb%2BOtAuR7jwrC09DgJ5V%2B7diOT2STtMIAFF6zWnjhS4F805NCPYTUX2ZO9aZgnQzBYIoJ%2B6OU55GgCZAfO3vrcFAzJ%2Fbt2z8AYp3qv49LhFzZ%2B9tpakcp0WFUDq7qoM5BFvrR%2F8rZ28DGc3ak8beBjJJHyOkfRDldpF7QR2eWy2%2FgZcSuDqquckb%2FGD7W%2Fzo8oMIKeiL0GOqUBg7b2kkDosMRBTddA0Nu679t9KkPLkqlkABFLkWMbu1e9mq7u0iI4ipVy7Q6BY8cxZLGW0KJbwn55UuBT2XYYlFIHDT30ZlNtRl3dmmQ16pM%2FQQ%2Fz63veAKFOQ1WIzeP%2FuMSe7GMqgi6594%2B9GEVaZj0z1FnjokzxDiT1uJUhiGLJT0za4ONWYSqdI8plNvy45geLgFwfiVrgVbR%2BdXRcfisdjSxn&X-Amz-Signature=5cc0e18625e698d8405e4bbcc641e96b3d7907bdbf788324fe12f8cea9f9613e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
### Seaborn Functions
#### 1. Regression Plot
A regression plot draws a scatter plot of two variables, `x` and `y`, and then fits the regression model and plots the resulting regression line along with a 95% confidence interval for that regression.
**Syntax:**
```python
sns.regplot(x='header_1', y='header_2', data=df)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPV53F2V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDuPtWDbIRqHbIz1R4cNm2waXdS2B%2FRvnBZQhD5yEXxFgIgd2dXmiT9f9hWqR%2BxZKDDd7FLG4PT%2FOenfIOpCMb9Sjwq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDEzinPv78kAs8yTqlircA1Zpw5JH%2BStPBLvGOJnzNS867K9Lf1u%2BU%2FndJ4ykqnuYzBeFWTB1RH0UorxMjayMZPpTcdZApID0EbX4Sk21oStZbT25oFi%2BSo7vZF0bpsIoaZkQYNdZyN9eRQ5O3oOtRK2uSy%2FTC4iMcFC7mh7bEWGZmICxDu1JITQjbZxx4KV%2F272m5mfa44dPlaDXvS%2F32%2Bzn2gEzy1ZdKCV5oyTpdgs5HidXn8RJi2GYq38sZ1UL6KjzHijHbbX%2Bo1oEoEHX9aYSonQ4tFLhcA2LlIf62N4twEWVr4UkOiu%2Fi9Z5VE6XkYxOsb6NYvgvQRU6UBlUNmN8GryefJpUa%2BbEUjzAwcH5bKnfvrvClKPp5wlnN%2B5e02VvFGJQADm1G%2FLYMlcix3wuK6R0ej2nqE4i3LZufFqxmkgTptraBzC0mJ%2F1dWJsHSLhKkrX%2Br9XGaSb%2BOtAuR7jwrC09DgJ5V%2B7diOT2STtMIAFF6zWnjhS4F805NCPYTUX2ZO9aZgnQzBYIoJ%2B6OU55GgCZAfO3vrcFAzJ%2Fbt2z8AYp3qv49LhFzZ%2B9tpakcp0WFUDq7qoM5BFvrR%2F8rZ28DGc3ak8beBjJJHyOkfRDldpF7QR2eWy2%2FgZcSuDqquckb%2FGD7W%2Fzo8oMIKeiL0GOqUBg7b2kkDosMRBTddA0Nu679t9KkPLkqlkABFLkWMbu1e9mq7u0iI4ipVy7Q6BY8cxZLGW0KJbwn55UuBT2XYYlFIHDT30ZlNtRl3dmmQ16pM%2FQQ%2Fz63veAKFOQ1WIzeP%2FuMSe7GMqgi6594%2B9GEVaZj0z1FnjokzxDiT1uJUhiGLJT0za4ONWYSqdI8plNvy45geLgFwfiVrgVbR%2BdXRcfisdjSxn&X-Amz-Signature=567bc4e83685e7f9e7bdeac342c5ab12def1f2ec2036c52a13bbaffa8a582f34&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZKXFTQF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQCAuLyK0RWQowol1PmAPrVXlIp9ZY%2BqAavsXLPJUC%2BOfwIgcWZdiqFdzYkaRdeg03bgikjChIHn%2FXsDhgDG6Fo3H4kq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDKhxZ1O1g2buy3GjgyrcA0HCfYBf4RYdLh7G4BQwhgi0iKDYZbnjKkq9IYTVuiKO%2Bvz3p1oS%2BqJnCcPtA12W40%2FfWoVm%2BdUSemRNaIgnuvXfmk9X2ImvvGkyrqAMuzeRDsstGpuJrc1ONa6d8567H414kwHDgH0%2FHP15v8%2FhKxdxeJ4Jvy%2FycTO74JQqFOdY%2FFzxAnNITwzwVWcusRriJa3l7koqaW79Q%2BI7NA%2Bee%2B0n09S%2FtH1ec1K6XcKbWrp8%2FJwcO3B04dqYHccSB9M2EInnPGdriwyIxFzzwT3hQiHn7D1XJdh0eI3qGrq4EZS%2Bhu8eVmkhWP%2FYFeFdhtoFD0OuOS6vVNhr4VyRtxo0W51b%2FmTygqxhfeIIjEiz%2BahfVyC%2BYvMZs68rVnHqZHWRswzHU8SOsSQdYbmPQVrSW026ePHWN33g%2FJfX%2FgO8bEWB8uGzYcxarba5uGHjipdV9uxc8WSK86Sz4SprfTDW8Il9RqjjrQ9MVogLohYf1fBA%2F8qVj7WwSB2R1p%2FmZlA4FiHXK0PUbHLIfk0XjaUVyGEhkpZ3rHPb%2Fl3vB9G6aWt4K7dvcmK8%2Ffd9NbZ7U5lqFU9qo7rKVj8yLT77QoyOIstQddUqy8ggt84T8Lc43NzOCP1BnA9wzFABDDjwMKKeiL0GOqUBFZV4Fdx2eg8OXaZpe4%2BvavSA3J0ytZDlZFoy8LVu5K%2FmiP1qJ%2F7GWrjL0MAvkOLYlvnjTVHMDIE6EP5SlM7KR2pkmzANDDtwEmNexfXxJqeyoff9YWsw9Fe2%2ByI9VQcv%2Fzd5UfsK1EN%2BNDY7SSvD7tvk0A6OydRR3kOACvYFQPSagEVvcQf6TVr2mRqFnY6L98NrOjQMC0YDKnlM7VAzJWWkET4%2F&X-Amz-Signature=31f5320e3979700b1c5a8fb0def4e69442086418748d3b0fb6bf641d184eeb71&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZZYWCQJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQCL5Uy0aPg9OR%2FfIIDbz7asVulzXJo%2FclcbU8%2FqJqO4lQIgPSK5QoBLc7RJgoMxieopnwMLknKNDYTLqureHsprVR8q%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDA12gLIjQljuqyMnLCrcA7EztrZE%2Bs%2B4cHnP96MhaBMaPpOc919epUim7usYKfUEtFYUjzh9pvl0zidT9RK5vhn4AkLyuZoGLIDQSzPrJpUta2J9yfm7mgjayWdQn6OUVtWuWEP1slrET%2BM5K0rLmlzS0IFpMnj4k%2F4%2Fxp1bbZh6v1Qh%2F0xa2T60lJLCJ%2FbOlWdQWrkW2OfZXVWzSbr4SXfiqWYWxUauuSC7A7jwiGyq596uNk%2B6GRqOTkoN3NUrisnzzR1E7m8ggqm2Z5KlPvIzB6Ht6T08aGQ26nxpHc4zO95Ww62kpNm4g8oUO1kgQzqG1baJRzn%2BJh%2BDiQC3O4wJcuRry0Q1exJ7CZ6cASgd2hNR0mtB0K4kjZsWocgT2OZNnKX%2F%2Blp8uMJWWlVEPXBiRqhJrj0QaW7fD7s7XoxEIlVofxtsF8sAMZJChncogZ7IH2aCyq0bR4H8040hoz5TkhNh3pz%2F6aZDtwa7yDjUbKiF41cWVfzyhZHd3xn0e1ZUsNKylX6VV6QY%2F7VlMc%2FCI7G27nZItxzS6PN716dLHCeijSW6G0fzB5mXc4jabAiXHxlncspx3sVKJtI6eKIp84zLI39n4RJZD19TiES0B1lPBjqu5bbR2WXWY302Riz0D7vq7M%2BqHaJ0MNWdiL0GOqUB0a9XjTqvYmy5aCfmPHiLOlCA4uV5yYdXJcp8mhht3pyWPJCusjCKtcCrmSuvN0oMGO1BqLD8MFCRSLV1XP1tQXUaDpSxYor0i%2Bc3Msnu%2FUPJ4m4h%2BwoBA%2FGRhR4qZJZgNqr9RTL%2F%2FHhzjyNMvGaGwiA7nhxteelQvEes4xHtSBhR3%2B83Z4b8bqNOf21hwxoOjXqUwLFQGqyJZkGfoeIFS85vd3u9&X-Amz-Signature=2c5508a0c60cf468aa1de01cf364fb61b89a8ad6b2b34b61609bfd591d62416c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Residual Plot
A residual plot is used to display the quality of polynomial regression. This function regresses `y` on `x` as a polynomial regression and then draws a scatter plot of the residuals.
**Syntax:**
```python
sns.residplot(data=df, x='header_1', y='header_2')
```
Alternatively:
```python
sns.residplot(x=df['header_1'], y=df['header_2'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPV53F2V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDuPtWDbIRqHbIz1R4cNm2waXdS2B%2FRvnBZQhD5yEXxFgIgd2dXmiT9f9hWqR%2BxZKDDd7FLG4PT%2FOenfIOpCMb9Sjwq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDEzinPv78kAs8yTqlircA1Zpw5JH%2BStPBLvGOJnzNS867K9Lf1u%2BU%2FndJ4ykqnuYzBeFWTB1RH0UorxMjayMZPpTcdZApID0EbX4Sk21oStZbT25oFi%2BSo7vZF0bpsIoaZkQYNdZyN9eRQ5O3oOtRK2uSy%2FTC4iMcFC7mh7bEWGZmICxDu1JITQjbZxx4KV%2F272m5mfa44dPlaDXvS%2F32%2Bzn2gEzy1ZdKCV5oyTpdgs5HidXn8RJi2GYq38sZ1UL6KjzHijHbbX%2Bo1oEoEHX9aYSonQ4tFLhcA2LlIf62N4twEWVr4UkOiu%2Fi9Z5VE6XkYxOsb6NYvgvQRU6UBlUNmN8GryefJpUa%2BbEUjzAwcH5bKnfvrvClKPp5wlnN%2B5e02VvFGJQADm1G%2FLYMlcix3wuK6R0ej2nqE4i3LZufFqxmkgTptraBzC0mJ%2F1dWJsHSLhKkrX%2Br9XGaSb%2BOtAuR7jwrC09DgJ5V%2B7diOT2STtMIAFF6zWnjhS4F805NCPYTUX2ZO9aZgnQzBYIoJ%2B6OU55GgCZAfO3vrcFAzJ%2Fbt2z8AYp3qv49LhFzZ%2B9tpakcp0WFUDq7qoM5BFvrR%2F8rZ28DGc3ak8beBjJJHyOkfRDldpF7QR2eWy2%2FgZcSuDqquckb%2FGD7W%2Fzo8oMIKeiL0GOqUBg7b2kkDosMRBTddA0Nu679t9KkPLkqlkABFLkWMbu1e9mq7u0iI4ipVy7Q6BY8cxZLGW0KJbwn55UuBT2XYYlFIHDT30ZlNtRl3dmmQ16pM%2FQQ%2Fz63veAKFOQ1WIzeP%2FuMSe7GMqgi6594%2B9GEVaZj0z1FnjokzxDiT1uJUhiGLJT0za4ONWYSqdI8plNvy45geLgFwfiVrgVbR%2BdXRcfisdjSxn&X-Amz-Signature=d485b802fb07f7c4e3fcd7cb7f6b47e6d7b14e9120cb3802ba2386cd4c05f091&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPV53F2V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDuPtWDbIRqHbIz1R4cNm2waXdS2B%2FRvnBZQhD5yEXxFgIgd2dXmiT9f9hWqR%2BxZKDDd7FLG4PT%2FOenfIOpCMb9Sjwq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDEzinPv78kAs8yTqlircA1Zpw5JH%2BStPBLvGOJnzNS867K9Lf1u%2BU%2FndJ4ykqnuYzBeFWTB1RH0UorxMjayMZPpTcdZApID0EbX4Sk21oStZbT25oFi%2BSo7vZF0bpsIoaZkQYNdZyN9eRQ5O3oOtRK2uSy%2FTC4iMcFC7mh7bEWGZmICxDu1JITQjbZxx4KV%2F272m5mfa44dPlaDXvS%2F32%2Bzn2gEzy1ZdKCV5oyTpdgs5HidXn8RJi2GYq38sZ1UL6KjzHijHbbX%2Bo1oEoEHX9aYSonQ4tFLhcA2LlIf62N4twEWVr4UkOiu%2Fi9Z5VE6XkYxOsb6NYvgvQRU6UBlUNmN8GryefJpUa%2BbEUjzAwcH5bKnfvrvClKPp5wlnN%2B5e02VvFGJQADm1G%2FLYMlcix3wuK6R0ej2nqE4i3LZufFqxmkgTptraBzC0mJ%2F1dWJsHSLhKkrX%2Br9XGaSb%2BOtAuR7jwrC09DgJ5V%2B7diOT2STtMIAFF6zWnjhS4F805NCPYTUX2ZO9aZgnQzBYIoJ%2B6OU55GgCZAfO3vrcFAzJ%2Fbt2z8AYp3qv49LhFzZ%2B9tpakcp0WFUDq7qoM5BFvrR%2F8rZ28DGc3ak8beBjJJHyOkfRDldpF7QR2eWy2%2FgZcSuDqquckb%2FGD7W%2Fzo8oMIKeiL0GOqUBg7b2kkDosMRBTddA0Nu679t9KkPLkqlkABFLkWMbu1e9mq7u0iI4ipVy7Q6BY8cxZLGW0KJbwn55UuBT2XYYlFIHDT30ZlNtRl3dmmQ16pM%2FQQ%2Fz63veAKFOQ1WIzeP%2FuMSe7GMqgi6594%2B9GEVaZj0z1FnjokzxDiT1uJUhiGLJT0za4ONWYSqdI8plNvy45geLgFwfiVrgVbR%2BdXRcfisdjSxn&X-Amz-Signature=acf9a43348617e4d290a4b554dcaa122ef14744fc2fd4704d9cd3eb361a1de29&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 5. Distribution Plot
This plot has the capacity to combine the histogram and the KDE plots. This plot creates the distribution curve using the bins of the histogram as a reference for estimation. You can optionally keep or discard the histogram from being displayed.
**Syntax:**
```python
sns.distplot(X, hist=False)
```
Keeping the argument `hist` as `True` would plot the histogram along with the distribution plot.
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPV53F2V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDuPtWDbIRqHbIz1R4cNm2waXdS2B%2FRvnBZQhD5yEXxFgIgd2dXmiT9f9hWqR%2BxZKDDd7FLG4PT%2FOenfIOpCMb9Sjwq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDEzinPv78kAs8yTqlircA1Zpw5JH%2BStPBLvGOJnzNS867K9Lf1u%2BU%2FndJ4ykqnuYzBeFWTB1RH0UorxMjayMZPpTcdZApID0EbX4Sk21oStZbT25oFi%2BSo7vZF0bpsIoaZkQYNdZyN9eRQ5O3oOtRK2uSy%2FTC4iMcFC7mh7bEWGZmICxDu1JITQjbZxx4KV%2F272m5mfa44dPlaDXvS%2F32%2Bzn2gEzy1ZdKCV5oyTpdgs5HidXn8RJi2GYq38sZ1UL6KjzHijHbbX%2Bo1oEoEHX9aYSonQ4tFLhcA2LlIf62N4twEWVr4UkOiu%2Fi9Z5VE6XkYxOsb6NYvgvQRU6UBlUNmN8GryefJpUa%2BbEUjzAwcH5bKnfvrvClKPp5wlnN%2B5e02VvFGJQADm1G%2FLYMlcix3wuK6R0ej2nqE4i3LZufFqxmkgTptraBzC0mJ%2F1dWJsHSLhKkrX%2Br9XGaSb%2BOtAuR7jwrC09DgJ5V%2B7diOT2STtMIAFF6zWnjhS4F805NCPYTUX2ZO9aZgnQzBYIoJ%2B6OU55GgCZAfO3vrcFAzJ%2Fbt2z8AYp3qv49LhFzZ%2B9tpakcp0WFUDq7qoM5BFvrR%2F8rZ28DGc3ak8beBjJJHyOkfRDldpF7QR2eWy2%2FgZcSuDqquckb%2FGD7W%2Fzo8oMIKeiL0GOqUBg7b2kkDosMRBTddA0Nu679t9KkPLkqlkABFLkWMbu1e9mq7u0iI4ipVy7Q6BY8cxZLGW0KJbwn55UuBT2XYYlFIHDT30ZlNtRl3dmmQ16pM%2FQQ%2Fz63veAKFOQ1WIzeP%2FuMSe7GMqgi6594%2B9GEVaZj0z1FnjokzxDiT1uJUhiGLJT0za4ONWYSqdI8plNvy45geLgFwfiVrgVbR%2BdXRcfisdjSxn&X-Amz-Signature=deeac3c0ad0b86eb4c20c78cfbb64d46cb7bb967d063b7e6b7629e2fed2341ce&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMIOEDMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDUCIIEXQluU1g1%2F2rYGjjRgtFi5kek9E6yh0hY%2FVv2bgIgVxlOGOa5RxBTd9rIYEYleKQEkSxYqbfThy8QaukZNpsq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDEAy50pu%2F4S8t0mJLyrcA%2F0Cfjkd5nIl2KgiL0%2FyOola94cjQNGxh3C%2BxwXJ3Kjb6Jes4n%2F2K14M3zH1SM5iUTKVFB7piN3lpm92ygzQe5vC1qgmRNcdEW48kiYTXs9n%2Fil2zs86FU6Xi9lk4NlhqlpljQRK40n%2BcF5ccwhUmm1%2BV8iqzy%2BqOedjIfifaBKUo7mdtz5EWWx1RBFTHg0%2FMLri9RGeX%2FM%2BiKZnmYam1GfTJjoGqKMDAwnBOEMcg8NrfUKUCu2DBj9%2Bl10ErWNhv3VftEQvPVksvh7O0G6O7Cv8uz7xJWaO9D40YOgHflj2%2B2rAm%2FkUn%2BDuJARviGTKNGf0q69SnqG9WlahCEg2HkSDyDMiDJUfkxAl6t9MZk3ZAp7968uzbuZtszXiWa4J0CJo4qar%2BoPTUKI%2BRqBSKTGhuuu2Ics%2FKxF4KsdHaxhRURp0Nz90taaVUXOYTH65Y5RlbALCnzkO06KjeMdHMsg1lYDD4nl8Wa4dR1R3v%2BG0R3ArbXykTp%2F6TjC47Fue9roTZvGzViClsxWSBVRFvvy1v%2Fv2vGYZu4dUF7rQ95aYUlKbeWNxj1PFIPGsXASd8Xu2zcIrEFOESWu4hlsFfdCzMopxHxr1gsHqmobtMv0p8w67Sa%2FZGt7Z7djSMLCeiL0GOqUBkcu8MrNuj5lLTZYzbuxWvSWQf%2Fcc0jrbX9CZABLVg%2Fj8qJZD3xgNYTIgrnIyz51K7rvU5dZM5EYuR%2FTiluFt7mn7RgAux5lMwhXCCRAQoXBlJxIcDG%2FkS%2FzhnICAeJW4NkQ9CROQ%2FpatZbVGih4%2FN2D8QtlRxXp8lPSUiR4zIdJnWNKWFOGqA9ZNtfdE2a4vpF7SPLMQMzWr1AqTC5%2BEjU6qG0ZI&X-Amz-Signature=961922ff8dde878046c7fe95a4a8e728a207747d4155e0ded0dce5845f07e8db&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB3A7TNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIAU%2Bs9SGuUK%2FlSmFynrAJOpMkBDyvTXMWsw3sS5gllbEAiEA6M4CUWQVpgXNiMcMGhovL6EGgPb8OnktQUi%2B%2BZRjl%2F0q%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDLp2oJsvxpwSFHMBqyrcA5dJf0FmRPjrS5c68LrRk1KI2zry2gtXLGg%2Fbt60jnTrn0%2F975qnrUKriem%2FvDk1aQCfK4zawZdqg4bj%2BtxrpTUvt%2BIuu72PxetuDyCI%2BtkjtPhfAyTRGK%2FPy4x7Qg9OCzBuLUy9ve5afwz0JXDeWn0q0Ar60i4YAKXrWoIvF4s7gO26R89vi5Yw62QFEz8duCCaBOrW8utmKMwxvaHBeMa%2BbM%2FSDsvmhCSWRXYlRfgEbw%2Fh8EZEXAAf%2FIYca04uGJRz%2FpCeif3eY8SSOmHXnsIvyWO%2FiAqu6RewSxSrN%2FVBkWgqt14oSfcGINx5l1lk6jTpqJstaBV6Yxt7Ltgu7cfsPY7Um2BrLw2QgQr%2FbnHORc9mxeMKA9jPdWNYHtA%2FvmsARmK87C6G24m2IdaXtDJUywVFQEG0Y1o5RtzUNKmqQjo1Fd0pzHRBqdGPnzW63%2BNMFaLN64R1pOf3A0Uid9PxW1xW5%2BotdP9xVlO6dXPirkudnNKPmngFZ5jSkVGq6wy1a8Ni5F%2BZLQAZRRKvY%2FjHerju5BbWSSllcI3dbjlXUn7ZHRHFMLkhX1PgzKPKhIzJkV2aLLfVftHjXDhUifn0VONqxcZvhTPdxvpO0STU3G4%2Bl57jsaUR8DItMLOeiL0GOqUBB8Q1qO%2FjD%2Ff2jrSDFEtYj6ww3o3%2BGDyUjH0zLxTlDdB167BNAJs9FHr81kyiSN3%2BHV1ItaQRuPTQElydqVe%2B8M1zH6nHsozyOIPKr5lLTa3uz3Dmn8fMi32cP6DzjJ4b4ZFd%2BoZSFFeTje4e2xHq9UC4zWg92VJGE6oHQS6ScpoKh3EN%2F00sIM9LYfbxjHzLJlLyeU%2BrUfmNuqmOyW0FjFaJA6fW&X-Amz-Signature=faa2fdf5c61f9f16faf6223e4455088f72eefc09d5627f1497ff3a42c894b28c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AR6KX6T%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQDVHO%2BJvwEtluzl7csgu3DIb7z31ES%2BcJ6P6JypiKKr1AIhAL%2FuXC%2FAu%2Fjn8Xlo3sgeyFLhCeVyUSiauZyJQwtzI6e%2BKv8DCC4QABoMNjM3NDIzMTgzODA1IgxkuAK5FMvCvnkLILgq3AMYCfshpddqfN9Q5b000Cwzm2926Nq2sOrrICo0Sz7zZOYuLUnNOXCLb63PypIFMmfQWTg2Ip1RgpH%2BJ%2F3276A3pUsOhPA32ihQ8WztPWrxDr%2FYrhwj4tCqDsxzpHgwg5B%2Fsh9or2%2FiGKfNbs%2F%2BGoB91PLcvSIDJYrVl7jE4vbBRSkbqvMNrCW3v5XQAbY%2B8woKY%2BuYW31dyZpgBhrzrssCjbTS9iIOuJVEr96uRUdK6rqH6tBofzQFNT37mXP9MJhzKWcE7cUaQPYH1LxxnUlrb9hOdmvJMrLTPHetLA9UjuUiFmDlCNALo81E9sB6HFeCUBpcSCrQgKxwolhRHzOeT3INFrXYSYRtH80REcObHZk2OfHvs%2FnCVr6HBIXs%2F8j1Kav0fl8fXP5lV0adB7%2B36B3uxYSzCnbNViDO436BP2iKQ80%2Fbxc2zWKr%2F6s%2BjkmmaWzINTZuLqJmbFvNClgjlywjvqYtm0398VTv%2FdIxb%2BHpnELbqFq5u4jzyMiD5TqUK8M7J9lsZ6PkJEETGkNXX%2FGx4NluC8AdwaZL3ZTDiOUXMaVxxUbnLOw2leRGhUvJFrOk%2F53fbRhIv%2B%2BUWWPJ87MlzO9YEFdjN0AQjojh%2FHQ5OPBegTWVtFKPjjDonYi9BjqkAbSXPdTztKYF49C5TExt642AG069gTHLgKGIIDDjTHIzGo3Zzn29HtO9nVk25rl7UzIfO5YzyqkJlMrR5LKADfHBCSK9%2FJaofPbjuv7p0buBMmvww2A%2BiemFuzDE2D2ovdLD6SlBr4LQSo7up%2BHk9di%2BJPk8tD3DaQIycAtZUAv5uUBhsd2TwbhbzsUaTW5zYsn1HOCsVadB5s6OgV8ZhnMcfqAj&X-Amz-Signature=05332dcb3d45a7fc7263cd5429ed19ab2df0f24629c1f0dfdba3ed9e73e9dcd6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** RPM (engine revolutions per minute) does not strongly predict the price of the vehicle. Both low and high RPM values can be associated with a wide range of prices, indicating that RPM alone is not a reliable indicator of vehicle price.
### **Important Note**
Correlation does not imply causation. It signifies a relationship but does not determine cause and effect.
___
## 5. Correlation Statistical Methods
Introduction to various correlation statistical methods. One method to measure correlation between continuous numerical variables is Pearson Correlation.
### Pearson Correlation
Pearson Correlation is a statistical measure that quantifies the strength and direction of the linear relationship between two continuous variables. It assesses how much one variable changes when the other variable changes. In other words, The Pearson Correlation measures the linear dependence between two variables `X` and `Y` . The resulting coefficient is a value between -1 and 1 inclusive. 
Pearson Correlation provides:
- **Correlation Coefficient:** Indicates strength and direction of correlation.
- **p-value:** Indicates certainty of correlation coefficient.
#### Interpreting Results
- **Correlation Coefficient:**
	- Close to 1: Large positive correlation.
	- Close to -1: Large negative correlation.
	- Close to 0: No correlation.
- **p-value:**
	- < 0.001: Strong certainty.
	- 0.001 - 0.05: Moderate certainty.
	- 0.05 - 0.1: Weak certainty.
	- > 0.1: No certainty.
#### Example: Horsepower and Car Price
Example examines correlation between horsepower and car price using Pearson Correlation. Correlation coefficient is approximately 0.8, indicating strong positive correlation. p-value is much < 0.001, confirming strong certainty.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYPKPCB5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQCnszYuw0q4Dh1kZXlUrGPpVENzrHQ11jf1AIGTDPj%2B3wIgcmqK5aIY3MCZKLlFj%2Buq%2Bccye5S5ZKYYUdHDjZuSskAq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDD%2B27e9sDhIwwaE9ZyrcA1wa3o5KMqHTIRuVeGcB03btzC9nl7ZQq1Th%2FE1Whg%2BSgH3SJ4eqPH49asI%2BxRYK59W5PlbesekEADkPPrAoc9dXFmqaL9vPOvMJ0T74YvYRiKNY0UH%2F4tHjmYmJuuAz%2FdzGAo%2BndJ2I7g26pdgcqpDzrULqUb43ZpILAA%2BlbstjXrjanoFaxcrlGffbCtj12e97kRqi%2BapZGUvaYBQfQNS0J5wQgsm4sQ0wg2ONFO62%2FoQGaRbXL2HoYR7G1wo7RzK2r2dbDMEZTE580lcdr%2Bic1fz3nLeTkeIB9lNIl0wX1ljLc%2B%2FmPnWM1B%2FmiHc2bGLUabTi2DJ3xJbbawspbFia8lmkhzTp2STxNEvAVqm3z8HSwChB29ncZhjFnGYEiHmG45w7nvUycxjLMw%2FnOoyiEr60G3ApSGDW3z8YcN9%2BBQx%2FaOo0VhGEvXDPY5sKsscyarH0qaENh5oERGZje97FsU%2BIpN8sGVPVfu%2FCc84xn75sjxNZg0qWgS%2BDXhtFyFk%2FoyUCf6%2FP9QAA7cxugmFsytF%2BoRDmytlN905FaOtccX2Wi0gvF%2B%2BmqQseFsovemzkPftbYr0%2BBQ3w1pDzD234dJ%2Fc%2Fp88W57kcwl4g2FR53PZJW%2Bh1J7ZFgLfMI6eiL0GOqUBKqLW965gBKfcJoug%2FThJUcff57Y8CUZLJkENZVqtQZzPorqfm2AbNRBtGdYjpAGH30UmlzrbQop1Eax0yctO%2F9sBdW%2F%2BJE0dAWhu1RTt0P5FsmAkROz3Wuh6cNC3GSiVGZzQreJfdQYMPfH4xzQpaJUt8YKehQLMBYqmdo2%2FoEEVWeKpwIo%2F1biUZmdE%2FbVlssKjn0z8wqslz9jV25mW3KI%2FYNy4&X-Amz-Signature=79313554af24d094e95ba938d7d444d2df0c6de8623ef390f017678861d5191f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYPKPCB5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQCnszYuw0q4Dh1kZXlUrGPpVENzrHQ11jf1AIGTDPj%2B3wIgcmqK5aIY3MCZKLlFj%2Buq%2Bccye5S5ZKYYUdHDjZuSskAq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDD%2B27e9sDhIwwaE9ZyrcA1wa3o5KMqHTIRuVeGcB03btzC9nl7ZQq1Th%2FE1Whg%2BSgH3SJ4eqPH49asI%2BxRYK59W5PlbesekEADkPPrAoc9dXFmqaL9vPOvMJ0T74YvYRiKNY0UH%2F4tHjmYmJuuAz%2FdzGAo%2BndJ2I7g26pdgcqpDzrULqUb43ZpILAA%2BlbstjXrjanoFaxcrlGffbCtj12e97kRqi%2BapZGUvaYBQfQNS0J5wQgsm4sQ0wg2ONFO62%2FoQGaRbXL2HoYR7G1wo7RzK2r2dbDMEZTE580lcdr%2Bic1fz3nLeTkeIB9lNIl0wX1ljLc%2B%2FmPnWM1B%2FmiHc2bGLUabTi2DJ3xJbbawspbFia8lmkhzTp2STxNEvAVqm3z8HSwChB29ncZhjFnGYEiHmG45w7nvUycxjLMw%2FnOoyiEr60G3ApSGDW3z8YcN9%2BBQx%2FaOo0VhGEvXDPY5sKsscyarH0qaENh5oERGZje97FsU%2BIpN8sGVPVfu%2FCc84xn75sjxNZg0qWgS%2BDXhtFyFk%2FoyUCf6%2FP9QAA7cxugmFsytF%2BoRDmytlN905FaOtccX2Wi0gvF%2B%2BmqQseFsovemzkPftbYr0%2BBQ3w1pDzD234dJ%2Fc%2Fp88W57kcwl4g2FR53PZJW%2Bh1J7ZFgLfMI6eiL0GOqUBKqLW965gBKfcJoug%2FThJUcff57Y8CUZLJkENZVqtQZzPorqfm2AbNRBtGdYjpAGH30UmlzrbQop1Eax0yctO%2F9sBdW%2F%2BJE0dAWhu1RTt0P5FsmAkROz3Wuh6cNC3GSiVGZzQreJfdQYMPfH4xzQpaJUt8YKehQLMBYqmdo2%2FoEEVWeKpwIo%2F1biUZmdE%2FbVlssKjn0z8wqslz9jV25mW3KI%2FYNy4&X-Amz-Signature=ee742a618a084d045197188dffd30fe377c8595efc73b16ef9fff87c9bc41cb2&X-Amz-SignedHeaders=host&x-id=GetObject)

**Note:** To calculate the Pearson Correlation Coefficient and P-value, use statistical functions available in Python libraries like `scipy.stats.pearsonr`.
```python
from scipy import stats

# Example calculation
x = df['horsepower']
y = df['price']
pearson_corr, p_value = stats.pearsonr(x, y)

print(f"Pearson Correlation Coefficient: {pearson_corr}")
print(f"P-value: {p_value}")
```
___
## Chi-Square Test for Categorical Variables
#### Introduction
The chi-square test is a statistical method used to determine if there is a significant association between two categorical variables. This test is widely employed in fields such as social sciences, marketing, and healthcare to analyze survey data, experimental results, and observational studies.
#### Concept
The chi-square test assesses the association between two categorical variables by comparing observed and expected frequencies. It evaluates whether the observed deviations from expected frequencies could have occurred by chance.
#### Null Hypothesis and Alternative Hypothesis
- **Null Hypothesis (𝐻₀)**: Assumes no association between variables, attributing differences to random chance.
- **Alternative Hypothesis (𝐻₁)**: Assumes a significant association between variables, indicating observed differences are not due to chance alone.
#### Formula
The chi-square statistic (𝜒²) is calculated as:
$$ χ2=∑(Oi−Ei)2Ei\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}χ2=∑Ei(Oi−Ei)2 $$
where:
$$ O_i \text{ = Observed frequency for category } i \\ E_i \text{ = Expected frequency for category } i $$
___
## **Cheat Sheet: Exploratory Data Analysis**
### Complete Dataframe Correlation
Correlation matrix created using all attributes of the dataset.
```scss
df.corr()
```
### Specific Attribute Correlation
Correlation matrix created using specific attributes of the dataset.
```python
df[['attribute1', 'attribute2']].corr()
```
### Scatter Plot
Create a scatter plot using the data points of the dependent variable along the x-axis and the independent variable along the y-axis.
```shell
import matplotlib.pyplot as plt
plt.scatter(df['attribute1'], df['attribute2'])
```
### Regression Plot
Uses the dependent and independent variables in a Pandas dataframe to create a scatter plot with a generated linear regression line for the data.
```kotlin
import seaborn as sns
sns.regplot(x='attribute1', y='attribute2', data=df)
```
### Box Plot
Create a box-and-whisker plot that uses the pandas dataframe, the dependent, and the independent variables.
```kotlin
import seaborn as sns
sns.boxplot(x='attribute1', y='attribute2', data=df)
```
### Grouping by Attributes
Create a group of different attributes of a dataset to create a subset of the data.
```lua
df_group = df[['attribute1', 'attribute2', ...]]
```
### GroupBy Statements
- a. Group the data by different categories of an attribute, displaying the average value of numerical attributes with the same category.
- b. Group the data by different categories of multiple attributes, displaying the average value of numerical attributes with the same category.
```css
a. df_group.groupby(['attribute1'], as_index=False).mean()
b. df_group.groupby(['attribute1', 'attribute2'], as_index=False).mean()
```
### Pivot Tables
Create Pivot tables for better representation of data based on parameters.
```perl
df_group.pivot(index='attribute1', columns='attribute2')
```
### Pseudocolor Plot
Create a heatmap image using a Pseudocolor plot (or pcolor) using the pivot table as data.
```javascript
import matplotlib.pyplot as plt
plt.pcolor(grouped_pivot, cmap='RdBu')
```
### Pearson Coefficient and p-value
Calculate the Pearson Coefficient and p-value of a pair of attributes.
```css
from scipy import stats
pearson_coef, p_value = stats.pearsonr(df['attribute1'], df['attribute2'])
```
___
