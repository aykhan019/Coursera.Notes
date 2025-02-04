

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FXYKRR2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIEbuGNbUxBUBGPlevMYGZCnPtKz4NYoCs%2FVPmgElBxXiAiEAlD4aRtHm3LMmtl88ui%2FQu03nP1NqlszuZ3ZBIPN8ZuAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDD%2FTYFTRq9oisbqXEircA%2F6HiKGO7Luxl1Tyz7z1yNe762yZ05RHYt1o3jf6dewqOzfmKnQAVJPxPrBUgoUgykyihDSNAYp4AVXNp8wGnNXzm1tX4k%2F%2BAHX5QynZHwu4Nib01SY3UieTbFFFBBI%2F0yg56JaJs2ZBhoLsCShYTuCupX56t4OLp19IYIVn9No2jEt%2Bdh%2FJfcmpTPs2e%2BpMF%2FXANqzeXg0jsHqsUiqfWz11qApZMG8NwDP1ko9VdiPGa9X%2FCG9mJkPz%2BR6%2FkavgkQWqwyXpRU%2FERk3zQWmdorZzKOCwei5JIw6aHGiLP47xr2e9WZFbX6zlPRXAyNWjdYv%2FD1i2Z%2FTy0WnE%2B%2FQHYNcEc8bWLALSSQ2uwTIkVO0N36U7pIn1yCQqKpQJHVW459Vkrde5JWmsjddKMk0lDIHeGODs1tPjFn65hPgdquSQhImzc%2FBOwdaITXrYHxwKoggrlxQ9iO9K1NR4ZVlfkox2Pplkh97kzbQoewmIbyP9HXKeq73KIc1I05Ai0FcbyHGVaA2jctCYRlpPOglwVYGdxqzWznWGNKibzbmDdxkYw6PpnJn89Oeo5fPUODy3RQ1wwVoSG7qS6DxhGa8XNq0jAzD3kgL75lY6P9sYB7Y5WSt6b3BslxMIbHGKMMW%2Bhr0GOqUBinM0zxcArws82%2Bslql66LNOT3dx%2BEHph2EjZPXGZwOJ2AdPVQ0wt%2B40bK5ShP6G15adsjF9BXLTHXILHMRr3p7hd0duFVEuyo61MjZaB0o5jroWQSza7uXprHqTfDEsF1Bf7aLbGIrKG1%2FAb%2FqWRptab3b50BH4BPd%2BFO7Oct%2FshXNmCdpm1bwLDVtlCT9oBj%2BbJ2INEqJoBOItVfoBJwvl7x8KD&X-Amz-Signature=04bb39f5f59d55b6dc2f5dfc752fdb65f726471a754b7b53f069d407625aa54c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FXYKRR2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIEbuGNbUxBUBGPlevMYGZCnPtKz4NYoCs%2FVPmgElBxXiAiEAlD4aRtHm3LMmtl88ui%2FQu03nP1NqlszuZ3ZBIPN8ZuAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDD%2FTYFTRq9oisbqXEircA%2F6HiKGO7Luxl1Tyz7z1yNe762yZ05RHYt1o3jf6dewqOzfmKnQAVJPxPrBUgoUgykyihDSNAYp4AVXNp8wGnNXzm1tX4k%2F%2BAHX5QynZHwu4Nib01SY3UieTbFFFBBI%2F0yg56JaJs2ZBhoLsCShYTuCupX56t4OLp19IYIVn9No2jEt%2Bdh%2FJfcmpTPs2e%2BpMF%2FXANqzeXg0jsHqsUiqfWz11qApZMG8NwDP1ko9VdiPGa9X%2FCG9mJkPz%2BR6%2FkavgkQWqwyXpRU%2FERk3zQWmdorZzKOCwei5JIw6aHGiLP47xr2e9WZFbX6zlPRXAyNWjdYv%2FD1i2Z%2FTy0WnE%2B%2FQHYNcEc8bWLALSSQ2uwTIkVO0N36U7pIn1yCQqKpQJHVW459Vkrde5JWmsjddKMk0lDIHeGODs1tPjFn65hPgdquSQhImzc%2FBOwdaITXrYHxwKoggrlxQ9iO9K1NR4ZVlfkox2Pplkh97kzbQoewmIbyP9HXKeq73KIc1I05Ai0FcbyHGVaA2jctCYRlpPOglwVYGdxqzWznWGNKibzbmDdxkYw6PpnJn89Oeo5fPUODy3RQ1wwVoSG7qS6DxhGa8XNq0jAzD3kgL75lY6P9sYB7Y5WSt6b3BslxMIbHGKMMW%2Bhr0GOqUBinM0zxcArws82%2Bslql66LNOT3dx%2BEHph2EjZPXGZwOJ2AdPVQ0wt%2B40bK5ShP6G15adsjF9BXLTHXILHMRr3p7hd0duFVEuyo61MjZaB0o5jroWQSza7uXprHqTfDEsF1Bf7aLbGIrKG1%2FAb%2FqWRptab3b50BH4BPd%2BFO7Oct%2FshXNmCdpm1bwLDVtlCT9oBj%2BbJ2INEqJoBOItVfoBJwvl7x8KD&X-Amz-Signature=8598da856afebea585168d48cbebd60c11422c884d05db2d956342f8bdfca4b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FXYKRR2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIEbuGNbUxBUBGPlevMYGZCnPtKz4NYoCs%2FVPmgElBxXiAiEAlD4aRtHm3LMmtl88ui%2FQu03nP1NqlszuZ3ZBIPN8ZuAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDD%2FTYFTRq9oisbqXEircA%2F6HiKGO7Luxl1Tyz7z1yNe762yZ05RHYt1o3jf6dewqOzfmKnQAVJPxPrBUgoUgykyihDSNAYp4AVXNp8wGnNXzm1tX4k%2F%2BAHX5QynZHwu4Nib01SY3UieTbFFFBBI%2F0yg56JaJs2ZBhoLsCShYTuCupX56t4OLp19IYIVn9No2jEt%2Bdh%2FJfcmpTPs2e%2BpMF%2FXANqzeXg0jsHqsUiqfWz11qApZMG8NwDP1ko9VdiPGa9X%2FCG9mJkPz%2BR6%2FkavgkQWqwyXpRU%2FERk3zQWmdorZzKOCwei5JIw6aHGiLP47xr2e9WZFbX6zlPRXAyNWjdYv%2FD1i2Z%2FTy0WnE%2B%2FQHYNcEc8bWLALSSQ2uwTIkVO0N36U7pIn1yCQqKpQJHVW459Vkrde5JWmsjddKMk0lDIHeGODs1tPjFn65hPgdquSQhImzc%2FBOwdaITXrYHxwKoggrlxQ9iO9K1NR4ZVlfkox2Pplkh97kzbQoewmIbyP9HXKeq73KIc1I05Ai0FcbyHGVaA2jctCYRlpPOglwVYGdxqzWznWGNKibzbmDdxkYw6PpnJn89Oeo5fPUODy3RQ1wwVoSG7qS6DxhGa8XNq0jAzD3kgL75lY6P9sYB7Y5WSt6b3BslxMIbHGKMMW%2Bhr0GOqUBinM0zxcArws82%2Bslql66LNOT3dx%2BEHph2EjZPXGZwOJ2AdPVQ0wt%2B40bK5ShP6G15adsjF9BXLTHXILHMRr3p7hd0duFVEuyo61MjZaB0o5jroWQSza7uXprHqTfDEsF1Bf7aLbGIrKG1%2FAb%2FqWRptab3b50BH4BPd%2BFO7Oct%2FshXNmCdpm1bwLDVtlCT9oBj%2BbJ2INEqJoBOItVfoBJwvl7x8KD&X-Amz-Signature=dd84f10488b2344a165f10cbea0b6a9463c49e2396ad2121a6937f4aab6682e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF4S45QD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIFOtIz9OHNX34BHOTGoqrYXhK5yZGPfTj5erQFKPmyDqAiEAw%2BOxP3kE0tXeZqV7wawf6wtP6AOvlcKGhiYrKQsTnW8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHjuSn4Ayv%2FZf8ebxyrcA5XzSwjzcxPcwrKp%2FpWxpxLH9zJvnh8zesRZu5VNhCnKgzaVsaMKh3qJZL0epzm4FNOxaJRK%2BrdgCz7Ya7CSmhxlDmIKXc6VLdS3QV6vX9L4oXwkyvUWexHz4BvBJ3Ilc%2F9rL5ogBbPr3zywt8sERn32veoPaIObcpLm9242yfFtguOQm%2F7DzwLma%2Bi0kIQOHjXjGOZ2H3fH%2BNMDGx%2FXoMoBINfMZpv8r32QFoXguBQMNIQPfcdqgKw26pbe%2BTNSNy7vs%2B3Sqz5dQ5SBH9FKJjRiG9qi%2BO4gvzMVnoaPlO4cFJvEa%2FQe6O0sTSx4HEOqf%2B6i60zRSMqI5%2BtxTuW2Pzv21aIBXRa9hsADsbs%2FQa9fEr8C8LyN%2BkvncRt8KZR9Dn9I5sHSfjWaYTALZbt9HjLlwo4UC7AWstvtVj%2FsOyCBh04Cohm4kOw6t6oE5KcA4conB3n%2BfYyzID0VrWm0LLwbwKhASIciT8fy6F0jSm%2F%2BjkjQWCy%2BvgY6u3Kos%2FXLM9NBNqN0BIR6C3rxgsFhtpabt1LCgCwThERS3mSD0I0%2BLhXC0v5tsMoPPjyVA1EZGugLfsmRTlyeZJZSQig6ZPuH65fvOKucMI0WGy6d%2BB5Wcywpy1ptfAajgT5IML6%2Bhr0GOqUBioqVsHJn%2B5iNk9rJc5HvaBWSe2lYtCeFx9iBAciU4zB2bqILVLzyPQQ9nqTHK7TZXyjGArWGbrwA8qepb1T%2BJxQte2rBZmM7HGFpdDpdDWWHvEO7bqeuk2atjXmWHkyxtouEgj4xFv5AWbAdDfyerqlyQrTlZ%2BKcEjLmsqLaQCTAKbX3cjM%2FpQjunXW%2FJQFsakHAIJgWkkoTBOtaa5MKLWAdK%2BCA&X-Amz-Signature=a3a0df273f55af0ad9f0db4766107074ceeba5de58d1f9a5a5ebbb21d4bb10e6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF4S45QD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIFOtIz9OHNX34BHOTGoqrYXhK5yZGPfTj5erQFKPmyDqAiEAw%2BOxP3kE0tXeZqV7wawf6wtP6AOvlcKGhiYrKQsTnW8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHjuSn4Ayv%2FZf8ebxyrcA5XzSwjzcxPcwrKp%2FpWxpxLH9zJvnh8zesRZu5VNhCnKgzaVsaMKh3qJZL0epzm4FNOxaJRK%2BrdgCz7Ya7CSmhxlDmIKXc6VLdS3QV6vX9L4oXwkyvUWexHz4BvBJ3Ilc%2F9rL5ogBbPr3zywt8sERn32veoPaIObcpLm9242yfFtguOQm%2F7DzwLma%2Bi0kIQOHjXjGOZ2H3fH%2BNMDGx%2FXoMoBINfMZpv8r32QFoXguBQMNIQPfcdqgKw26pbe%2BTNSNy7vs%2B3Sqz5dQ5SBH9FKJjRiG9qi%2BO4gvzMVnoaPlO4cFJvEa%2FQe6O0sTSx4HEOqf%2B6i60zRSMqI5%2BtxTuW2Pzv21aIBXRa9hsADsbs%2FQa9fEr8C8LyN%2BkvncRt8KZR9Dn9I5sHSfjWaYTALZbt9HjLlwo4UC7AWstvtVj%2FsOyCBh04Cohm4kOw6t6oE5KcA4conB3n%2BfYyzID0VrWm0LLwbwKhASIciT8fy6F0jSm%2F%2BjkjQWCy%2BvgY6u3Kos%2FXLM9NBNqN0BIR6C3rxgsFhtpabt1LCgCwThERS3mSD0I0%2BLhXC0v5tsMoPPjyVA1EZGugLfsmRTlyeZJZSQig6ZPuH65fvOKucMI0WGy6d%2BB5Wcywpy1ptfAajgT5IML6%2Bhr0GOqUBioqVsHJn%2B5iNk9rJc5HvaBWSe2lYtCeFx9iBAciU4zB2bqILVLzyPQQ9nqTHK7TZXyjGArWGbrwA8qepb1T%2BJxQte2rBZmM7HGFpdDpdDWWHvEO7bqeuk2atjXmWHkyxtouEgj4xFv5AWbAdDfyerqlyQrTlZ%2BKcEjLmsqLaQCTAKbX3cjM%2FpQjunXW%2FJQFsakHAIJgWkkoTBOtaa5MKLWAdK%2BCA&X-Amz-Signature=4f7fd31c781e5cfcd9137bfd56d63c299995220974b374d80f52608b4b3ff583&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF4S45QD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIFOtIz9OHNX34BHOTGoqrYXhK5yZGPfTj5erQFKPmyDqAiEAw%2BOxP3kE0tXeZqV7wawf6wtP6AOvlcKGhiYrKQsTnW8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHjuSn4Ayv%2FZf8ebxyrcA5XzSwjzcxPcwrKp%2FpWxpxLH9zJvnh8zesRZu5VNhCnKgzaVsaMKh3qJZL0epzm4FNOxaJRK%2BrdgCz7Ya7CSmhxlDmIKXc6VLdS3QV6vX9L4oXwkyvUWexHz4BvBJ3Ilc%2F9rL5ogBbPr3zywt8sERn32veoPaIObcpLm9242yfFtguOQm%2F7DzwLma%2Bi0kIQOHjXjGOZ2H3fH%2BNMDGx%2FXoMoBINfMZpv8r32QFoXguBQMNIQPfcdqgKw26pbe%2BTNSNy7vs%2B3Sqz5dQ5SBH9FKJjRiG9qi%2BO4gvzMVnoaPlO4cFJvEa%2FQe6O0sTSx4HEOqf%2B6i60zRSMqI5%2BtxTuW2Pzv21aIBXRa9hsADsbs%2FQa9fEr8C8LyN%2BkvncRt8KZR9Dn9I5sHSfjWaYTALZbt9HjLlwo4UC7AWstvtVj%2FsOyCBh04Cohm4kOw6t6oE5KcA4conB3n%2BfYyzID0VrWm0LLwbwKhASIciT8fy6F0jSm%2F%2BjkjQWCy%2BvgY6u3Kos%2FXLM9NBNqN0BIR6C3rxgsFhtpabt1LCgCwThERS3mSD0I0%2BLhXC0v5tsMoPPjyVA1EZGugLfsmRTlyeZJZSQig6ZPuH65fvOKucMI0WGy6d%2BB5Wcywpy1ptfAajgT5IML6%2Bhr0GOqUBioqVsHJn%2B5iNk9rJc5HvaBWSe2lYtCeFx9iBAciU4zB2bqILVLzyPQQ9nqTHK7TZXyjGArWGbrwA8qepb1T%2BJxQte2rBZmM7HGFpdDpdDWWHvEO7bqeuk2atjXmWHkyxtouEgj4xFv5AWbAdDfyerqlyQrTlZ%2BKcEjLmsqLaQCTAKbX3cjM%2FpQjunXW%2FJQFsakHAIJgWkkoTBOtaa5MKLWAdK%2BCA&X-Amz-Signature=d2c1b3499de332176877023429e0e01ba86964fd2cf82e7b3ed20f033e9f68d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF4S45QD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIFOtIz9OHNX34BHOTGoqrYXhK5yZGPfTj5erQFKPmyDqAiEAw%2BOxP3kE0tXeZqV7wawf6wtP6AOvlcKGhiYrKQsTnW8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHjuSn4Ayv%2FZf8ebxyrcA5XzSwjzcxPcwrKp%2FpWxpxLH9zJvnh8zesRZu5VNhCnKgzaVsaMKh3qJZL0epzm4FNOxaJRK%2BrdgCz7Ya7CSmhxlDmIKXc6VLdS3QV6vX9L4oXwkyvUWexHz4BvBJ3Ilc%2F9rL5ogBbPr3zywt8sERn32veoPaIObcpLm9242yfFtguOQm%2F7DzwLma%2Bi0kIQOHjXjGOZ2H3fH%2BNMDGx%2FXoMoBINfMZpv8r32QFoXguBQMNIQPfcdqgKw26pbe%2BTNSNy7vs%2B3Sqz5dQ5SBH9FKJjRiG9qi%2BO4gvzMVnoaPlO4cFJvEa%2FQe6O0sTSx4HEOqf%2B6i60zRSMqI5%2BtxTuW2Pzv21aIBXRa9hsADsbs%2FQa9fEr8C8LyN%2BkvncRt8KZR9Dn9I5sHSfjWaYTALZbt9HjLlwo4UC7AWstvtVj%2FsOyCBh04Cohm4kOw6t6oE5KcA4conB3n%2BfYyzID0VrWm0LLwbwKhASIciT8fy6F0jSm%2F%2BjkjQWCy%2BvgY6u3Kos%2FXLM9NBNqN0BIR6C3rxgsFhtpabt1LCgCwThERS3mSD0I0%2BLhXC0v5tsMoPPjyVA1EZGugLfsmRTlyeZJZSQig6ZPuH65fvOKucMI0WGy6d%2BB5Wcywpy1ptfAajgT5IML6%2Bhr0GOqUBioqVsHJn%2B5iNk9rJc5HvaBWSe2lYtCeFx9iBAciU4zB2bqILVLzyPQQ9nqTHK7TZXyjGArWGbrwA8qepb1T%2BJxQte2rBZmM7HGFpdDpdDWWHvEO7bqeuk2atjXmWHkyxtouEgj4xFv5AWbAdDfyerqlyQrTlZ%2BKcEjLmsqLaQCTAKbX3cjM%2FpQjunXW%2FJQFsakHAIJgWkkoTBOtaa5MKLWAdK%2BCA&X-Amz-Signature=5856f3609a285e8b324c3f3ebcbe7877b5b1f64bc52c88b38eab80dd37c390e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF4S45QD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIFOtIz9OHNX34BHOTGoqrYXhK5yZGPfTj5erQFKPmyDqAiEAw%2BOxP3kE0tXeZqV7wawf6wtP6AOvlcKGhiYrKQsTnW8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHjuSn4Ayv%2FZf8ebxyrcA5XzSwjzcxPcwrKp%2FpWxpxLH9zJvnh8zesRZu5VNhCnKgzaVsaMKh3qJZL0epzm4FNOxaJRK%2BrdgCz7Ya7CSmhxlDmIKXc6VLdS3QV6vX9L4oXwkyvUWexHz4BvBJ3Ilc%2F9rL5ogBbPr3zywt8sERn32veoPaIObcpLm9242yfFtguOQm%2F7DzwLma%2Bi0kIQOHjXjGOZ2H3fH%2BNMDGx%2FXoMoBINfMZpv8r32QFoXguBQMNIQPfcdqgKw26pbe%2BTNSNy7vs%2B3Sqz5dQ5SBH9FKJjRiG9qi%2BO4gvzMVnoaPlO4cFJvEa%2FQe6O0sTSx4HEOqf%2B6i60zRSMqI5%2BtxTuW2Pzv21aIBXRa9hsADsbs%2FQa9fEr8C8LyN%2BkvncRt8KZR9Dn9I5sHSfjWaYTALZbt9HjLlwo4UC7AWstvtVj%2FsOyCBh04Cohm4kOw6t6oE5KcA4conB3n%2BfYyzID0VrWm0LLwbwKhASIciT8fy6F0jSm%2F%2BjkjQWCy%2BvgY6u3Kos%2FXLM9NBNqN0BIR6C3rxgsFhtpabt1LCgCwThERS3mSD0I0%2BLhXC0v5tsMoPPjyVA1EZGugLfsmRTlyeZJZSQig6ZPuH65fvOKucMI0WGy6d%2BB5Wcywpy1ptfAajgT5IML6%2Bhr0GOqUBioqVsHJn%2B5iNk9rJc5HvaBWSe2lYtCeFx9iBAciU4zB2bqILVLzyPQQ9nqTHK7TZXyjGArWGbrwA8qepb1T%2BJxQte2rBZmM7HGFpdDpdDWWHvEO7bqeuk2atjXmWHkyxtouEgj4xFv5AWbAdDfyerqlyQrTlZ%2BKcEjLmsqLaQCTAKbX3cjM%2FpQjunXW%2FJQFsakHAIJgWkkoTBOtaa5MKLWAdK%2BCA&X-Amz-Signature=6c1305beeb45545b5102ed4b6a2d40425066794a7ebc794dbd46281bfc3ec4e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF4S45QD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIFOtIz9OHNX34BHOTGoqrYXhK5yZGPfTj5erQFKPmyDqAiEAw%2BOxP3kE0tXeZqV7wawf6wtP6AOvlcKGhiYrKQsTnW8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHjuSn4Ayv%2FZf8ebxyrcA5XzSwjzcxPcwrKp%2FpWxpxLH9zJvnh8zesRZu5VNhCnKgzaVsaMKh3qJZL0epzm4FNOxaJRK%2BrdgCz7Ya7CSmhxlDmIKXc6VLdS3QV6vX9L4oXwkyvUWexHz4BvBJ3Ilc%2F9rL5ogBbPr3zywt8sERn32veoPaIObcpLm9242yfFtguOQm%2F7DzwLma%2Bi0kIQOHjXjGOZ2H3fH%2BNMDGx%2FXoMoBINfMZpv8r32QFoXguBQMNIQPfcdqgKw26pbe%2BTNSNy7vs%2B3Sqz5dQ5SBH9FKJjRiG9qi%2BO4gvzMVnoaPlO4cFJvEa%2FQe6O0sTSx4HEOqf%2B6i60zRSMqI5%2BtxTuW2Pzv21aIBXRa9hsADsbs%2FQa9fEr8C8LyN%2BkvncRt8KZR9Dn9I5sHSfjWaYTALZbt9HjLlwo4UC7AWstvtVj%2FsOyCBh04Cohm4kOw6t6oE5KcA4conB3n%2BfYyzID0VrWm0LLwbwKhASIciT8fy6F0jSm%2F%2BjkjQWCy%2BvgY6u3Kos%2FXLM9NBNqN0BIR6C3rxgsFhtpabt1LCgCwThERS3mSD0I0%2BLhXC0v5tsMoPPjyVA1EZGugLfsmRTlyeZJZSQig6ZPuH65fvOKucMI0WGy6d%2BB5Wcywpy1ptfAajgT5IML6%2Bhr0GOqUBioqVsHJn%2B5iNk9rJc5HvaBWSe2lYtCeFx9iBAciU4zB2bqILVLzyPQQ9nqTHK7TZXyjGArWGbrwA8qepb1T%2BJxQte2rBZmM7HGFpdDpdDWWHvEO7bqeuk2atjXmWHkyxtouEgj4xFv5AWbAdDfyerqlyQrTlZ%2BKcEjLmsqLaQCTAKbX3cjM%2FpQjunXW%2FJQFsakHAIJgWkkoTBOtaa5MKLWAdK%2BCA&X-Amz-Signature=382c3d6adb584ee3d9b76a1b0452c422817284a69ac7f1cd494a1692bcab90b0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTVPXADI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCq9ZFgzFmm5%2BCBqbqEQbvveJyEWuX8D%2FeyYRfFzyn89wIhANu04vyoAw%2FfRLyG9hKXpSY1vsHuu26LyCC6fPDFSpREKv8DCCYQABoMNjM3NDIzMTgzODA1IgzZ%2F1FHln1ZF6IdpvMq3ANUhqdY6JDCh5X2CzgNwyIunUjW%2FvSeg3L4PXVwe3cL4Hw%2FA8HhOAPONoj7bcMjocMaeIB5H3sRGs4HOYBXilHbIlV6TG3dM%2BTfxhxdB3fIt3GCF9x6iH5qE9i5ZMpiAd8QVV%2BTGRSw3DgHTrN5OpnFw0XpNEUioS4JCQoy1YlRWaf4pEmGkBo6Fa1pWBNnIyCjsP52oSQSd7%2FsNTtYyZW%2FuXLlXr%2BnVH6n8bJmu76cjif86Er%2BDFI2PZt8y3rkvt0kWEqfpgcuU6LOKTaGhT%2F6KkWLYrDpJtzw351uan%2Ffb0kw0MR9BUtDcYqVOTKejBZdu3c25uvsU6aM5yMYF9c%2BN8ZhgkcklaSLIVSOBrh82F4GXmP8HnqGNvEKbJdESgSx9%2BDkmuhoBQ3D2CuaQfxsKhuRJSxM03DsOABXJu%2B4k9GEd%2BumRSy%2BpPUdRfQ90wOjTFRJgzSffKLMMjrlx0fqVx%2FmtKgfRd4H%2F5ckzCMMB94mp%2F1qwUL5SVdQHzhVCPW4WxVdcFjAzutPPZLnGnsN0njL3q5Up8GZJY9Oem3cTY4dKQVMFj9UgNuchiHXDP0ezBEEyPTOIEYutjoSyCHIDgUVjthI2tcr9xy%2F4r3LqW6Lf6YbKEPCk0KLGDDbvoa9BjqkAaNlL%2FzrBnA0HZWik0U39B8YZIoIC0w8VUFzwNqUaOlN1UI0xcGufmif%2BYN8imVzznu%2B%2Fg4HqWv7MuTmWUtBEKOo12BFxz9169OiD5aIlmD%2BVn2HjfF45GF1kjcmn0CMSSolAvz%2Fx8gQItTmrq2DILAHvzSB8olmtSKxEtSPQTirrdbE6pDeHwWFCVkY%2BWPYirnD1J6rFvgO3BTVV2tWed9UVA5e&X-Amz-Signature=fad0d7e81e03bdd2ff6c8691b6f4a357fda82dab4c73d683605436873ea17b6b&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BUUXBOE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIFFsCuJaUDxyGR9vWmYvGImnQrR9RRZDhnCXLm9qQZZPAiBEgNRBSYI7bY4062zL8gMDugC6VnymKYSwMt9AYdJE%2Fyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMvjqVuHjFaXiPjFpwKtwD2Or6H%2FlSffeA2R7dd4IkL2svDTiJDNbfjvqzCMGUJKvnpeTyDPhKl6hKyOZt%2FtD7%2FeJWjfrPzd75qyGiPn5z6BzxJ6eaybhimu9HV15BrjdLK9OzLUOoNmC5no%2Bd2KV8ZbA9DSFKbQfmB1BYrYQErMKGLuBzDESsiJMDK7TakiEQG6w2vPmInzEI92avn2LBcqx027mNUkB1JDKk98SFMbnUHYWpdOzEYDqU3HgCqiubWVqr6648ej5qjTzrdzq9aFVk0bfyjt%2BzbozPFS5GqxjDPhc4rUGTJ5OF58Iv%2BsoF3n32gJEurjmaeuVg%2BpYyGG%2BNLOqc9rGDmI9JuM8tjg6eUIah0KnByMP3E4zsMbIRNCOdEXSTCW72F6JayijEcGZfdnjtD6Ov1ZN7SrsdEae28k8Ycz83xYpKlaBrUdMk64FR4JsCDG%2Fd4y95zUbf1qKSwvrfcEDx%2FYkWK0SnkPJJigauoo3mMeqXGx6AaEcIRlZxN05g8gVYv7%2F9UpmJY55wtVJq3ICUr2xLn4BJO9tmrR%2FV7%2FNtSuaDHVrBFD049eOtJ1Y0mi5bgTl37FxU%2BMxtOR80SYYKMLht%2FHKXHck9LovqWubNXaExZa27o4OqFSS5R4O2mS7Z%2FXEwt7%2BGvQY6pgHdAitBNVKT9ZVRO8mLFSsagG6kuRB8hBURKhbFj0zPEJ%2FWwfQJK5OtmNy8lD3CITA954APedskh7YgquiUcEbu1EaSZgWs4kzZ5HsJHhfJWUNPwWs9iXr9apok%2FEWbnXxHUbYoK7ozi84we7GMhnig%2BxSz6TP5pygpM9fJ4i1J9OFZCJ1mKI%2BVKRonjVHXW%2BVCYQtHolvvUzGvLJRiUr5%2B6Y1Ilon8&X-Amz-Signature=622c244e532807620e076bf33f4b873e520fda66b86f3de05a7aea7718f0cdf8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF4S45QD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIFOtIz9OHNX34BHOTGoqrYXhK5yZGPfTj5erQFKPmyDqAiEAw%2BOxP3kE0tXeZqV7wawf6wtP6AOvlcKGhiYrKQsTnW8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHjuSn4Ayv%2FZf8ebxyrcA5XzSwjzcxPcwrKp%2FpWxpxLH9zJvnh8zesRZu5VNhCnKgzaVsaMKh3qJZL0epzm4FNOxaJRK%2BrdgCz7Ya7CSmhxlDmIKXc6VLdS3QV6vX9L4oXwkyvUWexHz4BvBJ3Ilc%2F9rL5ogBbPr3zywt8sERn32veoPaIObcpLm9242yfFtguOQm%2F7DzwLma%2Bi0kIQOHjXjGOZ2H3fH%2BNMDGx%2FXoMoBINfMZpv8r32QFoXguBQMNIQPfcdqgKw26pbe%2BTNSNy7vs%2B3Sqz5dQ5SBH9FKJjRiG9qi%2BO4gvzMVnoaPlO4cFJvEa%2FQe6O0sTSx4HEOqf%2B6i60zRSMqI5%2BtxTuW2Pzv21aIBXRa9hsADsbs%2FQa9fEr8C8LyN%2BkvncRt8KZR9Dn9I5sHSfjWaYTALZbt9HjLlwo4UC7AWstvtVj%2FsOyCBh04Cohm4kOw6t6oE5KcA4conB3n%2BfYyzID0VrWm0LLwbwKhASIciT8fy6F0jSm%2F%2BjkjQWCy%2BvgY6u3Kos%2FXLM9NBNqN0BIR6C3rxgsFhtpabt1LCgCwThERS3mSD0I0%2BLhXC0v5tsMoPPjyVA1EZGugLfsmRTlyeZJZSQig6ZPuH65fvOKucMI0WGy6d%2BB5Wcywpy1ptfAajgT5IML6%2Bhr0GOqUBioqVsHJn%2B5iNk9rJc5HvaBWSe2lYtCeFx9iBAciU4zB2bqILVLzyPQQ9nqTHK7TZXyjGArWGbrwA8qepb1T%2BJxQte2rBZmM7HGFpdDpdDWWHvEO7bqeuk2atjXmWHkyxtouEgj4xFv5AWbAdDfyerqlyQrTlZ%2BKcEjLmsqLaQCTAKbX3cjM%2FpQjunXW%2FJQFsakHAIJgWkkoTBOtaa5MKLWAdK%2BCA&X-Amz-Signature=7c2ad63bfc9f5af2f4bde85afbba4d797cc363129f5f9ff84ce05932e616ef78&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF4S45QD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIFOtIz9OHNX34BHOTGoqrYXhK5yZGPfTj5erQFKPmyDqAiEAw%2BOxP3kE0tXeZqV7wawf6wtP6AOvlcKGhiYrKQsTnW8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHjuSn4Ayv%2FZf8ebxyrcA5XzSwjzcxPcwrKp%2FpWxpxLH9zJvnh8zesRZu5VNhCnKgzaVsaMKh3qJZL0epzm4FNOxaJRK%2BrdgCz7Ya7CSmhxlDmIKXc6VLdS3QV6vX9L4oXwkyvUWexHz4BvBJ3Ilc%2F9rL5ogBbPr3zywt8sERn32veoPaIObcpLm9242yfFtguOQm%2F7DzwLma%2Bi0kIQOHjXjGOZ2H3fH%2BNMDGx%2FXoMoBINfMZpv8r32QFoXguBQMNIQPfcdqgKw26pbe%2BTNSNy7vs%2B3Sqz5dQ5SBH9FKJjRiG9qi%2BO4gvzMVnoaPlO4cFJvEa%2FQe6O0sTSx4HEOqf%2B6i60zRSMqI5%2BtxTuW2Pzv21aIBXRa9hsADsbs%2FQa9fEr8C8LyN%2BkvncRt8KZR9Dn9I5sHSfjWaYTALZbt9HjLlwo4UC7AWstvtVj%2FsOyCBh04Cohm4kOw6t6oE5KcA4conB3n%2BfYyzID0VrWm0LLwbwKhASIciT8fy6F0jSm%2F%2BjkjQWCy%2BvgY6u3Kos%2FXLM9NBNqN0BIR6C3rxgsFhtpabt1LCgCwThERS3mSD0I0%2BLhXC0v5tsMoPPjyVA1EZGugLfsmRTlyeZJZSQig6ZPuH65fvOKucMI0WGy6d%2BB5Wcywpy1ptfAajgT5IML6%2Bhr0GOqUBioqVsHJn%2B5iNk9rJc5HvaBWSe2lYtCeFx9iBAciU4zB2bqILVLzyPQQ9nqTHK7TZXyjGArWGbrwA8qepb1T%2BJxQte2rBZmM7HGFpdDpdDWWHvEO7bqeuk2atjXmWHkyxtouEgj4xFv5AWbAdDfyerqlyQrTlZ%2BKcEjLmsqLaQCTAKbX3cjM%2FpQjunXW%2FJQFsakHAIJgWkkoTBOtaa5MKLWAdK%2BCA&X-Amz-Signature=a9787a2d86185983d634584adc20530c37c615b5f9cb5a21bf6206db0bcbe0b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF4S45QD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIFOtIz9OHNX34BHOTGoqrYXhK5yZGPfTj5erQFKPmyDqAiEAw%2BOxP3kE0tXeZqV7wawf6wtP6AOvlcKGhiYrKQsTnW8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHjuSn4Ayv%2FZf8ebxyrcA5XzSwjzcxPcwrKp%2FpWxpxLH9zJvnh8zesRZu5VNhCnKgzaVsaMKh3qJZL0epzm4FNOxaJRK%2BrdgCz7Ya7CSmhxlDmIKXc6VLdS3QV6vX9L4oXwkyvUWexHz4BvBJ3Ilc%2F9rL5ogBbPr3zywt8sERn32veoPaIObcpLm9242yfFtguOQm%2F7DzwLma%2Bi0kIQOHjXjGOZ2H3fH%2BNMDGx%2FXoMoBINfMZpv8r32QFoXguBQMNIQPfcdqgKw26pbe%2BTNSNy7vs%2B3Sqz5dQ5SBH9FKJjRiG9qi%2BO4gvzMVnoaPlO4cFJvEa%2FQe6O0sTSx4HEOqf%2B6i60zRSMqI5%2BtxTuW2Pzv21aIBXRa9hsADsbs%2FQa9fEr8C8LyN%2BkvncRt8KZR9Dn9I5sHSfjWaYTALZbt9HjLlwo4UC7AWstvtVj%2FsOyCBh04Cohm4kOw6t6oE5KcA4conB3n%2BfYyzID0VrWm0LLwbwKhASIciT8fy6F0jSm%2F%2BjkjQWCy%2BvgY6u3Kos%2FXLM9NBNqN0BIR6C3rxgsFhtpabt1LCgCwThERS3mSD0I0%2BLhXC0v5tsMoPPjyVA1EZGugLfsmRTlyeZJZSQig6ZPuH65fvOKucMI0WGy6d%2BB5Wcywpy1ptfAajgT5IML6%2Bhr0GOqUBioqVsHJn%2B5iNk9rJc5HvaBWSe2lYtCeFx9iBAciU4zB2bqILVLzyPQQ9nqTHK7TZXyjGArWGbrwA8qepb1T%2BJxQte2rBZmM7HGFpdDpdDWWHvEO7bqeuk2atjXmWHkyxtouEgj4xFv5AWbAdDfyerqlyQrTlZ%2BKcEjLmsqLaQCTAKbX3cjM%2FpQjunXW%2FJQFsakHAIJgWkkoTBOtaa5MKLWAdK%2BCA&X-Amz-Signature=849876d05081c2c499cb19660c4b20eecf262a1c87e741e410b9c52c5dd5bac7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YBBQ4Q4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDWItS1gr4EkttZdDdd%2F6M5GWrADwLdJyqxv2sLWl4rZAIhAKLfxeZrlYsPDqGM90EM3r3ypKrZ52kaE1R8Ikmo%2BEYUKv8DCCYQABoMNjM3NDIzMTgzODA1IgxbZPUoxnQEaLHbGdcq3AOHRnnAxGBtOtakV%2BZXVNyLXbJVGFzEAgzxBPffwvVajIb7bRLK907%2F5iK9RJyR0Dvp6c3nPDHwnDAYkjuXlood9BV4lwThazzhLcJ%2FqVdbJEUiRPrn4k7wjEsLuhLvjIfiwyFRbvyIZg9kgFbQYGvQbPK8suWIRLOYh3MsyuZXI3IL17txXEb9fzWOjLo1DF%2BKeoWO4Tz2L7%2BNJTj6Ig0Y67HoBw4pHUm%2BCqNhQ38RIjDxsmeO66ukMWDQyPDgiteyvO0y8HrIP4zvvQR9cPdgsXbeyRfdmzl3yyCeEj7kRCBhzFLbjPcEwjhj9%2B14dZdpBsOaaaT2KhpUgUxl4ErTyQuDbrmFM8eP16X7uldTBiyHKkwiU9k3t0XaxoxrdazRa4kLdYPyTz4JaxVtxyAEVM%2FRMqUNcpLeDIp05Dg4DvxI5oK06NjwhDUL0%2FJm09DAY40eMQq5Ab8Z%2BvRfYY2Iog4h6%2Bxfs%2FLmydzE64mS6onnXUnBmw0CEYZyc9dyN%2BXqY6bMaN32Vc%2Bgh%2BAinY8lCjSsJbdWy4evsjFWhN0YuilEKoTrgNEvt3gmJ4NW0w6TI4JngeWXHcm3hlPn8ZzyN2OOxutgZrkZwwKCgpG7sfkbyhgT9hMt6mF7NzC0voa9BjqkAXzRKbGbBjNf%2FMhfGhOVpDUqjhtJyUGfzrspbyKi7uV0ZL8nezua%2FvCn2EHvw7FRXTDrDo96OUd1FEFyj4%2BI8z6DFje6voVf3CVBBvvrxekn2atQZ0n8RghDCDOKCD35ptr72CdoKSjzZI%2Fan0HSNDYkSJRCCNGvqON6pvhhik9u3NwmdBLt%2FMsRg2wlPCN1riPmJDQnXjYfsFbyM%2FFQjWAdy4MK&X-Amz-Signature=f4aa4aa2798e0630b3bee084f19d37b76869e7f017ca4ff1a8062bbd7b3d3b83&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ULI7HI7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIFRRIfrTBOEO8yznqfUg6HWMJENTh5WW1GCS3%2FzNhVjAAiBpyZ0hdNKhcQAImmszEW6Ais%2BaxxjFpm%2BfGbEGXDjI6ir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMbV%2FU2MRg3mtFZCb1KtwD%2F%2FsVhDx1EWFzIrWTWY6yIksSrdcqZHfcKkNZBI2%2Fh%2B0r8uykn5fs7IUJ3CPY1LwGtm9ujy8Nc%2FTSGwCxFVaneAfcP7ptMXV4UPGjix9Xh1KQ5Vm79EpdzvfgMlqzLdD8H0lqjd1Pja0Z4D9%2Fgkx9f9Rl%2BqtRawd%2BEsa9d7VNeIKJPsEiqOq5%2FHig8QnhFPxEyJ7cKkx0ey%2ByWNCSCrWRNhSOnZ7pnV0uSLg76UEWJ%2B69zOQdXDvwHrxo7ihxOd5zzjIQxAWVxW3F4X%2FtdOaxlG3vsAkiIylf1oDGY0sQeQCIK48%2F1zAuYvhBKbwdGqRAZBuAYxqYuI5g1m%2Fr6usHLFROLL2PXLN%2BfTEztpEl5iGFBgF%2BjPcuhYz4MVs7n04mJUP0BRYfRFWtz0ZSOwjHpRvaKeeipAhBnuHxZrTfinXjtoTgAqhXJCpW0u%2FAmQ67Q9y4qoBW%2BTfBXTFESSUeRQXRhLUnpKJQiqLLh%2F6mcRWNWAbj42qBiA6RJYFpvwZkALEh96Im%2FuCkPVyHq%2BlvCqIgbTquJcu1YrPdlntwcigubU9lNJ91GpkUC2R2zffxYSuf5QdDQ4%2B0r3htB7Q2jRXEOFgMcTnbDu9FjoyjApj%2B5Z0nj%2BdxDDNQWREwvr6GvQY6pgF%2FJalkkmxK929sQ%2F1PylV%2FzloL2BjfDjZSeuEUaTOo7DO68V7CtSVNtUNIILFJ6ygK7774pmj7KKWwwolbC%2FlB%2Ft0BUN3eZ4IAP2K0BB3CfGhtezV5PIv69zlC2TmZ2A921KTYPrHNFD2KspPT2aC6R4v%2Fmo8ZL6t1d3BBFkJ5rgv8Ako93UhbqU3mPpiMTEsGcw4YgqYETPgM6MDNwoFp7Cey%2Fqnb&X-Amz-Signature=e68e485b767cba493cb05068b7a4898882e9ee492087350741135f2b19301e64&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLFWDGMH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIFk%2BjvZE9Br70mMEGFIN94rp0VGQbEtJ5xIzR6Qi59UtAiANWS4knHefQNm2sxF0s4%2B3j6gdnNLLD22m6KCLXnuVaSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMewxU8AxJWupXupamKtwDpSpYkbSuhPI9v8doxwOqG2llEUcMBxK3O%2FCeofn8xkG9R24iVQ4BnIxh8to6YuG8AQDA%2F5pq2vbsIF5ehupmN4I89q5z01j8%2FzryhoSWyffbhPSgzl6dZqCPbT0iL5dYA5bya3ALpDi%2B1DzI%2FT7Nrr%2F0TVREp8DJ7gcbaSnnJ9GEYA0yne5GLzy09VY%2B7WqgPb7VLZOLubD4nbzVRilKEnAFRxknFNv14rtPYyLoL4MJqpd26Rll%2BgedjVxYRVFwo8fLTcFRv8sbY5zyJ9wn%2BDc2tguOB5Sk9vEvyHb4HHehtyqBGCaEldAJZhCU%2FxXRqzEn39PhbQMmnP92Gukg6bX06MwB8beIz4pz7ep1Bbmgvudy2%2FZn0FtH5lV8iDU3nNbc%2BbJp8nGtd8ueGSoQFZxcpb0b1QF4vroqZEfFQgCyVHkPJmiQXKj0oP9VbO71gXa1EraZ5893fAMV7ZtGgDAwWQDjGibPjCzG4e2UF1je3aWRTllx%2FQPb1r5HgaapRQXdEnqUoDv19USSHmLGd%2BvOZsu3SdqdIGsH2fgkUnjKyQox0QxBe5BgWBIcmOzLqw%2Fmn5poWgk6F381UGiWd7ycB5lIzA%2FaMi2OPfduhL1t%2F1vWc7NbNWYwtxwwvr6GvQY6pgFDsITjaCoT9WvvsnqddKqM4FLLHMScEqcAMymEm2yLdKTG0nqcai6UREoZA3YCiBTBtbvq8818EEXRgfme0SMY4F7Apm7C58D2euCbHJm5lQg7FowhZS2RGfjn1nzHLRQidgHL44GvG%2BXFtjFiR2303DtEjOnAgOq3eVFQKWIEYYbVFyv8YCb2aUB9eZ3qNJpvMBiu394W8zppqVCubw72Gqvjr%2B33&X-Amz-Signature=1c48d64b03771ffcc2c22be0b9f45d77f618bdf4f6d7b557ed2debc0c9f6c2bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYXEXMGT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICque%2B8ghcVGcTPA6dODdScY0t6vkZ6%2BlyWK30bz9VV%2BAiBKXUnJbMkgjNvTQjhq4IIXi9uLphH6qD%2FzKXZR0m%2FUvSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIM0FPotdis2N8j%2F4VMKtwDb3QYZG8Y1j530xwJBJtN9sF%2Bq9A9SIxzGGFLKAJXhv8K3y0evTau%2Bew2M1XimPw586w%2B4eA%2FjEg9a3L5um3d6yIty3oetBq91NBcy%2BIhizH4jkjmIY%2FjMxROaKMEocdg9xtTBwtmNsoFdsTfG6HDEE346sCvtXKUkEvsQo4joANiTxDacKbYpa3rFT6cqla83TULMk6jJESdKMqvNZwY9Rd1mgeUcL0%2FDMAyp%2Brnueh%2FdNtTXzZz80Z5NEboalcrvk8syuYATwQQLubPAQKq0IHn9CJls8VT8YnFtotz5IbLHJN3MPN4QK6IZmVGgI1nr5mB7gR2Uzbh6exK2J017xtTdiutPA9RlpXSxzsBDpj7pyuyNEWlcJTYUlaarA%2FHxslHgceNWn9It5cOZy%2FhHYcMSzsgZcMpdinYwW4qBg6edYvPBbb8xr2u7Yh75C71qUbPj1%2FwCKKc%2FhbHcrMTRlRrb%2B2oEC0tO%2FCD804ChhBgVZ7CqJ%2BgMM7yoXODWXRzxGNYnXWtaGTAjbcIWM5HZ6D0B8WBRZfPVsvbdYjhqcRWwZhzAe%2BIMX8zgOekaYJKePwp5QUaQeh0O6USQg%2BoucnqkVZA%2BiA5mvEjxfaiqoSFsUm%2BhbYcHgCMIRww476GvQY6pgEp0FnvGUQL0Nok4iMHl1icVAYEGyRO1HgFHYIKjoz6igYFy0t%2Fw4mRUeemzwDDnM0oMBXOx%2FiS8eftAo9UcLlXFHFfQ%2FPPZBLqp42B44nkTZ5alEjL59oKAc2WcfGRh3EAHhP7Kf%2Figcqad421vlgTZtPWiYL9%2B9yVi553437iNdyZcXCkdZXK3cc5O9FBuyDKZsqUNQONdMb7btVItbC%2FD2FMTEMR&X-Amz-Signature=56f9ecb8541213f9f33e312dd9d2e976c9d1a2e0a7c00be912023a2e64be9e79&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYXEXMGT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICque%2B8ghcVGcTPA6dODdScY0t6vkZ6%2BlyWK30bz9VV%2BAiBKXUnJbMkgjNvTQjhq4IIXi9uLphH6qD%2FzKXZR0m%2FUvSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIM0FPotdis2N8j%2F4VMKtwDb3QYZG8Y1j530xwJBJtN9sF%2Bq9A9SIxzGGFLKAJXhv8K3y0evTau%2Bew2M1XimPw586w%2B4eA%2FjEg9a3L5um3d6yIty3oetBq91NBcy%2BIhizH4jkjmIY%2FjMxROaKMEocdg9xtTBwtmNsoFdsTfG6HDEE346sCvtXKUkEvsQo4joANiTxDacKbYpa3rFT6cqla83TULMk6jJESdKMqvNZwY9Rd1mgeUcL0%2FDMAyp%2Brnueh%2FdNtTXzZz80Z5NEboalcrvk8syuYATwQQLubPAQKq0IHn9CJls8VT8YnFtotz5IbLHJN3MPN4QK6IZmVGgI1nr5mB7gR2Uzbh6exK2J017xtTdiutPA9RlpXSxzsBDpj7pyuyNEWlcJTYUlaarA%2FHxslHgceNWn9It5cOZy%2FhHYcMSzsgZcMpdinYwW4qBg6edYvPBbb8xr2u7Yh75C71qUbPj1%2FwCKKc%2FhbHcrMTRlRrb%2B2oEC0tO%2FCD804ChhBgVZ7CqJ%2BgMM7yoXODWXRzxGNYnXWtaGTAjbcIWM5HZ6D0B8WBRZfPVsvbdYjhqcRWwZhzAe%2BIMX8zgOekaYJKePwp5QUaQeh0O6USQg%2BoucnqkVZA%2BiA5mvEjxfaiqoSFsUm%2BhbYcHgCMIRww476GvQY6pgEp0FnvGUQL0Nok4iMHl1icVAYEGyRO1HgFHYIKjoz6igYFy0t%2Fw4mRUeemzwDDnM0oMBXOx%2FiS8eftAo9UcLlXFHFfQ%2FPPZBLqp42B44nkTZ5alEjL59oKAc2WcfGRh3EAHhP7Kf%2Figcqad421vlgTZtPWiYL9%2B9yVi553437iNdyZcXCkdZXK3cc5O9FBuyDKZsqUNQONdMb7btVItbC%2FD2FMTEMR&X-Amz-Signature=09e705047a72551a8e9e87ce83bd0dc1d7f8f73303403ae352248a44e48df7fa&X-Amz-SignedHeaders=host&x-id=GetObject)

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
