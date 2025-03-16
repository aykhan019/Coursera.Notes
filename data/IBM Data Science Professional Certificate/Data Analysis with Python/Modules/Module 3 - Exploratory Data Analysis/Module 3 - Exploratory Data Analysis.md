

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SB25SGJ7%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2L%2F54WPD5kkptL3Lhv5bDmTWMK%2BhUJfEhYz2RTBTuEQIhAKJItH30w7eHw9%2Fv%2BbOzZxfNKKY7jOYDNlG1ZOIKbPjMKv8DCCAQABoMNjM3NDIzMTgzODA1IgwuS2Z9LVl6iq7wvUIq3AOiV%2F6qqX%2BzoX%2Bv2NL84A9oCVDf1Jdu5O9HPOmn5BoTL2wm6rz%2Fmf1hJDcRdVSeqlEKoqGWeZ%2Bb183%2BdZhD5VSamE8tb8nY6tnRooqyWF43hbILr%2B32huZfw7npKkiC%2B7wu5k3oynI8JmxkWiOC%2BeB3Es9chFrH1WbyrnU94GLJY3ZrNUqQe7KVUZhtht7%2BqBKuO5ZRWPrW%2Bvk470QFwqAX%2BGtaSfFcIF3aTJWRsLlqZEzAKrsGMlg9n9cQEgKiLV4zm1u8iihAzEYVafzobY%2B6lBbBfY3HM931Aww1sk8Zs%2F%2FJ6lwWSD3xdKYwhx5JXhHlHi95UqEnRT7eZykNZF9O0AdTLTJvYYtq9gDPYGjGTgYg75fpxDnFbHWx6%2FaGcshovA0deo4CJMDIBHg1XkqYrLmiU55V9faL6NkTLM0ipOUUuw9KLU77IrgXZGwEz3N4Nf7F7iB%2BAEs96wZbjGoNejipDPT0pSACqgFTw13HtmrZBJOrladzRoLNWXnpPytX4Z4upx2TSbg68AAo4fgv5OwHUb1Wy9Z41OrhIyIbDbUT28V2WQQilzqpnSyg%2BU746SsulT893aQq4E1jcPqSVRjSLIijLBEb7kBCwHdB%2FqNOWqA9Y6Pt%2FEkcKjC1%2F9e%2BBjqkAbz8q6mqjT%2BEx09D3DvRbUsUhmyKFIHe84ERs%2BvqDmvwFFtz633RiqcOII2KNIJmjYguiqGz2FDpGViRzRm2l%2FPF3gm8d%2BpvEAVRCS6ksnk98cZOCQcDD3v%2BuNkB1fUpSfYTKpSa%2Fw8e3B5CqKqVgG0aSN0d9x6Gbs2EBDLO98CBmB5It0eQFZEA9vuowMq3ZWxztugSNGBWYUE75KfMSqeSnWYl&X-Amz-Signature=7e9d058c2c3eb79d192f834ab87173f49064c22a2eb673a01cedd203289cdfb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SB25SGJ7%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2L%2F54WPD5kkptL3Lhv5bDmTWMK%2BhUJfEhYz2RTBTuEQIhAKJItH30w7eHw9%2Fv%2BbOzZxfNKKY7jOYDNlG1ZOIKbPjMKv8DCCAQABoMNjM3NDIzMTgzODA1IgwuS2Z9LVl6iq7wvUIq3AOiV%2F6qqX%2BzoX%2Bv2NL84A9oCVDf1Jdu5O9HPOmn5BoTL2wm6rz%2Fmf1hJDcRdVSeqlEKoqGWeZ%2Bb183%2BdZhD5VSamE8tb8nY6tnRooqyWF43hbILr%2B32huZfw7npKkiC%2B7wu5k3oynI8JmxkWiOC%2BeB3Es9chFrH1WbyrnU94GLJY3ZrNUqQe7KVUZhtht7%2BqBKuO5ZRWPrW%2Bvk470QFwqAX%2BGtaSfFcIF3aTJWRsLlqZEzAKrsGMlg9n9cQEgKiLV4zm1u8iihAzEYVafzobY%2B6lBbBfY3HM931Aww1sk8Zs%2F%2FJ6lwWSD3xdKYwhx5JXhHlHi95UqEnRT7eZykNZF9O0AdTLTJvYYtq9gDPYGjGTgYg75fpxDnFbHWx6%2FaGcshovA0deo4CJMDIBHg1XkqYrLmiU55V9faL6NkTLM0ipOUUuw9KLU77IrgXZGwEz3N4Nf7F7iB%2BAEs96wZbjGoNejipDPT0pSACqgFTw13HtmrZBJOrladzRoLNWXnpPytX4Z4upx2TSbg68AAo4fgv5OwHUb1Wy9Z41OrhIyIbDbUT28V2WQQilzqpnSyg%2BU746SsulT893aQq4E1jcPqSVRjSLIijLBEb7kBCwHdB%2FqNOWqA9Y6Pt%2FEkcKjC1%2F9e%2BBjqkAbz8q6mqjT%2BEx09D3DvRbUsUhmyKFIHe84ERs%2BvqDmvwFFtz633RiqcOII2KNIJmjYguiqGz2FDpGViRzRm2l%2FPF3gm8d%2BpvEAVRCS6ksnk98cZOCQcDD3v%2BuNkB1fUpSfYTKpSa%2Fw8e3B5CqKqVgG0aSN0d9x6Gbs2EBDLO98CBmB5It0eQFZEA9vuowMq3ZWxztugSNGBWYUE75KfMSqeSnWYl&X-Amz-Signature=80e26ddac07b8d481a2a3c9b97e3a7776c5198dba1529454f316dd8cd0772758&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SB25SGJ7%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2L%2F54WPD5kkptL3Lhv5bDmTWMK%2BhUJfEhYz2RTBTuEQIhAKJItH30w7eHw9%2Fv%2BbOzZxfNKKY7jOYDNlG1ZOIKbPjMKv8DCCAQABoMNjM3NDIzMTgzODA1IgwuS2Z9LVl6iq7wvUIq3AOiV%2F6qqX%2BzoX%2Bv2NL84A9oCVDf1Jdu5O9HPOmn5BoTL2wm6rz%2Fmf1hJDcRdVSeqlEKoqGWeZ%2Bb183%2BdZhD5VSamE8tb8nY6tnRooqyWF43hbILr%2B32huZfw7npKkiC%2B7wu5k3oynI8JmxkWiOC%2BeB3Es9chFrH1WbyrnU94GLJY3ZrNUqQe7KVUZhtht7%2BqBKuO5ZRWPrW%2Bvk470QFwqAX%2BGtaSfFcIF3aTJWRsLlqZEzAKrsGMlg9n9cQEgKiLV4zm1u8iihAzEYVafzobY%2B6lBbBfY3HM931Aww1sk8Zs%2F%2FJ6lwWSD3xdKYwhx5JXhHlHi95UqEnRT7eZykNZF9O0AdTLTJvYYtq9gDPYGjGTgYg75fpxDnFbHWx6%2FaGcshovA0deo4CJMDIBHg1XkqYrLmiU55V9faL6NkTLM0ipOUUuw9KLU77IrgXZGwEz3N4Nf7F7iB%2BAEs96wZbjGoNejipDPT0pSACqgFTw13HtmrZBJOrladzRoLNWXnpPytX4Z4upx2TSbg68AAo4fgv5OwHUb1Wy9Z41OrhIyIbDbUT28V2WQQilzqpnSyg%2BU746SsulT893aQq4E1jcPqSVRjSLIijLBEb7kBCwHdB%2FqNOWqA9Y6Pt%2FEkcKjC1%2F9e%2BBjqkAbz8q6mqjT%2BEx09D3DvRbUsUhmyKFIHe84ERs%2BvqDmvwFFtz633RiqcOII2KNIJmjYguiqGz2FDpGViRzRm2l%2FPF3gm8d%2BpvEAVRCS6ksnk98cZOCQcDD3v%2BuNkB1fUpSfYTKpSa%2Fw8e3B5CqKqVgG0aSN0d9x6Gbs2EBDLO98CBmB5It0eQFZEA9vuowMq3ZWxztugSNGBWYUE75KfMSqeSnWYl&X-Amz-Signature=454cea96cbf42c5b3f47d9cc79dbca71a87c6022a8a7b908c5eeddbc54af1dd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT2DAPJQ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQowgHj6C7P29ThG2ffdCHH8gV9ssrDdGUXJ29Y%2FfPTAiA9zTAeWbWxCra4Hcr4BvjUSUbM1aoBquZw9bwZRdQpgSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMEkmDvFJVvUHzc27hKtwD1vta8Uc%2FF1bYqX%2BnTe1jvgLVMtsLV3diqNcUNsVDN7rrfZFskEXKaNEIK33fPnEKEgLrtKwBnNEMweF%2FNGjboBkiK4g4FJeWjpEOlqOIVyoiBsoNHUfnanwSPU2OBf0oGtp2TdmRugV3cs9aSkHe31kFUNxmzqBHBB1FmfeuOPj9CZHgQ5OMXkoWBNvGFPc7MGdzfFlWFlkrU6zPhxaXKD8rX0WLvlHGgV2LSKrxHQiLbR0Nv2xwg3JeN9SDHqMjJrcVPjQxCqJbSIUBSSYNh0NzG7Ek15x5z2Inkszcm4zUd1bXidPzkSJre%2FYbo8oSvxZRnDDMkJVhmMgvwEQpDCWaVwziJ4Um8Igq7A%2Fyim3bcd2t6f68BQqaaL3qlBj373VoV%2BzMlmPhWnS%2B8%2B%2FQge0jEkBU1KRsb6qsbA666ey3t6rW0vHuz3w1f5B5bbKqqfX9Fl1u8SLWZeMU2Cc83lmBzRubVgjvIr2lNUDFURSCCJDcLOsmPa4%2BQO5pQXEuABINf%2FwH3dT4hyyaBHB%2BU%2F9tPMFXwrYxJHN1NVsxY7uMXpvQQsmGviVKOI9qeIYr5uFrNDdKJBZoPxbeIwK4z6dkMdvzMoFlKJCQFAVq3oVoINOxVIGOCyFoWYYwtf%2FXvgY6pgH1CW9oPCkRCB4j3aihsBSp7%2BUN3%2FGAsnxiLlTtZdxDCDwQZkABuYylksaFK5Vm%2BkQm3IcJUXTDNV5Vy1%2FfMFED8pq3M3kfl25m7Wku%2Bf2m%2FqfUpSLyADfhJqH665W%2BIQtHUbkyORG0CxCHFOKNXeAxq%2F6z22hkLvXGqALvaTD6nc1%2B1f3QckNvCKSqpIlzRsIjE2rl1G1y%2Bt6fnGFRUDJDRHt862iO&X-Amz-Signature=208ffe287e3ca9500392b3dac27b3a301180a7ec698bc00a1ff37348d8d00003&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT2DAPJQ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQowgHj6C7P29ThG2ffdCHH8gV9ssrDdGUXJ29Y%2FfPTAiA9zTAeWbWxCra4Hcr4BvjUSUbM1aoBquZw9bwZRdQpgSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMEkmDvFJVvUHzc27hKtwD1vta8Uc%2FF1bYqX%2BnTe1jvgLVMtsLV3diqNcUNsVDN7rrfZFskEXKaNEIK33fPnEKEgLrtKwBnNEMweF%2FNGjboBkiK4g4FJeWjpEOlqOIVyoiBsoNHUfnanwSPU2OBf0oGtp2TdmRugV3cs9aSkHe31kFUNxmzqBHBB1FmfeuOPj9CZHgQ5OMXkoWBNvGFPc7MGdzfFlWFlkrU6zPhxaXKD8rX0WLvlHGgV2LSKrxHQiLbR0Nv2xwg3JeN9SDHqMjJrcVPjQxCqJbSIUBSSYNh0NzG7Ek15x5z2Inkszcm4zUd1bXidPzkSJre%2FYbo8oSvxZRnDDMkJVhmMgvwEQpDCWaVwziJ4Um8Igq7A%2Fyim3bcd2t6f68BQqaaL3qlBj373VoV%2BzMlmPhWnS%2B8%2B%2FQge0jEkBU1KRsb6qsbA666ey3t6rW0vHuz3w1f5B5bbKqqfX9Fl1u8SLWZeMU2Cc83lmBzRubVgjvIr2lNUDFURSCCJDcLOsmPa4%2BQO5pQXEuABINf%2FwH3dT4hyyaBHB%2BU%2F9tPMFXwrYxJHN1NVsxY7uMXpvQQsmGviVKOI9qeIYr5uFrNDdKJBZoPxbeIwK4z6dkMdvzMoFlKJCQFAVq3oVoINOxVIGOCyFoWYYwtf%2FXvgY6pgH1CW9oPCkRCB4j3aihsBSp7%2BUN3%2FGAsnxiLlTtZdxDCDwQZkABuYylksaFK5Vm%2BkQm3IcJUXTDNV5Vy1%2FfMFED8pq3M3kfl25m7Wku%2Bf2m%2FqfUpSLyADfhJqH665W%2BIQtHUbkyORG0CxCHFOKNXeAxq%2F6z22hkLvXGqALvaTD6nc1%2B1f3QckNvCKSqpIlzRsIjE2rl1G1y%2Bt6fnGFRUDJDRHt862iO&X-Amz-Signature=9669b0569876e76df128ccbb4d3b7ad4d6bea19f26258bf5c9487119cf359f72&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT2DAPJQ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQowgHj6C7P29ThG2ffdCHH8gV9ssrDdGUXJ29Y%2FfPTAiA9zTAeWbWxCra4Hcr4BvjUSUbM1aoBquZw9bwZRdQpgSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMEkmDvFJVvUHzc27hKtwD1vta8Uc%2FF1bYqX%2BnTe1jvgLVMtsLV3diqNcUNsVDN7rrfZFskEXKaNEIK33fPnEKEgLrtKwBnNEMweF%2FNGjboBkiK4g4FJeWjpEOlqOIVyoiBsoNHUfnanwSPU2OBf0oGtp2TdmRugV3cs9aSkHe31kFUNxmzqBHBB1FmfeuOPj9CZHgQ5OMXkoWBNvGFPc7MGdzfFlWFlkrU6zPhxaXKD8rX0WLvlHGgV2LSKrxHQiLbR0Nv2xwg3JeN9SDHqMjJrcVPjQxCqJbSIUBSSYNh0NzG7Ek15x5z2Inkszcm4zUd1bXidPzkSJre%2FYbo8oSvxZRnDDMkJVhmMgvwEQpDCWaVwziJ4Um8Igq7A%2Fyim3bcd2t6f68BQqaaL3qlBj373VoV%2BzMlmPhWnS%2B8%2B%2FQge0jEkBU1KRsb6qsbA666ey3t6rW0vHuz3w1f5B5bbKqqfX9Fl1u8SLWZeMU2Cc83lmBzRubVgjvIr2lNUDFURSCCJDcLOsmPa4%2BQO5pQXEuABINf%2FwH3dT4hyyaBHB%2BU%2F9tPMFXwrYxJHN1NVsxY7uMXpvQQsmGviVKOI9qeIYr5uFrNDdKJBZoPxbeIwK4z6dkMdvzMoFlKJCQFAVq3oVoINOxVIGOCyFoWYYwtf%2FXvgY6pgH1CW9oPCkRCB4j3aihsBSp7%2BUN3%2FGAsnxiLlTtZdxDCDwQZkABuYylksaFK5Vm%2BkQm3IcJUXTDNV5Vy1%2FfMFED8pq3M3kfl25m7Wku%2Bf2m%2FqfUpSLyADfhJqH665W%2BIQtHUbkyORG0CxCHFOKNXeAxq%2F6z22hkLvXGqALvaTD6nc1%2B1f3QckNvCKSqpIlzRsIjE2rl1G1y%2Bt6fnGFRUDJDRHt862iO&X-Amz-Signature=50af7e00622b5560052b5a529669238bd0dd221d3ed19630d5b4455732d5b593&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT2DAPJQ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQowgHj6C7P29ThG2ffdCHH8gV9ssrDdGUXJ29Y%2FfPTAiA9zTAeWbWxCra4Hcr4BvjUSUbM1aoBquZw9bwZRdQpgSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMEkmDvFJVvUHzc27hKtwD1vta8Uc%2FF1bYqX%2BnTe1jvgLVMtsLV3diqNcUNsVDN7rrfZFskEXKaNEIK33fPnEKEgLrtKwBnNEMweF%2FNGjboBkiK4g4FJeWjpEOlqOIVyoiBsoNHUfnanwSPU2OBf0oGtp2TdmRugV3cs9aSkHe31kFUNxmzqBHBB1FmfeuOPj9CZHgQ5OMXkoWBNvGFPc7MGdzfFlWFlkrU6zPhxaXKD8rX0WLvlHGgV2LSKrxHQiLbR0Nv2xwg3JeN9SDHqMjJrcVPjQxCqJbSIUBSSYNh0NzG7Ek15x5z2Inkszcm4zUd1bXidPzkSJre%2FYbo8oSvxZRnDDMkJVhmMgvwEQpDCWaVwziJ4Um8Igq7A%2Fyim3bcd2t6f68BQqaaL3qlBj373VoV%2BzMlmPhWnS%2B8%2B%2FQge0jEkBU1KRsb6qsbA666ey3t6rW0vHuz3w1f5B5bbKqqfX9Fl1u8SLWZeMU2Cc83lmBzRubVgjvIr2lNUDFURSCCJDcLOsmPa4%2BQO5pQXEuABINf%2FwH3dT4hyyaBHB%2BU%2F9tPMFXwrYxJHN1NVsxY7uMXpvQQsmGviVKOI9qeIYr5uFrNDdKJBZoPxbeIwK4z6dkMdvzMoFlKJCQFAVq3oVoINOxVIGOCyFoWYYwtf%2FXvgY6pgH1CW9oPCkRCB4j3aihsBSp7%2BUN3%2FGAsnxiLlTtZdxDCDwQZkABuYylksaFK5Vm%2BkQm3IcJUXTDNV5Vy1%2FfMFED8pq3M3kfl25m7Wku%2Bf2m%2FqfUpSLyADfhJqH665W%2BIQtHUbkyORG0CxCHFOKNXeAxq%2F6z22hkLvXGqALvaTD6nc1%2B1f3QckNvCKSqpIlzRsIjE2rl1G1y%2Bt6fnGFRUDJDRHt862iO&X-Amz-Signature=6fe5e7b00272831a1ec6541727da08be09d0ce8e253010b1d6b7aa3720112d67&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT2DAPJQ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQowgHj6C7P29ThG2ffdCHH8gV9ssrDdGUXJ29Y%2FfPTAiA9zTAeWbWxCra4Hcr4BvjUSUbM1aoBquZw9bwZRdQpgSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMEkmDvFJVvUHzc27hKtwD1vta8Uc%2FF1bYqX%2BnTe1jvgLVMtsLV3diqNcUNsVDN7rrfZFskEXKaNEIK33fPnEKEgLrtKwBnNEMweF%2FNGjboBkiK4g4FJeWjpEOlqOIVyoiBsoNHUfnanwSPU2OBf0oGtp2TdmRugV3cs9aSkHe31kFUNxmzqBHBB1FmfeuOPj9CZHgQ5OMXkoWBNvGFPc7MGdzfFlWFlkrU6zPhxaXKD8rX0WLvlHGgV2LSKrxHQiLbR0Nv2xwg3JeN9SDHqMjJrcVPjQxCqJbSIUBSSYNh0NzG7Ek15x5z2Inkszcm4zUd1bXidPzkSJre%2FYbo8oSvxZRnDDMkJVhmMgvwEQpDCWaVwziJ4Um8Igq7A%2Fyim3bcd2t6f68BQqaaL3qlBj373VoV%2BzMlmPhWnS%2B8%2B%2FQge0jEkBU1KRsb6qsbA666ey3t6rW0vHuz3w1f5B5bbKqqfX9Fl1u8SLWZeMU2Cc83lmBzRubVgjvIr2lNUDFURSCCJDcLOsmPa4%2BQO5pQXEuABINf%2FwH3dT4hyyaBHB%2BU%2F9tPMFXwrYxJHN1NVsxY7uMXpvQQsmGviVKOI9qeIYr5uFrNDdKJBZoPxbeIwK4z6dkMdvzMoFlKJCQFAVq3oVoINOxVIGOCyFoWYYwtf%2FXvgY6pgH1CW9oPCkRCB4j3aihsBSp7%2BUN3%2FGAsnxiLlTtZdxDCDwQZkABuYylksaFK5Vm%2BkQm3IcJUXTDNV5Vy1%2FfMFED8pq3M3kfl25m7Wku%2Bf2m%2FqfUpSLyADfhJqH665W%2BIQtHUbkyORG0CxCHFOKNXeAxq%2F6z22hkLvXGqALvaTD6nc1%2B1f3QckNvCKSqpIlzRsIjE2rl1G1y%2Bt6fnGFRUDJDRHt862iO&X-Amz-Signature=69af36ca190b4416172475025879edcdacbe8714ff5a52e70c3881ccf75e0e12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT2DAPJQ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQowgHj6C7P29ThG2ffdCHH8gV9ssrDdGUXJ29Y%2FfPTAiA9zTAeWbWxCra4Hcr4BvjUSUbM1aoBquZw9bwZRdQpgSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMEkmDvFJVvUHzc27hKtwD1vta8Uc%2FF1bYqX%2BnTe1jvgLVMtsLV3diqNcUNsVDN7rrfZFskEXKaNEIK33fPnEKEgLrtKwBnNEMweF%2FNGjboBkiK4g4FJeWjpEOlqOIVyoiBsoNHUfnanwSPU2OBf0oGtp2TdmRugV3cs9aSkHe31kFUNxmzqBHBB1FmfeuOPj9CZHgQ5OMXkoWBNvGFPc7MGdzfFlWFlkrU6zPhxaXKD8rX0WLvlHGgV2LSKrxHQiLbR0Nv2xwg3JeN9SDHqMjJrcVPjQxCqJbSIUBSSYNh0NzG7Ek15x5z2Inkszcm4zUd1bXidPzkSJre%2FYbo8oSvxZRnDDMkJVhmMgvwEQpDCWaVwziJ4Um8Igq7A%2Fyim3bcd2t6f68BQqaaL3qlBj373VoV%2BzMlmPhWnS%2B8%2B%2FQge0jEkBU1KRsb6qsbA666ey3t6rW0vHuz3w1f5B5bbKqqfX9Fl1u8SLWZeMU2Cc83lmBzRubVgjvIr2lNUDFURSCCJDcLOsmPa4%2BQO5pQXEuABINf%2FwH3dT4hyyaBHB%2BU%2F9tPMFXwrYxJHN1NVsxY7uMXpvQQsmGviVKOI9qeIYr5uFrNDdKJBZoPxbeIwK4z6dkMdvzMoFlKJCQFAVq3oVoINOxVIGOCyFoWYYwtf%2FXvgY6pgH1CW9oPCkRCB4j3aihsBSp7%2BUN3%2FGAsnxiLlTtZdxDCDwQZkABuYylksaFK5Vm%2BkQm3IcJUXTDNV5Vy1%2FfMFED8pq3M3kfl25m7Wku%2Bf2m%2FqfUpSLyADfhJqH665W%2BIQtHUbkyORG0CxCHFOKNXeAxq%2F6z22hkLvXGqALvaTD6nc1%2B1f3QckNvCKSqpIlzRsIjE2rl1G1y%2Bt6fnGFRUDJDRHt862iO&X-Amz-Signature=93e3cd41c246314112790d2a50fae09de159bc471d4e0256c639137a03feac33&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKY5CTO2%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBD1ana%2FPVn%2BrJixbgpKaleNiQBT97bkQ1%2BBgJQVkZ1vAiAHoRE4EZmvbcLhYjmdGGMtpWRBxaaL415tiOu7X9iizCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM3TZMxDl0EuinsoNTKtwDbImzjWzVdnodGUSWLVkJR7dZHbzhgcgBbtBzjYYjb05Am0poLIp%2FJ9%2Fw65C3727TfOTJFkBaxpRhOjWtqgDDplHcg4KiWChyC97m3lHGDGQhUsaCi7cnB0OyrGPq8OF3P6uK1SBAbf39Kyq0nV9KsdtMKu6la7f%2FWNSQEoy%2BB6PUG4LmU5BCwuqsO0fIIyfNde3yZPqEqbuPxaI9x6SpHowEJZY1RkDZ06uTO27ZPNhKcQ%2BnkjKpKtGNBjvBlydfz3fzR3bEUZb4u50jJ6PYroVQgWr9zNtFmd2dcRjpjKvofyl1xZIFj%2Fh0ARt6Rb%2BptA4635yJ1uDFNZL%2BeVuSGdmDEMeZ4KryxNl0QyI7o1D5aVSckW%2FzGXiyMmUVpkMDwNjbAduS7hmvZHfcRvTJHTQLxgumDAcZIVv22lDS%2Fhhmd9Qe31T8sY2S4lziMBtsQhQ0LY5wOjsCMWE%2Fz%2BF0TQt33Wnvqwbwq124qV0KQG%2BcGBPd8d9SdxvtzExSPhcvKKtrB3cQk%2FyJCyhJwdUoWvcP7ZMNXoV3ZP%2FvMOOBkJVN9tw4Da2owQHOEW8Gt455h5Lage1bhVytPokwUmMC5vWKlSSebL%2Ft5AUZAlvvfo9Wvghk%2FIqpHBJGaAYw2P%2FXvgY6pgF%2B9iwwxfOZPm2DUhwosKgFgkYWYQjxxX0zlJa%2F8PFEZHPpQavXgQNEqv6gwDFD0opz1dBP8%2BQHRgJiDF1SIkMs5e%2B1c2MsmnL2KpXhXgY1Q6UF%2FyFawvVwpio4JSXOpZNYf11kRFwVMzjmILbHotYZsXAxzRXmoILh8y%2FaI0dfwmlYvkdJRhcTVdY213ak8wStAa9iUslrE5csAjM6aS%2FAGR6dnFax&X-Amz-Signature=453ca74d2fa47f38f36cd1b5844c9d83fd1bd8a4e92e37f3761247afd183c8fc&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BHJ4MZ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGxMJzXMzkdcsZhUkTAjkr0%2FkVg8IHgfEM3cmlcHzJpUAiAPEQux%2B0YvCjpAZnuziye%2BeSjvZmWc1Op3Ri9JmkPcIir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMcfVSz4DXAA7p1jHaKtwDNbUKZKQqIQ3YDRDqS%2FoE9fmwULJJp0N1vtrePHPCgwLbzAxMtJpPrbowky8loypjMj037HzIt4LTJoJJzq52JymRiYcpOHgRyTcL6e2mZHQ%2B%2B1FutxpJn%2B574wpPwEFFYdmr2WgEvj4dPUKNROq2cTQjIR2HxljLDC%2FnGtSIT0vcVBsatNb1U2Zp6%2F3VKOEJnJEsvnjnqpwEcDWrEEIhxsfE3aQGESa1x2GSO8r5ywNkWFJngZguK362pepFTrp1W1Ub3UPoZa%2FAQUnx7Y2RhGat%2Fe7SxPztyugFjIQpy2xhtgbP2x9T5O%2B8VrYZpzHd0QTFlaLMqzgJ6dA4JwVaAxUnAUhw5xu2aBbZG%2FtmERidkgl0p4FQR2CFbyBwQh%2F50wzznIpL%2F1yjTP1IIRrBvBc0nunMkcFwBU7AF5dr0tCEjCRwKHWRtBYhK7BOemezLedUv3IIpKL1oCQkMCNpW%2F%2FoWu1ofV1Ph%2BRWE577%2BJ9HXLk0tgpEcgrScbm2jo%2B1tjJwBOA0I1QvCBWxrE5aTpDMxvEi0SjlqtIbnlwJc1vlvibfTyawH3FVRCwNdTrAGifs5c2Hd9%2F746tze90jK1iQzjxYllczW4m1ICYwyYI5gfXhHXs92M2RcYEwzP%2FXvgY6pgEfzuW3O6WrkcTQhRZ6YHnuNmAq9p6gUDUZqz5qisedgxEA4l5rIU%2Fm0w8naBTLpfH9O4IKjKtHcpTfb2mQc7iEjcno0%2FeFhDqq1WXznpzlUTAXPHWAEQt9VuOhxgy%2FwAUFFUxYlFj7X5uVnhXjAWhrQ4HUzG%2FVDyYHEizsUtI4FD61d3qfrXzvsFHncdMF3rnGumQw70hjpGlLH4ua4Gcy3oz6rRAv&X-Amz-Signature=d106d086f6ad2583d401a01183a2d652f3fe723f86a38423d947eeb1e87ab80d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT2DAPJQ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQowgHj6C7P29ThG2ffdCHH8gV9ssrDdGUXJ29Y%2FfPTAiA9zTAeWbWxCra4Hcr4BvjUSUbM1aoBquZw9bwZRdQpgSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMEkmDvFJVvUHzc27hKtwD1vta8Uc%2FF1bYqX%2BnTe1jvgLVMtsLV3diqNcUNsVDN7rrfZFskEXKaNEIK33fPnEKEgLrtKwBnNEMweF%2FNGjboBkiK4g4FJeWjpEOlqOIVyoiBsoNHUfnanwSPU2OBf0oGtp2TdmRugV3cs9aSkHe31kFUNxmzqBHBB1FmfeuOPj9CZHgQ5OMXkoWBNvGFPc7MGdzfFlWFlkrU6zPhxaXKD8rX0WLvlHGgV2LSKrxHQiLbR0Nv2xwg3JeN9SDHqMjJrcVPjQxCqJbSIUBSSYNh0NzG7Ek15x5z2Inkszcm4zUd1bXidPzkSJre%2FYbo8oSvxZRnDDMkJVhmMgvwEQpDCWaVwziJ4Um8Igq7A%2Fyim3bcd2t6f68BQqaaL3qlBj373VoV%2BzMlmPhWnS%2B8%2B%2FQge0jEkBU1KRsb6qsbA666ey3t6rW0vHuz3w1f5B5bbKqqfX9Fl1u8SLWZeMU2Cc83lmBzRubVgjvIr2lNUDFURSCCJDcLOsmPa4%2BQO5pQXEuABINf%2FwH3dT4hyyaBHB%2BU%2F9tPMFXwrYxJHN1NVsxY7uMXpvQQsmGviVKOI9qeIYr5uFrNDdKJBZoPxbeIwK4z6dkMdvzMoFlKJCQFAVq3oVoINOxVIGOCyFoWYYwtf%2FXvgY6pgH1CW9oPCkRCB4j3aihsBSp7%2BUN3%2FGAsnxiLlTtZdxDCDwQZkABuYylksaFK5Vm%2BkQm3IcJUXTDNV5Vy1%2FfMFED8pq3M3kfl25m7Wku%2Bf2m%2FqfUpSLyADfhJqH665W%2BIQtHUbkyORG0CxCHFOKNXeAxq%2F6z22hkLvXGqALvaTD6nc1%2B1f3QckNvCKSqpIlzRsIjE2rl1G1y%2Bt6fnGFRUDJDRHt862iO&X-Amz-Signature=1ae44c411a65927b0c4da51f470114ab9a1b68af449b4f0bb12082a150c7720f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT2DAPJQ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQowgHj6C7P29ThG2ffdCHH8gV9ssrDdGUXJ29Y%2FfPTAiA9zTAeWbWxCra4Hcr4BvjUSUbM1aoBquZw9bwZRdQpgSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMEkmDvFJVvUHzc27hKtwD1vta8Uc%2FF1bYqX%2BnTe1jvgLVMtsLV3diqNcUNsVDN7rrfZFskEXKaNEIK33fPnEKEgLrtKwBnNEMweF%2FNGjboBkiK4g4FJeWjpEOlqOIVyoiBsoNHUfnanwSPU2OBf0oGtp2TdmRugV3cs9aSkHe31kFUNxmzqBHBB1FmfeuOPj9CZHgQ5OMXkoWBNvGFPc7MGdzfFlWFlkrU6zPhxaXKD8rX0WLvlHGgV2LSKrxHQiLbR0Nv2xwg3JeN9SDHqMjJrcVPjQxCqJbSIUBSSYNh0NzG7Ek15x5z2Inkszcm4zUd1bXidPzkSJre%2FYbo8oSvxZRnDDMkJVhmMgvwEQpDCWaVwziJ4Um8Igq7A%2Fyim3bcd2t6f68BQqaaL3qlBj373VoV%2BzMlmPhWnS%2B8%2B%2FQge0jEkBU1KRsb6qsbA666ey3t6rW0vHuz3w1f5B5bbKqqfX9Fl1u8SLWZeMU2Cc83lmBzRubVgjvIr2lNUDFURSCCJDcLOsmPa4%2BQO5pQXEuABINf%2FwH3dT4hyyaBHB%2BU%2F9tPMFXwrYxJHN1NVsxY7uMXpvQQsmGviVKOI9qeIYr5uFrNDdKJBZoPxbeIwK4z6dkMdvzMoFlKJCQFAVq3oVoINOxVIGOCyFoWYYwtf%2FXvgY6pgH1CW9oPCkRCB4j3aihsBSp7%2BUN3%2FGAsnxiLlTtZdxDCDwQZkABuYylksaFK5Vm%2BkQm3IcJUXTDNV5Vy1%2FfMFED8pq3M3kfl25m7Wku%2Bf2m%2FqfUpSLyADfhJqH665W%2BIQtHUbkyORG0CxCHFOKNXeAxq%2F6z22hkLvXGqALvaTD6nc1%2B1f3QckNvCKSqpIlzRsIjE2rl1G1y%2Bt6fnGFRUDJDRHt862iO&X-Amz-Signature=eac7d549648445e680ee4a2f323fa2b8dd7f3dbb425bcf57fe698bbde988db7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT2DAPJQ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQowgHj6C7P29ThG2ffdCHH8gV9ssrDdGUXJ29Y%2FfPTAiA9zTAeWbWxCra4Hcr4BvjUSUbM1aoBquZw9bwZRdQpgSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMEkmDvFJVvUHzc27hKtwD1vta8Uc%2FF1bYqX%2BnTe1jvgLVMtsLV3diqNcUNsVDN7rrfZFskEXKaNEIK33fPnEKEgLrtKwBnNEMweF%2FNGjboBkiK4g4FJeWjpEOlqOIVyoiBsoNHUfnanwSPU2OBf0oGtp2TdmRugV3cs9aSkHe31kFUNxmzqBHBB1FmfeuOPj9CZHgQ5OMXkoWBNvGFPc7MGdzfFlWFlkrU6zPhxaXKD8rX0WLvlHGgV2LSKrxHQiLbR0Nv2xwg3JeN9SDHqMjJrcVPjQxCqJbSIUBSSYNh0NzG7Ek15x5z2Inkszcm4zUd1bXidPzkSJre%2FYbo8oSvxZRnDDMkJVhmMgvwEQpDCWaVwziJ4Um8Igq7A%2Fyim3bcd2t6f68BQqaaL3qlBj373VoV%2BzMlmPhWnS%2B8%2B%2FQge0jEkBU1KRsb6qsbA666ey3t6rW0vHuz3w1f5B5bbKqqfX9Fl1u8SLWZeMU2Cc83lmBzRubVgjvIr2lNUDFURSCCJDcLOsmPa4%2BQO5pQXEuABINf%2FwH3dT4hyyaBHB%2BU%2F9tPMFXwrYxJHN1NVsxY7uMXpvQQsmGviVKOI9qeIYr5uFrNDdKJBZoPxbeIwK4z6dkMdvzMoFlKJCQFAVq3oVoINOxVIGOCyFoWYYwtf%2FXvgY6pgH1CW9oPCkRCB4j3aihsBSp7%2BUN3%2FGAsnxiLlTtZdxDCDwQZkABuYylksaFK5Vm%2BkQm3IcJUXTDNV5Vy1%2FfMFED8pq3M3kfl25m7Wku%2Bf2m%2FqfUpSLyADfhJqH665W%2BIQtHUbkyORG0CxCHFOKNXeAxq%2F6z22hkLvXGqALvaTD6nc1%2B1f3QckNvCKSqpIlzRsIjE2rl1G1y%2Bt6fnGFRUDJDRHt862iO&X-Amz-Signature=d873dad05186abab606c7a535c7f2b490247d0987d484dbac292d41b738adc53&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M2E2TRJ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHkAQM90F94ydl0th1KCEUx%2FVpsNH2IgfzQr4zS0URZ1AiB8NTnpZTOXyPwICO7u7moVxvMNZav844u0i6xPwzpyeCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMIjuwmc%2BJ6Iszs7G6KtwDxmNuj4KEBD5p8xEIjbCriWdbOj0w6NzSzsaqi%2BzrsZYoS%2BqLBmyFRlpsjbdDWHjz4YVk67sqn0kkiP4DwNH54%2BvbRpI3E0SqphA82zhHuhMIKjxFQH54mK8mZi%2FlZkKcpAY%2Fl0eH7w6pjiOboMWwMOaR%2F%2F%2BGoo5pe8r%2FTUyAV7nyaTTCZBhBTII5foKChkFnFwaoFg6ctHrn7MvloZ0CBQkUz20Z%2F1WcsGlKfnxstJWQsZnHsMBENFu5FmrTGzXQ3oGMl3winbADkqcoSrgvAk6YqzWuPpG7TKev%2Bk45ph%2F%2F2cdtDsaKlwQiJrNQj82uPPriOS6lkdEIQw9jRSNWoFp6EGbe58Ur35SZIvhhdCrQQsuOiGjB7NNHTihsZLV8zMTcu0LCjJzsKv3obB%2FRWc0eVrDafZlt%2FZ3QH99Wxwy4zEqC3ds0n4Rv3MnE15%2BGqrjQy3fEj34tcAuURgdoTt0SY4pfYi%2FuXATeeRqlByz2bEKMUjnGcFBsQTSHIEaGZGNwdTDGG1SMbn0MULyyvkYLRpfzIMvzl7xbXyJSnRw1etIBjL%2BngAVbAunBNEpjK4kiJoyKhm9w21WGmn4O0GPphjYhu66VhaJE9VkOWDrs0EZ4Lf08Oh43BaQwlv%2FXvgY6pgH464cwkSbckkMjiiEXk02ZGsKlryn5GSKYN1JZuT97ZHmfYkg5MJmW1O3HAaEv%2FYvwNVx4l75tL3BKNxfq97Fpf1O9vhxjgpSMRxQf4ZtQtYi3fPbEawsNTHv5om77TCTes3Vn9JOFrIp1SozUnv%2FFx0NYqk5MSfJNcA204RpR6Owu1%2FNje9kVxO%2FiMGOcMEsJMFhgzuP48WbSYe3N2G4RTb4BjV5C&X-Amz-Signature=85f93f826a60154f8e97602f80a5dd73713f751a493857281c0594f3a40a1f7c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F57RASU%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGJ0kHwymkB2v5DxHR522PRr8yNblLzgogDb0KbkLnEAiEAnxid7u15XkdoVRfmqqRGuDApSFJOlba%2BkVuo1dyexdMq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDKrCy5gvZRwHnKp9hircA70LrlHz6HGV7n8OtNjSIj8%2BvSU74Ljl8tq6Lw0q7%2B19i4gtC8wwqZQ8TLk%2BJ3%2B%2BfedefYJbEjHEfjoY3Mq%2F%2BulTf%2FCvdlvnnqWKa7rkgSSKyt0F65RNWldGakQdtO4D2NUWF1DPkK8ajRDHqccVPFU%2B%2FOyANwr%2BuEzRC%2FhXHPT4Uq0Y2ROmM1GXMzdRKD2bhmPUFlT5OsGLOyV47LkWCx0tJAR%2BLunVImGOEwG2vwrde%2FqEpEFgkjy5oDL9HOYeGd%2FFidb0ezEa4A%2FOCyP6q8%2FNzZfYghK0Z%2BRHe7QhL3R330fawd9G%2Basg3BjZxlGfusxEUj5Npj8kVtPhmo6ufyIPeHkz7o1S6im0Fl%2FG4HI4y5cUZDto30JmuY%2Bb4Lcs2ZbdCtdBp%2B%2FemddYisi76O0T2%2Bm6ioS3vmpseke%2Bwd%2Bn0LCT8Hi6q3IKkui5O5BTL9q0IBUGJSXCDUqs8W9pildGl%2FTKS7b3W0Bqtwd%2FFII%2BCbUMm4FXtctL4K5fiR8hE10BWmimn2jP4KCNST5wezHH5zPzIU2Rx314mPTD4mwYgVPkj7BayfKWYuf4YhHQzsDtxmiyLFVfR0AN8FLnE%2B2uBOtenrwu6Hf2DZYL6VaWQejlguVCRWKLqv53MMb%2F174GOqUBiGjzaGuE5fkVDNsUV%2BlJTQ%2FpbogPC8qDnZQisLsYVYh4Oujp7wNuDJcgI8dPCwO6VjSHjvPjVEZe%2B8ne3KaEyyA7SpD482u9cTUxX%2B%2Fv9mzObvSgbMTfLx6c1Pn6yoDzREJwNEQk7fDlFDAr5Vmu1c0JP6tTdBhxJq9JmlG0QIqZT9ruomRIe4NCB1n6WtUXRe4RL3qBXv%2BUOW3Fxcr1FPnhuWH%2F&X-Amz-Signature=7b40ec13e98116623000009b1280d4c2ba7e072881e9c457acf3870ed063022e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMMH4DFP%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMI36BDmjQbfI%2Fk%2B%2Fl0k58n10hw%2B4QLCBXPr7ncB56fwIgEoNloc7ziaGhHg2cOHmFVe9CsQvDO%2FkBbqUahGk0C2Aq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDEoQIU0flwM6eSccASrcA8sQPS3EcauEZRQTOawNEusm5OSvGgw4n0tCvSuIgVOSDR7LIS9FrhXqfIz2cYp3Tv7yposg4LWZU7BZtbP6XpLum%2BNQ2AwbLYXhJpkk2C3PvhaMLmJE28d2gDKqwARHjXLl5zYDtjLk3EQ4pOP7WeJkXsQuK1qpt7gDO6CoCdjOWZUIEsaIE9Q44PI2QQhJne%2BpoD8RDtj2dELjISEuaweM2uSdn9n4jwFwkgeTCrROkRmN2v8HciuC73xBNg3lPDugt%2BMdR595bpVdMr1afE77bmA%2B5qBZluZWglUwqQ5MD2EnWqz2EmadazTfNEZjxfmAkLsG99PVXdfaVYX9zVfPaVAiJ%2F1Drrm0Luic9I3WbjSiGcVhjTCfIjXLmygRZ%2BGjbjoFl49C9zgqGkkoKWHjaA2ixR%2FE%2FPQ8SCnRbe%2FF2qmCdlVFzdE%2BL3ZTjhSe3LdtHAjvdcac62B6KDszez0Twk53eGbIsUCqK1SUu9qmhq7%2BPiD7BjbKn5dHpHr3KH8suXHTCM0BnJmvbLKZXFBjJ%2BC6re6Y2QGEtkbC6d%2BsGPW3HuQsuDK%2FY7NF0G4h16lll3fVbV1lRxL3FjOJKpX6QbQ6u0pSuFC4vPbILQHgr9ec8JjnOxhchSYQMJb%2F174GOqUBjwTKo2%2BA3Rv3V%2FXJ3c8lRoxFNi0UdQIOgACZvrgabuAX3jnunznHYYSZIBi9tIWuztffd1%2BM4%2FwivC25dP4DSz5vfNMZBaQN8IT4xwmx9lHrMyrKe3w8ljmz%2F%2FWfvBTXwfjwQtEJf43kA5Bs3mmcr3xfrxqwWEx7n10YLqrFqeUejC1WAKtx2BWojiM1Y12WZGWQkKiKooRZhcXNaGYuzJl8bVFd&X-Amz-Signature=82310553708acd3a2cfd7fbad9886b72015e912e43b8f2f4be05d718b284ab6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKY5CTO2%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBD1ana%2FPVn%2BrJixbgpKaleNiQBT97bkQ1%2BBgJQVkZ1vAiAHoRE4EZmvbcLhYjmdGGMtpWRBxaaL415tiOu7X9iizCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM3TZMxDl0EuinsoNTKtwDbImzjWzVdnodGUSWLVkJR7dZHbzhgcgBbtBzjYYjb05Am0poLIp%2FJ9%2Fw65C3727TfOTJFkBaxpRhOjWtqgDDplHcg4KiWChyC97m3lHGDGQhUsaCi7cnB0OyrGPq8OF3P6uK1SBAbf39Kyq0nV9KsdtMKu6la7f%2FWNSQEoy%2BB6PUG4LmU5BCwuqsO0fIIyfNde3yZPqEqbuPxaI9x6SpHowEJZY1RkDZ06uTO27ZPNhKcQ%2BnkjKpKtGNBjvBlydfz3fzR3bEUZb4u50jJ6PYroVQgWr9zNtFmd2dcRjpjKvofyl1xZIFj%2Fh0ARt6Rb%2BptA4635yJ1uDFNZL%2BeVuSGdmDEMeZ4KryxNl0QyI7o1D5aVSckW%2FzGXiyMmUVpkMDwNjbAduS7hmvZHfcRvTJHTQLxgumDAcZIVv22lDS%2Fhhmd9Qe31T8sY2S4lziMBtsQhQ0LY5wOjsCMWE%2Fz%2BF0TQt33Wnvqwbwq124qV0KQG%2BcGBPd8d9SdxvtzExSPhcvKKtrB3cQk%2FyJCyhJwdUoWvcP7ZMNXoV3ZP%2FvMOOBkJVN9tw4Da2owQHOEW8Gt455h5Lage1bhVytPokwUmMC5vWKlSSebL%2Ft5AUZAlvvfo9Wvghk%2FIqpHBJGaAYw2P%2FXvgY6pgF%2B9iwwxfOZPm2DUhwosKgFgkYWYQjxxX0zlJa%2F8PFEZHPpQavXgQNEqv6gwDFD0opz1dBP8%2BQHRgJiDF1SIkMs5e%2B1c2MsmnL2KpXhXgY1Q6UF%2FyFawvVwpio4JSXOpZNYf11kRFwVMzjmILbHotYZsXAxzRXmoILh8y%2FaI0dfwmlYvkdJRhcTVdY213ak8wStAa9iUslrE5csAjM6aS%2FAGR6dnFax&X-Amz-Signature=df72d5146dfcb1337a7b5d5dd6f981905cdfae45b336ab6f1d0601a5afc62fd6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKY5CTO2%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBD1ana%2FPVn%2BrJixbgpKaleNiQBT97bkQ1%2BBgJQVkZ1vAiAHoRE4EZmvbcLhYjmdGGMtpWRBxaaL415tiOu7X9iizCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM3TZMxDl0EuinsoNTKtwDbImzjWzVdnodGUSWLVkJR7dZHbzhgcgBbtBzjYYjb05Am0poLIp%2FJ9%2Fw65C3727TfOTJFkBaxpRhOjWtqgDDplHcg4KiWChyC97m3lHGDGQhUsaCi7cnB0OyrGPq8OF3P6uK1SBAbf39Kyq0nV9KsdtMKu6la7f%2FWNSQEoy%2BB6PUG4LmU5BCwuqsO0fIIyfNde3yZPqEqbuPxaI9x6SpHowEJZY1RkDZ06uTO27ZPNhKcQ%2BnkjKpKtGNBjvBlydfz3fzR3bEUZb4u50jJ6PYroVQgWr9zNtFmd2dcRjpjKvofyl1xZIFj%2Fh0ARt6Rb%2BptA4635yJ1uDFNZL%2BeVuSGdmDEMeZ4KryxNl0QyI7o1D5aVSckW%2FzGXiyMmUVpkMDwNjbAduS7hmvZHfcRvTJHTQLxgumDAcZIVv22lDS%2Fhhmd9Qe31T8sY2S4lziMBtsQhQ0LY5wOjsCMWE%2Fz%2BF0TQt33Wnvqwbwq124qV0KQG%2BcGBPd8d9SdxvtzExSPhcvKKtrB3cQk%2FyJCyhJwdUoWvcP7ZMNXoV3ZP%2FvMOOBkJVN9tw4Da2owQHOEW8Gt455h5Lage1bhVytPokwUmMC5vWKlSSebL%2Ft5AUZAlvvfo9Wvghk%2FIqpHBJGaAYw2P%2FXvgY6pgF%2B9iwwxfOZPm2DUhwosKgFgkYWYQjxxX0zlJa%2F8PFEZHPpQavXgQNEqv6gwDFD0opz1dBP8%2BQHRgJiDF1SIkMs5e%2B1c2MsmnL2KpXhXgY1Q6UF%2FyFawvVwpio4JSXOpZNYf11kRFwVMzjmILbHotYZsXAxzRXmoILh8y%2FaI0dfwmlYvkdJRhcTVdY213ak8wStAa9iUslrE5csAjM6aS%2FAGR6dnFax&X-Amz-Signature=bcddbfe789b41a7bee97443cbfa23ac246c0b5a59e7a6131ea769a1dba26a67a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
