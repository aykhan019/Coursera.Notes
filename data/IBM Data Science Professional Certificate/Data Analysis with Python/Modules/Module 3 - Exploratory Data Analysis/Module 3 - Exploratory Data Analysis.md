

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDBYMII5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDODkLjolWSXAfV8F05Os6unTOBB8TPfdQRhtjKOCHpqwIhANS5dwi6ONC2K1P5TqHJ47ABw5PPIxmdXjIp1byc8NLOKv8DCCAQABoMNjM3NDIzMTgzODA1IgzIm7aNSPgJMqbwaCkq3AOFO%2B6M8L2XTT3Wa5yyfOMNZl%2BQTewpKhRLTi6XQC76CE5ac%2FHHCJFz5zSji0jL%2BSECZLATCU7UKJiNxM2ef8YRCnpV5RyrA4W19ufeWm2%2BR%2F8DDwhuYur3OgAJnbAbhd0XxKR%2BVAzX%2FZSfy3x0v1qGcsD%2BN%2BiE%2BPw7toH60cSNUp%2FQJu1pPdvSp9auKx5xvwXFhj2sX6YBPM1IKGVOwVCtr0PPAQ5w9CTpSjDFapnQQgMZVK3QPdtJNftYODCgWAOU1QKj340FzQxt8AzbrwSjkYPz4%2BFvFyw5JzA7qnyOrS5tHk9n3Gh5swPIgfEyX3dDLumq9%2F5KZpdJDrIVrTlmvf6hZBqpYI%2FGGwl67BNmw%2FM%2BM5D4i7hHVoeK3if4uY5ATnwxrS%2BuSIr%2Fqn4cXvmwLcJkGn1vxzcpx6wYHbQ35c5n78oWTE5%2B6iCPoPhzp2GpcFauC0PQJssEXLCGXLt7XmXidmqgMHxX3ZVy6vSQwAzBfNGsU%2Fcc5ToEbWSjDUbzs2xxltVVfhUWcjlziIGrW3%2FREsmG68u0VderU9APnbypXKa7e9E5SuUxhVnLhFyuHjWWxXBtzCQih6YDu1JMsLhVaSTxn1OogHVPjkKINI2AhIbsEIG1yVr4wzDHlIW9BjqkATD2zeMJX1yA5GukOW1qEjAQ5GqIDuznQXwDH3OhlypC7jHpaTDjDeRiBrEGkRCuNj1J04gUn7bC71F%2Fffj9SmZlnVaGNgiPUTjUlXAWpGmc8I1mJUh24Bg7XD7omOlLqpXPKmSeA%2FR%2FwoG1y09KFGwxGbyy0wzSimrgA3ke4qFl7mZTmfIQEfkEa%2BHcZmNUrq%2BaI0s9dCsgzd8TUH0xpG4PKl9W&X-Amz-Signature=8c5b89186de2cc60532f585ae319fb8f1841f919dc7197813ceda92b8b1bd869&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDBYMII5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDODkLjolWSXAfV8F05Os6unTOBB8TPfdQRhtjKOCHpqwIhANS5dwi6ONC2K1P5TqHJ47ABw5PPIxmdXjIp1byc8NLOKv8DCCAQABoMNjM3NDIzMTgzODA1IgzIm7aNSPgJMqbwaCkq3AOFO%2B6M8L2XTT3Wa5yyfOMNZl%2BQTewpKhRLTi6XQC76CE5ac%2FHHCJFz5zSji0jL%2BSECZLATCU7UKJiNxM2ef8YRCnpV5RyrA4W19ufeWm2%2BR%2F8DDwhuYur3OgAJnbAbhd0XxKR%2BVAzX%2FZSfy3x0v1qGcsD%2BN%2BiE%2BPw7toH60cSNUp%2FQJu1pPdvSp9auKx5xvwXFhj2sX6YBPM1IKGVOwVCtr0PPAQ5w9CTpSjDFapnQQgMZVK3QPdtJNftYODCgWAOU1QKj340FzQxt8AzbrwSjkYPz4%2BFvFyw5JzA7qnyOrS5tHk9n3Gh5swPIgfEyX3dDLumq9%2F5KZpdJDrIVrTlmvf6hZBqpYI%2FGGwl67BNmw%2FM%2BM5D4i7hHVoeK3if4uY5ATnwxrS%2BuSIr%2Fqn4cXvmwLcJkGn1vxzcpx6wYHbQ35c5n78oWTE5%2B6iCPoPhzp2GpcFauC0PQJssEXLCGXLt7XmXidmqgMHxX3ZVy6vSQwAzBfNGsU%2Fcc5ToEbWSjDUbzs2xxltVVfhUWcjlziIGrW3%2FREsmG68u0VderU9APnbypXKa7e9E5SuUxhVnLhFyuHjWWxXBtzCQih6YDu1JMsLhVaSTxn1OogHVPjkKINI2AhIbsEIG1yVr4wzDHlIW9BjqkATD2zeMJX1yA5GukOW1qEjAQ5GqIDuznQXwDH3OhlypC7jHpaTDjDeRiBrEGkRCuNj1J04gUn7bC71F%2Fffj9SmZlnVaGNgiPUTjUlXAWpGmc8I1mJUh24Bg7XD7omOlLqpXPKmSeA%2FR%2FwoG1y09KFGwxGbyy0wzSimrgA3ke4qFl7mZTmfIQEfkEa%2BHcZmNUrq%2BaI0s9dCsgzd8TUH0xpG4PKl9W&X-Amz-Signature=96060e5ca829b866c54054effb21595ab05ccc6891d845eb3190a3cd68c16ffa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDBYMII5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDODkLjolWSXAfV8F05Os6unTOBB8TPfdQRhtjKOCHpqwIhANS5dwi6ONC2K1P5TqHJ47ABw5PPIxmdXjIp1byc8NLOKv8DCCAQABoMNjM3NDIzMTgzODA1IgzIm7aNSPgJMqbwaCkq3AOFO%2B6M8L2XTT3Wa5yyfOMNZl%2BQTewpKhRLTi6XQC76CE5ac%2FHHCJFz5zSji0jL%2BSECZLATCU7UKJiNxM2ef8YRCnpV5RyrA4W19ufeWm2%2BR%2F8DDwhuYur3OgAJnbAbhd0XxKR%2BVAzX%2FZSfy3x0v1qGcsD%2BN%2BiE%2BPw7toH60cSNUp%2FQJu1pPdvSp9auKx5xvwXFhj2sX6YBPM1IKGVOwVCtr0PPAQ5w9CTpSjDFapnQQgMZVK3QPdtJNftYODCgWAOU1QKj340FzQxt8AzbrwSjkYPz4%2BFvFyw5JzA7qnyOrS5tHk9n3Gh5swPIgfEyX3dDLumq9%2F5KZpdJDrIVrTlmvf6hZBqpYI%2FGGwl67BNmw%2FM%2BM5D4i7hHVoeK3if4uY5ATnwxrS%2BuSIr%2Fqn4cXvmwLcJkGn1vxzcpx6wYHbQ35c5n78oWTE5%2B6iCPoPhzp2GpcFauC0PQJssEXLCGXLt7XmXidmqgMHxX3ZVy6vSQwAzBfNGsU%2Fcc5ToEbWSjDUbzs2xxltVVfhUWcjlziIGrW3%2FREsmG68u0VderU9APnbypXKa7e9E5SuUxhVnLhFyuHjWWxXBtzCQih6YDu1JMsLhVaSTxn1OogHVPjkKINI2AhIbsEIG1yVr4wzDHlIW9BjqkATD2zeMJX1yA5GukOW1qEjAQ5GqIDuznQXwDH3OhlypC7jHpaTDjDeRiBrEGkRCuNj1J04gUn7bC71F%2Fffj9SmZlnVaGNgiPUTjUlXAWpGmc8I1mJUh24Bg7XD7omOlLqpXPKmSeA%2FR%2FwoG1y09KFGwxGbyy0wzSimrgA3ke4qFl7mZTmfIQEfkEa%2BHcZmNUrq%2BaI0s9dCsgzd8TUH0xpG4PKl9W&X-Amz-Signature=063a127f4af01c6d8058e481a9cf4fe8970269bea41f2c95e7769fa7d782e639&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FMIDT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHNzsQKKTvkVOgOd2TUEvqd9qJ5qlO4wdaB7KyVHBi2%2FAiEA%2B4zTnrm4M9aj%2BPHD2H3spq4Y1jGj9CFPhZSGWvuPap0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJha%2FSC%2Fg6garbfIiircA7vQNKiWhsXF8udEsGUb6Zh0J44gQOxz4ac25R%2Bk98k0LyQTA3MzSiMZu89h198aIGk6x7YGCN09TZUd9srvSNWI7EJjgvAMU5u1W%2FCIgludrEPdyhaHqn0bvr8JaDjZNwbP5%2FUjmUaLnMZVON1%2Bo%2BLedJ0o%2BDqJqvxwW2L5dB7ljoQl9s7QartvAGr1%2FI7CHniTkPYzoAytzMYV3RzcUQE32RZV4O%2BoajAzMdyNtVxuI%2FI2WAyiTs%2BSmdrUBVONY5hJ3h9sYI1%2Fch0G8anV7t2hR0wvHUZp0Ddj0IqUKL8sVSdajdbaLQMq5RNG1RJ4Xcgo0cmdtgSlsWWo%2FCZXNju9rh6lIBVu9uKdod4tK03hCKP3xQK4%2Fvyji6WvYE4h6Bw3H0Qdzt1Y0yd4%2Bgv8mNR49Xkj%2BAjFyZyk5P0MsvQ5adhmZBQWsXk4NmbFGNo51jPz6MYKloUmhNY0ZqBtmdUTCaeHbJBLiXbSSrRAGe4HSXNs2omSoW2vsPISYwSGFR32X%2F1cDhPDFt0BopXzp4ZUWh7a6U5jufLGRZtpR%2FWAhfhREtPSmsdy8B2fWQ9joRObb%2Fu6MO677hcT7PKPxJ%2FECycBv9r%2FpBZs%2F0GXBqYdfamJw2Xupo5FMC4mMMaUhb0GOqUBQ1w93x%2FPM4mGt5wchKD0GgyAb1Ord1sJB0yLZ%2BXQ%2BnCSwVUF4vb6246Dpz75m9oq9smA4Qqu0MMbORmBrh299mM9RfjaZl8crjo5ZZ%2BUO4SVBpzh7bvNaJe%2F3NHAHP3Qu06zk%2BW2Z2LhUyyKOa4%2BbBqY7xGHu63NpCNGAcKC3ujPeN8ybnzxLDosnlOZwXEhV5MljuQSVrwvzePS15A9A11VN3YD&X-Amz-Signature=8983ec12b923fe8fea91cf6ce2124a044719414aa942ffe8458904efe743286e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FMIDT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHNzsQKKTvkVOgOd2TUEvqd9qJ5qlO4wdaB7KyVHBi2%2FAiEA%2B4zTnrm4M9aj%2BPHD2H3spq4Y1jGj9CFPhZSGWvuPap0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJha%2FSC%2Fg6garbfIiircA7vQNKiWhsXF8udEsGUb6Zh0J44gQOxz4ac25R%2Bk98k0LyQTA3MzSiMZu89h198aIGk6x7YGCN09TZUd9srvSNWI7EJjgvAMU5u1W%2FCIgludrEPdyhaHqn0bvr8JaDjZNwbP5%2FUjmUaLnMZVON1%2Bo%2BLedJ0o%2BDqJqvxwW2L5dB7ljoQl9s7QartvAGr1%2FI7CHniTkPYzoAytzMYV3RzcUQE32RZV4O%2BoajAzMdyNtVxuI%2FI2WAyiTs%2BSmdrUBVONY5hJ3h9sYI1%2Fch0G8anV7t2hR0wvHUZp0Ddj0IqUKL8sVSdajdbaLQMq5RNG1RJ4Xcgo0cmdtgSlsWWo%2FCZXNju9rh6lIBVu9uKdod4tK03hCKP3xQK4%2Fvyji6WvYE4h6Bw3H0Qdzt1Y0yd4%2Bgv8mNR49Xkj%2BAjFyZyk5P0MsvQ5adhmZBQWsXk4NmbFGNo51jPz6MYKloUmhNY0ZqBtmdUTCaeHbJBLiXbSSrRAGe4HSXNs2omSoW2vsPISYwSGFR32X%2F1cDhPDFt0BopXzp4ZUWh7a6U5jufLGRZtpR%2FWAhfhREtPSmsdy8B2fWQ9joRObb%2Fu6MO677hcT7PKPxJ%2FECycBv9r%2FpBZs%2F0GXBqYdfamJw2Xupo5FMC4mMMaUhb0GOqUBQ1w93x%2FPM4mGt5wchKD0GgyAb1Ord1sJB0yLZ%2BXQ%2BnCSwVUF4vb6246Dpz75m9oq9smA4Qqu0MMbORmBrh299mM9RfjaZl8crjo5ZZ%2BUO4SVBpzh7bvNaJe%2F3NHAHP3Qu06zk%2BW2Z2LhUyyKOa4%2BbBqY7xGHu63NpCNGAcKC3ujPeN8ybnzxLDosnlOZwXEhV5MljuQSVrwvzePS15A9A11VN3YD&X-Amz-Signature=91d700de9d3245c2f506b9326d27cfa82478b30e539c0c3ddebbce29dab547ae&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FMIDT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHNzsQKKTvkVOgOd2TUEvqd9qJ5qlO4wdaB7KyVHBi2%2FAiEA%2B4zTnrm4M9aj%2BPHD2H3spq4Y1jGj9CFPhZSGWvuPap0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJha%2FSC%2Fg6garbfIiircA7vQNKiWhsXF8udEsGUb6Zh0J44gQOxz4ac25R%2Bk98k0LyQTA3MzSiMZu89h198aIGk6x7YGCN09TZUd9srvSNWI7EJjgvAMU5u1W%2FCIgludrEPdyhaHqn0bvr8JaDjZNwbP5%2FUjmUaLnMZVON1%2Bo%2BLedJ0o%2BDqJqvxwW2L5dB7ljoQl9s7QartvAGr1%2FI7CHniTkPYzoAytzMYV3RzcUQE32RZV4O%2BoajAzMdyNtVxuI%2FI2WAyiTs%2BSmdrUBVONY5hJ3h9sYI1%2Fch0G8anV7t2hR0wvHUZp0Ddj0IqUKL8sVSdajdbaLQMq5RNG1RJ4Xcgo0cmdtgSlsWWo%2FCZXNju9rh6lIBVu9uKdod4tK03hCKP3xQK4%2Fvyji6WvYE4h6Bw3H0Qdzt1Y0yd4%2Bgv8mNR49Xkj%2BAjFyZyk5P0MsvQ5adhmZBQWsXk4NmbFGNo51jPz6MYKloUmhNY0ZqBtmdUTCaeHbJBLiXbSSrRAGe4HSXNs2omSoW2vsPISYwSGFR32X%2F1cDhPDFt0BopXzp4ZUWh7a6U5jufLGRZtpR%2FWAhfhREtPSmsdy8B2fWQ9joRObb%2Fu6MO677hcT7PKPxJ%2FECycBv9r%2FpBZs%2F0GXBqYdfamJw2Xupo5FMC4mMMaUhb0GOqUBQ1w93x%2FPM4mGt5wchKD0GgyAb1Ord1sJB0yLZ%2BXQ%2BnCSwVUF4vb6246Dpz75m9oq9smA4Qqu0MMbORmBrh299mM9RfjaZl8crjo5ZZ%2BUO4SVBpzh7bvNaJe%2F3NHAHP3Qu06zk%2BW2Z2LhUyyKOa4%2BbBqY7xGHu63NpCNGAcKC3ujPeN8ybnzxLDosnlOZwXEhV5MljuQSVrwvzePS15A9A11VN3YD&X-Amz-Signature=f66d5287a19144a7ec331a99f6cb8ff549c4c8a07b19a92be00d1252707e8707&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FMIDT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHNzsQKKTvkVOgOd2TUEvqd9qJ5qlO4wdaB7KyVHBi2%2FAiEA%2B4zTnrm4M9aj%2BPHD2H3spq4Y1jGj9CFPhZSGWvuPap0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJha%2FSC%2Fg6garbfIiircA7vQNKiWhsXF8udEsGUb6Zh0J44gQOxz4ac25R%2Bk98k0LyQTA3MzSiMZu89h198aIGk6x7YGCN09TZUd9srvSNWI7EJjgvAMU5u1W%2FCIgludrEPdyhaHqn0bvr8JaDjZNwbP5%2FUjmUaLnMZVON1%2Bo%2BLedJ0o%2BDqJqvxwW2L5dB7ljoQl9s7QartvAGr1%2FI7CHniTkPYzoAytzMYV3RzcUQE32RZV4O%2BoajAzMdyNtVxuI%2FI2WAyiTs%2BSmdrUBVONY5hJ3h9sYI1%2Fch0G8anV7t2hR0wvHUZp0Ddj0IqUKL8sVSdajdbaLQMq5RNG1RJ4Xcgo0cmdtgSlsWWo%2FCZXNju9rh6lIBVu9uKdod4tK03hCKP3xQK4%2Fvyji6WvYE4h6Bw3H0Qdzt1Y0yd4%2Bgv8mNR49Xkj%2BAjFyZyk5P0MsvQ5adhmZBQWsXk4NmbFGNo51jPz6MYKloUmhNY0ZqBtmdUTCaeHbJBLiXbSSrRAGe4HSXNs2omSoW2vsPISYwSGFR32X%2F1cDhPDFt0BopXzp4ZUWh7a6U5jufLGRZtpR%2FWAhfhREtPSmsdy8B2fWQ9joRObb%2Fu6MO677hcT7PKPxJ%2FECycBv9r%2FpBZs%2F0GXBqYdfamJw2Xupo5FMC4mMMaUhb0GOqUBQ1w93x%2FPM4mGt5wchKD0GgyAb1Ord1sJB0yLZ%2BXQ%2BnCSwVUF4vb6246Dpz75m9oq9smA4Qqu0MMbORmBrh299mM9RfjaZl8crjo5ZZ%2BUO4SVBpzh7bvNaJe%2F3NHAHP3Qu06zk%2BW2Z2LhUyyKOa4%2BbBqY7xGHu63NpCNGAcKC3ujPeN8ybnzxLDosnlOZwXEhV5MljuQSVrwvzePS15A9A11VN3YD&X-Amz-Signature=267844632a5c435c90f782048f4b2a61a94d89ba80906a3a29dac0124b32e7eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FMIDT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHNzsQKKTvkVOgOd2TUEvqd9qJ5qlO4wdaB7KyVHBi2%2FAiEA%2B4zTnrm4M9aj%2BPHD2H3spq4Y1jGj9CFPhZSGWvuPap0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJha%2FSC%2Fg6garbfIiircA7vQNKiWhsXF8udEsGUb6Zh0J44gQOxz4ac25R%2Bk98k0LyQTA3MzSiMZu89h198aIGk6x7YGCN09TZUd9srvSNWI7EJjgvAMU5u1W%2FCIgludrEPdyhaHqn0bvr8JaDjZNwbP5%2FUjmUaLnMZVON1%2Bo%2BLedJ0o%2BDqJqvxwW2L5dB7ljoQl9s7QartvAGr1%2FI7CHniTkPYzoAytzMYV3RzcUQE32RZV4O%2BoajAzMdyNtVxuI%2FI2WAyiTs%2BSmdrUBVONY5hJ3h9sYI1%2Fch0G8anV7t2hR0wvHUZp0Ddj0IqUKL8sVSdajdbaLQMq5RNG1RJ4Xcgo0cmdtgSlsWWo%2FCZXNju9rh6lIBVu9uKdod4tK03hCKP3xQK4%2Fvyji6WvYE4h6Bw3H0Qdzt1Y0yd4%2Bgv8mNR49Xkj%2BAjFyZyk5P0MsvQ5adhmZBQWsXk4NmbFGNo51jPz6MYKloUmhNY0ZqBtmdUTCaeHbJBLiXbSSrRAGe4HSXNs2omSoW2vsPISYwSGFR32X%2F1cDhPDFt0BopXzp4ZUWh7a6U5jufLGRZtpR%2FWAhfhREtPSmsdy8B2fWQ9joRObb%2Fu6MO677hcT7PKPxJ%2FECycBv9r%2FpBZs%2F0GXBqYdfamJw2Xupo5FMC4mMMaUhb0GOqUBQ1w93x%2FPM4mGt5wchKD0GgyAb1Ord1sJB0yLZ%2BXQ%2BnCSwVUF4vb6246Dpz75m9oq9smA4Qqu0MMbORmBrh299mM9RfjaZl8crjo5ZZ%2BUO4SVBpzh7bvNaJe%2F3NHAHP3Qu06zk%2BW2Z2LhUyyKOa4%2BbBqY7xGHu63NpCNGAcKC3ujPeN8ybnzxLDosnlOZwXEhV5MljuQSVrwvzePS15A9A11VN3YD&X-Amz-Signature=423a7d5229c892b392ef8df56c043fa776de51884bc7b5e35882f80e84be50f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FMIDT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHNzsQKKTvkVOgOd2TUEvqd9qJ5qlO4wdaB7KyVHBi2%2FAiEA%2B4zTnrm4M9aj%2BPHD2H3spq4Y1jGj9CFPhZSGWvuPap0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJha%2FSC%2Fg6garbfIiircA7vQNKiWhsXF8udEsGUb6Zh0J44gQOxz4ac25R%2Bk98k0LyQTA3MzSiMZu89h198aIGk6x7YGCN09TZUd9srvSNWI7EJjgvAMU5u1W%2FCIgludrEPdyhaHqn0bvr8JaDjZNwbP5%2FUjmUaLnMZVON1%2Bo%2BLedJ0o%2BDqJqvxwW2L5dB7ljoQl9s7QartvAGr1%2FI7CHniTkPYzoAytzMYV3RzcUQE32RZV4O%2BoajAzMdyNtVxuI%2FI2WAyiTs%2BSmdrUBVONY5hJ3h9sYI1%2Fch0G8anV7t2hR0wvHUZp0Ddj0IqUKL8sVSdajdbaLQMq5RNG1RJ4Xcgo0cmdtgSlsWWo%2FCZXNju9rh6lIBVu9uKdod4tK03hCKP3xQK4%2Fvyji6WvYE4h6Bw3H0Qdzt1Y0yd4%2Bgv8mNR49Xkj%2BAjFyZyk5P0MsvQ5adhmZBQWsXk4NmbFGNo51jPz6MYKloUmhNY0ZqBtmdUTCaeHbJBLiXbSSrRAGe4HSXNs2omSoW2vsPISYwSGFR32X%2F1cDhPDFt0BopXzp4ZUWh7a6U5jufLGRZtpR%2FWAhfhREtPSmsdy8B2fWQ9joRObb%2Fu6MO677hcT7PKPxJ%2FECycBv9r%2FpBZs%2F0GXBqYdfamJw2Xupo5FMC4mMMaUhb0GOqUBQ1w93x%2FPM4mGt5wchKD0GgyAb1Ord1sJB0yLZ%2BXQ%2BnCSwVUF4vb6246Dpz75m9oq9smA4Qqu0MMbORmBrh299mM9RfjaZl8crjo5ZZ%2BUO4SVBpzh7bvNaJe%2F3NHAHP3Qu06zk%2BW2Z2LhUyyKOa4%2BbBqY7xGHu63NpCNGAcKC3ujPeN8ybnzxLDosnlOZwXEhV5MljuQSVrwvzePS15A9A11VN3YD&X-Amz-Signature=d7e761eee5144213e790d514fdf977c541032212b8aa4cab7392477d4c2777fb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ5OU7AB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCICJhcxF%2F6LiBCzLdADASVftzmquAi4wCUrAwzNQk3eW5AiEAtyOPwVq23Hi7GU3a8YH1BmGgjNP0B0IXASSx00VZPYAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDMK9aUJ18FY7GAtT9yrcA1J3hWFUceKIWNCovLwI5NEsLD78LlztlJ%2BYhWIvsv%2Byux0%2BoUi35QSFkJO0F4SZxV4FT8rHr%2BcBpsESUNWVT40ZrTfUR6W%2Fi%2B7Ud0z5ohqxtFPmBGx2HK1MmWQwWycM9JAqbxw1%2FX7yKdxYmPqYMDYfd2ZAbVkNlGsqh8g6rvvylVJzdUMUqe5D5yfPhZyWPaaCzzFXLdHAzL6%2FqOytXZ6G7o74TBOohqLVeWIzLuTqdfm08Xp6u3KR9ocdImpl1B9lgrz6t6PnGq4cGoGiizXA5EYkx5k7y6wqzawa54LDIPqRZQgP6Vy388HcgChmcLSSPp97f4egPCVf6oHpQFTBDl%2BCQWmtbcsetKZwL7lBGlY66RI2pTKr9NCo2RXB5rMrkQrgGp9jtFyNyrPqf9ldv%2BIrLePsfbld9gpKtkqcqeNovluAEcpc%2Bdf8sLATVa26VQFyKLt9kUSwsiBXEGwpOL9fKgJz5ke5VESh24NJHdab%2FOYd%2Fc4SrodOV7hzAIdVWVZCDnBysZ87YXRC8T7%2FihZBJB3BJ56IOuPVeZqm8qBcTcP%2B3fNVXMGRpK%2FRY8S8AIyaWtqdJNlPolgh5uppx0pznszDZodaTEorIXB00NTM4%2FG5WUlaVhSfMNiThb0GOqUBbkmDyweDhA3Fm1wXmPAr0jgZ4tqaOS8BD%2Fakhc%2F%2F%2BOQ%2B4AeVm9roe9r78ewh%2FxuVxvG67YUsafxUbUvpETCgAlXqw0XcbEPjacBpS4m3rqxGGIKuZ7Sv%2BmvyK98qnAzRGyy%2FIYm5t5BID9QKUcJ8h7J%2Bcwwjzf35AQB4Io8dwim%2Bmg3vFi6ZGlBhFGXW%2B9IVBh5n4ezvKb55MTBzIMzxIRjw10VR&X-Amz-Signature=072c9f3e08dd75c95e604d16e7e72243a01fd1a6bbaaea57a631b8c486b7cb13&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7FA3DKW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCkElqlxc5SlaoR220jdR6BEMbMDv0UEQ7lNvoU5Ny4mQIhAN33GH3HVYcPrtOB%2B4mg5DInhYldGk6C%2FtXPcSm7NDmMKv8DCCAQABoMNjM3NDIzMTgzODA1Igw6SVj07U3U3dpvpwEq3API5xY7GSH28NIc3YBCpaSUw8sMEGOteATeI1YIYJ9jDvhtVv5teZMQwTTGMQ%2BQon21vZ7LLHksnMrBzSQLFFN3TeDCMFHKwRTmcCIThPqD6%2BbeiunKrWFFb9xPNl3GSP%2F6EFjHfWEcyGDKn1VPdP%2FQAH%2F5p9dOozTotZK7qoWTdyDGUxNJtuj1v8dEeNGmcrPFPpf3eaJjsSdaDOBjA5jcxapdGxATNYm%2BSzOiIyQf3uWkki%2FDA6uoYycXrjG6ebVNV8K49CbgrueIV6h%2BOpXy%2Fs6HkSQegtBgwOWDMI%2FzMdBew2QjLxf4N%2F82x8mWWmBvgjsauveYsWLDBY9O9LXIfZBGORvdpXwd%2FksRc6eu12LkMtcP4HUSOyWfpMxY65tjx16OHygNX7vA5%2FuunE%2BYCK3k1m7HC%2FLqwLypSlAepQQFhXBoQBGa2C75G1Sj%2BjirOjugoIl2Eb3PcshG6ynaJYBHFJq1ntgkILEqxVB5cOMCczZF7NWtmNqQi%2B1CU%2B%2FCrhALiCVkmW0LmFojbDY%2BfhLr4o%2F5lmEr6t6bc%2BUbiKYWp76wMgmdLB3t%2F7aW1y%2BCwMC8yJSlFdh%2FUnXJTL58%2FhEiR8rIP2jZekx5fX4PEalCPG1Y%2FQ66HtfSSjDFlIW9BjqkAZhLLU14H6V3HAi5WfowL05xjtdtahlMONH7D0ykCnBoqxFRzgH5NTsLtTW0fjAuZpPCBbycOuMN30RoVUOLlpxP0q%2FjvaYp8lILVzATjwY1J2tRmvaTRSKd%2BbaRApDxcZJqr1l4OktlT5FodcfVjhgfGGB2fuAR7I2o8Df9Fy4v5EjfCMb54aRGw%2FthTWOu4WIKU%2BnA7z8ErWBhNcwFBM%2BqTKen&X-Amz-Signature=4f47efedece6a6bdcdaf46c5ea57e97d0e1b0b7fff11c8623ed100085e0cd04a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FMIDT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHNzsQKKTvkVOgOd2TUEvqd9qJ5qlO4wdaB7KyVHBi2%2FAiEA%2B4zTnrm4M9aj%2BPHD2H3spq4Y1jGj9CFPhZSGWvuPap0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJha%2FSC%2Fg6garbfIiircA7vQNKiWhsXF8udEsGUb6Zh0J44gQOxz4ac25R%2Bk98k0LyQTA3MzSiMZu89h198aIGk6x7YGCN09TZUd9srvSNWI7EJjgvAMU5u1W%2FCIgludrEPdyhaHqn0bvr8JaDjZNwbP5%2FUjmUaLnMZVON1%2Bo%2BLedJ0o%2BDqJqvxwW2L5dB7ljoQl9s7QartvAGr1%2FI7CHniTkPYzoAytzMYV3RzcUQE32RZV4O%2BoajAzMdyNtVxuI%2FI2WAyiTs%2BSmdrUBVONY5hJ3h9sYI1%2Fch0G8anV7t2hR0wvHUZp0Ddj0IqUKL8sVSdajdbaLQMq5RNG1RJ4Xcgo0cmdtgSlsWWo%2FCZXNju9rh6lIBVu9uKdod4tK03hCKP3xQK4%2Fvyji6WvYE4h6Bw3H0Qdzt1Y0yd4%2Bgv8mNR49Xkj%2BAjFyZyk5P0MsvQ5adhmZBQWsXk4NmbFGNo51jPz6MYKloUmhNY0ZqBtmdUTCaeHbJBLiXbSSrRAGe4HSXNs2omSoW2vsPISYwSGFR32X%2F1cDhPDFt0BopXzp4ZUWh7a6U5jufLGRZtpR%2FWAhfhREtPSmsdy8B2fWQ9joRObb%2Fu6MO677hcT7PKPxJ%2FECycBv9r%2FpBZs%2F0GXBqYdfamJw2Xupo5FMC4mMMaUhb0GOqUBQ1w93x%2FPM4mGt5wchKD0GgyAb1Ord1sJB0yLZ%2BXQ%2BnCSwVUF4vb6246Dpz75m9oq9smA4Qqu0MMbORmBrh299mM9RfjaZl8crjo5ZZ%2BUO4SVBpzh7bvNaJe%2F3NHAHP3Qu06zk%2BW2Z2LhUyyKOa4%2BbBqY7xGHu63NpCNGAcKC3ujPeN8ybnzxLDosnlOZwXEhV5MljuQSVrwvzePS15A9A11VN3YD&X-Amz-Signature=595c362f47eccc37daf76302d928bcbaf006f33433c3434c1888d9df086b4e43&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FMIDT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHNzsQKKTvkVOgOd2TUEvqd9qJ5qlO4wdaB7KyVHBi2%2FAiEA%2B4zTnrm4M9aj%2BPHD2H3spq4Y1jGj9CFPhZSGWvuPap0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJha%2FSC%2Fg6garbfIiircA7vQNKiWhsXF8udEsGUb6Zh0J44gQOxz4ac25R%2Bk98k0LyQTA3MzSiMZu89h198aIGk6x7YGCN09TZUd9srvSNWI7EJjgvAMU5u1W%2FCIgludrEPdyhaHqn0bvr8JaDjZNwbP5%2FUjmUaLnMZVON1%2Bo%2BLedJ0o%2BDqJqvxwW2L5dB7ljoQl9s7QartvAGr1%2FI7CHniTkPYzoAytzMYV3RzcUQE32RZV4O%2BoajAzMdyNtVxuI%2FI2WAyiTs%2BSmdrUBVONY5hJ3h9sYI1%2Fch0G8anV7t2hR0wvHUZp0Ddj0IqUKL8sVSdajdbaLQMq5RNG1RJ4Xcgo0cmdtgSlsWWo%2FCZXNju9rh6lIBVu9uKdod4tK03hCKP3xQK4%2Fvyji6WvYE4h6Bw3H0Qdzt1Y0yd4%2Bgv8mNR49Xkj%2BAjFyZyk5P0MsvQ5adhmZBQWsXk4NmbFGNo51jPz6MYKloUmhNY0ZqBtmdUTCaeHbJBLiXbSSrRAGe4HSXNs2omSoW2vsPISYwSGFR32X%2F1cDhPDFt0BopXzp4ZUWh7a6U5jufLGRZtpR%2FWAhfhREtPSmsdy8B2fWQ9joRObb%2Fu6MO677hcT7PKPxJ%2FECycBv9r%2FpBZs%2F0GXBqYdfamJw2Xupo5FMC4mMMaUhb0GOqUBQ1w93x%2FPM4mGt5wchKD0GgyAb1Ord1sJB0yLZ%2BXQ%2BnCSwVUF4vb6246Dpz75m9oq9smA4Qqu0MMbORmBrh299mM9RfjaZl8crjo5ZZ%2BUO4SVBpzh7bvNaJe%2F3NHAHP3Qu06zk%2BW2Z2LhUyyKOa4%2BbBqY7xGHu63NpCNGAcKC3ujPeN8ybnzxLDosnlOZwXEhV5MljuQSVrwvzePS15A9A11VN3YD&X-Amz-Signature=8cc87e523ed8cabdd4ae5c08f49e58496b9fe129ae99332ca0291059bcb2f2da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FMIDT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIHNzsQKKTvkVOgOd2TUEvqd9qJ5qlO4wdaB7KyVHBi2%2FAiEA%2B4zTnrm4M9aj%2BPHD2H3spq4Y1jGj9CFPhZSGWvuPap0q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJha%2FSC%2Fg6garbfIiircA7vQNKiWhsXF8udEsGUb6Zh0J44gQOxz4ac25R%2Bk98k0LyQTA3MzSiMZu89h198aIGk6x7YGCN09TZUd9srvSNWI7EJjgvAMU5u1W%2FCIgludrEPdyhaHqn0bvr8JaDjZNwbP5%2FUjmUaLnMZVON1%2Bo%2BLedJ0o%2BDqJqvxwW2L5dB7ljoQl9s7QartvAGr1%2FI7CHniTkPYzoAytzMYV3RzcUQE32RZV4O%2BoajAzMdyNtVxuI%2FI2WAyiTs%2BSmdrUBVONY5hJ3h9sYI1%2Fch0G8anV7t2hR0wvHUZp0Ddj0IqUKL8sVSdajdbaLQMq5RNG1RJ4Xcgo0cmdtgSlsWWo%2FCZXNju9rh6lIBVu9uKdod4tK03hCKP3xQK4%2Fvyji6WvYE4h6Bw3H0Qdzt1Y0yd4%2Bgv8mNR49Xkj%2BAjFyZyk5P0MsvQ5adhmZBQWsXk4NmbFGNo51jPz6MYKloUmhNY0ZqBtmdUTCaeHbJBLiXbSSrRAGe4HSXNs2omSoW2vsPISYwSGFR32X%2F1cDhPDFt0BopXzp4ZUWh7a6U5jufLGRZtpR%2FWAhfhREtPSmsdy8B2fWQ9joRObb%2Fu6MO677hcT7PKPxJ%2FECycBv9r%2FpBZs%2F0GXBqYdfamJw2Xupo5FMC4mMMaUhb0GOqUBQ1w93x%2FPM4mGt5wchKD0GgyAb1Ord1sJB0yLZ%2BXQ%2BnCSwVUF4vb6246Dpz75m9oq9smA4Qqu0MMbORmBrh299mM9RfjaZl8crjo5ZZ%2BUO4SVBpzh7bvNaJe%2F3NHAHP3Qu06zk%2BW2Z2LhUyyKOa4%2BbBqY7xGHu63NpCNGAcKC3ujPeN8ybnzxLDosnlOZwXEhV5MljuQSVrwvzePS15A9A11VN3YD&X-Amz-Signature=96df2878ba4c9ff01e9415699d78ce2a5bebc57c74fa02f980b104629ac9399a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZUNPID4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIC4T7ZvSmQFCBtxWY%2BfqPD2WqRJU7SKeNdwSFNx729I%2FAiA1UWzHU%2BgQu6zXhM5%2BF%2BECvx%2BZmkM4MdD5fbRXc4K7mir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMGlfqnpUsJmEd8JbyKtwD0P5re3Oudf67uJraNW1LW7J1%2FylejLM9KuQf7DGug3at9FkU5oa3aj4MSAoHcRqxmnGbhwZ%2BxrAV9irmzliZvZiqz%2FcU1ACPLiJcMtMASSTghXZ2kTQ8atwMGtQJ6WSisnu6%2BJhQBz2aSlyYVr9whWn4FoAjIRFiomzmEMLaGLAtyYK1TXsVNB%2BTHVzn1%2F2D4xks%2FIYc%2FouWhfwhqeUAnoOcLsVFZXWu0VtlvKCoA6EBBPfRUkSzpiMS7AHlatzBAjHzp%2BG%2F8vNW%2BncK9MLf4YX2MF81h24aQ8lCdbVR3MNJqd4MO%2BdSOSF60Hw5OGeiEO8ieQaijXEgwXuSGd1KN1ZhLts9hiDkYH7cnK0903sY7bygCrzZp%2Fb0SwGHxQCsfylHzgA2%2FRQDZ89emqnkLQ83%2Fj0P7b2ZYlEziJdx2TIvmzvlOKxbqBmbTocqEOkCdpjs47lRh41qvwa1cmlzuBlYs40GT72lpN2tUDZ8tmhCM1MAXoD97nbUg5uhOxrlWp0RoWbaGUn%2Begaw%2F5Sg0pqcFvvBck9Q2WprsAFdyGGGFdVBChfOnHjq%2BNfkE2l284pgUkFjSdOM%2BwCO7CCVRt3RHyLQ9QqrCYhgqda05x0EhUw89Hu09lkj3Acw95OFvQY6pgH7ePXAw1uquQjB4Jyis0DJTy3ZeWFZ7gAS2PrE00hsWnxiX3HhLNmaZlc%2F5VrqLN893DvFT1pevbCu7EOxkE8W4ueaJLF9Wyag5Ceo1EVnerVl%2FNSazcoEjsy10PSRXPqAJ1hdX6F93q5k92XPyQptja3Qc2DKgICtBL4ajWgjgJ4wlrVLfLOX%2FkP0kxxbF62kx2K1NjpZA9lzWR4e04GBf8l29t9X&X-Amz-Signature=afb08e160c3490e9ac446b3ce2f14c97f361e33c05103c64223310265a37c56b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665445LVHB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCDvtcAQCZNAEGzqCipPVPx5VMSx97gz7sx7nMwZxHUkQIgI3m7dzhDNsDonZ9kfksCbicd3Vu%2BIAGU6ulyqGYIS80q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDA%2FzRSpJvG31gzkreyrcA3HlM%2FSGb2rgqfESF5abv48ylmmb%2FmaGYYmX8iQNriDeDTrZsiONcnUpp%2BVBtDas66lRFdWos%2BVl9L7Vi60oD2mNa90r7g55dMuE6wEQw6QdMNsW6PsyEPELdDI8033L%2BlX%2Fz4BSvjkEwv6yWXXH4TW6TBvl0xkQjyqFL9OXKHcVn27sN58iDCQuQ5QoV5KGhvaclRKdcR4b2V9qNoCoELIWv9QQiQNzq0WUUbwXqHMow3OaL9Cxequc%2FOOv74IWE1WBKira7qXgilw4y0CcJ0qiqTugYdSQLMYoP1MbRB7hPm0Qucc2hs7nJcT0qmPoqj0PLiWr26h4KayJ582Yy6RdVPianXB9Y5fB2Lzz%2F3UR2j1CWkilsdxJWjrEBWMNVZn1REzS%2FaYySJiglaGngBEqhGmwNcFBp9onIjiLq3luwej0fVXc%2FXxcHWjxku5qbR8xOoapkpqOw1Khl9zQNA%2FerPQzwzWgIqgZHo%2FCbLF92Hol6CGS9q%2BI4oobAbKLwaFT2J1O0jNGg5W16qugHH739I%2BMLoIrXItUu1vagJThX%2F5jW37fVMHRIb0Oh4mA%2FoGpwKBsbcCA05GENQMK2xik41UbkL4EM88aO39p9T1AtUvCp8Sx6jZQfsWLMPeThb0GOqUBUgHm4Rgf2p9MzCEdE%2BOQi%2BfpJXk8tFbEhUdf9y2qanqeTjcDaG3qMSq2lW8uMPCsYQbCSG2O7uam5TE6SB%2BlI6i1JTBjGAB9hyhbUwGMAbX58rRcBM0Dqez4cLYJQszn1kyeFZQiu7%2BdKS9Z5vCph%2FVC6oLSQ6BwOe0bJlg9tLw%2F4%2B%2B93vx8Cv%2Bh0i1En130CyzgLHlhuOUuJL%2F6fjmXyrtwUWbv&X-Amz-Signature=b99498fc1eed943b53ce7fa9203d535b82e6efde29fd7c3918b4470ba9311b8a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4XVST7S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDWReR%2F7dPAJWlLiZeOvM3d8c99iveiRQUEy4fJw30ftQIgQ9NfCUwG8mSuLdwZC8oWZ0zVt2umhGN7pluT4Qe5DI8q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDJSF1efiJKyTRseWFircAywvrDpl25yybfxjc%2BGeiuyvVXIunLfRKcb4%2Fca6WuhxCBnZOIawx61Sscz1Vsok3RLubs4AunTwQy6REuQubOylNwCV8q3z%2BMlqo3K3u2LhEdbg7FXXZ1CW1D6ijnbYy99hm%2FfvzqjcFupYoKlkVEmULKKiCancEr1QGOXU8125iW9JlILPp50YM1ClUgiZp1lU%2FPZ2ULeRUC%2BfrWaxwAbZ0YqOLUOrz2M6frxW%2FgtU5Kfsm2cbO9hdcLGk3nPmzmNq7G46EI4HU8M62Z7%2BmXiFlj%2BlPColv2MPReeFvnw5zqFW8cIegh%2FIG4hKfRNQtaJC0rZALhAYhgeqgZvneELy853%2BjaJ6YVn%2FELsumK1WkC96bVy2sMxixN4pIB%2BcdwBHu0usZiGqzfoTlW6u09efTmYmD%2FiMiWW24MKHa9XzbQaG5U9mGXXFTe%2F9SVEiMZ16BaKXlYE1VMFxTXKecoQ6dIoZp2IOOoEDpM4xKaoGYsGyqe4%2FAjpEDuwI99Shzdk7wXhFWyinIuRLRqDzU0J8FB7Vooj%2BkJf%2BaKP8WoEwBosSmgSJpdhan8ouRBEtLh3jL3ZV%2FgQfOfrqGcUg3UldbiwTr9kP%2BhQO7lV9x4jpq%2FJoZF9gzGH278tvMPeThb0GOqUBXXdtg11sQfXLaTyRzsTAl0o10DmINLxCLI6n%2BdDte2JT5NAsig1RxQc50Z2Ev7EywA3cZTap4VepuP4%2BsdY5mB1EcFQM1xUgXOIQGwE0CXCdaSFlZfKOEYKeHwFHINAcanx49IZKdJrPZBTjZLpAGTAgnyxQYAoaXYG2nPItUeuxy0XprbXNm7JL6n5wUFUK0NWwCepY8OMXuAHfHmAyrZOxm2Hu&X-Amz-Signature=2fa6b779cf36a9e0b603dc4a889560d5c87f6ee80e29c151b8b9091dd1862062&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIGOJQCG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIGqaFmlmuQPz2T1aU62721OzShNZRFQVusTc%2F%2Bgij2D7AiAcYXWUiI4pEMbGV2w1r155LYLKIFC4X7QvCI85r3U6Cir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMeF98fHLgAvoLFieIKtwD8D0BthrxJ4iTiN2Q18RaMc9HUO%2Ftdo4%2BoZFTggy78STMy09mfuz5Thb4NGVIYlIpdB8YUsRxap%2B%2FIldtpOz683Twp%2BEt4tbV6aB9pgbrfLUE9BzhdyV%2BIU2OMW2rRowfytjxts%2FDJ%2B%2FN%2FJnBoNJuCkDJDIV3gYxnG6ylA4zlAMoGo00t6RsmjQFoTq3mG24h0IMe7DcUD8LP4XVZPXkuXIgmJ02HCu2vukO2Y2WGUOodhFs75APGyiiVA5hvXyRzoKYdZK3p4py1vLHcFYrbR4VvGAFrorXGjW3GJvuYlZWOTRMMuCN7hPYJwtVGczleDlhZDgRxv28tV0Tpdk4M99gymSQUND1QTs1dty9wQu8%2Bp1ZQvj8IT7f6JjlWpkSoJBQIDq%2FGgyiPV8XKAzUZdDbBP9gCmKS776ajWeglmbUIK3l5cN7ZsO4uJzntTaeT1MzQRlwxGcFr1YFnwBsdzJVJlVhpnqmMiRMKHlhJ5XnVdTm%2FSXhFu04BmTbhhPoFJkrxok5hykLrW%2Fexu%2FKtWRMErcxu%2BaS5Nconp32VpAqlCExjlgxBUOeza5gayGAlXeVVRuMw3i7Zgnxy5YF3D%2B%2BIHEPo%2FQL3tnk7X78ZjQsaoOnP3iSfbD3j%2BNAwlpSFvQY6pgELnHR0PhSip9BVqFJ0Cu8pI3ROpPJ1QoC1J9PsUR%2B%2B%2BHtfiHSjR1UWA2JCHyvUXGyvCdfra86yMHJQUUq%2FqPL1mTmEnsSeel3AQ1e%2BmYYfgawrtGy8rHN92B8m6ZlWNI4Ght%2Fy2tmhe8sv0xiZNX1%2FNBLilBCEGf%2FoU44wsdbYYTpwKApUEfMn%2FRHOhDVxLUMQV8tLkRtIippLhlNqPl0PYUf1sLEc&X-Amz-Signature=0cdb29ca0a6c14720bec241580708a2b153bb4a7c7896ad47894dddbc8b7fcc9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIGOJQCG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIGqaFmlmuQPz2T1aU62721OzShNZRFQVusTc%2F%2Bgij2D7AiAcYXWUiI4pEMbGV2w1r155LYLKIFC4X7QvCI85r3U6Cir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMeF98fHLgAvoLFieIKtwD8D0BthrxJ4iTiN2Q18RaMc9HUO%2Ftdo4%2BoZFTggy78STMy09mfuz5Thb4NGVIYlIpdB8YUsRxap%2B%2FIldtpOz683Twp%2BEt4tbV6aB9pgbrfLUE9BzhdyV%2BIU2OMW2rRowfytjxts%2FDJ%2B%2FN%2FJnBoNJuCkDJDIV3gYxnG6ylA4zlAMoGo00t6RsmjQFoTq3mG24h0IMe7DcUD8LP4XVZPXkuXIgmJ02HCu2vukO2Y2WGUOodhFs75APGyiiVA5hvXyRzoKYdZK3p4py1vLHcFYrbR4VvGAFrorXGjW3GJvuYlZWOTRMMuCN7hPYJwtVGczleDlhZDgRxv28tV0Tpdk4M99gymSQUND1QTs1dty9wQu8%2Bp1ZQvj8IT7f6JjlWpkSoJBQIDq%2FGgyiPV8XKAzUZdDbBP9gCmKS776ajWeglmbUIK3l5cN7ZsO4uJzntTaeT1MzQRlwxGcFr1YFnwBsdzJVJlVhpnqmMiRMKHlhJ5XnVdTm%2FSXhFu04BmTbhhPoFJkrxok5hykLrW%2Fexu%2FKtWRMErcxu%2BaS5Nconp32VpAqlCExjlgxBUOeza5gayGAlXeVVRuMw3i7Zgnxy5YF3D%2B%2BIHEPo%2FQL3tnk7X78ZjQsaoOnP3iSfbD3j%2BNAwlpSFvQY6pgELnHR0PhSip9BVqFJ0Cu8pI3ROpPJ1QoC1J9PsUR%2B%2B%2BHtfiHSjR1UWA2JCHyvUXGyvCdfra86yMHJQUUq%2FqPL1mTmEnsSeel3AQ1e%2BmYYfgawrtGy8rHN92B8m6ZlWNI4Ght%2Fy2tmhe8sv0xiZNX1%2FNBLilBCEGf%2FoU44wsdbYYTpwKApUEfMn%2FRHOhDVxLUMQV8tLkRtIippLhlNqPl0PYUf1sLEc&X-Amz-Signature=453c129701ad4fb3c8a77b774838f22802de967e4f47158c697d4d84e6edef14&X-Amz-SignedHeaders=host&x-id=GetObject)

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
