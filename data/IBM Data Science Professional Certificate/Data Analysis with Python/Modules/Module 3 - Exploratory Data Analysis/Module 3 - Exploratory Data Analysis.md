

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672FMXJY6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFasudFE79S%2B6qCCxK5zWK%2FTxdVraszGy7qTOkzepGF7AiEAw2bTcpsNmQdKAPsYYPaO5KlmUg%2Fi1fmHkUsdW2VVXqsqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4Nzu9wfIFM%2BGvY0CrcAw9IoMsHlOukimCM4UQow0%2F%2FjS1vZDqwF1UlgrqBmd%2BWodHO2wR1NEHL%2F1EM7fJYnNYiDcIluP0Bq94LDYRG8GiAVKXfQaSPEoYIs5Q%2FNkKHA0dlLXUOC8TBUXmhMrpBhWLz35cqPczOQpZ8K2eTt12midxY2PrtSUEqh%2FskVrhcWAclz5HyvF%2Bo7NeNTmIBuWXhuLJUODgMRAOwl6yD3umdPFvFWnXXtSoECm9DNEq6Ms3JWzOfFu4cFENgIIGzv2I%2F5IdU1FFsCd3VG0vu9Uf760S2G%2BeoRt2nZc3o6sZcndxDqta1xyv1GezKB2rEE6Y6lpEO2H36Eom1heILF6cWY4WVeaa6UdPVVHks%2FDeCglCdVgEHZu6tHWqdrIO4gyv4SYZdMAmQQJzDpGgKFHDr6JoaEUkwBZH5uSXllrP3EnFlmhbOVVYr7b6k6zfILjjTYK3bdZD3Yi1yIbjt9TfZqBwH26VIyJe%2FC8730%2BwoZY5CQQCFZrUWUyNBhfajDHt4Y8wZwpDgPe515v489DE%2FmXAHUOfFbkSd1oGaGcAcqzHFMozE7AhOTRu09lifGdWwitxyjorXmKquRrIhIRtWs4juvwwIB%2BV%2FXfBlhgguKxNBsQu0NneXJ9R4MKXN9bwGOqUBtfFfoV9mgYfLLOZ%2Br7JU82RNcbHGqrPCx63HqZ3QpH6eWYnW%2FK2qjzaaz1HJJvlX6rOWKjGNRbUGof4g3GHIyqVJPKCWAT9HDcTx4lebKkn2xNrnyI70QNaq1GgjprcCLH7Vb9gWjNS1D4jIQFO8pIfF0r4QfDvcywjWLRtyuDEUNwHYlUgXwhl8vKocmjBV80njLhZWQfAIJUK4Nrh12tTKFKI6&X-Amz-Signature=cfcb9e86348d81ea93f10dd315bb857b9f2703fed81ba15649954d10740e0546&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672FMXJY6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFasudFE79S%2B6qCCxK5zWK%2FTxdVraszGy7qTOkzepGF7AiEAw2bTcpsNmQdKAPsYYPaO5KlmUg%2Fi1fmHkUsdW2VVXqsqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4Nzu9wfIFM%2BGvY0CrcAw9IoMsHlOukimCM4UQow0%2F%2FjS1vZDqwF1UlgrqBmd%2BWodHO2wR1NEHL%2F1EM7fJYnNYiDcIluP0Bq94LDYRG8GiAVKXfQaSPEoYIs5Q%2FNkKHA0dlLXUOC8TBUXmhMrpBhWLz35cqPczOQpZ8K2eTt12midxY2PrtSUEqh%2FskVrhcWAclz5HyvF%2Bo7NeNTmIBuWXhuLJUODgMRAOwl6yD3umdPFvFWnXXtSoECm9DNEq6Ms3JWzOfFu4cFENgIIGzv2I%2F5IdU1FFsCd3VG0vu9Uf760S2G%2BeoRt2nZc3o6sZcndxDqta1xyv1GezKB2rEE6Y6lpEO2H36Eom1heILF6cWY4WVeaa6UdPVVHks%2FDeCglCdVgEHZu6tHWqdrIO4gyv4SYZdMAmQQJzDpGgKFHDr6JoaEUkwBZH5uSXllrP3EnFlmhbOVVYr7b6k6zfILjjTYK3bdZD3Yi1yIbjt9TfZqBwH26VIyJe%2FC8730%2BwoZY5CQQCFZrUWUyNBhfajDHt4Y8wZwpDgPe515v489DE%2FmXAHUOfFbkSd1oGaGcAcqzHFMozE7AhOTRu09lifGdWwitxyjorXmKquRrIhIRtWs4juvwwIB%2BV%2FXfBlhgguKxNBsQu0NneXJ9R4MKXN9bwGOqUBtfFfoV9mgYfLLOZ%2Br7JU82RNcbHGqrPCx63HqZ3QpH6eWYnW%2FK2qjzaaz1HJJvlX6rOWKjGNRbUGof4g3GHIyqVJPKCWAT9HDcTx4lebKkn2xNrnyI70QNaq1GgjprcCLH7Vb9gWjNS1D4jIQFO8pIfF0r4QfDvcywjWLRtyuDEUNwHYlUgXwhl8vKocmjBV80njLhZWQfAIJUK4Nrh12tTKFKI6&X-Amz-Signature=22cb164dc9a19877a59ac6f3b33d02b7e2d654a251237d5df6deb554a580c56d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672FMXJY6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFasudFE79S%2B6qCCxK5zWK%2FTxdVraszGy7qTOkzepGF7AiEAw2bTcpsNmQdKAPsYYPaO5KlmUg%2Fi1fmHkUsdW2VVXqsqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4Nzu9wfIFM%2BGvY0CrcAw9IoMsHlOukimCM4UQow0%2F%2FjS1vZDqwF1UlgrqBmd%2BWodHO2wR1NEHL%2F1EM7fJYnNYiDcIluP0Bq94LDYRG8GiAVKXfQaSPEoYIs5Q%2FNkKHA0dlLXUOC8TBUXmhMrpBhWLz35cqPczOQpZ8K2eTt12midxY2PrtSUEqh%2FskVrhcWAclz5HyvF%2Bo7NeNTmIBuWXhuLJUODgMRAOwl6yD3umdPFvFWnXXtSoECm9DNEq6Ms3JWzOfFu4cFENgIIGzv2I%2F5IdU1FFsCd3VG0vu9Uf760S2G%2BeoRt2nZc3o6sZcndxDqta1xyv1GezKB2rEE6Y6lpEO2H36Eom1heILF6cWY4WVeaa6UdPVVHks%2FDeCglCdVgEHZu6tHWqdrIO4gyv4SYZdMAmQQJzDpGgKFHDr6JoaEUkwBZH5uSXllrP3EnFlmhbOVVYr7b6k6zfILjjTYK3bdZD3Yi1yIbjt9TfZqBwH26VIyJe%2FC8730%2BwoZY5CQQCFZrUWUyNBhfajDHt4Y8wZwpDgPe515v489DE%2FmXAHUOfFbkSd1oGaGcAcqzHFMozE7AhOTRu09lifGdWwitxyjorXmKquRrIhIRtWs4juvwwIB%2BV%2FXfBlhgguKxNBsQu0NneXJ9R4MKXN9bwGOqUBtfFfoV9mgYfLLOZ%2Br7JU82RNcbHGqrPCx63HqZ3QpH6eWYnW%2FK2qjzaaz1HJJvlX6rOWKjGNRbUGof4g3GHIyqVJPKCWAT9HDcTx4lebKkn2xNrnyI70QNaq1GgjprcCLH7Vb9gWjNS1D4jIQFO8pIfF0r4QfDvcywjWLRtyuDEUNwHYlUgXwhl8vKocmjBV80njLhZWQfAIJUK4Nrh12tTKFKI6&X-Amz-Signature=d125650f9eb08c3f8e41f39eb9555689964b1dd406a59a48ff7ce3dcb47095a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643HAZAYA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHehnaHavpBatjPy9qFr1aqIR4mDaDjdDNcn1uaeE95AiEAt1iHGBvqgQGQ1P5q6hMP0%2Ft%2FUK%2BwCssyk7%2BJX2XnqmUqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjamEIQ5Jw7nBmV7yrcA7RUqtKtw9Hckt8KJHebKHqkVHrks3sv4bOKjXzStEP9ybpUbb3pj4rjnNkBwOf2fmiIBxWzj%2FWGFGJ9f9DJb%2F3EYu4Npy8h8mHox%2FUEFrRFQrivsu0VeXb5JCydUqSQwMPrepkI4vglN1GAN8RYEfq3sFRGfzgCAZTI34mY%2FvnbeDYxNjOvoQdmR43h2tl0OGnL8UOrFbaMqb%2FhaVqhJJfCiIB6v3H6yk6D9sRYoEoIZbe9WNw7%2FLDzXC%2Fx3GReGB9sufIgIXiB57TAuVFkT%2BM9qQGMhwP5QB0mMtvAKGgjV3sfzIypQRA6AX2QnzppOWs%2FFL9nI2WLNGGghV%2B33hR9nkZyqBgG1s6SpXofpwAKPHZRAvXD5A%2Bb4WIoyfKHtYX%2BMIMcLNY7qs9uSFLvmPSM2rAh9bbI8GpTMkV43iJr5CJFFE8us9dZBmCZnCsDT7RKBIXpiwMKaHkwEB0phlq13SeaKXgswPZ6y0KoA9BYSJCrKnSXIdAs5%2BR4jJr8sM7zJDLlwLoz2IARauFGFJaG0AQGuDkzR6adHORopxfDK4Ji8f4yRGEb91Lbyvf%2Bo6l8u7Dyy98VCrY4sDNazszQ9FzFO%2FyDolVYHm%2FhvZ7ImeZgQ7QeANwpPV73MJvN9bwGOqUB0NR%2BYLLY%2BFITq0B2tuOfRLYt4SWEHKKhUswn7HEoa36ZDMdoRakhacipjqbbyyxDBmKvL4Jy0ZTfw79Y3M1uIPkBevznXMAFqAej7CWWC0KBU8oXdz0jGN20iPZxJdqM9YSKDsT6c8nXBaP%2B6cXy7k1%2BwQYuRPaohTl4rjokr3cz%2BdrvGVKPEZgMYEEPcasX0evvOqDQB36NGfuI5GW4IowHddcu&X-Amz-Signature=92b194b0f698b985bbbe566dee5889347959e2419c5a6d9ec6926158696caca8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643HAZAYA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHehnaHavpBatjPy9qFr1aqIR4mDaDjdDNcn1uaeE95AiEAt1iHGBvqgQGQ1P5q6hMP0%2Ft%2FUK%2BwCssyk7%2BJX2XnqmUqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjamEIQ5Jw7nBmV7yrcA7RUqtKtw9Hckt8KJHebKHqkVHrks3sv4bOKjXzStEP9ybpUbb3pj4rjnNkBwOf2fmiIBxWzj%2FWGFGJ9f9DJb%2F3EYu4Npy8h8mHox%2FUEFrRFQrivsu0VeXb5JCydUqSQwMPrepkI4vglN1GAN8RYEfq3sFRGfzgCAZTI34mY%2FvnbeDYxNjOvoQdmR43h2tl0OGnL8UOrFbaMqb%2FhaVqhJJfCiIB6v3H6yk6D9sRYoEoIZbe9WNw7%2FLDzXC%2Fx3GReGB9sufIgIXiB57TAuVFkT%2BM9qQGMhwP5QB0mMtvAKGgjV3sfzIypQRA6AX2QnzppOWs%2FFL9nI2WLNGGghV%2B33hR9nkZyqBgG1s6SpXofpwAKPHZRAvXD5A%2Bb4WIoyfKHtYX%2BMIMcLNY7qs9uSFLvmPSM2rAh9bbI8GpTMkV43iJr5CJFFE8us9dZBmCZnCsDT7RKBIXpiwMKaHkwEB0phlq13SeaKXgswPZ6y0KoA9BYSJCrKnSXIdAs5%2BR4jJr8sM7zJDLlwLoz2IARauFGFJaG0AQGuDkzR6adHORopxfDK4Ji8f4yRGEb91Lbyvf%2Bo6l8u7Dyy98VCrY4sDNazszQ9FzFO%2FyDolVYHm%2FhvZ7ImeZgQ7QeANwpPV73MJvN9bwGOqUB0NR%2BYLLY%2BFITq0B2tuOfRLYt4SWEHKKhUswn7HEoa36ZDMdoRakhacipjqbbyyxDBmKvL4Jy0ZTfw79Y3M1uIPkBevznXMAFqAej7CWWC0KBU8oXdz0jGN20iPZxJdqM9YSKDsT6c8nXBaP%2B6cXy7k1%2BwQYuRPaohTl4rjokr3cz%2BdrvGVKPEZgMYEEPcasX0evvOqDQB36NGfuI5GW4IowHddcu&X-Amz-Signature=30d4d462e3627d183bc0f5bcc799d0fed2dde04001096fb024ad45c4b9f7469e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643HAZAYA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHehnaHavpBatjPy9qFr1aqIR4mDaDjdDNcn1uaeE95AiEAt1iHGBvqgQGQ1P5q6hMP0%2Ft%2FUK%2BwCssyk7%2BJX2XnqmUqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjamEIQ5Jw7nBmV7yrcA7RUqtKtw9Hckt8KJHebKHqkVHrks3sv4bOKjXzStEP9ybpUbb3pj4rjnNkBwOf2fmiIBxWzj%2FWGFGJ9f9DJb%2F3EYu4Npy8h8mHox%2FUEFrRFQrivsu0VeXb5JCydUqSQwMPrepkI4vglN1GAN8RYEfq3sFRGfzgCAZTI34mY%2FvnbeDYxNjOvoQdmR43h2tl0OGnL8UOrFbaMqb%2FhaVqhJJfCiIB6v3H6yk6D9sRYoEoIZbe9WNw7%2FLDzXC%2Fx3GReGB9sufIgIXiB57TAuVFkT%2BM9qQGMhwP5QB0mMtvAKGgjV3sfzIypQRA6AX2QnzppOWs%2FFL9nI2WLNGGghV%2B33hR9nkZyqBgG1s6SpXofpwAKPHZRAvXD5A%2Bb4WIoyfKHtYX%2BMIMcLNY7qs9uSFLvmPSM2rAh9bbI8GpTMkV43iJr5CJFFE8us9dZBmCZnCsDT7RKBIXpiwMKaHkwEB0phlq13SeaKXgswPZ6y0KoA9BYSJCrKnSXIdAs5%2BR4jJr8sM7zJDLlwLoz2IARauFGFJaG0AQGuDkzR6adHORopxfDK4Ji8f4yRGEb91Lbyvf%2Bo6l8u7Dyy98VCrY4sDNazszQ9FzFO%2FyDolVYHm%2FhvZ7ImeZgQ7QeANwpPV73MJvN9bwGOqUB0NR%2BYLLY%2BFITq0B2tuOfRLYt4SWEHKKhUswn7HEoa36ZDMdoRakhacipjqbbyyxDBmKvL4Jy0ZTfw79Y3M1uIPkBevznXMAFqAej7CWWC0KBU8oXdz0jGN20iPZxJdqM9YSKDsT6c8nXBaP%2B6cXy7k1%2BwQYuRPaohTl4rjokr3cz%2BdrvGVKPEZgMYEEPcasX0evvOqDQB36NGfuI5GW4IowHddcu&X-Amz-Signature=b9b9205114b0cb2ae822c09c73d3c998f78c0bdd18c91546b66994743ba7c9e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643HAZAYA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHehnaHavpBatjPy9qFr1aqIR4mDaDjdDNcn1uaeE95AiEAt1iHGBvqgQGQ1P5q6hMP0%2Ft%2FUK%2BwCssyk7%2BJX2XnqmUqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjamEIQ5Jw7nBmV7yrcA7RUqtKtw9Hckt8KJHebKHqkVHrks3sv4bOKjXzStEP9ybpUbb3pj4rjnNkBwOf2fmiIBxWzj%2FWGFGJ9f9DJb%2F3EYu4Npy8h8mHox%2FUEFrRFQrivsu0VeXb5JCydUqSQwMPrepkI4vglN1GAN8RYEfq3sFRGfzgCAZTI34mY%2FvnbeDYxNjOvoQdmR43h2tl0OGnL8UOrFbaMqb%2FhaVqhJJfCiIB6v3H6yk6D9sRYoEoIZbe9WNw7%2FLDzXC%2Fx3GReGB9sufIgIXiB57TAuVFkT%2BM9qQGMhwP5QB0mMtvAKGgjV3sfzIypQRA6AX2QnzppOWs%2FFL9nI2WLNGGghV%2B33hR9nkZyqBgG1s6SpXofpwAKPHZRAvXD5A%2Bb4WIoyfKHtYX%2BMIMcLNY7qs9uSFLvmPSM2rAh9bbI8GpTMkV43iJr5CJFFE8us9dZBmCZnCsDT7RKBIXpiwMKaHkwEB0phlq13SeaKXgswPZ6y0KoA9BYSJCrKnSXIdAs5%2BR4jJr8sM7zJDLlwLoz2IARauFGFJaG0AQGuDkzR6adHORopxfDK4Ji8f4yRGEb91Lbyvf%2Bo6l8u7Dyy98VCrY4sDNazszQ9FzFO%2FyDolVYHm%2FhvZ7ImeZgQ7QeANwpPV73MJvN9bwGOqUB0NR%2BYLLY%2BFITq0B2tuOfRLYt4SWEHKKhUswn7HEoa36ZDMdoRakhacipjqbbyyxDBmKvL4Jy0ZTfw79Y3M1uIPkBevznXMAFqAej7CWWC0KBU8oXdz0jGN20iPZxJdqM9YSKDsT6c8nXBaP%2B6cXy7k1%2BwQYuRPaohTl4rjokr3cz%2BdrvGVKPEZgMYEEPcasX0evvOqDQB36NGfuI5GW4IowHddcu&X-Amz-Signature=8e7bbe4073c687054d243cf29abeeeae9745be2746496471c4583a1776fb41de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643HAZAYA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHehnaHavpBatjPy9qFr1aqIR4mDaDjdDNcn1uaeE95AiEAt1iHGBvqgQGQ1P5q6hMP0%2Ft%2FUK%2BwCssyk7%2BJX2XnqmUqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjamEIQ5Jw7nBmV7yrcA7RUqtKtw9Hckt8KJHebKHqkVHrks3sv4bOKjXzStEP9ybpUbb3pj4rjnNkBwOf2fmiIBxWzj%2FWGFGJ9f9DJb%2F3EYu4Npy8h8mHox%2FUEFrRFQrivsu0VeXb5JCydUqSQwMPrepkI4vglN1GAN8RYEfq3sFRGfzgCAZTI34mY%2FvnbeDYxNjOvoQdmR43h2tl0OGnL8UOrFbaMqb%2FhaVqhJJfCiIB6v3H6yk6D9sRYoEoIZbe9WNw7%2FLDzXC%2Fx3GReGB9sufIgIXiB57TAuVFkT%2BM9qQGMhwP5QB0mMtvAKGgjV3sfzIypQRA6AX2QnzppOWs%2FFL9nI2WLNGGghV%2B33hR9nkZyqBgG1s6SpXofpwAKPHZRAvXD5A%2Bb4WIoyfKHtYX%2BMIMcLNY7qs9uSFLvmPSM2rAh9bbI8GpTMkV43iJr5CJFFE8us9dZBmCZnCsDT7RKBIXpiwMKaHkwEB0phlq13SeaKXgswPZ6y0KoA9BYSJCrKnSXIdAs5%2BR4jJr8sM7zJDLlwLoz2IARauFGFJaG0AQGuDkzR6adHORopxfDK4Ji8f4yRGEb91Lbyvf%2Bo6l8u7Dyy98VCrY4sDNazszQ9FzFO%2FyDolVYHm%2FhvZ7ImeZgQ7QeANwpPV73MJvN9bwGOqUB0NR%2BYLLY%2BFITq0B2tuOfRLYt4SWEHKKhUswn7HEoa36ZDMdoRakhacipjqbbyyxDBmKvL4Jy0ZTfw79Y3M1uIPkBevznXMAFqAej7CWWC0KBU8oXdz0jGN20iPZxJdqM9YSKDsT6c8nXBaP%2B6cXy7k1%2BwQYuRPaohTl4rjokr3cz%2BdrvGVKPEZgMYEEPcasX0evvOqDQB36NGfuI5GW4IowHddcu&X-Amz-Signature=c95607d69320a66645f2c389af595b671fc5f444e45a77734a580dc282d88104&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643HAZAYA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHehnaHavpBatjPy9qFr1aqIR4mDaDjdDNcn1uaeE95AiEAt1iHGBvqgQGQ1P5q6hMP0%2Ft%2FUK%2BwCssyk7%2BJX2XnqmUqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjamEIQ5Jw7nBmV7yrcA7RUqtKtw9Hckt8KJHebKHqkVHrks3sv4bOKjXzStEP9ybpUbb3pj4rjnNkBwOf2fmiIBxWzj%2FWGFGJ9f9DJb%2F3EYu4Npy8h8mHox%2FUEFrRFQrivsu0VeXb5JCydUqSQwMPrepkI4vglN1GAN8RYEfq3sFRGfzgCAZTI34mY%2FvnbeDYxNjOvoQdmR43h2tl0OGnL8UOrFbaMqb%2FhaVqhJJfCiIB6v3H6yk6D9sRYoEoIZbe9WNw7%2FLDzXC%2Fx3GReGB9sufIgIXiB57TAuVFkT%2BM9qQGMhwP5QB0mMtvAKGgjV3sfzIypQRA6AX2QnzppOWs%2FFL9nI2WLNGGghV%2B33hR9nkZyqBgG1s6SpXofpwAKPHZRAvXD5A%2Bb4WIoyfKHtYX%2BMIMcLNY7qs9uSFLvmPSM2rAh9bbI8GpTMkV43iJr5CJFFE8us9dZBmCZnCsDT7RKBIXpiwMKaHkwEB0phlq13SeaKXgswPZ6y0KoA9BYSJCrKnSXIdAs5%2BR4jJr8sM7zJDLlwLoz2IARauFGFJaG0AQGuDkzR6adHORopxfDK4Ji8f4yRGEb91Lbyvf%2Bo6l8u7Dyy98VCrY4sDNazszQ9FzFO%2FyDolVYHm%2FhvZ7ImeZgQ7QeANwpPV73MJvN9bwGOqUB0NR%2BYLLY%2BFITq0B2tuOfRLYt4SWEHKKhUswn7HEoa36ZDMdoRakhacipjqbbyyxDBmKvL4Jy0ZTfw79Y3M1uIPkBevznXMAFqAej7CWWC0KBU8oXdz0jGN20iPZxJdqM9YSKDsT6c8nXBaP%2B6cXy7k1%2BwQYuRPaohTl4rjokr3cz%2BdrvGVKPEZgMYEEPcasX0evvOqDQB36NGfuI5GW4IowHddcu&X-Amz-Signature=3a17af5f9f34e79283d79dfc6e83a10fe47918590ff5f1f691ed30aef8253611&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6LFOFI2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBS2vO5QIcJlC8ogh05mdmqs%2FR2yAarkS1M6vN5HNcFEAiBf7WwidjR4xHdhGtSsViHxEjAduk9%2BIHo8Nj0%2BLOq6mCqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLlG0Ggt%2B4kG7QRx0KtwDWvQkUClQSylPzzmySaDPT961gplDxyX5st5DMKK8jqJGA%2B6a1C%2BtLj103XD9sGK%2Bv8EP6zRbBV6qy4di%2BRMa4ueQ59Zisvprhwh6%2BtbUnfiLXqU522lcx4n2nvCTUOMOBdAncIhVGlsunbvJn3oVub9wdrMN5VSSovUDh%2FevGSTFJJzQeYiI44BrLpBQjLYN6k0%2BFv8naPjMsGeu3JoiP%2Ffxu2v4x102keQMF%2BM1lXEncxGxIXcyaXtPvaPDz4m82a8of6EIiJ%2Bc%2B5MAgPb0S2v4H28yuif0fR%2Fa0A%2F5%2ByKvv7hm5OAQCdWrekKeAdh8uazxrlyZaCVFhDCp9ThhZ8vb%2BpTkBNdrQzktXfvIZ%2FMLp6Hr9OlMes5EX25e%2BWVvNnmh22rbwlv%2B25OOacNW%2B0jS6DTE5slMm3I9DjrxDH5ppcft1ANZE7wTnTZIdUpxIDDA2LlrNAj0zyWzQAWmpKhRNA1QNSM%2FR0ZHZBmA4oIQtTfFoY9iraTDkGlwyAbdUsxlZ2xZum7bNdPwmK%2BqfrDbs0%2Fb9dUlB%2FSQAmKlZPtVEpeOpw0wljWCJVRwKdm5KwmB1he%2BqO%2Bro59S1z1TbKDUqP1WYpSPk91uz3zafl%2FGC%2Fw3b6E0XuaiI2kwi831vAY6pgHY3mybzYZjxOr%2BeUQ89NE5uH%2FQF5k%2BZdF1Phkqi3BqGnmrzFI%2BwAnoESIaT6ZyQvFYMw%2B%2BWpGQhPYBcBhKOULQsofvYK2q9XIB6CNEO1a4Dkv3Xj%2BkIsFjTjZ9Pw%2B1%2BjOiSfI822i2vZVWxsGIBnzolECAZ9%2BW3QKzwWyA2ho2uIWeW840akrOxiP6nlLe2fqjceRLT1XjsvTXW7nFqFvm%2BrV2%2FO7z&X-Amz-Signature=75d97fc3817b9ba3dcfc55e4812a9bf047bb6211365a7f75d04fa29b48feae47&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL233XGK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3KP8C2vY1xVxThLS3tB0XYdK0h2YfYnEbpcQMEISLfQIhAIoWoJdzpagVJPtvpT6efUt2IeehXojJzcx7q6Km7eXqKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzhMDO4FfPEGLssojoq3APS%2BsiDfQYDkJaKl0Z8zK72NoFvbRmBdIZQwvtZ%2FfjnVra%2FvSovhEFpYSoxz%2FV316HzIa8PZG%2B2P%2Fy%2FrPR99tdgk8XyedYZyJFOTSRykEG7INaH7BsQFqroZQgAhFg2l2oo99Ux3zHFM7M7SmSWzCUS93ng%2Fl%2FpUz%2BOpkKqFjbZoTbvg4yuqzKOgVu%2FfFz8incYCbMkbP57OoLJbt1glkUPQZa7n6%2FCJQmFd6HS5xpHCxZGFtcUOjJGKyuSqIEnYdDKM76AeonevXPryfxAmSAHGv9XAFbqSfCR7c0YN5dPR6NfYMPULJKolTs6gtZlpKWmo1KpxzqmszGCCMH%2BVFm4M9HttoiyfHekVMpNRrcg0JzOUvSNage6hyer054CzrneMlshtsVpqBHmV9G6HbnHWMMyanOeO2CCEDLenPomPtW59NdrJY8HR%2BVYZr6tCXXJRHpJsf2i9SJDxkA%2BNf6fIZQ%2F7ka5GquPJ3SKgUT1SLj0cvwqfyF3KQLrTuziWVWSOe4N6pDb5qJeDSS8DYkWXjUJug9cYPBQdpsgvSC3DdCeYHYhHN%2BL7l9gbnB5SlVw4QPdWp7ntwKWxHLAx3VPmqd%2F8XmDgCM8nHmReo2Xov%2BpT5cR8%2FjUmnK93DCbzfW8BjqkARhzMjNF2%2BRC3gMb8HZQM%2BAV3L8Q5El4VvjQnyq6R5pjGt0RiZgNHNCFFmJjZZmOnbwGVSQ3WXKU%2BExk39s640dWONBoY%2F5ItocIA89vWSX1uriPmszTy%2FQZ6h0cpW2YnbZgX6UsYHLBXw4zu649KhikqcsEe590sRbbmpBUazVdn245%2Bab3Pt3oN4HcXwuNF1MVKdOl5IjQH%2FZR76lHqxjrUrGw&X-Amz-Signature=71b974628a6011ca53e9da960d51147b2279f3dea93f187ba2b1a231fb7e9e4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643HAZAYA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHehnaHavpBatjPy9qFr1aqIR4mDaDjdDNcn1uaeE95AiEAt1iHGBvqgQGQ1P5q6hMP0%2Ft%2FUK%2BwCssyk7%2BJX2XnqmUqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjamEIQ5Jw7nBmV7yrcA7RUqtKtw9Hckt8KJHebKHqkVHrks3sv4bOKjXzStEP9ybpUbb3pj4rjnNkBwOf2fmiIBxWzj%2FWGFGJ9f9DJb%2F3EYu4Npy8h8mHox%2FUEFrRFQrivsu0VeXb5JCydUqSQwMPrepkI4vglN1GAN8RYEfq3sFRGfzgCAZTI34mY%2FvnbeDYxNjOvoQdmR43h2tl0OGnL8UOrFbaMqb%2FhaVqhJJfCiIB6v3H6yk6D9sRYoEoIZbe9WNw7%2FLDzXC%2Fx3GReGB9sufIgIXiB57TAuVFkT%2BM9qQGMhwP5QB0mMtvAKGgjV3sfzIypQRA6AX2QnzppOWs%2FFL9nI2WLNGGghV%2B33hR9nkZyqBgG1s6SpXofpwAKPHZRAvXD5A%2Bb4WIoyfKHtYX%2BMIMcLNY7qs9uSFLvmPSM2rAh9bbI8GpTMkV43iJr5CJFFE8us9dZBmCZnCsDT7RKBIXpiwMKaHkwEB0phlq13SeaKXgswPZ6y0KoA9BYSJCrKnSXIdAs5%2BR4jJr8sM7zJDLlwLoz2IARauFGFJaG0AQGuDkzR6adHORopxfDK4Ji8f4yRGEb91Lbyvf%2Bo6l8u7Dyy98VCrY4sDNazszQ9FzFO%2FyDolVYHm%2FhvZ7ImeZgQ7QeANwpPV73MJvN9bwGOqUB0NR%2BYLLY%2BFITq0B2tuOfRLYt4SWEHKKhUswn7HEoa36ZDMdoRakhacipjqbbyyxDBmKvL4Jy0ZTfw79Y3M1uIPkBevznXMAFqAej7CWWC0KBU8oXdz0jGN20iPZxJdqM9YSKDsT6c8nXBaP%2B6cXy7k1%2BwQYuRPaohTl4rjokr3cz%2BdrvGVKPEZgMYEEPcasX0evvOqDQB36NGfuI5GW4IowHddcu&X-Amz-Signature=33614e766fb1b00a95a5f19b1fd7e0d4057d8bcbc4fd5d6336746591139c5bd3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643HAZAYA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHehnaHavpBatjPy9qFr1aqIR4mDaDjdDNcn1uaeE95AiEAt1iHGBvqgQGQ1P5q6hMP0%2Ft%2FUK%2BwCssyk7%2BJX2XnqmUqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjamEIQ5Jw7nBmV7yrcA7RUqtKtw9Hckt8KJHebKHqkVHrks3sv4bOKjXzStEP9ybpUbb3pj4rjnNkBwOf2fmiIBxWzj%2FWGFGJ9f9DJb%2F3EYu4Npy8h8mHox%2FUEFrRFQrivsu0VeXb5JCydUqSQwMPrepkI4vglN1GAN8RYEfq3sFRGfzgCAZTI34mY%2FvnbeDYxNjOvoQdmR43h2tl0OGnL8UOrFbaMqb%2FhaVqhJJfCiIB6v3H6yk6D9sRYoEoIZbe9WNw7%2FLDzXC%2Fx3GReGB9sufIgIXiB57TAuVFkT%2BM9qQGMhwP5QB0mMtvAKGgjV3sfzIypQRA6AX2QnzppOWs%2FFL9nI2WLNGGghV%2B33hR9nkZyqBgG1s6SpXofpwAKPHZRAvXD5A%2Bb4WIoyfKHtYX%2BMIMcLNY7qs9uSFLvmPSM2rAh9bbI8GpTMkV43iJr5CJFFE8us9dZBmCZnCsDT7RKBIXpiwMKaHkwEB0phlq13SeaKXgswPZ6y0KoA9BYSJCrKnSXIdAs5%2BR4jJr8sM7zJDLlwLoz2IARauFGFJaG0AQGuDkzR6adHORopxfDK4Ji8f4yRGEb91Lbyvf%2Bo6l8u7Dyy98VCrY4sDNazszQ9FzFO%2FyDolVYHm%2FhvZ7ImeZgQ7QeANwpPV73MJvN9bwGOqUB0NR%2BYLLY%2BFITq0B2tuOfRLYt4SWEHKKhUswn7HEoa36ZDMdoRakhacipjqbbyyxDBmKvL4Jy0ZTfw79Y3M1uIPkBevznXMAFqAej7CWWC0KBU8oXdz0jGN20iPZxJdqM9YSKDsT6c8nXBaP%2B6cXy7k1%2BwQYuRPaohTl4rjokr3cz%2BdrvGVKPEZgMYEEPcasX0evvOqDQB36NGfuI5GW4IowHddcu&X-Amz-Signature=5c030b78e4b1c67d13a1e266c9902d7b40249826c73e2ed714d0d94c43b9bf03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643HAZAYA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHehnaHavpBatjPy9qFr1aqIR4mDaDjdDNcn1uaeE95AiEAt1iHGBvqgQGQ1P5q6hMP0%2Ft%2FUK%2BwCssyk7%2BJX2XnqmUqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjamEIQ5Jw7nBmV7yrcA7RUqtKtw9Hckt8KJHebKHqkVHrks3sv4bOKjXzStEP9ybpUbb3pj4rjnNkBwOf2fmiIBxWzj%2FWGFGJ9f9DJb%2F3EYu4Npy8h8mHox%2FUEFrRFQrivsu0VeXb5JCydUqSQwMPrepkI4vglN1GAN8RYEfq3sFRGfzgCAZTI34mY%2FvnbeDYxNjOvoQdmR43h2tl0OGnL8UOrFbaMqb%2FhaVqhJJfCiIB6v3H6yk6D9sRYoEoIZbe9WNw7%2FLDzXC%2Fx3GReGB9sufIgIXiB57TAuVFkT%2BM9qQGMhwP5QB0mMtvAKGgjV3sfzIypQRA6AX2QnzppOWs%2FFL9nI2WLNGGghV%2B33hR9nkZyqBgG1s6SpXofpwAKPHZRAvXD5A%2Bb4WIoyfKHtYX%2BMIMcLNY7qs9uSFLvmPSM2rAh9bbI8GpTMkV43iJr5CJFFE8us9dZBmCZnCsDT7RKBIXpiwMKaHkwEB0phlq13SeaKXgswPZ6y0KoA9BYSJCrKnSXIdAs5%2BR4jJr8sM7zJDLlwLoz2IARauFGFJaG0AQGuDkzR6adHORopxfDK4Ji8f4yRGEb91Lbyvf%2Bo6l8u7Dyy98VCrY4sDNazszQ9FzFO%2FyDolVYHm%2FhvZ7ImeZgQ7QeANwpPV73MJvN9bwGOqUB0NR%2BYLLY%2BFITq0B2tuOfRLYt4SWEHKKhUswn7HEoa36ZDMdoRakhacipjqbbyyxDBmKvL4Jy0ZTfw79Y3M1uIPkBevznXMAFqAej7CWWC0KBU8oXdz0jGN20iPZxJdqM9YSKDsT6c8nXBaP%2B6cXy7k1%2BwQYuRPaohTl4rjokr3cz%2BdrvGVKPEZgMYEEPcasX0evvOqDQB36NGfuI5GW4IowHddcu&X-Amz-Signature=fe94cebf044829072dd2c5922e5b258045e324d607355343e1ef42d4cdc6bf8a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWKPYINK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEQJBSj7BnDyUQe5vzzTfswNmLg7h4%2FOF0bJpBtK3OIgIgBIgS1PQGn7ATVJ5SzFWVtlJAQZF658wAjbMELGQ%2BvSQqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC4lnrZx6hLK3aq18ircA6U0ypmYCBaJHGnaholcGgG%2BgPY5Ie3KVnOy5kZOk880IkuYB%2Bkp53ILWUVqAEqcTp4mYWClbIUEk9jTSr78UthO256yNJiTSUca8ndbAwPIvyi34eLcg5Mc8%2FjWvp23x75s88xeobdjT5EENGTHvz56mppUWsQqVufUaGeXUT0Y1QJ4dX7lD5LJOCvT%2BeX%2FuD5Ioka%2Brf2fJP1KC9vuyWajAokTwR3gEyQYc4YPQSCykWl7IcHxuasOuY9eYUMTL98zniSOBeJgf7xQbmRCoS%2B%2Fj7M7dI2gyPRNZXIouwfu0qmuLOjPJLadtZVhOmHzdUleWDaCQif6O%2FsN%2BKD2GgxcvlGn4WML3tv8hpjTyoxpuxOxrxOwLT3lF%2FnyAvEViAwUFBAnn109dEOcBfbboghZVfG6HwI4mOYOniQBFNNAsHlWM2hrpb4NVpdGYtnNQGvnHWhsNkgDyTU%2FUHty99zH%2BmdXjkMNOlUj1EU8iEUhLD%2Ft0uZtB%2B5yrjP8E4dzkCizLSb%2Fwc17%2BifGU%2F14mBskS02IVeUZHC5L2%2F5lXXcm61q%2F1pwN%2FGrR6mY%2Bpan0gcZo6x7bq%2BmNx3%2FYA8EKqzzjAhPD%2FcLHZ%2BG0bL08BmLdQGY21ygRaAhUiGomMJzN9bwGOqUB1l%2BbpYxuK7ab154LVf4603BuifQWtcj5I9j3PqPPoEkBOxH30DqRUm0k8zJjw5lBOgo1sfPOiPX%2Bw2tGR9jNIb05D%2FQZiR35GzVHsnbsdycWN0EstjwddrfZnzcPnq%2BCS4gIVCw4GkA3i6vL2VBRd6HfvRDsScUf7F8PR8%2F6c73A1yvH1Z1WAg%2FK%2FAYyALpkBbrybDWc2OrT9D%2FQyw8WKIzxYKHB&X-Amz-Signature=1b621a86ad247c21ff480c78aaab3a89e76b5a7848e960eeb114ba3b085c169a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCXRN5V%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF2CP3XveIVrUm%2FIrz70pl9hEwPtBtP8qiVzYS0dgysiAiEA%2FZqoFSXUeYat2ULGKTaPRMqhcQOFlqgjmY%2B7vhFkI5YqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNOJUNmjDRynm9CKaircA6Mi4nxPSFwcO012oc4ZjF%2BWe3myNO8RI5WVX0DjpJ34TEV2sQ4z0t4QE%2F5kDfNKTuP%2Bm28RzuCz1JrPIl4QE%2FBMbKYM38Dlfqw52xrpo37PM5vAQxWK4XvtqngGgTruffTAirj5FfNtPcleAUYcaGwQQk3eD%2FPAyIVEJ29iQiYfqtpEJXd9ujgDMnW8zhctgYrSiLe2qqMN%2F4ef2RT3F8ivBf4fw755AFyIxuS9FYs2d4FqxxAsjdaxbSbd8TcZlDUSgouVRbqQgHgjL7LDivu7%2F6BLLsGsKwMKWmJJUZpUhMquttRlzTkNroIHCHDxr%2F776maCaz9fC7bFnB3H9mkEW%2FtXFcmJnfvKU%2B0%2BNnbvqek3gaSrQSY18%2BtBB3gxo8OYl1R4jhh1YgSx%2Bo58TaEUDigYSRy2cb9Nehxgj8%2BKE6vrw2LuTIb%2FkwITAXtY7fiNBmxYlxMGz6Oy1f99YUYBcXc%2Ff0V5BcyJXfcMn3T6w8rvM6128ttVdxho1Ap7V8PDIaDC68jtbUGQvRT8XoavZ4j%2Fe3CclMXR9w8kIWT8mAKzAkZFBDQdGHtbQzmckm3uF8uhujdVvrv2RJyUMxldA9a6Gxd0mLwpMw3BcmoiePJowKnCaUigc9OdMJ7N9bwGOqUBbiBVYptAksZlVwWseadSZznjgOMyNY7q65AyHycphqk69R%2F2XgJ9sR%2B5R9jlPF27RIIegV2yW9gYjw4glsDVrvALxfhaLpp4lPYzZnQMgS%2Bv7ulHF2vBNvRxMDAIO%2F7km9Mhfy6jrKN45%2FCWbR5LHZyGItG0AP806rvaERH1Nh2vklNAryCvuXHs6TBkkjnjN15KMYQvvwQxGjtqGUVJYkufzFJK&X-Amz-Signature=14465fccafd606b5cf2ac7c22125a07e8f8d306d8c3a740da9f430378691dec0&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMD47DE2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfUUUIjLH6jkSG0Pi8xi%2F5tcmemOyY3PoNhH3ENtucuAIhAOKHIB8lmNFMJ0YLczNKaztkK2wqkolsqaItWFCrJD8CKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyW%2FIDdfar2zSOjroYq3APE6UCaLfwpQVkDc3rBH8E2stiYJwVHaruPlE55YIiV8%2BLnpN03a0ABp6%2BzPXNw0WSgPxMojd3uHS%2BmSFWmGiHQYT0l%2B5wdUyP8VPZZyceLVgioI1LhI6iDcFt3VVahkFE0Fcdix%2FZqYTkOD4qE98QVzZwv0Sk1PTpbTorWJrlvjmCYxbnMAlLZSJl5yL83p0XiKhUfkfFTtD7GkI6ZZ6q31gQsD2LJgj13fXTx2R%2B8VoW8vkvHFYq0amtm9lWE4Xi9Ss6CPkFOu1NvivfhKXPoogkPaWu5fY2aXnjATH2FzCZzrXa4B4WVmQDV0Dl%2FglfQ87vNdz6EqkoGGJtLm9t7bz2U6oCiHuCF%2BtHeywdTM%2B6HtVP2q3IjhoI7WyXC%2BGt2GMQW8IAn0meNq9dc4slUdMoCSOFCIxTJ6rq69LWkhTdxy2p2C7RvTTzf4hB8G6QWfUnzucXyMPwIFRr0qUbRKtLpqYgG4CqYw0FxeRlvM%2FmRzrWT%2Fqk4DpQnb0mmEXEm6GaG4PVXwes1KWzCrXS4%2Fapgm%2FfxHElKCkpkXV2QtYyrohw%2FHizTRyJnq2ZqGs%2FbzwI%2FrexbIeURb7ZSwvJ5LBfUHWJlKO4awYZ%2FacP8UDcSZ6Gb0uk2jALdYTDvzPW8BjqkARPuUs0V6B07Svj2fJ%2FHGNc6HCwDMAkePGo3n7eq874CU4BUaU%2FDQn%2BkkLqahqM09DXrsLsgDr1WHDGT%2BGVZGwaDaHUzEQlV4ouqdZJG%2FXzxiLFDerTJbm1iuymRGF%2BTyixihJXKDf7Dfz%2BdRoezcs4Szg8a3R%2B4VF0%2FKPcMpNnG10yocK3C8L1G0HHJdGYIDY8LiCU0gWucD%2B7R4w19ENgdqHUn&X-Amz-Signature=14797c491883785775b3b34e4ac9c0c8470890fc2b9fb9dc0d313693f495fcfc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRGCOD4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdkIuanKTcBAVf4OAOKyyWs90HMa%2FAypSjHZGezcHl0wIhAPIebmMDXiKiel%2BYJ0F%2BnQd4VOFOEJGn8xLvSsVrA7bOKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw7K3xekg4lsg15COAq3ANXmaBhJwsj7S9DngcHvAE4S2fozdI43mlzc%2BFILbpoMWIBUgJ2HOvUL3iE2RuEa%2BCAaT9qDDt2J6lwbFj2sxMNDsj%2FbumRXjtBC14e2Mv6K29YJ1y0IYJgxAO7uBeUlXNGuqrJJU5O0jW4cDGzoUlRToALMN9Uz1Zi5P9vnRY4gkSnB5gweFfMW%2FSa%2Fi3fRdzoqPAHlcYJg6Q2O4bgbDQCWPMtWJrTSMdiWT9hZmfXs3qoF3EpAkX5qXZJToOKyscx%2F2VU1bfiEnhDjKDm6P52b4T45w1kCkcBMMtNmPPF7IJkLoBbAZTbqYTdYSgZG07N3VmFP%2F1P0O6r4MTluf1kWXM9hLSqM56RVHqMlUsVMWyGV7fdlNLI7zNI3pZFV6xEI5NmebX88lu1q8JGvwC17wyejpyjf6V3%2Flu2ey%2BbH96hZEUsoTR7PozDIYvHwun7Z5fDe5G4I7akwoQ3mTDNTrRiFCLwbd242XHtGL56QxP2Y%2BdMIu5BOqhhVpSfajnXL%2F%2FTDlz9kJ8NSN0%2B%2FVQM0K7fYHlWmrYP%2FL5NXsa7V%2F%2FkN8u9XPiBXnKrJ7%2BUZ7zn8CtRDgzAbEeBHioNEgw5qFhvVMXwDVMg%2BPICLbguYKzKpXv7HmKubW5PNzCZzfW8BjqkAVp0SSdsiC9QEI6bg9UuUfFVbhngAzQX3RXB7t5VrYnrWaIPDmKcVahjT0SkB7qGiGJPPLqgvDkgI7AS08vhc6Ij8sRFGr8bto4H4nMrfnKC8b%2BmPgm%2FpPBoLyVoXhAPLdhxFbaQLUJTjHEgMMLTGWQ9pjLwaimLTkGJVZ4iwgyW1gG5Z73rGqVgVsOPrZyZ%2FpSxDpZ8a8j9gj1sj6zSF1YYfEyb&X-Amz-Signature=aa09e77549b7b6c2b9d38f9cd2a4631dfcc01a58fff5bffcb6e8f8694d28d025&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRGCOD4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdkIuanKTcBAVf4OAOKyyWs90HMa%2FAypSjHZGezcHl0wIhAPIebmMDXiKiel%2BYJ0F%2BnQd4VOFOEJGn8xLvSsVrA7bOKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw7K3xekg4lsg15COAq3ANXmaBhJwsj7S9DngcHvAE4S2fozdI43mlzc%2BFILbpoMWIBUgJ2HOvUL3iE2RuEa%2BCAaT9qDDt2J6lwbFj2sxMNDsj%2FbumRXjtBC14e2Mv6K29YJ1y0IYJgxAO7uBeUlXNGuqrJJU5O0jW4cDGzoUlRToALMN9Uz1Zi5P9vnRY4gkSnB5gweFfMW%2FSa%2Fi3fRdzoqPAHlcYJg6Q2O4bgbDQCWPMtWJrTSMdiWT9hZmfXs3qoF3EpAkX5qXZJToOKyscx%2F2VU1bfiEnhDjKDm6P52b4T45w1kCkcBMMtNmPPF7IJkLoBbAZTbqYTdYSgZG07N3VmFP%2F1P0O6r4MTluf1kWXM9hLSqM56RVHqMlUsVMWyGV7fdlNLI7zNI3pZFV6xEI5NmebX88lu1q8JGvwC17wyejpyjf6V3%2Flu2ey%2BbH96hZEUsoTR7PozDIYvHwun7Z5fDe5G4I7akwoQ3mTDNTrRiFCLwbd242XHtGL56QxP2Y%2BdMIu5BOqhhVpSfajnXL%2F%2FTDlz9kJ8NSN0%2B%2FVQM0K7fYHlWmrYP%2FL5NXsa7V%2F%2FkN8u9XPiBXnKrJ7%2BUZ7zn8CtRDgzAbEeBHioNEgw5qFhvVMXwDVMg%2BPICLbguYKzKpXv7HmKubW5PNzCZzfW8BjqkAVp0SSdsiC9QEI6bg9UuUfFVbhngAzQX3RXB7t5VrYnrWaIPDmKcVahjT0SkB7qGiGJPPLqgvDkgI7AS08vhc6Ij8sRFGr8bto4H4nMrfnKC8b%2BmPgm%2FpPBoLyVoXhAPLdhxFbaQLUJTjHEgMMLTGWQ9pjLwaimLTkGJVZ4iwgyW1gG5Z73rGqVgVsOPrZyZ%2FpSxDpZ8a8j9gj1sj6zSF1YYfEyb&X-Amz-Signature=67089574b555d6c8ef41748597a4da4b201d1f9e5799bf03237b9c9ac63f7a63&X-Amz-SignedHeaders=host&x-id=GetObject)

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
