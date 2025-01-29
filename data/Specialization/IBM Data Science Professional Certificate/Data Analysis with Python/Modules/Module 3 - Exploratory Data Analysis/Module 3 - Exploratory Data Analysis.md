

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FCQMO4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIGNffm1V8cAjUB6koVWU2x58PxgC%2B2gGAvbOmtn1TOicAiEArX%2FQqY3p%2Fpwus10ip%2Fk%2BauCzwJg%2FMUx88TA2ckVqCeQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnHK18gz%2BiayRkpISrcAwmcyZmKvv3gJjhGQjIqqn5VhcaUnZwmK%2BXMtM0NTSN0IjzR1LnfQREe2OIRLrd1siZwOG%2BuMuJnA4ll58iqB3sy28vgt4FR9D3KzF4%2BqnVtHYzlvNhzwOCzJX%2B6s8EMeZmVGSk7GD5k5DU5XpP3uU2fr7OcOyIY%2BXTz57wwJ1z8ZiRr1MG3Fxmy8oWRP7n2LTCkGxWiiZHl4TULWKgMAzA%2BMJXaIPQkwX%2BJv1zkrFLjQtocJkoniLxtpSYSUew2mmoK0S5oVB7ea%2B2cJ879%2FFIlrv0JdvPJJ5lMTDXro6vMJFYsSoFFb%2BLKZOeMXu7t%2Fgb35riFgeyNqI4L9rsi9Uz%2F%2BIzgYf0%2FgQePZZ0nU6ytD1CCQFmfiwA3v3YBe5yS8EIZMzQObTJ0lt%2F6q9PCtzxoBiRYvVnmmy7Sh4TljUZDGnbrZBcAPO43qqNh7s13L7vNcfLj0ZOGf6JdGiv8BueJTnb3%2FN4ZMod24mh4IefJ284mQgYkdesMt20RPR4GWE5PUSYaD%2FJumxs84LkCufsszyXO39JSKYD0kYLJx5jFkMFR0tIm%2FIIGUEvwswVK4ruBcuaTpZNAUh8JLTQgl9TZq64X99Y27O9bbbohxbG8ayUkG9cpLBLTV6CFMNWQ57wGOqUBPI9otiJ%2FvoAgDsmkl9hFO3J4hp4sbyQ%2B0nGL9wf4wygf5xn8M0x6JebflHk0guxKlJ8Uyv2bwK7u7AlkgPaivghHBanVClBO57ILPLXNG1bLGdreRkfeYocBO7PkVf1FfNgGJVzoEN9h2jRPsZ%2Bok64Ui5eovncJm891DU0uUoGM766U1XJxsxYbLTsVNTPo8YQrzx0q4QoYl3QGCy7jAuLVpqiW&X-Amz-Signature=41cbe4f07efc6dd5924941cdc95112e453fe05c426affcc910a0f37c34594301&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FCQMO4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIGNffm1V8cAjUB6koVWU2x58PxgC%2B2gGAvbOmtn1TOicAiEArX%2FQqY3p%2Fpwus10ip%2Fk%2BauCzwJg%2FMUx88TA2ckVqCeQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnHK18gz%2BiayRkpISrcAwmcyZmKvv3gJjhGQjIqqn5VhcaUnZwmK%2BXMtM0NTSN0IjzR1LnfQREe2OIRLrd1siZwOG%2BuMuJnA4ll58iqB3sy28vgt4FR9D3KzF4%2BqnVtHYzlvNhzwOCzJX%2B6s8EMeZmVGSk7GD5k5DU5XpP3uU2fr7OcOyIY%2BXTz57wwJ1z8ZiRr1MG3Fxmy8oWRP7n2LTCkGxWiiZHl4TULWKgMAzA%2BMJXaIPQkwX%2BJv1zkrFLjQtocJkoniLxtpSYSUew2mmoK0S5oVB7ea%2B2cJ879%2FFIlrv0JdvPJJ5lMTDXro6vMJFYsSoFFb%2BLKZOeMXu7t%2Fgb35riFgeyNqI4L9rsi9Uz%2F%2BIzgYf0%2FgQePZZ0nU6ytD1CCQFmfiwA3v3YBe5yS8EIZMzQObTJ0lt%2F6q9PCtzxoBiRYvVnmmy7Sh4TljUZDGnbrZBcAPO43qqNh7s13L7vNcfLj0ZOGf6JdGiv8BueJTnb3%2FN4ZMod24mh4IefJ284mQgYkdesMt20RPR4GWE5PUSYaD%2FJumxs84LkCufsszyXO39JSKYD0kYLJx5jFkMFR0tIm%2FIIGUEvwswVK4ruBcuaTpZNAUh8JLTQgl9TZq64X99Y27O9bbbohxbG8ayUkG9cpLBLTV6CFMNWQ57wGOqUBPI9otiJ%2FvoAgDsmkl9hFO3J4hp4sbyQ%2B0nGL9wf4wygf5xn8M0x6JebflHk0guxKlJ8Uyv2bwK7u7AlkgPaivghHBanVClBO57ILPLXNG1bLGdreRkfeYocBO7PkVf1FfNgGJVzoEN9h2jRPsZ%2Bok64Ui5eovncJm891DU0uUoGM766U1XJxsxYbLTsVNTPo8YQrzx0q4QoYl3QGCy7jAuLVpqiW&X-Amz-Signature=c701bc141be86d0d19e04d56e44e88a78c5ddc71f27b957d07976b0c0747085a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FCQMO4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIGNffm1V8cAjUB6koVWU2x58PxgC%2B2gGAvbOmtn1TOicAiEArX%2FQqY3p%2Fpwus10ip%2Fk%2BauCzwJg%2FMUx88TA2ckVqCeQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnHK18gz%2BiayRkpISrcAwmcyZmKvv3gJjhGQjIqqn5VhcaUnZwmK%2BXMtM0NTSN0IjzR1LnfQREe2OIRLrd1siZwOG%2BuMuJnA4ll58iqB3sy28vgt4FR9D3KzF4%2BqnVtHYzlvNhzwOCzJX%2B6s8EMeZmVGSk7GD5k5DU5XpP3uU2fr7OcOyIY%2BXTz57wwJ1z8ZiRr1MG3Fxmy8oWRP7n2LTCkGxWiiZHl4TULWKgMAzA%2BMJXaIPQkwX%2BJv1zkrFLjQtocJkoniLxtpSYSUew2mmoK0S5oVB7ea%2B2cJ879%2FFIlrv0JdvPJJ5lMTDXro6vMJFYsSoFFb%2BLKZOeMXu7t%2Fgb35riFgeyNqI4L9rsi9Uz%2F%2BIzgYf0%2FgQePZZ0nU6ytD1CCQFmfiwA3v3YBe5yS8EIZMzQObTJ0lt%2F6q9PCtzxoBiRYvVnmmy7Sh4TljUZDGnbrZBcAPO43qqNh7s13L7vNcfLj0ZOGf6JdGiv8BueJTnb3%2FN4ZMod24mh4IefJ284mQgYkdesMt20RPR4GWE5PUSYaD%2FJumxs84LkCufsszyXO39JSKYD0kYLJx5jFkMFR0tIm%2FIIGUEvwswVK4ruBcuaTpZNAUh8JLTQgl9TZq64X99Y27O9bbbohxbG8ayUkG9cpLBLTV6CFMNWQ57wGOqUBPI9otiJ%2FvoAgDsmkl9hFO3J4hp4sbyQ%2B0nGL9wf4wygf5xn8M0x6JebflHk0guxKlJ8Uyv2bwK7u7AlkgPaivghHBanVClBO57ILPLXNG1bLGdreRkfeYocBO7PkVf1FfNgGJVzoEN9h2jRPsZ%2Bok64Ui5eovncJm891DU0uUoGM766U1XJxsxYbLTsVNTPo8YQrzx0q4QoYl3QGCy7jAuLVpqiW&X-Amz-Signature=83f373d518921759cf378ccd8ae25bb9ecd379940edef82183bb077a427fb723&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KDIX5HV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIFeCOfn6QiCdy6L6vRYohH8rHteJDMwnq92zRijrq%2BBhAiEA2ob4qXmR%2BDmIFKCysFiuRrjrDRPJdFVs3Xjbqp3VlAQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLmSPchsYuJjNaVIwSrcA5e0siOkzBSrE816%2BOn8Oq9Q0p4%2BxCwySFq8gotI6SIAr4QmazaD8iSvmJKtwS%2FKDbwPb2Atejvhyng5tHPim49xqaXCyDVnn%2Bmlgdj1%2B%2BAV4OCVdVtdUpRab5xHIiLsgALjShxKg7LAMCjlHyGjCEcoHJEp7g4%2BSdeNi%2B7AHntozzMtX%2FvGGivNrplopI5Cid8eGRV6D%2FsA9WefffyuiLAGKByFzGCZo8V%2B2qDVgQucCSEkr3%2Fq1FiY11O2rcoLGtvaDB%2B83zErgNS9VSaOYlVkHK2BSr%2BSWIah9gQWebywDgUkR6cr%2BhRHoQTfED%2F2ywNFmgk39qJnXFuHm1MAc7480v5jSZFPR1zSHYdKdGU8dSAQkSgJgI2ssEGevPPlKECW7KFy5GhuRxTMHhBK0ArxVhZH%2BwxikiXAjYMSCVh0rWyNcN9tFrLWZd7XBSVMq%2BEUdMLduIzt6o%2FYPRXUUida0IYjDAkDb3Yq18pHGSxPXDlj2YjdaXi3HmQa3h3LoX7S%2Fvd1heWKcMhWFdIGpMwkvZLZk78N4H5oLnpljniKLiTNGYUisHXF6dOpCnRgwNcBuqOECeOlPnrpt3AxCnNiespTOIbW6xELckbMCKSYv07yUWqxH7Am%2BDdDMKOQ57wGOqUBxjt8ZEgVOdIrM5YTAH6LKMkA9l44VKvcfo4xe0w8WZgZRsx4mmmrdWQP9EIQ%2Fj%2B7i4Hw7rF3I2ctB6nuC4%2Bn50hZv2%2BT2LVA1YrMsJhUTdh%2BCZ2ZN8zHjjLpjPn1v8nC3Bwrzpr%2BusKMaGnIswcxPdIlI5q4qzc48ffqr%2BuJAM7bn0KsJBO4YuDAx3735COyCCIPx%2B4kwOOfplmrHpqIcln1sELU&X-Amz-Signature=d7c3a260b1ee19309801bebfd6881ae03e81f680dec9461e82fcb675a327372d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KDIX5HV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIFeCOfn6QiCdy6L6vRYohH8rHteJDMwnq92zRijrq%2BBhAiEA2ob4qXmR%2BDmIFKCysFiuRrjrDRPJdFVs3Xjbqp3VlAQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLmSPchsYuJjNaVIwSrcA5e0siOkzBSrE816%2BOn8Oq9Q0p4%2BxCwySFq8gotI6SIAr4QmazaD8iSvmJKtwS%2FKDbwPb2Atejvhyng5tHPim49xqaXCyDVnn%2Bmlgdj1%2B%2BAV4OCVdVtdUpRab5xHIiLsgALjShxKg7LAMCjlHyGjCEcoHJEp7g4%2BSdeNi%2B7AHntozzMtX%2FvGGivNrplopI5Cid8eGRV6D%2FsA9WefffyuiLAGKByFzGCZo8V%2B2qDVgQucCSEkr3%2Fq1FiY11O2rcoLGtvaDB%2B83zErgNS9VSaOYlVkHK2BSr%2BSWIah9gQWebywDgUkR6cr%2BhRHoQTfED%2F2ywNFmgk39qJnXFuHm1MAc7480v5jSZFPR1zSHYdKdGU8dSAQkSgJgI2ssEGevPPlKECW7KFy5GhuRxTMHhBK0ArxVhZH%2BwxikiXAjYMSCVh0rWyNcN9tFrLWZd7XBSVMq%2BEUdMLduIzt6o%2FYPRXUUida0IYjDAkDb3Yq18pHGSxPXDlj2YjdaXi3HmQa3h3LoX7S%2Fvd1heWKcMhWFdIGpMwkvZLZk78N4H5oLnpljniKLiTNGYUisHXF6dOpCnRgwNcBuqOECeOlPnrpt3AxCnNiespTOIbW6xELckbMCKSYv07yUWqxH7Am%2BDdDMKOQ57wGOqUBxjt8ZEgVOdIrM5YTAH6LKMkA9l44VKvcfo4xe0w8WZgZRsx4mmmrdWQP9EIQ%2Fj%2B7i4Hw7rF3I2ctB6nuC4%2Bn50hZv2%2BT2LVA1YrMsJhUTdh%2BCZ2ZN8zHjjLpjPn1v8nC3Bwrzpr%2BusKMaGnIswcxPdIlI5q4qzc48ffqr%2BuJAM7bn0KsJBO4YuDAx3735COyCCIPx%2B4kwOOfplmrHpqIcln1sELU&X-Amz-Signature=91a293638b9cdb544383adbcd81303dd028d6aae5a4628f00fa398d8fdc3f1a8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KDIX5HV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIFeCOfn6QiCdy6L6vRYohH8rHteJDMwnq92zRijrq%2BBhAiEA2ob4qXmR%2BDmIFKCysFiuRrjrDRPJdFVs3Xjbqp3VlAQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLmSPchsYuJjNaVIwSrcA5e0siOkzBSrE816%2BOn8Oq9Q0p4%2BxCwySFq8gotI6SIAr4QmazaD8iSvmJKtwS%2FKDbwPb2Atejvhyng5tHPim49xqaXCyDVnn%2Bmlgdj1%2B%2BAV4OCVdVtdUpRab5xHIiLsgALjShxKg7LAMCjlHyGjCEcoHJEp7g4%2BSdeNi%2B7AHntozzMtX%2FvGGivNrplopI5Cid8eGRV6D%2FsA9WefffyuiLAGKByFzGCZo8V%2B2qDVgQucCSEkr3%2Fq1FiY11O2rcoLGtvaDB%2B83zErgNS9VSaOYlVkHK2BSr%2BSWIah9gQWebywDgUkR6cr%2BhRHoQTfED%2F2ywNFmgk39qJnXFuHm1MAc7480v5jSZFPR1zSHYdKdGU8dSAQkSgJgI2ssEGevPPlKECW7KFy5GhuRxTMHhBK0ArxVhZH%2BwxikiXAjYMSCVh0rWyNcN9tFrLWZd7XBSVMq%2BEUdMLduIzt6o%2FYPRXUUida0IYjDAkDb3Yq18pHGSxPXDlj2YjdaXi3HmQa3h3LoX7S%2Fvd1heWKcMhWFdIGpMwkvZLZk78N4H5oLnpljniKLiTNGYUisHXF6dOpCnRgwNcBuqOECeOlPnrpt3AxCnNiespTOIbW6xELckbMCKSYv07yUWqxH7Am%2BDdDMKOQ57wGOqUBxjt8ZEgVOdIrM5YTAH6LKMkA9l44VKvcfo4xe0w8WZgZRsx4mmmrdWQP9EIQ%2Fj%2B7i4Hw7rF3I2ctB6nuC4%2Bn50hZv2%2BT2LVA1YrMsJhUTdh%2BCZ2ZN8zHjjLpjPn1v8nC3Bwrzpr%2BusKMaGnIswcxPdIlI5q4qzc48ffqr%2BuJAM7bn0KsJBO4YuDAx3735COyCCIPx%2B4kwOOfplmrHpqIcln1sELU&X-Amz-Signature=d081e6663c6ce5cf95f39c2a9dd19dbaa0eb06636a61fd80c57e5cc9889e221c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KDIX5HV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIFeCOfn6QiCdy6L6vRYohH8rHteJDMwnq92zRijrq%2BBhAiEA2ob4qXmR%2BDmIFKCysFiuRrjrDRPJdFVs3Xjbqp3VlAQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLmSPchsYuJjNaVIwSrcA5e0siOkzBSrE816%2BOn8Oq9Q0p4%2BxCwySFq8gotI6SIAr4QmazaD8iSvmJKtwS%2FKDbwPb2Atejvhyng5tHPim49xqaXCyDVnn%2Bmlgdj1%2B%2BAV4OCVdVtdUpRab5xHIiLsgALjShxKg7LAMCjlHyGjCEcoHJEp7g4%2BSdeNi%2B7AHntozzMtX%2FvGGivNrplopI5Cid8eGRV6D%2FsA9WefffyuiLAGKByFzGCZo8V%2B2qDVgQucCSEkr3%2Fq1FiY11O2rcoLGtvaDB%2B83zErgNS9VSaOYlVkHK2BSr%2BSWIah9gQWebywDgUkR6cr%2BhRHoQTfED%2F2ywNFmgk39qJnXFuHm1MAc7480v5jSZFPR1zSHYdKdGU8dSAQkSgJgI2ssEGevPPlKECW7KFy5GhuRxTMHhBK0ArxVhZH%2BwxikiXAjYMSCVh0rWyNcN9tFrLWZd7XBSVMq%2BEUdMLduIzt6o%2FYPRXUUida0IYjDAkDb3Yq18pHGSxPXDlj2YjdaXi3HmQa3h3LoX7S%2Fvd1heWKcMhWFdIGpMwkvZLZk78N4H5oLnpljniKLiTNGYUisHXF6dOpCnRgwNcBuqOECeOlPnrpt3AxCnNiespTOIbW6xELckbMCKSYv07yUWqxH7Am%2BDdDMKOQ57wGOqUBxjt8ZEgVOdIrM5YTAH6LKMkA9l44VKvcfo4xe0w8WZgZRsx4mmmrdWQP9EIQ%2Fj%2B7i4Hw7rF3I2ctB6nuC4%2Bn50hZv2%2BT2LVA1YrMsJhUTdh%2BCZ2ZN8zHjjLpjPn1v8nC3Bwrzpr%2BusKMaGnIswcxPdIlI5q4qzc48ffqr%2BuJAM7bn0KsJBO4YuDAx3735COyCCIPx%2B4kwOOfplmrHpqIcln1sELU&X-Amz-Signature=e824a4f1ae51d95dd970ed9dbd17061666ac3934eaade3f7906b4b8fe3b752ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KDIX5HV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIFeCOfn6QiCdy6L6vRYohH8rHteJDMwnq92zRijrq%2BBhAiEA2ob4qXmR%2BDmIFKCysFiuRrjrDRPJdFVs3Xjbqp3VlAQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLmSPchsYuJjNaVIwSrcA5e0siOkzBSrE816%2BOn8Oq9Q0p4%2BxCwySFq8gotI6SIAr4QmazaD8iSvmJKtwS%2FKDbwPb2Atejvhyng5tHPim49xqaXCyDVnn%2Bmlgdj1%2B%2BAV4OCVdVtdUpRab5xHIiLsgALjShxKg7LAMCjlHyGjCEcoHJEp7g4%2BSdeNi%2B7AHntozzMtX%2FvGGivNrplopI5Cid8eGRV6D%2FsA9WefffyuiLAGKByFzGCZo8V%2B2qDVgQucCSEkr3%2Fq1FiY11O2rcoLGtvaDB%2B83zErgNS9VSaOYlVkHK2BSr%2BSWIah9gQWebywDgUkR6cr%2BhRHoQTfED%2F2ywNFmgk39qJnXFuHm1MAc7480v5jSZFPR1zSHYdKdGU8dSAQkSgJgI2ssEGevPPlKECW7KFy5GhuRxTMHhBK0ArxVhZH%2BwxikiXAjYMSCVh0rWyNcN9tFrLWZd7XBSVMq%2BEUdMLduIzt6o%2FYPRXUUida0IYjDAkDb3Yq18pHGSxPXDlj2YjdaXi3HmQa3h3LoX7S%2Fvd1heWKcMhWFdIGpMwkvZLZk78N4H5oLnpljniKLiTNGYUisHXF6dOpCnRgwNcBuqOECeOlPnrpt3AxCnNiespTOIbW6xELckbMCKSYv07yUWqxH7Am%2BDdDMKOQ57wGOqUBxjt8ZEgVOdIrM5YTAH6LKMkA9l44VKvcfo4xe0w8WZgZRsx4mmmrdWQP9EIQ%2Fj%2B7i4Hw7rF3I2ctB6nuC4%2Bn50hZv2%2BT2LVA1YrMsJhUTdh%2BCZ2ZN8zHjjLpjPn1v8nC3Bwrzpr%2BusKMaGnIswcxPdIlI5q4qzc48ffqr%2BuJAM7bn0KsJBO4YuDAx3735COyCCIPx%2B4kwOOfplmrHpqIcln1sELU&X-Amz-Signature=eb604b71c082d6abb2c9cd2ac71e99dbdcd1f111e112ea9987fac6205205040b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KDIX5HV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIFeCOfn6QiCdy6L6vRYohH8rHteJDMwnq92zRijrq%2BBhAiEA2ob4qXmR%2BDmIFKCysFiuRrjrDRPJdFVs3Xjbqp3VlAQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLmSPchsYuJjNaVIwSrcA5e0siOkzBSrE816%2BOn8Oq9Q0p4%2BxCwySFq8gotI6SIAr4QmazaD8iSvmJKtwS%2FKDbwPb2Atejvhyng5tHPim49xqaXCyDVnn%2Bmlgdj1%2B%2BAV4OCVdVtdUpRab5xHIiLsgALjShxKg7LAMCjlHyGjCEcoHJEp7g4%2BSdeNi%2B7AHntozzMtX%2FvGGivNrplopI5Cid8eGRV6D%2FsA9WefffyuiLAGKByFzGCZo8V%2B2qDVgQucCSEkr3%2Fq1FiY11O2rcoLGtvaDB%2B83zErgNS9VSaOYlVkHK2BSr%2BSWIah9gQWebywDgUkR6cr%2BhRHoQTfED%2F2ywNFmgk39qJnXFuHm1MAc7480v5jSZFPR1zSHYdKdGU8dSAQkSgJgI2ssEGevPPlKECW7KFy5GhuRxTMHhBK0ArxVhZH%2BwxikiXAjYMSCVh0rWyNcN9tFrLWZd7XBSVMq%2BEUdMLduIzt6o%2FYPRXUUida0IYjDAkDb3Yq18pHGSxPXDlj2YjdaXi3HmQa3h3LoX7S%2Fvd1heWKcMhWFdIGpMwkvZLZk78N4H5oLnpljniKLiTNGYUisHXF6dOpCnRgwNcBuqOECeOlPnrpt3AxCnNiespTOIbW6xELckbMCKSYv07yUWqxH7Am%2BDdDMKOQ57wGOqUBxjt8ZEgVOdIrM5YTAH6LKMkA9l44VKvcfo4xe0w8WZgZRsx4mmmrdWQP9EIQ%2Fj%2B7i4Hw7rF3I2ctB6nuC4%2Bn50hZv2%2BT2LVA1YrMsJhUTdh%2BCZ2ZN8zHjjLpjPn1v8nC3Bwrzpr%2BusKMaGnIswcxPdIlI5q4qzc48ffqr%2BuJAM7bn0KsJBO4YuDAx3735COyCCIPx%2B4kwOOfplmrHpqIcln1sELU&X-Amz-Signature=2688693986853dced7ce1439708a90229c910e7384f5636232aad3c68b2c2379&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZJ5B2UT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCgzNLnC2yx%2BmfD8EVFM7UjCF6Tmht9KTVpJckp64teRwIhAJ%2ByXTvdwa7vA62xqvMM2cw%2FxdWin9SAviUaArvOh1CLKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVv84D81ZKoVe7QCYq3APaW5TJY1dybGXGW09ktN7Fn2pkLwuok03yN1S1CXuXCknCAg0nCZnXqqnbr20cOqxb%2B%2B7h%2FqlVRg0IdLAQKqLckSRP522W8zQ4hlg3AuI80hP9r4WhGRnWegfNZrKXUkr2hQUommK%2Bwu6OYZ%2Ff%2BuuK6LMUhgYu2sY7C9Onux7Lpvqeg7WvXGY8zagANQDwc%2FBkL6j%2Fugx6jsUypDHh9eL4UfIo1vMdmm3z5zEp3Jf7Ii6Ddn0EmsI6nYn472adCNCEnnx8glyK7wBfMj%2Fclspu2hxgaFq1Y%2B21jYxatF5hR5JOZaFMAncIjSreM1ugwwJb4xOMlcqGRHoFGi6ABQ%2FlzUWszELQMdoOgUcxuRSxC0lVJ3M%2F9IV1%2BpZqeuN%2Bvk%2BtS6FIL47PujY%2BUq3f%2B70Kb0C0jXse%2BGTt5dYkWIrafqCwCnBuQ7jD7wtCgIgp67L1D5e%2FabV0Ew6wbozBq7SvrDkvUFtnF0cyiJFRVcMSBv%2B5qANntsvALFlHtq%2BU4UHoQ3X3XJrOgWv6WOXy8QWHQpM0fmwwpxPg5Bqdjg2Xtuork4ICpVwzIs6mfHkWbg0QUvB3b%2BBMA0GWqvU1y6Om9FM54US4IpR9xxLh9p%2BtFZ52pxls2EVHY%2FRkhzD6uua8BjqkAX%2FqHGsa12LlyGWeK8VDRZAM7F50dHIsq1jQEa3weLtkStIW4u1oIvnIguKBzAYVtVXcRNr6ryDCZeB5JhugZwBIwbow3jCX7lZuuyhUe0OUTet%2FHIQq1ZmwESN14G%2BzYjWkF190knpqN%2FjcgXrEAxMkpwzNkmR2JdqrUAqgUcbfQmLnE9sOoQbZWbS4Sn4F70%2BjPnYC%2FWjdtG8qNbqRQzZpymMH&X-Amz-Signature=bb537e53c36f83f132a0ad6a437fce10a7f4f2034421932e1ab9f28bbcd2c749&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVRCD3RE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIAaMezd%2Fc1Kh0OfHrMz6xKiTOMKNYBZhubNu7YGjNO2IAiBrAleQrOBDPApGXGd7kPYUA57NKdxva5bCiDvsK%2BTqsyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMh%2BniAX7JyduPnZ0RKtwDRISgKhfx7lc%2F3uFesx3cMqcZ3vy90gPCEf37EASXB%2FsR48OIxDvCrwyEpeZG2bC9ynvBgIrsoH64uz3AYI7tE06fBXafZeRjqChtdONw9CntHAyvecJtRTOU%2FfiB7AnyYM5xWZIuQ0YvgdriOHN0Dz61ACHOqiTVreVDP%2BjjOkMCocpBZ94oqAxjLHOwhLKfUmGpoTZE8MzK7IGmtkdrgOJVCgr0r2%2FYR5WthPJ3ZQdJAR%2FDo9g5EZv3fLWddVayY9WYd5rbw3skBDjyWovB7pnR4TCN1%2BNvfxpqqQEeBkNtDDgR88E4Dt9Okp%2BKQsshLFARRPwup%2Bd%2B7ptazx7P%2FqAdg%2BX9yFfeqyMFeh2ctg5MDH6yTUN4MwDaOPIXxwPzDVVtmpz6aDxgn8GhEeNIMdAxGmg1qm%2B0o4FNifliSYwyARI72olMgLKnvbpzLj8UMsVIFroZRaSNvAvnIW8n7CQicenaoOiiWR5wHKea4J6rQ08aRORjQMD%2BjFTPEjwfQmr6PtsU3zDLNjGmz3nmbqtabjS2DsaJG8FSKONvsOQJNsdHVlOcIAaYK0o3ud6CUQicSlNHdRSjjLvQXJznPJ59C1jPFdtAwOu4q79MkIDgMwA%2BSshB1KaD%2BYsw3rrmvAY6pgG0TCK07eYxtweWWYoR0fN13ZmdvR96CWAwG4OuvGxN2UGn2cBQX%2FKpNiXYEob792Zz4Qoi%2B%2FZwcefIr4wSvI1Ex4hsSXz7VivF9XgJHmiQsgv2QHAt4pvQCAnfYRH84WWtvo%2BGbTzXIWNWMSC2MCgTsWipLr10jSwv2eerbpU%2BwOAqeztKjZWxviMfHuJ%2BRTLPrZWMQ6PQK7WzUxiU0kVssXdvR1%2FE&X-Amz-Signature=0716c74136acbea845d3617063917799d74bcdd744af30928575bc6786124dc5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KDIX5HV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIFeCOfn6QiCdy6L6vRYohH8rHteJDMwnq92zRijrq%2BBhAiEA2ob4qXmR%2BDmIFKCysFiuRrjrDRPJdFVs3Xjbqp3VlAQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLmSPchsYuJjNaVIwSrcA5e0siOkzBSrE816%2BOn8Oq9Q0p4%2BxCwySFq8gotI6SIAr4QmazaD8iSvmJKtwS%2FKDbwPb2Atejvhyng5tHPim49xqaXCyDVnn%2Bmlgdj1%2B%2BAV4OCVdVtdUpRab5xHIiLsgALjShxKg7LAMCjlHyGjCEcoHJEp7g4%2BSdeNi%2B7AHntozzMtX%2FvGGivNrplopI5Cid8eGRV6D%2FsA9WefffyuiLAGKByFzGCZo8V%2B2qDVgQucCSEkr3%2Fq1FiY11O2rcoLGtvaDB%2B83zErgNS9VSaOYlVkHK2BSr%2BSWIah9gQWebywDgUkR6cr%2BhRHoQTfED%2F2ywNFmgk39qJnXFuHm1MAc7480v5jSZFPR1zSHYdKdGU8dSAQkSgJgI2ssEGevPPlKECW7KFy5GhuRxTMHhBK0ArxVhZH%2BwxikiXAjYMSCVh0rWyNcN9tFrLWZd7XBSVMq%2BEUdMLduIzt6o%2FYPRXUUida0IYjDAkDb3Yq18pHGSxPXDlj2YjdaXi3HmQa3h3LoX7S%2Fvd1heWKcMhWFdIGpMwkvZLZk78N4H5oLnpljniKLiTNGYUisHXF6dOpCnRgwNcBuqOECeOlPnrpt3AxCnNiespTOIbW6xELckbMCKSYv07yUWqxH7Am%2BDdDMKOQ57wGOqUBxjt8ZEgVOdIrM5YTAH6LKMkA9l44VKvcfo4xe0w8WZgZRsx4mmmrdWQP9EIQ%2Fj%2B7i4Hw7rF3I2ctB6nuC4%2Bn50hZv2%2BT2LVA1YrMsJhUTdh%2BCZ2ZN8zHjjLpjPn1v8nC3Bwrzpr%2BusKMaGnIswcxPdIlI5q4qzc48ffqr%2BuJAM7bn0KsJBO4YuDAx3735COyCCIPx%2B4kwOOfplmrHpqIcln1sELU&X-Amz-Signature=19f653733b4fdb7f75ca9288759ae316644b7f6b8614f98b3f3ffd096df5a7ef&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KDIX5HV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIFeCOfn6QiCdy6L6vRYohH8rHteJDMwnq92zRijrq%2BBhAiEA2ob4qXmR%2BDmIFKCysFiuRrjrDRPJdFVs3Xjbqp3VlAQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLmSPchsYuJjNaVIwSrcA5e0siOkzBSrE816%2BOn8Oq9Q0p4%2BxCwySFq8gotI6SIAr4QmazaD8iSvmJKtwS%2FKDbwPb2Atejvhyng5tHPim49xqaXCyDVnn%2Bmlgdj1%2B%2BAV4OCVdVtdUpRab5xHIiLsgALjShxKg7LAMCjlHyGjCEcoHJEp7g4%2BSdeNi%2B7AHntozzMtX%2FvGGivNrplopI5Cid8eGRV6D%2FsA9WefffyuiLAGKByFzGCZo8V%2B2qDVgQucCSEkr3%2Fq1FiY11O2rcoLGtvaDB%2B83zErgNS9VSaOYlVkHK2BSr%2BSWIah9gQWebywDgUkR6cr%2BhRHoQTfED%2F2ywNFmgk39qJnXFuHm1MAc7480v5jSZFPR1zSHYdKdGU8dSAQkSgJgI2ssEGevPPlKECW7KFy5GhuRxTMHhBK0ArxVhZH%2BwxikiXAjYMSCVh0rWyNcN9tFrLWZd7XBSVMq%2BEUdMLduIzt6o%2FYPRXUUida0IYjDAkDb3Yq18pHGSxPXDlj2YjdaXi3HmQa3h3LoX7S%2Fvd1heWKcMhWFdIGpMwkvZLZk78N4H5oLnpljniKLiTNGYUisHXF6dOpCnRgwNcBuqOECeOlPnrpt3AxCnNiespTOIbW6xELckbMCKSYv07yUWqxH7Am%2BDdDMKOQ57wGOqUBxjt8ZEgVOdIrM5YTAH6LKMkA9l44VKvcfo4xe0w8WZgZRsx4mmmrdWQP9EIQ%2Fj%2B7i4Hw7rF3I2ctB6nuC4%2Bn50hZv2%2BT2LVA1YrMsJhUTdh%2BCZ2ZN8zHjjLpjPn1v8nC3Bwrzpr%2BusKMaGnIswcxPdIlI5q4qzc48ffqr%2BuJAM7bn0KsJBO4YuDAx3735COyCCIPx%2B4kwOOfplmrHpqIcln1sELU&X-Amz-Signature=d260880ee773279d8685455303989dc5dcd30e54347dd21bf7a6005a8363fe20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KDIX5HV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIFeCOfn6QiCdy6L6vRYohH8rHteJDMwnq92zRijrq%2BBhAiEA2ob4qXmR%2BDmIFKCysFiuRrjrDRPJdFVs3Xjbqp3VlAQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLmSPchsYuJjNaVIwSrcA5e0siOkzBSrE816%2BOn8Oq9Q0p4%2BxCwySFq8gotI6SIAr4QmazaD8iSvmJKtwS%2FKDbwPb2Atejvhyng5tHPim49xqaXCyDVnn%2Bmlgdj1%2B%2BAV4OCVdVtdUpRab5xHIiLsgALjShxKg7LAMCjlHyGjCEcoHJEp7g4%2BSdeNi%2B7AHntozzMtX%2FvGGivNrplopI5Cid8eGRV6D%2FsA9WefffyuiLAGKByFzGCZo8V%2B2qDVgQucCSEkr3%2Fq1FiY11O2rcoLGtvaDB%2B83zErgNS9VSaOYlVkHK2BSr%2BSWIah9gQWebywDgUkR6cr%2BhRHoQTfED%2F2ywNFmgk39qJnXFuHm1MAc7480v5jSZFPR1zSHYdKdGU8dSAQkSgJgI2ssEGevPPlKECW7KFy5GhuRxTMHhBK0ArxVhZH%2BwxikiXAjYMSCVh0rWyNcN9tFrLWZd7XBSVMq%2BEUdMLduIzt6o%2FYPRXUUida0IYjDAkDb3Yq18pHGSxPXDlj2YjdaXi3HmQa3h3LoX7S%2Fvd1heWKcMhWFdIGpMwkvZLZk78N4H5oLnpljniKLiTNGYUisHXF6dOpCnRgwNcBuqOECeOlPnrpt3AxCnNiespTOIbW6xELckbMCKSYv07yUWqxH7Am%2BDdDMKOQ57wGOqUBxjt8ZEgVOdIrM5YTAH6LKMkA9l44VKvcfo4xe0w8WZgZRsx4mmmrdWQP9EIQ%2Fj%2B7i4Hw7rF3I2ctB6nuC4%2Bn50hZv2%2BT2LVA1YrMsJhUTdh%2BCZ2ZN8zHjjLpjPn1v8nC3Bwrzpr%2BusKMaGnIswcxPdIlI5q4qzc48ffqr%2BuJAM7bn0KsJBO4YuDAx3735COyCCIPx%2B4kwOOfplmrHpqIcln1sELU&X-Amz-Signature=d03663d24c7b0676be59b82302d3f7c654326b72fdd62e8d4587cdc7e783f7dd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636RFJWDT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDbRBjCk6YHbFwaWcGkmLN8bg9wqWHW9YZ2tKBgYGzWIwIhAIaIVpfAORVYBc%2FvcBltdapweA6oFqscDw6sJ%2FNcF4lLKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZymD3M0PNFmuFVjsq3AN%2BYxNp2G%2FZTwpVlFqupDC6JEHYcSX3YcPDhiZMwFuYdL3v3RYieBZ8X0T2q2dWAzcjH0kg6IfyLmnA%2FUcnCGhlGYsvejZwOJk%2FqTJfH5Q7qh3N59RfJ%2B3JqdNssey1UJVYOpYBIAvyM%2F5XvDyq%2FQl0IB60WWGQ70BXQJ797WTZdRyRwqN9lnSE%2F3%2F%2Fu6DPg%2BsfFCCQlxMFHljvN99IutBWbQgTXN69Yxk2NkA3xflqo3A%2BdPZqabjBTFLx5dNAavFje40svK8HfonMsG%2BclJXOXkwsPNtSeQLNdU9gAYFTduoQyY98fn5QckQEfB3v8xTlFXAi6TWDPAwEyJY%2BI1NmhzV7ntP2ExYzMOHr%2FlKhYxVWILveEloV0sNwSmF0DycHTSlRDbYVcMT%2BhKlJmO%2Bza%2BwAZ3m6AMaKztRXywHI8PaoWbGQrxFP%2BEHY%2F8cXNeTkGjlGLQP6z64yl1OcCZnSuAb3N9HhhCa6mKjD0ODggeTITdTa%2FCRPsrG5dfZzx1EXROcZKnkW0YRppZ7WXJuGNGE%2FtNhFmcgypYxk%2FPl%2BL2kmWlxj8z5PGClT1MnJgtGaYeSVNlj9QikuwGennQU8%2BKMGwPJ56Ne4D2n9ypng9EoP3S4I3itWkOh9TzCHkOe8BjqkAUXqANcTOByOLtixS4Y7XOaLiM%2FsEEBTWkCYQi4rMxFxhJJRq0KdNaVW%2F2qbdJ9IKBbQOndQ3ZtO8ZbiH0gbykl8Bqe1gTHIzbjuCChfbFUPXv6xviqIViYnRls88JU3cGygnySVx1o9NeKsmH3uY1Fe2l1%2FcX8RZtZATnd6G9WYPPvK1stcxTVpYh8a1w0YcKD%2BYusuquny%2BkwWovqABdBptVKC&X-Amz-Signature=6011a7177f71d794873cc23e3fc76cf73a82f4eef20680dc5c4e727c731bf887&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466255IZD3F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQCiGvEha4mqttzNhmoHoijEdIu%2FDEa0Gl5svoa1ycG%2FQwIhANREs62HG0ORJoH7oIjpSXe%2F9P4pkUBoK9iNeJ2y3xmTKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzITsKenfm628Eve18q3APAVnXyM3gTGM8f%2FodXr0wTkmpAFELepbIHLHFsWw8iNKfzK0B5q3Vn23GHmAukth9wQUs6Ex7NAC%2FRvzGvkKskY3mJEbDnAjdLRkknjP4OVRa4naY0smVE0Ab5%2F1Ttv9V8kTjC2G8lefslQiZMb075rmlgdG0981uoQ72F3stJx1J5KcW2hXm7wR9aUnAPqa89GbQmtVVV1tv07okELEiLbgpZ029JIhOf4I25Tlnp9Wb7znvI7VF3wspZCFFO0BMSGGsZN1YZj4MF15UAI45s4d15OHGno1g1%2FJ6B134Em13Vrqj08T0ik9i749XgedMykGk3OtIb7Bsl9gAbKNDc27OGcDfDIiqAu6v2CEneAXxSWEcICQ4lFFYpP%2FGmi4MqCWIrK5yUoa%2FKrBJjlRGtcqdhTk1DQowcMPfsh3b3EbgrmBdmqyikpUzvgrUbCoEzgcurbWjM9AgX006RqzOiFmqmo2ZpJoLNs1YTloZZe%2Bc9KW2E9e6KrS7gJvOLHrGtGTiRBQjDCpIW4j%2FNs%2Bm9kQurBt7SuJWvujzykJ%2FzePAWqrNhgsyYF56JPDk4bM4IRAcXgHdnjMa6J%2BeoDYXZT9FuKjD02LHI1lwodngqQPwB4SW1MNXjQxdxmDD9j%2Be8BjqkAWmTybCU4blTMsoTfj1AaySZEHq%2FGI7DRohNjy3shTalOO5oXcU6oOXjlC54v0vxw%2BWBH6n21qWzYe9KciFSjW%2FwZb%2F8VNLUIpp8cbBBr9mJRhRVH1xbQHU9bM82MK1FCW3VCNT5eAZo3LUZ7oGFAddNwZf4%2FDXnaW8IeDDrcGRAybMrPqcNd%2F8ivakVAi3Lrxohjt%2FU03V4LUWLI89LIPt7pehU&X-Amz-Signature=a08b344054a161e23a81cc91288aa8aedc985bd6ad732f0528fe69406c5d9fdf&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T75PD43C%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCR7tcJZx05Ri6F2Y6X6EQq0RmJaEgtDyao4USW9KJ7NwIgBpXzr4AyoZyqeHUpNjFfEFnWPmhCM9bg1YXSJaj5Yn0qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH4rJpZbr4wNG5k%2FqSrcA0deMNZp4GiqAMkrXL5oshWpXakLLVxcUUt93IxG0r0ySbTcJ5icrzA%2BeoF9KLMGZWOkm1fo1TkCb5AGRdrFfwnaftAG9KF0xGWd3yTmgx27QBrvuBHoQuFGxLdYqRJ8%2BO5l5F2pWrG9wvStJXEVyyfQdQgfv4bE3CGGqDZ%2FEuPrCKY%2BbZYu9fONXqlk6649xBrl0OW%2FkFHvLvAoLw5XZAM8MrO3MJ1zdtnPIQ%2Bkv8IygFJZ0p%2BReRByV6RXVVEJrKRGXMNC701DNfwalrVrF4oTSVJ9zGgluYdZU5v3teNG3FF%2FwuGoQH%2B5JKywedIctres%2BFzY7XFqSIHfLXODGJXEGDtN%2BA8VfN0WGYQQjDzYz32rMXaKDkdQADsbUUIunGSEuXxNVxGFhXCTEZKsUBRuGNo8vF2s0TVMoM7Ia1VqxgGtZ9E3e%2F7AOnINzXbP%2F8g8wkYwOrMEB9aqM9U%2FIqbC6rTJ22mdImeoKvElOpW%2BpLlmA0dFccF1fjh%2FKhzU%2BZiNrd4mnFxjlX3DuFspmx6J1HoKhFH7V9484dXVAb4qCRAHS2eNKV%2FhpvFCJ4UyJzNWoMSr1Y3QWRqOrM2EBV2IObVqhyrxx4NAfX%2FbMsdWR1bI7m7Soy76VcEeMKuQ57wGOqUBiTh7eQlCheIVJMwePOIw6RaJyRcrDtJWes8MG8MEg0%2Fi7g1a4eaSL2wXoM1IkTs2XLVS557wPTD62NTIq9mZUwYxMTg1RJBqtJ08YfKIR5wALwSjoy4P0ozRj7VflIDIocfn6HNc7%2B9amfJySgfstkp4Wcm6TsiIoxcmLCviT0UhvhTGp%2BCRA3WYVKIPVekw59K0tnJjsxDfCxCaDzUHtHPjbXa2&X-Amz-Signature=246ca647f2eb99f21b2e7f0ad7b843c9691cb6a90be4a01f9f02a90ccca69443&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662VLZEFL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICmBrI5LHC9ceSiQmmaVdOEcP%2BCAHozBvrJPx%2B5KoCGfAiEAhWPLUTl8wk9MLvyRGgWs8h0%2F4jEwmVwuuSKXZrX%2BsW8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOrEaVlUzbO%2B7nRJmCrcA%2FqF%2BD%2FUUWKFQoBiv61VF9O%2B7gpjvnz6zGAAr2VIftg6bhLoY4%2BnzIZIGPoMm%2Bt6%2FGT2ki5enRT%2F%2B9cEStTHcAaoePgVTP2lMYh5Yz8U0pT%2BKTALgdzre7wkBlPrrjzvgeS6uSJ%2FmM3151mBhIb9l4HXTflL%2Bz0icuwugy1hG6kDUaZoC7ax4T9WvTcQftAtpd4ig7BREZGUm2Ydrig0tRgZsDJ%2Fjt2E8qpesORthrb4psU1gl%2FMQqiGbqEbjcBweK20Mc98XmYB7x1VLXU8z80BXEui%2BCZz1MqEac6%2FmvxKuL6uYVSEIAPBmMBc476h3pE5vfNghiTHffR6SRtCpqWmwr%2BYsPd7SPzrh7NzcHboXysEmimIEPqfNz%2Fr9oXAbVuel%2Bwy8A6IFhWyOtp8oIH4OWGu1q0F33sIMPTzlOSYwEYUb1EyfC3%2FddS8IVDoKLuMOxkZgHnzZvurzH%2FyarPOwFpe%2B63a9Iyb%2FY2Ai%2FEoxhbVhON5F4AvqMi2O7B1IgLbeWVH8Xy1QMXnqTuVlW9IKvKBlRPks3SPYWvo6nG%2B7eeRwmtc3hHlWx14mnADcFmjjDpLOnlcI60SKFkU3Ekt9N8haRLlvwyYCAeusDkOMfgnXOWW%2BewSikD6MMi75rwGOqUBYEbk5Sj4YugYAzbsz6s4qKG3wE%2B6oVUjpjfloInqpiREzeA6nlaKkajdb1eInTlsQFi0GbVQf%2FPI%2FZM8MkGkVA%2F7ZkObT6TCkbtmyh0FoIvTXeq55WcSU5ufXzkhL1Sro6myxNjI6BupnMscP1c0r529DqTcUZ8yAWx%2FZScgb40C%2BnBWEPv6EduEd1Rmjaz6TFyWqNRT%2FU%2BWkL1SIOuB3xkn%2F6gd&X-Amz-Signature=0447e656953996a311e0ec028ebe22f50e385d3933e3b6e33fbb8ade4d3d7dde&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662VLZEFL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICmBrI5LHC9ceSiQmmaVdOEcP%2BCAHozBvrJPx%2B5KoCGfAiEAhWPLUTl8wk9MLvyRGgWs8h0%2F4jEwmVwuuSKXZrX%2BsW8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOrEaVlUzbO%2B7nRJmCrcA%2FqF%2BD%2FUUWKFQoBiv61VF9O%2B7gpjvnz6zGAAr2VIftg6bhLoY4%2BnzIZIGPoMm%2Bt6%2FGT2ki5enRT%2F%2B9cEStTHcAaoePgVTP2lMYh5Yz8U0pT%2BKTALgdzre7wkBlPrrjzvgeS6uSJ%2FmM3151mBhIb9l4HXTflL%2Bz0icuwugy1hG6kDUaZoC7ax4T9WvTcQftAtpd4ig7BREZGUm2Ydrig0tRgZsDJ%2Fjt2E8qpesORthrb4psU1gl%2FMQqiGbqEbjcBweK20Mc98XmYB7x1VLXU8z80BXEui%2BCZz1MqEac6%2FmvxKuL6uYVSEIAPBmMBc476h3pE5vfNghiTHffR6SRtCpqWmwr%2BYsPd7SPzrh7NzcHboXysEmimIEPqfNz%2Fr9oXAbVuel%2Bwy8A6IFhWyOtp8oIH4OWGu1q0F33sIMPTzlOSYwEYUb1EyfC3%2FddS8IVDoKLuMOxkZgHnzZvurzH%2FyarPOwFpe%2B63a9Iyb%2FY2Ai%2FEoxhbVhON5F4AvqMi2O7B1IgLbeWVH8Xy1QMXnqTuVlW9IKvKBlRPks3SPYWvo6nG%2B7eeRwmtc3hHlWx14mnADcFmjjDpLOnlcI60SKFkU3Ekt9N8haRLlvwyYCAeusDkOMfgnXOWW%2BewSikD6MMi75rwGOqUBYEbk5Sj4YugYAzbsz6s4qKG3wE%2B6oVUjpjfloInqpiREzeA6nlaKkajdb1eInTlsQFi0GbVQf%2FPI%2FZM8MkGkVA%2F7ZkObT6TCkbtmyh0FoIvTXeq55WcSU5ufXzkhL1Sro6myxNjI6BupnMscP1c0r529DqTcUZ8yAWx%2FZScgb40C%2BnBWEPv6EduEd1Rmjaz6TFyWqNRT%2FU%2BWkL1SIOuB3xkn%2F6gd&X-Amz-Signature=5b9cd330bedea696526151817fc8dcdf67bfa8cb2b90edf4ee11ace60234f4dd&X-Amz-SignedHeaders=host&x-id=GetObject)

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
