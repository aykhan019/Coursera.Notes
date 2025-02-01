

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WT65YZ7K%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCp7JvWkwkPDaMhNOOsPyRbgJ%2FPPsm%2FIoJaFPjr5HHjnwIhAJA9cpjlZge0dHrd9hlJ%2Bbjrx%2Fzxo4aoWUwNTcAzCo7qKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSEj6DWuuUA93FxfUq3AO6h3z16xhfdQOFgSvud7w4izx7CW17Gb7kgs%2FFHlIyOseMBBtuJOjvbu%2FYKFgUxz7GKBuZDceUddg6QLXDZiBM8JKuKJMbFgyCUQWc6%2BrjGNtU89n3y%2BLVWhtVmcj6%2B6hsDK3ihW2%2FhiDB89bsMUi9M3xUcuxvXZP05iXF%2FG2%2FRR3viVMbH8n0cnJpx9M6xK%2FNyM5jd4Yz%2Fv33wDC2kYB3%2BJf3XkvPHKF8gEwUh%2BYPHKtuC6KYiMMecXc%2BZwbybEEQdQLxhYY4ARY3yZuhfazmLYbdplsOAmF6NWqggppRMN60KTz5ePlYjjz5NMsoUgc01rMjbbPoqCBhQjJtfMmm1qZDU5nmw1gCeuWLgBGuARSuNEQXlMss%2BLHb%2BmAnusKQsj0NrnsCZZEt15sOFlGExUfXo6f2TI%2BzK8K8MHfwN9Y0gg%2FhD1ZsNyG8RFMsADIMN9qHp9Ycxgog2nNZ6Mc%2BG2KTHP1M%2FhbGmb8Qq4wntDvrEx0yEmM6zcq2drkuLyOVZpNu0%2F7YdzoYfQ%2BPerM7dhKNZuE2AVTrt3pD7oci9YrWgCn2LXrpUahVxiRH0wp7ASeNZkoL5gYxsNuttDjCZIx%2FzwnjZSwxZ5pP%2BW7q37511c62i4GyevgOyDDg%2Bfa8BjqkAZleQ4j2rcGGcqYcxa5UQEegEKtEgzsCBWm2z4GPVDHitT%2FQhaBwFAummLESjJxAAv6TLLU8h1udyTDBMLyvvNHmnUYvBuENt1qoG2zCsodA876K3JIFVmy%2Fkxo68Lr%2BiK1oIdxpYJ0HagumGkEzBt9ReIHEKasY1AV7K3PXlqQNIy5NZx%2Bl4hxzYuOQNp%2B%2Fph3%2FICtBILQmzIqTa0b9o0y4Hb5k&X-Amz-Signature=142e3b70e068a4a6b4be8cee17fd341612dc57aceca518ab8493ab95ff701907&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WT65YZ7K%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCp7JvWkwkPDaMhNOOsPyRbgJ%2FPPsm%2FIoJaFPjr5HHjnwIhAJA9cpjlZge0dHrd9hlJ%2Bbjrx%2Fzxo4aoWUwNTcAzCo7qKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSEj6DWuuUA93FxfUq3AO6h3z16xhfdQOFgSvud7w4izx7CW17Gb7kgs%2FFHlIyOseMBBtuJOjvbu%2FYKFgUxz7GKBuZDceUddg6QLXDZiBM8JKuKJMbFgyCUQWc6%2BrjGNtU89n3y%2BLVWhtVmcj6%2B6hsDK3ihW2%2FhiDB89bsMUi9M3xUcuxvXZP05iXF%2FG2%2FRR3viVMbH8n0cnJpx9M6xK%2FNyM5jd4Yz%2Fv33wDC2kYB3%2BJf3XkvPHKF8gEwUh%2BYPHKtuC6KYiMMecXc%2BZwbybEEQdQLxhYY4ARY3yZuhfazmLYbdplsOAmF6NWqggppRMN60KTz5ePlYjjz5NMsoUgc01rMjbbPoqCBhQjJtfMmm1qZDU5nmw1gCeuWLgBGuARSuNEQXlMss%2BLHb%2BmAnusKQsj0NrnsCZZEt15sOFlGExUfXo6f2TI%2BzK8K8MHfwN9Y0gg%2FhD1ZsNyG8RFMsADIMN9qHp9Ycxgog2nNZ6Mc%2BG2KTHP1M%2FhbGmb8Qq4wntDvrEx0yEmM6zcq2drkuLyOVZpNu0%2F7YdzoYfQ%2BPerM7dhKNZuE2AVTrt3pD7oci9YrWgCn2LXrpUahVxiRH0wp7ASeNZkoL5gYxsNuttDjCZIx%2FzwnjZSwxZ5pP%2BW7q37511c62i4GyevgOyDDg%2Bfa8BjqkAZleQ4j2rcGGcqYcxa5UQEegEKtEgzsCBWm2z4GPVDHitT%2FQhaBwFAummLESjJxAAv6TLLU8h1udyTDBMLyvvNHmnUYvBuENt1qoG2zCsodA876K3JIFVmy%2Fkxo68Lr%2BiK1oIdxpYJ0HagumGkEzBt9ReIHEKasY1AV7K3PXlqQNIy5NZx%2Bl4hxzYuOQNp%2B%2Fph3%2FICtBILQmzIqTa0b9o0y4Hb5k&X-Amz-Signature=557f0a4b44c95b90f72273e7ac3a369ad6bc358e9bca28b270077625b0454aeb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WT65YZ7K%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCp7JvWkwkPDaMhNOOsPyRbgJ%2FPPsm%2FIoJaFPjr5HHjnwIhAJA9cpjlZge0dHrd9hlJ%2Bbjrx%2Fzxo4aoWUwNTcAzCo7qKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSEj6DWuuUA93FxfUq3AO6h3z16xhfdQOFgSvud7w4izx7CW17Gb7kgs%2FFHlIyOseMBBtuJOjvbu%2FYKFgUxz7GKBuZDceUddg6QLXDZiBM8JKuKJMbFgyCUQWc6%2BrjGNtU89n3y%2BLVWhtVmcj6%2B6hsDK3ihW2%2FhiDB89bsMUi9M3xUcuxvXZP05iXF%2FG2%2FRR3viVMbH8n0cnJpx9M6xK%2FNyM5jd4Yz%2Fv33wDC2kYB3%2BJf3XkvPHKF8gEwUh%2BYPHKtuC6KYiMMecXc%2BZwbybEEQdQLxhYY4ARY3yZuhfazmLYbdplsOAmF6NWqggppRMN60KTz5ePlYjjz5NMsoUgc01rMjbbPoqCBhQjJtfMmm1qZDU5nmw1gCeuWLgBGuARSuNEQXlMss%2BLHb%2BmAnusKQsj0NrnsCZZEt15sOFlGExUfXo6f2TI%2BzK8K8MHfwN9Y0gg%2FhD1ZsNyG8RFMsADIMN9qHp9Ycxgog2nNZ6Mc%2BG2KTHP1M%2FhbGmb8Qq4wntDvrEx0yEmM6zcq2drkuLyOVZpNu0%2F7YdzoYfQ%2BPerM7dhKNZuE2AVTrt3pD7oci9YrWgCn2LXrpUahVxiRH0wp7ASeNZkoL5gYxsNuttDjCZIx%2FzwnjZSwxZ5pP%2BW7q37511c62i4GyevgOyDDg%2Bfa8BjqkAZleQ4j2rcGGcqYcxa5UQEegEKtEgzsCBWm2z4GPVDHitT%2FQhaBwFAummLESjJxAAv6TLLU8h1udyTDBMLyvvNHmnUYvBuENt1qoG2zCsodA876K3JIFVmy%2Fkxo68Lr%2BiK1oIdxpYJ0HagumGkEzBt9ReIHEKasY1AV7K3PXlqQNIy5NZx%2Bl4hxzYuOQNp%2B%2Fph3%2FICtBILQmzIqTa0b9o0y4Hb5k&X-Amz-Signature=a48b9d8a6128945350dc2e792f46f48a2326c6f0edbf582ff77c982561a29fb9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UV6DHM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCahQkfrmzQhKMAASPkUqSB3c1T9OtqEm1h8v6jKWnWEwIhAO%2BrxBfryF2NdCE2jqiX9ozRD4WCZtkJNnjVer%2FfQv%2BFKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx257eIZkB8uvu90mYq3ANsEQG0rWmBD%2FCbH3VTWdRSzbZH%2BO%2BIZOaX5vSwQeowIHO9%2BsvXwhHfNUCfIEVY7JhaYHCQy5yDS%2FYbficpfa6OHyetPvH0gQCj069%2FbDPoB1bYhbiWNtqXSzA6Ti7d216yVlV%2F8nUpaq8oZ0l3zHqZW8CwgxKEz5DFLQHZP8Kq4lDdNRp1MI1DdNkJo7DrWIQrmN%2Fd%2F%2BbtzM76OybGtsp%2BS960DpBDtw2W7GMf7qy1aTwR0ZjAmRzztYSzZQ6y%2BInD1e6PgRoFCX37DwRFqsbxPUQUOeBOpEPK0mQ9%2BjAmqjF%2BKr%2BZ%2BzmEn7G4UUvdT4ZrWsRAV%2FM26cW5NgTZ%2BRJGt7VyYmke4sIRS3PN7IAYj6qBQfIHcMHn8UFzvSPbPyv1V8Nf%2BWYX%2BuHr9L4qLid%2Bkvaf9H769zDea1kEE6k3CHOlSFuPqCvpw38e7dQ%2FYbC9P5c5UCHOYIIXKdIkbSQ%2FA0KUCeEQMbRNaoVqBo4GNDlQPxC0gmDKQFz9IadHbNE81UYZXpWusgx2kRkGE1D7%2BnJb3PV3Ofd%2B5mIq9uNMNqpsEwXNqqusHu7w7dzLdIImr8YZz48SlI%2B189URirJVtx23vp9X2FhJkg54bL1mBsJzx4i6gRVq3YAM3TDb%2Bfa8BjqkAVbX%2FRn0n54dnB4FWq46OZrw3sxOfmgFG5VM4KkhuHQflZ3LI6VV4q7%2BLAVQ3n2CeuR4M2V42%2Bj5T%2Fj8FVn%2B3a7J%2F0FSaLJ%2BkbuDW6MsxtF88ssulRzMmPZmmCDXQlCoMvXlr0GnCceauZornUhQAoPQULeu0DO6CVz%2B7mcwVGQfOPRNZqK2r11OVrqO%2BGIwKcWj0A1eDuVw%2FGaVvbUVQg21GRIF&X-Amz-Signature=e38045df031b98ae72dc09e08db61748dcbd6a4ce5d4623986f9d5f941f274cc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UV6DHM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCahQkfrmzQhKMAASPkUqSB3c1T9OtqEm1h8v6jKWnWEwIhAO%2BrxBfryF2NdCE2jqiX9ozRD4WCZtkJNnjVer%2FfQv%2BFKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx257eIZkB8uvu90mYq3ANsEQG0rWmBD%2FCbH3VTWdRSzbZH%2BO%2BIZOaX5vSwQeowIHO9%2BsvXwhHfNUCfIEVY7JhaYHCQy5yDS%2FYbficpfa6OHyetPvH0gQCj069%2FbDPoB1bYhbiWNtqXSzA6Ti7d216yVlV%2F8nUpaq8oZ0l3zHqZW8CwgxKEz5DFLQHZP8Kq4lDdNRp1MI1DdNkJo7DrWIQrmN%2Fd%2F%2BbtzM76OybGtsp%2BS960DpBDtw2W7GMf7qy1aTwR0ZjAmRzztYSzZQ6y%2BInD1e6PgRoFCX37DwRFqsbxPUQUOeBOpEPK0mQ9%2BjAmqjF%2BKr%2BZ%2BzmEn7G4UUvdT4ZrWsRAV%2FM26cW5NgTZ%2BRJGt7VyYmke4sIRS3PN7IAYj6qBQfIHcMHn8UFzvSPbPyv1V8Nf%2BWYX%2BuHr9L4qLid%2Bkvaf9H769zDea1kEE6k3CHOlSFuPqCvpw38e7dQ%2FYbC9P5c5UCHOYIIXKdIkbSQ%2FA0KUCeEQMbRNaoVqBo4GNDlQPxC0gmDKQFz9IadHbNE81UYZXpWusgx2kRkGE1D7%2BnJb3PV3Ofd%2B5mIq9uNMNqpsEwXNqqusHu7w7dzLdIImr8YZz48SlI%2B189URirJVtx23vp9X2FhJkg54bL1mBsJzx4i6gRVq3YAM3TDb%2Bfa8BjqkAVbX%2FRn0n54dnB4FWq46OZrw3sxOfmgFG5VM4KkhuHQflZ3LI6VV4q7%2BLAVQ3n2CeuR4M2V42%2Bj5T%2Fj8FVn%2B3a7J%2F0FSaLJ%2BkbuDW6MsxtF88ssulRzMmPZmmCDXQlCoMvXlr0GnCceauZornUhQAoPQULeu0DO6CVz%2B7mcwVGQfOPRNZqK2r11OVrqO%2BGIwKcWj0A1eDuVw%2FGaVvbUVQg21GRIF&X-Amz-Signature=76027717b55f87a90cecb06f05b03abc26af56948cfbc3558dd5631b5697bf1b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UV6DHM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCahQkfrmzQhKMAASPkUqSB3c1T9OtqEm1h8v6jKWnWEwIhAO%2BrxBfryF2NdCE2jqiX9ozRD4WCZtkJNnjVer%2FfQv%2BFKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx257eIZkB8uvu90mYq3ANsEQG0rWmBD%2FCbH3VTWdRSzbZH%2BO%2BIZOaX5vSwQeowIHO9%2BsvXwhHfNUCfIEVY7JhaYHCQy5yDS%2FYbficpfa6OHyetPvH0gQCj069%2FbDPoB1bYhbiWNtqXSzA6Ti7d216yVlV%2F8nUpaq8oZ0l3zHqZW8CwgxKEz5DFLQHZP8Kq4lDdNRp1MI1DdNkJo7DrWIQrmN%2Fd%2F%2BbtzM76OybGtsp%2BS960DpBDtw2W7GMf7qy1aTwR0ZjAmRzztYSzZQ6y%2BInD1e6PgRoFCX37DwRFqsbxPUQUOeBOpEPK0mQ9%2BjAmqjF%2BKr%2BZ%2BzmEn7G4UUvdT4ZrWsRAV%2FM26cW5NgTZ%2BRJGt7VyYmke4sIRS3PN7IAYj6qBQfIHcMHn8UFzvSPbPyv1V8Nf%2BWYX%2BuHr9L4qLid%2Bkvaf9H769zDea1kEE6k3CHOlSFuPqCvpw38e7dQ%2FYbC9P5c5UCHOYIIXKdIkbSQ%2FA0KUCeEQMbRNaoVqBo4GNDlQPxC0gmDKQFz9IadHbNE81UYZXpWusgx2kRkGE1D7%2BnJb3PV3Ofd%2B5mIq9uNMNqpsEwXNqqusHu7w7dzLdIImr8YZz48SlI%2B189URirJVtx23vp9X2FhJkg54bL1mBsJzx4i6gRVq3YAM3TDb%2Bfa8BjqkAVbX%2FRn0n54dnB4FWq46OZrw3sxOfmgFG5VM4KkhuHQflZ3LI6VV4q7%2BLAVQ3n2CeuR4M2V42%2Bj5T%2Fj8FVn%2B3a7J%2F0FSaLJ%2BkbuDW6MsxtF88ssulRzMmPZmmCDXQlCoMvXlr0GnCceauZornUhQAoPQULeu0DO6CVz%2B7mcwVGQfOPRNZqK2r11OVrqO%2BGIwKcWj0A1eDuVw%2FGaVvbUVQg21GRIF&X-Amz-Signature=d2a4307aea150b201aa8b22cda42c7970271ec01cbe5161096a2460edd28dbea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UV6DHM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCahQkfrmzQhKMAASPkUqSB3c1T9OtqEm1h8v6jKWnWEwIhAO%2BrxBfryF2NdCE2jqiX9ozRD4WCZtkJNnjVer%2FfQv%2BFKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx257eIZkB8uvu90mYq3ANsEQG0rWmBD%2FCbH3VTWdRSzbZH%2BO%2BIZOaX5vSwQeowIHO9%2BsvXwhHfNUCfIEVY7JhaYHCQy5yDS%2FYbficpfa6OHyetPvH0gQCj069%2FbDPoB1bYhbiWNtqXSzA6Ti7d216yVlV%2F8nUpaq8oZ0l3zHqZW8CwgxKEz5DFLQHZP8Kq4lDdNRp1MI1DdNkJo7DrWIQrmN%2Fd%2F%2BbtzM76OybGtsp%2BS960DpBDtw2W7GMf7qy1aTwR0ZjAmRzztYSzZQ6y%2BInD1e6PgRoFCX37DwRFqsbxPUQUOeBOpEPK0mQ9%2BjAmqjF%2BKr%2BZ%2BzmEn7G4UUvdT4ZrWsRAV%2FM26cW5NgTZ%2BRJGt7VyYmke4sIRS3PN7IAYj6qBQfIHcMHn8UFzvSPbPyv1V8Nf%2BWYX%2BuHr9L4qLid%2Bkvaf9H769zDea1kEE6k3CHOlSFuPqCvpw38e7dQ%2FYbC9P5c5UCHOYIIXKdIkbSQ%2FA0KUCeEQMbRNaoVqBo4GNDlQPxC0gmDKQFz9IadHbNE81UYZXpWusgx2kRkGE1D7%2BnJb3PV3Ofd%2B5mIq9uNMNqpsEwXNqqusHu7w7dzLdIImr8YZz48SlI%2B189URirJVtx23vp9X2FhJkg54bL1mBsJzx4i6gRVq3YAM3TDb%2Bfa8BjqkAVbX%2FRn0n54dnB4FWq46OZrw3sxOfmgFG5VM4KkhuHQflZ3LI6VV4q7%2BLAVQ3n2CeuR4M2V42%2Bj5T%2Fj8FVn%2B3a7J%2F0FSaLJ%2BkbuDW6MsxtF88ssulRzMmPZmmCDXQlCoMvXlr0GnCceauZornUhQAoPQULeu0DO6CVz%2B7mcwVGQfOPRNZqK2r11OVrqO%2BGIwKcWj0A1eDuVw%2FGaVvbUVQg21GRIF&X-Amz-Signature=ac9950dac7438224a69ccc2431d646c48e9088cfcff2e2cc7e06a75ceac8151c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UV6DHM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCahQkfrmzQhKMAASPkUqSB3c1T9OtqEm1h8v6jKWnWEwIhAO%2BrxBfryF2NdCE2jqiX9ozRD4WCZtkJNnjVer%2FfQv%2BFKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx257eIZkB8uvu90mYq3ANsEQG0rWmBD%2FCbH3VTWdRSzbZH%2BO%2BIZOaX5vSwQeowIHO9%2BsvXwhHfNUCfIEVY7JhaYHCQy5yDS%2FYbficpfa6OHyetPvH0gQCj069%2FbDPoB1bYhbiWNtqXSzA6Ti7d216yVlV%2F8nUpaq8oZ0l3zHqZW8CwgxKEz5DFLQHZP8Kq4lDdNRp1MI1DdNkJo7DrWIQrmN%2Fd%2F%2BbtzM76OybGtsp%2BS960DpBDtw2W7GMf7qy1aTwR0ZjAmRzztYSzZQ6y%2BInD1e6PgRoFCX37DwRFqsbxPUQUOeBOpEPK0mQ9%2BjAmqjF%2BKr%2BZ%2BzmEn7G4UUvdT4ZrWsRAV%2FM26cW5NgTZ%2BRJGt7VyYmke4sIRS3PN7IAYj6qBQfIHcMHn8UFzvSPbPyv1V8Nf%2BWYX%2BuHr9L4qLid%2Bkvaf9H769zDea1kEE6k3CHOlSFuPqCvpw38e7dQ%2FYbC9P5c5UCHOYIIXKdIkbSQ%2FA0KUCeEQMbRNaoVqBo4GNDlQPxC0gmDKQFz9IadHbNE81UYZXpWusgx2kRkGE1D7%2BnJb3PV3Ofd%2B5mIq9uNMNqpsEwXNqqusHu7w7dzLdIImr8YZz48SlI%2B189URirJVtx23vp9X2FhJkg54bL1mBsJzx4i6gRVq3YAM3TDb%2Bfa8BjqkAVbX%2FRn0n54dnB4FWq46OZrw3sxOfmgFG5VM4KkhuHQflZ3LI6VV4q7%2BLAVQ3n2CeuR4M2V42%2Bj5T%2Fj8FVn%2B3a7J%2F0FSaLJ%2BkbuDW6MsxtF88ssulRzMmPZmmCDXQlCoMvXlr0GnCceauZornUhQAoPQULeu0DO6CVz%2B7mcwVGQfOPRNZqK2r11OVrqO%2BGIwKcWj0A1eDuVw%2FGaVvbUVQg21GRIF&X-Amz-Signature=11c199aefd15c1d29cda1e4eaffc9a192eba81bdb77fd023996a864a705ca917&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UV6DHM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCahQkfrmzQhKMAASPkUqSB3c1T9OtqEm1h8v6jKWnWEwIhAO%2BrxBfryF2NdCE2jqiX9ozRD4WCZtkJNnjVer%2FfQv%2BFKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx257eIZkB8uvu90mYq3ANsEQG0rWmBD%2FCbH3VTWdRSzbZH%2BO%2BIZOaX5vSwQeowIHO9%2BsvXwhHfNUCfIEVY7JhaYHCQy5yDS%2FYbficpfa6OHyetPvH0gQCj069%2FbDPoB1bYhbiWNtqXSzA6Ti7d216yVlV%2F8nUpaq8oZ0l3zHqZW8CwgxKEz5DFLQHZP8Kq4lDdNRp1MI1DdNkJo7DrWIQrmN%2Fd%2F%2BbtzM76OybGtsp%2BS960DpBDtw2W7GMf7qy1aTwR0ZjAmRzztYSzZQ6y%2BInD1e6PgRoFCX37DwRFqsbxPUQUOeBOpEPK0mQ9%2BjAmqjF%2BKr%2BZ%2BzmEn7G4UUvdT4ZrWsRAV%2FM26cW5NgTZ%2BRJGt7VyYmke4sIRS3PN7IAYj6qBQfIHcMHn8UFzvSPbPyv1V8Nf%2BWYX%2BuHr9L4qLid%2Bkvaf9H769zDea1kEE6k3CHOlSFuPqCvpw38e7dQ%2FYbC9P5c5UCHOYIIXKdIkbSQ%2FA0KUCeEQMbRNaoVqBo4GNDlQPxC0gmDKQFz9IadHbNE81UYZXpWusgx2kRkGE1D7%2BnJb3PV3Ofd%2B5mIq9uNMNqpsEwXNqqusHu7w7dzLdIImr8YZz48SlI%2B189URirJVtx23vp9X2FhJkg54bL1mBsJzx4i6gRVq3YAM3TDb%2Bfa8BjqkAVbX%2FRn0n54dnB4FWq46OZrw3sxOfmgFG5VM4KkhuHQflZ3LI6VV4q7%2BLAVQ3n2CeuR4M2V42%2Bj5T%2Fj8FVn%2B3a7J%2F0FSaLJ%2BkbuDW6MsxtF88ssulRzMmPZmmCDXQlCoMvXlr0GnCceauZornUhQAoPQULeu0DO6CVz%2B7mcwVGQfOPRNZqK2r11OVrqO%2BGIwKcWj0A1eDuVw%2FGaVvbUVQg21GRIF&X-Amz-Signature=b8fc5e4f5456cfc212e7d69598036b97e571388c7f0c41898efeeff9eee0b386&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVPMK5PP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6eLb7teC9fa2PBlmE6%2FFmwsLjYEtshi7PqCkzV%2FVbvgIhAIPRuePfd0tzT8%2Fj6CJcmKLIePEH9Wl9tpUnE1ZW3orqKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7shA0z2v3Wu3ZniQq3APf%2FiLjBGilH%2F57w6bBIEFM53kbdIL3TFOarjN24hNuVnQcqtyDzjJDiiVpvNIz5Ie4NDd8Q%2BAYfLR9rZJQ6TQNXINu9vak3erSIahvC3mT7MoDWtAwL2kaXQMghfq11TKBWyxu%2B23YlazGpUkbvuG0nmQ1lBK2gQmrcWwkypLTSmedsUASO471%2FOGY1A0dykQCSjm%2FQmFUOuFOFKK84LweV3g%2Ffi8JjJa28PrgrBR3mjXx3vg4%2Bgm3AuhPBJGGYBlMU7MYqbObjPrrTjyc6%2FzeyR5TJ2Bq02jyfgUgXFULUb5hoBNvtJFzOQaXpKR4vlnZsbNfinyF81NFeDDYiqCVUSpfHPkgoZyhMeUotC3iTqz19POtLC1V3ChWGJYT246JcMsg9cg7cEBYQA%2Fs7MYe5olDraWlvTPG8AvFGaDsi%2B750l9tUdp64AtBJh3bfk54zfi%2F3vqJzsmTA7IDwfy1r8lQzKjHU6OWAPnMgN4RzheF7r2EHEgqqrSE4DpVBjHuA4IEJSr7FV9YtoYIuYFwbl3jkax6%2BxIfPiYqU5HvZTrFd3rHIwQVUO2PbOLoOhI34%2BliYX%2BCZCrSH8jN1AMKyOzGCfvLvLoDhqPkEG9N1oBXJX6nexN5hMm1ADC%2B%2Bfa8BjqkAWttFjZIS%2B3NwiYJKbCtOMwG%2FGvF2LOIV0X6%2FArgxVUsvhGuUkyPL%2Fpi%2F1A4w9mxoFmA4rbZEV3j%2FVYoa%2BQvc50Njh5m14ZzUe3LiZzAKFs9DEv19JLFVwQViQWe6sbiXqVAM2BuNgx0WrRFhPhZz8c9j%2FmsDLbhsEETWRB%2FBTOfr5Jy4WJl9GO4LGiXduK1ZHcaD9H4Yi1LV0nk8fYMwuY1hJkK&X-Amz-Signature=78f32127fbf5874d2ca9324747636b5bfa9222e22267974a2918e788edeb12f8&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466353DYTDO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEYg1ZtR6%2BX4TU0r%2FmxHHTQ6AktbbjfEtllOdZDRhodXAiEA0W0EGi%2BI5i9xQEVhsUOUcs1uU%2BvHKc%2FZeQ7i7PEHbl8qiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNrU7B9hkqD1viPoyrcA0mb0DC%2BpqgtNvhssee8FR9vs6x58PtGPrnMGRM2gyQLiWk6cofMP8xE1FRl5dZGcBME17Q92532oV3QXFlBm7jUpJtV%2F8cye%2BA02FO6zuUIvH0kQV7R0UNvHvrhguxHVF8q%2B4v7X9dye9mRPXdEOYEADwCuQadL%2BRZNZa0qKWGldHyqlVZkYn3y7opVQR71p%2Bo65gIzJIezzBaqGn%2F8l%2B5KhOfZH%2BzcET3L8onZvbFLBv0rTnTL4otn4SqjA9goqU4pC1aW2PQTJbqkzWDUbbW%2F4%2FDjvegtnQPg72rq%2Fcbi6JakEFR0Ejin74a3Ft9vPg4RqWR57vzGV37ZcYPnSxCI6yHrPDS2iyaU5gr25uF%2FMc1O71RpbS%2BrQ29JEj%2B2GYYXnIaXGf3ziN7s5YHgklmXElYV6RNbe0Bjv6jzZR6vifWcSqwQIZ%2BspY8tq02KGFbccfP6I8mg7gN5FS1BSVMUoPGDtxpgkRba2iyZ%2FH7KCFR7UwzYU1xoW%2BAJqumS%2FTLOrZ4ffSmgdWTVVbu8OVgkIdyMV77ZvTW%2FLpJkXN8ve%2FkmaLwvYh%2BYRhg%2BAEmASikKOCCr39SblaiBq1zyJqg%2Bxdjm5qEC%2FRq%2FUMuJ3FVpPyT%2FSlE26uup2h1CMPb59rwGOqUBEAOEoLn3z7B4kb3D1MsoHisLVHQi%2BGhowpgW%2Bf7opBU298x2d%2FwkiFTmdRz5rJXi%2FQ6LDmmcemxwL3heKxkvAJncmDTTmpU90tmOkrU75aeMxgaRAfdSekcPpoJ3JiWSRRpF86X0I5kx3g5vbqfPnZ9mJISdDBQWYiWDbt088kXlE9OHOK3pEftN3kvl94Fx7oQD5cye86G0n2YpSC9gYnkvUVff&X-Amz-Signature=968b4ffba5733d213299ec76720cc4b1790cd743a9a07be8e4ad63b7fb68d980&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UV6DHM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCahQkfrmzQhKMAASPkUqSB3c1T9OtqEm1h8v6jKWnWEwIhAO%2BrxBfryF2NdCE2jqiX9ozRD4WCZtkJNnjVer%2FfQv%2BFKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx257eIZkB8uvu90mYq3ANsEQG0rWmBD%2FCbH3VTWdRSzbZH%2BO%2BIZOaX5vSwQeowIHO9%2BsvXwhHfNUCfIEVY7JhaYHCQy5yDS%2FYbficpfa6OHyetPvH0gQCj069%2FbDPoB1bYhbiWNtqXSzA6Ti7d216yVlV%2F8nUpaq8oZ0l3zHqZW8CwgxKEz5DFLQHZP8Kq4lDdNRp1MI1DdNkJo7DrWIQrmN%2Fd%2F%2BbtzM76OybGtsp%2BS960DpBDtw2W7GMf7qy1aTwR0ZjAmRzztYSzZQ6y%2BInD1e6PgRoFCX37DwRFqsbxPUQUOeBOpEPK0mQ9%2BjAmqjF%2BKr%2BZ%2BzmEn7G4UUvdT4ZrWsRAV%2FM26cW5NgTZ%2BRJGt7VyYmke4sIRS3PN7IAYj6qBQfIHcMHn8UFzvSPbPyv1V8Nf%2BWYX%2BuHr9L4qLid%2Bkvaf9H769zDea1kEE6k3CHOlSFuPqCvpw38e7dQ%2FYbC9P5c5UCHOYIIXKdIkbSQ%2FA0KUCeEQMbRNaoVqBo4GNDlQPxC0gmDKQFz9IadHbNE81UYZXpWusgx2kRkGE1D7%2BnJb3PV3Ofd%2B5mIq9uNMNqpsEwXNqqusHu7w7dzLdIImr8YZz48SlI%2B189URirJVtx23vp9X2FhJkg54bL1mBsJzx4i6gRVq3YAM3TDb%2Bfa8BjqkAVbX%2FRn0n54dnB4FWq46OZrw3sxOfmgFG5VM4KkhuHQflZ3LI6VV4q7%2BLAVQ3n2CeuR4M2V42%2Bj5T%2Fj8FVn%2B3a7J%2F0FSaLJ%2BkbuDW6MsxtF88ssulRzMmPZmmCDXQlCoMvXlr0GnCceauZornUhQAoPQULeu0DO6CVz%2B7mcwVGQfOPRNZqK2r11OVrqO%2BGIwKcWj0A1eDuVw%2FGaVvbUVQg21GRIF&X-Amz-Signature=d764e575dc260121a779ee3abd0df6067d8abb0b0e4986c22214f93ec9a5893a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UV6DHM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCahQkfrmzQhKMAASPkUqSB3c1T9OtqEm1h8v6jKWnWEwIhAO%2BrxBfryF2NdCE2jqiX9ozRD4WCZtkJNnjVer%2FfQv%2BFKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx257eIZkB8uvu90mYq3ANsEQG0rWmBD%2FCbH3VTWdRSzbZH%2BO%2BIZOaX5vSwQeowIHO9%2BsvXwhHfNUCfIEVY7JhaYHCQy5yDS%2FYbficpfa6OHyetPvH0gQCj069%2FbDPoB1bYhbiWNtqXSzA6Ti7d216yVlV%2F8nUpaq8oZ0l3zHqZW8CwgxKEz5DFLQHZP8Kq4lDdNRp1MI1DdNkJo7DrWIQrmN%2Fd%2F%2BbtzM76OybGtsp%2BS960DpBDtw2W7GMf7qy1aTwR0ZjAmRzztYSzZQ6y%2BInD1e6PgRoFCX37DwRFqsbxPUQUOeBOpEPK0mQ9%2BjAmqjF%2BKr%2BZ%2BzmEn7G4UUvdT4ZrWsRAV%2FM26cW5NgTZ%2BRJGt7VyYmke4sIRS3PN7IAYj6qBQfIHcMHn8UFzvSPbPyv1V8Nf%2BWYX%2BuHr9L4qLid%2Bkvaf9H769zDea1kEE6k3CHOlSFuPqCvpw38e7dQ%2FYbC9P5c5UCHOYIIXKdIkbSQ%2FA0KUCeEQMbRNaoVqBo4GNDlQPxC0gmDKQFz9IadHbNE81UYZXpWusgx2kRkGE1D7%2BnJb3PV3Ofd%2B5mIq9uNMNqpsEwXNqqusHu7w7dzLdIImr8YZz48SlI%2B189URirJVtx23vp9X2FhJkg54bL1mBsJzx4i6gRVq3YAM3TDb%2Bfa8BjqkAVbX%2FRn0n54dnB4FWq46OZrw3sxOfmgFG5VM4KkhuHQflZ3LI6VV4q7%2BLAVQ3n2CeuR4M2V42%2Bj5T%2Fj8FVn%2B3a7J%2F0FSaLJ%2BkbuDW6MsxtF88ssulRzMmPZmmCDXQlCoMvXlr0GnCceauZornUhQAoPQULeu0DO6CVz%2B7mcwVGQfOPRNZqK2r11OVrqO%2BGIwKcWj0A1eDuVw%2FGaVvbUVQg21GRIF&X-Amz-Signature=a176371921171f64ebe0bffbeffc013f0af48180054deb8272b52b1b836e0f96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UV6DHM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCahQkfrmzQhKMAASPkUqSB3c1T9OtqEm1h8v6jKWnWEwIhAO%2BrxBfryF2NdCE2jqiX9ozRD4WCZtkJNnjVer%2FfQv%2BFKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx257eIZkB8uvu90mYq3ANsEQG0rWmBD%2FCbH3VTWdRSzbZH%2BO%2BIZOaX5vSwQeowIHO9%2BsvXwhHfNUCfIEVY7JhaYHCQy5yDS%2FYbficpfa6OHyetPvH0gQCj069%2FbDPoB1bYhbiWNtqXSzA6Ti7d216yVlV%2F8nUpaq8oZ0l3zHqZW8CwgxKEz5DFLQHZP8Kq4lDdNRp1MI1DdNkJo7DrWIQrmN%2Fd%2F%2BbtzM76OybGtsp%2BS960DpBDtw2W7GMf7qy1aTwR0ZjAmRzztYSzZQ6y%2BInD1e6PgRoFCX37DwRFqsbxPUQUOeBOpEPK0mQ9%2BjAmqjF%2BKr%2BZ%2BzmEn7G4UUvdT4ZrWsRAV%2FM26cW5NgTZ%2BRJGt7VyYmke4sIRS3PN7IAYj6qBQfIHcMHn8UFzvSPbPyv1V8Nf%2BWYX%2BuHr9L4qLid%2Bkvaf9H769zDea1kEE6k3CHOlSFuPqCvpw38e7dQ%2FYbC9P5c5UCHOYIIXKdIkbSQ%2FA0KUCeEQMbRNaoVqBo4GNDlQPxC0gmDKQFz9IadHbNE81UYZXpWusgx2kRkGE1D7%2BnJb3PV3Ofd%2B5mIq9uNMNqpsEwXNqqusHu7w7dzLdIImr8YZz48SlI%2B189URirJVtx23vp9X2FhJkg54bL1mBsJzx4i6gRVq3YAM3TDb%2Bfa8BjqkAVbX%2FRn0n54dnB4FWq46OZrw3sxOfmgFG5VM4KkhuHQflZ3LI6VV4q7%2BLAVQ3n2CeuR4M2V42%2Bj5T%2Fj8FVn%2B3a7J%2F0FSaLJ%2BkbuDW6MsxtF88ssulRzMmPZmmCDXQlCoMvXlr0GnCceauZornUhQAoPQULeu0DO6CVz%2B7mcwVGQfOPRNZqK2r11OVrqO%2BGIwKcWj0A1eDuVw%2FGaVvbUVQg21GRIF&X-Amz-Signature=2f7b3c6d6bb5d8916d597f3344bd94d15a529e9abf11e9dfcd04a331912a5abb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKH3ZLQZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCq94P4YhY06BIXeLSCiIErrNtcrvMLAas6JGBwBeCIkAIhAJls6cPg48Vz1F2299Fp6nMoHQSEeq3QGGve214xXwNnKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B0Gu114l%2F2uy9j3gq3ANWx3m7PT8d6fVv40ZXiNEJrl2BsAkGc%2FG8VxUuexvW62%2FnrsRkFV5LOAZFsMH17FsGRUZR0aFWqVYGCr6sRD837vqY8aP7XxZGsHgvMQWsU%2FpF9AZ6ZzFt6xjyLsAbNDIH%2BhkF5tjF2ZISGjSUD0bSDrCViyErA8bd8JP5%2FomObkLP8s1ClNSum4dc%2FhGJWYu0qnN5nw90PdSinOK9SWhGUOpCbYSCNwpCqGV3ueUGdtTn7PJw5sqX2TuDi%2BNA72OAXmQKB8%2FJs8GoGUQRIWINUB0mbp8MV3fCFtSeo0OgI%2Fp6cqr8EaRYN7Lk7fnXZxGKbHy63Yj2LSOhyHpQIb9w0abB%2FTwsL70WHYF0pIEGUdjUo4EvchiLEefinxazNe3iTfCliMsZB%2BpsfELaFUv3uuGvBYeLCZiLhKLjUnkWjnJY3VbDSC6xMigj%2B%2BVFsQNwykSlmOxfXL9kPFoxj8Z7o16If2LqMIZvyxsDOkJMR2nuEmYB3PYNOrBgKgZa3VhuP%2BcCF9Rki8WdYybgk7H676K8WYqsF2EdpcGYXQLgbkhwaBo5fHKP4UdFa7%2BdhcCh7dHUani%2FK5a2Ru2zeFQOptGDUS1BwwMYk1KylTTrBv42eV%2BUQD6xmFmAtDD1%2Bfa8BjqkAaUvWwGcAYVBxE0t4ekvcELDmqFVuvZ6%2Fh5efxp24UUragpmSQirjf0h8R5CYtgl8jVRQWlCVmOVyaWgTlFdHU4OcFeMNAaHu%2F04uL0c8KcLnCUnRMsRS4nXKbdWqiEkR5ynV7Vm1MXshUcSi1IfzFqqvxqqEb7mUxCIkIIPTvwrZxo8Dz4CgIGjCpKWUr8iA3i3G8DvYDfqzP7l2iB9WtagoSw1&X-Amz-Signature=58403c91436b3db7642be51a70f2cdc69c0ef8c9c299da453c0444e06dc143d7&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTRKCJAT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm%2BzmOdOZLlmQjillCY76tB5TGD5cVJxX3sUslUP6%2BLAIgaytV9PdN7r4itpEbH5HmkMYvwomzCsRf%2FP%2BAvlsRmNwqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA9AggOKQ4X1hKfVoyrcA3CdsESrr3Bl%2B6pl2JvTjfqXZ7dXE1BLmDz2iWpjZvjTUCXHdAbL0TEK8%2BMkZv2HKcG99hwGW3AGGyjkQM4AFCjOWdWzSeqs5XWg3wafct2BKAyOMWM1r7B7UgI2h3Ns0%2Fn0TEjplUkT1je7U6L63nwEfnrnkMJVvi%2FNETuP9DB45fZkZN3rSUF0P1NTfYHWdbBH2Ibeiyp2236EbTQ7FW6%2BDWuv2m8e8O1YRDuMh3Qe30%2Bmfa41GK0LEowUwFKnYOqrWwP6rqysq3EA%2B4OTPyHNV3cACICRH54IIhfhwvXxEDamASLFNr4jLFtFHtKetiyx4tD4mUOCoUVUTP%2BImKfMp3RsnhDAXO%2B8UyLoqi6V%2BX6zBuuxn8rDd29OIN4ELUYqAxMx173u3ByVbB64FlAxkwvFFEdtGF778F1VpQwMbXrrJvQtZsB6ZqVpn%2Ft5LrTx3POyelcHOy%2B32T451cPZtMSItgpfQfjN%2BvBeK9wu8jzmem6zzZTdarPi6Qgz6p%2FCV%2Fvhe9Sq1w0IYAcB7LhtAZOemrHdTynlunm5vnDTAOB7AUjLOx7zT%2Fp6kwdeWo24oN18R5YtzqP5J2mSm9EKtFHRWox12hwwCLPcy7FASeYLoBLzc1tAWl1sMLX59rwGOqUBIbcz9AJVzetkTi%2BAGzubkpi6HwoFCnwIUMN8tkN5B8N4pYKSnMDrPOexALL2fVVUiZXCXOSRa8PBFUYkkGHW3m9Dv0QwSZGpzfJie3vlcw3JKe9C6i2J3gvX5QIAqzrxoXKejDCjDNvMNbSgSU0mg4lhAQaY6bMVgGqH5QRfVSFoEAreMf9Mg2%2BkKpNlCM80Niwonm3WgiA9l4sibWVDi77gQuXo&X-Amz-Signature=b02e34e82a4cf0d4318e9163fb21e9995dd86d130e3a65f5ce80124a8b5c74dc&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRL5BVM4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAU5GSlWD6Rl3%2BOan%2BmNWjcwXxH53euOfk9aNpMgnZMmAiAoKmWPL97%2BzET1Jiv0L6dqwuz6QZb5MpeAv7iAMsowPyqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXupxwjUmZ6%2FYtQtnKtwDSFwFb1Ybjm8cPQ0pME3ChVd6%2BcOQc6qAOuN29wVa0qq9vAPinSIlEnXKZ9ouERPCEJbblWLQ3gjI45ZMIo%2F3x%2FnFfr%2BeONQT36eRZcJEr7t6CGWPIacFdFAmZFlxfEFVA9A%2BBPfyhFv%2BrZUz9pGcikwmAnLfkiNqGvJaIrOjHXikRjZVkyU2sLhvAJ3RNp5NzwSWApCfx3aDaJLUgf8PeXZ7HAxwqYrshBtx%2BtAA2M1ZjMdKKvadEj%2BqWv2T86si0ksUNmCDm1wjyOAEvruGkpnT3IDOktIPUs6Epn7cZ%2BVloWAhuNkb%2FbNMVpeTdmf4Fj2vjXRJtFF2WiaCcJWebwDBcsBlbnFRQsT3gaYuyMtKWV2mDZ2k76jvfSp3VDZWTl042aWNk0Gmb0uJCjUuF6c%2BslypNnj6uWRG3%2BzU2Iqc24YUyrqO%2B6NAUSxmNbW6o7rnpyF8onpiwuBteMY%2B8OnKrCKrehzZ6QNJAz9gFPHEO7KT6FdfEr82ncoBEzWRQIDb6IUitBUJ%2FvIiNvSov5aYy5ZP2GfwBp0PjI7TzXHRHM1jB6slscxaaAcz61uwZ9tN6lbpkxr5%2FR7l%2Fr3Zrcd3SoJRHT5LDYkxDixFX9pOxRp5qiwPwvUoKWww4vn2vAY6pgE7enjm2UQUY318OZbVUtRkCdOaaCsBS0bGlS6wUD5IbTJVIErU9d6Vgo4BTA2lh2mlsdQDktPzKjqj4JW79wzIj4YyFckA3%2FYCv1YccU5qxDNmDinwnhbGdwbQanBAOXJ22F%2FFiSZ%2F2p%2B7x9ccHEayiTTfOJIRVl6%2ByKQ8X7GcSGaLNX2nBF1bkOY%2BIPPzHQwepMjOvJHIyw4h29MoG%2FIQMXti9JyE&X-Amz-Signature=69aa44f023721c25854ca353e0aa0ee6803dbce1871091bce953b4889f593bf9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BSJA7CH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyAg5Om%2Fgk8uB63a7nBW7WVyD4AK6Xcx0kF655oXzBGAIhANoVfigWLMNGfVfxL%2Bb3fgOeaLnsH0Yg0s3jyiW0gyZaKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuzU5meBQGUIJUm1Eq3AMdeXS8g1xvAKrHCSGB%2Fvdh5nJ4x%2BQEEC7fAfsfRZwQ2D1UDeDqe9wD3WADGHXwqg2gAkANn4nH%2BDO7k1Lb4ZbNkB7BxrmvNIQlD4rc8iibv7I7ZlzhgPh9MD0Jv4i%2BWUpPT5p1r6SSo2tfRbGHtrlFu8P5jb%2Fh98PrShAGlA%2FFQ8ZHdKiHtawtBXbLrkqHE7WtjJrJOzQvqVTkhCwIquEoxOfKBKC6ButPJ4rjYI%2B94nwJvMxcfpBq2ytF0SXYQj5RW8d84WGIbhkWhvbUsgwFXOvNFAgFzf7qbvZPt4L8NsbWJPQL3sLzZWvqqnsoQclG9KbgBcVjzEFB1elqkYWy8rxkvNrHMhS1HAkKNcvOgEwUtwHQjzlD2Nuk3rk352pwfBCc%2BMVjqsMUKJvRsxWLYrpxmblOhyUdVY%2FTMzgkgJ6QQpUQHwsVkugdegGlJiiPMQ2K%2BZwEihbFTu9m2Ti1wRjLv3Vmb2apbvbKA5DkDPbBDluo%2B%2BN94K7vqW2ZxKD%2Fw5urD6R14LTQ5FxlMY8ZqXayjJb40OymqZ8B6rOy0TzErD6bkRZGw%2F0CkLstwjOO%2BIzmjFNu6lB646UYIoaxoWU0EzpukQPq1lg59U%2BvG2W1hFfwKnF3rOnWYTC8%2Bfa8BjqkAbj9LEmbrhD9ujl3YVlH6eo05Usagog7Bof9v6BX%2BRKxtR3LoS5bMnFAnDWvUMdWqoNkkEQycB1QLvSPovC0C4OgKlyyiCthkn76m9GoGc1FUVGoePQbISiZI4HeAuGp%2BAQYyvmOTU6l3GremSetLk%2BiBZsupEqOBpVryKd%2B9KiBYq8sZBXQyU%2FGGASVt%2BXFcdYy765i4Y%2FiKU8qqd1bT6D2WgaH&X-Amz-Signature=21076395d0a565b5b356ca453ebc9df99c6a5f868f13b03a8143deae0b0d0cbf&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BSJA7CH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyAg5Om%2Fgk8uB63a7nBW7WVyD4AK6Xcx0kF655oXzBGAIhANoVfigWLMNGfVfxL%2Bb3fgOeaLnsH0Yg0s3jyiW0gyZaKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuzU5meBQGUIJUm1Eq3AMdeXS8g1xvAKrHCSGB%2Fvdh5nJ4x%2BQEEC7fAfsfRZwQ2D1UDeDqe9wD3WADGHXwqg2gAkANn4nH%2BDO7k1Lb4ZbNkB7BxrmvNIQlD4rc8iibv7I7ZlzhgPh9MD0Jv4i%2BWUpPT5p1r6SSo2tfRbGHtrlFu8P5jb%2Fh98PrShAGlA%2FFQ8ZHdKiHtawtBXbLrkqHE7WtjJrJOzQvqVTkhCwIquEoxOfKBKC6ButPJ4rjYI%2B94nwJvMxcfpBq2ytF0SXYQj5RW8d84WGIbhkWhvbUsgwFXOvNFAgFzf7qbvZPt4L8NsbWJPQL3sLzZWvqqnsoQclG9KbgBcVjzEFB1elqkYWy8rxkvNrHMhS1HAkKNcvOgEwUtwHQjzlD2Nuk3rk352pwfBCc%2BMVjqsMUKJvRsxWLYrpxmblOhyUdVY%2FTMzgkgJ6QQpUQHwsVkugdegGlJiiPMQ2K%2BZwEihbFTu9m2Ti1wRjLv3Vmb2apbvbKA5DkDPbBDluo%2B%2BN94K7vqW2ZxKD%2Fw5urD6R14LTQ5FxlMY8ZqXayjJb40OymqZ8B6rOy0TzErD6bkRZGw%2F0CkLstwjOO%2BIzmjFNu6lB646UYIoaxoWU0EzpukQPq1lg59U%2BvG2W1hFfwKnF3rOnWYTC8%2Bfa8BjqkAbj9LEmbrhD9ujl3YVlH6eo05Usagog7Bof9v6BX%2BRKxtR3LoS5bMnFAnDWvUMdWqoNkkEQycB1QLvSPovC0C4OgKlyyiCthkn76m9GoGc1FUVGoePQbISiZI4HeAuGp%2BAQYyvmOTU6l3GremSetLk%2BiBZsupEqOBpVryKd%2B9KiBYq8sZBXQyU%2FGGASVt%2BXFcdYy765i4Y%2FiKU8qqd1bT6D2WgaH&X-Amz-Signature=834542e5ef4637bdfd1b87f96ba0b0b9cebd5ba9f96189f91ea7820d058a0d75&X-Amz-SignedHeaders=host&x-id=GetObject)

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
