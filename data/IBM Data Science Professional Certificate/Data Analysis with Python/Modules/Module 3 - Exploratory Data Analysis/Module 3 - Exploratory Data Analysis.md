

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRYNXIUY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXAFnYyUve7YcqjvYq8r6mmGr9zWWRVilxWWn2l6bfiQIhAMqSLDmPzyR1%2BE7qXYCwrZwDT8WIFIGFcfPIU%2FCVbg0PKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7ZIKxD6egpf%2FKEJ4q3ANOTYC0aSvNLQV%2FHxr0RPNi15q%2FvJQT90qITMesCjK%2B0mDR8tcsH9vUAkqsB1I09eoDq%2BhfjmqTePjK47t%2FzyNUSnDp1xr0nlnez6h5qRrDDOKItPS%2FIDEei5tZCWa4vgeqg%2F441VVocrDAEGbcbtoL7DcOKHwbKhptrXoClGY7Qptiw%2FWUfBw3zKR10vqnvI0uj90lUqHcDXhKAMHw5NyHfrso9Hk4r3k%2F8%2FdJmClY3atZvK%2F80Cr1LOCh%2FI%2BZhjkJCzIpG8xFN2kZiuRlgBSZBRtFJfXoOWBsHMp9j8PqV7%2B0%2BaKubcAU7LakpA0Ik1q92Lr7a%2FhxzDAbZOONQQtgIuj4rhpV2aYdH%2BhIoD6scCxemRDjLOI8f4rMriEN0mGuYj4F%2BfmeAZcnVzSm4gxUHvalP6oSZl5TGWOAosc%2BK9IT%2FXtWPpWjvFDCYdQdgrKPN%2Bg%2FRS%2FbOf%2B3GjbP%2FC4pbYqjU8ShHZDWmhQ0hgVi0dLTGBYLewSnWPfDd6CJn6%2F8ooi1bi8PF%2BZqKkMrIaZseUzjFOLbUhnurDyjRZ5gBVDFBhtqWjQNvDcAFD4Y7DQzfJjyhoPAnB4n7RrUDDitTgaZJX9BAPqIJoR1n2wOcwZ%2F1TvSJPVsm%2F8H2DCIv4C9BjqkAcMNlJyJAey4nA%2FZHLiQf%2F3f1kx6qh6ZOHRnkOBomqrH2Cv1hGJuP37RwFPm%2Bl6oHYPQCxVRV72y2bK3Bz9uCZHPAKOyR%2BjHQlZB%2BzYsqT38eXE3nU%2BlbmFKArpKVBGNG%2F0MuyR6PgSzhwZ1LmBt%2FbaxXEX9nsSBRgvJt43YHKesU5fNBcPnILFoAvjPJzcImHQDc%2BQ1UEy1sGQgreexSkoGS5ur&X-Amz-Signature=1d2662579ff69a1237bef430a7446b42260429f20700fd22a22c46b9884b48c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRYNXIUY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXAFnYyUve7YcqjvYq8r6mmGr9zWWRVilxWWn2l6bfiQIhAMqSLDmPzyR1%2BE7qXYCwrZwDT8WIFIGFcfPIU%2FCVbg0PKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7ZIKxD6egpf%2FKEJ4q3ANOTYC0aSvNLQV%2FHxr0RPNi15q%2FvJQT90qITMesCjK%2B0mDR8tcsH9vUAkqsB1I09eoDq%2BhfjmqTePjK47t%2FzyNUSnDp1xr0nlnez6h5qRrDDOKItPS%2FIDEei5tZCWa4vgeqg%2F441VVocrDAEGbcbtoL7DcOKHwbKhptrXoClGY7Qptiw%2FWUfBw3zKR10vqnvI0uj90lUqHcDXhKAMHw5NyHfrso9Hk4r3k%2F8%2FdJmClY3atZvK%2F80Cr1LOCh%2FI%2BZhjkJCzIpG8xFN2kZiuRlgBSZBRtFJfXoOWBsHMp9j8PqV7%2B0%2BaKubcAU7LakpA0Ik1q92Lr7a%2FhxzDAbZOONQQtgIuj4rhpV2aYdH%2BhIoD6scCxemRDjLOI8f4rMriEN0mGuYj4F%2BfmeAZcnVzSm4gxUHvalP6oSZl5TGWOAosc%2BK9IT%2FXtWPpWjvFDCYdQdgrKPN%2Bg%2FRS%2FbOf%2B3GjbP%2FC4pbYqjU8ShHZDWmhQ0hgVi0dLTGBYLewSnWPfDd6CJn6%2F8ooi1bi8PF%2BZqKkMrIaZseUzjFOLbUhnurDyjRZ5gBVDFBhtqWjQNvDcAFD4Y7DQzfJjyhoPAnB4n7RrUDDitTgaZJX9BAPqIJoR1n2wOcwZ%2F1TvSJPVsm%2F8H2DCIv4C9BjqkAcMNlJyJAey4nA%2FZHLiQf%2F3f1kx6qh6ZOHRnkOBomqrH2Cv1hGJuP37RwFPm%2Bl6oHYPQCxVRV72y2bK3Bz9uCZHPAKOyR%2BjHQlZB%2BzYsqT38eXE3nU%2BlbmFKArpKVBGNG%2F0MuyR6PgSzhwZ1LmBt%2FbaxXEX9nsSBRgvJt43YHKesU5fNBcPnILFoAvjPJzcImHQDc%2BQ1UEy1sGQgreexSkoGS5ur&X-Amz-Signature=0b0ea9a3e48890217edd3e4c149f4c08381ba8a5c1c6c396b782d282eb8d697f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRYNXIUY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXAFnYyUve7YcqjvYq8r6mmGr9zWWRVilxWWn2l6bfiQIhAMqSLDmPzyR1%2BE7qXYCwrZwDT8WIFIGFcfPIU%2FCVbg0PKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7ZIKxD6egpf%2FKEJ4q3ANOTYC0aSvNLQV%2FHxr0RPNi15q%2FvJQT90qITMesCjK%2B0mDR8tcsH9vUAkqsB1I09eoDq%2BhfjmqTePjK47t%2FzyNUSnDp1xr0nlnez6h5qRrDDOKItPS%2FIDEei5tZCWa4vgeqg%2F441VVocrDAEGbcbtoL7DcOKHwbKhptrXoClGY7Qptiw%2FWUfBw3zKR10vqnvI0uj90lUqHcDXhKAMHw5NyHfrso9Hk4r3k%2F8%2FdJmClY3atZvK%2F80Cr1LOCh%2FI%2BZhjkJCzIpG8xFN2kZiuRlgBSZBRtFJfXoOWBsHMp9j8PqV7%2B0%2BaKubcAU7LakpA0Ik1q92Lr7a%2FhxzDAbZOONQQtgIuj4rhpV2aYdH%2BhIoD6scCxemRDjLOI8f4rMriEN0mGuYj4F%2BfmeAZcnVzSm4gxUHvalP6oSZl5TGWOAosc%2BK9IT%2FXtWPpWjvFDCYdQdgrKPN%2Bg%2FRS%2FbOf%2B3GjbP%2FC4pbYqjU8ShHZDWmhQ0hgVi0dLTGBYLewSnWPfDd6CJn6%2F8ooi1bi8PF%2BZqKkMrIaZseUzjFOLbUhnurDyjRZ5gBVDFBhtqWjQNvDcAFD4Y7DQzfJjyhoPAnB4n7RrUDDitTgaZJX9BAPqIJoR1n2wOcwZ%2F1TvSJPVsm%2F8H2DCIv4C9BjqkAcMNlJyJAey4nA%2FZHLiQf%2F3f1kx6qh6ZOHRnkOBomqrH2Cv1hGJuP37RwFPm%2Bl6oHYPQCxVRV72y2bK3Bz9uCZHPAKOyR%2BjHQlZB%2BzYsqT38eXE3nU%2BlbmFKArpKVBGNG%2F0MuyR6PgSzhwZ1LmBt%2FbaxXEX9nsSBRgvJt43YHKesU5fNBcPnILFoAvjPJzcImHQDc%2BQ1UEy1sGQgreexSkoGS5ur&X-Amz-Signature=3f861ff668671e04eae0fb27e8ac1adc40b3f2175475aa2ac2442617e5b08d9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZHXWW5S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWuDcG8wGUEn%2F7ko%2B9s1TY3uWmWpo5o%2FCgWAzvvcejIAIhAImQ4zJR2WgwvXkqtIEdKsoweFmAx8jgY%2F92oDShVyoJKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpVlEd6nKZFOH47YEq3ANRBfAjnJ%2BSdKrzTkq9i1ZiyLqtoOXOBai7zxeqvUzStNW8DMPc17RzqfRRlJDEAYFuRwofH5YpX8kEMDPDJbSkyupyeT777G%2BIxmigVuVWkkyq2ihfjnrEMIwKc6T9OIys43lHfd4pQS5%2FCBZNtE%2BVj%2BXsQpluQ1fujz7DEosq%2F5jsNQgWkXsCP%2FzN8TEtbG8fcnhiDC3hWaLBblK06j6RpjbnEIhRBWwfGDQ7mx9Z7KEBqs%2Fz%2FnQemVOxgFXo%2B5JVBjtQe4at1b%2Bnck2ajEwW1tikAjssHV%2FUGLP%2FBvbMgv%2FAwSMIYHoZmsOmP6ZPtKu2gPpnqCtXr37Q9fvW7e%2FmJBKYC%2Fc2C1I6bBfrB6hz5DAmzDTpKnJJDMc19IdaIwipQOpY0hW4R1ZSsH0JnjPa6IWKJuEeKcAdK9G9G96Rq76CZCNBVftnXG6nVdIZcEObE2tDTwnXG7cx7GcofC18yb%2BAKojISN8OyoHvtXNKH%2FYH%2Fiu4lQlakxb%2Bv6TFV3iHiQ6Anso7JC%2BdHNBB0DIeTWomdnmDmP3qebUhVmTuf%2F7oLAJsowPK7YAGW6%2BGKH%2Bfsk43hD8y5OFIKjtqKjGw6EVPjavDZYr6HbApKOZoP64OPtPXeHt2kGbLsDDfwIC9BjqkAXQk02dkVOySAHdfkSSbKlm01sHGWlT%2BUvRNtAifgMCt7xakBYlkNRG4KbYwWNN6%2BET%2F50FwEkfrSOQmY5qx0t1jGBaRxWJVm6rU5wIOBu%2F4bmnWM2%2FqfIr5Ph7wRKbZ%2FQOXMHHz6c0upAbhrJA8kJ4SsFa4ml1WzC18qDmbfJflGJjYRBeGSv5vKWd8Qk%2F6M7A6ouKkZMRJXRBEtHeor5KONvDS&X-Amz-Signature=1b569b389c6fd09942792027f018167d3d2a1f63c339fd11a65a9c195ac314eb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZHXWW5S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWuDcG8wGUEn%2F7ko%2B9s1TY3uWmWpo5o%2FCgWAzvvcejIAIhAImQ4zJR2WgwvXkqtIEdKsoweFmAx8jgY%2F92oDShVyoJKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpVlEd6nKZFOH47YEq3ANRBfAjnJ%2BSdKrzTkq9i1ZiyLqtoOXOBai7zxeqvUzStNW8DMPc17RzqfRRlJDEAYFuRwofH5YpX8kEMDPDJbSkyupyeT777G%2BIxmigVuVWkkyq2ihfjnrEMIwKc6T9OIys43lHfd4pQS5%2FCBZNtE%2BVj%2BXsQpluQ1fujz7DEosq%2F5jsNQgWkXsCP%2FzN8TEtbG8fcnhiDC3hWaLBblK06j6RpjbnEIhRBWwfGDQ7mx9Z7KEBqs%2Fz%2FnQemVOxgFXo%2B5JVBjtQe4at1b%2Bnck2ajEwW1tikAjssHV%2FUGLP%2FBvbMgv%2FAwSMIYHoZmsOmP6ZPtKu2gPpnqCtXr37Q9fvW7e%2FmJBKYC%2Fc2C1I6bBfrB6hz5DAmzDTpKnJJDMc19IdaIwipQOpY0hW4R1ZSsH0JnjPa6IWKJuEeKcAdK9G9G96Rq76CZCNBVftnXG6nVdIZcEObE2tDTwnXG7cx7GcofC18yb%2BAKojISN8OyoHvtXNKH%2FYH%2Fiu4lQlakxb%2Bv6TFV3iHiQ6Anso7JC%2BdHNBB0DIeTWomdnmDmP3qebUhVmTuf%2F7oLAJsowPK7YAGW6%2BGKH%2Bfsk43hD8y5OFIKjtqKjGw6EVPjavDZYr6HbApKOZoP64OPtPXeHt2kGbLsDDfwIC9BjqkAXQk02dkVOySAHdfkSSbKlm01sHGWlT%2BUvRNtAifgMCt7xakBYlkNRG4KbYwWNN6%2BET%2F50FwEkfrSOQmY5qx0t1jGBaRxWJVm6rU5wIOBu%2F4bmnWM2%2FqfIr5Ph7wRKbZ%2FQOXMHHz6c0upAbhrJA8kJ4SsFa4ml1WzC18qDmbfJflGJjYRBeGSv5vKWd8Qk%2F6M7A6ouKkZMRJXRBEtHeor5KONvDS&X-Amz-Signature=57a97402319fa13e9c0c6480ed8595c95e6a4cf0fe003b16ef42832d130ebdb4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZHXWW5S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWuDcG8wGUEn%2F7ko%2B9s1TY3uWmWpo5o%2FCgWAzvvcejIAIhAImQ4zJR2WgwvXkqtIEdKsoweFmAx8jgY%2F92oDShVyoJKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpVlEd6nKZFOH47YEq3ANRBfAjnJ%2BSdKrzTkq9i1ZiyLqtoOXOBai7zxeqvUzStNW8DMPc17RzqfRRlJDEAYFuRwofH5YpX8kEMDPDJbSkyupyeT777G%2BIxmigVuVWkkyq2ihfjnrEMIwKc6T9OIys43lHfd4pQS5%2FCBZNtE%2BVj%2BXsQpluQ1fujz7DEosq%2F5jsNQgWkXsCP%2FzN8TEtbG8fcnhiDC3hWaLBblK06j6RpjbnEIhRBWwfGDQ7mx9Z7KEBqs%2Fz%2FnQemVOxgFXo%2B5JVBjtQe4at1b%2Bnck2ajEwW1tikAjssHV%2FUGLP%2FBvbMgv%2FAwSMIYHoZmsOmP6ZPtKu2gPpnqCtXr37Q9fvW7e%2FmJBKYC%2Fc2C1I6bBfrB6hz5DAmzDTpKnJJDMc19IdaIwipQOpY0hW4R1ZSsH0JnjPa6IWKJuEeKcAdK9G9G96Rq76CZCNBVftnXG6nVdIZcEObE2tDTwnXG7cx7GcofC18yb%2BAKojISN8OyoHvtXNKH%2FYH%2Fiu4lQlakxb%2Bv6TFV3iHiQ6Anso7JC%2BdHNBB0DIeTWomdnmDmP3qebUhVmTuf%2F7oLAJsowPK7YAGW6%2BGKH%2Bfsk43hD8y5OFIKjtqKjGw6EVPjavDZYr6HbApKOZoP64OPtPXeHt2kGbLsDDfwIC9BjqkAXQk02dkVOySAHdfkSSbKlm01sHGWlT%2BUvRNtAifgMCt7xakBYlkNRG4KbYwWNN6%2BET%2F50FwEkfrSOQmY5qx0t1jGBaRxWJVm6rU5wIOBu%2F4bmnWM2%2FqfIr5Ph7wRKbZ%2FQOXMHHz6c0upAbhrJA8kJ4SsFa4ml1WzC18qDmbfJflGJjYRBeGSv5vKWd8Qk%2F6M7A6ouKkZMRJXRBEtHeor5KONvDS&X-Amz-Signature=45f62d95e3dbf2b5416da2f3ceb84acf15eb9fd77d2d047bfbf5255312f8a0c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZHXWW5S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWuDcG8wGUEn%2F7ko%2B9s1TY3uWmWpo5o%2FCgWAzvvcejIAIhAImQ4zJR2WgwvXkqtIEdKsoweFmAx8jgY%2F92oDShVyoJKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpVlEd6nKZFOH47YEq3ANRBfAjnJ%2BSdKrzTkq9i1ZiyLqtoOXOBai7zxeqvUzStNW8DMPc17RzqfRRlJDEAYFuRwofH5YpX8kEMDPDJbSkyupyeT777G%2BIxmigVuVWkkyq2ihfjnrEMIwKc6T9OIys43lHfd4pQS5%2FCBZNtE%2BVj%2BXsQpluQ1fujz7DEosq%2F5jsNQgWkXsCP%2FzN8TEtbG8fcnhiDC3hWaLBblK06j6RpjbnEIhRBWwfGDQ7mx9Z7KEBqs%2Fz%2FnQemVOxgFXo%2B5JVBjtQe4at1b%2Bnck2ajEwW1tikAjssHV%2FUGLP%2FBvbMgv%2FAwSMIYHoZmsOmP6ZPtKu2gPpnqCtXr37Q9fvW7e%2FmJBKYC%2Fc2C1I6bBfrB6hz5DAmzDTpKnJJDMc19IdaIwipQOpY0hW4R1ZSsH0JnjPa6IWKJuEeKcAdK9G9G96Rq76CZCNBVftnXG6nVdIZcEObE2tDTwnXG7cx7GcofC18yb%2BAKojISN8OyoHvtXNKH%2FYH%2Fiu4lQlakxb%2Bv6TFV3iHiQ6Anso7JC%2BdHNBB0DIeTWomdnmDmP3qebUhVmTuf%2F7oLAJsowPK7YAGW6%2BGKH%2Bfsk43hD8y5OFIKjtqKjGw6EVPjavDZYr6HbApKOZoP64OPtPXeHt2kGbLsDDfwIC9BjqkAXQk02dkVOySAHdfkSSbKlm01sHGWlT%2BUvRNtAifgMCt7xakBYlkNRG4KbYwWNN6%2BET%2F50FwEkfrSOQmY5qx0t1jGBaRxWJVm6rU5wIOBu%2F4bmnWM2%2FqfIr5Ph7wRKbZ%2FQOXMHHz6c0upAbhrJA8kJ4SsFa4ml1WzC18qDmbfJflGJjYRBeGSv5vKWd8Qk%2F6M7A6ouKkZMRJXRBEtHeor5KONvDS&X-Amz-Signature=e9f4d66bd137a01adafe99b4cc1c6e9630c4e6b06bfd9477e7807c9224a8bb15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZHXWW5S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWuDcG8wGUEn%2F7ko%2B9s1TY3uWmWpo5o%2FCgWAzvvcejIAIhAImQ4zJR2WgwvXkqtIEdKsoweFmAx8jgY%2F92oDShVyoJKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpVlEd6nKZFOH47YEq3ANRBfAjnJ%2BSdKrzTkq9i1ZiyLqtoOXOBai7zxeqvUzStNW8DMPc17RzqfRRlJDEAYFuRwofH5YpX8kEMDPDJbSkyupyeT777G%2BIxmigVuVWkkyq2ihfjnrEMIwKc6T9OIys43lHfd4pQS5%2FCBZNtE%2BVj%2BXsQpluQ1fujz7DEosq%2F5jsNQgWkXsCP%2FzN8TEtbG8fcnhiDC3hWaLBblK06j6RpjbnEIhRBWwfGDQ7mx9Z7KEBqs%2Fz%2FnQemVOxgFXo%2B5JVBjtQe4at1b%2Bnck2ajEwW1tikAjssHV%2FUGLP%2FBvbMgv%2FAwSMIYHoZmsOmP6ZPtKu2gPpnqCtXr37Q9fvW7e%2FmJBKYC%2Fc2C1I6bBfrB6hz5DAmzDTpKnJJDMc19IdaIwipQOpY0hW4R1ZSsH0JnjPa6IWKJuEeKcAdK9G9G96Rq76CZCNBVftnXG6nVdIZcEObE2tDTwnXG7cx7GcofC18yb%2BAKojISN8OyoHvtXNKH%2FYH%2Fiu4lQlakxb%2Bv6TFV3iHiQ6Anso7JC%2BdHNBB0DIeTWomdnmDmP3qebUhVmTuf%2F7oLAJsowPK7YAGW6%2BGKH%2Bfsk43hD8y5OFIKjtqKjGw6EVPjavDZYr6HbApKOZoP64OPtPXeHt2kGbLsDDfwIC9BjqkAXQk02dkVOySAHdfkSSbKlm01sHGWlT%2BUvRNtAifgMCt7xakBYlkNRG4KbYwWNN6%2BET%2F50FwEkfrSOQmY5qx0t1jGBaRxWJVm6rU5wIOBu%2F4bmnWM2%2FqfIr5Ph7wRKbZ%2FQOXMHHz6c0upAbhrJA8kJ4SsFa4ml1WzC18qDmbfJflGJjYRBeGSv5vKWd8Qk%2F6M7A6ouKkZMRJXRBEtHeor5KONvDS&X-Amz-Signature=ba4fd037ae511d5d90e1659786310d75e94fa137cf9d4c09c58102f061b186c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZHXWW5S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWuDcG8wGUEn%2F7ko%2B9s1TY3uWmWpo5o%2FCgWAzvvcejIAIhAImQ4zJR2WgwvXkqtIEdKsoweFmAx8jgY%2F92oDShVyoJKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpVlEd6nKZFOH47YEq3ANRBfAjnJ%2BSdKrzTkq9i1ZiyLqtoOXOBai7zxeqvUzStNW8DMPc17RzqfRRlJDEAYFuRwofH5YpX8kEMDPDJbSkyupyeT777G%2BIxmigVuVWkkyq2ihfjnrEMIwKc6T9OIys43lHfd4pQS5%2FCBZNtE%2BVj%2BXsQpluQ1fujz7DEosq%2F5jsNQgWkXsCP%2FzN8TEtbG8fcnhiDC3hWaLBblK06j6RpjbnEIhRBWwfGDQ7mx9Z7KEBqs%2Fz%2FnQemVOxgFXo%2B5JVBjtQe4at1b%2Bnck2ajEwW1tikAjssHV%2FUGLP%2FBvbMgv%2FAwSMIYHoZmsOmP6ZPtKu2gPpnqCtXr37Q9fvW7e%2FmJBKYC%2Fc2C1I6bBfrB6hz5DAmzDTpKnJJDMc19IdaIwipQOpY0hW4R1ZSsH0JnjPa6IWKJuEeKcAdK9G9G96Rq76CZCNBVftnXG6nVdIZcEObE2tDTwnXG7cx7GcofC18yb%2BAKojISN8OyoHvtXNKH%2FYH%2Fiu4lQlakxb%2Bv6TFV3iHiQ6Anso7JC%2BdHNBB0DIeTWomdnmDmP3qebUhVmTuf%2F7oLAJsowPK7YAGW6%2BGKH%2Bfsk43hD8y5OFIKjtqKjGw6EVPjavDZYr6HbApKOZoP64OPtPXeHt2kGbLsDDfwIC9BjqkAXQk02dkVOySAHdfkSSbKlm01sHGWlT%2BUvRNtAifgMCt7xakBYlkNRG4KbYwWNN6%2BET%2F50FwEkfrSOQmY5qx0t1jGBaRxWJVm6rU5wIOBu%2F4bmnWM2%2FqfIr5Ph7wRKbZ%2FQOXMHHz6c0upAbhrJA8kJ4SsFa4ml1WzC18qDmbfJflGJjYRBeGSv5vKWd8Qk%2F6M7A6ouKkZMRJXRBEtHeor5KONvDS&X-Amz-Signature=78a4bfdd0c7e7b64b289eab7004ed82d340fb8e139eaf96d9fa6167dbe4e3975&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFDDIYRD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCC0j%2BtXtiqJbvxH4Rwn54IvmQEo8l2u7CDHBtjWTPJ7wIgJySwKkktk0K2P6Bln6%2BQlnooPjkPnVFCX9N8UhQyPDYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFO74zVfEJ1oNmxrHircA1usx6GqRQMXvl82f60RLt63UfFsrdrhBA5y7LuwoD7Z9jrH7%2Bv3YE5Jiv0oF7E5%2F%2BPJfmQ8EDM3lOWg7RFYqmlFpBRIhHBpn0%2F7Ab%2B%2BsVFqnuzroBa23fsPzEKL20LdBqZhNzhNZdPt3lkyLFqAHSOUeNA4CtJRh1hhpY9Yw66JUzIL5gMq7nHKJL3Wq7GRrAVXGaP8mWZWl9cQJ3w8mcFuomBWLXmzsMOBqfvFHzMmL%2BMYPQGh7BDIVv%2FK9ymW3xkvFfvNcvtFf%2FbX4cFJgM2OtdpsmYjaT2%2BktNzEk0UhRybayhuZ%2Byv%2FE47c28oxfRgiU9QcDRxxSh4dTRycINYEyK80SJrlEcS8EAr69LD9vVz%2FyS1anyoGgSZ3IwoWsuoc2jhbLUgWYaSjhE%2F%2BJBgM3lp2azjQtjDmWg8xke%2BAegGy4FswGNt2l5L7ViEBQYdubDrOyruMbR9qjalDRNlXoWrlcYyfbwi%2BftZDmHyPL2giy9WHnvfv7soCgdhJYHlIV%2B6c0%2FX%2FRYVucbJFW35KWCmnfnXiVNOaOKb1kYalxAyxcu%2F18Lgiv%2B4cEfBEBQxwZ3JmrYK39AER4Jw67JYhS2tlgD3EBkOpJqL9xlzqWO3qdAWzGhHdncABML3AgL0GOqUB1ZJjpNu%2Fq3bfFlvI7eCnVUwPaM6suo0zc%2B84Scn30rdTi1q9LQihPw8d0uHdvP2zJSO85yYyP%2BAb5gIsqclJH8weAwrw94wbdNd4A4VbKIc6%2Bbc2qBzDWCNW1DEtlYpeUyRwuqJG%2BqUnCU1NiKsOkIwHeEXsJZh7ns%2BWsQMdkKzD%2BrxNvqPmrve2NnoXuBdRt4ekjMKmgoRmiUthQIsO%2BeJChTA9&X-Amz-Signature=335464d4764d12eff4b9e85b472f81b29699fc82d426cbcedc0a7f8c7f20c4e7&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOLVIMWT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICVI%2Bi%2BG4zB9QRLkUnhIKV4DB2X%2FeK1djMPw%2FTFgDkDfAiEAzxil%2BfUAhT5yaOngaqxS%2FBqFt%2BHMVxIGEtItp0mN6MUqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2BBERNYHJy2eSFdmCrcA6rggg3yNEGhcfEB%2BnS7ecpPjnuk7FKb6D%2FcoeNb%2FVR3%2FDHY8BEbtoEex1r4vmVkhMAbU%2BhY%2FE7h6P6h%2BxNNLS3yR26i%2F7BtxwTkD3XvZioSs00FeS8l%2Fx6PffctXHCdStC6%2FyDfdmOQRx5%2Bjzig67x4XLjVZRvbx6IIyLBsCaNkrHt8ZGXsGqWAQRVSdzk9aHf6mB%2BJd9OdEW09dvC5R%2By84lG%2F6LOnePYZVMM%2FgnaVz0zIpi2NzyhvGSQACSGsv7t2iHZaozadw7PK50GC4Zj%2FT4lsKMUZ4j%2BMFe4ce8BVcm2WUvm31u1JLG%2FSSpFJUNZ5y%2B20FS1%2F0LeV1PvaZJxE0FiTNFHweF3IcEb4sx9Lkar5MxiHGzQCE6uf8tPPAhEo%2FLZe%2BI%2Fs4xcm%2BTkJKwWVvCP6wR7JXWfOy8iTZ6uBMatNRWtdPtQ%2Fs6OOsy9VnDCFLtgvaWKrlMwj44k9d6W1MQ3TX5mC7Tt9xj2pYQkibzCeqIa%2FlNUoUSo3wzok50GCV652zOfWMDv6shTQPcGl4xRRSllyZzGZ31yGDrzK%2FMR3KELW2U9EJH%2BNVpc%2FSTjdy9DLB%2B%2BHxJ2XO2oBwZplLispRqaCxqk6VyM0njIT9aYph2onCZ7gStC3MIi%2FgL0GOqUBXVvyWpygTAPfS0A9n4vypRP76Efm0sjLJiAFbGZYXIxmXHO0B2IKg%2FcbkKVrLwVGcp2PItl%2BfvLE7M1TOPUX3xR%2BLgW1%2Bl7VJJ0f9JvVGv1sbqORc%2FDQn05L7PEtF5B5aU1029ZwDw6Sj%2BQTsusNOpXaml64hrVJDfUXoW%2BDjNdQZM6oGWeVlcqPrYBbPlMjdIgvsnrduvZh1qpgucVBxkb31vmP&X-Amz-Signature=a2035d5def54e3f3049be5828f41c9fef2c9ee8416612dfa9d7520e861751190&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZHXWW5S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWuDcG8wGUEn%2F7ko%2B9s1TY3uWmWpo5o%2FCgWAzvvcejIAIhAImQ4zJR2WgwvXkqtIEdKsoweFmAx8jgY%2F92oDShVyoJKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpVlEd6nKZFOH47YEq3ANRBfAjnJ%2BSdKrzTkq9i1ZiyLqtoOXOBai7zxeqvUzStNW8DMPc17RzqfRRlJDEAYFuRwofH5YpX8kEMDPDJbSkyupyeT777G%2BIxmigVuVWkkyq2ihfjnrEMIwKc6T9OIys43lHfd4pQS5%2FCBZNtE%2BVj%2BXsQpluQ1fujz7DEosq%2F5jsNQgWkXsCP%2FzN8TEtbG8fcnhiDC3hWaLBblK06j6RpjbnEIhRBWwfGDQ7mx9Z7KEBqs%2Fz%2FnQemVOxgFXo%2B5JVBjtQe4at1b%2Bnck2ajEwW1tikAjssHV%2FUGLP%2FBvbMgv%2FAwSMIYHoZmsOmP6ZPtKu2gPpnqCtXr37Q9fvW7e%2FmJBKYC%2Fc2C1I6bBfrB6hz5DAmzDTpKnJJDMc19IdaIwipQOpY0hW4R1ZSsH0JnjPa6IWKJuEeKcAdK9G9G96Rq76CZCNBVftnXG6nVdIZcEObE2tDTwnXG7cx7GcofC18yb%2BAKojISN8OyoHvtXNKH%2FYH%2Fiu4lQlakxb%2Bv6TFV3iHiQ6Anso7JC%2BdHNBB0DIeTWomdnmDmP3qebUhVmTuf%2F7oLAJsowPK7YAGW6%2BGKH%2Bfsk43hD8y5OFIKjtqKjGw6EVPjavDZYr6HbApKOZoP64OPtPXeHt2kGbLsDDfwIC9BjqkAXQk02dkVOySAHdfkSSbKlm01sHGWlT%2BUvRNtAifgMCt7xakBYlkNRG4KbYwWNN6%2BET%2F50FwEkfrSOQmY5qx0t1jGBaRxWJVm6rU5wIOBu%2F4bmnWM2%2FqfIr5Ph7wRKbZ%2FQOXMHHz6c0upAbhrJA8kJ4SsFa4ml1WzC18qDmbfJflGJjYRBeGSv5vKWd8Qk%2F6M7A6ouKkZMRJXRBEtHeor5KONvDS&X-Amz-Signature=1b7c3b4bfca2973ca7ca4c229874d87a3dee40d98802f61912a6310a6a2dcdcd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZHXWW5S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWuDcG8wGUEn%2F7ko%2B9s1TY3uWmWpo5o%2FCgWAzvvcejIAIhAImQ4zJR2WgwvXkqtIEdKsoweFmAx8jgY%2F92oDShVyoJKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpVlEd6nKZFOH47YEq3ANRBfAjnJ%2BSdKrzTkq9i1ZiyLqtoOXOBai7zxeqvUzStNW8DMPc17RzqfRRlJDEAYFuRwofH5YpX8kEMDPDJbSkyupyeT777G%2BIxmigVuVWkkyq2ihfjnrEMIwKc6T9OIys43lHfd4pQS5%2FCBZNtE%2BVj%2BXsQpluQ1fujz7DEosq%2F5jsNQgWkXsCP%2FzN8TEtbG8fcnhiDC3hWaLBblK06j6RpjbnEIhRBWwfGDQ7mx9Z7KEBqs%2Fz%2FnQemVOxgFXo%2B5JVBjtQe4at1b%2Bnck2ajEwW1tikAjssHV%2FUGLP%2FBvbMgv%2FAwSMIYHoZmsOmP6ZPtKu2gPpnqCtXr37Q9fvW7e%2FmJBKYC%2Fc2C1I6bBfrB6hz5DAmzDTpKnJJDMc19IdaIwipQOpY0hW4R1ZSsH0JnjPa6IWKJuEeKcAdK9G9G96Rq76CZCNBVftnXG6nVdIZcEObE2tDTwnXG7cx7GcofC18yb%2BAKojISN8OyoHvtXNKH%2FYH%2Fiu4lQlakxb%2Bv6TFV3iHiQ6Anso7JC%2BdHNBB0DIeTWomdnmDmP3qebUhVmTuf%2F7oLAJsowPK7YAGW6%2BGKH%2Bfsk43hD8y5OFIKjtqKjGw6EVPjavDZYr6HbApKOZoP64OPtPXeHt2kGbLsDDfwIC9BjqkAXQk02dkVOySAHdfkSSbKlm01sHGWlT%2BUvRNtAifgMCt7xakBYlkNRG4KbYwWNN6%2BET%2F50FwEkfrSOQmY5qx0t1jGBaRxWJVm6rU5wIOBu%2F4bmnWM2%2FqfIr5Ph7wRKbZ%2FQOXMHHz6c0upAbhrJA8kJ4SsFa4ml1WzC18qDmbfJflGJjYRBeGSv5vKWd8Qk%2F6M7A6ouKkZMRJXRBEtHeor5KONvDS&X-Amz-Signature=4959edbd2aa05ff3189e625943422e0d25560935772ae478f1a0f689c6f186a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZHXWW5S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWuDcG8wGUEn%2F7ko%2B9s1TY3uWmWpo5o%2FCgWAzvvcejIAIhAImQ4zJR2WgwvXkqtIEdKsoweFmAx8jgY%2F92oDShVyoJKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpVlEd6nKZFOH47YEq3ANRBfAjnJ%2BSdKrzTkq9i1ZiyLqtoOXOBai7zxeqvUzStNW8DMPc17RzqfRRlJDEAYFuRwofH5YpX8kEMDPDJbSkyupyeT777G%2BIxmigVuVWkkyq2ihfjnrEMIwKc6T9OIys43lHfd4pQS5%2FCBZNtE%2BVj%2BXsQpluQ1fujz7DEosq%2F5jsNQgWkXsCP%2FzN8TEtbG8fcnhiDC3hWaLBblK06j6RpjbnEIhRBWwfGDQ7mx9Z7KEBqs%2Fz%2FnQemVOxgFXo%2B5JVBjtQe4at1b%2Bnck2ajEwW1tikAjssHV%2FUGLP%2FBvbMgv%2FAwSMIYHoZmsOmP6ZPtKu2gPpnqCtXr37Q9fvW7e%2FmJBKYC%2Fc2C1I6bBfrB6hz5DAmzDTpKnJJDMc19IdaIwipQOpY0hW4R1ZSsH0JnjPa6IWKJuEeKcAdK9G9G96Rq76CZCNBVftnXG6nVdIZcEObE2tDTwnXG7cx7GcofC18yb%2BAKojISN8OyoHvtXNKH%2FYH%2Fiu4lQlakxb%2Bv6TFV3iHiQ6Anso7JC%2BdHNBB0DIeTWomdnmDmP3qebUhVmTuf%2F7oLAJsowPK7YAGW6%2BGKH%2Bfsk43hD8y5OFIKjtqKjGw6EVPjavDZYr6HbApKOZoP64OPtPXeHt2kGbLsDDfwIC9BjqkAXQk02dkVOySAHdfkSSbKlm01sHGWlT%2BUvRNtAifgMCt7xakBYlkNRG4KbYwWNN6%2BET%2F50FwEkfrSOQmY5qx0t1jGBaRxWJVm6rU5wIOBu%2F4bmnWM2%2FqfIr5Ph7wRKbZ%2FQOXMHHz6c0upAbhrJA8kJ4SsFa4ml1WzC18qDmbfJflGJjYRBeGSv5vKWd8Qk%2F6M7A6ouKkZMRJXRBEtHeor5KONvDS&X-Amz-Signature=586c1722ee733ce4261ed3349519b0d2bea6be7c44ca7545b813f4a10d10d70e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4RVRTY2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICd6Kq1IOqHGPl9z7RZWkR9sMdN%2BXJyuvhSJMfCC23HNAiBzWR%2BDV7po8GjlsYSb22qEhYp1cvtJFsQDw0ocX%2F3kySqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXAhphaBKwTOG0OF8KtwDcXuoqfpfNDpoMrDnDGN3ccp6LArZRNVsvo4FAB%2B73V4Im6%2Fk55yz%2B0SJAHH5%2FnwJkd1%2FHXrn%2Fw7t1HOOuPrh1fIUHX0446ENJSXSpnHgp2DfsWIk10FuiJMrKSzoCVEEIw3fJGZhl93s%2FnxtoRAiRIakESLKH6lrPUvUD3bkMgT5FdXdQQSdefdufzKUArj%2BttwkDuRnttBpQshho%2B%2FHPAjhJYVz0IwvwRdqhh0BRLQJ6PfcJg0iSw5cFQtn1V0M%2BnNYFOlAqm8DUwL1Cvl1sz%2FKHJTqRoGbjI1BwJDvsBEMK23msydXPd5H5vwnDz7%2FOLuNT%2BKqhGJW%2FDqJ45sAUdDDJt%2FWgmEZLiVhiMpWuQ1GYqgSo05eyA%2BgIPZFJLJVSceqSHWGyVpU3xmHGgegS0%2B9p7LSfchJ2jT1j5CxI0L6cHsM%2FlpJn7KpytNBEeOHHC9Bw0Pk76VB5ZN%2BWgVSVukq99sCgZ6cTMxVnjYRxhyrP6k7EU9mBCQtfWZ1QQ2%2FYduqlsX5%2Fn5aUiU8nDH5xUYz2RCSg%2Bm6FyF1SgEbRW3q7hR%2BNZnKhwDOJlLvsjYqjRzLEfR1MCMxJnkTAuWRpwwhyH3r9X71IHyo32idFRwOzrOswp9rcNN5A0Awyr%2BAvQY6pgHkN8jA3xoN8qM5Juu%2BDtEgVe%2B8Hl%2FImjzN7QwzzBByTCfVwGowOCBqb2LJDcg6OqssuMs8BskksPQcOaKSJQrSei%2FrF8oD0xXv4ZM1bN0L8btZZavxpyBFGHOOZqAqBtkWPoVAKvmpAzo5RbVz0qmRJLzwiX%2BZxXLzFsHd%2FZCmefayLNvzsRfKtnRpRyYthlKEHRZ0xFlUA9i%2FtNgRBSDm%2FYoXXB31&X-Amz-Signature=25f1386f42880caf2daed47248e7e540f2101b0d7c80762d7cbb36259b8f1cdb&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MMEWOJT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAOOQfKkmEIgFW7m0rB4joCCgtm7e02WtRXuGf1sgF%2FFAiEA0%2FSyjQaDwgpKFEuQcvLVExaCOl%2BpClym5FB%2FyW3%2BdI0qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx%2F5kP8DinWDrxd9SrcA4Y3dST%2BbJSoyGS8us62PqCRqWaYV1xokzZOCjUfX%2F32UwfRmhQ0Wj0WdsH04tVdtxwPdnKB2cWGwqep7DsrFDRUqprjt9oLYxZB3GJtvWydCI6xi9Fw%2FhDRr1Dg8H0PX1bfGJzv8ahojZyqOomCW9uJAzkHjIkk6UkiwBkpKKJgBjfxUpnVwa8xdvOmuZHTAX57j32LsOoi%2FA2unDKaW66VNr7y0K%2B1yl7XaZJdvYVszB32CS7Ytz192LNIAWAh4Rb065iUQk1a7QCW8mIJMDkKPR2RZeYZyi%2BUgLp8vMVlWmH%2FVR2KvEXlgVtoALLG1r%2FKc9U7v%2BadocQNrwuYXkyvwf%2F2vpzvJsMojwsotiyhQQWcBDFfP153NWW6gzkUEnz0AJqLU9qZ6pjjCoJOTZOK4MOPCLPC%2ByAJkU%2BqsdpLOw2dxVRbQqFCY1RqdhiGP6qryDO08O3CmDP2rM9XAMiUvLouwhQWLr%2FoqCDRuxwO0NJqp%2BBxVhNnJoGliFlKo7qOyAMbALo%2BhB1M%2F0hugfr5kY9TgJBceRe3M2iXBT600BZ9TbhjhTetbGK%2BGiSzwpVhGETdeTISzXv0pQjVG0kV1EgkyPHWraw03LPaajYOsxdwyoCWkpBuTqmHMMu%2FgL0GOqUBDVOmAQy6zTL38mkt7XtxKxyawCVPL%2B7MHsXZP2TT5h%2FIsItrScVmV32j6Xt2mP%2FboF9yT5MbUlvgxGCnZamsCpgqU%2F%2BJ%2FCgMbJN2YhP0Gn6Xu%2F6JLezLa6kntOD0W9yF2RpGumCbbdHso1wgKAgiX4FYY8Yt4rNIShZYxV7dOAk8W9JgcPs96pMcZ7tT2LU8Eew%2BtYMI3TvZjBhWtEE%2BWF5C7DiR&X-Amz-Signature=6fc83b6ad05f6b496895f6ebc1845333d38a808582a15c8a02c53d1cd0cdcb9e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GKTPVFH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqY8H0c%2FF2K8NyG4azvEBbOrm4dxMsxHSS49hbqiKMWwIhALNkD5Xf%2BnDLLjMJjAPZLGJF2eXJqJS1lZ%2F5syQodTASKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwE5gMjw1EaCCVyzFsq3APRtviMkqgHa0t1d4t%2BpFaoVv3240FgWZtRyMnoAlVpjGtfmg93lIH9xQdIs%2FBD%2BzFTM%2BzwOLe2Eg27QlAvyHmEjbnsmswOwew3TOi2AGHtjeIwSIcqzeZWJEZTkIh0mSzGbJoBRUI6H2DeV5a6oDZcAS4v6GnBFA%2BeZeFgioW0ty10ptKWFrMmEriRTglWXsf6Ovs%2FQEGTAiIc5hwC4W4J9dnnBEmVafHkV2Hn61HKdwVKXlvtIC7mvlZZPK3sb9aRkD4EMEzmakJ8gAmT0xlLv08EgWdJ%2B4dJTP9WTuU2RphhUQC6BsTNl0XOlYXfd9fEBaLjlPf9sK9%2FdpbiGSmnENKRCd14OLdANVtqaNT2WDFrvViBXEv5MM%2F%2BJe1P74QDwcHYk3nXZQ9gD6Z2qyoGS0GxSD7KuPLoZRy%2FJ%2B3fYUgIpka1hiiuCayEdE5WYhZ7xFaz%2FhWl0q6s92De%2BO9Iw6EpXjZSSoLrlUELz3wEVMnWkXmpw9HiuJoCHHDGY3lqq7DawUQkAKWngBeV0RowEPbl8f4QdppKZKmTiuEn%2FZ12CzCm4oIkJG0FJ8T8dd4KuBaT23yuzPGGQQxOthxv3QzmbETC4yVgPOcQ1OsiJCE75AzoycwlKQCcVTCRv4C9BjqkAZ4p687IZThE1r%2BXdyncRTSaHAZPyfWZ%2BOjwsm8qVm7MFMs2d5lg9gxsmiGcwQ5wKgIK6IaoKslyQHSAd8JbJtKGT65m7VVAr9A7qeJBi4FNbo7MB3BBXVZIRn8C1Ff3Y1YRZ7YX%2BYAkvnRcDniJ7g8mtukwdHFWnj2T3CfEPP2Lu7Cmd7yiIaY5iWAR8KkJtVI%2BhaXgSe1i9OgnxAiyg1Rqsvy0&X-Amz-Signature=69c4b566fa540ab9122f24286e56f28e4c91b4cf00aff3a64f671fdfb6474805&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHBYSIML%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8dugMPoUTUpvh4gzsYML0KuMKAWtGCxphK6QIkP9BZAIgKm3HAxm84uVQy2vIUUMAu3KVpvbWKpc4QitSDK5e00IqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPfuQJYZGcsRwkt2dCrcAxAPl09Fk5%2FtESccsdGJuhRAofOaW%2FuSCYY%2BhBgY%2FjhU%2BaUP3lZJd0L%2BTfPHZ9LSqhZk1zM%2Fjp6y6ikyGkDyqmieunx7Ur8fHLcSmnCQ3vJ4i2li27G4Io0a3XEOdk6YhjE4ZiMQcWgDoRGHbH3tsCu7d18cJeOGF02quj2CNJ9Vxddl3sN3CNunAT5I9BeRLwhaklzenCUQv1pwOpCTW1jUtBhth%2F%2Bg%2FP1J018Xg67homvfuJn0%2F9BfqBwewQDUPVb92lK7PIkK3L8N1lj4cpemeCGUEejyE7f5aKDQLRgzpFn9ZyJAKJFgHDCfUL9J%2Fj3RfT3fBr2aP4DWTCDYh4PGzam1Mg4vDAXvaUvfQzymN6Pydtg90yQbEtP3Mz9WodeG5OASuOXegcYXTHD2jwGVeblZIUH7fLjDMWYpK6nL%2BO2FyfO5Achh2BT4t3%2FMHf3a3%2FQBtDPoQ9N6a7QQIEj4EtXZFBMXrJsaQjZP48j7DnXEp8eteNnocO61jGRNCNYXgnxd28MNO4bj4dg5%2BNepoZYmJsYrxcjVVbXFAn7%2BBmrLt5tTqYhLk%2FKQvtyX8VrNU311uiHu2sHGy4TmsRG0SPmW1dMqqAtNWvHBu8WZXv6OZZ9bkII98ZceMODAgL0GOqUBEIdJ6lXPbnYZ3ju%2F0dycrviWUvgPrz%2Fb%2FANel1y4Q0eLm0EcnWkuFyMsysze%2BviPjhfK1CG%2BLxEQMxMpTxRmgHMNEKPESNAz5l8dg8hhTQehNTlCoNJnpOcmti%2BZDtzK0IfZJYaKChcxvtQ1PERyfjFPG6Nlgb5ddMwpBspQI84DhnvbWRWqsE5aG%2FHMAknrRHMTLvvXlICfa2N%2FGx3QN9LeC7Sg&X-Amz-Signature=188e1447fde148d26563cc52c3e2563054ca57babf69a9325130927b6a9be02f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHBYSIML%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8dugMPoUTUpvh4gzsYML0KuMKAWtGCxphK6QIkP9BZAIgKm3HAxm84uVQy2vIUUMAu3KVpvbWKpc4QitSDK5e00IqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPfuQJYZGcsRwkt2dCrcAxAPl09Fk5%2FtESccsdGJuhRAofOaW%2FuSCYY%2BhBgY%2FjhU%2BaUP3lZJd0L%2BTfPHZ9LSqhZk1zM%2Fjp6y6ikyGkDyqmieunx7Ur8fHLcSmnCQ3vJ4i2li27G4Io0a3XEOdk6YhjE4ZiMQcWgDoRGHbH3tsCu7d18cJeOGF02quj2CNJ9Vxddl3sN3CNunAT5I9BeRLwhaklzenCUQv1pwOpCTW1jUtBhth%2F%2Bg%2FP1J018Xg67homvfuJn0%2F9BfqBwewQDUPVb92lK7PIkK3L8N1lj4cpemeCGUEejyE7f5aKDQLRgzpFn9ZyJAKJFgHDCfUL9J%2Fj3RfT3fBr2aP4DWTCDYh4PGzam1Mg4vDAXvaUvfQzymN6Pydtg90yQbEtP3Mz9WodeG5OASuOXegcYXTHD2jwGVeblZIUH7fLjDMWYpK6nL%2BO2FyfO5Achh2BT4t3%2FMHf3a3%2FQBtDPoQ9N6a7QQIEj4EtXZFBMXrJsaQjZP48j7DnXEp8eteNnocO61jGRNCNYXgnxd28MNO4bj4dg5%2BNepoZYmJsYrxcjVVbXFAn7%2BBmrLt5tTqYhLk%2FKQvtyX8VrNU311uiHu2sHGy4TmsRG0SPmW1dMqqAtNWvHBu8WZXv6OZZ9bkII98ZceMODAgL0GOqUBEIdJ6lXPbnYZ3ju%2F0dycrviWUvgPrz%2Fb%2FANel1y4Q0eLm0EcnWkuFyMsysze%2BviPjhfK1CG%2BLxEQMxMpTxRmgHMNEKPESNAz5l8dg8hhTQehNTlCoNJnpOcmti%2BZDtzK0IfZJYaKChcxvtQ1PERyfjFPG6Nlgb5ddMwpBspQI84DhnvbWRWqsE5aG%2FHMAknrRHMTLvvXlICfa2N%2FGx3QN9LeC7Sg&X-Amz-Signature=b72ef9ddc5045897e21fcdf80cf35099fc8b9abde62c70a6ce9d22d93d8b693a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
