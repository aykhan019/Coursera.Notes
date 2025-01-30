

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XE3QYUA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC2RozwEF3Y4E%2FeDVLx0WV9kJCUNuPqiZu3aRUtjDvmpAiEAgQBUVTWtzy7mERi2atxughGDh%2Ftk0V9O6n8AeN7wz5sqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPyqBTA30vusacePWyrcAzTDShFJWpWHm6xRq%2FYRrKosH%2BpysaGsNURvA5PxaMPCcmRLhLO2E%2Bzs%2BTjwIhYIYQuBtLT%2Bq0LnUSpMoxCElD9pYn5zDAlqJM%2FonNe2kk34Eey6IP3kh1vSW%2BIiBau7HXcIYsO5to0UCa1il4A%2BJE49RMkT%2B%2F7Vnrzk3IXT8MUb6nJgpTDyAXG%2BFjZBI331o4q50J9Man03y1o6JPI0Gv9nyOPzKZ3I8iEfVfOwtqtZZRSjg6syeO3nDQ2p34uv%2FgzvQz4gE6TSI4T1MBOufJ0qZB4YA0p3ujqZgP4cPpxRdqUGW4fQjRQz0D8z4EEFk3it8kYd4czEIZvYkicQGOA9F0jF9y%2B40CEbCXLV9jAmY%2BGf%2BSuxYmhMELvBmrcjOy%2FVYT%2BKEe3uLdAQrhWlE%2BoFmPbX0haeiZIVH%2FN4cmu44O%2B1G%2FofXOQUhjHn35COF3Bp52PDeq2U2hBh7Y1zaZCxe7z6BzpcfoymS%2FHmDrm45ETVq7OpYu%2BQ1PL4w99VWBottr6EbK6%2FBGut9cEbyJO45OEqSw1ejRrU7UhxLHrEOVMen8yUWgM%2BOaaMo0f6jnA3GpRixlsBB2kG2c8f6bQa%2Bs7o2fiCVLmJjeLIwse2yGxp5gdUhQbwgh2eMKyo7bwGOqUBhhNNZfeAQcjRiW3r%2FWJpoLc%2Fnb0dmPQa7BGuJPpJVLwAEql%2FgPWIx0zTyZ1SXisFH2XUvEIiiHWZNhUmGcAzYb9dJEBOzXAJ1iY83aZ5z1eO44iAyac3MsPE8TMGKZHqA5Gs0UdBIBhEy8MShvtFBorJT%2BvWLbgCIUmFNkITTRbqSsmnddB4KiQQs9Ioqp1hN5UrgyhOmN4g9933rFeV%2BRX5656p&X-Amz-Signature=0dc73a9585fc211bb5f2f71795f6fb19464ea79125f01bd2ad99d97dabd2e8f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XE3QYUA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC2RozwEF3Y4E%2FeDVLx0WV9kJCUNuPqiZu3aRUtjDvmpAiEAgQBUVTWtzy7mERi2atxughGDh%2Ftk0V9O6n8AeN7wz5sqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPyqBTA30vusacePWyrcAzTDShFJWpWHm6xRq%2FYRrKosH%2BpysaGsNURvA5PxaMPCcmRLhLO2E%2Bzs%2BTjwIhYIYQuBtLT%2Bq0LnUSpMoxCElD9pYn5zDAlqJM%2FonNe2kk34Eey6IP3kh1vSW%2BIiBau7HXcIYsO5to0UCa1il4A%2BJE49RMkT%2B%2F7Vnrzk3IXT8MUb6nJgpTDyAXG%2BFjZBI331o4q50J9Man03y1o6JPI0Gv9nyOPzKZ3I8iEfVfOwtqtZZRSjg6syeO3nDQ2p34uv%2FgzvQz4gE6TSI4T1MBOufJ0qZB4YA0p3ujqZgP4cPpxRdqUGW4fQjRQz0D8z4EEFk3it8kYd4czEIZvYkicQGOA9F0jF9y%2B40CEbCXLV9jAmY%2BGf%2BSuxYmhMELvBmrcjOy%2FVYT%2BKEe3uLdAQrhWlE%2BoFmPbX0haeiZIVH%2FN4cmu44O%2B1G%2FofXOQUhjHn35COF3Bp52PDeq2U2hBh7Y1zaZCxe7z6BzpcfoymS%2FHmDrm45ETVq7OpYu%2BQ1PL4w99VWBottr6EbK6%2FBGut9cEbyJO45OEqSw1ejRrU7UhxLHrEOVMen8yUWgM%2BOaaMo0f6jnA3GpRixlsBB2kG2c8f6bQa%2Bs7o2fiCVLmJjeLIwse2yGxp5gdUhQbwgh2eMKyo7bwGOqUBhhNNZfeAQcjRiW3r%2FWJpoLc%2Fnb0dmPQa7BGuJPpJVLwAEql%2FgPWIx0zTyZ1SXisFH2XUvEIiiHWZNhUmGcAzYb9dJEBOzXAJ1iY83aZ5z1eO44iAyac3MsPE8TMGKZHqA5Gs0UdBIBhEy8MShvtFBorJT%2BvWLbgCIUmFNkITTRbqSsmnddB4KiQQs9Ioqp1hN5UrgyhOmN4g9933rFeV%2BRX5656p&X-Amz-Signature=7c5b6952feaada3adba7f3d49ddef7af9ceec7bc55aa707cae515c8bb8a19ae6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XE3QYUA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC2RozwEF3Y4E%2FeDVLx0WV9kJCUNuPqiZu3aRUtjDvmpAiEAgQBUVTWtzy7mERi2atxughGDh%2Ftk0V9O6n8AeN7wz5sqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPyqBTA30vusacePWyrcAzTDShFJWpWHm6xRq%2FYRrKosH%2BpysaGsNURvA5PxaMPCcmRLhLO2E%2Bzs%2BTjwIhYIYQuBtLT%2Bq0LnUSpMoxCElD9pYn5zDAlqJM%2FonNe2kk34Eey6IP3kh1vSW%2BIiBau7HXcIYsO5to0UCa1il4A%2BJE49RMkT%2B%2F7Vnrzk3IXT8MUb6nJgpTDyAXG%2BFjZBI331o4q50J9Man03y1o6JPI0Gv9nyOPzKZ3I8iEfVfOwtqtZZRSjg6syeO3nDQ2p34uv%2FgzvQz4gE6TSI4T1MBOufJ0qZB4YA0p3ujqZgP4cPpxRdqUGW4fQjRQz0D8z4EEFk3it8kYd4czEIZvYkicQGOA9F0jF9y%2B40CEbCXLV9jAmY%2BGf%2BSuxYmhMELvBmrcjOy%2FVYT%2BKEe3uLdAQrhWlE%2BoFmPbX0haeiZIVH%2FN4cmu44O%2B1G%2FofXOQUhjHn35COF3Bp52PDeq2U2hBh7Y1zaZCxe7z6BzpcfoymS%2FHmDrm45ETVq7OpYu%2BQ1PL4w99VWBottr6EbK6%2FBGut9cEbyJO45OEqSw1ejRrU7UhxLHrEOVMen8yUWgM%2BOaaMo0f6jnA3GpRixlsBB2kG2c8f6bQa%2Bs7o2fiCVLmJjeLIwse2yGxp5gdUhQbwgh2eMKyo7bwGOqUBhhNNZfeAQcjRiW3r%2FWJpoLc%2Fnb0dmPQa7BGuJPpJVLwAEql%2FgPWIx0zTyZ1SXisFH2XUvEIiiHWZNhUmGcAzYb9dJEBOzXAJ1iY83aZ5z1eO44iAyac3MsPE8TMGKZHqA5Gs0UdBIBhEy8MShvtFBorJT%2BvWLbgCIUmFNkITTRbqSsmnddB4KiQQs9Ioqp1hN5UrgyhOmN4g9933rFeV%2BRX5656p&X-Amz-Signature=55828845e598b1ea988ac8353bc0df512bc4ae3f6761425fce26dd2cb905a9a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLEP5BKJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2aAGQrRFJmL3hwedC%2BW761N681HIMyNUN5TX7uYdK0wIgP15a6ZJsPxsbFF9nECKHFQfREp8mzAF1SvcVfsId%2Bk8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6%2FTJB%2FhbVtCoBgNircA0ZleTqSf78gQFvioZG7cPJn9o6qZ%2FgR2A6qkNQECs5cW9MazzzsgDABMf3NaQQYNlWoV5vnuPbdIAl4ZCzwCgFtx2iJTIabQDke1g98E80m9P%2FVXGJ09dCfN6bm8WjIjrCrjPH4WNYi012P5i0c%2F0ushaIJL1drJl0AcYUWdbrOgQpKRa7YhqBndE0doxol4cJV1N5rMogRzWSMwtNQ%2Fbe8o2F71tfKf0xs2%2BorlyceHb81O7AFH9gXQ9vvnaK%2FE3OggrKlv%2FhHnPtGICV1d4hFP9GPh9gI55ulVJCHR13YJBn8ESyZwSa%2BUyE9x7id4%2FZ8x0G22KnhJ7qaz6eXp%2FNWelsAYvVy9Nr1RJSJvkQUK0lUk0htPcWnrNQMCzBDEo6ojrlzY2VucHArtPc1m%2Bs2wlPkDZej%2Fa6TUOEGzZyjUXhj2IjKGVCy6nXespEWwaG5iuQmRUyuBS58%2F3cVsD0h141yTd1ClnlURknM%2Fihc1sy7k%2BsVbfKNv1rjsyem4l9UAjVIBI3ZfDB5C7OPm7DlxcqZDll6tFAo0JjOw0pGSdgaWUL6Qzr8fqUQx%2BNB1IQBz%2BlDZBIoNvuDYN3S64eUJEPZYQPi8CsHD9WPcJCIG2Wn%2B3AaEai5B2ySMJO77bwGOqUB%2FCEMxsqSuEw36LDyPZAka3LLNMHWNKQRSZ%2BY3LIETm23S55matLvchAPIQtN4x49BPYg9pF93PjvhzRq%2BrtT1LXoqp1a3ZFkhUXOc0U3lQptiNECwpgn0vZeMQroNO88WXuMKObXehzVZqt3iA2nXcztt%2F2m9UaoGCDHDws6dqJa59fCQYcRN9bfcGG3iiotadWEeS%2FqCmZrpCPo8t8PwYQaQsC0&X-Amz-Signature=651c801dc095bd2718be7934b0298c56d0a12abc096eb0cb800d405781fedd5b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLEP5BKJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2aAGQrRFJmL3hwedC%2BW761N681HIMyNUN5TX7uYdK0wIgP15a6ZJsPxsbFF9nECKHFQfREp8mzAF1SvcVfsId%2Bk8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6%2FTJB%2FhbVtCoBgNircA0ZleTqSf78gQFvioZG7cPJn9o6qZ%2FgR2A6qkNQECs5cW9MazzzsgDABMf3NaQQYNlWoV5vnuPbdIAl4ZCzwCgFtx2iJTIabQDke1g98E80m9P%2FVXGJ09dCfN6bm8WjIjrCrjPH4WNYi012P5i0c%2F0ushaIJL1drJl0AcYUWdbrOgQpKRa7YhqBndE0doxol4cJV1N5rMogRzWSMwtNQ%2Fbe8o2F71tfKf0xs2%2BorlyceHb81O7AFH9gXQ9vvnaK%2FE3OggrKlv%2FhHnPtGICV1d4hFP9GPh9gI55ulVJCHR13YJBn8ESyZwSa%2BUyE9x7id4%2FZ8x0G22KnhJ7qaz6eXp%2FNWelsAYvVy9Nr1RJSJvkQUK0lUk0htPcWnrNQMCzBDEo6ojrlzY2VucHArtPc1m%2Bs2wlPkDZej%2Fa6TUOEGzZyjUXhj2IjKGVCy6nXespEWwaG5iuQmRUyuBS58%2F3cVsD0h141yTd1ClnlURknM%2Fihc1sy7k%2BsVbfKNv1rjsyem4l9UAjVIBI3ZfDB5C7OPm7DlxcqZDll6tFAo0JjOw0pGSdgaWUL6Qzr8fqUQx%2BNB1IQBz%2BlDZBIoNvuDYN3S64eUJEPZYQPi8CsHD9WPcJCIG2Wn%2B3AaEai5B2ySMJO77bwGOqUB%2FCEMxsqSuEw36LDyPZAka3LLNMHWNKQRSZ%2BY3LIETm23S55matLvchAPIQtN4x49BPYg9pF93PjvhzRq%2BrtT1LXoqp1a3ZFkhUXOc0U3lQptiNECwpgn0vZeMQroNO88WXuMKObXehzVZqt3iA2nXcztt%2F2m9UaoGCDHDws6dqJa59fCQYcRN9bfcGG3iiotadWEeS%2FqCmZrpCPo8t8PwYQaQsC0&X-Amz-Signature=dfc0994d6993cf17117ae26a257b195702fc0e887f2d26c91205252956774d57&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLEP5BKJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2aAGQrRFJmL3hwedC%2BW761N681HIMyNUN5TX7uYdK0wIgP15a6ZJsPxsbFF9nECKHFQfREp8mzAF1SvcVfsId%2Bk8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6%2FTJB%2FhbVtCoBgNircA0ZleTqSf78gQFvioZG7cPJn9o6qZ%2FgR2A6qkNQECs5cW9MazzzsgDABMf3NaQQYNlWoV5vnuPbdIAl4ZCzwCgFtx2iJTIabQDke1g98E80m9P%2FVXGJ09dCfN6bm8WjIjrCrjPH4WNYi012P5i0c%2F0ushaIJL1drJl0AcYUWdbrOgQpKRa7YhqBndE0doxol4cJV1N5rMogRzWSMwtNQ%2Fbe8o2F71tfKf0xs2%2BorlyceHb81O7AFH9gXQ9vvnaK%2FE3OggrKlv%2FhHnPtGICV1d4hFP9GPh9gI55ulVJCHR13YJBn8ESyZwSa%2BUyE9x7id4%2FZ8x0G22KnhJ7qaz6eXp%2FNWelsAYvVy9Nr1RJSJvkQUK0lUk0htPcWnrNQMCzBDEo6ojrlzY2VucHArtPc1m%2Bs2wlPkDZej%2Fa6TUOEGzZyjUXhj2IjKGVCy6nXespEWwaG5iuQmRUyuBS58%2F3cVsD0h141yTd1ClnlURknM%2Fihc1sy7k%2BsVbfKNv1rjsyem4l9UAjVIBI3ZfDB5C7OPm7DlxcqZDll6tFAo0JjOw0pGSdgaWUL6Qzr8fqUQx%2BNB1IQBz%2BlDZBIoNvuDYN3S64eUJEPZYQPi8CsHD9WPcJCIG2Wn%2B3AaEai5B2ySMJO77bwGOqUB%2FCEMxsqSuEw36LDyPZAka3LLNMHWNKQRSZ%2BY3LIETm23S55matLvchAPIQtN4x49BPYg9pF93PjvhzRq%2BrtT1LXoqp1a3ZFkhUXOc0U3lQptiNECwpgn0vZeMQroNO88WXuMKObXehzVZqt3iA2nXcztt%2F2m9UaoGCDHDws6dqJa59fCQYcRN9bfcGG3iiotadWEeS%2FqCmZrpCPo8t8PwYQaQsC0&X-Amz-Signature=16d229e0ffef8d504a4c26bfc3bc8f82b87e8fa4bf357fda760ac5418070e5b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLEP5BKJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2aAGQrRFJmL3hwedC%2BW761N681HIMyNUN5TX7uYdK0wIgP15a6ZJsPxsbFF9nECKHFQfREp8mzAF1SvcVfsId%2Bk8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6%2FTJB%2FhbVtCoBgNircA0ZleTqSf78gQFvioZG7cPJn9o6qZ%2FgR2A6qkNQECs5cW9MazzzsgDABMf3NaQQYNlWoV5vnuPbdIAl4ZCzwCgFtx2iJTIabQDke1g98E80m9P%2FVXGJ09dCfN6bm8WjIjrCrjPH4WNYi012P5i0c%2F0ushaIJL1drJl0AcYUWdbrOgQpKRa7YhqBndE0doxol4cJV1N5rMogRzWSMwtNQ%2Fbe8o2F71tfKf0xs2%2BorlyceHb81O7AFH9gXQ9vvnaK%2FE3OggrKlv%2FhHnPtGICV1d4hFP9GPh9gI55ulVJCHR13YJBn8ESyZwSa%2BUyE9x7id4%2FZ8x0G22KnhJ7qaz6eXp%2FNWelsAYvVy9Nr1RJSJvkQUK0lUk0htPcWnrNQMCzBDEo6ojrlzY2VucHArtPc1m%2Bs2wlPkDZej%2Fa6TUOEGzZyjUXhj2IjKGVCy6nXespEWwaG5iuQmRUyuBS58%2F3cVsD0h141yTd1ClnlURknM%2Fihc1sy7k%2BsVbfKNv1rjsyem4l9UAjVIBI3ZfDB5C7OPm7DlxcqZDll6tFAo0JjOw0pGSdgaWUL6Qzr8fqUQx%2BNB1IQBz%2BlDZBIoNvuDYN3S64eUJEPZYQPi8CsHD9WPcJCIG2Wn%2B3AaEai5B2ySMJO77bwGOqUB%2FCEMxsqSuEw36LDyPZAka3LLNMHWNKQRSZ%2BY3LIETm23S55matLvchAPIQtN4x49BPYg9pF93PjvhzRq%2BrtT1LXoqp1a3ZFkhUXOc0U3lQptiNECwpgn0vZeMQroNO88WXuMKObXehzVZqt3iA2nXcztt%2F2m9UaoGCDHDws6dqJa59fCQYcRN9bfcGG3iiotadWEeS%2FqCmZrpCPo8t8PwYQaQsC0&X-Amz-Signature=813e3fa0611b3d4df9174e28a8764b9ff5d88d09c14f0d56058ffc406e57ac70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLEP5BKJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2aAGQrRFJmL3hwedC%2BW761N681HIMyNUN5TX7uYdK0wIgP15a6ZJsPxsbFF9nECKHFQfREp8mzAF1SvcVfsId%2Bk8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6%2FTJB%2FhbVtCoBgNircA0ZleTqSf78gQFvioZG7cPJn9o6qZ%2FgR2A6qkNQECs5cW9MazzzsgDABMf3NaQQYNlWoV5vnuPbdIAl4ZCzwCgFtx2iJTIabQDke1g98E80m9P%2FVXGJ09dCfN6bm8WjIjrCrjPH4WNYi012P5i0c%2F0ushaIJL1drJl0AcYUWdbrOgQpKRa7YhqBndE0doxol4cJV1N5rMogRzWSMwtNQ%2Fbe8o2F71tfKf0xs2%2BorlyceHb81O7AFH9gXQ9vvnaK%2FE3OggrKlv%2FhHnPtGICV1d4hFP9GPh9gI55ulVJCHR13YJBn8ESyZwSa%2BUyE9x7id4%2FZ8x0G22KnhJ7qaz6eXp%2FNWelsAYvVy9Nr1RJSJvkQUK0lUk0htPcWnrNQMCzBDEo6ojrlzY2VucHArtPc1m%2Bs2wlPkDZej%2Fa6TUOEGzZyjUXhj2IjKGVCy6nXespEWwaG5iuQmRUyuBS58%2F3cVsD0h141yTd1ClnlURknM%2Fihc1sy7k%2BsVbfKNv1rjsyem4l9UAjVIBI3ZfDB5C7OPm7DlxcqZDll6tFAo0JjOw0pGSdgaWUL6Qzr8fqUQx%2BNB1IQBz%2BlDZBIoNvuDYN3S64eUJEPZYQPi8CsHD9WPcJCIG2Wn%2B3AaEai5B2ySMJO77bwGOqUB%2FCEMxsqSuEw36LDyPZAka3LLNMHWNKQRSZ%2BY3LIETm23S55matLvchAPIQtN4x49BPYg9pF93PjvhzRq%2BrtT1LXoqp1a3ZFkhUXOc0U3lQptiNECwpgn0vZeMQroNO88WXuMKObXehzVZqt3iA2nXcztt%2F2m9UaoGCDHDws6dqJa59fCQYcRN9bfcGG3iiotadWEeS%2FqCmZrpCPo8t8PwYQaQsC0&X-Amz-Signature=12b3d88ed6df3fd7643672ae304395285d393056e4d25640785782f1d56f859a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLEP5BKJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2aAGQrRFJmL3hwedC%2BW761N681HIMyNUN5TX7uYdK0wIgP15a6ZJsPxsbFF9nECKHFQfREp8mzAF1SvcVfsId%2Bk8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6%2FTJB%2FhbVtCoBgNircA0ZleTqSf78gQFvioZG7cPJn9o6qZ%2FgR2A6qkNQECs5cW9MazzzsgDABMf3NaQQYNlWoV5vnuPbdIAl4ZCzwCgFtx2iJTIabQDke1g98E80m9P%2FVXGJ09dCfN6bm8WjIjrCrjPH4WNYi012P5i0c%2F0ushaIJL1drJl0AcYUWdbrOgQpKRa7YhqBndE0doxol4cJV1N5rMogRzWSMwtNQ%2Fbe8o2F71tfKf0xs2%2BorlyceHb81O7AFH9gXQ9vvnaK%2FE3OggrKlv%2FhHnPtGICV1d4hFP9GPh9gI55ulVJCHR13YJBn8ESyZwSa%2BUyE9x7id4%2FZ8x0G22KnhJ7qaz6eXp%2FNWelsAYvVy9Nr1RJSJvkQUK0lUk0htPcWnrNQMCzBDEo6ojrlzY2VucHArtPc1m%2Bs2wlPkDZej%2Fa6TUOEGzZyjUXhj2IjKGVCy6nXespEWwaG5iuQmRUyuBS58%2F3cVsD0h141yTd1ClnlURknM%2Fihc1sy7k%2BsVbfKNv1rjsyem4l9UAjVIBI3ZfDB5C7OPm7DlxcqZDll6tFAo0JjOw0pGSdgaWUL6Qzr8fqUQx%2BNB1IQBz%2BlDZBIoNvuDYN3S64eUJEPZYQPi8CsHD9WPcJCIG2Wn%2B3AaEai5B2ySMJO77bwGOqUB%2FCEMxsqSuEw36LDyPZAka3LLNMHWNKQRSZ%2BY3LIETm23S55matLvchAPIQtN4x49BPYg9pF93PjvhzRq%2BrtT1LXoqp1a3ZFkhUXOc0U3lQptiNECwpgn0vZeMQroNO88WXuMKObXehzVZqt3iA2nXcztt%2F2m9UaoGCDHDws6dqJa59fCQYcRN9bfcGG3iiotadWEeS%2FqCmZrpCPo8t8PwYQaQsC0&X-Amz-Signature=955eee054dc8f2e83d40abc856f3cded3d6182d951be0a07d4732d27afce367a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHQS2RB5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjxFSsaiApCvgAzSK%2FUTgUgd0Eb%2BUpzm72l8wpK94MOAiAXxXcr%2FwzJ6WWXGfZIYx5ka6cXhXuaiegbRimbzX2jDiqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXCgW6r9OvN8cZoEmKtwDdfwJ%2B3mfagtqiHV2zsH0ihXrhshrUJEfYJqMQYwzv%2B8hT85zrAuURlDmnr4hYx6QkS2%2BLFCDgZDoTh%2BfAqJYKA%2B8kErH%2FBcED%2BHKnwSYd1dTkKxM5B2W4OQk3%2Bc8Sb495GVqwWlI4GwljYr8QEiejdc%2BToFa3gytKgiRPNSZ%2BCfRM7NDdvCOOsCt%2B70nquz8lRX6DDqaXhQ6mvVja1BgmLYBCSN4BvgyfqNlBsWV4lJfJlzP7WgZVntYg0oYWZdv2td8Dn6dYwtw0L3lBndH10jU0CNLJfNWxwJCkNqSG%2BXTM1PeCxooOzZKjHUq3U0ROi3jTxWxivcqBV1HQA7Mq7%2B%2BrzH6t1arKgVIh0VvOK5jLPOYNgGDhwL8SPdPviq%2FwUzF8s7WohZtcdZ5zcAgktAd%2BmvxOG1lBp4BVk1VZ04FCRjlzeegsyTIpwlVLg2%2F9H8mryqDW9ORvE9j7g6wjhj4WtWsnVpMqAQDxoGRpDBlW103xurMEJTdrTpePXdLMn7wWdAR0tL95jXGakxQATdZ51iWMxOT11xd%2F7MgzSPEHnOcdUzKQvXbmiAsIRwCnzt9Hi%2BJls0bLJecJYHXnMM4IsOPVMuKkcR8JdYMxtc0VyCd%2F9WwAciss7MwxajtvAY6pgGyi5ZGRV1OnnJ0XRz9oP%2FhdUrFBlYUIFsN0LoapqWeXby%2BriowrvZvpRo0M8lTEkG5wZNPYAV1t9F7CXs8AEktx7nSqCQQHe%2Fxla0slEG%2Fh6L4IJaZ3%2Fnbnn9p1dVbhxmeKf3xyg1%2F7BUnGP8t574JsV5X1BxeHio93%2Bzia%2FMXR2Tdplfdu9jCnJosz9Il7hke%2FHzdgjNUB8MyBmQIaMCAPXpM%2BSA2&X-Amz-Signature=e3af6b7e347ae4b7182d17425e6a51d8626ef7a8a7691328923c0fea40801c38&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWD64LVL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBs%2FChczy897XcWQXqm%2FvVJFF2RDOJczK1E%2BQlcA91SdAiB9xQJVhk%2FX9AND%2Boc8mcsF8YnjkAQLxefBd5EMe3alkSqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMytjrfiSPa0k6ee6BKtwD13%2FjeeAa4WXvTs9RlXxUteCKo1lhfxKABUNcw9Df2OoHt7FfadVlkimLleCLWM5c%2BOY75AABr7DnSKBDmkt0GglEwP3c4FWHmF7LM2vuRVOuf4P1YOgg9jIkmXKrp%2BjEqLF3GHeCDSTK2HMjlmsOw9pJW7MnPRzpsRIKxhWStxultXx%2BvhBnY0agi%2F6v5mWuZkghGHqSYEQqMprxQ9bN5qkm0LqMKjCvNTgiJBzw9W242lfAIpdSQqiL2fHcA%2FzwWQUUQR7psu3OXGa%2BkYy%2F7b3We3g2Hj9X8UrgtbjuZtfxOXxW8BWAq4YY7X0aLdf1t772KXNldiKKsj%2F93jPeBKZ64rCaHz%2BNOr4vHE%2FvURq%2Fz17ery0k9lKiS9Tv2LDKQg46wqzU%2FYfM13DlmnFWr70lXXonoLWB2OE9tDW%2BRYTPzLAYT3g0AH5ty%2B01jqqD1NWEOzyUZUlO2hFMCH%2BpFvXycz52eR0fEOamhEYoBpLxanvxOSgk94AIJkelqz%2Bl9Xpp26sGyZbpvkQoTT9AXZaoqDf0RUOL4fWWgYdUhF4TZv7MIa9UuXPuBBloujTNfQIbBLM%2B7Tgekxh%2Bg7NJeAxDljDNApaDEQagHqaNPcIP6n1vp3sTyg1JNBMw%2FKftvAY6pgFHpq%2BOcuwvNqZvz3gvbwAS%2F0Q9LkjKy%2BVK3kNV704YJZoIkigAzj%2Fg%2F%2FrWsrTezLG3IfKqu2A3MBlsPzUNW8XAj9XEfx040ZEzjik9RIghydMyIpxUJ0owDCr9Fdb%2BGEnVyyRnONfzJQlnl%2F9HWKNEZkCTZI2jfW%2Br4YFt9Wc%2BCpM9%2BjaHguoLLtxbHovktmuKnzcYMR%2BOPEm3Kf2ATzCpkikX%2B%2BMF&X-Amz-Signature=7f9d20955e185c411b88bacc4e48e02d64ca3b69129d6faaf88a222fa8fd0107&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLEP5BKJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2aAGQrRFJmL3hwedC%2BW761N681HIMyNUN5TX7uYdK0wIgP15a6ZJsPxsbFF9nECKHFQfREp8mzAF1SvcVfsId%2Bk8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6%2FTJB%2FhbVtCoBgNircA0ZleTqSf78gQFvioZG7cPJn9o6qZ%2FgR2A6qkNQECs5cW9MazzzsgDABMf3NaQQYNlWoV5vnuPbdIAl4ZCzwCgFtx2iJTIabQDke1g98E80m9P%2FVXGJ09dCfN6bm8WjIjrCrjPH4WNYi012P5i0c%2F0ushaIJL1drJl0AcYUWdbrOgQpKRa7YhqBndE0doxol4cJV1N5rMogRzWSMwtNQ%2Fbe8o2F71tfKf0xs2%2BorlyceHb81O7AFH9gXQ9vvnaK%2FE3OggrKlv%2FhHnPtGICV1d4hFP9GPh9gI55ulVJCHR13YJBn8ESyZwSa%2BUyE9x7id4%2FZ8x0G22KnhJ7qaz6eXp%2FNWelsAYvVy9Nr1RJSJvkQUK0lUk0htPcWnrNQMCzBDEo6ojrlzY2VucHArtPc1m%2Bs2wlPkDZej%2Fa6TUOEGzZyjUXhj2IjKGVCy6nXespEWwaG5iuQmRUyuBS58%2F3cVsD0h141yTd1ClnlURknM%2Fihc1sy7k%2BsVbfKNv1rjsyem4l9UAjVIBI3ZfDB5C7OPm7DlxcqZDll6tFAo0JjOw0pGSdgaWUL6Qzr8fqUQx%2BNB1IQBz%2BlDZBIoNvuDYN3S64eUJEPZYQPi8CsHD9WPcJCIG2Wn%2B3AaEai5B2ySMJO77bwGOqUB%2FCEMxsqSuEw36LDyPZAka3LLNMHWNKQRSZ%2BY3LIETm23S55matLvchAPIQtN4x49BPYg9pF93PjvhzRq%2BrtT1LXoqp1a3ZFkhUXOc0U3lQptiNECwpgn0vZeMQroNO88WXuMKObXehzVZqt3iA2nXcztt%2F2m9UaoGCDHDws6dqJa59fCQYcRN9bfcGG3iiotadWEeS%2FqCmZrpCPo8t8PwYQaQsC0&X-Amz-Signature=7ff065c930fb0404bd32c6558392374ee18e29353042cd58562b9ea355b921c1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLEP5BKJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2aAGQrRFJmL3hwedC%2BW761N681HIMyNUN5TX7uYdK0wIgP15a6ZJsPxsbFF9nECKHFQfREp8mzAF1SvcVfsId%2Bk8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6%2FTJB%2FhbVtCoBgNircA0ZleTqSf78gQFvioZG7cPJn9o6qZ%2FgR2A6qkNQECs5cW9MazzzsgDABMf3NaQQYNlWoV5vnuPbdIAl4ZCzwCgFtx2iJTIabQDke1g98E80m9P%2FVXGJ09dCfN6bm8WjIjrCrjPH4WNYi012P5i0c%2F0ushaIJL1drJl0AcYUWdbrOgQpKRa7YhqBndE0doxol4cJV1N5rMogRzWSMwtNQ%2Fbe8o2F71tfKf0xs2%2BorlyceHb81O7AFH9gXQ9vvnaK%2FE3OggrKlv%2FhHnPtGICV1d4hFP9GPh9gI55ulVJCHR13YJBn8ESyZwSa%2BUyE9x7id4%2FZ8x0G22KnhJ7qaz6eXp%2FNWelsAYvVy9Nr1RJSJvkQUK0lUk0htPcWnrNQMCzBDEo6ojrlzY2VucHArtPc1m%2Bs2wlPkDZej%2Fa6TUOEGzZyjUXhj2IjKGVCy6nXespEWwaG5iuQmRUyuBS58%2F3cVsD0h141yTd1ClnlURknM%2Fihc1sy7k%2BsVbfKNv1rjsyem4l9UAjVIBI3ZfDB5C7OPm7DlxcqZDll6tFAo0JjOw0pGSdgaWUL6Qzr8fqUQx%2BNB1IQBz%2BlDZBIoNvuDYN3S64eUJEPZYQPi8CsHD9WPcJCIG2Wn%2B3AaEai5B2ySMJO77bwGOqUB%2FCEMxsqSuEw36LDyPZAka3LLNMHWNKQRSZ%2BY3LIETm23S55matLvchAPIQtN4x49BPYg9pF93PjvhzRq%2BrtT1LXoqp1a3ZFkhUXOc0U3lQptiNECwpgn0vZeMQroNO88WXuMKObXehzVZqt3iA2nXcztt%2F2m9UaoGCDHDws6dqJa59fCQYcRN9bfcGG3iiotadWEeS%2FqCmZrpCPo8t8PwYQaQsC0&X-Amz-Signature=67d715ca42608295845505262d359b23b965bc78c6681a304cd952c01fe2900c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLEP5BKJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2aAGQrRFJmL3hwedC%2BW761N681HIMyNUN5TX7uYdK0wIgP15a6ZJsPxsbFF9nECKHFQfREp8mzAF1SvcVfsId%2Bk8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6%2FTJB%2FhbVtCoBgNircA0ZleTqSf78gQFvioZG7cPJn9o6qZ%2FgR2A6qkNQECs5cW9MazzzsgDABMf3NaQQYNlWoV5vnuPbdIAl4ZCzwCgFtx2iJTIabQDke1g98E80m9P%2FVXGJ09dCfN6bm8WjIjrCrjPH4WNYi012P5i0c%2F0ushaIJL1drJl0AcYUWdbrOgQpKRa7YhqBndE0doxol4cJV1N5rMogRzWSMwtNQ%2Fbe8o2F71tfKf0xs2%2BorlyceHb81O7AFH9gXQ9vvnaK%2FE3OggrKlv%2FhHnPtGICV1d4hFP9GPh9gI55ulVJCHR13YJBn8ESyZwSa%2BUyE9x7id4%2FZ8x0G22KnhJ7qaz6eXp%2FNWelsAYvVy9Nr1RJSJvkQUK0lUk0htPcWnrNQMCzBDEo6ojrlzY2VucHArtPc1m%2Bs2wlPkDZej%2Fa6TUOEGzZyjUXhj2IjKGVCy6nXespEWwaG5iuQmRUyuBS58%2F3cVsD0h141yTd1ClnlURknM%2Fihc1sy7k%2BsVbfKNv1rjsyem4l9UAjVIBI3ZfDB5C7OPm7DlxcqZDll6tFAo0JjOw0pGSdgaWUL6Qzr8fqUQx%2BNB1IQBz%2BlDZBIoNvuDYN3S64eUJEPZYQPi8CsHD9WPcJCIG2Wn%2B3AaEai5B2ySMJO77bwGOqUB%2FCEMxsqSuEw36LDyPZAka3LLNMHWNKQRSZ%2BY3LIETm23S55matLvchAPIQtN4x49BPYg9pF93PjvhzRq%2BrtT1LXoqp1a3ZFkhUXOc0U3lQptiNECwpgn0vZeMQroNO88WXuMKObXehzVZqt3iA2nXcztt%2F2m9UaoGCDHDws6dqJa59fCQYcRN9bfcGG3iiotadWEeS%2FqCmZrpCPo8t8PwYQaQsC0&X-Amz-Signature=18c92afe4ebec972e5f39fb063f9c5f0da7ecc6a29843ddd4e687de8cbd541ad&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BKZ72QG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICiZX6TxVDyX4NPhx3PC0qC61gugzXHbeZihaaX2nGnUAiEApby26ANWOZ21XEzbyFFTcv6Fppk08SpySddfiW2gpQwqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEn6WhybqJVnkS0v6SrcAxcDmv0Wenz%2FC8nCmjhQZ82ZpXUFqYRUvNNcFXCjgAEK2UtpNa90nX8PObRIFsfHn7w6I7fe6091dzXPc2eQa1HapJmPfzaTyONkFEy4uHEhJnf516wRVMDf0HH%2BEIPbqzpmQOERJ583Sb%2F1XQLZOU%2FauSnFfpA80l14gtga539VQBkdhXq%2FyQlM8a9jyFCPEFhRKdd5PZTY4idbyJGH%2FA1RSHdXg7qXO6v12GxKktd7TJJSkLXdT5aMf61nB1j%2BI%2FT%2B4NEqeT9rA%2Fq9HpFb%2FePkgNMKu5Nz2bFOb1jhwk2KoB2NvXk3T5jxXN%2FrmMKLJaStkAKX2m35wNMNCSdFx215bD4MhEVoNysNMBLb2Et63RlbrgSbPFjNO2JFuomO8ITGggMw5VkqXs2SYPPjZOeuUz%2FFcSnDaM2OTRlHtmW%2BNkA10B5%2FPGx%2BsEmlQrlxSx19u7qkw0%2BBtIwk24D%2B29UcCEZDJqVovuEk1WTJI4Q%2FZMxCu15GGQbsp8UTBB51UiGOdWxe5uYzTrH896EEYHnbPemtNZcF1KNVIMq0Ud9DstXBrbMYpXh1cy0uitieglgt7bAm%2BWoHrtHjBYMYR99NI9pzUTEcKdV%2BbTftmCrD5iM%2FwFPxw0J7IrUuMN6o7bwGOqUB5A6aG6SkPbg0fqeh5EPP5DmrwIaqQcZePqgATedyWMnfJmx5Vj5USNBCsIJMzCdGU9ivW0jxObs08Osvo3TIeLrWKYoqcml3D72Ja%2Funoa%2BWt6%2Biz5xVeA3Xgraxx2DglgJuJetRnLQjFGppsLF9t78X2TkLoG0IDkByu1Km5g%2FByoCEXJkHU5nghH6THDcN5ezj0wF6PgxtdW1Q0YTMIfg%2FY3Dy&X-Amz-Signature=caabc65ca679be4cb92f532afb9499410f4e06e3586fd000deb4bd1c70849955&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A4ZMP42%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBSOT2L3%2BcdoN%2FhbKd21v4JLbLeTj%2FTVgn%2BkUCzGVfYmAiBbNrbmQaOBzz8A3ywgEqn6jVVzTk%2FP%2FhtOpE%2B8ADwrQiqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN4TTUDORomRmU3MqKtwD3HyNSxE5Dzxn1m93wFpyrp3zBX1c45D7kksRlm063Ln17gEYTPh0HF6V93dLxcXnvfdd31TG74EIOaytbVn0LczHlciTe%2F6TiHIr0m9VB2CMkBY9FxREIp%2F3EOFy2UzaeiXuYk7MXSFbAJF7ngn40dkTAKNZFo8qVrxsYDaCM00Gp1VlNB%2F6uH%2FUuCM5Lfzqx2k3OTa85ABTsA8W4AF9btJ97o3zxkkhkfHj9uYTNmMgYwYJf2o4y0bj9%2FvFsvIXB2f4fKsi2Ywo5JBhMmumuBx9sSPvUcAVblFZP4emvyD5tuxWPMBQElPkMK2BUzm7eEAywFt6JODs5ArId6nicyX7fwbi7h4XpIsm7m4IGkW3uSqS2xVSJe%2FCM7oV9Da%2FRHa01D9mLbH0L5GcDNz%2FJ7jtSeKjznZAi7EOknNH7I8s9RwR5CYj5PJm5WkuZaTNJnP0toPndNo2PAMQK7lxOa26aO5z4Q6j5cznAAoUVO%2BRIa7Y5SK%2FIbm2SSGBdqKFCRfWEKeo0Yin%2FYxNfeeV5CXMrM5lNDpixjKtL8Si1x%2Fe%2BslVw91zlu9kTH74495tf0HvSVrMkt%2FXgCtLPjsQ%2B7f410HDryUDqVe%2BkrRYJxC%2Fxogm6y5p1BToFaww7qntvAY6pgE0WEdm6G45sYoMC7uimOOYYeWjlFkL53hw3rXk%2BHPsweUDYBzH%2BsFpv7E5jTECH82r6BYX2IOjZ4ntVMXDuu1FgTBLOLSBoA%2ByNtBtzeQ%2BtO8yS%2BERt%2FMDWAWBLjlEx9M64o%2B3Oa4QjYY%2FtEMPhvOiG1iCQKDyWcx7eiuRjo%2F5dm9dM5vR78wdIKhHL70wBt5lskV5V7aqBrcJsAqr8B%2FUmQM%2BQmnt&X-Amz-Signature=9e7821dd499e667c7f1d77d4ec1e06c4696ac536f368e4394b733a5054a07074&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNOP7HZ3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB1OHkeZY1ZObMLyYArXYwoPkCZrH%2FWefhrwArV7XHN8AiEAqXG5TdGbtkn3hcIJ4%2BgoELcZw8IpsDYP85sg8mfe%2BnwqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGQhgVWCkQgbF1QuBircA%2FPz43dbQKycG3hK7GC%2Fc67PrOfrCsVMljekyAJsxkf7Z6UMXxtC08iWlqc51INc5VFyeAc2Tb6rGrnqBjR3WAlj2dtYLYOFRkoqkdpEi51ElhIp9poF3c5B0fM9169KXrYdnn5uA2BKvZ9lSSxABpuUh6rMSVXWmLlTxqj2A5vfM%2BI%2FfIsyX%2F7JbouLHtbiHo1BtlbiJ997U5owjb7Ossh83BQFUcD7%2B1RuCEN%2Bz1jXh2uPlwX1wIUowQqNMZmO%2F4bnakHtDi0pCF792A86wfvf2psdWpEMFC4tC4ESiZTsVxspUcGiAaXeIljx01Rm21QXl4k1KNBWj32w5%2Bk8%2BFE6URd5U8xJVdCajA4NYEKajdPcxsgEMPFz6NFP9Rxgv9vZhH3bdGJeDp75X91uG8BI4g2DvX4piq7VwS98WwuW8rIlWtiUY3aRcaEDoVoYLRCM0MZzg5KANb8FEStju1llEz5IfajEKViGUzlYaDLT2Vd3f%2BpQAqK0%2F22993YunsZwc2g4toCA4V78Cbe2Sf6bWlPXfwGWpDkS9BrG2Kxg0v%2FUIzXWgWMYRPz4lqvLReg2uDDj4%2FHrrDCuOZLXOmQgtBcj5OBRPhOFLgXUOLpbKntkPM%2BtehzuwyhcMIuq7bwGOqUBgCmTbfROuKOW2z%2F9uJXMVlXoEjiN4Wenrfn1tACxe2sQPgbEG7TP7anr3vUGg1hxY3n6mQ6s3Hdv4NMKOap36Ct2ga%2BUZ8XdUKFnaPFx0aXYouv96byJkFa7Ca8r6yxSkx7G7GmKTPJFp%2BM1Iy0I9JmkamQzuhBmf%2F9VhCRwnf1PnhdXANVSsU%2Bhqeutdp5SYJ05CC5B5M9Ow2%2F%2FWr1uQXtl8vFl&X-Amz-Signature=047938bc88f66b66c70cbdbc4af29caa5547897586cdadede1904c7acb98b780&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UJX3PCG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRVJ3HRv7a1AybILy%2BdHrn90T1NDfuRm2NFhEirBI9ngIgf0riRzfk5Pi%2BszGDE8H8SIUxyE22lUuxQP4mpZdUHXIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK9uUbmu6wtG96tdSyrcA1kGy9AIKYUB3wLIxIjHLfUi0Lj%2FAz6Nc6boiTRdEUtQ%2BwV%2FFQ96mYsfnahDX5%2FaZt5Zv%2FEGlQJ9w5Bq0ULHmoNBAxLnhg8nGM1WlTDTdR2eJsTsKmy8arI9Uu4B0bjDTMUtkVxIPDHcQmznN5yD4Gkl8udFXBFNVL5l5QCP3eGkid8t7a1IoylGPlJdI5WAKR9tRnQogN%2FxBSd82W%2Fs2z%2FElGNdOQGJAnTuAko6a4DEW2Tqv5kQgwOvVkg7ZxRm78a7mDl6uQZSSaFInW1Zfwh2oYF8aYNMQOgMPjtQV72qZtkgv3%2Bvxbb4eoJtvOOo4qCZB4Kv7%2BfJadAzWNtz4UpPqwvnLHCCIQz9fymo4zK%2FaMBlnGBkbPm5JdrMR1L9vxSakqBx2CtYjoOxqgoMQI2PNv1%2BHH6QAYiYzL2eWq1seYhNYGjv3YgXP4se4Nrs4O4Ukfp8V6XKQ0uFk4VTwcutJXqRQ1h0QOB1NwpfHmjRIK7F4HykUOsPNt9D6SrbgqZ6fOgy7iioo1CnC96INyIkrpiUzhdTQ45GQfxA45Uw14ewb6IwdbDvLEF%2FG%2B6XK7OyffFKQ2xgS9%2BypVYg9i0MUwqrOgXqxnlnRd4YbRjTaOJ4okm7tJI0QhQSMOio7bwGOqUBKWTBa5QLKGW2RglQLlB5a651DqcQs6Bdf7rp8vSTrQyJMbdLjbjcebV5Yh%2F3atHEohfua17pVTSdDVqR9Zo0HHNDvDxkUMBFnqP1sMfuA64lb3IYyc5tZqqkyT3s9pzBk4Ka4RFlHPG%2F2EHlF2k2JcQFq%2Fgt0wV12fFcghYI%2FOhvoQRtt%2BYYlC5h5MJeU4DOHq09CEJNjJo0X5ZMDTtxKVRhWbpg&X-Amz-Signature=bf78c57b715c84088d6f12e56249e36ede3b6a68e9ab5f17e32fb5a78c752536&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UJX3PCG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRVJ3HRv7a1AybILy%2BdHrn90T1NDfuRm2NFhEirBI9ngIgf0riRzfk5Pi%2BszGDE8H8SIUxyE22lUuxQP4mpZdUHXIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK9uUbmu6wtG96tdSyrcA1kGy9AIKYUB3wLIxIjHLfUi0Lj%2FAz6Nc6boiTRdEUtQ%2BwV%2FFQ96mYsfnahDX5%2FaZt5Zv%2FEGlQJ9w5Bq0ULHmoNBAxLnhg8nGM1WlTDTdR2eJsTsKmy8arI9Uu4B0bjDTMUtkVxIPDHcQmznN5yD4Gkl8udFXBFNVL5l5QCP3eGkid8t7a1IoylGPlJdI5WAKR9tRnQogN%2FxBSd82W%2Fs2z%2FElGNdOQGJAnTuAko6a4DEW2Tqv5kQgwOvVkg7ZxRm78a7mDl6uQZSSaFInW1Zfwh2oYF8aYNMQOgMPjtQV72qZtkgv3%2Bvxbb4eoJtvOOo4qCZB4Kv7%2BfJadAzWNtz4UpPqwvnLHCCIQz9fymo4zK%2FaMBlnGBkbPm5JdrMR1L9vxSakqBx2CtYjoOxqgoMQI2PNv1%2BHH6QAYiYzL2eWq1seYhNYGjv3YgXP4se4Nrs4O4Ukfp8V6XKQ0uFk4VTwcutJXqRQ1h0QOB1NwpfHmjRIK7F4HykUOsPNt9D6SrbgqZ6fOgy7iioo1CnC96INyIkrpiUzhdTQ45GQfxA45Uw14ewb6IwdbDvLEF%2FG%2B6XK7OyffFKQ2xgS9%2BypVYg9i0MUwqrOgXqxnlnRd4YbRjTaOJ4okm7tJI0QhQSMOio7bwGOqUBKWTBa5QLKGW2RglQLlB5a651DqcQs6Bdf7rp8vSTrQyJMbdLjbjcebV5Yh%2F3atHEohfua17pVTSdDVqR9Zo0HHNDvDxkUMBFnqP1sMfuA64lb3IYyc5tZqqkyT3s9pzBk4Ka4RFlHPG%2F2EHlF2k2JcQFq%2Fgt0wV12fFcghYI%2FOhvoQRtt%2BYYlC5h5MJeU4DOHq09CEJNjJo0X5ZMDTtxKVRhWbpg&X-Amz-Signature=261b95feb272a4d426e0b08f4575c1bbae454886321b00eb016c0ad79de84f05&X-Amz-SignedHeaders=host&x-id=GetObject)

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
