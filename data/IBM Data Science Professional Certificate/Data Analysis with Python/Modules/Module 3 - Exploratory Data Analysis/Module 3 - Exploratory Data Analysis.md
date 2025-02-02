

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTUOQI4F%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzj6k8TIZHkzBv6Z4AiYNzPnOff17d2i1WuCRuMK1%2BMAiEAscNlECRVN3g0dAbXLzMz9Ryc1efiNhWbGvB6ynmYu88qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIkQLb%2Fs3Y%2F3hSmJgircA4oEv%2BJ2vlMcYdSCNUHj0uRI75os6itVdnQdzerLit5PTKR2gTOvOsnAGndqHDMhadHEn1n%2FcwL43UEPHOmBfmtuG3bnr8%2BhTSNg%2BQnQLNAySrM74BRQYeBM9rHSAwwAPR4eWW10t02QsK4N68Lsw9uyqyuanVrYV1ImF6TVkgfeUMhTtRpQpeGOndX2XZx3Pg6QqwslzH4CZ2knd7OD7wX9joD63zVyYCNNRjCTbFmMuj%2F0bNzed1ockXX7ruffpWVMwsRxV8dTm%2F7cLvRSt8UAn9dcRO7mBoiCx9Enrwz8j3SEyXNFy6WzjVmnxA9rEbmyioMuH%2FJFmtwu8wHGw05972cPmqHPeRRyBWVJdFJ34H8uNqES0Vmd0pptPH6V7IStt%2FdA%2BtP8i0xVcLMbd3hWUNlbxq0HCotOq8DiTL9DA5mOll4o51aHIRF%2BcMlTWK0N1qI7IpsGyeOf3xbWRbE0qUxC6A5q7tpxoTGWvq5POaLiLNeGwW2z%2BO1vmDmD543tL%2FzmlFAUkCETFAEQVGcCYGZK%2Bm0HfUpF1WcRk7j8ilhoEuQp3%2FKKTuV2x%2FFh4lOYtdlPWx5HNzcP8yyXRXeS5LlHMTE6cWTnZmAy3NmGsAcp2x06%2BOm5J92TML3a%2FrwGOqUBHIxM8ZeSFuJOKpuQD7bOzLjYlCaItFSvckG0w0MAl1TpIHn9dV0MunFa1k9oZTp3KYi%2FuA%2F4dBXn%2BzQU%2Bg3FgAtqZmwJHtxUjJj0Dhi%2FawezsNnQ34%2BJA6xx4ISnH8W79hX2krqnzH6QE9vxKE%2F9FZ0D4mvJQ0kn%2BiqWgYvnpDwLrOReAwXCSD7GaM8TMoJzEsLt%2FpsdhAW0xl5H63WHyqwvdqIU&X-Amz-Signature=90808db0da4eb83618b3a081d15ea6f3dd3892d5806a7bb938bc7013f5ce07ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTUOQI4F%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzj6k8TIZHkzBv6Z4AiYNzPnOff17d2i1WuCRuMK1%2BMAiEAscNlECRVN3g0dAbXLzMz9Ryc1efiNhWbGvB6ynmYu88qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIkQLb%2Fs3Y%2F3hSmJgircA4oEv%2BJ2vlMcYdSCNUHj0uRI75os6itVdnQdzerLit5PTKR2gTOvOsnAGndqHDMhadHEn1n%2FcwL43UEPHOmBfmtuG3bnr8%2BhTSNg%2BQnQLNAySrM74BRQYeBM9rHSAwwAPR4eWW10t02QsK4N68Lsw9uyqyuanVrYV1ImF6TVkgfeUMhTtRpQpeGOndX2XZx3Pg6QqwslzH4CZ2knd7OD7wX9joD63zVyYCNNRjCTbFmMuj%2F0bNzed1ockXX7ruffpWVMwsRxV8dTm%2F7cLvRSt8UAn9dcRO7mBoiCx9Enrwz8j3SEyXNFy6WzjVmnxA9rEbmyioMuH%2FJFmtwu8wHGw05972cPmqHPeRRyBWVJdFJ34H8uNqES0Vmd0pptPH6V7IStt%2FdA%2BtP8i0xVcLMbd3hWUNlbxq0HCotOq8DiTL9DA5mOll4o51aHIRF%2BcMlTWK0N1qI7IpsGyeOf3xbWRbE0qUxC6A5q7tpxoTGWvq5POaLiLNeGwW2z%2BO1vmDmD543tL%2FzmlFAUkCETFAEQVGcCYGZK%2Bm0HfUpF1WcRk7j8ilhoEuQp3%2FKKTuV2x%2FFh4lOYtdlPWx5HNzcP8yyXRXeS5LlHMTE6cWTnZmAy3NmGsAcp2x06%2BOm5J92TML3a%2FrwGOqUBHIxM8ZeSFuJOKpuQD7bOzLjYlCaItFSvckG0w0MAl1TpIHn9dV0MunFa1k9oZTp3KYi%2FuA%2F4dBXn%2BzQU%2Bg3FgAtqZmwJHtxUjJj0Dhi%2FawezsNnQ34%2BJA6xx4ISnH8W79hX2krqnzH6QE9vxKE%2F9FZ0D4mvJQ0kn%2BiqWgYvnpDwLrOReAwXCSD7GaM8TMoJzEsLt%2FpsdhAW0xl5H63WHyqwvdqIU&X-Amz-Signature=222d8570595c512afe6d09533b012d734b1321fd95bc81e079eca5972f8d8ee2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTUOQI4F%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzj6k8TIZHkzBv6Z4AiYNzPnOff17d2i1WuCRuMK1%2BMAiEAscNlECRVN3g0dAbXLzMz9Ryc1efiNhWbGvB6ynmYu88qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIkQLb%2Fs3Y%2F3hSmJgircA4oEv%2BJ2vlMcYdSCNUHj0uRI75os6itVdnQdzerLit5PTKR2gTOvOsnAGndqHDMhadHEn1n%2FcwL43UEPHOmBfmtuG3bnr8%2BhTSNg%2BQnQLNAySrM74BRQYeBM9rHSAwwAPR4eWW10t02QsK4N68Lsw9uyqyuanVrYV1ImF6TVkgfeUMhTtRpQpeGOndX2XZx3Pg6QqwslzH4CZ2knd7OD7wX9joD63zVyYCNNRjCTbFmMuj%2F0bNzed1ockXX7ruffpWVMwsRxV8dTm%2F7cLvRSt8UAn9dcRO7mBoiCx9Enrwz8j3SEyXNFy6WzjVmnxA9rEbmyioMuH%2FJFmtwu8wHGw05972cPmqHPeRRyBWVJdFJ34H8uNqES0Vmd0pptPH6V7IStt%2FdA%2BtP8i0xVcLMbd3hWUNlbxq0HCotOq8DiTL9DA5mOll4o51aHIRF%2BcMlTWK0N1qI7IpsGyeOf3xbWRbE0qUxC6A5q7tpxoTGWvq5POaLiLNeGwW2z%2BO1vmDmD543tL%2FzmlFAUkCETFAEQVGcCYGZK%2Bm0HfUpF1WcRk7j8ilhoEuQp3%2FKKTuV2x%2FFh4lOYtdlPWx5HNzcP8yyXRXeS5LlHMTE6cWTnZmAy3NmGsAcp2x06%2BOm5J92TML3a%2FrwGOqUBHIxM8ZeSFuJOKpuQD7bOzLjYlCaItFSvckG0w0MAl1TpIHn9dV0MunFa1k9oZTp3KYi%2FuA%2F4dBXn%2BzQU%2Bg3FgAtqZmwJHtxUjJj0Dhi%2FawezsNnQ34%2BJA6xx4ISnH8W79hX2krqnzH6QE9vxKE%2F9FZ0D4mvJQ0kn%2BiqWgYvnpDwLrOReAwXCSD7GaM8TMoJzEsLt%2FpsdhAW0xl5H63WHyqwvdqIU&X-Amz-Signature=9f80c584bca02796819c8b5522786ee7d4aff3a5aa648fced65dfc2fa53a919b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJLBFXSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFC1gZYBtXYWA32gylWnEGZXUSXiabfrMqLR3VIPg21DAiBgGc9pq9THPaLoO4dMjWe6OH0yA3Vsdd28BjqjF9FwhCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsCHQw%2Bh5LHUYnBdKKtwD1v9yodlpIAuHTDmNvj8r29NQFR4R1vhJS97yfyNaGTA5cTAmhDFWwxX9Rmo%2FGYi%2B9%2BAoK7NZQhCHdf04%2BvLkxGNIqdD%2FPnKbMM7nE%2BsW3oc8SCs9rRsPYg6Iv5zHpGajbyYo6ugKtjB8ChxLwhg8XQKfBQPOgnEkF84HGFXJDzxSXE2g7NxUckT5cBYrzUHWcjT8LcyNqUFoGbCG75btLkeKk30XDg9GQ6mVEIyihr4Zs1uuA%2BuRVpqwerJgpZAz1GmCHxTkTtz99ZvBbEtVBkxG8wzafeRr0bjiyEbV8SueCo2gwi%2FjQEWCKW5162NNK8teQWxKHV3nohpz%2By0qe2hmhRWorTT8X990XkBWVlPyvJ%2Bje3Q895q1SBODqF0vEb%2BVVWTzS3xqh3C%2FdNQCvm%2BFvULMc3XPMdj5EHR%2FZibl5EHmaG%2Bwj1AwLoubijhkxwxtEQ26p52lAqkzOESYKagAr9G8yTmGw00jE8gwhLpAjDcKFcWC518qYQjKjEXT4DW%2FIYhEBnQCau3htUu28%2BajA3QEJAcGa1lP3FuTsJpgN%2F%2BRoZTR2XDOr8yWZixgDmRd6dzz5%2Ffo5R0dpqPl1sZ7A2wVICvjwL1js%2FPI0p2S04LIY30OytVHE2Uw4%2BH%2BvAY6pgHMdSbdHQZOnkIUBTC50s9F8f8bRbmOVmG2PIhdsFW5%2F3BRV3evOX%2BgmK%2B7bbQOg1QPd9MBrrQ3LNdEirMTcHrze6tZbF0U%2FqWR88WhVCn6nNLAHCsSWJl07XR1CPrEP0qlrfNhTXFBD%2BlKZEN%2F1Lfw7bsHb%2BkPB2yAdPB%2BUL9Bq5JvqgCLLlv0GqDxGHsksk6u4AW6TbDUx2dvmiHEmYR7tZCjBHBE&X-Amz-Signature=d103fde38af91905a9422162b78b0c598efae73e0a164abba3d249aae109a934&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJLBFXSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFC1gZYBtXYWA32gylWnEGZXUSXiabfrMqLR3VIPg21DAiBgGc9pq9THPaLoO4dMjWe6OH0yA3Vsdd28BjqjF9FwhCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsCHQw%2Bh5LHUYnBdKKtwD1v9yodlpIAuHTDmNvj8r29NQFR4R1vhJS97yfyNaGTA5cTAmhDFWwxX9Rmo%2FGYi%2B9%2BAoK7NZQhCHdf04%2BvLkxGNIqdD%2FPnKbMM7nE%2BsW3oc8SCs9rRsPYg6Iv5zHpGajbyYo6ugKtjB8ChxLwhg8XQKfBQPOgnEkF84HGFXJDzxSXE2g7NxUckT5cBYrzUHWcjT8LcyNqUFoGbCG75btLkeKk30XDg9GQ6mVEIyihr4Zs1uuA%2BuRVpqwerJgpZAz1GmCHxTkTtz99ZvBbEtVBkxG8wzafeRr0bjiyEbV8SueCo2gwi%2FjQEWCKW5162NNK8teQWxKHV3nohpz%2By0qe2hmhRWorTT8X990XkBWVlPyvJ%2Bje3Q895q1SBODqF0vEb%2BVVWTzS3xqh3C%2FdNQCvm%2BFvULMc3XPMdj5EHR%2FZibl5EHmaG%2Bwj1AwLoubijhkxwxtEQ26p52lAqkzOESYKagAr9G8yTmGw00jE8gwhLpAjDcKFcWC518qYQjKjEXT4DW%2FIYhEBnQCau3htUu28%2BajA3QEJAcGa1lP3FuTsJpgN%2F%2BRoZTR2XDOr8yWZixgDmRd6dzz5%2Ffo5R0dpqPl1sZ7A2wVICvjwL1js%2FPI0p2S04LIY30OytVHE2Uw4%2BH%2BvAY6pgHMdSbdHQZOnkIUBTC50s9F8f8bRbmOVmG2PIhdsFW5%2F3BRV3evOX%2BgmK%2B7bbQOg1QPd9MBrrQ3LNdEirMTcHrze6tZbF0U%2FqWR88WhVCn6nNLAHCsSWJl07XR1CPrEP0qlrfNhTXFBD%2BlKZEN%2F1Lfw7bsHb%2BkPB2yAdPB%2BUL9Bq5JvqgCLLlv0GqDxGHsksk6u4AW6TbDUx2dvmiHEmYR7tZCjBHBE&X-Amz-Signature=2498aec9c9149f9c33cac59aba8f5269d99206a48b88909acb32962fa7f87ad1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJLBFXSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFC1gZYBtXYWA32gylWnEGZXUSXiabfrMqLR3VIPg21DAiBgGc9pq9THPaLoO4dMjWe6OH0yA3Vsdd28BjqjF9FwhCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsCHQw%2Bh5LHUYnBdKKtwD1v9yodlpIAuHTDmNvj8r29NQFR4R1vhJS97yfyNaGTA5cTAmhDFWwxX9Rmo%2FGYi%2B9%2BAoK7NZQhCHdf04%2BvLkxGNIqdD%2FPnKbMM7nE%2BsW3oc8SCs9rRsPYg6Iv5zHpGajbyYo6ugKtjB8ChxLwhg8XQKfBQPOgnEkF84HGFXJDzxSXE2g7NxUckT5cBYrzUHWcjT8LcyNqUFoGbCG75btLkeKk30XDg9GQ6mVEIyihr4Zs1uuA%2BuRVpqwerJgpZAz1GmCHxTkTtz99ZvBbEtVBkxG8wzafeRr0bjiyEbV8SueCo2gwi%2FjQEWCKW5162NNK8teQWxKHV3nohpz%2By0qe2hmhRWorTT8X990XkBWVlPyvJ%2Bje3Q895q1SBODqF0vEb%2BVVWTzS3xqh3C%2FdNQCvm%2BFvULMc3XPMdj5EHR%2FZibl5EHmaG%2Bwj1AwLoubijhkxwxtEQ26p52lAqkzOESYKagAr9G8yTmGw00jE8gwhLpAjDcKFcWC518qYQjKjEXT4DW%2FIYhEBnQCau3htUu28%2BajA3QEJAcGa1lP3FuTsJpgN%2F%2BRoZTR2XDOr8yWZixgDmRd6dzz5%2Ffo5R0dpqPl1sZ7A2wVICvjwL1js%2FPI0p2S04LIY30OytVHE2Uw4%2BH%2BvAY6pgHMdSbdHQZOnkIUBTC50s9F8f8bRbmOVmG2PIhdsFW5%2F3BRV3evOX%2BgmK%2B7bbQOg1QPd9MBrrQ3LNdEirMTcHrze6tZbF0U%2FqWR88WhVCn6nNLAHCsSWJl07XR1CPrEP0qlrfNhTXFBD%2BlKZEN%2F1Lfw7bsHb%2BkPB2yAdPB%2BUL9Bq5JvqgCLLlv0GqDxGHsksk6u4AW6TbDUx2dvmiHEmYR7tZCjBHBE&X-Amz-Signature=99a490e819f577ba2bed29e889a76fea477aafa4061b1db862b1b61a6120a661&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJLBFXSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFC1gZYBtXYWA32gylWnEGZXUSXiabfrMqLR3VIPg21DAiBgGc9pq9THPaLoO4dMjWe6OH0yA3Vsdd28BjqjF9FwhCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsCHQw%2Bh5LHUYnBdKKtwD1v9yodlpIAuHTDmNvj8r29NQFR4R1vhJS97yfyNaGTA5cTAmhDFWwxX9Rmo%2FGYi%2B9%2BAoK7NZQhCHdf04%2BvLkxGNIqdD%2FPnKbMM7nE%2BsW3oc8SCs9rRsPYg6Iv5zHpGajbyYo6ugKtjB8ChxLwhg8XQKfBQPOgnEkF84HGFXJDzxSXE2g7NxUckT5cBYrzUHWcjT8LcyNqUFoGbCG75btLkeKk30XDg9GQ6mVEIyihr4Zs1uuA%2BuRVpqwerJgpZAz1GmCHxTkTtz99ZvBbEtVBkxG8wzafeRr0bjiyEbV8SueCo2gwi%2FjQEWCKW5162NNK8teQWxKHV3nohpz%2By0qe2hmhRWorTT8X990XkBWVlPyvJ%2Bje3Q895q1SBODqF0vEb%2BVVWTzS3xqh3C%2FdNQCvm%2BFvULMc3XPMdj5EHR%2FZibl5EHmaG%2Bwj1AwLoubijhkxwxtEQ26p52lAqkzOESYKagAr9G8yTmGw00jE8gwhLpAjDcKFcWC518qYQjKjEXT4DW%2FIYhEBnQCau3htUu28%2BajA3QEJAcGa1lP3FuTsJpgN%2F%2BRoZTR2XDOr8yWZixgDmRd6dzz5%2Ffo5R0dpqPl1sZ7A2wVICvjwL1js%2FPI0p2S04LIY30OytVHE2Uw4%2BH%2BvAY6pgHMdSbdHQZOnkIUBTC50s9F8f8bRbmOVmG2PIhdsFW5%2F3BRV3evOX%2BgmK%2B7bbQOg1QPd9MBrrQ3LNdEirMTcHrze6tZbF0U%2FqWR88WhVCn6nNLAHCsSWJl07XR1CPrEP0qlrfNhTXFBD%2BlKZEN%2F1Lfw7bsHb%2BkPB2yAdPB%2BUL9Bq5JvqgCLLlv0GqDxGHsksk6u4AW6TbDUx2dvmiHEmYR7tZCjBHBE&X-Amz-Signature=f9ef5ccc6508775c4d56069e7018f9f211fdb35e749438ebb0b66ffd6e07b5c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJLBFXSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFC1gZYBtXYWA32gylWnEGZXUSXiabfrMqLR3VIPg21DAiBgGc9pq9THPaLoO4dMjWe6OH0yA3Vsdd28BjqjF9FwhCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsCHQw%2Bh5LHUYnBdKKtwD1v9yodlpIAuHTDmNvj8r29NQFR4R1vhJS97yfyNaGTA5cTAmhDFWwxX9Rmo%2FGYi%2B9%2BAoK7NZQhCHdf04%2BvLkxGNIqdD%2FPnKbMM7nE%2BsW3oc8SCs9rRsPYg6Iv5zHpGajbyYo6ugKtjB8ChxLwhg8XQKfBQPOgnEkF84HGFXJDzxSXE2g7NxUckT5cBYrzUHWcjT8LcyNqUFoGbCG75btLkeKk30XDg9GQ6mVEIyihr4Zs1uuA%2BuRVpqwerJgpZAz1GmCHxTkTtz99ZvBbEtVBkxG8wzafeRr0bjiyEbV8SueCo2gwi%2FjQEWCKW5162NNK8teQWxKHV3nohpz%2By0qe2hmhRWorTT8X990XkBWVlPyvJ%2Bje3Q895q1SBODqF0vEb%2BVVWTzS3xqh3C%2FdNQCvm%2BFvULMc3XPMdj5EHR%2FZibl5EHmaG%2Bwj1AwLoubijhkxwxtEQ26p52lAqkzOESYKagAr9G8yTmGw00jE8gwhLpAjDcKFcWC518qYQjKjEXT4DW%2FIYhEBnQCau3htUu28%2BajA3QEJAcGa1lP3FuTsJpgN%2F%2BRoZTR2XDOr8yWZixgDmRd6dzz5%2Ffo5R0dpqPl1sZ7A2wVICvjwL1js%2FPI0p2S04LIY30OytVHE2Uw4%2BH%2BvAY6pgHMdSbdHQZOnkIUBTC50s9F8f8bRbmOVmG2PIhdsFW5%2F3BRV3evOX%2BgmK%2B7bbQOg1QPd9MBrrQ3LNdEirMTcHrze6tZbF0U%2FqWR88WhVCn6nNLAHCsSWJl07XR1CPrEP0qlrfNhTXFBD%2BlKZEN%2F1Lfw7bsHb%2BkPB2yAdPB%2BUL9Bq5JvqgCLLlv0GqDxGHsksk6u4AW6TbDUx2dvmiHEmYR7tZCjBHBE&X-Amz-Signature=9904278efa0998fe6555477b601be53d8752475de76a23c582c0e1a298c87a23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJLBFXSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFC1gZYBtXYWA32gylWnEGZXUSXiabfrMqLR3VIPg21DAiBgGc9pq9THPaLoO4dMjWe6OH0yA3Vsdd28BjqjF9FwhCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsCHQw%2Bh5LHUYnBdKKtwD1v9yodlpIAuHTDmNvj8r29NQFR4R1vhJS97yfyNaGTA5cTAmhDFWwxX9Rmo%2FGYi%2B9%2BAoK7NZQhCHdf04%2BvLkxGNIqdD%2FPnKbMM7nE%2BsW3oc8SCs9rRsPYg6Iv5zHpGajbyYo6ugKtjB8ChxLwhg8XQKfBQPOgnEkF84HGFXJDzxSXE2g7NxUckT5cBYrzUHWcjT8LcyNqUFoGbCG75btLkeKk30XDg9GQ6mVEIyihr4Zs1uuA%2BuRVpqwerJgpZAz1GmCHxTkTtz99ZvBbEtVBkxG8wzafeRr0bjiyEbV8SueCo2gwi%2FjQEWCKW5162NNK8teQWxKHV3nohpz%2By0qe2hmhRWorTT8X990XkBWVlPyvJ%2Bje3Q895q1SBODqF0vEb%2BVVWTzS3xqh3C%2FdNQCvm%2BFvULMc3XPMdj5EHR%2FZibl5EHmaG%2Bwj1AwLoubijhkxwxtEQ26p52lAqkzOESYKagAr9G8yTmGw00jE8gwhLpAjDcKFcWC518qYQjKjEXT4DW%2FIYhEBnQCau3htUu28%2BajA3QEJAcGa1lP3FuTsJpgN%2F%2BRoZTR2XDOr8yWZixgDmRd6dzz5%2Ffo5R0dpqPl1sZ7A2wVICvjwL1js%2FPI0p2S04LIY30OytVHE2Uw4%2BH%2BvAY6pgHMdSbdHQZOnkIUBTC50s9F8f8bRbmOVmG2PIhdsFW5%2F3BRV3evOX%2BgmK%2B7bbQOg1QPd9MBrrQ3LNdEirMTcHrze6tZbF0U%2FqWR88WhVCn6nNLAHCsSWJl07XR1CPrEP0qlrfNhTXFBD%2BlKZEN%2F1Lfw7bsHb%2BkPB2yAdPB%2BUL9Bq5JvqgCLLlv0GqDxGHsksk6u4AW6TbDUx2dvmiHEmYR7tZCjBHBE&X-Amz-Signature=1eca13e8ca8ddbf0824dbb1b31cb55b184029a97b00f994895b2373e51e6069a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y24SJQA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH1DAuoGKSEZDvg92W%2Bpon5e4XtOuJmqh%2BUgPGTHIImUAiBBLrT06nVGH4NQ9sACrLWTKW217JRs0SBsfVg29s5oISqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvV%2FkA4v68cnzguxVKtwD32lw0fjD85cLDFstKpbb%2FkdDenEtDuHmx6nUXBbzsShET0bNvNfiHu%2Fd%2BICKioOV9VZlP%2FOesloEJwcSkYXl0jC8GdnLQCQJka3PBFML017oXF8w9y4ZFreibGmJdS8Tpop0etfZVDkDTMIo69nxbq3s431tUVUbZ8Q6MJJcLIU2nvOqMnH%2Fw%2FJ7QlYe0CU78gZEDjS%2FqwMqqY21iEdte%2B1EhtP%2B6Jpp%2FxD58sEYuQMn4dZ0Gu9W1rB6SozagzUT%2B9kiPFjbciFcJh%2FNqyGDypRVqEm5XE%2FKdRwo1Om1thF1Nj4MJlVMFUsKDnmgv8DayinOSZ%2BscBeq0tHNfnrLEvmq6xruKPWGNu46fiZhyHHoLAIatXc9t6tRqiJndmKempBvaYY4Lqm6neUNcq3NY25LCs6dUTCrwfW1rXc0r4SpgS9e1GHv77b8fSsZpr6JY2KIZ%2B9Y1kEV7SY3DzNS1afEcvMzNtK8EJOV2bH8qInc4%2Bn1ntKw9ISQC0Y5lj6F0LeFj4TaQvJTm4HstQ6lFo4GxrwAYxOPD2TLlBdGrusccK176SqLH%2FF%2FVUFB1buiJUlulYUEiYlOF1U%2B06ZBDMnxhyjgv%2FALCgRSoelfeev38ipmD0RiyLmMQN4w2d7%2BvAY6pgFh7oAr0IX%2FclrWKLrsFrxVrz2uy56LNeNjGWJUbLdxQeXOXaXZ%2BaSSfQq8DqYzYQso3c%2BShi87SXZjpAiIeknNoHQJWyr37zbSdoFYjkVNUYcFUvfJebw3MQj99JfSr%2Bs3D5tB6aPmyajOQg6rE%2Faunuc0VIZ019mWDCzVywvR1ewK66eaHpPHFlscu217WWJla%2F6C6uGh1w%2BkppVF3GPqph7KrUVg&X-Amz-Signature=759d8c035dcebb7a17bc1d06e8bc52868da0b00b835428f89e1c3be648bd956a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KJKGDEN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGa2lOev7ayizbDaY19fgFPRjBFfgVTLHgZqDqCQ0%2FnpAiAaIAP0qnRfP40kan6yzV8mkEx1oAIrYkyONoYwyUnb0iqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxwoJ%2B5sFIPRMu6GoKtwDO8agfG7aXu%2Bct45iXPq9FpdXCyECyRBdwJaRJJmwQaTzy4fPtysLmgof91iGsO34bd4b48SEdVix9wtS4l6eUZHoqpHA1D2OleV3zxichV6dq3R3PuBD5Ueo5yUbPuI2BK1diK4QUCkw%2FXdFXD6cKlH%2BDXG6VqBEVgbjzjTAvpw6tJoYBMKIu6MM5VGjem9oVVD6XmuRIfDpXjfzjbEnKTLAG%2FVjIo5v8AylhLvNY3Y0X5DR4HJfmAZJaKvyPSotvsd3rhFdN8b9EqokD6l2IAAUajShDq5YZ0ErDMKbJFrvg4hAJUBqSoDvep%2Fu%2FNpQR%2FktaqbbhfvoMLFvwGzr8vUgQS7bIQKcG0AhUbSY0mntp51xJeXl3j9bfDFt83Z4W14pIKcvTQAL5CyNU56wKIGw62XxoQbydwCtPjClQA6ceRWoKui0ZN%2F%2BYsTn4p56wpn2bvXkXbm5eQiQ%2FdKDB3S7yVd%2BlN8fl7DO75MzdA%2FUmGj%2BEVGfVKnQZDq3Gr9N9M%2Fr1EdYY7UJbPY8%2B7JxGzkEwvHykM%2B5LxPazWVYZNWGL4Pt4GzvLIUxuGkhIFhOgt3VJd%2Bg5nKwvfjffIkSH3rVHYk1HKJZeau2t9FB2adEjExrEpRVVIuzLVMwpN3%2BvAY6pgHNrvDIfUAjfceguImJQHBnFj8TYEev0DM2nZ6%2F5A5myA93fkqsjh0%2Fkp0W8jm6dEdS%2BCwTm%2B6QiWNfg7vWrluxhEEalZwRBEVoep9OgFkFq2A0HTZKLhuJPiqBXp8SOBKo6PV0CimWcUYXWZnQpx8Vp4kb%2FbBwnHa7cIM%2F4xumGR3alGOSERkuTpaC%2F%2BiKj2yCWRwGDE35YZ5JILf%2BgW%2BzHGkPuzL7&X-Amz-Signature=f3dd777af28bd03f8b4fe863246f83e9d3e5ccaff4417dbdeb3a07796485441b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJLBFXSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFC1gZYBtXYWA32gylWnEGZXUSXiabfrMqLR3VIPg21DAiBgGc9pq9THPaLoO4dMjWe6OH0yA3Vsdd28BjqjF9FwhCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsCHQw%2Bh5LHUYnBdKKtwD1v9yodlpIAuHTDmNvj8r29NQFR4R1vhJS97yfyNaGTA5cTAmhDFWwxX9Rmo%2FGYi%2B9%2BAoK7NZQhCHdf04%2BvLkxGNIqdD%2FPnKbMM7nE%2BsW3oc8SCs9rRsPYg6Iv5zHpGajbyYo6ugKtjB8ChxLwhg8XQKfBQPOgnEkF84HGFXJDzxSXE2g7NxUckT5cBYrzUHWcjT8LcyNqUFoGbCG75btLkeKk30XDg9GQ6mVEIyihr4Zs1uuA%2BuRVpqwerJgpZAz1GmCHxTkTtz99ZvBbEtVBkxG8wzafeRr0bjiyEbV8SueCo2gwi%2FjQEWCKW5162NNK8teQWxKHV3nohpz%2By0qe2hmhRWorTT8X990XkBWVlPyvJ%2Bje3Q895q1SBODqF0vEb%2BVVWTzS3xqh3C%2FdNQCvm%2BFvULMc3XPMdj5EHR%2FZibl5EHmaG%2Bwj1AwLoubijhkxwxtEQ26p52lAqkzOESYKagAr9G8yTmGw00jE8gwhLpAjDcKFcWC518qYQjKjEXT4DW%2FIYhEBnQCau3htUu28%2BajA3QEJAcGa1lP3FuTsJpgN%2F%2BRoZTR2XDOr8yWZixgDmRd6dzz5%2Ffo5R0dpqPl1sZ7A2wVICvjwL1js%2FPI0p2S04LIY30OytVHE2Uw4%2BH%2BvAY6pgHMdSbdHQZOnkIUBTC50s9F8f8bRbmOVmG2PIhdsFW5%2F3BRV3evOX%2BgmK%2B7bbQOg1QPd9MBrrQ3LNdEirMTcHrze6tZbF0U%2FqWR88WhVCn6nNLAHCsSWJl07XR1CPrEP0qlrfNhTXFBD%2BlKZEN%2F1Lfw7bsHb%2BkPB2yAdPB%2BUL9Bq5JvqgCLLlv0GqDxGHsksk6u4AW6TbDUx2dvmiHEmYR7tZCjBHBE&X-Amz-Signature=955b09a68d0ad894b26b703a99a2b55bf7940bec4a9562fbe645310b11958c3a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJLBFXSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFC1gZYBtXYWA32gylWnEGZXUSXiabfrMqLR3VIPg21DAiBgGc9pq9THPaLoO4dMjWe6OH0yA3Vsdd28BjqjF9FwhCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsCHQw%2Bh5LHUYnBdKKtwD1v9yodlpIAuHTDmNvj8r29NQFR4R1vhJS97yfyNaGTA5cTAmhDFWwxX9Rmo%2FGYi%2B9%2BAoK7NZQhCHdf04%2BvLkxGNIqdD%2FPnKbMM7nE%2BsW3oc8SCs9rRsPYg6Iv5zHpGajbyYo6ugKtjB8ChxLwhg8XQKfBQPOgnEkF84HGFXJDzxSXE2g7NxUckT5cBYrzUHWcjT8LcyNqUFoGbCG75btLkeKk30XDg9GQ6mVEIyihr4Zs1uuA%2BuRVpqwerJgpZAz1GmCHxTkTtz99ZvBbEtVBkxG8wzafeRr0bjiyEbV8SueCo2gwi%2FjQEWCKW5162NNK8teQWxKHV3nohpz%2By0qe2hmhRWorTT8X990XkBWVlPyvJ%2Bje3Q895q1SBODqF0vEb%2BVVWTzS3xqh3C%2FdNQCvm%2BFvULMc3XPMdj5EHR%2FZibl5EHmaG%2Bwj1AwLoubijhkxwxtEQ26p52lAqkzOESYKagAr9G8yTmGw00jE8gwhLpAjDcKFcWC518qYQjKjEXT4DW%2FIYhEBnQCau3htUu28%2BajA3QEJAcGa1lP3FuTsJpgN%2F%2BRoZTR2XDOr8yWZixgDmRd6dzz5%2Ffo5R0dpqPl1sZ7A2wVICvjwL1js%2FPI0p2S04LIY30OytVHE2Uw4%2BH%2BvAY6pgHMdSbdHQZOnkIUBTC50s9F8f8bRbmOVmG2PIhdsFW5%2F3BRV3evOX%2BgmK%2B7bbQOg1QPd9MBrrQ3LNdEirMTcHrze6tZbF0U%2FqWR88WhVCn6nNLAHCsSWJl07XR1CPrEP0qlrfNhTXFBD%2BlKZEN%2F1Lfw7bsHb%2BkPB2yAdPB%2BUL9Bq5JvqgCLLlv0GqDxGHsksk6u4AW6TbDUx2dvmiHEmYR7tZCjBHBE&X-Amz-Signature=a9d53b9f6718bfab80f3ed833875cf09d128e3c0edb080c610704d3aa737ad5d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJLBFXSQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFC1gZYBtXYWA32gylWnEGZXUSXiabfrMqLR3VIPg21DAiBgGc9pq9THPaLoO4dMjWe6OH0yA3Vsdd28BjqjF9FwhCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsCHQw%2Bh5LHUYnBdKKtwD1v9yodlpIAuHTDmNvj8r29NQFR4R1vhJS97yfyNaGTA5cTAmhDFWwxX9Rmo%2FGYi%2B9%2BAoK7NZQhCHdf04%2BvLkxGNIqdD%2FPnKbMM7nE%2BsW3oc8SCs9rRsPYg6Iv5zHpGajbyYo6ugKtjB8ChxLwhg8XQKfBQPOgnEkF84HGFXJDzxSXE2g7NxUckT5cBYrzUHWcjT8LcyNqUFoGbCG75btLkeKk30XDg9GQ6mVEIyihr4Zs1uuA%2BuRVpqwerJgpZAz1GmCHxTkTtz99ZvBbEtVBkxG8wzafeRr0bjiyEbV8SueCo2gwi%2FjQEWCKW5162NNK8teQWxKHV3nohpz%2By0qe2hmhRWorTT8X990XkBWVlPyvJ%2Bje3Q895q1SBODqF0vEb%2BVVWTzS3xqh3C%2FdNQCvm%2BFvULMc3XPMdj5EHR%2FZibl5EHmaG%2Bwj1AwLoubijhkxwxtEQ26p52lAqkzOESYKagAr9G8yTmGw00jE8gwhLpAjDcKFcWC518qYQjKjEXT4DW%2FIYhEBnQCau3htUu28%2BajA3QEJAcGa1lP3FuTsJpgN%2F%2BRoZTR2XDOr8yWZixgDmRd6dzz5%2Ffo5R0dpqPl1sZ7A2wVICvjwL1js%2FPI0p2S04LIY30OytVHE2Uw4%2BH%2BvAY6pgHMdSbdHQZOnkIUBTC50s9F8f8bRbmOVmG2PIhdsFW5%2F3BRV3evOX%2BgmK%2B7bbQOg1QPd9MBrrQ3LNdEirMTcHrze6tZbF0U%2FqWR88WhVCn6nNLAHCsSWJl07XR1CPrEP0qlrfNhTXFBD%2BlKZEN%2F1Lfw7bsHb%2BkPB2yAdPB%2BUL9Bq5JvqgCLLlv0GqDxGHsksk6u4AW6TbDUx2dvmiHEmYR7tZCjBHBE&X-Amz-Signature=5e6243c454752a30766c5cf075d7e636d2346797eaa2e557ccfdbf586f082432&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3P3ID2Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRMD%2BfQpWz2J3FgWT%2BsAgkMgUXs9Ast%2BXSJGMzSjuj8QIhAPcWYI82nen%2FO2EVjYLzEiy81TXTWHtcsm9VjWyeX%2F9bKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVYRgWRIVO02tj%2Bjwq3AMsSrP3JTi25AOuP34CJ1Aexn4%2FUT2P6g7zjaJHeHpXMqJXe2y%2BF8B5kLDnXztxyuNqVlmI6tGveO01fvMHMkJ3j2XPWHFvAAsRyubhFWU%2BebztsxlS4oVJkmT31HC8t4d1PZ6Mnw6Hb%2FvDFpMVIPZHqKfrT54LiDI2mmnHK2B65dBp17xPfA7aehMw1g0602aXq5r7oLREgtRW8QjnD2wOgV4wUkN06ywZEpqVBqxu8ulTRgwb2coCGlZVb8rniPMj2HxkDJ7WHGGtkp363cHaQP9c1hVSq0Yh8Gb5WugchxserbJIDVvvpRI8X7tZQmh7MPeFHf3jKyUSXLUahtIKlK99ZEyGdtIcAPh%2BacTxNdkASdeMIbu3LvHnNhizwfvDO4J5jki9SWx619RXJQY1niYeQ4eASd70eQcdmaxBFp7kHqc8p9v2UXFi3%2FenzERKrxfWC7cgjvQiEeKmYFdgKtV8jVk7Hm%2BqgFpPNcpZbCJY2acFYvtwZVNvIJ8w1KAWUWWsCHhKpPS8kw%2BaAtrbpkJuH8GXfWT%2BQN%2FMVay0KQSTk9wCJb7%2BrvivtBT2RlOc6cm%2BCOyaWHGtIO%2Bo03mGKLdTKTa3StBcKefkt0h4zzp83u2OQ2ZZ6ngrpTCG4f68BjqkARf2CoPa0tJTOXhw9cOjoUW65GWoCGlA%2FD6zEBEI3bsnNDu06qu6K31w7FJk86B7pBdRqdxktZ4vNsGjSWGpd8YT1j7DPk%2BNA7NiqgNDqTNfUoii6qEXGN5FX8%2BRVp2yONl%2Bm2KCqRsw%2Fu9ICZtjaiTaALqTOk%2FqeBcy0VokismMfGJQf7nL5rSZK6dhYu40tB7SGQyaKmHGVlenUFj2AH4WsKBp&X-Amz-Signature=551fa0581c52673c5d3866e892c4c343bae48dd04dbc1d7e6097e08004cd36ce&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XL7ZLVW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICsRmwxfXQ9juGEJ15FlgUWkgCNn58SATA2sukVUWCWTAiEA7fwYxYJQtVEHAfUUaM7vMn0w7rls7HotI3gSJ5aQLfsqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoV52AbWaFcG5PA2yrcA05xNM6Ui5li%2FE%2BSq%2FrG6w8CtNnGSWV2pbcPzONUeLpQ5SHwTr0O4ff%2Bd5BDAWSXUC%2F5kMtNpJArQQktwvLVKc8tlpJG1NdEzGJqkHn%2BEX3Di3h%2BDlbIjmQswx0Nj5L2y1CBP5T%2F%2Fepp%2FNEGXeN76Mut1R%2Bd8uby%2F%2FMTdepS9sMZn4oA5O6QwdNPsWVZvLyeP40GfeCzVXzoVwSor7bMkV1chj0XQG2MIClV%2FI2TG1h4WF7wrZJAiESbDb89g7LWCPr%2BrolcPzKKL1EhqC4lXmSy9hImT6n0Zu9Tez3N7aGEMr6JVGQBUCRb%2FMvq2hCPZLenNdh%2BpT18Ep5gHmV9fHfhgK7xpfzJ1E%2B72s9Bvzc0vjIPVJ%2BhjsGzy42tuksZjdsraCWFbSIkFaArx0fofyR82oOpqcckXUGgzklu%2BiSYtS95BGmfCX7EJ9pdYzKJfAZdQ5HnREiIllNS%2FseKWwI7AC45jn5lukznyqEZ6W8ByVIclonAd2YsNlwIxOV1xkFyiJxX129xjbw255FqopO%2FAQHSkPOZB1SKZLQq4hfvT%2Fs%2Fr6TXSqOOgAl%2BntaPUHgoFB6v3JQ9%2FggSOvELxhDAe5wGOZChUC2wF8dy%2FpOHJCTuKWNgjOWYioZWMLTf%2FrwGOqUBDFyA9Wsk%2FldvG6jjvjCzgVmYZMxmJmeVwbnoamDa8uqF%2FwE4Ve1%2FB7ztg%2BZQEHAEegE7kkvN5HCaSCXqv6sC7I6QIAJ8kpK1DfcsHP9VXjrFbo7stmNdpLeWw0BlI%2BvL1pku91nL3AzyWpooRDbJIpulyVjctnNkMsQ1RpcbXKYM9H84UtFltZMie1glMFPv3h6%2BE4%2BlgIc2T2G8vsKMRTUugwFm&X-Amz-Signature=32ac1b680f813d62b4e44832460fd4bdfa7dc1bc0d907a6bc70d8b05919aa1d6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=e10947ffaee72dfbe8029614b09aaa07dff40e4d9ad2fec702181d0f36427f3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2NCXAQN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2BUxPTph2K8EcIrRSs7x2Wf%2FqBjAaMPQBJCqazVw4wgIgXgX2C6n9wUE8i%2B12ICHS0mhi2ujaUG2%2FTwVIx3sa9tQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2FyNImpEnnJjr6tOCrcA6Oi50z9r%2FgmVGvUgxZMkVK4SngN43BqZ58Q0RzvBmcO%2FSOoMJozkfnKk1TGlKuq03AHNWdcJmIqqf%2FQGcgOQDl7ggHqtyYmK8f3rJU6cJgV6fkPwrK8TO4l18F%2F8Sc2CQtn4YtWaI6dXMzhdHotwD8g2r91thRQBU54kJ95riF4z6WIhDq23%2BmtvN%2F5KWJOd1Qgu4ShSqQpENNzq788qY7gxYCpKleT4HIfKntQ5gy4%2FJuyfVkBDDfRvsUepK3P%2BLemnPFXoS78%2Ff8BcAQFXlEjmOUPxL8%2Fyv0tyUDEXa%2FUBi7i%2FVUoImVn3NdQhJ7OgH7dW%2F6epnkE4GzQiWwLchD9MrNqJRAAc3wtjVlGdLe0aPaOu0nolg92iiYwfpvWEBUqQ%2Fo%2BJ95dt4Gw1W5IMA1r4IcL%2BLiID0NPWfzK3vLeVC02jcfJaDBj5nVjzSOHREfeRseCDE%2FOqMuBoR%2B7hwNqFq%2BKMFNDOFGm54RLCbJzobfq8Ce%2FYSR6aBulOiD0%2BL5qrrN6%2F1SbWUPNAKa0K0TplM2WQT5BGqRIMba9Ora4MznJq716PE9h2kXRc1DvA4U3SXGmb0yCYqOEC%2FHgexC920Mp8FPFWXU4yoYBZiMiL5BW3ElKSJcisYCXMLbk%2FrwGOqUBwvRTF%2FL2FaqUFFyWy%2B8p7LmZF%2FlTYIx0M1sK%2FNHQbpkrrUBGwW1QEOvrIGpClCBDhQK4ejO6tos8t9o5HZXqnKcftPFYunCeRd%2FuXWrNLidw6cA7AavBW8mjGGInfV4MRcwZV3cfpUJ2vHjr1jD7f2f9o%2F44GcJ%2FODbLYJmTjK1gw7t641NQF8qOMHfKSTZCgJ94pp01yBdO86VukadfwNElvQZn&X-Amz-Signature=b6248b53de2f4a6a340262b8e1ab09a358e01913250d4ffaa52ea48dfa96a2b5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2NCXAQN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN%2BUxPTph2K8EcIrRSs7x2Wf%2FqBjAaMPQBJCqazVw4wgIgXgX2C6n9wUE8i%2B12ICHS0mhi2ujaUG2%2FTwVIx3sa9tQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2FyNImpEnnJjr6tOCrcA6Oi50z9r%2FgmVGvUgxZMkVK4SngN43BqZ58Q0RzvBmcO%2FSOoMJozkfnKk1TGlKuq03AHNWdcJmIqqf%2FQGcgOQDl7ggHqtyYmK8f3rJU6cJgV6fkPwrK8TO4l18F%2F8Sc2CQtn4YtWaI6dXMzhdHotwD8g2r91thRQBU54kJ95riF4z6WIhDq23%2BmtvN%2F5KWJOd1Qgu4ShSqQpENNzq788qY7gxYCpKleT4HIfKntQ5gy4%2FJuyfVkBDDfRvsUepK3P%2BLemnPFXoS78%2Ff8BcAQFXlEjmOUPxL8%2Fyv0tyUDEXa%2FUBi7i%2FVUoImVn3NdQhJ7OgH7dW%2F6epnkE4GzQiWwLchD9MrNqJRAAc3wtjVlGdLe0aPaOu0nolg92iiYwfpvWEBUqQ%2Fo%2BJ95dt4Gw1W5IMA1r4IcL%2BLiID0NPWfzK3vLeVC02jcfJaDBj5nVjzSOHREfeRseCDE%2FOqMuBoR%2B7hwNqFq%2BKMFNDOFGm54RLCbJzobfq8Ce%2FYSR6aBulOiD0%2BL5qrrN6%2F1SbWUPNAKa0K0TplM2WQT5BGqRIMba9Ora4MznJq716PE9h2kXRc1DvA4U3SXGmb0yCYqOEC%2FHgexC920Mp8FPFWXU4yoYBZiMiL5BW3ElKSJcisYCXMLbk%2FrwGOqUBwvRTF%2FL2FaqUFFyWy%2B8p7LmZF%2FlTYIx0M1sK%2FNHQbpkrrUBGwW1QEOvrIGpClCBDhQK4ejO6tos8t9o5HZXqnKcftPFYunCeRd%2FuXWrNLidw6cA7AavBW8mjGGInfV4MRcwZV3cfpUJ2vHjr1jD7f2f9o%2F44GcJ%2FODbLYJmTjK1gw7t641NQF8qOMHfKSTZCgJ94pp01yBdO86VukadfwNElvQZn&X-Amz-Signature=9989812467a5bc34c934460f5bba9a18477755175825788a47c2e97000a05df0&X-Amz-SignedHeaders=host&x-id=GetObject)

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
