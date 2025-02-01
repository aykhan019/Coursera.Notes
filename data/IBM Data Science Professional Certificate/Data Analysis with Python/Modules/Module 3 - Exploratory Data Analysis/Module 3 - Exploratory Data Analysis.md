

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWJTQCU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHMrYmgBl9kCUOqfAd%2BAL%2Fheo5ZCvNHGvm5r%2FJX86OiQIhAI7kwkcNBWryC1kpyAj8dymAXQSij%2B3tGyWRpNKQmlEFKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzpNkztjMNZ%2B8h4kmQq3APcwfbIQ4FeF%2FTg96P89XnDPCDu%2BAZ4iRgcX6rI7KdIDHlPFEqsly0Eb%2BHtLDPBKcyMc05YsFAEzrT888N5ORWJ2tnN2SXn%2Ba8tte4998ALaiYt9Khq3I72r8uzgyxQWfvcix9gxQGN1DGieZDZXPBjAaKe63mBuIYI50Ja6C6QCiGa%2BXx0H4YCCPARyioiWzun01MEEj%2B6%2Bap9ZbfxirFR52Q0WTX8h3O0Ln%2B%2FwlJxdp1kzmVYrQTK5hQHJqRsfQlil7qfIdCPCuSRmJ2GJfULURmxc7BnqEEmOkx%2BBowoOExHdJqt6vJ6HBBd6e%2FGXUy2vXtBb1jxhddP3oOIcQL%2FpLhpDEvBG7rbEcYNyKNPtlZUy8HJJLRRLjVkZQ2IL1Vh9VtEZnNZ1PJdvkcrqJfd38dLUF%2FLjxxdd9T6aa8rqhBWLu2MRa3HzhZUi4UixcGK%2B71ro%2BVY7j60M8Ot6ovUeEsD1blbBtxqejCoDqPIlawcgGdf%2BuN8dm%2BNHAGo2eQethqY5ur4spHaaZ4BSQqBDqoVudZvQaa7ad9MYB6tVBT7r3LKjabdLKofm6JQBOfhT6fAsgcmKqaBBid2WimTy0MoLZDrUhdl8erYZiQ39Gy5UuLp93qWmvKIMDCu7PW8BjqkAd0Jzyj0kXh%2B5rqNpZzDGJsTBPZ8tL1kewPajk9znik6qHNV%2F97z0Jysks8jLXUDsgAXoekbU7OgAI6As4nZceLM02cU6EdKB%2BB1WQJ2hcQKVfQfzqrpuYmq2zFgY9zSUYOyVyJr0a4Dqai4nsNzQfulZXxWFrvrHYdxbZygpbSb7kw1Y%2B0z4dvptl%2F3RQ04mT1rPdBrAk3Op1XakK5nOjHl6meR&X-Amz-Signature=b43c7ac16c90f0644e7540d8cfd65f4b8625cfc676c3a279508f744f44d779bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWJTQCU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHMrYmgBl9kCUOqfAd%2BAL%2Fheo5ZCvNHGvm5r%2FJX86OiQIhAI7kwkcNBWryC1kpyAj8dymAXQSij%2B3tGyWRpNKQmlEFKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzpNkztjMNZ%2B8h4kmQq3APcwfbIQ4FeF%2FTg96P89XnDPCDu%2BAZ4iRgcX6rI7KdIDHlPFEqsly0Eb%2BHtLDPBKcyMc05YsFAEzrT888N5ORWJ2tnN2SXn%2Ba8tte4998ALaiYt9Khq3I72r8uzgyxQWfvcix9gxQGN1DGieZDZXPBjAaKe63mBuIYI50Ja6C6QCiGa%2BXx0H4YCCPARyioiWzun01MEEj%2B6%2Bap9ZbfxirFR52Q0WTX8h3O0Ln%2B%2FwlJxdp1kzmVYrQTK5hQHJqRsfQlil7qfIdCPCuSRmJ2GJfULURmxc7BnqEEmOkx%2BBowoOExHdJqt6vJ6HBBd6e%2FGXUy2vXtBb1jxhddP3oOIcQL%2FpLhpDEvBG7rbEcYNyKNPtlZUy8HJJLRRLjVkZQ2IL1Vh9VtEZnNZ1PJdvkcrqJfd38dLUF%2FLjxxdd9T6aa8rqhBWLu2MRa3HzhZUi4UixcGK%2B71ro%2BVY7j60M8Ot6ovUeEsD1blbBtxqejCoDqPIlawcgGdf%2BuN8dm%2BNHAGo2eQethqY5ur4spHaaZ4BSQqBDqoVudZvQaa7ad9MYB6tVBT7r3LKjabdLKofm6JQBOfhT6fAsgcmKqaBBid2WimTy0MoLZDrUhdl8erYZiQ39Gy5UuLp93qWmvKIMDCu7PW8BjqkAd0Jzyj0kXh%2B5rqNpZzDGJsTBPZ8tL1kewPajk9znik6qHNV%2F97z0Jysks8jLXUDsgAXoekbU7OgAI6As4nZceLM02cU6EdKB%2BB1WQJ2hcQKVfQfzqrpuYmq2zFgY9zSUYOyVyJr0a4Dqai4nsNzQfulZXxWFrvrHYdxbZygpbSb7kw1Y%2B0z4dvptl%2F3RQ04mT1rPdBrAk3Op1XakK5nOjHl6meR&X-Amz-Signature=0bcf16f214c9775a4fcaedb80187acc36dc292788ec3ea8ac8bb5319dfcd74ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWJTQCU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHMrYmgBl9kCUOqfAd%2BAL%2Fheo5ZCvNHGvm5r%2FJX86OiQIhAI7kwkcNBWryC1kpyAj8dymAXQSij%2B3tGyWRpNKQmlEFKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzpNkztjMNZ%2B8h4kmQq3APcwfbIQ4FeF%2FTg96P89XnDPCDu%2BAZ4iRgcX6rI7KdIDHlPFEqsly0Eb%2BHtLDPBKcyMc05YsFAEzrT888N5ORWJ2tnN2SXn%2Ba8tte4998ALaiYt9Khq3I72r8uzgyxQWfvcix9gxQGN1DGieZDZXPBjAaKe63mBuIYI50Ja6C6QCiGa%2BXx0H4YCCPARyioiWzun01MEEj%2B6%2Bap9ZbfxirFR52Q0WTX8h3O0Ln%2B%2FwlJxdp1kzmVYrQTK5hQHJqRsfQlil7qfIdCPCuSRmJ2GJfULURmxc7BnqEEmOkx%2BBowoOExHdJqt6vJ6HBBd6e%2FGXUy2vXtBb1jxhddP3oOIcQL%2FpLhpDEvBG7rbEcYNyKNPtlZUy8HJJLRRLjVkZQ2IL1Vh9VtEZnNZ1PJdvkcrqJfd38dLUF%2FLjxxdd9T6aa8rqhBWLu2MRa3HzhZUi4UixcGK%2B71ro%2BVY7j60M8Ot6ovUeEsD1blbBtxqejCoDqPIlawcgGdf%2BuN8dm%2BNHAGo2eQethqY5ur4spHaaZ4BSQqBDqoVudZvQaa7ad9MYB6tVBT7r3LKjabdLKofm6JQBOfhT6fAsgcmKqaBBid2WimTy0MoLZDrUhdl8erYZiQ39Gy5UuLp93qWmvKIMDCu7PW8BjqkAd0Jzyj0kXh%2B5rqNpZzDGJsTBPZ8tL1kewPajk9znik6qHNV%2F97z0Jysks8jLXUDsgAXoekbU7OgAI6As4nZceLM02cU6EdKB%2BB1WQJ2hcQKVfQfzqrpuYmq2zFgY9zSUYOyVyJr0a4Dqai4nsNzQfulZXxWFrvrHYdxbZygpbSb7kw1Y%2B0z4dvptl%2F3RQ04mT1rPdBrAk3Op1XakK5nOjHl6meR&X-Amz-Signature=67edc2097425719cf634754a510d97dc07dd868e0c9a7e68806ce1d78a46a7d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXJ7E3B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQ5Yg24MIOCEKFsDxQ45exmXmJqDj8SAm%2FrMSNfby%2BeAiAkcjmn9G8%2BUe1PIl2R5lA3HRBfF95V2c7OeSdKq0QYbiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbnvs9TNjzfVg1m6SKtwDENGjVsvdBV0ExULYefetOxltbzP7ASJlJ4lJCF0i4FsnYBuQGWnOD1fpaFgyEz4s8wTE6Lht791pOHdht%2BRee3a%2FIQy2jlGXj2Ass1zHwovXDGakwMsyZw5DfvJqQxebyxRXS9EAd5uJAjSq0NZp2Me9YhvcQgrbAd7M7%2BkktpTYhCFIf5CMG6L7fStS0nYeAkkojg4qKRWIpRqD08mf3tGeDzMC6PnzADHEuA90RI5TmyWzrW4Ws9Wz3whe0bEIdpcgOqdCZbjMimrlkLU4bg8kFzA6W%2F73NR9SD3p%2F1uVF2uHf91eOke3ZsF1m5jjPL6TrMboR1hoIbKruHNNyLKnVhIc%2Fp7J6C56Ew7NLAYU5vsuQ26ixZil%2Fm1i7fl7QOYkcgmwkL5IohyfW%2FEdQDHxYwHgC7fmqq%2FlQF4wrO0MhINyU6KmYAYe4XfWwhykmslH0Xh%2Bmt2tbaY4933UjS0QNxoGS9C5PY%2FSdXjUo9ZrYbbCotBX1AxjbPtKWAzz8k2YCqI0bGqf4K3R6wbAEXkhx7AxLe%2BLDfFf4Bp3ryYyrqo69RfX6cpP%2FcFvZByI4UDXxE0VIYuTd42gNHW2kgvJnp3adH6HEuowcexi6Z5sO1QBs1LapaDcxqMswzez1vAY6pgEEBEnTW3SSkuBbIXj4AHUpEqyd%2BaoNAJzs7XaupdUATyk8CQS3EbWzxjuCQQ8SlLb554H4QYrmbhs1wv2e29K%2Fzx8ILSTvrewKnj1uWg0DVqkxy6hiA7q5uq0GenZjDIWxjlXWyLwdk7y2dT6fXTovhmNCk70kS%2B0bdRvUReVrOedzLFQO79cbwouPWLGr%2Bi5nxc8DPKWix3hFoMNePJrBC0cIxTts&X-Amz-Signature=93906dac81e00e971fa963b2d8fd7e59a834d2b0bb119e435f476c7c2b896d6b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXJ7E3B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQ5Yg24MIOCEKFsDxQ45exmXmJqDj8SAm%2FrMSNfby%2BeAiAkcjmn9G8%2BUe1PIl2R5lA3HRBfF95V2c7OeSdKq0QYbiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbnvs9TNjzfVg1m6SKtwDENGjVsvdBV0ExULYefetOxltbzP7ASJlJ4lJCF0i4FsnYBuQGWnOD1fpaFgyEz4s8wTE6Lht791pOHdht%2BRee3a%2FIQy2jlGXj2Ass1zHwovXDGakwMsyZw5DfvJqQxebyxRXS9EAd5uJAjSq0NZp2Me9YhvcQgrbAd7M7%2BkktpTYhCFIf5CMG6L7fStS0nYeAkkojg4qKRWIpRqD08mf3tGeDzMC6PnzADHEuA90RI5TmyWzrW4Ws9Wz3whe0bEIdpcgOqdCZbjMimrlkLU4bg8kFzA6W%2F73NR9SD3p%2F1uVF2uHf91eOke3ZsF1m5jjPL6TrMboR1hoIbKruHNNyLKnVhIc%2Fp7J6C56Ew7NLAYU5vsuQ26ixZil%2Fm1i7fl7QOYkcgmwkL5IohyfW%2FEdQDHxYwHgC7fmqq%2FlQF4wrO0MhINyU6KmYAYe4XfWwhykmslH0Xh%2Bmt2tbaY4933UjS0QNxoGS9C5PY%2FSdXjUo9ZrYbbCotBX1AxjbPtKWAzz8k2YCqI0bGqf4K3R6wbAEXkhx7AxLe%2BLDfFf4Bp3ryYyrqo69RfX6cpP%2FcFvZByI4UDXxE0VIYuTd42gNHW2kgvJnp3adH6HEuowcexi6Z5sO1QBs1LapaDcxqMswzez1vAY6pgEEBEnTW3SSkuBbIXj4AHUpEqyd%2BaoNAJzs7XaupdUATyk8CQS3EbWzxjuCQQ8SlLb554H4QYrmbhs1wv2e29K%2Fzx8ILSTvrewKnj1uWg0DVqkxy6hiA7q5uq0GenZjDIWxjlXWyLwdk7y2dT6fXTovhmNCk70kS%2B0bdRvUReVrOedzLFQO79cbwouPWLGr%2Bi5nxc8DPKWix3hFoMNePJrBC0cIxTts&X-Amz-Signature=8a3ff7e34aeca276fd020336ee84156c4d6af409b4c87fe558075740f8539412&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXJ7E3B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQ5Yg24MIOCEKFsDxQ45exmXmJqDj8SAm%2FrMSNfby%2BeAiAkcjmn9G8%2BUe1PIl2R5lA3HRBfF95V2c7OeSdKq0QYbiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbnvs9TNjzfVg1m6SKtwDENGjVsvdBV0ExULYefetOxltbzP7ASJlJ4lJCF0i4FsnYBuQGWnOD1fpaFgyEz4s8wTE6Lht791pOHdht%2BRee3a%2FIQy2jlGXj2Ass1zHwovXDGakwMsyZw5DfvJqQxebyxRXS9EAd5uJAjSq0NZp2Me9YhvcQgrbAd7M7%2BkktpTYhCFIf5CMG6L7fStS0nYeAkkojg4qKRWIpRqD08mf3tGeDzMC6PnzADHEuA90RI5TmyWzrW4Ws9Wz3whe0bEIdpcgOqdCZbjMimrlkLU4bg8kFzA6W%2F73NR9SD3p%2F1uVF2uHf91eOke3ZsF1m5jjPL6TrMboR1hoIbKruHNNyLKnVhIc%2Fp7J6C56Ew7NLAYU5vsuQ26ixZil%2Fm1i7fl7QOYkcgmwkL5IohyfW%2FEdQDHxYwHgC7fmqq%2FlQF4wrO0MhINyU6KmYAYe4XfWwhykmslH0Xh%2Bmt2tbaY4933UjS0QNxoGS9C5PY%2FSdXjUo9ZrYbbCotBX1AxjbPtKWAzz8k2YCqI0bGqf4K3R6wbAEXkhx7AxLe%2BLDfFf4Bp3ryYyrqo69RfX6cpP%2FcFvZByI4UDXxE0VIYuTd42gNHW2kgvJnp3adH6HEuowcexi6Z5sO1QBs1LapaDcxqMswzez1vAY6pgEEBEnTW3SSkuBbIXj4AHUpEqyd%2BaoNAJzs7XaupdUATyk8CQS3EbWzxjuCQQ8SlLb554H4QYrmbhs1wv2e29K%2Fzx8ILSTvrewKnj1uWg0DVqkxy6hiA7q5uq0GenZjDIWxjlXWyLwdk7y2dT6fXTovhmNCk70kS%2B0bdRvUReVrOedzLFQO79cbwouPWLGr%2Bi5nxc8DPKWix3hFoMNePJrBC0cIxTts&X-Amz-Signature=b88381f38d8c62e7b55d15bc0fc6cc9f7d6f5c817776fee9f07dc3a8da5f2341&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXJ7E3B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQ5Yg24MIOCEKFsDxQ45exmXmJqDj8SAm%2FrMSNfby%2BeAiAkcjmn9G8%2BUe1PIl2R5lA3HRBfF95V2c7OeSdKq0QYbiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbnvs9TNjzfVg1m6SKtwDENGjVsvdBV0ExULYefetOxltbzP7ASJlJ4lJCF0i4FsnYBuQGWnOD1fpaFgyEz4s8wTE6Lht791pOHdht%2BRee3a%2FIQy2jlGXj2Ass1zHwovXDGakwMsyZw5DfvJqQxebyxRXS9EAd5uJAjSq0NZp2Me9YhvcQgrbAd7M7%2BkktpTYhCFIf5CMG6L7fStS0nYeAkkojg4qKRWIpRqD08mf3tGeDzMC6PnzADHEuA90RI5TmyWzrW4Ws9Wz3whe0bEIdpcgOqdCZbjMimrlkLU4bg8kFzA6W%2F73NR9SD3p%2F1uVF2uHf91eOke3ZsF1m5jjPL6TrMboR1hoIbKruHNNyLKnVhIc%2Fp7J6C56Ew7NLAYU5vsuQ26ixZil%2Fm1i7fl7QOYkcgmwkL5IohyfW%2FEdQDHxYwHgC7fmqq%2FlQF4wrO0MhINyU6KmYAYe4XfWwhykmslH0Xh%2Bmt2tbaY4933UjS0QNxoGS9C5PY%2FSdXjUo9ZrYbbCotBX1AxjbPtKWAzz8k2YCqI0bGqf4K3R6wbAEXkhx7AxLe%2BLDfFf4Bp3ryYyrqo69RfX6cpP%2FcFvZByI4UDXxE0VIYuTd42gNHW2kgvJnp3adH6HEuowcexi6Z5sO1QBs1LapaDcxqMswzez1vAY6pgEEBEnTW3SSkuBbIXj4AHUpEqyd%2BaoNAJzs7XaupdUATyk8CQS3EbWzxjuCQQ8SlLb554H4QYrmbhs1wv2e29K%2Fzx8ILSTvrewKnj1uWg0DVqkxy6hiA7q5uq0GenZjDIWxjlXWyLwdk7y2dT6fXTovhmNCk70kS%2B0bdRvUReVrOedzLFQO79cbwouPWLGr%2Bi5nxc8DPKWix3hFoMNePJrBC0cIxTts&X-Amz-Signature=eb1432fdc7d40c580280907c40b74780ff9fa07632097a2f0f1cb858e756be7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXJ7E3B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQ5Yg24MIOCEKFsDxQ45exmXmJqDj8SAm%2FrMSNfby%2BeAiAkcjmn9G8%2BUe1PIl2R5lA3HRBfF95V2c7OeSdKq0QYbiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbnvs9TNjzfVg1m6SKtwDENGjVsvdBV0ExULYefetOxltbzP7ASJlJ4lJCF0i4FsnYBuQGWnOD1fpaFgyEz4s8wTE6Lht791pOHdht%2BRee3a%2FIQy2jlGXj2Ass1zHwovXDGakwMsyZw5DfvJqQxebyxRXS9EAd5uJAjSq0NZp2Me9YhvcQgrbAd7M7%2BkktpTYhCFIf5CMG6L7fStS0nYeAkkojg4qKRWIpRqD08mf3tGeDzMC6PnzADHEuA90RI5TmyWzrW4Ws9Wz3whe0bEIdpcgOqdCZbjMimrlkLU4bg8kFzA6W%2F73NR9SD3p%2F1uVF2uHf91eOke3ZsF1m5jjPL6TrMboR1hoIbKruHNNyLKnVhIc%2Fp7J6C56Ew7NLAYU5vsuQ26ixZil%2Fm1i7fl7QOYkcgmwkL5IohyfW%2FEdQDHxYwHgC7fmqq%2FlQF4wrO0MhINyU6KmYAYe4XfWwhykmslH0Xh%2Bmt2tbaY4933UjS0QNxoGS9C5PY%2FSdXjUo9ZrYbbCotBX1AxjbPtKWAzz8k2YCqI0bGqf4K3R6wbAEXkhx7AxLe%2BLDfFf4Bp3ryYyrqo69RfX6cpP%2FcFvZByI4UDXxE0VIYuTd42gNHW2kgvJnp3adH6HEuowcexi6Z5sO1QBs1LapaDcxqMswzez1vAY6pgEEBEnTW3SSkuBbIXj4AHUpEqyd%2BaoNAJzs7XaupdUATyk8CQS3EbWzxjuCQQ8SlLb554H4QYrmbhs1wv2e29K%2Fzx8ILSTvrewKnj1uWg0DVqkxy6hiA7q5uq0GenZjDIWxjlXWyLwdk7y2dT6fXTovhmNCk70kS%2B0bdRvUReVrOedzLFQO79cbwouPWLGr%2Bi5nxc8DPKWix3hFoMNePJrBC0cIxTts&X-Amz-Signature=0ad3fd67bb34e9e2673cd5e8c6cc897a27fe913036709c55e3497467a945020a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXJ7E3B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQ5Yg24MIOCEKFsDxQ45exmXmJqDj8SAm%2FrMSNfby%2BeAiAkcjmn9G8%2BUe1PIl2R5lA3HRBfF95V2c7OeSdKq0QYbiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbnvs9TNjzfVg1m6SKtwDENGjVsvdBV0ExULYefetOxltbzP7ASJlJ4lJCF0i4FsnYBuQGWnOD1fpaFgyEz4s8wTE6Lht791pOHdht%2BRee3a%2FIQy2jlGXj2Ass1zHwovXDGakwMsyZw5DfvJqQxebyxRXS9EAd5uJAjSq0NZp2Me9YhvcQgrbAd7M7%2BkktpTYhCFIf5CMG6L7fStS0nYeAkkojg4qKRWIpRqD08mf3tGeDzMC6PnzADHEuA90RI5TmyWzrW4Ws9Wz3whe0bEIdpcgOqdCZbjMimrlkLU4bg8kFzA6W%2F73NR9SD3p%2F1uVF2uHf91eOke3ZsF1m5jjPL6TrMboR1hoIbKruHNNyLKnVhIc%2Fp7J6C56Ew7NLAYU5vsuQ26ixZil%2Fm1i7fl7QOYkcgmwkL5IohyfW%2FEdQDHxYwHgC7fmqq%2FlQF4wrO0MhINyU6KmYAYe4XfWwhykmslH0Xh%2Bmt2tbaY4933UjS0QNxoGS9C5PY%2FSdXjUo9ZrYbbCotBX1AxjbPtKWAzz8k2YCqI0bGqf4K3R6wbAEXkhx7AxLe%2BLDfFf4Bp3ryYyrqo69RfX6cpP%2FcFvZByI4UDXxE0VIYuTd42gNHW2kgvJnp3adH6HEuowcexi6Z5sO1QBs1LapaDcxqMswzez1vAY6pgEEBEnTW3SSkuBbIXj4AHUpEqyd%2BaoNAJzs7XaupdUATyk8CQS3EbWzxjuCQQ8SlLb554H4QYrmbhs1wv2e29K%2Fzx8ILSTvrewKnj1uWg0DVqkxy6hiA7q5uq0GenZjDIWxjlXWyLwdk7y2dT6fXTovhmNCk70kS%2B0bdRvUReVrOedzLFQO79cbwouPWLGr%2Bi5nxc8DPKWix3hFoMNePJrBC0cIxTts&X-Amz-Signature=01ff7b4bad773f49a72bb3cba561c782025aa3b1a2d690ace02c7baa9ec49856&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE66X5ZP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQddNYrRIZnwolbx1gOnb1JZmAsL%2FVkA1%2Fm5cDVMgbsgIgBCjRcYRS8yF995PvexMpKU9mv6zSwB%2FB2aZNrh9KmCkqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB0ePw1FM4hxYKSG0SrcA%2BZbkOBGetmX66jk1iAuQqkMkqVErkZDu6gjBedun7muAuRfULeth3tFpG3E%2FS8DVWCWQjCD%2FUELaX0I%2FTFJ6npzH22Ixt7VfoMOKuOV8fomWvcNvlkJJV58Jboo479UsH%2FAdiWji%2B%2FEIPerZhLKGfieVg%2FOMUoa2LaqS08UgtltTxQBehWbYlEDjbWCtGXg8wg5%2BIIAPsq2hQKPvOav%2BGlkWy8fvNUQAGf0adkJNHVd06OpCvq44WZlAKIfmylm2sta2eKBfv2x47ysvZ%2BMwhKVn7yRQELvOdEqweoFA2zuHEz6j%2BX2ZTiUBb9fToxaA6XOoUg97255RyrH%2FPrdUbVeVXDZ7dChLzepGf9sybDifwTpKTuZNv1YQeXL8IwhjYr1Lq%2Bm%2Fxl211zPaf0DH33kMaV3VJMwFb5dnTVEhyLZy7tLYHIhbL3RH6Lgq5DnABU%2FKTX8zEWznOS4%2BOcCOBaU7RI8zDlKDcYG45Tq636KfDnF%2Bbjb6b8Vlu3aKEPcJqM68gusbnJAuKuVWfKtlXq3Uxw%2B8YNJv9srEjlWvy1iKo8rVRakmYka4ZsevBFuTd89AkwLzKfMhyiG2yLsJytwFhvlWnSLQuX1C8lnCcDTOiZR%2BQ7vBTLyC6l7MLDs9bwGOqUBRBhUoHN%2B263pK6svv3APVw74%2BajjDCRlVGNfWfgiozLCZMmqN74tXsPCwFPQDJib%2B%2FyrAFMlcrFTIMsHk8%2Fg9xsdvbP1jTSqY9UN%2F%2BSWIx47iSB%2BwzA1%2FvWdvCKVNuFU0Kui%2FZxDXKaZTwHerlpJRvqjXIp5ygYw2snzWPkx%2Bg%2BwDtKmi%2BBl3h%2BqpCM01ddF0PXLPxB%2BQq3Udp%2Bi3lDU60Sw1iU%2F&X-Amz-Signature=eee22d477f15f7e95c8b33ad217ae9950d5a269a03e9982de9fe652ef7b83347&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TDXTE7T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChdv6FoJO0ZP%2B%2Br1qiYDfbgfyuDpPqZYkLCgHOffntRQIhAP67y9vaSmQL21g94aKAOStFgo2OsJiFFRPTAopS9aSaKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwIeqlviedKSJyIdwq3ANfKfifIH6fm6FfwDjzTHDr6FHPycfrZSzwvZcUGhjRwlOyRy%2FHgrgjjVNeHP4PnmNx9NldPACNMQm9KBCkvmgVsb3r7sGYIZk5Q3EkRXsZd6JRkO8lLxvnxIhNRsMuUE6%2F%2F%2BRQogHW5BdbUI8dJzN1YkA%2FiAc%2FLSJDCcZDa9PqT61%2BJbNOz1ZU9i7zzGzPAaaXglWUFN%2Byhj6Gb50QiLq%2BhCDXqgzSDAW4A4gjXVsRrbWlpUSZBxk9hTuqVxW15fCpNJlJDGREBxRDb4calo5rusdchftpHEdrnRFX2db%2F22JiZjXM9iIrnmcSm0yEfP2zbUIL1%2BbMwWlikS4k6VqTumwtMKYbeQTN2DicRRkJNUtI%2F3fYUW%2FfxQk12sB9MUx86IQ4aw%2BFeEEmHkfamldDuLY9cVsV7jOc%2FoPCJxFbXgcjn4Uj9VAZsFAv20F2VGfwOkPWkWOE2AMskDnGNTSfH%2FO1p%2FU5j%2B49mdnnHwLP6VGjpcZJSpaCZzqA2OZDzLmAB2MI4FUdRILUtr1J5wc14ZMgoumLRvzEn3rrXSlEO29a3hcj8l8AGxxRHCCchNJj607jhLRMBCL%2Ft4ZxRnU2bAug7%2BQ2RbmHftWrquVzBSjy0Ia35mQCTmQqZTCm7fW8BjqkAfvgxtirEYA8zMUI9a73BphKTbYdrt55fCI4GbXBkOtG5Js0NvGEzFz07mxHk6x4IX4dXzr8LW0SsvHLbnJ2ifOvvCqv9RmpWaBaWBLtJA3G6YWlsSb9PC6Df4U8%2FvQebpw5WX%2FW%2F%2FGcIR1fpvoB6IEeGqhhbKDr6YjVFUAr5TOJa9q2NIDaUUcZFTfJkbD3WEFC1JQMCwh0E7SCtphdCpHsGj6T&X-Amz-Signature=8cb83735f7aa50ffeed61554ab6e94168e530482d131673834f6531a1ec0f539&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXJ7E3B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQ5Yg24MIOCEKFsDxQ45exmXmJqDj8SAm%2FrMSNfby%2BeAiAkcjmn9G8%2BUe1PIl2R5lA3HRBfF95V2c7OeSdKq0QYbiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbnvs9TNjzfVg1m6SKtwDENGjVsvdBV0ExULYefetOxltbzP7ASJlJ4lJCF0i4FsnYBuQGWnOD1fpaFgyEz4s8wTE6Lht791pOHdht%2BRee3a%2FIQy2jlGXj2Ass1zHwovXDGakwMsyZw5DfvJqQxebyxRXS9EAd5uJAjSq0NZp2Me9YhvcQgrbAd7M7%2BkktpTYhCFIf5CMG6L7fStS0nYeAkkojg4qKRWIpRqD08mf3tGeDzMC6PnzADHEuA90RI5TmyWzrW4Ws9Wz3whe0bEIdpcgOqdCZbjMimrlkLU4bg8kFzA6W%2F73NR9SD3p%2F1uVF2uHf91eOke3ZsF1m5jjPL6TrMboR1hoIbKruHNNyLKnVhIc%2Fp7J6C56Ew7NLAYU5vsuQ26ixZil%2Fm1i7fl7QOYkcgmwkL5IohyfW%2FEdQDHxYwHgC7fmqq%2FlQF4wrO0MhINyU6KmYAYe4XfWwhykmslH0Xh%2Bmt2tbaY4933UjS0QNxoGS9C5PY%2FSdXjUo9ZrYbbCotBX1AxjbPtKWAzz8k2YCqI0bGqf4K3R6wbAEXkhx7AxLe%2BLDfFf4Bp3ryYyrqo69RfX6cpP%2FcFvZByI4UDXxE0VIYuTd42gNHW2kgvJnp3adH6HEuowcexi6Z5sO1QBs1LapaDcxqMswzez1vAY6pgEEBEnTW3SSkuBbIXj4AHUpEqyd%2BaoNAJzs7XaupdUATyk8CQS3EbWzxjuCQQ8SlLb554H4QYrmbhs1wv2e29K%2Fzx8ILSTvrewKnj1uWg0DVqkxy6hiA7q5uq0GenZjDIWxjlXWyLwdk7y2dT6fXTovhmNCk70kS%2B0bdRvUReVrOedzLFQO79cbwouPWLGr%2Bi5nxc8DPKWix3hFoMNePJrBC0cIxTts&X-Amz-Signature=276d082efa2d0f54ede099ac7dba573ff492a1667a74a9d43c5a531d5ae260e6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXJ7E3B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQ5Yg24MIOCEKFsDxQ45exmXmJqDj8SAm%2FrMSNfby%2BeAiAkcjmn9G8%2BUe1PIl2R5lA3HRBfF95V2c7OeSdKq0QYbiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbnvs9TNjzfVg1m6SKtwDENGjVsvdBV0ExULYefetOxltbzP7ASJlJ4lJCF0i4FsnYBuQGWnOD1fpaFgyEz4s8wTE6Lht791pOHdht%2BRee3a%2FIQy2jlGXj2Ass1zHwovXDGakwMsyZw5DfvJqQxebyxRXS9EAd5uJAjSq0NZp2Me9YhvcQgrbAd7M7%2BkktpTYhCFIf5CMG6L7fStS0nYeAkkojg4qKRWIpRqD08mf3tGeDzMC6PnzADHEuA90RI5TmyWzrW4Ws9Wz3whe0bEIdpcgOqdCZbjMimrlkLU4bg8kFzA6W%2F73NR9SD3p%2F1uVF2uHf91eOke3ZsF1m5jjPL6TrMboR1hoIbKruHNNyLKnVhIc%2Fp7J6C56Ew7NLAYU5vsuQ26ixZil%2Fm1i7fl7QOYkcgmwkL5IohyfW%2FEdQDHxYwHgC7fmqq%2FlQF4wrO0MhINyU6KmYAYe4XfWwhykmslH0Xh%2Bmt2tbaY4933UjS0QNxoGS9C5PY%2FSdXjUo9ZrYbbCotBX1AxjbPtKWAzz8k2YCqI0bGqf4K3R6wbAEXkhx7AxLe%2BLDfFf4Bp3ryYyrqo69RfX6cpP%2FcFvZByI4UDXxE0VIYuTd42gNHW2kgvJnp3adH6HEuowcexi6Z5sO1QBs1LapaDcxqMswzez1vAY6pgEEBEnTW3SSkuBbIXj4AHUpEqyd%2BaoNAJzs7XaupdUATyk8CQS3EbWzxjuCQQ8SlLb554H4QYrmbhs1wv2e29K%2Fzx8ILSTvrewKnj1uWg0DVqkxy6hiA7q5uq0GenZjDIWxjlXWyLwdk7y2dT6fXTovhmNCk70kS%2B0bdRvUReVrOedzLFQO79cbwouPWLGr%2Bi5nxc8DPKWix3hFoMNePJrBC0cIxTts&X-Amz-Signature=f698b920525c744c1aa488116308085cc4ca26e8e63433e02f48344308ae2366&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXJ7E3B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQ5Yg24MIOCEKFsDxQ45exmXmJqDj8SAm%2FrMSNfby%2BeAiAkcjmn9G8%2BUe1PIl2R5lA3HRBfF95V2c7OeSdKq0QYbiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbnvs9TNjzfVg1m6SKtwDENGjVsvdBV0ExULYefetOxltbzP7ASJlJ4lJCF0i4FsnYBuQGWnOD1fpaFgyEz4s8wTE6Lht791pOHdht%2BRee3a%2FIQy2jlGXj2Ass1zHwovXDGakwMsyZw5DfvJqQxebyxRXS9EAd5uJAjSq0NZp2Me9YhvcQgrbAd7M7%2BkktpTYhCFIf5CMG6L7fStS0nYeAkkojg4qKRWIpRqD08mf3tGeDzMC6PnzADHEuA90RI5TmyWzrW4Ws9Wz3whe0bEIdpcgOqdCZbjMimrlkLU4bg8kFzA6W%2F73NR9SD3p%2F1uVF2uHf91eOke3ZsF1m5jjPL6TrMboR1hoIbKruHNNyLKnVhIc%2Fp7J6C56Ew7NLAYU5vsuQ26ixZil%2Fm1i7fl7QOYkcgmwkL5IohyfW%2FEdQDHxYwHgC7fmqq%2FlQF4wrO0MhINyU6KmYAYe4XfWwhykmslH0Xh%2Bmt2tbaY4933UjS0QNxoGS9C5PY%2FSdXjUo9ZrYbbCotBX1AxjbPtKWAzz8k2YCqI0bGqf4K3R6wbAEXkhx7AxLe%2BLDfFf4Bp3ryYyrqo69RfX6cpP%2FcFvZByI4UDXxE0VIYuTd42gNHW2kgvJnp3adH6HEuowcexi6Z5sO1QBs1LapaDcxqMswzez1vAY6pgEEBEnTW3SSkuBbIXj4AHUpEqyd%2BaoNAJzs7XaupdUATyk8CQS3EbWzxjuCQQ8SlLb554H4QYrmbhs1wv2e29K%2Fzx8ILSTvrewKnj1uWg0DVqkxy6hiA7q5uq0GenZjDIWxjlXWyLwdk7y2dT6fXTovhmNCk70kS%2B0bdRvUReVrOedzLFQO79cbwouPWLGr%2Bi5nxc8DPKWix3hFoMNePJrBC0cIxTts&X-Amz-Signature=5a92e6572ae95cd882ade4e1ea2e30f98e83d50ae30c0f235314ec15757b5d20&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662I72XKQT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjR2usqOA8OxybgzLR1Dw838MKY5GhhDdaBNJQzbkBRAIhANQIWeEhpv%2B1Q1CoEl2Jf6SkZpf0dX%2FJ95tVAy5IucPnKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy69FrboaDIH0BjrrMq3AN2rDY1D%2BhKc4b0ufNR%2FJTkwVK6OkedLM%2BaxD4PyI8W3ojymv5Kn5eiIsG8LE27iuc7jlWkqCHeJPEgKhKFl5kLGljoONASmi8H7nAO04NZBCYds5o%2Fyn3J33ZiRz64%2BH2y11WEt1MywvFq3yry994siet%2FnizEX26YD9Z73FBM39mH93q5NI9uompyCBxeH%2Fwl0C7wtGmpi71pliFxBfH26ihNcQ53BabkrDvZUgXlDBBL0ESnRZTktvTK61hgkRGM%2BL2%2Fy4pB3wxxAXVuBxTQlPXUhixS2Jj%2FG0RLTJOPhPwz2zC3vSz7Zov44HUXairYAY9v3fOcrFPY41%2B6jCFwE010aOT2P8i4GMfVkhY26V2JQJcA%2FUW3DifdrlpoZf%2BBkOtNB%2Bw9ZF5%2BiJjavkqK5oPCokmv9e%2FJUk7607KlJl4jSfy33ygeA2ql6h4U759yqN3MAwMtiiNgVSViUTNW3P7G68JQya4xoSnmgwuNL2PrJqJww6OYXzz28Q4mn8GYdJNPphFOps5xynt%2BhsfRj0Ev5ZXaTQfhHRhiye0oz3IC%2BNEUJR7NKEoF1x1Z%2ByY3Fc3VGmM2%2BciFveJTm5A9P5CgK2WvdOEUndmWGvKQKnHZveH3wKJ8%2Fw1LEDDG7PW8BjqkAeP6CMmk8MX%2B%2BjX1GlPSIIRlenhISY%2BBN%2B9XURXXaAitWj3UQj%2BKYJ%2BObD4kDe4dGNSRhwEthOBqGGamGVY%2BkoSx23q6%2BxpJ8NW4LdtEHk2FhyZY%2BFiDbrxbtvBGmhMBTrMRI43%2B5aVyl7zpgMpA3DpvnL32W41hgXPzNwUZVNpugvG8iIeNu1FPnb%2BZgf6aCJ0kfDnACHACVBbVi5v1ozwIAuI2&X-Amz-Signature=26f08f935232b34b328fef7d39e7ba31af7c97b862cda3f74a1ea6c66d58a86c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U63HABFO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGUjTRfJPJKQyLzQpHAIYupLMLN%2B1s6xESBi4l3y0JSsAiEA%2FAaK2IB3jFB9JRzNOTthk6GbRGlPhlcjI3p2Xsxh%2FhsqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEWKKc9ZmEqpM4C5LSrcAxg9MNzbQcux9VfYuWvtQt46EizOT7kRxVnuXmvPWy2vIM5TMVyuW6QSx0VEZBRZOvnf%2Bj0C9nDTEe3aSPcvoaSzLgIGy1TMb7p%2BDFTzJSFmijVmYAEo6Fx0Kn6xZH2uFndSCWEOyZosRQVVXyabOvfJInIxy6aUMg%2BDHuBVgguiBL9kWIc4%2FqSBqfmpPMzj%2BR6obP6TASugSdsGg9xPYnZgSEVUv7TFEn6iQeV1%2Fh3mMPHaAydOHZm80n0vVh30sZvCObFmffli%2FUtDZH62ZD3QJCdPEX0LbivxTwJPOoyzQ06UotMLmFizS3pyCg9e3GqdH%2BYdUURzzIGNAdl2%2BoQ1%2BUBVsMAzU3djZeEJtljmvoXrtvPyYizUgrXa8YuXTqhAOlZWT3llVeVdQ11uRtuEjAxyfQmofy%2FT%2FbiNCFUynzvsfPvRODydsdqd13g4MWwJcmRZGGQdjgWWVfFpNeG6m2Ih6QMaEiAZpy6cnyardCVxrPFFXbW%2FmnWNKS3rDJQYai%2FHvKvR3J7SYSeOafwsxyoAyQUqedZ1awPGdzCAj2i4Z%2F0d0StmO6cOOiniPdh5NcTlBV3ELE82anzSFjGoWdOtw%2FsxGvQMRpMWa1B7k1jGQ5iuzYzh7xkfMJvs9bwGOqUB%2B2Jo3GCnAo96zoRv2TohryMnq6ivS82YrsFI55w%2BOPzAT4yiYQn583SLPZqziBti9qBzhVJPe8RbZXp7h%2BMkyjqYy6lH7t3GgtptTkccvpU9JRGjFCv3YQhKRVPsA%2F5plyL3O2bvCOs1AYBOtNUkzBLzzBHpcdaQVq7yWDKhynysLmq%2BruhLMZqpV2VsROr8vB56AVwR9T%2FSPzEk0WY7rFu5Xa%2BA&X-Amz-Signature=8ecfa48e00ec0928927989e5d875a2d2865754badac1568e260298b794c7e4a2&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPU72WDQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOnhXSSo585KOMKyDWpdoz1vJOuTrc2OIuFGvvx7maGQIhAPDtrZ6x4HGc2chF7CAuthMaenEPuYeROCjtQygiNMyKKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxVpO8YlhzbOV8XysYq3AOqwnc5%2BvWakoubxMmU1P028x6bDu81ccTdFMoKbcka4ayWX2O2u45Hp%2BNsgnun%2Bpm5ZCUG22HJ5O09%2Bytt0i7k%2FwBTlMTXaPuD75zcBX%2BQvv4ddOthTH86nZH1ml%2Bx4plA427rf0mMIzerMzWjHvc6ofhhw3jjAs2Gqfdjx6%2BuVThnLf%2B5soNj93my7%2B58Gi2SmvpI2XnDXOusp6mu7C6mc8hpNWYKhDbnlqyAVPVuNaGlzxz0mmvK4%2BRRcUeKpReB8YkX4tJ9pRu3hdIkCKXT1xUuuWWoI4giRpSUF%2FD294ADuplSZQtWRVUEdLKWh8DKZODk3cc44gNsf6aRzPtdGk3SZBUCBCiV%2F%2F0mO9djB%2B4V%2Ff4k6BKdKJO8OwAHyBQSQiVd2Tujn4LuSMzU45lf3JybGUoDhizWOJh6VIIvv7qAfnIS2PZttYNO30z7tqJwDmgjvt6TfZE9uNElpJVIoQdVLx6%2FWb7flo%2BoBv2jTT5znrmErLU50q%2Feja5HbCZbzJQap03hmUUg%2BUH1N%2BeOHyEET8fPZIsdeAe%2FnARykXgJk%2FpRrFuIdGMjj584jOuqROfY6CkqqKVGQgsP7tJBClUG1Guis2KVI50ZcUqdscXd2HjKXE2DjLIpJDC67PW8BjqkAbTW5yJISQjkFRfSeoUy%2FfZpOmRFPfbDxqDfTKIY1maMioq5V1XukeZiu%2FobnpMrk4fX0PPK%2FX7pb2RzSa%2BK%2FofJIcsoIECNRVL9zPfjpD6q6C%2ByJ5%2B8nNoko37YGOHPOY3oq0kmqvMDVFB9qiJ3xSxL4qEYABXI9vWLWo1EsE01jPr1XL5ru%2BpFt3dXqq24ZpU32C1imfYC9wKo4mjkm%2B80iZIt&X-Amz-Signature=f493077313da9a95a53e04e4fb8798f0d24b5d9f5033c9a84134b96975af590a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667FJWDR4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGpXUpmcTAkCgFAjZvwYwDuO37mNNtb0rUA3%2B1LCc%2BofAiAPW4LJkJIirFGVA%2BAMKSv9ctq0ZCeGMLnO6y6RDCq4SyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgvivxOEQttMAuWIgKtwDQSMGVh9%2F7AzjllNwqLttPnLihqIC1%2Fee%2FMSX41eRKzRBycDJ4oHqTUhvBl4cdajzYv9bYBDUFJk4oONf6CxYK8o1MeUWnFzb6Ktf%2F3MO0wkmNTg7IJ5uPchN8cInXRBnlvd4MjJl8yf9VaDPkDKA2Cr14T8oXas3ROVl3J%2Fjw4xXEXG1Vn17VWbU4M4BnTDG3RQ5%2BflXzM2wGvjnJKLGksL64VNtmPO%2BFRQ75r1JyiNNyw5QA2HNr81q7YEIxIc1ofvnKSC5hrziYUc7JbQBSXUHd8iEkgYRQiJozUvnJnolprm5YjnLpVblpmNCo3wbEMgSVVl3bI8JIcBYg0Uw%2FJYcEnRywX2CurxSMLSx8eqVfc2OWoLRNDA1LA6Kao%2BZNlvf5MZcFfKwS1qpE5E8QnKEvYt2LDmhsoz7%2BFzjHTPNdZJXik4GIHQrDbzTPy4zLp7q4ds5DC7VUMtTy4DwE0IbX4cBQFt9vEg0vzqmOfO4oXMqlGRr%2FRdN566W%2FuMCn626tkNk%2FsOjMRNcGEwtkbW7pldaSZPanqchMEz7YFFypJPBPJjFTYoGpzXlWVbifREK8XB9XoaSCdosrlQ%2F0T8C08Q3odmoNX1%2B10Mv2ZgqJVJ5qw2x0jkX%2FAkwnOz1vAY6pgF26ptS5Hk%2FqST5ies%2FN8d4oj7WGr4XpUAwGKxLQT5yVTuWKDSpYnU79NcyQMt%2B0q20KGIvSg5sVPxQV6vJ1S4ua73aJIGF5U35lMKy4r2l1PVjL8KVCHqNRg6xqbDXw91DRIk6LTO6qcaa%2BgpVeh2zWNvQibr0JRZ8kWf7zhjdeCVx0G%2FPqphx1keQ0rNiHfJYwUr%2FxkZopV%2FklB8nrqW2uQ%2FEJfuG&X-Amz-Signature=ca79a69731d4e89f35d27b6194c6bafb339ec8411d1bb63d66cefcbbe250dd71&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667FJWDR4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGpXUpmcTAkCgFAjZvwYwDuO37mNNtb0rUA3%2B1LCc%2BofAiAPW4LJkJIirFGVA%2BAMKSv9ctq0ZCeGMLnO6y6RDCq4SyqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgvivxOEQttMAuWIgKtwDQSMGVh9%2F7AzjllNwqLttPnLihqIC1%2Fee%2FMSX41eRKzRBycDJ4oHqTUhvBl4cdajzYv9bYBDUFJk4oONf6CxYK8o1MeUWnFzb6Ktf%2F3MO0wkmNTg7IJ5uPchN8cInXRBnlvd4MjJl8yf9VaDPkDKA2Cr14T8oXas3ROVl3J%2Fjw4xXEXG1Vn17VWbU4M4BnTDG3RQ5%2BflXzM2wGvjnJKLGksL64VNtmPO%2BFRQ75r1JyiNNyw5QA2HNr81q7YEIxIc1ofvnKSC5hrziYUc7JbQBSXUHd8iEkgYRQiJozUvnJnolprm5YjnLpVblpmNCo3wbEMgSVVl3bI8JIcBYg0Uw%2FJYcEnRywX2CurxSMLSx8eqVfc2OWoLRNDA1LA6Kao%2BZNlvf5MZcFfKwS1qpE5E8QnKEvYt2LDmhsoz7%2BFzjHTPNdZJXik4GIHQrDbzTPy4zLp7q4ds5DC7VUMtTy4DwE0IbX4cBQFt9vEg0vzqmOfO4oXMqlGRr%2FRdN566W%2FuMCn626tkNk%2FsOjMRNcGEwtkbW7pldaSZPanqchMEz7YFFypJPBPJjFTYoGpzXlWVbifREK8XB9XoaSCdosrlQ%2F0T8C08Q3odmoNX1%2B10Mv2ZgqJVJ5qw2x0jkX%2FAkwnOz1vAY6pgF26ptS5Hk%2FqST5ies%2FN8d4oj7WGr4XpUAwGKxLQT5yVTuWKDSpYnU79NcyQMt%2B0q20KGIvSg5sVPxQV6vJ1S4ua73aJIGF5U35lMKy4r2l1PVjL8KVCHqNRg6xqbDXw91DRIk6LTO6qcaa%2BgpVeh2zWNvQibr0JRZ8kWf7zhjdeCVx0G%2FPqphx1keQ0rNiHfJYwUr%2FxkZopV%2FklB8nrqW2uQ%2FEJfuG&X-Amz-Signature=3f0e25db62411696287bcb418eb3b4f584bfd8f2f63966ef3d3db0687a5dfa8c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
