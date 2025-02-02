

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YC55IDQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICW3j5roNhAk8DLNVQnmQSwsbCERpOBw5orwx0om6ggLAiEA9%2BNg%2BqB0%2BW4zbJqO%2F4NIA22QveAMQuhgHev8Mt1lYQsqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDChL7VXSsoVKvTqexCrcA7rjrUnqVhoD0lZBh6zhlJsK15yQZGUhSmGrh1R8lNfkTvYTJuDI0Urz9gIdwh6lzOM%2BtD%2FTtnKMybyCnfHNsv3gFZJMBhUJe7RTcULOfnLMNmd9BQxH7MuWkCAUspEcmjo4a7wvEvBcCQR6v5AtOGR8hKxMAwluFkn2r37GFbP8Tt7b0gC3B21qbfhXpqfc8UWKXoAtGCwsJMcpxcPK4q9oco704NHb0TgKWHmAjlhWI3Abp91pY4LY16KjpirhLkMgU7fL7GuPprtgy%2BMwvCaljZOJr7Y3Dbt636%2BP%2FVoLU3LkkcKGOQjEUfz04rraXW6NtsqLmZjdy3%2BTks6xDJUmhGlm38wqmQQ0Tf9CzHo3ltvhYZf0XoQyTT%2FoLAq7GWMvxopt7zMW8Brb%2Fl3xGQ0k0dL8EsUILQigGUqCxmghcHkGYSDmnMizZMMqfzgPYaXiAsj0mnMUaSj5av44l6C5grMMX%2FgmXKPNzIvYOepCSFyrHUzDRY%2F0NXNPVAFPSUGy4jwsHkDm99cOrFgDZ1CE%2FUhAOvb017APYt9%2FNs7cwT7KFlDIC9aibLuFrqCaEX6vSLCwpnvZMbg6E6eOvl5B8qZgwkpfoiZ1WSCO81lyJAIwTp2nOTWq4S6mMJKU%2FrwGOqUBoK96O%2BXCg6nVE1ZPOtFTswK7iPFSiq0W%2FVrShWlAZB4OjOt1VuFlBSeL2JzWUC1weSusvx8vpnmbNaAXWi9ubRjWcE7Xm3WF8SIKqP95LhaYfUou0YSz7Z6N2bl2Q5XcLgtHAAEmkQ6sv%2F480ENF1uuHXi1zMlIgLca91WZ%2Bpap4MaYN%2B8gIPw5L3Th7BewJZPHHiqvVPwyH%2BfmrtAV53J0k%2BVqO&X-Amz-Signature=c5548d622e04b3a17bfd618d1cbf2d0b03b3abfa44fd04a9e6807ab08eaccacf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YC55IDQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICW3j5roNhAk8DLNVQnmQSwsbCERpOBw5orwx0om6ggLAiEA9%2BNg%2BqB0%2BW4zbJqO%2F4NIA22QveAMQuhgHev8Mt1lYQsqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDChL7VXSsoVKvTqexCrcA7rjrUnqVhoD0lZBh6zhlJsK15yQZGUhSmGrh1R8lNfkTvYTJuDI0Urz9gIdwh6lzOM%2BtD%2FTtnKMybyCnfHNsv3gFZJMBhUJe7RTcULOfnLMNmd9BQxH7MuWkCAUspEcmjo4a7wvEvBcCQR6v5AtOGR8hKxMAwluFkn2r37GFbP8Tt7b0gC3B21qbfhXpqfc8UWKXoAtGCwsJMcpxcPK4q9oco704NHb0TgKWHmAjlhWI3Abp91pY4LY16KjpirhLkMgU7fL7GuPprtgy%2BMwvCaljZOJr7Y3Dbt636%2BP%2FVoLU3LkkcKGOQjEUfz04rraXW6NtsqLmZjdy3%2BTks6xDJUmhGlm38wqmQQ0Tf9CzHo3ltvhYZf0XoQyTT%2FoLAq7GWMvxopt7zMW8Brb%2Fl3xGQ0k0dL8EsUILQigGUqCxmghcHkGYSDmnMizZMMqfzgPYaXiAsj0mnMUaSj5av44l6C5grMMX%2FgmXKPNzIvYOepCSFyrHUzDRY%2F0NXNPVAFPSUGy4jwsHkDm99cOrFgDZ1CE%2FUhAOvb017APYt9%2FNs7cwT7KFlDIC9aibLuFrqCaEX6vSLCwpnvZMbg6E6eOvl5B8qZgwkpfoiZ1WSCO81lyJAIwTp2nOTWq4S6mMJKU%2FrwGOqUBoK96O%2BXCg6nVE1ZPOtFTswK7iPFSiq0W%2FVrShWlAZB4OjOt1VuFlBSeL2JzWUC1weSusvx8vpnmbNaAXWi9ubRjWcE7Xm3WF8SIKqP95LhaYfUou0YSz7Z6N2bl2Q5XcLgtHAAEmkQ6sv%2F480ENF1uuHXi1zMlIgLca91WZ%2Bpap4MaYN%2B8gIPw5L3Th7BewJZPHHiqvVPwyH%2BfmrtAV53J0k%2BVqO&X-Amz-Signature=5da507cdc7fe6f7e8f92aa11e80a2428bbcef20cac1f889690d6e03217e96b9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YC55IDQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICW3j5roNhAk8DLNVQnmQSwsbCERpOBw5orwx0om6ggLAiEA9%2BNg%2BqB0%2BW4zbJqO%2F4NIA22QveAMQuhgHev8Mt1lYQsqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDChL7VXSsoVKvTqexCrcA7rjrUnqVhoD0lZBh6zhlJsK15yQZGUhSmGrh1R8lNfkTvYTJuDI0Urz9gIdwh6lzOM%2BtD%2FTtnKMybyCnfHNsv3gFZJMBhUJe7RTcULOfnLMNmd9BQxH7MuWkCAUspEcmjo4a7wvEvBcCQR6v5AtOGR8hKxMAwluFkn2r37GFbP8Tt7b0gC3B21qbfhXpqfc8UWKXoAtGCwsJMcpxcPK4q9oco704NHb0TgKWHmAjlhWI3Abp91pY4LY16KjpirhLkMgU7fL7GuPprtgy%2BMwvCaljZOJr7Y3Dbt636%2BP%2FVoLU3LkkcKGOQjEUfz04rraXW6NtsqLmZjdy3%2BTks6xDJUmhGlm38wqmQQ0Tf9CzHo3ltvhYZf0XoQyTT%2FoLAq7GWMvxopt7zMW8Brb%2Fl3xGQ0k0dL8EsUILQigGUqCxmghcHkGYSDmnMizZMMqfzgPYaXiAsj0mnMUaSj5av44l6C5grMMX%2FgmXKPNzIvYOepCSFyrHUzDRY%2F0NXNPVAFPSUGy4jwsHkDm99cOrFgDZ1CE%2FUhAOvb017APYt9%2FNs7cwT7KFlDIC9aibLuFrqCaEX6vSLCwpnvZMbg6E6eOvl5B8qZgwkpfoiZ1WSCO81lyJAIwTp2nOTWq4S6mMJKU%2FrwGOqUBoK96O%2BXCg6nVE1ZPOtFTswK7iPFSiq0W%2FVrShWlAZB4OjOt1VuFlBSeL2JzWUC1weSusvx8vpnmbNaAXWi9ubRjWcE7Xm3WF8SIKqP95LhaYfUou0YSz7Z6N2bl2Q5XcLgtHAAEmkQ6sv%2F480ENF1uuHXi1zMlIgLca91WZ%2Bpap4MaYN%2B8gIPw5L3Th7BewJZPHHiqvVPwyH%2BfmrtAV53J0k%2BVqO&X-Amz-Signature=b3c64317816d7cde0b7f219d884fa26360836b1fb7ecb7e47f3503be1f758772&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIQ4INWP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuG3WbsIgJZeHd1E3SUO9irKeIEfB3cM7VCEmLqJHzJAIhAMddLXvAsjUI6WHRJdmZWHLqqxDpRLz62vb3Dy3ZTyZvKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUbDI9QZCyh8HBvVQq3AMvyh0X88WSZ5LXb4jEvC1hbWh0RIrEIc5HJ%2BpxlCd4van%2F8fUZ9cvrJAA4W%2FgvR4ALkR0FLtbOiVmjvVM0yfyX8to69hyUcTa59%2BSt4z%2BlqvjR0RoglsDlwt%2B9V%2BiwHBnPfsVxqdpVlU3JFn0eHJSlwv0QvBjj5lIGenvzObSI5Xhvh2CReTwrfe04g%2F4Q%2F%2Fvzn9L%2FpOaZKHgXbcLt3pPZswZilQQ81LRHlZw%2FWU010sU6hCYo9mlHZ1xnpgszMdUjXbbwT7SLvNw7vk3XNRnDICkk5SLjkYrc1x1KAjTQGUp8Qlm2IfVam2upgeJ2VhcHa5kiQIhPJbF0Y5ddZvQ08El4gnXy9j69pFkK8y0GZgSZfW4H3vqTuNMvhAwNTx7cEJuhRIlxYixzQ3q08em5JAN8tvIbQtAI7eJgzTO%2B5febxACw0LDFbuFK5s9oW1XL3jk%2BBqgxnx%2By%2BN02f%2BNMu7Ho%2F6dpfmxQ5Ret1hOwLD6b4Zx%2F6%2B0e8hZKZSAl9Q%2FXICSxIPno4etxJkw5oBOBK01zv84XbQVuGDr2B%2BfcpHHkkMWGZGQadZRwlenqnp2HLMtp5LDTKtim5a4ce%2FDCM906xvVTypN74MArf5RyAKHCqDbi1AxGT3%2B7%2FzDXvf28BjqkAQNnBwYzh4w97OxZQtltsQup57%2Bq1eQF9z5XPXGWwDUhkuqGk1sZyqThcnTRju0bIG5sbryl7Y7GdKr9B3KlylxmQI2A3S5SpVsBdNUFpW5OVKsIRa%2FmIFEI%2BykcpFmFIMo7JS5Z1QLbECBOMi02w2C3VJqSZbxukAFtOw3e0tHSafWAu9SbtT5zDjZEdZ1fXfTdaUFUDPjYWkGzZZeac%2BBFhA0H&X-Amz-Signature=90f9c469721b0d9a1c34432451567ce7a07dc99afb2ae71292d47e71ba8ea57f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIQ4INWP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuG3WbsIgJZeHd1E3SUO9irKeIEfB3cM7VCEmLqJHzJAIhAMddLXvAsjUI6WHRJdmZWHLqqxDpRLz62vb3Dy3ZTyZvKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUbDI9QZCyh8HBvVQq3AMvyh0X88WSZ5LXb4jEvC1hbWh0RIrEIc5HJ%2BpxlCd4van%2F8fUZ9cvrJAA4W%2FgvR4ALkR0FLtbOiVmjvVM0yfyX8to69hyUcTa59%2BSt4z%2BlqvjR0RoglsDlwt%2B9V%2BiwHBnPfsVxqdpVlU3JFn0eHJSlwv0QvBjj5lIGenvzObSI5Xhvh2CReTwrfe04g%2F4Q%2F%2Fvzn9L%2FpOaZKHgXbcLt3pPZswZilQQ81LRHlZw%2FWU010sU6hCYo9mlHZ1xnpgszMdUjXbbwT7SLvNw7vk3XNRnDICkk5SLjkYrc1x1KAjTQGUp8Qlm2IfVam2upgeJ2VhcHa5kiQIhPJbF0Y5ddZvQ08El4gnXy9j69pFkK8y0GZgSZfW4H3vqTuNMvhAwNTx7cEJuhRIlxYixzQ3q08em5JAN8tvIbQtAI7eJgzTO%2B5febxACw0LDFbuFK5s9oW1XL3jk%2BBqgxnx%2By%2BN02f%2BNMu7Ho%2F6dpfmxQ5Ret1hOwLD6b4Zx%2F6%2B0e8hZKZSAl9Q%2FXICSxIPno4etxJkw5oBOBK01zv84XbQVuGDr2B%2BfcpHHkkMWGZGQadZRwlenqnp2HLMtp5LDTKtim5a4ce%2FDCM906xvVTypN74MArf5RyAKHCqDbi1AxGT3%2B7%2FzDXvf28BjqkAQNnBwYzh4w97OxZQtltsQup57%2Bq1eQF9z5XPXGWwDUhkuqGk1sZyqThcnTRju0bIG5sbryl7Y7GdKr9B3KlylxmQI2A3S5SpVsBdNUFpW5OVKsIRa%2FmIFEI%2BykcpFmFIMo7JS5Z1QLbECBOMi02w2C3VJqSZbxukAFtOw3e0tHSafWAu9SbtT5zDjZEdZ1fXfTdaUFUDPjYWkGzZZeac%2BBFhA0H&X-Amz-Signature=45667604fb11c379b3d488b24bc471a42226f9cb3aa5825fc1898be9edbeae4c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIQ4INWP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuG3WbsIgJZeHd1E3SUO9irKeIEfB3cM7VCEmLqJHzJAIhAMddLXvAsjUI6WHRJdmZWHLqqxDpRLz62vb3Dy3ZTyZvKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUbDI9QZCyh8HBvVQq3AMvyh0X88WSZ5LXb4jEvC1hbWh0RIrEIc5HJ%2BpxlCd4van%2F8fUZ9cvrJAA4W%2FgvR4ALkR0FLtbOiVmjvVM0yfyX8to69hyUcTa59%2BSt4z%2BlqvjR0RoglsDlwt%2B9V%2BiwHBnPfsVxqdpVlU3JFn0eHJSlwv0QvBjj5lIGenvzObSI5Xhvh2CReTwrfe04g%2F4Q%2F%2Fvzn9L%2FpOaZKHgXbcLt3pPZswZilQQ81LRHlZw%2FWU010sU6hCYo9mlHZ1xnpgszMdUjXbbwT7SLvNw7vk3XNRnDICkk5SLjkYrc1x1KAjTQGUp8Qlm2IfVam2upgeJ2VhcHa5kiQIhPJbF0Y5ddZvQ08El4gnXy9j69pFkK8y0GZgSZfW4H3vqTuNMvhAwNTx7cEJuhRIlxYixzQ3q08em5JAN8tvIbQtAI7eJgzTO%2B5febxACw0LDFbuFK5s9oW1XL3jk%2BBqgxnx%2By%2BN02f%2BNMu7Ho%2F6dpfmxQ5Ret1hOwLD6b4Zx%2F6%2B0e8hZKZSAl9Q%2FXICSxIPno4etxJkw5oBOBK01zv84XbQVuGDr2B%2BfcpHHkkMWGZGQadZRwlenqnp2HLMtp5LDTKtim5a4ce%2FDCM906xvVTypN74MArf5RyAKHCqDbi1AxGT3%2B7%2FzDXvf28BjqkAQNnBwYzh4w97OxZQtltsQup57%2Bq1eQF9z5XPXGWwDUhkuqGk1sZyqThcnTRju0bIG5sbryl7Y7GdKr9B3KlylxmQI2A3S5SpVsBdNUFpW5OVKsIRa%2FmIFEI%2BykcpFmFIMo7JS5Z1QLbECBOMi02w2C3VJqSZbxukAFtOw3e0tHSafWAu9SbtT5zDjZEdZ1fXfTdaUFUDPjYWkGzZZeac%2BBFhA0H&X-Amz-Signature=f7a8a7c0482ec60ea3fb0bf88a56654998f2eb069f6ab986f2086e825a9e6983&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIQ4INWP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuG3WbsIgJZeHd1E3SUO9irKeIEfB3cM7VCEmLqJHzJAIhAMddLXvAsjUI6WHRJdmZWHLqqxDpRLz62vb3Dy3ZTyZvKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUbDI9QZCyh8HBvVQq3AMvyh0X88WSZ5LXb4jEvC1hbWh0RIrEIc5HJ%2BpxlCd4van%2F8fUZ9cvrJAA4W%2FgvR4ALkR0FLtbOiVmjvVM0yfyX8to69hyUcTa59%2BSt4z%2BlqvjR0RoglsDlwt%2B9V%2BiwHBnPfsVxqdpVlU3JFn0eHJSlwv0QvBjj5lIGenvzObSI5Xhvh2CReTwrfe04g%2F4Q%2F%2Fvzn9L%2FpOaZKHgXbcLt3pPZswZilQQ81LRHlZw%2FWU010sU6hCYo9mlHZ1xnpgszMdUjXbbwT7SLvNw7vk3XNRnDICkk5SLjkYrc1x1KAjTQGUp8Qlm2IfVam2upgeJ2VhcHa5kiQIhPJbF0Y5ddZvQ08El4gnXy9j69pFkK8y0GZgSZfW4H3vqTuNMvhAwNTx7cEJuhRIlxYixzQ3q08em5JAN8tvIbQtAI7eJgzTO%2B5febxACw0LDFbuFK5s9oW1XL3jk%2BBqgxnx%2By%2BN02f%2BNMu7Ho%2F6dpfmxQ5Ret1hOwLD6b4Zx%2F6%2B0e8hZKZSAl9Q%2FXICSxIPno4etxJkw5oBOBK01zv84XbQVuGDr2B%2BfcpHHkkMWGZGQadZRwlenqnp2HLMtp5LDTKtim5a4ce%2FDCM906xvVTypN74MArf5RyAKHCqDbi1AxGT3%2B7%2FzDXvf28BjqkAQNnBwYzh4w97OxZQtltsQup57%2Bq1eQF9z5XPXGWwDUhkuqGk1sZyqThcnTRju0bIG5sbryl7Y7GdKr9B3KlylxmQI2A3S5SpVsBdNUFpW5OVKsIRa%2FmIFEI%2BykcpFmFIMo7JS5Z1QLbECBOMi02w2C3VJqSZbxukAFtOw3e0tHSafWAu9SbtT5zDjZEdZ1fXfTdaUFUDPjYWkGzZZeac%2BBFhA0H&X-Amz-Signature=c4f678600a80abfa3442f86a873c1f7bbe0d865e61f365d852ac156363d14389&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIQ4INWP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuG3WbsIgJZeHd1E3SUO9irKeIEfB3cM7VCEmLqJHzJAIhAMddLXvAsjUI6WHRJdmZWHLqqxDpRLz62vb3Dy3ZTyZvKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUbDI9QZCyh8HBvVQq3AMvyh0X88WSZ5LXb4jEvC1hbWh0RIrEIc5HJ%2BpxlCd4van%2F8fUZ9cvrJAA4W%2FgvR4ALkR0FLtbOiVmjvVM0yfyX8to69hyUcTa59%2BSt4z%2BlqvjR0RoglsDlwt%2B9V%2BiwHBnPfsVxqdpVlU3JFn0eHJSlwv0QvBjj5lIGenvzObSI5Xhvh2CReTwrfe04g%2F4Q%2F%2Fvzn9L%2FpOaZKHgXbcLt3pPZswZilQQ81LRHlZw%2FWU010sU6hCYo9mlHZ1xnpgszMdUjXbbwT7SLvNw7vk3XNRnDICkk5SLjkYrc1x1KAjTQGUp8Qlm2IfVam2upgeJ2VhcHa5kiQIhPJbF0Y5ddZvQ08El4gnXy9j69pFkK8y0GZgSZfW4H3vqTuNMvhAwNTx7cEJuhRIlxYixzQ3q08em5JAN8tvIbQtAI7eJgzTO%2B5febxACw0LDFbuFK5s9oW1XL3jk%2BBqgxnx%2By%2BN02f%2BNMu7Ho%2F6dpfmxQ5Ret1hOwLD6b4Zx%2F6%2B0e8hZKZSAl9Q%2FXICSxIPno4etxJkw5oBOBK01zv84XbQVuGDr2B%2BfcpHHkkMWGZGQadZRwlenqnp2HLMtp5LDTKtim5a4ce%2FDCM906xvVTypN74MArf5RyAKHCqDbi1AxGT3%2B7%2FzDXvf28BjqkAQNnBwYzh4w97OxZQtltsQup57%2Bq1eQF9z5XPXGWwDUhkuqGk1sZyqThcnTRju0bIG5sbryl7Y7GdKr9B3KlylxmQI2A3S5SpVsBdNUFpW5OVKsIRa%2FmIFEI%2BykcpFmFIMo7JS5Z1QLbECBOMi02w2C3VJqSZbxukAFtOw3e0tHSafWAu9SbtT5zDjZEdZ1fXfTdaUFUDPjYWkGzZZeac%2BBFhA0H&X-Amz-Signature=08917d7ace9c4bc987d9d9a63639e3f23c6d706999505ce290d78d868ddddecb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIQ4INWP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuG3WbsIgJZeHd1E3SUO9irKeIEfB3cM7VCEmLqJHzJAIhAMddLXvAsjUI6WHRJdmZWHLqqxDpRLz62vb3Dy3ZTyZvKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUbDI9QZCyh8HBvVQq3AMvyh0X88WSZ5LXb4jEvC1hbWh0RIrEIc5HJ%2BpxlCd4van%2F8fUZ9cvrJAA4W%2FgvR4ALkR0FLtbOiVmjvVM0yfyX8to69hyUcTa59%2BSt4z%2BlqvjR0RoglsDlwt%2B9V%2BiwHBnPfsVxqdpVlU3JFn0eHJSlwv0QvBjj5lIGenvzObSI5Xhvh2CReTwrfe04g%2F4Q%2F%2Fvzn9L%2FpOaZKHgXbcLt3pPZswZilQQ81LRHlZw%2FWU010sU6hCYo9mlHZ1xnpgszMdUjXbbwT7SLvNw7vk3XNRnDICkk5SLjkYrc1x1KAjTQGUp8Qlm2IfVam2upgeJ2VhcHa5kiQIhPJbF0Y5ddZvQ08El4gnXy9j69pFkK8y0GZgSZfW4H3vqTuNMvhAwNTx7cEJuhRIlxYixzQ3q08em5JAN8tvIbQtAI7eJgzTO%2B5febxACw0LDFbuFK5s9oW1XL3jk%2BBqgxnx%2By%2BN02f%2BNMu7Ho%2F6dpfmxQ5Ret1hOwLD6b4Zx%2F6%2B0e8hZKZSAl9Q%2FXICSxIPno4etxJkw5oBOBK01zv84XbQVuGDr2B%2BfcpHHkkMWGZGQadZRwlenqnp2HLMtp5LDTKtim5a4ce%2FDCM906xvVTypN74MArf5RyAKHCqDbi1AxGT3%2B7%2FzDXvf28BjqkAQNnBwYzh4w97OxZQtltsQup57%2Bq1eQF9z5XPXGWwDUhkuqGk1sZyqThcnTRju0bIG5sbryl7Y7GdKr9B3KlylxmQI2A3S5SpVsBdNUFpW5OVKsIRa%2FmIFEI%2BykcpFmFIMo7JS5Z1QLbECBOMi02w2C3VJqSZbxukAFtOw3e0tHSafWAu9SbtT5zDjZEdZ1fXfTdaUFUDPjYWkGzZZeac%2BBFhA0H&X-Amz-Signature=99843f65ee314431ecadbc3aea5db8535197d120823180accc684ce3111bdb4a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP5WOMRL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTzKcKXkry7LRA%2FqahRwK4ooK6dWzpRySxweln0v99mgIgECiZjR5ff0FLl5qGKg6AaD69HmgVicp8DRET%2FvuR9vIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4qxekKUIv3UftbRCrcA7L6L4CYiYK2yWIMtFmihsT2sHd5pHW5N9rEybt1%2FyHytLaD7R6rKW%2BZgtzt7RKvcegswmVt6k2JyVCIbNtfD7q1TuhExbc6bAjqPdvu2YQXIICTORsYx77iZ75IPEwdiilzFvTh%2BtXHKexkEVFnrqjjHjDvMhIQPOuUxObuAGiI7t0ga8WbyDMuPexNRpxShfs4xfVO2m06HT4Y7Dj%2FktFREL%2Bn7MQrdjjhqquK0YlpnMnqTExQ%2FxMXwajpwbl6m9lmCkbVv2pLPlH94wr2o3daBHauTUVoUjMni7exlpLqg8Dz3s4YVElcedYoLv2jWywGcH6QYZaApaNo%2BK8gQh48%2B858gWldVo8%2FSYtUiqG5oEhGNfEAANACdWtZ1rGbUl3vnSYj3cm9bbFPYPPr4PEwZwuxI4q0mnezbipqO%2Bhjf0vS%2FmKzaUHIYb3QwPevJQ2UZjuusEsyLAoUKlEnZ9ZGrDr%2By2LTjfEmIlZA%2F1j6sYYbmehzmAFf5hWEFogEkf4J%2FFmQRJ%2BEX0Hh4e4fSlHKvSVgc06TqP5B0asCtrjS6sQmbL1kqgDN7K28c%2F9JwU0yVAKT7HNmaxTCoWhl%2FQ2QjFlcSWhBiD5IT9Mq%2Bi0CWYlgAbTG57ftUpjRMJu%2B%2FbwGOqUBlBIh4nOP%2F1CLxaDzgs%2FL4FDIBXqgWSjYN%2Fw4RqI9quJQYJcX8JYPTAx1fMG4aVqC%2BWdgjkJM1oMqnl3%2BTdSvR1Xs78M3PA5tTZnoLQox4vOD71DDdyhBqxIY6qpYKROLMbJo02O8sk9YOyY9Qgjjg1LXoYDoztHufuKZSsAfhKxCqFlwki9S0Bhl1TOGr7gBGGzHlZPBUR9NNaVp%2BMYA%2BBwUL3T1&X-Amz-Signature=49b2db73ef14c60277d6b95050e9191594528a39365c86baa5d07a6d01451da7&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDCNDG6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGbuPbBPDYi%2FATIkhnQAOrDFEcJvMilgpks5orP3hMWlAiBc%2Bw92oBeThihBdQhkBjMsDVpRjaOCR8TwUqKa0K%2B1kSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiPlsy7XZOgzxEAoTKtwDt%2B9qqbO03BmHPfsIlb1roetl5ePvhp0qw3CJ%2FRP5Tw7kMt1uFOsr%2BScXhbgwSL2%2Bk2XhxwyppccqBsSyyAgzz5xmskrhXONVTqiGRXkkP0yPCpxdtU1IHmnPgE5jB12QThM7%2F2gbTl9lJMcr6kP47BZgy%2FDCcFJwwKH58%2BmygRBjLyM4XNI7gvnxlEbQ8maNbv2kHSd0uDB2Nw0ZQs6PaVrj3WP%2FAFxzUgbLxYfIqWh53CRm2mgUzLz%2FEokM8DRNoMp8VEP4rpwnZdl7gsqw%2FWiC%2BdOXXAZ%2B41fw49hwE7wWn74KykmhTFAKfI6ltuFoqO8feIMCzLjKVTqp9hMj7OwyGFP%2BvPSA8hOtE1CkSNyeDlofwPDrkSmmTcZzZhXi%2F1zQlFk%2Bn4%2FR2YfLZOiLTN0uaIrYhlJnHgmiYRvr1FwnvtIfzjDv2sKAq4ww9rHaxYfToKnt46cX3BLeuUQtXQ7jGqmu%2FzbH6ncIoFpGMigMP1uH7NvXX7rknZZaRWlsjdD4KJirkCD0nLz01f1PWJszTMQWbWXU4uTjm8ZTxo%2F5HQus7sxZzOJjRTYZ82SPobG6gyBhw%2BHadFOw0AwLvb35OVE30sdhZa4M1DBIS6qt8sTuRmyLqnxTf0Qw8r79vAY6pgErjdTk5%2BxjtxAMnqQO8czDZ8X%2BlaWLQl4WIOT1bG%2BVQAFkkQA6G3NFcVWa5yh%2BxtXA9Gk8N6audHL8GVDVcAvNp3bHfk0rBDJa5AkkWsYZXnDU%2BfWhnqae1FeShgzOYwgTgaSwt27m6HjzQYP%2FkklT8RBktuRGz1DaHgIHv6PKE%2F3aPsd%2BT8AY%2BswajSixHWT%2F8OKx%2BlxppjccZVviZ3hwm0VgK%2FZD&X-Amz-Signature=0bbba723c3dd216f15af4ef2e0755a279cd5237ede2ac9355e420273e4138426&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIQ4INWP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuG3WbsIgJZeHd1E3SUO9irKeIEfB3cM7VCEmLqJHzJAIhAMddLXvAsjUI6WHRJdmZWHLqqxDpRLz62vb3Dy3ZTyZvKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUbDI9QZCyh8HBvVQq3AMvyh0X88WSZ5LXb4jEvC1hbWh0RIrEIc5HJ%2BpxlCd4van%2F8fUZ9cvrJAA4W%2FgvR4ALkR0FLtbOiVmjvVM0yfyX8to69hyUcTa59%2BSt4z%2BlqvjR0RoglsDlwt%2B9V%2BiwHBnPfsVxqdpVlU3JFn0eHJSlwv0QvBjj5lIGenvzObSI5Xhvh2CReTwrfe04g%2F4Q%2F%2Fvzn9L%2FpOaZKHgXbcLt3pPZswZilQQ81LRHlZw%2FWU010sU6hCYo9mlHZ1xnpgszMdUjXbbwT7SLvNw7vk3XNRnDICkk5SLjkYrc1x1KAjTQGUp8Qlm2IfVam2upgeJ2VhcHa5kiQIhPJbF0Y5ddZvQ08El4gnXy9j69pFkK8y0GZgSZfW4H3vqTuNMvhAwNTx7cEJuhRIlxYixzQ3q08em5JAN8tvIbQtAI7eJgzTO%2B5febxACw0LDFbuFK5s9oW1XL3jk%2BBqgxnx%2By%2BN02f%2BNMu7Ho%2F6dpfmxQ5Ret1hOwLD6b4Zx%2F6%2B0e8hZKZSAl9Q%2FXICSxIPno4etxJkw5oBOBK01zv84XbQVuGDr2B%2BfcpHHkkMWGZGQadZRwlenqnp2HLMtp5LDTKtim5a4ce%2FDCM906xvVTypN74MArf5RyAKHCqDbi1AxGT3%2B7%2FzDXvf28BjqkAQNnBwYzh4w97OxZQtltsQup57%2Bq1eQF9z5XPXGWwDUhkuqGk1sZyqThcnTRju0bIG5sbryl7Y7GdKr9B3KlylxmQI2A3S5SpVsBdNUFpW5OVKsIRa%2FmIFEI%2BykcpFmFIMo7JS5Z1QLbECBOMi02w2C3VJqSZbxukAFtOw3e0tHSafWAu9SbtT5zDjZEdZ1fXfTdaUFUDPjYWkGzZZeac%2BBFhA0H&X-Amz-Signature=ee4e36cda1744b7d51360039873222ea57f45c4987993b532bd916f98b4d2c37&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIQ4INWP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuG3WbsIgJZeHd1E3SUO9irKeIEfB3cM7VCEmLqJHzJAIhAMddLXvAsjUI6WHRJdmZWHLqqxDpRLz62vb3Dy3ZTyZvKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUbDI9QZCyh8HBvVQq3AMvyh0X88WSZ5LXb4jEvC1hbWh0RIrEIc5HJ%2BpxlCd4van%2F8fUZ9cvrJAA4W%2FgvR4ALkR0FLtbOiVmjvVM0yfyX8to69hyUcTa59%2BSt4z%2BlqvjR0RoglsDlwt%2B9V%2BiwHBnPfsVxqdpVlU3JFn0eHJSlwv0QvBjj5lIGenvzObSI5Xhvh2CReTwrfe04g%2F4Q%2F%2Fvzn9L%2FpOaZKHgXbcLt3pPZswZilQQ81LRHlZw%2FWU010sU6hCYo9mlHZ1xnpgszMdUjXbbwT7SLvNw7vk3XNRnDICkk5SLjkYrc1x1KAjTQGUp8Qlm2IfVam2upgeJ2VhcHa5kiQIhPJbF0Y5ddZvQ08El4gnXy9j69pFkK8y0GZgSZfW4H3vqTuNMvhAwNTx7cEJuhRIlxYixzQ3q08em5JAN8tvIbQtAI7eJgzTO%2B5febxACw0LDFbuFK5s9oW1XL3jk%2BBqgxnx%2By%2BN02f%2BNMu7Ho%2F6dpfmxQ5Ret1hOwLD6b4Zx%2F6%2B0e8hZKZSAl9Q%2FXICSxIPno4etxJkw5oBOBK01zv84XbQVuGDr2B%2BfcpHHkkMWGZGQadZRwlenqnp2HLMtp5LDTKtim5a4ce%2FDCM906xvVTypN74MArf5RyAKHCqDbi1AxGT3%2B7%2FzDXvf28BjqkAQNnBwYzh4w97OxZQtltsQup57%2Bq1eQF9z5XPXGWwDUhkuqGk1sZyqThcnTRju0bIG5sbryl7Y7GdKr9B3KlylxmQI2A3S5SpVsBdNUFpW5OVKsIRa%2FmIFEI%2BykcpFmFIMo7JS5Z1QLbECBOMi02w2C3VJqSZbxukAFtOw3e0tHSafWAu9SbtT5zDjZEdZ1fXfTdaUFUDPjYWkGzZZeac%2BBFhA0H&X-Amz-Signature=b9bdeb30a2f9609192a99f0c8d66319ba8f43ad67ec8b2d3eec9475fe7a2fa11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIQ4INWP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuG3WbsIgJZeHd1E3SUO9irKeIEfB3cM7VCEmLqJHzJAIhAMddLXvAsjUI6WHRJdmZWHLqqxDpRLz62vb3Dy3ZTyZvKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUbDI9QZCyh8HBvVQq3AMvyh0X88WSZ5LXb4jEvC1hbWh0RIrEIc5HJ%2BpxlCd4van%2F8fUZ9cvrJAA4W%2FgvR4ALkR0FLtbOiVmjvVM0yfyX8to69hyUcTa59%2BSt4z%2BlqvjR0RoglsDlwt%2B9V%2BiwHBnPfsVxqdpVlU3JFn0eHJSlwv0QvBjj5lIGenvzObSI5Xhvh2CReTwrfe04g%2F4Q%2F%2Fvzn9L%2FpOaZKHgXbcLt3pPZswZilQQ81LRHlZw%2FWU010sU6hCYo9mlHZ1xnpgszMdUjXbbwT7SLvNw7vk3XNRnDICkk5SLjkYrc1x1KAjTQGUp8Qlm2IfVam2upgeJ2VhcHa5kiQIhPJbF0Y5ddZvQ08El4gnXy9j69pFkK8y0GZgSZfW4H3vqTuNMvhAwNTx7cEJuhRIlxYixzQ3q08em5JAN8tvIbQtAI7eJgzTO%2B5febxACw0LDFbuFK5s9oW1XL3jk%2BBqgxnx%2By%2BN02f%2BNMu7Ho%2F6dpfmxQ5Ret1hOwLD6b4Zx%2F6%2B0e8hZKZSAl9Q%2FXICSxIPno4etxJkw5oBOBK01zv84XbQVuGDr2B%2BfcpHHkkMWGZGQadZRwlenqnp2HLMtp5LDTKtim5a4ce%2FDCM906xvVTypN74MArf5RyAKHCqDbi1AxGT3%2B7%2FzDXvf28BjqkAQNnBwYzh4w97OxZQtltsQup57%2Bq1eQF9z5XPXGWwDUhkuqGk1sZyqThcnTRju0bIG5sbryl7Y7GdKr9B3KlylxmQI2A3S5SpVsBdNUFpW5OVKsIRa%2FmIFEI%2BykcpFmFIMo7JS5Z1QLbECBOMi02w2C3VJqSZbxukAFtOw3e0tHSafWAu9SbtT5zDjZEdZ1fXfTdaUFUDPjYWkGzZZeac%2BBFhA0H&X-Amz-Signature=07c510e323f380de162f3865b24452c6ad783069c07e5f71db47163e645fdd05&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2AC4ZPD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLfM9TJjA462hJYQVvNNu%2FBTCV6pvZ2Z5ZaUKq9%2FZGJgIgYUIcJ4ez%2FxRdKXj%2BaM1Bk6agbgvIQCx3GupgIRfdIhsqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOIixE5vLZ7QL3JnAircAzIwOeZ%2B9eog7lfugWm8UZhnoLzaEa8OkiVa%2FtR%2BdzKGcysUeXkjBYfc3c%2Fng4Oe1jjMNJt94g2nsAfkjm4EVLb%2BTRDLPkku4en%2Ff5JO3A5njyH4yaczN%2BNEKMRN5FJ182SSBfH0ZZJeufH01rCrAHheCMFI22GhrgtGoJHlvMZVEwmhx%2BDNoeeJdraj8%2Fg3mhBL2XrGc9w%2FsFqpZaF3GXn9HTsG%2B4M5ThUCAm2MGW4VnyVhACNCaSkT%2B21bgq2BOm53bgcg3tynLxCM%2FsQ%2B8vz2DO%2BQZRyAtRpYfCpzwGdHB5Nq6%2F1SqUfn0v0nGdZkmLoFNNYfBGFAmy6UMcw9D8MfXllxuUY7GCA4k0ADlTm%2BRwsUEEOVXE9NMxQn7t%2FzQeCEFmpsvkyNZmYV6IN9kTnakAjpu9SDofHSSGsOaRoEX6wZKF7J%2BIAzYDFgY4vwQSbs4ONF%2FyZOLLUo4cwvvN%2BryKi2vyg7XAqQ%2FOEJ%2F8qh4hJM507fnOTj5cLA2MFEXcghSBBP0cXslSGS94rb%2FFaOkeW9uEYiv93MAFEynlTtVJ%2F6ruW%2Fi4apTvDYeh1h4sda1jCqtIVtaJu7DtewlHmCqufsRKTAVikeoPf5tys7X0HVEoK4uzTjpokWMLG%2B%2FbwGOqUBVBjf%2BppJlzThVEYsSv8w6g7rBh8%2BySrQmDVff5W4pVLnjWvgSXboB73K9yEQjRPd5n6QitowBihvyKYFddk7Cot9rPF%2FKhOOkUUaKNiR4ionDabkIp22JIN7T0uWiMTeEHDKMOrU%2B4BjepkRmE0NsYhcODSZYrNnIn5fDUU9PAtAXQLkdxUuEmYDqHDq8L8TQt9JV44tJoV43NyiEpLyeAOs%2BgCg&X-Amz-Signature=b2d71d26240fb44ed5e0f1d0f7eb96e4da972bdea3bf67cd57ceed2fd3bcb443&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ6TDUCW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BNqbo6fpi3c6Od7UXe0GwvuA%2FBCRiYr7BZ7rd70wlAAIhAOCPdaUhC3DyhJbu1zKW8AgBaoS6TPfsY39%2F%2Bq%2FrerA9KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlNFsKAaeQJXVdsvAq3AM8VJ%2B2d7pyO7z3eERIUZNa6LntkWSC89BTKIIinBBExRqhlSs2q0M%2BC76RRjnWw%2BHawO%2BNhYIS0Kwipcn5bAoiP4ng8zFQcxIdlnFnn6mV6%2BHyrq52ADjxVzc0b97FqREWEQB5V1qfTEOhczQDZIAr1Wk73e1XDN3pdj8flQJ5O29DfExP9jyLoEiEECcziSTe%2BawpGXiIQP7R8PvNcsPLLyj6XGL2QYZW4i5Ox9QxZJj%2FTY3lKLtVmBkQOkEWefiRZ%2FaT%2FxMUZFJMVu9k6HCuXwXwr0E8UZyFwyqagirjmhjwLKwi4J7dQR%2B8gKmTmjtAKDWD3M%2F2k8FUIKsNSAryzgUg768Fx0iF615z9xZ%2BxX6M%2FzHTHEojTEwHBb%2FlKE6ueo9mZr2gaLdfF0ntxsaIO8qDZupXWGEeSF4QzFhrGmfBJzN3ZtiLePR1WkNHFFwgtIAbtfSbsZ7O0q5vPHJ98ch3%2FShy0nzFSeutxMM4RyRwNkd7pooMrMqu12Kd1A4ERVvTFzbWkNVxPBaSauwPI%2FY7IOdLf0f0YBEicjI15zOFWyh3qzEanfpot1uGF8YBYDLSs8rKzC1bxIXZo9js24FJhQ5tr3UbSftmbT3IwFWQS8SGv5UzFw6c0DDnuv28BjqkAapVO5eB6sQ0aCEiZtFJBTRP4Gp3ElvJk44GvdXcTw72l%2B%2BvD8PmjLZQB51QScDB89M6fb1DC%2Bu5SDSNn8JkdofK2aDbTHi4IjeyRKXCHxmbyr1Ho67jfgVKWY7Gcs%2BKLno7tJ4AUp1XrhnyhCUAMMBgw1%2FOJpZf6wr9ZRFIX%2Bu5G13m%2BQ9t6rr5WvN3X1HUK49rae78Q8ZwZPyqsv3u7jqJGtpO&X-Amz-Signature=4170f396f7434bb7918ca49f2f363a874517986077c879eef35ac6f78555412b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662POJVDFK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeTODrWY%2BcT0e9oC9I1dhCpFdXEgKZS2BSXP3%2FdoKaggIgbKPCv%2Bb5TfqTAFtqtPC4LPd79rOI9aJVqwLXA%2Fmzh20qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJjFYcwR545%2BZku2myrcA873G0mCN2OMk3rxzJvDguOoE3pBH5ZA89x6hRFUJsfQkTwqIMxWRI3H6wRjTQ6Owwwqr0Mx3yIE8qngk0suW5ECL%2BSPUA3IO%2F248ZxAkFtbZffRp6Q3bwA9VfrjpI1pbR9SuGqkkliZcTDZXCNA2O4LG8JYEIpD0ntbSLV1HTkpr3JNdeBzd1LGaTJ4TI23iUyimYV0B8%2Fp7fP5CQFqztp8Xx207EgaQ2SOPMTSQ%2FEbGOySCtvQUE2%2F4hNU8uH1fXid0CQ5pbHI5u4ExitY2FC7WeawXcM%2FGgBdBUn1BgTWnO51vi%2FC9S3PQcHkrSeS5%2F9zeBOVhjBuzKMuBbGyneIMfh10oQgwp16e8Sr63fbR%2Ben9Z4GBNnySnpRrF0T6uwI32k8OR55WPtdGFLJLZNibZpqsrAHmzO06DkdUz3KtQNtdHsIDGLSAN6LDy2Beu2N0Td0ThjethBQ%2BB0RbmE0UKGaxxTtrQs%2BH6C%2Bg94%2BkIdJzgQg5DOBoasmP2KTqux58Ytj5%2Bm19riKGiIoihv9v%2BFNhcEHOwTCDG%2FvlVRxVvQCQ18uhHiE6BtopL0g6g1MpFp4mJ5ISMMIKzshAAdHjCOBafM%2F2tRky2pRDD4LavDYNxgbAJCP5zxp5MMrC%2FbwGOqUBT1aZxqN6cKicGJs%2BP44TPwGkC3038c0taZqqYH%2BuuxdtV5kjjHl%2Bly6y60ADPqbC%2Fy7Ucljv76IH6misxxEbxr7Yr1i5Tb7wiPYK8IX2NDguvWj1y%2Ba%2BlDtOD8Txzc%2Fa31pa%2F7nWeOfCBoJQlbR0e8AbsDAnCacKnqdhmHiG9Ee2dDeqtl0LHEb7yxf7zt5UX7zonnPJf0DwGofUZgd4FuGCfTy4&X-Amz-Signature=1c36c85a6c211c5ccffa53a91eda80a33921a7db5ec8f61f0668c793f734c93c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL3PTYYJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICs7hILH9WEBTAdSQZanY2WpCVpIFRMsvbE1e%2BP8nXSKAiBZHiJmw48T%2B%2FwaXnQEAyhOkb7ziUiX75g%2FgXI%2Fmf%2FxRSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqCxyZ1LVvvyTBU7dKtwDqkOOanFsRoP71GCDYoJXf3yxhM48xp0jD2EzwnuI1%2FKLUeBM1rgAnjHgYe7dY7URFfqm372UxqfaHmG37QBzgqJLn8SDHhMMY67Obk23xvCIweV29fjQgMKxGru2tjXT6Mkf6HRg%2FY3C4NGXK13rvig2V2RMOoEk5%2BexhGq4xo50yleU9Hb4meZkF2IWVDu8NsR1BuoYFvfJ5PsCr2%2FkcbsyoBc57geEEi6YNHkCqYo2yMt9pfPyWa4zyR4J6xDiXaQYcqgEAW15zp0UZ1%2Biet3C%2FxOueswQ7qSIHV%2FlCaLeKWL%2F9Y8oGpvr54ZSgn%2F%2FfadbE67cVnBi0%2BR2Vp33pkxYZRB1hQbR%2FD%2BLCQNLqPK2P7VxRIeHCUgPlxgXOcvXra%2FFmAFq8Mokcap%2BaqEXNvlC1vjieqY1Ix3GguSo2LQTdGGpvnZsy7rm1Y%2F0LEB96zDWDEjzRvhdyqWd5vpy4C8snxktziwAy3uqKVOVl35V4nP3SLrKvuvm7ed6VK14VcUd1laiz%2FQLWK6OQRu5HdAbT9lybJeHVbFZIgEsobXCmOZb4O%2BcWKK6ciVyXzJoh3EfocCk0E%2FiFSMxC1ZrHpc0Eu9%2F5Dlf5HdD3R%2FeFzjgT2x98coRnRYFxdsw2L%2F9vAY6pgH%2BTi%2BINaPJcO7qyblSk5g9iyekoyKTTDRN26Cku3hBVsYAN75OrISfAH0TFpGHxmMnpZhYx2uowCbDdAccYg8LMmtvJdOsjQIfGaR2VpkAdjjxTPK2rm610UZNK4jF8DzhXkhjo%2BJHjS7ZAKHCQwaYeh8OgMffCUFLhVjp0CMKsXVZQOC1rWXu%2FeDcFMUpZs%2Bj1e0Re%2BRdIfFpA18tHtasdfkwc7gv&X-Amz-Signature=d156db48beb62dde275de471e2ae15b30ecb3d76f3adb17f7b8908a0de0c0ee4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL3PTYYJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICs7hILH9WEBTAdSQZanY2WpCVpIFRMsvbE1e%2BP8nXSKAiBZHiJmw48T%2B%2FwaXnQEAyhOkb7ziUiX75g%2FgXI%2Fmf%2FxRSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqCxyZ1LVvvyTBU7dKtwDqkOOanFsRoP71GCDYoJXf3yxhM48xp0jD2EzwnuI1%2FKLUeBM1rgAnjHgYe7dY7URFfqm372UxqfaHmG37QBzgqJLn8SDHhMMY67Obk23xvCIweV29fjQgMKxGru2tjXT6Mkf6HRg%2FY3C4NGXK13rvig2V2RMOoEk5%2BexhGq4xo50yleU9Hb4meZkF2IWVDu8NsR1BuoYFvfJ5PsCr2%2FkcbsyoBc57geEEi6YNHkCqYo2yMt9pfPyWa4zyR4J6xDiXaQYcqgEAW15zp0UZ1%2Biet3C%2FxOueswQ7qSIHV%2FlCaLeKWL%2F9Y8oGpvr54ZSgn%2F%2FfadbE67cVnBi0%2BR2Vp33pkxYZRB1hQbR%2FD%2BLCQNLqPK2P7VxRIeHCUgPlxgXOcvXra%2FFmAFq8Mokcap%2BaqEXNvlC1vjieqY1Ix3GguSo2LQTdGGpvnZsy7rm1Y%2F0LEB96zDWDEjzRvhdyqWd5vpy4C8snxktziwAy3uqKVOVl35V4nP3SLrKvuvm7ed6VK14VcUd1laiz%2FQLWK6OQRu5HdAbT9lybJeHVbFZIgEsobXCmOZb4O%2BcWKK6ciVyXzJoh3EfocCk0E%2FiFSMxC1ZrHpc0Eu9%2F5Dlf5HdD3R%2FeFzjgT2x98coRnRYFxdsw2L%2F9vAY6pgH%2BTi%2BINaPJcO7qyblSk5g9iyekoyKTTDRN26Cku3hBVsYAN75OrISfAH0TFpGHxmMnpZhYx2uowCbDdAccYg8LMmtvJdOsjQIfGaR2VpkAdjjxTPK2rm610UZNK4jF8DzhXkhjo%2BJHjS7ZAKHCQwaYeh8OgMffCUFLhVjp0CMKsXVZQOC1rWXu%2FeDcFMUpZs%2Bj1e0Re%2BRdIfFpA18tHtasdfkwc7gv&X-Amz-Signature=57344bc48a4ac193933abf82941b4386295d4d7925232bf8814583feceb42e0a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
