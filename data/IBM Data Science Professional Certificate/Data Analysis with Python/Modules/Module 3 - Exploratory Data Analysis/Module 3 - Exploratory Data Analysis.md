

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V5I75YG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCb8YrsjwsuVi8U8nE%2FjU7hnA4rQEbuKeR6fA6%2FF4Y5uQIgeA9dkhB9slGzZ%2BgIEDqA4pHT64US2G8MZsvMumtAMB4q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDOTYnsoasnUabWMcEyrcAxq48Gz0V2%2Bfz42I%2FSRB7pW7iuXBU3pDvAEbHwcD9i%2BUPNNb3h8gyoIVfautcVSPx0VhOfPXjNkFP9uryN392UHcCmjMCoZP86yYC8f9%2FYGiatjrN8UFlajK3e6tXEVQ%2Fn6YCUQGUt5LqpvfoH1X%2BHaB%2F5mxGS9EceNwh6IYDCnO2nKlGSpsXnRDyVyGShKGNI6YRvkDagsP1aButr9yxWInwzxQTwdKm6i5Wjq1zbeumoi01Ac%2FZkX1N9ArqLpeOE3h4TNvOAcLmk7goDQeh8G%2BFVFz82tjiXYXaw%2F8AvmT%2FlnTHF%2FqNnjc%2FslY0bldz%2BNZypyv3VSsDF4QVdm6yIwKw4YYn13ThZZx55xoCQHI7OKzXoCKP5o26JHlPrGBrCYE8WbMXh4Cfd2m%2BfSDzOzVpNRgO7L3LoMVIZR1EK7vnPLhIVlkjJILdUhA505TWRo1LlA9p8rR2qY0LYTRVCrsSY45gwz%2BuLrCTcOFSRnfeXiCsfSxLXrF56ZA%2B1DK%2Btc07aMBxG3SXnT3tiZGr%2F%2BSpLctyGZfNj%2BwxZqxQs2Nsbw%2Fa%2Bsk5gC3mgg5U3TYC0Ev%2Bw3CEGN%2Fo2XrJ6s%2BGUEWj61CXfGZdC7Yqn%2FP2%2Fp8ALy4yD92nymZ7ssXMPO6jr0GOqUBUi2BhJT40b0KTY7sWxK%2BiutnYkX%2F7HRHWvIo2qWgGVAvi7mnbBpFbT7yCj7Re7uUknQWdTXwxnF8F%2FPG9VJ2UeEx1nmm863jz3q4WITvCQ%2B%2BJ3fCKKegel2J%2BHHC5zrzkST5OzXjK%2BALqvfiVoCfzTnuDcmFGm%2BrVLf66CV%2BKuS4%2FMm9lQ0YCmTrorTzLQyu0lP1CMXhKNkp1FrrlHKpAcGGuJn0&X-Amz-Signature=912a5e80347488a8e9424e60b9ae3c9078f17f0fa423abd6ded0deb188485a0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V5I75YG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCb8YrsjwsuVi8U8nE%2FjU7hnA4rQEbuKeR6fA6%2FF4Y5uQIgeA9dkhB9slGzZ%2BgIEDqA4pHT64US2G8MZsvMumtAMB4q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDOTYnsoasnUabWMcEyrcAxq48Gz0V2%2Bfz42I%2FSRB7pW7iuXBU3pDvAEbHwcD9i%2BUPNNb3h8gyoIVfautcVSPx0VhOfPXjNkFP9uryN392UHcCmjMCoZP86yYC8f9%2FYGiatjrN8UFlajK3e6tXEVQ%2Fn6YCUQGUt5LqpvfoH1X%2BHaB%2F5mxGS9EceNwh6IYDCnO2nKlGSpsXnRDyVyGShKGNI6YRvkDagsP1aButr9yxWInwzxQTwdKm6i5Wjq1zbeumoi01Ac%2FZkX1N9ArqLpeOE3h4TNvOAcLmk7goDQeh8G%2BFVFz82tjiXYXaw%2F8AvmT%2FlnTHF%2FqNnjc%2FslY0bldz%2BNZypyv3VSsDF4QVdm6yIwKw4YYn13ThZZx55xoCQHI7OKzXoCKP5o26JHlPrGBrCYE8WbMXh4Cfd2m%2BfSDzOzVpNRgO7L3LoMVIZR1EK7vnPLhIVlkjJILdUhA505TWRo1LlA9p8rR2qY0LYTRVCrsSY45gwz%2BuLrCTcOFSRnfeXiCsfSxLXrF56ZA%2B1DK%2Btc07aMBxG3SXnT3tiZGr%2F%2BSpLctyGZfNj%2BwxZqxQs2Nsbw%2Fa%2Bsk5gC3mgg5U3TYC0Ev%2Bw3CEGN%2Fo2XrJ6s%2BGUEWj61CXfGZdC7Yqn%2FP2%2Fp8ALy4yD92nymZ7ssXMPO6jr0GOqUBUi2BhJT40b0KTY7sWxK%2BiutnYkX%2F7HRHWvIo2qWgGVAvi7mnbBpFbT7yCj7Re7uUknQWdTXwxnF8F%2FPG9VJ2UeEx1nmm863jz3q4WITvCQ%2B%2BJ3fCKKegel2J%2BHHC5zrzkST5OzXjK%2BALqvfiVoCfzTnuDcmFGm%2BrVLf66CV%2BKuS4%2FMm9lQ0YCmTrorTzLQyu0lP1CMXhKNkp1FrrlHKpAcGGuJn0&X-Amz-Signature=f5c17bb3fa4eba9dd0f39632ecdf228c8d666321bd6e0e33a96f51713911ed3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V5I75YG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCb8YrsjwsuVi8U8nE%2FjU7hnA4rQEbuKeR6fA6%2FF4Y5uQIgeA9dkhB9slGzZ%2BgIEDqA4pHT64US2G8MZsvMumtAMB4q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDOTYnsoasnUabWMcEyrcAxq48Gz0V2%2Bfz42I%2FSRB7pW7iuXBU3pDvAEbHwcD9i%2BUPNNb3h8gyoIVfautcVSPx0VhOfPXjNkFP9uryN392UHcCmjMCoZP86yYC8f9%2FYGiatjrN8UFlajK3e6tXEVQ%2Fn6YCUQGUt5LqpvfoH1X%2BHaB%2F5mxGS9EceNwh6IYDCnO2nKlGSpsXnRDyVyGShKGNI6YRvkDagsP1aButr9yxWInwzxQTwdKm6i5Wjq1zbeumoi01Ac%2FZkX1N9ArqLpeOE3h4TNvOAcLmk7goDQeh8G%2BFVFz82tjiXYXaw%2F8AvmT%2FlnTHF%2FqNnjc%2FslY0bldz%2BNZypyv3VSsDF4QVdm6yIwKw4YYn13ThZZx55xoCQHI7OKzXoCKP5o26JHlPrGBrCYE8WbMXh4Cfd2m%2BfSDzOzVpNRgO7L3LoMVIZR1EK7vnPLhIVlkjJILdUhA505TWRo1LlA9p8rR2qY0LYTRVCrsSY45gwz%2BuLrCTcOFSRnfeXiCsfSxLXrF56ZA%2B1DK%2Btc07aMBxG3SXnT3tiZGr%2F%2BSpLctyGZfNj%2BwxZqxQs2Nsbw%2Fa%2Bsk5gC3mgg5U3TYC0Ev%2Bw3CEGN%2Fo2XrJ6s%2BGUEWj61CXfGZdC7Yqn%2FP2%2Fp8ALy4yD92nymZ7ssXMPO6jr0GOqUBUi2BhJT40b0KTY7sWxK%2BiutnYkX%2F7HRHWvIo2qWgGVAvi7mnbBpFbT7yCj7Re7uUknQWdTXwxnF8F%2FPG9VJ2UeEx1nmm863jz3q4WITvCQ%2B%2BJ3fCKKegel2J%2BHHC5zrzkST5OzXjK%2BALqvfiVoCfzTnuDcmFGm%2BrVLf66CV%2BKuS4%2FMm9lQ0YCmTrorTzLQyu0lP1CMXhKNkp1FrrlHKpAcGGuJn0&X-Amz-Signature=0439daecddee4ffd2c297c7a42c6b8d9afb91e6b8d2b8a45addd1daedd428eca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUEA2RYW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEbPILCh8lTG8U5NJenVx6iKcgkkqTMLqZk7DdV1vYqrAiA9PA3e97uTNeB9Y%2F1lIEgdq98eF%2BCl4PioPEiAFYi%2B8yr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsp8lcaeKHb6BthBdKtwDaGhcKP5APgiXcaHB0rMJUcKt7uatcmnvoKYxb%2B%2FrjkYsm8coO1xVPx4ZRUkv8ogzJ%2FtMy43RSS1BuaWCgMi2j%2FeYymLFpJcxQHNNsGntknxR0lqpOuPlFdD1eSVHRiR9hLfadMjkTRsmRC0MBxyM068%2FcwJA%2BvP3cMFi128nFC%2FAuZqjHBgn3IlXVP3lfDgj1wYPqAl%2F0JmlROCILiJ3cE8Vpoc3Yl%2FM9peLplL%2FxJH0lnDX%2FqEW0Q5Q5I%2Brh4XdR5DRP39t5wSz%2FQeK%2FtGRRpppTp11Elcg5N69LG%2BzrEXg8KdU63pH4ExQyDJgy6I%2Bm0ynqPisPvqxnx9gCqkhp2dnLYnCevWhNOrNeXxuekXc8kIhBS1QXmqyeEMqmg2kd0hzxzMKuqkuLzP7BL6GxSIw1fPhAAn8QHTOBp2UP6M5YjiM26jdLbUt6qj3OqrgzcJqOVy8UcpIVaxU9%2B3Xs189TNSuXS1y2GkKjkScLFvZW%2FxHeZ4HGNTYqPSGRvz2apIF3mXmv3yiLEdpIq8fA9NYYQ2IFexJuxg3KAiui3zvpGKBZFlG4O9DRC6NkrHd%2Bryo4a4yt1%2FYYj%2BSBbyJmSxJ1l9XajudRxnGDDD5vWIo0mCOcLLbvuyxPaEwt7qOvQY6pgGGwxlVe%2F96BwXryqaSuvpWK0CiIGJ3PsIlfcynUsG6axZrSwgIolbg7dXH1hDQf86xOiDr%2BLcXcvySVOf%2F3xBx71FKEDp57Ze%2F0bhzZcOqofQTGTe4aP5%2FgeXd25evKWKG%2BXIgzCQZCdX6ICtJCm5%2FsezubHxoGjLktWJwtElMCOGpgnQKI%2BOMcTJSAmTT0sHMvouMepVuvR4J3ybAbknBNw66zD5M&X-Amz-Signature=3eddb711e3c641578e7fe9c766e66d12511d355864334cbba0fe08c6ca98d64c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUEA2RYW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEbPILCh8lTG8U5NJenVx6iKcgkkqTMLqZk7DdV1vYqrAiA9PA3e97uTNeB9Y%2F1lIEgdq98eF%2BCl4PioPEiAFYi%2B8yr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsp8lcaeKHb6BthBdKtwDaGhcKP5APgiXcaHB0rMJUcKt7uatcmnvoKYxb%2B%2FrjkYsm8coO1xVPx4ZRUkv8ogzJ%2FtMy43RSS1BuaWCgMi2j%2FeYymLFpJcxQHNNsGntknxR0lqpOuPlFdD1eSVHRiR9hLfadMjkTRsmRC0MBxyM068%2FcwJA%2BvP3cMFi128nFC%2FAuZqjHBgn3IlXVP3lfDgj1wYPqAl%2F0JmlROCILiJ3cE8Vpoc3Yl%2FM9peLplL%2FxJH0lnDX%2FqEW0Q5Q5I%2Brh4XdR5DRP39t5wSz%2FQeK%2FtGRRpppTp11Elcg5N69LG%2BzrEXg8KdU63pH4ExQyDJgy6I%2Bm0ynqPisPvqxnx9gCqkhp2dnLYnCevWhNOrNeXxuekXc8kIhBS1QXmqyeEMqmg2kd0hzxzMKuqkuLzP7BL6GxSIw1fPhAAn8QHTOBp2UP6M5YjiM26jdLbUt6qj3OqrgzcJqOVy8UcpIVaxU9%2B3Xs189TNSuXS1y2GkKjkScLFvZW%2FxHeZ4HGNTYqPSGRvz2apIF3mXmv3yiLEdpIq8fA9NYYQ2IFexJuxg3KAiui3zvpGKBZFlG4O9DRC6NkrHd%2Bryo4a4yt1%2FYYj%2BSBbyJmSxJ1l9XajudRxnGDDD5vWIo0mCOcLLbvuyxPaEwt7qOvQY6pgGGwxlVe%2F96BwXryqaSuvpWK0CiIGJ3PsIlfcynUsG6axZrSwgIolbg7dXH1hDQf86xOiDr%2BLcXcvySVOf%2F3xBx71FKEDp57Ze%2F0bhzZcOqofQTGTe4aP5%2FgeXd25evKWKG%2BXIgzCQZCdX6ICtJCm5%2FsezubHxoGjLktWJwtElMCOGpgnQKI%2BOMcTJSAmTT0sHMvouMepVuvR4J3ybAbknBNw66zD5M&X-Amz-Signature=6e323de421ad0ea55c89cd22d31890950f144a2de539a7487a7a79b0cbce6090&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUEA2RYW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEbPILCh8lTG8U5NJenVx6iKcgkkqTMLqZk7DdV1vYqrAiA9PA3e97uTNeB9Y%2F1lIEgdq98eF%2BCl4PioPEiAFYi%2B8yr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsp8lcaeKHb6BthBdKtwDaGhcKP5APgiXcaHB0rMJUcKt7uatcmnvoKYxb%2B%2FrjkYsm8coO1xVPx4ZRUkv8ogzJ%2FtMy43RSS1BuaWCgMi2j%2FeYymLFpJcxQHNNsGntknxR0lqpOuPlFdD1eSVHRiR9hLfadMjkTRsmRC0MBxyM068%2FcwJA%2BvP3cMFi128nFC%2FAuZqjHBgn3IlXVP3lfDgj1wYPqAl%2F0JmlROCILiJ3cE8Vpoc3Yl%2FM9peLplL%2FxJH0lnDX%2FqEW0Q5Q5I%2Brh4XdR5DRP39t5wSz%2FQeK%2FtGRRpppTp11Elcg5N69LG%2BzrEXg8KdU63pH4ExQyDJgy6I%2Bm0ynqPisPvqxnx9gCqkhp2dnLYnCevWhNOrNeXxuekXc8kIhBS1QXmqyeEMqmg2kd0hzxzMKuqkuLzP7BL6GxSIw1fPhAAn8QHTOBp2UP6M5YjiM26jdLbUt6qj3OqrgzcJqOVy8UcpIVaxU9%2B3Xs189TNSuXS1y2GkKjkScLFvZW%2FxHeZ4HGNTYqPSGRvz2apIF3mXmv3yiLEdpIq8fA9NYYQ2IFexJuxg3KAiui3zvpGKBZFlG4O9DRC6NkrHd%2Bryo4a4yt1%2FYYj%2BSBbyJmSxJ1l9XajudRxnGDDD5vWIo0mCOcLLbvuyxPaEwt7qOvQY6pgGGwxlVe%2F96BwXryqaSuvpWK0CiIGJ3PsIlfcynUsG6axZrSwgIolbg7dXH1hDQf86xOiDr%2BLcXcvySVOf%2F3xBx71FKEDp57Ze%2F0bhzZcOqofQTGTe4aP5%2FgeXd25evKWKG%2BXIgzCQZCdX6ICtJCm5%2FsezubHxoGjLktWJwtElMCOGpgnQKI%2BOMcTJSAmTT0sHMvouMepVuvR4J3ybAbknBNw66zD5M&X-Amz-Signature=80d18e5590b720dcce8683d441669afd48918673377d512258c71fe1a279878f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUEA2RYW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEbPILCh8lTG8U5NJenVx6iKcgkkqTMLqZk7DdV1vYqrAiA9PA3e97uTNeB9Y%2F1lIEgdq98eF%2BCl4PioPEiAFYi%2B8yr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsp8lcaeKHb6BthBdKtwDaGhcKP5APgiXcaHB0rMJUcKt7uatcmnvoKYxb%2B%2FrjkYsm8coO1xVPx4ZRUkv8ogzJ%2FtMy43RSS1BuaWCgMi2j%2FeYymLFpJcxQHNNsGntknxR0lqpOuPlFdD1eSVHRiR9hLfadMjkTRsmRC0MBxyM068%2FcwJA%2BvP3cMFi128nFC%2FAuZqjHBgn3IlXVP3lfDgj1wYPqAl%2F0JmlROCILiJ3cE8Vpoc3Yl%2FM9peLplL%2FxJH0lnDX%2FqEW0Q5Q5I%2Brh4XdR5DRP39t5wSz%2FQeK%2FtGRRpppTp11Elcg5N69LG%2BzrEXg8KdU63pH4ExQyDJgy6I%2Bm0ynqPisPvqxnx9gCqkhp2dnLYnCevWhNOrNeXxuekXc8kIhBS1QXmqyeEMqmg2kd0hzxzMKuqkuLzP7BL6GxSIw1fPhAAn8QHTOBp2UP6M5YjiM26jdLbUt6qj3OqrgzcJqOVy8UcpIVaxU9%2B3Xs189TNSuXS1y2GkKjkScLFvZW%2FxHeZ4HGNTYqPSGRvz2apIF3mXmv3yiLEdpIq8fA9NYYQ2IFexJuxg3KAiui3zvpGKBZFlG4O9DRC6NkrHd%2Bryo4a4yt1%2FYYj%2BSBbyJmSxJ1l9XajudRxnGDDD5vWIo0mCOcLLbvuyxPaEwt7qOvQY6pgGGwxlVe%2F96BwXryqaSuvpWK0CiIGJ3PsIlfcynUsG6axZrSwgIolbg7dXH1hDQf86xOiDr%2BLcXcvySVOf%2F3xBx71FKEDp57Ze%2F0bhzZcOqofQTGTe4aP5%2FgeXd25evKWKG%2BXIgzCQZCdX6ICtJCm5%2FsezubHxoGjLktWJwtElMCOGpgnQKI%2BOMcTJSAmTT0sHMvouMepVuvR4J3ybAbknBNw66zD5M&X-Amz-Signature=2417de2939ba34d9a016af6dc68a720e5e6030ab67161b73be6b607d9f05f5e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUEA2RYW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEbPILCh8lTG8U5NJenVx6iKcgkkqTMLqZk7DdV1vYqrAiA9PA3e97uTNeB9Y%2F1lIEgdq98eF%2BCl4PioPEiAFYi%2B8yr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsp8lcaeKHb6BthBdKtwDaGhcKP5APgiXcaHB0rMJUcKt7uatcmnvoKYxb%2B%2FrjkYsm8coO1xVPx4ZRUkv8ogzJ%2FtMy43RSS1BuaWCgMi2j%2FeYymLFpJcxQHNNsGntknxR0lqpOuPlFdD1eSVHRiR9hLfadMjkTRsmRC0MBxyM068%2FcwJA%2BvP3cMFi128nFC%2FAuZqjHBgn3IlXVP3lfDgj1wYPqAl%2F0JmlROCILiJ3cE8Vpoc3Yl%2FM9peLplL%2FxJH0lnDX%2FqEW0Q5Q5I%2Brh4XdR5DRP39t5wSz%2FQeK%2FtGRRpppTp11Elcg5N69LG%2BzrEXg8KdU63pH4ExQyDJgy6I%2Bm0ynqPisPvqxnx9gCqkhp2dnLYnCevWhNOrNeXxuekXc8kIhBS1QXmqyeEMqmg2kd0hzxzMKuqkuLzP7BL6GxSIw1fPhAAn8QHTOBp2UP6M5YjiM26jdLbUt6qj3OqrgzcJqOVy8UcpIVaxU9%2B3Xs189TNSuXS1y2GkKjkScLFvZW%2FxHeZ4HGNTYqPSGRvz2apIF3mXmv3yiLEdpIq8fA9NYYQ2IFexJuxg3KAiui3zvpGKBZFlG4O9DRC6NkrHd%2Bryo4a4yt1%2FYYj%2BSBbyJmSxJ1l9XajudRxnGDDD5vWIo0mCOcLLbvuyxPaEwt7qOvQY6pgGGwxlVe%2F96BwXryqaSuvpWK0CiIGJ3PsIlfcynUsG6axZrSwgIolbg7dXH1hDQf86xOiDr%2BLcXcvySVOf%2F3xBx71FKEDp57Ze%2F0bhzZcOqofQTGTe4aP5%2FgeXd25evKWKG%2BXIgzCQZCdX6ICtJCm5%2FsezubHxoGjLktWJwtElMCOGpgnQKI%2BOMcTJSAmTT0sHMvouMepVuvR4J3ybAbknBNw66zD5M&X-Amz-Signature=59d7a4bf8029e11f4d5740d310f401779b075771c929370e0190905f901d528e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUEA2RYW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEbPILCh8lTG8U5NJenVx6iKcgkkqTMLqZk7DdV1vYqrAiA9PA3e97uTNeB9Y%2F1lIEgdq98eF%2BCl4PioPEiAFYi%2B8yr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsp8lcaeKHb6BthBdKtwDaGhcKP5APgiXcaHB0rMJUcKt7uatcmnvoKYxb%2B%2FrjkYsm8coO1xVPx4ZRUkv8ogzJ%2FtMy43RSS1BuaWCgMi2j%2FeYymLFpJcxQHNNsGntknxR0lqpOuPlFdD1eSVHRiR9hLfadMjkTRsmRC0MBxyM068%2FcwJA%2BvP3cMFi128nFC%2FAuZqjHBgn3IlXVP3lfDgj1wYPqAl%2F0JmlROCILiJ3cE8Vpoc3Yl%2FM9peLplL%2FxJH0lnDX%2FqEW0Q5Q5I%2Brh4XdR5DRP39t5wSz%2FQeK%2FtGRRpppTp11Elcg5N69LG%2BzrEXg8KdU63pH4ExQyDJgy6I%2Bm0ynqPisPvqxnx9gCqkhp2dnLYnCevWhNOrNeXxuekXc8kIhBS1QXmqyeEMqmg2kd0hzxzMKuqkuLzP7BL6GxSIw1fPhAAn8QHTOBp2UP6M5YjiM26jdLbUt6qj3OqrgzcJqOVy8UcpIVaxU9%2B3Xs189TNSuXS1y2GkKjkScLFvZW%2FxHeZ4HGNTYqPSGRvz2apIF3mXmv3yiLEdpIq8fA9NYYQ2IFexJuxg3KAiui3zvpGKBZFlG4O9DRC6NkrHd%2Bryo4a4yt1%2FYYj%2BSBbyJmSxJ1l9XajudRxnGDDD5vWIo0mCOcLLbvuyxPaEwt7qOvQY6pgGGwxlVe%2F96BwXryqaSuvpWK0CiIGJ3PsIlfcynUsG6axZrSwgIolbg7dXH1hDQf86xOiDr%2BLcXcvySVOf%2F3xBx71FKEDp57Ze%2F0bhzZcOqofQTGTe4aP5%2FgeXd25evKWKG%2BXIgzCQZCdX6ICtJCm5%2FsezubHxoGjLktWJwtElMCOGpgnQKI%2BOMcTJSAmTT0sHMvouMepVuvR4J3ybAbknBNw66zD5M&X-Amz-Signature=84f86be5754dd63c50c64603cb60afcf3a56cdb36fd3140dca26eaf4b822bbad&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624PUDZSM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIEgUeCCTohN8E8kCAh5dE4qDBUXWh2ie0gkt5AfvAX4kAiBSJ%2FuE6El6bqrwXMINmqPOF03aI9pjwP2HCUV0%2FQWOUir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMkyA9gdavgSYN5c8gKtwDVWJpbtOmWJqzsFkg53VEWzb4udgL5HwNgFjjR%2Baep%2F00M8ojun6zrqzZQkg6FKADYVifsnkZ8YnA%2Bvs6YLmDmGiuZ%2FmmavhIaoYJWuUs2dd2BK1toQgMK%2FB0xuRVX7GPMAIVBVkrhZ6mLWyt4S2Ifin0PvNrhYnBKMtuc4p%2FJ46FdeDACo1SioKHNm%2FBYnpporXbquBygaHwSZrW%2B29Fe4Z1Mf2VCLK7P%2BoDEKhK3gou7FEGczFxfBRypXa24J%2FGGt1zJMfkIUWPcmzjTdRMmKoZhRRAyH2BVhCnnahUenHN8EqglDoD%2Brs%2B4T3iVf5oVoHNNBTyaEnT%2FRWnO0BEStr9tW1Vy6rZicG7dql%2FYNjQCBXHKqadRwdicHG%2FLGsjaC5bXHiLfP6P%2FKKtU5gcMSN7eGV%2BH6S3i9ABRWeMOO34hUZK%2FaH2LM1rKbg06myX3dJU%2BL5Lb3hKzUU7WTNW%2BVa%2FL02AL8VsWSxvw70w%2B6bO3nQc5evTEkgvCbYVfzGI6jB5j3ivwKWfV9eF71Ni0UAA7fDhXYvvZT7EhVolyVOhP1eoVmwNQZaM7jg1dqO9Ud2f28fBdy2rFA5o5RmpZv8NllZdPqRY9zuPQ%2Ftm%2Bj8tsfNDA0XUMLJrz6QwrLuOvQY6pgErtKQstQENTPLkhXMLcYaZPA9Kn93TJbYiuCYbQffqqOYRacdrmqIqEFz35lTXgvP05Wfnt57bfUR8iUGaGWiad66kiS%2Fw9SbtgySEpYX0%2Be1wJkLkLLCCMHSR8TK7LY8uPkIJVaCRJNqEAdBa3hmFcshfB5bBFUnyRj1yNm93Is4utaJMGelNzuZgIOPSBkD60RRiZYm9De9b%2BROKr%2B%2BLTF8QO6N1&X-Amz-Signature=0dc2eca1d1cca513e2ec6b30b715bfd1f754dbb665a96316e0e0204b8b4e1748&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPWNR4WB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDKt8xJzHIIG%2BQJchWntLagXDhfoJ%2FoAQ5aDoENXx76EQIgCwnag1PSeEaiekDkKyLsK%2F3WDw1SQzSi6%2B5i0phUeyMq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDEhTFQjPn0Aqr78sXyrcA%2Bx8au7RZ3BR%2FsEN4G%2FvRZptBzMfbGwK7XSzxsjMWmgjNgSskL%2FJgU%2BpnHHsuv9mzUdFx2JYzjKaE03MRQHyLljdUKv7Gx3XbQpt5J5AFEVx91gR4jR3EFpPrPrG0%2FTrrSSA%2F5LQ9Cl2a1j4Q2YfRScZVBBmfTnP%2FewK0XUCZB18AM3ZyL1ntM1c4ymbqJaBn6SwFwt%2B3YwLYaVLjQMnSsEr6Q6bXcvQBPeklNNwUiOYcJ2WAqkDs463rUKkoiLhSfdffsu1Oz97n5uO27n14UXcuqTJQiX0nhWRxebZq1idowF0HXO0JoQkhYIurS%2Btd%2Bc2lwg2xmh%2FzMNaw7NtozC%2BkE2roih4DuUY0cHLkbLdM5FXEGJGjsTh5AhabJCRG%2FRm%2BR1IpF5qBFWhG1UMYaOd55Q2fN5qj8jQXeDV%2F3N3tpEGgzVTirJ%2Fc2ujhiKUJ3f7ITBvXYWnCQVZe3b82wNYgaEMsoQfL4pHu3GFVfG%2FBMmuo0KE7iOWwYlb%2BXlCHOJtH8rvyj6oxfWZHlRW%2FkluqhJxtRs2bTVIPjXAdUuSyEGSoplmA8JGSs00YoukIbB9JpCKQoaqCob7vekvkiBYCTYY6lmN65nKjjjMcInNOVhmMQ8vMP3ceqnMMNC6jr0GOqUBpwhhjOZBCC2PYuHnyKOnuyujAVpTooZRN7vVwc%2FzRgsbcaaI0EacYtjDZC8aSV7mUbzw9y2D3SeWUKeXMNxbsyOJGWVJXsCCP1U%2Bs11eUWma2oA5Y0YAk22bKu0biM58fTrQOZsN4G06qwL0fp56vt05sMKvPeUVjIg%2F9T52Gb7GYFflQbDBA9QjLGO1p1DKcuuIYB%2FsT%2BsTEoCWh06YvHwc70Gk&X-Amz-Signature=ab4aefd4cf663b666cf699faf4e1be77a734d155b24b91b91fa51e69d4eae519&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUEA2RYW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEbPILCh8lTG8U5NJenVx6iKcgkkqTMLqZk7DdV1vYqrAiA9PA3e97uTNeB9Y%2F1lIEgdq98eF%2BCl4PioPEiAFYi%2B8yr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsp8lcaeKHb6BthBdKtwDaGhcKP5APgiXcaHB0rMJUcKt7uatcmnvoKYxb%2B%2FrjkYsm8coO1xVPx4ZRUkv8ogzJ%2FtMy43RSS1BuaWCgMi2j%2FeYymLFpJcxQHNNsGntknxR0lqpOuPlFdD1eSVHRiR9hLfadMjkTRsmRC0MBxyM068%2FcwJA%2BvP3cMFi128nFC%2FAuZqjHBgn3IlXVP3lfDgj1wYPqAl%2F0JmlROCILiJ3cE8Vpoc3Yl%2FM9peLplL%2FxJH0lnDX%2FqEW0Q5Q5I%2Brh4XdR5DRP39t5wSz%2FQeK%2FtGRRpppTp11Elcg5N69LG%2BzrEXg8KdU63pH4ExQyDJgy6I%2Bm0ynqPisPvqxnx9gCqkhp2dnLYnCevWhNOrNeXxuekXc8kIhBS1QXmqyeEMqmg2kd0hzxzMKuqkuLzP7BL6GxSIw1fPhAAn8QHTOBp2UP6M5YjiM26jdLbUt6qj3OqrgzcJqOVy8UcpIVaxU9%2B3Xs189TNSuXS1y2GkKjkScLFvZW%2FxHeZ4HGNTYqPSGRvz2apIF3mXmv3yiLEdpIq8fA9NYYQ2IFexJuxg3KAiui3zvpGKBZFlG4O9DRC6NkrHd%2Bryo4a4yt1%2FYYj%2BSBbyJmSxJ1l9XajudRxnGDDD5vWIo0mCOcLLbvuyxPaEwt7qOvQY6pgGGwxlVe%2F96BwXryqaSuvpWK0CiIGJ3PsIlfcynUsG6axZrSwgIolbg7dXH1hDQf86xOiDr%2BLcXcvySVOf%2F3xBx71FKEDp57Ze%2F0bhzZcOqofQTGTe4aP5%2FgeXd25evKWKG%2BXIgzCQZCdX6ICtJCm5%2FsezubHxoGjLktWJwtElMCOGpgnQKI%2BOMcTJSAmTT0sHMvouMepVuvR4J3ybAbknBNw66zD5M&X-Amz-Signature=84a34ceddf52b967d4f58179186f9dc2b38e05b53fee1edec9fe1b8390215c76&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUEA2RYW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEbPILCh8lTG8U5NJenVx6iKcgkkqTMLqZk7DdV1vYqrAiA9PA3e97uTNeB9Y%2F1lIEgdq98eF%2BCl4PioPEiAFYi%2B8yr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsp8lcaeKHb6BthBdKtwDaGhcKP5APgiXcaHB0rMJUcKt7uatcmnvoKYxb%2B%2FrjkYsm8coO1xVPx4ZRUkv8ogzJ%2FtMy43RSS1BuaWCgMi2j%2FeYymLFpJcxQHNNsGntknxR0lqpOuPlFdD1eSVHRiR9hLfadMjkTRsmRC0MBxyM068%2FcwJA%2BvP3cMFi128nFC%2FAuZqjHBgn3IlXVP3lfDgj1wYPqAl%2F0JmlROCILiJ3cE8Vpoc3Yl%2FM9peLplL%2FxJH0lnDX%2FqEW0Q5Q5I%2Brh4XdR5DRP39t5wSz%2FQeK%2FtGRRpppTp11Elcg5N69LG%2BzrEXg8KdU63pH4ExQyDJgy6I%2Bm0ynqPisPvqxnx9gCqkhp2dnLYnCevWhNOrNeXxuekXc8kIhBS1QXmqyeEMqmg2kd0hzxzMKuqkuLzP7BL6GxSIw1fPhAAn8QHTOBp2UP6M5YjiM26jdLbUt6qj3OqrgzcJqOVy8UcpIVaxU9%2B3Xs189TNSuXS1y2GkKjkScLFvZW%2FxHeZ4HGNTYqPSGRvz2apIF3mXmv3yiLEdpIq8fA9NYYQ2IFexJuxg3KAiui3zvpGKBZFlG4O9DRC6NkrHd%2Bryo4a4yt1%2FYYj%2BSBbyJmSxJ1l9XajudRxnGDDD5vWIo0mCOcLLbvuyxPaEwt7qOvQY6pgGGwxlVe%2F96BwXryqaSuvpWK0CiIGJ3PsIlfcynUsG6axZrSwgIolbg7dXH1hDQf86xOiDr%2BLcXcvySVOf%2F3xBx71FKEDp57Ze%2F0bhzZcOqofQTGTe4aP5%2FgeXd25evKWKG%2BXIgzCQZCdX6ICtJCm5%2FsezubHxoGjLktWJwtElMCOGpgnQKI%2BOMcTJSAmTT0sHMvouMepVuvR4J3ybAbknBNw66zD5M&X-Amz-Signature=91d74e339a6e146ade53256d69b7e783199d0065c40f3e116741b03cfd0115f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUEA2RYW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEbPILCh8lTG8U5NJenVx6iKcgkkqTMLqZk7DdV1vYqrAiA9PA3e97uTNeB9Y%2F1lIEgdq98eF%2BCl4PioPEiAFYi%2B8yr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMsp8lcaeKHb6BthBdKtwDaGhcKP5APgiXcaHB0rMJUcKt7uatcmnvoKYxb%2B%2FrjkYsm8coO1xVPx4ZRUkv8ogzJ%2FtMy43RSS1BuaWCgMi2j%2FeYymLFpJcxQHNNsGntknxR0lqpOuPlFdD1eSVHRiR9hLfadMjkTRsmRC0MBxyM068%2FcwJA%2BvP3cMFi128nFC%2FAuZqjHBgn3IlXVP3lfDgj1wYPqAl%2F0JmlROCILiJ3cE8Vpoc3Yl%2FM9peLplL%2FxJH0lnDX%2FqEW0Q5Q5I%2Brh4XdR5DRP39t5wSz%2FQeK%2FtGRRpppTp11Elcg5N69LG%2BzrEXg8KdU63pH4ExQyDJgy6I%2Bm0ynqPisPvqxnx9gCqkhp2dnLYnCevWhNOrNeXxuekXc8kIhBS1QXmqyeEMqmg2kd0hzxzMKuqkuLzP7BL6GxSIw1fPhAAn8QHTOBp2UP6M5YjiM26jdLbUt6qj3OqrgzcJqOVy8UcpIVaxU9%2B3Xs189TNSuXS1y2GkKjkScLFvZW%2FxHeZ4HGNTYqPSGRvz2apIF3mXmv3yiLEdpIq8fA9NYYQ2IFexJuxg3KAiui3zvpGKBZFlG4O9DRC6NkrHd%2Bryo4a4yt1%2FYYj%2BSBbyJmSxJ1l9XajudRxnGDDD5vWIo0mCOcLLbvuyxPaEwt7qOvQY6pgGGwxlVe%2F96BwXryqaSuvpWK0CiIGJ3PsIlfcynUsG6axZrSwgIolbg7dXH1hDQf86xOiDr%2BLcXcvySVOf%2F3xBx71FKEDp57Ze%2F0bhzZcOqofQTGTe4aP5%2FgeXd25evKWKG%2BXIgzCQZCdX6ICtJCm5%2FsezubHxoGjLktWJwtElMCOGpgnQKI%2BOMcTJSAmTT0sHMvouMepVuvR4J3ybAbknBNw66zD5M&X-Amz-Signature=0de5250006aac70b6f42580a398c736cfe967a398e2fbfe03eadd3e8ff9f1514&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVFFARDX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGmaANu82AwIePiQPNjHSeYBrAGFN%2FSuiswHLdT2yZ8RAiEA4HZfNhJ82KwDK9briNiGOE%2FTYdYS9zkUTX93rrKK5SQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDCL4J%2BetshfutpAjzCrcA4c8ueDtsxNqFHdIOLxl3%2B1S0QhMoEMa4fne4%2FS6PE0vWpJMeYBJQoZZagp5Sa75Nvs9dBEmh58yUutlAbRzHlFHQInKujgBIDp6UsTXUFnjn%2F3FHqh7FMLiMQW6CvOgtB%2F0iURxLnWeEmXMTAPeesdellqSEHRRj20WcD07gXEKO%2Bnu1UwulQTtpp%2BLihxa%2BvyHsFLJKCa1%2FTItAOIiIMS5RB8Xq3t%2BpDRWlsMhBfLTDsHWu8y8Phr%2FKe3eh6mslGrkpHwMILYLOlNnX%2BqYfSxTNQjO0WOUc7OC0SH1SQaPnwXy998BtrbhJcDHY2wcrH%2FhwGRcZu%2BeNYknyQoCE%2BURhH0Q8JteE0DSjSFlgproeMtXWJEApv6rrXtEuadCs8cMgRjyVP%2BEgv4FUE33m49uOWUGGI8nk4ovWn%2FahqZ3xr%2BYWv1dtjtJWiEIKeIJjqW%2FZcxcCnc2fLYo%2B9gI5dev%2FBvSy4YoB532HNH6cSRlpdQ6T1mx556l0sosCCesKP3bzsZXBJkyoHsZtE9EnyZMJ5jY7qvHt7p2w%2F39ZXozJwb6a0yEym13YM6Q2wmNE9vnayR08LegDWORgrRMkra9YGtXIdZWvCiz0R5WlAVsZ9HGSzRqK1We97%2BOMMG6jr0GOqUBh%2FSwiyGaC%2Bt%2F7MpoWHLpIrmGbh7sV%2BBTD%2BHR12T5tNOCRdje%2FeqpMVOFZOscL5FhiurIPGOQUpQEhcrSG1dHspR6BCrlhmR%2BfvRh5YsYGF9cBrlAkq4qWLiqQVTQLhLAV7RjDstbmACgDpU2AfC0j7zWuIsuCv2qWd5e4%2B%2Fg8vNv6rZKZjOzWm%2FPzcujEAlP5UWEXGH2ux6OEFROfpqE%2BfjCY86g&X-Amz-Signature=788003c10231ab021749707461d0b43230fd2f1e50866f3a63ff001196e05a6b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVXMRN4G%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCI12oj6N6UTvkDD8m7%2FYV7XgUbuLYS1G5DaSX43X1X9gIgff%2BdZHxfp1OCsUvFp3h%2FsT4x8u7eew3gSZ1VMhV3LrQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJlFWQdnP1aFnyhh8yrcA3AGmwU7wZ3hZc0ggVQxktXh%2Fjib8MK2UkNCYK51qPpNIXkBd%2F8WFUkggNzFk0zshkJEU1nkLplK7G0F%2F9Tlu55JwgxsQtN6tXR7PFXe5tIUJWKgRmw90kvWwJje0w1kvBrMfTyPpaGsPd3pTxr%2BnQIwmltc0YXz8bdHiV12DeXg62NMkLyb%2B2r7IbNJRmQ7G6J2X9njN9R88IwxfBbwaWEbGMu4wbZu%2BmbaIj5gmQt%2BZzRctUR9fAUBe66JkkFiPy3DlAbHhqPLtp7MrfJXq65aOBJpXXNB2SnYaU5B56oP0zNQZz4wgQ%2FI1XO62YkL%2BbJ%2FCf6L4hTvcdqkYj9mOMR4iDcxZeQbGU3ZOs7bBBAwlc0ASQ1CW%2BMrAlKSxH4H7na9bqnJvOHNJA7e%2BcvWWM%2BEZZmWflnGeilLpSv%2FKR2FTcAn7O%2BwbxUBWCb11hooeyB0G4Bk6ag2x92moo7cqtFMWIGetxPhw25VwMQkFqviRB9uqGfec9CmE1hPBwpoqvT5XfeIF6jNtGGl5SZGN55Og3tcsQcWrof%2BjJgzfqov2x%2FxxjmXA0pRhL%2FjiUfIWCYnGKvMYjN082jE%2F1h%2FS5BRhVBU%2F4DCzIQ0L8z9p%2B%2BFy0GSL4wRcBPJ%2BIesMMW6jr0GOqUBNquIaWyvI2NjtybSGKPQSWHoARrfRTkcokgtdvqIOZZUSRVrjXNTyXYp%2B7QWopmtTNto4SLD4Am9jhoQcalz8xGTL0u%2BR6UU07ROO6i%2BnWgaJ1Tgj%2BIBgUtcZ0PgMDiqh5rnANkPbXppnP2ijObETg7md9qFR0c32PB3KXGqloOoqn8L0O0%2BAwKiSb%2FeDGzQCQoByU1kCOhXb6tMIuspZmLy%2BWgC&X-Amz-Signature=b4087edad13f2ddb71ad7d00524da5799dd39404193b149cb5988878c260c53c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRDQKJOD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHAij%2FdnqMJNEJJpHwDFBhIwyfM3YGBpvehujNf5FmK%2FAiEAuViNnYVauEsTzYfcwYInyY%2BNRPt4zgJfYWLijU6HDcoq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDH3MnbyuGAvm55tLXyrcA%2F6yrFBtjA6GHuSjlpywt8G1hRubQ%2B4zKbhLmgZ3RTTbuWjxR6%2BQ%2FkKS9JbRFo9aDkgqbJBcwRnGNSXjxuDm%2FzgnrCG9k3Gka%2BAQ4eRjngu7M2j3OYp66IvOPNMpHuEhM3WXFLLGw2PpS0j38PbnSDJgIhzKj87QIrU2yMTx8VTpF3nEe%2BVf8dqjLf%2BWfvjp1juEsAv2rWmGjdwilsJd8Vb2gMMxv39vj58fkp8nLyLASqAudc2hAe3f3NXNrEoctJefS6pbE4dGPDdG6maRmvcljrBh%2FBUqsWrrAj%2F2fpWYJnwcRB38Quv2gzjIwqNfQMd8vC%2FvdtOCsYjYXjMsaifbzSouNhlvipHRg%2BhcbscW6jzFI%2B8mA%2BR2XHKgHvKYlgxW5ZNUzZ9ECNVP%2B5qcBo60uaxNV73zj%2FYm7aQQw11kggGC%2FBVxum1AAnOStcT%2FrCj4W5YKKTfR9Mck4Jl3ZLyFJY9tkklroOsnqKAtCtUaDD047%2FR8LEwD%2BS%2FQdJtcyMDqd%2F9isuRXKBuGNGxxsuDtp2U2BFGuh6s6XPRQVGMfSlA5CVzXk9LnRPxhfh5mhYKywZxw%2BGpKsDSM6cqCILbxYnjc5hKb3EYnb7e23AsDN5WCbodTO0Xct7HkMJ27jr0GOqUBDRMrykea0vDiFI6lCj%2F6S9b%2FsWX0YG%2Ft9swjW%2FtimwChLLyqiXy7XhSi4WGkZJO%2FFRR9hAjvYCzhYBwtsU5mk5bX%2BEGJs9FuaPRldTrt3p0AK12lLvlTfmUjwRM%2BBex6%2FWzwm1lrYH73nBeG2xHwo9sDKjgn3APRSRlkFeb%2FNFCiyn2txJea0zAuJmG%2FHzpgJh743xS9r9QVSbgrTN840SqPr3Mi&X-Amz-Signature=b3849f434d2162111a1ee17ba279614bcfbe0a28c26f24fdf7b406279ee029c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2ECVCGB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDCWc%2F8vcOBfChBq2Q0RyHPBIrLeC6DbDOFhhHFqJrfFwIhAKRWZbUP2zlTAh6s4VABn9CHTnnjl%2BfEDpxSC7HYeD7LKv8DCEoQABoMNjM3NDIzMTgzODA1Igykq5Tpk2%2FK%2BM16vIkq3APZMH%2BYoxtdsOm40VY5vna9X9QeNKqRf6e1VwfAlA9PKC7icA3Er96Utw%2FpeYT1NGQHwqlJMAIZxBVkV1Z1s4euYXrVPfc%2Frmx2DzV1ndP1wF05zfq6gdTyhRtYoirVwC%2Fxbt%2FkrzAxAONl9pfR5fu%2FdXBLpFPynAWGzD%2BMezHIDo5DomZ%2Fnw6T97QzHItKWRC3LjxwqdNlS8CkqrVw3VzqIzBHfS93ZxYLDm9cnUONQU8YBB9RRN7QE3M2VHNsPioPAZBhbBN7o9No1T1foE9Wer8obdnNWcMBe5VYAIoeGM7HPsrQ6xq6UKcodrYxS62uiisWQUFcuinaF2Q1GvrK7Q9IF1c7P2XcjHUP2R1FnERVXIAdn6Oucdx51NwkfF58Lk1tNh4OQw4RIsTDqoymbqHE9aDUSZdi9rMbLyuU5QmDKTfxxZnecKPGVJNDFTpwbbvfReAdu0YBfm6F%2BliGN%2BWrENAacUsGnKxG5AM%2BJkDZGagKPQa5qaoUsHcP9UIwG7nALjigWzS0RIPVBrdIp9RGkR9MkUkhJtDV0ZThjB86paTFTXTyhElgFKngzn51v%2BMNHFjJq%2F7ubIfoVFkMsP%2FTsBcyqiJXul7y2wLTO1efwLt0io0THMjHGjDIuo69BjqkATAPKbVxUk6rstCMzrtTN34vIBC9kLHyDPtg%2BZE0xH9azmWl64%2FmM0ZakWUU7n0MnQ6W1TSbpi7PZoH1V9DXJhgvN4HdjqmEMZFJf%2FFKaOy3iDCQbkSI%2Fo%2FfDw5L%2Blwy37wzU4gXLrL3nvjQ2CU%2BkreKWXeQamyjALgLUNCT2dE9Xt1aKn0Z6a2qbnPn5RbybWCmdy4HJbe9UOVC2FUOAOk%2B7cgF&X-Amz-Signature=5a790bcd1d3a19f811ca4ba789af9a06c4905df9a03f31608b08b9faa67c8714&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2ECVCGB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDCWc%2F8vcOBfChBq2Q0RyHPBIrLeC6DbDOFhhHFqJrfFwIhAKRWZbUP2zlTAh6s4VABn9CHTnnjl%2BfEDpxSC7HYeD7LKv8DCEoQABoMNjM3NDIzMTgzODA1Igykq5Tpk2%2FK%2BM16vIkq3APZMH%2BYoxtdsOm40VY5vna9X9QeNKqRf6e1VwfAlA9PKC7icA3Er96Utw%2FpeYT1NGQHwqlJMAIZxBVkV1Z1s4euYXrVPfc%2Frmx2DzV1ndP1wF05zfq6gdTyhRtYoirVwC%2Fxbt%2FkrzAxAONl9pfR5fu%2FdXBLpFPynAWGzD%2BMezHIDo5DomZ%2Fnw6T97QzHItKWRC3LjxwqdNlS8CkqrVw3VzqIzBHfS93ZxYLDm9cnUONQU8YBB9RRN7QE3M2VHNsPioPAZBhbBN7o9No1T1foE9Wer8obdnNWcMBe5VYAIoeGM7HPsrQ6xq6UKcodrYxS62uiisWQUFcuinaF2Q1GvrK7Q9IF1c7P2XcjHUP2R1FnERVXIAdn6Oucdx51NwkfF58Lk1tNh4OQw4RIsTDqoymbqHE9aDUSZdi9rMbLyuU5QmDKTfxxZnecKPGVJNDFTpwbbvfReAdu0YBfm6F%2BliGN%2BWrENAacUsGnKxG5AM%2BJkDZGagKPQa5qaoUsHcP9UIwG7nALjigWzS0RIPVBrdIp9RGkR9MkUkhJtDV0ZThjB86paTFTXTyhElgFKngzn51v%2BMNHFjJq%2F7ubIfoVFkMsP%2FTsBcyqiJXul7y2wLTO1efwLt0io0THMjHGjDIuo69BjqkATAPKbVxUk6rstCMzrtTN34vIBC9kLHyDPtg%2BZE0xH9azmWl64%2FmM0ZakWUU7n0MnQ6W1TSbpi7PZoH1V9DXJhgvN4HdjqmEMZFJf%2FFKaOy3iDCQbkSI%2Fo%2FfDw5L%2Blwy37wzU4gXLrL3nvjQ2CU%2BkreKWXeQamyjALgLUNCT2dE9Xt1aKn0Z6a2qbnPn5RbybWCmdy4HJbe9UOVC2FUOAOk%2B7cgF&X-Amz-Signature=d49f96b0da69ced0bd817684af9993772ce0918639ef907fffdef19accda96d5&X-Amz-SignedHeaders=host&x-id=GetObject)

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
