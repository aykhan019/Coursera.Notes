

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KEVHPNE%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDpm4tJFhw0vwt%2FYG4prOmx18IG%2FEzeWfqrqKnnAsW1eAIgTImM9r8m1w8d5w7P563%2Fn%2BUBomGC%2B0P895vs7cB58rAqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFihwiloZWHiRwHqeSrcA6hKYWlljTnRfJ8tKnVVPTVa%2FQEf%2F07rKFVw2wSwHY9eZt4663dbE2w8%2FXEKsA7dYT4YsiyODlLNbChuAyreYkRDUHfHlsaKyiFHAFJzIQLnFLN2IFGJdtUAT4%2BMaImZnvyuwCjfxl7ycf2mbj318dH2vkznZmJFRT99R0JsL4kbuO%2BsWg8Ce%2Bug7tV4T6QtkQIykn7wjFu%2F%2FeeSkL1OoaXGkq9ywS9Dnzh4UY%2BopZ%2FC2%2F19v13KfH%2BqGlxqfadVnZZ%2F1osCGtgFmCMUTengaSW3R64gg21Tzmw%2FxA50XDBtwkeG8R%2BR9Q2RUudSOM8IklUscG0r4rg76rA1ybKpNJoiD%2FKczFsBh2Pub8%2BK91qJ%2BpPDGWRbAu%2B15PvebVN52EKXdReJX9UWlqaRgWv5FMHM6qtuxwRPFT%2FLJcY6MmmFyT0smH7KtWTG7vrbG7VEl7aMV5FKQCFhRsYMNQBooiugc61JhhqTxWIgr53WKjroK2frkh%2BRTcmE6mzzPljBs%2FgJ1FGpKWL%2BROB5CTQJgJrNpU4DLpSMzlrxjEDX0zlj8zqIyLPIbxjabYUjcp3YXLOLVIYwveEdLIb1IIXvAkvvQQp2wi2kxMMiWgT8CRbP3Pu2QozJQTOXzxhrMOi3jr4GOqUBSWYNPSFtOYBqQY6cXZQfobuf4tmBmK3NzjDPWgixDNxOK0n%2Boj%2BmX1fgpS39RsKyF%2Fzj5FDg3p9hx4rOafNI0Wz2TjHRnyZ06HZJiLOYxyF43WJv06JedbLunEYp%2BBTHlKJDv3DbstuRzwqoNUVegjdFt2cNkv4A4jyOEBWFweHan0sqen0rDg1DudfuLgaTNVJxbKippdslsvQIpkE3Tyr3z%2Bp0&X-Amz-Signature=279504c465f0c616524dc4cd6b4a9a84814496351df9501b85295e98c8a9ea32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KEVHPNE%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDpm4tJFhw0vwt%2FYG4prOmx18IG%2FEzeWfqrqKnnAsW1eAIgTImM9r8m1w8d5w7P563%2Fn%2BUBomGC%2B0P895vs7cB58rAqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFihwiloZWHiRwHqeSrcA6hKYWlljTnRfJ8tKnVVPTVa%2FQEf%2F07rKFVw2wSwHY9eZt4663dbE2w8%2FXEKsA7dYT4YsiyODlLNbChuAyreYkRDUHfHlsaKyiFHAFJzIQLnFLN2IFGJdtUAT4%2BMaImZnvyuwCjfxl7ycf2mbj318dH2vkznZmJFRT99R0JsL4kbuO%2BsWg8Ce%2Bug7tV4T6QtkQIykn7wjFu%2F%2FeeSkL1OoaXGkq9ywS9Dnzh4UY%2BopZ%2FC2%2F19v13KfH%2BqGlxqfadVnZZ%2F1osCGtgFmCMUTengaSW3R64gg21Tzmw%2FxA50XDBtwkeG8R%2BR9Q2RUudSOM8IklUscG0r4rg76rA1ybKpNJoiD%2FKczFsBh2Pub8%2BK91qJ%2BpPDGWRbAu%2B15PvebVN52EKXdReJX9UWlqaRgWv5FMHM6qtuxwRPFT%2FLJcY6MmmFyT0smH7KtWTG7vrbG7VEl7aMV5FKQCFhRsYMNQBooiugc61JhhqTxWIgr53WKjroK2frkh%2BRTcmE6mzzPljBs%2FgJ1FGpKWL%2BROB5CTQJgJrNpU4DLpSMzlrxjEDX0zlj8zqIyLPIbxjabYUjcp3YXLOLVIYwveEdLIb1IIXvAkvvQQp2wi2kxMMiWgT8CRbP3Pu2QozJQTOXzxhrMOi3jr4GOqUBSWYNPSFtOYBqQY6cXZQfobuf4tmBmK3NzjDPWgixDNxOK0n%2Boj%2BmX1fgpS39RsKyF%2Fzj5FDg3p9hx4rOafNI0Wz2TjHRnyZ06HZJiLOYxyF43WJv06JedbLunEYp%2BBTHlKJDv3DbstuRzwqoNUVegjdFt2cNkv4A4jyOEBWFweHan0sqen0rDg1DudfuLgaTNVJxbKippdslsvQIpkE3Tyr3z%2Bp0&X-Amz-Signature=9efafc5d299f54b0c4195d64bfe717e71edd538e589e7f120e0e6fced1a09028&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KEVHPNE%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDpm4tJFhw0vwt%2FYG4prOmx18IG%2FEzeWfqrqKnnAsW1eAIgTImM9r8m1w8d5w7P563%2Fn%2BUBomGC%2B0P895vs7cB58rAqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFihwiloZWHiRwHqeSrcA6hKYWlljTnRfJ8tKnVVPTVa%2FQEf%2F07rKFVw2wSwHY9eZt4663dbE2w8%2FXEKsA7dYT4YsiyODlLNbChuAyreYkRDUHfHlsaKyiFHAFJzIQLnFLN2IFGJdtUAT4%2BMaImZnvyuwCjfxl7ycf2mbj318dH2vkznZmJFRT99R0JsL4kbuO%2BsWg8Ce%2Bug7tV4T6QtkQIykn7wjFu%2F%2FeeSkL1OoaXGkq9ywS9Dnzh4UY%2BopZ%2FC2%2F19v13KfH%2BqGlxqfadVnZZ%2F1osCGtgFmCMUTengaSW3R64gg21Tzmw%2FxA50XDBtwkeG8R%2BR9Q2RUudSOM8IklUscG0r4rg76rA1ybKpNJoiD%2FKczFsBh2Pub8%2BK91qJ%2BpPDGWRbAu%2B15PvebVN52EKXdReJX9UWlqaRgWv5FMHM6qtuxwRPFT%2FLJcY6MmmFyT0smH7KtWTG7vrbG7VEl7aMV5FKQCFhRsYMNQBooiugc61JhhqTxWIgr53WKjroK2frkh%2BRTcmE6mzzPljBs%2FgJ1FGpKWL%2BROB5CTQJgJrNpU4DLpSMzlrxjEDX0zlj8zqIyLPIbxjabYUjcp3YXLOLVIYwveEdLIb1IIXvAkvvQQp2wi2kxMMiWgT8CRbP3Pu2QozJQTOXzxhrMOi3jr4GOqUBSWYNPSFtOYBqQY6cXZQfobuf4tmBmK3NzjDPWgixDNxOK0n%2Boj%2BmX1fgpS39RsKyF%2Fzj5FDg3p9hx4rOafNI0Wz2TjHRnyZ06HZJiLOYxyF43WJv06JedbLunEYp%2BBTHlKJDv3DbstuRzwqoNUVegjdFt2cNkv4A4jyOEBWFweHan0sqen0rDg1DudfuLgaTNVJxbKippdslsvQIpkE3Tyr3z%2Bp0&X-Amz-Signature=624ec6267514a00cc82263414727296f94b22267a3d0df07619343422701bfce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMDKSSK%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDbnzZ8WqZF82%2Bv42VOIr0zuFwHoW5tCmuNuePUE3qyegIgAqsw9KZ8k5X6l5su%2B9XUzo0zDA9Q8gRu2AbtJS1HvEgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgmBQpyXDXmBx4hmyrcA6tsRPftjT%2BNbljnrGML9vuKvR1b9pNMjXyVSPetRq%2F1vlY5F5%2FYvHzRYIyxH46his8qhpXL84cgdyNYrWgjyrxOjgdQ2hjl6jW51ZLLmXKJoNAsigJPp%2BlsulPzHPJ1Oxor2tWuy7zsT4aZ%2BBc2g7W%2FMnImAZWfz7YQKxu39Nu6InPjfYlzVHaVZflhBzhbvOr2Y8TjOOAE3yDPl1T3LWrU%2BPtMTbbH58wHQbxzdq0gsOj%2BWJomLONGqmnSm%2FSgr2V3RxIq8fKF33877fvcGOgkfFTXqtaZXsEuqzqKhCImR9fkfs%2BXZuH3vrjSjl7mSCJzN0cM9X60hJZ7vCt81Rqf8mJk4JvWm3PtV9VtBW2k70u0%2BoKhh3Dza7%2FiUNvNuaQcFSoHQ9x9rKV1k95mYLdzRPNuxzXi8dROgJdyvpIl3vlAT09SIOsXGFncSG5PXT0ONA70lsGlCeU7F14c8S3Qtx1gr4BfO4T4EpFXWjARmtKX4kEJDL4zx2ybEIOyf03r55gnhAE8uzaOMSe2iZ6ysdw5X9cIYZTKbR5H8nzbvmHsSkyDwvxf3c8suiPeuOovfgq%2BZxyAKWC9d0ZqXufuJ%2Bi2djWvr0L7fibuD%2FCGItm%2Bd%2BSSTM11N1xBMIa4jr4GOqUBnYY8cvVxIhlESLGkphsl%2FYSJY1bUXF%2BmCoIEYySvt5N8wFuznSEazC0XP77C0fW89NsFb82ghsDOi3PzsuT9A6d0c01hqYY1oJk1vLJXe4ddzW5CafB6K91GJJvrGzekOn3y3gnLFtZ4HY%2BCTrmj8x7a2HKrLiHVHs8znJ7LaDFI5JHh%2F2bCcG4sqScMpz%2BgclyTTBV5qp5ww2iOpUQVoMA7sXnT&X-Amz-Signature=b2ac02f841c313fb94099ad9008cbf394a39533a431e1f88285e9ad4b193d5eb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMDKSSK%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDbnzZ8WqZF82%2Bv42VOIr0zuFwHoW5tCmuNuePUE3qyegIgAqsw9KZ8k5X6l5su%2B9XUzo0zDA9Q8gRu2AbtJS1HvEgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgmBQpyXDXmBx4hmyrcA6tsRPftjT%2BNbljnrGML9vuKvR1b9pNMjXyVSPetRq%2F1vlY5F5%2FYvHzRYIyxH46his8qhpXL84cgdyNYrWgjyrxOjgdQ2hjl6jW51ZLLmXKJoNAsigJPp%2BlsulPzHPJ1Oxor2tWuy7zsT4aZ%2BBc2g7W%2FMnImAZWfz7YQKxu39Nu6InPjfYlzVHaVZflhBzhbvOr2Y8TjOOAE3yDPl1T3LWrU%2BPtMTbbH58wHQbxzdq0gsOj%2BWJomLONGqmnSm%2FSgr2V3RxIq8fKF33877fvcGOgkfFTXqtaZXsEuqzqKhCImR9fkfs%2BXZuH3vrjSjl7mSCJzN0cM9X60hJZ7vCt81Rqf8mJk4JvWm3PtV9VtBW2k70u0%2BoKhh3Dza7%2FiUNvNuaQcFSoHQ9x9rKV1k95mYLdzRPNuxzXi8dROgJdyvpIl3vlAT09SIOsXGFncSG5PXT0ONA70lsGlCeU7F14c8S3Qtx1gr4BfO4T4EpFXWjARmtKX4kEJDL4zx2ybEIOyf03r55gnhAE8uzaOMSe2iZ6ysdw5X9cIYZTKbR5H8nzbvmHsSkyDwvxf3c8suiPeuOovfgq%2BZxyAKWC9d0ZqXufuJ%2Bi2djWvr0L7fibuD%2FCGItm%2Bd%2BSSTM11N1xBMIa4jr4GOqUBnYY8cvVxIhlESLGkphsl%2FYSJY1bUXF%2BmCoIEYySvt5N8wFuznSEazC0XP77C0fW89NsFb82ghsDOi3PzsuT9A6d0c01hqYY1oJk1vLJXe4ddzW5CafB6K91GJJvrGzekOn3y3gnLFtZ4HY%2BCTrmj8x7a2HKrLiHVHs8znJ7LaDFI5JHh%2F2bCcG4sqScMpz%2BgclyTTBV5qp5ww2iOpUQVoMA7sXnT&X-Amz-Signature=a43f1770da18d586d125f6314fb9b2159179bf2637d4435ecddcee87d2996ba9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMDKSSK%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDbnzZ8WqZF82%2Bv42VOIr0zuFwHoW5tCmuNuePUE3qyegIgAqsw9KZ8k5X6l5su%2B9XUzo0zDA9Q8gRu2AbtJS1HvEgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgmBQpyXDXmBx4hmyrcA6tsRPftjT%2BNbljnrGML9vuKvR1b9pNMjXyVSPetRq%2F1vlY5F5%2FYvHzRYIyxH46his8qhpXL84cgdyNYrWgjyrxOjgdQ2hjl6jW51ZLLmXKJoNAsigJPp%2BlsulPzHPJ1Oxor2tWuy7zsT4aZ%2BBc2g7W%2FMnImAZWfz7YQKxu39Nu6InPjfYlzVHaVZflhBzhbvOr2Y8TjOOAE3yDPl1T3LWrU%2BPtMTbbH58wHQbxzdq0gsOj%2BWJomLONGqmnSm%2FSgr2V3RxIq8fKF33877fvcGOgkfFTXqtaZXsEuqzqKhCImR9fkfs%2BXZuH3vrjSjl7mSCJzN0cM9X60hJZ7vCt81Rqf8mJk4JvWm3PtV9VtBW2k70u0%2BoKhh3Dza7%2FiUNvNuaQcFSoHQ9x9rKV1k95mYLdzRPNuxzXi8dROgJdyvpIl3vlAT09SIOsXGFncSG5PXT0ONA70lsGlCeU7F14c8S3Qtx1gr4BfO4T4EpFXWjARmtKX4kEJDL4zx2ybEIOyf03r55gnhAE8uzaOMSe2iZ6ysdw5X9cIYZTKbR5H8nzbvmHsSkyDwvxf3c8suiPeuOovfgq%2BZxyAKWC9d0ZqXufuJ%2Bi2djWvr0L7fibuD%2FCGItm%2Bd%2BSSTM11N1xBMIa4jr4GOqUBnYY8cvVxIhlESLGkphsl%2FYSJY1bUXF%2BmCoIEYySvt5N8wFuznSEazC0XP77C0fW89NsFb82ghsDOi3PzsuT9A6d0c01hqYY1oJk1vLJXe4ddzW5CafB6K91GJJvrGzekOn3y3gnLFtZ4HY%2BCTrmj8x7a2HKrLiHVHs8znJ7LaDFI5JHh%2F2bCcG4sqScMpz%2BgclyTTBV5qp5ww2iOpUQVoMA7sXnT&X-Amz-Signature=8e834933b6ea3bafadb671070c4edbaffa7fb51303108a52ed946b4248d8a1d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMDKSSK%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDbnzZ8WqZF82%2Bv42VOIr0zuFwHoW5tCmuNuePUE3qyegIgAqsw9KZ8k5X6l5su%2B9XUzo0zDA9Q8gRu2AbtJS1HvEgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgmBQpyXDXmBx4hmyrcA6tsRPftjT%2BNbljnrGML9vuKvR1b9pNMjXyVSPetRq%2F1vlY5F5%2FYvHzRYIyxH46his8qhpXL84cgdyNYrWgjyrxOjgdQ2hjl6jW51ZLLmXKJoNAsigJPp%2BlsulPzHPJ1Oxor2tWuy7zsT4aZ%2BBc2g7W%2FMnImAZWfz7YQKxu39Nu6InPjfYlzVHaVZflhBzhbvOr2Y8TjOOAE3yDPl1T3LWrU%2BPtMTbbH58wHQbxzdq0gsOj%2BWJomLONGqmnSm%2FSgr2V3RxIq8fKF33877fvcGOgkfFTXqtaZXsEuqzqKhCImR9fkfs%2BXZuH3vrjSjl7mSCJzN0cM9X60hJZ7vCt81Rqf8mJk4JvWm3PtV9VtBW2k70u0%2BoKhh3Dza7%2FiUNvNuaQcFSoHQ9x9rKV1k95mYLdzRPNuxzXi8dROgJdyvpIl3vlAT09SIOsXGFncSG5PXT0ONA70lsGlCeU7F14c8S3Qtx1gr4BfO4T4EpFXWjARmtKX4kEJDL4zx2ybEIOyf03r55gnhAE8uzaOMSe2iZ6ysdw5X9cIYZTKbR5H8nzbvmHsSkyDwvxf3c8suiPeuOovfgq%2BZxyAKWC9d0ZqXufuJ%2Bi2djWvr0L7fibuD%2FCGItm%2Bd%2BSSTM11N1xBMIa4jr4GOqUBnYY8cvVxIhlESLGkphsl%2FYSJY1bUXF%2BmCoIEYySvt5N8wFuznSEazC0XP77C0fW89NsFb82ghsDOi3PzsuT9A6d0c01hqYY1oJk1vLJXe4ddzW5CafB6K91GJJvrGzekOn3y3gnLFtZ4HY%2BCTrmj8x7a2HKrLiHVHs8znJ7LaDFI5JHh%2F2bCcG4sqScMpz%2BgclyTTBV5qp5ww2iOpUQVoMA7sXnT&X-Amz-Signature=25d5266b23bafa3897779b46457dad1dcea3eddf26886572e5ca75180c0fc839&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMDKSSK%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDbnzZ8WqZF82%2Bv42VOIr0zuFwHoW5tCmuNuePUE3qyegIgAqsw9KZ8k5X6l5su%2B9XUzo0zDA9Q8gRu2AbtJS1HvEgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgmBQpyXDXmBx4hmyrcA6tsRPftjT%2BNbljnrGML9vuKvR1b9pNMjXyVSPetRq%2F1vlY5F5%2FYvHzRYIyxH46his8qhpXL84cgdyNYrWgjyrxOjgdQ2hjl6jW51ZLLmXKJoNAsigJPp%2BlsulPzHPJ1Oxor2tWuy7zsT4aZ%2BBc2g7W%2FMnImAZWfz7YQKxu39Nu6InPjfYlzVHaVZflhBzhbvOr2Y8TjOOAE3yDPl1T3LWrU%2BPtMTbbH58wHQbxzdq0gsOj%2BWJomLONGqmnSm%2FSgr2V3RxIq8fKF33877fvcGOgkfFTXqtaZXsEuqzqKhCImR9fkfs%2BXZuH3vrjSjl7mSCJzN0cM9X60hJZ7vCt81Rqf8mJk4JvWm3PtV9VtBW2k70u0%2BoKhh3Dza7%2FiUNvNuaQcFSoHQ9x9rKV1k95mYLdzRPNuxzXi8dROgJdyvpIl3vlAT09SIOsXGFncSG5PXT0ONA70lsGlCeU7F14c8S3Qtx1gr4BfO4T4EpFXWjARmtKX4kEJDL4zx2ybEIOyf03r55gnhAE8uzaOMSe2iZ6ysdw5X9cIYZTKbR5H8nzbvmHsSkyDwvxf3c8suiPeuOovfgq%2BZxyAKWC9d0ZqXufuJ%2Bi2djWvr0L7fibuD%2FCGItm%2Bd%2BSSTM11N1xBMIa4jr4GOqUBnYY8cvVxIhlESLGkphsl%2FYSJY1bUXF%2BmCoIEYySvt5N8wFuznSEazC0XP77C0fW89NsFb82ghsDOi3PzsuT9A6d0c01hqYY1oJk1vLJXe4ddzW5CafB6K91GJJvrGzekOn3y3gnLFtZ4HY%2BCTrmj8x7a2HKrLiHVHs8znJ7LaDFI5JHh%2F2bCcG4sqScMpz%2BgclyTTBV5qp5ww2iOpUQVoMA7sXnT&X-Amz-Signature=2894496935be0a42777b59060975ccb39748eff159cb3692378e859bfd4f2f9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMDKSSK%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDbnzZ8WqZF82%2Bv42VOIr0zuFwHoW5tCmuNuePUE3qyegIgAqsw9KZ8k5X6l5su%2B9XUzo0zDA9Q8gRu2AbtJS1HvEgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgmBQpyXDXmBx4hmyrcA6tsRPftjT%2BNbljnrGML9vuKvR1b9pNMjXyVSPetRq%2F1vlY5F5%2FYvHzRYIyxH46his8qhpXL84cgdyNYrWgjyrxOjgdQ2hjl6jW51ZLLmXKJoNAsigJPp%2BlsulPzHPJ1Oxor2tWuy7zsT4aZ%2BBc2g7W%2FMnImAZWfz7YQKxu39Nu6InPjfYlzVHaVZflhBzhbvOr2Y8TjOOAE3yDPl1T3LWrU%2BPtMTbbH58wHQbxzdq0gsOj%2BWJomLONGqmnSm%2FSgr2V3RxIq8fKF33877fvcGOgkfFTXqtaZXsEuqzqKhCImR9fkfs%2BXZuH3vrjSjl7mSCJzN0cM9X60hJZ7vCt81Rqf8mJk4JvWm3PtV9VtBW2k70u0%2BoKhh3Dza7%2FiUNvNuaQcFSoHQ9x9rKV1k95mYLdzRPNuxzXi8dROgJdyvpIl3vlAT09SIOsXGFncSG5PXT0ONA70lsGlCeU7F14c8S3Qtx1gr4BfO4T4EpFXWjARmtKX4kEJDL4zx2ybEIOyf03r55gnhAE8uzaOMSe2iZ6ysdw5X9cIYZTKbR5H8nzbvmHsSkyDwvxf3c8suiPeuOovfgq%2BZxyAKWC9d0ZqXufuJ%2Bi2djWvr0L7fibuD%2FCGItm%2Bd%2BSSTM11N1xBMIa4jr4GOqUBnYY8cvVxIhlESLGkphsl%2FYSJY1bUXF%2BmCoIEYySvt5N8wFuznSEazC0XP77C0fW89NsFb82ghsDOi3PzsuT9A6d0c01hqYY1oJk1vLJXe4ddzW5CafB6K91GJJvrGzekOn3y3gnLFtZ4HY%2BCTrmj8x7a2HKrLiHVHs8znJ7LaDFI5JHh%2F2bCcG4sqScMpz%2BgclyTTBV5qp5ww2iOpUQVoMA7sXnT&X-Amz-Signature=63d522c4002da7600c90e8583667935f75b754c76716f495b7e2c73465df037f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MHEJHF3%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCIBw%2F7D3kafXX%2Bi6yxgrK3I8nb4IVjihwVSenhMunhZF3AiBdea8TWwbfzK%2BUs0vtWRh41ybO9EoRIQTpEsmXdhIvmyqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2L47qsmGVZDoea4jKtwD%2F1BNezIBEhDhP%2Frk3mIjV%2Fsfx7%2FsX5sE%2BCA7p%2BKOaqI3W%2BUW0tzrm0zVDE38d22sPk3KIsgiwWzIVTL7n0hb1Ah6f1xObEuI3IOVxVoZw3x%2BBZIp53YsRdSwRFnVF%2Bgf583kOuV20iw7kVPn1dcUSUynviSbNj9yLKBpT7KR0z0dCZp2g8J2cCgfgHd2C0Qm%2Fvjm650uecbvFcPbyLI7S8LXKMM1PKyzOkBrYc19zWCgExyu3CUG9JYwusMB5DS6Qpba37FSPGq27QKeZCg1bEVCYmAoVPn5MGCwbGc0ca69FO15xWIj2A1uBU%2Bq1JXYXfrVcDgz%2BKT%2FJCYz0Bn2udODDHVNEa9IPwDqEVgJuluMKywn%2FKERFGEdjs8FaAE9lKlZlqJiHsJyEaG0wCl8Fr%2BC5p3SQRSY%2BUpjGKR%2B6lDfORqb6%2B8FGwJ9pWmBuZiDK4qq0myX1solYkcSaYhD95DzbWJUSovdJQh4qjFWxChX7kQAmQwmQ8iUE4QnUU1qpuGh7qpOKOBbirN10H4Hg24Wd5UWkdqo038KtmNWFxb2DMvQO30Q1uEBCCfGUStdVSwmUAGRNFkkOZeI232acJSOWBO5zfjAYDhdsVDvvhCw6CPoNVveyuD6k3ow%2B7eOvgY6pgHk8XStK3e0yEpEM3RmB85wnPs3BEhUs4WQcuyawu1KOPWVOYl2sQdPoHMnC1dcdJgj4G9BMCeWX8DnqvTSmuHIyfqhJTxBpt1klGvlZoufnhfhXque2R7wkfUNcc46c4LSFYQ3MyjLAVbr4gF2lAWqWsJNi5CkDgqYX17zSprB7DfGCZzKCh1hQLiG3D2PtQlb9ilf5%2FDZdKZ%2BaEPUtHEJwX63%2BjMf&X-Amz-Signature=90251bebec8f4e8f2daf100f563316405826af4b186022d08e856ed8c664bf4c&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SU37HCR%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIBWgDqs0HuSk8tzphfUR%2FIolCBFpP5IIWsRPb2fDPTtPAiEAkXhfvaG27lAECw%2BP74Ncu%2Fq7l1wykBwBvkFnEU%2FyAtUqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDElgkEhhJQ48og7AIyrcA1fQ%2F9Iq6aSHRf0gN8UfX6ADQCu6L1mAFvScH8YY2Oh7Wz8fzr2gAm6zwZCPmax0KJjKAq5qui7uQyv3hhwJd%2F0tL78cnZV1dT3LmFJIkj1OhWZlKGY2Y1OGmPWlQyC3u66uS6jC6dMId30Ce7ypZb3jatV6b%2BjK8xtPFrPW6Nu5xO68qbhY%2BrHBHL6%2Bb%2B3sqefi9CDSnWvnlLOGDoNv7H299Cn6QmJR3siDaGxUpInJf%2FFJugnf4u%2Fi%2Br8KliFXFQsozkvsuRlG21ZwLoWgs5GdAxofu6BNbkT7lRCykrZRQXX4J6h4uT%2BdMQ%2BbIwH7vqQnFeGKD8XW8YjoSTuhthqBc9TH24MYRNwbb81J4gJJsJdmiUd1ZD171EJLfk%2FyrqCHVbr%2B9jnvkdfqz7orJgDdp2Vsdd2dHJkzHH6bu%2F72s3G1QxB99kRQqFcDyEAdRtfVYRW01X9Ya6bDpE3SfF%2FhmPqJogf8zf1Vxc6%2Fyp6uLWzJcFTOvX2%2Fm33vZ%2BHcEICvAged7IMweuqI3BbX5bvYVRzh38k30CV%2FLbsOXNpinzDlm1u6hLZvJpvGR23yBODZ0QDLqzWOmfg9Zid5xtXwSorjlmuMy7xKB4dxcj4hTbrAjpwwpvaCELKXMJW4jr4GOqUBsd6AGdPTYNxTFNNi7iOs8RJV%2BTzxaBfme5pMBQ0RavX2QPZfcSwkUSLllC7z3CrlhjD29vwldMS%2FsvOlDF%2BXc5VIV%2BmEQaLFqGm%2FQK4xfQ4Bo3tis3AIZnVajG5TnO9OI%2FZq7PxrBuzCUw%2BOZpGeVsyTDSv94KCrrYcwlb%2FsTCpXRXSlfCfbfLbU11erX%2BUqmvEwtpUHnC6mUeKTJ0MwD%2BA%2Be%2Fue&X-Amz-Signature=f309cf9f603a89cc772f0ce77fb011bd2fae3b8739daaa1b10d0a60bc08eac27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMDKSSK%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDbnzZ8WqZF82%2Bv42VOIr0zuFwHoW5tCmuNuePUE3qyegIgAqsw9KZ8k5X6l5su%2B9XUzo0zDA9Q8gRu2AbtJS1HvEgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgmBQpyXDXmBx4hmyrcA6tsRPftjT%2BNbljnrGML9vuKvR1b9pNMjXyVSPetRq%2F1vlY5F5%2FYvHzRYIyxH46his8qhpXL84cgdyNYrWgjyrxOjgdQ2hjl6jW51ZLLmXKJoNAsigJPp%2BlsulPzHPJ1Oxor2tWuy7zsT4aZ%2BBc2g7W%2FMnImAZWfz7YQKxu39Nu6InPjfYlzVHaVZflhBzhbvOr2Y8TjOOAE3yDPl1T3LWrU%2BPtMTbbH58wHQbxzdq0gsOj%2BWJomLONGqmnSm%2FSgr2V3RxIq8fKF33877fvcGOgkfFTXqtaZXsEuqzqKhCImR9fkfs%2BXZuH3vrjSjl7mSCJzN0cM9X60hJZ7vCt81Rqf8mJk4JvWm3PtV9VtBW2k70u0%2BoKhh3Dza7%2FiUNvNuaQcFSoHQ9x9rKV1k95mYLdzRPNuxzXi8dROgJdyvpIl3vlAT09SIOsXGFncSG5PXT0ONA70lsGlCeU7F14c8S3Qtx1gr4BfO4T4EpFXWjARmtKX4kEJDL4zx2ybEIOyf03r55gnhAE8uzaOMSe2iZ6ysdw5X9cIYZTKbR5H8nzbvmHsSkyDwvxf3c8suiPeuOovfgq%2BZxyAKWC9d0ZqXufuJ%2Bi2djWvr0L7fibuD%2FCGItm%2Bd%2BSSTM11N1xBMIa4jr4GOqUBnYY8cvVxIhlESLGkphsl%2FYSJY1bUXF%2BmCoIEYySvt5N8wFuznSEazC0XP77C0fW89NsFb82ghsDOi3PzsuT9A6d0c01hqYY1oJk1vLJXe4ddzW5CafB6K91GJJvrGzekOn3y3gnLFtZ4HY%2BCTrmj8x7a2HKrLiHVHs8znJ7LaDFI5JHh%2F2bCcG4sqScMpz%2BgclyTTBV5qp5ww2iOpUQVoMA7sXnT&X-Amz-Signature=a2b9b52296fb16339682be04da331079ec5281c6fc18065d5bee55d8c023721b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMDKSSK%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDbnzZ8WqZF82%2Bv42VOIr0zuFwHoW5tCmuNuePUE3qyegIgAqsw9KZ8k5X6l5su%2B9XUzo0zDA9Q8gRu2AbtJS1HvEgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgmBQpyXDXmBx4hmyrcA6tsRPftjT%2BNbljnrGML9vuKvR1b9pNMjXyVSPetRq%2F1vlY5F5%2FYvHzRYIyxH46his8qhpXL84cgdyNYrWgjyrxOjgdQ2hjl6jW51ZLLmXKJoNAsigJPp%2BlsulPzHPJ1Oxor2tWuy7zsT4aZ%2BBc2g7W%2FMnImAZWfz7YQKxu39Nu6InPjfYlzVHaVZflhBzhbvOr2Y8TjOOAE3yDPl1T3LWrU%2BPtMTbbH58wHQbxzdq0gsOj%2BWJomLONGqmnSm%2FSgr2V3RxIq8fKF33877fvcGOgkfFTXqtaZXsEuqzqKhCImR9fkfs%2BXZuH3vrjSjl7mSCJzN0cM9X60hJZ7vCt81Rqf8mJk4JvWm3PtV9VtBW2k70u0%2BoKhh3Dza7%2FiUNvNuaQcFSoHQ9x9rKV1k95mYLdzRPNuxzXi8dROgJdyvpIl3vlAT09SIOsXGFncSG5PXT0ONA70lsGlCeU7F14c8S3Qtx1gr4BfO4T4EpFXWjARmtKX4kEJDL4zx2ybEIOyf03r55gnhAE8uzaOMSe2iZ6ysdw5X9cIYZTKbR5H8nzbvmHsSkyDwvxf3c8suiPeuOovfgq%2BZxyAKWC9d0ZqXufuJ%2Bi2djWvr0L7fibuD%2FCGItm%2Bd%2BSSTM11N1xBMIa4jr4GOqUBnYY8cvVxIhlESLGkphsl%2FYSJY1bUXF%2BmCoIEYySvt5N8wFuznSEazC0XP77C0fW89NsFb82ghsDOi3PzsuT9A6d0c01hqYY1oJk1vLJXe4ddzW5CafB6K91GJJvrGzekOn3y3gnLFtZ4HY%2BCTrmj8x7a2HKrLiHVHs8znJ7LaDFI5JHh%2F2bCcG4sqScMpz%2BgclyTTBV5qp5ww2iOpUQVoMA7sXnT&X-Amz-Signature=cdccc945e9c60d4caa2dd0a5ca92e98c997bd475e10ef6df230f88caff16ba50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMDKSSK%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDbnzZ8WqZF82%2Bv42VOIr0zuFwHoW5tCmuNuePUE3qyegIgAqsw9KZ8k5X6l5su%2B9XUzo0zDA9Q8gRu2AbtJS1HvEgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgmBQpyXDXmBx4hmyrcA6tsRPftjT%2BNbljnrGML9vuKvR1b9pNMjXyVSPetRq%2F1vlY5F5%2FYvHzRYIyxH46his8qhpXL84cgdyNYrWgjyrxOjgdQ2hjl6jW51ZLLmXKJoNAsigJPp%2BlsulPzHPJ1Oxor2tWuy7zsT4aZ%2BBc2g7W%2FMnImAZWfz7YQKxu39Nu6InPjfYlzVHaVZflhBzhbvOr2Y8TjOOAE3yDPl1T3LWrU%2BPtMTbbH58wHQbxzdq0gsOj%2BWJomLONGqmnSm%2FSgr2V3RxIq8fKF33877fvcGOgkfFTXqtaZXsEuqzqKhCImR9fkfs%2BXZuH3vrjSjl7mSCJzN0cM9X60hJZ7vCt81Rqf8mJk4JvWm3PtV9VtBW2k70u0%2BoKhh3Dza7%2FiUNvNuaQcFSoHQ9x9rKV1k95mYLdzRPNuxzXi8dROgJdyvpIl3vlAT09SIOsXGFncSG5PXT0ONA70lsGlCeU7F14c8S3Qtx1gr4BfO4T4EpFXWjARmtKX4kEJDL4zx2ybEIOyf03r55gnhAE8uzaOMSe2iZ6ysdw5X9cIYZTKbR5H8nzbvmHsSkyDwvxf3c8suiPeuOovfgq%2BZxyAKWC9d0ZqXufuJ%2Bi2djWvr0L7fibuD%2FCGItm%2Bd%2BSSTM11N1xBMIa4jr4GOqUBnYY8cvVxIhlESLGkphsl%2FYSJY1bUXF%2BmCoIEYySvt5N8wFuznSEazC0XP77C0fW89NsFb82ghsDOi3PzsuT9A6d0c01hqYY1oJk1vLJXe4ddzW5CafB6K91GJJvrGzekOn3y3gnLFtZ4HY%2BCTrmj8x7a2HKrLiHVHs8znJ7LaDFI5JHh%2F2bCcG4sqScMpz%2BgclyTTBV5qp5ww2iOpUQVoMA7sXnT&X-Amz-Signature=8fd5a1a2948765f83eff6059f4f40aba203f09ca730ab63a2e9b381aac60aa4d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627KTK4J6%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDlC1FwlTMpD%2B5222iaxzqp1gRbqhTwWat5bpJpTHEj0QIgc6lHvV6pMyL31f5%2BDbPnDwz21ArUkHdvmI0Vry3ENo4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBbgmCIT%2BQc2M%2FWw9SrcA95hyS4aPEzLRgpl4CKcFB49d8mzEDhqZKQuxtFoBy6aygCtTOl%2FrtZo1q4TNbgFeGUeo41Cm%2BUrO92%2BDcfgSi9cNRfuRM8MYnOt8EpmRsV3t54HYt1wlQvCvHBIoSHo843ysZsu7cntPGD4D%2FzFl4VyMQH1AWq1Bw%2BPI9zFU%2B6ZBb%2FD%2B5B837rywi8vXSDYK5xVnB6j6%2FK0cDaKzSDWbi4mOw06nsvMGMMphy7dTCrp2HnG%2BthhuVqXxpNEqfr6OKZ0c7vSOTDNSDwBEHoZp1bg%2Bjc%2FJAEZ8yGm1HR21X7vdL6gPQAKAe7MjSgv%2B3JrCeprotM65G96JNmKZpQdAFU3JivXL2xVCdPuo2IETPY%2BOONXbVEmTgyz96MpTgMAb8ng83Ry0WWI9hCPsJiJ8G7x7VK9sX4b%2BMSvfl0AmjRE0jx4tCCUWkmlcl%2BXBtYyUNuUaNAI7Hm3BxXo%2F6ZO%2FYDpL4iBnIf%2FN0khE3LTYJiO4%2BVOIotM8VQaf0K5aknjyi0uZEGuuek9MgbiHUd5DWGWTEVBwbeJ71PthS8F5jXeTe71Gzhz078yYtu1tEzpTSDd9P7N91Vy2ZlQRltDaJAZ%2BhBkMRbo%2BYSgLkDoUQ9%2BCsX3T4zz0OqdulYJMOi3jr4GOqUBIT%2Bjaw0S7ltKLToUh1UKimf4NDenRBCMsg69DqMVw%2BkDrHh9N6s1O4UQ8dFyBb7WuF4kYp7XYaB0lZnyf69CzZO%2BGu4%2BZsWZXJfDfqG23EiSSeeV8z6aGpyXnu04AFd3PmFHVGjw01R%2F%2BsFQFJhlD1NbmMyc0mBb6xZ%2FZf8PHbz598Nol7jejN1gZcyUy4P8XDorYalu5DfFDx4lb7gDo1eOe7gM&X-Amz-Signature=627e3fca06c0777a590cbc5166cbc611d104dbff846a6a28f1cb8f19a2c95169&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUH3B6PG%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQC8dxErSwRvUzqkaQdRU18c6CKuCBDiVcL1d%2F6Rw3TMHgIgahZKpSdGIotdtK9PzmQcVsRwyqBv0SJewuCE%2BMsQil8qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMf6JgFoRT7ZM8zU2yrcAy%2BKHkQ2puedoy4rFOI0SJDD9v%2FdGMBY1oI7PDLDKN80ndQPuBSGBpuPZy7TarbzTpmS8XjF%2F8URL2fsX0eFjgyhl0cLcwUJaIYdADaYNB2Y7jQ2cV5zTfr4dWy%2FFwiLf6olQlZGd07HWQseiElfj08%2F%2FbT8qoyqKcr4t1vbuqfXKjmWiHy5zk8WQAOTSoExh%2B2XYF5FIGMvWtHRpfuXrH%2BdS%2BJgt4VgIqFS%2F7mEQjGC93WF%2FLej9l62VOJU9lh25OR%2BEqgXSYjpqweHv6cjujRXI5%2FUSMU4IyfKQi1RGz0teRe2odpGEXPTQ9UxYYAqJKtqFSRsaKwr85SiCKDd26EHMUAycfmzQCLr4RSC2v1Eo49fLiF1cvw8ePJMu9EMMFnEZJu4mgwt7GGJkS2xy0BbOjAnzfz2w0EZMF9doS%2Fxxsd5R3u1xFeO1zkzmtkRAzIoTlNE097IWmv%2Bn%2BaXStiD%2BWRJKJXfpotcH%2BW02Nh9ofCQtPLyqytDI6oK2ZV7bvDx48L4X95O6gG0CgbVJ%2FnUkrall1ONddfqVMqB5KXs6J36lJkgVyO1iGRTPBX2fK0VQtk5UnER9YZamiCJ1VbLPh%2FssmOOYrlSOdOuzxCqk%2FTeOFQGIcMyWZooMKW4jr4GOqUBqD1wRyjtp6Hfcku0Mfd0b9aGO7TkiIz2p4d8uKlUOZolGcO29XDi9l7%2Bs73ZiC5z98H1ynSB%2FazXT2BdpGMntOlvD81cROEJa0cszuTb2wlM%2Fy94yzcPJObvaWjAcBB%2BFFKMHyqnr3RVJM4pKOwc%2FQChoIHCUvcTcR5nKeD1wnM2hDz8I5HFOIBcjsvyvudMiwtrdXWfE5vu%2F6k5%2Bh3TVW2OgKKE&X-Amz-Signature=2ce8bc39ed65498849b8ce2e65d00761ba34e17e423860b825debe7123c4f227&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RHULDUV%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIAFyZIaxxkYbZeLf6d8phe1WDDy2X%2BFHquyvljLB6ZK2AiEAhLiigqdNyB3vjbBu%2BIRS4Z%2B3tOXrTvKwMdTkBGFfJ8MqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCHf4ng1UaRcirShMCrcA8MI1U3N29bp6VPuiFJsOfZuhipK%2Bp5GKh7ekGJZeljvpOOx0K0jOVI3mwNa%2FOgHa3cMbnGEJvfb9804MYLALbTimXKOMgXdXzSTvHwx8xzjibLrf4X8BRkRkZNXQlZs88AyeUdf13qLhi9csRZJqG7ivv0dTbys9J13XvfyjzADXk2tsZlw7sA6Pcaa1Hbts4q5v2otUTAMAJMSkRNW9NdbmZ580nhnLlPUA6zwDhqi5uNhnxQKQDbqiFI4Zy%2BYG9FQU62ftcbJAT2DAARvmX5GZ4Ri4wAIIXBWrmDWi1v6cehWbbyM1bDcMnwMD8c4rYKqOiquD7L1UP%2FouzNt8FN81EMRQQHMQVFXCSLAANpmyTFMYVrbXFImomU0cabjciRzWVlY718ubbnBuS%2B4Uso8mWEyOl8ejbGBBzhipjEilJm10j1UdAC9o14oAfDEb9WD6%2BpSFtLqUyrFzCia8m52q2zMCv3z4wziAwd5CmWO0qZaoL4R0avmt3Dh3lSi%2FKnyviAvyF9XUm8McZidtcNsSyooRKjC7JvrybXKdG5bQ3Ii0mV2TxOT129OsDn2PtrfPsH5mmaluxCFKYWGkn8VuCbGGTW8H6YJv%2BQ2dk%2F76sYALY9f4zNcP7DiMOe3jr4GOqUBhumNkBIzzjEm4CQuwYcAjsAkqhl2hIVtecOoSG3ggDgKj3TQFeauZAy2gEbuqkAGqDxPJUB3ElPJNs43kw7vEm1epWQQdWhnt%2Fu62OMu3FLhRvkoXiFA1FvDXa0H8RmyU1UU79zI4tKhU2g2uD%2FBdi7eSgABue94QX8sFBTBY%2BA8ATlnA5dZBDuXnfNW3BwyksiTI6ABIpt6sDAfOFnCi%2Fu1ws%2Bv&X-Amz-Signature=b6e555c4de521d5e2e968b2fe3a45a9e27ad1a532d731c908b5076b620200643&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCRGCVSQ%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQC6Tbl5Qg5mqAW6iBM5HGr2qf9p66GkhlXpP22UWN%2B9qQIhAND768%2F4gYz2oOLmLofhULZZ7rJURjCe3khAju6Dj7itKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyQe1de6%2FMkjAm6kQq3AM7N8IrxYOtpd2cx3BK6dILg3N0CjVpZZmHTfx6xNGW5eEiTIUJtn4vTUUNiQPlAGY3DmtaBSxikpZys2KrlofQ6W%2F65Ag1%2FFAp%2FLCO44wVAZR582TrKRuyQ6xXhJArg88s8IP853yN4fkCodngLfPDUZf1NALHVgz1m8p%2BjUUqBn9KFubQ%2BHZto0hcRlncf%2FXLsFpcZjSSqfDrMEt1AxW1YaF2U70fG7IN4LUb1A8pN534Z%2BfZLbjkJSXG8KT90FcSKbi%2BJ6R5tvvr8vAKBUbkbSw3p0czDvxkAflLKxdariv2CDqWyGiJ0CmEfjaCg9g%2F8ZswU02%2FfUar88Xz6pdJNAIogwsp7w9fZqbhftlune8f%2BYGEP9mWzEsIsHDNpI6647K%2FcIgjp%2F0kNnDa8C6tgCiSNTv1fwEgBn%2Fd9nnhrpixOaSgykIhkAe0hjyNpAsMMevkqp4O6VcuuzUUIVstkMwQCIHSGUH4D7uhSHWZuhmV7QjQZRJRSqRbT9n%2FWVgg%2Fq0CuNP51StB9nehmFvLuhXaZteS2l4r8hivd2ZdRXUSDVHZZSyyPz%2B6CHdoZx5NoocHUn9oYrnagl4OdgMWRdXF2INBWRDCwrY%2BP7UGBZShOJiSgMaT%2F2MC5zCEuI6%2BBjqkAXB6vB9PGWfsfE%2BxaindwiCrTq14%2Bj5dJFzScbWDSIjM3ZX%2Bh8XEZjmmuGvBD1mL%2BmVlj41iukKc7h61T5zMolFJXBIWGtN2i3xxr27QhcbLO8IOoGEWeMNLTZJ2JgqHlm4GlnXNBo41sdlOaigPGcodUOaK%2B7rfe%2BlgkQPbs3mHuO29zBRW5tFd7Gag1pEbQAlMxoXm7IQg1ov9gK%2BWyR1GmrR9&X-Amz-Signature=7982df587225ef37ab1f10e209705f87851c29a2bb52763862890cad9b9804de&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCRGCVSQ%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQC6Tbl5Qg5mqAW6iBM5HGr2qf9p66GkhlXpP22UWN%2B9qQIhAND768%2F4gYz2oOLmLofhULZZ7rJURjCe3khAju6Dj7itKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyQe1de6%2FMkjAm6kQq3AM7N8IrxYOtpd2cx3BK6dILg3N0CjVpZZmHTfx6xNGW5eEiTIUJtn4vTUUNiQPlAGY3DmtaBSxikpZys2KrlofQ6W%2F65Ag1%2FFAp%2FLCO44wVAZR582TrKRuyQ6xXhJArg88s8IP853yN4fkCodngLfPDUZf1NALHVgz1m8p%2BjUUqBn9KFubQ%2BHZto0hcRlncf%2FXLsFpcZjSSqfDrMEt1AxW1YaF2U70fG7IN4LUb1A8pN534Z%2BfZLbjkJSXG8KT90FcSKbi%2BJ6R5tvvr8vAKBUbkbSw3p0czDvxkAflLKxdariv2CDqWyGiJ0CmEfjaCg9g%2F8ZswU02%2FfUar88Xz6pdJNAIogwsp7w9fZqbhftlune8f%2BYGEP9mWzEsIsHDNpI6647K%2FcIgjp%2F0kNnDa8C6tgCiSNTv1fwEgBn%2Fd9nnhrpixOaSgykIhkAe0hjyNpAsMMevkqp4O6VcuuzUUIVstkMwQCIHSGUH4D7uhSHWZuhmV7QjQZRJRSqRbT9n%2FWVgg%2Fq0CuNP51StB9nehmFvLuhXaZteS2l4r8hivd2ZdRXUSDVHZZSyyPz%2B6CHdoZx5NoocHUn9oYrnagl4OdgMWRdXF2INBWRDCwrY%2BP7UGBZShOJiSgMaT%2F2MC5zCEuI6%2BBjqkAXB6vB9PGWfsfE%2BxaindwiCrTq14%2Bj5dJFzScbWDSIjM3ZX%2Bh8XEZjmmuGvBD1mL%2BmVlj41iukKc7h61T5zMolFJXBIWGtN2i3xxr27QhcbLO8IOoGEWeMNLTZJ2JgqHlm4GlnXNBo41sdlOaigPGcodUOaK%2B7rfe%2BlgkQPbs3mHuO29zBRW5tFd7Gag1pEbQAlMxoXm7IQg1ov9gK%2BWyR1GmrR9&X-Amz-Signature=c20a8032249dba8b7df790314ce46b9a3c052feb28171265a3e7a6f88dc0712f&X-Amz-SignedHeaders=host&x-id=GetObject)

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
