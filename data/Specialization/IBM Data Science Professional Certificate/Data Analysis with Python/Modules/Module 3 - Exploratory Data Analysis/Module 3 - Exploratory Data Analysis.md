

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ALTHZXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFlHTjoEhCSHzH2chVWyY7olpC1viNLbJkTAsHSRZB2AIgV%2BB7NEuWOSmL%2FCLTkfa0XREJYYi%2B6TaNd66DffncaSgqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBDhN7UVkFoQL8v9hircAwEjN15mLsw7SSSGN4qth7FpxrhgzO0i2m3iCBbNMxihsXL1npsGXPywQcxLDp5rIH5biTBKFFgfG%2B1CKR%2FIEtncIrb8DrT7S3FNZIYsi90bEh3PWgP%2Fwx8OroYDDRn%2FCregBEHXpM%2BIY0JVaJKn4uO29EBgWPA%2FpPH9%2FxsP7tc%2FVYPqPZ4Ck6PuX3%2FlEqWt4FGwfeDfvhDIolnO87Nt05eyl%2BNc9ZxnhOQFA%2BUuGXEo%2BbPqZdy9TDqq2pVhbyO1R2mMc8Iw4UzpYUcFgTivnTPErGlsqAKPVB1J8OX7qg%2F7V27%2FSxi9CHqNyGfoxQ%2FSDN7jlRFYr2KFEvN2qkwnndR%2BMhi7ojqB6oAfo1p7o0mml1QYEX5nNz2eW9VTOcxJZyfwA35OmCYzfO5BJRrHq5EbcpiTp9WT6XQ7QFWFpNvniUgCn1jN5XwbJkML8ZOlIJxoG1HXQNX6m6owguOID4z%2FJbadeFh3Cs18ZkXctBvRbKGtWkWxnRGlEFKV4WIHan9FjCbKsVD70O7A38Jgrk2%2BTw%2BHsqTC3MLYSHZpMfgLjeZEv%2Fs9ezSyZg0gN4AMxO49zerja1Wq8ppH0PFhroLx%2FxXWxMT2JhTWq2fyktDdSD8BYFdF%2BJQWDYV8MIyj7LwGOqUBvWaT2gn84guQS7KgWEZX%2B5gIHXXXZKFnqBiaPybU8X5ulYHjR0i14X8My%2FjN1cAApfYRKV9SOduk6q7ZABdrfh5BUTH9YWw1jxXoXUskh7qMB34BmlhWJlMTSg7V2Ns55ZIpnxQ1OZdX8hWJbHeTl85sl108ioKb74U6Dc1LTFoX%2FEMDCacI3viHMYud36afQXSMS1rSM6NpaDBqb6oe9xtwt73Q&X-Amz-Signature=e7d9c4a61c3dcecfe074948fc5d65a86d70d93d30ebf22afdd7eb5cd240d793e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ALTHZXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFlHTjoEhCSHzH2chVWyY7olpC1viNLbJkTAsHSRZB2AIgV%2BB7NEuWOSmL%2FCLTkfa0XREJYYi%2B6TaNd66DffncaSgqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBDhN7UVkFoQL8v9hircAwEjN15mLsw7SSSGN4qth7FpxrhgzO0i2m3iCBbNMxihsXL1npsGXPywQcxLDp5rIH5biTBKFFgfG%2B1CKR%2FIEtncIrb8DrT7S3FNZIYsi90bEh3PWgP%2Fwx8OroYDDRn%2FCregBEHXpM%2BIY0JVaJKn4uO29EBgWPA%2FpPH9%2FxsP7tc%2FVYPqPZ4Ck6PuX3%2FlEqWt4FGwfeDfvhDIolnO87Nt05eyl%2BNc9ZxnhOQFA%2BUuGXEo%2BbPqZdy9TDqq2pVhbyO1R2mMc8Iw4UzpYUcFgTivnTPErGlsqAKPVB1J8OX7qg%2F7V27%2FSxi9CHqNyGfoxQ%2FSDN7jlRFYr2KFEvN2qkwnndR%2BMhi7ojqB6oAfo1p7o0mml1QYEX5nNz2eW9VTOcxJZyfwA35OmCYzfO5BJRrHq5EbcpiTp9WT6XQ7QFWFpNvniUgCn1jN5XwbJkML8ZOlIJxoG1HXQNX6m6owguOID4z%2FJbadeFh3Cs18ZkXctBvRbKGtWkWxnRGlEFKV4WIHan9FjCbKsVD70O7A38Jgrk2%2BTw%2BHsqTC3MLYSHZpMfgLjeZEv%2Fs9ezSyZg0gN4AMxO49zerja1Wq8ppH0PFhroLx%2FxXWxMT2JhTWq2fyktDdSD8BYFdF%2BJQWDYV8MIyj7LwGOqUBvWaT2gn84guQS7KgWEZX%2B5gIHXXXZKFnqBiaPybU8X5ulYHjR0i14X8My%2FjN1cAApfYRKV9SOduk6q7ZABdrfh5BUTH9YWw1jxXoXUskh7qMB34BmlhWJlMTSg7V2Ns55ZIpnxQ1OZdX8hWJbHeTl85sl108ioKb74U6Dc1LTFoX%2FEMDCacI3viHMYud36afQXSMS1rSM6NpaDBqb6oe9xtwt73Q&X-Amz-Signature=0d0913933fa56255170f67b7cfbc86bc9daa4675f715fb4d9e375e1df196caf7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ALTHZXD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFlHTjoEhCSHzH2chVWyY7olpC1viNLbJkTAsHSRZB2AIgV%2BB7NEuWOSmL%2FCLTkfa0XREJYYi%2B6TaNd66DffncaSgqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBDhN7UVkFoQL8v9hircAwEjN15mLsw7SSSGN4qth7FpxrhgzO0i2m3iCBbNMxihsXL1npsGXPywQcxLDp5rIH5biTBKFFgfG%2B1CKR%2FIEtncIrb8DrT7S3FNZIYsi90bEh3PWgP%2Fwx8OroYDDRn%2FCregBEHXpM%2BIY0JVaJKn4uO29EBgWPA%2FpPH9%2FxsP7tc%2FVYPqPZ4Ck6PuX3%2FlEqWt4FGwfeDfvhDIolnO87Nt05eyl%2BNc9ZxnhOQFA%2BUuGXEo%2BbPqZdy9TDqq2pVhbyO1R2mMc8Iw4UzpYUcFgTivnTPErGlsqAKPVB1J8OX7qg%2F7V27%2FSxi9CHqNyGfoxQ%2FSDN7jlRFYr2KFEvN2qkwnndR%2BMhi7ojqB6oAfo1p7o0mml1QYEX5nNz2eW9VTOcxJZyfwA35OmCYzfO5BJRrHq5EbcpiTp9WT6XQ7QFWFpNvniUgCn1jN5XwbJkML8ZOlIJxoG1HXQNX6m6owguOID4z%2FJbadeFh3Cs18ZkXctBvRbKGtWkWxnRGlEFKV4WIHan9FjCbKsVD70O7A38Jgrk2%2BTw%2BHsqTC3MLYSHZpMfgLjeZEv%2Fs9ezSyZg0gN4AMxO49zerja1Wq8ppH0PFhroLx%2FxXWxMT2JhTWq2fyktDdSD8BYFdF%2BJQWDYV8MIyj7LwGOqUBvWaT2gn84guQS7KgWEZX%2B5gIHXXXZKFnqBiaPybU8X5ulYHjR0i14X8My%2FjN1cAApfYRKV9SOduk6q7ZABdrfh5BUTH9YWw1jxXoXUskh7qMB34BmlhWJlMTSg7V2Ns55ZIpnxQ1OZdX8hWJbHeTl85sl108ioKb74U6Dc1LTFoX%2FEMDCacI3viHMYud36afQXSMS1rSM6NpaDBqb6oe9xtwt73Q&X-Amz-Signature=ba7a2d84a9e22a1367cd2a9cbb481bbd4f506378448f9d82ba59dd420d083376&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEPIXPS4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLLed9s1MexsVxjQLAaavAs6B7gNLDegubdkgQKEeVOAiB3yF0N6TcgvMB7IPVoohnxIDS5mwXECYFIi7rYHeu0IyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbjb3lMI4tN%2B6AWA%2BKtwDK9F%2FmP2q3hN3SzcYT1sQj6%2BGhmuCqiA9yw97Kn6JS9TpFxFSGPO8d4PndqIcxzF7asFENX0Iw%2BRftmod3rlEsjnPm91c9k6XHUOe7PxuNa4nxj7dPd4qaIlhori0wwNXLXO2oNyDBPf8sIg99Fnj6znu5vSpcLld2MGUaNT6obEtKHORTlhNkqEKdC366tjN%2F8EKI8u%2BKucz344XeKEAPr8%2FkTPDKA39%2FSJ8NOX3q71fvpWooNoNR7ckMxoJ4vYAg7Dvw7KgYlTxZgvCbaNM3FUNEV8JQh%2BIMkH0jl32vN5Sv%2FSQ1O%2BjlWfbeQcW2vPnoJyzdqeCkUww04kMrJKL3%2BhwtURYNtHKwOu%2BwPpSrmkpqkXh1KnUaLC8Ol6XA2WCmNIjJ%2F3ObidtzEKhrHgKptLZZoIiFHf0%2FGe1OZQTWZ5FZnY3xy5DWWvorYNllUapn4Q8T20Dg0hMogvbkH9G%2Bv%2BdF4CVYO3gvYHKrg%2Btc0HbTt3OO5l6knR%2Fj1%2FKls33ShRX%2B0R6JHDh5geTC7PJRGcewmHgCCelLkRJL6NSjmiOYCI4xgnoSIQYyTJ8tR%2BdEWRn2uQ%2BLyMdca3rNT2rgwTZxtqx29cFdgnj4kPoBQQ1whfov6vXMfoP9qcwhaPsvAY6pgGDx6tlCxVdU1HhU%2BN%2B%2FZ%2BiqEeAgnU9QgQJljdloQjWSt%2B7S%2FJ%2BPLiC2cYtbZwaPnnnEneAX%2FoHX8XWQ%2BcbxzknY5HknqYE9%2BvkZ0ILAm7MK%2B%2Ff6XsvFJCQrU1EDwY8WdchOBTo%2Fjkarugqdp7fa4aqALXvTNOZi65lnBOKV%2F2jjAKIigOTbDIhHssuqq6MAKR%2FLTdUhBlqv%2B7OXv5YVNvkP7dqDoKy&X-Amz-Signature=645d5340495a13059ceb3555710a30d83a7496a7aa54a137358657b044ba5ceb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEPIXPS4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLLed9s1MexsVxjQLAaavAs6B7gNLDegubdkgQKEeVOAiB3yF0N6TcgvMB7IPVoohnxIDS5mwXECYFIi7rYHeu0IyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbjb3lMI4tN%2B6AWA%2BKtwDK9F%2FmP2q3hN3SzcYT1sQj6%2BGhmuCqiA9yw97Kn6JS9TpFxFSGPO8d4PndqIcxzF7asFENX0Iw%2BRftmod3rlEsjnPm91c9k6XHUOe7PxuNa4nxj7dPd4qaIlhori0wwNXLXO2oNyDBPf8sIg99Fnj6znu5vSpcLld2MGUaNT6obEtKHORTlhNkqEKdC366tjN%2F8EKI8u%2BKucz344XeKEAPr8%2FkTPDKA39%2FSJ8NOX3q71fvpWooNoNR7ckMxoJ4vYAg7Dvw7KgYlTxZgvCbaNM3FUNEV8JQh%2BIMkH0jl32vN5Sv%2FSQ1O%2BjlWfbeQcW2vPnoJyzdqeCkUww04kMrJKL3%2BhwtURYNtHKwOu%2BwPpSrmkpqkXh1KnUaLC8Ol6XA2WCmNIjJ%2F3ObidtzEKhrHgKptLZZoIiFHf0%2FGe1OZQTWZ5FZnY3xy5DWWvorYNllUapn4Q8T20Dg0hMogvbkH9G%2Bv%2BdF4CVYO3gvYHKrg%2Btc0HbTt3OO5l6knR%2Fj1%2FKls33ShRX%2B0R6JHDh5geTC7PJRGcewmHgCCelLkRJL6NSjmiOYCI4xgnoSIQYyTJ8tR%2BdEWRn2uQ%2BLyMdca3rNT2rgwTZxtqx29cFdgnj4kPoBQQ1whfov6vXMfoP9qcwhaPsvAY6pgGDx6tlCxVdU1HhU%2BN%2B%2FZ%2BiqEeAgnU9QgQJljdloQjWSt%2B7S%2FJ%2BPLiC2cYtbZwaPnnnEneAX%2FoHX8XWQ%2BcbxzknY5HknqYE9%2BvkZ0ILAm7MK%2B%2Ff6XsvFJCQrU1EDwY8WdchOBTo%2Fjkarugqdp7fa4aqALXvTNOZi65lnBOKV%2F2jjAKIigOTbDIhHssuqq6MAKR%2FLTdUhBlqv%2B7OXv5YVNvkP7dqDoKy&X-Amz-Signature=7b2f3f417a9949c26654c5e7cfbd5ec7562b75336717ab5809efe27e274e5c3a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEPIXPS4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLLed9s1MexsVxjQLAaavAs6B7gNLDegubdkgQKEeVOAiB3yF0N6TcgvMB7IPVoohnxIDS5mwXECYFIi7rYHeu0IyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbjb3lMI4tN%2B6AWA%2BKtwDK9F%2FmP2q3hN3SzcYT1sQj6%2BGhmuCqiA9yw97Kn6JS9TpFxFSGPO8d4PndqIcxzF7asFENX0Iw%2BRftmod3rlEsjnPm91c9k6XHUOe7PxuNa4nxj7dPd4qaIlhori0wwNXLXO2oNyDBPf8sIg99Fnj6znu5vSpcLld2MGUaNT6obEtKHORTlhNkqEKdC366tjN%2F8EKI8u%2BKucz344XeKEAPr8%2FkTPDKA39%2FSJ8NOX3q71fvpWooNoNR7ckMxoJ4vYAg7Dvw7KgYlTxZgvCbaNM3FUNEV8JQh%2BIMkH0jl32vN5Sv%2FSQ1O%2BjlWfbeQcW2vPnoJyzdqeCkUww04kMrJKL3%2BhwtURYNtHKwOu%2BwPpSrmkpqkXh1KnUaLC8Ol6XA2WCmNIjJ%2F3ObidtzEKhrHgKptLZZoIiFHf0%2FGe1OZQTWZ5FZnY3xy5DWWvorYNllUapn4Q8T20Dg0hMogvbkH9G%2Bv%2BdF4CVYO3gvYHKrg%2Btc0HbTt3OO5l6knR%2Fj1%2FKls33ShRX%2B0R6JHDh5geTC7PJRGcewmHgCCelLkRJL6NSjmiOYCI4xgnoSIQYyTJ8tR%2BdEWRn2uQ%2BLyMdca3rNT2rgwTZxtqx29cFdgnj4kPoBQQ1whfov6vXMfoP9qcwhaPsvAY6pgGDx6tlCxVdU1HhU%2BN%2B%2FZ%2BiqEeAgnU9QgQJljdloQjWSt%2B7S%2FJ%2BPLiC2cYtbZwaPnnnEneAX%2FoHX8XWQ%2BcbxzknY5HknqYE9%2BvkZ0ILAm7MK%2B%2Ff6XsvFJCQrU1EDwY8WdchOBTo%2Fjkarugqdp7fa4aqALXvTNOZi65lnBOKV%2F2jjAKIigOTbDIhHssuqq6MAKR%2FLTdUhBlqv%2B7OXv5YVNvkP7dqDoKy&X-Amz-Signature=d10416d13d5452cddcb88340c0ed9af8431f0e4c99e38d9761d5e7be1571a9c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEPIXPS4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLLed9s1MexsVxjQLAaavAs6B7gNLDegubdkgQKEeVOAiB3yF0N6TcgvMB7IPVoohnxIDS5mwXECYFIi7rYHeu0IyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbjb3lMI4tN%2B6AWA%2BKtwDK9F%2FmP2q3hN3SzcYT1sQj6%2BGhmuCqiA9yw97Kn6JS9TpFxFSGPO8d4PndqIcxzF7asFENX0Iw%2BRftmod3rlEsjnPm91c9k6XHUOe7PxuNa4nxj7dPd4qaIlhori0wwNXLXO2oNyDBPf8sIg99Fnj6znu5vSpcLld2MGUaNT6obEtKHORTlhNkqEKdC366tjN%2F8EKI8u%2BKucz344XeKEAPr8%2FkTPDKA39%2FSJ8NOX3q71fvpWooNoNR7ckMxoJ4vYAg7Dvw7KgYlTxZgvCbaNM3FUNEV8JQh%2BIMkH0jl32vN5Sv%2FSQ1O%2BjlWfbeQcW2vPnoJyzdqeCkUww04kMrJKL3%2BhwtURYNtHKwOu%2BwPpSrmkpqkXh1KnUaLC8Ol6XA2WCmNIjJ%2F3ObidtzEKhrHgKptLZZoIiFHf0%2FGe1OZQTWZ5FZnY3xy5DWWvorYNllUapn4Q8T20Dg0hMogvbkH9G%2Bv%2BdF4CVYO3gvYHKrg%2Btc0HbTt3OO5l6knR%2Fj1%2FKls33ShRX%2B0R6JHDh5geTC7PJRGcewmHgCCelLkRJL6NSjmiOYCI4xgnoSIQYyTJ8tR%2BdEWRn2uQ%2BLyMdca3rNT2rgwTZxtqx29cFdgnj4kPoBQQ1whfov6vXMfoP9qcwhaPsvAY6pgGDx6tlCxVdU1HhU%2BN%2B%2FZ%2BiqEeAgnU9QgQJljdloQjWSt%2B7S%2FJ%2BPLiC2cYtbZwaPnnnEneAX%2FoHX8XWQ%2BcbxzknY5HknqYE9%2BvkZ0ILAm7MK%2B%2Ff6XsvFJCQrU1EDwY8WdchOBTo%2Fjkarugqdp7fa4aqALXvTNOZi65lnBOKV%2F2jjAKIigOTbDIhHssuqq6MAKR%2FLTdUhBlqv%2B7OXv5YVNvkP7dqDoKy&X-Amz-Signature=5dc7634de4ccf08cd9b5fcc8b21f8cf9aa6c9e17970069193a31e82a268e7a44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEPIXPS4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLLed9s1MexsVxjQLAaavAs6B7gNLDegubdkgQKEeVOAiB3yF0N6TcgvMB7IPVoohnxIDS5mwXECYFIi7rYHeu0IyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbjb3lMI4tN%2B6AWA%2BKtwDK9F%2FmP2q3hN3SzcYT1sQj6%2BGhmuCqiA9yw97Kn6JS9TpFxFSGPO8d4PndqIcxzF7asFENX0Iw%2BRftmod3rlEsjnPm91c9k6XHUOe7PxuNa4nxj7dPd4qaIlhori0wwNXLXO2oNyDBPf8sIg99Fnj6znu5vSpcLld2MGUaNT6obEtKHORTlhNkqEKdC366tjN%2F8EKI8u%2BKucz344XeKEAPr8%2FkTPDKA39%2FSJ8NOX3q71fvpWooNoNR7ckMxoJ4vYAg7Dvw7KgYlTxZgvCbaNM3FUNEV8JQh%2BIMkH0jl32vN5Sv%2FSQ1O%2BjlWfbeQcW2vPnoJyzdqeCkUww04kMrJKL3%2BhwtURYNtHKwOu%2BwPpSrmkpqkXh1KnUaLC8Ol6XA2WCmNIjJ%2F3ObidtzEKhrHgKptLZZoIiFHf0%2FGe1OZQTWZ5FZnY3xy5DWWvorYNllUapn4Q8T20Dg0hMogvbkH9G%2Bv%2BdF4CVYO3gvYHKrg%2Btc0HbTt3OO5l6knR%2Fj1%2FKls33ShRX%2B0R6JHDh5geTC7PJRGcewmHgCCelLkRJL6NSjmiOYCI4xgnoSIQYyTJ8tR%2BdEWRn2uQ%2BLyMdca3rNT2rgwTZxtqx29cFdgnj4kPoBQQ1whfov6vXMfoP9qcwhaPsvAY6pgGDx6tlCxVdU1HhU%2BN%2B%2FZ%2BiqEeAgnU9QgQJljdloQjWSt%2B7S%2FJ%2BPLiC2cYtbZwaPnnnEneAX%2FoHX8XWQ%2BcbxzknY5HknqYE9%2BvkZ0ILAm7MK%2B%2Ff6XsvFJCQrU1EDwY8WdchOBTo%2Fjkarugqdp7fa4aqALXvTNOZi65lnBOKV%2F2jjAKIigOTbDIhHssuqq6MAKR%2FLTdUhBlqv%2B7OXv5YVNvkP7dqDoKy&X-Amz-Signature=a32adc896be3d589309ae47d2fb3260ddf99533c2366959c5b66d0c5f47a2dd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEPIXPS4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLLed9s1MexsVxjQLAaavAs6B7gNLDegubdkgQKEeVOAiB3yF0N6TcgvMB7IPVoohnxIDS5mwXECYFIi7rYHeu0IyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbjb3lMI4tN%2B6AWA%2BKtwDK9F%2FmP2q3hN3SzcYT1sQj6%2BGhmuCqiA9yw97Kn6JS9TpFxFSGPO8d4PndqIcxzF7asFENX0Iw%2BRftmod3rlEsjnPm91c9k6XHUOe7PxuNa4nxj7dPd4qaIlhori0wwNXLXO2oNyDBPf8sIg99Fnj6znu5vSpcLld2MGUaNT6obEtKHORTlhNkqEKdC366tjN%2F8EKI8u%2BKucz344XeKEAPr8%2FkTPDKA39%2FSJ8NOX3q71fvpWooNoNR7ckMxoJ4vYAg7Dvw7KgYlTxZgvCbaNM3FUNEV8JQh%2BIMkH0jl32vN5Sv%2FSQ1O%2BjlWfbeQcW2vPnoJyzdqeCkUww04kMrJKL3%2BhwtURYNtHKwOu%2BwPpSrmkpqkXh1KnUaLC8Ol6XA2WCmNIjJ%2F3ObidtzEKhrHgKptLZZoIiFHf0%2FGe1OZQTWZ5FZnY3xy5DWWvorYNllUapn4Q8T20Dg0hMogvbkH9G%2Bv%2BdF4CVYO3gvYHKrg%2Btc0HbTt3OO5l6knR%2Fj1%2FKls33ShRX%2B0R6JHDh5geTC7PJRGcewmHgCCelLkRJL6NSjmiOYCI4xgnoSIQYyTJ8tR%2BdEWRn2uQ%2BLyMdca3rNT2rgwTZxtqx29cFdgnj4kPoBQQ1whfov6vXMfoP9qcwhaPsvAY6pgGDx6tlCxVdU1HhU%2BN%2B%2FZ%2BiqEeAgnU9QgQJljdloQjWSt%2B7S%2FJ%2BPLiC2cYtbZwaPnnnEneAX%2FoHX8XWQ%2BcbxzknY5HknqYE9%2BvkZ0ILAm7MK%2B%2Ff6XsvFJCQrU1EDwY8WdchOBTo%2Fjkarugqdp7fa4aqALXvTNOZi65lnBOKV%2F2jjAKIigOTbDIhHssuqq6MAKR%2FLTdUhBlqv%2B7OXv5YVNvkP7dqDoKy&X-Amz-Signature=159928be1f28849bd95016290d57f6a886793990f94c4ad83ad51da025fcde97&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LHA5EKQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQPdcSlVQ9Y9j3NUe%2Ftz5dktO2NtjhhZ%2BiTXVWP%2FogFAIhAP6uYjkNdLB%2FT3Y4m%2FQJADgUK9Wl7B35jLLM%2FloAwygWKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAIyR0x42VmfgNwHIq3AOdnuGNcOpq6zlY4clSIUVZsqgZAkdTppWgyxq5RIHH%2B0gQiuy%2FWVidJz8jucYrAGIyv4Y87eZzvJN4YQn%2FJp71eofc4VFZOLfPJRwfR5rTU3stTXRqNKpgyKVe1Kx%2Fxp0xjFRWTO36wMdvQGve1kf%2BKge2I4HFWZRsDxYLAME%2Bp1C88A1Mq%2FFv9JQc7WnDwPxlOdGvNMErgIss02BPKXKep4kJTZQ2UiSTtKviOenuyYgmrdB0wlCxd6oe7%2B7YO6%2BVSpC5ut4gH4SZquLykHgf064WOO1ibAzbNq5PGwkbT8EMa9Ck01iMWtNlcCZ3T30AlyOZDhzKfd0jY%2F9cNmupXCZaeMu70GrUnJB65rvQIcTxGEZ4uKdTd1mt36mATDE%2FVZYrlKcezk%2FKR7YZ34OtiqJut%2F%2FatkUMPlcF6i6mBkujaVaY9V2Mx76qyb4JiNPuhEZljsFzsy6cjxkkMawF%2Fhp2vvlMtFSjxtPyqCtZQB%2FCUJM0R50fVpkQ0R%2FI%2BixqTHCYwCaDrU4Ruzwj8F27ZaWOLVAanc2haQh0kXMZpQLdj6n%2F7vWi7YfweLlX7FAEbn6oizl%2B5NAArq6tX2Qi8EPcKwdZUEJydnDL3x5gYPECTqjJZRlg3dwNYDDSouy8BjqkAYNuF4bXetkaZ%2Fczh91qnYMos56K6kbwpfDM7nYEMgSxhoAzW1lXkoI0m%2FO6LW2vULnAl%2FGTwsR2gJV%2BT36B8qglgGYoWrbVz15Vy13xWPn2yts1gYOLUhkwKQReUqGq%2F4T9sOXba8Fig9gFXJG5p1WMkrCyZrJR9DhXamD7mBn3QaBeOxxJTRBIAxMozeJ5JzT6ciPbG8PodZs4i%2Bgnbf0mxMxx&X-Amz-Signature=0b297008cbca9eb44615f8ac4446194203bd920a0d3da06c668a8808254f1172&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644RZD2CY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE5tu0vhqfrNltRnroqslICfR%2BcrLdI4f7O1GG7FgdmAAiAuT6fF9GgflKPhyT%2Fds784fybaZ5GkYOSC0BgFXAv3xyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJds7q1jKTQJziMagKtwDpy3ZXbTI5Ar121pBNNP5aqhq0dp0lfZRjfG2UED0lKAcrRAxxXA4EHrFO2LW7kRRwlpTzGEEqeuUzMI7n%2Ftv2VGVglq64yDlFI4u0P4QC5JvNWUvU%2Fmkbr3TY3dMJ9mwL6a6DTW8aXRPfUpZa1p1tvHXRPDD0AIon3STlJGLP32XGJVg65b1jkE4NhcUP6cgLAJA%2BNYMB2KYog0Aoe%2F8Lu1K6qg4m%2BJwohqdJytmAoieYl7rYPCwvs9OMkNhfDpXOY%2FEU580VgqVkUely1YnSzkgyAZbg%2Ffg%2BiB0PnW4WyLGMQhwWghL%2BarJQwHKIvw%2Fn90QnXr%2BZaYXKZAi7%2FZBf0pIBKr7ZqiNmz73z8If7of0%2B2wha%2F%2FDZ18s%2B25nJrI1sKqivHM6KFU9F9i4YmP2lJGYt3zzMD3ZuAw3MebLkb69WIzv3B1dlDlV%2F3STNLShBKk0JKHBRlnvQI57AF8PEByYypOdCrwLTKqQr7%2BXskdPanfgwsfHlpIzg%2BdBykGiMs%2BhTi3MBJq1q9KxurDmZPCiVsu7Dk9y6NqGKqB2oZhKcb3e5t4kXzt%2F8gA8nR6iE0R0Gt4uX38aYp8O4zGkLTjm1ITG8WnL%2FQx96afmJIdJadC3WKwjebUKtMswx6LsvAY6pgE3mcRsTl%2BulHnwf8mL9lM9pf%2B%2FNnJMLDcJyueG1nsX66Z71SQA4dGQL%2FIC3zRFCkjzF6UX73yuXqVUiiaNH87%2FK8WiOQLTJ2mS9O7CwxJIJqwrYOGEmk4W5qALFcp1Cx6CrWOvhvQT2P5NP0%2BStfvgWRhN0bWRqGZslx9usM6Fp%2FTR2J0YGsnoi5oqfZQrjxspyifuDg8IBnH3TMuIYN3ZaoFHf2KH&X-Amz-Signature=3dad1876f7a65c054e29abc3c6ef232557917e15411b32ede2f74a7e728c3c94&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEPIXPS4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLLed9s1MexsVxjQLAaavAs6B7gNLDegubdkgQKEeVOAiB3yF0N6TcgvMB7IPVoohnxIDS5mwXECYFIi7rYHeu0IyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbjb3lMI4tN%2B6AWA%2BKtwDK9F%2FmP2q3hN3SzcYT1sQj6%2BGhmuCqiA9yw97Kn6JS9TpFxFSGPO8d4PndqIcxzF7asFENX0Iw%2BRftmod3rlEsjnPm91c9k6XHUOe7PxuNa4nxj7dPd4qaIlhori0wwNXLXO2oNyDBPf8sIg99Fnj6znu5vSpcLld2MGUaNT6obEtKHORTlhNkqEKdC366tjN%2F8EKI8u%2BKucz344XeKEAPr8%2FkTPDKA39%2FSJ8NOX3q71fvpWooNoNR7ckMxoJ4vYAg7Dvw7KgYlTxZgvCbaNM3FUNEV8JQh%2BIMkH0jl32vN5Sv%2FSQ1O%2BjlWfbeQcW2vPnoJyzdqeCkUww04kMrJKL3%2BhwtURYNtHKwOu%2BwPpSrmkpqkXh1KnUaLC8Ol6XA2WCmNIjJ%2F3ObidtzEKhrHgKptLZZoIiFHf0%2FGe1OZQTWZ5FZnY3xy5DWWvorYNllUapn4Q8T20Dg0hMogvbkH9G%2Bv%2BdF4CVYO3gvYHKrg%2Btc0HbTt3OO5l6knR%2Fj1%2FKls33ShRX%2B0R6JHDh5geTC7PJRGcewmHgCCelLkRJL6NSjmiOYCI4xgnoSIQYyTJ8tR%2BdEWRn2uQ%2BLyMdca3rNT2rgwTZxtqx29cFdgnj4kPoBQQ1whfov6vXMfoP9qcwhaPsvAY6pgGDx6tlCxVdU1HhU%2BN%2B%2FZ%2BiqEeAgnU9QgQJljdloQjWSt%2B7S%2FJ%2BPLiC2cYtbZwaPnnnEneAX%2FoHX8XWQ%2BcbxzknY5HknqYE9%2BvkZ0ILAm7MK%2B%2Ff6XsvFJCQrU1EDwY8WdchOBTo%2Fjkarugqdp7fa4aqALXvTNOZi65lnBOKV%2F2jjAKIigOTbDIhHssuqq6MAKR%2FLTdUhBlqv%2B7OXv5YVNvkP7dqDoKy&X-Amz-Signature=94bd186238418a0998bc5c98fc898a07d3deb58d00531824bce30e67fb802d5f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEPIXPS4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLLed9s1MexsVxjQLAaavAs6B7gNLDegubdkgQKEeVOAiB3yF0N6TcgvMB7IPVoohnxIDS5mwXECYFIi7rYHeu0IyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbjb3lMI4tN%2B6AWA%2BKtwDK9F%2FmP2q3hN3SzcYT1sQj6%2BGhmuCqiA9yw97Kn6JS9TpFxFSGPO8d4PndqIcxzF7asFENX0Iw%2BRftmod3rlEsjnPm91c9k6XHUOe7PxuNa4nxj7dPd4qaIlhori0wwNXLXO2oNyDBPf8sIg99Fnj6znu5vSpcLld2MGUaNT6obEtKHORTlhNkqEKdC366tjN%2F8EKI8u%2BKucz344XeKEAPr8%2FkTPDKA39%2FSJ8NOX3q71fvpWooNoNR7ckMxoJ4vYAg7Dvw7KgYlTxZgvCbaNM3FUNEV8JQh%2BIMkH0jl32vN5Sv%2FSQ1O%2BjlWfbeQcW2vPnoJyzdqeCkUww04kMrJKL3%2BhwtURYNtHKwOu%2BwPpSrmkpqkXh1KnUaLC8Ol6XA2WCmNIjJ%2F3ObidtzEKhrHgKptLZZoIiFHf0%2FGe1OZQTWZ5FZnY3xy5DWWvorYNllUapn4Q8T20Dg0hMogvbkH9G%2Bv%2BdF4CVYO3gvYHKrg%2Btc0HbTt3OO5l6knR%2Fj1%2FKls33ShRX%2B0R6JHDh5geTC7PJRGcewmHgCCelLkRJL6NSjmiOYCI4xgnoSIQYyTJ8tR%2BdEWRn2uQ%2BLyMdca3rNT2rgwTZxtqx29cFdgnj4kPoBQQ1whfov6vXMfoP9qcwhaPsvAY6pgGDx6tlCxVdU1HhU%2BN%2B%2FZ%2BiqEeAgnU9QgQJljdloQjWSt%2B7S%2FJ%2BPLiC2cYtbZwaPnnnEneAX%2FoHX8XWQ%2BcbxzknY5HknqYE9%2BvkZ0ILAm7MK%2B%2Ff6XsvFJCQrU1EDwY8WdchOBTo%2Fjkarugqdp7fa4aqALXvTNOZi65lnBOKV%2F2jjAKIigOTbDIhHssuqq6MAKR%2FLTdUhBlqv%2B7OXv5YVNvkP7dqDoKy&X-Amz-Signature=7806d25b3a50a0b7d3cc3c2b3fab9e0d532b0aabb5e1ee962bb722b3a3369295&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEPIXPS4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLLed9s1MexsVxjQLAaavAs6B7gNLDegubdkgQKEeVOAiB3yF0N6TcgvMB7IPVoohnxIDS5mwXECYFIi7rYHeu0IyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbjb3lMI4tN%2B6AWA%2BKtwDK9F%2FmP2q3hN3SzcYT1sQj6%2BGhmuCqiA9yw97Kn6JS9TpFxFSGPO8d4PndqIcxzF7asFENX0Iw%2BRftmod3rlEsjnPm91c9k6XHUOe7PxuNa4nxj7dPd4qaIlhori0wwNXLXO2oNyDBPf8sIg99Fnj6znu5vSpcLld2MGUaNT6obEtKHORTlhNkqEKdC366tjN%2F8EKI8u%2BKucz344XeKEAPr8%2FkTPDKA39%2FSJ8NOX3q71fvpWooNoNR7ckMxoJ4vYAg7Dvw7KgYlTxZgvCbaNM3FUNEV8JQh%2BIMkH0jl32vN5Sv%2FSQ1O%2BjlWfbeQcW2vPnoJyzdqeCkUww04kMrJKL3%2BhwtURYNtHKwOu%2BwPpSrmkpqkXh1KnUaLC8Ol6XA2WCmNIjJ%2F3ObidtzEKhrHgKptLZZoIiFHf0%2FGe1OZQTWZ5FZnY3xy5DWWvorYNllUapn4Q8T20Dg0hMogvbkH9G%2Bv%2BdF4CVYO3gvYHKrg%2Btc0HbTt3OO5l6knR%2Fj1%2FKls33ShRX%2B0R6JHDh5geTC7PJRGcewmHgCCelLkRJL6NSjmiOYCI4xgnoSIQYyTJ8tR%2BdEWRn2uQ%2BLyMdca3rNT2rgwTZxtqx29cFdgnj4kPoBQQ1whfov6vXMfoP9qcwhaPsvAY6pgGDx6tlCxVdU1HhU%2BN%2B%2FZ%2BiqEeAgnU9QgQJljdloQjWSt%2B7S%2FJ%2BPLiC2cYtbZwaPnnnEneAX%2FoHX8XWQ%2BcbxzknY5HknqYE9%2BvkZ0ILAm7MK%2B%2Ff6XsvFJCQrU1EDwY8WdchOBTo%2Fjkarugqdp7fa4aqALXvTNOZi65lnBOKV%2F2jjAKIigOTbDIhHssuqq6MAKR%2FLTdUhBlqv%2B7OXv5YVNvkP7dqDoKy&X-Amz-Signature=f3c74a972f41999c753615148773dc571e352200494d4819685195f0e1272ba7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCVAINPC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtzySsn1DZoNAiM3PCT%2BFSe1FWcoh9yxHea6oJt4o9lQIhAPttVDVwPu0iqPD7bPNFPYnghL0XNIoPKWbATWF8gX8dKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwmk%2B0B74neOLm%2BUXsq3AM9mseudK9ltbm3J9Je9Bos2fqAULq3csdHKvvnHKIZhqYKYW6QY1hkAVmzzwBOsWIzU1hnE89KKJse3ixBEYJV5c8lpCyNqGpPv1%2FD%2Fmxubjt%2Bu5kkSJ1cpcHPl22Ezlnh%2FZL1uPaHj%2FplvG2Dj6kQpGo6CiDncwpWO8q38uV5uYFMut1YJAkVVi%2FyT0ml%2BbYFPTMDeuXtYv9JCU0doR4ZCTHPFrXyKEGrk0%2Fmr%2B6xCQ9HW4mec6iVpD6Qyi2IfPIygDmCSpIP7f2QpsVe5M4jS%2BuBnulGkIG5Y6uIrFd8gwz7SSCAx3efK69UCq1R%2Bc1pVLzOTSjlaU1HJxfazsIlGkB12TmbSzrnRFrF%2F97%2FWc14iyqRX930T%2FPr6Ei7JBaS819bbwbxkBZpnZmtu%2FHBZoEywOH8w%2BRl%2BA%2FyeCUmqbMHt%2FcfANy9mlfqfDjjTu%2BwqnKjXv%2B9K4KtwPPsXhukbzdeAOz2vviujE8%2FVDm82%2B9St4DH8%2FidBhr13be1GOzUFDwWmhh%2Bq%2BqKyadwnaaagfFEtDN9g96BlN7w8FdqIVNm35anxbdrNICg5Qac6KWnfFn4MlPVYkNOxSALl3psapJnfeavw0UZm%2FbSN6Y0igOg%2BAeFXAN8bl1WrjDZouy8BjqkARnp1hTUnQ0Jlqqv0IPs2O%2B%2BWMb5%2BiOHkweOti9dvSsUW0QYWY5aicuZdEAaMRAXIY3h4g3jGR1%2B9eH3aTXkzd9FEg3qCM9hZNEjdyB6B5%2B%2BEVZrPZxuXjR9Dd%2FjDi1qjcG2uVgxsMgficj97aSAijSEkLAJe4apz1et%2Bkthw8UC62SvjVp717JNtRJONNI7Gvuv3f%2FMoS7otLEugOnu%2F%2F58IRf4&X-Amz-Signature=fb6ca7f25531542774fb2e56c7ca87669a848a2ac36fab1121c5cbb8f52739bb&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PNCN3AK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECCP6%2BPlQ9CAmtnW3FOAWB5CfOI1OWW%2BPaEWygLJNRqAiB827%2B02S3%2Bi86bJZaw%2BVK9iFuvcU1IGotc781OqParQyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlbw4Xm%2Bz%2By00ajUlKtwDfMQx%2Fn%2F70lrAENZ%2BWmIq2dMOWsAt5zquTuoKY5R13Zk46QIZi6QY5BXxQgUZx69owOpkpdo0DLwBePMltMaf%2F8VzZb2TfwLwFvKCvZPHeT1NIju9Ie2jVY74E4%2F1wf11fxD3oBsQlP%2B9ymNVIXvyWCWzlHVEB1O1QGbgRtNNQMoEmVLhIBHsc9kxXBENOC%2BO%2FfiCiDkd6pGaWg9cq4AJ2eAZyOjkYnJWCoHPyZ5ZUgwiFankBfefhYHNZ%2FiCcgeZlLFCzTdH82WLimeCMWI9SKZH%2BFO6qqm533iAEy3cVK5RRkxjTcfochz%2F0fTg4uLILWLZbjvA6Lq02NCXhAt74in2WXzwGLXiZQSf6qKCbdKkLsECPcRFajJdAcW9NByjQjtH2Qbx3%2FXAIheME10OPaB6n4%2FrmwHXh1hVKuXIPdzPAzcy5c1Msus0uzXov76ebEjREc3Lxk7HnVJP5uRFJu6SSV%2BmdedFeT%2FRsKpJ5Z7DhZiAkgG%2BAtdA9EjCua0%2BmcjucZvkCZSPtBLXKkn593rn9Q6TwNUCFdjdN4kQH0OK2BMBmezpFdTwNzC84JaocDzoREkFb8mKIpb8zehHWcfj6ZTudJy44vSRFNZGoCaaXX79TlSvvGDm5Owwy6LsvAY6pgF0t9GB0PI39TIWy7Xxrm6%2FyB3TnaqrE6w6DQLmYPV7YUFKr%2FwYkPNk4De%2B1i496b8lBuqPw%2BkZ%2BK9lgA9qKOVpewcA%2FoOklAhD00QbXJyqeRw6vb2hbyFVmLcUIeNpla2gNyc%2B%2BaLjdjSvOU2kf9clkX%2FqRYtESS1gnyYtDtf0Ul%2FXiUyRvYx47wjoGv95l%2F0KhLgaqGuTeDlyLYUDww2Iihvza%2FyI&X-Amz-Signature=3bb20bddd928e1b37f347ddbcea00d391c51c9b1fea03417ccafa7ef2f49743e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643YH6LCR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXpwecSw9AK3gj6gGlXaj8Kq0k2jORcl5HVrhC2iH9XQIhAMZX1CKEU277R5%2Bpl%2BHISphqQpLoqARgP19bNzqeMMqNKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzg4Xg%2BpKfekK%2BodLQq3ANQLW1%2Bb9hAdcbClpNWepdN8ECK58OPNqoxZAsq4NNoq33Kd7%2FqStuVArort97KnILhuJqFCyey%2FDUmo%2BclJd9ZlFH2ISTUqRe%2FaPBxOae1ia7E2Z4v2YM%2B9%2Bm%2BqcOw73oe5c2scd6Jo3X2%2BE2nwHLqy3hIX%2Fr76jbvuRQ3hYo3lqflunY5GrUN7V8Wn2gnxciUvopuqsfzGHIlgarT7EYOFPLw6U25GPO33O3w%2BclTAslU4F7LTquKzu7371tLFB8ddlJquxEAAAIgVR72tSmrrkHA9a8gGIOjXjZTdp6VLUnqT6kxGeBH6%2FinH0ZZgJtO30GnA71NS8PLeGXAb2rDP3nW524bi0ueGh5RAL0ZgfNref4%2FvoWpxBhIhuuhVOBVuA9Yjd2YyfM7Nkp3NdkQt6aTk%2Fh98TSjD0XKzg7qKHzD2FtmUV1XEKR80ELxJAIRzi3AlBHuRdvUGSKqTFDek8pDSDeWrt2MXIc364lAaHDa%2B4Ozhh6djJRA2nuk3WIhwMtb%2FEr6y0UOq2ArfMJo4keFLfaFxz%2BqJEPwnLZyELasKIajtS6mzKQMLa7y4yzCS%2BQ88EhvR9D%2F3%2ForFcSMDzq3qpwcWZAW5OkFMFY9pephQWs%2FtuLL47mA2zCT6%2By8BjqkAfhl1zEVHYqfY580D%2F0D9LO101w0Thji2omqBDlkqoP0Z%2FefeHLTpxqjNVXdWi3alzEXPrjPw0WsxW1CjF3uokK2EumccMRc60cKJzEQICNB4gRFGU5TWhbBm9PM41XNk5qxeDiDcNOc7pKjnTaqB4FiSu8VV1j3dOhdZo%2FIIW2WxhuMxGWJk3ApNqzRP4yr45yb5WaSGipXFLQUSt0PLmyEjOWL&X-Amz-Signature=b9ef2a680ab2ecea2fdf1ec5573418abb91a035df1db607f422f9f2a797c2725&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2SG7RGK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9ra2R1i593w5CPod8O5xRJl3fWGNJ1aArubdEVuy%2BggIgMmDe%2FUt1vlbZalCWYxARD7%2B0Y4hQNv3gSCs3QuO8vP8qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRUHihEcMhjiVqQfCrcA5XAr12XZqmU9m9VePZ72illUxgEwp2HUNPuU9KLx2JxkgeHHtd24FxmIqyjyiXoZOzrJVirjop0qGu4ZrUVlXn4tKEPQfVpxRISWg0ZxdgA%2B3kxElLXUadFwQ4IJ11OzyuqtBAzvopHSKHalqBKuBVbgcGk6F%2FwDPhkFR0ZSyJNGhlSBwReOfO4h1vJSlaAddDg5Sw%2BueRmmug8tijIknKLlX0nClTLpbyqjGzUGCTUJE5E%2B27wlh3oOxN0bzWLkiqF4VBRvLno1xsSZZmv10TUvKlAHPeGDsCVjceM7VnW5%2FgLMml8xtnX2tjJjnHAeajWLuykSjkkXff%2BIREJvaitd4nc%2B50zFd974JzVXrXEYuAcCbEj9oQW2H%2FQbQw9zoSlRK7xHpKHhK8D5knPc8lIfjGkacq%2F9V9oySw%2BXofNj2rXj9LgKF2cGPKIDD6mo6b0DPI6yIZBjd%2FzlIxHlzMSGfOQlKvIrrYLbv4IN9zf6nvIwftd41c0niMmQesOUVduRcNKJBrA3e%2B%2F%2FBhu0x9mKkuEcE5A985zMAyBcWTJp8FoA0YRj1FTf42%2B60EEvOLd%2BBUJ4ZHImvgeXFRf82Vzka4pA1AH%2FxQgTWcUEBMbT18xWHlbxVmreKbvMInr7LwGOqUB78DIxX7k8W83Fm4tszjpP%2FbICDaJiumeLEOF32B2jVb9PYKSGKDF8hhh4WzWkACXQ1hzMPkEr2bVAkWzeicUa0DgHocJJU8NxXR0JOY4CfCAD37tYllWGDtHA%2FPOT98AhwOnoFGpBnlUcpH950357lGhI3nVAunkCOZTRX1Tw0iuET3%2F%2BV0jpIoTPLCYEUlueKQFxd0I%2BWwTA3%2BopxpV4XVhh%2BnU&X-Amz-Signature=a93637ed57d8b10404c2122c7b1b9a837d3965600a912d72ffc9e02499c6132c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2SG7RGK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9ra2R1i593w5CPod8O5xRJl3fWGNJ1aArubdEVuy%2BggIgMmDe%2FUt1vlbZalCWYxARD7%2B0Y4hQNv3gSCs3QuO8vP8qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRUHihEcMhjiVqQfCrcA5XAr12XZqmU9m9VePZ72illUxgEwp2HUNPuU9KLx2JxkgeHHtd24FxmIqyjyiXoZOzrJVirjop0qGu4ZrUVlXn4tKEPQfVpxRISWg0ZxdgA%2B3kxElLXUadFwQ4IJ11OzyuqtBAzvopHSKHalqBKuBVbgcGk6F%2FwDPhkFR0ZSyJNGhlSBwReOfO4h1vJSlaAddDg5Sw%2BueRmmug8tijIknKLlX0nClTLpbyqjGzUGCTUJE5E%2B27wlh3oOxN0bzWLkiqF4VBRvLno1xsSZZmv10TUvKlAHPeGDsCVjceM7VnW5%2FgLMml8xtnX2tjJjnHAeajWLuykSjkkXff%2BIREJvaitd4nc%2B50zFd974JzVXrXEYuAcCbEj9oQW2H%2FQbQw9zoSlRK7xHpKHhK8D5knPc8lIfjGkacq%2F9V9oySw%2BXofNj2rXj9LgKF2cGPKIDD6mo6b0DPI6yIZBjd%2FzlIxHlzMSGfOQlKvIrrYLbv4IN9zf6nvIwftd41c0niMmQesOUVduRcNKJBrA3e%2B%2F%2FBhu0x9mKkuEcE5A985zMAyBcWTJp8FoA0YRj1FTf42%2B60EEvOLd%2BBUJ4ZHImvgeXFRf82Vzka4pA1AH%2FxQgTWcUEBMbT18xWHlbxVmreKbvMInr7LwGOqUB78DIxX7k8W83Fm4tszjpP%2FbICDaJiumeLEOF32B2jVb9PYKSGKDF8hhh4WzWkACXQ1hzMPkEr2bVAkWzeicUa0DgHocJJU8NxXR0JOY4CfCAD37tYllWGDtHA%2FPOT98AhwOnoFGpBnlUcpH950357lGhI3nVAunkCOZTRX1Tw0iuET3%2F%2BV0jpIoTPLCYEUlueKQFxd0I%2BWwTA3%2BopxpV4XVhh%2BnU&X-Amz-Signature=fc91a7bc73fe72c4c7e4a3b6387a82353917b031e71f5f120037bbd8d100b87b&X-Amz-SignedHeaders=host&x-id=GetObject)

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
