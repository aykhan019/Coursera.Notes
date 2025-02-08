

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYGW623O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCICmOwSfZl%2BzfA9JaUwhpcNBlrOyg1xGvLALDjCxtuc%2BQAiBkFLXcf%2BUB2Cf7AvDzzQyd%2FYnHozOqQQJ4MWmEjHX3wiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCUEr4urOUXuNRZcfKtwDQIzCMRMaRuK2sldWKtxOzlguo6uBQxKCBICldDQllRtu%2FR41nLtVEjr3x7xNLGdUisMF9LW%2BUbww1sjzoL3P79FvFPKZToSDHXI4ws2fNVLpCRO%2FwbCtheQfYPvu%2BHZnPToWIysSBpAdD9AJqICShOSBFsRpoXIgI9br2dw4Lt7hJF0FZ%2FMm4epPC1TN48YRQbz3avHjWkM6I4NtA0frk9Iy77YvuKdVaLN4%2BRLbfPqZlsLoJscAzvfL0jgV5bgoSNBJxv49LBliPZnjoD1WZOSN4%2BPjNbbeK%2FBPXXLMP0Crh3g3EmmO9ezkapg0rMcesTp83cz1DsIszN5fxzEqDn46nX1ualUk3FwhPBqUvyjfzOI9ZoD5DtTi%2B6V09%2B63LiYXpAXg%2BNdTWLyPvaozgSdJfEgl4sZznHhGxWzNRr0wA4lYkvuxhos1YYMSTAGQLTEJazeSh0vdHWT4C%2FY%2FS3laN52EO8KBHGH0tO1nsbt475SVpU6FLBDSaSxQgjc3WQcuUw%2FlRXNDHWfb8d7L7NX1CJ1jQw9xtqOYwICWYvSebbshNZc%2F6qnmdfQeCBIcNL%2Bk8tb97cLIRZk17IeJuaHqp0HJNMv620Ev%2BReb1lxBwBO6wQlvcm0eIp4wx76avQY6pgFcu1tL2wNdoRgF7%2BJJWkTfD8ebKVkKvFwCYSGGJ0mGDQuboAaQeb7Gw2NXbHPIG6LNafx9g6b6vsn08Td4t4bUFM5tiDZFZD9nv7R2yosLksEA1HsVAC%2FWQ3%2BIZqxYhuMr3fo%2BjKreGhfx324VDL4XGM9zSliVaTbEhZP7BU4W%2Brv2ItrVa%2FnWf0DilXq0JYBUQDxBeFzJaFsT%2BJahq7yB43ewuAAp&X-Amz-Signature=c693052330061f43571ffaa52d6d87b5730065a2b18a98693cb28860d4bec089&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYGW623O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCICmOwSfZl%2BzfA9JaUwhpcNBlrOyg1xGvLALDjCxtuc%2BQAiBkFLXcf%2BUB2Cf7AvDzzQyd%2FYnHozOqQQJ4MWmEjHX3wiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCUEr4urOUXuNRZcfKtwDQIzCMRMaRuK2sldWKtxOzlguo6uBQxKCBICldDQllRtu%2FR41nLtVEjr3x7xNLGdUisMF9LW%2BUbww1sjzoL3P79FvFPKZToSDHXI4ws2fNVLpCRO%2FwbCtheQfYPvu%2BHZnPToWIysSBpAdD9AJqICShOSBFsRpoXIgI9br2dw4Lt7hJF0FZ%2FMm4epPC1TN48YRQbz3avHjWkM6I4NtA0frk9Iy77YvuKdVaLN4%2BRLbfPqZlsLoJscAzvfL0jgV5bgoSNBJxv49LBliPZnjoD1WZOSN4%2BPjNbbeK%2FBPXXLMP0Crh3g3EmmO9ezkapg0rMcesTp83cz1DsIszN5fxzEqDn46nX1ualUk3FwhPBqUvyjfzOI9ZoD5DtTi%2B6V09%2B63LiYXpAXg%2BNdTWLyPvaozgSdJfEgl4sZznHhGxWzNRr0wA4lYkvuxhos1YYMSTAGQLTEJazeSh0vdHWT4C%2FY%2FS3laN52EO8KBHGH0tO1nsbt475SVpU6FLBDSaSxQgjc3WQcuUw%2FlRXNDHWfb8d7L7NX1CJ1jQw9xtqOYwICWYvSebbshNZc%2F6qnmdfQeCBIcNL%2Bk8tb97cLIRZk17IeJuaHqp0HJNMv620Ev%2BReb1lxBwBO6wQlvcm0eIp4wx76avQY6pgFcu1tL2wNdoRgF7%2BJJWkTfD8ebKVkKvFwCYSGGJ0mGDQuboAaQeb7Gw2NXbHPIG6LNafx9g6b6vsn08Td4t4bUFM5tiDZFZD9nv7R2yosLksEA1HsVAC%2FWQ3%2BIZqxYhuMr3fo%2BjKreGhfx324VDL4XGM9zSliVaTbEhZP7BU4W%2Brv2ItrVa%2FnWf0DilXq0JYBUQDxBeFzJaFsT%2BJahq7yB43ewuAAp&X-Amz-Signature=b71919473aa984a10c19d12e2dc08ec9f7ef92114405d96f8f9c5a71e5362aa4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYGW623O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCICmOwSfZl%2BzfA9JaUwhpcNBlrOyg1xGvLALDjCxtuc%2BQAiBkFLXcf%2BUB2Cf7AvDzzQyd%2FYnHozOqQQJ4MWmEjHX3wiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCUEr4urOUXuNRZcfKtwDQIzCMRMaRuK2sldWKtxOzlguo6uBQxKCBICldDQllRtu%2FR41nLtVEjr3x7xNLGdUisMF9LW%2BUbww1sjzoL3P79FvFPKZToSDHXI4ws2fNVLpCRO%2FwbCtheQfYPvu%2BHZnPToWIysSBpAdD9AJqICShOSBFsRpoXIgI9br2dw4Lt7hJF0FZ%2FMm4epPC1TN48YRQbz3avHjWkM6I4NtA0frk9Iy77YvuKdVaLN4%2BRLbfPqZlsLoJscAzvfL0jgV5bgoSNBJxv49LBliPZnjoD1WZOSN4%2BPjNbbeK%2FBPXXLMP0Crh3g3EmmO9ezkapg0rMcesTp83cz1DsIszN5fxzEqDn46nX1ualUk3FwhPBqUvyjfzOI9ZoD5DtTi%2B6V09%2B63LiYXpAXg%2BNdTWLyPvaozgSdJfEgl4sZznHhGxWzNRr0wA4lYkvuxhos1YYMSTAGQLTEJazeSh0vdHWT4C%2FY%2FS3laN52EO8KBHGH0tO1nsbt475SVpU6FLBDSaSxQgjc3WQcuUw%2FlRXNDHWfb8d7L7NX1CJ1jQw9xtqOYwICWYvSebbshNZc%2F6qnmdfQeCBIcNL%2Bk8tb97cLIRZk17IeJuaHqp0HJNMv620Ev%2BReb1lxBwBO6wQlvcm0eIp4wx76avQY6pgFcu1tL2wNdoRgF7%2BJJWkTfD8ebKVkKvFwCYSGGJ0mGDQuboAaQeb7Gw2NXbHPIG6LNafx9g6b6vsn08Td4t4bUFM5tiDZFZD9nv7R2yosLksEA1HsVAC%2FWQ3%2BIZqxYhuMr3fo%2BjKreGhfx324VDL4XGM9zSliVaTbEhZP7BU4W%2Brv2ItrVa%2FnWf0DilXq0JYBUQDxBeFzJaFsT%2BJahq7yB43ewuAAp&X-Amz-Signature=8b6d9cbf19ea16e097c36d9ca3d3ac20dbc118511ade106e396dbc48ef39888e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7DDEJP4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBDxjGBvkdEFxC8g2w66E22nXoSPNN5Za3mRGgHZausDAiBhqH%2BZLJYhoL15Y772STxAKgdoTYPjXV3MT9Vb6NgJOCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEio3BZLQYjtfpSfPKtwDVr1GW2T2ttCvt5u3%2FOgCglyZ5Ij%2Bnd7n3aXU%2FWWvNHoKSwglqcFHd65baX8NrHdtpbzsOsg%2BhqKFor51BXueX%2FZrN9QJLAie7T8l8EmUHtfH7o1K6cXntC88ofzglSMshfhUGSk%2FNDUwZH8cEfPArptvrllRfhAEPruiSiAEYEm3YEpCgtTmSlCgMwd9UMBzfwAJUphUw0wt5LCyG08YorgQetbE%2Fy1xRiuCyPhRAXeikAr573CSw6Qtw1eH3HBw%2BxfYtqznUL90EUSStvjHoTPbG7Fxron1U80uz9GoKG8eMT0rg2xEOsRPcl1TUiuaJORN9guBKqiCFAupfwlbpqr4jWfBP1NEigOvoJo%2BEIW%2BEEDGLbW%2B58DLsTW2h%2FQhsS%2Fgtw0fBTIoJqS1V2c6k6C%2FmCOiKwOCYEx26c%2BcIyXQjvsl912eO%2FxZr3VcpoTBxokAaop9Vkda3yigPOS4cjve0q%2FcfwRvf1iqBIMkOQTuqu7haUJxbCJ41FuvdNb2ZXynbOper1ENtdRffRDZdHstpQ3aBFbint3mnArkAnbm3J%2FPHXdDeAUGDbRYRfcfLGi05eZq5Z6D8Vdt5B8M4x93fJ65ViS9FLgGG2%2Fmxqd8p%2FjU0hgNGxMEzn8wpb6avQY6pgHmGjjFMlgE8YMCzU34hC5igfu83y4taYPUD%2BSrVWbZ%2BeD6izfRPfudx788C55zUVKmX5ab2v4Cma233QhUv7LEG9yuOWSmA8c8N07SDdEqXknbibRmudYY3brKrVTjkJojWpdTFDrswUsuWy1F218RtfBKIJ2I6q0jnaVPegYIPlw98WZy5AHkfDbQwiUFIFRgqs3wNQKbKJVXb4m80uZIhenqdVgD&X-Amz-Signature=92e0c44116bc922b7c6eae8dfd6422bbad66f3900183d7a687b9f0f964b75aa1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7DDEJP4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBDxjGBvkdEFxC8g2w66E22nXoSPNN5Za3mRGgHZausDAiBhqH%2BZLJYhoL15Y772STxAKgdoTYPjXV3MT9Vb6NgJOCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEio3BZLQYjtfpSfPKtwDVr1GW2T2ttCvt5u3%2FOgCglyZ5Ij%2Bnd7n3aXU%2FWWvNHoKSwglqcFHd65baX8NrHdtpbzsOsg%2BhqKFor51BXueX%2FZrN9QJLAie7T8l8EmUHtfH7o1K6cXntC88ofzglSMshfhUGSk%2FNDUwZH8cEfPArptvrllRfhAEPruiSiAEYEm3YEpCgtTmSlCgMwd9UMBzfwAJUphUw0wt5LCyG08YorgQetbE%2Fy1xRiuCyPhRAXeikAr573CSw6Qtw1eH3HBw%2BxfYtqznUL90EUSStvjHoTPbG7Fxron1U80uz9GoKG8eMT0rg2xEOsRPcl1TUiuaJORN9guBKqiCFAupfwlbpqr4jWfBP1NEigOvoJo%2BEIW%2BEEDGLbW%2B58DLsTW2h%2FQhsS%2Fgtw0fBTIoJqS1V2c6k6C%2FmCOiKwOCYEx26c%2BcIyXQjvsl912eO%2FxZr3VcpoTBxokAaop9Vkda3yigPOS4cjve0q%2FcfwRvf1iqBIMkOQTuqu7haUJxbCJ41FuvdNb2ZXynbOper1ENtdRffRDZdHstpQ3aBFbint3mnArkAnbm3J%2FPHXdDeAUGDbRYRfcfLGi05eZq5Z6D8Vdt5B8M4x93fJ65ViS9FLgGG2%2Fmxqd8p%2FjU0hgNGxMEzn8wpb6avQY6pgHmGjjFMlgE8YMCzU34hC5igfu83y4taYPUD%2BSrVWbZ%2BeD6izfRPfudx788C55zUVKmX5ab2v4Cma233QhUv7LEG9yuOWSmA8c8N07SDdEqXknbibRmudYY3brKrVTjkJojWpdTFDrswUsuWy1F218RtfBKIJ2I6q0jnaVPegYIPlw98WZy5AHkfDbQwiUFIFRgqs3wNQKbKJVXb4m80uZIhenqdVgD&X-Amz-Signature=77fd0df81aa6a2c41ffc014e08948f1cf4d2ef8ca6feb35627cd9045fe681926&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7DDEJP4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBDxjGBvkdEFxC8g2w66E22nXoSPNN5Za3mRGgHZausDAiBhqH%2BZLJYhoL15Y772STxAKgdoTYPjXV3MT9Vb6NgJOCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEio3BZLQYjtfpSfPKtwDVr1GW2T2ttCvt5u3%2FOgCglyZ5Ij%2Bnd7n3aXU%2FWWvNHoKSwglqcFHd65baX8NrHdtpbzsOsg%2BhqKFor51BXueX%2FZrN9QJLAie7T8l8EmUHtfH7o1K6cXntC88ofzglSMshfhUGSk%2FNDUwZH8cEfPArptvrllRfhAEPruiSiAEYEm3YEpCgtTmSlCgMwd9UMBzfwAJUphUw0wt5LCyG08YorgQetbE%2Fy1xRiuCyPhRAXeikAr573CSw6Qtw1eH3HBw%2BxfYtqznUL90EUSStvjHoTPbG7Fxron1U80uz9GoKG8eMT0rg2xEOsRPcl1TUiuaJORN9guBKqiCFAupfwlbpqr4jWfBP1NEigOvoJo%2BEIW%2BEEDGLbW%2B58DLsTW2h%2FQhsS%2Fgtw0fBTIoJqS1V2c6k6C%2FmCOiKwOCYEx26c%2BcIyXQjvsl912eO%2FxZr3VcpoTBxokAaop9Vkda3yigPOS4cjve0q%2FcfwRvf1iqBIMkOQTuqu7haUJxbCJ41FuvdNb2ZXynbOper1ENtdRffRDZdHstpQ3aBFbint3mnArkAnbm3J%2FPHXdDeAUGDbRYRfcfLGi05eZq5Z6D8Vdt5B8M4x93fJ65ViS9FLgGG2%2Fmxqd8p%2FjU0hgNGxMEzn8wpb6avQY6pgHmGjjFMlgE8YMCzU34hC5igfu83y4taYPUD%2BSrVWbZ%2BeD6izfRPfudx788C55zUVKmX5ab2v4Cma233QhUv7LEG9yuOWSmA8c8N07SDdEqXknbibRmudYY3brKrVTjkJojWpdTFDrswUsuWy1F218RtfBKIJ2I6q0jnaVPegYIPlw98WZy5AHkfDbQwiUFIFRgqs3wNQKbKJVXb4m80uZIhenqdVgD&X-Amz-Signature=30d8a38a10fac515f89910d3ffddefa5b982c27111466713932ce5e14fbe7868&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7DDEJP4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBDxjGBvkdEFxC8g2w66E22nXoSPNN5Za3mRGgHZausDAiBhqH%2BZLJYhoL15Y772STxAKgdoTYPjXV3MT9Vb6NgJOCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEio3BZLQYjtfpSfPKtwDVr1GW2T2ttCvt5u3%2FOgCglyZ5Ij%2Bnd7n3aXU%2FWWvNHoKSwglqcFHd65baX8NrHdtpbzsOsg%2BhqKFor51BXueX%2FZrN9QJLAie7T8l8EmUHtfH7o1K6cXntC88ofzglSMshfhUGSk%2FNDUwZH8cEfPArptvrllRfhAEPruiSiAEYEm3YEpCgtTmSlCgMwd9UMBzfwAJUphUw0wt5LCyG08YorgQetbE%2Fy1xRiuCyPhRAXeikAr573CSw6Qtw1eH3HBw%2BxfYtqznUL90EUSStvjHoTPbG7Fxron1U80uz9GoKG8eMT0rg2xEOsRPcl1TUiuaJORN9guBKqiCFAupfwlbpqr4jWfBP1NEigOvoJo%2BEIW%2BEEDGLbW%2B58DLsTW2h%2FQhsS%2Fgtw0fBTIoJqS1V2c6k6C%2FmCOiKwOCYEx26c%2BcIyXQjvsl912eO%2FxZr3VcpoTBxokAaop9Vkda3yigPOS4cjve0q%2FcfwRvf1iqBIMkOQTuqu7haUJxbCJ41FuvdNb2ZXynbOper1ENtdRffRDZdHstpQ3aBFbint3mnArkAnbm3J%2FPHXdDeAUGDbRYRfcfLGi05eZq5Z6D8Vdt5B8M4x93fJ65ViS9FLgGG2%2Fmxqd8p%2FjU0hgNGxMEzn8wpb6avQY6pgHmGjjFMlgE8YMCzU34hC5igfu83y4taYPUD%2BSrVWbZ%2BeD6izfRPfudx788C55zUVKmX5ab2v4Cma233QhUv7LEG9yuOWSmA8c8N07SDdEqXknbibRmudYY3brKrVTjkJojWpdTFDrswUsuWy1F218RtfBKIJ2I6q0jnaVPegYIPlw98WZy5AHkfDbQwiUFIFRgqs3wNQKbKJVXb4m80uZIhenqdVgD&X-Amz-Signature=6c5e166ec3842a5f432efdeb1dea8d6fc36bcc232afd01baab84a2b38dcbe91c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7DDEJP4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBDxjGBvkdEFxC8g2w66E22nXoSPNN5Za3mRGgHZausDAiBhqH%2BZLJYhoL15Y772STxAKgdoTYPjXV3MT9Vb6NgJOCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEio3BZLQYjtfpSfPKtwDVr1GW2T2ttCvt5u3%2FOgCglyZ5Ij%2Bnd7n3aXU%2FWWvNHoKSwglqcFHd65baX8NrHdtpbzsOsg%2BhqKFor51BXueX%2FZrN9QJLAie7T8l8EmUHtfH7o1K6cXntC88ofzglSMshfhUGSk%2FNDUwZH8cEfPArptvrllRfhAEPruiSiAEYEm3YEpCgtTmSlCgMwd9UMBzfwAJUphUw0wt5LCyG08YorgQetbE%2Fy1xRiuCyPhRAXeikAr573CSw6Qtw1eH3HBw%2BxfYtqznUL90EUSStvjHoTPbG7Fxron1U80uz9GoKG8eMT0rg2xEOsRPcl1TUiuaJORN9guBKqiCFAupfwlbpqr4jWfBP1NEigOvoJo%2BEIW%2BEEDGLbW%2B58DLsTW2h%2FQhsS%2Fgtw0fBTIoJqS1V2c6k6C%2FmCOiKwOCYEx26c%2BcIyXQjvsl912eO%2FxZr3VcpoTBxokAaop9Vkda3yigPOS4cjve0q%2FcfwRvf1iqBIMkOQTuqu7haUJxbCJ41FuvdNb2ZXynbOper1ENtdRffRDZdHstpQ3aBFbint3mnArkAnbm3J%2FPHXdDeAUGDbRYRfcfLGi05eZq5Z6D8Vdt5B8M4x93fJ65ViS9FLgGG2%2Fmxqd8p%2FjU0hgNGxMEzn8wpb6avQY6pgHmGjjFMlgE8YMCzU34hC5igfu83y4taYPUD%2BSrVWbZ%2BeD6izfRPfudx788C55zUVKmX5ab2v4Cma233QhUv7LEG9yuOWSmA8c8N07SDdEqXknbibRmudYY3brKrVTjkJojWpdTFDrswUsuWy1F218RtfBKIJ2I6q0jnaVPegYIPlw98WZy5AHkfDbQwiUFIFRgqs3wNQKbKJVXb4m80uZIhenqdVgD&X-Amz-Signature=61bb13e83ba42c61e42d8bbedcb2444c986d11f7200589b10e6991c754f101ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7DDEJP4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBDxjGBvkdEFxC8g2w66E22nXoSPNN5Za3mRGgHZausDAiBhqH%2BZLJYhoL15Y772STxAKgdoTYPjXV3MT9Vb6NgJOCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEio3BZLQYjtfpSfPKtwDVr1GW2T2ttCvt5u3%2FOgCglyZ5Ij%2Bnd7n3aXU%2FWWvNHoKSwglqcFHd65baX8NrHdtpbzsOsg%2BhqKFor51BXueX%2FZrN9QJLAie7T8l8EmUHtfH7o1K6cXntC88ofzglSMshfhUGSk%2FNDUwZH8cEfPArptvrllRfhAEPruiSiAEYEm3YEpCgtTmSlCgMwd9UMBzfwAJUphUw0wt5LCyG08YorgQetbE%2Fy1xRiuCyPhRAXeikAr573CSw6Qtw1eH3HBw%2BxfYtqznUL90EUSStvjHoTPbG7Fxron1U80uz9GoKG8eMT0rg2xEOsRPcl1TUiuaJORN9guBKqiCFAupfwlbpqr4jWfBP1NEigOvoJo%2BEIW%2BEEDGLbW%2B58DLsTW2h%2FQhsS%2Fgtw0fBTIoJqS1V2c6k6C%2FmCOiKwOCYEx26c%2BcIyXQjvsl912eO%2FxZr3VcpoTBxokAaop9Vkda3yigPOS4cjve0q%2FcfwRvf1iqBIMkOQTuqu7haUJxbCJ41FuvdNb2ZXynbOper1ENtdRffRDZdHstpQ3aBFbint3mnArkAnbm3J%2FPHXdDeAUGDbRYRfcfLGi05eZq5Z6D8Vdt5B8M4x93fJ65ViS9FLgGG2%2Fmxqd8p%2FjU0hgNGxMEzn8wpb6avQY6pgHmGjjFMlgE8YMCzU34hC5igfu83y4taYPUD%2BSrVWbZ%2BeD6izfRPfudx788C55zUVKmX5ab2v4Cma233QhUv7LEG9yuOWSmA8c8N07SDdEqXknbibRmudYY3brKrVTjkJojWpdTFDrswUsuWy1F218RtfBKIJ2I6q0jnaVPegYIPlw98WZy5AHkfDbQwiUFIFRgqs3wNQKbKJVXb4m80uZIhenqdVgD&X-Amz-Signature=79743295f16c570583e554135f29ec9063879c8785f29f04100136e68d8099d6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZY7YCMI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQD9dH5j27Xx4xWHbjwQqghfeqyuCwgoFzXMO8HOx7KVrwIgR0zWAuHuzHChiZwhoP6HxWikcKKX%2F4%2BdfXDs9t6DcN8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFqEASv4hejwbzk8%2FCrcA%2BbduHEh94h7ZMBbW2fqsAiIDbUyGNOzaSmleKnPb%2F5qWC%2BwH0RII7NZ6ap3d4jvg5nnBYC5aBhQyJ44qMncQUDZpdFXIHaBmZScNQGLW42d2O3%2B3hS77C%2FQLfMqdRZAHxvXNJVvJCeVRXWjK3EuAKOqYRAjtuXo71GrWIsOU5YDcmlkZcjZ%2FepoVnj0dMy9ozC%2B2kWIQG6JK69FG%2Bx7bUiJWX6V%2FXLhyhcClWlHq3C5Xyj6ALR0zREpuzXhwO4pJbDIYsnM4HnPy%2BJPM2%2BETPmlDinViFY4t%2FR3e3TH0JSTOxSZFd5Z5SWdXr6rb9rWNFplaZr3M49YU3PifMhN%2FWEvTP%2Bs02BaCV0YzreFqlifjrHaf5rPTiDcaC1IwTiw8itH5YM5tgnQSz1VyhSSCPKvHo0qlepcsWuAoRpAGCswdA7Jb18pkXYxtLlowdQjwp%2FrkTkBbgRU2a0trT36UYwEtIEfTH4Xc9P1wStYfXm4T8cwp1mDhor43xpkP4Qhq08jZigAZTzcnvqr8ckUirLbmaiApbgqZwgK12MOAxB3NUA84NeYLBmvgrZP%2FZX86uDAXNyOjdZ9%2Fm4HTcRpb6PDpAjDZD964s3HSRzFJ3G5LwvK5Z%2BXvyyTp%2B7yMN6%2Bmr0GOqUB%2BV6gSvA9un3Fb5xOIZbe1dKIXrjCgz8hMQ3EcSK%2FI%2BRw1TrJz77sOsg0slQOo8zd8agrfGWRgwg0C1X0UaBgSSb%2Br6nnUB%2F6KI7GbE011d7Q4anUksNnYN0otzPJFGfb4ylCm1VKWK%2FM%2FuqHwDOLfHP0lEycgM3SwxDpBOGRVTkuiDxA54ok68xodRxt%2Bps%2BTw%2FtlpWRHZT6l7i2E1uBHqzUffSK&X-Amz-Signature=813b3889c1c83cd1c718433b1e3a0de9d98c4df0ee2e96eff92b29101b6278dc&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TLSS3AT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJIMEYCIQDqhYRNu%2BQv6rsyGeFcXFf43MNhsdcKv%2BAPWo8OHhJYHgIhALo5g2bq6bzHpBJoBiQDBDPoq4En8NdqF%2Fn8i0HOtc4NKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyaTM2IOEbVchV6YBcq3APOpNbjtWZ4DoWQljNsWz3LFoc8DgVdXXyD6oYbjQRmqCbVDwfEbRJl0qZVj0hjAoQECQVKsWNHMB3IgUmHSP%2Bomwt5SO0DHGbc14twqc4NUL9RbJwqVWzLuvKmjD29bfLWHjooPE5DdjQOSrcEw5y5jcHZ6%2BS7yOwXyaCy6qikCkDjEBmyQ6G3FnsJ7Rn6SFWWPIJD%2F0EncyD2VCHvwkCMyy193ZdGgE4sBizKi5nmAmHAn%2BHMp9uU9PtdcN%2FFx3okGaVUkCem%2FT%2FhlhTYJS7%2B6UyyRQKC9%2Bv81RKN1qAbGXWNXbq9bXzGhggdQF5tHw3Ywj5%2BDom3%2B3ScTmMrB%2FH%2Fu8voJioCXhVdBQNBJ8Y4PB9LcmbNOBzmbGHoqmcIxBcJaik9hA0f%2FbFsiDg%2FjfPSQgZyvjs56Fr2I0ETY1eIKyVVLY%2BjMis4E6ZZvpyCvPkYv7W1WpdzPwkO%2BV36krXaX5SdjIisWcy%2BWdABr%2B%2BKgooJ8ciXXxv406r22jjYVJYOMVTVgWOqEprKnulYvQBXl9eq%2BT5iLWT9QqbYjeUbm9yp0v1CGooHEJ%2B%2FxhSnutlgdYk7xg743gCv2RcdWfslP0QkiscQ8WkBkFcgfROwgCteTiTdNtzD4R3FQjCwvpq9BjqkAfii9LR5hByZR0vTnKVXsVsT76dBlDjdPIgdj8P35q4TIk%2FJmXAlrprEbW4cETS6domdJA5CE4VRufRhTaXMr0v8DlmsnMT1cJd2AWPKHFOhX2%2F4XIGmAOCWVOIvDTiNHqXp1%2F1JAx921rNLDbOMdC5UoId%2BosClCySDoGZjuMFO%2FdopSlDQyP%2F4MgfifYOJG5PLug77spZy2CPMYtItYZqz0ZXz&X-Amz-Signature=da5bae09be9b647d98eb7771e907e8369345248ef9f1254799b315b41afae2e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7DDEJP4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBDxjGBvkdEFxC8g2w66E22nXoSPNN5Za3mRGgHZausDAiBhqH%2BZLJYhoL15Y772STxAKgdoTYPjXV3MT9Vb6NgJOCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEio3BZLQYjtfpSfPKtwDVr1GW2T2ttCvt5u3%2FOgCglyZ5Ij%2Bnd7n3aXU%2FWWvNHoKSwglqcFHd65baX8NrHdtpbzsOsg%2BhqKFor51BXueX%2FZrN9QJLAie7T8l8EmUHtfH7o1K6cXntC88ofzglSMshfhUGSk%2FNDUwZH8cEfPArptvrllRfhAEPruiSiAEYEm3YEpCgtTmSlCgMwd9UMBzfwAJUphUw0wt5LCyG08YorgQetbE%2Fy1xRiuCyPhRAXeikAr573CSw6Qtw1eH3HBw%2BxfYtqznUL90EUSStvjHoTPbG7Fxron1U80uz9GoKG8eMT0rg2xEOsRPcl1TUiuaJORN9guBKqiCFAupfwlbpqr4jWfBP1NEigOvoJo%2BEIW%2BEEDGLbW%2B58DLsTW2h%2FQhsS%2Fgtw0fBTIoJqS1V2c6k6C%2FmCOiKwOCYEx26c%2BcIyXQjvsl912eO%2FxZr3VcpoTBxokAaop9Vkda3yigPOS4cjve0q%2FcfwRvf1iqBIMkOQTuqu7haUJxbCJ41FuvdNb2ZXynbOper1ENtdRffRDZdHstpQ3aBFbint3mnArkAnbm3J%2FPHXdDeAUGDbRYRfcfLGi05eZq5Z6D8Vdt5B8M4x93fJ65ViS9FLgGG2%2Fmxqd8p%2FjU0hgNGxMEzn8wpb6avQY6pgHmGjjFMlgE8YMCzU34hC5igfu83y4taYPUD%2BSrVWbZ%2BeD6izfRPfudx788C55zUVKmX5ab2v4Cma233QhUv7LEG9yuOWSmA8c8N07SDdEqXknbibRmudYY3brKrVTjkJojWpdTFDrswUsuWy1F218RtfBKIJ2I6q0jnaVPegYIPlw98WZy5AHkfDbQwiUFIFRgqs3wNQKbKJVXb4m80uZIhenqdVgD&X-Amz-Signature=aed8fec9f5e7f452576f701083edd06e0c448c33745423ad99e62af74d078ab4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7DDEJP4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBDxjGBvkdEFxC8g2w66E22nXoSPNN5Za3mRGgHZausDAiBhqH%2BZLJYhoL15Y772STxAKgdoTYPjXV3MT9Vb6NgJOCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEio3BZLQYjtfpSfPKtwDVr1GW2T2ttCvt5u3%2FOgCglyZ5Ij%2Bnd7n3aXU%2FWWvNHoKSwglqcFHd65baX8NrHdtpbzsOsg%2BhqKFor51BXueX%2FZrN9QJLAie7T8l8EmUHtfH7o1K6cXntC88ofzglSMshfhUGSk%2FNDUwZH8cEfPArptvrllRfhAEPruiSiAEYEm3YEpCgtTmSlCgMwd9UMBzfwAJUphUw0wt5LCyG08YorgQetbE%2Fy1xRiuCyPhRAXeikAr573CSw6Qtw1eH3HBw%2BxfYtqznUL90EUSStvjHoTPbG7Fxron1U80uz9GoKG8eMT0rg2xEOsRPcl1TUiuaJORN9guBKqiCFAupfwlbpqr4jWfBP1NEigOvoJo%2BEIW%2BEEDGLbW%2B58DLsTW2h%2FQhsS%2Fgtw0fBTIoJqS1V2c6k6C%2FmCOiKwOCYEx26c%2BcIyXQjvsl912eO%2FxZr3VcpoTBxokAaop9Vkda3yigPOS4cjve0q%2FcfwRvf1iqBIMkOQTuqu7haUJxbCJ41FuvdNb2ZXynbOper1ENtdRffRDZdHstpQ3aBFbint3mnArkAnbm3J%2FPHXdDeAUGDbRYRfcfLGi05eZq5Z6D8Vdt5B8M4x93fJ65ViS9FLgGG2%2Fmxqd8p%2FjU0hgNGxMEzn8wpb6avQY6pgHmGjjFMlgE8YMCzU34hC5igfu83y4taYPUD%2BSrVWbZ%2BeD6izfRPfudx788C55zUVKmX5ab2v4Cma233QhUv7LEG9yuOWSmA8c8N07SDdEqXknbibRmudYY3brKrVTjkJojWpdTFDrswUsuWy1F218RtfBKIJ2I6q0jnaVPegYIPlw98WZy5AHkfDbQwiUFIFRgqs3wNQKbKJVXb4m80uZIhenqdVgD&X-Amz-Signature=19a7737e917ccb58843ccad6a940a857b7b0ee9a4352ea86a8fd76fa44a5fe6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7DDEJP4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIBDxjGBvkdEFxC8g2w66E22nXoSPNN5Za3mRGgHZausDAiBhqH%2BZLJYhoL15Y772STxAKgdoTYPjXV3MT9Vb6NgJOCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEio3BZLQYjtfpSfPKtwDVr1GW2T2ttCvt5u3%2FOgCglyZ5Ij%2Bnd7n3aXU%2FWWvNHoKSwglqcFHd65baX8NrHdtpbzsOsg%2BhqKFor51BXueX%2FZrN9QJLAie7T8l8EmUHtfH7o1K6cXntC88ofzglSMshfhUGSk%2FNDUwZH8cEfPArptvrllRfhAEPruiSiAEYEm3YEpCgtTmSlCgMwd9UMBzfwAJUphUw0wt5LCyG08YorgQetbE%2Fy1xRiuCyPhRAXeikAr573CSw6Qtw1eH3HBw%2BxfYtqznUL90EUSStvjHoTPbG7Fxron1U80uz9GoKG8eMT0rg2xEOsRPcl1TUiuaJORN9guBKqiCFAupfwlbpqr4jWfBP1NEigOvoJo%2BEIW%2BEEDGLbW%2B58DLsTW2h%2FQhsS%2Fgtw0fBTIoJqS1V2c6k6C%2FmCOiKwOCYEx26c%2BcIyXQjvsl912eO%2FxZr3VcpoTBxokAaop9Vkda3yigPOS4cjve0q%2FcfwRvf1iqBIMkOQTuqu7haUJxbCJ41FuvdNb2ZXynbOper1ENtdRffRDZdHstpQ3aBFbint3mnArkAnbm3J%2FPHXdDeAUGDbRYRfcfLGi05eZq5Z6D8Vdt5B8M4x93fJ65ViS9FLgGG2%2Fmxqd8p%2FjU0hgNGxMEzn8wpb6avQY6pgHmGjjFMlgE8YMCzU34hC5igfu83y4taYPUD%2BSrVWbZ%2BeD6izfRPfudx788C55zUVKmX5ab2v4Cma233QhUv7LEG9yuOWSmA8c8N07SDdEqXknbibRmudYY3brKrVTjkJojWpdTFDrswUsuWy1F218RtfBKIJ2I6q0jnaVPegYIPlw98WZy5AHkfDbQwiUFIFRgqs3wNQKbKJVXb4m80uZIhenqdVgD&X-Amz-Signature=d9f8b02b1b83d657c7abc9d5979c19f46c62b06d40d932b136132c51fbff1c7a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622NVWXMA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJIMEYCIQDG2x2wjCTetF3z2dM77p8mzI%2ByE2jZdm%2FX4GqNUZvxEgIhAOvQ%2FVFHvc32m6ezhdDmtC%2BehntHGzsZQG1PBtSBq2h0KogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsHx2LmxfWFRYJKEgq3AOd%2BsZWoUnHGWj7a0K1sIDF8G1dGwz5H2CIzGwsLFydMV1DKINoFcQGJMdRc3gWzbpa57kYHIonSZrxQCwkReLO9c9ffnkuotUnTcSe9N7%2BP6Z7MS7EsqPeX7Knr0pllxjJtlVyQux0keritbHo2IP47BDlL%2BG7Ng9VvHWnIf9YGUKDgIuMmQCJpmWRW71vWVmRsm87W7IA2wD1xvXcl2U4%2B10Ii8ohJMzF3u2tW3WMFHjETlHIwmuR2wa%2BmxQOLfglUVLCBbpQKfdqVFrLpAVoVvdu4yWBQELJ3ANtr6JI34DwtKF7q07cyCF3IRDRjt62f7DOjGW%2BEgnKnsbdXXlxTU%2BR9ewUwmDnOgn1%2Fw1DLtQpGl1ECtyW5SeBK2I1bbW5Pa%2FeG1b5VdtQ12Ej7OMmNkSoT8UZgCrRgZQ9WlnMRA3tWx7ahGh9NUTvIDPTugLOLdnfFH%2F%2BDOcUVcrVCRdiz%2FZBSCzHBkUe7%2FsxlARe2IGE75iJbt7SHGyP0jnegonIjx2sXY46AGPKKMQhpT6pTzkbLn7VR1rG%2B44cuGIi5%2ForD4yXz%2F%2FJjrLrRbcDfmucFGDLN%2BuSiZnj84%2BLYmhqvttZ%2FTI4MGTGLMAadSknDyKMCJC3VOON7mWsVDDCvpq9BjqkAZXrR4WH37UfnF%2FHI6gZ429O9UsMaCpLPvq2tUbfzGbBmm%2Be503pnIDMPOMETlIdZCZEf9rngw2NzRqiIwSiO4JADbELbzN3pPWrumQLNkvbtFuBZ7JoLlKY6%2BhLXLaoHQ5SWA7Qni2It%2FEZ8TsDzmgifcH6A5gDC1UNrPIPOLoeBlQg3%2F%2BVfvpkMFipN8xhOsdadi4%2FdQCZxxHzrk6z69fEEMts&X-Amz-Signature=eed78ee24edd9e2c4a1ed7f22d56561e1e95c86356a71e5539994483cb962094&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFNBZORF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQDhsoL0ylkN26X2yWsjxw14HYDbL4GCnbqOKAt7QNnREwIgNYJQQeAzeYHkMQMgFegN9%2BKTCCoFH%2BKLby21IxByxLgqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEkDkVS%2BbIuwn%2BfwSrcA3IDtSpbk1ASlM7C3xUDGZhr1Y58imSNExKjFCXETbHOWy2o1T4MjB64Nm0LMBLYhR%2BGCALdqHKBYqB3R9r3ayHOPwSn1oMUbajQORF%2B7w3ZWmWX5FUs7LrSZYymZehn2PR0Fmm6J9u61tJrJWhrYSZxZRP3dwEtL6%2Fue6upCHIx6PI5L8R%2BcjfJYK9n2abNHvi5wSItK0YRis%2BawziziUmsclzlqS6x2pvFbRqoYHsWosds7i3eamMW0mgE%2BYXUxVsZ7BBr%2Be9BIqqAbxKaKLI6u6uvJ2SA2iboHduptXSCOoEgq15ALFXKNQTyg0V5KpC%2F%2BqBhhzh408ZFnlA3Yha8laEzYSeNRx%2Fjgcp1D08mgWl%2FHuYw7fhenaP4N7B%2BpYxg4s%2B%2BvH2wl%2B4nGYThemQ%2FBMJZtxZk2kkUGKJl2f1hvgt0G4DWFXe9RXRf4t351TFqf1PKAWlTO%2BAB1KOh47bwvlGpOzdaN8jzMe%2FDRWNfSDIMnh8rNc3IGaaeaGLv%2BBVQ1A0xaAQ%2BNMmnc6fBrcCo3jYaEI1%2BXjMnaxOKFH1vqM6dX64JOl0FSIUOgnlrOKM99CVj1qy2ufCKQSCJ%2BXCxh%2F5%2FUh3319yp0lLgktk8QNWRODF1JqfQMrGTMJG%2Bmr0GOqUBJyAnW83s4s9nYuAxZZhXRzEPJNU%2FyX8VEQVcZ7lbmWxcNFrDchjF69aYxZLhhdLxU%2FihV4gnl3GCxAlubrj10eOgsrAiSTSd%2Bq19YA%2BiXGBc%2B6WpV8Uik1PibJjYJLB9Q%2FTt0EPxFmywiz7jfhAFf7uDlcMbzP8d9cU212JmDZtpVBWPr05N%2B0ye%2Bu7gWj6HyX0%2B1Gd9A%2FT8azkf9roc5TgwOOnn&X-Amz-Signature=c7bb2904e090762581057d5c5fbac2e0873fb5181c6b6045dcb56d051eb325c4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5D7C2SE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQC7mEr8pkxBqZByEKASx6BbEe4C%2FJm3s2tw%2FtPT7HP%2BTAIgeqQPfH7Vid6k0ORglUtnmFlEVqA3914T1fgwXnPbZEcqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEqgSXl8tlmielRLPircA739R9ouTEQbmLXTxi3ek0WHkx7lW%2FwaUQ%2F0C5PDzkJ9k%2FRj4IKuCej2Fid8oe1zuKMfYKp81h0WMFopLhn3BUgJBO3g4AgJCeqr3HRs3vwrikX104tyr02uS0rEbxD6Qpm18Qzzoi4hu5AK5N7sHK750bmP%2F2MHpJFjqMHgFrk7NlfHIJnRx%2BAivBv7IY%2B7ctGlrkAeYkjtbZpkxxAKRlKlqdlSDWppxlH4DkdbLSk0hGz5gcYEybn7a%2BNILSzVE4JU20yPoS92roc%2Fxo%2ByQf%2Bieic%2BrszG8YRXr0%2BFcY9eRPbqVwxEJuGj1ztT29hGGUI2jFH%2B36qpcDZPZRZp3Da7SMS369F0JekbJ5mxZU95LWxUQYuszBeQ913YiJ2%2BVDnA1goUsdNit8wo7W2YqK4lbJS5mhQ4si2%2BNSU8Q0icZAX4Q%2FelICb5QsjJmQJ0d2wONWQ5Db4hmfZQtfQDyirdkEeateknc7Ra7WM80ARoFqccltMFfBlJnNubFrH%2BYmNMNz5BQhLkqVQhAz%2FN196y7uukkWKz5YZl96CBVJ46nTdDOlpVZYdAAS%2B5hO8idHDZUGGKJa4GMd50Y5a6El9DsuPG1tmCnU1YVF%2FHj2AVuGmYfPRINH%2BvDgdBMO2%2Bmr0GOqUBgrmjra%2BHYiTetU955ojmzfsSfSaCwQSVKuJwK4ifdUhgKfLsfC0GdRQUmrTSNOxt1fzo4sMF%2F0TdD1GZ8miDiEvpmOJjBBICy1D694%2ByYYNVd5ZW%2FFFG1bQk1kScn3GClcBTyA1U4xTUsX%2F1djuAVFBOE4lP9idfqN2xntZ2Vz2JHGr0KjsLLqSQE0ZlWFKIcFm6MJMr6%2F5rsrkAGAvxL37uYco4&X-Amz-Signature=c300b7662f04768ef45024eed9f48a50c40f62b266b1103c4ee8d2a3fb4bf71e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBJBECL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCICRQbFQIGrlzwubgJae%2BBlrWyLmWv0vB4uB%2FwwwaKO%2FBAiEA3aJ5i0Y3S7piIR4YMsY19NeKGqZcdoUgPuxJ1uvr1SAqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMIeY0rPyq9wT0Q%2FByrcAxeBR28dqD27drpikZspbN%2BI%2BBTYS7YtmRXqJnCdvXY9hqXM8uzlh0zntzpknuMGcYiKlPrj62jMmwnWUsYms6JG2%2ByqyXhPe%2Bgptg9dqWyW7u39fnU8KSqMVGjDBpr72072YVMdBOI3aKEAldc4P2Vnl%2FRsVmHcbAnY8RAskMweZxjlYhDLWgkUCiWljMTZ2NMCCbuIZiABlM5CVga5erXN0ZvfjFwacAMmsCU%2B7q2Q825dYUqgAaYfl5MGtAbbmEj2BwPiKUEQR9JyTKBCBJ2XRFo%2FKO6NL%2F8774%2BiHYRurSICu9Rd5I%2BquSZ1GqS1fanlbJgBR2pTE75E2je9UqXvgMJVANy9OT%2BTcDBO4LnqgB1Ju4bQABY9mzp0w5cYXvhyrElqgOCF5flYGTJzfL5Cz468ge60EAdZQ%2FPik12Okbs6lEIWkUpVBH4QysoNW%2FE0LfscOmAyfzUdhUJpiMt5h22VNfgDLmdWsKKSpb6lz5g4H8KbT%2Bbmlh4BJTGSswo6a2d2zYQ%2FfXlfNWKchk8kn1cGles73otw1182RTZsEqfoGzAlkRc3WMVY81Z97F9jn5O6Y28RT%2BallPtcE1g4kJnLWVxxz%2B7yD3n7a1gqmPYQ900QOcEmEZnyMPe%2Bmr0GOqUBW58sWJWlzuYm9kbzuShj6hz3N5VtQoWKYARd3TcZmrteJ5%2BROoc7Bsn%2ByhEk7fCHKYYSFm3%2FSIHcEt%2B%2FhcqKGhsubW36rhNdYEiA2QBGuDsVDg4BQ6iV8jgVgN9a6rvK7jbNxW5sFz%2FeN0Y%2Fl8DK2gIt8v8wAhDXn7zmuNEp1G26PfMVxsjBguaXDwwl7gRcRzflLaH6MokR3tNM%2BeZdZoGagiY4&X-Amz-Signature=7cf3da0bc99e3e017a298345db38ede05654d299eee59335c279b6d17dccb8bf&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPBJBECL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCICRQbFQIGrlzwubgJae%2BBlrWyLmWv0vB4uB%2FwwwaKO%2FBAiEA3aJ5i0Y3S7piIR4YMsY19NeKGqZcdoUgPuxJ1uvr1SAqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMIeY0rPyq9wT0Q%2FByrcAxeBR28dqD27drpikZspbN%2BI%2BBTYS7YtmRXqJnCdvXY9hqXM8uzlh0zntzpknuMGcYiKlPrj62jMmwnWUsYms6JG2%2ByqyXhPe%2Bgptg9dqWyW7u39fnU8KSqMVGjDBpr72072YVMdBOI3aKEAldc4P2Vnl%2FRsVmHcbAnY8RAskMweZxjlYhDLWgkUCiWljMTZ2NMCCbuIZiABlM5CVga5erXN0ZvfjFwacAMmsCU%2B7q2Q825dYUqgAaYfl5MGtAbbmEj2BwPiKUEQR9JyTKBCBJ2XRFo%2FKO6NL%2F8774%2BiHYRurSICu9Rd5I%2BquSZ1GqS1fanlbJgBR2pTE75E2je9UqXvgMJVANy9OT%2BTcDBO4LnqgB1Ju4bQABY9mzp0w5cYXvhyrElqgOCF5flYGTJzfL5Cz468ge60EAdZQ%2FPik12Okbs6lEIWkUpVBH4QysoNW%2FE0LfscOmAyfzUdhUJpiMt5h22VNfgDLmdWsKKSpb6lz5g4H8KbT%2Bbmlh4BJTGSswo6a2d2zYQ%2FfXlfNWKchk8kn1cGles73otw1182RTZsEqfoGzAlkRc3WMVY81Z97F9jn5O6Y28RT%2BallPtcE1g4kJnLWVxxz%2B7yD3n7a1gqmPYQ900QOcEmEZnyMPe%2Bmr0GOqUBW58sWJWlzuYm9kbzuShj6hz3N5VtQoWKYARd3TcZmrteJ5%2BROoc7Bsn%2ByhEk7fCHKYYSFm3%2FSIHcEt%2B%2FhcqKGhsubW36rhNdYEiA2QBGuDsVDg4BQ6iV8jgVgN9a6rvK7jbNxW5sFz%2FeN0Y%2Fl8DK2gIt8v8wAhDXn7zmuNEp1G26PfMVxsjBguaXDwwl7gRcRzflLaH6MokR3tNM%2BeZdZoGagiY4&X-Amz-Signature=03838f9f64c0ba943c84055e36fe22394458f8ef1d59dc10b7f295cdadedd2f8&X-Amz-SignedHeaders=host&x-id=GetObject)

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
