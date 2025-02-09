

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTDI2OXT%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3Pw6IXpdTabvzd585RMCxVNt1xEV9V1crrO0kPE8y8gIgH69yISeUBJxH2urbh0TGiYthvUgk%2FzSifboZqLBE27AqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbLgTlIsj0%2BXLHVUircAxYlPtb8R%2BGDff90ekZ8D5vrSUD4nFZnDPdMlgIiTAXTMxQmzYxD1BRiudVQDFnpwivxxk0%2B51ytLpc4Yd71Cp3zZLDwBYq538aRMeNyGqTi4IoGLgI%2F%2FvBqynyWw33X62LqOJlWyaxak8jCGsSvS%2BDG0QxSwOJhSdRRKtHwNdN8kgIPt8nzivlxQGSGT7vd8c6YDnchVNJ%2Bsm1nQ05vyxx%2ByW8SV22hqxkgk9rAxXwv0SSMWSyopprBNn9RcMPMLnZ5tkvAfjFzPPMKPSE8KKAAU1Q%2BC4SaOCw924%2FWnl5rC4w5YFqn4sHltGLBYuNKLfn6cTQHI%2BLIhTjxqLiOdn16rBxYs%2FBWajKar5xwPwhe%2FCzY%2FScIEhw2JzxMJX3IgtxC1FoEF64vtU9ct2sjz1clxKild5ApJnk8nFM0L38DIJF09Y8o7HKWyO4KXfkmm5BSAXkMGmx5mqGkkp%2F233F9yPO46vrp6RlRoZdsU8LeD3om7lpUCaD%2BkxL7IJWMBd0YQ82Cdfvvtk0V%2FrbV7iiS9STjdMXoR5IN1czCIPLiCaxHvPC5fr5EKnt8QHHsl9V0UYJ0MZxr%2BCKr2OM4kxxcVHYBLFtMWTOzy%2BTmswpPoyPEmuckoHAK9kS9MPXWn70GOqUB%2FVclO%2BO9cl9XTjLk19weTlyO2q7sFvYi%2FPn6%2FIfm4VLz%2F2UAcKlOShHj%2BDoQkdk7t1rh%2B6PjTtnMym6%2BOIFInqe5PB4adNCxSJXXKGyM%2F6FBdVmVY0YMGDSNDSB%2Bx6goBSDXHObklY6iEGI%2BTA5krVkK3jhBs6KqX%2Bi2EynV6DRiQHG%2BtYmIVzx0Zdao3uFgGHv39vy3Ct2uQtbUMWhDBeAd%2FsCw&X-Amz-Signature=979588b211b1ff91f3582f89e722b28a0130411d0c27542bb71a777e85ac1e1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTDI2OXT%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3Pw6IXpdTabvzd585RMCxVNt1xEV9V1crrO0kPE8y8gIgH69yISeUBJxH2urbh0TGiYthvUgk%2FzSifboZqLBE27AqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbLgTlIsj0%2BXLHVUircAxYlPtb8R%2BGDff90ekZ8D5vrSUD4nFZnDPdMlgIiTAXTMxQmzYxD1BRiudVQDFnpwivxxk0%2B51ytLpc4Yd71Cp3zZLDwBYq538aRMeNyGqTi4IoGLgI%2F%2FvBqynyWw33X62LqOJlWyaxak8jCGsSvS%2BDG0QxSwOJhSdRRKtHwNdN8kgIPt8nzivlxQGSGT7vd8c6YDnchVNJ%2Bsm1nQ05vyxx%2ByW8SV22hqxkgk9rAxXwv0SSMWSyopprBNn9RcMPMLnZ5tkvAfjFzPPMKPSE8KKAAU1Q%2BC4SaOCw924%2FWnl5rC4w5YFqn4sHltGLBYuNKLfn6cTQHI%2BLIhTjxqLiOdn16rBxYs%2FBWajKar5xwPwhe%2FCzY%2FScIEhw2JzxMJX3IgtxC1FoEF64vtU9ct2sjz1clxKild5ApJnk8nFM0L38DIJF09Y8o7HKWyO4KXfkmm5BSAXkMGmx5mqGkkp%2F233F9yPO46vrp6RlRoZdsU8LeD3om7lpUCaD%2BkxL7IJWMBd0YQ82Cdfvvtk0V%2FrbV7iiS9STjdMXoR5IN1czCIPLiCaxHvPC5fr5EKnt8QHHsl9V0UYJ0MZxr%2BCKr2OM4kxxcVHYBLFtMWTOzy%2BTmswpPoyPEmuckoHAK9kS9MPXWn70GOqUB%2FVclO%2BO9cl9XTjLk19weTlyO2q7sFvYi%2FPn6%2FIfm4VLz%2F2UAcKlOShHj%2BDoQkdk7t1rh%2B6PjTtnMym6%2BOIFInqe5PB4adNCxSJXXKGyM%2F6FBdVmVY0YMGDSNDSB%2Bx6goBSDXHObklY6iEGI%2BTA5krVkK3jhBs6KqX%2Bi2EynV6DRiQHG%2BtYmIVzx0Zdao3uFgGHv39vy3Ct2uQtbUMWhDBeAd%2FsCw&X-Amz-Signature=df727d3c0cd5e7f923d47bc1db82d2b158490004c6f93a8cc8d25dabf4d57d98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTDI2OXT%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3Pw6IXpdTabvzd585RMCxVNt1xEV9V1crrO0kPE8y8gIgH69yISeUBJxH2urbh0TGiYthvUgk%2FzSifboZqLBE27AqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbLgTlIsj0%2BXLHVUircAxYlPtb8R%2BGDff90ekZ8D5vrSUD4nFZnDPdMlgIiTAXTMxQmzYxD1BRiudVQDFnpwivxxk0%2B51ytLpc4Yd71Cp3zZLDwBYq538aRMeNyGqTi4IoGLgI%2F%2FvBqynyWw33X62LqOJlWyaxak8jCGsSvS%2BDG0QxSwOJhSdRRKtHwNdN8kgIPt8nzivlxQGSGT7vd8c6YDnchVNJ%2Bsm1nQ05vyxx%2ByW8SV22hqxkgk9rAxXwv0SSMWSyopprBNn9RcMPMLnZ5tkvAfjFzPPMKPSE8KKAAU1Q%2BC4SaOCw924%2FWnl5rC4w5YFqn4sHltGLBYuNKLfn6cTQHI%2BLIhTjxqLiOdn16rBxYs%2FBWajKar5xwPwhe%2FCzY%2FScIEhw2JzxMJX3IgtxC1FoEF64vtU9ct2sjz1clxKild5ApJnk8nFM0L38DIJF09Y8o7HKWyO4KXfkmm5BSAXkMGmx5mqGkkp%2F233F9yPO46vrp6RlRoZdsU8LeD3om7lpUCaD%2BkxL7IJWMBd0YQ82Cdfvvtk0V%2FrbV7iiS9STjdMXoR5IN1czCIPLiCaxHvPC5fr5EKnt8QHHsl9V0UYJ0MZxr%2BCKr2OM4kxxcVHYBLFtMWTOzy%2BTmswpPoyPEmuckoHAK9kS9MPXWn70GOqUB%2FVclO%2BO9cl9XTjLk19weTlyO2q7sFvYi%2FPn6%2FIfm4VLz%2F2UAcKlOShHj%2BDoQkdk7t1rh%2B6PjTtnMym6%2BOIFInqe5PB4adNCxSJXXKGyM%2F6FBdVmVY0YMGDSNDSB%2Bx6goBSDXHObklY6iEGI%2BTA5krVkK3jhBs6KqX%2Bi2EynV6DRiQHG%2BtYmIVzx0Zdao3uFgGHv39vy3Ct2uQtbUMWhDBeAd%2FsCw&X-Amz-Signature=21cc41f28441f20d3752bcde3339342761bf896298f4fe3c43c3354944f09fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NSWNTXC%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqH7POeGlJULnGgDNeqM15CuBxUHTTWAXqAwO831gj5wIgWvWx%2BQoVYWpwIZ6Vir080HHOrPxv2N23rbUmue%2B1nvMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLpk3G4f%2FrnxAS9JyrcAxP%2B%2Broio4vLXpdZOqQvgtHJLmKU1Wa0Qt%2BocnloSyNQgTQzRacPdJOGng5IU7TuytrDK%2FDspFR0OuxpNy7GbBwt0wUImqVgEYv14ZSDGnzgVkpAPRrsV24fmdBDajTJOwAgS9eM%2Bh6rZJC82Nd2KLbcRljqBkcD8VeI7Q8FEiWduSrWvNcrJhMUKvIKPNXliJS%2BfFVANW627NTa8NkZW3FBiO7SJBWiw4uXpp5NI%2FW29Ake9NVHcvId%2FF9cCkCLyTPxL%2BOff0RPCCUP%2Bjbk5tNCVjIPWE7m1BKBPqxd%2BkbdSz1zY7wGXvov92D1Yr%2FkkgejO%2FyM24oInNTHsPD8u4VfqRavaeDNxEaao%2BqN2mBk2RoSgfv7oJGaxRhR6XTfmgFRkab1J%2BXMyNuTLXwrBI7djSXdW4LGsaDCK6bHLbXUTyS4RGHtk%2BUjepgALqXPWcPoLZd9T4NjfBmhCh4tunVjLDDBBvHtgZQOH0SW0URMn43XBPRhAiGcpp5sTH4DKlDAQREbLnP6AAhI4JeDA0ePBN5Gm5z1nuTgkzanvasKGIBe4tTbGBpdG6oinCsThVf7e%2Fb0TYTG6j%2FgenrxHA0sgdQpmzUu1k7tPi0okCen2plvp5dD4ZyUXowJMIvXn70GOqUBGz9n9qDXqJHrmYdU9rY7PBPpwEmsGVV0md5WFfn01nj53RU%2BmgLFzn4GQp1ca5c%2BWTfGVsqBAGwzJrT9GRgMpDP8LS7o%2BMnrPvHIXrZeLIrzekciwrWAnSEnrl6eXnb621ZI4jPD2wBVrFyGw5742vU0Of%2BuwvZd%2BDVNJXYsqHk9vcFm0fYkttf3aUiy1XTY7NVrBIas218110Dn960WWblE0tUa&X-Amz-Signature=da097668d8420867c40fe450fcdc310229dbbea34ec8ad1fe17ca8027ce85513&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NSWNTXC%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqH7POeGlJULnGgDNeqM15CuBxUHTTWAXqAwO831gj5wIgWvWx%2BQoVYWpwIZ6Vir080HHOrPxv2N23rbUmue%2B1nvMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLpk3G4f%2FrnxAS9JyrcAxP%2B%2Broio4vLXpdZOqQvgtHJLmKU1Wa0Qt%2BocnloSyNQgTQzRacPdJOGng5IU7TuytrDK%2FDspFR0OuxpNy7GbBwt0wUImqVgEYv14ZSDGnzgVkpAPRrsV24fmdBDajTJOwAgS9eM%2Bh6rZJC82Nd2KLbcRljqBkcD8VeI7Q8FEiWduSrWvNcrJhMUKvIKPNXliJS%2BfFVANW627NTa8NkZW3FBiO7SJBWiw4uXpp5NI%2FW29Ake9NVHcvId%2FF9cCkCLyTPxL%2BOff0RPCCUP%2Bjbk5tNCVjIPWE7m1BKBPqxd%2BkbdSz1zY7wGXvov92D1Yr%2FkkgejO%2FyM24oInNTHsPD8u4VfqRavaeDNxEaao%2BqN2mBk2RoSgfv7oJGaxRhR6XTfmgFRkab1J%2BXMyNuTLXwrBI7djSXdW4LGsaDCK6bHLbXUTyS4RGHtk%2BUjepgALqXPWcPoLZd9T4NjfBmhCh4tunVjLDDBBvHtgZQOH0SW0URMn43XBPRhAiGcpp5sTH4DKlDAQREbLnP6AAhI4JeDA0ePBN5Gm5z1nuTgkzanvasKGIBe4tTbGBpdG6oinCsThVf7e%2Fb0TYTG6j%2FgenrxHA0sgdQpmzUu1k7tPi0okCen2plvp5dD4ZyUXowJMIvXn70GOqUBGz9n9qDXqJHrmYdU9rY7PBPpwEmsGVV0md5WFfn01nj53RU%2BmgLFzn4GQp1ca5c%2BWTfGVsqBAGwzJrT9GRgMpDP8LS7o%2BMnrPvHIXrZeLIrzekciwrWAnSEnrl6eXnb621ZI4jPD2wBVrFyGw5742vU0Of%2BuwvZd%2BDVNJXYsqHk9vcFm0fYkttf3aUiy1XTY7NVrBIas218110Dn960WWblE0tUa&X-Amz-Signature=01dfe805f19277f765554026e7510bdddac9b3785f792c9ffed6b5cb854ea5c5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NSWNTXC%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqH7POeGlJULnGgDNeqM15CuBxUHTTWAXqAwO831gj5wIgWvWx%2BQoVYWpwIZ6Vir080HHOrPxv2N23rbUmue%2B1nvMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLpk3G4f%2FrnxAS9JyrcAxP%2B%2Broio4vLXpdZOqQvgtHJLmKU1Wa0Qt%2BocnloSyNQgTQzRacPdJOGng5IU7TuytrDK%2FDspFR0OuxpNy7GbBwt0wUImqVgEYv14ZSDGnzgVkpAPRrsV24fmdBDajTJOwAgS9eM%2Bh6rZJC82Nd2KLbcRljqBkcD8VeI7Q8FEiWduSrWvNcrJhMUKvIKPNXliJS%2BfFVANW627NTa8NkZW3FBiO7SJBWiw4uXpp5NI%2FW29Ake9NVHcvId%2FF9cCkCLyTPxL%2BOff0RPCCUP%2Bjbk5tNCVjIPWE7m1BKBPqxd%2BkbdSz1zY7wGXvov92D1Yr%2FkkgejO%2FyM24oInNTHsPD8u4VfqRavaeDNxEaao%2BqN2mBk2RoSgfv7oJGaxRhR6XTfmgFRkab1J%2BXMyNuTLXwrBI7djSXdW4LGsaDCK6bHLbXUTyS4RGHtk%2BUjepgALqXPWcPoLZd9T4NjfBmhCh4tunVjLDDBBvHtgZQOH0SW0URMn43XBPRhAiGcpp5sTH4DKlDAQREbLnP6AAhI4JeDA0ePBN5Gm5z1nuTgkzanvasKGIBe4tTbGBpdG6oinCsThVf7e%2Fb0TYTG6j%2FgenrxHA0sgdQpmzUu1k7tPi0okCen2plvp5dD4ZyUXowJMIvXn70GOqUBGz9n9qDXqJHrmYdU9rY7PBPpwEmsGVV0md5WFfn01nj53RU%2BmgLFzn4GQp1ca5c%2BWTfGVsqBAGwzJrT9GRgMpDP8LS7o%2BMnrPvHIXrZeLIrzekciwrWAnSEnrl6eXnb621ZI4jPD2wBVrFyGw5742vU0Of%2BuwvZd%2BDVNJXYsqHk9vcFm0fYkttf3aUiy1XTY7NVrBIas218110Dn960WWblE0tUa&X-Amz-Signature=b51a048188ba6c877c116c579609b2c208caf224c5131e8736628a777f9d1441&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NSWNTXC%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqH7POeGlJULnGgDNeqM15CuBxUHTTWAXqAwO831gj5wIgWvWx%2BQoVYWpwIZ6Vir080HHOrPxv2N23rbUmue%2B1nvMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLpk3G4f%2FrnxAS9JyrcAxP%2B%2Broio4vLXpdZOqQvgtHJLmKU1Wa0Qt%2BocnloSyNQgTQzRacPdJOGng5IU7TuytrDK%2FDspFR0OuxpNy7GbBwt0wUImqVgEYv14ZSDGnzgVkpAPRrsV24fmdBDajTJOwAgS9eM%2Bh6rZJC82Nd2KLbcRljqBkcD8VeI7Q8FEiWduSrWvNcrJhMUKvIKPNXliJS%2BfFVANW627NTa8NkZW3FBiO7SJBWiw4uXpp5NI%2FW29Ake9NVHcvId%2FF9cCkCLyTPxL%2BOff0RPCCUP%2Bjbk5tNCVjIPWE7m1BKBPqxd%2BkbdSz1zY7wGXvov92D1Yr%2FkkgejO%2FyM24oInNTHsPD8u4VfqRavaeDNxEaao%2BqN2mBk2RoSgfv7oJGaxRhR6XTfmgFRkab1J%2BXMyNuTLXwrBI7djSXdW4LGsaDCK6bHLbXUTyS4RGHtk%2BUjepgALqXPWcPoLZd9T4NjfBmhCh4tunVjLDDBBvHtgZQOH0SW0URMn43XBPRhAiGcpp5sTH4DKlDAQREbLnP6AAhI4JeDA0ePBN5Gm5z1nuTgkzanvasKGIBe4tTbGBpdG6oinCsThVf7e%2Fb0TYTG6j%2FgenrxHA0sgdQpmzUu1k7tPi0okCen2plvp5dD4ZyUXowJMIvXn70GOqUBGz9n9qDXqJHrmYdU9rY7PBPpwEmsGVV0md5WFfn01nj53RU%2BmgLFzn4GQp1ca5c%2BWTfGVsqBAGwzJrT9GRgMpDP8LS7o%2BMnrPvHIXrZeLIrzekciwrWAnSEnrl6eXnb621ZI4jPD2wBVrFyGw5742vU0Of%2BuwvZd%2BDVNJXYsqHk9vcFm0fYkttf3aUiy1XTY7NVrBIas218110Dn960WWblE0tUa&X-Amz-Signature=cf5aca303a4f69aa0f40de162e92b954389e9d71829e483d09ead27145dcd635&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NSWNTXC%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqH7POeGlJULnGgDNeqM15CuBxUHTTWAXqAwO831gj5wIgWvWx%2BQoVYWpwIZ6Vir080HHOrPxv2N23rbUmue%2B1nvMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLpk3G4f%2FrnxAS9JyrcAxP%2B%2Broio4vLXpdZOqQvgtHJLmKU1Wa0Qt%2BocnloSyNQgTQzRacPdJOGng5IU7TuytrDK%2FDspFR0OuxpNy7GbBwt0wUImqVgEYv14ZSDGnzgVkpAPRrsV24fmdBDajTJOwAgS9eM%2Bh6rZJC82Nd2KLbcRljqBkcD8VeI7Q8FEiWduSrWvNcrJhMUKvIKPNXliJS%2BfFVANW627NTa8NkZW3FBiO7SJBWiw4uXpp5NI%2FW29Ake9NVHcvId%2FF9cCkCLyTPxL%2BOff0RPCCUP%2Bjbk5tNCVjIPWE7m1BKBPqxd%2BkbdSz1zY7wGXvov92D1Yr%2FkkgejO%2FyM24oInNTHsPD8u4VfqRavaeDNxEaao%2BqN2mBk2RoSgfv7oJGaxRhR6XTfmgFRkab1J%2BXMyNuTLXwrBI7djSXdW4LGsaDCK6bHLbXUTyS4RGHtk%2BUjepgALqXPWcPoLZd9T4NjfBmhCh4tunVjLDDBBvHtgZQOH0SW0URMn43XBPRhAiGcpp5sTH4DKlDAQREbLnP6AAhI4JeDA0ePBN5Gm5z1nuTgkzanvasKGIBe4tTbGBpdG6oinCsThVf7e%2Fb0TYTG6j%2FgenrxHA0sgdQpmzUu1k7tPi0okCen2plvp5dD4ZyUXowJMIvXn70GOqUBGz9n9qDXqJHrmYdU9rY7PBPpwEmsGVV0md5WFfn01nj53RU%2BmgLFzn4GQp1ca5c%2BWTfGVsqBAGwzJrT9GRgMpDP8LS7o%2BMnrPvHIXrZeLIrzekciwrWAnSEnrl6eXnb621ZI4jPD2wBVrFyGw5742vU0Of%2BuwvZd%2BDVNJXYsqHk9vcFm0fYkttf3aUiy1XTY7NVrBIas218110Dn960WWblE0tUa&X-Amz-Signature=0e9b3355d6812fd0bd5b4254d76e1017fe1525de0b0eb88f6d5385101b4dab37&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NSWNTXC%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqH7POeGlJULnGgDNeqM15CuBxUHTTWAXqAwO831gj5wIgWvWx%2BQoVYWpwIZ6Vir080HHOrPxv2N23rbUmue%2B1nvMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLpk3G4f%2FrnxAS9JyrcAxP%2B%2Broio4vLXpdZOqQvgtHJLmKU1Wa0Qt%2BocnloSyNQgTQzRacPdJOGng5IU7TuytrDK%2FDspFR0OuxpNy7GbBwt0wUImqVgEYv14ZSDGnzgVkpAPRrsV24fmdBDajTJOwAgS9eM%2Bh6rZJC82Nd2KLbcRljqBkcD8VeI7Q8FEiWduSrWvNcrJhMUKvIKPNXliJS%2BfFVANW627NTa8NkZW3FBiO7SJBWiw4uXpp5NI%2FW29Ake9NVHcvId%2FF9cCkCLyTPxL%2BOff0RPCCUP%2Bjbk5tNCVjIPWE7m1BKBPqxd%2BkbdSz1zY7wGXvov92D1Yr%2FkkgejO%2FyM24oInNTHsPD8u4VfqRavaeDNxEaao%2BqN2mBk2RoSgfv7oJGaxRhR6XTfmgFRkab1J%2BXMyNuTLXwrBI7djSXdW4LGsaDCK6bHLbXUTyS4RGHtk%2BUjepgALqXPWcPoLZd9T4NjfBmhCh4tunVjLDDBBvHtgZQOH0SW0URMn43XBPRhAiGcpp5sTH4DKlDAQREbLnP6AAhI4JeDA0ePBN5Gm5z1nuTgkzanvasKGIBe4tTbGBpdG6oinCsThVf7e%2Fb0TYTG6j%2FgenrxHA0sgdQpmzUu1k7tPi0okCen2plvp5dD4ZyUXowJMIvXn70GOqUBGz9n9qDXqJHrmYdU9rY7PBPpwEmsGVV0md5WFfn01nj53RU%2BmgLFzn4GQp1ca5c%2BWTfGVsqBAGwzJrT9GRgMpDP8LS7o%2BMnrPvHIXrZeLIrzekciwrWAnSEnrl6eXnb621ZI4jPD2wBVrFyGw5742vU0Of%2BuwvZd%2BDVNJXYsqHk9vcFm0fYkttf3aUiy1XTY7NVrBIas218110Dn960WWblE0tUa&X-Amz-Signature=6c107209ebe44ddc6b298bbc501332d97cd3b62642de865d4a70e702225972ff&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPKYKEXR%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDh0BjMZoZapkcPmLw7q3PIoRbmHeLjvX%2Bc8x%2BcEnNlFgIhAOL1%2Bkr6SFSuIIyF8tP1gb4QKhQ1v85bvvE3Yq%2FQhqDMKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVcX0iD6Myh853bloq3AMgbmPWEtpHik9rj2T177y8gdJSfbBx%2FhXdWLPbFLQWFMkeUADTGa%2BmvoAI%2B4wLiB3Csd5VEQ80cVBK2SfvaBj38yI7jpknPEqCcUd%2B8a8rTeL61sQgkzeta8F127PM1SbGDUg%2BWBdEm1vw2fu8QR50mnuxWBg4MQRkm1uwzlkKsfhNnBUzECUSeEdY%2FRicTFBWq1gNcMQQcpmp7cicyKGFzH9Vn7iLjMbyGv0MybhxxA4VtUztwmqhUlAy7j1mXVzzVBxNeOCT9qhVtop0jEJZI35EWTG3YU2uw6iIZX%2BXKRuxZLXrCYAKv1LgyNfg5NzGfzNh7gUjQRIYUMkNVjtRn4z%2BlARA1LvTQoYefClcHUBhyXOcN2DJmNfPv3gOpVmo%2FqGx4LHfLTMAmnGFHOUE7OrJ3pVIG%2FUim4%2BxctjmTpcjsgfGq4OUpi8jGUnSij0jXcZH54uhqjEzfHIxRZX%2BNbh%2B5A3cFCQA8GxqZ5a2%2By7kex1l9hTJHbDDex5qz7GCssRdOPcKe%2B3Nd8rZdFV52R2balQhOgF5I8ldsRVRshvXISL9b8i2U3AgQX6v0q0VTETZRQ48%2FC%2B0gdJo0QPkqNBk1lWJE11qphysYlMewP%2FXBYun0O%2Bhtkt3TjDg1p%2B9BjqkAdxa3Ep%2BshpkC1gHtBJwzRbl7mu%2BKshp4FQNCOg3TwOh2aWILGJ2Jgih4wpeejFQNkSGmv5qDtPP6EjmxHxK6%2Fre5wFIFKvLtXDIIU%2Fm6wrQkMbPowZMxdyQC0v11rTZwrigeI2NC8SK3u%2BMSQHu242RGq0lOPVImD%2FAltw0DEmh3Kj6CEtAToum7UASn1z9IWK2oEegVEwQtdLkmhtP%2BmW5kN1t&X-Amz-Signature=89ebcc823ffa241d8a55f5bd247b1151bbd77064183497393f802b57b8df3665&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOPNTG5J%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQwMvDP2Th3l5YTT4EszWqqND1mpomMZULl4M2Mi9YvwIhAIVISDuwu9jp9%2BNVmVGDzfXLtzbDdDJQqmRwLdUXAaTvKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwJKWhbvSv8Qb5vP0Iq3AMrYKIKWtaStEcb2Zzmh30x%2BA0p20Ht9cD1vB4jfvQDFAMmpRT5lOKb0uC4JqNXwo9qT91D3UGaHPRfJJps4cdo7Rw%2Fv%2B7SRehkl50ltKoUKoDffvam%2BMt7Y8bKBCxWoDDyPoCzXCv7qt0XW3q%2Fvkvp7dhhRiCBkk5XbHHPUosuS00dNNwBX7yv3eN%2Fjxbmb9q0ZYoITzUIfyNeV%2FdYPTOj4pwHyimNRhlz8H3pRgpRDsbQY4Vie2qmUWMnVHiswjl3iTVsWetp7IRzjxkBphnFJsr8wWhYzzn4OLfyMidgvlUO%2BbyYiJZOX5DB7iR6hNgTXaGfWo3MLbXcuwqUZ8zYjSQ%2FBg8B%2B9hgt7wxErqgN06Wwz8KfaoznXOZzQl40M9%2FKU4Mq944IR822DF9k5KgY8TpA4yHWAfFN17gqjPVORQUkppz6L3hLDxgaktEOOXcMHKcqK96qysoJSXRGD7squSTYhPBzDGDWvdRSs3wXhnaSRyXQfKClwILnUijt4YO%2FYwC%2Fk%2FPxm9NosZVGSoM2RvlgdIguLf4ZmrSOVJXgQd4N3rCP%2BgLtcNWvwWSByiJEil2x4u8J6KWP%2BCOIVZ4a7eZCh2lixWOe81Z%2BT4lg3dP8V3juHfxIxbCWzDA1p%2B9BjqkAZTbD%2B6%2F726K9v6lSUOG8hQZPw7yeQfHRiUyzNHG5fbFECUzIs0SZbvaU4Lb39%2F34ddYg2S5Pi9sH68ZXGvzjKVBkYNbIDF0KFGvXszvQAWxM8srTDPjMaWbZxfYoz84GaLwRz19Kp0F3mj0klG%2BXWmpsecTSH2J0pQP1gGxyeBWHWO4%2FTd%2BssvbFKFKsiOSbHqZhXHuxz%2FJmBYn553V3m1oPTUk&X-Amz-Signature=1ba155edcfe8244e8a9102b7ce15a5325e5e950492e9fd7d3a7daf174565bfba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NSWNTXC%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqH7POeGlJULnGgDNeqM15CuBxUHTTWAXqAwO831gj5wIgWvWx%2BQoVYWpwIZ6Vir080HHOrPxv2N23rbUmue%2B1nvMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLpk3G4f%2FrnxAS9JyrcAxP%2B%2Broio4vLXpdZOqQvgtHJLmKU1Wa0Qt%2BocnloSyNQgTQzRacPdJOGng5IU7TuytrDK%2FDspFR0OuxpNy7GbBwt0wUImqVgEYv14ZSDGnzgVkpAPRrsV24fmdBDajTJOwAgS9eM%2Bh6rZJC82Nd2KLbcRljqBkcD8VeI7Q8FEiWduSrWvNcrJhMUKvIKPNXliJS%2BfFVANW627NTa8NkZW3FBiO7SJBWiw4uXpp5NI%2FW29Ake9NVHcvId%2FF9cCkCLyTPxL%2BOff0RPCCUP%2Bjbk5tNCVjIPWE7m1BKBPqxd%2BkbdSz1zY7wGXvov92D1Yr%2FkkgejO%2FyM24oInNTHsPD8u4VfqRavaeDNxEaao%2BqN2mBk2RoSgfv7oJGaxRhR6XTfmgFRkab1J%2BXMyNuTLXwrBI7djSXdW4LGsaDCK6bHLbXUTyS4RGHtk%2BUjepgALqXPWcPoLZd9T4NjfBmhCh4tunVjLDDBBvHtgZQOH0SW0URMn43XBPRhAiGcpp5sTH4DKlDAQREbLnP6AAhI4JeDA0ePBN5Gm5z1nuTgkzanvasKGIBe4tTbGBpdG6oinCsThVf7e%2Fb0TYTG6j%2FgenrxHA0sgdQpmzUu1k7tPi0okCen2plvp5dD4ZyUXowJMIvXn70GOqUBGz9n9qDXqJHrmYdU9rY7PBPpwEmsGVV0md5WFfn01nj53RU%2BmgLFzn4GQp1ca5c%2BWTfGVsqBAGwzJrT9GRgMpDP8LS7o%2BMnrPvHIXrZeLIrzekciwrWAnSEnrl6eXnb621ZI4jPD2wBVrFyGw5742vU0Of%2BuwvZd%2BDVNJXYsqHk9vcFm0fYkttf3aUiy1XTY7NVrBIas218110Dn960WWblE0tUa&X-Amz-Signature=c8e9d0e50b735a4be1b993bd9f3f476864bb24bfc4559b30adc05cb1ebe17599&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NSWNTXC%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqH7POeGlJULnGgDNeqM15CuBxUHTTWAXqAwO831gj5wIgWvWx%2BQoVYWpwIZ6Vir080HHOrPxv2N23rbUmue%2B1nvMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLpk3G4f%2FrnxAS9JyrcAxP%2B%2Broio4vLXpdZOqQvgtHJLmKU1Wa0Qt%2BocnloSyNQgTQzRacPdJOGng5IU7TuytrDK%2FDspFR0OuxpNy7GbBwt0wUImqVgEYv14ZSDGnzgVkpAPRrsV24fmdBDajTJOwAgS9eM%2Bh6rZJC82Nd2KLbcRljqBkcD8VeI7Q8FEiWduSrWvNcrJhMUKvIKPNXliJS%2BfFVANW627NTa8NkZW3FBiO7SJBWiw4uXpp5NI%2FW29Ake9NVHcvId%2FF9cCkCLyTPxL%2BOff0RPCCUP%2Bjbk5tNCVjIPWE7m1BKBPqxd%2BkbdSz1zY7wGXvov92D1Yr%2FkkgejO%2FyM24oInNTHsPD8u4VfqRavaeDNxEaao%2BqN2mBk2RoSgfv7oJGaxRhR6XTfmgFRkab1J%2BXMyNuTLXwrBI7djSXdW4LGsaDCK6bHLbXUTyS4RGHtk%2BUjepgALqXPWcPoLZd9T4NjfBmhCh4tunVjLDDBBvHtgZQOH0SW0URMn43XBPRhAiGcpp5sTH4DKlDAQREbLnP6AAhI4JeDA0ePBN5Gm5z1nuTgkzanvasKGIBe4tTbGBpdG6oinCsThVf7e%2Fb0TYTG6j%2FgenrxHA0sgdQpmzUu1k7tPi0okCen2plvp5dD4ZyUXowJMIvXn70GOqUBGz9n9qDXqJHrmYdU9rY7PBPpwEmsGVV0md5WFfn01nj53RU%2BmgLFzn4GQp1ca5c%2BWTfGVsqBAGwzJrT9GRgMpDP8LS7o%2BMnrPvHIXrZeLIrzekciwrWAnSEnrl6eXnb621ZI4jPD2wBVrFyGw5742vU0Of%2BuwvZd%2BDVNJXYsqHk9vcFm0fYkttf3aUiy1XTY7NVrBIas218110Dn960WWblE0tUa&X-Amz-Signature=5802448481cdb2c86b55e8d897ede9527ba9a7b292597371b0d9b2e7183b5bd8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NSWNTXC%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqH7POeGlJULnGgDNeqM15CuBxUHTTWAXqAwO831gj5wIgWvWx%2BQoVYWpwIZ6Vir080HHOrPxv2N23rbUmue%2B1nvMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLpk3G4f%2FrnxAS9JyrcAxP%2B%2Broio4vLXpdZOqQvgtHJLmKU1Wa0Qt%2BocnloSyNQgTQzRacPdJOGng5IU7TuytrDK%2FDspFR0OuxpNy7GbBwt0wUImqVgEYv14ZSDGnzgVkpAPRrsV24fmdBDajTJOwAgS9eM%2Bh6rZJC82Nd2KLbcRljqBkcD8VeI7Q8FEiWduSrWvNcrJhMUKvIKPNXliJS%2BfFVANW627NTa8NkZW3FBiO7SJBWiw4uXpp5NI%2FW29Ake9NVHcvId%2FF9cCkCLyTPxL%2BOff0RPCCUP%2Bjbk5tNCVjIPWE7m1BKBPqxd%2BkbdSz1zY7wGXvov92D1Yr%2FkkgejO%2FyM24oInNTHsPD8u4VfqRavaeDNxEaao%2BqN2mBk2RoSgfv7oJGaxRhR6XTfmgFRkab1J%2BXMyNuTLXwrBI7djSXdW4LGsaDCK6bHLbXUTyS4RGHtk%2BUjepgALqXPWcPoLZd9T4NjfBmhCh4tunVjLDDBBvHtgZQOH0SW0URMn43XBPRhAiGcpp5sTH4DKlDAQREbLnP6AAhI4JeDA0ePBN5Gm5z1nuTgkzanvasKGIBe4tTbGBpdG6oinCsThVf7e%2Fb0TYTG6j%2FgenrxHA0sgdQpmzUu1k7tPi0okCen2plvp5dD4ZyUXowJMIvXn70GOqUBGz9n9qDXqJHrmYdU9rY7PBPpwEmsGVV0md5WFfn01nj53RU%2BmgLFzn4GQp1ca5c%2BWTfGVsqBAGwzJrT9GRgMpDP8LS7o%2BMnrPvHIXrZeLIrzekciwrWAnSEnrl6eXnb621ZI4jPD2wBVrFyGw5742vU0Of%2BuwvZd%2BDVNJXYsqHk9vcFm0fYkttf3aUiy1XTY7NVrBIas218110Dn960WWblE0tUa&X-Amz-Signature=515a508154d6378a808136e327faaa01248aed4e5ed03b8ac2aa44be55af2c9e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5ZY3TL5%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKRxFtA6VEzNuJY74M9%2F5iUf4W8cOjNg%2FVSdf0AMN4CwIhAKGuY18fs9QuTxVTpZyJU8wFP4HMLTILAylnjJMRbsxqKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz8jHuDcKMSq1LeMuMq3ANde9UazGz0S51HvuqY7ZucafV%2BXZTv8y0DXmsG4t8GD9ofbtG4Pwcw4RxAdteuyV6nVmTgdPLzdyIw%2BzAV6b8AiUQBShhmtG0ea4sKq4EgZgw%2BYWSetocEqmslOdgHBBwEjoY74tZQY%2BNHdblUgWZK6NO%2F8vMtGC7StXdqifC4brkZhN760fNkjCFlXxHbv1lT1dxnivb8TUQbin9HLsTYLURwUNSOecHbAYj%2Frbpz1dKEhXGN1wtnEoZILBmgCW8JaKZJ%2FTv85RQA9YDKlvUmm7AdPgzeCQxbVM7ffI4n7mwZ9N05b7QZd5mwPcpqmuCsg%2F2XwvHeuIgZsg9p%2FrTpVLgnOjgvHr4i2lXRUx9GG%2B4Ew5R2rORnmc9IIOQvmLry%2BLPVNxehhm58sgayyxjjw3UwiZJr50NI7ZuQglSCQxR2aV8zZX6JvvufvXaUT%2Bfd2obfB2KR7EGZWko9h1AZGvg1fYj%2B7RUDAy8ByaejKt38o5927z%2B73SL%2FZi4jwU1afjw%2BIO6B8wahNH7ltt%2FS20CU0u%2FtnOgb1CMEmARbHk8TF%2FJMNKIgKHZB24tzQwBUrhQCZMD4Db7erC%2BmWm1hKr5kDVq4JA%2Fpxc%2Fz8mZ7FzAxYZ7UrKkzJ26f9zDC1p%2B9BjqkAc%2FUKBlm2e9u6Is2vhePcL8U3i9F9X1mk4DcjfmVORIsZ0RsXnnKKH5eFjNbgmDQ%2FbelZTsLb73vyRvLLLEoAtMCbeHDgeb4yxZQteJDmgsSNHeCTN00ieEV3RkZ6q0L52nTg0ZOIT9naVHNeOks3qmwfvF%2BA%2Bar7Mhb3zOsldG9RFdOM6zNFkmd2WlciABom%2B9ZZbN3K8RzYRxVOZVAbMrkUPMQ&X-Amz-Signature=39e258d53656281fa73ec7c1c7d1a20b7d05090e07cef83c58e03aa467e0e910&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPUHSQEK%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoH3x7txd8HlJf%2BQI2GG91uc2pfXprmzkxCREGQifFrAiEAwC%2F6xhT08IScGWWiAaK7HSDZHdFLHVuxPjo8ESbv1L8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3B%2FCbp78bYrH0jACrcA5F0gdtjsWUERuBjaCLWN6OFLojYJOb6ektPdCn%2Bx%2BXoUYj9G6O6u6xGSywrNaAT4ggd4fcsBUbgbIGQ1HoYl1nnyk2sVAkLDCknE5eXB9Qnpf%2F%2BLZIGFgiZ3%2BemnMKiO7jDMO51ccL3hXMlGR%2B0p9Yrm0VaBBLXkegmQ7C2PTMjRrgSbjosWOUnpLNY%2FZ8X7E%2FtALHA5YfcdLlTMW3aX4jeZBDNOl6tD3FWq5yarfG927hMC6gp4eVk%2Fo2NcErfD13ddJUc1pxsbuNz8EsQIyl0ZDHYtX4fO1gwNIpqC0OEMGrZmzGQg%2Bw6yGNnFHFfmysdy92plNG6LipJvCI0%2BMJluPROC8WPn2Ha37Po55H%2BwUrTk7azcTbgtAzdFWy17F3aIGkn%2FK6siPUUYj2paorhKkM6FnL5ltLtEiN7phIiuAqFKXDnfs9f4zijBQi81Xugn0yrPY1JyRCSpRnru9bTHaZxGS9eahZWMoJqClsEndqVPCbtMG6BfHYEGp9TyXbkno7%2F08Papb2W4KB35rLR0IKuZq76UWH9biHup%2F1aEXg3ik2Ius5MbSHKXiTSz7Gej5mcm8ZYmYbngoVc2U%2FuX6tnuSoLnbuG9DZScwuBzfU2o11B69iapCsCMOjWn70GOqUBvKA9ixwYWqngI53GSMxk8CStVBZKaN3E7IHKudgXWD9FTBjpDcwRgNFOzSGMhvHmVUcAj%2F3Aic2DXR%2B7WrP4PBR%2Fnb3yJE2S0VQ0q0AicuJ%2Ft11%2BYNQhBPugliWQqBVKgfycjW9niPmADDhxCAc8Ni4TMNG%2FenC7HRlengybZOSzUsLHzD5V0C0XpC9D5AgDBHsdGuoSCaG25lne3pe0QYA8ALIh&X-Amz-Signature=6dfcc199d517adb7720697e31626d689310183355df30b300ec1928fcdd08811&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNZDSN4G%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLo9xwd3ml1o3VEaGe2%2FGnTd%2F344knyYh1tY5MQA0mogIhAJ31PpUNcc5UAbdq2niddK7etfziTH1yt2SmEUV0Km0bKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5QiMT5RCHdZ2ge4Qq3AN8kQeVlbyxw1HnAxd7hWT9qMVnnIjNsIGZw81unTALVjf9W6ctcz2eSi0HheMcBlD501rbzJW85iUv8VhnsOTHlE1yMz7KKknOhSdIIDv8cnrSxecLLPIZdyuvCljk4S4OR4YyoR%2FSWVlnEq2gMBD%2B0oLlMtAICMp46WKgHxcsBCLpLURr8CiAEMH1XUt0mQXCLoXmZIJupZ6Us%2FnebP2gk3zGr0J%2FRf3IAR98jvDiV1W5BMPXGhpl2zoMIIfnJVh6GZhwxlpc3lyP4%2B2N6W3AeAw70JCfIbW%2BmXPC13kKIFnp5kpuJvxZ3AcUhkWV1HTUXyz0ss9rsq%2FjzyXXK5%2BS1CEqG2pS3RHrpwjN0KGxgxZywZX%2FR71IduWM1Mn0Z0DWhHoF6wf4H8XrjDlALqxYUui%2FLTx0IVcjefdnxQzXnO2s3qbFyLTEUd3jljuPNnHoJF7ZgGtwoRzwYHXXgP3K7J8bB8NYqaAc%2B2H0T2m7l47yEYDNg1bjoiRPyipr70KOThghO1mOaWAQ5BfvrbQEQ%2BX4Kje%2FcfiHO0XNjRNFDjqyRIIKehYP0jPlIWUm%2FkmoXP7hQqpe9CymwKwZiF4h4R66lHmXVc8UVUqJDIL2OGW7NU36pmilotc17zD11p%2B9BjqkAW8YG0PMUFX%2FBDx0mfbrb5YlMQLP8sCGO2CFJG6SgdCpQKzGC5ayWIuYifmVzcYDdM9atBxUQEWYvC%2Fg73gi3NaD1vsT6s4A8L%2BZN8Nq1wL1aPvegfKDC31a0cgbaIRtmfibaV4SoO%2B6LeOKRCWq6QuhFmK1WVaqAeyDq0n22WP3R1EaQ6eZhzwzQrSslEDbWdfsoDF0cs3iGlIRUt2zsveSGNnp&X-Amz-Signature=e612fa68bbf4b3e4198997df21f97147d1c186408f3405f50d4470c2b9dd359a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEMADU2I%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEJDpez9TcAu9hsGaDtx5I2xsINUKnnb8XPCd%2BikoKTTAiBKrD09CxZuA%2F7keTDNUx4SOHNs%2Fn0g3yGPjP%2F8%2FiVmxCqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZptOjpvlYnAoxeDKtwD9QRHcopUG3gWMYSSMsAmyXR1jKal5%2B0svwoCd5azAlMbjf9dgSRa1Cq%2BL7DrkjZ2xrYU%2BAxWrE596i775Qn%2Fe5zbYRRfW4VcMFjs9xpXsQPeQTV3N6U957wuVHSLAlxOvSCAlrILfLmdm8sgO%2FgKLi%2B15pUuladNThpLfc8R%2BCbm%2BL8uucPlgaW032IzNScA8Y%2FyQYdlAiwP6OkP%2BczvVFJl6%2BAmse7Ay2eHifKpduRdwCS%2FfpB4SZaq0KVmWAJNDVHwGzCiJYDd5f7atuBVZ4oG4qrpwkH6GBkRTpUoxZ0hjQNoBPUnJ4s%2FBX92w47Knj0pCC21dKyC4zdHJvpKR18czgXk5P6Tmylp%2F16vxsedDrJpF34gOVqYZgmHR%2B8VqstAG0epSc81gyAJUV3mGdSWV0lk9ic8qM2hp%2BWI1DorFSWrDpGaZ2XC8%2B45vmWKypk6lkD9VECEvrUrx1S5in6ueLWxYhDalNXndJMKUwciEuaPqvJ2Tld5MdSnhnnPxX53qaJljoiEpTvIGDm%2BilzO2aTxwt7LiKNUZ0jFAgdkxj50FveJOk091RelB8BOrvv6ZrbBOZIKRGgk067Gd75OX7dxG0SFrf6STOdEA0sbeiCamDfEnGC7%2BU0wtdafvQY6pgEcE0itPYZP%2BG9RixsOep5JpQiw%2BjLIwjdzlsC47tkf9ZvISnHvxcml2mEN9Ej%2F2bDYc1MGKJKjb%2FedX4SBdLVSjDiqd1cUoFOmcRCBuLQ8ISv3arH6WgLYlucRWgddc2AbiuTPPa%2FnQjwGZEN8jfQppS%2BaUTc6Ntdbr5ax40nG4opkW6fFReQ8Ohh6YYiKyDF21R4JcUP53feJgGHf2gcFDWlGWe9Q&X-Amz-Signature=dd100cb1617a0df1a466dbe719de763b0f50dce09e1b3efa38a649b598b47a27&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEMADU2I%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEJDpez9TcAu9hsGaDtx5I2xsINUKnnb8XPCd%2BikoKTTAiBKrD09CxZuA%2F7keTDNUx4SOHNs%2Fn0g3yGPjP%2F8%2FiVmxCqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZptOjpvlYnAoxeDKtwD9QRHcopUG3gWMYSSMsAmyXR1jKal5%2B0svwoCd5azAlMbjf9dgSRa1Cq%2BL7DrkjZ2xrYU%2BAxWrE596i775Qn%2Fe5zbYRRfW4VcMFjs9xpXsQPeQTV3N6U957wuVHSLAlxOvSCAlrILfLmdm8sgO%2FgKLi%2B15pUuladNThpLfc8R%2BCbm%2BL8uucPlgaW032IzNScA8Y%2FyQYdlAiwP6OkP%2BczvVFJl6%2BAmse7Ay2eHifKpduRdwCS%2FfpB4SZaq0KVmWAJNDVHwGzCiJYDd5f7atuBVZ4oG4qrpwkH6GBkRTpUoxZ0hjQNoBPUnJ4s%2FBX92w47Knj0pCC21dKyC4zdHJvpKR18czgXk5P6Tmylp%2F16vxsedDrJpF34gOVqYZgmHR%2B8VqstAG0epSc81gyAJUV3mGdSWV0lk9ic8qM2hp%2BWI1DorFSWrDpGaZ2XC8%2B45vmWKypk6lkD9VECEvrUrx1S5in6ueLWxYhDalNXndJMKUwciEuaPqvJ2Tld5MdSnhnnPxX53qaJljoiEpTvIGDm%2BilzO2aTxwt7LiKNUZ0jFAgdkxj50FveJOk091RelB8BOrvv6ZrbBOZIKRGgk067Gd75OX7dxG0SFrf6STOdEA0sbeiCamDfEnGC7%2BU0wtdafvQY6pgEcE0itPYZP%2BG9RixsOep5JpQiw%2BjLIwjdzlsC47tkf9ZvISnHvxcml2mEN9Ej%2F2bDYc1MGKJKjb%2FedX4SBdLVSjDiqd1cUoFOmcRCBuLQ8ISv3arH6WgLYlucRWgddc2AbiuTPPa%2FnQjwGZEN8jfQppS%2BaUTc6Ntdbr5ax40nG4opkW6fFReQ8Ohh6YYiKyDF21R4JcUP53feJgGHf2gcFDWlGWe9Q&X-Amz-Signature=1b5d80c322ee650d2692347126b36b1cdc40ccae248d8a43ec5c2ea45856cb42&X-Amz-SignedHeaders=host&x-id=GetObject)

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
