

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=66a541d25930c81afad9f4251122f347a2bf4268bc72ff40d1ba955f3dd1c114&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=a17f6cc7171fc1b6c7c8c3d698ca353272ae668b3d5703600bd9698ac94b54a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R22TVBBP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCID7s5UwK04hCHX%2FtCCO4SKt%2BKlJ08VMgoyIp8u3lni5gAiEAw6RWGdHmliXRRFXKrSkDyixumSWLZ39WzJVjkGZcWiUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFZX3Xe2bK%2FV5zhX1yrcA8RDWWrV40DLKk%2BTlsw6W2tW7M7%2BQPNSSAc3j6qCuRsP6snbW6z9rx%2BSGntDyLTq1Q%2BqOFIqiXlXn6lrY6uV7f6SOsVgf7M1EK5QzVctOxmrBN6Qu6dB1nw0wq7MnlIOe%2BIeqSmW2KNklE9q0EwbiUQ7uN04zUfD1kx2QdnFrZahRuw9rJjeGmUA6MR%2Ba2reS7C2B2APAF5s%2FAtvkR1RJCdhJeYNLGic9qR7wtFKwhFv96QszgxY4f4eId3oW9CK%2Fn1bcuA0DDeH8Sybqh66U3qhX6Gol%2BaK7lvVpwtHGlQ6oL4YWhm6jRaXvKyckac1NeBhmceJI1QSvUXoha15Hx173rxKCvzc85rkVSO%2FyD2Ocp2U61UP22X7Z%2FdNJ8yyt69viTocvh0cxEEbuJ%2F0LkcAwxCn6yYSLd7pp7yb75qdxM9Azzyr4hht5KlHmXMfhGC%2FK9OrsqKQrlF62BpiN3CXompPc6gmYkVJHwEVb11dOeYeGYoKiFjjDhCrZQb8gkyYGwyNszyv7LuI4kmtnPpwCfsUQBe%2B1WiQ39%2BAYZDuWLT77y3wSGtJRv1Nd0ozY8CFahl50OIi5FfVm%2FVXPu%2BwDs8NoY1KOzlXtp1NeSWpVT5B37EVXy4j0U8uMJ%2Fskb0GOqUBSIpj9C203FfXYKB7mFBN5d4Cm14F0UWypTsG%2BoisRL6FWHaNMmgck%2BCRBFNaKVngUnvaRjTDnaQ0rWLeP1KZtNfuANdmF0MUs8lTYotR4F8lNJY9ZeBLH%2BizHZh1ussOz8mdxlVbVY4%2Fu6859bIuepel%2BlRQOzmSFPIYHSX6SpJyCBXPqK432ghau1hU4UXiBU9lOI1HySeR%2BXgrdC%2Bhnf0bCMiC&X-Amz-Signature=5e45e09d7261a29c131216713ad3de07897452f260e0d5752f516e73100b0d09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7BWY3F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGIuNlTUoRatp3glpT%2F4pSSKsPBBjlbPOZD518uELC8rAiEAnrjgK7YNf39Cvxz%2BUfjYUH8PBGAjYAapDJeaVRugQlgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBp1PzpLMlWiZbV3nSrcA4JakBUmXVc4JVf4L94kJAjVP3AgVdrDwwo3gkrRHql2GdBnnLnw2Nq0FZueJ394HkwTjg6EWRTo90in7UAhXyHiV%2BG%2FEi3%2FDhoWs3EU64uTgIkQe%2BAQO5AmM4aBWtqj6Jw8dHMBBzkDGHR3Hob1HcMLSVSbyAPgNGKbpGdgLPKZ9KvzQNtYEDSA2WPX5CwkvVyv5fIGefGil1ZoXiEWtn86ZJGkdlolFjJwtpIB7mVrpqnxJ5FUgWC5vo0A%2BZY%2FmpjDQaQpxy7rCpkh5beRB9m0dfsumbMIDalC1AlWMwiYGZfUdNHnQZtBOymQG%2BqPw2G3DcXA9q9jpxihvYxLhgKWaxDXL0foWtSFo6FfiTfIH2CFANzC2o86ujqGjUsRR%2ByDPoBQjMf47t5Xa6NHPMChS7WAjPiDR%2FBn8V2fGJ4Mtu2Foj1wAS4rQQpE0PbyK8zBdIXu4y8v6H8%2BzzIzwJCNpJf56f0Dfs3d6TwQmfuMTvniRCehHKN%2BTlrR2HmI14DDXzFsPJkHBz6arykeMpufb4ojZfdzC1tgWC39iBmh98%2By9%2FAqmAlpVk6eUAbp%2BE3LDskVPmFhb5zNO0tpbuK%2FB08LpQE4aSg8kAjvm0MX%2Bl%2FWNyZDQ43rog4tMN%2Frkb0GOqUBh%2Fdb9KKTeTc2LKORk%2FXR8pDl8qStIDp5vuHw%2BzxOf0SO%2F9%2F8LqieQ5j0S2NJGQvvKDuo6EGN5pe%2BjEKv8HnEF%2FJ%2F1nYfWHIJAoNzAd1m42%2FYPXZYRdqcRX5gBx7P6Y8eTFASTwxOUNBibJ6Gc28ItptbWagEcbK9rZNBjV1MBLYOBWKM47VKQJtOlvoW5PKNarNVggYLtSALpChwxqhHHYXUGbPf&X-Amz-Signature=09b19c382e469496614fea85557ede187ffb91bad98bcfad3c08d8938e84e24a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7BWY3F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGIuNlTUoRatp3glpT%2F4pSSKsPBBjlbPOZD518uELC8rAiEAnrjgK7YNf39Cvxz%2BUfjYUH8PBGAjYAapDJeaVRugQlgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBp1PzpLMlWiZbV3nSrcA4JakBUmXVc4JVf4L94kJAjVP3AgVdrDwwo3gkrRHql2GdBnnLnw2Nq0FZueJ394HkwTjg6EWRTo90in7UAhXyHiV%2BG%2FEi3%2FDhoWs3EU64uTgIkQe%2BAQO5AmM4aBWtqj6Jw8dHMBBzkDGHR3Hob1HcMLSVSbyAPgNGKbpGdgLPKZ9KvzQNtYEDSA2WPX5CwkvVyv5fIGefGil1ZoXiEWtn86ZJGkdlolFjJwtpIB7mVrpqnxJ5FUgWC5vo0A%2BZY%2FmpjDQaQpxy7rCpkh5beRB9m0dfsumbMIDalC1AlWMwiYGZfUdNHnQZtBOymQG%2BqPw2G3DcXA9q9jpxihvYxLhgKWaxDXL0foWtSFo6FfiTfIH2CFANzC2o86ujqGjUsRR%2ByDPoBQjMf47t5Xa6NHPMChS7WAjPiDR%2FBn8V2fGJ4Mtu2Foj1wAS4rQQpE0PbyK8zBdIXu4y8v6H8%2BzzIzwJCNpJf56f0Dfs3d6TwQmfuMTvniRCehHKN%2BTlrR2HmI14DDXzFsPJkHBz6arykeMpufb4ojZfdzC1tgWC39iBmh98%2By9%2FAqmAlpVk6eUAbp%2BE3LDskVPmFhb5zNO0tpbuK%2FB08LpQE4aSg8kAjvm0MX%2Bl%2FWNyZDQ43rog4tMN%2Frkb0GOqUBh%2Fdb9KKTeTc2LKORk%2FXR8pDl8qStIDp5vuHw%2BzxOf0SO%2F9%2F8LqieQ5j0S2NJGQvvKDuo6EGN5pe%2BjEKv8HnEF%2FJ%2F1nYfWHIJAoNzAd1m42%2FYPXZYRdqcRX5gBx7P6Y8eTFASTwxOUNBibJ6Gc28ItptbWagEcbK9rZNBjV1MBLYOBWKM47VKQJtOlvoW5PKNarNVggYLtSALpChwxqhHHYXUGbPf&X-Amz-Signature=b1e4808b3feca1611d5aa27de00a96ae7354057c39fd9c14f76578a81a0ffd07&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7BWY3F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGIuNlTUoRatp3glpT%2F4pSSKsPBBjlbPOZD518uELC8rAiEAnrjgK7YNf39Cvxz%2BUfjYUH8PBGAjYAapDJeaVRugQlgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBp1PzpLMlWiZbV3nSrcA4JakBUmXVc4JVf4L94kJAjVP3AgVdrDwwo3gkrRHql2GdBnnLnw2Nq0FZueJ394HkwTjg6EWRTo90in7UAhXyHiV%2BG%2FEi3%2FDhoWs3EU64uTgIkQe%2BAQO5AmM4aBWtqj6Jw8dHMBBzkDGHR3Hob1HcMLSVSbyAPgNGKbpGdgLPKZ9KvzQNtYEDSA2WPX5CwkvVyv5fIGefGil1ZoXiEWtn86ZJGkdlolFjJwtpIB7mVrpqnxJ5FUgWC5vo0A%2BZY%2FmpjDQaQpxy7rCpkh5beRB9m0dfsumbMIDalC1AlWMwiYGZfUdNHnQZtBOymQG%2BqPw2G3DcXA9q9jpxihvYxLhgKWaxDXL0foWtSFo6FfiTfIH2CFANzC2o86ujqGjUsRR%2ByDPoBQjMf47t5Xa6NHPMChS7WAjPiDR%2FBn8V2fGJ4Mtu2Foj1wAS4rQQpE0PbyK8zBdIXu4y8v6H8%2BzzIzwJCNpJf56f0Dfs3d6TwQmfuMTvniRCehHKN%2BTlrR2HmI14DDXzFsPJkHBz6arykeMpufb4ojZfdzC1tgWC39iBmh98%2By9%2FAqmAlpVk6eUAbp%2BE3LDskVPmFhb5zNO0tpbuK%2FB08LpQE4aSg8kAjvm0MX%2Bl%2FWNyZDQ43rog4tMN%2Frkb0GOqUBh%2Fdb9KKTeTc2LKORk%2FXR8pDl8qStIDp5vuHw%2BzxOf0SO%2F9%2F8LqieQ5j0S2NJGQvvKDuo6EGN5pe%2BjEKv8HnEF%2FJ%2F1nYfWHIJAoNzAd1m42%2FYPXZYRdqcRX5gBx7P6Y8eTFASTwxOUNBibJ6Gc28ItptbWagEcbK9rZNBjV1MBLYOBWKM47VKQJtOlvoW5PKNarNVggYLtSALpChwxqhHHYXUGbPf&X-Amz-Signature=b364719b09657e072e8438c10b30a749c3ef25118383361214f855ab2f1c7720&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7BWY3F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGIuNlTUoRatp3glpT%2F4pSSKsPBBjlbPOZD518uELC8rAiEAnrjgK7YNf39Cvxz%2BUfjYUH8PBGAjYAapDJeaVRugQlgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBp1PzpLMlWiZbV3nSrcA4JakBUmXVc4JVf4L94kJAjVP3AgVdrDwwo3gkrRHql2GdBnnLnw2Nq0FZueJ394HkwTjg6EWRTo90in7UAhXyHiV%2BG%2FEi3%2FDhoWs3EU64uTgIkQe%2BAQO5AmM4aBWtqj6Jw8dHMBBzkDGHR3Hob1HcMLSVSbyAPgNGKbpGdgLPKZ9KvzQNtYEDSA2WPX5CwkvVyv5fIGefGil1ZoXiEWtn86ZJGkdlolFjJwtpIB7mVrpqnxJ5FUgWC5vo0A%2BZY%2FmpjDQaQpxy7rCpkh5beRB9m0dfsumbMIDalC1AlWMwiYGZfUdNHnQZtBOymQG%2BqPw2G3DcXA9q9jpxihvYxLhgKWaxDXL0foWtSFo6FfiTfIH2CFANzC2o86ujqGjUsRR%2ByDPoBQjMf47t5Xa6NHPMChS7WAjPiDR%2FBn8V2fGJ4Mtu2Foj1wAS4rQQpE0PbyK8zBdIXu4y8v6H8%2BzzIzwJCNpJf56f0Dfs3d6TwQmfuMTvniRCehHKN%2BTlrR2HmI14DDXzFsPJkHBz6arykeMpufb4ojZfdzC1tgWC39iBmh98%2By9%2FAqmAlpVk6eUAbp%2BE3LDskVPmFhb5zNO0tpbuK%2FB08LpQE4aSg8kAjvm0MX%2Bl%2FWNyZDQ43rog4tMN%2Frkb0GOqUBh%2Fdb9KKTeTc2LKORk%2FXR8pDl8qStIDp5vuHw%2BzxOf0SO%2F9%2F8LqieQ5j0S2NJGQvvKDuo6EGN5pe%2BjEKv8HnEF%2FJ%2F1nYfWHIJAoNzAd1m42%2FYPXZYRdqcRX5gBx7P6Y8eTFASTwxOUNBibJ6Gc28ItptbWagEcbK9rZNBjV1MBLYOBWKM47VKQJtOlvoW5PKNarNVggYLtSALpChwxqhHHYXUGbPf&X-Amz-Signature=10eb04b7cf37bc9858325a759db5282843b3df175991053a4c4a824497294f1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7BWY3F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGIuNlTUoRatp3glpT%2F4pSSKsPBBjlbPOZD518uELC8rAiEAnrjgK7YNf39Cvxz%2BUfjYUH8PBGAjYAapDJeaVRugQlgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBp1PzpLMlWiZbV3nSrcA4JakBUmXVc4JVf4L94kJAjVP3AgVdrDwwo3gkrRHql2GdBnnLnw2Nq0FZueJ394HkwTjg6EWRTo90in7UAhXyHiV%2BG%2FEi3%2FDhoWs3EU64uTgIkQe%2BAQO5AmM4aBWtqj6Jw8dHMBBzkDGHR3Hob1HcMLSVSbyAPgNGKbpGdgLPKZ9KvzQNtYEDSA2WPX5CwkvVyv5fIGefGil1ZoXiEWtn86ZJGkdlolFjJwtpIB7mVrpqnxJ5FUgWC5vo0A%2BZY%2FmpjDQaQpxy7rCpkh5beRB9m0dfsumbMIDalC1AlWMwiYGZfUdNHnQZtBOymQG%2BqPw2G3DcXA9q9jpxihvYxLhgKWaxDXL0foWtSFo6FfiTfIH2CFANzC2o86ujqGjUsRR%2ByDPoBQjMf47t5Xa6NHPMChS7WAjPiDR%2FBn8V2fGJ4Mtu2Foj1wAS4rQQpE0PbyK8zBdIXu4y8v6H8%2BzzIzwJCNpJf56f0Dfs3d6TwQmfuMTvniRCehHKN%2BTlrR2HmI14DDXzFsPJkHBz6arykeMpufb4ojZfdzC1tgWC39iBmh98%2By9%2FAqmAlpVk6eUAbp%2BE3LDskVPmFhb5zNO0tpbuK%2FB08LpQE4aSg8kAjvm0MX%2Bl%2FWNyZDQ43rog4tMN%2Frkb0GOqUBh%2Fdb9KKTeTc2LKORk%2FXR8pDl8qStIDp5vuHw%2BzxOf0SO%2F9%2F8LqieQ5j0S2NJGQvvKDuo6EGN5pe%2BjEKv8HnEF%2FJ%2F1nYfWHIJAoNzAd1m42%2FYPXZYRdqcRX5gBx7P6Y8eTFASTwxOUNBibJ6Gc28ItptbWagEcbK9rZNBjV1MBLYOBWKM47VKQJtOlvoW5PKNarNVggYLtSALpChwxqhHHYXUGbPf&X-Amz-Signature=5a923eaac1b44753440f6fde4fa3d77e836dcc82310dcf475d5e09e683102879&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7BWY3F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGIuNlTUoRatp3glpT%2F4pSSKsPBBjlbPOZD518uELC8rAiEAnrjgK7YNf39Cvxz%2BUfjYUH8PBGAjYAapDJeaVRugQlgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBp1PzpLMlWiZbV3nSrcA4JakBUmXVc4JVf4L94kJAjVP3AgVdrDwwo3gkrRHql2GdBnnLnw2Nq0FZueJ394HkwTjg6EWRTo90in7UAhXyHiV%2BG%2FEi3%2FDhoWs3EU64uTgIkQe%2BAQO5AmM4aBWtqj6Jw8dHMBBzkDGHR3Hob1HcMLSVSbyAPgNGKbpGdgLPKZ9KvzQNtYEDSA2WPX5CwkvVyv5fIGefGil1ZoXiEWtn86ZJGkdlolFjJwtpIB7mVrpqnxJ5FUgWC5vo0A%2BZY%2FmpjDQaQpxy7rCpkh5beRB9m0dfsumbMIDalC1AlWMwiYGZfUdNHnQZtBOymQG%2BqPw2G3DcXA9q9jpxihvYxLhgKWaxDXL0foWtSFo6FfiTfIH2CFANzC2o86ujqGjUsRR%2ByDPoBQjMf47t5Xa6NHPMChS7WAjPiDR%2FBn8V2fGJ4Mtu2Foj1wAS4rQQpE0PbyK8zBdIXu4y8v6H8%2BzzIzwJCNpJf56f0Dfs3d6TwQmfuMTvniRCehHKN%2BTlrR2HmI14DDXzFsPJkHBz6arykeMpufb4ojZfdzC1tgWC39iBmh98%2By9%2FAqmAlpVk6eUAbp%2BE3LDskVPmFhb5zNO0tpbuK%2FB08LpQE4aSg8kAjvm0MX%2Bl%2FWNyZDQ43rog4tMN%2Frkb0GOqUBh%2Fdb9KKTeTc2LKORk%2FXR8pDl8qStIDp5vuHw%2BzxOf0SO%2F9%2F8LqieQ5j0S2NJGQvvKDuo6EGN5pe%2BjEKv8HnEF%2FJ%2F1nYfWHIJAoNzAd1m42%2FYPXZYRdqcRX5gBx7P6Y8eTFASTwxOUNBibJ6Gc28ItptbWagEcbK9rZNBjV1MBLYOBWKM47VKQJtOlvoW5PKNarNVggYLtSALpChwxqhHHYXUGbPf&X-Amz-Signature=eda0f49d3e68e7803d926e512309bfa30abfd090732738c615f80c1825b32d1d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NV7PUXT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCID4Mk9Gsjcagbin8Cy4173f1nuFvk7JVYAa49C1lPW7%2BAiA3fueq7Kxutu6mIIrfbseLmfGuqOuHz%2B3CwpNB6PtSMSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMzsxksS4Z6Wz%2Fp%2BEBKtwDRdsFQTLMMUlaluWaqVrqIhPpWASqHmYFhGX2UtNy3ab4YLWXSXaIabOyfskOb1qofJ9CS%2BvLTvrzZ7t3ZnufNATNAyjwYhGCI58ql7uHoYw81SmSWt9p88PM79AVcGP37%2FAVmFdPOqqU0tIi0Olo5aKda0LCLzWzIgdUSAHDp3qSTxEyvyggaAjNewu0CSHMSAnLi1PHTJYpirkTp9QvqQIvO%2F1dxDTDK7AzB%2FimeF6kGUQLwaHX46akGD3ckKbvaFuknSi6kn20eOWybvnvW2slp6D4aN%2FBAkdyyz7BZrPW68Nai71W3ZRzXa64u5t3%2Fc3xdNGhss2OxSbhpx2VGm8v527IzvDcoW34stO2X9EKAPV3DuZ2tbMk6lCDIK1u1GRlmFyn7q42gedsMg9Jla9pkURAB9d0A3lBuZDmLENr4dz5ImIairN1KbivFbCZmkyg6AX69q34WwDIKPZqdXJJqPjNW40PmE1YhQ%2FTlc%2F7imzVeCLwrBMFUxWzedNhqP5%2FNRmHBiNc%2FMwe%2Ff20gWxYoMjsgOux5g%2F9OI784xfKlrhrxeK7Mgto3gE13h7ocdwlf7c5Wh4drv7oLsKRtDMK4A3KHaeYGUcTb99y4uXo9AkFH1SEw04D9vwwjOyRvQY6pgESExZIFjDnBDHqWDuDnHZkArvBT%2BOZipVZikY74Xh%2B96%2FOIu9YKp04nMKQC2H26Xv3THsaWnE0DIQ835TqxbY4pXHUR3MEg1xZgYxyHDbtd7meuLWrZR2COk1KBMk5%2FkaG%2FyvzNDhjXUjjC3itE44VMnW6ie7euGxuboFRJrTMP8j3jmbgETRGGp9PJASyPOXxpnsqQdRVHaS3bga17ZeBYewI6lmn&X-Amz-Signature=efd35ffe4b88dfb53e4c2653b4a6052cf185b5b855917583effa4a732b05d186&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP2THKAE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIF603tzZlAgdjWmYtP9rplFQo0uK1DSRYombaaG64eMjAiB4nomZ6DbpCURUvVs7Wjt%2BMbDQ2IqAMVM74X2JP5589ir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIM%2B8tElqjD4FYyhH1sKtwDmOFzTThqtCEd0GkZnk%2BUDc7amHHbivw%2FIkjYGaAu80WDcLVbyZgrsxS2ANa%2BOoo4wdV5B9jXMnuCw4xrG%2B4lAhARVTmMJZc1mjMtEs22ANTRgrw3tFZNC0zuZoahPw99GemSyd%2Bl4acOPD97ezGxBO1T2cZLUImBXuKe88ns4YPq0LXl1kQHj7gAzWTY%2FruYXwfrSTgRulDbKp7nPwEYPc5%2Fd9QV4ts2q5O2ztpmtZLC9SaircjfCXs3m5CQiKa8xsCAwqFLdL2lq13z5IpXYagu4aURnA0dfPkG%2BIJLA%2B7WstCqfA7tOY4xAj%2F%2BfqXcE%2FZnvuADcMeQ848uVCJ6XEQ%2Bx1Gi2jvzSR1p9yzMjEnJv5bS8xJ61IKyWOFW%2FrKZgswxLO%2Bxxq%2FrEkZS7yknpxrMMH%2FJIlop8GbxLQlDD75h3C12Lk2%2BMlmuA6sQFXO6TLFlj6LHI7R80ZzQq6dG4cBeKuwFH%2BKNV6Iyf3PNtpApXnPWi5SVW11Frq%2B%2FLzDiyNgg8rOrxDnHxJXJGMYe6cc35XBwh22W33alQD3bqVKLjVvZ76VLi7iIWA9K1kvXjHY2KW96X3puN%2B8TmuS49khfNb3tgbuy%2BMGXBFpYW2rNsQu6C2JHGO6F5iwwzeyRvQY6pgFjhzr8%2FnUR8cuqYEYZrO7713rUFwdRnRXD2oKnaxVOyEOkxQN6vuSiTFsANJOw6jxkRnNMikQI2gkni8QfBzGrTSOgR%2B2KUUoxaLF2YRxSYWT4EUf6ppw9xrP%2FluyeNFXMJMwFAYmW%2BUfiWF1CzjoqZWL2dBZb%2Bp%2FwjdU7LhJn3RWS88F5KcUjqdcU0FZD8AcYpnZgWJ7QRuiLW3Wx2wJbOb4h28eU&X-Amz-Signature=6ceaaa25a58e556b1b71c1e1446719c17db507fcc630ce45c968e875c7b1642d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7BWY3F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGIuNlTUoRatp3glpT%2F4pSSKsPBBjlbPOZD518uELC8rAiEAnrjgK7YNf39Cvxz%2BUfjYUH8PBGAjYAapDJeaVRugQlgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBp1PzpLMlWiZbV3nSrcA4JakBUmXVc4JVf4L94kJAjVP3AgVdrDwwo3gkrRHql2GdBnnLnw2Nq0FZueJ394HkwTjg6EWRTo90in7UAhXyHiV%2BG%2FEi3%2FDhoWs3EU64uTgIkQe%2BAQO5AmM4aBWtqj6Jw8dHMBBzkDGHR3Hob1HcMLSVSbyAPgNGKbpGdgLPKZ9KvzQNtYEDSA2WPX5CwkvVyv5fIGefGil1ZoXiEWtn86ZJGkdlolFjJwtpIB7mVrpqnxJ5FUgWC5vo0A%2BZY%2FmpjDQaQpxy7rCpkh5beRB9m0dfsumbMIDalC1AlWMwiYGZfUdNHnQZtBOymQG%2BqPw2G3DcXA9q9jpxihvYxLhgKWaxDXL0foWtSFo6FfiTfIH2CFANzC2o86ujqGjUsRR%2ByDPoBQjMf47t5Xa6NHPMChS7WAjPiDR%2FBn8V2fGJ4Mtu2Foj1wAS4rQQpE0PbyK8zBdIXu4y8v6H8%2BzzIzwJCNpJf56f0Dfs3d6TwQmfuMTvniRCehHKN%2BTlrR2HmI14DDXzFsPJkHBz6arykeMpufb4ojZfdzC1tgWC39iBmh98%2By9%2FAqmAlpVk6eUAbp%2BE3LDskVPmFhb5zNO0tpbuK%2FB08LpQE4aSg8kAjvm0MX%2Bl%2FWNyZDQ43rog4tMN%2Frkb0GOqUBh%2Fdb9KKTeTc2LKORk%2FXR8pDl8qStIDp5vuHw%2BzxOf0SO%2F9%2F8LqieQ5j0S2NJGQvvKDuo6EGN5pe%2BjEKv8HnEF%2FJ%2F1nYfWHIJAoNzAd1m42%2FYPXZYRdqcRX5gBx7P6Y8eTFASTwxOUNBibJ6Gc28ItptbWagEcbK9rZNBjV1MBLYOBWKM47VKQJtOlvoW5PKNarNVggYLtSALpChwxqhHHYXUGbPf&X-Amz-Signature=b8a32ba4de35e639052aa5850f170dbdd39b7cf5f97e424255e1371981616403&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7BWY3F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGIuNlTUoRatp3glpT%2F4pSSKsPBBjlbPOZD518uELC8rAiEAnrjgK7YNf39Cvxz%2BUfjYUH8PBGAjYAapDJeaVRugQlgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBp1PzpLMlWiZbV3nSrcA4JakBUmXVc4JVf4L94kJAjVP3AgVdrDwwo3gkrRHql2GdBnnLnw2Nq0FZueJ394HkwTjg6EWRTo90in7UAhXyHiV%2BG%2FEi3%2FDhoWs3EU64uTgIkQe%2BAQO5AmM4aBWtqj6Jw8dHMBBzkDGHR3Hob1HcMLSVSbyAPgNGKbpGdgLPKZ9KvzQNtYEDSA2WPX5CwkvVyv5fIGefGil1ZoXiEWtn86ZJGkdlolFjJwtpIB7mVrpqnxJ5FUgWC5vo0A%2BZY%2FmpjDQaQpxy7rCpkh5beRB9m0dfsumbMIDalC1AlWMwiYGZfUdNHnQZtBOymQG%2BqPw2G3DcXA9q9jpxihvYxLhgKWaxDXL0foWtSFo6FfiTfIH2CFANzC2o86ujqGjUsRR%2ByDPoBQjMf47t5Xa6NHPMChS7WAjPiDR%2FBn8V2fGJ4Mtu2Foj1wAS4rQQpE0PbyK8zBdIXu4y8v6H8%2BzzIzwJCNpJf56f0Dfs3d6TwQmfuMTvniRCehHKN%2BTlrR2HmI14DDXzFsPJkHBz6arykeMpufb4ojZfdzC1tgWC39iBmh98%2By9%2FAqmAlpVk6eUAbp%2BE3LDskVPmFhb5zNO0tpbuK%2FB08LpQE4aSg8kAjvm0MX%2Bl%2FWNyZDQ43rog4tMN%2Frkb0GOqUBh%2Fdb9KKTeTc2LKORk%2FXR8pDl8qStIDp5vuHw%2BzxOf0SO%2F9%2F8LqieQ5j0S2NJGQvvKDuo6EGN5pe%2BjEKv8HnEF%2FJ%2F1nYfWHIJAoNzAd1m42%2FYPXZYRdqcRX5gBx7P6Y8eTFASTwxOUNBibJ6Gc28ItptbWagEcbK9rZNBjV1MBLYOBWKM47VKQJtOlvoW5PKNarNVggYLtSALpChwxqhHHYXUGbPf&X-Amz-Signature=597433e15d4ac6e5a98869646ea5dbab1854b0a9b147ce2bdd75a16d749d20b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7BWY3F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGIuNlTUoRatp3glpT%2F4pSSKsPBBjlbPOZD518uELC8rAiEAnrjgK7YNf39Cvxz%2BUfjYUH8PBGAjYAapDJeaVRugQlgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBp1PzpLMlWiZbV3nSrcA4JakBUmXVc4JVf4L94kJAjVP3AgVdrDwwo3gkrRHql2GdBnnLnw2Nq0FZueJ394HkwTjg6EWRTo90in7UAhXyHiV%2BG%2FEi3%2FDhoWs3EU64uTgIkQe%2BAQO5AmM4aBWtqj6Jw8dHMBBzkDGHR3Hob1HcMLSVSbyAPgNGKbpGdgLPKZ9KvzQNtYEDSA2WPX5CwkvVyv5fIGefGil1ZoXiEWtn86ZJGkdlolFjJwtpIB7mVrpqnxJ5FUgWC5vo0A%2BZY%2FmpjDQaQpxy7rCpkh5beRB9m0dfsumbMIDalC1AlWMwiYGZfUdNHnQZtBOymQG%2BqPw2G3DcXA9q9jpxihvYxLhgKWaxDXL0foWtSFo6FfiTfIH2CFANzC2o86ujqGjUsRR%2ByDPoBQjMf47t5Xa6NHPMChS7WAjPiDR%2FBn8V2fGJ4Mtu2Foj1wAS4rQQpE0PbyK8zBdIXu4y8v6H8%2BzzIzwJCNpJf56f0Dfs3d6TwQmfuMTvniRCehHKN%2BTlrR2HmI14DDXzFsPJkHBz6arykeMpufb4ojZfdzC1tgWC39iBmh98%2By9%2FAqmAlpVk6eUAbp%2BE3LDskVPmFhb5zNO0tpbuK%2FB08LpQE4aSg8kAjvm0MX%2Bl%2FWNyZDQ43rog4tMN%2Frkb0GOqUBh%2Fdb9KKTeTc2LKORk%2FXR8pDl8qStIDp5vuHw%2BzxOf0SO%2F9%2F8LqieQ5j0S2NJGQvvKDuo6EGN5pe%2BjEKv8HnEF%2FJ%2F1nYfWHIJAoNzAd1m42%2FYPXZYRdqcRX5gBx7P6Y8eTFASTwxOUNBibJ6Gc28ItptbWagEcbK9rZNBjV1MBLYOBWKM47VKQJtOlvoW5PKNarNVggYLtSALpChwxqhHHYXUGbPf&X-Amz-Signature=ec75e163d79766693f9569c8f728033fad24a47e2aec52ad0811447d5227f187&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LJP75EF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIF13Yd6TwgvkRDCDNLQJN%2FxudcXvHODZW6LEVRNM4y16AiEA6QPaxXfszn6BL2i0RVdhA4qeZewBNRFMXudlpePDbkIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDAiupoHumYizk8lZtyrcA5srwIqOVuNPL33QE6pMvjk8fPxPqsrlaj5Cwwo093LGVaWkc1y52PYI2YfOq39z0RYnv8rJKkgpKgmfl58Ed3xJgI6OPeD0mdj2OqA9EyHGeo5GQy9TD4wT9ppEBfBm0D1A8RjqTlVnXhUs%2BJr7xPBvk%2FgF44YYZJhR9lcVsN2WK8eRWbEJ%2BpD4k1ZsxV71tm5pq0h%2BWxbhk6Yd6FxtWI4%2BfmoCOjZpz9jz%2FGGR2Umt5n4rhzaf5XLTr4DUPJNNgufAAyEEBXjTQ0CFnhuV%2Fv9mpE1qNcWw2A70%2F3li1GrJ3lgBMVBDA6N7ZZKY87Uj2PpnAR1FYnOLj%2FbR8ZWkX%2BC5Q4%2BIExLcUQFL64ieDWYbTLplFXK6reDRW%2FLjH6yzMU8PBDYu5r5fyTD8cMTZRZdcdme%2Be2dR2bMTw7lLYfvLyqyfhb5e%2FfFLk86eiCuDfSVhaWsSkGpZvS7L%2Fb%2FZ%2F%2BLcoNucv6IGnCNb1UWGku7m6QpSCJBpxte3L3vbMdvt06oo7T5dYFbDVjDzcjlfohP5YzrNvTbvJ3CmCp48pTbh2x%2FuXrVAekVOD5FheqYurpiCBY0xyOBaJmd9uhP7jAUhfu%2BgMCHHileY%2FoW%2BGsY1N%2FfQFPqM368XI8C%2BMN7rkb0GOqUB6AjGNQYckAK4V%2FPPRl4sviKFU7j4B9Gy4IaGdF2d%2BzTAtFWjaAS1Q1FsU0qn8Lv2jFoWu3CXVDYdQt8uUMSkcGaZ6Nv9LwZuVG7dW9hn2jp369mBVXbnPwOSfwND%2BU58cZwWeStI2vwO4%2BTtmNmp%2FXK09Uwy%2B6rvBHWfPEFSRjJzklIFiqKcPbQZYIHCRKpOYNmQL0s30%2B18A%2FhQaQHteNaTIhZT&X-Amz-Signature=0d573ee9382fd8a570dc5dc5ef1d8129b7b4468423c2a0f47b1dfc5e781a40c8&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAULAC7W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIE1NN34EGaSPJoLfoGov%2FyY1ADyGranBv5Y7p%2B4pYyG7AiEA9lvFR8rbdz4PUbV2PGKa4jIJpXWBnxqvjM3lUZDe%2FyUq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGSzz4Vrlp9wr0iu0CrcA9Jh8f8nqtA8uBJ0nY7UVoxdO2D8p%2Fd94kQuyhbca4X8Xjps5iIb89BBNP5SOlnKQp34ohQc4lfVHQXRqtyHki3Wqi9uJCF60iHw6YCO%2FAHWB5kUO954okzc%2B5TOZ9bP8Ytb5AKiYv6RrC8%2Fq%2Bt5Vdcc9WYZX%2Bl5BrPTTIi1mub1b8wgBd0ItRpsC8l4TiFPGez8cAiRMXk4Eur6d%2F1KWsQIkZ4CJ4qgHSSfdK6w57HwoVjT2VMrvSmOHOs%2FYgTOzRMeHupJLVsfOAOFUHZRHpIZqftIGQZNKH7PqJMueQgWbQOfJIKLyVTAjj3G0BBe41dcP93QgiIaDISwcq4ArjEMzxyYZT9MIPd6EngQLi4BLw1bTxkoV42DhgulUWDf62XOQutdAxBmdk9fVRQHRhldC322om4qItCvyK8fJbgyChzvCaltXq6vjA%2BEBaes8%2FkHIl6xxauWRG6evaahhJvCRamuBbSLXIN7I2kSAzrbPkPFxUHroIjtRmvcPvk%2F%2BkyhNE6GpFBN9SYMpkQCYpieQ1q3o%2FZkslIIzhxq09BN3uTngHXTwVhKltn3jLa44bg8bPFoQUa0IWrOp8iLXLj74BIdSTWwmEGAN%2FJ3SkvLFBn9vBaSr5X8b44KMIHskb0GOqUBhLzYRCdr6C8MEurI1ez%2BAn3%2F%2FDAwZFwpHQQ8EYK1vRk9381I%2FjE3HTrVEI%2FpNY12wq7xHnKZt%2BCNNqPvTMAcbX3WprsuZM8oq8yk34h5cVo7NvN0044d1wWvBY4TMeROZqA%2BMqwMJjVt36%2BoNuV%2BORO3BMMgdVZ1jndTrXU3HdcPVL%2Ff9y%2FtJSX3Y24Odc8yxb%2BWIe5Wfo2DfUWVJWGvd8ZtX1%2Bo&X-Amz-Signature=f2fb320f83aa84ce55ad300964326cdb491a71d418bb5930c325fe3880ebc4de&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBBOUIUU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGciHFajeCnBu69tYLNGlxOVXHOJorsybmG4Owj%2FnYw8AiEA1u3s9F5FfITO%2FO5oZJ3qCJgQA2mM31Y6wjqBc4xIwnoq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJTZvNKxPWlDYLYO%2ByrcA%2FP7Lf%2Bec6y2gQuictKLYwCSefzbLppBT0qWGxqUF2A8vvYu7AsPKCOiJf42usJl5g5xoSW8R1kkff3XuViKOXMpkB2yjMoFi7I6P8YR3oRH3mZsxdeQWIhZheNI1yngDIRfgqvSJzoLAtWbwdEwJjMlfmme%2FeL4VEiYATqaKJehcq1sW9GJL19Lk8dKYvfaiAizkNbtFKnLIL6b7FLMdqtFpZ0zbzqhto0XdRyQjisLWYG9ob%2Bx3o4VTwxc9BlPr8TkG3wE8pVdmsG9WHTVe%2FXPYLRbDqoHrb0Z1TgiGwQ717MsS2ns%2FUrV93YxNzzYc8Gr5QD22lH%2BrCcbFRVUXip0u6A1EkVmEmA%2FqrJjRthahee%2FUXUWsLFtg%2FPRlbHh9dSW1Ir%2FKCCoyyZJTT92xt220QTRPNOKnceMaJSQzejUUASvgofl75WuXfjhTpdQ6baGQTnoVTyFAEfM7fYLz3MEBsn4LhXUPGZSnAuX4Kc0Mwnd8OSpgfFZA0oCaCe10eBaHu0Wx1KGHCryAP%2FHezcPgvhtUWtjeAyAkHg3xPUC1buIDM89m7WlRIeFEEj8glhKA7wLl7uDyXSAHbkFdIhP5PUmnoiFwTn1BEuAhoNag0O4zI15KyJqtLGzMInskb0GOqUBU3yeLbsHS4GFWZoOpmMOey0nxiwmOtvjhka5KHHUvK3SaB364H3gTnamARbjBiNYtLAXMnMpnKiBwqGOPem%2FSDsHRQ2ZZp5uKj8j%2BDhFb1NIHbr5uyNpUdyFQRR3D5mP6QvUuiZyQ5ej%2F%2BzNMej1iUwySe%2F%2FLGw%2BcngoMwWzS2o0aTrKGFCyjEG8HMlN%2FT8IFIFEFrKQD0zG%2Bg8plTSsgNwVOhGU&X-Amz-Signature=d0c34c3840f1ee6d75691ad8deaf645276d96d417e819fac6a00a7d2afae2ae6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R3KK3QZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCJ%2FMadLaU4WcHCyj5ZQcDIPSYDdm7NrOc8exJaW55KOAIgLx53QK2Fjry2d2svhHQsGpvR2c0zl7q2nHVFi2A2Cl0q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDr8BLZulVgx02PvYircA7%2B9juvW4ZPUQg49WXPuUYncnULg4xxL5tyNRfzT7fY%2FkRR0A4xXCwAFqOlJhHH53k7pH8vmLfHEKX3GHPCPvuzx2tt%2Br93VPgZlxmhTK%2F0rUigKIgF3pIrn3QQUx2OJE67dduLMjHDLuhu4m0hFgbVcOpCjhSzqF3wkntnWjG7vyRq5SuiAfGPXIdZEYAIwM5Ka61RawDsBMujaPX75qvstu3aliISJF8JXS6w%2BOQ2KgVGqv54P3YheZY1J2c645MQOL4pnHQyQhumAjAklNo5%2FWbfFHAaOrtpgus6iyMQYhWRLkPYSo%2BL2gF3dVWM4J1d2U%2FfNI%2FIVemqWhvxmRv6TJQQRm6jVbrCeobcAcjsCbpCEx1XVcN%2FNRlmBmLlv57AkX%2BzRpLRn4tFIP%2BCst35vxbD4GllWGNYVK9vXPxtWmcSXuefW7vVMvtOEGRdaxm%2FLAx2Unt2Uck0PwrfHJjpRpTdcNYvUwAobZoJLeyEhbo1u%2BzyJw%2BJObvoTtZQwSVUHtD5ekivHPJM2nuffuFahvgGulH38srYMxAgaiUEFL7bXIlMRJIe8Edsts%2FkVo78vEQmOH4c1U%2F2E0%2BwdYP%2BVtb5q8p2AdzzmX%2B1PxyxJReCcjPo1jGeGlUiUMJDskb0GOqUBEqeaQVlNiK0JsVswulN1wxTUgnmzq7ODT640G5RoAKCaHScX3Xtwd%2FwLUvoh%2BiR0PRPAMaFjpfnU6JMoxqeDfMH73jxiB22Ku7I%2B%2FQPKXhthHTTZWPO1UUvNK1mZ57pGayoBzsJE%2F%2FpmPbL9rr8vKZXDcK7N5S%2FOIXgeSzrIxueh4uknXwqQjCOYnsed6Pmzek%2BlESgC9Be0Grcusndrtp4y2gq8&X-Amz-Signature=d24fa0c96ec68f9f07b8c91e2db9cc034dd676eb3d5a44845f8694d347dfefce&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R3KK3QZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCJ%2FMadLaU4WcHCyj5ZQcDIPSYDdm7NrOc8exJaW55KOAIgLx53QK2Fjry2d2svhHQsGpvR2c0zl7q2nHVFi2A2Cl0q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDr8BLZulVgx02PvYircA7%2B9juvW4ZPUQg49WXPuUYncnULg4xxL5tyNRfzT7fY%2FkRR0A4xXCwAFqOlJhHH53k7pH8vmLfHEKX3GHPCPvuzx2tt%2Br93VPgZlxmhTK%2F0rUigKIgF3pIrn3QQUx2OJE67dduLMjHDLuhu4m0hFgbVcOpCjhSzqF3wkntnWjG7vyRq5SuiAfGPXIdZEYAIwM5Ka61RawDsBMujaPX75qvstu3aliISJF8JXS6w%2BOQ2KgVGqv54P3YheZY1J2c645MQOL4pnHQyQhumAjAklNo5%2FWbfFHAaOrtpgus6iyMQYhWRLkPYSo%2BL2gF3dVWM4J1d2U%2FfNI%2FIVemqWhvxmRv6TJQQRm6jVbrCeobcAcjsCbpCEx1XVcN%2FNRlmBmLlv57AkX%2BzRpLRn4tFIP%2BCst35vxbD4GllWGNYVK9vXPxtWmcSXuefW7vVMvtOEGRdaxm%2FLAx2Unt2Uck0PwrfHJjpRpTdcNYvUwAobZoJLeyEhbo1u%2BzyJw%2BJObvoTtZQwSVUHtD5ekivHPJM2nuffuFahvgGulH38srYMxAgaiUEFL7bXIlMRJIe8Edsts%2FkVo78vEQmOH4c1U%2F2E0%2BwdYP%2BVtb5q8p2AdzzmX%2B1PxyxJReCcjPo1jGeGlUiUMJDskb0GOqUBEqeaQVlNiK0JsVswulN1wxTUgnmzq7ODT640G5RoAKCaHScX3Xtwd%2FwLUvoh%2BiR0PRPAMaFjpfnU6JMoxqeDfMH73jxiB22Ku7I%2B%2FQPKXhthHTTZWPO1UUvNK1mZ57pGayoBzsJE%2F%2FpmPbL9rr8vKZXDcK7N5S%2FOIXgeSzrIxueh4uknXwqQjCOYnsed6Pmzek%2BlESgC9Be0Grcusndrtp4y2gq8&X-Amz-Signature=8bee9a7cb35400242d48e454b2ef85c845a036a8fbf2b5e380c2c1c3ea58d1f6&X-Amz-SignedHeaders=host&x-id=GetObject)

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
