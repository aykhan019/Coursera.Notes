

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7LRD7D5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDA0tkLD9ZvBvrRsjMQ0PSConuUW0o9I3zc54H%2B3Ifw%2FAIgGcUx%2BfvVjW7qqnJpL43E%2Fv9yVV1agZc%2FUKbxzY8IifQqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE7bDM2TEF1LHZGzPircAwPQ4AwwNVCGgF%2BWpsyUUOraGYvFuDVg4HB%2BBeK1b5lJvYrE5NIl65lYl1ZTAUMDxySaLrZXLN9Afw%2BiPxmXQIGDO8Ezx1zEkKw4sapr80SsuUQ63rQHJXRF6RcSSHc4xiTLmcAs2wa%2FDJRZidO4rMAj8tk7iw7ZzK3vj5CU0k9P9Tq9hjtSY2TOoD7Xid3nlhyRNHIG1IxNf4R4bCmtK%2Br2%2FT8kPTLf3ySKJ%2FQg62MgC5gOkC7siyErqxIWJ4B%2FSzvvJxjsH0C89%2BS6%2FSnU42phMsZ2tquUQKUkeYXF4zT8%2F3LPYjILDXU4N%2Fke0iRn0WtNkDhnlkCOED6e1EamY9eLP%2FjSTfXMwD2tYf6JEabIabOZUkzk7vHRIhOooF%2BqkVXz0XgqUhp6ZMBpuDm71lzJhv74p%2F5DC9piogteDjX3X8qvl2a9fhBFDXB0H6Cc4VbGIW7XVJtOj%2Bh8Zz83HcQZBWgEytAF4%2FdoyypCc4fCIJWwO%2B932FVyHVMlKI9OZc1ty4xmNQxIG1DT9iA09TMjRvlip9PNuDg1n1%2Blw%2BQ0UMpIjpDvzdOR5VSmKNcxD3m1eUVEcFEwP0ZZv6q3dhfvwGJ9m7LIdeOxhgGQEgdDJFHwC6RSEzgbN22gMM7L6LwGOqUBrahQ6RdbL1yHgCwcWF9HAgKVXtYGQPm2jUEpHtzGgXYW61ZPpl08i53h5OYKBImcNTrFsBFcFU4LFlDoPZvN55jdiBu4IGIFccQXMa8yrODDS7GD2uzEFetfEXhnds6TDk3yl66VeaqTJm%2B%2BCYrbdzTmVDx3l0XoGWq18Vskdket07Gj1MSBk0AuFlWhNKsUyCXrQWXnA4z7Kdjq3DaSRSv7TdzA&X-Amz-Signature=b71372a26a4eefb81c086106dcdc40ccfafa7cc024facdc309c31e24a6a81b99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7LRD7D5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDA0tkLD9ZvBvrRsjMQ0PSConuUW0o9I3zc54H%2B3Ifw%2FAIgGcUx%2BfvVjW7qqnJpL43E%2Fv9yVV1agZc%2FUKbxzY8IifQqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE7bDM2TEF1LHZGzPircAwPQ4AwwNVCGgF%2BWpsyUUOraGYvFuDVg4HB%2BBeK1b5lJvYrE5NIl65lYl1ZTAUMDxySaLrZXLN9Afw%2BiPxmXQIGDO8Ezx1zEkKw4sapr80SsuUQ63rQHJXRF6RcSSHc4xiTLmcAs2wa%2FDJRZidO4rMAj8tk7iw7ZzK3vj5CU0k9P9Tq9hjtSY2TOoD7Xid3nlhyRNHIG1IxNf4R4bCmtK%2Br2%2FT8kPTLf3ySKJ%2FQg62MgC5gOkC7siyErqxIWJ4B%2FSzvvJxjsH0C89%2BS6%2FSnU42phMsZ2tquUQKUkeYXF4zT8%2F3LPYjILDXU4N%2Fke0iRn0WtNkDhnlkCOED6e1EamY9eLP%2FjSTfXMwD2tYf6JEabIabOZUkzk7vHRIhOooF%2BqkVXz0XgqUhp6ZMBpuDm71lzJhv74p%2F5DC9piogteDjX3X8qvl2a9fhBFDXB0H6Cc4VbGIW7XVJtOj%2Bh8Zz83HcQZBWgEytAF4%2FdoyypCc4fCIJWwO%2B932FVyHVMlKI9OZc1ty4xmNQxIG1DT9iA09TMjRvlip9PNuDg1n1%2Blw%2BQ0UMpIjpDvzdOR5VSmKNcxD3m1eUVEcFEwP0ZZv6q3dhfvwGJ9m7LIdeOxhgGQEgdDJFHwC6RSEzgbN22gMM7L6LwGOqUBrahQ6RdbL1yHgCwcWF9HAgKVXtYGQPm2jUEpHtzGgXYW61ZPpl08i53h5OYKBImcNTrFsBFcFU4LFlDoPZvN55jdiBu4IGIFccQXMa8yrODDS7GD2uzEFetfEXhnds6TDk3yl66VeaqTJm%2B%2BCYrbdzTmVDx3l0XoGWq18Vskdket07Gj1MSBk0AuFlWhNKsUyCXrQWXnA4z7Kdjq3DaSRSv7TdzA&X-Amz-Signature=1e3a4e0e4ac12e526e13441a6ff45225a094f72e0fe6514605d222a2d1d43536&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7LRD7D5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDA0tkLD9ZvBvrRsjMQ0PSConuUW0o9I3zc54H%2B3Ifw%2FAIgGcUx%2BfvVjW7qqnJpL43E%2Fv9yVV1agZc%2FUKbxzY8IifQqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE7bDM2TEF1LHZGzPircAwPQ4AwwNVCGgF%2BWpsyUUOraGYvFuDVg4HB%2BBeK1b5lJvYrE5NIl65lYl1ZTAUMDxySaLrZXLN9Afw%2BiPxmXQIGDO8Ezx1zEkKw4sapr80SsuUQ63rQHJXRF6RcSSHc4xiTLmcAs2wa%2FDJRZidO4rMAj8tk7iw7ZzK3vj5CU0k9P9Tq9hjtSY2TOoD7Xid3nlhyRNHIG1IxNf4R4bCmtK%2Br2%2FT8kPTLf3ySKJ%2FQg62MgC5gOkC7siyErqxIWJ4B%2FSzvvJxjsH0C89%2BS6%2FSnU42phMsZ2tquUQKUkeYXF4zT8%2F3LPYjILDXU4N%2Fke0iRn0WtNkDhnlkCOED6e1EamY9eLP%2FjSTfXMwD2tYf6JEabIabOZUkzk7vHRIhOooF%2BqkVXz0XgqUhp6ZMBpuDm71lzJhv74p%2F5DC9piogteDjX3X8qvl2a9fhBFDXB0H6Cc4VbGIW7XVJtOj%2Bh8Zz83HcQZBWgEytAF4%2FdoyypCc4fCIJWwO%2B932FVyHVMlKI9OZc1ty4xmNQxIG1DT9iA09TMjRvlip9PNuDg1n1%2Blw%2BQ0UMpIjpDvzdOR5VSmKNcxD3m1eUVEcFEwP0ZZv6q3dhfvwGJ9m7LIdeOxhgGQEgdDJFHwC6RSEzgbN22gMM7L6LwGOqUBrahQ6RdbL1yHgCwcWF9HAgKVXtYGQPm2jUEpHtzGgXYW61ZPpl08i53h5OYKBImcNTrFsBFcFU4LFlDoPZvN55jdiBu4IGIFccQXMa8yrODDS7GD2uzEFetfEXhnds6TDk3yl66VeaqTJm%2B%2BCYrbdzTmVDx3l0XoGWq18Vskdket07Gj1MSBk0AuFlWhNKsUyCXrQWXnA4z7Kdjq3DaSRSv7TdzA&X-Amz-Signature=fcc7e2663e6266ca30a6e98afe1469b62d337359ef21845bf5b1b9022dccd21d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWEABAH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFHlMAJYQg%2BAklxgo84UJpyq0xhwPzf6%2B07gRwvILnsAIgTbGG4U9ypo3FQuEWNNx8Tc7vv19kAflrCI1n%2FUV7EakqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5dYHqXOzuevlKkeCrcA07h3WXFq4BpGKjZPiO%2FLfG8KhlEk05mC5LGdhkxwtWEjU0APAEANf3G7REHP4m10koF5USHA7jsuuwmqv7BMb6eMkfeJ3FoHfx359bT8PbnnUqwspxw5mi8MUGC6ETckjDrXj0o97g9HyEcSzP7xVFil9mVLwBPsrNsQYip6w78mt02%2BwTtVfVxE%2FeH4iet618N%2F6TLIQ9sFrw5DG1e3nj%2F1UQyulBcdoRslpTTOhsl2Ta7noP2yBCsRsq7N8x4xqrfD2it6QlRsElkp1F59UYcJFIVwImAJ8EUuGjFdGNvioA9V0QwO6cy7y1iFBTApIVjdFyNBy9ATO84GHip898lQeuxvIhiUOp0bgsuuEyBYrvDwRoI824GNmbjNIDnvBJjYifJw%2BlVaLyV%2BEVfElWr7kb4bGX3ti0bjFBbhlgnECYtV9%2F%2Fz9bVIyzJFlnc1kzUjbKe6e0RsHesX5Cn6vdG0AOD2ILxChWnnhu3YtYByvwOcYKMXxwemmFQr7dPsG%2FhqFSnGDlbdvG0dKhBMSVaE7iW9tlNxcWaW4ZfIC1bQMd3xdoQ1ODVhmspw%2FogQI7YGJPYfKwLpolvODj3lecz5l6zNlznOWBHft9TAY0Y34zmnjC7KY8YDLPHMJHL6LwGOqUBNuvc9YEVb3FgtvcMqu43wPQw3HPjwAIazbDhXF3ACOETBPi%2BWS7PGvMLzML2em8%2BCIsZlwoN66LNe4izZpMcdWxBkntIqQUjLkN0YxEP9kBRRpjYgK4gNdqsuMUMYOJVYNTAXCiH7DTNBh6UNXF53q7Qg3K1zrd4vHQsQ2ZCcKERp7oe%2BnKykJC6VDigqYqvpqwD6U3UO%2FcQ4z1%2B7a9cvKEhfAXc&X-Amz-Signature=899b004e3965a409d4894356b5173a1b7520aeee7bc6012c1832fbe721396795&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWEABAH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFHlMAJYQg%2BAklxgo84UJpyq0xhwPzf6%2B07gRwvILnsAIgTbGG4U9ypo3FQuEWNNx8Tc7vv19kAflrCI1n%2FUV7EakqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5dYHqXOzuevlKkeCrcA07h3WXFq4BpGKjZPiO%2FLfG8KhlEk05mC5LGdhkxwtWEjU0APAEANf3G7REHP4m10koF5USHA7jsuuwmqv7BMb6eMkfeJ3FoHfx359bT8PbnnUqwspxw5mi8MUGC6ETckjDrXj0o97g9HyEcSzP7xVFil9mVLwBPsrNsQYip6w78mt02%2BwTtVfVxE%2FeH4iet618N%2F6TLIQ9sFrw5DG1e3nj%2F1UQyulBcdoRslpTTOhsl2Ta7noP2yBCsRsq7N8x4xqrfD2it6QlRsElkp1F59UYcJFIVwImAJ8EUuGjFdGNvioA9V0QwO6cy7y1iFBTApIVjdFyNBy9ATO84GHip898lQeuxvIhiUOp0bgsuuEyBYrvDwRoI824GNmbjNIDnvBJjYifJw%2BlVaLyV%2BEVfElWr7kb4bGX3ti0bjFBbhlgnECYtV9%2F%2Fz9bVIyzJFlnc1kzUjbKe6e0RsHesX5Cn6vdG0AOD2ILxChWnnhu3YtYByvwOcYKMXxwemmFQr7dPsG%2FhqFSnGDlbdvG0dKhBMSVaE7iW9tlNxcWaW4ZfIC1bQMd3xdoQ1ODVhmspw%2FogQI7YGJPYfKwLpolvODj3lecz5l6zNlznOWBHft9TAY0Y34zmnjC7KY8YDLPHMJHL6LwGOqUBNuvc9YEVb3FgtvcMqu43wPQw3HPjwAIazbDhXF3ACOETBPi%2BWS7PGvMLzML2em8%2BCIsZlwoN66LNe4izZpMcdWxBkntIqQUjLkN0YxEP9kBRRpjYgK4gNdqsuMUMYOJVYNTAXCiH7DTNBh6UNXF53q7Qg3K1zrd4vHQsQ2ZCcKERp7oe%2BnKykJC6VDigqYqvpqwD6U3UO%2FcQ4z1%2B7a9cvKEhfAXc&X-Amz-Signature=05122a6a6d178e882becd391038f28378c2d7dbddc05522614f3556e37dfa0bf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWEABAH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFHlMAJYQg%2BAklxgo84UJpyq0xhwPzf6%2B07gRwvILnsAIgTbGG4U9ypo3FQuEWNNx8Tc7vv19kAflrCI1n%2FUV7EakqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5dYHqXOzuevlKkeCrcA07h3WXFq4BpGKjZPiO%2FLfG8KhlEk05mC5LGdhkxwtWEjU0APAEANf3G7REHP4m10koF5USHA7jsuuwmqv7BMb6eMkfeJ3FoHfx359bT8PbnnUqwspxw5mi8MUGC6ETckjDrXj0o97g9HyEcSzP7xVFil9mVLwBPsrNsQYip6w78mt02%2BwTtVfVxE%2FeH4iet618N%2F6TLIQ9sFrw5DG1e3nj%2F1UQyulBcdoRslpTTOhsl2Ta7noP2yBCsRsq7N8x4xqrfD2it6QlRsElkp1F59UYcJFIVwImAJ8EUuGjFdGNvioA9V0QwO6cy7y1iFBTApIVjdFyNBy9ATO84GHip898lQeuxvIhiUOp0bgsuuEyBYrvDwRoI824GNmbjNIDnvBJjYifJw%2BlVaLyV%2BEVfElWr7kb4bGX3ti0bjFBbhlgnECYtV9%2F%2Fz9bVIyzJFlnc1kzUjbKe6e0RsHesX5Cn6vdG0AOD2ILxChWnnhu3YtYByvwOcYKMXxwemmFQr7dPsG%2FhqFSnGDlbdvG0dKhBMSVaE7iW9tlNxcWaW4ZfIC1bQMd3xdoQ1ODVhmspw%2FogQI7YGJPYfKwLpolvODj3lecz5l6zNlznOWBHft9TAY0Y34zmnjC7KY8YDLPHMJHL6LwGOqUBNuvc9YEVb3FgtvcMqu43wPQw3HPjwAIazbDhXF3ACOETBPi%2BWS7PGvMLzML2em8%2BCIsZlwoN66LNe4izZpMcdWxBkntIqQUjLkN0YxEP9kBRRpjYgK4gNdqsuMUMYOJVYNTAXCiH7DTNBh6UNXF53q7Qg3K1zrd4vHQsQ2ZCcKERp7oe%2BnKykJC6VDigqYqvpqwD6U3UO%2FcQ4z1%2B7a9cvKEhfAXc&X-Amz-Signature=725d97935bda2c18a024b890f2883eb1ed0b3d453b9d924d13d01b6f803f4ea9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWEABAH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFHlMAJYQg%2BAklxgo84UJpyq0xhwPzf6%2B07gRwvILnsAIgTbGG4U9ypo3FQuEWNNx8Tc7vv19kAflrCI1n%2FUV7EakqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5dYHqXOzuevlKkeCrcA07h3WXFq4BpGKjZPiO%2FLfG8KhlEk05mC5LGdhkxwtWEjU0APAEANf3G7REHP4m10koF5USHA7jsuuwmqv7BMb6eMkfeJ3FoHfx359bT8PbnnUqwspxw5mi8MUGC6ETckjDrXj0o97g9HyEcSzP7xVFil9mVLwBPsrNsQYip6w78mt02%2BwTtVfVxE%2FeH4iet618N%2F6TLIQ9sFrw5DG1e3nj%2F1UQyulBcdoRslpTTOhsl2Ta7noP2yBCsRsq7N8x4xqrfD2it6QlRsElkp1F59UYcJFIVwImAJ8EUuGjFdGNvioA9V0QwO6cy7y1iFBTApIVjdFyNBy9ATO84GHip898lQeuxvIhiUOp0bgsuuEyBYrvDwRoI824GNmbjNIDnvBJjYifJw%2BlVaLyV%2BEVfElWr7kb4bGX3ti0bjFBbhlgnECYtV9%2F%2Fz9bVIyzJFlnc1kzUjbKe6e0RsHesX5Cn6vdG0AOD2ILxChWnnhu3YtYByvwOcYKMXxwemmFQr7dPsG%2FhqFSnGDlbdvG0dKhBMSVaE7iW9tlNxcWaW4ZfIC1bQMd3xdoQ1ODVhmspw%2FogQI7YGJPYfKwLpolvODj3lecz5l6zNlznOWBHft9TAY0Y34zmnjC7KY8YDLPHMJHL6LwGOqUBNuvc9YEVb3FgtvcMqu43wPQw3HPjwAIazbDhXF3ACOETBPi%2BWS7PGvMLzML2em8%2BCIsZlwoN66LNe4izZpMcdWxBkntIqQUjLkN0YxEP9kBRRpjYgK4gNdqsuMUMYOJVYNTAXCiH7DTNBh6UNXF53q7Qg3K1zrd4vHQsQ2ZCcKERp7oe%2BnKykJC6VDigqYqvpqwD6U3UO%2FcQ4z1%2B7a9cvKEhfAXc&X-Amz-Signature=5479fa875e80485fcd82a8239c0434be36c2f86230ce179fafd1aaba3e522704&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWEABAH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFHlMAJYQg%2BAklxgo84UJpyq0xhwPzf6%2B07gRwvILnsAIgTbGG4U9ypo3FQuEWNNx8Tc7vv19kAflrCI1n%2FUV7EakqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5dYHqXOzuevlKkeCrcA07h3WXFq4BpGKjZPiO%2FLfG8KhlEk05mC5LGdhkxwtWEjU0APAEANf3G7REHP4m10koF5USHA7jsuuwmqv7BMb6eMkfeJ3FoHfx359bT8PbnnUqwspxw5mi8MUGC6ETckjDrXj0o97g9HyEcSzP7xVFil9mVLwBPsrNsQYip6w78mt02%2BwTtVfVxE%2FeH4iet618N%2F6TLIQ9sFrw5DG1e3nj%2F1UQyulBcdoRslpTTOhsl2Ta7noP2yBCsRsq7N8x4xqrfD2it6QlRsElkp1F59UYcJFIVwImAJ8EUuGjFdGNvioA9V0QwO6cy7y1iFBTApIVjdFyNBy9ATO84GHip898lQeuxvIhiUOp0bgsuuEyBYrvDwRoI824GNmbjNIDnvBJjYifJw%2BlVaLyV%2BEVfElWr7kb4bGX3ti0bjFBbhlgnECYtV9%2F%2Fz9bVIyzJFlnc1kzUjbKe6e0RsHesX5Cn6vdG0AOD2ILxChWnnhu3YtYByvwOcYKMXxwemmFQr7dPsG%2FhqFSnGDlbdvG0dKhBMSVaE7iW9tlNxcWaW4ZfIC1bQMd3xdoQ1ODVhmspw%2FogQI7YGJPYfKwLpolvODj3lecz5l6zNlznOWBHft9TAY0Y34zmnjC7KY8YDLPHMJHL6LwGOqUBNuvc9YEVb3FgtvcMqu43wPQw3HPjwAIazbDhXF3ACOETBPi%2BWS7PGvMLzML2em8%2BCIsZlwoN66LNe4izZpMcdWxBkntIqQUjLkN0YxEP9kBRRpjYgK4gNdqsuMUMYOJVYNTAXCiH7DTNBh6UNXF53q7Qg3K1zrd4vHQsQ2ZCcKERp7oe%2BnKykJC6VDigqYqvpqwD6U3UO%2FcQ4z1%2B7a9cvKEhfAXc&X-Amz-Signature=81d3af95375983c57c8bdc6d0ca23e0a5131e687573d83dfeefb36137920e1ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWEABAH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFHlMAJYQg%2BAklxgo84UJpyq0xhwPzf6%2B07gRwvILnsAIgTbGG4U9ypo3FQuEWNNx8Tc7vv19kAflrCI1n%2FUV7EakqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5dYHqXOzuevlKkeCrcA07h3WXFq4BpGKjZPiO%2FLfG8KhlEk05mC5LGdhkxwtWEjU0APAEANf3G7REHP4m10koF5USHA7jsuuwmqv7BMb6eMkfeJ3FoHfx359bT8PbnnUqwspxw5mi8MUGC6ETckjDrXj0o97g9HyEcSzP7xVFil9mVLwBPsrNsQYip6w78mt02%2BwTtVfVxE%2FeH4iet618N%2F6TLIQ9sFrw5DG1e3nj%2F1UQyulBcdoRslpTTOhsl2Ta7noP2yBCsRsq7N8x4xqrfD2it6QlRsElkp1F59UYcJFIVwImAJ8EUuGjFdGNvioA9V0QwO6cy7y1iFBTApIVjdFyNBy9ATO84GHip898lQeuxvIhiUOp0bgsuuEyBYrvDwRoI824GNmbjNIDnvBJjYifJw%2BlVaLyV%2BEVfElWr7kb4bGX3ti0bjFBbhlgnECYtV9%2F%2Fz9bVIyzJFlnc1kzUjbKe6e0RsHesX5Cn6vdG0AOD2ILxChWnnhu3YtYByvwOcYKMXxwemmFQr7dPsG%2FhqFSnGDlbdvG0dKhBMSVaE7iW9tlNxcWaW4ZfIC1bQMd3xdoQ1ODVhmspw%2FogQI7YGJPYfKwLpolvODj3lecz5l6zNlznOWBHft9TAY0Y34zmnjC7KY8YDLPHMJHL6LwGOqUBNuvc9YEVb3FgtvcMqu43wPQw3HPjwAIazbDhXF3ACOETBPi%2BWS7PGvMLzML2em8%2BCIsZlwoN66LNe4izZpMcdWxBkntIqQUjLkN0YxEP9kBRRpjYgK4gNdqsuMUMYOJVYNTAXCiH7DTNBh6UNXF53q7Qg3K1zrd4vHQsQ2ZCcKERp7oe%2BnKykJC6VDigqYqvpqwD6U3UO%2FcQ4z1%2B7a9cvKEhfAXc&X-Amz-Signature=a31e56ffef031bcf4c4c0af702414e1db9c0bb796a39f6b58a3575bcff4dcabf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHCEGJCC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICLjP%2F5V8P3VbnfCZt1BCyZMbcNxy%2F%2FpRDHpy8BPMeBYAiBb4mFtntR%2FIcauk3e6KSYREywkvSf9%2BOiG6rTmiA9eRCqIBAiO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWVnTxpOBWVNbirciKtwD7iybeWg1zOufTtIqgrRC6m7TiZi%2FPYtDB7VjUPbEKPhkBSUgBjjUotDY%2F2JbuTJmVZDmTlY4TOvg2JDTCS6O355XKwHR1LxP8e9kYBrdOLSBLwLBAgz4lYkvgDNQL1HEjMu2oyOPByfpOOPf35OlUDMSpgU36p11Y7e%2BlgVZUKby1x%2B87my%2BwQENVYC2NrBz943xB2PJuS0VI%2FRHM1Syj%2FL0xKDbeHKRUY5YrqAf1u3P7hwyBim7Mxn514y%2FkPeeoO8ULZdtnz0D6immixLGrXs0Pnyx3nKa870ff%2BIr%2FR82IFCCQvI8roXTD8FMiy2vpnZZzBUgj3myXpZEiKJIsZD6uy1go8LzWk4WJAPo1L4smkg%2FRGSFIOGu2arr3vN%2FxFCWpkMjGfbkOaaZx%2B7kyAhNFucugubeQ20o95rcS0h4cGi7jH4FVA1E%2FlngCFUxabjbT3ECyPMugE%2F6kADqIoyUCWbWZqYMHUmt7%2BH1VJpCCh7usPSqkGwSu5fbJG3ovYOin3Off4umgtUMY5s0UkgloMWBSVkMa2feAi2K%2F8314Pvt3ESMm%2Fx8ISRCs5v3x46OnjAH8p37Kp4RYRIYssGnh9VfSGwMDIXKM1qqoXg7Cck1JeTjDSwIbnAw38vovAY6pgFCsPCgCbVpQpxBCP8EzRUCK1R2BwgJqGJWqIc2UIrSRNgKr2pIjt5GdlX06TqLguFdgNwA8yyxL2SWqvdCIg4Znx%2BbpdZ0LpUmBFRevt0MtQAsdzZ3g1%2FHk6r5Ic4%2BE4rguaZUCsdDH8Jh6wpswk230cikLP60QNeJEZB%2B2wl7SJ60gM0b8F75auMrFlj%2Fkt3Zx6qgeaXdUSMpm7mz8A909Z6PjDRi&X-Amz-Signature=010c57cc7dfa01552047dede27f9d6ef54ea76562a0fdb0575bc4e5582ae6b1c&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULYOYZEV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRJckdUUmzrXKzRfb2u1TYx9%2BfqAj%2BmFViYnksV7mJdAiBLnEcuqw8%2BzhQssQFPtzAX1tzXwbcxVmuG2S5RpnklWCqIBAiO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyJ28evwqqAQf3CufKtwDABfjOa3M0Vmfj5EL0aU3fvwb1H9LAcW022s2rVUyecRBvXzTK4EUwjO%2FUiP1ZGorGnV2MTAx9Q5xQZppmFxmbJrvdHaUotzArZauEg%2Bt5EcfUz7Zo2QKYIqowoU9ZRdlj5YiNi6J6BeqcqR81d2UNK%2F03Esqg%2B8WqwF%2BkiB5d5B5wYVncNlTr9IXn935Qv81u2JnmVVI%2BtH5bpn4Yn2f4g1w6ZAxhu7z949uEywEmDw4cUZ14dmOgGk3afV%2B%2FQaGRArVhZBDx%2FMvu2ZZkVF7zHwC3Oh7JsjxDnGz%2BCebgFPTDRUR6onOxrxjAO9RBqxQT1tyrDFCeMg1otpU1OIVi%2BnKN9p%2FIWAwUTUrjPvquhT6g5lsTYtOJipx08H%2FDZcGCEXqVf8TlL59nTRjp3KivpTtN3%2FaVNyEjY1BoUyjAeqLwxsBjDjh%2BCkmCiNjLm3z25Qu4Vb5ZcryHAToO%2Ffqii%2BnkwE4SGAp53x5BDJd6gLYYaOpOp9EUNt8ndr%2Bx1fblYbTpfC64BdlsEyq%2BKBTxDG2FZ5RDXGv1R%2F6oJgVxyQIN15WuEv4ogtAer1%2FXrpXIysPCfsXJGLXWMxZeXM6QpznQMhY7zSugvxVZR979BQCaWNHCSgh6%2BMin%2FAwlsvovAY6pgF7HRTA%2BWZzddXtqpE8ZsRIlQXrQ9FT73Mr51bbyQ9dFcPcbCJhhZP37ibI%2BMhQLBcJHe5KHRufPdh20aJ8pwKYR45n6wzTjValGT%2FUEsDaKz92AXbCdnBt7kFuCG9Uiz%2FSQZj6tnhJZLZdMjLcZEQBkKcWHEQjU2x0qyQm5CRCPu9NxY%2FCoXhhKWH3uNF8axWmLqu9Lu%2FZ%2Bf6vy5RnpX2Ms0NuG2GA&X-Amz-Signature=66edf1d8d5dea3b41dce65146a9678d7796ec4b4c66801f1cfae8f84ab2a0de7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWEABAH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFHlMAJYQg%2BAklxgo84UJpyq0xhwPzf6%2B07gRwvILnsAIgTbGG4U9ypo3FQuEWNNx8Tc7vv19kAflrCI1n%2FUV7EakqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5dYHqXOzuevlKkeCrcA07h3WXFq4BpGKjZPiO%2FLfG8KhlEk05mC5LGdhkxwtWEjU0APAEANf3G7REHP4m10koF5USHA7jsuuwmqv7BMb6eMkfeJ3FoHfx359bT8PbnnUqwspxw5mi8MUGC6ETckjDrXj0o97g9HyEcSzP7xVFil9mVLwBPsrNsQYip6w78mt02%2BwTtVfVxE%2FeH4iet618N%2F6TLIQ9sFrw5DG1e3nj%2F1UQyulBcdoRslpTTOhsl2Ta7noP2yBCsRsq7N8x4xqrfD2it6QlRsElkp1F59UYcJFIVwImAJ8EUuGjFdGNvioA9V0QwO6cy7y1iFBTApIVjdFyNBy9ATO84GHip898lQeuxvIhiUOp0bgsuuEyBYrvDwRoI824GNmbjNIDnvBJjYifJw%2BlVaLyV%2BEVfElWr7kb4bGX3ti0bjFBbhlgnECYtV9%2F%2Fz9bVIyzJFlnc1kzUjbKe6e0RsHesX5Cn6vdG0AOD2ILxChWnnhu3YtYByvwOcYKMXxwemmFQr7dPsG%2FhqFSnGDlbdvG0dKhBMSVaE7iW9tlNxcWaW4ZfIC1bQMd3xdoQ1ODVhmspw%2FogQI7YGJPYfKwLpolvODj3lecz5l6zNlznOWBHft9TAY0Y34zmnjC7KY8YDLPHMJHL6LwGOqUBNuvc9YEVb3FgtvcMqu43wPQw3HPjwAIazbDhXF3ACOETBPi%2BWS7PGvMLzML2em8%2BCIsZlwoN66LNe4izZpMcdWxBkntIqQUjLkN0YxEP9kBRRpjYgK4gNdqsuMUMYOJVYNTAXCiH7DTNBh6UNXF53q7Qg3K1zrd4vHQsQ2ZCcKERp7oe%2BnKykJC6VDigqYqvpqwD6U3UO%2FcQ4z1%2B7a9cvKEhfAXc&X-Amz-Signature=8a830569a7f0c6bd93be2e90732f198dfd871dc645af56c480b773d3077b06cd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWEABAH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFHlMAJYQg%2BAklxgo84UJpyq0xhwPzf6%2B07gRwvILnsAIgTbGG4U9ypo3FQuEWNNx8Tc7vv19kAflrCI1n%2FUV7EakqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5dYHqXOzuevlKkeCrcA07h3WXFq4BpGKjZPiO%2FLfG8KhlEk05mC5LGdhkxwtWEjU0APAEANf3G7REHP4m10koF5USHA7jsuuwmqv7BMb6eMkfeJ3FoHfx359bT8PbnnUqwspxw5mi8MUGC6ETckjDrXj0o97g9HyEcSzP7xVFil9mVLwBPsrNsQYip6w78mt02%2BwTtVfVxE%2FeH4iet618N%2F6TLIQ9sFrw5DG1e3nj%2F1UQyulBcdoRslpTTOhsl2Ta7noP2yBCsRsq7N8x4xqrfD2it6QlRsElkp1F59UYcJFIVwImAJ8EUuGjFdGNvioA9V0QwO6cy7y1iFBTApIVjdFyNBy9ATO84GHip898lQeuxvIhiUOp0bgsuuEyBYrvDwRoI824GNmbjNIDnvBJjYifJw%2BlVaLyV%2BEVfElWr7kb4bGX3ti0bjFBbhlgnECYtV9%2F%2Fz9bVIyzJFlnc1kzUjbKe6e0RsHesX5Cn6vdG0AOD2ILxChWnnhu3YtYByvwOcYKMXxwemmFQr7dPsG%2FhqFSnGDlbdvG0dKhBMSVaE7iW9tlNxcWaW4ZfIC1bQMd3xdoQ1ODVhmspw%2FogQI7YGJPYfKwLpolvODj3lecz5l6zNlznOWBHft9TAY0Y34zmnjC7KY8YDLPHMJHL6LwGOqUBNuvc9YEVb3FgtvcMqu43wPQw3HPjwAIazbDhXF3ACOETBPi%2BWS7PGvMLzML2em8%2BCIsZlwoN66LNe4izZpMcdWxBkntIqQUjLkN0YxEP9kBRRpjYgK4gNdqsuMUMYOJVYNTAXCiH7DTNBh6UNXF53q7Qg3K1zrd4vHQsQ2ZCcKERp7oe%2BnKykJC6VDigqYqvpqwD6U3UO%2FcQ4z1%2B7a9cvKEhfAXc&X-Amz-Signature=c3c8d768d7e5662780265d7822472d32791dd29fd720e0f72184c363804f66bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWEABAH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFHlMAJYQg%2BAklxgo84UJpyq0xhwPzf6%2B07gRwvILnsAIgTbGG4U9ypo3FQuEWNNx8Tc7vv19kAflrCI1n%2FUV7EakqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5dYHqXOzuevlKkeCrcA07h3WXFq4BpGKjZPiO%2FLfG8KhlEk05mC5LGdhkxwtWEjU0APAEANf3G7REHP4m10koF5USHA7jsuuwmqv7BMb6eMkfeJ3FoHfx359bT8PbnnUqwspxw5mi8MUGC6ETckjDrXj0o97g9HyEcSzP7xVFil9mVLwBPsrNsQYip6w78mt02%2BwTtVfVxE%2FeH4iet618N%2F6TLIQ9sFrw5DG1e3nj%2F1UQyulBcdoRslpTTOhsl2Ta7noP2yBCsRsq7N8x4xqrfD2it6QlRsElkp1F59UYcJFIVwImAJ8EUuGjFdGNvioA9V0QwO6cy7y1iFBTApIVjdFyNBy9ATO84GHip898lQeuxvIhiUOp0bgsuuEyBYrvDwRoI824GNmbjNIDnvBJjYifJw%2BlVaLyV%2BEVfElWr7kb4bGX3ti0bjFBbhlgnECYtV9%2F%2Fz9bVIyzJFlnc1kzUjbKe6e0RsHesX5Cn6vdG0AOD2ILxChWnnhu3YtYByvwOcYKMXxwemmFQr7dPsG%2FhqFSnGDlbdvG0dKhBMSVaE7iW9tlNxcWaW4ZfIC1bQMd3xdoQ1ODVhmspw%2FogQI7YGJPYfKwLpolvODj3lecz5l6zNlznOWBHft9TAY0Y34zmnjC7KY8YDLPHMJHL6LwGOqUBNuvc9YEVb3FgtvcMqu43wPQw3HPjwAIazbDhXF3ACOETBPi%2BWS7PGvMLzML2em8%2BCIsZlwoN66LNe4izZpMcdWxBkntIqQUjLkN0YxEP9kBRRpjYgK4gNdqsuMUMYOJVYNTAXCiH7DTNBh6UNXF53q7Qg3K1zrd4vHQsQ2ZCcKERp7oe%2BnKykJC6VDigqYqvpqwD6U3UO%2FcQ4z1%2B7a9cvKEhfAXc&X-Amz-Signature=d114ba69836161a7b1caf6220bbb491695726d01f5f9d823905e1d7366af3db4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCEBJIGR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFGpf01WXC6fKk7HqXjFoi51rhUb86Cp%2BaUS2Jr0k57eAiEAsm5cjHjwQ40KEpXII9lAu2kqfOA1%2B2U0EIfCp5ZNXk8qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIgDpE3MghlgGaQWgSrcA1SDxRI1rPW3ZwwzCjY5ml40huTbQIZt7%2FC0Cib9To7qXdhiJNtD%2B9j6EDeuKYUbAgZd12X3vEVLSBPcPluMkfA42wAV3kUTn5YKDR3BD8Vqy2VmK%2BHGkxL83x%2F2YFczVyVwxd%2FOT00ncNz4%2BngFP0TjDAETBEeHFbytkp5saTBZR0jc0o7pwCn6vI%2Fd3RUzylac59fmIE9ZDs4ZQCaA0GPmgILZb9OCoenmHibNO8NZ0dUycp9UqDcj6pT%2F4hDwHiDYhHIQr2m%2BBsZA3JnnGn%2BHJ4lcxHcMip7aBgmnUkanJ7ys0sbb5RE5WVe3MWL%2BP2Oqq6gLBVUzSW0N17A%2BF0Ha2ItOzon3SsfiPIdf3h2l7Nn8ZFVKlF63gGS%2F59yTZjDlBSVGiVkUO7KBYyZrjiDc0fAAp1FEMTvESnZShCQoFGqztjrlJDPMFatTtUwLGO3Ldrg4M%2FarBCXwmb8dhRYX6ZCPjSaD2wYhN8tbKU41gAUVyVwCGU0HQi%2B8Ru3oXdE1BEn9Kwy3pW%2FM1Pq8SBmzQ5NRFGCItqYAvALejSuF9Tav5plenjZ%2FNMIP%2FNLWUSPeWHy5capQ64rpO8K6AhK99Y4tNULMniEIyhf238NhR4PbGPE5XNTBtoIfMOjL6LwGOqUBoTnBdLMAr5QVM8rm8D%2BtbS3T5OlTUjQk6rdU%2Bmk2e6xbX1AubwnWdRSnthOuotr4mZIiQ6HOrhd6FBTf8QBH%2FVC1kVJQvOGwcxz2%2FZDrudv%2BnZKExXQky8Y5svU2NwqjMZF%2FkmfJuhQjz2EJ83i7yjQuGnmL9nl9v%2BpEZnOYdC3Z8CJVaDE9NT54yemE4Ix9%2Fg5AL8rs%2BW9MamdCtb6jOkt5YJTV&X-Amz-Signature=ce64287d45bfb9da62a9b0ad11fabfb06178178dd2b45ad6de18778571e50ad2&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ODGF37F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEPCW%2F%2BWacfBcoLBPKtDKacITWoO6stUjSK7Rw%2BzN7mnAiEAs2%2BzzRht23r1IPVtpLXHqR3vbO1O2t0aSP1BDotMYQ8qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiKIuJ%2FsyXkABoVvCrcA9xO0IT61P8wNKD4GmoiHzx%2FD5ZG9iaHPFS3PtU%2BpUh8g%2FXNel3R9iRaEk3hwNLJGfwp5HRrszPJW7Rpm7aj4bho7H2SsTdhDjj09S%2Fz2QVem4KcqSt6ZaqoCmFo%2BUEKhacd0dZqm6m35USJizUHl8vw9paOqDrvx1qYi%2BP5qRxO2ADP5zt2kB77fKzU0cipa827Pe0heCn0MvItl13x310%2BV34tjqO3AjYUVyOZLHY920BmEq9lppoew%2Fw4N1tCQMzUnBkoAfgJN%2B%2FZ9g4dbCf5PcJ%2BBunO670RnkY42Ombt50sbS5Gcm5Na%2B6fqWNsb91mYJRoT1kCwo7AoaDuaTPaRUDS%2F86RVSV6fv%2FezYq43CNjYITe1gdoul8yFXf6npZY26E7uxQ8HVcQzKZ%2BEhgH9R5VJ%2BZQGpTcDilMscjDd5xLFTRHTwur%2B3IBXm8qaBghazcyyvKqO9fZlKWX1hhqtM4CFeQTcczFyPrtzuXOFwr5xeCVnIhJSrtkL%2BLBSWDKpU2mDFvAkhv9W4TR%2BHLcwjt%2B4fxV%2BrmWEftcnxH%2F%2BtJ2P6lxq%2B4RMFnR9%2FT6lR5Fd6VpNRYdWvXQ14IbdXcEXC1m8Ev4TZOFRtknfZNv9FV7Zq2%2BD5AgwxEZMMXL6LwGOqUBH4gHg%2BVqvvFbQpDjhMMLqV3ii9wunPY72fmFlrl0AwB6%2FP1X8Y%2FXN5e5iH8dlUW%2FEj%2Fn2tItgOU1bl5HzJ2AjsLriRymZH51bHaGH5xHdkUgJGenGugBKabXHrV3MzPG1YQeU3nS%2FrRetcNPzVZqsNTe%2FsLWVBqLgmx5%2Fj8GdtkgGIoHI%2Bg4ni1PDdUCoTZGxLLJofxJD8fyes3Teoxl1ALWeXgw&X-Amz-Signature=eba163062bdc369022d90ef3dede46c159c300f3bd766bdff80a0a6104d02116&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MX7NDZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4INCH2vTgc4GsLnCYVG0IcP%2B5HaNbQ5HwcPV9fWW%2FAAiEA1GsnKU43koIl148dI9ld59WroIPERHhzxg0yHo8bRW8qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCDvgdO4YaPPn3WDLircAwKu06zv9hoC0z1xm7vlwEQdHuZoEEtMDxKinFflhLdtHbnj%2BzjEuiHsU9vH%2B0hqZP3WLhOzy5SmYUQ6fUJnwBekaImC1zkNTqX%2FN7ezDu0DY6QkLhKHjAqWhUEg7KWjYGrIbfCvmSZUoQ85Iy2yJwP%2FNi5AhS8K2Pi%2Ba%2Fu%2FsjncR5UD70l47u5noD3lQRtO0N%2Fkdm%2FglnYCD11L10BOnT1XoIsRAPDyafIVEzYiNJ2q6FZFKdpj2WrfHalvQTEV2ZSz9hvsbYdOhmydxCRamt6PypKgcjrqT4CiImwUBOtalnrexDz6sNkULsN2I3HL%2FkCB9BL1bNxI%2B2kgQqjQMy8%2FMhVNvnUA%2BtboLNB84wOGJwpwqArhgOB9kXJfpP6%2Bklq63rOpmXgYENDil5zLF9A64kpcv%2BSQJTKk7zDdm3vdzZympZWjkuoKvdha8mED8%2BQzWLuAXK2LT1uSXftMz50V7%2FluEjBVSvE6%2BORgTG6MDIQDxCdMM2ikFqF6wmOYCt2qUM5Ix1kr%2BNEubm%2BHKK0g0OIDWdQ8pu71%2FyigWR7gC3tnmWR97v3nDyPcewUbKzb7y4Tw8s5m3%2Bu8bAktuY94Dtl6ntDuctmbKmHFzcNqfBjVtoykLAjGni%2FXMPfL6LwGOqUB%2FiI3i%2B3egFyy34grT1D6DFd5Od5viFoU6gXgzH%2Bra9%2Bp78y6wrb3W4gWhM5CBQtEM3Sz4csPyAeR1fhR7KFwgz8nCvSrYIrx0t0SMcPPbN53AlB4MGBKzeLhAAhXlgm4CGudm0NEvXeFerdUb%2F3mCoil3gJ8p4x2Z9GQQWXNaiduRDbXBUi7pbLQLntAcbAJryqSbrEnFPhTCiYDmqDR%2Fn6YHZdb&X-Amz-Signature=3c76024a05663bbb254035a79b621f676eab4daa16e5f678747c7cdca28ea912&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6JHSTDO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuI6OOg9qtCTtCnuFWq075DJiFVQxCZaS9J9CoX2%2B53AiEAtNFY1%2FWIw9F3H9w31KB0QZ3uYIcrWnt0qIFOimEvv8MqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZfEIMhDjZRzRuI5yrcA%2FmHZOfmZG0lHHbCJhPgsYjot5McofoRPKVoDwiQmkoD62PP3MMddpCu07aZXmdWlRN3SzGrax4KkxzrCs%2BsQ%2F7z2keXmOvwWYX0j%2BQiQx7dDRCWHV7%2B5IvylES0DCemtH5K0AcdNCsDkdnHWosz4HBZkZNyFYoR153m1Sh2BvbGxYvlP7Sk0U4wW1VCuuyCwJc%2F4mJAa7cxWDJT4LNiHJlxZVct4aq5OTriGjqcuKlrQ5ziVwt79nYPMHUosvRgX9INHM3i9i%2FFDDgrybw6M4CSn%2B0HUDDwy6PLbwSa%2BvHbHDgKcdy%2FTslJIyotvgGMOL3QysZdzy6c5mWOWahZoLN%2Faj3MGIzR2xQv8SYmVtRTfQlxZoJUlHtH2GRiG63nD66l5oRwBA6TYpE9HdJz27Z9NCpvlnkns270atprTWb5HZv6f%2BZVwZ0kTHlJbke%2F0ypCxSeCUKvoNy470CD6xwSYDrswDP2D9VkJwJxGlA66yCKVGWx%2BMqaIvksDoSKrfDsEvieVOXwcQ6dGLl1f0YcxO6eVRqKxUKmXlL01TALdRrXwKesfAmjDW4C624sBUAQaG29%2FAvpZqMYYsNjG06wI5NE8mtR8Z1fdAMflUdgZJzXavTilLoO%2BbNtoMMfL6LwGOqUBCh5RLlmOJa%2BWS3%2BCnh6fLBbw%2FDQ46Uw8ikuYDzLliQxfqoHP6J9ebY2vpRigWU330%2BNIGT2OiItkbIUrsBUqI5Dp90ZMKhRQuscS82LB2GNJ6hq0G%2BNT5j9iZ6zPXp%2BpCQXQmOvQzJ9iXv%2B3bIFai1yI2TUeZJNzcXjy%2Bs5bw6mvebMMZkD9w%2FdaTBpWZtRgS%2By5mQc7OSd0qeEQx7205VMhKoaZ&X-Amz-Signature=83522c3f8f56ab343d995f2a1cbdad3c974c001ae09e53ed73eb17b7874d8d65&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6JHSTDO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuI6OOg9qtCTtCnuFWq075DJiFVQxCZaS9J9CoX2%2B53AiEAtNFY1%2FWIw9F3H9w31KB0QZ3uYIcrWnt0qIFOimEvv8MqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZfEIMhDjZRzRuI5yrcA%2FmHZOfmZG0lHHbCJhPgsYjot5McofoRPKVoDwiQmkoD62PP3MMddpCu07aZXmdWlRN3SzGrax4KkxzrCs%2BsQ%2F7z2keXmOvwWYX0j%2BQiQx7dDRCWHV7%2B5IvylES0DCemtH5K0AcdNCsDkdnHWosz4HBZkZNyFYoR153m1Sh2BvbGxYvlP7Sk0U4wW1VCuuyCwJc%2F4mJAa7cxWDJT4LNiHJlxZVct4aq5OTriGjqcuKlrQ5ziVwt79nYPMHUosvRgX9INHM3i9i%2FFDDgrybw6M4CSn%2B0HUDDwy6PLbwSa%2BvHbHDgKcdy%2FTslJIyotvgGMOL3QysZdzy6c5mWOWahZoLN%2Faj3MGIzR2xQv8SYmVtRTfQlxZoJUlHtH2GRiG63nD66l5oRwBA6TYpE9HdJz27Z9NCpvlnkns270atprTWb5HZv6f%2BZVwZ0kTHlJbke%2F0ypCxSeCUKvoNy470CD6xwSYDrswDP2D9VkJwJxGlA66yCKVGWx%2BMqaIvksDoSKrfDsEvieVOXwcQ6dGLl1f0YcxO6eVRqKxUKmXlL01TALdRrXwKesfAmjDW4C624sBUAQaG29%2FAvpZqMYYsNjG06wI5NE8mtR8Z1fdAMflUdgZJzXavTilLoO%2BbNtoMMfL6LwGOqUBCh5RLlmOJa%2BWS3%2BCnh6fLBbw%2FDQ46Uw8ikuYDzLliQxfqoHP6J9ebY2vpRigWU330%2BNIGT2OiItkbIUrsBUqI5Dp90ZMKhRQuscS82LB2GNJ6hq0G%2BNT5j9iZ6zPXp%2BpCQXQmOvQzJ9iXv%2B3bIFai1yI2TUeZJNzcXjy%2Bs5bw6mvebMMZkD9w%2FdaTBpWZtRgS%2By5mQc7OSd0qeEQx7205VMhKoaZ&X-Amz-Signature=8c1852ec48288bf8bcf504843e89025bbb48be4cb42426ba83635bdb514aca2a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
