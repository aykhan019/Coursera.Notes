

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMSNELDH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNg5%2FezdNxVs5x14u3WpKqdqlCE%2FjO1rJUnX%2FUiXs85AiEAvQJEdwCHQC6HCFwuxNWW%2BkzZLmChlaFFfMIWkmSfMaMq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIsWc5535ZWfvXXczyrcA3B9wmZpIN9mo7nJo8LbPHQhm1s5Dt%2BHjfHeO8XCHI8h%2BpIQLTzMwUqNFdooB%2B2ZQupRop1UXdCc0HMe9pbjAFWhdNrs2HFQrhDX6D7Xho%2B2TiwR166zeLCFGbs0KCIkgpOe4M7Q%2F9wg0ypUvwTFsN27e3ZxE1usVaO0J11BU8e3Hv62QiWW3mvWTI3XKrabeOYzCwcQkSNjFs%2FuNQscwjcfMItbx0%2BeEKDJ8mw9iuOfMoc0PGgO3ptlCq1aKpT3CWndd84jYI0sB2XUH%2FloNVrzkU3K6oDNEyCPMZtLkrjBZtQfow50lFYFUNyYA1SgIN%2BaLP4zdQUTVp%2FmVy5AGccumuTe%2BT%2B140FkHRPl58G%2F6bgfDdW6FUlf3YizeFemmBcVPjs1B0KK%2B80R5TnMnHZ4kp2cblRYV0CjQQZOmQj%2FMEapa35g5jf5L%2B6g0rU%2FyvsMJPm%2FoK4s0Ad%2BQQzAZvCxq9STbpICevpNE5S2z%2FUPHDQpe1paP8WQoE5DTmjsh8dfgIwbxO8P4oEvyJxXtvZykwTfsHIfZRtFbvqHM1W4R4utw7Hyubtdfr8kQlponZmV0AlN5VKIWbsWSiXBjccdofxDF%2F5zAO1MTJp8FcNgvWZlrEyoUESvQCHGMO%2Fygb0GOqUBd8iuuFLF%2BS%2Fffc6cZ30JryrE%2FJs097zfVhUjzPu4SJALxUjoi0IkSonOLSRoOysbkK5AmOu%2B9gR0ml8%2B0tZNMrxyYAqLWVwGisPZuZb1%2Bva5KDjpNW%2FN0HcPFRV0dhSrsFUt4G50QOFwBvfKSun%2BctSciXM9oGTWY67q1tgXYtmuutRxFGxBpnWgiuGcLxwk4PRF1DsHZVoY%2BxHRcHThufVjtJXr&X-Amz-Signature=ceace605efe7ef782f4443ca1ac1a6689a85b15ddaf133032a5594271888d2fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMSNELDH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNg5%2FezdNxVs5x14u3WpKqdqlCE%2FjO1rJUnX%2FUiXs85AiEAvQJEdwCHQC6HCFwuxNWW%2BkzZLmChlaFFfMIWkmSfMaMq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIsWc5535ZWfvXXczyrcA3B9wmZpIN9mo7nJo8LbPHQhm1s5Dt%2BHjfHeO8XCHI8h%2BpIQLTzMwUqNFdooB%2B2ZQupRop1UXdCc0HMe9pbjAFWhdNrs2HFQrhDX6D7Xho%2B2TiwR166zeLCFGbs0KCIkgpOe4M7Q%2F9wg0ypUvwTFsN27e3ZxE1usVaO0J11BU8e3Hv62QiWW3mvWTI3XKrabeOYzCwcQkSNjFs%2FuNQscwjcfMItbx0%2BeEKDJ8mw9iuOfMoc0PGgO3ptlCq1aKpT3CWndd84jYI0sB2XUH%2FloNVrzkU3K6oDNEyCPMZtLkrjBZtQfow50lFYFUNyYA1SgIN%2BaLP4zdQUTVp%2FmVy5AGccumuTe%2BT%2B140FkHRPl58G%2F6bgfDdW6FUlf3YizeFemmBcVPjs1B0KK%2B80R5TnMnHZ4kp2cblRYV0CjQQZOmQj%2FMEapa35g5jf5L%2B6g0rU%2FyvsMJPm%2FoK4s0Ad%2BQQzAZvCxq9STbpICevpNE5S2z%2FUPHDQpe1paP8WQoE5DTmjsh8dfgIwbxO8P4oEvyJxXtvZykwTfsHIfZRtFbvqHM1W4R4utw7Hyubtdfr8kQlponZmV0AlN5VKIWbsWSiXBjccdofxDF%2F5zAO1MTJp8FcNgvWZlrEyoUESvQCHGMO%2Fygb0GOqUBd8iuuFLF%2BS%2Fffc6cZ30JryrE%2FJs097zfVhUjzPu4SJALxUjoi0IkSonOLSRoOysbkK5AmOu%2B9gR0ml8%2B0tZNMrxyYAqLWVwGisPZuZb1%2Bva5KDjpNW%2FN0HcPFRV0dhSrsFUt4G50QOFwBvfKSun%2BctSciXM9oGTWY67q1tgXYtmuutRxFGxBpnWgiuGcLxwk4PRF1DsHZVoY%2BxHRcHThufVjtJXr&X-Amz-Signature=f93c4879b5a03f6e5091ebd55d4ca21cfb1141c76aefba533d44bb4be29bad9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMSNELDH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNg5%2FezdNxVs5x14u3WpKqdqlCE%2FjO1rJUnX%2FUiXs85AiEAvQJEdwCHQC6HCFwuxNWW%2BkzZLmChlaFFfMIWkmSfMaMq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDIsWc5535ZWfvXXczyrcA3B9wmZpIN9mo7nJo8LbPHQhm1s5Dt%2BHjfHeO8XCHI8h%2BpIQLTzMwUqNFdooB%2B2ZQupRop1UXdCc0HMe9pbjAFWhdNrs2HFQrhDX6D7Xho%2B2TiwR166zeLCFGbs0KCIkgpOe4M7Q%2F9wg0ypUvwTFsN27e3ZxE1usVaO0J11BU8e3Hv62QiWW3mvWTI3XKrabeOYzCwcQkSNjFs%2FuNQscwjcfMItbx0%2BeEKDJ8mw9iuOfMoc0PGgO3ptlCq1aKpT3CWndd84jYI0sB2XUH%2FloNVrzkU3K6oDNEyCPMZtLkrjBZtQfow50lFYFUNyYA1SgIN%2BaLP4zdQUTVp%2FmVy5AGccumuTe%2BT%2B140FkHRPl58G%2F6bgfDdW6FUlf3YizeFemmBcVPjs1B0KK%2B80R5TnMnHZ4kp2cblRYV0CjQQZOmQj%2FMEapa35g5jf5L%2B6g0rU%2FyvsMJPm%2FoK4s0Ad%2BQQzAZvCxq9STbpICevpNE5S2z%2FUPHDQpe1paP8WQoE5DTmjsh8dfgIwbxO8P4oEvyJxXtvZykwTfsHIfZRtFbvqHM1W4R4utw7Hyubtdfr8kQlponZmV0AlN5VKIWbsWSiXBjccdofxDF%2F5zAO1MTJp8FcNgvWZlrEyoUESvQCHGMO%2Fygb0GOqUBd8iuuFLF%2BS%2Fffc6cZ30JryrE%2FJs097zfVhUjzPu4SJALxUjoi0IkSonOLSRoOysbkK5AmOu%2B9gR0ml8%2B0tZNMrxyYAqLWVwGisPZuZb1%2Bva5KDjpNW%2FN0HcPFRV0dhSrsFUt4G50QOFwBvfKSun%2BctSciXM9oGTWY67q1tgXYtmuutRxFGxBpnWgiuGcLxwk4PRF1DsHZVoY%2BxHRcHThufVjtJXr&X-Amz-Signature=28a935df1abb16208112125dee7b4722332a88d77f2d714ad3a818dc558dbe04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X5VBUR4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcM00r7ilBHOjRdMuYV0fcq5AnIMKmmTSJPrsjO2xroAiASPsXBdQ%2FVcCueKumP%2F4on41MOnlZJkv33zll0aVed2ir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgNXYLpL%2FD9d1hllhKtwDN2gWyLqLrXKM996EIEIBm1lKfuIfS4MX4uu4oEHjC333fsWSZwFllRyE25BCmQwK9Zj2VENys%2BwZnwuBwMvN6VxStQFcenKv10KXZ2TIL4WnDj6wDkukb%2BZnUThF5kmoQ1aYP6ePv4NJurhSIv0xAYQxYEyZg52XnAMGaTfWyZE8wnjnjaRPGYaaDYRFdE3k6szZnELbNIrvHfhJdrMoNBujY6P5VsuxDJlhOo1mK%2BYvYaD8WjSEMbS3GKGbs5cFIqkFtZNVhmZhMkbw1xdDONMdhrISIfZzqJc8Pf7tZtf7%2ByjqU5cRqC39vG3jvXGFGzmGrTr7aWnxmwZze76XrHqnd6K9Eqvav%2BJ43127CeFKxWu4t%2FjEOAoEORLZRlVWBidS9mOpho31dDYeXJkK9SlWMwyXsxoz5ORNJb57hKJ3O%2FhN%2BLcAX60Z35L9x6Hq4PFltzKjEqlxoWw%2Bg5ArtluDHNzkIodjzgMr9utrTcmPk%2FhDuVdsn6xtiLhhtZ4mCwKvvI%2F%2Fbv1vqxeWAKaxJqAINiIY1eBGfw5SbQDUKhB7wa4EnkyeH3Qiu1CFXvfwZlOit9OIiWc%2FgAEeao82%2FYweocb46V%2BtfQoy14PSBvpxxyj%2FLsiOp6bY%2FFEw5vKBvQY6pgHwF15HdUIFRHTbKZ8ROZ9pkI8fneXSzULMWaF5isF7oVfE8ou4xCcHXr0SwS4yZtc4pUlP%2FQCiFJC2l7aw2HpnxTk8JtH3%2FDv6K%2Fcol2h6jRN53ZcnfoR%2BNseaR95DdLbfpRDz1JrMZp6SmPhYymi%2FXy1adg4CJJtsXHtt4hel%2BXIgZa1m%2FSYmNGLjIcRYxay9yaGuAfTH0oD4xsuwXpVTxbVgFBOa&X-Amz-Signature=40fe1ff92f75577f5688b25426078766f1700e20ff742f685f9a69a1cc9b9edc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X5VBUR4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcM00r7ilBHOjRdMuYV0fcq5AnIMKmmTSJPrsjO2xroAiASPsXBdQ%2FVcCueKumP%2F4on41MOnlZJkv33zll0aVed2ir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgNXYLpL%2FD9d1hllhKtwDN2gWyLqLrXKM996EIEIBm1lKfuIfS4MX4uu4oEHjC333fsWSZwFllRyE25BCmQwK9Zj2VENys%2BwZnwuBwMvN6VxStQFcenKv10KXZ2TIL4WnDj6wDkukb%2BZnUThF5kmoQ1aYP6ePv4NJurhSIv0xAYQxYEyZg52XnAMGaTfWyZE8wnjnjaRPGYaaDYRFdE3k6szZnELbNIrvHfhJdrMoNBujY6P5VsuxDJlhOo1mK%2BYvYaD8WjSEMbS3GKGbs5cFIqkFtZNVhmZhMkbw1xdDONMdhrISIfZzqJc8Pf7tZtf7%2ByjqU5cRqC39vG3jvXGFGzmGrTr7aWnxmwZze76XrHqnd6K9Eqvav%2BJ43127CeFKxWu4t%2FjEOAoEORLZRlVWBidS9mOpho31dDYeXJkK9SlWMwyXsxoz5ORNJb57hKJ3O%2FhN%2BLcAX60Z35L9x6Hq4PFltzKjEqlxoWw%2Bg5ArtluDHNzkIodjzgMr9utrTcmPk%2FhDuVdsn6xtiLhhtZ4mCwKvvI%2F%2Fbv1vqxeWAKaxJqAINiIY1eBGfw5SbQDUKhB7wa4EnkyeH3Qiu1CFXvfwZlOit9OIiWc%2FgAEeao82%2FYweocb46V%2BtfQoy14PSBvpxxyj%2FLsiOp6bY%2FFEw5vKBvQY6pgHwF15HdUIFRHTbKZ8ROZ9pkI8fneXSzULMWaF5isF7oVfE8ou4xCcHXr0SwS4yZtc4pUlP%2FQCiFJC2l7aw2HpnxTk8JtH3%2FDv6K%2Fcol2h6jRN53ZcnfoR%2BNseaR95DdLbfpRDz1JrMZp6SmPhYymi%2FXy1adg4CJJtsXHtt4hel%2BXIgZa1m%2FSYmNGLjIcRYxay9yaGuAfTH0oD4xsuwXpVTxbVgFBOa&X-Amz-Signature=11a4958b15a10262670f7b0f15b489743ba9c5b2a553b4bf6ff5034331d122ed&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X5VBUR4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcM00r7ilBHOjRdMuYV0fcq5AnIMKmmTSJPrsjO2xroAiASPsXBdQ%2FVcCueKumP%2F4on41MOnlZJkv33zll0aVed2ir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgNXYLpL%2FD9d1hllhKtwDN2gWyLqLrXKM996EIEIBm1lKfuIfS4MX4uu4oEHjC333fsWSZwFllRyE25BCmQwK9Zj2VENys%2BwZnwuBwMvN6VxStQFcenKv10KXZ2TIL4WnDj6wDkukb%2BZnUThF5kmoQ1aYP6ePv4NJurhSIv0xAYQxYEyZg52XnAMGaTfWyZE8wnjnjaRPGYaaDYRFdE3k6szZnELbNIrvHfhJdrMoNBujY6P5VsuxDJlhOo1mK%2BYvYaD8WjSEMbS3GKGbs5cFIqkFtZNVhmZhMkbw1xdDONMdhrISIfZzqJc8Pf7tZtf7%2ByjqU5cRqC39vG3jvXGFGzmGrTr7aWnxmwZze76XrHqnd6K9Eqvav%2BJ43127CeFKxWu4t%2FjEOAoEORLZRlVWBidS9mOpho31dDYeXJkK9SlWMwyXsxoz5ORNJb57hKJ3O%2FhN%2BLcAX60Z35L9x6Hq4PFltzKjEqlxoWw%2Bg5ArtluDHNzkIodjzgMr9utrTcmPk%2FhDuVdsn6xtiLhhtZ4mCwKvvI%2F%2Fbv1vqxeWAKaxJqAINiIY1eBGfw5SbQDUKhB7wa4EnkyeH3Qiu1CFXvfwZlOit9OIiWc%2FgAEeao82%2FYweocb46V%2BtfQoy14PSBvpxxyj%2FLsiOp6bY%2FFEw5vKBvQY6pgHwF15HdUIFRHTbKZ8ROZ9pkI8fneXSzULMWaF5isF7oVfE8ou4xCcHXr0SwS4yZtc4pUlP%2FQCiFJC2l7aw2HpnxTk8JtH3%2FDv6K%2Fcol2h6jRN53ZcnfoR%2BNseaR95DdLbfpRDz1JrMZp6SmPhYymi%2FXy1adg4CJJtsXHtt4hel%2BXIgZa1m%2FSYmNGLjIcRYxay9yaGuAfTH0oD4xsuwXpVTxbVgFBOa&X-Amz-Signature=fe6b616f449e215833b6a9ed9562a7882fc1d477cc51f84c4208e72a654c40ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X5VBUR4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcM00r7ilBHOjRdMuYV0fcq5AnIMKmmTSJPrsjO2xroAiASPsXBdQ%2FVcCueKumP%2F4on41MOnlZJkv33zll0aVed2ir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgNXYLpL%2FD9d1hllhKtwDN2gWyLqLrXKM996EIEIBm1lKfuIfS4MX4uu4oEHjC333fsWSZwFllRyE25BCmQwK9Zj2VENys%2BwZnwuBwMvN6VxStQFcenKv10KXZ2TIL4WnDj6wDkukb%2BZnUThF5kmoQ1aYP6ePv4NJurhSIv0xAYQxYEyZg52XnAMGaTfWyZE8wnjnjaRPGYaaDYRFdE3k6szZnELbNIrvHfhJdrMoNBujY6P5VsuxDJlhOo1mK%2BYvYaD8WjSEMbS3GKGbs5cFIqkFtZNVhmZhMkbw1xdDONMdhrISIfZzqJc8Pf7tZtf7%2ByjqU5cRqC39vG3jvXGFGzmGrTr7aWnxmwZze76XrHqnd6K9Eqvav%2BJ43127CeFKxWu4t%2FjEOAoEORLZRlVWBidS9mOpho31dDYeXJkK9SlWMwyXsxoz5ORNJb57hKJ3O%2FhN%2BLcAX60Z35L9x6Hq4PFltzKjEqlxoWw%2Bg5ArtluDHNzkIodjzgMr9utrTcmPk%2FhDuVdsn6xtiLhhtZ4mCwKvvI%2F%2Fbv1vqxeWAKaxJqAINiIY1eBGfw5SbQDUKhB7wa4EnkyeH3Qiu1CFXvfwZlOit9OIiWc%2FgAEeao82%2FYweocb46V%2BtfQoy14PSBvpxxyj%2FLsiOp6bY%2FFEw5vKBvQY6pgHwF15HdUIFRHTbKZ8ROZ9pkI8fneXSzULMWaF5isF7oVfE8ou4xCcHXr0SwS4yZtc4pUlP%2FQCiFJC2l7aw2HpnxTk8JtH3%2FDv6K%2Fcol2h6jRN53ZcnfoR%2BNseaR95DdLbfpRDz1JrMZp6SmPhYymi%2FXy1adg4CJJtsXHtt4hel%2BXIgZa1m%2FSYmNGLjIcRYxay9yaGuAfTH0oD4xsuwXpVTxbVgFBOa&X-Amz-Signature=23a98569fa18392e4229e2291054679e02d5b71393d5bcc5d933fec0c78c5ccb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X5VBUR4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcM00r7ilBHOjRdMuYV0fcq5AnIMKmmTSJPrsjO2xroAiASPsXBdQ%2FVcCueKumP%2F4on41MOnlZJkv33zll0aVed2ir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgNXYLpL%2FD9d1hllhKtwDN2gWyLqLrXKM996EIEIBm1lKfuIfS4MX4uu4oEHjC333fsWSZwFllRyE25BCmQwK9Zj2VENys%2BwZnwuBwMvN6VxStQFcenKv10KXZ2TIL4WnDj6wDkukb%2BZnUThF5kmoQ1aYP6ePv4NJurhSIv0xAYQxYEyZg52XnAMGaTfWyZE8wnjnjaRPGYaaDYRFdE3k6szZnELbNIrvHfhJdrMoNBujY6P5VsuxDJlhOo1mK%2BYvYaD8WjSEMbS3GKGbs5cFIqkFtZNVhmZhMkbw1xdDONMdhrISIfZzqJc8Pf7tZtf7%2ByjqU5cRqC39vG3jvXGFGzmGrTr7aWnxmwZze76XrHqnd6K9Eqvav%2BJ43127CeFKxWu4t%2FjEOAoEORLZRlVWBidS9mOpho31dDYeXJkK9SlWMwyXsxoz5ORNJb57hKJ3O%2FhN%2BLcAX60Z35L9x6Hq4PFltzKjEqlxoWw%2Bg5ArtluDHNzkIodjzgMr9utrTcmPk%2FhDuVdsn6xtiLhhtZ4mCwKvvI%2F%2Fbv1vqxeWAKaxJqAINiIY1eBGfw5SbQDUKhB7wa4EnkyeH3Qiu1CFXvfwZlOit9OIiWc%2FgAEeao82%2FYweocb46V%2BtfQoy14PSBvpxxyj%2FLsiOp6bY%2FFEw5vKBvQY6pgHwF15HdUIFRHTbKZ8ROZ9pkI8fneXSzULMWaF5isF7oVfE8ou4xCcHXr0SwS4yZtc4pUlP%2FQCiFJC2l7aw2HpnxTk8JtH3%2FDv6K%2Fcol2h6jRN53ZcnfoR%2BNseaR95DdLbfpRDz1JrMZp6SmPhYymi%2FXy1adg4CJJtsXHtt4hel%2BXIgZa1m%2FSYmNGLjIcRYxay9yaGuAfTH0oD4xsuwXpVTxbVgFBOa&X-Amz-Signature=00eed103cad700e13ee30214c8f85cf0a6cbcc72105ef5d7670d77912c72cb0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X5VBUR4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcM00r7ilBHOjRdMuYV0fcq5AnIMKmmTSJPrsjO2xroAiASPsXBdQ%2FVcCueKumP%2F4on41MOnlZJkv33zll0aVed2ir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgNXYLpL%2FD9d1hllhKtwDN2gWyLqLrXKM996EIEIBm1lKfuIfS4MX4uu4oEHjC333fsWSZwFllRyE25BCmQwK9Zj2VENys%2BwZnwuBwMvN6VxStQFcenKv10KXZ2TIL4WnDj6wDkukb%2BZnUThF5kmoQ1aYP6ePv4NJurhSIv0xAYQxYEyZg52XnAMGaTfWyZE8wnjnjaRPGYaaDYRFdE3k6szZnELbNIrvHfhJdrMoNBujY6P5VsuxDJlhOo1mK%2BYvYaD8WjSEMbS3GKGbs5cFIqkFtZNVhmZhMkbw1xdDONMdhrISIfZzqJc8Pf7tZtf7%2ByjqU5cRqC39vG3jvXGFGzmGrTr7aWnxmwZze76XrHqnd6K9Eqvav%2BJ43127CeFKxWu4t%2FjEOAoEORLZRlVWBidS9mOpho31dDYeXJkK9SlWMwyXsxoz5ORNJb57hKJ3O%2FhN%2BLcAX60Z35L9x6Hq4PFltzKjEqlxoWw%2Bg5ArtluDHNzkIodjzgMr9utrTcmPk%2FhDuVdsn6xtiLhhtZ4mCwKvvI%2F%2Fbv1vqxeWAKaxJqAINiIY1eBGfw5SbQDUKhB7wa4EnkyeH3Qiu1CFXvfwZlOit9OIiWc%2FgAEeao82%2FYweocb46V%2BtfQoy14PSBvpxxyj%2FLsiOp6bY%2FFEw5vKBvQY6pgHwF15HdUIFRHTbKZ8ROZ9pkI8fneXSzULMWaF5isF7oVfE8ou4xCcHXr0SwS4yZtc4pUlP%2FQCiFJC2l7aw2HpnxTk8JtH3%2FDv6K%2Fcol2h6jRN53ZcnfoR%2BNseaR95DdLbfpRDz1JrMZp6SmPhYymi%2FXy1adg4CJJtsXHtt4hel%2BXIgZa1m%2FSYmNGLjIcRYxay9yaGuAfTH0oD4xsuwXpVTxbVgFBOa&X-Amz-Signature=1fa8be9c0f91b897ba3eb49e2940eaf3b7c9f7c26d30fb2603b85b6b49120603&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QC4R3EOJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3hgzoe5aABKlmNFJbJWjF1xKgkvniRv1WVDSwrE%2FsvwIhAL3c0F9kHCKLxkOOWvpcyjQyat49jIPYlrcIV5sctOn9Kv8DCBEQABoMNjM3NDIzMTgzODA1IgzoWp6vPwVHu8EIup8q3ANg7ubUBdoXZa8BACRXa8pAkzSvoPPho1VqWccIV7fWeOWNSToJTFS2PqagGelIcghENdX6lmwMLafieBB34MF5RzLDxwOrdVAkOExTmy9xHJK1PtewcoLeSQ5Hwtq1%2Fg99fXvkvF%2FxRjAR%2Fb16REPPs9ab8qhpTL%2FRWkkCoAspV4fe2ci8jUy%2FL2pncZPJYXB4IiNgu%2BU3p3fUj5rUKFIdDyDJYLeYtkxv9KL2kz9ZmsUogKl5Vqq48HjyLP4MyoRxQWBof6zTQlesQNHAtbvhmPxD%2FoijiYn8z3d3%2BxNHPRpeQNb59iNsFyqWcsMZAWtVKlBrFWuuTyEULY%2B9Pu39GZha6k%2BPKm%2BxsywdG8FmWtCtDT%2FYjh9uTceJOM%2F2uV6znlaxDHUPMRnN5RxJP7Wg%2B7zyGC8Q6Pdll13wfmN7lzaCtkpdeazHo1EWzGFhc%2BA6QYxixxR6h7%2Ba37WgePvhmm4B5wymdthgXigqGH6nOC6ABy6SQD1yKkk4%2FnRaRDWDKTP9akpJv7FWKrnF3mpvMBKvC%2FoOmwQU2pCUXIIWiRtckXxA3%2Bsne%2F07DOkahijOBlMvdK7lTN3bDSm4omXMeoQ68Jgx15RTzlOtgUHDjnCya8R0rLf193VOQzCa84G9BjqkAUdE0lrAd4rjsqdUtVws90ZZ0NgNhnEoAHzUg3mlaz1IMPuGnqBR1bdbY4PYL61pPFepv4fBlcQuCVSlvQ7fkcTKW3ok3lEoi0mt4pSl41mScYPqW187i5yf%2FspLLhkyEbbjUD%2FL5%2BjYUNWNsdLuus4CX0WQdWr9bjBpL3SS4fRP2NZlBrQ0HZSesiikyZMkRoNT3nhQq90LXGHNF4DlJ64xRsA8&X-Amz-Signature=d1877bbd04684f833af92510f5bf8abd7693dd5b5ba43bbfa5fdc2375ff9def4&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DLZ4LJC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpEq8X6JtgckR8e4CHeIhn%2FIhG6bA0UWqtH%2Bm2ZzY0iwIhANvn6ORfFT1Ml03u0%2B2R5omdp9DbVfAmKZhr%2Bl55%2F2gUKv8DCBEQABoMNjM3NDIzMTgzODA1Igw6te67Mkht%2BnwOtnMq3AO9r0rHAqT9Au9so12wGYQRdiqkeEj%2BT69jETeRaBlS43foxUsfIYJ3jvh5b7tD%2B97qv8t2X3a2dDAeWmxjGbfZAh5OERilBNbYPE2jaFAeaDSdigKkDOzkuU6LPx8WaT2d0VPZGTSFbxB8hx7AL61n%2BXUOS74VuoF%2F1yNPVFYArjJpCGjXqQ6eYTb%2Bdu7NmH1MhTIxmD9jSk6mwQ2T7wseexbE1BHuAwPemu6jdTj9vWTUPWuB1obxmME6rhTIuiEdSlOUsELIwXgw4SWnCYy9qXtlSe0YgC%2BdbpGOomayFMN%2Fw3sCncfNbwOkJ9lKcR3tMvFT186A2Lat%2B8i%2FB79EgvR1Tr7gy5auf6k4hwtofzm9xTb5%2F%2FbLC%2BjoYjZ4UI1gGeqxa6OxH9sWqz8CQI9rgPumM%2FGSHJHlV9ARujUe%2B07zj8ooKUAylCnitlFj6MLSHM9nbf7RHidIPWzQeAJWhBIaWuBYeKrtUP3E34lBrkHioagoqAHI8Vn6qyLlA4SQHGNDJpFzCzgSpqYclUKQmewWxX1HpNXfbcgnyiA3r1PkGDchd9F%2BHRSCvbnwHBnwbYtusTLt0cwC3NaaRaJOd4aF%2Bc%2BNj9EROSbqem%2FFBc5LNLUyJYPfgcXFzjCr84G9BjqkAduHPZQFmAEfFnNfWTvFFkmBF4fHga1DtX5ELtGlgQN%2Fdqv84aKwVleMfi8QQ35oeXarwYdWZx%2B7Pe3hqkv%2Fmso5YtGNB1TT5FknlLCxCFqdArlGbpGZ1ePHZPsvSOHWUClWhjHn%2B0E%2B%2FOJS8e324QNzcbE6e64kH0OEw3BElRgO3kv%2B%2FvQMnStjiuqknCPLPXAB24IYuoTtVOvz3eH61%2Bk0SrZh&X-Amz-Signature=9ebea9617fdcf54697ea6508b9f39a0ccfce6d6d51f805123a1bcf2686f0b1d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X5VBUR4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcM00r7ilBHOjRdMuYV0fcq5AnIMKmmTSJPrsjO2xroAiASPsXBdQ%2FVcCueKumP%2F4on41MOnlZJkv33zll0aVed2ir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgNXYLpL%2FD9d1hllhKtwDN2gWyLqLrXKM996EIEIBm1lKfuIfS4MX4uu4oEHjC333fsWSZwFllRyE25BCmQwK9Zj2VENys%2BwZnwuBwMvN6VxStQFcenKv10KXZ2TIL4WnDj6wDkukb%2BZnUThF5kmoQ1aYP6ePv4NJurhSIv0xAYQxYEyZg52XnAMGaTfWyZE8wnjnjaRPGYaaDYRFdE3k6szZnELbNIrvHfhJdrMoNBujY6P5VsuxDJlhOo1mK%2BYvYaD8WjSEMbS3GKGbs5cFIqkFtZNVhmZhMkbw1xdDONMdhrISIfZzqJc8Pf7tZtf7%2ByjqU5cRqC39vG3jvXGFGzmGrTr7aWnxmwZze76XrHqnd6K9Eqvav%2BJ43127CeFKxWu4t%2FjEOAoEORLZRlVWBidS9mOpho31dDYeXJkK9SlWMwyXsxoz5ORNJb57hKJ3O%2FhN%2BLcAX60Z35L9x6Hq4PFltzKjEqlxoWw%2Bg5ArtluDHNzkIodjzgMr9utrTcmPk%2FhDuVdsn6xtiLhhtZ4mCwKvvI%2F%2Fbv1vqxeWAKaxJqAINiIY1eBGfw5SbQDUKhB7wa4EnkyeH3Qiu1CFXvfwZlOit9OIiWc%2FgAEeao82%2FYweocb46V%2BtfQoy14PSBvpxxyj%2FLsiOp6bY%2FFEw5vKBvQY6pgHwF15HdUIFRHTbKZ8ROZ9pkI8fneXSzULMWaF5isF7oVfE8ou4xCcHXr0SwS4yZtc4pUlP%2FQCiFJC2l7aw2HpnxTk8JtH3%2FDv6K%2Fcol2h6jRN53ZcnfoR%2BNseaR95DdLbfpRDz1JrMZp6SmPhYymi%2FXy1adg4CJJtsXHtt4hel%2BXIgZa1m%2FSYmNGLjIcRYxay9yaGuAfTH0oD4xsuwXpVTxbVgFBOa&X-Amz-Signature=676b6e0506ade1c292d16136a343a71cb8c984dfc2f31b21d7100ca340730c63&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X5VBUR4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcM00r7ilBHOjRdMuYV0fcq5AnIMKmmTSJPrsjO2xroAiASPsXBdQ%2FVcCueKumP%2F4on41MOnlZJkv33zll0aVed2ir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgNXYLpL%2FD9d1hllhKtwDN2gWyLqLrXKM996EIEIBm1lKfuIfS4MX4uu4oEHjC333fsWSZwFllRyE25BCmQwK9Zj2VENys%2BwZnwuBwMvN6VxStQFcenKv10KXZ2TIL4WnDj6wDkukb%2BZnUThF5kmoQ1aYP6ePv4NJurhSIv0xAYQxYEyZg52XnAMGaTfWyZE8wnjnjaRPGYaaDYRFdE3k6szZnELbNIrvHfhJdrMoNBujY6P5VsuxDJlhOo1mK%2BYvYaD8WjSEMbS3GKGbs5cFIqkFtZNVhmZhMkbw1xdDONMdhrISIfZzqJc8Pf7tZtf7%2ByjqU5cRqC39vG3jvXGFGzmGrTr7aWnxmwZze76XrHqnd6K9Eqvav%2BJ43127CeFKxWu4t%2FjEOAoEORLZRlVWBidS9mOpho31dDYeXJkK9SlWMwyXsxoz5ORNJb57hKJ3O%2FhN%2BLcAX60Z35L9x6Hq4PFltzKjEqlxoWw%2Bg5ArtluDHNzkIodjzgMr9utrTcmPk%2FhDuVdsn6xtiLhhtZ4mCwKvvI%2F%2Fbv1vqxeWAKaxJqAINiIY1eBGfw5SbQDUKhB7wa4EnkyeH3Qiu1CFXvfwZlOit9OIiWc%2FgAEeao82%2FYweocb46V%2BtfQoy14PSBvpxxyj%2FLsiOp6bY%2FFEw5vKBvQY6pgHwF15HdUIFRHTbKZ8ROZ9pkI8fneXSzULMWaF5isF7oVfE8ou4xCcHXr0SwS4yZtc4pUlP%2FQCiFJC2l7aw2HpnxTk8JtH3%2FDv6K%2Fcol2h6jRN53ZcnfoR%2BNseaR95DdLbfpRDz1JrMZp6SmPhYymi%2FXy1adg4CJJtsXHtt4hel%2BXIgZa1m%2FSYmNGLjIcRYxay9yaGuAfTH0oD4xsuwXpVTxbVgFBOa&X-Amz-Signature=a7c63742fa009b8fbb1523acb736d2737ed0e036658958492cf9ca7ad50f5137&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X5VBUR4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcM00r7ilBHOjRdMuYV0fcq5AnIMKmmTSJPrsjO2xroAiASPsXBdQ%2FVcCueKumP%2F4on41MOnlZJkv33zll0aVed2ir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgNXYLpL%2FD9d1hllhKtwDN2gWyLqLrXKM996EIEIBm1lKfuIfS4MX4uu4oEHjC333fsWSZwFllRyE25BCmQwK9Zj2VENys%2BwZnwuBwMvN6VxStQFcenKv10KXZ2TIL4WnDj6wDkukb%2BZnUThF5kmoQ1aYP6ePv4NJurhSIv0xAYQxYEyZg52XnAMGaTfWyZE8wnjnjaRPGYaaDYRFdE3k6szZnELbNIrvHfhJdrMoNBujY6P5VsuxDJlhOo1mK%2BYvYaD8WjSEMbS3GKGbs5cFIqkFtZNVhmZhMkbw1xdDONMdhrISIfZzqJc8Pf7tZtf7%2ByjqU5cRqC39vG3jvXGFGzmGrTr7aWnxmwZze76XrHqnd6K9Eqvav%2BJ43127CeFKxWu4t%2FjEOAoEORLZRlVWBidS9mOpho31dDYeXJkK9SlWMwyXsxoz5ORNJb57hKJ3O%2FhN%2BLcAX60Z35L9x6Hq4PFltzKjEqlxoWw%2Bg5ArtluDHNzkIodjzgMr9utrTcmPk%2FhDuVdsn6xtiLhhtZ4mCwKvvI%2F%2Fbv1vqxeWAKaxJqAINiIY1eBGfw5SbQDUKhB7wa4EnkyeH3Qiu1CFXvfwZlOit9OIiWc%2FgAEeao82%2FYweocb46V%2BtfQoy14PSBvpxxyj%2FLsiOp6bY%2FFEw5vKBvQY6pgHwF15HdUIFRHTbKZ8ROZ9pkI8fneXSzULMWaF5isF7oVfE8ou4xCcHXr0SwS4yZtc4pUlP%2FQCiFJC2l7aw2HpnxTk8JtH3%2FDv6K%2Fcol2h6jRN53ZcnfoR%2BNseaR95DdLbfpRDz1JrMZp6SmPhYymi%2FXy1adg4CJJtsXHtt4hel%2BXIgZa1m%2FSYmNGLjIcRYxay9yaGuAfTH0oD4xsuwXpVTxbVgFBOa&X-Amz-Signature=c5f69e35819d09ace3fccaf2d0f0d88d75f7b057ca9c729bafd5116e5e52037c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAFVIR23%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDro7vbNPx9%2FKTo0WW9OAEVAGGhl2XQo1Daqax3%2BL9nMQIgK0dJp%2B4VZNpBY7pSCq0fgRpPsp0FTwtxQVoldE%2BQCW8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPYnlZnwAXm5BMvdXCrcA4XbYXtNyQWMiRHRdhSYmZwVYckma3kTk%2FuERD0wc%2BoQMDPx%2B3oiv8dADSf3j%2Bxm7aYtcmjpW5HEPTB2KuvzHiW%2BOZ4jmMjTerrEQEn7QmOT6P0vb1opUuXF8%2BQZe5Msvi%2BPfYZsVV9QgoC87TFCfB329y2cWF1wYSplDSo4hD9polrtklxP9HaNNM93unAZBq1IYrLOzt%2Bm8wszOka5Df066MIRIh0KNw3Q4HWD0WzNH8s79AL8guzY4e28roHoahQsbqFkGpfsu%2BLMvn%2BnXPXKJa8H%2Fn0AF6VxDxcr9cI5FnZwOdMA95e5CWFihtjv%2Bdd%2F86nk6g1%2BnIG28Fei1OcKa0mEdo%2FyQ0YiGXuGNlDj0o6%2B22yMjqnBmfAlcCYHhiAaH6R4V0xydZNWZEbnJuLpbeNkluTbe9oicLegKKvlALcJFKiDN6Hih%2FRFQd3JAUxUrocmPMw7mE3oVfYYBfmuU1%2Fc9ArZ%2FfC4oWgJC5hG5P9zGe%2FrWfljL%2BVQkFdJ4wQg3DgXBSruDe3nUpwdHWEx5xjV5G40ioArHw3cwaDen75Cmy1tH9aRcOyTQun4HHzkskb1076zfoIP0t7RIjPH3edeKgudK4MQ71S1pSJJsMvFkSK3ubVJwBooMPvygb0GOqUBwTJ6Z90BMTvYa7hA8fu68Vgvj2rCp0iji5weS6YI3%2FCmlfFE%2BCP0fHkOEthlAY1cKXUJi9zaPxjK9v7pmw2wggaYep42Jo7k551%2BlcAsjL4ru9Wd2GtjjXPc%2BBzrdlT%2FyDx7wXTTimQAy5f%2FISzH5%2BRVhLMghr3MMV9tSXokyx1K35w7GyPpAy%2FltSh3bX67ZpPQ1t%2B4OzOa6f95%2FIJ%2B6JGBhmwd&X-Amz-Signature=b916ccbba822a21f07a7554220293710c029c31e8763f1b0b9c7d11656eb3208&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSKKQOGS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBGlaoyAgFOrDNV5wU8BT1OmTwLPHlo0qiWIxyfxbQ7KAiB6e7b4vZ76Z1g78tnWGRFW3tYYABjSSnNMKUXsdH5AQCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMJxfKbU7zuwbss3V7KtwDcQOd4uNp970dH5EnSnx5RpxRBQfBrxebBZ%2ByfWP34e6eYUoWxYXKs5a8GMjhMlStidWXpBvEw%2BXaRExiwawoabs0nvoI605LVEPcQt%2F2qkPvT6m9d1uPojRvqUkIqi9W%2B1sTOtTu70UcR7eeudzIQvDesp45Hw0sjffPgK%2FcCE8D8oJhVwx11ppaJmYmEKWtEHpsG92lnxwoDB67pkkL4hjmQ8Jaav%2F2HHKZhMhKSmjNm3wmbZHreCfBvImhAbfPDECjOTyl9XvZOgMJZAi4bhEtYHSJtgclh%2F%2FPSv%2Bm67wxoB21ftXih%2BKt0PpQWiTxzUnC4zcyR15EXGNbh27jHCqCKDHZvbzGyqjQmu9h1oqTgHVpeQ46lmlyGBxUT87TnJbypW9M3JxNMVrtW6IDBeiV3L1kcQaduzfunkdRa6P1KJ4mz7ZDSBciQ6Z6EfImy%2BlKuBuxNiJCG51OL0SbZJ4YMUzKtbDJm9fe0HrTlF7RW04tsi%2FbFvPfqygaIcVo44C8UEGkAph2FOg7YSwlzLo6iwT0d1iI8tr2TlNPuTsieW5%2BD1GKup%2BbV2QHYFewZWVueJqbIiuDPv2ht7asZqsFHT56856EvCHbAVj4xGoK7kIZRuFV39pdYUQwmvOBvQY6pgEplwLz3SZmxq42AVyM8n3rg4NN5RBL1oiz%2FQSsj60NtiBdxzHHTYZGIrnp7GUXNrwW8z1stbHR4aGP1oEoA9sfjUs0DmeU5vVENP2us7lwJa4lNicR6aLlonLlw2x6HsjJ9oAjTmSmNK3lFGjVXvBxS6hKrjCfJMF1p9bTIO0SPiB0hxXzKnvqL%2BMxduCVp9l9HUNx8ArdWwJ3rd6U%2BlVl6TUVMFRN&X-Amz-Signature=0e983db14447b7da45ae599153c0d486ea2628a0d6b203ece18f447e604e7320&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXDWDH5I%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYv09Lmaw4Sak%2F4vGYprIP1pFXfPwCYBW9ejpnTWIuoAiEArJT4hRrdJDeUuINImmCrguF8sE%2FcrUxzPQUdD0HUnHoq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGll3cXFaKTsLbM0sCrcAyulRMCLuL6uEHSiIMv2cXZUAnZM2l1aBPXkyoZk28GYBEUFt9icN91ehbMW7c4sCXqIk2fNyTVSCb%2B1N0Zu3TNv1hfME0T8vtaGqJEL6m7rTU0BXFBiZXtIkrTUSVVQzaOUwk4DmmVT6EcOvV%2FcxR5ECzSDfycApDoVl4NSDnVRhbv1iy%2FD4hfIPq%2FXXjpuPgg%2F6Do0ZJqW1ZrDXob5iGgDXHijXSAKOH%2F71KyM%2B58yL%2FsOoUPDucoKyFjTO7%2BrvWNXuI4gK80RXuc%2FixU9MFjYxSDxdVPrjIJZSeh2in55ti7oGpfjK%2F9dTD7H9zt86QNYPwC5lgK18vtZMi8OCTm7Kh2nV7gpEHprYhmLbpAdJr2vzeWqbbtbRx%2FnkxNTfnxZIOzBPjjTrwCEbzcrsiC7kTwznoZdGwcs4h0yFDaRQKfTcR%2BIDO8e1qd0xSlnG7KtF0cROC8qzWbLACygX6FR5KzVhExlRdkAaCI%2B2PGkfGciaTj9LgnCSgDnXR%2BcePlszjNQPbtd7kL%2BEornDYClFBV%2FyJYjUMftxpufF3xlblRrRZxAo5w187pxs1r8HTWcqKI10dVLEasETCOLr2NgT3pYnH0CsD5xFGkt5vcB1ccPD6EUZdAixXQOMK%2Fzgb0GOqUBE8hWLYKg9jW%2FyR4G1hIEzdM0JMNhsS29brfZcQzQ8d8gbabSZKPeUYm%2BJQ4XabFmzZcmJq3RZ8MtgAFogRKvDGWIZN8tQB4dji0lUCmrOjuA5Krt7G6sOz59FTgImY4xgZ3l4wtIKDA8bojzQHxF66ycbbu0SW3XbQYZrmq0ZwRHq0t0HMwZhWe%2F0PtxfyMZrzUGHjtxLpCR4nG%2BxkxwZRx%2B2VcI&X-Amz-Signature=9f4dee0c4b9a5a6deff87e6ef6ca72d01a2c298dfe7321f8661ebe437193d9ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYURTTGH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZX1WniJs008ZUUFgPGjX6PcJGPoKLlu5%2BvLmBpZ8m3QIgTgflzCtnlJMuSrRgg1rCzjA2PuR8R%2BqzJ7ijIPoh%2B2Uq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDCMji%2Brg4A4OioCLcircA0yUBpFm%2BAkFXOnsZSks3LVlRFZygM7YWnMZPmIg0NIP8ntL2sSwYobhZsqx06gUZiwtJZ8StVomKDZ8hXmi5q%2Bqt%2FVaJlTdiibfTf8NqHgatmcBLmMJTnON0nub3QYrdURHObwbD0HJOmdWwszrHnOV4%2B5fR53OvrZcoe7UbASqVXCB%2FYfxZgOFXp%2F5RF%2BYOAQB0D3uiCD3PpTS6RWMdit8EOa9OIHXDSuLqrfMJZbSgRnpzr6jg0KAo8oOHiO1U33J6doJs5%2F%2B3ko66iWYZ0vlNUuyBdki2Fx3W2xmKVva8KkJCJfLwaBn6wx%2FaY8t5mKE3TCW3i2W47ssCJBdDYty9XqgI2EWLcbNJtmglwzirFtz8Owpuzzyua7bXcYnds0Pk8QRaggHeZmbXmkj2MyPrC6KQGvNZFklYSHlGQCY%2FhnZvMzoyTKDnpiBypGteLuQ3gOTiRNCUKJIMUB%2F1hw8ZG5UU%2FwyrWmkALzRuJbkmqTpE39RgSIpE5xIWqPoTZFYeeT1dsMfGr7zcrVRj5q9a%2Bt7U4oTqNY24TZQmTLzQTH13p7dCi2TWoE6RG6K%2Fr49ZSaY8l2IvgX1%2F33fbzRiUOefeVlBVpc002Xu7T97WeHjOAbfaRFXHbi6MObygb0GOqUBbzaKjkTBoTMyKKloPiRE4qVx7GQrMEpVYMr0uDX1ylasaJjnjUB05T4CKliHu6C87R4yUmSvdmc%2FSXzO%2F8bWvDF5SwwWXrK7ZEbAbtLacnW6LmSiz72b2D1afh4%2BkPWEfk6DJqXVhDv54fbZdMhQYmMZP%2FFVdoCPFumBg7vIudrc5zhiGt9aQU9GERc847LODgFfD1NfrcnSrW85vdnwDVcyo7GC&X-Amz-Signature=9714411ddd1dd4584a73cc077267c11f50dd647d374bc3403c9596a9b2c555a5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYURTTGH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZX1WniJs008ZUUFgPGjX6PcJGPoKLlu5%2BvLmBpZ8m3QIgTgflzCtnlJMuSrRgg1rCzjA2PuR8R%2BqzJ7ijIPoh%2B2Uq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDCMji%2Brg4A4OioCLcircA0yUBpFm%2BAkFXOnsZSks3LVlRFZygM7YWnMZPmIg0NIP8ntL2sSwYobhZsqx06gUZiwtJZ8StVomKDZ8hXmi5q%2Bqt%2FVaJlTdiibfTf8NqHgatmcBLmMJTnON0nub3QYrdURHObwbD0HJOmdWwszrHnOV4%2B5fR53OvrZcoe7UbASqVXCB%2FYfxZgOFXp%2F5RF%2BYOAQB0D3uiCD3PpTS6RWMdit8EOa9OIHXDSuLqrfMJZbSgRnpzr6jg0KAo8oOHiO1U33J6doJs5%2F%2B3ko66iWYZ0vlNUuyBdki2Fx3W2xmKVva8KkJCJfLwaBn6wx%2FaY8t5mKE3TCW3i2W47ssCJBdDYty9XqgI2EWLcbNJtmglwzirFtz8Owpuzzyua7bXcYnds0Pk8QRaggHeZmbXmkj2MyPrC6KQGvNZFklYSHlGQCY%2FhnZvMzoyTKDnpiBypGteLuQ3gOTiRNCUKJIMUB%2F1hw8ZG5UU%2FwyrWmkALzRuJbkmqTpE39RgSIpE5xIWqPoTZFYeeT1dsMfGr7zcrVRj5q9a%2Bt7U4oTqNY24TZQmTLzQTH13p7dCi2TWoE6RG6K%2Fr49ZSaY8l2IvgX1%2F33fbzRiUOefeVlBVpc002Xu7T97WeHjOAbfaRFXHbi6MObygb0GOqUBbzaKjkTBoTMyKKloPiRE4qVx7GQrMEpVYMr0uDX1ylasaJjnjUB05T4CKliHu6C87R4yUmSvdmc%2FSXzO%2F8bWvDF5SwwWXrK7ZEbAbtLacnW6LmSiz72b2D1afh4%2BkPWEfk6DJqXVhDv54fbZdMhQYmMZP%2FFVdoCPFumBg7vIudrc5zhiGt9aQU9GERc847LODgFfD1NfrcnSrW85vdnwDVcyo7GC&X-Amz-Signature=6ad74b19e96a91c357bbbd4e96749058e6544541c256c78d19eb79edfe2184e1&X-Amz-SignedHeaders=host&x-id=GetObject)

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
