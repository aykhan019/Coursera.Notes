

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAON3ATO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEq4geRQ7BoSt7EYp2bztM0TcjHj2k8fHjv6Ik9ImWLmAiBKjoG%2BwdjY1HK4kD4vTUtfPIXYwMKGKlfeG6Pn3BM0DyqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7ZZbNzxSvuZg834dKtwDii6PYIzf0d%2B%2FE6o09xClcMjg3DIkV1UHuHHFHb2uJC70FRHmiaQcZ3oejc6Ul9ijMjxFtVfD6I3wUTqQJDGldULoL6Y3IT7hdRRIxAbNprX4JrtixNkQ99trEJYGV8IRK1h8bBBtxngGW5Q6ZOEIVkNEF%2FpMdJXL3QD9aiKwzPCsRRpSbVfhcAK2OTJTl9X69FtlchcsKotrHbAM%2FXziJEEqr0Nxb5jSysUaPm0adRuUA0gaFUrM0NQqT2JcfkDKW%2FlWLV%2FvHvdmYxJsSsy2%2FymRLp%2FCpdk7mE3v9shBlYZduOAmEbQNW%2BTf1%2BvctcgED3AG7z5fHA0qhLM0%2Bsgx12KbUjz1RhDrnI1Ikgg9nMneGe3YppL%2BrbxmZbt4ocBdscB3jFF4uPE%2FvVquLpcBdIxOdmC6aPz9jCwPuMt8D7it8IbH82dAf2EeZU5lDMtc8pkwF0f%2BDX%2FNpX8XMmo80x%2BgtWqSoURAPoZHCedjdFK%2BIy%2BGY8eKTIGWsUwEIV2n78DEtGNEGgAwdrEV1jVNVERqSfPkSW2VRdTf10gIWqYtpTRPPdIHWa3MHE12eW42DztdIljj5XwVsc%2Brh%2FW7CFuDq4LFWgu8RAipqO8wuJR29iAxrYhi%2FKZwOtIwwN7tvAY6pgFCWfleqNuhwv83NHm5O%2FBThX2ODj1bFvX6os0975pDR4TDua0%2B1qDBObX0RTwoA4Mzjq97sXp30XVunfEkmNkCD9bmNEXjrFxY02m1NWqJGAnAXXY5TxPM4tHAaqgylqFv%2F8xvWn8eIBK2F26sakAKB8ZwcB%2BJdr%2FJdpvkeogRlmG0SOgA1IvnpbC4u1IxnlfS05gbofUj1NJ1ROkjsDAZkOHm6NRG&X-Amz-Signature=a05b411397bb528c575e9f48512f58b2a84937280ad5e359293fe97e0011f817&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAON3ATO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEq4geRQ7BoSt7EYp2bztM0TcjHj2k8fHjv6Ik9ImWLmAiBKjoG%2BwdjY1HK4kD4vTUtfPIXYwMKGKlfeG6Pn3BM0DyqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7ZZbNzxSvuZg834dKtwDii6PYIzf0d%2B%2FE6o09xClcMjg3DIkV1UHuHHFHb2uJC70FRHmiaQcZ3oejc6Ul9ijMjxFtVfD6I3wUTqQJDGldULoL6Y3IT7hdRRIxAbNprX4JrtixNkQ99trEJYGV8IRK1h8bBBtxngGW5Q6ZOEIVkNEF%2FpMdJXL3QD9aiKwzPCsRRpSbVfhcAK2OTJTl9X69FtlchcsKotrHbAM%2FXziJEEqr0Nxb5jSysUaPm0adRuUA0gaFUrM0NQqT2JcfkDKW%2FlWLV%2FvHvdmYxJsSsy2%2FymRLp%2FCpdk7mE3v9shBlYZduOAmEbQNW%2BTf1%2BvctcgED3AG7z5fHA0qhLM0%2Bsgx12KbUjz1RhDrnI1Ikgg9nMneGe3YppL%2BrbxmZbt4ocBdscB3jFF4uPE%2FvVquLpcBdIxOdmC6aPz9jCwPuMt8D7it8IbH82dAf2EeZU5lDMtc8pkwF0f%2BDX%2FNpX8XMmo80x%2BgtWqSoURAPoZHCedjdFK%2BIy%2BGY8eKTIGWsUwEIV2n78DEtGNEGgAwdrEV1jVNVERqSfPkSW2VRdTf10gIWqYtpTRPPdIHWa3MHE12eW42DztdIljj5XwVsc%2Brh%2FW7CFuDq4LFWgu8RAipqO8wuJR29iAxrYhi%2FKZwOtIwwN7tvAY6pgFCWfleqNuhwv83NHm5O%2FBThX2ODj1bFvX6os0975pDR4TDua0%2B1qDBObX0RTwoA4Mzjq97sXp30XVunfEkmNkCD9bmNEXjrFxY02m1NWqJGAnAXXY5TxPM4tHAaqgylqFv%2F8xvWn8eIBK2F26sakAKB8ZwcB%2BJdr%2FJdpvkeogRlmG0SOgA1IvnpbC4u1IxnlfS05gbofUj1NJ1ROkjsDAZkOHm6NRG&X-Amz-Signature=004a45c95d0418db4311daf08048a94377d83284b72fb443aeb85a2bc7739eca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAON3ATO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEq4geRQ7BoSt7EYp2bztM0TcjHj2k8fHjv6Ik9ImWLmAiBKjoG%2BwdjY1HK4kD4vTUtfPIXYwMKGKlfeG6Pn3BM0DyqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7ZZbNzxSvuZg834dKtwDii6PYIzf0d%2B%2FE6o09xClcMjg3DIkV1UHuHHFHb2uJC70FRHmiaQcZ3oejc6Ul9ijMjxFtVfD6I3wUTqQJDGldULoL6Y3IT7hdRRIxAbNprX4JrtixNkQ99trEJYGV8IRK1h8bBBtxngGW5Q6ZOEIVkNEF%2FpMdJXL3QD9aiKwzPCsRRpSbVfhcAK2OTJTl9X69FtlchcsKotrHbAM%2FXziJEEqr0Nxb5jSysUaPm0adRuUA0gaFUrM0NQqT2JcfkDKW%2FlWLV%2FvHvdmYxJsSsy2%2FymRLp%2FCpdk7mE3v9shBlYZduOAmEbQNW%2BTf1%2BvctcgED3AG7z5fHA0qhLM0%2Bsgx12KbUjz1RhDrnI1Ikgg9nMneGe3YppL%2BrbxmZbt4ocBdscB3jFF4uPE%2FvVquLpcBdIxOdmC6aPz9jCwPuMt8D7it8IbH82dAf2EeZU5lDMtc8pkwF0f%2BDX%2FNpX8XMmo80x%2BgtWqSoURAPoZHCedjdFK%2BIy%2BGY8eKTIGWsUwEIV2n78DEtGNEGgAwdrEV1jVNVERqSfPkSW2VRdTf10gIWqYtpTRPPdIHWa3MHE12eW42DztdIljj5XwVsc%2Brh%2FW7CFuDq4LFWgu8RAipqO8wuJR29iAxrYhi%2FKZwOtIwwN7tvAY6pgFCWfleqNuhwv83NHm5O%2FBThX2ODj1bFvX6os0975pDR4TDua0%2B1qDBObX0RTwoA4Mzjq97sXp30XVunfEkmNkCD9bmNEXjrFxY02m1NWqJGAnAXXY5TxPM4tHAaqgylqFv%2F8xvWn8eIBK2F26sakAKB8ZwcB%2BJdr%2FJdpvkeogRlmG0SOgA1IvnpbC4u1IxnlfS05gbofUj1NJ1ROkjsDAZkOHm6NRG&X-Amz-Signature=327c4085fcd8f9a146a44146f1380c27027bc1fbc0c6c92652f9cb04258fee81&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W64NTNJW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaHvBzSTCQMQ4J07bOVEWUJZnihJe651P4uoae%2FybSqAiA5opOUSszLM526fMbrHpKoznWF4XYod6Nx6QMLmfdX1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FW1skD96yZdNUlKKtwDBYZIxk%2F%2BbcFCb1qPmpAo8CHDwQhTIuTeB4Xtl1SgIymJlcBfgurREA4PCg5ae0%2BAIjPiZwPziS2oBc1pliTHccTtRE2vke2bjiUTLcBxbiDbglie6YGn5RLdmxIlXmlxuo7a3wCBmVWA%2Fpg7tucuW%2BgQZbqxJXUMa6AkWUmo8%2FWl6Dj3LLKaOr63LIerLcuyrqfX9NiYOYVoQGl4poDfDMPoQ6rYgR43pj3WqaRJrCKe%2FB1r0nvIutWtj8EqSMriDgqtFt2LgotJ1tYJyE4NGSLL3A9grYsBiaHrm11d%2BHWqmfdIIvkv9K98jcFYkjpFAvgUhDV7flcsZ7E4TSOBJset%2FgSmvH10I4ijXXsY8EiV%2F0TAOiRnnW6sQ9sVzgLk2R8ml%2BsR084K0wBIVIO%2FsIN3m4TMElgss0ngdfHeam8cmSJGhaMLNz0KOw%2BUMyX%2BXbFB6tg7Vizzsw8IHA5qkXyu0atBZYrv1O6UPyc%2F8bqohbZYJlPW0CxTDh2OtR2pEKxoXd%2FXUlqrVZVl8bJwGe49bUrgamP6XYgBwaQVIYk2dQbRJW72BOWt1CWY68wP30QxMtaaewjxWijM9uRBO8pDnxNX3DiBvwZinltjn10eurR%2BUZrgT%2Fx2d7Uw1t7tvAY6pgGCG3D%2Folzf0R%2FMpNQoBlTc3QAMLKg%2BOktYUo6m2%2FyConhvDlGepAeQxOVv4SJ6CYbKf3n7IMeWw8%2F8knJC7dovZmP3mMzPGxIzWuVYCWMlyBfK7mZ19ebh9zauaFzcN0rWmeMmW%2FHPycIW28yof01p%2F9L6JlCxGzNMjtsI8yusTjD7BN9ICu7KQyZoowxnVHDjcWtJTwqWfToRDKmIOiGXt44r1Rfo&X-Amz-Signature=692cae4aa270af5ca5d3a2e5e910d46c53af4f92f642671f9ee8f9da778885e6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W64NTNJW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaHvBzSTCQMQ4J07bOVEWUJZnihJe651P4uoae%2FybSqAiA5opOUSszLM526fMbrHpKoznWF4XYod6Nx6QMLmfdX1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FW1skD96yZdNUlKKtwDBYZIxk%2F%2BbcFCb1qPmpAo8CHDwQhTIuTeB4Xtl1SgIymJlcBfgurREA4PCg5ae0%2BAIjPiZwPziS2oBc1pliTHccTtRE2vke2bjiUTLcBxbiDbglie6YGn5RLdmxIlXmlxuo7a3wCBmVWA%2Fpg7tucuW%2BgQZbqxJXUMa6AkWUmo8%2FWl6Dj3LLKaOr63LIerLcuyrqfX9NiYOYVoQGl4poDfDMPoQ6rYgR43pj3WqaRJrCKe%2FB1r0nvIutWtj8EqSMriDgqtFt2LgotJ1tYJyE4NGSLL3A9grYsBiaHrm11d%2BHWqmfdIIvkv9K98jcFYkjpFAvgUhDV7flcsZ7E4TSOBJset%2FgSmvH10I4ijXXsY8EiV%2F0TAOiRnnW6sQ9sVzgLk2R8ml%2BsR084K0wBIVIO%2FsIN3m4TMElgss0ngdfHeam8cmSJGhaMLNz0KOw%2BUMyX%2BXbFB6tg7Vizzsw8IHA5qkXyu0atBZYrv1O6UPyc%2F8bqohbZYJlPW0CxTDh2OtR2pEKxoXd%2FXUlqrVZVl8bJwGe49bUrgamP6XYgBwaQVIYk2dQbRJW72BOWt1CWY68wP30QxMtaaewjxWijM9uRBO8pDnxNX3DiBvwZinltjn10eurR%2BUZrgT%2Fx2d7Uw1t7tvAY6pgGCG3D%2Folzf0R%2FMpNQoBlTc3QAMLKg%2BOktYUo6m2%2FyConhvDlGepAeQxOVv4SJ6CYbKf3n7IMeWw8%2F8knJC7dovZmP3mMzPGxIzWuVYCWMlyBfK7mZ19ebh9zauaFzcN0rWmeMmW%2FHPycIW28yof01p%2F9L6JlCxGzNMjtsI8yusTjD7BN9ICu7KQyZoowxnVHDjcWtJTwqWfToRDKmIOiGXt44r1Rfo&X-Amz-Signature=0d03d05ccdb78363fceb7b79a0a2f0563bd230e2edd84d25f264c82be6d5d6ec&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W64NTNJW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaHvBzSTCQMQ4J07bOVEWUJZnihJe651P4uoae%2FybSqAiA5opOUSszLM526fMbrHpKoznWF4XYod6Nx6QMLmfdX1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FW1skD96yZdNUlKKtwDBYZIxk%2F%2BbcFCb1qPmpAo8CHDwQhTIuTeB4Xtl1SgIymJlcBfgurREA4PCg5ae0%2BAIjPiZwPziS2oBc1pliTHccTtRE2vke2bjiUTLcBxbiDbglie6YGn5RLdmxIlXmlxuo7a3wCBmVWA%2Fpg7tucuW%2BgQZbqxJXUMa6AkWUmo8%2FWl6Dj3LLKaOr63LIerLcuyrqfX9NiYOYVoQGl4poDfDMPoQ6rYgR43pj3WqaRJrCKe%2FB1r0nvIutWtj8EqSMriDgqtFt2LgotJ1tYJyE4NGSLL3A9grYsBiaHrm11d%2BHWqmfdIIvkv9K98jcFYkjpFAvgUhDV7flcsZ7E4TSOBJset%2FgSmvH10I4ijXXsY8EiV%2F0TAOiRnnW6sQ9sVzgLk2R8ml%2BsR084K0wBIVIO%2FsIN3m4TMElgss0ngdfHeam8cmSJGhaMLNz0KOw%2BUMyX%2BXbFB6tg7Vizzsw8IHA5qkXyu0atBZYrv1O6UPyc%2F8bqohbZYJlPW0CxTDh2OtR2pEKxoXd%2FXUlqrVZVl8bJwGe49bUrgamP6XYgBwaQVIYk2dQbRJW72BOWt1CWY68wP30QxMtaaewjxWijM9uRBO8pDnxNX3DiBvwZinltjn10eurR%2BUZrgT%2Fx2d7Uw1t7tvAY6pgGCG3D%2Folzf0R%2FMpNQoBlTc3QAMLKg%2BOktYUo6m2%2FyConhvDlGepAeQxOVv4SJ6CYbKf3n7IMeWw8%2F8knJC7dovZmP3mMzPGxIzWuVYCWMlyBfK7mZ19ebh9zauaFzcN0rWmeMmW%2FHPycIW28yof01p%2F9L6JlCxGzNMjtsI8yusTjD7BN9ICu7KQyZoowxnVHDjcWtJTwqWfToRDKmIOiGXt44r1Rfo&X-Amz-Signature=953dd66e2b9205687db3573694b26390a436caf921f40213f5f09e4dbe3659ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W64NTNJW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaHvBzSTCQMQ4J07bOVEWUJZnihJe651P4uoae%2FybSqAiA5opOUSszLM526fMbrHpKoznWF4XYod6Nx6QMLmfdX1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FW1skD96yZdNUlKKtwDBYZIxk%2F%2BbcFCb1qPmpAo8CHDwQhTIuTeB4Xtl1SgIymJlcBfgurREA4PCg5ae0%2BAIjPiZwPziS2oBc1pliTHccTtRE2vke2bjiUTLcBxbiDbglie6YGn5RLdmxIlXmlxuo7a3wCBmVWA%2Fpg7tucuW%2BgQZbqxJXUMa6AkWUmo8%2FWl6Dj3LLKaOr63LIerLcuyrqfX9NiYOYVoQGl4poDfDMPoQ6rYgR43pj3WqaRJrCKe%2FB1r0nvIutWtj8EqSMriDgqtFt2LgotJ1tYJyE4NGSLL3A9grYsBiaHrm11d%2BHWqmfdIIvkv9K98jcFYkjpFAvgUhDV7flcsZ7E4TSOBJset%2FgSmvH10I4ijXXsY8EiV%2F0TAOiRnnW6sQ9sVzgLk2R8ml%2BsR084K0wBIVIO%2FsIN3m4TMElgss0ngdfHeam8cmSJGhaMLNz0KOw%2BUMyX%2BXbFB6tg7Vizzsw8IHA5qkXyu0atBZYrv1O6UPyc%2F8bqohbZYJlPW0CxTDh2OtR2pEKxoXd%2FXUlqrVZVl8bJwGe49bUrgamP6XYgBwaQVIYk2dQbRJW72BOWt1CWY68wP30QxMtaaewjxWijM9uRBO8pDnxNX3DiBvwZinltjn10eurR%2BUZrgT%2Fx2d7Uw1t7tvAY6pgGCG3D%2Folzf0R%2FMpNQoBlTc3QAMLKg%2BOktYUo6m2%2FyConhvDlGepAeQxOVv4SJ6CYbKf3n7IMeWw8%2F8knJC7dovZmP3mMzPGxIzWuVYCWMlyBfK7mZ19ebh9zauaFzcN0rWmeMmW%2FHPycIW28yof01p%2F9L6JlCxGzNMjtsI8yusTjD7BN9ICu7KQyZoowxnVHDjcWtJTwqWfToRDKmIOiGXt44r1Rfo&X-Amz-Signature=bee928d0b6ba9a348c36f47cd8198c659cfc21f43554af6cb767e12d198268a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W64NTNJW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaHvBzSTCQMQ4J07bOVEWUJZnihJe651P4uoae%2FybSqAiA5opOUSszLM526fMbrHpKoznWF4XYod6Nx6QMLmfdX1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FW1skD96yZdNUlKKtwDBYZIxk%2F%2BbcFCb1qPmpAo8CHDwQhTIuTeB4Xtl1SgIymJlcBfgurREA4PCg5ae0%2BAIjPiZwPziS2oBc1pliTHccTtRE2vke2bjiUTLcBxbiDbglie6YGn5RLdmxIlXmlxuo7a3wCBmVWA%2Fpg7tucuW%2BgQZbqxJXUMa6AkWUmo8%2FWl6Dj3LLKaOr63LIerLcuyrqfX9NiYOYVoQGl4poDfDMPoQ6rYgR43pj3WqaRJrCKe%2FB1r0nvIutWtj8EqSMriDgqtFt2LgotJ1tYJyE4NGSLL3A9grYsBiaHrm11d%2BHWqmfdIIvkv9K98jcFYkjpFAvgUhDV7flcsZ7E4TSOBJset%2FgSmvH10I4ijXXsY8EiV%2F0TAOiRnnW6sQ9sVzgLk2R8ml%2BsR084K0wBIVIO%2FsIN3m4TMElgss0ngdfHeam8cmSJGhaMLNz0KOw%2BUMyX%2BXbFB6tg7Vizzsw8IHA5qkXyu0atBZYrv1O6UPyc%2F8bqohbZYJlPW0CxTDh2OtR2pEKxoXd%2FXUlqrVZVl8bJwGe49bUrgamP6XYgBwaQVIYk2dQbRJW72BOWt1CWY68wP30QxMtaaewjxWijM9uRBO8pDnxNX3DiBvwZinltjn10eurR%2BUZrgT%2Fx2d7Uw1t7tvAY6pgGCG3D%2Folzf0R%2FMpNQoBlTc3QAMLKg%2BOktYUo6m2%2FyConhvDlGepAeQxOVv4SJ6CYbKf3n7IMeWw8%2F8knJC7dovZmP3mMzPGxIzWuVYCWMlyBfK7mZ19ebh9zauaFzcN0rWmeMmW%2FHPycIW28yof01p%2F9L6JlCxGzNMjtsI8yusTjD7BN9ICu7KQyZoowxnVHDjcWtJTwqWfToRDKmIOiGXt44r1Rfo&X-Amz-Signature=f2f3b8a0a3fd0da02985ff76130c4d0a7c950d71f357f872d265ced9a116dfb6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W64NTNJW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaHvBzSTCQMQ4J07bOVEWUJZnihJe651P4uoae%2FybSqAiA5opOUSszLM526fMbrHpKoznWF4XYod6Nx6QMLmfdX1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FW1skD96yZdNUlKKtwDBYZIxk%2F%2BbcFCb1qPmpAo8CHDwQhTIuTeB4Xtl1SgIymJlcBfgurREA4PCg5ae0%2BAIjPiZwPziS2oBc1pliTHccTtRE2vke2bjiUTLcBxbiDbglie6YGn5RLdmxIlXmlxuo7a3wCBmVWA%2Fpg7tucuW%2BgQZbqxJXUMa6AkWUmo8%2FWl6Dj3LLKaOr63LIerLcuyrqfX9NiYOYVoQGl4poDfDMPoQ6rYgR43pj3WqaRJrCKe%2FB1r0nvIutWtj8EqSMriDgqtFt2LgotJ1tYJyE4NGSLL3A9grYsBiaHrm11d%2BHWqmfdIIvkv9K98jcFYkjpFAvgUhDV7flcsZ7E4TSOBJset%2FgSmvH10I4ijXXsY8EiV%2F0TAOiRnnW6sQ9sVzgLk2R8ml%2BsR084K0wBIVIO%2FsIN3m4TMElgss0ngdfHeam8cmSJGhaMLNz0KOw%2BUMyX%2BXbFB6tg7Vizzsw8IHA5qkXyu0atBZYrv1O6UPyc%2F8bqohbZYJlPW0CxTDh2OtR2pEKxoXd%2FXUlqrVZVl8bJwGe49bUrgamP6XYgBwaQVIYk2dQbRJW72BOWt1CWY68wP30QxMtaaewjxWijM9uRBO8pDnxNX3DiBvwZinltjn10eurR%2BUZrgT%2Fx2d7Uw1t7tvAY6pgGCG3D%2Folzf0R%2FMpNQoBlTc3QAMLKg%2BOktYUo6m2%2FyConhvDlGepAeQxOVv4SJ6CYbKf3n7IMeWw8%2F8knJC7dovZmP3mMzPGxIzWuVYCWMlyBfK7mZ19ebh9zauaFzcN0rWmeMmW%2FHPycIW28yof01p%2F9L6JlCxGzNMjtsI8yusTjD7BN9ICu7KQyZoowxnVHDjcWtJTwqWfToRDKmIOiGXt44r1Rfo&X-Amz-Signature=340d703244d09be9ec4b5aec793306fcf05aea97e5e834476f64c5745a117fa6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6QRI3JH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCveEvVSPduTRYxMFCSuUsQrW2JiDaLUn2rp57kWionvwIhAK6fwYiZwpT1ARj%2ByaJsmq90BsWdEjdxgBB8n1MCxniMKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgykoAT%2FNAEQUN5oYeYq3AOYGh4ZzHGZkhShVe%2FrauDlKwQW9b8KBO1Q304SY0wbYWY3X69%2BpR%2BEJ8VFSknq4QMEF6VsdxUMDHgzBRQ26A59ZRuuvrfwRV32cLxKXQhs5N4MREFhUw8XGNJsyimsGtjUeFbO5bNkmVnq7ngnKJ4Nfi2utTSPCnXF%2Bm3RWs4CUJudo4o5R4AC26uvWZDwGmFBUp%2BU4NzVKo9%2FH3aZbDUh5cJF%2F6J31LYENux9YujqnV2idz%2FwBaafFEKE%2F4aZ1U9Luy%2Ff80xsgS%2FGW3Td5QZf%2F2uLUZ01RQtxVhzI%2BmDiUrozXGQQx4l8q6pgXur1%2Bg19eUYehFrXitJxEV88av%2BMgqoBo0Xa9Avq0fWEsbUesLwMxy2kQSZpiWnMDEGXPP%2BL5iFce1GK5qsBkhhiNnK0tlX%2FpPJ4t%2BSkFypl%2BOKKHV1q8n8kuJZ7mO07OFBf137W20UvBc5zItbM%2Ba3Hc6V6Bft3PAiMvKSqjQIik7GzQsEL8DhKTYeR7WMXWRducMrE%2F7H632jr45GwZn%2Fo38lkupMy1hg359gteyVq%2BwphfF0W2nXYblXsH%2B1HRvlwjYnyenZc4tr9cuoRUCjuJ5M4yocOr7%2FzLQwTLnaNasNMW2cm%2FsV2%2FpoptKptujC43u28BjqkAVBeio7WoyeK%2BfC%2BLSrZt7u8WoPLzvU%2FjvAV%2FvlVDXEvSKfwFK%2BFeZbERo9fwruhY0OkhP22pMzpalTmVRAfzbrui5%2FtB3xHkgHDjzEeSiLxc%2BVeTQKZ1v1Br%2F9YkzO2UP8L3OW0wP5EZ8MXfq%2FraIBlHeUtz5RlPjQALmwCg%2F1jNBCMJkHkkXi5VlibUtuq9%2B%2F2%2BTxR%2FBp1piPW69gqZYoi7woY&X-Amz-Signature=30d095a7aedb4b7bd80f9e96ab8bc395c1ca6ca4383bf64b4cbbe829c1fb39ea&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6RN3RXP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnwz05AwSX6nzM5D%2BtuBJX0FvfE%2B2VzZwgVxKtKtoTkwIgAIMlzQxypRo2oHev3avCc8xPeO%2FxfFftkULqKpJIiY0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCd6bATJ5ewiJOxFZSrcA2qNiP%2BwtAVuuD2F%2B9sD9ja2u94hs8BmgRLIpb9bEiKPj7mQebZFKp2DXBeIpTCfzDR%2BxP5shjR97pD7Di9pia7moeSam%2BnWsRNDwnnpnkg7n1ZQhRcBCUREWr%2BZqc13GwVPEtkEMqqvM6EFZPg8cqzKSRoCTdTAPoCcpApwTu85a27dQPzo0pw7bXzgagaQLbb3rUKXrRsnIS2fbxNUsJuXXB5M6%2FvmdQMo%2FQoef3Gb5cQrQ7LM7OY%2FbAZfYDrJwTlDD4Yfm1lxjuAD%2FBG0esKIRLA5yrHIEY02%2B%2BhGXrktpw%2FFSR4KjndQ0DQpG%2FfUuiRt7Ra9%2BdEvvoXpbc5IIK2qOaOAigAD69NnkqWu64yGO%2FqVuCnTxenzC7NIR7iRua%2BSucneLX%2Bfpn1YUhgSg5HhgjN8z5Ux99G5fMC6bBP9qUkxZoYBlkqVRVJMY05ujuPxkWBEB23YSf3FwvxuyDhHPSSRJb5RGuKAuwfl3vn1xBC5t3f3uGfhbc7i94KbS6HDi41OLOI6bK4R%2B98lpYh6gFE3No0aTGCAwPr2t53AbZFtF33GHO418FzITY%2BW%2BDwToRRSRYnAuLg0vk2EugdJvUXeVYCMWQSzvmYltOhky%2F4ws8YvMo6EgLeUMJjf7bwGOqUBtDHsg9KmfrREd%2B2ILUrxJF1ldAcnP%2F2Uw2iT0%2BNqB90%2FIbYgsQLVFQbB6UYXIOwOAQRV0xf7rRm6CJlsP76VcglmcPqP8tP0NWf7kTXymojgstUyZWgUIIutjJ1UqP1rIlxvA%2Fen8Nyzf%2BdlrnPc0hr8ZaVZJ0TQVH48Pz%2BhF8%2Fxr5qxC8RwILDGWygIG2AH%2FvTglAZmCM0vzgFFwdGKZQcbk2SL&X-Amz-Signature=9ac5b5e08c3c52fad8e32f8314b87dcb44a10fc70d48af5423979130273abcfa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W64NTNJW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaHvBzSTCQMQ4J07bOVEWUJZnihJe651P4uoae%2FybSqAiA5opOUSszLM526fMbrHpKoznWF4XYod6Nx6QMLmfdX1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FW1skD96yZdNUlKKtwDBYZIxk%2F%2BbcFCb1qPmpAo8CHDwQhTIuTeB4Xtl1SgIymJlcBfgurREA4PCg5ae0%2BAIjPiZwPziS2oBc1pliTHccTtRE2vke2bjiUTLcBxbiDbglie6YGn5RLdmxIlXmlxuo7a3wCBmVWA%2Fpg7tucuW%2BgQZbqxJXUMa6AkWUmo8%2FWl6Dj3LLKaOr63LIerLcuyrqfX9NiYOYVoQGl4poDfDMPoQ6rYgR43pj3WqaRJrCKe%2FB1r0nvIutWtj8EqSMriDgqtFt2LgotJ1tYJyE4NGSLL3A9grYsBiaHrm11d%2BHWqmfdIIvkv9K98jcFYkjpFAvgUhDV7flcsZ7E4TSOBJset%2FgSmvH10I4ijXXsY8EiV%2F0TAOiRnnW6sQ9sVzgLk2R8ml%2BsR084K0wBIVIO%2FsIN3m4TMElgss0ngdfHeam8cmSJGhaMLNz0KOw%2BUMyX%2BXbFB6tg7Vizzsw8IHA5qkXyu0atBZYrv1O6UPyc%2F8bqohbZYJlPW0CxTDh2OtR2pEKxoXd%2FXUlqrVZVl8bJwGe49bUrgamP6XYgBwaQVIYk2dQbRJW72BOWt1CWY68wP30QxMtaaewjxWijM9uRBO8pDnxNX3DiBvwZinltjn10eurR%2BUZrgT%2Fx2d7Uw1t7tvAY6pgGCG3D%2Folzf0R%2FMpNQoBlTc3QAMLKg%2BOktYUo6m2%2FyConhvDlGepAeQxOVv4SJ6CYbKf3n7IMeWw8%2F8knJC7dovZmP3mMzPGxIzWuVYCWMlyBfK7mZ19ebh9zauaFzcN0rWmeMmW%2FHPycIW28yof01p%2F9L6JlCxGzNMjtsI8yusTjD7BN9ICu7KQyZoowxnVHDjcWtJTwqWfToRDKmIOiGXt44r1Rfo&X-Amz-Signature=df4cdda417f0f0b62e50fab21f7183898c689c13ddadff932ce6ef19e3c4da90&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W64NTNJW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaHvBzSTCQMQ4J07bOVEWUJZnihJe651P4uoae%2FybSqAiA5opOUSszLM526fMbrHpKoznWF4XYod6Nx6QMLmfdX1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FW1skD96yZdNUlKKtwDBYZIxk%2F%2BbcFCb1qPmpAo8CHDwQhTIuTeB4Xtl1SgIymJlcBfgurREA4PCg5ae0%2BAIjPiZwPziS2oBc1pliTHccTtRE2vke2bjiUTLcBxbiDbglie6YGn5RLdmxIlXmlxuo7a3wCBmVWA%2Fpg7tucuW%2BgQZbqxJXUMa6AkWUmo8%2FWl6Dj3LLKaOr63LIerLcuyrqfX9NiYOYVoQGl4poDfDMPoQ6rYgR43pj3WqaRJrCKe%2FB1r0nvIutWtj8EqSMriDgqtFt2LgotJ1tYJyE4NGSLL3A9grYsBiaHrm11d%2BHWqmfdIIvkv9K98jcFYkjpFAvgUhDV7flcsZ7E4TSOBJset%2FgSmvH10I4ijXXsY8EiV%2F0TAOiRnnW6sQ9sVzgLk2R8ml%2BsR084K0wBIVIO%2FsIN3m4TMElgss0ngdfHeam8cmSJGhaMLNz0KOw%2BUMyX%2BXbFB6tg7Vizzsw8IHA5qkXyu0atBZYrv1O6UPyc%2F8bqohbZYJlPW0CxTDh2OtR2pEKxoXd%2FXUlqrVZVl8bJwGe49bUrgamP6XYgBwaQVIYk2dQbRJW72BOWt1CWY68wP30QxMtaaewjxWijM9uRBO8pDnxNX3DiBvwZinltjn10eurR%2BUZrgT%2Fx2d7Uw1t7tvAY6pgGCG3D%2Folzf0R%2FMpNQoBlTc3QAMLKg%2BOktYUo6m2%2FyConhvDlGepAeQxOVv4SJ6CYbKf3n7IMeWw8%2F8knJC7dovZmP3mMzPGxIzWuVYCWMlyBfK7mZ19ebh9zauaFzcN0rWmeMmW%2FHPycIW28yof01p%2F9L6JlCxGzNMjtsI8yusTjD7BN9ICu7KQyZoowxnVHDjcWtJTwqWfToRDKmIOiGXt44r1Rfo&X-Amz-Signature=af19c53be9d13ce36f8170c0dc88757a5316d54a841b78f1b6597d203b2db113&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W64NTNJW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaHvBzSTCQMQ4J07bOVEWUJZnihJe651P4uoae%2FybSqAiA5opOUSszLM526fMbrHpKoznWF4XYod6Nx6QMLmfdX1SqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FW1skD96yZdNUlKKtwDBYZIxk%2F%2BbcFCb1qPmpAo8CHDwQhTIuTeB4Xtl1SgIymJlcBfgurREA4PCg5ae0%2BAIjPiZwPziS2oBc1pliTHccTtRE2vke2bjiUTLcBxbiDbglie6YGn5RLdmxIlXmlxuo7a3wCBmVWA%2Fpg7tucuW%2BgQZbqxJXUMa6AkWUmo8%2FWl6Dj3LLKaOr63LIerLcuyrqfX9NiYOYVoQGl4poDfDMPoQ6rYgR43pj3WqaRJrCKe%2FB1r0nvIutWtj8EqSMriDgqtFt2LgotJ1tYJyE4NGSLL3A9grYsBiaHrm11d%2BHWqmfdIIvkv9K98jcFYkjpFAvgUhDV7flcsZ7E4TSOBJset%2FgSmvH10I4ijXXsY8EiV%2F0TAOiRnnW6sQ9sVzgLk2R8ml%2BsR084K0wBIVIO%2FsIN3m4TMElgss0ngdfHeam8cmSJGhaMLNz0KOw%2BUMyX%2BXbFB6tg7Vizzsw8IHA5qkXyu0atBZYrv1O6UPyc%2F8bqohbZYJlPW0CxTDh2OtR2pEKxoXd%2FXUlqrVZVl8bJwGe49bUrgamP6XYgBwaQVIYk2dQbRJW72BOWt1CWY68wP30QxMtaaewjxWijM9uRBO8pDnxNX3DiBvwZinltjn10eurR%2BUZrgT%2Fx2d7Uw1t7tvAY6pgGCG3D%2Folzf0R%2FMpNQoBlTc3QAMLKg%2BOktYUo6m2%2FyConhvDlGepAeQxOVv4SJ6CYbKf3n7IMeWw8%2F8knJC7dovZmP3mMzPGxIzWuVYCWMlyBfK7mZ19ebh9zauaFzcN0rWmeMmW%2FHPycIW28yof01p%2F9L6JlCxGzNMjtsI8yusTjD7BN9ICu7KQyZoowxnVHDjcWtJTwqWfToRDKmIOiGXt44r1Rfo&X-Amz-Signature=56a0ef28e6e84649c54d6aa72bfd969c0b1a98e9a81953b2636e92a53e0a3384&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PFKHETS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSixLPTgBqZ9Zd1dFgpPqHCw3X3UQXvBSwZfbFWca5XwIhAKEExUg4LGXHB6gXOSEdy2%2B5dubgbqCXTygaiHLKCGDHKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcjrKuaI22X%2FBUdZoq3AP0i3w8KbEev3zY%2BNEBRIaaZAsh71de9FDb9RPoULN1fH3FreAM8wr76IKwRRkZvXdPit0nl7yvR6YlCuXf5HKRBZajYwNXCtcEgC8AmKdXx1tNg4Pncbwvnp7tRwXjb17CVyxBBGs6VguQGA4%2Bd4%2FigxULYHUpTyXN8HqOXKS2m7CcDjyyCZ6SMxUkghQ%2Fs8nro%2Bp60BxN6IWWT5INUFcxuBFC%2F5bgdGiIqBP7AD1UmxoGl0GUYch8eb7EI8Qu8s6K53dSKVg8%2B%2BWyh4%2Ff%2Bl2I01yTbHXb6yF5B5yP3I5jziCsgWHfnbhndK6ykqSXhwSFrA4BmS%2BfK5A%2Bgo4RJt2xGFF%2FiTdSGJLZ4HYM%2F8zdBU7jbuLhTPGcMfCEnfg52N2TkiQRc5DPkWjMSfTNIBaEqyXzJnun9z2i2dm5nczq2XuXIFoKMEyvJAvB%2FXnwsNmkRZLpfxAbYavyGLU4KkU6m7xV7%2Bi%2BX3UrzZoV4cacURrNva5PdJJFZRiekIKzw2FHiVemdFOW9UJjI2egAaTIHTRcicd0ceu3vscA2bd4GK4q4oq1Nrt7%2B4YI%2FjPsdGg1KiUpRki6RKVPiiOrTIxid3k4jmwn3fkzIzqUnyhdFMHj4PNfS3%2B1rGUHYDCP3%2B28BjqkAZm%2BQDt%2Bcea8XQqXwPJ8f5RjSiUWCdTIZG%2Bp4STFt1EvUOA%2FNh1WPSo6%2Fev3gaCTPgkSkXwFcuVn05K2ovT6JVyp0DBFh8x9NU2hsYO2MXLdbhhNOkkvxaiM7cOfdR6hyuuwFrgteGcfn4eH8r0y4lJ9t0Fy6gefikrtIoo4%2Bu9%2B32Z%2FfjGNnfvLVcoDdnj8oCu2Pl3KqHD%2FB%2F9kjuXaQYfIoPgM&X-Amz-Signature=1f81e48f1ac9191fc2148e6c851d69af8397cc25f98b577376386302d9abb5ed&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5F4CGAT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA608594H3kE8VMPbrJqv6YLEJuHIFY157ih6POA7raCAiEA1ohSov4U1aJzYbfKilF5MaGNkfxMgmrSlXISHr2ekQAqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJEePaoFei2xh0qZvCrcA5ZEK60EcMeEs46hUQ4tXIrgWd37oe1OIQYA%2BL27CdBqSU2mvP%2B5Wzt5SDWAX1DuvWiKOEV%2BFa%2FPnfxk0sQH20fN5xMb9CtfVRip7zi%2FZNyykkJ%2BD7tALj4%2F7vU9iv9r0CEzK6w0y1oTYrs8DaLM2SK1kUbsWe2fGr4rwy4HNsgH7lJMTfEmwCmr6Yb0Y3UFgKcstsni9cZSODyBLLd8reYcIecgI1Ft%2BT4u%2BYfMgTd%2Bc58XE4Ib1rowezeqYi3JCvUUlUd8SSyJpF9DhvhiA10biT%2F5knaos6CfipNNlhHIEFBLshcjT7X08zO9Cb%2FRLe6eQXuSIm9y0dkeDBzy0ykDAXaUDqKRlma78eYkHtzS1Rqt7HKhPEHpuJtH6Y8%2BX1EyRzTU%2Fh5VvuC2BrvqBMgFY6SDEZYZQr9VADUZb9%2B1c8suZ4BIsBP%2FoeEpSFqH2Xv2IePYsesX7AgDk9C8QMuGBH37uxHwxyBB37LEpCDKOnSfGIUl15X8DFNdYMCvihjV%2Ba7aieG3vQLmQJ2RUOZifG%2Fn5ZxDG4ykQeuAxwEBSBFu8YEYN%2BANTaB2Jj8SMcyEypWhuaRPA%2BqjuyNdMI5CHR1FsI0esOrJi6l74PgmpK%2B5mIkcsBEasCzNMNre7bwGOqUB8pF0Im8UvTcujXYf%2FBYWOkxgn4DvkXLPd%2BSN1kImsPD4JRFFBQigErlkekSeNnGeu2kxht3AgzpqcLfqkvBGNtAxxo%2F1zY7EACRZ84nobH0vISbLb1UeKmDdmtvw1eFX3O8Yw616RHbSOL4oBZiB%2BokXkfpynts7MlbtJmX54w9c2uKO8jBv0sNrZvIUSL2cKJGWuCwb7Gb4iKixUHncA%2FlI2OtO&X-Amz-Signature=dc819fde8ac149df3847e0bc4a382a778cb7e1efb15b178d80e223fa8bb597e6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDAJUJ6A%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmwI3%2FcUcPfoygzld%2B49hqBOd9GlG54z3EUTqgoelYWgIhAI4ocixD78yTS18GFYcq%2FuzJqn8RuHs%2BOg0rTyCY6jqPKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvUBEB7AZKyVTfgUUq3AMSRc7uGxo6UL39UmN1ZBBgS5hVsmmvG7sgC7KJqKdsXb69ZEFZx5p08uLQYgbpCxdUc4R1SnIXAvq1g3xiR6xeRws6XPcCz9AxZdnDc1BCis8KFfoNTxCz75vpg4GdQQ8%2BAmtREuZTewZ6JrkJ%2F7KkSMtxpn3Cfv1pfKPGC8iqb7hFwT9%2BIyGriNY5tk0Z80nhMNnWw8KKLs3oy09D6%2BbxE0c4mYDLqjYorGtfZiAAtyIfw9gvDALHwbFD4w%2FfAQJwqjeqADjmRVUu5IvBT4KxPO%2BH1HE3HllVzyaYcbaiFQLPmTPBREiQV0cJkCb6NAINNGtAMs4UYLQOUBGz097xcJM8OC4VPdLjLdn3oXbR9Pw%2FDYf0SgmPIZDip72xQ0zBhNoJwHD1h1Sdvf8XkCuYZkg1TqT2nnWl0uVyThVMCS6QniEiqEqRT%2BIU%2BFHftP%2B5%2BiNwCDLNIV%2FaD0jCQPis%2BaosrxnwxsCB%2FOOtOgVG4kaq7p0RPGfLIsTlQVn5yemoPyQcAWsSyvRIe1clj7BCVAEdR3FPo0kXiFfPPQ6WKWaOpl0TdqzNV6ovShWIGqYre0NBI%2F91H%2B7y9AZ19V%2B5cRS0l6uY2bnMBI57Uw0vIBnvHViiNhmPHYMxLDD03u28BjqkAXmXTeqsHq8VZZ7VBtBhWb8YHxmPTGUB4w8vRRabV0IxQ43aW7F4pGWiB2qtgemt%2BMgfnlCuzJIVUIM3gXKK6SF%2BvfTTtupbqTsyCajqUrC9NYXbvCVJNtA97WHcz%2Bam0eLXfL9bj6OtYmiKo77DQDB2DBAyMCCHNTwIlxsJz5wv4yKQX0iu9XFWqNXUO%2FO9xIXYtLFd7kia6EWeqgLLyhkoJzTb&X-Amz-Signature=13fe8dd2e9d676f453aec6cb8e3840c3dbd99a3def5ae347198ac6d71dafd204&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VW24ZVX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEWhETf4equgSCkB2auUlSK%2Fb9oNH84Pvlibz6SbSIiAiEAhx25XWVrISxFIZvUSr5oW06SQnxno5M6wUAHIsWdS%2FIqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIK%2FZAPEwHTLYwV0TSrcAxo9O1ntOVfneGy8y78mukGX0ahOw6ucBNvXYg3o6FSon%2B22V6mHKqvQ0JLUhsNxwK1xUqmJDq6wMt%2F7SB%2FzqtLaOQTEBm4x8fqP4UQXv5vACRCRpTnRas0M5%2FYiGS5pkxSXsW3kcdfCcyMWfPODA2NUlQRYSVxGUYR5hRKfPE7vloZDHcPUWD5VAboidmAgK82r02arhsfcpt0NQUirFqgn%2BXQ1bm6bOO4MDD3UsuvCgM6qnxd7Mis8n%2Bo6kaWzMtbviiszLBjqyfG1pT7hQfoLCYcxT3hpMxOyH3BhoqqM61fAzKMo1jiUPhM8mojwdQlEJZLz2p9gl7ghfs2KsQWwDKhDqBUXBft8xHjFyGktPROfyavdwaYkFjDYzwYVOxIeBYbbVJCbAqkTmMSgXYgmP0v2pg%2B274t0ohpBFSX%2FEiGkP4qqLkK1jrWRSaslsTmDpkIdvvIzDEDnjxKB5oKYC9WZu6Z0cZdVHP%2FxWJAcSJf05JrUS10uzd1FmZQBASPoA8FRjLZ3tsXob8d3XMjECVBvG9v3vOZDOocOkTHcdM4JquAMdhB0Ubmq20%2F1RS2jpVVad2M0tmnYhllah%2FAMMY4dopyRTnIeLGYL8EKaKfRHqInA4yJjYOq5MPTe7bwGOqUBEPZlAX84OE3tFoUfI7%2F4kOiHPAzYBMHnKGSlF7nf5GQAF308HS54kkox31PoAO08SRaypPQFwdaibwlR9dQXfe3DrBm%2FvoAlUctVrWptEhtxWrTvK8kCLoVjPOUfKeF2lQi9pZuSeyXrMWzZPCRJhg%2BORXB6SSe8GwiXQv%2F%2BEGPVLNnKZR%2FKDjRV%2Fr5%2F15oiLSfjyMbB060XopHxt0f0giyC3iUM&X-Amz-Signature=5b511f9558178cee4bcdc3f8f3ab3be9b1806055b9f7aa697c3e33cd44560207&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VW24ZVX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEWhETf4equgSCkB2auUlSK%2Fb9oNH84Pvlibz6SbSIiAiEAhx25XWVrISxFIZvUSr5oW06SQnxno5M6wUAHIsWdS%2FIqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIK%2FZAPEwHTLYwV0TSrcAxo9O1ntOVfneGy8y78mukGX0ahOw6ucBNvXYg3o6FSon%2B22V6mHKqvQ0JLUhsNxwK1xUqmJDq6wMt%2F7SB%2FzqtLaOQTEBm4x8fqP4UQXv5vACRCRpTnRas0M5%2FYiGS5pkxSXsW3kcdfCcyMWfPODA2NUlQRYSVxGUYR5hRKfPE7vloZDHcPUWD5VAboidmAgK82r02arhsfcpt0NQUirFqgn%2BXQ1bm6bOO4MDD3UsuvCgM6qnxd7Mis8n%2Bo6kaWzMtbviiszLBjqyfG1pT7hQfoLCYcxT3hpMxOyH3BhoqqM61fAzKMo1jiUPhM8mojwdQlEJZLz2p9gl7ghfs2KsQWwDKhDqBUXBft8xHjFyGktPROfyavdwaYkFjDYzwYVOxIeBYbbVJCbAqkTmMSgXYgmP0v2pg%2B274t0ohpBFSX%2FEiGkP4qqLkK1jrWRSaslsTmDpkIdvvIzDEDnjxKB5oKYC9WZu6Z0cZdVHP%2FxWJAcSJf05JrUS10uzd1FmZQBASPoA8FRjLZ3tsXob8d3XMjECVBvG9v3vOZDOocOkTHcdM4JquAMdhB0Ubmq20%2F1RS2jpVVad2M0tmnYhllah%2FAMMY4dopyRTnIeLGYL8EKaKfRHqInA4yJjYOq5MPTe7bwGOqUBEPZlAX84OE3tFoUfI7%2F4kOiHPAzYBMHnKGSlF7nf5GQAF308HS54kkox31PoAO08SRaypPQFwdaibwlR9dQXfe3DrBm%2FvoAlUctVrWptEhtxWrTvK8kCLoVjPOUfKeF2lQi9pZuSeyXrMWzZPCRJhg%2BORXB6SSe8GwiXQv%2F%2BEGPVLNnKZR%2FKDjRV%2Fr5%2F15oiLSfjyMbB060XopHxt0f0giyC3iUM&X-Amz-Signature=f85cb3e185768f812f8b8f1ff8ba36911345fcb2666b4b96541e9ebc09f82936&X-Amz-SignedHeaders=host&x-id=GetObject)

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
