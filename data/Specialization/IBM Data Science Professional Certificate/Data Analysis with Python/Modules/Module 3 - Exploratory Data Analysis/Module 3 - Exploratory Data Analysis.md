

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NIBCWNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEAwSKRfOhQXsBIh5KvhHh195tQqzWvyTbNtGKYOPTi3AiEA2m3I%2Fm86Oa4oHGxxRubsDDEmkwG0Cs1m3%2BydAhCszrsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBh5dFjT4Ggz%2Fl2dyrcAy%2FOKANrGpYheLfZfbgDq73Oda3GpNlGar%2BGRQEmVnuQb6wABPsRRnJiTo7IEDJ1bG4aLKa%2FC7yMNojr8CWRCy%2B7PbI8VihQERy4L0lEfRqV3uM%2ByClXHj2ollKkviFzPsc%2FWwum4zanVLuG7%2FwMgxzciG11s4IM57dqROfhXYiK83%2Biz6eGb%2BELZQla0JkaZwDe0UyKjy7OaZlh9neZhipM7JIi7%2F0TTwjWaJKiyPQgEMDDH2FcJBYYCd6ZokKnpBTtMkJ7idlLqPa6hSVltzeNT8JlA1VvRW5JEE1KzUpuqvOjmaki1eDto%2Bo6KILepbakg%2Fy5T8vY%2F5KvQUp%2FTgDoMyEHy2Bm9x4SHUu8TcYui%2FA6jRIThoo3aLFFNY76klNsL%2FzeSIyj6tr9XflWrjZ8GSeEIhG%2F2597p16hg%2FW7RkMZfeiGgTI%2BF5Vv7lnF7CmJ%2BqglzVa6qDBa60NA0y7vWDmg5YKpXNTIQdcA6W7aGdnYKOVIKdZYz6Ftg4MMJBMxY1SJJUtQtnKEHCFUxToGx5%2BOHhGcslbGzoP2Qu60%2F1S6HUQufCDWi0kaLWWisbfnE5V9WELpT0RNcQkbhJwNAR0jHJwjaHrH%2FZPhzBXNT%2BueKDha6Yb5ZfCvMLLe7bwGOqUBSa8zLgrMb23xYep%2Fp9jB0%2B%2B0J3GzQJFb8ciZh8aAjfvBHFvxx6iJhEYZsFRHySr9T7OWMJKlvWeseRmBlDM8DYTP442wlZ9mJ7Cc41yNUmF2MKuR99a7qv9v4nSXiY12WyE4anjSULvCebJ8uiQXzZXk5dcxqqqSK%2BnGIS9ovYqqyQkfVjoBQkUvWpv5wfSFeCy0dXyr6eyFyvVhvrNNrH386Hla&X-Amz-Signature=c1c5d7945b141172ccaa69a543d65477fb4287a654ba068945b0ffaed049c3f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NIBCWNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEAwSKRfOhQXsBIh5KvhHh195tQqzWvyTbNtGKYOPTi3AiEA2m3I%2Fm86Oa4oHGxxRubsDDEmkwG0Cs1m3%2BydAhCszrsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBh5dFjT4Ggz%2Fl2dyrcAy%2FOKANrGpYheLfZfbgDq73Oda3GpNlGar%2BGRQEmVnuQb6wABPsRRnJiTo7IEDJ1bG4aLKa%2FC7yMNojr8CWRCy%2B7PbI8VihQERy4L0lEfRqV3uM%2ByClXHj2ollKkviFzPsc%2FWwum4zanVLuG7%2FwMgxzciG11s4IM57dqROfhXYiK83%2Biz6eGb%2BELZQla0JkaZwDe0UyKjy7OaZlh9neZhipM7JIi7%2F0TTwjWaJKiyPQgEMDDH2FcJBYYCd6ZokKnpBTtMkJ7idlLqPa6hSVltzeNT8JlA1VvRW5JEE1KzUpuqvOjmaki1eDto%2Bo6KILepbakg%2Fy5T8vY%2F5KvQUp%2FTgDoMyEHy2Bm9x4SHUu8TcYui%2FA6jRIThoo3aLFFNY76klNsL%2FzeSIyj6tr9XflWrjZ8GSeEIhG%2F2597p16hg%2FW7RkMZfeiGgTI%2BF5Vv7lnF7CmJ%2BqglzVa6qDBa60NA0y7vWDmg5YKpXNTIQdcA6W7aGdnYKOVIKdZYz6Ftg4MMJBMxY1SJJUtQtnKEHCFUxToGx5%2BOHhGcslbGzoP2Qu60%2F1S6HUQufCDWi0kaLWWisbfnE5V9WELpT0RNcQkbhJwNAR0jHJwjaHrH%2FZPhzBXNT%2BueKDha6Yb5ZfCvMLLe7bwGOqUBSa8zLgrMb23xYep%2Fp9jB0%2B%2B0J3GzQJFb8ciZh8aAjfvBHFvxx6iJhEYZsFRHySr9T7OWMJKlvWeseRmBlDM8DYTP442wlZ9mJ7Cc41yNUmF2MKuR99a7qv9v4nSXiY12WyE4anjSULvCebJ8uiQXzZXk5dcxqqqSK%2BnGIS9ovYqqyQkfVjoBQkUvWpv5wfSFeCy0dXyr6eyFyvVhvrNNrH386Hla&X-Amz-Signature=75a569306ff31c239ce9ba4484a3079e31cf95901947c4585ddd01733ec9bee0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NIBCWNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEAwSKRfOhQXsBIh5KvhHh195tQqzWvyTbNtGKYOPTi3AiEA2m3I%2Fm86Oa4oHGxxRubsDDEmkwG0Cs1m3%2BydAhCszrsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBh5dFjT4Ggz%2Fl2dyrcAy%2FOKANrGpYheLfZfbgDq73Oda3GpNlGar%2BGRQEmVnuQb6wABPsRRnJiTo7IEDJ1bG4aLKa%2FC7yMNojr8CWRCy%2B7PbI8VihQERy4L0lEfRqV3uM%2ByClXHj2ollKkviFzPsc%2FWwum4zanVLuG7%2FwMgxzciG11s4IM57dqROfhXYiK83%2Biz6eGb%2BELZQla0JkaZwDe0UyKjy7OaZlh9neZhipM7JIi7%2F0TTwjWaJKiyPQgEMDDH2FcJBYYCd6ZokKnpBTtMkJ7idlLqPa6hSVltzeNT8JlA1VvRW5JEE1KzUpuqvOjmaki1eDto%2Bo6KILepbakg%2Fy5T8vY%2F5KvQUp%2FTgDoMyEHy2Bm9x4SHUu8TcYui%2FA6jRIThoo3aLFFNY76klNsL%2FzeSIyj6tr9XflWrjZ8GSeEIhG%2F2597p16hg%2FW7RkMZfeiGgTI%2BF5Vv7lnF7CmJ%2BqglzVa6qDBa60NA0y7vWDmg5YKpXNTIQdcA6W7aGdnYKOVIKdZYz6Ftg4MMJBMxY1SJJUtQtnKEHCFUxToGx5%2BOHhGcslbGzoP2Qu60%2F1S6HUQufCDWi0kaLWWisbfnE5V9WELpT0RNcQkbhJwNAR0jHJwjaHrH%2FZPhzBXNT%2BueKDha6Yb5ZfCvMLLe7bwGOqUBSa8zLgrMb23xYep%2Fp9jB0%2B%2B0J3GzQJFb8ciZh8aAjfvBHFvxx6iJhEYZsFRHySr9T7OWMJKlvWeseRmBlDM8DYTP442wlZ9mJ7Cc41yNUmF2MKuR99a7qv9v4nSXiY12WyE4anjSULvCebJ8uiQXzZXk5dcxqqqSK%2BnGIS9ovYqqyQkfVjoBQkUvWpv5wfSFeCy0dXyr6eyFyvVhvrNNrH386Hla&X-Amz-Signature=ff360bf0a5ed2b77bde8d4bae53b715c426c0d59fc4dfaa704c8cbb820db2d96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTZPMDLE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAhd2R84cqARHa%2BXDV5GX6qldpLiy%2FBn2Izh0OynSXLAiBFDWt%2BLhjRVz560DDqxLUrEMOSKmL1o2VqlKN5wFXUEyqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9V9PaFtkHxIYyIFLKtwDK0wroTAhZx2lRrGYDcY4nCsFhVhRgnclrd80kD9Yt%2F339LR42NYzfWBtSAxx6Ts6YJemN3x0%2B4PQEHoX7EshQBpshdlYpi%2BRQS3dgt6gMd1fGJbCPvgRh10ftg%2BWAP%2BHZP99yDCRxNE8aDqK8XIECiTxXuX%2B6%2FjHHVXeqMDdCJLU80%2Fh11x8YuSBxIyj0gqAueg5bJPfRU47rGNAYXtdRcUJ5lTl50KjHl4b0SUzLPdifBStxpuh6zAS6njpcb1Z9XTI0htzi1Rd68pmfgy7QO5hZfh3Kgij6NGyld24nhr%2BG%2BQAC6C6YNFGZMnYhfMiUU8GqsntRRkzuNR3Ss8LJaf7MgZPgLbxi8B4uZWcZBDtgHbjNMbGCmxlIlhUdHqhb3VMEHNe%2FfZEUnhRfAxla9b%2FY6fc6HsZ8Yh3DhmlTg1fsKUlBMishoyhZyy%2Fq%2FqrhAP6h7RlhEoFqFD%2Bi%2F%2FLOQl9GmiNMwAOV0brQtjD5pz%2FG7e9%2Bkf6gRtm%2F1dTP9iD1ghMWbx1%2FKEzG%2FppFzuxjSY3DSjoeKIcO4M7icXa%2F5cAUanaciZSXpAuMyEcTNax17p2LiFBbrcpcVUhFcFKCJOh88BWtxfUXY%2B%2BERVkX%2BlNstv524aq7XoNq2Ywzt7tvAY6pgFk%2B3D%2Fb5qsSlgRFKxhOIH%2Bf65FpY2AsFZDbSBx1P4Bu8EIDCzbZLfICKzmft%2FyRo5GD3oDVqaZRLCT7N4LSMhRJah475qR74hF7tCLtokOaZJFdoT14Hvj4eyv15jcNurJEcv7Xui1eCQUkCzGdvFat%2BnzsMBQPnaetUyt4nxRe8Jnj30AbcUhhN8NA5cm05x3SNc0%2FnYb2rCg%2B5a%2FFwFtzcdQZ4ak&X-Amz-Signature=931d4bf13bc20a6f68c3b81bd086720b4c5fb93345e4bd46d7f43ac0cfcff53f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTZPMDLE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAhd2R84cqARHa%2BXDV5GX6qldpLiy%2FBn2Izh0OynSXLAiBFDWt%2BLhjRVz560DDqxLUrEMOSKmL1o2VqlKN5wFXUEyqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9V9PaFtkHxIYyIFLKtwDK0wroTAhZx2lRrGYDcY4nCsFhVhRgnclrd80kD9Yt%2F339LR42NYzfWBtSAxx6Ts6YJemN3x0%2B4PQEHoX7EshQBpshdlYpi%2BRQS3dgt6gMd1fGJbCPvgRh10ftg%2BWAP%2BHZP99yDCRxNE8aDqK8XIECiTxXuX%2B6%2FjHHVXeqMDdCJLU80%2Fh11x8YuSBxIyj0gqAueg5bJPfRU47rGNAYXtdRcUJ5lTl50KjHl4b0SUzLPdifBStxpuh6zAS6njpcb1Z9XTI0htzi1Rd68pmfgy7QO5hZfh3Kgij6NGyld24nhr%2BG%2BQAC6C6YNFGZMnYhfMiUU8GqsntRRkzuNR3Ss8LJaf7MgZPgLbxi8B4uZWcZBDtgHbjNMbGCmxlIlhUdHqhb3VMEHNe%2FfZEUnhRfAxla9b%2FY6fc6HsZ8Yh3DhmlTg1fsKUlBMishoyhZyy%2Fq%2FqrhAP6h7RlhEoFqFD%2Bi%2F%2FLOQl9GmiNMwAOV0brQtjD5pz%2FG7e9%2Bkf6gRtm%2F1dTP9iD1ghMWbx1%2FKEzG%2FppFzuxjSY3DSjoeKIcO4M7icXa%2F5cAUanaciZSXpAuMyEcTNax17p2LiFBbrcpcVUhFcFKCJOh88BWtxfUXY%2B%2BERVkX%2BlNstv524aq7XoNq2Ywzt7tvAY6pgFk%2B3D%2Fb5qsSlgRFKxhOIH%2Bf65FpY2AsFZDbSBx1P4Bu8EIDCzbZLfICKzmft%2FyRo5GD3oDVqaZRLCT7N4LSMhRJah475qR74hF7tCLtokOaZJFdoT14Hvj4eyv15jcNurJEcv7Xui1eCQUkCzGdvFat%2BnzsMBQPnaetUyt4nxRe8Jnj30AbcUhhN8NA5cm05x3SNc0%2FnYb2rCg%2B5a%2FFwFtzcdQZ4ak&X-Amz-Signature=8e0eea7535f48778ce731362e6ecca000728c372fab0393fc552d278c01a5a63&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTZPMDLE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAhd2R84cqARHa%2BXDV5GX6qldpLiy%2FBn2Izh0OynSXLAiBFDWt%2BLhjRVz560DDqxLUrEMOSKmL1o2VqlKN5wFXUEyqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9V9PaFtkHxIYyIFLKtwDK0wroTAhZx2lRrGYDcY4nCsFhVhRgnclrd80kD9Yt%2F339LR42NYzfWBtSAxx6Ts6YJemN3x0%2B4PQEHoX7EshQBpshdlYpi%2BRQS3dgt6gMd1fGJbCPvgRh10ftg%2BWAP%2BHZP99yDCRxNE8aDqK8XIECiTxXuX%2B6%2FjHHVXeqMDdCJLU80%2Fh11x8YuSBxIyj0gqAueg5bJPfRU47rGNAYXtdRcUJ5lTl50KjHl4b0SUzLPdifBStxpuh6zAS6njpcb1Z9XTI0htzi1Rd68pmfgy7QO5hZfh3Kgij6NGyld24nhr%2BG%2BQAC6C6YNFGZMnYhfMiUU8GqsntRRkzuNR3Ss8LJaf7MgZPgLbxi8B4uZWcZBDtgHbjNMbGCmxlIlhUdHqhb3VMEHNe%2FfZEUnhRfAxla9b%2FY6fc6HsZ8Yh3DhmlTg1fsKUlBMishoyhZyy%2Fq%2FqrhAP6h7RlhEoFqFD%2Bi%2F%2FLOQl9GmiNMwAOV0brQtjD5pz%2FG7e9%2Bkf6gRtm%2F1dTP9iD1ghMWbx1%2FKEzG%2FppFzuxjSY3DSjoeKIcO4M7icXa%2F5cAUanaciZSXpAuMyEcTNax17p2LiFBbrcpcVUhFcFKCJOh88BWtxfUXY%2B%2BERVkX%2BlNstv524aq7XoNq2Ywzt7tvAY6pgFk%2B3D%2Fb5qsSlgRFKxhOIH%2Bf65FpY2AsFZDbSBx1P4Bu8EIDCzbZLfICKzmft%2FyRo5GD3oDVqaZRLCT7N4LSMhRJah475qR74hF7tCLtokOaZJFdoT14Hvj4eyv15jcNurJEcv7Xui1eCQUkCzGdvFat%2BnzsMBQPnaetUyt4nxRe8Jnj30AbcUhhN8NA5cm05x3SNc0%2FnYb2rCg%2B5a%2FFwFtzcdQZ4ak&X-Amz-Signature=f72119773431d16db181674901781a80d8c1065bb3809361fe17d67c83fba566&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTZPMDLE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAhd2R84cqARHa%2BXDV5GX6qldpLiy%2FBn2Izh0OynSXLAiBFDWt%2BLhjRVz560DDqxLUrEMOSKmL1o2VqlKN5wFXUEyqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9V9PaFtkHxIYyIFLKtwDK0wroTAhZx2lRrGYDcY4nCsFhVhRgnclrd80kD9Yt%2F339LR42NYzfWBtSAxx6Ts6YJemN3x0%2B4PQEHoX7EshQBpshdlYpi%2BRQS3dgt6gMd1fGJbCPvgRh10ftg%2BWAP%2BHZP99yDCRxNE8aDqK8XIECiTxXuX%2B6%2FjHHVXeqMDdCJLU80%2Fh11x8YuSBxIyj0gqAueg5bJPfRU47rGNAYXtdRcUJ5lTl50KjHl4b0SUzLPdifBStxpuh6zAS6njpcb1Z9XTI0htzi1Rd68pmfgy7QO5hZfh3Kgij6NGyld24nhr%2BG%2BQAC6C6YNFGZMnYhfMiUU8GqsntRRkzuNR3Ss8LJaf7MgZPgLbxi8B4uZWcZBDtgHbjNMbGCmxlIlhUdHqhb3VMEHNe%2FfZEUnhRfAxla9b%2FY6fc6HsZ8Yh3DhmlTg1fsKUlBMishoyhZyy%2Fq%2FqrhAP6h7RlhEoFqFD%2Bi%2F%2FLOQl9GmiNMwAOV0brQtjD5pz%2FG7e9%2Bkf6gRtm%2F1dTP9iD1ghMWbx1%2FKEzG%2FppFzuxjSY3DSjoeKIcO4M7icXa%2F5cAUanaciZSXpAuMyEcTNax17p2LiFBbrcpcVUhFcFKCJOh88BWtxfUXY%2B%2BERVkX%2BlNstv524aq7XoNq2Ywzt7tvAY6pgFk%2B3D%2Fb5qsSlgRFKxhOIH%2Bf65FpY2AsFZDbSBx1P4Bu8EIDCzbZLfICKzmft%2FyRo5GD3oDVqaZRLCT7N4LSMhRJah475qR74hF7tCLtokOaZJFdoT14Hvj4eyv15jcNurJEcv7Xui1eCQUkCzGdvFat%2BnzsMBQPnaetUyt4nxRe8Jnj30AbcUhhN8NA5cm05x3SNc0%2FnYb2rCg%2B5a%2FFwFtzcdQZ4ak&X-Amz-Signature=e801bd4004526aff39bf3413becb70127d2b1efbb73f276e4b9332aed9d5eee6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTZPMDLE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAhd2R84cqARHa%2BXDV5GX6qldpLiy%2FBn2Izh0OynSXLAiBFDWt%2BLhjRVz560DDqxLUrEMOSKmL1o2VqlKN5wFXUEyqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9V9PaFtkHxIYyIFLKtwDK0wroTAhZx2lRrGYDcY4nCsFhVhRgnclrd80kD9Yt%2F339LR42NYzfWBtSAxx6Ts6YJemN3x0%2B4PQEHoX7EshQBpshdlYpi%2BRQS3dgt6gMd1fGJbCPvgRh10ftg%2BWAP%2BHZP99yDCRxNE8aDqK8XIECiTxXuX%2B6%2FjHHVXeqMDdCJLU80%2Fh11x8YuSBxIyj0gqAueg5bJPfRU47rGNAYXtdRcUJ5lTl50KjHl4b0SUzLPdifBStxpuh6zAS6njpcb1Z9XTI0htzi1Rd68pmfgy7QO5hZfh3Kgij6NGyld24nhr%2BG%2BQAC6C6YNFGZMnYhfMiUU8GqsntRRkzuNR3Ss8LJaf7MgZPgLbxi8B4uZWcZBDtgHbjNMbGCmxlIlhUdHqhb3VMEHNe%2FfZEUnhRfAxla9b%2FY6fc6HsZ8Yh3DhmlTg1fsKUlBMishoyhZyy%2Fq%2FqrhAP6h7RlhEoFqFD%2Bi%2F%2FLOQl9GmiNMwAOV0brQtjD5pz%2FG7e9%2Bkf6gRtm%2F1dTP9iD1ghMWbx1%2FKEzG%2FppFzuxjSY3DSjoeKIcO4M7icXa%2F5cAUanaciZSXpAuMyEcTNax17p2LiFBbrcpcVUhFcFKCJOh88BWtxfUXY%2B%2BERVkX%2BlNstv524aq7XoNq2Ywzt7tvAY6pgFk%2B3D%2Fb5qsSlgRFKxhOIH%2Bf65FpY2AsFZDbSBx1P4Bu8EIDCzbZLfICKzmft%2FyRo5GD3oDVqaZRLCT7N4LSMhRJah475qR74hF7tCLtokOaZJFdoT14Hvj4eyv15jcNurJEcv7Xui1eCQUkCzGdvFat%2BnzsMBQPnaetUyt4nxRe8Jnj30AbcUhhN8NA5cm05x3SNc0%2FnYb2rCg%2B5a%2FFwFtzcdQZ4ak&X-Amz-Signature=461b1590bd77dca7f8738dcd533b821b014f08b5744bbb022fd02d8024e9f1c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTZPMDLE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAhd2R84cqARHa%2BXDV5GX6qldpLiy%2FBn2Izh0OynSXLAiBFDWt%2BLhjRVz560DDqxLUrEMOSKmL1o2VqlKN5wFXUEyqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9V9PaFtkHxIYyIFLKtwDK0wroTAhZx2lRrGYDcY4nCsFhVhRgnclrd80kD9Yt%2F339LR42NYzfWBtSAxx6Ts6YJemN3x0%2B4PQEHoX7EshQBpshdlYpi%2BRQS3dgt6gMd1fGJbCPvgRh10ftg%2BWAP%2BHZP99yDCRxNE8aDqK8XIECiTxXuX%2B6%2FjHHVXeqMDdCJLU80%2Fh11x8YuSBxIyj0gqAueg5bJPfRU47rGNAYXtdRcUJ5lTl50KjHl4b0SUzLPdifBStxpuh6zAS6njpcb1Z9XTI0htzi1Rd68pmfgy7QO5hZfh3Kgij6NGyld24nhr%2BG%2BQAC6C6YNFGZMnYhfMiUU8GqsntRRkzuNR3Ss8LJaf7MgZPgLbxi8B4uZWcZBDtgHbjNMbGCmxlIlhUdHqhb3VMEHNe%2FfZEUnhRfAxla9b%2FY6fc6HsZ8Yh3DhmlTg1fsKUlBMishoyhZyy%2Fq%2FqrhAP6h7RlhEoFqFD%2Bi%2F%2FLOQl9GmiNMwAOV0brQtjD5pz%2FG7e9%2Bkf6gRtm%2F1dTP9iD1ghMWbx1%2FKEzG%2FppFzuxjSY3DSjoeKIcO4M7icXa%2F5cAUanaciZSXpAuMyEcTNax17p2LiFBbrcpcVUhFcFKCJOh88BWtxfUXY%2B%2BERVkX%2BlNstv524aq7XoNq2Ywzt7tvAY6pgFk%2B3D%2Fb5qsSlgRFKxhOIH%2Bf65FpY2AsFZDbSBx1P4Bu8EIDCzbZLfICKzmft%2FyRo5GD3oDVqaZRLCT7N4LSMhRJah475qR74hF7tCLtokOaZJFdoT14Hvj4eyv15jcNurJEcv7Xui1eCQUkCzGdvFat%2BnzsMBQPnaetUyt4nxRe8Jnj30AbcUhhN8NA5cm05x3SNc0%2FnYb2rCg%2B5a%2FFwFtzcdQZ4ak&X-Amz-Signature=c397535fc59aa325c6332ccc7eab197a37f65eebf8d0b0ca0e0c2924e6089ce5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LHOB4H6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmLFi8pC9%2FxA42dTpFC2FMpzqZtpvLU9V6HycBWykaBgIgN47aLxk7mpvCcxGx2mbg6nPdbVXm2Li0XJRhj%2FPtAOoqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEtYmPLNF5o5NjnApCrcA7SPt8YOBZQSxD0caBlPepS0Du880YWEJFN3MyGmJJTUSrIR16kYacXq0Aux%2FhteAMa6rZLktrY1S2%2B0OmOaBnhBsdPRZdYMaTOGuDZZOspYf4BqoOEVn7Y8WOUftLkIaa4jfxomdGy2PLVw7%2F5JtzIGovCH6WAvYLg2hVXDOSpg1oUmu0ReDTR8ti7xl%2F86%2BOqdrQIJ8huWIVeLExWqYJ6bRJ%2FCci5fRveBoHGfVtzRVf%2BA1ZtdCrKO8E77jiG7%2B4DAuTHfQr97j%2FyArL1FFV5ZWp7Cln4n8MplFy1u3V2%2BLBRQY%2Bi%2BRYfIeL%2FOKgkLB2phIAb35uQBM%2BdqYVArCyexEsbkyTjAz5HOXfg7j%2Br9VZhfHTxlmeQngyUYkBwe0MxTLSkJepH1970AosP5ngcRg%2FVykmad3eS0mIBZSwv%2BUEjgIyDgeIqfyV08vykeF0BOKQBOActOgAOrXGLv0a8iszPikhzoJanFVwTDsSWMSOHi3n%2B6U5i2MztnpQYtCzkovApx3aKpFNV8IH7BuPfX21f6EK8v%2BgY4zw%2BoInpDcod5PxGurQxAOLKWO39iTP7UBCetXE426jhFrNtaoIXdEQfCh3HNeEvHLrvoOr4quRF%2FK6GTuYIa9xNHMLje7bwGOqUBVF2B5iTOWRxR3sIquz5DWSjlyMInbG1nv9NjGPI7R70FLn47EACqIuV26miFDLWjx184vsuYUaSpb9eyuxhL4bQL32VwnNv4rGrDbxFSE3Wbf3WNLaZTkkLiCT0Jaf%2BeM80X7W8iDia%2B17IdbsKCOgk7wm2lkl3mvJCDkBiHZViNVL04aEdL9DTUONtxffDEyoOqn1jusU5zTSkVBiRIz%2B5IIBHV&X-Amz-Signature=d34950ebd524232e45f8f0d97b3e1f63e023ed4142326c6b7b56c53831f87c6a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDAJUJ6A%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmwI3%2FcUcPfoygzld%2B49hqBOd9GlG54z3EUTqgoelYWgIhAI4ocixD78yTS18GFYcq%2FuzJqn8RuHs%2BOg0rTyCY6jqPKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvUBEB7AZKyVTfgUUq3AMSRc7uGxo6UL39UmN1ZBBgS5hVsmmvG7sgC7KJqKdsXb69ZEFZx5p08uLQYgbpCxdUc4R1SnIXAvq1g3xiR6xeRws6XPcCz9AxZdnDc1BCis8KFfoNTxCz75vpg4GdQQ8%2BAmtREuZTewZ6JrkJ%2F7KkSMtxpn3Cfv1pfKPGC8iqb7hFwT9%2BIyGriNY5tk0Z80nhMNnWw8KKLs3oy09D6%2BbxE0c4mYDLqjYorGtfZiAAtyIfw9gvDALHwbFD4w%2FfAQJwqjeqADjmRVUu5IvBT4KxPO%2BH1HE3HllVzyaYcbaiFQLPmTPBREiQV0cJkCb6NAINNGtAMs4UYLQOUBGz097xcJM8OC4VPdLjLdn3oXbR9Pw%2FDYf0SgmPIZDip72xQ0zBhNoJwHD1h1Sdvf8XkCuYZkg1TqT2nnWl0uVyThVMCS6QniEiqEqRT%2BIU%2BFHftP%2B5%2BiNwCDLNIV%2FaD0jCQPis%2BaosrxnwxsCB%2FOOtOgVG4kaq7p0RPGfLIsTlQVn5yemoPyQcAWsSyvRIe1clj7BCVAEdR3FPo0kXiFfPPQ6WKWaOpl0TdqzNV6ovShWIGqYre0NBI%2F91H%2B7y9AZ19V%2B5cRS0l6uY2bnMBI57Uw0vIBnvHViiNhmPHYMxLDD03u28BjqkAXmXTeqsHq8VZZ7VBtBhWb8YHxmPTGUB4w8vRRabV0IxQ43aW7F4pGWiB2qtgemt%2BMgfnlCuzJIVUIM3gXKK6SF%2BvfTTtupbqTsyCajqUrC9NYXbvCVJNtA97WHcz%2Bam0eLXfL9bj6OtYmiKo77DQDB2DBAyMCCHNTwIlxsJz5wv4yKQX0iu9XFWqNXUO%2FO9xIXYtLFd7kia6EWeqgLLyhkoJzTb&X-Amz-Signature=4e138bdfab206cedfa2bc51f17d1918d410360478e94d6479085b9625a2c53a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTZPMDLE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAhd2R84cqARHa%2BXDV5GX6qldpLiy%2FBn2Izh0OynSXLAiBFDWt%2BLhjRVz560DDqxLUrEMOSKmL1o2VqlKN5wFXUEyqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9V9PaFtkHxIYyIFLKtwDK0wroTAhZx2lRrGYDcY4nCsFhVhRgnclrd80kD9Yt%2F339LR42NYzfWBtSAxx6Ts6YJemN3x0%2B4PQEHoX7EshQBpshdlYpi%2BRQS3dgt6gMd1fGJbCPvgRh10ftg%2BWAP%2BHZP99yDCRxNE8aDqK8XIECiTxXuX%2B6%2FjHHVXeqMDdCJLU80%2Fh11x8YuSBxIyj0gqAueg5bJPfRU47rGNAYXtdRcUJ5lTl50KjHl4b0SUzLPdifBStxpuh6zAS6njpcb1Z9XTI0htzi1Rd68pmfgy7QO5hZfh3Kgij6NGyld24nhr%2BG%2BQAC6C6YNFGZMnYhfMiUU8GqsntRRkzuNR3Ss8LJaf7MgZPgLbxi8B4uZWcZBDtgHbjNMbGCmxlIlhUdHqhb3VMEHNe%2FfZEUnhRfAxla9b%2FY6fc6HsZ8Yh3DhmlTg1fsKUlBMishoyhZyy%2Fq%2FqrhAP6h7RlhEoFqFD%2Bi%2F%2FLOQl9GmiNMwAOV0brQtjD5pz%2FG7e9%2Bkf6gRtm%2F1dTP9iD1ghMWbx1%2FKEzG%2FppFzuxjSY3DSjoeKIcO4M7icXa%2F5cAUanaciZSXpAuMyEcTNax17p2LiFBbrcpcVUhFcFKCJOh88BWtxfUXY%2B%2BERVkX%2BlNstv524aq7XoNq2Ywzt7tvAY6pgFk%2B3D%2Fb5qsSlgRFKxhOIH%2Bf65FpY2AsFZDbSBx1P4Bu8EIDCzbZLfICKzmft%2FyRo5GD3oDVqaZRLCT7N4LSMhRJah475qR74hF7tCLtokOaZJFdoT14Hvj4eyv15jcNurJEcv7Xui1eCQUkCzGdvFat%2BnzsMBQPnaetUyt4nxRe8Jnj30AbcUhhN8NA5cm05x3SNc0%2FnYb2rCg%2B5a%2FFwFtzcdQZ4ak&X-Amz-Signature=0024717f9c944dbe60a169d8bbd3a768395d5bc0cbbd3d8c5c59bdd8c14560be&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTZPMDLE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAhd2R84cqARHa%2BXDV5GX6qldpLiy%2FBn2Izh0OynSXLAiBFDWt%2BLhjRVz560DDqxLUrEMOSKmL1o2VqlKN5wFXUEyqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9V9PaFtkHxIYyIFLKtwDK0wroTAhZx2lRrGYDcY4nCsFhVhRgnclrd80kD9Yt%2F339LR42NYzfWBtSAxx6Ts6YJemN3x0%2B4PQEHoX7EshQBpshdlYpi%2BRQS3dgt6gMd1fGJbCPvgRh10ftg%2BWAP%2BHZP99yDCRxNE8aDqK8XIECiTxXuX%2B6%2FjHHVXeqMDdCJLU80%2Fh11x8YuSBxIyj0gqAueg5bJPfRU47rGNAYXtdRcUJ5lTl50KjHl4b0SUzLPdifBStxpuh6zAS6njpcb1Z9XTI0htzi1Rd68pmfgy7QO5hZfh3Kgij6NGyld24nhr%2BG%2BQAC6C6YNFGZMnYhfMiUU8GqsntRRkzuNR3Ss8LJaf7MgZPgLbxi8B4uZWcZBDtgHbjNMbGCmxlIlhUdHqhb3VMEHNe%2FfZEUnhRfAxla9b%2FY6fc6HsZ8Yh3DhmlTg1fsKUlBMishoyhZyy%2Fq%2FqrhAP6h7RlhEoFqFD%2Bi%2F%2FLOQl9GmiNMwAOV0brQtjD5pz%2FG7e9%2Bkf6gRtm%2F1dTP9iD1ghMWbx1%2FKEzG%2FppFzuxjSY3DSjoeKIcO4M7icXa%2F5cAUanaciZSXpAuMyEcTNax17p2LiFBbrcpcVUhFcFKCJOh88BWtxfUXY%2B%2BERVkX%2BlNstv524aq7XoNq2Ywzt7tvAY6pgFk%2B3D%2Fb5qsSlgRFKxhOIH%2Bf65FpY2AsFZDbSBx1P4Bu8EIDCzbZLfICKzmft%2FyRo5GD3oDVqaZRLCT7N4LSMhRJah475qR74hF7tCLtokOaZJFdoT14Hvj4eyv15jcNurJEcv7Xui1eCQUkCzGdvFat%2BnzsMBQPnaetUyt4nxRe8Jnj30AbcUhhN8NA5cm05x3SNc0%2FnYb2rCg%2B5a%2FFwFtzcdQZ4ak&X-Amz-Signature=f6279a477cf1ae9b7718b0b7e7436e4438e69579df33213076c0ec9b03c2b69b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTZPMDLE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAhd2R84cqARHa%2BXDV5GX6qldpLiy%2FBn2Izh0OynSXLAiBFDWt%2BLhjRVz560DDqxLUrEMOSKmL1o2VqlKN5wFXUEyqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9V9PaFtkHxIYyIFLKtwDK0wroTAhZx2lRrGYDcY4nCsFhVhRgnclrd80kD9Yt%2F339LR42NYzfWBtSAxx6Ts6YJemN3x0%2B4PQEHoX7EshQBpshdlYpi%2BRQS3dgt6gMd1fGJbCPvgRh10ftg%2BWAP%2BHZP99yDCRxNE8aDqK8XIECiTxXuX%2B6%2FjHHVXeqMDdCJLU80%2Fh11x8YuSBxIyj0gqAueg5bJPfRU47rGNAYXtdRcUJ5lTl50KjHl4b0SUzLPdifBStxpuh6zAS6njpcb1Z9XTI0htzi1Rd68pmfgy7QO5hZfh3Kgij6NGyld24nhr%2BG%2BQAC6C6YNFGZMnYhfMiUU8GqsntRRkzuNR3Ss8LJaf7MgZPgLbxi8B4uZWcZBDtgHbjNMbGCmxlIlhUdHqhb3VMEHNe%2FfZEUnhRfAxla9b%2FY6fc6HsZ8Yh3DhmlTg1fsKUlBMishoyhZyy%2Fq%2FqrhAP6h7RlhEoFqFD%2Bi%2F%2FLOQl9GmiNMwAOV0brQtjD5pz%2FG7e9%2Bkf6gRtm%2F1dTP9iD1ghMWbx1%2FKEzG%2FppFzuxjSY3DSjoeKIcO4M7icXa%2F5cAUanaciZSXpAuMyEcTNax17p2LiFBbrcpcVUhFcFKCJOh88BWtxfUXY%2B%2BERVkX%2BlNstv524aq7XoNq2Ywzt7tvAY6pgFk%2B3D%2Fb5qsSlgRFKxhOIH%2Bf65FpY2AsFZDbSBx1P4Bu8EIDCzbZLfICKzmft%2FyRo5GD3oDVqaZRLCT7N4LSMhRJah475qR74hF7tCLtokOaZJFdoT14Hvj4eyv15jcNurJEcv7Xui1eCQUkCzGdvFat%2BnzsMBQPnaetUyt4nxRe8Jnj30AbcUhhN8NA5cm05x3SNc0%2FnYb2rCg%2B5a%2FFwFtzcdQZ4ak&X-Amz-Signature=30b53d2e300fae37b9a6c9666bf380a1039c7a05ce36bb5d1eeac8f0afad77c2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTADITYK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAHBSHQolUrk9vUqkhUaezvQp7aWHB2T%2Bw%2BYOXqKmDdzAiAsdU%2BlONxCl2wkbXzGa4uSvR6yHtRYNJe2CCOJdvmJlCqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJvJ5NDR1FQTpP%2BS4KtwDHENS%2BkmfpD8YOLkrw%2B%2Fr59J92pffcz7eJupMYzLk3E8rIabY%2F5AnE2dwL9LD9KhOOP5nf16BjUUQ2ql9Rqc2DmIlDRiNWaAscEB6vwZf681yNYk1SWB5bxpWNc7clvsv4u5LOe0EKSZglcxidW%2FwjQbQmn9ZJSt%2FACYys%2FweAfk7NykbdQPSB5wD4QvIJdeYF%2FHSKLYW13aPohVAxDModRXu46WwhG4QCadia56e174Ysa1VRSmbRBnPPAvj0NoNnZM0wL7s4v1%2BMESLBhxPV6PREbWYLQF%2Bri2mYzP5aGhExKgDNnZ4ZHdAsktw8PfniC1J5apj%2FBVHndtAV%2Fr0cZMt8HIHgVGDEZhaLQa4UdDFxSfBUieP%2FWCIilVFAKcI3G6p92yavLOxb4PSyMrK2veaOf5Q%2BcQDMKfYbExsqnu7n91amVMnOL8%2B7FNmyjyPKa7tqDvWmL2hygulp9Qm8Tz9X6wH%2BAS2hjs1nDPfNZGmUI84RyT%2BJ9Gu2Ye3Ix1nBfOf6GJvM3v4iC%2BTWrSUz1YnAQ4Xhin4hgJHqdSX9%2F%2B6Sp83jXFiOLe05i7LzlemlrTl3iVoSRQg5eg0MQ9%2FAw%2F0z832HVvxBJa85WCADboGtON2pAntalTLgXkw3d7tvAY6pgGrP4OBr1IHJIO5J4Nf6KcD6pwSO2jtIY%2BUKqmtccY9HgfPsb0fQIK3u6%2BMstxcNmMU0tUMEqGcNMBqt2hTR6rZpPt34i3QWZQTwtKFyHXvnOAZ5a%2BQh0SSKq1wyVj3tmxIU4G7mjJEWE4qCE%2FTG2I3SOaPcGGwkkM0sQb5Uxe9bHbrcscIO2MqkgMeJ3VynZhbAx9MrAHMCr9DbUFtnmB1qNyYL8va&X-Amz-Signature=bc7de200302ef236cd5d8406fe749effbeaade6b6d713843d69661b719e45d7e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNKXWZ4U%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCSnLKy1KIIQiRcSqqavncfwczMqaLFQGPQvMv2h2WGQIhAIO8%2FWokn6xrD1TAHoOw0ENYwfALDjxjWLEjWuiH53HGKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwl2rpzlBrDzsBXG94q3AMBsihaUodEbK1tdNmYqemZgTz1l4QJWozMBSYp5jSKC4SIXlo13zdM0h%2Bfn1HrYJ9edC96paCHLix0Lluk1refdcExnJui4XBozhdLZ%2FpTVAFHROqtwSineHT69GrvtqHpp5sDXZl0u%2Fnj3Sb%2F4tyomOO1cAWi3sBssbKt1o0S%2FS%2FfYEiE6iUGA%2BxnMONvTfjLojOHm%2F6U7JyLJlVAGap58LCajKS5eJVSu6L9MrjoYD0KsVBbekhN%2FmyKB%2BEqqB9WflT6zLwj0v4eSMhTI%2BT12IIjAlOg35CPXgOQG5NPriIoBoBNajJQU55U7FZiMyAl1NmNOjo7Mv0%2BwKn6EpfhmBpeE9CXKj8Zd06OVGIMpz0eowMLQghpAIzv22%2BMEGWjfyqo09kUDcqGwxA0A6jCx6rmN4V%2B2IPrRYiW%2FFnl%2BbkHTIWt2B7gyjf6KZbORgYDX9NuXyKnxTOE3E1NYu2S7W5ZiFdDfWvCbA%2FulZ7XlJf2R7SRX2QOgGBSUtMqw6SFdwqr%2BbXg9MXVT0DJBU%2Bjnsm3syGqUyHUUw5H%2Bjb%2FCcsqjtjtTPYpJbG0k55WCuPn04hsAQNgA0JSi5gdX0WmthmKnmSgcKQyuluYhNPTqO80w3OW9J73vAGyCDD13u28BjqkAXpbVQCbFtHi9oWbrWQWq7%2FaaMspZ7QxHkIg64S4NlfyeIN2dOYrG4nAJt0YskXSkYYlyS7SkTp2zKZDXFKTUznuRY6hGiP82EPJ%2Bg1N0gMXF0sbuEv4lrmPV2KNXWJBriZWwcI%2Baa7f8Ct1wGmPbh8C%2BrSEX%2F%2FWIxwO5A3sE8%2FCETQvbz9mU87HfIHlDpcrq0Z6ihGaxI5inKTOoIqkvGW2Ba9Z&X-Amz-Signature=c1ae395106073a074ff9699b688cf85a5a196c5542d445a4282e292595b6d66c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQZVXVUI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCebxN1%2BcpckaGtqCHUJexDe0h%2FbQgSEU5iuRHGoSJE%2FgIgU4tiSeBmLqDqpOUVZVOPfTx4HKrU8aTpq7gJ4Qb21rMqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNwOSAOOdZ%2BCXfjKZircA9o7l8ykzYxmEXNb%2FOHpTCMhZLgcW97HJpQfWWH8Wvngzugy5J3rVerFmwH8ZjUu4tqeIGf6mP54PZQEqNmRmOVdEj9yNldNCo4vEPDk5gdDJ7T0ju3SfoWY%2BCiYmAk6TdaZwcdb6xY%2FCd6os3IvGq6f%2BhhenVgxn9LufcbedzacQ1C13AbCA5CCb0U4wo%2F44C%2FHi2EwMa0mYrkCjGZ7xkyukOVwWNOYw%2BwZpn3orcE3a10%2FjBQoHA0jQawvsIYypkePO1C1YPrfoQOKmHmCu7CIdd09RXqT7lCm5R0sEDywS301N%2F2vlQBY4PkGUow7tLIUqRqVDjrBkkKLSL67tU5cO2YELRwUOL1UeeQVQpD87uUHyuPjyY9juIp6DL0B0zo3tJb3mWX1BrO3VGH6GCf4FxpaJxC9Z9e%2BBSLgfyx6f5axTTuPenxs4mZ%2BNnhCAFOGHuvoHgrYXLCF3wEx5xFRwpJr16NxhFzH6jtkZFzrba9%2FaIAnfalWzZfVZX6IYhueeIWLuVfULHLb10B0pNVgj2Pu9%2Bs1htikrpSywRtS8o5rvvV9Fe2LA2tqMjqE642O3FWzrX5X5G4dIj%2FKE0E7yWv5rYzpB%2Fn4Wf4WGDIjwqzICcUINR6yJTZhMLje7bwGOqUB0IiuzCjo3%2BiUq5sWir39%2F2rehEItrlqpKJbcGLY%2Bz9O6iReLYdvrDB3OpE36x%2Fr024IdIJDScPmxDhfzX0EHTxgOhfiVL8%2BS9LO5RTrgHOl5N2UGTiGuebNJgEqRlzQ9PUdrdW1pTblbTbCiAyuq3zQBw0TWGYvjW%2F8dbZFcjAtWE72uJQ0NsEgQPSc%2Bp7UYVYZcwG9nRVtQaob3tiY%2FlqeskIew&X-Amz-Signature=b22c83242dfdd5565224d15b8f3e1bb5f5424ed3c3fb1b0c49a7728e19a0a2f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSAUQHCX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPdaPmT%2B8t6za9Qu1ssxDJV4BP6heu5D843h3AMeDxiAiEA9IW4FcVWk2sAgAZAuE%2BlvskUhUDesH08YKiQEbRhe0EqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI0PK4Hbs0lrmLNv%2BircA%2BZjgfmaz%2BP7pklfful692e4ggNeke8%2F5GRXzu34vwkJtsbUMfxbGb2k%2BdAg4K3GEcW3giJuhSYi%2BNip8JUhXn1Og0zOQEwlvW3%2FYTZX34cPvcRXMtBxu95kjt0h4bSDflsx0sF9iKg4xvLu6FXJrRHIUfvk3E2bEuKVggwuFTrdqHNXzxzsgMUjq95ADsUdjGS4nFrmmZ17Xwdn%2Fq8jMSvi%2BPEPuT6ys6LObn32oG%2FxhN1hZtsBmnDBS5oRVrsvNd%2BaRyEpmTUhDwV03UwWzn8gej4hq0P67NkpBLwiGy%2BXchRE8uUYGnKr09%2BN0YjSyd%2Blc1KC%2FMFQUN2RZtvSKqTkzi%2FKKFHDssKJB7axrB0m%2FtQXrqaA6G8ipffAagOaCBAyXWWcgQ9QA3YhzRcP69ezovIDZxNl3ndhnelij3c2Q9N4UnITlAEwZ0nAUuacPlAX6t3Q3WPyON6hqYfKEOnSTRe%2FTavjg036583d50lxv%2FiH%2F9yjJoiiXkbUZxx9%2BPInLGCObfUDeoqxg2Rb7oIOJ0NN5hmnwsOugAJiEdsAHlz6fw%2FAebvBqJGBAT2LVutrQSe1XRYV5V6Fo96hrIvP2CEqIJSTfCmcSk0QIA6b7lTFcaezBCP9bI57MI7f7bwGOqUBUSgATJB2Q7xouYHcFqXVck%2B0satkWFvJbVCHel0MOcKfiyOiXeBSIXczGGiXk0uW2QHm1XxWt3FRqu6U%2Bglg%2BeLvI1NBxFv3JL7xS%2BvpTzZ41ZvZHwvRiqvC1ESL1hAhENvg1PALWHiAibdMGdbUt%2BV4SMKBkvrR%2BhZ0oacJajtbNbVUShwUgtELJNbbYbcBTfzoS3%2BgUOROI%2BMm%2FrU%2FHH4yLfvQ&X-Amz-Signature=13a32278b10c9948262f0150d7c596fff4e222df0e1fde45d04978a66e054dd6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSAUQHCX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPdaPmT%2B8t6za9Qu1ssxDJV4BP6heu5D843h3AMeDxiAiEA9IW4FcVWk2sAgAZAuE%2BlvskUhUDesH08YKiQEbRhe0EqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI0PK4Hbs0lrmLNv%2BircA%2BZjgfmaz%2BP7pklfful692e4ggNeke8%2F5GRXzu34vwkJtsbUMfxbGb2k%2BdAg4K3GEcW3giJuhSYi%2BNip8JUhXn1Og0zOQEwlvW3%2FYTZX34cPvcRXMtBxu95kjt0h4bSDflsx0sF9iKg4xvLu6FXJrRHIUfvk3E2bEuKVggwuFTrdqHNXzxzsgMUjq95ADsUdjGS4nFrmmZ17Xwdn%2Fq8jMSvi%2BPEPuT6ys6LObn32oG%2FxhN1hZtsBmnDBS5oRVrsvNd%2BaRyEpmTUhDwV03UwWzn8gej4hq0P67NkpBLwiGy%2BXchRE8uUYGnKr09%2BN0YjSyd%2Blc1KC%2FMFQUN2RZtvSKqTkzi%2FKKFHDssKJB7axrB0m%2FtQXrqaA6G8ipffAagOaCBAyXWWcgQ9QA3YhzRcP69ezovIDZxNl3ndhnelij3c2Q9N4UnITlAEwZ0nAUuacPlAX6t3Q3WPyON6hqYfKEOnSTRe%2FTavjg036583d50lxv%2FiH%2F9yjJoiiXkbUZxx9%2BPInLGCObfUDeoqxg2Rb7oIOJ0NN5hmnwsOugAJiEdsAHlz6fw%2FAebvBqJGBAT2LVutrQSe1XRYV5V6Fo96hrIvP2CEqIJSTfCmcSk0QIA6b7lTFcaezBCP9bI57MI7f7bwGOqUBUSgATJB2Q7xouYHcFqXVck%2B0satkWFvJbVCHel0MOcKfiyOiXeBSIXczGGiXk0uW2QHm1XxWt3FRqu6U%2Bglg%2BeLvI1NBxFv3JL7xS%2BvpTzZ41ZvZHwvRiqvC1ESL1hAhENvg1PALWHiAibdMGdbUt%2BV4SMKBkvrR%2BhZ0oacJajtbNbVUShwUgtELJNbbYbcBTfzoS3%2BgUOROI%2BMm%2FrU%2FHH4yLfvQ&X-Amz-Signature=5b059b1f78faaf9af6d037da133478d7e771bf8970bf790f6dc15d8cc0155aad&X-Amz-SignedHeaders=host&x-id=GetObject)

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
