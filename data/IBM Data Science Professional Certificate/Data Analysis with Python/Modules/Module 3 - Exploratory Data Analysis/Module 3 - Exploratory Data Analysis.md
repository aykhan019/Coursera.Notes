

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RACMV7X6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBv9MXYVgAeeVkahzBBkzBBlC6nBlSQcVE22mKPpUXyIAiEAzHitSQtlr941lbk5THKfgFgSU2PGCjkOYx0ZWJC%2B2oQqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG77f2Nt%2BKjHObTleircA5JQ0xM9m49msUV5Yn%2F1%2BG6Qi3v2F4wJBM6%2BAWSWKoPUyt4zoxuNJWQ2xpFkYMPDYN3X6ySSEA8sT%2BHmpyufZdue1H15TGf6KJbCK8epjDmJAe0JX8osF%2FxashgdsBIMWwr07N%2F2x4HiF9EEN8MMn%2Fa04zlKmxy%2BIvWKa5Xa5ZFBCkt8kT0goBpZk4L9jQ2ntXmR%2FGK7jmcCMu5u8Lis0SXaQtZls%2BivPC2zq4wtuHDmbaKarzBkgzH8zbH356a0EvXJCR0CNfcMq0dokKzM9Z5xjuWwcqkOn9xOmKO4RIfydcIS1HCeMYfHyxElOnId%2FQ3DUuc5JK4fWlSZhWLSngFiEC1Vj9VLFh7a0SnAg9Vl0fuLXzdoPICU7EszSnEMsX%2F0rnVqqt%2BO6f%2BoUNAgNsdfGe2YJ5iVVjy2TXaIMU0hSgMpdf9KOeheCUXN%2BQXXFWR0QT2A6uK7U11kMT%2Frlm6dSVRLfMlX1vlxU1e8cWDlDVbUSvzlOFA6c9DhA%2FpjDAnJI2%2FRIGbYvydXxr7RzIRtk1ZmIY8CwexVewRdnrNoDRnQcJh1YAv6I6xl1j1RSD2z1W4ImVAWqEy0Nn5lFt0Vsy%2BJMvS9gPzsmFqnN5EDIWl2hB%2FgBptYz%2Bf5MLrx%2BrwGOqUB05Wnl7IfVxQWD7XZXxh76tFvC3kcpmqRXpN6%2FPTtbI0eLRd5pU%2Fs0jJHwz0iQ8JXtyplbAv5Zkt27q%2Bz8PcTQWWRqVPAUoEafUM8ELCSFAiLKTpwDsoTTDqjbK8NnQdBS6%2F1vuk5EmXuCLrVIcjkQFCqPbk7RSAb8unz0XcScDr7MKGtd5zdKD%2F3Yy20YJlGq20SzVbBcoV6to%2F7GlcPI7A7BIOH&X-Amz-Signature=104aae48029f238d089a59063a21977cd775eac7b6e6e82d5edb22263828e3d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RACMV7X6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBv9MXYVgAeeVkahzBBkzBBlC6nBlSQcVE22mKPpUXyIAiEAzHitSQtlr941lbk5THKfgFgSU2PGCjkOYx0ZWJC%2B2oQqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG77f2Nt%2BKjHObTleircA5JQ0xM9m49msUV5Yn%2F1%2BG6Qi3v2F4wJBM6%2BAWSWKoPUyt4zoxuNJWQ2xpFkYMPDYN3X6ySSEA8sT%2BHmpyufZdue1H15TGf6KJbCK8epjDmJAe0JX8osF%2FxashgdsBIMWwr07N%2F2x4HiF9EEN8MMn%2Fa04zlKmxy%2BIvWKa5Xa5ZFBCkt8kT0goBpZk4L9jQ2ntXmR%2FGK7jmcCMu5u8Lis0SXaQtZls%2BivPC2zq4wtuHDmbaKarzBkgzH8zbH356a0EvXJCR0CNfcMq0dokKzM9Z5xjuWwcqkOn9xOmKO4RIfydcIS1HCeMYfHyxElOnId%2FQ3DUuc5JK4fWlSZhWLSngFiEC1Vj9VLFh7a0SnAg9Vl0fuLXzdoPICU7EszSnEMsX%2F0rnVqqt%2BO6f%2BoUNAgNsdfGe2YJ5iVVjy2TXaIMU0hSgMpdf9KOeheCUXN%2BQXXFWR0QT2A6uK7U11kMT%2Frlm6dSVRLfMlX1vlxU1e8cWDlDVbUSvzlOFA6c9DhA%2FpjDAnJI2%2FRIGbYvydXxr7RzIRtk1ZmIY8CwexVewRdnrNoDRnQcJh1YAv6I6xl1j1RSD2z1W4ImVAWqEy0Nn5lFt0Vsy%2BJMvS9gPzsmFqnN5EDIWl2hB%2FgBptYz%2Bf5MLrx%2BrwGOqUB05Wnl7IfVxQWD7XZXxh76tFvC3kcpmqRXpN6%2FPTtbI0eLRd5pU%2Fs0jJHwz0iQ8JXtyplbAv5Zkt27q%2Bz8PcTQWWRqVPAUoEafUM8ELCSFAiLKTpwDsoTTDqjbK8NnQdBS6%2F1vuk5EmXuCLrVIcjkQFCqPbk7RSAb8unz0XcScDr7MKGtd5zdKD%2F3Yy20YJlGq20SzVbBcoV6to%2F7GlcPI7A7BIOH&X-Amz-Signature=c2395b68dfb24398fd44f76d2faf2546a910007fbdd5aa124b4ed3503776ae2c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RACMV7X6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBv9MXYVgAeeVkahzBBkzBBlC6nBlSQcVE22mKPpUXyIAiEAzHitSQtlr941lbk5THKfgFgSU2PGCjkOYx0ZWJC%2B2oQqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG77f2Nt%2BKjHObTleircA5JQ0xM9m49msUV5Yn%2F1%2BG6Qi3v2F4wJBM6%2BAWSWKoPUyt4zoxuNJWQ2xpFkYMPDYN3X6ySSEA8sT%2BHmpyufZdue1H15TGf6KJbCK8epjDmJAe0JX8osF%2FxashgdsBIMWwr07N%2F2x4HiF9EEN8MMn%2Fa04zlKmxy%2BIvWKa5Xa5ZFBCkt8kT0goBpZk4L9jQ2ntXmR%2FGK7jmcCMu5u8Lis0SXaQtZls%2BivPC2zq4wtuHDmbaKarzBkgzH8zbH356a0EvXJCR0CNfcMq0dokKzM9Z5xjuWwcqkOn9xOmKO4RIfydcIS1HCeMYfHyxElOnId%2FQ3DUuc5JK4fWlSZhWLSngFiEC1Vj9VLFh7a0SnAg9Vl0fuLXzdoPICU7EszSnEMsX%2F0rnVqqt%2BO6f%2BoUNAgNsdfGe2YJ5iVVjy2TXaIMU0hSgMpdf9KOeheCUXN%2BQXXFWR0QT2A6uK7U11kMT%2Frlm6dSVRLfMlX1vlxU1e8cWDlDVbUSvzlOFA6c9DhA%2FpjDAnJI2%2FRIGbYvydXxr7RzIRtk1ZmIY8CwexVewRdnrNoDRnQcJh1YAv6I6xl1j1RSD2z1W4ImVAWqEy0Nn5lFt0Vsy%2BJMvS9gPzsmFqnN5EDIWl2hB%2FgBptYz%2Bf5MLrx%2BrwGOqUB05Wnl7IfVxQWD7XZXxh76tFvC3kcpmqRXpN6%2FPTtbI0eLRd5pU%2Fs0jJHwz0iQ8JXtyplbAv5Zkt27q%2Bz8PcTQWWRqVPAUoEafUM8ELCSFAiLKTpwDsoTTDqjbK8NnQdBS6%2F1vuk5EmXuCLrVIcjkQFCqPbk7RSAb8unz0XcScDr7MKGtd5zdKD%2F3Yy20YJlGq20SzVbBcoV6to%2F7GlcPI7A7BIOH&X-Amz-Signature=3b02c115ae3b0e3571e1e692f5241b866ba3c8b3d507660a15fe8cfced7c9193&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELE4CTN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQk7YPHWX40DDHhPhQihIaB5mmUU%2BasoMMjJoLvqKhFgIgRlsy4IyyCUDGSKTjvhvcaHrBbTM%2FmdE4KWSeewvGjKMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKM%2Fw01r6pIqKbLSuSrcA4oaeXei1hB34%2FM%2F4W2h7ZERkjqwmxRoZqoy%2Bj3pCXHe6YDho%2FngZRqA%2FsJLCIxQhuTrHiyM%2B8GK4LHu023dpa9TlL9Dcq9SiCY9%2B50%2FHkbpwMvTZCRjzN%2BLQfkq7d%2B9ZKPbIYnqAtN4b5Ke70OpmkNL2UD3BtyiJf0ILDWfyhu7ywFC%2BtkrIYO1mqjg4VNta%2BUoqKT0ivVvpKF3xHYHjYNGclgjIOSSQTcOfN8auhVUMZmlBpqhwFR6ndHjYHM6e0AtYDRsj%2F9Fm1NDTAFeA3%2BM0xohSBQvsaEOPEc1w6G8M7REvDv%2BzfK9LoQIQhpu89xI%2B0lNKC1sAPYU%2BQSxgro0ybmBGjoS8camvm5mbMFEdbeFN5O1zlFt%2BZOX5Dc4aeOncxRF5pmAjAviQ32IA2Mzkb9I7JQIX9wy83oKKZZuL6jvigpqWTJTGEgcUy8GGiWclPHUm9iddipdJV8x69g%2FxK1vhYlZg%2BzwKXPfLyTQphju%2FELelPmqmaaxp4NCVyDApEa7XYkOQOa1iozy5GYi9Hfj1L9736%2BzWk2BsA8n5sZnMIK%2FyTdSHCpNWNYqv0GhwjNB8x5ryBr5MAvXSfpBJsz9lcMheUjjTlUc1DY7fTfSWQ6s6drAEPBsMLzx%2BrwGOqUBheWH9tPTIjkc4NznxNrGl7SzKMKFym5C9qmeJAUY4Q4KzBBowqQumKton%2FhWW2a6dr6eh%2Bs8uEt11jS5ZKvG8DP%2FpLhBfFb5TXmjcGBdG1vD6vB%2FHdiqafzxiWHh3Ru8s633cozZ%2F5FE0SvbDujLVytg3m8nvFX%2BJUG47DzLJ3wpOYylpNBO64HNKODrNvZAey56mjQw9p4XSX94f6uXbtGob9np&X-Amz-Signature=11ff5318c6092469b813f70b735d0d8eabc7c621efa71649e0dc5047fdaf9a42&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELE4CTN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQk7YPHWX40DDHhPhQihIaB5mmUU%2BasoMMjJoLvqKhFgIgRlsy4IyyCUDGSKTjvhvcaHrBbTM%2FmdE4KWSeewvGjKMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKM%2Fw01r6pIqKbLSuSrcA4oaeXei1hB34%2FM%2F4W2h7ZERkjqwmxRoZqoy%2Bj3pCXHe6YDho%2FngZRqA%2FsJLCIxQhuTrHiyM%2B8GK4LHu023dpa9TlL9Dcq9SiCY9%2B50%2FHkbpwMvTZCRjzN%2BLQfkq7d%2B9ZKPbIYnqAtN4b5Ke70OpmkNL2UD3BtyiJf0ILDWfyhu7ywFC%2BtkrIYO1mqjg4VNta%2BUoqKT0ivVvpKF3xHYHjYNGclgjIOSSQTcOfN8auhVUMZmlBpqhwFR6ndHjYHM6e0AtYDRsj%2F9Fm1NDTAFeA3%2BM0xohSBQvsaEOPEc1w6G8M7REvDv%2BzfK9LoQIQhpu89xI%2B0lNKC1sAPYU%2BQSxgro0ybmBGjoS8camvm5mbMFEdbeFN5O1zlFt%2BZOX5Dc4aeOncxRF5pmAjAviQ32IA2Mzkb9I7JQIX9wy83oKKZZuL6jvigpqWTJTGEgcUy8GGiWclPHUm9iddipdJV8x69g%2FxK1vhYlZg%2BzwKXPfLyTQphju%2FELelPmqmaaxp4NCVyDApEa7XYkOQOa1iozy5GYi9Hfj1L9736%2BzWk2BsA8n5sZnMIK%2FyTdSHCpNWNYqv0GhwjNB8x5ryBr5MAvXSfpBJsz9lcMheUjjTlUc1DY7fTfSWQ6s6drAEPBsMLzx%2BrwGOqUBheWH9tPTIjkc4NznxNrGl7SzKMKFym5C9qmeJAUY4Q4KzBBowqQumKton%2FhWW2a6dr6eh%2Bs8uEt11jS5ZKvG8DP%2FpLhBfFb5TXmjcGBdG1vD6vB%2FHdiqafzxiWHh3Ru8s633cozZ%2F5FE0SvbDujLVytg3m8nvFX%2BJUG47DzLJ3wpOYylpNBO64HNKODrNvZAey56mjQw9p4XSX94f6uXbtGob9np&X-Amz-Signature=064a8419b7d84b1d8426a5b969556ffff66c507367a4f7af022c1d7085efc74c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELE4CTN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQk7YPHWX40DDHhPhQihIaB5mmUU%2BasoMMjJoLvqKhFgIgRlsy4IyyCUDGSKTjvhvcaHrBbTM%2FmdE4KWSeewvGjKMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKM%2Fw01r6pIqKbLSuSrcA4oaeXei1hB34%2FM%2F4W2h7ZERkjqwmxRoZqoy%2Bj3pCXHe6YDho%2FngZRqA%2FsJLCIxQhuTrHiyM%2B8GK4LHu023dpa9TlL9Dcq9SiCY9%2B50%2FHkbpwMvTZCRjzN%2BLQfkq7d%2B9ZKPbIYnqAtN4b5Ke70OpmkNL2UD3BtyiJf0ILDWfyhu7ywFC%2BtkrIYO1mqjg4VNta%2BUoqKT0ivVvpKF3xHYHjYNGclgjIOSSQTcOfN8auhVUMZmlBpqhwFR6ndHjYHM6e0AtYDRsj%2F9Fm1NDTAFeA3%2BM0xohSBQvsaEOPEc1w6G8M7REvDv%2BzfK9LoQIQhpu89xI%2B0lNKC1sAPYU%2BQSxgro0ybmBGjoS8camvm5mbMFEdbeFN5O1zlFt%2BZOX5Dc4aeOncxRF5pmAjAviQ32IA2Mzkb9I7JQIX9wy83oKKZZuL6jvigpqWTJTGEgcUy8GGiWclPHUm9iddipdJV8x69g%2FxK1vhYlZg%2BzwKXPfLyTQphju%2FELelPmqmaaxp4NCVyDApEa7XYkOQOa1iozy5GYi9Hfj1L9736%2BzWk2BsA8n5sZnMIK%2FyTdSHCpNWNYqv0GhwjNB8x5ryBr5MAvXSfpBJsz9lcMheUjjTlUc1DY7fTfSWQ6s6drAEPBsMLzx%2BrwGOqUBheWH9tPTIjkc4NznxNrGl7SzKMKFym5C9qmeJAUY4Q4KzBBowqQumKton%2FhWW2a6dr6eh%2Bs8uEt11jS5ZKvG8DP%2FpLhBfFb5TXmjcGBdG1vD6vB%2FHdiqafzxiWHh3Ru8s633cozZ%2F5FE0SvbDujLVytg3m8nvFX%2BJUG47DzLJ3wpOYylpNBO64HNKODrNvZAey56mjQw9p4XSX94f6uXbtGob9np&X-Amz-Signature=0a4e7f317e6fe077703cba2b9182119ce77984226a3b42b3c626840cd6ac91ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELE4CTN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQk7YPHWX40DDHhPhQihIaB5mmUU%2BasoMMjJoLvqKhFgIgRlsy4IyyCUDGSKTjvhvcaHrBbTM%2FmdE4KWSeewvGjKMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKM%2Fw01r6pIqKbLSuSrcA4oaeXei1hB34%2FM%2F4W2h7ZERkjqwmxRoZqoy%2Bj3pCXHe6YDho%2FngZRqA%2FsJLCIxQhuTrHiyM%2B8GK4LHu023dpa9TlL9Dcq9SiCY9%2B50%2FHkbpwMvTZCRjzN%2BLQfkq7d%2B9ZKPbIYnqAtN4b5Ke70OpmkNL2UD3BtyiJf0ILDWfyhu7ywFC%2BtkrIYO1mqjg4VNta%2BUoqKT0ivVvpKF3xHYHjYNGclgjIOSSQTcOfN8auhVUMZmlBpqhwFR6ndHjYHM6e0AtYDRsj%2F9Fm1NDTAFeA3%2BM0xohSBQvsaEOPEc1w6G8M7REvDv%2BzfK9LoQIQhpu89xI%2B0lNKC1sAPYU%2BQSxgro0ybmBGjoS8camvm5mbMFEdbeFN5O1zlFt%2BZOX5Dc4aeOncxRF5pmAjAviQ32IA2Mzkb9I7JQIX9wy83oKKZZuL6jvigpqWTJTGEgcUy8GGiWclPHUm9iddipdJV8x69g%2FxK1vhYlZg%2BzwKXPfLyTQphju%2FELelPmqmaaxp4NCVyDApEa7XYkOQOa1iozy5GYi9Hfj1L9736%2BzWk2BsA8n5sZnMIK%2FyTdSHCpNWNYqv0GhwjNB8x5ryBr5MAvXSfpBJsz9lcMheUjjTlUc1DY7fTfSWQ6s6drAEPBsMLzx%2BrwGOqUBheWH9tPTIjkc4NznxNrGl7SzKMKFym5C9qmeJAUY4Q4KzBBowqQumKton%2FhWW2a6dr6eh%2Bs8uEt11jS5ZKvG8DP%2FpLhBfFb5TXmjcGBdG1vD6vB%2FHdiqafzxiWHh3Ru8s633cozZ%2F5FE0SvbDujLVytg3m8nvFX%2BJUG47DzLJ3wpOYylpNBO64HNKODrNvZAey56mjQw9p4XSX94f6uXbtGob9np&X-Amz-Signature=cad9ba0f6c3788324026edb193d4fd3b3653a0a2744a2022e35e68a791d0024f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELE4CTN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQk7YPHWX40DDHhPhQihIaB5mmUU%2BasoMMjJoLvqKhFgIgRlsy4IyyCUDGSKTjvhvcaHrBbTM%2FmdE4KWSeewvGjKMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKM%2Fw01r6pIqKbLSuSrcA4oaeXei1hB34%2FM%2F4W2h7ZERkjqwmxRoZqoy%2Bj3pCXHe6YDho%2FngZRqA%2FsJLCIxQhuTrHiyM%2B8GK4LHu023dpa9TlL9Dcq9SiCY9%2B50%2FHkbpwMvTZCRjzN%2BLQfkq7d%2B9ZKPbIYnqAtN4b5Ke70OpmkNL2UD3BtyiJf0ILDWfyhu7ywFC%2BtkrIYO1mqjg4VNta%2BUoqKT0ivVvpKF3xHYHjYNGclgjIOSSQTcOfN8auhVUMZmlBpqhwFR6ndHjYHM6e0AtYDRsj%2F9Fm1NDTAFeA3%2BM0xohSBQvsaEOPEc1w6G8M7REvDv%2BzfK9LoQIQhpu89xI%2B0lNKC1sAPYU%2BQSxgro0ybmBGjoS8camvm5mbMFEdbeFN5O1zlFt%2BZOX5Dc4aeOncxRF5pmAjAviQ32IA2Mzkb9I7JQIX9wy83oKKZZuL6jvigpqWTJTGEgcUy8GGiWclPHUm9iddipdJV8x69g%2FxK1vhYlZg%2BzwKXPfLyTQphju%2FELelPmqmaaxp4NCVyDApEa7XYkOQOa1iozy5GYi9Hfj1L9736%2BzWk2BsA8n5sZnMIK%2FyTdSHCpNWNYqv0GhwjNB8x5ryBr5MAvXSfpBJsz9lcMheUjjTlUc1DY7fTfSWQ6s6drAEPBsMLzx%2BrwGOqUBheWH9tPTIjkc4NznxNrGl7SzKMKFym5C9qmeJAUY4Q4KzBBowqQumKton%2FhWW2a6dr6eh%2Bs8uEt11jS5ZKvG8DP%2FpLhBfFb5TXmjcGBdG1vD6vB%2FHdiqafzxiWHh3Ru8s633cozZ%2F5FE0SvbDujLVytg3m8nvFX%2BJUG47DzLJ3wpOYylpNBO64HNKODrNvZAey56mjQw9p4XSX94f6uXbtGob9np&X-Amz-Signature=fa93b8866617ee2b62d491d4444dbbf64c3c7622481f0907e66bd16ce9cdf8af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELE4CTN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQk7YPHWX40DDHhPhQihIaB5mmUU%2BasoMMjJoLvqKhFgIgRlsy4IyyCUDGSKTjvhvcaHrBbTM%2FmdE4KWSeewvGjKMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKM%2Fw01r6pIqKbLSuSrcA4oaeXei1hB34%2FM%2F4W2h7ZERkjqwmxRoZqoy%2Bj3pCXHe6YDho%2FngZRqA%2FsJLCIxQhuTrHiyM%2B8GK4LHu023dpa9TlL9Dcq9SiCY9%2B50%2FHkbpwMvTZCRjzN%2BLQfkq7d%2B9ZKPbIYnqAtN4b5Ke70OpmkNL2UD3BtyiJf0ILDWfyhu7ywFC%2BtkrIYO1mqjg4VNta%2BUoqKT0ivVvpKF3xHYHjYNGclgjIOSSQTcOfN8auhVUMZmlBpqhwFR6ndHjYHM6e0AtYDRsj%2F9Fm1NDTAFeA3%2BM0xohSBQvsaEOPEc1w6G8M7REvDv%2BzfK9LoQIQhpu89xI%2B0lNKC1sAPYU%2BQSxgro0ybmBGjoS8camvm5mbMFEdbeFN5O1zlFt%2BZOX5Dc4aeOncxRF5pmAjAviQ32IA2Mzkb9I7JQIX9wy83oKKZZuL6jvigpqWTJTGEgcUy8GGiWclPHUm9iddipdJV8x69g%2FxK1vhYlZg%2BzwKXPfLyTQphju%2FELelPmqmaaxp4NCVyDApEa7XYkOQOa1iozy5GYi9Hfj1L9736%2BzWk2BsA8n5sZnMIK%2FyTdSHCpNWNYqv0GhwjNB8x5ryBr5MAvXSfpBJsz9lcMheUjjTlUc1DY7fTfSWQ6s6drAEPBsMLzx%2BrwGOqUBheWH9tPTIjkc4NznxNrGl7SzKMKFym5C9qmeJAUY4Q4KzBBowqQumKton%2FhWW2a6dr6eh%2Bs8uEt11jS5ZKvG8DP%2FpLhBfFb5TXmjcGBdG1vD6vB%2FHdiqafzxiWHh3Ru8s633cozZ%2F5FE0SvbDujLVytg3m8nvFX%2BJUG47DzLJ3wpOYylpNBO64HNKODrNvZAey56mjQw9p4XSX94f6uXbtGob9np&X-Amz-Signature=0b003a4c5bc91e97e5004eb47d646cfaa8dc21f4808eedc2c9ea13bf73b3d624&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SYJ7VNN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCoGMB%2B9%2FFkn75wdHeGxgekRvkXtMyf4n4eSI5WmR1%2B4AIgB6%2FsmozeWtp2ZZfhOhJcYmA9DeWn21unrBt7mgIFnYEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOOJemv7HpWpLh5hpircAzFoBC42Q5YZi1WLTsGLTHAt7laNBuVteXAhOl8WCGwk2WR7z5eTzEjMAwu%2Bym1o%2FM%2BrijO4qpQk%2FUs%2BIewAs9zV43Fj5PqBClyfDQr8jxs2UgWnA6tbFPaHyD0Njq312VfAoQpZOJnI2N1fwKHuc1oSZcSyTeDLB5UH4DwJAXobA3%2FFDQmthu7UR9PEIaNmuIwiP3kV5J4ZbpvhxOJKUUV%2B6XkOJIFJ7VzIk49cnWOcHLSIBHqjfteEFPk1it2x5xYmvofSe6KQBXHdpYb%2Fvgb55zVlOCiDLM3PIzuEbC7oY%2F2Mbh5K%2BkU7YdPo3LTk%2Fk1wEynqFyxgb%2Fgqdt6okA0I%2F5uXFuOyyE3a7LZISN%2BO0GUz8dl%2FLH%2BWezFPClfPi%2FYVPe%2BTol07eko%2FBbDaRNXmG4vAZ%2FogD8Qiv%2BswQBm8k14q8TduYBsS3nTStvk1DqcW2Sf6U6nTB0zsVgHFUYt4%2BamMECqsIQ09vkhje4QoK4xBDPAwV%2ByBaH304iEpjBbEwTxq3nhwsFYekGpEcL4jE9RHunDCH1Otfi9HYjb7aNHTkKTb%2BnuejmywEiFjiG7gWklws8UWwgnwa9Sk92kBi2RMRoTp%2BGZTgJxZhYP1yNffRKviAgsFRe9fMOTx%2BrwGOqUBHz68hbJk%2BTPLOW0ZOWeAbzaloLJTgtj%2FzbXq%2Bh%2FBqE0C2uZDy3IbbWIACATxZ2pFyaesHlXpO9%2BUivhnr639%2B6Nf9YhJ2AZyGx0SCyHyjqvuuPRhB9A5iY1TxwQpsrkghDq7M9UdHfZRpqCNHj3Lg3LdcnIVw9bvQPpQv%2BfGY5xsGqtovM%2FADyMz%2BQHLfcFEflKryjYet1kTjRcsXr6VHHmU35M5&X-Amz-Signature=6352470fb69e7ee988d1bc373a12c9176edade20cdcc977a606817133f1c0de8&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W2KA6HM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMJltHz2qOBT1JSkNjpF3mIm2uqK19P3gPaN8y%2Fv%2FZUwIgGGTIVkoNBz4wYNzfQ952YmuXXM6Qsxtu%2FV%2F0VAUpsQoqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMSMf96u3Y5E%2FSlo9CrcAzxVH1ulaklj%2Be8AFgWbG1Oof6EoaXZPhlgB5Rou6l7KUy4Lyp9z6WKQ4HjKDnKFt8TQeEH%2BlJCeHKUfvTJrdqj4dZBIut8NnQ8X1DMS5B4jAntb9IF5zKqPk53grjrGEWVaEMZ2HB65LquKlLylg1YNWD%2FtHVz3Xrngmv6dyvMtKjzDTHI4LsoD01jfQr0RD%2BuVUktBpYvKPoam7ediOzgSxkCtJu6AynmyJWeM7oaSB6mvMjuFK2etaaYnSFQqEG8tBIQqbHltDtJ9peSOtLpw5%2BNWE5Ebgvz9RtukOEcP2xXFlO7O5T2Dcupl7Dh4K8ZrAJAXcpfs%2Bkqf33VsRxx33KyCoyaNvlq94c%2FF0fpEotOFdlabpI4dAZhAdSMFx1sL8blU%2FND6mVHX4r8akEF1FUUlT8StpxADVKC7RoVtTPqngXN0b8GYRamkmlDM88i8%2BpFI%2F7gGSKiTgLqKC3SbQDVSckannUtrax2gHBNaIAbVg0ohGOKB4PAUa4wlx7hLSYEVDtpGqXOPfSf3ypvIu8X0szd5TQfhrQpqUkGBDaj9mnr%2Fk8vmflYoyStWeH5C5Gxn948ynK4RFF20YyAJqsTIxiWu8NSMpzgkJFPIcfu2j08ko35Bt4f1MPfx%2BrwGOqUBrEg9sH4O1O8bKOoDIQzMW%2BpNJvNb%2B21KftNT7%2FcuIZG6IkgvbsvbMBJuRfBZH%2Fb1XghRCAHPUukYMEPlfy0WC%2FqfpczYIpy8paAVaA1oyTK57Onz3u0h2X%2BuuMv94nGadQsEOJIkZ65aJzvd1tXfXyBmIwum7Ro1HeRu7Z%2BDEqyvpfmEVJgeZ%2BS1fcww6RXQvItYPhk43iScMTUBhUQ6psnegCTr&X-Amz-Signature=f7acd8a9a6a81f10b44b852abf91b76efd7bb0c267fdb927a77a5dd7321fab15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELE4CTN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQk7YPHWX40DDHhPhQihIaB5mmUU%2BasoMMjJoLvqKhFgIgRlsy4IyyCUDGSKTjvhvcaHrBbTM%2FmdE4KWSeewvGjKMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKM%2Fw01r6pIqKbLSuSrcA4oaeXei1hB34%2FM%2F4W2h7ZERkjqwmxRoZqoy%2Bj3pCXHe6YDho%2FngZRqA%2FsJLCIxQhuTrHiyM%2B8GK4LHu023dpa9TlL9Dcq9SiCY9%2B50%2FHkbpwMvTZCRjzN%2BLQfkq7d%2B9ZKPbIYnqAtN4b5Ke70OpmkNL2UD3BtyiJf0ILDWfyhu7ywFC%2BtkrIYO1mqjg4VNta%2BUoqKT0ivVvpKF3xHYHjYNGclgjIOSSQTcOfN8auhVUMZmlBpqhwFR6ndHjYHM6e0AtYDRsj%2F9Fm1NDTAFeA3%2BM0xohSBQvsaEOPEc1w6G8M7REvDv%2BzfK9LoQIQhpu89xI%2B0lNKC1sAPYU%2BQSxgro0ybmBGjoS8camvm5mbMFEdbeFN5O1zlFt%2BZOX5Dc4aeOncxRF5pmAjAviQ32IA2Mzkb9I7JQIX9wy83oKKZZuL6jvigpqWTJTGEgcUy8GGiWclPHUm9iddipdJV8x69g%2FxK1vhYlZg%2BzwKXPfLyTQphju%2FELelPmqmaaxp4NCVyDApEa7XYkOQOa1iozy5GYi9Hfj1L9736%2BzWk2BsA8n5sZnMIK%2FyTdSHCpNWNYqv0GhwjNB8x5ryBr5MAvXSfpBJsz9lcMheUjjTlUc1DY7fTfSWQ6s6drAEPBsMLzx%2BrwGOqUBheWH9tPTIjkc4NznxNrGl7SzKMKFym5C9qmeJAUY4Q4KzBBowqQumKton%2FhWW2a6dr6eh%2Bs8uEt11jS5ZKvG8DP%2FpLhBfFb5TXmjcGBdG1vD6vB%2FHdiqafzxiWHh3Ru8s633cozZ%2F5FE0SvbDujLVytg3m8nvFX%2BJUG47DzLJ3wpOYylpNBO64HNKODrNvZAey56mjQw9p4XSX94f6uXbtGob9np&X-Amz-Signature=f32c685f934a032cfedf37521c539bbca7ca4a5d119fc45b6d4872668d71a68d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELE4CTN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQk7YPHWX40DDHhPhQihIaB5mmUU%2BasoMMjJoLvqKhFgIgRlsy4IyyCUDGSKTjvhvcaHrBbTM%2FmdE4KWSeewvGjKMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKM%2Fw01r6pIqKbLSuSrcA4oaeXei1hB34%2FM%2F4W2h7ZERkjqwmxRoZqoy%2Bj3pCXHe6YDho%2FngZRqA%2FsJLCIxQhuTrHiyM%2B8GK4LHu023dpa9TlL9Dcq9SiCY9%2B50%2FHkbpwMvTZCRjzN%2BLQfkq7d%2B9ZKPbIYnqAtN4b5Ke70OpmkNL2UD3BtyiJf0ILDWfyhu7ywFC%2BtkrIYO1mqjg4VNta%2BUoqKT0ivVvpKF3xHYHjYNGclgjIOSSQTcOfN8auhVUMZmlBpqhwFR6ndHjYHM6e0AtYDRsj%2F9Fm1NDTAFeA3%2BM0xohSBQvsaEOPEc1w6G8M7REvDv%2BzfK9LoQIQhpu89xI%2B0lNKC1sAPYU%2BQSxgro0ybmBGjoS8camvm5mbMFEdbeFN5O1zlFt%2BZOX5Dc4aeOncxRF5pmAjAviQ32IA2Mzkb9I7JQIX9wy83oKKZZuL6jvigpqWTJTGEgcUy8GGiWclPHUm9iddipdJV8x69g%2FxK1vhYlZg%2BzwKXPfLyTQphju%2FELelPmqmaaxp4NCVyDApEa7XYkOQOa1iozy5GYi9Hfj1L9736%2BzWk2BsA8n5sZnMIK%2FyTdSHCpNWNYqv0GhwjNB8x5ryBr5MAvXSfpBJsz9lcMheUjjTlUc1DY7fTfSWQ6s6drAEPBsMLzx%2BrwGOqUBheWH9tPTIjkc4NznxNrGl7SzKMKFym5C9qmeJAUY4Q4KzBBowqQumKton%2FhWW2a6dr6eh%2Bs8uEt11jS5ZKvG8DP%2FpLhBfFb5TXmjcGBdG1vD6vB%2FHdiqafzxiWHh3Ru8s633cozZ%2F5FE0SvbDujLVytg3m8nvFX%2BJUG47DzLJ3wpOYylpNBO64HNKODrNvZAey56mjQw9p4XSX94f6uXbtGob9np&X-Amz-Signature=09e9ac8c658bf329ac67f97a38fdba762d1e34d5b2643700c8344e1fecf6e7e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELE4CTN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQk7YPHWX40DDHhPhQihIaB5mmUU%2BasoMMjJoLvqKhFgIgRlsy4IyyCUDGSKTjvhvcaHrBbTM%2FmdE4KWSeewvGjKMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKM%2Fw01r6pIqKbLSuSrcA4oaeXei1hB34%2FM%2F4W2h7ZERkjqwmxRoZqoy%2Bj3pCXHe6YDho%2FngZRqA%2FsJLCIxQhuTrHiyM%2B8GK4LHu023dpa9TlL9Dcq9SiCY9%2B50%2FHkbpwMvTZCRjzN%2BLQfkq7d%2B9ZKPbIYnqAtN4b5Ke70OpmkNL2UD3BtyiJf0ILDWfyhu7ywFC%2BtkrIYO1mqjg4VNta%2BUoqKT0ivVvpKF3xHYHjYNGclgjIOSSQTcOfN8auhVUMZmlBpqhwFR6ndHjYHM6e0AtYDRsj%2F9Fm1NDTAFeA3%2BM0xohSBQvsaEOPEc1w6G8M7REvDv%2BzfK9LoQIQhpu89xI%2B0lNKC1sAPYU%2BQSxgro0ybmBGjoS8camvm5mbMFEdbeFN5O1zlFt%2BZOX5Dc4aeOncxRF5pmAjAviQ32IA2Mzkb9I7JQIX9wy83oKKZZuL6jvigpqWTJTGEgcUy8GGiWclPHUm9iddipdJV8x69g%2FxK1vhYlZg%2BzwKXPfLyTQphju%2FELelPmqmaaxp4NCVyDApEa7XYkOQOa1iozy5GYi9Hfj1L9736%2BzWk2BsA8n5sZnMIK%2FyTdSHCpNWNYqv0GhwjNB8x5ryBr5MAvXSfpBJsz9lcMheUjjTlUc1DY7fTfSWQ6s6drAEPBsMLzx%2BrwGOqUBheWH9tPTIjkc4NznxNrGl7SzKMKFym5C9qmeJAUY4Q4KzBBowqQumKton%2FhWW2a6dr6eh%2Bs8uEt11jS5ZKvG8DP%2FpLhBfFb5TXmjcGBdG1vD6vB%2FHdiqafzxiWHh3Ru8s633cozZ%2F5FE0SvbDujLVytg3m8nvFX%2BJUG47DzLJ3wpOYylpNBO64HNKODrNvZAey56mjQw9p4XSX94f6uXbtGob9np&X-Amz-Signature=7a901458bad18193cfb9b84157baf4a25f0138a52defd0c0f00a96a3fc8dec5a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645QUMZMQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcc44kASAUjR1ArokpM8wDKLs7g8kjmSSJKwV6ioSPPQIhAProsPAkqXtXKz%2FIyqlLNPFknXmLCoPzQRG9nNldd1bCKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzXToFLkixKGWWEbF8q3APhC%2FSdODy4L7HdCYJ3%2BGyPNfv0xVD8X%2FZUtjOcAZktbQyksPQK6gyWbavuehxFmx0HzBsKLs5TZd%2Fzvv8KPXBBIknPyqYHyQrlE9FDc5nidPHMnJQyOmzHvIgAQU%2BJ%2F8F4fmqZLvRQSw%2B1pnLAq0ydzc5OYFQ4fvn%2F6%2BO%2B6kisklixHZvOOLCAyNS%2BMwptrtjGU8zGKGPd%2BtFrhEcV43Ux9Ns7%2F%2Bq%2B5H%2BZVv6hwu6IVM2S7s8U5dxdTmAzu%2BybxafC4Hexq7nX3KYPBTT4IuQVRLzXwW%2BS5%2BQGLJdOlrmUyBNGr9cm8b2l6qj%2B869%2FZRl9tWgmq9S%2FHpAsFgcr17mgyXZyCrdiZWnSsp2aH0R55AnB5v05c2uAk12Pq6siFYVvOpVdP%2B1ijKPky5abRCSFG3bjV2dy7e448p3bdgsvpASYNZrVgyvn%2BbC0T68KVqtuPQ0VUhITIp1frusHUHLpzYdhKJL74CBNGjUkHpxHldA88X3bYCLCFjelKTHRaj4t%2BSSpSrw1FdQyvSfkrafe0gEVaFwsK9NwJ28HghrGQwVugZreWgE0PyTklxSU%2Bdm3qkTuofVqZIFl%2Fyz9vi%2Fm6MGBJULYy8wi9buFT0AJkEs5hGBNYhWBFDDiMjC68fq8BjqkAWh0hG4nzs7nDBEunpEBKxbJSaUhS0mSnJAhq5lq77kNDGq5rpg%2BE8YsoeyfXQuLKOdc7ojBbqRuaOixS9AbD9UCBHTg98tLYysIwJORiXkKC9yxOBDUDn11ofWPVF%2BxJJbOCbk9%2BpSW8wUtpXxyNt2QcnSfUIH%2FQkhiWKJkDeE3D5QxslmLwqx5QlCN7Vn7lBtrrgFQSNCoaGWOc0OPG7C%2FTfqr&X-Amz-Signature=699396730ecda29eae650a0a846eea33368186264cbabcf4d7373fd2d85e7628&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MBH2VG6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2iaWvP9QerMosKbcphGU2IzL6ygojRUBivvTfXtTxwQIgCQTNzcFAGH%2FcO0%2FmrGNN4dgf6s2cPvDN5RmtgjLEDhwqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdA0lLFN8k5hgX1MCrcA7dG%2BbcvDWJMIHr4XB5Gr%2Fkrm%2F7N61O2A5mPh3qIAJT0rzIV8GxAb676ehfQ2bx6rqmvg7WzVVbX7aHbereYAQ7N48AlRe4S8mfKCn1mTPn41V9AEpZdXMfSQgw1qq34ruGu%2BicUOCUjfIYdtRTLrq124%2FaYM0xsPBQkk8e%2FVredrQVRdmmdbiw7lIasEYQaE7SOsxIxPkvJMNo5K1i5T9pzrgNryPhoA1t7cD%2FRL9JCxckc5VWNExNqowyQ3Qkrz0ltVepkBTeX2ChBldftCeE1KsobneU2Y121YS38ZMR%2BLIL7QXnHLIiAU39fP8eFBW3TguV8cuBjF%2F4KYsPnlr7hmBo37Fd%2B4fBFoe9qOJse87573Rz5gIRkfdZ5%2BNklzTIhknaAEMNux4o2iIpkuvgAO6tYfDmW7VrA7ZgKzRlO2HBr01Tpt8%2FGetj%2Be4mbjz3fk7Bry5QSDazYM1tfwkQakbU1aIgEQlMHgqHPRK1eUlTCNLWQ1z%2B7uYczR1v4oUcFY5%2Fbuc%2FE7gsXGtLRnLF4PHOu4%2BvFn3PF4dApBEVF0AWGfTZpW15Au0SMQDGRS6J5nUTfzr04V5iNge204rdf8HxNgabcst5ipQcYelj7%2FiZwr8ka2SvlcRwlMLnx%2BrwGOqUBSdwsVLUc7vf2%2FF%2FrN4q6xMbo5G0PpQKXhYmwrg6nNJ8qHOdxY%2FQeiglFUwhR%2FruYoOloTuhW18U1sBUd6JvWtA%2FKZpeD2OdSHXZHhPZhePk7KyvAkcMTcx%2BbOpnGEVP3fn78EzcGMntkB%2FnhauNWrbv6O7tf9hNpIynjVCDqwZbSCdw2YxQcHUvpljXKkGusEf%2B2l49O88rnTEj%2F82T2acaSL71G&X-Amz-Signature=2040a15f3926a8f8a0672ab211d3443c21d576c01b7e99c94071571af43ea0a6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBUFBNQF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFuGLKWeYqRiE04fXTy%2BEdhM22OV7rLr8MkO4mYBvJC9AiAeXYUC9ji6gKAEnktRb5tB3ATMFHYDs1WYrhujIKq1%2ByqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKnNqnYXs41F%2Fkv6EKtwDJwgk6jJwCyjcYWr9KsODbZ7IwryEXEEl%2Fw8J%2B%2BaAtjMtpJV%2FWGSgEke26MSoSpuUrMaodU11lppbTeVJKkWEJ0scPbZMngolektB8pnLJGACdNdWuiDDO3Vt9ilu63raVa8R1LYbwQfVP1ldQIgC1lc%2B57Cpm8UT5%2BHKIQ2%2FddSsXzLZtUH3aLrYleTevi3HLbFBFHQ7rhJWLBIArHt4UQdzSsVtDzOQEVCSPdDRlYMZ30ygsLbaGtNW1IMSoEuvKMz5UhLfXoJTUX%2BsQi7LrbLqLPkyx0NvW6fYN6cNKnb%2BcchojCaQgKNuw6OzOqNdBnWuAUAzo0kqtujKXFjrF4OE1JwFFCp9W3dbuMNJUwOoqgR0oRhKVq8%2BgiXD9ta%2Bnl6i%2B%2Fx%2BqL92Sz0miFI6Gh%2BJUQzGr5OeMr%2Be2NkgepGgWz%2BQKqlqUVSjP9XjmUftSLG6v0nwwlSyBhdMMjbhsJ93F4U1rtxeqUNaP9rqBTFJ4a5fNyJN%2FjxCz4p87CInSyQg5CRPSHeNTZWKpr67SA2f6GmA30bqtfQjgMwjdsuIbhrwG4T8B1kkUfTxsTvGzfpoab07XM6bfW3x%2FxXec99j1ZsWvLvTx5avD6JIOd7UHFoVIu9UpKA8sT8w2vH6vAY6pgGpnC7rtpX69dYl9mUT1wVhcG%2BejGFThE70sKX2LRm%2BVRasBRpMAe56KmOTL40E9Ve63K%2FVE2LiR8qBY9xUIUlUDf7pmQqex5l4IIvzcYMNgxhLQ58hIABxMFHPBMObY1t3PB036HFPbvKin3k4alylHt8YGn3mhiXFHgNwG8AnbpWD1oUQv%2FsTcZdZpJELlnVtr47l8T%2FO1GhckUOnHLYo7v%2BJRl0h&X-Amz-Signature=68a04460688b1e1a093591145938b880e4e56f1def9eb5d825ae63dba2a811ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJNDWAKP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCh3ooR1E%2FtRG1JZFmpJbryGr6FKeXV8xKi4QdQ1GQBHQIgTUxxQ2CRzFyZZUTl%2BzwSepWMR61hPjNA4PDOMjmZPQ8qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFTDPHYEy92PLyk0BCrcA4%2B67%2BG1gRJ5Rmf1eK9EacoOVGHBzUxK0DWXmP%2FhBM5qF677cv6%2F3wxTa8blhfC5ww%2B4E2qxv3qiy74%2FHFwP1BypvYjWhustNDmCCt9HvPtnKDL7F2lxAGOT5nb%2FW%2FiB6NJE%2BOh%2BClgC2WAnspyHl6VJr0KKDriEKRkeOrb41yfDXLpS1TMSn2U%2BbvF1peGoKSDbZlaFRgd3e2lAr7qg5GcJ5u0ao%2Fuad5ldmQi3i4Qz1VGbaXbLD4Ixz2cSXeADiBJhyeFK2r%2BpL%2Bg6zfNVIHlGzurdXcQmdVMuQ6cZIjUkyL2a1%2FvjXkE%2Bhm38vPRJemw%2Frrmhe2lTKrdfF6sNrXZFc4Q4ditHGNUS0aCn1LUSyV9g9qej4ROqX%2BvdcdEZLTsn%2Br4MeqDQAEBmYBbSA%2B8IgNk%2FZK02C3b4H6lHelkb%2F%2B3sVdlwfpiIZbzcNvrcuOw%2BNUs%2BcG4tB7K%2FqDbZHsFb1CYGDmD3vkm2%2FmwNTVib5lFIfYNhO4cLQXBrMrm3fbH2SfvkEsHcGIas9g6SKyO%2BezVAhTNyRMktYHhy7dLRLLI8dgKiavBE6S8ogzm3c2yLwmrhBw%2FWXro60VBrIW1jymTyGt76iVM60jHH2MVq9FcNSMGFZ%2BRJz4YsMOTx%2BrwGOqUBX7PDJLd2Y4OvnQRwKdWTHnYXcuRNrweYczSBaDr3xMSXOenVNNrVJUMNLgs5cn5slS2ket46%2FpvijW8LOMRitOW5qjR9%2FMR5axS6jOkgls3FpPHh1G5WWMpAG5VH2Yyent31lPHJTUPKmWt%2B%2B3m03KbLPoyOYyZAjFFyJ%2BFUIgGWuEiZ3V5bROpFdy5qoSA39hE3UJSVRHFCWrtyw251TVvhQRau&X-Amz-Signature=e8a59a19f1caeca1f0ea9ad6c743d0a571119d4f0362c22b74ad2c7c8c92f823&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJNDWAKP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCh3ooR1E%2FtRG1JZFmpJbryGr6FKeXV8xKi4QdQ1GQBHQIgTUxxQ2CRzFyZZUTl%2BzwSepWMR61hPjNA4PDOMjmZPQ8qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFTDPHYEy92PLyk0BCrcA4%2B67%2BG1gRJ5Rmf1eK9EacoOVGHBzUxK0DWXmP%2FhBM5qF677cv6%2F3wxTa8blhfC5ww%2B4E2qxv3qiy74%2FHFwP1BypvYjWhustNDmCCt9HvPtnKDL7F2lxAGOT5nb%2FW%2FiB6NJE%2BOh%2BClgC2WAnspyHl6VJr0KKDriEKRkeOrb41yfDXLpS1TMSn2U%2BbvF1peGoKSDbZlaFRgd3e2lAr7qg5GcJ5u0ao%2Fuad5ldmQi3i4Qz1VGbaXbLD4Ixz2cSXeADiBJhyeFK2r%2BpL%2Bg6zfNVIHlGzurdXcQmdVMuQ6cZIjUkyL2a1%2FvjXkE%2Bhm38vPRJemw%2Frrmhe2lTKrdfF6sNrXZFc4Q4ditHGNUS0aCn1LUSyV9g9qej4ROqX%2BvdcdEZLTsn%2Br4MeqDQAEBmYBbSA%2B8IgNk%2FZK02C3b4H6lHelkb%2F%2B3sVdlwfpiIZbzcNvrcuOw%2BNUs%2BcG4tB7K%2FqDbZHsFb1CYGDmD3vkm2%2FmwNTVib5lFIfYNhO4cLQXBrMrm3fbH2SfvkEsHcGIas9g6SKyO%2BezVAhTNyRMktYHhy7dLRLLI8dgKiavBE6S8ogzm3c2yLwmrhBw%2FWXro60VBrIW1jymTyGt76iVM60jHH2MVq9FcNSMGFZ%2BRJz4YsMOTx%2BrwGOqUBX7PDJLd2Y4OvnQRwKdWTHnYXcuRNrweYczSBaDr3xMSXOenVNNrVJUMNLgs5cn5slS2ket46%2FpvijW8LOMRitOW5qjR9%2FMR5axS6jOkgls3FpPHh1G5WWMpAG5VH2Yyent31lPHJTUPKmWt%2B%2B3m03KbLPoyOYyZAjFFyJ%2BFUIgGWuEiZ3V5bROpFdy5qoSA39hE3UJSVRHFCWrtyw251TVvhQRau&X-Amz-Signature=9a9b0ce03217f15df035fb795e92b8ba62d03236976cb7ace99df63aed8a0e72&X-Amz-SignedHeaders=host&x-id=GetObject)

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
