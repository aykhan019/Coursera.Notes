

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=a4ad62392e961b88433875a42dc38cfb40727f7ec4a50b3352a86653c3b18c17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=5dfd818b3d85c0908bd117f1038fc68ee4dcdfb19c309cd7257b0e6a2c0dc105&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=0023597e82844f2a8c40d333f83a26f2e3d5c7448d9641def3ffeb9b534547a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4Y3XFP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3HzS0z8ctX%2Fh%2FIQ4tCKpJalgrcta89MHiy2LY0eqJgIhAPX3PcpqXSaKLp1Y8hJApqQbJh5PQGttAn5SoBFxEotBKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuuxU3PmAZJ0g4tuwq3APPq0tvIcgtrhAWuHSIMb5EkvifhyjbFyDyh%2BugU96C3cStU8MExSIrl0PTDr4lRLl7S0wMD%2FAwTj2w2IqHVK6TnBUqZHxHygS9uZ5idvylqgKg3ygldVgEECJYTcLw8YNUOr17XHn4Pw1XX%2FCKF%2FxwUgsx1eKwGKVrc9xJ%2BoM%2FL0iz2jyqaxL3%2F7tlyJcaf%2BIg7l6VgFstwlJI8h6x4uhHzqW77xLKd%2FwL60Honys68fHwt7MeWFFJ8UL%2B%2FDP7%2B6zelPY4bvgM3lt0yzITziqp8n1sqllv%2BmuA0yxU73d7CyRxwmdLYuYFSPqemsxG1GS2mI78DLoSz0vBtXAQYnLnQodhWVKYb7xBzK07yXEB5ZE8hx7KqPNRbQ9qnui%2BQPvikLio82k1xUdiBET0kz6%2FrWXsPx7aeK%2BzBB2vo4ME3hh4fkMLXuFauqSgBGGHWHN%2B0btke656jGK0aFCD3GQKHEwPVSGkt01kGq7e6D0pTwSGoLFeS9ZAJvSqhlIgtj%2BBW0lWQvRhozlas31x8baPkxnRQOziAZYjQ65I2RFanurfeks7AXtBTJB75ddpG7VWE%2B8aKm1%2FJshj5SB9Mwo3rOWg%2FcBN5Abpx%2Fmrn9GTj3RFbvQ59NFpfIxmYTCu0PC8BjqkAYu1aYRddGFBFvKIl%2Fid80VFcPvWFibCDTNzp%2BsDy5Ox53mcGBzazkbfMv4gg%2B1KRUtMrdSAjqfeTh5ljCYuTL7hc4Xmp%2BgSpcayylvz3LUMzi4q3IqGgDjnlvma1X17WnKGvtAiDQ0c1atzy%2Fq6EFWROodE03Qx9MoMhe487xK%2BEHzC%2FT2hDY9D3IOX6EXrhoJ7es1MNUwRpJQgfM7HJuLHxDJP&X-Amz-Signature=d902758f41c6ea7eb2920becd249b060a3b40da91c8569a0bd9ef5cf01b8a6d0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4Y3XFP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3HzS0z8ctX%2Fh%2FIQ4tCKpJalgrcta89MHiy2LY0eqJgIhAPX3PcpqXSaKLp1Y8hJApqQbJh5PQGttAn5SoBFxEotBKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuuxU3PmAZJ0g4tuwq3APPq0tvIcgtrhAWuHSIMb5EkvifhyjbFyDyh%2BugU96C3cStU8MExSIrl0PTDr4lRLl7S0wMD%2FAwTj2w2IqHVK6TnBUqZHxHygS9uZ5idvylqgKg3ygldVgEECJYTcLw8YNUOr17XHn4Pw1XX%2FCKF%2FxwUgsx1eKwGKVrc9xJ%2BoM%2FL0iz2jyqaxL3%2F7tlyJcaf%2BIg7l6VgFstwlJI8h6x4uhHzqW77xLKd%2FwL60Honys68fHwt7MeWFFJ8UL%2B%2FDP7%2B6zelPY4bvgM3lt0yzITziqp8n1sqllv%2BmuA0yxU73d7CyRxwmdLYuYFSPqemsxG1GS2mI78DLoSz0vBtXAQYnLnQodhWVKYb7xBzK07yXEB5ZE8hx7KqPNRbQ9qnui%2BQPvikLio82k1xUdiBET0kz6%2FrWXsPx7aeK%2BzBB2vo4ME3hh4fkMLXuFauqSgBGGHWHN%2B0btke656jGK0aFCD3GQKHEwPVSGkt01kGq7e6D0pTwSGoLFeS9ZAJvSqhlIgtj%2BBW0lWQvRhozlas31x8baPkxnRQOziAZYjQ65I2RFanurfeks7AXtBTJB75ddpG7VWE%2B8aKm1%2FJshj5SB9Mwo3rOWg%2FcBN5Abpx%2Fmrn9GTj3RFbvQ59NFpfIxmYTCu0PC8BjqkAYu1aYRddGFBFvKIl%2Fid80VFcPvWFibCDTNzp%2BsDy5Ox53mcGBzazkbfMv4gg%2B1KRUtMrdSAjqfeTh5ljCYuTL7hc4Xmp%2BgSpcayylvz3LUMzi4q3IqGgDjnlvma1X17WnKGvtAiDQ0c1atzy%2Fq6EFWROodE03Qx9MoMhe487xK%2BEHzC%2FT2hDY9D3IOX6EXrhoJ7es1MNUwRpJQgfM7HJuLHxDJP&X-Amz-Signature=62edb9bac99095c8bc01e7877bbec711837f29da7c0834a1f4d928b74be36b02&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4Y3XFP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3HzS0z8ctX%2Fh%2FIQ4tCKpJalgrcta89MHiy2LY0eqJgIhAPX3PcpqXSaKLp1Y8hJApqQbJh5PQGttAn5SoBFxEotBKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuuxU3PmAZJ0g4tuwq3APPq0tvIcgtrhAWuHSIMb5EkvifhyjbFyDyh%2BugU96C3cStU8MExSIrl0PTDr4lRLl7S0wMD%2FAwTj2w2IqHVK6TnBUqZHxHygS9uZ5idvylqgKg3ygldVgEECJYTcLw8YNUOr17XHn4Pw1XX%2FCKF%2FxwUgsx1eKwGKVrc9xJ%2BoM%2FL0iz2jyqaxL3%2F7tlyJcaf%2BIg7l6VgFstwlJI8h6x4uhHzqW77xLKd%2FwL60Honys68fHwt7MeWFFJ8UL%2B%2FDP7%2B6zelPY4bvgM3lt0yzITziqp8n1sqllv%2BmuA0yxU73d7CyRxwmdLYuYFSPqemsxG1GS2mI78DLoSz0vBtXAQYnLnQodhWVKYb7xBzK07yXEB5ZE8hx7KqPNRbQ9qnui%2BQPvikLio82k1xUdiBET0kz6%2FrWXsPx7aeK%2BzBB2vo4ME3hh4fkMLXuFauqSgBGGHWHN%2B0btke656jGK0aFCD3GQKHEwPVSGkt01kGq7e6D0pTwSGoLFeS9ZAJvSqhlIgtj%2BBW0lWQvRhozlas31x8baPkxnRQOziAZYjQ65I2RFanurfeks7AXtBTJB75ddpG7VWE%2B8aKm1%2FJshj5SB9Mwo3rOWg%2FcBN5Abpx%2Fmrn9GTj3RFbvQ59NFpfIxmYTCu0PC8BjqkAYu1aYRddGFBFvKIl%2Fid80VFcPvWFibCDTNzp%2BsDy5Ox53mcGBzazkbfMv4gg%2B1KRUtMrdSAjqfeTh5ljCYuTL7hc4Xmp%2BgSpcayylvz3LUMzi4q3IqGgDjnlvma1X17WnKGvtAiDQ0c1atzy%2Fq6EFWROodE03Qx9MoMhe487xK%2BEHzC%2FT2hDY9D3IOX6EXrhoJ7es1MNUwRpJQgfM7HJuLHxDJP&X-Amz-Signature=cc61edd5c0c6f35558f934333b3cc640aff0be1152e56d8e555ac8388ac10805&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4Y3XFP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3HzS0z8ctX%2Fh%2FIQ4tCKpJalgrcta89MHiy2LY0eqJgIhAPX3PcpqXSaKLp1Y8hJApqQbJh5PQGttAn5SoBFxEotBKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuuxU3PmAZJ0g4tuwq3APPq0tvIcgtrhAWuHSIMb5EkvifhyjbFyDyh%2BugU96C3cStU8MExSIrl0PTDr4lRLl7S0wMD%2FAwTj2w2IqHVK6TnBUqZHxHygS9uZ5idvylqgKg3ygldVgEECJYTcLw8YNUOr17XHn4Pw1XX%2FCKF%2FxwUgsx1eKwGKVrc9xJ%2BoM%2FL0iz2jyqaxL3%2F7tlyJcaf%2BIg7l6VgFstwlJI8h6x4uhHzqW77xLKd%2FwL60Honys68fHwt7MeWFFJ8UL%2B%2FDP7%2B6zelPY4bvgM3lt0yzITziqp8n1sqllv%2BmuA0yxU73d7CyRxwmdLYuYFSPqemsxG1GS2mI78DLoSz0vBtXAQYnLnQodhWVKYb7xBzK07yXEB5ZE8hx7KqPNRbQ9qnui%2BQPvikLio82k1xUdiBET0kz6%2FrWXsPx7aeK%2BzBB2vo4ME3hh4fkMLXuFauqSgBGGHWHN%2B0btke656jGK0aFCD3GQKHEwPVSGkt01kGq7e6D0pTwSGoLFeS9ZAJvSqhlIgtj%2BBW0lWQvRhozlas31x8baPkxnRQOziAZYjQ65I2RFanurfeks7AXtBTJB75ddpG7VWE%2B8aKm1%2FJshj5SB9Mwo3rOWg%2FcBN5Abpx%2Fmrn9GTj3RFbvQ59NFpfIxmYTCu0PC8BjqkAYu1aYRddGFBFvKIl%2Fid80VFcPvWFibCDTNzp%2BsDy5Ox53mcGBzazkbfMv4gg%2B1KRUtMrdSAjqfeTh5ljCYuTL7hc4Xmp%2BgSpcayylvz3LUMzi4q3IqGgDjnlvma1X17WnKGvtAiDQ0c1atzy%2Fq6EFWROodE03Qx9MoMhe487xK%2BEHzC%2FT2hDY9D3IOX6EXrhoJ7es1MNUwRpJQgfM7HJuLHxDJP&X-Amz-Signature=2c9497614ae2effb3f26b46f27e8e5e8742d7547d781b004d0d1c907b43c32c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4Y3XFP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3HzS0z8ctX%2Fh%2FIQ4tCKpJalgrcta89MHiy2LY0eqJgIhAPX3PcpqXSaKLp1Y8hJApqQbJh5PQGttAn5SoBFxEotBKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuuxU3PmAZJ0g4tuwq3APPq0tvIcgtrhAWuHSIMb5EkvifhyjbFyDyh%2BugU96C3cStU8MExSIrl0PTDr4lRLl7S0wMD%2FAwTj2w2IqHVK6TnBUqZHxHygS9uZ5idvylqgKg3ygldVgEECJYTcLw8YNUOr17XHn4Pw1XX%2FCKF%2FxwUgsx1eKwGKVrc9xJ%2BoM%2FL0iz2jyqaxL3%2F7tlyJcaf%2BIg7l6VgFstwlJI8h6x4uhHzqW77xLKd%2FwL60Honys68fHwt7MeWFFJ8UL%2B%2FDP7%2B6zelPY4bvgM3lt0yzITziqp8n1sqllv%2BmuA0yxU73d7CyRxwmdLYuYFSPqemsxG1GS2mI78DLoSz0vBtXAQYnLnQodhWVKYb7xBzK07yXEB5ZE8hx7KqPNRbQ9qnui%2BQPvikLio82k1xUdiBET0kz6%2FrWXsPx7aeK%2BzBB2vo4ME3hh4fkMLXuFauqSgBGGHWHN%2B0btke656jGK0aFCD3GQKHEwPVSGkt01kGq7e6D0pTwSGoLFeS9ZAJvSqhlIgtj%2BBW0lWQvRhozlas31x8baPkxnRQOziAZYjQ65I2RFanurfeks7AXtBTJB75ddpG7VWE%2B8aKm1%2FJshj5SB9Mwo3rOWg%2FcBN5Abpx%2Fmrn9GTj3RFbvQ59NFpfIxmYTCu0PC8BjqkAYu1aYRddGFBFvKIl%2Fid80VFcPvWFibCDTNzp%2BsDy5Ox53mcGBzazkbfMv4gg%2B1KRUtMrdSAjqfeTh5ljCYuTL7hc4Xmp%2BgSpcayylvz3LUMzi4q3IqGgDjnlvma1X17WnKGvtAiDQ0c1atzy%2Fq6EFWROodE03Qx9MoMhe487xK%2BEHzC%2FT2hDY9D3IOX6EXrhoJ7es1MNUwRpJQgfM7HJuLHxDJP&X-Amz-Signature=29260aa88ab9a4dd102769e49db13bcda9e50c0b0cc09c26f97fee204ee9cbbc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4Y3XFP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3HzS0z8ctX%2Fh%2FIQ4tCKpJalgrcta89MHiy2LY0eqJgIhAPX3PcpqXSaKLp1Y8hJApqQbJh5PQGttAn5SoBFxEotBKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuuxU3PmAZJ0g4tuwq3APPq0tvIcgtrhAWuHSIMb5EkvifhyjbFyDyh%2BugU96C3cStU8MExSIrl0PTDr4lRLl7S0wMD%2FAwTj2w2IqHVK6TnBUqZHxHygS9uZ5idvylqgKg3ygldVgEECJYTcLw8YNUOr17XHn4Pw1XX%2FCKF%2FxwUgsx1eKwGKVrc9xJ%2BoM%2FL0iz2jyqaxL3%2F7tlyJcaf%2BIg7l6VgFstwlJI8h6x4uhHzqW77xLKd%2FwL60Honys68fHwt7MeWFFJ8UL%2B%2FDP7%2B6zelPY4bvgM3lt0yzITziqp8n1sqllv%2BmuA0yxU73d7CyRxwmdLYuYFSPqemsxG1GS2mI78DLoSz0vBtXAQYnLnQodhWVKYb7xBzK07yXEB5ZE8hx7KqPNRbQ9qnui%2BQPvikLio82k1xUdiBET0kz6%2FrWXsPx7aeK%2BzBB2vo4ME3hh4fkMLXuFauqSgBGGHWHN%2B0btke656jGK0aFCD3GQKHEwPVSGkt01kGq7e6D0pTwSGoLFeS9ZAJvSqhlIgtj%2BBW0lWQvRhozlas31x8baPkxnRQOziAZYjQ65I2RFanurfeks7AXtBTJB75ddpG7VWE%2B8aKm1%2FJshj5SB9Mwo3rOWg%2FcBN5Abpx%2Fmrn9GTj3RFbvQ59NFpfIxmYTCu0PC8BjqkAYu1aYRddGFBFvKIl%2Fid80VFcPvWFibCDTNzp%2BsDy5Ox53mcGBzazkbfMv4gg%2B1KRUtMrdSAjqfeTh5ljCYuTL7hc4Xmp%2BgSpcayylvz3LUMzi4q3IqGgDjnlvma1X17WnKGvtAiDQ0c1atzy%2Fq6EFWROodE03Qx9MoMhe487xK%2BEHzC%2FT2hDY9D3IOX6EXrhoJ7es1MNUwRpJQgfM7HJuLHxDJP&X-Amz-Signature=5a4f549337ace5bba0c43b9568f8ea661d24cd21fecd3ca645a8ebde73fc9239&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655C24DS4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0FftIsCqWq%2Fp9%2FRHCSGZ96ulExw1pcm4to1VJze%2BvZAIgaVQhqQSZ8Bd%2FGcfwYJc9kocoKB9KPQiZVONdPgaSPnMqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGATOavBeS6ib2GJfircA2oYIa7l1t6IFDXQBtjxuZr3iRy8lSEo4TNY0s%2BTEAXKeC3F8z9uLC2l0oHL7nGEoZt%2BtffI1tNMwr8HU7dHXRi3oBCnGFhzSL5hY0eP2QoqsQZfQvwoJP6Vqsyrzv0rxW9iWFp6XYYmmVuahuYpAS5OqfTPesLGc5Iia4HQNWQvlyc2TtwpAtQGPpNmWpffJyKCUUtwVyqcs4xX86UTRQEGY9OBN2HurgRBKMSUS2QLUIOiQa%2BSXeDZKtRgi3OblXnpIxUONUKnUMUFWWpnlximgpgOzOrCUAZZPGwVeNRUSrdHHE7eCBsO%2F4Gc1%2FziaryL%2BBPrbjInoTsuCSeM40rmOKNE1W2BVmJvN0iqAOcCZVk1UrSt%2BHZmpwl8q6Jcv4I1TVEB6R%2FEdv0A98zrstiodKweCJMzR0%2BQoRs1XK%2BuL4EFuUaSyoHWm%2BaYri9wzdoqcWpYIoOez4Jj3lA1wE7AfwPJ4ENKLKMx7fKXusjPdujnOPSi3mFZgNutjhFFqWgbq0fsUc91Wh9uVm6dZMcLLJ9jLzxsm10uemaJGJeK63cFP29K7M%2FI4Nak69AHmdl4OG8VK4dgMhXSi6i65FVhUdJb8jlAEj0ScoizkiyLvk012B%2Fnj4v3wL4qMJnQ8LwGOqUB%2BsPE3ieCxICeraFG9U9GK5KdOGl7dbE6KBGpjryoDGMiiF1LCCTIygEv1HTXcLfuJC28yaQeQdsC19QW63sKAh8DjKX%2F%2FxIhYOu8gLU%2BqG3bumuIKeZx6fPOet68ijHQOeQdapVGEiOAg80LSOxgK6CB5PRbUnuiqn4ziSxefoPBqFLpmXrts03W74GI04oq52bVaMQqoLyjHRL9s%2B77OFSHthUp&X-Amz-Signature=97c410f71b7e95a952218adff549b3eb2756f20b737f281111ba65ad77425066&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FRDCE3L%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSIesQxO%2BnCA9Zx%2FALAxOw2PToNJWK09rTpjFzfRf0DQIgIqZrFrHBsv3yEejoOR9d%2FkeSAPlx5aeUlboeanY2tmAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFeENqduL53b0D8erCrcA9Gm9qOa7VfMJg80MCEPLYji%2BMCXxG2m2CCfNo9zWmce4kHXD%2F%2Bx%2BVairWJkqSpeh4g%2Fb17xYgXuUBohPGi0BQR6i6MFV%2BJzj3gr%2FPAuNfeoA76%2B7ApJ9B%2ByQFk6UJJihW%2B49xNXa%2FLDpQilxhR0VkSwn8ZMnAfYkb1l7YAz5Wwhp8kqkrS6AtP0PMPPauaDs3P0YWUeSQ6mtMCgfv6SLT4JBtFTpuN1vbMamoHojZSv87N3ny%2BWo6balI11IlkijIGs%2BEDcp0flHbHH2FEioGTHTzte90eSPQiZ60SIe5kaFXAqVUBU%2F9%2FrgSfhrEaN1ZJSa1FL2QXhn%2Fcm6wuxQT7F4wRmi0t92pUO1hmwLR0vyC3skatr%2BXLr0evn0goxQEdQIZQLHC5uLrVrdhFWRQSveCYug%2B%2FLPaFnxOTAeqyYeh2hazzMsvKSONoCe8a4EOlTQpctJez4%2Fdjm1PRbddyX5pcGhSLNm9%2FBf00Q63rkcJEZTfkiFCKqvWBcHhLe%2BLb1VMPiyPaeqC2jxCs%2BROqipMQA7mvw0OG0jVsWO1fUzk5lR7BLYTXsq5o5HyS720bVgrI2ku605mdwUvwjcGWmaps3asDfpBvesYcPlemRnkd4tyLxVZ1zB2wAMLzQ8LwGOqUBOXZumTShwfzdiOiYKXZNqJKLcuggCS6Nrhd%2ByPkxBKeqEvITkArC419d6iLIpyjjaL416rG65DQqyr2c6rYGQCX8PaW823RZAFZBE2fBOeQnrSbKeegUWmlGmcOUrRdCe8UjkdplCdOSXqO3BvCz4RZTcek0zujY%2BVNCHZ367qtgFnIiQOVxke2TozT%2BYSeliqvnVKY1VVMcv%2FAy%2BOoXL4u64KYl&X-Amz-Signature=8a1e9f1eefb0198f2db22000150a9113b7d0bdffd385a5c0822a9034f6118bb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4Y3XFP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3HzS0z8ctX%2Fh%2FIQ4tCKpJalgrcta89MHiy2LY0eqJgIhAPX3PcpqXSaKLp1Y8hJApqQbJh5PQGttAn5SoBFxEotBKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuuxU3PmAZJ0g4tuwq3APPq0tvIcgtrhAWuHSIMb5EkvifhyjbFyDyh%2BugU96C3cStU8MExSIrl0PTDr4lRLl7S0wMD%2FAwTj2w2IqHVK6TnBUqZHxHygS9uZ5idvylqgKg3ygldVgEECJYTcLw8YNUOr17XHn4Pw1XX%2FCKF%2FxwUgsx1eKwGKVrc9xJ%2BoM%2FL0iz2jyqaxL3%2F7tlyJcaf%2BIg7l6VgFstwlJI8h6x4uhHzqW77xLKd%2FwL60Honys68fHwt7MeWFFJ8UL%2B%2FDP7%2B6zelPY4bvgM3lt0yzITziqp8n1sqllv%2BmuA0yxU73d7CyRxwmdLYuYFSPqemsxG1GS2mI78DLoSz0vBtXAQYnLnQodhWVKYb7xBzK07yXEB5ZE8hx7KqPNRbQ9qnui%2BQPvikLio82k1xUdiBET0kz6%2FrWXsPx7aeK%2BzBB2vo4ME3hh4fkMLXuFauqSgBGGHWHN%2B0btke656jGK0aFCD3GQKHEwPVSGkt01kGq7e6D0pTwSGoLFeS9ZAJvSqhlIgtj%2BBW0lWQvRhozlas31x8baPkxnRQOziAZYjQ65I2RFanurfeks7AXtBTJB75ddpG7VWE%2B8aKm1%2FJshj5SB9Mwo3rOWg%2FcBN5Abpx%2Fmrn9GTj3RFbvQ59NFpfIxmYTCu0PC8BjqkAYu1aYRddGFBFvKIl%2Fid80VFcPvWFibCDTNzp%2BsDy5Ox53mcGBzazkbfMv4gg%2B1KRUtMrdSAjqfeTh5ljCYuTL7hc4Xmp%2BgSpcayylvz3LUMzi4q3IqGgDjnlvma1X17WnKGvtAiDQ0c1atzy%2Fq6EFWROodE03Qx9MoMhe487xK%2BEHzC%2FT2hDY9D3IOX6EXrhoJ7es1MNUwRpJQgfM7HJuLHxDJP&X-Amz-Signature=50a9bb6d5180e4ec89177b5c2d4d450c5416062ba7ef077ee3deded11904b322&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4Y3XFP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3HzS0z8ctX%2Fh%2FIQ4tCKpJalgrcta89MHiy2LY0eqJgIhAPX3PcpqXSaKLp1Y8hJApqQbJh5PQGttAn5SoBFxEotBKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuuxU3PmAZJ0g4tuwq3APPq0tvIcgtrhAWuHSIMb5EkvifhyjbFyDyh%2BugU96C3cStU8MExSIrl0PTDr4lRLl7S0wMD%2FAwTj2w2IqHVK6TnBUqZHxHygS9uZ5idvylqgKg3ygldVgEECJYTcLw8YNUOr17XHn4Pw1XX%2FCKF%2FxwUgsx1eKwGKVrc9xJ%2BoM%2FL0iz2jyqaxL3%2F7tlyJcaf%2BIg7l6VgFstwlJI8h6x4uhHzqW77xLKd%2FwL60Honys68fHwt7MeWFFJ8UL%2B%2FDP7%2B6zelPY4bvgM3lt0yzITziqp8n1sqllv%2BmuA0yxU73d7CyRxwmdLYuYFSPqemsxG1GS2mI78DLoSz0vBtXAQYnLnQodhWVKYb7xBzK07yXEB5ZE8hx7KqPNRbQ9qnui%2BQPvikLio82k1xUdiBET0kz6%2FrWXsPx7aeK%2BzBB2vo4ME3hh4fkMLXuFauqSgBGGHWHN%2B0btke656jGK0aFCD3GQKHEwPVSGkt01kGq7e6D0pTwSGoLFeS9ZAJvSqhlIgtj%2BBW0lWQvRhozlas31x8baPkxnRQOziAZYjQ65I2RFanurfeks7AXtBTJB75ddpG7VWE%2B8aKm1%2FJshj5SB9Mwo3rOWg%2FcBN5Abpx%2Fmrn9GTj3RFbvQ59NFpfIxmYTCu0PC8BjqkAYu1aYRddGFBFvKIl%2Fid80VFcPvWFibCDTNzp%2BsDy5Ox53mcGBzazkbfMv4gg%2B1KRUtMrdSAjqfeTh5ljCYuTL7hc4Xmp%2BgSpcayylvz3LUMzi4q3IqGgDjnlvma1X17WnKGvtAiDQ0c1atzy%2Fq6EFWROodE03Qx9MoMhe487xK%2BEHzC%2FT2hDY9D3IOX6EXrhoJ7es1MNUwRpJQgfM7HJuLHxDJP&X-Amz-Signature=d4577364f7c834f9841bf058612146420fdd03329f10633b99c07813b922b762&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4Y3XFP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3HzS0z8ctX%2Fh%2FIQ4tCKpJalgrcta89MHiy2LY0eqJgIhAPX3PcpqXSaKLp1Y8hJApqQbJh5PQGttAn5SoBFxEotBKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuuxU3PmAZJ0g4tuwq3APPq0tvIcgtrhAWuHSIMb5EkvifhyjbFyDyh%2BugU96C3cStU8MExSIrl0PTDr4lRLl7S0wMD%2FAwTj2w2IqHVK6TnBUqZHxHygS9uZ5idvylqgKg3ygldVgEECJYTcLw8YNUOr17XHn4Pw1XX%2FCKF%2FxwUgsx1eKwGKVrc9xJ%2BoM%2FL0iz2jyqaxL3%2F7tlyJcaf%2BIg7l6VgFstwlJI8h6x4uhHzqW77xLKd%2FwL60Honys68fHwt7MeWFFJ8UL%2B%2FDP7%2B6zelPY4bvgM3lt0yzITziqp8n1sqllv%2BmuA0yxU73d7CyRxwmdLYuYFSPqemsxG1GS2mI78DLoSz0vBtXAQYnLnQodhWVKYb7xBzK07yXEB5ZE8hx7KqPNRbQ9qnui%2BQPvikLio82k1xUdiBET0kz6%2FrWXsPx7aeK%2BzBB2vo4ME3hh4fkMLXuFauqSgBGGHWHN%2B0btke656jGK0aFCD3GQKHEwPVSGkt01kGq7e6D0pTwSGoLFeS9ZAJvSqhlIgtj%2BBW0lWQvRhozlas31x8baPkxnRQOziAZYjQ65I2RFanurfeks7AXtBTJB75ddpG7VWE%2B8aKm1%2FJshj5SB9Mwo3rOWg%2FcBN5Abpx%2Fmrn9GTj3RFbvQ59NFpfIxmYTCu0PC8BjqkAYu1aYRddGFBFvKIl%2Fid80VFcPvWFibCDTNzp%2BsDy5Ox53mcGBzazkbfMv4gg%2B1KRUtMrdSAjqfeTh5ljCYuTL7hc4Xmp%2BgSpcayylvz3LUMzi4q3IqGgDjnlvma1X17WnKGvtAiDQ0c1atzy%2Fq6EFWROodE03Qx9MoMhe487xK%2BEHzC%2FT2hDY9D3IOX6EXrhoJ7es1MNUwRpJQgfM7HJuLHxDJP&X-Amz-Signature=7f50a9288fb819fe983a47e8a48189c927a9528ea2b257be6d49bf53c584c166&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULA5SK24%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDHu84se4STp3Yf2hn%2Fged5GTAN%2FnuXKHrEitb8OYxkoAiEA6rmyhzOwHk0qy%2BmjMrf9JrTQZwWz07AXjkunSS9a9LsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN19gOA5sWvY6kQ%2BMCrcAxEi8GscYoXgn86HGZp%2B9iexDAgl0Wc7kgyIoRyU4MIsGlVPir8%2BS2mkQLQQVLmEKmf%2B7dgEGgVvNvj6A2aRshcbyCRK56DLgL8BV7R7A0sGjEmwSWM9K0F02ol1zvjmuqEwUwflm8BEZgdyrFkhZLTMhVmU8Y6xNEHMsgPygEzyI2MAoS2ga6WpopIQYfb2lVqHm9by5yAiWsgk8C%2FNKlJcgAlF2bBkYdT8KMsdnvjeRWCo%2FsaB3iM1RPsUvlDGDjxFErT%2BB78aBM%2BhQmgRPN4fCL3CCeWiR5rLg8UHGrZupK6OFgAtK49F6%2B4a8uOkDMueLBOoGpVBntElQ2pZZPOkED%2By4TYjz3dUcQ%2BTwT644n1ODDNCKB6gLi%2FhB5IBKnDwurLxCxBmDskQrUZVSgNCegNVKUMD0ps3AW1FA5mu5M7Jp4SrS2tZ5Ma8q4FAAV8X2ROPfHALpLmcHwkXddXamaMcO0SVgunIKZR5uysLQX5bkkVMoRoWBF2mELi5Wz7HfYvkkYN7ZwSfQaUm3FHfrw%2FxP3uA%2BH9%2FQ%2BRjKhlk4%2FVkPi48J3vKJuZRsZu9%2Bb%2B9NUSpnPFvAL3QX4lqux4cRaSWaleDUv1dHsj3jV0MIf7wp1VQVZFtP2zFMLjQ8LwGOqUBzylHZuGpCZaRwt2thSzGWxAbc6LifNrWb2NuzRuCxE%2Fza9mRphjC5OE0cIlYNoGx5jSZHInCHTCdTEqC4o0Ur9Rp6oNlfVeOrsSqMHKxmovy%2FEOcgC9RVH85yL8JMXUIPsg%2Fb7k9nnIiyzYl6DOUvkbde5ZHiXmsDA5Da18XpxWjivQ8VLDHnvOuTZXgwOy3txaFbaZBHMk1uSPRA5A88%2BL02TVN&X-Amz-Signature=58a17ed9885b8e6ebb51a42f899f7827e219a5b98125ac33023253341c45be02&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOW62EV3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCipfVVlJLiTl8WhtHzPwUUwNXCtZb9Dc%2FX9Z1ufHorJgIgPwQRbDqzl9J3hhzxqxmJpRxclVqou36E3EU5ijz4gpwqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB8yy1lnkgo%2BrKY7%2BCrcAwlYfYhIftSNQTkr7gnofDLh%2FhCAkd8lSjZfqx2CF5wgRR5hz8QQtRBrovArXroFQ765ALZl%2B1dElf4bXZrg4tU9TF1tMn%2FOKbg443%2BPDw55etJvxFwScRp12ALeQqNMWU4rfeoVgOjJl0ihT%2FpzckMaRir8r3rMc13q3GJM3T1Tu2dLR%2BLMOR4PxvAXxqqf1oc%2FhP2H30nNMbBt%2BtJ8nt%2B1tzNp3XRKcUHFtplVKRe%2Bgbxy6HAW%2F%2FRAKAykKzDYtjYK9JIiIh9ByNVItKRZWVC2jx9mB0ZdmBZ5SlvtOfH%2FfnDnXUMHJVRE9KqHaDJG41haMzz4J%2B1NO4oBaLgeVnK6sKUuYt6xR%2BTILaWwpC6Dx59CmcnZovKOYIcs9olKNgFka5bhMk3tidEJ7M304LPrIczJRYYyd99P%2BtCkgv%2BymOQFWYT7HYFMCTgSVappkcPYZPbiqZ51fs%2FbKA%2Bnl6HLPn34DvHrzFAFcbxZcNlKh%2FYegmWgobYR9fWOsFJgsHcv5rjqAfcznzvWYa4tux0L81SN5jG3r66DHOCazPkXQ7Y7wEXyiFVXvD5lXAOv4mJUFlabTCF40o%2FI2GMjosHjcD0SCqYj3usR46ihSdLoMBdsFc%2B6vxLKGRXzMLnQ8LwGOqUBAeflWJAyf3dgCSvAHXhZ4WyWNSZ6%2FPyPZiuGOR6jtTadT7sB37bFB10GUfw9PRF3kKG6BWcwMTUxVVBBu0QTeFsYnh1QrN5onzCJgb3linKfb8bNp9lZ56hR6jKyCOOGIeDn9rCo%2BTzoFp4FzlpNoKuMyab1zhUaifde6WR9eNblSWiw4y9aPwH5OhuYti25WaA2vlCqlNnCWfRW4GI1XnB3usZB&X-Amz-Signature=1fb20006f24f5cd67fc96f9db22f4242b66387942fa8c1152c0c08ee4c5e4f4b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXEATT43%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLz%2BLHBGXKCvJplzKDbtbzGnjlgmrZpdgIjUeSRh8qPgIhAJwvYMZOys5cNlQKe%2BoYvwCrx184R0ySoAJOPgufBJW6KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1Yqy%2FftgK%2BbncKJoq3APRgUmpwCmk2JbmftgQCLVMXywUHWbpSa5TyZoLa%2BsvIQseIMitZwcW3yFb4ybC4lu1fW4A0kfyByUroAiXywn5dwc4ZWW4Zb31YaWuE2VVcxS5%2BecN2tZQGQpCOv33If56tcm38E5dyb4Y9aHgWmI4y0gS2qnI5wuKiG7dnaTNw1jlOyfgVO6nj3yH5p3m7gj7z35MIyWpH7%2B%2F2AFU2gNJgMtdocSHLGThPHTfGb8oPsDadhEsnV%2B%2F9R6G8NQqvHDa1oBaCSNSuC78TQqiZdqT5JpMTytB1W4g4xbZCebGzVZMXCx91J3hxpQ5NQH4I3LO5L6RiAYzzzHNiprQ5SMvoeKyim%2FGJCXt9ou8p4YJ9SVrl2BetCBKlKtHIax8qkkR5ezu%2FoMcMPns4JsKpG5phXzPjC%2BoMKt0O1qmxl7hc%2BXikbjydMuEZ5WBQZbvqWWApUi4vSvzaYuSASxpR2gMbLux5q833BDS%2BdH3poKIkmxRWz9AVCNrnIsk1vnsSNAYQ3twSJwhp2c3CYqR%2B8VOUskt08Dc%2FicUOrxBzoKHstgFHcApe7WttcCwAn1HVN%2F30tdeRgZrcvU1BolG28E%2B4xktwFiA%2FgOxOwOU09IXHfj7VHX0kAiQ%2FMV45zDj0PC8BjqkAWwebxVQtzdrjt4bRuElDrCm%2B8YUO%2FuDs6vGWjILtUOG6JtmNVXpxFmY88Zcf7MQ9K2LKWhMG3cJcjgy5gTnWyl3DzMd1GFXCqLiAX%2B9b53uTbKi1rYIjH17VRq%2Bvg7f0b%2BHZeh%2FiqHZFddQbM89sxtBuBe8bn6NiYA3OSzfS6VMVLhCf4n7kbI5TvPvenvMpOH9MnWE%2Fw%2BhjHn5k3vGB%2BqxDnm3&X-Amz-Signature=43b4bd76f31b4c870a5c228d27cef97f833fc66b62e7454ca94a392660d9179f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZITOCURP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHaOS7X9P9NUqH9uRGY4c0m2ngBYPjb3RKtIuNooWBzgIgJ%2B8%2FKuU5nXkPMimp2v0QGWi19TybmVqYMm74UF7wVFoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaa333lSMFCz3BbzCrcA7N42ZeC9BOqegH5XmU9E5hpQs7LbqeHEM%2BzT7ToJ3n8m7Q%2BD0Y3gyv3%2B9G5HNVNGoMx2kfSHvXgpQsOKFMiaGEUxKDP%2F8Zf1SpUHUiRU2yhiBGq3U%2Fp2TvKQeJD7ZcEepx%2BZDh4ovqhlaKSWwrzjYGN3DvNcNpSh7jZiZDA2YNbKRUxw7W1V9x5K5IhmiIfTR6p2q25PBvyMXiCcRCmdoWuu96WgOdid7BosdfOik3DEa91CsLgWor8oX8E1LTcVNWyoB4BhPp8UOrR6Og6t2GTrEGUR9PUWsG%2BNCtCP7L25w6XFyz1TLH7GK4PtVLHH7TcthvDIE0pB3bqJY5ir4qtjX1VvNQHp21t3eGyAC446d9TlDUjqehfg1fOKPUmT7fuwI7KT0hdfT0t4xf17SkSPrnuyDwpD9%2Fq%2BVa%2BZmyFaB5PR343KhiUyPkF84ELPmONkBjOE5ofz2AxSteMYNsrlgrJwjeDiqvH3U7yrAlfI8BBT6s8OW%2FouqHuCFpQwSU%2FksfFqbTOef3o6ycscY2%2BR0MoKuwCrRw0awcmtvTf4jP5NCVWZiPgc%2BWqU%2BljILxzl9qg%2B9EaKXGOgBJk%2FGrqGjSbzOV9zZs%2Fm1FuiFrlPBoVWQE%2ByqwLv40FMOLQ8LwGOqUBDxFBFFa1sffyCYCU%2FdBLWYNWrRWJbno86%2B7sh9xOA5TAojx4kPgFEse8re6OMWrdRz8YsLjqh6SAb2tV1mbvXO0Cyu%2FwRUYdByGGGetZdA707a5KgMjdRWenEx4Fla%2FuzlUAlYJIvlxnJF4gnbHozC3efrPy4f3%2BgyV71dxhtwW7iMw8VtWyp3q68Dq8DIQ41L2%2Fbr0lsV4ZzvNIT7hxRrwS4NXi&X-Amz-Signature=c1198334fb6467c1e254a648ffcf2bc69342e0afb11b04a9fe09199ea22f4711&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZITOCURP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHaOS7X9P9NUqH9uRGY4c0m2ngBYPjb3RKtIuNooWBzgIgJ%2B8%2FKuU5nXkPMimp2v0QGWi19TybmVqYMm74UF7wVFoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNaa333lSMFCz3BbzCrcA7N42ZeC9BOqegH5XmU9E5hpQs7LbqeHEM%2BzT7ToJ3n8m7Q%2BD0Y3gyv3%2B9G5HNVNGoMx2kfSHvXgpQsOKFMiaGEUxKDP%2F8Zf1SpUHUiRU2yhiBGq3U%2Fp2TvKQeJD7ZcEepx%2BZDh4ovqhlaKSWwrzjYGN3DvNcNpSh7jZiZDA2YNbKRUxw7W1V9x5K5IhmiIfTR6p2q25PBvyMXiCcRCmdoWuu96WgOdid7BosdfOik3DEa91CsLgWor8oX8E1LTcVNWyoB4BhPp8UOrR6Og6t2GTrEGUR9PUWsG%2BNCtCP7L25w6XFyz1TLH7GK4PtVLHH7TcthvDIE0pB3bqJY5ir4qtjX1VvNQHp21t3eGyAC446d9TlDUjqehfg1fOKPUmT7fuwI7KT0hdfT0t4xf17SkSPrnuyDwpD9%2Fq%2BVa%2BZmyFaB5PR343KhiUyPkF84ELPmONkBjOE5ofz2AxSteMYNsrlgrJwjeDiqvH3U7yrAlfI8BBT6s8OW%2FouqHuCFpQwSU%2FksfFqbTOef3o6ycscY2%2BR0MoKuwCrRw0awcmtvTf4jP5NCVWZiPgc%2BWqU%2BljILxzl9qg%2B9EaKXGOgBJk%2FGrqGjSbzOV9zZs%2Fm1FuiFrlPBoVWQE%2ByqwLv40FMOLQ8LwGOqUBDxFBFFa1sffyCYCU%2FdBLWYNWrRWJbno86%2B7sh9xOA5TAojx4kPgFEse8re6OMWrdRz8YsLjqh6SAb2tV1mbvXO0Cyu%2FwRUYdByGGGetZdA707a5KgMjdRWenEx4Fla%2FuzlUAlYJIvlxnJF4gnbHozC3efrPy4f3%2BgyV71dxhtwW7iMw8VtWyp3q68Dq8DIQ41L2%2Fbr0lsV4ZzvNIT7hxRrwS4NXi&X-Amz-Signature=ad60d23a9589c8b98485a66c00f6d0495371f3c74037f97b6e5c63fa4b498f0b&X-Amz-SignedHeaders=host&x-id=GetObject)

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
