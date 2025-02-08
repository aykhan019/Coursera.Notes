

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFHUPX3U%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIFBC6Fbx7i7%2FLH4Mq6ilpdMZakgVFz2SkVTHDhQYRWGgAiBJVjRmMWDr7Db5fLQrqy82VIOtQYGBRr%2BuhMVICiWNAyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMabZimvGox%2Bh0mLRkKtwDofT8NGAcXhBlcCmRbFRgJTb90WiyOWHPamOyUr3GDgZefRSiYYVkZYe9QpJT%2FJUiTxL9Y1bTmdN2OkfrYx8%2B5WMbTkGsA5HUDCHDVM826b8Sv2nOvvs%2Fa6tWW8FwMtTEi691qERvrPGf9P%2ByVTWKLOk3cAR6FeL680UtTVaK3EuDud26cEk6ST6TVGj6zoCl%2BOTxFDd9xXrdEQKnlwJS6IhVWGznIsY3bIyHtqzDOWqqKyXWX4gjdPudpl83Qfe9BsqrE33%2FfZqI4khduuvdkxirZHokCtqZiVO6kfvbwSwtHHqXNCRsyCe6fymqSzqc0Ltg3jYe%2FsyndmdWpA6zJzig%2B1htMXoc%2FD2NMeuyMTJ%2B19%2Fo8acxv4ofG31vfasd80Fdgo2IrkrQPluDRyzj%2BtdjsG5cWHdQtbMWxD1h1qhTFMUOHXjUh%2BdudsqHme%2BcCFKgPBCN25ECxqKacrdZbdI2WgCWtpiR0cBAmEHtHVbXAdskWNv9U3bTwySqO2sOnV4IAmjZPsNXurKmJ6LfCfbAZ8KNiLzspmTu%2B4CWnicBthEMZhMReb56HFcM5MBBpx3IqNis35plgnMhYux9bzOrotnZD2iDMd8jR2hoiaAH3xvQlsOK15CHisUw9I2cvQY6pgEDAHsi9J7zVKli7q8k%2F0CvbfB%2BIrNDk%2BUR1DdlApEV6SnDEPF%2FVQVj7aCpivUb1BrsgbXxBrBXwOY%2FJS6cxX993%2BGYtG4OY7cdknYkt935RmaJXci9a79v9bkaqdFSWlZ3fWuNEyNk%2BMtZ5J9ii13KtBuVLK0FxjJekAwOfW%2BKSt968qIHVHfZiVDtJucOsXt10X4XrFLvM3RJS2FLA69DY5Id7kbe&X-Amz-Signature=d878d5f4eee66786780f07ff04e24bd044e36d2610f0d880fd094ebd123eb255&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFHUPX3U%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIFBC6Fbx7i7%2FLH4Mq6ilpdMZakgVFz2SkVTHDhQYRWGgAiBJVjRmMWDr7Db5fLQrqy82VIOtQYGBRr%2BuhMVICiWNAyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMabZimvGox%2Bh0mLRkKtwDofT8NGAcXhBlcCmRbFRgJTb90WiyOWHPamOyUr3GDgZefRSiYYVkZYe9QpJT%2FJUiTxL9Y1bTmdN2OkfrYx8%2B5WMbTkGsA5HUDCHDVM826b8Sv2nOvvs%2Fa6tWW8FwMtTEi691qERvrPGf9P%2ByVTWKLOk3cAR6FeL680UtTVaK3EuDud26cEk6ST6TVGj6zoCl%2BOTxFDd9xXrdEQKnlwJS6IhVWGznIsY3bIyHtqzDOWqqKyXWX4gjdPudpl83Qfe9BsqrE33%2FfZqI4khduuvdkxirZHokCtqZiVO6kfvbwSwtHHqXNCRsyCe6fymqSzqc0Ltg3jYe%2FsyndmdWpA6zJzig%2B1htMXoc%2FD2NMeuyMTJ%2B19%2Fo8acxv4ofG31vfasd80Fdgo2IrkrQPluDRyzj%2BtdjsG5cWHdQtbMWxD1h1qhTFMUOHXjUh%2BdudsqHme%2BcCFKgPBCN25ECxqKacrdZbdI2WgCWtpiR0cBAmEHtHVbXAdskWNv9U3bTwySqO2sOnV4IAmjZPsNXurKmJ6LfCfbAZ8KNiLzspmTu%2B4CWnicBthEMZhMReb56HFcM5MBBpx3IqNis35plgnMhYux9bzOrotnZD2iDMd8jR2hoiaAH3xvQlsOK15CHisUw9I2cvQY6pgEDAHsi9J7zVKli7q8k%2F0CvbfB%2BIrNDk%2BUR1DdlApEV6SnDEPF%2FVQVj7aCpivUb1BrsgbXxBrBXwOY%2FJS6cxX993%2BGYtG4OY7cdknYkt935RmaJXci9a79v9bkaqdFSWlZ3fWuNEyNk%2BMtZ5J9ii13KtBuVLK0FxjJekAwOfW%2BKSt968qIHVHfZiVDtJucOsXt10X4XrFLvM3RJS2FLA69DY5Id7kbe&X-Amz-Signature=1745b24f6499c471edbd71de0123571d65d112eeb73efd66d988042ccebcc261&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFHUPX3U%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIFBC6Fbx7i7%2FLH4Mq6ilpdMZakgVFz2SkVTHDhQYRWGgAiBJVjRmMWDr7Db5fLQrqy82VIOtQYGBRr%2BuhMVICiWNAyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMabZimvGox%2Bh0mLRkKtwDofT8NGAcXhBlcCmRbFRgJTb90WiyOWHPamOyUr3GDgZefRSiYYVkZYe9QpJT%2FJUiTxL9Y1bTmdN2OkfrYx8%2B5WMbTkGsA5HUDCHDVM826b8Sv2nOvvs%2Fa6tWW8FwMtTEi691qERvrPGf9P%2ByVTWKLOk3cAR6FeL680UtTVaK3EuDud26cEk6ST6TVGj6zoCl%2BOTxFDd9xXrdEQKnlwJS6IhVWGznIsY3bIyHtqzDOWqqKyXWX4gjdPudpl83Qfe9BsqrE33%2FfZqI4khduuvdkxirZHokCtqZiVO6kfvbwSwtHHqXNCRsyCe6fymqSzqc0Ltg3jYe%2FsyndmdWpA6zJzig%2B1htMXoc%2FD2NMeuyMTJ%2B19%2Fo8acxv4ofG31vfasd80Fdgo2IrkrQPluDRyzj%2BtdjsG5cWHdQtbMWxD1h1qhTFMUOHXjUh%2BdudsqHme%2BcCFKgPBCN25ECxqKacrdZbdI2WgCWtpiR0cBAmEHtHVbXAdskWNv9U3bTwySqO2sOnV4IAmjZPsNXurKmJ6LfCfbAZ8KNiLzspmTu%2B4CWnicBthEMZhMReb56HFcM5MBBpx3IqNis35plgnMhYux9bzOrotnZD2iDMd8jR2hoiaAH3xvQlsOK15CHisUw9I2cvQY6pgEDAHsi9J7zVKli7q8k%2F0CvbfB%2BIrNDk%2BUR1DdlApEV6SnDEPF%2FVQVj7aCpivUb1BrsgbXxBrBXwOY%2FJS6cxX993%2BGYtG4OY7cdknYkt935RmaJXci9a79v9bkaqdFSWlZ3fWuNEyNk%2BMtZ5J9ii13KtBuVLK0FxjJekAwOfW%2BKSt968qIHVHfZiVDtJucOsXt10X4XrFLvM3RJS2FLA69DY5Id7kbe&X-Amz-Signature=4f49c6699277125484e13762c26c536e583bf50fecf71d769b6d6435f519ec93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5KR2VHL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE9V4KMT8DrcQblW26KGO3dAc5NCNlW8AnZft6pk7%2BEKAiEAhgQbYKBcfiPB%2FUrKuHYkUZkErbkXAlhXEzVqX2vu3gUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdXlmtSp8HTFiBtcSrcA0jbIG6uUY7TsD24U6NXOkrhgIRmrZwD9twX5CWtppnYQopmZt9608bK2024OBQSowMwYmBxWcqjzHFjENDWt3nRdmswYY7nx%2Fbe2hwQRPwsNGTQtIUf2SCUa668Iytgr01vVC7lrCm62mMHKjBryYOJ7I%2FG8RGi5fn8sDLMIL2BHh1nfrLtrqsqbGc38crH%2BtkVGC9FP9peGgBsqmQhA0uuz2Z5zhBqHM8AwwnzYpXH6%2Fh8nNH77wiX%2Bh%2F%2Fi8IdYcMHRs6zma%2FKN3R7nR%2B4GeqW5WsGVCaVNtlZADIZvHHyYrS9aAhwRZaHrIIFx9SZlUbXjS6HGNutCmFrWIasEiYzIVqBLW9%2FShYaM0a5%2BJodsu87%2BvsNowMo2aFfVJEGip98pW%2FMDHmVLdXNrrP%2FMw1w4%2Bjx%2FLOGCh1tyoAr1O7SUTuS%2FdyYJgD%2Be4A72kkpcCaUbb24f%2BBPdbdci7uQCJGkR29W6Ze5OdeQ8MsUIai1RT7CyRHYbBhjIYYIh8eLpOOJmoWQ%2BXY3N%2FK6YQXaVFaX5zgPNrcLRtvyDbT33MVHefuFxHp8xfPMnge%2FbhogR6PV1kjE2W%2Far3kziGg4%2BFPTXMUDsMNGIKmgPInktOOAowroaKe4voaAgMdeMO2NnL0GOqUBgvj89JxpXkQUtEsZ8tvtnE98I1hhxsc2e4GJGx1DZcm9loaXTzWACjzEYIDzfwWjBMxvr73J1hHF7CqUGV3zpVFWXTkXPYyyoGShHeeHPSQE1YUzQAjNIZSs9YN5vAoMW4pbQFoWBDovcWV31o%2BXnBpVgXug4Gm16O4vzcc9x0IMOtWkRhjMZSWV52kCVJl0x3LunRnOvLpm8194Jwnqs%2FM8Hrpa&X-Amz-Signature=d84752e74f5ae5a6815d9bab07b63f1d0833935a926d0b247c6051d593bd4594&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5KR2VHL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE9V4KMT8DrcQblW26KGO3dAc5NCNlW8AnZft6pk7%2BEKAiEAhgQbYKBcfiPB%2FUrKuHYkUZkErbkXAlhXEzVqX2vu3gUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdXlmtSp8HTFiBtcSrcA0jbIG6uUY7TsD24U6NXOkrhgIRmrZwD9twX5CWtppnYQopmZt9608bK2024OBQSowMwYmBxWcqjzHFjENDWt3nRdmswYY7nx%2Fbe2hwQRPwsNGTQtIUf2SCUa668Iytgr01vVC7lrCm62mMHKjBryYOJ7I%2FG8RGi5fn8sDLMIL2BHh1nfrLtrqsqbGc38crH%2BtkVGC9FP9peGgBsqmQhA0uuz2Z5zhBqHM8AwwnzYpXH6%2Fh8nNH77wiX%2Bh%2F%2Fi8IdYcMHRs6zma%2FKN3R7nR%2B4GeqW5WsGVCaVNtlZADIZvHHyYrS9aAhwRZaHrIIFx9SZlUbXjS6HGNutCmFrWIasEiYzIVqBLW9%2FShYaM0a5%2BJodsu87%2BvsNowMo2aFfVJEGip98pW%2FMDHmVLdXNrrP%2FMw1w4%2Bjx%2FLOGCh1tyoAr1O7SUTuS%2FdyYJgD%2Be4A72kkpcCaUbb24f%2BBPdbdci7uQCJGkR29W6Ze5OdeQ8MsUIai1RT7CyRHYbBhjIYYIh8eLpOOJmoWQ%2BXY3N%2FK6YQXaVFaX5zgPNrcLRtvyDbT33MVHefuFxHp8xfPMnge%2FbhogR6PV1kjE2W%2Far3kziGg4%2BFPTXMUDsMNGIKmgPInktOOAowroaKe4voaAgMdeMO2NnL0GOqUBgvj89JxpXkQUtEsZ8tvtnE98I1hhxsc2e4GJGx1DZcm9loaXTzWACjzEYIDzfwWjBMxvr73J1hHF7CqUGV3zpVFWXTkXPYyyoGShHeeHPSQE1YUzQAjNIZSs9YN5vAoMW4pbQFoWBDovcWV31o%2BXnBpVgXug4Gm16O4vzcc9x0IMOtWkRhjMZSWV52kCVJl0x3LunRnOvLpm8194Jwnqs%2FM8Hrpa&X-Amz-Signature=17fa93b447aa4a09ba717bb14a236bdfb32c69f4bed185a8bd5c7b78278d0da3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5KR2VHL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE9V4KMT8DrcQblW26KGO3dAc5NCNlW8AnZft6pk7%2BEKAiEAhgQbYKBcfiPB%2FUrKuHYkUZkErbkXAlhXEzVqX2vu3gUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdXlmtSp8HTFiBtcSrcA0jbIG6uUY7TsD24U6NXOkrhgIRmrZwD9twX5CWtppnYQopmZt9608bK2024OBQSowMwYmBxWcqjzHFjENDWt3nRdmswYY7nx%2Fbe2hwQRPwsNGTQtIUf2SCUa668Iytgr01vVC7lrCm62mMHKjBryYOJ7I%2FG8RGi5fn8sDLMIL2BHh1nfrLtrqsqbGc38crH%2BtkVGC9FP9peGgBsqmQhA0uuz2Z5zhBqHM8AwwnzYpXH6%2Fh8nNH77wiX%2Bh%2F%2Fi8IdYcMHRs6zma%2FKN3R7nR%2B4GeqW5WsGVCaVNtlZADIZvHHyYrS9aAhwRZaHrIIFx9SZlUbXjS6HGNutCmFrWIasEiYzIVqBLW9%2FShYaM0a5%2BJodsu87%2BvsNowMo2aFfVJEGip98pW%2FMDHmVLdXNrrP%2FMw1w4%2Bjx%2FLOGCh1tyoAr1O7SUTuS%2FdyYJgD%2Be4A72kkpcCaUbb24f%2BBPdbdci7uQCJGkR29W6Ze5OdeQ8MsUIai1RT7CyRHYbBhjIYYIh8eLpOOJmoWQ%2BXY3N%2FK6YQXaVFaX5zgPNrcLRtvyDbT33MVHefuFxHp8xfPMnge%2FbhogR6PV1kjE2W%2Far3kziGg4%2BFPTXMUDsMNGIKmgPInktOOAowroaKe4voaAgMdeMO2NnL0GOqUBgvj89JxpXkQUtEsZ8tvtnE98I1hhxsc2e4GJGx1DZcm9loaXTzWACjzEYIDzfwWjBMxvr73J1hHF7CqUGV3zpVFWXTkXPYyyoGShHeeHPSQE1YUzQAjNIZSs9YN5vAoMW4pbQFoWBDovcWV31o%2BXnBpVgXug4Gm16O4vzcc9x0IMOtWkRhjMZSWV52kCVJl0x3LunRnOvLpm8194Jwnqs%2FM8Hrpa&X-Amz-Signature=850afde540c8f2fc1684d5346d122668090a3fdf53f4ed205eb604e50d969146&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5KR2VHL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE9V4KMT8DrcQblW26KGO3dAc5NCNlW8AnZft6pk7%2BEKAiEAhgQbYKBcfiPB%2FUrKuHYkUZkErbkXAlhXEzVqX2vu3gUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdXlmtSp8HTFiBtcSrcA0jbIG6uUY7TsD24U6NXOkrhgIRmrZwD9twX5CWtppnYQopmZt9608bK2024OBQSowMwYmBxWcqjzHFjENDWt3nRdmswYY7nx%2Fbe2hwQRPwsNGTQtIUf2SCUa668Iytgr01vVC7lrCm62mMHKjBryYOJ7I%2FG8RGi5fn8sDLMIL2BHh1nfrLtrqsqbGc38crH%2BtkVGC9FP9peGgBsqmQhA0uuz2Z5zhBqHM8AwwnzYpXH6%2Fh8nNH77wiX%2Bh%2F%2Fi8IdYcMHRs6zma%2FKN3R7nR%2B4GeqW5WsGVCaVNtlZADIZvHHyYrS9aAhwRZaHrIIFx9SZlUbXjS6HGNutCmFrWIasEiYzIVqBLW9%2FShYaM0a5%2BJodsu87%2BvsNowMo2aFfVJEGip98pW%2FMDHmVLdXNrrP%2FMw1w4%2Bjx%2FLOGCh1tyoAr1O7SUTuS%2FdyYJgD%2Be4A72kkpcCaUbb24f%2BBPdbdci7uQCJGkR29W6Ze5OdeQ8MsUIai1RT7CyRHYbBhjIYYIh8eLpOOJmoWQ%2BXY3N%2FK6YQXaVFaX5zgPNrcLRtvyDbT33MVHefuFxHp8xfPMnge%2FbhogR6PV1kjE2W%2Far3kziGg4%2BFPTXMUDsMNGIKmgPInktOOAowroaKe4voaAgMdeMO2NnL0GOqUBgvj89JxpXkQUtEsZ8tvtnE98I1hhxsc2e4GJGx1DZcm9loaXTzWACjzEYIDzfwWjBMxvr73J1hHF7CqUGV3zpVFWXTkXPYyyoGShHeeHPSQE1YUzQAjNIZSs9YN5vAoMW4pbQFoWBDovcWV31o%2BXnBpVgXug4Gm16O4vzcc9x0IMOtWkRhjMZSWV52kCVJl0x3LunRnOvLpm8194Jwnqs%2FM8Hrpa&X-Amz-Signature=29c5eee71d382faa05825ebdf99a6dbdb9023877a1cc15090d657337ccf9b77e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5KR2VHL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE9V4KMT8DrcQblW26KGO3dAc5NCNlW8AnZft6pk7%2BEKAiEAhgQbYKBcfiPB%2FUrKuHYkUZkErbkXAlhXEzVqX2vu3gUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdXlmtSp8HTFiBtcSrcA0jbIG6uUY7TsD24U6NXOkrhgIRmrZwD9twX5CWtppnYQopmZt9608bK2024OBQSowMwYmBxWcqjzHFjENDWt3nRdmswYY7nx%2Fbe2hwQRPwsNGTQtIUf2SCUa668Iytgr01vVC7lrCm62mMHKjBryYOJ7I%2FG8RGi5fn8sDLMIL2BHh1nfrLtrqsqbGc38crH%2BtkVGC9FP9peGgBsqmQhA0uuz2Z5zhBqHM8AwwnzYpXH6%2Fh8nNH77wiX%2Bh%2F%2Fi8IdYcMHRs6zma%2FKN3R7nR%2B4GeqW5WsGVCaVNtlZADIZvHHyYrS9aAhwRZaHrIIFx9SZlUbXjS6HGNutCmFrWIasEiYzIVqBLW9%2FShYaM0a5%2BJodsu87%2BvsNowMo2aFfVJEGip98pW%2FMDHmVLdXNrrP%2FMw1w4%2Bjx%2FLOGCh1tyoAr1O7SUTuS%2FdyYJgD%2Be4A72kkpcCaUbb24f%2BBPdbdci7uQCJGkR29W6Ze5OdeQ8MsUIai1RT7CyRHYbBhjIYYIh8eLpOOJmoWQ%2BXY3N%2FK6YQXaVFaX5zgPNrcLRtvyDbT33MVHefuFxHp8xfPMnge%2FbhogR6PV1kjE2W%2Far3kziGg4%2BFPTXMUDsMNGIKmgPInktOOAowroaKe4voaAgMdeMO2NnL0GOqUBgvj89JxpXkQUtEsZ8tvtnE98I1hhxsc2e4GJGx1DZcm9loaXTzWACjzEYIDzfwWjBMxvr73J1hHF7CqUGV3zpVFWXTkXPYyyoGShHeeHPSQE1YUzQAjNIZSs9YN5vAoMW4pbQFoWBDovcWV31o%2BXnBpVgXug4Gm16O4vzcc9x0IMOtWkRhjMZSWV52kCVJl0x3LunRnOvLpm8194Jwnqs%2FM8Hrpa&X-Amz-Signature=d7b62d80bd5455e0d3ddbc3a6559b2ae14dc5d7a3bf41ab725b812bfa03fe41b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5KR2VHL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE9V4KMT8DrcQblW26KGO3dAc5NCNlW8AnZft6pk7%2BEKAiEAhgQbYKBcfiPB%2FUrKuHYkUZkErbkXAlhXEzVqX2vu3gUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdXlmtSp8HTFiBtcSrcA0jbIG6uUY7TsD24U6NXOkrhgIRmrZwD9twX5CWtppnYQopmZt9608bK2024OBQSowMwYmBxWcqjzHFjENDWt3nRdmswYY7nx%2Fbe2hwQRPwsNGTQtIUf2SCUa668Iytgr01vVC7lrCm62mMHKjBryYOJ7I%2FG8RGi5fn8sDLMIL2BHh1nfrLtrqsqbGc38crH%2BtkVGC9FP9peGgBsqmQhA0uuz2Z5zhBqHM8AwwnzYpXH6%2Fh8nNH77wiX%2Bh%2F%2Fi8IdYcMHRs6zma%2FKN3R7nR%2B4GeqW5WsGVCaVNtlZADIZvHHyYrS9aAhwRZaHrIIFx9SZlUbXjS6HGNutCmFrWIasEiYzIVqBLW9%2FShYaM0a5%2BJodsu87%2BvsNowMo2aFfVJEGip98pW%2FMDHmVLdXNrrP%2FMw1w4%2Bjx%2FLOGCh1tyoAr1O7SUTuS%2FdyYJgD%2Be4A72kkpcCaUbb24f%2BBPdbdci7uQCJGkR29W6Ze5OdeQ8MsUIai1RT7CyRHYbBhjIYYIh8eLpOOJmoWQ%2BXY3N%2FK6YQXaVFaX5zgPNrcLRtvyDbT33MVHefuFxHp8xfPMnge%2FbhogR6PV1kjE2W%2Far3kziGg4%2BFPTXMUDsMNGIKmgPInktOOAowroaKe4voaAgMdeMO2NnL0GOqUBgvj89JxpXkQUtEsZ8tvtnE98I1hhxsc2e4GJGx1DZcm9loaXTzWACjzEYIDzfwWjBMxvr73J1hHF7CqUGV3zpVFWXTkXPYyyoGShHeeHPSQE1YUzQAjNIZSs9YN5vAoMW4pbQFoWBDovcWV31o%2BXnBpVgXug4Gm16O4vzcc9x0IMOtWkRhjMZSWV52kCVJl0x3LunRnOvLpm8194Jwnqs%2FM8Hrpa&X-Amz-Signature=b695937d31558d78e5022c1d97f63c4730b9ad2acff67a00a7276700d568cea8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YKMUAY3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIDratziFf2%2F9JQlnmkvooy8o%2FAWUF1Bz50D8hqzbR%2BYdAiB%2BbivkO0cjtj9dXTEGbjG0OsaPWu32QZFfOuIAWCCidyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGsS1VLhzN4pjc%2B%2BiKtwDcyEGLWj1e6TYwnacaZlSh6CaVqScP5ymKVTZSOjSkbT7Jk20ezik6TN3MACE%2B3Ava%2FQCGB6cuhbEr037dRFCAdWlPkE0gUuMWPe9H6MK%2FItenTI0DTN4wVcQibVw64AfGRLVqx8zJj9RfnJ06JOKyDB%2FQBh9mfX0l1POc54Fbuq7FpvGDo%2B1CpFtczLiKmG9xYRx05dB0ndjlCvl%2FIj4RLInAkh8oQ2OVaAX%2FzO0TgMviYkJ1hCGL1nhLJcd9hzEFg%2FoTxz4cErHVhUAGSYFULo71V%2Fg4SqSHj%2But1IXQBVEvTLHZ0Ca%2FJOcXeygmml9We31vwyivaAfXGHFg36mZXPZ11dZAIoG1lzF9Qeb0CKjySPydygfFDge%2BAxLu%2B3LD%2FtSxG%2BIz2eHCUMzZPA11C8xFKD1vGRKr9EIpGHw8CC1Hl21ENf1uEbEqws35Fnna9t5QARBy8DbKuhnXHMf8F6q7yc1%2BQzneMbWYrEEbS4vP4zQSml6tjUtYjwERW1iu4zinJ6H4lVnjMgAonZP3HTMYsXh9%2BZY%2BNhGr8nVmmj7B901f5XELUMAccyiXypAOWmZwVoEJNBpRangB42xE1v1uLwg8csc2vg9hXQ3lJmRTXmh2BnWuHZXVvUw7Y2cvQY6pgHqBPqppPE1i3sAbJm5cqSBb93qJh5MvTrdsgS9J%2Bo%2Bvw2GxDMTaRoMetlyrUESXQqQyFWOQbjk0EzQs6c0AA%2BEdECXKPXWv5IQVfD8d27SH3jFgpeA7MurmY17qGI9qD%2FzOZH62qx9%2Bx0ba8gf3mvDfj0ymh3FB812phh2vT%2FPQmHFxRe6k%2Fma90KNL46Ucov4fJOGROvMFcM3t4wNaH%2FvSJzu%2F%2Fli&X-Amz-Signature=330cbc93de58964fcfa9d6fa9bae73db8b4444536fb7f4f7251dbc04f5d66b8f&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOYRRDX4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDLNqw3uvZJdw6HGFEVlh0E9IRVuyFu%2BC3piVOMKEL%2FqQIgL9b%2BpmYeTM6ppTdmALC43CK%2FgFn1AgT5drJF0msmtJ0qiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPPr2xp8613ZrtLAaCrcA%2FVBY%2F8BwsCHhBHpGpW2nje2vlS%2BUTlr4qvfKlMLFJLdamzP664YPxLJcJsHugp%2FoHqSqTMTz%2BiS9Ll9J7le57kjW7wm9T8nmUTGpMXrDMxqQW4nJrIlZUVYHgboZCg%2B6dyKxTTK3xWanbK56u8i%2BpkM5ft3rrlIw8naO29gZHtOUT5jK95eLBehKx9kZ5g3vOT7Oh1QnTxzq9X6iCgwqNNIGLg8IqxfMqkJeMO6jKnmO%2BfMUWrNJ%2FcSRIzJt%2B5eAtIKtk7epMAm6%2BMDjqRYSbZG%2BZ3iwfyb0%2BTpkyFKFMUnhYw%2F2bszPm3DrKx2W%2Blh%2BgzaiDk80o8Cysi2cRSWtAvEp3t6ABJDZMc98tb1Dz5snSWLwOmsbW3VWK0%2B3bnewWDc%2FWJVHa0DtDnQFgub6Nrrw22G5ox8qj0KAVjwEUtPSHLbNWaeSxsRHmEFxgu1p1IOCbse6tEy%2FB2b%2BQgYWeDn0G3MqCbYANiu6%2FKO5rHZdx2RHaItIBDDZSohKPiU6utTO2fdeyw4nC5zV5WMFRG2h3S7Bh4QZcVrm6muTG200Ka0bgrofabyvdhyg9zkwjuDmBwwp9QQDkxcGcNDJEwJdGrmkADq1q8QQ6MB6g35JOe9Dv1EwBrH2JgQMO2NnL0GOqUB6P79J6qH51d4QCHg8wET9N5Bbnt%2Fs1LbOeY5wf2W9IR2t993O2IxN6bX%2FfHdwbSIE0T6iOlKuYAB9FYFxgk26FDPRo1pC98eBC8yJDjlXb%2Fd2axONxF8TNqWtOdiZMjP8sZ7I4eYrMTWez%2FIf7dhnZ76t5I%2FMuVYi07h2cROeXJn3HczXuRoNoiprr0y%2Fqu2oXrBy3rrhiIhxMXAe8F5vkhVJcvB&X-Amz-Signature=8db911a0564132889355dc5afea43b0cf177f9cf1e469dd812ce477001fed18b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5KR2VHL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE9V4KMT8DrcQblW26KGO3dAc5NCNlW8AnZft6pk7%2BEKAiEAhgQbYKBcfiPB%2FUrKuHYkUZkErbkXAlhXEzVqX2vu3gUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdXlmtSp8HTFiBtcSrcA0jbIG6uUY7TsD24U6NXOkrhgIRmrZwD9twX5CWtppnYQopmZt9608bK2024OBQSowMwYmBxWcqjzHFjENDWt3nRdmswYY7nx%2Fbe2hwQRPwsNGTQtIUf2SCUa668Iytgr01vVC7lrCm62mMHKjBryYOJ7I%2FG8RGi5fn8sDLMIL2BHh1nfrLtrqsqbGc38crH%2BtkVGC9FP9peGgBsqmQhA0uuz2Z5zhBqHM8AwwnzYpXH6%2Fh8nNH77wiX%2Bh%2F%2Fi8IdYcMHRs6zma%2FKN3R7nR%2B4GeqW5WsGVCaVNtlZADIZvHHyYrS9aAhwRZaHrIIFx9SZlUbXjS6HGNutCmFrWIasEiYzIVqBLW9%2FShYaM0a5%2BJodsu87%2BvsNowMo2aFfVJEGip98pW%2FMDHmVLdXNrrP%2FMw1w4%2Bjx%2FLOGCh1tyoAr1O7SUTuS%2FdyYJgD%2Be4A72kkpcCaUbb24f%2BBPdbdci7uQCJGkR29W6Ze5OdeQ8MsUIai1RT7CyRHYbBhjIYYIh8eLpOOJmoWQ%2BXY3N%2FK6YQXaVFaX5zgPNrcLRtvyDbT33MVHefuFxHp8xfPMnge%2FbhogR6PV1kjE2W%2Far3kziGg4%2BFPTXMUDsMNGIKmgPInktOOAowroaKe4voaAgMdeMO2NnL0GOqUBgvj89JxpXkQUtEsZ8tvtnE98I1hhxsc2e4GJGx1DZcm9loaXTzWACjzEYIDzfwWjBMxvr73J1hHF7CqUGV3zpVFWXTkXPYyyoGShHeeHPSQE1YUzQAjNIZSs9YN5vAoMW4pbQFoWBDovcWV31o%2BXnBpVgXug4Gm16O4vzcc9x0IMOtWkRhjMZSWV52kCVJl0x3LunRnOvLpm8194Jwnqs%2FM8Hrpa&X-Amz-Signature=2b833a43bd00e5d31c1a3ff98c5843c18ab1092af1b02da57dcf35977b49aa11&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5KR2VHL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE9V4KMT8DrcQblW26KGO3dAc5NCNlW8AnZft6pk7%2BEKAiEAhgQbYKBcfiPB%2FUrKuHYkUZkErbkXAlhXEzVqX2vu3gUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdXlmtSp8HTFiBtcSrcA0jbIG6uUY7TsD24U6NXOkrhgIRmrZwD9twX5CWtppnYQopmZt9608bK2024OBQSowMwYmBxWcqjzHFjENDWt3nRdmswYY7nx%2Fbe2hwQRPwsNGTQtIUf2SCUa668Iytgr01vVC7lrCm62mMHKjBryYOJ7I%2FG8RGi5fn8sDLMIL2BHh1nfrLtrqsqbGc38crH%2BtkVGC9FP9peGgBsqmQhA0uuz2Z5zhBqHM8AwwnzYpXH6%2Fh8nNH77wiX%2Bh%2F%2Fi8IdYcMHRs6zma%2FKN3R7nR%2B4GeqW5WsGVCaVNtlZADIZvHHyYrS9aAhwRZaHrIIFx9SZlUbXjS6HGNutCmFrWIasEiYzIVqBLW9%2FShYaM0a5%2BJodsu87%2BvsNowMo2aFfVJEGip98pW%2FMDHmVLdXNrrP%2FMw1w4%2Bjx%2FLOGCh1tyoAr1O7SUTuS%2FdyYJgD%2Be4A72kkpcCaUbb24f%2BBPdbdci7uQCJGkR29W6Ze5OdeQ8MsUIai1RT7CyRHYbBhjIYYIh8eLpOOJmoWQ%2BXY3N%2FK6YQXaVFaX5zgPNrcLRtvyDbT33MVHefuFxHp8xfPMnge%2FbhogR6PV1kjE2W%2Far3kziGg4%2BFPTXMUDsMNGIKmgPInktOOAowroaKe4voaAgMdeMO2NnL0GOqUBgvj89JxpXkQUtEsZ8tvtnE98I1hhxsc2e4GJGx1DZcm9loaXTzWACjzEYIDzfwWjBMxvr73J1hHF7CqUGV3zpVFWXTkXPYyyoGShHeeHPSQE1YUzQAjNIZSs9YN5vAoMW4pbQFoWBDovcWV31o%2BXnBpVgXug4Gm16O4vzcc9x0IMOtWkRhjMZSWV52kCVJl0x3LunRnOvLpm8194Jwnqs%2FM8Hrpa&X-Amz-Signature=8d2b568443d0468ef52107debbdb40ee3fc2b287e48ff83b6359139bac0601e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5KR2VHL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE9V4KMT8DrcQblW26KGO3dAc5NCNlW8AnZft6pk7%2BEKAiEAhgQbYKBcfiPB%2FUrKuHYkUZkErbkXAlhXEzVqX2vu3gUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdXlmtSp8HTFiBtcSrcA0jbIG6uUY7TsD24U6NXOkrhgIRmrZwD9twX5CWtppnYQopmZt9608bK2024OBQSowMwYmBxWcqjzHFjENDWt3nRdmswYY7nx%2Fbe2hwQRPwsNGTQtIUf2SCUa668Iytgr01vVC7lrCm62mMHKjBryYOJ7I%2FG8RGi5fn8sDLMIL2BHh1nfrLtrqsqbGc38crH%2BtkVGC9FP9peGgBsqmQhA0uuz2Z5zhBqHM8AwwnzYpXH6%2Fh8nNH77wiX%2Bh%2F%2Fi8IdYcMHRs6zma%2FKN3R7nR%2B4GeqW5WsGVCaVNtlZADIZvHHyYrS9aAhwRZaHrIIFx9SZlUbXjS6HGNutCmFrWIasEiYzIVqBLW9%2FShYaM0a5%2BJodsu87%2BvsNowMo2aFfVJEGip98pW%2FMDHmVLdXNrrP%2FMw1w4%2Bjx%2FLOGCh1tyoAr1O7SUTuS%2FdyYJgD%2Be4A72kkpcCaUbb24f%2BBPdbdci7uQCJGkR29W6Ze5OdeQ8MsUIai1RT7CyRHYbBhjIYYIh8eLpOOJmoWQ%2BXY3N%2FK6YQXaVFaX5zgPNrcLRtvyDbT33MVHefuFxHp8xfPMnge%2FbhogR6PV1kjE2W%2Far3kziGg4%2BFPTXMUDsMNGIKmgPInktOOAowroaKe4voaAgMdeMO2NnL0GOqUBgvj89JxpXkQUtEsZ8tvtnE98I1hhxsc2e4GJGx1DZcm9loaXTzWACjzEYIDzfwWjBMxvr73J1hHF7CqUGV3zpVFWXTkXPYyyoGShHeeHPSQE1YUzQAjNIZSs9YN5vAoMW4pbQFoWBDovcWV31o%2BXnBpVgXug4Gm16O4vzcc9x0IMOtWkRhjMZSWV52kCVJl0x3LunRnOvLpm8194Jwnqs%2FM8Hrpa&X-Amz-Signature=2515761a96cc6f022692a7f5b486dda6da4890d604a4bafc84a088b09ccd710f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663MO3YE5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIF0pG8DmSoEuhsgsVrs3cLh%2B81a8ta8rv%2FkNWv7aCZJ6AiB1ueNIQEQDAfHPxUInLji7U6SVdyfMI8%2BsB0YsRTtzbCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2c994y6pgPTPy4CGKtwDFSXknLZOoRIh2Z1sakCTZkhxi64Ojo2D3waJV9QIJc0BCT8Kn82SH7B%2BaJ3x%2BqCz%2FJPDv0MvbBQUbilCNJt99KrIULvMcKpkQyZ6CvBr0WFEpjDA%2BfHiMc4GiQIQw4mGAQNqiz5vZ%2Bc%2BgBAkM%2BYzzpu%2FIJqYKdGxbulzNr3ERa1O23YUFT0aRE4jVHvR3CBz9gt7gIm%2BH3Nk4zF6eKyfhhRgn%2B1y6wv6jFLR08KcR05u2fAdlOckTNDasF5A%2B2qMuEn5asotD80fJ0m3SQKfRJ7XshQh3Kyh4bC3FEbxvXxLnvuhfFVi3c1USiQV0GJUj%2FjY%2Fxzjt%2BeVD1UyaoSaLSmBTS42xGP0BO2QTRFICpmJPU6qXtn73PKQ%2BCGaSDkjIBVFYEMtO4G3aufvC7cpJOtGhH1uYDLTMTPGkeEdeEeEsuU%2FX4RV8FMmgh7BUbikbkOW%2Bay7ufKMI3yCEnmgTjYCKMVpZ8MYpp7cdlL6RXicOfiyN4Y2CwYjOoIgYYzSs04IqfuurODrR89yH14OWb0OOhISpPjDCb1yR9QwDZITSXwIWT8rP5JR326G0KsNE82ubM9s1viIceEvjllWMzpJpzmTEmtZ7a32fXec1bzYUYLbdDFp0Hghq9gwmI6cvQY6pgHr1YJLSgJ7bkveswq2w6S8F03LMr3kx9jwYqu3%2BOo7YnLZF730mpHxomlqWNBm%2B79hKYKfsPO7%2FwNgxkLiEJkEio0cfR3bkLWfT5SjeZp8Vh5skRtOn4hJAZmkRTDw9tDckP5hRrrhmGk%2FVu%2BEXhfp0EK0MytMLwEpCFvYDyHFbIVufLjGKeCzdHCYNJojHJO73Gv3GUoHmIrmK%2BOOv42CmOn82vHw&X-Amz-Signature=14e26cf954096f5272562d41a029c4e50d9263549f722cb8e8d0efe559645826&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UANYASI6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGyoMM7CkMgBSGhGjW9RiXbCo34dhd8hRlWKMWkbPTOZAiBSmcFpQqk7h1ANusWhYY1k04RHUO4EkaMxVcOzFlbIgSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNvuL%2FmUlAigM7g0eKtwD5LnIX71ahd%2B5qsuAhmlVLpSrXebq7pP4B%2BWVcgP6Aj9%2BZ78eJAo4SWePOku4VIaL%2Fc31I6oHKBU1mYw88eKQ4niYa%2B%2F61urpB1q2tLGuCHaJttBY4c8uvFCCG%2BcQb5%2B2F6Gk%2FKnze5WrC0Glo%2B6NiI2r%2BIstF6jiN6RlDHrdC9ElcWChgCHcEi4GtS5kTDh3jMziX8eP4QxFFX2zqhAOFAAkn%2BopdYDPudO8dMHw1gqntAcKFtzhVpQrfdMOCSedTkTz3iV1jGGiQjNbTpFzncgt2p%2F%2B2FjFEE3oauLEkcThPPMiIKYnKtGyv1qw3uN3vJpXwXHGjbGba6u%2BKwHgCTWDBiPzL009IsJ4%2Bklw4Iv9J0VaKXAo2XOb%2FwQXXcCzi22fUQdaMtmNy1J%2FgjJn08voUdcFug9Tiz6v%2Fj5Hrg4vfUh1v9SzLhYxzC%2BaSGY2RvR5ewd9VAqJBM6N2vV9pdJzrlJ%2BPJBw6hEtVhP%2FpDXx0To%2FzxzDCFstNubHEHahDDgzX7r8itTwnEzVHPiVnqf1PyGdMzPwhqm7%2BHcD3fNvvnP5yd5tLUqaIK4cAoHeDXWCLN03wEtM2KWUY%2BKb%2FPxJDOQRL6ZuEar8IE1sKo8w1uu6iEI3Fo5r6Isw1o6cvQY6pgFY0ZswAuiAr82dbR8vJjhe%2Bledhe8aNB5JrF9bhZnQ%2Fa%2FYtWz4wA8PYAre2x9dPasjORSJARWEiS%2BsiJ9mslpGqFrDjZ%2F1v5vPAmuSlQfSDNyILvLlMBOzax%2BP240MpNvNabho%2BR7sTIaJcTXZXKqx1cGjR7CusrpuWkpghaxiyAiGPQFtPuKZq%2B5UGpNHj3VlGEwRvYhwtkhep%2B5ZBirG0oD%2Bqcgk&X-Amz-Signature=20e1d63bbb852f59014ca15d06d0d84c495f0b70d399b2d27ddc4ff2aff0cd75&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5NKP2UM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDOriQmCguX4SQybIDRcNO77FjyB%2Bm6kaTqUlWxeGTUxgIgOqNCgS6vErTJ9NW11k5duwx52rcxHhaNNcusyGpZqagqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFb5nGjzR3I5AOrwyrcA6ZddVsIw3y0jlVLsow%2BiWXY20fDv%2FynT05TZZc3hilOMSMZzy2l5HG7P5klRzxOwpY1sCmSPs0YcdAsezRrwEmBp5cKlsChAix2ksYMPQahJSz32zakjsTUZon%2Fv%2FpeyswQUTH1A9DI2zTDlcd9dRIL7sezK%2FkHBUJt3hTaiYPWIm3kW4ceZfEABah%2B8ZGVtuyFuA5IBdc2mJ74smblCR2XBHgx%2Bz36ufvPT0gmyrCRaxNCaIVAPXrx22nXAFaDhiI3vrO7%2FwLowPWF0e7pLopA6cXaof%2Bm1owpcDAswAU5y0EcxwCmXAsbLIWL7brhrNEItOOzdwVJlNGoRP3sMfwgJPLyDu3fUHHgLhTWl%2BFySeXaYtnYNFiY6Nns0lUGGKDJmkW0LBtW2NXKPYjvRhAnjjahQYY7nPIa2fpvZBcKROusT%2BPKE13e%2F9qJ46heHU16TIp%2F7ylDDskMcdjbpyOzqmyUxM0GXi3NSh2gn0Fy5EVg8GYwxcMksQ2QnVlpNpOTM7LsvOtvEPzx%2F3WAQDqvMgi5k6BGgYDx%2FIP%2Bjkt9sLoHiDtLy6iB8C2XOgJ2mCwEHLpl6BKJlxGUWfVamoCqTteHwjzYECuIabIlxNmH3orcEB648Z4zcJvpMP6NnL0GOqUBI%2FCluqbe%2B5lcn3X%2FisFyJU0SiWh4IxScpGBTrtc33lxuFDrlJssfc%2F3aj7ms%2FRu6M1jSHKadSAX5JrmeEo166WYMJi%2Bz88jV0%2BLYI8eDtMvD8uiFoJjLlizkeBuAtFJcb1KZcYXrTzfyCOP0CHje%2BSO%2BhEhGwlM60q8qDk%2FeiKnhkqIzjOY6G1OZVv6mU6o6hFXaJbE4BQettWsm%2B1xxacDJ60dg&X-Amz-Signature=ffed0fc4efd0ab00e88feed2a7e2ce5924090871af474e15d0e7205107ff0513&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQQ42FZ3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCLeQeALUYWJvSNXRjtU1NtyEpkltyKklaayvwJ%2BWzpPQIgL1I6GFolx%2Bc%2FbfLB9IJhii3LhqNNruzYReQLQ3xVtC4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPchRMBZ4ulYnCR3hyrcA8NJKIEA0wRBoP7BqDZIskhlwStHNOQMwnCYdAXbMPADbW3oyecdzvsCEInA6ACqROweukWP7uzexGnrMzGfOayV%2Bfw7KJAfoeBKwb76TvnbxYFmY382UcNsX6uXuubnokZb%2Fy4qLt56TbusCWa3UDrSrc5vr260pMJi3gCDfVhNPqU5JaZZnHZxXOCa%2FEGcXLask92YFys%2FyFaMWEEwotmGLP%2ByTeS%2FhLtlGFIssW9QAlxWRy1O%2Fj0qX6%2BBLIEseXkbuoe%2FUcxqICfmjqhf2hTU7y2bVAM75tKvhoK4PpsuvefZGiqJl%2FDtd2m%2FzK%2Fz%2FGRiDRo3pL0nSET5Iwjp8Gjz1vy531C%2F1gfTeLO%2Flb1hlT7ZqY8THT9y%2Fo9gSxLtWElpxeH%2BBGBDxQnihT5q72vCwTAygVpUhokgZGH7fM3FzAxVRsPAitY8%2FHkeU6d0RiYKjFZYT%2B%2BYVBNEk0ysb8NCYL4HM01jjyKeJ%2FHT6DKvcx3H41igH%2Fj7h8ZFmEMtpzTLOg7BZ0PpdAkIdGz3eXcGE80CQJZDCPA5Y8%2FpOcZItXY87Jvne0WprcmaBHp8wsUtNLUV0qKTSO2b7WPa6zUWSPAAEz%2FsdN14XJoPWPL7qEJcXuF0RbupLq5TMKOOnL0GOqUBI9hZDvGOYChAnspkTIFAaRSwS%2BFWZMHn%2BlCewHx3NUITbpeK5GGZvv7%2BAjVbIOHJFHBH7KV3XEF69FphjXtGfIOqflhKYDn2x%2Bl3VyRJtZVEJius%2BHuMjx%2FzF0vVQZOmhU7J9oEWVQlW8Kvs1ElYeU9baBNlJVcaRFEFGFWPlIUdqE%2Busy%2BB2YD%2BXMKoMfUC%2BW6oudq3s2lcohKRX%2Fijar1nAKTH&X-Amz-Signature=083f110c3f45b4eb9e31b51c466c923a3453fefb3c397d81450c01d9048e9477&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQQ42FZ3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCLeQeALUYWJvSNXRjtU1NtyEpkltyKklaayvwJ%2BWzpPQIgL1I6GFolx%2Bc%2FbfLB9IJhii3LhqNNruzYReQLQ3xVtC4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPchRMBZ4ulYnCR3hyrcA8NJKIEA0wRBoP7BqDZIskhlwStHNOQMwnCYdAXbMPADbW3oyecdzvsCEInA6ACqROweukWP7uzexGnrMzGfOayV%2Bfw7KJAfoeBKwb76TvnbxYFmY382UcNsX6uXuubnokZb%2Fy4qLt56TbusCWa3UDrSrc5vr260pMJi3gCDfVhNPqU5JaZZnHZxXOCa%2FEGcXLask92YFys%2FyFaMWEEwotmGLP%2ByTeS%2FhLtlGFIssW9QAlxWRy1O%2Fj0qX6%2BBLIEseXkbuoe%2FUcxqICfmjqhf2hTU7y2bVAM75tKvhoK4PpsuvefZGiqJl%2FDtd2m%2FzK%2Fz%2FGRiDRo3pL0nSET5Iwjp8Gjz1vy531C%2F1gfTeLO%2Flb1hlT7ZqY8THT9y%2Fo9gSxLtWElpxeH%2BBGBDxQnihT5q72vCwTAygVpUhokgZGH7fM3FzAxVRsPAitY8%2FHkeU6d0RiYKjFZYT%2B%2BYVBNEk0ysb8NCYL4HM01jjyKeJ%2FHT6DKvcx3H41igH%2Fj7h8ZFmEMtpzTLOg7BZ0PpdAkIdGz3eXcGE80CQJZDCPA5Y8%2FpOcZItXY87Jvne0WprcmaBHp8wsUtNLUV0qKTSO2b7WPa6zUWSPAAEz%2FsdN14XJoPWPL7qEJcXuF0RbupLq5TMKOOnL0GOqUBI9hZDvGOYChAnspkTIFAaRSwS%2BFWZMHn%2BlCewHx3NUITbpeK5GGZvv7%2BAjVbIOHJFHBH7KV3XEF69FphjXtGfIOqflhKYDn2x%2Bl3VyRJtZVEJius%2BHuMjx%2FzF0vVQZOmhU7J9oEWVQlW8Kvs1ElYeU9baBNlJVcaRFEFGFWPlIUdqE%2Busy%2BB2YD%2BXMKoMfUC%2BW6oudq3s2lcohKRX%2Fijar1nAKTH&X-Amz-Signature=c8f8a35c2113872b6e172a6f47190043ebc730c87eb3221ee263061273b66fa9&X-Amz-SignedHeaders=host&x-id=GetObject)

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
