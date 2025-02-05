

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466547YNM4A%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDcLFcZAodej0UcWago5AJBW4V4mF0h2NvfEer2lAYDBAIgR6sFhjpEEaDClFJ9hDaqci5diaFvW5xx1bH8gjuzFhoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFq%2FD3N7DHdQqQ2jjSrcA%2BGxaMcit26HufZhVVryzNzm%2BP7qPsN95%2FAGdG5HOd20tPkoQY7C64WxHDsqbbWQvBoAaLb6r6%2FDx4UjIzj%2Bduo7YzKecrm4IQ7GK8gfg%2FKEHM0HeYmywJA%2F3aZdsfdjMfxJoHe6de71BpQAHsEUmsFUJAuJV1LqnCp%2BkvDpmKoywTmXrJlbTRbbwoFpjXbWAudQyoT6ThHVIclT%2F4dRBxL6l4pS9hZYTHJFgB9YyTtjEqMK4KIJtLBNdkz6leJ1DRLfyV9AyVW4pGY38elRTXPlK51Z4gAYot67mdGpcaQU25KyePu8ZEUd8gNZ6hrIbJRWfkB%2B2PQT4nv1TmJzgjRuzx1C%2FN8LzRCeI5p3qxQHI%2B%2FdEhPXUto%2F4e%2BMWrwNbNsLayGVmXKFXHIkfbVXsL7v%2FDwsDKMLqdKmVNr0A7y7FKMaI%2BScQtTIqDWoY7X3oEP4tbVRgUDwBAexPOY82QJ7r%2F1rPdqpXqT9pFNRI5JLrcHFINGe0%2BKn5t5589OXrGXIVvAr8yUBhDh4d8Dlcu1YQicjNH%2B9uYaUvNGfChuZhoh3UEah807mGwECZBr9n71bgk%2F8OxxjrlMDydbni%2FsZW7G0rbaS7yI87pSdIppBdTKdSYIC8oaKMspPMKDPjL0GOqUBkeohIuoao%2BuHq8t%2Fk2BMAcaJ0%2BbW6aoiKi6E%2Bl1YMJjylBcCcaKg8TQvcfWMpuEVmD4b2bti7x2f2%2BzAxO3yGBdM2PMPbMRo94MMaOqYijKCcwYoQkGoaeccbzvrTyX4Vr1b%2B565ZoRba0jmWLO3nyz88CmA5ATeuWZ9l3vLsAzZnUMvcnlcXFgxOVTyipxoOjIHcG6SG%2FpMeUW28jtmszBJV8Rl&X-Amz-Signature=23720fe94f43acac37ddc62ed494ec4331748e3f2bcb67309cea99a9ef239846&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466547YNM4A%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDcLFcZAodej0UcWago5AJBW4V4mF0h2NvfEer2lAYDBAIgR6sFhjpEEaDClFJ9hDaqci5diaFvW5xx1bH8gjuzFhoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFq%2FD3N7DHdQqQ2jjSrcA%2BGxaMcit26HufZhVVryzNzm%2BP7qPsN95%2FAGdG5HOd20tPkoQY7C64WxHDsqbbWQvBoAaLb6r6%2FDx4UjIzj%2Bduo7YzKecrm4IQ7GK8gfg%2FKEHM0HeYmywJA%2F3aZdsfdjMfxJoHe6de71BpQAHsEUmsFUJAuJV1LqnCp%2BkvDpmKoywTmXrJlbTRbbwoFpjXbWAudQyoT6ThHVIclT%2F4dRBxL6l4pS9hZYTHJFgB9YyTtjEqMK4KIJtLBNdkz6leJ1DRLfyV9AyVW4pGY38elRTXPlK51Z4gAYot67mdGpcaQU25KyePu8ZEUd8gNZ6hrIbJRWfkB%2B2PQT4nv1TmJzgjRuzx1C%2FN8LzRCeI5p3qxQHI%2B%2FdEhPXUto%2F4e%2BMWrwNbNsLayGVmXKFXHIkfbVXsL7v%2FDwsDKMLqdKmVNr0A7y7FKMaI%2BScQtTIqDWoY7X3oEP4tbVRgUDwBAexPOY82QJ7r%2F1rPdqpXqT9pFNRI5JLrcHFINGe0%2BKn5t5589OXrGXIVvAr8yUBhDh4d8Dlcu1YQicjNH%2B9uYaUvNGfChuZhoh3UEah807mGwECZBr9n71bgk%2F8OxxjrlMDydbni%2FsZW7G0rbaS7yI87pSdIppBdTKdSYIC8oaKMspPMKDPjL0GOqUBkeohIuoao%2BuHq8t%2Fk2BMAcaJ0%2BbW6aoiKi6E%2Bl1YMJjylBcCcaKg8TQvcfWMpuEVmD4b2bti7x2f2%2BzAxO3yGBdM2PMPbMRo94MMaOqYijKCcwYoQkGoaeccbzvrTyX4Vr1b%2B565ZoRba0jmWLO3nyz88CmA5ATeuWZ9l3vLsAzZnUMvcnlcXFgxOVTyipxoOjIHcG6SG%2FpMeUW28jtmszBJV8Rl&X-Amz-Signature=94eabe3edad96de812ccfdbdffffbc564941f25812a430d7893fd5112715d9de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466547YNM4A%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDcLFcZAodej0UcWago5AJBW4V4mF0h2NvfEer2lAYDBAIgR6sFhjpEEaDClFJ9hDaqci5diaFvW5xx1bH8gjuzFhoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFq%2FD3N7DHdQqQ2jjSrcA%2BGxaMcit26HufZhVVryzNzm%2BP7qPsN95%2FAGdG5HOd20tPkoQY7C64WxHDsqbbWQvBoAaLb6r6%2FDx4UjIzj%2Bduo7YzKecrm4IQ7GK8gfg%2FKEHM0HeYmywJA%2F3aZdsfdjMfxJoHe6de71BpQAHsEUmsFUJAuJV1LqnCp%2BkvDpmKoywTmXrJlbTRbbwoFpjXbWAudQyoT6ThHVIclT%2F4dRBxL6l4pS9hZYTHJFgB9YyTtjEqMK4KIJtLBNdkz6leJ1DRLfyV9AyVW4pGY38elRTXPlK51Z4gAYot67mdGpcaQU25KyePu8ZEUd8gNZ6hrIbJRWfkB%2B2PQT4nv1TmJzgjRuzx1C%2FN8LzRCeI5p3qxQHI%2B%2FdEhPXUto%2F4e%2BMWrwNbNsLayGVmXKFXHIkfbVXsL7v%2FDwsDKMLqdKmVNr0A7y7FKMaI%2BScQtTIqDWoY7X3oEP4tbVRgUDwBAexPOY82QJ7r%2F1rPdqpXqT9pFNRI5JLrcHFINGe0%2BKn5t5589OXrGXIVvAr8yUBhDh4d8Dlcu1YQicjNH%2B9uYaUvNGfChuZhoh3UEah807mGwECZBr9n71bgk%2F8OxxjrlMDydbni%2FsZW7G0rbaS7yI87pSdIppBdTKdSYIC8oaKMspPMKDPjL0GOqUBkeohIuoao%2BuHq8t%2Fk2BMAcaJ0%2BbW6aoiKi6E%2Bl1YMJjylBcCcaKg8TQvcfWMpuEVmD4b2bti7x2f2%2BzAxO3yGBdM2PMPbMRo94MMaOqYijKCcwYoQkGoaeccbzvrTyX4Vr1b%2B565ZoRba0jmWLO3nyz88CmA5ATeuWZ9l3vLsAzZnUMvcnlcXFgxOVTyipxoOjIHcG6SG%2FpMeUW28jtmszBJV8Rl&X-Amz-Signature=08c4ead3444acd0312841923f6dc06f59262436a99b360b7b377f6f9adb7cb0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCYNKPID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDtkvjDUGuNPCIWj3sj50DJaRiDeiuBh2ZmSt7STRag2QIgX1RBO1T%2FHEYKPDFPfegao3RRmOggjXafOvzmU6Mknuoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOQDCvNKcXeqpHs4HCrcAzLaZw1mts09lyvVaOx6%2B1qstExq8GU6bOA8RjaoSqYAcKQtRHqNd0hr56c4YRcbFuPKI%2BalrJLcxukqXqvbgUjIMALQkGocIjooXA1ucR9C9fC2a8oY%2FAisDIljyr3CtdG604o7IuOb8pojOI2Nz1P1e81Q08KFkIE5fZJa6WlonKVtTO8fGCk%2BC81HXb3g0sJqUqr%2FeDpOI8vILh2SsvO%2B8EJU2b%2F9bGjngCO%2B5S744LaR7gm2EF%2F6nhf6R37Y8ZyFi5CEa%2FcbCNLR73Nyu5Mx7PFcWHW67DO%2B91HzQr4%2FgsF6LbXiRDihFIWxY2xSBDpelLOC4iSEFSFiNPczElWNfdhi6me0UXxqQ%2BdJij5ehnfbKjNY9BRXYlPAuNiQRrJAMhB693E%2FYIqIRX8DqgdKbe%2BDURvfY25%2BgA%2BZOnvvgroNZ8uDX%2BrS4zbiraQ35ormSbI1dc7uvFNSCJeJwgABUcJws9mRHkhyGj9r%2FeV8r8JN40TnFcUYzT38q7XeOj93V2upcQqOt2X2J9kUSP%2BBchJxTH9Bp%2FQAeWdjVzJmWjH%2FTQAUy%2FfiwdahnnbXiOYW0qMGETFgCYEzYLyD9%2BD8vQp30lkmuGRIlHom1f9jzJ6J%2Bg54EmrmVcxEMIHQjL0GOqUB7GR1YPKdLZJFejvXiF3IabOSpjwhECObSLWTdh8naEqpHJ4q8FkriCJIXHgBmx7ta7HQrKsCyDkFg3n4EkyjTMkOeydYUxgCXg7L2UiNR4DdfJNx6nOOxorXlMjbd0%2BWUoBOdmXSl2apWkQ5RUCEYhHATUnmhmL1mx8cg77esOj6su6juC9PWO3jnd1swkUho0901u%2FiurhTuKNJYY%2B6irW7IMC%2F&X-Amz-Signature=d404eb95afc586101303426ebbef4b725f825b1114f6128ba75871518457f356&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCYNKPID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDtkvjDUGuNPCIWj3sj50DJaRiDeiuBh2ZmSt7STRag2QIgX1RBO1T%2FHEYKPDFPfegao3RRmOggjXafOvzmU6Mknuoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOQDCvNKcXeqpHs4HCrcAzLaZw1mts09lyvVaOx6%2B1qstExq8GU6bOA8RjaoSqYAcKQtRHqNd0hr56c4YRcbFuPKI%2BalrJLcxukqXqvbgUjIMALQkGocIjooXA1ucR9C9fC2a8oY%2FAisDIljyr3CtdG604o7IuOb8pojOI2Nz1P1e81Q08KFkIE5fZJa6WlonKVtTO8fGCk%2BC81HXb3g0sJqUqr%2FeDpOI8vILh2SsvO%2B8EJU2b%2F9bGjngCO%2B5S744LaR7gm2EF%2F6nhf6R37Y8ZyFi5CEa%2FcbCNLR73Nyu5Mx7PFcWHW67DO%2B91HzQr4%2FgsF6LbXiRDihFIWxY2xSBDpelLOC4iSEFSFiNPczElWNfdhi6me0UXxqQ%2BdJij5ehnfbKjNY9BRXYlPAuNiQRrJAMhB693E%2FYIqIRX8DqgdKbe%2BDURvfY25%2BgA%2BZOnvvgroNZ8uDX%2BrS4zbiraQ35ormSbI1dc7uvFNSCJeJwgABUcJws9mRHkhyGj9r%2FeV8r8JN40TnFcUYzT38q7XeOj93V2upcQqOt2X2J9kUSP%2BBchJxTH9Bp%2FQAeWdjVzJmWjH%2FTQAUy%2FfiwdahnnbXiOYW0qMGETFgCYEzYLyD9%2BD8vQp30lkmuGRIlHom1f9jzJ6J%2Bg54EmrmVcxEMIHQjL0GOqUB7GR1YPKdLZJFejvXiF3IabOSpjwhECObSLWTdh8naEqpHJ4q8FkriCJIXHgBmx7ta7HQrKsCyDkFg3n4EkyjTMkOeydYUxgCXg7L2UiNR4DdfJNx6nOOxorXlMjbd0%2BWUoBOdmXSl2apWkQ5RUCEYhHATUnmhmL1mx8cg77esOj6su6juC9PWO3jnd1swkUho0901u%2FiurhTuKNJYY%2B6irW7IMC%2F&X-Amz-Signature=cc84f8c02c33fe5cf71758a56f0a89aa701f69ca7a58d301a3cb87496ce5dbe6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCYNKPID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDtkvjDUGuNPCIWj3sj50DJaRiDeiuBh2ZmSt7STRag2QIgX1RBO1T%2FHEYKPDFPfegao3RRmOggjXafOvzmU6Mknuoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOQDCvNKcXeqpHs4HCrcAzLaZw1mts09lyvVaOx6%2B1qstExq8GU6bOA8RjaoSqYAcKQtRHqNd0hr56c4YRcbFuPKI%2BalrJLcxukqXqvbgUjIMALQkGocIjooXA1ucR9C9fC2a8oY%2FAisDIljyr3CtdG604o7IuOb8pojOI2Nz1P1e81Q08KFkIE5fZJa6WlonKVtTO8fGCk%2BC81HXb3g0sJqUqr%2FeDpOI8vILh2SsvO%2B8EJU2b%2F9bGjngCO%2B5S744LaR7gm2EF%2F6nhf6R37Y8ZyFi5CEa%2FcbCNLR73Nyu5Mx7PFcWHW67DO%2B91HzQr4%2FgsF6LbXiRDihFIWxY2xSBDpelLOC4iSEFSFiNPczElWNfdhi6me0UXxqQ%2BdJij5ehnfbKjNY9BRXYlPAuNiQRrJAMhB693E%2FYIqIRX8DqgdKbe%2BDURvfY25%2BgA%2BZOnvvgroNZ8uDX%2BrS4zbiraQ35ormSbI1dc7uvFNSCJeJwgABUcJws9mRHkhyGj9r%2FeV8r8JN40TnFcUYzT38q7XeOj93V2upcQqOt2X2J9kUSP%2BBchJxTH9Bp%2FQAeWdjVzJmWjH%2FTQAUy%2FfiwdahnnbXiOYW0qMGETFgCYEzYLyD9%2BD8vQp30lkmuGRIlHom1f9jzJ6J%2Bg54EmrmVcxEMIHQjL0GOqUB7GR1YPKdLZJFejvXiF3IabOSpjwhECObSLWTdh8naEqpHJ4q8FkriCJIXHgBmx7ta7HQrKsCyDkFg3n4EkyjTMkOeydYUxgCXg7L2UiNR4DdfJNx6nOOxorXlMjbd0%2BWUoBOdmXSl2apWkQ5RUCEYhHATUnmhmL1mx8cg77esOj6su6juC9PWO3jnd1swkUho0901u%2FiurhTuKNJYY%2B6irW7IMC%2F&X-Amz-Signature=e4d23990af28995324cf211f0efc22c6238225e3b187fa4efbf6db526b7c372f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCYNKPID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDtkvjDUGuNPCIWj3sj50DJaRiDeiuBh2ZmSt7STRag2QIgX1RBO1T%2FHEYKPDFPfegao3RRmOggjXafOvzmU6Mknuoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOQDCvNKcXeqpHs4HCrcAzLaZw1mts09lyvVaOx6%2B1qstExq8GU6bOA8RjaoSqYAcKQtRHqNd0hr56c4YRcbFuPKI%2BalrJLcxukqXqvbgUjIMALQkGocIjooXA1ucR9C9fC2a8oY%2FAisDIljyr3CtdG604o7IuOb8pojOI2Nz1P1e81Q08KFkIE5fZJa6WlonKVtTO8fGCk%2BC81HXb3g0sJqUqr%2FeDpOI8vILh2SsvO%2B8EJU2b%2F9bGjngCO%2B5S744LaR7gm2EF%2F6nhf6R37Y8ZyFi5CEa%2FcbCNLR73Nyu5Mx7PFcWHW67DO%2B91HzQr4%2FgsF6LbXiRDihFIWxY2xSBDpelLOC4iSEFSFiNPczElWNfdhi6me0UXxqQ%2BdJij5ehnfbKjNY9BRXYlPAuNiQRrJAMhB693E%2FYIqIRX8DqgdKbe%2BDURvfY25%2BgA%2BZOnvvgroNZ8uDX%2BrS4zbiraQ35ormSbI1dc7uvFNSCJeJwgABUcJws9mRHkhyGj9r%2FeV8r8JN40TnFcUYzT38q7XeOj93V2upcQqOt2X2J9kUSP%2BBchJxTH9Bp%2FQAeWdjVzJmWjH%2FTQAUy%2FfiwdahnnbXiOYW0qMGETFgCYEzYLyD9%2BD8vQp30lkmuGRIlHom1f9jzJ6J%2Bg54EmrmVcxEMIHQjL0GOqUB7GR1YPKdLZJFejvXiF3IabOSpjwhECObSLWTdh8naEqpHJ4q8FkriCJIXHgBmx7ta7HQrKsCyDkFg3n4EkyjTMkOeydYUxgCXg7L2UiNR4DdfJNx6nOOxorXlMjbd0%2BWUoBOdmXSl2apWkQ5RUCEYhHATUnmhmL1mx8cg77esOj6su6juC9PWO3jnd1swkUho0901u%2FiurhTuKNJYY%2B6irW7IMC%2F&X-Amz-Signature=5338982c812db30665f4ed4cd7b9e48a02578883debcdfd371b1070197d659a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCYNKPID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDtkvjDUGuNPCIWj3sj50DJaRiDeiuBh2ZmSt7STRag2QIgX1RBO1T%2FHEYKPDFPfegao3RRmOggjXafOvzmU6Mknuoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOQDCvNKcXeqpHs4HCrcAzLaZw1mts09lyvVaOx6%2B1qstExq8GU6bOA8RjaoSqYAcKQtRHqNd0hr56c4YRcbFuPKI%2BalrJLcxukqXqvbgUjIMALQkGocIjooXA1ucR9C9fC2a8oY%2FAisDIljyr3CtdG604o7IuOb8pojOI2Nz1P1e81Q08KFkIE5fZJa6WlonKVtTO8fGCk%2BC81HXb3g0sJqUqr%2FeDpOI8vILh2SsvO%2B8EJU2b%2F9bGjngCO%2B5S744LaR7gm2EF%2F6nhf6R37Y8ZyFi5CEa%2FcbCNLR73Nyu5Mx7PFcWHW67DO%2B91HzQr4%2FgsF6LbXiRDihFIWxY2xSBDpelLOC4iSEFSFiNPczElWNfdhi6me0UXxqQ%2BdJij5ehnfbKjNY9BRXYlPAuNiQRrJAMhB693E%2FYIqIRX8DqgdKbe%2BDURvfY25%2BgA%2BZOnvvgroNZ8uDX%2BrS4zbiraQ35ormSbI1dc7uvFNSCJeJwgABUcJws9mRHkhyGj9r%2FeV8r8JN40TnFcUYzT38q7XeOj93V2upcQqOt2X2J9kUSP%2BBchJxTH9Bp%2FQAeWdjVzJmWjH%2FTQAUy%2FfiwdahnnbXiOYW0qMGETFgCYEzYLyD9%2BD8vQp30lkmuGRIlHom1f9jzJ6J%2Bg54EmrmVcxEMIHQjL0GOqUB7GR1YPKdLZJFejvXiF3IabOSpjwhECObSLWTdh8naEqpHJ4q8FkriCJIXHgBmx7ta7HQrKsCyDkFg3n4EkyjTMkOeydYUxgCXg7L2UiNR4DdfJNx6nOOxorXlMjbd0%2BWUoBOdmXSl2apWkQ5RUCEYhHATUnmhmL1mx8cg77esOj6su6juC9PWO3jnd1swkUho0901u%2FiurhTuKNJYY%2B6irW7IMC%2F&X-Amz-Signature=ff2bc3e8befd7502f893946e21f5030b0669fa2caf2033ba2e71b78897d404a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCYNKPID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDtkvjDUGuNPCIWj3sj50DJaRiDeiuBh2ZmSt7STRag2QIgX1RBO1T%2FHEYKPDFPfegao3RRmOggjXafOvzmU6Mknuoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOQDCvNKcXeqpHs4HCrcAzLaZw1mts09lyvVaOx6%2B1qstExq8GU6bOA8RjaoSqYAcKQtRHqNd0hr56c4YRcbFuPKI%2BalrJLcxukqXqvbgUjIMALQkGocIjooXA1ucR9C9fC2a8oY%2FAisDIljyr3CtdG604o7IuOb8pojOI2Nz1P1e81Q08KFkIE5fZJa6WlonKVtTO8fGCk%2BC81HXb3g0sJqUqr%2FeDpOI8vILh2SsvO%2B8EJU2b%2F9bGjngCO%2B5S744LaR7gm2EF%2F6nhf6R37Y8ZyFi5CEa%2FcbCNLR73Nyu5Mx7PFcWHW67DO%2B91HzQr4%2FgsF6LbXiRDihFIWxY2xSBDpelLOC4iSEFSFiNPczElWNfdhi6me0UXxqQ%2BdJij5ehnfbKjNY9BRXYlPAuNiQRrJAMhB693E%2FYIqIRX8DqgdKbe%2BDURvfY25%2BgA%2BZOnvvgroNZ8uDX%2BrS4zbiraQ35ormSbI1dc7uvFNSCJeJwgABUcJws9mRHkhyGj9r%2FeV8r8JN40TnFcUYzT38q7XeOj93V2upcQqOt2X2J9kUSP%2BBchJxTH9Bp%2FQAeWdjVzJmWjH%2FTQAUy%2FfiwdahnnbXiOYW0qMGETFgCYEzYLyD9%2BD8vQp30lkmuGRIlHom1f9jzJ6J%2Bg54EmrmVcxEMIHQjL0GOqUB7GR1YPKdLZJFejvXiF3IabOSpjwhECObSLWTdh8naEqpHJ4q8FkriCJIXHgBmx7ta7HQrKsCyDkFg3n4EkyjTMkOeydYUxgCXg7L2UiNR4DdfJNx6nOOxorXlMjbd0%2BWUoBOdmXSl2apWkQ5RUCEYhHATUnmhmL1mx8cg77esOj6su6juC9PWO3jnd1swkUho0901u%2FiurhTuKNJYY%2B6irW7IMC%2F&X-Amz-Signature=c2a36a8c84c8a2abf34c3311ca4c4e0677c39861046113fd9d33c9714135dbbd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEXEAEKN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCRNVz5yOLjrgAsCCtVC0o0ZXmtPlu3U2YpkEhLHeJMsAIgJ8a3Uq6V5NAoGmt71604c%2FTDrSh9zudnhZMeOFTyPPIq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDN3%2FqIH%2BF52rVX6qjCrcA2K7jd2gKXWQBHkPVVbcPQUZm7mAvP4RQWBfGSIPDOemIUC6nGryLl8TcORgDdta8%2Fg%2BgG3C%2FeBCHMBCi0M7VhsSkB0Tm%2BMxc9PM0uuytsudBGOc0kZ3vu11dQnuzAKhoVnDwlhrU72tnwJity%2FHsgnRzunm18Zlx56hMy2TTfkHZqL8TJZMLzrWPX9ZoEQAHWD0Ea3kcnBZ96%2FbnQ2ke1dRE13Gab1x%2BlWrezzELGh5Umy6xSQfQwppnAdhpCUefwP%2BGw1Dd%2FFvimaYMNzF12JoeBtXdebmLshRxGXE4jiP6JWBAOXCFdXYi3GkQHvHOn2lKgIKgmXa9xUx10r5zZTrJllTPF1MZGjoXcJUi5w0FMijW0KO1vL69g5jHxU3wbbKYu%2Fq4z0MdeyvTdTKFCwgLQoeqRwnKyC8rorEz1cxVxH9HX2G4gNTO90PAGqmW5xuK5m9mQxk7SUVBpPbB07d0Gqwg2RJ%2BxpYqMi%2FJ33NFSueYyX5XabwGC0fyy1RztnFinJzRPESnzjHrspEheLXxa8JFr6df2IyGbdDY9rVLqxI04NeuWzt9UYW9UPiV%2FOsAmKBUF%2BHb4Bj0pWzJNRTm4YtiCkFaJn0hKgNPakbW8v3jJbUepQLyI3yML7PjL0GOqUBI4Q%2F9s1SP7aNEwjdDGc6qu59ABTDPqNIx75PTx2OZBzrt8j5DaWuKY18t0H1lxGcvN2gOuMj7ovBrEnmYuqNr5%2FBrXT0TwGrrXCxbe5KaD5g%2BHzQd5jp0kKv40vdlX58nDhkFGfzCriuu%2FhtvlDfQXumfOLjvXswcRjYjhEJVrohrNhHyuzafyZcznwSgPRt2XIzhiAivCh%2BKrsbc5RYBvXQrnBh&X-Amz-Signature=10a6aafe8ee2ef24d8ff2b111916fae92b813d92b5f4892478af3fdfbcf4a40a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI7W2Q5P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIBFlb4BzovgR08NwbavYG6lIPyN%2BjLTrnPC34pBBbZbBAiB49DjY4Yy3%2BITrwxD5Ib7eQm%2Fx29nXBrnlZgo2pm5PGir%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMUSAo8N%2FFXbZf%2F6tEKtwD7DTExddSiDPFk%2Bx2ZhBqMrd5Kp2Iv2Gi3DLSppWMmwfgjCsy2G5VpXMRJz%2BcKVcOdYz37onXC0wIT3GiV87zbg0dxymXqPVjDp%2BRFTiHNYrCGfbfcslLx1wlkgCNDIxAhs0RVVkqX0Z3Lt5kjOxfBdgvmvY%2F01d4Ff96Xf6GM0Kgfo%2BE0aXgL1HH79xXoaE5gpOQH1raEnSyOpBh9iZY9Xj7EzMc0H0mcJB8BcZTcVZr3pR90OiaHsdKcaKrlDTs3uV9xoqquiQe3Bvb7nMw1hbCK4EYNipFRyStufbKzosWrfp1oduiHw6iM5uELKlGRyMz7s6DaoRHriGUC%2BLscJKSnlLHK%2FiU9zObBDXe2tZvkKP9sEUX3f%2FNpIgYhz9mCnaCd8xuPDq8EVt%2F6o00kfOs5d9XyoL0P31MEimS4%2B9wz3jeDwvqKpJX%2BzVinP31hKiCnD2UwS9GZ%2BTD61Ba1IoLwrcL0dC8nqTXtWpbWxK1RjAx80LNyLGR21xUPqJEcKrxU6edrEd0Fv0BJl1%2BF0D0zF8MXypfKZuvOunaMyU4fcmA0N%2F0LiZynJCSJ42xkickLS418E61KY2NHXgw7GMYw5sP9Z1Onw2Bx0XSOeWddK3GIkAbR3ozugUws8%2BMvQY6pgFNsr796Gc%2FtjN%2BsvTLZZ%2FC2m65V6U9vWPHKVHA2TnYGweiYNmIpPIR9KvrDpxSB5exQlZjm1aHi3ZevzQIaiGPUhF5OO6A8CaTuFUZYAoTqNckWWdFADFthkioZTHUOiWItK36Zz6nJmAQ49baWvJN1k8yQH6o6yaRhQiXprd5ABvcheSOLs9GCkJ%2F8UPBNFI8blcr5G9ihMftZQHMU6gKoPRX1qsq&X-Amz-Signature=197064bdcf6a72f00eb9aafe9106719ffb50443bfee0ad1952ba37a06048a981&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCYNKPID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDtkvjDUGuNPCIWj3sj50DJaRiDeiuBh2ZmSt7STRag2QIgX1RBO1T%2FHEYKPDFPfegao3RRmOggjXafOvzmU6Mknuoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOQDCvNKcXeqpHs4HCrcAzLaZw1mts09lyvVaOx6%2B1qstExq8GU6bOA8RjaoSqYAcKQtRHqNd0hr56c4YRcbFuPKI%2BalrJLcxukqXqvbgUjIMALQkGocIjooXA1ucR9C9fC2a8oY%2FAisDIljyr3CtdG604o7IuOb8pojOI2Nz1P1e81Q08KFkIE5fZJa6WlonKVtTO8fGCk%2BC81HXb3g0sJqUqr%2FeDpOI8vILh2SsvO%2B8EJU2b%2F9bGjngCO%2B5S744LaR7gm2EF%2F6nhf6R37Y8ZyFi5CEa%2FcbCNLR73Nyu5Mx7PFcWHW67DO%2B91HzQr4%2FgsF6LbXiRDihFIWxY2xSBDpelLOC4iSEFSFiNPczElWNfdhi6me0UXxqQ%2BdJij5ehnfbKjNY9BRXYlPAuNiQRrJAMhB693E%2FYIqIRX8DqgdKbe%2BDURvfY25%2BgA%2BZOnvvgroNZ8uDX%2BrS4zbiraQ35ormSbI1dc7uvFNSCJeJwgABUcJws9mRHkhyGj9r%2FeV8r8JN40TnFcUYzT38q7XeOj93V2upcQqOt2X2J9kUSP%2BBchJxTH9Bp%2FQAeWdjVzJmWjH%2FTQAUy%2FfiwdahnnbXiOYW0qMGETFgCYEzYLyD9%2BD8vQp30lkmuGRIlHom1f9jzJ6J%2Bg54EmrmVcxEMIHQjL0GOqUB7GR1YPKdLZJFejvXiF3IabOSpjwhECObSLWTdh8naEqpHJ4q8FkriCJIXHgBmx7ta7HQrKsCyDkFg3n4EkyjTMkOeydYUxgCXg7L2UiNR4DdfJNx6nOOxorXlMjbd0%2BWUoBOdmXSl2apWkQ5RUCEYhHATUnmhmL1mx8cg77esOj6su6juC9PWO3jnd1swkUho0901u%2FiurhTuKNJYY%2B6irW7IMC%2F&X-Amz-Signature=d5d5fbdd1e84f7e2c2878fca60abd3e9579db4c1b5a0864738b6929c226bae84&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCYNKPID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDtkvjDUGuNPCIWj3sj50DJaRiDeiuBh2ZmSt7STRag2QIgX1RBO1T%2FHEYKPDFPfegao3RRmOggjXafOvzmU6Mknuoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOQDCvNKcXeqpHs4HCrcAzLaZw1mts09lyvVaOx6%2B1qstExq8GU6bOA8RjaoSqYAcKQtRHqNd0hr56c4YRcbFuPKI%2BalrJLcxukqXqvbgUjIMALQkGocIjooXA1ucR9C9fC2a8oY%2FAisDIljyr3CtdG604o7IuOb8pojOI2Nz1P1e81Q08KFkIE5fZJa6WlonKVtTO8fGCk%2BC81HXb3g0sJqUqr%2FeDpOI8vILh2SsvO%2B8EJU2b%2F9bGjngCO%2B5S744LaR7gm2EF%2F6nhf6R37Y8ZyFi5CEa%2FcbCNLR73Nyu5Mx7PFcWHW67DO%2B91HzQr4%2FgsF6LbXiRDihFIWxY2xSBDpelLOC4iSEFSFiNPczElWNfdhi6me0UXxqQ%2BdJij5ehnfbKjNY9BRXYlPAuNiQRrJAMhB693E%2FYIqIRX8DqgdKbe%2BDURvfY25%2BgA%2BZOnvvgroNZ8uDX%2BrS4zbiraQ35ormSbI1dc7uvFNSCJeJwgABUcJws9mRHkhyGj9r%2FeV8r8JN40TnFcUYzT38q7XeOj93V2upcQqOt2X2J9kUSP%2BBchJxTH9Bp%2FQAeWdjVzJmWjH%2FTQAUy%2FfiwdahnnbXiOYW0qMGETFgCYEzYLyD9%2BD8vQp30lkmuGRIlHom1f9jzJ6J%2Bg54EmrmVcxEMIHQjL0GOqUB7GR1YPKdLZJFejvXiF3IabOSpjwhECObSLWTdh8naEqpHJ4q8FkriCJIXHgBmx7ta7HQrKsCyDkFg3n4EkyjTMkOeydYUxgCXg7L2UiNR4DdfJNx6nOOxorXlMjbd0%2BWUoBOdmXSl2apWkQ5RUCEYhHATUnmhmL1mx8cg77esOj6su6juC9PWO3jnd1swkUho0901u%2FiurhTuKNJYY%2B6irW7IMC%2F&X-Amz-Signature=226da6e2b0a32926417a6a6e9b5fc3e61bf7271088292dca22438769a460d892&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCYNKPID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDtkvjDUGuNPCIWj3sj50DJaRiDeiuBh2ZmSt7STRag2QIgX1RBO1T%2FHEYKPDFPfegao3RRmOggjXafOvzmU6Mknuoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOQDCvNKcXeqpHs4HCrcAzLaZw1mts09lyvVaOx6%2B1qstExq8GU6bOA8RjaoSqYAcKQtRHqNd0hr56c4YRcbFuPKI%2BalrJLcxukqXqvbgUjIMALQkGocIjooXA1ucR9C9fC2a8oY%2FAisDIljyr3CtdG604o7IuOb8pojOI2Nz1P1e81Q08KFkIE5fZJa6WlonKVtTO8fGCk%2BC81HXb3g0sJqUqr%2FeDpOI8vILh2SsvO%2B8EJU2b%2F9bGjngCO%2B5S744LaR7gm2EF%2F6nhf6R37Y8ZyFi5CEa%2FcbCNLR73Nyu5Mx7PFcWHW67DO%2B91HzQr4%2FgsF6LbXiRDihFIWxY2xSBDpelLOC4iSEFSFiNPczElWNfdhi6me0UXxqQ%2BdJij5ehnfbKjNY9BRXYlPAuNiQRrJAMhB693E%2FYIqIRX8DqgdKbe%2BDURvfY25%2BgA%2BZOnvvgroNZ8uDX%2BrS4zbiraQ35ormSbI1dc7uvFNSCJeJwgABUcJws9mRHkhyGj9r%2FeV8r8JN40TnFcUYzT38q7XeOj93V2upcQqOt2X2J9kUSP%2BBchJxTH9Bp%2FQAeWdjVzJmWjH%2FTQAUy%2FfiwdahnnbXiOYW0qMGETFgCYEzYLyD9%2BD8vQp30lkmuGRIlHom1f9jzJ6J%2Bg54EmrmVcxEMIHQjL0GOqUB7GR1YPKdLZJFejvXiF3IabOSpjwhECObSLWTdh8naEqpHJ4q8FkriCJIXHgBmx7ta7HQrKsCyDkFg3n4EkyjTMkOeydYUxgCXg7L2UiNR4DdfJNx6nOOxorXlMjbd0%2BWUoBOdmXSl2apWkQ5RUCEYhHATUnmhmL1mx8cg77esOj6su6juC9PWO3jnd1swkUho0901u%2FiurhTuKNJYY%2B6irW7IMC%2F&X-Amz-Signature=432c8a89d2747dd93d1041be9b744ac505c54bb4a7d382edd9814d62da976419&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWZFGM4B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQC%2BY1%2Fq7AZXsVyxofBpUsxY9KgbTpAej7tsqpLaUAggCAIhAPxwDdjyUKM4Z4O%2FTftvQjiNEVNYYEpnIrhIsogRrDQgKv8DCEIQABoMNjM3NDIzMTgzODA1IgzRNP%2BbQ52ZPW%2FUGbgq3AMKsUvstoRFiiysbcLnU5T8mUayxcGjRtrIbG5EGGdp8xG7lVy1nhk5L7Bg9EiszQAv6s8oPE3r%2FFEUNeBRIz60D5NDkfdEyIlP%2FWLjNrvoDhzezzGdSSMpqILxohm5pnFnOIOAWD8REpmM4HAH0k0zCIJQK3zioDZUgYonYkchzlkj5NW1vA88WJJk3Pemi3AHdmhbt6OA8T%2F5ScF7lYPZc6mkjGXqvD4JVXnQaUoDxaPZRbg0muGsDeiAnDXwIUKqXU3IgVk01CeGlHRLpy8w3PvfGgPN2ElbHwByvAw5Irr2hLvrfojEvBhWVOVbo8GmTPtS9egAnD19LCKxN5SS2Bam1hvx8FDDCt5HgCsSGclHeuNwXy7RZS2yCCxvWchb9dsSGtqpm8nec2pxS379jN3OBXONE5DLhKSMW%2BsNTeqXbIADy1OngLrYiL%2FGl%2F8HJfTIcG8IoPfCAC623X%2FHGCuQ9fMPo3FkltwrH6FAnK9nlPdCzWswQXzT5GLYq%2BigA1oNV1METwhbSu6p5h7ACMJg69unaEoi9USPT73FdzgpptqxcA3cE8JLXUFFLy%2BRn%2Fl8CHMrfrquWWb5ciqXMcfHUCJQCfOCnz9wkc5n%2BRQjKI0zm6MrxPv9bTCEz4y9BjqkAQAcNzl32oVrz68dlZ2eIAuZ%2F8MJmOvMh7BqiMHHxG6nvhmfMrshlyaEbqjA6IYJKDlEwmWJDjO1EtjldKIgGMTrtLRBL9P29daOQBquU%2Brrn6Vu8UUm0HlYWwylnL7W5Zwr7tkR7QO%2FigrH4c6S2J%2F%2BD3dA40Dn6KzLEkWgcyMaQgABoeDAWEAQVT8niXOrrUvX8u1dl7qxXpAJeBf3tn2zmCJw&X-Amz-Signature=9693dde01bafa655768883f3e35fadedbc17188e35304a56008d6b1c965ce565&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Q2N4BW7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCit1GCtsZQbxojLbLBYlmoTkmGy9EbmLAXQOkPm%2FEHfAIgfB9C5P6DWvn%2FU44KGnScdM%2FmaPVsOGV9LgJlTFqLuMUq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDALtXNLzHPuN58LkjSrcA6Kuu4cCTga8Y4f51g8hKxIfrMv%2Bm3AciH4V1N84R2MJDHbDYOgR%2FYC1%2BC0%2BHb0Iou1%2BOjDTpgPa9N1etO9ZC5DzyOdnZl0hL%2B1MeTRTwELwRVYFDs6xAhRyyIIj3r9o0%2F%2FpXAX7DZo6e2SOt7hejZlxekuu0iCKYLX0c%2FUHyOQJ8b0NU6PwTgSbBtbBIocH2fucCBEF25kBz4VOUadlByjcHjXnpqyQk7ztNyZ2bk%2BXW7s%2FqsfiwUURB3qPyR3g9rnmGQav1mvIIiwuUJJ%2BWrj0BEP58yP2yJ8G0m06RwANFdUDNqy5pYmOIhVuc6YRaIS8GQ0mqjprvTd8xgdX7gDVBwY82a%2BbuQgnWOH0Vlm38rM3Im28Dzgu9dyMgLa3f0BeTH7pm72SpxN%2FumbZG7hT1WdP%2B%2Fq%2B2zYNDE%2BTTn3avfxJd1Jg5IcT7c%2BgCBC9DbFyG%2BHVxSIWNE%2BFDWm8dSY%2FNZTbrsitPIhCkfBO5Vrwjf4SM2VVRyeeFwefC60BGk6r3JGbbXkPv%2B%2FUi%2B066FOLvNh%2FomBjDFoqMnUhD9RfMAahBL0uPRB6bU97o5xkOa40X3DEGDn2kLAe2SHGlZW9rzTGWWQYLTQE8izC6VyM7YtVKAZ24cxK0PclMJ%2FPjL0GOqUBtRPsLYKfj8TzYUighcDhqgYYX1TOEFdxOY9xtWxvlGCLOxKTcz3udxySnFNr1s4rKbzZat2XyXFAhh1dpqIpAgIemduh%2BczrrLPf1niF8eKFfLFVkxBhV2yhSBLxwk%2FiBbfELdPjDAm%2FXdQ3azpmQ0wyVSogJZT6d9rTTiHaBAcP97vOK6onfwWqlXdyFtOFVhdv6FzcSdfRiNW3jaMZ2YPdph7M&X-Amz-Signature=2336a1c1a5670f07614d95c2272063a7fe2dc6379ee3a0be814215669244c0ea&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMEUI62W%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIBt%2FxmICMlJ58bP5I0IObuwFHllF2vtLYoJ94I2KiotLAiEAvgLOeFUy8X1kmOLjjmPn%2Fjk2b3dTZkuAkVaUhWOsiVYq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKaWLcijtVLoEw2sxircA4JORB%2BBDIVC2GLcVGdBGCWNarkf5Lj65877Ty%2FUh51Pm6DE7EwjyryNYptI%2Fm278MeQqKMFY%2FomhsmyT05lElqzDWX6dTplZWq2FCbdyFj3tX6U6QbWEH6d%2FKB6hEkkpuLt3uwReU6zgutcF515MtkDHalj6mktHFvCUcg2h%2Fuo1me6LP8qm9DLdYfgBnP9efQBgooJPBk0wO%2FqgHSninR7%2FztaQenMUBXvmpPGx0NOoNBYeu9EAGozAD2%2FwVe6NbsBrmD56cdbgOPyT9gyXc85aHXzCqzX71%2BZKbYYDGaOmf1vZK6ZpOd38dBHGnGRZic6xmdqvRgUQLi6TlcTi2roUSdoO%2BmLa9q1svq0mkexs7ZSWMRAI5jew49dqCy3SfvdR897UKcHAsxnaY8kjzYMmMu5c0NfmUVaJBKqi8EVAXPPPaibGOydvReBFc1iQN2Q8ogXPwdhFOmgZP8AFBKkpGl4dt9YtYqyHM6CltAE5LFAbkLpCo8Xpc1q7QV9bMESkAg1DTvgBig2%2B%2FLkR0T7dhbR0gYX7ESHEnndlMPORh6JDDXNc%2FLc4Blo1J6BAkH5eLCpYHf7A983Xugf7xeHgtYLUzGwcinH%2FYgDVlfSq3SDxeS0Ug21RGWaMKTPjL0GOqUBolHGG07fj2qdVK%2FtRayyLMsApw8%2FwdmrJvUTc41JshYm47vql3Tjfg02MjF%2FlUPAmTZSmQYCJkQisZTG412UQ5E4AyvHlSmqySsy3uiYnw0qErywhDcCA%2FefPJzET1TQLsMjxzcTPyVz4q8nHs8R%2BB3AEIHJcF34CbqNWJhRFxA8eIkwj24AOhZLNSCzl7N%2F9EHN7gYdr2uvyUK%2Bs%2FwLFVc1SEEy&X-Amz-Signature=50d167db76d46d6df0120c78e0bd1f64d7cdafd660e6fd3da06c14348a591868&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ADQG3Q6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIDWtzWLdJFcop8Fezhcugtpy%2Fm6fostahCv6crDhXWg2AiEAue3lyWPgx9b%2BmmKqKNrR4pQvGDojcXGCZzmhS7TBP68q%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDDbg5825pFDjIXx64CrcAwQLVbU7H9oed7f%2FIMNlFOlpioHs1LHmm9BRHkFRpzZhupUxfNCvYSRcobdFrwyqJjYKtV3yQy8R7IMkN9EDAFXsbVHTiK7R9q42G0b21TRMud0xLkLg3TT462x62QFlfXO2AoK1mnm%2F0prdmRW3uInel4bcPZ5JcLRgSersA1TRPhayJerOUp9nbvpz0eEDrjDbPygSXvBUVx8ooVQFDzP3o%2Bl4Hir7sgtXGoQ8aajFCR2ewxyJjMeVzQ2nNsDErOopW%2BZgojmpWd5kmtguLSvkhrcCxkSDljNifGKbQZZ471zV4HEAbsqpf8bSEZLCm967YH0Qla2jD5cFGurXwhMbYAhd3C4tIY6mntFXRnKa8HmlovxOlsW8ReoD0EDbuJ5mmAsd5A7q1n0i3RXhFiKiuYQrEg88yNKxZIiQXLbFS%2BbiOpSrptk41aXUfb7pL1Hlc3eeg%2F4QYs5E0U%2BEWFQFkQSgkYLSX%2B%2FcrCgoo6TzbBq37rs78JdEpXs8N1mxcMP6n6s5S3h%2FBKjDbzhcE%2F8RnQhbMI7Vcupu40v9DJ069EnDGjyvJCWEE5m68uQTZXegH13RQlyjbL8Kvx0Hzw%2B6raZTXoX8WVndVtaJk6%2B3vRLj%2BJIymRtRCdsiMPvOjL0GOqUB7WQNuFlQFCPeQNpQB894uhxT4p8QglMonqQPrNTIoKOi%2F6ItTkSrYsb7%2F%2FGsjbyjNYZafygU8T2mxG93GskIcrwVW6XsXqIP4HOGoUBTJqSlmH9nv7LjaV8QUqXvpVKFCpTuXeHJns6dJLtlU%2Fona7ZnCgYU2zRTLxoQD76Ca%2B5kVVd6m%2BTlhYUdvpfleWAO2FmlPbmoj5Oefie9Yqa4OA%2FKN5DX&X-Amz-Signature=832fc4c6688861b96aa9c15f5ec0ba99ca63eb109f26432dd18a5c8c9e596f19&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ADQG3Q6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIDWtzWLdJFcop8Fezhcugtpy%2Fm6fostahCv6crDhXWg2AiEAue3lyWPgx9b%2BmmKqKNrR4pQvGDojcXGCZzmhS7TBP68q%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDDbg5825pFDjIXx64CrcAwQLVbU7H9oed7f%2FIMNlFOlpioHs1LHmm9BRHkFRpzZhupUxfNCvYSRcobdFrwyqJjYKtV3yQy8R7IMkN9EDAFXsbVHTiK7R9q42G0b21TRMud0xLkLg3TT462x62QFlfXO2AoK1mnm%2F0prdmRW3uInel4bcPZ5JcLRgSersA1TRPhayJerOUp9nbvpz0eEDrjDbPygSXvBUVx8ooVQFDzP3o%2Bl4Hir7sgtXGoQ8aajFCR2ewxyJjMeVzQ2nNsDErOopW%2BZgojmpWd5kmtguLSvkhrcCxkSDljNifGKbQZZ471zV4HEAbsqpf8bSEZLCm967YH0Qla2jD5cFGurXwhMbYAhd3C4tIY6mntFXRnKa8HmlovxOlsW8ReoD0EDbuJ5mmAsd5A7q1n0i3RXhFiKiuYQrEg88yNKxZIiQXLbFS%2BbiOpSrptk41aXUfb7pL1Hlc3eeg%2F4QYs5E0U%2BEWFQFkQSgkYLSX%2B%2FcrCgoo6TzbBq37rs78JdEpXs8N1mxcMP6n6s5S3h%2FBKjDbzhcE%2F8RnQhbMI7Vcupu40v9DJ069EnDGjyvJCWEE5m68uQTZXegH13RQlyjbL8Kvx0Hzw%2B6raZTXoX8WVndVtaJk6%2B3vRLj%2BJIymRtRCdsiMPvOjL0GOqUB7WQNuFlQFCPeQNpQB894uhxT4p8QglMonqQPrNTIoKOi%2F6ItTkSrYsb7%2F%2FGsjbyjNYZafygU8T2mxG93GskIcrwVW6XsXqIP4HOGoUBTJqSlmH9nv7LjaV8QUqXvpVKFCpTuXeHJns6dJLtlU%2Fona7ZnCgYU2zRTLxoQD76Ca%2B5kVVd6m%2BTlhYUdvpfleWAO2FmlPbmoj5Oefie9Yqa4OA%2FKN5DX&X-Amz-Signature=a01e59e7eb4a7c011b351793eae2b81193ac3dddcf108b8dddeb1fa171a19a35&X-Amz-SignedHeaders=host&x-id=GetObject)

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
