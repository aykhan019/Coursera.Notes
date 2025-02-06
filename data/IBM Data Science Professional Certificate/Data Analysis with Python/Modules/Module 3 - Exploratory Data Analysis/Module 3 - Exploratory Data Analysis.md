

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZHKXZJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCzgZA%2FC9BgfzWB3N3LgOGjQYffRulPM%2FjcoBe9Ws%2FykwIgMpfDYYwAHyGpjUtuAQij5%2FGU6pBUUwVTIsnbxOXkOiYq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDIM8Tb72vUiguMTmBircAzy1YwrfcYnwcdgi38HEGPTdh0GZt5XiegUobMDKdW4Zu%2Bf4nYqFjX9fLcmWOoYvv5E%2FQ5VSrkumpWdWmmmFd0shDwZO%2F6N7yLS37F1snjtuwCJ%2FDnpMmsBulL%2BWZg616i3u16GyuVPbBObFX9FJSY8xCNFc7Nk%2Fx%2Fl24G0m7Npk1viAGtNryOuw5LYdst%2Bhj8pWmJU4svhLLVrYVA%2BDN29bFfIjDaYbz5VEDjjlvTkfHWzq5TKLB5vUGmT2WbvIzi9IlJBTr%2B0M7wKiLHaOsG9BGavH1kLO2YD5Qsw8QQiXOW8N6Ya2nDSOnfdtiBvRMEI%2FEVK5rjN%2B6XAEDukwo2wbggJBpOylSvyU2mSTvtwXPROz8xWu4WM1%2BDo%2BeYJTUTyUt26%2FDAAMHzloSNvTy2AwV0Ng84hZmMWKHoBpa7VvYqDb7R9eggOI3RwrFPSYU5eE05XTdgkhxDPMXeBTleXMhXsQs8nHZw9GrvXJSS0sHa4cvwOgtzs4dEj82E%2FKFD4hZXMhw1BCugyf07QsbQcnWTdMoWtXrTcKq9HfqbWhz8btKhZhTm%2BGxdFQkLthPHQIPaMbNa%2BDp4D3pw4%2BSDRf%2Fh%2BiWKvV4xIAgFd1IsGtGSvSYD2DgBVcSHJeMLLRkb0GOqUBSM9wZm2WIilN1UfrWfYdgZAbQgFMpmZOaPedADuZAYS9f9V%2FkMhRgvM6%2Bsg7bT5q%2FcxFXAmKn3kG4HeO5fiDwPK%2FZGtnHKOWWQJiafvOx8PFonueK9p3vSrln3IdWK6WoRFIVCxj0yEz674i3qdInJ7zrYrGfa8uSLo9WR5Rry5mpZ552eKEsqHLOhgNW9lU4t%2BWImoMlj3nHtoNKmA%2F%2FSbNJ%2BfP&X-Amz-Signature=db6c6ac75992d88cab70e9016eeb6b8b241f22eb277dcb1747d5930b29948466&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZHKXZJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCzgZA%2FC9BgfzWB3N3LgOGjQYffRulPM%2FjcoBe9Ws%2FykwIgMpfDYYwAHyGpjUtuAQij5%2FGU6pBUUwVTIsnbxOXkOiYq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDIM8Tb72vUiguMTmBircAzy1YwrfcYnwcdgi38HEGPTdh0GZt5XiegUobMDKdW4Zu%2Bf4nYqFjX9fLcmWOoYvv5E%2FQ5VSrkumpWdWmmmFd0shDwZO%2F6N7yLS37F1snjtuwCJ%2FDnpMmsBulL%2BWZg616i3u16GyuVPbBObFX9FJSY8xCNFc7Nk%2Fx%2Fl24G0m7Npk1viAGtNryOuw5LYdst%2Bhj8pWmJU4svhLLVrYVA%2BDN29bFfIjDaYbz5VEDjjlvTkfHWzq5TKLB5vUGmT2WbvIzi9IlJBTr%2B0M7wKiLHaOsG9BGavH1kLO2YD5Qsw8QQiXOW8N6Ya2nDSOnfdtiBvRMEI%2FEVK5rjN%2B6XAEDukwo2wbggJBpOylSvyU2mSTvtwXPROz8xWu4WM1%2BDo%2BeYJTUTyUt26%2FDAAMHzloSNvTy2AwV0Ng84hZmMWKHoBpa7VvYqDb7R9eggOI3RwrFPSYU5eE05XTdgkhxDPMXeBTleXMhXsQs8nHZw9GrvXJSS0sHa4cvwOgtzs4dEj82E%2FKFD4hZXMhw1BCugyf07QsbQcnWTdMoWtXrTcKq9HfqbWhz8btKhZhTm%2BGxdFQkLthPHQIPaMbNa%2BDp4D3pw4%2BSDRf%2Fh%2BiWKvV4xIAgFd1IsGtGSvSYD2DgBVcSHJeMLLRkb0GOqUBSM9wZm2WIilN1UfrWfYdgZAbQgFMpmZOaPedADuZAYS9f9V%2FkMhRgvM6%2Bsg7bT5q%2FcxFXAmKn3kG4HeO5fiDwPK%2FZGtnHKOWWQJiafvOx8PFonueK9p3vSrln3IdWK6WoRFIVCxj0yEz674i3qdInJ7zrYrGfa8uSLo9WR5Rry5mpZ552eKEsqHLOhgNW9lU4t%2BWImoMlj3nHtoNKmA%2F%2FSbNJ%2BfP&X-Amz-Signature=5697498fda993156a6f43a3019af97393a0b87d14f2d5d0f00759b9e2c960890&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZHKXZJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCzgZA%2FC9BgfzWB3N3LgOGjQYffRulPM%2FjcoBe9Ws%2FykwIgMpfDYYwAHyGpjUtuAQij5%2FGU6pBUUwVTIsnbxOXkOiYq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDIM8Tb72vUiguMTmBircAzy1YwrfcYnwcdgi38HEGPTdh0GZt5XiegUobMDKdW4Zu%2Bf4nYqFjX9fLcmWOoYvv5E%2FQ5VSrkumpWdWmmmFd0shDwZO%2F6N7yLS37F1snjtuwCJ%2FDnpMmsBulL%2BWZg616i3u16GyuVPbBObFX9FJSY8xCNFc7Nk%2Fx%2Fl24G0m7Npk1viAGtNryOuw5LYdst%2Bhj8pWmJU4svhLLVrYVA%2BDN29bFfIjDaYbz5VEDjjlvTkfHWzq5TKLB5vUGmT2WbvIzi9IlJBTr%2B0M7wKiLHaOsG9BGavH1kLO2YD5Qsw8QQiXOW8N6Ya2nDSOnfdtiBvRMEI%2FEVK5rjN%2B6XAEDukwo2wbggJBpOylSvyU2mSTvtwXPROz8xWu4WM1%2BDo%2BeYJTUTyUt26%2FDAAMHzloSNvTy2AwV0Ng84hZmMWKHoBpa7VvYqDb7R9eggOI3RwrFPSYU5eE05XTdgkhxDPMXeBTleXMhXsQs8nHZw9GrvXJSS0sHa4cvwOgtzs4dEj82E%2FKFD4hZXMhw1BCugyf07QsbQcnWTdMoWtXrTcKq9HfqbWhz8btKhZhTm%2BGxdFQkLthPHQIPaMbNa%2BDp4D3pw4%2BSDRf%2Fh%2BiWKvV4xIAgFd1IsGtGSvSYD2DgBVcSHJeMLLRkb0GOqUBSM9wZm2WIilN1UfrWfYdgZAbQgFMpmZOaPedADuZAYS9f9V%2FkMhRgvM6%2Bsg7bT5q%2FcxFXAmKn3kG4HeO5fiDwPK%2FZGtnHKOWWQJiafvOx8PFonueK9p3vSrln3IdWK6WoRFIVCxj0yEz674i3qdInJ7zrYrGfa8uSLo9WR5Rry5mpZ552eKEsqHLOhgNW9lU4t%2BWImoMlj3nHtoNKmA%2F%2FSbNJ%2BfP&X-Amz-Signature=8839a7d4cc399546426bfa890b7f390756947ee0b4fd9e29e0c1e164239386cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IM254BP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD%2Bqg1zvZTMMYqOA8dZGb5fu%2FVjUdpCvvSPmRJZySEWBwIgCkP0kys8DNBjPKmX4booSsWNtHMmRMPWBv%2Bsi2LUS%2F4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDAd%2BZnBdtlZqrr29gyrcA3qMc%2F9PQHg1OnqG9D7QlwFUBLs0hmFC8ahjZLhx61boz3riT5OvuioAbHghNofRSo6TKHaA8IqipEromlyBrzC2I4Fx%2BeXOhM6FBCwNxaqXyqnRiq35aP6X0v8kZOva7cxxBmoPHKwaBYU1p0bLtFGmcpZhNgbxJ%2BWLpLXe%2FnTylcMdljkPUu6%2F9zMFUQyCg6gDAIcH5SuSt%2F%2BgVmVa6%2FSGIK1JimAv4wJWRMvE1PfUoDkzuLdXBTTGVQdlJFZyILkJywl7flpEifL2DLd4dhZ72V1n3eQ7V2z52p8NBi2D7Cs1vQu3dYAO5CjL9k%2B72rQ6m925CL7ifXZJ1%2B2DIl%2BCCDVtoz0cKsHBKWKg%2BTsQHfLTTesS38ugm6xD9KJ8K%2BvyYgcioufueR7eesXKzox70dQHVn30OwqONFn0YlrEU0Gg02jy5lsX7toAyQV9oB3z8jStid2bVVoKLkVqO7OE8ZL3TVGx2Pdu2b%2B9iQcdwTzSqgHG4QKRfyzii%2Fsp%2BTpjsbhE9zjAFpCtfI4%2Fry1K%2BPBvn42IQT%2F23vPn8XTsmYxYPKGfhziWcR5SnzJB1PJHPyYBCkulpbKNQhdNLVjNtWJCQed0Qg3lMGjxfuQjSwW3zXr5mBaT5RrmMPfQkb0GOqUBjFYmI0OZGhwQweXGyMvk1VzhNd5sbgCtcyYvz0cjFup8t5mCWHT5O6R3HNBukwZIadFtI8CPwJTwDvEO2MeQ%2FhhXPF%2Fft9YZAATnN%2FVkRREJUL7ISuJo7YS%2FJvI0ZIKiafRP16ZdRcPEY3vh6vOWjB%2BPZLT8VwyS%2BqObAC4sCE5euQx%2FPJgjKASUq9C8kEBMbKuqKp5x1neAXXW9JYJ%2BRZWRftkc&X-Amz-Signature=787fbc8c96a3daabfb0453f0704f6bf03d643763fa7e6b2814cccdfd7f533b15&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IM254BP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD%2Bqg1zvZTMMYqOA8dZGb5fu%2FVjUdpCvvSPmRJZySEWBwIgCkP0kys8DNBjPKmX4booSsWNtHMmRMPWBv%2Bsi2LUS%2F4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDAd%2BZnBdtlZqrr29gyrcA3qMc%2F9PQHg1OnqG9D7QlwFUBLs0hmFC8ahjZLhx61boz3riT5OvuioAbHghNofRSo6TKHaA8IqipEromlyBrzC2I4Fx%2BeXOhM6FBCwNxaqXyqnRiq35aP6X0v8kZOva7cxxBmoPHKwaBYU1p0bLtFGmcpZhNgbxJ%2BWLpLXe%2FnTylcMdljkPUu6%2F9zMFUQyCg6gDAIcH5SuSt%2F%2BgVmVa6%2FSGIK1JimAv4wJWRMvE1PfUoDkzuLdXBTTGVQdlJFZyILkJywl7flpEifL2DLd4dhZ72V1n3eQ7V2z52p8NBi2D7Cs1vQu3dYAO5CjL9k%2B72rQ6m925CL7ifXZJ1%2B2DIl%2BCCDVtoz0cKsHBKWKg%2BTsQHfLTTesS38ugm6xD9KJ8K%2BvyYgcioufueR7eesXKzox70dQHVn30OwqONFn0YlrEU0Gg02jy5lsX7toAyQV9oB3z8jStid2bVVoKLkVqO7OE8ZL3TVGx2Pdu2b%2B9iQcdwTzSqgHG4QKRfyzii%2Fsp%2BTpjsbhE9zjAFpCtfI4%2Fry1K%2BPBvn42IQT%2F23vPn8XTsmYxYPKGfhziWcR5SnzJB1PJHPyYBCkulpbKNQhdNLVjNtWJCQed0Qg3lMGjxfuQjSwW3zXr5mBaT5RrmMPfQkb0GOqUBjFYmI0OZGhwQweXGyMvk1VzhNd5sbgCtcyYvz0cjFup8t5mCWHT5O6R3HNBukwZIadFtI8CPwJTwDvEO2MeQ%2FhhXPF%2Fft9YZAATnN%2FVkRREJUL7ISuJo7YS%2FJvI0ZIKiafRP16ZdRcPEY3vh6vOWjB%2BPZLT8VwyS%2BqObAC4sCE5euQx%2FPJgjKASUq9C8kEBMbKuqKp5x1neAXXW9JYJ%2BRZWRftkc&X-Amz-Signature=759bf80a2106eb922cb397efe6b0e0d217404d36166401a105c741b8a84a6428&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IM254BP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD%2Bqg1zvZTMMYqOA8dZGb5fu%2FVjUdpCvvSPmRJZySEWBwIgCkP0kys8DNBjPKmX4booSsWNtHMmRMPWBv%2Bsi2LUS%2F4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDAd%2BZnBdtlZqrr29gyrcA3qMc%2F9PQHg1OnqG9D7QlwFUBLs0hmFC8ahjZLhx61boz3riT5OvuioAbHghNofRSo6TKHaA8IqipEromlyBrzC2I4Fx%2BeXOhM6FBCwNxaqXyqnRiq35aP6X0v8kZOva7cxxBmoPHKwaBYU1p0bLtFGmcpZhNgbxJ%2BWLpLXe%2FnTylcMdljkPUu6%2F9zMFUQyCg6gDAIcH5SuSt%2F%2BgVmVa6%2FSGIK1JimAv4wJWRMvE1PfUoDkzuLdXBTTGVQdlJFZyILkJywl7flpEifL2DLd4dhZ72V1n3eQ7V2z52p8NBi2D7Cs1vQu3dYAO5CjL9k%2B72rQ6m925CL7ifXZJ1%2B2DIl%2BCCDVtoz0cKsHBKWKg%2BTsQHfLTTesS38ugm6xD9KJ8K%2BvyYgcioufueR7eesXKzox70dQHVn30OwqONFn0YlrEU0Gg02jy5lsX7toAyQV9oB3z8jStid2bVVoKLkVqO7OE8ZL3TVGx2Pdu2b%2B9iQcdwTzSqgHG4QKRfyzii%2Fsp%2BTpjsbhE9zjAFpCtfI4%2Fry1K%2BPBvn42IQT%2F23vPn8XTsmYxYPKGfhziWcR5SnzJB1PJHPyYBCkulpbKNQhdNLVjNtWJCQed0Qg3lMGjxfuQjSwW3zXr5mBaT5RrmMPfQkb0GOqUBjFYmI0OZGhwQweXGyMvk1VzhNd5sbgCtcyYvz0cjFup8t5mCWHT5O6R3HNBukwZIadFtI8CPwJTwDvEO2MeQ%2FhhXPF%2Fft9YZAATnN%2FVkRREJUL7ISuJo7YS%2FJvI0ZIKiafRP16ZdRcPEY3vh6vOWjB%2BPZLT8VwyS%2BqObAC4sCE5euQx%2FPJgjKASUq9C8kEBMbKuqKp5x1neAXXW9JYJ%2BRZWRftkc&X-Amz-Signature=1a9dd777e5779d92106563dfa96140958c6b496fe3eba625be474d4508dfc464&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IM254BP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD%2Bqg1zvZTMMYqOA8dZGb5fu%2FVjUdpCvvSPmRJZySEWBwIgCkP0kys8DNBjPKmX4booSsWNtHMmRMPWBv%2Bsi2LUS%2F4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDAd%2BZnBdtlZqrr29gyrcA3qMc%2F9PQHg1OnqG9D7QlwFUBLs0hmFC8ahjZLhx61boz3riT5OvuioAbHghNofRSo6TKHaA8IqipEromlyBrzC2I4Fx%2BeXOhM6FBCwNxaqXyqnRiq35aP6X0v8kZOva7cxxBmoPHKwaBYU1p0bLtFGmcpZhNgbxJ%2BWLpLXe%2FnTylcMdljkPUu6%2F9zMFUQyCg6gDAIcH5SuSt%2F%2BgVmVa6%2FSGIK1JimAv4wJWRMvE1PfUoDkzuLdXBTTGVQdlJFZyILkJywl7flpEifL2DLd4dhZ72V1n3eQ7V2z52p8NBi2D7Cs1vQu3dYAO5CjL9k%2B72rQ6m925CL7ifXZJ1%2B2DIl%2BCCDVtoz0cKsHBKWKg%2BTsQHfLTTesS38ugm6xD9KJ8K%2BvyYgcioufueR7eesXKzox70dQHVn30OwqONFn0YlrEU0Gg02jy5lsX7toAyQV9oB3z8jStid2bVVoKLkVqO7OE8ZL3TVGx2Pdu2b%2B9iQcdwTzSqgHG4QKRfyzii%2Fsp%2BTpjsbhE9zjAFpCtfI4%2Fry1K%2BPBvn42IQT%2F23vPn8XTsmYxYPKGfhziWcR5SnzJB1PJHPyYBCkulpbKNQhdNLVjNtWJCQed0Qg3lMGjxfuQjSwW3zXr5mBaT5RrmMPfQkb0GOqUBjFYmI0OZGhwQweXGyMvk1VzhNd5sbgCtcyYvz0cjFup8t5mCWHT5O6R3HNBukwZIadFtI8CPwJTwDvEO2MeQ%2FhhXPF%2Fft9YZAATnN%2FVkRREJUL7ISuJo7YS%2FJvI0ZIKiafRP16ZdRcPEY3vh6vOWjB%2BPZLT8VwyS%2BqObAC4sCE5euQx%2FPJgjKASUq9C8kEBMbKuqKp5x1neAXXW9JYJ%2BRZWRftkc&X-Amz-Signature=c584f7df2de547fc815a07243ba15bc225ef1e535ed50ed25d659c86f8fa3a70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IM254BP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD%2Bqg1zvZTMMYqOA8dZGb5fu%2FVjUdpCvvSPmRJZySEWBwIgCkP0kys8DNBjPKmX4booSsWNtHMmRMPWBv%2Bsi2LUS%2F4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDAd%2BZnBdtlZqrr29gyrcA3qMc%2F9PQHg1OnqG9D7QlwFUBLs0hmFC8ahjZLhx61boz3riT5OvuioAbHghNofRSo6TKHaA8IqipEromlyBrzC2I4Fx%2BeXOhM6FBCwNxaqXyqnRiq35aP6X0v8kZOva7cxxBmoPHKwaBYU1p0bLtFGmcpZhNgbxJ%2BWLpLXe%2FnTylcMdljkPUu6%2F9zMFUQyCg6gDAIcH5SuSt%2F%2BgVmVa6%2FSGIK1JimAv4wJWRMvE1PfUoDkzuLdXBTTGVQdlJFZyILkJywl7flpEifL2DLd4dhZ72V1n3eQ7V2z52p8NBi2D7Cs1vQu3dYAO5CjL9k%2B72rQ6m925CL7ifXZJ1%2B2DIl%2BCCDVtoz0cKsHBKWKg%2BTsQHfLTTesS38ugm6xD9KJ8K%2BvyYgcioufueR7eesXKzox70dQHVn30OwqONFn0YlrEU0Gg02jy5lsX7toAyQV9oB3z8jStid2bVVoKLkVqO7OE8ZL3TVGx2Pdu2b%2B9iQcdwTzSqgHG4QKRfyzii%2Fsp%2BTpjsbhE9zjAFpCtfI4%2Fry1K%2BPBvn42IQT%2F23vPn8XTsmYxYPKGfhziWcR5SnzJB1PJHPyYBCkulpbKNQhdNLVjNtWJCQed0Qg3lMGjxfuQjSwW3zXr5mBaT5RrmMPfQkb0GOqUBjFYmI0OZGhwQweXGyMvk1VzhNd5sbgCtcyYvz0cjFup8t5mCWHT5O6R3HNBukwZIadFtI8CPwJTwDvEO2MeQ%2FhhXPF%2Fft9YZAATnN%2FVkRREJUL7ISuJo7YS%2FJvI0ZIKiafRP16ZdRcPEY3vh6vOWjB%2BPZLT8VwyS%2BqObAC4sCE5euQx%2FPJgjKASUq9C8kEBMbKuqKp5x1neAXXW9JYJ%2BRZWRftkc&X-Amz-Signature=c62128ae4fd07e2c0add3110e4a96549c445ddd10e6b0b50516c787b0409946b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IM254BP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD%2Bqg1zvZTMMYqOA8dZGb5fu%2FVjUdpCvvSPmRJZySEWBwIgCkP0kys8DNBjPKmX4booSsWNtHMmRMPWBv%2Bsi2LUS%2F4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDAd%2BZnBdtlZqrr29gyrcA3qMc%2F9PQHg1OnqG9D7QlwFUBLs0hmFC8ahjZLhx61boz3riT5OvuioAbHghNofRSo6TKHaA8IqipEromlyBrzC2I4Fx%2BeXOhM6FBCwNxaqXyqnRiq35aP6X0v8kZOva7cxxBmoPHKwaBYU1p0bLtFGmcpZhNgbxJ%2BWLpLXe%2FnTylcMdljkPUu6%2F9zMFUQyCg6gDAIcH5SuSt%2F%2BgVmVa6%2FSGIK1JimAv4wJWRMvE1PfUoDkzuLdXBTTGVQdlJFZyILkJywl7flpEifL2DLd4dhZ72V1n3eQ7V2z52p8NBi2D7Cs1vQu3dYAO5CjL9k%2B72rQ6m925CL7ifXZJ1%2B2DIl%2BCCDVtoz0cKsHBKWKg%2BTsQHfLTTesS38ugm6xD9KJ8K%2BvyYgcioufueR7eesXKzox70dQHVn30OwqONFn0YlrEU0Gg02jy5lsX7toAyQV9oB3z8jStid2bVVoKLkVqO7OE8ZL3TVGx2Pdu2b%2B9iQcdwTzSqgHG4QKRfyzii%2Fsp%2BTpjsbhE9zjAFpCtfI4%2Fry1K%2BPBvn42IQT%2F23vPn8XTsmYxYPKGfhziWcR5SnzJB1PJHPyYBCkulpbKNQhdNLVjNtWJCQed0Qg3lMGjxfuQjSwW3zXr5mBaT5RrmMPfQkb0GOqUBjFYmI0OZGhwQweXGyMvk1VzhNd5sbgCtcyYvz0cjFup8t5mCWHT5O6R3HNBukwZIadFtI8CPwJTwDvEO2MeQ%2FhhXPF%2Fft9YZAATnN%2FVkRREJUL7ISuJo7YS%2FJvI0ZIKiafRP16ZdRcPEY3vh6vOWjB%2BPZLT8VwyS%2BqObAC4sCE5euQx%2FPJgjKASUq9C8kEBMbKuqKp5x1neAXXW9JYJ%2BRZWRftkc&X-Amz-Signature=b7918cd2dbaa42b05d2d38e24368c1605e081ac7cbf1112e14e71073973afcbc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZBO5XBE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCCit%2FoS6M7v%2Fzo67IbG0%2FsPVUfVXQn%2B1TF36HNbmwAmQIgMkuTDhY1CeWovWpS1rRz494xR41fDLRylSd1XUenFYEq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDOYmgezPfTqfX5vLjircAy%2FqaJgKw%2FguPPTfhCxwLS5SzlhrXGPmWkIXiMMbscgHaeoqWaj5%2BoY40sbfyzUResNNP3MMsMGhbDNUwn1uSzG%2FyMEzwNUQ0ASJAgxXUDKZ4kIMzjpUY8tDQUSRLW4WrINFjmTVIkOY67EHsX%2FBO0e3GQ7uQuT%2BRcvb1YsIGPCKC%2FKdXKnTXEOG6suK8GejWNcMKE6VRGCuVko1vDhHrA6IbzpSMid4huAcxhElag8suL36R3olLzIa5gqg5il835pV1cE4xVoSS0fpylsVdU%2FK6InRmL%2F0%2FjmfRnfOC%2Ba1n9LBdheIgYGSMfX7uyqd2cmcMz8fvBs3EdsZtgiRuijHkkVTivFlYDw0hPqf1wK0z7C1A8bZ9XMclGSnzHjebmNSFCyzQv8L8BKKmfnSFuOWYoZ2n4mCiV49NpPZwC9sMDPabT%2BjaM2H%2BHsi9f7saKnjJYU2OwyE84MkZQ9YKZzogLn19BOBwA7EkSyxao1SVTNIPspH1eXuztyL8om9Ohu6zOkV15SFPpLipM8P%2Fr%2FVIltFNJvRurz1MIvlDPwcOIrvgu1rtbEbB%2F3uQDRL8bl1WtC6Eu165eyr5a0Np57QfWw4AOwD%2FJzysXdh3MH2Q3UCRD78FstX3AevMNPRkb0GOqUBwqR9S8WEXvm2oq%2FdaLYQbbLsP%2F%2BEj%2BNkuakulFpkmxKDn3WfuVrXQYL0Bz1OE7GWSQgNTsOqACBV%2BS6kYAOfiNbTnFkKNqUh6fC2SgUYp0SK5pVbBf2%2FcPjzHEn18MWoZP4jhxom4E%2FPKf7wv5%2BzH2KNTnKcMpicGU9mNIfzTWMk5Q13foGVFToQt0F7UkphnEUuVunha9MmFPZWx8BhEkJYleOP&X-Amz-Signature=d7a5dd917090f957dec05e98a3ba5b3b15507a85a693c388d7c668b298d23139&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y45F4IHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCwyuW76%2FB3NVJqQZn8Oe8vclQFT5K%2FbjjJuPGJ4JOcrAIhANobJIzakKPJLkZpEXCCWho4%2Bff%2F26w6a0xQ4MEWw%2BFRKv8DCFkQABoMNjM3NDIzMTgzODA1Igxfs9xlYoHvRyMm19Uq3AOaOr6S%2BKgWSGv2lMPpxTYUqoE4DbjPt%2FnvMDJIfyzenambLSmExO36KbqZ4zbAdOsA0TYIZoZ%2FUNveEGbHySFFJAx3dfgHYYto755Hybe97xIpjZ2sOoFBMYEcXD8wcNx7NNKKpl5sRQFO7VaIoFVUiUitTeBsHF0n%2BcCdlI44POn5zTlDxXOAvUukBjh5xlya49fxwWWtZp7jtHcmk8Fk7WqbPaoXvw0CALotucZ3%2F1hf9%2FL1isaUUyW0khCsU5WX4c2qTYc69iiRV5wfTNhzPYrot88I6f2xM1rcxMfwJ4YNJW%2Fk%2FdpfqnDePVnkvbML4s%2Fic2axgnpsquOjE4DRMnZaw4MULJYxwe8MLCRU2BUSFbO0TsBpE5otLE%2FIyxHioTTzL1WNCJsxBWZnu1IKR71vLb%2FfHIS15FEvP70QZFUh2faftPJ%2BdVaVeR0nr%2F3Opc1i4ZospJU6rE6YpUIIcrvBRphfKjiYWZGsuqNUoqrONq93JFn65Wzu2PcUBwDqbZ%2B1E8NX9i1HCWQ9nA3xkK3ZRsvjzDNc1q4BHR%2F%2BVWf9wfKiQc7vLbgNIiBSgt02ADBw5%2BGgJqOyofT8TL3Mli4pNfpYcV9iXa0uSYsIrRDSBU3hOH81abQ88DDV0ZG9BjqkAdH5eFBpRXvnsZiHRL6x1VMLiyYLs4hCwUqwmJ6p4U%2B1cAtf%2F6TapfnjHEouPjcONDWjc0bf%2BhPjI352MH0nYjlk5reJ1UhKQzo1l%2FHjnG6qKkN20RkshWuG8bHuwVTu204%2Fm4twrmtfpwKDGHtZg6uya4YFPMrNHYI9jDXF0HTPhNRHyQYQG2pWfuw22L9MnEAzVje0Wx%2F%2BmAPAsi3r4ac2bKHQ&X-Amz-Signature=68396b1e8bd9385b442d57cf22a9adade47fd9851a08441329317fa996129b2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IM254BP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD%2Bqg1zvZTMMYqOA8dZGb5fu%2FVjUdpCvvSPmRJZySEWBwIgCkP0kys8DNBjPKmX4booSsWNtHMmRMPWBv%2Bsi2LUS%2F4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDAd%2BZnBdtlZqrr29gyrcA3qMc%2F9PQHg1OnqG9D7QlwFUBLs0hmFC8ahjZLhx61boz3riT5OvuioAbHghNofRSo6TKHaA8IqipEromlyBrzC2I4Fx%2BeXOhM6FBCwNxaqXyqnRiq35aP6X0v8kZOva7cxxBmoPHKwaBYU1p0bLtFGmcpZhNgbxJ%2BWLpLXe%2FnTylcMdljkPUu6%2F9zMFUQyCg6gDAIcH5SuSt%2F%2BgVmVa6%2FSGIK1JimAv4wJWRMvE1PfUoDkzuLdXBTTGVQdlJFZyILkJywl7flpEifL2DLd4dhZ72V1n3eQ7V2z52p8NBi2D7Cs1vQu3dYAO5CjL9k%2B72rQ6m925CL7ifXZJ1%2B2DIl%2BCCDVtoz0cKsHBKWKg%2BTsQHfLTTesS38ugm6xD9KJ8K%2BvyYgcioufueR7eesXKzox70dQHVn30OwqONFn0YlrEU0Gg02jy5lsX7toAyQV9oB3z8jStid2bVVoKLkVqO7OE8ZL3TVGx2Pdu2b%2B9iQcdwTzSqgHG4QKRfyzii%2Fsp%2BTpjsbhE9zjAFpCtfI4%2Fry1K%2BPBvn42IQT%2F23vPn8XTsmYxYPKGfhziWcR5SnzJB1PJHPyYBCkulpbKNQhdNLVjNtWJCQed0Qg3lMGjxfuQjSwW3zXr5mBaT5RrmMPfQkb0GOqUBjFYmI0OZGhwQweXGyMvk1VzhNd5sbgCtcyYvz0cjFup8t5mCWHT5O6R3HNBukwZIadFtI8CPwJTwDvEO2MeQ%2FhhXPF%2Fft9YZAATnN%2FVkRREJUL7ISuJo7YS%2FJvI0ZIKiafRP16ZdRcPEY3vh6vOWjB%2BPZLT8VwyS%2BqObAC4sCE5euQx%2FPJgjKASUq9C8kEBMbKuqKp5x1neAXXW9JYJ%2BRZWRftkc&X-Amz-Signature=069d477eb39ed56f366df67e2e620657c628490889a7dfb7a9709a4cd81bcf92&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IM254BP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD%2Bqg1zvZTMMYqOA8dZGb5fu%2FVjUdpCvvSPmRJZySEWBwIgCkP0kys8DNBjPKmX4booSsWNtHMmRMPWBv%2Bsi2LUS%2F4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDAd%2BZnBdtlZqrr29gyrcA3qMc%2F9PQHg1OnqG9D7QlwFUBLs0hmFC8ahjZLhx61boz3riT5OvuioAbHghNofRSo6TKHaA8IqipEromlyBrzC2I4Fx%2BeXOhM6FBCwNxaqXyqnRiq35aP6X0v8kZOva7cxxBmoPHKwaBYU1p0bLtFGmcpZhNgbxJ%2BWLpLXe%2FnTylcMdljkPUu6%2F9zMFUQyCg6gDAIcH5SuSt%2F%2BgVmVa6%2FSGIK1JimAv4wJWRMvE1PfUoDkzuLdXBTTGVQdlJFZyILkJywl7flpEifL2DLd4dhZ72V1n3eQ7V2z52p8NBi2D7Cs1vQu3dYAO5CjL9k%2B72rQ6m925CL7ifXZJ1%2B2DIl%2BCCDVtoz0cKsHBKWKg%2BTsQHfLTTesS38ugm6xD9KJ8K%2BvyYgcioufueR7eesXKzox70dQHVn30OwqONFn0YlrEU0Gg02jy5lsX7toAyQV9oB3z8jStid2bVVoKLkVqO7OE8ZL3TVGx2Pdu2b%2B9iQcdwTzSqgHG4QKRfyzii%2Fsp%2BTpjsbhE9zjAFpCtfI4%2Fry1K%2BPBvn42IQT%2F23vPn8XTsmYxYPKGfhziWcR5SnzJB1PJHPyYBCkulpbKNQhdNLVjNtWJCQed0Qg3lMGjxfuQjSwW3zXr5mBaT5RrmMPfQkb0GOqUBjFYmI0OZGhwQweXGyMvk1VzhNd5sbgCtcyYvz0cjFup8t5mCWHT5O6R3HNBukwZIadFtI8CPwJTwDvEO2MeQ%2FhhXPF%2Fft9YZAATnN%2FVkRREJUL7ISuJo7YS%2FJvI0ZIKiafRP16ZdRcPEY3vh6vOWjB%2BPZLT8VwyS%2BqObAC4sCE5euQx%2FPJgjKASUq9C8kEBMbKuqKp5x1neAXXW9JYJ%2BRZWRftkc&X-Amz-Signature=7c44a96b7c1148d5bc0e79ad07ec81f4fb0ee6b42ae5c808f0780f0bb620d97f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IM254BP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD%2Bqg1zvZTMMYqOA8dZGb5fu%2FVjUdpCvvSPmRJZySEWBwIgCkP0kys8DNBjPKmX4booSsWNtHMmRMPWBv%2Bsi2LUS%2F4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDAd%2BZnBdtlZqrr29gyrcA3qMc%2F9PQHg1OnqG9D7QlwFUBLs0hmFC8ahjZLhx61boz3riT5OvuioAbHghNofRSo6TKHaA8IqipEromlyBrzC2I4Fx%2BeXOhM6FBCwNxaqXyqnRiq35aP6X0v8kZOva7cxxBmoPHKwaBYU1p0bLtFGmcpZhNgbxJ%2BWLpLXe%2FnTylcMdljkPUu6%2F9zMFUQyCg6gDAIcH5SuSt%2F%2BgVmVa6%2FSGIK1JimAv4wJWRMvE1PfUoDkzuLdXBTTGVQdlJFZyILkJywl7flpEifL2DLd4dhZ72V1n3eQ7V2z52p8NBi2D7Cs1vQu3dYAO5CjL9k%2B72rQ6m925CL7ifXZJ1%2B2DIl%2BCCDVtoz0cKsHBKWKg%2BTsQHfLTTesS38ugm6xD9KJ8K%2BvyYgcioufueR7eesXKzox70dQHVn30OwqONFn0YlrEU0Gg02jy5lsX7toAyQV9oB3z8jStid2bVVoKLkVqO7OE8ZL3TVGx2Pdu2b%2B9iQcdwTzSqgHG4QKRfyzii%2Fsp%2BTpjsbhE9zjAFpCtfI4%2Fry1K%2BPBvn42IQT%2F23vPn8XTsmYxYPKGfhziWcR5SnzJB1PJHPyYBCkulpbKNQhdNLVjNtWJCQed0Qg3lMGjxfuQjSwW3zXr5mBaT5RrmMPfQkb0GOqUBjFYmI0OZGhwQweXGyMvk1VzhNd5sbgCtcyYvz0cjFup8t5mCWHT5O6R3HNBukwZIadFtI8CPwJTwDvEO2MeQ%2FhhXPF%2Fft9YZAATnN%2FVkRREJUL7ISuJo7YS%2FJvI0ZIKiafRP16ZdRcPEY3vh6vOWjB%2BPZLT8VwyS%2BqObAC4sCE5euQx%2FPJgjKASUq9C8kEBMbKuqKp5x1neAXXW9JYJ%2BRZWRftkc&X-Amz-Signature=4fc80acae56210e823fc451008da86f929904c9804ecf1f7e33cb99724180bbd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWETKBP4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIA1YFx4f7ckzLwtJ3r%2FjPt%2FnovsPRrfBEkpM4K0OaMMLAiEA8RyCJMDvvOpmf3umYAaabSpBqIF5nZ6fjjuwnrn52Rgq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDAkNgsde72bj%2B8o1SCrcA4i7KD2bf%2FRDCjtNIqhseY7BX1b5hUaBCwWoyQtuloSIbYh6xRAG%2BuS8b9MJi18CaXAMZNSpqS%2B8qdNclnL9e3i9Z9o0WMgO1gyOaWAcbH6nRQMbLzdmCQTBnaDTvuyBBt7083fB%2Fljgsb%2BGBlchr5ODV1h97C2A5IjWG8WCgHeD8onHlP%2F%2FytNwYbumUkKGXMnBHiqiyY8q8N55HXiWPINzNga2i8v%2FxM%2FvzSbsO10PtKBrLxbHqAv%2FOtI0ItJYZPuS9ZuKyFJdZyn3W%2F3JKzZ7PEsj56fUlWTB4rFEiX4Ted7l8ndVAZSOGnx5duCsFsWL%2BJTXxp73BT9oXxJRHpByGn8N0bQtKKWJ1KGg3t220vQ2K60%2Fin%2Fmm4OhKSYUsrnJ7E0z6tKmrfpd%2BzPApQo%2B1Ocl0F5zR7hGnWaf6QJb8n91MOJndoY8aiGES2WDnBAc9pBJpla8JqTjsyV9xHFW7nucNZOYF%2FRHDJ%2FDZfNIrw7T0gpucOqdqf7iO5uyjaW3Z2y7YBvJCUSjVhiQbocRGDGKv6%2BifAParZAjcuj88RxDMKaPW3tCjByac9M%2B6bKwZWLDR%2FfSytMFM%2B8FZGLf5Pd0jjVqG3orN9HqAL%2ByyOrqVBqkdQ%2BX50gNMMrRkb0GOqUBNI4c%2BFU5OWQqRWkSzh7RqOPYd5qYs8MRIY8O970nQ8G9pj6y6Xgcei3Btd5cYMnUpnfj0aPDJrBPZdyIPDYwAO%2Bvzp%2F3EwKCEBZo2Y8DtKotTntp%2BkWMV%2BnFJm6p7GNJqEsv9%2F2AZDsgFXRUVcmmkiq0vxUfeRkkwRmA3%2FLPTCHiZNFFXrbviZtTG%2FE5lTa72SC0aPfm9nZOyxWv2q4HTcq2de%2Bw&X-Amz-Signature=76a2fb9a2f9a10b8ced9a86d0ea3999bcc2aaae868a60c00c9831e98c60703c2&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664F65KHNZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD%2BfMbL0tdVyow7cdZ%2FEnk5CJpaTUPeXAGe0JgJDHSvmAIgI6ecgUCiAB2kSZEwjf64%2B7dlvYCfus%2FXKC6%2BphO5%2Bbsq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDPESokll%2B0O0mrvTEyrcA7qWoVl9iDNRY2sX%2F5Ua54yAxOwoqRbe%2BYFblFnB5EoDOQzbqo8R72ky81oYzrVLRjhLGjo1cdH8dDBk4EtWjp9fVgZwokqLaTgiFM3rsKIxyjpao7QUVc%2BskRB%2F6EhFANoDgS5YqJ5HZnZf%2F0qjYFGPChPBfbI6jWmYFUlxW1ZifokM4YlTsmSqfqILSFBT75spVz4DGvUzDuunDorQzS2hRdYZQKQpsho0u2%2FUC4eTI3AxG1LsxMR%2BbAY1ar4VF7gPg1f93dDJiTsGvTJRiPn0xNfqEqAIhvqmRNPIBYT406ZbrNvCCMMzt2om1Z5qtJu22vz4PGtDW07w0wP%2B%2BI3x6u3%2FA914jk2XXaxXe5ahk1H%2BCv6MqAcTkddKHw6O36jW3Vo9eokBGVIaIHUc%2BQcQ6SDh9CXg8566aAASzCTZ7xowe7DOqdGMkfdVJTLOGHjBpQj4xYDiwTgYN1ATKaETINpERyx8t4ac9v4aykaAs7Jo2R%2F3pu0Mx8mZsU6mY8BKEoERr5yWcpCoEo%2FE1ZWsAZcZ8aCmpF9QqJWXrSpwwJ03tFnjw0UapX86c%2B0s6GhoXrmqft%2FCWYt%2FGCcURjkVCKozPvsQqNjL%2BpFjz2jGBVLjocUz8YuoY0dsMInRkb0GOqUBsQMeWcVU6ZgWpJi2D6ZlburBE4YriP%2B9LbeNywBS33D6a9K8l%2BqqftCk1XgkBzwctCr6Z33i7AR%2F43Ahu0WrsrtCP6gnglaPuVU0TT2S%2BMVueMJn%2Bnqssn0OM8VvfoQVBCr7phiswbWQQ38EwZ4xxYZGDjmnEKEAE9sZAGMfzybV052%2BmMJ25SmLCyjZPYpgWW65xgES2i5jbv5hjngMhJZw3pUQ&X-Amz-Signature=88452ce01dbb1194df654a55fd4fad257cf66d65f1d537c5e44798a11814248c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK2RP4FG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIDmY94RALKEjQhtYgopILL%2FmwvPofeUUCKwfJoSVb3F%2BAiEA3KT9V9fhub4j5JrSRxlgO6fj0nOWadygFj7nzN4RAUYq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDGsRW4KgWz%2BVaa4lSircA9KgD2GWqS6SSV%2BXXyUeLOw3dRrWhM6QV%2BEcpGRvMzTW3eZonci9zlJUgjZIUtjkGaJybgwiADXTT0fLjm0dFhbNFyzvqWPFFqzarObPWeYXKJfXebtOYJYksjGZrDbKkgeuZFRbOX5lOl4Y9O2MeOxrIEIVm%2BFtBNUCgV5OD0FUyi1RmyFn8uYB1cr35miP1Rv34DJSEOaodtCNMSChIddY9nJCxHuNf%2BWLV9Cd2xtEJn2S1573Jqfk1RopPfR2xDeStlO%2BEhXJ57iM%2BjFO45Em2t9RBKSbCSgW3udVwfPulKMb6MSo7KjFehBY55XtC%2F9D%2FXXUb8P0gzGBG1vU0kBYSFR9THYVuXNaJExvuSz6eEAuoX42Q2ioJvQGLs27TdJINVG7A2%2FAnpV3paDUm9b%2FyJbESqaN1dGQfFn1U2GAQBnPd2zKfb4YWkfZxnCh8FDQp%2B%2F9Dt92Q04sqxrWTtvYxzTaTboEDfZGKbyCG2Fn%2FXdZ9k7Ho73xHgtS%2BxWk0aBzPRpwVEvk%2BzDGCQPc8%2BONW%2F3MKgwOIas323j7Or9kJrDmIGpjGQxb1g7vXW2KDXPBVsHd2kW18SITAznubOPjjvyV33zeCmJlDOQmLEJMtqLvQ7cRY0DxcixxMJrRkb0GOqUBrdDuMbKALrVTEuBkap6hndgrbSr%2FN%2BI9xCM2SAyqEqmMygENcMzCG%2FKB0k7V%2FZAYQeeqJKfYhZucwxrrjX4boEb16%2BGTX5L2tWnw5TwHe8PNqnl0cxzqtylLDT9bP63r7N8TAr5gk16opUur8HIpW%2BSjfncL%2FUttqp8PUZKZuABn6UrRhrJUUAD9THe1LaDt%2FcaWONilRE5N9cD5tO927khAXLcL&X-Amz-Signature=e8fb608cd3ef476d0bfd0d6de627e1947d51ae065a86ad7db867ce90e2724fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRWA3TYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIB8xeNy7TRrrF8TaL6Ce4kd6QPR7OPz%2FbxrTXO5wvxvMAiAbI2g5Jc1W%2Fna34NPZcxC%2F71hske9CnKHZ4D83gfu8YCr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMpac3VUDTxHLadhb4KtwDtHGOpN28XTUo5joYsn6h9iH9WbUMtytywLP3Ma3VZAs0%2BBkEdINyx9VnP9X9d5EENsUG06RLqD9VTz1pgEzbt0bxdeoZVcCtfr3KZdAcGpf5h7B%2FZSvDvzTRiiZrTEmI4EW%2FJu9xu%2Bjfk4y4kpOCzTlq%2B28Nc%2FsjPIuQqEaBAdqkO0XXO%2B2Td9UK4q25YDt0Ndy8XtBo1jbtWTn2aQb7Q5OP1t7kC6Tw6Sk75AH7Y%2BanSU91g1yYX%2BXizTj5MHCs%2BKrcICvhOu6amDF%2B2AtJaJIx4Nqq6H2ALYAwNLRxMo51CltFKRIRA1GX8g2eog5ZfchDgoKYbTzbpsOdNQdDGfthxtqD83Z8G%2B3UbLoyQvUPnhwfZo91RWggqqiVcbHqfv%2FDutmSSeDW7VZLU8a1oIIzq8oTakA5SKx%2Buec041CEtJiHyzbHJhTpazljQy8wjDzDJJx0MS8zes18JFO7UzyrhLaYUWOfFpuFVBdQ5vQhv20xGJ6pYXfI%2F5oNRU56301JSgx7RJXSoA%2F8egyefnxHiad0giDs%2Fb6uCtDhvCWaWXhC6pbsoYSZr5Y8t%2FQlC1%2FZztbAh6XolJty1aEbr8SKrqZc6DHB6lHAO46ZzG1HrAwAtjLIC1TxMyMw2NGRvQY6pgF6NPAhc8C8uCgaOeIGHzImBycujB7EQ3zhKz882t5VovJePJnpzWbXkUZnlvVwSXX6EV%2Fnn0bet%2BpVgP7Lo6P7WUMENbWVSdhh0JlDxDRpClVO3iuIl8Chwsw7%2B%2Fiw53iDgKWzovi8fzrx3J8DSZ5y2Y9GXnrEWdxX2JnAP6W7SPVNLGkAey%2BrBX%2FYzXpo8d0zSpk%2BFDbwOBmLmykmJyFtjYUxs7bQ&X-Amz-Signature=9b22e4263438e3623e57e59fb5169cbc1b099acc3c94c6088d39d23c13ec6de1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRWA3TYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIB8xeNy7TRrrF8TaL6Ce4kd6QPR7OPz%2FbxrTXO5wvxvMAiAbI2g5Jc1W%2Fna34NPZcxC%2F71hske9CnKHZ4D83gfu8YCr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMpac3VUDTxHLadhb4KtwDtHGOpN28XTUo5joYsn6h9iH9WbUMtytywLP3Ma3VZAs0%2BBkEdINyx9VnP9X9d5EENsUG06RLqD9VTz1pgEzbt0bxdeoZVcCtfr3KZdAcGpf5h7B%2FZSvDvzTRiiZrTEmI4EW%2FJu9xu%2Bjfk4y4kpOCzTlq%2B28Nc%2FsjPIuQqEaBAdqkO0XXO%2B2Td9UK4q25YDt0Ndy8XtBo1jbtWTn2aQb7Q5OP1t7kC6Tw6Sk75AH7Y%2BanSU91g1yYX%2BXizTj5MHCs%2BKrcICvhOu6amDF%2B2AtJaJIx4Nqq6H2ALYAwNLRxMo51CltFKRIRA1GX8g2eog5ZfchDgoKYbTzbpsOdNQdDGfthxtqD83Z8G%2B3UbLoyQvUPnhwfZo91RWggqqiVcbHqfv%2FDutmSSeDW7VZLU8a1oIIzq8oTakA5SKx%2Buec041CEtJiHyzbHJhTpazljQy8wjDzDJJx0MS8zes18JFO7UzyrhLaYUWOfFpuFVBdQ5vQhv20xGJ6pYXfI%2F5oNRU56301JSgx7RJXSoA%2F8egyefnxHiad0giDs%2Fb6uCtDhvCWaWXhC6pbsoYSZr5Y8t%2FQlC1%2FZztbAh6XolJty1aEbr8SKrqZc6DHB6lHAO46ZzG1HrAwAtjLIC1TxMyMw2NGRvQY6pgF6NPAhc8C8uCgaOeIGHzImBycujB7EQ3zhKz882t5VovJePJnpzWbXkUZnlvVwSXX6EV%2Fnn0bet%2BpVgP7Lo6P7WUMENbWVSdhh0JlDxDRpClVO3iuIl8Chwsw7%2B%2Fiw53iDgKWzovi8fzrx3J8DSZ5y2Y9GXnrEWdxX2JnAP6W7SPVNLGkAey%2BrBX%2FYzXpo8d0zSpk%2BFDbwOBmLmykmJyFtjYUxs7bQ&X-Amz-Signature=1702386d92e4e83bd4680d60fe1c9f04d7303146ca233db33378b6376a5e2dd3&X-Amz-SignedHeaders=host&x-id=GetObject)

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
