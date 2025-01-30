

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y33SZN3Q%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgTANtZaL9mnvWRotdUJfq5ZUTcOaAShRcinsIWxSBEgIgVJ6hSFH0Vx1BcTUa6k0aTguVf7eQzz3y1lUe%2Fcnal6YqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKzRQitX%2FCNJxdeeAyrcA81skLpqFdfEyJT%2BJzqVSk6%2BAnXPg97hcyytOzUnLQqI1k5nNDaBdOEhJNhT02is9tzJSH0WG%2FXlCXOJrb8HAUwIWXKpadj9jTe1aS8iMpuDRN1XA2IV%2BblRfnGWWAV1xnZsm0JFmFJWoQuWKkWNm%2Bj6OC4kmIzfpojJK70Ib0WoldHTMpiYO8CJ8RFA0uxjW55lRcHakzT%2BM7kgoKAhhSQN%2FNCdjpfXXwZnDfZkIScYq0sILEgZdlBbk7ci4uZMjHyrZynaASaCtUpU0LtUfoRWfGKg6E1q8zVmwVzm1r0STuQChTn6I0NYt4tZ9uhtnQgiPeo%2Fm2SNwyPH2qW8d9%2B7CR2DG7N5q0MZjK6MGng%2BCppKBvEhFOXI6z8iNePIDXBq9CYjOrHs4A5i0i%2FgB3I4eBwBepOGtBSpjnXOfwJqszoB0LJ0zzBAVO9qe%2FPQqsv%2F7Vn36jfkxsaJRR4orkz4zdWHFPjCwwOW7O4ZNQGUkch5GnXR0y5bsY54GFN%2BJKbXfdn2OenUj0OXnjQdViAckaPfbM%2FtCCVon11Z7BSlAJpyVTPT4y8zln1Mj683mj8dYiEVd8GEZ7E80%2F1oijwbeKI%2F2wu%2FJL8o6CkPePCzxTXetDkAo23dOqRjMIWY7rwGOqUBbf%2BVrXap3v38YnBJlm9%2Bmmg7qQDyq2t9w3GKH9K1wjrGkBBH8yZ8lpF9ENb1S4ZVefHeKKIZeAIDEd%2FwQGvkQpCXKoB6yO2u%2FSsr85cPCxvKdaE%2Frlciw0xhYnW0iVmLG5C%2Fsm8u6%2FIXPyecqDx27nTrQr3%2BKY8%2FC07i2dC8Pn1vNPnTzPBDS5hS2%2BY2OexDE3o27b51L7I5yV9q8JCfkCPFzlnX&X-Amz-Signature=1f9ee749add0e0c87e547b0b35302d3bd5d295541f82e2b48056d443bac61674&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y33SZN3Q%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgTANtZaL9mnvWRotdUJfq5ZUTcOaAShRcinsIWxSBEgIgVJ6hSFH0Vx1BcTUa6k0aTguVf7eQzz3y1lUe%2Fcnal6YqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKzRQitX%2FCNJxdeeAyrcA81skLpqFdfEyJT%2BJzqVSk6%2BAnXPg97hcyytOzUnLQqI1k5nNDaBdOEhJNhT02is9tzJSH0WG%2FXlCXOJrb8HAUwIWXKpadj9jTe1aS8iMpuDRN1XA2IV%2BblRfnGWWAV1xnZsm0JFmFJWoQuWKkWNm%2Bj6OC4kmIzfpojJK70Ib0WoldHTMpiYO8CJ8RFA0uxjW55lRcHakzT%2BM7kgoKAhhSQN%2FNCdjpfXXwZnDfZkIScYq0sILEgZdlBbk7ci4uZMjHyrZynaASaCtUpU0LtUfoRWfGKg6E1q8zVmwVzm1r0STuQChTn6I0NYt4tZ9uhtnQgiPeo%2Fm2SNwyPH2qW8d9%2B7CR2DG7N5q0MZjK6MGng%2BCppKBvEhFOXI6z8iNePIDXBq9CYjOrHs4A5i0i%2FgB3I4eBwBepOGtBSpjnXOfwJqszoB0LJ0zzBAVO9qe%2FPQqsv%2F7Vn36jfkxsaJRR4orkz4zdWHFPjCwwOW7O4ZNQGUkch5GnXR0y5bsY54GFN%2BJKbXfdn2OenUj0OXnjQdViAckaPfbM%2FtCCVon11Z7BSlAJpyVTPT4y8zln1Mj683mj8dYiEVd8GEZ7E80%2F1oijwbeKI%2F2wu%2FJL8o6CkPePCzxTXetDkAo23dOqRjMIWY7rwGOqUBbf%2BVrXap3v38YnBJlm9%2Bmmg7qQDyq2t9w3GKH9K1wjrGkBBH8yZ8lpF9ENb1S4ZVefHeKKIZeAIDEd%2FwQGvkQpCXKoB6yO2u%2FSsr85cPCxvKdaE%2Frlciw0xhYnW0iVmLG5C%2Fsm8u6%2FIXPyecqDx27nTrQr3%2BKY8%2FC07i2dC8Pn1vNPnTzPBDS5hS2%2BY2OexDE3o27b51L7I5yV9q8JCfkCPFzlnX&X-Amz-Signature=586cc7b342c5771470e1677605a8cf1ddc9ee5840fd838136781c28bfc181646&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y33SZN3Q%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgTANtZaL9mnvWRotdUJfq5ZUTcOaAShRcinsIWxSBEgIgVJ6hSFH0Vx1BcTUa6k0aTguVf7eQzz3y1lUe%2Fcnal6YqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKzRQitX%2FCNJxdeeAyrcA81skLpqFdfEyJT%2BJzqVSk6%2BAnXPg97hcyytOzUnLQqI1k5nNDaBdOEhJNhT02is9tzJSH0WG%2FXlCXOJrb8HAUwIWXKpadj9jTe1aS8iMpuDRN1XA2IV%2BblRfnGWWAV1xnZsm0JFmFJWoQuWKkWNm%2Bj6OC4kmIzfpojJK70Ib0WoldHTMpiYO8CJ8RFA0uxjW55lRcHakzT%2BM7kgoKAhhSQN%2FNCdjpfXXwZnDfZkIScYq0sILEgZdlBbk7ci4uZMjHyrZynaASaCtUpU0LtUfoRWfGKg6E1q8zVmwVzm1r0STuQChTn6I0NYt4tZ9uhtnQgiPeo%2Fm2SNwyPH2qW8d9%2B7CR2DG7N5q0MZjK6MGng%2BCppKBvEhFOXI6z8iNePIDXBq9CYjOrHs4A5i0i%2FgB3I4eBwBepOGtBSpjnXOfwJqszoB0LJ0zzBAVO9qe%2FPQqsv%2F7Vn36jfkxsaJRR4orkz4zdWHFPjCwwOW7O4ZNQGUkch5GnXR0y5bsY54GFN%2BJKbXfdn2OenUj0OXnjQdViAckaPfbM%2FtCCVon11Z7BSlAJpyVTPT4y8zln1Mj683mj8dYiEVd8GEZ7E80%2F1oijwbeKI%2F2wu%2FJL8o6CkPePCzxTXetDkAo23dOqRjMIWY7rwGOqUBbf%2BVrXap3v38YnBJlm9%2Bmmg7qQDyq2t9w3GKH9K1wjrGkBBH8yZ8lpF9ENb1S4ZVefHeKKIZeAIDEd%2FwQGvkQpCXKoB6yO2u%2FSsr85cPCxvKdaE%2Frlciw0xhYnW0iVmLG5C%2Fsm8u6%2FIXPyecqDx27nTrQr3%2BKY8%2FC07i2dC8Pn1vNPnTzPBDS5hS2%2BY2OexDE3o27b51L7I5yV9q8JCfkCPFzlnX&X-Amz-Signature=0048c96b55b4992625dab581db01acaecb68632c776fa2767c803ac3fc82b7fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMUSQ2L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCERVlptqIDht0noZU3fKekqYP1ChQ1a0nWWy2a4FosHgIhAIiSnEl9GUzSEhIY%2Fw1QiVCyV259tM7Ay1iGpWDePZvIKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzL1szVVwP%2B8jIjHQq3APVF4Lv%2BFGmwxlDdtnAk9r3ECt3Pyei7XHXYCKo5v%2Ffa7nBLNmdNtpvwjOGqZTnr2pdYecv9T9khw7tL8V34shI7c2Kffm6ycv3nHv%2BluPFFc4IzczXrLtKduEN%2Fqqb2K1Oi%2FnO8KWWoD%2BThX5ayKOa8MZV8TDlUdKi7vSyle3zo2iQ4mUFJyczI%2FFspddQl4qMXMHGn2yYbRkaviGuTWbvjp41Slt1b0gi0eHMDRPYUOW8rzr4Iz6vwUdN5KJ%2BJzkHmHhNYOcKP0Rg7WPy%2FlacPawa8OetlvERoLl756qnIVUnSNBn4Ri7OoX%2FFVCV%2B79HAbJm9zJuWMF3wL8r97jsFhgSWOe%2Be%2BJD7vohfGHVkcW2%2B5qx7xQB3yz1WWP7tPBeBmiyLj4YZKK3z78k3sBwF1nH%2FqmQhpu6nC5lBzoMStUfu3VeSxfhyA68zxPZbEs0kyCKUOekaQUc%2Bu8gJS6klvXa2R5%2BKGhGqbXykpHu1O5TgjI10ZifvFT6e7XmJGzgLOaGwF6yKxf6pjMMGU9hoZiRpSL8ZmlSdRi1%2BVCwNfXCOEhq%2FT9V6kJdBW6w%2FR8WpxuQzelm4gPCpGWaw6LzKPFaDYeDlB4EtE9HkztciX%2BwNqjTUHIKhPf2SzCel%2B68BjqkAXrzVtoK%2BkmxoTERuI3EZygLNI%2FNoqomC%2F99xtPeFQcP02eLpQi62GKk4vo6%2ByRT7w3BrGjYdj1XVTX%2Bn5fI3QlSTAzrkacSKIs8XvbdsMIiykUDAD%2BPvlThqUbMC6QmhzeQXKjsp0DPl7KjR51K54AtOlOkRbwzQUoeXV3nIEbwIG30MbPFU13WTrzNikqM%2B3hmpXPgZsZKDmUktXvFNwnej88Y&X-Amz-Signature=48ffb3e82f056822b9f85ca3335ea2f030bf312b085d595344b23101acca9066&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMUSQ2L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCERVlptqIDht0noZU3fKekqYP1ChQ1a0nWWy2a4FosHgIhAIiSnEl9GUzSEhIY%2Fw1QiVCyV259tM7Ay1iGpWDePZvIKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzL1szVVwP%2B8jIjHQq3APVF4Lv%2BFGmwxlDdtnAk9r3ECt3Pyei7XHXYCKo5v%2Ffa7nBLNmdNtpvwjOGqZTnr2pdYecv9T9khw7tL8V34shI7c2Kffm6ycv3nHv%2BluPFFc4IzczXrLtKduEN%2Fqqb2K1Oi%2FnO8KWWoD%2BThX5ayKOa8MZV8TDlUdKi7vSyle3zo2iQ4mUFJyczI%2FFspddQl4qMXMHGn2yYbRkaviGuTWbvjp41Slt1b0gi0eHMDRPYUOW8rzr4Iz6vwUdN5KJ%2BJzkHmHhNYOcKP0Rg7WPy%2FlacPawa8OetlvERoLl756qnIVUnSNBn4Ri7OoX%2FFVCV%2B79HAbJm9zJuWMF3wL8r97jsFhgSWOe%2Be%2BJD7vohfGHVkcW2%2B5qx7xQB3yz1WWP7tPBeBmiyLj4YZKK3z78k3sBwF1nH%2FqmQhpu6nC5lBzoMStUfu3VeSxfhyA68zxPZbEs0kyCKUOekaQUc%2Bu8gJS6klvXa2R5%2BKGhGqbXykpHu1O5TgjI10ZifvFT6e7XmJGzgLOaGwF6yKxf6pjMMGU9hoZiRpSL8ZmlSdRi1%2BVCwNfXCOEhq%2FT9V6kJdBW6w%2FR8WpxuQzelm4gPCpGWaw6LzKPFaDYeDlB4EtE9HkztciX%2BwNqjTUHIKhPf2SzCel%2B68BjqkAXrzVtoK%2BkmxoTERuI3EZygLNI%2FNoqomC%2F99xtPeFQcP02eLpQi62GKk4vo6%2ByRT7w3BrGjYdj1XVTX%2Bn5fI3QlSTAzrkacSKIs8XvbdsMIiykUDAD%2BPvlThqUbMC6QmhzeQXKjsp0DPl7KjR51K54AtOlOkRbwzQUoeXV3nIEbwIG30MbPFU13WTrzNikqM%2B3hmpXPgZsZKDmUktXvFNwnej88Y&X-Amz-Signature=988673347ffea174889330859582f1255abc3b1d882552794147d64bc0da2989&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMUSQ2L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCERVlptqIDht0noZU3fKekqYP1ChQ1a0nWWy2a4FosHgIhAIiSnEl9GUzSEhIY%2Fw1QiVCyV259tM7Ay1iGpWDePZvIKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzL1szVVwP%2B8jIjHQq3APVF4Lv%2BFGmwxlDdtnAk9r3ECt3Pyei7XHXYCKo5v%2Ffa7nBLNmdNtpvwjOGqZTnr2pdYecv9T9khw7tL8V34shI7c2Kffm6ycv3nHv%2BluPFFc4IzczXrLtKduEN%2Fqqb2K1Oi%2FnO8KWWoD%2BThX5ayKOa8MZV8TDlUdKi7vSyle3zo2iQ4mUFJyczI%2FFspddQl4qMXMHGn2yYbRkaviGuTWbvjp41Slt1b0gi0eHMDRPYUOW8rzr4Iz6vwUdN5KJ%2BJzkHmHhNYOcKP0Rg7WPy%2FlacPawa8OetlvERoLl756qnIVUnSNBn4Ri7OoX%2FFVCV%2B79HAbJm9zJuWMF3wL8r97jsFhgSWOe%2Be%2BJD7vohfGHVkcW2%2B5qx7xQB3yz1WWP7tPBeBmiyLj4YZKK3z78k3sBwF1nH%2FqmQhpu6nC5lBzoMStUfu3VeSxfhyA68zxPZbEs0kyCKUOekaQUc%2Bu8gJS6klvXa2R5%2BKGhGqbXykpHu1O5TgjI10ZifvFT6e7XmJGzgLOaGwF6yKxf6pjMMGU9hoZiRpSL8ZmlSdRi1%2BVCwNfXCOEhq%2FT9V6kJdBW6w%2FR8WpxuQzelm4gPCpGWaw6LzKPFaDYeDlB4EtE9HkztciX%2BwNqjTUHIKhPf2SzCel%2B68BjqkAXrzVtoK%2BkmxoTERuI3EZygLNI%2FNoqomC%2F99xtPeFQcP02eLpQi62GKk4vo6%2ByRT7w3BrGjYdj1XVTX%2Bn5fI3QlSTAzrkacSKIs8XvbdsMIiykUDAD%2BPvlThqUbMC6QmhzeQXKjsp0DPl7KjR51K54AtOlOkRbwzQUoeXV3nIEbwIG30MbPFU13WTrzNikqM%2B3hmpXPgZsZKDmUktXvFNwnej88Y&X-Amz-Signature=aa4105c236500548fc10e35b28781ba7cb118b170f48739929d10cf01cefd985&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMUSQ2L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCERVlptqIDht0noZU3fKekqYP1ChQ1a0nWWy2a4FosHgIhAIiSnEl9GUzSEhIY%2Fw1QiVCyV259tM7Ay1iGpWDePZvIKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzL1szVVwP%2B8jIjHQq3APVF4Lv%2BFGmwxlDdtnAk9r3ECt3Pyei7XHXYCKo5v%2Ffa7nBLNmdNtpvwjOGqZTnr2pdYecv9T9khw7tL8V34shI7c2Kffm6ycv3nHv%2BluPFFc4IzczXrLtKduEN%2Fqqb2K1Oi%2FnO8KWWoD%2BThX5ayKOa8MZV8TDlUdKi7vSyle3zo2iQ4mUFJyczI%2FFspddQl4qMXMHGn2yYbRkaviGuTWbvjp41Slt1b0gi0eHMDRPYUOW8rzr4Iz6vwUdN5KJ%2BJzkHmHhNYOcKP0Rg7WPy%2FlacPawa8OetlvERoLl756qnIVUnSNBn4Ri7OoX%2FFVCV%2B79HAbJm9zJuWMF3wL8r97jsFhgSWOe%2Be%2BJD7vohfGHVkcW2%2B5qx7xQB3yz1WWP7tPBeBmiyLj4YZKK3z78k3sBwF1nH%2FqmQhpu6nC5lBzoMStUfu3VeSxfhyA68zxPZbEs0kyCKUOekaQUc%2Bu8gJS6klvXa2R5%2BKGhGqbXykpHu1O5TgjI10ZifvFT6e7XmJGzgLOaGwF6yKxf6pjMMGU9hoZiRpSL8ZmlSdRi1%2BVCwNfXCOEhq%2FT9V6kJdBW6w%2FR8WpxuQzelm4gPCpGWaw6LzKPFaDYeDlB4EtE9HkztciX%2BwNqjTUHIKhPf2SzCel%2B68BjqkAXrzVtoK%2BkmxoTERuI3EZygLNI%2FNoqomC%2F99xtPeFQcP02eLpQi62GKk4vo6%2ByRT7w3BrGjYdj1XVTX%2Bn5fI3QlSTAzrkacSKIs8XvbdsMIiykUDAD%2BPvlThqUbMC6QmhzeQXKjsp0DPl7KjR51K54AtOlOkRbwzQUoeXV3nIEbwIG30MbPFU13WTrzNikqM%2B3hmpXPgZsZKDmUktXvFNwnej88Y&X-Amz-Signature=85e2574ac3d7cb32426d9deb736e90a97c4149cbfb55023d52c97958ad8e7ea2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMUSQ2L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCERVlptqIDht0noZU3fKekqYP1ChQ1a0nWWy2a4FosHgIhAIiSnEl9GUzSEhIY%2Fw1QiVCyV259tM7Ay1iGpWDePZvIKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzL1szVVwP%2B8jIjHQq3APVF4Lv%2BFGmwxlDdtnAk9r3ECt3Pyei7XHXYCKo5v%2Ffa7nBLNmdNtpvwjOGqZTnr2pdYecv9T9khw7tL8V34shI7c2Kffm6ycv3nHv%2BluPFFc4IzczXrLtKduEN%2Fqqb2K1Oi%2FnO8KWWoD%2BThX5ayKOa8MZV8TDlUdKi7vSyle3zo2iQ4mUFJyczI%2FFspddQl4qMXMHGn2yYbRkaviGuTWbvjp41Slt1b0gi0eHMDRPYUOW8rzr4Iz6vwUdN5KJ%2BJzkHmHhNYOcKP0Rg7WPy%2FlacPawa8OetlvERoLl756qnIVUnSNBn4Ri7OoX%2FFVCV%2B79HAbJm9zJuWMF3wL8r97jsFhgSWOe%2Be%2BJD7vohfGHVkcW2%2B5qx7xQB3yz1WWP7tPBeBmiyLj4YZKK3z78k3sBwF1nH%2FqmQhpu6nC5lBzoMStUfu3VeSxfhyA68zxPZbEs0kyCKUOekaQUc%2Bu8gJS6klvXa2R5%2BKGhGqbXykpHu1O5TgjI10ZifvFT6e7XmJGzgLOaGwF6yKxf6pjMMGU9hoZiRpSL8ZmlSdRi1%2BVCwNfXCOEhq%2FT9V6kJdBW6w%2FR8WpxuQzelm4gPCpGWaw6LzKPFaDYeDlB4EtE9HkztciX%2BwNqjTUHIKhPf2SzCel%2B68BjqkAXrzVtoK%2BkmxoTERuI3EZygLNI%2FNoqomC%2F99xtPeFQcP02eLpQi62GKk4vo6%2ByRT7w3BrGjYdj1XVTX%2Bn5fI3QlSTAzrkacSKIs8XvbdsMIiykUDAD%2BPvlThqUbMC6QmhzeQXKjsp0DPl7KjR51K54AtOlOkRbwzQUoeXV3nIEbwIG30MbPFU13WTrzNikqM%2B3hmpXPgZsZKDmUktXvFNwnej88Y&X-Amz-Signature=2c033ee8d78d350495e1add75a6ba999db8836a058883b674e0b31f1129c166d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMUSQ2L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCERVlptqIDht0noZU3fKekqYP1ChQ1a0nWWy2a4FosHgIhAIiSnEl9GUzSEhIY%2Fw1QiVCyV259tM7Ay1iGpWDePZvIKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzL1szVVwP%2B8jIjHQq3APVF4Lv%2BFGmwxlDdtnAk9r3ECt3Pyei7XHXYCKo5v%2Ffa7nBLNmdNtpvwjOGqZTnr2pdYecv9T9khw7tL8V34shI7c2Kffm6ycv3nHv%2BluPFFc4IzczXrLtKduEN%2Fqqb2K1Oi%2FnO8KWWoD%2BThX5ayKOa8MZV8TDlUdKi7vSyle3zo2iQ4mUFJyczI%2FFspddQl4qMXMHGn2yYbRkaviGuTWbvjp41Slt1b0gi0eHMDRPYUOW8rzr4Iz6vwUdN5KJ%2BJzkHmHhNYOcKP0Rg7WPy%2FlacPawa8OetlvERoLl756qnIVUnSNBn4Ri7OoX%2FFVCV%2B79HAbJm9zJuWMF3wL8r97jsFhgSWOe%2Be%2BJD7vohfGHVkcW2%2B5qx7xQB3yz1WWP7tPBeBmiyLj4YZKK3z78k3sBwF1nH%2FqmQhpu6nC5lBzoMStUfu3VeSxfhyA68zxPZbEs0kyCKUOekaQUc%2Bu8gJS6klvXa2R5%2BKGhGqbXykpHu1O5TgjI10ZifvFT6e7XmJGzgLOaGwF6yKxf6pjMMGU9hoZiRpSL8ZmlSdRi1%2BVCwNfXCOEhq%2FT9V6kJdBW6w%2FR8WpxuQzelm4gPCpGWaw6LzKPFaDYeDlB4EtE9HkztciX%2BwNqjTUHIKhPf2SzCel%2B68BjqkAXrzVtoK%2BkmxoTERuI3EZygLNI%2FNoqomC%2F99xtPeFQcP02eLpQi62GKk4vo6%2ByRT7w3BrGjYdj1XVTX%2Bn5fI3QlSTAzrkacSKIs8XvbdsMIiykUDAD%2BPvlThqUbMC6QmhzeQXKjsp0DPl7KjR51K54AtOlOkRbwzQUoeXV3nIEbwIG30MbPFU13WTrzNikqM%2B3hmpXPgZsZKDmUktXvFNwnej88Y&X-Amz-Signature=c61edf01be1cd617b15982d04e7eee111c9687c28033d768b2c026842c0a5876&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A7N7IFO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCh5YarRzbxPIp62LfIpph%2BMx3ujCiYY2e6ip5HnILr3QIhAOk5AQqiyd%2FaStJ1Skk5%2BjxA72ZlBlVLVtwwAj7pujmFKogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxzMBWvRnrJ4Gl3Szwq3ANqziYYBe9VH%2BV8O8lMHl%2FsFo%2FXsrolr1hnMxMK3T7NuV4vtoPYWYf40VjDdbDC5yKnAgkpWVWc19We7ZlQXNQ9XVQg%2Bi2Kvzo5w%2F7VOvR7XI70sgHvymLFKpcYrTpzJPrj9IGOjJ2crciSW9zI8hI1eaDrxGt1Fqn%2FdNBglGeF2dYgLRXigYUHJ5m2IOkxxydawrQOIIoQFZV8RAwy1enZQkD%2Blz1M3pYdXNLmWBSgOEBPmp0UNGjY7Zd5kPiUNRpUTFSKThPLyoVWP9aiMgkNYwTfnqEnFpf7nGSlevWRW2mMUHBAbH4Lw7GDp4yQpWXSLNcB%2FiH7sKUDsntY7XkboEJSQsAOfR54zBW%2F6C3Gn5MbUS6swajAu4WMYbOwD%2BXOK7cfmYEoBbOmus4Cy7EInj3QHJm4qp2IGn4QDMhFDlXeX3AOmnldsU%2B9tvubi14X3pqzLGczJzPyXd4mtDq88qvuSSh63LEte5foCYGDjm6C9k2HGR0rUm4rqYCVjhvctywavwLBHo4WtyfdABvn2sVw7tCq0fCfMzfGS3BAMTfukcYPqkC8a1qkUyA3ghyYvL9u8p7e9BipdAoUUulslg4oj%2Bjo%2Bl8g%2F8%2F38KRGjuq%2BzCU%2Fhr6d6drzTzCCl%2B68BjqkAUbSX7%2Bo2SYeCHk7ZuYEWwbjPvpt73R31XjyRrc1oOnMJLRQHsmdiEfKP%2FHVPkGqu5QyZRykx4IZqljRDBJE90KoeOn3JaupOHOfg%2F2okDgcPb1a4wtRP6wL8IYqOcsjVBuub9PdRbAJLv0hj7vLUlT5ImXp94eInSHRtd1j6E2pjFh8mAeOyn1jtprZS5ILW51FKXE%2B%2FJBhxkcvppZt8rIfrm2d&X-Amz-Signature=5759b44cf9d1703e8df1532e3a1549007e0f58a9b92e7f5ca6a07b9f40cd35f8&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3LOIP5C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfNB0aZI8VekVIQxQRohmAAP98jmaCo2KVm4pNmlgS2QIgLlp4LUb8yRMm5Iw0MTMZ4%2FpUAQDBMVFUib6jOvtVniYqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ5XI3yYErByd6b1dircA22kw7AJ628TRAB0XaelShNfex3bKoTI6aHCjCCwVHvStDC%2BhqSCC2T5GEumsVBQ1wM%2BAfGBMWgiRCkRXb1SQmVzOAKN0iMAya9hbEYFOvm1gvxNM2BsHp02%2BtfpzSXUzKe7sk1aOLd3zGmVCDpay%2F%2Fs4LNSjhqoA1pvr%2FlHC%2FRn%2FV8hSwqAZOCfzC23A31xfhlN0HG9ta9MfQiXbVyxRSfl7CG5zy01nRIAjAkRK2QArdEIyVZEiE2n3WTdidn5m7JyTuSItkqFZYsUyD1GXdxFj3h0EwS4ySjHkU%2FXuiTZxcEIXLJ7xRZXa1sxtcUmIjb%2Bm4nfhvxvsJk%2FR8DFmwwBgOvN%2BqYcj7kpChRElwknYJcQozqpcXLyTzfHmZ%2ByCgI6rnTCUki6NM1yZI80YFwo5F6NBe5SM%2FO9AlwA6SEfa84tRA0tj5POOA8usDvExAOrY3RwQLVvX4oO5KmTIiU2Sd4e7wrhkPvtZmXHmKZTCxDmBdSm%2BWD56T%2FrFcVU5QgUbXXMmymBxXE7qQmoMvNnr7GShjqrAqq0vGl8OBttH1GpLtrwCsnsJFEpuRSLcV4vBVnsclrbYKBbuINcsVkGo00Kpvq88RNLMYGto3gYGxJth%2BwqL6QXop%2F7MNOY7rwGOqUB9P%2F0mFRult8EW5rAiTbTmquwnpJ1Z3l%2FUcf0lFfbIv7AqV5dhTkxqHEYQXVZ1Jr0KG6IWWHhHTp6FB%2BhzsS5CkBYgzr32ID5IRsnlmMO0sgaVnskCwHr0iFY9TLWE5RDJt2x9RGsqyyCj1cM6%2FkcwI9bTZBPr5suYRrkICABpQyXHsMny2hDRtFmKsDMTL4FtNjoI8dxq1tGClScIYZn2x9frY5t&X-Amz-Signature=088817643b9ba8d2cb0fd8e8c07e8c20b65365f24c4871280319c11bb297cc6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMUSQ2L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCERVlptqIDht0noZU3fKekqYP1ChQ1a0nWWy2a4FosHgIhAIiSnEl9GUzSEhIY%2Fw1QiVCyV259tM7Ay1iGpWDePZvIKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzL1szVVwP%2B8jIjHQq3APVF4Lv%2BFGmwxlDdtnAk9r3ECt3Pyei7XHXYCKo5v%2Ffa7nBLNmdNtpvwjOGqZTnr2pdYecv9T9khw7tL8V34shI7c2Kffm6ycv3nHv%2BluPFFc4IzczXrLtKduEN%2Fqqb2K1Oi%2FnO8KWWoD%2BThX5ayKOa8MZV8TDlUdKi7vSyle3zo2iQ4mUFJyczI%2FFspddQl4qMXMHGn2yYbRkaviGuTWbvjp41Slt1b0gi0eHMDRPYUOW8rzr4Iz6vwUdN5KJ%2BJzkHmHhNYOcKP0Rg7WPy%2FlacPawa8OetlvERoLl756qnIVUnSNBn4Ri7OoX%2FFVCV%2B79HAbJm9zJuWMF3wL8r97jsFhgSWOe%2Be%2BJD7vohfGHVkcW2%2B5qx7xQB3yz1WWP7tPBeBmiyLj4YZKK3z78k3sBwF1nH%2FqmQhpu6nC5lBzoMStUfu3VeSxfhyA68zxPZbEs0kyCKUOekaQUc%2Bu8gJS6klvXa2R5%2BKGhGqbXykpHu1O5TgjI10ZifvFT6e7XmJGzgLOaGwF6yKxf6pjMMGU9hoZiRpSL8ZmlSdRi1%2BVCwNfXCOEhq%2FT9V6kJdBW6w%2FR8WpxuQzelm4gPCpGWaw6LzKPFaDYeDlB4EtE9HkztciX%2BwNqjTUHIKhPf2SzCel%2B68BjqkAXrzVtoK%2BkmxoTERuI3EZygLNI%2FNoqomC%2F99xtPeFQcP02eLpQi62GKk4vo6%2ByRT7w3BrGjYdj1XVTX%2Bn5fI3QlSTAzrkacSKIs8XvbdsMIiykUDAD%2BPvlThqUbMC6QmhzeQXKjsp0DPl7KjR51K54AtOlOkRbwzQUoeXV3nIEbwIG30MbPFU13WTrzNikqM%2B3hmpXPgZsZKDmUktXvFNwnej88Y&X-Amz-Signature=7d02d061ddc5c5849f2a8e4698ea920a071ebc656aa148966e1423a3c9b607a7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMUSQ2L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCERVlptqIDht0noZU3fKekqYP1ChQ1a0nWWy2a4FosHgIhAIiSnEl9GUzSEhIY%2Fw1QiVCyV259tM7Ay1iGpWDePZvIKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzL1szVVwP%2B8jIjHQq3APVF4Lv%2BFGmwxlDdtnAk9r3ECt3Pyei7XHXYCKo5v%2Ffa7nBLNmdNtpvwjOGqZTnr2pdYecv9T9khw7tL8V34shI7c2Kffm6ycv3nHv%2BluPFFc4IzczXrLtKduEN%2Fqqb2K1Oi%2FnO8KWWoD%2BThX5ayKOa8MZV8TDlUdKi7vSyle3zo2iQ4mUFJyczI%2FFspddQl4qMXMHGn2yYbRkaviGuTWbvjp41Slt1b0gi0eHMDRPYUOW8rzr4Iz6vwUdN5KJ%2BJzkHmHhNYOcKP0Rg7WPy%2FlacPawa8OetlvERoLl756qnIVUnSNBn4Ri7OoX%2FFVCV%2B79HAbJm9zJuWMF3wL8r97jsFhgSWOe%2Be%2BJD7vohfGHVkcW2%2B5qx7xQB3yz1WWP7tPBeBmiyLj4YZKK3z78k3sBwF1nH%2FqmQhpu6nC5lBzoMStUfu3VeSxfhyA68zxPZbEs0kyCKUOekaQUc%2Bu8gJS6klvXa2R5%2BKGhGqbXykpHu1O5TgjI10ZifvFT6e7XmJGzgLOaGwF6yKxf6pjMMGU9hoZiRpSL8ZmlSdRi1%2BVCwNfXCOEhq%2FT9V6kJdBW6w%2FR8WpxuQzelm4gPCpGWaw6LzKPFaDYeDlB4EtE9HkztciX%2BwNqjTUHIKhPf2SzCel%2B68BjqkAXrzVtoK%2BkmxoTERuI3EZygLNI%2FNoqomC%2F99xtPeFQcP02eLpQi62GKk4vo6%2ByRT7w3BrGjYdj1XVTX%2Bn5fI3QlSTAzrkacSKIs8XvbdsMIiykUDAD%2BPvlThqUbMC6QmhzeQXKjsp0DPl7KjR51K54AtOlOkRbwzQUoeXV3nIEbwIG30MbPFU13WTrzNikqM%2B3hmpXPgZsZKDmUktXvFNwnej88Y&X-Amz-Signature=565853a23323ee96e47cefad602347c7b12fd466b6bba49a0290a6d8faa65299&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMUSQ2L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCERVlptqIDht0noZU3fKekqYP1ChQ1a0nWWy2a4FosHgIhAIiSnEl9GUzSEhIY%2Fw1QiVCyV259tM7Ay1iGpWDePZvIKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzL1szVVwP%2B8jIjHQq3APVF4Lv%2BFGmwxlDdtnAk9r3ECt3Pyei7XHXYCKo5v%2Ffa7nBLNmdNtpvwjOGqZTnr2pdYecv9T9khw7tL8V34shI7c2Kffm6ycv3nHv%2BluPFFc4IzczXrLtKduEN%2Fqqb2K1Oi%2FnO8KWWoD%2BThX5ayKOa8MZV8TDlUdKi7vSyle3zo2iQ4mUFJyczI%2FFspddQl4qMXMHGn2yYbRkaviGuTWbvjp41Slt1b0gi0eHMDRPYUOW8rzr4Iz6vwUdN5KJ%2BJzkHmHhNYOcKP0Rg7WPy%2FlacPawa8OetlvERoLl756qnIVUnSNBn4Ri7OoX%2FFVCV%2B79HAbJm9zJuWMF3wL8r97jsFhgSWOe%2Be%2BJD7vohfGHVkcW2%2B5qx7xQB3yz1WWP7tPBeBmiyLj4YZKK3z78k3sBwF1nH%2FqmQhpu6nC5lBzoMStUfu3VeSxfhyA68zxPZbEs0kyCKUOekaQUc%2Bu8gJS6klvXa2R5%2BKGhGqbXykpHu1O5TgjI10ZifvFT6e7XmJGzgLOaGwF6yKxf6pjMMGU9hoZiRpSL8ZmlSdRi1%2BVCwNfXCOEhq%2FT9V6kJdBW6w%2FR8WpxuQzelm4gPCpGWaw6LzKPFaDYeDlB4EtE9HkztciX%2BwNqjTUHIKhPf2SzCel%2B68BjqkAXrzVtoK%2BkmxoTERuI3EZygLNI%2FNoqomC%2F99xtPeFQcP02eLpQi62GKk4vo6%2ByRT7w3BrGjYdj1XVTX%2Bn5fI3QlSTAzrkacSKIs8XvbdsMIiykUDAD%2BPvlThqUbMC6QmhzeQXKjsp0DPl7KjR51K54AtOlOkRbwzQUoeXV3nIEbwIG30MbPFU13WTrzNikqM%2B3hmpXPgZsZKDmUktXvFNwnej88Y&X-Amz-Signature=e3b67ca4e8b05fec87ca900170bdad06fdf1d33a1e329b81dbac91bffaaf1793&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJIMQJGN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhSyabRixo5nXf11bD7GlKKV%2BdfhNphmBCmF9mJJv9JQIgO54HO4gDismAlhW8Dqcs9PFctlA15tJHCjyW7E8SUssqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBjTnaz2QQqCuZhJhyrcA8RjmONfISbwCIPx9eUXz4GdAavOXhXsffACCbTIqxIFqGm6C97d8BYJDv8EeM3anRStIoaYElln%2BS7Fh56ObN3LZr%2BqEaoXTXbX14BdYLBCfCZ%2Bm35%2B%2BgpJ%2Bv%2FStpe8Sxaz%2BDh3fwLENt2L5mbe6kPn%2BsoJ8ciYm4frpR2H05WkWcuj0Xq%2BOvnvhiOJ8mR6CJK%2B4OH1hZlgt7dfzFfE3I9I1y4xdRpbWQHqOO1Ud%2FKSHsiDomLmogFjnYNjQ2ZofBVb7dRAiLyMkPAXpmdImKuhEJ3G4GvZCNprO8MQZyUhc3%2FON9o7HzNO9%2BIsH5%2FtvJSJoAHQyVhwQwgR6VkboWeYKs62wjQ5PlPaHATnY3frM8FyYIcQ6VVaWe6IaGifVMxXwA1k83S8cFeqfhkHBxJmUaI8szvawayrOGDHeIqIsMrEqSCnC%2FZY7r%2BYcO%2B2tZghfE8rhrg%2FCuho2%2Ba1oXQw1rseBHpgUQcRNCfMcN0efTGEn8s09RK1m2vPH0z9NpUXF6WXpdb5k0ZMK9EcPnKpU8YkUDPPajHblMKPgAR0%2B4kSfBpR%2BQzqqsn2ZUNEo5k0UTL5CZQHYO2UL1QTP%2FoorkoDBFoMVCjDBsNkm6nJhK7cyzzZG0fhmirDMMeX7rwGOqUBtcNDK7UWp%2FM%2By9TNYA3YXvztJCYwZJ3E7G6T5MsHl9lyJVC9Cb7ftIJ07LRgPBJGvjSzwkoKn08TjDMBVqDAWPrzE7YrdRxWCDDqniVsYXknzz4Ypo%2FqJOB7cnRqfUjMq3m4iNUtf1XjSZ0GeiwzasUVCCOYkIfeO6Bzb67xLSyoc3nvqEyNHeX7d0GvAtGE5S8kgvw8lh75i0FyEw5cSUVyx%2BtF&X-Amz-Signature=ac3a2bed14a37bebdebb896750eddb7003fc0425a340a09a65d73b354772397f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDR34AZY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsj7i9Lfe9snG5QpXA9zGxB7cNPJDkHAIIQXKD%2FUP3lgIgOiP3vQA1zSor3dACaVCIiSN9lp0ynG8MCJf%2F1Vt4LdoqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcuSxC4g7cBvdcneyrcAza6hbHdCzUHHmzQqGqxjMm8CZiOpLQZiRtNEsng20epLA8Y1%2FdEe%2FK8onCVXVMxMhH2Af2hX90ov7PtvPQ9d18wtTB06VNQZpuzQeSMny3AppEJonShj57nEXS0d9A74e2%2FbqY%2B9Myz2c%2FXiLdj7UdMtY3%2BCdFbp9WVdTqiB6Igq6vRxHxbNkxp%2BX52v2Byhk1fAWq96fcacG9EshFFybzCD384zWLqUfYmoOY8YTEk%2BYk637SNbc%2FlZyYjxaYiogoIQKA%2FSwWCm2OvXJCsSlARqax19rUiS0wJ3N%2FG8uHHyeIX2%2Fx4GIvEl0E9RS8MMDz0ltU%2BNeeJuksbSlG27jZ1OqzGcZWOmGESpp7Qm1%2BY3DCd9G8zJ9ZQx2EPH2h6wseaF81xxLqV86pwiCFkb1BMCj6e4GJlGbLG2srlMNs74pRC9jQH%2FwwgpvPoU%2Fu%2FT6kc6jm9rxFLmLVIuew4C2gpUj5P06lwnvbome13rZ7OcL729nFSir0cCr8TE7s%2FS6TrF4C0fSzsDYp8Mrdmy%2Fwz5oe7cvfk9Thqmxl40biXEHnka%2BXhqfjrLEVyzXfvcCFadkalJVFem4C2YIMpTBmS2sEEzeC7o4lJOiZrKvz79dGzRT%2BNJGgzQ1AwMIKY7rwGOqUBeZlJ3QQHM4x1kj47qLP1YjYVmLP%2BXy7AnfzhENOY5WgXcdeFk03agMI356x%2FYO2rwr7925i7dkSXWnW1VYeI6KwP8Hf4qvzrHODfFbb3%2B3LpDfhCzbX84CL7qfHL3b0sRlw0%2FOu0qO4QpynZjNX4dmLvfSdZpBq1Cmn%2F2qQarA1%2Ftgq2nBlqgt7SYkbaYkdL6U0KsMqozj6hNFm%2BPUq5H30JYcxu&X-Amz-Signature=e816a6e203d21ee55de3c84b760fd26954fcd0d0b3b43dbd5d92af9ad19df62a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QVT2V3F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICykFWjrPUI9RlEv9twwAwKuMsbclqGX1WANxPw5amPMAiAnINQs8SNlqJCHgVEOI%2FhKSr1bvBZWDDkVzphoINkGBCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMym0Bl0pVNHnXrKUtKtwDNxXCnGKJSb4gSoCNRhbxbmKKLksrYpKXAljMsaGQxs8Luo3tnfWAQq7MrYubmrgZ8APIPeCHcT%2BNRvqkE0cfDx8kDtS3nXziHaZE6CxLBha37srqwlAwpq7ArTYQal%2BreHvAA%2BJqV07FZpNwT21rnVOygp96yhHGqFJ3iuzlMjeHZpjm6GTQO88Pud6SljO4mojZsbc8J%2F3zURD1Wr8xzl80IjKnI6cYMgwcq4mOEIfQYwrhtSTfP8FFU7qncD3D%2Byye%2BRbiexoNnyvWjdOmV0Edsrfwp9Haubc43%2F1OIDkzV4x4hJMc46CLxOhKc%2FatwAF%2BzRF2kxes%2B8k%2B67fHM6LAKXjiuRX%2Ba%2BtsVrUUjtc6QW89LKuTuwA%2BdJmNFFdNKnaKpZq7YTP41u5Qmb%2BAY1N8upNQ8I%2BU5Xou7M3U4jYEjBN%2BGYZqUe5ohxXVUjG0FWGv1U8qX8kwu9UA8jvthTSYwz01od2fuhv6LlWLvP9fncireJlv%2B01DUlO95aJk0ptBER0Xy0Hc4n9eNEDloYH4WvAKorhmRuktfAU1K2PkGmaNOPqW%2FSjiWKZHgD4KYmzix4I2XiSsIdYVTmZlFmAxxiMMRdETnr03NDRdxhG3fdjuyqExGCXjgV0wwJjuvAY6pgFIPRLgrDhT8REkMXHQOzhrNq7nBmqIi1umYz35u4%2FirQEBvBLo7usI2iq586ZXWldoZZCd7cHWP29Gr%2BloVUeLw6fQArlMJqJ9nFwQCDyjs%2Bsp4Mpgvfp1%2BRuflfr%2B0QJbnun95Y3zNmVFb4EbC%2FPhxeteVQ4YrBt%2BQUdEKdDyrhok%2BCVVlIX%2FYEXDoMcNR%2FoU%2FSypT1EUbMt5u0aly7uWu8UmgYaD&X-Amz-Signature=71259b67c097d38481bf44be70d556b077f87313b995ac6e6f19883a61308e1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTFCDCQQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBctdBUd%2FqfYnrM0TlcIv0oer9Pc14N1iem1MJ6G%2BzYWAiEA%2FU9%2BrZrm2i20d9%2BSDjFrorSUHJBGE0j5kwmwRHrX3TIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMBXIxBtP%2FHDxwNqACrcA5XUeChg2rGYmK3dksUghkV3k45Q8JWj5JehS4ioKFEdQuWnwTPeqWkqzA9W5GlIPS6OwmQG6gMaOrUq2TJlAjMKN6w72sLuhnd5iC99Nbt7EZ4EcDSvZ8U76EREu0qPAqm%2BcYOU7NAS%2BTD3f3RzDuWfOwzDole28%2FrsnkNiTmxH1S0XQGYufUpzbHPoyFhBMSZtIJSsQG8wrGgZ1ooJYnLANRdyI1JvX3cbKTjlZpHtjXFeE8w163EUTNCl3L3IbRf3Vv0shVrWRIPZM24ZWwQifES4Q0ZVBXxl%2B%2FYdcIIMy5m6UFMbLzbEPwoH%2FUiuhl5SPfCnywlZdbpVShmUtIa3YPImqeA%2B8P1WXqZ4uTjUfsN%2BxMJ9LpF862VGUzLfkYCHt5ee8H8YtslStPFp8ysToC0TcFkiytD5PRzdLJ1q6lBsZviGFBSiQnlAn1zbTCCmyBQ%2F9baUKiinxL9brdiFTPDTJ1kgkfo9Ocg%2BmS63gp0Vli3Iac4BJFvDDqUm60WYUEbGmsZ3fDlA7K2Q1hFREbddcgV0bJD9flja0qU0H5lcWNmMkJt3Sf0sPDxbn9qm38wbynv5iEVKXiVew7dKSqhwX9%2BkA4vfOCPsSEruS%2B757RM6ASWjg2O5MMmX7rwGOqUBC9TfJhdd3aD8didxfyDwbNRceEkAH3JOqNtlwOZROtwW%2FMMDbx7CHS25jw6OtahchRDtV9GfU1ZtWokhuBQdqg8b5l7lwve1tEl8DABk20ViID54WSUP3QON0hXn6Vw9%2BeUzWBdhN61KyJInjOOfiylTwFlqvAnDbzNzs6%2BoPP3Di%2FZ21Ls%2FG1PKjWjmFAYmOeVLUnkmVMvKu79Okb51Wn4p5vQr&X-Amz-Signature=68b8bbe1501fc0b3eed9629b9b214d2a5485678bd7e1a7f1002b1837bf91380d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTFCDCQQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBctdBUd%2FqfYnrM0TlcIv0oer9Pc14N1iem1MJ6G%2BzYWAiEA%2FU9%2BrZrm2i20d9%2BSDjFrorSUHJBGE0j5kwmwRHrX3TIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMBXIxBtP%2FHDxwNqACrcA5XUeChg2rGYmK3dksUghkV3k45Q8JWj5JehS4ioKFEdQuWnwTPeqWkqzA9W5GlIPS6OwmQG6gMaOrUq2TJlAjMKN6w72sLuhnd5iC99Nbt7EZ4EcDSvZ8U76EREu0qPAqm%2BcYOU7NAS%2BTD3f3RzDuWfOwzDole28%2FrsnkNiTmxH1S0XQGYufUpzbHPoyFhBMSZtIJSsQG8wrGgZ1ooJYnLANRdyI1JvX3cbKTjlZpHtjXFeE8w163EUTNCl3L3IbRf3Vv0shVrWRIPZM24ZWwQifES4Q0ZVBXxl%2B%2FYdcIIMy5m6UFMbLzbEPwoH%2FUiuhl5SPfCnywlZdbpVShmUtIa3YPImqeA%2B8P1WXqZ4uTjUfsN%2BxMJ9LpF862VGUzLfkYCHt5ee8H8YtslStPFp8ysToC0TcFkiytD5PRzdLJ1q6lBsZviGFBSiQnlAn1zbTCCmyBQ%2F9baUKiinxL9brdiFTPDTJ1kgkfo9Ocg%2BmS63gp0Vli3Iac4BJFvDDqUm60WYUEbGmsZ3fDlA7K2Q1hFREbddcgV0bJD9flja0qU0H5lcWNmMkJt3Sf0sPDxbn9qm38wbynv5iEVKXiVew7dKSqhwX9%2BkA4vfOCPsSEruS%2B757RM6ASWjg2O5MMmX7rwGOqUBC9TfJhdd3aD8didxfyDwbNRceEkAH3JOqNtlwOZROtwW%2FMMDbx7CHS25jw6OtahchRDtV9GfU1ZtWokhuBQdqg8b5l7lwve1tEl8DABk20ViID54WSUP3QON0hXn6Vw9%2BeUzWBdhN61KyJInjOOfiylTwFlqvAnDbzNzs6%2BoPP3Di%2FZ21Ls%2FG1PKjWjmFAYmOeVLUnkmVMvKu79Okb51Wn4p5vQr&X-Amz-Signature=cdc116beb7ada1638f8ece4376fc71145d3e3010475844e543d7a20b6095e12b&X-Amz-SignedHeaders=host&x-id=GetObject)

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
