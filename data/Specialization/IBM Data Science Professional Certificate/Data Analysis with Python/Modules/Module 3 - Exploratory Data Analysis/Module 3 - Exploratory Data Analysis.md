

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSJVJPAN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBGaxSodaWjFN2kzUehYVHgemMfePd%2BiEe%2F3aYv2YlHlAiAF8AT%2Fjq6SVJQOF332ThaG3BceygzRDEfJ5fXdYADgeiqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFIO2y0zpvz8hsj0WKtwDqEgYiR0JruMz2L0SKpNeZnFi4gRAWpfbaJHGjze064UfJUhEST3%2FOpHByA0RjXu4VzZsxtXgSaF3MyXibSut2c9UCnRuiL5T0ppmlV2JcN8tlrx%2B2asJ5F3rP3hYjt1%2FRN1uy5QSD8rdf3o%2BDeHeXdGvmF8ACIqrYqgL7NJdPJ08mKiSWE8Inzy6djOP4w38pTWuumxJ28yB4nyiPznMI2hT3kzwPA7Ia3Wbtl%2Fb4s6qfrvF4zfOcahYwLSHQVxECL3qD3I%2BIqu3HgQmhuqjGDySZMZ%2FsfOZReFF59OBt6unhMFTARaZYN7zSinbHyIwlMqRLCZnv2ZkHqaNXjVBO9PtyRAT7zSLOODRi1fArZHRm2UwaHzD5fTiSjtp7U6H3g3u5joybtI6bsXkbUrRxVjEMHg%2BGNO1d4sy9i5WPnb3AU%2BiJucb9QUmSrCM5dgkFVSbbBUlHEt1IOFS9nUevQfZxAAJu5zySfl3yPoiasChtFOgkEFYVLNmTu0Hkjsito%2FrCcONFNxSqXujweA5Vg75m7MNnboimKxlvG3K%2Ft4KRkh4v3zy4hLc6I%2BRvo33vmLd1TIVnfZRMfLqz6rk2SZNY0ewaVDZYEP%2FFHAidpuaFDwKt1ol4B1x9VswjOLvvAY6pgGmEcyYnOOfXDs8l7Fhv7mEVwiRFafZykRYp56jRev0LBrj%2BvEjOAfo6RmJPsRS4cuQAdkWuC1uqKNvdIgLRTJRAE6DHoCKATZZMKaPWqg6%2BMACppZ774dI%2BW%2BoET5PZvmCcjWfANF77yZuS3nDxTcBQMyF7gQyYkwOTgjNRtYtQfJIBwVP2XOLiRh7uzS8glaN1%2BEX5CGvqt6GCwMlVG1nJYnBm78R&X-Amz-Signature=2339971d9cbc5c01491d7a21b895230fe1be92c9e9a882eab19e0b5a010ffbea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSJVJPAN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBGaxSodaWjFN2kzUehYVHgemMfePd%2BiEe%2F3aYv2YlHlAiAF8AT%2Fjq6SVJQOF332ThaG3BceygzRDEfJ5fXdYADgeiqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFIO2y0zpvz8hsj0WKtwDqEgYiR0JruMz2L0SKpNeZnFi4gRAWpfbaJHGjze064UfJUhEST3%2FOpHByA0RjXu4VzZsxtXgSaF3MyXibSut2c9UCnRuiL5T0ppmlV2JcN8tlrx%2B2asJ5F3rP3hYjt1%2FRN1uy5QSD8rdf3o%2BDeHeXdGvmF8ACIqrYqgL7NJdPJ08mKiSWE8Inzy6djOP4w38pTWuumxJ28yB4nyiPznMI2hT3kzwPA7Ia3Wbtl%2Fb4s6qfrvF4zfOcahYwLSHQVxECL3qD3I%2BIqu3HgQmhuqjGDySZMZ%2FsfOZReFF59OBt6unhMFTARaZYN7zSinbHyIwlMqRLCZnv2ZkHqaNXjVBO9PtyRAT7zSLOODRi1fArZHRm2UwaHzD5fTiSjtp7U6H3g3u5joybtI6bsXkbUrRxVjEMHg%2BGNO1d4sy9i5WPnb3AU%2BiJucb9QUmSrCM5dgkFVSbbBUlHEt1IOFS9nUevQfZxAAJu5zySfl3yPoiasChtFOgkEFYVLNmTu0Hkjsito%2FrCcONFNxSqXujweA5Vg75m7MNnboimKxlvG3K%2Ft4KRkh4v3zy4hLc6I%2BRvo33vmLd1TIVnfZRMfLqz6rk2SZNY0ewaVDZYEP%2FFHAidpuaFDwKt1ol4B1x9VswjOLvvAY6pgGmEcyYnOOfXDs8l7Fhv7mEVwiRFafZykRYp56jRev0LBrj%2BvEjOAfo6RmJPsRS4cuQAdkWuC1uqKNvdIgLRTJRAE6DHoCKATZZMKaPWqg6%2BMACppZ774dI%2BW%2BoET5PZvmCcjWfANF77yZuS3nDxTcBQMyF7gQyYkwOTgjNRtYtQfJIBwVP2XOLiRh7uzS8glaN1%2BEX5CGvqt6GCwMlVG1nJYnBm78R&X-Amz-Signature=4e0131b114636677d04234a03d543e8784be0853fa5b5a40e975d781a1a9de10&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSJVJPAN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBGaxSodaWjFN2kzUehYVHgemMfePd%2BiEe%2F3aYv2YlHlAiAF8AT%2Fjq6SVJQOF332ThaG3BceygzRDEfJ5fXdYADgeiqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFIO2y0zpvz8hsj0WKtwDqEgYiR0JruMz2L0SKpNeZnFi4gRAWpfbaJHGjze064UfJUhEST3%2FOpHByA0RjXu4VzZsxtXgSaF3MyXibSut2c9UCnRuiL5T0ppmlV2JcN8tlrx%2B2asJ5F3rP3hYjt1%2FRN1uy5QSD8rdf3o%2BDeHeXdGvmF8ACIqrYqgL7NJdPJ08mKiSWE8Inzy6djOP4w38pTWuumxJ28yB4nyiPznMI2hT3kzwPA7Ia3Wbtl%2Fb4s6qfrvF4zfOcahYwLSHQVxECL3qD3I%2BIqu3HgQmhuqjGDySZMZ%2FsfOZReFF59OBt6unhMFTARaZYN7zSinbHyIwlMqRLCZnv2ZkHqaNXjVBO9PtyRAT7zSLOODRi1fArZHRm2UwaHzD5fTiSjtp7U6H3g3u5joybtI6bsXkbUrRxVjEMHg%2BGNO1d4sy9i5WPnb3AU%2BiJucb9QUmSrCM5dgkFVSbbBUlHEt1IOFS9nUevQfZxAAJu5zySfl3yPoiasChtFOgkEFYVLNmTu0Hkjsito%2FrCcONFNxSqXujweA5Vg75m7MNnboimKxlvG3K%2Ft4KRkh4v3zy4hLc6I%2BRvo33vmLd1TIVnfZRMfLqz6rk2SZNY0ewaVDZYEP%2FFHAidpuaFDwKt1ol4B1x9VswjOLvvAY6pgGmEcyYnOOfXDs8l7Fhv7mEVwiRFafZykRYp56jRev0LBrj%2BvEjOAfo6RmJPsRS4cuQAdkWuC1uqKNvdIgLRTJRAE6DHoCKATZZMKaPWqg6%2BMACppZ774dI%2BW%2BoET5PZvmCcjWfANF77yZuS3nDxTcBQMyF7gQyYkwOTgjNRtYtQfJIBwVP2XOLiRh7uzS8glaN1%2BEX5CGvqt6GCwMlVG1nJYnBm78R&X-Amz-Signature=762101bdcb56e29281d1f993a5e4599c4667d19b257892ebd5f4ebf9d9e941be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3HIFAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3luYXvmdrbVT%2BdarBKppuo2Hi6540UHFd8yM%2BRXVSzAIgc%2FKQkCj5rAjItMd0UgGSrPGYS20O9OxtsITekZuI74oqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJoCgS4%2BDZCu0Jv5ircA1rDY0SZlclHRWElX9IWMDe9Ci%2B1WrHm7dHfuGR429fQxnlsLB0Ehl%2B60uAU9DmL5gn7JHkZ8EIzS4CIGW6dS8iAlETvMYQ51FPmpOOSYTa9uUvFXwuoEaW1C9yqZvtKPe8rZM9vDUReJ7MeBd%2BFM6Qhtd2EgaKRAuvLKhM%2FUtSJ9pHTNRYLJo7Xtp7t1bfEZstl6f%2Be2RDxQjfUouVpg600KBZXdpi1%2FUyZXQ04syuHt%2FSMx5VwYR4dCs64RfNuz4MF9Xgq2C3jA9hKEsio4VlS9iHxZCXcOyjkHhwIFQqNSChB%2BCYwQJapIxiK2wtJ%2BhnlZJCHw0PHTIY0shcxn6WcY81I7VqcYJlk88KhK0wftAD5Bkoz8H5lzwVgcJPmHnD65iqbgrkzfi9ZjClpViOUiaUNsQkJxh5XHsaM8r6DLUzE8RdNYzy7bAr%2FqX9y%2BAzffOM3e66Pc1dUGAQRHLcp2jx%2BFrDlbMCZyGd7QT60%2FVGx8UeanZzCVtH32TekZKatCboAo9g%2FPjakOwwoqcLW1Fh4VNXKBdMGuqTPqaP4YanY4qnYQst7RqATvKjbahyI6dAEGUc718w9l9jbjigEg99UDEnKVbCiKx3cW%2FKsWfGQu1eCoij0w260MKXh77wGOqUBNQ4zHcKWs9ZglmNMqfvfM6Okcl3SRMyM7KAxpY21SrtGlUxeO%2BbD9i8E5CgXuyTqNT%2FLg033f7nFnpFDQCzSfF1fkMol08ZoROGYIWH0F0drEAy%2BebMpybX24sLtdMhAgk%2BepFy0kQKvTdrQZ7WJnMOopb1kQOBT7pIgVubEW7hKpJZcNXm%2FprX5OfL0gXoQL2X339S6gQ9MPrf0aJiMSFKuPx8h&X-Amz-Signature=c0ec77c1528c7608aef34107f227c5b9baf4d6d952f3708bba71d8310a6b33bf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3HIFAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3luYXvmdrbVT%2BdarBKppuo2Hi6540UHFd8yM%2BRXVSzAIgc%2FKQkCj5rAjItMd0UgGSrPGYS20O9OxtsITekZuI74oqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJoCgS4%2BDZCu0Jv5ircA1rDY0SZlclHRWElX9IWMDe9Ci%2B1WrHm7dHfuGR429fQxnlsLB0Ehl%2B60uAU9DmL5gn7JHkZ8EIzS4CIGW6dS8iAlETvMYQ51FPmpOOSYTa9uUvFXwuoEaW1C9yqZvtKPe8rZM9vDUReJ7MeBd%2BFM6Qhtd2EgaKRAuvLKhM%2FUtSJ9pHTNRYLJo7Xtp7t1bfEZstl6f%2Be2RDxQjfUouVpg600KBZXdpi1%2FUyZXQ04syuHt%2FSMx5VwYR4dCs64RfNuz4MF9Xgq2C3jA9hKEsio4VlS9iHxZCXcOyjkHhwIFQqNSChB%2BCYwQJapIxiK2wtJ%2BhnlZJCHw0PHTIY0shcxn6WcY81I7VqcYJlk88KhK0wftAD5Bkoz8H5lzwVgcJPmHnD65iqbgrkzfi9ZjClpViOUiaUNsQkJxh5XHsaM8r6DLUzE8RdNYzy7bAr%2FqX9y%2BAzffOM3e66Pc1dUGAQRHLcp2jx%2BFrDlbMCZyGd7QT60%2FVGx8UeanZzCVtH32TekZKatCboAo9g%2FPjakOwwoqcLW1Fh4VNXKBdMGuqTPqaP4YanY4qnYQst7RqATvKjbahyI6dAEGUc718w9l9jbjigEg99UDEnKVbCiKx3cW%2FKsWfGQu1eCoij0w260MKXh77wGOqUBNQ4zHcKWs9ZglmNMqfvfM6Okcl3SRMyM7KAxpY21SrtGlUxeO%2BbD9i8E5CgXuyTqNT%2FLg033f7nFnpFDQCzSfF1fkMol08ZoROGYIWH0F0drEAy%2BebMpybX24sLtdMhAgk%2BepFy0kQKvTdrQZ7WJnMOopb1kQOBT7pIgVubEW7hKpJZcNXm%2FprX5OfL0gXoQL2X339S6gQ9MPrf0aJiMSFKuPx8h&X-Amz-Signature=57fca3973067727692a62e98851dabc55eadb0d455a99010d9eb2f7df417dd40&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3HIFAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3luYXvmdrbVT%2BdarBKppuo2Hi6540UHFd8yM%2BRXVSzAIgc%2FKQkCj5rAjItMd0UgGSrPGYS20O9OxtsITekZuI74oqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJoCgS4%2BDZCu0Jv5ircA1rDY0SZlclHRWElX9IWMDe9Ci%2B1WrHm7dHfuGR429fQxnlsLB0Ehl%2B60uAU9DmL5gn7JHkZ8EIzS4CIGW6dS8iAlETvMYQ51FPmpOOSYTa9uUvFXwuoEaW1C9yqZvtKPe8rZM9vDUReJ7MeBd%2BFM6Qhtd2EgaKRAuvLKhM%2FUtSJ9pHTNRYLJo7Xtp7t1bfEZstl6f%2Be2RDxQjfUouVpg600KBZXdpi1%2FUyZXQ04syuHt%2FSMx5VwYR4dCs64RfNuz4MF9Xgq2C3jA9hKEsio4VlS9iHxZCXcOyjkHhwIFQqNSChB%2BCYwQJapIxiK2wtJ%2BhnlZJCHw0PHTIY0shcxn6WcY81I7VqcYJlk88KhK0wftAD5Bkoz8H5lzwVgcJPmHnD65iqbgrkzfi9ZjClpViOUiaUNsQkJxh5XHsaM8r6DLUzE8RdNYzy7bAr%2FqX9y%2BAzffOM3e66Pc1dUGAQRHLcp2jx%2BFrDlbMCZyGd7QT60%2FVGx8UeanZzCVtH32TekZKatCboAo9g%2FPjakOwwoqcLW1Fh4VNXKBdMGuqTPqaP4YanY4qnYQst7RqATvKjbahyI6dAEGUc718w9l9jbjigEg99UDEnKVbCiKx3cW%2FKsWfGQu1eCoij0w260MKXh77wGOqUBNQ4zHcKWs9ZglmNMqfvfM6Okcl3SRMyM7KAxpY21SrtGlUxeO%2BbD9i8E5CgXuyTqNT%2FLg033f7nFnpFDQCzSfF1fkMol08ZoROGYIWH0F0drEAy%2BebMpybX24sLtdMhAgk%2BepFy0kQKvTdrQZ7WJnMOopb1kQOBT7pIgVubEW7hKpJZcNXm%2FprX5OfL0gXoQL2X339S6gQ9MPrf0aJiMSFKuPx8h&X-Amz-Signature=0a157bed3586531f051012bfdd6959f9d0b380da54320173c264f20542cc1c7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3HIFAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3luYXvmdrbVT%2BdarBKppuo2Hi6540UHFd8yM%2BRXVSzAIgc%2FKQkCj5rAjItMd0UgGSrPGYS20O9OxtsITekZuI74oqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJoCgS4%2BDZCu0Jv5ircA1rDY0SZlclHRWElX9IWMDe9Ci%2B1WrHm7dHfuGR429fQxnlsLB0Ehl%2B60uAU9DmL5gn7JHkZ8EIzS4CIGW6dS8iAlETvMYQ51FPmpOOSYTa9uUvFXwuoEaW1C9yqZvtKPe8rZM9vDUReJ7MeBd%2BFM6Qhtd2EgaKRAuvLKhM%2FUtSJ9pHTNRYLJo7Xtp7t1bfEZstl6f%2Be2RDxQjfUouVpg600KBZXdpi1%2FUyZXQ04syuHt%2FSMx5VwYR4dCs64RfNuz4MF9Xgq2C3jA9hKEsio4VlS9iHxZCXcOyjkHhwIFQqNSChB%2BCYwQJapIxiK2wtJ%2BhnlZJCHw0PHTIY0shcxn6WcY81I7VqcYJlk88KhK0wftAD5Bkoz8H5lzwVgcJPmHnD65iqbgrkzfi9ZjClpViOUiaUNsQkJxh5XHsaM8r6DLUzE8RdNYzy7bAr%2FqX9y%2BAzffOM3e66Pc1dUGAQRHLcp2jx%2BFrDlbMCZyGd7QT60%2FVGx8UeanZzCVtH32TekZKatCboAo9g%2FPjakOwwoqcLW1Fh4VNXKBdMGuqTPqaP4YanY4qnYQst7RqATvKjbahyI6dAEGUc718w9l9jbjigEg99UDEnKVbCiKx3cW%2FKsWfGQu1eCoij0w260MKXh77wGOqUBNQ4zHcKWs9ZglmNMqfvfM6Okcl3SRMyM7KAxpY21SrtGlUxeO%2BbD9i8E5CgXuyTqNT%2FLg033f7nFnpFDQCzSfF1fkMol08ZoROGYIWH0F0drEAy%2BebMpybX24sLtdMhAgk%2BepFy0kQKvTdrQZ7WJnMOopb1kQOBT7pIgVubEW7hKpJZcNXm%2FprX5OfL0gXoQL2X339S6gQ9MPrf0aJiMSFKuPx8h&X-Amz-Signature=32eaacfc7e0baf0872233822151ff5b822c0c40872828bc8a6996dbe3964eff1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3HIFAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3luYXvmdrbVT%2BdarBKppuo2Hi6540UHFd8yM%2BRXVSzAIgc%2FKQkCj5rAjItMd0UgGSrPGYS20O9OxtsITekZuI74oqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJoCgS4%2BDZCu0Jv5ircA1rDY0SZlclHRWElX9IWMDe9Ci%2B1WrHm7dHfuGR429fQxnlsLB0Ehl%2B60uAU9DmL5gn7JHkZ8EIzS4CIGW6dS8iAlETvMYQ51FPmpOOSYTa9uUvFXwuoEaW1C9yqZvtKPe8rZM9vDUReJ7MeBd%2BFM6Qhtd2EgaKRAuvLKhM%2FUtSJ9pHTNRYLJo7Xtp7t1bfEZstl6f%2Be2RDxQjfUouVpg600KBZXdpi1%2FUyZXQ04syuHt%2FSMx5VwYR4dCs64RfNuz4MF9Xgq2C3jA9hKEsio4VlS9iHxZCXcOyjkHhwIFQqNSChB%2BCYwQJapIxiK2wtJ%2BhnlZJCHw0PHTIY0shcxn6WcY81I7VqcYJlk88KhK0wftAD5Bkoz8H5lzwVgcJPmHnD65iqbgrkzfi9ZjClpViOUiaUNsQkJxh5XHsaM8r6DLUzE8RdNYzy7bAr%2FqX9y%2BAzffOM3e66Pc1dUGAQRHLcp2jx%2BFrDlbMCZyGd7QT60%2FVGx8UeanZzCVtH32TekZKatCboAo9g%2FPjakOwwoqcLW1Fh4VNXKBdMGuqTPqaP4YanY4qnYQst7RqATvKjbahyI6dAEGUc718w9l9jbjigEg99UDEnKVbCiKx3cW%2FKsWfGQu1eCoij0w260MKXh77wGOqUBNQ4zHcKWs9ZglmNMqfvfM6Okcl3SRMyM7KAxpY21SrtGlUxeO%2BbD9i8E5CgXuyTqNT%2FLg033f7nFnpFDQCzSfF1fkMol08ZoROGYIWH0F0drEAy%2BebMpybX24sLtdMhAgk%2BepFy0kQKvTdrQZ7WJnMOopb1kQOBT7pIgVubEW7hKpJZcNXm%2FprX5OfL0gXoQL2X339S6gQ9MPrf0aJiMSFKuPx8h&X-Amz-Signature=53a3a9a37245b89ffd8cef77f4c46531b9914da30ebb83da015677553f8e853f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3HIFAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3luYXvmdrbVT%2BdarBKppuo2Hi6540UHFd8yM%2BRXVSzAIgc%2FKQkCj5rAjItMd0UgGSrPGYS20O9OxtsITekZuI74oqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJoCgS4%2BDZCu0Jv5ircA1rDY0SZlclHRWElX9IWMDe9Ci%2B1WrHm7dHfuGR429fQxnlsLB0Ehl%2B60uAU9DmL5gn7JHkZ8EIzS4CIGW6dS8iAlETvMYQ51FPmpOOSYTa9uUvFXwuoEaW1C9yqZvtKPe8rZM9vDUReJ7MeBd%2BFM6Qhtd2EgaKRAuvLKhM%2FUtSJ9pHTNRYLJo7Xtp7t1bfEZstl6f%2Be2RDxQjfUouVpg600KBZXdpi1%2FUyZXQ04syuHt%2FSMx5VwYR4dCs64RfNuz4MF9Xgq2C3jA9hKEsio4VlS9iHxZCXcOyjkHhwIFQqNSChB%2BCYwQJapIxiK2wtJ%2BhnlZJCHw0PHTIY0shcxn6WcY81I7VqcYJlk88KhK0wftAD5Bkoz8H5lzwVgcJPmHnD65iqbgrkzfi9ZjClpViOUiaUNsQkJxh5XHsaM8r6DLUzE8RdNYzy7bAr%2FqX9y%2BAzffOM3e66Pc1dUGAQRHLcp2jx%2BFrDlbMCZyGd7QT60%2FVGx8UeanZzCVtH32TekZKatCboAo9g%2FPjakOwwoqcLW1Fh4VNXKBdMGuqTPqaP4YanY4qnYQst7RqATvKjbahyI6dAEGUc718w9l9jbjigEg99UDEnKVbCiKx3cW%2FKsWfGQu1eCoij0w260MKXh77wGOqUBNQ4zHcKWs9ZglmNMqfvfM6Okcl3SRMyM7KAxpY21SrtGlUxeO%2BbD9i8E5CgXuyTqNT%2FLg033f7nFnpFDQCzSfF1fkMol08ZoROGYIWH0F0drEAy%2BebMpybX24sLtdMhAgk%2BepFy0kQKvTdrQZ7WJnMOopb1kQOBT7pIgVubEW7hKpJZcNXm%2FprX5OfL0gXoQL2X339S6gQ9MPrf0aJiMSFKuPx8h&X-Amz-Signature=33c314da8b62f4ada250c4a3b6f3af21250e889ab787cc33deac6d8d79d5f3c8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466645SZUIO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRhWavdc8QGhec%2F2xZpsiGUNriwSShomje5UwxHyL9xQIgBo9GTYrJ46DrnqjOfOp64NcxxAee3xg4LWtldfmmNFsqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBQX92v6kR2M1GaImyrcA%2BOA11JKutr%2ByqBQyvQodiRUeLfIq5udLE9%2FKoIaNaUaUbJg4n4yFTryrMjFieIUmpIpEnctGvft2q2Dpzl5wsc7vuhffIWowrDqNkos9RFuDnHwMqZ6Y%2BACbgxGRSeqtsIOF4h5PqCEIsQjedjiAEKX12HPRWCAbc3rdlC62wCAWOM5osjbq6SApnkWYoHkvN%2BkpeJj8gD8vwlXoSI4udp9LVmm5gbX%2BgFEkybW2D9IgjCIue4G5GMnH4I6wQViM3NiAy%2FvHR3j1QK56xFoM5cCcoEne0HFFj3xWAEop%2BSr6hNsP6GiXG1OWpZzDT8S0k%2FcANCmU4wpZYz8nFe6gO7ZLC1Ws3ecnUsrIa%2FoSL2SMvMboVo6XykGz3zBrTOOPA5k%2B1OJJmXjG6OCctOWE5x3Z95dy7oHDS7eJjxOcqQv36wkfxPz2NSfGNYEENxeuviey4R78Va52aF7RlKYmkCHnepKuXCLnjjc4CHI%2B%2Fsm%2B2zhWfuNtjhHs07YdFF%2BtCghd8D9az80AWxuSR1w50NwwYe%2BGUQDY0mASOFyBKMTRmrzOGOEUxTV47mTe584njQ3rinzlwg%2FjQV1oHbiNvniWwRTJhd51kjfTqjQ1gJhNG8KGF04aLwfx5YrMMbh77wGOqUBQmC%2Fre2N2j8LDXK5PjogGLGIcGJVlSsVAGt7XFhNVbQ6QmsmyTy70ajXjf0hOpevtJhhcbBOWaLRKSI9B1kj7yWgcgi%2B8QfnNTuD4HkiCED34vFBGbp8U0sRydOg3nNyW%2Bwf7A5UGkMcnhnZa%2FbMdaY2jBt%2BjVS9OFl6RQwpEkHIxrrzawDKJ50pPKvEqsjZ9HEq6M4ZUbardTpK%2FTcNBN07XIKA&X-Amz-Signature=1981edfa655876ce0fbc194c19ad9cd0b364b9253f82504d5ef8242ad057b4b0&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVPA33JX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5f5WvV9Angyr1UiKoj3YsP%2BuXOyQBDtJYeQ6IKEWnpAIhAPv6HnSCpbcYGqCDz0A3T4hrzjvFg5ZDiW5bahZbKRXXKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz1VauN3pwR3QIkD90q3AP%2FNvniw%2F586ZHNTg%2BZC2BEBX3nshyau8j3mNvEwwqYJc7Xt8gva7Wa9C%2FQUTyELWv9ZaxTbeY1gYbPKBk4t00RhLD7UUCFsWuzFHa7CA027BcePC0m4%2BSN2ocH4CTbpO5RccYgU0FWLuid7yzhhvucDA6xaBQBlwOTNtlY0ChLvNW1SamRo4dsoqhHjHYfOqop9P9g60L6H%2BlnXPK%2B3mba%2BsTLTL1PlAGIzoU4K2rJbTkZcO6ugIK1Kxh3j2xwH8hD5vJ%2But23odObU45Y0h57rO7ZNd6FGqMa0pr3uBnuB3VholeBuLhRSpkbev7hRPCiFa6fd812M9W8D0FUn0VEpCGm0W9C8JMa9mxI5YBD0z5Kl9iRQt5cmVUAqBIIfPbaXVbV2EAO7w5AnYGXM77KMnGvIX9UHs2UoluONqH64zPQcjdMtzNgmyf2DGZDdyHruSldJgrRTj4Ghyk8EOqr0cCNz9Ys9oPfa1unioivAhqyhKDJi%2Bzhypj%2F4%2B%2BCFsJIDaXMshjHispog%2BMayjLKMo50stRmnXJcFIa53%2F8nasFH%2BFd3zNOgujy3XFJQkB%2BLRb38wSR6sPPEe61aMvfIJtSrqqXWr3RNezfG8%2BGHJzhl5l%2FYGMvlXdhWbjCI4e%2B8BjqkAW2zEAq8fCBCgagje6bLbLp8vWCOVA3IOSGBsYkYsGDlpfHWa41wT4u5rsCk3%2BVyu1MWqQzfzeRm8EjDyGwgQfmLAVWV%2BcmeZ5OvtQxXp%2BRK3hpbnTB4RoU%2BCfaPILECS5uGSqlU0ORLXF23LCwA3OMcS8eJqY8eJsXZu2O%2FdgoS5Xth9slMnIYKbsTAUgC9jZn%2BqNSonhx8OKS7RyAGmwQKEZwW&X-Amz-Signature=58069cbed899d01e1c4557c2a111505ccb94afbb55a5b1b6abc00e3005980747&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3HIFAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3luYXvmdrbVT%2BdarBKppuo2Hi6540UHFd8yM%2BRXVSzAIgc%2FKQkCj5rAjItMd0UgGSrPGYS20O9OxtsITekZuI74oqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJoCgS4%2BDZCu0Jv5ircA1rDY0SZlclHRWElX9IWMDe9Ci%2B1WrHm7dHfuGR429fQxnlsLB0Ehl%2B60uAU9DmL5gn7JHkZ8EIzS4CIGW6dS8iAlETvMYQ51FPmpOOSYTa9uUvFXwuoEaW1C9yqZvtKPe8rZM9vDUReJ7MeBd%2BFM6Qhtd2EgaKRAuvLKhM%2FUtSJ9pHTNRYLJo7Xtp7t1bfEZstl6f%2Be2RDxQjfUouVpg600KBZXdpi1%2FUyZXQ04syuHt%2FSMx5VwYR4dCs64RfNuz4MF9Xgq2C3jA9hKEsio4VlS9iHxZCXcOyjkHhwIFQqNSChB%2BCYwQJapIxiK2wtJ%2BhnlZJCHw0PHTIY0shcxn6WcY81I7VqcYJlk88KhK0wftAD5Bkoz8H5lzwVgcJPmHnD65iqbgrkzfi9ZjClpViOUiaUNsQkJxh5XHsaM8r6DLUzE8RdNYzy7bAr%2FqX9y%2BAzffOM3e66Pc1dUGAQRHLcp2jx%2BFrDlbMCZyGd7QT60%2FVGx8UeanZzCVtH32TekZKatCboAo9g%2FPjakOwwoqcLW1Fh4VNXKBdMGuqTPqaP4YanY4qnYQst7RqATvKjbahyI6dAEGUc718w9l9jbjigEg99UDEnKVbCiKx3cW%2FKsWfGQu1eCoij0w260MKXh77wGOqUBNQ4zHcKWs9ZglmNMqfvfM6Okcl3SRMyM7KAxpY21SrtGlUxeO%2BbD9i8E5CgXuyTqNT%2FLg033f7nFnpFDQCzSfF1fkMol08ZoROGYIWH0F0drEAy%2BebMpybX24sLtdMhAgk%2BepFy0kQKvTdrQZ7WJnMOopb1kQOBT7pIgVubEW7hKpJZcNXm%2FprX5OfL0gXoQL2X339S6gQ9MPrf0aJiMSFKuPx8h&X-Amz-Signature=079d88576560ff90ef7e2e6cc69116a156639ead63e91440190dca92e39ceaa4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3HIFAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3luYXvmdrbVT%2BdarBKppuo2Hi6540UHFd8yM%2BRXVSzAIgc%2FKQkCj5rAjItMd0UgGSrPGYS20O9OxtsITekZuI74oqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJoCgS4%2BDZCu0Jv5ircA1rDY0SZlclHRWElX9IWMDe9Ci%2B1WrHm7dHfuGR429fQxnlsLB0Ehl%2B60uAU9DmL5gn7JHkZ8EIzS4CIGW6dS8iAlETvMYQ51FPmpOOSYTa9uUvFXwuoEaW1C9yqZvtKPe8rZM9vDUReJ7MeBd%2BFM6Qhtd2EgaKRAuvLKhM%2FUtSJ9pHTNRYLJo7Xtp7t1bfEZstl6f%2Be2RDxQjfUouVpg600KBZXdpi1%2FUyZXQ04syuHt%2FSMx5VwYR4dCs64RfNuz4MF9Xgq2C3jA9hKEsio4VlS9iHxZCXcOyjkHhwIFQqNSChB%2BCYwQJapIxiK2wtJ%2BhnlZJCHw0PHTIY0shcxn6WcY81I7VqcYJlk88KhK0wftAD5Bkoz8H5lzwVgcJPmHnD65iqbgrkzfi9ZjClpViOUiaUNsQkJxh5XHsaM8r6DLUzE8RdNYzy7bAr%2FqX9y%2BAzffOM3e66Pc1dUGAQRHLcp2jx%2BFrDlbMCZyGd7QT60%2FVGx8UeanZzCVtH32TekZKatCboAo9g%2FPjakOwwoqcLW1Fh4VNXKBdMGuqTPqaP4YanY4qnYQst7RqATvKjbahyI6dAEGUc718w9l9jbjigEg99UDEnKVbCiKx3cW%2FKsWfGQu1eCoij0w260MKXh77wGOqUBNQ4zHcKWs9ZglmNMqfvfM6Okcl3SRMyM7KAxpY21SrtGlUxeO%2BbD9i8E5CgXuyTqNT%2FLg033f7nFnpFDQCzSfF1fkMol08ZoROGYIWH0F0drEAy%2BebMpybX24sLtdMhAgk%2BepFy0kQKvTdrQZ7WJnMOopb1kQOBT7pIgVubEW7hKpJZcNXm%2FprX5OfL0gXoQL2X339S6gQ9MPrf0aJiMSFKuPx8h&X-Amz-Signature=561b44e4afd8859f422144269f7ecaa56c16f1525bd3c874fe67d4e60c4843f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3HIFAF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3luYXvmdrbVT%2BdarBKppuo2Hi6540UHFd8yM%2BRXVSzAIgc%2FKQkCj5rAjItMd0UgGSrPGYS20O9OxtsITekZuI74oqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJoCgS4%2BDZCu0Jv5ircA1rDY0SZlclHRWElX9IWMDe9Ci%2B1WrHm7dHfuGR429fQxnlsLB0Ehl%2B60uAU9DmL5gn7JHkZ8EIzS4CIGW6dS8iAlETvMYQ51FPmpOOSYTa9uUvFXwuoEaW1C9yqZvtKPe8rZM9vDUReJ7MeBd%2BFM6Qhtd2EgaKRAuvLKhM%2FUtSJ9pHTNRYLJo7Xtp7t1bfEZstl6f%2Be2RDxQjfUouVpg600KBZXdpi1%2FUyZXQ04syuHt%2FSMx5VwYR4dCs64RfNuz4MF9Xgq2C3jA9hKEsio4VlS9iHxZCXcOyjkHhwIFQqNSChB%2BCYwQJapIxiK2wtJ%2BhnlZJCHw0PHTIY0shcxn6WcY81I7VqcYJlk88KhK0wftAD5Bkoz8H5lzwVgcJPmHnD65iqbgrkzfi9ZjClpViOUiaUNsQkJxh5XHsaM8r6DLUzE8RdNYzy7bAr%2FqX9y%2BAzffOM3e66Pc1dUGAQRHLcp2jx%2BFrDlbMCZyGd7QT60%2FVGx8UeanZzCVtH32TekZKatCboAo9g%2FPjakOwwoqcLW1Fh4VNXKBdMGuqTPqaP4YanY4qnYQst7RqATvKjbahyI6dAEGUc718w9l9jbjigEg99UDEnKVbCiKx3cW%2FKsWfGQu1eCoij0w260MKXh77wGOqUBNQ4zHcKWs9ZglmNMqfvfM6Okcl3SRMyM7KAxpY21SrtGlUxeO%2BbD9i8E5CgXuyTqNT%2FLg033f7nFnpFDQCzSfF1fkMol08ZoROGYIWH0F0drEAy%2BebMpybX24sLtdMhAgk%2BepFy0kQKvTdrQZ7WJnMOopb1kQOBT7pIgVubEW7hKpJZcNXm%2FprX5OfL0gXoQL2X339S6gQ9MPrf0aJiMSFKuPx8h&X-Amz-Signature=3fd6d1d805af3500499225bd3a4bbd33bf33a518e46161c4ac175bd65e58819f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJYRFV26%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGtSNvGcw%2F5Of%2Bu1usV%2F7thrQrdDgaxc919Z2QuY0LNWAiAN7peVDSRLEPS0VCGFOVswSMwvomz4TsXTDcXy%2B0QZ9SqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKOVKE1zjIi7i4yCzKtwD9ZLz%2BihiDmKKPwRg9iZqYh9pAlA09PQE0oYP4JlPWrTZYJEaR%2BEXZvgy05S3KkgDYV4dvpigHxYYkJSrP9nJmYmbs2b3xjJxYdcEZ2buliiiDtSzvFP%2FyzI%2FWl9RHF74krYdrGj2b7Rg1JEUXQe3E1DvkCgXB08%2BTCu1KR0e%2BVX42dTepi19X5PIVkL1KG0bSeVMro%2FL4Oo2m963ZELVDbPp1U52SSdy4MIX6PSK2TiR5r50qJqW1Sj2Nb0zzLSROgKWC9xcQFmRSOE8GbyLCeX4i7dwlhT9yFxiZ1G5Fvv0FkTRf7xDz2z%2FX50d6s6QWqw%2BS2ShOVZLmy9WmVgzAgP2U5EsEkCgchuk4IMRGteCEPuox75Sq6X1%2B%2FPlwTz2ihIMVQ190rrv3MNUcMWOx1lRoe7mX4sRmwiuFQlSSsxGRZmg3ufTDhMCLau4qJsZk6KdBTAay9E3db6GeJIDhROo6qlZ4wDDuj2cj0sOroiSwVlbStZAVm17kzn%2BgGjvgRsmwO5wbKsSNDf2Totner5%2FiBFkLoh2f0SW%2B0rB2f%2FGSfRZJbqCnYweOwivKUMKFUVwAdq%2BBlG4C5E6bc8Dno9d5UW0%2B3LE0phPacIbXTH9DnsFiBUkyb17boow5ODvvAY6pgEoEKm2VPYPKIwUi9VWrxUKIQzG2eBfFnMEYbrctlvWre6ZcY8fTQSwKcTsmkYDRps4bKtu%2FDwifiOtcguOadeR%2BmKToOFTwhIC4WhCYe3tnBgeh2MYIhXGOcG7xweREoTSVFM7pdz0UHr5l5%2FoUBjpjwhXNG4fRhA2K27vf%2BvmUfyjucMRrU6FKi%2BbztMenPknw73RZBWSJBzqLSTsAQPyjb1HWofb&X-Amz-Signature=e9f08bbbfc62ffb6c4dcbc5e0a5079d90c5be65a219c24df9c9940bb7758852b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGZ2GI2S%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUpTUQOo%2B14td2gUykG53j72QyW1Inpx7kyPN%2BoF%2BUJAIgPeKG6RDtCfpaK91qF2g29gaRvg3e6a4vxIKcruyKnPkqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpbB9d0hrCV3%2F%2F8pSrcA%2FAT7vte8s2MvcfJ3NAQx%2FIzmF%2F2dLNs2hWgTxyD0ZtP%2FI%2FobOPWLrvOo%2FAbdiao%2Fo0KbXEx%2B%2F%2FEFVLYvPUtWBD%2BGEwpIrCRzskz0GSPgoSQapzpKBqN85QreqBXBBJr0iWvCZ3rmPlvfyNomHs2Nzbgq55UN7rXJ01%2FCdzkt6KmKhy9YfzSdGMH7oDG4MPWUxF8emaKIHUAHJsnEWBm97f5JE15YOTdUWYjLj1vphccVryNcwH3hV38Zv2JPimLuK0kJdDonusKDTXRFfomgoyHTGnRM9HfVHf3dJh3AksaucEj%2B8q9kY2EAp1Ze%2F95UdWv5QSINcHawgjEjCQz5CiXDTu5cb0ALvJ18LViXYx3ogLacJtMiym1C28908kkjSZuuyAM8iMbizIiL1AubxUNbNXVdGC5r0iW%2FqeVNHjxZ2s2sEzaTglE4uggVljH5jwngAEloFQJRLSj3siPOkVABkxXyHDRMfObUhJbmZLSUlRJ%2BHoND9%2FX0JvJPXkbUhSESL0HRWS0s%2FcE0IiSyWQoHmIQcD%2BAmY1ICf7FG%2Bb4yDlkDCqWttjfn7q2eHbjLPmpUbDlzwMFj53xUUOEsAV964d5MXTTFRi0GMOdwNR9SXEiXrzanTm3TwSRMOfg77wGOqUBrjHMrcpu4ROy3dCILLsvMIshhoH6dcLRsU49l6%2Bw%2B0zMuDjZol5XWEP7umlj3s1bg4TpCaFkTZ1hcTwcMt7fi9FswEKXWa%2BW1Dopqez%2FskAWsLcxDXWUP4%2B0eHjtIqtbJ7ZRcX4qPvZ438QRAbpko7oimsl5%2BEkfwncv8gr5ippY9SW9PS7unAtK%2FHZ5378%2BgXevREUpkWsMslRxnUj5Ado55%2Ff1&X-Amz-Signature=95971ff880e7ba5dd9bb5229661a0264bca3f2a405800667e2248ce8f36fcbdc&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTEDCKK5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT0b0k9UjHO3VXjmaIfEJp%2FN99PY%2BITj2aRpWlgAi2xwIhAISlhMsWlHF8d72l%2BPSsMPj%2FZEyBRBP6CYDlCqfMcM4UKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzaTnM4vHF6doVcD8Yq3ANuEPtklzqv5qE0bIQSwB%2FtqIdhWaP%2FIcPRWp6gvr3qO4918dgYG3YsAnIJmzUEDVzoknsHzgngaUFRAEcYSV6D5gGnmGkwylM8xRkjKDjtf5m7J%2Bvna8x%2BCb2gO6ISciQswrVjMGd2O%2BEstMpGRoqwZWh%2FzSEZZioX7%2BqGdMECDSHp%2BFy50JnHecdNNotfEb%2BD0KtRFft4yrKLG25hErDHqsDEHhj2RcCXSY%2BgA67U2YxOAndBwDT%2B4FEhcZtBixz2eFDisT0AavzW4Pd8DN0P1eg2wbkLgj6kpfiRbuYbUBRcmAwWlkEJrPkpwVWcNdjPa2l6NK158g0%2FdG8lxejwyIuSEo%2BPden7iPUyBNy71h70ZaMvKHFCPLjq0QYGg5Qap5yvGI83MdmCx3mQR8aeBO5vHU8XHXYJmi7sOnUvgiOvLdUKrX%2BWrhRk%2FT6eCMMnUaO0dU%2FK1onDIVpdNFnsPIRKlsEXe8EyXBDENkRoaz3ZcrF1DV8xjK0BasaOIZZsv5%2FmFBedveOvpYAAOpLPrtCktYWrSGhy9lIrx7wxpBtjCJxch8070TktYERDPXFmr4yvy41HYXUx1HA0dmUFtgHoRGbs%2B5WDvP1kKiWxumDjPrASeHKbaMwXAzD%2B4O%2B8BjqkAS4cSY5ZMMhR1gTVUA%2FOpyrDHI4tiIoSfSwtG7izH63d1%2BO8%2B3Y0rqiQAVukNiu5gcfmeNbbxpzmffZfH%2BisE922yc8YiKfwMiG14f3cKKi1j7oAnGsbOn1PaIB6xgBcRYF2iIidljxfrZ0nkflBqJSjA5XYjeHtJXwUZWnxw0HMxFEtYsQGq%2FtQoXUKnsMOp%2FKPik6Y%2FVzulSEdVeVC1fKNqwvq&X-Amz-Signature=b067507ca3647fe984725d4e26f36a0a86d229f5a953054c67cacaec903a904d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2JN5HLJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7E2QBbEx0Q6WtdyBkUzopH7x9NQQ3ijqvFDNBPb3ZZgIgCWomZ3BBBf%2Ft%2Bm28rI4KbYOaRxjQBccFu4ak48w3bO8qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdDzGT%2BQWedICnbXyrcAz5RzqCp68VCW2y0%2FIzdlk9CyW%2B6IS5dx1sjE7x6csH3dHFk5Ux%2Bowhjpza0C3S7GKcFbZMCcgRgcFP1s%2FohO%2BD4DolRHzR%2FXjPe8i9EJWtG4PP60z2yiXSYe%2FHBygpSZBfJyYqlttiOQRrZgl9eBSHjycqsxiOcJ6LP%2Bj4tqbs14qQ1me0OrTjbjQanIjEpTrYJyyvUbJD%2Bd1%2FCqr%2FqbEJtJn873qEgVC6t7O9eoP7nIxm0pXpN3NZbbsVy33eG%2Bvqk1UTuINTv2gRzAs03KkNyyDcw%2F0epKhAABO8M0BLI87u9sR0Zuw3Hj5iB4r%2F7dHeWiwgkTuqqJ2%2BdBLUohYZVSwJ28F9sKJlTLSaWHN%2BOJla7siuRTXk%2B1QqXk%2BfqQEHNyShY7l41OAa%2FdUrHYHxMl8%2FclHb20z2E2BQzUv1QjTXNUG6f8r6GJ9iSaKVDGk8JMuP0HojJ2ZwKxADoXbT6M3y5AJDMH5CDFLWenukzmp9QXD036coiB9ZwF9QEe6gnpuMoVd%2FlnP%2F4xR0m8Ku7f9JJAzr0vqDWg8h9NvL9WE5j7%2BTf7yLZasysPJTRVoPcLD2%2FUqAjzyVXkfXWCinTW1vLmEl28aXNnaqgb4Gdjxh%2FPjH1GcJPdNdRMOTg77wGOqUBEqk7DvHCh4p6izd7mBDNeqJVCS92s22iGI5zQZjRRsZhXBoVLBwG0fE%2BG1Vx4leN68g4khtDvn%2FNUJmCpKpQhgatOZAsp6qTGJhVEqHywgNW9z6%2FcdaqKZ08ZmyF%2Fo7BSkJ8GcVMjz6%2FyGlaXeAoYbbpEkaeRUuKGK21VYI0XvS3BooaJQfpPsWIfgTHYHRPAwabzDDPIfb3kCS8kyN7NbRgE%2Bq7&X-Amz-Signature=ac96d34d9c9f10141662b67944abaac3b0d7b42956b37227242c249abd5c1c77&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2JN5HLJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7E2QBbEx0Q6WtdyBkUzopH7x9NQQ3ijqvFDNBPb3ZZgIgCWomZ3BBBf%2Ft%2Bm28rI4KbYOaRxjQBccFu4ak48w3bO8qiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdDzGT%2BQWedICnbXyrcAz5RzqCp68VCW2y0%2FIzdlk9CyW%2B6IS5dx1sjE7x6csH3dHFk5Ux%2Bowhjpza0C3S7GKcFbZMCcgRgcFP1s%2FohO%2BD4DolRHzR%2FXjPe8i9EJWtG4PP60z2yiXSYe%2FHBygpSZBfJyYqlttiOQRrZgl9eBSHjycqsxiOcJ6LP%2Bj4tqbs14qQ1me0OrTjbjQanIjEpTrYJyyvUbJD%2Bd1%2FCqr%2FqbEJtJn873qEgVC6t7O9eoP7nIxm0pXpN3NZbbsVy33eG%2Bvqk1UTuINTv2gRzAs03KkNyyDcw%2F0epKhAABO8M0BLI87u9sR0Zuw3Hj5iB4r%2F7dHeWiwgkTuqqJ2%2BdBLUohYZVSwJ28F9sKJlTLSaWHN%2BOJla7siuRTXk%2B1QqXk%2BfqQEHNyShY7l41OAa%2FdUrHYHxMl8%2FclHb20z2E2BQzUv1QjTXNUG6f8r6GJ9iSaKVDGk8JMuP0HojJ2ZwKxADoXbT6M3y5AJDMH5CDFLWenukzmp9QXD036coiB9ZwF9QEe6gnpuMoVd%2FlnP%2F4xR0m8Ku7f9JJAzr0vqDWg8h9NvL9WE5j7%2BTf7yLZasysPJTRVoPcLD2%2FUqAjzyVXkfXWCinTW1vLmEl28aXNnaqgb4Gdjxh%2FPjH1GcJPdNdRMOTg77wGOqUBEqk7DvHCh4p6izd7mBDNeqJVCS92s22iGI5zQZjRRsZhXBoVLBwG0fE%2BG1Vx4leN68g4khtDvn%2FNUJmCpKpQhgatOZAsp6qTGJhVEqHywgNW9z6%2FcdaqKZ08ZmyF%2Fo7BSkJ8GcVMjz6%2FyGlaXeAoYbbpEkaeRUuKGK21VYI0XvS3BooaJQfpPsWIfgTHYHRPAwabzDDPIfb3kCS8kyN7NbRgE%2Bq7&X-Amz-Signature=5b343c6f507fc2f229d5addaa933bc27b48d6ea59dd5a950bc18f957e19c1823&X-Amz-SignedHeaders=host&x-id=GetObject)

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
