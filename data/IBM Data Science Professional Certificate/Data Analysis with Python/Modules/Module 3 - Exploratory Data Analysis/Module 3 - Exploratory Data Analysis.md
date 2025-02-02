

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAZWGTJ6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBvE%2F366gqAhQt9IDa36CEQn1QRd65MoeI7gzqV%2Bp5F0AiAjgjSMq9gEKLaY6mxyHLqtajfn0tAAAB3b%2BP9gojYLmCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRpjyh9kvMuk1hqtuKtwDtSekRGkZFXQJuFPBxd%2F0Hz5pKWbDkbMCPU5oe0vA3l43pNwDceEhcCKPwcqszcsiWoyFgmd361sPIiRndiiKdgdS22Geo4Ov14EODiAJYnUyl7z7YUt%2BicPlSMeu00ngjHI2NAKthzr5fnvmMRCo6jtxDdg8KKBTBQ2D5A2id1Mw3Uii088yt1XXgKqFMe3X%2FMakDjhSn5B%2B%2BjCpB9%2FDVSBtmUe5FFwBvARsGbPV6IxIHcj%2F8IcU6QCi9dCyF49LBZhzw%2FupKWTgvKSY8Zdip4YOpu6hFxBQ%2FWuGVYi6DpqJ4qwdP65irU8GWM2HkejYaTDHN7Bivh2hIX43ReBCK%2BEVVfbp0e0UTWYo6xFH7dWf0AtrgXjpGsi40NVRmZCtTODHIm1JsyPAD3tI5FUzMO9kZeAff%2FTiC4teyY6m9liztkNhRmEelcLGxcV60eE4NOG7I00ffpGoM0oxWioHM54CxrOfmvg4jJOIEFjxDMM2Av2Tu2PZBF%2Br9r7sLPqXjrmqcd2wDR6yCjSt7fPAl2BqlT6BnskhECa4HgxpsnGaiPlKj3k26On7yhCcLs2hfRoLYrlAsiQYd3xoyaWGdEXk1Kf5dfts4rvYklbYxqlXnW1W3b6AkPU71fswtOD%2BvAY6pgFwEWz4qyrfsbnROZpIyWHBXgFqXFepZEEUmL%2Bc8OLKu60RtiAHv3g2V3%2BEctOg2bXKDmxKmLGOyQJSunieQwNUemXMimxbNmx5XxOie0vgBmKRA81wUD67mvqB0%2F%2BTELW2IBa67g0Q420JVYcVcda2y8hHKV2iB2qm1sE0m1mIPX2yov2Xl1%2BDO3pQ9yusgpFZiIw%2ByqQ6RyyF79wwCk%2FXHE5wbDm0&X-Amz-Signature=6c3724e65442ef92536e1e71bcd31b6eb7f735b495924a1b8b1cdb4dc3358a56&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAZWGTJ6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBvE%2F366gqAhQt9IDa36CEQn1QRd65MoeI7gzqV%2Bp5F0AiAjgjSMq9gEKLaY6mxyHLqtajfn0tAAAB3b%2BP9gojYLmCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRpjyh9kvMuk1hqtuKtwDtSekRGkZFXQJuFPBxd%2F0Hz5pKWbDkbMCPU5oe0vA3l43pNwDceEhcCKPwcqszcsiWoyFgmd361sPIiRndiiKdgdS22Geo4Ov14EODiAJYnUyl7z7YUt%2BicPlSMeu00ngjHI2NAKthzr5fnvmMRCo6jtxDdg8KKBTBQ2D5A2id1Mw3Uii088yt1XXgKqFMe3X%2FMakDjhSn5B%2B%2BjCpB9%2FDVSBtmUe5FFwBvARsGbPV6IxIHcj%2F8IcU6QCi9dCyF49LBZhzw%2FupKWTgvKSY8Zdip4YOpu6hFxBQ%2FWuGVYi6DpqJ4qwdP65irU8GWM2HkejYaTDHN7Bivh2hIX43ReBCK%2BEVVfbp0e0UTWYo6xFH7dWf0AtrgXjpGsi40NVRmZCtTODHIm1JsyPAD3tI5FUzMO9kZeAff%2FTiC4teyY6m9liztkNhRmEelcLGxcV60eE4NOG7I00ffpGoM0oxWioHM54CxrOfmvg4jJOIEFjxDMM2Av2Tu2PZBF%2Br9r7sLPqXjrmqcd2wDR6yCjSt7fPAl2BqlT6BnskhECa4HgxpsnGaiPlKj3k26On7yhCcLs2hfRoLYrlAsiQYd3xoyaWGdEXk1Kf5dfts4rvYklbYxqlXnW1W3b6AkPU71fswtOD%2BvAY6pgFwEWz4qyrfsbnROZpIyWHBXgFqXFepZEEUmL%2Bc8OLKu60RtiAHv3g2V3%2BEctOg2bXKDmxKmLGOyQJSunieQwNUemXMimxbNmx5XxOie0vgBmKRA81wUD67mvqB0%2F%2BTELW2IBa67g0Q420JVYcVcda2y8hHKV2iB2qm1sE0m1mIPX2yov2Xl1%2BDO3pQ9yusgpFZiIw%2ByqQ6RyyF79wwCk%2FXHE5wbDm0&X-Amz-Signature=165e6c90fb58f90e0ae5d525c480fd6c57a9e32d2a5c8458c4469fdb0dc003c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAZWGTJ6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBvE%2F366gqAhQt9IDa36CEQn1QRd65MoeI7gzqV%2Bp5F0AiAjgjSMq9gEKLaY6mxyHLqtajfn0tAAAB3b%2BP9gojYLmCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRpjyh9kvMuk1hqtuKtwDtSekRGkZFXQJuFPBxd%2F0Hz5pKWbDkbMCPU5oe0vA3l43pNwDceEhcCKPwcqszcsiWoyFgmd361sPIiRndiiKdgdS22Geo4Ov14EODiAJYnUyl7z7YUt%2BicPlSMeu00ngjHI2NAKthzr5fnvmMRCo6jtxDdg8KKBTBQ2D5A2id1Mw3Uii088yt1XXgKqFMe3X%2FMakDjhSn5B%2B%2BjCpB9%2FDVSBtmUe5FFwBvARsGbPV6IxIHcj%2F8IcU6QCi9dCyF49LBZhzw%2FupKWTgvKSY8Zdip4YOpu6hFxBQ%2FWuGVYi6DpqJ4qwdP65irU8GWM2HkejYaTDHN7Bivh2hIX43ReBCK%2BEVVfbp0e0UTWYo6xFH7dWf0AtrgXjpGsi40NVRmZCtTODHIm1JsyPAD3tI5FUzMO9kZeAff%2FTiC4teyY6m9liztkNhRmEelcLGxcV60eE4NOG7I00ffpGoM0oxWioHM54CxrOfmvg4jJOIEFjxDMM2Av2Tu2PZBF%2Br9r7sLPqXjrmqcd2wDR6yCjSt7fPAl2BqlT6BnskhECa4HgxpsnGaiPlKj3k26On7yhCcLs2hfRoLYrlAsiQYd3xoyaWGdEXk1Kf5dfts4rvYklbYxqlXnW1W3b6AkPU71fswtOD%2BvAY6pgFwEWz4qyrfsbnROZpIyWHBXgFqXFepZEEUmL%2Bc8OLKu60RtiAHv3g2V3%2BEctOg2bXKDmxKmLGOyQJSunieQwNUemXMimxbNmx5XxOie0vgBmKRA81wUD67mvqB0%2F%2BTELW2IBa67g0Q420JVYcVcda2y8hHKV2iB2qm1sE0m1mIPX2yov2Xl1%2BDO3pQ9yusgpFZiIw%2ByqQ6RyyF79wwCk%2FXHE5wbDm0&X-Amz-Signature=a04503535f733b2e99ebddd3e7f5b4a82caf0d2f9dd3fbecf0904e28e773d2d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJE7WGWL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr9yrb2arW5uJx3cIbv7ViONaITB8nHnDy8eWseTqmNwIhANA782AXtxjOon9Ygc41NmBlbyJiy3ps7cHIyjmh2qIYKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcePN2DH5Larej3vgq3AODzA7KlIrZhJjeuSyLRlgziMBQPg54wdzZdbVq%2Bo9RCQi9efj3nE%2BGtSBv64cyazt8Ao2fASMVHZEr0wwW5EelN5vBXvE3kUO2NTz104PHGwU%2FuE1Ss4YeeZ%2Bid26q%2B6MDIYqrbJOePgCyBQy4gz3Z70dqVejOPP23k%2BftpwCg4L%2BeerEWnGRDTeRJssm4M%2BJeodKJmPb7QCnetiSjAA6gffaszFuamI%2FXsFx8fn5zmPnxyDoOgYjfDJvZG7QNeGW2OGGHh8TRQORE3SEWEmdrfhpge2WElKPzbnZrU5kW%2Fpm51soIhp9WdmK4Wigjo9dUL60GWjYvgoLDAWf684aQLzp3DlO7X8%2FCoFaO3SbEfbhsekt9C36lPn1H140lcY0%2Fe7B8ebJP9KlW4%2BsrQ225X0TgNPZ9VgEbjMpb3pHuaeIEavTtzebQY1WNrA3I%2F3G97dG7tgisjpU5Ytouftv63%2BkKXbUOYaG0uj8jTVLepehTAx9l0NPWxVFzu274hm%2FCgvmtWY4GDaXEKMdw8t4Gsl9SHETXqIMV1zuOxGMxt7EWpTkbPoosWygsySH3FzzIN1RaKe4IHJqy0XxDD%2FsSw3EcD9Uz9LshfID7OOcaQV6%2BClhRBI8acZfF9DCtq%2F%2B8BjqkAcqRH9qQw0qnwFC2wouEpJz%2BTyOr6pFFfUvBvPq5JgSv%2BXrO%2FNKsJY8tNtwALl1ghLatFX%2B%2BpBlXRA5K3TA%2FFmIOOXlyhvRx8ELDQk5OcFTytCq8bUbaBi6n2RrYieu%2BhwkbuUs2KsHIXzfx5TfCNZfw8lXyp%2BMtbTjRcr%2BK%2BgnWvs3beFAVvZPJlW3VJbkXMVYFj3UDmV0YugdhCvkLLHCkgrfs&X-Amz-Signature=a7bb12b2b8f029d5b2bc88f2ec0fdafdfe50aea42fbcf0c803653084944aaeb1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJE7WGWL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr9yrb2arW5uJx3cIbv7ViONaITB8nHnDy8eWseTqmNwIhANA782AXtxjOon9Ygc41NmBlbyJiy3ps7cHIyjmh2qIYKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcePN2DH5Larej3vgq3AODzA7KlIrZhJjeuSyLRlgziMBQPg54wdzZdbVq%2Bo9RCQi9efj3nE%2BGtSBv64cyazt8Ao2fASMVHZEr0wwW5EelN5vBXvE3kUO2NTz104PHGwU%2FuE1Ss4YeeZ%2Bid26q%2B6MDIYqrbJOePgCyBQy4gz3Z70dqVejOPP23k%2BftpwCg4L%2BeerEWnGRDTeRJssm4M%2BJeodKJmPb7QCnetiSjAA6gffaszFuamI%2FXsFx8fn5zmPnxyDoOgYjfDJvZG7QNeGW2OGGHh8TRQORE3SEWEmdrfhpge2WElKPzbnZrU5kW%2Fpm51soIhp9WdmK4Wigjo9dUL60GWjYvgoLDAWf684aQLzp3DlO7X8%2FCoFaO3SbEfbhsekt9C36lPn1H140lcY0%2Fe7B8ebJP9KlW4%2BsrQ225X0TgNPZ9VgEbjMpb3pHuaeIEavTtzebQY1WNrA3I%2F3G97dG7tgisjpU5Ytouftv63%2BkKXbUOYaG0uj8jTVLepehTAx9l0NPWxVFzu274hm%2FCgvmtWY4GDaXEKMdw8t4Gsl9SHETXqIMV1zuOxGMxt7EWpTkbPoosWygsySH3FzzIN1RaKe4IHJqy0XxDD%2FsSw3EcD9Uz9LshfID7OOcaQV6%2BClhRBI8acZfF9DCtq%2F%2B8BjqkAcqRH9qQw0qnwFC2wouEpJz%2BTyOr6pFFfUvBvPq5JgSv%2BXrO%2FNKsJY8tNtwALl1ghLatFX%2B%2BpBlXRA5K3TA%2FFmIOOXlyhvRx8ELDQk5OcFTytCq8bUbaBi6n2RrYieu%2BhwkbuUs2KsHIXzfx5TfCNZfw8lXyp%2BMtbTjRcr%2BK%2BgnWvs3beFAVvZPJlW3VJbkXMVYFj3UDmV0YugdhCvkLLHCkgrfs&X-Amz-Signature=26c5f09fb0d39f1a65c8e74e7fcf7d71e787bb349153f22100a41ffb6f2b78bd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJE7WGWL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr9yrb2arW5uJx3cIbv7ViONaITB8nHnDy8eWseTqmNwIhANA782AXtxjOon9Ygc41NmBlbyJiy3ps7cHIyjmh2qIYKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcePN2DH5Larej3vgq3AODzA7KlIrZhJjeuSyLRlgziMBQPg54wdzZdbVq%2Bo9RCQi9efj3nE%2BGtSBv64cyazt8Ao2fASMVHZEr0wwW5EelN5vBXvE3kUO2NTz104PHGwU%2FuE1Ss4YeeZ%2Bid26q%2B6MDIYqrbJOePgCyBQy4gz3Z70dqVejOPP23k%2BftpwCg4L%2BeerEWnGRDTeRJssm4M%2BJeodKJmPb7QCnetiSjAA6gffaszFuamI%2FXsFx8fn5zmPnxyDoOgYjfDJvZG7QNeGW2OGGHh8TRQORE3SEWEmdrfhpge2WElKPzbnZrU5kW%2Fpm51soIhp9WdmK4Wigjo9dUL60GWjYvgoLDAWf684aQLzp3DlO7X8%2FCoFaO3SbEfbhsekt9C36lPn1H140lcY0%2Fe7B8ebJP9KlW4%2BsrQ225X0TgNPZ9VgEbjMpb3pHuaeIEavTtzebQY1WNrA3I%2F3G97dG7tgisjpU5Ytouftv63%2BkKXbUOYaG0uj8jTVLepehTAx9l0NPWxVFzu274hm%2FCgvmtWY4GDaXEKMdw8t4Gsl9SHETXqIMV1zuOxGMxt7EWpTkbPoosWygsySH3FzzIN1RaKe4IHJqy0XxDD%2FsSw3EcD9Uz9LshfID7OOcaQV6%2BClhRBI8acZfF9DCtq%2F%2B8BjqkAcqRH9qQw0qnwFC2wouEpJz%2BTyOr6pFFfUvBvPq5JgSv%2BXrO%2FNKsJY8tNtwALl1ghLatFX%2B%2BpBlXRA5K3TA%2FFmIOOXlyhvRx8ELDQk5OcFTytCq8bUbaBi6n2RrYieu%2BhwkbuUs2KsHIXzfx5TfCNZfw8lXyp%2BMtbTjRcr%2BK%2BgnWvs3beFAVvZPJlW3VJbkXMVYFj3UDmV0YugdhCvkLLHCkgrfs&X-Amz-Signature=6f7acc9db0f10285a35d303bdb0c043a8ce9bbfdfb3286aaadf1de4ca83703ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJE7WGWL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr9yrb2arW5uJx3cIbv7ViONaITB8nHnDy8eWseTqmNwIhANA782AXtxjOon9Ygc41NmBlbyJiy3ps7cHIyjmh2qIYKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcePN2DH5Larej3vgq3AODzA7KlIrZhJjeuSyLRlgziMBQPg54wdzZdbVq%2Bo9RCQi9efj3nE%2BGtSBv64cyazt8Ao2fASMVHZEr0wwW5EelN5vBXvE3kUO2NTz104PHGwU%2FuE1Ss4YeeZ%2Bid26q%2B6MDIYqrbJOePgCyBQy4gz3Z70dqVejOPP23k%2BftpwCg4L%2BeerEWnGRDTeRJssm4M%2BJeodKJmPb7QCnetiSjAA6gffaszFuamI%2FXsFx8fn5zmPnxyDoOgYjfDJvZG7QNeGW2OGGHh8TRQORE3SEWEmdrfhpge2WElKPzbnZrU5kW%2Fpm51soIhp9WdmK4Wigjo9dUL60GWjYvgoLDAWf684aQLzp3DlO7X8%2FCoFaO3SbEfbhsekt9C36lPn1H140lcY0%2Fe7B8ebJP9KlW4%2BsrQ225X0TgNPZ9VgEbjMpb3pHuaeIEavTtzebQY1WNrA3I%2F3G97dG7tgisjpU5Ytouftv63%2BkKXbUOYaG0uj8jTVLepehTAx9l0NPWxVFzu274hm%2FCgvmtWY4GDaXEKMdw8t4Gsl9SHETXqIMV1zuOxGMxt7EWpTkbPoosWygsySH3FzzIN1RaKe4IHJqy0XxDD%2FsSw3EcD9Uz9LshfID7OOcaQV6%2BClhRBI8acZfF9DCtq%2F%2B8BjqkAcqRH9qQw0qnwFC2wouEpJz%2BTyOr6pFFfUvBvPq5JgSv%2BXrO%2FNKsJY8tNtwALl1ghLatFX%2B%2BpBlXRA5K3TA%2FFmIOOXlyhvRx8ELDQk5OcFTytCq8bUbaBi6n2RrYieu%2BhwkbuUs2KsHIXzfx5TfCNZfw8lXyp%2BMtbTjRcr%2BK%2BgnWvs3beFAVvZPJlW3VJbkXMVYFj3UDmV0YugdhCvkLLHCkgrfs&X-Amz-Signature=13b59664cea9efbbe7d19d7d04bacf9989ba884a4173ef8e91099bd0f22b2779&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJE7WGWL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr9yrb2arW5uJx3cIbv7ViONaITB8nHnDy8eWseTqmNwIhANA782AXtxjOon9Ygc41NmBlbyJiy3ps7cHIyjmh2qIYKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcePN2DH5Larej3vgq3AODzA7KlIrZhJjeuSyLRlgziMBQPg54wdzZdbVq%2Bo9RCQi9efj3nE%2BGtSBv64cyazt8Ao2fASMVHZEr0wwW5EelN5vBXvE3kUO2NTz104PHGwU%2FuE1Ss4YeeZ%2Bid26q%2B6MDIYqrbJOePgCyBQy4gz3Z70dqVejOPP23k%2BftpwCg4L%2BeerEWnGRDTeRJssm4M%2BJeodKJmPb7QCnetiSjAA6gffaszFuamI%2FXsFx8fn5zmPnxyDoOgYjfDJvZG7QNeGW2OGGHh8TRQORE3SEWEmdrfhpge2WElKPzbnZrU5kW%2Fpm51soIhp9WdmK4Wigjo9dUL60GWjYvgoLDAWf684aQLzp3DlO7X8%2FCoFaO3SbEfbhsekt9C36lPn1H140lcY0%2Fe7B8ebJP9KlW4%2BsrQ225X0TgNPZ9VgEbjMpb3pHuaeIEavTtzebQY1WNrA3I%2F3G97dG7tgisjpU5Ytouftv63%2BkKXbUOYaG0uj8jTVLepehTAx9l0NPWxVFzu274hm%2FCgvmtWY4GDaXEKMdw8t4Gsl9SHETXqIMV1zuOxGMxt7EWpTkbPoosWygsySH3FzzIN1RaKe4IHJqy0XxDD%2FsSw3EcD9Uz9LshfID7OOcaQV6%2BClhRBI8acZfF9DCtq%2F%2B8BjqkAcqRH9qQw0qnwFC2wouEpJz%2BTyOr6pFFfUvBvPq5JgSv%2BXrO%2FNKsJY8tNtwALl1ghLatFX%2B%2BpBlXRA5K3TA%2FFmIOOXlyhvRx8ELDQk5OcFTytCq8bUbaBi6n2RrYieu%2BhwkbuUs2KsHIXzfx5TfCNZfw8lXyp%2BMtbTjRcr%2BK%2BgnWvs3beFAVvZPJlW3VJbkXMVYFj3UDmV0YugdhCvkLLHCkgrfs&X-Amz-Signature=457e240f2af3e78444a49f97c59e5b560ce9942547d959cbd2a4212ceaa45aae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJE7WGWL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr9yrb2arW5uJx3cIbv7ViONaITB8nHnDy8eWseTqmNwIhANA782AXtxjOon9Ygc41NmBlbyJiy3ps7cHIyjmh2qIYKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcePN2DH5Larej3vgq3AODzA7KlIrZhJjeuSyLRlgziMBQPg54wdzZdbVq%2Bo9RCQi9efj3nE%2BGtSBv64cyazt8Ao2fASMVHZEr0wwW5EelN5vBXvE3kUO2NTz104PHGwU%2FuE1Ss4YeeZ%2Bid26q%2B6MDIYqrbJOePgCyBQy4gz3Z70dqVejOPP23k%2BftpwCg4L%2BeerEWnGRDTeRJssm4M%2BJeodKJmPb7QCnetiSjAA6gffaszFuamI%2FXsFx8fn5zmPnxyDoOgYjfDJvZG7QNeGW2OGGHh8TRQORE3SEWEmdrfhpge2WElKPzbnZrU5kW%2Fpm51soIhp9WdmK4Wigjo9dUL60GWjYvgoLDAWf684aQLzp3DlO7X8%2FCoFaO3SbEfbhsekt9C36lPn1H140lcY0%2Fe7B8ebJP9KlW4%2BsrQ225X0TgNPZ9VgEbjMpb3pHuaeIEavTtzebQY1WNrA3I%2F3G97dG7tgisjpU5Ytouftv63%2BkKXbUOYaG0uj8jTVLepehTAx9l0NPWxVFzu274hm%2FCgvmtWY4GDaXEKMdw8t4Gsl9SHETXqIMV1zuOxGMxt7EWpTkbPoosWygsySH3FzzIN1RaKe4IHJqy0XxDD%2FsSw3EcD9Uz9LshfID7OOcaQV6%2BClhRBI8acZfF9DCtq%2F%2B8BjqkAcqRH9qQw0qnwFC2wouEpJz%2BTyOr6pFFfUvBvPq5JgSv%2BXrO%2FNKsJY8tNtwALl1ghLatFX%2B%2BpBlXRA5K3TA%2FFmIOOXlyhvRx8ELDQk5OcFTytCq8bUbaBi6n2RrYieu%2BhwkbuUs2KsHIXzfx5TfCNZfw8lXyp%2BMtbTjRcr%2BK%2BgnWvs3beFAVvZPJlW3VJbkXMVYFj3UDmV0YugdhCvkLLHCkgrfs&X-Amz-Signature=26bea7c1e0479edfe4afd2a8e5dd8dbaa4e42a9a40b3c107a528521ad892649c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QO3KM4Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6nck%2BbdTsM1QW0W4DUYEL3GAy65pdAieL8n8hUPCZAAIhAJzeyWeMABzNoDwKIPPQJFnT1kLe4osfFEwWB%2FJL1p5GKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKKXDm%2FuRuG84nixMq3AO3tVot9ZzlouJS5NSEBVnEtN2RQ8xHnEnTNq9E8qWv%2BrrwzJlCAmQJ%2B%2Fb%2BZ75yHeLGfkDwemtHiVAZYP4MLAozP2xdcvISZ4XtAe2p%2FheH1DAK6rVCKEmeJAdGJhDtkO9yYfmeZ3AsGr%2B1lEoc2gNWYlyun4EWOvH%2FDKsz%2FWv3yG3rk404Rs7Xkmaa3dclyLKfK1o2NL2novXSyl9NVHlPJMRjAxCMLujLm%2FLQ%2FJJiXnBxKNIb6TF4gdL4taECQo8hLKfqug6zovO6Ee8ybT3XULmKXTbz51IQB4jVxrcATbgRZ1POj5SHubQ%2BZePMsdhqnz5mKc3vBGt%2BTE1BcDuEz7gW7NiGPIGVII5KLA9u9MczRBECa650GA2QZpqEdM5PHiKCo5a02eCyGuEtL7Lstwzhtzo2We81yBEMX4KjaRBIVdjYNInpWdzcNXvlPygxK4DmxLDQ1JYzTD6enDY8bEo7MT5KeQCLvuU7jw9TyBlEP6fvCnVciQwoQKGrzcDgWH3cb51nWNepHAncg5l4PGtaCw1ZikY1ZVUqcv1j0F9tFGrbsY2i%2B2YtS9pbkZtarVrklvSaHU3zIY1x%2FYG%2BoqFiM7fDclKNiU19gZYc5mLBkil%2FUoa7o6oY4DDj4f68BjqkARo1h4jGuzaNSSqJ3jZw0tsy5wMB7GLI3TVUV8w6HY%2FEVz%2FETyDXWrLT3f8LVQv3bQp5Bj%2BwS3smN%2BAV1LAEZwU3FmiYAiEJQa%2B2W7USG7QR80bfNegSyxNb2p%2FQi64%2FvIG61jcvm%2FO0dAp9fsLfXGC4lR1Q5InOHAWH1p4LJQyFv7w5NIiN1P0pBGYzJDCwpmBNAeGmZEgEtuiy8Q35v62gE0nB&X-Amz-Signature=2ecae73ca6b1be1d327a3005bb95d85e621c93b8c76e4b75425665467b096bae&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SB7SOU34%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJDcQCvc4lP1Vajf9Y6hLi8MVggLbn6IjrcPEilZakYwIgelGIrYEj9H61YhnOb7Trx25%2Fv4Vb%2FQyUNWKpPTHwXPIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHtvIrAeq2a22uolircAzJ6zD6AwHtZEOYeOJHmd9Zrxcm2g8JDiyLJxtXtIafPV5%2F1NIeuFvwYYRq9p%2BcSLzkh1mi5u6hJKnWJJfacTOWY9SVQ1NHwPT4HBuRodsUr8mfhcMaQeuqgl3EKb2Zhb2tUcOB2kpxG9EqLUh6VklcDukEcUqdkKpT4%2BEE%2Buwn4iZhrUzBtmY%2FUeq8Hxg2eO7v1xWiErGprOYt0Vl8agoWudlKqSJo7nGP0VO2ZPvgngR7YxpoRMp9DpqwPedQcO1I8yIlnV9NFsMpeguIBAc9tvyYDURY3QUPRhFUIksH2erk0RHHhUGChQKrGFqbFid6ojboQ6DDe4h4S8R3ZbsENItz13uSN0xLFoqwtC%2BC8%2FME%2BRA3LQp6xAdj4SD5k4U5Sqhl82%2B3rY8denE6Yn0DAkwNXOjxqnVBc0j188BvD35%2F83si4oW7amM18LFRb04loeIpCo%2F03Cx9oPl8EMXcWKzueQtm6F0Fykl3BKpWiBWY5xZ5Zwncl%2FzCPpzq362fh%2Bz2F70VamAzFaPWfZu%2ByJL%2BbK8jlgQELC2xILcFQZV5hvah4lkjLPqb0aSsYhwFW0ieMqNOAJqqKwKbY%2FXhXtRo%2B6ceU8JGxaEmiPD7v6lYxpIitjhaTHQseMPzi%2FrwGOqUB%2B3km4P03LOwFYEyRioKsgy8EE3L83%2BzA7qG2xPkoTxzo%2BuceG7KSbyA9l8%2Ba2MRlA0zaEEkpmMknxj9U%2FYN7nKODbfDf3Yu4s%2BuYK5HFBkJLkKe3VH7jFdC5QRJo6eESnxyRWkVpUE%2B%2BLj0Cxmqx2wYtHBCYvnTqAjlJED8LEseLP7R2XMGrPLVAuRYFP1qlCs%2F3QG73jAjc5Gp%2FUdlqCe7U1XWS&X-Amz-Signature=09a30c2bf80a92b096c2df46d99cf531abc00b2c92bb8ada89a71e94f561a2f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJE7WGWL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr9yrb2arW5uJx3cIbv7ViONaITB8nHnDy8eWseTqmNwIhANA782AXtxjOon9Ygc41NmBlbyJiy3ps7cHIyjmh2qIYKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcePN2DH5Larej3vgq3AODzA7KlIrZhJjeuSyLRlgziMBQPg54wdzZdbVq%2Bo9RCQi9efj3nE%2BGtSBv64cyazt8Ao2fASMVHZEr0wwW5EelN5vBXvE3kUO2NTz104PHGwU%2FuE1Ss4YeeZ%2Bid26q%2B6MDIYqrbJOePgCyBQy4gz3Z70dqVejOPP23k%2BftpwCg4L%2BeerEWnGRDTeRJssm4M%2BJeodKJmPb7QCnetiSjAA6gffaszFuamI%2FXsFx8fn5zmPnxyDoOgYjfDJvZG7QNeGW2OGGHh8TRQORE3SEWEmdrfhpge2WElKPzbnZrU5kW%2Fpm51soIhp9WdmK4Wigjo9dUL60GWjYvgoLDAWf684aQLzp3DlO7X8%2FCoFaO3SbEfbhsekt9C36lPn1H140lcY0%2Fe7B8ebJP9KlW4%2BsrQ225X0TgNPZ9VgEbjMpb3pHuaeIEavTtzebQY1WNrA3I%2F3G97dG7tgisjpU5Ytouftv63%2BkKXbUOYaG0uj8jTVLepehTAx9l0NPWxVFzu274hm%2FCgvmtWY4GDaXEKMdw8t4Gsl9SHETXqIMV1zuOxGMxt7EWpTkbPoosWygsySH3FzzIN1RaKe4IHJqy0XxDD%2FsSw3EcD9Uz9LshfID7OOcaQV6%2BClhRBI8acZfF9DCtq%2F%2B8BjqkAcqRH9qQw0qnwFC2wouEpJz%2BTyOr6pFFfUvBvPq5JgSv%2BXrO%2FNKsJY8tNtwALl1ghLatFX%2B%2BpBlXRA5K3TA%2FFmIOOXlyhvRx8ELDQk5OcFTytCq8bUbaBi6n2RrYieu%2BhwkbuUs2KsHIXzfx5TfCNZfw8lXyp%2BMtbTjRcr%2BK%2BgnWvs3beFAVvZPJlW3VJbkXMVYFj3UDmV0YugdhCvkLLHCkgrfs&X-Amz-Signature=106de10c1e0771ede1e4ff3a4a7cbf0505666046854e6125561115e08ed2f86b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJE7WGWL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr9yrb2arW5uJx3cIbv7ViONaITB8nHnDy8eWseTqmNwIhANA782AXtxjOon9Ygc41NmBlbyJiy3ps7cHIyjmh2qIYKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcePN2DH5Larej3vgq3AODzA7KlIrZhJjeuSyLRlgziMBQPg54wdzZdbVq%2Bo9RCQi9efj3nE%2BGtSBv64cyazt8Ao2fASMVHZEr0wwW5EelN5vBXvE3kUO2NTz104PHGwU%2FuE1Ss4YeeZ%2Bid26q%2B6MDIYqrbJOePgCyBQy4gz3Z70dqVejOPP23k%2BftpwCg4L%2BeerEWnGRDTeRJssm4M%2BJeodKJmPb7QCnetiSjAA6gffaszFuamI%2FXsFx8fn5zmPnxyDoOgYjfDJvZG7QNeGW2OGGHh8TRQORE3SEWEmdrfhpge2WElKPzbnZrU5kW%2Fpm51soIhp9WdmK4Wigjo9dUL60GWjYvgoLDAWf684aQLzp3DlO7X8%2FCoFaO3SbEfbhsekt9C36lPn1H140lcY0%2Fe7B8ebJP9KlW4%2BsrQ225X0TgNPZ9VgEbjMpb3pHuaeIEavTtzebQY1WNrA3I%2F3G97dG7tgisjpU5Ytouftv63%2BkKXbUOYaG0uj8jTVLepehTAx9l0NPWxVFzu274hm%2FCgvmtWY4GDaXEKMdw8t4Gsl9SHETXqIMV1zuOxGMxt7EWpTkbPoosWygsySH3FzzIN1RaKe4IHJqy0XxDD%2FsSw3EcD9Uz9LshfID7OOcaQV6%2BClhRBI8acZfF9DCtq%2F%2B8BjqkAcqRH9qQw0qnwFC2wouEpJz%2BTyOr6pFFfUvBvPq5JgSv%2BXrO%2FNKsJY8tNtwALl1ghLatFX%2B%2BpBlXRA5K3TA%2FFmIOOXlyhvRx8ELDQk5OcFTytCq8bUbaBi6n2RrYieu%2BhwkbuUs2KsHIXzfx5TfCNZfw8lXyp%2BMtbTjRcr%2BK%2BgnWvs3beFAVvZPJlW3VJbkXMVYFj3UDmV0YugdhCvkLLHCkgrfs&X-Amz-Signature=66cd71e6051e76232897f5e740bc25c47366291413fc8b07209ac4835e906ab1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJE7WGWL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr9yrb2arW5uJx3cIbv7ViONaITB8nHnDy8eWseTqmNwIhANA782AXtxjOon9Ygc41NmBlbyJiy3ps7cHIyjmh2qIYKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcePN2DH5Larej3vgq3AODzA7KlIrZhJjeuSyLRlgziMBQPg54wdzZdbVq%2Bo9RCQi9efj3nE%2BGtSBv64cyazt8Ao2fASMVHZEr0wwW5EelN5vBXvE3kUO2NTz104PHGwU%2FuE1Ss4YeeZ%2Bid26q%2B6MDIYqrbJOePgCyBQy4gz3Z70dqVejOPP23k%2BftpwCg4L%2BeerEWnGRDTeRJssm4M%2BJeodKJmPb7QCnetiSjAA6gffaszFuamI%2FXsFx8fn5zmPnxyDoOgYjfDJvZG7QNeGW2OGGHh8TRQORE3SEWEmdrfhpge2WElKPzbnZrU5kW%2Fpm51soIhp9WdmK4Wigjo9dUL60GWjYvgoLDAWf684aQLzp3DlO7X8%2FCoFaO3SbEfbhsekt9C36lPn1H140lcY0%2Fe7B8ebJP9KlW4%2BsrQ225X0TgNPZ9VgEbjMpb3pHuaeIEavTtzebQY1WNrA3I%2F3G97dG7tgisjpU5Ytouftv63%2BkKXbUOYaG0uj8jTVLepehTAx9l0NPWxVFzu274hm%2FCgvmtWY4GDaXEKMdw8t4Gsl9SHETXqIMV1zuOxGMxt7EWpTkbPoosWygsySH3FzzIN1RaKe4IHJqy0XxDD%2FsSw3EcD9Uz9LshfID7OOcaQV6%2BClhRBI8acZfF9DCtq%2F%2B8BjqkAcqRH9qQw0qnwFC2wouEpJz%2BTyOr6pFFfUvBvPq5JgSv%2BXrO%2FNKsJY8tNtwALl1ghLatFX%2B%2BpBlXRA5K3TA%2FFmIOOXlyhvRx8ELDQk5OcFTytCq8bUbaBi6n2RrYieu%2BhwkbuUs2KsHIXzfx5TfCNZfw8lXyp%2BMtbTjRcr%2BK%2BgnWvs3beFAVvZPJlW3VJbkXMVYFj3UDmV0YugdhCvkLLHCkgrfs&X-Amz-Signature=b552fb2cd64ac876a2791b855f285b08e033e1666b622dbf086b1a61d6de8434&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625SFBM74%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNdOoB9VtMpIUpO4GRD3byKR4FKA4%2FmYRRFYFyOIiXnAiEArfO5OO7oMAnLDeGthIbljHb7bD10HlDEk52N2XCnTvAqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFEn%2BdmUvMhy6a2x1CrcA5WwoEg4H03bP02jY7Col5tHn%2FlYDKb66F3NaUMiIpwYCqoZRxUNMPyG3TxrwyIzIkXoBGDgjgLXdozJdDTh9s1mjFPJpSzVxgdeY2a8K6Z5cwmwHQBGfGmyg%2FzYyvUSaUDAycAv0p42c4IIzKMdPY%2F1uZKjpbgsOdrJQ6QJObg%2FgBC9MKslrl5fj2nfdcw2VFNG%2F2WoSuhBroe62FmIYIQV8Be9q4CYoN5vh3GnRfDg2%2BWOxhNl2k7GYTRCcU6MkqNZoxkMAyjBNqBaAi3oohp13YBReNgbO%2Ble2gL%2Bh3geCDzIeUlL7GjYaMr6enJFvORVe5RhWzP73rFXcyr9JXMdCIA9WhXpqQ7th8hq4eQ8o2XaBXDgEZ7n6BjMryAoMViSF8JEfuh2Ac6O0yTXqruiSZ6%2BoCSQsf3odzb0d0ShsVRnNL4Ae1Ai297kEuwS2M%2FtgkN9a8rcukJJBCcKpRgL7e6UDzdZVy1UDz89qhWmKxCfc0sK3TyarLlTpBCy09GZWLG6HcILNkmpgiPxCl4i2L7b9L%2BKgmqojIJ46fEd7e54eDNNsvsDgrbzmZe5qwdRaAXJPeQo8khXGELcO56mZQY9lZLbMVientjoX23w5RBV6sPLrsp6RBrcMIfb%2FrwGOqUB9KtUngIi48nDTimbfPnvzmxZl1v95ikbCMazRLKRicdlp%2FHTaFzCAxcdkQUCO3yfwflqFcP33vmLnT2Ha9zpi1KvQUVZ4tZJ0ZyE5lyuXG%2B0LmhfmZhikVdAqt6ewoh6kx773lvGlBh2GUXk5rFMlgryCBjkAOTJJWHIStVLjorc%2FX%2B07jzC%2FcpKrHSo8GcDJgakfi5aUMoLUV1OiWpgZC2HCDb%2B&X-Amz-Signature=22e62a3b2b397c71424bc2070dfc7fd23f0492d36460f440120340d8c6c4f8cb&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GZ5QUB5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvJPNcb9OPVvojGXMTNupr0d6IiquxNi%2BInJuLux%2Ba8AiAOC3IYlg6K8kcrEb8zZJRoi7g1rR%2FuEi5oiE1Zs3sMiiqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdBEO%2BaECleItJ0b4KtwDlzYClGV334OnlzXnfjHEugoAQtKFhtKULdCd%2BT9b3JsWMPzoSJ81ycA75hS2%2FrSvReQBX5KjbpCLtGguJYDAYnj%2FVGXcq8ummpboak%2FbzwuCD9eKEEMjYlEALw6uourYT%2BHVzxs1WRl%2FyT4hXMTKwFtA3jDvooeYjVLU7Y6wYuKbkQ7q%2FnCGflI8qZd3F5O72jdMaZCv3AiaXH7aVwBzdNGmNd%2B5eUVouofFdk0Aqx2aUYSGWIzhe%2BWy0odTODDB8pWCt00OZ2oxwKKDaSFw3QaIkvGgubO5efj69MUmeaY39IYvKl0W95TkXkrkiR7fPLGP50LmNGf0vBEoI0sPJJ1EKfye%2FTF9pNR4RDLPvagtXHnHTYfvlllPL%2BtcTvEHMYZu5BiQEu8e4t7dJwMmCWLdZUAmqiVeK%2FBhNz00iae0H5%2Ff9EqXC12iWIMf%2BGrKnFADyTNPrCfYg1%2F39LhMCAk7keBygbZA0d%2BLeBZjovdPVuiVcAGC7jSXyb%2BNihXIkP8IZAX0e01Uc4IkTfHytQnTEXGq5p7rBa%2FeUuoRxk5g3pNuUo9%2FJPYcjqr8sgo0ohv4eq69y8GyIUGGyqtjSyDiEt3Gfzyye%2BVoQhMCulMJenz41qYnWYnktEgwgt3%2BvAY6pgFEl%2B7EcEmJ8yCbEI%2BXw6eAhFGmHZPBGbuGvltdVLpJokLcLeUvQMIKsnyYvw%2FjU6smkx13gC%2FxXjOnFckmJy56uoa00hUl63Svex1ZgbdW310EngZ4%2FPb4rKQpoQfL4kcV5zo9KBcyp9SHU61FEH348NjsDiehe9qC%2FH%2FV0d91KlsRKX8ouhlPqP%2FZSUqmCPLRkf%2BjcMV%2B1i4TZ48k9V1wM3PT6HCb&X-Amz-Signature=629084fc4c8aeffe1772794e700029af8b1870f321a4513b282256fdd39bc10b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJRDQ4PT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmRkSIzbQat%2FgF5ZCJFrgc4HMYrDif7SJ%2BkNHY4jU%2F8AiAAuqeDTQp%2FQGowdVVGSOeCX2PKXGZQdRNQg2n%2B5K%2Fh1SqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMca74ZTKFOKC%2FuJaKKtwDAaH%2BCoko2yHM%2FQQWbHEIBfyJV7CUARU6iE6s5ZDsp6k5yAeY%2B6cv%2FlT94X3JDvMLSsPh7Gy6O%2F80DSFQzHlARjXkJeyho0iLgyGSki6GK%2FOPqzKm9sontIS4p9utYZejfmZ%2B7xGuBjixfoVbsNgjNuyd3nHLNrBLwpYHCtdGaiKLKWet3hPnQSQwEf8jGkPV1v4kChG%2F0%2BoOn9gJUFHVFAq8qlYzX5%2B2Uc2mTHyzA1oSpZ4XzrwRNxnY8DhddYdRJPDt%2FhbKX9IRYpPxNTVOJHPLKl6zLi3pP%2BZJfJp4p%2FwK9KerVD%2FH%2FmLOv5LBwWVSqxR5l0XsIRfHx0ZXIyY%2FVfLVY9OkU7%2BV9Gm1k9VamRD0V4DULYhK8giZy%2BEQsAbUzdFaMSYeyi2vdbyD1t2dLrPTZL4vTQJqW8m4MxThUkc8Bob211sU9b2%2Bzkrkqdt8O3x4cn5E9MI9yK7ZgzfWlRJAcULS7LYoZZSbP3DGy11vE4wOhVrECuTonFlA%2FdSMU03dkobrtFU0thfrTl8FmgRkhha4cYpchSXFtIg3ha5J6c%2F6AVlXnfn8Y%2FjfZUwRRfhlVDj5D9i0WSEDdSWe%2BLVdeI0LnYx4Flro2JvjojMljmXx6QRRwwuoGLEwpeX%2BvAY6pgEY4x3t1VwoNU0zv4VsYxOSwlJQwrOynlFcThnimX6QAF2w8Jye9Hs3dVS%2BzCbJhOZ%2BnMaYN61j92HTVq6v%2BkOlq9%2FiRHS9GXneLAQKVmIyO72LqNTqS4tpMasy8ykLX1cn9i0uVWiKf65NRBgoZ3KEtM3hyx%2F414KddUygpVbc8BsJqra%2FJwasVu7m4N3%2Blhs%2Fiyr%2Fm7VBtOVtqslffxRzhZJSVXNh&X-Amz-Signature=da9d467c22c78150e2cf3ae509daab06e7bd8c40d52aef8bbcbc859daae02e82&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466343SPVIQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn6i0DLTU%2ByVwS98CitmzKgwqHTvNULDTryFehOmR2WgIgInEvG3rWZR8TcnQ03EpDiF2WJFfjVPFoay79fKJVWxMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA1JALlw%2BF1CMdLuCyrcAx5EjxWEFXckg5xzMIvKZW1BlwDOhDeIOY%2FwGppg%2Fc5f3%2FjUb%2BXhLy7JQdgtqnYs91N%2FnlEw0LQrhA7UAao4Lu7iEZSObQ7NwuendkTtp57wSZZIoeMwPT69xEd5AADeKBPzipGS5HBb9iYDFEOWYvmp2kDOBrNYC%2FGT36A1M%2Bh6PgPplJ4iJ6y5gmmJM97GwM5ZsYgMBw7lbq3NVwYpLYwTd8aI5FDfkpZOcrfxAUGjfOoQvl0337Q4zsDuLhWd3KIeBIIk1DQfbhuysvEvBXe%2BSzdwuyUxKqfvi3DbWXqwl%2BmaLhdEPR%2FRPIyS1Y%2BWT1FcKz2YErPIZF5vVRpL4scwGI4eSql7mzQXUm59230mbu3fU5MHC1UKVgh0fernMd6Q7Kc%2BnjJzPcFWBd%2Bp%2FBTr0Cn%2FvAf3qIvdGmXemQbbVJC9ZCJD2zMshvj2H%2FxTSCgzWyfnlIBYermDndAbG3Jyn0FFXQSL0R0Y2Tj1c0KVdTGtyiAY4YAvVAAYdTvtq0d0hy3hyuCxSqYtH0Am6DdWujw%2F5JIZDnSo5SooN%2FBjRiho8IdRxNueLF2AB8lwVS9Qec8tvH17ru2jK6KxAWHp6Oz8HpuIwPosxkMO5C1IFHmFcjRnfHTm4nzsMMfh%2FrwGOqUBgu8mSQ60hD%2FoZlGbidqArXBq66dlorGxC4H3iTN3lSWyNpnRN6nXmXRo5W9OloMy0MEhdC3cn8fJemBG2GvPCaxGYfLbToQg568jhNlJ2IzBlGKek74OA7540iFLDxHWsHmMWyoUcSkOAj1X1R4IwkAgD3I%2BYlWDuGc%2BwxsI3KgfX0aP%2BTCfUsDTxpjsOqytpW4i6Q%2BO1zDatIUiQ4Pkkd24Uh9m&X-Amz-Signature=10111d0ff96b38b6e47a050b0116f528dad90d1a34df14866d41caabb482777c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466343SPVIQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn6i0DLTU%2ByVwS98CitmzKgwqHTvNULDTryFehOmR2WgIgInEvG3rWZR8TcnQ03EpDiF2WJFfjVPFoay79fKJVWxMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA1JALlw%2BF1CMdLuCyrcAx5EjxWEFXckg5xzMIvKZW1BlwDOhDeIOY%2FwGppg%2Fc5f3%2FjUb%2BXhLy7JQdgtqnYs91N%2FnlEw0LQrhA7UAao4Lu7iEZSObQ7NwuendkTtp57wSZZIoeMwPT69xEd5AADeKBPzipGS5HBb9iYDFEOWYvmp2kDOBrNYC%2FGT36A1M%2Bh6PgPplJ4iJ6y5gmmJM97GwM5ZsYgMBw7lbq3NVwYpLYwTd8aI5FDfkpZOcrfxAUGjfOoQvl0337Q4zsDuLhWd3KIeBIIk1DQfbhuysvEvBXe%2BSzdwuyUxKqfvi3DbWXqwl%2BmaLhdEPR%2FRPIyS1Y%2BWT1FcKz2YErPIZF5vVRpL4scwGI4eSql7mzQXUm59230mbu3fU5MHC1UKVgh0fernMd6Q7Kc%2BnjJzPcFWBd%2Bp%2FBTr0Cn%2FvAf3qIvdGmXemQbbVJC9ZCJD2zMshvj2H%2FxTSCgzWyfnlIBYermDndAbG3Jyn0FFXQSL0R0Y2Tj1c0KVdTGtyiAY4YAvVAAYdTvtq0d0hy3hyuCxSqYtH0Am6DdWujw%2F5JIZDnSo5SooN%2FBjRiho8IdRxNueLF2AB8lwVS9Qec8tvH17ru2jK6KxAWHp6Oz8HpuIwPosxkMO5C1IFHmFcjRnfHTm4nzsMMfh%2FrwGOqUBgu8mSQ60hD%2FoZlGbidqArXBq66dlorGxC4H3iTN3lSWyNpnRN6nXmXRo5W9OloMy0MEhdC3cn8fJemBG2GvPCaxGYfLbToQg568jhNlJ2IzBlGKek74OA7540iFLDxHWsHmMWyoUcSkOAj1X1R4IwkAgD3I%2BYlWDuGc%2BwxsI3KgfX0aP%2BTCfUsDTxpjsOqytpW4i6Q%2BO1zDatIUiQ4Pkkd24Uh9m&X-Amz-Signature=5241cbe217fc687df684fdc79f3c9e8f37bfba0c6ae4beaf11c217d5718c5986&X-Amz-SignedHeaders=host&x-id=GetObject)

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
