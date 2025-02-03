

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU3U66JW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDroJBpcAAIKrDTi6LH4mZHGQ3oFm0Zs7t4EG2HWvSFSAIhAMMqkE36ecH3KPNFKZjYN8k1d5iiKu73kyLaNYS0KdzoKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmzAvYGQ7gh5C4DC4q3AMTfIrHbJDa1nklT76t01blO82savMnHQY1TX4TeMDHqRZFEE2VtX3VbngN5W9JfRjfxNQmwDrEbZLPTIU6fsR8MTUngpy59rTpgWBmEFEe9xpu7g2k3dx0VbJnHevfw%2F4uVyFNDGR8MxiiJLoKGvE3eEzEE0yWveBsG987Deehpz2UbqFov1GqaU%2BRk5EcO03xhzPC267piBY506j5VQHjHYILYDTBo0f01dbQbTJaj9Ebdri6ADCO5WNPSiRWj0bSJl293gYsX6oGR1O8gwGiPawifo1HuMFBy2F052SLzFJ6KC41wxBEc3dR8UXJaqe0OzTj0B27IusGtKfGWL2wu%2FGkpCT3NWyTp%2BNaGUU0iDQ031bbxymfSKcaZyX%2FzfxsQbAC0WSYqKJarq6G2fUk0kxcYfse%2B4o%2BWtYIqChycwtfZ%2FxCzdoffTUPRLHmPPPZZ66AqdKjSwH4ctBlsWhV0maW%2FGHnea2UlHsOKDLL5BuYQIWSQQcF34EJrFlhGnmMXJFHvmsuyMerCoidmM0KV7GLH6q0Cr2m4NSRWQMBhwYMDTr6PhogMNJ11v3ZXQRndD2D5QN4H3JKcAMir9MG%2B8WOtmdaRLgVwKRdNvI8rJDYvzi%2BHptb9K9lfTCbwIC9BjqkASIptw%2FqPFWPrVmGAtikcmAg3aobYiVNAaxIEXmcVHABfr4YfL3FCN3gci%2BXSoxJHUxPnD0RI%2BI66W1AvJ92ZkOljFnyy4Shw%2FGdhaWuh1bdPDMhCdurGtPXWosRiP%2FsAvagz%2FomyysoVGXMak1shmOYER8dPOGyTUL7PujZjbjSDjbealx%2FdA%2BRb4163XoaqiG8iGwLB3GWgz9Stfy%2FB1%2BS21sV&X-Amz-Signature=b9932146d965d81d24bb94c5855bf3053094c30ee69cd745168be4a417e93ae6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU3U66JW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDroJBpcAAIKrDTi6LH4mZHGQ3oFm0Zs7t4EG2HWvSFSAIhAMMqkE36ecH3KPNFKZjYN8k1d5iiKu73kyLaNYS0KdzoKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmzAvYGQ7gh5C4DC4q3AMTfIrHbJDa1nklT76t01blO82savMnHQY1TX4TeMDHqRZFEE2VtX3VbngN5W9JfRjfxNQmwDrEbZLPTIU6fsR8MTUngpy59rTpgWBmEFEe9xpu7g2k3dx0VbJnHevfw%2F4uVyFNDGR8MxiiJLoKGvE3eEzEE0yWveBsG987Deehpz2UbqFov1GqaU%2BRk5EcO03xhzPC267piBY506j5VQHjHYILYDTBo0f01dbQbTJaj9Ebdri6ADCO5WNPSiRWj0bSJl293gYsX6oGR1O8gwGiPawifo1HuMFBy2F052SLzFJ6KC41wxBEc3dR8UXJaqe0OzTj0B27IusGtKfGWL2wu%2FGkpCT3NWyTp%2BNaGUU0iDQ031bbxymfSKcaZyX%2FzfxsQbAC0WSYqKJarq6G2fUk0kxcYfse%2B4o%2BWtYIqChycwtfZ%2FxCzdoffTUPRLHmPPPZZ66AqdKjSwH4ctBlsWhV0maW%2FGHnea2UlHsOKDLL5BuYQIWSQQcF34EJrFlhGnmMXJFHvmsuyMerCoidmM0KV7GLH6q0Cr2m4NSRWQMBhwYMDTr6PhogMNJ11v3ZXQRndD2D5QN4H3JKcAMir9MG%2B8WOtmdaRLgVwKRdNvI8rJDYvzi%2BHptb9K9lfTCbwIC9BjqkASIptw%2FqPFWPrVmGAtikcmAg3aobYiVNAaxIEXmcVHABfr4YfL3FCN3gci%2BXSoxJHUxPnD0RI%2BI66W1AvJ92ZkOljFnyy4Shw%2FGdhaWuh1bdPDMhCdurGtPXWosRiP%2FsAvagz%2FomyysoVGXMak1shmOYER8dPOGyTUL7PujZjbjSDjbealx%2FdA%2BRb4163XoaqiG8iGwLB3GWgz9Stfy%2FB1%2BS21sV&X-Amz-Signature=16a3a6b5b8d7981f2835a7d8c0430fbe108cd4f0420c0cae22fd4ff273d1a4b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU3U66JW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDroJBpcAAIKrDTi6LH4mZHGQ3oFm0Zs7t4EG2HWvSFSAIhAMMqkE36ecH3KPNFKZjYN8k1d5iiKu73kyLaNYS0KdzoKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmzAvYGQ7gh5C4DC4q3AMTfIrHbJDa1nklT76t01blO82savMnHQY1TX4TeMDHqRZFEE2VtX3VbngN5W9JfRjfxNQmwDrEbZLPTIU6fsR8MTUngpy59rTpgWBmEFEe9xpu7g2k3dx0VbJnHevfw%2F4uVyFNDGR8MxiiJLoKGvE3eEzEE0yWveBsG987Deehpz2UbqFov1GqaU%2BRk5EcO03xhzPC267piBY506j5VQHjHYILYDTBo0f01dbQbTJaj9Ebdri6ADCO5WNPSiRWj0bSJl293gYsX6oGR1O8gwGiPawifo1HuMFBy2F052SLzFJ6KC41wxBEc3dR8UXJaqe0OzTj0B27IusGtKfGWL2wu%2FGkpCT3NWyTp%2BNaGUU0iDQ031bbxymfSKcaZyX%2FzfxsQbAC0WSYqKJarq6G2fUk0kxcYfse%2B4o%2BWtYIqChycwtfZ%2FxCzdoffTUPRLHmPPPZZ66AqdKjSwH4ctBlsWhV0maW%2FGHnea2UlHsOKDLL5BuYQIWSQQcF34EJrFlhGnmMXJFHvmsuyMerCoidmM0KV7GLH6q0Cr2m4NSRWQMBhwYMDTr6PhogMNJ11v3ZXQRndD2D5QN4H3JKcAMir9MG%2B8WOtmdaRLgVwKRdNvI8rJDYvzi%2BHptb9K9lfTCbwIC9BjqkASIptw%2FqPFWPrVmGAtikcmAg3aobYiVNAaxIEXmcVHABfr4YfL3FCN3gci%2BXSoxJHUxPnD0RI%2BI66W1AvJ92ZkOljFnyy4Shw%2FGdhaWuh1bdPDMhCdurGtPXWosRiP%2FsAvagz%2FomyysoVGXMak1shmOYER8dPOGyTUL7PujZjbjSDjbealx%2FdA%2BRb4163XoaqiG8iGwLB3GWgz9Stfy%2FB1%2BS21sV&X-Amz-Signature=12cdf1ad669b4173c346f4909286b1012f0b346290329922ad5c1c5a8ab433d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z72FV4F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6up2eUCBvm9T%2F48PLI8TNcOGmvEVZY%2FkWPwDMReiOJAiBTSxVSfcJoySezroba9h2HPL662fmZ1K3%2BvpK%2FGzv1iyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSI42hXNR%2FmmMvBJTKtwDt2u6p%2FbxkI43amtYKVXpphkzkpBKX8gbLq29gb8njZVvxoP4QXriAAQDDtJUp%2Bl4rCDnykOMYcNxlVgDjbXuBAGrXxXzsVSA6WZLbrVI%2B2v4dIZXFmzdj2x3v8cQInCNiXepWsfT5NqgOS1vKjkRgpl9Te9NFhTzX%2B1tWe9IqPWzUtHPuJ71l2c4Yni%2Ff5hz59CFn%2FbJtvXrrEpaVOt0o98Ku23%2BndWNuv3ywT2qZAiHGwrwXjwy13Zx3ngIQQQmzIHNB4%2BRYXwVwR5wFU2cj0dJ0gyy7SAL43jHQwcBVeR6iVvnXl2A8Q809j%2BC9jimw3kN8CStODxe28DLqdwBhxryggznp%2Bavx5DS0BOoXzynwfUwVaDT9yecL%2BUWbiJ3tt5WmlA3ylfskFlv1cfIfbogThmGBzt3r1%2FLoccrI1bJlLlkY%2FTwBCU7p41XR5t8%2FH60SW5UEagmJm165AtisQLV5JZ%2FjBEGKCoJKo0iB3SaQzcXnSVeyrWXBpIk%2BnynA15idWJep1THeGzEfHrip510BmC7DtxGE%2BXKqzB6Bg1DdcQOA4C4Np%2FDne3DzItonzL20RrPpwZAUDsICV2mp96i21IVqJauabl67MjkDXBXDv3ESM5b3hXd0iswub%2BAvQY6pgFccYgIu9XwQiOkLr%2BqKxcgytZ76N265LRgsPyZmhihAOnm2QkMBYRMREyyJNyR1T4ubcN%2BJhc8hm3jW4g%2BSPUFK3DAwI3zlYymjFVutOhAfdnmnd1Nh6XGWQ8xiQAaC%2BzIibJbkzBINpPmud2zgGMnyg%2BnWrUd15GlGrB36uvCUBjICce8uWJs9KMdMnXXjqDx3KiK86%2BpBspACgRlViYVkZIrIUan&X-Amz-Signature=2d51d164fe9e5d34de3d74830730a0dc0de424772abb657180442558ea943673&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z72FV4F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6up2eUCBvm9T%2F48PLI8TNcOGmvEVZY%2FkWPwDMReiOJAiBTSxVSfcJoySezroba9h2HPL662fmZ1K3%2BvpK%2FGzv1iyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSI42hXNR%2FmmMvBJTKtwDt2u6p%2FbxkI43amtYKVXpphkzkpBKX8gbLq29gb8njZVvxoP4QXriAAQDDtJUp%2Bl4rCDnykOMYcNxlVgDjbXuBAGrXxXzsVSA6WZLbrVI%2B2v4dIZXFmzdj2x3v8cQInCNiXepWsfT5NqgOS1vKjkRgpl9Te9NFhTzX%2B1tWe9IqPWzUtHPuJ71l2c4Yni%2Ff5hz59CFn%2FbJtvXrrEpaVOt0o98Ku23%2BndWNuv3ywT2qZAiHGwrwXjwy13Zx3ngIQQQmzIHNB4%2BRYXwVwR5wFU2cj0dJ0gyy7SAL43jHQwcBVeR6iVvnXl2A8Q809j%2BC9jimw3kN8CStODxe28DLqdwBhxryggznp%2Bavx5DS0BOoXzynwfUwVaDT9yecL%2BUWbiJ3tt5WmlA3ylfskFlv1cfIfbogThmGBzt3r1%2FLoccrI1bJlLlkY%2FTwBCU7p41XR5t8%2FH60SW5UEagmJm165AtisQLV5JZ%2FjBEGKCoJKo0iB3SaQzcXnSVeyrWXBpIk%2BnynA15idWJep1THeGzEfHrip510BmC7DtxGE%2BXKqzB6Bg1DdcQOA4C4Np%2FDne3DzItonzL20RrPpwZAUDsICV2mp96i21IVqJauabl67MjkDXBXDv3ESM5b3hXd0iswub%2BAvQY6pgFccYgIu9XwQiOkLr%2BqKxcgytZ76N265LRgsPyZmhihAOnm2QkMBYRMREyyJNyR1T4ubcN%2BJhc8hm3jW4g%2BSPUFK3DAwI3zlYymjFVutOhAfdnmnd1Nh6XGWQ8xiQAaC%2BzIibJbkzBINpPmud2zgGMnyg%2BnWrUd15GlGrB36uvCUBjICce8uWJs9KMdMnXXjqDx3KiK86%2BpBspACgRlViYVkZIrIUan&X-Amz-Signature=738b6604b9cfc691e7da3896a1877ca564ad41029513a53aacf0c709f334ad86&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z72FV4F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6up2eUCBvm9T%2F48PLI8TNcOGmvEVZY%2FkWPwDMReiOJAiBTSxVSfcJoySezroba9h2HPL662fmZ1K3%2BvpK%2FGzv1iyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSI42hXNR%2FmmMvBJTKtwDt2u6p%2FbxkI43amtYKVXpphkzkpBKX8gbLq29gb8njZVvxoP4QXriAAQDDtJUp%2Bl4rCDnykOMYcNxlVgDjbXuBAGrXxXzsVSA6WZLbrVI%2B2v4dIZXFmzdj2x3v8cQInCNiXepWsfT5NqgOS1vKjkRgpl9Te9NFhTzX%2B1tWe9IqPWzUtHPuJ71l2c4Yni%2Ff5hz59CFn%2FbJtvXrrEpaVOt0o98Ku23%2BndWNuv3ywT2qZAiHGwrwXjwy13Zx3ngIQQQmzIHNB4%2BRYXwVwR5wFU2cj0dJ0gyy7SAL43jHQwcBVeR6iVvnXl2A8Q809j%2BC9jimw3kN8CStODxe28DLqdwBhxryggznp%2Bavx5DS0BOoXzynwfUwVaDT9yecL%2BUWbiJ3tt5WmlA3ylfskFlv1cfIfbogThmGBzt3r1%2FLoccrI1bJlLlkY%2FTwBCU7p41XR5t8%2FH60SW5UEagmJm165AtisQLV5JZ%2FjBEGKCoJKo0iB3SaQzcXnSVeyrWXBpIk%2BnynA15idWJep1THeGzEfHrip510BmC7DtxGE%2BXKqzB6Bg1DdcQOA4C4Np%2FDne3DzItonzL20RrPpwZAUDsICV2mp96i21IVqJauabl67MjkDXBXDv3ESM5b3hXd0iswub%2BAvQY6pgFccYgIu9XwQiOkLr%2BqKxcgytZ76N265LRgsPyZmhihAOnm2QkMBYRMREyyJNyR1T4ubcN%2BJhc8hm3jW4g%2BSPUFK3DAwI3zlYymjFVutOhAfdnmnd1Nh6XGWQ8xiQAaC%2BzIibJbkzBINpPmud2zgGMnyg%2BnWrUd15GlGrB36uvCUBjICce8uWJs9KMdMnXXjqDx3KiK86%2BpBspACgRlViYVkZIrIUan&X-Amz-Signature=98f24cd3212332d6ccf466a56892893f1af834fbed5e0c7e24224b17bbb58f15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z72FV4F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6up2eUCBvm9T%2F48PLI8TNcOGmvEVZY%2FkWPwDMReiOJAiBTSxVSfcJoySezroba9h2HPL662fmZ1K3%2BvpK%2FGzv1iyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSI42hXNR%2FmmMvBJTKtwDt2u6p%2FbxkI43amtYKVXpphkzkpBKX8gbLq29gb8njZVvxoP4QXriAAQDDtJUp%2Bl4rCDnykOMYcNxlVgDjbXuBAGrXxXzsVSA6WZLbrVI%2B2v4dIZXFmzdj2x3v8cQInCNiXepWsfT5NqgOS1vKjkRgpl9Te9NFhTzX%2B1tWe9IqPWzUtHPuJ71l2c4Yni%2Ff5hz59CFn%2FbJtvXrrEpaVOt0o98Ku23%2BndWNuv3ywT2qZAiHGwrwXjwy13Zx3ngIQQQmzIHNB4%2BRYXwVwR5wFU2cj0dJ0gyy7SAL43jHQwcBVeR6iVvnXl2A8Q809j%2BC9jimw3kN8CStODxe28DLqdwBhxryggznp%2Bavx5DS0BOoXzynwfUwVaDT9yecL%2BUWbiJ3tt5WmlA3ylfskFlv1cfIfbogThmGBzt3r1%2FLoccrI1bJlLlkY%2FTwBCU7p41XR5t8%2FH60SW5UEagmJm165AtisQLV5JZ%2FjBEGKCoJKo0iB3SaQzcXnSVeyrWXBpIk%2BnynA15idWJep1THeGzEfHrip510BmC7DtxGE%2BXKqzB6Bg1DdcQOA4C4Np%2FDne3DzItonzL20RrPpwZAUDsICV2mp96i21IVqJauabl67MjkDXBXDv3ESM5b3hXd0iswub%2BAvQY6pgFccYgIu9XwQiOkLr%2BqKxcgytZ76N265LRgsPyZmhihAOnm2QkMBYRMREyyJNyR1T4ubcN%2BJhc8hm3jW4g%2BSPUFK3DAwI3zlYymjFVutOhAfdnmnd1Nh6XGWQ8xiQAaC%2BzIibJbkzBINpPmud2zgGMnyg%2BnWrUd15GlGrB36uvCUBjICce8uWJs9KMdMnXXjqDx3KiK86%2BpBspACgRlViYVkZIrIUan&X-Amz-Signature=dcb2fadb05d68cdf313ba84a891b12bb1bb65ec4752aaa005b08a342aa962283&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z72FV4F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6up2eUCBvm9T%2F48PLI8TNcOGmvEVZY%2FkWPwDMReiOJAiBTSxVSfcJoySezroba9h2HPL662fmZ1K3%2BvpK%2FGzv1iyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSI42hXNR%2FmmMvBJTKtwDt2u6p%2FbxkI43amtYKVXpphkzkpBKX8gbLq29gb8njZVvxoP4QXriAAQDDtJUp%2Bl4rCDnykOMYcNxlVgDjbXuBAGrXxXzsVSA6WZLbrVI%2B2v4dIZXFmzdj2x3v8cQInCNiXepWsfT5NqgOS1vKjkRgpl9Te9NFhTzX%2B1tWe9IqPWzUtHPuJ71l2c4Yni%2Ff5hz59CFn%2FbJtvXrrEpaVOt0o98Ku23%2BndWNuv3ywT2qZAiHGwrwXjwy13Zx3ngIQQQmzIHNB4%2BRYXwVwR5wFU2cj0dJ0gyy7SAL43jHQwcBVeR6iVvnXl2A8Q809j%2BC9jimw3kN8CStODxe28DLqdwBhxryggznp%2Bavx5DS0BOoXzynwfUwVaDT9yecL%2BUWbiJ3tt5WmlA3ylfskFlv1cfIfbogThmGBzt3r1%2FLoccrI1bJlLlkY%2FTwBCU7p41XR5t8%2FH60SW5UEagmJm165AtisQLV5JZ%2FjBEGKCoJKo0iB3SaQzcXnSVeyrWXBpIk%2BnynA15idWJep1THeGzEfHrip510BmC7DtxGE%2BXKqzB6Bg1DdcQOA4C4Np%2FDne3DzItonzL20RrPpwZAUDsICV2mp96i21IVqJauabl67MjkDXBXDv3ESM5b3hXd0iswub%2BAvQY6pgFccYgIu9XwQiOkLr%2BqKxcgytZ76N265LRgsPyZmhihAOnm2QkMBYRMREyyJNyR1T4ubcN%2BJhc8hm3jW4g%2BSPUFK3DAwI3zlYymjFVutOhAfdnmnd1Nh6XGWQ8xiQAaC%2BzIibJbkzBINpPmud2zgGMnyg%2BnWrUd15GlGrB36uvCUBjICce8uWJs9KMdMnXXjqDx3KiK86%2BpBspACgRlViYVkZIrIUan&X-Amz-Signature=e4639c9ca2f44c2771413507004ecb5a3f851920f46ada21343fbe35aca40142&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z72FV4F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6up2eUCBvm9T%2F48PLI8TNcOGmvEVZY%2FkWPwDMReiOJAiBTSxVSfcJoySezroba9h2HPL662fmZ1K3%2BvpK%2FGzv1iyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSI42hXNR%2FmmMvBJTKtwDt2u6p%2FbxkI43amtYKVXpphkzkpBKX8gbLq29gb8njZVvxoP4QXriAAQDDtJUp%2Bl4rCDnykOMYcNxlVgDjbXuBAGrXxXzsVSA6WZLbrVI%2B2v4dIZXFmzdj2x3v8cQInCNiXepWsfT5NqgOS1vKjkRgpl9Te9NFhTzX%2B1tWe9IqPWzUtHPuJ71l2c4Yni%2Ff5hz59CFn%2FbJtvXrrEpaVOt0o98Ku23%2BndWNuv3ywT2qZAiHGwrwXjwy13Zx3ngIQQQmzIHNB4%2BRYXwVwR5wFU2cj0dJ0gyy7SAL43jHQwcBVeR6iVvnXl2A8Q809j%2BC9jimw3kN8CStODxe28DLqdwBhxryggznp%2Bavx5DS0BOoXzynwfUwVaDT9yecL%2BUWbiJ3tt5WmlA3ylfskFlv1cfIfbogThmGBzt3r1%2FLoccrI1bJlLlkY%2FTwBCU7p41XR5t8%2FH60SW5UEagmJm165AtisQLV5JZ%2FjBEGKCoJKo0iB3SaQzcXnSVeyrWXBpIk%2BnynA15idWJep1THeGzEfHrip510BmC7DtxGE%2BXKqzB6Bg1DdcQOA4C4Np%2FDne3DzItonzL20RrPpwZAUDsICV2mp96i21IVqJauabl67MjkDXBXDv3ESM5b3hXd0iswub%2BAvQY6pgFccYgIu9XwQiOkLr%2BqKxcgytZ76N265LRgsPyZmhihAOnm2QkMBYRMREyyJNyR1T4ubcN%2BJhc8hm3jW4g%2BSPUFK3DAwI3zlYymjFVutOhAfdnmnd1Nh6XGWQ8xiQAaC%2BzIibJbkzBINpPmud2zgGMnyg%2BnWrUd15GlGrB36uvCUBjICce8uWJs9KMdMnXXjqDx3KiK86%2BpBspACgRlViYVkZIrIUan&X-Amz-Signature=b43e0514109352786ca9ed01bb82de0d19c104ee1a7284d40196ca39a591007f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ILHCPBE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG6Q17YZYXruzga2oH1Jmuvgx6UJbnVDfe3cOPJrZWdVAiBTxN1CO1F8iEDRjZp7bvlaZZwTj7Xgf3Dq6q1NIZjBsSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT%2FtMiirrgT4sfbwJKtwDP4vpOyjWIDB7%2B8ByGCt%2FlmPJpkjdFDBooxDTFYv9yfzjVoy3RYG9IML1uC%2F4C5P3sBiuGpMagdpuwdzqL%2BH6WfoeRHmDYkBfHic433XBO2ZZTeEXjpp%2FK8N0G4t9OIrSYRXXNqX02%2BkdsDXxuxVZ7I9spToxpQDe%2BEFUb1FCs7axZLIshK8i1EpaonvtbC15uDa21MGXETkpxx8TKeB2rnVoVs%2FS33uArN0JIvGLH%2BOgVyZ6ij%2F53ZA00ZYI8CmYLF8z3p2UygW9NcLROIsLov%2BaBn9D8LJH8xmrRegJQ7WZlG9z8UuUnK6AJqO7YhKnpD8JMOA%2BPDFJkNzPDkLz8T6HWyjGrXJ%2FfUnvE88kxWZS8peZ4jE4RaKWWZQWGoxOlE4gce5Xpm1%2BjuQkoae67C%2B9OWBxrMW7eDwCrL9B7EzB4tSmb89SNkqM9GG%2Foj31T6mbmb4IgbgSbRcnJK%2BzBh2W5xpo0i4JiodFTcKMZLbsCWaQz3eySAFpptNnGwTNcQZXlwxgQEk21nCy8tqcL38FnUEBUsXF2dJac4U89XV%2Fu17b12f6nfypcv%2BHCd24MkGJFD219C2kpGgibWvGaBNVzy3rX7Z1oPch0p22opgVplWNSlDgL3W3VeowvsCAvQY6pgE%2FjAo6HLRbVL2aHFT8BE%2FFibAM86SscsGT0MmkT%2FjqJNO9xbq5GzFzXQJatWGFI1v3kSkC1VwTHDjkwuT0MA0yIO26G4LeJWP7W1DNpQo3HOtPS1PWgNsQ%2BDxxVwRgf9gLTd9aSG7DF4e8g99DGOnzUcvqX3egvwlwK%2FevtTN6cr8s3EmjFAhtV8hWAyHel%2Bp2%2BpGcjuQzBz%2FaZN%2FnUyTx8jpJLsue&X-Amz-Signature=299c6334498a17ad77ce192ffd7d3533209e1592586bf4ac34e8d2bb7325871b&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGMCM6QU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCb5xa0P7XrskuR%2FPU42E9%2B2URt1O3dGQAcbtaP57bC6AIhANkC4PQ2S0U9XAIfxm8qYeyTq3%2FZM94vxRq7mEYbgNIbKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEoxk7EQdzQnnkiHcq3APE3kGpxs4%2B6lQZeSUteiMZv6hzZmVkxGPRSxNIpCIt4bOBtdKpfVqa2dZBUEmP%2F6j3ybU5zpS0D4FAgEND6Wu7837EeqF12vCBX07dR529dDaoO7sPYjdtAd%2BjuVubwvCVu2GEZdtg%2BIntHHaTFzTi4FUsuHj6eDtMT4EKx4Xvd4XgbpTbgczOcx3PK87yCJ%2FjPrLFaFEjvflq7v8ckM0cKx%2B6KYaVBGtboc28vwJ0PGhoZ1RyWPIRCD9pbcJZC7epFZlTI9742CJBJ%2BkEuxi5%2Fz7bULuML8DECKnjiF%2BG1jvI%2BAp5aCiO5AqA6k38EsWLMtXDgSLd%2FFcEn9RBklHuY8YrpG6j02CIOFqQd9vzpS9LpbRGg0AEtWr%2BnSxCvH5PQTZAk%2B8LchrsstoNZ2viCwfT9VpQ%2BlvoJFiAfbgBsQJbPedtEGDAwLwyGOPBawnagZUsnPYWsshwwEjkCMKx837JFPcXuUbST8Bjc2RnInYfJruGosX5m2SKJe8d%2FGTIno23TjwElm1rlE8I7PPF3oXt6iTn%2BwjTQm8KeCncCFF3D4ClZa9NKo2LZU6mKwfVxPfyfIzIzjG1KN6SdgjhpWFGRljdys7%2FbAZ7GkC17Cd220Uu4xydwkK%2BRTCPwIC9BjqkAYYanwlL7klMn42gYaEJP%2BlBSOgkW%2F3%2FVJWkYWO29qnU6BaUhcNfIrQ07chBHCkfyxAleb%2BUwHuazYUx8Br4wCsfKH4J1%2Fy%2BFqNTnDI072VsBeIzcMqWtoClQpVZt5hHUHC7LKrvxU0eyXIKpykiDa2BBq6vtEdbezvrCpXV0KzSWxtx9Gfg%2FqYITHa3lxl6BHQbuRnuiK7fZDkJVURA7i0eSi5X&X-Amz-Signature=679eed9d932633d7c8718777280cbdc48d2fdb5fe979c3073ebea96ec8201e74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z72FV4F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6up2eUCBvm9T%2F48PLI8TNcOGmvEVZY%2FkWPwDMReiOJAiBTSxVSfcJoySezroba9h2HPL662fmZ1K3%2BvpK%2FGzv1iyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSI42hXNR%2FmmMvBJTKtwDt2u6p%2FbxkI43amtYKVXpphkzkpBKX8gbLq29gb8njZVvxoP4QXriAAQDDtJUp%2Bl4rCDnykOMYcNxlVgDjbXuBAGrXxXzsVSA6WZLbrVI%2B2v4dIZXFmzdj2x3v8cQInCNiXepWsfT5NqgOS1vKjkRgpl9Te9NFhTzX%2B1tWe9IqPWzUtHPuJ71l2c4Yni%2Ff5hz59CFn%2FbJtvXrrEpaVOt0o98Ku23%2BndWNuv3ywT2qZAiHGwrwXjwy13Zx3ngIQQQmzIHNB4%2BRYXwVwR5wFU2cj0dJ0gyy7SAL43jHQwcBVeR6iVvnXl2A8Q809j%2BC9jimw3kN8CStODxe28DLqdwBhxryggznp%2Bavx5DS0BOoXzynwfUwVaDT9yecL%2BUWbiJ3tt5WmlA3ylfskFlv1cfIfbogThmGBzt3r1%2FLoccrI1bJlLlkY%2FTwBCU7p41XR5t8%2FH60SW5UEagmJm165AtisQLV5JZ%2FjBEGKCoJKo0iB3SaQzcXnSVeyrWXBpIk%2BnynA15idWJep1THeGzEfHrip510BmC7DtxGE%2BXKqzB6Bg1DdcQOA4C4Np%2FDne3DzItonzL20RrPpwZAUDsICV2mp96i21IVqJauabl67MjkDXBXDv3ESM5b3hXd0iswub%2BAvQY6pgFccYgIu9XwQiOkLr%2BqKxcgytZ76N265LRgsPyZmhihAOnm2QkMBYRMREyyJNyR1T4ubcN%2BJhc8hm3jW4g%2BSPUFK3DAwI3zlYymjFVutOhAfdnmnd1Nh6XGWQ8xiQAaC%2BzIibJbkzBINpPmud2zgGMnyg%2BnWrUd15GlGrB36uvCUBjICce8uWJs9KMdMnXXjqDx3KiK86%2BpBspACgRlViYVkZIrIUan&X-Amz-Signature=547c0bb96ef7b20c0ab53d556f98bd8144291ed9ef4c75571d9a77758cf38b3e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z72FV4F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6up2eUCBvm9T%2F48PLI8TNcOGmvEVZY%2FkWPwDMReiOJAiBTSxVSfcJoySezroba9h2HPL662fmZ1K3%2BvpK%2FGzv1iyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSI42hXNR%2FmmMvBJTKtwDt2u6p%2FbxkI43amtYKVXpphkzkpBKX8gbLq29gb8njZVvxoP4QXriAAQDDtJUp%2Bl4rCDnykOMYcNxlVgDjbXuBAGrXxXzsVSA6WZLbrVI%2B2v4dIZXFmzdj2x3v8cQInCNiXepWsfT5NqgOS1vKjkRgpl9Te9NFhTzX%2B1tWe9IqPWzUtHPuJ71l2c4Yni%2Ff5hz59CFn%2FbJtvXrrEpaVOt0o98Ku23%2BndWNuv3ywT2qZAiHGwrwXjwy13Zx3ngIQQQmzIHNB4%2BRYXwVwR5wFU2cj0dJ0gyy7SAL43jHQwcBVeR6iVvnXl2A8Q809j%2BC9jimw3kN8CStODxe28DLqdwBhxryggznp%2Bavx5DS0BOoXzynwfUwVaDT9yecL%2BUWbiJ3tt5WmlA3ylfskFlv1cfIfbogThmGBzt3r1%2FLoccrI1bJlLlkY%2FTwBCU7p41XR5t8%2FH60SW5UEagmJm165AtisQLV5JZ%2FjBEGKCoJKo0iB3SaQzcXnSVeyrWXBpIk%2BnynA15idWJep1THeGzEfHrip510BmC7DtxGE%2BXKqzB6Bg1DdcQOA4C4Np%2FDne3DzItonzL20RrPpwZAUDsICV2mp96i21IVqJauabl67MjkDXBXDv3ESM5b3hXd0iswub%2BAvQY6pgFccYgIu9XwQiOkLr%2BqKxcgytZ76N265LRgsPyZmhihAOnm2QkMBYRMREyyJNyR1T4ubcN%2BJhc8hm3jW4g%2BSPUFK3DAwI3zlYymjFVutOhAfdnmnd1Nh6XGWQ8xiQAaC%2BzIibJbkzBINpPmud2zgGMnyg%2BnWrUd15GlGrB36uvCUBjICce8uWJs9KMdMnXXjqDx3KiK86%2BpBspACgRlViYVkZIrIUan&X-Amz-Signature=64362628071fe19a874935b349269460d5bc8e202f3b2fd47c80477fb7a5bc4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z72FV4F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6up2eUCBvm9T%2F48PLI8TNcOGmvEVZY%2FkWPwDMReiOJAiBTSxVSfcJoySezroba9h2HPL662fmZ1K3%2BvpK%2FGzv1iyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSI42hXNR%2FmmMvBJTKtwDt2u6p%2FbxkI43amtYKVXpphkzkpBKX8gbLq29gb8njZVvxoP4QXriAAQDDtJUp%2Bl4rCDnykOMYcNxlVgDjbXuBAGrXxXzsVSA6WZLbrVI%2B2v4dIZXFmzdj2x3v8cQInCNiXepWsfT5NqgOS1vKjkRgpl9Te9NFhTzX%2B1tWe9IqPWzUtHPuJ71l2c4Yni%2Ff5hz59CFn%2FbJtvXrrEpaVOt0o98Ku23%2BndWNuv3ywT2qZAiHGwrwXjwy13Zx3ngIQQQmzIHNB4%2BRYXwVwR5wFU2cj0dJ0gyy7SAL43jHQwcBVeR6iVvnXl2A8Q809j%2BC9jimw3kN8CStODxe28DLqdwBhxryggznp%2Bavx5DS0BOoXzynwfUwVaDT9yecL%2BUWbiJ3tt5WmlA3ylfskFlv1cfIfbogThmGBzt3r1%2FLoccrI1bJlLlkY%2FTwBCU7p41XR5t8%2FH60SW5UEagmJm165AtisQLV5JZ%2FjBEGKCoJKo0iB3SaQzcXnSVeyrWXBpIk%2BnynA15idWJep1THeGzEfHrip510BmC7DtxGE%2BXKqzB6Bg1DdcQOA4C4Np%2FDne3DzItonzL20RrPpwZAUDsICV2mp96i21IVqJauabl67MjkDXBXDv3ESM5b3hXd0iswub%2BAvQY6pgFccYgIu9XwQiOkLr%2BqKxcgytZ76N265LRgsPyZmhihAOnm2QkMBYRMREyyJNyR1T4ubcN%2BJhc8hm3jW4g%2BSPUFK3DAwI3zlYymjFVutOhAfdnmnd1Nh6XGWQ8xiQAaC%2BzIibJbkzBINpPmud2zgGMnyg%2BnWrUd15GlGrB36uvCUBjICce8uWJs9KMdMnXXjqDx3KiK86%2BpBspACgRlViYVkZIrIUan&X-Amz-Signature=281920630cf3775924bb51be755e0a3b226355d9a8a7c74f8b35db8fa42dd166&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ7324CB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG219riaT5oe%2F4L62jryZ%2FYd898dJH0s1E1abAbnzpluAiEA1FyEZCwHbilq79Ewo3Srd5f9KAtCwmmzJllTDfS1b5sqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBu8%2FO6DF9u7DCla9CrcA9HNCH7NTUyrqzMKhFQ0ckIC6xOQIsu8jwkRaccisHw%2F%2F1mP5mgYrYvEbgbUYbUF2Ed3chXlccCRX9UdF1ALIbpBFQOLb6gPrVpi%2F8v38C2tac9sITVP4QOYKsYKUOHP40JfZP1%2BvFM5S8N0Kw4qenSZgmccvzr5HHR5lGnYJnmvFFkkNIuZaTrFwlE3f5%2FJwBNolmDgFkNsfMAhTcajjtFWYon1XxsBsltALgoca2PVrJXHhDrFOta3mHrvNqVW%2BKTQgJwOeDNaTnMbSKesFm1zGvvV4FEJnngBhqAL7UuMgcbyXetW%2FuiH5buFqf3Tm4kR4KQZDNgxKUQ8SDB7yFbz8Ok%2B%2FMuYTy9EVC3c%2BVJ31rhfk2UA998ek0rBC8HFufe30W52DEMu94dpo7N6GdpTAcXwhGtcsBUZ8lGlFvvT7y7EuAEzNXExgCVMT1xzYKwYW3fdhXY2qH4vgkl6xYYiPA2mkZitK5gl3ndsrd%2BcOTdmiqb5zeBBN8HO0%2FA%2BghRJK%2BltmrxI4ZgKYF1HT3qF4S6Px%2Fp6QRvt9VR9dF%2B7DS6I0bBRIs2Su4MSHrunX2mP2bt3GcsQCKoSeSBlksuaqQjBUnz4K6Zv1JNUOzy0PPoFEc0w%2F5jrHeZYMNO%2FgL0GOqUBbx%2BKvUMvExvIeVfrgNenwTWZNzbf5s0lGTRErpz53N07MK2rSyQX1khR7l5Uyyjv67jTeOs1nlGhAPjS9oEb5Bb9gLSI9v9gtViDT56N5jisH05aZPsUxeIJb8TObq4ZOf6L9SpTHYbGJukYUqu4wCCgwncNnq2SgQqixbxCyOtIRjOJxWoOm3rjTqmxKhVd2zza1aGYILXDUuDBFbxfQNQ833Be&X-Amz-Signature=42e59688425323486d1c66079c6a40a5d4d02353d81b4fddce19c56b9eb1bd69&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDD6W3DD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDpWou7rfgV6DcHfDB0aF8k6AmxUg%2Ft8zVbksOOI5XWhAiEAg3%2BJKN8DTwiZq21hZbG1fMsdlngG7TLfAQmC46mfbfMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEabzz6cafj6pKs74CrcA%2BCbRscFfjZ3uKzy1sp1R1J7MD%2B2lukWRSzFN6Lt04DGaZMdxIZ380o3BMthd9BsryYesNWcP0e%2BIcJZAPPDPSgC4yNapjxploX8Vi%2BsfNq8AIVDPvczJUycg8CKCx4Tzp6SkXHZhX62noocGGj8VelTb7ahg%2FdXqlE0WASwYHzF4cW6gAhuCwk1QahT33lDjpUUItKKvU1AcraJlqNujiJsmK6%2FdSbPKWDFV36aybyfDHi%2BUf15yUrZiHpzsHkpVR028a6GjSFMULKi2O2oBnoIu7hX%2BOYsiz2rmEYFvjyacWH5z68r%2B%2FJ3gYe6emhHdoDhZCeU%2F2h0rNgpFICIiwYXS7dCRymykUGcTQmWj4ROEP2iGpHo%2Fas%2FhgF7HsD0AIGor4sEHuIm%2BGQx4pVF5zrLteekYYvB2eucINVN1JHV0x4aZmU0Mk1zFLQcK1A00B6KHXR3ND6G0pqVi7TrdIqLNUEsewpb1dY0mdxEBJyCCjTfW%2FFPaUIFUkux6i3%2BGpzSTkM8wa3csziJQSU16R%2FN3eh%2FWhkh8VzkZXd7qQ3oRLV%2B9lWSA6Ya5YxMsLBJ%2BMpErAoKfClQOr9A1SE2uqFzFS%2BLt4oAGXAIQogLTeg6RgrafrRTfpKDbs%2F7MMG%2FgL0GOqUBLJqGJRjd1edcavqGjQ0ud5cnekFFu7eSQniAD6tBXFPbMv7EkW3vjlPUEq10w6Ip0kYNpLm%2FOmO0ng5tBhBogQveBy9Fg9j3WxQ2aoUwMyATPUcKleg1VQBZwcj13JXfw%2FWJTT9j2KGMpqxT66GncJYcN9kWRn8TT%2FbzHjWjWWBWRyVg0%2ByOCU0SxLQQrX4akx6MAm2OPvLDYZreA5dvWOqizbCj&X-Amz-Signature=dd9d4a9aeaf458a76937803d3808108d11f1b66852ac126b912ddfc3fab51e9b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MJB4G4T%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8V6DgGbA%2Fl79FPXR5DExsncpiHnThIGRYJL0XsgXRYAIhALHPOhj%2Bm5IKoEIYt%2B81GddmPGyc0U%2BBWPMjwLDF5iWRKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbK1i8wV%2FOWhNhDfgq3AMBzSz5%2BQowNGtOmviDPZG0vIjBFtxnGM8nJGLjEU1VN7Qh3HyyRwNHbtjayhfN7l4O7lToowbsl2%2Fs21DOEik1ZnFJpka3gpuA4XXQdUSh75U%2B3EwK0D%2BlRafm%2FugF%2BX4ff%2Bg%2FUqLq4LRGAAB%2Bhc5FkANm%2BCCTFOvtzOUXADxFkAGjvvng6PC6sPc9uG9aQ2f42%2BjPHD%2FvwloXYQ%2BCM073AyIaTjpSJ%2F%2FS%2BCWtRLMdJGgjnURDwEdK8YLgPw0Hpd8PBsJIa7F3Uod%2FCcTeMMTeIgoCk6D288KeOV55719R9Lhk47mhu4VZH7hM8qNN54Be6MhO25vazvy%2FMCeNdnadtYCilLAfj95fYFAFsVScWroblNNtmmVWFrz94jatuDVXpOGEidQQjpOd4yCzW%2FUYNmxmZ6PiaDrTpC0ar6gtqYxfJeq3yceJOPbOiRKoHTfpd%2FwEIj1yrzfSX1bxwI5jNdmDbo05ewfbs5cggS7f0iMBTWJUGwxX5MKCz4b54AOailhte3gmiRf0nhJJJKPy2psQ2OumS6X9E0wP16KmsQLv%2BBuH2sFfX%2Bf%2BHtmtvbfPv3cMRlkD25W%2BF8t9ZpOj%2BCyfYCxdxdb7mjJ0G%2BFb%2BqXZadFPSpvEmWdNWzCXv4C9BjqkAeLIWsQnz5zlUBtdpC2tURpsciXdyaNOoTt0TEPXWX3fZGDo9%2BVAFBflNGVFRKHYcSSQ%2FA%2BikO3He7MvrzURVThrGUlwX7GDLZcXBbiINm1LiV1KuBz%2B8FzQ8jGZAa1R4MeH205L54%2F544LxVUmCEXbCUJzQmuuV1Mj9i97cJRdNXxD1p0k3GgWEv8EZwoFGA6OdGrlLmSIJ5NMl0uu5XRp%2FSynO&X-Amz-Signature=0d9f5712c141cee4d06b068dbc827bb39cf6cca5ae864d018c56836e2d6cc3b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ENB3J4L%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGMOJnJso4CcPsZzFtisd%2FUIBv2LgmcKEw5zo%2FoIxQlyAiEAmtBB7ZjBMp1wY7IkznvHhHqPkRng9PhmR9W2Xr5eo5IqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2%2FKqMKnzeCYsah2CrcA6vOlvCXKcD5rEn38Q2CX62%2B5GVJT44f%2FQ0ZLeYtO847xLxe0sFDcYCoremLTZ1ZkuKTKzJLmZhw3KNwnTe0tsYaqMXSZr0OsNQyLfSdNcy%2FFkmAsQ8kxVmgpwYZbrm4JRPFqv%2BQ%2FqYbxWHvA21tNUy6g7XvBJZ0lqEJBIFy5O1UOuxSIpD%2FeZ5S8vyXgg2PSnh6pUBRHLSuCQ7avnx07f1D%2Fo5RuzaJ%2BSWQhPLtp%2BtvpaOzTm9CHZf9ljGnC52WpCTk2CGJdCj5cNLck9HDksr%2FVMkt26OkIs7fR4hURmjYQ0p0WO2tIG98HCGLP7xv0DMBfOu8HewfyCjLAxG8iogDjaS4NUpz9rbeRhNPmCeaQOICXcXsPPEFCrCbpZZKgZ3FRYRB859DdyTadYhA%2FIleIIVDJaUg%2FMTWdxBHrX%2FPEbyXfuK97kxYA8pbCJT7479vZdeFgQaDYgvRrvT80vf5ECXLQEkWkDklJKewwGSFNOV3LcQL47zESn7ngC0GnHCKmBG04ztfvwUwaT2nn8wuPZLgKhwzyRak%2BvRYnhpQXsAueRHUqIs1jLV3W%2F6fn2Hvfsrchze3nXRA6zB3IHSqWr5sEUGlj3QN3Ek8h%2FvOdaeFd3KFKqBS1WKGMIq%2FgL0GOqUBi6OOAvI3kIS9NrdP9xYs34u2%2FMeeeg%2BBPqZBNRSlS2Z0RlDGhtSpHRZfms8FblOeG6iMgJkeWAJ6xW9pbChMaG3f8hba7ZZZXUFO4xGPRsEKNjJengys5ZWyofUVcHrQC7twcmg3pMoxVmsmy8eyg0iVXndEwjHLG8SlBoJ53p5C1sou6rvU7gv4LnCIKlSnSkB4KueIta631iMyWBbA6%2BSLWJcm&X-Amz-Signature=0660882e5c1d3e41e79ea22a677174393ed0f07ceb554d5dbaae8c9a609b8c5f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ENB3J4L%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGMOJnJso4CcPsZzFtisd%2FUIBv2LgmcKEw5zo%2FoIxQlyAiEAmtBB7ZjBMp1wY7IkznvHhHqPkRng9PhmR9W2Xr5eo5IqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2%2FKqMKnzeCYsah2CrcA6vOlvCXKcD5rEn38Q2CX62%2B5GVJT44f%2FQ0ZLeYtO847xLxe0sFDcYCoremLTZ1ZkuKTKzJLmZhw3KNwnTe0tsYaqMXSZr0OsNQyLfSdNcy%2FFkmAsQ8kxVmgpwYZbrm4JRPFqv%2BQ%2FqYbxWHvA21tNUy6g7XvBJZ0lqEJBIFy5O1UOuxSIpD%2FeZ5S8vyXgg2PSnh6pUBRHLSuCQ7avnx07f1D%2Fo5RuzaJ%2BSWQhPLtp%2BtvpaOzTm9CHZf9ljGnC52WpCTk2CGJdCj5cNLck9HDksr%2FVMkt26OkIs7fR4hURmjYQ0p0WO2tIG98HCGLP7xv0DMBfOu8HewfyCjLAxG8iogDjaS4NUpz9rbeRhNPmCeaQOICXcXsPPEFCrCbpZZKgZ3FRYRB859DdyTadYhA%2FIleIIVDJaUg%2FMTWdxBHrX%2FPEbyXfuK97kxYA8pbCJT7479vZdeFgQaDYgvRrvT80vf5ECXLQEkWkDklJKewwGSFNOV3LcQL47zESn7ngC0GnHCKmBG04ztfvwUwaT2nn8wuPZLgKhwzyRak%2BvRYnhpQXsAueRHUqIs1jLV3W%2F6fn2Hvfsrchze3nXRA6zB3IHSqWr5sEUGlj3QN3Ek8h%2FvOdaeFd3KFKqBS1WKGMIq%2FgL0GOqUBi6OOAvI3kIS9NrdP9xYs34u2%2FMeeeg%2BBPqZBNRSlS2Z0RlDGhtSpHRZfms8FblOeG6iMgJkeWAJ6xW9pbChMaG3f8hba7ZZZXUFO4xGPRsEKNjJengys5ZWyofUVcHrQC7twcmg3pMoxVmsmy8eyg0iVXndEwjHLG8SlBoJ53p5C1sou6rvU7gv4LnCIKlSnSkB4KueIta631iMyWBbA6%2BSLWJcm&X-Amz-Signature=7706498a1cd76a7b2973780e654da4e7016c2765a58f77a7e6f99fc7fa8cb9c6&X-Amz-SignedHeaders=host&x-id=GetObject)

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
