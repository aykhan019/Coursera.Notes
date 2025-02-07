

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I7ZAOOI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCvaUdnGvenHfb2DhrmWP%2BxTyq3UwW0l2iQw7vvMuOW1AIhAOvl4fgx0SSJinlcCe6zQtMmXBPsogNh%2F2h4M1EFd4ymKv8DCH0QABoMNjM3NDIzMTgzODA1IgwpVGWH4S2j6CahmTAq3AMlCXsrvwZGNpMlKCfrjxMdRbNDFAzW0i%2Bo5vUO%2FFiqVQcqxiZtgJ24B7s9Atk%2BI4sC7J2ncuveWH10V7KnMpBLiKZIIXVXNtNlfFB6qW4ZzMMq2blpDUFza%2BmIitDccWRMJIuhcdj1EAaFsE4TZ5GVZoTSewAjKoRd4Oj4Y29%2Fe8T%2FVZe70paAvu4Fow8Vs1xfi%2BrDxXbp7gtVLTtPdVHU7hIneSbGDmhCIFuQ80SJLYREsO53NrICGhR9WWub2xGgcQaGTcR8c7wQMJpCOsuDvGuEADSmPPsFcFFdusyejUveLld1c79%2BrrLVBEBp53jFYI%2B9ujuYo%2F13xzHPgFZPjLTSOUti74H33l1%2FV9ZCmJGd8gnR1%2FXzyMHRCGUonRP7FQRNPeDwMpqujOH5uUjh1VJWa33T63f%2FnDMuJMFX8BQMps17PbowRiz3VOaxWHMJMTJNJGocWPQULhTKP8NyTQD2lRH%2BE2RUwxegw0K0a9lEwL3yUf1k%2BpA%2FqY%2BfGuKVDJhiIGJ0BdK4ihntdutfp0YDbWuddqF%2F9sSwdIltihsezoF%2BlDHXtuycqe0GTQtHx%2Fdi1AQ3lyZyga3tnfEto9QmQ0mP4geTBJ%2BlyJgiINxYtO5lb2ze%2BXfYiDC10pm9BjqkAcYMZsKfwfhoYHpoLV4KEwWCDDfzqxpOxlKHOR6yddFnrMXwGsFW3JrDO3xsJWROpWPdF0XNBJnAmt6%2FnXnQLVYeGz0tFZlarmiK%2BxLbzmxNsU6%2BfPNL8VvN9xm6VGrkPZil%2FHXu%2Bg66NqDw9HA8ewyN0yvmgX8aPG8c%2BYMncYH3jCXlho7XrCPEanNw1G4uDOQlBER%2BVhwzh%2FHvDJvsZrI%2BKNkO&X-Amz-Signature=eee0b58b1f48cb4701c5a7afe2de56b25eced276c4c2ea257559c8f46780866b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I7ZAOOI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCvaUdnGvenHfb2DhrmWP%2BxTyq3UwW0l2iQw7vvMuOW1AIhAOvl4fgx0SSJinlcCe6zQtMmXBPsogNh%2F2h4M1EFd4ymKv8DCH0QABoMNjM3NDIzMTgzODA1IgwpVGWH4S2j6CahmTAq3AMlCXsrvwZGNpMlKCfrjxMdRbNDFAzW0i%2Bo5vUO%2FFiqVQcqxiZtgJ24B7s9Atk%2BI4sC7J2ncuveWH10V7KnMpBLiKZIIXVXNtNlfFB6qW4ZzMMq2blpDUFza%2BmIitDccWRMJIuhcdj1EAaFsE4TZ5GVZoTSewAjKoRd4Oj4Y29%2Fe8T%2FVZe70paAvu4Fow8Vs1xfi%2BrDxXbp7gtVLTtPdVHU7hIneSbGDmhCIFuQ80SJLYREsO53NrICGhR9WWub2xGgcQaGTcR8c7wQMJpCOsuDvGuEADSmPPsFcFFdusyejUveLld1c79%2BrrLVBEBp53jFYI%2B9ujuYo%2F13xzHPgFZPjLTSOUti74H33l1%2FV9ZCmJGd8gnR1%2FXzyMHRCGUonRP7FQRNPeDwMpqujOH5uUjh1VJWa33T63f%2FnDMuJMFX8BQMps17PbowRiz3VOaxWHMJMTJNJGocWPQULhTKP8NyTQD2lRH%2BE2RUwxegw0K0a9lEwL3yUf1k%2BpA%2FqY%2BfGuKVDJhiIGJ0BdK4ihntdutfp0YDbWuddqF%2F9sSwdIltihsezoF%2BlDHXtuycqe0GTQtHx%2Fdi1AQ3lyZyga3tnfEto9QmQ0mP4geTBJ%2BlyJgiINxYtO5lb2ze%2BXfYiDC10pm9BjqkAcYMZsKfwfhoYHpoLV4KEwWCDDfzqxpOxlKHOR6yddFnrMXwGsFW3JrDO3xsJWROpWPdF0XNBJnAmt6%2FnXnQLVYeGz0tFZlarmiK%2BxLbzmxNsU6%2BfPNL8VvN9xm6VGrkPZil%2FHXu%2Bg66NqDw9HA8ewyN0yvmgX8aPG8c%2BYMncYH3jCXlho7XrCPEanNw1G4uDOQlBER%2BVhwzh%2FHvDJvsZrI%2BKNkO&X-Amz-Signature=72d1d115694338fd74476a699429ad36df237e0c6c0f5290d4799731d74b32d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I7ZAOOI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCvaUdnGvenHfb2DhrmWP%2BxTyq3UwW0l2iQw7vvMuOW1AIhAOvl4fgx0SSJinlcCe6zQtMmXBPsogNh%2F2h4M1EFd4ymKv8DCH0QABoMNjM3NDIzMTgzODA1IgwpVGWH4S2j6CahmTAq3AMlCXsrvwZGNpMlKCfrjxMdRbNDFAzW0i%2Bo5vUO%2FFiqVQcqxiZtgJ24B7s9Atk%2BI4sC7J2ncuveWH10V7KnMpBLiKZIIXVXNtNlfFB6qW4ZzMMq2blpDUFza%2BmIitDccWRMJIuhcdj1EAaFsE4TZ5GVZoTSewAjKoRd4Oj4Y29%2Fe8T%2FVZe70paAvu4Fow8Vs1xfi%2BrDxXbp7gtVLTtPdVHU7hIneSbGDmhCIFuQ80SJLYREsO53NrICGhR9WWub2xGgcQaGTcR8c7wQMJpCOsuDvGuEADSmPPsFcFFdusyejUveLld1c79%2BrrLVBEBp53jFYI%2B9ujuYo%2F13xzHPgFZPjLTSOUti74H33l1%2FV9ZCmJGd8gnR1%2FXzyMHRCGUonRP7FQRNPeDwMpqujOH5uUjh1VJWa33T63f%2FnDMuJMFX8BQMps17PbowRiz3VOaxWHMJMTJNJGocWPQULhTKP8NyTQD2lRH%2BE2RUwxegw0K0a9lEwL3yUf1k%2BpA%2FqY%2BfGuKVDJhiIGJ0BdK4ihntdutfp0YDbWuddqF%2F9sSwdIltihsezoF%2BlDHXtuycqe0GTQtHx%2Fdi1AQ3lyZyga3tnfEto9QmQ0mP4geTBJ%2BlyJgiINxYtO5lb2ze%2BXfYiDC10pm9BjqkAcYMZsKfwfhoYHpoLV4KEwWCDDfzqxpOxlKHOR6yddFnrMXwGsFW3JrDO3xsJWROpWPdF0XNBJnAmt6%2FnXnQLVYeGz0tFZlarmiK%2BxLbzmxNsU6%2BfPNL8VvN9xm6VGrkPZil%2FHXu%2Bg66NqDw9HA8ewyN0yvmgX8aPG8c%2BYMncYH3jCXlho7XrCPEanNw1G4uDOQlBER%2BVhwzh%2FHvDJvsZrI%2BKNkO&X-Amz-Signature=e2272f1ad77049b02881fb72f72b18230b621e231fa63791e683dee9f3a186c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGL4ERJK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDsbM1QJ7PhGYBNtdAsB16mYAsiosLkLQ5m%2BZf3LAWv5wIgZYGHnm968K2jS08HU%2B5SKGdPTC%2FpPpZjTis5vjoW%2BTEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFel6VozqWqI3bec%2BSrcA0DFBjYF2pOisiVmpoy964R8jvvD7R%2FhEhnO8%2FrHJrIxbj31SGb%2Fr5gpOddoIVMuZRW5%2BbLaMkpOOF2lEWYiRDMXS9mMPrCthN4QV4sWcDciv1bBMVgrmX0qFMdsXMK0b9Qxnp1n5kLMSj7aAx2kLK18RrT%2Fwo2IQIp3PxOoah5LwHSyw2wIH2Go%2BdaYfuOh6Uwk7teDrImIkdJSlGI%2B%2F2zqUYa65yb08hOTMU5%2FMXBWcPK6D0X1Iivupa3e8WPEZvgFAPQb8irLhUyKKM41LRHRGt4DwueAcBRbfQg0sh8v3I1u724HA8QvdRvKqUE2CVbzBHV8xmU4m6z30oSG91PMv8mmcqNP%2FDLE7mN0fdiB%2BwgYUkeFCJVgkfPzETIT0mMKUYyMbNhuVtjR6IIaog8cMW0euJPoapxjikeIpfQgUtLBumi6%2BRYsVXuk%2Fdab7lLfjTsDdERc4Ip3zTJOpFicI9y3evd4jDXokhwYstmAlcQK29mDE4XaZjwrFL1eiCCsIHLHNlAMRXlPQuvl6KBbA8CvZ1DXf6ZZcUlhz0%2BRkQMV8cTialqMvihssvOvyBjo8%2FlzQnyVcfSxWWPPT5vQLZQwO8AZ%2F8kSUwDonXa8OimelAGPua0xkk0XMNDSmb0GOqUBvduT3zoK9s7I1PdxtHOxqWq9FGGG9m54Dcj5giEsA0hJ30D0wUOHHWytN0PoeX26Nnc1qm1pQJlBViACtq9EJKSYTQt1tWYGkajDq7990AH6dVKJg%2FHNrG1EVUtu8P6HbjZ9dMJXgMBm2zygXkwHJ5eoi%2B84NKg85zH9CcHMprfT4obxSf8d2gkCVB5b6fkkRCqy3R0wowO4vWBAFAortKW77dIv&X-Amz-Signature=6eb69f7998bd08a3b83ce04e1c7a92ddf2bb1cc3324a969e3637a8c6ab9e62aa&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGL4ERJK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDsbM1QJ7PhGYBNtdAsB16mYAsiosLkLQ5m%2BZf3LAWv5wIgZYGHnm968K2jS08HU%2B5SKGdPTC%2FpPpZjTis5vjoW%2BTEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFel6VozqWqI3bec%2BSrcA0DFBjYF2pOisiVmpoy964R8jvvD7R%2FhEhnO8%2FrHJrIxbj31SGb%2Fr5gpOddoIVMuZRW5%2BbLaMkpOOF2lEWYiRDMXS9mMPrCthN4QV4sWcDciv1bBMVgrmX0qFMdsXMK0b9Qxnp1n5kLMSj7aAx2kLK18RrT%2Fwo2IQIp3PxOoah5LwHSyw2wIH2Go%2BdaYfuOh6Uwk7teDrImIkdJSlGI%2B%2F2zqUYa65yb08hOTMU5%2FMXBWcPK6D0X1Iivupa3e8WPEZvgFAPQb8irLhUyKKM41LRHRGt4DwueAcBRbfQg0sh8v3I1u724HA8QvdRvKqUE2CVbzBHV8xmU4m6z30oSG91PMv8mmcqNP%2FDLE7mN0fdiB%2BwgYUkeFCJVgkfPzETIT0mMKUYyMbNhuVtjR6IIaog8cMW0euJPoapxjikeIpfQgUtLBumi6%2BRYsVXuk%2Fdab7lLfjTsDdERc4Ip3zTJOpFicI9y3evd4jDXokhwYstmAlcQK29mDE4XaZjwrFL1eiCCsIHLHNlAMRXlPQuvl6KBbA8CvZ1DXf6ZZcUlhz0%2BRkQMV8cTialqMvihssvOvyBjo8%2FlzQnyVcfSxWWPPT5vQLZQwO8AZ%2F8kSUwDonXa8OimelAGPua0xkk0XMNDSmb0GOqUBvduT3zoK9s7I1PdxtHOxqWq9FGGG9m54Dcj5giEsA0hJ30D0wUOHHWytN0PoeX26Nnc1qm1pQJlBViACtq9EJKSYTQt1tWYGkajDq7990AH6dVKJg%2FHNrG1EVUtu8P6HbjZ9dMJXgMBm2zygXkwHJ5eoi%2B84NKg85zH9CcHMprfT4obxSf8d2gkCVB5b6fkkRCqy3R0wowO4vWBAFAortKW77dIv&X-Amz-Signature=e53abe1c6d4a5dbff7dfc65779aadcf74110d53d45bcb52bd3dc1cf2772580a1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGL4ERJK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDsbM1QJ7PhGYBNtdAsB16mYAsiosLkLQ5m%2BZf3LAWv5wIgZYGHnm968K2jS08HU%2B5SKGdPTC%2FpPpZjTis5vjoW%2BTEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFel6VozqWqI3bec%2BSrcA0DFBjYF2pOisiVmpoy964R8jvvD7R%2FhEhnO8%2FrHJrIxbj31SGb%2Fr5gpOddoIVMuZRW5%2BbLaMkpOOF2lEWYiRDMXS9mMPrCthN4QV4sWcDciv1bBMVgrmX0qFMdsXMK0b9Qxnp1n5kLMSj7aAx2kLK18RrT%2Fwo2IQIp3PxOoah5LwHSyw2wIH2Go%2BdaYfuOh6Uwk7teDrImIkdJSlGI%2B%2F2zqUYa65yb08hOTMU5%2FMXBWcPK6D0X1Iivupa3e8WPEZvgFAPQb8irLhUyKKM41LRHRGt4DwueAcBRbfQg0sh8v3I1u724HA8QvdRvKqUE2CVbzBHV8xmU4m6z30oSG91PMv8mmcqNP%2FDLE7mN0fdiB%2BwgYUkeFCJVgkfPzETIT0mMKUYyMbNhuVtjR6IIaog8cMW0euJPoapxjikeIpfQgUtLBumi6%2BRYsVXuk%2Fdab7lLfjTsDdERc4Ip3zTJOpFicI9y3evd4jDXokhwYstmAlcQK29mDE4XaZjwrFL1eiCCsIHLHNlAMRXlPQuvl6KBbA8CvZ1DXf6ZZcUlhz0%2BRkQMV8cTialqMvihssvOvyBjo8%2FlzQnyVcfSxWWPPT5vQLZQwO8AZ%2F8kSUwDonXa8OimelAGPua0xkk0XMNDSmb0GOqUBvduT3zoK9s7I1PdxtHOxqWq9FGGG9m54Dcj5giEsA0hJ30D0wUOHHWytN0PoeX26Nnc1qm1pQJlBViACtq9EJKSYTQt1tWYGkajDq7990AH6dVKJg%2FHNrG1EVUtu8P6HbjZ9dMJXgMBm2zygXkwHJ5eoi%2B84NKg85zH9CcHMprfT4obxSf8d2gkCVB5b6fkkRCqy3R0wowO4vWBAFAortKW77dIv&X-Amz-Signature=81c979216d7b51eabcec5c138c3c63bc753533cb6b30f5b95570530aee653de0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGL4ERJK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDsbM1QJ7PhGYBNtdAsB16mYAsiosLkLQ5m%2BZf3LAWv5wIgZYGHnm968K2jS08HU%2B5SKGdPTC%2FpPpZjTis5vjoW%2BTEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFel6VozqWqI3bec%2BSrcA0DFBjYF2pOisiVmpoy964R8jvvD7R%2FhEhnO8%2FrHJrIxbj31SGb%2Fr5gpOddoIVMuZRW5%2BbLaMkpOOF2lEWYiRDMXS9mMPrCthN4QV4sWcDciv1bBMVgrmX0qFMdsXMK0b9Qxnp1n5kLMSj7aAx2kLK18RrT%2Fwo2IQIp3PxOoah5LwHSyw2wIH2Go%2BdaYfuOh6Uwk7teDrImIkdJSlGI%2B%2F2zqUYa65yb08hOTMU5%2FMXBWcPK6D0X1Iivupa3e8WPEZvgFAPQb8irLhUyKKM41LRHRGt4DwueAcBRbfQg0sh8v3I1u724HA8QvdRvKqUE2CVbzBHV8xmU4m6z30oSG91PMv8mmcqNP%2FDLE7mN0fdiB%2BwgYUkeFCJVgkfPzETIT0mMKUYyMbNhuVtjR6IIaog8cMW0euJPoapxjikeIpfQgUtLBumi6%2BRYsVXuk%2Fdab7lLfjTsDdERc4Ip3zTJOpFicI9y3evd4jDXokhwYstmAlcQK29mDE4XaZjwrFL1eiCCsIHLHNlAMRXlPQuvl6KBbA8CvZ1DXf6ZZcUlhz0%2BRkQMV8cTialqMvihssvOvyBjo8%2FlzQnyVcfSxWWPPT5vQLZQwO8AZ%2F8kSUwDonXa8OimelAGPua0xkk0XMNDSmb0GOqUBvduT3zoK9s7I1PdxtHOxqWq9FGGG9m54Dcj5giEsA0hJ30D0wUOHHWytN0PoeX26Nnc1qm1pQJlBViACtq9EJKSYTQt1tWYGkajDq7990AH6dVKJg%2FHNrG1EVUtu8P6HbjZ9dMJXgMBm2zygXkwHJ5eoi%2B84NKg85zH9CcHMprfT4obxSf8d2gkCVB5b6fkkRCqy3R0wowO4vWBAFAortKW77dIv&X-Amz-Signature=b3a67e3bdcf15c4ce32ccd6e0229c4fb1962778b1ad8dac4acbcc5c2229138b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGL4ERJK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDsbM1QJ7PhGYBNtdAsB16mYAsiosLkLQ5m%2BZf3LAWv5wIgZYGHnm968K2jS08HU%2B5SKGdPTC%2FpPpZjTis5vjoW%2BTEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFel6VozqWqI3bec%2BSrcA0DFBjYF2pOisiVmpoy964R8jvvD7R%2FhEhnO8%2FrHJrIxbj31SGb%2Fr5gpOddoIVMuZRW5%2BbLaMkpOOF2lEWYiRDMXS9mMPrCthN4QV4sWcDciv1bBMVgrmX0qFMdsXMK0b9Qxnp1n5kLMSj7aAx2kLK18RrT%2Fwo2IQIp3PxOoah5LwHSyw2wIH2Go%2BdaYfuOh6Uwk7teDrImIkdJSlGI%2B%2F2zqUYa65yb08hOTMU5%2FMXBWcPK6D0X1Iivupa3e8WPEZvgFAPQb8irLhUyKKM41LRHRGt4DwueAcBRbfQg0sh8v3I1u724HA8QvdRvKqUE2CVbzBHV8xmU4m6z30oSG91PMv8mmcqNP%2FDLE7mN0fdiB%2BwgYUkeFCJVgkfPzETIT0mMKUYyMbNhuVtjR6IIaog8cMW0euJPoapxjikeIpfQgUtLBumi6%2BRYsVXuk%2Fdab7lLfjTsDdERc4Ip3zTJOpFicI9y3evd4jDXokhwYstmAlcQK29mDE4XaZjwrFL1eiCCsIHLHNlAMRXlPQuvl6KBbA8CvZ1DXf6ZZcUlhz0%2BRkQMV8cTialqMvihssvOvyBjo8%2FlzQnyVcfSxWWPPT5vQLZQwO8AZ%2F8kSUwDonXa8OimelAGPua0xkk0XMNDSmb0GOqUBvduT3zoK9s7I1PdxtHOxqWq9FGGG9m54Dcj5giEsA0hJ30D0wUOHHWytN0PoeX26Nnc1qm1pQJlBViACtq9EJKSYTQt1tWYGkajDq7990AH6dVKJg%2FHNrG1EVUtu8P6HbjZ9dMJXgMBm2zygXkwHJ5eoi%2B84NKg85zH9CcHMprfT4obxSf8d2gkCVB5b6fkkRCqy3R0wowO4vWBAFAortKW77dIv&X-Amz-Signature=f45ac6c6e965067cf64970c67f99b74deeda73d7c2d65fbafa7ac27263002c60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGL4ERJK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDsbM1QJ7PhGYBNtdAsB16mYAsiosLkLQ5m%2BZf3LAWv5wIgZYGHnm968K2jS08HU%2B5SKGdPTC%2FpPpZjTis5vjoW%2BTEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFel6VozqWqI3bec%2BSrcA0DFBjYF2pOisiVmpoy964R8jvvD7R%2FhEhnO8%2FrHJrIxbj31SGb%2Fr5gpOddoIVMuZRW5%2BbLaMkpOOF2lEWYiRDMXS9mMPrCthN4QV4sWcDciv1bBMVgrmX0qFMdsXMK0b9Qxnp1n5kLMSj7aAx2kLK18RrT%2Fwo2IQIp3PxOoah5LwHSyw2wIH2Go%2BdaYfuOh6Uwk7teDrImIkdJSlGI%2B%2F2zqUYa65yb08hOTMU5%2FMXBWcPK6D0X1Iivupa3e8WPEZvgFAPQb8irLhUyKKM41LRHRGt4DwueAcBRbfQg0sh8v3I1u724HA8QvdRvKqUE2CVbzBHV8xmU4m6z30oSG91PMv8mmcqNP%2FDLE7mN0fdiB%2BwgYUkeFCJVgkfPzETIT0mMKUYyMbNhuVtjR6IIaog8cMW0euJPoapxjikeIpfQgUtLBumi6%2BRYsVXuk%2Fdab7lLfjTsDdERc4Ip3zTJOpFicI9y3evd4jDXokhwYstmAlcQK29mDE4XaZjwrFL1eiCCsIHLHNlAMRXlPQuvl6KBbA8CvZ1DXf6ZZcUlhz0%2BRkQMV8cTialqMvihssvOvyBjo8%2FlzQnyVcfSxWWPPT5vQLZQwO8AZ%2F8kSUwDonXa8OimelAGPua0xkk0XMNDSmb0GOqUBvduT3zoK9s7I1PdxtHOxqWq9FGGG9m54Dcj5giEsA0hJ30D0wUOHHWytN0PoeX26Nnc1qm1pQJlBViACtq9EJKSYTQt1tWYGkajDq7990AH6dVKJg%2FHNrG1EVUtu8P6HbjZ9dMJXgMBm2zygXkwHJ5eoi%2B84NKg85zH9CcHMprfT4obxSf8d2gkCVB5b6fkkRCqy3R0wowO4vWBAFAortKW77dIv&X-Amz-Signature=5bfa750fc99c7b363ca9b610856da38b87406681249f30c828b56901745da956&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEPFQVXL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIAkJ%2F0OD3Jx1S82ALZSXBjc1t3DFaue9Oo%2F7Q3JE2rN7AiEAhvv%2F9wg6RCJokoE%2Bhgi1SbRT7t87gUizGPDw0fuVGyYq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDyuW1afK4X06yUfOircAyVmNb9bmidqVXo74Z4sNq7KsQB0k75EtWtgOz%2FK%2F%2BrrifxFmlN%2FrPOKYpp9nVSUdBx0jSr7BfphTWBkbGxtI1QGrSKk09nGaC0ol5nVdbfz57YOVEftSJWeFXEC6YfeZ0XG72qCAX6nfqg1Xa3fwX6oOxdR6LdVxB2dE4Toezt%2B5U%2F%2FXQSgm10WxFCo7Z9tSa6HKbeBURssv2YHw6osGlHxP1EXdXJCy3yW6ynZGAN4KskRpbgLj2ogeoAFvHQoBKWQU%2FfiEmYf4JQ84iQtaFUkZJC%2FPY0MAWi%2BmxmAyio%2FaKnDAzfCeKQtESESjEmOnu6ED4BG4SADwfQUBBXGqzPpghCJ92xMJBuBTYyt4VlRVkMQjGNOB1Vq58QnpvcD%2B4vSsC8hLbmScQq6NQ07gzNXE%2FQsOyFQCsOCEQ%2F%2BufdhaxgeYWkN5W04b5rNgpWpb7M1zsLY6ttuXGb2NdE1WtO3M47KN%2FyQlis5oVAI%2FvhEsjN3Z3UogAH%2FQoJbwAKIZIHlhVOy%2BKNfC8UDI2mA4tSvL6bnp%2BM1BPPx1%2FgagT1s8wtikWODJeGbgdaWU%2F7lLp7wOeWCwb7UZAHDP2Zt7uCOUYsD0thKg2XmCybsptXzI3kQFlw%2BjURbvZKmMPbSmb0GOqUBMT3rINt%2FeA%2FKORKCwSsWz%2F3CVF%2FDnB00%2BDE1qC2qGIKF3N4B0tf4P3%2BgCBQq7bZP48s7cWXr3JoFgxZFJ4O2V8YjiwBzGSzspDWPgKLOqKocdsLk0p5Jynm8RWtIIG872JhRYZ7%2BL7EUYOUkBD6pJPQq6XmOBUZfGEQOWPQXJY6FngXqGFDqlea8A41xob3FQQV%2FtVUu9wToYKcOfN181G%2B948%2Br&X-Amz-Signature=c01b874982e56f69598a675ece0c042ec0c36d98bdb02edd070f92957585f9f2&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666A6ULA7U%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCICBuTFJR2wIGNmi0i5q5Lj2J38dWMRTzbKUwTnDE1tL7AiEAkg8Zo5luRnaQEi4VUpFU6NHejaYQEoxv4CpYyx4cS4Iq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDOw9iGWCf5mNLZXPLSrcA5QsZkeepmHae1%2BcEmw9aBd9OrqmbTbgeBrykVKZVz6uHIYRGo1zne0W2cfbAsle9aLu8u4t8rYcZ3HBeiUMkJLOIi0eKLGoY%2BMkGJV9mumwKfBw5viZZfXNA%2FJQ2bA1YZPjL505jr%2FGtigU4rchYBJNAR5S6uR7T94dqx1QfqlxvC3TOD%2FvQJK1OMMeD%2F%2BCochant%2BLv2Tcegvu4fnbPZBc3njmsqCqwrGsN7cceOenagZUZN9SxAzO7V4yzuE9ISDx9QEQlPr8TFx4F3uIAiQTvBKdkkfCBIIP5h%2FBuC8QS%2FVCIHSHegri9EBSV1%2FdeWU0RgUecSAmbMU9Le4shWJI1M%2BSIOfMBPuIVI9uz2DBrEV3lw2tDQtXnmXShxSxtKEM%2BgUSP5uuSfGALjdLwZLAoWzxzV6zntYmdSPHfLRV8Uzu2K4XZsdN5qtUre7FYnPslCSOKXiK1qH2IzBMQbd9TM5xgyqgREpYgVutP0JzjNsHAM%2Fm%2BOOLunDca2juEoZlT0oddO3RMWRNi8fA9pfD9epD3GJLOQGS3pGE5apbjkmdUSg74pnGfYQCmVv6TiJt0F%2BfPtcJvIpyQzDzC19Vac7g79X2%2B7NYZGvxdYrEyBNU2swUgVO9yXIUMJS2mb0GOqUBUsbgJVwTEcWvCtlf1skMLjelY02EbzfCVEv6Au1XaxSgctI1TT4rFkWmgFsA8lXxMQ2A7nDKrZVxRyCKIyNGTGTxqsxjfCAxcqbOmSaVT6TJnBwaPZg7ILcBgN53VgECW7jzznpECO1gr%2BBIbHriBtgELNUV3WKF4eqmqE3fssuSsMG8HcihjINwqwknSDga6aKMxAOzqU5DkypHsMb1dpP4RDtN&X-Amz-Signature=ac0b5ea4ee746575b3fe92132938293c885cbe8fd100b5314a0b4ca7f148cef5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGL4ERJK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDsbM1QJ7PhGYBNtdAsB16mYAsiosLkLQ5m%2BZf3LAWv5wIgZYGHnm968K2jS08HU%2B5SKGdPTC%2FpPpZjTis5vjoW%2BTEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFel6VozqWqI3bec%2BSrcA0DFBjYF2pOisiVmpoy964R8jvvD7R%2FhEhnO8%2FrHJrIxbj31SGb%2Fr5gpOddoIVMuZRW5%2BbLaMkpOOF2lEWYiRDMXS9mMPrCthN4QV4sWcDciv1bBMVgrmX0qFMdsXMK0b9Qxnp1n5kLMSj7aAx2kLK18RrT%2Fwo2IQIp3PxOoah5LwHSyw2wIH2Go%2BdaYfuOh6Uwk7teDrImIkdJSlGI%2B%2F2zqUYa65yb08hOTMU5%2FMXBWcPK6D0X1Iivupa3e8WPEZvgFAPQb8irLhUyKKM41LRHRGt4DwueAcBRbfQg0sh8v3I1u724HA8QvdRvKqUE2CVbzBHV8xmU4m6z30oSG91PMv8mmcqNP%2FDLE7mN0fdiB%2BwgYUkeFCJVgkfPzETIT0mMKUYyMbNhuVtjR6IIaog8cMW0euJPoapxjikeIpfQgUtLBumi6%2BRYsVXuk%2Fdab7lLfjTsDdERc4Ip3zTJOpFicI9y3evd4jDXokhwYstmAlcQK29mDE4XaZjwrFL1eiCCsIHLHNlAMRXlPQuvl6KBbA8CvZ1DXf6ZZcUlhz0%2BRkQMV8cTialqMvihssvOvyBjo8%2FlzQnyVcfSxWWPPT5vQLZQwO8AZ%2F8kSUwDonXa8OimelAGPua0xkk0XMNDSmb0GOqUBvduT3zoK9s7I1PdxtHOxqWq9FGGG9m54Dcj5giEsA0hJ30D0wUOHHWytN0PoeX26Nnc1qm1pQJlBViACtq9EJKSYTQt1tWYGkajDq7990AH6dVKJg%2FHNrG1EVUtu8P6HbjZ9dMJXgMBm2zygXkwHJ5eoi%2B84NKg85zH9CcHMprfT4obxSf8d2gkCVB5b6fkkRCqy3R0wowO4vWBAFAortKW77dIv&X-Amz-Signature=7d8a8524d00a876abe29919cf22afd23630a19eb95f57adda242fe45ea263def&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGL4ERJK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDsbM1QJ7PhGYBNtdAsB16mYAsiosLkLQ5m%2BZf3LAWv5wIgZYGHnm968K2jS08HU%2B5SKGdPTC%2FpPpZjTis5vjoW%2BTEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFel6VozqWqI3bec%2BSrcA0DFBjYF2pOisiVmpoy964R8jvvD7R%2FhEhnO8%2FrHJrIxbj31SGb%2Fr5gpOddoIVMuZRW5%2BbLaMkpOOF2lEWYiRDMXS9mMPrCthN4QV4sWcDciv1bBMVgrmX0qFMdsXMK0b9Qxnp1n5kLMSj7aAx2kLK18RrT%2Fwo2IQIp3PxOoah5LwHSyw2wIH2Go%2BdaYfuOh6Uwk7teDrImIkdJSlGI%2B%2F2zqUYa65yb08hOTMU5%2FMXBWcPK6D0X1Iivupa3e8WPEZvgFAPQb8irLhUyKKM41LRHRGt4DwueAcBRbfQg0sh8v3I1u724HA8QvdRvKqUE2CVbzBHV8xmU4m6z30oSG91PMv8mmcqNP%2FDLE7mN0fdiB%2BwgYUkeFCJVgkfPzETIT0mMKUYyMbNhuVtjR6IIaog8cMW0euJPoapxjikeIpfQgUtLBumi6%2BRYsVXuk%2Fdab7lLfjTsDdERc4Ip3zTJOpFicI9y3evd4jDXokhwYstmAlcQK29mDE4XaZjwrFL1eiCCsIHLHNlAMRXlPQuvl6KBbA8CvZ1DXf6ZZcUlhz0%2BRkQMV8cTialqMvihssvOvyBjo8%2FlzQnyVcfSxWWPPT5vQLZQwO8AZ%2F8kSUwDonXa8OimelAGPua0xkk0XMNDSmb0GOqUBvduT3zoK9s7I1PdxtHOxqWq9FGGG9m54Dcj5giEsA0hJ30D0wUOHHWytN0PoeX26Nnc1qm1pQJlBViACtq9EJKSYTQt1tWYGkajDq7990AH6dVKJg%2FHNrG1EVUtu8P6HbjZ9dMJXgMBm2zygXkwHJ5eoi%2B84NKg85zH9CcHMprfT4obxSf8d2gkCVB5b6fkkRCqy3R0wowO4vWBAFAortKW77dIv&X-Amz-Signature=d37641aa9cc8cafa97c3d74db7952f9e94df0c2b393c98d66f0868e1478ef08c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGL4ERJK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQDsbM1QJ7PhGYBNtdAsB16mYAsiosLkLQ5m%2BZf3LAWv5wIgZYGHnm968K2jS08HU%2B5SKGdPTC%2FpPpZjTis5vjoW%2BTEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFel6VozqWqI3bec%2BSrcA0DFBjYF2pOisiVmpoy964R8jvvD7R%2FhEhnO8%2FrHJrIxbj31SGb%2Fr5gpOddoIVMuZRW5%2BbLaMkpOOF2lEWYiRDMXS9mMPrCthN4QV4sWcDciv1bBMVgrmX0qFMdsXMK0b9Qxnp1n5kLMSj7aAx2kLK18RrT%2Fwo2IQIp3PxOoah5LwHSyw2wIH2Go%2BdaYfuOh6Uwk7teDrImIkdJSlGI%2B%2F2zqUYa65yb08hOTMU5%2FMXBWcPK6D0X1Iivupa3e8WPEZvgFAPQb8irLhUyKKM41LRHRGt4DwueAcBRbfQg0sh8v3I1u724HA8QvdRvKqUE2CVbzBHV8xmU4m6z30oSG91PMv8mmcqNP%2FDLE7mN0fdiB%2BwgYUkeFCJVgkfPzETIT0mMKUYyMbNhuVtjR6IIaog8cMW0euJPoapxjikeIpfQgUtLBumi6%2BRYsVXuk%2Fdab7lLfjTsDdERc4Ip3zTJOpFicI9y3evd4jDXokhwYstmAlcQK29mDE4XaZjwrFL1eiCCsIHLHNlAMRXlPQuvl6KBbA8CvZ1DXf6ZZcUlhz0%2BRkQMV8cTialqMvihssvOvyBjo8%2FlzQnyVcfSxWWPPT5vQLZQwO8AZ%2F8kSUwDonXa8OimelAGPua0xkk0XMNDSmb0GOqUBvduT3zoK9s7I1PdxtHOxqWq9FGGG9m54Dcj5giEsA0hJ30D0wUOHHWytN0PoeX26Nnc1qm1pQJlBViACtq9EJKSYTQt1tWYGkajDq7990AH6dVKJg%2FHNrG1EVUtu8P6HbjZ9dMJXgMBm2zygXkwHJ5eoi%2B84NKg85zH9CcHMprfT4obxSf8d2gkCVB5b6fkkRCqy3R0wowO4vWBAFAortKW77dIv&X-Amz-Signature=cde6e348c69bf92fd67aff093c133d92050839d92cb0837d92fa346f675d3ef8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PIYK5MV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIA3pdZUd%2FSevkXdcV6cp22QQo7NtlfU0uYqRRcql2PbYAiBm9mYj2wXUnk%2F0yy5rC0ioxUS2HshZZI1EAg4HAegIrCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMdQXBkqf%2B1pOMcqgtKtwD6DVyplYuRb2VOlG0WGBVIQKrRRBh7V75W02eYfnjFJ4BAcxp8urjyDOkZv93nESLJp1gz92In7MnCmTrkWw6ZKQUhcqGWGJb6WGWQOgYW%2B8fRNn5bHhzZTbssNFdRb%2BIBPFUF3cLraC4nGGToKOihuG1zZ%2F1nLaGxlO67tHNPSeomuHn6jmwqPHC%2BA9c0%2BbwRTOX1WH%2FPTgSebEgBxaziTk%2FReY9xn8AzDBrs7yOlwlnIp0ABxpxGQy8Hc4NmIqwwz4rSSKCn4P8Si7KC7cg0nnm%2F1RdzB4xndVoKZI7l3%2FqM6P6UuhVkWqC5GFgyrdsBz8l%2FIHKe3l61MbuYc0FmSRNghkzfVRLU2QenjfLDqq%2FS1W0OBY%2Bk7JnePocchBIr5que6Nq%2BSZhlYJiq5U5P9WNNZw5HorBooQBiZnWNDbj%2BQzeCIF5OhaB3p4UaEe8d3vfInwbXpW3cVlWtxuiHGb7Sb72svtLF%2F2JNtf3RMMjnO6MED%2FkQ6XhFsShE9Pb9yrJrlK4JEYUbk4gCqZubKRru5GqkWLyQfd6NYBEzDejNjwJ9sWBr5MWl2Dtr92CyaL%2Bdbstqbm11t%2BXlarHPKC1hept002NaRmBIvIyPIipyTQx%2Bl4K18u3dQowttKZvQY6pgGxNTn2cvpqN91ft0f99f3%2F50NZKPx98owkybaAt6B7XQPg9cyWXUNpXhlP0NUOoqzJMARKJfj%2FDH64i3NqgBauAkrWTQCs2H68CwVW3hBjGTcUH7auO0wH9BE1067vGznw1eoJodM%2FOZn3GA3fLLm2SxLEg3boJUSvlE9k85KuWKJ5I2Qo8kQ%2B59f1fUUlPZOnI%2F8Y3XwyXkfQLScLN5OJ9Q%2B0prdZ&X-Amz-Signature=5a4add98c2d10960cbfb2b1c3d2800db306d5e3a2774fe701e44e87874ce1177&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJZ4LVTP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCvxYRh2oZWaIkdz0OELxnFQr3tFSPO0FUFE%2Bwb9M1VDwIgLVsGCaR9BhWZJ6mkpar2BWw52Aj6AdN%2BnHPLlAgxrf8q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDExlGdnYj%2B1KTcgVuircA4Wzy7%2FAPfE8K2KRZ4U2UklihkFb4njqz0goee1UTc07wyT7Qt4yh%2BdpYzBvS0oe115ADtCobYcUdTOmdDneGQ3NSxErsDvvxtkcMQ6b%2FTbUDCXau9fSb8KK%2B19AbbK3wkYvbLDGtYO3KtCmWFdhMsRK3q2yXdwzTkXb8udRD9SLfWjTb9f1XATQat7UfsaG2HXKIkKJsZndMkRp7sl6P%2BfIn3TMaqwkqCG1CPWSjY5Bj5m%2BzRjmaC027%2B%2FcnsFroAtuK2v%2BqXEB1vIA9mnEcOEp3s0jorx4KZct6n2bIx9IwbfDT3asAhpoP4%2Bk2XxLyX%2BkGwWDlXS660WlNFdY4A4dElHYTZTLYtWMV8v2HlTMxBdQBNNtyEJMK440IbDOu36nYP7GUwvXTFpAbsBAPFKh0mZR%2FPlTQ8xppTpRSEEbrkuOnzEWSm%2FXbI6WM6MLgmDrHrqxS799PMizQLXsOk0eZuMnXEIL0J%2FyB2iGon8FxKcHiL2L333LvL1pR0c4Fa0DbbqJqa7%2FTj%2BHZpNsfIFWHRp58n9rKasXxJDebKPbDpNzGfzrsPUzWI%2BI%2BrJ7btVy65F9IBExzlu57n1OmIj5dnHiYhEZY1g%2FUxiPQvljCcFIBwe1jKxtQxHYMKTSmb0GOqUB9bmWnu38Y8qUVuWb8TK%2BH9imyR9M24L991Ti8aRy3%2B9w60EPP015rD8D2lhU0zBMItBgfXnhmjXlHA%2BgfNotAalUHRqM%2FayJo5bq3pRCTTagTRIGHKMWtDDhGQkHBDNwgx3%2Fw3UlVlSD9m5rp9U0xRzzAoriG2cIownALqSxd0FBYc0sBrKxT6HChNcjgSSCDXN%2B3K04piuT9OWAoQ07pyOtN0Gb&X-Amz-Signature=2c8aa0f087364ed5bc0e58b79165a169df666eb4f849cac249a999dd284b4d7a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN7QNDJF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIFdiu0LL8kkQmJKKpstB1QzptJZqOYLF2kgnC3BvvTNIAiEA2kplopq38Sn7GXg%2F9n8rHGA1N4N3oe4aAd4eWvqJBdYq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDKfbe0aglOIt8DbZaircA3q10MbVvOR14n9woGQ79y7G0dnNXoKOWiHKxYgDktzfNKJvkM0lkDu1SfJSkX16J%2BAF5ZOv%2FTGSxS11RAAaCiX2GIx8YIyoI%2FBFDuAVoYzAKm2V0RgF88TahTr9uvb1QiY0PyMstXNOKF1PoxZjVnKOscD1490EdqaOxFdFxxdj0J2AU3ZKuRCH94XGPBjExMpVElGWsTlBobg%2BrVdDq4qq4XixZvCjp18r6dPYT38KvU0iRSKG%2BXhACtzkRZtx1pUMTcs0xHGgomxuCCdUBYPQVcBeTXxeVh3Ls9mY9g53tGXq5IzPcwonDRYuRgJi%2BcdiFOxU0HKeD6OkABpCkG9o0%2F5Vg2oK6JbJ8aHv7qpHXb0sOrbvJQSw0vZ5XLYjnovnP8mOXmIGxVczhg9FLzLmtK3cTM7LdGzLqO%2F0jV6aT%2BB6xl3xybK3MjqYwIgFCKBDhYUSp%2Fi%2FAgPQb%2Fi67PTZPXjoFhhHOxIryvcZTGnr8kOpKt8uGjkpzRXKMBMuKbEJo5fNJrC7EYB3SGveGsgMh%2BD8y0wNNkNkwjPcRNR7Knk4hYK9Y5PfWbVV%2Bqy2AQbf0%2F3mq6FXE3LH8oPWPL8qcJhhD4d4HZgP2DwrENM4WKUG2bIuLswVQDLzMPi1mb0GOqUBTll3zU5UDGCS%2BLvkbBNFtrr45Kj57B1YnBQUn97pyvvBcuhMKxgEeu1ASdetjfHWeEWIe1T0ZD6HqI6H5RO83yiUdVUBt%2BqhEZhN8nN6fbwGMJ%2BI9OB21jYXBKdZJ50kUwJknRVm2TKno6N5GB8nNQSFmLVw2I4pYpZq6RZUf7lF%2BHy4iTZonhpwD8bQXcn8sLdoeGGR%2FoqiDOnoYLAm2sWS7i3O&X-Amz-Signature=50c7cc1c357d6e687abb1841b9d4a368730513e0d7e5eefd4a3d479c727788ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMTG73RW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIELedNFAZli8yQHNafqzO%2FwKTjTVPxBC%2BDCmVPIgKDGWAiBIJF8S5tyMsQvJOxyDf3eeIC7Px43IQ%2FouG6yYRnIR4Cr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIM1xtzbun%2B3mIeqgGfKtwDdai9E4Ww0Xp9NYmHom0F%2Fztfxi0mPdn6ApAcnOBC48pj2GKRF9minIQGpqBmEb0sCp3D3dG9usf%2FXL3ZQTDIkXXtf5WfYtHUyM2ROv5WwssQuqB%2Frz1usLVQWSV76TY65jThYlviSr5I2vKvGxUbOy95qanXJwjqLZJIb0h82HOHlk5K7L0nc6HNnTR6cGopdDm%2Fyp52LCgHnUtudKYIblQJ1WhhxRhlgKXLrR8fLv8XSkeNxjYpTRaDa2Ig85Ko2TkK%2FVjAXP3%2BeaOkROhm%2B7DMzS9MLW41dlonVaD3GDDgy1vRfNNmslY%2Fjvvvnh35Wr%2BoZAJW0ZtMKnLuQE6mi%2FmkCBrFPeAuSq3ONAP6rim2JO3P9KCWd9dIwBGgDkoYNMi6aS7jTdDodlvFfXDdba76hXCSKMFu%2F8R8FTJI0n22VSU6yhrQXyyiQY0NjI1e2ZUhh%2FTMhO4yQ3PXoqv4KmhkZKkYp5y8v%2FHo9iFvqg7aRFI%2BrRnb42EC%2B4sLRvnKn6tSdrqaMN8Zws%2BVvtVPQq8cxxGSBqbZukMUdaq6bH2POLwGDTiukUrKGTTR7L3fCdqmju6oRbmSiRUWwjiNIs6bNecNuGNPupCWM3XO94qN5jhzfFFRmJPUsN0wgtOZvQY6pgEN5U0csaK6Q3d%2Bz7%2FrTZyDa4vff04ZK9a41hdak6NgR5SftvM2ea4ysygkH%2FaPHbnDChKo%2BTft1IMHj%2BLbQMC195M0m%2FRZwg%2BZhG%2B6z3AfKvsdwXQiDxUz%2FXaAGkIuJQBStvdddPvXPC4wpq61MQbM7UPLAbVBc1WpXjnlo6JOf%2FH3A9L40JrwNfDsVPexpl%2BVEmw06uebTLRFvXfOsLXltN14dykT&X-Amz-Signature=6f3e9557e79497d2adaaefd459940b7aad4fdb6af13821909200d1bbaa10943d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMTG73RW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIELedNFAZli8yQHNafqzO%2FwKTjTVPxBC%2BDCmVPIgKDGWAiBIJF8S5tyMsQvJOxyDf3eeIC7Px43IQ%2FouG6yYRnIR4Cr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIM1xtzbun%2B3mIeqgGfKtwDdai9E4Ww0Xp9NYmHom0F%2Fztfxi0mPdn6ApAcnOBC48pj2GKRF9minIQGpqBmEb0sCp3D3dG9usf%2FXL3ZQTDIkXXtf5WfYtHUyM2ROv5WwssQuqB%2Frz1usLVQWSV76TY65jThYlviSr5I2vKvGxUbOy95qanXJwjqLZJIb0h82HOHlk5K7L0nc6HNnTR6cGopdDm%2Fyp52LCgHnUtudKYIblQJ1WhhxRhlgKXLrR8fLv8XSkeNxjYpTRaDa2Ig85Ko2TkK%2FVjAXP3%2BeaOkROhm%2B7DMzS9MLW41dlonVaD3GDDgy1vRfNNmslY%2Fjvvvnh35Wr%2BoZAJW0ZtMKnLuQE6mi%2FmkCBrFPeAuSq3ONAP6rim2JO3P9KCWd9dIwBGgDkoYNMi6aS7jTdDodlvFfXDdba76hXCSKMFu%2F8R8FTJI0n22VSU6yhrQXyyiQY0NjI1e2ZUhh%2FTMhO4yQ3PXoqv4KmhkZKkYp5y8v%2FHo9iFvqg7aRFI%2BrRnb42EC%2B4sLRvnKn6tSdrqaMN8Zws%2BVvtVPQq8cxxGSBqbZukMUdaq6bH2POLwGDTiukUrKGTTR7L3fCdqmju6oRbmSiRUWwjiNIs6bNecNuGNPupCWM3XO94qN5jhzfFFRmJPUsN0wgtOZvQY6pgEN5U0csaK6Q3d%2Bz7%2FrTZyDa4vff04ZK9a41hdak6NgR5SftvM2ea4ysygkH%2FaPHbnDChKo%2BTft1IMHj%2BLbQMC195M0m%2FRZwg%2BZhG%2B6z3AfKvsdwXQiDxUz%2FXaAGkIuJQBStvdddPvXPC4wpq61MQbM7UPLAbVBc1WpXjnlo6JOf%2FH3A9L40JrwNfDsVPexpl%2BVEmw06uebTLRFvXfOsLXltN14dykT&X-Amz-Signature=72b411e97d483be87fc0e2583b963959978e3d9bfa39ec299b53ec3d562d7869&X-Amz-SignedHeaders=host&x-id=GetObject)

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
