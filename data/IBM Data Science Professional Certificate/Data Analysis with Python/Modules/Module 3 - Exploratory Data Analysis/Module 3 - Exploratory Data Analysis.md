

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JNQBEAF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIBPLrjAzP5ERySc0eOlNYGKQ1bCXvTnsIT6v%2FAvx1XM%2BAiEAtCbjYR58%2FHVi8Xz0z5%2FWgs5aou49evT1K87CQrbEQi0q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDONffmMfKSL3H3FTXyrcA%2F%2FIBVpZobXaYo7Es7FA7Iqvx7Jo3r5G0ZLxhpW9s0Fdk8fTSi8sZcJ34krvtWyind1tETaukE%2FVpO8NFER5IUf5jygp6u90E%2B51v9MKPhLFuHDucfVjv6u%2FDAptHIdp79jV4aI7NVgk%2FA00O2y1RDcaDhN%2FBZEma8iE5Lax1dTMk%2FC9AlMcMn1QeK8qfyCJHApCjmqyI%2BHWGlLwBg4MyScMCPYkef3harWIxDe7KFDfKH6DNGRHDtVmNUFAii6%2B7V3IHjlqbMlVH8zWjaKZp5tTN67fnYZaYx9DC5qsH1UVtRo2FRpCNH%2FVkveHJW1dK4Jyx8hS56jiH8l569eGZFlLJWciA%2Flmp%2FoBc0PqiQc8p0OSWnrSEWmyIvp%2Bo5cHEBqxm0zRxKkkxFTXE3LgnAOcbtdBIMkGXOoqa6siNfkQBba4w2WcfjAbyAiZjGJ4Ce9hZDQRoOm2JKQTqY0KtbaTe%2Fq1gXdgnm%2F232qt2Pbo4U0KbFXfFL7cT8J5edQlHCo4JnKDZqhNNKp4mlbRnNt%2BMhoq5DuWCo3rhi3wUKHfPfdE4iXig1E6JvWLR6KKGfNCQBA53wQlm3FwL4MumUKONR5ZNTOHr0HWle1u%2BV6iSeerWXaZ%2BBxoY4COMP6VjL0GOqUBiARkXsXL55zZhjSnuak49VCNp0jI7JDVnffOwi3tUCILZhKD2tNaq76FqCPQ2TtuiQREuD9lZgiYmh83YQgExTZ%2F7HZiOLQebMZbrEH6EOSn7Uci0jqR1BwaM55FzMr0Zj0CNwo02M%2B%2FjMtf2uzNmtz%2BEXLKu5bnayoC9HQczJkOn2bVZpq7p4ukxQ5GihghmI4GBiQn4%2F0HtrWgKRhZS%2BiAwBxJ&X-Amz-Signature=5074e4f41bd3b9cbe27442ba86c2293b45284b8f9c5abfdbf2647875a843a971&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JNQBEAF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIBPLrjAzP5ERySc0eOlNYGKQ1bCXvTnsIT6v%2FAvx1XM%2BAiEAtCbjYR58%2FHVi8Xz0z5%2FWgs5aou49evT1K87CQrbEQi0q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDONffmMfKSL3H3FTXyrcA%2F%2FIBVpZobXaYo7Es7FA7Iqvx7Jo3r5G0ZLxhpW9s0Fdk8fTSi8sZcJ34krvtWyind1tETaukE%2FVpO8NFER5IUf5jygp6u90E%2B51v9MKPhLFuHDucfVjv6u%2FDAptHIdp79jV4aI7NVgk%2FA00O2y1RDcaDhN%2FBZEma8iE5Lax1dTMk%2FC9AlMcMn1QeK8qfyCJHApCjmqyI%2BHWGlLwBg4MyScMCPYkef3harWIxDe7KFDfKH6DNGRHDtVmNUFAii6%2B7V3IHjlqbMlVH8zWjaKZp5tTN67fnYZaYx9DC5qsH1UVtRo2FRpCNH%2FVkveHJW1dK4Jyx8hS56jiH8l569eGZFlLJWciA%2Flmp%2FoBc0PqiQc8p0OSWnrSEWmyIvp%2Bo5cHEBqxm0zRxKkkxFTXE3LgnAOcbtdBIMkGXOoqa6siNfkQBba4w2WcfjAbyAiZjGJ4Ce9hZDQRoOm2JKQTqY0KtbaTe%2Fq1gXdgnm%2F232qt2Pbo4U0KbFXfFL7cT8J5edQlHCo4JnKDZqhNNKp4mlbRnNt%2BMhoq5DuWCo3rhi3wUKHfPfdE4iXig1E6JvWLR6KKGfNCQBA53wQlm3FwL4MumUKONR5ZNTOHr0HWle1u%2BV6iSeerWXaZ%2BBxoY4COMP6VjL0GOqUBiARkXsXL55zZhjSnuak49VCNp0jI7JDVnffOwi3tUCILZhKD2tNaq76FqCPQ2TtuiQREuD9lZgiYmh83YQgExTZ%2F7HZiOLQebMZbrEH6EOSn7Uci0jqR1BwaM55FzMr0Zj0CNwo02M%2B%2FjMtf2uzNmtz%2BEXLKu5bnayoC9HQczJkOn2bVZpq7p4ukxQ5GihghmI4GBiQn4%2F0HtrWgKRhZS%2BiAwBxJ&X-Amz-Signature=dd05d849db53031c9025d747a8d0dbfb36f92cb6d2fe400a270226b67901146e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JNQBEAF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIBPLrjAzP5ERySc0eOlNYGKQ1bCXvTnsIT6v%2FAvx1XM%2BAiEAtCbjYR58%2FHVi8Xz0z5%2FWgs5aou49evT1K87CQrbEQi0q%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDONffmMfKSL3H3FTXyrcA%2F%2FIBVpZobXaYo7Es7FA7Iqvx7Jo3r5G0ZLxhpW9s0Fdk8fTSi8sZcJ34krvtWyind1tETaukE%2FVpO8NFER5IUf5jygp6u90E%2B51v9MKPhLFuHDucfVjv6u%2FDAptHIdp79jV4aI7NVgk%2FA00O2y1RDcaDhN%2FBZEma8iE5Lax1dTMk%2FC9AlMcMn1QeK8qfyCJHApCjmqyI%2BHWGlLwBg4MyScMCPYkef3harWIxDe7KFDfKH6DNGRHDtVmNUFAii6%2B7V3IHjlqbMlVH8zWjaKZp5tTN67fnYZaYx9DC5qsH1UVtRo2FRpCNH%2FVkveHJW1dK4Jyx8hS56jiH8l569eGZFlLJWciA%2Flmp%2FoBc0PqiQc8p0OSWnrSEWmyIvp%2Bo5cHEBqxm0zRxKkkxFTXE3LgnAOcbtdBIMkGXOoqa6siNfkQBba4w2WcfjAbyAiZjGJ4Ce9hZDQRoOm2JKQTqY0KtbaTe%2Fq1gXdgnm%2F232qt2Pbo4U0KbFXfFL7cT8J5edQlHCo4JnKDZqhNNKp4mlbRnNt%2BMhoq5DuWCo3rhi3wUKHfPfdE4iXig1E6JvWLR6KKGfNCQBA53wQlm3FwL4MumUKONR5ZNTOHr0HWle1u%2BV6iSeerWXaZ%2BBxoY4COMP6VjL0GOqUBiARkXsXL55zZhjSnuak49VCNp0jI7JDVnffOwi3tUCILZhKD2tNaq76FqCPQ2TtuiQREuD9lZgiYmh83YQgExTZ%2F7HZiOLQebMZbrEH6EOSn7Uci0jqR1BwaM55FzMr0Zj0CNwo02M%2B%2FjMtf2uzNmtz%2BEXLKu5bnayoC9HQczJkOn2bVZpq7p4ukxQ5GihghmI4GBiQn4%2F0HtrWgKRhZS%2BiAwBxJ&X-Amz-Signature=48b7f4ef3c45b5218d94c34b322126c492078133835718c6b9e5758af9ca42a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LLI346%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDZ%2FhZV7JmOOu8eZRu7Pt%2BSl1cOdfv0WY3OWoUcK%2FFEKQIgLPtHru78VhKC9MZqYjBVJZpb%2BIltYSuzJI8H91bbFAoq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDCUEuFwYrfxdXn3bhSrcA9X6wDN71eYxXVVowln8pC5WeyJSv0F0PS9VJZKctOUgJEhlVkIGl0x0z8U%2FREZ1yfpy8DhA0SuVnzezImMNNbEQ6fzd0sE6xHnYz%2FZiLuV%2F6TDzI7qKJkiRuBLax2Yezg1n%2BfhP0Ts3aP0gxX40jPbdRCCCOp2RtoEsh5tzQ6s%2Fw1Fk2CrvHYcCXCx8d9GYRh%2Fa0942uNYpLPMD0io8Hc%2BYeHPFTH86Avqdi%2BcQbGYBRxwniP6a5UthtbuEQQ3Q0kjEGT5%2FeqFo7ReAN6xykcejSffn5SkdYxfK3jdFpwSknLOsmiuCbTOgUblToBPC9eOawydCxpS2H04r8k8sjp7Bzw28Fy26fYk1CMf4XwzZoU%2F65aaCvqSlVHGBHouO9ld%2Bh00IE%2BrF1IxUNW8h%2FZJdk2JqLXK3dejsCbG3K6wNbikDt%2BGLXn9rquNFdxxa5wgookC%2BXRslnBf4QqRiyu2BzBpH5ladkC7lblqSRucT8mNWddZsUEYc5eKoFGRUoXC3NnUDXz1jQyx3AOTyw5qIi3OkgHvxQYDWGyHf2MjmlUnYbDZYtgQQw2wdKwMjdLkRVl%2BP%2B0ES7Mt4HZd37mZyBy36XZUEKoeIojGkci8Z30tgPkoDKIad%2BptmMLyWjL0GOqUBLaS%2Fx%2Bmxj1pWnfvmjfOt6x1z0Kub7vBsDrFWN7L6G8VCVZWbWWUOPaHc2274HbIeCYSv9bFSNkgSNwpEyqZ1i5vjlZABUYuzrpeRyO99%2F5YeFa7KIQWaZ7LL1gh4oS52jThsuZ19wEiWxAXZ4Fw9v9jxk0GWRRh9RPZahEXrg81p%2Fi4QInUvxF7FIHmr0%2BjO%2Bls6wGGZsyA%2BIs0hLny4mjyCjeuP&X-Amz-Signature=ad2efe1a2906081d81f926e1040e477b877bdc1abe32b04f7134b6ab6e6a4de0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LLI346%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDZ%2FhZV7JmOOu8eZRu7Pt%2BSl1cOdfv0WY3OWoUcK%2FFEKQIgLPtHru78VhKC9MZqYjBVJZpb%2BIltYSuzJI8H91bbFAoq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDCUEuFwYrfxdXn3bhSrcA9X6wDN71eYxXVVowln8pC5WeyJSv0F0PS9VJZKctOUgJEhlVkIGl0x0z8U%2FREZ1yfpy8DhA0SuVnzezImMNNbEQ6fzd0sE6xHnYz%2FZiLuV%2F6TDzI7qKJkiRuBLax2Yezg1n%2BfhP0Ts3aP0gxX40jPbdRCCCOp2RtoEsh5tzQ6s%2Fw1Fk2CrvHYcCXCx8d9GYRh%2Fa0942uNYpLPMD0io8Hc%2BYeHPFTH86Avqdi%2BcQbGYBRxwniP6a5UthtbuEQQ3Q0kjEGT5%2FeqFo7ReAN6xykcejSffn5SkdYxfK3jdFpwSknLOsmiuCbTOgUblToBPC9eOawydCxpS2H04r8k8sjp7Bzw28Fy26fYk1CMf4XwzZoU%2F65aaCvqSlVHGBHouO9ld%2Bh00IE%2BrF1IxUNW8h%2FZJdk2JqLXK3dejsCbG3K6wNbikDt%2BGLXn9rquNFdxxa5wgookC%2BXRslnBf4QqRiyu2BzBpH5ladkC7lblqSRucT8mNWddZsUEYc5eKoFGRUoXC3NnUDXz1jQyx3AOTyw5qIi3OkgHvxQYDWGyHf2MjmlUnYbDZYtgQQw2wdKwMjdLkRVl%2BP%2B0ES7Mt4HZd37mZyBy36XZUEKoeIojGkci8Z30tgPkoDKIad%2BptmMLyWjL0GOqUBLaS%2Fx%2Bmxj1pWnfvmjfOt6x1z0Kub7vBsDrFWN7L6G8VCVZWbWWUOPaHc2274HbIeCYSv9bFSNkgSNwpEyqZ1i5vjlZABUYuzrpeRyO99%2F5YeFa7KIQWaZ7LL1gh4oS52jThsuZ19wEiWxAXZ4Fw9v9jxk0GWRRh9RPZahEXrg81p%2Fi4QInUvxF7FIHmr0%2BjO%2Bls6wGGZsyA%2BIs0hLny4mjyCjeuP&X-Amz-Signature=51f7aff79d69e766736f8a375a5b5a8638f526414501da7adf4e7708b6eebf15&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LLI346%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDZ%2FhZV7JmOOu8eZRu7Pt%2BSl1cOdfv0WY3OWoUcK%2FFEKQIgLPtHru78VhKC9MZqYjBVJZpb%2BIltYSuzJI8H91bbFAoq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDCUEuFwYrfxdXn3bhSrcA9X6wDN71eYxXVVowln8pC5WeyJSv0F0PS9VJZKctOUgJEhlVkIGl0x0z8U%2FREZ1yfpy8DhA0SuVnzezImMNNbEQ6fzd0sE6xHnYz%2FZiLuV%2F6TDzI7qKJkiRuBLax2Yezg1n%2BfhP0Ts3aP0gxX40jPbdRCCCOp2RtoEsh5tzQ6s%2Fw1Fk2CrvHYcCXCx8d9GYRh%2Fa0942uNYpLPMD0io8Hc%2BYeHPFTH86Avqdi%2BcQbGYBRxwniP6a5UthtbuEQQ3Q0kjEGT5%2FeqFo7ReAN6xykcejSffn5SkdYxfK3jdFpwSknLOsmiuCbTOgUblToBPC9eOawydCxpS2H04r8k8sjp7Bzw28Fy26fYk1CMf4XwzZoU%2F65aaCvqSlVHGBHouO9ld%2Bh00IE%2BrF1IxUNW8h%2FZJdk2JqLXK3dejsCbG3K6wNbikDt%2BGLXn9rquNFdxxa5wgookC%2BXRslnBf4QqRiyu2BzBpH5ladkC7lblqSRucT8mNWddZsUEYc5eKoFGRUoXC3NnUDXz1jQyx3AOTyw5qIi3OkgHvxQYDWGyHf2MjmlUnYbDZYtgQQw2wdKwMjdLkRVl%2BP%2B0ES7Mt4HZd37mZyBy36XZUEKoeIojGkci8Z30tgPkoDKIad%2BptmMLyWjL0GOqUBLaS%2Fx%2Bmxj1pWnfvmjfOt6x1z0Kub7vBsDrFWN7L6G8VCVZWbWWUOPaHc2274HbIeCYSv9bFSNkgSNwpEyqZ1i5vjlZABUYuzrpeRyO99%2F5YeFa7KIQWaZ7LL1gh4oS52jThsuZ19wEiWxAXZ4Fw9v9jxk0GWRRh9RPZahEXrg81p%2Fi4QInUvxF7FIHmr0%2BjO%2Bls6wGGZsyA%2BIs0hLny4mjyCjeuP&X-Amz-Signature=239c00ac2cf3e7884a1bce67be616f309de949a92e45eef9be0a434865397144&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LLI346%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDZ%2FhZV7JmOOu8eZRu7Pt%2BSl1cOdfv0WY3OWoUcK%2FFEKQIgLPtHru78VhKC9MZqYjBVJZpb%2BIltYSuzJI8H91bbFAoq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDCUEuFwYrfxdXn3bhSrcA9X6wDN71eYxXVVowln8pC5WeyJSv0F0PS9VJZKctOUgJEhlVkIGl0x0z8U%2FREZ1yfpy8DhA0SuVnzezImMNNbEQ6fzd0sE6xHnYz%2FZiLuV%2F6TDzI7qKJkiRuBLax2Yezg1n%2BfhP0Ts3aP0gxX40jPbdRCCCOp2RtoEsh5tzQ6s%2Fw1Fk2CrvHYcCXCx8d9GYRh%2Fa0942uNYpLPMD0io8Hc%2BYeHPFTH86Avqdi%2BcQbGYBRxwniP6a5UthtbuEQQ3Q0kjEGT5%2FeqFo7ReAN6xykcejSffn5SkdYxfK3jdFpwSknLOsmiuCbTOgUblToBPC9eOawydCxpS2H04r8k8sjp7Bzw28Fy26fYk1CMf4XwzZoU%2F65aaCvqSlVHGBHouO9ld%2Bh00IE%2BrF1IxUNW8h%2FZJdk2JqLXK3dejsCbG3K6wNbikDt%2BGLXn9rquNFdxxa5wgookC%2BXRslnBf4QqRiyu2BzBpH5ladkC7lblqSRucT8mNWddZsUEYc5eKoFGRUoXC3NnUDXz1jQyx3AOTyw5qIi3OkgHvxQYDWGyHf2MjmlUnYbDZYtgQQw2wdKwMjdLkRVl%2BP%2B0ES7Mt4HZd37mZyBy36XZUEKoeIojGkci8Z30tgPkoDKIad%2BptmMLyWjL0GOqUBLaS%2Fx%2Bmxj1pWnfvmjfOt6x1z0Kub7vBsDrFWN7L6G8VCVZWbWWUOPaHc2274HbIeCYSv9bFSNkgSNwpEyqZ1i5vjlZABUYuzrpeRyO99%2F5YeFa7KIQWaZ7LL1gh4oS52jThsuZ19wEiWxAXZ4Fw9v9jxk0GWRRh9RPZahEXrg81p%2Fi4QInUvxF7FIHmr0%2BjO%2Bls6wGGZsyA%2BIs0hLny4mjyCjeuP&X-Amz-Signature=ffb928be40b6593ad1fffe790948489b9f1603a6b30c6976f6d365677c631005&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LLI346%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDZ%2FhZV7JmOOu8eZRu7Pt%2BSl1cOdfv0WY3OWoUcK%2FFEKQIgLPtHru78VhKC9MZqYjBVJZpb%2BIltYSuzJI8H91bbFAoq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDCUEuFwYrfxdXn3bhSrcA9X6wDN71eYxXVVowln8pC5WeyJSv0F0PS9VJZKctOUgJEhlVkIGl0x0z8U%2FREZ1yfpy8DhA0SuVnzezImMNNbEQ6fzd0sE6xHnYz%2FZiLuV%2F6TDzI7qKJkiRuBLax2Yezg1n%2BfhP0Ts3aP0gxX40jPbdRCCCOp2RtoEsh5tzQ6s%2Fw1Fk2CrvHYcCXCx8d9GYRh%2Fa0942uNYpLPMD0io8Hc%2BYeHPFTH86Avqdi%2BcQbGYBRxwniP6a5UthtbuEQQ3Q0kjEGT5%2FeqFo7ReAN6xykcejSffn5SkdYxfK3jdFpwSknLOsmiuCbTOgUblToBPC9eOawydCxpS2H04r8k8sjp7Bzw28Fy26fYk1CMf4XwzZoU%2F65aaCvqSlVHGBHouO9ld%2Bh00IE%2BrF1IxUNW8h%2FZJdk2JqLXK3dejsCbG3K6wNbikDt%2BGLXn9rquNFdxxa5wgookC%2BXRslnBf4QqRiyu2BzBpH5ladkC7lblqSRucT8mNWddZsUEYc5eKoFGRUoXC3NnUDXz1jQyx3AOTyw5qIi3OkgHvxQYDWGyHf2MjmlUnYbDZYtgQQw2wdKwMjdLkRVl%2BP%2B0ES7Mt4HZd37mZyBy36XZUEKoeIojGkci8Z30tgPkoDKIad%2BptmMLyWjL0GOqUBLaS%2Fx%2Bmxj1pWnfvmjfOt6x1z0Kub7vBsDrFWN7L6G8VCVZWbWWUOPaHc2274HbIeCYSv9bFSNkgSNwpEyqZ1i5vjlZABUYuzrpeRyO99%2F5YeFa7KIQWaZ7LL1gh4oS52jThsuZ19wEiWxAXZ4Fw9v9jxk0GWRRh9RPZahEXrg81p%2Fi4QInUvxF7FIHmr0%2BjO%2Bls6wGGZsyA%2BIs0hLny4mjyCjeuP&X-Amz-Signature=e4b763c16026039e6c9d679d9ce6fd5b2fd3daac659fb5b7db06e0c58232b996&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LLI346%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDZ%2FhZV7JmOOu8eZRu7Pt%2BSl1cOdfv0WY3OWoUcK%2FFEKQIgLPtHru78VhKC9MZqYjBVJZpb%2BIltYSuzJI8H91bbFAoq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDCUEuFwYrfxdXn3bhSrcA9X6wDN71eYxXVVowln8pC5WeyJSv0F0PS9VJZKctOUgJEhlVkIGl0x0z8U%2FREZ1yfpy8DhA0SuVnzezImMNNbEQ6fzd0sE6xHnYz%2FZiLuV%2F6TDzI7qKJkiRuBLax2Yezg1n%2BfhP0Ts3aP0gxX40jPbdRCCCOp2RtoEsh5tzQ6s%2Fw1Fk2CrvHYcCXCx8d9GYRh%2Fa0942uNYpLPMD0io8Hc%2BYeHPFTH86Avqdi%2BcQbGYBRxwniP6a5UthtbuEQQ3Q0kjEGT5%2FeqFo7ReAN6xykcejSffn5SkdYxfK3jdFpwSknLOsmiuCbTOgUblToBPC9eOawydCxpS2H04r8k8sjp7Bzw28Fy26fYk1CMf4XwzZoU%2F65aaCvqSlVHGBHouO9ld%2Bh00IE%2BrF1IxUNW8h%2FZJdk2JqLXK3dejsCbG3K6wNbikDt%2BGLXn9rquNFdxxa5wgookC%2BXRslnBf4QqRiyu2BzBpH5ladkC7lblqSRucT8mNWddZsUEYc5eKoFGRUoXC3NnUDXz1jQyx3AOTyw5qIi3OkgHvxQYDWGyHf2MjmlUnYbDZYtgQQw2wdKwMjdLkRVl%2BP%2B0ES7Mt4HZd37mZyBy36XZUEKoeIojGkci8Z30tgPkoDKIad%2BptmMLyWjL0GOqUBLaS%2Fx%2Bmxj1pWnfvmjfOt6x1z0Kub7vBsDrFWN7L6G8VCVZWbWWUOPaHc2274HbIeCYSv9bFSNkgSNwpEyqZ1i5vjlZABUYuzrpeRyO99%2F5YeFa7KIQWaZ7LL1gh4oS52jThsuZ19wEiWxAXZ4Fw9v9jxk0GWRRh9RPZahEXrg81p%2Fi4QInUvxF7FIHmr0%2BjO%2Bls6wGGZsyA%2BIs0hLny4mjyCjeuP&X-Amz-Signature=7cf55159c6f79945d50940241fd45678d5f57c3164189a2c6748d1f8bdb91f29&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S42WWDWY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQD%2FPE4r6v8FwA6L6fLhqce92fBp9PhFQMBEpNGg8DDqZgIgPvQCl1sG69iffmPEi%2BLERdy6Swd%2FqvxiOaKw9myuwWUq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDNCPCVacDNz7k9dRFCrcA%2BGmfuDf2s9wVQvQRRrKuWj3Eq1esAVhYPdBphm6DqS%2F9dGaT9FLCrzuDdU1OTNFT4QzUfdtgQbk%2BpSd7GOpeY4R3KkRs8n2%2BZQj290ljtwW9mxIDc335T5img1tDKKfD3VL1%2F0K8P3fPHni5Jl3A2D5JpLQ6Vy%2Bf%2FP1jBXgETFH72YmkBHP20trSBi2ZOwmWvDOmD40mFjVdN6knTVisJVep5VFaSIey1uYJ5m7t2f7H0XHEDZVo6g2h1EMdu%2FyIgb%2FF%2FO%2B%2BVt8e6M5ROurOy%2FHJEKCPeRv%2BOmEgcmrcIXPMNQDLkgquCBmI1Ez3%2F1yUonHd7on8qvweGELz1842rtenQpmClNlX6vEihhY%2FNcEs%2FVpeCqnrgT5SOlpnOsrZYVZumZWwkPydDz3eG9PtMedU3RECRRerz6r49r6UHt58B1XLDyX%2F%2FRDIh2gIzIGZc0x%2B%2FjSOtvYZV0dKCMyzdQMO2luINZ%2BRexHrebGrBp4KI1zlPbF6iDnxGFUI6OCrGrU5Q5W2gSSLWuqH%2BgX5HUU1KQr0VRX%2BkvTjMlEQMI9V70pesLWWKFSYibdKOA9DIwPm64retDXcpoEatmpeu69DFqmq4iw88fL37VYcnkhiRu5cKTPoE17j3%2FUMJ6XjL0GOqUBmYU9BVXqvjtCxJMc1mNWbPU5YPumUJ9MKRL7tMkGvcC4DTTAqM%2BiEP9x6KPmqbZWCvqykBVrWP2TKE3T6rVf5lmef05tIGNa16zF626zY9ns0qkkKQy4MzYWQV8GIHM20Rshho%2F69FZsXH1pcnxqPKPat5jzo5K9XSnxRInxhDK8CMnDXpEDR5YBqDG6SsRgkC0%2Fe6HpD8sq9osimiuvMIsaR47J&X-Amz-Signature=24d664291fa527051906214acb211135a031db8f816630e453d43d71a1a2799a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBVXVQJH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIBpOS8DcYbZkQLv094A%2FILsO4mnac0NwnDcq%2BTcWOe4ZAiEAtLVw7ExcLrhNcEDWgSU3nFBT6lnB6Xgeeb%2BeekaWkSYq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDOoN7X3jrLEU%2FSBOmSrcA1pLNBsyRLtjNInWCGpK5yRVpcSck68lC4ZgbXL1OcUw3UgHMPXyoWqNvQu1DbWMVRlLpKGMazvZLVGIkKu%2BzTlx6KNIiBe%2FulOIG2ev2LhEkBC27IUmXCZ6SYsR8ROLtNJzKNMLhGZJPdCZTeqGHgsxQIxTmONZgtCXPHZhNmLZAIvF8xZUp6trxC6G5J98%2BlINUlXYxX%2B0fAZ8nyKO0g8AgPO5Wd%2ByWC28HR1bIWhVFUs4wXULXdvpckAJFNuJBlR%2BhBUZAf7OAE%2Bs2VlRz1TsNKdZz3gkR3PPxzmj2%2BnIR%2FPGoVPHuE09IYCVELTivtTDSPHU4Iqw0ja9eJbYP8%2FDoXAvhyxLkFoqxItO5k1sbgWjuwOaj7UPz8IvGoj6YmDVJhH96WPCjmxAqE1wg5zKNdTBRGUsfFLgctWFpGpOFebmqvZNoAIIsUayPBS80r6Xcrbcy7Qy4PBUOJPKbyYbSPhD6JOAX7EcCVM1VnCvzmI43dDhhIjtnNDtfZpVRWSCh0mgTAK82GJIgfFKsV2eYp4QtvMwk8krFZa6f55LiswfZQ%2BKg00Xv573M1g1n6BU6OPDXHkdSYLj8pijH%2BfU76dgLoLkThP99cvTVpKwDFM0OD7pex%2BMdLBdMLyWjL0GOqUBMqd4%2FbWqHrHoIZNbgdzHHYNqJlXzRcCklfIoKPq85b%2BqtaPEFLMPbyQ1UjuJrjpXkqoQE%2Bk75akpJd1CFk5JVJM9hyrG7YyyZyrQa3RQoQD6FbP8PfFlw9TswLEfTnA%2Btrm0tjA4PO59BNljtCwa5tDQlbYu2%2FVDHa6epQUcMv9uEsSjyLWwPi4K3kv7BpY%2F9TxkiFGUtDyq7wLsRCZ0zECHB%2Fnc&X-Amz-Signature=d259cdc7f3230f798dab9d9658e6be44fc825f024449f89fdc492d433d9e5254&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LLI346%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDZ%2FhZV7JmOOu8eZRu7Pt%2BSl1cOdfv0WY3OWoUcK%2FFEKQIgLPtHru78VhKC9MZqYjBVJZpb%2BIltYSuzJI8H91bbFAoq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDCUEuFwYrfxdXn3bhSrcA9X6wDN71eYxXVVowln8pC5WeyJSv0F0PS9VJZKctOUgJEhlVkIGl0x0z8U%2FREZ1yfpy8DhA0SuVnzezImMNNbEQ6fzd0sE6xHnYz%2FZiLuV%2F6TDzI7qKJkiRuBLax2Yezg1n%2BfhP0Ts3aP0gxX40jPbdRCCCOp2RtoEsh5tzQ6s%2Fw1Fk2CrvHYcCXCx8d9GYRh%2Fa0942uNYpLPMD0io8Hc%2BYeHPFTH86Avqdi%2BcQbGYBRxwniP6a5UthtbuEQQ3Q0kjEGT5%2FeqFo7ReAN6xykcejSffn5SkdYxfK3jdFpwSknLOsmiuCbTOgUblToBPC9eOawydCxpS2H04r8k8sjp7Bzw28Fy26fYk1CMf4XwzZoU%2F65aaCvqSlVHGBHouO9ld%2Bh00IE%2BrF1IxUNW8h%2FZJdk2JqLXK3dejsCbG3K6wNbikDt%2BGLXn9rquNFdxxa5wgookC%2BXRslnBf4QqRiyu2BzBpH5ladkC7lblqSRucT8mNWddZsUEYc5eKoFGRUoXC3NnUDXz1jQyx3AOTyw5qIi3OkgHvxQYDWGyHf2MjmlUnYbDZYtgQQw2wdKwMjdLkRVl%2BP%2B0ES7Mt4HZd37mZyBy36XZUEKoeIojGkci8Z30tgPkoDKIad%2BptmMLyWjL0GOqUBLaS%2Fx%2Bmxj1pWnfvmjfOt6x1z0Kub7vBsDrFWN7L6G8VCVZWbWWUOPaHc2274HbIeCYSv9bFSNkgSNwpEyqZ1i5vjlZABUYuzrpeRyO99%2F5YeFa7KIQWaZ7LL1gh4oS52jThsuZ19wEiWxAXZ4Fw9v9jxk0GWRRh9RPZahEXrg81p%2Fi4QInUvxF7FIHmr0%2BjO%2Bls6wGGZsyA%2BIs0hLny4mjyCjeuP&X-Amz-Signature=6d0eab9d0cd809198105d5b4bab39ce6177e3c6711eebb3d30a12b1ccfd20605&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LLI346%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDZ%2FhZV7JmOOu8eZRu7Pt%2BSl1cOdfv0WY3OWoUcK%2FFEKQIgLPtHru78VhKC9MZqYjBVJZpb%2BIltYSuzJI8H91bbFAoq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDCUEuFwYrfxdXn3bhSrcA9X6wDN71eYxXVVowln8pC5WeyJSv0F0PS9VJZKctOUgJEhlVkIGl0x0z8U%2FREZ1yfpy8DhA0SuVnzezImMNNbEQ6fzd0sE6xHnYz%2FZiLuV%2F6TDzI7qKJkiRuBLax2Yezg1n%2BfhP0Ts3aP0gxX40jPbdRCCCOp2RtoEsh5tzQ6s%2Fw1Fk2CrvHYcCXCx8d9GYRh%2Fa0942uNYpLPMD0io8Hc%2BYeHPFTH86Avqdi%2BcQbGYBRxwniP6a5UthtbuEQQ3Q0kjEGT5%2FeqFo7ReAN6xykcejSffn5SkdYxfK3jdFpwSknLOsmiuCbTOgUblToBPC9eOawydCxpS2H04r8k8sjp7Bzw28Fy26fYk1CMf4XwzZoU%2F65aaCvqSlVHGBHouO9ld%2Bh00IE%2BrF1IxUNW8h%2FZJdk2JqLXK3dejsCbG3K6wNbikDt%2BGLXn9rquNFdxxa5wgookC%2BXRslnBf4QqRiyu2BzBpH5ladkC7lblqSRucT8mNWddZsUEYc5eKoFGRUoXC3NnUDXz1jQyx3AOTyw5qIi3OkgHvxQYDWGyHf2MjmlUnYbDZYtgQQw2wdKwMjdLkRVl%2BP%2B0ES7Mt4HZd37mZyBy36XZUEKoeIojGkci8Z30tgPkoDKIad%2BptmMLyWjL0GOqUBLaS%2Fx%2Bmxj1pWnfvmjfOt6x1z0Kub7vBsDrFWN7L6G8VCVZWbWWUOPaHc2274HbIeCYSv9bFSNkgSNwpEyqZ1i5vjlZABUYuzrpeRyO99%2F5YeFa7KIQWaZ7LL1gh4oS52jThsuZ19wEiWxAXZ4Fw9v9jxk0GWRRh9RPZahEXrg81p%2Fi4QInUvxF7FIHmr0%2BjO%2Bls6wGGZsyA%2BIs0hLny4mjyCjeuP&X-Amz-Signature=a19b4d79799f88eee0264edf11d46d0df6f483903765bd783b4d8def51fc68a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LLI346%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDZ%2FhZV7JmOOu8eZRu7Pt%2BSl1cOdfv0WY3OWoUcK%2FFEKQIgLPtHru78VhKC9MZqYjBVJZpb%2BIltYSuzJI8H91bbFAoq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDCUEuFwYrfxdXn3bhSrcA9X6wDN71eYxXVVowln8pC5WeyJSv0F0PS9VJZKctOUgJEhlVkIGl0x0z8U%2FREZ1yfpy8DhA0SuVnzezImMNNbEQ6fzd0sE6xHnYz%2FZiLuV%2F6TDzI7qKJkiRuBLax2Yezg1n%2BfhP0Ts3aP0gxX40jPbdRCCCOp2RtoEsh5tzQ6s%2Fw1Fk2CrvHYcCXCx8d9GYRh%2Fa0942uNYpLPMD0io8Hc%2BYeHPFTH86Avqdi%2BcQbGYBRxwniP6a5UthtbuEQQ3Q0kjEGT5%2FeqFo7ReAN6xykcejSffn5SkdYxfK3jdFpwSknLOsmiuCbTOgUblToBPC9eOawydCxpS2H04r8k8sjp7Bzw28Fy26fYk1CMf4XwzZoU%2F65aaCvqSlVHGBHouO9ld%2Bh00IE%2BrF1IxUNW8h%2FZJdk2JqLXK3dejsCbG3K6wNbikDt%2BGLXn9rquNFdxxa5wgookC%2BXRslnBf4QqRiyu2BzBpH5ladkC7lblqSRucT8mNWddZsUEYc5eKoFGRUoXC3NnUDXz1jQyx3AOTyw5qIi3OkgHvxQYDWGyHf2MjmlUnYbDZYtgQQw2wdKwMjdLkRVl%2BP%2B0ES7Mt4HZd37mZyBy36XZUEKoeIojGkci8Z30tgPkoDKIad%2BptmMLyWjL0GOqUBLaS%2Fx%2Bmxj1pWnfvmjfOt6x1z0Kub7vBsDrFWN7L6G8VCVZWbWWUOPaHc2274HbIeCYSv9bFSNkgSNwpEyqZ1i5vjlZABUYuzrpeRyO99%2F5YeFa7KIQWaZ7LL1gh4oS52jThsuZ19wEiWxAXZ4Fw9v9jxk0GWRRh9RPZahEXrg81p%2Fi4QInUvxF7FIHmr0%2BjO%2Bls6wGGZsyA%2BIs0hLny4mjyCjeuP&X-Amz-Signature=46bbab048cfdde85aed38d15759809760fa03ea9a8e01c9a6eb68b0a9669b3bc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7K6UBWC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDG3Q3qeQjurbH4kx%2BGuMQ5J0CcouexRberjyhDDkAxcwIhAIoyt0huRQD3iBTOb%2BNgkCDdMxGMtyzsGtcbHbv%2FfH56Kv8DCEAQABoMNjM3NDIzMTgzODA1IgyS7yyNeM0WrZmo7%2B4q3AM8BFV3NYBg%2B6eNXMO%2F%2BTN7uEikma1FppT%2Fsr4u%2Bx5pHaOz46J%2FO3jfxmEmnzfTorrDNjy1kOZhCRWc2fn24cxUZDjT39p4aT7g%2FcLmd4shzXVhJWXQs7sm5S0EaqfibpfrCQ%2FjX6My083T8mXUGPHyMnd8Qz1gkVM0M4vwS6Le394pc%2BGN6snZhSwr7%2BnKdaphNGK9aeOz8Dq%2F67uUoVGUD%2BBPngwVoz7kLld%2B4XSnbAXezhs8ohBjS33QEp%2Bc8z0G26Dz7KpHy14ymnkfKsdLN1a55taBqh6Zl3Iz%2FciU0UjX7hiK5MjHZBMcNox8fTJ8B8ns1KRGouR6UdsBMFy%2BC81G2a%2BX6k6NOyMbmlTPaP2cvJTEa6UcypcRnHqt5lKzM3FS9F4qbnWj%2BJfJphoBK4WckCl7uDJiP3nI7DCB109O%2B8OlKVQnHKlBu3z9gvL0nQAhEW%2BwIl2kielmf1%2BIaOdw3z4CZ1CR6eflw46FZZeJuSN7%2FLmUM6GTAcRNNdltLGT6NhyCwb3kLYouhYboxdn22Bt1SjvhVxOIu%2FapWkQCvtcHkzM0o9wKCwkinLpYSeiZobzEKyMTKkTO1b6mTaEZ8Xbs1I2Ja132N8dQLdPwjdGoWavuGLAXjDDMlYy9BjqkAWg33q0dOQIe7ClUFgGPTp8%2BdjpU7waT3rs%2BSCHU5wM7wxIXwwk6K0WxwURnRCpZMOAaT8TeOBKKDM%2BetJwMX0R4wlUGFnLGCjqCmUEewfsTFFypmBfKG8Od38oo9L1RSYCJn1wqWsml0yNkn7XewTbJyiAXdSWmUYhXe1yZewBpmdJXnH5RfohaGd1X99exvCG8We3ESS63zIiBIJO3RkM%2FzfAP&X-Amz-Signature=50635f2397e2660e88affbbfa71bf6cb8bb7c5e789449489dda12793ed4ff0eb&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQPN4ETY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCID%2Ft%2B%2FAmXj62H3MRybDFq3e58J6kzpyIgph%2FsFz62IemAiAHnUOZP%2FJKwEGJ0DJjoC1L65A17IJIICI6QfPk547upCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMpm8f9Nw4h9AiUZKlKtwDB%2BA027n6e6oqEKVLSrdmjpZzukJJwP0V5UlYhi3LRKPCSJv2nzYNR%2BcNIHpplvP2wUW2iodMzD3M4Zl78GFULri6%2FMcXFjipLT0VWK1ktZvYaP2Wb7fjGIkR4gWKOWFsfANQ46Lur7LRfLNBhaZHQqSREuQl0GnYAHQ%2BSPENMJjJwcyPbZBnjddv43Y%2BPkNkWpDEAcz5MxTp1eCwVaW3lJcM3nSG8o7M1Cs0nKPhR8KMpdoL0YYZcNyf7T9MbNzVrMZAkigIy3hRQ9YJl6%2FRTdd%2BTCF9B6VgEI48nFgHx%2FH4efsgoB%2FZ%2B0heYZzPKS52U7WzlRetjbXcnHsmHDZCtxDPoU6k%2B9CZ0p10avb6gqjkHQMo92NL%2Bnux7tX4sgH9%2Bw4MtCsgefdXHF7Mf1JcRIQzgMoWRn7hfn4x6NbQgT78K9rKUEwpMTwG10Ounb6I7RDxVoG8Pddu1lPfOl36s0OTuXBAyuxqIn1Oe%2F2v1akAeOHbTuG%2FrvhGz9Si%2F11ul8Z04ORE415f2BbC9VIbt1REYOjY0jFH03X4Rpwfk8%2FdhOyBslgNMCvvLPj%2BCYHTiq5rUda0e8PT7yiMh29cB%2Fbf0GnXLXgfsMvXpKhxHqatrMQ2go8IyWWrxXEw4JWMvQY6pgFeMUaz03%2FGNJnn3SjfWwj%2FM4my0TunlLSBS4487Ot36s2OPnEmPdI0Ylg1nIa5SyQbG5KGQf9y2Wlp2yOG%2BAGBZ8Gpba1nVnWfvEFX2TJZo%2FYOe%2FuMCwnZ6lEeslRPIGG25HiuMT0bY%2Fm%2BNYkOHV1VXnXj30HXTMfE62s6Z4hhM08aea%2FcMsAyeBvMTKc%2B%2BqtXV8qtn7kvbYwebOGenqv8eYzpNPzg&X-Amz-Signature=d9df469220515e4fe4d58ea959bee811934ca2f9ceb97b61e081acc9db3badb1&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAKGF7M7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIHjFaZ4w4ms3xWy%2FMxaFBXgOmdhnwknTMZY20kxeotTQAiBLs6brb8cFHMvlv5bWnlsH7gB9p0NwIbF9mrlWGHqibir%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMaPZTwRm2fplelcz0KtwDiVh1ATwxvi7rXT4PTipVoYuhM3RkHA82r1OtrNNXsumbs23AIRX5DUJQ0rHpH1RAhptAWUw2t3Xs3qCzw5wDsKfmIVpVDJqqudnq3huPPTj%2FaZK%2BsnJUHrzsv5y%2BgB005d3QyofVhLktMCkFaXv2yrg8fJVul32p6nXijO6B88h4veiRsIWR7BzNybjTeVc661vNED5lZMuJf9zm4K0%2FMp2w2DRmK%2BR73bqcMg90WKEMaC7G%2Fuh95CHZIbhIeDYnv4lfTn2Y4CSkI5oQkhzFearuaDvidgedwMesx5alXl9XZZrCUSBX8KlLPXuWJesM%2B%2FoTG%2FE%2FAXOtnLy0%2BWqQRkTAbpPZJtlkOcGOiJPFaDdCU9Vq2%2B9CiHAXMircxZcGUhLSKbARmz4vEYzp6AuBVjqFEKfRRVioh%2BhGcCrND1lQ1R%2FeSCFR5BMe4hmTJc%2BJVp1S2I17Bl60o%2B835hWGTaSmi3iEAJmW3Sk7G%2F8E2B6e448lelUw0gc4dY6QzC0otYAkVzuR9S44J8X40ojovyDd9Z8kxO9AIH6MSMmuH6zTkkGWo0HF54i8vaP8zM3ul5%2BAMux5NJUN1z23c257SNDbd0u4m%2BVR0fPhBXIdZLCeIOxP6hDSvNwnSEAwsJaMvQY6pgE8%2Bbm%2BGTZwFvlP81iVnnmUy45Vnenjo2NWZyjRcJmE%2By3TjzBm8IfNYwMQxfvcnZCddY6zZHFrtmtnXsA2GnF2Hj7PnQldaXrmi4FJHCpA7tvwDucrk%2FI5lkWB%2FSsti2UCSA2vLCvsVNW8K8zjIW1%2FEGFNdWO2pxZKHTQgqZbBA2XHjzyQNSnKf8vgkQfr0anKnqceQTevocsviK2RhAGZqKOzVbQH&X-Amz-Signature=94da78dd7e9dd7742c1fb985757daa565ca4e2f0df6cf29ff46181b4ad850bde&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JOK6V4W%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIDykgJEMQJFwx2YZi%2F6bqlK92z2S1p6B4VqCv2pXDaQMAiEAiT57Pd6fiVgpwXv6n%2FTUYLhF7lj2IuryOAR3R6%2F%2FJrsq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDJVS9JAyWL9sdZDVBSrcAz17axENVJOgwShHo4huNe8xA%2BD%2B%2BX6E%2FYFmyCjnIzavwa1GIP3JD6d%2FMXJORu%2B06FJHWjzPr9tcSlI4o7T0eynnEL2ljMlRWSJRX3yZaTUsHIMfzGlvLSw4fpiq3CIrSlVobw8pvQKaBq2p0RDp1Y%2BlGlccw5pFjxVmYoC0QUmrzx8rMEZuC9Djo8bNFrnm2C8iQNS1D35pP4QkSv857B4x1C0n%2Btm1KID8%2B2kIfABB4J1WqtWrqAJXAgu1kpnhwkDl%2Fn6yknFS4qWudxlRo56zSI3VmJJXAIDGkUlXiX8OGOqOm%2BrUZHWWXiu9mJnqwxSjH8Er4sF3NehWhz%2FrDwyg8wQA41URb2I%2FaaFeK5743hODWAHgopa06aA3ZkOo1sY9ydjGKZL%2BTklv2ljZgJeAr8GYo2zNTxG4aDqT3k1Xop4Ji8AW31oWl6OF%2F5drHP6GNuMsH1Dfxcq9sgOJz7XYdC3GOzpULY%2FxLySJe3zOmfsIFwGHFJfxnnYVc3iWk8vhYjEN0YrWY1AW3Zi2uifod0wHGrvC6We%2FcCfsN3QKdarnmghHnKUBmD7Jx9yHct2WN0Is6dJlZB9tp%2FOfEVhWR3I8FVTAa1rqVMzo3sUPv4Tl3KmyztVHIMkRMJ6WjL0GOqUB%2FnTr3hWUU9w0rcOwKWjcvSdhZKu5bnrneCJ8BX80jWmRiO%2F87ONngUwF8G42kBjXcWa04vTkmEa8uQlQ4Ji9FdiSYpvkyDwsEykUgFRQRT1rQvNJjLnqZtuTZJPrZxSsMVv0tfqQYVLl%2FU0%2BXZie96bQb8EF9Yl5l2jHd2LVKPIPSiZfEKP4E%2Bt0SJBX4xmqUxp1VJooUy%2FE1N4OibjTbSX%2BNvZ6&X-Amz-Signature=b4ed6f3b4d5d1ca007a11f1ae172d6d1e18eaa09bc91bb48d66fe84e1a354abe&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JOK6V4W%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIDykgJEMQJFwx2YZi%2F6bqlK92z2S1p6B4VqCv2pXDaQMAiEAiT57Pd6fiVgpwXv6n%2FTUYLhF7lj2IuryOAR3R6%2F%2FJrsq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDJVS9JAyWL9sdZDVBSrcAz17axENVJOgwShHo4huNe8xA%2BD%2B%2BX6E%2FYFmyCjnIzavwa1GIP3JD6d%2FMXJORu%2B06FJHWjzPr9tcSlI4o7T0eynnEL2ljMlRWSJRX3yZaTUsHIMfzGlvLSw4fpiq3CIrSlVobw8pvQKaBq2p0RDp1Y%2BlGlccw5pFjxVmYoC0QUmrzx8rMEZuC9Djo8bNFrnm2C8iQNS1D35pP4QkSv857B4x1C0n%2Btm1KID8%2B2kIfABB4J1WqtWrqAJXAgu1kpnhwkDl%2Fn6yknFS4qWudxlRo56zSI3VmJJXAIDGkUlXiX8OGOqOm%2BrUZHWWXiu9mJnqwxSjH8Er4sF3NehWhz%2FrDwyg8wQA41URb2I%2FaaFeK5743hODWAHgopa06aA3ZkOo1sY9ydjGKZL%2BTklv2ljZgJeAr8GYo2zNTxG4aDqT3k1Xop4Ji8AW31oWl6OF%2F5drHP6GNuMsH1Dfxcq9sgOJz7XYdC3GOzpULY%2FxLySJe3zOmfsIFwGHFJfxnnYVc3iWk8vhYjEN0YrWY1AW3Zi2uifod0wHGrvC6We%2FcCfsN3QKdarnmghHnKUBmD7Jx9yHct2WN0Is6dJlZB9tp%2FOfEVhWR3I8FVTAa1rqVMzo3sUPv4Tl3KmyztVHIMkRMJ6WjL0GOqUB%2FnTr3hWUU9w0rcOwKWjcvSdhZKu5bnrneCJ8BX80jWmRiO%2F87ONngUwF8G42kBjXcWa04vTkmEa8uQlQ4Ji9FdiSYpvkyDwsEykUgFRQRT1rQvNJjLnqZtuTZJPrZxSsMVv0tfqQYVLl%2FU0%2BXZie96bQb8EF9Yl5l2jHd2LVKPIPSiZfEKP4E%2Bt0SJBX4xmqUxp1VJooUy%2FE1N4OibjTbSX%2BNvZ6&X-Amz-Signature=5ae03cb7e731f84900a1364e33182b2b3e564064f7505d84927d90e88d70bab6&X-Amz-SignedHeaders=host&x-id=GetObject)

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
