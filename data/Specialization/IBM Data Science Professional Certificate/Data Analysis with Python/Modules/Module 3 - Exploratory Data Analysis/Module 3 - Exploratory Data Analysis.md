

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Q45TIHA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjqWsvtA7SY578grdkxI1jWwgSSARX4Xzq1U2oxBLSngIgcexn4BteEu2BsnF5EFVRH2rsH9fzWpLAJQDya0J4DuIqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPWBV%2BSSo8WK5Aby3ircAwTJ80x4WziLjTAGJaMeS8SLqbKv39kc%2FXQXNa7XtzLG6l4j8e4%2B53ZkUHhQTxMGRjZqjSLZsxUtoDHRtGPE9vyatAifCVfdKinK%2BnqBo7tB00paX1S45cQblWnWj42Ykfsow0DfUBNEJauX3Fin1u%2FQ06kixIW3dBgPzBW5pMWwW9mWu9hqpUitqKcvNuwcW4nL%2Bto%2FiQaTqFoLfkcBDltX0J0ZFoV9PXsIUo0K9CbzWi0YbnL3ZocBGwUsXIiToOHrLhHjIs33CdqvErNA02n5VteOALr8CaQQJ4HH1n%2BTKvHzjj0OVle2871Gw29RwpeG16i6NF1NmFD1Ynbc%2FUJw%2F7EG8TFRYkrRRQQQNRlxC3SGGt233SUc7TV00EHWPfvVNsmbB%2BdTUwzDk6ikGvt4eQyxCadvW1kaXeyyachsmb%2B7GuuJWDjVnftUEEiHvxqWubRRhdp1joZmjMADC536%2Bcj4Sq%2BCb9PHZPmT8UC41g93rLPzwMgq8hZFQtrSGBAXDpRCo1kJKt0eJD%2Fz5VAcAaWYdK%2BLRE6zRp8Hg9fLDlUmEpovz5JwK9MVmAPcSBTqUK8YwUSCJ2pH371MYN9E7Wp6%2FQQ6cjw5jLHXd9pX47Ikt%2FxHEvV%2FmVWOMNLW7rwGOqUB6TAuQC5J4Je9tjJTzg7WHsC3qjWKrfrl7wohou5LwetSbW%2FekK9zaxArAWX8TdERhypMREEiaFG3BsXxBXOpyEyfEiKntluNEn%2BJf3IjQdAAj8GkpgKzQnfvfMeVDg00IzLfcXCuIj3uhApwdvv4I%2FKAPopi%2BKMUc%2FCTHZ8%2BuBBHXcmYh4PUoQ6NyyJYSApu%2B%2F7eo5Dkc267MM%2BJ9FFR22YAvI2C&X-Amz-Signature=73313ec67d2b32be9ce9db9edf24cac28eba5f0755265fca32823dbc7a7f5c93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Q45TIHA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjqWsvtA7SY578grdkxI1jWwgSSARX4Xzq1U2oxBLSngIgcexn4BteEu2BsnF5EFVRH2rsH9fzWpLAJQDya0J4DuIqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPWBV%2BSSo8WK5Aby3ircAwTJ80x4WziLjTAGJaMeS8SLqbKv39kc%2FXQXNa7XtzLG6l4j8e4%2B53ZkUHhQTxMGRjZqjSLZsxUtoDHRtGPE9vyatAifCVfdKinK%2BnqBo7tB00paX1S45cQblWnWj42Ykfsow0DfUBNEJauX3Fin1u%2FQ06kixIW3dBgPzBW5pMWwW9mWu9hqpUitqKcvNuwcW4nL%2Bto%2FiQaTqFoLfkcBDltX0J0ZFoV9PXsIUo0K9CbzWi0YbnL3ZocBGwUsXIiToOHrLhHjIs33CdqvErNA02n5VteOALr8CaQQJ4HH1n%2BTKvHzjj0OVle2871Gw29RwpeG16i6NF1NmFD1Ynbc%2FUJw%2F7EG8TFRYkrRRQQQNRlxC3SGGt233SUc7TV00EHWPfvVNsmbB%2BdTUwzDk6ikGvt4eQyxCadvW1kaXeyyachsmb%2B7GuuJWDjVnftUEEiHvxqWubRRhdp1joZmjMADC536%2Bcj4Sq%2BCb9PHZPmT8UC41g93rLPzwMgq8hZFQtrSGBAXDpRCo1kJKt0eJD%2Fz5VAcAaWYdK%2BLRE6zRp8Hg9fLDlUmEpovz5JwK9MVmAPcSBTqUK8YwUSCJ2pH371MYN9E7Wp6%2FQQ6cjw5jLHXd9pX47Ikt%2FxHEvV%2FmVWOMNLW7rwGOqUB6TAuQC5J4Je9tjJTzg7WHsC3qjWKrfrl7wohou5LwetSbW%2FekK9zaxArAWX8TdERhypMREEiaFG3BsXxBXOpyEyfEiKntluNEn%2BJf3IjQdAAj8GkpgKzQnfvfMeVDg00IzLfcXCuIj3uhApwdvv4I%2FKAPopi%2BKMUc%2FCTHZ8%2BuBBHXcmYh4PUoQ6NyyJYSApu%2B%2F7eo5Dkc267MM%2BJ9FFR22YAvI2C&X-Amz-Signature=9a72b2f73f23340c6b5d02fdebdf460cf3458be5bd7bb4cee8ec8c4a50a19655&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Q45TIHA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjqWsvtA7SY578grdkxI1jWwgSSARX4Xzq1U2oxBLSngIgcexn4BteEu2BsnF5EFVRH2rsH9fzWpLAJQDya0J4DuIqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPWBV%2BSSo8WK5Aby3ircAwTJ80x4WziLjTAGJaMeS8SLqbKv39kc%2FXQXNa7XtzLG6l4j8e4%2B53ZkUHhQTxMGRjZqjSLZsxUtoDHRtGPE9vyatAifCVfdKinK%2BnqBo7tB00paX1S45cQblWnWj42Ykfsow0DfUBNEJauX3Fin1u%2FQ06kixIW3dBgPzBW5pMWwW9mWu9hqpUitqKcvNuwcW4nL%2Bto%2FiQaTqFoLfkcBDltX0J0ZFoV9PXsIUo0K9CbzWi0YbnL3ZocBGwUsXIiToOHrLhHjIs33CdqvErNA02n5VteOALr8CaQQJ4HH1n%2BTKvHzjj0OVle2871Gw29RwpeG16i6NF1NmFD1Ynbc%2FUJw%2F7EG8TFRYkrRRQQQNRlxC3SGGt233SUc7TV00EHWPfvVNsmbB%2BdTUwzDk6ikGvt4eQyxCadvW1kaXeyyachsmb%2B7GuuJWDjVnftUEEiHvxqWubRRhdp1joZmjMADC536%2Bcj4Sq%2BCb9PHZPmT8UC41g93rLPzwMgq8hZFQtrSGBAXDpRCo1kJKt0eJD%2Fz5VAcAaWYdK%2BLRE6zRp8Hg9fLDlUmEpovz5JwK9MVmAPcSBTqUK8YwUSCJ2pH371MYN9E7Wp6%2FQQ6cjw5jLHXd9pX47Ikt%2FxHEvV%2FmVWOMNLW7rwGOqUB6TAuQC5J4Je9tjJTzg7WHsC3qjWKrfrl7wohou5LwetSbW%2FekK9zaxArAWX8TdERhypMREEiaFG3BsXxBXOpyEyfEiKntluNEn%2BJf3IjQdAAj8GkpgKzQnfvfMeVDg00IzLfcXCuIj3uhApwdvv4I%2FKAPopi%2BKMUc%2FCTHZ8%2BuBBHXcmYh4PUoQ6NyyJYSApu%2B%2F7eo5Dkc267MM%2BJ9FFR22YAvI2C&X-Amz-Signature=f49cd6fb05ebbaff047d0580741a83e901a9457b043791c29579f1919c26a584&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKHUS4B4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWx3dxyaWLeo3zdFkCMwvkMvt9KnnNK9MBqaX0sGsYAAiBYx%2BACS1fjl9oOe5FWQH3usw9ciwMwZB4BZB4voQipdCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRa7BFw3xjVGn3182KtwD5wYNvCPtzBuYjnHZ208sAoOdgp6IRrDUxLCLeKDW0AcObK8a8Br8RS3aKjxB%2BalirjlNcd37rzD6myABNNJB8VRSKTT8AhxWYDIdF7M%2FneOa5yj6ajx%2FAmTYFL9l8BvoEp4BOpUjIu7fdYg6wRicXSTj7h4JFc3AL785jgGcg18zdCFyTUV4GDGW37%2B%2BGVUVuZcXQEM2vIRkOvPGtIZ1aM6S92YDbh4cV21MVWDE20Af8jsFLKnEGAI37KDm5jBta4hM%2Bgb2YbQ%2BWErSQDjS%2BSQs4Jmy7pFeU3rjEP6QTxT8tAVXH4r5Wswr4JjJLveYvisrtoPvGA7hgRKTI97cAxJYFu7jo6UNJXP3yBZbxP2qa6kVdBzcSDRJuKTF8%2F4gfuO99%2B1OMRokXKxeZ%2BSuvnttkLF2jD3tgN2krQ%2B0qpElMPOF0NiOYhq73JNsaxv3pdEKuWNSXtMUKM5rWNF2XggkTDr%2BkzSjwS8Y6XKL2jk6Ss2nYrd4%2BQyA26OX2hfZIbuANupfbkrHHN42YAxfjxyZaM0w5dQewdHFpJ7%2FQeB3%2FSW7vDkIcVOeBfRoFLXMmPjtaMZjn6cNUraiGk%2BesD7lTdwdgeusvSlwekmSk5uVHVJWlX94WPNsF3owo9fuvAY6pgEHUOR3K0xCEtvEDRUgxB7sdlXjtvLoTlbvslftK4HemdhtehgTgJJRa39Bmgra9V9KPtUMwUJbe%2FUp8JlH0Afu8imLo6WNuYu4bCDdsPeOk1CqNaJxTQpgJD1PVVMEIgfnjeastu7QmUs6dgqQvqrDSOdueaS%2B2LK8%2BGq9Fb3o5DnBFyK8wQbR1j2COdEL%2BpIJ2r04cQpFXBaqdXv%2B7VeCa2mKc2dF&X-Amz-Signature=ba763b9ff968ee2fe23ceb5376fbb989f71f7ce4f99f871a538539440981e7c2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKHUS4B4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWx3dxyaWLeo3zdFkCMwvkMvt9KnnNK9MBqaX0sGsYAAiBYx%2BACS1fjl9oOe5FWQH3usw9ciwMwZB4BZB4voQipdCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRa7BFw3xjVGn3182KtwD5wYNvCPtzBuYjnHZ208sAoOdgp6IRrDUxLCLeKDW0AcObK8a8Br8RS3aKjxB%2BalirjlNcd37rzD6myABNNJB8VRSKTT8AhxWYDIdF7M%2FneOa5yj6ajx%2FAmTYFL9l8BvoEp4BOpUjIu7fdYg6wRicXSTj7h4JFc3AL785jgGcg18zdCFyTUV4GDGW37%2B%2BGVUVuZcXQEM2vIRkOvPGtIZ1aM6S92YDbh4cV21MVWDE20Af8jsFLKnEGAI37KDm5jBta4hM%2Bgb2YbQ%2BWErSQDjS%2BSQs4Jmy7pFeU3rjEP6QTxT8tAVXH4r5Wswr4JjJLveYvisrtoPvGA7hgRKTI97cAxJYFu7jo6UNJXP3yBZbxP2qa6kVdBzcSDRJuKTF8%2F4gfuO99%2B1OMRokXKxeZ%2BSuvnttkLF2jD3tgN2krQ%2B0qpElMPOF0NiOYhq73JNsaxv3pdEKuWNSXtMUKM5rWNF2XggkTDr%2BkzSjwS8Y6XKL2jk6Ss2nYrd4%2BQyA26OX2hfZIbuANupfbkrHHN42YAxfjxyZaM0w5dQewdHFpJ7%2FQeB3%2FSW7vDkIcVOeBfRoFLXMmPjtaMZjn6cNUraiGk%2BesD7lTdwdgeusvSlwekmSk5uVHVJWlX94WPNsF3owo9fuvAY6pgEHUOR3K0xCEtvEDRUgxB7sdlXjtvLoTlbvslftK4HemdhtehgTgJJRa39Bmgra9V9KPtUMwUJbe%2FUp8JlH0Afu8imLo6WNuYu4bCDdsPeOk1CqNaJxTQpgJD1PVVMEIgfnjeastu7QmUs6dgqQvqrDSOdueaS%2B2LK8%2BGq9Fb3o5DnBFyK8wQbR1j2COdEL%2BpIJ2r04cQpFXBaqdXv%2B7VeCa2mKc2dF&X-Amz-Signature=4b5eb95080db269a827a6ddfc99ac2da32df82979ba2fd8949baeef1afd4b46a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKHUS4B4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWx3dxyaWLeo3zdFkCMwvkMvt9KnnNK9MBqaX0sGsYAAiBYx%2BACS1fjl9oOe5FWQH3usw9ciwMwZB4BZB4voQipdCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRa7BFw3xjVGn3182KtwD5wYNvCPtzBuYjnHZ208sAoOdgp6IRrDUxLCLeKDW0AcObK8a8Br8RS3aKjxB%2BalirjlNcd37rzD6myABNNJB8VRSKTT8AhxWYDIdF7M%2FneOa5yj6ajx%2FAmTYFL9l8BvoEp4BOpUjIu7fdYg6wRicXSTj7h4JFc3AL785jgGcg18zdCFyTUV4GDGW37%2B%2BGVUVuZcXQEM2vIRkOvPGtIZ1aM6S92YDbh4cV21MVWDE20Af8jsFLKnEGAI37KDm5jBta4hM%2Bgb2YbQ%2BWErSQDjS%2BSQs4Jmy7pFeU3rjEP6QTxT8tAVXH4r5Wswr4JjJLveYvisrtoPvGA7hgRKTI97cAxJYFu7jo6UNJXP3yBZbxP2qa6kVdBzcSDRJuKTF8%2F4gfuO99%2B1OMRokXKxeZ%2BSuvnttkLF2jD3tgN2krQ%2B0qpElMPOF0NiOYhq73JNsaxv3pdEKuWNSXtMUKM5rWNF2XggkTDr%2BkzSjwS8Y6XKL2jk6Ss2nYrd4%2BQyA26OX2hfZIbuANupfbkrHHN42YAxfjxyZaM0w5dQewdHFpJ7%2FQeB3%2FSW7vDkIcVOeBfRoFLXMmPjtaMZjn6cNUraiGk%2BesD7lTdwdgeusvSlwekmSk5uVHVJWlX94WPNsF3owo9fuvAY6pgEHUOR3K0xCEtvEDRUgxB7sdlXjtvLoTlbvslftK4HemdhtehgTgJJRa39Bmgra9V9KPtUMwUJbe%2FUp8JlH0Afu8imLo6WNuYu4bCDdsPeOk1CqNaJxTQpgJD1PVVMEIgfnjeastu7QmUs6dgqQvqrDSOdueaS%2B2LK8%2BGq9Fb3o5DnBFyK8wQbR1j2COdEL%2BpIJ2r04cQpFXBaqdXv%2B7VeCa2mKc2dF&X-Amz-Signature=0ff47110077dc975e57631911d2e46d6bc1b1e843bfdd1cd6dc325b298251b6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKHUS4B4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWx3dxyaWLeo3zdFkCMwvkMvt9KnnNK9MBqaX0sGsYAAiBYx%2BACS1fjl9oOe5FWQH3usw9ciwMwZB4BZB4voQipdCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRa7BFw3xjVGn3182KtwD5wYNvCPtzBuYjnHZ208sAoOdgp6IRrDUxLCLeKDW0AcObK8a8Br8RS3aKjxB%2BalirjlNcd37rzD6myABNNJB8VRSKTT8AhxWYDIdF7M%2FneOa5yj6ajx%2FAmTYFL9l8BvoEp4BOpUjIu7fdYg6wRicXSTj7h4JFc3AL785jgGcg18zdCFyTUV4GDGW37%2B%2BGVUVuZcXQEM2vIRkOvPGtIZ1aM6S92YDbh4cV21MVWDE20Af8jsFLKnEGAI37KDm5jBta4hM%2Bgb2YbQ%2BWErSQDjS%2BSQs4Jmy7pFeU3rjEP6QTxT8tAVXH4r5Wswr4JjJLveYvisrtoPvGA7hgRKTI97cAxJYFu7jo6UNJXP3yBZbxP2qa6kVdBzcSDRJuKTF8%2F4gfuO99%2B1OMRokXKxeZ%2BSuvnttkLF2jD3tgN2krQ%2B0qpElMPOF0NiOYhq73JNsaxv3pdEKuWNSXtMUKM5rWNF2XggkTDr%2BkzSjwS8Y6XKL2jk6Ss2nYrd4%2BQyA26OX2hfZIbuANupfbkrHHN42YAxfjxyZaM0w5dQewdHFpJ7%2FQeB3%2FSW7vDkIcVOeBfRoFLXMmPjtaMZjn6cNUraiGk%2BesD7lTdwdgeusvSlwekmSk5uVHVJWlX94WPNsF3owo9fuvAY6pgEHUOR3K0xCEtvEDRUgxB7sdlXjtvLoTlbvslftK4HemdhtehgTgJJRa39Bmgra9V9KPtUMwUJbe%2FUp8JlH0Afu8imLo6WNuYu4bCDdsPeOk1CqNaJxTQpgJD1PVVMEIgfnjeastu7QmUs6dgqQvqrDSOdueaS%2B2LK8%2BGq9Fb3o5DnBFyK8wQbR1j2COdEL%2BpIJ2r04cQpFXBaqdXv%2B7VeCa2mKc2dF&X-Amz-Signature=0d6ef2d8adceb16942270b13448b2be01577fe9d114607aa8054e761fe941472&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKHUS4B4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWx3dxyaWLeo3zdFkCMwvkMvt9KnnNK9MBqaX0sGsYAAiBYx%2BACS1fjl9oOe5FWQH3usw9ciwMwZB4BZB4voQipdCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRa7BFw3xjVGn3182KtwD5wYNvCPtzBuYjnHZ208sAoOdgp6IRrDUxLCLeKDW0AcObK8a8Br8RS3aKjxB%2BalirjlNcd37rzD6myABNNJB8VRSKTT8AhxWYDIdF7M%2FneOa5yj6ajx%2FAmTYFL9l8BvoEp4BOpUjIu7fdYg6wRicXSTj7h4JFc3AL785jgGcg18zdCFyTUV4GDGW37%2B%2BGVUVuZcXQEM2vIRkOvPGtIZ1aM6S92YDbh4cV21MVWDE20Af8jsFLKnEGAI37KDm5jBta4hM%2Bgb2YbQ%2BWErSQDjS%2BSQs4Jmy7pFeU3rjEP6QTxT8tAVXH4r5Wswr4JjJLveYvisrtoPvGA7hgRKTI97cAxJYFu7jo6UNJXP3yBZbxP2qa6kVdBzcSDRJuKTF8%2F4gfuO99%2B1OMRokXKxeZ%2BSuvnttkLF2jD3tgN2krQ%2B0qpElMPOF0NiOYhq73JNsaxv3pdEKuWNSXtMUKM5rWNF2XggkTDr%2BkzSjwS8Y6XKL2jk6Ss2nYrd4%2BQyA26OX2hfZIbuANupfbkrHHN42YAxfjxyZaM0w5dQewdHFpJ7%2FQeB3%2FSW7vDkIcVOeBfRoFLXMmPjtaMZjn6cNUraiGk%2BesD7lTdwdgeusvSlwekmSk5uVHVJWlX94WPNsF3owo9fuvAY6pgEHUOR3K0xCEtvEDRUgxB7sdlXjtvLoTlbvslftK4HemdhtehgTgJJRa39Bmgra9V9KPtUMwUJbe%2FUp8JlH0Afu8imLo6WNuYu4bCDdsPeOk1CqNaJxTQpgJD1PVVMEIgfnjeastu7QmUs6dgqQvqrDSOdueaS%2B2LK8%2BGq9Fb3o5DnBFyK8wQbR1j2COdEL%2BpIJ2r04cQpFXBaqdXv%2B7VeCa2mKc2dF&X-Amz-Signature=9cae0ba069e3f4b65eeb83ad39c6683412b8b4c141152784eda55dded69e2dee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKHUS4B4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWx3dxyaWLeo3zdFkCMwvkMvt9KnnNK9MBqaX0sGsYAAiBYx%2BACS1fjl9oOe5FWQH3usw9ciwMwZB4BZB4voQipdCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRa7BFw3xjVGn3182KtwD5wYNvCPtzBuYjnHZ208sAoOdgp6IRrDUxLCLeKDW0AcObK8a8Br8RS3aKjxB%2BalirjlNcd37rzD6myABNNJB8VRSKTT8AhxWYDIdF7M%2FneOa5yj6ajx%2FAmTYFL9l8BvoEp4BOpUjIu7fdYg6wRicXSTj7h4JFc3AL785jgGcg18zdCFyTUV4GDGW37%2B%2BGVUVuZcXQEM2vIRkOvPGtIZ1aM6S92YDbh4cV21MVWDE20Af8jsFLKnEGAI37KDm5jBta4hM%2Bgb2YbQ%2BWErSQDjS%2BSQs4Jmy7pFeU3rjEP6QTxT8tAVXH4r5Wswr4JjJLveYvisrtoPvGA7hgRKTI97cAxJYFu7jo6UNJXP3yBZbxP2qa6kVdBzcSDRJuKTF8%2F4gfuO99%2B1OMRokXKxeZ%2BSuvnttkLF2jD3tgN2krQ%2B0qpElMPOF0NiOYhq73JNsaxv3pdEKuWNSXtMUKM5rWNF2XggkTDr%2BkzSjwS8Y6XKL2jk6Ss2nYrd4%2BQyA26OX2hfZIbuANupfbkrHHN42YAxfjxyZaM0w5dQewdHFpJ7%2FQeB3%2FSW7vDkIcVOeBfRoFLXMmPjtaMZjn6cNUraiGk%2BesD7lTdwdgeusvSlwekmSk5uVHVJWlX94WPNsF3owo9fuvAY6pgEHUOR3K0xCEtvEDRUgxB7sdlXjtvLoTlbvslftK4HemdhtehgTgJJRa39Bmgra9V9KPtUMwUJbe%2FUp8JlH0Afu8imLo6WNuYu4bCDdsPeOk1CqNaJxTQpgJD1PVVMEIgfnjeastu7QmUs6dgqQvqrDSOdueaS%2B2LK8%2BGq9Fb3o5DnBFyK8wQbR1j2COdEL%2BpIJ2r04cQpFXBaqdXv%2B7VeCa2mKc2dF&X-Amz-Signature=e46cc31cee97eda000b4f3d214eee8787fb54c162e2b2e2b6016f226b982f4b0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R35ZJB3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpvjLftKCbxH6DnGlf6OSatfSd28QZOQG4m6TORmrlqgIhAMsororAQnqpzX3nyKBoNPvAAf9wfsAXTHfFZb7CVg4VKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxW0fL1rPwjFNiX%2F9cq3AMmwfaU6eL%2F%2BcaDgl6tkn2qjSeQS7uc4D%2FlnIsL1w8dGpP8pm%2FsczcTO3A2iJwTek7j2HTc0Yb138%2F77mPs9JzL1qdZEx2PcVX8vdp9zHedpazsf7jHof2JTOEB%2FM5iJKH5OPutS4yBLnH7nhuvE2QqTjuznZMs658r25dOu8wMQcDdZuc5T06frUqZuIiLlqWa8GdPurZszQW9FwQpMTA30Uv6WVOZ2HHLYXIQieNwACqjQcIfHY2Dc5mdqYqmueiIbyT8czqEjWdP6OaMNf3wRRyXAswhCxPXNysvASeQMg51JVaVgx02IWOPU%2Fx16NpCTABbDpU53hLuSYkk4KJCD9%2BtLBYKpZ0D8n%2F8P6ID9LM74xYkyEc55N4gvmN5tfEMeWzKJvvXNAbCcYp0SS8xGOfeSyER%2FtXZo%2B0SpveR8dLGP13FpblyyZbUUQUVWm%2BxBC1QHxd59Vr0cafd96%2FPBLS%2B1BQlSqlbUM365Q6Fdisgty0VKRR9Tmb2UdXB%2F%2F4WtAhQbcdNLuSPnwf4zv7VBWo3oyZ8XlhzmdgqpqiVGjNZgJxAYp8UJcuNzhQ9sE7My5UX%2F%2F4rs00NSZVPryAvUeZByh4zhSw9iJaLgWm4MZuFYvY5DRrcqYIwajDP1u68BjqkAZoA0YksxI3RSCoiBHcTh2GltCkHsUlfXTEmDJCeGxpAwcSpKbcnuaktONHfZdNLjnEnNjHzw0siKMQVo1GHRSVkF8X86B%2BsYE54KHl7NJLJNPvbo2yejmQTWVH9IAFnzQM9TLCFtc5i5osI0WWliyAJcRMbEx0eNU93qMFPIUjDT5B%2FCOtDjCIouHPo5kVQZRHdeBFLJsSfOl7bhs5B10YYowaI&X-Amz-Signature=86f83e7de51d7916a23d6c994b7d923e846cd683257ac72713fb59886c994a5d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSQVGNQU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOzcc5dTTo2Hjob84B1yXm2Dc2NwcRlu%2BsklnNOQpiuAIgJof%2FujJZZXj4kSXgiHXweE9zPmQuoTcwE7plICGSaG4qiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeuB2V0VCXverv0sSrcAwDHkDZhdGmK7gecix%2B81MyxXDiMhXe6lXa9Au0iaIuAyWhCnm4zMiTfhg3Hu690HV8XxMQVFfo5kalieItDYWcCa%2BuLaxYyr0WB6gKU7m8gGqJpWH1tWOknZdtsYgnW8stdrAKlFaqDpX5dDnHtjUGh9e%2FKqy1am3X6U%2FDwDZFSuuNZowXOGomyHWaSbmTFp535rp7OmrHqyGwMayj3BwQF%2F5%2FnmYFhohNiosyeNznp2Pi19HoGAS8nz0SKRlQwqyiVrvEdaxwgSHBvpKs1pI498iVX9B2BqC3exL8Mzjx%2BcquWsR7W0ujpIko5hDT1O1MupgeAjDcrPjjfsHVdfFZ3GQyW%2BMfHVMAERztygzHk5f0Xrv%2B04Bl9TFcAXMlUJU6FXWN2saGNFsA%2FEBtUojM6icWdyRaWtww8ZAXvqySSM6XmBNRFqJ7r9oMA28gwDV1Kx%2B9%2FtWYdKB9FGtv3%2Bll9TobCo1BMN78vzoaR6mAOd5ZJs3HDUDJo%2B87m1OxE%2FHERDigvJszQL%2BDR%2BG0pY47SN2yA3ElgOtBPdsalefpYukjVasYHyw1NIYnz0KlQxWP2F4qXA4aF6Ang%2F1f6BWcegx01v0FCNBLd0redVrMC4jcuIlm7TXn0CILSMN3W7rwGOqUBg3qXDQk3i5Zmg%2BSsY%2FzpnR%2F5yY43EFs7b%2FDJ79NFn934m9y3qjSmTsstr4qWsv%2FPQqtmuqK9fWdwNxv3wTxtycXZ0YLvX1IGA2A6CjiWej3qq%2FgmoYvZ1xztIYl5EdG4tQBX1vc%2BpgIFXenj75GF4LtSEHDts20SSRIBd1rEKYy7Ct3WoAua2h6K%2BB6IJi087ZK1TiZE1W01NuXQOOzuQFeyG4LR&X-Amz-Signature=e5fc321429aa0ee28e02aa07e6b69cf67b2cdd74bfaa951cee3724fc61ae452c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKHUS4B4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWx3dxyaWLeo3zdFkCMwvkMvt9KnnNK9MBqaX0sGsYAAiBYx%2BACS1fjl9oOe5FWQH3usw9ciwMwZB4BZB4voQipdCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRa7BFw3xjVGn3182KtwD5wYNvCPtzBuYjnHZ208sAoOdgp6IRrDUxLCLeKDW0AcObK8a8Br8RS3aKjxB%2BalirjlNcd37rzD6myABNNJB8VRSKTT8AhxWYDIdF7M%2FneOa5yj6ajx%2FAmTYFL9l8BvoEp4BOpUjIu7fdYg6wRicXSTj7h4JFc3AL785jgGcg18zdCFyTUV4GDGW37%2B%2BGVUVuZcXQEM2vIRkOvPGtIZ1aM6S92YDbh4cV21MVWDE20Af8jsFLKnEGAI37KDm5jBta4hM%2Bgb2YbQ%2BWErSQDjS%2BSQs4Jmy7pFeU3rjEP6QTxT8tAVXH4r5Wswr4JjJLveYvisrtoPvGA7hgRKTI97cAxJYFu7jo6UNJXP3yBZbxP2qa6kVdBzcSDRJuKTF8%2F4gfuO99%2B1OMRokXKxeZ%2BSuvnttkLF2jD3tgN2krQ%2B0qpElMPOF0NiOYhq73JNsaxv3pdEKuWNSXtMUKM5rWNF2XggkTDr%2BkzSjwS8Y6XKL2jk6Ss2nYrd4%2BQyA26OX2hfZIbuANupfbkrHHN42YAxfjxyZaM0w5dQewdHFpJ7%2FQeB3%2FSW7vDkIcVOeBfRoFLXMmPjtaMZjn6cNUraiGk%2BesD7lTdwdgeusvSlwekmSk5uVHVJWlX94WPNsF3owo9fuvAY6pgEHUOR3K0xCEtvEDRUgxB7sdlXjtvLoTlbvslftK4HemdhtehgTgJJRa39Bmgra9V9KPtUMwUJbe%2FUp8JlH0Afu8imLo6WNuYu4bCDdsPeOk1CqNaJxTQpgJD1PVVMEIgfnjeastu7QmUs6dgqQvqrDSOdueaS%2B2LK8%2BGq9Fb3o5DnBFyK8wQbR1j2COdEL%2BpIJ2r04cQpFXBaqdXv%2B7VeCa2mKc2dF&X-Amz-Signature=ac3f36e17ef1a9bdcbe4c3c1dbabf9266cbfd754da88a011afa64e34d6869307&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKHUS4B4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWx3dxyaWLeo3zdFkCMwvkMvt9KnnNK9MBqaX0sGsYAAiBYx%2BACS1fjl9oOe5FWQH3usw9ciwMwZB4BZB4voQipdCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRa7BFw3xjVGn3182KtwD5wYNvCPtzBuYjnHZ208sAoOdgp6IRrDUxLCLeKDW0AcObK8a8Br8RS3aKjxB%2BalirjlNcd37rzD6myABNNJB8VRSKTT8AhxWYDIdF7M%2FneOa5yj6ajx%2FAmTYFL9l8BvoEp4BOpUjIu7fdYg6wRicXSTj7h4JFc3AL785jgGcg18zdCFyTUV4GDGW37%2B%2BGVUVuZcXQEM2vIRkOvPGtIZ1aM6S92YDbh4cV21MVWDE20Af8jsFLKnEGAI37KDm5jBta4hM%2Bgb2YbQ%2BWErSQDjS%2BSQs4Jmy7pFeU3rjEP6QTxT8tAVXH4r5Wswr4JjJLveYvisrtoPvGA7hgRKTI97cAxJYFu7jo6UNJXP3yBZbxP2qa6kVdBzcSDRJuKTF8%2F4gfuO99%2B1OMRokXKxeZ%2BSuvnttkLF2jD3tgN2krQ%2B0qpElMPOF0NiOYhq73JNsaxv3pdEKuWNSXtMUKM5rWNF2XggkTDr%2BkzSjwS8Y6XKL2jk6Ss2nYrd4%2BQyA26OX2hfZIbuANupfbkrHHN42YAxfjxyZaM0w5dQewdHFpJ7%2FQeB3%2FSW7vDkIcVOeBfRoFLXMmPjtaMZjn6cNUraiGk%2BesD7lTdwdgeusvSlwekmSk5uVHVJWlX94WPNsF3owo9fuvAY6pgEHUOR3K0xCEtvEDRUgxB7sdlXjtvLoTlbvslftK4HemdhtehgTgJJRa39Bmgra9V9KPtUMwUJbe%2FUp8JlH0Afu8imLo6WNuYu4bCDdsPeOk1CqNaJxTQpgJD1PVVMEIgfnjeastu7QmUs6dgqQvqrDSOdueaS%2B2LK8%2BGq9Fb3o5DnBFyK8wQbR1j2COdEL%2BpIJ2r04cQpFXBaqdXv%2B7VeCa2mKc2dF&X-Amz-Signature=43ad082cfc08e74560115c9fd160bd63b04d635750bff5320033f78e4e46f272&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKHUS4B4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWx3dxyaWLeo3zdFkCMwvkMvt9KnnNK9MBqaX0sGsYAAiBYx%2BACS1fjl9oOe5FWQH3usw9ciwMwZB4BZB4voQipdCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRa7BFw3xjVGn3182KtwD5wYNvCPtzBuYjnHZ208sAoOdgp6IRrDUxLCLeKDW0AcObK8a8Br8RS3aKjxB%2BalirjlNcd37rzD6myABNNJB8VRSKTT8AhxWYDIdF7M%2FneOa5yj6ajx%2FAmTYFL9l8BvoEp4BOpUjIu7fdYg6wRicXSTj7h4JFc3AL785jgGcg18zdCFyTUV4GDGW37%2B%2BGVUVuZcXQEM2vIRkOvPGtIZ1aM6S92YDbh4cV21MVWDE20Af8jsFLKnEGAI37KDm5jBta4hM%2Bgb2YbQ%2BWErSQDjS%2BSQs4Jmy7pFeU3rjEP6QTxT8tAVXH4r5Wswr4JjJLveYvisrtoPvGA7hgRKTI97cAxJYFu7jo6UNJXP3yBZbxP2qa6kVdBzcSDRJuKTF8%2F4gfuO99%2B1OMRokXKxeZ%2BSuvnttkLF2jD3tgN2krQ%2B0qpElMPOF0NiOYhq73JNsaxv3pdEKuWNSXtMUKM5rWNF2XggkTDr%2BkzSjwS8Y6XKL2jk6Ss2nYrd4%2BQyA26OX2hfZIbuANupfbkrHHN42YAxfjxyZaM0w5dQewdHFpJ7%2FQeB3%2FSW7vDkIcVOeBfRoFLXMmPjtaMZjn6cNUraiGk%2BesD7lTdwdgeusvSlwekmSk5uVHVJWlX94WPNsF3owo9fuvAY6pgEHUOR3K0xCEtvEDRUgxB7sdlXjtvLoTlbvslftK4HemdhtehgTgJJRa39Bmgra9V9KPtUMwUJbe%2FUp8JlH0Afu8imLo6WNuYu4bCDdsPeOk1CqNaJxTQpgJD1PVVMEIgfnjeastu7QmUs6dgqQvqrDSOdueaS%2B2LK8%2BGq9Fb3o5DnBFyK8wQbR1j2COdEL%2BpIJ2r04cQpFXBaqdXv%2B7VeCa2mKc2dF&X-Amz-Signature=260ef77ad152036bb7e07d87a6fd5cb30851e21e6a5ae4283180ebf17be54eb8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GCRSSTD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiGMRVBLDhVDMUXucSgd7YuM5oPSHMOlOc%2F%2FRyhtkaVAIhAOBFntQTULinpXBdXXaYegHnCIIcORc98pS0VGjoFCD3KogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjnivUgy%2BYLfPcrK0q3AMqy1NnDAa4rEg3wN%2FnG8Y50nX4UBIeCLofhS1p9007uVNYHM5mjk0ORlFKwyG%2Bg7FxHY%2BnCc6nHCrHhxqIw0Ya3Hq8pzOQ4RZWQ9eI3QrZbZJXkXgoIazNA542KMYgb9wX6kK7TKZj8WjjkpMuFRMNGUwIcSzbkXMso%2BgMGBvdY2S3jOy6BdNzPWGQGAy2uV0AH%2Fysfqcbp7%2FBM7l6Rz4jZLKsWPw6MXTLM1dc9Nj4GQRworXBxL0yxNsXlF2js9QjtbvWHGh1C%2FFCJTCy7d85QFsuK3gr%2BgWv92ZL86jgwKh%2FfLtT70yD3PbUqqzzq%2Fh8gXuKXVGQGGXsJ%2FzFvEPtDup14RqURo5Q8%2F%2FzB2ynZo7YGOJlm1a1BGNYypF5xc5LahH1KRn7weF87ykjLACdAG7ofOC7NLKCngV2ztCuXxXd%2B%2BJ84An4cgoby%2BN0JkaQlnTALuj3AUzU1aQFOQLl2%2FQg2ecEbIu4j33b1%2BwEIbZ6NVMYmEN40s1GbvQI2P8Lv%2BwZ2RSc8PsP%2BoyLyzDDEHwV2O2qF6zcCBk0oZ%2Fy%2BTUgZEwUJgRH%2BcKyES4grDiSPSBxg%2BIoDhP8gb0OOda5wdfIKf%2BHvH%2BDqXHTszliupN5q3ii3CqpfmZHKTDD1u68BjqkAcweYOEt1n7cKwedinyROzHCio5KKLXA4nKar0vSoYVG7sySB1mkrmFvVrjDwlYgKvQA%2BFiC44zgLOgXwmkQ%2FTjTkoy4TP7oF3OeBNrfPExqzau5OpoZ7BEjZj99uegmH2vqYiQGd4xVvfMgcGJbeUPBDBxipX24KbEB%2F6EWwPAsxYAKLcqfSMtcQKh0rZtE4tXVzQZRk366VGXvQtU6yJNi99Yc&X-Amz-Signature=02b3e4533dc419fcc8431e372ad2140c60ca4db2b67530af1c672e34ac4e6375&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6OSBLLU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFIKQBwxBEgmyK5bU5ZO%2B5rp82rnNVK2V9Ef9MSpjMYAiEA4FJVAm%2BeOzzTHNXXjS9cRSWb1cepqp1MNeHb6%2B6lKSYqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwwD%2FUdQ9%2B9EidwgCrcA69%2BFBUJOMKW8q2I0%2B5zEh90WStsCd0v1n6BwrDj1L5AaK6FXB1JF91c8fI%2FGfGAU1o9tQu8VQlNG%2B6LldyfrQfTIN%2BTV%2BwioXDYFCUgmR3M5uwxBEaUszzkm3%2Bfi3Q8KpmH0AJ8AnF5nqSNtxIb05nn7npj6gQ7zWLPsO%2BWLymRYv8VwNK%2BmfgWlCby3XV6J%2FEgJO66fxSs0GS8ofg7MI84Osp0gGJn4wbRRzH96mMQzFaKS7msPJmEqAckzLv2%2FX0h7CuOYxRQZZpPQEvb2pZzRFGIp3M1xHxB%2Fs5iX58B7T%2ByHx08I%2Bc2PgwFzbtBCqHI2UEERinN0G%2F7C%2BHHpG1%2F4mDmjFPfu94zZ9pa%2BDWi6JaHNFpwclHNKT%2FYRflJlvcPlDY05eKK1z8qD3VrSECeeN5yRh7zaLnPTRBKwJhBGXyCgnxhn2PpyRBpv%2Feqhs0oYshspuS8%2B0u3vxUIY4X8KGpbT8Z4hnPHD1D4v3Wu3xqcHcUnoc6s1SgYg9t8C22oOO7X2mmBF7ZhDXPn1rncAny8mxpUXnHs%2FOKhZryH62uGG2L50PxUVV0c0EBULVGDqfIVG2ySzLmbFgLwl76rsSDeQpnyfIgnpTIpzzI3dp8iUkTYLovqvpf3MLDX7rwGOqUB%2BfkUQwjIj9TbDfeBg%2F7bYLNLeleDTbfKdwB6Hszu9w%2Fd4hQn45k%2BpGgjQWlg9Er7EI4H%2BaHIK1hz8FG7zWtf4UEmNUG%2BlV8dLTHslupaORWs1G2gBO6%2BH8gzMqVZAPH%2BJAlciAaWH7FWZOzsoLVKJDo5oHZDcW1FuHkkwCg9Uz%2FCMDPl28cB6oUsISLtmoOagZYOkFH%2FAlA2H4paT3iAaX42dqdt&X-Amz-Signature=463c65cb75a539d1cc918feacde4dd237fcbcd9c7ee078992bccb867ad3f421b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSDFSRWF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnU9kzEPvfrwiXdVBBYRGjHB6efEkhZrbRdpqQP%2FCiFwIgCHnkWBkg0qZoclZTuyHSezIAtHeiMMxZx6ze9tzSrLYqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC5KhYtnE6bKoa%2FqvSrcAwKg3qMUfKbXEp%2BJsIHp2B4OMszOhNXhIZx8%2F9FyeRVPDPQ7ukWfEttyWl%2F9YUeWqHGDcVbxY2grajSo8XkYXsx%2F2Hm%2BUCK9TMxj2z7%2F0Y8Ju6W4Wr%2FobidnD6gZA528THBCKTt3lK0CpaaG8pm7vIFpfSNM5ekwmzCdxehHnnfMS6woO3kCyXqkBNDwOlCcDQuBMRCHes1IZHrQ13AF8JsFFupu2FGfLteYurcHnx%2BHi8Okq8eiJKAdyn04bPEDg2e07xsdFOrWDqjNu6w2mqFCDWT2WMjVBGzGdDws2a0BSshmGiL2IWHwFxykFNZVNM052NS2qIIeMhWk%2B3n1RTfNK%2F9Nxyo8NCu%2BlqPDBCfw0bQoXXkrPoQm5egSax%2BZLEEQhEBr1SNb5eku4CA0moY2burWW5Y%2BMdLCV0y%2B0P67YlXT%2FPKP9RoOzU%2FZNLGQBljFcf%2Fn%2FkbTnMj2jI7xIfpP8PtGykbNkHYGoYyiVmVz6NIbqY%2BYABGbGu33tSQF7yBT%2FxGokxfLqSLMgW19RBbBTuTObTTpxWYGkVM83KIyAuEac1uZf42c3AL3To2micaoZX9CbMDq64nHiSxhY1Mqaz44AaXAXNgTdiPXd5lAzcsr%2BCz8a8Y85%2BKLMN7W7rwGOqUBvQSSvGuWjJzhtaDiOtg5Zus6S8cqIZ5StuVmzJHgPMDGcZl7%2B9LFevDLFv8nkQpcoZ0ZcmGbLDyk9kafZ23cZDa7chHLYaH%2Fh7a8mqKnjPg8IQtOunUGY9N75yGdDZ6Qos%2BgCEsdB9M4I6Q2GjnEENT%2Bk9EWk6Qwi8nQnxt3yJRnKKMyLLBciCz2FZY5lnONpCmpFBPbjOH514IpeqYoEi%2BsHsYx&X-Amz-Signature=8bf91dd20fbe0b4a043de7c5b1d81b8b51c76b6b871a15ca0fe85ea2353b27f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EF6YEEA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAesSrbhNwkhg8ZFAsz%2B7D4DoFPCPTpV0yZ0KSnPyBVGAiBLNtypISQ2kRIAgO9IknRQhviLiNovR3ROnT9ga2%2BkHSqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgk%2F3n%2F69su80l57dKtwDIFBivpsxl%2Fx2NLlk2FHZoeLkx9thjn4V5Tm%2F0vlfcotsNWeAfcnNayUqUn17HYAdpoffed9MMq52XZnv98%2F3boM0RXY56CBgvHnSYNZrNb0zY83y1%2FA0uBZDL81RW9PjqCfVXwF1h8RmYLHLmqxfn2oRSh9Tc3xIWxc5%2FJxr%2BE4lWK24AnlSs1cxUwnRZnJKGNUq8pWPrlB0CC1kqxmBKd1NypBGXbVHcJ4DYnj6IBYNEwiVay1AorANO03dVUxh9bI%2B%2B%2FVvklwOkLXdISgT7Vw7NXjIESJN7Yvunf%2FImkWTeo5%2B3ciWp%2FzS8ePNJSsD8c5H67GcrG9K9uH%2B1p2Ppngae8Q8KmP7%2FA%2BpKjhx0uYrrJWl3k1q2cazXdZ%2BlR2eJ9iWm6dGy4HokLywfjDfgpk6WtgyLpi99MNcTlLr6AeRrkfdAFTM3m0qKmXZ%2FTFBelYD%2BIZYU8EwPweWiuju88uHYNGNKAMGkG%2F8UNR89PFH%2FNIe11r5Um5lIHOyVh58GLUlB4v%2Bg6FBeIN%2Fwas1YHzkD%2BBQAkbrMQ6%2FHhjt832l8KsguYIwi3b8V9HStNDuOATTm1SAz4w%2FEavKqMRS0esilD3M2maO7QPMqt90eBa4I5utwxZ74I7BT8cww9buvAY6pgG8e46zxJ8yIyZEqVCy2WXEYWeNBmqSmuFDEc6Hgn70P9DiWTjjx%2B3Bw3p3GOfn9ncJNfQDq9hhYor4SaV41rkaBwytqLF4xwxCbVUuAry6fvfX33vQEXUO9gfJUXWLw%2BGtz%2BhD0kFtOdKzY7LqiJdV176aXA8wpxXO9h0AAW8pIviVvdX3e%2FO1KKIDgf3d3YXO5XuPk9yTVBHVrHhB5eB0swnbXtyH&X-Amz-Signature=2153a0c56cbd069766a285447d31c7fee6df03b3727e35e959a4d7b90c282ede&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EF6YEEA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAesSrbhNwkhg8ZFAsz%2B7D4DoFPCPTpV0yZ0KSnPyBVGAiBLNtypISQ2kRIAgO9IknRQhviLiNovR3ROnT9ga2%2BkHSqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgk%2F3n%2F69su80l57dKtwDIFBivpsxl%2Fx2NLlk2FHZoeLkx9thjn4V5Tm%2F0vlfcotsNWeAfcnNayUqUn17HYAdpoffed9MMq52XZnv98%2F3boM0RXY56CBgvHnSYNZrNb0zY83y1%2FA0uBZDL81RW9PjqCfVXwF1h8RmYLHLmqxfn2oRSh9Tc3xIWxc5%2FJxr%2BE4lWK24AnlSs1cxUwnRZnJKGNUq8pWPrlB0CC1kqxmBKd1NypBGXbVHcJ4DYnj6IBYNEwiVay1AorANO03dVUxh9bI%2B%2B%2FVvklwOkLXdISgT7Vw7NXjIESJN7Yvunf%2FImkWTeo5%2B3ciWp%2FzS8ePNJSsD8c5H67GcrG9K9uH%2B1p2Ppngae8Q8KmP7%2FA%2BpKjhx0uYrrJWl3k1q2cazXdZ%2BlR2eJ9iWm6dGy4HokLywfjDfgpk6WtgyLpi99MNcTlLr6AeRrkfdAFTM3m0qKmXZ%2FTFBelYD%2BIZYU8EwPweWiuju88uHYNGNKAMGkG%2F8UNR89PFH%2FNIe11r5Um5lIHOyVh58GLUlB4v%2Bg6FBeIN%2Fwas1YHzkD%2BBQAkbrMQ6%2FHhjt832l8KsguYIwi3b8V9HStNDuOATTm1SAz4w%2FEavKqMRS0esilD3M2maO7QPMqt90eBa4I5utwxZ74I7BT8cww9buvAY6pgG8e46zxJ8yIyZEqVCy2WXEYWeNBmqSmuFDEc6Hgn70P9DiWTjjx%2B3Bw3p3GOfn9ncJNfQDq9hhYor4SaV41rkaBwytqLF4xwxCbVUuAry6fvfX33vQEXUO9gfJUXWLw%2BGtz%2BhD0kFtOdKzY7LqiJdV176aXA8wpxXO9h0AAW8pIviVvdX3e%2FO1KKIDgf3d3YXO5XuPk9yTVBHVrHhB5eB0swnbXtyH&X-Amz-Signature=b047bef2f3e507da82e495f4b20a6079ba88ea4c6451bc1b34cd4c6b9c4abe15&X-Amz-SignedHeaders=host&x-id=GetObject)

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
