

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677MUWE3N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCgcVwJUxIXrh1rH62%2BzpFea21A6j7W%2BvvjAAsMHcvivgIgS4WIcer7kfAx8J9ZknsfAAWQUdrZ7o6msffytG6%2Fqh8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNWQ0ddDLUwTeF5V9ircA2DOCjh%2FR7t3vbY55vUf4JO25IjVOgejzXa%2BveZ%2FyfkI3nVE2UDapxQATggAxszngJ1u3%2BZrOHfun9bH5ZMCYJO%2BK6FCm6qnD7PRB3yNCGDWeLm0kLblQDrauj9yrXAbgUCwYleEntFiooy%2BP5%2F5MxPk8FM3Z9V8e0WY0MwDYbuvavmNxdvOi0nReAcp6O9Yae8tS9V%2B%2FoldqhZKcLS1KLrrYmbwXYyYYssVM4JR2JsheIqgDpEznzHKKz3OKi6AOid985KoeMvP%2BK%2F2KmhYPkmTzhLyTWXxrPUSxERCdERALNbGxBzCz3rhi0BhTDBwUkIZJ1EMYtLheeISNomf3Uz73pvWKu9A4dA9TPzAJP6V5re8Gg0ZDYZoCYMCAtLX1GJbOHxHE5eC52Dcr76FHLDf%2Bh%2BD0wYmRjCi8x01KhlMeKyjEksPHfKmgbnLuuGDwZtLx1M4bSGL8F47%2BbDzKig7B5%2F9jkezNBMVOd5h7vGh0wElmMMCI8fSZliBFUk7n30gnQQDvRt0f8Un1BC9M6AXYrc5CUzSudCSTUIfWMV%2BuT%2Fi1l3FcH9jHtp2nH983z7V7hsiZEYAa4cyyh7TDO%2BNE%2FwcKM9mYS9vo03gaXxnj8iSuDp7VVRU6fBqMIq8jr0GOqUBLFfjqDKUDNqDxOOufTJbccbUD32p4%2B%2FtwzxOI4FUz5moZQ%2FMaUyj4N2ecKXlHqIMmDBru5%2FcZTqhLY9gIzJdG4i33scgFKg8uY7FzrITGKJitGq7mzVo9km4u6y8fCW91yC2%2BWnVtSZtYyOt3%2FoPUHVqsA6qyNoYKWqORKRi9Jf603dH9Nt6NN09T17NPDSc5fbtfwJMaMYOMrV6nT2MxdflCBYP&X-Amz-Signature=7dae58f41c5fdbd7614d5e3af3dd2121db2951a969099ba7cad42674137625dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677MUWE3N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCgcVwJUxIXrh1rH62%2BzpFea21A6j7W%2BvvjAAsMHcvivgIgS4WIcer7kfAx8J9ZknsfAAWQUdrZ7o6msffytG6%2Fqh8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNWQ0ddDLUwTeF5V9ircA2DOCjh%2FR7t3vbY55vUf4JO25IjVOgejzXa%2BveZ%2FyfkI3nVE2UDapxQATggAxszngJ1u3%2BZrOHfun9bH5ZMCYJO%2BK6FCm6qnD7PRB3yNCGDWeLm0kLblQDrauj9yrXAbgUCwYleEntFiooy%2BP5%2F5MxPk8FM3Z9V8e0WY0MwDYbuvavmNxdvOi0nReAcp6O9Yae8tS9V%2B%2FoldqhZKcLS1KLrrYmbwXYyYYssVM4JR2JsheIqgDpEznzHKKz3OKi6AOid985KoeMvP%2BK%2F2KmhYPkmTzhLyTWXxrPUSxERCdERALNbGxBzCz3rhi0BhTDBwUkIZJ1EMYtLheeISNomf3Uz73pvWKu9A4dA9TPzAJP6V5re8Gg0ZDYZoCYMCAtLX1GJbOHxHE5eC52Dcr76FHLDf%2Bh%2BD0wYmRjCi8x01KhlMeKyjEksPHfKmgbnLuuGDwZtLx1M4bSGL8F47%2BbDzKig7B5%2F9jkezNBMVOd5h7vGh0wElmMMCI8fSZliBFUk7n30gnQQDvRt0f8Un1BC9M6AXYrc5CUzSudCSTUIfWMV%2BuT%2Fi1l3FcH9jHtp2nH983z7V7hsiZEYAa4cyyh7TDO%2BNE%2FwcKM9mYS9vo03gaXxnj8iSuDp7VVRU6fBqMIq8jr0GOqUBLFfjqDKUDNqDxOOufTJbccbUD32p4%2B%2FtwzxOI4FUz5moZQ%2FMaUyj4N2ecKXlHqIMmDBru5%2FcZTqhLY9gIzJdG4i33scgFKg8uY7FzrITGKJitGq7mzVo9km4u6y8fCW91yC2%2BWnVtSZtYyOt3%2FoPUHVqsA6qyNoYKWqORKRi9Jf603dH9Nt6NN09T17NPDSc5fbtfwJMaMYOMrV6nT2MxdflCBYP&X-Amz-Signature=6b92f8f121f77eac41e9d03fbbcee2e573ade32a402981a9a0c2ce1a5eaa787e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677MUWE3N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCgcVwJUxIXrh1rH62%2BzpFea21A6j7W%2BvvjAAsMHcvivgIgS4WIcer7kfAx8J9ZknsfAAWQUdrZ7o6msffytG6%2Fqh8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNWQ0ddDLUwTeF5V9ircA2DOCjh%2FR7t3vbY55vUf4JO25IjVOgejzXa%2BveZ%2FyfkI3nVE2UDapxQATggAxszngJ1u3%2BZrOHfun9bH5ZMCYJO%2BK6FCm6qnD7PRB3yNCGDWeLm0kLblQDrauj9yrXAbgUCwYleEntFiooy%2BP5%2F5MxPk8FM3Z9V8e0WY0MwDYbuvavmNxdvOi0nReAcp6O9Yae8tS9V%2B%2FoldqhZKcLS1KLrrYmbwXYyYYssVM4JR2JsheIqgDpEznzHKKz3OKi6AOid985KoeMvP%2BK%2F2KmhYPkmTzhLyTWXxrPUSxERCdERALNbGxBzCz3rhi0BhTDBwUkIZJ1EMYtLheeISNomf3Uz73pvWKu9A4dA9TPzAJP6V5re8Gg0ZDYZoCYMCAtLX1GJbOHxHE5eC52Dcr76FHLDf%2Bh%2BD0wYmRjCi8x01KhlMeKyjEksPHfKmgbnLuuGDwZtLx1M4bSGL8F47%2BbDzKig7B5%2F9jkezNBMVOd5h7vGh0wElmMMCI8fSZliBFUk7n30gnQQDvRt0f8Un1BC9M6AXYrc5CUzSudCSTUIfWMV%2BuT%2Fi1l3FcH9jHtp2nH983z7V7hsiZEYAa4cyyh7TDO%2BNE%2FwcKM9mYS9vo03gaXxnj8iSuDp7VVRU6fBqMIq8jr0GOqUBLFfjqDKUDNqDxOOufTJbccbUD32p4%2B%2FtwzxOI4FUz5moZQ%2FMaUyj4N2ecKXlHqIMmDBru5%2FcZTqhLY9gIzJdG4i33scgFKg8uY7FzrITGKJitGq7mzVo9km4u6y8fCW91yC2%2BWnVtSZtYyOt3%2FoPUHVqsA6qyNoYKWqORKRi9Jf603dH9Nt6NN09T17NPDSc5fbtfwJMaMYOMrV6nT2MxdflCBYP&X-Amz-Signature=783aa9221c6ddcfcd589286f0e88205c55daadd77ba7d95497f92287b509f4eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AQ3IBTB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCrweqey%2F1aBDuEUlmDU8Be%2Fxvgggqnin%2B3Do8DRYLirgIgYHfLmVtLYEayzf4SIUplWJRhN9UxIjurZf%2FODEplMV8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHzpaKYxPXfCJ4gSJircAy0GIf10r10oqztq7u%2FIOL5QRQxzdWf2gssmjdVSvECdQAUnqUBRg5EMOBRqxaea2olFNn8Ucr6NyQE0%2F9%2FvCrXdBjEhYpEHBpvxNnaX1EFoyNBjxB7rHWfSifuTACxR7n%2FqPp9oXADe2r03bJWfuvXLOfCDzKoNjfhCS244MAOxdzT8MYj6Qj4ecgQSr8mtqSFpEL9HIJQP%2FauljXhE2ws0TKn2xbJbki%2Fqhf9e00y5twiSL756bfqzjAd566uXzhnHWFNpyWAAXISbV1B4jW56t%2Bswe7eteb3soJKn%2Bsrda1d7LF0ocE33aBrkXJsnFVTRLUZ7ahWQOuiT6zURueXJp2JOaaBr5ngNs56zXl5%2BfWrCF3%2BMd7ezY8qld7veACfZJWSX5P3qCuMgnZsk3%2FSwhtQveRUW1SPtbGyZj1F8nR1tI7WilaWizRA9iOT1hPjhoXwFUSRdX6JYceqIdNpzU%2Bqc1RkKljDbwg0tDoDoK2BWN5penMWUrYTY%2FPhnWxLd956yq5JLU2Z%2FWyaVc4GMFyuKIgeIy%2FiA37%2BjRiolEEDLzuh%2BW47N74bFZhdAbkHxkRDxAdocGzFQeTIy6Fk5TdvW4fn7%2B9CQGdxP74R00C71POKlaPF%2FGYBKMPK6jr0GOqUBZoLHyQ%2BRN2POpkUmnQ5KphzU5%2BDm8gDwvpBa0bWkEJ71W9zyawQov8u%2BSNVT5s5r5SmGKSHJ3eynWGX012zYwu9qccSey5v74Iq%2Fyzs6txGbOGUGPFhu16mBb5q2qpiv%2BgiQiP9pF0Nm6t3rxcxLl0ifsrOW%2B1XPLbdgCKw99aMa%2B%2BMS%2FRRL7kmyemHKYb2LDjxwfvv%2FTv5rYANza4egJb0dwrem&X-Amz-Signature=ff526d7f21d224f3ee43c17ff2bf04d47e5d9b72eab7fc41202e4de023946ec2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AQ3IBTB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCrweqey%2F1aBDuEUlmDU8Be%2Fxvgggqnin%2B3Do8DRYLirgIgYHfLmVtLYEayzf4SIUplWJRhN9UxIjurZf%2FODEplMV8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHzpaKYxPXfCJ4gSJircAy0GIf10r10oqztq7u%2FIOL5QRQxzdWf2gssmjdVSvECdQAUnqUBRg5EMOBRqxaea2olFNn8Ucr6NyQE0%2F9%2FvCrXdBjEhYpEHBpvxNnaX1EFoyNBjxB7rHWfSifuTACxR7n%2FqPp9oXADe2r03bJWfuvXLOfCDzKoNjfhCS244MAOxdzT8MYj6Qj4ecgQSr8mtqSFpEL9HIJQP%2FauljXhE2ws0TKn2xbJbki%2Fqhf9e00y5twiSL756bfqzjAd566uXzhnHWFNpyWAAXISbV1B4jW56t%2Bswe7eteb3soJKn%2Bsrda1d7LF0ocE33aBrkXJsnFVTRLUZ7ahWQOuiT6zURueXJp2JOaaBr5ngNs56zXl5%2BfWrCF3%2BMd7ezY8qld7veACfZJWSX5P3qCuMgnZsk3%2FSwhtQveRUW1SPtbGyZj1F8nR1tI7WilaWizRA9iOT1hPjhoXwFUSRdX6JYceqIdNpzU%2Bqc1RkKljDbwg0tDoDoK2BWN5penMWUrYTY%2FPhnWxLd956yq5JLU2Z%2FWyaVc4GMFyuKIgeIy%2FiA37%2BjRiolEEDLzuh%2BW47N74bFZhdAbkHxkRDxAdocGzFQeTIy6Fk5TdvW4fn7%2B9CQGdxP74R00C71POKlaPF%2FGYBKMPK6jr0GOqUBZoLHyQ%2BRN2POpkUmnQ5KphzU5%2BDm8gDwvpBa0bWkEJ71W9zyawQov8u%2BSNVT5s5r5SmGKSHJ3eynWGX012zYwu9qccSey5v74Iq%2Fyzs6txGbOGUGPFhu16mBb5q2qpiv%2BgiQiP9pF0Nm6t3rxcxLl0ifsrOW%2B1XPLbdgCKw99aMa%2B%2BMS%2FRRL7kmyemHKYb2LDjxwfvv%2FTv5rYANza4egJb0dwrem&X-Amz-Signature=2ad39509d360000749cc4136b2d0527d57d31ec1a306c40ca2818e64282f67b3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AQ3IBTB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCrweqey%2F1aBDuEUlmDU8Be%2Fxvgggqnin%2B3Do8DRYLirgIgYHfLmVtLYEayzf4SIUplWJRhN9UxIjurZf%2FODEplMV8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHzpaKYxPXfCJ4gSJircAy0GIf10r10oqztq7u%2FIOL5QRQxzdWf2gssmjdVSvECdQAUnqUBRg5EMOBRqxaea2olFNn8Ucr6NyQE0%2F9%2FvCrXdBjEhYpEHBpvxNnaX1EFoyNBjxB7rHWfSifuTACxR7n%2FqPp9oXADe2r03bJWfuvXLOfCDzKoNjfhCS244MAOxdzT8MYj6Qj4ecgQSr8mtqSFpEL9HIJQP%2FauljXhE2ws0TKn2xbJbki%2Fqhf9e00y5twiSL756bfqzjAd566uXzhnHWFNpyWAAXISbV1B4jW56t%2Bswe7eteb3soJKn%2Bsrda1d7LF0ocE33aBrkXJsnFVTRLUZ7ahWQOuiT6zURueXJp2JOaaBr5ngNs56zXl5%2BfWrCF3%2BMd7ezY8qld7veACfZJWSX5P3qCuMgnZsk3%2FSwhtQveRUW1SPtbGyZj1F8nR1tI7WilaWizRA9iOT1hPjhoXwFUSRdX6JYceqIdNpzU%2Bqc1RkKljDbwg0tDoDoK2BWN5penMWUrYTY%2FPhnWxLd956yq5JLU2Z%2FWyaVc4GMFyuKIgeIy%2FiA37%2BjRiolEEDLzuh%2BW47N74bFZhdAbkHxkRDxAdocGzFQeTIy6Fk5TdvW4fn7%2B9CQGdxP74R00C71POKlaPF%2FGYBKMPK6jr0GOqUBZoLHyQ%2BRN2POpkUmnQ5KphzU5%2BDm8gDwvpBa0bWkEJ71W9zyawQov8u%2BSNVT5s5r5SmGKSHJ3eynWGX012zYwu9qccSey5v74Iq%2Fyzs6txGbOGUGPFhu16mBb5q2qpiv%2BgiQiP9pF0Nm6t3rxcxLl0ifsrOW%2B1XPLbdgCKw99aMa%2B%2BMS%2FRRL7kmyemHKYb2LDjxwfvv%2FTv5rYANza4egJb0dwrem&X-Amz-Signature=10cbce4702c8b2538f3dfd9613c4fdc7d0f26fe304abaaa4f77faa31a0868974&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AQ3IBTB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCrweqey%2F1aBDuEUlmDU8Be%2Fxvgggqnin%2B3Do8DRYLirgIgYHfLmVtLYEayzf4SIUplWJRhN9UxIjurZf%2FODEplMV8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHzpaKYxPXfCJ4gSJircAy0GIf10r10oqztq7u%2FIOL5QRQxzdWf2gssmjdVSvECdQAUnqUBRg5EMOBRqxaea2olFNn8Ucr6NyQE0%2F9%2FvCrXdBjEhYpEHBpvxNnaX1EFoyNBjxB7rHWfSifuTACxR7n%2FqPp9oXADe2r03bJWfuvXLOfCDzKoNjfhCS244MAOxdzT8MYj6Qj4ecgQSr8mtqSFpEL9HIJQP%2FauljXhE2ws0TKn2xbJbki%2Fqhf9e00y5twiSL756bfqzjAd566uXzhnHWFNpyWAAXISbV1B4jW56t%2Bswe7eteb3soJKn%2Bsrda1d7LF0ocE33aBrkXJsnFVTRLUZ7ahWQOuiT6zURueXJp2JOaaBr5ngNs56zXl5%2BfWrCF3%2BMd7ezY8qld7veACfZJWSX5P3qCuMgnZsk3%2FSwhtQveRUW1SPtbGyZj1F8nR1tI7WilaWizRA9iOT1hPjhoXwFUSRdX6JYceqIdNpzU%2Bqc1RkKljDbwg0tDoDoK2BWN5penMWUrYTY%2FPhnWxLd956yq5JLU2Z%2FWyaVc4GMFyuKIgeIy%2FiA37%2BjRiolEEDLzuh%2BW47N74bFZhdAbkHxkRDxAdocGzFQeTIy6Fk5TdvW4fn7%2B9CQGdxP74R00C71POKlaPF%2FGYBKMPK6jr0GOqUBZoLHyQ%2BRN2POpkUmnQ5KphzU5%2BDm8gDwvpBa0bWkEJ71W9zyawQov8u%2BSNVT5s5r5SmGKSHJ3eynWGX012zYwu9qccSey5v74Iq%2Fyzs6txGbOGUGPFhu16mBb5q2qpiv%2BgiQiP9pF0Nm6t3rxcxLl0ifsrOW%2B1XPLbdgCKw99aMa%2B%2BMS%2FRRL7kmyemHKYb2LDjxwfvv%2FTv5rYANza4egJb0dwrem&X-Amz-Signature=bcdac1fe7912442be69d69ad5cc0951ab87bcaabaad0b5e89d19630399610ede&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AQ3IBTB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCrweqey%2F1aBDuEUlmDU8Be%2Fxvgggqnin%2B3Do8DRYLirgIgYHfLmVtLYEayzf4SIUplWJRhN9UxIjurZf%2FODEplMV8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHzpaKYxPXfCJ4gSJircAy0GIf10r10oqztq7u%2FIOL5QRQxzdWf2gssmjdVSvECdQAUnqUBRg5EMOBRqxaea2olFNn8Ucr6NyQE0%2F9%2FvCrXdBjEhYpEHBpvxNnaX1EFoyNBjxB7rHWfSifuTACxR7n%2FqPp9oXADe2r03bJWfuvXLOfCDzKoNjfhCS244MAOxdzT8MYj6Qj4ecgQSr8mtqSFpEL9HIJQP%2FauljXhE2ws0TKn2xbJbki%2Fqhf9e00y5twiSL756bfqzjAd566uXzhnHWFNpyWAAXISbV1B4jW56t%2Bswe7eteb3soJKn%2Bsrda1d7LF0ocE33aBrkXJsnFVTRLUZ7ahWQOuiT6zURueXJp2JOaaBr5ngNs56zXl5%2BfWrCF3%2BMd7ezY8qld7veACfZJWSX5P3qCuMgnZsk3%2FSwhtQveRUW1SPtbGyZj1F8nR1tI7WilaWizRA9iOT1hPjhoXwFUSRdX6JYceqIdNpzU%2Bqc1RkKljDbwg0tDoDoK2BWN5penMWUrYTY%2FPhnWxLd956yq5JLU2Z%2FWyaVc4GMFyuKIgeIy%2FiA37%2BjRiolEEDLzuh%2BW47N74bFZhdAbkHxkRDxAdocGzFQeTIy6Fk5TdvW4fn7%2B9CQGdxP74R00C71POKlaPF%2FGYBKMPK6jr0GOqUBZoLHyQ%2BRN2POpkUmnQ5KphzU5%2BDm8gDwvpBa0bWkEJ71W9zyawQov8u%2BSNVT5s5r5SmGKSHJ3eynWGX012zYwu9qccSey5v74Iq%2Fyzs6txGbOGUGPFhu16mBb5q2qpiv%2BgiQiP9pF0Nm6t3rxcxLl0ifsrOW%2B1XPLbdgCKw99aMa%2B%2BMS%2FRRL7kmyemHKYb2LDjxwfvv%2FTv5rYANza4egJb0dwrem&X-Amz-Signature=37a815d6f7f8b858967db3ae4ce78eca694cd417218b45c62eb4ac03d84572a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AQ3IBTB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCrweqey%2F1aBDuEUlmDU8Be%2Fxvgggqnin%2B3Do8DRYLirgIgYHfLmVtLYEayzf4SIUplWJRhN9UxIjurZf%2FODEplMV8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHzpaKYxPXfCJ4gSJircAy0GIf10r10oqztq7u%2FIOL5QRQxzdWf2gssmjdVSvECdQAUnqUBRg5EMOBRqxaea2olFNn8Ucr6NyQE0%2F9%2FvCrXdBjEhYpEHBpvxNnaX1EFoyNBjxB7rHWfSifuTACxR7n%2FqPp9oXADe2r03bJWfuvXLOfCDzKoNjfhCS244MAOxdzT8MYj6Qj4ecgQSr8mtqSFpEL9HIJQP%2FauljXhE2ws0TKn2xbJbki%2Fqhf9e00y5twiSL756bfqzjAd566uXzhnHWFNpyWAAXISbV1B4jW56t%2Bswe7eteb3soJKn%2Bsrda1d7LF0ocE33aBrkXJsnFVTRLUZ7ahWQOuiT6zURueXJp2JOaaBr5ngNs56zXl5%2BfWrCF3%2BMd7ezY8qld7veACfZJWSX5P3qCuMgnZsk3%2FSwhtQveRUW1SPtbGyZj1F8nR1tI7WilaWizRA9iOT1hPjhoXwFUSRdX6JYceqIdNpzU%2Bqc1RkKljDbwg0tDoDoK2BWN5penMWUrYTY%2FPhnWxLd956yq5JLU2Z%2FWyaVc4GMFyuKIgeIy%2FiA37%2BjRiolEEDLzuh%2BW47N74bFZhdAbkHxkRDxAdocGzFQeTIy6Fk5TdvW4fn7%2B9CQGdxP74R00C71POKlaPF%2FGYBKMPK6jr0GOqUBZoLHyQ%2BRN2POpkUmnQ5KphzU5%2BDm8gDwvpBa0bWkEJ71W9zyawQov8u%2BSNVT5s5r5SmGKSHJ3eynWGX012zYwu9qccSey5v74Iq%2Fyzs6txGbOGUGPFhu16mBb5q2qpiv%2BgiQiP9pF0Nm6t3rxcxLl0ifsrOW%2B1XPLbdgCKw99aMa%2B%2BMS%2FRRL7kmyemHKYb2LDjxwfvv%2FTv5rYANza4egJb0dwrem&X-Amz-Signature=4c6740eecbb1a152ff5f551b9a042346941c78d8e33ed3a147aaee56bb7cd6c7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YBHYX3X%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDSowDMKKbkca53uyfcj4B10seHNoxj8JwKa%2Bfd0PTIVAIhAJes%2BTxaXEglX1fU0hMycqTIvw9HGwkFFNZ1u4XZkt10Kv8DCEoQABoMNjM3NDIzMTgzODA1Igyy%2B04t20GIuAIQi2wq3APxpFkLZiG32tRjB6357eR7roeqnoVM0u2Jd2ayO5GHr9fBeaV4tAg3M6vPM79QnLC%2BHmXVDn%2FgMAy8YCN6dzEPrXdKuVrQc2%2FoBu56OVnYGufiJ0a42y%2BEXOcFx7MSbiMihRUrV1K8A6qj1B4dGkW12A%2BAw4aHjgvCDjurZ%2BSZYLlCTDNzt672F5oLyznwVrN1NcBiDmdynWd1p1B1eWGtuxqzi087Tvtz%2BwJIuukRDPaZWlhbEGm%2FHzrpJ%2FkJC%2BZfMLm8NvZ6Sxtlh63GTIguMRixDwFS%2BINO%2FQSkLnCp0eqlgcj%2BrSJlA%2FTAaTuaGALIIVBWtqosMN4ILVA5qCr1MPfcunhRBvrSv9vj2GNjiyPkT205e2Jc0xJuYEAgt0bwTJuMATxutmSHH3LEZavAP%2FVm76FkrxQk%2B5iNKGjbLptv2boqTs%2F6wyr%2BeTsiWrIT7vdO1p83t9L1UIG3AhZet2yaP2ZLrdYFFRH9ZP0LGZ7iWujSWqWOH2SpWBY1vh49SGC09ikLUQdIuNNRYP1SUNUUk8qpbChBIBGGPR3o02Q7NYOMwnGV%2FLPusRHrcABNS6zxQjeFRypj3IlwCR6Tjf0A7LU7AabNiba1gbtgAla8eWup5XHKEjzlDjDUuo69BjqkAT5f9lktX75A14hwJyiLSHODitSLMjM8L%2B997VVBBLURsQb%2FhyW0l6mW5hhGwJrlNrEuUy1KuBMCDlT9e%2BdEo3HzsiNIorGcpowT1KCjBNgbRYIZjbh8Asoj%2BHVt02XGr5SC2Mb%2BIEa34ocSQBPEeZz3Mrz%2FLu6y7mJCUoXxf7aWEnpIVOVVogsFFlA%2BOAagxoEVyh9%2FZrFItaJ%2FUJ5wkypgvkTD&X-Amz-Signature=4bdb3389e210ee9ae3dde87dca4df1beb89e449aefb75ad8e185ded59626382b&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4LLCQSB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIEkEIS29%2F3ybjKnFEtv7f6UXDN5zl929uoCQywKS94JWAiBRk5eaxsPxZUBTu%2BsCbhq33VvIRPxwMVOqH17bvmP%2Fzyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMvV5x7RG478VMPajBKtwD514jGTEd7OFsdZ68d7bNkoSyP21L222pBTAIP4E4zuZTSNkwYZHlBqWDHl2gIpAc707FvhnJT11YTw8vJrgzx6rn6h7pvheLrebGIN26XEWtKoKuoDzqJ8gQZnbsyLSD2FcSHZy%2FDrC6zS15BvTHeL8B8UueAFYRj7d6XE5GgIJVmYqq0bQXItEEPwFWMpiM7mV9zN%2BqTwNHJvFYfkZ5pPS0lfJJL0a%2BT7HytObFW7I1FG6S4NHHQxXbM7rYNDTRPMZsQiMgI8xvuUN5kerJzCSo8i%2B9lG7TwvedKJAvZkOC0R3veLHBHECMTMi8GmIOvaPLDUADcuDMYjYfWtt50ULFm3kjuT%2BmlK1HeXZ2crYNqkAJRqc8cOp6ygS%2BUTRJLlBVDSFTVF8oc1S52CZIbTin1hmqzPPaYb5LRrrjXjsNQnDTTI1Eub2wpvhRrP2CQXV1sWQDCM8qUqd8rwt5H%2Buq66uPtrVzR5D%2FNIodxvvkX4ZAQjmp3x9kOsUrFxqG4P7bzTXxAqy62226JC%2FVnAmx%2FEt7DNvcYYiDXnfTl0C4DEubRrhptJs8TjShPLm4CwqVW%2FLwiWEuh58MhJueerozA9F1JBG%2FGz18XxFj3zYdixGfGMlHAEmcMyMw5bqOvQY6pgFjnE0%2Fby03fcsrp2W%2FJ9r6NNigC0gys2oDQyI6Zcf53tUMlAxcrIaUrOulnaTO%2BVb0LfVzns7cxzM8toCdtGMSQK10ssVRUPLfR2CzqF4DGIEAejjnQxk8qqnL7OvxAh9gIf%2F%2BZ9MYkxR8DaUlwkrE29yQlZtC0lwtFJQcEEXFq%2Fr548EqIZ4wu%2FhSzKwVzrKRgUOSA9SgISgWAmnI%2BY%2FFkO8F3BiZ&X-Amz-Signature=619e65b3aa1d46ee69b9055973a055d3900974d6f7a0c82d1f897a746ace0736&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AQ3IBTB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCrweqey%2F1aBDuEUlmDU8Be%2Fxvgggqnin%2B3Do8DRYLirgIgYHfLmVtLYEayzf4SIUplWJRhN9UxIjurZf%2FODEplMV8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHzpaKYxPXfCJ4gSJircAy0GIf10r10oqztq7u%2FIOL5QRQxzdWf2gssmjdVSvECdQAUnqUBRg5EMOBRqxaea2olFNn8Ucr6NyQE0%2F9%2FvCrXdBjEhYpEHBpvxNnaX1EFoyNBjxB7rHWfSifuTACxR7n%2FqPp9oXADe2r03bJWfuvXLOfCDzKoNjfhCS244MAOxdzT8MYj6Qj4ecgQSr8mtqSFpEL9HIJQP%2FauljXhE2ws0TKn2xbJbki%2Fqhf9e00y5twiSL756bfqzjAd566uXzhnHWFNpyWAAXISbV1B4jW56t%2Bswe7eteb3soJKn%2Bsrda1d7LF0ocE33aBrkXJsnFVTRLUZ7ahWQOuiT6zURueXJp2JOaaBr5ngNs56zXl5%2BfWrCF3%2BMd7ezY8qld7veACfZJWSX5P3qCuMgnZsk3%2FSwhtQveRUW1SPtbGyZj1F8nR1tI7WilaWizRA9iOT1hPjhoXwFUSRdX6JYceqIdNpzU%2Bqc1RkKljDbwg0tDoDoK2BWN5penMWUrYTY%2FPhnWxLd956yq5JLU2Z%2FWyaVc4GMFyuKIgeIy%2FiA37%2BjRiolEEDLzuh%2BW47N74bFZhdAbkHxkRDxAdocGzFQeTIy6Fk5TdvW4fn7%2B9CQGdxP74R00C71POKlaPF%2FGYBKMPK6jr0GOqUBZoLHyQ%2BRN2POpkUmnQ5KphzU5%2BDm8gDwvpBa0bWkEJ71W9zyawQov8u%2BSNVT5s5r5SmGKSHJ3eynWGX012zYwu9qccSey5v74Iq%2Fyzs6txGbOGUGPFhu16mBb5q2qpiv%2BgiQiP9pF0Nm6t3rxcxLl0ifsrOW%2B1XPLbdgCKw99aMa%2B%2BMS%2FRRL7kmyemHKYb2LDjxwfvv%2FTv5rYANza4egJb0dwrem&X-Amz-Signature=db50984c47f625d5f04c576b863e68371f9369bf65b8fab7033c24238c1239b8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AQ3IBTB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCrweqey%2F1aBDuEUlmDU8Be%2Fxvgggqnin%2B3Do8DRYLirgIgYHfLmVtLYEayzf4SIUplWJRhN9UxIjurZf%2FODEplMV8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHzpaKYxPXfCJ4gSJircAy0GIf10r10oqztq7u%2FIOL5QRQxzdWf2gssmjdVSvECdQAUnqUBRg5EMOBRqxaea2olFNn8Ucr6NyQE0%2F9%2FvCrXdBjEhYpEHBpvxNnaX1EFoyNBjxB7rHWfSifuTACxR7n%2FqPp9oXADe2r03bJWfuvXLOfCDzKoNjfhCS244MAOxdzT8MYj6Qj4ecgQSr8mtqSFpEL9HIJQP%2FauljXhE2ws0TKn2xbJbki%2Fqhf9e00y5twiSL756bfqzjAd566uXzhnHWFNpyWAAXISbV1B4jW56t%2Bswe7eteb3soJKn%2Bsrda1d7LF0ocE33aBrkXJsnFVTRLUZ7ahWQOuiT6zURueXJp2JOaaBr5ngNs56zXl5%2BfWrCF3%2BMd7ezY8qld7veACfZJWSX5P3qCuMgnZsk3%2FSwhtQveRUW1SPtbGyZj1F8nR1tI7WilaWizRA9iOT1hPjhoXwFUSRdX6JYceqIdNpzU%2Bqc1RkKljDbwg0tDoDoK2BWN5penMWUrYTY%2FPhnWxLd956yq5JLU2Z%2FWyaVc4GMFyuKIgeIy%2FiA37%2BjRiolEEDLzuh%2BW47N74bFZhdAbkHxkRDxAdocGzFQeTIy6Fk5TdvW4fn7%2B9CQGdxP74R00C71POKlaPF%2FGYBKMPK6jr0GOqUBZoLHyQ%2BRN2POpkUmnQ5KphzU5%2BDm8gDwvpBa0bWkEJ71W9zyawQov8u%2BSNVT5s5r5SmGKSHJ3eynWGX012zYwu9qccSey5v74Iq%2Fyzs6txGbOGUGPFhu16mBb5q2qpiv%2BgiQiP9pF0Nm6t3rxcxLl0ifsrOW%2B1XPLbdgCKw99aMa%2B%2BMS%2FRRL7kmyemHKYb2LDjxwfvv%2FTv5rYANza4egJb0dwrem&X-Amz-Signature=1a42273ac8240322632836d84a9dcfbb66b6394a52679935613dc394e524667b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AQ3IBTB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCrweqey%2F1aBDuEUlmDU8Be%2Fxvgggqnin%2B3Do8DRYLirgIgYHfLmVtLYEayzf4SIUplWJRhN9UxIjurZf%2FODEplMV8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHzpaKYxPXfCJ4gSJircAy0GIf10r10oqztq7u%2FIOL5QRQxzdWf2gssmjdVSvECdQAUnqUBRg5EMOBRqxaea2olFNn8Ucr6NyQE0%2F9%2FvCrXdBjEhYpEHBpvxNnaX1EFoyNBjxB7rHWfSifuTACxR7n%2FqPp9oXADe2r03bJWfuvXLOfCDzKoNjfhCS244MAOxdzT8MYj6Qj4ecgQSr8mtqSFpEL9HIJQP%2FauljXhE2ws0TKn2xbJbki%2Fqhf9e00y5twiSL756bfqzjAd566uXzhnHWFNpyWAAXISbV1B4jW56t%2Bswe7eteb3soJKn%2Bsrda1d7LF0ocE33aBrkXJsnFVTRLUZ7ahWQOuiT6zURueXJp2JOaaBr5ngNs56zXl5%2BfWrCF3%2BMd7ezY8qld7veACfZJWSX5P3qCuMgnZsk3%2FSwhtQveRUW1SPtbGyZj1F8nR1tI7WilaWizRA9iOT1hPjhoXwFUSRdX6JYceqIdNpzU%2Bqc1RkKljDbwg0tDoDoK2BWN5penMWUrYTY%2FPhnWxLd956yq5JLU2Z%2FWyaVc4GMFyuKIgeIy%2FiA37%2BjRiolEEDLzuh%2BW47N74bFZhdAbkHxkRDxAdocGzFQeTIy6Fk5TdvW4fn7%2B9CQGdxP74R00C71POKlaPF%2FGYBKMPK6jr0GOqUBZoLHyQ%2BRN2POpkUmnQ5KphzU5%2BDm8gDwvpBa0bWkEJ71W9zyawQov8u%2BSNVT5s5r5SmGKSHJ3eynWGX012zYwu9qccSey5v74Iq%2Fyzs6txGbOGUGPFhu16mBb5q2qpiv%2BgiQiP9pF0Nm6t3rxcxLl0ifsrOW%2B1XPLbdgCKw99aMa%2B%2BMS%2FRRL7kmyemHKYb2LDjxwfvv%2FTv5rYANza4egJb0dwrem&X-Amz-Signature=d134e9bf90b29a9644107be7b3beee28cb399a38b41cd8c2eaa604a4ac8680b3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUFNNCP7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGOMDGOLKv6%2Fu3belWf46IxcA%2BYB5Y297wfyGPgAVGF0AiEA1VjoenJfPxdoLqHpKXBmePkHailybQWV4z4upZWBn3sq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDMXSDT%2BSE3vnHnSNdircA8fQ8KeD7Hxs6fuon2O%2Fv5SgPa3ez2EKuiqMysqssHvO3OCR%2BA7nhKnek4%2BOOKOLET6l2AXUhowHulnMnC8V655b5lKBrLQ7U4ORKZl9zJMY3X74LNq0tMgTLqj287fDAEeU2Ad1X5Ln0SONfK4ItlbRRK3MFNTPQ2lS9ENNVPkJIcdzeupYJjuTI%2FBhzoTUh3FgrPK0Z2PfkddUWHRzZAYQX%2FNO%2BKCIVbGE5Nd9w4Gpz8Fr%2F%2FT159RoOtxIZop8ZLgLWWHbm1VdELl5ukICw4KKyH4zvOmxf5Ygz6AYgS1nQGyrRXYjDqHpkvq5uX3UuhIvOHCN3FAYjFNUIwAjA8SBodrMkXABnhRx8NMOBf%2FvRsVjZT32zD6dmcoERtb3S5OqUQ5l2Sgrohy5QUIIIwk%2FLOr%2F5z9pryemm0EPJ4rqKIWk1YwpBlEoqJySZDddP9M9FnhX%2BFmU8M6F69cOy48o4wGXTctGGe8DMEhJ58toPfSzR97a44eBMk0PPpOVCGoDEXyJ7aQxI7eRsfy%2Bu036ldfYK9USo3ZaH%2FKDm84TngSR6vowyRrfx3ejJwRO%2F8t54c%2Bm2p2L4R3H%2FS0HvwPIdi%2Bss7HXASB8tzJvxypDxfAkqdQGZyUU7tk6MOW6jr0GOqUBKfq7%2FuQLe7SZKkfv9dQHAoNefyqHzSn7TjjBnFfcjhNRqblcrUVucEnldJx5YD2BBnq9XRisyta5q3%2FrHCaGK%2F3ghIcNI1PAj2F7jsMBW5VNnZE2nuEs9ySI0jiY0%2BGkjfcPj2mwOZUnf5N2DgCRNvKtRfE%2B3qH48cCOTV7peIvBu6JOcGQcMlOnc3eoF17c7hrz3kymjxXg4kFvc%2FeRdwwstySo&X-Amz-Signature=c8206b947c459f485dcb716c70d237e16dd30c88917dfce59196f65fdc5fb798&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRIWQFCM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQC5XU%2BytRNmW8f6WjwRGXEANOwJ%2BhR1s5wxPSUPZwKmOgIgOBh3SKNXyl4d1zhO9TbZ8l7wmjBjum3QmroxRJXxed8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI2%2FvDXhYntEO8YbYyrcA2ZlmgOSa%2BtfcUfu149WvJosurvqyUlViC9YxHn%2FOgzVubud7dqFdJjGwFGqcW6NwcDVXDHOu7TLca3408OOK6FgDf52sEZQI08eJTermetAXDsRjVoHaXM1p1T4SYEhknJWtXcUGrbqY3BEy8%2BPxL2tZSL6QDYQ48pIr1b6MYX9LgsoMc3nAsMHiiDY0zfPPbXp1X80ePCeXVqBaJPjoyGsLMJGHo7Q%2FhwIl8UfPCH8BHHknHDzgIiy8yRnVMkk9wISDMW3Zkg54b3Vuzju1dQaYKU8Qijf4lJnDLIdQiTm4XbdxGvacwgmD2fst8UuzJiCi7ZNT0SxkPsg0af1C4SIYKnYHP9JTvvPHpeLdEZx0mPSZG6k8siRpmgYA%2FZbI2VHS2KQ848a7Rq%2BhIa1zcXj%2BQUzwqxT%2BmvrCZnuEsopM4bTZaMd38hZ33rOKV%2FiAShL%2BMBdyShRcwoP3K1HkvUUYR2oJSGSyKwLO%2F5RPfB319Gfo43GN6yFZMGhy2qCCGeAl9tzrxv0jY%2BRYH0l%2Bt5UX0g6IfiYqzGBh21YTqGomaOb4tAfwk1XpgWeM9XQOHWonEdkxT5brqc%2FtbVE53Rr1ZTGlJf5sOp5FBn2qq4TxW%2F8osSbdOQyhMP1MLm6jr0GOqUBwvZghelQsUiZZWYyp5K0ZeK03nwA75cwKQ4quFauzX9r%2BhLk7jeCXcwm6Q9y9g1mk2Snohn4uLuZhvbhoXmcL7xP6AiPEE0fPIF9hDqWhi%2FbzhQnlgfZ3GU0gtGNvv3oKBJedo5d2Z4s712bTXy2GdToWOgAiX8mAIaYjMR6KiGZaDuq2cgEyS6%2FgPUlN0wciwIvvKmdst1gfOybARFTBBenUSSx&X-Amz-Signature=7afdfea4e2fa97c7e07d68e52ccdce15de1f80760b8e75231875edbe60204aed&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ESNOEGN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCIdyuILf%2FpL65AhxMmnFXS3Utr8pundMUk7JdoTTyMJAIhAOyW%2FMalq8hBYRsd%2F8Moi1bnutTcELDOpKl3cTQzwQkTKv8DCEoQABoMNjM3NDIzMTgzODA1Igycu%2FqO1u8dsZO7oZAq3AMT4ri9A%2Fm1JxYkivyGYME4pQ5CKdbjPkNokiU7YyVqkATatPYeLCvc9K1BC3x1wYtBFGlhv0LMOrZR3gYmnt20HAB0QTrFasozIyNRJKVhaW7EC9GN5l5yoUWYHwzPKqJ3L%2BXU%2BHJCnEBSDvv42g8L4BF2bHQcz%2Bws%2BkgZz%2FeBZkpgznXqdutjLHLEZ6zpmgf%2FViWY1Gtt6LoejXOLFq9vAQ7phv2JkN3PXqPRYARJyvRHHIhu4ljt%2BaVQ6PqBeFNENiFZy7DztbLhqKYGb214rgjuaB7AaccOkXfuAAolxABb1PwZz8uTW8qKIlqyrANDhFKb3IPfD3cDpTrYDGcrBFH9DHBrLnwPlGML9P%2Bx2tQQcQKoHkuTAE3NY%2FOhdAiMh35EgWNJSVIjVCFYn1g5Qx%2BHM21GcWOI2sca1nW2dY%2Furysmg02wOYw7CyIe%2BU%2FcrQ%2F8ysYW1mqVQoa6X4J8mWZ2f64M8sF2mECBs2xxKzmWwlqH4xjy8JECT4XzpjPuuZ0ka7PMnaeMJMLzLKaeUUu340E5iuZABDyrUcK6MbwmBK1dWp1HHpAgHJODL7b3nQCupQxykVjDGIIG7oBVRyP9xI9ukDmNiWJVylVWMvXxPl5pg%2Bl%2F1qBOcjDHuo69BjqkATlzBNjyNItKLPoTZm6Pw6prpUanTLnNGWJa7LaDouCwSDX56y6wvxHo1GcM6rAQp49fG7qS5YZAbDlxqN4PZv685vIv0r9kWOmb7qzkyGOL9K7lRLfQL3l%2BM781gJiyXYdCgbq1kYfrDwN%2Fz%2F1T1Z%2FCDdlF2DUw6VAiwRFxoQWnEoth8eDjLITVyw6RrKTHBxADTLZY9869rXoeIbe917cUfPqe&X-Amz-Signature=3cc74166b7b80cfbc80feac1b306f015f417fedadd84b62e3f92feb06e577005&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGOXFD72%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCICBFLuKBUFUrxlU6A7QVmSNpn%2F4BM8mXyw%2Ff0PnPzfqHAiA3QuimlKtWBKxDP3oEegRly1Or6UtAYDfN3bNdVO3Loyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMHK0K5G0DLRXT28GnKtwDl7QQlO86CHP2HVQu7zNxhBdjnxYFyUXbJd9a7pf9%2BSKUYy4dYZV8QHkWhpYg%2FVl5O0fJ289TChSW60EPRE4ZH0eFQc4oY%2FT0I5gwa12TIosYzPFTtolADajA%2F%2Ft%2FdCbtvDw6wHTbmRwX3Y1jpdrlWhSXE1H6bJutrUgah616SsrP2jNkXXAOFxHoIWFk7rFsDeyN%2BWL2T0KPhBdeBKDCn7z1v2DTFsRTlpHey9nDyuQPLKRTE93dqto9z2gFm3FvYAESEuF8NDXJNx3KHio4KFgicRJMbzXTn7cfsVhgn2mEuK9kDeR2En%2Fw2jYWWEBfMFY9LU4kJMxVANRyOSWYU69tCmLeIZOnWy8tlwrWNZkmPum71RkgJ2qld9M%2Fq76xcDdirsP1ZhyjtdE5hrcHNnUbAksrI80hlsPmlF7Sio5RKa9dLC52FNA2A7ZvWm%2Bz8Y%2BzXXibF2CODuLIXsKuaJd6eyxYbZELAVXEi4gXmX8KYJLYXDMy7rsE7jKsm2tdr9qtgkmWrLq26famuNK0UqRZd2XtUYWNwI38bNnz5aXpti1KFWN0hQanY4v8pcKl1mdb8EV8qAWNsSPLCFwYluio4uOw%2BYDiIT26PEC2KJVKgfzCv2BmzmSL0Now9bqOvQY6pgFzxTBCCqSE1ou4GAE64hrJMqAiSE%2FiHzak7TMauwFGP6v%2BP5UknkXaKpE%2B9XiVK0c0X3KnkwijrKhQ37vNofzQ9L7EiiALowBEf2Z%2BAejMWYsy2Ftal%2BU5oJq7RVxiK2YiRWPAnzq8Tx7MfYH%2FC5deALapbGuMiXj0LL5rXbGcBCROx7TKOfgjhe37a2Z9vzgMKyrc3E0oLKHOPRax0csMCLGmque2&X-Amz-Signature=d6cf6599cd4f37c81552926498c8a245a713174226205cde122bd94c5553f753&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGOXFD72%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCICBFLuKBUFUrxlU6A7QVmSNpn%2F4BM8mXyw%2Ff0PnPzfqHAiA3QuimlKtWBKxDP3oEegRly1Or6UtAYDfN3bNdVO3Loyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMHK0K5G0DLRXT28GnKtwDl7QQlO86CHP2HVQu7zNxhBdjnxYFyUXbJd9a7pf9%2BSKUYy4dYZV8QHkWhpYg%2FVl5O0fJ289TChSW60EPRE4ZH0eFQc4oY%2FT0I5gwa12TIosYzPFTtolADajA%2F%2Ft%2FdCbtvDw6wHTbmRwX3Y1jpdrlWhSXE1H6bJutrUgah616SsrP2jNkXXAOFxHoIWFk7rFsDeyN%2BWL2T0KPhBdeBKDCn7z1v2DTFsRTlpHey9nDyuQPLKRTE93dqto9z2gFm3FvYAESEuF8NDXJNx3KHio4KFgicRJMbzXTn7cfsVhgn2mEuK9kDeR2En%2Fw2jYWWEBfMFY9LU4kJMxVANRyOSWYU69tCmLeIZOnWy8tlwrWNZkmPum71RkgJ2qld9M%2Fq76xcDdirsP1ZhyjtdE5hrcHNnUbAksrI80hlsPmlF7Sio5RKa9dLC52FNA2A7ZvWm%2Bz8Y%2BzXXibF2CODuLIXsKuaJd6eyxYbZELAVXEi4gXmX8KYJLYXDMy7rsE7jKsm2tdr9qtgkmWrLq26famuNK0UqRZd2XtUYWNwI38bNnz5aXpti1KFWN0hQanY4v8pcKl1mdb8EV8qAWNsSPLCFwYluio4uOw%2BYDiIT26PEC2KJVKgfzCv2BmzmSL0Now9bqOvQY6pgFzxTBCCqSE1ou4GAE64hrJMqAiSE%2FiHzak7TMauwFGP6v%2BP5UknkXaKpE%2B9XiVK0c0X3KnkwijrKhQ37vNofzQ9L7EiiALowBEf2Z%2BAejMWYsy2Ftal%2BU5oJq7RVxiK2YiRWPAnzq8Tx7MfYH%2FC5deALapbGuMiXj0LL5rXbGcBCROx7TKOfgjhe37a2Z9vzgMKyrc3E0oLKHOPRax0csMCLGmque2&X-Amz-Signature=d4073c43160e6b1d9f6247d29623da9972bf79892f62d50157b586f9798fc860&X-Amz-SignedHeaders=host&x-id=GetObject)

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
