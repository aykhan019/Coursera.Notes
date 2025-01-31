

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFVIQXXK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvRDdtUAw1NhB3LWAGivPwLL9HK%2BUs9O8rbs31xooXqAIhAMSRpA5DqfH3ZTY8PXxXzIHkHKGeP7shXTUIJ3IojKoSKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLSpDs665WhvxLQLUq3ANq2no%2BWKz5yXJ13r%2B2ccqx8M4WX9y8cpsJcLLZi4%2BrP9Uxl4%2FigP951MlrTqi212eiYoBDjOkJFd2EdKKy21Vjzpsu8glplUJ%2Fyh3PpnGUIJHt4S%2FCSw39LN8EGa4k27hgkFYMoifMflD4cnrsbZh%2FFftW5V%2F1nlr1llpIT8kWSR1Lohl7auh76I8KJoTGWkQ%2FzjgUOkF8NXyzD1rW0asoB9r5ng8uvGUeUlHDzvPkCANdHEo%2FSPJijlZ%2FMedJkRP7m2knCeCLj2xkpD1Z9Mxxzbv4A7TBXwyEiCTke5YDNMXqW6qUdCuS6beNd%2F5mKSq5J%2FKlO1lXB9hd0bdjYMwT9MCYnR7%2Bnu2x4Yp5jBC2QF593Y3zQ44JvVKKI0oowvhT34xu3pb7Pae8aBpiKEPsR7oH46QAdAgHQN8G%2BC80%2F3M9dVGO3NF1ReMJB3kd0yWRnjtUqgaQsGO0ahlYD5%2BfQ0ANzayCMxdPMaL5sc8d2OD5HgDvJOMeQzmhK5DmdsLoU4HIVG%2FSB4d%2FwVmyia5IW4EPiIZ6etiRPGtp%2FodoND5e%2FfdjCGqznV29FBOeNZchEklwmtPj3CjdEMrl9swrvnxduYVLS4maDqSAmzANI3QRzts0nBecSLUsrjC84fG8BjqkARsT9qt7%2BTFqpkPf00%2BFit9vCpWIujTAk094VEKk3aMw0MsoUYs21%2Fw01fhjEvqIJ9Fx6Ps5nSzqv397RMjayI7IaOkMHXMHtmgquBoNNSllK0aJS7ABr1DpxRC1Y42LZ6ZELYimSS6r4rOaH7LIwZhii4xC3QDvDs758tYsB%2BIyef8KJRsOFepPzqfcmEtCUDJ93Z7ChCKno5lp0mx22aurbq2A&X-Amz-Signature=6186b5d0d411045441c8ca214438c5625b25c8fdfbad7486c3cdf60a69e3105b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFVIQXXK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvRDdtUAw1NhB3LWAGivPwLL9HK%2BUs9O8rbs31xooXqAIhAMSRpA5DqfH3ZTY8PXxXzIHkHKGeP7shXTUIJ3IojKoSKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLSpDs665WhvxLQLUq3ANq2no%2BWKz5yXJ13r%2B2ccqx8M4WX9y8cpsJcLLZi4%2BrP9Uxl4%2FigP951MlrTqi212eiYoBDjOkJFd2EdKKy21Vjzpsu8glplUJ%2Fyh3PpnGUIJHt4S%2FCSw39LN8EGa4k27hgkFYMoifMflD4cnrsbZh%2FFftW5V%2F1nlr1llpIT8kWSR1Lohl7auh76I8KJoTGWkQ%2FzjgUOkF8NXyzD1rW0asoB9r5ng8uvGUeUlHDzvPkCANdHEo%2FSPJijlZ%2FMedJkRP7m2knCeCLj2xkpD1Z9Mxxzbv4A7TBXwyEiCTke5YDNMXqW6qUdCuS6beNd%2F5mKSq5J%2FKlO1lXB9hd0bdjYMwT9MCYnR7%2Bnu2x4Yp5jBC2QF593Y3zQ44JvVKKI0oowvhT34xu3pb7Pae8aBpiKEPsR7oH46QAdAgHQN8G%2BC80%2F3M9dVGO3NF1ReMJB3kd0yWRnjtUqgaQsGO0ahlYD5%2BfQ0ANzayCMxdPMaL5sc8d2OD5HgDvJOMeQzmhK5DmdsLoU4HIVG%2FSB4d%2FwVmyia5IW4EPiIZ6etiRPGtp%2FodoND5e%2FfdjCGqznV29FBOeNZchEklwmtPj3CjdEMrl9swrvnxduYVLS4maDqSAmzANI3QRzts0nBecSLUsrjC84fG8BjqkARsT9qt7%2BTFqpkPf00%2BFit9vCpWIujTAk094VEKk3aMw0MsoUYs21%2Fw01fhjEvqIJ9Fx6Ps5nSzqv397RMjayI7IaOkMHXMHtmgquBoNNSllK0aJS7ABr1DpxRC1Y42LZ6ZELYimSS6r4rOaH7LIwZhii4xC3QDvDs758tYsB%2BIyef8KJRsOFepPzqfcmEtCUDJ93Z7ChCKno5lp0mx22aurbq2A&X-Amz-Signature=c21d9ef1252f9d1d57f6a1c9bbdb5a0dc03a507dbb33483e725d1e07bb8ea8a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFVIQXXK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvRDdtUAw1NhB3LWAGivPwLL9HK%2BUs9O8rbs31xooXqAIhAMSRpA5DqfH3ZTY8PXxXzIHkHKGeP7shXTUIJ3IojKoSKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLSpDs665WhvxLQLUq3ANq2no%2BWKz5yXJ13r%2B2ccqx8M4WX9y8cpsJcLLZi4%2BrP9Uxl4%2FigP951MlrTqi212eiYoBDjOkJFd2EdKKy21Vjzpsu8glplUJ%2Fyh3PpnGUIJHt4S%2FCSw39LN8EGa4k27hgkFYMoifMflD4cnrsbZh%2FFftW5V%2F1nlr1llpIT8kWSR1Lohl7auh76I8KJoTGWkQ%2FzjgUOkF8NXyzD1rW0asoB9r5ng8uvGUeUlHDzvPkCANdHEo%2FSPJijlZ%2FMedJkRP7m2knCeCLj2xkpD1Z9Mxxzbv4A7TBXwyEiCTke5YDNMXqW6qUdCuS6beNd%2F5mKSq5J%2FKlO1lXB9hd0bdjYMwT9MCYnR7%2Bnu2x4Yp5jBC2QF593Y3zQ44JvVKKI0oowvhT34xu3pb7Pae8aBpiKEPsR7oH46QAdAgHQN8G%2BC80%2F3M9dVGO3NF1ReMJB3kd0yWRnjtUqgaQsGO0ahlYD5%2BfQ0ANzayCMxdPMaL5sc8d2OD5HgDvJOMeQzmhK5DmdsLoU4HIVG%2FSB4d%2FwVmyia5IW4EPiIZ6etiRPGtp%2FodoND5e%2FfdjCGqznV29FBOeNZchEklwmtPj3CjdEMrl9swrvnxduYVLS4maDqSAmzANI3QRzts0nBecSLUsrjC84fG8BjqkARsT9qt7%2BTFqpkPf00%2BFit9vCpWIujTAk094VEKk3aMw0MsoUYs21%2Fw01fhjEvqIJ9Fx6Ps5nSzqv397RMjayI7IaOkMHXMHtmgquBoNNSllK0aJS7ABr1DpxRC1Y42LZ6ZELYimSS6r4rOaH7LIwZhii4xC3QDvDs758tYsB%2BIyef8KJRsOFepPzqfcmEtCUDJ93Z7ChCKno5lp0mx22aurbq2A&X-Amz-Signature=4e67c685cbb453b27a209e82a873b5afefebb8636555c7c49052818f195e358e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DEMKESA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbhEokUecGMqKC88eKe3dv29jPO%2B2685VEg7ejP3xIzAiAvAReVEELYqkQ7qzh7DDwo3%2BdH%2F1FL%2BZGHJTBQ7GxQ4SqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd5SzLMoNNrOKknUEKtwDpW30qX%2BEzwyguYRyTx6xH4%2B5HlLTbNVVreAmOjXLtdQHqebR4OaJIJio%2BwO4P0dChnODV5AwM8Mohzmn0ron6LzHn8cgBxuJ4w9HlUP%2BW5iZfXGtbYr0a%2Fb8WkhEvZhgXJfxCGzukEjH8KQLXn7NUJ%2FIakwpekU6zFIqGidXYtDScM%2BD4EJ7rY0PUzCAa7ktQBZN1b0fRZ9dAZLCRezoOi07NK3FTC3j2nlx8NL0hdFuQX890ZjAaA0RWt0poTvvQqh%2BzMY0cOIP%2BJdCXZIbVsKkRZGj6iGoqYylEQWzKk2eF9soGWjqr7F5713UilbSwrIaRdcmw2mw6CS99o7QBe8M9gGnYunM18vK3%2BDxjNMNq0JHChId8jgaBUW8tGMfRhbeyw2grclW5oTx5O%2BOzUtRsW33nwOnKTkw2JWdCH%2FNfwAFA3sSKsIKDcYfbfHarqUkuTsAxtJW5UzKPNaF%2B0ytnd2kesxiUFZoMRmAev6jQMO0BR2I2YW5NWoafObq0FxOctKaQAW%2F0MgnpEF5bjm4nukRvKFQK6AHChPXx6toflZ3U8fRuE%2BJbENjvRA8MQ7MSN8DSzRcab83ViuyxEntAiRKBLE2Mm9jn7NF8QJiU17sWDvVr3JemTEw1uHxvAY6pgHpTCm9ys6MUP%2BwRJGUMY%2FlzWfwmK7q82pt0AXF5y6mV%2FBvD8m3o31bt9UKfL39%2F2bw2QNercrDOr3wqa4djfV%2FNrql7QfzT%2F2ntNWfb1TZOkKN9nIj7%2B0blI0KohuXTJy38NyGldBjULsdTdqaqz69exRmTvqfsQId9L71ID%2FYvryiptS%2Fua3oGWDM0xJi7yEsqzftw86NksDhybm%2BC9iErGJGYflQ&X-Amz-Signature=585df186b911f10d774514c8d0521496ac51fe40cbbd3866020c8d41715a2a34&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DEMKESA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbhEokUecGMqKC88eKe3dv29jPO%2B2685VEg7ejP3xIzAiAvAReVEELYqkQ7qzh7DDwo3%2BdH%2F1FL%2BZGHJTBQ7GxQ4SqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd5SzLMoNNrOKknUEKtwDpW30qX%2BEzwyguYRyTx6xH4%2B5HlLTbNVVreAmOjXLtdQHqebR4OaJIJio%2BwO4P0dChnODV5AwM8Mohzmn0ron6LzHn8cgBxuJ4w9HlUP%2BW5iZfXGtbYr0a%2Fb8WkhEvZhgXJfxCGzukEjH8KQLXn7NUJ%2FIakwpekU6zFIqGidXYtDScM%2BD4EJ7rY0PUzCAa7ktQBZN1b0fRZ9dAZLCRezoOi07NK3FTC3j2nlx8NL0hdFuQX890ZjAaA0RWt0poTvvQqh%2BzMY0cOIP%2BJdCXZIbVsKkRZGj6iGoqYylEQWzKk2eF9soGWjqr7F5713UilbSwrIaRdcmw2mw6CS99o7QBe8M9gGnYunM18vK3%2BDxjNMNq0JHChId8jgaBUW8tGMfRhbeyw2grclW5oTx5O%2BOzUtRsW33nwOnKTkw2JWdCH%2FNfwAFA3sSKsIKDcYfbfHarqUkuTsAxtJW5UzKPNaF%2B0ytnd2kesxiUFZoMRmAev6jQMO0BR2I2YW5NWoafObq0FxOctKaQAW%2F0MgnpEF5bjm4nukRvKFQK6AHChPXx6toflZ3U8fRuE%2BJbENjvRA8MQ7MSN8DSzRcab83ViuyxEntAiRKBLE2Mm9jn7NF8QJiU17sWDvVr3JemTEw1uHxvAY6pgHpTCm9ys6MUP%2BwRJGUMY%2FlzWfwmK7q82pt0AXF5y6mV%2FBvD8m3o31bt9UKfL39%2F2bw2QNercrDOr3wqa4djfV%2FNrql7QfzT%2F2ntNWfb1TZOkKN9nIj7%2B0blI0KohuXTJy38NyGldBjULsdTdqaqz69exRmTvqfsQId9L71ID%2FYvryiptS%2Fua3oGWDM0xJi7yEsqzftw86NksDhybm%2BC9iErGJGYflQ&X-Amz-Signature=11f14f41b435a84ea0bbfef813ff002661debfb3f0ffca1edf6aca3f0c3ae111&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DEMKESA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbhEokUecGMqKC88eKe3dv29jPO%2B2685VEg7ejP3xIzAiAvAReVEELYqkQ7qzh7DDwo3%2BdH%2F1FL%2BZGHJTBQ7GxQ4SqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd5SzLMoNNrOKknUEKtwDpW30qX%2BEzwyguYRyTx6xH4%2B5HlLTbNVVreAmOjXLtdQHqebR4OaJIJio%2BwO4P0dChnODV5AwM8Mohzmn0ron6LzHn8cgBxuJ4w9HlUP%2BW5iZfXGtbYr0a%2Fb8WkhEvZhgXJfxCGzukEjH8KQLXn7NUJ%2FIakwpekU6zFIqGidXYtDScM%2BD4EJ7rY0PUzCAa7ktQBZN1b0fRZ9dAZLCRezoOi07NK3FTC3j2nlx8NL0hdFuQX890ZjAaA0RWt0poTvvQqh%2BzMY0cOIP%2BJdCXZIbVsKkRZGj6iGoqYylEQWzKk2eF9soGWjqr7F5713UilbSwrIaRdcmw2mw6CS99o7QBe8M9gGnYunM18vK3%2BDxjNMNq0JHChId8jgaBUW8tGMfRhbeyw2grclW5oTx5O%2BOzUtRsW33nwOnKTkw2JWdCH%2FNfwAFA3sSKsIKDcYfbfHarqUkuTsAxtJW5UzKPNaF%2B0ytnd2kesxiUFZoMRmAev6jQMO0BR2I2YW5NWoafObq0FxOctKaQAW%2F0MgnpEF5bjm4nukRvKFQK6AHChPXx6toflZ3U8fRuE%2BJbENjvRA8MQ7MSN8DSzRcab83ViuyxEntAiRKBLE2Mm9jn7NF8QJiU17sWDvVr3JemTEw1uHxvAY6pgHpTCm9ys6MUP%2BwRJGUMY%2FlzWfwmK7q82pt0AXF5y6mV%2FBvD8m3o31bt9UKfL39%2F2bw2QNercrDOr3wqa4djfV%2FNrql7QfzT%2F2ntNWfb1TZOkKN9nIj7%2B0blI0KohuXTJy38NyGldBjULsdTdqaqz69exRmTvqfsQId9L71ID%2FYvryiptS%2Fua3oGWDM0xJi7yEsqzftw86NksDhybm%2BC9iErGJGYflQ&X-Amz-Signature=52dc06f7e5d1199b0db23037982e81db0a45582a53a74972ab6542f42ac60770&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DEMKESA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbhEokUecGMqKC88eKe3dv29jPO%2B2685VEg7ejP3xIzAiAvAReVEELYqkQ7qzh7DDwo3%2BdH%2F1FL%2BZGHJTBQ7GxQ4SqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd5SzLMoNNrOKknUEKtwDpW30qX%2BEzwyguYRyTx6xH4%2B5HlLTbNVVreAmOjXLtdQHqebR4OaJIJio%2BwO4P0dChnODV5AwM8Mohzmn0ron6LzHn8cgBxuJ4w9HlUP%2BW5iZfXGtbYr0a%2Fb8WkhEvZhgXJfxCGzukEjH8KQLXn7NUJ%2FIakwpekU6zFIqGidXYtDScM%2BD4EJ7rY0PUzCAa7ktQBZN1b0fRZ9dAZLCRezoOi07NK3FTC3j2nlx8NL0hdFuQX890ZjAaA0RWt0poTvvQqh%2BzMY0cOIP%2BJdCXZIbVsKkRZGj6iGoqYylEQWzKk2eF9soGWjqr7F5713UilbSwrIaRdcmw2mw6CS99o7QBe8M9gGnYunM18vK3%2BDxjNMNq0JHChId8jgaBUW8tGMfRhbeyw2grclW5oTx5O%2BOzUtRsW33nwOnKTkw2JWdCH%2FNfwAFA3sSKsIKDcYfbfHarqUkuTsAxtJW5UzKPNaF%2B0ytnd2kesxiUFZoMRmAev6jQMO0BR2I2YW5NWoafObq0FxOctKaQAW%2F0MgnpEF5bjm4nukRvKFQK6AHChPXx6toflZ3U8fRuE%2BJbENjvRA8MQ7MSN8DSzRcab83ViuyxEntAiRKBLE2Mm9jn7NF8QJiU17sWDvVr3JemTEw1uHxvAY6pgHpTCm9ys6MUP%2BwRJGUMY%2FlzWfwmK7q82pt0AXF5y6mV%2FBvD8m3o31bt9UKfL39%2F2bw2QNercrDOr3wqa4djfV%2FNrql7QfzT%2F2ntNWfb1TZOkKN9nIj7%2B0blI0KohuXTJy38NyGldBjULsdTdqaqz69exRmTvqfsQId9L71ID%2FYvryiptS%2Fua3oGWDM0xJi7yEsqzftw86NksDhybm%2BC9iErGJGYflQ&X-Amz-Signature=87fb252a0ba5eaecb9b793905df108089f8065c6f5084344da170228671d9c96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DEMKESA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbhEokUecGMqKC88eKe3dv29jPO%2B2685VEg7ejP3xIzAiAvAReVEELYqkQ7qzh7DDwo3%2BdH%2F1FL%2BZGHJTBQ7GxQ4SqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd5SzLMoNNrOKknUEKtwDpW30qX%2BEzwyguYRyTx6xH4%2B5HlLTbNVVreAmOjXLtdQHqebR4OaJIJio%2BwO4P0dChnODV5AwM8Mohzmn0ron6LzHn8cgBxuJ4w9HlUP%2BW5iZfXGtbYr0a%2Fb8WkhEvZhgXJfxCGzukEjH8KQLXn7NUJ%2FIakwpekU6zFIqGidXYtDScM%2BD4EJ7rY0PUzCAa7ktQBZN1b0fRZ9dAZLCRezoOi07NK3FTC3j2nlx8NL0hdFuQX890ZjAaA0RWt0poTvvQqh%2BzMY0cOIP%2BJdCXZIbVsKkRZGj6iGoqYylEQWzKk2eF9soGWjqr7F5713UilbSwrIaRdcmw2mw6CS99o7QBe8M9gGnYunM18vK3%2BDxjNMNq0JHChId8jgaBUW8tGMfRhbeyw2grclW5oTx5O%2BOzUtRsW33nwOnKTkw2JWdCH%2FNfwAFA3sSKsIKDcYfbfHarqUkuTsAxtJW5UzKPNaF%2B0ytnd2kesxiUFZoMRmAev6jQMO0BR2I2YW5NWoafObq0FxOctKaQAW%2F0MgnpEF5bjm4nukRvKFQK6AHChPXx6toflZ3U8fRuE%2BJbENjvRA8MQ7MSN8DSzRcab83ViuyxEntAiRKBLE2Mm9jn7NF8QJiU17sWDvVr3JemTEw1uHxvAY6pgHpTCm9ys6MUP%2BwRJGUMY%2FlzWfwmK7q82pt0AXF5y6mV%2FBvD8m3o31bt9UKfL39%2F2bw2QNercrDOr3wqa4djfV%2FNrql7QfzT%2F2ntNWfb1TZOkKN9nIj7%2B0blI0KohuXTJy38NyGldBjULsdTdqaqz69exRmTvqfsQId9L71ID%2FYvryiptS%2Fua3oGWDM0xJi7yEsqzftw86NksDhybm%2BC9iErGJGYflQ&X-Amz-Signature=8c05b434f723ad44dbbaea61207addc29f88bb3b113f08362d1aefd8eb9c585d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DEMKESA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbhEokUecGMqKC88eKe3dv29jPO%2B2685VEg7ejP3xIzAiAvAReVEELYqkQ7qzh7DDwo3%2BdH%2F1FL%2BZGHJTBQ7GxQ4SqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd5SzLMoNNrOKknUEKtwDpW30qX%2BEzwyguYRyTx6xH4%2B5HlLTbNVVreAmOjXLtdQHqebR4OaJIJio%2BwO4P0dChnODV5AwM8Mohzmn0ron6LzHn8cgBxuJ4w9HlUP%2BW5iZfXGtbYr0a%2Fb8WkhEvZhgXJfxCGzukEjH8KQLXn7NUJ%2FIakwpekU6zFIqGidXYtDScM%2BD4EJ7rY0PUzCAa7ktQBZN1b0fRZ9dAZLCRezoOi07NK3FTC3j2nlx8NL0hdFuQX890ZjAaA0RWt0poTvvQqh%2BzMY0cOIP%2BJdCXZIbVsKkRZGj6iGoqYylEQWzKk2eF9soGWjqr7F5713UilbSwrIaRdcmw2mw6CS99o7QBe8M9gGnYunM18vK3%2BDxjNMNq0JHChId8jgaBUW8tGMfRhbeyw2grclW5oTx5O%2BOzUtRsW33nwOnKTkw2JWdCH%2FNfwAFA3sSKsIKDcYfbfHarqUkuTsAxtJW5UzKPNaF%2B0ytnd2kesxiUFZoMRmAev6jQMO0BR2I2YW5NWoafObq0FxOctKaQAW%2F0MgnpEF5bjm4nukRvKFQK6AHChPXx6toflZ3U8fRuE%2BJbENjvRA8MQ7MSN8DSzRcab83ViuyxEntAiRKBLE2Mm9jn7NF8QJiU17sWDvVr3JemTEw1uHxvAY6pgHpTCm9ys6MUP%2BwRJGUMY%2FlzWfwmK7q82pt0AXF5y6mV%2FBvD8m3o31bt9UKfL39%2F2bw2QNercrDOr3wqa4djfV%2FNrql7QfzT%2F2ntNWfb1TZOkKN9nIj7%2B0blI0KohuXTJy38NyGldBjULsdTdqaqz69exRmTvqfsQId9L71ID%2FYvryiptS%2Fua3oGWDM0xJi7yEsqzftw86NksDhybm%2BC9iErGJGYflQ&X-Amz-Signature=bf023696b637ec2e913449522d7e2cc4ec2e14cf11f8c95dfbdc51dbc72f7e83&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDS33CCE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtqBIYMkhNaqZF7rY7s8%2BmV2SjWmHvBu8YDXIBVfc2WAIgQF2hvHns3y2UOF%2BPPiHA8xjKT3Ll4vHf2i47m4oosDsqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMAXTv4n0CskFgFtPircA1Ke%2BJP2Ww6EJ0IZjrgWxRVSQXxcew4Us%2BAtr4v3zSuYF2AE%2B6XeZCenvVy%2F3w2cvIV2OKXM%2BB3lYER1ZAhVLCUKJ7GvQUvqwACg7y2n%2FdpDB4aQuTjU7citcwp9cj3CYMdZSjAcvlPSruDDc6UlCTp5ZEREWBlluj7IJ74zRZmrN1Hd5Y82rDHNqSoQrPnJBxlxD5%2FAkQUtwWCAvHxMNMQxGCQAFvruHmRAxjI23rnkiXVA3S2AaG6S%2BVKx34XyH1Oa131Y4WkzB22AbdeJQPavoF9Qunb3g6nqgDmhHQ%2BGLZ9XFkE3p0ej0lA3h1N%2FRQ3XDHwjx%2FyR%2B%2FPqCe3es8Uu5YA1CLizNU9YZqNqkUoX5MFMBQ%2Fv1RZBSShM9n%2BFBPJcp9MrGWLdIO0UMmr8AT8r64rqX%2FxsucYpBR1til%2BJF2sohuOiJOpQhseUA%2FgNkJJCYn34KyjijrO1ifjJG01eVtVcK5hAcwk1oRwLCVLlcBzjssBOmmJg4P%2FljNNmhLOXyDH40EgkYO5%2BC9%2BWsLWTgjILnhxMx9fpYdeEwq6%2BcFmQHY4DgYB4MQkIBaieJYo0EDEYbs%2FrF5B7EGEpWMMQ2YXZhRi2vLNvX%2FsQpIMjsjNUURTN1T8uzJz3MJji8bwGOqUBWdpiYk7pO8768nwhbiBbEBgNoNwYLGuEEAjiazZsNpfWZIjrtYXYc8j4INphmMwYlQa%2FhGViePD1gP87p5pSW38wK3XI6f6cgSEF9tW0W3ZrODuBh6glYZq5CzNERJg5wKORGRWqDxUEX0Y5y7EQHWmZKIjTh60zD2pH%2FKA3GXtpQwtlVOkRZ2zbkIRCg2rqUQRxolbUiKVnxsw0Gn%2BOor4IpR4V&X-Amz-Signature=05071af341e5e457ec285840ab8d6636247eb412b04c81faa9b7aad77d65d64b&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NSWYMKG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKF5ATnpKHxnYa1ckDpFQt7z2Nvwluuo2dWfjRLu5r6AIgBGGcSsTHvS%2BeKnWlLVRMY3GjUiW%2FJRQMkyzxxP7FmdoqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBFLh4BrQAluj5Kw5ircA9m5B%2FI%2FE60MgA5tst0L%2FOqrcuoIzaweL1kUPfP502Ip%2B4mV0n5pRSzsAji3K9G%2FaqkEB%2B7WsxxQ%2BHP7UT1zbG32%2BAiZzBsJkFeMG%2BJrhcHXsCIG1wubpMF7NPmrcX4SHPo7A6wG%2F%2BR6RHfvVtdIhONmDhooNzJZ6%2BVFXOUPLMtuCDZuATFl5ux79ZjYvIPKGJ%2BZIkRZd7Kvv9sSFlm05Cpv2BB2WQhMY6pD%2FpGzevxxp407v%2FgzN2th71MuXvkuQUa4Ks2WQ2W7OxveOsinoN4tRhRXqpgWOrWnAOupp3GDLxPOZ1DlrVYvcWeaUe9T3XiCh0e3CTZtrHeCaUQaL7qmjkLU0gbH8AiOYtPW3citXzp9dGFzsEFoxpvSSzNEg04SCtxIRh%2Fx4wg5Ftku8dKzYoONboo%2BhIh3I7nQdZMPWXi%2Ba%2BM766hhewVDOnkzW9MWunJih3AnFO1k%2B3Wm5vS%2FXJ6c%2FaXyP6OvEyChmDc8RPWickDieNUwbRWnqYA9oa97LHhQnPQb%2BKSTxs%2F%2BF3IuD%2BbCSuIYlNetMVF94IZRA%2B12wG26rrjIvikn0u9YxTCWZMR2BteoVGQkzclEnmL5D6w8FEw4Hnmc6w1gxRrvf%2BWRkif%2FtbBpxlkJMMDi8bwGOqUBMLcZjm6Nv%2F0o7VeLp%2FsmxSxL8kGdrRMlOI2N5mEAsY2Yk5X1IBBzTLLmQjbKGYyHexLW5PekgFTEaV9Uo0qKJuEsnkPSD8z7HakWAPrnH7%2Bbjk7N7PgwouyZgVprM8%2F9fwqOHXYembLdsr9s5MdcxayW8KIXOdAFSJDhWsBLpA8aZudCf4jzDkbRvm%2FlIjpguBA1Nj%2BrcZQ4C3npRYIqwnwIte5%2B&X-Amz-Signature=7827467387ffc4c8239c722edea46062edaaf1bed7bbda86b9f18588e1a972d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DEMKESA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbhEokUecGMqKC88eKe3dv29jPO%2B2685VEg7ejP3xIzAiAvAReVEELYqkQ7qzh7DDwo3%2BdH%2F1FL%2BZGHJTBQ7GxQ4SqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd5SzLMoNNrOKknUEKtwDpW30qX%2BEzwyguYRyTx6xH4%2B5HlLTbNVVreAmOjXLtdQHqebR4OaJIJio%2BwO4P0dChnODV5AwM8Mohzmn0ron6LzHn8cgBxuJ4w9HlUP%2BW5iZfXGtbYr0a%2Fb8WkhEvZhgXJfxCGzukEjH8KQLXn7NUJ%2FIakwpekU6zFIqGidXYtDScM%2BD4EJ7rY0PUzCAa7ktQBZN1b0fRZ9dAZLCRezoOi07NK3FTC3j2nlx8NL0hdFuQX890ZjAaA0RWt0poTvvQqh%2BzMY0cOIP%2BJdCXZIbVsKkRZGj6iGoqYylEQWzKk2eF9soGWjqr7F5713UilbSwrIaRdcmw2mw6CS99o7QBe8M9gGnYunM18vK3%2BDxjNMNq0JHChId8jgaBUW8tGMfRhbeyw2grclW5oTx5O%2BOzUtRsW33nwOnKTkw2JWdCH%2FNfwAFA3sSKsIKDcYfbfHarqUkuTsAxtJW5UzKPNaF%2B0ytnd2kesxiUFZoMRmAev6jQMO0BR2I2YW5NWoafObq0FxOctKaQAW%2F0MgnpEF5bjm4nukRvKFQK6AHChPXx6toflZ3U8fRuE%2BJbENjvRA8MQ7MSN8DSzRcab83ViuyxEntAiRKBLE2Mm9jn7NF8QJiU17sWDvVr3JemTEw1uHxvAY6pgHpTCm9ys6MUP%2BwRJGUMY%2FlzWfwmK7q82pt0AXF5y6mV%2FBvD8m3o31bt9UKfL39%2F2bw2QNercrDOr3wqa4djfV%2FNrql7QfzT%2F2ntNWfb1TZOkKN9nIj7%2B0blI0KohuXTJy38NyGldBjULsdTdqaqz69exRmTvqfsQId9L71ID%2FYvryiptS%2Fua3oGWDM0xJi7yEsqzftw86NksDhybm%2BC9iErGJGYflQ&X-Amz-Signature=b4bbaf6207409821bf693868aeb7f4887dd61c3dec8de4358fdc4c548c660b2a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DEMKESA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbhEokUecGMqKC88eKe3dv29jPO%2B2685VEg7ejP3xIzAiAvAReVEELYqkQ7qzh7DDwo3%2BdH%2F1FL%2BZGHJTBQ7GxQ4SqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd5SzLMoNNrOKknUEKtwDpW30qX%2BEzwyguYRyTx6xH4%2B5HlLTbNVVreAmOjXLtdQHqebR4OaJIJio%2BwO4P0dChnODV5AwM8Mohzmn0ron6LzHn8cgBxuJ4w9HlUP%2BW5iZfXGtbYr0a%2Fb8WkhEvZhgXJfxCGzukEjH8KQLXn7NUJ%2FIakwpekU6zFIqGidXYtDScM%2BD4EJ7rY0PUzCAa7ktQBZN1b0fRZ9dAZLCRezoOi07NK3FTC3j2nlx8NL0hdFuQX890ZjAaA0RWt0poTvvQqh%2BzMY0cOIP%2BJdCXZIbVsKkRZGj6iGoqYylEQWzKk2eF9soGWjqr7F5713UilbSwrIaRdcmw2mw6CS99o7QBe8M9gGnYunM18vK3%2BDxjNMNq0JHChId8jgaBUW8tGMfRhbeyw2grclW5oTx5O%2BOzUtRsW33nwOnKTkw2JWdCH%2FNfwAFA3sSKsIKDcYfbfHarqUkuTsAxtJW5UzKPNaF%2B0ytnd2kesxiUFZoMRmAev6jQMO0BR2I2YW5NWoafObq0FxOctKaQAW%2F0MgnpEF5bjm4nukRvKFQK6AHChPXx6toflZ3U8fRuE%2BJbENjvRA8MQ7MSN8DSzRcab83ViuyxEntAiRKBLE2Mm9jn7NF8QJiU17sWDvVr3JemTEw1uHxvAY6pgHpTCm9ys6MUP%2BwRJGUMY%2FlzWfwmK7q82pt0AXF5y6mV%2FBvD8m3o31bt9UKfL39%2F2bw2QNercrDOr3wqa4djfV%2FNrql7QfzT%2F2ntNWfb1TZOkKN9nIj7%2B0blI0KohuXTJy38NyGldBjULsdTdqaqz69exRmTvqfsQId9L71ID%2FYvryiptS%2Fua3oGWDM0xJi7yEsqzftw86NksDhybm%2BC9iErGJGYflQ&X-Amz-Signature=8ddbefa5d87b07602757c47c9b8ec283926b2e931ead43426f21dde9710d2312&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DEMKESA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbhEokUecGMqKC88eKe3dv29jPO%2B2685VEg7ejP3xIzAiAvAReVEELYqkQ7qzh7DDwo3%2BdH%2F1FL%2BZGHJTBQ7GxQ4SqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd5SzLMoNNrOKknUEKtwDpW30qX%2BEzwyguYRyTx6xH4%2B5HlLTbNVVreAmOjXLtdQHqebR4OaJIJio%2BwO4P0dChnODV5AwM8Mohzmn0ron6LzHn8cgBxuJ4w9HlUP%2BW5iZfXGtbYr0a%2Fb8WkhEvZhgXJfxCGzukEjH8KQLXn7NUJ%2FIakwpekU6zFIqGidXYtDScM%2BD4EJ7rY0PUzCAa7ktQBZN1b0fRZ9dAZLCRezoOi07NK3FTC3j2nlx8NL0hdFuQX890ZjAaA0RWt0poTvvQqh%2BzMY0cOIP%2BJdCXZIbVsKkRZGj6iGoqYylEQWzKk2eF9soGWjqr7F5713UilbSwrIaRdcmw2mw6CS99o7QBe8M9gGnYunM18vK3%2BDxjNMNq0JHChId8jgaBUW8tGMfRhbeyw2grclW5oTx5O%2BOzUtRsW33nwOnKTkw2JWdCH%2FNfwAFA3sSKsIKDcYfbfHarqUkuTsAxtJW5UzKPNaF%2B0ytnd2kesxiUFZoMRmAev6jQMO0BR2I2YW5NWoafObq0FxOctKaQAW%2F0MgnpEF5bjm4nukRvKFQK6AHChPXx6toflZ3U8fRuE%2BJbENjvRA8MQ7MSN8DSzRcab83ViuyxEntAiRKBLE2Mm9jn7NF8QJiU17sWDvVr3JemTEw1uHxvAY6pgHpTCm9ys6MUP%2BwRJGUMY%2FlzWfwmK7q82pt0AXF5y6mV%2FBvD8m3o31bt9UKfL39%2F2bw2QNercrDOr3wqa4djfV%2FNrql7QfzT%2F2ntNWfb1TZOkKN9nIj7%2B0blI0KohuXTJy38NyGldBjULsdTdqaqz69exRmTvqfsQId9L71ID%2FYvryiptS%2Fua3oGWDM0xJi7yEsqzftw86NksDhybm%2BC9iErGJGYflQ&X-Amz-Signature=4ca733e5cb785e175c63ae18f69c4070efb289e760d3471656c441dd13117690&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDPQBG5E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGKj8mXcD%2F4Aes4T3Gabtmy%2BlpxtyLlxEJRxiJJ7anYQIhAOzOjaZfq6TGeECYfPNpxesqTXswizzgCqlK0Oeqe03EKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUgQkgJsDO0ZacmEMq3ANHAxTo7Osg1gGxzTijhzGThi7dXp7T%2FD1TBXZEbvsJDLKBB97VWlcwnTs9bUwQ4eh%2Br4kJO3nKwhLqPcnIDb7ODOa52tGR8KQzVBnVonslN764RFJt353aMopOlcp%2F3OWn2zDs2J63GEMUXNx2iPpOYyNCnk1yGtiNdKvXgnMQcfS16TOhQnp%2Ff%2B9YmDBQTouEMRVVFgkZRqqDOxfFGDz1g7T%2BKLEL9LYau2En2jwxjrQ61NckMxAnq2EYbAgsTyTs6R4yNrv8PNEDn6MANaOET5YjQB5TK9FHLWFTGpFXW1NnRkIAnqFKXmTTwgvbclpBh%2BPAyUmzXt0fss1y%2B7CW%2FefQpJDKrv8y2zzNMXR9yv4wFghghGIKpk0skjzM%2FjonVKJunKqerDSMWyzO9agRnpqe7LvEbA9Vyh49hT0VKoVcwr1O6r%2F8AQYR6cd0Mxb2JqJ3lXvidtZlxTVfyB0fmhzVCKr8ZLWjB6rNMwx%2B59YtRFbeC8u%2F3%2Bh2s5%2FYvd8fqPE%2BXDMNTki1CC4JP63uaLnR%2FKcHKfypMMTqimSr4Nj7mr2000CTB1ByDP8wWI1kYqqpnUGjg9cIsAKB5qTcYhbF87mZt1uoJ1C1MTU5tw7xI3k37P9OeVTM%2BTCF4vG8BjqkAX%2BDwX3%2BC9lwDJwXWx2sQ8BcqP%2FX%2B%2FvJfAHTrqGQo0LusZPV7CUKjWmL4m3hpJxgu6Rcs7GNNJkhxosDsEIh8i%2FHHwwYsTEjWybb1Fk%2Bkwz15XL%2BUtEJVa6LcR6VDgqKoYmI8J5UqDL7T0PtvbK5BdJ4GNTYN628yopfBvlrmtyqbGhkCLKmqv%2B8v97Ye9NVdQQ%2BorzBlGNzua6UhkjU1VDJR5rD&X-Amz-Signature=e9df82839f4a98898d4e131aa295304d95c0946a57370a2d7f76d4bf2b03310e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7IGPUKP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB6JT7NCGCyR6RF7pYRJaV2v5Gi8zP7s9T2of%2BuPdLv5AiAnerHf24VkC1J1fiq4wc8CnE5GYMi%2BTYb%2B0KzED21u0SqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQVcdK4jdCXKAmfkJKtwDaB95trxnUuDawUQhrx%2FYFBL357qWRQIem853z%2Bl4MGXzSustUH9W8DBx2uOFE0LCVstHBXh1ZUpsRHWarnaiMRZaQf73NrFDk2%2F0YuVHUFSMcmMl0fXZYbAyaMF%2F3osddFQ8ZH7XJNC2R3hIWpkAemDgwELYy001muK8W7%2FmfAUYO8WT7uYdzYmQJg3t7hDKqnGU9boVUEKTHG7N5jgB6Tt8y0H8YbiapuxRGIoCxXeX9MAUKOyHteVGzUdDEadAVuxzNs%2Bhl3QcQlOqE3U7gmREQjtI8XcHtld%2BlbhZ3MA5u3YRxvaVCUcubN8IK2AcUm78EBaDUub7Ym3B85Msff4NJrP87RhKX%2BKZNS30jm7VJpU3qjGHigyw2vY0iWYcfw1U2u4h9ADjCDI1I2HHE7UFbmdGdgEcguyeHvVrJXgQ3rdh63PkL5CzekmJkhI29600VCXd0McJ%2BVt5RZFwV6bHU0%2B720OFJlTxunmVtTZ9uv3GpLF6%2B4QYxO%2BjNmLtT7sQhhrmRn0rNV%2FaK99ne0VZw%2BbOnTXOddvoXNxasxsdIUwRkXhmK7Teobn%2FcdtttfAI7F244QpMHnCeIg6yjFSH3nHxaBLJLsZxvJmqsuSGcc0lcyLtWuwp1Ogwh%2BLxvAY6pgFLWkgLj9nuxNIZiHEQ9anS4KdjFODurvBxsbgwU%2BSXGC%2BWg2sPl21QljIld07FHvjp7EhWTAYK1o6RRK72JerwoSZfpRWIY73WWVPKMi17qlhYdFz976d8tXkCeLtgsNypiIiS0yROBdVrT9IyIkZKNkQT0hKucKnzZH0W1hoO6YZpI8PWjAcoC4BoRUoQFALtKk0O8tm8sLJJjqqt3OovPza%2FycqG&X-Amz-Signature=54c0a6ee9a804d05b8115fa5b301dc23891c870cbe508821ec63447b618561a6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7JRY3C4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHd1NFIfEjb%2BjMcsvZmQkttU89JLA5vjIbfXO6jLNC7EAiEA7ca4aawV6HkbaKzr%2B881OXVuBr6kn5bBhJxszbKLWvcqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGRgi3wjVtbkzKOemyrcAycDrY%2FrMWUtWuldhFiqTV5G1gV%2FJwaEbfEvb0UBRsNg%2BTDNuTlk69zOZ6Dpl%2BpbDTzkS0ks68sTp7Rqmeb3XUEczOSkCT9Dvz92yrF%2FVAS5hY5GN15eZD4mQqXbDKNIqBbHtQkJM2sivdG259zxmuQ28Lb04bIRxxuXwTMyUeaJ2zVfHr9SxK18afdo71YdQLEYvBcboCHYINe4t6Yl%2Be3v6Sc1wqvSyYDDwGPhcY7C6QjW5tRKGvrtP6Ph%2FezmJb4JGeIReA49h%2BSm3OESjyDFfOlE5WmxoJi9X18S3W8AyCKHQhTSQOMwX%2FJ9wVKWs7LxPXIHz0ysrLPyy0Ec%2FDD2dJPywp3ZLOTRcRYsLg5H%2B71aUp629VAUYrELfDfVcJjZA04nvOlTV8PbQsTWRACoHdYTADDsq04Nuv4iVaypMMoSYrGXcpP1vZBC0IwMl1oxnVCOYMYXebUWnsXqVpp7AppmWJS1ppLB0HaE8C0CPHheF55YrWG%2BQJ%2BKCjSph22FR6REoBuqRAX0zzshpLjOappke0SQ4ofu9LiX4b%2BQx1is6Ts%2BgS0dj2B0to1IAslJE2Ku5NZBbiC4x59O6gKn%2FUGAhWoHo1nDBG%2FgikOtwOywt6BfMlYqSLvkMIHi8bwGOqUBH0cRFs4cCKEE9lczPdi3l99S2qysaOH9AUMXyAStmYqi7XUS7qPhRXO2DSCTJSMiUj2VEGfwml8L4uNMwC43gmJtLXDjEQZMjZ%2Bp%2FJaMZgJfO4MjpWpwD9YneOjZOz5a3CAd2X8ZJw4L%2FuY0%2Fm3421n7aDJcbkl%2Bs8Ks1MydPLq3MA6c8IsH%2Bq893r5L2BxTMmePbx8aHtJL7RzejEb9pbMbDTa4&X-Amz-Signature=5fb598237e2fb5acccb4f3f65a241ea3ccf6f046511b46ad262a14774a69eb24&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN7EKPKX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXjzON5G049mN0etJbBtdmkNJItdU3hgnGnWSHRw0B6AiAMEmrNkSJjMtijTU1HByVQzsqMzKEZ%2F95S1oc%2BOIrotCqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZ38Zw0QUP%2B0kgtoxKtwD3QiRd8kM4Tc9t5a%2Fr37OrSC3NudtJ1kvAnZaFCarw3HB%2B%2F9rJO2VWHg9an6QWJUtAG6m2SLUkiTEmPU%2BRfCDfl6TVXt%2B%2FmsXi8LQb%2B4yl1T%2BJ2UD88YsBIdNzLt%2FekwwH5H%2Fv%2By2CLsvRYSenEJ0kfucR3S3p3L7fXZj36Tib8ruAI6GDfZAVbCh5v9JBsnpaDv6ItoaBoYWx8%2BwcXKFNKzaeMq83BCbUuY5hx5Oi9WoNZUBPO98VgNenIRSaFX370ehIB4acYsrmNh2fcOAHuRBzL%2FM4e4nL8v6RYqYNAUDzm%2F30C6gWpQu0X%2FMcb61fc0CLVUm3HNoQVZu86G%2FezYfZyaTOoTKj0WZdsMztrnM8Ch0fLrDWxK5LuDbmjSeNeY8fcjjv%2FA1%2FbrXnHVchhvcMfWHPvJ7%2FPuWoTqLJp3Dpg%2FigA%2BOu2lr7vCumn1E1x1v93qNSatElD2f2eKeMHMGdxTHzyIwVAxheCSvDRBn76DsEnjubLlNQ43PwRK1L3VJ%2B8Yn6zsOmiSUnYhO5f3Xgi3gfN7vFgFPHTfGY0P5bWlyj7QfjjpHyQSzmqmOP9j1a%2BRW5SvYbhhy9q15jzYaWXLyYQ0qgpdOe%2F8yCB%2BQpcs9ETFKWaqWI3ww8%2BHxvAY6pgHFRTw9tJs5RSVeu%2FWRA4vG1lKn4hYWHiEAu3GjqcmJm0ONMc2XxhJPM2Z%2Fdu3Jhjhc9NhfPExFwxoV7riqfq2XF9%2BRwfyR8%2BKpCAu%2F76Tl8WAB%2FhcwRvnmIh8Y%2FOZPFQTvOnUmjTpjY1PCjeonArcsv66A3yuyw2yZO8KhI7ehuDOTsCnRVE7cM5snim2Fe5DHDCED14sPJgWLOKEoLeI9zynDnk%2F0&X-Amz-Signature=a39d7a512ffd3a34cc49bfac15da9451cb7232f0d42284070b412a3c67c49d48&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN7EKPKX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXjzON5G049mN0etJbBtdmkNJItdU3hgnGnWSHRw0B6AiAMEmrNkSJjMtijTU1HByVQzsqMzKEZ%2F95S1oc%2BOIrotCqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZ38Zw0QUP%2B0kgtoxKtwD3QiRd8kM4Tc9t5a%2Fr37OrSC3NudtJ1kvAnZaFCarw3HB%2B%2F9rJO2VWHg9an6QWJUtAG6m2SLUkiTEmPU%2BRfCDfl6TVXt%2B%2FmsXi8LQb%2B4yl1T%2BJ2UD88YsBIdNzLt%2FekwwH5H%2Fv%2By2CLsvRYSenEJ0kfucR3S3p3L7fXZj36Tib8ruAI6GDfZAVbCh5v9JBsnpaDv6ItoaBoYWx8%2BwcXKFNKzaeMq83BCbUuY5hx5Oi9WoNZUBPO98VgNenIRSaFX370ehIB4acYsrmNh2fcOAHuRBzL%2FM4e4nL8v6RYqYNAUDzm%2F30C6gWpQu0X%2FMcb61fc0CLVUm3HNoQVZu86G%2FezYfZyaTOoTKj0WZdsMztrnM8Ch0fLrDWxK5LuDbmjSeNeY8fcjjv%2FA1%2FbrXnHVchhvcMfWHPvJ7%2FPuWoTqLJp3Dpg%2FigA%2BOu2lr7vCumn1E1x1v93qNSatElD2f2eKeMHMGdxTHzyIwVAxheCSvDRBn76DsEnjubLlNQ43PwRK1L3VJ%2B8Yn6zsOmiSUnYhO5f3Xgi3gfN7vFgFPHTfGY0P5bWlyj7QfjjpHyQSzmqmOP9j1a%2BRW5SvYbhhy9q15jzYaWXLyYQ0qgpdOe%2F8yCB%2BQpcs9ETFKWaqWI3ww8%2BHxvAY6pgHFRTw9tJs5RSVeu%2FWRA4vG1lKn4hYWHiEAu3GjqcmJm0ONMc2XxhJPM2Z%2Fdu3Jhjhc9NhfPExFwxoV7riqfq2XF9%2BRwfyR8%2BKpCAu%2F76Tl8WAB%2FhcwRvnmIh8Y%2FOZPFQTvOnUmjTpjY1PCjeonArcsv66A3yuyw2yZO8KhI7ehuDOTsCnRVE7cM5snim2Fe5DHDCED14sPJgWLOKEoLeI9zynDnk%2F0&X-Amz-Signature=9ee6353aaf032c73550fe00172df784737976f1686960197c6bbd8c9bcdebbaf&X-Amz-SignedHeaders=host&x-id=GetObject)

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
