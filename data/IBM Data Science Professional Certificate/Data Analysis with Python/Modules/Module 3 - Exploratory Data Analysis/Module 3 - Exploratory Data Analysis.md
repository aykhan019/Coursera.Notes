

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM4PESTQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDF7kYXGGL5gfkMpSkwDNw3QXGBUJWTwEwlCXmuN475pAIhAK%2Fo0tvExKTk3ZA8JEs1IgSk7I9rr7qibWvvwtVjjpCsKv8DCEgQABoMNjM3NDIzMTgzODA1Igx7ymb4AN7YgTEsCMcq3AOkODJ58gDMfFkB8fbdi2E%2FFSXmW8pJf1IzkTMwWcHiOlY%2BPXlNtoOIt39aFtQa8GvWU57%2FovfXuDhA2IhtPC3fzJ7CJz4JH5qpbLRtNUdgpqYkppewd0oCkiSelkKB%2FIvly26XxioORcfT2LpMWC84G5n080WDvv2Mi2EJ90sHp2icKZqTItX0Xk8geIXvurrwV38EZkq6cHfD0AQ5fX5iwy9JNQ93iJC%2FUn0SfRzsz6aFP1CCdUq%2B9p%2BcXu%2BU%2BgYZa1lr18xH8TQ%2B4lHcWUTct3zONhcXSRXh9z9vbBvxxTGwBK3ydWUq%2BYanh%2BIAi9%2FmBCZzLuIxSXT1sld2%2F9uwkD2KxqgcozqxzgJtvEhbCqMcBzwqb62okVZple8ESCY7QNXI6XHhcp9l5365J1C86vsrsreE9wClbyJXWrwpqTCqrw0%2BmqDURvKBtNwisSuiPXQlxWWrH6%2BPFXcbMn%2B771fUR7S%2FD7HzbtfPFYGLJT5TqEgE7d%2B86xogF%2FGKwA%2FshZzn0i75Cozf7FOXYFZYS9CT5slUAsfULhlLp1nQ4v4wbdDR%2BJ7eEPGU%2FQKfIxSp2PRqJAuUpMx9EwsEWYz9WwfycdgLk987K1aUxCss43Mrcl1TKjgjTZrjTTDxgI69BjqkAbNWmHO8u8zskgP7V8FBll8UZuIOTxPRiMzGoqBKVd1cmDZcoyO3Hp%2BLIn%2B6MJ7fZtPgrqX98UWRWnhQ9%2BMsboPKXfvQCKxgdkSwXDPCC9gwAuuCQ0PQhHDBbUPyi%2Fe9WVKG7zGEVCMZyj%2ByQIvAoHI7Q09lJOmWUcbdIJq7h4DZ%2BsnqztZI2Tpvdp1DhoOiAEnbLcjezMPOOJwGGPtKC3MZMZ5w&X-Amz-Signature=bed546cde8ee9f7e9e95ef7fa7e593473e6680a40a95c8a042519ed399abe7a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM4PESTQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDF7kYXGGL5gfkMpSkwDNw3QXGBUJWTwEwlCXmuN475pAIhAK%2Fo0tvExKTk3ZA8JEs1IgSk7I9rr7qibWvvwtVjjpCsKv8DCEgQABoMNjM3NDIzMTgzODA1Igx7ymb4AN7YgTEsCMcq3AOkODJ58gDMfFkB8fbdi2E%2FFSXmW8pJf1IzkTMwWcHiOlY%2BPXlNtoOIt39aFtQa8GvWU57%2FovfXuDhA2IhtPC3fzJ7CJz4JH5qpbLRtNUdgpqYkppewd0oCkiSelkKB%2FIvly26XxioORcfT2LpMWC84G5n080WDvv2Mi2EJ90sHp2icKZqTItX0Xk8geIXvurrwV38EZkq6cHfD0AQ5fX5iwy9JNQ93iJC%2FUn0SfRzsz6aFP1CCdUq%2B9p%2BcXu%2BU%2BgYZa1lr18xH8TQ%2B4lHcWUTct3zONhcXSRXh9z9vbBvxxTGwBK3ydWUq%2BYanh%2BIAi9%2FmBCZzLuIxSXT1sld2%2F9uwkD2KxqgcozqxzgJtvEhbCqMcBzwqb62okVZple8ESCY7QNXI6XHhcp9l5365J1C86vsrsreE9wClbyJXWrwpqTCqrw0%2BmqDURvKBtNwisSuiPXQlxWWrH6%2BPFXcbMn%2B771fUR7S%2FD7HzbtfPFYGLJT5TqEgE7d%2B86xogF%2FGKwA%2FshZzn0i75Cozf7FOXYFZYS9CT5slUAsfULhlLp1nQ4v4wbdDR%2BJ7eEPGU%2FQKfIxSp2PRqJAuUpMx9EwsEWYz9WwfycdgLk987K1aUxCss43Mrcl1TKjgjTZrjTTDxgI69BjqkAbNWmHO8u8zskgP7V8FBll8UZuIOTxPRiMzGoqBKVd1cmDZcoyO3Hp%2BLIn%2B6MJ7fZtPgrqX98UWRWnhQ9%2BMsboPKXfvQCKxgdkSwXDPCC9gwAuuCQ0PQhHDBbUPyi%2Fe9WVKG7zGEVCMZyj%2ByQIvAoHI7Q09lJOmWUcbdIJq7h4DZ%2BsnqztZI2Tpvdp1DhoOiAEnbLcjezMPOOJwGGPtKC3MZMZ5w&X-Amz-Signature=dd8e479a613a63776616cfcd5df040c821c92d6594891fc4f6ab00ca729af1c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM4PESTQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDF7kYXGGL5gfkMpSkwDNw3QXGBUJWTwEwlCXmuN475pAIhAK%2Fo0tvExKTk3ZA8JEs1IgSk7I9rr7qibWvvwtVjjpCsKv8DCEgQABoMNjM3NDIzMTgzODA1Igx7ymb4AN7YgTEsCMcq3AOkODJ58gDMfFkB8fbdi2E%2FFSXmW8pJf1IzkTMwWcHiOlY%2BPXlNtoOIt39aFtQa8GvWU57%2FovfXuDhA2IhtPC3fzJ7CJz4JH5qpbLRtNUdgpqYkppewd0oCkiSelkKB%2FIvly26XxioORcfT2LpMWC84G5n080WDvv2Mi2EJ90sHp2icKZqTItX0Xk8geIXvurrwV38EZkq6cHfD0AQ5fX5iwy9JNQ93iJC%2FUn0SfRzsz6aFP1CCdUq%2B9p%2BcXu%2BU%2BgYZa1lr18xH8TQ%2B4lHcWUTct3zONhcXSRXh9z9vbBvxxTGwBK3ydWUq%2BYanh%2BIAi9%2FmBCZzLuIxSXT1sld2%2F9uwkD2KxqgcozqxzgJtvEhbCqMcBzwqb62okVZple8ESCY7QNXI6XHhcp9l5365J1C86vsrsreE9wClbyJXWrwpqTCqrw0%2BmqDURvKBtNwisSuiPXQlxWWrH6%2BPFXcbMn%2B771fUR7S%2FD7HzbtfPFYGLJT5TqEgE7d%2B86xogF%2FGKwA%2FshZzn0i75Cozf7FOXYFZYS9CT5slUAsfULhlLp1nQ4v4wbdDR%2BJ7eEPGU%2FQKfIxSp2PRqJAuUpMx9EwsEWYz9WwfycdgLk987K1aUxCss43Mrcl1TKjgjTZrjTTDxgI69BjqkAbNWmHO8u8zskgP7V8FBll8UZuIOTxPRiMzGoqBKVd1cmDZcoyO3Hp%2BLIn%2B6MJ7fZtPgrqX98UWRWnhQ9%2BMsboPKXfvQCKxgdkSwXDPCC9gwAuuCQ0PQhHDBbUPyi%2Fe9WVKG7zGEVCMZyj%2ByQIvAoHI7Q09lJOmWUcbdIJq7h4DZ%2BsnqztZI2Tpvdp1DhoOiAEnbLcjezMPOOJwGGPtKC3MZMZ5w&X-Amz-Signature=7ed61195f1812ad7ccddb34bc753e6b1508db41c9501b5316f1eae675fbccc46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7ZVW762%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC2%2BX41r6BSxRJDLQcHz%2B84u8oXWTlyunr5PXl1uEby%2BAIgXazQyjapxve%2B%2By%2F9HfgGACyi9oPfYx4gPRA53B68KAwq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCqp6mejKDvNMosEayrcA0pho3sy0yHhFG0T9LH%2BVZpgA8OhnMV454pL5vyvEUhwU7MMQnuB81ZH8Qj7DmOsqrE0CT5rDkj17I1pZl1AZjm%2Fj0js8aKhAawb1eYmv8nhr%2FXYLPA3CNOSQreDyhG%2FmQA6lhxwKho4BD9oHKNS3SIMXlHk5DyYzL5rN26KIQPWmVS7njCJEVGQ8MV3ypsEOLXZr0pShqZd1tPyGJmpINjtAWQFEW6mxR%2FlPhZLpY1K3zA0ATk9cbTOerihtQS4aBSYvcNlPzHwk8THadc8T6SGJ9WXBqQ5nmGzeCTh%2F7XOchWQKaEZqLnmLL4T9bo%2FONbIydnb402ADGduUhWTyd53V2m0wwGpX3a9iBEbTPLqUN5frp%2BepBOiYOmra4nihxOYlQ02taVwMqDIYSeRAQqpyuuESG9aaf1j9tVNzsmNL3oheDchNU%2BCJ9ddFZ7BW3G8cyl1XZZRXrG3Oq11xY8DahDOWZjRpLYlO2XmsUX8aex9ok49UeK65RwDgYKyHxpFjbdulQMuNYu5oBr5gnFSxx7gqvekhIXxJduLXxH5fQTedBreTvqTqIr6UkktlBdtzfyf7c8ZoJWBmRllXMX5sbiKZAD4R%2FGikOkrzlGHb%2F4AzK7vLraXUk%2FDMMuAjr0GOqUBh8oaaLFJ3Ld9vd%2FbXSr3ojzYRy2ukqXPgDvCL0y78I7leb0%2FS3Bi6p%2Fs93TyzsnHQQdh7%2B5ldwli064I3tJ9LRaxng26ydhYqtTyqZU53mZdwpv7cY%2B%2F2QPkybJqLpXqaR29Fo026VZkt8iSmbr6%2BF2dops2jNoCZ6s6g38qjbFTV7DESBJrW%2B%2F%2BPiZZhrjBh4IG%2FZF89AT5C6ohStJgOI05HIKr&X-Amz-Signature=996bbb89b5a4899c2a1aa4ca7e839b7bb150270e6da322594390c5f5ea20ee05&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7ZVW762%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC2%2BX41r6BSxRJDLQcHz%2B84u8oXWTlyunr5PXl1uEby%2BAIgXazQyjapxve%2B%2By%2F9HfgGACyi9oPfYx4gPRA53B68KAwq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCqp6mejKDvNMosEayrcA0pho3sy0yHhFG0T9LH%2BVZpgA8OhnMV454pL5vyvEUhwU7MMQnuB81ZH8Qj7DmOsqrE0CT5rDkj17I1pZl1AZjm%2Fj0js8aKhAawb1eYmv8nhr%2FXYLPA3CNOSQreDyhG%2FmQA6lhxwKho4BD9oHKNS3SIMXlHk5DyYzL5rN26KIQPWmVS7njCJEVGQ8MV3ypsEOLXZr0pShqZd1tPyGJmpINjtAWQFEW6mxR%2FlPhZLpY1K3zA0ATk9cbTOerihtQS4aBSYvcNlPzHwk8THadc8T6SGJ9WXBqQ5nmGzeCTh%2F7XOchWQKaEZqLnmLL4T9bo%2FONbIydnb402ADGduUhWTyd53V2m0wwGpX3a9iBEbTPLqUN5frp%2BepBOiYOmra4nihxOYlQ02taVwMqDIYSeRAQqpyuuESG9aaf1j9tVNzsmNL3oheDchNU%2BCJ9ddFZ7BW3G8cyl1XZZRXrG3Oq11xY8DahDOWZjRpLYlO2XmsUX8aex9ok49UeK65RwDgYKyHxpFjbdulQMuNYu5oBr5gnFSxx7gqvekhIXxJduLXxH5fQTedBreTvqTqIr6UkktlBdtzfyf7c8ZoJWBmRllXMX5sbiKZAD4R%2FGikOkrzlGHb%2F4AzK7vLraXUk%2FDMMuAjr0GOqUBh8oaaLFJ3Ld9vd%2FbXSr3ojzYRy2ukqXPgDvCL0y78I7leb0%2FS3Bi6p%2Fs93TyzsnHQQdh7%2B5ldwli064I3tJ9LRaxng26ydhYqtTyqZU53mZdwpv7cY%2B%2F2QPkybJqLpXqaR29Fo026VZkt8iSmbr6%2BF2dops2jNoCZ6s6g38qjbFTV7DESBJrW%2B%2F%2BPiZZhrjBh4IG%2FZF89AT5C6ohStJgOI05HIKr&X-Amz-Signature=f1b25e640ff3f31dc25d326653459300bd43ed37b4d22d6486973528a29af15c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7ZVW762%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC2%2BX41r6BSxRJDLQcHz%2B84u8oXWTlyunr5PXl1uEby%2BAIgXazQyjapxve%2B%2By%2F9HfgGACyi9oPfYx4gPRA53B68KAwq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCqp6mejKDvNMosEayrcA0pho3sy0yHhFG0T9LH%2BVZpgA8OhnMV454pL5vyvEUhwU7MMQnuB81ZH8Qj7DmOsqrE0CT5rDkj17I1pZl1AZjm%2Fj0js8aKhAawb1eYmv8nhr%2FXYLPA3CNOSQreDyhG%2FmQA6lhxwKho4BD9oHKNS3SIMXlHk5DyYzL5rN26KIQPWmVS7njCJEVGQ8MV3ypsEOLXZr0pShqZd1tPyGJmpINjtAWQFEW6mxR%2FlPhZLpY1K3zA0ATk9cbTOerihtQS4aBSYvcNlPzHwk8THadc8T6SGJ9WXBqQ5nmGzeCTh%2F7XOchWQKaEZqLnmLL4T9bo%2FONbIydnb402ADGduUhWTyd53V2m0wwGpX3a9iBEbTPLqUN5frp%2BepBOiYOmra4nihxOYlQ02taVwMqDIYSeRAQqpyuuESG9aaf1j9tVNzsmNL3oheDchNU%2BCJ9ddFZ7BW3G8cyl1XZZRXrG3Oq11xY8DahDOWZjRpLYlO2XmsUX8aex9ok49UeK65RwDgYKyHxpFjbdulQMuNYu5oBr5gnFSxx7gqvekhIXxJduLXxH5fQTedBreTvqTqIr6UkktlBdtzfyf7c8ZoJWBmRllXMX5sbiKZAD4R%2FGikOkrzlGHb%2F4AzK7vLraXUk%2FDMMuAjr0GOqUBh8oaaLFJ3Ld9vd%2FbXSr3ojzYRy2ukqXPgDvCL0y78I7leb0%2FS3Bi6p%2Fs93TyzsnHQQdh7%2B5ldwli064I3tJ9LRaxng26ydhYqtTyqZU53mZdwpv7cY%2B%2F2QPkybJqLpXqaR29Fo026VZkt8iSmbr6%2BF2dops2jNoCZ6s6g38qjbFTV7DESBJrW%2B%2F%2BPiZZhrjBh4IG%2FZF89AT5C6ohStJgOI05HIKr&X-Amz-Signature=05ca1df0e372ca3fa535850c152fb386d6805c55dd5eefec64a224c157ca238e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7ZVW762%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC2%2BX41r6BSxRJDLQcHz%2B84u8oXWTlyunr5PXl1uEby%2BAIgXazQyjapxve%2B%2By%2F9HfgGACyi9oPfYx4gPRA53B68KAwq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCqp6mejKDvNMosEayrcA0pho3sy0yHhFG0T9LH%2BVZpgA8OhnMV454pL5vyvEUhwU7MMQnuB81ZH8Qj7DmOsqrE0CT5rDkj17I1pZl1AZjm%2Fj0js8aKhAawb1eYmv8nhr%2FXYLPA3CNOSQreDyhG%2FmQA6lhxwKho4BD9oHKNS3SIMXlHk5DyYzL5rN26KIQPWmVS7njCJEVGQ8MV3ypsEOLXZr0pShqZd1tPyGJmpINjtAWQFEW6mxR%2FlPhZLpY1K3zA0ATk9cbTOerihtQS4aBSYvcNlPzHwk8THadc8T6SGJ9WXBqQ5nmGzeCTh%2F7XOchWQKaEZqLnmLL4T9bo%2FONbIydnb402ADGduUhWTyd53V2m0wwGpX3a9iBEbTPLqUN5frp%2BepBOiYOmra4nihxOYlQ02taVwMqDIYSeRAQqpyuuESG9aaf1j9tVNzsmNL3oheDchNU%2BCJ9ddFZ7BW3G8cyl1XZZRXrG3Oq11xY8DahDOWZjRpLYlO2XmsUX8aex9ok49UeK65RwDgYKyHxpFjbdulQMuNYu5oBr5gnFSxx7gqvekhIXxJduLXxH5fQTedBreTvqTqIr6UkktlBdtzfyf7c8ZoJWBmRllXMX5sbiKZAD4R%2FGikOkrzlGHb%2F4AzK7vLraXUk%2FDMMuAjr0GOqUBh8oaaLFJ3Ld9vd%2FbXSr3ojzYRy2ukqXPgDvCL0y78I7leb0%2FS3Bi6p%2Fs93TyzsnHQQdh7%2B5ldwli064I3tJ9LRaxng26ydhYqtTyqZU53mZdwpv7cY%2B%2F2QPkybJqLpXqaR29Fo026VZkt8iSmbr6%2BF2dops2jNoCZ6s6g38qjbFTV7DESBJrW%2B%2F%2BPiZZhrjBh4IG%2FZF89AT5C6ohStJgOI05HIKr&X-Amz-Signature=aae3fb18f71a35e8c9a58967b95d0ad8ac2995c26442800d79f7a5c657320eb7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7ZVW762%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC2%2BX41r6BSxRJDLQcHz%2B84u8oXWTlyunr5PXl1uEby%2BAIgXazQyjapxve%2B%2By%2F9HfgGACyi9oPfYx4gPRA53B68KAwq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCqp6mejKDvNMosEayrcA0pho3sy0yHhFG0T9LH%2BVZpgA8OhnMV454pL5vyvEUhwU7MMQnuB81ZH8Qj7DmOsqrE0CT5rDkj17I1pZl1AZjm%2Fj0js8aKhAawb1eYmv8nhr%2FXYLPA3CNOSQreDyhG%2FmQA6lhxwKho4BD9oHKNS3SIMXlHk5DyYzL5rN26KIQPWmVS7njCJEVGQ8MV3ypsEOLXZr0pShqZd1tPyGJmpINjtAWQFEW6mxR%2FlPhZLpY1K3zA0ATk9cbTOerihtQS4aBSYvcNlPzHwk8THadc8T6SGJ9WXBqQ5nmGzeCTh%2F7XOchWQKaEZqLnmLL4T9bo%2FONbIydnb402ADGduUhWTyd53V2m0wwGpX3a9iBEbTPLqUN5frp%2BepBOiYOmra4nihxOYlQ02taVwMqDIYSeRAQqpyuuESG9aaf1j9tVNzsmNL3oheDchNU%2BCJ9ddFZ7BW3G8cyl1XZZRXrG3Oq11xY8DahDOWZjRpLYlO2XmsUX8aex9ok49UeK65RwDgYKyHxpFjbdulQMuNYu5oBr5gnFSxx7gqvekhIXxJduLXxH5fQTedBreTvqTqIr6UkktlBdtzfyf7c8ZoJWBmRllXMX5sbiKZAD4R%2FGikOkrzlGHb%2F4AzK7vLraXUk%2FDMMuAjr0GOqUBh8oaaLFJ3Ld9vd%2FbXSr3ojzYRy2ukqXPgDvCL0y78I7leb0%2FS3Bi6p%2Fs93TyzsnHQQdh7%2B5ldwli064I3tJ9LRaxng26ydhYqtTyqZU53mZdwpv7cY%2B%2F2QPkybJqLpXqaR29Fo026VZkt8iSmbr6%2BF2dops2jNoCZ6s6g38qjbFTV7DESBJrW%2B%2F%2BPiZZhrjBh4IG%2FZF89AT5C6ohStJgOI05HIKr&X-Amz-Signature=08c11210b0d2f4f89ab1e8132ddbdacaceaa2785e0eccf6fcfcd1ff4f30202b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7ZVW762%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC2%2BX41r6BSxRJDLQcHz%2B84u8oXWTlyunr5PXl1uEby%2BAIgXazQyjapxve%2B%2By%2F9HfgGACyi9oPfYx4gPRA53B68KAwq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCqp6mejKDvNMosEayrcA0pho3sy0yHhFG0T9LH%2BVZpgA8OhnMV454pL5vyvEUhwU7MMQnuB81ZH8Qj7DmOsqrE0CT5rDkj17I1pZl1AZjm%2Fj0js8aKhAawb1eYmv8nhr%2FXYLPA3CNOSQreDyhG%2FmQA6lhxwKho4BD9oHKNS3SIMXlHk5DyYzL5rN26KIQPWmVS7njCJEVGQ8MV3ypsEOLXZr0pShqZd1tPyGJmpINjtAWQFEW6mxR%2FlPhZLpY1K3zA0ATk9cbTOerihtQS4aBSYvcNlPzHwk8THadc8T6SGJ9WXBqQ5nmGzeCTh%2F7XOchWQKaEZqLnmLL4T9bo%2FONbIydnb402ADGduUhWTyd53V2m0wwGpX3a9iBEbTPLqUN5frp%2BepBOiYOmra4nihxOYlQ02taVwMqDIYSeRAQqpyuuESG9aaf1j9tVNzsmNL3oheDchNU%2BCJ9ddFZ7BW3G8cyl1XZZRXrG3Oq11xY8DahDOWZjRpLYlO2XmsUX8aex9ok49UeK65RwDgYKyHxpFjbdulQMuNYu5oBr5gnFSxx7gqvekhIXxJduLXxH5fQTedBreTvqTqIr6UkktlBdtzfyf7c8ZoJWBmRllXMX5sbiKZAD4R%2FGikOkrzlGHb%2F4AzK7vLraXUk%2FDMMuAjr0GOqUBh8oaaLFJ3Ld9vd%2FbXSr3ojzYRy2ukqXPgDvCL0y78I7leb0%2FS3Bi6p%2Fs93TyzsnHQQdh7%2B5ldwli064I3tJ9LRaxng26ydhYqtTyqZU53mZdwpv7cY%2B%2F2QPkybJqLpXqaR29Fo026VZkt8iSmbr6%2BF2dops2jNoCZ6s6g38qjbFTV7DESBJrW%2B%2F%2BPiZZhrjBh4IG%2FZF89AT5C6ohStJgOI05HIKr&X-Amz-Signature=0fb4228daa1456bb49f0665f65a1a0eb0d5ea65490f2f293478686e555fda1b4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7Y3BUDT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQCPS%2FP2Gg5KGJNApj2sapQlI2xecIeVzRAE0QoSBBbKCQIgTKWDImk%2FkrTy8lQ1stO%2Bh1qCQU2MDgPbrSe5zlYOiiYq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDE9w8EiJCLzNvDjV4ircAwQ6l1HJ68ba5PE4g%2B3FIU01AOZeCeMLB1%2FOYvacP6zJ4wxjZrvl8OPBUKpnwy0VDxn%2FYeLa%2B0LeuJV6d4ljctxO3nipnKm6Ae0cFBkt92lMRNL3klfW1qHdNuGKgpZO%2B28W2J%2B%2BdEFmOeSdM6i5gT9oPAWHbRVTfPQIPNBbXMfV6AXFgnaiKBf69riueW7EuDQX9alOlB2SxmLw3kCCBwBca%2Bbpsa4GL8BgOUrx2i2uUS1O2DVAhIi3quema230o4B2SKI%2F5jvw6ip%2B5U7LtXg%2B8zskPqivFt5PdHM%2F8UPdXC2S8jvV4orZJ7L0rIuiYf0QVdswgrpSsb3YxnkmUvYIPc01kBTXLnSq4ftm7QYGUX4%2BooeRZ4BSZPvduWHn7z36rXWjVrPA%2FLzLcArYF8AzmTITtf99qg1XML04tQvg2B6vLgX9hihwLT1hzWFKztGXMbeNUfy0dBd1gxKiNFTxVAftZPmY7vqxXHj7pPbspRKWcgDdLiXrfDxroLpxrPbMlws8kgSmP1beYcWft0nnwDtGYT8O1yKlpZ%2Bu2a79bxpstXKfbu11SUZY6ymycK1SoYVVqSCIUZXCFm46O7GBF1a4hkzgcKUPascZ0p1qotogBb3aA3pEWq0hMK3jjb0GOqUBxs%2F0SMJFBMVMnEm%2BQQ8ZfEuvaTqMR7O%2Fr2XIBOf8u3AZIqKecB4aY4mur5qrXhQPYSFHlrMKG%2FlFyQAnMrKgTiWOjWyK9GZAUMriwAaWOJ4VhofvpkVQUNCKRmcblP6timNl5FICdtnEqHmsoF8CeOwdzKtD0gYalC8Uh%2FpcdqY%2BFdoaTcCtVmHCGV5IcJkufgmGVgqcahcA8inTdMO5kwPd2rQ%2B&X-Amz-Signature=6a625268242bf226965e57ff68dfb7f44f349220dd74be054dca16772300fd8c&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWZ53ISO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIGeUJCS%2FWdYJJiz6s9FYE0BEm4P8c3uwfOP8h2xZmgOrAiEA45t73u1p6pH3O4JAUeH3QunVsQVXGKdj%2Fev1HX9FSiYq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDM3lQ6hoPDzEFJQ9OyrcA%2BieOT2eFpB%2BeMLL1SWgG9%2FCHvVCiIr69k2J105gsEwsBaqfI%2F1d7ASRoS7O%2FhAqustkezIMLxpwfWSUvaZZ86jrLhCnOsMH6CZ3nxty0eb8yLgU1WGX15CSCKAp%2F8L6pQDNoros83ZDXLrfOqOATtb72zxgMzQe74iJdIbFA7MNzcJxmT6eu6Wqmbfk1Bf%2BCJ0isdRGR%2BLO1k%2BazZ5ADfVpGWPaDeypt7NaF3pCkHq%2FCiEBNjlpkiDqclLscFjneCVkvowV9Q1tEG1dQf0qx9%2BpUxEuK1M7IkCcPnGQ2zTv4hrosJHFs90NsoaYFnzjjBtnrzk0kN2ah2wkpQ6WjlHUJEOt9w9mWfDipcMN91tKyv9Cmpdq8AfJaMvu4AMDZ0xbrT9Zh2tMa0TlmypCZj4XpVAdR9NouzpR92trUKGUr0YG1MShInzRmf7GpLRjr3e%2FpOTxZ1DYzdQlJO9nm1Ai5v4NeWzXbo%2BBFGj4RLF6%2FxwppZfIqES9HjFxawbEEC5PmoPu3%2F0YQAgMGNrQu2nnJb3KP6mgMWN7cGSulJTHxHlvrRgltRgLO5uneyGmMfUcsC8CS4meLHB3wSDJ0YH%2BQxAeyO1QlYPk4GeOCuMGOCO0L2xk5O5o3DeNMPjjjb0GOqUBjZQLpp6U4gZlhpqvR%2FUPsBVRCi4lV1fWz6YyNsi3B19kCxedMs8GMTIZKBGYDz%2FupG2Xx4DnvBi9NmS5BbY8tf1DvBy%2FBmZb6Js5WlDNPp39cprqUnW54zDs2vyAGlKPiz2ivMUSRXEaZer4wgm%2FVjHtLoif1ciqj9a0eFD0uzsg3odIAFMIyUjHu5MbiQm%2Bi2MgoN2w0SplxrouDIvNLMEjTMxs&X-Amz-Signature=6b1a5c2f21b5aee576c0f53d14f088e854d18d67c5014cb9f8c7c40bafc0ad9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7ZVW762%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC2%2BX41r6BSxRJDLQcHz%2B84u8oXWTlyunr5PXl1uEby%2BAIgXazQyjapxve%2B%2By%2F9HfgGACyi9oPfYx4gPRA53B68KAwq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCqp6mejKDvNMosEayrcA0pho3sy0yHhFG0T9LH%2BVZpgA8OhnMV454pL5vyvEUhwU7MMQnuB81ZH8Qj7DmOsqrE0CT5rDkj17I1pZl1AZjm%2Fj0js8aKhAawb1eYmv8nhr%2FXYLPA3CNOSQreDyhG%2FmQA6lhxwKho4BD9oHKNS3SIMXlHk5DyYzL5rN26KIQPWmVS7njCJEVGQ8MV3ypsEOLXZr0pShqZd1tPyGJmpINjtAWQFEW6mxR%2FlPhZLpY1K3zA0ATk9cbTOerihtQS4aBSYvcNlPzHwk8THadc8T6SGJ9WXBqQ5nmGzeCTh%2F7XOchWQKaEZqLnmLL4T9bo%2FONbIydnb402ADGduUhWTyd53V2m0wwGpX3a9iBEbTPLqUN5frp%2BepBOiYOmra4nihxOYlQ02taVwMqDIYSeRAQqpyuuESG9aaf1j9tVNzsmNL3oheDchNU%2BCJ9ddFZ7BW3G8cyl1XZZRXrG3Oq11xY8DahDOWZjRpLYlO2XmsUX8aex9ok49UeK65RwDgYKyHxpFjbdulQMuNYu5oBr5gnFSxx7gqvekhIXxJduLXxH5fQTedBreTvqTqIr6UkktlBdtzfyf7c8ZoJWBmRllXMX5sbiKZAD4R%2FGikOkrzlGHb%2F4AzK7vLraXUk%2FDMMuAjr0GOqUBh8oaaLFJ3Ld9vd%2FbXSr3ojzYRy2ukqXPgDvCL0y78I7leb0%2FS3Bi6p%2Fs93TyzsnHQQdh7%2B5ldwli064I3tJ9LRaxng26ydhYqtTyqZU53mZdwpv7cY%2B%2F2QPkybJqLpXqaR29Fo026VZkt8iSmbr6%2BF2dops2jNoCZ6s6g38qjbFTV7DESBJrW%2B%2F%2BPiZZhrjBh4IG%2FZF89AT5C6ohStJgOI05HIKr&X-Amz-Signature=d58a48e924ff0829683731874201af14f000b760c78fe11ea36b43658c22ce2b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7ZVW762%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC2%2BX41r6BSxRJDLQcHz%2B84u8oXWTlyunr5PXl1uEby%2BAIgXazQyjapxve%2B%2By%2F9HfgGACyi9oPfYx4gPRA53B68KAwq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCqp6mejKDvNMosEayrcA0pho3sy0yHhFG0T9LH%2BVZpgA8OhnMV454pL5vyvEUhwU7MMQnuB81ZH8Qj7DmOsqrE0CT5rDkj17I1pZl1AZjm%2Fj0js8aKhAawb1eYmv8nhr%2FXYLPA3CNOSQreDyhG%2FmQA6lhxwKho4BD9oHKNS3SIMXlHk5DyYzL5rN26KIQPWmVS7njCJEVGQ8MV3ypsEOLXZr0pShqZd1tPyGJmpINjtAWQFEW6mxR%2FlPhZLpY1K3zA0ATk9cbTOerihtQS4aBSYvcNlPzHwk8THadc8T6SGJ9WXBqQ5nmGzeCTh%2F7XOchWQKaEZqLnmLL4T9bo%2FONbIydnb402ADGduUhWTyd53V2m0wwGpX3a9iBEbTPLqUN5frp%2BepBOiYOmra4nihxOYlQ02taVwMqDIYSeRAQqpyuuESG9aaf1j9tVNzsmNL3oheDchNU%2BCJ9ddFZ7BW3G8cyl1XZZRXrG3Oq11xY8DahDOWZjRpLYlO2XmsUX8aex9ok49UeK65RwDgYKyHxpFjbdulQMuNYu5oBr5gnFSxx7gqvekhIXxJduLXxH5fQTedBreTvqTqIr6UkktlBdtzfyf7c8ZoJWBmRllXMX5sbiKZAD4R%2FGikOkrzlGHb%2F4AzK7vLraXUk%2FDMMuAjr0GOqUBh8oaaLFJ3Ld9vd%2FbXSr3ojzYRy2ukqXPgDvCL0y78I7leb0%2FS3Bi6p%2Fs93TyzsnHQQdh7%2B5ldwli064I3tJ9LRaxng26ydhYqtTyqZU53mZdwpv7cY%2B%2F2QPkybJqLpXqaR29Fo026VZkt8iSmbr6%2BF2dops2jNoCZ6s6g38qjbFTV7DESBJrW%2B%2F%2BPiZZhrjBh4IG%2FZF89AT5C6ohStJgOI05HIKr&X-Amz-Signature=a019cac975b3e12a614d9efd9b08fbbb3a051bd031e4f3918740d542bb469815&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7ZVW762%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC2%2BX41r6BSxRJDLQcHz%2B84u8oXWTlyunr5PXl1uEby%2BAIgXazQyjapxve%2B%2By%2F9HfgGACyi9oPfYx4gPRA53B68KAwq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCqp6mejKDvNMosEayrcA0pho3sy0yHhFG0T9LH%2BVZpgA8OhnMV454pL5vyvEUhwU7MMQnuB81ZH8Qj7DmOsqrE0CT5rDkj17I1pZl1AZjm%2Fj0js8aKhAawb1eYmv8nhr%2FXYLPA3CNOSQreDyhG%2FmQA6lhxwKho4BD9oHKNS3SIMXlHk5DyYzL5rN26KIQPWmVS7njCJEVGQ8MV3ypsEOLXZr0pShqZd1tPyGJmpINjtAWQFEW6mxR%2FlPhZLpY1K3zA0ATk9cbTOerihtQS4aBSYvcNlPzHwk8THadc8T6SGJ9WXBqQ5nmGzeCTh%2F7XOchWQKaEZqLnmLL4T9bo%2FONbIydnb402ADGduUhWTyd53V2m0wwGpX3a9iBEbTPLqUN5frp%2BepBOiYOmra4nihxOYlQ02taVwMqDIYSeRAQqpyuuESG9aaf1j9tVNzsmNL3oheDchNU%2BCJ9ddFZ7BW3G8cyl1XZZRXrG3Oq11xY8DahDOWZjRpLYlO2XmsUX8aex9ok49UeK65RwDgYKyHxpFjbdulQMuNYu5oBr5gnFSxx7gqvekhIXxJduLXxH5fQTedBreTvqTqIr6UkktlBdtzfyf7c8ZoJWBmRllXMX5sbiKZAD4R%2FGikOkrzlGHb%2F4AzK7vLraXUk%2FDMMuAjr0GOqUBh8oaaLFJ3Ld9vd%2FbXSr3ojzYRy2ukqXPgDvCL0y78I7leb0%2FS3Bi6p%2Fs93TyzsnHQQdh7%2B5ldwli064I3tJ9LRaxng26ydhYqtTyqZU53mZdwpv7cY%2B%2F2QPkybJqLpXqaR29Fo026VZkt8iSmbr6%2BF2dops2jNoCZ6s6g38qjbFTV7DESBJrW%2B%2F%2BPiZZhrjBh4IG%2FZF89AT5C6ohStJgOI05HIKr&X-Amz-Signature=af001a3994f31a7eba2d847f3aff204a10a3596b6da249518acd5afbc9d94f8e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DXEETJY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIGLXX%2FlOIVGTvy1JXjBB1NcqGBE8DWO81alZFwHPCDs5AiEAnvgO0LO99mzADnGxfPxzUaoU2sRg0XwJo1h%2FZB%2BKfHgq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDJrliDYUsfshOZQiJyrcA43zNe11fYSkwugZGT0F5qQh6nehfqZ%2FHFrDgh5VnkJ9rd6ldiYA9g%2F49Qihf7v6tPrfsgypwD8p9pK%2B97%2B7U6ZJ8r9Zpd74s53%2BJc2%2BdaLAW3ms6pt3TzirTsrc1Tbgdes1C0Xz1tRp9k7EZkeALclV1lTGVMga%2Bpoyg7DwokSXQ2L72POh8nsLxzGGwphEkWGZl5ZAbKdkhUllTY71EZH57eoNVp93phRK0pDMlakHGR7XWEdH1BQLs%2FxQhzTkCmijXi9eGTIXb%2B0TVJpTA%2BtigSP%2BdScRetEkJzbAnXfllfOPiJ0NkPFtTiqOC%2B83F19LMBWatx67UK6uSNopW5h%2Fqb%2BJFm%2BqrjT7l7AGDBgbmRL76jnMRQS36D2BXoCoK7%2FuRM7RPrOWT%2Bctkgy6gxBKz03BbC3%2FfD%2FwVXJBnxTL9%2F9nk3k62WJwcesqqWbAsaiAjIK6Ksm9QFZhD8lsSSy4b6lgGeVXhzE8w0RnNzeUKPhsfsiPXZ0fl4X%2F66MZ5SdnkCdit0OEmxBjhG0%2F0Czb7bU80j7L2vAU6QR2uKkgv5PtlhXfMb0%2BSjSC9oOdN8iVToSGu0TQh5M3AbCGgg36%2BuOpmhUUuxWvPWRuUStCCAtLSmWLQKh2CiYiMNfjjb0GOqUBhNSmvP2PVPfrNqU10aNDFgmeKD74KSlUEKCWX%2BYiVYNGrLxQ2F8e0znPPj6lDnYAnMhjix1mf5EfCH%2FQxJj1ZTpEPzyo9d4zw%2F8YJ%2FrcR6ibkVEQMZOMaFPN2tmbmOm2lqI2xO9gkwXuTBphC4a4ruDXEuouyEu4LOUdgo3ae1UzgAQUFCnpPiIndKteV2%2Bsicsjb%2BoYyokXo4asGtWJoK4GqZkZ&X-Amz-Signature=8c3056cdee51ac5ebe614a539693f099d9a254a8e13adaaff3c2bfc67140ec54&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OA5DDZ6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQCqWCnEfMihAgrPb7P7xIMtexhGktkl0TgRjk%2BKERHAngIhAMNZHEQeqhxIxJC9iDecinsiiZ%2FqNFqlM9A2%2BfaFxxa%2BKv8DCEgQABoMNjM3NDIzMTgzODA1IgzEZeZ6kaztChIkoSEq3ANlVmQ6l2ujmYmsljHwp66j6Anc67GTX%2BOTSMTI46yYyGSNPcPlqTxedWdQhssM0IJu8N%2FdKaOfDBZgEe9dZ%2BadAFHjI5qCN9HCJtoB8MPbBTiLZtTgHEOJ0AFDI%2Bf3sXAdvDcFa9K%2BtZRrZNDyijTeTIeDtAfQe6id5Ow%2FsDHeHpk1I2rrk2ppLhYKP8jFVbEXX7dFMij2YBzJ0NXwqbL6J3XAygujptnPc%2F62lp8Am7gB8kZpKPpAR%2BajkhrmaSr%2FhvIdeIiQnTxlyvx2uG1afxEJMwfTJGn5XSDAnHFvonBGQDBX8l2HAY4sOM2P28QLZIBUJFTn%2Fd5C0d1A65aNg2IQmDCUr1QJA6sA5ykr%2BdiXN43DVn9%2FZcSrQp04gI2OqC87zNlRBuSOS%2FcnnAhYM1zZLhO271Cwat8cGSj69bSLFLNAFzQAKsG0M%2BQ890wFBDQheLlULsfeyTBjnfXoGgwaEyle4Q0hF4p%2FgczpQxxM78CBzoAJdxtl66qSscFntEixc7mxVOdPc2AUZh5eKwsru0It5bFXu8rXwn7e%2FdmEZSaof8nzZ0D5sreGhyZl7SJLCkZqtLGaq%2FqTrVB5kt5Y5tTcuYY5C%2B9MM21yO7O5AokCcUOfs6YWVzDBgI69BjqkAXbcv%2BpRo2A3D2N7v2ug98dn1urBugvYO3rijARMvkBJ8hohwap3cGdat8%2FkmODYzUuSVtHP%2Bwalp0VUea1mSCH%2FE2IWFwQ5V9WMzzJ5D2KGcGbXHIh%2BAqWs1CYJKwR5BRYRqmudyEKeWp0JZ9mJlBJ0AQ3l49f1JU7BpCyz3rttphJijqGtfkTPaYoZY6sGVvBMYjtKIo23U3P8mt4ntMbpWrV1&X-Amz-Signature=63538ebf17e7ef82177a0119aa832abf6bdb4b14cf0404a71d37e6a5ba106947&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SG3YOLAB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIGcy9XfgKBXB5mLviVdEKm8pvfYUJvbnmQufaufoeYKJAiBsflmlEk75vAVRBoe%2BaOJIrCbp%2Ft8cTPE2lI7hMAaIySr%2FAwhIEAAaDDYzNzQyMzE4MzgwNSIMx71qMPoY8oJIa71GKtwDK9VPWqARLZOa%2FRS9c3iRJZNfZsnWtA%2Fqf9qqmjkw35hHsjSEYyT0z9%2FwzPWAaIx%2FcBoYtnmBe2LdHeDYQENUf4iUv7%2FILzvlsb9GdalO1aN9MDVo5v9lwSZffxh9pD7jJi6rFyeNX%2FZ8JLJqe%2FkVt0r3eX9HTR3gzL%2Ft00609KEvZ2BdOOWzLBgP24S%2FnRXTIgRu%2BiQWeK3Npn1Y34NyUq%2BnmYLjOczDrLqZ1V4kFEF8hrdrd6MT0pVwh%2F%2FU%2Fn55lEqR9EOCPxe8gAqSVoLnuz890s9WkM44t9GHpoKGNuWADgKSMs0Djy848e6FUntaJbETAHFsDdshCqzlPSqqPIB3UqI8hwSBiJEIxGwOEQc5r3mr%2BNldu%2Fr5VWdMwXaHHnUGTw4gjfTNHbg71Kn4y%2BJgkQJ%2BhKZjp6utyonO3K3zgCLaC4WuHnMJlxCrdIC73zAhIoftmkkSUk3NmCpVOSfcx%2B%2Bpm3vsdtOdpxWRb3CRhUGyaj0AHN%2FM7vh%2F%2FNeG3yX%2FNkJV4Je7AvQ7%2BV3MzJUGfQSDHq5kcoT%2Fst6wEQUhswLyrOsJbDhbbzSiXlVSMbk488CFNmTvV4RCv4fa10T2PllLZGB4gDjMnLUH689MwFebW8aO3bEJmO4wy4COvQY6pgFwJYAit0PJpOMfmf4URUCCgVSkeUu%2FZoOZX5AwOl5E6vksTJkY0UsA0sRbrAAkx5%2FQ8R1z3fuPkIVxMtpk1a37wBIyvQISD9tYqiwNwtdV81Gg%2Bb89cPry%2FQ4QHqErQaD6YkmiDvCeeTrDNmGlzqMSEHo8u475NXXDtx70sva6K1VLpsxg0vg2FLolfi0eDpNPlc4PD%2FiWKY0u3k0d8SnZ2ugFdakT&X-Amz-Signature=c3b44cbce88e21ac9b616f4285d78c63bdf40f8bb5cf9630f25555ebce0ef8af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YUQ22AV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCUpkVzGwSTMLpzTzcIBZjZlutnt1ROewSXr9o4jbSFeAIhAJBYMFCcKIUQP4oj%2FIvaguy%2FwnJbjO8W5geHyC%2FuxQqOKv8DCEcQABoMNjM3NDIzMTgzODA1Igxxi4cHAqn5ZRkXeLAq3ANfaD%2BgXUTMYJ7V3IU6n%2BzCJ8m7I4X8aUcRQ3NGSruc2S9MQGhzyUuGPYUVGAr1ovdyI2cBovn2mu5oxohlqI1LjdK9wjswjt1ImK2RcsR%2FjElhBs21f0jubMAFklLC2jhXvlbxbJOVOwP2nRHJJbhIofbh20Rosf3QoXXzNFr1rGDNR%2FzcwlhxGw80V3HHSgId8e%2B2uQrtjSNhuU%2B1BlIm2hFV33DqgTKCu9F7eBkmaRxryhpzNN%2FBOo2z2g%2Fzu8YAoXoxawpwLjoJPz%2FC53Z%2FlQIJp3clfAqUMaSCqwvy44vXESf0M7euOXY7yikBlpSWorEgVRoDL8IgBzuX51wqzhD0ip06w1f9suNyDunsIfC4hCzGz3TFTIE5uAWNAscO257m7du9U9a3VDd9pHYuGjlswHsVXJjTFY1y3A24HxLQ7mOf7s8tN5f0Q6inLUNxpnuQLzeB%2FLi0CGjuqG0gpMag2vRRnoSd1iNzvDO0%2FamleTVM88kEUBTxa02gO2VRzE4tnwZUubBQ8gLJJ6Sk3CNyRHu7t4WtsPJmdTDJmVxOrC%2B23N%2BHpzCgy8ewUBg68fdjPLNvFFI0KE5AT2CdUUQddoG0msx%2BA8LskpIoxnPpLeSUlGwCOpgfqTCt4429BjqkAf5OQqWCnlKaW0IC8OiaMh4RShdiO1NdUbdPNaMFELhf7OcA3F2VK2bYDRTsyKXG%2BrQvE4CIBDl%2BamYmc6ZMGtx3kkfkoQ9BgqgHMuS3tl9qAAdb%2BrQOHFnLkmZ%2FoLAz%2BjDND0tSGY93ZVXRsTBg7lu8EC939B750WiSP46FR8PWcVfOQ00%2FASi9WI4QMyL7Ooyq1aOckLd2TsFsHVzI5ha0Np3F&X-Amz-Signature=34022761a29ac8f615f8ab77e89cdc98cb6058b38c85919e0fabb7140fa35ae1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YUQ22AV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCUpkVzGwSTMLpzTzcIBZjZlutnt1ROewSXr9o4jbSFeAIhAJBYMFCcKIUQP4oj%2FIvaguy%2FwnJbjO8W5geHyC%2FuxQqOKv8DCEcQABoMNjM3NDIzMTgzODA1Igxxi4cHAqn5ZRkXeLAq3ANfaD%2BgXUTMYJ7V3IU6n%2BzCJ8m7I4X8aUcRQ3NGSruc2S9MQGhzyUuGPYUVGAr1ovdyI2cBovn2mu5oxohlqI1LjdK9wjswjt1ImK2RcsR%2FjElhBs21f0jubMAFklLC2jhXvlbxbJOVOwP2nRHJJbhIofbh20Rosf3QoXXzNFr1rGDNR%2FzcwlhxGw80V3HHSgId8e%2B2uQrtjSNhuU%2B1BlIm2hFV33DqgTKCu9F7eBkmaRxryhpzNN%2FBOo2z2g%2Fzu8YAoXoxawpwLjoJPz%2FC53Z%2FlQIJp3clfAqUMaSCqwvy44vXESf0M7euOXY7yikBlpSWorEgVRoDL8IgBzuX51wqzhD0ip06w1f9suNyDunsIfC4hCzGz3TFTIE5uAWNAscO257m7du9U9a3VDd9pHYuGjlswHsVXJjTFY1y3A24HxLQ7mOf7s8tN5f0Q6inLUNxpnuQLzeB%2FLi0CGjuqG0gpMag2vRRnoSd1iNzvDO0%2FamleTVM88kEUBTxa02gO2VRzE4tnwZUubBQ8gLJJ6Sk3CNyRHu7t4WtsPJmdTDJmVxOrC%2B23N%2BHpzCgy8ewUBg68fdjPLNvFFI0KE5AT2CdUUQddoG0msx%2BA8LskpIoxnPpLeSUlGwCOpgfqTCt4429BjqkAf5OQqWCnlKaW0IC8OiaMh4RShdiO1NdUbdPNaMFELhf7OcA3F2VK2bYDRTsyKXG%2BrQvE4CIBDl%2BamYmc6ZMGtx3kkfkoQ9BgqgHMuS3tl9qAAdb%2BrQOHFnLkmZ%2FoLAz%2BjDND0tSGY93ZVXRsTBg7lu8EC939B750WiSP46FR8PWcVfOQ00%2FASi9WI4QMyL7Ooyq1aOckLd2TsFsHVzI5ha0Np3F&X-Amz-Signature=b64f01d8629b2fe26a273b274abc4d799d05d596cf7046f1f1fd583c45fab29c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
