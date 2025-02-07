

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H5TCLEI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHFkNldTQiMhP0q%2FAII4dM5UQ%2F9UMACPPNeRaoU54pyFAiEA%2F%2F8ATkvhtL%2BmeRxH0cuxcryrVBAaJgz1cl5GKfs1ZGMq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDVhryLDxqWGnUrjVSrcA2B7N205hAIZKVZ7ig6GW0cKs8CadwZAC5yHAeu9zML%2Bgq2kMTiEngE3WHsajuNUhOd3BMqMzsHbsT0dvKE2e2HQPQ6E4swInd7q2L7kggLJk0cwIlE1ZOOOEE2u0Ry6%2BaUxPq7rFHIms%2FLTqOePIQ3GChjBWzj96n9m%2Fr%2FfGBvhRJ25%2FKuQospLBZ8mw%2Bv5dK907Ed%2BJFZM2N88v%2F7vk29Hg2UDZp6DcZu7Yci2PaMZAeblk4W80fvi%2Fb2NMMjXO1fl9XswclrqcxiCT54f1MAG%2FiI9%2B9R9rsDKRZf07t2zWgOwSy%2BGZGR1qlIgImWVCWLP8uZvdiFy7KQndkLNKEBdISqLMJNeRWr3PjfL4mVweZbWF8MI4Kq9Qdu92c%2BjzS5OtT34VaASFNXjH8zF1YVGgL0CPvjmW0C5RbXwsonmvGfBbhXhAZPmbB50aQ5zCMZqHJ0NIobTgobx8FgHvKjwt5DdlIa0G00ky1TkD2OXxw3qQOApaf%2Fz8Z8vEzRB8LYUiZPIxK%2FEvyl6p8428AlviClwK35GcSVzv26huFLHLiotRnLkKyN8%2FZj6g7vafbipov%2B2ybvW9wQl4s2me5%2Bec%2BoMCXUCQBrCE%2BX2vRxQnJWhSwHrznV7Ka9zMOaZlb0GOqUBkhEN5rllPcWJeHNIk%2B8tRRKFnoWsoGi8jTdw5qDTg74FloqZbFakNuSMKr9DsLBIShPNvIP8%2FaHofavCxNJHiAJ9RtMRPJSPf3VckW2ANPeci6PC9iEIRq0mKQHPvXiP63uqqqMMdPMiBnnpU1h%2FqyALtb9l58YC5jKiBHBHTbNLpyJzWq8aqo6LBd4wvYd30rSo3AOV7KXRDNEWWoOKBB1kav1d&X-Amz-Signature=c063f270154758aca4df087ebbdcd5ab98720e706d710acf1be3e91bfc36d35d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H5TCLEI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHFkNldTQiMhP0q%2FAII4dM5UQ%2F9UMACPPNeRaoU54pyFAiEA%2F%2F8ATkvhtL%2BmeRxH0cuxcryrVBAaJgz1cl5GKfs1ZGMq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDVhryLDxqWGnUrjVSrcA2B7N205hAIZKVZ7ig6GW0cKs8CadwZAC5yHAeu9zML%2Bgq2kMTiEngE3WHsajuNUhOd3BMqMzsHbsT0dvKE2e2HQPQ6E4swInd7q2L7kggLJk0cwIlE1ZOOOEE2u0Ry6%2BaUxPq7rFHIms%2FLTqOePIQ3GChjBWzj96n9m%2Fr%2FfGBvhRJ25%2FKuQospLBZ8mw%2Bv5dK907Ed%2BJFZM2N88v%2F7vk29Hg2UDZp6DcZu7Yci2PaMZAeblk4W80fvi%2Fb2NMMjXO1fl9XswclrqcxiCT54f1MAG%2FiI9%2B9R9rsDKRZf07t2zWgOwSy%2BGZGR1qlIgImWVCWLP8uZvdiFy7KQndkLNKEBdISqLMJNeRWr3PjfL4mVweZbWF8MI4Kq9Qdu92c%2BjzS5OtT34VaASFNXjH8zF1YVGgL0CPvjmW0C5RbXwsonmvGfBbhXhAZPmbB50aQ5zCMZqHJ0NIobTgobx8FgHvKjwt5DdlIa0G00ky1TkD2OXxw3qQOApaf%2Fz8Z8vEzRB8LYUiZPIxK%2FEvyl6p8428AlviClwK35GcSVzv26huFLHLiotRnLkKyN8%2FZj6g7vafbipov%2B2ybvW9wQl4s2me5%2Bec%2BoMCXUCQBrCE%2BX2vRxQnJWhSwHrznV7Ka9zMOaZlb0GOqUBkhEN5rllPcWJeHNIk%2B8tRRKFnoWsoGi8jTdw5qDTg74FloqZbFakNuSMKr9DsLBIShPNvIP8%2FaHofavCxNJHiAJ9RtMRPJSPf3VckW2ANPeci6PC9iEIRq0mKQHPvXiP63uqqqMMdPMiBnnpU1h%2FqyALtb9l58YC5jKiBHBHTbNLpyJzWq8aqo6LBd4wvYd30rSo3AOV7KXRDNEWWoOKBB1kav1d&X-Amz-Signature=ae4035a8bf16ed9fe604c496dd9b37e146182bbd30520581e2a4a747c65ca339&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H5TCLEI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHFkNldTQiMhP0q%2FAII4dM5UQ%2F9UMACPPNeRaoU54pyFAiEA%2F%2F8ATkvhtL%2BmeRxH0cuxcryrVBAaJgz1cl5GKfs1ZGMq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDVhryLDxqWGnUrjVSrcA2B7N205hAIZKVZ7ig6GW0cKs8CadwZAC5yHAeu9zML%2Bgq2kMTiEngE3WHsajuNUhOd3BMqMzsHbsT0dvKE2e2HQPQ6E4swInd7q2L7kggLJk0cwIlE1ZOOOEE2u0Ry6%2BaUxPq7rFHIms%2FLTqOePIQ3GChjBWzj96n9m%2Fr%2FfGBvhRJ25%2FKuQospLBZ8mw%2Bv5dK907Ed%2BJFZM2N88v%2F7vk29Hg2UDZp6DcZu7Yci2PaMZAeblk4W80fvi%2Fb2NMMjXO1fl9XswclrqcxiCT54f1MAG%2FiI9%2B9R9rsDKRZf07t2zWgOwSy%2BGZGR1qlIgImWVCWLP8uZvdiFy7KQndkLNKEBdISqLMJNeRWr3PjfL4mVweZbWF8MI4Kq9Qdu92c%2BjzS5OtT34VaASFNXjH8zF1YVGgL0CPvjmW0C5RbXwsonmvGfBbhXhAZPmbB50aQ5zCMZqHJ0NIobTgobx8FgHvKjwt5DdlIa0G00ky1TkD2OXxw3qQOApaf%2Fz8Z8vEzRB8LYUiZPIxK%2FEvyl6p8428AlviClwK35GcSVzv26huFLHLiotRnLkKyN8%2FZj6g7vafbipov%2B2ybvW9wQl4s2me5%2Bec%2BoMCXUCQBrCE%2BX2vRxQnJWhSwHrznV7Ka9zMOaZlb0GOqUBkhEN5rllPcWJeHNIk%2B8tRRKFnoWsoGi8jTdw5qDTg74FloqZbFakNuSMKr9DsLBIShPNvIP8%2FaHofavCxNJHiAJ9RtMRPJSPf3VckW2ANPeci6PC9iEIRq0mKQHPvXiP63uqqqMMdPMiBnnpU1h%2FqyALtb9l58YC5jKiBHBHTbNLpyJzWq8aqo6LBd4wvYd30rSo3AOV7KXRDNEWWoOKBB1kav1d&X-Amz-Signature=c7538e150978d5ad4633a10aac369186a860666291af3e6f7dc3348d7bc12681&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMZTVTNK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDgWqqtouGXE%2BY44pg26S2oq%2FS8P5WVSBrz7gnHtklmhwIhAIiCJALpPm%2F8fCvvm5%2BmfZwgp%2F0%2BTdcI6eA4%2BGiqbbTbKv8DCGkQABoMNjM3NDIzMTgzODA1IgyhhigcpLoBk3wYzAAq3APXk8n%2BKwyU0KqyB7pD7ZE6noltB4%2F5DMjSR%2FXdHyq5w80DBE9kkNOd%2Fl7ayky5p8w%2FV0RfhMUXMOgB3rD5xcM7FBqnpq0ZRAUED77jtkgJLNOxR82eYu7axDAkInwpVKkSUPsL0Y9dgx4pcI7kb41e7aujrlE39cPqdvlIASw%2FTRk7yPqdAUkFK9c8ZemWE7v6pwy1TDqYc0YT5IMKwsLxp6UNVB26bdcREz2UGiDtjTiGfSeGBAzE1wyfjuXTxaxTBiJEU%2BwIwR7vdQm%2F7nxoWnbPbuhIEyx0V%2BL6HZOjTY5%2Bbk4Hfr5QN5bgVi5fg2T65THHj5LTX26LxHbLuoC4rtaHrfDj%2BVQffFlWv83nvUEY8J6U3zxzJChhJE2rkJh5u4ltoJlTWiOfztw3ltNlbxr1%2FrHndlU5i33VyCOZSbjrb%2FyTK16MIsZZDCFg3OswEtJdVxdsLLcv%2FMXJ5RBpEIUzxzsk9QOHzo%2BW%2BNDCsZGiHoRk%2FjRpLYJVfg7Xu%2Ff7LrVTDekJdyD%2BRjy%2BB723vvGwEadKyGF%2BhRrkogHiqwQp4c3LknNtrzgkELIJbARJnIQHSYg%2F754TVGERWeUyvZkGmRhOEe1MwemyL82%2B8LtExx%2BG6v%2FDKgRCbTClmpW9BjqkAfKOTpZhKLXl3ZglIsb32NtOky3VtgYYrDzyWzkZQCClA%2FejqQbjE4oGeA%2FVy4CM4617E6gWfUoPPvT53tYzNfnRzdmhT92N72whUu%2F8MtBXc28A6t%2BSorb4eqE4rU%2Fgrb1vRac%2BSfem3np0Hcb8G%2FLHNo3sPQ3ziaEvJmd28%2BqRFYlnbUGPUYA50tdSQxf7McOTR4NH8UBoc1M88vWNOj%2FCue40&X-Amz-Signature=1a2ae29fb69db0c9e7be2ce746b3a5bf38be765cfe7bf7f3007a8f78d28af151&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMZTVTNK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDgWqqtouGXE%2BY44pg26S2oq%2FS8P5WVSBrz7gnHtklmhwIhAIiCJALpPm%2F8fCvvm5%2BmfZwgp%2F0%2BTdcI6eA4%2BGiqbbTbKv8DCGkQABoMNjM3NDIzMTgzODA1IgyhhigcpLoBk3wYzAAq3APXk8n%2BKwyU0KqyB7pD7ZE6noltB4%2F5DMjSR%2FXdHyq5w80DBE9kkNOd%2Fl7ayky5p8w%2FV0RfhMUXMOgB3rD5xcM7FBqnpq0ZRAUED77jtkgJLNOxR82eYu7axDAkInwpVKkSUPsL0Y9dgx4pcI7kb41e7aujrlE39cPqdvlIASw%2FTRk7yPqdAUkFK9c8ZemWE7v6pwy1TDqYc0YT5IMKwsLxp6UNVB26bdcREz2UGiDtjTiGfSeGBAzE1wyfjuXTxaxTBiJEU%2BwIwR7vdQm%2F7nxoWnbPbuhIEyx0V%2BL6HZOjTY5%2Bbk4Hfr5QN5bgVi5fg2T65THHj5LTX26LxHbLuoC4rtaHrfDj%2BVQffFlWv83nvUEY8J6U3zxzJChhJE2rkJh5u4ltoJlTWiOfztw3ltNlbxr1%2FrHndlU5i33VyCOZSbjrb%2FyTK16MIsZZDCFg3OswEtJdVxdsLLcv%2FMXJ5RBpEIUzxzsk9QOHzo%2BW%2BNDCsZGiHoRk%2FjRpLYJVfg7Xu%2Ff7LrVTDekJdyD%2BRjy%2BB723vvGwEadKyGF%2BhRrkogHiqwQp4c3LknNtrzgkELIJbARJnIQHSYg%2F754TVGERWeUyvZkGmRhOEe1MwemyL82%2B8LtExx%2BG6v%2FDKgRCbTClmpW9BjqkAfKOTpZhKLXl3ZglIsb32NtOky3VtgYYrDzyWzkZQCClA%2FejqQbjE4oGeA%2FVy4CM4617E6gWfUoPPvT53tYzNfnRzdmhT92N72whUu%2F8MtBXc28A6t%2BSorb4eqE4rU%2Fgrb1vRac%2BSfem3np0Hcb8G%2FLHNo3sPQ3ziaEvJmd28%2BqRFYlnbUGPUYA50tdSQxf7McOTR4NH8UBoc1M88vWNOj%2FCue40&X-Amz-Signature=b42c7e0ba211cb4c819fd54229f654c468375a009862c91b8848abd6b0e7451f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMZTVTNK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDgWqqtouGXE%2BY44pg26S2oq%2FS8P5WVSBrz7gnHtklmhwIhAIiCJALpPm%2F8fCvvm5%2BmfZwgp%2F0%2BTdcI6eA4%2BGiqbbTbKv8DCGkQABoMNjM3NDIzMTgzODA1IgyhhigcpLoBk3wYzAAq3APXk8n%2BKwyU0KqyB7pD7ZE6noltB4%2F5DMjSR%2FXdHyq5w80DBE9kkNOd%2Fl7ayky5p8w%2FV0RfhMUXMOgB3rD5xcM7FBqnpq0ZRAUED77jtkgJLNOxR82eYu7axDAkInwpVKkSUPsL0Y9dgx4pcI7kb41e7aujrlE39cPqdvlIASw%2FTRk7yPqdAUkFK9c8ZemWE7v6pwy1TDqYc0YT5IMKwsLxp6UNVB26bdcREz2UGiDtjTiGfSeGBAzE1wyfjuXTxaxTBiJEU%2BwIwR7vdQm%2F7nxoWnbPbuhIEyx0V%2BL6HZOjTY5%2Bbk4Hfr5QN5bgVi5fg2T65THHj5LTX26LxHbLuoC4rtaHrfDj%2BVQffFlWv83nvUEY8J6U3zxzJChhJE2rkJh5u4ltoJlTWiOfztw3ltNlbxr1%2FrHndlU5i33VyCOZSbjrb%2FyTK16MIsZZDCFg3OswEtJdVxdsLLcv%2FMXJ5RBpEIUzxzsk9QOHzo%2BW%2BNDCsZGiHoRk%2FjRpLYJVfg7Xu%2Ff7LrVTDekJdyD%2BRjy%2BB723vvGwEadKyGF%2BhRrkogHiqwQp4c3LknNtrzgkELIJbARJnIQHSYg%2F754TVGERWeUyvZkGmRhOEe1MwemyL82%2B8LtExx%2BG6v%2FDKgRCbTClmpW9BjqkAfKOTpZhKLXl3ZglIsb32NtOky3VtgYYrDzyWzkZQCClA%2FejqQbjE4oGeA%2FVy4CM4617E6gWfUoPPvT53tYzNfnRzdmhT92N72whUu%2F8MtBXc28A6t%2BSorb4eqE4rU%2Fgrb1vRac%2BSfem3np0Hcb8G%2FLHNo3sPQ3ziaEvJmd28%2BqRFYlnbUGPUYA50tdSQxf7McOTR4NH8UBoc1M88vWNOj%2FCue40&X-Amz-Signature=f224acbf27387f3f4571340da7fe61bb66d6efc5d53226aee4f0e2dd63a065e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMZTVTNK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDgWqqtouGXE%2BY44pg26S2oq%2FS8P5WVSBrz7gnHtklmhwIhAIiCJALpPm%2F8fCvvm5%2BmfZwgp%2F0%2BTdcI6eA4%2BGiqbbTbKv8DCGkQABoMNjM3NDIzMTgzODA1IgyhhigcpLoBk3wYzAAq3APXk8n%2BKwyU0KqyB7pD7ZE6noltB4%2F5DMjSR%2FXdHyq5w80DBE9kkNOd%2Fl7ayky5p8w%2FV0RfhMUXMOgB3rD5xcM7FBqnpq0ZRAUED77jtkgJLNOxR82eYu7axDAkInwpVKkSUPsL0Y9dgx4pcI7kb41e7aujrlE39cPqdvlIASw%2FTRk7yPqdAUkFK9c8ZemWE7v6pwy1TDqYc0YT5IMKwsLxp6UNVB26bdcREz2UGiDtjTiGfSeGBAzE1wyfjuXTxaxTBiJEU%2BwIwR7vdQm%2F7nxoWnbPbuhIEyx0V%2BL6HZOjTY5%2Bbk4Hfr5QN5bgVi5fg2T65THHj5LTX26LxHbLuoC4rtaHrfDj%2BVQffFlWv83nvUEY8J6U3zxzJChhJE2rkJh5u4ltoJlTWiOfztw3ltNlbxr1%2FrHndlU5i33VyCOZSbjrb%2FyTK16MIsZZDCFg3OswEtJdVxdsLLcv%2FMXJ5RBpEIUzxzsk9QOHzo%2BW%2BNDCsZGiHoRk%2FjRpLYJVfg7Xu%2Ff7LrVTDekJdyD%2BRjy%2BB723vvGwEadKyGF%2BhRrkogHiqwQp4c3LknNtrzgkELIJbARJnIQHSYg%2F754TVGERWeUyvZkGmRhOEe1MwemyL82%2B8LtExx%2BG6v%2FDKgRCbTClmpW9BjqkAfKOTpZhKLXl3ZglIsb32NtOky3VtgYYrDzyWzkZQCClA%2FejqQbjE4oGeA%2FVy4CM4617E6gWfUoPPvT53tYzNfnRzdmhT92N72whUu%2F8MtBXc28A6t%2BSorb4eqE4rU%2Fgrb1vRac%2BSfem3np0Hcb8G%2FLHNo3sPQ3ziaEvJmd28%2BqRFYlnbUGPUYA50tdSQxf7McOTR4NH8UBoc1M88vWNOj%2FCue40&X-Amz-Signature=957ebd508080874546be71f0d52238b1b37808e54915685943edc4bf135249f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMZTVTNK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDgWqqtouGXE%2BY44pg26S2oq%2FS8P5WVSBrz7gnHtklmhwIhAIiCJALpPm%2F8fCvvm5%2BmfZwgp%2F0%2BTdcI6eA4%2BGiqbbTbKv8DCGkQABoMNjM3NDIzMTgzODA1IgyhhigcpLoBk3wYzAAq3APXk8n%2BKwyU0KqyB7pD7ZE6noltB4%2F5DMjSR%2FXdHyq5w80DBE9kkNOd%2Fl7ayky5p8w%2FV0RfhMUXMOgB3rD5xcM7FBqnpq0ZRAUED77jtkgJLNOxR82eYu7axDAkInwpVKkSUPsL0Y9dgx4pcI7kb41e7aujrlE39cPqdvlIASw%2FTRk7yPqdAUkFK9c8ZemWE7v6pwy1TDqYc0YT5IMKwsLxp6UNVB26bdcREz2UGiDtjTiGfSeGBAzE1wyfjuXTxaxTBiJEU%2BwIwR7vdQm%2F7nxoWnbPbuhIEyx0V%2BL6HZOjTY5%2Bbk4Hfr5QN5bgVi5fg2T65THHj5LTX26LxHbLuoC4rtaHrfDj%2BVQffFlWv83nvUEY8J6U3zxzJChhJE2rkJh5u4ltoJlTWiOfztw3ltNlbxr1%2FrHndlU5i33VyCOZSbjrb%2FyTK16MIsZZDCFg3OswEtJdVxdsLLcv%2FMXJ5RBpEIUzxzsk9QOHzo%2BW%2BNDCsZGiHoRk%2FjRpLYJVfg7Xu%2Ff7LrVTDekJdyD%2BRjy%2BB723vvGwEadKyGF%2BhRrkogHiqwQp4c3LknNtrzgkELIJbARJnIQHSYg%2F754TVGERWeUyvZkGmRhOEe1MwemyL82%2B8LtExx%2BG6v%2FDKgRCbTClmpW9BjqkAfKOTpZhKLXl3ZglIsb32NtOky3VtgYYrDzyWzkZQCClA%2FejqQbjE4oGeA%2FVy4CM4617E6gWfUoPPvT53tYzNfnRzdmhT92N72whUu%2F8MtBXc28A6t%2BSorb4eqE4rU%2Fgrb1vRac%2BSfem3np0Hcb8G%2FLHNo3sPQ3ziaEvJmd28%2BqRFYlnbUGPUYA50tdSQxf7McOTR4NH8UBoc1M88vWNOj%2FCue40&X-Amz-Signature=a8bf8622dd9b3ace6d6b2d34716db7ad0dbe552b38676b5b16631692135edca5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMZTVTNK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDgWqqtouGXE%2BY44pg26S2oq%2FS8P5WVSBrz7gnHtklmhwIhAIiCJALpPm%2F8fCvvm5%2BmfZwgp%2F0%2BTdcI6eA4%2BGiqbbTbKv8DCGkQABoMNjM3NDIzMTgzODA1IgyhhigcpLoBk3wYzAAq3APXk8n%2BKwyU0KqyB7pD7ZE6noltB4%2F5DMjSR%2FXdHyq5w80DBE9kkNOd%2Fl7ayky5p8w%2FV0RfhMUXMOgB3rD5xcM7FBqnpq0ZRAUED77jtkgJLNOxR82eYu7axDAkInwpVKkSUPsL0Y9dgx4pcI7kb41e7aujrlE39cPqdvlIASw%2FTRk7yPqdAUkFK9c8ZemWE7v6pwy1TDqYc0YT5IMKwsLxp6UNVB26bdcREz2UGiDtjTiGfSeGBAzE1wyfjuXTxaxTBiJEU%2BwIwR7vdQm%2F7nxoWnbPbuhIEyx0V%2BL6HZOjTY5%2Bbk4Hfr5QN5bgVi5fg2T65THHj5LTX26LxHbLuoC4rtaHrfDj%2BVQffFlWv83nvUEY8J6U3zxzJChhJE2rkJh5u4ltoJlTWiOfztw3ltNlbxr1%2FrHndlU5i33VyCOZSbjrb%2FyTK16MIsZZDCFg3OswEtJdVxdsLLcv%2FMXJ5RBpEIUzxzsk9QOHzo%2BW%2BNDCsZGiHoRk%2FjRpLYJVfg7Xu%2Ff7LrVTDekJdyD%2BRjy%2BB723vvGwEadKyGF%2BhRrkogHiqwQp4c3LknNtrzgkELIJbARJnIQHSYg%2F754TVGERWeUyvZkGmRhOEe1MwemyL82%2B8LtExx%2BG6v%2FDKgRCbTClmpW9BjqkAfKOTpZhKLXl3ZglIsb32NtOky3VtgYYrDzyWzkZQCClA%2FejqQbjE4oGeA%2FVy4CM4617E6gWfUoPPvT53tYzNfnRzdmhT92N72whUu%2F8MtBXc28A6t%2BSorb4eqE4rU%2Fgrb1vRac%2BSfem3np0Hcb8G%2FLHNo3sPQ3ziaEvJmd28%2BqRFYlnbUGPUYA50tdSQxf7McOTR4NH8UBoc1M88vWNOj%2FCue40&X-Amz-Signature=13da5b108ce9b83dc71b31f9dbe5033e001fdfbce6b10a0dc7f7251ed2e67b7b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5PTIGAM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDkhwAws79oDKiqYGRgzjWSAf%2BR3bOVXUr7%2F6rKDfgmkQIhANvPXnTRIVJ8qW9I7wDobwoMtnBjhkuU29rhAPBT0yfvKv8DCGkQABoMNjM3NDIzMTgzODA1Igw7dHjO%2FxDJjkwABUIq3AMEnHPIXCZRImCu8UIeY0TtI%2BU9nrz7mJgqCoK9oFEJskhTRZOzf%2FPPrMC8mAX1gSiZOYrZOXor4Viz%2BpYmqf8LoIpoZtraP0HyZYVFV1gVY4ihMsGKl4qJ7n548ExTXemxv58FZwq6gl98fLmgmyPO19Xlq9Vz4ILUgBf3Di0P94MqnNoVCAzbSLdWXqS4rJntw0jJmAtTXiaGwx12tI2ZMuuE23rvc0112CDfs%2FXOT%2BJGfS03u1acrGj00uj5wslKt%2FsnJuviath5kyXVlgX%2FsIIgtuyEa5mDOKYJJqBVnieq2k4uh%2F%2BkpZ0fmNl6%2FMNjZZ%2FIxYpYWd50Wa49Ag2lM1Mhzd0Opctstu8jipTwbD6FWt%2BEY2iTBPGKfZUDeCNt8zyvjk%2BeNuIhDPnNVg1fh8nSEKfrvXsMY7ubAb3B5i00EUSPr7YpldfIlszp58SwaLxUYjDtIaa%2BVZrljUEDsdo%2F7A1nb9LaXp31NrVbLVgBAY6P2n0n3m3fNGbd3DRIcU7u1z4NdZQyEvbpxSEjcCh5ZXe7sVj8%2BfF72vT3nTSUXe7csaoARhlf1I%2BAdDx8g25E2HzLvGlzlR%2B0WTg3qUO90GctuEMAuHbe6XfVcTQyTY53ADjIxNrnizDKmpW9BjqkARtDXw05ZZDH4rWaWcW3y70tt4e5JmWJBdR%2BzJcpcMvyWWjeHKfARX1P58mnfxrNRJhlSgCgXKQ6Nw6mwl25wMfeD8vDWq488DWJ6CEpP4irJJnWebf9FWskuSmv%2B2tGW88RrPvpKl2F6gCBesx507GCT6rB8%2F9nmDZJizQ02NbUGk3nqAMxhFKM39cuCoFHrXqSXgRPhjNC4Q8%2Bee4gjNUy2lBd&X-Amz-Signature=0aa9ed6c357b1770c30e5cc5e01a2f2ece1d85b129789ad6c6c7463fadc58d63&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCY6YJF4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDn4VSKF4dO2UwAKuysS03eEHEXilfvc%2BChEESKd1WBUAiEAjdaSdq5Oj3Knv%2FMSODhfhaT%2BQ2rCibRROU4JgJ9QUVIq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDOznN5slEe%2FSn68F3yrcA14ExBxPcfNaj3xHVhOdQtO2KEnOGcKV9lDlYCe1cTQcOA7xq29QnKRFmEdBB8mxAvuZLPRRyRFq3lGeHt6NerHz2LX7pyyHzIhLJAWprojdlFgbOo2w8uGKScj4VA9Z0Viyh1aeyI57%2Bm%2BoBjv5lTDwXxvs3lIsl5fBX2sMLHxtjwOdQ1xzlJhTrIfdeYytn7TVJXcJf9UJQfrpzIJFJA0yueCvD9Cq0O%2FcNggS%2BmzpLvvSg1MPRQDzMJ1ao1WZ7XwEU9KbqugOzLr3pBz%2Bo6XJfObkgZjnZ6ShN2f8CKo2o3WLpUwskSOnL%2FIOs6Wm%2FJgHjKfLqYSDIKtcyAEbrWD5ZF13CEmX5ybGqQ1Hvj6pOLcxDbTki90PiPpBWbMc6uqiit%2BWeT1yf4sYNo5l5pyStnjPApfovq%2BgdR7eUra4SETlccGE09ouJoj9bEyVq%2F7X%2BLio4TjLMU5ux9Ykq9pga0rtMH08d9PXNaw2IFUxWxylZan%2B5P%2BedDg8D6pQQ%2FAhW8IJjE72mtHNJLQNn7EYWS2BAkdMSC9U3VLX1GhBgLbYy0ipArCCVsXPgn7s4XO2DkmpVYj8hfhhl7zao9lD1uimESv%2FRbrozx7l5c33O7%2FtdM%2FKriGuIYDFMOaZlb0GOqUBq5FKnG0j7HqsWdWL7FBMC6FRie8d%2BrLfgLREQXHvxtlzNtcDY7MKHy4CtEOWtOezjQcYOAzU7XVunsZ2KvsFSynKmNiFoihkRLllX%2Fn%2BooAMEGvZot8UM%2B1aha2d2nhaTajgKKS4oQ%2BACBWSjZEGdiJIb7jiSVUDgYPw0d3eF9njNjYHkhIZSwTr7AHq3%2Bj60cGbK0oS02APxc5NSlIP5kH%2BLG69&X-Amz-Signature=4ca979b7361b82f373733f9796d354d62d89190b1d51e4a5e3a455073260eea7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMZTVTNK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDgWqqtouGXE%2BY44pg26S2oq%2FS8P5WVSBrz7gnHtklmhwIhAIiCJALpPm%2F8fCvvm5%2BmfZwgp%2F0%2BTdcI6eA4%2BGiqbbTbKv8DCGkQABoMNjM3NDIzMTgzODA1IgyhhigcpLoBk3wYzAAq3APXk8n%2BKwyU0KqyB7pD7ZE6noltB4%2F5DMjSR%2FXdHyq5w80DBE9kkNOd%2Fl7ayky5p8w%2FV0RfhMUXMOgB3rD5xcM7FBqnpq0ZRAUED77jtkgJLNOxR82eYu7axDAkInwpVKkSUPsL0Y9dgx4pcI7kb41e7aujrlE39cPqdvlIASw%2FTRk7yPqdAUkFK9c8ZemWE7v6pwy1TDqYc0YT5IMKwsLxp6UNVB26bdcREz2UGiDtjTiGfSeGBAzE1wyfjuXTxaxTBiJEU%2BwIwR7vdQm%2F7nxoWnbPbuhIEyx0V%2BL6HZOjTY5%2Bbk4Hfr5QN5bgVi5fg2T65THHj5LTX26LxHbLuoC4rtaHrfDj%2BVQffFlWv83nvUEY8J6U3zxzJChhJE2rkJh5u4ltoJlTWiOfztw3ltNlbxr1%2FrHndlU5i33VyCOZSbjrb%2FyTK16MIsZZDCFg3OswEtJdVxdsLLcv%2FMXJ5RBpEIUzxzsk9QOHzo%2BW%2BNDCsZGiHoRk%2FjRpLYJVfg7Xu%2Ff7LrVTDekJdyD%2BRjy%2BB723vvGwEadKyGF%2BhRrkogHiqwQp4c3LknNtrzgkELIJbARJnIQHSYg%2F754TVGERWeUyvZkGmRhOEe1MwemyL82%2B8LtExx%2BG6v%2FDKgRCbTClmpW9BjqkAfKOTpZhKLXl3ZglIsb32NtOky3VtgYYrDzyWzkZQCClA%2FejqQbjE4oGeA%2FVy4CM4617E6gWfUoPPvT53tYzNfnRzdmhT92N72whUu%2F8MtBXc28A6t%2BSorb4eqE4rU%2Fgrb1vRac%2BSfem3np0Hcb8G%2FLHNo3sPQ3ziaEvJmd28%2BqRFYlnbUGPUYA50tdSQxf7McOTR4NH8UBoc1M88vWNOj%2FCue40&X-Amz-Signature=5f1f6f1082cf21043998947d76684c7ca03afc5a846b828f3300a01590225998&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMZTVTNK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDgWqqtouGXE%2BY44pg26S2oq%2FS8P5WVSBrz7gnHtklmhwIhAIiCJALpPm%2F8fCvvm5%2BmfZwgp%2F0%2BTdcI6eA4%2BGiqbbTbKv8DCGkQABoMNjM3NDIzMTgzODA1IgyhhigcpLoBk3wYzAAq3APXk8n%2BKwyU0KqyB7pD7ZE6noltB4%2F5DMjSR%2FXdHyq5w80DBE9kkNOd%2Fl7ayky5p8w%2FV0RfhMUXMOgB3rD5xcM7FBqnpq0ZRAUED77jtkgJLNOxR82eYu7axDAkInwpVKkSUPsL0Y9dgx4pcI7kb41e7aujrlE39cPqdvlIASw%2FTRk7yPqdAUkFK9c8ZemWE7v6pwy1TDqYc0YT5IMKwsLxp6UNVB26bdcREz2UGiDtjTiGfSeGBAzE1wyfjuXTxaxTBiJEU%2BwIwR7vdQm%2F7nxoWnbPbuhIEyx0V%2BL6HZOjTY5%2Bbk4Hfr5QN5bgVi5fg2T65THHj5LTX26LxHbLuoC4rtaHrfDj%2BVQffFlWv83nvUEY8J6U3zxzJChhJE2rkJh5u4ltoJlTWiOfztw3ltNlbxr1%2FrHndlU5i33VyCOZSbjrb%2FyTK16MIsZZDCFg3OswEtJdVxdsLLcv%2FMXJ5RBpEIUzxzsk9QOHzo%2BW%2BNDCsZGiHoRk%2FjRpLYJVfg7Xu%2Ff7LrVTDekJdyD%2BRjy%2BB723vvGwEadKyGF%2BhRrkogHiqwQp4c3LknNtrzgkELIJbARJnIQHSYg%2F754TVGERWeUyvZkGmRhOEe1MwemyL82%2B8LtExx%2BG6v%2FDKgRCbTClmpW9BjqkAfKOTpZhKLXl3ZglIsb32NtOky3VtgYYrDzyWzkZQCClA%2FejqQbjE4oGeA%2FVy4CM4617E6gWfUoPPvT53tYzNfnRzdmhT92N72whUu%2F8MtBXc28A6t%2BSorb4eqE4rU%2Fgrb1vRac%2BSfem3np0Hcb8G%2FLHNo3sPQ3ziaEvJmd28%2BqRFYlnbUGPUYA50tdSQxf7McOTR4NH8UBoc1M88vWNOj%2FCue40&X-Amz-Signature=7bc4bb71318319d30e4e4d91f0d5861b87cce514d4d8a4e8148d34e1499f6a4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMZTVTNK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDgWqqtouGXE%2BY44pg26S2oq%2FS8P5WVSBrz7gnHtklmhwIhAIiCJALpPm%2F8fCvvm5%2BmfZwgp%2F0%2BTdcI6eA4%2BGiqbbTbKv8DCGkQABoMNjM3NDIzMTgzODA1IgyhhigcpLoBk3wYzAAq3APXk8n%2BKwyU0KqyB7pD7ZE6noltB4%2F5DMjSR%2FXdHyq5w80DBE9kkNOd%2Fl7ayky5p8w%2FV0RfhMUXMOgB3rD5xcM7FBqnpq0ZRAUED77jtkgJLNOxR82eYu7axDAkInwpVKkSUPsL0Y9dgx4pcI7kb41e7aujrlE39cPqdvlIASw%2FTRk7yPqdAUkFK9c8ZemWE7v6pwy1TDqYc0YT5IMKwsLxp6UNVB26bdcREz2UGiDtjTiGfSeGBAzE1wyfjuXTxaxTBiJEU%2BwIwR7vdQm%2F7nxoWnbPbuhIEyx0V%2BL6HZOjTY5%2Bbk4Hfr5QN5bgVi5fg2T65THHj5LTX26LxHbLuoC4rtaHrfDj%2BVQffFlWv83nvUEY8J6U3zxzJChhJE2rkJh5u4ltoJlTWiOfztw3ltNlbxr1%2FrHndlU5i33VyCOZSbjrb%2FyTK16MIsZZDCFg3OswEtJdVxdsLLcv%2FMXJ5RBpEIUzxzsk9QOHzo%2BW%2BNDCsZGiHoRk%2FjRpLYJVfg7Xu%2Ff7LrVTDekJdyD%2BRjy%2BB723vvGwEadKyGF%2BhRrkogHiqwQp4c3LknNtrzgkELIJbARJnIQHSYg%2F754TVGERWeUyvZkGmRhOEe1MwemyL82%2B8LtExx%2BG6v%2FDKgRCbTClmpW9BjqkAfKOTpZhKLXl3ZglIsb32NtOky3VtgYYrDzyWzkZQCClA%2FejqQbjE4oGeA%2FVy4CM4617E6gWfUoPPvT53tYzNfnRzdmhT92N72whUu%2F8MtBXc28A6t%2BSorb4eqE4rU%2Fgrb1vRac%2BSfem3np0Hcb8G%2FLHNo3sPQ3ziaEvJmd28%2BqRFYlnbUGPUYA50tdSQxf7McOTR4NH8UBoc1M88vWNOj%2FCue40&X-Amz-Signature=fca49b67da67128dd5300824284e4936924542606927bd9da2dfec0118a4d136&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIJVRDFK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHFiKDoBsD%2FeaRs8UZAeMPVB3dwC36waKsa4ZsTCdYUxAiEA41K8CyL59O64SfDHn7jc3OVHP7cl7yzNTSnrvcjpKg0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKXe50pIY3gs5mq5rCrcA9rnPqmBjork8Vci1pGYudht1GvSLxgQQDVuw8mUm4%2FY%2FzPT%2FPY%2FfVQYMX9DcVlyDGAILzCoRuixL5Sv5ygDUZ0S79WKbUkAn%2F8iEOpF5WEiS8Bg9ntNmKty9IlSqX%2BQj%2FpU1QXIA1AlMF%2BqpP1UWxxcxS9f341RinqOSwLz1ryVC6Xk6y5McdnEt%2FQZCtPLdfPRn08R7ley8jNnVLYj0j5re9X3P5DY2NbdevHB7RV4dC%2FOA%2B1eJKpEiXoGJ%2B1LEsVhKfS4bCYYsB3ISzYPqDJyUqZnpH1Oc9KmM2A9DSGYzOFYYY%2BUOK2WyQAOBp0CHBTDobshiOb1TVJ3FDo%2BdFGHDayL56JE3OOgHmx7wstYetu07x3XgKk%2BxDhbteF%2Bn6nnaNmlqC1C3hZa5RPrRnrr0Q7fGUwZcKTNpviBQl5nkdiDjBg0mH8BPPbrM7LN99jFsVZW7Kss71EIYjhsujufOJVgNTnzh0MIGzsJewWWS5tz7azpK6E6%2FnM8ftsSuzPSsp4eAhvirAplrT3PDzCG35GmAQHFjB7lUvL0k2mEqp%2BPHS%2BmFT7nOgHiwa9Fr2EE6KWKR5lxwZUa%2FLv8owMJnKZnYZFIACqWVax69aI%2BmUUhtl%2FiDHhrNLAQMKaalb0GOqUB6j8miT6R3LBEvQXEOlHa1WzRvzo8yFHzJJsuYuKSKUIBePMw%2BWLtXfeJOCsCOPYGdTbz8zyNaGUpp0U7ru0WA9l361vNTYW1q%2F9zobERzDHmF1%2FCnMYSQug6MP8OHCJih%2BltQ4UoQy1VGlqHRTDKNUo5ujhPJwXD0v1Sl0JfoP6xwl5kBoLBySsDsjh0gQPd3ZV3IJhGCEE8H5f1ZkoNUE4evdj8&X-Amz-Signature=6416448a85d4d2325f84834c6cd3a81b15a531823438cb98272bbeca38ac7e7d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GTWDTA3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCh2er64xxdRoNGYBG2%2FEsZh%2FMwKTC3PC8QASkX8YUZ%2FQIhAJuKjjLa4WhH9G2B73KX%2BT0mcxixndJXBKJnUo%2BIaKQ4Kv8DCGkQABoMNjM3NDIzMTgzODA1IgzspopJ1y96j4bAjSkq3APBnLACbO3jeQSXI6wM%2F0nOfwJbsSbfyYi5JT4SKhHKtXI4AWEwQfgzZ4WZ%2BFXZV5ovutijPrudITomYgKMdnCcoby4r%2BX47iwSfaQcI0shlnnL9y2XfHI7bXYYR8bp4h0re6OnIjEKVjDUKAbhAWNMTEUFzSrBFJj3HU70YXNwIOx2mgPYvt5Ej3ZxsfSpoi8BD0kczaF1q%2FOXPUm2ruJ3%2Bi3v7RZaqoYq9fXdn5EIRjZXj9EtT%2FBx7lKhyQbb5MTMbS9qqWslv65ckKR4L%2Bl20WUQRHx8gOnRwqow%2FPz8AMzoz4T2kQNQtb5L99bA5hKI9XOmAbbRzVp3dexrJU7OjVXEAYJGiX4rWP3vRZAbZwhx45vGy%2BEHtZLUwecBj%2BEKVzAEcz1sTbWAYnhym7vB6jSVjt85c656XcZotMF6CYJpBRtC45dK1M6rykF3bLUTCHMk1xLMqrOIMjZHbZk1ogkru2TQKGIkzc9wZ%2BA7qPNAVqnzCgryhME9RvghRE1QYxJgsgakjPy6ae8KzGKVygbth2Qxqc2GI4BQYTq6u667Cqf2LprhuxEPHa%2BJjWa1pTQ5iIzVrNYuQtXCBSmQ7a4hrq4MX1SSc5RECJ2kCIOpMHZ9KEsy%2FWeT8zCZmpW9BjqkARwo9vtEY8Fb%2BPn%2Bd8MvQ9ESjbDmWbA72DW06sKtWHperbWLrvyTbEs26cUimWWZ204t3C5cjNm3qo0J8QJDwCXpYnvEzbtx1aAtBp7LCsKR6ixk0a%2BpblIsgtuaYPHKrWmQIgySW%2BSPkEH432Ns%2FmwKRz9JeuIBVotI1J0XhChxGAme2jfIKO2CCsyAzQLppnpT8Rjmenfx8ptBV9O0VVC%2BoORJ&X-Amz-Signature=1223e5394db5d458bb9b83648c0b852ad347883edfe585ea2e07e6bca6ef07f4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6KGTOVO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCtj2sS%2Flwbq7vko%2FIaa3%2BSDESlkB3oq68i2cw%2BOtXV2QIgeAwOPOc8UKbkIppUvXFwD6jLTkt%2BzRbEzLZ3U2OqaoQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDDkAtD%2BTcjJN0CZrRyrcA%2FFzC3xrXGKxm7rh4uMhPXzeeV5MsU6HVYA0s1wlqc%2BdsBaq8qswfuOzAtKOl3A63CQ6sFM5ZcfOGQLr7sf03Qp0YlhX5c7nCQy1FrC0EP9k9kLHfvFNq7hVkWLMPWkqqupOr%2Bhpp45e4S7s4%2FBIpeTQ8lqBxgLljo30o2VEq5Lo5QRPEILRSYGtyDm6yMHBs1etcFc4wBfDKMlxEcSVVDZHmd6TMG1TxVYY3d%2FpktWql6IBWEUtPVAWkM5BoZWMUJhzm31eFaTdj9hpZrgzGGS%2BKD4%2FNUBIrk%2Fxd9qqxBOtzLhSOWrU16mMdJYZtfc63bdPcRx40%2B8fgUm6Qz0KbhhrfHpr%2FuSMRhfsMAUsspN7UtvwF5OWmJh1HcDDvU5kmE9Res2DEUVe6I8rKjVIHX9EJDcpXeYhkpnU0JW9XDr9K3FI7%2FuaAn%2FeQJWJ3ZlR6tnwlSEvDaKQkyrzWoG0TyM1kDzdyOSjtmI3qLYfuhPKo2O1mzieY8u%2Bx6MkkUlS6HLavLNLs5BmPb%2FhMr0b3ImnDXBSbBru2jyrAulQcWyUbUV%2BArUlNc8GzQhk7gp4L%2BrshvAdWq5XXGDJoUhzOE70RV4%2FlNwFAbQ5rN%2BX7MODIQPo%2FOtRDHx5NfvvMKSalb0GOqUBwIP%2FiFPRjucWPopk%2BRdpgOLVcZ5TItDqVz%2B2OIuhJE0NO6o268VkwS%2Fo%2BgknUVxfwS8hcunT%2BXF2rFX1Jeb4qYoRjRZl%2BGgQKhCFhlrXVCzlaCV6F5hukuZiPqKDxwcXAEUdVBurAQkMvyqxiULN%2FZX8qEDtEktHjzL2iqqyQoEh%2FEZ0h5C%2Be1jGqhxR9tkesFVHAF%2FN3DPQol7R1W2KmctdvKki&X-Amz-Signature=26f8c1cba0868166b277dc1c30e5d368d0ed5af645dcedb77606478cc047d583&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYA3RTNZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCcHaR34QfAE00YA40Dp856YEi3CN5k%2BUIuf6vOECLiMAIgZKg8r%2Bp7WG94nzWrSGWJinIC41qWN16kBx7ci38YakQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDOopn8qnsJQqy7yl7CrcA290MGl53NN0APLjdcrzjCwOIlHT8jQ3oiWPwZy%2BdaA1evOMt%2Fa5iUYPmofCjxdbF9LSbv6y5KjjXuWN21FYk%2FqUK9W8XdBG875Q5c9VXpUzO4gV03ZSZ65N7tDuSp7eVMWLMMmr8fsoCaI8aMT5Ky2qJTwNXLRWl4tI9GzU%2FJko5LVWTDz6VEC4SpMz8UBAaGf9H%2Ft%2FfcFN0b%2BgtcdTX0CxwSHNg1Q7U4w7KvdmNYlG7mOchip40kGpmOOxizpTbMN68jQiwIysYyd8%2Ffz1IdP8xkEtrrARgkLKYGotg%2B4Lx4M0LnVa4uem35l4Rzer1oGfeyXl%2FlODDLAyKmRDu4TUc8Cz3nqSoGTrTQ77au3wWSNmDfI8BorrxVqSH%2BYk7gt6LlCgg0RCQBzqjOH%2Fu39pJ3RPZLo%2B9lziks1YayZqtSWM0otCeYp17WEcC5ZAmfN9OqSpA7SjUwwPUcE40ZStbyYExYrS2uMzVDZkEajSbD2wcJwbhshVEzofKv2q3U3jRUvV0TtrmlBvsG5DJCxoaQQlaA%2F%2BPj3hZ8Yf9hEr8E4Rr9MhP5cuIAFmQuzhUT%2BbDjJu18WJLzDTf8apvwJW3EgUbx5vBJL59SjlYMEuNk4KNWxJ4OrmPUXlMLGalb0GOqUBk217K%2B%2FU5ag3SrHLr0ZbBhA0wLnKbA3NVMBJrT%2FMrtlv61JE%2BmpDMn%2B%2BppBVzzW9dYCRvuHJXaffeZ3MiSsFnntXAaLsrUxqe%2FN4JnzNYHdkZsGZhlZS%2BWafGeTPT4qX6q7ae7BQ1cezuSewveVl%2B8qu4hZNJjGRVa7LUhno7%2FXePkRgjHfeqJTex98NY%2F6sBhDhSS32l4vs2WjZh4iheZfUyB5e&X-Amz-Signature=5b186e89b851e6a42a81340b051f509040e4ad793c2ccfd53338cf36ee855b5e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYA3RTNZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCcHaR34QfAE00YA40Dp856YEi3CN5k%2BUIuf6vOECLiMAIgZKg8r%2Bp7WG94nzWrSGWJinIC41qWN16kBx7ci38YakQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDOopn8qnsJQqy7yl7CrcA290MGl53NN0APLjdcrzjCwOIlHT8jQ3oiWPwZy%2BdaA1evOMt%2Fa5iUYPmofCjxdbF9LSbv6y5KjjXuWN21FYk%2FqUK9W8XdBG875Q5c9VXpUzO4gV03ZSZ65N7tDuSp7eVMWLMMmr8fsoCaI8aMT5Ky2qJTwNXLRWl4tI9GzU%2FJko5LVWTDz6VEC4SpMz8UBAaGf9H%2Ft%2FfcFN0b%2BgtcdTX0CxwSHNg1Q7U4w7KvdmNYlG7mOchip40kGpmOOxizpTbMN68jQiwIysYyd8%2Ffz1IdP8xkEtrrARgkLKYGotg%2B4Lx4M0LnVa4uem35l4Rzer1oGfeyXl%2FlODDLAyKmRDu4TUc8Cz3nqSoGTrTQ77au3wWSNmDfI8BorrxVqSH%2BYk7gt6LlCgg0RCQBzqjOH%2Fu39pJ3RPZLo%2B9lziks1YayZqtSWM0otCeYp17WEcC5ZAmfN9OqSpA7SjUwwPUcE40ZStbyYExYrS2uMzVDZkEajSbD2wcJwbhshVEzofKv2q3U3jRUvV0TtrmlBvsG5DJCxoaQQlaA%2F%2BPj3hZ8Yf9hEr8E4Rr9MhP5cuIAFmQuzhUT%2BbDjJu18WJLzDTf8apvwJW3EgUbx5vBJL59SjlYMEuNk4KNWxJ4OrmPUXlMLGalb0GOqUBk217K%2B%2FU5ag3SrHLr0ZbBhA0wLnKbA3NVMBJrT%2FMrtlv61JE%2BmpDMn%2B%2BppBVzzW9dYCRvuHJXaffeZ3MiSsFnntXAaLsrUxqe%2FN4JnzNYHdkZsGZhlZS%2BWafGeTPT4qX6q7ae7BQ1cezuSewveVl%2B8qu4hZNJjGRVa7LUhno7%2FXePkRgjHfeqJTex98NY%2F6sBhDhSS32l4vs2WjZh4iheZfUyB5e&X-Amz-Signature=00261ddaf375fdbe01e093e1bf15804fdb2ad49655cab4605e512a4760ad598c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
