

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZROXBZV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCDDkwZyrkQ8qBbBGZMpd5ToR5EbUBVpYq%2BaAB2DS0N5QIhAMDGZ4%2F%2FdKeyViOj%2Bm3YP6uHPDDXMfLmizg%2B6U46bkA6KogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQQqxAx8eKfFEnVZQq3APyh4cZNrDN%2BbfEAQDrqL23%2BvMbJ5pJWHUUJQ3yxddIBfRcCOF%2B2sosP6isjG16yc2ANw0V9lflYl%2BoyZQl%2F26vKU50B%2B87aTpVMYO6KkzQGw04h7FH6yJ1lnRBvbTe%2B0iCJ3ICmui9UVZkD7bH0BsdruDgQipXvRFeZsDJH0N4pzQt8floRY7GPvXayNAU5crcbOXfJtBi3Q8KcfMPNHQDLLpf2j3ttgrkOnH%2BFBSXjdyGgK1bBRtFV5MUamGsNZk%2FSTA2tbOe%2Bo5BXCwDWfZeB8otOgxUU1R5sXkQpnb2I7yeRORnz9pw4ouK4onQ7Ir%2FEWCw%2B9ZzmPGxC26W5CsWHq5WmLyl6Q%2BNkNFmRAv2DKe1N9uYED4gZ4luJ13F6VhJX%2BbDjRKNpRzMbEMVLdGMMIuFIm285uVGVRdDhyV%2BFKrgziF0kNjJ8BcoOkvOjVMjJvCgbAnfVyU8vhzwXFwGZhY%2Bd%2Bk%2BR1lV0YrQNv2BT3bF4%2FEErrKbZagucHR1ILTtoqe8RUKsveIC5M%2FEq%2BtkOvT4YLaDmoJdVNJMjVpdtW5G99mmhd4fq%2Fgkc6%2BanGOBpMMpYRBCe4kOeaGyS9mP2n9moijMpSvycBsrKUcNl0W9aIE9deG3dflWNDD%2B2vS8BjqkARIJYVlT%2Bj05MJW2Ks3EeMplfc73q7PLDNIKiUglNGhngvPjIB%2BmwLZwtFEbElduuDxwWpmJyedb5HOwdMkg4ayysY1peToqboHfKVW%2FhyyONIjnL5q2Bag7hIWMqe7mp56Aq55TG9MAGxv3xvnrYfxcOB89clhGgUZjjWkFR2QzRO%2F8RR%2BgVYmL5hM4IXd5ZCz%2Fj8adb%2BGt313SDkoEzo84Ya8T&X-Amz-Signature=3762389437afbd13cfe1c71c77c80701da57da0a923cb4edc16200b569b884d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZROXBZV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCDDkwZyrkQ8qBbBGZMpd5ToR5EbUBVpYq%2BaAB2DS0N5QIhAMDGZ4%2F%2FdKeyViOj%2Bm3YP6uHPDDXMfLmizg%2B6U46bkA6KogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQQqxAx8eKfFEnVZQq3APyh4cZNrDN%2BbfEAQDrqL23%2BvMbJ5pJWHUUJQ3yxddIBfRcCOF%2B2sosP6isjG16yc2ANw0V9lflYl%2BoyZQl%2F26vKU50B%2B87aTpVMYO6KkzQGw04h7FH6yJ1lnRBvbTe%2B0iCJ3ICmui9UVZkD7bH0BsdruDgQipXvRFeZsDJH0N4pzQt8floRY7GPvXayNAU5crcbOXfJtBi3Q8KcfMPNHQDLLpf2j3ttgrkOnH%2BFBSXjdyGgK1bBRtFV5MUamGsNZk%2FSTA2tbOe%2Bo5BXCwDWfZeB8otOgxUU1R5sXkQpnb2I7yeRORnz9pw4ouK4onQ7Ir%2FEWCw%2B9ZzmPGxC26W5CsWHq5WmLyl6Q%2BNkNFmRAv2DKe1N9uYED4gZ4luJ13F6VhJX%2BbDjRKNpRzMbEMVLdGMMIuFIm285uVGVRdDhyV%2BFKrgziF0kNjJ8BcoOkvOjVMjJvCgbAnfVyU8vhzwXFwGZhY%2Bd%2Bk%2BR1lV0YrQNv2BT3bF4%2FEErrKbZagucHR1ILTtoqe8RUKsveIC5M%2FEq%2BtkOvT4YLaDmoJdVNJMjVpdtW5G99mmhd4fq%2Fgkc6%2BanGOBpMMpYRBCe4kOeaGyS9mP2n9moijMpSvycBsrKUcNl0W9aIE9deG3dflWNDD%2B2vS8BjqkARIJYVlT%2Bj05MJW2Ks3EeMplfc73q7PLDNIKiUglNGhngvPjIB%2BmwLZwtFEbElduuDxwWpmJyedb5HOwdMkg4ayysY1peToqboHfKVW%2FhyyONIjnL5q2Bag7hIWMqe7mp56Aq55TG9MAGxv3xvnrYfxcOB89clhGgUZjjWkFR2QzRO%2F8RR%2BgVYmL5hM4IXd5ZCz%2Fj8adb%2BGt313SDkoEzo84Ya8T&X-Amz-Signature=6e36e6114790a3e303f96c5f522d49ab49f8d5f0b8f361f084d85e1ae43c1849&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZROXBZV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCDDkwZyrkQ8qBbBGZMpd5ToR5EbUBVpYq%2BaAB2DS0N5QIhAMDGZ4%2F%2FdKeyViOj%2Bm3YP6uHPDDXMfLmizg%2B6U46bkA6KogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQQqxAx8eKfFEnVZQq3APyh4cZNrDN%2BbfEAQDrqL23%2BvMbJ5pJWHUUJQ3yxddIBfRcCOF%2B2sosP6isjG16yc2ANw0V9lflYl%2BoyZQl%2F26vKU50B%2B87aTpVMYO6KkzQGw04h7FH6yJ1lnRBvbTe%2B0iCJ3ICmui9UVZkD7bH0BsdruDgQipXvRFeZsDJH0N4pzQt8floRY7GPvXayNAU5crcbOXfJtBi3Q8KcfMPNHQDLLpf2j3ttgrkOnH%2BFBSXjdyGgK1bBRtFV5MUamGsNZk%2FSTA2tbOe%2Bo5BXCwDWfZeB8otOgxUU1R5sXkQpnb2I7yeRORnz9pw4ouK4onQ7Ir%2FEWCw%2B9ZzmPGxC26W5CsWHq5WmLyl6Q%2BNkNFmRAv2DKe1N9uYED4gZ4luJ13F6VhJX%2BbDjRKNpRzMbEMVLdGMMIuFIm285uVGVRdDhyV%2BFKrgziF0kNjJ8BcoOkvOjVMjJvCgbAnfVyU8vhzwXFwGZhY%2Bd%2Bk%2BR1lV0YrQNv2BT3bF4%2FEErrKbZagucHR1ILTtoqe8RUKsveIC5M%2FEq%2BtkOvT4YLaDmoJdVNJMjVpdtW5G99mmhd4fq%2Fgkc6%2BanGOBpMMpYRBCe4kOeaGyS9mP2n9moijMpSvycBsrKUcNl0W9aIE9deG3dflWNDD%2B2vS8BjqkARIJYVlT%2Bj05MJW2Ks3EeMplfc73q7PLDNIKiUglNGhngvPjIB%2BmwLZwtFEbElduuDxwWpmJyedb5HOwdMkg4ayysY1peToqboHfKVW%2FhyyONIjnL5q2Bag7hIWMqe7mp56Aq55TG9MAGxv3xvnrYfxcOB89clhGgUZjjWkFR2QzRO%2F8RR%2BgVYmL5hM4IXd5ZCz%2Fj8adb%2BGt313SDkoEzo84Ya8T&X-Amz-Signature=d1954efb65fcbc129441ba9df9b06cdba287e0694363fd62966275090fb14ca2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A4ODINV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Fstunl4n1SCJkQS0HHj0Wqt2K7HN43KAeDkRRps4IuAiEAtiBgu5ECfIG%2FVl%2F6NL2Bz3Se2jsf2S7jd0EeZORGHTYqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ0pemvVDKjyN6plmircA3nStuP1P94%2BBOfwXDvs%2BUzJjwKszEcU3yOhDjNEtAWju%2FQE7suNKhiN4QTsV2MwMQjRYOhiJUPjK7zmZWDPe3n6lKuQ81YrDSwOWZsbIvxBiey6VFCg2ZL4DDRGvkaiKRlVhv6RsOVZQrCWcB2mW1aEBnolukD3U7j%2Bc2tu6m4W6WEQS3ioQOhuvcRXftBV0mWrBRtKt1cSoD30SXrqivOskxJek4nYxa4cuLhu9SQ27K7DEVo%2F0rgsL59NZkUEolZ9ovHMD4deiOOKTAe4rkDYIxw8BkT7LECl8%2Bif3T54CG9XIoPoYE%2FFs6C%2BSwTQkaSBHR%2FriQWuLLXgbnl%2FOEvxJ85%2B3PUJ%2FyM6uPq8azd5AkDb7Ocslgnmh%2BWfDAUfobcdPdzxMHT5FwqTfxKfX13Gg4MTnnX%2BH39NXV2FmObGuuVNEchs48mObiJvG6cA5lqhOHtVYVvncNZMFL1HTfEdAE%2FzRT3ZVsXGcFbkVEDNiJBZVOffho%2BDJ0reeF3c2LwY25Gr1SwoSZRduddhpQIWa9rB8XzV93F8tRdZQVve24%2Fs%2FnWcPS3BfEGJEIXDq0KxeN6T8N9qUDrHbF9j%2BMfFevnokmBoPmUkMJJGR8CT9Nfac1j3RwfOMVneMKXb9LwGOqUBZKZKjPofibCzBh546cWGQfhKA2T%2FeAHUpPHZ0wjQwTT09KX%2BZYixxg85NDoPwODLzydQhdt8sYblRHsKQt6ClfTSmWMtdMaHOuGuhP8DZ8YUuP0tG8AdIjLrg0aqs520MG8p2vbiKm1tiD5CUwPsghP%2BIX519D7tzXRRjtSjHCwTMTd6uNHvO7Iv1FYueD%2BpputFKyTdYJteEdgwgzPDWqDWEotQ&X-Amz-Signature=69d116ef17aa8a193455c345b27f253983e1d2266f666c290d006a75bb5897b8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A4ODINV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Fstunl4n1SCJkQS0HHj0Wqt2K7HN43KAeDkRRps4IuAiEAtiBgu5ECfIG%2FVl%2F6NL2Bz3Se2jsf2S7jd0EeZORGHTYqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ0pemvVDKjyN6plmircA3nStuP1P94%2BBOfwXDvs%2BUzJjwKszEcU3yOhDjNEtAWju%2FQE7suNKhiN4QTsV2MwMQjRYOhiJUPjK7zmZWDPe3n6lKuQ81YrDSwOWZsbIvxBiey6VFCg2ZL4DDRGvkaiKRlVhv6RsOVZQrCWcB2mW1aEBnolukD3U7j%2Bc2tu6m4W6WEQS3ioQOhuvcRXftBV0mWrBRtKt1cSoD30SXrqivOskxJek4nYxa4cuLhu9SQ27K7DEVo%2F0rgsL59NZkUEolZ9ovHMD4deiOOKTAe4rkDYIxw8BkT7LECl8%2Bif3T54CG9XIoPoYE%2FFs6C%2BSwTQkaSBHR%2FriQWuLLXgbnl%2FOEvxJ85%2B3PUJ%2FyM6uPq8azd5AkDb7Ocslgnmh%2BWfDAUfobcdPdzxMHT5FwqTfxKfX13Gg4MTnnX%2BH39NXV2FmObGuuVNEchs48mObiJvG6cA5lqhOHtVYVvncNZMFL1HTfEdAE%2FzRT3ZVsXGcFbkVEDNiJBZVOffho%2BDJ0reeF3c2LwY25Gr1SwoSZRduddhpQIWa9rB8XzV93F8tRdZQVve24%2Fs%2FnWcPS3BfEGJEIXDq0KxeN6T8N9qUDrHbF9j%2BMfFevnokmBoPmUkMJJGR8CT9Nfac1j3RwfOMVneMKXb9LwGOqUBZKZKjPofibCzBh546cWGQfhKA2T%2FeAHUpPHZ0wjQwTT09KX%2BZYixxg85NDoPwODLzydQhdt8sYblRHsKQt6ClfTSmWMtdMaHOuGuhP8DZ8YUuP0tG8AdIjLrg0aqs520MG8p2vbiKm1tiD5CUwPsghP%2BIX519D7tzXRRjtSjHCwTMTd6uNHvO7Iv1FYueD%2BpputFKyTdYJteEdgwgzPDWqDWEotQ&X-Amz-Signature=e3501710e4e27c528f155cacb4bda827878fdc1df47e0d7c3869ec0eb208761f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A4ODINV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Fstunl4n1SCJkQS0HHj0Wqt2K7HN43KAeDkRRps4IuAiEAtiBgu5ECfIG%2FVl%2F6NL2Bz3Se2jsf2S7jd0EeZORGHTYqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ0pemvVDKjyN6plmircA3nStuP1P94%2BBOfwXDvs%2BUzJjwKszEcU3yOhDjNEtAWju%2FQE7suNKhiN4QTsV2MwMQjRYOhiJUPjK7zmZWDPe3n6lKuQ81YrDSwOWZsbIvxBiey6VFCg2ZL4DDRGvkaiKRlVhv6RsOVZQrCWcB2mW1aEBnolukD3U7j%2Bc2tu6m4W6WEQS3ioQOhuvcRXftBV0mWrBRtKt1cSoD30SXrqivOskxJek4nYxa4cuLhu9SQ27K7DEVo%2F0rgsL59NZkUEolZ9ovHMD4deiOOKTAe4rkDYIxw8BkT7LECl8%2Bif3T54CG9XIoPoYE%2FFs6C%2BSwTQkaSBHR%2FriQWuLLXgbnl%2FOEvxJ85%2B3PUJ%2FyM6uPq8azd5AkDb7Ocslgnmh%2BWfDAUfobcdPdzxMHT5FwqTfxKfX13Gg4MTnnX%2BH39NXV2FmObGuuVNEchs48mObiJvG6cA5lqhOHtVYVvncNZMFL1HTfEdAE%2FzRT3ZVsXGcFbkVEDNiJBZVOffho%2BDJ0reeF3c2LwY25Gr1SwoSZRduddhpQIWa9rB8XzV93F8tRdZQVve24%2Fs%2FnWcPS3BfEGJEIXDq0KxeN6T8N9qUDrHbF9j%2BMfFevnokmBoPmUkMJJGR8CT9Nfac1j3RwfOMVneMKXb9LwGOqUBZKZKjPofibCzBh546cWGQfhKA2T%2FeAHUpPHZ0wjQwTT09KX%2BZYixxg85NDoPwODLzydQhdt8sYblRHsKQt6ClfTSmWMtdMaHOuGuhP8DZ8YUuP0tG8AdIjLrg0aqs520MG8p2vbiKm1tiD5CUwPsghP%2BIX519D7tzXRRjtSjHCwTMTd6uNHvO7Iv1FYueD%2BpputFKyTdYJteEdgwgzPDWqDWEotQ&X-Amz-Signature=6f8f6bb3012940f5a24300704ebb760c2a01c40cef96e1e8f42871672c475d95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A4ODINV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Fstunl4n1SCJkQS0HHj0Wqt2K7HN43KAeDkRRps4IuAiEAtiBgu5ECfIG%2FVl%2F6NL2Bz3Se2jsf2S7jd0EeZORGHTYqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ0pemvVDKjyN6plmircA3nStuP1P94%2BBOfwXDvs%2BUzJjwKszEcU3yOhDjNEtAWju%2FQE7suNKhiN4QTsV2MwMQjRYOhiJUPjK7zmZWDPe3n6lKuQ81YrDSwOWZsbIvxBiey6VFCg2ZL4DDRGvkaiKRlVhv6RsOVZQrCWcB2mW1aEBnolukD3U7j%2Bc2tu6m4W6WEQS3ioQOhuvcRXftBV0mWrBRtKt1cSoD30SXrqivOskxJek4nYxa4cuLhu9SQ27K7DEVo%2F0rgsL59NZkUEolZ9ovHMD4deiOOKTAe4rkDYIxw8BkT7LECl8%2Bif3T54CG9XIoPoYE%2FFs6C%2BSwTQkaSBHR%2FriQWuLLXgbnl%2FOEvxJ85%2B3PUJ%2FyM6uPq8azd5AkDb7Ocslgnmh%2BWfDAUfobcdPdzxMHT5FwqTfxKfX13Gg4MTnnX%2BH39NXV2FmObGuuVNEchs48mObiJvG6cA5lqhOHtVYVvncNZMFL1HTfEdAE%2FzRT3ZVsXGcFbkVEDNiJBZVOffho%2BDJ0reeF3c2LwY25Gr1SwoSZRduddhpQIWa9rB8XzV93F8tRdZQVve24%2Fs%2FnWcPS3BfEGJEIXDq0KxeN6T8N9qUDrHbF9j%2BMfFevnokmBoPmUkMJJGR8CT9Nfac1j3RwfOMVneMKXb9LwGOqUBZKZKjPofibCzBh546cWGQfhKA2T%2FeAHUpPHZ0wjQwTT09KX%2BZYixxg85NDoPwODLzydQhdt8sYblRHsKQt6ClfTSmWMtdMaHOuGuhP8DZ8YUuP0tG8AdIjLrg0aqs520MG8p2vbiKm1tiD5CUwPsghP%2BIX519D7tzXRRjtSjHCwTMTd6uNHvO7Iv1FYueD%2BpputFKyTdYJteEdgwgzPDWqDWEotQ&X-Amz-Signature=cf16c88d4fa1b051db1579434354126bedc04c41e0e9832cdece3dfa58bcf94d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A4ODINV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Fstunl4n1SCJkQS0HHj0Wqt2K7HN43KAeDkRRps4IuAiEAtiBgu5ECfIG%2FVl%2F6NL2Bz3Se2jsf2S7jd0EeZORGHTYqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ0pemvVDKjyN6plmircA3nStuP1P94%2BBOfwXDvs%2BUzJjwKszEcU3yOhDjNEtAWju%2FQE7suNKhiN4QTsV2MwMQjRYOhiJUPjK7zmZWDPe3n6lKuQ81YrDSwOWZsbIvxBiey6VFCg2ZL4DDRGvkaiKRlVhv6RsOVZQrCWcB2mW1aEBnolukD3U7j%2Bc2tu6m4W6WEQS3ioQOhuvcRXftBV0mWrBRtKt1cSoD30SXrqivOskxJek4nYxa4cuLhu9SQ27K7DEVo%2F0rgsL59NZkUEolZ9ovHMD4deiOOKTAe4rkDYIxw8BkT7LECl8%2Bif3T54CG9XIoPoYE%2FFs6C%2BSwTQkaSBHR%2FriQWuLLXgbnl%2FOEvxJ85%2B3PUJ%2FyM6uPq8azd5AkDb7Ocslgnmh%2BWfDAUfobcdPdzxMHT5FwqTfxKfX13Gg4MTnnX%2BH39NXV2FmObGuuVNEchs48mObiJvG6cA5lqhOHtVYVvncNZMFL1HTfEdAE%2FzRT3ZVsXGcFbkVEDNiJBZVOffho%2BDJ0reeF3c2LwY25Gr1SwoSZRduddhpQIWa9rB8XzV93F8tRdZQVve24%2Fs%2FnWcPS3BfEGJEIXDq0KxeN6T8N9qUDrHbF9j%2BMfFevnokmBoPmUkMJJGR8CT9Nfac1j3RwfOMVneMKXb9LwGOqUBZKZKjPofibCzBh546cWGQfhKA2T%2FeAHUpPHZ0wjQwTT09KX%2BZYixxg85NDoPwODLzydQhdt8sYblRHsKQt6ClfTSmWMtdMaHOuGuhP8DZ8YUuP0tG8AdIjLrg0aqs520MG8p2vbiKm1tiD5CUwPsghP%2BIX519D7tzXRRjtSjHCwTMTd6uNHvO7Iv1FYueD%2BpputFKyTdYJteEdgwgzPDWqDWEotQ&X-Amz-Signature=555f9cf410e9f39fd02be403cd7e4d9564967991811c6895ed828e75a883c2dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A4ODINV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Fstunl4n1SCJkQS0HHj0Wqt2K7HN43KAeDkRRps4IuAiEAtiBgu5ECfIG%2FVl%2F6NL2Bz3Se2jsf2S7jd0EeZORGHTYqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ0pemvVDKjyN6plmircA3nStuP1P94%2BBOfwXDvs%2BUzJjwKszEcU3yOhDjNEtAWju%2FQE7suNKhiN4QTsV2MwMQjRYOhiJUPjK7zmZWDPe3n6lKuQ81YrDSwOWZsbIvxBiey6VFCg2ZL4DDRGvkaiKRlVhv6RsOVZQrCWcB2mW1aEBnolukD3U7j%2Bc2tu6m4W6WEQS3ioQOhuvcRXftBV0mWrBRtKt1cSoD30SXrqivOskxJek4nYxa4cuLhu9SQ27K7DEVo%2F0rgsL59NZkUEolZ9ovHMD4deiOOKTAe4rkDYIxw8BkT7LECl8%2Bif3T54CG9XIoPoYE%2FFs6C%2BSwTQkaSBHR%2FriQWuLLXgbnl%2FOEvxJ85%2B3PUJ%2FyM6uPq8azd5AkDb7Ocslgnmh%2BWfDAUfobcdPdzxMHT5FwqTfxKfX13Gg4MTnnX%2BH39NXV2FmObGuuVNEchs48mObiJvG6cA5lqhOHtVYVvncNZMFL1HTfEdAE%2FzRT3ZVsXGcFbkVEDNiJBZVOffho%2BDJ0reeF3c2LwY25Gr1SwoSZRduddhpQIWa9rB8XzV93F8tRdZQVve24%2Fs%2FnWcPS3BfEGJEIXDq0KxeN6T8N9qUDrHbF9j%2BMfFevnokmBoPmUkMJJGR8CT9Nfac1j3RwfOMVneMKXb9LwGOqUBZKZKjPofibCzBh546cWGQfhKA2T%2FeAHUpPHZ0wjQwTT09KX%2BZYixxg85NDoPwODLzydQhdt8sYblRHsKQt6ClfTSmWMtdMaHOuGuhP8DZ8YUuP0tG8AdIjLrg0aqs520MG8p2vbiKm1tiD5CUwPsghP%2BIX519D7tzXRRjtSjHCwTMTd6uNHvO7Iv1FYueD%2BpputFKyTdYJteEdgwgzPDWqDWEotQ&X-Amz-Signature=0eeb446ef6bd58ee9c1194d3c85d9c13e39c060ffeded111b8243d88fa3e6275&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ5JKZ3Q%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDv1%2BC%2BIpXA%2B9kWyPypTSd3nmHpq6JmBn1VUT%2BL6H%2F30QIgSeybHgFaDuotg7Igam9IBmdIpKbWiPWADrQW0i9VKn4qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFMLg5fBsLUdprrApSrcA%2B6%2FqDKJXXCb0nqzkpihUxqQ23QhbZ75mdydLfHhUbxcoIkLCfHnXfsdXejPg3Jrkyy4RQH%2BU7DCgShUmThFUQai0NjZcLK7omHmi8otv%2BN%2BNSHE8tb1gFaLU9mMKgNCnceU%2BldQ4GRNtlEI20gqoXvW4bAVEqh3KxO4ZkMhldAv%2B%2FZ0TTEARM1E2vmbcVQG89Np%2B785e3VKPQCW7tLiX6imOph4%2Bx032tpOarVSxSSurqiW9upluGAdjJB7YxjnQ75TV23jBaQ16FyoIavZxl2fgek4RSz%2FucnoaTFLpndIK76%2FrHghlWUkktXo8gF9kuHvIZTQCmmm%2FplGQvyQwtyVpfbtKYmIVES5eLkJUAMmujWCVsiC3sWnMudmbVx6vSQhKPmRJ4fDr0DaVDwX2Sl6b7G%2FeaG1o0TPz8i2lBfZShLa%2FFah75QeF6Y05I8ohTcVkm5cFMmbuxjQ1x%2BUg5YoBPcG%2BsYpFFbONeNft1yyLJx9xXFA99EmPZ7JWrNsrLszBQhmF1W4rW3yqiue4sSTkUVUqA39t9XBa9G8mQEIEpipgF2u7%2B%2FCGp1lMLmRw%2FOGkBD%2B7lPKv9BcO2FNnIvgIOya6f5T64LrEcaZVq%2FLndIwt1Tz1q8jhTUcMLnb9LwGOqUBVfMXHEEqcPCv6NKHgsMAXmrkV%2F4r4x8mNXHQeYAcbaMNj7qv6D1fYcVJDP%2FtOutf5YsaSm9EiUEIg8Z5P0jLs2QMaYD9WZlVY%2FePGiNVuHiKKpoL6jV8593pL%2F0u9TZvnC%2BxxSG15WVCVNgWqiaKDVyzk%2BM1iCHMB3ckIhMjk9BxoVZJDR6JfMQldt7h7clA6cWBDA1HseETevv7Rxk%2B%2FqNupn57&X-Amz-Signature=ca997e79a54f16854f365fa0e9b9a7b2623aefb5eb410e60eb4acc57232ed3c1&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBDZEKTO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEOgZTXpD%2BdTaBeSdTU1KLp%2B4imQX%2FHptG6u%2F55pE3T7AiEA9B5vxFnLWC8Hd4zKqn8%2BGbN50dvEDRpUgtRWtdGT%2Bi8qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLGkkOdjYdrc9VJzRSrcAwkYd6j3jGekTJWnP27F%2FJk9YLyINM5ojFVKCD9hq5NH%2FnMyCm2UyWEc1spzSyy9UoVlyBt8x5IyiTQLl1dGXb4%2BEJV6u7MZUAirI7dYmF4cvwagOHmnEMS9dxD2wV42L1qF6iJymK6oqqTc5uj4dXf8jmGg0ib%2BSjTbEAN%2BsGl2mDwX7sj4NsVMAC5jD7NY5NAAreye2OLKKtLyxPuPu4TiGl4txnSdOmzI%2FbJjvD1CV%2BCruVulrqaRZjrJKcC2IFL9E4FVsuToJqASYNMIG0bxI%2BApi4h2ecVmmI2u3iMDsu1qb%2FuX8HnyX9b0AUl2qOaLRPcB7N8cARkyuhsp3pCjRSstyRnGwJs%2BOcrfLjwIcrC2uDEqpQJIGTEM7zKOvEbp4OnaxNaA6HLoPW5LF%2BBA%2B2aIz6TyEKMPLrdEwlSmo0sRoN4%2Bu4wLZfS4yEUmy2hbruhDAJpxZzfNA8RWs3%2FjwU%2FjY7bYkVs1QYd66uszWbkWxev7OHqHQ7SqQ6yZv0%2BuWrYFjOQBbN2RaAlh0x5irzaonKV1anO0uqrWnhU2EcCQrVL3WvuBRlHPHe5f0Jr23PbuEXOX%2FuNHCDhApURH7R1tRD8jyIClzX46rJzjriQM4F2BDn5hkPQBMNbb9LwGOqUBIBgNT4CbdAlTkGK%2F7B%2BCzSkUOjX5%2FkiOIV29ibbR5B0c%2Bc7ZQPnETZFeRvTqoQvt828Znac2oaf%2BdUtP%2FXcWjudo0TPu8rXmFPZKsmfDPvkMWOMC1Z8MEUB%2FRkkq9A%2FIT7E08osab5Qr9JTRCTc51OhKWKtrOv54iXUCYyBDo7r0hmk9f%2BIkv2JPO9qbYaEFbdDFY3J813XaPCJsCIPTCF6OARFe&X-Amz-Signature=7524417841650e0582321d0d204a056af1a64dae07b862d185b230652a97f226&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A4ODINV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Fstunl4n1SCJkQS0HHj0Wqt2K7HN43KAeDkRRps4IuAiEAtiBgu5ECfIG%2FVl%2F6NL2Bz3Se2jsf2S7jd0EeZORGHTYqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ0pemvVDKjyN6plmircA3nStuP1P94%2BBOfwXDvs%2BUzJjwKszEcU3yOhDjNEtAWju%2FQE7suNKhiN4QTsV2MwMQjRYOhiJUPjK7zmZWDPe3n6lKuQ81YrDSwOWZsbIvxBiey6VFCg2ZL4DDRGvkaiKRlVhv6RsOVZQrCWcB2mW1aEBnolukD3U7j%2Bc2tu6m4W6WEQS3ioQOhuvcRXftBV0mWrBRtKt1cSoD30SXrqivOskxJek4nYxa4cuLhu9SQ27K7DEVo%2F0rgsL59NZkUEolZ9ovHMD4deiOOKTAe4rkDYIxw8BkT7LECl8%2Bif3T54CG9XIoPoYE%2FFs6C%2BSwTQkaSBHR%2FriQWuLLXgbnl%2FOEvxJ85%2B3PUJ%2FyM6uPq8azd5AkDb7Ocslgnmh%2BWfDAUfobcdPdzxMHT5FwqTfxKfX13Gg4MTnnX%2BH39NXV2FmObGuuVNEchs48mObiJvG6cA5lqhOHtVYVvncNZMFL1HTfEdAE%2FzRT3ZVsXGcFbkVEDNiJBZVOffho%2BDJ0reeF3c2LwY25Gr1SwoSZRduddhpQIWa9rB8XzV93F8tRdZQVve24%2Fs%2FnWcPS3BfEGJEIXDq0KxeN6T8N9qUDrHbF9j%2BMfFevnokmBoPmUkMJJGR8CT9Nfac1j3RwfOMVneMKXb9LwGOqUBZKZKjPofibCzBh546cWGQfhKA2T%2FeAHUpPHZ0wjQwTT09KX%2BZYixxg85NDoPwODLzydQhdt8sYblRHsKQt6ClfTSmWMtdMaHOuGuhP8DZ8YUuP0tG8AdIjLrg0aqs520MG8p2vbiKm1tiD5CUwPsghP%2BIX519D7tzXRRjtSjHCwTMTd6uNHvO7Iv1FYueD%2BpputFKyTdYJteEdgwgzPDWqDWEotQ&X-Amz-Signature=36ec94ddbd446462177d1d6d8848df6dfbe267511c06eea58cdc8e8c927ae850&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A4ODINV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Fstunl4n1SCJkQS0HHj0Wqt2K7HN43KAeDkRRps4IuAiEAtiBgu5ECfIG%2FVl%2F6NL2Bz3Se2jsf2S7jd0EeZORGHTYqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ0pemvVDKjyN6plmircA3nStuP1P94%2BBOfwXDvs%2BUzJjwKszEcU3yOhDjNEtAWju%2FQE7suNKhiN4QTsV2MwMQjRYOhiJUPjK7zmZWDPe3n6lKuQ81YrDSwOWZsbIvxBiey6VFCg2ZL4DDRGvkaiKRlVhv6RsOVZQrCWcB2mW1aEBnolukD3U7j%2Bc2tu6m4W6WEQS3ioQOhuvcRXftBV0mWrBRtKt1cSoD30SXrqivOskxJek4nYxa4cuLhu9SQ27K7DEVo%2F0rgsL59NZkUEolZ9ovHMD4deiOOKTAe4rkDYIxw8BkT7LECl8%2Bif3T54CG9XIoPoYE%2FFs6C%2BSwTQkaSBHR%2FriQWuLLXgbnl%2FOEvxJ85%2B3PUJ%2FyM6uPq8azd5AkDb7Ocslgnmh%2BWfDAUfobcdPdzxMHT5FwqTfxKfX13Gg4MTnnX%2BH39NXV2FmObGuuVNEchs48mObiJvG6cA5lqhOHtVYVvncNZMFL1HTfEdAE%2FzRT3ZVsXGcFbkVEDNiJBZVOffho%2BDJ0reeF3c2LwY25Gr1SwoSZRduddhpQIWa9rB8XzV93F8tRdZQVve24%2Fs%2FnWcPS3BfEGJEIXDq0KxeN6T8N9qUDrHbF9j%2BMfFevnokmBoPmUkMJJGR8CT9Nfac1j3RwfOMVneMKXb9LwGOqUBZKZKjPofibCzBh546cWGQfhKA2T%2FeAHUpPHZ0wjQwTT09KX%2BZYixxg85NDoPwODLzydQhdt8sYblRHsKQt6ClfTSmWMtdMaHOuGuhP8DZ8YUuP0tG8AdIjLrg0aqs520MG8p2vbiKm1tiD5CUwPsghP%2BIX519D7tzXRRjtSjHCwTMTd6uNHvO7Iv1FYueD%2BpputFKyTdYJteEdgwgzPDWqDWEotQ&X-Amz-Signature=66e974966916ff44f737b36efbdb008fc5702e28e322fcdd74cbac8ba24e4b63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A4ODINV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Fstunl4n1SCJkQS0HHj0Wqt2K7HN43KAeDkRRps4IuAiEAtiBgu5ECfIG%2FVl%2F6NL2Bz3Se2jsf2S7jd0EeZORGHTYqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ0pemvVDKjyN6plmircA3nStuP1P94%2BBOfwXDvs%2BUzJjwKszEcU3yOhDjNEtAWju%2FQE7suNKhiN4QTsV2MwMQjRYOhiJUPjK7zmZWDPe3n6lKuQ81YrDSwOWZsbIvxBiey6VFCg2ZL4DDRGvkaiKRlVhv6RsOVZQrCWcB2mW1aEBnolukD3U7j%2Bc2tu6m4W6WEQS3ioQOhuvcRXftBV0mWrBRtKt1cSoD30SXrqivOskxJek4nYxa4cuLhu9SQ27K7DEVo%2F0rgsL59NZkUEolZ9ovHMD4deiOOKTAe4rkDYIxw8BkT7LECl8%2Bif3T54CG9XIoPoYE%2FFs6C%2BSwTQkaSBHR%2FriQWuLLXgbnl%2FOEvxJ85%2B3PUJ%2FyM6uPq8azd5AkDb7Ocslgnmh%2BWfDAUfobcdPdzxMHT5FwqTfxKfX13Gg4MTnnX%2BH39NXV2FmObGuuVNEchs48mObiJvG6cA5lqhOHtVYVvncNZMFL1HTfEdAE%2FzRT3ZVsXGcFbkVEDNiJBZVOffho%2BDJ0reeF3c2LwY25Gr1SwoSZRduddhpQIWa9rB8XzV93F8tRdZQVve24%2Fs%2FnWcPS3BfEGJEIXDq0KxeN6T8N9qUDrHbF9j%2BMfFevnokmBoPmUkMJJGR8CT9Nfac1j3RwfOMVneMKXb9LwGOqUBZKZKjPofibCzBh546cWGQfhKA2T%2FeAHUpPHZ0wjQwTT09KX%2BZYixxg85NDoPwODLzydQhdt8sYblRHsKQt6ClfTSmWMtdMaHOuGuhP8DZ8YUuP0tG8AdIjLrg0aqs520MG8p2vbiKm1tiD5CUwPsghP%2BIX519D7tzXRRjtSjHCwTMTd6uNHvO7Iv1FYueD%2BpputFKyTdYJteEdgwgzPDWqDWEotQ&X-Amz-Signature=6095520cdb0142f781c4981507faee2dc0f691abd1ab52402862cbdec4889352&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP7IZR4S%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF5LBfS1hkqs5rCvy05j1%2Fxn1mCAO2GAs%2F2cFPgkQ3HvAiAJb4qgHiWrm2O6idXwtPLST4b2A5%2FYxvJyghHynXcHciqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbOEMl9ChdTLQ3dk0KtwD%2BLdHoRuX0h2URM6vMJsQnNQuJrlSRqoio9YTry%2FvZvZrug9uCpQvJy2WnO4JXHwYe4E5E7P294bk4SHwP2TuP1BE0LnfCozfOaA9cw1wxX2WbQUAQknsQRwQEPzFwj%2FSgtaW7koG9FHFSXQtOy59%2B4kdpi%2FJg%2Flsj3C9MjaRzYNwfJOFSbCWmsn%2FWnZVNm9oFbNqmss3QWevDPL9dW5ekmJIduZNnjTZoiPlZ%2BV9mnlXorq6fKXpltMYVIXDFCenHoUIK41Ym2Q9zlOE1A%2BjWvYF5dLSs2eslLecETD80vg5tdTB9CSzM6AWlpWrvwZUWr941TfWZSi%2FNoLAY67Bfg%2FlFcjmIrE7LT4PAJGMR5dD1RlgOh08mQOxAI4lP5k9vU1kQXF1q1%2FKTfo0yL00RZlkCZeiT1pu5BslLYSz9Ia7FGmuuO%2FZ%2Brp4PBgFckT8mofdQzg4VncLqC354PBglFnX0OOP1fZwIIdd%2Ba%2F9bymMHvodG7jd4OFDJFYXwO7d5eod8mWW%2BcuZATy2i%2FUgTOGZvxjFL0SnTu5niVc27hWGcAT6A6duGMkxDlLcYayCb1g0UYsOD%2FuuJJ66tiZ0I9LYrfOD7a4wBwI3wLadG%2F2YMSDiyuukYBuAw5Aw0dv0vAY6pgGM0G93lUEuYBdNOy66GWRoWkD2oivVIKTVYzNsbC5sfC6WXszaQwrFqH%2FomIveI62Z6Kz6aBRjsAZAgOfPwPfbgFcAI30TU5RVXS6WrTKyZOBjnzN4X1Kl2HPqROukPFeObUFrksqOr63dmqQyB4HzehCAxRsR%2Fjswfu0fhiSdAU%2BAUdxU%2Br0Mq4rr3n5BARQMOuvLV5j1z04jwAZ6F%2Br1WvU7OK5v&X-Amz-Signature=0edfcd56c88f19788ad2ae3aa368d633b5006f9669e75c42aed7449c2dd8450d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCYPQ26I%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICebcYnreFTdq%2FnrmVAN4ndLvWQvHXAsnM2ZlIHLq3jdAiBY0vxUZL3zJ7KjdmsMm5KPywIsskaBx9DN8hqaHGIFVCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2bMmOouZ05WW2jNzKtwDV7VQb8n3mCzi5baQiqI3dzBZPJDwucbtHa7i5edUNp8JYfohulIvLreb3EYbFgQUeFukjyEmaN6uXInrILtePoTbHfdJczLrPxXrQPhSaoRpeVJ5E%2F%2FVd9DZe9yIP18EDli1CRvd5f1ngtNSVI0lvSLUzUMXZ%2BchyNa%2F6g%2BG4cLB1%2FaArBuZUEzq3FIHsEPTAtnYbtpT%2F9ks9zuRHyM6pDUxvWLEsaK0cH%2BzVAzj%2FQhy4XD%2BG4duAnlLXuWj3AmNEqimAW8ocrZtlBqBY5MC837W1NccJ15IjJeWFASHqYVxsgWaiJ%2BIQFERleBFBhHYsRnABE%2F8CZLSsExnNzwS3szT%2FkTVhfaqzrCIqsAhEiy7trW1eRCXO0fuV0AlNnuywuznsCFCArba0CY7JlM1wA9UjnLLWq5eqmoYU%2FVXZUQrKkF76apDuhWo2sd74bB4GjMMTKCCAmaL5RQt9uUvnTKh%2FXOaMff4zKT0Nlpy1T1n7eMfSkALnECPIB%2FFd5kowzM%2By2BKPzi1uwq5QQl6uN3aUEy%2FT5Kci%2BqlNYIyZt%2FvzMkFR5xKvqb42bgpFh6DhrSwDKZZPLboO9BUAKRs1USQJk7osPWA6hRHDE%2FKQKfyXG95dvXua9RrB1Iwpdv0vAY6pgE%2B0V%2Bs1v4S6M%2BOmvBvNOhcSTdLUAmnGiPCWAaMulhINBVM9yOnMhfo9WFojeeY14H15Son01gSay2dIYFMR9Hf80pyNEJeNKhNJjHCormUtcXsVkCPBll%2BVRKdgbmv5z1OOA%2BoMfjsOuCWbOKQjYpcnqongx7%2Fq%2B%2BX93qMbiieUB4q%2BYIftV6YvYFGd0Jz4%2FeB4qeAwVRECUEmqMSm4rxVQzObT4sA&X-Amz-Signature=9d087aa3c38d76beca6a7cecaabb9becb16ceaf19e8e579edf08a49ffd6c2713&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7JRMKYL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSpuzE3HRa3ZUOUwD%2F0yvlG264gznB%2B76%2BTPqmJjnzaAiEAtTP1EIWW0vQYEDoOrSKGZ79ES2c9F1yfIx0B9EY11NEqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLk8pI%2B0T5bLqHiFNSrcAy20XnsfYCTnbhhGOPsgo6xu%2Ftqc9FK9BqvmRuJ4Y4NMNZ1061RrXga%2B2%2FYzAazuwiXA%2FSo33Zdu0PGBd3xYJR0DApOWtZb6YO%2FpOTmJn%2FDESWqb9A2U52ODCr%2F2tAsqBiBEidZP0A8U1hUUe61tjDsmhtFuTC5978aOdwaH8RaKLiVuZIq8Cx9EkU3r7vC3CfsgZQ6hhmJEbxmtBoLeK3pJ%2BhGc19V4FiEgjY7d5llOEqklJ0qbgcU4wEBxHbPdhivbIsmNqSRkWtev3NHaQ1s8fLdv9T6Otf1L9YAys3sU4n5AVVKOHxanPw1IQfoAqY87AMn6jwGfM7rcSekSNwWTMt8BlcutSY%2BO%2BqjIIBEsrfgUvA%2B9HuX6oylH783dsOd1mnEAy3q57YBnD7xaK%2F4mdgCcmrjACQ1mst674u5uMQQNfW6XkhNIhltBRc4ZUowQcwviG1ZL9xvCIOm5rBSTOp2vYZSO8AyF7GxI3Zoa7zPTd2%2FvKZ5%2BLDmady16RrMT%2Fnbcjz9MJH%2F9t9371Qk%2BYBNxVYFYYi8vSFQeOblzj2r0tvlsTLMpIGW39P4C6mi8CSqGkE%2B3TFIucDVekqYU4MA5Cmh88ho3%2BWbFLSx%2Fz9n66k4NzBhJjAy3ML3b9LwGOqUBKqx1Nl6EYrtZurLlLa9S%2FjW5N4Aw6IZpvrN3omTiRLR14W5IKK8d0evq4buUye156Eri%2BQNIU8Gt6zmvZeepWrFlM8IBq6q%2FNGQHC3kq0O%2FDFCbrL%2FK%2FMRgcbQZk0noBuzzY79%2FXL6Gy8GgnGZJYHORVextXhWsAqWa%2BW2I%2ByfB2QE2aJLL7uxxmfCFETZqPu5ZpBwGIu2q%2F2thvurCkOfKhlsBG&X-Amz-Signature=7b79ba598222c181353eff31bfdf318b98b08cdfa29342e6c070089d2e60e928&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOLBW2DV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBW4PQkPt58HaYe3DSfx6UBXeLv9KO%2FUDDdsuliC3ka7AiBj%2BeZ1rUoLphhYJ0cIxGyTtNcV2Ix3TrU%2Fi3hw4jg0miqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZ6Pl81jlvxbeLqnjKtwD3%2BDwBKuITsKt0vXXmxMlJE3K7cFtI7YtKf4nl3bNv%2BZ%2F8fbCFPWCTP9kBF73r6c3jBx8jCPvzRKCtirr7ek%2FnkrWT8wetZfD3Y%2B88nj%2FLgFRGUOTZjmDMbHyTH1SXnTR9gL7Yke%2FOSNWi9l0rFLJbBXyVj4XnwPr0%2FiCCE7TbKSe3RLzc4O16ZAlki3XP5AQDOTFd2mihoHnMNtH18Z5MNXaX4F23EArUtZlBNmakx%2B0mwOnMgocmQdDp%2BI5HzBKnyXs43PbT1MvT4Pij%2F%2B3JhH9FxEnTMvzsHkPq5vF7GHbo2qmNX1O9%2FFGo9LgkZDf17a3CyUbBPIpzWFcS5KB3yjLKrFiEWEAhsLJAi3qnK1mEMx9XgotZSkllbPiUyHR27k%2FdSZ7xLAUzxStq2o3C%2F2%2FyAYwFOz7H27K0E%2BFyZqEPaiNjotshKA%2Fy1%2FQIFe%2BOQ9uD9R35cU65%2BhzrJfQfRn5vKVmgxsOVMRIfe3uUS%2Fm8GFnkhta2jWlJWhOicu4Jes1yqFEUC9vSZ9xWmWGTpZiPpRb1zAVLyQQt4xvlwe4PSKJbtDgERgkRcB0bPlb1XcuOu5WsVJ6LQrV0%2B6pHFF1By03dlheksH%2BHUaffIUGOn%2Bh1jcIOOHfVJwwp9v0vAY6pgG5fcDBRgbxs5v%2BsRBq0eZ6Zg18OJDqmE%2BWbzpq%2BfjvMzUSQd48jthdMBiYMeblt%2BnkXsEejih%2BMfrauYfOh3WGlHFXelC149elDK%2Ba61JZc8JeDlxvglc0njsGBGr4j%2B8DysyAX2bKf2xoa3P4BqQLdUXr3c7gclV%2FqpzGajq7bUHZKoB1HUpEhHUmDwLAFQSgjmHd7QUDdqrkmOvVpC9pUeQRO%2Fi1&X-Amz-Signature=05bec2aa453c756acfd28790f31df160b24a8cef3822e8a750f150f94899f59c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOLBW2DV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBW4PQkPt58HaYe3DSfx6UBXeLv9KO%2FUDDdsuliC3ka7AiBj%2BeZ1rUoLphhYJ0cIxGyTtNcV2Ix3TrU%2Fi3hw4jg0miqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZ6Pl81jlvxbeLqnjKtwD3%2BDwBKuITsKt0vXXmxMlJE3K7cFtI7YtKf4nl3bNv%2BZ%2F8fbCFPWCTP9kBF73r6c3jBx8jCPvzRKCtirr7ek%2FnkrWT8wetZfD3Y%2B88nj%2FLgFRGUOTZjmDMbHyTH1SXnTR9gL7Yke%2FOSNWi9l0rFLJbBXyVj4XnwPr0%2FiCCE7TbKSe3RLzc4O16ZAlki3XP5AQDOTFd2mihoHnMNtH18Z5MNXaX4F23EArUtZlBNmakx%2B0mwOnMgocmQdDp%2BI5HzBKnyXs43PbT1MvT4Pij%2F%2B3JhH9FxEnTMvzsHkPq5vF7GHbo2qmNX1O9%2FFGo9LgkZDf17a3CyUbBPIpzWFcS5KB3yjLKrFiEWEAhsLJAi3qnK1mEMx9XgotZSkllbPiUyHR27k%2FdSZ7xLAUzxStq2o3C%2F2%2FyAYwFOz7H27K0E%2BFyZqEPaiNjotshKA%2Fy1%2FQIFe%2BOQ9uD9R35cU65%2BhzrJfQfRn5vKVmgxsOVMRIfe3uUS%2Fm8GFnkhta2jWlJWhOicu4Jes1yqFEUC9vSZ9xWmWGTpZiPpRb1zAVLyQQt4xvlwe4PSKJbtDgERgkRcB0bPlb1XcuOu5WsVJ6LQrV0%2B6pHFF1By03dlheksH%2BHUaffIUGOn%2Bh1jcIOOHfVJwwp9v0vAY6pgG5fcDBRgbxs5v%2BsRBq0eZ6Zg18OJDqmE%2BWbzpq%2BfjvMzUSQd48jthdMBiYMeblt%2BnkXsEejih%2BMfrauYfOh3WGlHFXelC149elDK%2Ba61JZc8JeDlxvglc0njsGBGr4j%2B8DysyAX2bKf2xoa3P4BqQLdUXr3c7gclV%2FqpzGajq7bUHZKoB1HUpEhHUmDwLAFQSgjmHd7QUDdqrkmOvVpC9pUeQRO%2Fi1&X-Amz-Signature=5f477e08b797dd764edc704f26189350bd49c17b466cb3af594f07877e6b5e96&X-Amz-SignedHeaders=host&x-id=GetObject)

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
