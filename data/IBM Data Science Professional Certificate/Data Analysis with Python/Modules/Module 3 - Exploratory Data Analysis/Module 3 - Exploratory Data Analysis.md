

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSGYW7D5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCICI%2FuYAN2RHT65IZMYAswRGvAPoPNkpsDtsHl4LoxOYyAiBuZ9jgCfHvU9eZJKmijTuxCgfXzM1VA9hiqpwCVspqEir%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM6TPKruN8gjkNxaXmKtwDRTw0GblC2VQiEBOpznIdf67eWUDvOacp9pg6GyKxDJZXvmDF92vwYEaCHSIq2o6bJHIimtgMb0jcFMlFdIecfeMu4Yylea6M3mDIUzjCiDLWPR3hj3RHG%2FXrmCB%2FiTBX2h60Hpu7jzm%2BX3SlfTYEaX9Mck60yefsWNYWs01oH%2B2jzo0oim6OZI%2BNs2nI9umfM6DuXZhz1jW%2FgCFCh4ur4V%2FQIVUbz197OnbSraOSLhHaH0VWE4nvIqFaGeCOkXNCoVIJHI%2FjUtsFxCtpbHTYxMXYcAqdG1AOI%2FTGWF8wIHdUauXiCnPn03t8zn%2BpHHDV4ZLNzO%2FKpG6RiEShYp%2FqK0XS7gnUaDasFlHHhalQtzBEv%2BD37CR%2FaUleMDkl6IunG0o4bwS0AQJakNW3re5frlZeLBahXQOaqXayZEcN4ihupIJJqjFkTcSsV6WuzTpLccw6qOf6y9pX8oYoh6M1123XZWWVSEjQ%2FOlB53pWvRAUMnEaFnpQBgf%2FvvVAaoPqUhZH4xscws%2F%2BoJn4noYlRSpGIFnYiPHqSseidnvYKRUFTLcmZeVSsSh6%2FrX%2BbbqRauHZKZJGBz0SyY4t%2BSzszzwMjI76h%2FzYiAFdgnaNgkSY32prTLpZXbRl99YwwfuTvQY6pgGT%2FjQzwtrSdpdEUSf%2BQDpxj17xRglW5TV9zAedRdeHI2K9la2Cn3fhLqAOf0GhjDoF9d0%2FDhuAFvcGHhDyqnmirqRmGhykl0zUsdapggKqDsMyTIFtIWgPlGPGNP%2FnnDFboYBCrGrkg7c8fPUa0UVmDy1nR23EnS9kQZnmIPjYDFiDwRwDJHoKJ26ojQA%2Fy4393i%2B2HZwfW7zOCsujOdIJh8v7l4YA&X-Amz-Signature=e34eeee9fc6af508c36d6a58ad9e46ab1b8ea68d1f30918e0becbf59fcae8077&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSGYW7D5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCICI%2FuYAN2RHT65IZMYAswRGvAPoPNkpsDtsHl4LoxOYyAiBuZ9jgCfHvU9eZJKmijTuxCgfXzM1VA9hiqpwCVspqEir%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM6TPKruN8gjkNxaXmKtwDRTw0GblC2VQiEBOpznIdf67eWUDvOacp9pg6GyKxDJZXvmDF92vwYEaCHSIq2o6bJHIimtgMb0jcFMlFdIecfeMu4Yylea6M3mDIUzjCiDLWPR3hj3RHG%2FXrmCB%2FiTBX2h60Hpu7jzm%2BX3SlfTYEaX9Mck60yefsWNYWs01oH%2B2jzo0oim6OZI%2BNs2nI9umfM6DuXZhz1jW%2FgCFCh4ur4V%2FQIVUbz197OnbSraOSLhHaH0VWE4nvIqFaGeCOkXNCoVIJHI%2FjUtsFxCtpbHTYxMXYcAqdG1AOI%2FTGWF8wIHdUauXiCnPn03t8zn%2BpHHDV4ZLNzO%2FKpG6RiEShYp%2FqK0XS7gnUaDasFlHHhalQtzBEv%2BD37CR%2FaUleMDkl6IunG0o4bwS0AQJakNW3re5frlZeLBahXQOaqXayZEcN4ihupIJJqjFkTcSsV6WuzTpLccw6qOf6y9pX8oYoh6M1123XZWWVSEjQ%2FOlB53pWvRAUMnEaFnpQBgf%2FvvVAaoPqUhZH4xscws%2F%2BoJn4noYlRSpGIFnYiPHqSseidnvYKRUFTLcmZeVSsSh6%2FrX%2BbbqRauHZKZJGBz0SyY4t%2BSzszzwMjI76h%2FzYiAFdgnaNgkSY32prTLpZXbRl99YwwfuTvQY6pgGT%2FjQzwtrSdpdEUSf%2BQDpxj17xRglW5TV9zAedRdeHI2K9la2Cn3fhLqAOf0GhjDoF9d0%2FDhuAFvcGHhDyqnmirqRmGhykl0zUsdapggKqDsMyTIFtIWgPlGPGNP%2FnnDFboYBCrGrkg7c8fPUa0UVmDy1nR23EnS9kQZnmIPjYDFiDwRwDJHoKJ26ojQA%2Fy4393i%2B2HZwfW7zOCsujOdIJh8v7l4YA&X-Amz-Signature=d7ecdde3ab8de4b641ec16e3810f38fc4265d827448cc9b39cdfa3387d91d157&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSGYW7D5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCICI%2FuYAN2RHT65IZMYAswRGvAPoPNkpsDtsHl4LoxOYyAiBuZ9jgCfHvU9eZJKmijTuxCgfXzM1VA9hiqpwCVspqEir%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM6TPKruN8gjkNxaXmKtwDRTw0GblC2VQiEBOpznIdf67eWUDvOacp9pg6GyKxDJZXvmDF92vwYEaCHSIq2o6bJHIimtgMb0jcFMlFdIecfeMu4Yylea6M3mDIUzjCiDLWPR3hj3RHG%2FXrmCB%2FiTBX2h60Hpu7jzm%2BX3SlfTYEaX9Mck60yefsWNYWs01oH%2B2jzo0oim6OZI%2BNs2nI9umfM6DuXZhz1jW%2FgCFCh4ur4V%2FQIVUbz197OnbSraOSLhHaH0VWE4nvIqFaGeCOkXNCoVIJHI%2FjUtsFxCtpbHTYxMXYcAqdG1AOI%2FTGWF8wIHdUauXiCnPn03t8zn%2BpHHDV4ZLNzO%2FKpG6RiEShYp%2FqK0XS7gnUaDasFlHHhalQtzBEv%2BD37CR%2FaUleMDkl6IunG0o4bwS0AQJakNW3re5frlZeLBahXQOaqXayZEcN4ihupIJJqjFkTcSsV6WuzTpLccw6qOf6y9pX8oYoh6M1123XZWWVSEjQ%2FOlB53pWvRAUMnEaFnpQBgf%2FvvVAaoPqUhZH4xscws%2F%2BoJn4noYlRSpGIFnYiPHqSseidnvYKRUFTLcmZeVSsSh6%2FrX%2BbbqRauHZKZJGBz0SyY4t%2BSzszzwMjI76h%2FzYiAFdgnaNgkSY32prTLpZXbRl99YwwfuTvQY6pgGT%2FjQzwtrSdpdEUSf%2BQDpxj17xRglW5TV9zAedRdeHI2K9la2Cn3fhLqAOf0GhjDoF9d0%2FDhuAFvcGHhDyqnmirqRmGhykl0zUsdapggKqDsMyTIFtIWgPlGPGNP%2FnnDFboYBCrGrkg7c8fPUa0UVmDy1nR23EnS9kQZnmIPjYDFiDwRwDJHoKJ26ojQA%2Fy4393i%2B2HZwfW7zOCsujOdIJh8v7l4YA&X-Amz-Signature=f40b69f86e2ba51386ce922b1e6bba0b70fb7dfd9e735e8d223f61a999bf7254&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG4JYFV5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGUB2YAr0OILMwmaYL0xFAgeP6CXkTonnHoi2L%2FDJS7gAiAMKt6tvQeaH6T4J%2B969YxoAZ0Wabs0d7p4zCMhZCYLIyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMtUP4OmE3undHdlaOKtwDSYeUfVWP1WrIB5iv3QVDva6KecJSEEpNGZ0nS2spRhnIM%2FBBAbD6GMIEROjNLwFfmkJbxjsq5GDuT8N0zk75RWW%2BHTE9%2BevAz37xusjQuaJi71jUmzUVS4Ox8R9CZOlG9sIREnAD1G3qGKYYUQYyZQqlv9zz%2FhBu%2BgHsLi8r2IWvTl5pkLPSU5SoRSusequanBL%2B7smOmklKQuY4nTDFmwbyfMwwVlOBaM4TOJafccpS48NaE8gV0wN3yOtUYUGpvjv2Rt18on4JylUDMpZVjimR92FRu3SI0B%2BHcrFLvWtvKMBvN%2F8dW6%2B%2BKh8U1iok8zsrYLK9sAuApV83CjfT3RrB1XNO4e27xf75PxMLCcPi%2FznqZSCMyObjXb5ECvEZODA%2BX8LP7CR1xq75xbbBpWZRzlGw3mJk09TfBT3rSyWOFKQxs%2F4gIF7k8R2Lu%2ByPhyvqGJIyVb16To4RuFNIpkhW7YGDv5VvzZgeSGndZHo39%2FCnhlovqFCeBCmLxOKTAm%2BilsuvTGUQ6Sg9xfwGgdUqF%2BB95qDj9zsNClEW5efJCt0RCboHVeaWZF1jGAe9qownaGplyO3Bwx3OqieDFNEevQhfM1nF1us74xoYrnIRfJusVSva5NmhIlMw2fuTvQY6pgFw8ph87nlOOzagnjKMfSAn1CsDeV6a6aSqvNseY7DpQQtG1jxpm6HF4PEGKJ3PfcxNmSO6sHL5ZEOrM2Q3srexg8N5ibGXoTP5xIJxq%2FQAqPoCck%2FkO8O1xN0uWdhpAQRrAo3GxFN%2Fwh%2BRFtyOv%2FioCeY8sWTEazJ7XPGGMQ8m9vG%2BHV%2BK016mVtP1f0W8ivdJSG9Uepv6OBsRoc2QECp8j%2FS65jN0&X-Amz-Signature=b7b8f030e1a05cbbffca6b6148591905c3c8e28c24a583593bedf5d1911b0f30&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG4JYFV5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGUB2YAr0OILMwmaYL0xFAgeP6CXkTonnHoi2L%2FDJS7gAiAMKt6tvQeaH6T4J%2B969YxoAZ0Wabs0d7p4zCMhZCYLIyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMtUP4OmE3undHdlaOKtwDSYeUfVWP1WrIB5iv3QVDva6KecJSEEpNGZ0nS2spRhnIM%2FBBAbD6GMIEROjNLwFfmkJbxjsq5GDuT8N0zk75RWW%2BHTE9%2BevAz37xusjQuaJi71jUmzUVS4Ox8R9CZOlG9sIREnAD1G3qGKYYUQYyZQqlv9zz%2FhBu%2BgHsLi8r2IWvTl5pkLPSU5SoRSusequanBL%2B7smOmklKQuY4nTDFmwbyfMwwVlOBaM4TOJafccpS48NaE8gV0wN3yOtUYUGpvjv2Rt18on4JylUDMpZVjimR92FRu3SI0B%2BHcrFLvWtvKMBvN%2F8dW6%2B%2BKh8U1iok8zsrYLK9sAuApV83CjfT3RrB1XNO4e27xf75PxMLCcPi%2FznqZSCMyObjXb5ECvEZODA%2BX8LP7CR1xq75xbbBpWZRzlGw3mJk09TfBT3rSyWOFKQxs%2F4gIF7k8R2Lu%2ByPhyvqGJIyVb16To4RuFNIpkhW7YGDv5VvzZgeSGndZHo39%2FCnhlovqFCeBCmLxOKTAm%2BilsuvTGUQ6Sg9xfwGgdUqF%2BB95qDj9zsNClEW5efJCt0RCboHVeaWZF1jGAe9qownaGplyO3Bwx3OqieDFNEevQhfM1nF1us74xoYrnIRfJusVSva5NmhIlMw2fuTvQY6pgFw8ph87nlOOzagnjKMfSAn1CsDeV6a6aSqvNseY7DpQQtG1jxpm6HF4PEGKJ3PfcxNmSO6sHL5ZEOrM2Q3srexg8N5ibGXoTP5xIJxq%2FQAqPoCck%2FkO8O1xN0uWdhpAQRrAo3GxFN%2Fwh%2BRFtyOv%2FioCeY8sWTEazJ7XPGGMQ8m9vG%2BHV%2BK016mVtP1f0W8ivdJSG9Uepv6OBsRoc2QECp8j%2FS65jN0&X-Amz-Signature=798cd278f5e83e1104941960ab663511ed563497ed471e8af1416326f48f86d2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG4JYFV5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGUB2YAr0OILMwmaYL0xFAgeP6CXkTonnHoi2L%2FDJS7gAiAMKt6tvQeaH6T4J%2B969YxoAZ0Wabs0d7p4zCMhZCYLIyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMtUP4OmE3undHdlaOKtwDSYeUfVWP1WrIB5iv3QVDva6KecJSEEpNGZ0nS2spRhnIM%2FBBAbD6GMIEROjNLwFfmkJbxjsq5GDuT8N0zk75RWW%2BHTE9%2BevAz37xusjQuaJi71jUmzUVS4Ox8R9CZOlG9sIREnAD1G3qGKYYUQYyZQqlv9zz%2FhBu%2BgHsLi8r2IWvTl5pkLPSU5SoRSusequanBL%2B7smOmklKQuY4nTDFmwbyfMwwVlOBaM4TOJafccpS48NaE8gV0wN3yOtUYUGpvjv2Rt18on4JylUDMpZVjimR92FRu3SI0B%2BHcrFLvWtvKMBvN%2F8dW6%2B%2BKh8U1iok8zsrYLK9sAuApV83CjfT3RrB1XNO4e27xf75PxMLCcPi%2FznqZSCMyObjXb5ECvEZODA%2BX8LP7CR1xq75xbbBpWZRzlGw3mJk09TfBT3rSyWOFKQxs%2F4gIF7k8R2Lu%2ByPhyvqGJIyVb16To4RuFNIpkhW7YGDv5VvzZgeSGndZHo39%2FCnhlovqFCeBCmLxOKTAm%2BilsuvTGUQ6Sg9xfwGgdUqF%2BB95qDj9zsNClEW5efJCt0RCboHVeaWZF1jGAe9qownaGplyO3Bwx3OqieDFNEevQhfM1nF1us74xoYrnIRfJusVSva5NmhIlMw2fuTvQY6pgFw8ph87nlOOzagnjKMfSAn1CsDeV6a6aSqvNseY7DpQQtG1jxpm6HF4PEGKJ3PfcxNmSO6sHL5ZEOrM2Q3srexg8N5ibGXoTP5xIJxq%2FQAqPoCck%2FkO8O1xN0uWdhpAQRrAo3GxFN%2Fwh%2BRFtyOv%2FioCeY8sWTEazJ7XPGGMQ8m9vG%2BHV%2BK016mVtP1f0W8ivdJSG9Uepv6OBsRoc2QECp8j%2FS65jN0&X-Amz-Signature=083ed06b06e5748b646803a6ce043b32ab689882f03a72a9b05bf28038ac956d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG4JYFV5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGUB2YAr0OILMwmaYL0xFAgeP6CXkTonnHoi2L%2FDJS7gAiAMKt6tvQeaH6T4J%2B969YxoAZ0Wabs0d7p4zCMhZCYLIyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMtUP4OmE3undHdlaOKtwDSYeUfVWP1WrIB5iv3QVDva6KecJSEEpNGZ0nS2spRhnIM%2FBBAbD6GMIEROjNLwFfmkJbxjsq5GDuT8N0zk75RWW%2BHTE9%2BevAz37xusjQuaJi71jUmzUVS4Ox8R9CZOlG9sIREnAD1G3qGKYYUQYyZQqlv9zz%2FhBu%2BgHsLi8r2IWvTl5pkLPSU5SoRSusequanBL%2B7smOmklKQuY4nTDFmwbyfMwwVlOBaM4TOJafccpS48NaE8gV0wN3yOtUYUGpvjv2Rt18on4JylUDMpZVjimR92FRu3SI0B%2BHcrFLvWtvKMBvN%2F8dW6%2B%2BKh8U1iok8zsrYLK9sAuApV83CjfT3RrB1XNO4e27xf75PxMLCcPi%2FznqZSCMyObjXb5ECvEZODA%2BX8LP7CR1xq75xbbBpWZRzlGw3mJk09TfBT3rSyWOFKQxs%2F4gIF7k8R2Lu%2ByPhyvqGJIyVb16To4RuFNIpkhW7YGDv5VvzZgeSGndZHo39%2FCnhlovqFCeBCmLxOKTAm%2BilsuvTGUQ6Sg9xfwGgdUqF%2BB95qDj9zsNClEW5efJCt0RCboHVeaWZF1jGAe9qownaGplyO3Bwx3OqieDFNEevQhfM1nF1us74xoYrnIRfJusVSva5NmhIlMw2fuTvQY6pgFw8ph87nlOOzagnjKMfSAn1CsDeV6a6aSqvNseY7DpQQtG1jxpm6HF4PEGKJ3PfcxNmSO6sHL5ZEOrM2Q3srexg8N5ibGXoTP5xIJxq%2FQAqPoCck%2FkO8O1xN0uWdhpAQRrAo3GxFN%2Fwh%2BRFtyOv%2FioCeY8sWTEazJ7XPGGMQ8m9vG%2BHV%2BK016mVtP1f0W8ivdJSG9Uepv6OBsRoc2QECp8j%2FS65jN0&X-Amz-Signature=46b8c0e8b31714e065463b486735a316aeadfea7db087cb85eccc818ed8d2e80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG4JYFV5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGUB2YAr0OILMwmaYL0xFAgeP6CXkTonnHoi2L%2FDJS7gAiAMKt6tvQeaH6T4J%2B969YxoAZ0Wabs0d7p4zCMhZCYLIyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMtUP4OmE3undHdlaOKtwDSYeUfVWP1WrIB5iv3QVDva6KecJSEEpNGZ0nS2spRhnIM%2FBBAbD6GMIEROjNLwFfmkJbxjsq5GDuT8N0zk75RWW%2BHTE9%2BevAz37xusjQuaJi71jUmzUVS4Ox8R9CZOlG9sIREnAD1G3qGKYYUQYyZQqlv9zz%2FhBu%2BgHsLi8r2IWvTl5pkLPSU5SoRSusequanBL%2B7smOmklKQuY4nTDFmwbyfMwwVlOBaM4TOJafccpS48NaE8gV0wN3yOtUYUGpvjv2Rt18on4JylUDMpZVjimR92FRu3SI0B%2BHcrFLvWtvKMBvN%2F8dW6%2B%2BKh8U1iok8zsrYLK9sAuApV83CjfT3RrB1XNO4e27xf75PxMLCcPi%2FznqZSCMyObjXb5ECvEZODA%2BX8LP7CR1xq75xbbBpWZRzlGw3mJk09TfBT3rSyWOFKQxs%2F4gIF7k8R2Lu%2ByPhyvqGJIyVb16To4RuFNIpkhW7YGDv5VvzZgeSGndZHo39%2FCnhlovqFCeBCmLxOKTAm%2BilsuvTGUQ6Sg9xfwGgdUqF%2BB95qDj9zsNClEW5efJCt0RCboHVeaWZF1jGAe9qownaGplyO3Bwx3OqieDFNEevQhfM1nF1us74xoYrnIRfJusVSva5NmhIlMw2fuTvQY6pgFw8ph87nlOOzagnjKMfSAn1CsDeV6a6aSqvNseY7DpQQtG1jxpm6HF4PEGKJ3PfcxNmSO6sHL5ZEOrM2Q3srexg8N5ibGXoTP5xIJxq%2FQAqPoCck%2FkO8O1xN0uWdhpAQRrAo3GxFN%2Fwh%2BRFtyOv%2FioCeY8sWTEazJ7XPGGMQ8m9vG%2BHV%2BK016mVtP1f0W8ivdJSG9Uepv6OBsRoc2QECp8j%2FS65jN0&X-Amz-Signature=9b9c61959934ec1a7888baa7035c3cddba4b8593b12d3085a976ac5e4bf344b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG4JYFV5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGUB2YAr0OILMwmaYL0xFAgeP6CXkTonnHoi2L%2FDJS7gAiAMKt6tvQeaH6T4J%2B969YxoAZ0Wabs0d7p4zCMhZCYLIyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMtUP4OmE3undHdlaOKtwDSYeUfVWP1WrIB5iv3QVDva6KecJSEEpNGZ0nS2spRhnIM%2FBBAbD6GMIEROjNLwFfmkJbxjsq5GDuT8N0zk75RWW%2BHTE9%2BevAz37xusjQuaJi71jUmzUVS4Ox8R9CZOlG9sIREnAD1G3qGKYYUQYyZQqlv9zz%2FhBu%2BgHsLi8r2IWvTl5pkLPSU5SoRSusequanBL%2B7smOmklKQuY4nTDFmwbyfMwwVlOBaM4TOJafccpS48NaE8gV0wN3yOtUYUGpvjv2Rt18on4JylUDMpZVjimR92FRu3SI0B%2BHcrFLvWtvKMBvN%2F8dW6%2B%2BKh8U1iok8zsrYLK9sAuApV83CjfT3RrB1XNO4e27xf75PxMLCcPi%2FznqZSCMyObjXb5ECvEZODA%2BX8LP7CR1xq75xbbBpWZRzlGw3mJk09TfBT3rSyWOFKQxs%2F4gIF7k8R2Lu%2ByPhyvqGJIyVb16To4RuFNIpkhW7YGDv5VvzZgeSGndZHo39%2FCnhlovqFCeBCmLxOKTAm%2BilsuvTGUQ6Sg9xfwGgdUqF%2BB95qDj9zsNClEW5efJCt0RCboHVeaWZF1jGAe9qownaGplyO3Bwx3OqieDFNEevQhfM1nF1us74xoYrnIRfJusVSva5NmhIlMw2fuTvQY6pgFw8ph87nlOOzagnjKMfSAn1CsDeV6a6aSqvNseY7DpQQtG1jxpm6HF4PEGKJ3PfcxNmSO6sHL5ZEOrM2Q3srexg8N5ibGXoTP5xIJxq%2FQAqPoCck%2FkO8O1xN0uWdhpAQRrAo3GxFN%2Fwh%2BRFtyOv%2FioCeY8sWTEazJ7XPGGMQ8m9vG%2BHV%2BK016mVtP1f0W8ivdJSG9Uepv6OBsRoc2QECp8j%2FS65jN0&X-Amz-Signature=df073a91b5df203002bb0cfe912bd6e761434721e2d1a102942df6c0ccb8f2b6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSQVQ3P4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQC2zsqFG6nrxrzmT0xcGtP9%2BpMe7OfwSR1cS4g9GXRtegIhAMBQgJwpSnznhmYxThE9TWqPU22ppU%2FHMK7tXHKDNpqSKv8DCGMQABoMNjM3NDIzMTgzODA1IgzWxOr0Cfrp2hZ295Mq3AN6lFXwpdtXhJ1pdAgW5DeQ%2FfWlAhDebZCLDPKTVigHaETXsq5BedXu5%2F4IACQiPXsBn3Xvba5DbQG798tqhfBVvJJHKv9N3DLKLhrmOsZghh89SjZ32Eh6H3kZLIJI%2BLE9sp68i74Mj6AX8SGWrcwczWdEy2ocbnxd7gBTgQbPUrOhve5qopgOxCsIq2Mn1R0c%2BG3EXfK4m471uku1tZ9IPQ2KJFL5eSgCiKHp8D5BOZ6kmfNJ7gbL06GpSHeMMzVd5JGRFAvLU%2FQKv2bxtfOwR71%2FuOu2UtmBJHZrr8a54fKsSxUt2oM3eB%2BzjwKDfYuSQZX5bgd3rosGYDZEu2FWAu%2F2p9Qo%2FPQPAN%2F6Y7VZnwfU5JK9Zqvdll9GFDuoV5cB9dmlYYU8FJ7W1F8jyJ0PFBp5x5LqQ20zSDk3%2F193a%2FnF6VIR8uedtVb0GL1GGqnUl6dVqZHT4j6evQ1jeEpd4eVZKuDQ9UynGsyxSVQYX6DyZQ3ivmwO3IVZSacFJRa301m29r38dOr4U4rleuB0sDY7oH3A5PfMDJju%2BmIBF%2FZZYaJSGhDFJq7%2F4QOgTF3GTkYlOyKK2Nekw2P3L0lq8MCm3AtneRua4atLq%2FcAMFooPWbu8yeyLciucjCc%2B5O9BjqkAUpVtR0VwIJzcG48rj%2B4ECJRvjFrsKolffH1k%2F%2BD%2BPTRaF6EX6wf6hLX6o%2Fy5OlrylOyHeqXyagvm1ZJzILeBSfAr3yRvdFizdsEU6QIXLyNeKk%2F6PkrrB1vlKrk8pFbDs8r7K4KWcY6QdMxEDbJsa8PTeTMG2tik2JD2Cy8Kv4bTvm0yfZvUoQW8s3WVdXUdct7AWFKtA1jECq1VXEr0mI5NB%2B3&X-Amz-Signature=bd18e41180c533b4a35b20cb8c1143be6909a504d959db227400b1cc47aba121&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNN2DHYY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCb9pGKcWxtuWHABlJeKTU%2BVZ6Jn57byWAlO4pd%2Bf5MRgIhANG5w15beIJHNpDu8g3jMRc%2BPV4EtoJEt2wGATLVAJsAKv8DCGMQABoMNjM3NDIzMTgzODA1IgzT2KmslbaIaBY8RGkq3AO6w2mFo%2BUMh5H%2BEiDAemWgcalFnhP3cPK49kNTTvn7Y2VnsqBRvTbKa0p9GJOD8LVthEtUOpmaKvftWvtihHhrbF1zF%2BcsIzW3Ws0z%2BYjIo4dWkPJZObxArH9Z5vXMEMg1Tzto1hFiefbxoTyFvTtp%2BUUvFvJTNxpa9Dt1s8LCw1z%2Bj2gAc8i5%2FWhik73e1D%2BFh37bREzi2w05mqsqM012z5OW3jzfp8kKns%2BGXXWVA%2FvDgMlJry9muqELbPcBxuiYN67jjw%2BphlbEizEqHR5h%2FoEqyEicrnhEhypkIeGAXyjspUKVLMhoKIIExPCOGtDIJm92zSTlFLJ%2FzJEvLu%2B4zG65oJ4vZWMmT5vRLOLRyqMhj5ux72aw01BloEt9fT3IianXIwGP1lZE5bbLNqv7KoKwYJeLhwXBTKmg2LLwguna9A53NP23zC0K9Fw2SLXA1fPlOwh9KC0RrzihdqTT3Fk93zpZVT%2B7X%2BxlFRjbseIXeYYnB4fXHT1Ky6Y5tDgmzU2L4ZC2f%2B%2BOjH0vNOhVLlllUjhfFNUyNa5VeClbkjVcbIezy0Fmb%2FrBRUKcl7RiEcoZuErX9UFFyzHQ5ySSsPYVYHWTn5eHX0p%2FGcRUvBxh5aLgS8o1ZF%2FxkTDR%2B5O9BjqkAXFaauSHxbs4V%2FJce0xrGMaZTYOJDsj4oDqm%2FWDkdvAPRvUumyYV09vQEOX5IbcVj68s%2FJa%2BLTqwRyuPN3w7tymQqKN7P4dd%2FFzboYHL0Rp8RmbvO6CEIuISH%2BdXoxNIrqpSqkMjFdlskStLxXLMSa5%2B9nJwYlRcGpzEjxyUPP4z2QtBV26iwpimotdydWfcEp0ra9lVM4U2iwLmoOSD%2FSDO03el&X-Amz-Signature=abe495e2e964ba835ae026c99e26d4d073c3572c22eab2b5940e3ded9556f704&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG4JYFV5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGUB2YAr0OILMwmaYL0xFAgeP6CXkTonnHoi2L%2FDJS7gAiAMKt6tvQeaH6T4J%2B969YxoAZ0Wabs0d7p4zCMhZCYLIyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMtUP4OmE3undHdlaOKtwDSYeUfVWP1WrIB5iv3QVDva6KecJSEEpNGZ0nS2spRhnIM%2FBBAbD6GMIEROjNLwFfmkJbxjsq5GDuT8N0zk75RWW%2BHTE9%2BevAz37xusjQuaJi71jUmzUVS4Ox8R9CZOlG9sIREnAD1G3qGKYYUQYyZQqlv9zz%2FhBu%2BgHsLi8r2IWvTl5pkLPSU5SoRSusequanBL%2B7smOmklKQuY4nTDFmwbyfMwwVlOBaM4TOJafccpS48NaE8gV0wN3yOtUYUGpvjv2Rt18on4JylUDMpZVjimR92FRu3SI0B%2BHcrFLvWtvKMBvN%2F8dW6%2B%2BKh8U1iok8zsrYLK9sAuApV83CjfT3RrB1XNO4e27xf75PxMLCcPi%2FznqZSCMyObjXb5ECvEZODA%2BX8LP7CR1xq75xbbBpWZRzlGw3mJk09TfBT3rSyWOFKQxs%2F4gIF7k8R2Lu%2ByPhyvqGJIyVb16To4RuFNIpkhW7YGDv5VvzZgeSGndZHo39%2FCnhlovqFCeBCmLxOKTAm%2BilsuvTGUQ6Sg9xfwGgdUqF%2BB95qDj9zsNClEW5efJCt0RCboHVeaWZF1jGAe9qownaGplyO3Bwx3OqieDFNEevQhfM1nF1us74xoYrnIRfJusVSva5NmhIlMw2fuTvQY6pgFw8ph87nlOOzagnjKMfSAn1CsDeV6a6aSqvNseY7DpQQtG1jxpm6HF4PEGKJ3PfcxNmSO6sHL5ZEOrM2Q3srexg8N5ibGXoTP5xIJxq%2FQAqPoCck%2FkO8O1xN0uWdhpAQRrAo3GxFN%2Fwh%2BRFtyOv%2FioCeY8sWTEazJ7XPGGMQ8m9vG%2BHV%2BK016mVtP1f0W8ivdJSG9Uepv6OBsRoc2QECp8j%2FS65jN0&X-Amz-Signature=49faed2ff1c0c8c8e4d79cd81260b585bd76b2e458de7eba50a913a51d3ddd09&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG4JYFV5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGUB2YAr0OILMwmaYL0xFAgeP6CXkTonnHoi2L%2FDJS7gAiAMKt6tvQeaH6T4J%2B969YxoAZ0Wabs0d7p4zCMhZCYLIyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMtUP4OmE3undHdlaOKtwDSYeUfVWP1WrIB5iv3QVDva6KecJSEEpNGZ0nS2spRhnIM%2FBBAbD6GMIEROjNLwFfmkJbxjsq5GDuT8N0zk75RWW%2BHTE9%2BevAz37xusjQuaJi71jUmzUVS4Ox8R9CZOlG9sIREnAD1G3qGKYYUQYyZQqlv9zz%2FhBu%2BgHsLi8r2IWvTl5pkLPSU5SoRSusequanBL%2B7smOmklKQuY4nTDFmwbyfMwwVlOBaM4TOJafccpS48NaE8gV0wN3yOtUYUGpvjv2Rt18on4JylUDMpZVjimR92FRu3SI0B%2BHcrFLvWtvKMBvN%2F8dW6%2B%2BKh8U1iok8zsrYLK9sAuApV83CjfT3RrB1XNO4e27xf75PxMLCcPi%2FznqZSCMyObjXb5ECvEZODA%2BX8LP7CR1xq75xbbBpWZRzlGw3mJk09TfBT3rSyWOFKQxs%2F4gIF7k8R2Lu%2ByPhyvqGJIyVb16To4RuFNIpkhW7YGDv5VvzZgeSGndZHo39%2FCnhlovqFCeBCmLxOKTAm%2BilsuvTGUQ6Sg9xfwGgdUqF%2BB95qDj9zsNClEW5efJCt0RCboHVeaWZF1jGAe9qownaGplyO3Bwx3OqieDFNEevQhfM1nF1us74xoYrnIRfJusVSva5NmhIlMw2fuTvQY6pgFw8ph87nlOOzagnjKMfSAn1CsDeV6a6aSqvNseY7DpQQtG1jxpm6HF4PEGKJ3PfcxNmSO6sHL5ZEOrM2Q3srexg8N5ibGXoTP5xIJxq%2FQAqPoCck%2FkO8O1xN0uWdhpAQRrAo3GxFN%2Fwh%2BRFtyOv%2FioCeY8sWTEazJ7XPGGMQ8m9vG%2BHV%2BK016mVtP1f0W8ivdJSG9Uepv6OBsRoc2QECp8j%2FS65jN0&X-Amz-Signature=f6273fa3ae06115bfd6c947722a0c18504b1416c3508c7d0bed690939f4a79cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG4JYFV5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGUB2YAr0OILMwmaYL0xFAgeP6CXkTonnHoi2L%2FDJS7gAiAMKt6tvQeaH6T4J%2B969YxoAZ0Wabs0d7p4zCMhZCYLIyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMtUP4OmE3undHdlaOKtwDSYeUfVWP1WrIB5iv3QVDva6KecJSEEpNGZ0nS2spRhnIM%2FBBAbD6GMIEROjNLwFfmkJbxjsq5GDuT8N0zk75RWW%2BHTE9%2BevAz37xusjQuaJi71jUmzUVS4Ox8R9CZOlG9sIREnAD1G3qGKYYUQYyZQqlv9zz%2FhBu%2BgHsLi8r2IWvTl5pkLPSU5SoRSusequanBL%2B7smOmklKQuY4nTDFmwbyfMwwVlOBaM4TOJafccpS48NaE8gV0wN3yOtUYUGpvjv2Rt18on4JylUDMpZVjimR92FRu3SI0B%2BHcrFLvWtvKMBvN%2F8dW6%2B%2BKh8U1iok8zsrYLK9sAuApV83CjfT3RrB1XNO4e27xf75PxMLCcPi%2FznqZSCMyObjXb5ECvEZODA%2BX8LP7CR1xq75xbbBpWZRzlGw3mJk09TfBT3rSyWOFKQxs%2F4gIF7k8R2Lu%2ByPhyvqGJIyVb16To4RuFNIpkhW7YGDv5VvzZgeSGndZHo39%2FCnhlovqFCeBCmLxOKTAm%2BilsuvTGUQ6Sg9xfwGgdUqF%2BB95qDj9zsNClEW5efJCt0RCboHVeaWZF1jGAe9qownaGplyO3Bwx3OqieDFNEevQhfM1nF1us74xoYrnIRfJusVSva5NmhIlMw2fuTvQY6pgFw8ph87nlOOzagnjKMfSAn1CsDeV6a6aSqvNseY7DpQQtG1jxpm6HF4PEGKJ3PfcxNmSO6sHL5ZEOrM2Q3srexg8N5ibGXoTP5xIJxq%2FQAqPoCck%2FkO8O1xN0uWdhpAQRrAo3GxFN%2Fwh%2BRFtyOv%2FioCeY8sWTEazJ7XPGGMQ8m9vG%2BHV%2BK016mVtP1f0W8ivdJSG9Uepv6OBsRoc2QECp8j%2FS65jN0&X-Amz-Signature=14edae75dda8cc0a5fff3f2280fb1dcbb2e6750757638ded55121f0276016a86&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QSPPWTB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQD3lHEpho50zHPFjV3F9Qhaqgh5K9edeiRVjcd%2FdY1FQgIhAI%2B9fNtXhDhvVveIIeojd9T%2FBp4eKb7Jlb9YTT8qulSFKv8DCGMQABoMNjM3NDIzMTgzODA1Igzp%2F%2BIiIDzUk0BiSKEq3APgJ1K8SEakR9kgHDc5F%2BdKUDgf7TJECSRdsDKQJmgWUtbsPn7rY8mnjT9Jv30U4JUISdftbsxZHpWl7pKpoYq5doq6ozUmGzRgC3vSU35iRZeag2CQutNnED9XwT2FrI2iNdbW2Wf818aKTzbehOTEMVv1%2FFFlmoB%2BNeX0Imz8Cx538FkX0oqyaJY0r%2F%2FLjn0cI8yeYAo8vlDAafiST98qrQqZfK%2BsOk9DhVpq0qK6lpPh8fg4chtRBA318CP9pHGMwT0OrYTQSxfjB7LDZk%2Fewl33sG64tjba4ExRloB37PL7%2BXVOn5kc21pR2dVIzG5URA0VW3ZGsatwZW7yBHrOBMmyWeEguco5YGEU5MlTVyqkP7t1DV2sIHNTeUOZXETztHf6Vyz%2BrwoMiFnk8iYNuoe7r74ajweiVCcnC4mOjM%2BOqkpXbE5aDM7nPLat%2Bs8ol3gKvDDm5V3%2FUzxsoXLrPtXgEI5dHT6IvsjpTBlv4KatgTGde6knj%2FLOTf3a8dr4CKesWXBgVV%2BJiA7%2FR%2FQpk59xuGZdSAjKHEWXPV3tBa2iV0%2FmKVdSxq4dh8%2BCNnt7hgs4dmv4jePSYpai%2FT8Xe0yKc5Q495JNavbfTst17w7%2BAIGxSzpIhI93xDCm%2B5O9BjqkASVftU7JYnN4z%2BkxwO4YXsY4Or4QbJ4l9iGr4VXKV894dLqGmpqTvpB4rSz7ly9YK%2Ft9CBcvaqpNJoTtGXYuigBfGV8EaKdq1JlQWPdhPflYLoejh4Mb2R6MCG8KwKleTNgzP%2FhGsRFddLYBq1tJE2DQqm99szXeJVVewp8fZmncqp2WSk7ulsZQWS5WkJrBCLF06Ox3jOsM1H3vWIu%2F1xLhyhNV&X-Amz-Signature=3f8e69896a3d66689b8b481df38fd1d34e065c8202de7c86dfa1899d7a0c0872&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVWAYN7F%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIB%2Bl%2FeHLUElQ5gqYtICGoQKMLDJ%2BLqpHi6655PpO14lyAiB9%2BwKrcJP3rgGlKyAHPRKQDWMIPqTrCMoknNIuMVeSKCr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMHRlNbqYdUoMl2irfKtwD88yjNCsRodmldYvNo%2BAn0CPPVRLsXnKJqbp%2BA7ljE7ANicxQLJIWXP9GxmYx2qBFCdj7ql3b19IntTPhZh9W4y2Ipj4kfEkYPS5CVqsW2lVGMyLGaxVEUocVD7NnBeCb6rXzxUsmMghQV1T%2Fb7pO6pgUoTcdvhNxwVr141dNgLklpeZ5JTmueiT0KULWxSOktLHh6ISIJSrpcrK6NDjjjwC8MPUeUCZxkSVCCSePtJkDpWVqpNP3W5kGcu1myX8Tu5HvrCJuAgq2HfALPe6kZ8hFEOLw65a%2FtY3moTsfbTNrm%2B9RVVtCsWS3O5Xj7IP%2BtcOXIrCzrQFKux691IO0RQEC6sHa4eKWm734HXNyWieSIhBJvQmK7Q%2BhSLCTc9SyqkfBiLrk1VBt0%2FtGQmJzlvbB6un0JWtOMmsJPwCcC4xm4se7k63NuLZnu0DLBIOlgIW0xK5reDfS6Jsdmp5pUrqHGR3vYZlX5DNsd52sR60UYnarQjtJEZW2RSvBWj9jz9vcXFgnKeRa%2BMqdlz7cB%2FiLx7uunR6dHgZ4h7aml9Shx97Yj914SwYhs2%2B0Zm7GKGhtrjTChZ93prdK1vfHmqmbkx6zZ69MNS4cIb2wdaqVO%2FyR6kT0ZL%2FUaccw%2B%2FuTvQY6pgEWcWPuWUXBHQsHCeUGlU4F0u9C7qhXcJjDZJ3yMGh4FaMxW2T7IhZ1clLtmICHW%2BKq9GDE0YEE41PmB6y6JShxSLjB6fv%2FqZUCcs3CuOWXB8VcJYt%2F1jZXj6C2CRXRmKXrz97qetdeQZElqs63VZPBAWr522mWRZV54GW%2B2a884kh%2B6khBck3rh650ku9EH%2BEJqbYJOnuZg3BGvkUxpFVWIDMhrW66&X-Amz-Signature=6e85b9815aa1251f6aabc3f8c49bcec8575448126b9b954e11d14861de5c4c0d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJTKX54T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDr5dW%2FEIgPZWLv8KHtqPd386l%2F3QHlvl6eMnTNBQHkcAiEA%2BbqBRidogCzvau9NJRrPZZdSfVwmdQ98OFzGFTWDosIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDPSZTsNSqIRmc9ncICrcA7HYU4bY0%2FqwdBpB8v1U%2BTRBELA8S78b1mNJLD5NBXBKRlSNUWvzLubqQOT8bmbNOEcM8enuRrGzkeqymgTNcVFi6%2FpCQIk%2BxA%2BFT4MPkV9u%2FSvrmZbHZnIJLySWOVDlu8BsuLgVsPqX1W3LsXPHpyrytxSe2MPb7tWZnfoun6Bejl9VUxwhlnqoSMmsi2lUiX%2FldKzs7VeeAUP0rApN%2F70JIGjeYjLp9UWi4V8d3cMH20rpgmOebzKGN%2FLFHMOCOapPnI0lofmS6bbS5ShcYrtu8zaFfCfBmI992NoFipAHZu7ARSnSvn4H1GcHx2Ch5THFRe%2F2Iwa9xSV4YwNFD8CfvhV8NtJWYWayupVd64ExheSgWdeO0OJUBafRPg6MYhEPFhvehEkRucgtCQsOzri3rXOqSfJS2XMojlct8oL%2FB%2BsR9IivYhPHRkhZOnw7AVeH6sw9fdvX2W1EEREfUERfVF8xOzwB2YIc69zK54JznPtQWsY7mI0B5geIAB3CsE2vAbg8NzciUiYfKkI9ElT1GvTgORBo9%2FHIeem4xBOJ0Qiwynh3hqdKASf735MucY2Lj4KFxpCkraHW3q%2FFLlq5JM2ZjOja12EWlumyERCYCNTM8W6uNIhTDgKAMNz7k70GOqUB4AO7q9gAG7S1tWoeHigP3cgzTGZ9JW%2FiIqllGK8WTmA3lprywYnzIQuUrozIWdVAbz%2FgoHSdFWHwiuHisGUlLos2gNKyxADVdr7G15qWc2mZ%2F5vsZY0bx1%2B0DG3V7oe8f7GEoemdngfn6eDPnrwdAbleIulHeCobS2wwFcA%2BTQ62d2H2kU6pxLCb0z4G%2BgeioDTWsfJcLNbjpMLKhNzLfSgLPSw3&X-Amz-Signature=5cf951d14943484a16a9d7a83ae3be70f0942544cc5f9b8e2e0e57e93653adab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYYWAPXU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDl%2BDlfZt6KcjhYrNiGFE9Eqi3T09DuhVBk4dW9IbyVhAiAi2LFHV2eAJT%2BOqGDOwpgzG0XFHBMz%2FvhQYe1hW6P%2FMCr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM4PrExIQG7ifz1LndKtwD69MBQWR4IHNU0Xld9yuZcx8jHH0H1eW86lG48MPNpFkgCAnXz8xfWDqpstk0eVNuExskVD5mEIC41FCPjfr983iJFLyyqDhfEij%2Bg0OzaM%2FXUZgeAso8VRWIPJ7TYyNajsOmJMQZhXSrLRh%2FZ0ynpKfl9FzAcPWtoA9Z7bJPM0nu7uYdEK5fM8sC8ja3lLyQnHFj%2BiioYfD8I%2FKk6%2BugAElxBx49cUS8BJxhCudVlmpimAjzaVTaZEYJRHhalnIPWnaM9ZzYF0wqa54ejrNxJEC3U5G5UVC8pVLi7u3AbSay13oJZmYMwGXaVfKBGVD8WOq0vGKlV5aC4BkYGGXUF08R4LFg4osSkfvnaNLbpf3l0cpgY%2BecouffE4SMaMFjpHXi7vXufiafBN2BOGILsmLwixURAzFCFwDtVPXGIwhhZGuGN7c6n2YGPgHXm1YAYwrlCEl8tqYurDRB6rhS8loIU%2FCZaEfL%2Fe8QndIJljy4JFE0pcM3wMFmdt7XsjAP1WD%2BOJACQTvSipQmFrCn2ZJGh%2B0yak3UisiotcA8tv6agFDukGNedlId%2BDxhLAurobwbQQ0NQdF%2BEiJZK3exld2M0lwpx8Zlbq8DvmFlCbrSDxHzrEygSG3SgU8wo%2FuTvQY6pgG4lH8FaJUGpMPBlVNSB25TmjSLtBv7sOLo%2B46WZkX%2FF%2BPK55e9eGvvEex%2FmtsLczQ67eNpGp2l2fOYROZw0T9avRWKFNbjF8ZvSk3cEBioVAOd2lmQbuQuhO1ZlN0g6vCEKo6B5gayBrI6rFbncLNHcTgXoYN3pFeX0noOOHf3WkBja1zx4bOACY3%2BzWuHgbzdXkzJoA16xJyGbtHQDyUaHmavyAT4&X-Amz-Signature=40ace54be1e1b22160af016b7f4a2ac51f876040c85856b00755cebf2a76d3f0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYYWAPXU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDl%2BDlfZt6KcjhYrNiGFE9Eqi3T09DuhVBk4dW9IbyVhAiAi2LFHV2eAJT%2BOqGDOwpgzG0XFHBMz%2FvhQYe1hW6P%2FMCr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM4PrExIQG7ifz1LndKtwD69MBQWR4IHNU0Xld9yuZcx8jHH0H1eW86lG48MPNpFkgCAnXz8xfWDqpstk0eVNuExskVD5mEIC41FCPjfr983iJFLyyqDhfEij%2Bg0OzaM%2FXUZgeAso8VRWIPJ7TYyNajsOmJMQZhXSrLRh%2FZ0ynpKfl9FzAcPWtoA9Z7bJPM0nu7uYdEK5fM8sC8ja3lLyQnHFj%2BiioYfD8I%2FKk6%2BugAElxBx49cUS8BJxhCudVlmpimAjzaVTaZEYJRHhalnIPWnaM9ZzYF0wqa54ejrNxJEC3U5G5UVC8pVLi7u3AbSay13oJZmYMwGXaVfKBGVD8WOq0vGKlV5aC4BkYGGXUF08R4LFg4osSkfvnaNLbpf3l0cpgY%2BecouffE4SMaMFjpHXi7vXufiafBN2BOGILsmLwixURAzFCFwDtVPXGIwhhZGuGN7c6n2YGPgHXm1YAYwrlCEl8tqYurDRB6rhS8loIU%2FCZaEfL%2Fe8QndIJljy4JFE0pcM3wMFmdt7XsjAP1WD%2BOJACQTvSipQmFrCn2ZJGh%2B0yak3UisiotcA8tv6agFDukGNedlId%2BDxhLAurobwbQQ0NQdF%2BEiJZK3exld2M0lwpx8Zlbq8DvmFlCbrSDxHzrEygSG3SgU8wo%2FuTvQY6pgG4lH8FaJUGpMPBlVNSB25TmjSLtBv7sOLo%2B46WZkX%2FF%2BPK55e9eGvvEex%2FmtsLczQ67eNpGp2l2fOYROZw0T9avRWKFNbjF8ZvSk3cEBioVAOd2lmQbuQuhO1ZlN0g6vCEKo6B5gayBrI6rFbncLNHcTgXoYN3pFeX0noOOHf3WkBja1zx4bOACY3%2BzWuHgbzdXkzJoA16xJyGbtHQDyUaHmavyAT4&X-Amz-Signature=b586caf90055a6503ec7d983daeb31c8f99daa3c7dddbaa477dfa84ec783e18c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
