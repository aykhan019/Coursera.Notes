

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BBAUNRD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFZj2ZkwQvKKO99TWNCJlSfJEmD7QtE1Ir290Ef%2BOVEAAiB83NySwSAkyygKF7fyNz5NqpI72%2FpaY6tLJonqMHTN9iqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd%2B9IF5INU%2BJ3WuOBKtwDA6CJI5bD8qqC75hDAxBqQHj6nqJNmnh%2FW%2Fo8KQ7G%2BdWJyoKqYesoexQ%2FrAATBHBQsle0KtNkiwU1lj6qeyEJdZZNrvcN58PqYA6EOiIbU%2B3icGK3LzLkfZJxfAcFcBkICZwTgRAps4jNUc%2F2Bsnkst4JDj68J7WSaLs2gsQ4PzNGdy9k%2FCeNiQMIImmGMBzu5Xm4hZe3Q2bDU95VtYhWJ3HvUFrEmct2KVFO7wVcpQPniAwkOsmLi8MlMg8XIW1v63EX%2F07zX2LhC4AEv1XqrDSkagPf5GV4G6Z%2F%2F%2FpFmMkqdI0OQvnCQnO4WQCVVhYq%2FXG04w6DLhgmTfLO0Q7m9R6zdP5ls805hfdVGY5BVKLK0qXt4yCaDsQVblpw4Qg5wiun%2FAKf9msOjW59OZoq2ztbaVW9SyUJXXDKZcglOty2tR2%2Bo599B6LQTPqcNke6zby%2BlaPygVVuSV%2FpeXMKrwL9WPoe%2FE4AcuJRFjwQoVosl0HZnBYq%2BwddpDwyTe7m1QbkjGd1HKNjM0%2FJi9IPclIzVmLqfjFgDPDnRf68b4i1eCF7EeOn%2BToi9WdRKPoB1C982rHP2vLo%2FklNw9MEFEIJOw5Sk49IfjTrzfo5AjfIXO0XtDRjvDeXZu4whK3zvAY6pgE8O2FobhXw%2F8vcElTUCQTTQLGnMF2tPjhhHnKReotBGiCK7oL7KWo8Ra0HXEBAdCOEk5Pt6TY7YWBpzOEhpSwG6xVDlIgi2koyBf3flrrZh41x%2FDAzorCsEO%2B0v7RSmG%2BChKNL9msQS2kj11WJ%2FoHNFf3q%2FHU9ECfyTY0jgMCWLfobaxmcaIni%2BFZbDfsFKCG1%2FMJs9lRgUrR%2B7A1W1DzHiunFIgeT&X-Amz-Signature=f2ca989d5f269c2e5c26302d337f4a921a1d614763191f7ac37f4c0764d3a852&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BBAUNRD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFZj2ZkwQvKKO99TWNCJlSfJEmD7QtE1Ir290Ef%2BOVEAAiB83NySwSAkyygKF7fyNz5NqpI72%2FpaY6tLJonqMHTN9iqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd%2B9IF5INU%2BJ3WuOBKtwDA6CJI5bD8qqC75hDAxBqQHj6nqJNmnh%2FW%2Fo8KQ7G%2BdWJyoKqYesoexQ%2FrAATBHBQsle0KtNkiwU1lj6qeyEJdZZNrvcN58PqYA6EOiIbU%2B3icGK3LzLkfZJxfAcFcBkICZwTgRAps4jNUc%2F2Bsnkst4JDj68J7WSaLs2gsQ4PzNGdy9k%2FCeNiQMIImmGMBzu5Xm4hZe3Q2bDU95VtYhWJ3HvUFrEmct2KVFO7wVcpQPniAwkOsmLi8MlMg8XIW1v63EX%2F07zX2LhC4AEv1XqrDSkagPf5GV4G6Z%2F%2F%2FpFmMkqdI0OQvnCQnO4WQCVVhYq%2FXG04w6DLhgmTfLO0Q7m9R6zdP5ls805hfdVGY5BVKLK0qXt4yCaDsQVblpw4Qg5wiun%2FAKf9msOjW59OZoq2ztbaVW9SyUJXXDKZcglOty2tR2%2Bo599B6LQTPqcNke6zby%2BlaPygVVuSV%2FpeXMKrwL9WPoe%2FE4AcuJRFjwQoVosl0HZnBYq%2BwddpDwyTe7m1QbkjGd1HKNjM0%2FJi9IPclIzVmLqfjFgDPDnRf68b4i1eCF7EeOn%2BToi9WdRKPoB1C982rHP2vLo%2FklNw9MEFEIJOw5Sk49IfjTrzfo5AjfIXO0XtDRjvDeXZu4whK3zvAY6pgE8O2FobhXw%2F8vcElTUCQTTQLGnMF2tPjhhHnKReotBGiCK7oL7KWo8Ra0HXEBAdCOEk5Pt6TY7YWBpzOEhpSwG6xVDlIgi2koyBf3flrrZh41x%2FDAzorCsEO%2B0v7RSmG%2BChKNL9msQS2kj11WJ%2FoHNFf3q%2FHU9ECfyTY0jgMCWLfobaxmcaIni%2BFZbDfsFKCG1%2FMJs9lRgUrR%2B7A1W1DzHiunFIgeT&X-Amz-Signature=91f2e46b5d49e56aa0490b701cbc0f7fb076149c918eef4144f4d56eca7fb8c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BBAUNRD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFZj2ZkwQvKKO99TWNCJlSfJEmD7QtE1Ir290Ef%2BOVEAAiB83NySwSAkyygKF7fyNz5NqpI72%2FpaY6tLJonqMHTN9iqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd%2B9IF5INU%2BJ3WuOBKtwDA6CJI5bD8qqC75hDAxBqQHj6nqJNmnh%2FW%2Fo8KQ7G%2BdWJyoKqYesoexQ%2FrAATBHBQsle0KtNkiwU1lj6qeyEJdZZNrvcN58PqYA6EOiIbU%2B3icGK3LzLkfZJxfAcFcBkICZwTgRAps4jNUc%2F2Bsnkst4JDj68J7WSaLs2gsQ4PzNGdy9k%2FCeNiQMIImmGMBzu5Xm4hZe3Q2bDU95VtYhWJ3HvUFrEmct2KVFO7wVcpQPniAwkOsmLi8MlMg8XIW1v63EX%2F07zX2LhC4AEv1XqrDSkagPf5GV4G6Z%2F%2F%2FpFmMkqdI0OQvnCQnO4WQCVVhYq%2FXG04w6DLhgmTfLO0Q7m9R6zdP5ls805hfdVGY5BVKLK0qXt4yCaDsQVblpw4Qg5wiun%2FAKf9msOjW59OZoq2ztbaVW9SyUJXXDKZcglOty2tR2%2Bo599B6LQTPqcNke6zby%2BlaPygVVuSV%2FpeXMKrwL9WPoe%2FE4AcuJRFjwQoVosl0HZnBYq%2BwddpDwyTe7m1QbkjGd1HKNjM0%2FJi9IPclIzVmLqfjFgDPDnRf68b4i1eCF7EeOn%2BToi9WdRKPoB1C982rHP2vLo%2FklNw9MEFEIJOw5Sk49IfjTrzfo5AjfIXO0XtDRjvDeXZu4whK3zvAY6pgE8O2FobhXw%2F8vcElTUCQTTQLGnMF2tPjhhHnKReotBGiCK7oL7KWo8Ra0HXEBAdCOEk5Pt6TY7YWBpzOEhpSwG6xVDlIgi2koyBf3flrrZh41x%2FDAzorCsEO%2B0v7RSmG%2BChKNL9msQS2kj11WJ%2FoHNFf3q%2FHU9ECfyTY0jgMCWLfobaxmcaIni%2BFZbDfsFKCG1%2FMJs9lRgUrR%2B7A1W1DzHiunFIgeT&X-Amz-Signature=cfca9c67ecefc698537a96378ff4131ec137c7f35ed4953d58d5879eae611780&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HKTN63G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMeVPv9oFBvSbSVQud87UyZ8aZ2FnrT0iiEjRtC3rHiAiAemuC8MlcR%2Fa0bIREU7c6dJ3AOFlhza%2BhYoxoP3IhZhCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMniCuBKhbMtfHrjhhKtwDlXGJFgtDW23b0NIoG020cFg5iUrSsZC2HnAcCCKArMh3v%2F4Qah4dvYk0MMz8JmWs0iikOfe8qCZEmxhselQrL09NmYOwF5U4s%2BUP1vPsOSk%2Fuk3sqW0z%2BL1%2Fw3K%2BhTkLbDob4r50ukoX1lJMniQm4C5Vdq9jITOZdXpN2MnvhfvMSSm53Mq1a1%2FGeu2TfCoMybBwT4U5hdtj293GgnCwsued6raxyNg17dOPrxJC54j%2FVx5rg2EXlcNESHGK%2BcNF4et3P8nWWgH2Sb1Az3SlneCI853wJUpBxUszl9mUiFXnANDm89PZR%2B7YYMBPE97p10Q1RuXMitbMMCGZaf91KNQMZqsv0RdBHU6UGMdxVWSQlctIw6bq3TJiAArxaN0t%2FunCrRz%2BRfqOcGkEqpC3NBia0u48%2BEPxX0bq6CcJ3xYSUwK2oAWpIw171IgjQ3%2BOxK0Ry6VjWxxihkhg0EXKzlp0LfH2v57nFeIA6aBrQXCZIeSJInhafBQt7fUuX5jb7bgirpcTwJilUBq8Oi3Yi0P%2FSSEz5pdCX6%2B8GxPWnhZekzDdfyJg9G6WAwJoEsI6TRTERSj8E1cxu3NVBdnGd%2BwPgszOVC7m%2F3Kyr4KV8La4diWtEfvOnUvuAsMwzazzvAY6pgGOOzPjOs53QfdjJp3Kpl5GOu%2Fujar33XY4v0prOowHd0rd%2Fj%2F4lUH8cMHL0NizgeG0irDefhBE5qZNvId2v2phnJ4QoEOO0Pf1qwllcTswqkhPhLtLPpC5I52cdI1fZfP8uPVzbpkKI5LLPWGzUyNKcIu0Dsqmf7izJ%2BpBngJ%2B1azvYBSYk33aJk6iLSE91cyFwywl8O1EOg77A2ptJzzJ%2B8OVIDVJ&X-Amz-Signature=96b7aa3b6556e0f508ce220d257e24cc30cfe2eeac8c0fe97344b24e8cb7040f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HKTN63G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMeVPv9oFBvSbSVQud87UyZ8aZ2FnrT0iiEjRtC3rHiAiAemuC8MlcR%2Fa0bIREU7c6dJ3AOFlhza%2BhYoxoP3IhZhCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMniCuBKhbMtfHrjhhKtwDlXGJFgtDW23b0NIoG020cFg5iUrSsZC2HnAcCCKArMh3v%2F4Qah4dvYk0MMz8JmWs0iikOfe8qCZEmxhselQrL09NmYOwF5U4s%2BUP1vPsOSk%2Fuk3sqW0z%2BL1%2Fw3K%2BhTkLbDob4r50ukoX1lJMniQm4C5Vdq9jITOZdXpN2MnvhfvMSSm53Mq1a1%2FGeu2TfCoMybBwT4U5hdtj293GgnCwsued6raxyNg17dOPrxJC54j%2FVx5rg2EXlcNESHGK%2BcNF4et3P8nWWgH2Sb1Az3SlneCI853wJUpBxUszl9mUiFXnANDm89PZR%2B7YYMBPE97p10Q1RuXMitbMMCGZaf91KNQMZqsv0RdBHU6UGMdxVWSQlctIw6bq3TJiAArxaN0t%2FunCrRz%2BRfqOcGkEqpC3NBia0u48%2BEPxX0bq6CcJ3xYSUwK2oAWpIw171IgjQ3%2BOxK0Ry6VjWxxihkhg0EXKzlp0LfH2v57nFeIA6aBrQXCZIeSJInhafBQt7fUuX5jb7bgirpcTwJilUBq8Oi3Yi0P%2FSSEz5pdCX6%2B8GxPWnhZekzDdfyJg9G6WAwJoEsI6TRTERSj8E1cxu3NVBdnGd%2BwPgszOVC7m%2F3Kyr4KV8La4diWtEfvOnUvuAsMwzazzvAY6pgGOOzPjOs53QfdjJp3Kpl5GOu%2Fujar33XY4v0prOowHd0rd%2Fj%2F4lUH8cMHL0NizgeG0irDefhBE5qZNvId2v2phnJ4QoEOO0Pf1qwllcTswqkhPhLtLPpC5I52cdI1fZfP8uPVzbpkKI5LLPWGzUyNKcIu0Dsqmf7izJ%2BpBngJ%2B1azvYBSYk33aJk6iLSE91cyFwywl8O1EOg77A2ptJzzJ%2B8OVIDVJ&X-Amz-Signature=64e2d82b1c0b86bd80dd8ccaf879a2c12af3f4d213bf595ad852f1c60e583599&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HKTN63G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMeVPv9oFBvSbSVQud87UyZ8aZ2FnrT0iiEjRtC3rHiAiAemuC8MlcR%2Fa0bIREU7c6dJ3AOFlhza%2BhYoxoP3IhZhCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMniCuBKhbMtfHrjhhKtwDlXGJFgtDW23b0NIoG020cFg5iUrSsZC2HnAcCCKArMh3v%2F4Qah4dvYk0MMz8JmWs0iikOfe8qCZEmxhselQrL09NmYOwF5U4s%2BUP1vPsOSk%2Fuk3sqW0z%2BL1%2Fw3K%2BhTkLbDob4r50ukoX1lJMniQm4C5Vdq9jITOZdXpN2MnvhfvMSSm53Mq1a1%2FGeu2TfCoMybBwT4U5hdtj293GgnCwsued6raxyNg17dOPrxJC54j%2FVx5rg2EXlcNESHGK%2BcNF4et3P8nWWgH2Sb1Az3SlneCI853wJUpBxUszl9mUiFXnANDm89PZR%2B7YYMBPE97p10Q1RuXMitbMMCGZaf91KNQMZqsv0RdBHU6UGMdxVWSQlctIw6bq3TJiAArxaN0t%2FunCrRz%2BRfqOcGkEqpC3NBia0u48%2BEPxX0bq6CcJ3xYSUwK2oAWpIw171IgjQ3%2BOxK0Ry6VjWxxihkhg0EXKzlp0LfH2v57nFeIA6aBrQXCZIeSJInhafBQt7fUuX5jb7bgirpcTwJilUBq8Oi3Yi0P%2FSSEz5pdCX6%2B8GxPWnhZekzDdfyJg9G6WAwJoEsI6TRTERSj8E1cxu3NVBdnGd%2BwPgszOVC7m%2F3Kyr4KV8La4diWtEfvOnUvuAsMwzazzvAY6pgGOOzPjOs53QfdjJp3Kpl5GOu%2Fujar33XY4v0prOowHd0rd%2Fj%2F4lUH8cMHL0NizgeG0irDefhBE5qZNvId2v2phnJ4QoEOO0Pf1qwllcTswqkhPhLtLPpC5I52cdI1fZfP8uPVzbpkKI5LLPWGzUyNKcIu0Dsqmf7izJ%2BpBngJ%2B1azvYBSYk33aJk6iLSE91cyFwywl8O1EOg77A2ptJzzJ%2B8OVIDVJ&X-Amz-Signature=095921f5166e152828cfe8a200087cef29689575d9c54bbbfaef01b648a11c3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HKTN63G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMeVPv9oFBvSbSVQud87UyZ8aZ2FnrT0iiEjRtC3rHiAiAemuC8MlcR%2Fa0bIREU7c6dJ3AOFlhza%2BhYoxoP3IhZhCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMniCuBKhbMtfHrjhhKtwDlXGJFgtDW23b0NIoG020cFg5iUrSsZC2HnAcCCKArMh3v%2F4Qah4dvYk0MMz8JmWs0iikOfe8qCZEmxhselQrL09NmYOwF5U4s%2BUP1vPsOSk%2Fuk3sqW0z%2BL1%2Fw3K%2BhTkLbDob4r50ukoX1lJMniQm4C5Vdq9jITOZdXpN2MnvhfvMSSm53Mq1a1%2FGeu2TfCoMybBwT4U5hdtj293GgnCwsued6raxyNg17dOPrxJC54j%2FVx5rg2EXlcNESHGK%2BcNF4et3P8nWWgH2Sb1Az3SlneCI853wJUpBxUszl9mUiFXnANDm89PZR%2B7YYMBPE97p10Q1RuXMitbMMCGZaf91KNQMZqsv0RdBHU6UGMdxVWSQlctIw6bq3TJiAArxaN0t%2FunCrRz%2BRfqOcGkEqpC3NBia0u48%2BEPxX0bq6CcJ3xYSUwK2oAWpIw171IgjQ3%2BOxK0Ry6VjWxxihkhg0EXKzlp0LfH2v57nFeIA6aBrQXCZIeSJInhafBQt7fUuX5jb7bgirpcTwJilUBq8Oi3Yi0P%2FSSEz5pdCX6%2B8GxPWnhZekzDdfyJg9G6WAwJoEsI6TRTERSj8E1cxu3NVBdnGd%2BwPgszOVC7m%2F3Kyr4KV8La4diWtEfvOnUvuAsMwzazzvAY6pgGOOzPjOs53QfdjJp3Kpl5GOu%2Fujar33XY4v0prOowHd0rd%2Fj%2F4lUH8cMHL0NizgeG0irDefhBE5qZNvId2v2phnJ4QoEOO0Pf1qwllcTswqkhPhLtLPpC5I52cdI1fZfP8uPVzbpkKI5LLPWGzUyNKcIu0Dsqmf7izJ%2BpBngJ%2B1azvYBSYk33aJk6iLSE91cyFwywl8O1EOg77A2ptJzzJ%2B8OVIDVJ&X-Amz-Signature=d140994df751e15148f3817633e765e1a237a998375c9988bd86dcd158fb82c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HKTN63G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMeVPv9oFBvSbSVQud87UyZ8aZ2FnrT0iiEjRtC3rHiAiAemuC8MlcR%2Fa0bIREU7c6dJ3AOFlhza%2BhYoxoP3IhZhCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMniCuBKhbMtfHrjhhKtwDlXGJFgtDW23b0NIoG020cFg5iUrSsZC2HnAcCCKArMh3v%2F4Qah4dvYk0MMz8JmWs0iikOfe8qCZEmxhselQrL09NmYOwF5U4s%2BUP1vPsOSk%2Fuk3sqW0z%2BL1%2Fw3K%2BhTkLbDob4r50ukoX1lJMniQm4C5Vdq9jITOZdXpN2MnvhfvMSSm53Mq1a1%2FGeu2TfCoMybBwT4U5hdtj293GgnCwsued6raxyNg17dOPrxJC54j%2FVx5rg2EXlcNESHGK%2BcNF4et3P8nWWgH2Sb1Az3SlneCI853wJUpBxUszl9mUiFXnANDm89PZR%2B7YYMBPE97p10Q1RuXMitbMMCGZaf91KNQMZqsv0RdBHU6UGMdxVWSQlctIw6bq3TJiAArxaN0t%2FunCrRz%2BRfqOcGkEqpC3NBia0u48%2BEPxX0bq6CcJ3xYSUwK2oAWpIw171IgjQ3%2BOxK0Ry6VjWxxihkhg0EXKzlp0LfH2v57nFeIA6aBrQXCZIeSJInhafBQt7fUuX5jb7bgirpcTwJilUBq8Oi3Yi0P%2FSSEz5pdCX6%2B8GxPWnhZekzDdfyJg9G6WAwJoEsI6TRTERSj8E1cxu3NVBdnGd%2BwPgszOVC7m%2F3Kyr4KV8La4diWtEfvOnUvuAsMwzazzvAY6pgGOOzPjOs53QfdjJp3Kpl5GOu%2Fujar33XY4v0prOowHd0rd%2Fj%2F4lUH8cMHL0NizgeG0irDefhBE5qZNvId2v2phnJ4QoEOO0Pf1qwllcTswqkhPhLtLPpC5I52cdI1fZfP8uPVzbpkKI5LLPWGzUyNKcIu0Dsqmf7izJ%2BpBngJ%2B1azvYBSYk33aJk6iLSE91cyFwywl8O1EOg77A2ptJzzJ%2B8OVIDVJ&X-Amz-Signature=8096226bc612cfc7a7aba12750655347e01583c6a8956e513fdf71cc0212e511&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HKTN63G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMeVPv9oFBvSbSVQud87UyZ8aZ2FnrT0iiEjRtC3rHiAiAemuC8MlcR%2Fa0bIREU7c6dJ3AOFlhza%2BhYoxoP3IhZhCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMniCuBKhbMtfHrjhhKtwDlXGJFgtDW23b0NIoG020cFg5iUrSsZC2HnAcCCKArMh3v%2F4Qah4dvYk0MMz8JmWs0iikOfe8qCZEmxhselQrL09NmYOwF5U4s%2BUP1vPsOSk%2Fuk3sqW0z%2BL1%2Fw3K%2BhTkLbDob4r50ukoX1lJMniQm4C5Vdq9jITOZdXpN2MnvhfvMSSm53Mq1a1%2FGeu2TfCoMybBwT4U5hdtj293GgnCwsued6raxyNg17dOPrxJC54j%2FVx5rg2EXlcNESHGK%2BcNF4et3P8nWWgH2Sb1Az3SlneCI853wJUpBxUszl9mUiFXnANDm89PZR%2B7YYMBPE97p10Q1RuXMitbMMCGZaf91KNQMZqsv0RdBHU6UGMdxVWSQlctIw6bq3TJiAArxaN0t%2FunCrRz%2BRfqOcGkEqpC3NBia0u48%2BEPxX0bq6CcJ3xYSUwK2oAWpIw171IgjQ3%2BOxK0Ry6VjWxxihkhg0EXKzlp0LfH2v57nFeIA6aBrQXCZIeSJInhafBQt7fUuX5jb7bgirpcTwJilUBq8Oi3Yi0P%2FSSEz5pdCX6%2B8GxPWnhZekzDdfyJg9G6WAwJoEsI6TRTERSj8E1cxu3NVBdnGd%2BwPgszOVC7m%2F3Kyr4KV8La4diWtEfvOnUvuAsMwzazzvAY6pgGOOzPjOs53QfdjJp3Kpl5GOu%2Fujar33XY4v0prOowHd0rd%2Fj%2F4lUH8cMHL0NizgeG0irDefhBE5qZNvId2v2phnJ4QoEOO0Pf1qwllcTswqkhPhLtLPpC5I52cdI1fZfP8uPVzbpkKI5LLPWGzUyNKcIu0Dsqmf7izJ%2BpBngJ%2B1azvYBSYk33aJk6iLSE91cyFwywl8O1EOg77A2ptJzzJ%2B8OVIDVJ&X-Amz-Signature=08af68e997cd375dc83cd9694d6660082055abbdad6cbf5b2f039c88f70a9964&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RX6GAJF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3AUuTmyIi6v7iq3buR%2BX97yeA4rkB8G6QmE5gIvf%2BxQIgIQSYIUlB4iC0nMCW%2Bsc72M1ldW5891rEjRG4kUDnNZ0qiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIoOdXiKlvliwnlg0SrcA58qbLxrmySmzR2OUCxmE4%2BMLX4Op6eQEv5zzZP09WzUaMUlj7yIaGm0Axz29bb6iftHVziK4ZEcOIuY4K85Pbt4llVjzOH0Cy0TMO54qlFyNabczkDZJjKY4bkXsILvTvVeYpg7J2AuheG5kMqTNiSk8Jrkb3CwOXQghc7sLsK9SJEF4%2FWFFv%2BQmiSSHgQqZFYv8v%2FbL5YuEm%2BpaoxRrcUlq1wHOoBO75ESxK0evprrZ7qVewzuis9PvD1Xhl1yx%2BjT83R61I759%2BNa1N3DFSN1X%2B6R9TX2VLJeJ%2BTb3%2FBJrP%2FSupmwhkMmCde1uQ0o5eFZWnB6KzA6zL%2BXNaDgh7pNqwMYgMRb0K0RqBUaqn3SKKpx0iMYiuaqKOoGP6fUDNbPeXvV1SFBZUul3VnaJFIUDktdZt%2ByKYTuZkepxXnQf3f7LOhxhELdpJ04TBD8Cv1x%2BiIs%2FTTKABE%2BAo4nEw6d%2FGLkvh9rxetpWmy%2ByDB8AaPNwtnrunJbRi%2BY9gtMiBRK44ZshpHqZHvocAtpSUH0a1Ankq4FyupapVhHWEpy3PA6J%2BeXqt4H7wiLnuwwZ%2BlH5Gl5AdKRdJBQb9eE2JiOkHu9S%2FaXflqKFVIFP3a5E6YrZdb9BcWZWBKAMLus87wGOqUBc20QViFB3u8oeMI9XoZ2iETMwHP2F9ftqt9GwAHCsvJfuny40j%2Bxu4TgQsTWg7VPrAlv9v4W8MQvhFaXuBw9kdFVfNAjikX48%2BDK3A%2BpHzSgCA0FjgONiJ7PB5OXV%2FDOXpKDVqJDuhp6iG38AXhuTkuErA3%2BJ56r5putN8aE3iY6TCeJAQFAaWp7%2FYu7P6EKoZ32Z%2BDP9TJka983Bg53o%2B8g8lMV&X-Amz-Signature=720dd5c9307e5d5793880dcdf6762757c00ca567f8742f36a8899c5bcf562442&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZASIYAX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDneGXgf4hdIThlOl9jKhpU7gJkPgiHdCfku4oc4eWsxwIhALolx5L5EHrI3ZYa0P5eC8t3%2FJ4GtjkV8%2BXAPNggDwhhKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLISjvan%2BCSm3vbaAq3AMjsGmsKGHnq3Ff1hN%2BcbvveFNicRr1XO6MDz1FFt5HOB%2BctkyUtYc5Utf3xkWpYjBhnpjh3yl574RYc9TlXJSrVY7jYhqhsNT4v7XOgdPzdmFJdlF2yWTlqp%2F60sfF4FPWrA%2FijKweW%2BxdptFWdk0W3z%2FsUu6OdZ%2FrpbxJ1pAhgRb60WjlAWKpBDP12JP%2BE9VG3ZTTHsNwtSDjlwKXVQhnr%2B64vL1RZVy5UrIqIW5nxppdnULv%2BpTh6jMz2P5tb7TQ0ghG0CuXFtPSQq0s%2F5M85bAnT5plqKml9JEdiZZW99VtsTG8u%2BvmC5Nzt7vaHFcxnkcOfVqH4%2BJKhaZfFP9KL1yiB%2BkRHwK%2F2PZl3psMDZrSLxwuSsOfbLVjxBOPiHGbobW%2Fhj11z0ajUbJItJH3Zcjln6y3vPPGC5Rsv%2BN1NK3eEQylww1b5ltbyGQwBsU1GdGFJaO5vG84yzBPhqc%2BrvbyYkAGhfSKGyrBzaE6PvkzLcKPzYVKBefB7PttHpl2ZwjReVAb4xcTsE9zSDZZcDpI1IpMYU7UiAYP7i3KIQWmpYV%2BiP5EkTgEpVXHLo%2BpyXU3JOp%2F%2FTYE%2BeuS7O5qcsmKE5VvEZma5VjdUCoEQ0%2FA%2B%2BS%2FEkuNkSyVEjC6rPO8BjqkAcwlE7KjlTn6E9gD4EqhQPsm%2B9Y%2BcuVlzpcS22X1R%2BpAREYdJsOyOoUb1PZBlj1qVcxSN5dQ4I1F2eXlM4HP6W9y4E86ZUlWP7scuE0iqginFZj%2Bod2ocetS5DJv2PNoLViQ6AIFVxfB7ahN%2BM4qV4zKoW66GeP%2FN6sQ4UdC%2F2bkJGhQXKhS7m6eqXaM1JNvOQlbG6tJ8b9fsXpenqM9%2Fh95Ngwb&X-Amz-Signature=5380f07d4b4874e1a2ce771ace285be606ad9a7f97c033a4272eb4ea58fd0b36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HKTN63G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMeVPv9oFBvSbSVQud87UyZ8aZ2FnrT0iiEjRtC3rHiAiAemuC8MlcR%2Fa0bIREU7c6dJ3AOFlhza%2BhYoxoP3IhZhCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMniCuBKhbMtfHrjhhKtwDlXGJFgtDW23b0NIoG020cFg5iUrSsZC2HnAcCCKArMh3v%2F4Qah4dvYk0MMz8JmWs0iikOfe8qCZEmxhselQrL09NmYOwF5U4s%2BUP1vPsOSk%2Fuk3sqW0z%2BL1%2Fw3K%2BhTkLbDob4r50ukoX1lJMniQm4C5Vdq9jITOZdXpN2MnvhfvMSSm53Mq1a1%2FGeu2TfCoMybBwT4U5hdtj293GgnCwsued6raxyNg17dOPrxJC54j%2FVx5rg2EXlcNESHGK%2BcNF4et3P8nWWgH2Sb1Az3SlneCI853wJUpBxUszl9mUiFXnANDm89PZR%2B7YYMBPE97p10Q1RuXMitbMMCGZaf91KNQMZqsv0RdBHU6UGMdxVWSQlctIw6bq3TJiAArxaN0t%2FunCrRz%2BRfqOcGkEqpC3NBia0u48%2BEPxX0bq6CcJ3xYSUwK2oAWpIw171IgjQ3%2BOxK0Ry6VjWxxihkhg0EXKzlp0LfH2v57nFeIA6aBrQXCZIeSJInhafBQt7fUuX5jb7bgirpcTwJilUBq8Oi3Yi0P%2FSSEz5pdCX6%2B8GxPWnhZekzDdfyJg9G6WAwJoEsI6TRTERSj8E1cxu3NVBdnGd%2BwPgszOVC7m%2F3Kyr4KV8La4diWtEfvOnUvuAsMwzazzvAY6pgGOOzPjOs53QfdjJp3Kpl5GOu%2Fujar33XY4v0prOowHd0rd%2Fj%2F4lUH8cMHL0NizgeG0irDefhBE5qZNvId2v2phnJ4QoEOO0Pf1qwllcTswqkhPhLtLPpC5I52cdI1fZfP8uPVzbpkKI5LLPWGzUyNKcIu0Dsqmf7izJ%2BpBngJ%2B1azvYBSYk33aJk6iLSE91cyFwywl8O1EOg77A2ptJzzJ%2B8OVIDVJ&X-Amz-Signature=858de5a61924587c6a1931d5ec6e82815ab3a19c7751f59c46c700647ad1e661&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HKTN63G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMeVPv9oFBvSbSVQud87UyZ8aZ2FnrT0iiEjRtC3rHiAiAemuC8MlcR%2Fa0bIREU7c6dJ3AOFlhza%2BhYoxoP3IhZhCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMniCuBKhbMtfHrjhhKtwDlXGJFgtDW23b0NIoG020cFg5iUrSsZC2HnAcCCKArMh3v%2F4Qah4dvYk0MMz8JmWs0iikOfe8qCZEmxhselQrL09NmYOwF5U4s%2BUP1vPsOSk%2Fuk3sqW0z%2BL1%2Fw3K%2BhTkLbDob4r50ukoX1lJMniQm4C5Vdq9jITOZdXpN2MnvhfvMSSm53Mq1a1%2FGeu2TfCoMybBwT4U5hdtj293GgnCwsued6raxyNg17dOPrxJC54j%2FVx5rg2EXlcNESHGK%2BcNF4et3P8nWWgH2Sb1Az3SlneCI853wJUpBxUszl9mUiFXnANDm89PZR%2B7YYMBPE97p10Q1RuXMitbMMCGZaf91KNQMZqsv0RdBHU6UGMdxVWSQlctIw6bq3TJiAArxaN0t%2FunCrRz%2BRfqOcGkEqpC3NBia0u48%2BEPxX0bq6CcJ3xYSUwK2oAWpIw171IgjQ3%2BOxK0Ry6VjWxxihkhg0EXKzlp0LfH2v57nFeIA6aBrQXCZIeSJInhafBQt7fUuX5jb7bgirpcTwJilUBq8Oi3Yi0P%2FSSEz5pdCX6%2B8GxPWnhZekzDdfyJg9G6WAwJoEsI6TRTERSj8E1cxu3NVBdnGd%2BwPgszOVC7m%2F3Kyr4KV8La4diWtEfvOnUvuAsMwzazzvAY6pgGOOzPjOs53QfdjJp3Kpl5GOu%2Fujar33XY4v0prOowHd0rd%2Fj%2F4lUH8cMHL0NizgeG0irDefhBE5qZNvId2v2phnJ4QoEOO0Pf1qwllcTswqkhPhLtLPpC5I52cdI1fZfP8uPVzbpkKI5LLPWGzUyNKcIu0Dsqmf7izJ%2BpBngJ%2B1azvYBSYk33aJk6iLSE91cyFwywl8O1EOg77A2ptJzzJ%2B8OVIDVJ&X-Amz-Signature=7edb7c264b9eb375e99c775014ae724d2e08a9852e05c93df5042a2782921920&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HKTN63G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMeVPv9oFBvSbSVQud87UyZ8aZ2FnrT0iiEjRtC3rHiAiAemuC8MlcR%2Fa0bIREU7c6dJ3AOFlhza%2BhYoxoP3IhZhCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMniCuBKhbMtfHrjhhKtwDlXGJFgtDW23b0NIoG020cFg5iUrSsZC2HnAcCCKArMh3v%2F4Qah4dvYk0MMz8JmWs0iikOfe8qCZEmxhselQrL09NmYOwF5U4s%2BUP1vPsOSk%2Fuk3sqW0z%2BL1%2Fw3K%2BhTkLbDob4r50ukoX1lJMniQm4C5Vdq9jITOZdXpN2MnvhfvMSSm53Mq1a1%2FGeu2TfCoMybBwT4U5hdtj293GgnCwsued6raxyNg17dOPrxJC54j%2FVx5rg2EXlcNESHGK%2BcNF4et3P8nWWgH2Sb1Az3SlneCI853wJUpBxUszl9mUiFXnANDm89PZR%2B7YYMBPE97p10Q1RuXMitbMMCGZaf91KNQMZqsv0RdBHU6UGMdxVWSQlctIw6bq3TJiAArxaN0t%2FunCrRz%2BRfqOcGkEqpC3NBia0u48%2BEPxX0bq6CcJ3xYSUwK2oAWpIw171IgjQ3%2BOxK0Ry6VjWxxihkhg0EXKzlp0LfH2v57nFeIA6aBrQXCZIeSJInhafBQt7fUuX5jb7bgirpcTwJilUBq8Oi3Yi0P%2FSSEz5pdCX6%2B8GxPWnhZekzDdfyJg9G6WAwJoEsI6TRTERSj8E1cxu3NVBdnGd%2BwPgszOVC7m%2F3Kyr4KV8La4diWtEfvOnUvuAsMwzazzvAY6pgGOOzPjOs53QfdjJp3Kpl5GOu%2Fujar33XY4v0prOowHd0rd%2Fj%2F4lUH8cMHL0NizgeG0irDefhBE5qZNvId2v2phnJ4QoEOO0Pf1qwllcTswqkhPhLtLPpC5I52cdI1fZfP8uPVzbpkKI5LLPWGzUyNKcIu0Dsqmf7izJ%2BpBngJ%2B1azvYBSYk33aJk6iLSE91cyFwywl8O1EOg77A2ptJzzJ%2B8OVIDVJ&X-Amz-Signature=0780fb0a7ff103b023bc598b895a04381f8db02a35af84da38226e1535b3dc1e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBJYYU6P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4%2FDO29rhxgbLQOQrRBlFFaunEAT5VSWykvDBUuIcwgAIgeVOV7Yrf66ExE%2FNHKuCxhDpe3btQSAfwZ%2F8vqd6UGi0qiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDMRm%2B%2BHvK4LfuJueCrcAyzr2ZMBrGf6lOTJ1eCq8iBvDrhCzFYJ7NVJ9Y2wFJPpUdZKdLdVbj0Ysae%2FcvmX17c%2Ff13FueYZ94MOJ1qKvqZmzAOUfYvqN9qUdde7f1Uwvq7%2B0F2JRq6AIdf5E%2BATYgXKw0oUdMtpSBC1xAGzU%2Fo6V46sYWAQz%2B67%2FiYlpwm7OzauUkGMgN07S3%2BYXCd1P36o6jj%2FYYjmi7woYqMtpLuF4edm7slZ7wcFPxGiWfHuL%2FT36EDubSNSADLtSSyOmXNCAzXwRxwxx7fQtXoUta%2Bt%2BAzGHZwy7097gcKjh8g%2Bca9VKrCXrRuyJjvAoMpS1M%2BS5LiqPDyYOtmvc7ZbILXHJ1AxCixaKPvskQcx10LFWN%2BgoHlCZyaEHnfql2Dqlo8Fi%2FlGGTNNpSNSM9xgSvaae4PqWwQXHTEy2r7rTZFi2N0QbVS6ih0ESv%2Bkv7mwl7hV6TBJtsJM7kEnNHePlb0XVMNbLhEmWuz668QM5uLmQThoDSvSObzh1EYbp1BJxdlnFoSO2u%2FZosCJEyrzTyCNjB8w9SR2UMzSw1GUfKL0hc7GMkSrYfZKPH%2FNBHtKcWf1JwnKdbFrMUAqK71qps73D3f%2F%2FOPxuMi%2Bp6IWKJTbr2wvBenFyS2DUCzVMMas87wGOqUB2hMNmV5SpiRrghBIRhQUk7NgQ7SLBsxnfF9kn%2FXoHMlb3Pkg0PEV%2Baq4nEjkTNGVaP0JkMnVTbJE0b3GHbTokKRdyMk%2BJihfQPexTO3zcdLyYz5Ttp4IR3yGCyxFTofljpnKg843boRqMkvqmGp0Tpwi8gOTCmRFnTvWgf%2BhiApTlx61M5304nXvdnbBNxF%2FSXXnS1tCPyjEJruuCDG7S373RM3O&X-Amz-Signature=ae4362e941f7589dd37fc52327d834fbe50cd0ebead39e06a71a33152765ac7b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663B4LXZXO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICEsMfKFFMTdrmhL4pOZDGHQYhjsgtSfULwOayc%2FG%2B%2FXAiBuM6eyLLmh5JMtHQpzkQ1t5RrG34tOpCnABNPaXtVxYSqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8ypiOwmgtG8gR7jlKtwDzDFV3ycNXNK%2FWf14baMYf74dMxPrct29Wvd2IQOT9ugeVgfNur0ofVQHbNEM71yF1o6si3DEkxNca84EDbQHdg%2F7HhJYjfOHfDLmCySRSV6frxPtMkvCnJPxDsFgeIZrq8oeK1PfwmsccE5guUtYSVtYYVC2zOAlg8btSQalLAPJVh94cyQSctIJzHMI5MrToIrWGgj9xrEx4ICEIWj5d6%2F1%2FAlT3Gp99wmue0CrAsmb%2BOIBRX0Iblb6nLPartSR%2FWQZNYT%2FqoWGkKOWb%2BCxsx6%2FfnpEQ6JivhcyuJYQXuQGdtN%2FokUWO5bRXO0xfVsp2wFvxaOvMZL%2FQ88i493qe2WSg6ApfnWToLUer1PRs%2BRw1YBdXoEK6C8fgH6FUpDSHTS2N%2F%2BXYGgrJUh6hhT%2B1fbs4He7u6qqq%2Bjvw9Jr2ru38WSqQAdJ9jwiM0cbGt1RiSf9ovVvK1fdRITwwxej0Qsfx5pGNoZOAlvbxrBdgYj%2Bwno5evEAeNmeqDKv7uU548RF03HHalaMS0JMCXKz8LxTkCdmuNJhqwHGjW4UfG0Tq20ceDNkiSAB2s6tElAMJDCua1m4C24HftqS%2FHj%2Bi322loAAoQacWKw1zS7PDme9VqqPdQa6cBW1%2FygwsKzzvAY6pgEMvMayO57mgrlIC5uawg7xm5XoL%2BPz13JaxAR21bdmmcsNoK8t%2BTDecIjzjygOUS50CZSuB7%2B6ECoo6HdwHnXAApdEWNkO84Mlx0PYGWy4GWa6Xxlv0rxOvkSoZZjd46lGKDBj4FMCqGyFm3wloNJ7DhOAMGmItCgcznjxYyCZScvKZ4AAUnmYc98509T5l%2F1JjTMmLx6pMIkKj74khqO%2F6GAWJrL%2F&X-Amz-Signature=4e186736eda63a69f7636c940406d54adf1f747561a0d5ad8d7af00e9bb1e707&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRHZIHEJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8C5u1DYQgeT3lYPbXtxnKSgGizdN%2FlfiUrukkPNxPxwIgfkHXY5gjqofi6nVBefaLm9zt3M0UQJrAzHiZY5cD5TIqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPTUvRqW7rDEy8tGlyrcAyxMS0iVFSkh0YeMEQ875PtnAJS9oyeMj7c0OTZxZtvdRG6J0EZNhDFBbR5lfoTnWv3A65Y4S5tR%2BKvxACTZs%2F%2BHEPwyCwQMfOzqk4BtZZg20R7WP7EJXSF0LIY7gJRyr3SnNf8VQQPcc9wGTR4RoXFsIceYf17KTK%2BLKLLOOz60fuILotbMaDxhUQ9DaeImuBM8x6mqiNtAoS6fJ0hzFo23r4CJJaf%2B3rwUhaqnimzL%2FQ5t3cn%2FkJ9D%2B48s9QDllLEAtkc6LTWzBw2KJ1pTRgsQ%2BF5BSGLWlUSra2OQwGYbQaySqghE3hemVfVuwGHcsVtsvtidGekr4kl3NSjIpme4M4LHOKNN6U4nSuuzGFSK37jrET6P6NpiNcObPoGWp%2F6SHpr507j8UyVy3f1EFIAdx7dBz%2BMOBA0qVHul0FSCtaZlieD9kyf47nV31k0QSfZ2u4um3kSq60QcFLYDYXPbKZGEaNLYmdrFZ890F1Dg7VFxyjxjdaiMsnsFeYyebZviFtS2s9e64Bb%2FnWsMkTJScB6OC4Agj1i5yjqrIWIlWKISYoDldQL0QTzASjPXnA%2BT%2BTf6ko5TYiFID%2FsbMh08cC76fBkSn%2BZ6jRjg%2FpcLAx5DcDanAwBFyLLTMLKs87wGOqUBogDLHZ9qIXbRaplPDBI3GivQpvSJ6LIoS2JpLMAuBbbgPCe00K%2BsttJN%2BQqVWac%2FiGsWNWUgs3dp8IMP6AlixXnIARlXsMbmluOHm9OvQJLKLX7UE0lvq1XQluCXmaqy3QvKk4FNkCDmdnQG0ZIMQKTe2HDQF%2BhJxN22OIgnPqji81KyN%2F%2Ba%2BTO3EgNSfzfh8dLHxRq6a4m2dID%2BrjzC3RnV9Ylg&X-Amz-Signature=d55eccc8d4b65a97c55e38194476e71547be44424eb830e7cd9f3dfd52152f70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKC3G7AW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGnuHe6IUKNSyg98wYafCn82TIbwgJ%2F7b6epwEs88zdzAiEAivjEBPaw2MBdc0ydnAqe00q3LdJ4ZFXHclrFGLXyp8AqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFs6mH8KiEG%2F06nnNircA56NxJVGFYKyxG90PqEXiXsPmiaqGPNCqvDhc8KvUR6DlBhFEwnRhpqTFAY1IvlaenE3fKYiuGlfyMKuuEFpGMy%2BaYrTfBR%2FwWUSaqmyw40HMUfqHI9aN2gjbo9FqIDW%2BGMNmGPnbaAWU5bh3rIrJlVhe57tpcRgS66hIumsUiof6sEaBEcbViRoeIoEai%2F1golG2YeOt2giiCOWagoO05NXrX7OoZUtHrOkYMHQxej22nOPVXlS%2Fy%2BIhwNLEGDvv1WI9me0n0EPzT7Dcb7EdxT5erA5%2BukbqpMm1jviABJPz6BCStfyohejLO%2FVal0gYPqt2BDWECZzIZklD03U%2Fqcjb%2Bgjua3W4JXViJtx7XKd6Q%2FYRXyfVpZ2yCRayfw4XPVsoTvAoYAWvvlOXc89yb6QoE9If1KqUzLSGmlNmwVad9dwF5w3TWbR1aY4OhzXzzNOzvFZyBzCju1GQTPgmHrTIU%2Fnk%2BpRoaN%2FO4%2FgFmLK2TYch6WgCqnQVc4cWVIxtKko0s8pqlJY6wALG18IzVVNsOLXztg66RHoiZy71Yov03r2kvg7fD%2Fntp%2F4qh%2FXxFrenEas6dbmsMcagPYESpmKGyclfphiF8lYqFAi4X4uk6TlQfEmMjeEYF%2FHMNms87wGOqUBromkLsLSq6xKrM%2Fds7So7c%2FSXv7orzbbQompnTKKC6Bnnkxv8zwPZOHvnoWVMeKMqr1dcwzgR7B0prxETQJH%2BKKBG9Pqav26LX9ZqDvkZSQidUWa9Ly3VFeYGagFESog%2FIh6ayieuKRREESTJykoZRwE7mBjVaw4P4qARpFn0ah0s3%2FNe8wi1Os8Uysmgzm9Xqbklok94Vl4NYGBCw6ZBapotif3&X-Amz-Signature=6b2bcc552abcdafb91959ec93922ed9618798921a5bcdc95bf2b3046fea0b075&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKC3G7AW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGnuHe6IUKNSyg98wYafCn82TIbwgJ%2F7b6epwEs88zdzAiEAivjEBPaw2MBdc0ydnAqe00q3LdJ4ZFXHclrFGLXyp8AqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFs6mH8KiEG%2F06nnNircA56NxJVGFYKyxG90PqEXiXsPmiaqGPNCqvDhc8KvUR6DlBhFEwnRhpqTFAY1IvlaenE3fKYiuGlfyMKuuEFpGMy%2BaYrTfBR%2FwWUSaqmyw40HMUfqHI9aN2gjbo9FqIDW%2BGMNmGPnbaAWU5bh3rIrJlVhe57tpcRgS66hIumsUiof6sEaBEcbViRoeIoEai%2F1golG2YeOt2giiCOWagoO05NXrX7OoZUtHrOkYMHQxej22nOPVXlS%2Fy%2BIhwNLEGDvv1WI9me0n0EPzT7Dcb7EdxT5erA5%2BukbqpMm1jviABJPz6BCStfyohejLO%2FVal0gYPqt2BDWECZzIZklD03U%2Fqcjb%2Bgjua3W4JXViJtx7XKd6Q%2FYRXyfVpZ2yCRayfw4XPVsoTvAoYAWvvlOXc89yb6QoE9If1KqUzLSGmlNmwVad9dwF5w3TWbR1aY4OhzXzzNOzvFZyBzCju1GQTPgmHrTIU%2Fnk%2BpRoaN%2FO4%2FgFmLK2TYch6WgCqnQVc4cWVIxtKko0s8pqlJY6wALG18IzVVNsOLXztg66RHoiZy71Yov03r2kvg7fD%2Fntp%2F4qh%2FXxFrenEas6dbmsMcagPYESpmKGyclfphiF8lYqFAi4X4uk6TlQfEmMjeEYF%2FHMNms87wGOqUBromkLsLSq6xKrM%2Fds7So7c%2FSXv7orzbbQompnTKKC6Bnnkxv8zwPZOHvnoWVMeKMqr1dcwzgR7B0prxETQJH%2BKKBG9Pqav26LX9ZqDvkZSQidUWa9Ly3VFeYGagFESog%2FIh6ayieuKRREESTJykoZRwE7mBjVaw4P4qARpFn0ah0s3%2FNe8wi1Os8Uysmgzm9Xqbklok94Vl4NYGBCw6ZBapotif3&X-Amz-Signature=f1f0fbf22fbf46bf86473479f549dd3b2df9dd6bffb3c1db8da32fda7368f53a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
