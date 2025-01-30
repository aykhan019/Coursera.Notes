

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJV4WRP6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWuW6%2F6tREAk%2Be6zScOd8VJh7RJsVoxqScl%2FxYr07J%2FAiEAtkNgvBrlmm95eLdSRRxEG6KGPXwufqWqmyHBZJnyRhoqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGVt%2BFKkv0qt5G4yjCrcA%2FdJSg6j%2BpCGbqGLXFvurHz9mLRj9MfbTvs%2BqWgNZ2MrTSq6Ib4VRLOR1IZXHxswlNqpHIVSlVGyi%2FSbPSX3gjgjwQYrLBsBAG%2Fwd%2Ft0JM5OCidOR7GhnmcdfG5XfiLBdThw5mKBUMkvfmTzc4XmM5xOHTkqY8Y3VSQkQdOKsxrySxGOXikUD7D31M67%2BI1AcBbhY6x0l2xh1WhGBEk75gg1Vvg1MJUgnQaQNyznszSQ4CWFn1U9hgFguRsCYRHRAu74EQ1sji5QfyXBBxFTIdyeGbVpTZ%2BXsw5rPT%2FdtOKueuaB%2BsyE45sNgg7bYPOUGBlnUG%2B4wXzxQCqYSC%2FI172Cee4q6Yn555dMfi%2F3L9KbcYzUs%2Fd9DezcQxKFxJOFnAhfWLtZFgMo%2FD6E3JKXYx94cXY8sHhL7BxwI1C7eht%2FHk3XjK5qyyx1HXhabFJ%2FIjXf7%2Bt9ApsgBZETDZuCPZyEyunhYlOf78z5AhMkbOGYzIO%2FMtYNI3ZFgYmeudSWH3WzTOjP32JBOq07etS%2BWxqqssHZYuZ%2BVpCmFrZWNbb2c%2FkXBxx6lGwTEs9qk4lMQHSGWfypfxASWS027raWnX5fe4khPqBdjVnj%2B7v2PwNGf7gsXY9opA0ljGvwML6W67wGOqUB1fuEGgFm8cjhT0Ug9aADVw5oxlPy50UYDLjSXzUyKkpWcii5P2r61KvKrAG7CxerfbtGN72u0pSxES8xvqIluvj0NWa55%2FlGHGU3Yhy3mqpy6dybSPsMtheh3025zhJDgBm%2BHzIarNO55JIKWfeqTB0RuUP3qgM5jdKTw3THFmxq2drlIVNpE4COmM2heRYhjTiaYp4C0PGHaI6vPqPLtlS5X1zz&X-Amz-Signature=0bd852b79b7c687c6820bf3726d047c8a4665039d07c2c88d1bcfd7bcf96a0ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJV4WRP6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWuW6%2F6tREAk%2Be6zScOd8VJh7RJsVoxqScl%2FxYr07J%2FAiEAtkNgvBrlmm95eLdSRRxEG6KGPXwufqWqmyHBZJnyRhoqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGVt%2BFKkv0qt5G4yjCrcA%2FdJSg6j%2BpCGbqGLXFvurHz9mLRj9MfbTvs%2BqWgNZ2MrTSq6Ib4VRLOR1IZXHxswlNqpHIVSlVGyi%2FSbPSX3gjgjwQYrLBsBAG%2Fwd%2Ft0JM5OCidOR7GhnmcdfG5XfiLBdThw5mKBUMkvfmTzc4XmM5xOHTkqY8Y3VSQkQdOKsxrySxGOXikUD7D31M67%2BI1AcBbhY6x0l2xh1WhGBEk75gg1Vvg1MJUgnQaQNyznszSQ4CWFn1U9hgFguRsCYRHRAu74EQ1sji5QfyXBBxFTIdyeGbVpTZ%2BXsw5rPT%2FdtOKueuaB%2BsyE45sNgg7bYPOUGBlnUG%2B4wXzxQCqYSC%2FI172Cee4q6Yn555dMfi%2F3L9KbcYzUs%2Fd9DezcQxKFxJOFnAhfWLtZFgMo%2FD6E3JKXYx94cXY8sHhL7BxwI1C7eht%2FHk3XjK5qyyx1HXhabFJ%2FIjXf7%2Bt9ApsgBZETDZuCPZyEyunhYlOf78z5AhMkbOGYzIO%2FMtYNI3ZFgYmeudSWH3WzTOjP32JBOq07etS%2BWxqqssHZYuZ%2BVpCmFrZWNbb2c%2FkXBxx6lGwTEs9qk4lMQHSGWfypfxASWS027raWnX5fe4khPqBdjVnj%2B7v2PwNGf7gsXY9opA0ljGvwML6W67wGOqUB1fuEGgFm8cjhT0Ug9aADVw5oxlPy50UYDLjSXzUyKkpWcii5P2r61KvKrAG7CxerfbtGN72u0pSxES8xvqIluvj0NWa55%2FlGHGU3Yhy3mqpy6dybSPsMtheh3025zhJDgBm%2BHzIarNO55JIKWfeqTB0RuUP3qgM5jdKTw3THFmxq2drlIVNpE4COmM2heRYhjTiaYp4C0PGHaI6vPqPLtlS5X1zz&X-Amz-Signature=fd3df7aca66d33b7d615c6fcb7e70bc2637154e8942488cbedc0a2724a24f581&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJV4WRP6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWuW6%2F6tREAk%2Be6zScOd8VJh7RJsVoxqScl%2FxYr07J%2FAiEAtkNgvBrlmm95eLdSRRxEG6KGPXwufqWqmyHBZJnyRhoqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGVt%2BFKkv0qt5G4yjCrcA%2FdJSg6j%2BpCGbqGLXFvurHz9mLRj9MfbTvs%2BqWgNZ2MrTSq6Ib4VRLOR1IZXHxswlNqpHIVSlVGyi%2FSbPSX3gjgjwQYrLBsBAG%2Fwd%2Ft0JM5OCidOR7GhnmcdfG5XfiLBdThw5mKBUMkvfmTzc4XmM5xOHTkqY8Y3VSQkQdOKsxrySxGOXikUD7D31M67%2BI1AcBbhY6x0l2xh1WhGBEk75gg1Vvg1MJUgnQaQNyznszSQ4CWFn1U9hgFguRsCYRHRAu74EQ1sji5QfyXBBxFTIdyeGbVpTZ%2BXsw5rPT%2FdtOKueuaB%2BsyE45sNgg7bYPOUGBlnUG%2B4wXzxQCqYSC%2FI172Cee4q6Yn555dMfi%2F3L9KbcYzUs%2Fd9DezcQxKFxJOFnAhfWLtZFgMo%2FD6E3JKXYx94cXY8sHhL7BxwI1C7eht%2FHk3XjK5qyyx1HXhabFJ%2FIjXf7%2Bt9ApsgBZETDZuCPZyEyunhYlOf78z5AhMkbOGYzIO%2FMtYNI3ZFgYmeudSWH3WzTOjP32JBOq07etS%2BWxqqssHZYuZ%2BVpCmFrZWNbb2c%2FkXBxx6lGwTEs9qk4lMQHSGWfypfxASWS027raWnX5fe4khPqBdjVnj%2B7v2PwNGf7gsXY9opA0ljGvwML6W67wGOqUB1fuEGgFm8cjhT0Ug9aADVw5oxlPy50UYDLjSXzUyKkpWcii5P2r61KvKrAG7CxerfbtGN72u0pSxES8xvqIluvj0NWa55%2FlGHGU3Yhy3mqpy6dybSPsMtheh3025zhJDgBm%2BHzIarNO55JIKWfeqTB0RuUP3qgM5jdKTw3THFmxq2drlIVNpE4COmM2heRYhjTiaYp4C0PGHaI6vPqPLtlS5X1zz&X-Amz-Signature=db37d9f05ad54c53f928105ed7a9a2966d941a182137ca4677bf5f6144d0a4d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626OMWRUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpz%2B%2Bz1Y3dYKbz6%2Foym6w1TMwUxm%2Fv0V9BiDRXKD5XfAiEAwpSvIipnLY8YQp%2FXkCWx757kX16xc3hd5yIb77Hb3csqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClo1bvf%2BE5E2DdoOSrcA3aBDlotL6pROBCmkL4Kn3QPnVwHChJi4K0HOTrhcN4juR0cgz9SU%2Fdvgo6TGRWWI787%2BMc3hmiVbEip6vMI4tvQbIRyWJ1QHXUtDIyqGIQ3Cp4MzgqbhRLFIDNQIIfqib5xE80CLzlB%2F4MfPGPLe6tDJuQeVhWmi9e%2B6BuIDtz1V5pVQyxI3mGfHXyD5p5flfyg08DRfY0e8Z3t5dezeJVLQVBrAEhCwWAQ7HaGaBv3JDbhAsIDFi1dzA6J9I4o5YZHAS8c3kMi8ADVIXZWlWzK5XzFZZIasdPpnvxQtYFHxm4NC1mLFOWiSvxhq8ycJJ6ym2MOKlxxpZWuNrzbhU9DFVCLIygcPW3hgbLskerfvx1QHE03%2BNwyko9%2BhIKRq7I6qvS0iDWgQ8uhBQiRjz4dBZWjgmO%2FLOwhGdpAQMfsgHdXbDyRkL1wymSjjG0GirxAzWI7Y5USrSnc1S4gAsi9PtED62601I0pLb1KYhqEEpXANduR3haCHTXBhnST4FzS62OowNhunP22J4nFCXWqTtRavfTGFZZUK%2FCjWissjusxBSj1TuVxfuVadhp4VZ%2FFFtS8iGL1gxRayxXx1zIMNi%2FABkq3nDICbD4aiJZeqyp38Q2O8qWYo6ZTMOSW67wGOqUBJXfccyqpWY7BLX5Y1s%2Fj2hMDbaRlE4a3M9wRKkwiMl5REQpnmxkNNELH9qtZeDLr4ZTt1n5ZD94EezzEKAiB%2BPb0Sj8MZThaFuCXeeFAtMAI3CwV8Kt7ZjoPYD%2BRZU81e7lZMXVx6oaBT4pH3JXnAoeHQdN94zd4Mywti3kxnCQyloq9ysp0KMRovOuronRHNrsKnaGhsLlB2Igl2isbFr1FU%2BCQ&X-Amz-Signature=5d264965fcbe0fd4917da86d9051e8b98c0b62e8b0fe0ad6de511a27db0200e9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626OMWRUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpz%2B%2Bz1Y3dYKbz6%2Foym6w1TMwUxm%2Fv0V9BiDRXKD5XfAiEAwpSvIipnLY8YQp%2FXkCWx757kX16xc3hd5yIb77Hb3csqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClo1bvf%2BE5E2DdoOSrcA3aBDlotL6pROBCmkL4Kn3QPnVwHChJi4K0HOTrhcN4juR0cgz9SU%2Fdvgo6TGRWWI787%2BMc3hmiVbEip6vMI4tvQbIRyWJ1QHXUtDIyqGIQ3Cp4MzgqbhRLFIDNQIIfqib5xE80CLzlB%2F4MfPGPLe6tDJuQeVhWmi9e%2B6BuIDtz1V5pVQyxI3mGfHXyD5p5flfyg08DRfY0e8Z3t5dezeJVLQVBrAEhCwWAQ7HaGaBv3JDbhAsIDFi1dzA6J9I4o5YZHAS8c3kMi8ADVIXZWlWzK5XzFZZIasdPpnvxQtYFHxm4NC1mLFOWiSvxhq8ycJJ6ym2MOKlxxpZWuNrzbhU9DFVCLIygcPW3hgbLskerfvx1QHE03%2BNwyko9%2BhIKRq7I6qvS0iDWgQ8uhBQiRjz4dBZWjgmO%2FLOwhGdpAQMfsgHdXbDyRkL1wymSjjG0GirxAzWI7Y5USrSnc1S4gAsi9PtED62601I0pLb1KYhqEEpXANduR3haCHTXBhnST4FzS62OowNhunP22J4nFCXWqTtRavfTGFZZUK%2FCjWissjusxBSj1TuVxfuVadhp4VZ%2FFFtS8iGL1gxRayxXx1zIMNi%2FABkq3nDICbD4aiJZeqyp38Q2O8qWYo6ZTMOSW67wGOqUBJXfccyqpWY7BLX5Y1s%2Fj2hMDbaRlE4a3M9wRKkwiMl5REQpnmxkNNELH9qtZeDLr4ZTt1n5ZD94EezzEKAiB%2BPb0Sj8MZThaFuCXeeFAtMAI3CwV8Kt7ZjoPYD%2BRZU81e7lZMXVx6oaBT4pH3JXnAoeHQdN94zd4Mywti3kxnCQyloq9ysp0KMRovOuronRHNrsKnaGhsLlB2Igl2isbFr1FU%2BCQ&X-Amz-Signature=170208b659572864a8f796cec76eb16605aea3216b315291860d527d7555c527&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626OMWRUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpz%2B%2Bz1Y3dYKbz6%2Foym6w1TMwUxm%2Fv0V9BiDRXKD5XfAiEAwpSvIipnLY8YQp%2FXkCWx757kX16xc3hd5yIb77Hb3csqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClo1bvf%2BE5E2DdoOSrcA3aBDlotL6pROBCmkL4Kn3QPnVwHChJi4K0HOTrhcN4juR0cgz9SU%2Fdvgo6TGRWWI787%2BMc3hmiVbEip6vMI4tvQbIRyWJ1QHXUtDIyqGIQ3Cp4MzgqbhRLFIDNQIIfqib5xE80CLzlB%2F4MfPGPLe6tDJuQeVhWmi9e%2B6BuIDtz1V5pVQyxI3mGfHXyD5p5flfyg08DRfY0e8Z3t5dezeJVLQVBrAEhCwWAQ7HaGaBv3JDbhAsIDFi1dzA6J9I4o5YZHAS8c3kMi8ADVIXZWlWzK5XzFZZIasdPpnvxQtYFHxm4NC1mLFOWiSvxhq8ycJJ6ym2MOKlxxpZWuNrzbhU9DFVCLIygcPW3hgbLskerfvx1QHE03%2BNwyko9%2BhIKRq7I6qvS0iDWgQ8uhBQiRjz4dBZWjgmO%2FLOwhGdpAQMfsgHdXbDyRkL1wymSjjG0GirxAzWI7Y5USrSnc1S4gAsi9PtED62601I0pLb1KYhqEEpXANduR3haCHTXBhnST4FzS62OowNhunP22J4nFCXWqTtRavfTGFZZUK%2FCjWissjusxBSj1TuVxfuVadhp4VZ%2FFFtS8iGL1gxRayxXx1zIMNi%2FABkq3nDICbD4aiJZeqyp38Q2O8qWYo6ZTMOSW67wGOqUBJXfccyqpWY7BLX5Y1s%2Fj2hMDbaRlE4a3M9wRKkwiMl5REQpnmxkNNELH9qtZeDLr4ZTt1n5ZD94EezzEKAiB%2BPb0Sj8MZThaFuCXeeFAtMAI3CwV8Kt7ZjoPYD%2BRZU81e7lZMXVx6oaBT4pH3JXnAoeHQdN94zd4Mywti3kxnCQyloq9ysp0KMRovOuronRHNrsKnaGhsLlB2Igl2isbFr1FU%2BCQ&X-Amz-Signature=24482ea6193584f80ed77d10cd1a7f7facf1baf61a90610d14f5160ab0cf746e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626OMWRUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpz%2B%2Bz1Y3dYKbz6%2Foym6w1TMwUxm%2Fv0V9BiDRXKD5XfAiEAwpSvIipnLY8YQp%2FXkCWx757kX16xc3hd5yIb77Hb3csqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClo1bvf%2BE5E2DdoOSrcA3aBDlotL6pROBCmkL4Kn3QPnVwHChJi4K0HOTrhcN4juR0cgz9SU%2Fdvgo6TGRWWI787%2BMc3hmiVbEip6vMI4tvQbIRyWJ1QHXUtDIyqGIQ3Cp4MzgqbhRLFIDNQIIfqib5xE80CLzlB%2F4MfPGPLe6tDJuQeVhWmi9e%2B6BuIDtz1V5pVQyxI3mGfHXyD5p5flfyg08DRfY0e8Z3t5dezeJVLQVBrAEhCwWAQ7HaGaBv3JDbhAsIDFi1dzA6J9I4o5YZHAS8c3kMi8ADVIXZWlWzK5XzFZZIasdPpnvxQtYFHxm4NC1mLFOWiSvxhq8ycJJ6ym2MOKlxxpZWuNrzbhU9DFVCLIygcPW3hgbLskerfvx1QHE03%2BNwyko9%2BhIKRq7I6qvS0iDWgQ8uhBQiRjz4dBZWjgmO%2FLOwhGdpAQMfsgHdXbDyRkL1wymSjjG0GirxAzWI7Y5USrSnc1S4gAsi9PtED62601I0pLb1KYhqEEpXANduR3haCHTXBhnST4FzS62OowNhunP22J4nFCXWqTtRavfTGFZZUK%2FCjWissjusxBSj1TuVxfuVadhp4VZ%2FFFtS8iGL1gxRayxXx1zIMNi%2FABkq3nDICbD4aiJZeqyp38Q2O8qWYo6ZTMOSW67wGOqUBJXfccyqpWY7BLX5Y1s%2Fj2hMDbaRlE4a3M9wRKkwiMl5REQpnmxkNNELH9qtZeDLr4ZTt1n5ZD94EezzEKAiB%2BPb0Sj8MZThaFuCXeeFAtMAI3CwV8Kt7ZjoPYD%2BRZU81e7lZMXVx6oaBT4pH3JXnAoeHQdN94zd4Mywti3kxnCQyloq9ysp0KMRovOuronRHNrsKnaGhsLlB2Igl2isbFr1FU%2BCQ&X-Amz-Signature=113643e7b6711e5017904c896193c2064902d0d394554602c17595c281e4e3b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626OMWRUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpz%2B%2Bz1Y3dYKbz6%2Foym6w1TMwUxm%2Fv0V9BiDRXKD5XfAiEAwpSvIipnLY8YQp%2FXkCWx757kX16xc3hd5yIb77Hb3csqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClo1bvf%2BE5E2DdoOSrcA3aBDlotL6pROBCmkL4Kn3QPnVwHChJi4K0HOTrhcN4juR0cgz9SU%2Fdvgo6TGRWWI787%2BMc3hmiVbEip6vMI4tvQbIRyWJ1QHXUtDIyqGIQ3Cp4MzgqbhRLFIDNQIIfqib5xE80CLzlB%2F4MfPGPLe6tDJuQeVhWmi9e%2B6BuIDtz1V5pVQyxI3mGfHXyD5p5flfyg08DRfY0e8Z3t5dezeJVLQVBrAEhCwWAQ7HaGaBv3JDbhAsIDFi1dzA6J9I4o5YZHAS8c3kMi8ADVIXZWlWzK5XzFZZIasdPpnvxQtYFHxm4NC1mLFOWiSvxhq8ycJJ6ym2MOKlxxpZWuNrzbhU9DFVCLIygcPW3hgbLskerfvx1QHE03%2BNwyko9%2BhIKRq7I6qvS0iDWgQ8uhBQiRjz4dBZWjgmO%2FLOwhGdpAQMfsgHdXbDyRkL1wymSjjG0GirxAzWI7Y5USrSnc1S4gAsi9PtED62601I0pLb1KYhqEEpXANduR3haCHTXBhnST4FzS62OowNhunP22J4nFCXWqTtRavfTGFZZUK%2FCjWissjusxBSj1TuVxfuVadhp4VZ%2FFFtS8iGL1gxRayxXx1zIMNi%2FABkq3nDICbD4aiJZeqyp38Q2O8qWYo6ZTMOSW67wGOqUBJXfccyqpWY7BLX5Y1s%2Fj2hMDbaRlE4a3M9wRKkwiMl5REQpnmxkNNELH9qtZeDLr4ZTt1n5ZD94EezzEKAiB%2BPb0Sj8MZThaFuCXeeFAtMAI3CwV8Kt7ZjoPYD%2BRZU81e7lZMXVx6oaBT4pH3JXnAoeHQdN94zd4Mywti3kxnCQyloq9ysp0KMRovOuronRHNrsKnaGhsLlB2Igl2isbFr1FU%2BCQ&X-Amz-Signature=23d5616b3cbcd05b8d4c084abf384d606aba12023ede11d6a6539bbfa4066867&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626OMWRUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpz%2B%2Bz1Y3dYKbz6%2Foym6w1TMwUxm%2Fv0V9BiDRXKD5XfAiEAwpSvIipnLY8YQp%2FXkCWx757kX16xc3hd5yIb77Hb3csqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClo1bvf%2BE5E2DdoOSrcA3aBDlotL6pROBCmkL4Kn3QPnVwHChJi4K0HOTrhcN4juR0cgz9SU%2Fdvgo6TGRWWI787%2BMc3hmiVbEip6vMI4tvQbIRyWJ1QHXUtDIyqGIQ3Cp4MzgqbhRLFIDNQIIfqib5xE80CLzlB%2F4MfPGPLe6tDJuQeVhWmi9e%2B6BuIDtz1V5pVQyxI3mGfHXyD5p5flfyg08DRfY0e8Z3t5dezeJVLQVBrAEhCwWAQ7HaGaBv3JDbhAsIDFi1dzA6J9I4o5YZHAS8c3kMi8ADVIXZWlWzK5XzFZZIasdPpnvxQtYFHxm4NC1mLFOWiSvxhq8ycJJ6ym2MOKlxxpZWuNrzbhU9DFVCLIygcPW3hgbLskerfvx1QHE03%2BNwyko9%2BhIKRq7I6qvS0iDWgQ8uhBQiRjz4dBZWjgmO%2FLOwhGdpAQMfsgHdXbDyRkL1wymSjjG0GirxAzWI7Y5USrSnc1S4gAsi9PtED62601I0pLb1KYhqEEpXANduR3haCHTXBhnST4FzS62OowNhunP22J4nFCXWqTtRavfTGFZZUK%2FCjWissjusxBSj1TuVxfuVadhp4VZ%2FFFtS8iGL1gxRayxXx1zIMNi%2FABkq3nDICbD4aiJZeqyp38Q2O8qWYo6ZTMOSW67wGOqUBJXfccyqpWY7BLX5Y1s%2Fj2hMDbaRlE4a3M9wRKkwiMl5REQpnmxkNNELH9qtZeDLr4ZTt1n5ZD94EezzEKAiB%2BPb0Sj8MZThaFuCXeeFAtMAI3CwV8Kt7ZjoPYD%2BRZU81e7lZMXVx6oaBT4pH3JXnAoeHQdN94zd4Mywti3kxnCQyloq9ysp0KMRovOuronRHNrsKnaGhsLlB2Igl2isbFr1FU%2BCQ&X-Amz-Signature=e413fd751ceddb06082f93c2fd23ff8b9aa786b23f72128bbfa5a85ebbc7a451&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RTQPF65%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAeemXhMO798NIPrcC12dR%2ByIKbNgdYmISlV3jlXcrezAiACdKCzMqaFiI7OkL4LL2kbn%2FPETnsf17l6HxJ5XWirzyqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKsFaWlff5jvAvLQ9KtwD9WcxK9wa6KKBLE8X0F%2Fig1Jt%2F%2B0hU3lqN0Mdv2Zm59uwQsH9lYvcc2V1ERPoyZE1ZlGnCapRn%2B%2Fo%2FLn66%2BowO4WMQuPKONgijjsKJADTMTi7g6HXNPH3rWdL%2FwHo5IbsbeHvZ0Gqrt7XZ5yeBgLRmC1YL5Js7WXxdJCVLd12j483w6ItwQO4fcQLSiYLCcnaa482ufgKOcn6k5RXH1jinvxodSZovpuIE4OoyCQKxh1cizFSITbe%2BfgBiPmkV9Iuxx8oZ4z8M1HcrCQFyrXCZLkl%2BkkCYwfRDBK75PlCAUt76hUUj2G%2FKause7ZRkG6QplGAubs%2FDgigJYBSunNr9qWctxIXJogSXSdTGuDeLmuqRTty4UwX2dy%2FsOATasg2PQ1W2tt70Bzlne24tpWClOB6SxnuNdLf8XsXfDGFnwkEfkhDiQfarGA85Uu5lC4RC5UsuGLHUztk3OrIzzu7939szexSoehcNq5tLCMfNPBvX%2BLIz7m9M65yFOkNPmLVZWk18wGc%2BHUhYWg8jHfV1%2F2AbUNrIn0ErJfNyz6EvQ54bptS2M%2Bor4%2FrahYaeR5F7jKZPIxkd790qwkF%2FDpNeF0ZX6fp3eVV2ENXOAQqLvUfKz%2FHlKJKA0Y1Euww6ZbrvAY6pgFvlmtXls9%2BKv9O5bV2ObXtVlrBrI%2Blx5pT7Q0RI%2FnLmqiHg0kEngrNux35d7kYeM%2BwLeKNLtgO2kv2r%2FHzNphKdjSvS3CFYmLwZB4RdILccrMr8o2o0dCr%2FCv9KNN1VrTGkcC99oO5mzVojDEt6LiOZxrsDvsOxi4CSftDKROQasrYo3L782xlFFudb0U6HRK3CSZ1JwGaN2mbNqjIwrHxDIrGnPT4&X-Amz-Signature=b9dd2e198879c7d445a747d5c210e05d6e805c01326bf0f21c55457ef30f8643&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN65G3ND%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNGfNgi2rvakM3ziFN70G2jPE%2BGRGezt2mN%2BxpIPA7rgIhAOAve4vbLuyR169gn5ahoWGzDM9DpdVhiVtXFQjNzEgUKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxSSol8pEudPMbHDu8q3AOIdlaQO8KNJOpl2FQBEH4WqbnjPp4hVhuW5y6agVpla00spteam1wQi33RcJss0ghnYQtkTG%2BOWFnCcRSEdG6geUZhzIR6D0fZakvzGXghapm8%2FORhp7zKaLZ5gkT7cTgYKpUXRHdZi%2FBQsh%2Fpv4yBkt5CByDOtOlc63Hoe4dwcipBpCdBCy0FdjN9I4uIwhpQP6FxnA%2Bsg7Fv4iJ375i4u9QasqVHYNKFtwcOqyeMGCMbU7B7DbsA%2BPTs2PvSI8oL9Xj0uPTw0ALF%2FZuqhu8B%2BCFXLOrElANrKuwJmN1bkb%2FCWfhUX5zTX2FxSI6wh4tm%2BoH7R39uNm3oFtwmhjzrHVfYYjSlAXBLB%2FoZtBEE1NN6nIbXe9Vhp67%2FoRuwrFyfctwHiiOReNhqirl0Es8DNTuyUirmhr%2Fq7IRJF3o%2BWVnUkX7t2n8Hv5suZGesS3mdbXUQim0mlzkWMV2Vv%2F5jb9aZ%2BC1K%2BA9u74%2BrCIDzWUkKoNjQmnhJ3BYms9Bcx7L7o22MMJDrFTbaQ30RlDRBIGWVvuv9ipBj4XvNSb5heYhUcfxX6BHB1mjJhl%2F5IcQ9BGWz1q%2BFhKFIynIfWYdOBTA1WZh6pQQJdk2MsvHQOKTPIIYoFNbLu5kmITDnluu8BjqkAZvgR4uhQKAjZMYWsCPKgYux%2FmrV66UUZdB1bNtorLurQXNHe7%2BuEhRAwt1mQCB0Gzs0bIGd8Gv8VrSsDMuIa%2BclF5w416M8rmnOkEszTrrlDVftM9IiL%2FmLOEc8Xg%2FI5GfLg8iOsBiS1sg7Rc8qW15hxaiMMYG9E8%2F9qIRIcAWxVl97wE01xiVX99ut2%2FTYNFO0LwI9nqc2bpHQbGZTNbwpAdKJ&X-Amz-Signature=feefd6cff35f3792aeb14af511c8ec8986dff563bbf7b52cbd58e8ba16f51ee4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626OMWRUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpz%2B%2Bz1Y3dYKbz6%2Foym6w1TMwUxm%2Fv0V9BiDRXKD5XfAiEAwpSvIipnLY8YQp%2FXkCWx757kX16xc3hd5yIb77Hb3csqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClo1bvf%2BE5E2DdoOSrcA3aBDlotL6pROBCmkL4Kn3QPnVwHChJi4K0HOTrhcN4juR0cgz9SU%2Fdvgo6TGRWWI787%2BMc3hmiVbEip6vMI4tvQbIRyWJ1QHXUtDIyqGIQ3Cp4MzgqbhRLFIDNQIIfqib5xE80CLzlB%2F4MfPGPLe6tDJuQeVhWmi9e%2B6BuIDtz1V5pVQyxI3mGfHXyD5p5flfyg08DRfY0e8Z3t5dezeJVLQVBrAEhCwWAQ7HaGaBv3JDbhAsIDFi1dzA6J9I4o5YZHAS8c3kMi8ADVIXZWlWzK5XzFZZIasdPpnvxQtYFHxm4NC1mLFOWiSvxhq8ycJJ6ym2MOKlxxpZWuNrzbhU9DFVCLIygcPW3hgbLskerfvx1QHE03%2BNwyko9%2BhIKRq7I6qvS0iDWgQ8uhBQiRjz4dBZWjgmO%2FLOwhGdpAQMfsgHdXbDyRkL1wymSjjG0GirxAzWI7Y5USrSnc1S4gAsi9PtED62601I0pLb1KYhqEEpXANduR3haCHTXBhnST4FzS62OowNhunP22J4nFCXWqTtRavfTGFZZUK%2FCjWissjusxBSj1TuVxfuVadhp4VZ%2FFFtS8iGL1gxRayxXx1zIMNi%2FABkq3nDICbD4aiJZeqyp38Q2O8qWYo6ZTMOSW67wGOqUBJXfccyqpWY7BLX5Y1s%2Fj2hMDbaRlE4a3M9wRKkwiMl5REQpnmxkNNELH9qtZeDLr4ZTt1n5ZD94EezzEKAiB%2BPb0Sj8MZThaFuCXeeFAtMAI3CwV8Kt7ZjoPYD%2BRZU81e7lZMXVx6oaBT4pH3JXnAoeHQdN94zd4Mywti3kxnCQyloq9ysp0KMRovOuronRHNrsKnaGhsLlB2Igl2isbFr1FU%2BCQ&X-Amz-Signature=1d859e4dde2917e7084db7227a991ec1bbd91d24df5a1b6fd312ccd7c73f53eb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626OMWRUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpz%2B%2Bz1Y3dYKbz6%2Foym6w1TMwUxm%2Fv0V9BiDRXKD5XfAiEAwpSvIipnLY8YQp%2FXkCWx757kX16xc3hd5yIb77Hb3csqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClo1bvf%2BE5E2DdoOSrcA3aBDlotL6pROBCmkL4Kn3QPnVwHChJi4K0HOTrhcN4juR0cgz9SU%2Fdvgo6TGRWWI787%2BMc3hmiVbEip6vMI4tvQbIRyWJ1QHXUtDIyqGIQ3Cp4MzgqbhRLFIDNQIIfqib5xE80CLzlB%2F4MfPGPLe6tDJuQeVhWmi9e%2B6BuIDtz1V5pVQyxI3mGfHXyD5p5flfyg08DRfY0e8Z3t5dezeJVLQVBrAEhCwWAQ7HaGaBv3JDbhAsIDFi1dzA6J9I4o5YZHAS8c3kMi8ADVIXZWlWzK5XzFZZIasdPpnvxQtYFHxm4NC1mLFOWiSvxhq8ycJJ6ym2MOKlxxpZWuNrzbhU9DFVCLIygcPW3hgbLskerfvx1QHE03%2BNwyko9%2BhIKRq7I6qvS0iDWgQ8uhBQiRjz4dBZWjgmO%2FLOwhGdpAQMfsgHdXbDyRkL1wymSjjG0GirxAzWI7Y5USrSnc1S4gAsi9PtED62601I0pLb1KYhqEEpXANduR3haCHTXBhnST4FzS62OowNhunP22J4nFCXWqTtRavfTGFZZUK%2FCjWissjusxBSj1TuVxfuVadhp4VZ%2FFFtS8iGL1gxRayxXx1zIMNi%2FABkq3nDICbD4aiJZeqyp38Q2O8qWYo6ZTMOSW67wGOqUBJXfccyqpWY7BLX5Y1s%2Fj2hMDbaRlE4a3M9wRKkwiMl5REQpnmxkNNELH9qtZeDLr4ZTt1n5ZD94EezzEKAiB%2BPb0Sj8MZThaFuCXeeFAtMAI3CwV8Kt7ZjoPYD%2BRZU81e7lZMXVx6oaBT4pH3JXnAoeHQdN94zd4Mywti3kxnCQyloq9ysp0KMRovOuronRHNrsKnaGhsLlB2Igl2isbFr1FU%2BCQ&X-Amz-Signature=50be3748306d852f87ab2a99c5bce6abb1b3f7948f10ac7c77e307ff5a01a067&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626OMWRUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpz%2B%2Bz1Y3dYKbz6%2Foym6w1TMwUxm%2Fv0V9BiDRXKD5XfAiEAwpSvIipnLY8YQp%2FXkCWx757kX16xc3hd5yIb77Hb3csqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClo1bvf%2BE5E2DdoOSrcA3aBDlotL6pROBCmkL4Kn3QPnVwHChJi4K0HOTrhcN4juR0cgz9SU%2Fdvgo6TGRWWI787%2BMc3hmiVbEip6vMI4tvQbIRyWJ1QHXUtDIyqGIQ3Cp4MzgqbhRLFIDNQIIfqib5xE80CLzlB%2F4MfPGPLe6tDJuQeVhWmi9e%2B6BuIDtz1V5pVQyxI3mGfHXyD5p5flfyg08DRfY0e8Z3t5dezeJVLQVBrAEhCwWAQ7HaGaBv3JDbhAsIDFi1dzA6J9I4o5YZHAS8c3kMi8ADVIXZWlWzK5XzFZZIasdPpnvxQtYFHxm4NC1mLFOWiSvxhq8ycJJ6ym2MOKlxxpZWuNrzbhU9DFVCLIygcPW3hgbLskerfvx1QHE03%2BNwyko9%2BhIKRq7I6qvS0iDWgQ8uhBQiRjz4dBZWjgmO%2FLOwhGdpAQMfsgHdXbDyRkL1wymSjjG0GirxAzWI7Y5USrSnc1S4gAsi9PtED62601I0pLb1KYhqEEpXANduR3haCHTXBhnST4FzS62OowNhunP22J4nFCXWqTtRavfTGFZZUK%2FCjWissjusxBSj1TuVxfuVadhp4VZ%2FFFtS8iGL1gxRayxXx1zIMNi%2FABkq3nDICbD4aiJZeqyp38Q2O8qWYo6ZTMOSW67wGOqUBJXfccyqpWY7BLX5Y1s%2Fj2hMDbaRlE4a3M9wRKkwiMl5REQpnmxkNNELH9qtZeDLr4ZTt1n5ZD94EezzEKAiB%2BPb0Sj8MZThaFuCXeeFAtMAI3CwV8Kt7ZjoPYD%2BRZU81e7lZMXVx6oaBT4pH3JXnAoeHQdN94zd4Mywti3kxnCQyloq9ysp0KMRovOuronRHNrsKnaGhsLlB2Igl2isbFr1FU%2BCQ&X-Amz-Signature=6b0bbe3288660c2981ba021cf084f07cb6e9b0d0acb437f63309d2b735784d78&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHNGJFS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlhjliEq0wZHRVjCNA44ytroF556GEUh1Vl5465OkdmgIgE0r8MYWqhAYj7lyWWujCNtcIJzz%2F%2B3vqy8PuNIfc1SUqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEkrltnI%2Bzm8NXMTsircAy3crN6xw4PRh1TV1OH%2B0OGaqPTvt3WlOJ3NY9E8QbO0RFI52jlTMZO2x01TXPlFmk%2BWM5kIwgq8Hy9woGkYoAx9oxleXHTt7%2F6wpm8HDVzMRC1rh91Wu5eGPIQWAC0uDMOOG9C5yGCQEZ5uhMoOAauP7ecyauqIz8Pl2Bo6AysjntBAkkpIxIlJSmQog88QfUndcYTTLXo2xYI%2BEvWi%2BeZEWmUm0F%2BQL7aHxjIcbaPL5SzvPKjChSbZoTJhI2FhA9n%2FaoKwEEqjQOi02cG05Dit%2FcUfkdzA85YmUmAFDiWvaMUXTRO3aOyA24TE845cegI93hsWSKmF76zlyjT%2FKz%2BZ5RULDjFO373mp3ne3KzHvfqBq9BNCl7u3AgxIJsl6MH%2BlWvA9uZOMPiciC1%2BOr6TmRidAbDko%2FtecoH3XEeUxGA7KwAs3ahy7s0W3lK4MebVNZxZssAca%2B6WNi1KUTStwRV4l0f86kZd25iuuL%2FkYKirLNU%2Fk9iTlCdqt0ZCkGeVrO%2Bt0AOw5ZpDeWb2tmze52%2FENGJkmcHsYoPxtD%2BCyh5qZrf0%2BghTPbYeZVw01mhv3lnKEz9CWXu83R4ML9qmk4TxfToT9ZSqrB6dlMLfr2BB5snUBb0kNMItMLKW67wGOqUBXkoe23m%2F2ANGnEpRunKzKz1gmJHLTIS7EM%2B%2B7IXgo1IGeSUAVXnYmbbF5rGY6R%2BfrMfwGx3JDAWkDy7Vc2VpcawB7rWrCgjQu6bkbLTahNUve1r9EAhSk5G3to6SfWsEdcxHD2sRVRRh4rOwDUEyZavIMGIxkNDIIeHjdzD7XJY%2BpwX0wkGyd9DNr6PsfdM4xUlSOTxHW1ExfC5gwU0G7FY5miMW&X-Amz-Signature=6434ec56e4e45d33c5bd32bb78bf227675fe89a466f78ddf11e5ebe5a5aeaea3&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TLZNU7Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQ34ZhIjqpWAL2B7n6IcXI5Gcf7HZ8R2Py71gnB80NUAiBpxY03GjWteCae2KgdRvcUtA16xyarvuZ%2Fu8342pArvyqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCJSG6BMMMpxMlSBOKtwDVfg%2F4tt%2BjWy9ye6XEAPPuv9MXkiaUsTP4AlZIS4mLkfMWkSkXp%2B%2FR5H5Y0voBlbhajvHfqY5SZUe5Kt4CRMw6i5SdTQn%2BBKlsAoTmVqieBKcFJ9yRxl65el593EPvQv8pVLeqKzmrnfXtcx7nymGr3CcTZd0p3AsYER2QzH%2FvTPz%2F9kP2Z30GSoeMlleYuG7AaRKqIVw5n2TnYkOJQWgGpIEUDvKKyAZTLboPB4%2BoeNx5v5HsOX0g8qQkVRGRn1bnm1QDMJqfRjrG3U4%2FLVejPodVskjFFsDTWc1t4cUu%2F3o%2FYsjSROvicyec%2BooOzkxy9CzRbqeMH28%2F2w72G0Fjr2DpYLwrnXpttRazVse71BMEF2v3xk3dPmiKig6zQdLvviGKDZEXi6vmPnEJRO6TQtBbo06ahsi7xy5UefKjUYoUhbx75up8KuhZYVmqzCzSDl955VZ3e3I5allzjbm6RoVAQ6RlTpcpepH%2BsLONtVIKasZ5IGjzliPf0GH3vVotEE1ws6uYyAZJZax4k7kSuc0Q%2FU27G04UReTEU31Vz34jIYewDWzC6%2Ffq8Z0dD%2BOr%2BVmoeYrd2ZI9LeOgPVu1m5zl9j4bGrtR%2FMnXx1K7mmJEUhqv9fHuyYRS%2B0wupbrvAY6pgHIKX%2Fh%2FLwXM3pN2iYKpwDPIoVwVMornaiydrwvyMoP29z9r5Hwdy8X5vKDkwPAeK0NcT4jPva%2BNtXEoqhZXerUAZmAcorRVYAuCGauf7cwlYEFrj0BvLXdwKgIi0L%2FNp8ZT2Nk4%2B0KE%2FjdzraLIX9Ct27483%2B5lv5CU44V4taPAPSNYTo%2FNJdlb%2B6ktQPWJCBfkiF3I2TsQ30DGBbRIopWeJFDAIvn&X-Amz-Signature=36309d828d7c0103910617ba3e4afd92369d6ed13b9121c77e310e1bfda9312a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ4ZKNZ4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDl%2FQtmiHmcN3EwQPL9rvXp0iSnso%2BRgWsh%2Fn8HfRfyDAiBsTQgr4afoRQMSC6vGdXBjLUPsxuVCUq78vtcF%2Bm611CqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtVMkck%2Fx4LyckvXGKtwD4wlAB2XZ%2B4jnZlCWISDpmYy5zspffZ12CkyKy2X1Q0T1VdZouqiB7Icy5BEntj333l1p4GlpKzkU72OSQ16QMl6ZHy5m9A3urNIH7Fztf5ms2HoxY%2FhzJCenXRrwUymsxX52b9Pv4rI9g5V4ur9IFwhEn2uwsKXLQ%2BT8OMQbGelgcVydhPxulecJkS2wHW0QV7OkN7I2vckrn4mAdgTl8Zv5yKxMdTRPp%2FYL3ySy5%2B6O5B0npxK%2FvBiVtuVe7vRtd2GoOqK6Ra64AS3AKnoZM%2B9JYT%2BSB2c4wsERJoZp4qrqG8zWF7BEgmHlhL%2F7PKgazWElfp2ALfLZLViaHnWp21PboxYdU6u7eWDI%2BMi%2BYTnG4LJOLomLrpWWBygF65pMpymh6Vvm9hJ8Ct2HyK4v26P%2F1m4pnxh1aMdrCgjCXzpj%2FunWo1bMwHQkAMRd9C2Ml9frWko4h8DoDZ%2Fs2jeK6zrG%2FRij5h81rGPbNC3hvPK2tl%2BXawiZ0dYgAaBt1El%2F516XZNd8d%2BHa6ZB04idYTm%2FZhtXddmk%2FlbFA2IaDEeksPtVVIiTI2KeyPSQlfkPODKDRtwB%2B%2FOnOHnSbrtkyTrbslpB5OWNP34VGF%2BqJl8EyzC1sOLaLaONN1CYw%2B5brvAY6pgHupP1vp1ZVLZXr788McjqAef0KHpN%2F3K0kY3M%2FnoQKlrOoPxq05fWDkMQf2mYmHd7PBmvPPcjXUYfO8KbvR4iJpdPqmkfQ01z0L48NaSjh07y9b7xE6dG7kYaO%2BrzZkb%2Br%2Be%2BJlhxYFNIFBWFohBJF3Ro7enrqaXf7sTmZKh2RgiTLg%2Bdogluo9VhF8GJ5HdOMv8ii55%2Fr11Awv6ewt0uCQ0Rpv96x&X-Amz-Signature=4f490f7ea0851c9a2100136332db1dcbf21ca44e5fdbdf292af30b4bd2d03769&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIETZXU5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAa7rs%2F2fUawFL7n5mYG%2F8of6C7Kk47iLYZWDZAhXASQIhAKcfX3ApHRIl5zvchqoQOuP4sxndsXSwrmhFwPAaB3UFKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7VCy7dXh2AldxYR4q3APszW7mIPkjMUD%2BHpbXQi0OhbgPFpGLwlQ75PvuOxRrHzMrsYY0erCZ12ouQRu2IjLtiKSdlFKd1zD8mzKKW8lxDPb4yzXmcrUWYiVZu87L%2FL5j4dei83RB4pxhioA6GJR0M5mN9Y7qW8usbEcRNzTDiHhvhehXruL6ioUwANnsnnJoH4EdFwkkX%2Bt3S5PGW3ZYSOiijPvRLfdBCjy9oO8K69vfYa52irsV6dynknB2owLB1zACzkasOiFo5f5r%2FlBJDX1unEj8zZW4dbPR1Xsv%2B6I6XVxbzTUk8gsokY45yp279rtu1peJOO6reDO5tPH164a9ak8CsTPfQaQ3N%2F3jAtt2NCbYu00k7CqOoYlhWkkUGDy7jRsNqMWu0O%2Fy9SUgslw4yBn1iMUp8S0dYODSwCi69LmuH2Mgi1VARq1gPg7zPbpP8IMgrOSb%2BB95FBDoRN28y8VWFiecTV%2Fox5ot4QNPWZPn8Hh3fY72ZkmdAXOjLruPc5UvDca4KbGIfoz0NY5etSXzVZnVKEWw7xPwlcFZ14ufR5fP6xPdsrBnQHTK%2BU9favVlqSvFza%2BSXwEUlx11bD%2BHmiACt5KRQrSVFLqm8d2Wv642duET%2Bm6WRsUFzWaDsDFFJGXYmDCHl%2Bu8BjqkATwcGsqLm6%2BvRpXRP3qTdNdU%2Bb5oW4A0sAUg85BpF3Cv866erl6s7RGicyaaFREEUq8Wta10EN8oqZ59%2F0PrN%2BU6cHEtkIGy177gVe0SwyU%2FhRMoR%2BelpFLKRYk434OEceq8%2FggBBp3vWc4CGtFRJtfW1yJivyl3ah7Onlf2uIMYy1%2Fk6bgoAasEeixGx%2B4SRjL8bvF898AfnssckIWR8Hk%2B2xES&X-Amz-Signature=4123d7012d94c06a2d67dcb1112f5dc33e74eaa527984e9bb695d34bd562b894&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIETZXU5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAa7rs%2F2fUawFL7n5mYG%2F8of6C7Kk47iLYZWDZAhXASQIhAKcfX3ApHRIl5zvchqoQOuP4sxndsXSwrmhFwPAaB3UFKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7VCy7dXh2AldxYR4q3APszW7mIPkjMUD%2BHpbXQi0OhbgPFpGLwlQ75PvuOxRrHzMrsYY0erCZ12ouQRu2IjLtiKSdlFKd1zD8mzKKW8lxDPb4yzXmcrUWYiVZu87L%2FL5j4dei83RB4pxhioA6GJR0M5mN9Y7qW8usbEcRNzTDiHhvhehXruL6ioUwANnsnnJoH4EdFwkkX%2Bt3S5PGW3ZYSOiijPvRLfdBCjy9oO8K69vfYa52irsV6dynknB2owLB1zACzkasOiFo5f5r%2FlBJDX1unEj8zZW4dbPR1Xsv%2B6I6XVxbzTUk8gsokY45yp279rtu1peJOO6reDO5tPH164a9ak8CsTPfQaQ3N%2F3jAtt2NCbYu00k7CqOoYlhWkkUGDy7jRsNqMWu0O%2Fy9SUgslw4yBn1iMUp8S0dYODSwCi69LmuH2Mgi1VARq1gPg7zPbpP8IMgrOSb%2BB95FBDoRN28y8VWFiecTV%2Fox5ot4QNPWZPn8Hh3fY72ZkmdAXOjLruPc5UvDca4KbGIfoz0NY5etSXzVZnVKEWw7xPwlcFZ14ufR5fP6xPdsrBnQHTK%2BU9favVlqSvFza%2BSXwEUlx11bD%2BHmiACt5KRQrSVFLqm8d2Wv642duET%2Bm6WRsUFzWaDsDFFJGXYmDCHl%2Bu8BjqkATwcGsqLm6%2BvRpXRP3qTdNdU%2Bb5oW4A0sAUg85BpF3Cv866erl6s7RGicyaaFREEUq8Wta10EN8oqZ59%2F0PrN%2BU6cHEtkIGy177gVe0SwyU%2FhRMoR%2BelpFLKRYk434OEceq8%2FggBBp3vWc4CGtFRJtfW1yJivyl3ah7Onlf2uIMYy1%2Fk6bgoAasEeixGx%2B4SRjL8bvF898AfnssckIWR8Hk%2B2xES&X-Amz-Signature=c4e31d80324684fe16e8068c6d23ede2a66ef7907eb3c46bdad533e99097bbfb&X-Amz-SignedHeaders=host&x-id=GetObject)

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
