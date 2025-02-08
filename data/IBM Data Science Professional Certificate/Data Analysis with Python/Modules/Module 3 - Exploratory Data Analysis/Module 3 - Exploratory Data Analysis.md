

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7FVMZUU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDOPkOyH0kjxA6L2CFFD%2F18VUu0Cc4vnemTmIpBvgcAngIgKTXXIpizNMi1wzOQ4W47jlX7%2FTptt%2BYDg8Y%2B0i9lUzYqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInQyGxsr6PN%2FFXxvyrcA6Qn7xQc%2F2I8ttvlE7KtypU0rMKkIsBM%2Fv5mr%2BTPtCsNh90ju%2BXwHikbYjymTl%2BAys4eFNEKJWNgNKMUBqpIvgeiWeaCbN1ov0si3%2BTpOCuSTojlkBOu6LvUIRHeGvPAU9HV%2FI2X%2BccOpV31XJucfhZZlLMAETfWcGGC1Xd1RYEf61wnQDLxoz421HdatLc5eCMoAwEiX9b%2B2De%2FuNks0eqKeSomMzNsedcnVPlR3h0duKAQrtuj2G2pZXVxQIUdHqt7cMTEd2Ra%2BRt6%2BPtm8l5JxR8a%2FdeF8NC28mCe%2BWDhGb2vbHb5vS6PJE2nZa0yNXQy2YtHYIq%2BhzCb1EgDZz0x7vhPhojeK0DTRIYVG3u13e1AtzqIPV7XEnumMQx0J3XQekM7OfmO%2F8t%2F7GhZd3CVdsxlpFyadjghxmd8ICNxfNybOjSIA3zYpD1kHLLKlSCTX95siEksPD%2BuSgXRnndC6wgwQCERFs1dGwgwb5UG%2Bg6GIQUc4JAXZkkxAi2w0jKmJrBX%2BNS2CrmrNJ81c0YMz10%2BfheanX58o2WosLg73fiQpdQ2OSTJKMcrO1GexwHCcUhJt8ziChLePSZ5CXlCSCAEC3GxIMa6CCV1%2BjCkEJipe9hl%2FMM1ZK96MNCym70GOqUBZsTiaTaEXJGRURarcdT0rToLdKIcWZmMUcguf5J11GERV19DBTv5aV%2BIhv%2BBCbhWBehasUE2KyITGAZtnrleOF2jKg%2BmC85qeGtTCc06xDdp2NnN3nyApJ6Qe6Qo6vyP3DEow7L57g9wivK0HUEO2tOnBN4f1Lpy7IcnYYyHaEvbV2ziC2mZp5JeqyRAKibZC4eExrFGj4ASsPdcAnM3UyYzjw0k&X-Amz-Signature=e9ceff307349aa5da06d29db95008cb46619700bf26a61cdd1a8fedc493de0ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7FVMZUU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDOPkOyH0kjxA6L2CFFD%2F18VUu0Cc4vnemTmIpBvgcAngIgKTXXIpizNMi1wzOQ4W47jlX7%2FTptt%2BYDg8Y%2B0i9lUzYqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInQyGxsr6PN%2FFXxvyrcA6Qn7xQc%2F2I8ttvlE7KtypU0rMKkIsBM%2Fv5mr%2BTPtCsNh90ju%2BXwHikbYjymTl%2BAys4eFNEKJWNgNKMUBqpIvgeiWeaCbN1ov0si3%2BTpOCuSTojlkBOu6LvUIRHeGvPAU9HV%2FI2X%2BccOpV31XJucfhZZlLMAETfWcGGC1Xd1RYEf61wnQDLxoz421HdatLc5eCMoAwEiX9b%2B2De%2FuNks0eqKeSomMzNsedcnVPlR3h0duKAQrtuj2G2pZXVxQIUdHqt7cMTEd2Ra%2BRt6%2BPtm8l5JxR8a%2FdeF8NC28mCe%2BWDhGb2vbHb5vS6PJE2nZa0yNXQy2YtHYIq%2BhzCb1EgDZz0x7vhPhojeK0DTRIYVG3u13e1AtzqIPV7XEnumMQx0J3XQekM7OfmO%2F8t%2F7GhZd3CVdsxlpFyadjghxmd8ICNxfNybOjSIA3zYpD1kHLLKlSCTX95siEksPD%2BuSgXRnndC6wgwQCERFs1dGwgwb5UG%2Bg6GIQUc4JAXZkkxAi2w0jKmJrBX%2BNS2CrmrNJ81c0YMz10%2BfheanX58o2WosLg73fiQpdQ2OSTJKMcrO1GexwHCcUhJt8ziChLePSZ5CXlCSCAEC3GxIMa6CCV1%2BjCkEJipe9hl%2FMM1ZK96MNCym70GOqUBZsTiaTaEXJGRURarcdT0rToLdKIcWZmMUcguf5J11GERV19DBTv5aV%2BIhv%2BBCbhWBehasUE2KyITGAZtnrleOF2jKg%2BmC85qeGtTCc06xDdp2NnN3nyApJ6Qe6Qo6vyP3DEow7L57g9wivK0HUEO2tOnBN4f1Lpy7IcnYYyHaEvbV2ziC2mZp5JeqyRAKibZC4eExrFGj4ASsPdcAnM3UyYzjw0k&X-Amz-Signature=44c4a4ff1f1e616682784850b78ce0881de5e6a5e0ed3f6cab0c9879741206bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7FVMZUU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDOPkOyH0kjxA6L2CFFD%2F18VUu0Cc4vnemTmIpBvgcAngIgKTXXIpizNMi1wzOQ4W47jlX7%2FTptt%2BYDg8Y%2B0i9lUzYqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInQyGxsr6PN%2FFXxvyrcA6Qn7xQc%2F2I8ttvlE7KtypU0rMKkIsBM%2Fv5mr%2BTPtCsNh90ju%2BXwHikbYjymTl%2BAys4eFNEKJWNgNKMUBqpIvgeiWeaCbN1ov0si3%2BTpOCuSTojlkBOu6LvUIRHeGvPAU9HV%2FI2X%2BccOpV31XJucfhZZlLMAETfWcGGC1Xd1RYEf61wnQDLxoz421HdatLc5eCMoAwEiX9b%2B2De%2FuNks0eqKeSomMzNsedcnVPlR3h0duKAQrtuj2G2pZXVxQIUdHqt7cMTEd2Ra%2BRt6%2BPtm8l5JxR8a%2FdeF8NC28mCe%2BWDhGb2vbHb5vS6PJE2nZa0yNXQy2YtHYIq%2BhzCb1EgDZz0x7vhPhojeK0DTRIYVG3u13e1AtzqIPV7XEnumMQx0J3XQekM7OfmO%2F8t%2F7GhZd3CVdsxlpFyadjghxmd8ICNxfNybOjSIA3zYpD1kHLLKlSCTX95siEksPD%2BuSgXRnndC6wgwQCERFs1dGwgwb5UG%2Bg6GIQUc4JAXZkkxAi2w0jKmJrBX%2BNS2CrmrNJ81c0YMz10%2BfheanX58o2WosLg73fiQpdQ2OSTJKMcrO1GexwHCcUhJt8ziChLePSZ5CXlCSCAEC3GxIMa6CCV1%2BjCkEJipe9hl%2FMM1ZK96MNCym70GOqUBZsTiaTaEXJGRURarcdT0rToLdKIcWZmMUcguf5J11GERV19DBTv5aV%2BIhv%2BBCbhWBehasUE2KyITGAZtnrleOF2jKg%2BmC85qeGtTCc06xDdp2NnN3nyApJ6Qe6Qo6vyP3DEow7L57g9wivK0HUEO2tOnBN4f1Lpy7IcnYYyHaEvbV2ziC2mZp5JeqyRAKibZC4eExrFGj4ASsPdcAnM3UyYzjw0k&X-Amz-Signature=68239abe963d3f0becf4754e88f9aa4af8352c24ee9bb69099d81a4ee90c9a7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXDW57Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDpgysalmwqc9OVq4Q5J%2FrmE1O%2BNSLciQEoIo3uZocNlgIgS2vQwkHU5dDw0ADI2f%2FF28Z%2B0ZTenOoIHzIlQDCLg0MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGOmDtyA7TleR%2F1nyrcA7Jb1Dd9AUBada4xVXcmXlpY3eKuluwNjiO2GScdM1PUUHMQwDcuAD62YgMGCVk%2FstjIGe%2FUFncjVnul9DkszrC0riQH8bRvMD1uu39DUY3BI5qj24DPNGX8XbzCodU3G3yIDMS%2B0rvZkrCDAWOwA56ce9QHMbbASupnW2SZncSbtyO6Q2b3HZGitTwfHdq73l7pz5OO1wv%2F5%2F81nc3awRhPbM%2BRMNNXbWzoaawzAMeI29kAJ07xbACxj8p0iMNSOQ2qNzm3KVIp3pcmW3Cum71X1HqGYcerAIOiq8Nyec2Z7PRIZ9XmpquFOkQZY4kJFX5gzBHpHoZ2j5crSzQWOAIfxHQmZkiq1%2BPnrboP1iijs5HDHiCnXvXR88ocK%2FmUvYnJdFTTK0nsIRVlExeE4eW3t2xIHTgwR5CcXOQiKVUC62T29Uvx%2BjRL89oY1u8XeJPG3lU5brmwlFeVZrdPIeVwJYww6LwRqN%2BBKzOAg4z5Y7gagPUXkH02bkFkuamFj%2B8jv%2FHVR4qme4xtVoWQ4n9wItixTv54X8fdf3jc100KJHHmZGXFLVaWQ5iR4rpccLcMRpy65U2CUy5Pln6TItmR8Sk3NhwbuH7yrEX3mx3zio87hoVJ6cWx%2BoTMMJyzm70GOqUBILR8bfPLht2RkatuEgsX94gBjdrKgf9fZjqfwajNaEmlIJ%2BlwNmZj1776EbsRyqUXqwLjuKIcFxE4bh8NytgW552%2FVHObKl9zpJD1FCDO4Y14dIJ9N6kWWFEgd1rHO2JTzDTjyLi3Mehbm07nf%2BLOANplyPYtDs8PHfolyp%2BQL4pxTvWXg4XeInya0MgeGM5WJGn28NMt%2FcLNYNxTPuOFx34%2BUa4&X-Amz-Signature=ef2d86ca37be0a40f1fa56c9f5072f4b3d5d39f67d761572dcdbc4def9c7c0c4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXDW57Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDpgysalmwqc9OVq4Q5J%2FrmE1O%2BNSLciQEoIo3uZocNlgIgS2vQwkHU5dDw0ADI2f%2FF28Z%2B0ZTenOoIHzIlQDCLg0MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGOmDtyA7TleR%2F1nyrcA7Jb1Dd9AUBada4xVXcmXlpY3eKuluwNjiO2GScdM1PUUHMQwDcuAD62YgMGCVk%2FstjIGe%2FUFncjVnul9DkszrC0riQH8bRvMD1uu39DUY3BI5qj24DPNGX8XbzCodU3G3yIDMS%2B0rvZkrCDAWOwA56ce9QHMbbASupnW2SZncSbtyO6Q2b3HZGitTwfHdq73l7pz5OO1wv%2F5%2F81nc3awRhPbM%2BRMNNXbWzoaawzAMeI29kAJ07xbACxj8p0iMNSOQ2qNzm3KVIp3pcmW3Cum71X1HqGYcerAIOiq8Nyec2Z7PRIZ9XmpquFOkQZY4kJFX5gzBHpHoZ2j5crSzQWOAIfxHQmZkiq1%2BPnrboP1iijs5HDHiCnXvXR88ocK%2FmUvYnJdFTTK0nsIRVlExeE4eW3t2xIHTgwR5CcXOQiKVUC62T29Uvx%2BjRL89oY1u8XeJPG3lU5brmwlFeVZrdPIeVwJYww6LwRqN%2BBKzOAg4z5Y7gagPUXkH02bkFkuamFj%2B8jv%2FHVR4qme4xtVoWQ4n9wItixTv54X8fdf3jc100KJHHmZGXFLVaWQ5iR4rpccLcMRpy65U2CUy5Pln6TItmR8Sk3NhwbuH7yrEX3mx3zio87hoVJ6cWx%2BoTMMJyzm70GOqUBILR8bfPLht2RkatuEgsX94gBjdrKgf9fZjqfwajNaEmlIJ%2BlwNmZj1776EbsRyqUXqwLjuKIcFxE4bh8NytgW552%2FVHObKl9zpJD1FCDO4Y14dIJ9N6kWWFEgd1rHO2JTzDTjyLi3Mehbm07nf%2BLOANplyPYtDs8PHfolyp%2BQL4pxTvWXg4XeInya0MgeGM5WJGn28NMt%2FcLNYNxTPuOFx34%2BUa4&X-Amz-Signature=fe239fe7a63a03715e2f9f5ea33b700e459cd3e688b77c2d9e3477753bcbaad4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXDW57Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDpgysalmwqc9OVq4Q5J%2FrmE1O%2BNSLciQEoIo3uZocNlgIgS2vQwkHU5dDw0ADI2f%2FF28Z%2B0ZTenOoIHzIlQDCLg0MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGOmDtyA7TleR%2F1nyrcA7Jb1Dd9AUBada4xVXcmXlpY3eKuluwNjiO2GScdM1PUUHMQwDcuAD62YgMGCVk%2FstjIGe%2FUFncjVnul9DkszrC0riQH8bRvMD1uu39DUY3BI5qj24DPNGX8XbzCodU3G3yIDMS%2B0rvZkrCDAWOwA56ce9QHMbbASupnW2SZncSbtyO6Q2b3HZGitTwfHdq73l7pz5OO1wv%2F5%2F81nc3awRhPbM%2BRMNNXbWzoaawzAMeI29kAJ07xbACxj8p0iMNSOQ2qNzm3KVIp3pcmW3Cum71X1HqGYcerAIOiq8Nyec2Z7PRIZ9XmpquFOkQZY4kJFX5gzBHpHoZ2j5crSzQWOAIfxHQmZkiq1%2BPnrboP1iijs5HDHiCnXvXR88ocK%2FmUvYnJdFTTK0nsIRVlExeE4eW3t2xIHTgwR5CcXOQiKVUC62T29Uvx%2BjRL89oY1u8XeJPG3lU5brmwlFeVZrdPIeVwJYww6LwRqN%2BBKzOAg4z5Y7gagPUXkH02bkFkuamFj%2B8jv%2FHVR4qme4xtVoWQ4n9wItixTv54X8fdf3jc100KJHHmZGXFLVaWQ5iR4rpccLcMRpy65U2CUy5Pln6TItmR8Sk3NhwbuH7yrEX3mx3zio87hoVJ6cWx%2BoTMMJyzm70GOqUBILR8bfPLht2RkatuEgsX94gBjdrKgf9fZjqfwajNaEmlIJ%2BlwNmZj1776EbsRyqUXqwLjuKIcFxE4bh8NytgW552%2FVHObKl9zpJD1FCDO4Y14dIJ9N6kWWFEgd1rHO2JTzDTjyLi3Mehbm07nf%2BLOANplyPYtDs8PHfolyp%2BQL4pxTvWXg4XeInya0MgeGM5WJGn28NMt%2FcLNYNxTPuOFx34%2BUa4&X-Amz-Signature=1d3e18631f4e236f853cbce709bd4572029b0e8bbbe9f29ac144ae4e380b3e66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXDW57Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDpgysalmwqc9OVq4Q5J%2FrmE1O%2BNSLciQEoIo3uZocNlgIgS2vQwkHU5dDw0ADI2f%2FF28Z%2B0ZTenOoIHzIlQDCLg0MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGOmDtyA7TleR%2F1nyrcA7Jb1Dd9AUBada4xVXcmXlpY3eKuluwNjiO2GScdM1PUUHMQwDcuAD62YgMGCVk%2FstjIGe%2FUFncjVnul9DkszrC0riQH8bRvMD1uu39DUY3BI5qj24DPNGX8XbzCodU3G3yIDMS%2B0rvZkrCDAWOwA56ce9QHMbbASupnW2SZncSbtyO6Q2b3HZGitTwfHdq73l7pz5OO1wv%2F5%2F81nc3awRhPbM%2BRMNNXbWzoaawzAMeI29kAJ07xbACxj8p0iMNSOQ2qNzm3KVIp3pcmW3Cum71X1HqGYcerAIOiq8Nyec2Z7PRIZ9XmpquFOkQZY4kJFX5gzBHpHoZ2j5crSzQWOAIfxHQmZkiq1%2BPnrboP1iijs5HDHiCnXvXR88ocK%2FmUvYnJdFTTK0nsIRVlExeE4eW3t2xIHTgwR5CcXOQiKVUC62T29Uvx%2BjRL89oY1u8XeJPG3lU5brmwlFeVZrdPIeVwJYww6LwRqN%2BBKzOAg4z5Y7gagPUXkH02bkFkuamFj%2B8jv%2FHVR4qme4xtVoWQ4n9wItixTv54X8fdf3jc100KJHHmZGXFLVaWQ5iR4rpccLcMRpy65U2CUy5Pln6TItmR8Sk3NhwbuH7yrEX3mx3zio87hoVJ6cWx%2BoTMMJyzm70GOqUBILR8bfPLht2RkatuEgsX94gBjdrKgf9fZjqfwajNaEmlIJ%2BlwNmZj1776EbsRyqUXqwLjuKIcFxE4bh8NytgW552%2FVHObKl9zpJD1FCDO4Y14dIJ9N6kWWFEgd1rHO2JTzDTjyLi3Mehbm07nf%2BLOANplyPYtDs8PHfolyp%2BQL4pxTvWXg4XeInya0MgeGM5WJGn28NMt%2FcLNYNxTPuOFx34%2BUa4&X-Amz-Signature=c7958772ed12cf827fc65c289f9e863e41a59de2b2a734f1663d2dc6fd9801a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXDW57Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDpgysalmwqc9OVq4Q5J%2FrmE1O%2BNSLciQEoIo3uZocNlgIgS2vQwkHU5dDw0ADI2f%2FF28Z%2B0ZTenOoIHzIlQDCLg0MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGOmDtyA7TleR%2F1nyrcA7Jb1Dd9AUBada4xVXcmXlpY3eKuluwNjiO2GScdM1PUUHMQwDcuAD62YgMGCVk%2FstjIGe%2FUFncjVnul9DkszrC0riQH8bRvMD1uu39DUY3BI5qj24DPNGX8XbzCodU3G3yIDMS%2B0rvZkrCDAWOwA56ce9QHMbbASupnW2SZncSbtyO6Q2b3HZGitTwfHdq73l7pz5OO1wv%2F5%2F81nc3awRhPbM%2BRMNNXbWzoaawzAMeI29kAJ07xbACxj8p0iMNSOQ2qNzm3KVIp3pcmW3Cum71X1HqGYcerAIOiq8Nyec2Z7PRIZ9XmpquFOkQZY4kJFX5gzBHpHoZ2j5crSzQWOAIfxHQmZkiq1%2BPnrboP1iijs5HDHiCnXvXR88ocK%2FmUvYnJdFTTK0nsIRVlExeE4eW3t2xIHTgwR5CcXOQiKVUC62T29Uvx%2BjRL89oY1u8XeJPG3lU5brmwlFeVZrdPIeVwJYww6LwRqN%2BBKzOAg4z5Y7gagPUXkH02bkFkuamFj%2B8jv%2FHVR4qme4xtVoWQ4n9wItixTv54X8fdf3jc100KJHHmZGXFLVaWQ5iR4rpccLcMRpy65U2CUy5Pln6TItmR8Sk3NhwbuH7yrEX3mx3zio87hoVJ6cWx%2BoTMMJyzm70GOqUBILR8bfPLht2RkatuEgsX94gBjdrKgf9fZjqfwajNaEmlIJ%2BlwNmZj1776EbsRyqUXqwLjuKIcFxE4bh8NytgW552%2FVHObKl9zpJD1FCDO4Y14dIJ9N6kWWFEgd1rHO2JTzDTjyLi3Mehbm07nf%2BLOANplyPYtDs8PHfolyp%2BQL4pxTvWXg4XeInya0MgeGM5WJGn28NMt%2FcLNYNxTPuOFx34%2BUa4&X-Amz-Signature=0d90ab76295f44d28d939631a56751725fdb10dad67623295756e03707cb5545&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXDW57Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDpgysalmwqc9OVq4Q5J%2FrmE1O%2BNSLciQEoIo3uZocNlgIgS2vQwkHU5dDw0ADI2f%2FF28Z%2B0ZTenOoIHzIlQDCLg0MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGOmDtyA7TleR%2F1nyrcA7Jb1Dd9AUBada4xVXcmXlpY3eKuluwNjiO2GScdM1PUUHMQwDcuAD62YgMGCVk%2FstjIGe%2FUFncjVnul9DkszrC0riQH8bRvMD1uu39DUY3BI5qj24DPNGX8XbzCodU3G3yIDMS%2B0rvZkrCDAWOwA56ce9QHMbbASupnW2SZncSbtyO6Q2b3HZGitTwfHdq73l7pz5OO1wv%2F5%2F81nc3awRhPbM%2BRMNNXbWzoaawzAMeI29kAJ07xbACxj8p0iMNSOQ2qNzm3KVIp3pcmW3Cum71X1HqGYcerAIOiq8Nyec2Z7PRIZ9XmpquFOkQZY4kJFX5gzBHpHoZ2j5crSzQWOAIfxHQmZkiq1%2BPnrboP1iijs5HDHiCnXvXR88ocK%2FmUvYnJdFTTK0nsIRVlExeE4eW3t2xIHTgwR5CcXOQiKVUC62T29Uvx%2BjRL89oY1u8XeJPG3lU5brmwlFeVZrdPIeVwJYww6LwRqN%2BBKzOAg4z5Y7gagPUXkH02bkFkuamFj%2B8jv%2FHVR4qme4xtVoWQ4n9wItixTv54X8fdf3jc100KJHHmZGXFLVaWQ5iR4rpccLcMRpy65U2CUy5Pln6TItmR8Sk3NhwbuH7yrEX3mx3zio87hoVJ6cWx%2BoTMMJyzm70GOqUBILR8bfPLht2RkatuEgsX94gBjdrKgf9fZjqfwajNaEmlIJ%2BlwNmZj1776EbsRyqUXqwLjuKIcFxE4bh8NytgW552%2FVHObKl9zpJD1FCDO4Y14dIJ9N6kWWFEgd1rHO2JTzDTjyLi3Mehbm07nf%2BLOANplyPYtDs8PHfolyp%2BQL4pxTvWXg4XeInya0MgeGM5WJGn28NMt%2FcLNYNxTPuOFx34%2BUa4&X-Amz-Signature=2a488e52e03f9348c7e2d5f04086e18d01dad58f48ae090b222779e48470daaa&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V75ZWE3X%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIApVYFq6Faa3w4hT4cEgb2W785wF3cKbK4grkJoePuxcAiAv%2Bin6k8PiWLPY7o8Fi50ZD2YUqRo%2B28XbgGM20%2BiBSyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHY%2BAnAy5bY8oesaqKtwDltA5V0R6xoHgmorf56CFeMiNpboB39eG7GlFn2a9WuiMJ0nR9PkeDm6pj%2FEhyK7c1ohvN%2BL7s9od72CQGzNnrP3%2FoLWztIsCB5PPpCmfiUktuYFR87R23KQ1zJPi%2FuEV8z5AV3si1reRc9sP3DVA3Fu7IrLwyVo%2F18%2FjW2O5QqO4T7jmoiF%2BowmXw%2FoBhJFRJvmm4GWRZS%2B9GNkYSHngS1qzHUro%2BVIH76BsQjWKRs2Txoasd22OG4B0jM8pjT7sF4I%2BXeeAmT9OAcCS40jWHf7cx1ilY3uDCvvfrY58MdpnQ0xLRO5xVl697DpJbHfvetJNaly9LspmOto%2FB7yTjhgSh7mkGgsAJ%2Bmykhv9QviADZPU8N4QsGQbq5c2ezwIBXXHrMaOIHcJnPvpYWUlTDEDbXHayzEHGrLzSUi2uwd8YDkduCTkS4nLxOZuKt5uNfkO54KgVhJyJBBW5WX28f%2BBydz5XDdyESeTqTuUQML7NBIkAodgiPGj4kLHUYx3fufItcSOkpilTIz7Q5KfZDQKnMehuWxdBpc5%2BLPqgvcaWqPSD4Cu4D%2Bs8QI3qBHj%2FeUyop2xvwRzquIGqVGUr%2BRMO%2BP5xXkFmDez%2FsOEZJceiUGk8PKwyZe6vzYw07KbvQY6pgG6mXR9ChxMbd3OT6oxSKfnTbnGgbLl4VS0xWdM1i%2FkJLOzSUqr5YsY7uh%2BuZjvlMXHxvAHC6Jl1dFSw6SV%2Bn7TFrORAJTvK4DdY7uaOVRGPhKSjXB%2FpOFOj0DDE3SQHQJlGRveN8bJct18VBgLbmILhDff8KWSasgRkY4rwycFLydRHCn0LJyl4GVD68jukwRzcGUCKr94wg98KXEurIlxaVaduAi4&X-Amz-Signature=b4d1b0cae1b47e7a0374d5a2e441cdaf7c2de1e6dd242cd6001a9a13ff116d81&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SV7JKTMV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIFg4TfYjdr0s7F6KVhLPQpCJV469SH7SWayfXNYKm5R5AiBQBn2swGDj9OwyogwTPi8ecIscHze3xWNT3dz9vKQ7aCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMopcabXI8A%2BOBNaBdKtwDfqDr7xXGezQSps5kSTxr3X5egpbRyXKkxdfqAgh5f7CpKKTl0hpF%2BpresNL1EqqmkJl4sKwss%2B5dc73ouuxZheJzi2nMxwE48RatbKE%2BbNl7Tvu%2FSzBX6CvUp%2FAzMRaXn3wjCm5bCFuqgrVUN8pjpxi8IBhyrk8pbfAr1LRKciuCO%2Fg4qbkQQO0Kd3eEuRIT%2F6CUNf5JPYd9ib%2Fk6mv3Srwz4ot2zBMvpdlJ9xcGQBLo3EUGfUBe%2F1Sill%2FPlu3OJKqQQGlrIEdC6%2Fkz9TzINwe4ekxiwpgCJ%2FKk0QVsUANg8rw1yf%2Fmkbk2f1qZnKvIzGmJaX7%2Bvkh293drwBJyR5ZU7XC%2ByCZe%2F14hObTjvgEP8aMqa%2FYQmWh87dSGO9LQS4lJAbQSYeCg2XO8l6wxd3RiaQHL5rJ4iCnljBkXuANDPKkAqVlFPuZnutHV3PwqFhZZ6%2Bo9Dj%2B7zL%2Fuh1v%2BfqF6Wr1KN9xJ%2FbkmuLQG%2Fnttdus5QUcHZGs19Z3LoKOeRixEWh%2BoTdsbYWr7zCUElZU9rgSeUTf2VhTfrB2sxDt7wyfJFWIXAYy7X%2FIQB57XALHw8rcbYXcaaan6nwIZ8eRZTNsaIrLrimQqVMr5EB34xN44fpY8%2BlWm0rswn7KbvQY6pgEFsNaJNCcQYt%2B1spzrvWXybqLNt9wd%2Bl0RizGK3k2BT0dKA6EPBGRgtySZISWjQVc3ZkEhy4MyM4DlrSfnx%2BFgu4vC1TQ%2BnF3peUlFKbM%2F1Sno1tvo27SwkhXhXoIBH5r%2Fwd3vWVjaVUMm3XnHvc12%2B3s9go76fwDFx07ymEtfNO0VKuqsJFcJT4KUClalsSXFAiGxrgYj2hW3%2BWbgSgQgMh6NvC6Q&X-Amz-Signature=1d976f7a803b5fd968fce57bcbd854357eabe06ca1bcd81f79e9a885053bb611&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXDW57Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDpgysalmwqc9OVq4Q5J%2FrmE1O%2BNSLciQEoIo3uZocNlgIgS2vQwkHU5dDw0ADI2f%2FF28Z%2B0ZTenOoIHzIlQDCLg0MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGOmDtyA7TleR%2F1nyrcA7Jb1Dd9AUBada4xVXcmXlpY3eKuluwNjiO2GScdM1PUUHMQwDcuAD62YgMGCVk%2FstjIGe%2FUFncjVnul9DkszrC0riQH8bRvMD1uu39DUY3BI5qj24DPNGX8XbzCodU3G3yIDMS%2B0rvZkrCDAWOwA56ce9QHMbbASupnW2SZncSbtyO6Q2b3HZGitTwfHdq73l7pz5OO1wv%2F5%2F81nc3awRhPbM%2BRMNNXbWzoaawzAMeI29kAJ07xbACxj8p0iMNSOQ2qNzm3KVIp3pcmW3Cum71X1HqGYcerAIOiq8Nyec2Z7PRIZ9XmpquFOkQZY4kJFX5gzBHpHoZ2j5crSzQWOAIfxHQmZkiq1%2BPnrboP1iijs5HDHiCnXvXR88ocK%2FmUvYnJdFTTK0nsIRVlExeE4eW3t2xIHTgwR5CcXOQiKVUC62T29Uvx%2BjRL89oY1u8XeJPG3lU5brmwlFeVZrdPIeVwJYww6LwRqN%2BBKzOAg4z5Y7gagPUXkH02bkFkuamFj%2B8jv%2FHVR4qme4xtVoWQ4n9wItixTv54X8fdf3jc100KJHHmZGXFLVaWQ5iR4rpccLcMRpy65U2CUy5Pln6TItmR8Sk3NhwbuH7yrEX3mx3zio87hoVJ6cWx%2BoTMMJyzm70GOqUBILR8bfPLht2RkatuEgsX94gBjdrKgf9fZjqfwajNaEmlIJ%2BlwNmZj1776EbsRyqUXqwLjuKIcFxE4bh8NytgW552%2FVHObKl9zpJD1FCDO4Y14dIJ9N6kWWFEgd1rHO2JTzDTjyLi3Mehbm07nf%2BLOANplyPYtDs8PHfolyp%2BQL4pxTvWXg4XeInya0MgeGM5WJGn28NMt%2FcLNYNxTPuOFx34%2BUa4&X-Amz-Signature=d75ad00388aa4e2b56d4c997a96c91ae33c8d7d6dcaa73b1de4e5ca4890a9a10&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXDW57Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDpgysalmwqc9OVq4Q5J%2FrmE1O%2BNSLciQEoIo3uZocNlgIgS2vQwkHU5dDw0ADI2f%2FF28Z%2B0ZTenOoIHzIlQDCLg0MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGOmDtyA7TleR%2F1nyrcA7Jb1Dd9AUBada4xVXcmXlpY3eKuluwNjiO2GScdM1PUUHMQwDcuAD62YgMGCVk%2FstjIGe%2FUFncjVnul9DkszrC0riQH8bRvMD1uu39DUY3BI5qj24DPNGX8XbzCodU3G3yIDMS%2B0rvZkrCDAWOwA56ce9QHMbbASupnW2SZncSbtyO6Q2b3HZGitTwfHdq73l7pz5OO1wv%2F5%2F81nc3awRhPbM%2BRMNNXbWzoaawzAMeI29kAJ07xbACxj8p0iMNSOQ2qNzm3KVIp3pcmW3Cum71X1HqGYcerAIOiq8Nyec2Z7PRIZ9XmpquFOkQZY4kJFX5gzBHpHoZ2j5crSzQWOAIfxHQmZkiq1%2BPnrboP1iijs5HDHiCnXvXR88ocK%2FmUvYnJdFTTK0nsIRVlExeE4eW3t2xIHTgwR5CcXOQiKVUC62T29Uvx%2BjRL89oY1u8XeJPG3lU5brmwlFeVZrdPIeVwJYww6LwRqN%2BBKzOAg4z5Y7gagPUXkH02bkFkuamFj%2B8jv%2FHVR4qme4xtVoWQ4n9wItixTv54X8fdf3jc100KJHHmZGXFLVaWQ5iR4rpccLcMRpy65U2CUy5Pln6TItmR8Sk3NhwbuH7yrEX3mx3zio87hoVJ6cWx%2BoTMMJyzm70GOqUBILR8bfPLht2RkatuEgsX94gBjdrKgf9fZjqfwajNaEmlIJ%2BlwNmZj1776EbsRyqUXqwLjuKIcFxE4bh8NytgW552%2FVHObKl9zpJD1FCDO4Y14dIJ9N6kWWFEgd1rHO2JTzDTjyLi3Mehbm07nf%2BLOANplyPYtDs8PHfolyp%2BQL4pxTvWXg4XeInya0MgeGM5WJGn28NMt%2FcLNYNxTPuOFx34%2BUa4&X-Amz-Signature=88e64bedaae1a899e95017e5cff345d386b9f1d481b5d767d4cf9f785acb60f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIXDW57Z%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDpgysalmwqc9OVq4Q5J%2FrmE1O%2BNSLciQEoIo3uZocNlgIgS2vQwkHU5dDw0ADI2f%2FF28Z%2B0ZTenOoIHzIlQDCLg0MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGOmDtyA7TleR%2F1nyrcA7Jb1Dd9AUBada4xVXcmXlpY3eKuluwNjiO2GScdM1PUUHMQwDcuAD62YgMGCVk%2FstjIGe%2FUFncjVnul9DkszrC0riQH8bRvMD1uu39DUY3BI5qj24DPNGX8XbzCodU3G3yIDMS%2B0rvZkrCDAWOwA56ce9QHMbbASupnW2SZncSbtyO6Q2b3HZGitTwfHdq73l7pz5OO1wv%2F5%2F81nc3awRhPbM%2BRMNNXbWzoaawzAMeI29kAJ07xbACxj8p0iMNSOQ2qNzm3KVIp3pcmW3Cum71X1HqGYcerAIOiq8Nyec2Z7PRIZ9XmpquFOkQZY4kJFX5gzBHpHoZ2j5crSzQWOAIfxHQmZkiq1%2BPnrboP1iijs5HDHiCnXvXR88ocK%2FmUvYnJdFTTK0nsIRVlExeE4eW3t2xIHTgwR5CcXOQiKVUC62T29Uvx%2BjRL89oY1u8XeJPG3lU5brmwlFeVZrdPIeVwJYww6LwRqN%2BBKzOAg4z5Y7gagPUXkH02bkFkuamFj%2B8jv%2FHVR4qme4xtVoWQ4n9wItixTv54X8fdf3jc100KJHHmZGXFLVaWQ5iR4rpccLcMRpy65U2CUy5Pln6TItmR8Sk3NhwbuH7yrEX3mx3zio87hoVJ6cWx%2BoTMMJyzm70GOqUBILR8bfPLht2RkatuEgsX94gBjdrKgf9fZjqfwajNaEmlIJ%2BlwNmZj1776EbsRyqUXqwLjuKIcFxE4bh8NytgW552%2FVHObKl9zpJD1FCDO4Y14dIJ9N6kWWFEgd1rHO2JTzDTjyLi3Mehbm07nf%2BLOANplyPYtDs8PHfolyp%2BQL4pxTvWXg4XeInya0MgeGM5WJGn28NMt%2FcLNYNxTPuOFx34%2BUa4&X-Amz-Signature=db25f06d48c5bc9982d5ffccc3c618625c42f2ed518aefd6850e43e6448748db&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637TYXFMK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIDbMM7itHwOG36GyujVlqH2aUeqeaywM6Qt4S%2FTuXy1jAiEAlzspxZd3ckSYO34mS9wNUU9BcS39z2U2HawnryZE%2BUIqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFd7YjiwxB9gAKhqhSrcA2WGQTrQOGGsoMySYMk9K7AEo4bReyQvIIIlkKU7j1IieQ5AIZO3w8sL6y4ad8nMOa7kMJ0d%2FZn78ITU3I505EfDALon1sTLnHJ7SQwFdbJtgGMdCb18pBa59BRIiHMjhnLuZ3mZJ5wKh6DJzce7CzpZxnnT03dnwvCPyV3z9GmsMMzl2PphkJ%2BOl9isAzSFUsIJdaq9T6Sg%2F936esEa7yCZJRAQEzX109oC%2FxFDtGRg5JLA%2BhDDsbEUOIRfA60QJ8xRRWfJqaAd2oifeJ0RfgJFhrvyiQ47aEJ%2BX4N2RezEE0fLi5swshUPhDGnOqsmE8gBxhHEy1C1BNLLhBAWzEamjRSnVXTlnlUl2ZaXCDMgvuVyutUSqtogMPucQDiId4%2BXszn74XObsSKniGAP1qq3PRW4EwTNkmoaWs%2FhWuXKVC3AlkwLG0o1ddJr96I%2FVTcVIFi33ERLp1sVVA8b9OOx0veIONCUk5vcywj29jU4SO%2FCBUZ9e6ZGMXcTYMu%2FwVLr6yM8FIYHejFUfJtAPIZbBv0CWM5ywLy8DKPli8cjDn%2F63gqh2ib3hFuZyowCqqpXqlmFFcx3%2FFKvU%2FPJkTh9cSeDWWBjVh4J2SdFji4j2zck9TFNAZ%2Bp8GZtMOGym70GOqUBTuZvE%2BpzEv9w9Vl6HCX%2BSDsllAs%2B7fCB0ucxpih2hVwfOpOxyVdjn%2Fz1EuGR4eHzI1%2FVAWUXJ7EmIeSIuWprGlUo%2FpJ29eHriQnfOOm6btNYR72LrzHUQKKwthcIolvfMdsa20SJBehDNs16AM5sbdr%2FNXNoljFISPW5SRAJiL3H7awEDNWXatFm0fnWvQW6VbklSyFfehp8dIJdi8O33lYTk97K&X-Amz-Signature=cfa33adfd8b7a52765fdc0b1a97ded14886c522214fb73ba43d4e7daa8a5d836&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REVJ2YTY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIBGWV4X%2FmGUe5%2FMZCrWPKfDbroJl5oYT3yeCj1dwlv9VAiEAsYl9CXIexv9%2FeB%2FDIIql9lwJtGFmWqlNY26lVMWhdzIqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLJ7y2f5TMLR0KZ5SCrcA5Dcw%2BLAepYVpL6SEp11HT7q0%2FEdGOGICT8J6hr0yfYLK6tkB1n9v6azyRVSe9sOYC903xXBgekWmbndX%2FQGC9cwx0AePhXP0ET1Glg5IGAtYVzKfcOTRr0EUIS%2B%2BETjYU3N7lfhtfjL%2BwDn9PpGyq84yJZBQMupPPG6cVjxcj1gf3MVDnQRfp%2BOPLFHpYqcq8PF59%2B9qyf1QgblWVLltQXOo0iR2HPgeoXCDmq%2Fli49ik6v37NniOGljwAHh1VCcixHatbk0zVRc671kMUkXLhGZR1s1DIch4GOn5nDk%2FSV7UaGeUuKmc9fQDTI0ZTkvlidKh70HLwMuRaPG2syy%2B%2BoFPClT8ZOHYnd7rIqjNG%2F%2F25ZsV3LRgmZo8di0HFpIe9z0iKAa%2B14rlgnNGfpt5gjiLAihyrsB%2Fg9x%2FhYMsiee5S%2FVvB8T8ZU%2BNUHliTfYN1Tbw%2BPftSPEh6ZWXepqv2yFV%2Bg%2Bgw%2FmjRHurYbZP559Pl1Mzv8Z5A62YbDcycQRAOJGLEuGR6v5%2FjYPYN5EKqX%2B7kJ0MgVlQAjNbaxdAMJL7lCGZ2z7f43mcVvSLyca71fTltZ3UdfRkD6Vj%2B%2Bj%2BYqi1F%2FST%2FpPkgnNNGyKNZVN2p7CwgHfLq0N0j3MPyym70GOqUBzNImCG7mrZsgzGwIM0zmXxyhJNFQ6WKiyZst7x5%2F3FoVVFdDr%2F2DgnB2SvwOCy85IKSwzhKszn9WtB4bf2YpPT8D%2F1x0JPFDmUK6R31ZXzM%2Fjx5MSJ50WZtnxKY4BDzmojpernxf%2F1FsRIRnpjXRHRkylcNH8%2B79EGy6Mm4lPE4uRh2Z1RkMS3UdkcB3cuKbYq8CHJuddqsnXeDhx4ANtzqxwZQq&X-Amz-Signature=30a8c12ceeabf79a0d4400913af3aa18ec32a9a94274331ce68ac6c1ca81b866&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2GWFDE2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEglj5Nzd6vJU2oMQpqfaWkkoC%2BSAwwboeHlS5KFRZnJAiBplQRvi669cyrHZ879B%2B%2F5Y1H2TzhQDEqO1TqTt6WD%2FSqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMU3cZxhgE2gz4HgcVKtwDA02C6SFT9AwrxXXGovtFACamu0R1uDgjHMNESTcRidioQIteJQjffqvr7f0OBV5RnEUF6dTHHpbhvxnWnSOWiWN1jlYOKOZpqb43VZ3wxM7dQhkv1qBgOmbKFBFJOFthx6aHqPpu8f1PcMk8%2BQvlYyPy6NjYUSXlwBWHn3dLgcmxlD%2FBS8vKyiYsH3vpjQNnTAXwReGAz%2BllukIx7rGK85Sj3jege1dqVIiuh2RUqFSU4SFZAKE9thoDtrEPB5Xcj2H8DblvsjxsSlr0ce6w40qJK%2BV%2Ff%2BbOU0ajqHKx2L5ukkgAXk1Muly%2FrEdWlttbnllB7Ki543uGI5ygEuHQ5P8JDU%2FuiAqrRXpnqqc%2FuDkU7nnot7pHics1h%2FovXeL5mc%2FnX7I4cJLHz1iYlvRGBszz9aXoqBQYFpxsf1HgJKlLptYX7dTFeKquvx2OajfOz3zpdQSUAWCgBw3XGX%2FQEgrW1ojYzxHVmLJywceFFy0x9ccu8ebuCrFYNLIaym87J%2B9v0PS%2B%2FYlzdjMFvKRZX0o5%2FSxTtV5WNgW8TAYNdefpJXLVID6vGiZyOck3vaLUILb8oFNGOd8VtZeNjKGbArVJk31IOsCAb1fjWgj7QsXpJz%2Bf4ma9v0Iuc4YwsLKbvQY6pgHJUYVAgDFTgEE7qlxo287qTPI%2Bm9RFky4KAItNf2WvtR3whcCqdvyAryRCUNm%2BArB%2BKAhRFHWb4RiIROzYftp7%2FKTLX5Th%2BOGzCaascohUekVLZlMwPYdktbee%2FiT%2Bd%2BRI2LYrS6J5upkISdMKHotKEj4HNqOFBMNvtGmEmZtgBsQUxDkANE8UaxiGra224CaZdilKF5WKguoQZugjsNzLWtv1IHg1&X-Amz-Signature=4f3c77b225ce09f880de67579df3216c2bc3efd9fc21cbeaf12826f0ad694a31&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXWFLMBO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCH%2BOdrevyeWpynmwsRaEjU9mKAFrvGDxTANcHwlgjNPwIhANBzp81CFYe7izT5FNyGomS%2BxJYmVhNSCA8B8PRIvkDSKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZt701Pi81ByibgsUq3AMoBWbs462eQbtOeyTBBgNVUACCHu26J8Sf%2FO3CaKPueWzJ2wVPYDVvqCE%2F5ZFy2T7C%2BPD1rXGGXekKyzDIRy1v%2B%2BXVfH4AguvZou1OKnvrOCNr9V97F6%2Bq63swYfl0tvEdKQL9nT0nmO82EVSuHN8dUHdlQlqExWhLypInf0pVIUZDb29YfBtqlfvz5fDJaQKtZRh1FFuAJ8NemMBy773AGYVLHYZC19orsRNPINQq86u3Vgf%2FHU%2FlJuf7t9EDZluIK1f8CFW%2F7NUNlPk9D0uiYJJP7cxCINi0%2FfcrZbh49mZzHg80rQAO%2FhMDzCHHSWo1RqOsyZV5NZLe6G1991nKmApjokQtEg2HUZcV%2FmnCn1KNKltj%2FuUOiR7eG6b%2B%2FSK6WJTY586ecchqXapLWOyMeeq7mCYFoLCocAzuTxvRmTD5b%2FLRHO6yraWyNytjWanKx4Lh5DT8wDiuDXDMNMEXd8PBk%2FtGq2ILuqStHTcgVxWfVvxX0ckXGF6lBxBB6Ypc3TFHKNS9cF9YnnyvPwMxAiFxb5YeZziHwOtWs0%2BkjsiiQqmzYSSdaomPn8MjSUI1%2F2mPtPPmZ8QRlwM0daM%2F9vO2Mc%2FwWxAldJvzV7kc5cHaU%2BCLrRBn4FIFNjCxspu9BjqkAU7H8pGIgv2z8Yfr7pn8uNKAQlsuVFOjwHFC1CdIbW2BvfPUJYQ2mIKY4H%2FP8IMQBITJxPxZH5U%2F0IInuEE1%2F5yAek27DX4arRPt4q7XOItWB9hkLpsDbQO%2FhI0nGDmWvJPJPq16dIwS2K%2BMw9duyzdaVLP1SWDoU%2FHuYw%2F3nHzy0UM91O92%2Fxspop7OYYJlm2cN5PLhsLfyyliDYw%2FbmJDJFjjC&X-Amz-Signature=b0af9676601d62ad0b9d4fbe698372dd3e88f27aed8c54cf3ca1a6ecbdf06adf&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXWFLMBO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCH%2BOdrevyeWpynmwsRaEjU9mKAFrvGDxTANcHwlgjNPwIhANBzp81CFYe7izT5FNyGomS%2BxJYmVhNSCA8B8PRIvkDSKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZt701Pi81ByibgsUq3AMoBWbs462eQbtOeyTBBgNVUACCHu26J8Sf%2FO3CaKPueWzJ2wVPYDVvqCE%2F5ZFy2T7C%2BPD1rXGGXekKyzDIRy1v%2B%2BXVfH4AguvZou1OKnvrOCNr9V97F6%2Bq63swYfl0tvEdKQL9nT0nmO82EVSuHN8dUHdlQlqExWhLypInf0pVIUZDb29YfBtqlfvz5fDJaQKtZRh1FFuAJ8NemMBy773AGYVLHYZC19orsRNPINQq86u3Vgf%2FHU%2FlJuf7t9EDZluIK1f8CFW%2F7NUNlPk9D0uiYJJP7cxCINi0%2FfcrZbh49mZzHg80rQAO%2FhMDzCHHSWo1RqOsyZV5NZLe6G1991nKmApjokQtEg2HUZcV%2FmnCn1KNKltj%2FuUOiR7eG6b%2B%2FSK6WJTY586ecchqXapLWOyMeeq7mCYFoLCocAzuTxvRmTD5b%2FLRHO6yraWyNytjWanKx4Lh5DT8wDiuDXDMNMEXd8PBk%2FtGq2ILuqStHTcgVxWfVvxX0ckXGF6lBxBB6Ypc3TFHKNS9cF9YnnyvPwMxAiFxb5YeZziHwOtWs0%2BkjsiiQqmzYSSdaomPn8MjSUI1%2F2mPtPPmZ8QRlwM0daM%2F9vO2Mc%2FwWxAldJvzV7kc5cHaU%2BCLrRBn4FIFNjCxspu9BjqkAU7H8pGIgv2z8Yfr7pn8uNKAQlsuVFOjwHFC1CdIbW2BvfPUJYQ2mIKY4H%2FP8IMQBITJxPxZH5U%2F0IInuEE1%2F5yAek27DX4arRPt4q7XOItWB9hkLpsDbQO%2FhI0nGDmWvJPJPq16dIwS2K%2BMw9duyzdaVLP1SWDoU%2FHuYw%2F3nHzy0UM91O92%2Fxspop7OYYJlm2cN5PLhsLfyyliDYw%2FbmJDJFjjC&X-Amz-Signature=fa8c97a535ec1809f2f03f16050cbc309c31f0e76226960fbe174b387a5fd119&X-Amz-SignedHeaders=host&x-id=GetObject)

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
