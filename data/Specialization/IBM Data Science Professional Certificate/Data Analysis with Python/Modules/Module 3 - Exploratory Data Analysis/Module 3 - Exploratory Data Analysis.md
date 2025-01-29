

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCECNUI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBEg5aAi6AfzR1Tm0IgIDk1koSqv8StZTc8KFDMC1zYAiAJpuQKOD6RXHl5GD3xUkfS8p0wec9g4CA%2FBbubu23pHSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM41u5grN3%2FtuWpQHOKtwDIDBelN0oDj5zCWyl%2BEX%2Bc9YzTqy5WXYsbuxV0HfaugSpSkSwfozHU9WkmuOS2zUl9WQdNRB5h1gZkIIyYREAWDWgXOAeIy9L5uYT0TU%2FLodpD8anAqu8AhRHyOhaW1jfLZd%2Bz9srk%2BA2fToeZpgUjrDA5qBpeSHCxZjmGJMYp4sug90nlIcdBXOQUDZbKINeicPgbkAk8TqpqNIQI%2BagB10M%2Bol2guFVu%2FnAkLssvRFHTOd1MIA64M%2B02%2FHVRTKaxA0tc%2BbDxgipQy94pAsayDQZolwa78EtfONvAvQ4yIXnKd3ZeOrtwqk%2BU2RU2t9wTHHNnQitla3CryFfLQfXQfDeUMk7xKuW2ZUYG5BEUCWpvqTfm%2FONDIkTqCRv2YqGK2LevA8%2Bp29VoB7RLk0rW3KXRwDzP6ZEP%2BzmZ1SVN%2BSJXS9CuZ6PDlOhtVanSfj1Qtp9VuG3k9og0B0Fd6K4KXXw%2Fgesw5lfbHTuYpCggVL7A6hdKyA%2BPCV5rsnVj8cYoql5hmedMLnINVTVFbDU%2FSIOkyYOqOEZ5zDNvsDiDuIli9%2FSNcHyI5E6OmO5UqELlyzv0CnAT2PHGj%2FTi2zVv2ZgcXcBI5bCt5lOFZblc4LtzqoO%2BKsjy4wag8swlanqvAY6pgHULLfPCRBVcryJu9yH7jGtCe3v2%2Fo1T0zvQ4gPhQ%2FJ1ekv4UtUiaLWLfIuhO7yMG8rN4RQdd1ISW%2Bppbr0ZP%2FFa%2B0YJjBh8pHwAjKGJj%2F9akGX5x60Dkhiv0HwoH0kPEI8R5OjJvgkDanHXE4LIcdzccVEbOHf7AACDZ7kDxkQwbqIc%2B3cxRcGvbBxtswjsKi%2BTB7aG0dnq2XmljBOQAYMt0Ycm8de&X-Amz-Signature=ef9e10b35660c2ea07ebbcf37f4385ded5391b334bc96ba2feb702cd547b0e23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCECNUI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBEg5aAi6AfzR1Tm0IgIDk1koSqv8StZTc8KFDMC1zYAiAJpuQKOD6RXHl5GD3xUkfS8p0wec9g4CA%2FBbubu23pHSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM41u5grN3%2FtuWpQHOKtwDIDBelN0oDj5zCWyl%2BEX%2Bc9YzTqy5WXYsbuxV0HfaugSpSkSwfozHU9WkmuOS2zUl9WQdNRB5h1gZkIIyYREAWDWgXOAeIy9L5uYT0TU%2FLodpD8anAqu8AhRHyOhaW1jfLZd%2Bz9srk%2BA2fToeZpgUjrDA5qBpeSHCxZjmGJMYp4sug90nlIcdBXOQUDZbKINeicPgbkAk8TqpqNIQI%2BagB10M%2Bol2guFVu%2FnAkLssvRFHTOd1MIA64M%2B02%2FHVRTKaxA0tc%2BbDxgipQy94pAsayDQZolwa78EtfONvAvQ4yIXnKd3ZeOrtwqk%2BU2RU2t9wTHHNnQitla3CryFfLQfXQfDeUMk7xKuW2ZUYG5BEUCWpvqTfm%2FONDIkTqCRv2YqGK2LevA8%2Bp29VoB7RLk0rW3KXRwDzP6ZEP%2BzmZ1SVN%2BSJXS9CuZ6PDlOhtVanSfj1Qtp9VuG3k9og0B0Fd6K4KXXw%2Fgesw5lfbHTuYpCggVL7A6hdKyA%2BPCV5rsnVj8cYoql5hmedMLnINVTVFbDU%2FSIOkyYOqOEZ5zDNvsDiDuIli9%2FSNcHyI5E6OmO5UqELlyzv0CnAT2PHGj%2FTi2zVv2ZgcXcBI5bCt5lOFZblc4LtzqoO%2BKsjy4wag8swlanqvAY6pgHULLfPCRBVcryJu9yH7jGtCe3v2%2Fo1T0zvQ4gPhQ%2FJ1ekv4UtUiaLWLfIuhO7yMG8rN4RQdd1ISW%2Bppbr0ZP%2FFa%2B0YJjBh8pHwAjKGJj%2F9akGX5x60Dkhiv0HwoH0kPEI8R5OjJvgkDanHXE4LIcdzccVEbOHf7AACDZ7kDxkQwbqIc%2B3cxRcGvbBxtswjsKi%2BTB7aG0dnq2XmljBOQAYMt0Ycm8de&X-Amz-Signature=d6eb11feb30d8fa41f777d29a89e138fc69663b4ac62c725ec7fa2dc7a0ab2f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCECNUI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBEg5aAi6AfzR1Tm0IgIDk1koSqv8StZTc8KFDMC1zYAiAJpuQKOD6RXHl5GD3xUkfS8p0wec9g4CA%2FBbubu23pHSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM41u5grN3%2FtuWpQHOKtwDIDBelN0oDj5zCWyl%2BEX%2Bc9YzTqy5WXYsbuxV0HfaugSpSkSwfozHU9WkmuOS2zUl9WQdNRB5h1gZkIIyYREAWDWgXOAeIy9L5uYT0TU%2FLodpD8anAqu8AhRHyOhaW1jfLZd%2Bz9srk%2BA2fToeZpgUjrDA5qBpeSHCxZjmGJMYp4sug90nlIcdBXOQUDZbKINeicPgbkAk8TqpqNIQI%2BagB10M%2Bol2guFVu%2FnAkLssvRFHTOd1MIA64M%2B02%2FHVRTKaxA0tc%2BbDxgipQy94pAsayDQZolwa78EtfONvAvQ4yIXnKd3ZeOrtwqk%2BU2RU2t9wTHHNnQitla3CryFfLQfXQfDeUMk7xKuW2ZUYG5BEUCWpvqTfm%2FONDIkTqCRv2YqGK2LevA8%2Bp29VoB7RLk0rW3KXRwDzP6ZEP%2BzmZ1SVN%2BSJXS9CuZ6PDlOhtVanSfj1Qtp9VuG3k9og0B0Fd6K4KXXw%2Fgesw5lfbHTuYpCggVL7A6hdKyA%2BPCV5rsnVj8cYoql5hmedMLnINVTVFbDU%2FSIOkyYOqOEZ5zDNvsDiDuIli9%2FSNcHyI5E6OmO5UqELlyzv0CnAT2PHGj%2FTi2zVv2ZgcXcBI5bCt5lOFZblc4LtzqoO%2BKsjy4wag8swlanqvAY6pgHULLfPCRBVcryJu9yH7jGtCe3v2%2Fo1T0zvQ4gPhQ%2FJ1ekv4UtUiaLWLfIuhO7yMG8rN4RQdd1ISW%2Bppbr0ZP%2FFa%2B0YJjBh8pHwAjKGJj%2F9akGX5x60Dkhiv0HwoH0kPEI8R5OjJvgkDanHXE4LIcdzccVEbOHf7AACDZ7kDxkQwbqIc%2B3cxRcGvbBxtswjsKi%2BTB7aG0dnq2XmljBOQAYMt0Ycm8de&X-Amz-Signature=0812a79d6dc4f705f8899d7c52de572a2665c5fe64724e4836d4bb5ab2526009&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGWNIULG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpsZyJEF81edGKReC6H3wVBdsxEuT%2FqnXvZeyGtDZEgQIgafxO7IBtqnnJK%2FTtOqbNPExCe5BSYsv7OQqla6wMhnwqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzAdsrFhhtUB27hPyrcA7PhHAyiS5x%2BgniqRPR26lzVfMotQ7T%2F5AZ%2FDfjZ4t16fLb0ePoDfFIi1uAiOPS6UveMagimlQMovNO3CutzaVhh9Auj4To5FDwq2Gb0pxFPcgV3zD3Lv28oVJNed%2FftGnSFSeSIhEGGE0Yy7sqxcTOMcqKpZWeGtp6ekIIVvmb9zIzMFs9E8CAf1CUyK6s2djwqfzZPTn%2BM3QFVs1DFHNiqF8rPEySG7nBUX0dsDyKDa9WbdofjOc2sSNE1ixUOCUOLv0sye8opq%2B3eBq8mJwllrCY13HH2vviDmUkKkOUk6vvrPV595D89Hfa06CNnEfOzmjpyzlCvDBPY46YKj2JW9X7%2BUO9gkLUfUEdhrE1IYhb1MLQ%2B7LCsRbLGX7SKv0FofaaMyIFpskU4XAFLj2eK%2FY1zAirK7efCY4ROYxMF%2BFqcfsUliSlllej5hWGiUHlG00KNH59luIUS7b%2FNGaQPruDbKDl%2BllxgDlnc9ST%2BUlG%2Func%2FSczNHkBcdCQxYP%2B2JJ2uS9ClYYzr1Df%2FBeQaml0qUw5nZ0aD2K%2F67Ta%2Fx5gOauUQzCg%2F0JlqqNS1%2Fy1ipsPT7FW4EPevOwoZnDB6uFX4fYyl5LRzQbdgskS7nHXCORo93RYWXG%2BkMOKo6rwGOqUBxTeb5UUA9Oo4JYtGPWsX0ROBijkJBTx7fMQqchefxqGUS0wqrm2xsGuJ7DR6H003gic2epFa94%2BZX7aMjqnnXLp4YmGb37bm2KXl%2FlVpI0QnD8ZFKJqmHgBPX8JSCxKsJi8a6%2Bg76sPh%2FefPwrYZvhjbZQh9tgrjCyKXfpJD46taWAIQixG0TGHN7Y0YPxMGXmKGpQmd7whmLaSpSBUv3cLOQEZ1&X-Amz-Signature=8bb5aba36fbfae04655e4f38e06b3b6bc0369da052e39d51941d48f8d7c66fda&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGWNIULG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpsZyJEF81edGKReC6H3wVBdsxEuT%2FqnXvZeyGtDZEgQIgafxO7IBtqnnJK%2FTtOqbNPExCe5BSYsv7OQqla6wMhnwqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzAdsrFhhtUB27hPyrcA7PhHAyiS5x%2BgniqRPR26lzVfMotQ7T%2F5AZ%2FDfjZ4t16fLb0ePoDfFIi1uAiOPS6UveMagimlQMovNO3CutzaVhh9Auj4To5FDwq2Gb0pxFPcgV3zD3Lv28oVJNed%2FftGnSFSeSIhEGGE0Yy7sqxcTOMcqKpZWeGtp6ekIIVvmb9zIzMFs9E8CAf1CUyK6s2djwqfzZPTn%2BM3QFVs1DFHNiqF8rPEySG7nBUX0dsDyKDa9WbdofjOc2sSNE1ixUOCUOLv0sye8opq%2B3eBq8mJwllrCY13HH2vviDmUkKkOUk6vvrPV595D89Hfa06CNnEfOzmjpyzlCvDBPY46YKj2JW9X7%2BUO9gkLUfUEdhrE1IYhb1MLQ%2B7LCsRbLGX7SKv0FofaaMyIFpskU4XAFLj2eK%2FY1zAirK7efCY4ROYxMF%2BFqcfsUliSlllej5hWGiUHlG00KNH59luIUS7b%2FNGaQPruDbKDl%2BllxgDlnc9ST%2BUlG%2Func%2FSczNHkBcdCQxYP%2B2JJ2uS9ClYYzr1Df%2FBeQaml0qUw5nZ0aD2K%2F67Ta%2Fx5gOauUQzCg%2F0JlqqNS1%2Fy1ipsPT7FW4EPevOwoZnDB6uFX4fYyl5LRzQbdgskS7nHXCORo93RYWXG%2BkMOKo6rwGOqUBxTeb5UUA9Oo4JYtGPWsX0ROBijkJBTx7fMQqchefxqGUS0wqrm2xsGuJ7DR6H003gic2epFa94%2BZX7aMjqnnXLp4YmGb37bm2KXl%2FlVpI0QnD8ZFKJqmHgBPX8JSCxKsJi8a6%2Bg76sPh%2FefPwrYZvhjbZQh9tgrjCyKXfpJD46taWAIQixG0TGHN7Y0YPxMGXmKGpQmd7whmLaSpSBUv3cLOQEZ1&X-Amz-Signature=637002c6396a6632c41542e60ab376888759efe76e01e02c033d82d29f24fe8f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGWNIULG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpsZyJEF81edGKReC6H3wVBdsxEuT%2FqnXvZeyGtDZEgQIgafxO7IBtqnnJK%2FTtOqbNPExCe5BSYsv7OQqla6wMhnwqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzAdsrFhhtUB27hPyrcA7PhHAyiS5x%2BgniqRPR26lzVfMotQ7T%2F5AZ%2FDfjZ4t16fLb0ePoDfFIi1uAiOPS6UveMagimlQMovNO3CutzaVhh9Auj4To5FDwq2Gb0pxFPcgV3zD3Lv28oVJNed%2FftGnSFSeSIhEGGE0Yy7sqxcTOMcqKpZWeGtp6ekIIVvmb9zIzMFs9E8CAf1CUyK6s2djwqfzZPTn%2BM3QFVs1DFHNiqF8rPEySG7nBUX0dsDyKDa9WbdofjOc2sSNE1ixUOCUOLv0sye8opq%2B3eBq8mJwllrCY13HH2vviDmUkKkOUk6vvrPV595D89Hfa06CNnEfOzmjpyzlCvDBPY46YKj2JW9X7%2BUO9gkLUfUEdhrE1IYhb1MLQ%2B7LCsRbLGX7SKv0FofaaMyIFpskU4XAFLj2eK%2FY1zAirK7efCY4ROYxMF%2BFqcfsUliSlllej5hWGiUHlG00KNH59luIUS7b%2FNGaQPruDbKDl%2BllxgDlnc9ST%2BUlG%2Func%2FSczNHkBcdCQxYP%2B2JJ2uS9ClYYzr1Df%2FBeQaml0qUw5nZ0aD2K%2F67Ta%2Fx5gOauUQzCg%2F0JlqqNS1%2Fy1ipsPT7FW4EPevOwoZnDB6uFX4fYyl5LRzQbdgskS7nHXCORo93RYWXG%2BkMOKo6rwGOqUBxTeb5UUA9Oo4JYtGPWsX0ROBijkJBTx7fMQqchefxqGUS0wqrm2xsGuJ7DR6H003gic2epFa94%2BZX7aMjqnnXLp4YmGb37bm2KXl%2FlVpI0QnD8ZFKJqmHgBPX8JSCxKsJi8a6%2Bg76sPh%2FefPwrYZvhjbZQh9tgrjCyKXfpJD46taWAIQixG0TGHN7Y0YPxMGXmKGpQmd7whmLaSpSBUv3cLOQEZ1&X-Amz-Signature=be0f44441f0d3a4b9413d60b780da5b1e3904e9cabff98af93e59f5fa66df0db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGWNIULG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpsZyJEF81edGKReC6H3wVBdsxEuT%2FqnXvZeyGtDZEgQIgafxO7IBtqnnJK%2FTtOqbNPExCe5BSYsv7OQqla6wMhnwqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzAdsrFhhtUB27hPyrcA7PhHAyiS5x%2BgniqRPR26lzVfMotQ7T%2F5AZ%2FDfjZ4t16fLb0ePoDfFIi1uAiOPS6UveMagimlQMovNO3CutzaVhh9Auj4To5FDwq2Gb0pxFPcgV3zD3Lv28oVJNed%2FftGnSFSeSIhEGGE0Yy7sqxcTOMcqKpZWeGtp6ekIIVvmb9zIzMFs9E8CAf1CUyK6s2djwqfzZPTn%2BM3QFVs1DFHNiqF8rPEySG7nBUX0dsDyKDa9WbdofjOc2sSNE1ixUOCUOLv0sye8opq%2B3eBq8mJwllrCY13HH2vviDmUkKkOUk6vvrPV595D89Hfa06CNnEfOzmjpyzlCvDBPY46YKj2JW9X7%2BUO9gkLUfUEdhrE1IYhb1MLQ%2B7LCsRbLGX7SKv0FofaaMyIFpskU4XAFLj2eK%2FY1zAirK7efCY4ROYxMF%2BFqcfsUliSlllej5hWGiUHlG00KNH59luIUS7b%2FNGaQPruDbKDl%2BllxgDlnc9ST%2BUlG%2Func%2FSczNHkBcdCQxYP%2B2JJ2uS9ClYYzr1Df%2FBeQaml0qUw5nZ0aD2K%2F67Ta%2Fx5gOauUQzCg%2F0JlqqNS1%2Fy1ipsPT7FW4EPevOwoZnDB6uFX4fYyl5LRzQbdgskS7nHXCORo93RYWXG%2BkMOKo6rwGOqUBxTeb5UUA9Oo4JYtGPWsX0ROBijkJBTx7fMQqchefxqGUS0wqrm2xsGuJ7DR6H003gic2epFa94%2BZX7aMjqnnXLp4YmGb37bm2KXl%2FlVpI0QnD8ZFKJqmHgBPX8JSCxKsJi8a6%2Bg76sPh%2FefPwrYZvhjbZQh9tgrjCyKXfpJD46taWAIQixG0TGHN7Y0YPxMGXmKGpQmd7whmLaSpSBUv3cLOQEZ1&X-Amz-Signature=1a8ed8144f52fcc7e38044e5dea48f3aa245c0a33212da0ef5c787a5eadfe351&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGWNIULG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpsZyJEF81edGKReC6H3wVBdsxEuT%2FqnXvZeyGtDZEgQIgafxO7IBtqnnJK%2FTtOqbNPExCe5BSYsv7OQqla6wMhnwqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzAdsrFhhtUB27hPyrcA7PhHAyiS5x%2BgniqRPR26lzVfMotQ7T%2F5AZ%2FDfjZ4t16fLb0ePoDfFIi1uAiOPS6UveMagimlQMovNO3CutzaVhh9Auj4To5FDwq2Gb0pxFPcgV3zD3Lv28oVJNed%2FftGnSFSeSIhEGGE0Yy7sqxcTOMcqKpZWeGtp6ekIIVvmb9zIzMFs9E8CAf1CUyK6s2djwqfzZPTn%2BM3QFVs1DFHNiqF8rPEySG7nBUX0dsDyKDa9WbdofjOc2sSNE1ixUOCUOLv0sye8opq%2B3eBq8mJwllrCY13HH2vviDmUkKkOUk6vvrPV595D89Hfa06CNnEfOzmjpyzlCvDBPY46YKj2JW9X7%2BUO9gkLUfUEdhrE1IYhb1MLQ%2B7LCsRbLGX7SKv0FofaaMyIFpskU4XAFLj2eK%2FY1zAirK7efCY4ROYxMF%2BFqcfsUliSlllej5hWGiUHlG00KNH59luIUS7b%2FNGaQPruDbKDl%2BllxgDlnc9ST%2BUlG%2Func%2FSczNHkBcdCQxYP%2B2JJ2uS9ClYYzr1Df%2FBeQaml0qUw5nZ0aD2K%2F67Ta%2Fx5gOauUQzCg%2F0JlqqNS1%2Fy1ipsPT7FW4EPevOwoZnDB6uFX4fYyl5LRzQbdgskS7nHXCORo93RYWXG%2BkMOKo6rwGOqUBxTeb5UUA9Oo4JYtGPWsX0ROBijkJBTx7fMQqchefxqGUS0wqrm2xsGuJ7DR6H003gic2epFa94%2BZX7aMjqnnXLp4YmGb37bm2KXl%2FlVpI0QnD8ZFKJqmHgBPX8JSCxKsJi8a6%2Bg76sPh%2FefPwrYZvhjbZQh9tgrjCyKXfpJD46taWAIQixG0TGHN7Y0YPxMGXmKGpQmd7whmLaSpSBUv3cLOQEZ1&X-Amz-Signature=593b7d9f09bc63fe89a38856a21e24cc162dd24dc8d75a1cab96d0d1288c1264&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGWNIULG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpsZyJEF81edGKReC6H3wVBdsxEuT%2FqnXvZeyGtDZEgQIgafxO7IBtqnnJK%2FTtOqbNPExCe5BSYsv7OQqla6wMhnwqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzAdsrFhhtUB27hPyrcA7PhHAyiS5x%2BgniqRPR26lzVfMotQ7T%2F5AZ%2FDfjZ4t16fLb0ePoDfFIi1uAiOPS6UveMagimlQMovNO3CutzaVhh9Auj4To5FDwq2Gb0pxFPcgV3zD3Lv28oVJNed%2FftGnSFSeSIhEGGE0Yy7sqxcTOMcqKpZWeGtp6ekIIVvmb9zIzMFs9E8CAf1CUyK6s2djwqfzZPTn%2BM3QFVs1DFHNiqF8rPEySG7nBUX0dsDyKDa9WbdofjOc2sSNE1ixUOCUOLv0sye8opq%2B3eBq8mJwllrCY13HH2vviDmUkKkOUk6vvrPV595D89Hfa06CNnEfOzmjpyzlCvDBPY46YKj2JW9X7%2BUO9gkLUfUEdhrE1IYhb1MLQ%2B7LCsRbLGX7SKv0FofaaMyIFpskU4XAFLj2eK%2FY1zAirK7efCY4ROYxMF%2BFqcfsUliSlllej5hWGiUHlG00KNH59luIUS7b%2FNGaQPruDbKDl%2BllxgDlnc9ST%2BUlG%2Func%2FSczNHkBcdCQxYP%2B2JJ2uS9ClYYzr1Df%2FBeQaml0qUw5nZ0aD2K%2F67Ta%2Fx5gOauUQzCg%2F0JlqqNS1%2Fy1ipsPT7FW4EPevOwoZnDB6uFX4fYyl5LRzQbdgskS7nHXCORo93RYWXG%2BkMOKo6rwGOqUBxTeb5UUA9Oo4JYtGPWsX0ROBijkJBTx7fMQqchefxqGUS0wqrm2xsGuJ7DR6H003gic2epFa94%2BZX7aMjqnnXLp4YmGb37bm2KXl%2FlVpI0QnD8ZFKJqmHgBPX8JSCxKsJi8a6%2Bg76sPh%2FefPwrYZvhjbZQh9tgrjCyKXfpJD46taWAIQixG0TGHN7Y0YPxMGXmKGpQmd7whmLaSpSBUv3cLOQEZ1&X-Amz-Signature=27177c2d78df93ee1ecab524942e4cdf3d7a95f556594c94a23bd21b60e07dfa&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJG7AU6Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHvNwbuhGObwqQSa%2FfdPmvrQuWwllhufN43duMtSO7e8AiA3shZ6Lv8OmWdNdxfV5Q6S%2Bilhav1rrQjtKenL9loJ3yqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTfcJjW%2BL0LynabyHKtwD6LqvO9UDZx7C3kQshT3OaZM0OArG50oVHQC8znEO%2FDvvN41flTwpKXUoSsyl9jYlRqWp0EU3nLrLuMriGLvppaHzgt1fQRH%2BpNBA954Vx1cRvyEDg1g0Q8E5OfdSAjHMhzaSOXpVSKl%2FskLPCMsZbxl3dCC5sKrOXQ5IIu6UHtN0xJo8Y4hy3OmVE%2FIQe%2FvD6q2oJzL1OuHteFmq3jMRv9izdyZ31gfGKnUa%2FrzW%2B9ILZKJw6iJxVai61bfHEMzL5KhE8OKvBEOgwz46H2Ghn8s5t0LaPTxk9WB756i1kYsEM1%2FXebPoYNTVglkmPeTpiRyW4lC5lVhfepfIqdbaGZp6a6So8C5jZhbXIKkyF5VK%2B2ixEBezCw%2BABm7v%2FuHqWmEu%2BZCs2lvL5up2AVUgpRQYE959yBjxWJURpsD5GNwokhbHPCJqKU0gytFb5tAqX1Umc6m6BmLNZeiCYPe13P3vOmtCpRp61c9SDl4zvgG1Htco4BvlFbbWPtM8IdTLQbfxRcABbpfKLz2U%2FhHHmT9lWYytiY0yu5blO24arK5YNIzZrE1HX%2B9T%2BWMmgk16qhkuQc2lMvlnQQuJuJOj8dXUT%2FF5GGY7eGUevcXTitdyNLEVSYAjw8JodLYwoqnqvAY6pgGEoSRlfCXWTSt0LkwnuFGnuacwXaXNLnQTLlVJgVK4AQHQyXbOUIxidZZQMLU7sQNSjfPgJR0XQ8omoLWl0ISJpOp9cyQgeoMsyRISt8v5iGRFhpyD5MNLQ396Yq9113xyqwA7ItVet92mwkhvxPcSFfUnBRXYya42KGRuaiqPbSaWEabHCkqYqXqGvS3qRiudAvYSte0ce0rZ6Md9XDozBfTTOtRr&X-Amz-Signature=75e27c04cf112d7e958eeab8847a514ffe3c916fe9c28886f1598a9916722333&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2YOSUYG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7SFpj1ygVRfXulbSKee67406pltorH9G5R9fc8VMTCAIhAPxl3TOqI3th%2FjRI1P4wA859YvFvNY9C2VMQ3hNplxrCKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRZI8pbkXZoNwW0rAq3AMv6rZYBoOuFESm81%2BDxRCK7VrnuZ029%2B%2B%2BbQwZX%2Bz7lTPccXohFxi8kcRchKFfnxIMQ4tdzmMUHPDbTgE1bqblFGShe%2FfedHfdOdjdxiSdhIyQK%2FdiEVJzCTB9KBDZQchfux%2FjCpZSAIA4M5bz8v7Lz8HvOn2UsakesJn5qyPG7MDWXlw52DclTecae7Z40IbPeaqGlHZTBaDW8euOu4j85djlCsALiwleog2NRqZqM4oJJkU30QP%2FDZCIrpVK%2BoIANIJezQ68DmXXiSpM87HiopZPRF8OplbcPwLOkDKzKT4YKxJe1xKwdWBdinUEVOK8jh6h3mJbYwvM89%2BXZ78wtgOowcuWWEKuL6gQ3SWBWaH9pYfo2Q4aRBUAtGYLwbV2DBM2AZz8dMEmLi8QRbqy72BLjQ5MarJCTuMRYQ9s%2FByeKdiEg6%2FuUvPPXFnOqg%2FNWFmOVfg3PdDP%2BOOVu5eMqilTOsEONMpiCwnJFQlnNMUKRbO4i%2Bq%2Bw8vuU5GjtjJpPoM67HvW0kP47DS1Q%2FGDpEzcRQbB3IxonrDAk%2FVAAe%2BTKzlollSriCWuePOsNKhOqTbDvS%2BUGeV5jK854yDhyLmUWCZyTU1R7o88uRtPtJg37epZZIOoSEXc2DCqqeq8BjqkAQHZMQmz24vn4U9waMN41zt%2BdeZs97IfTJwffGksN0CMhzGb7wi%2FQaU6C0%2FGMUTRsj6Bo56hy839kxYJzpdADfIeFtded2EeuOzt5wAcF1IeeZe6j55FonNURum92685MS1TSvZtE%2FqhA%2Bn9mrQswf2X0l%2BRtYqYJJcqbjqDAUBPcYNJFv%2BVMaY%2FCROzYGnmrrEDJtazRV3p2VKI1HGIySxvx2Kc&X-Amz-Signature=a6c08f4977f0e9cf44b4ef8b54506a4772a16810dfb0889e5bf399c869c77ba9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGWNIULG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpsZyJEF81edGKReC6H3wVBdsxEuT%2FqnXvZeyGtDZEgQIgafxO7IBtqnnJK%2FTtOqbNPExCe5BSYsv7OQqla6wMhnwqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzAdsrFhhtUB27hPyrcA7PhHAyiS5x%2BgniqRPR26lzVfMotQ7T%2F5AZ%2FDfjZ4t16fLb0ePoDfFIi1uAiOPS6UveMagimlQMovNO3CutzaVhh9Auj4To5FDwq2Gb0pxFPcgV3zD3Lv28oVJNed%2FftGnSFSeSIhEGGE0Yy7sqxcTOMcqKpZWeGtp6ekIIVvmb9zIzMFs9E8CAf1CUyK6s2djwqfzZPTn%2BM3QFVs1DFHNiqF8rPEySG7nBUX0dsDyKDa9WbdofjOc2sSNE1ixUOCUOLv0sye8opq%2B3eBq8mJwllrCY13HH2vviDmUkKkOUk6vvrPV595D89Hfa06CNnEfOzmjpyzlCvDBPY46YKj2JW9X7%2BUO9gkLUfUEdhrE1IYhb1MLQ%2B7LCsRbLGX7SKv0FofaaMyIFpskU4XAFLj2eK%2FY1zAirK7efCY4ROYxMF%2BFqcfsUliSlllej5hWGiUHlG00KNH59luIUS7b%2FNGaQPruDbKDl%2BllxgDlnc9ST%2BUlG%2Func%2FSczNHkBcdCQxYP%2B2JJ2uS9ClYYzr1Df%2FBeQaml0qUw5nZ0aD2K%2F67Ta%2Fx5gOauUQzCg%2F0JlqqNS1%2Fy1ipsPT7FW4EPevOwoZnDB6uFX4fYyl5LRzQbdgskS7nHXCORo93RYWXG%2BkMOKo6rwGOqUBxTeb5UUA9Oo4JYtGPWsX0ROBijkJBTx7fMQqchefxqGUS0wqrm2xsGuJ7DR6H003gic2epFa94%2BZX7aMjqnnXLp4YmGb37bm2KXl%2FlVpI0QnD8ZFKJqmHgBPX8JSCxKsJi8a6%2Bg76sPh%2FefPwrYZvhjbZQh9tgrjCyKXfpJD46taWAIQixG0TGHN7Y0YPxMGXmKGpQmd7whmLaSpSBUv3cLOQEZ1&X-Amz-Signature=199c1e2aa41d899989c45f1015e31f5dbb9cf6f02909f83e60a938ac13228b40&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGWNIULG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpsZyJEF81edGKReC6H3wVBdsxEuT%2FqnXvZeyGtDZEgQIgafxO7IBtqnnJK%2FTtOqbNPExCe5BSYsv7OQqla6wMhnwqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzAdsrFhhtUB27hPyrcA7PhHAyiS5x%2BgniqRPR26lzVfMotQ7T%2F5AZ%2FDfjZ4t16fLb0ePoDfFIi1uAiOPS6UveMagimlQMovNO3CutzaVhh9Auj4To5FDwq2Gb0pxFPcgV3zD3Lv28oVJNed%2FftGnSFSeSIhEGGE0Yy7sqxcTOMcqKpZWeGtp6ekIIVvmb9zIzMFs9E8CAf1CUyK6s2djwqfzZPTn%2BM3QFVs1DFHNiqF8rPEySG7nBUX0dsDyKDa9WbdofjOc2sSNE1ixUOCUOLv0sye8opq%2B3eBq8mJwllrCY13HH2vviDmUkKkOUk6vvrPV595D89Hfa06CNnEfOzmjpyzlCvDBPY46YKj2JW9X7%2BUO9gkLUfUEdhrE1IYhb1MLQ%2B7LCsRbLGX7SKv0FofaaMyIFpskU4XAFLj2eK%2FY1zAirK7efCY4ROYxMF%2BFqcfsUliSlllej5hWGiUHlG00KNH59luIUS7b%2FNGaQPruDbKDl%2BllxgDlnc9ST%2BUlG%2Func%2FSczNHkBcdCQxYP%2B2JJ2uS9ClYYzr1Df%2FBeQaml0qUw5nZ0aD2K%2F67Ta%2Fx5gOauUQzCg%2F0JlqqNS1%2Fy1ipsPT7FW4EPevOwoZnDB6uFX4fYyl5LRzQbdgskS7nHXCORo93RYWXG%2BkMOKo6rwGOqUBxTeb5UUA9Oo4JYtGPWsX0ROBijkJBTx7fMQqchefxqGUS0wqrm2xsGuJ7DR6H003gic2epFa94%2BZX7aMjqnnXLp4YmGb37bm2KXl%2FlVpI0QnD8ZFKJqmHgBPX8JSCxKsJi8a6%2Bg76sPh%2FefPwrYZvhjbZQh9tgrjCyKXfpJD46taWAIQixG0TGHN7Y0YPxMGXmKGpQmd7whmLaSpSBUv3cLOQEZ1&X-Amz-Signature=602f63d0f6361ead13a938997a0657f115a2ffd4b105f9fd7320e24fd94a73a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGWNIULG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpsZyJEF81edGKReC6H3wVBdsxEuT%2FqnXvZeyGtDZEgQIgafxO7IBtqnnJK%2FTtOqbNPExCe5BSYsv7OQqla6wMhnwqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzAdsrFhhtUB27hPyrcA7PhHAyiS5x%2BgniqRPR26lzVfMotQ7T%2F5AZ%2FDfjZ4t16fLb0ePoDfFIi1uAiOPS6UveMagimlQMovNO3CutzaVhh9Auj4To5FDwq2Gb0pxFPcgV3zD3Lv28oVJNed%2FftGnSFSeSIhEGGE0Yy7sqxcTOMcqKpZWeGtp6ekIIVvmb9zIzMFs9E8CAf1CUyK6s2djwqfzZPTn%2BM3QFVs1DFHNiqF8rPEySG7nBUX0dsDyKDa9WbdofjOc2sSNE1ixUOCUOLv0sye8opq%2B3eBq8mJwllrCY13HH2vviDmUkKkOUk6vvrPV595D89Hfa06CNnEfOzmjpyzlCvDBPY46YKj2JW9X7%2BUO9gkLUfUEdhrE1IYhb1MLQ%2B7LCsRbLGX7SKv0FofaaMyIFpskU4XAFLj2eK%2FY1zAirK7efCY4ROYxMF%2BFqcfsUliSlllej5hWGiUHlG00KNH59luIUS7b%2FNGaQPruDbKDl%2BllxgDlnc9ST%2BUlG%2Func%2FSczNHkBcdCQxYP%2B2JJ2uS9ClYYzr1Df%2FBeQaml0qUw5nZ0aD2K%2F67Ta%2Fx5gOauUQzCg%2F0JlqqNS1%2Fy1ipsPT7FW4EPevOwoZnDB6uFX4fYyl5LRzQbdgskS7nHXCORo93RYWXG%2BkMOKo6rwGOqUBxTeb5UUA9Oo4JYtGPWsX0ROBijkJBTx7fMQqchefxqGUS0wqrm2xsGuJ7DR6H003gic2epFa94%2BZX7aMjqnnXLp4YmGb37bm2KXl%2FlVpI0QnD8ZFKJqmHgBPX8JSCxKsJi8a6%2Bg76sPh%2FefPwrYZvhjbZQh9tgrjCyKXfpJD46taWAIQixG0TGHN7Y0YPxMGXmKGpQmd7whmLaSpSBUv3cLOQEZ1&X-Amz-Signature=1c0907ca87daee77b251c513c4a19c7568ed220bd3eba92f367720b17c77b354&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWNORYOG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDe5HcRW4BwZzpx5q3bg0bDSaV8JCyd8BKFFJvP0ZXZXAiBL97NqT3sQ2983mUwJOOTNHokxFoCDtGUJJrLD5qxSsyqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMS7EhiU88znO4ChpSKtwDItqesatau08ch44JYQiyzGGFtr460kC2Ep%2FAw7ykLGNxmkhqzm4%2FgxpLJTjm2POJ8FAkFqNOyGbhyAY%2Bt8BFV4aQp%2FjODVxgOjs%2BGKAz2D3uszmbFnE5juxFghaG1cA7yw6dpmPsjULEGyKeHzE9KCqQCnrULg%2BKy%2FkftOvUOnodyaLV2Eq%2FqnBM4L3MIbe64U3ArZLhwdt3nwaK1Z4bL9aKNXPynXgEularF7PsnCgATFahNCR%2FI%2FSlJScBOtNHlwkPJUYigHXOXaZkl19AuMZF8kzkGNbK7Z%2FEmplRrPXvNpLFIczTbNRbDItC0tLtvnJUjzzxbVabZgGVorrwbxHdASmfJD9LQu6Hr5KaF%2FmRbVFyWdzY9XQJOYmF1UaVTlrxSnOxqkX%2Bt%2B0O5Q5L%2FCNo%2Furizg7t6FevKYpZ5XRNfVmSHJr%2BiWkCNdJN7k43xXUrOuyFeve8c5Phu6cewhVKkgTJ5XPOVqxLuknPm5sXBN6mQ%2FtNO%2FeHo6BdDLasgdBGrC7J%2BWUijdDwGxogv98VmYLs8axWyepvk4fUqEKq3MnL1KNHEhvszi8FYAiSF%2B%2F%2B80y27MGdpjwNfxWJcwThldRo5afme%2FixBrpG3FxA%2FF%2BukV52wh7VogowpKrqvAY6pgG%2Fvyimj%2BcqFdX6jzpL2V2KBOnNaGRyVYa1HJzZZ3TZofQayEYFz%2BA3Z9NfTTsIW7JyYaPNTcjyEW5b4P3OcQ0tw9EJpLejzhilFe%2FcP6%2FX0IiDzlUhpjySfQZSNECQPt0%2FIOQ2IL0RQ0ROd1%2BNyDVc4RmURbEHSMojWhcXKbHwLrZaN8DvYu4XfBAVkt5Xq9%2B28lIcoZ2kE6FJEhwkUegdU%2BCZi3H3&X-Amz-Signature=9cea4bfe92922b3dcd290107597e5e1d6f25faf690098e1c82500bde1384736f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEOSEHU2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCA1aRVeRFXE9FdcJ4mIDokXCIUPOMqLP3dOnJSpUCMQgIgAnF04YHK5C5uyZdrKx7taex%2FhvPpiaKFlQt%2FvJpkPxUqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEfH3iK2fbNWmSxg%2FyrcA7yWnsjUvbpRudwkZx6GoXVGpVe83dMupPI5o3Og83f9tlxT7U6teUq33hHCtvte9nk3BUVFIiAh7A28SZCgAST%2Fq7ETzikQDbWBECAg9xvivIDTsRpH8SvU6iH0YkiQpzRcAY0J5IbqYOJwVRRdSoGUbO60FdnBJKBANV9mi0DlrLIBSkQxXGA%2Fqo4qls4xqd4HVcnFVOWbjpnfPLB%2FVpe7LD7VHOuS1HvsrSsplAzvAT2AjE92rPT%2F7vUM9JfQObaqVCoyn89Ryt9r%2FngtaDzDYvQbEJbmVveIpoCuVrd4o0UbL1BAi0%2Bqp1xe6kfIzudFnhZL7dLlOJca%2FCtGmFmcrGFEdYk%2F6BM6UaQj3mRINb6V4BtC9v9ec59J%2BzqEz7Lo%2BjunXZCjD2wCMEG7AVuXxdoQL2V3caRJ0GhmyMKjuZgRoD8TTFCNr3mT%2BW4%2F3ZZXE%2Bd4Kf8CQt7RUEltC2is6Bzos3YR6jvs1npxprz2E63%2FDeJfVO1f5SzclIji%2BsmRYDBnFw%2BXt6gUdUZv0fAdu1WLXbNRjKnXDFDBLvG39njErSeUqcnEjpljzyvLW2Nuy5e09s2zzrrhWuB%2FO3snM2kmifXnr13kWz%2Fq7LUhQACGb8vHXa2SBmSKMOio6rwGOqUBuCyrDL3DNoL%2BUbaRX1JBl25ybDgp1Ta6C9jtw44pYuYPANqkJuwUSnQcevXXUCANRoDsCPUk2Zbb0SBxIaBVCgMph3%2FjeCru6wJo38YDhjQ4K4kR9l0gsXpHE6yzjb5e9V3PZ7i190zewDITwPdS7bbcKqhEJV1%2Ba78rY0uoLs4ngz1wXTVi1X98WrKW%2Fm%2BBZwvJYXTwWEK9v4XjtLuIvKtiiAIW&X-Amz-Signature=e333998f12fb2c26c3fdd0358fe1297c5d4506e2780ec1187f655d4c2ba79987&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSP7B4TO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6D6qwEIvHt7JiBQmhPCpgLV7Je9GFexFtyPJpVjDYFwIhAM7GN55YefFnKIYqP68z0aGDhTXi2vMyEtdK0GJPXFbfKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyUTwIWhZsmwIAXgOIq3APlUnEnp%2F545bq5NDDV7B4vkYXkXr7dsjpP0ip%2FMB10PcTJgBx%2BuHta8KwNwhit78czgCBJQucHmYbwOLVk2hvYvNVa5YdYaokSjk2FtAN0yiuyNoi5wqQax0icLfkDSPdMSJwI6oscFxV8ixPCIaWlB%2BfbEAkgTvYV%2Fc7DZn39KcdxQlKoru9bwZizasZeuRnaBWc5ArucvliurMcjR9RebrF%2BaaX%2FfSoDd6VZ9CDqRhEBE%2BJW8%2FxFxvu6DO%2FNTFs9Pr%2BOpKIzzkx54nksez%2FJ3oed1ra%2BJl6xRKBqNsg2Sw21xXW%2BwYqnmMNLKrVj7Ji%2BJvt4Rhbia3Frn8YWTfZvyiIth15TJXHjlyExi0NrLkK2QTOarq6v2ze3RLSLJuLlQ5H1YXSj8i2GTKumGcBtsHgL3wxxKnVQFkz8VGZlunIWZZl33yuUfe8vVVxej%2Bda1BZ4UryBzQuPH11Lulv%2B8%2BAESOiIBJRMKRhIEH9dG7Ql1fdcvTtG8kNydO8CAhRFktQR62%2F2gPJZH1%2B5CjU4%2Bo%2FuQ4ZaTWv8T3Oa6BBzA3QVEicDF10%2B7tc1T7NNley2ltYP3UeQZiguVHF2NPvRUMZ2SjAB7%2FGDtnLW8XNUHRZSXaGpoQDhCoHKSzDOqeq8BjqkAY%2BzbQU8S86TCh%2FzY1WBeIRntm9XUnnmaR0zqk%2BLlg4w094q5I56fu4AOur5TnWOUFPoplmY5L2G6VgUyOVeeGFCrOtGP%2FrzMrlOyi3MJ%2FQHTu0tqyB8j2pbH%2Bu3bNoIFlOzocxIT0nJMJCB9pnidU83ZwV9bnaAtN%2FxIpUqE7Q6hh8nQ3DMrWGDJfjRv%2F0zIw7SN%2FzfSwBcG%2B1QNnxEP0YK714M&X-Amz-Signature=86377ee4b92b0f16d895f4ff1d578e517ed1237ce0fdca0a5476bfe7fa866d29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W7I52ZU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCQUTrGBDhO19%2FqT5pXIsfX804dlwbGjVIhiATuTLAKrgIfBddZMd1EuwIrB%2FnRZRYwir4fQv3iz5mERUuGw3qiVSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnBIVmEDJgAT3R7rLKtwDrwW3SaBsh0I4x%2F5B9q2zGA1VY9hEj%2BfmG1Gk5LFoZfC%2Bx2UMxlvRqFRCNkB8W8XGSQXik%2FGCuxupnYWqKChMN7oE2oMee7tgtZGboL12E7JJJXINSpJg3UBcw82h8VrAvUknAewIx7TS1A27Q16St0D6CHRUC%2Bs4%2B4VAdb3LPItnzG%2Bjn985rC%2F1muA4pRPYrdtjv%2FVHqam3Tpuhmri8PzUZ53tvvPxfkZOJCl785%2BXDpfmoOSAsFhchGbP1Sn0CyzNJjepR0CLvCrJsrx6a1giFCwcogo8HWXSNtWoEiHzpDABOMVFSlOmqyjesOWaBx0o%2B90EUvkeCGHZKJGKr3G0MOE1MR3f90uZW92iFkEzGK%2BZzWPRzfpn1po6IVQTxAB2%2B46xIjm4MA%2FwMghxhzk%2FI39UOUxILd2vZ5%2FZY5CereqkzkbGeYjvNBXBgQKhDP777kaFMXQyRxS8Cp2Fi1WMQGy9HpQbmvo4lAykUpOfEUBlS5e764b%2BHbcbYf%2BlphKhR4bWwleVyvGdWB5K5ct60O1fbVNooSz5RV9KDmU3z6cr%2Brvw7vGbh7L9BKsX301RKpPgyEN4KWG1m5hBrBrtJRBJxts%2BVwFm4%2BOOSBT1kF%2Bvgrth9RQSMD2swlKnqvAY6pgEUTGcZCD3H1jCHNYMKx0rui0NALZCTbIM7ikAl%2BZjyk107sYOR3p4qbM2FbFu86RPingj70ElU3EePjpRkmUmXt3VUm1KDAZlNGAq8h8Rg1lsB4aeIm%2FVsdn%2BfI9VErLyQvkScXC7CQV6bWnUxSCSotBBc8ewL1EzSoZGxcS066MbBDpGVi4CTUtJ9hhApVg51zquI9iF8kmlaHhOfABUpSYC50U6U&X-Amz-Signature=1c142a81173e415fe72d1fa82d2614f997e266a5baedf30220cd8403dcb8d568&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W7I52ZU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCQUTrGBDhO19%2FqT5pXIsfX804dlwbGjVIhiATuTLAKrgIfBddZMd1EuwIrB%2FnRZRYwir4fQv3iz5mERUuGw3qiVSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnBIVmEDJgAT3R7rLKtwDrwW3SaBsh0I4x%2F5B9q2zGA1VY9hEj%2BfmG1Gk5LFoZfC%2Bx2UMxlvRqFRCNkB8W8XGSQXik%2FGCuxupnYWqKChMN7oE2oMee7tgtZGboL12E7JJJXINSpJg3UBcw82h8VrAvUknAewIx7TS1A27Q16St0D6CHRUC%2Bs4%2B4VAdb3LPItnzG%2Bjn985rC%2F1muA4pRPYrdtjv%2FVHqam3Tpuhmri8PzUZ53tvvPxfkZOJCl785%2BXDpfmoOSAsFhchGbP1Sn0CyzNJjepR0CLvCrJsrx6a1giFCwcogo8HWXSNtWoEiHzpDABOMVFSlOmqyjesOWaBx0o%2B90EUvkeCGHZKJGKr3G0MOE1MR3f90uZW92iFkEzGK%2BZzWPRzfpn1po6IVQTxAB2%2B46xIjm4MA%2FwMghxhzk%2FI39UOUxILd2vZ5%2FZY5CereqkzkbGeYjvNBXBgQKhDP777kaFMXQyRxS8Cp2Fi1WMQGy9HpQbmvo4lAykUpOfEUBlS5e764b%2BHbcbYf%2BlphKhR4bWwleVyvGdWB5K5ct60O1fbVNooSz5RV9KDmU3z6cr%2Brvw7vGbh7L9BKsX301RKpPgyEN4KWG1m5hBrBrtJRBJxts%2BVwFm4%2BOOSBT1kF%2Bvgrth9RQSMD2swlKnqvAY6pgEUTGcZCD3H1jCHNYMKx0rui0NALZCTbIM7ikAl%2BZjyk107sYOR3p4qbM2FbFu86RPingj70ElU3EePjpRkmUmXt3VUm1KDAZlNGAq8h8Rg1lsB4aeIm%2FVsdn%2BfI9VErLyQvkScXC7CQV6bWnUxSCSotBBc8ewL1EzSoZGxcS066MbBDpGVi4CTUtJ9hhApVg51zquI9iF8kmlaHhOfABUpSYC50U6U&X-Amz-Signature=5f815b4bee8e4c6cba1887350ddd5d95583d27c8bc57b91fb6dd9d064fae8786&X-Amz-SignedHeaders=host&x-id=GetObject)

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
