

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHSWWIXP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsvd72%2FGwyIbRZGABYJlkV%2FAB1%2FHiAYKVTYhqPHMOj5AiEAumys4njqUi3RBpS%2FrSUxm8%2FrHQRpn%2F9IkyKpkvQvQnQqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkPEvNBA%2FUUHIqIwyrcAwumlnUV39nIKqRXFEM13YuvAz5LWNPx8xBNdTcf2jsQvaFgvajPm3uGF8OCDTS7Oe74lfOjpGlArs7H6NLWAwa5oXbNHiLtweczEyGaKg9NTalpcIMxBTds%2FCTj2gwWYItItxgnC80ihKxYYlu7i13%2B8398MhVcpUJGzTTZiI8pIZy3IIrg7qDIqE%2FnZOT5aYWnSRK50JNewSlejVXtm%2BwozXmJhqQ%2Fgta2z9H6PTmPHiDvy42grv0KKmm7PkYY14kGXS64ndBG53%2B82acdZlRbG6B1Hc8zLGogDZP66qJG6MVuk6SdJ4Z%2B756z%2BGtqf04vVm686shvvSiSK9kZP8JqR2q3nNnH45FpFtGhx%2FsrvIg8LNWGYf2OGJcfmO2vIUbiFgRnY8YVuV0Egkk9XrE9pVB3nLeQb%2BrrkTTTv3j%2FyAdVUf4Lo537ej3vk9Bv9DvoYlTjJl3h6D%2FxiSAUX6MjI%2FeK3Cya74nyJD23hngO903EXVTpVOrNyVLBdMEQ%2FHLa5jix9oWve9o4BJNl%2F3J0%2BMzxbLRxrr9rEHTDTSUvbYLgnvU8eNXby4nAVC7vqbMFu%2FrG7uA8L5yu5vSk4EVEcOL9CpgmU5iM1u48itWjaoiSkmLBLCJkijhGMLWm9rwGOqUB451FMTZW%2BCCAcGTPuBB8w9mw%2FcO4gDGK7CVWgrfMKLMbu9Fr9RgmMWWo3f5A%2BhIw3Yho89fE8NkZ6UL%2BHtj%2Bwi3E%2F9%2FAFNL751Jp2hC44Gc%2BjDDaXUgrCh70VuXeB8RqHXkz8xfW0Jt1DdPiaYyrXvGRDyJ2nNSJAeH%2BJCsFATk9kLpqJ4UbdelnPj3EYNUtBtSVGTktt4r3ZUFEaXAuNnshS1dy&X-Amz-Signature=47bf72de367202f9af9bcfaf0d82e98a22a9511c181109289c85951b252c0ec8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHSWWIXP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsvd72%2FGwyIbRZGABYJlkV%2FAB1%2FHiAYKVTYhqPHMOj5AiEAumys4njqUi3RBpS%2FrSUxm8%2FrHQRpn%2F9IkyKpkvQvQnQqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkPEvNBA%2FUUHIqIwyrcAwumlnUV39nIKqRXFEM13YuvAz5LWNPx8xBNdTcf2jsQvaFgvajPm3uGF8OCDTS7Oe74lfOjpGlArs7H6NLWAwa5oXbNHiLtweczEyGaKg9NTalpcIMxBTds%2FCTj2gwWYItItxgnC80ihKxYYlu7i13%2B8398MhVcpUJGzTTZiI8pIZy3IIrg7qDIqE%2FnZOT5aYWnSRK50JNewSlejVXtm%2BwozXmJhqQ%2Fgta2z9H6PTmPHiDvy42grv0KKmm7PkYY14kGXS64ndBG53%2B82acdZlRbG6B1Hc8zLGogDZP66qJG6MVuk6SdJ4Z%2B756z%2BGtqf04vVm686shvvSiSK9kZP8JqR2q3nNnH45FpFtGhx%2FsrvIg8LNWGYf2OGJcfmO2vIUbiFgRnY8YVuV0Egkk9XrE9pVB3nLeQb%2BrrkTTTv3j%2FyAdVUf4Lo537ej3vk9Bv9DvoYlTjJl3h6D%2FxiSAUX6MjI%2FeK3Cya74nyJD23hngO903EXVTpVOrNyVLBdMEQ%2FHLa5jix9oWve9o4BJNl%2F3J0%2BMzxbLRxrr9rEHTDTSUvbYLgnvU8eNXby4nAVC7vqbMFu%2FrG7uA8L5yu5vSk4EVEcOL9CpgmU5iM1u48itWjaoiSkmLBLCJkijhGMLWm9rwGOqUB451FMTZW%2BCCAcGTPuBB8w9mw%2FcO4gDGK7CVWgrfMKLMbu9Fr9RgmMWWo3f5A%2BhIw3Yho89fE8NkZ6UL%2BHtj%2Bwi3E%2F9%2FAFNL751Jp2hC44Gc%2BjDDaXUgrCh70VuXeB8RqHXkz8xfW0Jt1DdPiaYyrXvGRDyJ2nNSJAeH%2BJCsFATk9kLpqJ4UbdelnPj3EYNUtBtSVGTktt4r3ZUFEaXAuNnshS1dy&X-Amz-Signature=a227480d83a3e1a66d4a1cdef67c03378c57607bb46e3179dd7e7f8b4599ebf5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHSWWIXP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsvd72%2FGwyIbRZGABYJlkV%2FAB1%2FHiAYKVTYhqPHMOj5AiEAumys4njqUi3RBpS%2FrSUxm8%2FrHQRpn%2F9IkyKpkvQvQnQqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkPEvNBA%2FUUHIqIwyrcAwumlnUV39nIKqRXFEM13YuvAz5LWNPx8xBNdTcf2jsQvaFgvajPm3uGF8OCDTS7Oe74lfOjpGlArs7H6NLWAwa5oXbNHiLtweczEyGaKg9NTalpcIMxBTds%2FCTj2gwWYItItxgnC80ihKxYYlu7i13%2B8398MhVcpUJGzTTZiI8pIZy3IIrg7qDIqE%2FnZOT5aYWnSRK50JNewSlejVXtm%2BwozXmJhqQ%2Fgta2z9H6PTmPHiDvy42grv0KKmm7PkYY14kGXS64ndBG53%2B82acdZlRbG6B1Hc8zLGogDZP66qJG6MVuk6SdJ4Z%2B756z%2BGtqf04vVm686shvvSiSK9kZP8JqR2q3nNnH45FpFtGhx%2FsrvIg8LNWGYf2OGJcfmO2vIUbiFgRnY8YVuV0Egkk9XrE9pVB3nLeQb%2BrrkTTTv3j%2FyAdVUf4Lo537ej3vk9Bv9DvoYlTjJl3h6D%2FxiSAUX6MjI%2FeK3Cya74nyJD23hngO903EXVTpVOrNyVLBdMEQ%2FHLa5jix9oWve9o4BJNl%2F3J0%2BMzxbLRxrr9rEHTDTSUvbYLgnvU8eNXby4nAVC7vqbMFu%2FrG7uA8L5yu5vSk4EVEcOL9CpgmU5iM1u48itWjaoiSkmLBLCJkijhGMLWm9rwGOqUB451FMTZW%2BCCAcGTPuBB8w9mw%2FcO4gDGK7CVWgrfMKLMbu9Fr9RgmMWWo3f5A%2BhIw3Yho89fE8NkZ6UL%2BHtj%2Bwi3E%2F9%2FAFNL751Jp2hC44Gc%2BjDDaXUgrCh70VuXeB8RqHXkz8xfW0Jt1DdPiaYyrXvGRDyJ2nNSJAeH%2BJCsFATk9kLpqJ4UbdelnPj3EYNUtBtSVGTktt4r3ZUFEaXAuNnshS1dy&X-Amz-Signature=ab474bd9a54532416eec43a64e784ebd1d08ed68c8c7b0e5e3bce0001562c50d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3GWGOV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhp874xJkIF41bV58QutR2CZt%2FhaG9QYOEiEesqtCIbAiEAvmIleOKe8bVOn0NO%2FxEtLu2XUbrf7Nl4SFVoVKfYplcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPib8%2Bhg%2BOJRnDfdSrcA7vg1wjKa%2B9hiA3oBYLL4oriyX%2FQxNUrzlCj%2BjqXRhLUOVsHuzlUOQ8kLZQdf8cpg6LMo5OXB0cd8SeCzIURxgmtm8XWT6yWaE30Isjj%2Bych3fRxAlS6iqnokOh0qpKxIAee5T1Q0zEawb2S%2FE8C8pF%2FFCWOtXx7U4sFgE%2FE%2BEt%2F7Ic6%2BC0kG9qpXHEM54sJIQ7r0vHDH4BGcX7mun1lt2AkaUpK2zg0EMZeqQ%2FM0Ac1Vng1pv7dVsJ0r5X08Ge6nhdHuDSAV%2B3qcHq1jbIHAtFjxK0DYMMWHtY3MkfanwMmU0PuIT9TEXVXp7jHyl%2FKbgPpFTua0w0hAY0MayWMx2vrHH1XUOxErPzTlYkIRUvzLIHOMX6kerMD%2BCeOO%2BCbuE8Ma05jYj40n%2FsXFg9KjDQnl9xOV%2Fi%2BNt%2FY8Rv6AdrulSffXYS%2BGsdzhXfqsdJRnuL6%2Bx0RLa5MFb0%2FE3LEXBezZREWY0mhPLSqWymFqhJHkR0E3cjt6EnxKkHAE8YW1M%2F7%2FuSXtj5TeHnT1E%2FByZSBgSrAYsv7m%2BRXtnaBJYC30vafg5Zj7kRVnR%2BUrhzdtRziAxWR%2B40bxaYaRNGPX752yD4HRpWOAPYtSmrFWdiLg0pYJRvtFW%2BbWMEPMPql9rwGOqUBFkfV%2BZdguQgJw%2Fl50qaz5urK%2F4V0L9nKqxNmOcJR%2B6V1hpxhUYVwBoVo0INhqbOYBj8ghYT98cJsSVpXN5dvNkc6%2Bv01224omf5rSGy%2BORSSdb8O4%2FCIjr8ku38LFrxBJ%2FJ%2F1XzV7kh0YHzE8V3QViQhoulkCxmcwOmvtJZDwgCcDb5wu6EnUV5ExLhcudJjF4HFBjPJSAEakDrgMeNwGSDo16%2Bf&X-Amz-Signature=71273ce92273648a3b5bc227db5d88cf530cbe165ce6276e4202164a1bd43be8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3GWGOV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhp874xJkIF41bV58QutR2CZt%2FhaG9QYOEiEesqtCIbAiEAvmIleOKe8bVOn0NO%2FxEtLu2XUbrf7Nl4SFVoVKfYplcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPib8%2Bhg%2BOJRnDfdSrcA7vg1wjKa%2B9hiA3oBYLL4oriyX%2FQxNUrzlCj%2BjqXRhLUOVsHuzlUOQ8kLZQdf8cpg6LMo5OXB0cd8SeCzIURxgmtm8XWT6yWaE30Isjj%2Bych3fRxAlS6iqnokOh0qpKxIAee5T1Q0zEawb2S%2FE8C8pF%2FFCWOtXx7U4sFgE%2FE%2BEt%2F7Ic6%2BC0kG9qpXHEM54sJIQ7r0vHDH4BGcX7mun1lt2AkaUpK2zg0EMZeqQ%2FM0Ac1Vng1pv7dVsJ0r5X08Ge6nhdHuDSAV%2B3qcHq1jbIHAtFjxK0DYMMWHtY3MkfanwMmU0PuIT9TEXVXp7jHyl%2FKbgPpFTua0w0hAY0MayWMx2vrHH1XUOxErPzTlYkIRUvzLIHOMX6kerMD%2BCeOO%2BCbuE8Ma05jYj40n%2FsXFg9KjDQnl9xOV%2Fi%2BNt%2FY8Rv6AdrulSffXYS%2BGsdzhXfqsdJRnuL6%2Bx0RLa5MFb0%2FE3LEXBezZREWY0mhPLSqWymFqhJHkR0E3cjt6EnxKkHAE8YW1M%2F7%2FuSXtj5TeHnT1E%2FByZSBgSrAYsv7m%2BRXtnaBJYC30vafg5Zj7kRVnR%2BUrhzdtRziAxWR%2B40bxaYaRNGPX752yD4HRpWOAPYtSmrFWdiLg0pYJRvtFW%2BbWMEPMPql9rwGOqUBFkfV%2BZdguQgJw%2Fl50qaz5urK%2F4V0L9nKqxNmOcJR%2B6V1hpxhUYVwBoVo0INhqbOYBj8ghYT98cJsSVpXN5dvNkc6%2Bv01224omf5rSGy%2BORSSdb8O4%2FCIjr8ku38LFrxBJ%2FJ%2F1XzV7kh0YHzE8V3QViQhoulkCxmcwOmvtJZDwgCcDb5wu6EnUV5ExLhcudJjF4HFBjPJSAEakDrgMeNwGSDo16%2Bf&X-Amz-Signature=0874872e9fbc4abe77650677c2bfee000fde0efc6e47fba3dcce6c22db392c16&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3GWGOV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhp874xJkIF41bV58QutR2CZt%2FhaG9QYOEiEesqtCIbAiEAvmIleOKe8bVOn0NO%2FxEtLu2XUbrf7Nl4SFVoVKfYplcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPib8%2Bhg%2BOJRnDfdSrcA7vg1wjKa%2B9hiA3oBYLL4oriyX%2FQxNUrzlCj%2BjqXRhLUOVsHuzlUOQ8kLZQdf8cpg6LMo5OXB0cd8SeCzIURxgmtm8XWT6yWaE30Isjj%2Bych3fRxAlS6iqnokOh0qpKxIAee5T1Q0zEawb2S%2FE8C8pF%2FFCWOtXx7U4sFgE%2FE%2BEt%2F7Ic6%2BC0kG9qpXHEM54sJIQ7r0vHDH4BGcX7mun1lt2AkaUpK2zg0EMZeqQ%2FM0Ac1Vng1pv7dVsJ0r5X08Ge6nhdHuDSAV%2B3qcHq1jbIHAtFjxK0DYMMWHtY3MkfanwMmU0PuIT9TEXVXp7jHyl%2FKbgPpFTua0w0hAY0MayWMx2vrHH1XUOxErPzTlYkIRUvzLIHOMX6kerMD%2BCeOO%2BCbuE8Ma05jYj40n%2FsXFg9KjDQnl9xOV%2Fi%2BNt%2FY8Rv6AdrulSffXYS%2BGsdzhXfqsdJRnuL6%2Bx0RLa5MFb0%2FE3LEXBezZREWY0mhPLSqWymFqhJHkR0E3cjt6EnxKkHAE8YW1M%2F7%2FuSXtj5TeHnT1E%2FByZSBgSrAYsv7m%2BRXtnaBJYC30vafg5Zj7kRVnR%2BUrhzdtRziAxWR%2B40bxaYaRNGPX752yD4HRpWOAPYtSmrFWdiLg0pYJRvtFW%2BbWMEPMPql9rwGOqUBFkfV%2BZdguQgJw%2Fl50qaz5urK%2F4V0L9nKqxNmOcJR%2B6V1hpxhUYVwBoVo0INhqbOYBj8ghYT98cJsSVpXN5dvNkc6%2Bv01224omf5rSGy%2BORSSdb8O4%2FCIjr8ku38LFrxBJ%2FJ%2F1XzV7kh0YHzE8V3QViQhoulkCxmcwOmvtJZDwgCcDb5wu6EnUV5ExLhcudJjF4HFBjPJSAEakDrgMeNwGSDo16%2Bf&X-Amz-Signature=e698120634258903bc60faaa2f215b8da1bc62dc63e8fda3e72816da837c416a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3GWGOV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhp874xJkIF41bV58QutR2CZt%2FhaG9QYOEiEesqtCIbAiEAvmIleOKe8bVOn0NO%2FxEtLu2XUbrf7Nl4SFVoVKfYplcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPib8%2Bhg%2BOJRnDfdSrcA7vg1wjKa%2B9hiA3oBYLL4oriyX%2FQxNUrzlCj%2BjqXRhLUOVsHuzlUOQ8kLZQdf8cpg6LMo5OXB0cd8SeCzIURxgmtm8XWT6yWaE30Isjj%2Bych3fRxAlS6iqnokOh0qpKxIAee5T1Q0zEawb2S%2FE8C8pF%2FFCWOtXx7U4sFgE%2FE%2BEt%2F7Ic6%2BC0kG9qpXHEM54sJIQ7r0vHDH4BGcX7mun1lt2AkaUpK2zg0EMZeqQ%2FM0Ac1Vng1pv7dVsJ0r5X08Ge6nhdHuDSAV%2B3qcHq1jbIHAtFjxK0DYMMWHtY3MkfanwMmU0PuIT9TEXVXp7jHyl%2FKbgPpFTua0w0hAY0MayWMx2vrHH1XUOxErPzTlYkIRUvzLIHOMX6kerMD%2BCeOO%2BCbuE8Ma05jYj40n%2FsXFg9KjDQnl9xOV%2Fi%2BNt%2FY8Rv6AdrulSffXYS%2BGsdzhXfqsdJRnuL6%2Bx0RLa5MFb0%2FE3LEXBezZREWY0mhPLSqWymFqhJHkR0E3cjt6EnxKkHAE8YW1M%2F7%2FuSXtj5TeHnT1E%2FByZSBgSrAYsv7m%2BRXtnaBJYC30vafg5Zj7kRVnR%2BUrhzdtRziAxWR%2B40bxaYaRNGPX752yD4HRpWOAPYtSmrFWdiLg0pYJRvtFW%2BbWMEPMPql9rwGOqUBFkfV%2BZdguQgJw%2Fl50qaz5urK%2F4V0L9nKqxNmOcJR%2B6V1hpxhUYVwBoVo0INhqbOYBj8ghYT98cJsSVpXN5dvNkc6%2Bv01224omf5rSGy%2BORSSdb8O4%2FCIjr8ku38LFrxBJ%2FJ%2F1XzV7kh0YHzE8V3QViQhoulkCxmcwOmvtJZDwgCcDb5wu6EnUV5ExLhcudJjF4HFBjPJSAEakDrgMeNwGSDo16%2Bf&X-Amz-Signature=4c20e45513a12a66671cdb79f09a2bc42fb5ae873fb34672500663096712019a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3GWGOV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhp874xJkIF41bV58QutR2CZt%2FhaG9QYOEiEesqtCIbAiEAvmIleOKe8bVOn0NO%2FxEtLu2XUbrf7Nl4SFVoVKfYplcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPib8%2Bhg%2BOJRnDfdSrcA7vg1wjKa%2B9hiA3oBYLL4oriyX%2FQxNUrzlCj%2BjqXRhLUOVsHuzlUOQ8kLZQdf8cpg6LMo5OXB0cd8SeCzIURxgmtm8XWT6yWaE30Isjj%2Bych3fRxAlS6iqnokOh0qpKxIAee5T1Q0zEawb2S%2FE8C8pF%2FFCWOtXx7U4sFgE%2FE%2BEt%2F7Ic6%2BC0kG9qpXHEM54sJIQ7r0vHDH4BGcX7mun1lt2AkaUpK2zg0EMZeqQ%2FM0Ac1Vng1pv7dVsJ0r5X08Ge6nhdHuDSAV%2B3qcHq1jbIHAtFjxK0DYMMWHtY3MkfanwMmU0PuIT9TEXVXp7jHyl%2FKbgPpFTua0w0hAY0MayWMx2vrHH1XUOxErPzTlYkIRUvzLIHOMX6kerMD%2BCeOO%2BCbuE8Ma05jYj40n%2FsXFg9KjDQnl9xOV%2Fi%2BNt%2FY8Rv6AdrulSffXYS%2BGsdzhXfqsdJRnuL6%2Bx0RLa5MFb0%2FE3LEXBezZREWY0mhPLSqWymFqhJHkR0E3cjt6EnxKkHAE8YW1M%2F7%2FuSXtj5TeHnT1E%2FByZSBgSrAYsv7m%2BRXtnaBJYC30vafg5Zj7kRVnR%2BUrhzdtRziAxWR%2B40bxaYaRNGPX752yD4HRpWOAPYtSmrFWdiLg0pYJRvtFW%2BbWMEPMPql9rwGOqUBFkfV%2BZdguQgJw%2Fl50qaz5urK%2F4V0L9nKqxNmOcJR%2B6V1hpxhUYVwBoVo0INhqbOYBj8ghYT98cJsSVpXN5dvNkc6%2Bv01224omf5rSGy%2BORSSdb8O4%2FCIjr8ku38LFrxBJ%2FJ%2F1XzV7kh0YHzE8V3QViQhoulkCxmcwOmvtJZDwgCcDb5wu6EnUV5ExLhcudJjF4HFBjPJSAEakDrgMeNwGSDo16%2Bf&X-Amz-Signature=50fc4e69681aca16c5af520459fb460603a13be3436f76ff83a742aea5ff488c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3GWGOV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhp874xJkIF41bV58QutR2CZt%2FhaG9QYOEiEesqtCIbAiEAvmIleOKe8bVOn0NO%2FxEtLu2XUbrf7Nl4SFVoVKfYplcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPib8%2Bhg%2BOJRnDfdSrcA7vg1wjKa%2B9hiA3oBYLL4oriyX%2FQxNUrzlCj%2BjqXRhLUOVsHuzlUOQ8kLZQdf8cpg6LMo5OXB0cd8SeCzIURxgmtm8XWT6yWaE30Isjj%2Bych3fRxAlS6iqnokOh0qpKxIAee5T1Q0zEawb2S%2FE8C8pF%2FFCWOtXx7U4sFgE%2FE%2BEt%2F7Ic6%2BC0kG9qpXHEM54sJIQ7r0vHDH4BGcX7mun1lt2AkaUpK2zg0EMZeqQ%2FM0Ac1Vng1pv7dVsJ0r5X08Ge6nhdHuDSAV%2B3qcHq1jbIHAtFjxK0DYMMWHtY3MkfanwMmU0PuIT9TEXVXp7jHyl%2FKbgPpFTua0w0hAY0MayWMx2vrHH1XUOxErPzTlYkIRUvzLIHOMX6kerMD%2BCeOO%2BCbuE8Ma05jYj40n%2FsXFg9KjDQnl9xOV%2Fi%2BNt%2FY8Rv6AdrulSffXYS%2BGsdzhXfqsdJRnuL6%2Bx0RLa5MFb0%2FE3LEXBezZREWY0mhPLSqWymFqhJHkR0E3cjt6EnxKkHAE8YW1M%2F7%2FuSXtj5TeHnT1E%2FByZSBgSrAYsv7m%2BRXtnaBJYC30vafg5Zj7kRVnR%2BUrhzdtRziAxWR%2B40bxaYaRNGPX752yD4HRpWOAPYtSmrFWdiLg0pYJRvtFW%2BbWMEPMPql9rwGOqUBFkfV%2BZdguQgJw%2Fl50qaz5urK%2F4V0L9nKqxNmOcJR%2B6V1hpxhUYVwBoVo0INhqbOYBj8ghYT98cJsSVpXN5dvNkc6%2Bv01224omf5rSGy%2BORSSdb8O4%2FCIjr8ku38LFrxBJ%2FJ%2F1XzV7kh0YHzE8V3QViQhoulkCxmcwOmvtJZDwgCcDb5wu6EnUV5ExLhcudJjF4HFBjPJSAEakDrgMeNwGSDo16%2Bf&X-Amz-Signature=9e675feb11b3f8dce4cfa8e959aa015f368ab69c93d70c6e1e8950a9eca8e84d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF2RT7BF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDiU5Ht5TTXzhiCTGJHz6A8YoneNWM1BWAoBaLENETVCAiAvzvvMvXoYdjjrIQBAViOYtBgsAA0qnmcJOIkrcWtAASqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFU3sKNQlm5d9BC4MKtwDA6VD6sgURdiJvx%2BwgxY%2FMk1ZWNHNVJ51tgRdN%2Ftg5P8PTWFb1WVMMRSIjfDVx7TTmfF4wi8nw69W1SegPL%2B43xf%2FG1D%2FQy6CgUVCwHBBqfko%2Fw7b4c9Y7lgpYUzpd1ryf5hD2A6rNHgYwNng7EpkGAfjj9uXbMd9Paw44IaU2lf9xCkgolt8GZ9lUQCrvcSjhsogcnI6JnxoDp3OFxUyqAvGw3Ip%2Be84WMNcByT0CUNsBpzYhUcrLfWe8CNzFzJc7wq2T9Y91PJicGWLxkZFQRZ5w6qmhaoAzzoFBP8I9qtgbGvlOpHiMYCXwwkxhlnD9PDh5sI2LhFAdRiIFs%2F0b0UEHxGCZO9iux3UVipMchn4zVPIjk8KL9yPlBjRniBngWdyBqZSGB6spHi2Rucau%2B7NhVGrJI2PnXYx0UMczTcJ2aO%2B8tZQ1U9OTv6lcH1OEyqgQHeK%2BlT0q4fQheMunMATi3h2N7GLKOtDqKnR3ymLALgWDp9UP%2B6Jj%2FWvxRH3J7oGDVWBBsWxHXWpBw6Xq84CIRIijfk%2BqXLCEEXe6UuxNALoPNMndFKgfWezj7CcwY9WgD82XYKwtfcX0wtOcnyp1HXS6z3f%2F%2BhieHTy7aldjNMQlXrIObpsTC8wxab2vAY6pgFUDD9AgxOKjujDt7GeG1wdU79jKv300bHVbLt9TP6oFbZI3n9czYKlgrlbpEvRkw6DmvjZkJsAhK5gOGskQcG0auQk57OJepZvvWu3n28k4L7snABX%2FrvHa0AVanNiyK8RmKide%2Bb95UuhOYuDcnWDZh2pXKnK5N2VpNTcYNpoZtcRiKoM9k%2BtgjM1yv%2F0Wxv0ISQ0ijEdfMrBVyjI7hZEywUsItFW&X-Amz-Signature=c9a6ef7b0bd759ca3ea79206779b10ef02a1416fa0cb9aec604405abdbaf0020&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOFFTZX7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC49tU9VeKFktE2d0weo%2B1pI1IVeM18HgILYhmgKzaiDAiBSVKXv%2FBlWIZUlsoZXM44%2Fgo%2BF6Q%2BTqOuRuCdoi1PpTSqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM94XhJETk%2BF4jAJggKtwDneSwkXpRhAheURwj%2Bw1f6oV7FLx%2F1o7fOodlHg1v17AwnbtMAIy2YEl3xXtbdru9WVuy%2B8AN%2Bjy3dFrIgzkBvwKk93D6VNQ%2BGd5wpG2R5bTv%2FJypamOZSl6FHf5%2FKBJYnhpjtYsQ%2Fog7Q0%2BzyrKQruGcrc26yBcXUcbGW9q4ULCiT3ogyM4vpIR8U4yyGXjljyAimSgzMFLx5D%2FygzsWF5nSgeAr4ViSRK7RmaO1L4rOUG8YMPoY5C8UXXsZcOBqbOGoSbyARgsuxaKOJxoZQ68MLlAksVFgpGRElfsH4i4ZxIylCjjElVK1Z6fAXNLC1G5CM3lTdcsApaRp02%2B8aOfYuptDGB9PLM%2FoQuVzSQwePBfM9%2BPhyjGRsvFrCFcuBdhp0I4CdOvTYg2raobsQTbfwb%2BdSiQq%2FR5O030syYXxMzxaOVN49QwWUgrAEm%2BMfvpLfG53oBqb2NNZunyD8vrdgOdt5pxgh5RAlp%2BEhAU04efHJOkC5FlFC%2BKPTJ1tUFLEPi6e5jCmV0G9wNWSviE2YVAqfMiftWzH40ZXFWZVfSTUdOIRjH28aAGSrX2y6A7gp1oWsOjN8rD45WoM7YB7zRhNLlsGIPweYK4NNAjO%2B234nWVdX211MzkwhKb2vAY6pgE0YpyGTe1rbTjCiRiBF%2FehWLAdOV06f6ut3RNbfzo0yfov%2BIPF5ZO1ZSdLVXqyhp6XKB7LclvyOuah%2Bg4eOjToqpXOTTtHWrXkhbVFzdWDdfzRCNXktgKbVzFCkXzjs7LbAy2Xdd1%2By2fRYbqm7MJALimjfV6rMg%2F86rthMv%2B8Fo6tqwv%2BUW9YPF7Y%2Fol%2BVfnkBCkkHrOSLh4B1%2FEQOgZHElkrP2nY&X-Amz-Signature=4d7d5fb862bae2739f4bf8f51a478c40fac544d6144230c2c36ce7373174b857&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3GWGOV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhp874xJkIF41bV58QutR2CZt%2FhaG9QYOEiEesqtCIbAiEAvmIleOKe8bVOn0NO%2FxEtLu2XUbrf7Nl4SFVoVKfYplcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPib8%2Bhg%2BOJRnDfdSrcA7vg1wjKa%2B9hiA3oBYLL4oriyX%2FQxNUrzlCj%2BjqXRhLUOVsHuzlUOQ8kLZQdf8cpg6LMo5OXB0cd8SeCzIURxgmtm8XWT6yWaE30Isjj%2Bych3fRxAlS6iqnokOh0qpKxIAee5T1Q0zEawb2S%2FE8C8pF%2FFCWOtXx7U4sFgE%2FE%2BEt%2F7Ic6%2BC0kG9qpXHEM54sJIQ7r0vHDH4BGcX7mun1lt2AkaUpK2zg0EMZeqQ%2FM0Ac1Vng1pv7dVsJ0r5X08Ge6nhdHuDSAV%2B3qcHq1jbIHAtFjxK0DYMMWHtY3MkfanwMmU0PuIT9TEXVXp7jHyl%2FKbgPpFTua0w0hAY0MayWMx2vrHH1XUOxErPzTlYkIRUvzLIHOMX6kerMD%2BCeOO%2BCbuE8Ma05jYj40n%2FsXFg9KjDQnl9xOV%2Fi%2BNt%2FY8Rv6AdrulSffXYS%2BGsdzhXfqsdJRnuL6%2Bx0RLa5MFb0%2FE3LEXBezZREWY0mhPLSqWymFqhJHkR0E3cjt6EnxKkHAE8YW1M%2F7%2FuSXtj5TeHnT1E%2FByZSBgSrAYsv7m%2BRXtnaBJYC30vafg5Zj7kRVnR%2BUrhzdtRziAxWR%2B40bxaYaRNGPX752yD4HRpWOAPYtSmrFWdiLg0pYJRvtFW%2BbWMEPMPql9rwGOqUBFkfV%2BZdguQgJw%2Fl50qaz5urK%2F4V0L9nKqxNmOcJR%2B6V1hpxhUYVwBoVo0INhqbOYBj8ghYT98cJsSVpXN5dvNkc6%2Bv01224omf5rSGy%2BORSSdb8O4%2FCIjr8ku38LFrxBJ%2FJ%2F1XzV7kh0YHzE8V3QViQhoulkCxmcwOmvtJZDwgCcDb5wu6EnUV5ExLhcudJjF4HFBjPJSAEakDrgMeNwGSDo16%2Bf&X-Amz-Signature=184abbc44cabe2325f71da8c73453ff383a90108f4b5c7c5fd3f2b60c0eecbc2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3GWGOV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhp874xJkIF41bV58QutR2CZt%2FhaG9QYOEiEesqtCIbAiEAvmIleOKe8bVOn0NO%2FxEtLu2XUbrf7Nl4SFVoVKfYplcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPib8%2Bhg%2BOJRnDfdSrcA7vg1wjKa%2B9hiA3oBYLL4oriyX%2FQxNUrzlCj%2BjqXRhLUOVsHuzlUOQ8kLZQdf8cpg6LMo5OXB0cd8SeCzIURxgmtm8XWT6yWaE30Isjj%2Bych3fRxAlS6iqnokOh0qpKxIAee5T1Q0zEawb2S%2FE8C8pF%2FFCWOtXx7U4sFgE%2FE%2BEt%2F7Ic6%2BC0kG9qpXHEM54sJIQ7r0vHDH4BGcX7mun1lt2AkaUpK2zg0EMZeqQ%2FM0Ac1Vng1pv7dVsJ0r5X08Ge6nhdHuDSAV%2B3qcHq1jbIHAtFjxK0DYMMWHtY3MkfanwMmU0PuIT9TEXVXp7jHyl%2FKbgPpFTua0w0hAY0MayWMx2vrHH1XUOxErPzTlYkIRUvzLIHOMX6kerMD%2BCeOO%2BCbuE8Ma05jYj40n%2FsXFg9KjDQnl9xOV%2Fi%2BNt%2FY8Rv6AdrulSffXYS%2BGsdzhXfqsdJRnuL6%2Bx0RLa5MFb0%2FE3LEXBezZREWY0mhPLSqWymFqhJHkR0E3cjt6EnxKkHAE8YW1M%2F7%2FuSXtj5TeHnT1E%2FByZSBgSrAYsv7m%2BRXtnaBJYC30vafg5Zj7kRVnR%2BUrhzdtRziAxWR%2B40bxaYaRNGPX752yD4HRpWOAPYtSmrFWdiLg0pYJRvtFW%2BbWMEPMPql9rwGOqUBFkfV%2BZdguQgJw%2Fl50qaz5urK%2F4V0L9nKqxNmOcJR%2B6V1hpxhUYVwBoVo0INhqbOYBj8ghYT98cJsSVpXN5dvNkc6%2Bv01224omf5rSGy%2BORSSdb8O4%2FCIjr8ku38LFrxBJ%2FJ%2F1XzV7kh0YHzE8V3QViQhoulkCxmcwOmvtJZDwgCcDb5wu6EnUV5ExLhcudJjF4HFBjPJSAEakDrgMeNwGSDo16%2Bf&X-Amz-Signature=96284325bece5efd0282447a98f40f545cc0664ee68d9088853e1a956721f864&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3GWGOV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhp874xJkIF41bV58QutR2CZt%2FhaG9QYOEiEesqtCIbAiEAvmIleOKe8bVOn0NO%2FxEtLu2XUbrf7Nl4SFVoVKfYplcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPib8%2Bhg%2BOJRnDfdSrcA7vg1wjKa%2B9hiA3oBYLL4oriyX%2FQxNUrzlCj%2BjqXRhLUOVsHuzlUOQ8kLZQdf8cpg6LMo5OXB0cd8SeCzIURxgmtm8XWT6yWaE30Isjj%2Bych3fRxAlS6iqnokOh0qpKxIAee5T1Q0zEawb2S%2FE8C8pF%2FFCWOtXx7U4sFgE%2FE%2BEt%2F7Ic6%2BC0kG9qpXHEM54sJIQ7r0vHDH4BGcX7mun1lt2AkaUpK2zg0EMZeqQ%2FM0Ac1Vng1pv7dVsJ0r5X08Ge6nhdHuDSAV%2B3qcHq1jbIHAtFjxK0DYMMWHtY3MkfanwMmU0PuIT9TEXVXp7jHyl%2FKbgPpFTua0w0hAY0MayWMx2vrHH1XUOxErPzTlYkIRUvzLIHOMX6kerMD%2BCeOO%2BCbuE8Ma05jYj40n%2FsXFg9KjDQnl9xOV%2Fi%2BNt%2FY8Rv6AdrulSffXYS%2BGsdzhXfqsdJRnuL6%2Bx0RLa5MFb0%2FE3LEXBezZREWY0mhPLSqWymFqhJHkR0E3cjt6EnxKkHAE8YW1M%2F7%2FuSXtj5TeHnT1E%2FByZSBgSrAYsv7m%2BRXtnaBJYC30vafg5Zj7kRVnR%2BUrhzdtRziAxWR%2B40bxaYaRNGPX752yD4HRpWOAPYtSmrFWdiLg0pYJRvtFW%2BbWMEPMPql9rwGOqUBFkfV%2BZdguQgJw%2Fl50qaz5urK%2F4V0L9nKqxNmOcJR%2B6V1hpxhUYVwBoVo0INhqbOYBj8ghYT98cJsSVpXN5dvNkc6%2Bv01224omf5rSGy%2BORSSdb8O4%2FCIjr8ku38LFrxBJ%2FJ%2F1XzV7kh0YHzE8V3QViQhoulkCxmcwOmvtJZDwgCcDb5wu6EnUV5ExLhcudJjF4HFBjPJSAEakDrgMeNwGSDo16%2Bf&X-Amz-Signature=174863346d1f30720cbf186d346ad1be088df0466ae1c5ef7952242f37461a2d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HMLNHW3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6AXskCypyfmG5mtZbRrTRe8fhK92ozpggNJADJXmI6QIhAL9W5gPa9SKA2oDvi0sxs2yX5j7mLiRPUexrw4jDAR98KogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx3AYvrJ3tzDQZ5BNwq3AMMZOuu4RlZGBqBZ89KARLXGQQXthyw0dpApHL43e3uXQxxCTY34UmCYRHF%2B5hKppIxpIsKOfvRkTjw5h04w%2Bm7FXvzI5S2mPuakcKrhnaHJMrnvAfo%2BwYRbHaZlkcx3h6CAzY2xpaEQGz4ebYSCdDnZ7%2Bhen2FFAnHvGZ99XBOclUcWLPAH2eCcNRl%2FUxcLKwDna4DWx%2FIOC7BplacDKSle3DHhU0wKtrqMlHil5TMj2HLbV4Ab0kpOL2QGZE%2FuPpPTuwdaFUivzYv6t1EEMasJeA%2Fy9v31VbIRA5Nc1w1QJLzx2r%2FsvxmrbRdJ29TyvUqEr5OvvAHvR6w%2BfpBm4PthXqG5wEffs%2FOTr6cIPBSLXrz73eAR5oxyXwQlAVw47UTsKFy8l%2B9ndtFMM84HazCkOJh7GmJ6jzT6MSjghpJ6Bo9rjM%2B3vyMivTT431z8KOLOWWxO8s2O3WgopZs5%2B%2FbJpyJxRDS2qPvjXq%2BPhMxP27AXjWrR2vX5ZU%2FRJqildg7%2BySQ2dyuEThBOARs8at7KsV7G9x5DrwKq1HhdzSMGXgiLpnXtOu3GRk02QodE7cgpsQTjMueboKO1fYLSPetRl7ND9W21Z0%2B%2F%2F4ZpbxZ9GhLnWP8xzGM9KgAMTDupfa8BjqkAUafmV3BdKllc12c79mflY9zMNQaSXZH4UiZSJsYGsFw0KRV%2FVT4GL4El2LxMG506InonST9wbZiGxn%2BIkFthz%2FdvGHPUBsnTqZdPOnYuqDVv4ffhB%2BF%2BRm43j6QvVlOK6qeGWBz%2F1y7K%2Btm9HTeWSiuMmmESVMWozRp%2ByzUW5AN0ZY8vjSlPTihwnJ2fhJAMXwzmmwyz8CEmhJTaZY0n3zdToZA&X-Amz-Signature=42a5085115aab514ce075f6b8ea958960572f469c63b91214aa947bf2e89a63e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U54G4ZPK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5r%2Bv0D7QXUC0IN3IuL4YWc752ao9gLmrXRCvCQhkCxwIhAIKFUNtJqj7n%2FbXxB0r%2B%2F4hIjJd3rI3S0RhItxHHtg1mKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHYL7qh6Xr1dzjmysq3AP4r3t2B1ampdxZCDcT%2Bcf5v6JB9SRcZ%2F2zadyaA4qcbXsc6fWr8%2BD3Ff%2FUtQcw25OL8jNmyxxYHthuPOcVE%2BLxa2zXWa4U7jOCtjsXZSwGsTnJh6Ry12gCfDH%2BTr2BAw33H6375CJvLdngGwiZG2Hdn0guf3una882HyFCrGDtekBqLpLX9aqhoHQ9tdhkbHpEH5hioBjx2bpQf0d3iog7DHsnnq5Iyu%2FCqPu4enhGcVWoP13U0r%2BbpQgDD2ZmGCYeagtPY%2Bb%2FxY2v3mcuVEQ4bh59plELvI4XeZFVcgoe28B4maYbyXesoaMgk1MPDUvh8OxYAZFFk53x6d2s5kRPZ8Wso%2B8nsVvc7gKI3x6M66x0zY4Dzrw6FvrGqM5RlnkS7zrMNqDIca85CeQHDsXEqOgNM16GqWZLPo5aqrd3vFrozaEY2bXSsmDj7xjMXmxRC1HJl8ql%2BRTdfDq2CwhiljEPFJBnBN4LKjqoGd1pnOrouNMVgSvi9G%2BiRRFmA%2FHRb4xAWQXujt7Pmivq6MGNlPba9zxzpdBC63hQ12YMlRcuN5FqJTCLEotfIUKONiR1tMLOBauDd21Y6GmT0ld8475UHhmAEJPGflyQ36PSus5KLsoBDnwXoaA%2BkDDgpfa8BjqkAS5CFLplgeVc0AEnEBdFTPW53BerTP3cPOjfe7y%2Bbejant7A4OxyvGjrKOtIqA4QiEfIKAstHVX7fHQ80AUwv7uPycuukxtJP0kQH%2BxsQAjXCIwf4LYgS%2FjRW4NNJUpkwQxK3YHhotUqvNPABwEs1ixcCMdUK26tvryCFfeX%2Fy4TsIPEclqVDf8Hnt0G%2FR%2FT38R8VYMc%2FjgG%2Bx3TJQxEwukqns6B&X-Amz-Signature=8bbb3160189b27213327d7de86cab6333a448eb9e429e3f7cf0bc44f05bc7c80&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JYPB35J%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwZhrs8WXwDcl29jejkIoh4d4jQKzobHfz8vOX1U3AVgIhAN7FUpX2aJQe5tnv1XMpp29aZmPdDwAKXIfv6WHOm2W6KogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFMFefX8opfKQniesq3AO%2BM%2BWYxiZg%2BFpNBu7cTYK2ccFzTtRHGkWxA840%2BMZ6MKE4f3EwI2fO20iQIowXVq4y4BMhHwC8%2B6xnClbNvBAhKlCiFjVbbBTz5Cnv5JFh6Uak82UmPgUfMv0esdvNuVlxIBIldfZ009DogyX6uGILsHZVWSEn2eBhWWTKDdhIQ9RMOVvb1QFfUAroUUJJmzgpViIDasVgHWdx8dCVikOnI%2FvnzqCaL6M1rrdtTzvb1kCc6sJUuBIvRrBW37q1eCnc5ikTY%2BvOUuJLpM0CGdQooGOfE9ZQrZQPCS7R3MOKZazaWTF85uk8mdxO7%2BWTbej4n00Wh41DCHfy3jmjPk3s0v8OrbgD4z%2F2kFZP0tRjb%2F7ZEiyetIjQb7nYzOodmVX5rBhqh6H0od3xNokVZUEIOeJQHGkl2%2BtxhlA%2BJuqAXhAYTOsoX5rKsDgTz324YjbEJr4m0zjVlCYeI8pzMAgt0Xix1xsV8KsYajHOrXw1t8ErkvUiBfoIgir36Cy5zI4bCb5T3%2B9GHAUdrEGk7cJ%2FIqDuB3PBb8XYQ1sQRfpf3RkRs3AVHC%2FtHswPddCM0amw%2FC%2BZRs7xQsg9RmUr43y1X0vvzkphog8xt3tthwYiFJLgLC9iWvpMintFgzC%2Fpfa8BjqkAWoaDOp1NmQVDoSTQUPmpL2ed7UtZWwtzjzgm2KgyVqcRz%2Bj2TNUysaSxuMELYZtD%2FYHKkNZli6x2OhuITln8U7dbEVlsX5p2SwDBp1r6p%2FG0%2BdfS5w0qxxw1RQs5I4PpmhatGUqVzXrOXECXgx6FxxI1GNIWDT%2B6Pn9c%2FCmDbgkzncyVKFDu8wkWLF538Um0s5tKnoISRtRROpAFeCmoErAlRbQ&X-Amz-Signature=5fe143a456df47420bb84fcc046db6c0dec995993343f48933a8723d71175a06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZDDLFDB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI0UIABfEf4a86vwqzinUtQxUFKyVub%2B3qdX8mtQ9agQIhAKgyk%2B5bMAFmDi6hxVjVJiljVDSvjMFBln8oUXLRi6MUKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxqdTdYSv2J819e2Ugq3AObRyXYYLKaUAGas3TzJryH4htUXpjwf%2FptwCmAncIqBZvqscTX3pwkIqqOhwYOQ54Y13fdwFJD%2FoFxCnYjK8Gvd%2FMESqL%2Btm8NZNDEhrUMGDc%2BDv1cgqkYjB5NQ0waJN6im9cIv0hIfgSPZdPQSEVidNqIA4YtY9XyA6dWxkQIjo8RpTpaOJ51bOQOu21yLiYwgGy1vyp4kQp9x6qwr4GczHDUslJ7o5gRqbwsKvFWpGhJW8iQU%2FqRrfkL9wEvKjonPtZQ%2Fb5T63zNni3qJ0Ln6qXCSNoTcBvkMQYb3Jw8gf%2BxQs%2BNQQun9urJ%2BZzvT1BYntrxV0FNO%2BKIBsXu1399%2BSbmezs%2FOJRB%2F7qPCasLImbdSDMs%2BN8PyCoyBtuj00eWOrYWjQm0E1AVeEERQww0d1nvKhqDQjp9iRaQG8sziHLCxXLOVn0JW%2Bq3Ik1Qz7ozxmUJm7YvYjsJK8qYIDUWrkJ0R1FChR7pd5VrV3I3uDbkmE6L5R766vOjO5zQuJeJFTA4CCPmkZoQeaioDwVv5CzzLY25HqXTdR75FEyXr0tIaKQnjio%2FdAsuthQBFp69wnI%2F02wdTFtuK8rlM0gU%2FfnEpt95vZxMPippjq2sOndM6EwohYaNl5kTVzCTpva8BjqkAYWUFndgocm%2F9JlnOp%2BvLuTKgfXg%2Bciglp%2F%2FTA%2FPwatll7By5bJZYWmrxGCkCXUXcD5V8wGWiy0HYZ%2FMuAmApUF%2BoFUDa%2F1WY9C3%2BwuOOPlvVBMEO9NOZz0UhAOuvlotXFFA5gXOmPoR6zqpeYrNs7kM9p7GEWNoru1lLBSPiWzOl3xKmN%2Fy%2F1Is3xyeKDqtoUpyxFIdkAwlxfI%2FF%2BedIbSrcpkg&X-Amz-Signature=582835dd3effa50ed89edaaae03c0b9b4047ac81ceb46c37fbd023a4775edf4a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZDDLFDB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI0UIABfEf4a86vwqzinUtQxUFKyVub%2B3qdX8mtQ9agQIhAKgyk%2B5bMAFmDi6hxVjVJiljVDSvjMFBln8oUXLRi6MUKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxqdTdYSv2J819e2Ugq3AObRyXYYLKaUAGas3TzJryH4htUXpjwf%2FptwCmAncIqBZvqscTX3pwkIqqOhwYOQ54Y13fdwFJD%2FoFxCnYjK8Gvd%2FMESqL%2Btm8NZNDEhrUMGDc%2BDv1cgqkYjB5NQ0waJN6im9cIv0hIfgSPZdPQSEVidNqIA4YtY9XyA6dWxkQIjo8RpTpaOJ51bOQOu21yLiYwgGy1vyp4kQp9x6qwr4GczHDUslJ7o5gRqbwsKvFWpGhJW8iQU%2FqRrfkL9wEvKjonPtZQ%2Fb5T63zNni3qJ0Ln6qXCSNoTcBvkMQYb3Jw8gf%2BxQs%2BNQQun9urJ%2BZzvT1BYntrxV0FNO%2BKIBsXu1399%2BSbmezs%2FOJRB%2F7qPCasLImbdSDMs%2BN8PyCoyBtuj00eWOrYWjQm0E1AVeEERQww0d1nvKhqDQjp9iRaQG8sziHLCxXLOVn0JW%2Bq3Ik1Qz7ozxmUJm7YvYjsJK8qYIDUWrkJ0R1FChR7pd5VrV3I3uDbkmE6L5R766vOjO5zQuJeJFTA4CCPmkZoQeaioDwVv5CzzLY25HqXTdR75FEyXr0tIaKQnjio%2FdAsuthQBFp69wnI%2F02wdTFtuK8rlM0gU%2FfnEpt95vZxMPippjq2sOndM6EwohYaNl5kTVzCTpva8BjqkAYWUFndgocm%2F9JlnOp%2BvLuTKgfXg%2Bciglp%2F%2FTA%2FPwatll7By5bJZYWmrxGCkCXUXcD5V8wGWiy0HYZ%2FMuAmApUF%2BoFUDa%2F1WY9C3%2BwuOOPlvVBMEO9NOZz0UhAOuvlotXFFA5gXOmPoR6zqpeYrNs7kM9p7GEWNoru1lLBSPiWzOl3xKmN%2Fy%2F1Is3xyeKDqtoUpyxFIdkAwlxfI%2FF%2BedIbSrcpkg&X-Amz-Signature=6767d364de3364d1c4507759ff3d362d8d01eaa484541d99cbb07e082f2dff31&X-Amz-SignedHeaders=host&x-id=GetObject)

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
