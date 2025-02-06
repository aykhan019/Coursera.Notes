

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZU2SVQE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIA6qSmuwvdMoVtI8UO9HyjC3%2BjOKZQ0D1O9O0K5pRXciAiAekKRLmSVgxohTFFkm%2B0xGfWSIFpjPBsweMI807GxB6yr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIM3v7LJbuQWM3nFuleKtwDziWrfRtFziEEavSat4B07ujeYbhhVDwCIs%2Bdee%2B9IqsGLoeZxTQBH6w9sknv5WU2vhAiRJFotObMoEf1wQEIujYf3iK6pJsz1%2B0JjrzVB61EqtX9NVze0cDDBK4hDAmQCRRnrOL%2Bpobxp2S623ZJ0zWkKjZaplxclXfnBt%2Fsg0SOnI1yQT8sYdadoPIyXyawRk243ttTuNJf%2BZdxOvmrzTSZTQu5MyWDgFv%2FW0gfdXNS7QbeGEiiPo3ddQ%2BG3J8xqEnpEqZW8n5orwNBiLqT3TE39iPKK%2BcnPGFSgZulFZlq%2FrOqANmje5vafPVDsVr8NP1TDoHzR8p6ONLyjTwpl6KEmRM3a6KiqtGMxO0DocL5%2B2AIs0smqz75%2F4gqDd6XrQ1x%2Fq1NuFWQvT3V7M4YPvBMkXMS4LUAl%2BLnnCcgKU0C2%2Bs6BB1PamIneP9JS7HRj8p%2B9lQqe2X21bIdkp07sVhZiEjPZ4h4CL7cuxJMr4Umibh7N7fzF48bk3%2BwXrTxELOx%2B1gQAgU0dsnTwknLADrAMl%2FE13BtL5JuhNRgWHcJZU941n3iX1567n05GB8%2BZDFFUpP5Ak6SWbeTlDvfBgzZkzyXn%2B6y4Pz5mUjkA45jkbk07HHwsBiSa4Mw2eyRvQY6pgG8CPm84HuI9oA1%2B7HSSycnNP52uxghCwVfVqmJq7C%2Fg3QLn%2B1DekSlp8OIwI7FbQ3FNO0cp9SwxYSDHqP3kNMO8MkjzjH8Wn8IVjgWeEZQ%2Bs%2ByM8TMvwfSisY9seQYDe0%2FD%2FdOzw5bfOJ5UvxAP0LLWzqvqiA8m7RJGpwkJLvPgy2bdX996kpF892myNf0z4uY67dUj%2BEuUOBLNu3sZzskKqckVceG&X-Amz-Signature=8486a1f0e5e8a7f5a2f8be1778d7a9b6110ba89973fbc4ded08f8a7652c66eda&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZU2SVQE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIA6qSmuwvdMoVtI8UO9HyjC3%2BjOKZQ0D1O9O0K5pRXciAiAekKRLmSVgxohTFFkm%2B0xGfWSIFpjPBsweMI807GxB6yr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIM3v7LJbuQWM3nFuleKtwDziWrfRtFziEEavSat4B07ujeYbhhVDwCIs%2Bdee%2B9IqsGLoeZxTQBH6w9sknv5WU2vhAiRJFotObMoEf1wQEIujYf3iK6pJsz1%2B0JjrzVB61EqtX9NVze0cDDBK4hDAmQCRRnrOL%2Bpobxp2S623ZJ0zWkKjZaplxclXfnBt%2Fsg0SOnI1yQT8sYdadoPIyXyawRk243ttTuNJf%2BZdxOvmrzTSZTQu5MyWDgFv%2FW0gfdXNS7QbeGEiiPo3ddQ%2BG3J8xqEnpEqZW8n5orwNBiLqT3TE39iPKK%2BcnPGFSgZulFZlq%2FrOqANmje5vafPVDsVr8NP1TDoHzR8p6ONLyjTwpl6KEmRM3a6KiqtGMxO0DocL5%2B2AIs0smqz75%2F4gqDd6XrQ1x%2Fq1NuFWQvT3V7M4YPvBMkXMS4LUAl%2BLnnCcgKU0C2%2Bs6BB1PamIneP9JS7HRj8p%2B9lQqe2X21bIdkp07sVhZiEjPZ4h4CL7cuxJMr4Umibh7N7fzF48bk3%2BwXrTxELOx%2B1gQAgU0dsnTwknLADrAMl%2FE13BtL5JuhNRgWHcJZU941n3iX1567n05GB8%2BZDFFUpP5Ak6SWbeTlDvfBgzZkzyXn%2B6y4Pz5mUjkA45jkbk07HHwsBiSa4Mw2eyRvQY6pgG8CPm84HuI9oA1%2B7HSSycnNP52uxghCwVfVqmJq7C%2Fg3QLn%2B1DekSlp8OIwI7FbQ3FNO0cp9SwxYSDHqP3kNMO8MkjzjH8Wn8IVjgWeEZQ%2Bs%2ByM8TMvwfSisY9seQYDe0%2FD%2FdOzw5bfOJ5UvxAP0LLWzqvqiA8m7RJGpwkJLvPgy2bdX996kpF892myNf0z4uY67dUj%2BEuUOBLNu3sZzskKqckVceG&X-Amz-Signature=47bcbf1bac9cbda9449690e31c6a691b93f88dd0ddb8a519c8d3242a521087aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZU2SVQE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIA6qSmuwvdMoVtI8UO9HyjC3%2BjOKZQ0D1O9O0K5pRXciAiAekKRLmSVgxohTFFkm%2B0xGfWSIFpjPBsweMI807GxB6yr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIM3v7LJbuQWM3nFuleKtwDziWrfRtFziEEavSat4B07ujeYbhhVDwCIs%2Bdee%2B9IqsGLoeZxTQBH6w9sknv5WU2vhAiRJFotObMoEf1wQEIujYf3iK6pJsz1%2B0JjrzVB61EqtX9NVze0cDDBK4hDAmQCRRnrOL%2Bpobxp2S623ZJ0zWkKjZaplxclXfnBt%2Fsg0SOnI1yQT8sYdadoPIyXyawRk243ttTuNJf%2BZdxOvmrzTSZTQu5MyWDgFv%2FW0gfdXNS7QbeGEiiPo3ddQ%2BG3J8xqEnpEqZW8n5orwNBiLqT3TE39iPKK%2BcnPGFSgZulFZlq%2FrOqANmje5vafPVDsVr8NP1TDoHzR8p6ONLyjTwpl6KEmRM3a6KiqtGMxO0DocL5%2B2AIs0smqz75%2F4gqDd6XrQ1x%2Fq1NuFWQvT3V7M4YPvBMkXMS4LUAl%2BLnnCcgKU0C2%2Bs6BB1PamIneP9JS7HRj8p%2B9lQqe2X21bIdkp07sVhZiEjPZ4h4CL7cuxJMr4Umibh7N7fzF48bk3%2BwXrTxELOx%2B1gQAgU0dsnTwknLADrAMl%2FE13BtL5JuhNRgWHcJZU941n3iX1567n05GB8%2BZDFFUpP5Ak6SWbeTlDvfBgzZkzyXn%2B6y4Pz5mUjkA45jkbk07HHwsBiSa4Mw2eyRvQY6pgG8CPm84HuI9oA1%2B7HSSycnNP52uxghCwVfVqmJq7C%2Fg3QLn%2B1DekSlp8OIwI7FbQ3FNO0cp9SwxYSDHqP3kNMO8MkjzjH8Wn8IVjgWeEZQ%2Bs%2ByM8TMvwfSisY9seQYDe0%2FD%2FdOzw5bfOJ5UvxAP0LLWzqvqiA8m7RJGpwkJLvPgy2bdX996kpF892myNf0z4uY67dUj%2BEuUOBLNu3sZzskKqckVceG&X-Amz-Signature=538db1d47591d820b9d7b47dc09837f70f7b54225b54e097c75ab81dfc70cb96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666NKX5LI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPHdz77aDps7TMrBmnjXeVfYKuFPiD5mz%2BSRkL8zw4KgIhAMw58xUOxSqr7DqwJT9RhluF9WqkdWQgR4miVkXXk5%2FxKv8DCFoQABoMNjM3NDIzMTgzODA1Igwk%2Byks6ANNAhL0yNAq3AONMVO9h3TL3bPkadcxSP79WvMZaq%2BF%2BHfNWIphLM5EXq0RezsJsRlypaswZYP2ZjwPIjfqDC8HA2FGZfrPTPD4X0VL22J6Qip1qc231Z%2F5wxIB9m9ucgASxLLJYnOcEXNrbBCW0%2BkjRMwkIbk%2FsCInshb7NZWvDBlI6pln2%2BlpnIVdIUcI7ubr%2FMKN6xijAkK6rM4FP5S8LcgiUlCFWi%2B9Z2uXlXvTZgo41o4nmezBiYurVkfi0gTA8XFUifOdx6vLoOBWsGyVQ2aYufgy%2BG%2FWf3ywIlVf8HJEy1VYLrlcNwPmRYXTjValEa43Qqc66ndlzIhv8A6ffNgtLuVQemS0YnLgXJ8WTO4lm1m%2ByqNyalAHm7fCnVV%2BOmyVdkuU74rFhAsFEvcQWdedlF1MXxzxIW%2FQOYeNItpyS3pOcgLDS38bx6WnkdTEf10C0%2FinAeG7zjx4iZSnri0%2BHhMzBdEi2mMBhgBM7c9n4QYVLMD5kS9%2FH2I3nOdXEwydiv6gfdbHabkET9pGU8d79HxbGhLrwXSeiop%2B6Vevzg%2FulcQhVq5cus%2B71863QzcWDHeDdL6I2KWTeN%2Ban%2BubFnoxSWzpistb0aX%2Fxyc5a2W%2FLQ1sH%2BYPKINjvDNvccyw3TCt7JG9BjqkAYCguH849yJLxm2EHI7n1YRR%2Fw5XfbXh73v9KAVIKHKoS2MRXQcC4EXCNW71kkoUhVkBqRcqKKXbVm3%2BvJA4Ot8NzTZ7sqWot0%2FVwt%2Fn17lVU5maqQNSskiOeacMs13vPNGPQBgbDDKum4mjjalzANmdGcsbDQCwOZNbhJhpNcrGvbzQYKqBSBqp05h1DLC%2FV1T2ZfH%2Fref6iKlqwPwIsAn8dpNN&X-Amz-Signature=3adfa87394d72e4b46e782b2a0c68ddb63fb6c20ef3314ed9af7c346a5e2afc5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666NKX5LI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPHdz77aDps7TMrBmnjXeVfYKuFPiD5mz%2BSRkL8zw4KgIhAMw58xUOxSqr7DqwJT9RhluF9WqkdWQgR4miVkXXk5%2FxKv8DCFoQABoMNjM3NDIzMTgzODA1Igwk%2Byks6ANNAhL0yNAq3AONMVO9h3TL3bPkadcxSP79WvMZaq%2BF%2BHfNWIphLM5EXq0RezsJsRlypaswZYP2ZjwPIjfqDC8HA2FGZfrPTPD4X0VL22J6Qip1qc231Z%2F5wxIB9m9ucgASxLLJYnOcEXNrbBCW0%2BkjRMwkIbk%2FsCInshb7NZWvDBlI6pln2%2BlpnIVdIUcI7ubr%2FMKN6xijAkK6rM4FP5S8LcgiUlCFWi%2B9Z2uXlXvTZgo41o4nmezBiYurVkfi0gTA8XFUifOdx6vLoOBWsGyVQ2aYufgy%2BG%2FWf3ywIlVf8HJEy1VYLrlcNwPmRYXTjValEa43Qqc66ndlzIhv8A6ffNgtLuVQemS0YnLgXJ8WTO4lm1m%2ByqNyalAHm7fCnVV%2BOmyVdkuU74rFhAsFEvcQWdedlF1MXxzxIW%2FQOYeNItpyS3pOcgLDS38bx6WnkdTEf10C0%2FinAeG7zjx4iZSnri0%2BHhMzBdEi2mMBhgBM7c9n4QYVLMD5kS9%2FH2I3nOdXEwydiv6gfdbHabkET9pGU8d79HxbGhLrwXSeiop%2B6Vevzg%2FulcQhVq5cus%2B71863QzcWDHeDdL6I2KWTeN%2Ban%2BubFnoxSWzpistb0aX%2Fxyc5a2W%2FLQ1sH%2BYPKINjvDNvccyw3TCt7JG9BjqkAYCguH849yJLxm2EHI7n1YRR%2Fw5XfbXh73v9KAVIKHKoS2MRXQcC4EXCNW71kkoUhVkBqRcqKKXbVm3%2BvJA4Ot8NzTZ7sqWot0%2FVwt%2Fn17lVU5maqQNSskiOeacMs13vPNGPQBgbDDKum4mjjalzANmdGcsbDQCwOZNbhJhpNcrGvbzQYKqBSBqp05h1DLC%2FV1T2ZfH%2Fref6iKlqwPwIsAn8dpNN&X-Amz-Signature=13555fff16d6891552821c0370470d01a49bf7b16e8e65ec32c9222409dd12dd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666NKX5LI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPHdz77aDps7TMrBmnjXeVfYKuFPiD5mz%2BSRkL8zw4KgIhAMw58xUOxSqr7DqwJT9RhluF9WqkdWQgR4miVkXXk5%2FxKv8DCFoQABoMNjM3NDIzMTgzODA1Igwk%2Byks6ANNAhL0yNAq3AONMVO9h3TL3bPkadcxSP79WvMZaq%2BF%2BHfNWIphLM5EXq0RezsJsRlypaswZYP2ZjwPIjfqDC8HA2FGZfrPTPD4X0VL22J6Qip1qc231Z%2F5wxIB9m9ucgASxLLJYnOcEXNrbBCW0%2BkjRMwkIbk%2FsCInshb7NZWvDBlI6pln2%2BlpnIVdIUcI7ubr%2FMKN6xijAkK6rM4FP5S8LcgiUlCFWi%2B9Z2uXlXvTZgo41o4nmezBiYurVkfi0gTA8XFUifOdx6vLoOBWsGyVQ2aYufgy%2BG%2FWf3ywIlVf8HJEy1VYLrlcNwPmRYXTjValEa43Qqc66ndlzIhv8A6ffNgtLuVQemS0YnLgXJ8WTO4lm1m%2ByqNyalAHm7fCnVV%2BOmyVdkuU74rFhAsFEvcQWdedlF1MXxzxIW%2FQOYeNItpyS3pOcgLDS38bx6WnkdTEf10C0%2FinAeG7zjx4iZSnri0%2BHhMzBdEi2mMBhgBM7c9n4QYVLMD5kS9%2FH2I3nOdXEwydiv6gfdbHabkET9pGU8d79HxbGhLrwXSeiop%2B6Vevzg%2FulcQhVq5cus%2B71863QzcWDHeDdL6I2KWTeN%2Ban%2BubFnoxSWzpistb0aX%2Fxyc5a2W%2FLQ1sH%2BYPKINjvDNvccyw3TCt7JG9BjqkAYCguH849yJLxm2EHI7n1YRR%2Fw5XfbXh73v9KAVIKHKoS2MRXQcC4EXCNW71kkoUhVkBqRcqKKXbVm3%2BvJA4Ot8NzTZ7sqWot0%2FVwt%2Fn17lVU5maqQNSskiOeacMs13vPNGPQBgbDDKum4mjjalzANmdGcsbDQCwOZNbhJhpNcrGvbzQYKqBSBqp05h1DLC%2FV1T2ZfH%2Fref6iKlqwPwIsAn8dpNN&X-Amz-Signature=3eac61e60290a18ae8c4c5bd53ad839d5117ce178fec8f83ee37329ff15f7903&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666NKX5LI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPHdz77aDps7TMrBmnjXeVfYKuFPiD5mz%2BSRkL8zw4KgIhAMw58xUOxSqr7DqwJT9RhluF9WqkdWQgR4miVkXXk5%2FxKv8DCFoQABoMNjM3NDIzMTgzODA1Igwk%2Byks6ANNAhL0yNAq3AONMVO9h3TL3bPkadcxSP79WvMZaq%2BF%2BHfNWIphLM5EXq0RezsJsRlypaswZYP2ZjwPIjfqDC8HA2FGZfrPTPD4X0VL22J6Qip1qc231Z%2F5wxIB9m9ucgASxLLJYnOcEXNrbBCW0%2BkjRMwkIbk%2FsCInshb7NZWvDBlI6pln2%2BlpnIVdIUcI7ubr%2FMKN6xijAkK6rM4FP5S8LcgiUlCFWi%2B9Z2uXlXvTZgo41o4nmezBiYurVkfi0gTA8XFUifOdx6vLoOBWsGyVQ2aYufgy%2BG%2FWf3ywIlVf8HJEy1VYLrlcNwPmRYXTjValEa43Qqc66ndlzIhv8A6ffNgtLuVQemS0YnLgXJ8WTO4lm1m%2ByqNyalAHm7fCnVV%2BOmyVdkuU74rFhAsFEvcQWdedlF1MXxzxIW%2FQOYeNItpyS3pOcgLDS38bx6WnkdTEf10C0%2FinAeG7zjx4iZSnri0%2BHhMzBdEi2mMBhgBM7c9n4QYVLMD5kS9%2FH2I3nOdXEwydiv6gfdbHabkET9pGU8d79HxbGhLrwXSeiop%2B6Vevzg%2FulcQhVq5cus%2B71863QzcWDHeDdL6I2KWTeN%2Ban%2BubFnoxSWzpistb0aX%2Fxyc5a2W%2FLQ1sH%2BYPKINjvDNvccyw3TCt7JG9BjqkAYCguH849yJLxm2EHI7n1YRR%2Fw5XfbXh73v9KAVIKHKoS2MRXQcC4EXCNW71kkoUhVkBqRcqKKXbVm3%2BvJA4Ot8NzTZ7sqWot0%2FVwt%2Fn17lVU5maqQNSskiOeacMs13vPNGPQBgbDDKum4mjjalzANmdGcsbDQCwOZNbhJhpNcrGvbzQYKqBSBqp05h1DLC%2FV1T2ZfH%2Fref6iKlqwPwIsAn8dpNN&X-Amz-Signature=c41be0f3c64b6e3773eadb475f5693b29a010d048e478208f826d8005c2f8918&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666NKX5LI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPHdz77aDps7TMrBmnjXeVfYKuFPiD5mz%2BSRkL8zw4KgIhAMw58xUOxSqr7DqwJT9RhluF9WqkdWQgR4miVkXXk5%2FxKv8DCFoQABoMNjM3NDIzMTgzODA1Igwk%2Byks6ANNAhL0yNAq3AONMVO9h3TL3bPkadcxSP79WvMZaq%2BF%2BHfNWIphLM5EXq0RezsJsRlypaswZYP2ZjwPIjfqDC8HA2FGZfrPTPD4X0VL22J6Qip1qc231Z%2F5wxIB9m9ucgASxLLJYnOcEXNrbBCW0%2BkjRMwkIbk%2FsCInshb7NZWvDBlI6pln2%2BlpnIVdIUcI7ubr%2FMKN6xijAkK6rM4FP5S8LcgiUlCFWi%2B9Z2uXlXvTZgo41o4nmezBiYurVkfi0gTA8XFUifOdx6vLoOBWsGyVQ2aYufgy%2BG%2FWf3ywIlVf8HJEy1VYLrlcNwPmRYXTjValEa43Qqc66ndlzIhv8A6ffNgtLuVQemS0YnLgXJ8WTO4lm1m%2ByqNyalAHm7fCnVV%2BOmyVdkuU74rFhAsFEvcQWdedlF1MXxzxIW%2FQOYeNItpyS3pOcgLDS38bx6WnkdTEf10C0%2FinAeG7zjx4iZSnri0%2BHhMzBdEi2mMBhgBM7c9n4QYVLMD5kS9%2FH2I3nOdXEwydiv6gfdbHabkET9pGU8d79HxbGhLrwXSeiop%2B6Vevzg%2FulcQhVq5cus%2B71863QzcWDHeDdL6I2KWTeN%2Ban%2BubFnoxSWzpistb0aX%2Fxyc5a2W%2FLQ1sH%2BYPKINjvDNvccyw3TCt7JG9BjqkAYCguH849yJLxm2EHI7n1YRR%2Fw5XfbXh73v9KAVIKHKoS2MRXQcC4EXCNW71kkoUhVkBqRcqKKXbVm3%2BvJA4Ot8NzTZ7sqWot0%2FVwt%2Fn17lVU5maqQNSskiOeacMs13vPNGPQBgbDDKum4mjjalzANmdGcsbDQCwOZNbhJhpNcrGvbzQYKqBSBqp05h1DLC%2FV1T2ZfH%2Fref6iKlqwPwIsAn8dpNN&X-Amz-Signature=e42e20ccc000dc5314e343bb8d804b090b628ac4fdcfd0b66d0b46ed83f202e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666NKX5LI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPHdz77aDps7TMrBmnjXeVfYKuFPiD5mz%2BSRkL8zw4KgIhAMw58xUOxSqr7DqwJT9RhluF9WqkdWQgR4miVkXXk5%2FxKv8DCFoQABoMNjM3NDIzMTgzODA1Igwk%2Byks6ANNAhL0yNAq3AONMVO9h3TL3bPkadcxSP79WvMZaq%2BF%2BHfNWIphLM5EXq0RezsJsRlypaswZYP2ZjwPIjfqDC8HA2FGZfrPTPD4X0VL22J6Qip1qc231Z%2F5wxIB9m9ucgASxLLJYnOcEXNrbBCW0%2BkjRMwkIbk%2FsCInshb7NZWvDBlI6pln2%2BlpnIVdIUcI7ubr%2FMKN6xijAkK6rM4FP5S8LcgiUlCFWi%2B9Z2uXlXvTZgo41o4nmezBiYurVkfi0gTA8XFUifOdx6vLoOBWsGyVQ2aYufgy%2BG%2FWf3ywIlVf8HJEy1VYLrlcNwPmRYXTjValEa43Qqc66ndlzIhv8A6ffNgtLuVQemS0YnLgXJ8WTO4lm1m%2ByqNyalAHm7fCnVV%2BOmyVdkuU74rFhAsFEvcQWdedlF1MXxzxIW%2FQOYeNItpyS3pOcgLDS38bx6WnkdTEf10C0%2FinAeG7zjx4iZSnri0%2BHhMzBdEi2mMBhgBM7c9n4QYVLMD5kS9%2FH2I3nOdXEwydiv6gfdbHabkET9pGU8d79HxbGhLrwXSeiop%2B6Vevzg%2FulcQhVq5cus%2B71863QzcWDHeDdL6I2KWTeN%2Ban%2BubFnoxSWzpistb0aX%2Fxyc5a2W%2FLQ1sH%2BYPKINjvDNvccyw3TCt7JG9BjqkAYCguH849yJLxm2EHI7n1YRR%2Fw5XfbXh73v9KAVIKHKoS2MRXQcC4EXCNW71kkoUhVkBqRcqKKXbVm3%2BvJA4Ot8NzTZ7sqWot0%2FVwt%2Fn17lVU5maqQNSskiOeacMs13vPNGPQBgbDDKum4mjjalzANmdGcsbDQCwOZNbhJhpNcrGvbzQYKqBSBqp05h1DLC%2FV1T2ZfH%2Fref6iKlqwPwIsAn8dpNN&X-Amz-Signature=23d04659da974808dfc88b3b9cffe267151968285eec4cd46b18eafdf3a5e1a1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XMKT3VD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQC%2B7yVCjGtBpN5PsMqY2LWoJLXqJytve9WiXAn%2BYfswrQIhAJJftv%2Fq7yEFrezjI8GaMZpDPlTnQ6Yu06i0DsgQCXueKv8DCFoQABoMNjM3NDIzMTgzODA1Igy2n7F7LnEgPs6ZDIMq3AOx9mOGRqChMUFz8asm1aQisiLP4q4PSsvP5MVMwVVZXlSJA2eOM0AnIdL1fXjELuHRuFF10to5EDspNCUBa6IOZoKt5hZTTWI4ykfYcFHRzXYd5UVOkwidFaBQ9RxsiTh0DRBmAJt88ky%2BYAu8PjPyP2OdTUH7GAgOwvmnYbOL%2FaYVQPx%2F6Pq6wmEk%2FtEskfjyeCqgmZ1P281fAGyQbJzY118M5EuJnNjjCqV2pLtQeFViuIGUgGil%2BdUjhtpR6fUgHqpvk097n8JMqS5y6hlLIa8MVLfAz0xRMF0VJlwaZ0af6JW%2FQjmzwXfUK8S%2FxvHmtQKqVIiHKmEIQPKsyWC3irXO9B7SVUyJ3Lcj3ii1DRb40ViOsxpIv2ubmjSdslvMVlQNwy8L1JXpAClFFASZGG%2F1fQSFv5ji24MDxsPzOxdQIjI2Mxtla649JUH9K3qCqJa84zfVuBwnydJYAaaxkL7qVQSnhIUMQEHdtzK7z7rhIU4SzxUnilnO9KBlYngYzjJjB7LWIrJcX1%2FBUojSuWVpSYcvqZ1DBufo4n%2BZ%2F4qBEoJGCxZ5NxKQCk5sdpvmcrujeGD4a5Nc7FPetKeZ5RPgJfiIL%2BHCbF3WMMHxF24E1AP0C1qmLJ2n7TDX65G9BjqkASFaklEg9AjmWCqxOBJZM7JXY9xgL%2B%2Ftb%2F%2FrzNzrpO8Z9LL0OB0zVnnBVWcxgRS7I81xOK0QsDqqHCWl8Ha03NS0ACTUQ6fpE%2BvcoAH24%2FhOHWo%2FVWONoG0Giw9Sui4NHmyCb0zrOyHTk92ZsDAV93pRBzRQLElyQd8Y5ifX3HJZkdXFKFiRsK9MEt2HKGh2YYzTfJWBI4knzs9qiRJXohRZdTSF&X-Amz-Signature=adfbc38d48bf55800b3f0f8dd28fb2ac19f758ac34ce978ce9155e56a4b5a96d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UX4WEXV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFI41kzxS7F0PWdi9HWobfR1Jp4UOPwEq7gi2YQikvbsAiBw9%2BnGAhnnjtraGiVIeMnktKmZSvHRV7i3IakbfWdWnyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMvzvk7tRZMvlgt1XrKtwDwEJfwrNOgu7Y%2BgYd6y4CQGjdRfWSv%2F7kVEtAV8w4nN2jHweLBHQHNt8bDUFRJKFb2JwyhdVVBVhWLIgcRxXBIbyinNYMHwoKJ5%2FGuQYmFSMBMN4wcF%2BqV9YtLSD44%2BOskMWls5Ki7AcbK5X4a6hd4wjkuGoJ%2BFfvGD%2F2OHzMHZerZd0NxKk8htxQwB0obALWiVsYyWiHCvJFbWttn1ve8t9h%2FdEF4dzwO2URDQJf12FeUJ58ojBgzbT0mUv0xDb7v7nNFRtihy40Lxnh%2BKzAjc3uEJNXIoZrngho%2BHCx1KRfGByWBLTQULL3pi56s3TfrsY9sCy%2B3rI5HkCL9pWefoehHzUVCzr9gfOLgUgeC9%2BHtOqKqB3ZDKm3SaolcIePLYPZpXFdADCL0p5hiIlef7EnQaG8POhJJqsbvZfeiMFAb3X6nLqm4gqeyZAx8wVhLLdhhQNzdQtotiJ%2BSKZCfa5owY1FAZLQMB64CnfOTJXFqkAnmRm8go1i8nkI5KOwVbahkVGhsvu8m3rML%2FjBpVkm6w2iYaQTF1xVzsZMt6wR38uIPgpGgrQxYwYFtxeayV%2BwJAS3LbVMdlnlDRmouQQVZzKBWBIPY5pmC8pO%2B%2FhybwA3K84p8kiC4q8woeyRvQY6pgFRi8rFqyuLJu6RXz7dE59902fp6MLyGZnGaHx1tgGZgd5Qjpt8D%2BwotaJ5AblgZkPP79xCp1dEHJzrxIhHbx57w17kruAvQWIWLTjw05FZvIMczGxI0Gg9YrPo864BIvW9pwh0RUiCgbBDhIioja%2FjVtE7a4r%2BlkiCQAGE9IF%2Fl6smER0qgLhsW5YV0gmE6D4FmtLp2KwvgVE1Yn%2FBvwRIDFYwzoJ5&X-Amz-Signature=438f7fc701561bcd656ecf11bc0405f768f5ace2e24fb38712f639f78e14bc2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666NKX5LI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPHdz77aDps7TMrBmnjXeVfYKuFPiD5mz%2BSRkL8zw4KgIhAMw58xUOxSqr7DqwJT9RhluF9WqkdWQgR4miVkXXk5%2FxKv8DCFoQABoMNjM3NDIzMTgzODA1Igwk%2Byks6ANNAhL0yNAq3AONMVO9h3TL3bPkadcxSP79WvMZaq%2BF%2BHfNWIphLM5EXq0RezsJsRlypaswZYP2ZjwPIjfqDC8HA2FGZfrPTPD4X0VL22J6Qip1qc231Z%2F5wxIB9m9ucgASxLLJYnOcEXNrbBCW0%2BkjRMwkIbk%2FsCInshb7NZWvDBlI6pln2%2BlpnIVdIUcI7ubr%2FMKN6xijAkK6rM4FP5S8LcgiUlCFWi%2B9Z2uXlXvTZgo41o4nmezBiYurVkfi0gTA8XFUifOdx6vLoOBWsGyVQ2aYufgy%2BG%2FWf3ywIlVf8HJEy1VYLrlcNwPmRYXTjValEa43Qqc66ndlzIhv8A6ffNgtLuVQemS0YnLgXJ8WTO4lm1m%2ByqNyalAHm7fCnVV%2BOmyVdkuU74rFhAsFEvcQWdedlF1MXxzxIW%2FQOYeNItpyS3pOcgLDS38bx6WnkdTEf10C0%2FinAeG7zjx4iZSnri0%2BHhMzBdEi2mMBhgBM7c9n4QYVLMD5kS9%2FH2I3nOdXEwydiv6gfdbHabkET9pGU8d79HxbGhLrwXSeiop%2B6Vevzg%2FulcQhVq5cus%2B71863QzcWDHeDdL6I2KWTeN%2Ban%2BubFnoxSWzpistb0aX%2Fxyc5a2W%2FLQ1sH%2BYPKINjvDNvccyw3TCt7JG9BjqkAYCguH849yJLxm2EHI7n1YRR%2Fw5XfbXh73v9KAVIKHKoS2MRXQcC4EXCNW71kkoUhVkBqRcqKKXbVm3%2BvJA4Ot8NzTZ7sqWot0%2FVwt%2Fn17lVU5maqQNSskiOeacMs13vPNGPQBgbDDKum4mjjalzANmdGcsbDQCwOZNbhJhpNcrGvbzQYKqBSBqp05h1DLC%2FV1T2ZfH%2Fref6iKlqwPwIsAn8dpNN&X-Amz-Signature=e73db27d61b056fc440425d35e462c212c621da254b362033fae7bd38d0893e4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666NKX5LI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPHdz77aDps7TMrBmnjXeVfYKuFPiD5mz%2BSRkL8zw4KgIhAMw58xUOxSqr7DqwJT9RhluF9WqkdWQgR4miVkXXk5%2FxKv8DCFoQABoMNjM3NDIzMTgzODA1Igwk%2Byks6ANNAhL0yNAq3AONMVO9h3TL3bPkadcxSP79WvMZaq%2BF%2BHfNWIphLM5EXq0RezsJsRlypaswZYP2ZjwPIjfqDC8HA2FGZfrPTPD4X0VL22J6Qip1qc231Z%2F5wxIB9m9ucgASxLLJYnOcEXNrbBCW0%2BkjRMwkIbk%2FsCInshb7NZWvDBlI6pln2%2BlpnIVdIUcI7ubr%2FMKN6xijAkK6rM4FP5S8LcgiUlCFWi%2B9Z2uXlXvTZgo41o4nmezBiYurVkfi0gTA8XFUifOdx6vLoOBWsGyVQ2aYufgy%2BG%2FWf3ywIlVf8HJEy1VYLrlcNwPmRYXTjValEa43Qqc66ndlzIhv8A6ffNgtLuVQemS0YnLgXJ8WTO4lm1m%2ByqNyalAHm7fCnVV%2BOmyVdkuU74rFhAsFEvcQWdedlF1MXxzxIW%2FQOYeNItpyS3pOcgLDS38bx6WnkdTEf10C0%2FinAeG7zjx4iZSnri0%2BHhMzBdEi2mMBhgBM7c9n4QYVLMD5kS9%2FH2I3nOdXEwydiv6gfdbHabkET9pGU8d79HxbGhLrwXSeiop%2B6Vevzg%2FulcQhVq5cus%2B71863QzcWDHeDdL6I2KWTeN%2Ban%2BubFnoxSWzpistb0aX%2Fxyc5a2W%2FLQ1sH%2BYPKINjvDNvccyw3TCt7JG9BjqkAYCguH849yJLxm2EHI7n1YRR%2Fw5XfbXh73v9KAVIKHKoS2MRXQcC4EXCNW71kkoUhVkBqRcqKKXbVm3%2BvJA4Ot8NzTZ7sqWot0%2FVwt%2Fn17lVU5maqQNSskiOeacMs13vPNGPQBgbDDKum4mjjalzANmdGcsbDQCwOZNbhJhpNcrGvbzQYKqBSBqp05h1DLC%2FV1T2ZfH%2Fref6iKlqwPwIsAn8dpNN&X-Amz-Signature=c35270835792767bf04fb0b5997edf9dc2f83a200b539075d96e05902cc03058&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666NKX5LI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCPHdz77aDps7TMrBmnjXeVfYKuFPiD5mz%2BSRkL8zw4KgIhAMw58xUOxSqr7DqwJT9RhluF9WqkdWQgR4miVkXXk5%2FxKv8DCFoQABoMNjM3NDIzMTgzODA1Igwk%2Byks6ANNAhL0yNAq3AONMVO9h3TL3bPkadcxSP79WvMZaq%2BF%2BHfNWIphLM5EXq0RezsJsRlypaswZYP2ZjwPIjfqDC8HA2FGZfrPTPD4X0VL22J6Qip1qc231Z%2F5wxIB9m9ucgASxLLJYnOcEXNrbBCW0%2BkjRMwkIbk%2FsCInshb7NZWvDBlI6pln2%2BlpnIVdIUcI7ubr%2FMKN6xijAkK6rM4FP5S8LcgiUlCFWi%2B9Z2uXlXvTZgo41o4nmezBiYurVkfi0gTA8XFUifOdx6vLoOBWsGyVQ2aYufgy%2BG%2FWf3ywIlVf8HJEy1VYLrlcNwPmRYXTjValEa43Qqc66ndlzIhv8A6ffNgtLuVQemS0YnLgXJ8WTO4lm1m%2ByqNyalAHm7fCnVV%2BOmyVdkuU74rFhAsFEvcQWdedlF1MXxzxIW%2FQOYeNItpyS3pOcgLDS38bx6WnkdTEf10C0%2FinAeG7zjx4iZSnri0%2BHhMzBdEi2mMBhgBM7c9n4QYVLMD5kS9%2FH2I3nOdXEwydiv6gfdbHabkET9pGU8d79HxbGhLrwXSeiop%2B6Vevzg%2FulcQhVq5cus%2B71863QzcWDHeDdL6I2KWTeN%2Ban%2BubFnoxSWzpistb0aX%2Fxyc5a2W%2FLQ1sH%2BYPKINjvDNvccyw3TCt7JG9BjqkAYCguH849yJLxm2EHI7n1YRR%2Fw5XfbXh73v9KAVIKHKoS2MRXQcC4EXCNW71kkoUhVkBqRcqKKXbVm3%2BvJA4Ot8NzTZ7sqWot0%2FVwt%2Fn17lVU5maqQNSskiOeacMs13vPNGPQBgbDDKum4mjjalzANmdGcsbDQCwOZNbhJhpNcrGvbzQYKqBSBqp05h1DLC%2FV1T2ZfH%2Fref6iKlqwPwIsAn8dpNN&X-Amz-Signature=59c7f497c26d46451bca624a8ed08ac5d3dd923c15a1142399c99bd6360edd3c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDKKYIWN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQD3IoQ7Zu92T3AtCJBI522NlGmzLwwwnzfe%2FaTsYzrg9gIgQhlde8VI3Qdt1SvmweoyUGLUyQp1fq0knQIoHt5MWn4q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDCKQy7hwd%2BYJajxppyrcA0nnR2j5Ro8p8hcuVpNu0vT6kZA7DxfYOUEsI4ELy8jgTftNzq6t6eWPtT4OtxeuEZ%2BkSFpYmtakdILcz7eO%2BxHErevJH1Of%2B%2BmCAyu9bJfvVCqARqRPQPwNxXn6mlGolbrgmeHiKbMTQZTV1BI3rAOd5BvLVqcbYAZ0Z6GwXOkxXGxu0mN%2FM5RrVOY8MPmQjbO5pcwqX3rg7maYkcWhFsYF5oYkXxMrVPLYSsGK%2FT%2FPq%2B9OgauUiBYQkZqr%2BHb4jl3P4RuWP%2F80T2KJsHdWznmv%2FSVbmp4%2FrYWyh5J7gJfkasbidVUdkmo1PuTxlSAIoSReQ8AOjUj%2FvGk6PnNOM7ohJbYZVKeKXcaoQ5k6vdrrD2mZmuT%2FcyhPV84i3uLfBcHbvSbXKczKtM0Djoo1niVJWj5%2FDq9vQwAJf9bnKJE91tbOvwXc8TI2DvLUq9fnS51nOoLsnk54AUc5oei3Hi6leBhjKnAXqhbiBEdXFbphp3Tc%2BmbbtmJ2ctq44kGSvQZGxICYeakblp9zxctQKJ5E19CtpOKKOSsjkcqlc3SMghiHgdpb%2BNWHl5ufQTZYM7mmBhoVQXgeReBB4q55LqiStLQ60Sp9zQX3qvtj0OgV8gIyHOnYN0JinmMHMK3skb0GOqUBgpCv7n8ZHw60iRhdb%2BeW4KEBZV6CzPokfTVB0GxTL%2BFbZ79Sh3Je80%2BzKqaeT%2B9RJSq7XRhwjjkXlL3zRcTeBqIxOsWhi%2FWl2tJ1NM%2FZFqI9rgS3KDZcsoPu8AR%2B14IkC1pHu0WphFzlRTKga9mtOfLb%2BndIWl4Koab2%2BxqVpghGe%2BSUu%2BF9WdJ3A80XTe2%2BKIO96nWa9tKJYefK2w4RiOwFGVru&X-Amz-Signature=799de719ceb45a97303ca3658d589542dc52324973ef6d383afdb48a31986711&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V3HSRUA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIEFbz0vsW6t5A5dQrLKkUUBtqFQXllMLDgtfmpBXTvOzAiB46qfI9PKYrwrm859telxz9wLUNKZU%2FyUSYXQ4QepxdSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMlKA%2FHc2HjQOd7sQjKtwDX0A%2F6SmXLdUVs0CbXrVKq5umQwZOtF9MpfOp8S9pz1%2Bv1arO4WtoRgiF3Ug8JBq2LVVvRNOX%2BzbThAeHcERl4av797GO0cvGy%2BlnmJ8GpeV7l%2BsBg%2BHWsRXiB%2BY9zZInziRZxgjzPMhIC%2FqPA%2BNdqD%2FaettyAvW9oeQXjNw7xwH84AogQh15nlYfuvlPlHJeObRhtlb6ajUrmlVqK5%2FXUfpgNs9tiM0t%2Ba763FnNQuoG5O1XgVX%2Bsz66w1h8%2B6f%2B%2Bh95St%2Fq6D8ISeQSrZNRQfwKXxGef515RHHYU%2Bj%2BN82iLSoEcD10YFfbHQueES7zqd%2BtN6EW7Qps9zPEH2Hh5kdu14m%2BQMm4KKi3B%2Bg3b9P78pjN%2BBwB4x3rYuWr4WJT8rMbNx5wjHZ1h7yfVsfJa1CkRkUkNMqZAdLCGDmaKxNk7nwGxdlpvLxC7alZ%2BsKVnErvThh%2FVJANeQVx3S2Ne3FWPXy8%2Fvod8LsI9bS6y%2Bc8vpMrBmwPS4Y0GY8e%2BKkehP3p9M7F0EAXTrqIsegMqzJX7lWr6oKg2ZP%2Bq2aEFJOaJfUHonAQCdAQ26bCroV8miSFBGx8LyBWGvSvG8kZAHet5S42xlh%2BpkR6iEqqcV0Zzn7qPRKsTOlN18wwjOyRvQY6pgH5M9NuLem5vB1XEz9hOAuuHrgeHjRqBxJWeSp4k2ywDzUmlssy%2B5wovn6UvS%2BNR7cMUkKxIfs0HtJXVJsTGYA8j%2FAy8qny9LouxpRJ%2BBlzs%2BA4vwRI3LmhZ568l0j8DCxJVzCokFaiNJwTFZM%2Bx0kRdGz1xy%2BNyHXKJVtVGgnlXlToZVal0a6ijd5ilayzbAlzLOZW4MPobmfBgy%2Bq7v7NVNW8iuDO&X-Amz-Signature=7942b0f5b5c2a3fc1d630227cbed13309ad0640f3cb8dee042ae06e5f355408e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVXH6XH7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCUpEwfV3gxJdKD5FxRuoxVjONNy0lj3QP%2ByIYtAPM8pgIgMt5b8gemslC2oH3w%2FLK8WOu%2BjrcmntR0HQcQK0aFSdsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDf65C1kCcEIEspUVircA2X6KHeJnMBD2WElRHhZbHjiTyvsT0X5nhO6sRy4WkRJk9OAUknk5SVzFGImFzWiwwBaW8YPEYyVxgP1y%2BKdwk2Y3hwTlKbsinCS%2BuWMOdZP0bcpb5C%2Bpgcx5wAKOHYTALRHxWF87p4KL30cy0YTLuxUfoE0tpkR5baRFUMTCmLVFfOUPHZhqXrcNrXvoPNdWd9JDJ0L5yGRGrwaVB18mmj627nbdXct59Yu4LBbXMhCqkkv4%2FiSLdAcD%2BJc8TSfNUkr8XI7et6pUeHImj3lIy8GEh%2BZ%2Bz%2FLap8ZxDQayY46L9i%2BNCPfmwvDbjtOybBWMHiP0parEAUn3phkW5NQA%2Fw59LKGedO1IdqtF0SX8wbhcf9fo1aGc4oHCNPUPTgrqnvChqFlNe0HatIV1W9UWQyGDB1V5FcTpZGbAwMCP%2B%2BwxDBsr1RiljGAm6fTyyRawM3sI3LtYlqSw638rFLUoD3rA8%2FEWd6QY9P9E1fO8bdQkD30CTWnKDW2ED4NjepACsPQHGumZHQ%2FkrOIDfBZUKoHbf9%2FIuWmmH2n4jsQxqBhfUBungoeRgM8S83cIPIECe8XxLKPAhbeXXaosl3lSQK90%2FHCO10ip2rIyelmVaJZnNnmoVTvP%2FlfpfNMMJTskb0GOqUBM7eLlblyMoLNEWo0L2Tj6p7U0IsqzlXW2GTI8Q2yfmUEdj40jPY90r5EPrG1ZSokCuXiw%2FqGcfhGxgo3w%2FUgkEkMW1xlxjhHv51d2HI8vHOb%2FEVO7ehhfmdkLNLgUJdsgKZZar5O%2BdnETHhixtGqSiLs4xC49Of%2Bya2EzutcS4w0oorP%2Bra8RiilWCUPKcwTG2oOr9hnenMtc5%2B06teOVCHY%2BjA%2B&X-Amz-Signature=086b054881b670f8458b33b91dba25f6ec6510ba02684ab1c479810ddf76acf5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4QVEWQJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIE3cTEFYeO02VCkbPXpsPZjDMhzvGtE%2Fq3nzkvGGw1w%2FAiAkOcwZX68pJsmBivte43wulkUaUj9R69vvIWMfQUYXhCr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMTrK%2B7l8fXH1cMMOIKtwD3HOVoV7q7RphX2JqeLHR7N8PAKglib%2BrNl48hq3FdKArNffGN0cutAxtTwowXNgOyRVZLmjsxgb4OkqKQr6RAAZBIHFNWqlVYpTqQDLNZ%2BIqrzcY%2FFPz3Sm2VJs7Etuas2nxA2J3oxrwOAz09Ihuk6TIY7ccFTZJqrruY68Czs%2BuWmr%2Fl9N02CyisIvtfQK%2FeeJzDrx9%2BvajWvXaUR6DDVdxSZNgWIZw6L6zY1%2FCaVfrsrE4xc%2BMOOalV%2BktzX8D2v2rCXf0eIe7uai0IsQm7bD%2FUCLtDQ0kkXtgeuVFSe9X9IiFMROMIhuRPUwgIhfX3NqNU2tnitnVMxA%2FIAOUA42WcSWWJj83yetTinUIRUF4f7R%2BCT7njR1oTVe4ceBpy8ZVLCP9ubHp6RmxqNBUVT%2FWzeQ2Fa1Ho3MC8caHKPI5AXGiSFJUSN6WN1eKtGDSwTl6fcN5ebGF%2F47R0NeawVnF9M0xSCgtNiZFZfranJjdZlf%2Bsm0mR2htsFWx3dYVJf9YYVgOiZxrPfenVVZmqwLkgzjwia89RGMwrqONxdSyVvmeXryGDqStE6zDMqeSGUP%2BqdeoM1HS52aZ5qgtnaLdxgS9CKn3zzr%2FAwpX1BWKH0dC0cy2HLTZrn4woOyRvQY6pgHhnqtUxcrvMm1Q%2FNxQb51PdYq%2FlmV8jUMQk2sIwAr6Z7K5vXqUSUO617roJTURa%2FMM0z6zp7llHFm5jJAW1eR%2BrYuMFWaiJGY8Dcw6w2U7Pd0WfWKBQoopQpv4V7XxbFfLS89lIm9Pd8S7CdRM8FcZRE0NKb7HlhVc4x342Fgz%2B2ytfJ1vNZmogzUL%2BPGoZET5soZv4oMYzA4ruKaRRzrFeAy52mEo&X-Amz-Signature=abb1b327c26be3e7fe7e987b0ece979e4c8c1788ceb53b8b3b1c88088cd65260&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4QVEWQJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIE3cTEFYeO02VCkbPXpsPZjDMhzvGtE%2Fq3nzkvGGw1w%2FAiAkOcwZX68pJsmBivte43wulkUaUj9R69vvIWMfQUYXhCr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMTrK%2B7l8fXH1cMMOIKtwD3HOVoV7q7RphX2JqeLHR7N8PAKglib%2BrNl48hq3FdKArNffGN0cutAxtTwowXNgOyRVZLmjsxgb4OkqKQr6RAAZBIHFNWqlVYpTqQDLNZ%2BIqrzcY%2FFPz3Sm2VJs7Etuas2nxA2J3oxrwOAz09Ihuk6TIY7ccFTZJqrruY68Czs%2BuWmr%2Fl9N02CyisIvtfQK%2FeeJzDrx9%2BvajWvXaUR6DDVdxSZNgWIZw6L6zY1%2FCaVfrsrE4xc%2BMOOalV%2BktzX8D2v2rCXf0eIe7uai0IsQm7bD%2FUCLtDQ0kkXtgeuVFSe9X9IiFMROMIhuRPUwgIhfX3NqNU2tnitnVMxA%2FIAOUA42WcSWWJj83yetTinUIRUF4f7R%2BCT7njR1oTVe4ceBpy8ZVLCP9ubHp6RmxqNBUVT%2FWzeQ2Fa1Ho3MC8caHKPI5AXGiSFJUSN6WN1eKtGDSwTl6fcN5ebGF%2F47R0NeawVnF9M0xSCgtNiZFZfranJjdZlf%2Bsm0mR2htsFWx3dYVJf9YYVgOiZxrPfenVVZmqwLkgzjwia89RGMwrqONxdSyVvmeXryGDqStE6zDMqeSGUP%2BqdeoM1HS52aZ5qgtnaLdxgS9CKn3zzr%2FAwpX1BWKH0dC0cy2HLTZrn4woOyRvQY6pgHhnqtUxcrvMm1Q%2FNxQb51PdYq%2FlmV8jUMQk2sIwAr6Z7K5vXqUSUO617roJTURa%2FMM0z6zp7llHFm5jJAW1eR%2BrYuMFWaiJGY8Dcw6w2U7Pd0WfWKBQoopQpv4V7XxbFfLS89lIm9Pd8S7CdRM8FcZRE0NKb7HlhVc4x342Fgz%2B2ytfJ1vNZmogzUL%2BPGoZET5soZv4oMYzA4ruKaRRzrFeAy52mEo&X-Amz-Signature=2e13c33a01cdc4b08b2c781cc35fefa99154d7bcd0982225f74d4a75b0a5c635&X-Amz-SignedHeaders=host&x-id=GetObject)

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
