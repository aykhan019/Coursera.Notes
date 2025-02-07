

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5R7BNZO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD3Y217KbCMCekAOq4EgibIp4kF57XaxZJM1zMuKAFqngIgOjYfJWAagV9qkqAVQ5P6TwOXy5fmyu8k9HXqDKhYRPkq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDLUu%2FwiThCkFVPVNsircA8RBm%2FIqDTGFyaENIRmNWDoF3Z%2BsTfaVOZzRSTAymGvO8Xfd%2Fag%2BQ06XbUqQaeWZRLWLwjwWLwJRwdbMrHuZFnJLzm%2B6ZSYBnKBcyzFuTws56wMazvLWX%2FaEYi5k21h4fIsUPqhAcljrByPkIJ%2B1lCaKz4lqu8PGHCWzG6oLjU2GL2ndgbeQlyZGqvQuM7BLPHV9DVYbrahvr4zeC2STvBfftyXheJLVPm8f8bJ%2FQm%2FhBh2O3ALwT1njCSOh2Ig4IsjOU299r3KRiLEOqRdC9J%2BuLM%2FgshpOBBLRiu2hPyVfqmdOBWvhN4sAvDUOt2yQCxfYvNMNhHawXGI5aOUl5SdgOaeqPPCtun%2FH%2B%2FFDv%2BwNZne%2FqM9QBR0YVLW6iUdvRcBg8UEaeidWxAyqKCXEA4pxhTQ7McJ1FEVr%2FZTCsJjr8YAUNV6QwzlBkO6On%2FaCZaj61pSgesbyxoe27RWVLfPzUZxokzoMjSxZRGCOnDiwguYq%2F4STdlJcVVB3ELvqEzdNYs5vR7IZn02VoWT%2B41YeJyMJYtW6BUw3eJZ5ZyhTcqGpoS1BxVDM%2BaHJ8jjBaWihWDiba%2F%2Fb0xAfzIHiFZE4wAXqisMGKX6nOJRfR4u2UIIpXzOKAsSQra03MLOalb0GOqUBPxKvVVkaQKTIEdwyhzw%2BZkahr2VFSFKMhPxcRi9hjpnlfnT8aUySROqSbC97JxLThEHFm5fp7lHdRAUgUlEJ8FSfO8TD%2BxJP78z7OMEacZXY7wjWFhJdCw5DdgUToIOxcYijGdt4m%2B46gLO%2FTURO%2Bj0buM3fVR6dUtwLKA1am%2BXL%2FAe%2Bd6dPW03BWGyA4UZJBfDXV7uM5OcTSVnqF4uktyarxU2o&X-Amz-Signature=2c7172bc9e8b6f8a441627d882d217b6b141f1d8b83612dd91e1bb2a23f64298&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5R7BNZO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD3Y217KbCMCekAOq4EgibIp4kF57XaxZJM1zMuKAFqngIgOjYfJWAagV9qkqAVQ5P6TwOXy5fmyu8k9HXqDKhYRPkq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDLUu%2FwiThCkFVPVNsircA8RBm%2FIqDTGFyaENIRmNWDoF3Z%2BsTfaVOZzRSTAymGvO8Xfd%2Fag%2BQ06XbUqQaeWZRLWLwjwWLwJRwdbMrHuZFnJLzm%2B6ZSYBnKBcyzFuTws56wMazvLWX%2FaEYi5k21h4fIsUPqhAcljrByPkIJ%2B1lCaKz4lqu8PGHCWzG6oLjU2GL2ndgbeQlyZGqvQuM7BLPHV9DVYbrahvr4zeC2STvBfftyXheJLVPm8f8bJ%2FQm%2FhBh2O3ALwT1njCSOh2Ig4IsjOU299r3KRiLEOqRdC9J%2BuLM%2FgshpOBBLRiu2hPyVfqmdOBWvhN4sAvDUOt2yQCxfYvNMNhHawXGI5aOUl5SdgOaeqPPCtun%2FH%2B%2FFDv%2BwNZne%2FqM9QBR0YVLW6iUdvRcBg8UEaeidWxAyqKCXEA4pxhTQ7McJ1FEVr%2FZTCsJjr8YAUNV6QwzlBkO6On%2FaCZaj61pSgesbyxoe27RWVLfPzUZxokzoMjSxZRGCOnDiwguYq%2F4STdlJcVVB3ELvqEzdNYs5vR7IZn02VoWT%2B41YeJyMJYtW6BUw3eJZ5ZyhTcqGpoS1BxVDM%2BaHJ8jjBaWihWDiba%2F%2Fb0xAfzIHiFZE4wAXqisMGKX6nOJRfR4u2UIIpXzOKAsSQra03MLOalb0GOqUBPxKvVVkaQKTIEdwyhzw%2BZkahr2VFSFKMhPxcRi9hjpnlfnT8aUySROqSbC97JxLThEHFm5fp7lHdRAUgUlEJ8FSfO8TD%2BxJP78z7OMEacZXY7wjWFhJdCw5DdgUToIOxcYijGdt4m%2B46gLO%2FTURO%2Bj0buM3fVR6dUtwLKA1am%2BXL%2FAe%2Bd6dPW03BWGyA4UZJBfDXV7uM5OcTSVnqF4uktyarxU2o&X-Amz-Signature=100e30b092e4a0bc8b21fcd48d3357fb7cdd34fd5124b715bd689938f492af00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5R7BNZO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD3Y217KbCMCekAOq4EgibIp4kF57XaxZJM1zMuKAFqngIgOjYfJWAagV9qkqAVQ5P6TwOXy5fmyu8k9HXqDKhYRPkq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDLUu%2FwiThCkFVPVNsircA8RBm%2FIqDTGFyaENIRmNWDoF3Z%2BsTfaVOZzRSTAymGvO8Xfd%2Fag%2BQ06XbUqQaeWZRLWLwjwWLwJRwdbMrHuZFnJLzm%2B6ZSYBnKBcyzFuTws56wMazvLWX%2FaEYi5k21h4fIsUPqhAcljrByPkIJ%2B1lCaKz4lqu8PGHCWzG6oLjU2GL2ndgbeQlyZGqvQuM7BLPHV9DVYbrahvr4zeC2STvBfftyXheJLVPm8f8bJ%2FQm%2FhBh2O3ALwT1njCSOh2Ig4IsjOU299r3KRiLEOqRdC9J%2BuLM%2FgshpOBBLRiu2hPyVfqmdOBWvhN4sAvDUOt2yQCxfYvNMNhHawXGI5aOUl5SdgOaeqPPCtun%2FH%2B%2FFDv%2BwNZne%2FqM9QBR0YVLW6iUdvRcBg8UEaeidWxAyqKCXEA4pxhTQ7McJ1FEVr%2FZTCsJjr8YAUNV6QwzlBkO6On%2FaCZaj61pSgesbyxoe27RWVLfPzUZxokzoMjSxZRGCOnDiwguYq%2F4STdlJcVVB3ELvqEzdNYs5vR7IZn02VoWT%2B41YeJyMJYtW6BUw3eJZ5ZyhTcqGpoS1BxVDM%2BaHJ8jjBaWihWDiba%2F%2Fb0xAfzIHiFZE4wAXqisMGKX6nOJRfR4u2UIIpXzOKAsSQra03MLOalb0GOqUBPxKvVVkaQKTIEdwyhzw%2BZkahr2VFSFKMhPxcRi9hjpnlfnT8aUySROqSbC97JxLThEHFm5fp7lHdRAUgUlEJ8FSfO8TD%2BxJP78z7OMEacZXY7wjWFhJdCw5DdgUToIOxcYijGdt4m%2B46gLO%2FTURO%2Bj0buM3fVR6dUtwLKA1am%2BXL%2FAe%2Bd6dPW03BWGyA4UZJBfDXV7uM5OcTSVnqF4uktyarxU2o&X-Amz-Signature=aaa56f3bb15a84ec9f8002f5c5d77a8d17b16ee0064538917874037f0c61fcf3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUNY7TA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDlFuRJTan8bKCvS08%2FgL%2BH8ilj6Frk9NRwTD4QOVZCuQIhANpfiGYqcdJgQRpxasIfSwTOkJ7iOhPS%2B3RtlzKlueqnKv8DCGkQABoMNjM3NDIzMTgzODA1IgyYI6JrrivDxDc9AZ0q3ANAMK%2FI05V%2Bxxe5DgLqCWTnRpPBoMR9CZ6UJzF7FdZtNE0LEPAVYr2SFF%2Bvja9IbEA%2BW%2F5JK00OBMg0E3oaepY5ACRgqcEo4bvZON3vnQebUSmo5TO73CRBFb8ZFOOEqllejsGOTdp7AvnSjIiNToRg5P5xcvl73w0vewB6sCpCDBukn%2FkiQruQQb0jDhSXZVdQENa%2F%2BCk2DUd0RLoMlrAEZAMimuCXqWg411VGufL8NlVpX%2BMkC4BwQwASxEnuDNIBAf1em7YmpSksyT%2BJNMBPjQZ1NPPnKtkpFYNCpKmWCccZTi2LseEomaPevcCgRaOpihLLK5lzI569QynXHmhkRuw4bqDOtnOfo8iNs5LzuuJ6qlcUpeMJxwAedQ%2B%2F77XE%2FWJddMPF8MRCvjYn0RL47YCptbroJbnnoIa3b4J4rEhEMiSUhkiK%2Bob7AT0KPRWDnVmR1j7cA3uQO%2Bcimyu3PYMlvFuAJcen18AL463iOHSlbg%2Bt4sKwXST88Dwtahkc6ZtVsa2%2FifvGu0oCCbuDAy3mUCMKy0q2WbgUv6B3PvjAOE69OitZWmG7bJ8WJcLXBJfaTkqlWjPbqLRqOgJ6ST8Ge6CQAwzowwvYohU%2BeFyPfR8FQkwBQXbD8jDumZW9BjqkAcX483wt1T56Nfqonk5rkrFCD7uvAMQ7H4ss8c%2BJNZ9gFgQYwoQ4dKf9Djl%2F6zr06RjGdfyf5mUOsspYgT6iYP3zaCLwiCVGPzLGWI4V3MaxT7GSfs%2BhoL2YelXlmphVzMAX6RKy8v%2BsIgGo8S9DydwsV6bEa%2B9zl9VglXk2Moe4BrWlTEGu1d%2FKYFh06BSWq%2FvZXB6AerNKiCej8BTNtqHR9wkC&X-Amz-Signature=f8d784d8bef568210d87192e7dbc6f3ef3c2d616953718d9626ef03007d57d53&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUNY7TA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDlFuRJTan8bKCvS08%2FgL%2BH8ilj6Frk9NRwTD4QOVZCuQIhANpfiGYqcdJgQRpxasIfSwTOkJ7iOhPS%2B3RtlzKlueqnKv8DCGkQABoMNjM3NDIzMTgzODA1IgyYI6JrrivDxDc9AZ0q3ANAMK%2FI05V%2Bxxe5DgLqCWTnRpPBoMR9CZ6UJzF7FdZtNE0LEPAVYr2SFF%2Bvja9IbEA%2BW%2F5JK00OBMg0E3oaepY5ACRgqcEo4bvZON3vnQebUSmo5TO73CRBFb8ZFOOEqllejsGOTdp7AvnSjIiNToRg5P5xcvl73w0vewB6sCpCDBukn%2FkiQruQQb0jDhSXZVdQENa%2F%2BCk2DUd0RLoMlrAEZAMimuCXqWg411VGufL8NlVpX%2BMkC4BwQwASxEnuDNIBAf1em7YmpSksyT%2BJNMBPjQZ1NPPnKtkpFYNCpKmWCccZTi2LseEomaPevcCgRaOpihLLK5lzI569QynXHmhkRuw4bqDOtnOfo8iNs5LzuuJ6qlcUpeMJxwAedQ%2B%2F77XE%2FWJddMPF8MRCvjYn0RL47YCptbroJbnnoIa3b4J4rEhEMiSUhkiK%2Bob7AT0KPRWDnVmR1j7cA3uQO%2Bcimyu3PYMlvFuAJcen18AL463iOHSlbg%2Bt4sKwXST88Dwtahkc6ZtVsa2%2FifvGu0oCCbuDAy3mUCMKy0q2WbgUv6B3PvjAOE69OitZWmG7bJ8WJcLXBJfaTkqlWjPbqLRqOgJ6ST8Ge6CQAwzowwvYohU%2BeFyPfR8FQkwBQXbD8jDumZW9BjqkAcX483wt1T56Nfqonk5rkrFCD7uvAMQ7H4ss8c%2BJNZ9gFgQYwoQ4dKf9Djl%2F6zr06RjGdfyf5mUOsspYgT6iYP3zaCLwiCVGPzLGWI4V3MaxT7GSfs%2BhoL2YelXlmphVzMAX6RKy8v%2BsIgGo8S9DydwsV6bEa%2B9zl9VglXk2Moe4BrWlTEGu1d%2FKYFh06BSWq%2FvZXB6AerNKiCej8BTNtqHR9wkC&X-Amz-Signature=f4bd5d158e907168d66962043deec5387b07c47cb4d234bb73b4369211b44966&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUNY7TA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDlFuRJTan8bKCvS08%2FgL%2BH8ilj6Frk9NRwTD4QOVZCuQIhANpfiGYqcdJgQRpxasIfSwTOkJ7iOhPS%2B3RtlzKlueqnKv8DCGkQABoMNjM3NDIzMTgzODA1IgyYI6JrrivDxDc9AZ0q3ANAMK%2FI05V%2Bxxe5DgLqCWTnRpPBoMR9CZ6UJzF7FdZtNE0LEPAVYr2SFF%2Bvja9IbEA%2BW%2F5JK00OBMg0E3oaepY5ACRgqcEo4bvZON3vnQebUSmo5TO73CRBFb8ZFOOEqllejsGOTdp7AvnSjIiNToRg5P5xcvl73w0vewB6sCpCDBukn%2FkiQruQQb0jDhSXZVdQENa%2F%2BCk2DUd0RLoMlrAEZAMimuCXqWg411VGufL8NlVpX%2BMkC4BwQwASxEnuDNIBAf1em7YmpSksyT%2BJNMBPjQZ1NPPnKtkpFYNCpKmWCccZTi2LseEomaPevcCgRaOpihLLK5lzI569QynXHmhkRuw4bqDOtnOfo8iNs5LzuuJ6qlcUpeMJxwAedQ%2B%2F77XE%2FWJddMPF8MRCvjYn0RL47YCptbroJbnnoIa3b4J4rEhEMiSUhkiK%2Bob7AT0KPRWDnVmR1j7cA3uQO%2Bcimyu3PYMlvFuAJcen18AL463iOHSlbg%2Bt4sKwXST88Dwtahkc6ZtVsa2%2FifvGu0oCCbuDAy3mUCMKy0q2WbgUv6B3PvjAOE69OitZWmG7bJ8WJcLXBJfaTkqlWjPbqLRqOgJ6ST8Ge6CQAwzowwvYohU%2BeFyPfR8FQkwBQXbD8jDumZW9BjqkAcX483wt1T56Nfqonk5rkrFCD7uvAMQ7H4ss8c%2BJNZ9gFgQYwoQ4dKf9Djl%2F6zr06RjGdfyf5mUOsspYgT6iYP3zaCLwiCVGPzLGWI4V3MaxT7GSfs%2BhoL2YelXlmphVzMAX6RKy8v%2BsIgGo8S9DydwsV6bEa%2B9zl9VglXk2Moe4BrWlTEGu1d%2FKYFh06BSWq%2FvZXB6AerNKiCej8BTNtqHR9wkC&X-Amz-Signature=f8f6fa3c3d24d0569bfe108038df41e38647c81258dd4b3d7f4f4273ba242cf3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUNY7TA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDlFuRJTan8bKCvS08%2FgL%2BH8ilj6Frk9NRwTD4QOVZCuQIhANpfiGYqcdJgQRpxasIfSwTOkJ7iOhPS%2B3RtlzKlueqnKv8DCGkQABoMNjM3NDIzMTgzODA1IgyYI6JrrivDxDc9AZ0q3ANAMK%2FI05V%2Bxxe5DgLqCWTnRpPBoMR9CZ6UJzF7FdZtNE0LEPAVYr2SFF%2Bvja9IbEA%2BW%2F5JK00OBMg0E3oaepY5ACRgqcEo4bvZON3vnQebUSmo5TO73CRBFb8ZFOOEqllejsGOTdp7AvnSjIiNToRg5P5xcvl73w0vewB6sCpCDBukn%2FkiQruQQb0jDhSXZVdQENa%2F%2BCk2DUd0RLoMlrAEZAMimuCXqWg411VGufL8NlVpX%2BMkC4BwQwASxEnuDNIBAf1em7YmpSksyT%2BJNMBPjQZ1NPPnKtkpFYNCpKmWCccZTi2LseEomaPevcCgRaOpihLLK5lzI569QynXHmhkRuw4bqDOtnOfo8iNs5LzuuJ6qlcUpeMJxwAedQ%2B%2F77XE%2FWJddMPF8MRCvjYn0RL47YCptbroJbnnoIa3b4J4rEhEMiSUhkiK%2Bob7AT0KPRWDnVmR1j7cA3uQO%2Bcimyu3PYMlvFuAJcen18AL463iOHSlbg%2Bt4sKwXST88Dwtahkc6ZtVsa2%2FifvGu0oCCbuDAy3mUCMKy0q2WbgUv6B3PvjAOE69OitZWmG7bJ8WJcLXBJfaTkqlWjPbqLRqOgJ6ST8Ge6CQAwzowwvYohU%2BeFyPfR8FQkwBQXbD8jDumZW9BjqkAcX483wt1T56Nfqonk5rkrFCD7uvAMQ7H4ss8c%2BJNZ9gFgQYwoQ4dKf9Djl%2F6zr06RjGdfyf5mUOsspYgT6iYP3zaCLwiCVGPzLGWI4V3MaxT7GSfs%2BhoL2YelXlmphVzMAX6RKy8v%2BsIgGo8S9DydwsV6bEa%2B9zl9VglXk2Moe4BrWlTEGu1d%2FKYFh06BSWq%2FvZXB6AerNKiCej8BTNtqHR9wkC&X-Amz-Signature=942dcd2a84147fafa61464eeeead56638295237c61fbeaf62bc29d8903e812a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUNY7TA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDlFuRJTan8bKCvS08%2FgL%2BH8ilj6Frk9NRwTD4QOVZCuQIhANpfiGYqcdJgQRpxasIfSwTOkJ7iOhPS%2B3RtlzKlueqnKv8DCGkQABoMNjM3NDIzMTgzODA1IgyYI6JrrivDxDc9AZ0q3ANAMK%2FI05V%2Bxxe5DgLqCWTnRpPBoMR9CZ6UJzF7FdZtNE0LEPAVYr2SFF%2Bvja9IbEA%2BW%2F5JK00OBMg0E3oaepY5ACRgqcEo4bvZON3vnQebUSmo5TO73CRBFb8ZFOOEqllejsGOTdp7AvnSjIiNToRg5P5xcvl73w0vewB6sCpCDBukn%2FkiQruQQb0jDhSXZVdQENa%2F%2BCk2DUd0RLoMlrAEZAMimuCXqWg411VGufL8NlVpX%2BMkC4BwQwASxEnuDNIBAf1em7YmpSksyT%2BJNMBPjQZ1NPPnKtkpFYNCpKmWCccZTi2LseEomaPevcCgRaOpihLLK5lzI569QynXHmhkRuw4bqDOtnOfo8iNs5LzuuJ6qlcUpeMJxwAedQ%2B%2F77XE%2FWJddMPF8MRCvjYn0RL47YCptbroJbnnoIa3b4J4rEhEMiSUhkiK%2Bob7AT0KPRWDnVmR1j7cA3uQO%2Bcimyu3PYMlvFuAJcen18AL463iOHSlbg%2Bt4sKwXST88Dwtahkc6ZtVsa2%2FifvGu0oCCbuDAy3mUCMKy0q2WbgUv6B3PvjAOE69OitZWmG7bJ8WJcLXBJfaTkqlWjPbqLRqOgJ6ST8Ge6CQAwzowwvYohU%2BeFyPfR8FQkwBQXbD8jDumZW9BjqkAcX483wt1T56Nfqonk5rkrFCD7uvAMQ7H4ss8c%2BJNZ9gFgQYwoQ4dKf9Djl%2F6zr06RjGdfyf5mUOsspYgT6iYP3zaCLwiCVGPzLGWI4V3MaxT7GSfs%2BhoL2YelXlmphVzMAX6RKy8v%2BsIgGo8S9DydwsV6bEa%2B9zl9VglXk2Moe4BrWlTEGu1d%2FKYFh06BSWq%2FvZXB6AerNKiCej8BTNtqHR9wkC&X-Amz-Signature=89d217071354372b7049dc7985d160bafca7c817eefdc4713f53000fec0aa0a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUNY7TA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDlFuRJTan8bKCvS08%2FgL%2BH8ilj6Frk9NRwTD4QOVZCuQIhANpfiGYqcdJgQRpxasIfSwTOkJ7iOhPS%2B3RtlzKlueqnKv8DCGkQABoMNjM3NDIzMTgzODA1IgyYI6JrrivDxDc9AZ0q3ANAMK%2FI05V%2Bxxe5DgLqCWTnRpPBoMR9CZ6UJzF7FdZtNE0LEPAVYr2SFF%2Bvja9IbEA%2BW%2F5JK00OBMg0E3oaepY5ACRgqcEo4bvZON3vnQebUSmo5TO73CRBFb8ZFOOEqllejsGOTdp7AvnSjIiNToRg5P5xcvl73w0vewB6sCpCDBukn%2FkiQruQQb0jDhSXZVdQENa%2F%2BCk2DUd0RLoMlrAEZAMimuCXqWg411VGufL8NlVpX%2BMkC4BwQwASxEnuDNIBAf1em7YmpSksyT%2BJNMBPjQZ1NPPnKtkpFYNCpKmWCccZTi2LseEomaPevcCgRaOpihLLK5lzI569QynXHmhkRuw4bqDOtnOfo8iNs5LzuuJ6qlcUpeMJxwAedQ%2B%2F77XE%2FWJddMPF8MRCvjYn0RL47YCptbroJbnnoIa3b4J4rEhEMiSUhkiK%2Bob7AT0KPRWDnVmR1j7cA3uQO%2Bcimyu3PYMlvFuAJcen18AL463iOHSlbg%2Bt4sKwXST88Dwtahkc6ZtVsa2%2FifvGu0oCCbuDAy3mUCMKy0q2WbgUv6B3PvjAOE69OitZWmG7bJ8WJcLXBJfaTkqlWjPbqLRqOgJ6ST8Ge6CQAwzowwvYohU%2BeFyPfR8FQkwBQXbD8jDumZW9BjqkAcX483wt1T56Nfqonk5rkrFCD7uvAMQ7H4ss8c%2BJNZ9gFgQYwoQ4dKf9Djl%2F6zr06RjGdfyf5mUOsspYgT6iYP3zaCLwiCVGPzLGWI4V3MaxT7GSfs%2BhoL2YelXlmphVzMAX6RKy8v%2BsIgGo8S9DydwsV6bEa%2B9zl9VglXk2Moe4BrWlTEGu1d%2FKYFh06BSWq%2FvZXB6AerNKiCej8BTNtqHR9wkC&X-Amz-Signature=0bb4e6b32b3020f0e807e446302f2d404123daf183622d3c762bca574bffe520&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB66TIGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD4L9ploCUmqLPKxToL%2FEmoUc%2FFd65yhRINImbdD38o4wIgQwOmC9Cc0lyq4m7EfRELWK6K5JfXZgoE49Hy16Cv%2B28q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDny2HvHSfdcFZrQwCrcA1cdW7%2BtdxS9vl2EBw0Esjw5OgozsQsBMyUCYoKUU4aQYXm03R%2FgL0b%2B7aPOeZEtWC2hlgDHv9qvs8zL4%2Fq9x9QcrCrDWJV8TH4L92y%2B3vJ52wr%2BYJDtuSswVZeoH8kRnkx1hHtt%2BGLeJm1W2Ch3F5fIym%2FtDkWT%2BvsnfEAcZNoJrVqHnoxMSAAu5bZKauaK09n89eJAE7NxYj1tXqrzQ0aGcMfUuWJRuAcoNIA4h241rSL%2BtcW2BkMYWlGJKDyhypwl3uqNP%2BuQEbryWtgIhs0m9T2odPP1sXEAK5yN0yjHenYPssWM1IGegh%2FKiTcnMXHAqlMDKo5Gs3Fi0SDN%2FKmglfAWmvDM3eV8x2%2Ba%2B9UOnx6RZa9w1SqzcltpGsDilu24KTmB2Pf3ejRNMtIhtHwyHnmbTF6BTD36EX6Jr5dTLOdNCYl%2FRVGBVrN40Gh4zhWs2HbzWxw71yhJZfX%2BVRuDZE3WIKt1EtfD6%2BMXJeR8cgIjqzAT%2FaJY5NGQijPfdxw%2BQWXlra%2F%2Bf7kSGhfRMAKo74wL5iJJVvXlhwsbTslMw0W1jPCIvsWEgCQGDRdMfaY1GJ1VNPh1bZNP3oyMOtQQx1HGeQbkqWJukjikH2gq%2FSZxRPle8nl2EFNUMImalb0GOqUBFl0m9pn%2F2xwrRPTGajTwfgA1lMQ2xrDq7t12uLZl5ksKlFIWRHuDHJ3rlyyMt%2FNuoYpX%2FjowAUYDLrJw2P0RBtFnt0rn8NjwZ7jECTHHeKrZ0u%2F080ejtwrIUfiqaGxNqbCOyJzaDg575EZOoSVMIaT5w9U9fOT6e%2BAW%2FIQLRm1Sc5oKvM1DdjDGmrHH8OYU1sqAN6t4q6eXXNzUgNML5h4%2Fh49K&X-Amz-Signature=0c2885f5358328fc6ac4128ec87d86bfea9b486ca0edb6bb65083a9c0baf9093&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FVG5SMH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIFoexJtBmrK5JrmANOLWMpu%2BSdo8VDuA%2BThxDuf8XX3eAiAkC%2FxG8AB9BvGGxDVeMG3aLIx5PsqDKsv%2B2N02vTlh0Cr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMpCckLRuFzZYBnXC4KtwDGdSZtjWkKgjtpWLeXbILYjyrlsNkbIg0ORi2JKneoLk0pw4PXVWGzgDkOqeuAFrTef4dnVyNjS3tJkVMuthsppoYpAcjIYHmtY8weAi3sf3tWWTO0Xa%2FZ0%2BBatTcCnJftl1moy452hlTAwyXRLDdSjnFR5w3BD53bQGyqduV4T9dMROW9beer7TVzs4Z9ekCEl4xQkOZuKH%2FL2iLLuonwuxFvlqT4L8YUIsQkJsTo9%2Be8M010b%2BicVtQ7reLnBnm8eyfmmvsUqj7K3YK2LGZRyJypmEkBE1p9MvGhOsvGXQGCqkux0mjMK5Y9RRgnELF9VvKkfCGLWlJF8hpuaUhDqSDzg%2BK6ZMjKZqteNwLdqMaEDbPYEL3cItYonwle0WVi%2FxZoMonIrmoSzUGWKJFjfU5EEQEVeIBuaCceQOW%2Bt9qQUKy4h%2Bca91cUguhpIT7PlMd2apDSWlOjw%2FVSs9Rfatg3PF09967KW3OHHjS7gYGewK7G9lNlPJUHwdOqDNo8n4FOEEhkjU1fTTknD3CAqqxoF2H49Ybj7zqChSJ1CIVRFuN43nC5fWfeSO8no16T8zi%2FNGinlk0wyNb7r%2BFB0FXqlKSqPso7C5uRot3BPrGMXlnFtkvIdNICmow5JmVvQY6pgFczf0jsXQG4jNpFl4NKbUer1Ygtouh0oC4NbJNrA93yhnFc0eZqtFRbscezh%2F8UWyDusNjiivXoESkj7xVPVu6D0WRXzBBe8aT6Gw2YindJ1w12jqETS8EaniVEJ%2FDchyDsH4xPS1RagTRLQIbxrQKr6lhmTD0%2FE0xs9gW8rccKgJkvGT%2F6ddJxiZGQRwmQvHxTfbd9udXo4%2Fm2fRmFZDbsjMxvBw3&X-Amz-Signature=449a19120d64b61e2c8bfc12a079333cccea73815d4bb1825130eabe60e792a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUNY7TA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDlFuRJTan8bKCvS08%2FgL%2BH8ilj6Frk9NRwTD4QOVZCuQIhANpfiGYqcdJgQRpxasIfSwTOkJ7iOhPS%2B3RtlzKlueqnKv8DCGkQABoMNjM3NDIzMTgzODA1IgyYI6JrrivDxDc9AZ0q3ANAMK%2FI05V%2Bxxe5DgLqCWTnRpPBoMR9CZ6UJzF7FdZtNE0LEPAVYr2SFF%2Bvja9IbEA%2BW%2F5JK00OBMg0E3oaepY5ACRgqcEo4bvZON3vnQebUSmo5TO73CRBFb8ZFOOEqllejsGOTdp7AvnSjIiNToRg5P5xcvl73w0vewB6sCpCDBukn%2FkiQruQQb0jDhSXZVdQENa%2F%2BCk2DUd0RLoMlrAEZAMimuCXqWg411VGufL8NlVpX%2BMkC4BwQwASxEnuDNIBAf1em7YmpSksyT%2BJNMBPjQZ1NPPnKtkpFYNCpKmWCccZTi2LseEomaPevcCgRaOpihLLK5lzI569QynXHmhkRuw4bqDOtnOfo8iNs5LzuuJ6qlcUpeMJxwAedQ%2B%2F77XE%2FWJddMPF8MRCvjYn0RL47YCptbroJbnnoIa3b4J4rEhEMiSUhkiK%2Bob7AT0KPRWDnVmR1j7cA3uQO%2Bcimyu3PYMlvFuAJcen18AL463iOHSlbg%2Bt4sKwXST88Dwtahkc6ZtVsa2%2FifvGu0oCCbuDAy3mUCMKy0q2WbgUv6B3PvjAOE69OitZWmG7bJ8WJcLXBJfaTkqlWjPbqLRqOgJ6ST8Ge6CQAwzowwvYohU%2BeFyPfR8FQkwBQXbD8jDumZW9BjqkAcX483wt1T56Nfqonk5rkrFCD7uvAMQ7H4ss8c%2BJNZ9gFgQYwoQ4dKf9Djl%2F6zr06RjGdfyf5mUOsspYgT6iYP3zaCLwiCVGPzLGWI4V3MaxT7GSfs%2BhoL2YelXlmphVzMAX6RKy8v%2BsIgGo8S9DydwsV6bEa%2B9zl9VglXk2Moe4BrWlTEGu1d%2FKYFh06BSWq%2FvZXB6AerNKiCej8BTNtqHR9wkC&X-Amz-Signature=b7168094681a6be0eb400a4ecdcd6d42526745dd2e5165ed826595b101d58773&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUNY7TA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDlFuRJTan8bKCvS08%2FgL%2BH8ilj6Frk9NRwTD4QOVZCuQIhANpfiGYqcdJgQRpxasIfSwTOkJ7iOhPS%2B3RtlzKlueqnKv8DCGkQABoMNjM3NDIzMTgzODA1IgyYI6JrrivDxDc9AZ0q3ANAMK%2FI05V%2Bxxe5DgLqCWTnRpPBoMR9CZ6UJzF7FdZtNE0LEPAVYr2SFF%2Bvja9IbEA%2BW%2F5JK00OBMg0E3oaepY5ACRgqcEo4bvZON3vnQebUSmo5TO73CRBFb8ZFOOEqllejsGOTdp7AvnSjIiNToRg5P5xcvl73w0vewB6sCpCDBukn%2FkiQruQQb0jDhSXZVdQENa%2F%2BCk2DUd0RLoMlrAEZAMimuCXqWg411VGufL8NlVpX%2BMkC4BwQwASxEnuDNIBAf1em7YmpSksyT%2BJNMBPjQZ1NPPnKtkpFYNCpKmWCccZTi2LseEomaPevcCgRaOpihLLK5lzI569QynXHmhkRuw4bqDOtnOfo8iNs5LzuuJ6qlcUpeMJxwAedQ%2B%2F77XE%2FWJddMPF8MRCvjYn0RL47YCptbroJbnnoIa3b4J4rEhEMiSUhkiK%2Bob7AT0KPRWDnVmR1j7cA3uQO%2Bcimyu3PYMlvFuAJcen18AL463iOHSlbg%2Bt4sKwXST88Dwtahkc6ZtVsa2%2FifvGu0oCCbuDAy3mUCMKy0q2WbgUv6B3PvjAOE69OitZWmG7bJ8WJcLXBJfaTkqlWjPbqLRqOgJ6ST8Ge6CQAwzowwvYohU%2BeFyPfR8FQkwBQXbD8jDumZW9BjqkAcX483wt1T56Nfqonk5rkrFCD7uvAMQ7H4ss8c%2BJNZ9gFgQYwoQ4dKf9Djl%2F6zr06RjGdfyf5mUOsspYgT6iYP3zaCLwiCVGPzLGWI4V3MaxT7GSfs%2BhoL2YelXlmphVzMAX6RKy8v%2BsIgGo8S9DydwsV6bEa%2B9zl9VglXk2Moe4BrWlTEGu1d%2FKYFh06BSWq%2FvZXB6AerNKiCej8BTNtqHR9wkC&X-Amz-Signature=0034f2c92e1755fa6bee2ee4564cd565d0dba1d54fffed71f211b862c4e9e5f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUNY7TA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDlFuRJTan8bKCvS08%2FgL%2BH8ilj6Frk9NRwTD4QOVZCuQIhANpfiGYqcdJgQRpxasIfSwTOkJ7iOhPS%2B3RtlzKlueqnKv8DCGkQABoMNjM3NDIzMTgzODA1IgyYI6JrrivDxDc9AZ0q3ANAMK%2FI05V%2Bxxe5DgLqCWTnRpPBoMR9CZ6UJzF7FdZtNE0LEPAVYr2SFF%2Bvja9IbEA%2BW%2F5JK00OBMg0E3oaepY5ACRgqcEo4bvZON3vnQebUSmo5TO73CRBFb8ZFOOEqllejsGOTdp7AvnSjIiNToRg5P5xcvl73w0vewB6sCpCDBukn%2FkiQruQQb0jDhSXZVdQENa%2F%2BCk2DUd0RLoMlrAEZAMimuCXqWg411VGufL8NlVpX%2BMkC4BwQwASxEnuDNIBAf1em7YmpSksyT%2BJNMBPjQZ1NPPnKtkpFYNCpKmWCccZTi2LseEomaPevcCgRaOpihLLK5lzI569QynXHmhkRuw4bqDOtnOfo8iNs5LzuuJ6qlcUpeMJxwAedQ%2B%2F77XE%2FWJddMPF8MRCvjYn0RL47YCptbroJbnnoIa3b4J4rEhEMiSUhkiK%2Bob7AT0KPRWDnVmR1j7cA3uQO%2Bcimyu3PYMlvFuAJcen18AL463iOHSlbg%2Bt4sKwXST88Dwtahkc6ZtVsa2%2FifvGu0oCCbuDAy3mUCMKy0q2WbgUv6B3PvjAOE69OitZWmG7bJ8WJcLXBJfaTkqlWjPbqLRqOgJ6ST8Ge6CQAwzowwvYohU%2BeFyPfR8FQkwBQXbD8jDumZW9BjqkAcX483wt1T56Nfqonk5rkrFCD7uvAMQ7H4ss8c%2BJNZ9gFgQYwoQ4dKf9Djl%2F6zr06RjGdfyf5mUOsspYgT6iYP3zaCLwiCVGPzLGWI4V3MaxT7GSfs%2BhoL2YelXlmphVzMAX6RKy8v%2BsIgGo8S9DydwsV6bEa%2B9zl9VglXk2Moe4BrWlTEGu1d%2FKYFh06BSWq%2FvZXB6AerNKiCej8BTNtqHR9wkC&X-Amz-Signature=886241bb8d460b275df8d47ca5f2462c2dd4a375799ebfb55aba1a26fca63260&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LLN7JCM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBB3lc02kxiVJiVVR7rIkbl08trOd1k%2Bf1wUCMX8%2BmX3AiEAnJMiYbvV76uBIZp7WTaiiSwS1JuqgOOUAKM54gtY8fsq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDEYg2yD5MT44WkqoXircA5%2BHyfhBCrXxFK8Xe3LHcDd5GfeVnVewy3C7NH97NG9yU%2FsosZxtjH2MX0MkcZjb3tMtPgfqk%2BlfCncypk4Dn9RCQJA4E6%2FaVuALKFHunPqcds6N7DjILwFFdX4E18uhBh5uTFDSAHcsmY3OVe9VT%2BEcaEKZCsYOnNMDxdwl2DM2CZoG0KXG7esSJiiD0IMTZ%2BegQHFTPKGJJknj0Dwgh8MD6EONrnAreitJdeHwV8nqLrC7WZqmHbYTLF6xZkP3Aeu33kl7jYngWPY81TkrquyFKqRFPkl9f7H5B8RCm7gcH7Rhi6t2fkJ1liRAHaVGcG%2BHeP%2BcKKTem7%2B2TOjteccfZNFPVB7WPSzIARom02piDCDzQWIH531xgOJU9ruT6jaip2hGi%2F%2BlsnwlvDF1p4shy%2FQHsTiEBpW%2FI71um6rwcTPic0r%2F7j%2Fxp2RuxdLTKG%2BrXMAqCshKHPKJK1%2Fyen2ehwbTQ6k4GMqEW3T5E2%2BuGs5yRaShBZ9zGaaba9dPZYiQYSLanDwZqK4Vin1CgFAnww38%2Bp99Xn9GxapDbQFj10x%2FsCJqYLoBg8yzWE9SMz0LnMIh7dWJhcrFrPSfxgKWV9fj5F1NnXFVtcSWXuFWrivBtQhsZ6s%2FDxNLMNyZlb0GOqUBQ0oN%2FGXCMyg1ItHScYSuzxGZtsk9eEwvVAvePdL%2F5roct3BpwjR8b1vntp9E%2FSAzifCvkCiXOGUDRzsHOgDefBWky5bh71csvXay1n2e964kph809EhMCEaNQroYfd%2BuSgmN0Ui6GDvgSC%2BBlUHga6vSilIjWppgwMml82EuQqAz8NU5eF68cS2jBbz2GMof97yLgdNIWXj%2BBPBDNP9AqhrVEU2n&X-Amz-Signature=511bcaacf10a82ae55e1a13a11df37462ac086efe38c742c7e88feab7d3176b4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQV443OC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBPrAEvWxTq2jG50UuBJnrHpMK%2FCkGC%2F2ptghXyK6KxIAiEA%2BSs3hUD%2BFwGljGLqzrztdk5JwydFLXtfctxP%2FAXCrlkq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDOBm8O4T%2BH2qaKjNsCrcA3t117Ef1YyfcMYp%2BxEEWRoEvbnzbHpUse0MaCwsmzq5Y8CUITSotYuHvtIxwNlJZefz1rmwyRXBE%2Fx6ddkuyGFfbAWFLfhuxlU1phiuMzOo1FPPoG34t9jkQs3tlrKa21TqtHOpTyysBDQbuLctZzmEy7EpHWFkD5HbrQGu3hatdmwajdbEfvb%2BcM7gFzsqtws2PFgNixdFjSZfrep0oy51pF2QwfhnJZArUzJAvW9foN%2FcFdxUwobAq9AsKe%2FRk1woBTxlbPyAAZs7Rdf3VMbP60M1Me9fnYzaEimwqAyc99QrPcSfA6czIyRKPG61vfobAs4ijXlxwlC3UgSWT5BtGkiavE0nhLIWHcPBMRc0zvNwzdnCIKbYKZMfCD9TBGIa4bbcc7vpqeQXfVmHsAmkQczTlFLoMCQVsMcj3KjGep1fcdeY1BtBVGWg0Aa4OpQyAIfZnEWx51Avx8X0UvdnQPIAe%2Frp8ikOVE2kS%2B1RAbw1ps9oWXduvCJcODE7H780FdAR04LVVIEP9SDPJADsKL0uaxEW%2FeyfFu3xovKjUYEDugLCHxfQUNgjYTBsJwNqdD42oHoMe6uTSfX4npEiEJ3g%2FAzEkKS4zrqTqmnBhXDRabT8jU7x%2BzYsMOKZlb0GOqUB4fNAOjp3OYr8XSHaKUQ6QymuvvNqxg7Cdi9SioEAbohCplMycD9p6yVrexLP13w%2BQfPLdhDiZG11JxV%2FeR4ZNMC5%2FkhK8DteuKzCLSMp7ukyzg0kqMuhLAIYjsS3MCJBN%2FhknoGmIeyyPp6rnLNNBXBaaf0a3ak6fkk8D3855LcDUhfsz6oagfCkYmbPQJ8l%2Bzc3tFTduYW6JRFv%2Bn8KAb3aM4Te&X-Amz-Signature=0f22eb88edf13b4f7ff2a8c3c771588d3e928cc25a4c1c7fde75f5278bee351f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMAPU2EN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQC6M1mVV8W3tz970gBxc4L2TteSAm5Hanr1cfL0VZ2SnAIhAND46JB7W7r65jpaNj9fQrmDOiGyNiuJ%2F5rA0vWuCu3LKv8DCGkQABoMNjM3NDIzMTgzODA1IgwGYpMIgvxJueqSc%2FIq3AMZjIy7EnjWpyQb3SDwI6oRpRNdP7V0yLXGOWTm6r%2Btl6u3l45SWbhNGhXNBmgcpVC5mrqbP8JlnZYg4LfrhGPI8uax1pEMMWbKnEJUd6tdKD1IPr130t1du8LQPiCFiyKXmBxdLH7GMbat3xR48mI5o8heiwBw3IRQDqIXJjAr6VS3c2pGqrBfWGmz9oU20aLw1S59cSEkejgyIf96mxOeh6zRuLkWPjPubJGr2uAzu5Yz9CaT6yhsfXC0eW%2B6937Iq55VObnZQIr%2FmHU7KeDXv8plUTjCeatQjFE6RNGmuQLNPNn63NUMNoWX%2FgNpvHva3dgwwKnbr8TzAjIO7cONK0mzjEp5KkjpRQG2CREC1cT5YlQBNwjV3b6DQM%2Bn9eAUlTgbSQwz1XAzTqSYe4mJPdrdfwsY2RoKsYE7gFoCAnCkVha2b2L9MTihgW4XtWZD2tPkbZRlymNv%2FhWhsx%2Bg9P%2B51TY%2F1Pnaee0GQy2r1cKIN9m0tYdkwgQ%2BMfa%2BxcJkC5ZPBJ24N7UIsG6iMJmeda0dCaYAiU7DCNJ7q8SqTyMK5p4Qy8zOMREiIl5VyQnYk8W4ljq7OFuLMhFBvUN6wOG7brqhPd6zmDpqrlUGm9qr9J9VcSEJ8FxaFzC8mpW9BjqkAZ0PDY4I2TAjWqIAJMZbN0fs84h7aJJS0nGh1c9486xm9inMekexZwyp%2BJA4Va4MYBbLRl4VZAXVCcag%2Fnw2FsNOhy81gMzEHGjNWC5KGcLy7aK21dghh1v%2Fp%2Fe8UMjBUQGpHzcNxhDP1kJe%2B%2FoORLBV5UlCDx4BEw2pZtepkEWhSzmpLf53H9Poa5zx0uy2c%2B6AVbYqAHUBSgR1UN9Xw9NN%2FeAd&X-Amz-Signature=9e2f4beae3daa08a8790bcf6b71b4a559003f655ec47144ab5f0230fa49b5a88&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R54CZ3DM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDDhRLZaEdacLYhfFsrGfiCNhSAGNJWgtga%2BwRM55%2Fr4wIhAOSp3r52BljHQ5EqJL1AdjYaao1AXAOufjQHdpiYsTGsKv8DCGkQABoMNjM3NDIzMTgzODA1IgwDz1MFeuxpDFCbsNAq3ANt6ECILTEgNs2xoNVqiRYqRZmgz4Z2CGGWzk0twaAysrYLKDxZBzctRYAIhnvp4qZe0QmNl76fHRAIQ0LC%2FxxQUq6xmE3FD6FEQxnpFtOLsar1qW29zIvwusbNiRZEMWzE5UnVT4SeNwi4EmMKhdrheEZCzVbdFna75pePDp%2BqvtK6ediJgm9pODJvdfUSMNaDv%2BDIewU4pbKdgOyHwX2D%2BXF71qhl1%2Fs4tf%2FBHISmzLCayt2c2d%2Feyma2vW2B6ZAnptgYnkLDtHhTsCbb1AjkE4tfDeF%2BVVb6KSai%2B75UVewc1pJGmR%2BdGrFnzC06wvlFLloeKj4I4m77o908Syu3C6jvmw4SRmnkvIWdci098lItQZfWS3HvX092bU3pc0RhOY485%2F0nFj%2FpQ7FZyV7VU37GsSORD0T6QunEFYD5UHNDJIUONbRTxETy9vnWR3rsJ4maStl7kqcox%2FZfgAUl2pQHJWy%2BSNo2hfCXPu3kjFFl08jsx2pRsLlz8Grt1BCU9eSQ4Ofw2%2FGB9kVP1664oyc0XRWB264U2toCIYCQU%2F%2BuSSyNF%2FGaLjWMqcQpAELdscTQJMfydPiiIGCI%2BgEc%2BHYAdFidkywKzsGmQw8e%2BYtYU0bv6oJqwa7M%2FjCTmpW9BjqkAUUHrcjG5U51CUx%2BFj6eQFc5EwskOEJGCogCIF9YxTaUBLZpNnF3uRQayONibhpiB%2BtAiuZKjQcGwO%2FNBE5FL1CN13FdtbepFMx2WUmV0ePfiJU5K3V1Ot0Dg0RIc2tbHEQmtImpGsDBBZc6a1InxDG1rxGjK4V0IQj10oR3J734mCleFL%2By8YwBVD%2BxojoWmj6NYYLhjJl2jQ9eurogIdeTPbxp&X-Amz-Signature=1bec19b2563cf6251dbfbbf314155d0aed2d0a67d50e1e89e0bb7762062e294a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R54CZ3DM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDDhRLZaEdacLYhfFsrGfiCNhSAGNJWgtga%2BwRM55%2Fr4wIhAOSp3r52BljHQ5EqJL1AdjYaao1AXAOufjQHdpiYsTGsKv8DCGkQABoMNjM3NDIzMTgzODA1IgwDz1MFeuxpDFCbsNAq3ANt6ECILTEgNs2xoNVqiRYqRZmgz4Z2CGGWzk0twaAysrYLKDxZBzctRYAIhnvp4qZe0QmNl76fHRAIQ0LC%2FxxQUq6xmE3FD6FEQxnpFtOLsar1qW29zIvwusbNiRZEMWzE5UnVT4SeNwi4EmMKhdrheEZCzVbdFna75pePDp%2BqvtK6ediJgm9pODJvdfUSMNaDv%2BDIewU4pbKdgOyHwX2D%2BXF71qhl1%2Fs4tf%2FBHISmzLCayt2c2d%2Feyma2vW2B6ZAnptgYnkLDtHhTsCbb1AjkE4tfDeF%2BVVb6KSai%2B75UVewc1pJGmR%2BdGrFnzC06wvlFLloeKj4I4m77o908Syu3C6jvmw4SRmnkvIWdci098lItQZfWS3HvX092bU3pc0RhOY485%2F0nFj%2FpQ7FZyV7VU37GsSORD0T6QunEFYD5UHNDJIUONbRTxETy9vnWR3rsJ4maStl7kqcox%2FZfgAUl2pQHJWy%2BSNo2hfCXPu3kjFFl08jsx2pRsLlz8Grt1BCU9eSQ4Ofw2%2FGB9kVP1664oyc0XRWB264U2toCIYCQU%2F%2BuSSyNF%2FGaLjWMqcQpAELdscTQJMfydPiiIGCI%2BgEc%2BHYAdFidkywKzsGmQw8e%2BYtYU0bv6oJqwa7M%2FjCTmpW9BjqkAUUHrcjG5U51CUx%2BFj6eQFc5EwskOEJGCogCIF9YxTaUBLZpNnF3uRQayONibhpiB%2BtAiuZKjQcGwO%2FNBE5FL1CN13FdtbepFMx2WUmV0ePfiJU5K3V1Ot0Dg0RIc2tbHEQmtImpGsDBBZc6a1InxDG1rxGjK4V0IQj10oR3J734mCleFL%2By8YwBVD%2BxojoWmj6NYYLhjJl2jQ9eurogIdeTPbxp&X-Amz-Signature=ba9b43fd838393ce4ddc6b47cadc2d6d3bf4f2709f01901a08ae5f766fc13bfe&X-Amz-SignedHeaders=host&x-id=GetObject)

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
