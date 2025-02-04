

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFXTPGB7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCBq4GQaAKxPQ%2Fb6CCD8LG3jMSfdtFxLjfxMaM2VmMOOQIhAJ3voteqoNjYRaC5T%2BFkgNuO22In6WVxM0f2mT9AWL7UKv8DCDUQABoMNjM3NDIzMTgzODA1IgyelHLpruTF1uCqrSsq3AM%2BYGGIAmwetn9%2B%2BvQd8hZZFQ1jd%2BA4NylVlykcI%2FnhMyIlGrS52Zp9VajH9N5rurx4jVKj9zKzEOvWb4g%2BAo0DDN0ULxkquAIR1ixUYgpQza1Nh0ucc42B64Ilw0rGhVflB%2BsqCLZry84ZdKXSL3dJHAVqi1GDahKnIZyDFBRsGwwcLZJSDCTRmBXVusPCtDB3E6CFRByelm%2B3l3sHpdhnKiHaDq7MFXFdfVECICQ0r2Nz7YIMEdhnsw%2B2QMzLTS1o%2F5z8lwjPrRevCAk8IC3SunBI12117cgbocUGOoz5eNfjns5BI1zd2%2B0pwWEAdPCivW1NVA%2FQWqUw45aEYaWJDPNz%2FOZwB0u8R%2FxbWfWrbMqgkaMQ0EQFPtM3FEITeePruoYmv1fO3ki5M7saOazZLQx%2FJJBiU3A6Kd6tCBhOJYn%2Fvq4EZ3i8KVgVl7AncbY8Rg6WLRdK7u1dZF4wdK%2B8vm%2BlDzxVWojhNAr4KZcXDbi%2FAEpkQ0bOrdhkNncvzGcYfGqJLEGIHBkVKoy4xIOk26FWHFCJmTHQ2zWv1RE%2BqHtxq%2FqhB70oB4Lyn5SZqLW5XgSs4aMNmcy42gSa5h1HkgRGFi4XCgVfD5BVt%2B4uYme0y8Fs0nMM%2BfcbDzD13Im9BjqkAfhoCUCl4gIrUAtihfMLD2EviAXhdZv9Btmkz956iPSRyGTbeXC%2FoMzfsiNBdhDQpf5elIYCGIgnVYvmLX4GhlzMylch10KoiWHjqQ8LO2HvyfZ0TKOL3ETYMrPHXl1xGYMLOh2FB8OsFcJ67%2FrGgJmt15O6S1h4AK0ibfb4ZM%2FrnMn8u7BKj74iq0HJ2v8QH4qp8HW9ArlbeUzz915%2BPdXtmDqP&X-Amz-Signature=d2c71ae7f10e34c7a0dff26a122d12359d1a29b535b0ad6378deec430100aef5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFXTPGB7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCBq4GQaAKxPQ%2Fb6CCD8LG3jMSfdtFxLjfxMaM2VmMOOQIhAJ3voteqoNjYRaC5T%2BFkgNuO22In6WVxM0f2mT9AWL7UKv8DCDUQABoMNjM3NDIzMTgzODA1IgyelHLpruTF1uCqrSsq3AM%2BYGGIAmwetn9%2B%2BvQd8hZZFQ1jd%2BA4NylVlykcI%2FnhMyIlGrS52Zp9VajH9N5rurx4jVKj9zKzEOvWb4g%2BAo0DDN0ULxkquAIR1ixUYgpQza1Nh0ucc42B64Ilw0rGhVflB%2BsqCLZry84ZdKXSL3dJHAVqi1GDahKnIZyDFBRsGwwcLZJSDCTRmBXVusPCtDB3E6CFRByelm%2B3l3sHpdhnKiHaDq7MFXFdfVECICQ0r2Nz7YIMEdhnsw%2B2QMzLTS1o%2F5z8lwjPrRevCAk8IC3SunBI12117cgbocUGOoz5eNfjns5BI1zd2%2B0pwWEAdPCivW1NVA%2FQWqUw45aEYaWJDPNz%2FOZwB0u8R%2FxbWfWrbMqgkaMQ0EQFPtM3FEITeePruoYmv1fO3ki5M7saOazZLQx%2FJJBiU3A6Kd6tCBhOJYn%2Fvq4EZ3i8KVgVl7AncbY8Rg6WLRdK7u1dZF4wdK%2B8vm%2BlDzxVWojhNAr4KZcXDbi%2FAEpkQ0bOrdhkNncvzGcYfGqJLEGIHBkVKoy4xIOk26FWHFCJmTHQ2zWv1RE%2BqHtxq%2FqhB70oB4Lyn5SZqLW5XgSs4aMNmcy42gSa5h1HkgRGFi4XCgVfD5BVt%2B4uYme0y8Fs0nMM%2BfcbDzD13Im9BjqkAfhoCUCl4gIrUAtihfMLD2EviAXhdZv9Btmkz956iPSRyGTbeXC%2FoMzfsiNBdhDQpf5elIYCGIgnVYvmLX4GhlzMylch10KoiWHjqQ8LO2HvyfZ0TKOL3ETYMrPHXl1xGYMLOh2FB8OsFcJ67%2FrGgJmt15O6S1h4AK0ibfb4ZM%2FrnMn8u7BKj74iq0HJ2v8QH4qp8HW9ArlbeUzz915%2BPdXtmDqP&X-Amz-Signature=60178c6a27844a1e7b2331c9f123f3855bf4afb7a9ce044cfc0455a19af0c597&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFXTPGB7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCBq4GQaAKxPQ%2Fb6CCD8LG3jMSfdtFxLjfxMaM2VmMOOQIhAJ3voteqoNjYRaC5T%2BFkgNuO22In6WVxM0f2mT9AWL7UKv8DCDUQABoMNjM3NDIzMTgzODA1IgyelHLpruTF1uCqrSsq3AM%2BYGGIAmwetn9%2B%2BvQd8hZZFQ1jd%2BA4NylVlykcI%2FnhMyIlGrS52Zp9VajH9N5rurx4jVKj9zKzEOvWb4g%2BAo0DDN0ULxkquAIR1ixUYgpQza1Nh0ucc42B64Ilw0rGhVflB%2BsqCLZry84ZdKXSL3dJHAVqi1GDahKnIZyDFBRsGwwcLZJSDCTRmBXVusPCtDB3E6CFRByelm%2B3l3sHpdhnKiHaDq7MFXFdfVECICQ0r2Nz7YIMEdhnsw%2B2QMzLTS1o%2F5z8lwjPrRevCAk8IC3SunBI12117cgbocUGOoz5eNfjns5BI1zd2%2B0pwWEAdPCivW1NVA%2FQWqUw45aEYaWJDPNz%2FOZwB0u8R%2FxbWfWrbMqgkaMQ0EQFPtM3FEITeePruoYmv1fO3ki5M7saOazZLQx%2FJJBiU3A6Kd6tCBhOJYn%2Fvq4EZ3i8KVgVl7AncbY8Rg6WLRdK7u1dZF4wdK%2B8vm%2BlDzxVWojhNAr4KZcXDbi%2FAEpkQ0bOrdhkNncvzGcYfGqJLEGIHBkVKoy4xIOk26FWHFCJmTHQ2zWv1RE%2BqHtxq%2FqhB70oB4Lyn5SZqLW5XgSs4aMNmcy42gSa5h1HkgRGFi4XCgVfD5BVt%2B4uYme0y8Fs0nMM%2BfcbDzD13Im9BjqkAfhoCUCl4gIrUAtihfMLD2EviAXhdZv9Btmkz956iPSRyGTbeXC%2FoMzfsiNBdhDQpf5elIYCGIgnVYvmLX4GhlzMylch10KoiWHjqQ8LO2HvyfZ0TKOL3ETYMrPHXl1xGYMLOh2FB8OsFcJ67%2FrGgJmt15O6S1h4AK0ibfb4ZM%2FrnMn8u7BKj74iq0HJ2v8QH4qp8HW9ArlbeUzz915%2BPdXtmDqP&X-Amz-Signature=4e4b2b895d658b540000bf98417871ee39982be27dfa3188a10a3b1c84e01d07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662CEKIYG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCz7gqYUBkjrhtMut%2F1JoFdz%2BFmzC1BDoPR2B7Pd5EoZAIgZUwariN1FaanpXktYGFYdejroYmx%2FzmuahKpAMxMU84q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDCs7%2FJ1VXFYyUNUz4SrcA9An1TCk3H%2FNhV%2BDOm4zQQ6ZtoLxAxipWCDvn5azIbYDvZEYhqMbpEjRkzQGrXpD0TlbylQvFT4vKRjJ44YqKc9YzqYUMT8lYeP40CS4u8swq%2BpUQAiPG7Tx4wzbmNzKj%2Fgyuy8oFyCt6ile%2Bu9eV2PvW9ZWPIlx03GEpP%2B3WnlHAYLlHxUfgf5tYwFWjdysaZr62QzOyBx4b5beffnJ6iWZz0iI1jbMd790lovpsfa9PD7DTugsPxUq85zuIEH6iHPX0jUSGsqRceX%2B23bMcpnr5dMmjStxEbMVyhlAs1i0ONjuv5Z9GsiOEXolMpyf1d4XhsA1A32qrsLMnMRgGCIGmzAd13zViez7EWBf8KBUds%2F2vDYh%2FLhfs6JqiDLdwK2L0iVgsqCftHzQl3q78L8YIt3HAwIiqT4O9Q7VMIBKDWZTzOLSEg44L5q7jfsYuQ5YU0%2BxMqDYIvvtShdnaaLBfHt%2FcuUHgt9lXmB9NBg3imdT%2BztU3eHszHiGiTYIo%2FsCHBYlcwUwAUr5H%2BBBXp%2FIxanS7bZtTphKyp59e7oBavaQuuVHC3lOTvyGO2D0Igrj6iUqiAQsNabh0YbtPaNfMskyGsOHKXd2CpDC%2FwIZ9roL27jqfQbQEibgMOLdib0GOqUB%2BT%2F3Gomks2j%2BbO0HSjplQaQLokwsS5nhh%2FnldyyJqtXRF1bZNeUWE6NyW3%2FWsapLisPxChpiylWAolXNKoQ0ue%2F8qqe6Y4g5Vs3yhUCp9146QeuJIKSFiS77oavNrpGlkaC22KtFB0z%2BySqLVTJqnZuDyztNBN79AVpulU3NqKmkP6GiMnj2Cp7ZPSoolnDfHnxjyGWYE5SIoeEtGAlPJUWDD%2FBr&X-Amz-Signature=75de1958a099798041eddac0903256b2062fd7b6d6807560c4194ebecc61fa37&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662CEKIYG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCz7gqYUBkjrhtMut%2F1JoFdz%2BFmzC1BDoPR2B7Pd5EoZAIgZUwariN1FaanpXktYGFYdejroYmx%2FzmuahKpAMxMU84q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDCs7%2FJ1VXFYyUNUz4SrcA9An1TCk3H%2FNhV%2BDOm4zQQ6ZtoLxAxipWCDvn5azIbYDvZEYhqMbpEjRkzQGrXpD0TlbylQvFT4vKRjJ44YqKc9YzqYUMT8lYeP40CS4u8swq%2BpUQAiPG7Tx4wzbmNzKj%2Fgyuy8oFyCt6ile%2Bu9eV2PvW9ZWPIlx03GEpP%2B3WnlHAYLlHxUfgf5tYwFWjdysaZr62QzOyBx4b5beffnJ6iWZz0iI1jbMd790lovpsfa9PD7DTugsPxUq85zuIEH6iHPX0jUSGsqRceX%2B23bMcpnr5dMmjStxEbMVyhlAs1i0ONjuv5Z9GsiOEXolMpyf1d4XhsA1A32qrsLMnMRgGCIGmzAd13zViez7EWBf8KBUds%2F2vDYh%2FLhfs6JqiDLdwK2L0iVgsqCftHzQl3q78L8YIt3HAwIiqT4O9Q7VMIBKDWZTzOLSEg44L5q7jfsYuQ5YU0%2BxMqDYIvvtShdnaaLBfHt%2FcuUHgt9lXmB9NBg3imdT%2BztU3eHszHiGiTYIo%2FsCHBYlcwUwAUr5H%2BBBXp%2FIxanS7bZtTphKyp59e7oBavaQuuVHC3lOTvyGO2D0Igrj6iUqiAQsNabh0YbtPaNfMskyGsOHKXd2CpDC%2FwIZ9roL27jqfQbQEibgMOLdib0GOqUB%2BT%2F3Gomks2j%2BbO0HSjplQaQLokwsS5nhh%2FnldyyJqtXRF1bZNeUWE6NyW3%2FWsapLisPxChpiylWAolXNKoQ0ue%2F8qqe6Y4g5Vs3yhUCp9146QeuJIKSFiS77oavNrpGlkaC22KtFB0z%2BySqLVTJqnZuDyztNBN79AVpulU3NqKmkP6GiMnj2Cp7ZPSoolnDfHnxjyGWYE5SIoeEtGAlPJUWDD%2FBr&X-Amz-Signature=62e6d65203c270f01a977d2bb4315d27914ebc91d5e29a0a34f578fa7a2c3c45&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662CEKIYG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCz7gqYUBkjrhtMut%2F1JoFdz%2BFmzC1BDoPR2B7Pd5EoZAIgZUwariN1FaanpXktYGFYdejroYmx%2FzmuahKpAMxMU84q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDCs7%2FJ1VXFYyUNUz4SrcA9An1TCk3H%2FNhV%2BDOm4zQQ6ZtoLxAxipWCDvn5azIbYDvZEYhqMbpEjRkzQGrXpD0TlbylQvFT4vKRjJ44YqKc9YzqYUMT8lYeP40CS4u8swq%2BpUQAiPG7Tx4wzbmNzKj%2Fgyuy8oFyCt6ile%2Bu9eV2PvW9ZWPIlx03GEpP%2B3WnlHAYLlHxUfgf5tYwFWjdysaZr62QzOyBx4b5beffnJ6iWZz0iI1jbMd790lovpsfa9PD7DTugsPxUq85zuIEH6iHPX0jUSGsqRceX%2B23bMcpnr5dMmjStxEbMVyhlAs1i0ONjuv5Z9GsiOEXolMpyf1d4XhsA1A32qrsLMnMRgGCIGmzAd13zViez7EWBf8KBUds%2F2vDYh%2FLhfs6JqiDLdwK2L0iVgsqCftHzQl3q78L8YIt3HAwIiqT4O9Q7VMIBKDWZTzOLSEg44L5q7jfsYuQ5YU0%2BxMqDYIvvtShdnaaLBfHt%2FcuUHgt9lXmB9NBg3imdT%2BztU3eHszHiGiTYIo%2FsCHBYlcwUwAUr5H%2BBBXp%2FIxanS7bZtTphKyp59e7oBavaQuuVHC3lOTvyGO2D0Igrj6iUqiAQsNabh0YbtPaNfMskyGsOHKXd2CpDC%2FwIZ9roL27jqfQbQEibgMOLdib0GOqUB%2BT%2F3Gomks2j%2BbO0HSjplQaQLokwsS5nhh%2FnldyyJqtXRF1bZNeUWE6NyW3%2FWsapLisPxChpiylWAolXNKoQ0ue%2F8qqe6Y4g5Vs3yhUCp9146QeuJIKSFiS77oavNrpGlkaC22KtFB0z%2BySqLVTJqnZuDyztNBN79AVpulU3NqKmkP6GiMnj2Cp7ZPSoolnDfHnxjyGWYE5SIoeEtGAlPJUWDD%2FBr&X-Amz-Signature=e21b1b0c8a11f0fe9ee580c3f58065aea4e158ff0bd8dc81d1122dea8bc46f8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662CEKIYG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCz7gqYUBkjrhtMut%2F1JoFdz%2BFmzC1BDoPR2B7Pd5EoZAIgZUwariN1FaanpXktYGFYdejroYmx%2FzmuahKpAMxMU84q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDCs7%2FJ1VXFYyUNUz4SrcA9An1TCk3H%2FNhV%2BDOm4zQQ6ZtoLxAxipWCDvn5azIbYDvZEYhqMbpEjRkzQGrXpD0TlbylQvFT4vKRjJ44YqKc9YzqYUMT8lYeP40CS4u8swq%2BpUQAiPG7Tx4wzbmNzKj%2Fgyuy8oFyCt6ile%2Bu9eV2PvW9ZWPIlx03GEpP%2B3WnlHAYLlHxUfgf5tYwFWjdysaZr62QzOyBx4b5beffnJ6iWZz0iI1jbMd790lovpsfa9PD7DTugsPxUq85zuIEH6iHPX0jUSGsqRceX%2B23bMcpnr5dMmjStxEbMVyhlAs1i0ONjuv5Z9GsiOEXolMpyf1d4XhsA1A32qrsLMnMRgGCIGmzAd13zViez7EWBf8KBUds%2F2vDYh%2FLhfs6JqiDLdwK2L0iVgsqCftHzQl3q78L8YIt3HAwIiqT4O9Q7VMIBKDWZTzOLSEg44L5q7jfsYuQ5YU0%2BxMqDYIvvtShdnaaLBfHt%2FcuUHgt9lXmB9NBg3imdT%2BztU3eHszHiGiTYIo%2FsCHBYlcwUwAUr5H%2BBBXp%2FIxanS7bZtTphKyp59e7oBavaQuuVHC3lOTvyGO2D0Igrj6iUqiAQsNabh0YbtPaNfMskyGsOHKXd2CpDC%2FwIZ9roL27jqfQbQEibgMOLdib0GOqUB%2BT%2F3Gomks2j%2BbO0HSjplQaQLokwsS5nhh%2FnldyyJqtXRF1bZNeUWE6NyW3%2FWsapLisPxChpiylWAolXNKoQ0ue%2F8qqe6Y4g5Vs3yhUCp9146QeuJIKSFiS77oavNrpGlkaC22KtFB0z%2BySqLVTJqnZuDyztNBN79AVpulU3NqKmkP6GiMnj2Cp7ZPSoolnDfHnxjyGWYE5SIoeEtGAlPJUWDD%2FBr&X-Amz-Signature=f51cc1fab7065244894eb0cda080b0e4970c800ab081f98b39f2fe1d75cd728a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662CEKIYG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCz7gqYUBkjrhtMut%2F1JoFdz%2BFmzC1BDoPR2B7Pd5EoZAIgZUwariN1FaanpXktYGFYdejroYmx%2FzmuahKpAMxMU84q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDCs7%2FJ1VXFYyUNUz4SrcA9An1TCk3H%2FNhV%2BDOm4zQQ6ZtoLxAxipWCDvn5azIbYDvZEYhqMbpEjRkzQGrXpD0TlbylQvFT4vKRjJ44YqKc9YzqYUMT8lYeP40CS4u8swq%2BpUQAiPG7Tx4wzbmNzKj%2Fgyuy8oFyCt6ile%2Bu9eV2PvW9ZWPIlx03GEpP%2B3WnlHAYLlHxUfgf5tYwFWjdysaZr62QzOyBx4b5beffnJ6iWZz0iI1jbMd790lovpsfa9PD7DTugsPxUq85zuIEH6iHPX0jUSGsqRceX%2B23bMcpnr5dMmjStxEbMVyhlAs1i0ONjuv5Z9GsiOEXolMpyf1d4XhsA1A32qrsLMnMRgGCIGmzAd13zViez7EWBf8KBUds%2F2vDYh%2FLhfs6JqiDLdwK2L0iVgsqCftHzQl3q78L8YIt3HAwIiqT4O9Q7VMIBKDWZTzOLSEg44L5q7jfsYuQ5YU0%2BxMqDYIvvtShdnaaLBfHt%2FcuUHgt9lXmB9NBg3imdT%2BztU3eHszHiGiTYIo%2FsCHBYlcwUwAUr5H%2BBBXp%2FIxanS7bZtTphKyp59e7oBavaQuuVHC3lOTvyGO2D0Igrj6iUqiAQsNabh0YbtPaNfMskyGsOHKXd2CpDC%2FwIZ9roL27jqfQbQEibgMOLdib0GOqUB%2BT%2F3Gomks2j%2BbO0HSjplQaQLokwsS5nhh%2FnldyyJqtXRF1bZNeUWE6NyW3%2FWsapLisPxChpiylWAolXNKoQ0ue%2F8qqe6Y4g5Vs3yhUCp9146QeuJIKSFiS77oavNrpGlkaC22KtFB0z%2BySqLVTJqnZuDyztNBN79AVpulU3NqKmkP6GiMnj2Cp7ZPSoolnDfHnxjyGWYE5SIoeEtGAlPJUWDD%2FBr&X-Amz-Signature=1398337bbf1ca1f3c2e8fba5822ef80752e3d643440977119371a6586d635674&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662CEKIYG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCz7gqYUBkjrhtMut%2F1JoFdz%2BFmzC1BDoPR2B7Pd5EoZAIgZUwariN1FaanpXktYGFYdejroYmx%2FzmuahKpAMxMU84q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDCs7%2FJ1VXFYyUNUz4SrcA9An1TCk3H%2FNhV%2BDOm4zQQ6ZtoLxAxipWCDvn5azIbYDvZEYhqMbpEjRkzQGrXpD0TlbylQvFT4vKRjJ44YqKc9YzqYUMT8lYeP40CS4u8swq%2BpUQAiPG7Tx4wzbmNzKj%2Fgyuy8oFyCt6ile%2Bu9eV2PvW9ZWPIlx03GEpP%2B3WnlHAYLlHxUfgf5tYwFWjdysaZr62QzOyBx4b5beffnJ6iWZz0iI1jbMd790lovpsfa9PD7DTugsPxUq85zuIEH6iHPX0jUSGsqRceX%2B23bMcpnr5dMmjStxEbMVyhlAs1i0ONjuv5Z9GsiOEXolMpyf1d4XhsA1A32qrsLMnMRgGCIGmzAd13zViez7EWBf8KBUds%2F2vDYh%2FLhfs6JqiDLdwK2L0iVgsqCftHzQl3q78L8YIt3HAwIiqT4O9Q7VMIBKDWZTzOLSEg44L5q7jfsYuQ5YU0%2BxMqDYIvvtShdnaaLBfHt%2FcuUHgt9lXmB9NBg3imdT%2BztU3eHszHiGiTYIo%2FsCHBYlcwUwAUr5H%2BBBXp%2FIxanS7bZtTphKyp59e7oBavaQuuVHC3lOTvyGO2D0Igrj6iUqiAQsNabh0YbtPaNfMskyGsOHKXd2CpDC%2FwIZ9roL27jqfQbQEibgMOLdib0GOqUB%2BT%2F3Gomks2j%2BbO0HSjplQaQLokwsS5nhh%2FnldyyJqtXRF1bZNeUWE6NyW3%2FWsapLisPxChpiylWAolXNKoQ0ue%2F8qqe6Y4g5Vs3yhUCp9146QeuJIKSFiS77oavNrpGlkaC22KtFB0z%2BySqLVTJqnZuDyztNBN79AVpulU3NqKmkP6GiMnj2Cp7ZPSoolnDfHnxjyGWYE5SIoeEtGAlPJUWDD%2FBr&X-Amz-Signature=313dd7460fb7cd943c47f538b93c845e1b5765a443de61530a3454101328cd0d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AXWGC6E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDQUkS1HUWe11gVGAkROfan6%2BbfbE%2FNQcqvZFF%2FAK8LXAIhAKOoD8EWqJats%2BlByl2Szrajirjimg2eEpnVapu7U6pkKv8DCDUQABoMNjM3NDIzMTgzODA1IgzSDisN4sbq2YtP9kMq3APp4Q2be1q2um76bwTkJhuujZ4wvA2QZW4ND64%2FKdlOeoANFX88FA0hYuccY6qXxD3z8fT8IZI%2FDWrCITQhRRrVcgboEP7Lm6WBYyEudcyTIOX8zoWpvIdPP%2BnPAWnIMYqgISAEDicEEW%2FOKhHsxv1dtDzT4dS5yhux669Mi3NMbgazv8geZVNq%2Bd8jVTaT3QIeoipA%2BsxrjXtkGQ%2BOcNswIXFXSB7fif93LwXXb97eVEtXA9ebNyjZ6suN7b5FRNmgYXlq0LZT%2FHJiKjSspOABhnu5PojDbKKVyu%2FjJFSoqaN7OlyMxjYV2jM%2Fi2dudjHEtyUBgTXxlf0QTwkGzgIvdkKOWUQmD29zde53gYqgnMM1yFLMmNE9yubsZqIVDX95o%2BlN3cODmQq5uZmsYG42Q5lzQGcdQ9EpJNjP93PvVwhkI4GUTjY9d%2B4ZeszOF%2BO0ZIj1TNueIYXTzRQyhQ49bldQkv%2FCHU9TWy0qXLl0Xrz4eH2%2Bin91bUlnbkTjuxjrqm6xu3CxjqMkhvr318Sp7wDCbBw0D6vvGaFM9M2QvTfCFNN8CXc2i5XBG0F6O%2FhwLy7CMbTas3haQxoYqVUL1vOYSu%2BkvrcUJyo9YaIs%2F%2FatC4OuPzFOn7DwaTC%2B3Ym9BjqkAV0LaheUw0xgUZAdBBLr%2FxN2HFObDAJldS2bs3QMLm3T0v752sigfWdVtShDB1Dql0i%2B1GM8twNXdoaScHYIRauaJ7fTwzrmWCePCsKZUx%2BW5npLzC6ontShKfd0AD573wB%2FnzielTphPyx%2BpS5mmXnj1fdx84FRLy0KyV%2FHkX5OvF8CbsAGQbFP6oygQVOpfpYl%2F%2FKI3N%2Fs7BbPdoVwO%2BR34Rat&X-Amz-Signature=c836eb87f45db63b29ad591587acae013aa86b43e81bb92d0a7c64d88bc3584f&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BSVTXPN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGRcnYDpkpRUGNkwb2Jb0Rtc%2B7YNkUWCp6Uz7yrzpnDSAiApMVQLsJVE%2BbQGSEW0nWHw%2FaTm%2FTK%2Fe5wgrc8pUZOWUyr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMI6sslna%2BIMCvlCKcKtwDMoKpalyB3WdCp8kpmrZqP5Dpxoua%2BgGXIakJZ%2BP6b3icJW8emZbmit2WrO7tNJWUHvG%2BaXssvDMLYFwFZBT3vdUXTk5qePqb8PGiDOzNJ36teFVv6LD1oRvzba9ve5Bg%2B0hl0pKzxCWO17ABYNVzZjmB2hFDZD%2Fmx7q4mFYow4adRxfH5YE4q4bjy8HSHGcO5SgzUXPYy6dwjXUnX8Q3mCbiD%2F3fw6R6XyHyPo9aY%2B5KYVKiwTvZtztNxXi1R8fRyp5kaSFDBvPnfujmk50Km472a1%2BRmHAUH825SsBe4v3RDGnPfPrU5gxktNJEFAZJc6i5B4o7XIfW4iSIKWPcblOp4knSpG7HCrw1eOBJ6b71nNVu57nlzx%2Fc2FH7SZGYSHKU90UKSE8vPz1XqcXGXiL75AQj%2BzEt7FGUr56FSHxpYSPdDHVDTJhRyNv5g6bFecT6HcVIpC1epglXcs9TRzXto2PNePRq63Gafjq3E%2BXvfqIFI%2FI98M09mX4jO8bmHUFZT5RrIUqDf1xXbw61P89LHKfOrAk1m5q1LXAbuZI0kWCgNmAz%2FnN42nKAdDMhXbrwKJAIurj2F9cQVEGAD1Xg8rgBfbe7Gqh1TdR5Jd7tPtj82hml%2BG19FDEw6NyJvQY6pgGkblb6XWNUdXadMX1eAlNBZW7XYl6Qwmr6YvoYe0dvbIlSeuL2Ng3p8A%2BVn2g9ct9hYL%2BZ01IXIGsTW7P%2B4ljIqgKjRkcfLyG2BmiSpSE%2BL28zzoQsUbyh8cK8U%2BXh9SV25RGB7wjkUL5sDF2IzC9RzLzCNbF2Jn0N%2BREQtcUPxmBQxbLVzU%2BCIJJ9B8XjEH%2BJFXwDipI1If3CpycXC%2F5UwOgwZ2xQ&X-Amz-Signature=edb385e1ce889ade9b514d24e68cd5fec37abf2ec47e5155585eb22d6d2ac27e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662CEKIYG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCz7gqYUBkjrhtMut%2F1JoFdz%2BFmzC1BDoPR2B7Pd5EoZAIgZUwariN1FaanpXktYGFYdejroYmx%2FzmuahKpAMxMU84q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDCs7%2FJ1VXFYyUNUz4SrcA9An1TCk3H%2FNhV%2BDOm4zQQ6ZtoLxAxipWCDvn5azIbYDvZEYhqMbpEjRkzQGrXpD0TlbylQvFT4vKRjJ44YqKc9YzqYUMT8lYeP40CS4u8swq%2BpUQAiPG7Tx4wzbmNzKj%2Fgyuy8oFyCt6ile%2Bu9eV2PvW9ZWPIlx03GEpP%2B3WnlHAYLlHxUfgf5tYwFWjdysaZr62QzOyBx4b5beffnJ6iWZz0iI1jbMd790lovpsfa9PD7DTugsPxUq85zuIEH6iHPX0jUSGsqRceX%2B23bMcpnr5dMmjStxEbMVyhlAs1i0ONjuv5Z9GsiOEXolMpyf1d4XhsA1A32qrsLMnMRgGCIGmzAd13zViez7EWBf8KBUds%2F2vDYh%2FLhfs6JqiDLdwK2L0iVgsqCftHzQl3q78L8YIt3HAwIiqT4O9Q7VMIBKDWZTzOLSEg44L5q7jfsYuQ5YU0%2BxMqDYIvvtShdnaaLBfHt%2FcuUHgt9lXmB9NBg3imdT%2BztU3eHszHiGiTYIo%2FsCHBYlcwUwAUr5H%2BBBXp%2FIxanS7bZtTphKyp59e7oBavaQuuVHC3lOTvyGO2D0Igrj6iUqiAQsNabh0YbtPaNfMskyGsOHKXd2CpDC%2FwIZ9roL27jqfQbQEibgMOLdib0GOqUB%2BT%2F3Gomks2j%2BbO0HSjplQaQLokwsS5nhh%2FnldyyJqtXRF1bZNeUWE6NyW3%2FWsapLisPxChpiylWAolXNKoQ0ue%2F8qqe6Y4g5Vs3yhUCp9146QeuJIKSFiS77oavNrpGlkaC22KtFB0z%2BySqLVTJqnZuDyztNBN79AVpulU3NqKmkP6GiMnj2Cp7ZPSoolnDfHnxjyGWYE5SIoeEtGAlPJUWDD%2FBr&X-Amz-Signature=e124c4540c9fa49021c951277305bc75a025c70d2bdf9b0fe6b2fd8ee68dd54c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662CEKIYG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCz7gqYUBkjrhtMut%2F1JoFdz%2BFmzC1BDoPR2B7Pd5EoZAIgZUwariN1FaanpXktYGFYdejroYmx%2FzmuahKpAMxMU84q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDCs7%2FJ1VXFYyUNUz4SrcA9An1TCk3H%2FNhV%2BDOm4zQQ6ZtoLxAxipWCDvn5azIbYDvZEYhqMbpEjRkzQGrXpD0TlbylQvFT4vKRjJ44YqKc9YzqYUMT8lYeP40CS4u8swq%2BpUQAiPG7Tx4wzbmNzKj%2Fgyuy8oFyCt6ile%2Bu9eV2PvW9ZWPIlx03GEpP%2B3WnlHAYLlHxUfgf5tYwFWjdysaZr62QzOyBx4b5beffnJ6iWZz0iI1jbMd790lovpsfa9PD7DTugsPxUq85zuIEH6iHPX0jUSGsqRceX%2B23bMcpnr5dMmjStxEbMVyhlAs1i0ONjuv5Z9GsiOEXolMpyf1d4XhsA1A32qrsLMnMRgGCIGmzAd13zViez7EWBf8KBUds%2F2vDYh%2FLhfs6JqiDLdwK2L0iVgsqCftHzQl3q78L8YIt3HAwIiqT4O9Q7VMIBKDWZTzOLSEg44L5q7jfsYuQ5YU0%2BxMqDYIvvtShdnaaLBfHt%2FcuUHgt9lXmB9NBg3imdT%2BztU3eHszHiGiTYIo%2FsCHBYlcwUwAUr5H%2BBBXp%2FIxanS7bZtTphKyp59e7oBavaQuuVHC3lOTvyGO2D0Igrj6iUqiAQsNabh0YbtPaNfMskyGsOHKXd2CpDC%2FwIZ9roL27jqfQbQEibgMOLdib0GOqUB%2BT%2F3Gomks2j%2BbO0HSjplQaQLokwsS5nhh%2FnldyyJqtXRF1bZNeUWE6NyW3%2FWsapLisPxChpiylWAolXNKoQ0ue%2F8qqe6Y4g5Vs3yhUCp9146QeuJIKSFiS77oavNrpGlkaC22KtFB0z%2BySqLVTJqnZuDyztNBN79AVpulU3NqKmkP6GiMnj2Cp7ZPSoolnDfHnxjyGWYE5SIoeEtGAlPJUWDD%2FBr&X-Amz-Signature=3f126e92d1c8e68aff125833a2eb3573c9295c77cd0c710dbfe3e1cc3d98fbb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662CEKIYG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCz7gqYUBkjrhtMut%2F1JoFdz%2BFmzC1BDoPR2B7Pd5EoZAIgZUwariN1FaanpXktYGFYdejroYmx%2FzmuahKpAMxMU84q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDCs7%2FJ1VXFYyUNUz4SrcA9An1TCk3H%2FNhV%2BDOm4zQQ6ZtoLxAxipWCDvn5azIbYDvZEYhqMbpEjRkzQGrXpD0TlbylQvFT4vKRjJ44YqKc9YzqYUMT8lYeP40CS4u8swq%2BpUQAiPG7Tx4wzbmNzKj%2Fgyuy8oFyCt6ile%2Bu9eV2PvW9ZWPIlx03GEpP%2B3WnlHAYLlHxUfgf5tYwFWjdysaZr62QzOyBx4b5beffnJ6iWZz0iI1jbMd790lovpsfa9PD7DTugsPxUq85zuIEH6iHPX0jUSGsqRceX%2B23bMcpnr5dMmjStxEbMVyhlAs1i0ONjuv5Z9GsiOEXolMpyf1d4XhsA1A32qrsLMnMRgGCIGmzAd13zViez7EWBf8KBUds%2F2vDYh%2FLhfs6JqiDLdwK2L0iVgsqCftHzQl3q78L8YIt3HAwIiqT4O9Q7VMIBKDWZTzOLSEg44L5q7jfsYuQ5YU0%2BxMqDYIvvtShdnaaLBfHt%2FcuUHgt9lXmB9NBg3imdT%2BztU3eHszHiGiTYIo%2FsCHBYlcwUwAUr5H%2BBBXp%2FIxanS7bZtTphKyp59e7oBavaQuuVHC3lOTvyGO2D0Igrj6iUqiAQsNabh0YbtPaNfMskyGsOHKXd2CpDC%2FwIZ9roL27jqfQbQEibgMOLdib0GOqUB%2BT%2F3Gomks2j%2BbO0HSjplQaQLokwsS5nhh%2FnldyyJqtXRF1bZNeUWE6NyW3%2FWsapLisPxChpiylWAolXNKoQ0ue%2F8qqe6Y4g5Vs3yhUCp9146QeuJIKSFiS77oavNrpGlkaC22KtFB0z%2BySqLVTJqnZuDyztNBN79AVpulU3NqKmkP6GiMnj2Cp7ZPSoolnDfHnxjyGWYE5SIoeEtGAlPJUWDD%2FBr&X-Amz-Signature=a48a52c3fad10d75a23bd79e4e71bade42357507dacf80340e0e623a29912af5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TFXPIQP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCLKSK2%2Bwsi6wvIfjvoswYlEoDPZRlbluKj1q62ZEMdXwIgUgIazkbGTaI6J%2FrplOFZ44osdUeZYr2dgs77OR%2FuiLEq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDE%2F1DtLkBxUNRiMwtyrcA4jtaRJYGPcNVVrTk3ZG159G6z3zTONrJLLjgIjyb0F02xeAY9cUxDloft2M3%2BvtzKFSgyT5PTtpF%2FsURBHMl1SSiiaYGQJTtpqNRq3qTPtrz8S30v8KsKcN3hPVcgjLi9Ic%2FzJCpGu831fXtmBx76t5PBUrbd65ap1KNunF3CT69SKwG9suPE3JaI%2FBN15Ln7oHc92yLSOdtqwwzdpOaggghfrJL4HL9OhaawckUl5CXymQN25opV3UstZLdxOc7BS0ZTt708E2WEHr701uuo3Z5cMUiQerQ4hBpwch6TlgsKxa7kwfcWLU2zLxU1x0nwE0k1yUMPmw0adDbLxCfChRdWzt32c3NbWzbu%2BbO7oE66RKR0Cv%2F1IwuPTwoKJ9IAxiZeEfLR%2BvL%2F1CyneYmzbpk9uuZv0zTnXWaLxNlNsD2EBPUmbnW42sAz3znwMns4n3xNF0g7RAehbBEHBeciRsWcOMyUBN5z4qKACVmJ500rcS%2FIGoAWAq8HnOjKKlYWAgyvxdtycYv7aWFpp8zPS%2F%2Ftf4120ptXlTSLJasfGAVJ6RCQY3rvgDjsub3W4H1F3%2BDHWp94nKF6fq08MkXZmDHnNyWPPcslwZ5wZ6PRnaQ%2BgJHjMVPEDzf4DtMPHcib0GOqUB5ghAvHDGFLPNoSbKTNperBP6bkwkVCbEfYNuxVQL6Crpz31oZ4R2NBHDTxCx7nsqXMPIR3dR7D2aD%2FWtNjhbtn5NeXN0vMkAkj025l7wJtcNWKhy9fMjpOoBmdFSz30lyR%2Fbd2xuORBwXQ9v1qvmot7lYP3z1VHy6pRpKBaIRD6NunQM5JNJPQqkZV4ce%2FuUFKAPXpqiOkhE9lfI4mfXDptp50ur&X-Amz-Signature=57cb1a8d7831dbc1ad948ad70419e62ad564d0c6e6e494582248075ed22ee600&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVUNTTHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQDUOSJ%2BCP5O6nTOJuxrG%2F0xnBiUXWYiHYm4vOWyJX%2FbfAIgaYkKRT7ThtsTwjixSOOwCRQ50oaKUcYKZvtsPDWdUGoq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDE0ktv%2FHR%2FqiP1K5XyrcA3coXNdfmwOfiaid4w5GqnyEpqyQQklT8Biia02iyD%2FWDMjb3RVr24ySjbl4yoE%2FfESoqOKaG26r%2F5xAIaRJ86CXLHfRp%2FlaU2x2OKCU%2FRc6E2VghZ76IwooUaFk9GeicbaSIgEQfe1N8dXmIyxujUtYGxrHnwpIP%2FSuJko12XuPlDRD%2F6zR%2FrRsfGX5C%2Byka45j7o8N7UBiv4NNig5nTrqrkC1KKQinpEC1zcyjNVvco%2FQMP%2B0mIGCmRrtmiMavRqoaTxlHqoI7b5Sq4CKLSkSmmxNpL2EYi7RFQM%2BsIpo3mpPMs5EWx44DZWca5NU8vqxVheJ56bQhroB9dUazPelj1QiHOykeVagxWEL3q7A1jXYxhALXwRS7dlPrFZpanYO7JIEOrJ8pKwQRRPhNA9zr7E9EtbB%2BrNwORVb3zQjevTJAQIXjaETfDlXZKU5FVeWQWSkzJ%2FRibf%2BmrbKgLDqw6s4DMy3X0cKOCss9hcInuOYxsZWjnVIz%2B17Mi1FQbEKMC8v%2FOTu37fiUwvB0SUKMnd000BOyQRB5iPaeE9AK%2B3JeshPB1bBjsbtJgteytVYT0g6IIORMzEYBL8vYc%2BYkt1TUakxt%2Bp9zWzO7R6vCR8G7rrRGB78%2FX3EUMNzcib0GOqUBndDePhRI3VFhEac%2BbxR5W4TVw1tJwnaZhRP2hE6uswGPHzBN%2B%2B1hghgFFG0JFs2n3Y0W4UY89rEDqdIbMBGnI99dhl1nZFtnCEM4Px%2BW3xTBBzs4QB6XEqgYVg%2FAd0yH54cx5A8u3NRVne4rxa9mLfVJCPmWJ5gkxL07LT71eCDNO5wipAwarZqBTrjKulTqGAyX6nnb59kgekLGKyw4Y5L8B6Di&X-Amz-Signature=3ce5ec60717c8d3a46f63f021a4710ebaf53465187af87ccdf21087c061bba4c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SACWVI3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCfWeXXvHGEkYyWe8KFLuPjp2CFNRzTRoe2m3qfhmWYdgIhALi1djRc5RwEbVkG6kiGpeT1bBOPZvdiISk5qtfVw%2FdTKv8DCDUQABoMNjM3NDIzMTgzODA1IgwUViXhWXWX%2FNqKqUQq3APooYJ83B8iOgykGroUYrvrdNhOpdOaYk7%2FjO0vnkjr25OsAqlrLZftg67F9PvPZm3Ah3rA940wphNnwtbS6jlfcCnh1WuQi%2FPKD2iVs78JL%2BXX%2BrAa%2B7ETfBBbF2IN4uLvpV11t14fsOtVJ3Qr1IiAoX3zyij2X3YnOXOV2DvpeNLuilMHSKf%2BTwQwZwiqoxA0aHZbr%2FkLWJoWI1cH23Rxm3%2FXhL504b%2BtmpBIx1%2F5FZMuVw58HJAnmVK4ASTsg4dPmR2EV%2BX54tuTP1Ww5Gu1nCuLVBdowKmtFww9cxsNSz43cBBdGlZkJzbmdf6YfPN7Z3Ui1r2Siwk%2FDTg9SuNyAsoHUsl6gK%2B%2Blv0btnN5a9coSHGW91KNPjifQftaLoZNkDZrjKNB4EJm68R%2FvBO3V6ODHsGkUgBt6gPnAqF1WpuLWlmSp5QqLDlRRm1%2FhnLOYC1CNj6mNme4hvqV%2Bq5T8ykd7jCNDCl2ESlms43cK63JLUZ1NGABize%2FGlDttwQjlU%2FczEcnVH9gaUMq20Qzfwuo%2F0MEPpn15pbijh1XAxV5J8%2BLI2MDSo38xRKqir1ercEw6HWyEatxry9y8FDJXzbNQCx%2BIefg0XVdwHJ4jumii9X99F2wn%2FY6dzDl3Im9BjqkAXl0kyEbzOyyOCTF9p46uRNIuiF%2FoixrnN1AHwMcNk9VdVsXr3Yfqd%2FbEWmLpIQ9QNOPJfMgdjXchKJv98CO5NkAISC6Va7xqXhAskgwwovMxNxqY5pTI1AF%2FfX5YxMg9%2BK%2BX7vl%2FDC8jzHObrrd5nkBUqh0bT%2BSNIvDuLU3wweLym6fP80NSASB5zUsVfcWTJQVdQZ%2F6uDgVERU6fwG73jHets9&X-Amz-Signature=dc4a009a6a6f6bafad8dd75d35c46d9173ed98a9142e9d6b0ab589b959326a1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MDMN2D2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGWxuGODjr0P7FgJOCAmWuYpExJmHKuQBDtSJCHm6pMpAiA0%2FH%2BGAohm%2FWAvgnqRrhasJm5knOvvdmz2FOI6TOr%2BYir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMK52UpKBMbeYRssIZKtwDY7Bk9gZMKXHg%2BU0XFv2RKIPrCnW6vP6tWuTU%2FKLzOX8m3AySwdUQVIgP8pfN5%2FSnBdNPMfD%2BfNe6IMK5J%2FHlUVyPqncMmo6xO1poMrXRNEE3zrH3P5tt1dBG9ZRVorcaV4%2FVwbS%2FRANfjCb7MjC8F30ZhIXUkPpwg%2FGSs8fd528RQUeKEp6VT7Ky0RQPS0ProjkhyamlWpCEPNF8Dn8HCol29HzAZuv54KiBWszVOS%2FUW8w1iW%2BaoS3iA2zxHtK3%2FUeR2H55YXnw3zySPSVXy5aQqqzaPA%2B4TZmMJ1xsF9ulqY%2F0BYHZ8VYCLbn1SJoup3GNrfkuTZ9ewe6cEcLjWnhnLgtoGBfG%2FRFNoAHxJOrl3HSdLa7td%2BL1ZjPbvkG9%2FjwpW4AKLlwwT9EflsUysq7cD5N%2BWJxTVgbwIfxMAYjGNbgCWdEG9b7yvhtMx3GCJOH7Qzjcr%2FgfbneHZiSFLkRbv5WKjTMoPbi%2F1su4gvU12JZfNxjWGHiHMp1Llg%2BUPGC5TzV9k7hXbHHPAG2LEj6mnhg7ZGtn6xNuWJWoFLXHGtakhgW1wMid9VfjjazXCrBQ6ZSkdPyu7ft9YbpSOmY9t0%2FeETsVLUKn5WgPX%2BiLrsOkkiVZw6D6qTgwv92JvQY6pgGDRvYNS8DTzGxe25wOArWKc4Xqzm5Ijq6BwyshDPtp10a%2FPhuF3EfHyy9KtOYRpq7CpY4qX%2FnrtWa5iA25arQgoWB8AzChOG7xhGwAyJSdvllZtN4f3AB2lJlPXZ3%2FuDpN%2B4LEagqTXLj0iUIQM8UOcQKZGbtV1U4JbLA6Jap6sA0lLullGVQrJVkvORhaQBRsIK4PRcu2ISC%2BdsPvlJDuIx00b8jM&X-Amz-Signature=838dc718c6dd74a77d9165e3c28bf6b3d875d669507ddb546794e5e099b855e7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MDMN2D2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIGWxuGODjr0P7FgJOCAmWuYpExJmHKuQBDtSJCHm6pMpAiA0%2FH%2BGAohm%2FWAvgnqRrhasJm5knOvvdmz2FOI6TOr%2BYir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMK52UpKBMbeYRssIZKtwDY7Bk9gZMKXHg%2BU0XFv2RKIPrCnW6vP6tWuTU%2FKLzOX8m3AySwdUQVIgP8pfN5%2FSnBdNPMfD%2BfNe6IMK5J%2FHlUVyPqncMmo6xO1poMrXRNEE3zrH3P5tt1dBG9ZRVorcaV4%2FVwbS%2FRANfjCb7MjC8F30ZhIXUkPpwg%2FGSs8fd528RQUeKEp6VT7Ky0RQPS0ProjkhyamlWpCEPNF8Dn8HCol29HzAZuv54KiBWszVOS%2FUW8w1iW%2BaoS3iA2zxHtK3%2FUeR2H55YXnw3zySPSVXy5aQqqzaPA%2B4TZmMJ1xsF9ulqY%2F0BYHZ8VYCLbn1SJoup3GNrfkuTZ9ewe6cEcLjWnhnLgtoGBfG%2FRFNoAHxJOrl3HSdLa7td%2BL1ZjPbvkG9%2FjwpW4AKLlwwT9EflsUysq7cD5N%2BWJxTVgbwIfxMAYjGNbgCWdEG9b7yvhtMx3GCJOH7Qzjcr%2FgfbneHZiSFLkRbv5WKjTMoPbi%2F1su4gvU12JZfNxjWGHiHMp1Llg%2BUPGC5TzV9k7hXbHHPAG2LEj6mnhg7ZGtn6xNuWJWoFLXHGtakhgW1wMid9VfjjazXCrBQ6ZSkdPyu7ft9YbpSOmY9t0%2FeETsVLUKn5WgPX%2BiLrsOkkiVZw6D6qTgwv92JvQY6pgGDRvYNS8DTzGxe25wOArWKc4Xqzm5Ijq6BwyshDPtp10a%2FPhuF3EfHyy9KtOYRpq7CpY4qX%2FnrtWa5iA25arQgoWB8AzChOG7xhGwAyJSdvllZtN4f3AB2lJlPXZ3%2FuDpN%2B4LEagqTXLj0iUIQM8UOcQKZGbtV1U4JbLA6Jap6sA0lLullGVQrJVkvORhaQBRsIK4PRcu2ISC%2BdsPvlJDuIx00b8jM&X-Amz-Signature=f3d406e983db2edf9512f765c6492eae5d378ee7344826132c774f1609213d3b&X-Amz-SignedHeaders=host&x-id=GetObject)

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
