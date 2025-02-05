

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOQJUQFR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIB69O1y4sob%2FD684Yb0gZh9ko%2BWAPz9yku9m0ZswNEOUAiEA4HvLOYXkYR2lNGuhqrkTfUkwBQI4QCoW9XmGDwKU4EAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFIEYFmXUAAjyekbYircAzqNViOSm7%2Ff0mmcKed618lrO%2BMgkfXPxWxdHFhE78KTXH5hB41O2NUSKkCjMqXnoBnq9eTGHS8oq99ZT1mZ5RXw%2FaHxZlTperQO6ow%2Fzn59CWPhRW7RGkdZ%2BFTWXRAtu0yh9vd92UaY%2BDmDDT8uULxLkGsLsYRwcrMNBM1nf1NLI1lJvJCHAcJm6s9vfzYTMIlgaT7spPuYXKNwMnchUXpTkbWUvsURc7NzkDyej%2BBWwf3ScktQElE6nTyYQoKyj%2FMZa4ngtBMij2lbR1%2F3f86TPAEX4PRyxuAHLQv1NNHjT634C5e0ST%2FcKD74VZgdrnN8UOU43sA7RZEx5Sw0X58Oi2wTgEoYwThSFxUveI%2FePx4AY74CR7VjY78dOCGywaw%2FsghbcC6GvRb63ZXANwEUtExFvGN9lFFNvAd%2BAF%2F5pVY%2FNpNMv9c7KeWfdlr1XH%2BvVdXW8jemunjO4IjyApbyGKUpj6BEJJl5JLiSbZrGC6JuVh04pvUQCLoVUPWplO%2B5V35kfFsBhrkRBAvxG9oZNrTxTuaymNwzigECONYTNK8lSGRd0G4zuXTdwL4QNwW1popm0RSdhbqlp9WgROy5wBTckHNNHagNHjm8jJJAVTu2Hm%2FdfrJPWMk4MOD5i70GOqUB3jNgghgX9K9eznSD%2BjbSqpFDbt%2Ft0mR6SxCY8VCTTtNrK1LTwyXmwGkXL11xl%2FfsxawBUkxe4T8Mf1wuK7jLdxrXb1g6Au9PpbXjFoOeXpEkV0sFmWOp09lmQAkgw%2FwROp07d8wbe1LZuSQEg5NENKH%2BKCCwg6HFRIUqUMjeIRGg3a%2F2w3xd4qBpXPeQYyrOROjdw6qrjnCYyesJofZOtkrQWmYx&X-Amz-Signature=054e36dd5b1dc82a1d719573da9c4ce54e1c08d75ba63b642f0a229434afbb86&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOQJUQFR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIB69O1y4sob%2FD684Yb0gZh9ko%2BWAPz9yku9m0ZswNEOUAiEA4HvLOYXkYR2lNGuhqrkTfUkwBQI4QCoW9XmGDwKU4EAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFIEYFmXUAAjyekbYircAzqNViOSm7%2Ff0mmcKed618lrO%2BMgkfXPxWxdHFhE78KTXH5hB41O2NUSKkCjMqXnoBnq9eTGHS8oq99ZT1mZ5RXw%2FaHxZlTperQO6ow%2Fzn59CWPhRW7RGkdZ%2BFTWXRAtu0yh9vd92UaY%2BDmDDT8uULxLkGsLsYRwcrMNBM1nf1NLI1lJvJCHAcJm6s9vfzYTMIlgaT7spPuYXKNwMnchUXpTkbWUvsURc7NzkDyej%2BBWwf3ScktQElE6nTyYQoKyj%2FMZa4ngtBMij2lbR1%2F3f86TPAEX4PRyxuAHLQv1NNHjT634C5e0ST%2FcKD74VZgdrnN8UOU43sA7RZEx5Sw0X58Oi2wTgEoYwThSFxUveI%2FePx4AY74CR7VjY78dOCGywaw%2FsghbcC6GvRb63ZXANwEUtExFvGN9lFFNvAd%2BAF%2F5pVY%2FNpNMv9c7KeWfdlr1XH%2BvVdXW8jemunjO4IjyApbyGKUpj6BEJJl5JLiSbZrGC6JuVh04pvUQCLoVUPWplO%2B5V35kfFsBhrkRBAvxG9oZNrTxTuaymNwzigECONYTNK8lSGRd0G4zuXTdwL4QNwW1popm0RSdhbqlp9WgROy5wBTckHNNHagNHjm8jJJAVTu2Hm%2FdfrJPWMk4MOD5i70GOqUB3jNgghgX9K9eznSD%2BjbSqpFDbt%2Ft0mR6SxCY8VCTTtNrK1LTwyXmwGkXL11xl%2FfsxawBUkxe4T8Mf1wuK7jLdxrXb1g6Au9PpbXjFoOeXpEkV0sFmWOp09lmQAkgw%2FwROp07d8wbe1LZuSQEg5NENKH%2BKCCwg6HFRIUqUMjeIRGg3a%2F2w3xd4qBpXPeQYyrOROjdw6qrjnCYyesJofZOtkrQWmYx&X-Amz-Signature=2e3627e7b28c2e08936cef2e3c7b6cf07eb34e5781e57ea5469342c7946e93a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOQJUQFR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIB69O1y4sob%2FD684Yb0gZh9ko%2BWAPz9yku9m0ZswNEOUAiEA4HvLOYXkYR2lNGuhqrkTfUkwBQI4QCoW9XmGDwKU4EAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFIEYFmXUAAjyekbYircAzqNViOSm7%2Ff0mmcKed618lrO%2BMgkfXPxWxdHFhE78KTXH5hB41O2NUSKkCjMqXnoBnq9eTGHS8oq99ZT1mZ5RXw%2FaHxZlTperQO6ow%2Fzn59CWPhRW7RGkdZ%2BFTWXRAtu0yh9vd92UaY%2BDmDDT8uULxLkGsLsYRwcrMNBM1nf1NLI1lJvJCHAcJm6s9vfzYTMIlgaT7spPuYXKNwMnchUXpTkbWUvsURc7NzkDyej%2BBWwf3ScktQElE6nTyYQoKyj%2FMZa4ngtBMij2lbR1%2F3f86TPAEX4PRyxuAHLQv1NNHjT634C5e0ST%2FcKD74VZgdrnN8UOU43sA7RZEx5Sw0X58Oi2wTgEoYwThSFxUveI%2FePx4AY74CR7VjY78dOCGywaw%2FsghbcC6GvRb63ZXANwEUtExFvGN9lFFNvAd%2BAF%2F5pVY%2FNpNMv9c7KeWfdlr1XH%2BvVdXW8jemunjO4IjyApbyGKUpj6BEJJl5JLiSbZrGC6JuVh04pvUQCLoVUPWplO%2B5V35kfFsBhrkRBAvxG9oZNrTxTuaymNwzigECONYTNK8lSGRd0G4zuXTdwL4QNwW1popm0RSdhbqlp9WgROy5wBTckHNNHagNHjm8jJJAVTu2Hm%2FdfrJPWMk4MOD5i70GOqUB3jNgghgX9K9eznSD%2BjbSqpFDbt%2Ft0mR6SxCY8VCTTtNrK1LTwyXmwGkXL11xl%2FfsxawBUkxe4T8Mf1wuK7jLdxrXb1g6Au9PpbXjFoOeXpEkV0sFmWOp09lmQAkgw%2FwROp07d8wbe1LZuSQEg5NENKH%2BKCCwg6HFRIUqUMjeIRGg3a%2F2w3xd4qBpXPeQYyrOROjdw6qrjnCYyesJofZOtkrQWmYx&X-Amz-Signature=90cd4f2463718dd773e5950506c6bf1828da2f5d8d557f638c6d43b5dc750feb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUU5QVK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIAHW6HLc3kNPK7vVxRe0YIubYyrmXuSM%2FzJSBquYrFl7AiAmbBgkyfJtpR%2FEYeHa%2F7KnsQudcaAbEP5x%2FTgH4jun6Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMV32jKTKSERbJ2sR%2BKtwDUyMkhmD9b6MXYWSH0Hc%2BYCz9b5%2FNPpYLU9xuTYxJm%2FvM84khJXz0kLwyvgNJYPN%2BxwfcTDNMuMeF0uvoAqgXZZW0AZ7UG236eNoaNT0K2krBdW6olemLJij7FlqC9MaMInomHG61cAr5%2Bc1Uo1c2XsNfl3Vs%2F7Gyf96ZtB0LGudiF%2BHw5gXJPK%2FRX4McfCTUninmdsdDstdIMLe8HNZ6LLLzoNpkgE%2FTHiTJm6oRBIXh9vL9LQeevPyV4%2B0EMiy6ZgV57UPipyHshaLJmGILWIggtqRUX3d24Zi0xKMeJPo41Gl%2F3u0blxOV2xqFxBNXyj5iwk%2BY3cy3vm9E5PA8gwLII0lsHXQwDgi%2BQqLgDEKO3RLkU9H%2BW1ngY5f9njOSyvu3hYbBsrv59CWn8IT6T80HN8IFJFVrGfJGn4Iz84blg%2B1KaCY%2FfrKc5SEfBLJqGKbmsc9Ne6o1lUQdHNPJdjIghMJQpndIOZkjL7afsHX282JEuROiK4wsVmnma8MJ1g%2FoddSLUkN6xXGi8kxaVheheMBx2YtTrO%2B4ChYqKPF%2F2WXpJX671uZn3cD7Isniu55ow8EmgGxmV8JMSJh1IS8dWz1vfLQMRJLl4ABp8RHBGfIw5bWFScYY4WkwwfmLvQY6pgGcx4SkIoHGXoEeqiojLFNPyS12zLLiUWI6NTlhSRKF7c0Te3oV5GOEl9ICm%2FvXKvHEav8bM2NhfB%2ByR%2FDZaWdrwCiy9Nb6rtIstaB8ZZuyfxyPYOy1ZdhdHCj86bEGABUJfLZZDHvBDOqEhSMnI1rNxKeQRNHyCCeQC%2FMWKf9hhf%2BnhL5CybilTAJYD7vHgfOufyeYJb%2Fummc6NvXjhBCQm0pPqozD&X-Amz-Signature=aa74588128fc5df6a8cb8388a41bb941819caa80ccc01da5bbde1cdc1950a63c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUU5QVK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIAHW6HLc3kNPK7vVxRe0YIubYyrmXuSM%2FzJSBquYrFl7AiAmbBgkyfJtpR%2FEYeHa%2F7KnsQudcaAbEP5x%2FTgH4jun6Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMV32jKTKSERbJ2sR%2BKtwDUyMkhmD9b6MXYWSH0Hc%2BYCz9b5%2FNPpYLU9xuTYxJm%2FvM84khJXz0kLwyvgNJYPN%2BxwfcTDNMuMeF0uvoAqgXZZW0AZ7UG236eNoaNT0K2krBdW6olemLJij7FlqC9MaMInomHG61cAr5%2Bc1Uo1c2XsNfl3Vs%2F7Gyf96ZtB0LGudiF%2BHw5gXJPK%2FRX4McfCTUninmdsdDstdIMLe8HNZ6LLLzoNpkgE%2FTHiTJm6oRBIXh9vL9LQeevPyV4%2B0EMiy6ZgV57UPipyHshaLJmGILWIggtqRUX3d24Zi0xKMeJPo41Gl%2F3u0blxOV2xqFxBNXyj5iwk%2BY3cy3vm9E5PA8gwLII0lsHXQwDgi%2BQqLgDEKO3RLkU9H%2BW1ngY5f9njOSyvu3hYbBsrv59CWn8IT6T80HN8IFJFVrGfJGn4Iz84blg%2B1KaCY%2FfrKc5SEfBLJqGKbmsc9Ne6o1lUQdHNPJdjIghMJQpndIOZkjL7afsHX282JEuROiK4wsVmnma8MJ1g%2FoddSLUkN6xXGi8kxaVheheMBx2YtTrO%2B4ChYqKPF%2F2WXpJX671uZn3cD7Isniu55ow8EmgGxmV8JMSJh1IS8dWz1vfLQMRJLl4ABp8RHBGfIw5bWFScYY4WkwwfmLvQY6pgGcx4SkIoHGXoEeqiojLFNPyS12zLLiUWI6NTlhSRKF7c0Te3oV5GOEl9ICm%2FvXKvHEav8bM2NhfB%2ByR%2FDZaWdrwCiy9Nb6rtIstaB8ZZuyfxyPYOy1ZdhdHCj86bEGABUJfLZZDHvBDOqEhSMnI1rNxKeQRNHyCCeQC%2FMWKf9hhf%2BnhL5CybilTAJYD7vHgfOufyeYJb%2Fummc6NvXjhBCQm0pPqozD&X-Amz-Signature=559f89255ab3324f3898beea9ca429e2b4ff70120e4d09c8d53ae0b777d10976&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUU5QVK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIAHW6HLc3kNPK7vVxRe0YIubYyrmXuSM%2FzJSBquYrFl7AiAmbBgkyfJtpR%2FEYeHa%2F7KnsQudcaAbEP5x%2FTgH4jun6Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMV32jKTKSERbJ2sR%2BKtwDUyMkhmD9b6MXYWSH0Hc%2BYCz9b5%2FNPpYLU9xuTYxJm%2FvM84khJXz0kLwyvgNJYPN%2BxwfcTDNMuMeF0uvoAqgXZZW0AZ7UG236eNoaNT0K2krBdW6olemLJij7FlqC9MaMInomHG61cAr5%2Bc1Uo1c2XsNfl3Vs%2F7Gyf96ZtB0LGudiF%2BHw5gXJPK%2FRX4McfCTUninmdsdDstdIMLe8HNZ6LLLzoNpkgE%2FTHiTJm6oRBIXh9vL9LQeevPyV4%2B0EMiy6ZgV57UPipyHshaLJmGILWIggtqRUX3d24Zi0xKMeJPo41Gl%2F3u0blxOV2xqFxBNXyj5iwk%2BY3cy3vm9E5PA8gwLII0lsHXQwDgi%2BQqLgDEKO3RLkU9H%2BW1ngY5f9njOSyvu3hYbBsrv59CWn8IT6T80HN8IFJFVrGfJGn4Iz84blg%2B1KaCY%2FfrKc5SEfBLJqGKbmsc9Ne6o1lUQdHNPJdjIghMJQpndIOZkjL7afsHX282JEuROiK4wsVmnma8MJ1g%2FoddSLUkN6xXGi8kxaVheheMBx2YtTrO%2B4ChYqKPF%2F2WXpJX671uZn3cD7Isniu55ow8EmgGxmV8JMSJh1IS8dWz1vfLQMRJLl4ABp8RHBGfIw5bWFScYY4WkwwfmLvQY6pgGcx4SkIoHGXoEeqiojLFNPyS12zLLiUWI6NTlhSRKF7c0Te3oV5GOEl9ICm%2FvXKvHEav8bM2NhfB%2ByR%2FDZaWdrwCiy9Nb6rtIstaB8ZZuyfxyPYOy1ZdhdHCj86bEGABUJfLZZDHvBDOqEhSMnI1rNxKeQRNHyCCeQC%2FMWKf9hhf%2BnhL5CybilTAJYD7vHgfOufyeYJb%2Fummc6NvXjhBCQm0pPqozD&X-Amz-Signature=e12e9a8c9416c7e9f2f84b4530f6dfabc2c69d82589b2b3c6f956ca0e0d88381&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUU5QVK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIAHW6HLc3kNPK7vVxRe0YIubYyrmXuSM%2FzJSBquYrFl7AiAmbBgkyfJtpR%2FEYeHa%2F7KnsQudcaAbEP5x%2FTgH4jun6Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMV32jKTKSERbJ2sR%2BKtwDUyMkhmD9b6MXYWSH0Hc%2BYCz9b5%2FNPpYLU9xuTYxJm%2FvM84khJXz0kLwyvgNJYPN%2BxwfcTDNMuMeF0uvoAqgXZZW0AZ7UG236eNoaNT0K2krBdW6olemLJij7FlqC9MaMInomHG61cAr5%2Bc1Uo1c2XsNfl3Vs%2F7Gyf96ZtB0LGudiF%2BHw5gXJPK%2FRX4McfCTUninmdsdDstdIMLe8HNZ6LLLzoNpkgE%2FTHiTJm6oRBIXh9vL9LQeevPyV4%2B0EMiy6ZgV57UPipyHshaLJmGILWIggtqRUX3d24Zi0xKMeJPo41Gl%2F3u0blxOV2xqFxBNXyj5iwk%2BY3cy3vm9E5PA8gwLII0lsHXQwDgi%2BQqLgDEKO3RLkU9H%2BW1ngY5f9njOSyvu3hYbBsrv59CWn8IT6T80HN8IFJFVrGfJGn4Iz84blg%2B1KaCY%2FfrKc5SEfBLJqGKbmsc9Ne6o1lUQdHNPJdjIghMJQpndIOZkjL7afsHX282JEuROiK4wsVmnma8MJ1g%2FoddSLUkN6xXGi8kxaVheheMBx2YtTrO%2B4ChYqKPF%2F2WXpJX671uZn3cD7Isniu55ow8EmgGxmV8JMSJh1IS8dWz1vfLQMRJLl4ABp8RHBGfIw5bWFScYY4WkwwfmLvQY6pgGcx4SkIoHGXoEeqiojLFNPyS12zLLiUWI6NTlhSRKF7c0Te3oV5GOEl9ICm%2FvXKvHEav8bM2NhfB%2ByR%2FDZaWdrwCiy9Nb6rtIstaB8ZZuyfxyPYOy1ZdhdHCj86bEGABUJfLZZDHvBDOqEhSMnI1rNxKeQRNHyCCeQC%2FMWKf9hhf%2BnhL5CybilTAJYD7vHgfOufyeYJb%2Fummc6NvXjhBCQm0pPqozD&X-Amz-Signature=3984616616e29f83786f74437a087bad4ffa148f5ab812042b64a458b5a54a3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUU5QVK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIAHW6HLc3kNPK7vVxRe0YIubYyrmXuSM%2FzJSBquYrFl7AiAmbBgkyfJtpR%2FEYeHa%2F7KnsQudcaAbEP5x%2FTgH4jun6Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMV32jKTKSERbJ2sR%2BKtwDUyMkhmD9b6MXYWSH0Hc%2BYCz9b5%2FNPpYLU9xuTYxJm%2FvM84khJXz0kLwyvgNJYPN%2BxwfcTDNMuMeF0uvoAqgXZZW0AZ7UG236eNoaNT0K2krBdW6olemLJij7FlqC9MaMInomHG61cAr5%2Bc1Uo1c2XsNfl3Vs%2F7Gyf96ZtB0LGudiF%2BHw5gXJPK%2FRX4McfCTUninmdsdDstdIMLe8HNZ6LLLzoNpkgE%2FTHiTJm6oRBIXh9vL9LQeevPyV4%2B0EMiy6ZgV57UPipyHshaLJmGILWIggtqRUX3d24Zi0xKMeJPo41Gl%2F3u0blxOV2xqFxBNXyj5iwk%2BY3cy3vm9E5PA8gwLII0lsHXQwDgi%2BQqLgDEKO3RLkU9H%2BW1ngY5f9njOSyvu3hYbBsrv59CWn8IT6T80HN8IFJFVrGfJGn4Iz84blg%2B1KaCY%2FfrKc5SEfBLJqGKbmsc9Ne6o1lUQdHNPJdjIghMJQpndIOZkjL7afsHX282JEuROiK4wsVmnma8MJ1g%2FoddSLUkN6xXGi8kxaVheheMBx2YtTrO%2B4ChYqKPF%2F2WXpJX671uZn3cD7Isniu55ow8EmgGxmV8JMSJh1IS8dWz1vfLQMRJLl4ABp8RHBGfIw5bWFScYY4WkwwfmLvQY6pgGcx4SkIoHGXoEeqiojLFNPyS12zLLiUWI6NTlhSRKF7c0Te3oV5GOEl9ICm%2FvXKvHEav8bM2NhfB%2ByR%2FDZaWdrwCiy9Nb6rtIstaB8ZZuyfxyPYOy1ZdhdHCj86bEGABUJfLZZDHvBDOqEhSMnI1rNxKeQRNHyCCeQC%2FMWKf9hhf%2BnhL5CybilTAJYD7vHgfOufyeYJb%2Fummc6NvXjhBCQm0pPqozD&X-Amz-Signature=507a860d26389decdaf22bf6a2be8222d81a461f2824512da8e9ea19ac1129b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUU5QVK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIAHW6HLc3kNPK7vVxRe0YIubYyrmXuSM%2FzJSBquYrFl7AiAmbBgkyfJtpR%2FEYeHa%2F7KnsQudcaAbEP5x%2FTgH4jun6Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMV32jKTKSERbJ2sR%2BKtwDUyMkhmD9b6MXYWSH0Hc%2BYCz9b5%2FNPpYLU9xuTYxJm%2FvM84khJXz0kLwyvgNJYPN%2BxwfcTDNMuMeF0uvoAqgXZZW0AZ7UG236eNoaNT0K2krBdW6olemLJij7FlqC9MaMInomHG61cAr5%2Bc1Uo1c2XsNfl3Vs%2F7Gyf96ZtB0LGudiF%2BHw5gXJPK%2FRX4McfCTUninmdsdDstdIMLe8HNZ6LLLzoNpkgE%2FTHiTJm6oRBIXh9vL9LQeevPyV4%2B0EMiy6ZgV57UPipyHshaLJmGILWIggtqRUX3d24Zi0xKMeJPo41Gl%2F3u0blxOV2xqFxBNXyj5iwk%2BY3cy3vm9E5PA8gwLII0lsHXQwDgi%2BQqLgDEKO3RLkU9H%2BW1ngY5f9njOSyvu3hYbBsrv59CWn8IT6T80HN8IFJFVrGfJGn4Iz84blg%2B1KaCY%2FfrKc5SEfBLJqGKbmsc9Ne6o1lUQdHNPJdjIghMJQpndIOZkjL7afsHX282JEuROiK4wsVmnma8MJ1g%2FoddSLUkN6xXGi8kxaVheheMBx2YtTrO%2B4ChYqKPF%2F2WXpJX671uZn3cD7Isniu55ow8EmgGxmV8JMSJh1IS8dWz1vfLQMRJLl4ABp8RHBGfIw5bWFScYY4WkwwfmLvQY6pgGcx4SkIoHGXoEeqiojLFNPyS12zLLiUWI6NTlhSRKF7c0Te3oV5GOEl9ICm%2FvXKvHEav8bM2NhfB%2ByR%2FDZaWdrwCiy9Nb6rtIstaB8ZZuyfxyPYOy1ZdhdHCj86bEGABUJfLZZDHvBDOqEhSMnI1rNxKeQRNHyCCeQC%2FMWKf9hhf%2BnhL5CybilTAJYD7vHgfOufyeYJb%2Fummc6NvXjhBCQm0pPqozD&X-Amz-Signature=f0279d1aa673b146881e8a93f305942d162df6bf2419e128687a7f57c494b09b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RD6XG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBCeYorktqU92ABtLi8hnC3Fy8iP3ZzlJBdb2APEXzP9AiEAsqpUfL7omv6v6b4xjFScePE6s44HcwoDCuKpUWdz%2FQEq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFJJRnnPDCe0nXHGjSrcA%2FRlNgw%2BzQWWAEE5NjjaHiCEAg1YCN47GesbS3Ymd0UYsSrpH2aam96blliIFbXjiMB7e2aMOXuxxb21F0FdiDU4B%2FmazkpqL5uyivA7xHXJlnhfD%2F2gWkZG2Ukv5%2BvD12y4TMlBK9sNy03oEw6qeRP5SRkEJ%2BzhFBCj8a1DuobtcQSkZsOwnpfJj9xSFXnCPbDn5AqV%2BIpZJN2oMgVqlc0Wl2yIUkA7pa0sd9JMjRzwEOBycXf6%2BPx7IorANbYZsUIWebZ8Q6KDGrOYD2xvL9SjnRnpXnrUmRvXV7qELWrCBPRgLDKc1VXZyvq5TBOaGhFbh%2FrM%2BE1eh6Ou9MBfMspIV9Bf8fm67fP51%2BdK6wgd%2Bb0KKTThgHkdmYoBoexYKp5tc3qYvhtwb8rzxoiuo4uQ8wypMrCgt33977YHMjCJhhySYxh8pbNrAnxP1bSry39YGS9szHOlg8Z8oSaV0tkt2b3tVZTXjO5Bo2pY7POybjae01DpyxL%2FbcW1mMINldXcyr3oWuakJ1KvZYHrC6rMW3wdvFvX0KwSg8gNTDb6LYY%2Fnmetn62qtayA0BqeysZ%2BixtIXZAvbUu00HBCLpQn%2F0E%2BzKW%2FOQMiRTCAr9Fzrg0gSZX82YigplDOMJ%2F5i70GOqUBhEQN4a%2BhM2yxIQr%2Bg29laFSuWvCMyKK3tSo4gy0cPaqaPDsacHUUe52jhuBEL8Bx671VyrFg9RCZif%2B%2FjOUfvomAEDXiCstIXn10VFy%2BSl5h0Y97d9%2Fya6B5ISksI7BO96OLI5tcaONOn69nMzsE0dmvi0hXZx4Jcd%2B0U9oAp0MwWbnQoVSlmxNip4ecZRMa38D0FW4ouc3Lv%2FeRqiRYUNRdVU3M&X-Amz-Signature=1c68f7367bbeca7ac952daa07e5647dddb306d4bbfabc08154a6b8fe467429ba&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663INMFT7N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDg8Veho0sk2D%2FXEfHzghIuo5RtrIxhPhIMdgVpyPGuaAIgdVTABKw6EKdVgs%2FCUa%2F4aDtuh9Fq0ApYzzjz%2B9olqvYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMMa1oXBOi30Ccl5XyrcA2O6VhMlSDa5DTSRVbOExvN8hsxq90%2BOWnxTalhZl%2B7%2BQwoo%2FCKYgck4Xl9093v1Mrxua9rJcT7I7cSfmnP3S1te2vteGSAly0DFOJx7vxAulH%2FhW48wMuopP1twJoMjwIhdAHjKOrM%2B6TJL4F4LwxGtRn7gRz%2B9vBzeFD2YvsEnTrlKOhfJskYFEIfavRj543kyFky2Tvk%2F1CCh7R0MA7zei6H0V3UMrG%2F3NX6eOWIrV8Xh7AE7xhUAfe0%2BbYjZELrvzP4c0OLBfZ1C%2FFn0G6ctNcV43Ki0VHljyTBSlAwOF1ctH8HdL%2FYMSa3G1NKj8%2FvR6xbChMKtlvqVo8LES7RHbioPwyWLAVjM%2FXkVvt9jQaG1OC8wnK9ARMuguOKD6pOU%2FSB1TDETRxUrEn9yHVt4l7TSvqnNrsW0Jr9w8EECx2oyBCz4ZKNTdpj%2BdBnHB1wVzupPMvMXOaZ8%2FA6Beze2EJbxp7qFLbso8SVMpZkUL3QH6%2BiT6kfTFSQf9KJp54bczC%2F3fmZF%2BXZc8zGvFNadn5DQef6W%2BUHiN8D5JpytaRaOxpPcUfL2f5d0aRe3fA3CBJB9%2BqrgZs1zRG6%2FAGVGstLtndldBvuSiOdK5rws7ZlMddyOXnxQAuQrMNP5i70GOqUB05%2BixIFq%2BQ1X%2Bf5jjfBTLByY%2Fk%2FqEcWQrnmQMAHkY6%2B42PI00AxyRfKfdkkIwhCVDz%2BpvFdwDIRihVAR9tFxzDffWCOoU822s858ZCGoJI3%2BYIaqq4CBKAFVidFIPyf8TOlMUDRoHAZ%2BAoMmAR%2FZKKYcSnDQAdenizv3cKmhPO9nLWrXrjpnytKqHI%2F0Z98LtlwXNXGNQgp2euHJ38euvRcEXb6o&X-Amz-Signature=de2482178dd6faceffa3e1b28d9ab070302aff5cbfdbcc34f8377af04612d09e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUU5QVK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIAHW6HLc3kNPK7vVxRe0YIubYyrmXuSM%2FzJSBquYrFl7AiAmbBgkyfJtpR%2FEYeHa%2F7KnsQudcaAbEP5x%2FTgH4jun6Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMV32jKTKSERbJ2sR%2BKtwDUyMkhmD9b6MXYWSH0Hc%2BYCz9b5%2FNPpYLU9xuTYxJm%2FvM84khJXz0kLwyvgNJYPN%2BxwfcTDNMuMeF0uvoAqgXZZW0AZ7UG236eNoaNT0K2krBdW6olemLJij7FlqC9MaMInomHG61cAr5%2Bc1Uo1c2XsNfl3Vs%2F7Gyf96ZtB0LGudiF%2BHw5gXJPK%2FRX4McfCTUninmdsdDstdIMLe8HNZ6LLLzoNpkgE%2FTHiTJm6oRBIXh9vL9LQeevPyV4%2B0EMiy6ZgV57UPipyHshaLJmGILWIggtqRUX3d24Zi0xKMeJPo41Gl%2F3u0blxOV2xqFxBNXyj5iwk%2BY3cy3vm9E5PA8gwLII0lsHXQwDgi%2BQqLgDEKO3RLkU9H%2BW1ngY5f9njOSyvu3hYbBsrv59CWn8IT6T80HN8IFJFVrGfJGn4Iz84blg%2B1KaCY%2FfrKc5SEfBLJqGKbmsc9Ne6o1lUQdHNPJdjIghMJQpndIOZkjL7afsHX282JEuROiK4wsVmnma8MJ1g%2FoddSLUkN6xXGi8kxaVheheMBx2YtTrO%2B4ChYqKPF%2F2WXpJX671uZn3cD7Isniu55ow8EmgGxmV8JMSJh1IS8dWz1vfLQMRJLl4ABp8RHBGfIw5bWFScYY4WkwwfmLvQY6pgGcx4SkIoHGXoEeqiojLFNPyS12zLLiUWI6NTlhSRKF7c0Te3oV5GOEl9ICm%2FvXKvHEav8bM2NhfB%2ByR%2FDZaWdrwCiy9Nb6rtIstaB8ZZuyfxyPYOy1ZdhdHCj86bEGABUJfLZZDHvBDOqEhSMnI1rNxKeQRNHyCCeQC%2FMWKf9hhf%2BnhL5CybilTAJYD7vHgfOufyeYJb%2Fummc6NvXjhBCQm0pPqozD&X-Amz-Signature=b671c03ecb2ec6433d4d52fe449b4bdbdd9653eee7b19e9810770ae435dfdf4b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUU5QVK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIAHW6HLc3kNPK7vVxRe0YIubYyrmXuSM%2FzJSBquYrFl7AiAmbBgkyfJtpR%2FEYeHa%2F7KnsQudcaAbEP5x%2FTgH4jun6Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMV32jKTKSERbJ2sR%2BKtwDUyMkhmD9b6MXYWSH0Hc%2BYCz9b5%2FNPpYLU9xuTYxJm%2FvM84khJXz0kLwyvgNJYPN%2BxwfcTDNMuMeF0uvoAqgXZZW0AZ7UG236eNoaNT0K2krBdW6olemLJij7FlqC9MaMInomHG61cAr5%2Bc1Uo1c2XsNfl3Vs%2F7Gyf96ZtB0LGudiF%2BHw5gXJPK%2FRX4McfCTUninmdsdDstdIMLe8HNZ6LLLzoNpkgE%2FTHiTJm6oRBIXh9vL9LQeevPyV4%2B0EMiy6ZgV57UPipyHshaLJmGILWIggtqRUX3d24Zi0xKMeJPo41Gl%2F3u0blxOV2xqFxBNXyj5iwk%2BY3cy3vm9E5PA8gwLII0lsHXQwDgi%2BQqLgDEKO3RLkU9H%2BW1ngY5f9njOSyvu3hYbBsrv59CWn8IT6T80HN8IFJFVrGfJGn4Iz84blg%2B1KaCY%2FfrKc5SEfBLJqGKbmsc9Ne6o1lUQdHNPJdjIghMJQpndIOZkjL7afsHX282JEuROiK4wsVmnma8MJ1g%2FoddSLUkN6xXGi8kxaVheheMBx2YtTrO%2B4ChYqKPF%2F2WXpJX671uZn3cD7Isniu55ow8EmgGxmV8JMSJh1IS8dWz1vfLQMRJLl4ABp8RHBGfIw5bWFScYY4WkwwfmLvQY6pgGcx4SkIoHGXoEeqiojLFNPyS12zLLiUWI6NTlhSRKF7c0Te3oV5GOEl9ICm%2FvXKvHEav8bM2NhfB%2ByR%2FDZaWdrwCiy9Nb6rtIstaB8ZZuyfxyPYOy1ZdhdHCj86bEGABUJfLZZDHvBDOqEhSMnI1rNxKeQRNHyCCeQC%2FMWKf9hhf%2BnhL5CybilTAJYD7vHgfOufyeYJb%2Fummc6NvXjhBCQm0pPqozD&X-Amz-Signature=4c351e8836edb9765532f74532215e67b62cf8703ab10614b21d5157c3581403&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUU5QVK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIAHW6HLc3kNPK7vVxRe0YIubYyrmXuSM%2FzJSBquYrFl7AiAmbBgkyfJtpR%2FEYeHa%2F7KnsQudcaAbEP5x%2FTgH4jun6Sr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMV32jKTKSERbJ2sR%2BKtwDUyMkhmD9b6MXYWSH0Hc%2BYCz9b5%2FNPpYLU9xuTYxJm%2FvM84khJXz0kLwyvgNJYPN%2BxwfcTDNMuMeF0uvoAqgXZZW0AZ7UG236eNoaNT0K2krBdW6olemLJij7FlqC9MaMInomHG61cAr5%2Bc1Uo1c2XsNfl3Vs%2F7Gyf96ZtB0LGudiF%2BHw5gXJPK%2FRX4McfCTUninmdsdDstdIMLe8HNZ6LLLzoNpkgE%2FTHiTJm6oRBIXh9vL9LQeevPyV4%2B0EMiy6ZgV57UPipyHshaLJmGILWIggtqRUX3d24Zi0xKMeJPo41Gl%2F3u0blxOV2xqFxBNXyj5iwk%2BY3cy3vm9E5PA8gwLII0lsHXQwDgi%2BQqLgDEKO3RLkU9H%2BW1ngY5f9njOSyvu3hYbBsrv59CWn8IT6T80HN8IFJFVrGfJGn4Iz84blg%2B1KaCY%2FfrKc5SEfBLJqGKbmsc9Ne6o1lUQdHNPJdjIghMJQpndIOZkjL7afsHX282JEuROiK4wsVmnma8MJ1g%2FoddSLUkN6xXGi8kxaVheheMBx2YtTrO%2B4ChYqKPF%2F2WXpJX671uZn3cD7Isniu55ow8EmgGxmV8JMSJh1IS8dWz1vfLQMRJLl4ABp8RHBGfIw5bWFScYY4WkwwfmLvQY6pgGcx4SkIoHGXoEeqiojLFNPyS12zLLiUWI6NTlhSRKF7c0Te3oV5GOEl9ICm%2FvXKvHEav8bM2NhfB%2ByR%2FDZaWdrwCiy9Nb6rtIstaB8ZZuyfxyPYOy1ZdhdHCj86bEGABUJfLZZDHvBDOqEhSMnI1rNxKeQRNHyCCeQC%2FMWKf9hhf%2BnhL5CybilTAJYD7vHgfOufyeYJb%2Fummc6NvXjhBCQm0pPqozD&X-Amz-Signature=759aca7463abb16faf1f613d837e549bd1f81b698863c35ee24a7f7ef472bb8b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YG4ERXR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIDd5R4BdzVugJvgEACfOcNoT5Epi1fdPmEzTQUQv1vXJAiEApIYuI4HeNCkzbEQOiz8S7LqbeGvLsqjRhDgt51pLD4gq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFL5xBQ%2FQzrqCjekMircA2Z2PRpcslrx%2BFJuRkjP0BAF9gKN%2BbmvmCrkb7P2GpKlAjy%2FSzuD1rQuochct8XGAvvzAc0qR2ZSAXkvsXgyIt8Jh5JQXrATZN9Je43%2BVhjJA%2B8pL4S5fPI4B1dfvy25825iP4ti4BNVYlh2cvNEhR8Jbz2q66n1B%2FSgxW9NsdlcLcVZQAWX75K69xGplYAF2WB%2FLlrTf3biWu%2FneGLRtPZ45TwUTzsl%2BhDSvvJTE8Z25TmlmP6zxz9puJLyAHuEtVqq%2FH36QOEx5F%2Bm%2F7cMlaGenTfBiLEo6%2B0SadgPwcr8bA0S0k6Tgq226qYktNNzgwLfK9MZ4M6KUheHXwq3R5%2Bd0tV%2By6dSXL%2B4AkB44KyopQvFjGLTVzSUKJkFx2NOFlg%2FOyPW4Nk1rrs5z8ErCJH3sC7D%2B0VmYNm2h%2BNUcwaK5MQ3aoE34yfVX2w2nZPBfkE%2F%2FyZVbSGP9rFmoq%2F80vAamcsccn6G8Uh1FqFbqaZXNmxcYQ0t%2FTplRqmPedHNafmmXc2B4xmCcHtSx%2BmoiX0xPEtXudOT%2BvYG6w1PBsmkzIhxcvL%2Fs3wRIw7KNCqsVfcxN3%2Bzf6XfykOFz%2BlHVg4R7hgccmmR%2FtCnmuHWxZxzNVtj52LX8IAEN9djMIn6i70GOqUBjqlSpdRg3DtrVNtVbDIGUpGPmS2weq2Ck0qAOxypNAR5h9nh74Wx3w1aIOkm%2BYR%2Fjm1Gpbm7Dh9Upwt4TULAb1mSpjaD%2FNM9OV5zqd8yG06uRRyEDrqv%2FxMPoTW1%2BSeBIbr8OH6KUBzMkSKOi7Hh%2BCDqwwMH6BREualhyqf6vkbaa1PwsLZi2H9hZxVMWubfVknk6x53DipnnVQ5l0dgE7bnJhM0&X-Amz-Signature=387d2cecbd08cc1d2798f5732f033b99bae6f42ae0629ff85f8f272675752986&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DD7CPKO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQDx%2F5Gx2Z0yHqsvANTtJS5Na5ZbPalgxXwiUYY8Cw7F4gIhAKSaPMpVVGuD8V%2B7%2Bapl2wszn2Q4rQyoUk1%2Be633jLwNKv8DCD8QABoMNjM3NDIzMTgzODA1IgzUhlRT%2FQi%2FSSBG%2F1Mq3APWwXpWuKwzJmoAgvHl9psHpJDlPh5sQg1tEiMyQXZRQAdysOuAek5PCIrtfHaYyiJygFt5%2FiMAV%2BYvYz24p2Q6O1AS7Qa3L8v7NMP2aDqnirPXeZ1MKojzEaIcwaDv2PvoF6E1bRBmeCza85%2F9cUyHvYTBfhIuLoHl1pzon0ijLC2VSKRPUPyEhGXbAhpUmceSW6CiZ%2BYRNdU%2B5xM1PAH8f%2BiBcXtR18tHBJPw1mSPrIKeiPfPXEulEPiCZmtS9LeOZKC%2FZHcLi03zZmBGIX1LLaYAuZWlO1SMyftXUv4VJwAdncziQyVtQKtGr9H42vaNTqsIcKpcIvXZx3yx2tGUIaGY1lBJ0l9%2BzCJ4suidOLmv5NaXtXRQsBU3E780VCaMVWYZ%2FnJKZA44VyYbyEXovcSNpPMZKeeBUiSvZ3AW6ZFMtjnF%2FXqE460TH3ye6mWuwKwORk82CmKS0S%2F4ax1DRsJGUeoHFMNWRpoE2j67WMRH7ARwhq8mKTlsNSIOq0tGKE5OKCqVk5BDBSaXVtK5CUb2BMJlVJWwmda8pbkS3JZyqxUWffgzouWexaqwZu%2Bcl%2Bux%2FAyBEzf5Gz48m2p%2BqrceQuLfT25YsA5HfPjHsYTL1H3ug56hFcLTKjDd%2BYu9BjqkATLQugBnuV6d7ZdcFqTwGVtDnARPTEo5ZUj%2FGTLDC1CLv6O%2BRMJUGSWAy0qmwn3lSS39VdqSKouxURsYlZbnKxnseJxHmaWaRYM19%2FWX32wcZeuYU9RPecmJgPLopDCoirixx6YIH0uAvHrJXylHN5Lq1k%2F206VmcZYA0XEYTaLU08u2DAd75qxiC2Kta4DpFt6mlPwltzd6HcMfbloxcNkRa5ME&X-Amz-Signature=40e0dc626a8b4d348c1758b3692c265ef984047f1a620d738d4e42380b7a69fa&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7XKNVRU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQC6aRdUqLDRQHKhqKnZ3Q%2BINfKheyhNwo2IkammLzGNzQIgbQxu%2F%2BkocbP5%2BhnoHa6ySH%2FMHYw3fKZoe1wl1EOxCGoq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMNhmpmSo%2BKonekGwSrcA0wBHXxx42DUczlOHTwuhC7k20quNoGBseN6NFU64qKkTplDz3o%2BPSfSGb%2Fa1%2BdNgwzIWH19I2YIB5fOTZaFGS1SkEb%2Fh%2Bq7LRw0AjYRF%2FBTwjd%2FjLCzmbSCqYOOHCRO4U7ky1jCa%2BcPyohf%2F4zKc4YOZCU5ysUJRPeXFvggiXUqtzTO51mP4weXeML%2BgyFOWLxHmQYDneSO9v1YmRz7Oy7i0ksG268NT8oQ7RAdEgGDE9xJfUDSOmYPlEvKV%2BasQoBDkF2mZC12Qeq9353zEdK60U%2Fa2%2BZqSao%2F9DJy%2Fwc1kuQuggLGY7D4doEKWxZbu4iEWHs6cq5IFHOM1Bfzn4wrDhnuoNEAyfxJb6NqCda0qwmchZCCRMnFPwisFfaG3ga7EeWE3Z3r6otZQUUBko3MnoHyLMIY4Q2D1THA%2FpRefTIXuNVgZzgZdjB4zMQlMYF97UenqBgaEwKzRZCT0ipdP%2FauMmmB0jPuhN4%2BBHtuLTrc5bwPcZrcCOXDKIVi6vRPeedGeVOeiSQa7xrBqUKTfl32ldQbWPq0gG21ZxLP0y6o1WdshzUYXtQ%2BfRWJ7dsoOuO1IqyuShNADW5CQ7xirnw%2FfYW9meyVizSvv71ZiGI70cWkNDH5mWCTMKz5i70GOqUB3bDkCDEw1K5MGWkC6jh%2FMIyaEx%2BNvaQmr9tjvUC1Dnv9mD3hFvr95lgJHDLEQ3qVz8S5GnsmHQ56FHbt%2Bn77CWjvMipVhGpFkjElGkJiIbpMWOxr%2FVtAWLJE7uZ%2B9TA%2BHp1YxnapA%2Bz312XPOHnUgyLF9436QO9nvGHxpjcPJH5GK1RCmI10XGHzNi3swC4tk68u49aN%2F6fvVRk%2BzduukIEpDftl&X-Amz-Signature=18f077aad0f13bd84f9218d589896600c3b7eac3bf601fc3cb4fc9a3a7888110&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U32ETZ6N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCiUdH5IWzx2s3PutazxFRuaM2w2OQztn1A8uA9I82zVgIhAI7fmPJEU4SsK09PBNZb37dm0mjz6Q6PYvUJfVcM0yAJKv8DCD8QABoMNjM3NDIzMTgzODA1IgybaM86Py0W1wo1O1Aq3AON%2FAzzCJ3lq7LT9PoKYbWBCgRNfwXlkGEe13KYKsBsRTk0CZk0e05cCnG0lBw98zLNLxHnnjAZfRFmSH0908j%2BQF2yHuJOZfEAD7qSSao%2FsyHfBYhYXrUo4llGkmme2dx1mrotrV5z781XqbkEDUgYEZHFoJT6WLY3WpNdjzpJ6w3iOTWZil8GrZh%2FLE47felGUq8Y1M66dvmjc40ryIA4Xj4%2Bg1XfvtOLchOXV4BzTAiZjbiadS1jEkQOI3BfkdxPGAswHITBHg3iUSpW9Qe7Ps4BReWUetJRH81iKas360702SAjMkwmwHcTzsJM%2FPUPJRG51XeRrDQtVQxvNFycgF%2B50iqhPzzuW%2F%2FwlhME7Y9bOc9525t5fgvTTye3t%2B2PWHgeh%2FrDffffARFkviPS9BqNfkqGtDmiOAyYlN%2FVUQESu%2FTvj7rKNmEwudbW5JuAr4CCljEbSYj5Pd2ZXGXsyYg3p4TrNZKEVY08I9XBSEm2cK4Ce7wqJyl6EoIJvThCJqE7H0%2FL8kdp99gGZxwoFFaE0G1ltNj0DY3SJbvJamW1Q3C7QgBg5lrYSwiaKN2dpv8dvHouwIGBXguSRwbGStKyUopo67QDuNa9D9zdZZHyRoKwoosl%2FJIFYjDS%2BYu9BjqkARU4s9sgpoBC%2F96AvOHSB1qNQ1JAYPn3oZ9Y3fujV5R2zEZywGwdtSghXuajWQUOR3fOH%2FvyWr2cYApVmlzgChqGekwdmFWlepJNz%2FRC4rnKI6SeBv%2FHsTTxVrrwAc7v763sHJKmQfiS%2BLmTFQfirsv5uftGZAJ57Y5Fc%2Bge8TfexpqIPsQ7swn4%2FqC7sP6udcM7g%2FI86n2IbgIWv5Hf254CokdB&X-Amz-Signature=a4f91b36d8d43bffe820c4ca9948c6e27a8e75d2c33b1b6dd33509fc160c1114&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U32ETZ6N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCiUdH5IWzx2s3PutazxFRuaM2w2OQztn1A8uA9I82zVgIhAI7fmPJEU4SsK09PBNZb37dm0mjz6Q6PYvUJfVcM0yAJKv8DCD8QABoMNjM3NDIzMTgzODA1IgybaM86Py0W1wo1O1Aq3AON%2FAzzCJ3lq7LT9PoKYbWBCgRNfwXlkGEe13KYKsBsRTk0CZk0e05cCnG0lBw98zLNLxHnnjAZfRFmSH0908j%2BQF2yHuJOZfEAD7qSSao%2FsyHfBYhYXrUo4llGkmme2dx1mrotrV5z781XqbkEDUgYEZHFoJT6WLY3WpNdjzpJ6w3iOTWZil8GrZh%2FLE47felGUq8Y1M66dvmjc40ryIA4Xj4%2Bg1XfvtOLchOXV4BzTAiZjbiadS1jEkQOI3BfkdxPGAswHITBHg3iUSpW9Qe7Ps4BReWUetJRH81iKas360702SAjMkwmwHcTzsJM%2FPUPJRG51XeRrDQtVQxvNFycgF%2B50iqhPzzuW%2F%2FwlhME7Y9bOc9525t5fgvTTye3t%2B2PWHgeh%2FrDffffARFkviPS9BqNfkqGtDmiOAyYlN%2FVUQESu%2FTvj7rKNmEwudbW5JuAr4CCljEbSYj5Pd2ZXGXsyYg3p4TrNZKEVY08I9XBSEm2cK4Ce7wqJyl6EoIJvThCJqE7H0%2FL8kdp99gGZxwoFFaE0G1ltNj0DY3SJbvJamW1Q3C7QgBg5lrYSwiaKN2dpv8dvHouwIGBXguSRwbGStKyUopo67QDuNa9D9zdZZHyRoKwoosl%2FJIFYjDS%2BYu9BjqkARU4s9sgpoBC%2F96AvOHSB1qNQ1JAYPn3oZ9Y3fujV5R2zEZywGwdtSghXuajWQUOR3fOH%2FvyWr2cYApVmlzgChqGekwdmFWlepJNz%2FRC4rnKI6SeBv%2FHsTTxVrrwAc7v763sHJKmQfiS%2BLmTFQfirsv5uftGZAJ57Y5Fc%2Bge8TfexpqIPsQ7swn4%2FqC7sP6udcM7g%2FI86n2IbgIWv5Hf254CokdB&X-Amz-Signature=36177eedf492bbee0fe006c4c45f555e6e41e5aab5ee256819727eb4f1f5a3c9&X-Amz-SignedHeaders=host&x-id=GetObject)

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
