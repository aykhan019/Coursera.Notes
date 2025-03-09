

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z34BIKHP%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQD6Nh1FsDuwJXQNUilV4NTAsI55k9xP5rleClI4%2FV%2Bx%2BQIgVOvVi5BcL10XA68yFkopyXpCpnuDtDNsnUDwzzMKpc8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBM3CJ%2B0K1t6YH23iSrcA5mB4x9C3UIy1KHLVOXmf1LSNkQI0Rbh33AwbiG9RI6uuT5uUXJJ%2Bv%2BZPQFCeKsfoZG9%2F34euSmMs7HWS2kbvm0oAEhMfdknTRwTEZOrPzRPj5ReiHBP4j%2FjvqTcVv02WP69fjmZLyJ%2FuHnr%2FVgvEq9ZnZbKoz5b0bLN%2FBZUXfrwUzLSpPyC1pVPYPJgqjevbHjVovbUD0pzE9kijr9P6zB48iFeH5ifh7qIF8z%2BIKfxOmpfc8Qqw1uornLeKS1oEGrYeCFZ3QY1qrrZWR%2Fxla4Q073myLtqXeYJ1ZngfPAcMy7AuRzInkeaccVLddWbDll616uDB2lMDog83qg3bmlV7TiYgr%2BgLJ7cSg3BIxV2bL1NQoXId1cRMVc5wYmDEi%2FtmKqnQAyIUc7ftF5igu54yEHN%2B0hi%2FpRFLCfvDQ%2BcfLRbYT2eSuOgooHd5dHJr1DtnYqzKWzgtOjCUr9kiN%2BJMy2tgpso8Uf8bIO8Qs2noyDOI7E46R3jQc%2BM1WyIa597tvuPdAuPzOJhiiLLdURGXmnUetiLIjrRARAXoUIcr92ANrynbruszaSDCZc2LexgdPhBmPhW8XnHcwCdprFJi5SdM2MngxMPSekGV8oQ89z6VLN%2FJOJ%2FzERXMLmps74GOqUBvidHRs9wvQLlGetiV8G8rN8N%2F78lB6kzq9rdMIhwqXXVJny7Mh%2FQHG9RFiHDdMQ5p8%2FG8DqB5Y1KQvp2nYmFj8r9FguEHl%2FoPfjw91g7SwhLsLy0n8zfdhy%2F%2FFCNoRSrx5kpp4YVR9u%2FVVdFOheNFqFELCiO8WXEzpAKQo71JMPvP7nbS3drLFySaGdQm8hjhsGaFl5DYOwSZtfSVh2G7TvTVR0P&X-Amz-Signature=989d466e119a83c605c7c8fed27c5c026417d9d5fa42efcbe980167242927ffe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z34BIKHP%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQD6Nh1FsDuwJXQNUilV4NTAsI55k9xP5rleClI4%2FV%2Bx%2BQIgVOvVi5BcL10XA68yFkopyXpCpnuDtDNsnUDwzzMKpc8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBM3CJ%2B0K1t6YH23iSrcA5mB4x9C3UIy1KHLVOXmf1LSNkQI0Rbh33AwbiG9RI6uuT5uUXJJ%2Bv%2BZPQFCeKsfoZG9%2F34euSmMs7HWS2kbvm0oAEhMfdknTRwTEZOrPzRPj5ReiHBP4j%2FjvqTcVv02WP69fjmZLyJ%2FuHnr%2FVgvEq9ZnZbKoz5b0bLN%2FBZUXfrwUzLSpPyC1pVPYPJgqjevbHjVovbUD0pzE9kijr9P6zB48iFeH5ifh7qIF8z%2BIKfxOmpfc8Qqw1uornLeKS1oEGrYeCFZ3QY1qrrZWR%2Fxla4Q073myLtqXeYJ1ZngfPAcMy7AuRzInkeaccVLddWbDll616uDB2lMDog83qg3bmlV7TiYgr%2BgLJ7cSg3BIxV2bL1NQoXId1cRMVc5wYmDEi%2FtmKqnQAyIUc7ftF5igu54yEHN%2B0hi%2FpRFLCfvDQ%2BcfLRbYT2eSuOgooHd5dHJr1DtnYqzKWzgtOjCUr9kiN%2BJMy2tgpso8Uf8bIO8Qs2noyDOI7E46R3jQc%2BM1WyIa597tvuPdAuPzOJhiiLLdURGXmnUetiLIjrRARAXoUIcr92ANrynbruszaSDCZc2LexgdPhBmPhW8XnHcwCdprFJi5SdM2MngxMPSekGV8oQ89z6VLN%2FJOJ%2FzERXMLmps74GOqUBvidHRs9wvQLlGetiV8G8rN8N%2F78lB6kzq9rdMIhwqXXVJny7Mh%2FQHG9RFiHDdMQ5p8%2FG8DqB5Y1KQvp2nYmFj8r9FguEHl%2FoPfjw91g7SwhLsLy0n8zfdhy%2F%2FFCNoRSrx5kpp4YVR9u%2FVVdFOheNFqFELCiO8WXEzpAKQo71JMPvP7nbS3drLFySaGdQm8hjhsGaFl5DYOwSZtfSVh2G7TvTVR0P&X-Amz-Signature=0ff015aa1fe6c1b158d0abee6a0221c2f8ba0c6d4e9e8ffc14a8e272c2e39eb2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z34BIKHP%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQD6Nh1FsDuwJXQNUilV4NTAsI55k9xP5rleClI4%2FV%2Bx%2BQIgVOvVi5BcL10XA68yFkopyXpCpnuDtDNsnUDwzzMKpc8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBM3CJ%2B0K1t6YH23iSrcA5mB4x9C3UIy1KHLVOXmf1LSNkQI0Rbh33AwbiG9RI6uuT5uUXJJ%2Bv%2BZPQFCeKsfoZG9%2F34euSmMs7HWS2kbvm0oAEhMfdknTRwTEZOrPzRPj5ReiHBP4j%2FjvqTcVv02WP69fjmZLyJ%2FuHnr%2FVgvEq9ZnZbKoz5b0bLN%2FBZUXfrwUzLSpPyC1pVPYPJgqjevbHjVovbUD0pzE9kijr9P6zB48iFeH5ifh7qIF8z%2BIKfxOmpfc8Qqw1uornLeKS1oEGrYeCFZ3QY1qrrZWR%2Fxla4Q073myLtqXeYJ1ZngfPAcMy7AuRzInkeaccVLddWbDll616uDB2lMDog83qg3bmlV7TiYgr%2BgLJ7cSg3BIxV2bL1NQoXId1cRMVc5wYmDEi%2FtmKqnQAyIUc7ftF5igu54yEHN%2B0hi%2FpRFLCfvDQ%2BcfLRbYT2eSuOgooHd5dHJr1DtnYqzKWzgtOjCUr9kiN%2BJMy2tgpso8Uf8bIO8Qs2noyDOI7E46R3jQc%2BM1WyIa597tvuPdAuPzOJhiiLLdURGXmnUetiLIjrRARAXoUIcr92ANrynbruszaSDCZc2LexgdPhBmPhW8XnHcwCdprFJi5SdM2MngxMPSekGV8oQ89z6VLN%2FJOJ%2FzERXMLmps74GOqUBvidHRs9wvQLlGetiV8G8rN8N%2F78lB6kzq9rdMIhwqXXVJny7Mh%2FQHG9RFiHDdMQ5p8%2FG8DqB5Y1KQvp2nYmFj8r9FguEHl%2FoPfjw91g7SwhLsLy0n8zfdhy%2F%2FFCNoRSrx5kpp4YVR9u%2FVVdFOheNFqFELCiO8WXEzpAKQo71JMPvP7nbS3drLFySaGdQm8hjhsGaFl5DYOwSZtfSVh2G7TvTVR0P&X-Amz-Signature=8bb5b84821032bc9610ec53994e8ad175dbf2714143e5a27a1c0b2f315cc999d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y7YXBDB%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDCDJp9WVnrDhXePt4qk1Wqmvq5nk4UpXnz5Nk81EGNQwIhALT8bqLIMeCH%2Fw0VWHdhiBT2B7jgdKe0CPRexjC0EZ5PKv8DCGkQABoMNjM3NDIzMTgzODA1IgxqDguNJlLQoFabhKYq3APRDoRjf2asfGXHjpeOrhJ0QKEnYLlo%2BEjDPVogew597D%2B59XOaiVvDFNVcWCRsKcp6kT2dloTMo9oa3jvqVFPlBQ4SMCs2rdKmAhInQYXKQ3%2Fb%2BowiT1lHsxiGi81ohc9EIwgEmX%2FaTK%2B4LHyj9%2BELLxaZnmqF09g1krGGKZPop4MGSQxpPqKPniVu9lr%2Bm8YcSMkqQjvTNzgfVkH1YA%2FD0kYviruMz0b%2Fk9xOmdMhFVFESU%2BOrasVwzpAh5bYanh3NC9Egau6wBu3zx7jl9qiw7gk4dPvI6eRtdMzq%2Bk4Ytr3Wfhb%2BHT4BOKUv1tFopK%2Bu%2BrNIponaLu49nkSzvUEagC2SqgI3bfkLB48LHl5RXmQ2gvBLIaHKUUOigtUOOY%2BxgNOaxMAp%2FE0McNMMAVBLjFCPQgNv579FopKIajyQCATCGWrccKXX9bMUzO8Jm%2F5MFhPMZyWH%2Fo328Pg89%2FZ1eJFycSJai0aSdNZc9nFsme%2BrAqEOQd1vEeD55Ba0JS2lhuJ32rBFPQ6KIZsCYXRXKWyJXdaLl8l6qZl54LszHvE0VqASHU0HrPWDsUHihgiSBDjB6NMXM9OPGUkeVQr4mYvPLnlCkwjTzFF6BsJTmjwNAnEN42%2BZAjK9DD6qbO%2BBjqkAc40bIkcYnw2dTJOGd8kT2TYpMHgAG9INrKRXFuEF6oijNjXYSrcFmReAtg0zVpLoCstcHXwh6V2rqTFD1sAZ57bbhx4TLjrokBUZc8CpH4QKDN77IFaOJchId0Y7247obyQ%2BwriwJIDtUoy0LDnoVQV4YGhhrjsCMl6kR%2Bexuw2%2FEz4bX0dF9M811oKpHbKAB2VvWQ7kXwy%2FHKcbConq%2FwwAYyD&X-Amz-Signature=2244f682fb0a4f695ecaf4f3b53a4b97aeef819cdd1f719f5560fd8dd2abbe9a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y7YXBDB%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDCDJp9WVnrDhXePt4qk1Wqmvq5nk4UpXnz5Nk81EGNQwIhALT8bqLIMeCH%2Fw0VWHdhiBT2B7jgdKe0CPRexjC0EZ5PKv8DCGkQABoMNjM3NDIzMTgzODA1IgxqDguNJlLQoFabhKYq3APRDoRjf2asfGXHjpeOrhJ0QKEnYLlo%2BEjDPVogew597D%2B59XOaiVvDFNVcWCRsKcp6kT2dloTMo9oa3jvqVFPlBQ4SMCs2rdKmAhInQYXKQ3%2Fb%2BowiT1lHsxiGi81ohc9EIwgEmX%2FaTK%2B4LHyj9%2BELLxaZnmqF09g1krGGKZPop4MGSQxpPqKPniVu9lr%2Bm8YcSMkqQjvTNzgfVkH1YA%2FD0kYviruMz0b%2Fk9xOmdMhFVFESU%2BOrasVwzpAh5bYanh3NC9Egau6wBu3zx7jl9qiw7gk4dPvI6eRtdMzq%2Bk4Ytr3Wfhb%2BHT4BOKUv1tFopK%2Bu%2BrNIponaLu49nkSzvUEagC2SqgI3bfkLB48LHl5RXmQ2gvBLIaHKUUOigtUOOY%2BxgNOaxMAp%2FE0McNMMAVBLjFCPQgNv579FopKIajyQCATCGWrccKXX9bMUzO8Jm%2F5MFhPMZyWH%2Fo328Pg89%2FZ1eJFycSJai0aSdNZc9nFsme%2BrAqEOQd1vEeD55Ba0JS2lhuJ32rBFPQ6KIZsCYXRXKWyJXdaLl8l6qZl54LszHvE0VqASHU0HrPWDsUHihgiSBDjB6NMXM9OPGUkeVQr4mYvPLnlCkwjTzFF6BsJTmjwNAnEN42%2BZAjK9DD6qbO%2BBjqkAc40bIkcYnw2dTJOGd8kT2TYpMHgAG9INrKRXFuEF6oijNjXYSrcFmReAtg0zVpLoCstcHXwh6V2rqTFD1sAZ57bbhx4TLjrokBUZc8CpH4QKDN77IFaOJchId0Y7247obyQ%2BwriwJIDtUoy0LDnoVQV4YGhhrjsCMl6kR%2Bexuw2%2FEz4bX0dF9M811oKpHbKAB2VvWQ7kXwy%2FHKcbConq%2FwwAYyD&X-Amz-Signature=9fe2618b0a63802a5e5048e3e54a02907aeb7872ffdbba3922975fa8c436020e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y7YXBDB%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDCDJp9WVnrDhXePt4qk1Wqmvq5nk4UpXnz5Nk81EGNQwIhALT8bqLIMeCH%2Fw0VWHdhiBT2B7jgdKe0CPRexjC0EZ5PKv8DCGkQABoMNjM3NDIzMTgzODA1IgxqDguNJlLQoFabhKYq3APRDoRjf2asfGXHjpeOrhJ0QKEnYLlo%2BEjDPVogew597D%2B59XOaiVvDFNVcWCRsKcp6kT2dloTMo9oa3jvqVFPlBQ4SMCs2rdKmAhInQYXKQ3%2Fb%2BowiT1lHsxiGi81ohc9EIwgEmX%2FaTK%2B4LHyj9%2BELLxaZnmqF09g1krGGKZPop4MGSQxpPqKPniVu9lr%2Bm8YcSMkqQjvTNzgfVkH1YA%2FD0kYviruMz0b%2Fk9xOmdMhFVFESU%2BOrasVwzpAh5bYanh3NC9Egau6wBu3zx7jl9qiw7gk4dPvI6eRtdMzq%2Bk4Ytr3Wfhb%2BHT4BOKUv1tFopK%2Bu%2BrNIponaLu49nkSzvUEagC2SqgI3bfkLB48LHl5RXmQ2gvBLIaHKUUOigtUOOY%2BxgNOaxMAp%2FE0McNMMAVBLjFCPQgNv579FopKIajyQCATCGWrccKXX9bMUzO8Jm%2F5MFhPMZyWH%2Fo328Pg89%2FZ1eJFycSJai0aSdNZc9nFsme%2BrAqEOQd1vEeD55Ba0JS2lhuJ32rBFPQ6KIZsCYXRXKWyJXdaLl8l6qZl54LszHvE0VqASHU0HrPWDsUHihgiSBDjB6NMXM9OPGUkeVQr4mYvPLnlCkwjTzFF6BsJTmjwNAnEN42%2BZAjK9DD6qbO%2BBjqkAc40bIkcYnw2dTJOGd8kT2TYpMHgAG9INrKRXFuEF6oijNjXYSrcFmReAtg0zVpLoCstcHXwh6V2rqTFD1sAZ57bbhx4TLjrokBUZc8CpH4QKDN77IFaOJchId0Y7247obyQ%2BwriwJIDtUoy0LDnoVQV4YGhhrjsCMl6kR%2Bexuw2%2FEz4bX0dF9M811oKpHbKAB2VvWQ7kXwy%2FHKcbConq%2FwwAYyD&X-Amz-Signature=ee7e9301ecb45d8cebb8c7f73c46b5b58a7a14d1a8d678edb0f14eea34356d57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y7YXBDB%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDCDJp9WVnrDhXePt4qk1Wqmvq5nk4UpXnz5Nk81EGNQwIhALT8bqLIMeCH%2Fw0VWHdhiBT2B7jgdKe0CPRexjC0EZ5PKv8DCGkQABoMNjM3NDIzMTgzODA1IgxqDguNJlLQoFabhKYq3APRDoRjf2asfGXHjpeOrhJ0QKEnYLlo%2BEjDPVogew597D%2B59XOaiVvDFNVcWCRsKcp6kT2dloTMo9oa3jvqVFPlBQ4SMCs2rdKmAhInQYXKQ3%2Fb%2BowiT1lHsxiGi81ohc9EIwgEmX%2FaTK%2B4LHyj9%2BELLxaZnmqF09g1krGGKZPop4MGSQxpPqKPniVu9lr%2Bm8YcSMkqQjvTNzgfVkH1YA%2FD0kYviruMz0b%2Fk9xOmdMhFVFESU%2BOrasVwzpAh5bYanh3NC9Egau6wBu3zx7jl9qiw7gk4dPvI6eRtdMzq%2Bk4Ytr3Wfhb%2BHT4BOKUv1tFopK%2Bu%2BrNIponaLu49nkSzvUEagC2SqgI3bfkLB48LHl5RXmQ2gvBLIaHKUUOigtUOOY%2BxgNOaxMAp%2FE0McNMMAVBLjFCPQgNv579FopKIajyQCATCGWrccKXX9bMUzO8Jm%2F5MFhPMZyWH%2Fo328Pg89%2FZ1eJFycSJai0aSdNZc9nFsme%2BrAqEOQd1vEeD55Ba0JS2lhuJ32rBFPQ6KIZsCYXRXKWyJXdaLl8l6qZl54LszHvE0VqASHU0HrPWDsUHihgiSBDjB6NMXM9OPGUkeVQr4mYvPLnlCkwjTzFF6BsJTmjwNAnEN42%2BZAjK9DD6qbO%2BBjqkAc40bIkcYnw2dTJOGd8kT2TYpMHgAG9INrKRXFuEF6oijNjXYSrcFmReAtg0zVpLoCstcHXwh6V2rqTFD1sAZ57bbhx4TLjrokBUZc8CpH4QKDN77IFaOJchId0Y7247obyQ%2BwriwJIDtUoy0LDnoVQV4YGhhrjsCMl6kR%2Bexuw2%2FEz4bX0dF9M811oKpHbKAB2VvWQ7kXwy%2FHKcbConq%2FwwAYyD&X-Amz-Signature=81839c3595a3caed21581b3588a4e7321a38880c707e561ba3e7c98b5366d205&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y7YXBDB%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDCDJp9WVnrDhXePt4qk1Wqmvq5nk4UpXnz5Nk81EGNQwIhALT8bqLIMeCH%2Fw0VWHdhiBT2B7jgdKe0CPRexjC0EZ5PKv8DCGkQABoMNjM3NDIzMTgzODA1IgxqDguNJlLQoFabhKYq3APRDoRjf2asfGXHjpeOrhJ0QKEnYLlo%2BEjDPVogew597D%2B59XOaiVvDFNVcWCRsKcp6kT2dloTMo9oa3jvqVFPlBQ4SMCs2rdKmAhInQYXKQ3%2Fb%2BowiT1lHsxiGi81ohc9EIwgEmX%2FaTK%2B4LHyj9%2BELLxaZnmqF09g1krGGKZPop4MGSQxpPqKPniVu9lr%2Bm8YcSMkqQjvTNzgfVkH1YA%2FD0kYviruMz0b%2Fk9xOmdMhFVFESU%2BOrasVwzpAh5bYanh3NC9Egau6wBu3zx7jl9qiw7gk4dPvI6eRtdMzq%2Bk4Ytr3Wfhb%2BHT4BOKUv1tFopK%2Bu%2BrNIponaLu49nkSzvUEagC2SqgI3bfkLB48LHl5RXmQ2gvBLIaHKUUOigtUOOY%2BxgNOaxMAp%2FE0McNMMAVBLjFCPQgNv579FopKIajyQCATCGWrccKXX9bMUzO8Jm%2F5MFhPMZyWH%2Fo328Pg89%2FZ1eJFycSJai0aSdNZc9nFsme%2BrAqEOQd1vEeD55Ba0JS2lhuJ32rBFPQ6KIZsCYXRXKWyJXdaLl8l6qZl54LszHvE0VqASHU0HrPWDsUHihgiSBDjB6NMXM9OPGUkeVQr4mYvPLnlCkwjTzFF6BsJTmjwNAnEN42%2BZAjK9DD6qbO%2BBjqkAc40bIkcYnw2dTJOGd8kT2TYpMHgAG9INrKRXFuEF6oijNjXYSrcFmReAtg0zVpLoCstcHXwh6V2rqTFD1sAZ57bbhx4TLjrokBUZc8CpH4QKDN77IFaOJchId0Y7247obyQ%2BwriwJIDtUoy0LDnoVQV4YGhhrjsCMl6kR%2Bexuw2%2FEz4bX0dF9M811oKpHbKAB2VvWQ7kXwy%2FHKcbConq%2FwwAYyD&X-Amz-Signature=c8441a5c66ef4adb85bc3619f32442120e7d6b7ecd908b6755d94b031ed8d314&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y7YXBDB%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDCDJp9WVnrDhXePt4qk1Wqmvq5nk4UpXnz5Nk81EGNQwIhALT8bqLIMeCH%2Fw0VWHdhiBT2B7jgdKe0CPRexjC0EZ5PKv8DCGkQABoMNjM3NDIzMTgzODA1IgxqDguNJlLQoFabhKYq3APRDoRjf2asfGXHjpeOrhJ0QKEnYLlo%2BEjDPVogew597D%2B59XOaiVvDFNVcWCRsKcp6kT2dloTMo9oa3jvqVFPlBQ4SMCs2rdKmAhInQYXKQ3%2Fb%2BowiT1lHsxiGi81ohc9EIwgEmX%2FaTK%2B4LHyj9%2BELLxaZnmqF09g1krGGKZPop4MGSQxpPqKPniVu9lr%2Bm8YcSMkqQjvTNzgfVkH1YA%2FD0kYviruMz0b%2Fk9xOmdMhFVFESU%2BOrasVwzpAh5bYanh3NC9Egau6wBu3zx7jl9qiw7gk4dPvI6eRtdMzq%2Bk4Ytr3Wfhb%2BHT4BOKUv1tFopK%2Bu%2BrNIponaLu49nkSzvUEagC2SqgI3bfkLB48LHl5RXmQ2gvBLIaHKUUOigtUOOY%2BxgNOaxMAp%2FE0McNMMAVBLjFCPQgNv579FopKIajyQCATCGWrccKXX9bMUzO8Jm%2F5MFhPMZyWH%2Fo328Pg89%2FZ1eJFycSJai0aSdNZc9nFsme%2BrAqEOQd1vEeD55Ba0JS2lhuJ32rBFPQ6KIZsCYXRXKWyJXdaLl8l6qZl54LszHvE0VqASHU0HrPWDsUHihgiSBDjB6NMXM9OPGUkeVQr4mYvPLnlCkwjTzFF6BsJTmjwNAnEN42%2BZAjK9DD6qbO%2BBjqkAc40bIkcYnw2dTJOGd8kT2TYpMHgAG9INrKRXFuEF6oijNjXYSrcFmReAtg0zVpLoCstcHXwh6V2rqTFD1sAZ57bbhx4TLjrokBUZc8CpH4QKDN77IFaOJchId0Y7247obyQ%2BwriwJIDtUoy0LDnoVQV4YGhhrjsCMl6kR%2Bexuw2%2FEz4bX0dF9M811oKpHbKAB2VvWQ7kXwy%2FHKcbConq%2FwwAYyD&X-Amz-Signature=a43909af17adb0e8c953dc02fac789d22f2f3c976cc87ec27d229fc6f848e955&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWQZXBD%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC5x%2Bn3oHW8NL9BY3E75JoTCOvR9iAZLgcleVkHpBW6FgIhAIv848N47BMWm3QYjSpOGLvakrvsY0Q5iuNlUuzJc1bIKv8DCGkQABoMNjM3NDIzMTgzODA1IgzQSv4gijXSOExUY9Mq3AP6QX14lUQRH0fCMTBZ9X1bDynHprlQhv7FHe9Z26Al0pQV2Ssea1UJdPchRtG650ZlH36l0YgOk0S%2BkZkXVcrOvZldAkqMDDfe%2Bi9r1JP8zIQTxwHvdM4vkSBF3yI%2BgHig6J%2Fc%2Blw8oBnr8d5gKXEjLUEXn%2BKgsenQSwLx35PrwwUQOBG2JP1%2FPb7W2MQ0nGUHN8qr4%2Fpv27Dtknhd%2FSHjxWnhyRFKyzJl8x3%2BaHtvgXJEQY5czRfOsI04p%2Bzv7bpc4V7dqqGmMIgtFBzs71Ro2ufUR2s8BimPhLToINx0hQKqcFkJNFNPbE0pVFTCKOuQASnPh4ECxiqpmGJXPVWXjmjxtYP1%2B8b42ZqFx5KYE2fhjyysD40udRMs2%2BlKl5Q8WI%2FVvNKrFhCGpSREYQdwM%2FSi3A8DIWC9KpVFUvMYpGLR2ruz0IHXp%2BIzect5mUCpwSA6KUKLXfc93AUIEc32cPi3amcbCAksbOGkR%2FXRTVnKNQj%2BqMb4DIy5cfDmUYhNKHuLCgGCV9P8l0yacRMvTKdApt%2FRjWmpUpWPeCliDikWjJ%2FPTSx95KvPNTMb70%2Bei98YzZ2sDqNOIRFDkOqb6EhkqAq2KaACRfXZhgIP%2FXfnvxnw6FhHmcrTIjDvqbO%2BBjqkAW2cDLuVN3hPSvAPM68Ca%2FuzVD5TmvRUTPtfXIN8WjQkIIqsejuboexmviC2vjpHr9QY8SGpPgXgu39ww88MqD5ZSTtvBfDCzTSzsIpoqLVVfvcW3hQTDMBv30z%2FrF92%2Fbrg9prebCpFT80JoX5jQuQNPX80qCu%2F%2Fc7FXl9puS7W4i8FdcIxX%2Bc%2By1QT%2Fe%2FupAZbNE7ob2NcFht%2FaOwVxbR5IEvV&X-Amz-Signature=4d98d0d01301d9e61c11b18dd834e10852bbeddfeeb9bc89e0b4206230fa981c&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVKWZ5U5%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCjgbdnesx6lsSUC6A2CRgJQrFp2aEUWtkPtOD8jjgm1AIgHm3JWKbbR%2Br7GGhjj5mGDyZIvX%2FXiYuFZhsNebLsSXEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDNuAwHVSn9PUlC%2F8%2FSrcA88W%2BSLoAd9EIeNbnBiqeXHfVynv%2Fj9ARvlxx%2FjusoacHgwHHwGHd8OcmmkWYnzKFmnt84A%2Bzb5lp8DFxZhbQ3M9uBqB380LGw8SDhkLgrSvraRte9ytqzV%2Bjt5nzrl0QHboJlXzJMkbgrxtTkUSKiQp4pnL9MTsq0hCOh7U%2BSAeSE6X0WlZZnY5SqoAaGsVfosSCM9w7i4o%2B2d7JWUvrf8sAEkmjIFUvFypG2xcbBm7h3dmf8gAPOEcsLrSqQSnhRNPYh%2FnLh06NymaTXDS3tFhHCDt3Y7cX%2B2Pxv7CS13Y3xOlf5CZ69t72zkvP46Qs6JR94VSxDhlFKkAqmxlllbhPFgs0AsyjqPZ%2Fu6WiDAiZkkcde4PzimOrhW9ZAkK8NGNTsM24GpVvubJNtzldLlhvbGZZ%2BYrStKCg%2F2GG7QDm2fBp6Kcb76zBqYiCp40Sxh1ZuapfbrWuqXxaVjs%2BjKvT6zDKIROm%2F0Aagcx1%2B1Y%2FzmjEZ5TerXULVjxq3MGP6yD0CWtofLXrqZaxA3xabf6EXCQBxy3QcOJqZcva2jgb89yY5ZmSuj6j00FjFINeU93ACU3GBE4DP9IlyJ6qRJx%2FT9mCtbTXDzUNP48U6gtBU9Zff%2Fgd2xVPyRHMJyqs74GOqUBcMEZN5wIplqHjskVvvs0UixU%2Bop3%2FMNpvjGLmM8R%2B%2FexG8HFPe%2Br6PFXMaetSth996tcy87Ny5fRTJC6VGVMaquZTIn2weQsl4KAUpot60uq2keaLv0GC%2BQh1xVQDziCbIa8AHSMR62gHxaIAC87dJtDe%2FcAgHSjHmfU%2BT6kbUD1XVTtaCxxAdH8vnSdnGTVRt1fy%2FoXzxyO3p41W0aftLkJlTzi&X-Amz-Signature=757bd9f1954e052faa6071a179bd8a8ad21b0603f518c2aa499ebab02f1a51ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y7YXBDB%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDCDJp9WVnrDhXePt4qk1Wqmvq5nk4UpXnz5Nk81EGNQwIhALT8bqLIMeCH%2Fw0VWHdhiBT2B7jgdKe0CPRexjC0EZ5PKv8DCGkQABoMNjM3NDIzMTgzODA1IgxqDguNJlLQoFabhKYq3APRDoRjf2asfGXHjpeOrhJ0QKEnYLlo%2BEjDPVogew597D%2B59XOaiVvDFNVcWCRsKcp6kT2dloTMo9oa3jvqVFPlBQ4SMCs2rdKmAhInQYXKQ3%2Fb%2BowiT1lHsxiGi81ohc9EIwgEmX%2FaTK%2B4LHyj9%2BELLxaZnmqF09g1krGGKZPop4MGSQxpPqKPniVu9lr%2Bm8YcSMkqQjvTNzgfVkH1YA%2FD0kYviruMz0b%2Fk9xOmdMhFVFESU%2BOrasVwzpAh5bYanh3NC9Egau6wBu3zx7jl9qiw7gk4dPvI6eRtdMzq%2Bk4Ytr3Wfhb%2BHT4BOKUv1tFopK%2Bu%2BrNIponaLu49nkSzvUEagC2SqgI3bfkLB48LHl5RXmQ2gvBLIaHKUUOigtUOOY%2BxgNOaxMAp%2FE0McNMMAVBLjFCPQgNv579FopKIajyQCATCGWrccKXX9bMUzO8Jm%2F5MFhPMZyWH%2Fo328Pg89%2FZ1eJFycSJai0aSdNZc9nFsme%2BrAqEOQd1vEeD55Ba0JS2lhuJ32rBFPQ6KIZsCYXRXKWyJXdaLl8l6qZl54LszHvE0VqASHU0HrPWDsUHihgiSBDjB6NMXM9OPGUkeVQr4mYvPLnlCkwjTzFF6BsJTmjwNAnEN42%2BZAjK9DD6qbO%2BBjqkAc40bIkcYnw2dTJOGd8kT2TYpMHgAG9INrKRXFuEF6oijNjXYSrcFmReAtg0zVpLoCstcHXwh6V2rqTFD1sAZ57bbhx4TLjrokBUZc8CpH4QKDN77IFaOJchId0Y7247obyQ%2BwriwJIDtUoy0LDnoVQV4YGhhrjsCMl6kR%2Bexuw2%2FEz4bX0dF9M811oKpHbKAB2VvWQ7kXwy%2FHKcbConq%2FwwAYyD&X-Amz-Signature=da691949adf45eac1cdb0ca3773b242011022998f257d9c3414e2e66c99f49c6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y7YXBDB%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDCDJp9WVnrDhXePt4qk1Wqmvq5nk4UpXnz5Nk81EGNQwIhALT8bqLIMeCH%2Fw0VWHdhiBT2B7jgdKe0CPRexjC0EZ5PKv8DCGkQABoMNjM3NDIzMTgzODA1IgxqDguNJlLQoFabhKYq3APRDoRjf2asfGXHjpeOrhJ0QKEnYLlo%2BEjDPVogew597D%2B59XOaiVvDFNVcWCRsKcp6kT2dloTMo9oa3jvqVFPlBQ4SMCs2rdKmAhInQYXKQ3%2Fb%2BowiT1lHsxiGi81ohc9EIwgEmX%2FaTK%2B4LHyj9%2BELLxaZnmqF09g1krGGKZPop4MGSQxpPqKPniVu9lr%2Bm8YcSMkqQjvTNzgfVkH1YA%2FD0kYviruMz0b%2Fk9xOmdMhFVFESU%2BOrasVwzpAh5bYanh3NC9Egau6wBu3zx7jl9qiw7gk4dPvI6eRtdMzq%2Bk4Ytr3Wfhb%2BHT4BOKUv1tFopK%2Bu%2BrNIponaLu49nkSzvUEagC2SqgI3bfkLB48LHl5RXmQ2gvBLIaHKUUOigtUOOY%2BxgNOaxMAp%2FE0McNMMAVBLjFCPQgNv579FopKIajyQCATCGWrccKXX9bMUzO8Jm%2F5MFhPMZyWH%2Fo328Pg89%2FZ1eJFycSJai0aSdNZc9nFsme%2BrAqEOQd1vEeD55Ba0JS2lhuJ32rBFPQ6KIZsCYXRXKWyJXdaLl8l6qZl54LszHvE0VqASHU0HrPWDsUHihgiSBDjB6NMXM9OPGUkeVQr4mYvPLnlCkwjTzFF6BsJTmjwNAnEN42%2BZAjK9DD6qbO%2BBjqkAc40bIkcYnw2dTJOGd8kT2TYpMHgAG9INrKRXFuEF6oijNjXYSrcFmReAtg0zVpLoCstcHXwh6V2rqTFD1sAZ57bbhx4TLjrokBUZc8CpH4QKDN77IFaOJchId0Y7247obyQ%2BwriwJIDtUoy0LDnoVQV4YGhhrjsCMl6kR%2Bexuw2%2FEz4bX0dF9M811oKpHbKAB2VvWQ7kXwy%2FHKcbConq%2FwwAYyD&X-Amz-Signature=b986efb3d57e69dbabb5a18aa09286c97f4549688e3d5b5c1ef0a008501e7619&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y7YXBDB%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDCDJp9WVnrDhXePt4qk1Wqmvq5nk4UpXnz5Nk81EGNQwIhALT8bqLIMeCH%2Fw0VWHdhiBT2B7jgdKe0CPRexjC0EZ5PKv8DCGkQABoMNjM3NDIzMTgzODA1IgxqDguNJlLQoFabhKYq3APRDoRjf2asfGXHjpeOrhJ0QKEnYLlo%2BEjDPVogew597D%2B59XOaiVvDFNVcWCRsKcp6kT2dloTMo9oa3jvqVFPlBQ4SMCs2rdKmAhInQYXKQ3%2Fb%2BowiT1lHsxiGi81ohc9EIwgEmX%2FaTK%2B4LHyj9%2BELLxaZnmqF09g1krGGKZPop4MGSQxpPqKPniVu9lr%2Bm8YcSMkqQjvTNzgfVkH1YA%2FD0kYviruMz0b%2Fk9xOmdMhFVFESU%2BOrasVwzpAh5bYanh3NC9Egau6wBu3zx7jl9qiw7gk4dPvI6eRtdMzq%2Bk4Ytr3Wfhb%2BHT4BOKUv1tFopK%2Bu%2BrNIponaLu49nkSzvUEagC2SqgI3bfkLB48LHl5RXmQ2gvBLIaHKUUOigtUOOY%2BxgNOaxMAp%2FE0McNMMAVBLjFCPQgNv579FopKIajyQCATCGWrccKXX9bMUzO8Jm%2F5MFhPMZyWH%2Fo328Pg89%2FZ1eJFycSJai0aSdNZc9nFsme%2BrAqEOQd1vEeD55Ba0JS2lhuJ32rBFPQ6KIZsCYXRXKWyJXdaLl8l6qZl54LszHvE0VqASHU0HrPWDsUHihgiSBDjB6NMXM9OPGUkeVQr4mYvPLnlCkwjTzFF6BsJTmjwNAnEN42%2BZAjK9DD6qbO%2BBjqkAc40bIkcYnw2dTJOGd8kT2TYpMHgAG9INrKRXFuEF6oijNjXYSrcFmReAtg0zVpLoCstcHXwh6V2rqTFD1sAZ57bbhx4TLjrokBUZc8CpH4QKDN77IFaOJchId0Y7247obyQ%2BwriwJIDtUoy0LDnoVQV4YGhhrjsCMl6kR%2Bexuw2%2FEz4bX0dF9M811oKpHbKAB2VvWQ7kXwy%2FHKcbConq%2FwwAYyD&X-Amz-Signature=e363c3fde8cf581b22cdf6828b948800df483e8a9498a97509f29f5e88ccddaa&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ3TC4MG%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCKsMlcSeR7S3KQ7RkYIWYv1lZa2BvLuSHkJh%2FCnnQEAwIhAMk45loeFCS7B3%2Fv8cH9A5TC4WZaVx6Co%2Fy9j8InGsJfKv8DCGkQABoMNjM3NDIzMTgzODA1IgwQIJfNzm8aNvdaQIQq3APtg6oNxxnX1Cpus4OZqEQ1t00OHvJRo91JP5Jt%2FaAoDP743FdROMngT%2Fu06u015I2yiMKlFIylD7hreNY4bPH%2BGWotYtQXUJS1cF%2B852mMaL60dSrT%2FeUKW17%2FRjlx4WOVoigH4Q%2Fod05mDijxDDizPy6tJ7qAAXudkefVwdk1mwVaAfL%2Bfr3PiogVkFfAxWGypq%2BOvhKBXOusfjh0ANXCMRpxE0qNm5zbx1f7m6mzyJzdRoZ8rYAO7GCXHWrhzPIatVtdqGpwRL9wXelcyHpHFGAuaUXaW0Ye6V8UN9%2BG%2BIM8cbPED58ZdVQyQHVrT0NOinAjr0z%2FNyw18KvO40ajIOkAJ0a7s8j7%2BvHDKkw0qrzOPd4bkn%2F9cLkJ8EWNmVtrDPe2EAOvY4PJWh0rUIP3VYUtjdOEazmyi2J9aM%2Btj9dscmh%2F%2Bgj9SKGB0YulcoUqUcB7CdpgjQu2vDCHIgFN%2FkZowZ6KrF278nwt83rCgS4spcWt%2Bz5Uu6R5S%2BGReExFOKNuXPat%2F2rBGdPqojoSaI%2FSukLZ2LgrgQFIC2A56d2SVNlNNm1umKtxNXVIMWCJ6J7pManCkrdA5Q%2BgypEeFDRl%2FQsYTnDlTeQ1T4Ijds3fMd8BouC%2FAH887DDrqbO%2BBjqkAcNt8mQmxgIsFSVNOZAAsZ%2BAScTM0sLYV4PrQAY023hvFPrni9yEIKZCaBnE4wn8zoqqjnPz0ewVtpbKaL5mfpheuxBm0Fe8dQ%2BzIJHc60O5lQAN%2Fssv2zKFdvgP1qqMJippX%2BFvq%2BBaiNQIcO7XKQ5UA8WVgtPnaE%2FISCAOPcPulOC47nHg1lQRwAMS3h97r8YMk4jpNvjfdkDAfivZ%2FUpVEk4k&X-Amz-Signature=1ad0c8c713bc61376b0821a156ddc5ed0e4806d9ca2532df91f5bfb222b884ac&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDQFJMM3%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGN6mfZyu6o37cCeAEgQuO%2F1W1U5cRMvVlTTrkPsQ%2FimAiEAmolcZUnGH5%2BIEbcwovXuqSP9ANlmomWnBwUr%2FetOf5sq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDHKMvvP%2B5SEOz3vXoCrcAwnWHsZABgYRsxgLUhcaIYoNeC7Xg%2BK6s4NAkHHrETvesFHYaVJ4m6vcTRbBtTFDPTvYg4hnaMmHpq5ZzOp359TqCYbTChuCSJ63YbTr4%2F5a4VL3gZCxbtOyH9kGRMX8HJohvnylF1giVBQRRD65bDP3oO4POaIn%2Fw7wb6RPZOwSAiDqYB6fc%2FIZWv%2FamjqmJRR340%2FZc99kaITZQixuTO%2B%2ByImoqMqnen7NtdEplU7NpMmmBj9xtT1zI8ZxfqsBKMGvFZBk0sGF3Vh16LTb96j%2B5RFqolOv79dY0XD%2BDoi5XhXBzSXntqq%2BtxCA8zop4pn9p2deZ7Nm2FpfyKEdIRNi4uk6kPEeRbYOanQKxQbClgE18NGYKz6xC%2FF16VMWvPk3m3kp08n010bV3qm%2FJN9eacnH2nxXK%2BbL2845NPS7Dn5IlDwe%2BEDMBz4YXp5cUPG19VUY0QfwCIRcxtJwk5kqDHcmelBJl97MkwCI3ir4EKv3P60gJmlIhTs2SsfQGR96rrhtpr%2FYMGyGWerb%2BQlXcg%2B1vwjgCoJXlYBcGa%2FEibOlwEWHE1rmwzg8fIxz0P0JTFjz2wkJtigq%2BQUlI2YYe2YROdi5%2B5zVK45Jhxv1X24F%2F502pt0E5nVBMM%2Bps74GOqUBSnnh83m%2F89sWm4KMS5zVnfKgcDcr25FIgco7G%2FZWGxKoCSgc49XKndd0977hvfDhnkV7eMCtp%2BOM8%2F8Jkv5upzLvrdu%2BmVn%2FIcZ14vVU6AgPyjN5E0ozi4vUSGQD3xrWkBcWZYXsMQHGVrSOt2rcvusjLu%2BN5EmXJbmIywz4HVrkwk2K46XlMYxRJHzC86ISXLtdV2IlknQrZtv4hyJ3FfJgJoCj&X-Amz-Signature=38f0da849331c17a4d53d0c8ae23b9bef41519d65fb4adff78d2a7a4a4974a21&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY7SJUTI%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDFGkN%2FjwPHLXfGxm6RmQO2z%2BVoNnYjDqjKUNT%2B%2BrdTxwIgZno95Fq0Fvdx5aXcRaF59iWDN4UtPdpxkJrF3%2B1ttiQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDIlKjnFRFEpZa912zSrcA%2BFiAN0olGF0fTpBxNEchbVheOsDXV201rXQQbYa2gI2er%2FFOdBJMjoGLpu186chCkY9C2nfqRatVCuDEoLcDezrg1YnoOuXBGbK%2FGXQTpd5B6yeOyBiC0quIkGZMlnmRY1CXCqsUX6sSVIWu4t2BjaezdVWkLZN9gzsjL7SyPra1tCIFwUkZ%2FfimDdFmVs5NEvQqxJSeT5GBPXQi5lQHp3SbAjrACEIdP%2FaDj5HaMLqNU20YBxMT1l8c5%2BiWo1JpZ4jP3AVqbB63OhTaxNVex7WC25oYceyhBLoPMtKDt6hFZnoyBePPPt%2BhMp%2FNL2v0Ng6%2FR8JSoKlf8o5eSqkY3%2FzGrpCTv4Oo%2F57Td4Gg6lwvZQBK1imhhikA5e007vSogZd8KjYuxMAPBJ%2FflZZqGG8tIdGvNbnaxWRwLVBuEXy0MH0XADHoT1niO%2FKCbzJQQCq05uK30BrbenJVDTqK2a142YjI1sBRqe52dei94efhjRWo0kF3cWmcSC4kXXmRhRespXaKHBtG2u0bQO0S%2FSUg8CWfFXMI%2F7z6g7sFW4%2FC6rHF9%2BAw9GwdcBgRttlHVUwV8wuM3cEOA6C4xe2NPJqCFWMQ%2Fsyvd6zXBdoH%2BFcBH7h5FES6Qf3OJ2sMMyps74GOqUBgufJhyUbhby2RCiI670Ap8r6qlsihw3xzvBA%2BYW5QG7tr0wHv1TMuIKKdJYqg0rRkz9ov8gYGa51tBUSnKsOUgJL9tsTt0gY8zYeDTp%2BXc0YhGz1fLJCTOQKwXIPtreQ%2FeT67cVDszHPsvAq5kUkdSY7gZVcVLr8s70mCTDiSerBlmEkTLK5gojuSILHufHWJiLi0sjrq%2BTRHykeT2uxtid%2BytKO&X-Amz-Signature=7f25163b3d0abb99b7a5e0159f2f2e20114580f2361abf2a8fc8cb15f23ab357&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEBNKBER%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9KUsAwiCCOj1OsFi%2FYZJ1LDm8ySuziNUnN6X6ptRrtgIhAJgiu88MZxyqInu4nA%2BGrjUdlxLKYJfpvmeTinZ9KgwlKv8DCGkQABoMNjM3NDIzMTgzODA1Igw4SbkKpozdBtvIyeAq3AMXLdOd5sBUHUhbJOuozWhZ17frZqBA%2FmxJgy90mIogmtgprVc45VnbXydIm7naWjEKQqi0lBkI9TPiHb5jz9imZ24nRRLaJalq7%2Bm5zxTevVrIaCnYELZy4GvPixkNdL8FrA1lYwbTPnisG4MadW%2Ff%2B2DSKpXFS1gPUGlvZwpid4I43b26Hbx0M1SZZOWvKHGjC5pcIOrlXasVhCWbR1DVeYyECnJ68sUl7wl1Z6g135Q49XSQPRm%2FbPkLAflbjtXQJw1qE3orQZHzAzzTaHPWjpDG7J7K%2BV9pJoePBBgwCsrWBSEsaUZT3WEN2ScgkPuBVBDejSQbwxPjFuNDnZHo53%2FUcMYFJTWMPRHl6zYnvcppv1b1Yau30QxlIODdH8sFmiHfH1Sj%2FyQNyJWObssjt0ifS206jmbHB0pZK3cL4vAVZObocTv%2FIiWJZ8fcQOrWRKyIO85CPRidpxCbSkOrVIBZvDd07KcEhrJDVid26R%2F8CTygdVjFo0XSzW261akgz3WPlc77oLZROMZQCFjSzSrFD3mFgQAf3CnqQyJzThqReOvalY0JOQPIZeYor9zPAAWr7LU03FIqb69V4ZgQvGzrQ5tto57NspA%2FjhytIXjkdj64KKw49NOKajC7qbO%2BBjqkAUPfPqAgF1%2FPe3pqmcSLuZsxZhBMMdXlOyUv0o3WlDxw41q6cNofZ%2FOiCKn3%2FTh4Z33%2FI1NZlBVHK0cBg0qKNUUZmhir%2FvLnrAAqveWj0TvACoDgnEXh3M9y3GQRj5vo6MamXlU5wRm%2Bzt8KebHwO7q0baLQAgX4yXc4MEs5Dnp9pRJKyv%2BysUWAYfFGlwAdtZyzASiRYTb6DsCRh8lDrJ6730Wt&X-Amz-Signature=688e1665fc6ba55a7d6c1d6e24e0ba94babe4dd422224771b103283565d79dae&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEBNKBER%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC9KUsAwiCCOj1OsFi%2FYZJ1LDm8ySuziNUnN6X6ptRrtgIhAJgiu88MZxyqInu4nA%2BGrjUdlxLKYJfpvmeTinZ9KgwlKv8DCGkQABoMNjM3NDIzMTgzODA1Igw4SbkKpozdBtvIyeAq3AMXLdOd5sBUHUhbJOuozWhZ17frZqBA%2FmxJgy90mIogmtgprVc45VnbXydIm7naWjEKQqi0lBkI9TPiHb5jz9imZ24nRRLaJalq7%2Bm5zxTevVrIaCnYELZy4GvPixkNdL8FrA1lYwbTPnisG4MadW%2Ff%2B2DSKpXFS1gPUGlvZwpid4I43b26Hbx0M1SZZOWvKHGjC5pcIOrlXasVhCWbR1DVeYyECnJ68sUl7wl1Z6g135Q49XSQPRm%2FbPkLAflbjtXQJw1qE3orQZHzAzzTaHPWjpDG7J7K%2BV9pJoePBBgwCsrWBSEsaUZT3WEN2ScgkPuBVBDejSQbwxPjFuNDnZHo53%2FUcMYFJTWMPRHl6zYnvcppv1b1Yau30QxlIODdH8sFmiHfH1Sj%2FyQNyJWObssjt0ifS206jmbHB0pZK3cL4vAVZObocTv%2FIiWJZ8fcQOrWRKyIO85CPRidpxCbSkOrVIBZvDd07KcEhrJDVid26R%2F8CTygdVjFo0XSzW261akgz3WPlc77oLZROMZQCFjSzSrFD3mFgQAf3CnqQyJzThqReOvalY0JOQPIZeYor9zPAAWr7LU03FIqb69V4ZgQvGzrQ5tto57NspA%2FjhytIXjkdj64KKw49NOKajC7qbO%2BBjqkAUPfPqAgF1%2FPe3pqmcSLuZsxZhBMMdXlOyUv0o3WlDxw41q6cNofZ%2FOiCKn3%2FTh4Z33%2FI1NZlBVHK0cBg0qKNUUZmhir%2FvLnrAAqveWj0TvACoDgnEXh3M9y3GQRj5vo6MamXlU5wRm%2Bzt8KebHwO7q0baLQAgX4yXc4MEs5Dnp9pRJKyv%2BysUWAYfFGlwAdtZyzASiRYTb6DsCRh8lDrJ6730Wt&X-Amz-Signature=850da494963116ebd5273c09e675d45a978b98000c430d829c26d05616bad2d3&X-Amz-SignedHeaders=host&x-id=GetObject)

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
