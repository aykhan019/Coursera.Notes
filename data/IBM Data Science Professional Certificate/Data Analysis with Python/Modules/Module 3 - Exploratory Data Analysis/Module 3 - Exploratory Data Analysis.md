

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=3c3699be597a30429033a8c8fa041ae461f57c6ccd62ccb69622bb5bec13a4b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=0d9a267b4397bd3215c462dd4f9ed027ee8753094d644e8e0c8264b36065b90c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=e0b0c44f31edf0207d41439471c5d3a8b56d4d078566c6fd55019df8aefca9c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=b33d6c5ec26288f8f09bd55e3c92adb0668f74a1a7e2b3ad1bd9894725f2df82&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=5fa9f4c884b5012509a5da0d82cf6882ab5a5c863720273680b907b64a61df58&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=50c9e1db25e11d6077730bab1461c1630007bc44d745b0077a1fe3e68caf4b73&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=ed310da32232efcf66cc7fe86b6848c318ccbaa177624cae92c580627fcddbce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=1749005235616c63af11954d86de1f764c05248f45f1fd03ec78f77be6f8e8d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=dac104c7f53094f21c3b4fe13707c106b6e92b672cd35f274f9439954c5e3f45&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MDABVN4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDEXEjEFhtzk7SXdRblnJoEWyQrI4d4YL0gl8HV6fMF8QIgO8AO9vGnkMkmASgYwawjfrfhzBHW8NFhbJjEJTIWkhkq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMQwPKNusZ96fAL0NSrcA22XYRvRnQ8d1zCgV5XMzbKOp2ry6yPcYZO1QX%2BbOS%2BOMjKZUn1M%2FBU6BU4QtYPYX%2BbGrzMsyw8XsM0rXmBUsg2Alu3JqVIlJz8B8WwvmIQQyWCFTA%2FK1JPbqYvuQJx24AbzJt9rkwE%2BzzeqIuYMrRKcVHKph4hgSPhAFTc7r0ojCkjjtkJhhiVVpMZM2dKjtb1Ize1%2BIyhP5WHNmz8c9Z6Km0Y68y5%2B1J3ERk9n1nbD1TEX6UsnUmlaVioVHaQ1dJrCFVkgsvduHvxPaYv03%2Fu7bRjH6%2BAGB4gr%2BI7Ui%2BjLT7MqTz3Xl%2BirqBbICjhmMA46PRlLvO6WMkfU%2BFWZWjFsVEfa19gmNxfzIx6f9sfWW4nM9KFsihSm3tLaaqOfphEI28mc2dMyJvAlTh8YiGXvZfpoT4Pifs9%2FQz7Uzl70ncrNMHJSoG0Um2TbJEfMPbsZC%2FGuz1R3zbmWDE%2BeCxtPApbbxVAn6%2BHo5pDtXyr9go%2FB0fdJm3dH63zPSF2uiUeeFBLwe0FRwRqh2aWC7%2FPOAwLw3LS7BVej5a1zP4gdufo7Qi7we5L97Ip8zZ7jw8kXOyx0wkoHVwOKr5Ca82AJjoD2NzL%2BGmqfTR2%2F2A%2FJlGmgzqwZ%2BoneAF6xMNrqj70GOqUBxLq9Efy90h3hxuB2uSnYTNaOkm%2FRm5X2HxuAyUIn5hRRHyodLRO2yZL0iXKd%2F8tk8Q1ifyZdYpGUthLU9gpuCjWB2nlSam8OPzx3BeG7zCNsWq7m7ho31SCnW8KzQnIa9mO%2BnS7FFruBB13TrG2O5cP2092UPSfNv%2F283tO2OsZWQpi7RfM0%2F%2FrfMW7yGi%2Fix6iIrKzWLttFWvkVUWJMVPgRQMfO&X-Amz-Signature=30c448a92e98746eb36db413f797f6665996e54c62360d869a83d9e5bd6282b8&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBQYZNAM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDF7y6pVjv68xA8kylm5vmYi4vMnnB56wL9ndLn33dcwAIgWLTXCxn7h2jHOYZi0%2BIYI%2FiK750zOb004o%2BCMkcJ2Msq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMI0SrpzPNhiSrIL1ircA5XlKjmCRWd6SrBIPn0XioRMovkZmSeRmA7wC7yBgPgPQWqLyQp4dWHU3tt1O3PMZcNU4eKSw5EiTPug%2F5oKrK4KN1ptBg731ZuJf5Do72F%2F5qqO8gJYUCN7dACQf%2BSjWQjg4uSi4hHXBf7Uvl1urzmZjKtVePMl0aEa%2FNn756PrpOl8koO0aKezMvpjiOZP1S9rl62FXJshqmuPypdhNrarGdmT5709tRc%2Be6PsO74rVthJPLJwaefya51BdXA%2BTVznJ2fBZAokEfIicdAxrQ5qaAUe9XHIqCnzNm%2FCALLI%2BDqTDiLCrBYaaBvhf6infMUel3hHEBvOn%2BRpIBKH%2Ft0Y8vNkv0F%2FnUVfiR11wvq36unuWW3oDYBzBizijaMA2j9L6Ah6OkL5JaBNC%2FYTYsPot12Bxf2%2FwyHFQtCI5UsnPCZfEoQWkDKHrfZY8FBb%2FboOxqZvc6W9ZC%2BUvQ0HgUFF62eDxAFinj%2FvmKqTOFKqQ2lqgmaMnQG1Ugji1gKMtpJV5kq%2B5c1gwKw%2F%2FbWR67Y0waGcuqAX7pqZcxlMa8d3dIMoi%2Brq2AjRMn%2BLjordOwELpOSQ1mYYoeVBiV9foNmS701wTqkkTSuzGCzYLwXktr1wvwQmMv%2FPcqivMM7qj70GOqUBSH818wNS86blmwis4X7VOf5h9Y5dUHVQfPIanV6P33Js9LhfJkLNNplRU1pTw%2FsuHrQll1Z4uV3ttUD3ENVafnRXDEmRSRQqdjswIOpJJB1TF%2BugQD6FkWQYsL0EkJye8wrzTgdPqsBdtiGcy5V2TBVDloJeSYVdVXyIpRdhE%2FI1b%2B52kGVuSONfKIeauIXaSyoyRyRMm7v%2FxYHgIy9w3qIVfOng&X-Amz-Signature=b8095a4b1d1899a33fce71fc5358f36db9705bf7593b77bf9bab46a853d909fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=e27f6c9a60cd79666bafaf83c5c47ab5a8a9e36960332d5d34fd1fb28ab111bc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=918724d02f1b0ab05c3c365d9b6e19b8de130c252721865ed8451f6cc54af6f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YDS7UOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGtFUx7hWbA1d9oqAe4nV94U9NEqQIFlj4oqAZ2yYv6GAiEAsE9HYMYPKZxFumZSLOwR0Q5DFy%2BYW9hsx1Do%2BddQsvwq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJv7IoH65k6iuR%2Bn4SrcA%2F6p9%2Bw5RljxX6aVBbE8RBIEZIoaH8ywsvhKjR3p%2BwKkTj%2BF6nrViVRtcQ63hIO5zRO54W2g3cce335aQEEUgkhiBnVuLzRWKCoDSPvdMpQP2WQrPIAbgsptkTEIUZX8BI%2FwytoFPEpvSyxHn%2FoANMDt0cSjSO4n1%2F0uRYf6yrBaoOXyu%2BVRHelMSy2jpWgbSbWobe1LxQpqm1KXM3gRMzijGbhp5ddTm4qzhbrjDng%2BgUY2MyN3pWxiLy1GOCprZ33wDz63cRTuRClmS4g%2FuCc8Ra2I%2F7V8j%2FYiIbE3xPsjB8JIKf5Ds1EJFjYzY%2FK9dW4CMMdTGoaxZNqjSeEyi8YtkuZVFIi%2ByZDBO4USowvriLlyV0hO84kzlj6eaD%2BWK3yrghBBpTdb2v9dMTb%2FYUCl%2FuSyxQZLksW9%2B9YWOQUbJOSz%2FTVtwg42KcG7JKoASTWt7NDMeDyR7nKfxW2aXPx%2FKblUx%2BYwH%2BjKxbBhNUGJ7G2jP8eIVQKe3ppmOXrGTry%2FHi7f7ScqUOb4SVWobNB6I7Mo9zkFGtlhMOUjeuFpz3SAFvcmX2NCJxS4niTp6xReYnKwYTZrUnSL8KlcuruEX1WdJsvdpmYJErKHll9xhuCjZwYkYcO%2F%2FhugMOjqj70GOqUB5tPLvTk0ls5yDkfN%2F9VVE8eJsnK8tWnGq4Qbjwu66qosmBCXU4NobOOaAPFQOsFATAs6nfrVENDiBnwqQMDzHyKfKhcwpqLlU2DFPJX6n6HbiAFsmhQHDdz%2Byu1wBwfTjAoeHFPEvkcwuXuoJeE22PhryG2Yw%2F4oV2iGD1s2C924iUM%2BcyQODL13NJR8USa1PMJ1G6nJS0qNQ69L9iCLHGas2l%2FM&X-Amz-Signature=14f32da25616102eeb718b8d6a2e2f9c50b0e45350f8828a688291bbccba9f22&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWNE7NBX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCnQbnFfAXZFTgTHnjSU6POI35X%2FokRrcJDO1S6Ag3NZwIhAKHJrbRMikCc0h7krTGEQGhfok2mNL1xgIaYUuqSvPr%2FKv8DCFEQABoMNjM3NDIzMTgzODA1IgztMxGuuYYRVTJj9Esq3APQ%2FZdsNn%2FxMeRrWgR3iRpCiYRleuTQDrpAIWT2rKy0CzpifdVEcSL0%2FPh1VFZ7ITsZ52G9cTMbhemHPjHupsKR7X4h0lrYHeoyP0LyMp%2Bqg9TS6tbCQ6gBzXr5Q%2FfIzpo9oT9Ld8EfmcEsbNaDgDZ%2F%2FrYw%2F2MX540kEpAvMgRWIVI73EyvpqR7QdwsqleukEy8LPKxJPfuHbwPc65Edcxtu4MeXf67Y89fsSSsCXRDi7J4OHezss0YcWc6by29sC9%2BAyNOQFwI1AUWl0LTI%2Bj5dgG%2Bmm4Hm%2Fqp4Fnr2MxfuivLGhuLS9FJNG3E%2FbWiwifHIKLhvsPlwg%2FnjnRcEUwcet4%2BC4IvruKClKF4ikM3SU3aGHEZBrEBDEUyNqPjC%2FEOQPQR65iOrV4GQp0HOF%2BGeadJ5Z%2Fl3QIF%2FrOlxYQUBnB9G2c5cPX1baX3w%2BQX8QWSf83N%2Bdi8ewIPpzIyU3Jkv1ipjhdCSetn9bC9B2koB0SiT37p17WHlCLk%2BmqJh%2BpReepswn1AcZ%2FAz0j1uAg6jK3DkaJJjd5MY5iz9%2BnkuY8eTotkAnK8IuL2oaU23Z7wgl8RFiznphxjs8Ujx2kYJZUMVGH0WUxpjpUAnQKDv%2FJlG4OpA6f60nP4zzCU64%2B9BjqkAfFaT3tWnq9%2BYzM5K3zP0akmsoUSS%2Fe5u82dx%2FVs6gWm3o%2FVPsNAs162itSl6x4PZy35EptUHFJp%2FLqf8sIbGm5a524h5GKCdrwz7GHBEFjdmzLX8izG06lnPrOshc1Kj%2FOgpq9DrHcU1%2FZbDpePXefrO8HNQQ50FmoSP8Mxvi2jGYUVW5zrAtt%2BZqgVkzqcxWTZiIICf9Yfoc60DXBYGrLcZoOt&X-Amz-Signature=a4469aefa20452f6fb1c2b9e8372d2d76fc4023e5db870217167ca9b531edec7&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7ZISBG2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDxy0t%2Bg51F8dSZbxqlFyofkkNuKuWL5OJXPmLn6R1i%2BwIgF%2FfqE3L3YKGOuu1w9k%2FhFglgMqxuBzGBNDLVnpEupyoq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDCTcp%2BlhrGpOVuxV1ircAxBrFX58iEFm3ajAJ3zRBeiEukXlkb%2FVZx2mh0kKUaPMxmrFqDRRfYVGcYV6PMmgSiOTqjTbX3Mead6kgdmIUiBtp5wTsieor80umSzSyw4ubUW4yI4RqV7xcbIB7f6zQenxReiromuBMGm2KQ7BvNC%2FK4wBJMdItFMSicWBAnTgfbSqH%2FB2s1GCVKuAfIaJwZNK4N6S%2F6XTD7jH3obcGtF7HUFkAmFZVM3hdWY%2FbIOUP0Tgh4nvZWMmdSth72sRt4X2ZtG5xWL%2F1g8IxmWoeMc1KQP%2FGM%2FsL2QBCJD2AodrDKdyRRYcpbzo8PT5OZpbQwwvLLcZ7l6M%2Feg9HeOpAeogN%2BUf6ViHod0N7XNk9UZT6oiAo5W%2FidG630q1yNuoA4QTPi3IT71MUI3RdXdE83YHt5YYUeS3yK4AEOkG5%2FkopNiyNePJ2%2FjGhE8iPf0XJz5GIq4GscjlX%2BzpaSARDG3NQ1rQlTDMZmJ%2FUkozB1U0FLNRwe2wKJNfNQwN%2FtaxzS%2BYtcDrRdzAZkNjykv%2Fdq8t81w0TpmTpu9tuCS58y2MxyV%2Fpizz0Ik5BFBpQ6kWRCcf%2FGzj%2FwxeKopL%2FlE3NC3Sifpwdn3qXXTb79yGXsSOtCi4A92r9TjLEBLDMITrj70GOqUBnHMQHvkbpKpeea4%2BS5%2FCmZ6VdCbEOzDxhfZ65t0xEVPGmsIZO9xtTk0j7l%2F2ytQzGMiMnyiUPEVTbD%2F1P6Z42iIcw44PgvTU94AZSFSi8T45sEbHsVA%2FaG4MOAc9sYWGR1IkE7wdjfDl647YBUyXwlgm7%2FAaZinYCt8cf553T4ovZhbEe1EInJLylIw0jxJft330DuHizfE2PIsKTEWjqMsB7dz4&X-Amz-Signature=06e4b4e4c4650f6691facbc110a04d2f76f3f69af4777b7aad4d1ed44f050354&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EKI3MXI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAS83wUrJM5WllLyQFpHsPoumoukpMYCPtpuqmzX6KoBAiEA6pk0zyFIFI8yYVOsVJ6VJy257D22dzJ6JKPrljf4JM8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDB8405yWMEhcAQaacSrcA7vvJgZPOe1HfegLEos9hJ9OHyPxMTXRE5PY1%2BR106WesYzoXrcc23rgk1uWKPwkFpi%2BC8OlLixta%2F%2FAAtD7T9mC4ndgT5y9wBo0hZRu5frXQTUzgffkPiCZyGLCkL5V3FDv1Y0dxOyqZ6q6KHYU%2FTjkVOR51Fg1KbAnfXjgrAnR07KyPLzdtwMGJInQkr3hin07MLcu2Mz2xGXpIFq2HhfPFM7Dc5cMpdqKctvyhYK8Jy65hOfT8irKTUkfOi4MKumFbINSZ5vt9m6J%2B0KyspR6LkHnCly%2BMXobMSrhj%2F0ZIdohzYpAYUN5jRp1u8sFrSH68Z8d3CCk39nLguGME7lkTZaGYt01fe5JTxfMPtFJ%2FXWjWr2jSYGiHRpvf%2Fn8Ka%2BrFfrp2yFtWC4v5w11CZWlk8jPdVfoQTvyxl84NADKQ67T8hzKaqClq8fUpPVZgeFVDxFb5vpaxBJ1xV3bApBfcg6KSNx%2Be0vF2F8c26jxTXtCr889OSpn7lWSxnRYOL3LBCWtNsq5LzcVOzU4eZ7aNv3676rsmsgaEWm5oqgwCQWpd%2BHWOQWXnm81QVfHifocEbSQbXdiz6O%2FuLQ2i0c%2BNkMQxCDc9y60lJ9yVtdA%2BffsynwsLwoy1aPPMOjqj70GOqUBH%2FRe2AQmBRMbdSOd8SfBnuGMp71STGXAWedEauZQt7RPr%2FqFOu5WiKUEoHJVX1yEOxk3Wo4Q9oqoZJDyEnjdzlescGS4xFKo0ErOrEqmbpkLwEO8xZ2XG9FyxeX8UcJMF01QrRVNwQzMdGsDzC1qCjqMb3ttBI8XSq5ysZmkbTYfa2jzRdKZEitobIypobLuu1WaMAU4lufDZ3zdMh5BkU7vTtRr&X-Amz-Signature=e2b62200ff3cd169e0212ad5eb8537f632b816a77c0cbc9985f12f14b93d06c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ5253HR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQChD4h7P8HPxFGZq%2BVFm5YYkIvn1%2FH8IQa47%2BS5wIIynwIhAPWy2m6xEhEljaYDushykk5j3wn9PUSK2LtkBXuseaMAKv8DCFEQABoMNjM3NDIzMTgzODA1IgwsJygdSyK4SrbAZUwq3APBRK9ck6lBEkaUnLLanWfDmVvkk%2F3%2Fc%2FI1b3iiaPwYqi%2FQ%2FU%2FBG9p%2BrVs2KRRuSKjuJGgutC7lOunEKjvM3czCQthBUFGWdshi%2FuJiXr17Sxyj1MEEw828xPLnOgQZ%2FJLeFUCSRPqznH29uV4LJns09jlDgR8CKUiZGqFskt7T1dywgBIHu5swl7ooPnmzMXFxzCfRyIYWyTIFl4EhR%2BdBEtYaiENjcyLBEXRHZrqrgkznI7eVJajt7cvQjoADJtCgRC55xrpkPcIpaseI0DoaoxUCF1ytsxVv1MYSpGt1qD1h8jN9oNPxnzmkIb7o2z6FSBEJUV%2BR6kgD8hCpHjEAEpOHghEnT%2Fb1oDOflxZfr7Bm66eFveYaYYP5t2xbu%2BuC8PFo1wwzmcUSYh2vwgc8s%2Bumb1AijW4%2BLou5ZXFmHbHOlb%2B20%2BRC%2F39nLZ4xi81n%2B%2BlhueZdmEsa2ZNxa7FRY%2Bou97tvub8QB%2BqBobFZ5OLE%2FFWf41zSHA9%2BaxN0c3fbLq2OFrThJjTyh5JaTO%2BNwnk3GBF3awvAEvbsDYmEJei8NioGu9KuA6K6iEXtYBih2zVinwJpuMLjds2unIBhc8m1PePbaY%2F2GjaulF9JG8nqcc55xVPeS8AAkDCV64%2B9BjqkAd08hSIW69fHWqKlhw7R%2FAV1YSuN4cQJoHpZ28V8be9gMyxCmm24F0ryvtzxeFAwqrWszDSZTu7mQ%2FYp7mxmZwPphBfjV4GYm1hYF2X6Bs03pEssol7hRn03JToYOmTdQCqi9HQLLWZF%2FD5v6f12MqrJ9qrj3arvqMUZPcU7h69hFivlxcL0rzYAt3sV8Yv%2FYIMkLXOo16BakuKptccjZY4%2BJu6b&X-Amz-Signature=df0919c00ff500b8a285d54ebe1832c22df7778355c1a572763a0a8e8e47190c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ5253HR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQChD4h7P8HPxFGZq%2BVFm5YYkIvn1%2FH8IQa47%2BS5wIIynwIhAPWy2m6xEhEljaYDushykk5j3wn9PUSK2LtkBXuseaMAKv8DCFEQABoMNjM3NDIzMTgzODA1IgwsJygdSyK4SrbAZUwq3APBRK9ck6lBEkaUnLLanWfDmVvkk%2F3%2Fc%2FI1b3iiaPwYqi%2FQ%2FU%2FBG9p%2BrVs2KRRuSKjuJGgutC7lOunEKjvM3czCQthBUFGWdshi%2FuJiXr17Sxyj1MEEw828xPLnOgQZ%2FJLeFUCSRPqznH29uV4LJns09jlDgR8CKUiZGqFskt7T1dywgBIHu5swl7ooPnmzMXFxzCfRyIYWyTIFl4EhR%2BdBEtYaiENjcyLBEXRHZrqrgkznI7eVJajt7cvQjoADJtCgRC55xrpkPcIpaseI0DoaoxUCF1ytsxVv1MYSpGt1qD1h8jN9oNPxnzmkIb7o2z6FSBEJUV%2BR6kgD8hCpHjEAEpOHghEnT%2Fb1oDOflxZfr7Bm66eFveYaYYP5t2xbu%2BuC8PFo1wwzmcUSYh2vwgc8s%2Bumb1AijW4%2BLou5ZXFmHbHOlb%2B20%2BRC%2F39nLZ4xi81n%2B%2BlhueZdmEsa2ZNxa7FRY%2Bou97tvub8QB%2BqBobFZ5OLE%2FFWf41zSHA9%2BaxN0c3fbLq2OFrThJjTyh5JaTO%2BNwnk3GBF3awvAEvbsDYmEJei8NioGu9KuA6K6iEXtYBih2zVinwJpuMLjds2unIBhc8m1PePbaY%2F2GjaulF9JG8nqcc55xVPeS8AAkDCV64%2B9BjqkAd08hSIW69fHWqKlhw7R%2FAV1YSuN4cQJoHpZ28V8be9gMyxCmm24F0ryvtzxeFAwqrWszDSZTu7mQ%2FYp7mxmZwPphBfjV4GYm1hYF2X6Bs03pEssol7hRn03JToYOmTdQCqi9HQLLWZF%2FD5v6f12MqrJ9qrj3arvqMUZPcU7h69hFivlxcL0rzYAt3sV8Yv%2FYIMkLXOo16BakuKptccjZY4%2BJu6b&X-Amz-Signature=ee4805ca067500352896b77074f9c5ad652a55ca67427ee031948060dcce749b&X-Amz-SignedHeaders=host&x-id=GetObject)

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
