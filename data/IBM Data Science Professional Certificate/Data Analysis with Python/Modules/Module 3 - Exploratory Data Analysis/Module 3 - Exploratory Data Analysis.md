

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VGHB5HW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIANH124KXHcspyHKfNoNaRlatdWIkXES9WVgzWHeS6QWAiAZLPqBZd0BWCQnbNvCi8KsrlCgGEhLfuTnznHF74Wduyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMqaei%2BX7Hq6uA8qjTKtwD1VIjU1oGt88KS2NVGYuUf181eOJw9wWx27qEIlIP1qTuR7SXNDNI4k8duHfQTz6WsKWxsxMMo6Ol%2Bd0zDBqHmb4Aik6eyGpAuGqafrFwuMIvdk8E%2Fqqw8tktAk0HCaHnCuB04er9Ts%2BXGmf%2Frc5M6DpnnO5B9%2FWenOM85LG0pjaKLIJV%2FmWKnpK%2BDatv8rrMDyE0jp3udKf5%2BMBJND8ToIgNiPVWreZwL7hur6WXV4pXCtZ15peyTJSQ0z7zou9jG0pNu3F%2BMx1kRsTnBHmDn%2BqoVuXB3N9B3O7oZZaUcmryPZu6j5SCCgvx2VYO1wnBlWn6HgLnfepxwRpXjhARhncZ2t9Ne0K%2BA5gZv1ihoU28jfM3lvF6Ckekn7iA2j78JBp4zUgmEAwaPN9tHIJUeDBMB5ckVCrr9H2CSDz9NOg6yG%2B030H%2F3Plcs63bI08bTwhI3EE8b0iO%2FpbE75gQNQbN7qegatW%2B8IdTOJXk8YHADDQk%2BOttTAeNaYa7LQL%2FcZQ2JnKZ%2B%2FcJqLGTMTNloPKngxwDMjnG1q%2Fw2aSg2XBIsUOrjSRy1yBa3dXPmKJ02dON%2B5bvpW2Ywpjs2AD04po9OLGo6xR6CeFigsTWOqpAx9NZyMwSumG4N%2Bowlf6ZvQY6pgHDeTQAtiBQa7kLs%2FOyHjpLOonZZpDZPtwqIIe7x3E%2BNZz%2BAGGPUEoMKAdVnZdBnQB7rOn2l3kYlqqT1G6WN%2BRNH5M2zs2vvSfXfrWd6d1FdQIhDOYAbmAhh8rgPmnvcyt3U6hc4fvi3ge9tgbEaOz5R3sHfP1oSWG1ApAdspLH802UZAnzGskIT9y98%2FC%2FYOwbvg7hnzhaLnuF95%2BkyXiLsXv56rJm&X-Amz-Signature=9b1fd0d127bd63081c2601c9b48a9e0efa69ffbf203b1fef329fac55fb879520&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VGHB5HW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIANH124KXHcspyHKfNoNaRlatdWIkXES9WVgzWHeS6QWAiAZLPqBZd0BWCQnbNvCi8KsrlCgGEhLfuTnznHF74Wduyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMqaei%2BX7Hq6uA8qjTKtwD1VIjU1oGt88KS2NVGYuUf181eOJw9wWx27qEIlIP1qTuR7SXNDNI4k8duHfQTz6WsKWxsxMMo6Ol%2Bd0zDBqHmb4Aik6eyGpAuGqafrFwuMIvdk8E%2Fqqw8tktAk0HCaHnCuB04er9Ts%2BXGmf%2Frc5M6DpnnO5B9%2FWenOM85LG0pjaKLIJV%2FmWKnpK%2BDatv8rrMDyE0jp3udKf5%2BMBJND8ToIgNiPVWreZwL7hur6WXV4pXCtZ15peyTJSQ0z7zou9jG0pNu3F%2BMx1kRsTnBHmDn%2BqoVuXB3N9B3O7oZZaUcmryPZu6j5SCCgvx2VYO1wnBlWn6HgLnfepxwRpXjhARhncZ2t9Ne0K%2BA5gZv1ihoU28jfM3lvF6Ckekn7iA2j78JBp4zUgmEAwaPN9tHIJUeDBMB5ckVCrr9H2CSDz9NOg6yG%2B030H%2F3Plcs63bI08bTwhI3EE8b0iO%2FpbE75gQNQbN7qegatW%2B8IdTOJXk8YHADDQk%2BOttTAeNaYa7LQL%2FcZQ2JnKZ%2B%2FcJqLGTMTNloPKngxwDMjnG1q%2Fw2aSg2XBIsUOrjSRy1yBa3dXPmKJ02dON%2B5bvpW2Ywpjs2AD04po9OLGo6xR6CeFigsTWOqpAx9NZyMwSumG4N%2Bowlf6ZvQY6pgHDeTQAtiBQa7kLs%2FOyHjpLOonZZpDZPtwqIIe7x3E%2BNZz%2BAGGPUEoMKAdVnZdBnQB7rOn2l3kYlqqT1G6WN%2BRNH5M2zs2vvSfXfrWd6d1FdQIhDOYAbmAhh8rgPmnvcyt3U6hc4fvi3ge9tgbEaOz5R3sHfP1oSWG1ApAdspLH802UZAnzGskIT9y98%2FC%2FYOwbvg7hnzhaLnuF95%2BkyXiLsXv56rJm&X-Amz-Signature=a5d87b97c01c92d8155b9998ca26d82d788cc8dfd32a630978bcd67f5fee7219&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VGHB5HW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIANH124KXHcspyHKfNoNaRlatdWIkXES9WVgzWHeS6QWAiAZLPqBZd0BWCQnbNvCi8KsrlCgGEhLfuTnznHF74Wduyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMqaei%2BX7Hq6uA8qjTKtwD1VIjU1oGt88KS2NVGYuUf181eOJw9wWx27qEIlIP1qTuR7SXNDNI4k8duHfQTz6WsKWxsxMMo6Ol%2Bd0zDBqHmb4Aik6eyGpAuGqafrFwuMIvdk8E%2Fqqw8tktAk0HCaHnCuB04er9Ts%2BXGmf%2Frc5M6DpnnO5B9%2FWenOM85LG0pjaKLIJV%2FmWKnpK%2BDatv8rrMDyE0jp3udKf5%2BMBJND8ToIgNiPVWreZwL7hur6WXV4pXCtZ15peyTJSQ0z7zou9jG0pNu3F%2BMx1kRsTnBHmDn%2BqoVuXB3N9B3O7oZZaUcmryPZu6j5SCCgvx2VYO1wnBlWn6HgLnfepxwRpXjhARhncZ2t9Ne0K%2BA5gZv1ihoU28jfM3lvF6Ckekn7iA2j78JBp4zUgmEAwaPN9tHIJUeDBMB5ckVCrr9H2CSDz9NOg6yG%2B030H%2F3Plcs63bI08bTwhI3EE8b0iO%2FpbE75gQNQbN7qegatW%2B8IdTOJXk8YHADDQk%2BOttTAeNaYa7LQL%2FcZQ2JnKZ%2B%2FcJqLGTMTNloPKngxwDMjnG1q%2Fw2aSg2XBIsUOrjSRy1yBa3dXPmKJ02dON%2B5bvpW2Ywpjs2AD04po9OLGo6xR6CeFigsTWOqpAx9NZyMwSumG4N%2Bowlf6ZvQY6pgHDeTQAtiBQa7kLs%2FOyHjpLOonZZpDZPtwqIIe7x3E%2BNZz%2BAGGPUEoMKAdVnZdBnQB7rOn2l3kYlqqT1G6WN%2BRNH5M2zs2vvSfXfrWd6d1FdQIhDOYAbmAhh8rgPmnvcyt3U6hc4fvi3ge9tgbEaOz5R3sHfP1oSWG1ApAdspLH802UZAnzGskIT9y98%2FC%2FYOwbvg7hnzhaLnuF95%2BkyXiLsXv56rJm&X-Amz-Signature=407de3ab36bc24d038f96240ae69d49c0e417e5f239c5a80a5b0f8c670009fce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IFSSKDI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFjrPiWdPbuqvazLoleolWENTOT5u1R9b7sX8EKD6AG0AiEAh39j2DpJLzad1aLPeqPp1VwekuyW5QDih%2FDItNQCaBsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDBy0EfUSk%2BhQmtAucyrcA6KICx0WS42QexUII2ZFSPvdMeiY9y8vBVm2NhYCeKKacRdkbEDRcmsVMkNtzHRydF5%2FVM4VuCP1pHIBemX2491uTNoAjG6EwqSTC0k4FjcMVZrt6Q%2FM0l%2BYIUl0Lu%2BrDGdre6ke8b4s%2BAuS06%2Bzu77sMzdbgoENhhh9ckZsV62mLdW6AUBD4pm5AvWvtdiHoJNzyXFtibGliEf70prEtStL%2BycE4ygfwyAEQ3dFlLdGl5Br0N2MnKchX9cw7a%2Bpl9jaDzo3f%2FwJ6HBLet9FEhoj3SJ6gMvNhdyf1ocRlnbJYdQRcQDxj7g%2B7sPNUMFPdjtIy8oa1YHLnMAZngGzalYeR%2BZJ%2FAb6JsK7qjQQRXu9nruoE5AFh%2BmaRvBdkGBGV7bc4BIH40z3NN09NEr06tp0YOWxbOBRAm8Ryrqw6DYkBeIGM3uREo%2Be%2FzaG0INTXmXPBEwV0Qc2QC0vdUTYOWsG%2BPtKysJeICkRRuGxNrvEvQmoE5jGYVA4SrkicgzEgekCENzxiB3pjlSU%2BZKVEpGm00XJtqo2J7%2BkoOK57c6e3Uyo7SA4FOfqpJVdcbZMHxe5%2Bnx5IgF5u4bXMHbLQA8xTKO6fFDELN7n6rwsjKvogilkXxEUbp0WuYZoMN3%2Bmb0GOqUB0neKLfCrToe25TCYvPCWEMj2tuQgveR32vwyB0%2BANKzDjg4LdMyTtgvDJD1RFJKxRIFnhCbyM1w9i8SvHw7SZ4DDmUvF0zXvWkOI88dwzAM%2B5dat9x3BRAQEBejFVtLPUy3TDgqwmhp2%2BClDEiPXYmLLAWwFj8ILjepbveIM1YG%2F8zXFbJQ9YTNg7sc4%2B%2BUOmF9S4d2b2cIemKBCoguw0kC8y1mV&X-Amz-Signature=3b3a348ae4fe2aab9c1f474f9b9686e78f8a3a52f8cd9a26bccfb73e2613b581&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IFSSKDI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFjrPiWdPbuqvazLoleolWENTOT5u1R9b7sX8EKD6AG0AiEAh39j2DpJLzad1aLPeqPp1VwekuyW5QDih%2FDItNQCaBsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDBy0EfUSk%2BhQmtAucyrcA6KICx0WS42QexUII2ZFSPvdMeiY9y8vBVm2NhYCeKKacRdkbEDRcmsVMkNtzHRydF5%2FVM4VuCP1pHIBemX2491uTNoAjG6EwqSTC0k4FjcMVZrt6Q%2FM0l%2BYIUl0Lu%2BrDGdre6ke8b4s%2BAuS06%2Bzu77sMzdbgoENhhh9ckZsV62mLdW6AUBD4pm5AvWvtdiHoJNzyXFtibGliEf70prEtStL%2BycE4ygfwyAEQ3dFlLdGl5Br0N2MnKchX9cw7a%2Bpl9jaDzo3f%2FwJ6HBLet9FEhoj3SJ6gMvNhdyf1ocRlnbJYdQRcQDxj7g%2B7sPNUMFPdjtIy8oa1YHLnMAZngGzalYeR%2BZJ%2FAb6JsK7qjQQRXu9nruoE5AFh%2BmaRvBdkGBGV7bc4BIH40z3NN09NEr06tp0YOWxbOBRAm8Ryrqw6DYkBeIGM3uREo%2Be%2FzaG0INTXmXPBEwV0Qc2QC0vdUTYOWsG%2BPtKysJeICkRRuGxNrvEvQmoE5jGYVA4SrkicgzEgekCENzxiB3pjlSU%2BZKVEpGm00XJtqo2J7%2BkoOK57c6e3Uyo7SA4FOfqpJVdcbZMHxe5%2Bnx5IgF5u4bXMHbLQA8xTKO6fFDELN7n6rwsjKvogilkXxEUbp0WuYZoMN3%2Bmb0GOqUB0neKLfCrToe25TCYvPCWEMj2tuQgveR32vwyB0%2BANKzDjg4LdMyTtgvDJD1RFJKxRIFnhCbyM1w9i8SvHw7SZ4DDmUvF0zXvWkOI88dwzAM%2B5dat9x3BRAQEBejFVtLPUy3TDgqwmhp2%2BClDEiPXYmLLAWwFj8ILjepbveIM1YG%2F8zXFbJQ9YTNg7sc4%2B%2BUOmF9S4d2b2cIemKBCoguw0kC8y1mV&X-Amz-Signature=fad5af4255547690f4df32fefa6d634e4e0804aaaecb8e9726d1862727dc9467&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IFSSKDI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFjrPiWdPbuqvazLoleolWENTOT5u1R9b7sX8EKD6AG0AiEAh39j2DpJLzad1aLPeqPp1VwekuyW5QDih%2FDItNQCaBsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDBy0EfUSk%2BhQmtAucyrcA6KICx0WS42QexUII2ZFSPvdMeiY9y8vBVm2NhYCeKKacRdkbEDRcmsVMkNtzHRydF5%2FVM4VuCP1pHIBemX2491uTNoAjG6EwqSTC0k4FjcMVZrt6Q%2FM0l%2BYIUl0Lu%2BrDGdre6ke8b4s%2BAuS06%2Bzu77sMzdbgoENhhh9ckZsV62mLdW6AUBD4pm5AvWvtdiHoJNzyXFtibGliEf70prEtStL%2BycE4ygfwyAEQ3dFlLdGl5Br0N2MnKchX9cw7a%2Bpl9jaDzo3f%2FwJ6HBLet9FEhoj3SJ6gMvNhdyf1ocRlnbJYdQRcQDxj7g%2B7sPNUMFPdjtIy8oa1YHLnMAZngGzalYeR%2BZJ%2FAb6JsK7qjQQRXu9nruoE5AFh%2BmaRvBdkGBGV7bc4BIH40z3NN09NEr06tp0YOWxbOBRAm8Ryrqw6DYkBeIGM3uREo%2Be%2FzaG0INTXmXPBEwV0Qc2QC0vdUTYOWsG%2BPtKysJeICkRRuGxNrvEvQmoE5jGYVA4SrkicgzEgekCENzxiB3pjlSU%2BZKVEpGm00XJtqo2J7%2BkoOK57c6e3Uyo7SA4FOfqpJVdcbZMHxe5%2Bnx5IgF5u4bXMHbLQA8xTKO6fFDELN7n6rwsjKvogilkXxEUbp0WuYZoMN3%2Bmb0GOqUB0neKLfCrToe25TCYvPCWEMj2tuQgveR32vwyB0%2BANKzDjg4LdMyTtgvDJD1RFJKxRIFnhCbyM1w9i8SvHw7SZ4DDmUvF0zXvWkOI88dwzAM%2B5dat9x3BRAQEBejFVtLPUy3TDgqwmhp2%2BClDEiPXYmLLAWwFj8ILjepbveIM1YG%2F8zXFbJQ9YTNg7sc4%2B%2BUOmF9S4d2b2cIemKBCoguw0kC8y1mV&X-Amz-Signature=3d02eff57b5bc60d1410d41a0a51a15459281175d23cb0549e9229a51c7411cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IFSSKDI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFjrPiWdPbuqvazLoleolWENTOT5u1R9b7sX8EKD6AG0AiEAh39j2DpJLzad1aLPeqPp1VwekuyW5QDih%2FDItNQCaBsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDBy0EfUSk%2BhQmtAucyrcA6KICx0WS42QexUII2ZFSPvdMeiY9y8vBVm2NhYCeKKacRdkbEDRcmsVMkNtzHRydF5%2FVM4VuCP1pHIBemX2491uTNoAjG6EwqSTC0k4FjcMVZrt6Q%2FM0l%2BYIUl0Lu%2BrDGdre6ke8b4s%2BAuS06%2Bzu77sMzdbgoENhhh9ckZsV62mLdW6AUBD4pm5AvWvtdiHoJNzyXFtibGliEf70prEtStL%2BycE4ygfwyAEQ3dFlLdGl5Br0N2MnKchX9cw7a%2Bpl9jaDzo3f%2FwJ6HBLet9FEhoj3SJ6gMvNhdyf1ocRlnbJYdQRcQDxj7g%2B7sPNUMFPdjtIy8oa1YHLnMAZngGzalYeR%2BZJ%2FAb6JsK7qjQQRXu9nruoE5AFh%2BmaRvBdkGBGV7bc4BIH40z3NN09NEr06tp0YOWxbOBRAm8Ryrqw6DYkBeIGM3uREo%2Be%2FzaG0INTXmXPBEwV0Qc2QC0vdUTYOWsG%2BPtKysJeICkRRuGxNrvEvQmoE5jGYVA4SrkicgzEgekCENzxiB3pjlSU%2BZKVEpGm00XJtqo2J7%2BkoOK57c6e3Uyo7SA4FOfqpJVdcbZMHxe5%2Bnx5IgF5u4bXMHbLQA8xTKO6fFDELN7n6rwsjKvogilkXxEUbp0WuYZoMN3%2Bmb0GOqUB0neKLfCrToe25TCYvPCWEMj2tuQgveR32vwyB0%2BANKzDjg4LdMyTtgvDJD1RFJKxRIFnhCbyM1w9i8SvHw7SZ4DDmUvF0zXvWkOI88dwzAM%2B5dat9x3BRAQEBejFVtLPUy3TDgqwmhp2%2BClDEiPXYmLLAWwFj8ILjepbveIM1YG%2F8zXFbJQ9YTNg7sc4%2B%2BUOmF9S4d2b2cIemKBCoguw0kC8y1mV&X-Amz-Signature=36a79e864b36b92a516f1059ba1e22c0aef3db90f4b84b20ebeee264cfec9ce4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IFSSKDI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFjrPiWdPbuqvazLoleolWENTOT5u1R9b7sX8EKD6AG0AiEAh39j2DpJLzad1aLPeqPp1VwekuyW5QDih%2FDItNQCaBsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDBy0EfUSk%2BhQmtAucyrcA6KICx0WS42QexUII2ZFSPvdMeiY9y8vBVm2NhYCeKKacRdkbEDRcmsVMkNtzHRydF5%2FVM4VuCP1pHIBemX2491uTNoAjG6EwqSTC0k4FjcMVZrt6Q%2FM0l%2BYIUl0Lu%2BrDGdre6ke8b4s%2BAuS06%2Bzu77sMzdbgoENhhh9ckZsV62mLdW6AUBD4pm5AvWvtdiHoJNzyXFtibGliEf70prEtStL%2BycE4ygfwyAEQ3dFlLdGl5Br0N2MnKchX9cw7a%2Bpl9jaDzo3f%2FwJ6HBLet9FEhoj3SJ6gMvNhdyf1ocRlnbJYdQRcQDxj7g%2B7sPNUMFPdjtIy8oa1YHLnMAZngGzalYeR%2BZJ%2FAb6JsK7qjQQRXu9nruoE5AFh%2BmaRvBdkGBGV7bc4BIH40z3NN09NEr06tp0YOWxbOBRAm8Ryrqw6DYkBeIGM3uREo%2Be%2FzaG0INTXmXPBEwV0Qc2QC0vdUTYOWsG%2BPtKysJeICkRRuGxNrvEvQmoE5jGYVA4SrkicgzEgekCENzxiB3pjlSU%2BZKVEpGm00XJtqo2J7%2BkoOK57c6e3Uyo7SA4FOfqpJVdcbZMHxe5%2Bnx5IgF5u4bXMHbLQA8xTKO6fFDELN7n6rwsjKvogilkXxEUbp0WuYZoMN3%2Bmb0GOqUB0neKLfCrToe25TCYvPCWEMj2tuQgveR32vwyB0%2BANKzDjg4LdMyTtgvDJD1RFJKxRIFnhCbyM1w9i8SvHw7SZ4DDmUvF0zXvWkOI88dwzAM%2B5dat9x3BRAQEBejFVtLPUy3TDgqwmhp2%2BClDEiPXYmLLAWwFj8ILjepbveIM1YG%2F8zXFbJQ9YTNg7sc4%2B%2BUOmF9S4d2b2cIemKBCoguw0kC8y1mV&X-Amz-Signature=a075f3ec91efc7b1e55f700036721243c5235d588b30a4b710a0b535b279a1c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IFSSKDI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFjrPiWdPbuqvazLoleolWENTOT5u1R9b7sX8EKD6AG0AiEAh39j2DpJLzad1aLPeqPp1VwekuyW5QDih%2FDItNQCaBsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDBy0EfUSk%2BhQmtAucyrcA6KICx0WS42QexUII2ZFSPvdMeiY9y8vBVm2NhYCeKKacRdkbEDRcmsVMkNtzHRydF5%2FVM4VuCP1pHIBemX2491uTNoAjG6EwqSTC0k4FjcMVZrt6Q%2FM0l%2BYIUl0Lu%2BrDGdre6ke8b4s%2BAuS06%2Bzu77sMzdbgoENhhh9ckZsV62mLdW6AUBD4pm5AvWvtdiHoJNzyXFtibGliEf70prEtStL%2BycE4ygfwyAEQ3dFlLdGl5Br0N2MnKchX9cw7a%2Bpl9jaDzo3f%2FwJ6HBLet9FEhoj3SJ6gMvNhdyf1ocRlnbJYdQRcQDxj7g%2B7sPNUMFPdjtIy8oa1YHLnMAZngGzalYeR%2BZJ%2FAb6JsK7qjQQRXu9nruoE5AFh%2BmaRvBdkGBGV7bc4BIH40z3NN09NEr06tp0YOWxbOBRAm8Ryrqw6DYkBeIGM3uREo%2Be%2FzaG0INTXmXPBEwV0Qc2QC0vdUTYOWsG%2BPtKysJeICkRRuGxNrvEvQmoE5jGYVA4SrkicgzEgekCENzxiB3pjlSU%2BZKVEpGm00XJtqo2J7%2BkoOK57c6e3Uyo7SA4FOfqpJVdcbZMHxe5%2Bnx5IgF5u4bXMHbLQA8xTKO6fFDELN7n6rwsjKvogilkXxEUbp0WuYZoMN3%2Bmb0GOqUB0neKLfCrToe25TCYvPCWEMj2tuQgveR32vwyB0%2BANKzDjg4LdMyTtgvDJD1RFJKxRIFnhCbyM1w9i8SvHw7SZ4DDmUvF0zXvWkOI88dwzAM%2B5dat9x3BRAQEBejFVtLPUy3TDgqwmhp2%2BClDEiPXYmLLAWwFj8ILjepbveIM1YG%2F8zXFbJQ9YTNg7sc4%2B%2BUOmF9S4d2b2cIemKBCoguw0kC8y1mV&X-Amz-Signature=cb1337da1dcae169919bf5ec3798c0cb1c24078757ee48e752ef109aad78f74a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SYIBEUM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIEgOnEQ9ahPH5pY9NR4zPZ%2B7z7Trsbn7hnUaDG3VO1ymAiB9DYNutg8vpIiEPVGEoSfEFv4x%2BZwU3YeGRgR5rZBiSCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMYdzW2UMmxaavTBsTKtwDNVaXPjdG%2BRpEFWD7jfQ6L7L6L2Bh4U7fVrPNUDm%2B7IqbRQ5ZlYIzjtvR5na1E5HrxkBVZvbMAqrwnOXXhlm1UCj0ggrGFLms91BwG5%2FbxeaK%2F3xPeFgKEO5t18auG2VQi4T0bA9E3f0OaqQGgs8DxyP8Qcmi4IhF%2Fqd6aNXlHkT0D4N3R2oJqopbdJGN8%2Bn26qR90AEzYibvdNDKH8Ecx2fAX0TIoAv973TCva%2BGsvzhkbb0smi4l8%2Bj%2F6A3KnuAzntc3aXwc29%2FRpis9g86%2BB5%2Fq9vBE036fyL1kVpIEl0zckB7VFevZ1VDLqEN%2BM5w16aSH9S3N%2Fwex4ZFq46EQuP6%2FElh4bTPj1vuDINh%2FBfFZOG3UH%2BhLA9ALJc3WTOXE6mzkjorGjmffUtLYJq9NlGH5mVQ6gsXP6dufvyqShxlg4XhoUP1Tajl9%2F%2FNubkb%2Bz7cMQlYgz31MsiMmC2MbXy9MmUEQqEXehoB0MfFSdRElPT68e4nreg9EUSt9uxU1YYKG1sZAOc%2BuOcCA%2FdaFQkaSJcjZq2AAHo0YPHUwJ%2FCEN6VGlmeQDiPW%2Fgayeal2pGKZPiNBAXKGMJUvAY18P%2FFBI5qNe%2B6CxI0YKj0SxcIqaHQjNaPEacDmfsw3%2F6ZvQY6pgHF3fIHMcvnKP2OgAWjcKOnjS9r7Sm5oonMgX5dzzNxeK%2B2h%2FTWikDNT0LCkFy29GHrG%2FfyVM2HbtcvBUGcaVZzoljWbSXyi%2BO8QZ5CwT1pvIrVz9ojdU8iQwvpCVtOz9QP%2B6GsEYol4Wi%2B%2BNnJufQce4vZmdxWMrFC7sRH0IwlghVJSrfJEzfl0vREkss3qlBVdJUGcvCKYasckKYoxomgZuTQJ7cq&X-Amz-Signature=5948b1c74b989de575cb10b51ec711f47602a4d09e0699a022b7d5d49741254a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AA4CB5P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDV4727FO4baDNT3Rf3ou%2F0H%2BNxxy8EkSrDNLfGUQt9pgIhALR0qm1a8Mzu2Nd6ObnEjxTsvGRsFsMGAbRk%2BTAJpwAHKv8DCH8QABoMNjM3NDIzMTgzODA1IgySIJwlEcyzWWJ4TWMq3ANDE0Bbh0THnLrXeKl8pBcmaWLUpaN%2FL0Znu3iX3EGU2gDLKAmSqKsUKoWTq2VcHUiZxU8bOWHAJPS85Tpll2LccFSmUJSwg0%2FASsIpUGzNgb1gEInq5MrZzrpi9w4Tz9yrEpNJ5%2Bn0lTbLwg4skZldKRF4NdeJPnjYsAfqgZORknzS7cDp9OAHwYB1GtLoTyoWd9Yv1pTU2r8Cdma%2FYiNm9Z1u%2F8MqL892Te6DgOLnLkbuKjohiSgnYaymb3cR7K5iETa8l331l%2Fcjj5mSTMTVVNGGiCXeHdTIzj%2FXyflNlTsCSWAPMmEJbsCQw9Uz1yje8wC%2FNXnVARYdQmAx6rIEOUWTC0Huz9dwu6iKLk%2BFGFnEqmUAev0jdQn9ysY%2Bf1cEvJW%2B%2Bksrt9NVyNph0IZY5YWb32MM067TlLmM81AdAyKZKr6YfEWdgUabRRZ5fD5dS5aGNpidettHEcvowkcQJY%2F0qcLKI4%2F%2BvSVwAmdHq0qF1nPvwS2jWfL1vCiaKPK%2BI%2BX27sbBdic%2BngP%2B%2BE%2BNrXLPpsgPtcYkBmK7uu5Cdee1uqdB%2FkCaBSwcfi3W46fEkI8lh7vTsZa6OnsoOHUFKJHtlYqJHO301OeXBmtbLDOm6YVjkrXRCXxa5zD%2B%2Fpm9BjqkAdMLk96p%2FQSG5gIRsH7OgLPuLbT0s4Nt6d1kfk82W15N42Oto4ekkqSaW%2F2eBeJnVaSI1Ha1R%2BFDjXRaBrdI4daVTFS16KvtU5CnCTEKOWWbR7SvNSoP%2BK9CDobVIQs5ycn5Y6GRT7QjG%2FvLWIIEBeG95ix9UXN3nKHqF04ms2OgecHDZTXgarP0q314DJ%2FqhcjfwjVOQ8vwIOcVblCoCwBZf6Iv&X-Amz-Signature=19e5aa23af14093ad54d63b8a659c98323bef96be565a52cfac203b4c0dd2eb0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IFSSKDI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFjrPiWdPbuqvazLoleolWENTOT5u1R9b7sX8EKD6AG0AiEAh39j2DpJLzad1aLPeqPp1VwekuyW5QDih%2FDItNQCaBsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDBy0EfUSk%2BhQmtAucyrcA6KICx0WS42QexUII2ZFSPvdMeiY9y8vBVm2NhYCeKKacRdkbEDRcmsVMkNtzHRydF5%2FVM4VuCP1pHIBemX2491uTNoAjG6EwqSTC0k4FjcMVZrt6Q%2FM0l%2BYIUl0Lu%2BrDGdre6ke8b4s%2BAuS06%2Bzu77sMzdbgoENhhh9ckZsV62mLdW6AUBD4pm5AvWvtdiHoJNzyXFtibGliEf70prEtStL%2BycE4ygfwyAEQ3dFlLdGl5Br0N2MnKchX9cw7a%2Bpl9jaDzo3f%2FwJ6HBLet9FEhoj3SJ6gMvNhdyf1ocRlnbJYdQRcQDxj7g%2B7sPNUMFPdjtIy8oa1YHLnMAZngGzalYeR%2BZJ%2FAb6JsK7qjQQRXu9nruoE5AFh%2BmaRvBdkGBGV7bc4BIH40z3NN09NEr06tp0YOWxbOBRAm8Ryrqw6DYkBeIGM3uREo%2Be%2FzaG0INTXmXPBEwV0Qc2QC0vdUTYOWsG%2BPtKysJeICkRRuGxNrvEvQmoE5jGYVA4SrkicgzEgekCENzxiB3pjlSU%2BZKVEpGm00XJtqo2J7%2BkoOK57c6e3Uyo7SA4FOfqpJVdcbZMHxe5%2Bnx5IgF5u4bXMHbLQA8xTKO6fFDELN7n6rwsjKvogilkXxEUbp0WuYZoMN3%2Bmb0GOqUB0neKLfCrToe25TCYvPCWEMj2tuQgveR32vwyB0%2BANKzDjg4LdMyTtgvDJD1RFJKxRIFnhCbyM1w9i8SvHw7SZ4DDmUvF0zXvWkOI88dwzAM%2B5dat9x3BRAQEBejFVtLPUy3TDgqwmhp2%2BClDEiPXYmLLAWwFj8ILjepbveIM1YG%2F8zXFbJQ9YTNg7sc4%2B%2BUOmF9S4d2b2cIemKBCoguw0kC8y1mV&X-Amz-Signature=791583471bcd0eafc9d82e8c031eebc8f9c494ddb2e02ec94c8863b67c3962e0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IFSSKDI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFjrPiWdPbuqvazLoleolWENTOT5u1R9b7sX8EKD6AG0AiEAh39j2DpJLzad1aLPeqPp1VwekuyW5QDih%2FDItNQCaBsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDBy0EfUSk%2BhQmtAucyrcA6KICx0WS42QexUII2ZFSPvdMeiY9y8vBVm2NhYCeKKacRdkbEDRcmsVMkNtzHRydF5%2FVM4VuCP1pHIBemX2491uTNoAjG6EwqSTC0k4FjcMVZrt6Q%2FM0l%2BYIUl0Lu%2BrDGdre6ke8b4s%2BAuS06%2Bzu77sMzdbgoENhhh9ckZsV62mLdW6AUBD4pm5AvWvtdiHoJNzyXFtibGliEf70prEtStL%2BycE4ygfwyAEQ3dFlLdGl5Br0N2MnKchX9cw7a%2Bpl9jaDzo3f%2FwJ6HBLet9FEhoj3SJ6gMvNhdyf1ocRlnbJYdQRcQDxj7g%2B7sPNUMFPdjtIy8oa1YHLnMAZngGzalYeR%2BZJ%2FAb6JsK7qjQQRXu9nruoE5AFh%2BmaRvBdkGBGV7bc4BIH40z3NN09NEr06tp0YOWxbOBRAm8Ryrqw6DYkBeIGM3uREo%2Be%2FzaG0INTXmXPBEwV0Qc2QC0vdUTYOWsG%2BPtKysJeICkRRuGxNrvEvQmoE5jGYVA4SrkicgzEgekCENzxiB3pjlSU%2BZKVEpGm00XJtqo2J7%2BkoOK57c6e3Uyo7SA4FOfqpJVdcbZMHxe5%2Bnx5IgF5u4bXMHbLQA8xTKO6fFDELN7n6rwsjKvogilkXxEUbp0WuYZoMN3%2Bmb0GOqUB0neKLfCrToe25TCYvPCWEMj2tuQgveR32vwyB0%2BANKzDjg4LdMyTtgvDJD1RFJKxRIFnhCbyM1w9i8SvHw7SZ4DDmUvF0zXvWkOI88dwzAM%2B5dat9x3BRAQEBejFVtLPUy3TDgqwmhp2%2BClDEiPXYmLLAWwFj8ILjepbveIM1YG%2F8zXFbJQ9YTNg7sc4%2B%2BUOmF9S4d2b2cIemKBCoguw0kC8y1mV&X-Amz-Signature=371661616084fd9570b67ce664625adf220c838f20f59d253a3a5c0a0a937bc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IFSSKDI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFjrPiWdPbuqvazLoleolWENTOT5u1R9b7sX8EKD6AG0AiEAh39j2DpJLzad1aLPeqPp1VwekuyW5QDih%2FDItNQCaBsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDBy0EfUSk%2BhQmtAucyrcA6KICx0WS42QexUII2ZFSPvdMeiY9y8vBVm2NhYCeKKacRdkbEDRcmsVMkNtzHRydF5%2FVM4VuCP1pHIBemX2491uTNoAjG6EwqSTC0k4FjcMVZrt6Q%2FM0l%2BYIUl0Lu%2BrDGdre6ke8b4s%2BAuS06%2Bzu77sMzdbgoENhhh9ckZsV62mLdW6AUBD4pm5AvWvtdiHoJNzyXFtibGliEf70prEtStL%2BycE4ygfwyAEQ3dFlLdGl5Br0N2MnKchX9cw7a%2Bpl9jaDzo3f%2FwJ6HBLet9FEhoj3SJ6gMvNhdyf1ocRlnbJYdQRcQDxj7g%2B7sPNUMFPdjtIy8oa1YHLnMAZngGzalYeR%2BZJ%2FAb6JsK7qjQQRXu9nruoE5AFh%2BmaRvBdkGBGV7bc4BIH40z3NN09NEr06tp0YOWxbOBRAm8Ryrqw6DYkBeIGM3uREo%2Be%2FzaG0INTXmXPBEwV0Qc2QC0vdUTYOWsG%2BPtKysJeICkRRuGxNrvEvQmoE5jGYVA4SrkicgzEgekCENzxiB3pjlSU%2BZKVEpGm00XJtqo2J7%2BkoOK57c6e3Uyo7SA4FOfqpJVdcbZMHxe5%2Bnx5IgF5u4bXMHbLQA8xTKO6fFDELN7n6rwsjKvogilkXxEUbp0WuYZoMN3%2Bmb0GOqUB0neKLfCrToe25TCYvPCWEMj2tuQgveR32vwyB0%2BANKzDjg4LdMyTtgvDJD1RFJKxRIFnhCbyM1w9i8SvHw7SZ4DDmUvF0zXvWkOI88dwzAM%2B5dat9x3BRAQEBejFVtLPUy3TDgqwmhp2%2BClDEiPXYmLLAWwFj8ILjepbveIM1YG%2F8zXFbJQ9YTNg7sc4%2B%2BUOmF9S4d2b2cIemKBCoguw0kC8y1mV&X-Amz-Signature=4532ca7c96e21c4e757bc24896d78d2cdbf7672e4263452590254fd619f0ba0d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7YDTA6W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEht43tkWu47xfFZZNZKV3PfpTWlh7Gntcq8SndT2CHZAiEAx%2Fy1P0dxoHCUz6xiDz5gs4JfUXpXYgAvaxS0YudVeYMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFgdFH4nnN%2B%2B3O7QVircA5A0zZ3%2FlGORaODYn3nZBoLcKyiphy7%2FzTKAqY9QS6vQMcJI%2BCIHXEHctd8Eu9tsi1J%2FYAR86bebOf1BVmqbhcDUQM6XF64L2yKdrxgwmHLB%2Bs3CAbLnvyd5wXyYHOlQ9RFgN9bddGxM%2Bt5%2Fd0N%2F2SPZ1c%2BybpIipfFvEC30oWwqXqQlSJSF3Y8R7%2BL5yeVSxzp095vcZU5V5n5ioa7xKSWkYPdx9wBH5t7D40I6NcVofZCmZ8VLSaHUVmHehL359QIScAnYcKSYbMZ4zuynmRr0MvYAkbwRMxhoU0VvU6SK0LLbZw5XrniXrtH44WosH%2FiDCrs8eFElOOKBCqDJAYCpJYf6ZFK56JW2WSA67vJ39DofliffdCxmmCxUao3AZO2XFWfgyV0I3nBXn29f5vk70R1vwbpG8QWV5LaAiYxp7j0RLnYV6I%2BzA1lDWlA%2B7eymZRhfOVVqvjtU%2Fn3g7Cdl4F%2BSbRi76Hpdg5d9GYBgeFVLke%2BjIP59sdEAUninXpS5jh3pI6DxDmVDdvZ442WHNnBbFrJCuTZExXH1fkyVASJaxJz7oCaBl2KHaAbI20ttQzBBRo3n3Pt3vnTA%2FV56LlnaLooeT5CHWLTpz6qPc%2BLHUyia4H8WcaJlMLj%2Bmb0GOqUBrZCKaXXiSLLUzmnf2qfYjvtWdBzOqDUH0xWwGZ43Vx8V9bRlhbAfkbCN6Nn08eH3Mf7%2Fllr4xVxH4ZVnQ58rF6S8qDllfrMBYmRFn6wwHL%2BX0ViGu1NEtC4IaNI0VwRuPuN0JF%2Fvsob0K7zJ3S%2BTZkisQQOfZoT11xqTY2X6byugixLkKFVlWcjaZ9gV7hb9ih5RqMuffGfYXNz7oPEm3eQCFlXr&X-Amz-Signature=52e1c1185720073e39db9407ec9163f2251a95be451f27a86c399706d51b82a1&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XPOMDZ7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIAsyomWmjM%2Fd4PeplPjO7cx%2F8AXMI6CJ8QZYS3XDfDm6AiAwjnDF3EcamhggMc8jxPLq2NqLZLNVPykeeZAadFiXUSr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMuhhUaiLRY21P6UclKtwDJPHMchqCh7M5YIFex4Il6ZM%2FOzUGTYpXwQ94k0l0%2F31ziYCkn2q5a6C4Y2VoxW5yDrXpZzyc7GGSWDrhTGzWLhACMjp3VCb5CwING0T0evn4sl3tB9WEiaKxyy3tZ2%2FvhYxsORWVvYBvQNxQ6gljyTPZy8ZHwyytrypwnowh5NMTDeWlsisYD1w19rd5mE556hF9tiSHxvjWWmxRv3rUmZWaeOau92F%2BLRk3YihbY0uQ8E%2FN9XX2%2BLrsP%2BvQRlw%2Fld0vofvRQgXTUJ%2BP5maDp9LsGalFbmtKJMx1BjZ5KNqblRDNlEawO%2FA2sqze5yChVTyand2PJ5Oon9%2BgDoMn9HDMfIN7fPRsBaNHQY4uS0MlIVmtK5gLGIwAKMt%2BiormiWCVE9lXPzTopf8ZtAv5E%2B%2FTfyhvDq3dzLdG12yCbgrlXI8yvY59SeAeOLdTwL0EiUqlmJkR3%2F7if7K9RykbPcIGOos6tnrS1FiDxGtM7W5NOzPjB8g9oNWyOVlqo4kozifg3fT3dcG%2Bz6QphxW64Qfs3ZwFhMhaPmD1EaTiNR3bV9OYx6bVAAgHnT6T4P%2FbSePMi2y4tW2ZCP1JqtQB4xebOIHhjLPqGXXXGnKBP6kCFis3JU0BU3HR9d0wu%2F6ZvQY6pgEbEpy2K5Lz5VTbKVvwqaFRqBZL%2F2gfEsbtIVPORKPXeQtOdPahSwgKNLkIb2U5T7wf6kjNeOk4NAoBnsx7QXctWAezli3cKzuo7atY6SfeEQxzXakg1EghhH9POJrkoGZSd89GBDH6C7%2BeemIOZ2gN%2Bmq4nJk%2FEtG8fIfZ3Lq9T6hXGyeL%2FO3DL7WIr9iOkR3WQVyXAJ7LgziYAATIlqd91j2Dz7Uc&X-Amz-Signature=9b2c6de99555e1b423791750281ce5e8071cc2284aa98a39ddadf968417bb400&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUPAPEFO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDAS2p15ioHz3TaWKwad3Y7dJN%2BaNJEtpr9tEwj8FqqTAiAflkT0IJtkxJDU3ts0hetPFIReiFIFexwwR21FClM7eSr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM1qmtdEITZwlvKoYgKtwDa8BD20KNCMwm2j1pqSVEexgojOvetIeefefgT8uymQcjaiGjvcEkGTUPxlin7v88%2Bl5iKc5DcJz%2B5KOt9L00YAhjPVRSqxHn0aXHM5cC18dz7VjnEevagt6RwkZ74zuBDN1b3Ck6EMqsGa5%2FsSLtym6CRpOcRSL5vOpTqcO5u4s1zYrhC4PiZTFYk5h4Sr%2BXS%2BpVFyynOEzPh6hqN6wVuyazTWTB%2FmhjFBU6HCifXX2gfxFPlvKcygo6Ypco9a6z08XcCfeiWHXF1%2FvFd0UpQS6%2FkNbWmTeM%2BObDePMviDVeEn%2BsqJr5x%2FsDvRVvs9MR1mVWK%2ByP48hQ4vM8%2Bj0Z%2FLhj5bVl7QvjnFlSgiHZqucDhV%2FG%2B9r3JR6UxKQ11JpGNIVTNlaS9HwJqo4txDULJUaFZSvdxZm2cjVQQaNZwLLr%2FvlAjim5X0alExqG4cQLMKM7IJ%2FFSnFQRPMqoPrIbNqxKaWJtL9l9J5yoUoYpr2QLPo9rYZ5DjhDagzu6dBUnGjBcZ%2BGggazT7Ypb8xbm5WN5pgLA4BOv5bvdwuX3Hwt1AdRUOXj2EBNY1AJvrCFw%2F2ducBr9pJ%2BgJ1%2FDRaU52Q8PNPcMfFZs9XM%2F9NB89kzrR%2BNKQw9IKJksywwqP6ZvQY6pgHmwsNmFFGIO5dlmxcfB9FgVRWN%2FC7IrGrsMnWESHnFrDDD5d0VKCFDw7zA4y8vY0v94zL7YvsS%2BBbOZITNiFjkB7YJ46uuAQteoiDkLr9vhQAfU6w4K0uHjiDkFaNv%2FSi8068ly7044Rr5A%2B4YTig%2Ba%2Bj9uPfdMu%2BmOF65naO6%2FNTzjFGAqMYGDJQpQPsgQfzeoHkrNe%2FjWWnOzw0BCT7nar0Em5mU&X-Amz-Signature=b92d3919b2afa29b24745e140d1029a3665d44061579c58e6933d4fee95bc6e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JKSZFX5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCICVRhV%2FNYr%2FqSBNAm9yOF6mSU63beBC9%2BHFfUJJVFVFIAiB7GW2oQ8ai3yg7w0THcd5Rrh7WUM8856LGwgp1YOd4Myr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMMv5aMu8%2FqAQZDIp3KtwDZ7yHb879u%2BetGPuIkVjUPaR8EoS1%2BtiMs7frViDs0AX1PICynNUExSL%2FYZh6B62%2F%2BldPQ24gmzedAoyo7b1yLblXG5Fxm7xROe%2FlSv3FZqSHD13JK84ZqngLaPuC4TkcHld7EznwiYcRTGyEtnxatG5HUqZbrQYARZJcm7fwTlwCu0aCuIKMd0RG11lgRJibet8TFJv9D6ts4WVy%2BwE67PtFy9Vahd%2BiHR8SLKIP1BBL%2BnapyJkpE7B4qro7M6PeTjTRK5D%2FfxBtFqRP2Lqj8qAmlnB4TUkiwSv6Qb44Pak0itLQmFuYjMcemAtRzxpHf7rrTh5xta0c2t8%2FTXmJONByh7RID6f1H2f0OTGFAXR2fv%2Bry2%2B9ChhTYodDazjkA%2BRMUry5bprRQ0iSRNFeXBlCACK%2BTUwck2K%2FuwF7ba2b5QeXPOvmSdTIFCTQOLjf2nX%2FlHcgLyeEGhG83uJN47HyFdGYJ4aDyYAYt0%2Fpc4XmkMtQF1cssO6J02YDnIoyZwN1jF7w3ZFdgpg%2FZ2tMjVrNoU3ESHUAUUGKIsrX0azQlSPNHNX%2BqJGAJMq9f5Y8JvfxdBPvEpftcapY1r7HReH9gjEgCj26b9bAQ%2FeFwOrO82td2biNtM25%2FqUwm%2F6ZvQY6pgFoVVmpPWHNoRpqEK5p%2F8owbTInEEJsTCyyBkmw9yVk32dv%2FIrgA3boseSrQiTTJmGrRd1qdLt8s3GrEiNjUgi4UMbrX4l5keC2eicfU8Sj42G6HyYhocqDBzIlRyVmtTm6QxuLVlt0Kgb2%2FbV8yKMzCzAhVmIStB2U3XOATWhrEJamCjvMQq7rzRgghQPPZceD9Rynpa5BsqWJuFyjfMPI%2B7JH2%2BTJ&X-Amz-Signature=f05abe31c1f0cc607b68de8a8822f76a08c0c3b576f47b5cd16d4c68b5dd900a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JKSZFX5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCICVRhV%2FNYr%2FqSBNAm9yOF6mSU63beBC9%2BHFfUJJVFVFIAiB7GW2oQ8ai3yg7w0THcd5Rrh7WUM8856LGwgp1YOd4Myr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMMv5aMu8%2FqAQZDIp3KtwDZ7yHb879u%2BetGPuIkVjUPaR8EoS1%2BtiMs7frViDs0AX1PICynNUExSL%2FYZh6B62%2F%2BldPQ24gmzedAoyo7b1yLblXG5Fxm7xROe%2FlSv3FZqSHD13JK84ZqngLaPuC4TkcHld7EznwiYcRTGyEtnxatG5HUqZbrQYARZJcm7fwTlwCu0aCuIKMd0RG11lgRJibet8TFJv9D6ts4WVy%2BwE67PtFy9Vahd%2BiHR8SLKIP1BBL%2BnapyJkpE7B4qro7M6PeTjTRK5D%2FfxBtFqRP2Lqj8qAmlnB4TUkiwSv6Qb44Pak0itLQmFuYjMcemAtRzxpHf7rrTh5xta0c2t8%2FTXmJONByh7RID6f1H2f0OTGFAXR2fv%2Bry2%2B9ChhTYodDazjkA%2BRMUry5bprRQ0iSRNFeXBlCACK%2BTUwck2K%2FuwF7ba2b5QeXPOvmSdTIFCTQOLjf2nX%2FlHcgLyeEGhG83uJN47HyFdGYJ4aDyYAYt0%2Fpc4XmkMtQF1cssO6J02YDnIoyZwN1jF7w3ZFdgpg%2FZ2tMjVrNoU3ESHUAUUGKIsrX0azQlSPNHNX%2BqJGAJMq9f5Y8JvfxdBPvEpftcapY1r7HReH9gjEgCj26b9bAQ%2FeFwOrO82td2biNtM25%2FqUwm%2F6ZvQY6pgFoVVmpPWHNoRpqEK5p%2F8owbTInEEJsTCyyBkmw9yVk32dv%2FIrgA3boseSrQiTTJmGrRd1qdLt8s3GrEiNjUgi4UMbrX4l5keC2eicfU8Sj42G6HyYhocqDBzIlRyVmtTm6QxuLVlt0Kgb2%2FbV8yKMzCzAhVmIStB2U3XOATWhrEJamCjvMQq7rzRgghQPPZceD9Rynpa5BsqWJuFyjfMPI%2B7JH2%2BTJ&X-Amz-Signature=8d9ed696e4c2955e88705327d8392d2037e170fbd294645999ebd38c4ba426df&X-Amz-SignedHeaders=host&x-id=GetObject)

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
