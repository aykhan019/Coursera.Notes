

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJGOQOGO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCASBjICjLsKAsuhySiZ7ttK%2FoZBB%2FZ9TgQ4DetNTXHWwIhANfkbfkhGWuG%2BERr86lMoDMPQn9zNF8LV6vOoX1x8EsLKv8DCDcQABoMNjM3NDIzMTgzODA1IgxTZUOnTXLSFhL5Ff4q3AOGk%2B%2Fy4S6RPEPxGWqY9t1MF46GZIiUWclX8sG0fsCLd6T09mh2cDyOmVrcpJzwVtluB0KsGK%2BYWDIKcabYD24fCeRvsTqPfMD9ntih%2F9vfwPShrxjjzxa0caA%2BkhJFgeSLR8tOQs7uWwChWgbdYQ37dIW0JPDZHI8Zsk5FTRKCg3lfidm2sMtrWQ9bI7O7hrIyXyjNnvaZcPtH6eMMHpFExj%2BDYLditSjumx4wPKlrn2dhjPKxx1s3MH8nH732HIAzONyKfgRxm7%2F0M5rPP4csCcGKcEBsZQ8idr1upOVeaoysHJq5mGbvQ%2Bdr%2B7%2B3AvFXyGPSjynixSRzwSCv9j8ORAkq5pKLHkrRma20RXLzFJbJ1xvwehjgHT6j8B7s7Y8kKN98I%2B1oQA3HHbiPMDx5olKmPHzPd2GNdpamAacI2H%2FVpQ58YJo8ADhgnNcN17Jns%2BpgGucg6YL3g4vLXpQk0K3BneEa6mvbiWy53QghxdFjBJPMUvQotacGi7qKyfvmnIFCm9M07QFr1a6XPuTainPaM7BPCTawy541acyWA9bazExmzFQ8mfaCAHHFla6WPQEoFFBhGXgBJHxr%2FRv4FBaYeGkVe7S1QOUOogzKo5T9JNC7%2FY3YTbq4YjCslIq9BjqkASlL2N8XuqRdkPyZ4ygldVmM0Tzqx9GaVcLME4fb7FwfxZ0jj0vLGeMKEPe398eeNuLU1dqUUTFXJd0lCOAeBOj2kfClLCg%2FDEVeWIb93EaqmDEsPRugvKrOQs2v%2FOpx2iuCDR02qe7zmQ9IpYMzTYKU5QEuqe%2BnGU36Lc%2Fbw3GzBsWzoOsV6bdYLlJPfouD8hQV6DNo3FcJZ0UQagT1jJ9G2ftX&X-Amz-Signature=0ee909d3d120cc0e04c9e854ba443016c1a99108590db6f05783a764eaf0b365&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJGOQOGO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCASBjICjLsKAsuhySiZ7ttK%2FoZBB%2FZ9TgQ4DetNTXHWwIhANfkbfkhGWuG%2BERr86lMoDMPQn9zNF8LV6vOoX1x8EsLKv8DCDcQABoMNjM3NDIzMTgzODA1IgxTZUOnTXLSFhL5Ff4q3AOGk%2B%2Fy4S6RPEPxGWqY9t1MF46GZIiUWclX8sG0fsCLd6T09mh2cDyOmVrcpJzwVtluB0KsGK%2BYWDIKcabYD24fCeRvsTqPfMD9ntih%2F9vfwPShrxjjzxa0caA%2BkhJFgeSLR8tOQs7uWwChWgbdYQ37dIW0JPDZHI8Zsk5FTRKCg3lfidm2sMtrWQ9bI7O7hrIyXyjNnvaZcPtH6eMMHpFExj%2BDYLditSjumx4wPKlrn2dhjPKxx1s3MH8nH732HIAzONyKfgRxm7%2F0M5rPP4csCcGKcEBsZQ8idr1upOVeaoysHJq5mGbvQ%2Bdr%2B7%2B3AvFXyGPSjynixSRzwSCv9j8ORAkq5pKLHkrRma20RXLzFJbJ1xvwehjgHT6j8B7s7Y8kKN98I%2B1oQA3HHbiPMDx5olKmPHzPd2GNdpamAacI2H%2FVpQ58YJo8ADhgnNcN17Jns%2BpgGucg6YL3g4vLXpQk0K3BneEa6mvbiWy53QghxdFjBJPMUvQotacGi7qKyfvmnIFCm9M07QFr1a6XPuTainPaM7BPCTawy541acyWA9bazExmzFQ8mfaCAHHFla6WPQEoFFBhGXgBJHxr%2FRv4FBaYeGkVe7S1QOUOogzKo5T9JNC7%2FY3YTbq4YjCslIq9BjqkASlL2N8XuqRdkPyZ4ygldVmM0Tzqx9GaVcLME4fb7FwfxZ0jj0vLGeMKEPe398eeNuLU1dqUUTFXJd0lCOAeBOj2kfClLCg%2FDEVeWIb93EaqmDEsPRugvKrOQs2v%2FOpx2iuCDR02qe7zmQ9IpYMzTYKU5QEuqe%2BnGU36Lc%2Fbw3GzBsWzoOsV6bdYLlJPfouD8hQV6DNo3FcJZ0UQagT1jJ9G2ftX&X-Amz-Signature=21cc9ec767bb913e2a814b3833458424f76e6bcc532bc2e3819067f8dc3093fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJGOQOGO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCASBjICjLsKAsuhySiZ7ttK%2FoZBB%2FZ9TgQ4DetNTXHWwIhANfkbfkhGWuG%2BERr86lMoDMPQn9zNF8LV6vOoX1x8EsLKv8DCDcQABoMNjM3NDIzMTgzODA1IgxTZUOnTXLSFhL5Ff4q3AOGk%2B%2Fy4S6RPEPxGWqY9t1MF46GZIiUWclX8sG0fsCLd6T09mh2cDyOmVrcpJzwVtluB0KsGK%2BYWDIKcabYD24fCeRvsTqPfMD9ntih%2F9vfwPShrxjjzxa0caA%2BkhJFgeSLR8tOQs7uWwChWgbdYQ37dIW0JPDZHI8Zsk5FTRKCg3lfidm2sMtrWQ9bI7O7hrIyXyjNnvaZcPtH6eMMHpFExj%2BDYLditSjumx4wPKlrn2dhjPKxx1s3MH8nH732HIAzONyKfgRxm7%2F0M5rPP4csCcGKcEBsZQ8idr1upOVeaoysHJq5mGbvQ%2Bdr%2B7%2B3AvFXyGPSjynixSRzwSCv9j8ORAkq5pKLHkrRma20RXLzFJbJ1xvwehjgHT6j8B7s7Y8kKN98I%2B1oQA3HHbiPMDx5olKmPHzPd2GNdpamAacI2H%2FVpQ58YJo8ADhgnNcN17Jns%2BpgGucg6YL3g4vLXpQk0K3BneEa6mvbiWy53QghxdFjBJPMUvQotacGi7qKyfvmnIFCm9M07QFr1a6XPuTainPaM7BPCTawy541acyWA9bazExmzFQ8mfaCAHHFla6WPQEoFFBhGXgBJHxr%2FRv4FBaYeGkVe7S1QOUOogzKo5T9JNC7%2FY3YTbq4YjCslIq9BjqkASlL2N8XuqRdkPyZ4ygldVmM0Tzqx9GaVcLME4fb7FwfxZ0jj0vLGeMKEPe398eeNuLU1dqUUTFXJd0lCOAeBOj2kfClLCg%2FDEVeWIb93EaqmDEsPRugvKrOQs2v%2FOpx2iuCDR02qe7zmQ9IpYMzTYKU5QEuqe%2BnGU36Lc%2Fbw3GzBsWzoOsV6bdYLlJPfouD8hQV6DNo3FcJZ0UQagT1jJ9G2ftX&X-Amz-Signature=584ae71dbd05e786691557578f9bc9771aeba355e3959d1bcac640a99c7b17e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5W2OYF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEQ%2BJKLM%2Bb7HB8TzlnzjO%2BaGgEG7vtkdxtVZ4%2BYMZg7XAiAucHtO4EQ7Qnfb0DTitZ7%2BNeFJ%2BYI9zIa%2Fg3Uo7oUWVSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMRXENOAYq4eTtYyQFKtwDq0OOb7vyKjW5f5RE6wBDufS%2FIeZHtupJz4sk1BfjWivl8GEMHVtZE3q0ksXUZyexwQgGYXZlT5OQyUVlJ1KYzBJH6Y11EcBoiBBYAVRU4gJNWtilbSsRdtQdRrkGF4%2BlPJIGSE5XiiblgTX7eIiUvC2bv9mp4bhYxIaBoYgIZ2MSXiGi3splzre0RL26diPywl0GlNM2CtF8H%2F%2FHKt07rtV9caEGJXekc7PV24x9syKGaJ6Iiz1OEpsWxdygBfOvYpsOv8Nl2%2BtREqx%2FBBm0MbuZgqGEkHgvNIexXzOCs3mYJy6IBJi%2FBUbJhTeUHrErW%2BkZlMGdZSWHrn6OPn3g1nSQxUaAhCIIvN4J3pVX4w6q%2Ffb%2FoQ2qFyu6EoPNwRAvaACdOoY1qNCa265kfD30DKF4xpzAlcuKCyqAO9THd7Ws6l4wcVS1S8d8324QX6DqfdgxF3Iy5yYNr2u1Gao6e6kyBLCSRTWorhsx3DlnnW4x7E0Q0mLsxgz7Ex18fPBsVj3cXGblyQJodDgRYTLDPJhFynnQJMp4vv26CNkHItM6wrAXYW4glu08iHxWDSxoqPmAoZV5LV8GmOqzHn%2FiHfaDyMR3YF9JA520vdB63hGbN1CADPQTxeT08VYwwZSKvQY6pgGA2JVHwEqqkhpDmt7Im2OKDfj0HEdwu%2BV8m0sEpaM%2Fn8R%2BMDyvoHTbUhFFRyOW79fZEJZUC3HDFZcDQe%2F%2FwgL0Hl%2FBWs4pn5wjNukzmT4TfEJljs3cMWbgM9C%2FacBIFmlSWOaH6MazuKPq26l2JxZLi3jsKzT53x4VKC761szrC0NKCurA%2BUZhkkCAWLzgxERJKJaLHCRVclh%2BAwwdF5dv16q%2FW%2Ff5&X-Amz-Signature=5aaf8ce35a7afb210ba0a1747fb3a9d1b1d0965d45bfe6195b30be073fbd6d4a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5W2OYF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEQ%2BJKLM%2Bb7HB8TzlnzjO%2BaGgEG7vtkdxtVZ4%2BYMZg7XAiAucHtO4EQ7Qnfb0DTitZ7%2BNeFJ%2BYI9zIa%2Fg3Uo7oUWVSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMRXENOAYq4eTtYyQFKtwDq0OOb7vyKjW5f5RE6wBDufS%2FIeZHtupJz4sk1BfjWivl8GEMHVtZE3q0ksXUZyexwQgGYXZlT5OQyUVlJ1KYzBJH6Y11EcBoiBBYAVRU4gJNWtilbSsRdtQdRrkGF4%2BlPJIGSE5XiiblgTX7eIiUvC2bv9mp4bhYxIaBoYgIZ2MSXiGi3splzre0RL26diPywl0GlNM2CtF8H%2F%2FHKt07rtV9caEGJXekc7PV24x9syKGaJ6Iiz1OEpsWxdygBfOvYpsOv8Nl2%2BtREqx%2FBBm0MbuZgqGEkHgvNIexXzOCs3mYJy6IBJi%2FBUbJhTeUHrErW%2BkZlMGdZSWHrn6OPn3g1nSQxUaAhCIIvN4J3pVX4w6q%2Ffb%2FoQ2qFyu6EoPNwRAvaACdOoY1qNCa265kfD30DKF4xpzAlcuKCyqAO9THd7Ws6l4wcVS1S8d8324QX6DqfdgxF3Iy5yYNr2u1Gao6e6kyBLCSRTWorhsx3DlnnW4x7E0Q0mLsxgz7Ex18fPBsVj3cXGblyQJodDgRYTLDPJhFynnQJMp4vv26CNkHItM6wrAXYW4glu08iHxWDSxoqPmAoZV5LV8GmOqzHn%2FiHfaDyMR3YF9JA520vdB63hGbN1CADPQTxeT08VYwwZSKvQY6pgGA2JVHwEqqkhpDmt7Im2OKDfj0HEdwu%2BV8m0sEpaM%2Fn8R%2BMDyvoHTbUhFFRyOW79fZEJZUC3HDFZcDQe%2F%2FwgL0Hl%2FBWs4pn5wjNukzmT4TfEJljs3cMWbgM9C%2FacBIFmlSWOaH6MazuKPq26l2JxZLi3jsKzT53x4VKC761szrC0NKCurA%2BUZhkkCAWLzgxERJKJaLHCRVclh%2BAwwdF5dv16q%2FW%2Ff5&X-Amz-Signature=3a171db678fee00e428c472db705b8caf0dab6f169a7439201e4d8307087e0ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5W2OYF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEQ%2BJKLM%2Bb7HB8TzlnzjO%2BaGgEG7vtkdxtVZ4%2BYMZg7XAiAucHtO4EQ7Qnfb0DTitZ7%2BNeFJ%2BYI9zIa%2Fg3Uo7oUWVSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMRXENOAYq4eTtYyQFKtwDq0OOb7vyKjW5f5RE6wBDufS%2FIeZHtupJz4sk1BfjWivl8GEMHVtZE3q0ksXUZyexwQgGYXZlT5OQyUVlJ1KYzBJH6Y11EcBoiBBYAVRU4gJNWtilbSsRdtQdRrkGF4%2BlPJIGSE5XiiblgTX7eIiUvC2bv9mp4bhYxIaBoYgIZ2MSXiGi3splzre0RL26diPywl0GlNM2CtF8H%2F%2FHKt07rtV9caEGJXekc7PV24x9syKGaJ6Iiz1OEpsWxdygBfOvYpsOv8Nl2%2BtREqx%2FBBm0MbuZgqGEkHgvNIexXzOCs3mYJy6IBJi%2FBUbJhTeUHrErW%2BkZlMGdZSWHrn6OPn3g1nSQxUaAhCIIvN4J3pVX4w6q%2Ffb%2FoQ2qFyu6EoPNwRAvaACdOoY1qNCa265kfD30DKF4xpzAlcuKCyqAO9THd7Ws6l4wcVS1S8d8324QX6DqfdgxF3Iy5yYNr2u1Gao6e6kyBLCSRTWorhsx3DlnnW4x7E0Q0mLsxgz7Ex18fPBsVj3cXGblyQJodDgRYTLDPJhFynnQJMp4vv26CNkHItM6wrAXYW4glu08iHxWDSxoqPmAoZV5LV8GmOqzHn%2FiHfaDyMR3YF9JA520vdB63hGbN1CADPQTxeT08VYwwZSKvQY6pgGA2JVHwEqqkhpDmt7Im2OKDfj0HEdwu%2BV8m0sEpaM%2Fn8R%2BMDyvoHTbUhFFRyOW79fZEJZUC3HDFZcDQe%2F%2FwgL0Hl%2FBWs4pn5wjNukzmT4TfEJljs3cMWbgM9C%2FacBIFmlSWOaH6MazuKPq26l2JxZLi3jsKzT53x4VKC761szrC0NKCurA%2BUZhkkCAWLzgxERJKJaLHCRVclh%2BAwwdF5dv16q%2FW%2Ff5&X-Amz-Signature=67932fe6f4c4e6a01996ee481d7885ee520d467bb3c62e83a2c19cf342186725&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5W2OYF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEQ%2BJKLM%2Bb7HB8TzlnzjO%2BaGgEG7vtkdxtVZ4%2BYMZg7XAiAucHtO4EQ7Qnfb0DTitZ7%2BNeFJ%2BYI9zIa%2Fg3Uo7oUWVSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMRXENOAYq4eTtYyQFKtwDq0OOb7vyKjW5f5RE6wBDufS%2FIeZHtupJz4sk1BfjWivl8GEMHVtZE3q0ksXUZyexwQgGYXZlT5OQyUVlJ1KYzBJH6Y11EcBoiBBYAVRU4gJNWtilbSsRdtQdRrkGF4%2BlPJIGSE5XiiblgTX7eIiUvC2bv9mp4bhYxIaBoYgIZ2MSXiGi3splzre0RL26diPywl0GlNM2CtF8H%2F%2FHKt07rtV9caEGJXekc7PV24x9syKGaJ6Iiz1OEpsWxdygBfOvYpsOv8Nl2%2BtREqx%2FBBm0MbuZgqGEkHgvNIexXzOCs3mYJy6IBJi%2FBUbJhTeUHrErW%2BkZlMGdZSWHrn6OPn3g1nSQxUaAhCIIvN4J3pVX4w6q%2Ffb%2FoQ2qFyu6EoPNwRAvaACdOoY1qNCa265kfD30DKF4xpzAlcuKCyqAO9THd7Ws6l4wcVS1S8d8324QX6DqfdgxF3Iy5yYNr2u1Gao6e6kyBLCSRTWorhsx3DlnnW4x7E0Q0mLsxgz7Ex18fPBsVj3cXGblyQJodDgRYTLDPJhFynnQJMp4vv26CNkHItM6wrAXYW4glu08iHxWDSxoqPmAoZV5LV8GmOqzHn%2FiHfaDyMR3YF9JA520vdB63hGbN1CADPQTxeT08VYwwZSKvQY6pgGA2JVHwEqqkhpDmt7Im2OKDfj0HEdwu%2BV8m0sEpaM%2Fn8R%2BMDyvoHTbUhFFRyOW79fZEJZUC3HDFZcDQe%2F%2FwgL0Hl%2FBWs4pn5wjNukzmT4TfEJljs3cMWbgM9C%2FacBIFmlSWOaH6MazuKPq26l2JxZLi3jsKzT53x4VKC761szrC0NKCurA%2BUZhkkCAWLzgxERJKJaLHCRVclh%2BAwwdF5dv16q%2FW%2Ff5&X-Amz-Signature=721501b747bac2f6c0e4b18c95b8c80cd2ac7a532ba8ff198510736342929610&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5W2OYF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEQ%2BJKLM%2Bb7HB8TzlnzjO%2BaGgEG7vtkdxtVZ4%2BYMZg7XAiAucHtO4EQ7Qnfb0DTitZ7%2BNeFJ%2BYI9zIa%2Fg3Uo7oUWVSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMRXENOAYq4eTtYyQFKtwDq0OOb7vyKjW5f5RE6wBDufS%2FIeZHtupJz4sk1BfjWivl8GEMHVtZE3q0ksXUZyexwQgGYXZlT5OQyUVlJ1KYzBJH6Y11EcBoiBBYAVRU4gJNWtilbSsRdtQdRrkGF4%2BlPJIGSE5XiiblgTX7eIiUvC2bv9mp4bhYxIaBoYgIZ2MSXiGi3splzre0RL26diPywl0GlNM2CtF8H%2F%2FHKt07rtV9caEGJXekc7PV24x9syKGaJ6Iiz1OEpsWxdygBfOvYpsOv8Nl2%2BtREqx%2FBBm0MbuZgqGEkHgvNIexXzOCs3mYJy6IBJi%2FBUbJhTeUHrErW%2BkZlMGdZSWHrn6OPn3g1nSQxUaAhCIIvN4J3pVX4w6q%2Ffb%2FoQ2qFyu6EoPNwRAvaACdOoY1qNCa265kfD30DKF4xpzAlcuKCyqAO9THd7Ws6l4wcVS1S8d8324QX6DqfdgxF3Iy5yYNr2u1Gao6e6kyBLCSRTWorhsx3DlnnW4x7E0Q0mLsxgz7Ex18fPBsVj3cXGblyQJodDgRYTLDPJhFynnQJMp4vv26CNkHItM6wrAXYW4glu08iHxWDSxoqPmAoZV5LV8GmOqzHn%2FiHfaDyMR3YF9JA520vdB63hGbN1CADPQTxeT08VYwwZSKvQY6pgGA2JVHwEqqkhpDmt7Im2OKDfj0HEdwu%2BV8m0sEpaM%2Fn8R%2BMDyvoHTbUhFFRyOW79fZEJZUC3HDFZcDQe%2F%2FwgL0Hl%2FBWs4pn5wjNukzmT4TfEJljs3cMWbgM9C%2FacBIFmlSWOaH6MazuKPq26l2JxZLi3jsKzT53x4VKC761szrC0NKCurA%2BUZhkkCAWLzgxERJKJaLHCRVclh%2BAwwdF5dv16q%2FW%2Ff5&X-Amz-Signature=31fe27c742361ca19c15b9b49f81f52dabb2bd28158b0349054efb00e6b7dbde&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5W2OYF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEQ%2BJKLM%2Bb7HB8TzlnzjO%2BaGgEG7vtkdxtVZ4%2BYMZg7XAiAucHtO4EQ7Qnfb0DTitZ7%2BNeFJ%2BYI9zIa%2Fg3Uo7oUWVSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMRXENOAYq4eTtYyQFKtwDq0OOb7vyKjW5f5RE6wBDufS%2FIeZHtupJz4sk1BfjWivl8GEMHVtZE3q0ksXUZyexwQgGYXZlT5OQyUVlJ1KYzBJH6Y11EcBoiBBYAVRU4gJNWtilbSsRdtQdRrkGF4%2BlPJIGSE5XiiblgTX7eIiUvC2bv9mp4bhYxIaBoYgIZ2MSXiGi3splzre0RL26diPywl0GlNM2CtF8H%2F%2FHKt07rtV9caEGJXekc7PV24x9syKGaJ6Iiz1OEpsWxdygBfOvYpsOv8Nl2%2BtREqx%2FBBm0MbuZgqGEkHgvNIexXzOCs3mYJy6IBJi%2FBUbJhTeUHrErW%2BkZlMGdZSWHrn6OPn3g1nSQxUaAhCIIvN4J3pVX4w6q%2Ffb%2FoQ2qFyu6EoPNwRAvaACdOoY1qNCa265kfD30DKF4xpzAlcuKCyqAO9THd7Ws6l4wcVS1S8d8324QX6DqfdgxF3Iy5yYNr2u1Gao6e6kyBLCSRTWorhsx3DlnnW4x7E0Q0mLsxgz7Ex18fPBsVj3cXGblyQJodDgRYTLDPJhFynnQJMp4vv26CNkHItM6wrAXYW4glu08iHxWDSxoqPmAoZV5LV8GmOqzHn%2FiHfaDyMR3YF9JA520vdB63hGbN1CADPQTxeT08VYwwZSKvQY6pgGA2JVHwEqqkhpDmt7Im2OKDfj0HEdwu%2BV8m0sEpaM%2Fn8R%2BMDyvoHTbUhFFRyOW79fZEJZUC3HDFZcDQe%2F%2FwgL0Hl%2FBWs4pn5wjNukzmT4TfEJljs3cMWbgM9C%2FacBIFmlSWOaH6MazuKPq26l2JxZLi3jsKzT53x4VKC761szrC0NKCurA%2BUZhkkCAWLzgxERJKJaLHCRVclh%2BAwwdF5dv16q%2FW%2Ff5&X-Amz-Signature=39fb01befee6e9910e7ea46881b035a584634d0ff54f59dbb1fbf1df028153bf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666W5AVO6R%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIEetjS6WQeE5RG8k8Jco64hSr%2BJcygZ5Duce0Wi%2BhzEDAiEAtR8H7QiFX19AE0twLSCipM1Lic3MOKZPu8dcAKGgZR8q%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDMW%2FeEY79TDvyAMnwSrcA976MCkfn%2Bf3BiQN%2BE6%2FHQc5kG3JE%2B0dr2jW6QWekQA%2FKoEp6I0UEvMeQvfQxAorxGWt1Nwp03rgkoCEYV0Ar2N0IqSvRsF1t%2FwuPhx%2BTomkpn0zD6S0HsWjaLQX9s4ecKB7q2hWTFA12EEMqf0FdV4ZHoQ2tQERh4BwfzaaocBLnfmEUgo5Isx7VAmL5AY%2BE9xJRjy8lJxzc2%2B%2FFstFWSV%2B3ECQoewS8JX1U5m7dKa8aQZoh%2B1jfT46Rhy7NNhTbrQmMTNbHKiMwx1zPxoQpcfTQfBwX67U3DskTg3n20WB2nGw2xeDVvVwaAYqdlTBW8NFZsmgRrT%2B4f0JEnO0oCxwOCplmo6IqDtR%2FFR3JWfiF20VSdwnCy%2FWd2XPTGWPYGPwlFKq4mGv1PPndXqOY5sJtKEQ7KcKCPWuEdw8yPj2mSr%2BNLccqZavYkJ2PAfWtzO6NCdKbfoQCGnP%2BbKd05RS%2BjVHVRcqtWMvYTPyT3sk2X3%2Bnls5qgPKYjTBnKntQoZqeTUvvFjqQB4lFI494kPc4y7U7k%2BqGKGzIK7jMEXK8plK4y7dk2silK1VkB9nCk7uLHNe%2FcaqOA7tav1jXYQby0csX%2FSNtEHj%2FYKtWKMwmE6%2FtJC0Pzvx1aMIMN%2BUir0GOqUBlnJoPZb9ZJ3i0epauHzF18pGUKGz4Kbregtreqc8uoaGMX0KcyZ2A7l20D5yJTf%2BrsSDU0MRoTLxl3O69BUNHkFDYotY%2F0tGqnPjtNoYY8MFsENXOMFbWrfSD1PqTY6Ai807IT%2F%2B1sZpV%2BBtoXU1x2Yo5rYsVEun%2Bsu%2B2G9DAONdWoOtlRSaohFxhNny5QOeO1B260FgAgTg9W4eqr7xx1qTuxtc&X-Amz-Signature=e62f92454594e4cba05fcc23620ffa00698f195d13499d4c52c946b6fa44bb15&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665RZ3ELJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDPHyM49YxJ%2BlaDJLeWH4f3XSC%2FzeBlIWdDHe4BD0FawAIgTmtzLWwDXsODxZhxW8YDEGRVd3Dw%2FkFV5VORSWCidoIq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDMadwua0a%2Fvsd%2BJm6SrcAz41pOzvtjp9LiO%2FjO3cHsI0S%2FohSkQaYlNrFxRzM8Sfdgtcmr7BDIgykfctvsQovLKFNOZmzUBWPxQIfL2%2Fz8X5QbKwuoX9ZeIarBBzaF5YUkFROjrGk4M66fVz74ribSa9zrckfR4llihQKer4ZsGNbulYLnSZ0qtQobavW6NQ5QqMYQ7Y3lwUI5%2B4pS90TRamf1riAXXmFCMLHKMqSkWfvzFu5yNNVi5NxeNIJ%2BLJACSxK3P%2BjXhQWKeFH%2F8CrJONC82k5vVQBhR7gxQPxpDm8tIQUQB6voJFYuRhmtcupIzEK6RoOmThLXS2dWYcWoOPd1Cd%2Bbpslu7DPW4xIbOylWEPPFFbGVR51uRr6uRV5viPzS6wQVl12eBdHdw1tk%2BKSqz6WyZClWa80qtCPY0pdmTu5yfytrKhFzhkw%2BOXNAw%2BTDhqf588i6qA2TZCQKMiK3%2FkdHm4zla389SffGaaToY%2FBCT3HA5mXrxU3a7lLmyN%2Fp7NpfbVb0tlzkmYRgczn15%2B4SK%2B2%2FQnAiHzSPnSlfjh5YmjWHqngI%2BKMT5hPwHxVe0w%2F7XxTD3qWC0zC9cGMgyqSgn0EeWxA3E3ouH2S7xgUMKZjOlNgMyBPxbJ2LFLXodQUo2Jxt%2FmMM6Uir0GOqUBF1t9z553c0DrydqRL8TUzyR6kPrabtWMUFN71qQQr7ENZ9Rx1oGx6d2bPA5EDnU8ste0abynHE74uerdXRbB2ufDfwToNHIr3sMGShCihCwR%2Fb%2FrfTDcGS%2BgcAI7NyPjNqX5AWUtekL42UzV%2F4shD0SDhSaNhdVzDtQtCxseyq1C%2FfREzJf%2BOVDgzcDm4nofa9IHc6hlrfrGDNmGojdBdkOcj7te&X-Amz-Signature=8b3458a3a48a3af12d80ff5d38dec5f4ede3a7fe9d7721ad5e54e5b7386a0ac6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5W2OYF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEQ%2BJKLM%2Bb7HB8TzlnzjO%2BaGgEG7vtkdxtVZ4%2BYMZg7XAiAucHtO4EQ7Qnfb0DTitZ7%2BNeFJ%2BYI9zIa%2Fg3Uo7oUWVSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMRXENOAYq4eTtYyQFKtwDq0OOb7vyKjW5f5RE6wBDufS%2FIeZHtupJz4sk1BfjWivl8GEMHVtZE3q0ksXUZyexwQgGYXZlT5OQyUVlJ1KYzBJH6Y11EcBoiBBYAVRU4gJNWtilbSsRdtQdRrkGF4%2BlPJIGSE5XiiblgTX7eIiUvC2bv9mp4bhYxIaBoYgIZ2MSXiGi3splzre0RL26diPywl0GlNM2CtF8H%2F%2FHKt07rtV9caEGJXekc7PV24x9syKGaJ6Iiz1OEpsWxdygBfOvYpsOv8Nl2%2BtREqx%2FBBm0MbuZgqGEkHgvNIexXzOCs3mYJy6IBJi%2FBUbJhTeUHrErW%2BkZlMGdZSWHrn6OPn3g1nSQxUaAhCIIvN4J3pVX4w6q%2Ffb%2FoQ2qFyu6EoPNwRAvaACdOoY1qNCa265kfD30DKF4xpzAlcuKCyqAO9THd7Ws6l4wcVS1S8d8324QX6DqfdgxF3Iy5yYNr2u1Gao6e6kyBLCSRTWorhsx3DlnnW4x7E0Q0mLsxgz7Ex18fPBsVj3cXGblyQJodDgRYTLDPJhFynnQJMp4vv26CNkHItM6wrAXYW4glu08iHxWDSxoqPmAoZV5LV8GmOqzHn%2FiHfaDyMR3YF9JA520vdB63hGbN1CADPQTxeT08VYwwZSKvQY6pgGA2JVHwEqqkhpDmt7Im2OKDfj0HEdwu%2BV8m0sEpaM%2Fn8R%2BMDyvoHTbUhFFRyOW79fZEJZUC3HDFZcDQe%2F%2FwgL0Hl%2FBWs4pn5wjNukzmT4TfEJljs3cMWbgM9C%2FacBIFmlSWOaH6MazuKPq26l2JxZLi3jsKzT53x4VKC761szrC0NKCurA%2BUZhkkCAWLzgxERJKJaLHCRVclh%2BAwwdF5dv16q%2FW%2Ff5&X-Amz-Signature=140bea28812bd050ab3b9d7829891066e67a2f5320c8f6b38d1d81d82c82f0a1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5W2OYF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEQ%2BJKLM%2Bb7HB8TzlnzjO%2BaGgEG7vtkdxtVZ4%2BYMZg7XAiAucHtO4EQ7Qnfb0DTitZ7%2BNeFJ%2BYI9zIa%2Fg3Uo7oUWVSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMRXENOAYq4eTtYyQFKtwDq0OOb7vyKjW5f5RE6wBDufS%2FIeZHtupJz4sk1BfjWivl8GEMHVtZE3q0ksXUZyexwQgGYXZlT5OQyUVlJ1KYzBJH6Y11EcBoiBBYAVRU4gJNWtilbSsRdtQdRrkGF4%2BlPJIGSE5XiiblgTX7eIiUvC2bv9mp4bhYxIaBoYgIZ2MSXiGi3splzre0RL26diPywl0GlNM2CtF8H%2F%2FHKt07rtV9caEGJXekc7PV24x9syKGaJ6Iiz1OEpsWxdygBfOvYpsOv8Nl2%2BtREqx%2FBBm0MbuZgqGEkHgvNIexXzOCs3mYJy6IBJi%2FBUbJhTeUHrErW%2BkZlMGdZSWHrn6OPn3g1nSQxUaAhCIIvN4J3pVX4w6q%2Ffb%2FoQ2qFyu6EoPNwRAvaACdOoY1qNCa265kfD30DKF4xpzAlcuKCyqAO9THd7Ws6l4wcVS1S8d8324QX6DqfdgxF3Iy5yYNr2u1Gao6e6kyBLCSRTWorhsx3DlnnW4x7E0Q0mLsxgz7Ex18fPBsVj3cXGblyQJodDgRYTLDPJhFynnQJMp4vv26CNkHItM6wrAXYW4glu08iHxWDSxoqPmAoZV5LV8GmOqzHn%2FiHfaDyMR3YF9JA520vdB63hGbN1CADPQTxeT08VYwwZSKvQY6pgGA2JVHwEqqkhpDmt7Im2OKDfj0HEdwu%2BV8m0sEpaM%2Fn8R%2BMDyvoHTbUhFFRyOW79fZEJZUC3HDFZcDQe%2F%2FwgL0Hl%2FBWs4pn5wjNukzmT4TfEJljs3cMWbgM9C%2FacBIFmlSWOaH6MazuKPq26l2JxZLi3jsKzT53x4VKC761szrC0NKCurA%2BUZhkkCAWLzgxERJKJaLHCRVclh%2BAwwdF5dv16q%2FW%2Ff5&X-Amz-Signature=05e98eac606910c71154ec78121c19da11437ed8b92d1ed6c42cd110906adf3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI5W2OYF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEQ%2BJKLM%2Bb7HB8TzlnzjO%2BaGgEG7vtkdxtVZ4%2BYMZg7XAiAucHtO4EQ7Qnfb0DTitZ7%2BNeFJ%2BYI9zIa%2Fg3Uo7oUWVSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMRXENOAYq4eTtYyQFKtwDq0OOb7vyKjW5f5RE6wBDufS%2FIeZHtupJz4sk1BfjWivl8GEMHVtZE3q0ksXUZyexwQgGYXZlT5OQyUVlJ1KYzBJH6Y11EcBoiBBYAVRU4gJNWtilbSsRdtQdRrkGF4%2BlPJIGSE5XiiblgTX7eIiUvC2bv9mp4bhYxIaBoYgIZ2MSXiGi3splzre0RL26diPywl0GlNM2CtF8H%2F%2FHKt07rtV9caEGJXekc7PV24x9syKGaJ6Iiz1OEpsWxdygBfOvYpsOv8Nl2%2BtREqx%2FBBm0MbuZgqGEkHgvNIexXzOCs3mYJy6IBJi%2FBUbJhTeUHrErW%2BkZlMGdZSWHrn6OPn3g1nSQxUaAhCIIvN4J3pVX4w6q%2Ffb%2FoQ2qFyu6EoPNwRAvaACdOoY1qNCa265kfD30DKF4xpzAlcuKCyqAO9THd7Ws6l4wcVS1S8d8324QX6DqfdgxF3Iy5yYNr2u1Gao6e6kyBLCSRTWorhsx3DlnnW4x7E0Q0mLsxgz7Ex18fPBsVj3cXGblyQJodDgRYTLDPJhFynnQJMp4vv26CNkHItM6wrAXYW4glu08iHxWDSxoqPmAoZV5LV8GmOqzHn%2FiHfaDyMR3YF9JA520vdB63hGbN1CADPQTxeT08VYwwZSKvQY6pgGA2JVHwEqqkhpDmt7Im2OKDfj0HEdwu%2BV8m0sEpaM%2Fn8R%2BMDyvoHTbUhFFRyOW79fZEJZUC3HDFZcDQe%2F%2FwgL0Hl%2FBWs4pn5wjNukzmT4TfEJljs3cMWbgM9C%2FacBIFmlSWOaH6MazuKPq26l2JxZLi3jsKzT53x4VKC761szrC0NKCurA%2BUZhkkCAWLzgxERJKJaLHCRVclh%2BAwwdF5dv16q%2FW%2Ff5&X-Amz-Signature=36b1e675d28b008d9bc54a0fc5b655d43b4e4133c76912d6abe30584bdb42b45&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFPNOPNB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDHXk8xhbVvevWzFp%2FkX670Xf6lq6ORC%2Bp%2Bsg5hBBohfAIgbpF92%2BAINNFvApBr92ONvN%2B6NLld8D5%2BC9vsLG9a3hcq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDCF%2FzfFdkDjfFBBkYSrcAxXJUGsBuzaWhOBi9LpzMCF8xQklcCgs3Gr4oS8XTCd3hKRZjJRtJ%2FZg1OkXLOfSxaUQpVr5pd0qaB8vpQ%2FwFVtmOYHSjlOVRSD3VfHpv22Tx359yf2eJFPfPwJ43JFfRqiGJ1TN09zp7pAmMuguHa7K9aaCY7pCE5Wc7z8DlMh7KHyYGv1kDDDcbdZYQGw7lnyUYQn%2BvwggdkwlmVR6M5zmJjMwKgiZ2ZjODK9JraLMc3xh1PiFeAtKYDlIL%2FdwrjVmh7tatnLjEy3topMRuets0cIr8AaQ0dNRSQbG44S%2Bx9C3AMgk6xFqmSgPhP0MqPhlHJnKQL4zF6ua5Og%2Bb3GxScolMXmufD4DMe%2F77VjY%2BVCdjyheQM0vlSM4AHXstP%2Bz%2BLxRPFXgVaHnbfXpqoAbsT%2BFyA8kp72ZWOGOkAAtse3iRR6OAunPItynBzylE9JG5adaEhFkhCUXMaf16XlU%2FVYuvb6a6RaTy5nvc3P9NlQmW0Q%2BOg7WxfOpfMW3RVcJehaeVCmw70CAU0feY6WYsY8qK9j52iIuRqb2uH4GRvwAba6joeQ%2FlIb0OLIXlBowm%2FfTtxz7Tquo6tg%2BBfPWwUHhHngMj%2F8NcE%2FSnmIlhIBrH89e%2FufNWuroMOaTir0GOqUBBy4GraWuCBLVPKrDMBGn8MsQYDTkaZAp6YvSlrf91CfVbDovWBPPgGZD7fVqGwBGf5mKDn0MXeJd%2BCrHuSxDQSskCyMobVoxbHaXJsxZxhCgL6Iu%2F5oxDfQ%2F1GJKmO%2B%2FoF%2Br%2BEged04Zje387wnMtkcQTaSNooBu9yKMraFWiPniwGo1MMDi%2BOdJ%2Fn57R3qx%2F01LPY74Myt%2F%2FH%2Fe%2BRfOjElJ1Def&X-Amz-Signature=df8899e3aad92cd3a67e944ee36278f7b59123118039876e80cccd3cc9928217&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CNV5IJG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCH%2B0L5dFyv76MJJ2IIwv6CllhqSHuZAizf9VEKeyp49QIhAJ2VBxRgwKl%2BKvosRPZElcg0BTopnlv3TwdPgBmmIR9aKv8DCDcQABoMNjM3NDIzMTgzODA1IgyAL3S%2FkfsR10E2TUAq3AMmuPou%2BkVd0z9G6%2FehMt8ob7FrC4E8ex23BcQcVAO59NzYuHXO1RfSy7YUICIEsS62FSNWsKtVi7X%2BlCZ8WLL49UfUtQwmoLuzY1%2BLLCfwBAyjIz5pxgBgS7ypjWppOVgk05Kz7pK1IoazxKlIqagcXEOCIXaHKAQpmOQHzzfr0mBvhYE0w1gj61UjWM%2FnABRB9yG5MynzA7lYHSMEmuCwxrEoGAa2moSTa38lWQXv%2F9JMeXPR8fXsm%2FdCRVeZc31yjrxsagduvOc61fZYqGLJ3D%2F04KgrPUGdmrsfoSTLARXMIE1Q82IO0fypegsGr%2FrjsavY1dyPLiRv6YOi2J2hlbZmTbrqQchulsegWuLW6DY7t%2BcDO%2BoGM3yOHP6Ha1sUwy8AzToHDqeaLFN7iw4c6HMnLSm55N53H7OTpg420jXuWkmJLJF6byRahUOVfpK0FQmQ1vc9J2kCxt2K%2Fxf3jVJhCKi0KeZk95ldtEUY86%2FBjJHhHfOqF2hdiVMYtKs1l7EoHx02SH9rKI26LO1QxIW1jjG1eSU5eeRqgxPAg%2FgoFMZLTIvSGqQvnq8pPAbiVX0knRMeF9yIOGribi7zgZNLFzDaX6taeySom%2B6qRi7dU35Bg19s39h2SDCwlYq9BjqkAcU1F1cwA52YIEjGC%2BIlECEL1rowQe1Ug82W%2FpB5BhzQre07CO4%2FbDSyRN3b7V88jcLnEKX1Jk%2B5jhpHeyzjGimJyJXFoziSufIbZxnOph8jtt9ZJ3qOMrzLC7V7hQTnpL7r%2BtlEms2VNvIhrHDrQsjXQGlEO3Wdd916g0WpS%2Bgaw5B4WRM57GHg%2F%2Fwy5uUJ7ZeWEk%2F1fYy%2BJ9cCTmE3%2Bb8nbgz%2F&X-Amz-Signature=df903f91534e3d9c34cd94f743e029f4451f7c2474bbb1bd7493cfc36efddb6d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YADWWSTJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIEE%2Bb%2BiMcsuA7JE0oaJ7jxZG91%2F4B%2FTNVUCp4RPXn3s0AiBJgcQdxLl3YJLehV3p1Mk1QZjBxOtcVhns9jl9%2F%2BZqUir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMO6Hl%2B6HLwpFPZ%2FmSKtwDe4Vc2zquJNmL0TymWim8sEhyOkCCmh3vLa%2BnQRr6cChJF1XMBtdy9Td%2B%2BWtOPMEtp55YcBXkPL0NJqqvPQB%2FFhRJwXhEUkglBqdGSFDBpe4wtnq4b4seIFuNehV91L1rSptCKPcEikBPHaigW0d1ik%2BGx4Ti3Doeqw2NMNGm%2F8LPanrtbMSC%2Fml%2FiD8TNWVc%2BvvIitLx7G29cZ8vkhCf32ESzmFihFQXIpbT3x4W5tV7AhzuKsEXD3IU7baOWI%2BK2yuYrteyY3Me1NFsFJ%2FxgxdQIRiKv%2F6hmJU2qCQu39mNtw0nb0%2B5eCtUCR52QrE7awNGqLP%2BW46mREraBT8yDkRVwnrM8AgJKEnOoHcfKUXr21Oo5FCh%2BnO7dWNIq49FXi1ylgPDP9PdDqJzS1hLMLfomvDlM9RkmtWHJiFuwVc6c4bmGreHXs7bpV6ED2m7FydfGkkilTTDw4jiHSgfswWgTE909EVX4dAYmHC6Hzj4FzrJIsmazC13t%2B%2BHTserDeVVpcXPQxIdf9eByOSMf65s%2BW7nM9qZlahw2X2xdOumhyLmMkkLOrjxYtd0DbWYX8MaTOu0DxVfLlCJA%2BCkFXhezgY98jcC36zOG0nfO6qhPKvjuBplbl6vffEwtpSKvQY6pgGI2fIOYNOPLTx7V8fMwTB5w70yk9G1UueyqazLRGgZJZ6W%2BBswiqaTyr5afRE%2Bh%2BHQBs5otufZ5cTr6h7U1Lr44bs6mmXZ%2F%2BPG5PB9jqdL7Te%2BcI2v94o57IcPhaMFuu2%2FqONOJx4EqmrfOZ81kb5UFIpPG7%2FfaTcTzQI42dJ5H1xX9GoHwnoMuCWim2HCdDeQN%2FGaRQSCAPxlGapwH9TVLc%2BCUz4w&X-Amz-Signature=e71760bf9f0a3b1924f055cadd38373299b325380ccb7016ded2a1e785edd66d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJDQBAIJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCj0RZik1e3NrFGnHu%2FlSV85kBe0QBgpt6KE66Q3C8XywIhAMqRMGGf%2FJvpD90ooKoT79s7BDrLlTxlQ8rYnAlgop1LKv8DCDcQABoMNjM3NDIzMTgzODA1IgwY5zsxgOHupqz4934q3ANAdzjpLAnAwIGp2pv5lwxUHtfB5D4nmR2zavpOyQeTHH8z1dN%2BnOunMlWMyICZJvaNk%2FpbWodx8v1XOaVRu4B3NXBTu0K8iJ2ncppGykvEnM5RNC6vf49jidsysU7l6tM1wG7cLqioliTIHhBO5UClzyVCs6F2Pi49DWj3pC%2Bgif%2F7lpMV8qBgyaeyD%2BMzz%2FFfl7NiJlPQghbSi7dkWg4Wiob1jqFjU2AbyZZ0qthcyH2v7fCJ7rMiZEtbNhwqcVn3KGGcBkjkImfeqGZotARXerYNU%2F%2Fd2hEEiwhQsd01baSQTFM%2Bxf%2FXXwd0j5xU%2BfCcWN1viIzIlAtkalmTpPV1wfwqObl8L4GyZZfYZ6Jt5vhZiyN0NJw54X90B6gzQuAw1dF6OYGQTIh9cQSf1spVgsqlapfvhotADM9wl9djzhdH1tWc5YUaoCiFS4VIbecsr3jC47ZMCcbKfMREn64yXOtAhJcSJpW6lzSe%2FWi0Efg9F4hTpX0YL1s9%2BQtd1E0yaYggRInEbZQiv3viTRT4goLshSecTJbEDz7BTB%2BR1GV4vhUWr1TbmfgWgzcrXFaxfiLOEz2oQ1w%2BOfbMsd6h6NMeCDPJnwTPWnpyRDrLELe49DKdhxQWJUXivDCdlIq9BjqkAaM2V%2FFBtgawXfmd7cYcP8zCuYu9U%2Bky2%2FA%2BfjwVUmWIMV9sDWMzEvy4X7G6t6V2mMht%2Fh3dYuRgu7poZTyFWtDbvb8HSMio1KXgk%2FhxwMnwCfVHdVAjh8PJqATSdD1%2FTYGgdsNxm%2Fy4Ce29%2F8BpenK269dq4uOu4PbjkQHl7PPA3z0pr27D%2FUcSJ7oUqCDih3U8DpqaMf2YqNk7kWZwGBwYeV%2BN&X-Amz-Signature=ae36ded553f4d3a2ea7d147f874649ab7503b189ba3022b5ac56e63893b3f048&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJDQBAIJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCj0RZik1e3NrFGnHu%2FlSV85kBe0QBgpt6KE66Q3C8XywIhAMqRMGGf%2FJvpD90ooKoT79s7BDrLlTxlQ8rYnAlgop1LKv8DCDcQABoMNjM3NDIzMTgzODA1IgwY5zsxgOHupqz4934q3ANAdzjpLAnAwIGp2pv5lwxUHtfB5D4nmR2zavpOyQeTHH8z1dN%2BnOunMlWMyICZJvaNk%2FpbWodx8v1XOaVRu4B3NXBTu0K8iJ2ncppGykvEnM5RNC6vf49jidsysU7l6tM1wG7cLqioliTIHhBO5UClzyVCs6F2Pi49DWj3pC%2Bgif%2F7lpMV8qBgyaeyD%2BMzz%2FFfl7NiJlPQghbSi7dkWg4Wiob1jqFjU2AbyZZ0qthcyH2v7fCJ7rMiZEtbNhwqcVn3KGGcBkjkImfeqGZotARXerYNU%2F%2Fd2hEEiwhQsd01baSQTFM%2Bxf%2FXXwd0j5xU%2BfCcWN1viIzIlAtkalmTpPV1wfwqObl8L4GyZZfYZ6Jt5vhZiyN0NJw54X90B6gzQuAw1dF6OYGQTIh9cQSf1spVgsqlapfvhotADM9wl9djzhdH1tWc5YUaoCiFS4VIbecsr3jC47ZMCcbKfMREn64yXOtAhJcSJpW6lzSe%2FWi0Efg9F4hTpX0YL1s9%2BQtd1E0yaYggRInEbZQiv3viTRT4goLshSecTJbEDz7BTB%2BR1GV4vhUWr1TbmfgWgzcrXFaxfiLOEz2oQ1w%2BOfbMsd6h6NMeCDPJnwTPWnpyRDrLELe49DKdhxQWJUXivDCdlIq9BjqkAaM2V%2FFBtgawXfmd7cYcP8zCuYu9U%2Bky2%2FA%2BfjwVUmWIMV9sDWMzEvy4X7G6t6V2mMht%2Fh3dYuRgu7poZTyFWtDbvb8HSMio1KXgk%2FhxwMnwCfVHdVAjh8PJqATSdD1%2FTYGgdsNxm%2Fy4Ce29%2F8BpenK269dq4uOu4PbjkQHl7PPA3z0pr27D%2FUcSJ7oUqCDih3U8DpqaMf2YqNk7kWZwGBwYeV%2BN&X-Amz-Signature=01a6c395fcf5d77725e42d25dc257c307c6ba3aa45c95b7b9438f6f0736fbe3e&X-Amz-SignedHeaders=host&x-id=GetObject)

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
