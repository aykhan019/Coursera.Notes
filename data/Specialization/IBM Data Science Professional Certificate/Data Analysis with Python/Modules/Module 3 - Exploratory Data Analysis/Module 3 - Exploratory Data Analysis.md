

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLGF6LSJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTuDQiwlNSkBeyKmjIw0UTyMgfuRrFC2UOv%2F87W1J%2FRAIhAKUckpMS5VibJRSkRupT48uV2Rdtleg629jKV5xU3FRHKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVCDOT7YYO8lOEOcMq3AONjFuDFVx1AfN0jCw7bD3pO%2B1wN23bkJ112%2F74IVlA0CcSzv66vJB303qT%2FWCnyqmEuue%2BJKEMDIxpIkHHn5DUhbclFG1wEy%2BfEcYeYO27TtBaUBo%2Fef4u8SnLrkwp5IFr9rYS8a%2BOeRB6RhNKlU64vbgTDbGdD63N%2B6n0PjkR1NbrKx%2FT8bRzYipDE725rCHET4ysHvhVIYUHoyqP0wzbOxN%2BuWrGbiuIFQKm0IhJLTfjvLEScB2WIaS%2FjL23J0S1v4qt2YcNENqmQQ%2Bo%2FozurkprBS6vjMHXAyPECRv14TJoM5y65p3XA7nCFObIloPwmRk9dnSVpuUjfXsNVG03kFQq%2BDObDJqbF6V0404%2FFjkNUbl%2Bk2imhb425OcXf3f31ORDb9hqJOSBHriPvmFeLUx4NP1amiTm9hClW0m8QzHD%2B7UzGhqXPtMqp8UK%2F8WcLYsVS2wZFnNdWbdPJoi%2FH%2FNWHQh4yVbU0nZSYNxXUxTwB2itCzuNtXb7PNhdRDOGGf32Y%2FdLTwzEB0QZ7JfuVZkvgnQaINu5UGV1gBjyatfnqduEd7ICvJCqLFgvLDIg4dEOAQwpo1gtFRaRHLT%2Baqb%2FEi730hBQg3iLz1f63MH1XNtVhnm1Izmo0zDD%2F%2Be8BjqkAcd2Gji4IMuGnVDpfhTqLK36Ra9YAVPRdbhbu4Ky1LL%2FpjUV3U97AEJJu82qjnVh%2BUaNnerxLolzfnaUrDlkpFkZHuW0J%2B7Xg69nTAcZrXJGejHYpuFCGVQ6jB40Hw8i7VH8dnR79MRa7c8OzLwQ3y2RAJl6tOCjEHAGUiDsu0Vsx0shjH%2FMKWZbMggT1sZrgwEjIFLYhOKN%2BuXqMKESo4%2FTdLeT&X-Amz-Signature=fb36c63509cef82d19af0fc65acd9ed21ecee7414c2b01a5cd6e533b066e9edf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLGF6LSJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTuDQiwlNSkBeyKmjIw0UTyMgfuRrFC2UOv%2F87W1J%2FRAIhAKUckpMS5VibJRSkRupT48uV2Rdtleg629jKV5xU3FRHKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVCDOT7YYO8lOEOcMq3AONjFuDFVx1AfN0jCw7bD3pO%2B1wN23bkJ112%2F74IVlA0CcSzv66vJB303qT%2FWCnyqmEuue%2BJKEMDIxpIkHHn5DUhbclFG1wEy%2BfEcYeYO27TtBaUBo%2Fef4u8SnLrkwp5IFr9rYS8a%2BOeRB6RhNKlU64vbgTDbGdD63N%2B6n0PjkR1NbrKx%2FT8bRzYipDE725rCHET4ysHvhVIYUHoyqP0wzbOxN%2BuWrGbiuIFQKm0IhJLTfjvLEScB2WIaS%2FjL23J0S1v4qt2YcNENqmQQ%2Bo%2FozurkprBS6vjMHXAyPECRv14TJoM5y65p3XA7nCFObIloPwmRk9dnSVpuUjfXsNVG03kFQq%2BDObDJqbF6V0404%2FFjkNUbl%2Bk2imhb425OcXf3f31ORDb9hqJOSBHriPvmFeLUx4NP1amiTm9hClW0m8QzHD%2B7UzGhqXPtMqp8UK%2F8WcLYsVS2wZFnNdWbdPJoi%2FH%2FNWHQh4yVbU0nZSYNxXUxTwB2itCzuNtXb7PNhdRDOGGf32Y%2FdLTwzEB0QZ7JfuVZkvgnQaINu5UGV1gBjyatfnqduEd7ICvJCqLFgvLDIg4dEOAQwpo1gtFRaRHLT%2Baqb%2FEi730hBQg3iLz1f63MH1XNtVhnm1Izmo0zDD%2F%2Be8BjqkAcd2Gji4IMuGnVDpfhTqLK36Ra9YAVPRdbhbu4Ky1LL%2FpjUV3U97AEJJu82qjnVh%2BUaNnerxLolzfnaUrDlkpFkZHuW0J%2B7Xg69nTAcZrXJGejHYpuFCGVQ6jB40Hw8i7VH8dnR79MRa7c8OzLwQ3y2RAJl6tOCjEHAGUiDsu0Vsx0shjH%2FMKWZbMggT1sZrgwEjIFLYhOKN%2BuXqMKESo4%2FTdLeT&X-Amz-Signature=03a35f881cb2cdb9bd60c03e92b04e97633151838b10eb06a07021770fcc7336&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLGF6LSJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTuDQiwlNSkBeyKmjIw0UTyMgfuRrFC2UOv%2F87W1J%2FRAIhAKUckpMS5VibJRSkRupT48uV2Rdtleg629jKV5xU3FRHKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVCDOT7YYO8lOEOcMq3AONjFuDFVx1AfN0jCw7bD3pO%2B1wN23bkJ112%2F74IVlA0CcSzv66vJB303qT%2FWCnyqmEuue%2BJKEMDIxpIkHHn5DUhbclFG1wEy%2BfEcYeYO27TtBaUBo%2Fef4u8SnLrkwp5IFr9rYS8a%2BOeRB6RhNKlU64vbgTDbGdD63N%2B6n0PjkR1NbrKx%2FT8bRzYipDE725rCHET4ysHvhVIYUHoyqP0wzbOxN%2BuWrGbiuIFQKm0IhJLTfjvLEScB2WIaS%2FjL23J0S1v4qt2YcNENqmQQ%2Bo%2FozurkprBS6vjMHXAyPECRv14TJoM5y65p3XA7nCFObIloPwmRk9dnSVpuUjfXsNVG03kFQq%2BDObDJqbF6V0404%2FFjkNUbl%2Bk2imhb425OcXf3f31ORDb9hqJOSBHriPvmFeLUx4NP1amiTm9hClW0m8QzHD%2B7UzGhqXPtMqp8UK%2F8WcLYsVS2wZFnNdWbdPJoi%2FH%2FNWHQh4yVbU0nZSYNxXUxTwB2itCzuNtXb7PNhdRDOGGf32Y%2FdLTwzEB0QZ7JfuVZkvgnQaINu5UGV1gBjyatfnqduEd7ICvJCqLFgvLDIg4dEOAQwpo1gtFRaRHLT%2Baqb%2FEi730hBQg3iLz1f63MH1XNtVhnm1Izmo0zDD%2F%2Be8BjqkAcd2Gji4IMuGnVDpfhTqLK36Ra9YAVPRdbhbu4Ky1LL%2FpjUV3U97AEJJu82qjnVh%2BUaNnerxLolzfnaUrDlkpFkZHuW0J%2B7Xg69nTAcZrXJGejHYpuFCGVQ6jB40Hw8i7VH8dnR79MRa7c8OzLwQ3y2RAJl6tOCjEHAGUiDsu0Vsx0shjH%2FMKWZbMggT1sZrgwEjIFLYhOKN%2BuXqMKESo4%2FTdLeT&X-Amz-Signature=5d782dd37cf30616e201cfa8df3448b1322a6b3ac9b403abbd1bdcc7b9f8fc50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMEIXNEB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxioIy%2F4xtje0adZQEcylqYeahE%2Fnsety0Qg8Es%2F7bzAIgaKvZD1ZLYmAy6%2F2OlPtPsDVCPANXVdwxl%2F%2Fn6F4S1PgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCo0dAO12glEKJ8OgircA3gKGl%2BMEOcg6ctvIriEVDucj55h0Porz6hR86B%2BuqkxVdIUhMPGqYO7CdP%2FwY7Us2v0F8TTmW3tHim%2BW5A8dItpgd2HtK1oeaTlLPTILF3RdzsfV71N%2FtVxWuae8zonLg%2BItbnznTa2nY7bV%2BJvyUZ%2FQHJCImmYuhTOXCuyIjMIiuVhyqCBf9ekFQXWhOPp8SchNOlSk1QMGNn3kB47AZci1vdb5B%2FlXHLBB4mXxQQrCO1L1nyksLgxRy8HtbveqXrOT2TGiDkTMq144ZcdcViRvUBbog4go6Q551cRg8GtoMLm4PfEkYXG3lxHN7YaQZGrgInDFVu7t19x3PtgwTfhqtWrFtagiVNpompayLvZSQzq0H4PstkG6bp6Wcah4tf6CTxuju8PEyIucCtyPH4UzK0EbrKShjIjso29sacfvC9DjMGzj2pKEDNKGTFExVQErkyl8I2Y0WVbLj1mWUswhSdA23EoJg8jZma03F2RQO3kAy1AJoLjTE66OYZPb5F9B6cg%2BTg%2F6p2NbjkhRyQSQCquQ3%2BHRh%2FCcfnYe4pduTyczWocXCV481XlbkBm39OsYU0LHeoQBDTce1EGzUq9hV9dh7PAVhJv43l7AWrD%2BAk7IfKrfSsUa8kCMIuA6LwGOqUBubAFiTQHLPnhzfBfA7rcKCpeFscy%2BZOeHBsWiwz%2BpV5P8aTfPaNf8%2FY4sZ%2FZROzbSse7h34dWQX8PC6ce3ZpUNHDvqAt35LdRE9fV6fLzT0M%2BNlflhyeuNaWUbE37yheIOm2DSJIq2Rh6N9YGtnsUIppBN%2Bd8HHO7g7WvOgBC%2BnMKQNPChjt6spJKQEjLNh2jpJv%2F0ArhsQS5T%2FZXh%2FkDqmpxCcX&X-Amz-Signature=439820bcc7bef81f9569dfcb62fd0a70f8de75d3f110c76b26fbd9d902bb235b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMEIXNEB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxioIy%2F4xtje0adZQEcylqYeahE%2Fnsety0Qg8Es%2F7bzAIgaKvZD1ZLYmAy6%2F2OlPtPsDVCPANXVdwxl%2F%2Fn6F4S1PgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCo0dAO12glEKJ8OgircA3gKGl%2BMEOcg6ctvIriEVDucj55h0Porz6hR86B%2BuqkxVdIUhMPGqYO7CdP%2FwY7Us2v0F8TTmW3tHim%2BW5A8dItpgd2HtK1oeaTlLPTILF3RdzsfV71N%2FtVxWuae8zonLg%2BItbnznTa2nY7bV%2BJvyUZ%2FQHJCImmYuhTOXCuyIjMIiuVhyqCBf9ekFQXWhOPp8SchNOlSk1QMGNn3kB47AZci1vdb5B%2FlXHLBB4mXxQQrCO1L1nyksLgxRy8HtbveqXrOT2TGiDkTMq144ZcdcViRvUBbog4go6Q551cRg8GtoMLm4PfEkYXG3lxHN7YaQZGrgInDFVu7t19x3PtgwTfhqtWrFtagiVNpompayLvZSQzq0H4PstkG6bp6Wcah4tf6CTxuju8PEyIucCtyPH4UzK0EbrKShjIjso29sacfvC9DjMGzj2pKEDNKGTFExVQErkyl8I2Y0WVbLj1mWUswhSdA23EoJg8jZma03F2RQO3kAy1AJoLjTE66OYZPb5F9B6cg%2BTg%2F6p2NbjkhRyQSQCquQ3%2BHRh%2FCcfnYe4pduTyczWocXCV481XlbkBm39OsYU0LHeoQBDTce1EGzUq9hV9dh7PAVhJv43l7AWrD%2BAk7IfKrfSsUa8kCMIuA6LwGOqUBubAFiTQHLPnhzfBfA7rcKCpeFscy%2BZOeHBsWiwz%2BpV5P8aTfPaNf8%2FY4sZ%2FZROzbSse7h34dWQX8PC6ce3ZpUNHDvqAt35LdRE9fV6fLzT0M%2BNlflhyeuNaWUbE37yheIOm2DSJIq2Rh6N9YGtnsUIppBN%2Bd8HHO7g7WvOgBC%2BnMKQNPChjt6spJKQEjLNh2jpJv%2F0ArhsQS5T%2FZXh%2FkDqmpxCcX&X-Amz-Signature=cb2e41dc0d6d0a7b3e1cb12dd3a2645de057608aec98c0d23ce333744173d077&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMEIXNEB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxioIy%2F4xtje0adZQEcylqYeahE%2Fnsety0Qg8Es%2F7bzAIgaKvZD1ZLYmAy6%2F2OlPtPsDVCPANXVdwxl%2F%2Fn6F4S1PgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCo0dAO12glEKJ8OgircA3gKGl%2BMEOcg6ctvIriEVDucj55h0Porz6hR86B%2BuqkxVdIUhMPGqYO7CdP%2FwY7Us2v0F8TTmW3tHim%2BW5A8dItpgd2HtK1oeaTlLPTILF3RdzsfV71N%2FtVxWuae8zonLg%2BItbnznTa2nY7bV%2BJvyUZ%2FQHJCImmYuhTOXCuyIjMIiuVhyqCBf9ekFQXWhOPp8SchNOlSk1QMGNn3kB47AZci1vdb5B%2FlXHLBB4mXxQQrCO1L1nyksLgxRy8HtbveqXrOT2TGiDkTMq144ZcdcViRvUBbog4go6Q551cRg8GtoMLm4PfEkYXG3lxHN7YaQZGrgInDFVu7t19x3PtgwTfhqtWrFtagiVNpompayLvZSQzq0H4PstkG6bp6Wcah4tf6CTxuju8PEyIucCtyPH4UzK0EbrKShjIjso29sacfvC9DjMGzj2pKEDNKGTFExVQErkyl8I2Y0WVbLj1mWUswhSdA23EoJg8jZma03F2RQO3kAy1AJoLjTE66OYZPb5F9B6cg%2BTg%2F6p2NbjkhRyQSQCquQ3%2BHRh%2FCcfnYe4pduTyczWocXCV481XlbkBm39OsYU0LHeoQBDTce1EGzUq9hV9dh7PAVhJv43l7AWrD%2BAk7IfKrfSsUa8kCMIuA6LwGOqUBubAFiTQHLPnhzfBfA7rcKCpeFscy%2BZOeHBsWiwz%2BpV5P8aTfPaNf8%2FY4sZ%2FZROzbSse7h34dWQX8PC6ce3ZpUNHDvqAt35LdRE9fV6fLzT0M%2BNlflhyeuNaWUbE37yheIOm2DSJIq2Rh6N9YGtnsUIppBN%2Bd8HHO7g7WvOgBC%2BnMKQNPChjt6spJKQEjLNh2jpJv%2F0ArhsQS5T%2FZXh%2FkDqmpxCcX&X-Amz-Signature=2524453bae2f1dbacd83fa88882dabf2b85b2ae45b0c28a6550689a177353507&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMEIXNEB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxioIy%2F4xtje0adZQEcylqYeahE%2Fnsety0Qg8Es%2F7bzAIgaKvZD1ZLYmAy6%2F2OlPtPsDVCPANXVdwxl%2F%2Fn6F4S1PgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCo0dAO12glEKJ8OgircA3gKGl%2BMEOcg6ctvIriEVDucj55h0Porz6hR86B%2BuqkxVdIUhMPGqYO7CdP%2FwY7Us2v0F8TTmW3tHim%2BW5A8dItpgd2HtK1oeaTlLPTILF3RdzsfV71N%2FtVxWuae8zonLg%2BItbnznTa2nY7bV%2BJvyUZ%2FQHJCImmYuhTOXCuyIjMIiuVhyqCBf9ekFQXWhOPp8SchNOlSk1QMGNn3kB47AZci1vdb5B%2FlXHLBB4mXxQQrCO1L1nyksLgxRy8HtbveqXrOT2TGiDkTMq144ZcdcViRvUBbog4go6Q551cRg8GtoMLm4PfEkYXG3lxHN7YaQZGrgInDFVu7t19x3PtgwTfhqtWrFtagiVNpompayLvZSQzq0H4PstkG6bp6Wcah4tf6CTxuju8PEyIucCtyPH4UzK0EbrKShjIjso29sacfvC9DjMGzj2pKEDNKGTFExVQErkyl8I2Y0WVbLj1mWUswhSdA23EoJg8jZma03F2RQO3kAy1AJoLjTE66OYZPb5F9B6cg%2BTg%2F6p2NbjkhRyQSQCquQ3%2BHRh%2FCcfnYe4pduTyczWocXCV481XlbkBm39OsYU0LHeoQBDTce1EGzUq9hV9dh7PAVhJv43l7AWrD%2BAk7IfKrfSsUa8kCMIuA6LwGOqUBubAFiTQHLPnhzfBfA7rcKCpeFscy%2BZOeHBsWiwz%2BpV5P8aTfPaNf8%2FY4sZ%2FZROzbSse7h34dWQX8PC6ce3ZpUNHDvqAt35LdRE9fV6fLzT0M%2BNlflhyeuNaWUbE37yheIOm2DSJIq2Rh6N9YGtnsUIppBN%2Bd8HHO7g7WvOgBC%2BnMKQNPChjt6spJKQEjLNh2jpJv%2F0ArhsQS5T%2FZXh%2FkDqmpxCcX&X-Amz-Signature=c5dbec35444154391ea74b67a8b5d072d752d2213441067b0bae6f17699bad4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMEIXNEB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxioIy%2F4xtje0adZQEcylqYeahE%2Fnsety0Qg8Es%2F7bzAIgaKvZD1ZLYmAy6%2F2OlPtPsDVCPANXVdwxl%2F%2Fn6F4S1PgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCo0dAO12glEKJ8OgircA3gKGl%2BMEOcg6ctvIriEVDucj55h0Porz6hR86B%2BuqkxVdIUhMPGqYO7CdP%2FwY7Us2v0F8TTmW3tHim%2BW5A8dItpgd2HtK1oeaTlLPTILF3RdzsfV71N%2FtVxWuae8zonLg%2BItbnznTa2nY7bV%2BJvyUZ%2FQHJCImmYuhTOXCuyIjMIiuVhyqCBf9ekFQXWhOPp8SchNOlSk1QMGNn3kB47AZci1vdb5B%2FlXHLBB4mXxQQrCO1L1nyksLgxRy8HtbveqXrOT2TGiDkTMq144ZcdcViRvUBbog4go6Q551cRg8GtoMLm4PfEkYXG3lxHN7YaQZGrgInDFVu7t19x3PtgwTfhqtWrFtagiVNpompayLvZSQzq0H4PstkG6bp6Wcah4tf6CTxuju8PEyIucCtyPH4UzK0EbrKShjIjso29sacfvC9DjMGzj2pKEDNKGTFExVQErkyl8I2Y0WVbLj1mWUswhSdA23EoJg8jZma03F2RQO3kAy1AJoLjTE66OYZPb5F9B6cg%2BTg%2F6p2NbjkhRyQSQCquQ3%2BHRh%2FCcfnYe4pduTyczWocXCV481XlbkBm39OsYU0LHeoQBDTce1EGzUq9hV9dh7PAVhJv43l7AWrD%2BAk7IfKrfSsUa8kCMIuA6LwGOqUBubAFiTQHLPnhzfBfA7rcKCpeFscy%2BZOeHBsWiwz%2BpV5P8aTfPaNf8%2FY4sZ%2FZROzbSse7h34dWQX8PC6ce3ZpUNHDvqAt35LdRE9fV6fLzT0M%2BNlflhyeuNaWUbE37yheIOm2DSJIq2Rh6N9YGtnsUIppBN%2Bd8HHO7g7WvOgBC%2BnMKQNPChjt6spJKQEjLNh2jpJv%2F0ArhsQS5T%2FZXh%2FkDqmpxCcX&X-Amz-Signature=46d9e2a3b87224a5b0f3a7fc1c3b191b4d6f1a11bd9c445680d539ccaa2d2323&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMEIXNEB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxioIy%2F4xtje0adZQEcylqYeahE%2Fnsety0Qg8Es%2F7bzAIgaKvZD1ZLYmAy6%2F2OlPtPsDVCPANXVdwxl%2F%2Fn6F4S1PgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCo0dAO12glEKJ8OgircA3gKGl%2BMEOcg6ctvIriEVDucj55h0Porz6hR86B%2BuqkxVdIUhMPGqYO7CdP%2FwY7Us2v0F8TTmW3tHim%2BW5A8dItpgd2HtK1oeaTlLPTILF3RdzsfV71N%2FtVxWuae8zonLg%2BItbnznTa2nY7bV%2BJvyUZ%2FQHJCImmYuhTOXCuyIjMIiuVhyqCBf9ekFQXWhOPp8SchNOlSk1QMGNn3kB47AZci1vdb5B%2FlXHLBB4mXxQQrCO1L1nyksLgxRy8HtbveqXrOT2TGiDkTMq144ZcdcViRvUBbog4go6Q551cRg8GtoMLm4PfEkYXG3lxHN7YaQZGrgInDFVu7t19x3PtgwTfhqtWrFtagiVNpompayLvZSQzq0H4PstkG6bp6Wcah4tf6CTxuju8PEyIucCtyPH4UzK0EbrKShjIjso29sacfvC9DjMGzj2pKEDNKGTFExVQErkyl8I2Y0WVbLj1mWUswhSdA23EoJg8jZma03F2RQO3kAy1AJoLjTE66OYZPb5F9B6cg%2BTg%2F6p2NbjkhRyQSQCquQ3%2BHRh%2FCcfnYe4pduTyczWocXCV481XlbkBm39OsYU0LHeoQBDTce1EGzUq9hV9dh7PAVhJv43l7AWrD%2BAk7IfKrfSsUa8kCMIuA6LwGOqUBubAFiTQHLPnhzfBfA7rcKCpeFscy%2BZOeHBsWiwz%2BpV5P8aTfPaNf8%2FY4sZ%2FZROzbSse7h34dWQX8PC6ce3ZpUNHDvqAt35LdRE9fV6fLzT0M%2BNlflhyeuNaWUbE37yheIOm2DSJIq2Rh6N9YGtnsUIppBN%2Bd8HHO7g7WvOgBC%2BnMKQNPChjt6spJKQEjLNh2jpJv%2F0ArhsQS5T%2FZXh%2FkDqmpxCcX&X-Amz-Signature=b2dbecbdd0d93fa5b6b0695fc80bf73e0987f7aafe52f4a8591180ba3908ea4f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WNDWL3F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTCJM9gwzLmYTBE%2BiIoTPZHtHsQlPVHy5TklS72bFA8QIhAPffdjFRzqauAL3FCtZHh3j1oAl02jpH366%2Ff1HHTCTeKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FWCmQy2NeMzLYiVoq3AOTRqO4Tnjfu9%2FGrDhaS33plt5%2FOvIo4QXmSdK9gukZ62v4YmApcK%2FgCIw%2FY9P9%2F2n%2BDlwT7zRf0SQ6CkYjqb5bKyFc%2BeX%2B5iU8TdMU7HeQcLyn%2BXu9HdM7gH83FpuaTIHwFt0dZL%2FOEvGoq0dabD%2BRvQ7d9FqFNrydShaYzog0EvLGIPeSHRqFzLAd0SukHVj7REXejXbL3B8vLsDmnSZcasaup3KLJQEt%2B8S2xA5EQI%2FWisJukipUIwRq5SvtFhs4T6HuuQjkGwkn1sGd57sArhUCuZW4nIcPakyCW7GFNOOBc%2FBaxeS1b6xlIRSbdgsW%2B7M%2B%2BCFCscVTWFr%2Bz08YeJG4voHPTYpXjWi6FUqjpJx4qnegXEUA2O2GgpzmzGfo3lbUDz5397HupLleR%2F6H7rbcllG56uRI8o4UUNtzhUcw8kdkGCj%2BHvQ8hG1Tb%2BeFJiG%2Fs7%2Fli53nqdgjWM6YLmtlpnTsST3jRkHhq%2B7HoBt%2FpfYwmoomCVYl5i0SdlqHu4gKvh4n0vu6QJShZ7IwMg6rnmCOcstl6FRSC%2BLc3go5o5pJyAGrK3tUlVdw%2Fqwnjnl0E1j3jBmPLhnB%2FkMxl3D3KTlSvJRPr6DwyRl0YbeJr9T%2FF7CXvQzXkDDz%2Fue8BjqkARuK7UovX1T1NcSh66OSTnhvzAttUTsDbIyN8aFmWxAPwKcy7QHJAA5NBdNNGObEZmFzNLGQ7GfINT31%2Bm4tXSkEwd6QPYapwgq5UKelAaxKrNBt2XctgzcmWmecgfVc5dj0cVZ1euo%2FM%2BPL7bh1096J%2BcYzybHMWlRZd9fdewD750p4ZHOz3M9iAdwiw1BQzSV1652VApCzIMcEMzEACQ5A%2BTqE&X-Amz-Signature=e64708ddb0b8a4e584f956b565aab7506a1c5e85569b06cef10d5c4dc3baedb8&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VYOXAGP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTHOIufyKwBzXWxId6TUvuy24BgbqIaL3FFKyFKHe8zgIhAJi4Q8%2F0i%2FZHg8y8FPhoSvS%2Bww1gweP%2BXHw69mjKLl%2B6KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwHkK3yrUfaG%2BuaEooq3AN9eJcBHWov7KzKU9uxX%2B1OwvtDgOAiMjtV7zHIGm298gCI486QjCjUN4ZxgwB7UlVo%2BR0CAqYqo4Fu9xoZV0eUvryhGdIj0Hrnd%2Bqi3qPaa8wJDcTTfCa2m0Ar%2FiFSKKeDm3pnsog8ElbZln5nRhOvQCkRaNgK3bXkfTa9OGqpvAaQb83EbBisOe0xX78xVaPcBN%2FEcsAq1kcUIivBC%2BkEN3gqRIVjy7Tizv%2BXacrgRLDnTTscTKd5vg9AfDzG4SZweM6%2FYMf1x42p5mcXqsCbfNbrxahh23C2zyffDxLLNfA3PV9qbv9w8bl%2F0Lqj4F%2F3elAIqiJd3jJZPgcSbzhITSGr457mIf%2F7jrVl1fFKPe9u5MgdKwHmPjzP3pwgqw3cy9IC8TVdxn8UutUnIyq5p9tatTtX4RaVTwYPw15FBJ7RWlgi8kDqL%2BckHbllHTO%2BXNrRk5U5W3RSnYmregpOWlizMaEaqgxTpuvepyjiRb5VJL6H70INcMFXQ%2FIvlxHf3U1l2ure2uIVlsH0TDu7H3GXbiFX5SBGDpK1l5kBcTAnybzGh9y5YM%2BG8Gyy78iO%2BzTTAoAgSbFwQOdog2%2FnU8VlUQ0eSwT%2Fyu8X1uamKSI2i7ML3eS3%2Fuew4DDB%2Fue8BjqkAcJbwBi3%2FKPNywu2mebtRA62NQ%2BSaJOZ%2Bb13zKK3s%2BXj%2Bl9A%2FtO1J%2FiCpq4SdZVGMB%2BrJIZjLm5QDJXiwe0gC9wtaFpzVHUP00Fhub8FRm568Stxl2EmswijGanf%2FGei%2B4eSQPYP3Uy73aL211JM%2BHuDv2RMtdUFp2kdI1iWjX6%2BGHETKd6OTIyWpweFCJLEjqM9f1VtEGaWaLEWx%2FC0xTfEAhIi&X-Amz-Signature=d9293d111bbdb1444125b5b5254a77ee4ab141ce6d7177d74de329722d5337c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMEIXNEB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxioIy%2F4xtje0adZQEcylqYeahE%2Fnsety0Qg8Es%2F7bzAIgaKvZD1ZLYmAy6%2F2OlPtPsDVCPANXVdwxl%2F%2Fn6F4S1PgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCo0dAO12glEKJ8OgircA3gKGl%2BMEOcg6ctvIriEVDucj55h0Porz6hR86B%2BuqkxVdIUhMPGqYO7CdP%2FwY7Us2v0F8TTmW3tHim%2BW5A8dItpgd2HtK1oeaTlLPTILF3RdzsfV71N%2FtVxWuae8zonLg%2BItbnznTa2nY7bV%2BJvyUZ%2FQHJCImmYuhTOXCuyIjMIiuVhyqCBf9ekFQXWhOPp8SchNOlSk1QMGNn3kB47AZci1vdb5B%2FlXHLBB4mXxQQrCO1L1nyksLgxRy8HtbveqXrOT2TGiDkTMq144ZcdcViRvUBbog4go6Q551cRg8GtoMLm4PfEkYXG3lxHN7YaQZGrgInDFVu7t19x3PtgwTfhqtWrFtagiVNpompayLvZSQzq0H4PstkG6bp6Wcah4tf6CTxuju8PEyIucCtyPH4UzK0EbrKShjIjso29sacfvC9DjMGzj2pKEDNKGTFExVQErkyl8I2Y0WVbLj1mWUswhSdA23EoJg8jZma03F2RQO3kAy1AJoLjTE66OYZPb5F9B6cg%2BTg%2F6p2NbjkhRyQSQCquQ3%2BHRh%2FCcfnYe4pduTyczWocXCV481XlbkBm39OsYU0LHeoQBDTce1EGzUq9hV9dh7PAVhJv43l7AWrD%2BAk7IfKrfSsUa8kCMIuA6LwGOqUBubAFiTQHLPnhzfBfA7rcKCpeFscy%2BZOeHBsWiwz%2BpV5P8aTfPaNf8%2FY4sZ%2FZROzbSse7h34dWQX8PC6ce3ZpUNHDvqAt35LdRE9fV6fLzT0M%2BNlflhyeuNaWUbE37yheIOm2DSJIq2Rh6N9YGtnsUIppBN%2Bd8HHO7g7WvOgBC%2BnMKQNPChjt6spJKQEjLNh2jpJv%2F0ArhsQS5T%2FZXh%2FkDqmpxCcX&X-Amz-Signature=bb572bc1707b3a4d28fe527c99b5182ceb956af09b7d2d40043e15f7cf58726f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMEIXNEB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxioIy%2F4xtje0adZQEcylqYeahE%2Fnsety0Qg8Es%2F7bzAIgaKvZD1ZLYmAy6%2F2OlPtPsDVCPANXVdwxl%2F%2Fn6F4S1PgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCo0dAO12glEKJ8OgircA3gKGl%2BMEOcg6ctvIriEVDucj55h0Porz6hR86B%2BuqkxVdIUhMPGqYO7CdP%2FwY7Us2v0F8TTmW3tHim%2BW5A8dItpgd2HtK1oeaTlLPTILF3RdzsfV71N%2FtVxWuae8zonLg%2BItbnznTa2nY7bV%2BJvyUZ%2FQHJCImmYuhTOXCuyIjMIiuVhyqCBf9ekFQXWhOPp8SchNOlSk1QMGNn3kB47AZci1vdb5B%2FlXHLBB4mXxQQrCO1L1nyksLgxRy8HtbveqXrOT2TGiDkTMq144ZcdcViRvUBbog4go6Q551cRg8GtoMLm4PfEkYXG3lxHN7YaQZGrgInDFVu7t19x3PtgwTfhqtWrFtagiVNpompayLvZSQzq0H4PstkG6bp6Wcah4tf6CTxuju8PEyIucCtyPH4UzK0EbrKShjIjso29sacfvC9DjMGzj2pKEDNKGTFExVQErkyl8I2Y0WVbLj1mWUswhSdA23EoJg8jZma03F2RQO3kAy1AJoLjTE66OYZPb5F9B6cg%2BTg%2F6p2NbjkhRyQSQCquQ3%2BHRh%2FCcfnYe4pduTyczWocXCV481XlbkBm39OsYU0LHeoQBDTce1EGzUq9hV9dh7PAVhJv43l7AWrD%2BAk7IfKrfSsUa8kCMIuA6LwGOqUBubAFiTQHLPnhzfBfA7rcKCpeFscy%2BZOeHBsWiwz%2BpV5P8aTfPaNf8%2FY4sZ%2FZROzbSse7h34dWQX8PC6ce3ZpUNHDvqAt35LdRE9fV6fLzT0M%2BNlflhyeuNaWUbE37yheIOm2DSJIq2Rh6N9YGtnsUIppBN%2Bd8HHO7g7WvOgBC%2BnMKQNPChjt6spJKQEjLNh2jpJv%2F0ArhsQS5T%2FZXh%2FkDqmpxCcX&X-Amz-Signature=ee7b49d1cb4719f6802560c8ace2dbbcd2eaca6410a2828d952d9c6ebb96b879&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMEIXNEB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxioIy%2F4xtje0adZQEcylqYeahE%2Fnsety0Qg8Es%2F7bzAIgaKvZD1ZLYmAy6%2F2OlPtPsDVCPANXVdwxl%2F%2Fn6F4S1PgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCo0dAO12glEKJ8OgircA3gKGl%2BMEOcg6ctvIriEVDucj55h0Porz6hR86B%2BuqkxVdIUhMPGqYO7CdP%2FwY7Us2v0F8TTmW3tHim%2BW5A8dItpgd2HtK1oeaTlLPTILF3RdzsfV71N%2FtVxWuae8zonLg%2BItbnznTa2nY7bV%2BJvyUZ%2FQHJCImmYuhTOXCuyIjMIiuVhyqCBf9ekFQXWhOPp8SchNOlSk1QMGNn3kB47AZci1vdb5B%2FlXHLBB4mXxQQrCO1L1nyksLgxRy8HtbveqXrOT2TGiDkTMq144ZcdcViRvUBbog4go6Q551cRg8GtoMLm4PfEkYXG3lxHN7YaQZGrgInDFVu7t19x3PtgwTfhqtWrFtagiVNpompayLvZSQzq0H4PstkG6bp6Wcah4tf6CTxuju8PEyIucCtyPH4UzK0EbrKShjIjso29sacfvC9DjMGzj2pKEDNKGTFExVQErkyl8I2Y0WVbLj1mWUswhSdA23EoJg8jZma03F2RQO3kAy1AJoLjTE66OYZPb5F9B6cg%2BTg%2F6p2NbjkhRyQSQCquQ3%2BHRh%2FCcfnYe4pduTyczWocXCV481XlbkBm39OsYU0LHeoQBDTce1EGzUq9hV9dh7PAVhJv43l7AWrD%2BAk7IfKrfSsUa8kCMIuA6LwGOqUBubAFiTQHLPnhzfBfA7rcKCpeFscy%2BZOeHBsWiwz%2BpV5P8aTfPaNf8%2FY4sZ%2FZROzbSse7h34dWQX8PC6ce3ZpUNHDvqAt35LdRE9fV6fLzT0M%2BNlflhyeuNaWUbE37yheIOm2DSJIq2Rh6N9YGtnsUIppBN%2Bd8HHO7g7WvOgBC%2BnMKQNPChjt6spJKQEjLNh2jpJv%2F0ArhsQS5T%2FZXh%2FkDqmpxCcX&X-Amz-Signature=b144568f25b1e91fd7b324f61da1fc8842e526115196622ed715fabcb751412b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBIZSVBR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH4tXta%2FbjsdHtaHyr%2F3xzkiYIuD3jfJTZeMqE28eQSjAiAuAN1bed2RdqcZNupwXMLMLl6ptszPwFhXYpRtHFq2SSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2P1QdBdDpvmchKKfKtwDYpsxmKzpyDbd9TB%2B2kVnrmm4Mk7%2BboAR6Sf7zlT%2FMXers7aGCqDy1QBnSmi5xzs%2FfxFz8y%2Fe7KNYYQKEA%2BNIA%2FcqCO6mykHF1UdQA4%2BFmdYIoU3hR03vYxhIO7aDxTRoUJnCkM2uZ3sXuEqRPehxLFle9whG48JeifRlyHSCD0s5yvNj%2BN79EbWyL8r4en9O97LRadx18gDwcqUeI8Bt4Yovi4OFb0DhI%2BR2ssL06%2FceLQHSXF%2F6uXEno2%2F%2FORadhZaBvsDlRF2cTJhP4rlCliXYrVZl5tR6qzLqL%2Fkb99M3oGzeWbivqL2c4i3I5ggZBLiWwZ1Px%2F3sZ5wjMv6qpNNE52OfbdVWfrO8aaACF6vcXxGT%2BCLg%2BUWyDEUTqAer9SOiOhi3Z6hbnReH6C6z2Y75QmgbSeGhhTqeQupIytMCydZN6%2FGEJe6qyEBnJlntuOdvMVntr8QhRni1lKWrccxnkngncH45FOwr036xE0PWanWKtcWrMg41XIkf2Wmy5%2BWCNBo%2BKE3cNAEqSdjYKljmv3m2HrcVj3NE0KaIppOfVbtxcA27otGQ1E9FnMy18gdqbzvCMae6gF%2BwAU4%2BOepZhR92Eh45Csr4MHlXQ3yoAX3SlfGS95ZZq6UwiYDovAY6pgGIzapOqKDQ6vX6c%2BsIXBWcAkMKZUHjkU5eIgVmox2wwTvyPX9inMPKqHLs0rqLfOnaoFnve81%2BO0r7geU6PtsblgCpGisvwFf4%2Bab30g4O%2FkSdLEPQa76%2BrzLGjao6WdZmKlxeepEIMYlj45PK9T5xVXKWZTa2RWllLY5VKcxlcjNE4EdrhL2pD9cX38EFjV9XIRtWqYSlVH%2BBtzPiT2%2FxfkmeQJkQ&X-Amz-Signature=b6f43b7ff0794a8374fcb55ee19ddc9e039b865c461ec639dd6fb5da82e8f3c9&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMK4A7N2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHj5wnl6ZJ5u3ojhQaL4VakpLzUbzP%2B8YcIFNcsuxuNAAiBSoGWqD%2BZQyyeDzjUuhV0Y1519whewQrRYTSqhgyi9HCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPhwJc6fbaC4RLG0lKtwD0uG%2BgxWB7ovmuRwpbkjOmNAm2QrnOUPZLFQwW4LRda1UtqXnL3aLDFbvekpt6Qjx7%2FldEGBYsPl%2Bm0VPIWtxeM5jGH7OcR94UGfxTEnKyRn6K0DWG%2FdVg7cFTCN6TrSzio8noy%2FwSTjR0NlG7f59njDm%2FtQvVUuv9FRUUAMCNKtjP1EilZHFhJjCeZuIKN3eKuwUcNWSz36qgnXiaeKrDni5rmVVQV5%2BlszJ6JRr3U5mOAXITnjPuxqxg9RezZVdWJb%2FfMs4Fhi9oEeHnwAUf8qB64TW5C%2FFwt0VFy5A0OMs%2F1H5Ua73g%2BtNv%2FhXGhybo5Che2gi0jT39w8Q%2BKp6SIF%2Fp0b%2BL%2BpxcuY3%2FAj06kxKd9%2B7IZ6ZtLal%2BaHThz5BLOqHlGWfv78lpTUib2yefluugb2vnSZaTqiCC0qH2d98MjLxHZEVrzGt0o0H0dt4JNZYx2yD6RQU2gNPj2Tpg0ZMMMRMgUPW%2BzUm6wki%2F2919x5tURZa1sX86%2B9lSjDKp5gDjKim3vxvEvvpOkg1%2FktXPQrCEOYDKZFGO%2Biroun3JnjxVcA4yQkhd%2FjSmXXZRc%2Fr2p5pM%2B%2FVlyvqd3E%2FGhsUE4dgGuLYUVXANhkJAKU16VQCm81CTeP2%2B04w7%2F7nvAY6pgG%2BmmHCU6oNpqo3fEGKeW4Qp4eSn%2BYdQayvE8or3KnWb1DksWvVBOfIMnqRMfIx2LuQrVmUbhO%2B%2FiH43d%2Blx%2BubUEmFX%2Brs1%2Fj8Ssw7wmui5Z%2BF4P%2FQzzhVU5dCw%2BpKmGN9NSBbPHo6yD3%2F%2FstPPT5kUTwQvQKMDxjId3d3kp7BShogA7ASWo6NjCrPhLkYvKzfFhwayPWZN%2FI7OitQQI3TtxJ%2Bxzja&X-Amz-Signature=43f859fe43ed6571533c358a1dbb4cc313e0f4b4b2d1b6d440c31eb94d089e52&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6NMVRTZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDqej5gcFhysQrUihlQ6s3y51mX5p90FsHNnXqTk2ebkAiBgplas2fnnGrTxBb%2F85av7PYpSoYt%2F6mtDV2k7LYiDsCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBaYTDHKghS8ll8QMKtwD%2FMYYBFspfL1UjfRR6A%2FGvLB%2FVR4z4yPVGb%2B08YvHlFH99Wt0b%2FaOnhRS2MNXOeKOJGRjcNf%2FALJnoV8SfZP26gRyEG2Azk0H4gUfdjrCB10StbKSJq1fOeaInZCf31dVxHjJtp%2F5IBCoh1xNqlFOIuzk5BgU31%2FPD87OLM%2Bb0s0pRBCK5Gjcv2l7Gsu08I%2Fht9BNWR%2FGZL1sj8Sgr%2FzG%2FXmKchA8aG5j8juQVh97%2BP4Kzb1tg35SbFToKSyvdATfO2tYpjgpsVZxcrYM224mJpVKTXRyu2FdPTzWP25wJcCFYQibPILyTUdZzzpliwKYKWrSkNKXdha9HZFAb%2BkflsXNDm8RLw%2FxsTkjFczObQB3ylmrdhTbrLVRzLUUC68jZvl3AzOSP9Ot9FdBBeTvtj7aI5RmN%2FQ7Ol1qA%2F1q8WQThgRvR5zYVsSErKDkZobk0ja4JQTKtdYFNhh2D0qP3LzA76D5V2fcFbsybEIE%2BQPhf1NefUc6RAgMcwivKKTeSbRCWf%2FVg3BgG%2B4M9NOQ9lF9DM05FkA0N0TCEoFK%2BlWj69%2FxQFJ7QNneAtaxiiOKozLxSrvnjMFuGm0WqAPEl1a3nJE8GeItnT5bNLKYw6klTmk14R3e87HBaOAwhP%2FnvAY6pgFvodFZGZflIXRaK67A5QDzFAtfOvwYqwOzQqg%2FI46m4J2yHnFprQC3Ug8oR2gLB28DLCJYCnS4xLBKwwXJO54q%2BI9ujuhfpwQm0Pw4FETNKcJPpUjeodXFA%2Bd87vqQID1AyC%2FFb%2BOoezKrGqdYifAFdOysoGhs8C%2Bhzg7e%2BB4QwxaHMgXk8r7A7rLdZ9A9IYMIBUp2S8cL0kyelqfJzObNHEAYpCzy&X-Amz-Signature=1d1f880fbcfff380cf334a548327d606401888c6cbaac69c8dcd337ed21bf996&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7AHFVN2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDFnLEMTGSs6rgkjfEVJm268v7MBJVsNEineSmxwIg9HAiEA5hBdSEkFNYFyj%2BKrNGtE7%2FL%2BQ7bzqvSVJBQ7L3giFKcqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIVCebinE1a%2B1ML8ICrcAx6%2BRdW%2FxF38wZX7l0Sd1tPJK0QNbp8gtf6pjtEctHue5IFZoLnm4evUmMMemo4g%2FAK946rSKrcNFwlAimJPoq7fkQ%2FKqyOz8UENpN8gp8q46PR9t4FSTBkbsTrs6Z76mGlItIjj%2FfZgI4oRbczPDX7RDqvyM06K1pxQLdsfMf7%2Bekj0ioahaUBe3CJOQzZSggrlvooL9NOTTvdFG1Hqz%2F%2BialNY%2BGSpy4FJVmm5KgVYaW85U1tqlXgRCI%2BPyC0TV3rjq56lOVSKkkJJSTcwvB0FDWOcRALlLb3CyBg8zu4Oyp%2FlZP76%2B9XEqOa1e9w23pe%2BAE%2B6ZmCMn5pWELntf7VlG%2Fdfk3Cxv6Q7OC%2BEQ%2FIZdr7cArw581BVH9R2jJsdgpiLoxpmLp5nFgRRlJANcEbkZ5RGx48oCOh1Wz6HAhbou297Z4fzAIxPXK6Z%2FbiNT59ew0ts3%2FA2UBuJhndhkfLlWABrfAVSkiQMeYZjkHAGQExCe5%2FoP%2BqNyW3tvI8jCdo3Kl8%2B1OruG0cAu8HqaS4si4V2GwJBeoXbxhUKWulVwLr8xhv6Q4PmOe28JyviWW4AHPi15yFLPPNjKC26CUwdzIFluNOeCqBe8fR1P%2FcYgPUS9qdR8d1AuPwgMNH%2B57wGOqUBwA6aRfswABMOjQu%2BW4OERjtsf%2BUa8YEIm0U2fEwDCad7I0wKhFqQrLHoN4Jm4YIzg8Z%2ByW0P%2FbgI3jmOYarjB%2BzZDbMAAdlHKGBcwhzlbLTUnAe8h5K2qEH%2BtUhj51tD5W%2BTLM3BoFXUY4kSLfwpXlo8mEacCOqYFdyrIbkEO3WwQ7e3a4piYPyq2KR%2FxSHJ2x%2FkGHTRuSwoQhLyVSZZJWsG%2B7EY&X-Amz-Signature=07a157bbdf85ee3cb67b20614e2ca33b4e24c5af8ddc575c3871b40153ea80fb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7AHFVN2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDFnLEMTGSs6rgkjfEVJm268v7MBJVsNEineSmxwIg9HAiEA5hBdSEkFNYFyj%2BKrNGtE7%2FL%2BQ7bzqvSVJBQ7L3giFKcqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIVCebinE1a%2B1ML8ICrcAx6%2BRdW%2FxF38wZX7l0Sd1tPJK0QNbp8gtf6pjtEctHue5IFZoLnm4evUmMMemo4g%2FAK946rSKrcNFwlAimJPoq7fkQ%2FKqyOz8UENpN8gp8q46PR9t4FSTBkbsTrs6Z76mGlItIjj%2FfZgI4oRbczPDX7RDqvyM06K1pxQLdsfMf7%2Bekj0ioahaUBe3CJOQzZSggrlvooL9NOTTvdFG1Hqz%2F%2BialNY%2BGSpy4FJVmm5KgVYaW85U1tqlXgRCI%2BPyC0TV3rjq56lOVSKkkJJSTcwvB0FDWOcRALlLb3CyBg8zu4Oyp%2FlZP76%2B9XEqOa1e9w23pe%2BAE%2B6ZmCMn5pWELntf7VlG%2Fdfk3Cxv6Q7OC%2BEQ%2FIZdr7cArw581BVH9R2jJsdgpiLoxpmLp5nFgRRlJANcEbkZ5RGx48oCOh1Wz6HAhbou297Z4fzAIxPXK6Z%2FbiNT59ew0ts3%2FA2UBuJhndhkfLlWABrfAVSkiQMeYZjkHAGQExCe5%2FoP%2BqNyW3tvI8jCdo3Kl8%2B1OruG0cAu8HqaS4si4V2GwJBeoXbxhUKWulVwLr8xhv6Q4PmOe28JyviWW4AHPi15yFLPPNjKC26CUwdzIFluNOeCqBe8fR1P%2FcYgPUS9qdR8d1AuPwgMNH%2B57wGOqUBwA6aRfswABMOjQu%2BW4OERjtsf%2BUa8YEIm0U2fEwDCad7I0wKhFqQrLHoN4Jm4YIzg8Z%2ByW0P%2FbgI3jmOYarjB%2BzZDbMAAdlHKGBcwhzlbLTUnAe8h5K2qEH%2BtUhj51tD5W%2BTLM3BoFXUY4kSLfwpXlo8mEacCOqYFdyrIbkEO3WwQ7e3a4piYPyq2KR%2FxSHJ2x%2FkGHTRuSwoQhLyVSZZJWsG%2B7EY&X-Amz-Signature=22ecb4e88ffdb4f3cb1c9b583c354f5605b05dfbe3a873601100aa5fb4dc8721&X-Amz-SignedHeaders=host&x-id=GetObject)

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
