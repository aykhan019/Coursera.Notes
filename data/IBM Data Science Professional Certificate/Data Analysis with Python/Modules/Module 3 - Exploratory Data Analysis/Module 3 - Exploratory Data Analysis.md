

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUAVE36G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCghfo6rvdl5FFeS3GAuLoCJvScUJbxf0SQN9i9gzRCJwIhAKoY%2BJD9mGQECYFZdBIqXs2abg8Wa5bpULDIKz88wiowKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXmLNPeILBGsXSKWMq3ANpfrtQKU%2F1QTovG77d64XulGLRt%2F%2FDxDLlYb%2F7j%2BbFXhn32DAi81xQPSfPnV8U%2BmWH9LMi%2FdtBHYjMMzBrIM3h1Au7gICCFIDof%2FrRPpCY6qyKIRWxuj%2FykhSW0C%2FrPAvZlq9fhf%2Fit3xuVtfSVti04dWHSzRqM3I4TdZ4%2FqN3CkQ1Yc%2Fc3W0b1p9ZSLuNl%2FM4C8eRPSLGzMmtL5rDuPh6%2Fa%2FKmlcL19T6XubxzBr3dX2r9cCdY9ZTirXgk9YGahN07JbAhacPkiWd0%2BdWxKcGguiLuLTL57%2BO0eBCLb9h6seTcYxULNf8wqPSpvi3SoBR1fHHSMV64aEfo0WfslYVGDGyQ2NC4O3zMM2QHnOhzM75g539%2BhYnRk8pzcvm71AISimLNVoFAwaHBzmVswgjidXqSpGJY31kJnqM7P0Q2DdH%2FHINXidVANcnpLW03LS78L46Yfkyf2QIRyUW1tgOdOpQDpM%2FpYrtesjDoHhr9XjIxPLlHHH1941pa9s6Dh0%2F0WbZD0OGvfpHxC01l5UoEKWKJr5MdsJHFYJ97qqP0lW0pAqxWsSrv3jrMCMJp0rJDYFjF9vVhPj7U2smV04Y3%2BSDDgqTS9MZw6DhV6OkSsbmP6%2BmhTAoBE07xDC475u9BjqkATfuctTPZgPNS%2BLC3aouLxH98ffdFtvaUerpqG1zxsr%2BQyRgn3siU3XaolCoC3JD7Yi7esJdlXmaq%2Biork1Gj4YnS2wZRwT8LqWRA9GYLspEK60x%2BsKrqUdpOUbvVcgrb%2FwsjNuOb0kQVXhJacOxREW8qcx%2FhYjVYvK0llmpyn4aSrwtZ6UmAjMggbChjPJ4Aqm9w5tgvbFm4m4yJJ03ecrUQvac&X-Amz-Signature=f79d02218ec695a4f0c6754617d5ba6de50c5c537bfc3fe697cdd03ced6bfb6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUAVE36G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCghfo6rvdl5FFeS3GAuLoCJvScUJbxf0SQN9i9gzRCJwIhAKoY%2BJD9mGQECYFZdBIqXs2abg8Wa5bpULDIKz88wiowKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXmLNPeILBGsXSKWMq3ANpfrtQKU%2F1QTovG77d64XulGLRt%2F%2FDxDLlYb%2F7j%2BbFXhn32DAi81xQPSfPnV8U%2BmWH9LMi%2FdtBHYjMMzBrIM3h1Au7gICCFIDof%2FrRPpCY6qyKIRWxuj%2FykhSW0C%2FrPAvZlq9fhf%2Fit3xuVtfSVti04dWHSzRqM3I4TdZ4%2FqN3CkQ1Yc%2Fc3W0b1p9ZSLuNl%2FM4C8eRPSLGzMmtL5rDuPh6%2Fa%2FKmlcL19T6XubxzBr3dX2r9cCdY9ZTirXgk9YGahN07JbAhacPkiWd0%2BdWxKcGguiLuLTL57%2BO0eBCLb9h6seTcYxULNf8wqPSpvi3SoBR1fHHSMV64aEfo0WfslYVGDGyQ2NC4O3zMM2QHnOhzM75g539%2BhYnRk8pzcvm71AISimLNVoFAwaHBzmVswgjidXqSpGJY31kJnqM7P0Q2DdH%2FHINXidVANcnpLW03LS78L46Yfkyf2QIRyUW1tgOdOpQDpM%2FpYrtesjDoHhr9XjIxPLlHHH1941pa9s6Dh0%2F0WbZD0OGvfpHxC01l5UoEKWKJr5MdsJHFYJ97qqP0lW0pAqxWsSrv3jrMCMJp0rJDYFjF9vVhPj7U2smV04Y3%2BSDDgqTS9MZw6DhV6OkSsbmP6%2BmhTAoBE07xDC475u9BjqkATfuctTPZgPNS%2BLC3aouLxH98ffdFtvaUerpqG1zxsr%2BQyRgn3siU3XaolCoC3JD7Yi7esJdlXmaq%2Biork1Gj4YnS2wZRwT8LqWRA9GYLspEK60x%2BsKrqUdpOUbvVcgrb%2FwsjNuOb0kQVXhJacOxREW8qcx%2FhYjVYvK0llmpyn4aSrwtZ6UmAjMggbChjPJ4Aqm9w5tgvbFm4m4yJJ03ecrUQvac&X-Amz-Signature=688b5ec261cb3cdf68582695811d354903b9ce9cd0b27b0f3d49748522e7543d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUAVE36G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCghfo6rvdl5FFeS3GAuLoCJvScUJbxf0SQN9i9gzRCJwIhAKoY%2BJD9mGQECYFZdBIqXs2abg8Wa5bpULDIKz88wiowKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXmLNPeILBGsXSKWMq3ANpfrtQKU%2F1QTovG77d64XulGLRt%2F%2FDxDLlYb%2F7j%2BbFXhn32DAi81xQPSfPnV8U%2BmWH9LMi%2FdtBHYjMMzBrIM3h1Au7gICCFIDof%2FrRPpCY6qyKIRWxuj%2FykhSW0C%2FrPAvZlq9fhf%2Fit3xuVtfSVti04dWHSzRqM3I4TdZ4%2FqN3CkQ1Yc%2Fc3W0b1p9ZSLuNl%2FM4C8eRPSLGzMmtL5rDuPh6%2Fa%2FKmlcL19T6XubxzBr3dX2r9cCdY9ZTirXgk9YGahN07JbAhacPkiWd0%2BdWxKcGguiLuLTL57%2BO0eBCLb9h6seTcYxULNf8wqPSpvi3SoBR1fHHSMV64aEfo0WfslYVGDGyQ2NC4O3zMM2QHnOhzM75g539%2BhYnRk8pzcvm71AISimLNVoFAwaHBzmVswgjidXqSpGJY31kJnqM7P0Q2DdH%2FHINXidVANcnpLW03LS78L46Yfkyf2QIRyUW1tgOdOpQDpM%2FpYrtesjDoHhr9XjIxPLlHHH1941pa9s6Dh0%2F0WbZD0OGvfpHxC01l5UoEKWKJr5MdsJHFYJ97qqP0lW0pAqxWsSrv3jrMCMJp0rJDYFjF9vVhPj7U2smV04Y3%2BSDDgqTS9MZw6DhV6OkSsbmP6%2BmhTAoBE07xDC475u9BjqkATfuctTPZgPNS%2BLC3aouLxH98ffdFtvaUerpqG1zxsr%2BQyRgn3siU3XaolCoC3JD7Yi7esJdlXmaq%2Biork1Gj4YnS2wZRwT8LqWRA9GYLspEK60x%2BsKrqUdpOUbvVcgrb%2FwsjNuOb0kQVXhJacOxREW8qcx%2FhYjVYvK0llmpyn4aSrwtZ6UmAjMggbChjPJ4Aqm9w5tgvbFm4m4yJJ03ecrUQvac&X-Amz-Signature=2a3e0e2af8a2a7366b135d01fb4b4c6c2e9de0e2b9e242e7d76018213f777164&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV22VLGA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIGhb2gM9MSLz9vqBOloAxV16E0c%2Bixh7JqcygxFbdLUxAiA35tKsg%2FTiHBC3TbUNuh9Os8h9jiAXN4xnzQuGRWwTmSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo1uT0QD%2B3CZKgADXKtwD2Xz39BOXxk87yK5SM72BFpA7yHSpbt32xubTPibyyvMW%2BIBGyvYSWbbK8Y36a1b50WJBU0k2QvDEsCvy9KZGpRKh8hAR%2FwF02DbLTByBwhffTwQg1AtZa9PgNPEw87ySxnSj3xFmpFaCI3huTrzN%2B2mOUlT1Hbok4b21Eq52VOBSZqkZ1mSh0HDpfQtsTNPRRjG4%2BexovRj3mSjxex9uBp6G%2F8Rr%2B2f%2B4692FBJHP0eEO9RME0MOP%2FmqsjkID345WxXECH4hBsvz6wz00w80UQ2d1hVMjSQ5RlRJSYiJDiEnQpv8gFkfM8iTda4jRBvB0fwHJFVjal08lPp8hwFUX2cCK%2F8wMNCEOsWYa4XGy5U%2FaULpYFWjnswCQ9CiIjjIxgAXsfAHXBLEW8fFCXEC0qOueJxgKS9jhnq%2B3RgO%2Fhe3OWGB2bIPKQBMLwd%2B4%2BTqubH2aiJtsSiprndAlevTve5U8%2FpYwNo6qhOYtYOoimo4c931LN5O3YBjrGSEYiAZZTrvIqjGnMiSOXB7dH3Q4LUGGqqICNQdzG9%2FnQhp%2FC5X%2FLTuzz0Ep4v58zJu4gYdZkcdzXiHsvmo%2BDTR7%2FRhiX3uEBqzwCBpcnskUTg6CMH9YjiRc2xrlP0mkecw7O6bvQY6pgHuD5HHRHmXiXK5RovoT2fItN%2BxpKKLbI3On5TvMpcm1OjbmzuFOksI5kXEV5Z2aTI8LA1NR9eAq2%2BESw03Dzodnx%2FsCjvgTLCj%2FO2JDTfp7el59cgXwLHwhV8EXfeEWs1wk%2BIIhaA0aDMhf78iHZgAf8h2qAyyQKdV%2FsxHV83lIPcChF2kfPR1D%2BvVhAfLHTKEqKCSd3JUd3wcCnvzJeBTL9BnicMn&X-Amz-Signature=ab3378a13ef9a07101134391718764996fb0cb55123a021223ada709d34c41fc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV22VLGA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIGhb2gM9MSLz9vqBOloAxV16E0c%2Bixh7JqcygxFbdLUxAiA35tKsg%2FTiHBC3TbUNuh9Os8h9jiAXN4xnzQuGRWwTmSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo1uT0QD%2B3CZKgADXKtwD2Xz39BOXxk87yK5SM72BFpA7yHSpbt32xubTPibyyvMW%2BIBGyvYSWbbK8Y36a1b50WJBU0k2QvDEsCvy9KZGpRKh8hAR%2FwF02DbLTByBwhffTwQg1AtZa9PgNPEw87ySxnSj3xFmpFaCI3huTrzN%2B2mOUlT1Hbok4b21Eq52VOBSZqkZ1mSh0HDpfQtsTNPRRjG4%2BexovRj3mSjxex9uBp6G%2F8Rr%2B2f%2B4692FBJHP0eEO9RME0MOP%2FmqsjkID345WxXECH4hBsvz6wz00w80UQ2d1hVMjSQ5RlRJSYiJDiEnQpv8gFkfM8iTda4jRBvB0fwHJFVjal08lPp8hwFUX2cCK%2F8wMNCEOsWYa4XGy5U%2FaULpYFWjnswCQ9CiIjjIxgAXsfAHXBLEW8fFCXEC0qOueJxgKS9jhnq%2B3RgO%2Fhe3OWGB2bIPKQBMLwd%2B4%2BTqubH2aiJtsSiprndAlevTve5U8%2FpYwNo6qhOYtYOoimo4c931LN5O3YBjrGSEYiAZZTrvIqjGnMiSOXB7dH3Q4LUGGqqICNQdzG9%2FnQhp%2FC5X%2FLTuzz0Ep4v58zJu4gYdZkcdzXiHsvmo%2BDTR7%2FRhiX3uEBqzwCBpcnskUTg6CMH9YjiRc2xrlP0mkecw7O6bvQY6pgHuD5HHRHmXiXK5RovoT2fItN%2BxpKKLbI3On5TvMpcm1OjbmzuFOksI5kXEV5Z2aTI8LA1NR9eAq2%2BESw03Dzodnx%2FsCjvgTLCj%2FO2JDTfp7el59cgXwLHwhV8EXfeEWs1wk%2BIIhaA0aDMhf78iHZgAf8h2qAyyQKdV%2FsxHV83lIPcChF2kfPR1D%2BvVhAfLHTKEqKCSd3JUd3wcCnvzJeBTL9BnicMn&X-Amz-Signature=03ef8dc75914c9bfb11bbc8af5f27cef2b13e7294e96507b3f93da90a07c5083&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV22VLGA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIGhb2gM9MSLz9vqBOloAxV16E0c%2Bixh7JqcygxFbdLUxAiA35tKsg%2FTiHBC3TbUNuh9Os8h9jiAXN4xnzQuGRWwTmSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo1uT0QD%2B3CZKgADXKtwD2Xz39BOXxk87yK5SM72BFpA7yHSpbt32xubTPibyyvMW%2BIBGyvYSWbbK8Y36a1b50WJBU0k2QvDEsCvy9KZGpRKh8hAR%2FwF02DbLTByBwhffTwQg1AtZa9PgNPEw87ySxnSj3xFmpFaCI3huTrzN%2B2mOUlT1Hbok4b21Eq52VOBSZqkZ1mSh0HDpfQtsTNPRRjG4%2BexovRj3mSjxex9uBp6G%2F8Rr%2B2f%2B4692FBJHP0eEO9RME0MOP%2FmqsjkID345WxXECH4hBsvz6wz00w80UQ2d1hVMjSQ5RlRJSYiJDiEnQpv8gFkfM8iTda4jRBvB0fwHJFVjal08lPp8hwFUX2cCK%2F8wMNCEOsWYa4XGy5U%2FaULpYFWjnswCQ9CiIjjIxgAXsfAHXBLEW8fFCXEC0qOueJxgKS9jhnq%2B3RgO%2Fhe3OWGB2bIPKQBMLwd%2B4%2BTqubH2aiJtsSiprndAlevTve5U8%2FpYwNo6qhOYtYOoimo4c931LN5O3YBjrGSEYiAZZTrvIqjGnMiSOXB7dH3Q4LUGGqqICNQdzG9%2FnQhp%2FC5X%2FLTuzz0Ep4v58zJu4gYdZkcdzXiHsvmo%2BDTR7%2FRhiX3uEBqzwCBpcnskUTg6CMH9YjiRc2xrlP0mkecw7O6bvQY6pgHuD5HHRHmXiXK5RovoT2fItN%2BxpKKLbI3On5TvMpcm1OjbmzuFOksI5kXEV5Z2aTI8LA1NR9eAq2%2BESw03Dzodnx%2FsCjvgTLCj%2FO2JDTfp7el59cgXwLHwhV8EXfeEWs1wk%2BIIhaA0aDMhf78iHZgAf8h2qAyyQKdV%2FsxHV83lIPcChF2kfPR1D%2BvVhAfLHTKEqKCSd3JUd3wcCnvzJeBTL9BnicMn&X-Amz-Signature=2bcf40a4faafb4e2c67576fcab27df561227eda1ec3549b21bc70b188b8946dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV22VLGA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIGhb2gM9MSLz9vqBOloAxV16E0c%2Bixh7JqcygxFbdLUxAiA35tKsg%2FTiHBC3TbUNuh9Os8h9jiAXN4xnzQuGRWwTmSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo1uT0QD%2B3CZKgADXKtwD2Xz39BOXxk87yK5SM72BFpA7yHSpbt32xubTPibyyvMW%2BIBGyvYSWbbK8Y36a1b50WJBU0k2QvDEsCvy9KZGpRKh8hAR%2FwF02DbLTByBwhffTwQg1AtZa9PgNPEw87ySxnSj3xFmpFaCI3huTrzN%2B2mOUlT1Hbok4b21Eq52VOBSZqkZ1mSh0HDpfQtsTNPRRjG4%2BexovRj3mSjxex9uBp6G%2F8Rr%2B2f%2B4692FBJHP0eEO9RME0MOP%2FmqsjkID345WxXECH4hBsvz6wz00w80UQ2d1hVMjSQ5RlRJSYiJDiEnQpv8gFkfM8iTda4jRBvB0fwHJFVjal08lPp8hwFUX2cCK%2F8wMNCEOsWYa4XGy5U%2FaULpYFWjnswCQ9CiIjjIxgAXsfAHXBLEW8fFCXEC0qOueJxgKS9jhnq%2B3RgO%2Fhe3OWGB2bIPKQBMLwd%2B4%2BTqubH2aiJtsSiprndAlevTve5U8%2FpYwNo6qhOYtYOoimo4c931LN5O3YBjrGSEYiAZZTrvIqjGnMiSOXB7dH3Q4LUGGqqICNQdzG9%2FnQhp%2FC5X%2FLTuzz0Ep4v58zJu4gYdZkcdzXiHsvmo%2BDTR7%2FRhiX3uEBqzwCBpcnskUTg6CMH9YjiRc2xrlP0mkecw7O6bvQY6pgHuD5HHRHmXiXK5RovoT2fItN%2BxpKKLbI3On5TvMpcm1OjbmzuFOksI5kXEV5Z2aTI8LA1NR9eAq2%2BESw03Dzodnx%2FsCjvgTLCj%2FO2JDTfp7el59cgXwLHwhV8EXfeEWs1wk%2BIIhaA0aDMhf78iHZgAf8h2qAyyQKdV%2FsxHV83lIPcChF2kfPR1D%2BvVhAfLHTKEqKCSd3JUd3wcCnvzJeBTL9BnicMn&X-Amz-Signature=b1a14b2cba896d86407264cc2f3a05eedddf585f9aad35d3d4aa10038cb57121&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV22VLGA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIGhb2gM9MSLz9vqBOloAxV16E0c%2Bixh7JqcygxFbdLUxAiA35tKsg%2FTiHBC3TbUNuh9Os8h9jiAXN4xnzQuGRWwTmSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo1uT0QD%2B3CZKgADXKtwD2Xz39BOXxk87yK5SM72BFpA7yHSpbt32xubTPibyyvMW%2BIBGyvYSWbbK8Y36a1b50WJBU0k2QvDEsCvy9KZGpRKh8hAR%2FwF02DbLTByBwhffTwQg1AtZa9PgNPEw87ySxnSj3xFmpFaCI3huTrzN%2B2mOUlT1Hbok4b21Eq52VOBSZqkZ1mSh0HDpfQtsTNPRRjG4%2BexovRj3mSjxex9uBp6G%2F8Rr%2B2f%2B4692FBJHP0eEO9RME0MOP%2FmqsjkID345WxXECH4hBsvz6wz00w80UQ2d1hVMjSQ5RlRJSYiJDiEnQpv8gFkfM8iTda4jRBvB0fwHJFVjal08lPp8hwFUX2cCK%2F8wMNCEOsWYa4XGy5U%2FaULpYFWjnswCQ9CiIjjIxgAXsfAHXBLEW8fFCXEC0qOueJxgKS9jhnq%2B3RgO%2Fhe3OWGB2bIPKQBMLwd%2B4%2BTqubH2aiJtsSiprndAlevTve5U8%2FpYwNo6qhOYtYOoimo4c931LN5O3YBjrGSEYiAZZTrvIqjGnMiSOXB7dH3Q4LUGGqqICNQdzG9%2FnQhp%2FC5X%2FLTuzz0Ep4v58zJu4gYdZkcdzXiHsvmo%2BDTR7%2FRhiX3uEBqzwCBpcnskUTg6CMH9YjiRc2xrlP0mkecw7O6bvQY6pgHuD5HHRHmXiXK5RovoT2fItN%2BxpKKLbI3On5TvMpcm1OjbmzuFOksI5kXEV5Z2aTI8LA1NR9eAq2%2BESw03Dzodnx%2FsCjvgTLCj%2FO2JDTfp7el59cgXwLHwhV8EXfeEWs1wk%2BIIhaA0aDMhf78iHZgAf8h2qAyyQKdV%2FsxHV83lIPcChF2kfPR1D%2BvVhAfLHTKEqKCSd3JUd3wcCnvzJeBTL9BnicMn&X-Amz-Signature=0f8d50544f5b2fb4ade9016257aec98751968af89208d42600d41b5e7e447e0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV22VLGA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIGhb2gM9MSLz9vqBOloAxV16E0c%2Bixh7JqcygxFbdLUxAiA35tKsg%2FTiHBC3TbUNuh9Os8h9jiAXN4xnzQuGRWwTmSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo1uT0QD%2B3CZKgADXKtwD2Xz39BOXxk87yK5SM72BFpA7yHSpbt32xubTPibyyvMW%2BIBGyvYSWbbK8Y36a1b50WJBU0k2QvDEsCvy9KZGpRKh8hAR%2FwF02DbLTByBwhffTwQg1AtZa9PgNPEw87ySxnSj3xFmpFaCI3huTrzN%2B2mOUlT1Hbok4b21Eq52VOBSZqkZ1mSh0HDpfQtsTNPRRjG4%2BexovRj3mSjxex9uBp6G%2F8Rr%2B2f%2B4692FBJHP0eEO9RME0MOP%2FmqsjkID345WxXECH4hBsvz6wz00w80UQ2d1hVMjSQ5RlRJSYiJDiEnQpv8gFkfM8iTda4jRBvB0fwHJFVjal08lPp8hwFUX2cCK%2F8wMNCEOsWYa4XGy5U%2FaULpYFWjnswCQ9CiIjjIxgAXsfAHXBLEW8fFCXEC0qOueJxgKS9jhnq%2B3RgO%2Fhe3OWGB2bIPKQBMLwd%2B4%2BTqubH2aiJtsSiprndAlevTve5U8%2FpYwNo6qhOYtYOoimo4c931LN5O3YBjrGSEYiAZZTrvIqjGnMiSOXB7dH3Q4LUGGqqICNQdzG9%2FnQhp%2FC5X%2FLTuzz0Ep4v58zJu4gYdZkcdzXiHsvmo%2BDTR7%2FRhiX3uEBqzwCBpcnskUTg6CMH9YjiRc2xrlP0mkecw7O6bvQY6pgHuD5HHRHmXiXK5RovoT2fItN%2BxpKKLbI3On5TvMpcm1OjbmzuFOksI5kXEV5Z2aTI8LA1NR9eAq2%2BESw03Dzodnx%2FsCjvgTLCj%2FO2JDTfp7el59cgXwLHwhV8EXfeEWs1wk%2BIIhaA0aDMhf78iHZgAf8h2qAyyQKdV%2FsxHV83lIPcChF2kfPR1D%2BvVhAfLHTKEqKCSd3JUd3wcCnvzJeBTL9BnicMn&X-Amz-Signature=de6088886aab7d6f1e0e311eb13c4581f402f9e0a43302015f3b9beda20873f0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGY65VQW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIAO6XeAvAx0us2cnNpofD%2B0cDzJ1TYlVn9QoHFK%2BDdwTAiBN1Aq3I%2BjlAazPmFlamkzEZVCYd8lr7wGm2R9wdGuzHyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPiKqrUH02HffYTjyKtwDB9vGyYzL7uIv1Ma3Lg0OW3U7T3ByFMvjYFgnwDWVJ3EFVwF9MbKg28Fa663Yw3d%2BLNTLH8rQJaFLPIQN7lTZrL0WK45GSI9NWj9XCPiMWH6vOkKI%2BfZkXZA0JXkNHQwK%2FfXd80pA2GvAjI1VXQSyLltNLOklRjt4rYgJwif6JiJdJ%2BD9XChXczPCFvxqOJLyVjUiVxIT7fcDAyTTEYGWcYdPy9oKKETZ%2Flt%2FPzz2XwIrJS3e1u7ugzhHF5gSz7FmjfJaerpNTUrKD%2BSO561KEMUQl2EctG8UBfcaOD9%2BPs004EqiLWUf6sXxpLPdkiKnrzoSpJtnXsNUj4ngzgQCkUPxEj9ajkTDjTbQ6dWq1rpNjSdoZIV7j%2Fd8YQo15wMigfbArCKq9cvaizKBcAQP%2FtCdQ7wTYpgQUn4XVwFrOKBhhT%2BrYIEvPTRym4iOexAnrqu7b5jmHAINz9CUiS4XMp%2F47MnHPD9JtR7ozHiJdY1yF1IXKt0Rr4mE6D8eIRyTqLoWjRI%2FX0ZqMtWE48UCyKDwRkStTy0ss7%2FQEBKfaq2%2FUYpE1yMva7mXZZYOFV2jbI9e8GoUKExbd%2FilQW7iFEcQsIJbZV6Ft4%2BEssDIFXCtZ5eeywGKRJ%2FstFwwqe%2BbvQY6pgGuS1scq%2Bt2fvs6fPnoW%2BNGZ2uxYO99UgI4EdpiJxp3qRuTDjMH3Q1SQ7kx28JIT%2FM0UbPx1W2NVYbqxlgpag6pViCi9HFGHpZuDA%2BiIu6cOMvFlspU00K%2Bt0yKSTDaBbgoosv36pZEUMkMWVyRstlPH9a6GRygEJJOZQJTcliNOyLHbH6Z0ZXSLHm%2Fj3eKcj9MxeoTkGRYrTz3sdKkQ3SrgQugPbQH&X-Amz-Signature=d77d546de4688d362a8a9bfd058d03246d793124e9b1e1c3f2b818681a1ff218&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDDOWEMQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQC9Q%2BJpc0tiDjaBJ4cFKT7dBM9KFXWxW1wsoDxovSJD0AIhAKwdIn9WxOzJ6r1H21F9opKXGiuZx5UFbk6o0nBKj4p6KogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxnpc85b34l98OkLEMq3AMGaAyaktvQGULR%2FAOZ2Qg9GZD6YbRg8b5%2F5j8Syb%2FjAbuwVX68CiXewtiB6MmquB0%2FczXFqYOQ3BZn%2FficWxTLNY8kEakKoMkH0MqYmAFz2dVWYQHz%2By2Y9WZ7gTdxwgPqdqabYgq6uqEChlpld8vr7U8AR1B%2BEo4CS5ftH%2FHeqFv71Td7h7Da%2FCGTKldYxSKrTzFh1msxYGlzmaS1Eveqr0%2FMrBnlTLUOTU7FPKW%2Bqw05UP7mAj52zS2GGRWB%2Fs5RSZ4%2F2BAx3kHfjaBHuV%2BEJ2BOSwMLCrGBm1YGHjejF4Ra%2BG9eaD0E9P2jSzBBl1mNttEliCh8MTXh%2FZCwyPFJ5oqApLrdghZ7ugFP%2FwbXhz1ACga3oHJcEfPHAp5A5MFrJFqymYu%2BlFwFjeLovtRYkCn2CtcKV%2FXnDLaK0I2vwVFlgpSxQQJySuRhQ0qieMp37pBoPkPb0LyR5%2F0vFoyPQO5KLzzyg49da4c9vBBDpQhX%2Bm5Duwo%2B5nCl2bBALOCLp2knbHd2T9k4XPyaUmSKoB4ec5KIzyM8eLUeU6jiM4rB0cl%2FwTa49jFxPqlx4rChgz%2FyJwTx8d5l7%2B2RVFx9tLHppinhcwTNDfMbFLX6V11ND%2Fs6kQlqG4Lr%2BDDI75u9BjqkATsoFuHjUZePa1Dhn36isy3frFb1ttx4r%2F3AIpwV7cb3S5bHpEA9ToVI%2BV6qEXG%2BdZY5jDQvGKF70Gig8VILWvOXtmihwdVfT9i5ctPqc1bCjjMt%2FB%2BWxSA9JKLd5p3%2FYXXAjUgAf8VdPFYNEkV4N%2B%2BdScXNwI2oAFgOg87d7MzT3022NNb6qPOfYUBcvPQJCuv00iBlWGnYS2U%2BjDeq1rGo52Yx&X-Amz-Signature=cbeefc45d4b37b4537fc6528a45fd121560551be69a2d3d406c81c7aae88019d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV22VLGA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIGhb2gM9MSLz9vqBOloAxV16E0c%2Bixh7JqcygxFbdLUxAiA35tKsg%2FTiHBC3TbUNuh9Os8h9jiAXN4xnzQuGRWwTmSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo1uT0QD%2B3CZKgADXKtwD2Xz39BOXxk87yK5SM72BFpA7yHSpbt32xubTPibyyvMW%2BIBGyvYSWbbK8Y36a1b50WJBU0k2QvDEsCvy9KZGpRKh8hAR%2FwF02DbLTByBwhffTwQg1AtZa9PgNPEw87ySxnSj3xFmpFaCI3huTrzN%2B2mOUlT1Hbok4b21Eq52VOBSZqkZ1mSh0HDpfQtsTNPRRjG4%2BexovRj3mSjxex9uBp6G%2F8Rr%2B2f%2B4692FBJHP0eEO9RME0MOP%2FmqsjkID345WxXECH4hBsvz6wz00w80UQ2d1hVMjSQ5RlRJSYiJDiEnQpv8gFkfM8iTda4jRBvB0fwHJFVjal08lPp8hwFUX2cCK%2F8wMNCEOsWYa4XGy5U%2FaULpYFWjnswCQ9CiIjjIxgAXsfAHXBLEW8fFCXEC0qOueJxgKS9jhnq%2B3RgO%2Fhe3OWGB2bIPKQBMLwd%2B4%2BTqubH2aiJtsSiprndAlevTve5U8%2FpYwNo6qhOYtYOoimo4c931LN5O3YBjrGSEYiAZZTrvIqjGnMiSOXB7dH3Q4LUGGqqICNQdzG9%2FnQhp%2FC5X%2FLTuzz0Ep4v58zJu4gYdZkcdzXiHsvmo%2BDTR7%2FRhiX3uEBqzwCBpcnskUTg6CMH9YjiRc2xrlP0mkecw7O6bvQY6pgHuD5HHRHmXiXK5RovoT2fItN%2BxpKKLbI3On5TvMpcm1OjbmzuFOksI5kXEV5Z2aTI8LA1NR9eAq2%2BESw03Dzodnx%2FsCjvgTLCj%2FO2JDTfp7el59cgXwLHwhV8EXfeEWs1wk%2BIIhaA0aDMhf78iHZgAf8h2qAyyQKdV%2FsxHV83lIPcChF2kfPR1D%2BvVhAfLHTKEqKCSd3JUd3wcCnvzJeBTL9BnicMn&X-Amz-Signature=1a212177dbe0b477148846303867a61ce4c6421bf3ad52e204b9628d2302f861&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV22VLGA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIGhb2gM9MSLz9vqBOloAxV16E0c%2Bixh7JqcygxFbdLUxAiA35tKsg%2FTiHBC3TbUNuh9Os8h9jiAXN4xnzQuGRWwTmSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo1uT0QD%2B3CZKgADXKtwD2Xz39BOXxk87yK5SM72BFpA7yHSpbt32xubTPibyyvMW%2BIBGyvYSWbbK8Y36a1b50WJBU0k2QvDEsCvy9KZGpRKh8hAR%2FwF02DbLTByBwhffTwQg1AtZa9PgNPEw87ySxnSj3xFmpFaCI3huTrzN%2B2mOUlT1Hbok4b21Eq52VOBSZqkZ1mSh0HDpfQtsTNPRRjG4%2BexovRj3mSjxex9uBp6G%2F8Rr%2B2f%2B4692FBJHP0eEO9RME0MOP%2FmqsjkID345WxXECH4hBsvz6wz00w80UQ2d1hVMjSQ5RlRJSYiJDiEnQpv8gFkfM8iTda4jRBvB0fwHJFVjal08lPp8hwFUX2cCK%2F8wMNCEOsWYa4XGy5U%2FaULpYFWjnswCQ9CiIjjIxgAXsfAHXBLEW8fFCXEC0qOueJxgKS9jhnq%2B3RgO%2Fhe3OWGB2bIPKQBMLwd%2B4%2BTqubH2aiJtsSiprndAlevTve5U8%2FpYwNo6qhOYtYOoimo4c931LN5O3YBjrGSEYiAZZTrvIqjGnMiSOXB7dH3Q4LUGGqqICNQdzG9%2FnQhp%2FC5X%2FLTuzz0Ep4v58zJu4gYdZkcdzXiHsvmo%2BDTR7%2FRhiX3uEBqzwCBpcnskUTg6CMH9YjiRc2xrlP0mkecw7O6bvQY6pgHuD5HHRHmXiXK5RovoT2fItN%2BxpKKLbI3On5TvMpcm1OjbmzuFOksI5kXEV5Z2aTI8LA1NR9eAq2%2BESw03Dzodnx%2FsCjvgTLCj%2FO2JDTfp7el59cgXwLHwhV8EXfeEWs1wk%2BIIhaA0aDMhf78iHZgAf8h2qAyyQKdV%2FsxHV83lIPcChF2kfPR1D%2BvVhAfLHTKEqKCSd3JUd3wcCnvzJeBTL9BnicMn&X-Amz-Signature=34db90ac6bc6949cf62ddef82012d64614f16f0561cf409a70a4b6bc04e378d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV22VLGA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIGhb2gM9MSLz9vqBOloAxV16E0c%2Bixh7JqcygxFbdLUxAiA35tKsg%2FTiHBC3TbUNuh9Os8h9jiAXN4xnzQuGRWwTmSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo1uT0QD%2B3CZKgADXKtwD2Xz39BOXxk87yK5SM72BFpA7yHSpbt32xubTPibyyvMW%2BIBGyvYSWbbK8Y36a1b50WJBU0k2QvDEsCvy9KZGpRKh8hAR%2FwF02DbLTByBwhffTwQg1AtZa9PgNPEw87ySxnSj3xFmpFaCI3huTrzN%2B2mOUlT1Hbok4b21Eq52VOBSZqkZ1mSh0HDpfQtsTNPRRjG4%2BexovRj3mSjxex9uBp6G%2F8Rr%2B2f%2B4692FBJHP0eEO9RME0MOP%2FmqsjkID345WxXECH4hBsvz6wz00w80UQ2d1hVMjSQ5RlRJSYiJDiEnQpv8gFkfM8iTda4jRBvB0fwHJFVjal08lPp8hwFUX2cCK%2F8wMNCEOsWYa4XGy5U%2FaULpYFWjnswCQ9CiIjjIxgAXsfAHXBLEW8fFCXEC0qOueJxgKS9jhnq%2B3RgO%2Fhe3OWGB2bIPKQBMLwd%2B4%2BTqubH2aiJtsSiprndAlevTve5U8%2FpYwNo6qhOYtYOoimo4c931LN5O3YBjrGSEYiAZZTrvIqjGnMiSOXB7dH3Q4LUGGqqICNQdzG9%2FnQhp%2FC5X%2FLTuzz0Ep4v58zJu4gYdZkcdzXiHsvmo%2BDTR7%2FRhiX3uEBqzwCBpcnskUTg6CMH9YjiRc2xrlP0mkecw7O6bvQY6pgHuD5HHRHmXiXK5RovoT2fItN%2BxpKKLbI3On5TvMpcm1OjbmzuFOksI5kXEV5Z2aTI8LA1NR9eAq2%2BESw03Dzodnx%2FsCjvgTLCj%2FO2JDTfp7el59cgXwLHwhV8EXfeEWs1wk%2BIIhaA0aDMhf78iHZgAf8h2qAyyQKdV%2FsxHV83lIPcChF2kfPR1D%2BvVhAfLHTKEqKCSd3JUd3wcCnvzJeBTL9BnicMn&X-Amz-Signature=56f3ea3de4d82fa85f4b9ac06fe0f1028d9098aee0ee9e56cb9d015220ba821f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AE2RKBN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCICQ%2FUko7nLd6drjSOOCBIA2IUtiFisiuajpLrvbNCN58AiBuz3LKnwrXxMV7MtafZYcdb1mK33rxOJXb3GNMysM5fCqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmEWdCT%2Fxn7qM8QqlKtwDfQvcMqV9BuZErvV2jSQRAZOhGuc4vXEtkPo1BTHr2giJVAFu6llnLIgmS35Ui1q8%2BGUhDmpETwjXWxr5NPeh6ec3xOtjzEZZ3MFECvLHZnm99ijRDdlfxCuN%2BDgPK7bXNG%2Fok8%2FJyfZloHesPGPgtRSZ4nVJiSbR%2F27rgX66X6PeM533UH28VPooigiFAX3rQFDxIAMiwEhVB4ZV8%2FarQ0JL4f9fiFUXY%2F%2BgEjlXPOk5yciI3UVZxen%2BLa%2BOZ1cUwKTXaQj6OaKHeZDugj%2FhU784taZCd6Hx5YkssgMBuJA4vk0Q97VvTxBiZnwKgPsHBASr32Xb0P8uxImrXR%2BQZAFzKng7ZsDw4%2BjYYLbIUmSWRNcvgBtornW9eaiCpvK77AsHQqBvrPSAd%2BkUruMLEtC5PngMaIXjM2BmMZuRuCs2nyU3sLhOf31wtvN9l5epHIag10kBeW21diBZQjy%2FtVHWsLfTuMcce47zQg0xAdja0pcekHe58KYZxy4bG8D%2Fb5vFLKCsJ9md8hKQirXKpCVVcowC%2FIMf50jeujFsGP3xnmC0WUUHe9JlVCvBpcOj7suO1KzSJeS0zwaZOTiVkffNgDzwBj4x7SZF%2Bt3uxAHXhjm%2FAScHuJNGAk4wzu%2BbvQY6pgFEkolbZ2TAH6ElM7BR2T0dzNLQrrHxsSsdpUHSZM84zk3Kj0QlgsGNi%2BnpzA4g615pObkPD%2BoPGm8Bog5dbABUxtdXCluHK7UgvBQZExdW6Wc42afE4HWEQObQL%2Fod%2FwJxW0lGBNqQ3Yacvedgc8TYePOxWfUFfWvbAXFEfluee8SJRB1I5wwmIEdAqLxA0D%2Bl2nUP%2F3k%2FP4hFfz22IMnhK1k%2BVmaW&X-Amz-Signature=3944189ef75de88e2c2df0392727b943c30a02c5bc1e1f892c399315acee2b54&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JXOMZ4G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIG2C09rTX2AjNF3d4%2Bogiyr%2FmX%2FKzuJjTDfyVZ%2BU7CB3AiBAGrALhI2m%2BFtZCZ%2Bjl5tTj9A6XxJOOTYXUzX2BCcqISqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaeUeLLX5KgF8wvG7KtwDl8IJ0C9sZrJF1RoStQ%2Blq%2BXBXnVbi75LBZQt3BrDPCtgBikQNsVmFsYZVaHefYYB0lp2iFkbhbR0EcX18s1Y74j8JDXWE4uPU1y9%2FHrsY7ZLHUb0R1LdRjEDaxgKCAbdZ5UUoljg9fOOQKREuoG3hA7xdniyyBno3DWK7ibJAznbI%2FFeSqVLt1ozwh4KJ5SzDjd5lfUnZTiE7iN7ngzwW2bBk62dKStkZK2p0OQWLNL4DKPhNc5sn0hbRudzySX8%2BlYEEZJboI4BwHNUG7ujW2K1GnKR4JU1hWIjwa9vFAcWBC3Ko8zFR5mfGyGh5KAIBxJcvDW7lEoqh%2F4xpyWF64q6VOdcFhaXqtQAwlYzeIElob9QEa8gwaKUfbWHP%2BYmwgzNyFA7TCljgb1E6w80wmFKl56eR%2FCEwn3eMBnKOB%2FPK1YUuEcgEQpri62uaYRLujlQoRd26eEJSBO7%2BLA7m0UkEpO4X%2FGgUBmKNOsRWrjfp9yvnmifFbVVWeegNb%2BRl6I7RaOy38AVCtMEnVdjXwIZCs%2FOESD%2BTWh8sfENlLNBvGaZoZeuPxtRCugBUyY4sApEyHixiojNWiTGdMh6FcN4NenaN5jGIU%2FONUwWf7k8zNCTIssID1B59LIw%2Be6bvQY6pgErS5x2prvjHZSPvId8BIQC%2Bv6hurxJOqANciFpmoyrFx9o43Mkuogu4mDFF8LIP6lIFK%2BEH%2Fbb82F1NGMu8qx1nefl%2B%2BHFql2qArf4yfTIJmkqy6tv7E8ED7AzJajk9xHcyfVTKrx0FbeRNPUD6UBpTd%2FNDDSemaAjHo4ewVy7SuFDR5vZL4xv5bS4SgOWJjaTGledbgrL%2Bwyd9AI3DsgAP95s9bO3&X-Amz-Signature=5919d513f62143d725f1bd6639199d27df8bc6c51212e5a2f81ef10f6fda40e8&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q27CAUR6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQC1QcuAcPb6sS9hRIeNE8%2BGoHHP5gTn39Ys%2B9Jf7hgUcwIgSmAmp%2FsKCtwMg8WvFl4jyExuWUGaVqVzsKczqraxu%2FkqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCN8y0A1uxNUP%2FILwSrcA7sRHEEH8Y8fIMmqOGLIzxVg8CBBStdN26AtjpsL9HCU%2FXHcXaByqRDJGlrV1TMfmYfzLHM73hIg12E03fj%2FHblClnYpaZiSvXyI0oP501AdBUz0pOa5SvLrJ%2BCXEr4Ps6Byd1MDmcsgJ7yB62tM9I163uVhFX1ocLXV2%2BwY8vZd3cmX0vzNpl7duPI1sQLpqDvkmF9ZR26WSP38fgTkX1vybnLVmANDhNz82fDuB%2Fi%2FLrpHI4Thth4VLZftX6Y%2Brb9L%2FconuRre0k2Qpdf%2F0oQTHCGv3xj9fu4iaxUtDND%2B4zzG2oXf%2FxnQUcyD5AOmC2TUn%2FgY1KT6fE4V1OVWc0V0kIbRdE3iaR%2FBIr5FghtaUL27f131lVWJAd6%2B61xaHSYLgcb8ABLnSHMytH8nWhO7R8mIPA%2B%2B9O5od3UG6PgY96bhfXiecqLPXcxPPDRU%2Fi1qhOqHoRIpXlqrH%2Fs8Vwk2QJlLcclXZqcAKG7j3hZ0yVi5q8%2BB6ByQPGvlV3fWJ%2FbpP6s2KIw8llmH0pstoUJpAsvRXD%2BQvIwtItjPEFBUYWVQvDdu6CZ0RgAWbx71UzDRtuQQRsQNLFHQMm6TXg0uW1NIvwRSoAL9xv3AeNkoZDLGGPDBsH345%2FmGMMbvm70GOqUBr1Y3tysZZbXcSbZez8RH4DJTKoVyM28tqmhOYXdKg5jx8AFCSfW0LWNzG8%2BqiQdLgBnxQVHTItjkeQHtET%2BFub4eKm%2BYmh1zK0e5uHNtVvvQym2ENaFBk%2FQrZ7S0PcRjWgkUAOYJSb5l7vcBd60DDjWNncuzgQmEFifAsvqaXyIIFegxMBBz%2B%2FDR5Q3x%2FukciDwA8salnll0vssiREXNniYCct%2Bn&X-Amz-Signature=29114511737cfc4a7ee6f1ff7c40a18b7fbcdedbfa42b4ecec0414b9a3b2054b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ESY3S3F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIFfVSruL7aqHm7gUKkspXllPBTAtDLYvPNJxQcGUHtYxAiBCiNBfCzH6Mg5L%2FJbYI8vwvH14KrbiQDhaiWwzFbQBgCqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVNTLYlLzKjfOstcUKtwDXE5AnTQMSeHYVBbpAY%2FQvscf0fHtPELF0uOTePe9hM8t8Npooaz3o9g1uUQeVts9T1Xyn3E9Ay64dNtrLJnddg1RFvsXfxTs12N7MAfJtKLnrJHWbtqEuAHNBWZcaos48MLT7IjKsGSxmCKaETdnx1fp3fHEBydIHXZpthz6IcpiNsQ21nrGJ8RdIubjjlSZaAKdx8sTXsDMtnHMw%2FIiMuzASggheidf6N06%2FTZcoqGfQn4pcZ%2F0VNMfyQ8ukfAE88t3EuXHfJVkDuWm666CMWxGFOxKBSjCfkPuCfPu2RFSV6R7qCeXFYRKJ34rkPR%2BfrKmXLnyajrbYwF20hkPQyHhwHMQoGZXfSh4Dl%2Be%2F3wwZnxM3PRAV7T%2BsFAHzMsl03o9r1hlUGotDSAjDV8IjcksGyXTDljjfUhgpuZB3upGAgL2YGOf3SsyRzE8Wqt24xL%2FtX1WAdkaZwyfBJIulYsI9HU4jTsDP4RjehmRqPBc0UAxmcaQQYKzLNifLj%2BC7gRA5VW9vtWBTtIoQVpvd7469eZzm2wURJU%2BR4nnZ3U2HkZvTaZ63s%2Bi6Ql2Y92g36iDosJtqgkkazPJGPcMXxNxoS9N72z7dZj6JM3g9fcrZ4GACRcUYJFx1Usw6O%2BbvQY6pgEVYx0W1yjb98hfr4MMIbpzyQ3a9Y0r2%2FEyqk7f3qpVOtIO5HlQ7P3s4AK0P4RsHSiYERzpy2CBuDeSS9NHnxOJSK0Ktt4tHsH7%2BM0%2B7pHZLEnEcbt69dy83hcaGnw%2B0%2FpTIZefEfn5PrPx13gX3OBJccs8v3b38rixlCq4IkMV3EUnnrQoCpYP36tfQGJsOAb1K%2FhUvzPx%2FdPXYhYKEzAzuI7k2XkT&X-Amz-Signature=288b6cca4404b262cb798d729bdc99efc25a32a2701f2d0716a2f1057068aa9b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ESY3S3F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIFfVSruL7aqHm7gUKkspXllPBTAtDLYvPNJxQcGUHtYxAiBCiNBfCzH6Mg5L%2FJbYI8vwvH14KrbiQDhaiWwzFbQBgCqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVNTLYlLzKjfOstcUKtwDXE5AnTQMSeHYVBbpAY%2FQvscf0fHtPELF0uOTePe9hM8t8Npooaz3o9g1uUQeVts9T1Xyn3E9Ay64dNtrLJnddg1RFvsXfxTs12N7MAfJtKLnrJHWbtqEuAHNBWZcaos48MLT7IjKsGSxmCKaETdnx1fp3fHEBydIHXZpthz6IcpiNsQ21nrGJ8RdIubjjlSZaAKdx8sTXsDMtnHMw%2FIiMuzASggheidf6N06%2FTZcoqGfQn4pcZ%2F0VNMfyQ8ukfAE88t3EuXHfJVkDuWm666CMWxGFOxKBSjCfkPuCfPu2RFSV6R7qCeXFYRKJ34rkPR%2BfrKmXLnyajrbYwF20hkPQyHhwHMQoGZXfSh4Dl%2Be%2F3wwZnxM3PRAV7T%2BsFAHzMsl03o9r1hlUGotDSAjDV8IjcksGyXTDljjfUhgpuZB3upGAgL2YGOf3SsyRzE8Wqt24xL%2FtX1WAdkaZwyfBJIulYsI9HU4jTsDP4RjehmRqPBc0UAxmcaQQYKzLNifLj%2BC7gRA5VW9vtWBTtIoQVpvd7469eZzm2wURJU%2BR4nnZ3U2HkZvTaZ63s%2Bi6Ql2Y92g36iDosJtqgkkazPJGPcMXxNxoS9N72z7dZj6JM3g9fcrZ4GACRcUYJFx1Usw6O%2BbvQY6pgEVYx0W1yjb98hfr4MMIbpzyQ3a9Y0r2%2FEyqk7f3qpVOtIO5HlQ7P3s4AK0P4RsHSiYERzpy2CBuDeSS9NHnxOJSK0Ktt4tHsH7%2BM0%2B7pHZLEnEcbt69dy83hcaGnw%2B0%2FpTIZefEfn5PrPx13gX3OBJccs8v3b38rixlCq4IkMV3EUnnrQoCpYP36tfQGJsOAb1K%2FhUvzPx%2FdPXYhYKEzAzuI7k2XkT&X-Amz-Signature=fb532362d0a5c275dabdd94e65dab854297d77d0817dd2e888767358a1d2f029&X-Amz-SignedHeaders=host&x-id=GetObject)

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
