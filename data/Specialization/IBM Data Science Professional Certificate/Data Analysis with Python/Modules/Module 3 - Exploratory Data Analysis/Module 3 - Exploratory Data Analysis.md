

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCSFTE7I%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIE%2FHuUhKyGO3WFqYM1oIS8xiSlknM1PYQsyzmRqRjQh6AiEA0umibSECyrYlM5bJ%2F2vSCVt33TVr8U37ZeWMa746pioq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDK7SeXPCNjB4mY2%2F%2FyrcA12S77BMgY1QuoYqM06sw6W7MjGkgDLSomhshB9WTBMomVT8D2ZgDKiwzyN3JNU3LKV5ZZUuadS7Vf0CqExx8SRzymnj7mV7XTEmFN9u7SkYWz75kuussNRV3Bk4z4pe%2FtkOVhhKI1wUNnnyJMMQ5gYbwGJ9y7DfyfPC86uiQeqP6P9vQZIOVEBq3GTGpaVquYtQ8Pt3wVqtja8KGv2HQ2dlcZU3vwvaGsWeYeNxclUgMlWrHipAOqLtuU0XfUyCrUoHyLNALJ1rbCWACPiXkF5wyREDjTsg6MbTH1jV4xq5yCZtDPSQSubt6eC%2FnAtnR4EbW7e5wPD34Vs3lwier0rcKSAOH2BrAF7FedhWdvGcIwE5%2FfciImrjOHJK5pp5YmXvrplWH0hRcxu6XHop7KzVu6lDpIsQKrO%2By6Kx0CFDT8%2FmZWsuv8bJBkDUJlwSXIsIlgWiWwPH0ps9NQUP2nA%2BCVUaMnBgAKfg%2B69L0iWtYBbg4Z6WSpdoYSYcumQHPcBfwC1iWP3vW7nyLd9WAx3ynk0h8Mdzz1h4VCm%2BFYjSBB4en6MTLsCvmiBmwS2LlJhCYp1FEU9HKTiPSDyOZQ0S6VDGjniUvadwUJoOc0MTCtxlAzIWL4SYpKbRMNKU5bwGOqUBYpzk8%2BQ38EnO8qAw3UU%2FdaAYt3atOdCv%2BPbQUzyoaypfHNPFD%2B2cCLF%2Fa5pZw9cM2dGNvF7r5K3JdI8SeBVcj%2FxN8TJFw%2Fy0KDJ5%2BWhmpqIAkRbCMT9tbQX9%2FSywQVqVS4pZl%2BzNOsq5YNTmwqkqepHYY0gM%2BDDUEM5L%2BylLCtwsF1Xe9ptbvC8u2yi5Jq5LRDBoT%2B058herocMXZl11oDUl4BNT&X-Amz-Signature=54a5891c066ff6a5527780620ea9514f70b29020991da88706ea7e1a98245cd2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCSFTE7I%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIE%2FHuUhKyGO3WFqYM1oIS8xiSlknM1PYQsyzmRqRjQh6AiEA0umibSECyrYlM5bJ%2F2vSCVt33TVr8U37ZeWMa746pioq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDK7SeXPCNjB4mY2%2F%2FyrcA12S77BMgY1QuoYqM06sw6W7MjGkgDLSomhshB9WTBMomVT8D2ZgDKiwzyN3JNU3LKV5ZZUuadS7Vf0CqExx8SRzymnj7mV7XTEmFN9u7SkYWz75kuussNRV3Bk4z4pe%2FtkOVhhKI1wUNnnyJMMQ5gYbwGJ9y7DfyfPC86uiQeqP6P9vQZIOVEBq3GTGpaVquYtQ8Pt3wVqtja8KGv2HQ2dlcZU3vwvaGsWeYeNxclUgMlWrHipAOqLtuU0XfUyCrUoHyLNALJ1rbCWACPiXkF5wyREDjTsg6MbTH1jV4xq5yCZtDPSQSubt6eC%2FnAtnR4EbW7e5wPD34Vs3lwier0rcKSAOH2BrAF7FedhWdvGcIwE5%2FfciImrjOHJK5pp5YmXvrplWH0hRcxu6XHop7KzVu6lDpIsQKrO%2By6Kx0CFDT8%2FmZWsuv8bJBkDUJlwSXIsIlgWiWwPH0ps9NQUP2nA%2BCVUaMnBgAKfg%2B69L0iWtYBbg4Z6WSpdoYSYcumQHPcBfwC1iWP3vW7nyLd9WAx3ynk0h8Mdzz1h4VCm%2BFYjSBB4en6MTLsCvmiBmwS2LlJhCYp1FEU9HKTiPSDyOZQ0S6VDGjniUvadwUJoOc0MTCtxlAzIWL4SYpKbRMNKU5bwGOqUBYpzk8%2BQ38EnO8qAw3UU%2FdaAYt3atOdCv%2BPbQUzyoaypfHNPFD%2B2cCLF%2Fa5pZw9cM2dGNvF7r5K3JdI8SeBVcj%2FxN8TJFw%2Fy0KDJ5%2BWhmpqIAkRbCMT9tbQX9%2FSywQVqVS4pZl%2BzNOsq5YNTmwqkqepHYY0gM%2BDDUEM5L%2BylLCtwsF1Xe9ptbvC8u2yi5Jq5LRDBoT%2B058herocMXZl11oDUl4BNT&X-Amz-Signature=096d7155b1372ac9d9dd1784695eb91ce7a141bfca59df9cf7bf000cd72deec2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCSFTE7I%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIE%2FHuUhKyGO3WFqYM1oIS8xiSlknM1PYQsyzmRqRjQh6AiEA0umibSECyrYlM5bJ%2F2vSCVt33TVr8U37ZeWMa746pioq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDK7SeXPCNjB4mY2%2F%2FyrcA12S77BMgY1QuoYqM06sw6W7MjGkgDLSomhshB9WTBMomVT8D2ZgDKiwzyN3JNU3LKV5ZZUuadS7Vf0CqExx8SRzymnj7mV7XTEmFN9u7SkYWz75kuussNRV3Bk4z4pe%2FtkOVhhKI1wUNnnyJMMQ5gYbwGJ9y7DfyfPC86uiQeqP6P9vQZIOVEBq3GTGpaVquYtQ8Pt3wVqtja8KGv2HQ2dlcZU3vwvaGsWeYeNxclUgMlWrHipAOqLtuU0XfUyCrUoHyLNALJ1rbCWACPiXkF5wyREDjTsg6MbTH1jV4xq5yCZtDPSQSubt6eC%2FnAtnR4EbW7e5wPD34Vs3lwier0rcKSAOH2BrAF7FedhWdvGcIwE5%2FfciImrjOHJK5pp5YmXvrplWH0hRcxu6XHop7KzVu6lDpIsQKrO%2By6Kx0CFDT8%2FmZWsuv8bJBkDUJlwSXIsIlgWiWwPH0ps9NQUP2nA%2BCVUaMnBgAKfg%2B69L0iWtYBbg4Z6WSpdoYSYcumQHPcBfwC1iWP3vW7nyLd9WAx3ynk0h8Mdzz1h4VCm%2BFYjSBB4en6MTLsCvmiBmwS2LlJhCYp1FEU9HKTiPSDyOZQ0S6VDGjniUvadwUJoOc0MTCtxlAzIWL4SYpKbRMNKU5bwGOqUBYpzk8%2BQ38EnO8qAw3UU%2FdaAYt3atOdCv%2BPbQUzyoaypfHNPFD%2B2cCLF%2Fa5pZw9cM2dGNvF7r5K3JdI8SeBVcj%2FxN8TJFw%2Fy0KDJ5%2BWhmpqIAkRbCMT9tbQX9%2FSywQVqVS4pZl%2BzNOsq5YNTmwqkqepHYY0gM%2BDDUEM5L%2BylLCtwsF1Xe9ptbvC8u2yi5Jq5LRDBoT%2B058herocMXZl11oDUl4BNT&X-Amz-Signature=e084522c77674ae6a34c299de0668f63293805dfc3db4c4ed381dbd02df5dfea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOION2XX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEFraGuw%2BUTdWVH8ojChwm%2BHD7%2By6CqvdOfdJPkror8SAiAJvSLI5atS%2FC%2Bzl4FitHT9lPKztXLVuj2Z3xhzT1dsXyr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM5afSZdRzIGqecakvKtwDJhYbY%2BbAMCR2OfJRGza5j7Z9Q%2Ben%2FVfkkC%2B1U%2BUMj2qNr0J6nmXshk%2BmjxUsMMb5coNYUZ2Bkx0TF%2FMssYErbBpbRxkyCBsrtXdW8wHm8T1P6fe%2F51gjJsIcuOO1SAV02tA6SMn3upl1z1j5yjWzzq1pmjGoMOvK66cyWx9yb4RbavID7LSQdvNjRZ8Er2hS6Fu37h07fxx4XFS2YvslRbiWtLW6zFY8p1ciYIhKezWe3QMEysAnB8KCzUGUUZJRYmMWJiNbc%2F9UY7NxMgN8Tv8i9KXUgam7wtvEC9WwnFlLsIdtA5H9n8F%2BcTisIZTaagzdNqIA367puuwjswWR9oRHPaUxBYV6QdpAT2SAZDtHLo07ACvUWzVi9dvZs%2BAs9dWIVSqEj1nFwdnKu8Zn08IuF9r5H5iO3aqbT%2F%2FiJfdd3Y3R7jbZJsadZ%2F5gqZf1lMtfnpispSFPymKY7GrbjnDVKEI%2FKkQtMgNvX15AbZxSOG8zwJyEGR72JPMNK3ys8l%2F6QU76xiRV3CF8ml0g8VX2tXqBQWV3NbGcaGwFOQBcuEBSz6qfV%2B2u87uHzXbqQ2EXyrSqh7sVxu7roWnQTO2ecB%2FkzEwX5bCSmUqhrvd5I9bG5Rbi7b%2FUfkEw05TlvAY6pgH%2Bd3fuXtsFnw%2Br6snN3tUs2CbcqZ023HjUxkVW3oQjedKVLnVgGI4wVBg1Vl3nPYvhmGhJSB%2FnbW1bpGTD4zJ0f59DgCyFPUEMkqAfRbbEQXtNs0MnK09hJ1btGDRqHPkwhSJEV15iBIkgV5P5gpSaSaWRsX6b2eM95jiEAu2gWwNxZxdPvvbTCwsDAOUCCDNJQfj8sripKzwQyjdqHD3n3YPwiQfp&X-Amz-Signature=f956126e80acbc30427193cd2247ac294eaf17a0cce81028e6cd98c21d2b6588&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOION2XX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEFraGuw%2BUTdWVH8ojChwm%2BHD7%2By6CqvdOfdJPkror8SAiAJvSLI5atS%2FC%2Bzl4FitHT9lPKztXLVuj2Z3xhzT1dsXyr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM5afSZdRzIGqecakvKtwDJhYbY%2BbAMCR2OfJRGza5j7Z9Q%2Ben%2FVfkkC%2B1U%2BUMj2qNr0J6nmXshk%2BmjxUsMMb5coNYUZ2Bkx0TF%2FMssYErbBpbRxkyCBsrtXdW8wHm8T1P6fe%2F51gjJsIcuOO1SAV02tA6SMn3upl1z1j5yjWzzq1pmjGoMOvK66cyWx9yb4RbavID7LSQdvNjRZ8Er2hS6Fu37h07fxx4XFS2YvslRbiWtLW6zFY8p1ciYIhKezWe3QMEysAnB8KCzUGUUZJRYmMWJiNbc%2F9UY7NxMgN8Tv8i9KXUgam7wtvEC9WwnFlLsIdtA5H9n8F%2BcTisIZTaagzdNqIA367puuwjswWR9oRHPaUxBYV6QdpAT2SAZDtHLo07ACvUWzVi9dvZs%2BAs9dWIVSqEj1nFwdnKu8Zn08IuF9r5H5iO3aqbT%2F%2FiJfdd3Y3R7jbZJsadZ%2F5gqZf1lMtfnpispSFPymKY7GrbjnDVKEI%2FKkQtMgNvX15AbZxSOG8zwJyEGR72JPMNK3ys8l%2F6QU76xiRV3CF8ml0g8VX2tXqBQWV3NbGcaGwFOQBcuEBSz6qfV%2B2u87uHzXbqQ2EXyrSqh7sVxu7roWnQTO2ecB%2FkzEwX5bCSmUqhrvd5I9bG5Rbi7b%2FUfkEw05TlvAY6pgH%2Bd3fuXtsFnw%2Br6snN3tUs2CbcqZ023HjUxkVW3oQjedKVLnVgGI4wVBg1Vl3nPYvhmGhJSB%2FnbW1bpGTD4zJ0f59DgCyFPUEMkqAfRbbEQXtNs0MnK09hJ1btGDRqHPkwhSJEV15iBIkgV5P5gpSaSaWRsX6b2eM95jiEAu2gWwNxZxdPvvbTCwsDAOUCCDNJQfj8sripKzwQyjdqHD3n3YPwiQfp&X-Amz-Signature=ef3158d18b94406174576d4eb431694e49886edf06b7bbc5f340762a84416be3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOION2XX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEFraGuw%2BUTdWVH8ojChwm%2BHD7%2By6CqvdOfdJPkror8SAiAJvSLI5atS%2FC%2Bzl4FitHT9lPKztXLVuj2Z3xhzT1dsXyr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM5afSZdRzIGqecakvKtwDJhYbY%2BbAMCR2OfJRGza5j7Z9Q%2Ben%2FVfkkC%2B1U%2BUMj2qNr0J6nmXshk%2BmjxUsMMb5coNYUZ2Bkx0TF%2FMssYErbBpbRxkyCBsrtXdW8wHm8T1P6fe%2F51gjJsIcuOO1SAV02tA6SMn3upl1z1j5yjWzzq1pmjGoMOvK66cyWx9yb4RbavID7LSQdvNjRZ8Er2hS6Fu37h07fxx4XFS2YvslRbiWtLW6zFY8p1ciYIhKezWe3QMEysAnB8KCzUGUUZJRYmMWJiNbc%2F9UY7NxMgN8Tv8i9KXUgam7wtvEC9WwnFlLsIdtA5H9n8F%2BcTisIZTaagzdNqIA367puuwjswWR9oRHPaUxBYV6QdpAT2SAZDtHLo07ACvUWzVi9dvZs%2BAs9dWIVSqEj1nFwdnKu8Zn08IuF9r5H5iO3aqbT%2F%2FiJfdd3Y3R7jbZJsadZ%2F5gqZf1lMtfnpispSFPymKY7GrbjnDVKEI%2FKkQtMgNvX15AbZxSOG8zwJyEGR72JPMNK3ys8l%2F6QU76xiRV3CF8ml0g8VX2tXqBQWV3NbGcaGwFOQBcuEBSz6qfV%2B2u87uHzXbqQ2EXyrSqh7sVxu7roWnQTO2ecB%2FkzEwX5bCSmUqhrvd5I9bG5Rbi7b%2FUfkEw05TlvAY6pgH%2Bd3fuXtsFnw%2Br6snN3tUs2CbcqZ023HjUxkVW3oQjedKVLnVgGI4wVBg1Vl3nPYvhmGhJSB%2FnbW1bpGTD4zJ0f59DgCyFPUEMkqAfRbbEQXtNs0MnK09hJ1btGDRqHPkwhSJEV15iBIkgV5P5gpSaSaWRsX6b2eM95jiEAu2gWwNxZxdPvvbTCwsDAOUCCDNJQfj8sripKzwQyjdqHD3n3YPwiQfp&X-Amz-Signature=fc5b246adaf1bbebded11061d982f816f6c27b51b499da5fb2283e46d1623202&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOION2XX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEFraGuw%2BUTdWVH8ojChwm%2BHD7%2By6CqvdOfdJPkror8SAiAJvSLI5atS%2FC%2Bzl4FitHT9lPKztXLVuj2Z3xhzT1dsXyr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM5afSZdRzIGqecakvKtwDJhYbY%2BbAMCR2OfJRGza5j7Z9Q%2Ben%2FVfkkC%2B1U%2BUMj2qNr0J6nmXshk%2BmjxUsMMb5coNYUZ2Bkx0TF%2FMssYErbBpbRxkyCBsrtXdW8wHm8T1P6fe%2F51gjJsIcuOO1SAV02tA6SMn3upl1z1j5yjWzzq1pmjGoMOvK66cyWx9yb4RbavID7LSQdvNjRZ8Er2hS6Fu37h07fxx4XFS2YvslRbiWtLW6zFY8p1ciYIhKezWe3QMEysAnB8KCzUGUUZJRYmMWJiNbc%2F9UY7NxMgN8Tv8i9KXUgam7wtvEC9WwnFlLsIdtA5H9n8F%2BcTisIZTaagzdNqIA367puuwjswWR9oRHPaUxBYV6QdpAT2SAZDtHLo07ACvUWzVi9dvZs%2BAs9dWIVSqEj1nFwdnKu8Zn08IuF9r5H5iO3aqbT%2F%2FiJfdd3Y3R7jbZJsadZ%2F5gqZf1lMtfnpispSFPymKY7GrbjnDVKEI%2FKkQtMgNvX15AbZxSOG8zwJyEGR72JPMNK3ys8l%2F6QU76xiRV3CF8ml0g8VX2tXqBQWV3NbGcaGwFOQBcuEBSz6qfV%2B2u87uHzXbqQ2EXyrSqh7sVxu7roWnQTO2ecB%2FkzEwX5bCSmUqhrvd5I9bG5Rbi7b%2FUfkEw05TlvAY6pgH%2Bd3fuXtsFnw%2Br6snN3tUs2CbcqZ023HjUxkVW3oQjedKVLnVgGI4wVBg1Vl3nPYvhmGhJSB%2FnbW1bpGTD4zJ0f59DgCyFPUEMkqAfRbbEQXtNs0MnK09hJ1btGDRqHPkwhSJEV15iBIkgV5P5gpSaSaWRsX6b2eM95jiEAu2gWwNxZxdPvvbTCwsDAOUCCDNJQfj8sripKzwQyjdqHD3n3YPwiQfp&X-Amz-Signature=eb29e11fe1ebf0f0faa6da8402ac021c54b7178c933f7db312f338dd1014422c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOION2XX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEFraGuw%2BUTdWVH8ojChwm%2BHD7%2By6CqvdOfdJPkror8SAiAJvSLI5atS%2FC%2Bzl4FitHT9lPKztXLVuj2Z3xhzT1dsXyr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM5afSZdRzIGqecakvKtwDJhYbY%2BbAMCR2OfJRGza5j7Z9Q%2Ben%2FVfkkC%2B1U%2BUMj2qNr0J6nmXshk%2BmjxUsMMb5coNYUZ2Bkx0TF%2FMssYErbBpbRxkyCBsrtXdW8wHm8T1P6fe%2F51gjJsIcuOO1SAV02tA6SMn3upl1z1j5yjWzzq1pmjGoMOvK66cyWx9yb4RbavID7LSQdvNjRZ8Er2hS6Fu37h07fxx4XFS2YvslRbiWtLW6zFY8p1ciYIhKezWe3QMEysAnB8KCzUGUUZJRYmMWJiNbc%2F9UY7NxMgN8Tv8i9KXUgam7wtvEC9WwnFlLsIdtA5H9n8F%2BcTisIZTaagzdNqIA367puuwjswWR9oRHPaUxBYV6QdpAT2SAZDtHLo07ACvUWzVi9dvZs%2BAs9dWIVSqEj1nFwdnKu8Zn08IuF9r5H5iO3aqbT%2F%2FiJfdd3Y3R7jbZJsadZ%2F5gqZf1lMtfnpispSFPymKY7GrbjnDVKEI%2FKkQtMgNvX15AbZxSOG8zwJyEGR72JPMNK3ys8l%2F6QU76xiRV3CF8ml0g8VX2tXqBQWV3NbGcaGwFOQBcuEBSz6qfV%2B2u87uHzXbqQ2EXyrSqh7sVxu7roWnQTO2ecB%2FkzEwX5bCSmUqhrvd5I9bG5Rbi7b%2FUfkEw05TlvAY6pgH%2Bd3fuXtsFnw%2Br6snN3tUs2CbcqZ023HjUxkVW3oQjedKVLnVgGI4wVBg1Vl3nPYvhmGhJSB%2FnbW1bpGTD4zJ0f59DgCyFPUEMkqAfRbbEQXtNs0MnK09hJ1btGDRqHPkwhSJEV15iBIkgV5P5gpSaSaWRsX6b2eM95jiEAu2gWwNxZxdPvvbTCwsDAOUCCDNJQfj8sripKzwQyjdqHD3n3YPwiQfp&X-Amz-Signature=b13a14940e79fc9642e639ab51b9c2b1ee777ca3b39e376b70082f7300d970f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOION2XX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEFraGuw%2BUTdWVH8ojChwm%2BHD7%2By6CqvdOfdJPkror8SAiAJvSLI5atS%2FC%2Bzl4FitHT9lPKztXLVuj2Z3xhzT1dsXyr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM5afSZdRzIGqecakvKtwDJhYbY%2BbAMCR2OfJRGza5j7Z9Q%2Ben%2FVfkkC%2B1U%2BUMj2qNr0J6nmXshk%2BmjxUsMMb5coNYUZ2Bkx0TF%2FMssYErbBpbRxkyCBsrtXdW8wHm8T1P6fe%2F51gjJsIcuOO1SAV02tA6SMn3upl1z1j5yjWzzq1pmjGoMOvK66cyWx9yb4RbavID7LSQdvNjRZ8Er2hS6Fu37h07fxx4XFS2YvslRbiWtLW6zFY8p1ciYIhKezWe3QMEysAnB8KCzUGUUZJRYmMWJiNbc%2F9UY7NxMgN8Tv8i9KXUgam7wtvEC9WwnFlLsIdtA5H9n8F%2BcTisIZTaagzdNqIA367puuwjswWR9oRHPaUxBYV6QdpAT2SAZDtHLo07ACvUWzVi9dvZs%2BAs9dWIVSqEj1nFwdnKu8Zn08IuF9r5H5iO3aqbT%2F%2FiJfdd3Y3R7jbZJsadZ%2F5gqZf1lMtfnpispSFPymKY7GrbjnDVKEI%2FKkQtMgNvX15AbZxSOG8zwJyEGR72JPMNK3ys8l%2F6QU76xiRV3CF8ml0g8VX2tXqBQWV3NbGcaGwFOQBcuEBSz6qfV%2B2u87uHzXbqQ2EXyrSqh7sVxu7roWnQTO2ecB%2FkzEwX5bCSmUqhrvd5I9bG5Rbi7b%2FUfkEw05TlvAY6pgH%2Bd3fuXtsFnw%2Br6snN3tUs2CbcqZ023HjUxkVW3oQjedKVLnVgGI4wVBg1Vl3nPYvhmGhJSB%2FnbW1bpGTD4zJ0f59DgCyFPUEMkqAfRbbEQXtNs0MnK09hJ1btGDRqHPkwhSJEV15iBIkgV5P5gpSaSaWRsX6b2eM95jiEAu2gWwNxZxdPvvbTCwsDAOUCCDNJQfj8sripKzwQyjdqHD3n3YPwiQfp&X-Amz-Signature=de3a9ed671adcdb31c9adf918df44599bd23e84b6b2a61db5d3a1718cee09338&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5LJ2GIB%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDgPah1SotQ9ycRHCPI2IQnvZZ%2F8IuSVABK0Ar7gQgW2AIgGLkjv18eumHru%2FKrwzD4qtiTZk5eUknC1KDwV%2B0X3rQq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDPEdt%2B0EYHbQIeiAXyrcA70uY5jUmFWohix%2FfGrTO1LDyIVI%2FHVn6tvpxmzY3j%2B83VH1GaZWSYAsFouM3BCAFObqw79EZudladvk5bB6Mo8KT%2FWuK95eTZrEA3%2BVkOnUdXpASpC9cQnWMBdxOk0gaboqOsHpy4AsPFm3iYN7b9ciXk9zf78MOXFW7GRy624aFXRxSeuhadUSvb5Po4fE0YytPAppTYkXbj5c5Woc%2FhJ2aDmhJ6tZQaXnAtECVABeluCUbxcVho4r9%2FWOe48OCDAI7CmDt6arhwFw4EsMWxWInWwnUb1TdYPmGHrDLudmdFHBUYY57hT59tpLWeLgdBxbozsZMQaz7CPCS6fUA8Wv8lYleis9M4H70YhBtRl%2BPkZH5sE0loBgjEWnb7MaOWCwTh7etrqx1KepPBAqSbee2g%2FPnsqIPXPt0r4TQOU5YBLN5hMaicrJa5TxfVU9NsqgrAih9lrikMdEZxXLTbB85iYL4nRJg%2B5VW7dyCZEYABd0%2FlxcdMN8djeucVc5uZ7gcksQh7VgkF1C7p9xZ7f44f8pIiiPmGAHx86qZP9cD%2FRTOZQDH0VYPjj4lkJlZR8U3n3jML2oJwswHkBqO60PBGONzBXi5ZK3XKF6r8bg5bIb85bNByDbHwSmMOmU5bwGOqUByw59YBoy7Zf4AwMiiZXKDP5b5aXPXtXaEoTvGJQ60YKR%2ByvkQPP%2FI2PKigqiTaeeaE78oTshL0VShkXdESphzVi8qGJP0%2Fl%2FKeCvAHomXxcWiP6WRyiuodgrGj6mCLiB60eX8s%2BwHBdg4KgaqXRuEpVcmUK9XsTiv5fFzM9TmCBNTysXf8QD3qPl04jsEt6G50Af27gscKMfI53h3nO0YdVx50zJ&X-Amz-Signature=e7f9bbb1fc9c179f7f8c1ca0a3df2fb096e475c542e602682aa270ba9d059286&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PMARNRY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIFHFgQv9RwTLvKHZP%2BdRGdn8XNihejveJnCCSwyJ0Nd5AiEAqH5xIA3dutKJR3zgafaaLymNS1hzatZ0j1zNaQ2%2Fvd0q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDIIkY6VdEIYFvV7sDircA9ksHnvyi3X3cxhuOw%2FLw9J0NEu9RSFqk%2BKt7ET67JYdzo95u9%2FinKOyhop3HaNY64%2FEb8dAfcbgdTM9%2BurnYl%2B6bKf%2BbgMSrDLUFE2BvgBy6cYODut2JmajI3LpHQYM8btsigSVFiH34hxXK%2B6IUcpk2PyuxT%2BVFOStXoBuktD6ElxyicgnUKs5Ha%2FgdumQYX69NvWeY6m1LqtN618Y7V78r7WLM%2Ff19vbhhIo8F68Cu58wwo%2FxNsUDcEsShnu3pIb7l8jaLiUWh3Vrs5JFG8XEwAuvCpotc3coa%2BJdOT8uQZmCdJIgdfpVzxWhELbpAa9zt4L1SVm3WPwIFkkrdVneTuCC9rC6kFxxFNNKl%2Bl6001Vc7mRayiehnGD7Mgfabp%2BTN3kxrdQpfgEqggXfzNiq19pM6fcjvywCGyOuw0gqDWrMZz4cSyfwiMRZXiKwjwIQ1PbvFhWy5sWlyXeNh1R28HdJaD0v%2FZNPUzTDMhjQLhDk13pXoMHtjWXn%2BCkxs1vgMaoHGVbibZ2T22iAzay5g1InSAeAYFatsFlsax1KTAeS%2Fq2HYAuO2oNII8lZ9HetJxqaIHPFbGXsFmo%2Bn3riyikOEp9zmTWe5fYzZErd2qYoOiV1TKjlxmLMM6U5bwGOqUBmp7zBP7wBDCmuwwzfoT8NR3FdrL%2BosafMe0I98ihS%2B5DuBh8fQZAx9AO2C84zSq4SelMtz7gZz9wwXWQ4FxHSipSkVdUcu%2BxpuoyysSr1Rbq9NbEnwdq4O%2BFo8ESRYj5oVjx9LnBye8L6r0ln5CWE8ekkwM6Q3rDFfAUZJ2p1UMzEaUnoGQOJQwFjECnPWmt3UVtnsO8Cdweof5dqLuloGo6xXl6&X-Amz-Signature=2ef1b1162bf7ffb769671cc87195b27b3fca1b792aafb87362ddb80775085d95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOION2XX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEFraGuw%2BUTdWVH8ojChwm%2BHD7%2By6CqvdOfdJPkror8SAiAJvSLI5atS%2FC%2Bzl4FitHT9lPKztXLVuj2Z3xhzT1dsXyr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM5afSZdRzIGqecakvKtwDJhYbY%2BbAMCR2OfJRGza5j7Z9Q%2Ben%2FVfkkC%2B1U%2BUMj2qNr0J6nmXshk%2BmjxUsMMb5coNYUZ2Bkx0TF%2FMssYErbBpbRxkyCBsrtXdW8wHm8T1P6fe%2F51gjJsIcuOO1SAV02tA6SMn3upl1z1j5yjWzzq1pmjGoMOvK66cyWx9yb4RbavID7LSQdvNjRZ8Er2hS6Fu37h07fxx4XFS2YvslRbiWtLW6zFY8p1ciYIhKezWe3QMEysAnB8KCzUGUUZJRYmMWJiNbc%2F9UY7NxMgN8Tv8i9KXUgam7wtvEC9WwnFlLsIdtA5H9n8F%2BcTisIZTaagzdNqIA367puuwjswWR9oRHPaUxBYV6QdpAT2SAZDtHLo07ACvUWzVi9dvZs%2BAs9dWIVSqEj1nFwdnKu8Zn08IuF9r5H5iO3aqbT%2F%2FiJfdd3Y3R7jbZJsadZ%2F5gqZf1lMtfnpispSFPymKY7GrbjnDVKEI%2FKkQtMgNvX15AbZxSOG8zwJyEGR72JPMNK3ys8l%2F6QU76xiRV3CF8ml0g8VX2tXqBQWV3NbGcaGwFOQBcuEBSz6qfV%2B2u87uHzXbqQ2EXyrSqh7sVxu7roWnQTO2ecB%2FkzEwX5bCSmUqhrvd5I9bG5Rbi7b%2FUfkEw05TlvAY6pgH%2Bd3fuXtsFnw%2Br6snN3tUs2CbcqZ023HjUxkVW3oQjedKVLnVgGI4wVBg1Vl3nPYvhmGhJSB%2FnbW1bpGTD4zJ0f59DgCyFPUEMkqAfRbbEQXtNs0MnK09hJ1btGDRqHPkwhSJEV15iBIkgV5P5gpSaSaWRsX6b2eM95jiEAu2gWwNxZxdPvvbTCwsDAOUCCDNJQfj8sripKzwQyjdqHD3n3YPwiQfp&X-Amz-Signature=621ecd6f2f6b7abd6df4d509af10028e1370729ee55396bb8f3f05a3891f75c6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOION2XX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEFraGuw%2BUTdWVH8ojChwm%2BHD7%2By6CqvdOfdJPkror8SAiAJvSLI5atS%2FC%2Bzl4FitHT9lPKztXLVuj2Z3xhzT1dsXyr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM5afSZdRzIGqecakvKtwDJhYbY%2BbAMCR2OfJRGza5j7Z9Q%2Ben%2FVfkkC%2B1U%2BUMj2qNr0J6nmXshk%2BmjxUsMMb5coNYUZ2Bkx0TF%2FMssYErbBpbRxkyCBsrtXdW8wHm8T1P6fe%2F51gjJsIcuOO1SAV02tA6SMn3upl1z1j5yjWzzq1pmjGoMOvK66cyWx9yb4RbavID7LSQdvNjRZ8Er2hS6Fu37h07fxx4XFS2YvslRbiWtLW6zFY8p1ciYIhKezWe3QMEysAnB8KCzUGUUZJRYmMWJiNbc%2F9UY7NxMgN8Tv8i9KXUgam7wtvEC9WwnFlLsIdtA5H9n8F%2BcTisIZTaagzdNqIA367puuwjswWR9oRHPaUxBYV6QdpAT2SAZDtHLo07ACvUWzVi9dvZs%2BAs9dWIVSqEj1nFwdnKu8Zn08IuF9r5H5iO3aqbT%2F%2FiJfdd3Y3R7jbZJsadZ%2F5gqZf1lMtfnpispSFPymKY7GrbjnDVKEI%2FKkQtMgNvX15AbZxSOG8zwJyEGR72JPMNK3ys8l%2F6QU76xiRV3CF8ml0g8VX2tXqBQWV3NbGcaGwFOQBcuEBSz6qfV%2B2u87uHzXbqQ2EXyrSqh7sVxu7roWnQTO2ecB%2FkzEwX5bCSmUqhrvd5I9bG5Rbi7b%2FUfkEw05TlvAY6pgH%2Bd3fuXtsFnw%2Br6snN3tUs2CbcqZ023HjUxkVW3oQjedKVLnVgGI4wVBg1Vl3nPYvhmGhJSB%2FnbW1bpGTD4zJ0f59DgCyFPUEMkqAfRbbEQXtNs0MnK09hJ1btGDRqHPkwhSJEV15iBIkgV5P5gpSaSaWRsX6b2eM95jiEAu2gWwNxZxdPvvbTCwsDAOUCCDNJQfj8sripKzwQyjdqHD3n3YPwiQfp&X-Amz-Signature=a78c28613c485c29b06867802829af78021d25c92585d7dea486eae62d1fc39b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOION2XX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEFraGuw%2BUTdWVH8ojChwm%2BHD7%2By6CqvdOfdJPkror8SAiAJvSLI5atS%2FC%2Bzl4FitHT9lPKztXLVuj2Z3xhzT1dsXyr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM5afSZdRzIGqecakvKtwDJhYbY%2BbAMCR2OfJRGza5j7Z9Q%2Ben%2FVfkkC%2B1U%2BUMj2qNr0J6nmXshk%2BmjxUsMMb5coNYUZ2Bkx0TF%2FMssYErbBpbRxkyCBsrtXdW8wHm8T1P6fe%2F51gjJsIcuOO1SAV02tA6SMn3upl1z1j5yjWzzq1pmjGoMOvK66cyWx9yb4RbavID7LSQdvNjRZ8Er2hS6Fu37h07fxx4XFS2YvslRbiWtLW6zFY8p1ciYIhKezWe3QMEysAnB8KCzUGUUZJRYmMWJiNbc%2F9UY7NxMgN8Tv8i9KXUgam7wtvEC9WwnFlLsIdtA5H9n8F%2BcTisIZTaagzdNqIA367puuwjswWR9oRHPaUxBYV6QdpAT2SAZDtHLo07ACvUWzVi9dvZs%2BAs9dWIVSqEj1nFwdnKu8Zn08IuF9r5H5iO3aqbT%2F%2FiJfdd3Y3R7jbZJsadZ%2F5gqZf1lMtfnpispSFPymKY7GrbjnDVKEI%2FKkQtMgNvX15AbZxSOG8zwJyEGR72JPMNK3ys8l%2F6QU76xiRV3CF8ml0g8VX2tXqBQWV3NbGcaGwFOQBcuEBSz6qfV%2B2u87uHzXbqQ2EXyrSqh7sVxu7roWnQTO2ecB%2FkzEwX5bCSmUqhrvd5I9bG5Rbi7b%2FUfkEw05TlvAY6pgH%2Bd3fuXtsFnw%2Br6snN3tUs2CbcqZ023HjUxkVW3oQjedKVLnVgGI4wVBg1Vl3nPYvhmGhJSB%2FnbW1bpGTD4zJ0f59DgCyFPUEMkqAfRbbEQXtNs0MnK09hJ1btGDRqHPkwhSJEV15iBIkgV5P5gpSaSaWRsX6b2eM95jiEAu2gWwNxZxdPvvbTCwsDAOUCCDNJQfj8sripKzwQyjdqHD3n3YPwiQfp&X-Amz-Signature=bba710d439e5983477b84a1cb555aed0793f0d90e0274a4c27ad857a322efcaf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUWCZYTC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIEHoUfQFD3pqQGmbKYwJt8wAoiboFckjQ3JiBCIRMO4KAiEApFI7SC25WjtirnzYwpYgl6%2F0%2FWhIrv8iox253NB1AhQq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDO89UIw8d8yF5Mz44yrcA%2BdD3XvHfriuT42eKvVsZEDU34Lhlv9QrjjLXP7Y0ByQcx5CA8DkBNZ1QNYGlUYEdy4p9fKa63%2Fa7CjVQuoKng0qR9B2BYw3DanpJHFxwtXZBal3hBfx27RNJ3xvsfX5ZUlcRnB20T4RbMKjqTHGCgfxfP9ZV3pHTqayV0x98sxw196TxRSFQQVfZTBXvuy2URyS%2BozP8l11VfYfPUZPM1UieGEWn1RQ1oNFa9ANtXMilFYS%2FkKydAPljaqsovMx2gg5MqRkERhrPTJLA8yroF4xFAagZK%2F8lA4aknSVJo7q%2BV%2BOnFekJyNpWW5IFq3yDmG2SkTPLyRCjuACrhlq5zX7q7P7kFh1P99lm925%2ByBUWd%2BYTipI4ghYIKYatr9vqdnukLgnVz1oJqolp4mMCa%2FYqW5VEf6XDeLfnbWL%2FHIzsnHD1W5xmKxjFt4Y82xV7B9cM2RLr%2FiVnkotZ3eXudy%2FPGuOoZFvqgunb%2FIh9VfARy9krFwMLaX9M83fiFavvMaFjZxUpxkoteNl4fejNKPz6ykol%2Flp545XZNzExaCgla%2FfpUWvHYhFjNfvit%2Ffq7esZQ1%2FHYZBAiU0tJLW6hOEmB3%2BBJfYv8wB%2B7zzkoyh0Bf5z4rLmW8hSVqUMN2U5bwGOqUBmmC4h%2F4l1hkdjeomSdojUQvpTIDlzA6Qc2dC9QLmUZqEOjOSTazoQVWDBOClw4IUhYjm8KSpktYFbVJo56TPKphDOS5DBTA824M4S%2Bb2Se9NthbpS%2FXmX1v6XrWju638bvct7gbXK%2BYddbT%2FJ3c8vT48xDhUsvdztH6uGcGo25MtZiU2bcpZsL7VyolMHnydobQfCtgpIy33do%2F8oXFy%2BNozkGdX&X-Amz-Signature=30d739863a7027cd42002d3fb139d38f3cb4075ce9e97b1c28f4f8a5c3798140&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VADG6VS%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIF6NqmSG8V43SB1dFjuezXPkRf4I81lFIvh%2BCn273Uh1AiB8ZkAioZXMbh28Q%2FIOu8%2BkNsC7evzXV6%2B6babjcV%2BM3Cr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMJIh8qpSD9JFiB0beKtwDDOi9z0%2FVGA1hNaxsvdCUY%2FmPKmmBgN90hTXRvdtWOxHPBX9Hai7epPd3FD9ivmO2DwXo4ZvqzCEdpj2T3wL498diqy4OZ6EdGQSVsb3%2BydKoiNe3zoGEO4XkP%2FUbuBw%2FS5347Px%2Bg82mjQUEwZjFprGXQ6kBkxU73rYoLDs3y4L%2F9Uk5tR42866a9Ba5amkM8LXuyy%2BkUvRMqWMgf4KET%2FCgUh7bRkIC1EoozsLTMTlyiBA0z7W4oLit%2FMPXR54NTOfxLmpCS8wGHiDhT7NBbuYETOXbT5F71R606rG0VZxMzAFUffuZ1XJlCsItAmjDua0K%2B6N4pDJbdbvJAHKA4l3gninMrBRikspydkoBrHS5CgMurpeyDMl83gzhVNqGA%2F7FmnwBBwKRVDstEVcSHaGmqc3B5i04l4hEP0JD4b6gjHPvlCsQDBtULO2iB3wfzEhhQSOkrmi4RSYTE58cixuWkJ6vVMIX8rIps4%2FmuM8CCqHmfvOgpvEez1t3JTM5E%2BaS8M2K2HVOUGuFsPU5JQsWCNr7N4YtL3QY76xXRygO8pvWbH3aeb%2BSo9dFIcM3hvbJelqI13Ds2KYwq216tXZ%2BkFxQiiqnOv59B9nBilrbFeLJQA8VzqSqHCQw%2BZTlvAY6pgHAobu8nmnGkIktoR9qDUQU2MU4vF1hv0qmr0LAVGS7oaRLRtcb2OHF%2BaigqOOqtXGWv3QhMsg6b23C5si86LAkRK0PNAk1DuVPrt0eg6mLOdVc%2BwBI%2FCLzx19NZZ3M4RC7TTUzXITbu2lU6wDS0npR1AEsO87atPnfqbGZFCt7uNqTzyPg764ZeFf9aBsA9fhBc8Av%2FjxCWEELH9uApx4Q4XALoehP&X-Amz-Signature=1ce12c0cf49a00dc60e7668b4626673a3ad186e512bddcbd72e9e4dd155c0ceb&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DZ4TNJ2%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCID29f1p9yO6dZqVW7vkqZtajW%2BDPhd8MzUo157vjZGZyAiEA2io0vRIGNmxXaRKvSDVWRCWuexrs55%2F0XIs6xwaGZsEq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDDE4hQ%2BE1%2F38a4WvWSrcAxN5FNccXwaPtkkT5b%2Bj02Qs6bnNqzztKNuGDW%2FTSQrWLVAsDXwX9HbHoRdKCU6RCDMdpvh238FrFew2vrkLHrGXUetEJPeMtK%2BHEm6kee4jAeC1OTO0fx0Vmtm3SdwBE%2B6bV3iu8JYvAhnwLwgGcZG%2BuNwVV3XFhVMNYvNI%2BTNBdf5htw3d%2F2I0yTJLENMKjlWcR379BVJ7HFPf1z0n94Aou7C59I3HcT%2Fe2%2FNT8SJPW2jsivLNU8J3yhneZ7cHpoeQ5pY%2F2%2FdYjd2qa1aWwm%2BKFQ4D6867OMMAK5KuqYswJWPT4glkOHKm03V6fo3IEydmxywB0OxbJ8Kzfy%2FvO8xa2qeblcoq7I%2FqKZPwQrU2RVYhVAyqrID6eAAzJhoy9fqvZlNaaCCC80lRGAHr0DMvCW%2BkBWDC9%2Fw0JpTa0Q0DBfy8lWu4hk0nX1htcMylJPnNQlX%2Fobx0KeQsz89%2BBXACqrPwYV%2BrMApG34LdbNmkDqTTrLaLUrBqyShxwV9gW%2BhfhKy29%2FCfgy2ix93jn2ijDENIv1HGbbLLe5YNt7qHJpC870k2YdBNnaQRRFALKXwNGlkOua4hdx7D2Eu0jlT3Coyi%2FGcMtNwt4maX14ZpvyYXTgW%2BxlQDa33rMNKU5bwGOqUBJ%2FLQFkk9EEg2KO6sInICCp%2FDS46wCUQI%2BeOIwoCrCsSH1GB1ZcJprofiPnPWaAMHpqUG8la6RuDVGzc9bMOARaE6RlDTf2SZ8e35JZCG8w47A0MYEPYU5MGSMqzNF%2FxQN8uCyGfyQuBFp5gmJrwa3kX0VnJP1TbwsHyXsXERIaO%2BVSfzkB9huzZYGeszCn9f%2FQ1UCUlkjQW0sMkRIDV5bznBt8W3&X-Amz-Signature=3da29faf4b4f6453e2435fb5694d9c75544656aebcf6a1d49bc5c6cd0619ec97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHFEL2Q7%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCW7gyakXsSHZB4HgRAMLtfAzxROuphhHr4npK5M%2BeysgIhAPjLHjK8b6OoUsNeZWU1cLqN4eU2ifcac1%2BgaWq4QdTWKv8DCH4QABoMNjM3NDIzMTgzODA1Igx4wRdJiBxlLD59YBcq3AMPfka7kKDJUlmnU8h6QLY5S349iHdwZ2j2YXnfPkbWtJ70nwlY1p5B7u%2BBrHiIGaYsOYY%2BDCJ2%2BcY94ZhU%2FIoYIbpGbgu0RwCcw8sFu1%2B6cJXf18tIk5SeZ3YIQCmMlWERJI6dZamX60x9egvvD7SjFn6YvfpY4AVQJ9dRjT5czoKy9q%2BWDy6IQnQawGjN2eM7eLf5RLg%2BGSrtFaTo1TT7E225r5GW1qofa%2FRqZm3gE7t03ozWAIzRrH9CMO6MdN6seuEM7mxMya14UUeOgrOvi84JppialENozV6Ok7OIiY0idsuG2%2FPS1SHdBAgjqzLuA2HXUgOd3CMhY6BkwzPynY47f%2BsS1ng9LGP4hzdEI7mXJKJEbB0S3dHFLdr3fjMzbJjfqIK98N%2FMB1MWKNsfC3QALkx2wXksScdJspyn%2BrLdMfZqepAi8aBbOXn9GN3XAI05W%2F7y8uq2AnMjrtEYRS01fgqp%2FFRhWg8lYUS0jgaWq%2B3ejYz3n%2F43PnIDfBVtSs2d%2FfwXDUTXAPZTS88l6CJQK16Y%2Bzui0Es%2F36f%2FOMhuY1%2Fu0QNB71UJGyYT07hT2EJednAnqG278hOFwx2LQvfuH7jdxftX6T4vITt%2BndKXBZdXspvOjlKlGDDtlOW8BjqkATCWCiJ1u%2FyHeptTSvbdoKcqrrlaaYBkxC8V%2BtFh%2BnQGIYLWxqmTMPPMsog1%2BepzbayfWhG6m7HOZEpVflZQ1Pc3nFZzXwsxmIKYS1OFR9OIqFwVoZatJRu%2Btz8CvwG91HocPLkv7NWdtod3DZ6OsvmcBfJgT2Vk0PBarcRNRUBnhB%2FMiw9rSEIOVyCA41Y81SqcJjIp5K9%2Bnv8pgcM9mZ8IiROM&X-Amz-Signature=aa54cf585afce3104c5023e4774c248be0451a3584f6d3ba4d78ecd11dc43def&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHFEL2Q7%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCW7gyakXsSHZB4HgRAMLtfAzxROuphhHr4npK5M%2BeysgIhAPjLHjK8b6OoUsNeZWU1cLqN4eU2ifcac1%2BgaWq4QdTWKv8DCH4QABoMNjM3NDIzMTgzODA1Igx4wRdJiBxlLD59YBcq3AMPfka7kKDJUlmnU8h6QLY5S349iHdwZ2j2YXnfPkbWtJ70nwlY1p5B7u%2BBrHiIGaYsOYY%2BDCJ2%2BcY94ZhU%2FIoYIbpGbgu0RwCcw8sFu1%2B6cJXf18tIk5SeZ3YIQCmMlWERJI6dZamX60x9egvvD7SjFn6YvfpY4AVQJ9dRjT5czoKy9q%2BWDy6IQnQawGjN2eM7eLf5RLg%2BGSrtFaTo1TT7E225r5GW1qofa%2FRqZm3gE7t03ozWAIzRrH9CMO6MdN6seuEM7mxMya14UUeOgrOvi84JppialENozV6Ok7OIiY0idsuG2%2FPS1SHdBAgjqzLuA2HXUgOd3CMhY6BkwzPynY47f%2BsS1ng9LGP4hzdEI7mXJKJEbB0S3dHFLdr3fjMzbJjfqIK98N%2FMB1MWKNsfC3QALkx2wXksScdJspyn%2BrLdMfZqepAi8aBbOXn9GN3XAI05W%2F7y8uq2AnMjrtEYRS01fgqp%2FFRhWg8lYUS0jgaWq%2B3ejYz3n%2F43PnIDfBVtSs2d%2FfwXDUTXAPZTS88l6CJQK16Y%2Bzui0Es%2F36f%2FOMhuY1%2Fu0QNB71UJGyYT07hT2EJednAnqG278hOFwx2LQvfuH7jdxftX6T4vITt%2BndKXBZdXspvOjlKlGDDtlOW8BjqkATCWCiJ1u%2FyHeptTSvbdoKcqrrlaaYBkxC8V%2BtFh%2BnQGIYLWxqmTMPPMsog1%2BepzbayfWhG6m7HOZEpVflZQ1Pc3nFZzXwsxmIKYS1OFR9OIqFwVoZatJRu%2Btz8CvwG91HocPLkv7NWdtod3DZ6OsvmcBfJgT2Vk0PBarcRNRUBnhB%2FMiw9rSEIOVyCA41Y81SqcJjIp5K9%2Bnv8pgcM9mZ8IiROM&X-Amz-Signature=9174f207234695965ebc8823b10f2858c48e5b68317c049f7b0a7d657a91301e&X-Amz-SignedHeaders=host&x-id=GetObject)

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
