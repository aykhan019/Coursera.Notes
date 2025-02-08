

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EDQKKQN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCWAiP%2BqwvQYW08PjHcSxXpFqZb%2BV%2Bu6I1YUth8QFZHawIhAOpZKEj1IEfT2XMTV%2FnHUO6QVA0HTgqFNp%2BlrjLWQyHxKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5chgRlRqEXnjcbqsq3AP4kVUhNPUHmFfDQcfhzu3xKeBDfZwM1nG20gPx2Fbt%2BYEAGD4aQA270lxUHBIxA25PNsZEsuiq30YmfAJBwn99lmlG4ZeGM8mP4rNcKfHiAql0GAljwE8n855X8kSAvoCWNC9VRNjbkdUXpGFINgwACKPK3KsaEIRla%2FVCBjhlzHqslXtwcpDMMLj6r4wfBGgyX%2FnpDHddkwdYP2IGKDMmxC3emcLrA3BGlDyiiItWfvy%2FFogHMiSDoo5%2FvtEtWNN3mcFMmJIRGba0UTrqxM1uxmXej06lkhQN9jW%2BARVNWF5%2BKTMrkSnLGhyGPMs6%2B%2BmNjwpz3wf5iEgacGld3CZiP3qRQAoIPjcp6uEc%2Fs7Pr4jMyaqv1QP7TGfqwder0ce%2Bn2G02V2bPH3VzvQil0frzvXQboYy1TAso168kne2kBX3USNheNVn%2BjZXqlYo3rnzl2r7EiSknHJtO8%2FJecsfLRODhcbO0b11uIYC9olikhp2G8ix2TNGCyz86XB7ex%2F%2FIxg%2BDB%2FNuVBmBgwu5FSN8tpnajXODIEmr%2FS4xd5SRMIgLciieDix9wQeiVL89LCgJArqe13SzWBm6QWU2Fae87K096WP17r9DbAnvIVUKdI3da1TgWW%2FBu8KhDDOspu9BjqkASee2w6pdxGLbXu13Hhjl55NvlfvUCtbhC2wFAGJXWStuYKS8gryTOGqxP6TeuvHEWexRJ9MHERupPfIHgkb9BpamDO522at86E1TrmNhZaBzWkdAxL4OBAcaAzjejPL3fMRs6WeByrYofuUEyE2CHvvTW1%2F3Z0jqUv8CO%2Bka%2FLsFufYNxn0mXf6sTSoabVedSQCundxxkR0q05loaFmO2k2a6nz&X-Amz-Signature=376445ad92cb0863645aa6f9aadc8df82d37135a292f8c46b1179f361ab85bd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EDQKKQN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCWAiP%2BqwvQYW08PjHcSxXpFqZb%2BV%2Bu6I1YUth8QFZHawIhAOpZKEj1IEfT2XMTV%2FnHUO6QVA0HTgqFNp%2BlrjLWQyHxKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5chgRlRqEXnjcbqsq3AP4kVUhNPUHmFfDQcfhzu3xKeBDfZwM1nG20gPx2Fbt%2BYEAGD4aQA270lxUHBIxA25PNsZEsuiq30YmfAJBwn99lmlG4ZeGM8mP4rNcKfHiAql0GAljwE8n855X8kSAvoCWNC9VRNjbkdUXpGFINgwACKPK3KsaEIRla%2FVCBjhlzHqslXtwcpDMMLj6r4wfBGgyX%2FnpDHddkwdYP2IGKDMmxC3emcLrA3BGlDyiiItWfvy%2FFogHMiSDoo5%2FvtEtWNN3mcFMmJIRGba0UTrqxM1uxmXej06lkhQN9jW%2BARVNWF5%2BKTMrkSnLGhyGPMs6%2B%2BmNjwpz3wf5iEgacGld3CZiP3qRQAoIPjcp6uEc%2Fs7Pr4jMyaqv1QP7TGfqwder0ce%2Bn2G02V2bPH3VzvQil0frzvXQboYy1TAso168kne2kBX3USNheNVn%2BjZXqlYo3rnzl2r7EiSknHJtO8%2FJecsfLRODhcbO0b11uIYC9olikhp2G8ix2TNGCyz86XB7ex%2F%2FIxg%2BDB%2FNuVBmBgwu5FSN8tpnajXODIEmr%2FS4xd5SRMIgLciieDix9wQeiVL89LCgJArqe13SzWBm6QWU2Fae87K096WP17r9DbAnvIVUKdI3da1TgWW%2FBu8KhDDOspu9BjqkASee2w6pdxGLbXu13Hhjl55NvlfvUCtbhC2wFAGJXWStuYKS8gryTOGqxP6TeuvHEWexRJ9MHERupPfIHgkb9BpamDO522at86E1TrmNhZaBzWkdAxL4OBAcaAzjejPL3fMRs6WeByrYofuUEyE2CHvvTW1%2F3Z0jqUv8CO%2Bka%2FLsFufYNxn0mXf6sTSoabVedSQCundxxkR0q05loaFmO2k2a6nz&X-Amz-Signature=fd17c4b5c32ad94ec8c285ce0a53cebdee39fb867ac00bf86d90e2898f9ab02f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EDQKKQN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCWAiP%2BqwvQYW08PjHcSxXpFqZb%2BV%2Bu6I1YUth8QFZHawIhAOpZKEj1IEfT2XMTV%2FnHUO6QVA0HTgqFNp%2BlrjLWQyHxKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5chgRlRqEXnjcbqsq3AP4kVUhNPUHmFfDQcfhzu3xKeBDfZwM1nG20gPx2Fbt%2BYEAGD4aQA270lxUHBIxA25PNsZEsuiq30YmfAJBwn99lmlG4ZeGM8mP4rNcKfHiAql0GAljwE8n855X8kSAvoCWNC9VRNjbkdUXpGFINgwACKPK3KsaEIRla%2FVCBjhlzHqslXtwcpDMMLj6r4wfBGgyX%2FnpDHddkwdYP2IGKDMmxC3emcLrA3BGlDyiiItWfvy%2FFogHMiSDoo5%2FvtEtWNN3mcFMmJIRGba0UTrqxM1uxmXej06lkhQN9jW%2BARVNWF5%2BKTMrkSnLGhyGPMs6%2B%2BmNjwpz3wf5iEgacGld3CZiP3qRQAoIPjcp6uEc%2Fs7Pr4jMyaqv1QP7TGfqwder0ce%2Bn2G02V2bPH3VzvQil0frzvXQboYy1TAso168kne2kBX3USNheNVn%2BjZXqlYo3rnzl2r7EiSknHJtO8%2FJecsfLRODhcbO0b11uIYC9olikhp2G8ix2TNGCyz86XB7ex%2F%2FIxg%2BDB%2FNuVBmBgwu5FSN8tpnajXODIEmr%2FS4xd5SRMIgLciieDix9wQeiVL89LCgJArqe13SzWBm6QWU2Fae87K096WP17r9DbAnvIVUKdI3da1TgWW%2FBu8KhDDOspu9BjqkASee2w6pdxGLbXu13Hhjl55NvlfvUCtbhC2wFAGJXWStuYKS8gryTOGqxP6TeuvHEWexRJ9MHERupPfIHgkb9BpamDO522at86E1TrmNhZaBzWkdAxL4OBAcaAzjejPL3fMRs6WeByrYofuUEyE2CHvvTW1%2F3Z0jqUv8CO%2Bka%2FLsFufYNxn0mXf6sTSoabVedSQCundxxkR0q05loaFmO2k2a6nz&X-Amz-Signature=17cc77e4c1d10e85b49f0e149a3da860be986a99bf5452d2d3a836225fb29e7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWAVYVG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDKR7xihEcerzBlRVx5JZCE2BQhY%2Bnwed754gQ6TBnTugIhANQ7t%2BKd55ro1B0gRc8aC3ktzQmxVdBxtVFuFkPQFebQKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzD0rf%2BQOUMfLOIOGEq3AOywa76cBpI%2Bz7oZo1ThCDhEEdQ%2FASzl8PuKE%2FdKsFfj%2BCGfJS7Ip9WQ7TQgN1jJgifYhntyV7fPIKMQIQf8xUjLxa7DsyNyMK12jckRA%2FD7Qu6obu5%2BldCe4CQbx%2BUytvuxxfDLSRvbS%2FrJ3outW%2BF1uR6n%2BWzL9xWSLvX7ab1OmcWL6COZjGvTs9yBc%2FMIiE0bVg1D7l0CLcbQxmbgwygF7mIHF79NejWCQxS6Dl3yoAb8DzJ56fVPKxankDNSq5djZGghQ6NU2YdDcnHiktB%2BvvTDpIglvWsCx2gl4WKsKXSjAsYviqGKxZJZmba2sHTZk0mj4d%2Bf6ooiLygDA%2BEtV6Ave19b03DvAzQA9eUkf58dIEU0ZfV%2FmxUyRLVzzojh4ffH4TvjTj%2FAi8a%2FAuRvuV999KiWNYDGm69SgLwg42v7pTrW97SlMHRrtwt9L9CLetgIccvf9%2FAqmSpI5KeXvboZVANgdZC0EuI8iLsmi3%2FvTyncHEjb1GPkBYxLy4DWSld71RiSWPSJ9edeKQv%2Bg6R%2BfIuSEptfu%2BRQjYfQcOaHPBaHYwOZUgSyqk7wBApfKpO%2BzPQ5eX0D5Gn8%2Frp6evJ2QK0YDLtB%2BkwamNiq4K%2FqmoqgBkPZp8UjDDTspu9BjqkAY9CNU9992h53MLVghm7ONeBkuQ9i75vUvaLo%2B4a904HES7F61BOceYsdXIhDvWVizDvbsYiP3pJ2SRiZdTWR8ZyHmJV75ZWNkM%2FZterkGnP7VTMjyNefOLjTLvET60B1e1YF0ta8uHvQ%2FOCLKtyqczV8LzBpfdiu2On2ZOYPCsQiVE2jnRVDM5v7Dg1wNq%2FOCgNRNlYlGKpHPgQWhwOwcDxrDQ1&X-Amz-Signature=b71c9a44c95344f5eb1f1d7dcacdae219c59a757c38ea72b2ba4bc74d07541c9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWAVYVG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDKR7xihEcerzBlRVx5JZCE2BQhY%2Bnwed754gQ6TBnTugIhANQ7t%2BKd55ro1B0gRc8aC3ktzQmxVdBxtVFuFkPQFebQKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzD0rf%2BQOUMfLOIOGEq3AOywa76cBpI%2Bz7oZo1ThCDhEEdQ%2FASzl8PuKE%2FdKsFfj%2BCGfJS7Ip9WQ7TQgN1jJgifYhntyV7fPIKMQIQf8xUjLxa7DsyNyMK12jckRA%2FD7Qu6obu5%2BldCe4CQbx%2BUytvuxxfDLSRvbS%2FrJ3outW%2BF1uR6n%2BWzL9xWSLvX7ab1OmcWL6COZjGvTs9yBc%2FMIiE0bVg1D7l0CLcbQxmbgwygF7mIHF79NejWCQxS6Dl3yoAb8DzJ56fVPKxankDNSq5djZGghQ6NU2YdDcnHiktB%2BvvTDpIglvWsCx2gl4WKsKXSjAsYviqGKxZJZmba2sHTZk0mj4d%2Bf6ooiLygDA%2BEtV6Ave19b03DvAzQA9eUkf58dIEU0ZfV%2FmxUyRLVzzojh4ffH4TvjTj%2FAi8a%2FAuRvuV999KiWNYDGm69SgLwg42v7pTrW97SlMHRrtwt9L9CLetgIccvf9%2FAqmSpI5KeXvboZVANgdZC0EuI8iLsmi3%2FvTyncHEjb1GPkBYxLy4DWSld71RiSWPSJ9edeKQv%2Bg6R%2BfIuSEptfu%2BRQjYfQcOaHPBaHYwOZUgSyqk7wBApfKpO%2BzPQ5eX0D5Gn8%2Frp6evJ2QK0YDLtB%2BkwamNiq4K%2FqmoqgBkPZp8UjDDTspu9BjqkAY9CNU9992h53MLVghm7ONeBkuQ9i75vUvaLo%2B4a904HES7F61BOceYsdXIhDvWVizDvbsYiP3pJ2SRiZdTWR8ZyHmJV75ZWNkM%2FZterkGnP7VTMjyNefOLjTLvET60B1e1YF0ta8uHvQ%2FOCLKtyqczV8LzBpfdiu2On2ZOYPCsQiVE2jnRVDM5v7Dg1wNq%2FOCgNRNlYlGKpHPgQWhwOwcDxrDQ1&X-Amz-Signature=39ebe6d1bf91f366d2eec880b7cd4ff1c7d890f087f87f5bf5bc813e2ab43b83&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWAVYVG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDKR7xihEcerzBlRVx5JZCE2BQhY%2Bnwed754gQ6TBnTugIhANQ7t%2BKd55ro1B0gRc8aC3ktzQmxVdBxtVFuFkPQFebQKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzD0rf%2BQOUMfLOIOGEq3AOywa76cBpI%2Bz7oZo1ThCDhEEdQ%2FASzl8PuKE%2FdKsFfj%2BCGfJS7Ip9WQ7TQgN1jJgifYhntyV7fPIKMQIQf8xUjLxa7DsyNyMK12jckRA%2FD7Qu6obu5%2BldCe4CQbx%2BUytvuxxfDLSRvbS%2FrJ3outW%2BF1uR6n%2BWzL9xWSLvX7ab1OmcWL6COZjGvTs9yBc%2FMIiE0bVg1D7l0CLcbQxmbgwygF7mIHF79NejWCQxS6Dl3yoAb8DzJ56fVPKxankDNSq5djZGghQ6NU2YdDcnHiktB%2BvvTDpIglvWsCx2gl4WKsKXSjAsYviqGKxZJZmba2sHTZk0mj4d%2Bf6ooiLygDA%2BEtV6Ave19b03DvAzQA9eUkf58dIEU0ZfV%2FmxUyRLVzzojh4ffH4TvjTj%2FAi8a%2FAuRvuV999KiWNYDGm69SgLwg42v7pTrW97SlMHRrtwt9L9CLetgIccvf9%2FAqmSpI5KeXvboZVANgdZC0EuI8iLsmi3%2FvTyncHEjb1GPkBYxLy4DWSld71RiSWPSJ9edeKQv%2Bg6R%2BfIuSEptfu%2BRQjYfQcOaHPBaHYwOZUgSyqk7wBApfKpO%2BzPQ5eX0D5Gn8%2Frp6evJ2QK0YDLtB%2BkwamNiq4K%2FqmoqgBkPZp8UjDDTspu9BjqkAY9CNU9992h53MLVghm7ONeBkuQ9i75vUvaLo%2B4a904HES7F61BOceYsdXIhDvWVizDvbsYiP3pJ2SRiZdTWR8ZyHmJV75ZWNkM%2FZterkGnP7VTMjyNefOLjTLvET60B1e1YF0ta8uHvQ%2FOCLKtyqczV8LzBpfdiu2On2ZOYPCsQiVE2jnRVDM5v7Dg1wNq%2FOCgNRNlYlGKpHPgQWhwOwcDxrDQ1&X-Amz-Signature=c9c4f860bea84b3e93b64edf5a06900cb2694031ca54af05e024d61166587dab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWAVYVG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDKR7xihEcerzBlRVx5JZCE2BQhY%2Bnwed754gQ6TBnTugIhANQ7t%2BKd55ro1B0gRc8aC3ktzQmxVdBxtVFuFkPQFebQKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzD0rf%2BQOUMfLOIOGEq3AOywa76cBpI%2Bz7oZo1ThCDhEEdQ%2FASzl8PuKE%2FdKsFfj%2BCGfJS7Ip9WQ7TQgN1jJgifYhntyV7fPIKMQIQf8xUjLxa7DsyNyMK12jckRA%2FD7Qu6obu5%2BldCe4CQbx%2BUytvuxxfDLSRvbS%2FrJ3outW%2BF1uR6n%2BWzL9xWSLvX7ab1OmcWL6COZjGvTs9yBc%2FMIiE0bVg1D7l0CLcbQxmbgwygF7mIHF79NejWCQxS6Dl3yoAb8DzJ56fVPKxankDNSq5djZGghQ6NU2YdDcnHiktB%2BvvTDpIglvWsCx2gl4WKsKXSjAsYviqGKxZJZmba2sHTZk0mj4d%2Bf6ooiLygDA%2BEtV6Ave19b03DvAzQA9eUkf58dIEU0ZfV%2FmxUyRLVzzojh4ffH4TvjTj%2FAi8a%2FAuRvuV999KiWNYDGm69SgLwg42v7pTrW97SlMHRrtwt9L9CLetgIccvf9%2FAqmSpI5KeXvboZVANgdZC0EuI8iLsmi3%2FvTyncHEjb1GPkBYxLy4DWSld71RiSWPSJ9edeKQv%2Bg6R%2BfIuSEptfu%2BRQjYfQcOaHPBaHYwOZUgSyqk7wBApfKpO%2BzPQ5eX0D5Gn8%2Frp6evJ2QK0YDLtB%2BkwamNiq4K%2FqmoqgBkPZp8UjDDTspu9BjqkAY9CNU9992h53MLVghm7ONeBkuQ9i75vUvaLo%2B4a904HES7F61BOceYsdXIhDvWVizDvbsYiP3pJ2SRiZdTWR8ZyHmJV75ZWNkM%2FZterkGnP7VTMjyNefOLjTLvET60B1e1YF0ta8uHvQ%2FOCLKtyqczV8LzBpfdiu2On2ZOYPCsQiVE2jnRVDM5v7Dg1wNq%2FOCgNRNlYlGKpHPgQWhwOwcDxrDQ1&X-Amz-Signature=455e47e17a0d8a17dfe84f0649ce26894fd46c50f6670057eb14caa42b712219&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWAVYVG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDKR7xihEcerzBlRVx5JZCE2BQhY%2Bnwed754gQ6TBnTugIhANQ7t%2BKd55ro1B0gRc8aC3ktzQmxVdBxtVFuFkPQFebQKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzD0rf%2BQOUMfLOIOGEq3AOywa76cBpI%2Bz7oZo1ThCDhEEdQ%2FASzl8PuKE%2FdKsFfj%2BCGfJS7Ip9WQ7TQgN1jJgifYhntyV7fPIKMQIQf8xUjLxa7DsyNyMK12jckRA%2FD7Qu6obu5%2BldCe4CQbx%2BUytvuxxfDLSRvbS%2FrJ3outW%2BF1uR6n%2BWzL9xWSLvX7ab1OmcWL6COZjGvTs9yBc%2FMIiE0bVg1D7l0CLcbQxmbgwygF7mIHF79NejWCQxS6Dl3yoAb8DzJ56fVPKxankDNSq5djZGghQ6NU2YdDcnHiktB%2BvvTDpIglvWsCx2gl4WKsKXSjAsYviqGKxZJZmba2sHTZk0mj4d%2Bf6ooiLygDA%2BEtV6Ave19b03DvAzQA9eUkf58dIEU0ZfV%2FmxUyRLVzzojh4ffH4TvjTj%2FAi8a%2FAuRvuV999KiWNYDGm69SgLwg42v7pTrW97SlMHRrtwt9L9CLetgIccvf9%2FAqmSpI5KeXvboZVANgdZC0EuI8iLsmi3%2FvTyncHEjb1GPkBYxLy4DWSld71RiSWPSJ9edeKQv%2Bg6R%2BfIuSEptfu%2BRQjYfQcOaHPBaHYwOZUgSyqk7wBApfKpO%2BzPQ5eX0D5Gn8%2Frp6evJ2QK0YDLtB%2BkwamNiq4K%2FqmoqgBkPZp8UjDDTspu9BjqkAY9CNU9992h53MLVghm7ONeBkuQ9i75vUvaLo%2B4a904HES7F61BOceYsdXIhDvWVizDvbsYiP3pJ2SRiZdTWR8ZyHmJV75ZWNkM%2FZterkGnP7VTMjyNefOLjTLvET60B1e1YF0ta8uHvQ%2FOCLKtyqczV8LzBpfdiu2On2ZOYPCsQiVE2jnRVDM5v7Dg1wNq%2FOCgNRNlYlGKpHPgQWhwOwcDxrDQ1&X-Amz-Signature=35389c30cd55330201a7fbd82bc580e69622ce4cfec7ee35aa45b13fc31bdb75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWAVYVG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDKR7xihEcerzBlRVx5JZCE2BQhY%2Bnwed754gQ6TBnTugIhANQ7t%2BKd55ro1B0gRc8aC3ktzQmxVdBxtVFuFkPQFebQKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzD0rf%2BQOUMfLOIOGEq3AOywa76cBpI%2Bz7oZo1ThCDhEEdQ%2FASzl8PuKE%2FdKsFfj%2BCGfJS7Ip9WQ7TQgN1jJgifYhntyV7fPIKMQIQf8xUjLxa7DsyNyMK12jckRA%2FD7Qu6obu5%2BldCe4CQbx%2BUytvuxxfDLSRvbS%2FrJ3outW%2BF1uR6n%2BWzL9xWSLvX7ab1OmcWL6COZjGvTs9yBc%2FMIiE0bVg1D7l0CLcbQxmbgwygF7mIHF79NejWCQxS6Dl3yoAb8DzJ56fVPKxankDNSq5djZGghQ6NU2YdDcnHiktB%2BvvTDpIglvWsCx2gl4WKsKXSjAsYviqGKxZJZmba2sHTZk0mj4d%2Bf6ooiLygDA%2BEtV6Ave19b03DvAzQA9eUkf58dIEU0ZfV%2FmxUyRLVzzojh4ffH4TvjTj%2FAi8a%2FAuRvuV999KiWNYDGm69SgLwg42v7pTrW97SlMHRrtwt9L9CLetgIccvf9%2FAqmSpI5KeXvboZVANgdZC0EuI8iLsmi3%2FvTyncHEjb1GPkBYxLy4DWSld71RiSWPSJ9edeKQv%2Bg6R%2BfIuSEptfu%2BRQjYfQcOaHPBaHYwOZUgSyqk7wBApfKpO%2BzPQ5eX0D5Gn8%2Frp6evJ2QK0YDLtB%2BkwamNiq4K%2FqmoqgBkPZp8UjDDTspu9BjqkAY9CNU9992h53MLVghm7ONeBkuQ9i75vUvaLo%2B4a904HES7F61BOceYsdXIhDvWVizDvbsYiP3pJ2SRiZdTWR8ZyHmJV75ZWNkM%2FZterkGnP7VTMjyNefOLjTLvET60B1e1YF0ta8uHvQ%2FOCLKtyqczV8LzBpfdiu2On2ZOYPCsQiVE2jnRVDM5v7Dg1wNq%2FOCgNRNlYlGKpHPgQWhwOwcDxrDQ1&X-Amz-Signature=1ebe0bb13d3e398298c0d9aae88c460c2d5704621a2a9f0a9bfb69dba15b1a5d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHWUFN7R%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQC1jE4qZ2bxGuQOkSaJ9yEb0VlxAXmqBw0cuO73D6F9RAIhAPUD47s5q8fKFVnK6fn3b74E0l5TL72%2FdPDomNjR60s4KogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyR%2BCRl5gIhgREG1Goq3APvGH%2FMx9Xx0r9wWT6AjpVO4DX%2BRuSvPUhYlJ%2BoNNBcIoZaBobuC6SJNg8jJXF3K24hvJYAJdMl9ZjdQzg7o%2FuoV9KbJFqwnZhvlyP6iWSESXffanyVX0%2BKtF5NswhQTh3z6b42SJPz%2Bbcprg%2FU3IO25yXCgwgHLKgRiWlHlo2Zyl%2FqAYR3%2Fuu7glorMNuw9i0ulPcUBmti%2B52P%2BzpGXLEUU4VRbk7Hp6nsgRNEiRmRCypANQzJvrC6XIlyQxB2BSH7d0ssskHBz8fQWMNFai9q8YhK8IGJSjdHE0BB7NkAnllIKSH%2Feh7MFcVxRpD%2BUvUZgRSHNxf3FGnF9RkonZ9KHtSvT%2Bj5xi%2Bk4SS3oQhqfn%2BlqispGvkMlcdXT7rr%2F%2FX8uH%2B7XM62y%2ByL5zP5j9YR9cJq28ShU5iqcPG%2F3t0KyOPBk3hJLxbYvWA46EivwfiYwJ55M5YhUxj02GMWUeITKVgbIZxYyNIQa9k3QMVwrW1vIrUnHQxtYYkB7Ambw3nPbxyqyO%2Fjjpzn3FJTItMo7BlUUDYAqihX43rhTcKlDWiYyeWoYHK5qzKWmhDRgi85Xtwvs%2FW29jqYuVfF9h0FboLWqMh1DVb4Op5MibtwyXr6y7tnck2INw86CjCospu9BjqkAbEzdIZ5y2D1t6dyJtpGxjTk94RYyc2Ho2SG66LyN4h4ou6Q%2Bm5Bd6SJwGkXzbLuz5vTbkG0wr9xW5%2F67euhq5GzRoJV8aPHvSMb8OZR0h2BZNkCOQI2m1RyXMBws4DFVwnHbqeXhGBFeA6QaXyfrmNIgujMk5ssLTVT1LJd0nz5k0Vf%2B4gY7MVoWYI9RkbOogHoBhuVV%2Fw2auLOwly2s%2Fu6Dm7%2F&X-Amz-Signature=5441e888a042ef0a4c998d0692932c4c92a845b44dfafde79319dd3ccfdec9b5&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SSBKMUH%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCbJZhJWrpzVh0QlMhLFcY%2FHbDZm5DpWLTFGO2shGeYgQIhAI7xwxy9bk46RBcDLEszY9C9qRmGTCakFr9hvmLBTbPJKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGqdDo7a2gmZvEhnAq3ANmQz2WSdnyL2ttNiHe3R9mfEkGvqcHfNQUS1N98X2i%2FF73Bh8vU3UtL6wENEqGUND3477MiQkfnjL5yZE0FU43RcTPMdVxfVedNjqODCv5eL72rIVRmBHkvTESN9DgXycd%2FsX9AzJduJ2aNM0qksfKHnWBg0KSwK7P5m7g7sh5lL92MlzfNtkVt2OWDAoY8aX2UIAHnb0A4R10xhN85jQsXGUUmBDsK8hYD9NJa7IBxfhSZgIDkuT1oi8yfdgOGCVDEX3KxAWBJeUjAI9H%2FV4L%2B4HrHJkG%2FzPFXifklemzotwpbr4GZlGN8iE1IkHemmJSnCzlYqgywusW%2FWWg7M4mWDwB94u8KZhXAXle3zKConeBxIliN3oiMRDpaVppIuHVZiBUxK53jVuWNaAYEngrMnlHpK7mightY3geIypuDIk5e7SC80XrDRi4HfRje9Li11s57%2BWumVfTtapQZDsL2RUkl2zl63HR3Yy1Y4i72eJOmXnxr9iX0P5oaAZ5niJKa6Zakb7xvz63oIALrwZOPoDu2F%2B5zDdfEUgwJbMNWrCu4oprVpJ82A%2BvSKgi1HU4NasWGRa6RxUp4AISL5zIb0GAlliyuo0UMPx%2BvQOOCYhlikNoiAtykf9FLDDgspu9BjqkATbAh0n5kX8j7tm7Ao1CEOCfKd97yKTJpYAcL%2FNK6sk%2Fd23sXvJJWY%2FeKDbOyfNgYSuwCneBnz8%2FM3WufPt6dhhUDV%2BDtxiFrGBWE18bXcbjEnaRu5EWMsnQwrcRSq94uiWCy0ev%2FJkPEkmPzJt9nfbNltKI1vw2YIeNobjWHjVHwSWFM5EE7Wxjwz09u7IYRvaPXU4oj71yMcoZmbVsY9YeAFWV&X-Amz-Signature=2a3be630a604ca92937104bd316c0706c381a9521d5a11bb5637ce415463ec3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWAVYVG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDKR7xihEcerzBlRVx5JZCE2BQhY%2Bnwed754gQ6TBnTugIhANQ7t%2BKd55ro1B0gRc8aC3ktzQmxVdBxtVFuFkPQFebQKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzD0rf%2BQOUMfLOIOGEq3AOywa76cBpI%2Bz7oZo1ThCDhEEdQ%2FASzl8PuKE%2FdKsFfj%2BCGfJS7Ip9WQ7TQgN1jJgifYhntyV7fPIKMQIQf8xUjLxa7DsyNyMK12jckRA%2FD7Qu6obu5%2BldCe4CQbx%2BUytvuxxfDLSRvbS%2FrJ3outW%2BF1uR6n%2BWzL9xWSLvX7ab1OmcWL6COZjGvTs9yBc%2FMIiE0bVg1D7l0CLcbQxmbgwygF7mIHF79NejWCQxS6Dl3yoAb8DzJ56fVPKxankDNSq5djZGghQ6NU2YdDcnHiktB%2BvvTDpIglvWsCx2gl4WKsKXSjAsYviqGKxZJZmba2sHTZk0mj4d%2Bf6ooiLygDA%2BEtV6Ave19b03DvAzQA9eUkf58dIEU0ZfV%2FmxUyRLVzzojh4ffH4TvjTj%2FAi8a%2FAuRvuV999KiWNYDGm69SgLwg42v7pTrW97SlMHRrtwt9L9CLetgIccvf9%2FAqmSpI5KeXvboZVANgdZC0EuI8iLsmi3%2FvTyncHEjb1GPkBYxLy4DWSld71RiSWPSJ9edeKQv%2Bg6R%2BfIuSEptfu%2BRQjYfQcOaHPBaHYwOZUgSyqk7wBApfKpO%2BzPQ5eX0D5Gn8%2Frp6evJ2QK0YDLtB%2BkwamNiq4K%2FqmoqgBkPZp8UjDDTspu9BjqkAY9CNU9992h53MLVghm7ONeBkuQ9i75vUvaLo%2B4a904HES7F61BOceYsdXIhDvWVizDvbsYiP3pJ2SRiZdTWR8ZyHmJV75ZWNkM%2FZterkGnP7VTMjyNefOLjTLvET60B1e1YF0ta8uHvQ%2FOCLKtyqczV8LzBpfdiu2On2ZOYPCsQiVE2jnRVDM5v7Dg1wNq%2FOCgNRNlYlGKpHPgQWhwOwcDxrDQ1&X-Amz-Signature=58420f912e28625057a9709df6e75a5a386f2f87bbe30fa6f17959f5f2ea47ea&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWAVYVG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDKR7xihEcerzBlRVx5JZCE2BQhY%2Bnwed754gQ6TBnTugIhANQ7t%2BKd55ro1B0gRc8aC3ktzQmxVdBxtVFuFkPQFebQKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzD0rf%2BQOUMfLOIOGEq3AOywa76cBpI%2Bz7oZo1ThCDhEEdQ%2FASzl8PuKE%2FdKsFfj%2BCGfJS7Ip9WQ7TQgN1jJgifYhntyV7fPIKMQIQf8xUjLxa7DsyNyMK12jckRA%2FD7Qu6obu5%2BldCe4CQbx%2BUytvuxxfDLSRvbS%2FrJ3outW%2BF1uR6n%2BWzL9xWSLvX7ab1OmcWL6COZjGvTs9yBc%2FMIiE0bVg1D7l0CLcbQxmbgwygF7mIHF79NejWCQxS6Dl3yoAb8DzJ56fVPKxankDNSq5djZGghQ6NU2YdDcnHiktB%2BvvTDpIglvWsCx2gl4WKsKXSjAsYviqGKxZJZmba2sHTZk0mj4d%2Bf6ooiLygDA%2BEtV6Ave19b03DvAzQA9eUkf58dIEU0ZfV%2FmxUyRLVzzojh4ffH4TvjTj%2FAi8a%2FAuRvuV999KiWNYDGm69SgLwg42v7pTrW97SlMHRrtwt9L9CLetgIccvf9%2FAqmSpI5KeXvboZVANgdZC0EuI8iLsmi3%2FvTyncHEjb1GPkBYxLy4DWSld71RiSWPSJ9edeKQv%2Bg6R%2BfIuSEptfu%2BRQjYfQcOaHPBaHYwOZUgSyqk7wBApfKpO%2BzPQ5eX0D5Gn8%2Frp6evJ2QK0YDLtB%2BkwamNiq4K%2FqmoqgBkPZp8UjDDTspu9BjqkAY9CNU9992h53MLVghm7ONeBkuQ9i75vUvaLo%2B4a904HES7F61BOceYsdXIhDvWVizDvbsYiP3pJ2SRiZdTWR8ZyHmJV75ZWNkM%2FZterkGnP7VTMjyNefOLjTLvET60B1e1YF0ta8uHvQ%2FOCLKtyqczV8LzBpfdiu2On2ZOYPCsQiVE2jnRVDM5v7Dg1wNq%2FOCgNRNlYlGKpHPgQWhwOwcDxrDQ1&X-Amz-Signature=d466256f41764613ff42e6559a0856f7d20c0b40bed1c62f003671f6848268c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWAVYVG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDKR7xihEcerzBlRVx5JZCE2BQhY%2Bnwed754gQ6TBnTugIhANQ7t%2BKd55ro1B0gRc8aC3ktzQmxVdBxtVFuFkPQFebQKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzD0rf%2BQOUMfLOIOGEq3AOywa76cBpI%2Bz7oZo1ThCDhEEdQ%2FASzl8PuKE%2FdKsFfj%2BCGfJS7Ip9WQ7TQgN1jJgifYhntyV7fPIKMQIQf8xUjLxa7DsyNyMK12jckRA%2FD7Qu6obu5%2BldCe4CQbx%2BUytvuxxfDLSRvbS%2FrJ3outW%2BF1uR6n%2BWzL9xWSLvX7ab1OmcWL6COZjGvTs9yBc%2FMIiE0bVg1D7l0CLcbQxmbgwygF7mIHF79NejWCQxS6Dl3yoAb8DzJ56fVPKxankDNSq5djZGghQ6NU2YdDcnHiktB%2BvvTDpIglvWsCx2gl4WKsKXSjAsYviqGKxZJZmba2sHTZk0mj4d%2Bf6ooiLygDA%2BEtV6Ave19b03DvAzQA9eUkf58dIEU0ZfV%2FmxUyRLVzzojh4ffH4TvjTj%2FAi8a%2FAuRvuV999KiWNYDGm69SgLwg42v7pTrW97SlMHRrtwt9L9CLetgIccvf9%2FAqmSpI5KeXvboZVANgdZC0EuI8iLsmi3%2FvTyncHEjb1GPkBYxLy4DWSld71RiSWPSJ9edeKQv%2Bg6R%2BfIuSEptfu%2BRQjYfQcOaHPBaHYwOZUgSyqk7wBApfKpO%2BzPQ5eX0D5Gn8%2Frp6evJ2QK0YDLtB%2BkwamNiq4K%2FqmoqgBkPZp8UjDDTspu9BjqkAY9CNU9992h53MLVghm7ONeBkuQ9i75vUvaLo%2B4a904HES7F61BOceYsdXIhDvWVizDvbsYiP3pJ2SRiZdTWR8ZyHmJV75ZWNkM%2FZterkGnP7VTMjyNefOLjTLvET60B1e1YF0ta8uHvQ%2FOCLKtyqczV8LzBpfdiu2On2ZOYPCsQiVE2jnRVDM5v7Dg1wNq%2FOCgNRNlYlGKpHPgQWhwOwcDxrDQ1&X-Amz-Signature=52fe20987fe67e71e46f88e20786255c7f912ce8c672a98c017928ab6d2575bc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBX6BVQY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCoLTIzuIorZi12Ua32N2VRAwF61%2FtcXWO1%2BK6IP4fcbwIgeMxEKssklz43RSqe1hsun4UVSowpTH6sqnKEjs0ID2MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3cerhazYesyTBt0CrcA94iT607%2F96cwb5rs1jH%2BPSYUzz7Q1Ds78yWkO7EfBz2KwYrPOl1Ems%2FUSJ8NNAvCzMMZOUdurb0Jj%2F0YLbGlhzH3ADbgCUfsden7a7%2Bt6lGe6rDRz32d4rNYhSETnNhVlhn0Ux04CdPeK6C0xunTwK9tN2dyS4qtKkYkHYCI8v8CBvA4rttwam5OV%2F1fo%2BM4i4BSwz3OPNbmg784hDQl0fh%2FP70N6icQ7fM6rpXJObEHRApO9USlhtUn2%2FsQVPkSapKTebKB2%2FeUU5jI4yHj31fLTMDQ8J%2FpI5X8hzZjRKe%2BABqqRwdayWfzK55waLoLADSXs1uT7xhqbzqynUrcCJyp2H3c1xPUsFYEMcgp78rdZSwyw7lreGygnh6hM4zvQpqWIq2agQKtLQ4xxZ9oqR7HkZKTEG1QNidh%2BusfHh%2BSc4HMfK4MQ%2FqeywrlgGMqKNSnUgVw095akjiU9ov6CYdzsXuA3fpNELUYvXo61IxCWsuzOQdp5%2BG5P0Eb0pqDmYyFG4fQA0aaEeKKnmydmo4zUr1vAONfzbPv8Plzr6K1Ch%2BbYEt1%2Fz%2Bx%2FSYbGy1Sjjo67BfZMfWio34h%2BQC2UmxqxU5%2BWG%2FECaV3cFbFvaCOwweaPLrMJUOFOfJMKiym70GOqUBGwtktze%2F13Ra3gAxcEkLTwD75eIDHF2QQc%2FO4DqdGf2aK%2FBjp8C9JwSydmoNE%2B3T63e4XPjm4bMMPzqTXRGVups6ciVPJCmj4HeMAmHSWKUYCW03XNRoZc6ITnqPlgFk3sKm5DE3m1yrHuQn5Ycpf%2F1LDBG%2B0gDSKYzaScj%2FXAuOcrmRwVhdmyK54YUNmNcSdZnEfQ00PDOk9RxImcKCIzUTyUbJ&X-Amz-Signature=59cfcccd1f910b5fc77767373f75e4276147cf86b2ea03ecf62fe6775903af2a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRJEV2FR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIFM1Lshoq%2BFruoebld%2Bn5UYkAURir%2B6W6f845LIXRoe8AiEA1rrPr2r8ClsUl1eroLVZ8ydymPMSabQCeD4fXB1c2REqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHF9n0y6oJPRmVgOyCrcA1gV5af8T5lfJndwOLUk0aH5CVshCO5LduBXP9jPSeexSAqgNbwqKClBL6t1l8AonI%2FwJ8R9wD4zo4AgS5Fo%2FnVkK4MfjbY%2BreSGIpAfmEYRirz4jZ2Kz1%2Bd09t1ncMCFYTE%2FjIQiclFl5tv9g7RVUiBDGoXz1mIQuWKbqGNKk6v1OSyUyZMQ%2BRXzNaJiSo5%2FCwU%2FKfdfnfDTrwesfCUR7p%2FyJX4byzQCd5J%2BVS807Ea5GDhxH9wS3fhS11Cy%2BDB7QROU611IJxUwHHQYm%2BdDFapu8gf1IGz48MxVulfQnBaidymLors2TxJ0uIg01rtJ2mc2G%2FZOS7KWeQcVC95i6xluo3htW4K6tZPTQGPd2Y0VYGpsW3XY%2BMQ9Qbihf3rEPXC3f%2FdhGPySsj3dJvIjFyDD%2Ffjnw7kZJwXOg27a%2BJFIgxTV9bJVnV9B%2BRqDxrv%2FzTwkFWUZg7bLbTw8EWxlNQgMZ6R9CK62th4mNKHB3kzF7247SHtCrIw9Wz7oPeFme6OiZzgYMEVy48GeziSsdnxO2UTUfP53nwj1s1w0QVChLmrqlrlLXCj7ugJdfLBeg495ug9f3L%2Bkaa55vnCSVkQsLTlwUv8%2FJRy12He7fB85fFirq0gm1LIjrG7MOCym70GOqUBmDqCsTfaNwz60aXDbYgDmV0lNW1T0pdxy%2BXtziecTQWdq9xTTRPz7U1BNu8ERUS%2BqdvMhxlt6YDY4TQib9hXBFMCCsroGeYqsD8cd6j%2BUSQ5bkI%2F21b7vKxcjFf3vnysqMAiB%2FO0wjyexJbzLDr0WvQ86dnbvCFPhEBHjpuNSEQg8%2FXRv6R4yzRRVaXwhIGcUG6rkZwZND6Be9dNzlCWjwiuxanX&X-Amz-Signature=8b226b47272361f6992320e7cd7efbbeec9862755365357330202a3a19581ed7&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUXBCJFU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQD58triC637PgKMCR8vQ93Dzs1B9miK6VeAVriMGXj4KgIgMfcpbdtHc5XKFVtKDKWEBeoppH0WBEw1Bt9e5WKT8TkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJpdDrTcb6ZWmrYk8CrcA8j%2BHJaA2TsRDpdfIp2HR7vhJbwHQEcxO4wRNcsmDuHXdYu6F1YJP5RjjJPu6KhCi7XzBElSnRDOKZLXlnkvtoQxB5mB1AGpv4Q8EF8O5ZJjcskr%2BEM8wZ5AAFNvG%2BvqydT9Gyw8CXyc5bYg%2FiVY8JJgtSNGJWbhb323Ai1VR76dXmDhyChhlXPUNccU5BulIM9QndSpv6naR1JAI%2BApxgJ7HbSdZdbNqx2r5AJFoBmWLDX3GfFGZm4vcljeJBkc7rbzRsag1r0QIkVEbdUtUNB6JOspq8d%2FrP2dqvYGPb518CWshYjTWTJymjptnXv6FfT3tosUj1YghQ1wwfAS%2FSDacNA%2BcqK0HpvdLjmi2bETwg83Xqb%2BLJNs9mD6ijgwkxDEIAeCs%2FymwyEv2RRdNRsONpvjx2MPECK0rwitdqCqjk6DpOxaLRYI8oSsMdY0rGV0aVkpYn9W3LQHmsIXTzGvmb%2FTxvgkqeXU0IO8fRYRim6uXyn1bsmE1Bfe%2BI0ruFsfhGHPBuTSEeirC1pubneMuvEG8FPw6G4uIb9VzeaR6HfV2DccLMyYlyR0kXnXosEWwV%2FA9WOxdGWlqf2Lcg02PyJ2oPiOC7G6%2Fpu%2FN4DPz%2B1wxWerVW63mwORMJWym70GOqUB0V1a7oaDoDEoZ6MYLx9vXeHXcRuWi8W2jfscvF4XEkVF5q8Qnm%2FJXQgulO7Uvd5z%2FrXQtlaygwncZVH4W9WLEGTO0CfTrU%2FADw259XHPjOzbptSMy18L8mkNBWpXEJRNJOSrIpp1M6ktcDayxAwooeLHi%2BUIgAeHSWq3xeqmlkrAzqbp%2B%2BjXyTqZ1P6tYB7BNhSvxZgxaxH5aT%2Bt6WnW%2ByEbBZZC&X-Amz-Signature=dbd1286c69ad6f7c3e358725c3b6544284f85693e3107c8d13be9f02cd045d2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZSATWIN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIEk06MDYzQBVHNMzQ6g0pTFhTEzo7N2qkkXhdMzX6S9mAiEAlJOIEiF2lAMi0lG8o0SumqF2JVWGLup7njDlQeebtHkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMRzQLHj9oHTgLixCyrcA2PdgaLqilK9aELfdya9ifF%2Ft%2Bbc4KXwIMlBXi%2BMma3KSv%2BAY%2F%2ByhgYnbeId25qHdMJZSjKQdOS4TGD9b7K7u3fOYJoiJQOoIQWQ9KeIFogHYmXWNCI819mzoe8cJWQUU488KZscc%2BAKPXgS755KUslIWiu%2FQHoyCm%2FqBVTfL9GxiXe%2FuAIN4gAA2riSjbUEYxvI3v%2BQO7YkUc8Mh2UB5mIgJrZki3r6yWzEG6h%2F7xtcJdx7tUxzd8%2B1V%2Fe969G7PlLYSoSf3U3WBH7TFmNSmIiPvxnUJq7eIY165%2FjvPkuJaxIEFTxJX3Y5GCcmFke%2FXV34Rdzhy3noxVmCZb8su1w%2F%2FOtdl6DO4s6RvgSzreM723S4P4LaT1%2Fa4fdtIf%2FNfqSJFJ%2BQo4cpYmQ4GWcUt6pd%2FDcR3oAkOhDQSO4TatYwqmMeDqxg5g8s7EBS9UxfwWe97t08I2ZUIrkZH8ksTgm3nGtkIHxeOZGWtiJbFC7nRTA0lNg3KTRw5JefUpPXoPcSB%2BSoLLNsAs17HeSmiRvvfupoMFsn0W36tF%2B1eYdHsCb95T%2FebOrqiL4lCRxeshb1LJAngvHm1RjChFIQ7iJ2ZcNeOxyip77gk%2F8w%2FixTqVfLV4lhBxox2jqTMJyym70GOqUBtklQviYOkobp15J33ULyziO2KN8Oz75rn%2BEocA3vA1MFE4bpyrM8I2ZcgNdiGa0%2Fan2ANvdq8ZpZQ1B21spK6bEE3TQl5o%2Fp%2BNHVeC6MmdTpj7hge2SuMgvD9%2FhA%2BqEy6OG5MayRVOWgb8yyMtemf36XZXln%2F3pzOMczln%2F39uffQ3zdP%2FFpKh6HdXEvV0k%2FmGBTBAjayh%2BpXOHk86qMPE%2Bit0Xx&X-Amz-Signature=b3b2894306eec2a51f201b9b769f3eccfb500cfb53881a00b47d16b3095e20aa&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZSATWIN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIEk06MDYzQBVHNMzQ6g0pTFhTEzo7N2qkkXhdMzX6S9mAiEAlJOIEiF2lAMi0lG8o0SumqF2JVWGLup7njDlQeebtHkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMRzQLHj9oHTgLixCyrcA2PdgaLqilK9aELfdya9ifF%2Ft%2Bbc4KXwIMlBXi%2BMma3KSv%2BAY%2F%2ByhgYnbeId25qHdMJZSjKQdOS4TGD9b7K7u3fOYJoiJQOoIQWQ9KeIFogHYmXWNCI819mzoe8cJWQUU488KZscc%2BAKPXgS755KUslIWiu%2FQHoyCm%2FqBVTfL9GxiXe%2FuAIN4gAA2riSjbUEYxvI3v%2BQO7YkUc8Mh2UB5mIgJrZki3r6yWzEG6h%2F7xtcJdx7tUxzd8%2B1V%2Fe969G7PlLYSoSf3U3WBH7TFmNSmIiPvxnUJq7eIY165%2FjvPkuJaxIEFTxJX3Y5GCcmFke%2FXV34Rdzhy3noxVmCZb8su1w%2F%2FOtdl6DO4s6RvgSzreM723S4P4LaT1%2Fa4fdtIf%2FNfqSJFJ%2BQo4cpYmQ4GWcUt6pd%2FDcR3oAkOhDQSO4TatYwqmMeDqxg5g8s7EBS9UxfwWe97t08I2ZUIrkZH8ksTgm3nGtkIHxeOZGWtiJbFC7nRTA0lNg3KTRw5JefUpPXoPcSB%2BSoLLNsAs17HeSmiRvvfupoMFsn0W36tF%2B1eYdHsCb95T%2FebOrqiL4lCRxeshb1LJAngvHm1RjChFIQ7iJ2ZcNeOxyip77gk%2F8w%2FixTqVfLV4lhBxox2jqTMJyym70GOqUBtklQviYOkobp15J33ULyziO2KN8Oz75rn%2BEocA3vA1MFE4bpyrM8I2ZcgNdiGa0%2Fan2ANvdq8ZpZQ1B21spK6bEE3TQl5o%2Fp%2BNHVeC6MmdTpj7hge2SuMgvD9%2FhA%2BqEy6OG5MayRVOWgb8yyMtemf36XZXln%2F3pzOMczln%2F39uffQ3zdP%2FFpKh6HdXEvV0k%2FmGBTBAjayh%2BpXOHk86qMPE%2Bit0Xx&X-Amz-Signature=ab4b11351d48e20d1f1afeff512f3681f5af38a2de470b5fb8e93e3ce6232a5f&X-Amz-SignedHeaders=host&x-id=GetObject)

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
