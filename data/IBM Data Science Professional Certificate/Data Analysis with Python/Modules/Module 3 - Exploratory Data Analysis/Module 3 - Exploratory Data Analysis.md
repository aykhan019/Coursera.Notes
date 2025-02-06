

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHGYLMAL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCwHQWcswywZr828lTjfUEWi7CE2T9EOocBQ3OSeN%2Fv3gIgOoM49f2%2FvBsaDDh5mn1ARMlBi2hESw%2B%2BWoPzQO5U4jwq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJrcIRKu%2ByBQ4WoylSrcA7YQ1y40L7qrWtIwxphH86b3CIFUhCIr4TXFl9OxSklGC7DQsxIy%2FPVgRoQosQs0MfjIMurXAUCy%2BVTdu9Gs5stDZ8E2iEJ7%2FkPSVOJ9tWJ1UeTCTlQFig863R9Romq%2BL03jh5yGhXGWLmFiTTsh8WN0VwtacGIS6L2mACl9%2B3L5GFovZl%2Fys6pje54HQ74ooh6Gbqbd52kB45XT7e0VP0TAL3dI7J8FJEy7jU8ENU7uE58bhEf%2Fg0QIARRl5FDLQtKYx3eWJFQhAJXQ%2FzwvJM9tnWMqLHiqT3WLDCz0XsOplWvMnvKEsBUvUEozGvt4y6q2BypPxYOKThRumoQ41b4cTqpkI1xs%2B1vaf6Zgl29OwbxQLFjdgH7B%2Bptce%2B48c9VjHUgR6EE4bEDsTRPe4nG%2BGWir21flR%2FajKF4tW10ZPBlpEWhC8CrcFzGUK6rMWcblqfhtJfzq06OdfUzGKj%2F2qRXR%2FvGbSNJZDiila01w20k80iJKwpeFYgBmrJY8Li7hldSpliOWZ3YCoTiEuJtLr4LNLV8QIB%2FpjT%2BwD4TBmx9VofvjELEBTi2ykDt8BII8TyWy2bnpIqWkW9br4UmdVo7%2F9bLUPfLiqermWUBOPiuPKkRe8rFPT99XMNXRk70GOqUBbhKSuKanchWpX0OhtqS3IkW5tM725CcQ%2ByHQVX%2FrFxi21%2BmFgah1whyQkrRdbPA6zsflwrHAP2Q1HogOxQp1JHzF4bVjDuvuQGJbFWyZd7gldrrF9192B4bwDNoMWAQQB%2BhuAt86zxYUZP9H0QCglbb5BD7n2MUGtdCczNkS0I0Jf7AegBKogyCchjKTa1ilN6GQJMmH4I18V3lg8fE94my0iTrT&X-Amz-Signature=922fe7913e646cf3f2ccda01ca25db7281320d6ab644bbaebefc3a7bc009a582&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHGYLMAL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCwHQWcswywZr828lTjfUEWi7CE2T9EOocBQ3OSeN%2Fv3gIgOoM49f2%2FvBsaDDh5mn1ARMlBi2hESw%2B%2BWoPzQO5U4jwq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJrcIRKu%2ByBQ4WoylSrcA7YQ1y40L7qrWtIwxphH86b3CIFUhCIr4TXFl9OxSklGC7DQsxIy%2FPVgRoQosQs0MfjIMurXAUCy%2BVTdu9Gs5stDZ8E2iEJ7%2FkPSVOJ9tWJ1UeTCTlQFig863R9Romq%2BL03jh5yGhXGWLmFiTTsh8WN0VwtacGIS6L2mACl9%2B3L5GFovZl%2Fys6pje54HQ74ooh6Gbqbd52kB45XT7e0VP0TAL3dI7J8FJEy7jU8ENU7uE58bhEf%2Fg0QIARRl5FDLQtKYx3eWJFQhAJXQ%2FzwvJM9tnWMqLHiqT3WLDCz0XsOplWvMnvKEsBUvUEozGvt4y6q2BypPxYOKThRumoQ41b4cTqpkI1xs%2B1vaf6Zgl29OwbxQLFjdgH7B%2Bptce%2B48c9VjHUgR6EE4bEDsTRPe4nG%2BGWir21flR%2FajKF4tW10ZPBlpEWhC8CrcFzGUK6rMWcblqfhtJfzq06OdfUzGKj%2F2qRXR%2FvGbSNJZDiila01w20k80iJKwpeFYgBmrJY8Li7hldSpliOWZ3YCoTiEuJtLr4LNLV8QIB%2FpjT%2BwD4TBmx9VofvjELEBTi2ykDt8BII8TyWy2bnpIqWkW9br4UmdVo7%2F9bLUPfLiqermWUBOPiuPKkRe8rFPT99XMNXRk70GOqUBbhKSuKanchWpX0OhtqS3IkW5tM725CcQ%2ByHQVX%2FrFxi21%2BmFgah1whyQkrRdbPA6zsflwrHAP2Q1HogOxQp1JHzF4bVjDuvuQGJbFWyZd7gldrrF9192B4bwDNoMWAQQB%2BhuAt86zxYUZP9H0QCglbb5BD7n2MUGtdCczNkS0I0Jf7AegBKogyCchjKTa1ilN6GQJMmH4I18V3lg8fE94my0iTrT&X-Amz-Signature=ce2f7483a5865f58df27336d322cff38f08c47dd3c20a276216b90e0abdb042e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHGYLMAL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCwHQWcswywZr828lTjfUEWi7CE2T9EOocBQ3OSeN%2Fv3gIgOoM49f2%2FvBsaDDh5mn1ARMlBi2hESw%2B%2BWoPzQO5U4jwq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJrcIRKu%2ByBQ4WoylSrcA7YQ1y40L7qrWtIwxphH86b3CIFUhCIr4TXFl9OxSklGC7DQsxIy%2FPVgRoQosQs0MfjIMurXAUCy%2BVTdu9Gs5stDZ8E2iEJ7%2FkPSVOJ9tWJ1UeTCTlQFig863R9Romq%2BL03jh5yGhXGWLmFiTTsh8WN0VwtacGIS6L2mACl9%2B3L5GFovZl%2Fys6pje54HQ74ooh6Gbqbd52kB45XT7e0VP0TAL3dI7J8FJEy7jU8ENU7uE58bhEf%2Fg0QIARRl5FDLQtKYx3eWJFQhAJXQ%2FzwvJM9tnWMqLHiqT3WLDCz0XsOplWvMnvKEsBUvUEozGvt4y6q2BypPxYOKThRumoQ41b4cTqpkI1xs%2B1vaf6Zgl29OwbxQLFjdgH7B%2Bptce%2B48c9VjHUgR6EE4bEDsTRPe4nG%2BGWir21flR%2FajKF4tW10ZPBlpEWhC8CrcFzGUK6rMWcblqfhtJfzq06OdfUzGKj%2F2qRXR%2FvGbSNJZDiila01w20k80iJKwpeFYgBmrJY8Li7hldSpliOWZ3YCoTiEuJtLr4LNLV8QIB%2FpjT%2BwD4TBmx9VofvjELEBTi2ykDt8BII8TyWy2bnpIqWkW9br4UmdVo7%2F9bLUPfLiqermWUBOPiuPKkRe8rFPT99XMNXRk70GOqUBbhKSuKanchWpX0OhtqS3IkW5tM725CcQ%2ByHQVX%2FrFxi21%2BmFgah1whyQkrRdbPA6zsflwrHAP2Q1HogOxQp1JHzF4bVjDuvuQGJbFWyZd7gldrrF9192B4bwDNoMWAQQB%2BhuAt86zxYUZP9H0QCglbb5BD7n2MUGtdCczNkS0I0Jf7AegBKogyCchjKTa1ilN6GQJMmH4I18V3lg8fE94my0iTrT&X-Amz-Signature=f58f13c869440916d321697807940ecaa48474039f1742370662c614bb540754&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGN2L3QO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDI7rZY7uR2%2Bw%2FIRuB8oiRKU%2BfjbiYC1gzoX%2Bs%2FiNeBiAiA9CdRWu6yrKNA13VTAijorf%2B38OsfA5fZ5g0pfOh6Umir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMDFNXLt7hvO%2F53yNDKtwDHnaJRB1IxtEO2iYl9Hbc6B%2BNV6iqEJEv9yAOGsIC6MCN4KfrzByoZtX2Qsl09%2Bfe7cmsrSqZwjS1dLGc5bPrnvFyzL1AzCaTZGItDnaUsc2fdffrb7wk9bePMlo7IdYNU%2Ff%2FAgFfkM4yWu1G8j2tstYiRAtOw7K4Tp2EExXE%2FBR8KMNDhBOy8Py9NIEWKGOJw8EPdu39KCvNB0C0aoWZqg4Kj%2BjyW9f42ah4BwOkgLLWAPgjO4qYhXB0phTSFVuoMbY9N46d0cpGuU7z9Y74vo6xMCN245qAXF7Nd1HjkK1xDRS5YY9XUWlTfqR0NSpv0BG%2BI5hc%2BF1OC0VC9npny5jIuI1kMIuh8ONqHYmRaMfuLmPmlklTueShKgk4ep%2BBHVE08OrWF%2FVIxioiCHRuPUZYA%2FHtF9GdWafTTC%2B6deXbEM76Nls5UvBeyjyoFqgf9598NTFzoAMBBNDGT5mcP7cNo679emLMb3quJgeB24L3V3skjaIRYid5gCPBR3rUbTSZD8X5Q1pN%2BkoVG4pYglUadudXNK8%2BM0FgSL6wh%2Bj2y90tDFg07TqZizRuM%2BayhDHzDm52C13E43FaKA6h%2Bt%2Bbekoncbth3QSrsLLhyPB5eAo2VIYRQd9zjcow4tGTvQY6pgHNJ38dKib9c2Lwn1D%2FlFwp3uR5Jj28KuhU70ecum84sZeX586bWMX8fYY2T8IIP4vzx5J9nGUK%2Fuq6L1vftjBW29oE%2FF9WR37QVVzE4kkmQtPJVPUFZR4h%2F66DYUES07xGbwqtpwpHtwZZdbkNu%2BfXDS5R2yzXr7Xg60RXjTVwjt%2FZ1Cbw1TLpYqY%2FI8u%2FPbxMqCr57uBhUfuqNxPqiFrROKhzXrLz&X-Amz-Signature=e12ecac92fe35697ffecee0136018f4f22899b199e6d79eac93648f08ce6efb0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGN2L3QO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDI7rZY7uR2%2Bw%2FIRuB8oiRKU%2BfjbiYC1gzoX%2Bs%2FiNeBiAiA9CdRWu6yrKNA13VTAijorf%2B38OsfA5fZ5g0pfOh6Umir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMDFNXLt7hvO%2F53yNDKtwDHnaJRB1IxtEO2iYl9Hbc6B%2BNV6iqEJEv9yAOGsIC6MCN4KfrzByoZtX2Qsl09%2Bfe7cmsrSqZwjS1dLGc5bPrnvFyzL1AzCaTZGItDnaUsc2fdffrb7wk9bePMlo7IdYNU%2Ff%2FAgFfkM4yWu1G8j2tstYiRAtOw7K4Tp2EExXE%2FBR8KMNDhBOy8Py9NIEWKGOJw8EPdu39KCvNB0C0aoWZqg4Kj%2BjyW9f42ah4BwOkgLLWAPgjO4qYhXB0phTSFVuoMbY9N46d0cpGuU7z9Y74vo6xMCN245qAXF7Nd1HjkK1xDRS5YY9XUWlTfqR0NSpv0BG%2BI5hc%2BF1OC0VC9npny5jIuI1kMIuh8ONqHYmRaMfuLmPmlklTueShKgk4ep%2BBHVE08OrWF%2FVIxioiCHRuPUZYA%2FHtF9GdWafTTC%2B6deXbEM76Nls5UvBeyjyoFqgf9598NTFzoAMBBNDGT5mcP7cNo679emLMb3quJgeB24L3V3skjaIRYid5gCPBR3rUbTSZD8X5Q1pN%2BkoVG4pYglUadudXNK8%2BM0FgSL6wh%2Bj2y90tDFg07TqZizRuM%2BayhDHzDm52C13E43FaKA6h%2Bt%2Bbekoncbth3QSrsLLhyPB5eAo2VIYRQd9zjcow4tGTvQY6pgHNJ38dKib9c2Lwn1D%2FlFwp3uR5Jj28KuhU70ecum84sZeX586bWMX8fYY2T8IIP4vzx5J9nGUK%2Fuq6L1vftjBW29oE%2FF9WR37QVVzE4kkmQtPJVPUFZR4h%2F66DYUES07xGbwqtpwpHtwZZdbkNu%2BfXDS5R2yzXr7Xg60RXjTVwjt%2FZ1Cbw1TLpYqY%2FI8u%2FPbxMqCr57uBhUfuqNxPqiFrROKhzXrLz&X-Amz-Signature=8a0cb5c3d39af58386e4b6d1d2ee3b616364cce24692f1b4fd02b9508c226715&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGN2L3QO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDI7rZY7uR2%2Bw%2FIRuB8oiRKU%2BfjbiYC1gzoX%2Bs%2FiNeBiAiA9CdRWu6yrKNA13VTAijorf%2B38OsfA5fZ5g0pfOh6Umir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMDFNXLt7hvO%2F53yNDKtwDHnaJRB1IxtEO2iYl9Hbc6B%2BNV6iqEJEv9yAOGsIC6MCN4KfrzByoZtX2Qsl09%2Bfe7cmsrSqZwjS1dLGc5bPrnvFyzL1AzCaTZGItDnaUsc2fdffrb7wk9bePMlo7IdYNU%2Ff%2FAgFfkM4yWu1G8j2tstYiRAtOw7K4Tp2EExXE%2FBR8KMNDhBOy8Py9NIEWKGOJw8EPdu39KCvNB0C0aoWZqg4Kj%2BjyW9f42ah4BwOkgLLWAPgjO4qYhXB0phTSFVuoMbY9N46d0cpGuU7z9Y74vo6xMCN245qAXF7Nd1HjkK1xDRS5YY9XUWlTfqR0NSpv0BG%2BI5hc%2BF1OC0VC9npny5jIuI1kMIuh8ONqHYmRaMfuLmPmlklTueShKgk4ep%2BBHVE08OrWF%2FVIxioiCHRuPUZYA%2FHtF9GdWafTTC%2B6deXbEM76Nls5UvBeyjyoFqgf9598NTFzoAMBBNDGT5mcP7cNo679emLMb3quJgeB24L3V3skjaIRYid5gCPBR3rUbTSZD8X5Q1pN%2BkoVG4pYglUadudXNK8%2BM0FgSL6wh%2Bj2y90tDFg07TqZizRuM%2BayhDHzDm52C13E43FaKA6h%2Bt%2Bbekoncbth3QSrsLLhyPB5eAo2VIYRQd9zjcow4tGTvQY6pgHNJ38dKib9c2Lwn1D%2FlFwp3uR5Jj28KuhU70ecum84sZeX586bWMX8fYY2T8IIP4vzx5J9nGUK%2Fuq6L1vftjBW29oE%2FF9WR37QVVzE4kkmQtPJVPUFZR4h%2F66DYUES07xGbwqtpwpHtwZZdbkNu%2BfXDS5R2yzXr7Xg60RXjTVwjt%2FZ1Cbw1TLpYqY%2FI8u%2FPbxMqCr57uBhUfuqNxPqiFrROKhzXrLz&X-Amz-Signature=f0fe5befdf3eaf28e4b9ae15c02190fb2f7b91d36545ab94c9d59687e224f326&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGN2L3QO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDI7rZY7uR2%2Bw%2FIRuB8oiRKU%2BfjbiYC1gzoX%2Bs%2FiNeBiAiA9CdRWu6yrKNA13VTAijorf%2B38OsfA5fZ5g0pfOh6Umir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMDFNXLt7hvO%2F53yNDKtwDHnaJRB1IxtEO2iYl9Hbc6B%2BNV6iqEJEv9yAOGsIC6MCN4KfrzByoZtX2Qsl09%2Bfe7cmsrSqZwjS1dLGc5bPrnvFyzL1AzCaTZGItDnaUsc2fdffrb7wk9bePMlo7IdYNU%2Ff%2FAgFfkM4yWu1G8j2tstYiRAtOw7K4Tp2EExXE%2FBR8KMNDhBOy8Py9NIEWKGOJw8EPdu39KCvNB0C0aoWZqg4Kj%2BjyW9f42ah4BwOkgLLWAPgjO4qYhXB0phTSFVuoMbY9N46d0cpGuU7z9Y74vo6xMCN245qAXF7Nd1HjkK1xDRS5YY9XUWlTfqR0NSpv0BG%2BI5hc%2BF1OC0VC9npny5jIuI1kMIuh8ONqHYmRaMfuLmPmlklTueShKgk4ep%2BBHVE08OrWF%2FVIxioiCHRuPUZYA%2FHtF9GdWafTTC%2B6deXbEM76Nls5UvBeyjyoFqgf9598NTFzoAMBBNDGT5mcP7cNo679emLMb3quJgeB24L3V3skjaIRYid5gCPBR3rUbTSZD8X5Q1pN%2BkoVG4pYglUadudXNK8%2BM0FgSL6wh%2Bj2y90tDFg07TqZizRuM%2BayhDHzDm52C13E43FaKA6h%2Bt%2Bbekoncbth3QSrsLLhyPB5eAo2VIYRQd9zjcow4tGTvQY6pgHNJ38dKib9c2Lwn1D%2FlFwp3uR5Jj28KuhU70ecum84sZeX586bWMX8fYY2T8IIP4vzx5J9nGUK%2Fuq6L1vftjBW29oE%2FF9WR37QVVzE4kkmQtPJVPUFZR4h%2F66DYUES07xGbwqtpwpHtwZZdbkNu%2BfXDS5R2yzXr7Xg60RXjTVwjt%2FZ1Cbw1TLpYqY%2FI8u%2FPbxMqCr57uBhUfuqNxPqiFrROKhzXrLz&X-Amz-Signature=a7441ad3543c2d69c2ce25fa1576c2ba8dd6c2d6c3d092902f989d6f8a4b2304&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGN2L3QO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDI7rZY7uR2%2Bw%2FIRuB8oiRKU%2BfjbiYC1gzoX%2Bs%2FiNeBiAiA9CdRWu6yrKNA13VTAijorf%2B38OsfA5fZ5g0pfOh6Umir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMDFNXLt7hvO%2F53yNDKtwDHnaJRB1IxtEO2iYl9Hbc6B%2BNV6iqEJEv9yAOGsIC6MCN4KfrzByoZtX2Qsl09%2Bfe7cmsrSqZwjS1dLGc5bPrnvFyzL1AzCaTZGItDnaUsc2fdffrb7wk9bePMlo7IdYNU%2Ff%2FAgFfkM4yWu1G8j2tstYiRAtOw7K4Tp2EExXE%2FBR8KMNDhBOy8Py9NIEWKGOJw8EPdu39KCvNB0C0aoWZqg4Kj%2BjyW9f42ah4BwOkgLLWAPgjO4qYhXB0phTSFVuoMbY9N46d0cpGuU7z9Y74vo6xMCN245qAXF7Nd1HjkK1xDRS5YY9XUWlTfqR0NSpv0BG%2BI5hc%2BF1OC0VC9npny5jIuI1kMIuh8ONqHYmRaMfuLmPmlklTueShKgk4ep%2BBHVE08OrWF%2FVIxioiCHRuPUZYA%2FHtF9GdWafTTC%2B6deXbEM76Nls5UvBeyjyoFqgf9598NTFzoAMBBNDGT5mcP7cNo679emLMb3quJgeB24L3V3skjaIRYid5gCPBR3rUbTSZD8X5Q1pN%2BkoVG4pYglUadudXNK8%2BM0FgSL6wh%2Bj2y90tDFg07TqZizRuM%2BayhDHzDm52C13E43FaKA6h%2Bt%2Bbekoncbth3QSrsLLhyPB5eAo2VIYRQd9zjcow4tGTvQY6pgHNJ38dKib9c2Lwn1D%2FlFwp3uR5Jj28KuhU70ecum84sZeX586bWMX8fYY2T8IIP4vzx5J9nGUK%2Fuq6L1vftjBW29oE%2FF9WR37QVVzE4kkmQtPJVPUFZR4h%2F66DYUES07xGbwqtpwpHtwZZdbkNu%2BfXDS5R2yzXr7Xg60RXjTVwjt%2FZ1Cbw1TLpYqY%2FI8u%2FPbxMqCr57uBhUfuqNxPqiFrROKhzXrLz&X-Amz-Signature=ef505d05e0ce59395a1ab23a89fb87cf4072fca63760ae39cf1df7ef9fe20de3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGN2L3QO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDI7rZY7uR2%2Bw%2FIRuB8oiRKU%2BfjbiYC1gzoX%2Bs%2FiNeBiAiA9CdRWu6yrKNA13VTAijorf%2B38OsfA5fZ5g0pfOh6Umir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMDFNXLt7hvO%2F53yNDKtwDHnaJRB1IxtEO2iYl9Hbc6B%2BNV6iqEJEv9yAOGsIC6MCN4KfrzByoZtX2Qsl09%2Bfe7cmsrSqZwjS1dLGc5bPrnvFyzL1AzCaTZGItDnaUsc2fdffrb7wk9bePMlo7IdYNU%2Ff%2FAgFfkM4yWu1G8j2tstYiRAtOw7K4Tp2EExXE%2FBR8KMNDhBOy8Py9NIEWKGOJw8EPdu39KCvNB0C0aoWZqg4Kj%2BjyW9f42ah4BwOkgLLWAPgjO4qYhXB0phTSFVuoMbY9N46d0cpGuU7z9Y74vo6xMCN245qAXF7Nd1HjkK1xDRS5YY9XUWlTfqR0NSpv0BG%2BI5hc%2BF1OC0VC9npny5jIuI1kMIuh8ONqHYmRaMfuLmPmlklTueShKgk4ep%2BBHVE08OrWF%2FVIxioiCHRuPUZYA%2FHtF9GdWafTTC%2B6deXbEM76Nls5UvBeyjyoFqgf9598NTFzoAMBBNDGT5mcP7cNo679emLMb3quJgeB24L3V3skjaIRYid5gCPBR3rUbTSZD8X5Q1pN%2BkoVG4pYglUadudXNK8%2BM0FgSL6wh%2Bj2y90tDFg07TqZizRuM%2BayhDHzDm52C13E43FaKA6h%2Bt%2Bbekoncbth3QSrsLLhyPB5eAo2VIYRQd9zjcow4tGTvQY6pgHNJ38dKib9c2Lwn1D%2FlFwp3uR5Jj28KuhU70ecum84sZeX586bWMX8fYY2T8IIP4vzx5J9nGUK%2Fuq6L1vftjBW29oE%2FF9WR37QVVzE4kkmQtPJVPUFZR4h%2F66DYUES07xGbwqtpwpHtwZZdbkNu%2BfXDS5R2yzXr7Xg60RXjTVwjt%2FZ1Cbw1TLpYqY%2FI8u%2FPbxMqCr57uBhUfuqNxPqiFrROKhzXrLz&X-Amz-Signature=bbcb4026a05d3c5c454dfac29b530a9571d2932124b2462efe74b31ecd83e4f1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466742PYWHD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIHJzECZNd12kiju986%2FVAX%2FPi322WsNE2l0h9PGYPR9WAiAW3j%2F6H6S7OaArRjXDYSus8yNdgsA0YvTu7RB8YjzQhSr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMgu2Xw6kQONqbEoO2KtwDx5kqjUkH8wF9H1neDOTvFtjOByX6Epw9s15xG1MDwapabkhs0DclE8gcn68NRQUhq%2F3U5WxUj84wwlxETuXGXiH8%2FOf5Lu7AU0DCsizPDANj9rig0Vqc1gUKdv8II8kwGXu1Lu37jdgI3JuG5AsPPplKnxHt8koPkSd73NMG%2FfsFXIVOZDP1HE%2FXgsz5c0CqVzuPmQCAJjI%2FKWyRWAEdTcP%2BsU%2Fj3S%2FSZJASg7UX%2BOtykTnLrluKwQZI7DnXtsmNb5SbNr2RSxVn3mg3YdoDIqtQvi6h3pS%2FCoOo90l7W1r2Ycu%2FdpXZVeD4Eew86Jkl0OXPmaZosNl0qw2xk%2B%2FZh%2FqzDgN5qy2MEeBn%2FfekL7njaMELl1ZXj4F9UTM75Am%2BUgldV05okiOaMcWs7DRIKQMXQhTLYLAPolWoFRxlChB7HEajXS3I%2BnflBT%2BRLzCKMlg3ZfmKDCStRLwnFoB%2FXo467ZQ3r8FibVMbFxyKCeedF0EqcFMp%2BZT%2FKW83KQwDgECX3%2BSUYXZZATE3FmPwrKZtO1mUiJ4gZhWl0IP945IhyfFTRud41AARA%2BsWb83YyZs44%2BugXFssEjzB4S9r0bPn6Y4zamy76%2FCpFrAFKIUzOk8TyfkcMLRymHAwydGTvQY6pgGC%2BMbi9e1%2FJMZYA%2Bl%2BpEn3bWsQl9hjLp1o7NMEwlK1h7mgjLdLYHJ9mlqRYn7wa95V15P3jtaP69A1rxicninoVEcVg3WwwYhuEkr0hvJ%2ByGkY4wFO3UdrD6WZMUY%2FhWl3EbGkIh%2BnEzgpu%2BOwPhrqDxiW5IB1VLGDwo%2BeHnllOvGuZVb0W93WsoG3BoQvpScAZNYRCOl%2BUIL0qwXgr3BPRoy4zzXb&X-Amz-Signature=169913802971c72e61bd535e75118493356cafd5b27e0476c6ad26cc2b18e3f9&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJKEH22%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEiAzmxNXWukf1olDtlaoplPGPpL50vqW6%2BLWU9TNkU%2FAiBkVwowXeCP5bOB%2BQFiemirpe8J7NJGxJhFz0IJIc4tXSr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM0spja672qsiXHw2nKtwD0ZnO8hs3dIYbe4SWdpX2iwCb6EMaHH9nkuZMWtgmkAAE4Nbh21WG%2BCzxS4znvdhOmh8Q7KVPoba3j291fWyMiqgIneer8QR81yogkvPpNxYPoz%2FykH8Sd8LzCBBg16JTh6yKiIhVO63lPO0hFFt5oxmz0f2aw7Lqi33hTlcw8F9Hm1%2BATxu%2B%2FFeRNiC%2BsmKZCmr2JjTrK0H7gLzihd8pFqdaxIqDahSk8RllDLGhMenSZMeeYjvmziujHeZOZ7l2zQriq%2BqVZd40lLZK4ICfToM6UXAtdGkidxpd2e2Q%2BoeTflfJQAtG436bmEHFCz1JX4j3dPdRe7kLDf7%2Ff%2BfqKviL0B%2FpU7v11WXtMMYgnaXael2Dd2gzy%2BJaZVhjYpATTfLpIhelb06V2DxsKyUWN3nbulZuMPXEOpAPNON7MQWLw2GSVxqpqQWcJW8onicEDV0LFTKLBMFKEPez45fW4Wup7Att35bIooC%2FkOxXCrlH4z9Mca0LUcdY64nqIa2Yi2EBvFe9pcbs9rL2pGLzMSZwfovMrhig45SfYxwAoeVJJBjkNrNcWxYY%2BYQZikXbRHnlq7xT2jZ6BwTe8YdGbwMx5Ueq%2BQyeQAy5Ny5yQwUbK59lTJkTQWrm%2FeswvNGTvQY6pgG%2FYB9ipASpj4tWD5VvJQYAQy2KvqgjU3ZZ1h8ZvSaj73p82jD1ha5qBQ%2B6DSStiaKDzyi5e%2F%2FfsbyJDJ%2FWHwYNZojfqUJRlUSLi1f7jP5SmKL9cdYKDDxPzUr6pkeIslxyyyYRm%2FwFFG4zMOkVysZM2Hf%2FYhm%2FD9SClJjK%2B3M5jlJH2DuEp16p6QsJm5uqH6fWmjkpWUcdsPxB%2FSNjy9gHAf18ZSeE&X-Amz-Signature=40a9691076c6358d41801063cacafbb51fd77020c4b6395e869769f4b59e6b25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGN2L3QO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDI7rZY7uR2%2Bw%2FIRuB8oiRKU%2BfjbiYC1gzoX%2Bs%2FiNeBiAiA9CdRWu6yrKNA13VTAijorf%2B38OsfA5fZ5g0pfOh6Umir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMDFNXLt7hvO%2F53yNDKtwDHnaJRB1IxtEO2iYl9Hbc6B%2BNV6iqEJEv9yAOGsIC6MCN4KfrzByoZtX2Qsl09%2Bfe7cmsrSqZwjS1dLGc5bPrnvFyzL1AzCaTZGItDnaUsc2fdffrb7wk9bePMlo7IdYNU%2Ff%2FAgFfkM4yWu1G8j2tstYiRAtOw7K4Tp2EExXE%2FBR8KMNDhBOy8Py9NIEWKGOJw8EPdu39KCvNB0C0aoWZqg4Kj%2BjyW9f42ah4BwOkgLLWAPgjO4qYhXB0phTSFVuoMbY9N46d0cpGuU7z9Y74vo6xMCN245qAXF7Nd1HjkK1xDRS5YY9XUWlTfqR0NSpv0BG%2BI5hc%2BF1OC0VC9npny5jIuI1kMIuh8ONqHYmRaMfuLmPmlklTueShKgk4ep%2BBHVE08OrWF%2FVIxioiCHRuPUZYA%2FHtF9GdWafTTC%2B6deXbEM76Nls5UvBeyjyoFqgf9598NTFzoAMBBNDGT5mcP7cNo679emLMb3quJgeB24L3V3skjaIRYid5gCPBR3rUbTSZD8X5Q1pN%2BkoVG4pYglUadudXNK8%2BM0FgSL6wh%2Bj2y90tDFg07TqZizRuM%2BayhDHzDm52C13E43FaKA6h%2Bt%2Bbekoncbth3QSrsLLhyPB5eAo2VIYRQd9zjcow4tGTvQY6pgHNJ38dKib9c2Lwn1D%2FlFwp3uR5Jj28KuhU70ecum84sZeX586bWMX8fYY2T8IIP4vzx5J9nGUK%2Fuq6L1vftjBW29oE%2FF9WR37QVVzE4kkmQtPJVPUFZR4h%2F66DYUES07xGbwqtpwpHtwZZdbkNu%2BfXDS5R2yzXr7Xg60RXjTVwjt%2FZ1Cbw1TLpYqY%2FI8u%2FPbxMqCr57uBhUfuqNxPqiFrROKhzXrLz&X-Amz-Signature=d554b704b30f2a4a93661e6ba943160cc2103e19d1d06612469acd5aa9ac64d1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGN2L3QO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDI7rZY7uR2%2Bw%2FIRuB8oiRKU%2BfjbiYC1gzoX%2Bs%2FiNeBiAiA9CdRWu6yrKNA13VTAijorf%2B38OsfA5fZ5g0pfOh6Umir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMDFNXLt7hvO%2F53yNDKtwDHnaJRB1IxtEO2iYl9Hbc6B%2BNV6iqEJEv9yAOGsIC6MCN4KfrzByoZtX2Qsl09%2Bfe7cmsrSqZwjS1dLGc5bPrnvFyzL1AzCaTZGItDnaUsc2fdffrb7wk9bePMlo7IdYNU%2Ff%2FAgFfkM4yWu1G8j2tstYiRAtOw7K4Tp2EExXE%2FBR8KMNDhBOy8Py9NIEWKGOJw8EPdu39KCvNB0C0aoWZqg4Kj%2BjyW9f42ah4BwOkgLLWAPgjO4qYhXB0phTSFVuoMbY9N46d0cpGuU7z9Y74vo6xMCN245qAXF7Nd1HjkK1xDRS5YY9XUWlTfqR0NSpv0BG%2BI5hc%2BF1OC0VC9npny5jIuI1kMIuh8ONqHYmRaMfuLmPmlklTueShKgk4ep%2BBHVE08OrWF%2FVIxioiCHRuPUZYA%2FHtF9GdWafTTC%2B6deXbEM76Nls5UvBeyjyoFqgf9598NTFzoAMBBNDGT5mcP7cNo679emLMb3quJgeB24L3V3skjaIRYid5gCPBR3rUbTSZD8X5Q1pN%2BkoVG4pYglUadudXNK8%2BM0FgSL6wh%2Bj2y90tDFg07TqZizRuM%2BayhDHzDm52C13E43FaKA6h%2Bt%2Bbekoncbth3QSrsLLhyPB5eAo2VIYRQd9zjcow4tGTvQY6pgHNJ38dKib9c2Lwn1D%2FlFwp3uR5Jj28KuhU70ecum84sZeX586bWMX8fYY2T8IIP4vzx5J9nGUK%2Fuq6L1vftjBW29oE%2FF9WR37QVVzE4kkmQtPJVPUFZR4h%2F66DYUES07xGbwqtpwpHtwZZdbkNu%2BfXDS5R2yzXr7Xg60RXjTVwjt%2FZ1Cbw1TLpYqY%2FI8u%2FPbxMqCr57uBhUfuqNxPqiFrROKhzXrLz&X-Amz-Signature=479d5b237b253c5aa9651e7281d47c16513bdc41c324315a2ac841cc7473a3c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGN2L3QO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDI7rZY7uR2%2Bw%2FIRuB8oiRKU%2BfjbiYC1gzoX%2Bs%2FiNeBiAiA9CdRWu6yrKNA13VTAijorf%2B38OsfA5fZ5g0pfOh6Umir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMDFNXLt7hvO%2F53yNDKtwDHnaJRB1IxtEO2iYl9Hbc6B%2BNV6iqEJEv9yAOGsIC6MCN4KfrzByoZtX2Qsl09%2Bfe7cmsrSqZwjS1dLGc5bPrnvFyzL1AzCaTZGItDnaUsc2fdffrb7wk9bePMlo7IdYNU%2Ff%2FAgFfkM4yWu1G8j2tstYiRAtOw7K4Tp2EExXE%2FBR8KMNDhBOy8Py9NIEWKGOJw8EPdu39KCvNB0C0aoWZqg4Kj%2BjyW9f42ah4BwOkgLLWAPgjO4qYhXB0phTSFVuoMbY9N46d0cpGuU7z9Y74vo6xMCN245qAXF7Nd1HjkK1xDRS5YY9XUWlTfqR0NSpv0BG%2BI5hc%2BF1OC0VC9npny5jIuI1kMIuh8ONqHYmRaMfuLmPmlklTueShKgk4ep%2BBHVE08OrWF%2FVIxioiCHRuPUZYA%2FHtF9GdWafTTC%2B6deXbEM76Nls5UvBeyjyoFqgf9598NTFzoAMBBNDGT5mcP7cNo679emLMb3quJgeB24L3V3skjaIRYid5gCPBR3rUbTSZD8X5Q1pN%2BkoVG4pYglUadudXNK8%2BM0FgSL6wh%2Bj2y90tDFg07TqZizRuM%2BayhDHzDm52C13E43FaKA6h%2Bt%2Bbekoncbth3QSrsLLhyPB5eAo2VIYRQd9zjcow4tGTvQY6pgHNJ38dKib9c2Lwn1D%2FlFwp3uR5Jj28KuhU70ecum84sZeX586bWMX8fYY2T8IIP4vzx5J9nGUK%2Fuq6L1vftjBW29oE%2FF9WR37QVVzE4kkmQtPJVPUFZR4h%2F66DYUES07xGbwqtpwpHtwZZdbkNu%2BfXDS5R2yzXr7Xg60RXjTVwjt%2FZ1Cbw1TLpYqY%2FI8u%2FPbxMqCr57uBhUfuqNxPqiFrROKhzXrLz&X-Amz-Signature=76f116d17ba1eed5a59982f933ba55d57010283e99e58851fe9d72f291aa3e83&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKLO5AX2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIC92KuHBTIgj2UNlG9WMc%2B4hQpdO1YXhAr3rlQZihweKAiAOkUi45jnT%2FCZ8%2FxaaGO4uq%2FrnY4TZ5V9NL5xyYR1HBCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM48fu0gE7e55cRoHwKtwDYkLx61k%2BBWPiDE1Zbn8V9Zu80%2F7smJ2gBMGCiEtr7x8tKgw7Hre477IaQ0%2FQh9AwKc3tB%2BPigmqJbHQGpieO3fnv4xQLX8EYG71DW3PgA2CkRf2IqiUCgV3SDz3L1FFK4AelnhGFRqsuJtKo1kqcEmsqpGbvHCfh%2B6IpOlGbxvNjtoWFAqMDIL688f8%2Fac6vZobq6yXZf2TPiHXcI1LBgN%2BnwaLW7zNc5g5NzHNfjH3o2oMrO0mGJs5ZJhwxd9dSDa8eEYDjZ4ZlMXAP1XwI4xQxrgdUw1rJlpOTcuoKTHSlLHA2Jev2hsfWk3lpKAomz92T8Af%2FoCsFZSpvvreUfXU%2BIyp%2FRd13w1HCxhiv0KcP6u6hlGkQQ0ACeX7serYvCgqY%2BSXgxjjBvyFDhM8mFiYYXn1aLKvk59%2B6%2BkOyN3ZuMb%2FaJztzGHIO%2FUN0rS4dOOdgScvZUISgIcZGQ0%2FwWzkLTeQbAY611gbFhXOP90aNCVWQNEcoDWXeY4vMj3unDRydpFEpGAaBoEZLL53k%2BgoTaOy37TwE5jQK2Ukq%2BMcQ00CRW0%2BlIPIVxj7%2FcnLa%2BsFuxE1anikZUTPv0yR8PkI98QfHsovxMw%2FNjV1EzEcRLdbLchpx73bdDecww9KTvQY6pgHGc68jAQtfFW29R%2BCJD8QB04lkPzcF7NI4VJQWrnf504ZeGzF%2Fpt5U0h8aIs91DEHzfgxBGUfAvP31CBAACYCG%2BlE%2BMsZ6uFlcFK9P5%2Fie04HGPI7ulsrr2VO1xaJhMK4zADkLIkAN69qGk3rcdoWeesuuhnJ%2FIu1GBQ5ZXAxIOpGl7SwLK5FLD32OLkxlznZfJ3Q3I3eW3eq0TTsldTUhEy7YvR99&X-Amz-Signature=d7f36953b7d205d5195c1284715150d2870f1aba2d6a6e87720757ef31738b64&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJWIM76M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDpiIkcn%2Fi2hS%2BWIo6ZXlsNCqp%2FujkF2RYIj712QSmY4wIgOvaFYlr00EjZs5Ey8f3m68WndFs6AWL6k%2BKonZdJfisq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDDyRIWe8sMnbawTxfCrcA05zHAK9U2C5vfI2Pjjvy8BN6r%2Fr2gAMe%2FoGZcmjgGd9lPG9QlHXOL59Hh4VAAtvvs7DcHSI2YHtcV98eOOSS6yVrqdm7ABEVu1DwWRkc5cyVS9kXZKjTYoKULej8ogtp1IcIeklt4XBmQNnwFjB5i%2BuEHvbzrxw2ljfYFWUCMTCfkI%2BHpMQGrvFMpwhRavl9WbrNic7I5YxyeI0jki7QV33mORHqJoKEzxkOWWrc6ZIn1pgCCveBIYaaZ6psBc1qGrIyg0BYcYYr44MRZiUcdU03BI0kdZaH3kieUlrWkkxeEmwBt4VMZsv1iah%2Bxau42gr1X6pfxC8WhxgfX6pQetSTpZDR87Ju7Nh1B1MTVW8X8%2FQIP6G%2BT5AJWi6U4fEqqv%2FhucO1E655QCeJ4aKFHXOEVpR%2Fmg9rJlSjTXn9WrnBu5NknHayK0QD522REfrlRoW5xcCsn%2BsvOw6Crtk4cvq%2F%2BKiHrj8GIOLgskfNSieKYXhmdhz%2FpYRAo7AOv3N%2BVsR84SVVeuRXY5ejtaP%2Bz7N00Y1fvacnP%2FyzQh%2B4Q5eHEL0b7AkikVi2SvBNfPrhhYKEzXUO300%2BKlOsTpKCaD%2BSj0wV%2FLvhnE2Xu2NsWjkL%2F4OOxCyqLB3SQYwMOvRk70GOqUBOZMELrz1P%2FUnn4Q8ICM%2FurTkvU9lqcNXy0lgiO3WQwnibwEKLY19FjlApgHd5NkqSAxOzyKrYw4iLt4%2FGp0Eb7xIvnOApGMFIrz1oR6cuie6oRopVVax5Jg5AlDtr0aPTYcYb1TNYcosl5%2FDXUW72guQMRB56rn9ubB3d2BmpCCW9Pj1dQjxz9zGcHQc2pgUeuRMDcAlB1MUnlwDdme1Ad31gBF4&X-Amz-Signature=62da6066997e95ee3be78d66873ab401156ab3e15e3506530311d7991c072445&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWJC6EB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIEG3hairwi2K0%2BsBlRd3Ah3PRGXziylkcVxLMCO1QC2EAiAE2rs1xBMGcCphaigYalXNMCa3h2Ghb%2BLWI6KL%2FmA%2Blir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMTKhMfwWb1573KY2HKtwDr51wGV9N2oDBwb6RM%2BUEteg%2FNiSvUpmQkuQhTssRTYieEbgNbZCyo7GOdbRAlt9OXNElU5%2FmoQgZoUsDkK8BjgrJ0WoYXW5GaVHuNKphL1zwhPYw%2BrnBuM18UaEkr1YTnCYsS9VCDjr316ydNWiDy3MA%2BYTA9lDX6ejU6YWMgZNxfugsckUZebmSrDnseeUHIy4aShwLTuriU4CGnQDiCRAhsfKvxY7LJM9uPiER%2BLu0IOmFbboD2bXxCJ0F9m3B7e9K2HcY2UynnFEbafrht%2FPUZfgOyHTlvFKT1jvlhX0Ov11tUQ%2FvovXTNDyHejomAlfcqmdLkJu5udnETKnXdKB3QuDuuAD2kNich533ywy8PVW7oRnJPqqZL8zCY4no%2F695M2NzaURIZ3YcDMoNwSREpyyJbO85KWPpVdHM4WCpcgZKjw9Jh9fAxvePl2ie010rVL7OHBUY1%2B6kOAVQiY21FDSjeOk8O%2BGgbROiC1RTW1X7GO8Ork99SkZr%2FgmCUsfzOiPSoCN%2BatGw31%2F%2BluEuDKIGUdHa7PxY2a8pzXjeFXsjzwJhxoFyWboT5vlWJSUBPHcWfnJKj6q62XZiu6XPAHsVZv24rCfkniewlxHQrGS78bo5CiJpQOww09GTvQY6pgEGz2pl%2BdSbFXGD52X%2B0Qqik9lMC6hNGHuPxuZfmu%2BvRQUWEQ4M58SNAwTEq%2FkyoHKpyfazVO08zIkKSfOzM4gsxQSWpiWHskNOYlc5bR5WwADo9hI5N1RXqiWlgmwWa2mFPBnOYu6lzbcY4d7D%2FdNqpWrjZG8fIJ620R4EJCQ9LkKos9ZMeRy2SADMdGcavkyE%2BhdBPypvBffahOYmOZWO4Bay7h%2BU&X-Amz-Signature=e37022ed731421272926dab269f349abfe1db4ba4026ed2304ef6837b6c35b0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOE7GDBW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDlcC7r1UJeYsg46HhGUkSxpKPTJGbymNdn81LaiPPiEgIhAOlkASMk0o8jy4nZBaG3h1R2%2Bn3atxrarXJ2Kpy5RF8IKv8DCGIQABoMNjM3NDIzMTgzODA1IgwgdtlL8MVPO2czlb8q3APGIY8pgrDL90hm5Mb4aqEtwgfDrlqYL1%2FmQJQPAdtWX6GeXYJTsPRqWlQbjlpJHfMjfS4mHeASUPBgDn9liRuPNKzjGIbRpqoLBB3yPx2OsmbR6KwmSkYGP1xCWCXiUYUfHAHcIuLQvPdGq84rpwyqLA9njF511tgidZRbqSYoEUBe3ByZyPxZ1kKV8sIHltOmM7ivj1tQMuKatepXKYqhjC4IioPOoOg15FhwXoUQ69IGNKSpRcxV2bsVizveEZa8MPFkK4O6aRozi%2FSEpSMzBmqRJOVBwymj1sTDmqGp76JxDBp1mjkTRQpR4ywB2vX9cOVAf5U00lkwJRZbOoKOCTGCAQch87teFRtknKz51Vlh%2BDK4mBQ6flRdcDIjCFVNXf5MCGzzPiFtPw1%2BhT65hErYh3dOajOOWj5OWTr2MifI4H7RXzXjFlx8EmxlWMPsUAjBQDxU2icGF2Pq6uDNaSkcgMgU2%2B2%2BH7gNeWYM6PEkx4VRTzi7WMhxnnyv5SqK%2FmymuvMXvQ65%2FtokPeXknH8i9eH%2BDfEf1zZqx9dU9C2QUqPCnRSnjl9PV05dN5UIAEugJN%2FptTAiTUlWZdbYxaBUBED98RctpRJbPIWYenZ%2FOQJZKVtlq025FDCT0ZO9BjqkAX5VaxicFKrgxR5HOS%2Bg1ITpSvybNjSB9TWBhEoQL9niT2OFh0d5qRTcn9FRTYniH4sYlCFEOUn10rWnAyVD%2FFJhT5MBa5wCByGCreRICXb2QxdXobVFKuTwhUcjVJcZAYOzsDjuLoYr2wrSaznu8sWFycPOcFAlTTmdf%2BKTh8NLNTORuPeCuwB13WKQBWHGRVhpyvUtnoBGrNf4gOaYE9ojoqER&X-Amz-Signature=523b0e9a2fffce9fd33a04d7454e3486479e11b82574c9f70d1a0c745ad302e4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOE7GDBW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDlcC7r1UJeYsg46HhGUkSxpKPTJGbymNdn81LaiPPiEgIhAOlkASMk0o8jy4nZBaG3h1R2%2Bn3atxrarXJ2Kpy5RF8IKv8DCGIQABoMNjM3NDIzMTgzODA1IgwgdtlL8MVPO2czlb8q3APGIY8pgrDL90hm5Mb4aqEtwgfDrlqYL1%2FmQJQPAdtWX6GeXYJTsPRqWlQbjlpJHfMjfS4mHeASUPBgDn9liRuPNKzjGIbRpqoLBB3yPx2OsmbR6KwmSkYGP1xCWCXiUYUfHAHcIuLQvPdGq84rpwyqLA9njF511tgidZRbqSYoEUBe3ByZyPxZ1kKV8sIHltOmM7ivj1tQMuKatepXKYqhjC4IioPOoOg15FhwXoUQ69IGNKSpRcxV2bsVizveEZa8MPFkK4O6aRozi%2FSEpSMzBmqRJOVBwymj1sTDmqGp76JxDBp1mjkTRQpR4ywB2vX9cOVAf5U00lkwJRZbOoKOCTGCAQch87teFRtknKz51Vlh%2BDK4mBQ6flRdcDIjCFVNXf5MCGzzPiFtPw1%2BhT65hErYh3dOajOOWj5OWTr2MifI4H7RXzXjFlx8EmxlWMPsUAjBQDxU2icGF2Pq6uDNaSkcgMgU2%2B2%2BH7gNeWYM6PEkx4VRTzi7WMhxnnyv5SqK%2FmymuvMXvQ65%2FtokPeXknH8i9eH%2BDfEf1zZqx9dU9C2QUqPCnRSnjl9PV05dN5UIAEugJN%2FptTAiTUlWZdbYxaBUBED98RctpRJbPIWYenZ%2FOQJZKVtlq025FDCT0ZO9BjqkAX5VaxicFKrgxR5HOS%2Bg1ITpSvybNjSB9TWBhEoQL9niT2OFh0d5qRTcn9FRTYniH4sYlCFEOUn10rWnAyVD%2FFJhT5MBa5wCByGCreRICXb2QxdXobVFKuTwhUcjVJcZAYOzsDjuLoYr2wrSaznu8sWFycPOcFAlTTmdf%2BKTh8NLNTORuPeCuwB13WKQBWHGRVhpyvUtnoBGrNf4gOaYE9ojoqER&X-Amz-Signature=ed0a88112784b03541df8858c2cb635eeda84e1145f7fc3b64ed650e599f9422&X-Amz-SignedHeaders=host&x-id=GetObject)

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
