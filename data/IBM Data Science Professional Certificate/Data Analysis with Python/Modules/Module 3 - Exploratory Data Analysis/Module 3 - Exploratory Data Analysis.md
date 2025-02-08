

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIV4LY5X%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIGnOfquBiXp6g5gdBLwYkBl7oy9vWZI5OyNa0VQErCgHAiARQAUuX1DJ0Oct3k8%2BOdZimCymzPpgFVjhP2XU7nbUsyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYtvQLAcTxJlcf4u5KtwDqLFtB%2BEPRX1PCoQc0yrFype6e%2Brk6BZGnnmbqwEzYojVlqPPlRXAb13Ef%2BqyzBYjzMTmGkCGmklTrZdVuT3MytyrY0tpPQLk5NXOMLg%2FRsSLDlhDQO%2FxaHKcMDMVecvZZdL6fIr6JC3ltnXgqjITMFyxlhZwD%2By1cQNbmPbEBwIhX0klg9ukU6U0KPTHPEPi5TmZin8PFYFyhkjVfe3Mr8BmnWKd8GkmrGJkqHPLEhGsGkZwT0IGi1KaZ3edl4Oxg0jnlvEMXcxPfGfcJofIRwqxZfRGcQKyECnUtxV5Ds%2BMcRdR6ei9Y1F8B5O5Riq43clNV%2FGe7ikVBjmoka8zDuoIHxzDhCSvUgKQuVBcO9BmcoO5z6M%2F2T2SW75iSisytVBJQLmLF3DDCcCJeqe%2FdVOhwb2kuzWybQnLZ4Mejzn5WDaNTD5jSY8oSlrveRVHfnqRdgaTHy8nM4oLFrKCNdAyP%2B4onbTt91ymm%2BldNrnEBKgYXk7AueGTUF5FIVInLM2%2BxLLyjPI6jNSKk8RGMKzTTnYnZgs%2Fdx9K%2BJcnGs4yRMlZlkNuZHAomU0WJoSf6%2FDQkyymwXh2mR09kvFsQEaC5YIJniW2ok0iMbQ9G5Pdb08mDdXPZIkeHx0wkoWdvQY6pgGjtnNp%2F9Q3Ry9fadYMoTgCRhLjG9djPGwvUXNyAkqHlR4RpBLugeOK5HQNgZ%2FzpQdmsvt5jx17xkrBi4d8TyuclS6bvXDB66V5KU%2FbLQzJin86Palqch7lcS2Px7nkCmryY8qET0%2FeYPR%2BN47Qj07BgErBLDmwk2xk30wVYwDe6UfCQhwnpVl9C318G5oUR4e71sBjvjuJfVyIrrfXJvJxHfXN000d&X-Amz-Signature=8ab7874558268ce90dc1803dc6c99f82b683642f3167d46777a520b6a8282016&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIV4LY5X%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIGnOfquBiXp6g5gdBLwYkBl7oy9vWZI5OyNa0VQErCgHAiARQAUuX1DJ0Oct3k8%2BOdZimCymzPpgFVjhP2XU7nbUsyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYtvQLAcTxJlcf4u5KtwDqLFtB%2BEPRX1PCoQc0yrFype6e%2Brk6BZGnnmbqwEzYojVlqPPlRXAb13Ef%2BqyzBYjzMTmGkCGmklTrZdVuT3MytyrY0tpPQLk5NXOMLg%2FRsSLDlhDQO%2FxaHKcMDMVecvZZdL6fIr6JC3ltnXgqjITMFyxlhZwD%2By1cQNbmPbEBwIhX0klg9ukU6U0KPTHPEPi5TmZin8PFYFyhkjVfe3Mr8BmnWKd8GkmrGJkqHPLEhGsGkZwT0IGi1KaZ3edl4Oxg0jnlvEMXcxPfGfcJofIRwqxZfRGcQKyECnUtxV5Ds%2BMcRdR6ei9Y1F8B5O5Riq43clNV%2FGe7ikVBjmoka8zDuoIHxzDhCSvUgKQuVBcO9BmcoO5z6M%2F2T2SW75iSisytVBJQLmLF3DDCcCJeqe%2FdVOhwb2kuzWybQnLZ4Mejzn5WDaNTD5jSY8oSlrveRVHfnqRdgaTHy8nM4oLFrKCNdAyP%2B4onbTt91ymm%2BldNrnEBKgYXk7AueGTUF5FIVInLM2%2BxLLyjPI6jNSKk8RGMKzTTnYnZgs%2Fdx9K%2BJcnGs4yRMlZlkNuZHAomU0WJoSf6%2FDQkyymwXh2mR09kvFsQEaC5YIJniW2ok0iMbQ9G5Pdb08mDdXPZIkeHx0wkoWdvQY6pgGjtnNp%2F9Q3Ry9fadYMoTgCRhLjG9djPGwvUXNyAkqHlR4RpBLugeOK5HQNgZ%2FzpQdmsvt5jx17xkrBi4d8TyuclS6bvXDB66V5KU%2FbLQzJin86Palqch7lcS2Px7nkCmryY8qET0%2FeYPR%2BN47Qj07BgErBLDmwk2xk30wVYwDe6UfCQhwnpVl9C318G5oUR4e71sBjvjuJfVyIrrfXJvJxHfXN000d&X-Amz-Signature=040b9d1e62ca2fd2df54fdd7d7c086389b97b41c19ee6932161e3ebf23b280e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIV4LY5X%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIGnOfquBiXp6g5gdBLwYkBl7oy9vWZI5OyNa0VQErCgHAiARQAUuX1DJ0Oct3k8%2BOdZimCymzPpgFVjhP2XU7nbUsyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYtvQLAcTxJlcf4u5KtwDqLFtB%2BEPRX1PCoQc0yrFype6e%2Brk6BZGnnmbqwEzYojVlqPPlRXAb13Ef%2BqyzBYjzMTmGkCGmklTrZdVuT3MytyrY0tpPQLk5NXOMLg%2FRsSLDlhDQO%2FxaHKcMDMVecvZZdL6fIr6JC3ltnXgqjITMFyxlhZwD%2By1cQNbmPbEBwIhX0klg9ukU6U0KPTHPEPi5TmZin8PFYFyhkjVfe3Mr8BmnWKd8GkmrGJkqHPLEhGsGkZwT0IGi1KaZ3edl4Oxg0jnlvEMXcxPfGfcJofIRwqxZfRGcQKyECnUtxV5Ds%2BMcRdR6ei9Y1F8B5O5Riq43clNV%2FGe7ikVBjmoka8zDuoIHxzDhCSvUgKQuVBcO9BmcoO5z6M%2F2T2SW75iSisytVBJQLmLF3DDCcCJeqe%2FdVOhwb2kuzWybQnLZ4Mejzn5WDaNTD5jSY8oSlrveRVHfnqRdgaTHy8nM4oLFrKCNdAyP%2B4onbTt91ymm%2BldNrnEBKgYXk7AueGTUF5FIVInLM2%2BxLLyjPI6jNSKk8RGMKzTTnYnZgs%2Fdx9K%2BJcnGs4yRMlZlkNuZHAomU0WJoSf6%2FDQkyymwXh2mR09kvFsQEaC5YIJniW2ok0iMbQ9G5Pdb08mDdXPZIkeHx0wkoWdvQY6pgGjtnNp%2F9Q3Ry9fadYMoTgCRhLjG9djPGwvUXNyAkqHlR4RpBLugeOK5HQNgZ%2FzpQdmsvt5jx17xkrBi4d8TyuclS6bvXDB66V5KU%2FbLQzJin86Palqch7lcS2Px7nkCmryY8qET0%2FeYPR%2BN47Qj07BgErBLDmwk2xk30wVYwDe6UfCQhwnpVl9C318G5oUR4e71sBjvjuJfVyIrrfXJvJxHfXN000d&X-Amz-Signature=74478f273e01959adaa66bb81b591b364da2b37431a5ce0e42c37263be560e3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRJ57DZG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIATXA3Ua%2Ffg2TyTrWGPAE0aykBDeBVa9EffL0xNAjLS6AiEA3A07yJWZHcEe23F8YYsecjEG3ElOIwACLBPITiQIKzUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2hKazXEb1W5MUrPSrcA6kJFAPfO0esT7VSaMLhd6d6FxJQR1v8pxK8QgcwyW5LmOubMsienm9GnaVrzcxn9x3IKVSBv9pKXpuoiSNjsxFbq8e4Dk2Uk7KMGPlEHJmvxSGajdSOh0gNc0jw5H3hNmy5CTEwLRNlfdONq5boDnHHVZ15Qmf4Sx7%2By5Sd25%2FC9A13DQsvEZ6LuI6yyDa8AKMxJOxOCDu5THj1MjgWqoDWwFCGJnfdIlPLrZDvgeUnQVDNxWa4GqAp3b0JhUmFP3wvBNOhCYJNW743Xr%2FXjHyXsfxKy%2BH7n2y1jk0Ix8g1pmz6wqcvgy%2FVQPCjMXluKWiVzMnWpeEgcne4WlYEaWgEI6LkiralxedZWflOxK5wDbIN8jjsN3q4AuXirU2f8ABgVxMTF9IcMS0boqpW6ppAB%2FJxkHpiwcFZEN%2F0XSzjFJyt2c6hfjhxemd9gi3lv1xzlk%2B5tqUCLh071uI61nqCT2vJmQkBuUL2y4uBz5RIR4qvnBXTaVC%2FsCyzrjViQNvEFgZr4rj8DQ4lMZM6N0k1whCELtwdYAsFQF3ZMnVzwc%2FMPpWLIgsdnkm3rGUe5K79%2ByGU72vIb0aL%2B30eoF3sfiOgc0zgMtseQfQXayKFslRZq5a8nZN7yT6FMMiFnb0GOqUBTkQxOcKvm883tOgYGuN0%2Fd4jnwRyX6gY0uJq3TyYuizHINNbeyMmq8MoZe6Zemd2GrHQIKACu4%2FYprycfYqKgXlWaZSuQ5BXp0MXjBqH5lmDwDO6dYWonSL6tRveksbwLy1ZgghC89NEZJqRKlIEafqgrt3YA27xhDCJEI59lC5BLOjS%2FjK6WgBZnfNle%2BtkBFj236MFtTkMYeuAvDyQXP6qHll6&X-Amz-Signature=311869ad85e587dd6aedd1c22d903373e035af2b015f508fd01185dcbce34988&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRJ57DZG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIATXA3Ua%2Ffg2TyTrWGPAE0aykBDeBVa9EffL0xNAjLS6AiEA3A07yJWZHcEe23F8YYsecjEG3ElOIwACLBPITiQIKzUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2hKazXEb1W5MUrPSrcA6kJFAPfO0esT7VSaMLhd6d6FxJQR1v8pxK8QgcwyW5LmOubMsienm9GnaVrzcxn9x3IKVSBv9pKXpuoiSNjsxFbq8e4Dk2Uk7KMGPlEHJmvxSGajdSOh0gNc0jw5H3hNmy5CTEwLRNlfdONq5boDnHHVZ15Qmf4Sx7%2By5Sd25%2FC9A13DQsvEZ6LuI6yyDa8AKMxJOxOCDu5THj1MjgWqoDWwFCGJnfdIlPLrZDvgeUnQVDNxWa4GqAp3b0JhUmFP3wvBNOhCYJNW743Xr%2FXjHyXsfxKy%2BH7n2y1jk0Ix8g1pmz6wqcvgy%2FVQPCjMXluKWiVzMnWpeEgcne4WlYEaWgEI6LkiralxedZWflOxK5wDbIN8jjsN3q4AuXirU2f8ABgVxMTF9IcMS0boqpW6ppAB%2FJxkHpiwcFZEN%2F0XSzjFJyt2c6hfjhxemd9gi3lv1xzlk%2B5tqUCLh071uI61nqCT2vJmQkBuUL2y4uBz5RIR4qvnBXTaVC%2FsCyzrjViQNvEFgZr4rj8DQ4lMZM6N0k1whCELtwdYAsFQF3ZMnVzwc%2FMPpWLIgsdnkm3rGUe5K79%2ByGU72vIb0aL%2B30eoF3sfiOgc0zgMtseQfQXayKFslRZq5a8nZN7yT6FMMiFnb0GOqUBTkQxOcKvm883tOgYGuN0%2Fd4jnwRyX6gY0uJq3TyYuizHINNbeyMmq8MoZe6Zemd2GrHQIKACu4%2FYprycfYqKgXlWaZSuQ5BXp0MXjBqH5lmDwDO6dYWonSL6tRveksbwLy1ZgghC89NEZJqRKlIEafqgrt3YA27xhDCJEI59lC5BLOjS%2FjK6WgBZnfNle%2BtkBFj236MFtTkMYeuAvDyQXP6qHll6&X-Amz-Signature=a8bcebf6cc73aeb77ee8ad6271fe1f53801ddf318aab30aa373bc535d390daa7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRJ57DZG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIATXA3Ua%2Ffg2TyTrWGPAE0aykBDeBVa9EffL0xNAjLS6AiEA3A07yJWZHcEe23F8YYsecjEG3ElOIwACLBPITiQIKzUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2hKazXEb1W5MUrPSrcA6kJFAPfO0esT7VSaMLhd6d6FxJQR1v8pxK8QgcwyW5LmOubMsienm9GnaVrzcxn9x3IKVSBv9pKXpuoiSNjsxFbq8e4Dk2Uk7KMGPlEHJmvxSGajdSOh0gNc0jw5H3hNmy5CTEwLRNlfdONq5boDnHHVZ15Qmf4Sx7%2By5Sd25%2FC9A13DQsvEZ6LuI6yyDa8AKMxJOxOCDu5THj1MjgWqoDWwFCGJnfdIlPLrZDvgeUnQVDNxWa4GqAp3b0JhUmFP3wvBNOhCYJNW743Xr%2FXjHyXsfxKy%2BH7n2y1jk0Ix8g1pmz6wqcvgy%2FVQPCjMXluKWiVzMnWpeEgcne4WlYEaWgEI6LkiralxedZWflOxK5wDbIN8jjsN3q4AuXirU2f8ABgVxMTF9IcMS0boqpW6ppAB%2FJxkHpiwcFZEN%2F0XSzjFJyt2c6hfjhxemd9gi3lv1xzlk%2B5tqUCLh071uI61nqCT2vJmQkBuUL2y4uBz5RIR4qvnBXTaVC%2FsCyzrjViQNvEFgZr4rj8DQ4lMZM6N0k1whCELtwdYAsFQF3ZMnVzwc%2FMPpWLIgsdnkm3rGUe5K79%2ByGU72vIb0aL%2B30eoF3sfiOgc0zgMtseQfQXayKFslRZq5a8nZN7yT6FMMiFnb0GOqUBTkQxOcKvm883tOgYGuN0%2Fd4jnwRyX6gY0uJq3TyYuizHINNbeyMmq8MoZe6Zemd2GrHQIKACu4%2FYprycfYqKgXlWaZSuQ5BXp0MXjBqH5lmDwDO6dYWonSL6tRveksbwLy1ZgghC89NEZJqRKlIEafqgrt3YA27xhDCJEI59lC5BLOjS%2FjK6WgBZnfNle%2BtkBFj236MFtTkMYeuAvDyQXP6qHll6&X-Amz-Signature=512464211982b9c408d18ab38d6a61767cabb40eeb863f1d6751e4b2e96c72a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRJ57DZG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIATXA3Ua%2Ffg2TyTrWGPAE0aykBDeBVa9EffL0xNAjLS6AiEA3A07yJWZHcEe23F8YYsecjEG3ElOIwACLBPITiQIKzUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2hKazXEb1W5MUrPSrcA6kJFAPfO0esT7VSaMLhd6d6FxJQR1v8pxK8QgcwyW5LmOubMsienm9GnaVrzcxn9x3IKVSBv9pKXpuoiSNjsxFbq8e4Dk2Uk7KMGPlEHJmvxSGajdSOh0gNc0jw5H3hNmy5CTEwLRNlfdONq5boDnHHVZ15Qmf4Sx7%2By5Sd25%2FC9A13DQsvEZ6LuI6yyDa8AKMxJOxOCDu5THj1MjgWqoDWwFCGJnfdIlPLrZDvgeUnQVDNxWa4GqAp3b0JhUmFP3wvBNOhCYJNW743Xr%2FXjHyXsfxKy%2BH7n2y1jk0Ix8g1pmz6wqcvgy%2FVQPCjMXluKWiVzMnWpeEgcne4WlYEaWgEI6LkiralxedZWflOxK5wDbIN8jjsN3q4AuXirU2f8ABgVxMTF9IcMS0boqpW6ppAB%2FJxkHpiwcFZEN%2F0XSzjFJyt2c6hfjhxemd9gi3lv1xzlk%2B5tqUCLh071uI61nqCT2vJmQkBuUL2y4uBz5RIR4qvnBXTaVC%2FsCyzrjViQNvEFgZr4rj8DQ4lMZM6N0k1whCELtwdYAsFQF3ZMnVzwc%2FMPpWLIgsdnkm3rGUe5K79%2ByGU72vIb0aL%2B30eoF3sfiOgc0zgMtseQfQXayKFslRZq5a8nZN7yT6FMMiFnb0GOqUBTkQxOcKvm883tOgYGuN0%2Fd4jnwRyX6gY0uJq3TyYuizHINNbeyMmq8MoZe6Zemd2GrHQIKACu4%2FYprycfYqKgXlWaZSuQ5BXp0MXjBqH5lmDwDO6dYWonSL6tRveksbwLy1ZgghC89NEZJqRKlIEafqgrt3YA27xhDCJEI59lC5BLOjS%2FjK6WgBZnfNle%2BtkBFj236MFtTkMYeuAvDyQXP6qHll6&X-Amz-Signature=e4cacb789a5c91e175976211705a92500bd9481e39dda9fba9fcf2ad7e67113e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRJ57DZG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIATXA3Ua%2Ffg2TyTrWGPAE0aykBDeBVa9EffL0xNAjLS6AiEA3A07yJWZHcEe23F8YYsecjEG3ElOIwACLBPITiQIKzUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2hKazXEb1W5MUrPSrcA6kJFAPfO0esT7VSaMLhd6d6FxJQR1v8pxK8QgcwyW5LmOubMsienm9GnaVrzcxn9x3IKVSBv9pKXpuoiSNjsxFbq8e4Dk2Uk7KMGPlEHJmvxSGajdSOh0gNc0jw5H3hNmy5CTEwLRNlfdONq5boDnHHVZ15Qmf4Sx7%2By5Sd25%2FC9A13DQsvEZ6LuI6yyDa8AKMxJOxOCDu5THj1MjgWqoDWwFCGJnfdIlPLrZDvgeUnQVDNxWa4GqAp3b0JhUmFP3wvBNOhCYJNW743Xr%2FXjHyXsfxKy%2BH7n2y1jk0Ix8g1pmz6wqcvgy%2FVQPCjMXluKWiVzMnWpeEgcne4WlYEaWgEI6LkiralxedZWflOxK5wDbIN8jjsN3q4AuXirU2f8ABgVxMTF9IcMS0boqpW6ppAB%2FJxkHpiwcFZEN%2F0XSzjFJyt2c6hfjhxemd9gi3lv1xzlk%2B5tqUCLh071uI61nqCT2vJmQkBuUL2y4uBz5RIR4qvnBXTaVC%2FsCyzrjViQNvEFgZr4rj8DQ4lMZM6N0k1whCELtwdYAsFQF3ZMnVzwc%2FMPpWLIgsdnkm3rGUe5K79%2ByGU72vIb0aL%2B30eoF3sfiOgc0zgMtseQfQXayKFslRZq5a8nZN7yT6FMMiFnb0GOqUBTkQxOcKvm883tOgYGuN0%2Fd4jnwRyX6gY0uJq3TyYuizHINNbeyMmq8MoZe6Zemd2GrHQIKACu4%2FYprycfYqKgXlWaZSuQ5BXp0MXjBqH5lmDwDO6dYWonSL6tRveksbwLy1ZgghC89NEZJqRKlIEafqgrt3YA27xhDCJEI59lC5BLOjS%2FjK6WgBZnfNle%2BtkBFj236MFtTkMYeuAvDyQXP6qHll6&X-Amz-Signature=a92c8c18087a9a00fae140bbb4f04b2096108fc45ebdab3ec33158c946e11490&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRJ57DZG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIATXA3Ua%2Ffg2TyTrWGPAE0aykBDeBVa9EffL0xNAjLS6AiEA3A07yJWZHcEe23F8YYsecjEG3ElOIwACLBPITiQIKzUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2hKazXEb1W5MUrPSrcA6kJFAPfO0esT7VSaMLhd6d6FxJQR1v8pxK8QgcwyW5LmOubMsienm9GnaVrzcxn9x3IKVSBv9pKXpuoiSNjsxFbq8e4Dk2Uk7KMGPlEHJmvxSGajdSOh0gNc0jw5H3hNmy5CTEwLRNlfdONq5boDnHHVZ15Qmf4Sx7%2By5Sd25%2FC9A13DQsvEZ6LuI6yyDa8AKMxJOxOCDu5THj1MjgWqoDWwFCGJnfdIlPLrZDvgeUnQVDNxWa4GqAp3b0JhUmFP3wvBNOhCYJNW743Xr%2FXjHyXsfxKy%2BH7n2y1jk0Ix8g1pmz6wqcvgy%2FVQPCjMXluKWiVzMnWpeEgcne4WlYEaWgEI6LkiralxedZWflOxK5wDbIN8jjsN3q4AuXirU2f8ABgVxMTF9IcMS0boqpW6ppAB%2FJxkHpiwcFZEN%2F0XSzjFJyt2c6hfjhxemd9gi3lv1xzlk%2B5tqUCLh071uI61nqCT2vJmQkBuUL2y4uBz5RIR4qvnBXTaVC%2FsCyzrjViQNvEFgZr4rj8DQ4lMZM6N0k1whCELtwdYAsFQF3ZMnVzwc%2FMPpWLIgsdnkm3rGUe5K79%2ByGU72vIb0aL%2B30eoF3sfiOgc0zgMtseQfQXayKFslRZq5a8nZN7yT6FMMiFnb0GOqUBTkQxOcKvm883tOgYGuN0%2Fd4jnwRyX6gY0uJq3TyYuizHINNbeyMmq8MoZe6Zemd2GrHQIKACu4%2FYprycfYqKgXlWaZSuQ5BXp0MXjBqH5lmDwDO6dYWonSL6tRveksbwLy1ZgghC89NEZJqRKlIEafqgrt3YA27xhDCJEI59lC5BLOjS%2FjK6WgBZnfNle%2BtkBFj236MFtTkMYeuAvDyQXP6qHll6&X-Amz-Signature=e63d7f34497444de3c9061c575f35bd3f318187ef8b758b10c9691a6821520d3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQK32GVQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCFSoqj7HOnBkjKjW4smOGODFoV14ODhl1%2F0hoe2DXXugIhAMyUkVPAkqcRi%2BHCxEEB3bYMDCVEFbJWFJA7Kh4cjo7%2BKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6n5GgULuXtO%2B8pjQq3AM8tpCCx%2B%2BvDXUQTPEL4bDDyMw96fXSAeLn%2BJwbVfaWWFZsFzx2FU5NpRDOD4Vlfe9Mv9lmBOQWq84tVJ%2FvlxLeSFfczUieM0fJ%2BFNWWyoZ76VGWO2b2RoDknsoj9O8XmvksDTprV%2F6EIWc9jFJbmG89buDl084V6A051YQagWzvFHc%2FpUOtblDUA2OZ6Il7fyGnzinWJmTi1ta0Jih2LW7PMKeSL%2FxzhNnG70jaNB%2F6jR06J9z9lP0zcikNxKxafPLnxMoGRFUjTKhr3kqboyx0%2BoG2uvEOFXUWS8Fn1I2Mn571yPrfzp5QTRFtVLZw%2Bi1EeoQi%2F7T%2B%2BW9%2FAaKpJ0YpqKHLX3pyIGwWyJ%2BTewRfUK0Vp4mBh2wQovMOjTQYZXvnYzpYwdyC49oK8oKmCk%2B9mWrXSO6ZaDWO6hO7RDGzWHO51jsb3pDafxvmv%2FdbvBbCpnjUu2TGyorfcA%2FlkX%2BGzd04vrvHAHYsq%2Bt9k52HzYOJ%2FJ5GxPI9%2BHeW50K%2FucdGAfCN3dQkVNfS7KEX3UKx%2Fv1QIDnS%2F3Ht0L%2BcoSyFQe3Q9mkmfcNwnznCNFJTI4RhvCgb7tAmumL3Wspx5mZMRBujofGnK%2BF071g9romIuyAdxJT1ghBidohCDCJhZ29BjqkAZ6pIjaiCespJBcjZWGcAEDhVqhDiDZS87HO%2BsLG6FbhZEfPVJjR1lS2miCo1uBnJGnmeGDekVy7myZPwujQoyBYESze%2FpG6TCkX6ATA32ltRP8MuE8GuIG60wQ2NWPaVm%2BPnw4qRAcR5axHjJQ%2FBFpYT%2FyGfYPVCSXXspThKbobwlAmhLXmJEG%2BEApdOOH3yBjF4GJFjTkLpqXg5nXiyYdrsGKY&X-Amz-Signature=2157509553a67a2269ee588c030f9a93391ed5b436fe9ffb1c1d11efd74d6955&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2UXRCK3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCICfgnuOTNjHJxHjkxcgLJfP108gc8RRXXgcQ12l%2F0fZKAiBiMjyyPcZg1xkVyw27o9By6Tmy%2Fetq%2FFSUZ772P8UYmyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHjWYmi8vAdD%2BIcCgKtwD4a%2F9lixAxNHuBB2Mq%2Fq8mvh0kQma4exbv7xMrhXiounN9tHQsXvNRk66UHrxoML2mjIJJhEkotERTbtpsTq2c2DzII8D%2FFA8CnMffET%2BVvflVed8zpG3fZOcSs7ILur7BSE7Rbd%2FWUtdWjNALDfZQk8S%2BCGnow99ga6UwmLGt%2F2uxwoADk4AjoNEk7L47VyEfkMOI%2B4Af9DjZpdDn3C347RU%2FWTSNfwcfDwcRlaSoX%2FjU1z9wLTQKNl6pKIxoKcK2nQ7XbixLENFPn%2BvYSHChGMqgozAESN75CvzYbhco4mIXt0Sq9hvF%2B5XzLgAK%2F32Su1qsRB1YKFHVb18K5f1X0v8cKtVS8WcNB60YYKowW%2F6%2FjbzLYaIKTSszE3gYe%2BR192lAbZwNAy2UyY5nzp8oHjIIflXLhC9wipXHqMJD7ruOh2jLRyCzjyU%2BVLYfXMnLMTdYtTYxlGWD%2BgSbRTChlkieddvQXxTVAJR71mnvCUrAKs%2Bm3CSHGf6hz%2BXN6cZYjc0jp8%2B9lpc0xlgNYmkWIVO4p7AV9Y0lZxtL0olCROhFFpsLqfAiiVQ62LwSeAUwqATHFaAHcJYsDbRJsnfXi4AMGXzv3L%2BUIGhlzKSZYO6ZBEF3WVYzKCJ3JwwvYWdvQY6pgHVhRmsnCkHoczv%2FtoNAMVxp%2FOAr%2Bd%2FWVknPTIOqMz05zg9Mm8W%2F59%2FjKt94cSk9YGS92A7xLGxrNHjH3nQ5q%2F4xJHIclwc1PC5s4C8tDfpAEKYSDaGqSDW33edB7rnl2I%2FcFRyVaVIxUwlUNdJfx%2BRfZj%2BbarDifKRA74rsV1E0vx8GNkOyJbUKQ797z2UaPgmDhbdnCC9PrzzzdbOlpvKM7vZG%2Fdy&X-Amz-Signature=528242669dbd9359ec5fb40ad143710a79f2e1fbc631d092515d26d7b21f2c83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRJ57DZG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIATXA3Ua%2Ffg2TyTrWGPAE0aykBDeBVa9EffL0xNAjLS6AiEA3A07yJWZHcEe23F8YYsecjEG3ElOIwACLBPITiQIKzUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2hKazXEb1W5MUrPSrcA6kJFAPfO0esT7VSaMLhd6d6FxJQR1v8pxK8QgcwyW5LmOubMsienm9GnaVrzcxn9x3IKVSBv9pKXpuoiSNjsxFbq8e4Dk2Uk7KMGPlEHJmvxSGajdSOh0gNc0jw5H3hNmy5CTEwLRNlfdONq5boDnHHVZ15Qmf4Sx7%2By5Sd25%2FC9A13DQsvEZ6LuI6yyDa8AKMxJOxOCDu5THj1MjgWqoDWwFCGJnfdIlPLrZDvgeUnQVDNxWa4GqAp3b0JhUmFP3wvBNOhCYJNW743Xr%2FXjHyXsfxKy%2BH7n2y1jk0Ix8g1pmz6wqcvgy%2FVQPCjMXluKWiVzMnWpeEgcne4WlYEaWgEI6LkiralxedZWflOxK5wDbIN8jjsN3q4AuXirU2f8ABgVxMTF9IcMS0boqpW6ppAB%2FJxkHpiwcFZEN%2F0XSzjFJyt2c6hfjhxemd9gi3lv1xzlk%2B5tqUCLh071uI61nqCT2vJmQkBuUL2y4uBz5RIR4qvnBXTaVC%2FsCyzrjViQNvEFgZr4rj8DQ4lMZM6N0k1whCELtwdYAsFQF3ZMnVzwc%2FMPpWLIgsdnkm3rGUe5K79%2ByGU72vIb0aL%2B30eoF3sfiOgc0zgMtseQfQXayKFslRZq5a8nZN7yT6FMMiFnb0GOqUBTkQxOcKvm883tOgYGuN0%2Fd4jnwRyX6gY0uJq3TyYuizHINNbeyMmq8MoZe6Zemd2GrHQIKACu4%2FYprycfYqKgXlWaZSuQ5BXp0MXjBqH5lmDwDO6dYWonSL6tRveksbwLy1ZgghC89NEZJqRKlIEafqgrt3YA27xhDCJEI59lC5BLOjS%2FjK6WgBZnfNle%2BtkBFj236MFtTkMYeuAvDyQXP6qHll6&X-Amz-Signature=ae0ddfd99b0e30447f6f18189bde8d1cd18ec2f697cd43471284aebcdee1b960&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRJ57DZG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIATXA3Ua%2Ffg2TyTrWGPAE0aykBDeBVa9EffL0xNAjLS6AiEA3A07yJWZHcEe23F8YYsecjEG3ElOIwACLBPITiQIKzUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2hKazXEb1W5MUrPSrcA6kJFAPfO0esT7VSaMLhd6d6FxJQR1v8pxK8QgcwyW5LmOubMsienm9GnaVrzcxn9x3IKVSBv9pKXpuoiSNjsxFbq8e4Dk2Uk7KMGPlEHJmvxSGajdSOh0gNc0jw5H3hNmy5CTEwLRNlfdONq5boDnHHVZ15Qmf4Sx7%2By5Sd25%2FC9A13DQsvEZ6LuI6yyDa8AKMxJOxOCDu5THj1MjgWqoDWwFCGJnfdIlPLrZDvgeUnQVDNxWa4GqAp3b0JhUmFP3wvBNOhCYJNW743Xr%2FXjHyXsfxKy%2BH7n2y1jk0Ix8g1pmz6wqcvgy%2FVQPCjMXluKWiVzMnWpeEgcne4WlYEaWgEI6LkiralxedZWflOxK5wDbIN8jjsN3q4AuXirU2f8ABgVxMTF9IcMS0boqpW6ppAB%2FJxkHpiwcFZEN%2F0XSzjFJyt2c6hfjhxemd9gi3lv1xzlk%2B5tqUCLh071uI61nqCT2vJmQkBuUL2y4uBz5RIR4qvnBXTaVC%2FsCyzrjViQNvEFgZr4rj8DQ4lMZM6N0k1whCELtwdYAsFQF3ZMnVzwc%2FMPpWLIgsdnkm3rGUe5K79%2ByGU72vIb0aL%2B30eoF3sfiOgc0zgMtseQfQXayKFslRZq5a8nZN7yT6FMMiFnb0GOqUBTkQxOcKvm883tOgYGuN0%2Fd4jnwRyX6gY0uJq3TyYuizHINNbeyMmq8MoZe6Zemd2GrHQIKACu4%2FYprycfYqKgXlWaZSuQ5BXp0MXjBqH5lmDwDO6dYWonSL6tRveksbwLy1ZgghC89NEZJqRKlIEafqgrt3YA27xhDCJEI59lC5BLOjS%2FjK6WgBZnfNle%2BtkBFj236MFtTkMYeuAvDyQXP6qHll6&X-Amz-Signature=e0223b37613aeb727a9dfd848ee5bf944054b58aef99ee6412791a436a072233&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRJ57DZG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIATXA3Ua%2Ffg2TyTrWGPAE0aykBDeBVa9EffL0xNAjLS6AiEA3A07yJWZHcEe23F8YYsecjEG3ElOIwACLBPITiQIKzUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2hKazXEb1W5MUrPSrcA6kJFAPfO0esT7VSaMLhd6d6FxJQR1v8pxK8QgcwyW5LmOubMsienm9GnaVrzcxn9x3IKVSBv9pKXpuoiSNjsxFbq8e4Dk2Uk7KMGPlEHJmvxSGajdSOh0gNc0jw5H3hNmy5CTEwLRNlfdONq5boDnHHVZ15Qmf4Sx7%2By5Sd25%2FC9A13DQsvEZ6LuI6yyDa8AKMxJOxOCDu5THj1MjgWqoDWwFCGJnfdIlPLrZDvgeUnQVDNxWa4GqAp3b0JhUmFP3wvBNOhCYJNW743Xr%2FXjHyXsfxKy%2BH7n2y1jk0Ix8g1pmz6wqcvgy%2FVQPCjMXluKWiVzMnWpeEgcne4WlYEaWgEI6LkiralxedZWflOxK5wDbIN8jjsN3q4AuXirU2f8ABgVxMTF9IcMS0boqpW6ppAB%2FJxkHpiwcFZEN%2F0XSzjFJyt2c6hfjhxemd9gi3lv1xzlk%2B5tqUCLh071uI61nqCT2vJmQkBuUL2y4uBz5RIR4qvnBXTaVC%2FsCyzrjViQNvEFgZr4rj8DQ4lMZM6N0k1whCELtwdYAsFQF3ZMnVzwc%2FMPpWLIgsdnkm3rGUe5K79%2ByGU72vIb0aL%2B30eoF3sfiOgc0zgMtseQfQXayKFslRZq5a8nZN7yT6FMMiFnb0GOqUBTkQxOcKvm883tOgYGuN0%2Fd4jnwRyX6gY0uJq3TyYuizHINNbeyMmq8MoZe6Zemd2GrHQIKACu4%2FYprycfYqKgXlWaZSuQ5BXp0MXjBqH5lmDwDO6dYWonSL6tRveksbwLy1ZgghC89NEZJqRKlIEafqgrt3YA27xhDCJEI59lC5BLOjS%2FjK6WgBZnfNle%2BtkBFj236MFtTkMYeuAvDyQXP6qHll6&X-Amz-Signature=027fb2513eedff0d7e3e8c93b919e26bee9acc73561cb0584cade55228d5c416&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJIHD4ZH%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCCiDc4tqnhx2MHSBuHx%2FsGseOoCY0MfBocQepydMI09wIhANFpIZt%2F%2BdSN2w3ZZK2SUhBG4AEeCv3ktJlC%2BM93XO6NKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B1m89IFycldUXi8wq3AMSCUq5q3nn%2FvXZ7CaJYPHx5JNm081XW1YNErQ%2Fzj%2FQ2cAS2JQ8ye9rESRRLROAmf%2BSncZ4NvlqPZ4J12JbFtCA2BXZ%2BGnMS5uFkxdH8ZpxteBHUNYNTUY721cXh7yXGF%2FkbRaSbY61QZ7ohHIeomYs454U99P8yOqAa7BAkuIE9n4PQ4u3Vc5Voy%2BHZWE%2FNLYlZX3yZ6G2gtOMis0Z942LZrFHSOif7W%2FqD0ZBSrLZVBhjD9LG1Di1pGXnMoWk%2FpWNoSo4CH%2Bm7nfTH9KGHA%2BsD6Bow01Cwnr2FAE95FENkJpbJeBkj6q9frp6sQsAAF6dvCmsPbW2FTuqG98Y01KkK5DydBSrHkgkHdmQeG1G%2FS7X3vBoXNO6ITV5Zt7q%2FmO4tV1KhZrfFaMXXS8VkkjfxgMh7WGfj8qGl4QbMhFBN6HF5fomuPMiiN0smmli1duTodYIQzmy9A5kMapd5pzI%2Bqi%2BLP0n44PImWPV3XshCuRPnoqvJU8vn4irqlemuBbfO8rkjFR%2FIKUYsIm0D8JorpNxBqhC2b%2BEk2n37IdPBxRyZYFCpZX9rHlGNGiJ63H7HH0LoJj1kih91RX6d5F30VKKuy83Nsu%2F%2FP2rweBhTyDUgMlqzE6dtG%2BMaTCBhZ29BjqkAeTLIW%2FD2aq4td3ScL02b%2FZuDxGXCD%2FyL%2B7X1Ak1%2BC0BNseN0DsfivyJUxZM3Cdxx36oo50kODwHq0BPzdSOkT7W4%2BHpHh8AyMkNOW2YqXmSrr9iknI%2BrA1k6iMnY%2FjZfDpk1KOqGee85nYEs%2BrskvrPC8qsNiy4b7P%2B2hpAXrg4G4jpq09qiMD6uyRnjSNvRFlRHMi99Hqs96feFV04nV%2BBECgK&X-Amz-Signature=5a1c5e2dccec36737fecf2e6ac9d704d40e3227595e924c488f3b1b397a5c36e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REHGX6N3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGAjsmgrjMXwMFehBfVfvcB9rbPjvsfFItQgvMEHPlYiAiEArH8%2FUA7iSy5IxT72GaeXzmQki7ixZB0Vjkji0mvXiNkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDhrCY0kzqZY2jNysCrcA5OFgy4DRQcE2B01ZQlbaG73gUo%2FW%2F%2FffL%2FaGmNfzUd0t31MO9z1z5L47zWjxo%2FNR8dWPGy6efSL2tSfwPw80E8XrXxHjl222M8catNd1Wa%2F8Qr52XGQbDZYfDLC2ilFwFZaM%2Fwgu%2BwQPnLX25McAkKBYIB0a%2FBiELGa1MRfdv6dg5muey702qTFGvxxtMqcRYX5%2FtxDHOntKcEZhWIHnA2tPzgBk8b1oJVNogy5%2Byt86riVaZKjQM%2FcogtBvYUJKOy3rRC3SpkYG5Y%2FMc%2FqDd9%2BaG069HMd5XxTCEv%2BfxVCH22xBfCuGJKalJQwaJx9la3VGRMZ3Ibg9ittEqWAIUFLwziMS%2FL9eFcqNd5TAiqm8FaE3Q0DAjc3u5vRXfSRaFATjU03T6RC%2BVXdxATtSrOjlIkixGr5M8MXlhm866u45xbzZMVFJKJCgAmZAFnlzUo%2BOQ2aESHeR0VE%2BIrrs4PZ49s%2F4yU63kP%2F9%2FemnxH8qbxhvVEGIwW8PM8pmOUJ4Wnd%2BA4x%2FWzNrx04ZwvbqANVnaZ8OneNEwwatkmPRIERsX0vD09db1QOUSvmd0XOMAxXY4%2FdrEObBAhrYSH4nUeDGLUXOm8WzqNcST0wWFgZJFZbPGmorJE4dWP1MLmFnb0GOqUBzenE5PHqITDKobX9rBnmqxdk7mlQqgtCodug4z2Myh6Y%2ByYBt3JelHjwZf7hVlHPaoiqD8g407bvt22Uo1Xp3kuZkbFROWbQjfdQbtSzeYYy1vEz%2F4leQudCpPkCbsof64EiL2GugHQYHBCXBxNE%2FLfsluVE4P67w9nuz7QKIn%2BuL9i2ayf%2Bg4FQXsF%2BeGsy%2FsYQsCYN74JQaYZ%2BUSxo%2BM1FYHod&X-Amz-Signature=0b7205fd9401db67e9eaed71992bc5706deb7bc59236cd23a7f7a0251f719d92&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJSPIFYS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFnRj%2FIqM0HDJw%2FaQBm4PzEUWzLu%2BPRi6BEbp7WWHj3mAiB1SmvmTWPWTDi%2BX9Qiu13xxjj%2BjqMK18wep3o8OYV6NCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLIYEGbFBOtnH4M8FKtwD71KD9ekQDbGvJGo4LFBXuKJUL3W3KBXAoTH9aQj4LBEC4OGejg7k%2Bi%2FMRGXm4c2gV22WXkfVOnkfgbQoW%2B%2Fbr9l8p9gmRcU5mea9cx5Dp9QpFMN3%2Bzfv895Lai3DP9wEyFPQn61G6RHvDyRx%2Fv1YGA6lrqqTEkEVytlzssXXy0L%2FNO64j%2BKlD47Ty0DPJybOaiZcIsqrmeUB4uSgIF3%2Bh0dEY%2B67Fubdg9C8%2BR%2Fh5%2BNbkp%2FnGchPPdWE49GmknC8wx7NZ%2BitSfOXBbmn5ytMadfeTUPk8RlUt6tcgprpTCEGu%2BHqlls8VlKq8Va3sVCRWnnVJtkPnAd0i4cu5KG7zripNLK5EjJa4NkoQizU2tiRPSc65ntSvrKIHOTx2ekhf63cG88IEXKPRhWq3DvQcy01hEYOw2wNZfh2tvwKOIYJzy0NUd0kJ7UHdQbclDnP9eO0poW8pLPzwWnfyN%2FVYNXUDaJedMMAL%2FTivtio6yNvogtBexfz%2FgB6HVPJM8YQ%2FMm%2FzJslsc6lkfUwXfD5Yu9LAB8J6NHKmt2DbES9OmxybfmjmP84ckD4z42Nc%2FmlDLD%2BjZfgHAkpJ24SolWM9u%2FjZQKE%2F8Y9bnQNS9msAci2U7j6LJw%2F39JDHH8wq4WdvQY6pgE03vBt1wHdJPZFd%2Fr%2Bw6GCQXt95ZRYwLwyyyNbE5%2BTFaQ5WW1fYEbn6iyIJFSSo9%2F8dSNgXW96pvht3KAAUDaG3y29QTj3wSVNI8fTZGKRF1nnGH7nyDtKECGc2fvX%2B0Xyf5zgpvvUs56znDEQnmxHddRhazRM%2F4LAlf8alDOvNJlSvmcjIjnMW89J0l4zMa14F5JLMEqra4w7Nx8odMovrMgSVi5o&X-Amz-Signature=046cbc1f11bb53ffc262f839fb359acec1d78749ff1b6441a57fac263bc98121&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TC3ODFR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIEweSh%2FL7LHRJe3aJPy8Qv8kDaCoDOIVqXu1Sn63xy1DAiEAxjeebmPKU%2BlGVKKb68CembYUqCKxuPlVc9%2FwW9rUTBsqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBOY8BBb9KL5wXzrircA0opKhTaruFIH8zBKvWde%2BDRb1UAsvNqV727nzkHpkkrdneozDOwfsQyVhL909kyBwpddbsZe3D3hGui09gCy5s0iIb2jZo3UJP%2FiWUlJBpKuAX07AjvvDTBrMfxHBne0gDRSEQBWC74wTnlg1mhTGrj9vWZnNEi5bLWfD0JgmdLqQ9QZtk54Ovdbum2tmXxRH7YIbCp%2B37f1PGpnkxO1wedEQUc2Lq8pWPCMXvQW0ipe8dHILnSbU696uk5k1bX%2FR0v0SggwhkAIXLy3LawKDXbswPE3R%2F7GFRckoT%2FQqE70F3F37t1n96KXCVCUhY8Gj9FBrpKbyGbw1XVPz8krpDquold9mVH%2Bo9VaIHENhz21wHicyuEYD9%2BqNWcbmgIEeut46X8fpbw7JeU6p9RtkGLR9MutGKfb92sCxEymmO%2FVn8DD1KqHZ6iAlPR%2B1qkgL%2FdxhwQJ8LStwCEa%2BVSI2avEU1yg0qowjMpbY8q9wYyLFvLIBZjs3IBmUI%2Ftdm%2BbdYFX40xDiHIVcOai56lPFgOFOUi11RdqMs%2F6Xa0ZlBNZIfyUKB5F99wtHbuSe3S%2Fb75wtvdtuKeZP409P4QHdHAnChDH%2BH2WNlXHcCMzxQl5QPnGVkhkahV4W7TMLmFnb0GOqUBoxf4aS631%2BrZP4AnGifhJ%2B5aFe6JXggzgc%2BxFQ4yhoslrsriMnJru3aSUgfgpBWZvLOsIMdgXnNxFIkt9C%2BRCe7R42JzXO0oOcdVXlhBbya89K42jk1kGg6CUqL%2BEhCUm0gcRkzukiz%2Fo1%2B6omsAsfSj7%2F89qjuyc8QUtB%2BVf1PasJAoiAtvaxcde3pjku4J2FY1hWOdRwDN8OmVnCdRDkXQTWkB&X-Amz-Signature=37e5dd56f29e23d73b4754442a5be7aaeb51c6d3ccea1612e900cc8a29f622f5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TC3ODFR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIEweSh%2FL7LHRJe3aJPy8Qv8kDaCoDOIVqXu1Sn63xy1DAiEAxjeebmPKU%2BlGVKKb68CembYUqCKxuPlVc9%2FwW9rUTBsqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBOY8BBb9KL5wXzrircA0opKhTaruFIH8zBKvWde%2BDRb1UAsvNqV727nzkHpkkrdneozDOwfsQyVhL909kyBwpddbsZe3D3hGui09gCy5s0iIb2jZo3UJP%2FiWUlJBpKuAX07AjvvDTBrMfxHBne0gDRSEQBWC74wTnlg1mhTGrj9vWZnNEi5bLWfD0JgmdLqQ9QZtk54Ovdbum2tmXxRH7YIbCp%2B37f1PGpnkxO1wedEQUc2Lq8pWPCMXvQW0ipe8dHILnSbU696uk5k1bX%2FR0v0SggwhkAIXLy3LawKDXbswPE3R%2F7GFRckoT%2FQqE70F3F37t1n96KXCVCUhY8Gj9FBrpKbyGbw1XVPz8krpDquold9mVH%2Bo9VaIHENhz21wHicyuEYD9%2BqNWcbmgIEeut46X8fpbw7JeU6p9RtkGLR9MutGKfb92sCxEymmO%2FVn8DD1KqHZ6iAlPR%2B1qkgL%2FdxhwQJ8LStwCEa%2BVSI2avEU1yg0qowjMpbY8q9wYyLFvLIBZjs3IBmUI%2Ftdm%2BbdYFX40xDiHIVcOai56lPFgOFOUi11RdqMs%2F6Xa0ZlBNZIfyUKB5F99wtHbuSe3S%2Fb75wtvdtuKeZP409P4QHdHAnChDH%2BH2WNlXHcCMzxQl5QPnGVkhkahV4W7TMLmFnb0GOqUBoxf4aS631%2BrZP4AnGifhJ%2B5aFe6JXggzgc%2BxFQ4yhoslrsriMnJru3aSUgfgpBWZvLOsIMdgXnNxFIkt9C%2BRCe7R42JzXO0oOcdVXlhBbya89K42jk1kGg6CUqL%2BEhCUm0gcRkzukiz%2Fo1%2B6omsAsfSj7%2F89qjuyc8QUtB%2BVf1PasJAoiAtvaxcde3pjku4J2FY1hWOdRwDN8OmVnCdRDkXQTWkB&X-Amz-Signature=6370b072703f39f5a17d4eef7e7b0a4ab0ac0198437baaaca7ec750886808c9d&X-Amz-SignedHeaders=host&x-id=GetObject)

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
