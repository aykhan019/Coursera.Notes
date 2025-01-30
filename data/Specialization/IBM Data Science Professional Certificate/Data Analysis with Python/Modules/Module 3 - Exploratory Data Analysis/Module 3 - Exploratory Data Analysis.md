

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4HKU77A%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEtgwAli1XlMQW2xmnj345ZcDQ%2BNVEuCEAqRvGzL7lcnAiB3lXmPkfZUHFYitjy1JbvN%2FWio7rVgoXRZ16t7xBGFnyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJFwlxxlXfE3ZkUo0KtwDdVBTu5nnQZnU%2BtnCsJfRMizh3zI6aMD6OVltXyPbYK7XdeRtr032OOG76xEgP2VCai3i4CFhzlsjBTNN2qBUYvGevzRCgb1hgyQbxMA0P31FHGogaKtFqp4ujAhCNX2d%2BLCUD3MxnBuO1Aq757%2FokaCIRfAppaCcRdKu55uKrNt2MmLlLOSFS9HxvUxI4NoqKLK4zZyn8msBHbL3OE1jetVzUQEopsYAHSc9VQtkYqlQhLHB%2FJzljjaBu1Au7%2FRj2sng7TFKgmBrfECR3%2BMiWUeU2LIWLIP1yaeD1mtI1tCKJQuTA6Um1gl33T5v2eOLU68mku4zHUTWTfLfuJSt4lOIIRQux5pfKojwFnhG4i4hsYxrK4ksuve4wnKWuvnpiCF3XLpiFyLSqRe1w27uDA%2FasU6Np0LcUqUkIrMcTpmneCQ4LB%2BmAPDKw7hnrhTSxIn%2BfAEBTlygR%2Fl1sWkFGMDcWZK6d3Z6qhPzTgvQKRhiFY%2By%2F9P6azvG4yL74LO%2FQpWcnkqAlZ6QydghAo87mlnowIHj8Wy3%2FvDEFHtxgAul6521zgfOGsB16VCWm%2Bcw6ZBxWoKepWzKMcT0V2Gwr85UnPKsX3ku1MxSRO7ojsHekkBm46DJktWEuCswvaPsvAY6pgE%2BGw97ECzr02rxg5k3%2FhdlLZ2CIr1ZsgP1oYuVW6mBMB4HxnFMDE10MAgczTKJYFZTuZ19GQ4xRK1HUfx03uGsUiwFq95HQEE52UFh2agLUoDsCFf4IW4bfeS%2BjVwOTkiXOSUx2SoJ03r5msZadpm3osNAD28B37XtOj2u%2F%2B8sjMwZ4HtV9YgHy7Lo%2FT4O%2BzeOsd3ZSL8d184d9bwZSfM4EkH78VA0&X-Amz-Signature=d539c1e87850d59d028bf399bd7e593dbb368d0bcedebc3b808707327a418c8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4HKU77A%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEtgwAli1XlMQW2xmnj345ZcDQ%2BNVEuCEAqRvGzL7lcnAiB3lXmPkfZUHFYitjy1JbvN%2FWio7rVgoXRZ16t7xBGFnyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJFwlxxlXfE3ZkUo0KtwDdVBTu5nnQZnU%2BtnCsJfRMizh3zI6aMD6OVltXyPbYK7XdeRtr032OOG76xEgP2VCai3i4CFhzlsjBTNN2qBUYvGevzRCgb1hgyQbxMA0P31FHGogaKtFqp4ujAhCNX2d%2BLCUD3MxnBuO1Aq757%2FokaCIRfAppaCcRdKu55uKrNt2MmLlLOSFS9HxvUxI4NoqKLK4zZyn8msBHbL3OE1jetVzUQEopsYAHSc9VQtkYqlQhLHB%2FJzljjaBu1Au7%2FRj2sng7TFKgmBrfECR3%2BMiWUeU2LIWLIP1yaeD1mtI1tCKJQuTA6Um1gl33T5v2eOLU68mku4zHUTWTfLfuJSt4lOIIRQux5pfKojwFnhG4i4hsYxrK4ksuve4wnKWuvnpiCF3XLpiFyLSqRe1w27uDA%2FasU6Np0LcUqUkIrMcTpmneCQ4LB%2BmAPDKw7hnrhTSxIn%2BfAEBTlygR%2Fl1sWkFGMDcWZK6d3Z6qhPzTgvQKRhiFY%2By%2F9P6azvG4yL74LO%2FQpWcnkqAlZ6QydghAo87mlnowIHj8Wy3%2FvDEFHtxgAul6521zgfOGsB16VCWm%2Bcw6ZBxWoKepWzKMcT0V2Gwr85UnPKsX3ku1MxSRO7ojsHekkBm46DJktWEuCswvaPsvAY6pgE%2BGw97ECzr02rxg5k3%2FhdlLZ2CIr1ZsgP1oYuVW6mBMB4HxnFMDE10MAgczTKJYFZTuZ19GQ4xRK1HUfx03uGsUiwFq95HQEE52UFh2agLUoDsCFf4IW4bfeS%2BjVwOTkiXOSUx2SoJ03r5msZadpm3osNAD28B37XtOj2u%2F%2B8sjMwZ4HtV9YgHy7Lo%2FT4O%2BzeOsd3ZSL8d184d9bwZSfM4EkH78VA0&X-Amz-Signature=8084623ce8beee60fe747fc49073b745eee5824a9d3ce4331040b9862f9c1755&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4HKU77A%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEtgwAli1XlMQW2xmnj345ZcDQ%2BNVEuCEAqRvGzL7lcnAiB3lXmPkfZUHFYitjy1JbvN%2FWio7rVgoXRZ16t7xBGFnyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJFwlxxlXfE3ZkUo0KtwDdVBTu5nnQZnU%2BtnCsJfRMizh3zI6aMD6OVltXyPbYK7XdeRtr032OOG76xEgP2VCai3i4CFhzlsjBTNN2qBUYvGevzRCgb1hgyQbxMA0P31FHGogaKtFqp4ujAhCNX2d%2BLCUD3MxnBuO1Aq757%2FokaCIRfAppaCcRdKu55uKrNt2MmLlLOSFS9HxvUxI4NoqKLK4zZyn8msBHbL3OE1jetVzUQEopsYAHSc9VQtkYqlQhLHB%2FJzljjaBu1Au7%2FRj2sng7TFKgmBrfECR3%2BMiWUeU2LIWLIP1yaeD1mtI1tCKJQuTA6Um1gl33T5v2eOLU68mku4zHUTWTfLfuJSt4lOIIRQux5pfKojwFnhG4i4hsYxrK4ksuve4wnKWuvnpiCF3XLpiFyLSqRe1w27uDA%2FasU6Np0LcUqUkIrMcTpmneCQ4LB%2BmAPDKw7hnrhTSxIn%2BfAEBTlygR%2Fl1sWkFGMDcWZK6d3Z6qhPzTgvQKRhiFY%2By%2F9P6azvG4yL74LO%2FQpWcnkqAlZ6QydghAo87mlnowIHj8Wy3%2FvDEFHtxgAul6521zgfOGsB16VCWm%2Bcw6ZBxWoKepWzKMcT0V2Gwr85UnPKsX3ku1MxSRO7ojsHekkBm46DJktWEuCswvaPsvAY6pgE%2BGw97ECzr02rxg5k3%2FhdlLZ2CIr1ZsgP1oYuVW6mBMB4HxnFMDE10MAgczTKJYFZTuZ19GQ4xRK1HUfx03uGsUiwFq95HQEE52UFh2agLUoDsCFf4IW4bfeS%2BjVwOTkiXOSUx2SoJ03r5msZadpm3osNAD28B37XtOj2u%2F%2B8sjMwZ4HtV9YgHy7Lo%2FT4O%2BzeOsd3ZSL8d184d9bwZSfM4EkH78VA0&X-Amz-Signature=d98fc26363ebf15e0116ecb19a440b818aa21604741a101ffa5fccce8aa4e1df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BSBDSCX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWbZH462%2BLY1j9qfoDjPH6fT5QZGIahhLPVmBrQv7BnAiAPxRqKFQcfhMS4vU4LhCEctvdnktFBxvi%2Fq9Dr5cf3NiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHUc3KRclq47f4dnKtwDOlMH9ABzSj08S5X5vi3ZHJDYTkqByX49mr%2FqwfwVQroWyfR8YRifpqi%2FffUFtLXQYDZczZ1cX55VbOCgqme5jSxdD6AM%2BVhnrpg9%2B%2FM%2FfNloytr2P44cmQoNbKd4KDL2UJOf9f39V4jL0AWvpPEZKH%2Fuq4ysryR8AeNqWHbIEmGBGLjxDVSm1qzfu2fdLEU1s5nD8NqhnAPMn2PBJsE%2F8yYHpxAjRNhmZAxiBZ9h0Cr%2B%2Fh4Ru47gbjvjbV%2B9CIwEtFSz%2FwEFThg2iiEOu7HALD%2Fa9O%2BNDDNsgi%2FdHy7RVO90YQuHp1wzkpV3ZpIpIbL%2B%2B%2B97AcqJq20NQnZAs1WxDmmQUvjGQgP7bjTfpLlXhKceA%2Fjbx%2BKtuXLMIAfNDzYHpxOl9AZEi065o9c1Ng1veKjVBeGMyLwQR8EwzKfe7ZDO7ofN6avY%2FdFlHju5t1pbv8LcFCBvtDatVD%2BZP8wlRvnLbbXwQqmE6NflK8X%2FMclb%2FyOEQsnPU32y3EAPU6Pd%2FdEvoTjPYVRgLQuqy80hRQxsXYitHONgrGA30RnDZnDtgEYxYhHs3MyOGGBTyfnawob24jxULbWI2tvSFTllIYF1HIjYUKb3ytXBqyhPXB2ZNiSfvuNSdiDlTSwwmqPsvAY6pgF3s9KI95Ym%2FKnnuZxJVWgfuBMiAmcAN4XXuE4pZ2lc6xW7b79i2mcuUgr8trvi159YjbqYf2MZgBmzgV43jZ3sEI1HRep9Q3tJ6uWbbgnPqrEstgY5UCuFPa3MHJkz0USe%2FpcksNo0dfRyCDtdzaqAAJdK6BzX29joqQBcZb4j6CnA3D%2BtjveFZLjWBRs147I%2BsiaLJrPqDMPz2d2HZUSM4KDjskSH&X-Amz-Signature=cc8c9ce35d7e2cd63f4e5f3ac6c39f7988cd90472e7ea189306710f997eed9ce&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BSBDSCX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWbZH462%2BLY1j9qfoDjPH6fT5QZGIahhLPVmBrQv7BnAiAPxRqKFQcfhMS4vU4LhCEctvdnktFBxvi%2Fq9Dr5cf3NiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHUc3KRclq47f4dnKtwDOlMH9ABzSj08S5X5vi3ZHJDYTkqByX49mr%2FqwfwVQroWyfR8YRifpqi%2FffUFtLXQYDZczZ1cX55VbOCgqme5jSxdD6AM%2BVhnrpg9%2B%2FM%2FfNloytr2P44cmQoNbKd4KDL2UJOf9f39V4jL0AWvpPEZKH%2Fuq4ysryR8AeNqWHbIEmGBGLjxDVSm1qzfu2fdLEU1s5nD8NqhnAPMn2PBJsE%2F8yYHpxAjRNhmZAxiBZ9h0Cr%2B%2Fh4Ru47gbjvjbV%2B9CIwEtFSz%2FwEFThg2iiEOu7HALD%2Fa9O%2BNDDNsgi%2FdHy7RVO90YQuHp1wzkpV3ZpIpIbL%2B%2B%2B97AcqJq20NQnZAs1WxDmmQUvjGQgP7bjTfpLlXhKceA%2Fjbx%2BKtuXLMIAfNDzYHpxOl9AZEi065o9c1Ng1veKjVBeGMyLwQR8EwzKfe7ZDO7ofN6avY%2FdFlHju5t1pbv8LcFCBvtDatVD%2BZP8wlRvnLbbXwQqmE6NflK8X%2FMclb%2FyOEQsnPU32y3EAPU6Pd%2FdEvoTjPYVRgLQuqy80hRQxsXYitHONgrGA30RnDZnDtgEYxYhHs3MyOGGBTyfnawob24jxULbWI2tvSFTllIYF1HIjYUKb3ytXBqyhPXB2ZNiSfvuNSdiDlTSwwmqPsvAY6pgF3s9KI95Ym%2FKnnuZxJVWgfuBMiAmcAN4XXuE4pZ2lc6xW7b79i2mcuUgr8trvi159YjbqYf2MZgBmzgV43jZ3sEI1HRep9Q3tJ6uWbbgnPqrEstgY5UCuFPa3MHJkz0USe%2FpcksNo0dfRyCDtdzaqAAJdK6BzX29joqQBcZb4j6CnA3D%2BtjveFZLjWBRs147I%2BsiaLJrPqDMPz2d2HZUSM4KDjskSH&X-Amz-Signature=dfd602e4ebe9b6c750c1e8f13c1fdbb2139c3f703474aa01d373457cb339d46d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BSBDSCX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWbZH462%2BLY1j9qfoDjPH6fT5QZGIahhLPVmBrQv7BnAiAPxRqKFQcfhMS4vU4LhCEctvdnktFBxvi%2Fq9Dr5cf3NiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHUc3KRclq47f4dnKtwDOlMH9ABzSj08S5X5vi3ZHJDYTkqByX49mr%2FqwfwVQroWyfR8YRifpqi%2FffUFtLXQYDZczZ1cX55VbOCgqme5jSxdD6AM%2BVhnrpg9%2B%2FM%2FfNloytr2P44cmQoNbKd4KDL2UJOf9f39V4jL0AWvpPEZKH%2Fuq4ysryR8AeNqWHbIEmGBGLjxDVSm1qzfu2fdLEU1s5nD8NqhnAPMn2PBJsE%2F8yYHpxAjRNhmZAxiBZ9h0Cr%2B%2Fh4Ru47gbjvjbV%2B9CIwEtFSz%2FwEFThg2iiEOu7HALD%2Fa9O%2BNDDNsgi%2FdHy7RVO90YQuHp1wzkpV3ZpIpIbL%2B%2B%2B97AcqJq20NQnZAs1WxDmmQUvjGQgP7bjTfpLlXhKceA%2Fjbx%2BKtuXLMIAfNDzYHpxOl9AZEi065o9c1Ng1veKjVBeGMyLwQR8EwzKfe7ZDO7ofN6avY%2FdFlHju5t1pbv8LcFCBvtDatVD%2BZP8wlRvnLbbXwQqmE6NflK8X%2FMclb%2FyOEQsnPU32y3EAPU6Pd%2FdEvoTjPYVRgLQuqy80hRQxsXYitHONgrGA30RnDZnDtgEYxYhHs3MyOGGBTyfnawob24jxULbWI2tvSFTllIYF1HIjYUKb3ytXBqyhPXB2ZNiSfvuNSdiDlTSwwmqPsvAY6pgF3s9KI95Ym%2FKnnuZxJVWgfuBMiAmcAN4XXuE4pZ2lc6xW7b79i2mcuUgr8trvi159YjbqYf2MZgBmzgV43jZ3sEI1HRep9Q3tJ6uWbbgnPqrEstgY5UCuFPa3MHJkz0USe%2FpcksNo0dfRyCDtdzaqAAJdK6BzX29joqQBcZb4j6CnA3D%2BtjveFZLjWBRs147I%2BsiaLJrPqDMPz2d2HZUSM4KDjskSH&X-Amz-Signature=b24d2ca947b70c500072c98f9d2746f0034d35ca7d168202bd1b6fa657791067&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BSBDSCX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWbZH462%2BLY1j9qfoDjPH6fT5QZGIahhLPVmBrQv7BnAiAPxRqKFQcfhMS4vU4LhCEctvdnktFBxvi%2Fq9Dr5cf3NiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHUc3KRclq47f4dnKtwDOlMH9ABzSj08S5X5vi3ZHJDYTkqByX49mr%2FqwfwVQroWyfR8YRifpqi%2FffUFtLXQYDZczZ1cX55VbOCgqme5jSxdD6AM%2BVhnrpg9%2B%2FM%2FfNloytr2P44cmQoNbKd4KDL2UJOf9f39V4jL0AWvpPEZKH%2Fuq4ysryR8AeNqWHbIEmGBGLjxDVSm1qzfu2fdLEU1s5nD8NqhnAPMn2PBJsE%2F8yYHpxAjRNhmZAxiBZ9h0Cr%2B%2Fh4Ru47gbjvjbV%2B9CIwEtFSz%2FwEFThg2iiEOu7HALD%2Fa9O%2BNDDNsgi%2FdHy7RVO90YQuHp1wzkpV3ZpIpIbL%2B%2B%2B97AcqJq20NQnZAs1WxDmmQUvjGQgP7bjTfpLlXhKceA%2Fjbx%2BKtuXLMIAfNDzYHpxOl9AZEi065o9c1Ng1veKjVBeGMyLwQR8EwzKfe7ZDO7ofN6avY%2FdFlHju5t1pbv8LcFCBvtDatVD%2BZP8wlRvnLbbXwQqmE6NflK8X%2FMclb%2FyOEQsnPU32y3EAPU6Pd%2FdEvoTjPYVRgLQuqy80hRQxsXYitHONgrGA30RnDZnDtgEYxYhHs3MyOGGBTyfnawob24jxULbWI2tvSFTllIYF1HIjYUKb3ytXBqyhPXB2ZNiSfvuNSdiDlTSwwmqPsvAY6pgF3s9KI95Ym%2FKnnuZxJVWgfuBMiAmcAN4XXuE4pZ2lc6xW7b79i2mcuUgr8trvi159YjbqYf2MZgBmzgV43jZ3sEI1HRep9Q3tJ6uWbbgnPqrEstgY5UCuFPa3MHJkz0USe%2FpcksNo0dfRyCDtdzaqAAJdK6BzX29joqQBcZb4j6CnA3D%2BtjveFZLjWBRs147I%2BsiaLJrPqDMPz2d2HZUSM4KDjskSH&X-Amz-Signature=6a3e8158f6ac287ae939d4c7e44f492ff8ed6ca89f29db3e381e8977d0b92573&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BSBDSCX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWbZH462%2BLY1j9qfoDjPH6fT5QZGIahhLPVmBrQv7BnAiAPxRqKFQcfhMS4vU4LhCEctvdnktFBxvi%2Fq9Dr5cf3NiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHUc3KRclq47f4dnKtwDOlMH9ABzSj08S5X5vi3ZHJDYTkqByX49mr%2FqwfwVQroWyfR8YRifpqi%2FffUFtLXQYDZczZ1cX55VbOCgqme5jSxdD6AM%2BVhnrpg9%2B%2FM%2FfNloytr2P44cmQoNbKd4KDL2UJOf9f39V4jL0AWvpPEZKH%2Fuq4ysryR8AeNqWHbIEmGBGLjxDVSm1qzfu2fdLEU1s5nD8NqhnAPMn2PBJsE%2F8yYHpxAjRNhmZAxiBZ9h0Cr%2B%2Fh4Ru47gbjvjbV%2B9CIwEtFSz%2FwEFThg2iiEOu7HALD%2Fa9O%2BNDDNsgi%2FdHy7RVO90YQuHp1wzkpV3ZpIpIbL%2B%2B%2B97AcqJq20NQnZAs1WxDmmQUvjGQgP7bjTfpLlXhKceA%2Fjbx%2BKtuXLMIAfNDzYHpxOl9AZEi065o9c1Ng1veKjVBeGMyLwQR8EwzKfe7ZDO7ofN6avY%2FdFlHju5t1pbv8LcFCBvtDatVD%2BZP8wlRvnLbbXwQqmE6NflK8X%2FMclb%2FyOEQsnPU32y3EAPU6Pd%2FdEvoTjPYVRgLQuqy80hRQxsXYitHONgrGA30RnDZnDtgEYxYhHs3MyOGGBTyfnawob24jxULbWI2tvSFTllIYF1HIjYUKb3ytXBqyhPXB2ZNiSfvuNSdiDlTSwwmqPsvAY6pgF3s9KI95Ym%2FKnnuZxJVWgfuBMiAmcAN4XXuE4pZ2lc6xW7b79i2mcuUgr8trvi159YjbqYf2MZgBmzgV43jZ3sEI1HRep9Q3tJ6uWbbgnPqrEstgY5UCuFPa3MHJkz0USe%2FpcksNo0dfRyCDtdzaqAAJdK6BzX29joqQBcZb4j6CnA3D%2BtjveFZLjWBRs147I%2BsiaLJrPqDMPz2d2HZUSM4KDjskSH&X-Amz-Signature=6d76b4685411b5aea3157ef27b4e596da23cc809cdbaa543d12b45a4cb1737ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BSBDSCX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWbZH462%2BLY1j9qfoDjPH6fT5QZGIahhLPVmBrQv7BnAiAPxRqKFQcfhMS4vU4LhCEctvdnktFBxvi%2Fq9Dr5cf3NiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHUc3KRclq47f4dnKtwDOlMH9ABzSj08S5X5vi3ZHJDYTkqByX49mr%2FqwfwVQroWyfR8YRifpqi%2FffUFtLXQYDZczZ1cX55VbOCgqme5jSxdD6AM%2BVhnrpg9%2B%2FM%2FfNloytr2P44cmQoNbKd4KDL2UJOf9f39V4jL0AWvpPEZKH%2Fuq4ysryR8AeNqWHbIEmGBGLjxDVSm1qzfu2fdLEU1s5nD8NqhnAPMn2PBJsE%2F8yYHpxAjRNhmZAxiBZ9h0Cr%2B%2Fh4Ru47gbjvjbV%2B9CIwEtFSz%2FwEFThg2iiEOu7HALD%2Fa9O%2BNDDNsgi%2FdHy7RVO90YQuHp1wzkpV3ZpIpIbL%2B%2B%2B97AcqJq20NQnZAs1WxDmmQUvjGQgP7bjTfpLlXhKceA%2Fjbx%2BKtuXLMIAfNDzYHpxOl9AZEi065o9c1Ng1veKjVBeGMyLwQR8EwzKfe7ZDO7ofN6avY%2FdFlHju5t1pbv8LcFCBvtDatVD%2BZP8wlRvnLbbXwQqmE6NflK8X%2FMclb%2FyOEQsnPU32y3EAPU6Pd%2FdEvoTjPYVRgLQuqy80hRQxsXYitHONgrGA30RnDZnDtgEYxYhHs3MyOGGBTyfnawob24jxULbWI2tvSFTllIYF1HIjYUKb3ytXBqyhPXB2ZNiSfvuNSdiDlTSwwmqPsvAY6pgF3s9KI95Ym%2FKnnuZxJVWgfuBMiAmcAN4XXuE4pZ2lc6xW7b79i2mcuUgr8trvi159YjbqYf2MZgBmzgV43jZ3sEI1HRep9Q3tJ6uWbbgnPqrEstgY5UCuFPa3MHJkz0USe%2FpcksNo0dfRyCDtdzaqAAJdK6BzX29joqQBcZb4j6CnA3D%2BtjveFZLjWBRs147I%2BsiaLJrPqDMPz2d2HZUSM4KDjskSH&X-Amz-Signature=d5abfadada0ed883e5088542de322173ec032ec0f93c73123de996b043932f49&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI2ZNCD7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm%2BQyj32AU0kH5%2F6zgU2Z7iBIJZY200Omt%2FO%2BorN5IrAIgTlOLL%2Ba5s1nLOSHXUnA8qOYK1owQWxIMENxS0%2FSOcFIqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHrtem8PbHjBNG5pircA%2FdEbBSxd4BItC1%2BEzMj2hEhNjpATq%2ByBl3tM504udTKvxrhJ1utqgkae1Z6rAVNKIqyz1Y3%2BzQ5%2FLwLk8J4C%2FUNYaDJa20csPUvLinbnj8P0aTmydbD6%2FpcovaxLmvybIZp2niglzQJIiWxSVKw%2FqVgYxIHcGKe0Q2W%2Bu4WVYKayQYyR%2BLJHAnrDtkgd0FYdAXPJ5wlsogD43E0T4J7NZWzUx3sPh%2B0VfoAPdkTpV6Z6LPppOC6NRu9ADkR5j4V8utpxW2CF%2BTXVoMVYV12sXc8Ogj33rNtCggCXDDlyIJcgyXuBgzJH9dyT%2FrIAgh6jt8QtkE7FZ95u5FzpxiK5a3eM%2FgjC7ZHxM8tAbRrN0kOyxbtPlrtbJK0AD126l3cNGhVzhUavqHe1VC7XxkJH2fgUZHTI%2BwQlriCTobLZNpAy6%2BuN4wlFXses%2FZkefbPFuxwpiJOc%2FN53A8E7Knmd5BxOsafc8Cy1kS1USHo97zCwt8MPb7brWUFj96i0hA%2F8ZPHcJym1uN8vW8b5i%2FBPJfOdd3B5yUjnXRgwH2DMJOei19ZXOKJUPc8Y5juSNbhDGA9zG0Np2fQIWAoZC2lt2%2FnGoYwJvVLhVrWX8W%2F3G048DPl1Ox0zf9jtbmxMM%2Bi7LwGOqUBOcsC98WIE24tTjEig5yxvpBct0iGFmqQEXgdwNw7kBavglUuUUD5bc%2F5Ldfozz0xnA9SUUARXS9eq7fPPYcH0hZVsM8Q%2BP2myi9%2BK9Q%2FApmOSd%2FP754vadl90Incsdik385eepJQ%2Bdr%2Fxyx6Uloc1baSTWJW0TZt2HRxjAYfXw5%2FvBEUyp63ujkNhTblKry6ERRrdH3CZsx0ECCFdH2lzfq0xKrn&X-Amz-Signature=23dfb41e4f3839e1277329b641370626d1e872864939620aa39a8eab4a6ea55f&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3RLCA2R%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FdYQcR32%2FFxErap4K3z3NJfUHXPvMDIIuD6PdqWzqSAiAmbnkAjMr3RWy41oYIUvR%2B4oa1gulABMvz%2FLKRvhBLXSqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3OxP7lnB5UahMtMQKtwDwOQSs8U8GFYn6HfJcGqv%2B0oTGNBemQFq26VBbx4XNvPrhqognhnnFiEDfI2J%2FWo2g2UExKVWoSxHp%2BxQc%2Fzi1OFZI96aNxlvE92GytCl4pN9MnD%2FanSDHFV1vAJfH1tX2DIFNApFwq82QMLPcDfc37cQtYeWTT3F3G6wPkSnCu4utEJEic1Gn2cjfKymk7%2BfgSewE4X9hpoE6ng7GI2YEr8wzeAEzyX69mqWkKHGFrUfUesZA5f4RSE3WMieuwGQycwgznRy1Ma7Zfs1ObYtgGFKyOen0rTjl1PPpRhg%2FenaRSursDO72w6CAw%2FtLYX7ed2rtJbiuYbnryGptWjLyOqjgwG%2FcWwdruELukS%2BorOO4qRSbTuMh9IdzD0wRgSOxz3gP72e8tlSUpIIeFbxwWSJZTNSCkcYUGQ0QxUfwKzo0wP2WD8CxUXCVWMAHIBof74EDqpifRVChinb47iYhlly9Dac45Hidxnixc0XcC4XH%2B1pAjiZzVaUk6KO696omCGsy5kaA8ZoaKy%2F%2FZujhhRNQYNAeDa6vKKUhkQtU4kaBfYZEKoN%2BX1PvGHsCcmfwNko2GDuh5j%2BOGY2jj20FOSlZTcnMoF4bSkOUGmOM6EmPPhQ60X4aFiF%2B4gwwKLsvAY6pgHJpNKjf%2FKyFXzhF54KNxUDO%2By0zK%2FgYwVM5tuV%2FykGwlQECXFQp1gJLJPfXXfFtlAbiCor3EZoBTfrFsnQ%2B8oMv9ae%2FYn%2FhIFvZRB%2FhpC%2F9pyIIsw6z6d18x4DrBNRWF4fTIrU%2F7UvQReE1a7TK%2Fk177ymUmb%2BmV6W2MUsdAE17QFre9BHLstr01KHye1DEsytLY%2FDvbal1nN6ne36OxmMS83ovh4W&X-Amz-Signature=8e6cdfc9b783324e0fc4bd56c225ca34480ee088414ba988b6a3b310a157292b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BSBDSCX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWbZH462%2BLY1j9qfoDjPH6fT5QZGIahhLPVmBrQv7BnAiAPxRqKFQcfhMS4vU4LhCEctvdnktFBxvi%2Fq9Dr5cf3NiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHUc3KRclq47f4dnKtwDOlMH9ABzSj08S5X5vi3ZHJDYTkqByX49mr%2FqwfwVQroWyfR8YRifpqi%2FffUFtLXQYDZczZ1cX55VbOCgqme5jSxdD6AM%2BVhnrpg9%2B%2FM%2FfNloytr2P44cmQoNbKd4KDL2UJOf9f39V4jL0AWvpPEZKH%2Fuq4ysryR8AeNqWHbIEmGBGLjxDVSm1qzfu2fdLEU1s5nD8NqhnAPMn2PBJsE%2F8yYHpxAjRNhmZAxiBZ9h0Cr%2B%2Fh4Ru47gbjvjbV%2B9CIwEtFSz%2FwEFThg2iiEOu7HALD%2Fa9O%2BNDDNsgi%2FdHy7RVO90YQuHp1wzkpV3ZpIpIbL%2B%2B%2B97AcqJq20NQnZAs1WxDmmQUvjGQgP7bjTfpLlXhKceA%2Fjbx%2BKtuXLMIAfNDzYHpxOl9AZEi065o9c1Ng1veKjVBeGMyLwQR8EwzKfe7ZDO7ofN6avY%2FdFlHju5t1pbv8LcFCBvtDatVD%2BZP8wlRvnLbbXwQqmE6NflK8X%2FMclb%2FyOEQsnPU32y3EAPU6Pd%2FdEvoTjPYVRgLQuqy80hRQxsXYitHONgrGA30RnDZnDtgEYxYhHs3MyOGGBTyfnawob24jxULbWI2tvSFTllIYF1HIjYUKb3ytXBqyhPXB2ZNiSfvuNSdiDlTSwwmqPsvAY6pgF3s9KI95Ym%2FKnnuZxJVWgfuBMiAmcAN4XXuE4pZ2lc6xW7b79i2mcuUgr8trvi159YjbqYf2MZgBmzgV43jZ3sEI1HRep9Q3tJ6uWbbgnPqrEstgY5UCuFPa3MHJkz0USe%2FpcksNo0dfRyCDtdzaqAAJdK6BzX29joqQBcZb4j6CnA3D%2BtjveFZLjWBRs147I%2BsiaLJrPqDMPz2d2HZUSM4KDjskSH&X-Amz-Signature=4acc25e31874f541e854fb10e1d5736005d9a2d27824729c5bf6f0680481e37c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BSBDSCX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWbZH462%2BLY1j9qfoDjPH6fT5QZGIahhLPVmBrQv7BnAiAPxRqKFQcfhMS4vU4LhCEctvdnktFBxvi%2Fq9Dr5cf3NiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHUc3KRclq47f4dnKtwDOlMH9ABzSj08S5X5vi3ZHJDYTkqByX49mr%2FqwfwVQroWyfR8YRifpqi%2FffUFtLXQYDZczZ1cX55VbOCgqme5jSxdD6AM%2BVhnrpg9%2B%2FM%2FfNloytr2P44cmQoNbKd4KDL2UJOf9f39V4jL0AWvpPEZKH%2Fuq4ysryR8AeNqWHbIEmGBGLjxDVSm1qzfu2fdLEU1s5nD8NqhnAPMn2PBJsE%2F8yYHpxAjRNhmZAxiBZ9h0Cr%2B%2Fh4Ru47gbjvjbV%2B9CIwEtFSz%2FwEFThg2iiEOu7HALD%2Fa9O%2BNDDNsgi%2FdHy7RVO90YQuHp1wzkpV3ZpIpIbL%2B%2B%2B97AcqJq20NQnZAs1WxDmmQUvjGQgP7bjTfpLlXhKceA%2Fjbx%2BKtuXLMIAfNDzYHpxOl9AZEi065o9c1Ng1veKjVBeGMyLwQR8EwzKfe7ZDO7ofN6avY%2FdFlHju5t1pbv8LcFCBvtDatVD%2BZP8wlRvnLbbXwQqmE6NflK8X%2FMclb%2FyOEQsnPU32y3EAPU6Pd%2FdEvoTjPYVRgLQuqy80hRQxsXYitHONgrGA30RnDZnDtgEYxYhHs3MyOGGBTyfnawob24jxULbWI2tvSFTllIYF1HIjYUKb3ytXBqyhPXB2ZNiSfvuNSdiDlTSwwmqPsvAY6pgF3s9KI95Ym%2FKnnuZxJVWgfuBMiAmcAN4XXuE4pZ2lc6xW7b79i2mcuUgr8trvi159YjbqYf2MZgBmzgV43jZ3sEI1HRep9Q3tJ6uWbbgnPqrEstgY5UCuFPa3MHJkz0USe%2FpcksNo0dfRyCDtdzaqAAJdK6BzX29joqQBcZb4j6CnA3D%2BtjveFZLjWBRs147I%2BsiaLJrPqDMPz2d2HZUSM4KDjskSH&X-Amz-Signature=87df0cfc1ddf43360e2bb9a06d705bb9d9bac240ec203ab16ae79ad65312df62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BSBDSCX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWbZH462%2BLY1j9qfoDjPH6fT5QZGIahhLPVmBrQv7BnAiAPxRqKFQcfhMS4vU4LhCEctvdnktFBxvi%2Fq9Dr5cf3NiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHUc3KRclq47f4dnKtwDOlMH9ABzSj08S5X5vi3ZHJDYTkqByX49mr%2FqwfwVQroWyfR8YRifpqi%2FffUFtLXQYDZczZ1cX55VbOCgqme5jSxdD6AM%2BVhnrpg9%2B%2FM%2FfNloytr2P44cmQoNbKd4KDL2UJOf9f39V4jL0AWvpPEZKH%2Fuq4ysryR8AeNqWHbIEmGBGLjxDVSm1qzfu2fdLEU1s5nD8NqhnAPMn2PBJsE%2F8yYHpxAjRNhmZAxiBZ9h0Cr%2B%2Fh4Ru47gbjvjbV%2B9CIwEtFSz%2FwEFThg2iiEOu7HALD%2Fa9O%2BNDDNsgi%2FdHy7RVO90YQuHp1wzkpV3ZpIpIbL%2B%2B%2B97AcqJq20NQnZAs1WxDmmQUvjGQgP7bjTfpLlXhKceA%2Fjbx%2BKtuXLMIAfNDzYHpxOl9AZEi065o9c1Ng1veKjVBeGMyLwQR8EwzKfe7ZDO7ofN6avY%2FdFlHju5t1pbv8LcFCBvtDatVD%2BZP8wlRvnLbbXwQqmE6NflK8X%2FMclb%2FyOEQsnPU32y3EAPU6Pd%2FdEvoTjPYVRgLQuqy80hRQxsXYitHONgrGA30RnDZnDtgEYxYhHs3MyOGGBTyfnawob24jxULbWI2tvSFTllIYF1HIjYUKb3ytXBqyhPXB2ZNiSfvuNSdiDlTSwwmqPsvAY6pgF3s9KI95Ym%2FKnnuZxJVWgfuBMiAmcAN4XXuE4pZ2lc6xW7b79i2mcuUgr8trvi159YjbqYf2MZgBmzgV43jZ3sEI1HRep9Q3tJ6uWbbgnPqrEstgY5UCuFPa3MHJkz0USe%2FpcksNo0dfRyCDtdzaqAAJdK6BzX29joqQBcZb4j6CnA3D%2BtjveFZLjWBRs147I%2BsiaLJrPqDMPz2d2HZUSM4KDjskSH&X-Amz-Signature=563d0316c95aee2447f3786b3ff4abf1720a751f10a631d3f1ce57df853761b0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BPPLYXE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBQl2RukQ4%2Bn34%2B6jxSJ8OVLXIW3ZHu81Lzaz0ebGvh8AiAoVIgMbe1Li7f%2B1gwfOksC8CkVLA8GRhGFuJXNCRcHLiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMk0qI3bsl8ky47WqtKtwDx8orrjNR8NLAsBrA3nFxNcdE7NbqILiEPF5gDnw6GJbkz2BLsU2VApv2vMqvXrDx5Y2i2QQ7rvtNXedrx2nNBIDCUtXmKdet3T%2FBjt2ZPdvHqtW0j8Kb5knGwgvP4rSlCYnF%2BzLzx%2BpIscwkMQxA0ZWcN5aDFsu4rglqFH%2BGubi3Kpfp0bKHBADsyDCT2CKuGYwLGWxPrrm9eiqgcp5CRvyaaCwGN%2FGOskgDqPHK6e0qCXXY%2FXtATY7pWza7%2F5NaQYBzLIyu4rl7DZSgnspHG%2BAn%2B8OugthskN1U3Z4N3BfYs8h5r%2F6flOsa3iXc79jZgsDXk4SCOxh13kGsa%2FL%2FO34E09s0ydW59oqn6F2fzlvEMOHJ1Uf%2F9Gaz%2BDpL1arPWKAPN5Do3kmVrw%2F70dz7hxb3%2BWvvVcKrm8LbfMAs18OeKA9i1lDxHR7RGai8A9sRnKxYvvfsYTJ%2BkqWd4d%2B0Hj6KCBuMq%2FWuMhbma8uf4t3jgrucK86KiDeMFfKFDHYKOCK%2FJzSVaPTFyvnQplS%2FRkFKHLKX%2FUXpvGfOBzhpV0wQ4APsF9UisVrBIJqLQrepDkF%2FYAU7FBER6vAMtf7TmNRcy0u7fCFHZgV4b4ulJe2XEA2YR4PEtEzpj3kw6KLsvAY6pgHGcVZH4HPgxrjzfVPRFgWYieQ%2Bg9kThn1MeQWn9I2GANaz4C0VmifUo6Fou9mMqrZ%2Bqt%2BE%2FuDM0eXOlwAJ3E80NZKggHG6KPJIe7PWU6i9Xwu03OdI9dvOnE6SrJWlXRJd9%2FXh3Zjbb%2BI75oEsxFIEvqtpjwWD8PS2jWl2fPZimnC8dnwggSP5JKF3z6pvUign4q9C3%2FNSbKSQOs%2BtYvcBdXhgReHr&X-Amz-Signature=d903ac79aa59fee1c9770fb093626ef99a1fea6cf1246230d778e70a27257571&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4FEKXG7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB40mGc0lAO%2BvRSvN9RAzSS7TPMxm8ekSpONMrT9KPXcAiATtl05BAtyWCvNLOVJXRevBxMUgrZ1NEpD8uPgeFjXBSqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWGbiSfyID8oMkW5TKtwDv3E3RhU%2FeRuu%2B5ZqIs6BThyJhoSxQwi7VsFcDCoxXFG1%2BPRKLEb8qrbchQWrlGioXTjpMGnLVjEVSOtcsVZ4wGVWQyv7VccUkMsDKztZcFOLxAX%2BkRXsk625l2UtiBKuY00trm1FvlILgm7%2BI0Sadx%2FQeatvqtrHAYeXmQeEYqD1XOz5dvAzt1XCxbwyRvfTR6CIg9TYWxrGHT72ojAByHUDXPzQcCjcPv122BjShQR%2BCe2g79qs%2B0GWWGwj%2BY1sXfHEIfLn1XBu%2FHxE6wT1zdFziA%2FVvBBkLuK6%2Fy%2B0DCzpM6J%2BtwsgOT7ulz8DDgUlFmJdCKi66NhHMpyoVdvVO%2ByKhpmxL538GqXfaNCrXuB9vdLIQC1RpKBVpzVMRxEtUTs5VHw6x2UdsBzGqoC1crLOzUgXU1q19PU60BHFlyAiuLmz1RHADZOaYICPBJilKCDoC%2F7xaUSuwpUzY9PSV9kb8RvRLIzSdRu0F8Mz4dNmSy4Jzxb%2BCcUMhBkUc%2FbrsuF%2FuOavv1nO%2FEnyuWe6Qxvex23x%2FkBnS45Gc9AlvXMGY5Hc1Ea03oySDi6tEZhhmBNGKiOpPZJWJ9tFO1ENaDbMZS6ZQ6nldjlFhn4LV1xA%2BKZDtYS7WpHBgzkwqqPsvAY6pgH6hTvf%2B2ip%2Bsog9qigZH%2BgmCJtPr2rLrBllQ7vlSMHbGeepxxelP2vBDs3oAyJ0FkxMjFg5jJFU%2FEt%2B6mQw29nju3rqBTR2%2Bq7ElSfZHI5UB3Cq2coEqsLJKSMt2hEJescXnRrJCXRNTMX1QN6MvvDErycDcAgKSQ13KtIxWmyGN2MeUWiuXGZAM6kQpYjIDzKc94z9USL0Jave8IZrdEdFuGVlKO2&X-Amz-Signature=38531fba40759da78224310c4159e407225be0571581d470eb8cce81501b9d3f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FB6MH6K%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUZJI%2Bb0aSJtKJondsYVQJSiJ78fjVNTZT11yUW1Sz8wIhAO61rsS0AXbdWHPUYUxvctmnrFNlIEAWq6O7bHIaPwVkKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb9w0LRPZIwzgP21gq3ANOtjsP6NGf%2FvCUWFBRuBcxmB6Z%2FqfAhijok0HHDDttTLm5d%2FsDuh7xQqPmBL1KA7VEhrqKHeXsMtTuUoIdCKilN93y%2BFDe90128NfHPBj6GXHEqOoTHd1DKH9CWgw2BiY22uwNUSqyihHvPM2x8NdRO5IpHb%2BVgxYAkgJBLNpvPTdNEqp2W8LqFkUFm9CmTrdERIgJ3URSnMcdA3MSSBfNkgcT4r%2B9y5%2BE8wSY2byLHGULv%2B%2Bse2oYyhwye%2FzFriuijrpRG3B7S9sPd9b8xSQcw8CpxpgbYKCogqdm9r8tWw0BPek1X%2FrL8E5yuJA599xKRpwwU1W0iGMWCTx6YjIRglkvv6k2rjVGMQb5r9Xu0d%2Bvs9sEPyPwyx%2B9PRwROlhcjdd8ePJ376Ahyea6SrD4LB5KetnYDNG8JNqQOX6TcCJTABvTU8TllNqba92QePv%2BgOhgZ8NEeHDqCbEbOv09enDf5IE%2FfulTnIv%2BcGZwjbMnowTxi9WX1QZDlzlnXr7LF7mmNn59%2BxOg7F1kdpaYfDQHhtlQzjlVIO%2FUabxxIxfhjzhHYsXOJit9NpmMt6gf8w8mdjAcIztj9ualDJlAzFhyF7eJp%2FTTyYeNxUNooQquN6JTFgZEHAfQJjD7ouy8BjqkAZvQWxJWNeh5MiZceK2q75JpipaGppBbr%2BkgVBnhyTkv7gOjPrN1nHiXG4E%2FPrsvzFFQrZ6dtoXZ4mxbrR7aFGfEYZsv7Isf%2FhWXUH8l6mIvufx7X0YYGrMV%2F3Va%2BOhQbsL7%2FqEig%2FGNZGb79TUzgpeghur1Mo2465mYgjKNHaVvZMTO9EqvMAnsgN%2FwB772yhxm9qstA5mvT0yfkImG2QgWoYQG&X-Amz-Signature=43fa59e538dab1cd2425fa1d96baa88acad8d671529ea840c80b8191feeb3e61&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSRBKRZH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI20Y%2FlnApVJrP7fOzbsPFD64MfACY8N2PoyfY6a%2FDsAiEAoIHbmBQJfw0T7TbAy9jAwwn7KP9leAyME%2Foj0njjYxYqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcXDUDaexvYMe8c0yrcA%2Fj33q4oWUooO%2FAG0nLbqT%2B1BgvF3%2F6iw5DbOM7N93%2B1%2FYwgIjoYIiEGv7EXzLlwkzF5%2FCfe6cqbuCIrX79Frbti0Qr943doNyfZloDq658K9xTBPpdl8JsLNZOORMny4AWQIj1ENV1C6Czn6k%2FIhVEgKrfqv60%2B9b6tN7DKEOwyF8uBiE4ggJ5FepadAk0LiF8U6NJ2y1n33G5boHy22QK80ZSbNuxK1o4TdG05qG%2F1f1jy8o%2Fx1UqBjlvyzTMZG3pqWe8LY17sAEtXo0vk8jAA4sz7so%2Fy4Y8iW1FAZnVhAu3z9s%2B%2FKPAoWKdLfQgMJyCWwHQaUC3AUtTdtxtwMV4vkV1y8uDixPAsL14QN4cedZJAPVE94de8rDIo0aZBuoOEjTrtyzkqz2Hk2baY35%2FCLuOjIWxMR2kYBp36sqld8OXYvEbfc9Nxyx84BOE9z%2F7gcd8CjMUKJRUGgrVExL2%2BV1cIvjz9IUo%2BGlAtir4er6GWp77TAQhDzlofiCGhaqqOTrn33RfrKo6NLn%2FlwUWROLpJv0ui4OjLTdc038MRNmhhHO2Eb7Jq7qQWXVbwv%2FEGCuJwUIyrIVmOjLVjS0tYjH9EDMX6I8mfcWAbYR96VhQtOe6aogmmm%2Bo8MPui7LwGOqUBwYE%2BrvsVqBc1deAP5fxSNbpGn95D3REXvzMKl9OSzGjcyFkWWUXsH1LUOZTiCtpYXIwt8zXMC8BzLWqFwV1GsEQc280tRtQhKjt%2BCuOKtLPvbKFjekNq5No1gnqXs10y6sJ3ildNJrpLf3xO7EV8%2B3wAITB4Rk97Km6TEXi22nQOSQ8MNJdmUtUGGR7vT2qCqsyBT4GW%2BBNcKEYUovjnrpflgpAq&X-Amz-Signature=7fcb325b8289913ba926b1d1bc35af16ec330109314645356fc796a389c6eb4e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSRBKRZH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI20Y%2FlnApVJrP7fOzbsPFD64MfACY8N2PoyfY6a%2FDsAiEAoIHbmBQJfw0T7TbAy9jAwwn7KP9leAyME%2Foj0njjYxYqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcXDUDaexvYMe8c0yrcA%2Fj33q4oWUooO%2FAG0nLbqT%2B1BgvF3%2F6iw5DbOM7N93%2B1%2FYwgIjoYIiEGv7EXzLlwkzF5%2FCfe6cqbuCIrX79Frbti0Qr943doNyfZloDq658K9xTBPpdl8JsLNZOORMny4AWQIj1ENV1C6Czn6k%2FIhVEgKrfqv60%2B9b6tN7DKEOwyF8uBiE4ggJ5FepadAk0LiF8U6NJ2y1n33G5boHy22QK80ZSbNuxK1o4TdG05qG%2F1f1jy8o%2Fx1UqBjlvyzTMZG3pqWe8LY17sAEtXo0vk8jAA4sz7so%2Fy4Y8iW1FAZnVhAu3z9s%2B%2FKPAoWKdLfQgMJyCWwHQaUC3AUtTdtxtwMV4vkV1y8uDixPAsL14QN4cedZJAPVE94de8rDIo0aZBuoOEjTrtyzkqz2Hk2baY35%2FCLuOjIWxMR2kYBp36sqld8OXYvEbfc9Nxyx84BOE9z%2F7gcd8CjMUKJRUGgrVExL2%2BV1cIvjz9IUo%2BGlAtir4er6GWp77TAQhDzlofiCGhaqqOTrn33RfrKo6NLn%2FlwUWROLpJv0ui4OjLTdc038MRNmhhHO2Eb7Jq7qQWXVbwv%2FEGCuJwUIyrIVmOjLVjS0tYjH9EDMX6I8mfcWAbYR96VhQtOe6aogmmm%2Bo8MPui7LwGOqUBwYE%2BrvsVqBc1deAP5fxSNbpGn95D3REXvzMKl9OSzGjcyFkWWUXsH1LUOZTiCtpYXIwt8zXMC8BzLWqFwV1GsEQc280tRtQhKjt%2BCuOKtLPvbKFjekNq5No1gnqXs10y6sJ3ildNJrpLf3xO7EV8%2B3wAITB4Rk97Km6TEXi22nQOSQ8MNJdmUtUGGR7vT2qCqsyBT4GW%2BBNcKEYUovjnrpflgpAq&X-Amz-Signature=57a5077bdea4db35a3899111ebb70d987722881a81b63281db004743daef8002&X-Amz-SignedHeaders=host&x-id=GetObject)

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
