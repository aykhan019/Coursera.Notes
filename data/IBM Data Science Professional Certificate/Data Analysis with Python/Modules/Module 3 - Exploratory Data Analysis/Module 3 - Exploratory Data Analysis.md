

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=2c0d3ac1321507f24f493bd759900164fe01e3f2d04d6f68b81d97e4a45e0fad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=5366e739541dec755312ae5875b09e16614e6fca8399bb16f7440a5e7c504f1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=5550d4c7ce4493730e09fa06599ac488709d046118b9c564691e573b6bee9d49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U56UISOB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEZO2q3hXmtcOLsP4WhKGQ3TcjHc8U7WxronPy%2FLmLrdAiBr9G%2BtVxzNaeyopUGb6deIR6r7BkwBEfhOflE0baLyFir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMGuDBmXYtqH%2FbPHbZKtwDlLhUagk7qDBAiWfz7gYQbp6XJ%2FQM6FIL8CiS%2FBRBgBWg4R9yqS6TaJR0GpWs7xHZqZ2AgQALXYdyFFS0CLBuHpVZSOmm%2F%2F%2FM5Sg12dcSwirglUSRjJLkV1%2BBZ8zRHAZe3shrWBx0EqXjolBHGfbPtQpNT45DIa3TYR%2Big9JYnz%2FgY6Cmp8IzWy%2ByVFYAqGY1jm4gB7ZEaVXSbHfCUxw2fMkcKbD9xtnwrw0omj7zb5bQstTC0PgEIYFCiQWW9zRkAtAihPOuxlNmnXq19BSwZsYAzwv2l2tLt3ajrJKlHiBbYqI96LiffptFb5DznMRv1H2zsbmuMeh6v9hqYn%2FgrKCrh%2FKPnMi5wDWNhxFk94h2B0p%2BybRE%2B9olKVQ0c921GxBul3mtpDipuHhPZYU%2FMNErWVUp%2BmBsRpmDxUtOsIpcTJDPpzf3MObeB6mMXbESbBiR%2BBhRZPuXKVA2mzhXy5%2FqBjhxpcB9eIY82wfzB3XFC1uzPF%2FVOBIujysoluMPCS8JnwALsQgNOdI2OZvEX62up3r%2FiwB3nGXk%2BxevVg8%2B7hRReVBrdKsQVXdfEJofoYtdq3wolM2TV2ckaWTxy374XIGUBEVF0QYC8UrDv3hFmsRf3wKP%2ByQkptYw%2F4uNvQY6pgHMwJz04DBbU%2BCFpzSPm3rs9R99tCfnsTY6EolbHaIkq9fc9yw47x6ENvOQ5oKJqKfVW%2BOaP58wfWMXGNiukT%2BGE%2Bg9jMD%2FOvn1puV%2FIomye%2FK1is6GsVM1f7K8SOPfFT1TOmhzLasVv8EkHWsapxTqyB22%2FFLnamGmLuTpsurfy5wjeJqF2RvOzYaKGI4%2BGzw6FXZFlUzf67PlccejEfn%2Fwx3vNv31&X-Amz-Signature=22fc7f79e21435233da5ef147346fbd11b4b1e271b2320b088826c31c44160c2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U56UISOB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEZO2q3hXmtcOLsP4WhKGQ3TcjHc8U7WxronPy%2FLmLrdAiBr9G%2BtVxzNaeyopUGb6deIR6r7BkwBEfhOflE0baLyFir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMGuDBmXYtqH%2FbPHbZKtwDlLhUagk7qDBAiWfz7gYQbp6XJ%2FQM6FIL8CiS%2FBRBgBWg4R9yqS6TaJR0GpWs7xHZqZ2AgQALXYdyFFS0CLBuHpVZSOmm%2F%2F%2FM5Sg12dcSwirglUSRjJLkV1%2BBZ8zRHAZe3shrWBx0EqXjolBHGfbPtQpNT45DIa3TYR%2Big9JYnz%2FgY6Cmp8IzWy%2ByVFYAqGY1jm4gB7ZEaVXSbHfCUxw2fMkcKbD9xtnwrw0omj7zb5bQstTC0PgEIYFCiQWW9zRkAtAihPOuxlNmnXq19BSwZsYAzwv2l2tLt3ajrJKlHiBbYqI96LiffptFb5DznMRv1H2zsbmuMeh6v9hqYn%2FgrKCrh%2FKPnMi5wDWNhxFk94h2B0p%2BybRE%2B9olKVQ0c921GxBul3mtpDipuHhPZYU%2FMNErWVUp%2BmBsRpmDxUtOsIpcTJDPpzf3MObeB6mMXbESbBiR%2BBhRZPuXKVA2mzhXy5%2FqBjhxpcB9eIY82wfzB3XFC1uzPF%2FVOBIujysoluMPCS8JnwALsQgNOdI2OZvEX62up3r%2FiwB3nGXk%2BxevVg8%2B7hRReVBrdKsQVXdfEJofoYtdq3wolM2TV2ckaWTxy374XIGUBEVF0QYC8UrDv3hFmsRf3wKP%2ByQkptYw%2F4uNvQY6pgHMwJz04DBbU%2BCFpzSPm3rs9R99tCfnsTY6EolbHaIkq9fc9yw47x6ENvOQ5oKJqKfVW%2BOaP58wfWMXGNiukT%2BGE%2Bg9jMD%2FOvn1puV%2FIomye%2FK1is6GsVM1f7K8SOPfFT1TOmhzLasVv8EkHWsapxTqyB22%2FFLnamGmLuTpsurfy5wjeJqF2RvOzYaKGI4%2BGzw6FXZFlUzf67PlccejEfn%2Fwx3vNv31&X-Amz-Signature=099f347027aa0e089c629c4cf40ddde212879e98a22562ada5a85139018ddbf1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U56UISOB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEZO2q3hXmtcOLsP4WhKGQ3TcjHc8U7WxronPy%2FLmLrdAiBr9G%2BtVxzNaeyopUGb6deIR6r7BkwBEfhOflE0baLyFir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMGuDBmXYtqH%2FbPHbZKtwDlLhUagk7qDBAiWfz7gYQbp6XJ%2FQM6FIL8CiS%2FBRBgBWg4R9yqS6TaJR0GpWs7xHZqZ2AgQALXYdyFFS0CLBuHpVZSOmm%2F%2F%2FM5Sg12dcSwirglUSRjJLkV1%2BBZ8zRHAZe3shrWBx0EqXjolBHGfbPtQpNT45DIa3TYR%2Big9JYnz%2FgY6Cmp8IzWy%2ByVFYAqGY1jm4gB7ZEaVXSbHfCUxw2fMkcKbD9xtnwrw0omj7zb5bQstTC0PgEIYFCiQWW9zRkAtAihPOuxlNmnXq19BSwZsYAzwv2l2tLt3ajrJKlHiBbYqI96LiffptFb5DznMRv1H2zsbmuMeh6v9hqYn%2FgrKCrh%2FKPnMi5wDWNhxFk94h2B0p%2BybRE%2B9olKVQ0c921GxBul3mtpDipuHhPZYU%2FMNErWVUp%2BmBsRpmDxUtOsIpcTJDPpzf3MObeB6mMXbESbBiR%2BBhRZPuXKVA2mzhXy5%2FqBjhxpcB9eIY82wfzB3XFC1uzPF%2FVOBIujysoluMPCS8JnwALsQgNOdI2OZvEX62up3r%2FiwB3nGXk%2BxevVg8%2B7hRReVBrdKsQVXdfEJofoYtdq3wolM2TV2ckaWTxy374XIGUBEVF0QYC8UrDv3hFmsRf3wKP%2ByQkptYw%2F4uNvQY6pgHMwJz04DBbU%2BCFpzSPm3rs9R99tCfnsTY6EolbHaIkq9fc9yw47x6ENvOQ5oKJqKfVW%2BOaP58wfWMXGNiukT%2BGE%2Bg9jMD%2FOvn1puV%2FIomye%2FK1is6GsVM1f7K8SOPfFT1TOmhzLasVv8EkHWsapxTqyB22%2FFLnamGmLuTpsurfy5wjeJqF2RvOzYaKGI4%2BGzw6FXZFlUzf67PlccejEfn%2Fwx3vNv31&X-Amz-Signature=d2cb3a69c0c49e1be69d124d1a9ffa3a2275a23a8b5e37b89f9dcab50d176d1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U56UISOB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEZO2q3hXmtcOLsP4WhKGQ3TcjHc8U7WxronPy%2FLmLrdAiBr9G%2BtVxzNaeyopUGb6deIR6r7BkwBEfhOflE0baLyFir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMGuDBmXYtqH%2FbPHbZKtwDlLhUagk7qDBAiWfz7gYQbp6XJ%2FQM6FIL8CiS%2FBRBgBWg4R9yqS6TaJR0GpWs7xHZqZ2AgQALXYdyFFS0CLBuHpVZSOmm%2F%2F%2FM5Sg12dcSwirglUSRjJLkV1%2BBZ8zRHAZe3shrWBx0EqXjolBHGfbPtQpNT45DIa3TYR%2Big9JYnz%2FgY6Cmp8IzWy%2ByVFYAqGY1jm4gB7ZEaVXSbHfCUxw2fMkcKbD9xtnwrw0omj7zb5bQstTC0PgEIYFCiQWW9zRkAtAihPOuxlNmnXq19BSwZsYAzwv2l2tLt3ajrJKlHiBbYqI96LiffptFb5DznMRv1H2zsbmuMeh6v9hqYn%2FgrKCrh%2FKPnMi5wDWNhxFk94h2B0p%2BybRE%2B9olKVQ0c921GxBul3mtpDipuHhPZYU%2FMNErWVUp%2BmBsRpmDxUtOsIpcTJDPpzf3MObeB6mMXbESbBiR%2BBhRZPuXKVA2mzhXy5%2FqBjhxpcB9eIY82wfzB3XFC1uzPF%2FVOBIujysoluMPCS8JnwALsQgNOdI2OZvEX62up3r%2FiwB3nGXk%2BxevVg8%2B7hRReVBrdKsQVXdfEJofoYtdq3wolM2TV2ckaWTxy374XIGUBEVF0QYC8UrDv3hFmsRf3wKP%2ByQkptYw%2F4uNvQY6pgHMwJz04DBbU%2BCFpzSPm3rs9R99tCfnsTY6EolbHaIkq9fc9yw47x6ENvOQ5oKJqKfVW%2BOaP58wfWMXGNiukT%2BGE%2Bg9jMD%2FOvn1puV%2FIomye%2FK1is6GsVM1f7K8SOPfFT1TOmhzLasVv8EkHWsapxTqyB22%2FFLnamGmLuTpsurfy5wjeJqF2RvOzYaKGI4%2BGzw6FXZFlUzf67PlccejEfn%2Fwx3vNv31&X-Amz-Signature=5f53c7ecc3370732eadd01b222d053f8fa8aec6f4ea970c5e1142cb534974764&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U56UISOB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEZO2q3hXmtcOLsP4WhKGQ3TcjHc8U7WxronPy%2FLmLrdAiBr9G%2BtVxzNaeyopUGb6deIR6r7BkwBEfhOflE0baLyFir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMGuDBmXYtqH%2FbPHbZKtwDlLhUagk7qDBAiWfz7gYQbp6XJ%2FQM6FIL8CiS%2FBRBgBWg4R9yqS6TaJR0GpWs7xHZqZ2AgQALXYdyFFS0CLBuHpVZSOmm%2F%2F%2FM5Sg12dcSwirglUSRjJLkV1%2BBZ8zRHAZe3shrWBx0EqXjolBHGfbPtQpNT45DIa3TYR%2Big9JYnz%2FgY6Cmp8IzWy%2ByVFYAqGY1jm4gB7ZEaVXSbHfCUxw2fMkcKbD9xtnwrw0omj7zb5bQstTC0PgEIYFCiQWW9zRkAtAihPOuxlNmnXq19BSwZsYAzwv2l2tLt3ajrJKlHiBbYqI96LiffptFb5DznMRv1H2zsbmuMeh6v9hqYn%2FgrKCrh%2FKPnMi5wDWNhxFk94h2B0p%2BybRE%2B9olKVQ0c921GxBul3mtpDipuHhPZYU%2FMNErWVUp%2BmBsRpmDxUtOsIpcTJDPpzf3MObeB6mMXbESbBiR%2BBhRZPuXKVA2mzhXy5%2FqBjhxpcB9eIY82wfzB3XFC1uzPF%2FVOBIujysoluMPCS8JnwALsQgNOdI2OZvEX62up3r%2FiwB3nGXk%2BxevVg8%2B7hRReVBrdKsQVXdfEJofoYtdq3wolM2TV2ckaWTxy374XIGUBEVF0QYC8UrDv3hFmsRf3wKP%2ByQkptYw%2F4uNvQY6pgHMwJz04DBbU%2BCFpzSPm3rs9R99tCfnsTY6EolbHaIkq9fc9yw47x6ENvOQ5oKJqKfVW%2BOaP58wfWMXGNiukT%2BGE%2Bg9jMD%2FOvn1puV%2FIomye%2FK1is6GsVM1f7K8SOPfFT1TOmhzLasVv8EkHWsapxTqyB22%2FFLnamGmLuTpsurfy5wjeJqF2RvOzYaKGI4%2BGzw6FXZFlUzf67PlccejEfn%2Fwx3vNv31&X-Amz-Signature=e3e13fd68bacbe60e180a313709fec701164cd0ea4be9f9454162a5ad5b742df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U56UISOB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEZO2q3hXmtcOLsP4WhKGQ3TcjHc8U7WxronPy%2FLmLrdAiBr9G%2BtVxzNaeyopUGb6deIR6r7BkwBEfhOflE0baLyFir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMGuDBmXYtqH%2FbPHbZKtwDlLhUagk7qDBAiWfz7gYQbp6XJ%2FQM6FIL8CiS%2FBRBgBWg4R9yqS6TaJR0GpWs7xHZqZ2AgQALXYdyFFS0CLBuHpVZSOmm%2F%2F%2FM5Sg12dcSwirglUSRjJLkV1%2BBZ8zRHAZe3shrWBx0EqXjolBHGfbPtQpNT45DIa3TYR%2Big9JYnz%2FgY6Cmp8IzWy%2ByVFYAqGY1jm4gB7ZEaVXSbHfCUxw2fMkcKbD9xtnwrw0omj7zb5bQstTC0PgEIYFCiQWW9zRkAtAihPOuxlNmnXq19BSwZsYAzwv2l2tLt3ajrJKlHiBbYqI96LiffptFb5DznMRv1H2zsbmuMeh6v9hqYn%2FgrKCrh%2FKPnMi5wDWNhxFk94h2B0p%2BybRE%2B9olKVQ0c921GxBul3mtpDipuHhPZYU%2FMNErWVUp%2BmBsRpmDxUtOsIpcTJDPpzf3MObeB6mMXbESbBiR%2BBhRZPuXKVA2mzhXy5%2FqBjhxpcB9eIY82wfzB3XFC1uzPF%2FVOBIujysoluMPCS8JnwALsQgNOdI2OZvEX62up3r%2FiwB3nGXk%2BxevVg8%2B7hRReVBrdKsQVXdfEJofoYtdq3wolM2TV2ckaWTxy374XIGUBEVF0QYC8UrDv3hFmsRf3wKP%2ByQkptYw%2F4uNvQY6pgHMwJz04DBbU%2BCFpzSPm3rs9R99tCfnsTY6EolbHaIkq9fc9yw47x6ENvOQ5oKJqKfVW%2BOaP58wfWMXGNiukT%2BGE%2Bg9jMD%2FOvn1puV%2FIomye%2FK1is6GsVM1f7K8SOPfFT1TOmhzLasVv8EkHWsapxTqyB22%2FFLnamGmLuTpsurfy5wjeJqF2RvOzYaKGI4%2BGzw6FXZFlUzf67PlccejEfn%2Fwx3vNv31&X-Amz-Signature=0d2156651f8cfe92e66096ce00a6110a0240bc33d2c263d7dca6e34cb0d1ed54&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TARW7VO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFE5Fqf7fOoDyNT1xjXAicStOD7HYD4P9uDII8o3mRlHAiEA5r3kgdAgV5uSXG5Mm0T37BYRGu8%2BVgDvb1EgIRRWYjYq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDEdgH%2FzQujnVuyANaCrcA84Qw91ks%2FUkNL4OKAxkSi1IBu%2FJrJN2jeBp9qxvb4cob%2B5kOqYThY5dEPQ9jI2N2txZl7vlziZ0BD0BRyAC6FuXGcznxvM5MTh2Eum4CAmR9Y4r9bG1t9J63b8bc1aDqFgQXwgtEZbYAgzt5YcF%2B9sVCGI2Xi7A3UMhrtbu%2FDfdgoeH81ciMYvMVv1rySu4nDJdGw5vLPEqv%2Fq2ERinySHPMWw156youoVQQu6l0gkCze8ZNIeYRu0GMIeswpZhn8MXmo3nGtvoa1WEmBMsPMcNpjxrxJWZWY5gcm1%2Biu2ZpvDXJ3tzbQgUti1%2Fp6ztmOFML%2BMm%2Ba8HTYQqp9Tu4X6hmysqnBIAHe7ef9u04Etxy2grVGM0%2FT7SJcz%2FAiE5FpZC%2BcOewtLdmYGJQ2oCQc47%2BSXYmD74espX6SobAzZD7NODnnPY7OoGoTJe6zA092M%2BuxmjbT90zER9RZ8e1hjrS%2BD%2FZEknttTfitHvo0R7kt9Ct3ofkKp6783unxnUB9tsBYwhXRut4N4L%2Fn9%2BQ0LJfx1hhHO4ckQKwzsUSv9xjmZtec46xlDt4vLs7AGZAEELq%2FsQZ3Ow1wWsJzO6Aar5nSUo8VhHPdhWuA%2FiJ%2FkN0dSZDRDLDmWAQ4E8MKGLjb0GOqUBBINjbI04d0vE8WdE0ysfyy%2BkZWIjO9p0mWNoBnbtTDCLy6e36kip8CBCYGkBXqBPShG2XUcCJpi3cLm6vmawf7YLXZVH9Hu3Wpf2Jhz%2BJs%2BKRvdjSYekd%2B3wrfsWaw4THhUdfXtENwnMnVf%2BmIGu8rWc06zKxQtuLk09cRpm2w%2B%2BuG4cuSAvhb1LXQJRX0m5hDE9ADobX03hhQ6k8x442922sO3x&X-Amz-Signature=3facaf6b5eccb9690c3b4e96a18d5052f7146af50144da3d01a9a03868e1dd8b&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE7SQFIX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCt2cK7DY8OATDC5v%2BD%2BySgP0dOdckmBeVtRbm%2BsG4TmgIgXvEq%2BBaQ2MWQLM%2Figkp50RaLhBiiIbRVQZU%2FkynQJscq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDM74DaNKuU3VoO0gvyrcA0kSJn74BSdfrSiyV8XbIFI5PBN8C0ngiYejaZH5F42a1HAXqisLDaJYJx3q%2B0a370lOz0urWjRlg5dvtQdIHRqeH8z9CXQ6ySugWjSspuda%2FqaYNI6La2lq9h3hXHdNWt1LRdxgzRPlRR3ZToWpNm43g8zWk12EqDTuB3CXnVc0GZ1t2ke%2Bgojupbow%2FYL8DiRtg1ij8EWyMKFtOdP9Oq%2B8oGc2ggRM%2F9fD3CIFKehMrBP9dtmX0XXMaNzMsUx7DdD6tsspGOcIAsYwmLwZahW1tuuxj5M8GR9L82lEx%2Fz0FX0BWwN4OiNpkas33AEgmRaFpb7XSXXcLAwiznDaVNjG14C2WG6Ns2D%2FDzfP3Q5Z22z%2BGAoSOfbe4aVlTwQX6%2Br8nGKjaLNkv%2FbwZkRxUyu%2FGZJklVFQrf1AV0RiTm%2FhflOgIM0sLCwXEHQO86rvdzwX5ufd755WmUcTJfNhIPy4MK4zuec1RD2sNnN4JqJsAnYDmQUIpEM3W0Dk0y1kD%2B7BBM%2FqhERh582bk15%2Fz%2BUuxPXL4evpvuZPRTBMd%2Bt0EfZMv1fNyKo7IFp%2F5YEr50ChmOFLh9ldTvPmMZseBe0ifKXoK7AH1%2FaOmteBHuPzuMbGNrWsIg8d5y1MMLiLjb0GOqUBoie1Y9PNYW6edhmHwKoHw25YG8qshBdEpshhH1BF8GVMdNEPNsmmNSCP5HV7wIuiW0jFl8V1FPt6KclVvsGm2kwQEaEMtCtXXQEZ6UlJy%2FmAYpyRBLBJkPRGPYByoXMp3rTEp4Njq0NrNXpqbILwVPASqLWVcgxe%2FtU43hkmf8an0cl577M3UsENYnGg1Ub8hK0IXAYFdshApiVarHNKIEf%2FR2L4&X-Amz-Signature=f0d4a0146a8f4764cbae1c0cc35f65ce517974c26efd932c136db0bd352ebd87&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U56UISOB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEZO2q3hXmtcOLsP4WhKGQ3TcjHc8U7WxronPy%2FLmLrdAiBr9G%2BtVxzNaeyopUGb6deIR6r7BkwBEfhOflE0baLyFir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMGuDBmXYtqH%2FbPHbZKtwDlLhUagk7qDBAiWfz7gYQbp6XJ%2FQM6FIL8CiS%2FBRBgBWg4R9yqS6TaJR0GpWs7xHZqZ2AgQALXYdyFFS0CLBuHpVZSOmm%2F%2F%2FM5Sg12dcSwirglUSRjJLkV1%2BBZ8zRHAZe3shrWBx0EqXjolBHGfbPtQpNT45DIa3TYR%2Big9JYnz%2FgY6Cmp8IzWy%2ByVFYAqGY1jm4gB7ZEaVXSbHfCUxw2fMkcKbD9xtnwrw0omj7zb5bQstTC0PgEIYFCiQWW9zRkAtAihPOuxlNmnXq19BSwZsYAzwv2l2tLt3ajrJKlHiBbYqI96LiffptFb5DznMRv1H2zsbmuMeh6v9hqYn%2FgrKCrh%2FKPnMi5wDWNhxFk94h2B0p%2BybRE%2B9olKVQ0c921GxBul3mtpDipuHhPZYU%2FMNErWVUp%2BmBsRpmDxUtOsIpcTJDPpzf3MObeB6mMXbESbBiR%2BBhRZPuXKVA2mzhXy5%2FqBjhxpcB9eIY82wfzB3XFC1uzPF%2FVOBIujysoluMPCS8JnwALsQgNOdI2OZvEX62up3r%2FiwB3nGXk%2BxevVg8%2B7hRReVBrdKsQVXdfEJofoYtdq3wolM2TV2ckaWTxy374XIGUBEVF0QYC8UrDv3hFmsRf3wKP%2ByQkptYw%2F4uNvQY6pgHMwJz04DBbU%2BCFpzSPm3rs9R99tCfnsTY6EolbHaIkq9fc9yw47x6ENvOQ5oKJqKfVW%2BOaP58wfWMXGNiukT%2BGE%2Bg9jMD%2FOvn1puV%2FIomye%2FK1is6GsVM1f7K8SOPfFT1TOmhzLasVv8EkHWsapxTqyB22%2FFLnamGmLuTpsurfy5wjeJqF2RvOzYaKGI4%2BGzw6FXZFlUzf67PlccejEfn%2Fwx3vNv31&X-Amz-Signature=b01c1e2c3765a61308b8644702ba948bcbc3fbafc8e9be27f30aca61d6de7aaf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U56UISOB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEZO2q3hXmtcOLsP4WhKGQ3TcjHc8U7WxronPy%2FLmLrdAiBr9G%2BtVxzNaeyopUGb6deIR6r7BkwBEfhOflE0baLyFir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMGuDBmXYtqH%2FbPHbZKtwDlLhUagk7qDBAiWfz7gYQbp6XJ%2FQM6FIL8CiS%2FBRBgBWg4R9yqS6TaJR0GpWs7xHZqZ2AgQALXYdyFFS0CLBuHpVZSOmm%2F%2F%2FM5Sg12dcSwirglUSRjJLkV1%2BBZ8zRHAZe3shrWBx0EqXjolBHGfbPtQpNT45DIa3TYR%2Big9JYnz%2FgY6Cmp8IzWy%2ByVFYAqGY1jm4gB7ZEaVXSbHfCUxw2fMkcKbD9xtnwrw0omj7zb5bQstTC0PgEIYFCiQWW9zRkAtAihPOuxlNmnXq19BSwZsYAzwv2l2tLt3ajrJKlHiBbYqI96LiffptFb5DznMRv1H2zsbmuMeh6v9hqYn%2FgrKCrh%2FKPnMi5wDWNhxFk94h2B0p%2BybRE%2B9olKVQ0c921GxBul3mtpDipuHhPZYU%2FMNErWVUp%2BmBsRpmDxUtOsIpcTJDPpzf3MObeB6mMXbESbBiR%2BBhRZPuXKVA2mzhXy5%2FqBjhxpcB9eIY82wfzB3XFC1uzPF%2FVOBIujysoluMPCS8JnwALsQgNOdI2OZvEX62up3r%2FiwB3nGXk%2BxevVg8%2B7hRReVBrdKsQVXdfEJofoYtdq3wolM2TV2ckaWTxy374XIGUBEVF0QYC8UrDv3hFmsRf3wKP%2ByQkptYw%2F4uNvQY6pgHMwJz04DBbU%2BCFpzSPm3rs9R99tCfnsTY6EolbHaIkq9fc9yw47x6ENvOQ5oKJqKfVW%2BOaP58wfWMXGNiukT%2BGE%2Bg9jMD%2FOvn1puV%2FIomye%2FK1is6GsVM1f7K8SOPfFT1TOmhzLasVv8EkHWsapxTqyB22%2FFLnamGmLuTpsurfy5wjeJqF2RvOzYaKGI4%2BGzw6FXZFlUzf67PlccejEfn%2Fwx3vNv31&X-Amz-Signature=0c7a98756a934e8113ea2e580eb86f5dbaf5e0ef005dadad3762c7f94157dc4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U56UISOB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEZO2q3hXmtcOLsP4WhKGQ3TcjHc8U7WxronPy%2FLmLrdAiBr9G%2BtVxzNaeyopUGb6deIR6r7BkwBEfhOflE0baLyFir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMGuDBmXYtqH%2FbPHbZKtwDlLhUagk7qDBAiWfz7gYQbp6XJ%2FQM6FIL8CiS%2FBRBgBWg4R9yqS6TaJR0GpWs7xHZqZ2AgQALXYdyFFS0CLBuHpVZSOmm%2F%2F%2FM5Sg12dcSwirglUSRjJLkV1%2BBZ8zRHAZe3shrWBx0EqXjolBHGfbPtQpNT45DIa3TYR%2Big9JYnz%2FgY6Cmp8IzWy%2ByVFYAqGY1jm4gB7ZEaVXSbHfCUxw2fMkcKbD9xtnwrw0omj7zb5bQstTC0PgEIYFCiQWW9zRkAtAihPOuxlNmnXq19BSwZsYAzwv2l2tLt3ajrJKlHiBbYqI96LiffptFb5DznMRv1H2zsbmuMeh6v9hqYn%2FgrKCrh%2FKPnMi5wDWNhxFk94h2B0p%2BybRE%2B9olKVQ0c921GxBul3mtpDipuHhPZYU%2FMNErWVUp%2BmBsRpmDxUtOsIpcTJDPpzf3MObeB6mMXbESbBiR%2BBhRZPuXKVA2mzhXy5%2FqBjhxpcB9eIY82wfzB3XFC1uzPF%2FVOBIujysoluMPCS8JnwALsQgNOdI2OZvEX62up3r%2FiwB3nGXk%2BxevVg8%2B7hRReVBrdKsQVXdfEJofoYtdq3wolM2TV2ckaWTxy374XIGUBEVF0QYC8UrDv3hFmsRf3wKP%2ByQkptYw%2F4uNvQY6pgHMwJz04DBbU%2BCFpzSPm3rs9R99tCfnsTY6EolbHaIkq9fc9yw47x6ENvOQ5oKJqKfVW%2BOaP58wfWMXGNiukT%2BGE%2Bg9jMD%2FOvn1puV%2FIomye%2FK1is6GsVM1f7K8SOPfFT1TOmhzLasVv8EkHWsapxTqyB22%2FFLnamGmLuTpsurfy5wjeJqF2RvOzYaKGI4%2BGzw6FXZFlUzf67PlccejEfn%2Fwx3vNv31&X-Amz-Signature=8eb6201ab2e1093bd403f45f6d17881db0685809fc66a11a77e484faac3ecd2e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMGTI6QU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIET98eggxbVyOOFkfZYyhXdH%2B3yvtxIOtJ0%2BnFIybh4KAiEAycfiBmmKvIqa9byFGtoqobCZdvZhxB2dmR%2BwAZADQaIq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDJIyJ89Gw6g7xDjjOCrcA42Tus6QIEfvsyQZ1vzO0OI7N9h1W1F%2FIG4SQqOshONpYb1XXGILkRvHOuiM8MbqqMnbyQTUj8dp%2FsJMSWGMSmF2WMcFstiDNS%2B53aCKwM5pulQJnqN5yhg4tR7fiHqg53VQYlMjrJ1UWQp0KdKgz9gOCwHbpLJfiHGAUFuD7XgZ%2BY8F93PrOPCYqOMYbhpFHglkvOeF4WHZNnayJu3C7TvSpT3lv5MEccKi273bykunn0JyqWqhGl6lcEhM%2FBCiD0aiKDd2JqAZWj9U3LYZ3j4KBVOw26yRRni217yhxJ9agt%2B13MB0r1wXOKU5C4HkM%2FKl4c9jkQsBHFK86HW7uTiHSyT5DVAa5Z2lDsPu%2B09G0ImHnI02n7%2FSD8jx0qq9eaOMBRphKctZT4VA2iz3mf6QC06NZ84aoogr67WUl9C9Gg4dwquszGrySd%2F1zMUQOwOuAV6L6ev%2FGtiC%2FK%2FPiZOAQcAtWXtAu5AOLBeWHRB%2BO7JhcTro%2BDKMliFODDujiEnR9B%2B29CxS52g0YilOoIu4wa8kANOpyjAsomnJezvvHqy0HR4J%2FOjJdJSIQetWk%2BFbk5HfnCFhF8Ua7I%2FRg0w52oVdqvWpP7QDv4pwyB3iymbeb7VpBzwZiY4RMPuKjb0GOqUBEG7CdALlqY6UgWlX2KIKgZTpPK30s1wGcbCnjDui0plbMZhXxlT0Rhev7vsLf8AXs%2Fr5T23ne8WoCI52UVqfv3x7wFE53ErNgTHe4t1bax8J6Tf%2FaSnc5pt6RLTMWzMzfwgExEeY%2F3DfwzvH4OvvG3dO86xZvnXWyNN18WdySafWJcEGvj6KoJc1NPPsFcoGYwAaG4ECXNu1%2BXizLqoP5OxrU3PM&X-Amz-Signature=9d850a974ef2796e86b6d897e1c3642e6853eafce3738bf89c901645611c3a85&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GQN4ACR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDj9uWR2uC9EPQbwywVcnM4pPnrtXbo463bo%2B6p%2FMDUsQIgJRzai2pPoSj2KeJYAIOzfKOT3w5F6Vg%2F0D5WBrQPOYUq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDAmhl7lieBq3X3XkfSrcA3%2B6gz9nizAm7uiVftywNAS5WlcLIG9bGggUnCQYDIRyllgmwZDAfjyono%2FjG8ZECgd5gcpPbxc%2B5f6YA7dthAG60Xa7wHD8pwiincNxWcmAldhlFf4Re0Sqhv0p91cEAPAt5nLRC%2FjF2rfI22BfOWS9h7zYpLRUxXD%2FPpKTH4xWFOTqTRnbYgYqwNYS8jTqTYNq2JSFANsoZkAYyeojm7AjyXQt%2FrG3z%2F9D96x5ql4mj7PSWRdOSeJ5DtQtOuPoaNc%2BGTySRiPvhM7gE7B%2F5GWjGJoXoR8v16r%2Bj6oHUUgIGnvDyoA5Tey3k5CNugCxX4jREfSDcVHBAMQDUFIKhXY46teQ5Dqi4moVtwEQeS8HjSesNjCEHvfRt2xHy2DxQwGMhUSHdZbihBLmwtd6UGSO4Moj205%2FHVpSqVfzv3t%2FnYzO%2F7SI7Hk%2F2BZg0iZXdFDo7jNLisbkRkIlnb9NTPHiLP8ktk25lP6RbeTpdEMPKb2TIbyi6ulsTUACyV4%2BElSrOwynnvV8CZ%2Be1hOppx4RtVkDd%2BR%2BteP%2FF8nE6ojzeFwipa2Wfbn3Rvy%2FNp1ne6JD51QvtVQKk%2FGN0dXQg9sMMW2%2BBBKKXaTT%2FjeFUeZY5WeMvAakrZMZr3avMNSKjb0GOqUBwtZoaOAPGtJb6NagjkhDQF9Oqi5y0r65JkM58yMjLIh9bjxweqEwA1p%2F8CdVoyKVz2kLWT6VyyON39nH8kOpGGKZh8LJUDTK3CEdV0QOLVqxOcxBCCpDjLNVo8k0azMZ1QLF5du3ypAdG%2B03jnNWfeOOq9tdkhgI9fN48f6iQPCGqRZOJzT3xReKi5fc9SlvBP32d432dO3ubHJS%2FnOCuTyQprIF&X-Amz-Signature=62b7e4e37a433806072b8d74191ebc9e140523ad8df6011108788195b04f2348&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XUVQVTJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIGIZNk2wbg2uATI1UTtYYlUoSbTkLWD8Rb6KstdxGi5NAiBRHPNInN%2BrqD8aBN5oY1t%2BUJXBbA381Oe46uRjIjuIJir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMj5Q1p7v8WPtrzSPwKtwDZ8mjtGtwTqX9jG1SbOmSWlH85dZBVt1gadMTibRKRS8%2BOu8%2F%2FSR8KZ7eygqhX1a4hsw%2BAAr2sDyZf0bmDUsYtySStb6f6pXQsmQsC5KCLlliNd0AyHzm7bWDOdOXoprXZFxESjZQMwB5P%2F8mUU0fS6o25hiuchPpybY8JaHouQMC7jrXCKP3NhLvrHpeF5l9XsZglZKc0lBrdcEdcZZKwgo%2BHGyrVn04%2BpuidhcgXT2effoQutz6E60zbROVtvdVoJbP4xju8d%2FljNmL9L2JDl6b1fxvv13VIjs%2BPqMQ0qIAcybevevtlrtUjJL7h550QuoXMPQm2rRDFi4RUjR7N4UGrh2TZRcsGOOqUTKsx5DELY%2FAmsJwbde6TCErSJbPIPd%2BDQhBZc0iwsA%2FIiQl3XO0BYO6NqNVa5vn0dUFWsiS2pGKddOYKWi4SDrW9549KCZIIRFua1O4t9lbU9X%2Fbm2OZFf51KSgKQrzdKu79llpJnfX7a7KdwYVFJUur4XLwxhuuyuIfsM2h0wBYxQ6rQavjdkIYAe2DY8Qe7J17Df0JrYpTX1e6kCUe8GFvu2z9Fsy9682f6%2BjkyGRXvvpYLd3ezMqrDxt6%2FcdiSlrJcBRhKpdll%2F2%2F6NjkcQw6YqNvQY6pgHLsDShFfsF%2F9%2BtldlqQ94ycRGFOT6RdGt9MN8Zzy2pS0rOd%2F6VAu1TWMNLaQJC3QvmkRbho1IVBSMdSYDf0dGpYSvg3aHEU9HyHxF%2Frb8gAY7wLyt%2FMDDHY%2BqgupOh7CO6HKQhVfg4Q5TQh%2Fc0gUlsOLYFNGbirwpF35nOO%2BpwQE5mP5OztHtE5Xji3QQukyn%2FZEd05CXQNA%2BrRuuo%2F3qOns4n5NRK&X-Amz-Signature=aa8c228338bc62ef3af0d77c4bf2cbc1a0f691acace798e39c05bb1734373bdd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BGYRENA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD5NzhaTL8vu1n6v8h4i7PAX%2F9lkKZ2%2B%2BsWMTeaF5RhMAIhAJznCvNhecniuDoPGhc3Sro2EB68cuELU8UaO8i2Ke61Kv8DCEQQABoMNjM3NDIzMTgzODA1IgxLjxbdTHGpIpqhxcEq3AOVd7C4fv6TxI6VmVxasxfTIfnYDSdfMjoWOPa6oD0ngDOD8Bs%2BUxdEJI2yS3MzAp%2F%2B8hsV0KAO5AvLAJQ6GnCUdUlfSz8%2B95TxECQwgc8NaHC90qn5cejpq7Alv90%2F5r%2Fl7OrjJoQcK%2BPSEk%2FT6vQUTwE%2FvZr0Yoq2WBUpe5dxd4QC5gbuxtdi%2BFCpIecGRsXh2aDh2dWx%2FLZetIb5RzFg0KE3MZkHkXnYDV2DOF%2FZmfZ86l%2FplaKKAwio2JbTI11ycNK4XjHsEmO02ZCri%2BEW%2F0u3iEOFZ0bnhmb6f3j6RpOGrS2oDJ1F2%2Bae49OhabJgujH1HFI4NtFH6sp%2FFw7%2F8N2U9C3SSNa1t9kZH38%2F0GmAxLBatum3tF2u5RFE3EpNBbcxm2Gslv3Ew7toBM5bhSaxgkXMd7KmZfM1QswOU8LxRjCJc3fqtYlpbHbgcLHsSGn7FzjcjNvLqeosYwAnY2%2Bw1ST%2Blxpy5JdNeqCKVLmHTFaF0cdu3edICvhvJCFLOwZqv8%2F5%2BDWn2vGskwX8KyTQikT1yjimzHDlNn6mYIB5RNsUeG5X%2BIX8KWBGD8y9Y2y7xoaT2kkn2R8kVVuL4hTZN31PWFoSfxk9snIRvxQIxQROLCWqwIcOEjDfio29BjqkAX8xFMrjp21MVShJ74Ww4wTxuz6ViOCFxympAhBW0wcYowptXfBbpVcigpsQ4wK1YQcdMo2nYchkAqCbyJUlD4qqc9yCXnl0TIGEIszn1Rimkd2d39H6%2F0w2Hj%2FyVLAN9YAgNAkkSJSY%2FlxfpzcNrhLj2Jlp4c3hkXSUemWeRSaF57SjAbJNVbUfL4m7at2JiQRIoubLGMw1XmRKNNi3kWVLhej5&X-Amz-Signature=c930f0ce6bf61dcc6f3d14075764921b7bcb391ac8dea29a03cdc1006a08f88f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BGYRENA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD5NzhaTL8vu1n6v8h4i7PAX%2F9lkKZ2%2B%2BsWMTeaF5RhMAIhAJznCvNhecniuDoPGhc3Sro2EB68cuELU8UaO8i2Ke61Kv8DCEQQABoMNjM3NDIzMTgzODA1IgxLjxbdTHGpIpqhxcEq3AOVd7C4fv6TxI6VmVxasxfTIfnYDSdfMjoWOPa6oD0ngDOD8Bs%2BUxdEJI2yS3MzAp%2F%2B8hsV0KAO5AvLAJQ6GnCUdUlfSz8%2B95TxECQwgc8NaHC90qn5cejpq7Alv90%2F5r%2Fl7OrjJoQcK%2BPSEk%2FT6vQUTwE%2FvZr0Yoq2WBUpe5dxd4QC5gbuxtdi%2BFCpIecGRsXh2aDh2dWx%2FLZetIb5RzFg0KE3MZkHkXnYDV2DOF%2FZmfZ86l%2FplaKKAwio2JbTI11ycNK4XjHsEmO02ZCri%2BEW%2F0u3iEOFZ0bnhmb6f3j6RpOGrS2oDJ1F2%2Bae49OhabJgujH1HFI4NtFH6sp%2FFw7%2F8N2U9C3SSNa1t9kZH38%2F0GmAxLBatum3tF2u5RFE3EpNBbcxm2Gslv3Ew7toBM5bhSaxgkXMd7KmZfM1QswOU8LxRjCJc3fqtYlpbHbgcLHsSGn7FzjcjNvLqeosYwAnY2%2Bw1ST%2Blxpy5JdNeqCKVLmHTFaF0cdu3edICvhvJCFLOwZqv8%2F5%2BDWn2vGskwX8KyTQikT1yjimzHDlNn6mYIB5RNsUeG5X%2BIX8KWBGD8y9Y2y7xoaT2kkn2R8kVVuL4hTZN31PWFoSfxk9snIRvxQIxQROLCWqwIcOEjDfio29BjqkAX8xFMrjp21MVShJ74Ww4wTxuz6ViOCFxympAhBW0wcYowptXfBbpVcigpsQ4wK1YQcdMo2nYchkAqCbyJUlD4qqc9yCXnl0TIGEIszn1Rimkd2d39H6%2F0w2Hj%2FyVLAN9YAgNAkkSJSY%2FlxfpzcNrhLj2Jlp4c3hkXSUemWeRSaF57SjAbJNVbUfL4m7at2JiQRIoubLGMw1XmRKNNi3kWVLhej5&X-Amz-Signature=34fbf5e63ebf85c2a991a1aff427725041f0e6c686472eb86389826b39de4533&X-Amz-SignedHeaders=host&x-id=GetObject)

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
