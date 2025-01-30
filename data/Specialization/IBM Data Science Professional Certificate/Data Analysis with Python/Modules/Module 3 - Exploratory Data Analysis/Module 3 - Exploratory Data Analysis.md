

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKYOBO3M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjngjRKfWXi28R3ih32UrOh3k1ex9yhvjcSP2qdQ2uHgIhALbM%2F3A9r%2BY%2B4D0GDZB5Bkvaa9BRygkhp7LQpky25LGgKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwTr1%2FMm0NkvQdh0A4q3AM5XWIWAeH3F%2FWii3vDXLFaFcpOPZYikVluPJ%2FqZyQE3yRdDEzFufd5bXpp6RDhqGc8oJ7%2FPiIUtZO3hEwOCF%2BpW4BSrzJ43hYDRyGg1MM9F9pq8va4OtzDzEqihrK4k3%2B81VCV8HE5se4rfq43Jol1tIwU3K2mEXDUhPV3RUQwNFje3f%2FwSYB0Y7J7E%2FRM3h7vQls60ahObFK8Q%2FFfllfr6PLueR75LD3d7u8nptjUoGCeFtVfnpYv8ns%2FPN1v6gYdJDEca4dpSkJ3rGM%2Fa0pxGvLvVTZ6vBtnWULUwEMspXsQmO%2Fw2Pr9PuDCNZEfSGuCWm%2F12YKObhsgGJwcOPFILy88gFpAaZ5CAswe7nME8vQlrWTPh%2BdbSH%2FDT4a2TkjkAD6p9KdaGjgEQuYxn0psdU3T6oWXl7BHpJpJUw6M%2BhrXnq5Bp5Sh5Bt0kFpjNUtYhh%2BPJdZzhdBJL%2FH7kO4AJhPxyhju9QCREtZwn9Z26IBmMoPzDtm%2FSKvGVfwoPobT1N%2FisQlO%2F%2BByO6apIoiAk6ebcOk4eIxipBu6HAvLPIJkQDdhweTNLx0s9Y6zR7EUnpXewWxFEy0o4lDzu5wWIjxuPCix9m5ysrS2WEnUXKNpmyEIin8sU6ZkQzCWl%2B68BjqkATIHszuxTH9NrKx0Do2RJkJSAb1r9%2FnWw6vtBmuh7M6TBNqV1cyhmevONvSqoNF%2FmDxNHXr3saaTdLs0ZmDjvDpHxhh0R41V9oXif%2BgmnCQkWMcfL18fGXgyP2S6VmPY7Qvb%2FKtpOtmPoaaGhMeDD0fFkOIy0HO3QcO6Dshnz3G%2BThe34w7ZBgIDD9Tn4nY0mWopK7tCg7Fd3sngT82nYuFbGEjK&X-Amz-Signature=e67c613c2834097b2463a85aea4cb5dcc0339c4a1275477844d4ea3c347e7356&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKYOBO3M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjngjRKfWXi28R3ih32UrOh3k1ex9yhvjcSP2qdQ2uHgIhALbM%2F3A9r%2BY%2B4D0GDZB5Bkvaa9BRygkhp7LQpky25LGgKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwTr1%2FMm0NkvQdh0A4q3AM5XWIWAeH3F%2FWii3vDXLFaFcpOPZYikVluPJ%2FqZyQE3yRdDEzFufd5bXpp6RDhqGc8oJ7%2FPiIUtZO3hEwOCF%2BpW4BSrzJ43hYDRyGg1MM9F9pq8va4OtzDzEqihrK4k3%2B81VCV8HE5se4rfq43Jol1tIwU3K2mEXDUhPV3RUQwNFje3f%2FwSYB0Y7J7E%2FRM3h7vQls60ahObFK8Q%2FFfllfr6PLueR75LD3d7u8nptjUoGCeFtVfnpYv8ns%2FPN1v6gYdJDEca4dpSkJ3rGM%2Fa0pxGvLvVTZ6vBtnWULUwEMspXsQmO%2Fw2Pr9PuDCNZEfSGuCWm%2F12YKObhsgGJwcOPFILy88gFpAaZ5CAswe7nME8vQlrWTPh%2BdbSH%2FDT4a2TkjkAD6p9KdaGjgEQuYxn0psdU3T6oWXl7BHpJpJUw6M%2BhrXnq5Bp5Sh5Bt0kFpjNUtYhh%2BPJdZzhdBJL%2FH7kO4AJhPxyhju9QCREtZwn9Z26IBmMoPzDtm%2FSKvGVfwoPobT1N%2FisQlO%2F%2BByO6apIoiAk6ebcOk4eIxipBu6HAvLPIJkQDdhweTNLx0s9Y6zR7EUnpXewWxFEy0o4lDzu5wWIjxuPCix9m5ysrS2WEnUXKNpmyEIin8sU6ZkQzCWl%2B68BjqkATIHszuxTH9NrKx0Do2RJkJSAb1r9%2FnWw6vtBmuh7M6TBNqV1cyhmevONvSqoNF%2FmDxNHXr3saaTdLs0ZmDjvDpHxhh0R41V9oXif%2BgmnCQkWMcfL18fGXgyP2S6VmPY7Qvb%2FKtpOtmPoaaGhMeDD0fFkOIy0HO3QcO6Dshnz3G%2BThe34w7ZBgIDD9Tn4nY0mWopK7tCg7Fd3sngT82nYuFbGEjK&X-Amz-Signature=4d2aaa02c73cc15c9f2bde6b6d8af8136fdb1eeb960f3afdca5f35fe12733b42&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKYOBO3M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjngjRKfWXi28R3ih32UrOh3k1ex9yhvjcSP2qdQ2uHgIhALbM%2F3A9r%2BY%2B4D0GDZB5Bkvaa9BRygkhp7LQpky25LGgKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwTr1%2FMm0NkvQdh0A4q3AM5XWIWAeH3F%2FWii3vDXLFaFcpOPZYikVluPJ%2FqZyQE3yRdDEzFufd5bXpp6RDhqGc8oJ7%2FPiIUtZO3hEwOCF%2BpW4BSrzJ43hYDRyGg1MM9F9pq8va4OtzDzEqihrK4k3%2B81VCV8HE5se4rfq43Jol1tIwU3K2mEXDUhPV3RUQwNFje3f%2FwSYB0Y7J7E%2FRM3h7vQls60ahObFK8Q%2FFfllfr6PLueR75LD3d7u8nptjUoGCeFtVfnpYv8ns%2FPN1v6gYdJDEca4dpSkJ3rGM%2Fa0pxGvLvVTZ6vBtnWULUwEMspXsQmO%2Fw2Pr9PuDCNZEfSGuCWm%2F12YKObhsgGJwcOPFILy88gFpAaZ5CAswe7nME8vQlrWTPh%2BdbSH%2FDT4a2TkjkAD6p9KdaGjgEQuYxn0psdU3T6oWXl7BHpJpJUw6M%2BhrXnq5Bp5Sh5Bt0kFpjNUtYhh%2BPJdZzhdBJL%2FH7kO4AJhPxyhju9QCREtZwn9Z26IBmMoPzDtm%2FSKvGVfwoPobT1N%2FisQlO%2F%2BByO6apIoiAk6ebcOk4eIxipBu6HAvLPIJkQDdhweTNLx0s9Y6zR7EUnpXewWxFEy0o4lDzu5wWIjxuPCix9m5ysrS2WEnUXKNpmyEIin8sU6ZkQzCWl%2B68BjqkATIHszuxTH9NrKx0Do2RJkJSAb1r9%2FnWw6vtBmuh7M6TBNqV1cyhmevONvSqoNF%2FmDxNHXr3saaTdLs0ZmDjvDpHxhh0R41V9oXif%2BgmnCQkWMcfL18fGXgyP2S6VmPY7Qvb%2FKtpOtmPoaaGhMeDD0fFkOIy0HO3QcO6Dshnz3G%2BThe34w7ZBgIDD9Tn4nY0mWopK7tCg7Fd3sngT82nYuFbGEjK&X-Amz-Signature=bd76f61658f5f9cb2d0e917f67e04cb8bf61f4a77c378c6e9c97401fbf98bbfc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIZVJAKK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICj1TjKrV5YyvGNlhL1ofrH%2BzpU%2Bp5PGzgo2ALHcnyEfAiA%2FYgrS%2FB5tQ5SsNTpXr9qwTdqVTZabtBVcV1zIl6NqrSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfmn2DhvhVky2yhoqKtwDfRRXremSc97nQuhYElUnm3E9h1I%2FveJc076%2FyHYgqcBKCn7keEcVJHHoziaRHzgqHHwp6zStUgRjkakmVzJYQZmdEM9BeSuoT5nhs0fYUcgTSs5AqLHNVEK6esKbZE4PL7Cpgm%2B8hIc%2Bq75XkkpvcPV5xoXxz1gzyo4pSYjSJX%2FeSkPO%2BsFladazxA5yWztahUSP0FvCWiXat7o6Obe8Xr3TFi2xhC0NJo0d34w9OcdEY0eFmpZn3WwvTSOAnIiu6LoTIqr1rlAAzmc5r%2BHTrrQK%2B8Dyxx8%2BnlJwx7XHTF7UO4EVABKZf7WL1qE32kGeBqB6ud%2Fudet%2FI8kpsDsGWjd0Fm8gSoFRhJaCqPeXNt1ZTeGlfCRpi9pswiWTDmIVtjvDTA42LMdx2OM76Rhdbmz0Mo%2B55yvu%2Bhr1HF1RNlKNsJ12S2DHfx806rzfYAAxdm%2BUbGAxrdfbd%2FkPylJRqfGJmPeSc9d%2BAjlKCHZ3iGPSjdnmNL4JlEcJAwS%2BDvx0tY06GSZXKXigS0hf1VV0oJQFopv%2FCw%2BUM%2BMUn45tQ9FgQGfzuKNu%2BM%2BS8xmQQKSp2rlzbMvNndTed%2BEwJVnxc205ESsbp1kAQYR8IH3SbU%2FHFms4W9aVZrFj4wgw35fuvAY6pgEEghoR%2BTtnazLC6WqOoWho6VHSYAetThJgB0on%2BytsvrpStKpNbDF6F2DMCDKuQ4eRQan1oei9JS0i7NoCmp8hqJSenKdSRV790os0yuSrrrBabBO1f6%2FytuMo79fqhYY7%2B5RY9ysTQ7D3jpFG%2FVouXDbK1UbyY0uAxTYfmU5OyklZaLFjwX7JZ9DZJrQNtbpxFmqfEmcHH0Aw1Fy66JzLE3ulXGuP&X-Amz-Signature=742e3faf1fc40156cfdf233e46dba19380060a0e2ac85a08230b8efdbb384056&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIZVJAKK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICj1TjKrV5YyvGNlhL1ofrH%2BzpU%2Bp5PGzgo2ALHcnyEfAiA%2FYgrS%2FB5tQ5SsNTpXr9qwTdqVTZabtBVcV1zIl6NqrSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfmn2DhvhVky2yhoqKtwDfRRXremSc97nQuhYElUnm3E9h1I%2FveJc076%2FyHYgqcBKCn7keEcVJHHoziaRHzgqHHwp6zStUgRjkakmVzJYQZmdEM9BeSuoT5nhs0fYUcgTSs5AqLHNVEK6esKbZE4PL7Cpgm%2B8hIc%2Bq75XkkpvcPV5xoXxz1gzyo4pSYjSJX%2FeSkPO%2BsFladazxA5yWztahUSP0FvCWiXat7o6Obe8Xr3TFi2xhC0NJo0d34w9OcdEY0eFmpZn3WwvTSOAnIiu6LoTIqr1rlAAzmc5r%2BHTrrQK%2B8Dyxx8%2BnlJwx7XHTF7UO4EVABKZf7WL1qE32kGeBqB6ud%2Fudet%2FI8kpsDsGWjd0Fm8gSoFRhJaCqPeXNt1ZTeGlfCRpi9pswiWTDmIVtjvDTA42LMdx2OM76Rhdbmz0Mo%2B55yvu%2Bhr1HF1RNlKNsJ12S2DHfx806rzfYAAxdm%2BUbGAxrdfbd%2FkPylJRqfGJmPeSc9d%2BAjlKCHZ3iGPSjdnmNL4JlEcJAwS%2BDvx0tY06GSZXKXigS0hf1VV0oJQFopv%2FCw%2BUM%2BMUn45tQ9FgQGfzuKNu%2BM%2BS8xmQQKSp2rlzbMvNndTed%2BEwJVnxc205ESsbp1kAQYR8IH3SbU%2FHFms4W9aVZrFj4wgw35fuvAY6pgEEghoR%2BTtnazLC6WqOoWho6VHSYAetThJgB0on%2BytsvrpStKpNbDF6F2DMCDKuQ4eRQan1oei9JS0i7NoCmp8hqJSenKdSRV790os0yuSrrrBabBO1f6%2FytuMo79fqhYY7%2B5RY9ysTQ7D3jpFG%2FVouXDbK1UbyY0uAxTYfmU5OyklZaLFjwX7JZ9DZJrQNtbpxFmqfEmcHH0Aw1Fy66JzLE3ulXGuP&X-Amz-Signature=0a28a756570100ee9ae052df7edd049da0931f115a1563772d751b5fcf53984b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIZVJAKK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICj1TjKrV5YyvGNlhL1ofrH%2BzpU%2Bp5PGzgo2ALHcnyEfAiA%2FYgrS%2FB5tQ5SsNTpXr9qwTdqVTZabtBVcV1zIl6NqrSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfmn2DhvhVky2yhoqKtwDfRRXremSc97nQuhYElUnm3E9h1I%2FveJc076%2FyHYgqcBKCn7keEcVJHHoziaRHzgqHHwp6zStUgRjkakmVzJYQZmdEM9BeSuoT5nhs0fYUcgTSs5AqLHNVEK6esKbZE4PL7Cpgm%2B8hIc%2Bq75XkkpvcPV5xoXxz1gzyo4pSYjSJX%2FeSkPO%2BsFladazxA5yWztahUSP0FvCWiXat7o6Obe8Xr3TFi2xhC0NJo0d34w9OcdEY0eFmpZn3WwvTSOAnIiu6LoTIqr1rlAAzmc5r%2BHTrrQK%2B8Dyxx8%2BnlJwx7XHTF7UO4EVABKZf7WL1qE32kGeBqB6ud%2Fudet%2FI8kpsDsGWjd0Fm8gSoFRhJaCqPeXNt1ZTeGlfCRpi9pswiWTDmIVtjvDTA42LMdx2OM76Rhdbmz0Mo%2B55yvu%2Bhr1HF1RNlKNsJ12S2DHfx806rzfYAAxdm%2BUbGAxrdfbd%2FkPylJRqfGJmPeSc9d%2BAjlKCHZ3iGPSjdnmNL4JlEcJAwS%2BDvx0tY06GSZXKXigS0hf1VV0oJQFopv%2FCw%2BUM%2BMUn45tQ9FgQGfzuKNu%2BM%2BS8xmQQKSp2rlzbMvNndTed%2BEwJVnxc205ESsbp1kAQYR8IH3SbU%2FHFms4W9aVZrFj4wgw35fuvAY6pgEEghoR%2BTtnazLC6WqOoWho6VHSYAetThJgB0on%2BytsvrpStKpNbDF6F2DMCDKuQ4eRQan1oei9JS0i7NoCmp8hqJSenKdSRV790os0yuSrrrBabBO1f6%2FytuMo79fqhYY7%2B5RY9ysTQ7D3jpFG%2FVouXDbK1UbyY0uAxTYfmU5OyklZaLFjwX7JZ9DZJrQNtbpxFmqfEmcHH0Aw1Fy66JzLE3ulXGuP&X-Amz-Signature=acefa0bfbd11773d3afb03ccdfb6b29a97f769e6271c5bd29ce0bedd335fac36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIZVJAKK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICj1TjKrV5YyvGNlhL1ofrH%2BzpU%2Bp5PGzgo2ALHcnyEfAiA%2FYgrS%2FB5tQ5SsNTpXr9qwTdqVTZabtBVcV1zIl6NqrSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfmn2DhvhVky2yhoqKtwDfRRXremSc97nQuhYElUnm3E9h1I%2FveJc076%2FyHYgqcBKCn7keEcVJHHoziaRHzgqHHwp6zStUgRjkakmVzJYQZmdEM9BeSuoT5nhs0fYUcgTSs5AqLHNVEK6esKbZE4PL7Cpgm%2B8hIc%2Bq75XkkpvcPV5xoXxz1gzyo4pSYjSJX%2FeSkPO%2BsFladazxA5yWztahUSP0FvCWiXat7o6Obe8Xr3TFi2xhC0NJo0d34w9OcdEY0eFmpZn3WwvTSOAnIiu6LoTIqr1rlAAzmc5r%2BHTrrQK%2B8Dyxx8%2BnlJwx7XHTF7UO4EVABKZf7WL1qE32kGeBqB6ud%2Fudet%2FI8kpsDsGWjd0Fm8gSoFRhJaCqPeXNt1ZTeGlfCRpi9pswiWTDmIVtjvDTA42LMdx2OM76Rhdbmz0Mo%2B55yvu%2Bhr1HF1RNlKNsJ12S2DHfx806rzfYAAxdm%2BUbGAxrdfbd%2FkPylJRqfGJmPeSc9d%2BAjlKCHZ3iGPSjdnmNL4JlEcJAwS%2BDvx0tY06GSZXKXigS0hf1VV0oJQFopv%2FCw%2BUM%2BMUn45tQ9FgQGfzuKNu%2BM%2BS8xmQQKSp2rlzbMvNndTed%2BEwJVnxc205ESsbp1kAQYR8IH3SbU%2FHFms4W9aVZrFj4wgw35fuvAY6pgEEghoR%2BTtnazLC6WqOoWho6VHSYAetThJgB0on%2BytsvrpStKpNbDF6F2DMCDKuQ4eRQan1oei9JS0i7NoCmp8hqJSenKdSRV790os0yuSrrrBabBO1f6%2FytuMo79fqhYY7%2B5RY9ysTQ7D3jpFG%2FVouXDbK1UbyY0uAxTYfmU5OyklZaLFjwX7JZ9DZJrQNtbpxFmqfEmcHH0Aw1Fy66JzLE3ulXGuP&X-Amz-Signature=3687c979e7b4d876d5fae11d1e004435af35f6e22c8e608f4f3625bf78c85059&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIZVJAKK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICj1TjKrV5YyvGNlhL1ofrH%2BzpU%2Bp5PGzgo2ALHcnyEfAiA%2FYgrS%2FB5tQ5SsNTpXr9qwTdqVTZabtBVcV1zIl6NqrSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfmn2DhvhVky2yhoqKtwDfRRXremSc97nQuhYElUnm3E9h1I%2FveJc076%2FyHYgqcBKCn7keEcVJHHoziaRHzgqHHwp6zStUgRjkakmVzJYQZmdEM9BeSuoT5nhs0fYUcgTSs5AqLHNVEK6esKbZE4PL7Cpgm%2B8hIc%2Bq75XkkpvcPV5xoXxz1gzyo4pSYjSJX%2FeSkPO%2BsFladazxA5yWztahUSP0FvCWiXat7o6Obe8Xr3TFi2xhC0NJo0d34w9OcdEY0eFmpZn3WwvTSOAnIiu6LoTIqr1rlAAzmc5r%2BHTrrQK%2B8Dyxx8%2BnlJwx7XHTF7UO4EVABKZf7WL1qE32kGeBqB6ud%2Fudet%2FI8kpsDsGWjd0Fm8gSoFRhJaCqPeXNt1ZTeGlfCRpi9pswiWTDmIVtjvDTA42LMdx2OM76Rhdbmz0Mo%2B55yvu%2Bhr1HF1RNlKNsJ12S2DHfx806rzfYAAxdm%2BUbGAxrdfbd%2FkPylJRqfGJmPeSc9d%2BAjlKCHZ3iGPSjdnmNL4JlEcJAwS%2BDvx0tY06GSZXKXigS0hf1VV0oJQFopv%2FCw%2BUM%2BMUn45tQ9FgQGfzuKNu%2BM%2BS8xmQQKSp2rlzbMvNndTed%2BEwJVnxc205ESsbp1kAQYR8IH3SbU%2FHFms4W9aVZrFj4wgw35fuvAY6pgEEghoR%2BTtnazLC6WqOoWho6VHSYAetThJgB0on%2BytsvrpStKpNbDF6F2DMCDKuQ4eRQan1oei9JS0i7NoCmp8hqJSenKdSRV790os0yuSrrrBabBO1f6%2FytuMo79fqhYY7%2B5RY9ysTQ7D3jpFG%2FVouXDbK1UbyY0uAxTYfmU5OyklZaLFjwX7JZ9DZJrQNtbpxFmqfEmcHH0Aw1Fy66JzLE3ulXGuP&X-Amz-Signature=0d34e0e4975617d4b0ac6cb5ec5e7a4bd707af1b384aa0dc36f6cb977490e501&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIZVJAKK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICj1TjKrV5YyvGNlhL1ofrH%2BzpU%2Bp5PGzgo2ALHcnyEfAiA%2FYgrS%2FB5tQ5SsNTpXr9qwTdqVTZabtBVcV1zIl6NqrSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfmn2DhvhVky2yhoqKtwDfRRXremSc97nQuhYElUnm3E9h1I%2FveJc076%2FyHYgqcBKCn7keEcVJHHoziaRHzgqHHwp6zStUgRjkakmVzJYQZmdEM9BeSuoT5nhs0fYUcgTSs5AqLHNVEK6esKbZE4PL7Cpgm%2B8hIc%2Bq75XkkpvcPV5xoXxz1gzyo4pSYjSJX%2FeSkPO%2BsFladazxA5yWztahUSP0FvCWiXat7o6Obe8Xr3TFi2xhC0NJo0d34w9OcdEY0eFmpZn3WwvTSOAnIiu6LoTIqr1rlAAzmc5r%2BHTrrQK%2B8Dyxx8%2BnlJwx7XHTF7UO4EVABKZf7WL1qE32kGeBqB6ud%2Fudet%2FI8kpsDsGWjd0Fm8gSoFRhJaCqPeXNt1ZTeGlfCRpi9pswiWTDmIVtjvDTA42LMdx2OM76Rhdbmz0Mo%2B55yvu%2Bhr1HF1RNlKNsJ12S2DHfx806rzfYAAxdm%2BUbGAxrdfbd%2FkPylJRqfGJmPeSc9d%2BAjlKCHZ3iGPSjdnmNL4JlEcJAwS%2BDvx0tY06GSZXKXigS0hf1VV0oJQFopv%2FCw%2BUM%2BMUn45tQ9FgQGfzuKNu%2BM%2BS8xmQQKSp2rlzbMvNndTed%2BEwJVnxc205ESsbp1kAQYR8IH3SbU%2FHFms4W9aVZrFj4wgw35fuvAY6pgEEghoR%2BTtnazLC6WqOoWho6VHSYAetThJgB0on%2BytsvrpStKpNbDF6F2DMCDKuQ4eRQan1oei9JS0i7NoCmp8hqJSenKdSRV790os0yuSrrrBabBO1f6%2FytuMo79fqhYY7%2B5RY9ysTQ7D3jpFG%2FVouXDbK1UbyY0uAxTYfmU5OyklZaLFjwX7JZ9DZJrQNtbpxFmqfEmcHH0Aw1Fy66JzLE3ulXGuP&X-Amz-Signature=e15b2c3e257cafb4994b632a4813540c1ffc16a75f9397f5b03eac62c2d7a0de&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TB6Y5JNS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjR9EoVNTYLsDZkZxZjmJXtiFNttIlz2dLOsJlkWhA7AiEAvq0xZf087Okc2qXDRuvu71kuUgW1booeVBlg12f8EZQqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXP3rcXjIi%2FvbutvSrcA87%2B1iqBwvujW6uaH3clFYGAw9MaIEZD7BDl4BGnVW0tZnDQxevNuQ6L03WZu%2BxjLNbFD0cCDCt4Bs2Byzl6L3yV9ePOC%2FIoX7z%2BzA0lIVVmNn9crcp9bLzWnrHOqBLHybLtL9G7r%2F5DApkO8zUTcwd12jpSVxEgDEc49byBTAp0craCIVJO4mihZ0q%2FLzyRjxGwhNorE%2Fxc%2FWFiP8%2F4xXT1GE8iev%2B6HQ1%2BM00A1It6kxkV2f%2BqCAglKdzVfrPg5Pv%2FJ6X55cf0AIN7nvchfwKdTkuKJpsnRYKNvwEZjSTCImOQbnYl%2FgD4H4CqoqFYoFcoy2cxQP0CRFo8%2BaVOSfDIbvG7oFLVYAqAZvJ4CNYcT%2BxTNzLI0ihzGTCxbndc%2FN8wk9thzV2pBGyvBLqbr1rQHn%2BmXWB5qmhzmzVirc%2BEMCpEGp6Xt6Y7J2GHU3UY0aTlrHS%2Fdd%2FMYpIM6pGyi3mOjo0ujnw%2FrWBpkjEa%2FBm0DPuzxZedSFCfbcVn%2BhEG5775zbCzUf0upvoSIer2pe9P6o2AYL23k2BmsFUEo1j9noTi0Qzw4Ar4ZT6rZwCJLf6dTPKnnEZg4iHt%2BFwVWExajA7Kol%2FdqqpjPv4QOBoJ69lVa%2B61D3qJm5rEMLmY7rwGOqUBJvwqbMP4q1A%2FkuehrcJuXaImhQin94SNyBCiV9f4eDICSzjkHqjXGb31fqsASYOoDNQSj%2B2Yk%2B60BxuhZy3iIDst5kDK5kib8UjCBfDUmUDxfsB0aFCGhY3Axxark4xjEWMDUm6C17pfDKOrNGUckHZ2E7OUbn2tt801cWUncBjm23f%2B4k8GQ6uW%2FYBq5wjRzYFnDIKzoKdQC5u7Gz4R1hkngMbb&X-Amz-Signature=54d7829cd7ca597b7fd178bd77bda730a6ef2ba8037a27cb967384b443707fc1&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLXVQE3G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUU7EFhDVYdfrGicXh1CxiPY6eEYq7OQ0m0spj%2F%2BtpdgIhAJcHKrwdkCzBTwMdlhkvu5w0Q9PCbfmTAmFcG%2BzVvAyTKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3zHkmQNsq9t1yGMIq3APnJHIHRGPR8DUDzCjBA5SvbD4noW%2FmeFUFY5G%2BqKopIZjWLtnXX1dJGkC4OIOhF%2BWfpCoDjJthUzMe2AsRr7CFiGqk4OVHI0SusbXZa6GUEjaz93EiZeAroLi5TQafqPRUDa3Kjz01cRkUVMJ5gxlwVCTVSRbXvV6iBhnR%2B8ufULc6WZRvC8bbdxyoViZruNxnAa4Ya6tPXnsjTZgZrHJ%2Bi2hgGJWh7lHyCLdiwx3wQPFSrwxgktCGBmv4njBLdIop7WnJbe9zN4fHnzfaWxCiF4%2BJbCQbJryMbhqCLxFFAxUWK5vt0b%2F32fEukwmyTvVkoX71pFkflkZe%2BitNMhHpp8qiBNvdbAMPlbfgNwCBstijHsUrGrzu%2Bf9O1JvTmJL%2B%2FFhHXnfWkw%2BDSPPwV8xiZ0q2L%2BhFa%2FO9prTbqVUwNU8poTFE3%2F5CRWV7v6jfnBhe1q5Z%2FKQ1IoZFCIglyWuAC5jz10%2B%2F3Z9mi%2BfMm%2B8pwx9rMJLl%2BK4%2FX8bSjGZJ1Dc5Fxy9tO6rnGjxFTwJnwIcH38AAuvPhR3dwunkDRJPxWtoK4AqTiPR19OK9gvpNzSW0Vu0NTXiHx2HbZg%2B5Wh3wmfPT5K6iADYfuL9%2BVjtx1cbNMMxTZU8x0bHkzCAmO68BjqkARSovD0RXWQaqdfp1FRNmk2pu9pyUWzEinmxSIHwlr7jbLwuyuzDzaNveIrO4N%2F9jLiOLe%2Ba6aTXX0Gqiz8vt1P9qN%2BpHmDaxVOvFlXzhGTHiVQ%2FrCJqJIv8uR0qsgZDZa961wyMnniFxW4parc6AAiiVMJtLiWdCqwSo0cYr7SJAHcEO%2F9S05YNT238GlaMAt1OF0pOSs7bcCbypRsS537fQ214&X-Amz-Signature=bc7a2198d68eeae596a3b1e8962c7db7f5ff1e6b326c9b1104f910b6245cb134&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIZVJAKK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICj1TjKrV5YyvGNlhL1ofrH%2BzpU%2Bp5PGzgo2ALHcnyEfAiA%2FYgrS%2FB5tQ5SsNTpXr9qwTdqVTZabtBVcV1zIl6NqrSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfmn2DhvhVky2yhoqKtwDfRRXremSc97nQuhYElUnm3E9h1I%2FveJc076%2FyHYgqcBKCn7keEcVJHHoziaRHzgqHHwp6zStUgRjkakmVzJYQZmdEM9BeSuoT5nhs0fYUcgTSs5AqLHNVEK6esKbZE4PL7Cpgm%2B8hIc%2Bq75XkkpvcPV5xoXxz1gzyo4pSYjSJX%2FeSkPO%2BsFladazxA5yWztahUSP0FvCWiXat7o6Obe8Xr3TFi2xhC0NJo0d34w9OcdEY0eFmpZn3WwvTSOAnIiu6LoTIqr1rlAAzmc5r%2BHTrrQK%2B8Dyxx8%2BnlJwx7XHTF7UO4EVABKZf7WL1qE32kGeBqB6ud%2Fudet%2FI8kpsDsGWjd0Fm8gSoFRhJaCqPeXNt1ZTeGlfCRpi9pswiWTDmIVtjvDTA42LMdx2OM76Rhdbmz0Mo%2B55yvu%2Bhr1HF1RNlKNsJ12S2DHfx806rzfYAAxdm%2BUbGAxrdfbd%2FkPylJRqfGJmPeSc9d%2BAjlKCHZ3iGPSjdnmNL4JlEcJAwS%2BDvx0tY06GSZXKXigS0hf1VV0oJQFopv%2FCw%2BUM%2BMUn45tQ9FgQGfzuKNu%2BM%2BS8xmQQKSp2rlzbMvNndTed%2BEwJVnxc205ESsbp1kAQYR8IH3SbU%2FHFms4W9aVZrFj4wgw35fuvAY6pgEEghoR%2BTtnazLC6WqOoWho6VHSYAetThJgB0on%2BytsvrpStKpNbDF6F2DMCDKuQ4eRQan1oei9JS0i7NoCmp8hqJSenKdSRV790os0yuSrrrBabBO1f6%2FytuMo79fqhYY7%2B5RY9ysTQ7D3jpFG%2FVouXDbK1UbyY0uAxTYfmU5OyklZaLFjwX7JZ9DZJrQNtbpxFmqfEmcHH0Aw1Fy66JzLE3ulXGuP&X-Amz-Signature=27fde847464cd4ee9f10b094ea9bc5ea7859f52b5363adfee7c1a3f43a4d6269&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIZVJAKK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICj1TjKrV5YyvGNlhL1ofrH%2BzpU%2Bp5PGzgo2ALHcnyEfAiA%2FYgrS%2FB5tQ5SsNTpXr9qwTdqVTZabtBVcV1zIl6NqrSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfmn2DhvhVky2yhoqKtwDfRRXremSc97nQuhYElUnm3E9h1I%2FveJc076%2FyHYgqcBKCn7keEcVJHHoziaRHzgqHHwp6zStUgRjkakmVzJYQZmdEM9BeSuoT5nhs0fYUcgTSs5AqLHNVEK6esKbZE4PL7Cpgm%2B8hIc%2Bq75XkkpvcPV5xoXxz1gzyo4pSYjSJX%2FeSkPO%2BsFladazxA5yWztahUSP0FvCWiXat7o6Obe8Xr3TFi2xhC0NJo0d34w9OcdEY0eFmpZn3WwvTSOAnIiu6LoTIqr1rlAAzmc5r%2BHTrrQK%2B8Dyxx8%2BnlJwx7XHTF7UO4EVABKZf7WL1qE32kGeBqB6ud%2Fudet%2FI8kpsDsGWjd0Fm8gSoFRhJaCqPeXNt1ZTeGlfCRpi9pswiWTDmIVtjvDTA42LMdx2OM76Rhdbmz0Mo%2B55yvu%2Bhr1HF1RNlKNsJ12S2DHfx806rzfYAAxdm%2BUbGAxrdfbd%2FkPylJRqfGJmPeSc9d%2BAjlKCHZ3iGPSjdnmNL4JlEcJAwS%2BDvx0tY06GSZXKXigS0hf1VV0oJQFopv%2FCw%2BUM%2BMUn45tQ9FgQGfzuKNu%2BM%2BS8xmQQKSp2rlzbMvNndTed%2BEwJVnxc205ESsbp1kAQYR8IH3SbU%2FHFms4W9aVZrFj4wgw35fuvAY6pgEEghoR%2BTtnazLC6WqOoWho6VHSYAetThJgB0on%2BytsvrpStKpNbDF6F2DMCDKuQ4eRQan1oei9JS0i7NoCmp8hqJSenKdSRV790os0yuSrrrBabBO1f6%2FytuMo79fqhYY7%2B5RY9ysTQ7D3jpFG%2FVouXDbK1UbyY0uAxTYfmU5OyklZaLFjwX7JZ9DZJrQNtbpxFmqfEmcHH0Aw1Fy66JzLE3ulXGuP&X-Amz-Signature=2324b799a9fb6c6cb23b675d3451795d7602da45e7b0c8df5d741e6f667e4548&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIZVJAKK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICj1TjKrV5YyvGNlhL1ofrH%2BzpU%2Bp5PGzgo2ALHcnyEfAiA%2FYgrS%2FB5tQ5SsNTpXr9qwTdqVTZabtBVcV1zIl6NqrSqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfmn2DhvhVky2yhoqKtwDfRRXremSc97nQuhYElUnm3E9h1I%2FveJc076%2FyHYgqcBKCn7keEcVJHHoziaRHzgqHHwp6zStUgRjkakmVzJYQZmdEM9BeSuoT5nhs0fYUcgTSs5AqLHNVEK6esKbZE4PL7Cpgm%2B8hIc%2Bq75XkkpvcPV5xoXxz1gzyo4pSYjSJX%2FeSkPO%2BsFladazxA5yWztahUSP0FvCWiXat7o6Obe8Xr3TFi2xhC0NJo0d34w9OcdEY0eFmpZn3WwvTSOAnIiu6LoTIqr1rlAAzmc5r%2BHTrrQK%2B8Dyxx8%2BnlJwx7XHTF7UO4EVABKZf7WL1qE32kGeBqB6ud%2Fudet%2FI8kpsDsGWjd0Fm8gSoFRhJaCqPeXNt1ZTeGlfCRpi9pswiWTDmIVtjvDTA42LMdx2OM76Rhdbmz0Mo%2B55yvu%2Bhr1HF1RNlKNsJ12S2DHfx806rzfYAAxdm%2BUbGAxrdfbd%2FkPylJRqfGJmPeSc9d%2BAjlKCHZ3iGPSjdnmNL4JlEcJAwS%2BDvx0tY06GSZXKXigS0hf1VV0oJQFopv%2FCw%2BUM%2BMUn45tQ9FgQGfzuKNu%2BM%2BS8xmQQKSp2rlzbMvNndTed%2BEwJVnxc205ESsbp1kAQYR8IH3SbU%2FHFms4W9aVZrFj4wgw35fuvAY6pgEEghoR%2BTtnazLC6WqOoWho6VHSYAetThJgB0on%2BytsvrpStKpNbDF6F2DMCDKuQ4eRQan1oei9JS0i7NoCmp8hqJSenKdSRV790os0yuSrrrBabBO1f6%2FytuMo79fqhYY7%2B5RY9ysTQ7D3jpFG%2FVouXDbK1UbyY0uAxTYfmU5OyklZaLFjwX7JZ9DZJrQNtbpxFmqfEmcHH0Aw1Fy66JzLE3ulXGuP&X-Amz-Signature=5cce1bed4fd68c8d868abd133a0da16a1f6709a2df8ad33e1520b96b8a8dbc1a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQM4XPNM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCl0pWicdmjbxLUq%2FfJHxUsuhhljAZg%2B4rIKjKwzxBxOgIhAOi1vFrXOm4m69fgAiYnkQv7EhuqyBU3MoreWBPvR8O0KogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7rDmIjYTSn5BAFGEq3ANYp7wqBgG9CPyNQLNpWIp0xFWIH%2BtuhXkV12ln8OJClg7dPZ0ZfIEbeFPdWdt4iTLh2zDZeyvMinbMi%2FdBxyd9ZKHwOzGOUROd6t1uhrAWR7B2br22OxxyhEFUvvYAkdDPSaLKSy86UejbQqYTDyKygDUueTmMO0yAv6JWpXHmAzCCsXFx5OpHx3vKGVp3vNRt%2Bpfl4h5%2BhJij2Y%2BwaXzWWBsC5QF%2Frd9OLWeArFVd1cJTFcDti2%2BrxAgCs4zJ6JkB%2BEXNlrVhxF5TSoAkxLf3eT5ZzJaF8SGF%2FU42BI%2FTUCroAENddj1t9FjDCWCnCciWZMnKroPCQGRUWs1d%2FqKGKfnk9UBJx3yjtz98xR9DzlkKlRuF19E31wy2wJvHbno5LxloGa46vczIGxJXBsYA%2FBesUIYxe0QAYjT2PPUBqZ3b139rlB1fDCJLg68H1cSedIBNADYIp10ky%2FpmAdl9YjAeu7tgShpD8yh4Asxd6l8pTdxa8LgeFsoAZyUeG5x%2Bh4n4pi2zWwcNNrZaY14hA0hnKc1WOnrTzU7VprFTjR6mUT%2BaYfNGj4ND7vdJVzzZjDZWPD%2B4BfEqqrCvXo%2F0fCCte7hA5HunfHBttCoCclS1Wr5qnUW6C8DI%2BTDfl%2B68BjqkAYZP0nUk5qO6Jx%2FORkpKgmCKrMux6BJYukTmEH3yhWDkuAUGXef99Kldz1OYc9F1bil1TCFxbYK4wb5bHzaJ%2FD6hTWEaJcUZnZZWJ7XPuJDMj8vntQTSYi8%2Fm%2BdvdAC5UZ%2Fiw919Dhi%2Fm17Yoc5c93oyuNjfw2ER%2FwlyEOu69mB2aybbSfr1%2B%2F3UKqtGxCit48X652t9b44DPyTYL4sRHxVCibwa&X-Amz-Signature=e1521af5c30215870af6e158f4541be65ba405f13010607ef46136194c09d95c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43WUSUP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDBKTbjnPW5S%2FSF0I2rdYrS2UHNcIlM4HFdMufpDvTBFAiEAgd9WZpUSw0CYy7nQbdxsrp9f8OwCRtwii7mGF0vZHtIqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOumpVlPm0Q8HYkmiyrcAxykleD7kpcyP7AX3UAutUOvVEK8ksJ8pH9WAIycQm5e3%2B5On0OlRL6yKSHqbIzcMSEjJgQzctobzubcuEkxtG6Crw145X4dlZyNxLtmCXR52k9uBlLSoeoljooAtCGjjyluw1%2F%2FDNGx74BoiI1gZXydbJl0l2h11IDziFz%2Fd6G6VOuG3vieua2bNK6j5eLLokjRu6axEUuVN4mQqhHQnsakN%2FvQHy1LaJjzK%2F8qqhpOoQRp4WklJn1R0GrckCrTgBNJowqxzMfikvlIjR4CSdigbxwmoJt6Pi0i3RXu0SZU5hDFwngtOVF7tvYbDx2FpCnpZlFv1dhkHf8zfK%2FML2De7aPVahocMLP1OEgwjJSTRHmwJ6SYzLxhKeCdZ3EB3EP4OJeDAO2ajdSBIFgaqIreb9kF9LPnB7eN2Viv6TosaFJEM1xOMABGk9zUugqHCsQ3rCiWc6l%2BGu%2F4PnihV4GmPxvOe5pFahAJcAKavLJCrRZ0R9HhYH2cTHKqWBGdEOV2RQLQknGEUtBVjWwCD%2F50PYBJW49Y8ErAlKjl5wzueAXzScW2wyo7dKtLld1SKN9Kj8MHAkSp6VZMhi18BpEQH72swGX0%2BLE5Y4Vz7CUAuMAInxBLsvqLuuICMJaX7rwGOqUB%2B41331qKjv6yCf%2FDxgwCpWIqcHCPz11I3rRKD%2FM7y8cH8Op0riuu9KUpHcUP3qXuyN9QbeTw6SFxl1TfkuKvcsJl5PXE66jp4%2FdmIT%2Bj601INBzEuP2lJPhXxsmq%2F9q%2BC2jUVnap89dus0Ria7zFrrJ0gh16WNFwVgt%2B08BkPNJYHdvuWkVryNSTnU39jWtFxr7PnjtEe%2FM6%2Fgtgjpm1xqFoVlAz&X-Amz-Signature=811020830d677dff430273dfe55919233217731abb38a0c0ac82f99a07373f6a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKSLLOLA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4zdB6C%2F9qam8o55gNgKpIZCdtz3qitBlRi%2Fj70ARBPAIgE%2FkmJ5ryyRh9noL2tJEHXOmNwraZtYNlTSTAvQK1exUqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCgN18H3VC3SL%2FgZHyrcA8yS%2B9eFvcqIQQrIyuKEjdS9ZtCJf2quxluzd2bKUzXiuTE6TI0jdHbWzhX0PTLGiTmpyiqvF4Hr%2F4F%2B7DZ15j%2FG6F2VsomsvrceDZe4xC22PKYdNmwmcmFfomdJ5QdLJ52Zg2HLz4y%2FLSP4z8jV87HurlloBDy6ZVa0UCL3dF4%2BXkgbQgsYJcAQ3TpFB7NhLqoS8K8KBtcTCNXS8b1wpxkpdjiPm6QxcdZhp6OtZUjVx8xzGcaoXho8XYCVRbolGibhn7dxhNqJ1nv2E3Dc%2FlzUjWYs%2FcN%2FHyZM%2FKcOWN8Q7a1r6SBxkP8aap0TJuD06ZqH9WARWahZCPPDDSAFtLSs0nRUXVDpVvskMo3EuYN2GZwZmp9wepa%2Bmjq9BvLMiiFdmk0npdpxE73uP1sn%2FM2Na4yczOW%2Bqp61JlZE363gTHnpt16zDpzHtUvqzZ1Q5qTlkLFvwGBzoYYZYBWjTvpGAjNwTXsDHz9km1IW%2Byf99q%2FOqiKHSx9ID5lJnjig6z%2BQOe40OXgQhsY58HqBePGypCETc7nt%2FFAmwwdTaCoH1AOszHsTx2D3sFRZYVbc58foUIobYFRswmfmrWfl2opNuRqSqWtIR7FAl5%2FgVRBSo70ecBXLOTns5U9SMIKX7rwGOqUB5dThwfGaCmVYoCRtsE2dFcKpjZXUfEVx%2Bx%2FTy17lrkWYwWYn68ZD%2Fb3%2Fs1bAbN8p8yXFcrXRwCgIqEnrWJpTsdNnp7HCqfgnlmatyt9MB9QwQzOW5O1YrFa6qVu4oafYWjgDpx%2B5u2weBTtr7zB%2FZ9UTs32U9E1nl99REy5qV8Qkh15ck0zmiLvjOhcIQbxqWQFVIJWqnsQas7h6BUV8ZP0Ve9wZ&X-Amz-Signature=1d369c9661bbc00ce0fbae6d3cb541a152d914b831cc46c679be646891c73a43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJWQ4NK2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGRny7Q2vbtZDeu0nnF62izJce0AjoDGn1y%2BErn8MkvlAiEAoL0eC1lE9TyLxCMZPtcgv5GWZ0LtPrQRnCZo3AGgEUAqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJmAR4q6ddk7K88BMCrcA%2FnFAsfhr7fVqCKCiT3UXMsAV41LwEVF9x2VKAcgBIoKXd2sGX0Z42%2BNlWrt5BPXK1N8X40bnayqM7T6M3TzOT2t20lep7Me26yA%2FC4ueBrlz09yXcW5HEi5mx1GtTZAa4bJwueMOUM4qhV8xOHKEija2nPQhfKzsaTfVXGkLEJiMMAhu47c8ODhWuk43MgOxSn6kxePjxPZlfbfmgIMrw6fVImJhx2vKtDtLdVc2sJUNeCFdajn7%2Bb4NFsvFPVTpsbCgHUHXRsoGYw3GHhRnXxdrGW9rhvIkrs5fj0LiBjwji9LiScprUgN300apd5oS0g3blfcW4YJVr94RfcqJdtkLmnYByX24aU6JlQ2gYMyyhq7AeLvSC6FK%2BeqLX5cPuTOGM2jKfqhOjEDmX2DQT2%2BaBTpta4X3JSrkaVP1XERGx3iVv0n%2BneeM5KrKVYZqOl8Nlmb3MiGp3xqpKrlVo2oJ9b7xlvxYvDL9%2FqEtB5oCTHGX2Yy9pPgitngw4VhpH1zGmPUV9sLerNR8%2B61N7N0FGW59CsG0qr%2BmjUaSukjkzfQj4uVguDuzlL%2FUWOCtoCw74AJcqbuyzMo0G5R4coJVGy7yKflbAJhHoM%2BNowBltNxWfCxkzqNZLggMJiY7rwGOqUButCEqv0%2Bwaz9%2Bf4LG54stjj5qWht1uYkSkRJ%2F9ytVX%2BW43gDJJ8SzCQxnAA4BplAyDx6XrtBC3ryPp%2FbyUNOr8TMQ8dSEzi6ve2MEDY94EVKZ8x0D9FumAzVqKfybwpJdnPjDCUUNoLDniBbuzSs7%2F4GrMxWq%2FwhlxcD64fiFDNI033odnvsWWg6KyDO37aoyIFsEi5a0387obmU7wSsLQbadEBm&X-Amz-Signature=1325db7da945051aca7d620077d940e7bb88fdcea66915bb4a61861ab1928c33&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJWQ4NK2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGRny7Q2vbtZDeu0nnF62izJce0AjoDGn1y%2BErn8MkvlAiEAoL0eC1lE9TyLxCMZPtcgv5GWZ0LtPrQRnCZo3AGgEUAqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJmAR4q6ddk7K88BMCrcA%2FnFAsfhr7fVqCKCiT3UXMsAV41LwEVF9x2VKAcgBIoKXd2sGX0Z42%2BNlWrt5BPXK1N8X40bnayqM7T6M3TzOT2t20lep7Me26yA%2FC4ueBrlz09yXcW5HEi5mx1GtTZAa4bJwueMOUM4qhV8xOHKEija2nPQhfKzsaTfVXGkLEJiMMAhu47c8ODhWuk43MgOxSn6kxePjxPZlfbfmgIMrw6fVImJhx2vKtDtLdVc2sJUNeCFdajn7%2Bb4NFsvFPVTpsbCgHUHXRsoGYw3GHhRnXxdrGW9rhvIkrs5fj0LiBjwji9LiScprUgN300apd5oS0g3blfcW4YJVr94RfcqJdtkLmnYByX24aU6JlQ2gYMyyhq7AeLvSC6FK%2BeqLX5cPuTOGM2jKfqhOjEDmX2DQT2%2BaBTpta4X3JSrkaVP1XERGx3iVv0n%2BneeM5KrKVYZqOl8Nlmb3MiGp3xqpKrlVo2oJ9b7xlvxYvDL9%2FqEtB5oCTHGX2Yy9pPgitngw4VhpH1zGmPUV9sLerNR8%2B61N7N0FGW59CsG0qr%2BmjUaSukjkzfQj4uVguDuzlL%2FUWOCtoCw74AJcqbuyzMo0G5R4coJVGy7yKflbAJhHoM%2BNowBltNxWfCxkzqNZLggMJiY7rwGOqUButCEqv0%2Bwaz9%2Bf4LG54stjj5qWht1uYkSkRJ%2F9ytVX%2BW43gDJJ8SzCQxnAA4BplAyDx6XrtBC3ryPp%2FbyUNOr8TMQ8dSEzi6ve2MEDY94EVKZ8x0D9FumAzVqKfybwpJdnPjDCUUNoLDniBbuzSs7%2F4GrMxWq%2FwhlxcD64fiFDNI033odnvsWWg6KyDO37aoyIFsEi5a0387obmU7wSsLQbadEBm&X-Amz-Signature=9c246cd6c52df72183d36fb4d1325d07071f00622b6f1437898782236a3b9911&X-Amz-SignedHeaders=host&x-id=GetObject)

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
