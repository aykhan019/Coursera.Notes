

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUMUKO4X%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCID725t5JlTNKlb6YHBYVvvpxYPI9Cy84%2BWrgOaXMRJO2AiEAwcJQhbikjhYVyqzz9eULCArD%2BngO9DoKFwvVSvpVvT0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAZaBxlm%2BgVTEixzKyrcAxXsohpBo2gs9LYRq%2F2Gl7yMTyi2BFg0APnKIEOXe1I3XHoatYCVI4F9L2Ag7Qhw7LfHm3ObBU6qqHWzsfXqo%2BzrItEKDonwNhHYwYrneRO%2BqVjMlibSlnW5Z3GaKvdoyXQ73gvWE2Y5OsGihAi7firX5fyX1zgdHkhMF1dY7AAjNyoHhl5ciLrmbTrwsh7ukpgAbOPptyUMBaIZDJDjws9U%2BXXiJAngztJtaUiZt0aO28kcf37m8DO0XgmoqZwvg8aVos6rcJSYHCEF4kODQFmJ1qb26ILud1zoQAkLo9dze%2F%2FgJpVFYGiRdzkRlx%2BzcpG%2BhfUW09NUmfTRHBpYa1ylSAl6bUYifUg3C2LiBjTH%2B%2BXBZJ1ryb%2FWmhqEfreInhxRHXl6viXqC2ODp%2BXOl9G6jbmXkRg9yT%2BqqCoZQMGacz5KimDi8sE7ASXO6Y3kDB0pSX1g0fByfoEBZtlRwaLZ6tjYrvgydz7hHh8cgLXMcqpyDMy%2Bvl%2BJMWEashOk6BP7UEkPLuxEug6BdkHjY6uCeR0%2FkgYOjUwsVEtbl%2FXbXx6lAIM4fAi25Eqxbi37P44xFIM%2Bk0aUwHj8NOGtzeUYG4VN4XPljjNgbfRU28i2GIq30LplZpY3LqU2MIvNir0GOqUBr%2BaibQLk5scEJ2Jyn1NVQJlu%2B2QBot7eJAI425y7ShDe8p606V2kYLeBibFs8vgA07N3hgbzxaPQ05oYM54FUOmraReCNsorNCyHe3E2QdPWruSxSgh4VrbDAGA%2BHCe5kSN6f66%2FhbP84HmgWBwx3V8R6shA1DaTf1fLFtDvGS%2FDGzdJer3Ivyv5uEzl5ojKA3U7kYnWLYmyMr3GNqjYmjtOQBC3&X-Amz-Signature=ff17c013ec188d5bf8e220c0094bcdaa5507e39201afaf782960ea5f89087d47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUMUKO4X%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCID725t5JlTNKlb6YHBYVvvpxYPI9Cy84%2BWrgOaXMRJO2AiEAwcJQhbikjhYVyqzz9eULCArD%2BngO9DoKFwvVSvpVvT0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAZaBxlm%2BgVTEixzKyrcAxXsohpBo2gs9LYRq%2F2Gl7yMTyi2BFg0APnKIEOXe1I3XHoatYCVI4F9L2Ag7Qhw7LfHm3ObBU6qqHWzsfXqo%2BzrItEKDonwNhHYwYrneRO%2BqVjMlibSlnW5Z3GaKvdoyXQ73gvWE2Y5OsGihAi7firX5fyX1zgdHkhMF1dY7AAjNyoHhl5ciLrmbTrwsh7ukpgAbOPptyUMBaIZDJDjws9U%2BXXiJAngztJtaUiZt0aO28kcf37m8DO0XgmoqZwvg8aVos6rcJSYHCEF4kODQFmJ1qb26ILud1zoQAkLo9dze%2F%2FgJpVFYGiRdzkRlx%2BzcpG%2BhfUW09NUmfTRHBpYa1ylSAl6bUYifUg3C2LiBjTH%2B%2BXBZJ1ryb%2FWmhqEfreInhxRHXl6viXqC2ODp%2BXOl9G6jbmXkRg9yT%2BqqCoZQMGacz5KimDi8sE7ASXO6Y3kDB0pSX1g0fByfoEBZtlRwaLZ6tjYrvgydz7hHh8cgLXMcqpyDMy%2Bvl%2BJMWEashOk6BP7UEkPLuxEug6BdkHjY6uCeR0%2FkgYOjUwsVEtbl%2FXbXx6lAIM4fAi25Eqxbi37P44xFIM%2Bk0aUwHj8NOGtzeUYG4VN4XPljjNgbfRU28i2GIq30LplZpY3LqU2MIvNir0GOqUBr%2BaibQLk5scEJ2Jyn1NVQJlu%2B2QBot7eJAI425y7ShDe8p606V2kYLeBibFs8vgA07N3hgbzxaPQ05oYM54FUOmraReCNsorNCyHe3E2QdPWruSxSgh4VrbDAGA%2BHCe5kSN6f66%2FhbP84HmgWBwx3V8R6shA1DaTf1fLFtDvGS%2FDGzdJer3Ivyv5uEzl5ojKA3U7kYnWLYmyMr3GNqjYmjtOQBC3&X-Amz-Signature=686f52ecf49899903682efa6fcdc274b43d22cf9f4c199d226a60da852fed992&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUMUKO4X%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCID725t5JlTNKlb6YHBYVvvpxYPI9Cy84%2BWrgOaXMRJO2AiEAwcJQhbikjhYVyqzz9eULCArD%2BngO9DoKFwvVSvpVvT0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAZaBxlm%2BgVTEixzKyrcAxXsohpBo2gs9LYRq%2F2Gl7yMTyi2BFg0APnKIEOXe1I3XHoatYCVI4F9L2Ag7Qhw7LfHm3ObBU6qqHWzsfXqo%2BzrItEKDonwNhHYwYrneRO%2BqVjMlibSlnW5Z3GaKvdoyXQ73gvWE2Y5OsGihAi7firX5fyX1zgdHkhMF1dY7AAjNyoHhl5ciLrmbTrwsh7ukpgAbOPptyUMBaIZDJDjws9U%2BXXiJAngztJtaUiZt0aO28kcf37m8DO0XgmoqZwvg8aVos6rcJSYHCEF4kODQFmJ1qb26ILud1zoQAkLo9dze%2F%2FgJpVFYGiRdzkRlx%2BzcpG%2BhfUW09NUmfTRHBpYa1ylSAl6bUYifUg3C2LiBjTH%2B%2BXBZJ1ryb%2FWmhqEfreInhxRHXl6viXqC2ODp%2BXOl9G6jbmXkRg9yT%2BqqCoZQMGacz5KimDi8sE7ASXO6Y3kDB0pSX1g0fByfoEBZtlRwaLZ6tjYrvgydz7hHh8cgLXMcqpyDMy%2Bvl%2BJMWEashOk6BP7UEkPLuxEug6BdkHjY6uCeR0%2FkgYOjUwsVEtbl%2FXbXx6lAIM4fAi25Eqxbi37P44xFIM%2Bk0aUwHj8NOGtzeUYG4VN4XPljjNgbfRU28i2GIq30LplZpY3LqU2MIvNir0GOqUBr%2BaibQLk5scEJ2Jyn1NVQJlu%2B2QBot7eJAI425y7ShDe8p606V2kYLeBibFs8vgA07N3hgbzxaPQ05oYM54FUOmraReCNsorNCyHe3E2QdPWruSxSgh4VrbDAGA%2BHCe5kSN6f66%2FhbP84HmgWBwx3V8R6shA1DaTf1fLFtDvGS%2FDGzdJer3Ivyv5uEzl5ojKA3U7kYnWLYmyMr3GNqjYmjtOQBC3&X-Amz-Signature=ff0ab7305b705495061eca9cefa3a1b94684b3f1ee0e99a6fd7844e90b3cce08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TC2ZOGK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCnESdNHzFmzYrPqA4J28r33rzG6f%2FL3WWzKBIMdoTuRwIhAL210KD%2FlBW1Qt2zFnl2RYy763id01fcjURHvGwP1T8tKv8DCDkQABoMNjM3NDIzMTgzODA1IgxIzVA5E1pELgg1Z2Yq3AMlDkPL6CAFD9avdihL2Jd0a1mxPmBV4J5iBgezmQiHEzqbdasVUn758p5%2Bpxx2rD2kvfT%2BpGVfU5IPNj3yRQTGxW6NSPOknvEmgOvHo6XEoT79JVXAfJqh%2FXzbrMg9S5oxEdgQg1MOMvcouyBI3iC0DjbE3xzhS17Lr7t1fr%2B%2BKmz4LfNm24R%2BMil8jDBFy%2B1hmF5n%2BXrAFgqey9HmLg16%2BBdQMuHfIL3nUS81reLMoDvElFg8Pb4Iy5HJCJBdZ%2F%2FdVf6LlWVq97S%2BpVaooA7MQsTB66CXPz7GKTj5XtXskZsedC%2Bexa0Bn2cfRVIbHompukXjhCeZ30A4vC7LUNpweOu3591i%2Fa1wdDtlY%2BPMQH30Rl%2BaDysCq%2FaxnVLhyyJ28moSEcf7ZeMlTYEsmpb44GQReQhTgn5gnXQ5Nc6x2jWJHSW0esfsS4aUvQRqWuNM2iucbjxQMQOgxQH3oUINocPx288k6Q%2Flx%2BaAmgjiqB9NbODHe7yk41UGcQicq8vLyO1ZF%2BbpSSnbHV9Lj2jxfbhc4AW59ya6bEzcKdgQ92uZXi4BQQ06MtTIc3KCPDe%2BeKS3cCgkVJTyMn24VYHMKIntoc6RIwlEJ%2FXdUO%2Fp1naDTSN1syTCK8jb%2BDCZzYq9BjqkAa74kW7jifhaziWyh%2BtF2DcbypncFqL3s9lzJLmQqye9oEVFGb6rsP5uxxMd%2By1So7Ov8Sw1s0j3ahSklErkvwBNLcei%2Fx6WWBG6g2Wcj7y0ggy9d7KQHEQpYk8lDmvAWzOxImiaDSS3XQV%2FORDKrLjgjAhAx9ZOiJVpZbhN8E5xGj%2FiawcU8VuE3gd844gQq7w8s4lJQDyp43nuBT6cFbWRQiFM&X-Amz-Signature=bef792f8af0ad2cbe42f4d9d509cf1750702c45b657255e0a5baa21d2bee06a9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TC2ZOGK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCnESdNHzFmzYrPqA4J28r33rzG6f%2FL3WWzKBIMdoTuRwIhAL210KD%2FlBW1Qt2zFnl2RYy763id01fcjURHvGwP1T8tKv8DCDkQABoMNjM3NDIzMTgzODA1IgxIzVA5E1pELgg1Z2Yq3AMlDkPL6CAFD9avdihL2Jd0a1mxPmBV4J5iBgezmQiHEzqbdasVUn758p5%2Bpxx2rD2kvfT%2BpGVfU5IPNj3yRQTGxW6NSPOknvEmgOvHo6XEoT79JVXAfJqh%2FXzbrMg9S5oxEdgQg1MOMvcouyBI3iC0DjbE3xzhS17Lr7t1fr%2B%2BKmz4LfNm24R%2BMil8jDBFy%2B1hmF5n%2BXrAFgqey9HmLg16%2BBdQMuHfIL3nUS81reLMoDvElFg8Pb4Iy5HJCJBdZ%2F%2FdVf6LlWVq97S%2BpVaooA7MQsTB66CXPz7GKTj5XtXskZsedC%2Bexa0Bn2cfRVIbHompukXjhCeZ30A4vC7LUNpweOu3591i%2Fa1wdDtlY%2BPMQH30Rl%2BaDysCq%2FaxnVLhyyJ28moSEcf7ZeMlTYEsmpb44GQReQhTgn5gnXQ5Nc6x2jWJHSW0esfsS4aUvQRqWuNM2iucbjxQMQOgxQH3oUINocPx288k6Q%2Flx%2BaAmgjiqB9NbODHe7yk41UGcQicq8vLyO1ZF%2BbpSSnbHV9Lj2jxfbhc4AW59ya6bEzcKdgQ92uZXi4BQQ06MtTIc3KCPDe%2BeKS3cCgkVJTyMn24VYHMKIntoc6RIwlEJ%2FXdUO%2Fp1naDTSN1syTCK8jb%2BDCZzYq9BjqkAa74kW7jifhaziWyh%2BtF2DcbypncFqL3s9lzJLmQqye9oEVFGb6rsP5uxxMd%2By1So7Ov8Sw1s0j3ahSklErkvwBNLcei%2Fx6WWBG6g2Wcj7y0ggy9d7KQHEQpYk8lDmvAWzOxImiaDSS3XQV%2FORDKrLjgjAhAx9ZOiJVpZbhN8E5xGj%2FiawcU8VuE3gd844gQq7w8s4lJQDyp43nuBT6cFbWRQiFM&X-Amz-Signature=eba17a91ee0dd3f31282d07ef7f9206a22b69139cb9bb6e5753ad80b74faa3f3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TC2ZOGK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCnESdNHzFmzYrPqA4J28r33rzG6f%2FL3WWzKBIMdoTuRwIhAL210KD%2FlBW1Qt2zFnl2RYy763id01fcjURHvGwP1T8tKv8DCDkQABoMNjM3NDIzMTgzODA1IgxIzVA5E1pELgg1Z2Yq3AMlDkPL6CAFD9avdihL2Jd0a1mxPmBV4J5iBgezmQiHEzqbdasVUn758p5%2Bpxx2rD2kvfT%2BpGVfU5IPNj3yRQTGxW6NSPOknvEmgOvHo6XEoT79JVXAfJqh%2FXzbrMg9S5oxEdgQg1MOMvcouyBI3iC0DjbE3xzhS17Lr7t1fr%2B%2BKmz4LfNm24R%2BMil8jDBFy%2B1hmF5n%2BXrAFgqey9HmLg16%2BBdQMuHfIL3nUS81reLMoDvElFg8Pb4Iy5HJCJBdZ%2F%2FdVf6LlWVq97S%2BpVaooA7MQsTB66CXPz7GKTj5XtXskZsedC%2Bexa0Bn2cfRVIbHompukXjhCeZ30A4vC7LUNpweOu3591i%2Fa1wdDtlY%2BPMQH30Rl%2BaDysCq%2FaxnVLhyyJ28moSEcf7ZeMlTYEsmpb44GQReQhTgn5gnXQ5Nc6x2jWJHSW0esfsS4aUvQRqWuNM2iucbjxQMQOgxQH3oUINocPx288k6Q%2Flx%2BaAmgjiqB9NbODHe7yk41UGcQicq8vLyO1ZF%2BbpSSnbHV9Lj2jxfbhc4AW59ya6bEzcKdgQ92uZXi4BQQ06MtTIc3KCPDe%2BeKS3cCgkVJTyMn24VYHMKIntoc6RIwlEJ%2FXdUO%2Fp1naDTSN1syTCK8jb%2BDCZzYq9BjqkAa74kW7jifhaziWyh%2BtF2DcbypncFqL3s9lzJLmQqye9oEVFGb6rsP5uxxMd%2By1So7Ov8Sw1s0j3ahSklErkvwBNLcei%2Fx6WWBG6g2Wcj7y0ggy9d7KQHEQpYk8lDmvAWzOxImiaDSS3XQV%2FORDKrLjgjAhAx9ZOiJVpZbhN8E5xGj%2FiawcU8VuE3gd844gQq7w8s4lJQDyp43nuBT6cFbWRQiFM&X-Amz-Signature=2b62cd8c42397e91169a6474d0f09d2e2478c8fac7d6c350aeb77a3c749a9475&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TC2ZOGK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCnESdNHzFmzYrPqA4J28r33rzG6f%2FL3WWzKBIMdoTuRwIhAL210KD%2FlBW1Qt2zFnl2RYy763id01fcjURHvGwP1T8tKv8DCDkQABoMNjM3NDIzMTgzODA1IgxIzVA5E1pELgg1Z2Yq3AMlDkPL6CAFD9avdihL2Jd0a1mxPmBV4J5iBgezmQiHEzqbdasVUn758p5%2Bpxx2rD2kvfT%2BpGVfU5IPNj3yRQTGxW6NSPOknvEmgOvHo6XEoT79JVXAfJqh%2FXzbrMg9S5oxEdgQg1MOMvcouyBI3iC0DjbE3xzhS17Lr7t1fr%2B%2BKmz4LfNm24R%2BMil8jDBFy%2B1hmF5n%2BXrAFgqey9HmLg16%2BBdQMuHfIL3nUS81reLMoDvElFg8Pb4Iy5HJCJBdZ%2F%2FdVf6LlWVq97S%2BpVaooA7MQsTB66CXPz7GKTj5XtXskZsedC%2Bexa0Bn2cfRVIbHompukXjhCeZ30A4vC7LUNpweOu3591i%2Fa1wdDtlY%2BPMQH30Rl%2BaDysCq%2FaxnVLhyyJ28moSEcf7ZeMlTYEsmpb44GQReQhTgn5gnXQ5Nc6x2jWJHSW0esfsS4aUvQRqWuNM2iucbjxQMQOgxQH3oUINocPx288k6Q%2Flx%2BaAmgjiqB9NbODHe7yk41UGcQicq8vLyO1ZF%2BbpSSnbHV9Lj2jxfbhc4AW59ya6bEzcKdgQ92uZXi4BQQ06MtTIc3KCPDe%2BeKS3cCgkVJTyMn24VYHMKIntoc6RIwlEJ%2FXdUO%2Fp1naDTSN1syTCK8jb%2BDCZzYq9BjqkAa74kW7jifhaziWyh%2BtF2DcbypncFqL3s9lzJLmQqye9oEVFGb6rsP5uxxMd%2By1So7Ov8Sw1s0j3ahSklErkvwBNLcei%2Fx6WWBG6g2Wcj7y0ggy9d7KQHEQpYk8lDmvAWzOxImiaDSS3XQV%2FORDKrLjgjAhAx9ZOiJVpZbhN8E5xGj%2FiawcU8VuE3gd844gQq7w8s4lJQDyp43nuBT6cFbWRQiFM&X-Amz-Signature=b4598e0226b937bdf70b1981144e4de88c22a7a2dd5b7d9f2b3474329f88d30e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TC2ZOGK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCnESdNHzFmzYrPqA4J28r33rzG6f%2FL3WWzKBIMdoTuRwIhAL210KD%2FlBW1Qt2zFnl2RYy763id01fcjURHvGwP1T8tKv8DCDkQABoMNjM3NDIzMTgzODA1IgxIzVA5E1pELgg1Z2Yq3AMlDkPL6CAFD9avdihL2Jd0a1mxPmBV4J5iBgezmQiHEzqbdasVUn758p5%2Bpxx2rD2kvfT%2BpGVfU5IPNj3yRQTGxW6NSPOknvEmgOvHo6XEoT79JVXAfJqh%2FXzbrMg9S5oxEdgQg1MOMvcouyBI3iC0DjbE3xzhS17Lr7t1fr%2B%2BKmz4LfNm24R%2BMil8jDBFy%2B1hmF5n%2BXrAFgqey9HmLg16%2BBdQMuHfIL3nUS81reLMoDvElFg8Pb4Iy5HJCJBdZ%2F%2FdVf6LlWVq97S%2BpVaooA7MQsTB66CXPz7GKTj5XtXskZsedC%2Bexa0Bn2cfRVIbHompukXjhCeZ30A4vC7LUNpweOu3591i%2Fa1wdDtlY%2BPMQH30Rl%2BaDysCq%2FaxnVLhyyJ28moSEcf7ZeMlTYEsmpb44GQReQhTgn5gnXQ5Nc6x2jWJHSW0esfsS4aUvQRqWuNM2iucbjxQMQOgxQH3oUINocPx288k6Q%2Flx%2BaAmgjiqB9NbODHe7yk41UGcQicq8vLyO1ZF%2BbpSSnbHV9Lj2jxfbhc4AW59ya6bEzcKdgQ92uZXi4BQQ06MtTIc3KCPDe%2BeKS3cCgkVJTyMn24VYHMKIntoc6RIwlEJ%2FXdUO%2Fp1naDTSN1syTCK8jb%2BDCZzYq9BjqkAa74kW7jifhaziWyh%2BtF2DcbypncFqL3s9lzJLmQqye9oEVFGb6rsP5uxxMd%2By1So7Ov8Sw1s0j3ahSklErkvwBNLcei%2Fx6WWBG6g2Wcj7y0ggy9d7KQHEQpYk8lDmvAWzOxImiaDSS3XQV%2FORDKrLjgjAhAx9ZOiJVpZbhN8E5xGj%2FiawcU8VuE3gd844gQq7w8s4lJQDyp43nuBT6cFbWRQiFM&X-Amz-Signature=cc2df9374ff37fbf469ca46c10924bad9f52fe6f118c168342140e30785e608d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TC2ZOGK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCnESdNHzFmzYrPqA4J28r33rzG6f%2FL3WWzKBIMdoTuRwIhAL210KD%2FlBW1Qt2zFnl2RYy763id01fcjURHvGwP1T8tKv8DCDkQABoMNjM3NDIzMTgzODA1IgxIzVA5E1pELgg1Z2Yq3AMlDkPL6CAFD9avdihL2Jd0a1mxPmBV4J5iBgezmQiHEzqbdasVUn758p5%2Bpxx2rD2kvfT%2BpGVfU5IPNj3yRQTGxW6NSPOknvEmgOvHo6XEoT79JVXAfJqh%2FXzbrMg9S5oxEdgQg1MOMvcouyBI3iC0DjbE3xzhS17Lr7t1fr%2B%2BKmz4LfNm24R%2BMil8jDBFy%2B1hmF5n%2BXrAFgqey9HmLg16%2BBdQMuHfIL3nUS81reLMoDvElFg8Pb4Iy5HJCJBdZ%2F%2FdVf6LlWVq97S%2BpVaooA7MQsTB66CXPz7GKTj5XtXskZsedC%2Bexa0Bn2cfRVIbHompukXjhCeZ30A4vC7LUNpweOu3591i%2Fa1wdDtlY%2BPMQH30Rl%2BaDysCq%2FaxnVLhyyJ28moSEcf7ZeMlTYEsmpb44GQReQhTgn5gnXQ5Nc6x2jWJHSW0esfsS4aUvQRqWuNM2iucbjxQMQOgxQH3oUINocPx288k6Q%2Flx%2BaAmgjiqB9NbODHe7yk41UGcQicq8vLyO1ZF%2BbpSSnbHV9Lj2jxfbhc4AW59ya6bEzcKdgQ92uZXi4BQQ06MtTIc3KCPDe%2BeKS3cCgkVJTyMn24VYHMKIntoc6RIwlEJ%2FXdUO%2Fp1naDTSN1syTCK8jb%2BDCZzYq9BjqkAa74kW7jifhaziWyh%2BtF2DcbypncFqL3s9lzJLmQqye9oEVFGb6rsP5uxxMd%2By1So7Ov8Sw1s0j3ahSklErkvwBNLcei%2Fx6WWBG6g2Wcj7y0ggy9d7KQHEQpYk8lDmvAWzOxImiaDSS3XQV%2FORDKrLjgjAhAx9ZOiJVpZbhN8E5xGj%2FiawcU8VuE3gd844gQq7w8s4lJQDyp43nuBT6cFbWRQiFM&X-Amz-Signature=b0077b6b5acb15ec1f7c96a551118330e442574f815f31f3f923d8d7217bf4eb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIOUIOUJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDoT09X%2F0nrXtQ69o8vAfIfBhwg4Shm9P2HjL5Az53RGAIhAIRdscAd9C%2BwfM0zp7%2F3JsmEvb%2FhzdtPz9Z5CR9blnh8Kv8DCDkQABoMNjM3NDIzMTgzODA1Igzj45N%2FrrMiA83wIBkq3AONWDQaYh1hBq9EIHAtrdwRck0E%2F0SXFhRlqTLjto2SJlQcoOI7BlbGlmNYqeszwSObsnF%2FhA2SQ0jbnvdTPEWh8I5WoxmbhZ5NxvEGV%2B2N5qek9s7fEOhdTFse1ClRlMjZAh8ExV%2BautAJ2xr26pLIHxVW2pUA1CBtTarrUa7C3fQoj8aMCk7LTMEv7CXT17m6TTZJUdNuHCmt4EbY9CFFJbM6A1hjSesJqR5sB4kuTcoFWkDnlA7%2Bv87vtL48c3XMZjkVZ2XTXJaFk1Ri6k9%2B%2F38ww%2Bib6WbTyyeNDlQRPEq6JvmtoCm2%2BTg53gGSy2ivIeCwz3ni2mjVob7o5MePmx0JTs4YNhwh2iqCMVL2ACcs8awH2Q8FbuofQvc0vTNQTrGzlpjiftRrpA9vVurqbHMVHoQ4fFDLNb7qSG%2FfQfkE7XE00mkpczt5HSttn05fHRtsPC8mMB4Vt%2FHWjgyCfXwOGFoBQdsfX8wIAfEKTtUvPJR5LheAG%2BaUmxEMFntIm7tPuzkU3CZLLYUFH1xDU7id3w6zQNPekRJY12A3CQJDr6yEPICOdSh%2BFkrRiHAja6jusP9ek9nEzpvRVw%2BOOFaACxS%2Fo9BFVDegHz6XZyXJZm%2FdmdvpNlv8mTCkzYq9BjqkAT016hn5oGK%2B9J7EoEnHqRh1QSaw9S6nr349PnE4237MosMbuG%2BM2vB3y5F5hFU6FWnOyBRv2jJcT7b0hvhhPhSjtzny39eF1Y3M3bz18d1QELGDz94eYv6EIyPVX3h3te0oNmQE6nf0vnWMFlfk86VBquYW8tJsRs1Oa4X%2BjbLSFBhJ9XUUJcWF%2FPBvUBEnmiKTpnZM4NClWJNlzGovpsav44xu&X-Amz-Signature=1a2b85090ca19eccd9859dec1d85ab2ab7ba53e85397f30c1aeee9811e14cbbc&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUTIXAEE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIBlMy3Ndtwnh4xfJaupAAvChhZFmSxPwI1v0mXZBQl3mAiAUj8xl14JQRbB1mkTb93EVY9ZCRyijgqr6Al9suOnnaSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMC%2BVIZi60Y4oxO51OKtwDFvyPNu%2BXTAY8aY9E6dpc3A0WD9FDwkNETP%2FJhnXIvvPVlMAZPpZ%2BYAe48d%2FcsWP1Frx6gehV5orC3RTLr07aLuBk%2BgtrKAX%2B8RUB0VpuhdMtx9jjcVd4t8FDO%2Fh9JbqSHEL0VldDlvdPueD7IFWoaDA8hpGfGUU1W1NGua6UBl%2ByUmd%2Bj6olTQgXjEQXO7OMncz2CBFrHA%2BhPtb2rI7oyVgtj5K92gMerBe%2BI5%2FMTwXlTyLrhgU83YwADmsg8XgOy9ZxFdz8ksB5Nc4cgvlWTZriNk%2BuUtjxVzDZNBUxLGvQL3Rv8x2N7jUpBFuhU85snP739EqXq2HvwYu3Oo0ym6yAST37D%2FZLdIJbELXmn9R9a1Wpf4UFgbqvj8xq%2BAHthXXQUeYlnYFrIZFoJ7hsuyerIok9HlFPBrYHuy%2BsvBBLeclu5AQo%2FUMLqW6qT2TboR8Oic2ob8jcl3CDtH%2Bff4bcaNDcTWkQe%2BSIbcB5uxYnXXg%2BE1T8pKrnCtZ9rIMYrtQh9jslE1606%2F%2B2odva6uEK%2BCG6hfnuCNodqRKS5AcoB0hfy%2Bks9aRbhQzIrBk678ntuqWt3ek8uDmtETC1RamPdRcWjy%2FD%2BNo1Lylwzc1LVMnkCLEHrdi%2FRcEw58yKvQY6pgHpmxi%2FHWziV6s1azR4qgXpd8rZjvnZO1YlNTCke0pKe9nY2%2FvKxMITJ9qS46AlUoOzn6ADrmvN898D5q1A4VUB1S4i70ssFO5qJgwLWTPGuaGx8FwWcyMgQD7e02Ie7iWU5udvkNoYJj8jxQN4yWMYpABgpNfg9qsjt%2BkrxyQGiX%2FTC2jIxMip3NgHTr4Gvih01Vcp3FMmf1neo1eXjrT%2Fd2mQNbKp&X-Amz-Signature=26cfbb6b0b8e110dbebfe0964d0bd8f87d4e81ab860754a22e3ec60570a408af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TC2ZOGK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCnESdNHzFmzYrPqA4J28r33rzG6f%2FL3WWzKBIMdoTuRwIhAL210KD%2FlBW1Qt2zFnl2RYy763id01fcjURHvGwP1T8tKv8DCDkQABoMNjM3NDIzMTgzODA1IgxIzVA5E1pELgg1Z2Yq3AMlDkPL6CAFD9avdihL2Jd0a1mxPmBV4J5iBgezmQiHEzqbdasVUn758p5%2Bpxx2rD2kvfT%2BpGVfU5IPNj3yRQTGxW6NSPOknvEmgOvHo6XEoT79JVXAfJqh%2FXzbrMg9S5oxEdgQg1MOMvcouyBI3iC0DjbE3xzhS17Lr7t1fr%2B%2BKmz4LfNm24R%2BMil8jDBFy%2B1hmF5n%2BXrAFgqey9HmLg16%2BBdQMuHfIL3nUS81reLMoDvElFg8Pb4Iy5HJCJBdZ%2F%2FdVf6LlWVq97S%2BpVaooA7MQsTB66CXPz7GKTj5XtXskZsedC%2Bexa0Bn2cfRVIbHompukXjhCeZ30A4vC7LUNpweOu3591i%2Fa1wdDtlY%2BPMQH30Rl%2BaDysCq%2FaxnVLhyyJ28moSEcf7ZeMlTYEsmpb44GQReQhTgn5gnXQ5Nc6x2jWJHSW0esfsS4aUvQRqWuNM2iucbjxQMQOgxQH3oUINocPx288k6Q%2Flx%2BaAmgjiqB9NbODHe7yk41UGcQicq8vLyO1ZF%2BbpSSnbHV9Lj2jxfbhc4AW59ya6bEzcKdgQ92uZXi4BQQ06MtTIc3KCPDe%2BeKS3cCgkVJTyMn24VYHMKIntoc6RIwlEJ%2FXdUO%2Fp1naDTSN1syTCK8jb%2BDCZzYq9BjqkAa74kW7jifhaziWyh%2BtF2DcbypncFqL3s9lzJLmQqye9oEVFGb6rsP5uxxMd%2By1So7Ov8Sw1s0j3ahSklErkvwBNLcei%2Fx6WWBG6g2Wcj7y0ggy9d7KQHEQpYk8lDmvAWzOxImiaDSS3XQV%2FORDKrLjgjAhAx9ZOiJVpZbhN8E5xGj%2FiawcU8VuE3gd844gQq7w8s4lJQDyp43nuBT6cFbWRQiFM&X-Amz-Signature=44dcf856c40f7dbe040c48ed159596615108c0f646609e05079c9f5300b702f6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TC2ZOGK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCnESdNHzFmzYrPqA4J28r33rzG6f%2FL3WWzKBIMdoTuRwIhAL210KD%2FlBW1Qt2zFnl2RYy763id01fcjURHvGwP1T8tKv8DCDkQABoMNjM3NDIzMTgzODA1IgxIzVA5E1pELgg1Z2Yq3AMlDkPL6CAFD9avdihL2Jd0a1mxPmBV4J5iBgezmQiHEzqbdasVUn758p5%2Bpxx2rD2kvfT%2BpGVfU5IPNj3yRQTGxW6NSPOknvEmgOvHo6XEoT79JVXAfJqh%2FXzbrMg9S5oxEdgQg1MOMvcouyBI3iC0DjbE3xzhS17Lr7t1fr%2B%2BKmz4LfNm24R%2BMil8jDBFy%2B1hmF5n%2BXrAFgqey9HmLg16%2BBdQMuHfIL3nUS81reLMoDvElFg8Pb4Iy5HJCJBdZ%2F%2FdVf6LlWVq97S%2BpVaooA7MQsTB66CXPz7GKTj5XtXskZsedC%2Bexa0Bn2cfRVIbHompukXjhCeZ30A4vC7LUNpweOu3591i%2Fa1wdDtlY%2BPMQH30Rl%2BaDysCq%2FaxnVLhyyJ28moSEcf7ZeMlTYEsmpb44GQReQhTgn5gnXQ5Nc6x2jWJHSW0esfsS4aUvQRqWuNM2iucbjxQMQOgxQH3oUINocPx288k6Q%2Flx%2BaAmgjiqB9NbODHe7yk41UGcQicq8vLyO1ZF%2BbpSSnbHV9Lj2jxfbhc4AW59ya6bEzcKdgQ92uZXi4BQQ06MtTIc3KCPDe%2BeKS3cCgkVJTyMn24VYHMKIntoc6RIwlEJ%2FXdUO%2Fp1naDTSN1syTCK8jb%2BDCZzYq9BjqkAa74kW7jifhaziWyh%2BtF2DcbypncFqL3s9lzJLmQqye9oEVFGb6rsP5uxxMd%2By1So7Ov8Sw1s0j3ahSklErkvwBNLcei%2Fx6WWBG6g2Wcj7y0ggy9d7KQHEQpYk8lDmvAWzOxImiaDSS3XQV%2FORDKrLjgjAhAx9ZOiJVpZbhN8E5xGj%2FiawcU8VuE3gd844gQq7w8s4lJQDyp43nuBT6cFbWRQiFM&X-Amz-Signature=6737590e0dc43463110c3c8e2f01be50a2fcef28350e3d61b50e3b3c18712acf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TC2ZOGK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCnESdNHzFmzYrPqA4J28r33rzG6f%2FL3WWzKBIMdoTuRwIhAL210KD%2FlBW1Qt2zFnl2RYy763id01fcjURHvGwP1T8tKv8DCDkQABoMNjM3NDIzMTgzODA1IgxIzVA5E1pELgg1Z2Yq3AMlDkPL6CAFD9avdihL2Jd0a1mxPmBV4J5iBgezmQiHEzqbdasVUn758p5%2Bpxx2rD2kvfT%2BpGVfU5IPNj3yRQTGxW6NSPOknvEmgOvHo6XEoT79JVXAfJqh%2FXzbrMg9S5oxEdgQg1MOMvcouyBI3iC0DjbE3xzhS17Lr7t1fr%2B%2BKmz4LfNm24R%2BMil8jDBFy%2B1hmF5n%2BXrAFgqey9HmLg16%2BBdQMuHfIL3nUS81reLMoDvElFg8Pb4Iy5HJCJBdZ%2F%2FdVf6LlWVq97S%2BpVaooA7MQsTB66CXPz7GKTj5XtXskZsedC%2Bexa0Bn2cfRVIbHompukXjhCeZ30A4vC7LUNpweOu3591i%2Fa1wdDtlY%2BPMQH30Rl%2BaDysCq%2FaxnVLhyyJ28moSEcf7ZeMlTYEsmpb44GQReQhTgn5gnXQ5Nc6x2jWJHSW0esfsS4aUvQRqWuNM2iucbjxQMQOgxQH3oUINocPx288k6Q%2Flx%2BaAmgjiqB9NbODHe7yk41UGcQicq8vLyO1ZF%2BbpSSnbHV9Lj2jxfbhc4AW59ya6bEzcKdgQ92uZXi4BQQ06MtTIc3KCPDe%2BeKS3cCgkVJTyMn24VYHMKIntoc6RIwlEJ%2FXdUO%2Fp1naDTSN1syTCK8jb%2BDCZzYq9BjqkAa74kW7jifhaziWyh%2BtF2DcbypncFqL3s9lzJLmQqye9oEVFGb6rsP5uxxMd%2By1So7Ov8Sw1s0j3ahSklErkvwBNLcei%2Fx6WWBG6g2Wcj7y0ggy9d7KQHEQpYk8lDmvAWzOxImiaDSS3XQV%2FORDKrLjgjAhAx9ZOiJVpZbhN8E5xGj%2FiawcU8VuE3gd844gQq7w8s4lJQDyp43nuBT6cFbWRQiFM&X-Amz-Signature=296adba3bd613d363224673817274ba294a2ebb98a3c49305a78ff7b6c848f2c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C63XWT5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIEPES5pHoPbcCquxkAxAXzsBd5FZX5Rd5CN6Uwm8bNLiAiEAhidhLukTxLIfL0OLrMrJMb%2BPHZKBFsiEpY1vTVbnt4wq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDI6RzvHcZQ5DfMqE%2BCrcA47v%2BcCnjRu3lYktH99GVXBlyzZNrsP46jkejVo7fa7Z9DCktdcm%2Bvd18EFXjvWGqFPkSIfbyUIDzHNSKU0PHMXdfgpXQIlRegWDSwKhafYFmGuAUZPYKFuBPWgKBZ9nn%2Fu0QypeD%2BG6Yx8BLBdkJLQ62p2jwS2EtExwDjExJ6oxi%2BQkTXiGBrsRm8pVxuNGmwr%2BIyQhM0lZsZhVqYcFM1Ux5a65CGdjn0wmCruCg%2FB2q6vaBkjqQw6yGMpRWL8i%2Ftu4WjNhERbcBVI6M2b6LDkJXZAqbm1K86Ei2laeY6nCplQUXoMeW1dfgHRIqFbQ0KoB4u6LQbvSO3%2FTFh5tEQjPEaC67MGsOdeccdBYZppBQkRdqUTzQpaO3hNV1KTvp6XysPtuqnqE6UwC4CgOe2jRRths1emqqQ9VF7orGeZ0iEsLisTa7Ve%2BwgKn%2BlubxjRYqJSP5cCQA9sMYgIxGl9zoEB7IHpmUS6DW2LH2wmt4fsD79bl%2F1teGz7R1X1c8OkceLgox%2BM2TdoUil%2Bb7h8b9BfDE4JFkSoV6iHQtUhNto6VAjziYTJh0a4ZuAgMhSN6nefxhLK%2F9iLSCHbOXOC%2BZ68YgT6A6%2B%2BOQ5m%2FqAHqHL67O76ECjuCD5uVMKjNir0GOqUBh3gW1hbs35WO%2BHXx3MHDZjOjNgkOtX3l6q5uekbKDDhlSZ2HIJszRmYLsc6eICii20C2NXvYyIfznsVbb5Kerq6Yv1X9xEY2xsIr8gpA6CWw1SHFzHTwJxzFtvKvFcsfezKpXswh8T88MbXF2%2BNyNLUCk7tGDJPO8UQZtw1QdDH7TMlTy8VFoWOMzU7Nz7UjU3ImPOB2GkfbOFQo3e6cGISHzLPZ&X-Amz-Signature=dc255dfebda53cd8e85af50a160aa23755e6159a2d64d3fc57403b8a6015a450&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQYMOBOO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIB4xZuB7UqTkSbYF7C%2BMSu6%2FDULnX0k7v%2FC80zuIjGSRAiAOUsxaiIpPoq%2FcNc1%2BHNcMbQ9ALzus0G8MkR6fDn1NUir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMmwJfriVTECKAIoQSKtwDnmHwtF0OuAY13bbGdmrmCNSSwsIY21JgPdcQ46djJswr%2B9M%2FTbpeo571P98RHbPapjHIx%2Fuw6FGctNOVncVzmZ1LxEJlaMhUObRGnFkwqV2PCjTNcDZvFv7SH3G9fxGuNTJx7txyO2twgl28rO827m5tPV5KGaeo4rgipxgGP7qoRCloCwFk3zgQMl7hZEgkvhf1a3y2ej6Yfo4Q3CW3CkLOnxNGbrp0ihb34iuSZYmN2nezd6vjLwD9e6RdQm6TSHwKlWmyB6OlU6MNxanL3lK%2B3gquxcreWhgEr7AXIzcp%2FRYO%2FX7CA%2FJgYrXjpFW40w2H8%2FcIlAGqxYEsGPJ9fqnoMK4Uw4%2FX0Mfv2%2FmhRbNo%2B046C%2BHdETdpbS28MSxzhQFtL68%2BPCGb5Iu7FS3iUMt4kKcf2ckdNJuSvFiOkTcGKXTZW9Ykf2ypS3W%2FD4DjCNOz8WMtYMa4IGN3MEMHI8S8g%2BzgC0Y2an0WQ5S5LR1y3FMvl1dmXMNjso4VBmtrwRRm2m6LdPx7yNDsdY6dlTLGdhwf12gTNiOJd2h1iAuYFEbAxL53URhlCrVqT7oIYkg5CL%2B81apXHH2bn%2F2mPfmDkXNoTngUDAlCm6U1IRQqPxRw2qc%2F8GDNpeEwrs2KvQY6pgEt4d4FSKkvvRBKnyhmQCIKxLpPEHUhO4But0IzggUf0Pq%2FDrcY1Nv4%2BNtMIvV2LW1Dq9k7QAC9%2Blp85A%2F8TV0aBmbqvS%2FMV2WDIuOIdYDoq8RcGKTgGhTfnE6HXgM03AMrWI95FN1zUrwdEX6Kczojxt8TDQp%2BSmwhsP1oWykKshDEEKP57YPMxDKhTwF%2FDCjVGLtfTYZ8qMYswnepgh2y4pnQsydl&X-Amz-Signature=25f48e058597053a647dcdfd666da9786d670550eb2e74f83caf6656e6f7157f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7PAK753%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFkHlZ3HNByaNZSI2Sf2istsj539WfhV%2BwzWIQzIMLngAiEAkyQy1xm8oxn8jLCUdpzW5PB0cEC%2FoDaBJZlCK6CYj0Qq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCZFuxv4xPxVFBrHmircAwUxbUAfMwVPqmXt1zWIR9o1zMAnfxFqgTjPG0dCRY0EMol%2B1P2wf%2FJ8gVEkBWr1qQwhgSHMmIrWVzuNex4mwcuy%2FwC5w6V2fSzQtNophxtz%2FVqqEQeqpqIf%2BLB7%2F5vjpA%2FAg1Ow8BqVNhwHeh%2F%2Fadx3zTZYEMDv%2Fh2KyIp7C5RbFbAEC2qoO8f5j5dKw6ZWcpRlMZhkkcl5c7dfb3DqFJDz2hBjjbjl0Ew5axx7zTa7meKvPhX8EjmdfIDGkWQHsymQ1NNbXkG%2B9z7%2F8PqgHs5jE8xDR3TKI61DX%2BZoFSfALUNc%2B93GQ4q81mpuFmzWjM8PP1dYtHE3v%2BGMSDQAhqDPfAYJO1JRJtwPSeTZi2cJg2MtU7VS0TPUrsqTJ23LSlxf0SsDwvwIfmc1UD4SQwIlAxHPgVy0HKfHCY1QPQixIWNva1GVorVVCqLXKP%2F42KZoGDnwrHB2eeKJC8lYwAL9NwpEk3V8M%2FpzuluAcWK07Tw3zFO9rc11qYfQhMx%2BZrOmiZgWeTUMnlSvk0zJtZTRad0nRsmUGG2jkbk9V7SJgXD3EPU%2BNNmi%2Bm3W10gHTcOXoL5f4TXaV2JCz4G9MpgaWaeHYb9gCfEDGzPgNgbqCUn5RtVhyJyWK7ufMNLNir0GOqUBLogL7HneIKavI6aA6Hc5rP%2FrU2OXHwaUMuaVTuoXFrao4BkvbrF1C02KbiYh9X9IcwCWHBY0a%2Ft0CAIQjQJ7dP7ZuUcrvftODgsGqbwzmOhsSFpU%2FTG8A3yanxVne4POGjiEEGVOOANLUNDlK9QGAFczQNKCM%2BpxyAqi8r2bGMh8JlOY2eqCkE1HDOFMWE0M%2Fi%2B4AWXAFaqsvGpGqv8IXQfvqqTf&X-Amz-Signature=6c70b0bce881b5382b42b2164cb72facd0df5c3c9501f134eac3a9f36aae6c83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDJ4QFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSs9Nq6NU0wMcE89LH%2Bh7i5rx%2FTFpHaQdhx8r1LoqRmQIhAIoYHzNypZTlQKgoGgaFwlz90WBJg7eZH62u1JGjRgxeKv8DCDkQABoMNjM3NDIzMTgzODA1Igy3lYbWSrUKqali0lwq3ANrUu%2FI2u5yxMwmt2%2BiBQKtzVFuYt%2BkpP8TnwgemPrVNSmt2F5G30ONz9woq2EYIamyW0i36fXUFu1WFdS%2BFLaAX97ouHSKnhn7w2BVk4CuE7PEtPI%2BJb76bAlZ9nhYTCII%2B9SitE%2FWuRFnLfAgkvIp5icxuE7Kw72j%2Fxlz7FUmjM1MBTbAdwyQET%2BtPcxKCkgPplc4YI1a0wzrD%2BI%2F38HaDB2qpISmIfLYkPpcTaW34bGuOiBFjiltdeqDhc%2BWRpLjypgQjIN5FbT%2F4JjiaHJl%2Faa0txb34CBDfK88eVCyteLyMhJBpwPEJ2jAFFTnW6k%2FmEWTSZWkDy1JNoQ0ZVN%2BSfLwGZdP8ir7E8lW5jTcTK8H6GXJOIC5%2FK8maAV2%2F5b%2FKr2nTuNt8Yk38HK%2F0Sl2fLOMUycFw12vWan3Wqjy6WzEOxVSDrSM0eM6yuoAw%2FhsSQpmGuL8nReMZmIHvwR7ullen8ldOWmuIjecKNig94ifS33m5SUScsRFT3%2F9ne502ZByu86%2FBg26ddxFsJdZQr%2FbsoGV7orJZ%2B8hOv4w%2FQMjhazcfYVpy6vvCfLvpiP5Fy1LcHKPzQihYPMA32NhoMfXFq0b9AUbQK%2FXkYKk79a%2FGIlvZ3wTQz63ijD7zIq9BjqkAX61kSrzTwLhZcFQ2mb29kaMsVHyKrw4QEhrLxlkPiKzzins7GpUdlSa3ayZRtbYi%2FdqJgutgze6HulU%2F1g58tTUvJcXfF%2FRXAdAmz9JAjnK6PMOgGDB6NMFruvVEffkYzkj%2FNZ9udgc2j6TE2ptfWoc9SnyUtmajKD1Ku11UnX8FW6b8eTizLKVnEgO6pKdaUuLrxj93iAC1BXPRv%2FMPe6VMS75&X-Amz-Signature=7d7386ce2759c0a311a3dfeab1f1883903ada44471946f33cef8e211129f893d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDJ4QFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSs9Nq6NU0wMcE89LH%2Bh7i5rx%2FTFpHaQdhx8r1LoqRmQIhAIoYHzNypZTlQKgoGgaFwlz90WBJg7eZH62u1JGjRgxeKv8DCDkQABoMNjM3NDIzMTgzODA1Igy3lYbWSrUKqali0lwq3ANrUu%2FI2u5yxMwmt2%2BiBQKtzVFuYt%2BkpP8TnwgemPrVNSmt2F5G30ONz9woq2EYIamyW0i36fXUFu1WFdS%2BFLaAX97ouHSKnhn7w2BVk4CuE7PEtPI%2BJb76bAlZ9nhYTCII%2B9SitE%2FWuRFnLfAgkvIp5icxuE7Kw72j%2Fxlz7FUmjM1MBTbAdwyQET%2BtPcxKCkgPplc4YI1a0wzrD%2BI%2F38HaDB2qpISmIfLYkPpcTaW34bGuOiBFjiltdeqDhc%2BWRpLjypgQjIN5FbT%2F4JjiaHJl%2Faa0txb34CBDfK88eVCyteLyMhJBpwPEJ2jAFFTnW6k%2FmEWTSZWkDy1JNoQ0ZVN%2BSfLwGZdP8ir7E8lW5jTcTK8H6GXJOIC5%2FK8maAV2%2F5b%2FKr2nTuNt8Yk38HK%2F0Sl2fLOMUycFw12vWan3Wqjy6WzEOxVSDrSM0eM6yuoAw%2FhsSQpmGuL8nReMZmIHvwR7ullen8ldOWmuIjecKNig94ifS33m5SUScsRFT3%2F9ne502ZByu86%2FBg26ddxFsJdZQr%2FbsoGV7orJZ%2B8hOv4w%2FQMjhazcfYVpy6vvCfLvpiP5Fy1LcHKPzQihYPMA32NhoMfXFq0b9AUbQK%2FXkYKk79a%2FGIlvZ3wTQz63ijD7zIq9BjqkAX61kSrzTwLhZcFQ2mb29kaMsVHyKrw4QEhrLxlkPiKzzins7GpUdlSa3ayZRtbYi%2FdqJgutgze6HulU%2F1g58tTUvJcXfF%2FRXAdAmz9JAjnK6PMOgGDB6NMFruvVEffkYzkj%2FNZ9udgc2j6TE2ptfWoc9SnyUtmajKD1Ku11UnX8FW6b8eTizLKVnEgO6pKdaUuLrxj93iAC1BXPRv%2FMPe6VMS75&X-Amz-Signature=37deca93a778e621dc43253b5b36138bf4e45c7e23d370de351c1d0c1a4561b4&X-Amz-SignedHeaders=host&x-id=GetObject)

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
