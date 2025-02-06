

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654YPQOT4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIHsbTe86HbCoQL7zkM8rSDAfLArDQg%2BarEvbotio%2BUOTAiAC4l2SivwEZ3Ragh24MSEJO5uNQvrru7PHoAhfMJSpBir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMaYkbiHlc5Ld%2BQiKFKtwDS%2FnaNQ%2FqE4NrnF%2BcQ3gPGAo9DLSoIV4vDEABDgQnmvuyTdv1Rqb%2FWkIPLONrzPt7%2F2OG9aOwfuQsn3dv1kfIUF5hkKdNVaz7MBx7pwMZUQnF4dS3wONuC3%2BoYblI6AwLcSA9jk7RIsdz0hhQG7xgwVmifH3r%2BsN%2Fe%2BGQCkgACMHxzN2GB8AsOAESobG6171nTUSLMBESlWWUiQdL3taGbqmUsUhwdksyYLs9xHN1DBDQuoq0e%2BT4fbRBfwhxZj98tBMME%2BtSDHO1Aq72wnzHyobRzuzlZ7XGhF5%2FhALYFKPzhm8cSjOOUPLw%2FSqL6EN%2BJ4%2BFlVO1wcdvfGZWE8FpvcoGPoo5GT8EDF7bqhrcOUIiF4DWTVjcPlRmwGdH8JaZCoHYXgczPDWGEjDa6CQn%2BBwPJlXWoaM%2FEoCryfd0sz3BCIPm1zdv31JSdw0pnBIQmeAYeSdtLIMtcs3zyzRjUQXmaDty8CBLxEVQpSg9ymS%2FJRvcpFFRaOY%2BDaNIam11Tyu3RJLtUsikZYzxIJqDAmnfTg5ZEohaslng2R2gfStPh1zucVo%2BbS5VauZJmSZxTk%2BF1e9yhKG0UWphXQEWY%2Bf3%2BbH%2BN%2F5aDm5tnHluGKksS00hnmw%2F0xKpYVkwq8SSvQY6pgFkEdny9OGTfB%2BYE8p1Y%2F5rIwkY8c4At9YSLN%2BxJWZvZF8I8QZEVnNNYMMYb8UIF8eQIgdkxIFcZC13HNCdfaEf8MDv1OveJf6AdR9Gd2RhtGNC7Y9%2BnhpO85pu792wE9R7EafcZ61QIRHpP5qWOTIx1WxHDWbqoyQfMjhXwG9pQ4cRu21FM0N7iazjaqTZOdm%2Fb4ia2teInEkKCOp8PMGPyqlaRJg3&X-Amz-Signature=d4c503623a47c5382ea0c7ab06746b0feebc5bdaec86338dfd5e19380aba8908&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654YPQOT4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIHsbTe86HbCoQL7zkM8rSDAfLArDQg%2BarEvbotio%2BUOTAiAC4l2SivwEZ3Ragh24MSEJO5uNQvrru7PHoAhfMJSpBir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMaYkbiHlc5Ld%2BQiKFKtwDS%2FnaNQ%2FqE4NrnF%2BcQ3gPGAo9DLSoIV4vDEABDgQnmvuyTdv1Rqb%2FWkIPLONrzPt7%2F2OG9aOwfuQsn3dv1kfIUF5hkKdNVaz7MBx7pwMZUQnF4dS3wONuC3%2BoYblI6AwLcSA9jk7RIsdz0hhQG7xgwVmifH3r%2BsN%2Fe%2BGQCkgACMHxzN2GB8AsOAESobG6171nTUSLMBESlWWUiQdL3taGbqmUsUhwdksyYLs9xHN1DBDQuoq0e%2BT4fbRBfwhxZj98tBMME%2BtSDHO1Aq72wnzHyobRzuzlZ7XGhF5%2FhALYFKPzhm8cSjOOUPLw%2FSqL6EN%2BJ4%2BFlVO1wcdvfGZWE8FpvcoGPoo5GT8EDF7bqhrcOUIiF4DWTVjcPlRmwGdH8JaZCoHYXgczPDWGEjDa6CQn%2BBwPJlXWoaM%2FEoCryfd0sz3BCIPm1zdv31JSdw0pnBIQmeAYeSdtLIMtcs3zyzRjUQXmaDty8CBLxEVQpSg9ymS%2FJRvcpFFRaOY%2BDaNIam11Tyu3RJLtUsikZYzxIJqDAmnfTg5ZEohaslng2R2gfStPh1zucVo%2BbS5VauZJmSZxTk%2BF1e9yhKG0UWphXQEWY%2Bf3%2BbH%2BN%2F5aDm5tnHluGKksS00hnmw%2F0xKpYVkwq8SSvQY6pgFkEdny9OGTfB%2BYE8p1Y%2F5rIwkY8c4At9YSLN%2BxJWZvZF8I8QZEVnNNYMMYb8UIF8eQIgdkxIFcZC13HNCdfaEf8MDv1OveJf6AdR9Gd2RhtGNC7Y9%2BnhpO85pu792wE9R7EafcZ61QIRHpP5qWOTIx1WxHDWbqoyQfMjhXwG9pQ4cRu21FM0N7iazjaqTZOdm%2Fb4ia2teInEkKCOp8PMGPyqlaRJg3&X-Amz-Signature=2ec4404da9640c9a23aac24e90a381a67fcf0296d049013dd16aa86e6df81148&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654YPQOT4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIHsbTe86HbCoQL7zkM8rSDAfLArDQg%2BarEvbotio%2BUOTAiAC4l2SivwEZ3Ragh24MSEJO5uNQvrru7PHoAhfMJSpBir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMaYkbiHlc5Ld%2BQiKFKtwDS%2FnaNQ%2FqE4NrnF%2BcQ3gPGAo9DLSoIV4vDEABDgQnmvuyTdv1Rqb%2FWkIPLONrzPt7%2F2OG9aOwfuQsn3dv1kfIUF5hkKdNVaz7MBx7pwMZUQnF4dS3wONuC3%2BoYblI6AwLcSA9jk7RIsdz0hhQG7xgwVmifH3r%2BsN%2Fe%2BGQCkgACMHxzN2GB8AsOAESobG6171nTUSLMBESlWWUiQdL3taGbqmUsUhwdksyYLs9xHN1DBDQuoq0e%2BT4fbRBfwhxZj98tBMME%2BtSDHO1Aq72wnzHyobRzuzlZ7XGhF5%2FhALYFKPzhm8cSjOOUPLw%2FSqL6EN%2BJ4%2BFlVO1wcdvfGZWE8FpvcoGPoo5GT8EDF7bqhrcOUIiF4DWTVjcPlRmwGdH8JaZCoHYXgczPDWGEjDa6CQn%2BBwPJlXWoaM%2FEoCryfd0sz3BCIPm1zdv31JSdw0pnBIQmeAYeSdtLIMtcs3zyzRjUQXmaDty8CBLxEVQpSg9ymS%2FJRvcpFFRaOY%2BDaNIam11Tyu3RJLtUsikZYzxIJqDAmnfTg5ZEohaslng2R2gfStPh1zucVo%2BbS5VauZJmSZxTk%2BF1e9yhKG0UWphXQEWY%2Bf3%2BbH%2BN%2F5aDm5tnHluGKksS00hnmw%2F0xKpYVkwq8SSvQY6pgFkEdny9OGTfB%2BYE8p1Y%2F5rIwkY8c4At9YSLN%2BxJWZvZF8I8QZEVnNNYMMYb8UIF8eQIgdkxIFcZC13HNCdfaEf8MDv1OveJf6AdR9Gd2RhtGNC7Y9%2BnhpO85pu792wE9R7EafcZ61QIRHpP5qWOTIx1WxHDWbqoyQfMjhXwG9pQ4cRu21FM0N7iazjaqTZOdm%2Fb4ia2teInEkKCOp8PMGPyqlaRJg3&X-Amz-Signature=fc11bececa986ec15d2445984002402ba844fc5ee1e6cf52a40088511d8c1369&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A22YZZI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC%2Fejx51%2BZkRp7oC3AiT68PEiGliHvGAk1A%2FJ5Bn84YhAIhAIaC0JCYpOsZePBThSzl3A7ivlcahsChynkJCBntLZ1eKv8DCF0QABoMNjM3NDIzMTgzODA1IgzSJMVJY9fjkdzmYIMq3AMsjWxvy5GoPjA32f8PeSKm2Bv83YWQeZYQJk6ucNwSL5IyT5F97pYXqi6sfraNFP50QKzrZk3%2FV9DfMzBw9qMiw%2F62GvpWZM6sGvo9eV7e3HETRBw1AkPImaG0GZdOgovEmjMDjthrJermncSriiSPbLj2sOGnYVMuUCzB1KWjIMZhYmQnKkqz5rbFi8juwVlh1Di0xLjSKzK8W9hCwo4pSXMjOV8tS0gNLidQCbXaiXTWYpIbvRPW5kVkXpHEkeTkPImdtENoNKwKgP8rDe3G%2BY10EkdR9d8HAbIalzrw7qVSddSOmAnyLhofOT6qLdR553RxcsFYsJWLFR4TNktHBYaFHndzOGdkLd0qHo9sjqyqeASTezNjs7PyIh%2BX5AN75MDgi%2FC79lZscBTYiCccr5rPb5bFJ1n7lClDRy0uBFwjUpcVAZ%2Fnj5QT4ZL0c9GDaBuCcBjY1oB67adDZMAYxbVODKBIe7GnfwC33iG7vGtraK2iOsveltAdqqhM1Z440gSInz2VsttgOG%2BkyQn2viqzOpPKxGMepndPcCK18i7zQ83yAPoNJjBUF3QEPZ%2BrA4R7LxrBZMoW5lzXwOiSwSj%2BzG%2BNTM2Up62aYo6FsOPekvU%2FeS3Z0bEC5TCVxJK9BjqkAUka5NRTRBR%2Ftrg96WnV%2FxtL3K1g5alosXiYpni%2FJj671mgXcj%2FjnkcLB3d9CshYDBgQ9vrJ5%2BVjDzk2jC33uk%2Bd0%2BjwweiKQIcyhyAuVTULlz3hD1vEmTyT%2BRG0OPshiAWp%2F%2F1ZT%2ByKR%2BSEK3UxYThHTz%2Beg9K8VXQhdYvKQFWExK48nbHhtwdZpU5meF1hJmh8pvvw35pC2R%2B5auzQTowIAaiS&X-Amz-Signature=cef9589c2975c5ffc9a0c8be9ac61597bf79751470e810ef84031a1821433e8c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A22YZZI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC%2Fejx51%2BZkRp7oC3AiT68PEiGliHvGAk1A%2FJ5Bn84YhAIhAIaC0JCYpOsZePBThSzl3A7ivlcahsChynkJCBntLZ1eKv8DCF0QABoMNjM3NDIzMTgzODA1IgzSJMVJY9fjkdzmYIMq3AMsjWxvy5GoPjA32f8PeSKm2Bv83YWQeZYQJk6ucNwSL5IyT5F97pYXqi6sfraNFP50QKzrZk3%2FV9DfMzBw9qMiw%2F62GvpWZM6sGvo9eV7e3HETRBw1AkPImaG0GZdOgovEmjMDjthrJermncSriiSPbLj2sOGnYVMuUCzB1KWjIMZhYmQnKkqz5rbFi8juwVlh1Di0xLjSKzK8W9hCwo4pSXMjOV8tS0gNLidQCbXaiXTWYpIbvRPW5kVkXpHEkeTkPImdtENoNKwKgP8rDe3G%2BY10EkdR9d8HAbIalzrw7qVSddSOmAnyLhofOT6qLdR553RxcsFYsJWLFR4TNktHBYaFHndzOGdkLd0qHo9sjqyqeASTezNjs7PyIh%2BX5AN75MDgi%2FC79lZscBTYiCccr5rPb5bFJ1n7lClDRy0uBFwjUpcVAZ%2Fnj5QT4ZL0c9GDaBuCcBjY1oB67adDZMAYxbVODKBIe7GnfwC33iG7vGtraK2iOsveltAdqqhM1Z440gSInz2VsttgOG%2BkyQn2viqzOpPKxGMepndPcCK18i7zQ83yAPoNJjBUF3QEPZ%2BrA4R7LxrBZMoW5lzXwOiSwSj%2BzG%2BNTM2Up62aYo6FsOPekvU%2FeS3Z0bEC5TCVxJK9BjqkAUka5NRTRBR%2Ftrg96WnV%2FxtL3K1g5alosXiYpni%2FJj671mgXcj%2FjnkcLB3d9CshYDBgQ9vrJ5%2BVjDzk2jC33uk%2Bd0%2BjwweiKQIcyhyAuVTULlz3hD1vEmTyT%2BRG0OPshiAWp%2F%2F1ZT%2ByKR%2BSEK3UxYThHTz%2Beg9K8VXQhdYvKQFWExK48nbHhtwdZpU5meF1hJmh8pvvw35pC2R%2B5auzQTowIAaiS&X-Amz-Signature=ee00009f8fd8391dbe6850ed179ce6130e0e64af9a94296365ad1a02c6dedc7b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A22YZZI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC%2Fejx51%2BZkRp7oC3AiT68PEiGliHvGAk1A%2FJ5Bn84YhAIhAIaC0JCYpOsZePBThSzl3A7ivlcahsChynkJCBntLZ1eKv8DCF0QABoMNjM3NDIzMTgzODA1IgzSJMVJY9fjkdzmYIMq3AMsjWxvy5GoPjA32f8PeSKm2Bv83YWQeZYQJk6ucNwSL5IyT5F97pYXqi6sfraNFP50QKzrZk3%2FV9DfMzBw9qMiw%2F62GvpWZM6sGvo9eV7e3HETRBw1AkPImaG0GZdOgovEmjMDjthrJermncSriiSPbLj2sOGnYVMuUCzB1KWjIMZhYmQnKkqz5rbFi8juwVlh1Di0xLjSKzK8W9hCwo4pSXMjOV8tS0gNLidQCbXaiXTWYpIbvRPW5kVkXpHEkeTkPImdtENoNKwKgP8rDe3G%2BY10EkdR9d8HAbIalzrw7qVSddSOmAnyLhofOT6qLdR553RxcsFYsJWLFR4TNktHBYaFHndzOGdkLd0qHo9sjqyqeASTezNjs7PyIh%2BX5AN75MDgi%2FC79lZscBTYiCccr5rPb5bFJ1n7lClDRy0uBFwjUpcVAZ%2Fnj5QT4ZL0c9GDaBuCcBjY1oB67adDZMAYxbVODKBIe7GnfwC33iG7vGtraK2iOsveltAdqqhM1Z440gSInz2VsttgOG%2BkyQn2viqzOpPKxGMepndPcCK18i7zQ83yAPoNJjBUF3QEPZ%2BrA4R7LxrBZMoW5lzXwOiSwSj%2BzG%2BNTM2Up62aYo6FsOPekvU%2FeS3Z0bEC5TCVxJK9BjqkAUka5NRTRBR%2Ftrg96WnV%2FxtL3K1g5alosXiYpni%2FJj671mgXcj%2FjnkcLB3d9CshYDBgQ9vrJ5%2BVjDzk2jC33uk%2Bd0%2BjwweiKQIcyhyAuVTULlz3hD1vEmTyT%2BRG0OPshiAWp%2F%2F1ZT%2ByKR%2BSEK3UxYThHTz%2Beg9K8VXQhdYvKQFWExK48nbHhtwdZpU5meF1hJmh8pvvw35pC2R%2B5auzQTowIAaiS&X-Amz-Signature=5e8c37d2e57b65c2f401d2a7528b69684f1f861de0a03154e6ad5a5ab81509a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A22YZZI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC%2Fejx51%2BZkRp7oC3AiT68PEiGliHvGAk1A%2FJ5Bn84YhAIhAIaC0JCYpOsZePBThSzl3A7ivlcahsChynkJCBntLZ1eKv8DCF0QABoMNjM3NDIzMTgzODA1IgzSJMVJY9fjkdzmYIMq3AMsjWxvy5GoPjA32f8PeSKm2Bv83YWQeZYQJk6ucNwSL5IyT5F97pYXqi6sfraNFP50QKzrZk3%2FV9DfMzBw9qMiw%2F62GvpWZM6sGvo9eV7e3HETRBw1AkPImaG0GZdOgovEmjMDjthrJermncSriiSPbLj2sOGnYVMuUCzB1KWjIMZhYmQnKkqz5rbFi8juwVlh1Di0xLjSKzK8W9hCwo4pSXMjOV8tS0gNLidQCbXaiXTWYpIbvRPW5kVkXpHEkeTkPImdtENoNKwKgP8rDe3G%2BY10EkdR9d8HAbIalzrw7qVSddSOmAnyLhofOT6qLdR553RxcsFYsJWLFR4TNktHBYaFHndzOGdkLd0qHo9sjqyqeASTezNjs7PyIh%2BX5AN75MDgi%2FC79lZscBTYiCccr5rPb5bFJ1n7lClDRy0uBFwjUpcVAZ%2Fnj5QT4ZL0c9GDaBuCcBjY1oB67adDZMAYxbVODKBIe7GnfwC33iG7vGtraK2iOsveltAdqqhM1Z440gSInz2VsttgOG%2BkyQn2viqzOpPKxGMepndPcCK18i7zQ83yAPoNJjBUF3QEPZ%2BrA4R7LxrBZMoW5lzXwOiSwSj%2BzG%2BNTM2Up62aYo6FsOPekvU%2FeS3Z0bEC5TCVxJK9BjqkAUka5NRTRBR%2Ftrg96WnV%2FxtL3K1g5alosXiYpni%2FJj671mgXcj%2FjnkcLB3d9CshYDBgQ9vrJ5%2BVjDzk2jC33uk%2Bd0%2BjwweiKQIcyhyAuVTULlz3hD1vEmTyT%2BRG0OPshiAWp%2F%2F1ZT%2ByKR%2BSEK3UxYThHTz%2Beg9K8VXQhdYvKQFWExK48nbHhtwdZpU5meF1hJmh8pvvw35pC2R%2B5auzQTowIAaiS&X-Amz-Signature=5102c7cbf4cbecd738b09198a46cd8948c4bd3493141e4cb4054e6996e4f36b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A22YZZI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC%2Fejx51%2BZkRp7oC3AiT68PEiGliHvGAk1A%2FJ5Bn84YhAIhAIaC0JCYpOsZePBThSzl3A7ivlcahsChynkJCBntLZ1eKv8DCF0QABoMNjM3NDIzMTgzODA1IgzSJMVJY9fjkdzmYIMq3AMsjWxvy5GoPjA32f8PeSKm2Bv83YWQeZYQJk6ucNwSL5IyT5F97pYXqi6sfraNFP50QKzrZk3%2FV9DfMzBw9qMiw%2F62GvpWZM6sGvo9eV7e3HETRBw1AkPImaG0GZdOgovEmjMDjthrJermncSriiSPbLj2sOGnYVMuUCzB1KWjIMZhYmQnKkqz5rbFi8juwVlh1Di0xLjSKzK8W9hCwo4pSXMjOV8tS0gNLidQCbXaiXTWYpIbvRPW5kVkXpHEkeTkPImdtENoNKwKgP8rDe3G%2BY10EkdR9d8HAbIalzrw7qVSddSOmAnyLhofOT6qLdR553RxcsFYsJWLFR4TNktHBYaFHndzOGdkLd0qHo9sjqyqeASTezNjs7PyIh%2BX5AN75MDgi%2FC79lZscBTYiCccr5rPb5bFJ1n7lClDRy0uBFwjUpcVAZ%2Fnj5QT4ZL0c9GDaBuCcBjY1oB67adDZMAYxbVODKBIe7GnfwC33iG7vGtraK2iOsveltAdqqhM1Z440gSInz2VsttgOG%2BkyQn2viqzOpPKxGMepndPcCK18i7zQ83yAPoNJjBUF3QEPZ%2BrA4R7LxrBZMoW5lzXwOiSwSj%2BzG%2BNTM2Up62aYo6FsOPekvU%2FeS3Z0bEC5TCVxJK9BjqkAUka5NRTRBR%2Ftrg96WnV%2FxtL3K1g5alosXiYpni%2FJj671mgXcj%2FjnkcLB3d9CshYDBgQ9vrJ5%2BVjDzk2jC33uk%2Bd0%2BjwweiKQIcyhyAuVTULlz3hD1vEmTyT%2BRG0OPshiAWp%2F%2F1ZT%2ByKR%2BSEK3UxYThHTz%2Beg9K8VXQhdYvKQFWExK48nbHhtwdZpU5meF1hJmh8pvvw35pC2R%2B5auzQTowIAaiS&X-Amz-Signature=64c5a3ecc8c7162cb606dd563aac418280a38944547f00da9722edb92c0d7771&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A22YZZI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC%2Fejx51%2BZkRp7oC3AiT68PEiGliHvGAk1A%2FJ5Bn84YhAIhAIaC0JCYpOsZePBThSzl3A7ivlcahsChynkJCBntLZ1eKv8DCF0QABoMNjM3NDIzMTgzODA1IgzSJMVJY9fjkdzmYIMq3AMsjWxvy5GoPjA32f8PeSKm2Bv83YWQeZYQJk6ucNwSL5IyT5F97pYXqi6sfraNFP50QKzrZk3%2FV9DfMzBw9qMiw%2F62GvpWZM6sGvo9eV7e3HETRBw1AkPImaG0GZdOgovEmjMDjthrJermncSriiSPbLj2sOGnYVMuUCzB1KWjIMZhYmQnKkqz5rbFi8juwVlh1Di0xLjSKzK8W9hCwo4pSXMjOV8tS0gNLidQCbXaiXTWYpIbvRPW5kVkXpHEkeTkPImdtENoNKwKgP8rDe3G%2BY10EkdR9d8HAbIalzrw7qVSddSOmAnyLhofOT6qLdR553RxcsFYsJWLFR4TNktHBYaFHndzOGdkLd0qHo9sjqyqeASTezNjs7PyIh%2BX5AN75MDgi%2FC79lZscBTYiCccr5rPb5bFJ1n7lClDRy0uBFwjUpcVAZ%2Fnj5QT4ZL0c9GDaBuCcBjY1oB67adDZMAYxbVODKBIe7GnfwC33iG7vGtraK2iOsveltAdqqhM1Z440gSInz2VsttgOG%2BkyQn2viqzOpPKxGMepndPcCK18i7zQ83yAPoNJjBUF3QEPZ%2BrA4R7LxrBZMoW5lzXwOiSwSj%2BzG%2BNTM2Up62aYo6FsOPekvU%2FeS3Z0bEC5TCVxJK9BjqkAUka5NRTRBR%2Ftrg96WnV%2FxtL3K1g5alosXiYpni%2FJj671mgXcj%2FjnkcLB3d9CshYDBgQ9vrJ5%2BVjDzk2jC33uk%2Bd0%2BjwweiKQIcyhyAuVTULlz3hD1vEmTyT%2BRG0OPshiAWp%2F%2F1ZT%2ByKR%2BSEK3UxYThHTz%2Beg9K8VXQhdYvKQFWExK48nbHhtwdZpU5meF1hJmh8pvvw35pC2R%2B5auzQTowIAaiS&X-Amz-Signature=c2cc73460ee5aac5ddeaade55c57bec0c2fc684fc645e4ca9364f1d876e90b6d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IZ7HFYW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIGRES7qV1wzi74Cp0WDryREyCWPuCL8ONam5ErLiuFC4AiAXlMw0lHuogKMHI0v4MfJ7WvJ3Z%2Bk5KmHkHXUqsU62oCr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMp%2BgAJqKudzLC7kgpKtwDrAEylACpP%2FUiBODD7hjDR7NxVUNsGE6j65us0oJomVBdHPX9imHHjVjIryKpjDj9FRay2uZN4WnteD47ws8vecHrCdVVa8Zv4hn25W%2FEqHgeqSrssuSg7N3RAPt8ENTRtzV8sUOgnwQh6NxmvnP4afs3WkziTfU%2F%2FjlMIMdNsSQf%2FCWdDD9wZnSReu7dd8lp%2BeWBMftLhwrNJzWWXkY7khcxGSNOJ9MsxNnBq%2BzPFDEoPJaP0okedX5hAVVr5GdH5JJtej5K0Z2LoeIA7KyV%2BMsIGBcXQnnyMafWKfPEbbtkrGAM6NRLvX8MVFMgfxxWTsyvjESYod852sySLk00NJeH%2Bp6jVxSOn6Eb9GKE245MkbX1B%2FVYGmH1DsOGBNOl9CJZ%2FQKu9l%2FQljZQxg%2FvViOmIbEOb%2FTxR0F0DyUqCuOTfwOSJ4aKjSL7IyF%2FSjK%2Fb2YLkZirdSqbC4tighX68EQLDqScpugXl0IS7xIM0HEOisBsHoguTgczfjgKNO8%2FH6Abp3EWT%2Bna9CXWXwqWIIsWD7zVzPIbaCeLUr6PSNtBfVVmUDwUkDO%2B2M8nneL8oQzHtyJuaBVpqurrjFq%2FIL%2Bqovc63IThB4Et%2B63E7smQSOhFqQCDzopHNtEw%2FMOSvQY6pgGHNjroPJ0p3Np1VvHsrkznbXAnS%2FfpZPeUDEx3Bvt5VdhThGj5hhcEhLxbCOjnGkOghPZNeJLZDSjtu4ZWRhjKx%2BcskgakcY9KcNJeZ6w2Ck3ggDaeVeNTcN3Meaazp7JFy%2FXdfvk2o5HQiJNADbfOdZHuaT9IxxCYh88RVOgqY60seKWzx%2FHdZeAJvwimfLW4gDjbTvdS3a7lyrQD7QXY4nPMHk17&X-Amz-Signature=e1ad9fccd3712dcd1b47b59ae0b709bbd600558b4d43afb7a663f4eb4076c345&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647GA7SI6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIH7ewdhpGcn4pYJbDpJO9JmLjqB22cld4x%2FnldSi5WKuAiEAtuBR%2Fj%2FbhI7DLiiLjA9hQ1jhnKWLAxh3TRuX5f1%2BdrYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDLE5vvnKvI6HLZO0NircAzyNA9u8pVFPlqOiSQYQ1WZWacQ3g7MvqQWfLtFBqX4RhV4LDyjlz1ZZwr7D8UY6oF3qbbjNCMVWRgD39AfQfgUzntal%2F3VGarYis5852FGcsqTlbbUzLHFBijFiFgMoSwEEbaV5kB%2BpytgEndJWx8lo8nDoU6O3%2FfVjr4Q4ycHJvqtF3%2F9%2Fw%2BrD9%2F%2F5R5yyBVfWjf0dnmoNlmpMvHwxp3voEcKFHI4wqezdLio1KHa2INf6R0FMDTlO2%2FAtdYFJCgfq2fuhtLq7bv%2FCn2%2BbbhDlIrkrWZXdfanPvhj4z0kAy71FNQUCwpji6XKHeyYMpH3J4qnR4T0Y%2Bd9AOas%2FXe589G4gnVugnMXKLi6jrqMvArnWo1jrnzQd%2FjTRcB7WncHxvSBkFW2agWdc0CPJu0WT6cIuWnw%2BNRi1D1Wi9wmvcDfgAuMCRGjBaZc6ARMA%2B3RYuuTJuy6%2BusAvixwuSV91cHvd6bqqWjxSpGEdL1PGgMModUU4RlMmROYKM%2BTTwnhbuZPqiMFxd%2Bd4Q6ig20pepAH85hujkQxnO%2F2kHLrtBxmoZqAgd1OJ8QfIpsVRPhlR9XxzTdS9IdY23btqNI5r1ORXfSJCewP85wu0lvI12LqUnTVlDZ4xN1jgMNbDkr0GOqUBRxCrqW8LolHm4X7tXP2EnPVKiwAMucKLN2bjeMd1nTDvlCb4JkWakSDIRCtSPaMwN8Ih9%2FpPQWm8v3b9rzLw5Zl7ddWSZQF1wC3lsaTIbQzi7N%2BfPc%2FyNqjbw%2FWL6s8eqAI6%2F2kejJSryUDRKNWmPFTHBusD5Pl%2BzHcbX%2BHwkQm7NzrbagW9O73gUlFqscO0XN8EGbOOKMmPsc2dAKpZ3AV3Dsvw&X-Amz-Signature=f09478914c21e534fb75fa918e2439ad2481ac23dc8987f472cf583edd0729e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A22YZZI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC%2Fejx51%2BZkRp7oC3AiT68PEiGliHvGAk1A%2FJ5Bn84YhAIhAIaC0JCYpOsZePBThSzl3A7ivlcahsChynkJCBntLZ1eKv8DCF0QABoMNjM3NDIzMTgzODA1IgzSJMVJY9fjkdzmYIMq3AMsjWxvy5GoPjA32f8PeSKm2Bv83YWQeZYQJk6ucNwSL5IyT5F97pYXqi6sfraNFP50QKzrZk3%2FV9DfMzBw9qMiw%2F62GvpWZM6sGvo9eV7e3HETRBw1AkPImaG0GZdOgovEmjMDjthrJermncSriiSPbLj2sOGnYVMuUCzB1KWjIMZhYmQnKkqz5rbFi8juwVlh1Di0xLjSKzK8W9hCwo4pSXMjOV8tS0gNLidQCbXaiXTWYpIbvRPW5kVkXpHEkeTkPImdtENoNKwKgP8rDe3G%2BY10EkdR9d8HAbIalzrw7qVSddSOmAnyLhofOT6qLdR553RxcsFYsJWLFR4TNktHBYaFHndzOGdkLd0qHo9sjqyqeASTezNjs7PyIh%2BX5AN75MDgi%2FC79lZscBTYiCccr5rPb5bFJ1n7lClDRy0uBFwjUpcVAZ%2Fnj5QT4ZL0c9GDaBuCcBjY1oB67adDZMAYxbVODKBIe7GnfwC33iG7vGtraK2iOsveltAdqqhM1Z440gSInz2VsttgOG%2BkyQn2viqzOpPKxGMepndPcCK18i7zQ83yAPoNJjBUF3QEPZ%2BrA4R7LxrBZMoW5lzXwOiSwSj%2BzG%2BNTM2Up62aYo6FsOPekvU%2FeS3Z0bEC5TCVxJK9BjqkAUka5NRTRBR%2Ftrg96WnV%2FxtL3K1g5alosXiYpni%2FJj671mgXcj%2FjnkcLB3d9CshYDBgQ9vrJ5%2BVjDzk2jC33uk%2Bd0%2BjwweiKQIcyhyAuVTULlz3hD1vEmTyT%2BRG0OPshiAWp%2F%2F1ZT%2ByKR%2BSEK3UxYThHTz%2Beg9K8VXQhdYvKQFWExK48nbHhtwdZpU5meF1hJmh8pvvw35pC2R%2B5auzQTowIAaiS&X-Amz-Signature=776d79301c411c9d2f268126f3695507b880b45c20cac76f8e8edcfe076c5e00&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A22YZZI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC%2Fejx51%2BZkRp7oC3AiT68PEiGliHvGAk1A%2FJ5Bn84YhAIhAIaC0JCYpOsZePBThSzl3A7ivlcahsChynkJCBntLZ1eKv8DCF0QABoMNjM3NDIzMTgzODA1IgzSJMVJY9fjkdzmYIMq3AMsjWxvy5GoPjA32f8PeSKm2Bv83YWQeZYQJk6ucNwSL5IyT5F97pYXqi6sfraNFP50QKzrZk3%2FV9DfMzBw9qMiw%2F62GvpWZM6sGvo9eV7e3HETRBw1AkPImaG0GZdOgovEmjMDjthrJermncSriiSPbLj2sOGnYVMuUCzB1KWjIMZhYmQnKkqz5rbFi8juwVlh1Di0xLjSKzK8W9hCwo4pSXMjOV8tS0gNLidQCbXaiXTWYpIbvRPW5kVkXpHEkeTkPImdtENoNKwKgP8rDe3G%2BY10EkdR9d8HAbIalzrw7qVSddSOmAnyLhofOT6qLdR553RxcsFYsJWLFR4TNktHBYaFHndzOGdkLd0qHo9sjqyqeASTezNjs7PyIh%2BX5AN75MDgi%2FC79lZscBTYiCccr5rPb5bFJ1n7lClDRy0uBFwjUpcVAZ%2Fnj5QT4ZL0c9GDaBuCcBjY1oB67adDZMAYxbVODKBIe7GnfwC33iG7vGtraK2iOsveltAdqqhM1Z440gSInz2VsttgOG%2BkyQn2viqzOpPKxGMepndPcCK18i7zQ83yAPoNJjBUF3QEPZ%2BrA4R7LxrBZMoW5lzXwOiSwSj%2BzG%2BNTM2Up62aYo6FsOPekvU%2FeS3Z0bEC5TCVxJK9BjqkAUka5NRTRBR%2Ftrg96WnV%2FxtL3K1g5alosXiYpni%2FJj671mgXcj%2FjnkcLB3d9CshYDBgQ9vrJ5%2BVjDzk2jC33uk%2Bd0%2BjwweiKQIcyhyAuVTULlz3hD1vEmTyT%2BRG0OPshiAWp%2F%2F1ZT%2ByKR%2BSEK3UxYThHTz%2Beg9K8VXQhdYvKQFWExK48nbHhtwdZpU5meF1hJmh8pvvw35pC2R%2B5auzQTowIAaiS&X-Amz-Signature=817f74d8ca042eb873394d486f78240c3e0e377e6ab13914b413c16720fb2262&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A22YZZI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC%2Fejx51%2BZkRp7oC3AiT68PEiGliHvGAk1A%2FJ5Bn84YhAIhAIaC0JCYpOsZePBThSzl3A7ivlcahsChynkJCBntLZ1eKv8DCF0QABoMNjM3NDIzMTgzODA1IgzSJMVJY9fjkdzmYIMq3AMsjWxvy5GoPjA32f8PeSKm2Bv83YWQeZYQJk6ucNwSL5IyT5F97pYXqi6sfraNFP50QKzrZk3%2FV9DfMzBw9qMiw%2F62GvpWZM6sGvo9eV7e3HETRBw1AkPImaG0GZdOgovEmjMDjthrJermncSriiSPbLj2sOGnYVMuUCzB1KWjIMZhYmQnKkqz5rbFi8juwVlh1Di0xLjSKzK8W9hCwo4pSXMjOV8tS0gNLidQCbXaiXTWYpIbvRPW5kVkXpHEkeTkPImdtENoNKwKgP8rDe3G%2BY10EkdR9d8HAbIalzrw7qVSddSOmAnyLhofOT6qLdR553RxcsFYsJWLFR4TNktHBYaFHndzOGdkLd0qHo9sjqyqeASTezNjs7PyIh%2BX5AN75MDgi%2FC79lZscBTYiCccr5rPb5bFJ1n7lClDRy0uBFwjUpcVAZ%2Fnj5QT4ZL0c9GDaBuCcBjY1oB67adDZMAYxbVODKBIe7GnfwC33iG7vGtraK2iOsveltAdqqhM1Z440gSInz2VsttgOG%2BkyQn2viqzOpPKxGMepndPcCK18i7zQ83yAPoNJjBUF3QEPZ%2BrA4R7LxrBZMoW5lzXwOiSwSj%2BzG%2BNTM2Up62aYo6FsOPekvU%2FeS3Z0bEC5TCVxJK9BjqkAUka5NRTRBR%2Ftrg96WnV%2FxtL3K1g5alosXiYpni%2FJj671mgXcj%2FjnkcLB3d9CshYDBgQ9vrJ5%2BVjDzk2jC33uk%2Bd0%2BjwweiKQIcyhyAuVTULlz3hD1vEmTyT%2BRG0OPshiAWp%2F%2F1ZT%2ByKR%2BSEK3UxYThHTz%2Beg9K8VXQhdYvKQFWExK48nbHhtwdZpU5meF1hJmh8pvvw35pC2R%2B5auzQTowIAaiS&X-Amz-Signature=0cd14db1c25cc9d3e190d24e0799ab721296d9c34d205d28a6cb4df6478d0088&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDX435DH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIFcMsQi%2Fg4NMyGQGOkT7zs9h1cFIwYJqaqNxr8mJ46M5AiEApivFu3MyGcXF6Dv2nF2gAILGRn3G1P%2B13a0BI18D0qwq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDJ6SOmCM1RlraZaBLircAxoVOVlv3tb3Ko4kVhebdl3oSi3AAgCcEr5VAlhzardvltEdeCWnv6F9lvBb0cU%2Bo3dK5jWfftYxIz2I31XBDm6d6N8F8rweI5kl0VoAtRs%2BPWEYtCyX8jTNfyI1sME4oPMYgDNCoBqp87hwPlGWJRj8JSqUebGS6iQJ%2FyrqzFKDNd2vmrS3Jg8ibbirV9pY%2FrNTUbaOnGaZcbQhFO3QHyZPoDNXjpeW3AMycgN25ayakiIZojfF14ZHXmYI7RrG3rjM2gIvLVHbX14z%2FAlLMOnKnCYUbOH9hOx2v8kTzyIAthXCCfMS5yrxEDa%2Fze5f0cvaXDvm%2Bmt%2Bytd5GHeJCNtQswIU1mr3wUl6A4Sltpg0cj0kiLYQPz4KcMMKO2U9aaSNClZ%2FvQOppE%2BA2STepcfKdpr0bFvwzSdKzz55k97lmj%2By6At1wa479HgtVoHoFjKdh75O3rDEd75aANPXsh0swmxY2q8dMXThcfOq7UWWY6NG8VBszqY0ysFTybQKD8zstDPjYbVL%2FNZcOaerzvcn0EuXWAcnHszCSZbeTvS2lcpgsndl7iYHq3Fz3qiZsn4Em1fbdoXA%2FBKX0foYOMKvIxYc9XJM7%2FCB9dvSdij6MgobNMrHGZdw7MjiMIzEkr0GOqUBPYkfow%2BfQKF1Oy1uQ54r6L8QqqTfKpkUlzvrIny%2FX70QfU2Pzyk9lANhOd2MKIgI1m4HTK0ZbbjEhWBzLNjdMHx63z39%2FIi9LIBGUBQeqqxun4jCrfVNz%2FkhUEGFaJ2QXC3kXRIKC7zANf157L%2Fl1ELttHQiGItl3Wh3hFY3oryo4cPvCeXU0PXNUVKCsD51fvpncLtrd1zkMdA67qvZ8MawsCuT&X-Amz-Signature=027711b4ee94de7f84105ae7e992d2d667b37dbe944c65573963e68cd17edc0f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XY247YY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCID%2Fo1bJ7lDhuL4XtxFbuYzXHuXZwthVIPi7kg5Inq5wTAiEAh7ZO%2Fwdx0I2qn%2B0crenAUhNuNmvTVJZR3B8D0alodDUq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDIu8w0ZWrvdb8fCntyrcAzL04cPSgGZfJCOHG4eA9a4PtZtphR%2BMqyfGF2EKVYTuSdb2e41hShN37itWIV%2BusyIZKakG%2BXEyVaXXFe%2F3azuN%2BalsATTXEBzI1DmMW%2B3p7E2Bu1F80ovk6vn2hj3l7Lkz2McP9N3JACyn2wamfO%2BeyOT4NCl6owsb%2BPHAIF9fXhlVL1I0XltII%2FrL6rzY1CT8bq7dsODo1fuvpSfRFaywk5qdceRqUHD2iWdi7P%2FSkFBjoEXIIeXOVrW7kL2HL0aApFFNq0%2FzsCnrytYMOjBKawyO0FAKSzZOWREDYlm%2BWFe6dB32Dq2fGrLYkJ2GxQiZwbE93%2B4uXgdcN8Yz0e%2Bfizje7X0flmj1b1NpPNOHG7sFP9nGCYNQSqfH1fmp9%2BPRXE03QyH93Ks2geqyAHeSIJrso13FuvH1ZkkqfJtH21oWOSE9KWRJero7fJ8Gty72coR6BvNmXI2ZKxgcyq8uLJ4ek1wAFqmxzon7eZB3snYk7CQACWCKYsFG4N1EO%2BsnkuHaAdTiEMaY4wuG70IwGWdzim8MCQQuR1dbEMOPtSiGPrqF79K6UUNfrIVFn7UpksEsydTscqCFsjQYpcOy56EUTTYsK%2BHyR6IFZfq3AF%2FBXxUpPOmM8mnhMIbEkr0GOqUBOSA6NmQZOPAyvSw96lezmJFm8F5KKMeeduqYkrY86atA53H9P2kcQ3%2F3wBFSYwsdCwf%2FpiLxRQSTrLfs3XIHP%2BR48MME9qNNzn8PBAJlq7drXrbd4KQ3UQnjcQrCjx1ONMLjWLsDS%2BvxdtXcbKFTqHHEF4OMJWG1C8T8IiRRVPtSnng4UClLPVgglm80sEYLbHpkXgK9h2HAmk3fXez9Iq2xGWyU&X-Amz-Signature=d81783fab598e8fcff235220503446d7503f3b0d180770f740109204d7964302&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYX4JJS7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQC3EmoOsEzq0Xzy89leXdKBanJPNQ8EOxpe%2FXgeuVLY8wIgSMXv8vtlTAt1eKU9%2BpCwq3WMvBntEp9LivUQ4NjV61Uq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDB0aLHMfSWuZWvpqVSrcA0t68Uxt00HCFNpd9O5Cuk7cl2Zk8eG0rmj9CTDVGeqrELAIEk97jdTOI4AhQ2Ifzo0ZK9JSZsupEMwu%2BSVxmZeIq9%2BPZqeDct28TpLn6TN0N5%2F54Xffpa%2B1n4t1IeplMLXXVN%2Bv0XeO0bDrOpLruzTJSwlfNlT1t3f7LdE6NmiqhW%2BEnxQZXyfPw82wwAlN4CO2ifDrsQ8J%2BU1nAV%2FsQTxoTS%2FcrcXz1h0kMexlmEpZbzNJlh0Hs9B08kWI2ZyHlSF%2FQBK3u8AHuDsE8WbwxbJKzw1EWHzw3lqmditf9RVZhjBXDIx0tPjznR%2B%2FhiRbhn4DgQUOfXGSbSnWYZ%2Bqfl36MXQuzHrCHv%2BWf8HgWEhgVDTHgqRQK73UVY4tpWcCXq9U9GwPKZpPl7ODkjrP41uVEmHB4TifrHJL1UaRIP%2BiLE%2FJ1X6eohZLTqZZVdKjJWEiBjj2mY2%2B1YPu0WsdGMXJ335QPrAUS7RYosfiqqXVYW%2BAmzaOPJajUfFiXhY7pkUgMLrcUwx%2BH4wGUAL7d5XQEjeEFWinY%2B1APLZ9M6cphTMqR6tvancg6mYGWgydm6%2BDB1kxani3XUHMagAeMduWj%2FoDnzCu%2FTmoU62kK0d%2BhGFNLfxxjf9bl7XEMI3Ekr0GOqUB%2FgXONTtjCl76ITJ7TSsCln2w3qWTaLd0YZcDKzvlPfzTKxMqnrkZcS5sptXVaSKnD3ZNtvcOZt5b1oJlAOFZV552pugORYX5yWMNZjuZxAdQR8l%2FvCbk%2BDyoDQmXuGsvVTAiJMG5R9G1KALq2890XBeSlkUOjWk55qIAxbAyvLLiSgh0oyIUT%2BYMXq9Pv8y9g%2B1ORb8IuDoALR8gQ5HM8YF8fEli&X-Amz-Signature=d217874bdebb5b14fd29ee4dd51187b33c28b12b515b66d9433d896c033b75fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7QFWI3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQCXnEocCiu1zXhCUXi5%2BtzWqDBJrC6hb3rYBbF%2Fmj4IeAIhANKlHkW2O4yLFNnvE3ra19u6mUk0aJVV3rd8rOE3dba5Kv8DCF0QABoMNjM3NDIzMTgzODA1IgxYjEIiFfJtCAn4I0cq3AMBAmXBNylHb7L0dC6xV0ljKOmrK34HXwL%2BEN2ZJXrom15df3m6YOYZfiO19VeCsTPHCkDLhcxRYSEBDOIrMz4j0Zw%2FeCOOmXuXZ%2BHjHMuufh5PTU6EFw7QPsnrhYelX%2FfRcK4tNVikodM3i5CvYr0VazBbDlI4karAF449%2FDD%2B5OULlyeKizwb5XnzWMR870OJTN26uN2EXbe%2FufcIl7eUYhRN7hzGokTiOjn0ldYyQ6D%2FsDaJcCigbOHe9wsw0W6ordpo0Ed3YJpFBg1Z17hCMg9R2bhrYBgWy2JQDu9GkAYn7nd%2Fdi0eAjL5yvj30EYOlKhhSXBx865Mga5mqHJtPP471yg9xSwEpamfMSMEdtKs2No4Trew2pri2yhh36YYdWhHrxVlEPuJ99KQYxf0T0BREFjdfjDhzqPF5tgNF0CLb%2Bxda%2B%2BX9TGc%2Fa9FwPlDeMHA%2Bfx5G8Mc16o%2FRp5RtQ0Ptv6ts%2B2EnXiPnP1ukcB5DoHTKNZIUyD7EtkuGABUtdy5msqTuISa9Klj2FSS5cmt9BoReD7IkOPg5yBUI3b79nyWjRMcBohilT6ddJVDYNQrQxDMMs9G%2F0mBFXjpPKWnGCfL0sJ5RrgpKfqR%2FAlsCdS2P7jgNQQHYDCMxJK9BjqkAYg0V1FejsnqJ0GwWf0%2FWvW37r8VX60mz4W8TeMFFn83z6M2xmzl0gkYd9EhYQdsYYgLYToKCzpnKC38%2FmbO5sKv3E5yCr6O73DGzAPdtu7ZDjpXHQbzbkD5%2BJzf0%2Fe2pAVf7XvIHe66LDYYopmGh6om09rqJuYMWQUWLpCO6DS82iZOUvjXIIPAJqygFwjHKWDstQyex0EqcFPMXZQVNfZAKgi0&X-Amz-Signature=31c9e5b3c40e227c6ecbf35440c931d4857dca3a5be202af556e187b59425e36&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7QFWI3K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQCXnEocCiu1zXhCUXi5%2BtzWqDBJrC6hb3rYBbF%2Fmj4IeAIhANKlHkW2O4yLFNnvE3ra19u6mUk0aJVV3rd8rOE3dba5Kv8DCF0QABoMNjM3NDIzMTgzODA1IgxYjEIiFfJtCAn4I0cq3AMBAmXBNylHb7L0dC6xV0ljKOmrK34HXwL%2BEN2ZJXrom15df3m6YOYZfiO19VeCsTPHCkDLhcxRYSEBDOIrMz4j0Zw%2FeCOOmXuXZ%2BHjHMuufh5PTU6EFw7QPsnrhYelX%2FfRcK4tNVikodM3i5CvYr0VazBbDlI4karAF449%2FDD%2B5OULlyeKizwb5XnzWMR870OJTN26uN2EXbe%2FufcIl7eUYhRN7hzGokTiOjn0ldYyQ6D%2FsDaJcCigbOHe9wsw0W6ordpo0Ed3YJpFBg1Z17hCMg9R2bhrYBgWy2JQDu9GkAYn7nd%2Fdi0eAjL5yvj30EYOlKhhSXBx865Mga5mqHJtPP471yg9xSwEpamfMSMEdtKs2No4Trew2pri2yhh36YYdWhHrxVlEPuJ99KQYxf0T0BREFjdfjDhzqPF5tgNF0CLb%2Bxda%2B%2BX9TGc%2Fa9FwPlDeMHA%2Bfx5G8Mc16o%2FRp5RtQ0Ptv6ts%2B2EnXiPnP1ukcB5DoHTKNZIUyD7EtkuGABUtdy5msqTuISa9Klj2FSS5cmt9BoReD7IkOPg5yBUI3b79nyWjRMcBohilT6ddJVDYNQrQxDMMs9G%2F0mBFXjpPKWnGCfL0sJ5RrgpKfqR%2FAlsCdS2P7jgNQQHYDCMxJK9BjqkAYg0V1FejsnqJ0GwWf0%2FWvW37r8VX60mz4W8TeMFFn83z6M2xmzl0gkYd9EhYQdsYYgLYToKCzpnKC38%2FmbO5sKv3E5yCr6O73DGzAPdtu7ZDjpXHQbzbkD5%2BJzf0%2Fe2pAVf7XvIHe66LDYYopmGh6om09rqJuYMWQUWLpCO6DS82iZOUvjXIIPAJqygFwjHKWDstQyex0EqcFPMXZQVNfZAKgi0&X-Amz-Signature=8485ab4f94ef5c930cd6d8b1af62395ad64500649ce7ada8b8f33d89f0cbff82&X-Amz-SignedHeaders=host&x-id=GetObject)

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
