

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2HQVIRT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIQDoy6dEEgp%2FjyCoYPc7EPUsqYzW6E0H7f9qZx4%2F%2F9EKLgIfNrFn2oKdqIusxnntQ%2BLX2JFKUrgfU8qWkbek611cFCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2NrF79%2FUSJroMSe7KtwDqpCqk5FYUwCinQ0%2BbZMYYuJTXDzU%2F3dEd6VdF7OUS5%2FWU%2F5ooY1DuIv5FcrScgk%2FwUqGtBkNCX7ID3FQm70iV2cF1SoGiWRYFWLetLstTHzEBdq2aVHlphu9RKpyOSVbL0YfJyLDWI%2BRAbQ0Izs%2FVEp0661fDAOCJAfCpzuFMbZnvrwntedOcQH0mcUtqdB2hcOjMSQTk17nuJOsHWa3yd%2Bylup4pwSGxb7F0ljMviocPW6RamlQMPnRn3WXFucRQ72PRG4KDc%2BOaplJFIg0RN9VBZ222C0RrZDMfKaZf36RwPfGdd4YBdiqu2IhmxMXE93gllbT%2B%2F%2B2B2CJ0Oluy7LZmOUkJkvmWUoLctBNUOuk3Leh83g5lb8yY%2B2mDdaUmCbuorey4ULa5cPCuqmWBSBw29XXRAJH6xv16rF0ufSl2APmyXYLlN9SwLwTZ5v%2BfW49mwwv77bg3wwxfc2YAVC33irkE4lalIhz%2FP4IaoBX53yDGCFvuNHffXqMSO1joU0%2FzQB3MrIHnMhKOKjYrxbh7t6rXUYAQxsotX31KPcMw4lieNvdiQziEo616UdB84twttvgo65QIqrDsz16BpyPlOW9bEW%2FBD%2BpWD7Fw8X8tc3zk8xHtNbUkWwwqrvmvAY6pgHQrKyMNzhuvSsjWFmxUAayUPxqrVn%2Bh7Dz4QXlGydH7ZcXlfWdiZYltzQ4bQn3EO1kd3OmzMw%2F4q7zzljyGuSn67ivKyYb9boJOp5cec86QjSAAaxeGJsR0Erljd7R4AHZJtNHaQjpwCNKF%2BdA9Fb2BvbiY0Iajxhle3CG2tvM7AJuEclMZGHGxLIEeeRxjDpJRrH0PzyKpR0ishoqEXpaLzfz652m&X-Amz-Signature=b276a23a959ae3a7ef2c2b2e84887019c60b3f7858868ac719f9e529e83a48db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2HQVIRT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIQDoy6dEEgp%2FjyCoYPc7EPUsqYzW6E0H7f9qZx4%2F%2F9EKLgIfNrFn2oKdqIusxnntQ%2BLX2JFKUrgfU8qWkbek611cFCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2NrF79%2FUSJroMSe7KtwDqpCqk5FYUwCinQ0%2BbZMYYuJTXDzU%2F3dEd6VdF7OUS5%2FWU%2F5ooY1DuIv5FcrScgk%2FwUqGtBkNCX7ID3FQm70iV2cF1SoGiWRYFWLetLstTHzEBdq2aVHlphu9RKpyOSVbL0YfJyLDWI%2BRAbQ0Izs%2FVEp0661fDAOCJAfCpzuFMbZnvrwntedOcQH0mcUtqdB2hcOjMSQTk17nuJOsHWa3yd%2Bylup4pwSGxb7F0ljMviocPW6RamlQMPnRn3WXFucRQ72PRG4KDc%2BOaplJFIg0RN9VBZ222C0RrZDMfKaZf36RwPfGdd4YBdiqu2IhmxMXE93gllbT%2B%2F%2B2B2CJ0Oluy7LZmOUkJkvmWUoLctBNUOuk3Leh83g5lb8yY%2B2mDdaUmCbuorey4ULa5cPCuqmWBSBw29XXRAJH6xv16rF0ufSl2APmyXYLlN9SwLwTZ5v%2BfW49mwwv77bg3wwxfc2YAVC33irkE4lalIhz%2FP4IaoBX53yDGCFvuNHffXqMSO1joU0%2FzQB3MrIHnMhKOKjYrxbh7t6rXUYAQxsotX31KPcMw4lieNvdiQziEo616UdB84twttvgo65QIqrDsz16BpyPlOW9bEW%2FBD%2BpWD7Fw8X8tc3zk8xHtNbUkWwwqrvmvAY6pgHQrKyMNzhuvSsjWFmxUAayUPxqrVn%2Bh7Dz4QXlGydH7ZcXlfWdiZYltzQ4bQn3EO1kd3OmzMw%2F4q7zzljyGuSn67ivKyYb9boJOp5cec86QjSAAaxeGJsR0Erljd7R4AHZJtNHaQjpwCNKF%2BdA9Fb2BvbiY0Iajxhle3CG2tvM7AJuEclMZGHGxLIEeeRxjDpJRrH0PzyKpR0ishoqEXpaLzfz652m&X-Amz-Signature=901bef5bd748985396456a28a3953d10f30f2c23004514c0a452314c20dd0ff8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2HQVIRT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIQDoy6dEEgp%2FjyCoYPc7EPUsqYzW6E0H7f9qZx4%2F%2F9EKLgIfNrFn2oKdqIusxnntQ%2BLX2JFKUrgfU8qWkbek611cFCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2NrF79%2FUSJroMSe7KtwDqpCqk5FYUwCinQ0%2BbZMYYuJTXDzU%2F3dEd6VdF7OUS5%2FWU%2F5ooY1DuIv5FcrScgk%2FwUqGtBkNCX7ID3FQm70iV2cF1SoGiWRYFWLetLstTHzEBdq2aVHlphu9RKpyOSVbL0YfJyLDWI%2BRAbQ0Izs%2FVEp0661fDAOCJAfCpzuFMbZnvrwntedOcQH0mcUtqdB2hcOjMSQTk17nuJOsHWa3yd%2Bylup4pwSGxb7F0ljMviocPW6RamlQMPnRn3WXFucRQ72PRG4KDc%2BOaplJFIg0RN9VBZ222C0RrZDMfKaZf36RwPfGdd4YBdiqu2IhmxMXE93gllbT%2B%2F%2B2B2CJ0Oluy7LZmOUkJkvmWUoLctBNUOuk3Leh83g5lb8yY%2B2mDdaUmCbuorey4ULa5cPCuqmWBSBw29XXRAJH6xv16rF0ufSl2APmyXYLlN9SwLwTZ5v%2BfW49mwwv77bg3wwxfc2YAVC33irkE4lalIhz%2FP4IaoBX53yDGCFvuNHffXqMSO1joU0%2FzQB3MrIHnMhKOKjYrxbh7t6rXUYAQxsotX31KPcMw4lieNvdiQziEo616UdB84twttvgo65QIqrDsz16BpyPlOW9bEW%2FBD%2BpWD7Fw8X8tc3zk8xHtNbUkWwwqrvmvAY6pgHQrKyMNzhuvSsjWFmxUAayUPxqrVn%2Bh7Dz4QXlGydH7ZcXlfWdiZYltzQ4bQn3EO1kd3OmzMw%2F4q7zzljyGuSn67ivKyYb9boJOp5cec86QjSAAaxeGJsR0Erljd7R4AHZJtNHaQjpwCNKF%2BdA9Fb2BvbiY0Iajxhle3CG2tvM7AJuEclMZGHGxLIEeeRxjDpJRrH0PzyKpR0ishoqEXpaLzfz652m&X-Amz-Signature=f706f9f3f2539b8e10832e7477baa17017c2b79980d09dbe251f3c2192d32663&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637DA2RHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCNBuYc7KxNY%2F826Acg6sCIxb8jEuOI9mqRuAcR44AdOwIgYB7JrSlg3w1oWoJcgWZMbBXJZuQo%2BczH%2B2q6m1JB1JgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOati3mBuCSdohVVfircA6hhfb7ayQj37UlijhdjeVdJOrGvi00jy4ZdF3cbpG%2FM7NoRWUrQM3%2F%2BPOsie5YVy3jKPp4iMY54Ub9LauZqzUaZETQugo2AOflQ5ixxZQYLmH0a7knaVoI0zqiPi0%2FICkFiKi7dYITDWm8OLPDI8%2FngGbCvTB7nDfaTiJ7SA4VG%2BLnSoFab%2BbKj91ubAAODjM31iaNs%2BfT6CEHOmjOiDsZgCs6lwD2wk0cKWsyaAAYMAzPlAn6cFvslHZGVn7XXMyMGQ3%2BSX5VV3MlYkHznvHdVP51a%2B8IsuH133%2B2mOCSHl5tSDURQNfjQIHWSEnycEvWq%2FhUGA%2BNBIB11vua9mq30rGprr%2BMBezhvU5XkUS9BPgiva6AxbFF2kEWfggPxDJbhuiMjvJrrBaIAsUYTwrTK0m7h8SqMmJC%2BsVnyLurpTGvXvPmlry81IVvt0D3eDGFMpveXunYiuNJDQtBzw3Q%2FvDJlHAr9skLtK%2B578OETR5gGNTVGqdapjTytXrLgEQaMpea4uBRgWeMsexz0CXCZE87Lbm4nRxWz2VQudeJrbqRUqoLtqEE%2FfIbPZQJyShEPuEW%2F4xy%2FPl%2F%2BUbAqjL2Xg0LIsyZTYGcUDg0FVHyAZWi%2Bgf4UExjfdUPOMNO65rwGOqUBSltPZByM2yjdOd2nH6bUYKT4TCUtOqwN7%2F3bcopFwSlUAB7xWnwrm4mHVk1B5MLcEaEKWLNZEGYftNZADGxM%2B%2FL%2FegbBbkcFQpGPbXxV5HTXl7Xe6xFuvS3qOm7kMyoWLs5uJRZxYft%2B655OCc5LQsD7H5lCzIqA5AMz5wx84wRyJQqx71NrCtV52iret%2FkYPnV6%2Byt0IqxrHOC7U1tie5j%2FFpl1&X-Amz-Signature=b6eb6c5c64157e9e4bbe2985c3041863344ce2e9b22445e79370915f9b56e9c7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637DA2RHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCNBuYc7KxNY%2F826Acg6sCIxb8jEuOI9mqRuAcR44AdOwIgYB7JrSlg3w1oWoJcgWZMbBXJZuQo%2BczH%2B2q6m1JB1JgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOati3mBuCSdohVVfircA6hhfb7ayQj37UlijhdjeVdJOrGvi00jy4ZdF3cbpG%2FM7NoRWUrQM3%2F%2BPOsie5YVy3jKPp4iMY54Ub9LauZqzUaZETQugo2AOflQ5ixxZQYLmH0a7knaVoI0zqiPi0%2FICkFiKi7dYITDWm8OLPDI8%2FngGbCvTB7nDfaTiJ7SA4VG%2BLnSoFab%2BbKj91ubAAODjM31iaNs%2BfT6CEHOmjOiDsZgCs6lwD2wk0cKWsyaAAYMAzPlAn6cFvslHZGVn7XXMyMGQ3%2BSX5VV3MlYkHznvHdVP51a%2B8IsuH133%2B2mOCSHl5tSDURQNfjQIHWSEnycEvWq%2FhUGA%2BNBIB11vua9mq30rGprr%2BMBezhvU5XkUS9BPgiva6AxbFF2kEWfggPxDJbhuiMjvJrrBaIAsUYTwrTK0m7h8SqMmJC%2BsVnyLurpTGvXvPmlry81IVvt0D3eDGFMpveXunYiuNJDQtBzw3Q%2FvDJlHAr9skLtK%2B578OETR5gGNTVGqdapjTytXrLgEQaMpea4uBRgWeMsexz0CXCZE87Lbm4nRxWz2VQudeJrbqRUqoLtqEE%2FfIbPZQJyShEPuEW%2F4xy%2FPl%2F%2BUbAqjL2Xg0LIsyZTYGcUDg0FVHyAZWi%2Bgf4UExjfdUPOMNO65rwGOqUBSltPZByM2yjdOd2nH6bUYKT4TCUtOqwN7%2F3bcopFwSlUAB7xWnwrm4mHVk1B5MLcEaEKWLNZEGYftNZADGxM%2B%2FL%2FegbBbkcFQpGPbXxV5HTXl7Xe6xFuvS3qOm7kMyoWLs5uJRZxYft%2B655OCc5LQsD7H5lCzIqA5AMz5wx84wRyJQqx71NrCtV52iret%2FkYPnV6%2Byt0IqxrHOC7U1tie5j%2FFpl1&X-Amz-Signature=c1fcd27577c1eb5c45ee8e8ff144ecbb3894c067a625aedb85bad2243656ecb4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637DA2RHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCNBuYc7KxNY%2F826Acg6sCIxb8jEuOI9mqRuAcR44AdOwIgYB7JrSlg3w1oWoJcgWZMbBXJZuQo%2BczH%2B2q6m1JB1JgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOati3mBuCSdohVVfircA6hhfb7ayQj37UlijhdjeVdJOrGvi00jy4ZdF3cbpG%2FM7NoRWUrQM3%2F%2BPOsie5YVy3jKPp4iMY54Ub9LauZqzUaZETQugo2AOflQ5ixxZQYLmH0a7knaVoI0zqiPi0%2FICkFiKi7dYITDWm8OLPDI8%2FngGbCvTB7nDfaTiJ7SA4VG%2BLnSoFab%2BbKj91ubAAODjM31iaNs%2BfT6CEHOmjOiDsZgCs6lwD2wk0cKWsyaAAYMAzPlAn6cFvslHZGVn7XXMyMGQ3%2BSX5VV3MlYkHznvHdVP51a%2B8IsuH133%2B2mOCSHl5tSDURQNfjQIHWSEnycEvWq%2FhUGA%2BNBIB11vua9mq30rGprr%2BMBezhvU5XkUS9BPgiva6AxbFF2kEWfggPxDJbhuiMjvJrrBaIAsUYTwrTK0m7h8SqMmJC%2BsVnyLurpTGvXvPmlry81IVvt0D3eDGFMpveXunYiuNJDQtBzw3Q%2FvDJlHAr9skLtK%2B578OETR5gGNTVGqdapjTytXrLgEQaMpea4uBRgWeMsexz0CXCZE87Lbm4nRxWz2VQudeJrbqRUqoLtqEE%2FfIbPZQJyShEPuEW%2F4xy%2FPl%2F%2BUbAqjL2Xg0LIsyZTYGcUDg0FVHyAZWi%2Bgf4UExjfdUPOMNO65rwGOqUBSltPZByM2yjdOd2nH6bUYKT4TCUtOqwN7%2F3bcopFwSlUAB7xWnwrm4mHVk1B5MLcEaEKWLNZEGYftNZADGxM%2B%2FL%2FegbBbkcFQpGPbXxV5HTXl7Xe6xFuvS3qOm7kMyoWLs5uJRZxYft%2B655OCc5LQsD7H5lCzIqA5AMz5wx84wRyJQqx71NrCtV52iret%2FkYPnV6%2Byt0IqxrHOC7U1tie5j%2FFpl1&X-Amz-Signature=c4b2cde71d8eb01ee819ebc7ab5ba149cf4e674221c9f9dafa8c420f7f2e6bd7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637DA2RHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCNBuYc7KxNY%2F826Acg6sCIxb8jEuOI9mqRuAcR44AdOwIgYB7JrSlg3w1oWoJcgWZMbBXJZuQo%2BczH%2B2q6m1JB1JgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOati3mBuCSdohVVfircA6hhfb7ayQj37UlijhdjeVdJOrGvi00jy4ZdF3cbpG%2FM7NoRWUrQM3%2F%2BPOsie5YVy3jKPp4iMY54Ub9LauZqzUaZETQugo2AOflQ5ixxZQYLmH0a7knaVoI0zqiPi0%2FICkFiKi7dYITDWm8OLPDI8%2FngGbCvTB7nDfaTiJ7SA4VG%2BLnSoFab%2BbKj91ubAAODjM31iaNs%2BfT6CEHOmjOiDsZgCs6lwD2wk0cKWsyaAAYMAzPlAn6cFvslHZGVn7XXMyMGQ3%2BSX5VV3MlYkHznvHdVP51a%2B8IsuH133%2B2mOCSHl5tSDURQNfjQIHWSEnycEvWq%2FhUGA%2BNBIB11vua9mq30rGprr%2BMBezhvU5XkUS9BPgiva6AxbFF2kEWfggPxDJbhuiMjvJrrBaIAsUYTwrTK0m7h8SqMmJC%2BsVnyLurpTGvXvPmlry81IVvt0D3eDGFMpveXunYiuNJDQtBzw3Q%2FvDJlHAr9skLtK%2B578OETR5gGNTVGqdapjTytXrLgEQaMpea4uBRgWeMsexz0CXCZE87Lbm4nRxWz2VQudeJrbqRUqoLtqEE%2FfIbPZQJyShEPuEW%2F4xy%2FPl%2F%2BUbAqjL2Xg0LIsyZTYGcUDg0FVHyAZWi%2Bgf4UExjfdUPOMNO65rwGOqUBSltPZByM2yjdOd2nH6bUYKT4TCUtOqwN7%2F3bcopFwSlUAB7xWnwrm4mHVk1B5MLcEaEKWLNZEGYftNZADGxM%2B%2FL%2FegbBbkcFQpGPbXxV5HTXl7Xe6xFuvS3qOm7kMyoWLs5uJRZxYft%2B655OCc5LQsD7H5lCzIqA5AMz5wx84wRyJQqx71NrCtV52iret%2FkYPnV6%2Byt0IqxrHOC7U1tie5j%2FFpl1&X-Amz-Signature=1a2dddd10a373a07f919f3574db899f0a3d31e791b6c32b5d2f537d0d1ffe549&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637DA2RHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCNBuYc7KxNY%2F826Acg6sCIxb8jEuOI9mqRuAcR44AdOwIgYB7JrSlg3w1oWoJcgWZMbBXJZuQo%2BczH%2B2q6m1JB1JgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOati3mBuCSdohVVfircA6hhfb7ayQj37UlijhdjeVdJOrGvi00jy4ZdF3cbpG%2FM7NoRWUrQM3%2F%2BPOsie5YVy3jKPp4iMY54Ub9LauZqzUaZETQugo2AOflQ5ixxZQYLmH0a7knaVoI0zqiPi0%2FICkFiKi7dYITDWm8OLPDI8%2FngGbCvTB7nDfaTiJ7SA4VG%2BLnSoFab%2BbKj91ubAAODjM31iaNs%2BfT6CEHOmjOiDsZgCs6lwD2wk0cKWsyaAAYMAzPlAn6cFvslHZGVn7XXMyMGQ3%2BSX5VV3MlYkHznvHdVP51a%2B8IsuH133%2B2mOCSHl5tSDURQNfjQIHWSEnycEvWq%2FhUGA%2BNBIB11vua9mq30rGprr%2BMBezhvU5XkUS9BPgiva6AxbFF2kEWfggPxDJbhuiMjvJrrBaIAsUYTwrTK0m7h8SqMmJC%2BsVnyLurpTGvXvPmlry81IVvt0D3eDGFMpveXunYiuNJDQtBzw3Q%2FvDJlHAr9skLtK%2B578OETR5gGNTVGqdapjTytXrLgEQaMpea4uBRgWeMsexz0CXCZE87Lbm4nRxWz2VQudeJrbqRUqoLtqEE%2FfIbPZQJyShEPuEW%2F4xy%2FPl%2F%2BUbAqjL2Xg0LIsyZTYGcUDg0FVHyAZWi%2Bgf4UExjfdUPOMNO65rwGOqUBSltPZByM2yjdOd2nH6bUYKT4TCUtOqwN7%2F3bcopFwSlUAB7xWnwrm4mHVk1B5MLcEaEKWLNZEGYftNZADGxM%2B%2FL%2FegbBbkcFQpGPbXxV5HTXl7Xe6xFuvS3qOm7kMyoWLs5uJRZxYft%2B655OCc5LQsD7H5lCzIqA5AMz5wx84wRyJQqx71NrCtV52iret%2FkYPnV6%2Byt0IqxrHOC7U1tie5j%2FFpl1&X-Amz-Signature=c7d8858dea38dd18abff638ed743bd076565847fee4b50b29b06f695a388e66a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637DA2RHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCNBuYc7KxNY%2F826Acg6sCIxb8jEuOI9mqRuAcR44AdOwIgYB7JrSlg3w1oWoJcgWZMbBXJZuQo%2BczH%2B2q6m1JB1JgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOati3mBuCSdohVVfircA6hhfb7ayQj37UlijhdjeVdJOrGvi00jy4ZdF3cbpG%2FM7NoRWUrQM3%2F%2BPOsie5YVy3jKPp4iMY54Ub9LauZqzUaZETQugo2AOflQ5ixxZQYLmH0a7knaVoI0zqiPi0%2FICkFiKi7dYITDWm8OLPDI8%2FngGbCvTB7nDfaTiJ7SA4VG%2BLnSoFab%2BbKj91ubAAODjM31iaNs%2BfT6CEHOmjOiDsZgCs6lwD2wk0cKWsyaAAYMAzPlAn6cFvslHZGVn7XXMyMGQ3%2BSX5VV3MlYkHznvHdVP51a%2B8IsuH133%2B2mOCSHl5tSDURQNfjQIHWSEnycEvWq%2FhUGA%2BNBIB11vua9mq30rGprr%2BMBezhvU5XkUS9BPgiva6AxbFF2kEWfggPxDJbhuiMjvJrrBaIAsUYTwrTK0m7h8SqMmJC%2BsVnyLurpTGvXvPmlry81IVvt0D3eDGFMpveXunYiuNJDQtBzw3Q%2FvDJlHAr9skLtK%2B578OETR5gGNTVGqdapjTytXrLgEQaMpea4uBRgWeMsexz0CXCZE87Lbm4nRxWz2VQudeJrbqRUqoLtqEE%2FfIbPZQJyShEPuEW%2F4xy%2FPl%2F%2BUbAqjL2Xg0LIsyZTYGcUDg0FVHyAZWi%2Bgf4UExjfdUPOMNO65rwGOqUBSltPZByM2yjdOd2nH6bUYKT4TCUtOqwN7%2F3bcopFwSlUAB7xWnwrm4mHVk1B5MLcEaEKWLNZEGYftNZADGxM%2B%2FL%2FegbBbkcFQpGPbXxV5HTXl7Xe6xFuvS3qOm7kMyoWLs5uJRZxYft%2B655OCc5LQsD7H5lCzIqA5AMz5wx84wRyJQqx71NrCtV52iret%2FkYPnV6%2Byt0IqxrHOC7U1tie5j%2FFpl1&X-Amz-Signature=0a0f02d477d68e3ef54587570ec62647b322497c26c38098832ad788cad675b7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFHOZ3FT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIB8SkI7YubEY43qrkro7aKf7G4DHx1c59zqw6zTsAV%2FeAiEAh301UXVjC4ZdexSzOvRXNZPIwt5Xh7s1oP7r4w6y8RUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGmvNOeFGuR2SIVmSrcA4oOPXKmK65uLPV2ZP9h%2FA%2BXoF3Nzk1znVlb1Y8c5kqvRftOd58htnNuqjPuVlPzov5MGmcN8iHyqYcDod3DBJPJfWAs8O74LHMlKikZcAC9HAtXhCppyjj9QX843B8P%2B959Jd86lyVLAhQL%2BsaztxUMP6cN48xdQOCZMmsYKp0x42J9mXsufvNuWeaLxSP3V%2BJM7vLFH%2FBF9k8rtpFTZ0IETm0iC8b6J2MTXTec2bhyVKZdZ7rl%2B5UmRzNLH%2FgShh5WUihQ3nvkcKoONQGeikfbLB4s55Kc%2B7F6Is%2F07i7EAoyHAoYrW48tNClN1aNe75nmeBSF7voROQvZYXPSmYMB46lcw99PHQZW1InvSx0qCQcNnbQQQTaIJRy1CryJCUritoK%2Fhr2nhPNLK9AJv8V2rH65hge5uj6IOfjMW0N2cp4M7VitxlFqwJYRsjBiwhldgWVaBg%2BTFHQm00xpxQelM2m8iDDONG3GxtbSPO7eB0Z4s2EJe8bxAsK3W6cIlDf%2BAsxn03lJVRMdyqHiutSfk2zei2XWd0bYkYHZDVntA%2FrGO1DAEjyR7XfBrPbfVVsXgxMF9lC1x%2BxelK9N%2B0YB4Vlbt8GCFDICnsCxOVp%2Be7baGwZ7Vz4Fnlk1MIa75rwGOqUBrh4lVEckbfXNban2mOx7aWyOAMH2Eq%2FpAm%2Bt4zDiZ%2Ffvat%2FZ9q0yPtl8CEIWWxrkAm7SbtINMeAgOhLE%2BDTgaJ%2BWAR554cxVFnhsXO48LB3xnacsegXhNHS2RFnMDilwCGhzoyjEhwqq%2BPPsyCb3ZO3bblVWqZDSZ6fGMin0kGgXvKLNWTEVsKVIHXZqRPVzB6DBCbMs4iX4rrC0kTR4whylLWux&X-Amz-Signature=f961594f22e0d90da9f4e71931d67d5db50dbfc56c7f735490076134e5d4eee6&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X77TSWDR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDAudPEV8rAn6%2BeqKpvqInFtvvUqWyUDYuRjfbxe90TowIhAL2868OsKC1cb631%2Fx0YW2ZQB1eOhqMGK0%2FeogCxD72hKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZF4veRlrttpbfJxIq3AOM7NqmNITCHgAfaKW34fG8JjP4KuA8ZwwlXC5sXNca2d8KplImjm17%2Fa%2BEgRWt1m72mhtJHkfS1JB00m09uxpt28MJMvZwviGjTo4bnpNoXZyL1CSZB%2Fb8sS3fhdkGUNla2eZFr1qBvKYheAX2yMMEBILaxapND5b6EJv0PtgoDjPt9jlT6028ORiW1lgl0y3JbTCgA2XcGGcmffvKn6oDwxWyFNskiaCcyPlx3%2F%2B5mPcsAuI56iFXiBHU3aox4IzBVpau%2B3mIGkFxIfOPuS6ajj%2BUOgtwaYYT8veSCd7MPEcLXqlhjMP%2Bvj3H00OJZhRtcz%2B%2FA%2BJNSAK4qCSRMylDgDt0423gzMV8CQRZYTon7zaY11VSsD1fc5kQZj0bmtAgF0fxmko3LTbccizx%2BX6n11zL9sDcNGpVtTJJMdN69chk27tU515%2Bm0Un3BXXfXrgVUJ66xAvrDfzW2YOWzgCX6AZiAXzUyBu9J4NbyuCe%2BCqPoO%2Bt1xWwicgPRjZbNIgt4EForPg1VbzOmYfaMYPUZWKvZFRA5AT17o5O%2BZ3ClCmKmN2t3FabNaAAXgQiVmGIyvx0vdfe5frEl%2BDcYD2271KRQJp%2BnDeFiUwFn0YoxP%2BRr8aSbFZRXM79TDduua8BjqkAboR2VRHwknEx21RYct0KQd0rr8Lh4fgJmaiPGmSoEO4f8r%2FTLJnIBnIMuZYMjZMFJfZ1frb%2BpS%2FTKFZgXOGaWMMbGpl0VKYT8wmXEY1wt9et1pEnxYSzTQgwEYnrbGRGB0fIbNGT933eEtYUH7gkuO3Ru%2F9%2FLzkkIiiNfSDecZXQ47GcA2Tk03fkXMN%2B6qki%2BYy1tV415Rjc8fLFBPwtG7dxjfL&X-Amz-Signature=bd8b30742844fe919dc42d2a90fc129aa0036491d55c19f05065abbb63587605&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637DA2RHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCNBuYc7KxNY%2F826Acg6sCIxb8jEuOI9mqRuAcR44AdOwIgYB7JrSlg3w1oWoJcgWZMbBXJZuQo%2BczH%2B2q6m1JB1JgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOati3mBuCSdohVVfircA6hhfb7ayQj37UlijhdjeVdJOrGvi00jy4ZdF3cbpG%2FM7NoRWUrQM3%2F%2BPOsie5YVy3jKPp4iMY54Ub9LauZqzUaZETQugo2AOflQ5ixxZQYLmH0a7knaVoI0zqiPi0%2FICkFiKi7dYITDWm8OLPDI8%2FngGbCvTB7nDfaTiJ7SA4VG%2BLnSoFab%2BbKj91ubAAODjM31iaNs%2BfT6CEHOmjOiDsZgCs6lwD2wk0cKWsyaAAYMAzPlAn6cFvslHZGVn7XXMyMGQ3%2BSX5VV3MlYkHznvHdVP51a%2B8IsuH133%2B2mOCSHl5tSDURQNfjQIHWSEnycEvWq%2FhUGA%2BNBIB11vua9mq30rGprr%2BMBezhvU5XkUS9BPgiva6AxbFF2kEWfggPxDJbhuiMjvJrrBaIAsUYTwrTK0m7h8SqMmJC%2BsVnyLurpTGvXvPmlry81IVvt0D3eDGFMpveXunYiuNJDQtBzw3Q%2FvDJlHAr9skLtK%2B578OETR5gGNTVGqdapjTytXrLgEQaMpea4uBRgWeMsexz0CXCZE87Lbm4nRxWz2VQudeJrbqRUqoLtqEE%2FfIbPZQJyShEPuEW%2F4xy%2FPl%2F%2BUbAqjL2Xg0LIsyZTYGcUDg0FVHyAZWi%2Bgf4UExjfdUPOMNO65rwGOqUBSltPZByM2yjdOd2nH6bUYKT4TCUtOqwN7%2F3bcopFwSlUAB7xWnwrm4mHVk1B5MLcEaEKWLNZEGYftNZADGxM%2B%2FL%2FegbBbkcFQpGPbXxV5HTXl7Xe6xFuvS3qOm7kMyoWLs5uJRZxYft%2B655OCc5LQsD7H5lCzIqA5AMz5wx84wRyJQqx71NrCtV52iret%2FkYPnV6%2Byt0IqxrHOC7U1tie5j%2FFpl1&X-Amz-Signature=5c37c6c79679d091c636d20bffa4cea6b4362b157d01b983bfa1ee3fd0e92bc1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637DA2RHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCNBuYc7KxNY%2F826Acg6sCIxb8jEuOI9mqRuAcR44AdOwIgYB7JrSlg3w1oWoJcgWZMbBXJZuQo%2BczH%2B2q6m1JB1JgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOati3mBuCSdohVVfircA6hhfb7ayQj37UlijhdjeVdJOrGvi00jy4ZdF3cbpG%2FM7NoRWUrQM3%2F%2BPOsie5YVy3jKPp4iMY54Ub9LauZqzUaZETQugo2AOflQ5ixxZQYLmH0a7knaVoI0zqiPi0%2FICkFiKi7dYITDWm8OLPDI8%2FngGbCvTB7nDfaTiJ7SA4VG%2BLnSoFab%2BbKj91ubAAODjM31iaNs%2BfT6CEHOmjOiDsZgCs6lwD2wk0cKWsyaAAYMAzPlAn6cFvslHZGVn7XXMyMGQ3%2BSX5VV3MlYkHznvHdVP51a%2B8IsuH133%2B2mOCSHl5tSDURQNfjQIHWSEnycEvWq%2FhUGA%2BNBIB11vua9mq30rGprr%2BMBezhvU5XkUS9BPgiva6AxbFF2kEWfggPxDJbhuiMjvJrrBaIAsUYTwrTK0m7h8SqMmJC%2BsVnyLurpTGvXvPmlry81IVvt0D3eDGFMpveXunYiuNJDQtBzw3Q%2FvDJlHAr9skLtK%2B578OETR5gGNTVGqdapjTytXrLgEQaMpea4uBRgWeMsexz0CXCZE87Lbm4nRxWz2VQudeJrbqRUqoLtqEE%2FfIbPZQJyShEPuEW%2F4xy%2FPl%2F%2BUbAqjL2Xg0LIsyZTYGcUDg0FVHyAZWi%2Bgf4UExjfdUPOMNO65rwGOqUBSltPZByM2yjdOd2nH6bUYKT4TCUtOqwN7%2F3bcopFwSlUAB7xWnwrm4mHVk1B5MLcEaEKWLNZEGYftNZADGxM%2B%2FL%2FegbBbkcFQpGPbXxV5HTXl7Xe6xFuvS3qOm7kMyoWLs5uJRZxYft%2B655OCc5LQsD7H5lCzIqA5AMz5wx84wRyJQqx71NrCtV52iret%2FkYPnV6%2Byt0IqxrHOC7U1tie5j%2FFpl1&X-Amz-Signature=9d5fa2d6af15ebc74a44c4181a0a87d4ed51a3414a102f0a2086301510c2209e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637DA2RHE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCNBuYc7KxNY%2F826Acg6sCIxb8jEuOI9mqRuAcR44AdOwIgYB7JrSlg3w1oWoJcgWZMbBXJZuQo%2BczH%2B2q6m1JB1JgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOati3mBuCSdohVVfircA6hhfb7ayQj37UlijhdjeVdJOrGvi00jy4ZdF3cbpG%2FM7NoRWUrQM3%2F%2BPOsie5YVy3jKPp4iMY54Ub9LauZqzUaZETQugo2AOflQ5ixxZQYLmH0a7knaVoI0zqiPi0%2FICkFiKi7dYITDWm8OLPDI8%2FngGbCvTB7nDfaTiJ7SA4VG%2BLnSoFab%2BbKj91ubAAODjM31iaNs%2BfT6CEHOmjOiDsZgCs6lwD2wk0cKWsyaAAYMAzPlAn6cFvslHZGVn7XXMyMGQ3%2BSX5VV3MlYkHznvHdVP51a%2B8IsuH133%2B2mOCSHl5tSDURQNfjQIHWSEnycEvWq%2FhUGA%2BNBIB11vua9mq30rGprr%2BMBezhvU5XkUS9BPgiva6AxbFF2kEWfggPxDJbhuiMjvJrrBaIAsUYTwrTK0m7h8SqMmJC%2BsVnyLurpTGvXvPmlry81IVvt0D3eDGFMpveXunYiuNJDQtBzw3Q%2FvDJlHAr9skLtK%2B578OETR5gGNTVGqdapjTytXrLgEQaMpea4uBRgWeMsexz0CXCZE87Lbm4nRxWz2VQudeJrbqRUqoLtqEE%2FfIbPZQJyShEPuEW%2F4xy%2FPl%2F%2BUbAqjL2Xg0LIsyZTYGcUDg0FVHyAZWi%2Bgf4UExjfdUPOMNO65rwGOqUBSltPZByM2yjdOd2nH6bUYKT4TCUtOqwN7%2F3bcopFwSlUAB7xWnwrm4mHVk1B5MLcEaEKWLNZEGYftNZADGxM%2B%2FL%2FegbBbkcFQpGPbXxV5HTXl7Xe6xFuvS3qOm7kMyoWLs5uJRZxYft%2B655OCc5LQsD7H5lCzIqA5AMz5wx84wRyJQqx71NrCtV52iret%2FkYPnV6%2Byt0IqxrHOC7U1tie5j%2FFpl1&X-Amz-Signature=60562d916a21439775173bd9b6d2c6380191a7ac49e39c8934c9c710b5aed94b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBOPB5ME%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCrOJAr6WAsM1S6Fh35h2X8SAa0wDhDGy1Gu%2BdbEymc8wIhALoaci1R2dJ9V2ADtgjxz%2FEP7xFhkyYALSz6gfRTgygnKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgRc58QTYkqwlSB3cq3AOt78ZPyfM0wPdP%2FZlMvguTkNyaLuvrnm%2FA9swyEtv73%2FAB%2Bb2Ab7oUk%2BgdqbWwwe7eXMJUzfBtm7q9wKC4XFdpTYlZd12pBgng8wRf6mgjCjK3DHsHBh0xfh%2BYUDjze%2F224a9KmWOrcfac1RX2nQD0b3D0bkSHDKsktzu%2B4W7cbsSN4j3VQ%2BqND%2FH0rFcSNQm%2BsygkCUai1bUIOJxWS4oeoGkB7BqhNjkmiqtc4T2EMHeoMTQER7qBY7UTM5TO90ljrUAe4t43VGrKKkmmrHu2fKXeRBeJO6GBlnHogwgePzUieHbcMIkpS2yW1ut%2B1sC%2F5ZigR6ls980M6%2Fq3v3mnysRGI4mzsNzV9Uvn4CMTQ5CiY8BRovdOONUvlpbXdgmIOcEjx4MF11BKww%2FIhXnW%2FAqQSD58lCI1pS8PKPYqDdzgvxGQDQ7%2F5LzvxcnAd1uFOR9EHCQXqCf0lJ1uJrr%2FEyWQEMgwdSk9d%2FG6XOrP1Q9%2FHKD84AaAvTAqnDs3XYTZAThbN8SAX4IOfkq%2Bd6JdUKnO1OvJRB3fbJnpxHqYLvxVQs0%2FZLb4fd7PmkFzIGPVNVfwJ8jtaJZuWi42hnw6%2BsNcQx%2BaOhOM0Atbk0POZ%2FhQdfFN2C9aIjqh0DCIu%2Ba8BjqkAbqrQbrDdE54wEQrxLkHvdqGRtYJFlQqFRAPYgZxaJvssr7Af1zGgjV02Q%2BE86hNcIbNXamFu2s%2FLPHPUIk9OhUJyDv%2BtWzYYEMD2Y1%2FpkuQ5L7pM9iXZl8QjYM8b0dXV54BG0dpx%2F8lm0uiU1MmULWntxREQT4C1FmzLDmo6Y6XGIUiUcP%2FQ7K6rZ57cVx5zTnYYkfaR0LDx3w9uzDdlmGLdOn6&X-Amz-Signature=8a5a354786d9f5e332c30cdf70567deb8db1f044cdbe491f76f1ba77aeb47d8f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JP3AMLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIGRh9KjxSu6F%2Fhy1VZB7fMrvWkQMV7Io%2BMXSKxA%2FEiUpAiEAye1NQH996mj73eldiYKwXgp4oX1wCby0Aru8OJiQg2QqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHpGcVEILlIBNTzfSSrcA%2FiXZHwsRpQsCJz51VkdEOUmuw1mA%2Bvw0rvmNbYZzBFFkyx2rDCrKKb3d5%2Fxp5gjzQW1JcDQGAqOZ0cManf724T0bhqHjP6ntJvI71O4t%2B7W4W6lUW4Z%2Bky9y4dUQyJ7ZkxZLotTUh7PXBaEkowbnFwIIn%2B7pbIIOF1W%2FuAezQ%2Bl6tGcEUxkPEB08hYDz5lelyLrfHrxvcoTHI7napgOAfbAgRagu5lRQzALUZVPQ6X%2BZdzegQ5ILa%2BmYBpkGZzQHV1ffYN1N8Iz9byeobsEpFdo5QOXAqgFmvB6y5LlYQyc%2BzIwVKhlVzUQxB5CL%2BHO9WaGtRhXWkHQMD%2FUfx2ZtLsMakG22bRrwsvKcA36D8fPs3gl0XWmgtsus6%2BI9AXdtFR%2FC9cjJDF0ZRCcQeZuYKiOFNC9XzO64Kf7O1EqAW8M9IDjMC%2F4U4WbFf5SXSsKccnDb0gwCgB9F3%2BDFJitV8GZMqaeD7wJE6bJNIUQ4tBP0weoEsyPHjYzB6%2FYaemzx3jErhBj4bfIXmQ%2BETyZVdOdjTABNYLJ4Hn%2F7%2BZyVoHihLgPJ8K%2FWdarFBwxqUYo8jP%2BiRPe6NSvEVnTr%2FUGOGVOp3oR1pORFjIwo7CRFNWhuOT0rP5lMLvRh8H%2FMN275rwGOqUBGiOHVo1wobpKzLy5wTseHmwpFyWn4dCuauBHRAsOIrfPV5flUahIkzltTnRTdy8O2aA6%2FIYgC5Y6aDWooZH3kRs3ydoKH3xJBsqoKkB3nKSo0eyZsJ0zU0JuFSBg5K%2FkYp6vHrUGtO9TvS84E%2FM%2FquGZ%2BAxDN9qj6qfKdQz4ZrUoC0%2Bzg3YPHSuw4MynFxJ1FtkOMxuhA1a0GxmFw7zqZR%2FX%2FPCM&X-Amz-Signature=4e47f1fcfccfbf353ff507a6f0399bf157d8b21a81df911146fa70462636f5a8&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XFYAFY2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIH4THewt%2BN7EZ823kUVJ52V1c2fg8WHMuKcyabeiATr%2BAiEA4yI8eHsR8QM7hZH8pUmcHf4r4V50PYD2eeLtf2atL2cqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdRe5npzS%2FMKzoZgircA8jKAuSQyvZSoxuY%2FjFe7bQhvS%2BEhh3Y4dQzkAqCd8chdQDICl%2BYxciwDzr6500g5C4fj2EiGIxMYkYmqu1x9%2BFyCsgFWnHgTCEKrqOgoT%2BFNFD4fbCIFwGQxLEP5aOaZOkYwrxVfZi0MMPrWng602862Bbcd%2BAqi11JdTGzckdwpHNMaKvzdm%2BKoecbDkDZYdcBn0N2apAQ7dJdSQLFqT1Rv%2BS%2F6cff%2F%2BMxkdU8w8Vv5fHTKM9aiqKGqcb9rdqLUJh5m0smwzD1WMqYHB%2BmLy0JOTALLG99MMvOlmI9e4xquaX9OiP3tUlnj4MBfFt9LZISelivBix20I7BjIjb%2FWyuDe4s%2F3YTxJHM%2BGo8KDYUv%2F5X274w1lcUKsDAgWZGcbhZOf5yLRit1uxse8%2FyMm9c%2FR6I1KOIrA2vjaonZNnPJEcUyFm3HjI4IVWuYGZb7TW0iA%2FXfBgcAVxnZOYIOqk7yW4r%2FCA%2Ft7tLihon1iCxhpgoZLcmeWYaMbGRkSP1FCugl5WQebRcjsPYB%2BQmOrzAJqzJKa4ArA0MKnFoUaxhYNA%2BX8LzN%2FhHfrB8XDgx4PbgFGzoPBhKJqPs21IspXetmFXlAfXsIfnhBePlhkFJUuNVxzaaoDqrBocmMIi75rwGOqUBFhHpp0qJNPE0zupN1IxyzxEU5y5jspGZg%2BAIsH00gERge2aB1PAQySr2Y4LtdQXxccSnfMAozvMKA6XJrcLygnwxnJ4cSacCo4asoz1s%2BrBKJBrwSybAy1qWsO92%2F4w2AXc28t9SLvwnbUfKD3xUFA8ZLt8G62jVUmmpIKj%2BiKvh04FZgYea07XlniwMFOOSev7KcU1LHeaKm0TbUKp8O8GQiPEx&X-Amz-Signature=3a2797c265003fd0c669c0ad2da4a10f8680e1e26b9e1a050b352af57753249b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVDHPMSK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQD3eaO1IV%2BVYxp1zqIylykDpBkQVmUndlCjX%2F8Q1%2Bv4bgIhAOAWzLJwq0oMYT1DZS8p38AaEidGyXxYJ%2FzN%2BpNEui0yKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJQiNAzd0n26YeDNUq3APFv6%2F8%2FP3ivWJ7Vlwees2hA6xwcsgnKb%2BZi20hsxgpwhiPQZy%2BbQxY5xxKD4%2FNRKv3r9fzVn%2F2Avo8lUeg7X2YNPA5AOcadiQ4I5dpg4D3B0w72usdIZijYwsbLiQvDK2CBvsEkPxivg5NQ2CZl9hVPNZHZF8ZGZagfgyu3G3DaKNmtLIBcjus55rUNHGqhoGLDV6XbicttSh0Sc9YkUYkeTXa7yitJbNMMjBUcOruNNS3kDHF1EIciYfm8FKQIKJtctYly4Jl5CAernL0Dsmgidf9dfYo9%2Fe1Xk%2FJbmgvhlZduqPYaHmfQziC1gMmRtKJxDHLjKcuAx3PeF3CVED0XgNqnv5MOybcUHWKwc85lPxbfawIrplxobwHuuaxYf1fqTLEEDdVzvtrbC4dXln0o%2FdcqbfjRqsrLbfKcmcsAaCXxQ728owcdB3LKaozPqjvCWA9hZdtwhKu3W2RWptif68X%2BxVS9v1n8ePTCWtEfAing3dylqPTX2DiYpRwGnz8GVKq0jQwqi3gNkbGwAxNcXSKalSBjSvBgKOw4dqKfHHkvV6YlyM8cdOB8GCcFn%2F%2F01uVFHIC1wJ3tnDiLZi7X2Lpn6658PzbODtrs92YM8ZyRv8tkdZ%2BIec8pTDzuua8BjqkAcFX4yfIjF%2Fv3CJZOtfq5J%2B89GRof%2FEoX9nkWdzIryLOsrG5JgaiuSAlbTHJqXA%2B5CmwwFi022GDY7YoFAxRb4bZFWmRKHjJ0AdVm4pvADvFMzg3UCU2EldxGj5k9XKtVVLVQAOtP0Eg7FPOWi7s2q4ejzShhoGY3qBJrRl7Htv6JI1Y4cffasSeWB1fkvpUx3lrZdqrracTSH7OoP7DwvmaxodY&X-Amz-Signature=d8ae967b3253fe1c2d12aa10deb0610b05a1347bb534f7052459bd38cc5b4734&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVDHPMSK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQD3eaO1IV%2BVYxp1zqIylykDpBkQVmUndlCjX%2F8Q1%2Bv4bgIhAOAWzLJwq0oMYT1DZS8p38AaEidGyXxYJ%2FzN%2BpNEui0yKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJQiNAzd0n26YeDNUq3APFv6%2F8%2FP3ivWJ7Vlwees2hA6xwcsgnKb%2BZi20hsxgpwhiPQZy%2BbQxY5xxKD4%2FNRKv3r9fzVn%2F2Avo8lUeg7X2YNPA5AOcadiQ4I5dpg4D3B0w72usdIZijYwsbLiQvDK2CBvsEkPxivg5NQ2CZl9hVPNZHZF8ZGZagfgyu3G3DaKNmtLIBcjus55rUNHGqhoGLDV6XbicttSh0Sc9YkUYkeTXa7yitJbNMMjBUcOruNNS3kDHF1EIciYfm8FKQIKJtctYly4Jl5CAernL0Dsmgidf9dfYo9%2Fe1Xk%2FJbmgvhlZduqPYaHmfQziC1gMmRtKJxDHLjKcuAx3PeF3CVED0XgNqnv5MOybcUHWKwc85lPxbfawIrplxobwHuuaxYf1fqTLEEDdVzvtrbC4dXln0o%2FdcqbfjRqsrLbfKcmcsAaCXxQ728owcdB3LKaozPqjvCWA9hZdtwhKu3W2RWptif68X%2BxVS9v1n8ePTCWtEfAing3dylqPTX2DiYpRwGnz8GVKq0jQwqi3gNkbGwAxNcXSKalSBjSvBgKOw4dqKfHHkvV6YlyM8cdOB8GCcFn%2F%2F01uVFHIC1wJ3tnDiLZi7X2Lpn6658PzbODtrs92YM8ZyRv8tkdZ%2BIec8pTDzuua8BjqkAcFX4yfIjF%2Fv3CJZOtfq5J%2B89GRof%2FEoX9nkWdzIryLOsrG5JgaiuSAlbTHJqXA%2B5CmwwFi022GDY7YoFAxRb4bZFWmRKHjJ0AdVm4pvADvFMzg3UCU2EldxGj5k9XKtVVLVQAOtP0Eg7FPOWi7s2q4ejzShhoGY3qBJrRl7Htv6JI1Y4cffasSeWB1fkvpUx3lrZdqrracTSH7OoP7DwvmaxodY&X-Amz-Signature=c9ff25d6a54f7b31edfd57dd19c1dff6c1772a012ad59475cd9c80301b15ab75&X-Amz-SignedHeaders=host&x-id=GetObject)

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
