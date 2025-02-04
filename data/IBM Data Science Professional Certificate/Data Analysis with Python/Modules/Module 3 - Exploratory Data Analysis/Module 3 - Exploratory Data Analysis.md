

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWEQDGCW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIDLW7%2BT2eoCJNwGaaoLNw9zXMvcGYfBV6fGZVW4GdCR6AiBSC9TZsLocw2cP0v0RgWWZgkvOC%2FRLRQNRVx%2Fmpwag5yr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMHk3JE%2BHeraDhIATwKtwDygCibbIGZvdp%2Fc7lqyaOiI6z%2BgIjnSPl5S%2Bohabv6AdYV1Pg3%2FvVtYpyuASWxrWjwChvK%2FswH5m8toOZfpYmHBdDGqj62RAYv9H5yGmWAUrDJkqymXwruNVhNEWr54bly3GcpBJ%2BpBaxAKNbbVvRxz5Cr8Rm8BxyzkXzdfo27qHWQfbnL1aOYK1VAYGPlSxbmIc2adGajFjRyIMFIJy1grjzDr47xlGKkWFgxngIjZQzwhLqbY2LEMJNVbfDvCTJcxDamlcj53j1Xwefm7m8RkfKRgtlkg4IhhvRW5wq8BgzvMx7nwVweIioVulvEAXw%2FKQXASBR8iV%2FnWyVb2PMxz%2BCzvjgsCony4QZFNlLTd2LE5vEH%2FYW2kpNwe%2FRq0vRuamfLBu7iZVI6o67PkpfajlakcP8fTRpOzDUt8%2By4FzCB4eIRHueyXxPrUVh7%2FLStJSGkjzJVTSjDgvzSerBTet48CeydcnYOetDB3SmbEVJJNlX9z9MNC%2Be7fE%2BklSn%2BLRZEfvrf%2FooLxAuu4VqH1VvaOzE%2BpZmsebLrvwb5KhWLRb2ix8oVFeAsQPyUntxuuIJ7vn6kuaL%2BdS%2B9Q9yNA9AQFx9ZK714bOqOBMjHjZzupVSxe%2FYfHD1UM4w%2FuWHvQY6pgEXFWyRz74SRorZB0kbvuY6O0NeMUTFywVyyv6fmkZBpWKYQcjG2Xd20XUg7cNX%2BfGFb%2BS1EVgax%2FYnu2Gj7OAffboY6bOKs6M5Wj%2BhYBtN5%2Fyk5a2aqftp%2B%2B52a8ZbkB7dktdhlL6b5aWZARNTU7ORE%2BcpVqPkooUgFFZumSQ70l6whTSB%2BsHrYWNCUua4g39EnM7faCja3U42JsoE3Xbj6trCTOe%2F&X-Amz-Signature=53833fecaf7d2c82fe9afe92edef4652c07749b680c770a655ef6f15ab40ca27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWEQDGCW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIDLW7%2BT2eoCJNwGaaoLNw9zXMvcGYfBV6fGZVW4GdCR6AiBSC9TZsLocw2cP0v0RgWWZgkvOC%2FRLRQNRVx%2Fmpwag5yr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMHk3JE%2BHeraDhIATwKtwDygCibbIGZvdp%2Fc7lqyaOiI6z%2BgIjnSPl5S%2Bohabv6AdYV1Pg3%2FvVtYpyuASWxrWjwChvK%2FswH5m8toOZfpYmHBdDGqj62RAYv9H5yGmWAUrDJkqymXwruNVhNEWr54bly3GcpBJ%2BpBaxAKNbbVvRxz5Cr8Rm8BxyzkXzdfo27qHWQfbnL1aOYK1VAYGPlSxbmIc2adGajFjRyIMFIJy1grjzDr47xlGKkWFgxngIjZQzwhLqbY2LEMJNVbfDvCTJcxDamlcj53j1Xwefm7m8RkfKRgtlkg4IhhvRW5wq8BgzvMx7nwVweIioVulvEAXw%2FKQXASBR8iV%2FnWyVb2PMxz%2BCzvjgsCony4QZFNlLTd2LE5vEH%2FYW2kpNwe%2FRq0vRuamfLBu7iZVI6o67PkpfajlakcP8fTRpOzDUt8%2By4FzCB4eIRHueyXxPrUVh7%2FLStJSGkjzJVTSjDgvzSerBTet48CeydcnYOetDB3SmbEVJJNlX9z9MNC%2Be7fE%2BklSn%2BLRZEfvrf%2FooLxAuu4VqH1VvaOzE%2BpZmsebLrvwb5KhWLRb2ix8oVFeAsQPyUntxuuIJ7vn6kuaL%2BdS%2B9Q9yNA9AQFx9ZK714bOqOBMjHjZzupVSxe%2FYfHD1UM4w%2FuWHvQY6pgEXFWyRz74SRorZB0kbvuY6O0NeMUTFywVyyv6fmkZBpWKYQcjG2Xd20XUg7cNX%2BfGFb%2BS1EVgax%2FYnu2Gj7OAffboY6bOKs6M5Wj%2BhYBtN5%2Fyk5a2aqftp%2B%2B52a8ZbkB7dktdhlL6b5aWZARNTU7ORE%2BcpVqPkooUgFFZumSQ70l6whTSB%2BsHrYWNCUua4g39EnM7faCja3U42JsoE3Xbj6trCTOe%2F&X-Amz-Signature=c37a29de1a4681f6f1d2e3c6d1b21f2fe57139740738f17e269e714f3b75e8f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWEQDGCW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIDLW7%2BT2eoCJNwGaaoLNw9zXMvcGYfBV6fGZVW4GdCR6AiBSC9TZsLocw2cP0v0RgWWZgkvOC%2FRLRQNRVx%2Fmpwag5yr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMHk3JE%2BHeraDhIATwKtwDygCibbIGZvdp%2Fc7lqyaOiI6z%2BgIjnSPl5S%2Bohabv6AdYV1Pg3%2FvVtYpyuASWxrWjwChvK%2FswH5m8toOZfpYmHBdDGqj62RAYv9H5yGmWAUrDJkqymXwruNVhNEWr54bly3GcpBJ%2BpBaxAKNbbVvRxz5Cr8Rm8BxyzkXzdfo27qHWQfbnL1aOYK1VAYGPlSxbmIc2adGajFjRyIMFIJy1grjzDr47xlGKkWFgxngIjZQzwhLqbY2LEMJNVbfDvCTJcxDamlcj53j1Xwefm7m8RkfKRgtlkg4IhhvRW5wq8BgzvMx7nwVweIioVulvEAXw%2FKQXASBR8iV%2FnWyVb2PMxz%2BCzvjgsCony4QZFNlLTd2LE5vEH%2FYW2kpNwe%2FRq0vRuamfLBu7iZVI6o67PkpfajlakcP8fTRpOzDUt8%2By4FzCB4eIRHueyXxPrUVh7%2FLStJSGkjzJVTSjDgvzSerBTet48CeydcnYOetDB3SmbEVJJNlX9z9MNC%2Be7fE%2BklSn%2BLRZEfvrf%2FooLxAuu4VqH1VvaOzE%2BpZmsebLrvwb5KhWLRb2ix8oVFeAsQPyUntxuuIJ7vn6kuaL%2BdS%2B9Q9yNA9AQFx9ZK714bOqOBMjHjZzupVSxe%2FYfHD1UM4w%2FuWHvQY6pgEXFWyRz74SRorZB0kbvuY6O0NeMUTFywVyyv6fmkZBpWKYQcjG2Xd20XUg7cNX%2BfGFb%2BS1EVgax%2FYnu2Gj7OAffboY6bOKs6M5Wj%2BhYBtN5%2Fyk5a2aqftp%2B%2B52a8ZbkB7dktdhlL6b5aWZARNTU7ORE%2BcpVqPkooUgFFZumSQ70l6whTSB%2BsHrYWNCUua4g39EnM7faCja3U42JsoE3Xbj6trCTOe%2F&X-Amz-Signature=779f686513c01348f9aab9ac062cf6b71ded5da7529f5fbd5d70dfec08dda315&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTSU6GMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCKma8%2BxE1ZyM%2BX7xKY2NSEQJ%2FdXYDe2sIqp%2FUooG2z1gIgCtwAynjF7bHZns4bMuw3TCASwlprZ%2Bj1sMqgNBL2CpUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDAyB8fGhcCyOVPcvfCrcAz%2BL9VXCZYJMuq4MPohZFSdNVkWFujVyeVGjM7nWDh4tNW3Grg0bQ7Yoevwd3avkLood7TgSoX64i0hmM5GVnWpkPlN2wecUPUNi3r%2Fcn13MB%2Bqkw4dhCfaa18PPOCacJ%2Bu%2Bh8CPSwlxC00yWpY8vvSYliSSfQK7G3Xo%2Bk9Zq4MmQrdD26ruoBl%2FyUU5TVp1p8Fav5RkKgWYVY3HBWXw9QAzFrmArkEFlrm5f73qwgPRmqE9KpYXbmmtAT9%2BJV7dr6ieWMHlfQ3NlIrflAPkahpJl1fjICGuE0cSAhDvTBo2r3EkyBhK4pu7E%2FfYCTPxWmz4kNftV1yGQ0M%2Fw%2Fb%2F44WFW7YUgEZFZVrd5T2HxRLiDK5Ep%2FDaKDNTu71E1ALetpg9Yf%2FnyXHWNbqOXiitInwacQtn%2FAaLOwRAxHHcY7dTSEXRL9%2FHZGSHRobTWQX7oreqtGMuuzUgVAS3uyF6MBYo4I9mcjVhryj1mNJkewP0mi4GrsSb9q%2BySq63DXwYKRQo8j3KjIoU0peplnhW%2Ftfi7GxK4RdTwUcFw3%2FFGbFlvDsVkrSw8H3o69qzoIWPicIX6Vdq0FSDX4eu65tUe1q1328Ox%2BevPS4y5L0D4mXg7WQlrlIyYlhvYpgXMJjmh70GOqUBt6Eas7kaHTWjmngT68S1qEttEMIf%2B6Bh8FnB1%2BML1srTw%2BsWDYXAbA%2FSl8sOkl7TIpj4BzY98OC5x9iypBbx1%2BB1VI3tA6OXVX8b2%2BWwUZ1mgJqm56ZlozivRqCGVFdtrg0E7J92mj8fgOp8V%2Fhb681DdTluGrs8Bx2Ph4XJg1YUxPIuc9ssJIfyUh8DJYRxqU7ihib%2FF4Nob9tq5PlU%2BzEMKvKj&X-Amz-Signature=052c00f5a7911e3b5a9758f5109e8d18df7c99e920ad394aef82eebca973e569&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTSU6GMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCKma8%2BxE1ZyM%2BX7xKY2NSEQJ%2FdXYDe2sIqp%2FUooG2z1gIgCtwAynjF7bHZns4bMuw3TCASwlprZ%2Bj1sMqgNBL2CpUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDAyB8fGhcCyOVPcvfCrcAz%2BL9VXCZYJMuq4MPohZFSdNVkWFujVyeVGjM7nWDh4tNW3Grg0bQ7Yoevwd3avkLood7TgSoX64i0hmM5GVnWpkPlN2wecUPUNi3r%2Fcn13MB%2Bqkw4dhCfaa18PPOCacJ%2Bu%2Bh8CPSwlxC00yWpY8vvSYliSSfQK7G3Xo%2Bk9Zq4MmQrdD26ruoBl%2FyUU5TVp1p8Fav5RkKgWYVY3HBWXw9QAzFrmArkEFlrm5f73qwgPRmqE9KpYXbmmtAT9%2BJV7dr6ieWMHlfQ3NlIrflAPkahpJl1fjICGuE0cSAhDvTBo2r3EkyBhK4pu7E%2FfYCTPxWmz4kNftV1yGQ0M%2Fw%2Fb%2F44WFW7YUgEZFZVrd5T2HxRLiDK5Ep%2FDaKDNTu71E1ALetpg9Yf%2FnyXHWNbqOXiitInwacQtn%2FAaLOwRAxHHcY7dTSEXRL9%2FHZGSHRobTWQX7oreqtGMuuzUgVAS3uyF6MBYo4I9mcjVhryj1mNJkewP0mi4GrsSb9q%2BySq63DXwYKRQo8j3KjIoU0peplnhW%2Ftfi7GxK4RdTwUcFw3%2FFGbFlvDsVkrSw8H3o69qzoIWPicIX6Vdq0FSDX4eu65tUe1q1328Ox%2BevPS4y5L0D4mXg7WQlrlIyYlhvYpgXMJjmh70GOqUBt6Eas7kaHTWjmngT68S1qEttEMIf%2B6Bh8FnB1%2BML1srTw%2BsWDYXAbA%2FSl8sOkl7TIpj4BzY98OC5x9iypBbx1%2BB1VI3tA6OXVX8b2%2BWwUZ1mgJqm56ZlozivRqCGVFdtrg0E7J92mj8fgOp8V%2Fhb681DdTluGrs8Bx2Ph4XJg1YUxPIuc9ssJIfyUh8DJYRxqU7ihib%2FF4Nob9tq5PlU%2BzEMKvKj&X-Amz-Signature=73be438c26c507a7b2ec276a0b29ee45fadfc71fd76c2abe96f2d4ae2b8528c0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTSU6GMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCKma8%2BxE1ZyM%2BX7xKY2NSEQJ%2FdXYDe2sIqp%2FUooG2z1gIgCtwAynjF7bHZns4bMuw3TCASwlprZ%2Bj1sMqgNBL2CpUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDAyB8fGhcCyOVPcvfCrcAz%2BL9VXCZYJMuq4MPohZFSdNVkWFujVyeVGjM7nWDh4tNW3Grg0bQ7Yoevwd3avkLood7TgSoX64i0hmM5GVnWpkPlN2wecUPUNi3r%2Fcn13MB%2Bqkw4dhCfaa18PPOCacJ%2Bu%2Bh8CPSwlxC00yWpY8vvSYliSSfQK7G3Xo%2Bk9Zq4MmQrdD26ruoBl%2FyUU5TVp1p8Fav5RkKgWYVY3HBWXw9QAzFrmArkEFlrm5f73qwgPRmqE9KpYXbmmtAT9%2BJV7dr6ieWMHlfQ3NlIrflAPkahpJl1fjICGuE0cSAhDvTBo2r3EkyBhK4pu7E%2FfYCTPxWmz4kNftV1yGQ0M%2Fw%2Fb%2F44WFW7YUgEZFZVrd5T2HxRLiDK5Ep%2FDaKDNTu71E1ALetpg9Yf%2FnyXHWNbqOXiitInwacQtn%2FAaLOwRAxHHcY7dTSEXRL9%2FHZGSHRobTWQX7oreqtGMuuzUgVAS3uyF6MBYo4I9mcjVhryj1mNJkewP0mi4GrsSb9q%2BySq63DXwYKRQo8j3KjIoU0peplnhW%2Ftfi7GxK4RdTwUcFw3%2FFGbFlvDsVkrSw8H3o69qzoIWPicIX6Vdq0FSDX4eu65tUe1q1328Ox%2BevPS4y5L0D4mXg7WQlrlIyYlhvYpgXMJjmh70GOqUBt6Eas7kaHTWjmngT68S1qEttEMIf%2B6Bh8FnB1%2BML1srTw%2BsWDYXAbA%2FSl8sOkl7TIpj4BzY98OC5x9iypBbx1%2BB1VI3tA6OXVX8b2%2BWwUZ1mgJqm56ZlozivRqCGVFdtrg0E7J92mj8fgOp8V%2Fhb681DdTluGrs8Bx2Ph4XJg1YUxPIuc9ssJIfyUh8DJYRxqU7ihib%2FF4Nob9tq5PlU%2BzEMKvKj&X-Amz-Signature=8c80b058206ea646dbe3bc115ca65f017a918a067af91fc22ff8d34dd4a63b53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTSU6GMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCKma8%2BxE1ZyM%2BX7xKY2NSEQJ%2FdXYDe2sIqp%2FUooG2z1gIgCtwAynjF7bHZns4bMuw3TCASwlprZ%2Bj1sMqgNBL2CpUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDAyB8fGhcCyOVPcvfCrcAz%2BL9VXCZYJMuq4MPohZFSdNVkWFujVyeVGjM7nWDh4tNW3Grg0bQ7Yoevwd3avkLood7TgSoX64i0hmM5GVnWpkPlN2wecUPUNi3r%2Fcn13MB%2Bqkw4dhCfaa18PPOCacJ%2Bu%2Bh8CPSwlxC00yWpY8vvSYliSSfQK7G3Xo%2Bk9Zq4MmQrdD26ruoBl%2FyUU5TVp1p8Fav5RkKgWYVY3HBWXw9QAzFrmArkEFlrm5f73qwgPRmqE9KpYXbmmtAT9%2BJV7dr6ieWMHlfQ3NlIrflAPkahpJl1fjICGuE0cSAhDvTBo2r3EkyBhK4pu7E%2FfYCTPxWmz4kNftV1yGQ0M%2Fw%2Fb%2F44WFW7YUgEZFZVrd5T2HxRLiDK5Ep%2FDaKDNTu71E1ALetpg9Yf%2FnyXHWNbqOXiitInwacQtn%2FAaLOwRAxHHcY7dTSEXRL9%2FHZGSHRobTWQX7oreqtGMuuzUgVAS3uyF6MBYo4I9mcjVhryj1mNJkewP0mi4GrsSb9q%2BySq63DXwYKRQo8j3KjIoU0peplnhW%2Ftfi7GxK4RdTwUcFw3%2FFGbFlvDsVkrSw8H3o69qzoIWPicIX6Vdq0FSDX4eu65tUe1q1328Ox%2BevPS4y5L0D4mXg7WQlrlIyYlhvYpgXMJjmh70GOqUBt6Eas7kaHTWjmngT68S1qEttEMIf%2B6Bh8FnB1%2BML1srTw%2BsWDYXAbA%2FSl8sOkl7TIpj4BzY98OC5x9iypBbx1%2BB1VI3tA6OXVX8b2%2BWwUZ1mgJqm56ZlozivRqCGVFdtrg0E7J92mj8fgOp8V%2Fhb681DdTluGrs8Bx2Ph4XJg1YUxPIuc9ssJIfyUh8DJYRxqU7ihib%2FF4Nob9tq5PlU%2BzEMKvKj&X-Amz-Signature=64c02f617d270f584f58b53e4db0fe74e18184e28eb0a659d857e774d88dc08d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTSU6GMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCKma8%2BxE1ZyM%2BX7xKY2NSEQJ%2FdXYDe2sIqp%2FUooG2z1gIgCtwAynjF7bHZns4bMuw3TCASwlprZ%2Bj1sMqgNBL2CpUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDAyB8fGhcCyOVPcvfCrcAz%2BL9VXCZYJMuq4MPohZFSdNVkWFujVyeVGjM7nWDh4tNW3Grg0bQ7Yoevwd3avkLood7TgSoX64i0hmM5GVnWpkPlN2wecUPUNi3r%2Fcn13MB%2Bqkw4dhCfaa18PPOCacJ%2Bu%2Bh8CPSwlxC00yWpY8vvSYliSSfQK7G3Xo%2Bk9Zq4MmQrdD26ruoBl%2FyUU5TVp1p8Fav5RkKgWYVY3HBWXw9QAzFrmArkEFlrm5f73qwgPRmqE9KpYXbmmtAT9%2BJV7dr6ieWMHlfQ3NlIrflAPkahpJl1fjICGuE0cSAhDvTBo2r3EkyBhK4pu7E%2FfYCTPxWmz4kNftV1yGQ0M%2Fw%2Fb%2F44WFW7YUgEZFZVrd5T2HxRLiDK5Ep%2FDaKDNTu71E1ALetpg9Yf%2FnyXHWNbqOXiitInwacQtn%2FAaLOwRAxHHcY7dTSEXRL9%2FHZGSHRobTWQX7oreqtGMuuzUgVAS3uyF6MBYo4I9mcjVhryj1mNJkewP0mi4GrsSb9q%2BySq63DXwYKRQo8j3KjIoU0peplnhW%2Ftfi7GxK4RdTwUcFw3%2FFGbFlvDsVkrSw8H3o69qzoIWPicIX6Vdq0FSDX4eu65tUe1q1328Ox%2BevPS4y5L0D4mXg7WQlrlIyYlhvYpgXMJjmh70GOqUBt6Eas7kaHTWjmngT68S1qEttEMIf%2B6Bh8FnB1%2BML1srTw%2BsWDYXAbA%2FSl8sOkl7TIpj4BzY98OC5x9iypBbx1%2BB1VI3tA6OXVX8b2%2BWwUZ1mgJqm56ZlozivRqCGVFdtrg0E7J92mj8fgOp8V%2Fhb681DdTluGrs8Bx2Ph4XJg1YUxPIuc9ssJIfyUh8DJYRxqU7ihib%2FF4Nob9tq5PlU%2BzEMKvKj&X-Amz-Signature=aa85accbbefdd7f4f2df0155f089bbce329c762c4d0dbf35f34bab5af6f769e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTSU6GMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCKma8%2BxE1ZyM%2BX7xKY2NSEQJ%2FdXYDe2sIqp%2FUooG2z1gIgCtwAynjF7bHZns4bMuw3TCASwlprZ%2Bj1sMqgNBL2CpUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDAyB8fGhcCyOVPcvfCrcAz%2BL9VXCZYJMuq4MPohZFSdNVkWFujVyeVGjM7nWDh4tNW3Grg0bQ7Yoevwd3avkLood7TgSoX64i0hmM5GVnWpkPlN2wecUPUNi3r%2Fcn13MB%2Bqkw4dhCfaa18PPOCacJ%2Bu%2Bh8CPSwlxC00yWpY8vvSYliSSfQK7G3Xo%2Bk9Zq4MmQrdD26ruoBl%2FyUU5TVp1p8Fav5RkKgWYVY3HBWXw9QAzFrmArkEFlrm5f73qwgPRmqE9KpYXbmmtAT9%2BJV7dr6ieWMHlfQ3NlIrflAPkahpJl1fjICGuE0cSAhDvTBo2r3EkyBhK4pu7E%2FfYCTPxWmz4kNftV1yGQ0M%2Fw%2Fb%2F44WFW7YUgEZFZVrd5T2HxRLiDK5Ep%2FDaKDNTu71E1ALetpg9Yf%2FnyXHWNbqOXiitInwacQtn%2FAaLOwRAxHHcY7dTSEXRL9%2FHZGSHRobTWQX7oreqtGMuuzUgVAS3uyF6MBYo4I9mcjVhryj1mNJkewP0mi4GrsSb9q%2BySq63DXwYKRQo8j3KjIoU0peplnhW%2Ftfi7GxK4RdTwUcFw3%2FFGbFlvDsVkrSw8H3o69qzoIWPicIX6Vdq0FSDX4eu65tUe1q1328Ox%2BevPS4y5L0D4mXg7WQlrlIyYlhvYpgXMJjmh70GOqUBt6Eas7kaHTWjmngT68S1qEttEMIf%2B6Bh8FnB1%2BML1srTw%2BsWDYXAbA%2FSl8sOkl7TIpj4BzY98OC5x9iypBbx1%2BB1VI3tA6OXVX8b2%2BWwUZ1mgJqm56ZlozivRqCGVFdtrg0E7J92mj8fgOp8V%2Fhb681DdTluGrs8Bx2Ph4XJg1YUxPIuc9ssJIfyUh8DJYRxqU7ihib%2FF4Nob9tq5PlU%2BzEMKvKj&X-Amz-Signature=979b0fd88c14f8686d0e7a0c9b8747cb9d12c5d8fb362c6403dc564d521e7cd9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKQHP75R%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCVbBha%2FTeT89EJQ03XsszD9P2BLvSXxbqqnUILYh1W7gIgFvmDzFXaVpKArvi1HgOEpHYcBISI%2F62gYF0Yxbd%2BYt8q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNjw9ifGZsCruckovircA57wD3OVtiNK38gHyzEYK2%2BzpxVVYwlasbOyLLK3e%2FkT6r3PXWtPjMMSexpo107h8fPIWisHW4MomaoboF09rjr%2FHk9%2FZ5qSU%2FVG0XKDeliSuqJMzX1oaPUhSaMO5OJz7b3l%2FrWW0I8K58Z4WB1b%2FwcP4qaDcuFOEAE%2Fj2PR%2BAsYSCi7cwhoUAx%2B8eNtZkoNOl4qBM%2FS%2Bwd6WRbM5kyp%2F71rWX4S3wSBxQ0fcGnZ6KlInShN7%2Bmc75gLKlwieRKxCjHsEmuwM2R4wBr7%2FtQeq6WrkK5eIccb6cQoM4d9d4%2BjPEzkq6VGWCZY2kHCdADnnB%2FdVvyrJtiUBZmmL%2BzCdHU6gYa%2FtaL8e6xmjaAFIyRB59DSfXtnp4RC3zCyeMSKyWccW%2FlJRnggy19F5N2loEqenuuDDQk2EQ0v8RJNCx8juB9SWSGSG3Ms1QAgeiu2yASRMaGV4TAT%2Bc9Tp0NA6G9dpcDMheJGJY%2F6VRNbFD8W1vHgiLRN4tiFCfao5xgfPhtMZFMsWyGZN%2BnSRAD0vrQHvn3ZrB%2F%2FIQfVJLhnu1fKNOP7sH4v%2BpdeJ2yYpOb6PVOEC23z%2Bu5crwsIhCGncAtoZ7GoENUZ1R5wNdcRfAYshAg6DRSzeH5GM21mML7lh70GOqUBDLgFDFLzc5Rn%2FTR0cmLHNgD1Gri5Rso%2Fiz02khN8FzsV4g05ZslCcBgAd5llaa0We%2Ff1yvWJRaEwymAnEuWoXPnogt0GxvyhtTOZ8zvftqt9zqY%2F1%2FpXlrJVD5Ok96d8xu507cUTi%2BvkuiD51aL6xJ7y65hwF7aCUN%2FYjQ1oXxMTCRAcIp1bySewauSbBlf0pTwD9bFg4AoO20tjGBfj55dWoiI5&X-Amz-Signature=fa6ce6be653641d090978ccc1d03693417154a45db120c3920bfbf751d82a7cd&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLO2WVFP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIBfYJ%2FWHUupTXLvZBcX0c7KvM260rg37gIqdEXv6o83wAiBfAqtbW%2BR0h%2BB7DAVOsU9v1v%2Bo58%2BLZNnVUFlilw1N6yr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIM5Mmm5w46Nx4qLrVvKtwDAw08lOTjE%2FU4DeLFLWmCDmQl2Z2OhwUVxYnI6OOWWxc19Em5tJ9JwjVej63bARIjYmzKOKSp4nJSQ0cKBvG66zoLo%2Bqm1WBAUaF8BIB%2Ftq2EHod8fn9FDUWjZTedKxPQrIgOO4desJnagnANJSRWvRwUWZQXdxLHwP%2FtqClhqzS%2FtOEatrVI%2FzWuk4Fk2eKevYfoouKcHht9JU2wD1QzzGDn7A80I4mwe5pdxlKdRFXoUULhSi7KTSZfePYG05OqEjdWDh4aS%2FZxhZ1fLXjhybNtCH7rna%2BJRt6ORIU%2FEwhqn4DuO%2B%2FHYg79uf5n5CxMWFVW7otukpZaDKqlF%2BPvYGXQO3Vh8oAb2guUaHwk2biAkxRwLAEjPZPHEmq9EwtnAA2wy4vo6d2nZNoqM6Hi6NC9P5oxut7nLYK87Qf6eWnI4y9AUC5JCMFdVdExWMLXJKTnnvsYGQIAQte%2BAWvRJsi7NEgIt%2B4LELrVAEWref7D%2F0wMfYzU4onkCzOKt2ZRMfbTk0tgbjw3c01io%2FjO0cqxDq4R2qjhprcnXmDDlHjhYP8R8t2%2BurkRjwqjjS3ygaMU0059DgNR40QL58AOjll%2BYyLmslzkaGxyNURbligQwb%2B0zLIkqlXSFGww%2F%2BWHvQY6pgETM3A%2FYFlwU7lJqegUzuwns5nSCOvVF%2FcErC%2FnLQU%2Ft5XEmZGYB6jq3SG77ATVMA6yzkEyCfg9oUPUnpchKqpLxY1UjzUMXm56qzbRiGgOOdhN9TBA6hLMhNxzudVf0aZGgTbnV2iRXEj98QPxcT0sDnsfB7xtM298ENQ31SnyARu5uEvLJxD%2FdkmPAKYmBihzHPwuNDjSkLDtsrHxDRXRVdBgoRpK&X-Amz-Signature=99ca9c9461e6e99aa5d61a544d105c857d9df8aa93fecbb2fc073f27fc092821&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTSU6GMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCKma8%2BxE1ZyM%2BX7xKY2NSEQJ%2FdXYDe2sIqp%2FUooG2z1gIgCtwAynjF7bHZns4bMuw3TCASwlprZ%2Bj1sMqgNBL2CpUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDAyB8fGhcCyOVPcvfCrcAz%2BL9VXCZYJMuq4MPohZFSdNVkWFujVyeVGjM7nWDh4tNW3Grg0bQ7Yoevwd3avkLood7TgSoX64i0hmM5GVnWpkPlN2wecUPUNi3r%2Fcn13MB%2Bqkw4dhCfaa18PPOCacJ%2Bu%2Bh8CPSwlxC00yWpY8vvSYliSSfQK7G3Xo%2Bk9Zq4MmQrdD26ruoBl%2FyUU5TVp1p8Fav5RkKgWYVY3HBWXw9QAzFrmArkEFlrm5f73qwgPRmqE9KpYXbmmtAT9%2BJV7dr6ieWMHlfQ3NlIrflAPkahpJl1fjICGuE0cSAhDvTBo2r3EkyBhK4pu7E%2FfYCTPxWmz4kNftV1yGQ0M%2Fw%2Fb%2F44WFW7YUgEZFZVrd5T2HxRLiDK5Ep%2FDaKDNTu71E1ALetpg9Yf%2FnyXHWNbqOXiitInwacQtn%2FAaLOwRAxHHcY7dTSEXRL9%2FHZGSHRobTWQX7oreqtGMuuzUgVAS3uyF6MBYo4I9mcjVhryj1mNJkewP0mi4GrsSb9q%2BySq63DXwYKRQo8j3KjIoU0peplnhW%2Ftfi7GxK4RdTwUcFw3%2FFGbFlvDsVkrSw8H3o69qzoIWPicIX6Vdq0FSDX4eu65tUe1q1328Ox%2BevPS4y5L0D4mXg7WQlrlIyYlhvYpgXMJjmh70GOqUBt6Eas7kaHTWjmngT68S1qEttEMIf%2B6Bh8FnB1%2BML1srTw%2BsWDYXAbA%2FSl8sOkl7TIpj4BzY98OC5x9iypBbx1%2BB1VI3tA6OXVX8b2%2BWwUZ1mgJqm56ZlozivRqCGVFdtrg0E7J92mj8fgOp8V%2Fhb681DdTluGrs8Bx2Ph4XJg1YUxPIuc9ssJIfyUh8DJYRxqU7ihib%2FF4Nob9tq5PlU%2BzEMKvKj&X-Amz-Signature=0e43152b855a9449a12218094fffca72e12fee88115b7b70b3229e9f07265309&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTSU6GMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCKma8%2BxE1ZyM%2BX7xKY2NSEQJ%2FdXYDe2sIqp%2FUooG2z1gIgCtwAynjF7bHZns4bMuw3TCASwlprZ%2Bj1sMqgNBL2CpUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDAyB8fGhcCyOVPcvfCrcAz%2BL9VXCZYJMuq4MPohZFSdNVkWFujVyeVGjM7nWDh4tNW3Grg0bQ7Yoevwd3avkLood7TgSoX64i0hmM5GVnWpkPlN2wecUPUNi3r%2Fcn13MB%2Bqkw4dhCfaa18PPOCacJ%2Bu%2Bh8CPSwlxC00yWpY8vvSYliSSfQK7G3Xo%2Bk9Zq4MmQrdD26ruoBl%2FyUU5TVp1p8Fav5RkKgWYVY3HBWXw9QAzFrmArkEFlrm5f73qwgPRmqE9KpYXbmmtAT9%2BJV7dr6ieWMHlfQ3NlIrflAPkahpJl1fjICGuE0cSAhDvTBo2r3EkyBhK4pu7E%2FfYCTPxWmz4kNftV1yGQ0M%2Fw%2Fb%2F44WFW7YUgEZFZVrd5T2HxRLiDK5Ep%2FDaKDNTu71E1ALetpg9Yf%2FnyXHWNbqOXiitInwacQtn%2FAaLOwRAxHHcY7dTSEXRL9%2FHZGSHRobTWQX7oreqtGMuuzUgVAS3uyF6MBYo4I9mcjVhryj1mNJkewP0mi4GrsSb9q%2BySq63DXwYKRQo8j3KjIoU0peplnhW%2Ftfi7GxK4RdTwUcFw3%2FFGbFlvDsVkrSw8H3o69qzoIWPicIX6Vdq0FSDX4eu65tUe1q1328Ox%2BevPS4y5L0D4mXg7WQlrlIyYlhvYpgXMJjmh70GOqUBt6Eas7kaHTWjmngT68S1qEttEMIf%2B6Bh8FnB1%2BML1srTw%2BsWDYXAbA%2FSl8sOkl7TIpj4BzY98OC5x9iypBbx1%2BB1VI3tA6OXVX8b2%2BWwUZ1mgJqm56ZlozivRqCGVFdtrg0E7J92mj8fgOp8V%2Fhb681DdTluGrs8Bx2Ph4XJg1YUxPIuc9ssJIfyUh8DJYRxqU7ihib%2FF4Nob9tq5PlU%2BzEMKvKj&X-Amz-Signature=d85af371827da2f4c55a8967c6bc45ec0f922dc84401a11099df4a571257aafb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTSU6GMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCKma8%2BxE1ZyM%2BX7xKY2NSEQJ%2FdXYDe2sIqp%2FUooG2z1gIgCtwAynjF7bHZns4bMuw3TCASwlprZ%2Bj1sMqgNBL2CpUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDAyB8fGhcCyOVPcvfCrcAz%2BL9VXCZYJMuq4MPohZFSdNVkWFujVyeVGjM7nWDh4tNW3Grg0bQ7Yoevwd3avkLood7TgSoX64i0hmM5GVnWpkPlN2wecUPUNi3r%2Fcn13MB%2Bqkw4dhCfaa18PPOCacJ%2Bu%2Bh8CPSwlxC00yWpY8vvSYliSSfQK7G3Xo%2Bk9Zq4MmQrdD26ruoBl%2FyUU5TVp1p8Fav5RkKgWYVY3HBWXw9QAzFrmArkEFlrm5f73qwgPRmqE9KpYXbmmtAT9%2BJV7dr6ieWMHlfQ3NlIrflAPkahpJl1fjICGuE0cSAhDvTBo2r3EkyBhK4pu7E%2FfYCTPxWmz4kNftV1yGQ0M%2Fw%2Fb%2F44WFW7YUgEZFZVrd5T2HxRLiDK5Ep%2FDaKDNTu71E1ALetpg9Yf%2FnyXHWNbqOXiitInwacQtn%2FAaLOwRAxHHcY7dTSEXRL9%2FHZGSHRobTWQX7oreqtGMuuzUgVAS3uyF6MBYo4I9mcjVhryj1mNJkewP0mi4GrsSb9q%2BySq63DXwYKRQo8j3KjIoU0peplnhW%2Ftfi7GxK4RdTwUcFw3%2FFGbFlvDsVkrSw8H3o69qzoIWPicIX6Vdq0FSDX4eu65tUe1q1328Ox%2BevPS4y5L0D4mXg7WQlrlIyYlhvYpgXMJjmh70GOqUBt6Eas7kaHTWjmngT68S1qEttEMIf%2B6Bh8FnB1%2BML1srTw%2BsWDYXAbA%2FSl8sOkl7TIpj4BzY98OC5x9iypBbx1%2BB1VI3tA6OXVX8b2%2BWwUZ1mgJqm56ZlozivRqCGVFdtrg0E7J92mj8fgOp8V%2Fhb681DdTluGrs8Bx2Ph4XJg1YUxPIuc9ssJIfyUh8DJYRxqU7ihib%2FF4Nob9tq5PlU%2BzEMKvKj&X-Amz-Signature=cd967946a05d1f3d2bad39eb4d17f781d2e8cdc75d778adbca3d30317cf39482&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSKW4HGA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDvpTBHeSidrulZTJonSU17%2Fw0s4oGtzNRgA5LDZQv1MAIhALZXX6%2BOzwvkoWX8Lxw1YROSq%2BPXCPczrWi08hMVk%2Fb7Kv8DCCwQABoMNjM3NDIzMTgzODA1Igxjwo4DFkrit%2FvRFiEq3ANkW8uqTxXO2IzByT3%2Bi3Q8o31prf17qq0UB54OYZJ3J%2BfnXUN9hGUoay9W7vls12%2BFctW2a0eifokD4SQuJdLoI1Par6w5e8ocU03rEk1gH9ATGgqM%2F64SObDS1rH3dMYe3o8Tm0Gj0yAw%2FEllTQIt4icxdemhUrdWs1PdTTsTb2CWpiGjZyqCTXLcu7HxapOokcIQXQpH38DGf0jEmY%2BllvLQ5Xybu%2FHCHBPaNkLaxPtvtXpEQFk1OejI837KBauXPPwoKN%2BZSBtL8PPOqxY5%2BKygS1jR6V8NiVK3IJVQiHJw035xb2W0z8%2FkmwXZ3mHmvFhS0pexRiQzPiJuHtka2ZxANuS6ApiDnG1oSpUHl81J5Gh6H9w%2BlFjCY3ttKnULTFwlyz44k3gvuG77lrcrRPakNLJiRFTA%2FmVjJEPQDhK9qDoIlzIrM%2FMLOdyEd8dJ985SR2%2BDEPA4qr2hFvyFQIakEoHxW%2Bd8CRKlOjGncZiMSxYHl96U6EhH6APlSDgTSlgyBBzvaqHdl1NxKda2qAzLVfrtWHMnXernAwu3sd%2BvpsTbNdE71r9VQnvZNWvVmfyicrIyyda%2BgtYhftYOLEzAXcESLuLFtYRc2xql7dnPC7fAJCJRo02j4zDQ5oe9BjqkAUFprC%2Brajvsh%2BUejEsuSXPMp%2B2lOmWFWfnj7TaDl19q9ihR6t8EH0l1d2IV7rlTPYOXT7gkpOcgz06142WtAOCc5qlSVhl3%2FspOrlr%2FgZqQsxgRghRKVYQoyCEFpvHHJTl9Ka278ItjqyoHE%2F6z%2FCpKwFFcDyBnNnEgiwJDyN4Jtko6HKkPnBOzcXLeDYkUdohE32sOTkMtFEibCVKphw4GHKRV&X-Amz-Signature=51ccf9f8997c992512e4e6ceb2d8cac4b57660bc67e8da7677bd6187a77e2064&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663IDUUYB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIDKo5prdzBQrfT98VDU9Bv%2FgJxIxg1WXbGyc0yVnyxBbAiEAm30W6%2FnYUJN%2BnzMUgQlpCB%2BXxD0oYnidFD1ccp6XZwwq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDC9f%2BxDjk99V0iANEircA9xMXcEkbrp9GK2NaqvvkUlNsYwiRL4HSquQQ6SM1hm9DhrkQvUnZqHxkG3z%2Ff4%2B9D3A7vjgAbpOJDl9LHDbETITKQNY%2BUXd6BcD3UgJ%2Fyr5FFaNOot2YLmeinfnCLsAl7zIEfkuUl8CoyNGziJXJ8loSoen1AxxahJb%2FaFpvlxNm8cNvyRSZaoIgIf7M%2BZEFpSZ7yi9gTXvu%2FMEPUabTby4DyDTEb%2FKofXjlSSZamKWOQ5KJjGu%2BrSlB%2FI1asLEq%2FGU17J45bJJPx0h9Lz9s4mdKznhHp72ffY0j6TMd0sQBsB7kWsrJ1qL%2B6UTwz%2F2jom3ZQRNpVDVxbiji0MjEha1oauyg0lVyaz%2FKeTL%2FruQotdaNysooI4Gj%2B7W2abuqgtEAVgBTJE9WBzMMGfYSymXs20FLd0jVH0tnrjhT1ihwcquMyARZqVbItu8HBhRxeVCXGRaEBd9SbeJUGC9VJbVoY5m%2Frp%2FMRs2OlJbSTX2xEUBEvjivhb3fOZhhnhDpEQCYrRVyVZs3W3Y100n01SddqMykDm1peNAYtfNNZm7InepuO0uiS%2FxlE5fM%2FfLv%2FhBBzmsjrF%2Bq6%2BpxX2wodTQYl8bb%2B2c3zCaq%2F95rDL901QgYC757b3Y%2FXatMILmh70GOqUBRL9hMiUetpjs4Bhwwl1Vu6UZJax1QM7yNJ86%2FPCM0B6jFNzhFk4cw%2FbOs4CK8mK2iCJ6K3G%2FlVeSJ1MCqN1N5pFSJ6pyXcOgDoGg5WC00m8qzD4QI019QEH%2BSnZvyjreyMip69MYwmTGY5EhRUO3O9MUnI9Q2X%2BA9Bx0TSXIfPNrxb4O11rLM544N1izJxqto0NT2p7L84vAQzjMOxxllcyNn4se&X-Amz-Signature=5fbe67e6d2daea505bec4b25d50f0c29476824b724098c99f656540fb9aeac01&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TXZP7RX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCICwvitwW8ZDyQ4%2BDo2RXT5HXjFUXBIY5qqxtP9jf%2B3pwAiEAyma7vM32q91aLAhNokv38D3i%2Bdrxckhog6s%2F1hVS70gq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDEae1VYffHvGsgaqpSrcA7xBgfJdyxRFrLSaoZYtcOU75xJnWE1ppa37Z7BMpqzR6FmA7lAjjT%2FOzqyJEf8iBD8CG2ucOQghUfM%2Fa0%2Bfn%2B24tHJmOZl4fGBC68YGyT6xpHCkMh5DLFhFULg9p%2B847d2SuNBCovlLUNENN6xw7Ut8mtNd5qGj39MGgEvn%2FkatX4ljpZBOFmE8gJ7os6OrpTXfD0DfbyXzGNw4miSB8ooQOVjgtzgnMgxYAiaS9QxdfJhzaC1S2y%2FpIIjEI68AhsB2b%2FH8nTn2ZxV%2Bf6FkcyiVuas0RKRC5JDWIwaDtHDrVotipnkE7Q4Kn5sgrgT4%2FaxSKKjmI8UPBPFwfjsDELQQZTkcDJt%2BjKxIAsXttH%2FD8yF%2F%2FmYZvvlwcaK2m4DAWqfQOQyVIcByPLnWB41e1BPsE3bt0g6B0GKXtfUf4MpDoJRs44Qa5ubqz4WGzfmVWa4am75reM2a4TCcPEas7jLCDEWfQUzpyFRzbIVTnly1NoVH0y6dUYI7KbWgEiUGkorNB3LjxhmykQSdczTAb0H3%2BCUGJHzB52wvdRtgH2qfT2K8sF1vUSM2bs8%2BgcinGL6v5eMPcbXj1z9pjXwLZnS1mIbGhxz%2B6sx%2BoG7vHu%2BgyOXFnY2zmC0lgnuTMJTmh70GOqUB%2FAnrUMMAoyZLuAIw8ttBAM2IB%2FYzhROGGpHimDKrV55qpo8y7PtwJd9W4d8Pxqh4f1vALgZvxPlPLVVgFjy6G8WdwtKpAXngrdNYWJuysm22WW%2B8o9BXDMakbvDYuUXBoZVwvMiuFnv5Aiapt71Vw1BtHxs%2Bx0vtthx7l3Tk2NzCrpWBb25W6o8v9czo9DuLtXXv7weUL%2BXEnfHBKDjBxCtVdH1h&X-Amz-Signature=fd899b072578bc159af3dcfa57a584570246c9e4dda239d3e780ffafbe5997e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3P64RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDv30jYe1ko79t7zgx0qbFU0GwH79fgnsR5lVeyricyYAIhAPsjT9TQ7XTUsONUZYQnSUjxTjXzsK0piNgN%2FwyDX61dKv8DCCwQABoMNjM3NDIzMTgzODA1IgyuSugIjQAhCS7lO6sq3APYb9nAlFn9bKq6n1ObYEXfwRpCxvVqbk0AWX7rVPyY96vFNR7g7c9TZTWMqLkGA%2FYPnzmDTN5D8JcVNZM3aiRIMDiOIkkc7SgOSykCHzPqkUvJBaeuTrL4FjsyFS1Db6l7tsvdy2BDbVa9AIjq%2BnicRtPFx08DH9FXlP272rxk8mQ1bhfK1q3GD%2FhTiQ59lYTVFH7%2BOIWPjyqU0XpoofWv8YKxqdMkvdNFF0dgBUfBUFEub%2Fj%2B2WBHCFoE398RuTCiFg65wYBQu6DPoAlBAc%2F%2BZ5903%2BpDQqDAi%2BlLUhnNvna1OXWVminyVKtGlF2PojiWLLJqLaka9vtFxDRh5xseFTh%2BZjMlCPXHaIqo2h7EzXsWEGoC7J4Rcix%2FUXMa9M%2BoEcKN9EsCRuhsnR51r9i59U5R85gY401odZ9xgo1SksKIe2wBWeuz4kqhXzwPD5v337hrMMWDk0oq2iNuOefAZuQ7q074uRvHj74eWkz4Wht1OowKGkthQQHwuHlqpMVlvG7PO0u9%2Fb7CFWyD3WIbW85FfCW3xJjTz4hUYBd%2FEklZzjF0PRvOtmw9h%2By9M0Gwm%2FtvJZpWFEhRqlE9OL9f2CnQaKCWlRJ%2Ba9%2BjQIhYQiryDFPfYYgAQN8c9DCI5oe9BjqkAVSc98eB6h8C4Vn8GheXX1jrlEuy%2BkREJCP3JcHFSdmkz%2F5WQ7fWExqRyvIM5d9orIcddqEuM8xuXMZDHFQoFw4i6oGVtFvRvW%2FvWlKNymN61fTt5Yw7UEFGtxE838RxXQgW1EB5yoQZJl1FiIx20hpcq11eripTUhn5ON1Difdak5qcIQjkpIZotLdBltD0jT4ivio8qnNyRrKXtCuA5mKd7YWc&X-Amz-Signature=40181781641ecd8d3b6122a7d9088a57acfe3685fbed97563c4a77811e140f01&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3P64RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDv30jYe1ko79t7zgx0qbFU0GwH79fgnsR5lVeyricyYAIhAPsjT9TQ7XTUsONUZYQnSUjxTjXzsK0piNgN%2FwyDX61dKv8DCCwQABoMNjM3NDIzMTgzODA1IgyuSugIjQAhCS7lO6sq3APYb9nAlFn9bKq6n1ObYEXfwRpCxvVqbk0AWX7rVPyY96vFNR7g7c9TZTWMqLkGA%2FYPnzmDTN5D8JcVNZM3aiRIMDiOIkkc7SgOSykCHzPqkUvJBaeuTrL4FjsyFS1Db6l7tsvdy2BDbVa9AIjq%2BnicRtPFx08DH9FXlP272rxk8mQ1bhfK1q3GD%2FhTiQ59lYTVFH7%2BOIWPjyqU0XpoofWv8YKxqdMkvdNFF0dgBUfBUFEub%2Fj%2B2WBHCFoE398RuTCiFg65wYBQu6DPoAlBAc%2F%2BZ5903%2BpDQqDAi%2BlLUhnNvna1OXWVminyVKtGlF2PojiWLLJqLaka9vtFxDRh5xseFTh%2BZjMlCPXHaIqo2h7EzXsWEGoC7J4Rcix%2FUXMa9M%2BoEcKN9EsCRuhsnR51r9i59U5R85gY401odZ9xgo1SksKIe2wBWeuz4kqhXzwPD5v337hrMMWDk0oq2iNuOefAZuQ7q074uRvHj74eWkz4Wht1OowKGkthQQHwuHlqpMVlvG7PO0u9%2Fb7CFWyD3WIbW85FfCW3xJjTz4hUYBd%2FEklZzjF0PRvOtmw9h%2By9M0Gwm%2FtvJZpWFEhRqlE9OL9f2CnQaKCWlRJ%2Ba9%2BjQIhYQiryDFPfYYgAQN8c9DCI5oe9BjqkAVSc98eB6h8C4Vn8GheXX1jrlEuy%2BkREJCP3JcHFSdmkz%2F5WQ7fWExqRyvIM5d9orIcddqEuM8xuXMZDHFQoFw4i6oGVtFvRvW%2FvWlKNymN61fTt5Yw7UEFGtxE838RxXQgW1EB5yoQZJl1FiIx20hpcq11eripTUhn5ON1Difdak5qcIQjkpIZotLdBltD0jT4ivio8qnNyRrKXtCuA5mKd7YWc&X-Amz-Signature=8ce865691abc94222583a2b21939db45104cd2d9786f58224212788477e275d1&X-Amz-SignedHeaders=host&x-id=GetObject)

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
