

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSLK2BWN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQCkoEcwsDnVF4zuETjle2Z%2BHXTMLQXGhfNLrPd8QAjEjgIgPqf2h8Rybj1HCae2W0kd6PKeTK7%2FYJ4lw0ZQRk7J8CEq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDPwvcOMuoNYXORqY2SrcA0kubxyK5cdiiRgWgS3Xy1sxO5hVgFN%2BHgho90w7%2FWNbV2nb%2BJLQlTXRwdDwIfIy00GCARd8YF%2BglZuZNKJkEExouGgF3F9S0PmQvUh7DaygPEPCuI%2F3T%2F0DnRBr8%2FWObXNM%2B6fVP9z%2FVB7BD9JWModjDtfPskee1nRihre%2FUbv%2FvwEykST26Hj2G9O%2F0yFSzYgsa4e1eZ%2ByKX6JAmCiRqIs7gcf71hvKXECvBvXNvpcUYA1KoBsMbJBjEEHRMugf7MUYlbmR%2B1N9SFtc%2BxN%2BLKD099CPB7wm2RKzrpU2hLOVk%2FVIxUoDf6vc06yB8Mb2dslpdhyA%2Fnr4s%2FAd70vCOVwVTwxayXwbWSGz1mvvGXFsP0jngQ%2FDzF%2BGWiiluJYlctahtNynP5s2%2B1OVGPO%2Bm3633w0yWclJyyMzyFWBlbL07K4rP82EFKoluiUjI2l3Dz0D4R%2FZStowciFbNDTB3JlU1tKxuA2v1PqKWN%2BaC6CE3dOVrf7lje41st9cuYxQ3VSnEmaPL0BUz4F1IaJwDF4tDYs8vYYZQuAvDGARKHXgJP6Y9WNTCIaFdL1%2B25gjA1c95mLUOe3KP%2FaEPWuzCV0S0MXfK4fI1igW9z1elLUCbG2O%2FiJ0IxdAgEDMLyRh70GOqUBZauUEkZCuAuAQgCzMVbNsfjszyYoerAPLdeYYpkJQLivgFhikr4Yh%2F%2FGiA%2F%2BXm%2BiW1SseN0UYRrmKMnsi9JMek%2FVH6JkCxZiNUvp2icXsI33pzRTSMePAZbbCQa%2FCddhzVQxjJFRspZN5jNeSFgt9nYcSKhW2eZgll7OutSBsMQPlfufqDA96Fu09GS3Eh21z%2F9rd3crtuD8ts2XeTCbTtnoJfz2&X-Amz-Signature=4fa30a2880e83b55b2bcf140286c78b96bbb7981839ce9364b64bc552799f4e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSLK2BWN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQCkoEcwsDnVF4zuETjle2Z%2BHXTMLQXGhfNLrPd8QAjEjgIgPqf2h8Rybj1HCae2W0kd6PKeTK7%2FYJ4lw0ZQRk7J8CEq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDPwvcOMuoNYXORqY2SrcA0kubxyK5cdiiRgWgS3Xy1sxO5hVgFN%2BHgho90w7%2FWNbV2nb%2BJLQlTXRwdDwIfIy00GCARd8YF%2BglZuZNKJkEExouGgF3F9S0PmQvUh7DaygPEPCuI%2F3T%2F0DnRBr8%2FWObXNM%2B6fVP9z%2FVB7BD9JWModjDtfPskee1nRihre%2FUbv%2FvwEykST26Hj2G9O%2F0yFSzYgsa4e1eZ%2ByKX6JAmCiRqIs7gcf71hvKXECvBvXNvpcUYA1KoBsMbJBjEEHRMugf7MUYlbmR%2B1N9SFtc%2BxN%2BLKD099CPB7wm2RKzrpU2hLOVk%2FVIxUoDf6vc06yB8Mb2dslpdhyA%2Fnr4s%2FAd70vCOVwVTwxayXwbWSGz1mvvGXFsP0jngQ%2FDzF%2BGWiiluJYlctahtNynP5s2%2B1OVGPO%2Bm3633w0yWclJyyMzyFWBlbL07K4rP82EFKoluiUjI2l3Dz0D4R%2FZStowciFbNDTB3JlU1tKxuA2v1PqKWN%2BaC6CE3dOVrf7lje41st9cuYxQ3VSnEmaPL0BUz4F1IaJwDF4tDYs8vYYZQuAvDGARKHXgJP6Y9WNTCIaFdL1%2B25gjA1c95mLUOe3KP%2FaEPWuzCV0S0MXfK4fI1igW9z1elLUCbG2O%2FiJ0IxdAgEDMLyRh70GOqUBZauUEkZCuAuAQgCzMVbNsfjszyYoerAPLdeYYpkJQLivgFhikr4Yh%2F%2FGiA%2F%2BXm%2BiW1SseN0UYRrmKMnsi9JMek%2FVH6JkCxZiNUvp2icXsI33pzRTSMePAZbbCQa%2FCddhzVQxjJFRspZN5jNeSFgt9nYcSKhW2eZgll7OutSBsMQPlfufqDA96Fu09GS3Eh21z%2F9rd3crtuD8ts2XeTCbTtnoJfz2&X-Amz-Signature=09a05e34e50627cb4384dd798a3f588e9f5f7d7e55d308d456edfd6e6d259f23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSLK2BWN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQCkoEcwsDnVF4zuETjle2Z%2BHXTMLQXGhfNLrPd8QAjEjgIgPqf2h8Rybj1HCae2W0kd6PKeTK7%2FYJ4lw0ZQRk7J8CEq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDPwvcOMuoNYXORqY2SrcA0kubxyK5cdiiRgWgS3Xy1sxO5hVgFN%2BHgho90w7%2FWNbV2nb%2BJLQlTXRwdDwIfIy00GCARd8YF%2BglZuZNKJkEExouGgF3F9S0PmQvUh7DaygPEPCuI%2F3T%2F0DnRBr8%2FWObXNM%2B6fVP9z%2FVB7BD9JWModjDtfPskee1nRihre%2FUbv%2FvwEykST26Hj2G9O%2F0yFSzYgsa4e1eZ%2ByKX6JAmCiRqIs7gcf71hvKXECvBvXNvpcUYA1KoBsMbJBjEEHRMugf7MUYlbmR%2B1N9SFtc%2BxN%2BLKD099CPB7wm2RKzrpU2hLOVk%2FVIxUoDf6vc06yB8Mb2dslpdhyA%2Fnr4s%2FAd70vCOVwVTwxayXwbWSGz1mvvGXFsP0jngQ%2FDzF%2BGWiiluJYlctahtNynP5s2%2B1OVGPO%2Bm3633w0yWclJyyMzyFWBlbL07K4rP82EFKoluiUjI2l3Dz0D4R%2FZStowciFbNDTB3JlU1tKxuA2v1PqKWN%2BaC6CE3dOVrf7lje41st9cuYxQ3VSnEmaPL0BUz4F1IaJwDF4tDYs8vYYZQuAvDGARKHXgJP6Y9WNTCIaFdL1%2B25gjA1c95mLUOe3KP%2FaEPWuzCV0S0MXfK4fI1igW9z1elLUCbG2O%2FiJ0IxdAgEDMLyRh70GOqUBZauUEkZCuAuAQgCzMVbNsfjszyYoerAPLdeYYpkJQLivgFhikr4Yh%2F%2FGiA%2F%2BXm%2BiW1SseN0UYRrmKMnsi9JMek%2FVH6JkCxZiNUvp2icXsI33pzRTSMePAZbbCQa%2FCddhzVQxjJFRspZN5jNeSFgt9nYcSKhW2eZgll7OutSBsMQPlfufqDA96Fu09GS3Eh21z%2F9rd3crtuD8ts2XeTCbTtnoJfz2&X-Amz-Signature=d3e4637709463ac6abb89e17226e214f4762011f7cb39130b095e919586fc871&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SKL32WN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCICKq3f2z9xOPZ%2BzA9qyA018AkkETvpc65I2PYa%2Bonm87AiEAkEqy0EMvpmg5rLTiH0zKqGCugOhdT1LPECBjDj7k8XQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDP6CedU%2BoBsyF1lBjCrcA8h4sYp%2F3FMPfQVcx%2FimBdzPqs5EhiYpJoe1mfmOYAPlZGJjCbHDyfIGO%2FFNen41SmOMLcAvCxL%2BwGpSopRxmPA0v9rozAkg4eqRP%2FfqHMH0z4aIBjc7DccHoJrbpOdNas1uMVUcIdl%2BaCoBe3nAAii3J0isAHW0MfqUIUa2Qc%2BRu7wA8ndJrygtKLHhFhpeGLnVUabLihvAY3NV6Vk51jAYn8H9I5gCCYDBiqGhprzyUD1dL1%2FD1XTub9a%2FFwzLn7J05vZAuR7kjGaxQjbH%2FhXizxOWWVoRGf5aC7sXIwOO8OmLGeleLckOP%2BNQ8njivQX9fABoiPswF5D7GKp3HLgAEV7Y%2FdCj04nd8P1M%2FLA4CPSX8FJxd%2B%2FsKhN%2B5COel945rd4o1kaaVoIgsTDGtxEW%2Fy4nAJRZE9e%2BNS0%2Fh0QdV0oNDZ0MAm9sNaISJJ%2FxsY1O2R2vzMzUMI3%2BjokFm%2F1qzXnaGiLInl0htbqRxx8W1JnnD6mVXPe6kl2NiJRHmdhCFCCxOeI%2Bz307pYDbF8zDu8x9EyGvx67zPe1t8XUJtGQxXLA5dmYAp4M02yP8%2FSHbXtkHhQBC5Y11M93KOQuRQOqgiufwNU5v4VFh2XeonuPdwjCLgRkkOZP6MPOSh70GOqUBCEwI4n%2F5AgoZprIIePO2ErhZv%2FegCSH0j1pUQPRSBstEkmM4CPMbzM2I81gR%2FbTT8wCkUq8tTN%2F1hzAfHV9HvUH9UiYwDm08nHCVlDDG1%2FYY9Wctg8ISMg2rGGrNlG0RWTTVcPw4BK5HqvW4lgXjn%2BtozuMDBuW75we0tV%2FYY4xgNDlEJq4o1KytwSZK%2F1JERUwJnQ9K70%2FjU3Rn1TWRBSqlewSy&X-Amz-Signature=b3f2ed25d0730495640a3618ef978700e63ffb2ed74c74b7574f39c58d3ce4fb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SKL32WN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCICKq3f2z9xOPZ%2BzA9qyA018AkkETvpc65I2PYa%2Bonm87AiEAkEqy0EMvpmg5rLTiH0zKqGCugOhdT1LPECBjDj7k8XQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDP6CedU%2BoBsyF1lBjCrcA8h4sYp%2F3FMPfQVcx%2FimBdzPqs5EhiYpJoe1mfmOYAPlZGJjCbHDyfIGO%2FFNen41SmOMLcAvCxL%2BwGpSopRxmPA0v9rozAkg4eqRP%2FfqHMH0z4aIBjc7DccHoJrbpOdNas1uMVUcIdl%2BaCoBe3nAAii3J0isAHW0MfqUIUa2Qc%2BRu7wA8ndJrygtKLHhFhpeGLnVUabLihvAY3NV6Vk51jAYn8H9I5gCCYDBiqGhprzyUD1dL1%2FD1XTub9a%2FFwzLn7J05vZAuR7kjGaxQjbH%2FhXizxOWWVoRGf5aC7sXIwOO8OmLGeleLckOP%2BNQ8njivQX9fABoiPswF5D7GKp3HLgAEV7Y%2FdCj04nd8P1M%2FLA4CPSX8FJxd%2B%2FsKhN%2B5COel945rd4o1kaaVoIgsTDGtxEW%2Fy4nAJRZE9e%2BNS0%2Fh0QdV0oNDZ0MAm9sNaISJJ%2FxsY1O2R2vzMzUMI3%2BjokFm%2F1qzXnaGiLInl0htbqRxx8W1JnnD6mVXPe6kl2NiJRHmdhCFCCxOeI%2Bz307pYDbF8zDu8x9EyGvx67zPe1t8XUJtGQxXLA5dmYAp4M02yP8%2FSHbXtkHhQBC5Y11M93KOQuRQOqgiufwNU5v4VFh2XeonuPdwjCLgRkkOZP6MPOSh70GOqUBCEwI4n%2F5AgoZprIIePO2ErhZv%2FegCSH0j1pUQPRSBstEkmM4CPMbzM2I81gR%2FbTT8wCkUq8tTN%2F1hzAfHV9HvUH9UiYwDm08nHCVlDDG1%2FYY9Wctg8ISMg2rGGrNlG0RWTTVcPw4BK5HqvW4lgXjn%2BtozuMDBuW75we0tV%2FYY4xgNDlEJq4o1KytwSZK%2F1JERUwJnQ9K70%2FjU3Rn1TWRBSqlewSy&X-Amz-Signature=e21ec38a7dbe07ea4d046b97ad3cbf73b3193908226dbc7bbf8fc76e93936c66&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SKL32WN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCICKq3f2z9xOPZ%2BzA9qyA018AkkETvpc65I2PYa%2Bonm87AiEAkEqy0EMvpmg5rLTiH0zKqGCugOhdT1LPECBjDj7k8XQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDP6CedU%2BoBsyF1lBjCrcA8h4sYp%2F3FMPfQVcx%2FimBdzPqs5EhiYpJoe1mfmOYAPlZGJjCbHDyfIGO%2FFNen41SmOMLcAvCxL%2BwGpSopRxmPA0v9rozAkg4eqRP%2FfqHMH0z4aIBjc7DccHoJrbpOdNas1uMVUcIdl%2BaCoBe3nAAii3J0isAHW0MfqUIUa2Qc%2BRu7wA8ndJrygtKLHhFhpeGLnVUabLihvAY3NV6Vk51jAYn8H9I5gCCYDBiqGhprzyUD1dL1%2FD1XTub9a%2FFwzLn7J05vZAuR7kjGaxQjbH%2FhXizxOWWVoRGf5aC7sXIwOO8OmLGeleLckOP%2BNQ8njivQX9fABoiPswF5D7GKp3HLgAEV7Y%2FdCj04nd8P1M%2FLA4CPSX8FJxd%2B%2FsKhN%2B5COel945rd4o1kaaVoIgsTDGtxEW%2Fy4nAJRZE9e%2BNS0%2Fh0QdV0oNDZ0MAm9sNaISJJ%2FxsY1O2R2vzMzUMI3%2BjokFm%2F1qzXnaGiLInl0htbqRxx8W1JnnD6mVXPe6kl2NiJRHmdhCFCCxOeI%2Bz307pYDbF8zDu8x9EyGvx67zPe1t8XUJtGQxXLA5dmYAp4M02yP8%2FSHbXtkHhQBC5Y11M93KOQuRQOqgiufwNU5v4VFh2XeonuPdwjCLgRkkOZP6MPOSh70GOqUBCEwI4n%2F5AgoZprIIePO2ErhZv%2FegCSH0j1pUQPRSBstEkmM4CPMbzM2I81gR%2FbTT8wCkUq8tTN%2F1hzAfHV9HvUH9UiYwDm08nHCVlDDG1%2FYY9Wctg8ISMg2rGGrNlG0RWTTVcPw4BK5HqvW4lgXjn%2BtozuMDBuW75we0tV%2FYY4xgNDlEJq4o1KytwSZK%2F1JERUwJnQ9K70%2FjU3Rn1TWRBSqlewSy&X-Amz-Signature=035c1b75f19003503eeb408134eacca3877c944494b72e229bbc05a6bba95583&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SKL32WN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCICKq3f2z9xOPZ%2BzA9qyA018AkkETvpc65I2PYa%2Bonm87AiEAkEqy0EMvpmg5rLTiH0zKqGCugOhdT1LPECBjDj7k8XQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDP6CedU%2BoBsyF1lBjCrcA8h4sYp%2F3FMPfQVcx%2FimBdzPqs5EhiYpJoe1mfmOYAPlZGJjCbHDyfIGO%2FFNen41SmOMLcAvCxL%2BwGpSopRxmPA0v9rozAkg4eqRP%2FfqHMH0z4aIBjc7DccHoJrbpOdNas1uMVUcIdl%2BaCoBe3nAAii3J0isAHW0MfqUIUa2Qc%2BRu7wA8ndJrygtKLHhFhpeGLnVUabLihvAY3NV6Vk51jAYn8H9I5gCCYDBiqGhprzyUD1dL1%2FD1XTub9a%2FFwzLn7J05vZAuR7kjGaxQjbH%2FhXizxOWWVoRGf5aC7sXIwOO8OmLGeleLckOP%2BNQ8njivQX9fABoiPswF5D7GKp3HLgAEV7Y%2FdCj04nd8P1M%2FLA4CPSX8FJxd%2B%2FsKhN%2B5COel945rd4o1kaaVoIgsTDGtxEW%2Fy4nAJRZE9e%2BNS0%2Fh0QdV0oNDZ0MAm9sNaISJJ%2FxsY1O2R2vzMzUMI3%2BjokFm%2F1qzXnaGiLInl0htbqRxx8W1JnnD6mVXPe6kl2NiJRHmdhCFCCxOeI%2Bz307pYDbF8zDu8x9EyGvx67zPe1t8XUJtGQxXLA5dmYAp4M02yP8%2FSHbXtkHhQBC5Y11M93KOQuRQOqgiufwNU5v4VFh2XeonuPdwjCLgRkkOZP6MPOSh70GOqUBCEwI4n%2F5AgoZprIIePO2ErhZv%2FegCSH0j1pUQPRSBstEkmM4CPMbzM2I81gR%2FbTT8wCkUq8tTN%2F1hzAfHV9HvUH9UiYwDm08nHCVlDDG1%2FYY9Wctg8ISMg2rGGrNlG0RWTTVcPw4BK5HqvW4lgXjn%2BtozuMDBuW75we0tV%2FYY4xgNDlEJq4o1KytwSZK%2F1JERUwJnQ9K70%2FjU3Rn1TWRBSqlewSy&X-Amz-Signature=952f3231be52e616994c75c63ddb760415c2887132102edf69e54f1e24da99c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SKL32WN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCICKq3f2z9xOPZ%2BzA9qyA018AkkETvpc65I2PYa%2Bonm87AiEAkEqy0EMvpmg5rLTiH0zKqGCugOhdT1LPECBjDj7k8XQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDP6CedU%2BoBsyF1lBjCrcA8h4sYp%2F3FMPfQVcx%2FimBdzPqs5EhiYpJoe1mfmOYAPlZGJjCbHDyfIGO%2FFNen41SmOMLcAvCxL%2BwGpSopRxmPA0v9rozAkg4eqRP%2FfqHMH0z4aIBjc7DccHoJrbpOdNas1uMVUcIdl%2BaCoBe3nAAii3J0isAHW0MfqUIUa2Qc%2BRu7wA8ndJrygtKLHhFhpeGLnVUabLihvAY3NV6Vk51jAYn8H9I5gCCYDBiqGhprzyUD1dL1%2FD1XTub9a%2FFwzLn7J05vZAuR7kjGaxQjbH%2FhXizxOWWVoRGf5aC7sXIwOO8OmLGeleLckOP%2BNQ8njivQX9fABoiPswF5D7GKp3HLgAEV7Y%2FdCj04nd8P1M%2FLA4CPSX8FJxd%2B%2FsKhN%2B5COel945rd4o1kaaVoIgsTDGtxEW%2Fy4nAJRZE9e%2BNS0%2Fh0QdV0oNDZ0MAm9sNaISJJ%2FxsY1O2R2vzMzUMI3%2BjokFm%2F1qzXnaGiLInl0htbqRxx8W1JnnD6mVXPe6kl2NiJRHmdhCFCCxOeI%2Bz307pYDbF8zDu8x9EyGvx67zPe1t8XUJtGQxXLA5dmYAp4M02yP8%2FSHbXtkHhQBC5Y11M93KOQuRQOqgiufwNU5v4VFh2XeonuPdwjCLgRkkOZP6MPOSh70GOqUBCEwI4n%2F5AgoZprIIePO2ErhZv%2FegCSH0j1pUQPRSBstEkmM4CPMbzM2I81gR%2FbTT8wCkUq8tTN%2F1hzAfHV9HvUH9UiYwDm08nHCVlDDG1%2FYY9Wctg8ISMg2rGGrNlG0RWTTVcPw4BK5HqvW4lgXjn%2BtozuMDBuW75we0tV%2FYY4xgNDlEJq4o1KytwSZK%2F1JERUwJnQ9K70%2FjU3Rn1TWRBSqlewSy&X-Amz-Signature=3ee94b3f32caa191e90407cfda93259786c33b961f2ee1bc9177d9ee8f7e104d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SKL32WN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCICKq3f2z9xOPZ%2BzA9qyA018AkkETvpc65I2PYa%2Bonm87AiEAkEqy0EMvpmg5rLTiH0zKqGCugOhdT1LPECBjDj7k8XQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDP6CedU%2BoBsyF1lBjCrcA8h4sYp%2F3FMPfQVcx%2FimBdzPqs5EhiYpJoe1mfmOYAPlZGJjCbHDyfIGO%2FFNen41SmOMLcAvCxL%2BwGpSopRxmPA0v9rozAkg4eqRP%2FfqHMH0z4aIBjc7DccHoJrbpOdNas1uMVUcIdl%2BaCoBe3nAAii3J0isAHW0MfqUIUa2Qc%2BRu7wA8ndJrygtKLHhFhpeGLnVUabLihvAY3NV6Vk51jAYn8H9I5gCCYDBiqGhprzyUD1dL1%2FD1XTub9a%2FFwzLn7J05vZAuR7kjGaxQjbH%2FhXizxOWWVoRGf5aC7sXIwOO8OmLGeleLckOP%2BNQ8njivQX9fABoiPswF5D7GKp3HLgAEV7Y%2FdCj04nd8P1M%2FLA4CPSX8FJxd%2B%2FsKhN%2B5COel945rd4o1kaaVoIgsTDGtxEW%2Fy4nAJRZE9e%2BNS0%2Fh0QdV0oNDZ0MAm9sNaISJJ%2FxsY1O2R2vzMzUMI3%2BjokFm%2F1qzXnaGiLInl0htbqRxx8W1JnnD6mVXPe6kl2NiJRHmdhCFCCxOeI%2Bz307pYDbF8zDu8x9EyGvx67zPe1t8XUJtGQxXLA5dmYAp4M02yP8%2FSHbXtkHhQBC5Y11M93KOQuRQOqgiufwNU5v4VFh2XeonuPdwjCLgRkkOZP6MPOSh70GOqUBCEwI4n%2F5AgoZprIIePO2ErhZv%2FegCSH0j1pUQPRSBstEkmM4CPMbzM2I81gR%2FbTT8wCkUq8tTN%2F1hzAfHV9HvUH9UiYwDm08nHCVlDDG1%2FYY9Wctg8ISMg2rGGrNlG0RWTTVcPw4BK5HqvW4lgXjn%2BtozuMDBuW75we0tV%2FYY4xgNDlEJq4o1KytwSZK%2F1JERUwJnQ9K70%2FjU3Rn1TWRBSqlewSy&X-Amz-Signature=edda9267b3495f5af81ce539f2524e7a403c5255b1d09a0bcae4c9edab338d08&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STBWJHWJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDSxTAfDjQVnTBFpTSNhYE1qI7m8Gv7geQZkfQdxINm8gIhAP5dBMyPJCCLCJT5Urn%2F0nDKJD%2Fpcym%2BGSYCLY%2FRrctqKv8DCCkQABoMNjM3NDIzMTgzODA1IgzSzOcAMaHTbvbiyCoq3AO42cCN2wIviUB621PeNCVUT9jXfKwx4Idmp2dARjSJp8BvYHClYkBa1VsecwUhlB2S9XAhUN7Cjtk7AKkJ3jGDRkyL4%2F%2Bd4kgcqPB1I%2FtiSJFdrrOgJGt6wLOc083vUttGz1xKmttQY4wE%2Fn0UU%2F9qM3JhmlOShS78mktaD69Pf51C0OafNG9vHWSz0iGYK5Agi9In6uBDgLCTHgdcMkztfvffoHTXqp%2FwJ067SRN7nWyssEVd8iJK%2Btsw25s1aFO%2BuA%2FB4cNYDuHSC4joBVbknTSC348ybj%2BkbFSv1MIu20YgTMveWJ1UCHBTvK7ZenbNbt45JC7MqYWp7jaHM%2Fk88PfKwCpDLkihfvNl5t4ryeXd%2Fl5%2BNRAc%2FIBkcaA3LZYythzJQbEnrbujE1lOuGJ5abb5Ks5zLS8sP2wI%2F1l67G3LwfvsMnQi3tD62PIKgyH8P7FDe7AKAuwaIOllARGvjDB4JTI5hIDykSJSD0McbO5Y8TYQk8ViLg9WoGNKNmh%2B1cHpRdFGR0u9zrTGhHwonZQTs4n4oVdnm0Gup9EDvU4fCVxqWqxuDbnXfw6uNPfJqpUdyrRp0ei24cyLW%2FIo%2FR9Myz80C7LleDnfZyg%2F6i7NHSNgF9PMOvnS2zCckYe9BjqkARKvPfqn9NO4CSshjLzfo1UP0c8L9rxQLK8LfqWR9xJCgd4qo%2Bz64qJpbrRf7DVfQgtO0cO3TLLTbwfg%2F8NGBeGhk0biF9TGUWoF%2FYt7nBWe0CBqyu4pg%2Fw5gS5cBE0mhjnQNo5oIBa8NoRQWbcW339JrAYAY2rLbQ0S7vEfCegV0tV1Pq9jHdHzLPMN5s%2FWcLlfvCRtRU401SBHaN2%2FLA0h6tyO&X-Amz-Signature=24105c813ed23080149516de31782106b791a2b07746c68538e302d9e430c954&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VQTMOTY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBtIPZGKrolm7ehzmEghID4EuxZKq87wJtRjhCFAkptcAiBhZ%2FddhaNwX7pIc%2B25QluohzFQFyh%2B4BXmUwKRvQkEJSr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMR%2BsDC9a3KCTH3OxpKtwDAhaHs3E7IZAImwmeQma1ObksOLGyAEe8GYpLw5Vk2lOFCKlJDYPl3RHX%2F%2FhXtX7NNQfgYlPoHW%2B5p0o0Gwgtwa2xC5lF0pDL%2BLwfj3id7jfW2549DMzBvoTYzcJ5iD%2B4PDWT6H%2BbQ%2Bbae8iVW%2BA0EJJsD6HZ5p8c94icaOCAbgLmm%2BPpIKtFx8jx80n%2FNZHia9iTsLMx5v%2BoSmee7f69Z97ODJQ5qUR1xXTgKY1Yuoq4kkiDKzTuZlvj%2Fd6B%2FBVu%2FyzAWntD41FH4XgFQSMHqYj8FSI4x3YIQjvBeqDLSXi2z9Rl000xbe33sxkX%2B4SWQ2HvtRwjJuJD3CmM4d3rtWt%2FLdcTQ38w9dscFW4J%2FtX%2B1wKZOBu4STF5DO%2BzcUYYxHfgIWlBNresUDMz09ScuSd%2Fyw8xqylp0ix9HzZdbw9QGwUu8wXVEtHca5OlAkYpWEqTFnu8sEZfk3XauL0cCIHVXC%2BX%2FfB1YB6Ur7h%2F5pu17CVLxdvNJzBQJyP8%2FpVzLP%2Bj4m%2FPfjnHAt3gozGrT61%2FVUU1ZLat0oEXcM7eTX9aZTCbbU4cPGJxTkUoO6oGgl29V2ojrEcCXyMUrcRbOwFlZP89BcFNEjhpiEPDLqoHFr%2FgHK9wv%2Fw0t2QwupOHvQY6pgHNzoZvcxAH9LPmj8eZByglzUm%2FjQK7tRIA8P2OmqBqHCMQG3pEya9e0pCDMIa5Y8kmtpQLPUoT1qspOVaN8CEU7%2B7sMCGilkg1tGuo1dNwo53lE3i%2BuSpQ7Jx7rGbURCH6e4LmzYzCny7WfG4WjW8%2FNi%2FUMPzfVH3ENjOB0X66xXihkk4pEalhkCuM5J6PNur4p6wnHmyq9lG2%2BKnF3ThnGIjrGnte&X-Amz-Signature=be04dbef4e04aa6dcf16454eebc37e1ae5881adfb83b9776d7b143776fde2818&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SKL32WN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCICKq3f2z9xOPZ%2BzA9qyA018AkkETvpc65I2PYa%2Bonm87AiEAkEqy0EMvpmg5rLTiH0zKqGCugOhdT1LPECBjDj7k8XQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDP6CedU%2BoBsyF1lBjCrcA8h4sYp%2F3FMPfQVcx%2FimBdzPqs5EhiYpJoe1mfmOYAPlZGJjCbHDyfIGO%2FFNen41SmOMLcAvCxL%2BwGpSopRxmPA0v9rozAkg4eqRP%2FfqHMH0z4aIBjc7DccHoJrbpOdNas1uMVUcIdl%2BaCoBe3nAAii3J0isAHW0MfqUIUa2Qc%2BRu7wA8ndJrygtKLHhFhpeGLnVUabLihvAY3NV6Vk51jAYn8H9I5gCCYDBiqGhprzyUD1dL1%2FD1XTub9a%2FFwzLn7J05vZAuR7kjGaxQjbH%2FhXizxOWWVoRGf5aC7sXIwOO8OmLGeleLckOP%2BNQ8njivQX9fABoiPswF5D7GKp3HLgAEV7Y%2FdCj04nd8P1M%2FLA4CPSX8FJxd%2B%2FsKhN%2B5COel945rd4o1kaaVoIgsTDGtxEW%2Fy4nAJRZE9e%2BNS0%2Fh0QdV0oNDZ0MAm9sNaISJJ%2FxsY1O2R2vzMzUMI3%2BjokFm%2F1qzXnaGiLInl0htbqRxx8W1JnnD6mVXPe6kl2NiJRHmdhCFCCxOeI%2Bz307pYDbF8zDu8x9EyGvx67zPe1t8XUJtGQxXLA5dmYAp4M02yP8%2FSHbXtkHhQBC5Y11M93KOQuRQOqgiufwNU5v4VFh2XeonuPdwjCLgRkkOZP6MPOSh70GOqUBCEwI4n%2F5AgoZprIIePO2ErhZv%2FegCSH0j1pUQPRSBstEkmM4CPMbzM2I81gR%2FbTT8wCkUq8tTN%2F1hzAfHV9HvUH9UiYwDm08nHCVlDDG1%2FYY9Wctg8ISMg2rGGrNlG0RWTTVcPw4BK5HqvW4lgXjn%2BtozuMDBuW75we0tV%2FYY4xgNDlEJq4o1KytwSZK%2F1JERUwJnQ9K70%2FjU3Rn1TWRBSqlewSy&X-Amz-Signature=00a46a64f32b2a09a50892fc2998c5f7f7fe680223bdca8a1589b3b5a3cda4ae&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SKL32WN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCICKq3f2z9xOPZ%2BzA9qyA018AkkETvpc65I2PYa%2Bonm87AiEAkEqy0EMvpmg5rLTiH0zKqGCugOhdT1LPECBjDj7k8XQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDP6CedU%2BoBsyF1lBjCrcA8h4sYp%2F3FMPfQVcx%2FimBdzPqs5EhiYpJoe1mfmOYAPlZGJjCbHDyfIGO%2FFNen41SmOMLcAvCxL%2BwGpSopRxmPA0v9rozAkg4eqRP%2FfqHMH0z4aIBjc7DccHoJrbpOdNas1uMVUcIdl%2BaCoBe3nAAii3J0isAHW0MfqUIUa2Qc%2BRu7wA8ndJrygtKLHhFhpeGLnVUabLihvAY3NV6Vk51jAYn8H9I5gCCYDBiqGhprzyUD1dL1%2FD1XTub9a%2FFwzLn7J05vZAuR7kjGaxQjbH%2FhXizxOWWVoRGf5aC7sXIwOO8OmLGeleLckOP%2BNQ8njivQX9fABoiPswF5D7GKp3HLgAEV7Y%2FdCj04nd8P1M%2FLA4CPSX8FJxd%2B%2FsKhN%2B5COel945rd4o1kaaVoIgsTDGtxEW%2Fy4nAJRZE9e%2BNS0%2Fh0QdV0oNDZ0MAm9sNaISJJ%2FxsY1O2R2vzMzUMI3%2BjokFm%2F1qzXnaGiLInl0htbqRxx8W1JnnD6mVXPe6kl2NiJRHmdhCFCCxOeI%2Bz307pYDbF8zDu8x9EyGvx67zPe1t8XUJtGQxXLA5dmYAp4M02yP8%2FSHbXtkHhQBC5Y11M93KOQuRQOqgiufwNU5v4VFh2XeonuPdwjCLgRkkOZP6MPOSh70GOqUBCEwI4n%2F5AgoZprIIePO2ErhZv%2FegCSH0j1pUQPRSBstEkmM4CPMbzM2I81gR%2FbTT8wCkUq8tTN%2F1hzAfHV9HvUH9UiYwDm08nHCVlDDG1%2FYY9Wctg8ISMg2rGGrNlG0RWTTVcPw4BK5HqvW4lgXjn%2BtozuMDBuW75we0tV%2FYY4xgNDlEJq4o1KytwSZK%2F1JERUwJnQ9K70%2FjU3Rn1TWRBSqlewSy&X-Amz-Signature=790ec1e12fabc7d55592ea884839d4d6908d2322718e0161cf8d550b1eeaa3c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SKL32WN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCICKq3f2z9xOPZ%2BzA9qyA018AkkETvpc65I2PYa%2Bonm87AiEAkEqy0EMvpmg5rLTiH0zKqGCugOhdT1LPECBjDj7k8XQq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDP6CedU%2BoBsyF1lBjCrcA8h4sYp%2F3FMPfQVcx%2FimBdzPqs5EhiYpJoe1mfmOYAPlZGJjCbHDyfIGO%2FFNen41SmOMLcAvCxL%2BwGpSopRxmPA0v9rozAkg4eqRP%2FfqHMH0z4aIBjc7DccHoJrbpOdNas1uMVUcIdl%2BaCoBe3nAAii3J0isAHW0MfqUIUa2Qc%2BRu7wA8ndJrygtKLHhFhpeGLnVUabLihvAY3NV6Vk51jAYn8H9I5gCCYDBiqGhprzyUD1dL1%2FD1XTub9a%2FFwzLn7J05vZAuR7kjGaxQjbH%2FhXizxOWWVoRGf5aC7sXIwOO8OmLGeleLckOP%2BNQ8njivQX9fABoiPswF5D7GKp3HLgAEV7Y%2FdCj04nd8P1M%2FLA4CPSX8FJxd%2B%2FsKhN%2B5COel945rd4o1kaaVoIgsTDGtxEW%2Fy4nAJRZE9e%2BNS0%2Fh0QdV0oNDZ0MAm9sNaISJJ%2FxsY1O2R2vzMzUMI3%2BjokFm%2F1qzXnaGiLInl0htbqRxx8W1JnnD6mVXPe6kl2NiJRHmdhCFCCxOeI%2Bz307pYDbF8zDu8x9EyGvx67zPe1t8XUJtGQxXLA5dmYAp4M02yP8%2FSHbXtkHhQBC5Y11M93KOQuRQOqgiufwNU5v4VFh2XeonuPdwjCLgRkkOZP6MPOSh70GOqUBCEwI4n%2F5AgoZprIIePO2ErhZv%2FegCSH0j1pUQPRSBstEkmM4CPMbzM2I81gR%2FbTT8wCkUq8tTN%2F1hzAfHV9HvUH9UiYwDm08nHCVlDDG1%2FYY9Wctg8ISMg2rGGrNlG0RWTTVcPw4BK5HqvW4lgXjn%2BtozuMDBuW75we0tV%2FYY4xgNDlEJq4o1KytwSZK%2F1JERUwJnQ9K70%2FjU3Rn1TWRBSqlewSy&X-Amz-Signature=dc93aab15095de12fb7127be8129f5af188fa1edc1e90a3f7ffde07fd86565b4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FNP65BW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIE8MgXuvg4SHSjcZLHwm5sfQ%2BPsfM7metN%2FM%2Fw%2BvHGTtAiEAlHBNiOr79xWFwzHp%2BAugvPz08vPgcQOooROfSj71AqIq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDJ5QwIwuKhlKF57fkSrcA%2BQ7MXDoItd%2BCR8x8abWOG6JzRdwqj%2BQ8L54uO1y4C0BZ%2BQ6JXBW6ubOolpe5dI53VomCxRIfAlULVghMBy1ZYAC5Y0byUH%2BNJjyzrdPLfX%2FbNKrconz%2BajcH40FKycSzO8RYD56WWeNAF%2FZ7FjLeVZtE5ngccxZdbVw0dOtMAULrMotI0nRY6vqW%2F8nxswkhPjXPwvQOaCsOJf%2BA%2FxYfbeaxjRvQCoAQ7Pyx1B82RO8PpeYVlQSFAy8hLwiRBtYE%2BkUquOv1hJI45zC9fQmm3FUEYMEwqXzdEBn6ZukxlEOSe7qGBCFwEtHLI2VvR0%2FsnkWZ%2FCc%2FzcPH1D%2BQl3V%2FlIReVtOcHVqPecMJL%2F9kP9GoAcZ7nYJeLp7yx3zbqZanfn8MStDu9Tv5AFc7rMQAOZcH%2FsfH0yko09XCgeTa36kz41jdVRTAaa8P5bNSBywypNe07woVNAJFqFeEgQ0fST77sawa42zZlRAzMiPo2ROPAtZSyqg%2BmeRsjGXB2T%2BGYGjqoBkTQYxf8ubLFld7D8dvG%2B0LzNVrOZ0x6R5WN8buhSBAovkMHO5%2BtN1m9zRHhHzWzyDEUqtPIjZQTgbUIXTZIFXv3c%2F7%2B9iuqzy48kg2OtDnGWDsEOaZo1vMLKRh70GOqUB%2BIllLVOjLnN7XA8LdcveKTtgjT17ZxnuXdNXjwhwZfoh27LX2r%2Fd73kyV7ivnQssfOMWyCbSGtaZuX6QFh%2BfXBvq58nKFs4MjHXZPqySio2%2BMVVfqCzIGVpk8MdqOZ5hwqMItLW%2BsXIOZjEc8zlT%2FcZ30eyZbC%2BwKL%2BH4FrqhFK901jiTXwUREsn8TP1HMfUY72k6zPNwJuj%2FZ0Eifm%2F0lKL4mff&X-Amz-Signature=d5bbe425f4e56135c827c0a7f6f52d178609840d488289c33c25c85162c3baff&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U62KY7H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD1V8RFQsEAy1xmG%2BZ9nmx60WEffSxDpuKupEzORxRVmwIhANQmruWae4osOy2KCc9bhnI0hmKJD0cmwp%2BhlM91yOkeKv8DCCkQABoMNjM3NDIzMTgzODA1Igw38rhONkbIobgooY4q3AN63RfEUtA0SjA1MxKJxsUp%2B%2B5mjvAOJfo1CGm47Uid43QR6mTx66olD37vnWqQNp1%2Fp1BzVBGAGW8K6yUhVrq7RGy%2BrAdnWNDWHIjyQ%2Fd3Yd5lQJIgESlDeAzRO1JJ9rzSvbfiZX%2Fs521NQlJJZgIv5HZoT47Fwmj0%2FQ9tl6X4MtNyNRTNzRAM%2Bj7%2BF4ffPUupzjg9idEDuTJwUEsBs1bQVLPaafMui6ZW8Mcg3y2p%2FcodCgkx0UoUjFag%2BwoYZlqj7Rb36aEI33kcNt9fu13OLMIIxuGYQ1ZoBJCZma0OY6witw1zXgOKw3s0ootxPamcaU3sTnEmETwe50EcJdG4BI7qEVafS8U5J63gTkuk8YEDc%2F9HCoDzGvwKQgESyNhpaw21Wlb26VBQkyYs4ZTPnDapq1C7bRnUERyJvbGHwt7F9V2mQD2mE70zfgTqeOvVTtfJwih04Fo1PLY8ipdfAdujUahwbeNs%2F27DH3hoWoA1XNwpOvLNXWEGW4R8mi1EZOP9RtCwliAh85XG4gTdsOD3HDuZBlqaBvobLhMMt3A7Bi3XLQuEQjfFr0ZknjGKRGrRcoc3JysUVfrwESgp2bSHUYz4EqQIaPCBQ7SDKoaMhj6W%2FDP3cOKibTC6k4e9BjqkAaq629b7OCyajE%2FCMR6F5zmG6F99pRHA5JTrutcqZMWfOcV1ZNzmnCGzrizsdlcl%2BKvGl0KgJLqFc3QRD3AL68TAZ%2B1Dpd0Wj6W8R2Ie3UtQPQi%2BbtFROYqnDJB49NGaH%2FSzACuYSRQ2NaNYG3LzglR48TLiclvjRwDdLh5JS53lLpiXHs0dQzuHtti%2BZdOKWuIBwqcIxtb8Vj9EAPEPVpqbRQQx&X-Amz-Signature=bf5c5c456e2b5a0fae064504d767b743aece64a62d2f4d93af75c1b45e7c7b8c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPSG4E3L%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQDT2fZ%2Btnownhf8d%2B6PW9glmwtX9Rr5dM75xo7j7g6afwIgWjz3HUgCTYTSKFMeRBCzsEfc0hFiLCWC1dCLTG30rgUq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDJU6b1joz%2Bczx%2BIlLSrcA8l4xIwbdwZdDoiLqJk9A0tVg09s7Hw3X4EgTsKwcEN5WTBsWdNAbh%2FER2KOcb%2BipIKahCOHrCAr4P5tmZLrClyFlybZZTPQjViit5A77OvbCOFDKZZH0gGzgEWDaBZU5nqmV4JxRw9WcKMRSIzQeew2JyONz81oUKMDNSaz3ABfObB4EZca7lsnK44HDZ%2FXOfuy99l4HTEHqKH8QnOqEX2zFPQC0a8qhpqHNeVXh2dAvunCFPI6LpHhGksLqtflEQA%2Bqy317iwJPaHZVrjFpCqpQOzSaPkWtAVsN295obrWL9fRQ4VRP3ETJZ2TObiYYuVHL63kc8SXFgDJEWHDNxy833TZb20IwlXV6g3i%2FrdQmbKH19ZrWYXE0%2FkRMooEjWKhg4GDYI5hkH9tr8fMaLmriYkuO1wJ9a%2F6xZVxrUyU3rEkMWxdgG%2By8Z0wEWpbC0q9EV1hNM20YnT5gA03%2FytbFeYt%2FwhZJVVs7bxK0h1FxLj3tZ57ZCE2%2Fi37d%2BXc8BObMF3RcMbDwaV1No5Ab%2B3y0HuPIXx9IrfcNzdzJXpYoE3Q1%2FjcdCDOczjk%2F%2BeyEwuZajvBcTlKahT8bED0p59qihRhuivIINxrzWhwYbG5H42qOs5KJCygg%2BzWMM2Rh70GOqUBdTQrX8QAYE85vn7Cwap6qrUiU2f2cE%2BxqcnUJ0aFcz%2Fj5y%2F2zCmx4k1SO8IAyn4dDum6eOFCNcbZJ1w5cQoMUQeEngm%2FJCGMYogP2W4Ud1IgVCGuGLvoWdSLhFrBCfJv5nHQ%2BZYOghkpFYCwWsrUv6RgVgRJr3AqoW86i4UoQZq2TBh49yH989lQ8HFFnCAJv1YQlDPBnmdoThNw665ZGcFy3%2FYP&X-Amz-Signature=80333d23ac4483fe9448b8948fa02c4a9654a1faf56d2ce10686d3481f89d215&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD5IKFYI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC5zVIs8xsAuI1R6KicjdSfeXuQ1Q8e3H9xVNpbRl6maQIhAOkr8OB6i7sErrvzFUj48JTceBvKPkurWDIBsB9avtT6Kv8DCCkQABoMNjM3NDIzMTgzODA1IgxTEAmy0co7jm4PMXEq3APMeu3D91CwGTWwGZNMpraRk6Y79B32IcCzExJxvTof%2F7pSnpVu2Y0bFXrV1louiumxB7QOJTGiD9bZcxBYYfPOh4ojJAm67tbbHyCYWCn1bNFLWDakPih3wTrbtM0dVob%2Fn%2F1Hyysn6Xuk6zSvJCJMAzCL4hBPByMbUEgXy7Ui8fpWak4727BAlMDm3GA0BtJozkJ%2BZB0ZE2ce6ZpBsHkNjTn0WNySZ0qMxTlY3F7n6Nk5KZt1vu2yJYA6%2FOnUmtsFXB96VxWQHc4ZDMJpDPpiGB3ENPoGm7DaylNruLtav%2BHKOsFp8LIWZ43UozLD%2F5uvq%2Bsz%2BitouCHTf3GqMZEhxP83ZRPlapcxl43ZkQT6StNNgMD%2BKgwwBp3ToZ2T4Yb7MGBsJGvKLB1VCb9RMDmTTNT0SOhKB%2FkeXR3dvK7Bjql1KDx%2FXOfjTyFHoq0wf5PMoAPiS901%2FGa4fE0L44qFqZ4U4DvEl97tDqHKT2xx%2F80RcYHJsLoekd387IP2fF4qx4Afnulto%2Ft36RxOUWELONuBnOkm0kyqinSYDbXWDXUU1rbPljjtd6R%2BIOzrJ24rGc8e44itxuUDO28%2F6CVYZpx7801rVaSi637o421KsH2ofe4rOViEruAZFjCykYe9BjqkARZyWaJ7wFW9kXwyw5F8XX1Zp%2Fdi8uCrlnpCX%2FttCNEEfTqbhgz4IU5Uhh%2BB7871Addx9fo2r2dz77hhGr0DIOCB%2BE0e0QYFmztDL%2Bz74j8Qy8LDtDp9bW62%2BZy1A5c5TajBaPftWTEqHAHWDB%2Fsbk1M1Xm7EJiteDSTKjW%2BYKUhOB73svgnlHseVRQO%2FVZ%2BwSuNTz57BJ2ns8wirHylWFlYediw&X-Amz-Signature=bef49d675a64bf5a060ea3690085c17dce6202d43662d1adf8ad3f0e3063dbb0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD5IKFYI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC5zVIs8xsAuI1R6KicjdSfeXuQ1Q8e3H9xVNpbRl6maQIhAOkr8OB6i7sErrvzFUj48JTceBvKPkurWDIBsB9avtT6Kv8DCCkQABoMNjM3NDIzMTgzODA1IgxTEAmy0co7jm4PMXEq3APMeu3D91CwGTWwGZNMpraRk6Y79B32IcCzExJxvTof%2F7pSnpVu2Y0bFXrV1louiumxB7QOJTGiD9bZcxBYYfPOh4ojJAm67tbbHyCYWCn1bNFLWDakPih3wTrbtM0dVob%2Fn%2F1Hyysn6Xuk6zSvJCJMAzCL4hBPByMbUEgXy7Ui8fpWak4727BAlMDm3GA0BtJozkJ%2BZB0ZE2ce6ZpBsHkNjTn0WNySZ0qMxTlY3F7n6Nk5KZt1vu2yJYA6%2FOnUmtsFXB96VxWQHc4ZDMJpDPpiGB3ENPoGm7DaylNruLtav%2BHKOsFp8LIWZ43UozLD%2F5uvq%2Bsz%2BitouCHTf3GqMZEhxP83ZRPlapcxl43ZkQT6StNNgMD%2BKgwwBp3ToZ2T4Yb7MGBsJGvKLB1VCb9RMDmTTNT0SOhKB%2FkeXR3dvK7Bjql1KDx%2FXOfjTyFHoq0wf5PMoAPiS901%2FGa4fE0L44qFqZ4U4DvEl97tDqHKT2xx%2F80RcYHJsLoekd387IP2fF4qx4Afnulto%2Ft36RxOUWELONuBnOkm0kyqinSYDbXWDXUU1rbPljjtd6R%2BIOzrJ24rGc8e44itxuUDO28%2F6CVYZpx7801rVaSi637o421KsH2ofe4rOViEruAZFjCykYe9BjqkARZyWaJ7wFW9kXwyw5F8XX1Zp%2Fdi8uCrlnpCX%2FttCNEEfTqbhgz4IU5Uhh%2BB7871Addx9fo2r2dz77hhGr0DIOCB%2BE0e0QYFmztDL%2Bz74j8Qy8LDtDp9bW62%2BZy1A5c5TajBaPftWTEqHAHWDB%2Fsbk1M1Xm7EJiteDSTKjW%2BYKUhOB73svgnlHseVRQO%2FVZ%2BwSuNTz57BJ2ns8wirHylWFlYediw&X-Amz-Signature=cc5e8d8cc00d28568f2924e55011688dc2175b796fdc5402497c56908bba7a66&X-Amz-SignedHeaders=host&x-id=GetObject)

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
