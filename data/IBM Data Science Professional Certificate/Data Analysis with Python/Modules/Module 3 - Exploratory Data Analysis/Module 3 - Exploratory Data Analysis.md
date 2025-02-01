

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YR6FT3P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDha1%2FeFbiIxZ5mZRrBGPhl8BMpiUmJNly8BnM5Zi%2BmtwIhAMgbXKzlMSdniH2%2FeJfrx7J6TpHzkVio%2FoBp5CQ0PFWyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxnGvNOBunzT8K0Ploq3AMZR2S9QDSXBSlvY9Xm8BCZ%2BAJvu%2Ba3Ht%2Bv8fRnga2Bs1KpZqPp9Y2pdvno8NkT1Y2n0kojr4zRa59B49C8KtbC0oNukU4JQ%2BL5OPmSpmXFpQU79w4np0DMKa0zHKXLODW0QpQ1vyRjYF5GVMs%2FiFKcKLq24p4s%2Bd1fT2h%2BYHTJVronvw6XcZn7%2BmFM6XFh2YzkU5pC5B%2BuI8lrAvx0SAcS3tzd36mTxhinTF7Z3BvVBl6hgcg7QHo9yYodTIIMTcExqZGUTQPnRkJsiPOhoxEuIu1jGhRoIcZnKx2F8Fki2m7y5Yr3wArXrnDAK7DU52ufbgNblMZuUpFh2z5BKZf8TukAG6xdkzNsisVzy4vGjpOMDpDUryGKTcW3w77hEpk%2B%2F181q3KRzEe8LJTtt1FfCnq2gf6Ti5%2F4YGHRD8jpKKZohatxP9pCyc1se4JwUTSv8pB0scciEGsV8RspIkxCV64IPxiyszaJ9ta%2Ftk1IB5gqcq58rVKqHzdfowdhShFaEvRb1YJD5dV%2BTvlW78%2FPR3puEjU5powTeMU%2BhAfU2nsQ3x5tMBaxYuqKlZbCNXghzxqFfSVj%2B9fc5CGX%2BHOzzB2OpRL%2BgG5exo0GSqJw0ZbAC9KjvoG9d8BHPTDdpPe8BjqkAcM0YI9V2ayHAaB09%2Fy3oiO6uzTxI5396EICcPZTJ%2FRWz1VBBUhiMtjqXL7FlMuMQr3T2bFjxp3F8Z4pFEypLyIwql07TviDIal38EQk7moP133XuzK0yvuBg0ehjyrr5GkMZBWpMuxaWvIogczNTF0UlNo6UIXPBbAILXi378rxjnlHtIoHIKrNOV6P0yI4FbIOBAWeNEXQY4Scd8GHRk8VVx3x&X-Amz-Signature=b7223e67741b9f1d75fa087e0b3827cdb9e35a7d8f3449589fc14066f91a4d64&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YR6FT3P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDha1%2FeFbiIxZ5mZRrBGPhl8BMpiUmJNly8BnM5Zi%2BmtwIhAMgbXKzlMSdniH2%2FeJfrx7J6TpHzkVio%2FoBp5CQ0PFWyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxnGvNOBunzT8K0Ploq3AMZR2S9QDSXBSlvY9Xm8BCZ%2BAJvu%2Ba3Ht%2Bv8fRnga2Bs1KpZqPp9Y2pdvno8NkT1Y2n0kojr4zRa59B49C8KtbC0oNukU4JQ%2BL5OPmSpmXFpQU79w4np0DMKa0zHKXLODW0QpQ1vyRjYF5GVMs%2FiFKcKLq24p4s%2Bd1fT2h%2BYHTJVronvw6XcZn7%2BmFM6XFh2YzkU5pC5B%2BuI8lrAvx0SAcS3tzd36mTxhinTF7Z3BvVBl6hgcg7QHo9yYodTIIMTcExqZGUTQPnRkJsiPOhoxEuIu1jGhRoIcZnKx2F8Fki2m7y5Yr3wArXrnDAK7DU52ufbgNblMZuUpFh2z5BKZf8TukAG6xdkzNsisVzy4vGjpOMDpDUryGKTcW3w77hEpk%2B%2F181q3KRzEe8LJTtt1FfCnq2gf6Ti5%2F4YGHRD8jpKKZohatxP9pCyc1se4JwUTSv8pB0scciEGsV8RspIkxCV64IPxiyszaJ9ta%2Ftk1IB5gqcq58rVKqHzdfowdhShFaEvRb1YJD5dV%2BTvlW78%2FPR3puEjU5powTeMU%2BhAfU2nsQ3x5tMBaxYuqKlZbCNXghzxqFfSVj%2B9fc5CGX%2BHOzzB2OpRL%2BgG5exo0GSqJw0ZbAC9KjvoG9d8BHPTDdpPe8BjqkAcM0YI9V2ayHAaB09%2Fy3oiO6uzTxI5396EICcPZTJ%2FRWz1VBBUhiMtjqXL7FlMuMQr3T2bFjxp3F8Z4pFEypLyIwql07TviDIal38EQk7moP133XuzK0yvuBg0ehjyrr5GkMZBWpMuxaWvIogczNTF0UlNo6UIXPBbAILXi378rxjnlHtIoHIKrNOV6P0yI4FbIOBAWeNEXQY4Scd8GHRk8VVx3x&X-Amz-Signature=4dfe60ebfa3db3417d7b4b3bf38592aaa0ec465acdfe60cb70c2bc37d786aa4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YR6FT3P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDha1%2FeFbiIxZ5mZRrBGPhl8BMpiUmJNly8BnM5Zi%2BmtwIhAMgbXKzlMSdniH2%2FeJfrx7J6TpHzkVio%2FoBp5CQ0PFWyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxnGvNOBunzT8K0Ploq3AMZR2S9QDSXBSlvY9Xm8BCZ%2BAJvu%2Ba3Ht%2Bv8fRnga2Bs1KpZqPp9Y2pdvno8NkT1Y2n0kojr4zRa59B49C8KtbC0oNukU4JQ%2BL5OPmSpmXFpQU79w4np0DMKa0zHKXLODW0QpQ1vyRjYF5GVMs%2FiFKcKLq24p4s%2Bd1fT2h%2BYHTJVronvw6XcZn7%2BmFM6XFh2YzkU5pC5B%2BuI8lrAvx0SAcS3tzd36mTxhinTF7Z3BvVBl6hgcg7QHo9yYodTIIMTcExqZGUTQPnRkJsiPOhoxEuIu1jGhRoIcZnKx2F8Fki2m7y5Yr3wArXrnDAK7DU52ufbgNblMZuUpFh2z5BKZf8TukAG6xdkzNsisVzy4vGjpOMDpDUryGKTcW3w77hEpk%2B%2F181q3KRzEe8LJTtt1FfCnq2gf6Ti5%2F4YGHRD8jpKKZohatxP9pCyc1se4JwUTSv8pB0scciEGsV8RspIkxCV64IPxiyszaJ9ta%2Ftk1IB5gqcq58rVKqHzdfowdhShFaEvRb1YJD5dV%2BTvlW78%2FPR3puEjU5powTeMU%2BhAfU2nsQ3x5tMBaxYuqKlZbCNXghzxqFfSVj%2B9fc5CGX%2BHOzzB2OpRL%2BgG5exo0GSqJw0ZbAC9KjvoG9d8BHPTDdpPe8BjqkAcM0YI9V2ayHAaB09%2Fy3oiO6uzTxI5396EICcPZTJ%2FRWz1VBBUhiMtjqXL7FlMuMQr3T2bFjxp3F8Z4pFEypLyIwql07TviDIal38EQk7moP133XuzK0yvuBg0ehjyrr5GkMZBWpMuxaWvIogczNTF0UlNo6UIXPBbAILXi378rxjnlHtIoHIKrNOV6P0yI4FbIOBAWeNEXQY4Scd8GHRk8VVx3x&X-Amz-Signature=001c4c627308c91418f2fb5288240fb356e8afd444598e7d47c6ce63bf28e246&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6XQXT6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCds3c6jG0%2B%2FzQ%2FQUgvY%2FN%2FQlt%2BvQI1y74LVnD15sKmywIgRWij6kXK0XTpDNtB3vfPJNzSYk3HAZcLpQl1XbXFQFgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9GE%2FZfGNdmFhKvzircA9oFvkF%2F46R6QTL3xfQjf%2BHpshZEGXn8f7GQhCJO8BJsW%2F13fk%2FSEbWPBrNXdbnPSU%2Fa80AfmETVCPGPpQ8XBSrOdG8kUPtKE8HlNYO%2Bsx3PwJg6nzj4FanN%2F0I7VYnK%2FMVsEtg6QnM45CPonz73LgNZ1wYKByRSET%2BAUfGY5uX1GFOmTTjakmz0RQ3Ov428GWaI%2FZKZ0htngVdW41%2FXHIxCWrVDcVcGWSM488yd2869tS16uLVWktKzQRAlAIDdkv1TxGU59SeKBGqggpyVTa1WaseLWk8bX6VpXa74THJEau41zR7bcQ3CioSmDG5uBdpbwFXfBos%2BZ8wFWgBbV25AcHzkd19QG%2F30VW6FZEkGlltpLxOIs90uwPe3p7BcC8GULzQIHccy3L8FGZ6AaxICrTZN8yh6KSO30lqsA4%2FKb64dug7SWPdOVOt1tyx618RCbd34a8vV%2Bp8%2Bz30ddKjI5Dps9QTpMswjDtI4Pa51obxpSNYacS0V4TZYe0gcE9MrcR7jNsaPcmrP1A%2FgOwOWaj%2BdmmWcTpKQd8NN%2Blyt8JvKOwcSyg%2Br1b30SyDz2FgPBb2rt4pDNRLaiYv3j9U1wFXO0AwB83ZDXrZgf8JamFGtqWvUEbZCDqIqMKqk97wGOqUBq0afSx34EEQPGdKcEjgp1PZODPI08mzkPyMZxjrhB3dTb7NWHL3jbKk%2BEfgnGAWS1gX2O6svXiR3lUIuyiKRZiPhMHIy%2FJXQP5qkG%2BuIhyC%2BOkOPl4XUM8gAdHIQ87mn7PPmzFPBtwUOelZGqvjQLptfn90uWCeXgxP0a%2BtgDVCodjlqUzXVtMAaeKR8WbNey1w%2F4IUlNcF%2Fl5CukZcfrelqwhRI&X-Amz-Signature=247863e1abcccc32739f7e0050b11c2d1fa7b2aaa223608fd005003135aecbe5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6XQXT6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCds3c6jG0%2B%2FzQ%2FQUgvY%2FN%2FQlt%2BvQI1y74LVnD15sKmywIgRWij6kXK0XTpDNtB3vfPJNzSYk3HAZcLpQl1XbXFQFgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9GE%2FZfGNdmFhKvzircA9oFvkF%2F46R6QTL3xfQjf%2BHpshZEGXn8f7GQhCJO8BJsW%2F13fk%2FSEbWPBrNXdbnPSU%2Fa80AfmETVCPGPpQ8XBSrOdG8kUPtKE8HlNYO%2Bsx3PwJg6nzj4FanN%2F0I7VYnK%2FMVsEtg6QnM45CPonz73LgNZ1wYKByRSET%2BAUfGY5uX1GFOmTTjakmz0RQ3Ov428GWaI%2FZKZ0htngVdW41%2FXHIxCWrVDcVcGWSM488yd2869tS16uLVWktKzQRAlAIDdkv1TxGU59SeKBGqggpyVTa1WaseLWk8bX6VpXa74THJEau41zR7bcQ3CioSmDG5uBdpbwFXfBos%2BZ8wFWgBbV25AcHzkd19QG%2F30VW6FZEkGlltpLxOIs90uwPe3p7BcC8GULzQIHccy3L8FGZ6AaxICrTZN8yh6KSO30lqsA4%2FKb64dug7SWPdOVOt1tyx618RCbd34a8vV%2Bp8%2Bz30ddKjI5Dps9QTpMswjDtI4Pa51obxpSNYacS0V4TZYe0gcE9MrcR7jNsaPcmrP1A%2FgOwOWaj%2BdmmWcTpKQd8NN%2Blyt8JvKOwcSyg%2Br1b30SyDz2FgPBb2rt4pDNRLaiYv3j9U1wFXO0AwB83ZDXrZgf8JamFGtqWvUEbZCDqIqMKqk97wGOqUBq0afSx34EEQPGdKcEjgp1PZODPI08mzkPyMZxjrhB3dTb7NWHL3jbKk%2BEfgnGAWS1gX2O6svXiR3lUIuyiKRZiPhMHIy%2FJXQP5qkG%2BuIhyC%2BOkOPl4XUM8gAdHIQ87mn7PPmzFPBtwUOelZGqvjQLptfn90uWCeXgxP0a%2BtgDVCodjlqUzXVtMAaeKR8WbNey1w%2F4IUlNcF%2Fl5CukZcfrelqwhRI&X-Amz-Signature=c2ee7ea9924eeb6f8ee2656bef574c448e624ec06df9b04ef9475fabc0411d5e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6XQXT6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCds3c6jG0%2B%2FzQ%2FQUgvY%2FN%2FQlt%2BvQI1y74LVnD15sKmywIgRWij6kXK0XTpDNtB3vfPJNzSYk3HAZcLpQl1XbXFQFgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9GE%2FZfGNdmFhKvzircA9oFvkF%2F46R6QTL3xfQjf%2BHpshZEGXn8f7GQhCJO8BJsW%2F13fk%2FSEbWPBrNXdbnPSU%2Fa80AfmETVCPGPpQ8XBSrOdG8kUPtKE8HlNYO%2Bsx3PwJg6nzj4FanN%2F0I7VYnK%2FMVsEtg6QnM45CPonz73LgNZ1wYKByRSET%2BAUfGY5uX1GFOmTTjakmz0RQ3Ov428GWaI%2FZKZ0htngVdW41%2FXHIxCWrVDcVcGWSM488yd2869tS16uLVWktKzQRAlAIDdkv1TxGU59SeKBGqggpyVTa1WaseLWk8bX6VpXa74THJEau41zR7bcQ3CioSmDG5uBdpbwFXfBos%2BZ8wFWgBbV25AcHzkd19QG%2F30VW6FZEkGlltpLxOIs90uwPe3p7BcC8GULzQIHccy3L8FGZ6AaxICrTZN8yh6KSO30lqsA4%2FKb64dug7SWPdOVOt1tyx618RCbd34a8vV%2Bp8%2Bz30ddKjI5Dps9QTpMswjDtI4Pa51obxpSNYacS0V4TZYe0gcE9MrcR7jNsaPcmrP1A%2FgOwOWaj%2BdmmWcTpKQd8NN%2Blyt8JvKOwcSyg%2Br1b30SyDz2FgPBb2rt4pDNRLaiYv3j9U1wFXO0AwB83ZDXrZgf8JamFGtqWvUEbZCDqIqMKqk97wGOqUBq0afSx34EEQPGdKcEjgp1PZODPI08mzkPyMZxjrhB3dTb7NWHL3jbKk%2BEfgnGAWS1gX2O6svXiR3lUIuyiKRZiPhMHIy%2FJXQP5qkG%2BuIhyC%2BOkOPl4XUM8gAdHIQ87mn7PPmzFPBtwUOelZGqvjQLptfn90uWCeXgxP0a%2BtgDVCodjlqUzXVtMAaeKR8WbNey1w%2F4IUlNcF%2Fl5CukZcfrelqwhRI&X-Amz-Signature=e41f345efcbeacb450c495262780cfc790ff22346bedcad013ce82ba1c58a3f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6XQXT6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCds3c6jG0%2B%2FzQ%2FQUgvY%2FN%2FQlt%2BvQI1y74LVnD15sKmywIgRWij6kXK0XTpDNtB3vfPJNzSYk3HAZcLpQl1XbXFQFgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9GE%2FZfGNdmFhKvzircA9oFvkF%2F46R6QTL3xfQjf%2BHpshZEGXn8f7GQhCJO8BJsW%2F13fk%2FSEbWPBrNXdbnPSU%2Fa80AfmETVCPGPpQ8XBSrOdG8kUPtKE8HlNYO%2Bsx3PwJg6nzj4FanN%2F0I7VYnK%2FMVsEtg6QnM45CPonz73LgNZ1wYKByRSET%2BAUfGY5uX1GFOmTTjakmz0RQ3Ov428GWaI%2FZKZ0htngVdW41%2FXHIxCWrVDcVcGWSM488yd2869tS16uLVWktKzQRAlAIDdkv1TxGU59SeKBGqggpyVTa1WaseLWk8bX6VpXa74THJEau41zR7bcQ3CioSmDG5uBdpbwFXfBos%2BZ8wFWgBbV25AcHzkd19QG%2F30VW6FZEkGlltpLxOIs90uwPe3p7BcC8GULzQIHccy3L8FGZ6AaxICrTZN8yh6KSO30lqsA4%2FKb64dug7SWPdOVOt1tyx618RCbd34a8vV%2Bp8%2Bz30ddKjI5Dps9QTpMswjDtI4Pa51obxpSNYacS0V4TZYe0gcE9MrcR7jNsaPcmrP1A%2FgOwOWaj%2BdmmWcTpKQd8NN%2Blyt8JvKOwcSyg%2Br1b30SyDz2FgPBb2rt4pDNRLaiYv3j9U1wFXO0AwB83ZDXrZgf8JamFGtqWvUEbZCDqIqMKqk97wGOqUBq0afSx34EEQPGdKcEjgp1PZODPI08mzkPyMZxjrhB3dTb7NWHL3jbKk%2BEfgnGAWS1gX2O6svXiR3lUIuyiKRZiPhMHIy%2FJXQP5qkG%2BuIhyC%2BOkOPl4XUM8gAdHIQ87mn7PPmzFPBtwUOelZGqvjQLptfn90uWCeXgxP0a%2BtgDVCodjlqUzXVtMAaeKR8WbNey1w%2F4IUlNcF%2Fl5CukZcfrelqwhRI&X-Amz-Signature=9b2a5df105a1c2ab8a442f14b219b79221c8b91e46e4176d635f3df10a6f16fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6XQXT6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCds3c6jG0%2B%2FzQ%2FQUgvY%2FN%2FQlt%2BvQI1y74LVnD15sKmywIgRWij6kXK0XTpDNtB3vfPJNzSYk3HAZcLpQl1XbXFQFgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9GE%2FZfGNdmFhKvzircA9oFvkF%2F46R6QTL3xfQjf%2BHpshZEGXn8f7GQhCJO8BJsW%2F13fk%2FSEbWPBrNXdbnPSU%2Fa80AfmETVCPGPpQ8XBSrOdG8kUPtKE8HlNYO%2Bsx3PwJg6nzj4FanN%2F0I7VYnK%2FMVsEtg6QnM45CPonz73LgNZ1wYKByRSET%2BAUfGY5uX1GFOmTTjakmz0RQ3Ov428GWaI%2FZKZ0htngVdW41%2FXHIxCWrVDcVcGWSM488yd2869tS16uLVWktKzQRAlAIDdkv1TxGU59SeKBGqggpyVTa1WaseLWk8bX6VpXa74THJEau41zR7bcQ3CioSmDG5uBdpbwFXfBos%2BZ8wFWgBbV25AcHzkd19QG%2F30VW6FZEkGlltpLxOIs90uwPe3p7BcC8GULzQIHccy3L8FGZ6AaxICrTZN8yh6KSO30lqsA4%2FKb64dug7SWPdOVOt1tyx618RCbd34a8vV%2Bp8%2Bz30ddKjI5Dps9QTpMswjDtI4Pa51obxpSNYacS0V4TZYe0gcE9MrcR7jNsaPcmrP1A%2FgOwOWaj%2BdmmWcTpKQd8NN%2Blyt8JvKOwcSyg%2Br1b30SyDz2FgPBb2rt4pDNRLaiYv3j9U1wFXO0AwB83ZDXrZgf8JamFGtqWvUEbZCDqIqMKqk97wGOqUBq0afSx34EEQPGdKcEjgp1PZODPI08mzkPyMZxjrhB3dTb7NWHL3jbKk%2BEfgnGAWS1gX2O6svXiR3lUIuyiKRZiPhMHIy%2FJXQP5qkG%2BuIhyC%2BOkOPl4XUM8gAdHIQ87mn7PPmzFPBtwUOelZGqvjQLptfn90uWCeXgxP0a%2BtgDVCodjlqUzXVtMAaeKR8WbNey1w%2F4IUlNcF%2Fl5CukZcfrelqwhRI&X-Amz-Signature=d8d1db9cde7eec6074d70bb54cae8ab7b109154ba02c5100711d1c90f531dd63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6XQXT6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCds3c6jG0%2B%2FzQ%2FQUgvY%2FN%2FQlt%2BvQI1y74LVnD15sKmywIgRWij6kXK0XTpDNtB3vfPJNzSYk3HAZcLpQl1XbXFQFgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9GE%2FZfGNdmFhKvzircA9oFvkF%2F46R6QTL3xfQjf%2BHpshZEGXn8f7GQhCJO8BJsW%2F13fk%2FSEbWPBrNXdbnPSU%2Fa80AfmETVCPGPpQ8XBSrOdG8kUPtKE8HlNYO%2Bsx3PwJg6nzj4FanN%2F0I7VYnK%2FMVsEtg6QnM45CPonz73LgNZ1wYKByRSET%2BAUfGY5uX1GFOmTTjakmz0RQ3Ov428GWaI%2FZKZ0htngVdW41%2FXHIxCWrVDcVcGWSM488yd2869tS16uLVWktKzQRAlAIDdkv1TxGU59SeKBGqggpyVTa1WaseLWk8bX6VpXa74THJEau41zR7bcQ3CioSmDG5uBdpbwFXfBos%2BZ8wFWgBbV25AcHzkd19QG%2F30VW6FZEkGlltpLxOIs90uwPe3p7BcC8GULzQIHccy3L8FGZ6AaxICrTZN8yh6KSO30lqsA4%2FKb64dug7SWPdOVOt1tyx618RCbd34a8vV%2Bp8%2Bz30ddKjI5Dps9QTpMswjDtI4Pa51obxpSNYacS0V4TZYe0gcE9MrcR7jNsaPcmrP1A%2FgOwOWaj%2BdmmWcTpKQd8NN%2Blyt8JvKOwcSyg%2Br1b30SyDz2FgPBb2rt4pDNRLaiYv3j9U1wFXO0AwB83ZDXrZgf8JamFGtqWvUEbZCDqIqMKqk97wGOqUBq0afSx34EEQPGdKcEjgp1PZODPI08mzkPyMZxjrhB3dTb7NWHL3jbKk%2BEfgnGAWS1gX2O6svXiR3lUIuyiKRZiPhMHIy%2FJXQP5qkG%2BuIhyC%2BOkOPl4XUM8gAdHIQ87mn7PPmzFPBtwUOelZGqvjQLptfn90uWCeXgxP0a%2BtgDVCodjlqUzXVtMAaeKR8WbNey1w%2F4IUlNcF%2Fl5CukZcfrelqwhRI&X-Amz-Signature=a7221430e8fac5c3d4d69121a317d590ee1f6b17f504c2da6629c6e5b3e12bcf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664J5P5RMS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAk2OMBP3K3nwONE4XhQ9ILXAt9njN%2BiYiejsipf44WsAiAouRX%2BYsCm814LxI8NVysUenKIvuixn2fiT87Qi3miJSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuMz8mBmLb9BIJTqPKtwDEHUBFN6NiSQwFXGAcEaasTxn1AS3MU26K2fO0lpFbtws1nuGeM%2B%2B6K8jLkmPmfdRFbpo0%2B5cB2xUWETis6LlblLNdvRRzx6JrEx7xBTDPGxuuchFZXVcr0dZStM7kFx5xU6GufVxGylmHP0RYcr%2BFt65gcarpXg0cit9IdM7pUIdC1e3RLnZ2Ysma%2Byjy5rHOxscdzAgteW7H3i%2Fh8S7QSAkZtqj9%2F8T0ui6XAJez%2BZ4Fh61YSHyipoGQ6qmd5EvAIC6yONhLa79st2%2FWHY4oFhsJpYvbN%2BQ%2FBKCK18AuJ1Ta1WC1OmTdsa8rlMiUg%2FqzDkYaJw6qJ6AVTRSeOEw2Ho8VAkFapM3lP1%2Bvl4i8c4ShUrv%2F%2BJO3MgJlV22zwdNlsG8dUTdwLB2nSf6%2BnJv%2BJwGz%2FKeh8do7Hyic%2Fy0g9ZirPdfAXxR28o7zIxfK1dk7Z6qdM2U83mO4od95pKinwV9%2BW9EPM2HV6d%2BJubqNtx2J2dfFVnBpB5HFPlbax1Y3wCxQ3zbCNoWhY53DrQiRIyRNVNBF%2FVdoQfWcPvzdxNR6V9%2BaU9nk3LIMcyEYdi%2F0b3TwKct4IS5ls67Mvyg%2FZrMCUlA%2Bcs9jONaQWPgSQCUbNa9QjfMsJye1f0wqaT3vAY6pgEZWIlv%2Fptjy2tz9e46SArNBu2L2enlYMwWb31dKT3%2FS1QURwbPr9IzAbggyoKvweFuGPKFesqheMW22NQDyP%2FJ4QZDCEEwNgqeVrLYiZjlcBC1j%2BibKcm0lVkgWgFz53dRNlEh75a7MKiNZ5%2Bm%2FqQewjmwOi1251CJyCRXxSXU2SQq8zeOunNAXTveN2ukfHLb%2Bvx6z1W%2Fthhrz9uwhYULtxpzGJkI&X-Amz-Signature=f15b191ef1386884b37c1db41aaa16f623a998b005c4804ef8b115222336ca3a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSDHBF4A%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNo5B7pzn08noOBqUXEPtcck0eToMC4Sdrb9mf0wFZqgIhANub2NtT0FxMmfRzywkfQ6vBNDF6b%2FofgOgLqiAhQZjMKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igybq3o67rXaBVMeWyQq3ANawJnd8xPVMzziNiZMXSfUngfcjJROEwyAH4XhyjUOJoIX8n1Cb4lM0DyCfczJ%2BNr7vV%2FK2lMbbpsl5fyrEkFFKuK%2FUcJxN10gbqvHuYVc0wznq5ItyBPX3MMduYrcgp47wvVlkmZlSn%2FuemLIkYk15SzJnY19vMOG352KczGQD2X6PJMp11Seqhcdo1khysbE9hUBeLyJETRMAT8E4ytGKX%2Bl%2FFd%2FfKYbXSHH526wMo7xAQWsO3jjm4e1XQiQW5QmVdHhlUko70GJ77DiIjQJdF9taE%2B8s4fj8eBRGPGjAyMSg%2B%2FrHAwGjHbcegE4cB8yX4JFPzvCVTn0VDOr1QwHF9nLO65tIy%2FvaF5qcPw2VYsroyprs2%2Bo9v5t4l3rFtq6vqAPpii%2BmdJI3daecACRtCXkM8CL%2FIzeSJQvGCTddfsZuQKcS8%2FgKGICx9IsjFmvBM9Mnn6K66y7c1oDAK2Ds5GSPJW8kYdjU50%2FVQgnUo4VxO2762AkXoOjeL3X%2FUm5JKt6qnmcPl%2FnXZzSNXRVjYcouyILXo44FODzHvD3Ri8qc4plDe5mV3uJMRlBLW80n0lAMAgzbOotSEDkF2UI39qVSqFbTJ%2F3u74HhEzLDL8HzqDg8vcMcsg95TDXpPe8BjqkAZlTho9B5zALw0tTnqjb1Neo0XEQo9tbsrrbOMlElQRNpsYqOWN%2BQIrTQlSJle0nO4XI9yMYIBlEpVzVxwIYWF3rZ7kbdb37zh%2FdbWIYTzbAw3JrNB%2FWYh%2FQ%2Fqn%2BeIwnVbWumAAvTfRM5opwg950a6uOStaDy1Qfi74TkurSAnB0oey%2B143tXh098X6yeoFBJNfu8LgHP0V7Fuy6g19hddDeYf28&X-Amz-Signature=f0379959c4c300f2acb03cc001d9e028412ba2cdd4a4f365ceb1d486062af05d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6XQXT6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCds3c6jG0%2B%2FzQ%2FQUgvY%2FN%2FQlt%2BvQI1y74LVnD15sKmywIgRWij6kXK0XTpDNtB3vfPJNzSYk3HAZcLpQl1XbXFQFgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9GE%2FZfGNdmFhKvzircA9oFvkF%2F46R6QTL3xfQjf%2BHpshZEGXn8f7GQhCJO8BJsW%2F13fk%2FSEbWPBrNXdbnPSU%2Fa80AfmETVCPGPpQ8XBSrOdG8kUPtKE8HlNYO%2Bsx3PwJg6nzj4FanN%2F0I7VYnK%2FMVsEtg6QnM45CPonz73LgNZ1wYKByRSET%2BAUfGY5uX1GFOmTTjakmz0RQ3Ov428GWaI%2FZKZ0htngVdW41%2FXHIxCWrVDcVcGWSM488yd2869tS16uLVWktKzQRAlAIDdkv1TxGU59SeKBGqggpyVTa1WaseLWk8bX6VpXa74THJEau41zR7bcQ3CioSmDG5uBdpbwFXfBos%2BZ8wFWgBbV25AcHzkd19QG%2F30VW6FZEkGlltpLxOIs90uwPe3p7BcC8GULzQIHccy3L8FGZ6AaxICrTZN8yh6KSO30lqsA4%2FKb64dug7SWPdOVOt1tyx618RCbd34a8vV%2Bp8%2Bz30ddKjI5Dps9QTpMswjDtI4Pa51obxpSNYacS0V4TZYe0gcE9MrcR7jNsaPcmrP1A%2FgOwOWaj%2BdmmWcTpKQd8NN%2Blyt8JvKOwcSyg%2Br1b30SyDz2FgPBb2rt4pDNRLaiYv3j9U1wFXO0AwB83ZDXrZgf8JamFGtqWvUEbZCDqIqMKqk97wGOqUBq0afSx34EEQPGdKcEjgp1PZODPI08mzkPyMZxjrhB3dTb7NWHL3jbKk%2BEfgnGAWS1gX2O6svXiR3lUIuyiKRZiPhMHIy%2FJXQP5qkG%2BuIhyC%2BOkOPl4XUM8gAdHIQ87mn7PPmzFPBtwUOelZGqvjQLptfn90uWCeXgxP0a%2BtgDVCodjlqUzXVtMAaeKR8WbNey1w%2F4IUlNcF%2Fl5CukZcfrelqwhRI&X-Amz-Signature=8aa61fe3b8ca20173b23198a20ad814f97292e30ca6db1c1f9015a3baaffb302&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6XQXT6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCds3c6jG0%2B%2FzQ%2FQUgvY%2FN%2FQlt%2BvQI1y74LVnD15sKmywIgRWij6kXK0XTpDNtB3vfPJNzSYk3HAZcLpQl1XbXFQFgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9GE%2FZfGNdmFhKvzircA9oFvkF%2F46R6QTL3xfQjf%2BHpshZEGXn8f7GQhCJO8BJsW%2F13fk%2FSEbWPBrNXdbnPSU%2Fa80AfmETVCPGPpQ8XBSrOdG8kUPtKE8HlNYO%2Bsx3PwJg6nzj4FanN%2F0I7VYnK%2FMVsEtg6QnM45CPonz73LgNZ1wYKByRSET%2BAUfGY5uX1GFOmTTjakmz0RQ3Ov428GWaI%2FZKZ0htngVdW41%2FXHIxCWrVDcVcGWSM488yd2869tS16uLVWktKzQRAlAIDdkv1TxGU59SeKBGqggpyVTa1WaseLWk8bX6VpXa74THJEau41zR7bcQ3CioSmDG5uBdpbwFXfBos%2BZ8wFWgBbV25AcHzkd19QG%2F30VW6FZEkGlltpLxOIs90uwPe3p7BcC8GULzQIHccy3L8FGZ6AaxICrTZN8yh6KSO30lqsA4%2FKb64dug7SWPdOVOt1tyx618RCbd34a8vV%2Bp8%2Bz30ddKjI5Dps9QTpMswjDtI4Pa51obxpSNYacS0V4TZYe0gcE9MrcR7jNsaPcmrP1A%2FgOwOWaj%2BdmmWcTpKQd8NN%2Blyt8JvKOwcSyg%2Br1b30SyDz2FgPBb2rt4pDNRLaiYv3j9U1wFXO0AwB83ZDXrZgf8JamFGtqWvUEbZCDqIqMKqk97wGOqUBq0afSx34EEQPGdKcEjgp1PZODPI08mzkPyMZxjrhB3dTb7NWHL3jbKk%2BEfgnGAWS1gX2O6svXiR3lUIuyiKRZiPhMHIy%2FJXQP5qkG%2BuIhyC%2BOkOPl4XUM8gAdHIQ87mn7PPmzFPBtwUOelZGqvjQLptfn90uWCeXgxP0a%2BtgDVCodjlqUzXVtMAaeKR8WbNey1w%2F4IUlNcF%2Fl5CukZcfrelqwhRI&X-Amz-Signature=d3504b6abc4ff0cecc94c89d554463ea19268994f107b09865f2950a3c7f4281&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6XQXT6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCds3c6jG0%2B%2FzQ%2FQUgvY%2FN%2FQlt%2BvQI1y74LVnD15sKmywIgRWij6kXK0XTpDNtB3vfPJNzSYk3HAZcLpQl1XbXFQFgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9GE%2FZfGNdmFhKvzircA9oFvkF%2F46R6QTL3xfQjf%2BHpshZEGXn8f7GQhCJO8BJsW%2F13fk%2FSEbWPBrNXdbnPSU%2Fa80AfmETVCPGPpQ8XBSrOdG8kUPtKE8HlNYO%2Bsx3PwJg6nzj4FanN%2F0I7VYnK%2FMVsEtg6QnM45CPonz73LgNZ1wYKByRSET%2BAUfGY5uX1GFOmTTjakmz0RQ3Ov428GWaI%2FZKZ0htngVdW41%2FXHIxCWrVDcVcGWSM488yd2869tS16uLVWktKzQRAlAIDdkv1TxGU59SeKBGqggpyVTa1WaseLWk8bX6VpXa74THJEau41zR7bcQ3CioSmDG5uBdpbwFXfBos%2BZ8wFWgBbV25AcHzkd19QG%2F30VW6FZEkGlltpLxOIs90uwPe3p7BcC8GULzQIHccy3L8FGZ6AaxICrTZN8yh6KSO30lqsA4%2FKb64dug7SWPdOVOt1tyx618RCbd34a8vV%2Bp8%2Bz30ddKjI5Dps9QTpMswjDtI4Pa51obxpSNYacS0V4TZYe0gcE9MrcR7jNsaPcmrP1A%2FgOwOWaj%2BdmmWcTpKQd8NN%2Blyt8JvKOwcSyg%2Br1b30SyDz2FgPBb2rt4pDNRLaiYv3j9U1wFXO0AwB83ZDXrZgf8JamFGtqWvUEbZCDqIqMKqk97wGOqUBq0afSx34EEQPGdKcEjgp1PZODPI08mzkPyMZxjrhB3dTb7NWHL3jbKk%2BEfgnGAWS1gX2O6svXiR3lUIuyiKRZiPhMHIy%2FJXQP5qkG%2BuIhyC%2BOkOPl4XUM8gAdHIQ87mn7PPmzFPBtwUOelZGqvjQLptfn90uWCeXgxP0a%2BtgDVCodjlqUzXVtMAaeKR8WbNey1w%2F4IUlNcF%2Fl5CukZcfrelqwhRI&X-Amz-Signature=54c688a7c002fdaa34a355d251e023562f55fc76399d160dfb08175e20c4f26a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6ILVKGV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICOjIViJn%2F%2F8EvwfZvmS%2FDYn8sRlp4waQ8%2BSA9xGJktDAiEAh22UTekv%2FraGh0%2F4JxirEKumkFxymS0se15WucDxvi0qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB7vQwGiV69xM1YucCrcAypf0dSKsknbfRCwSy63xLIohOXgzoZ81nLkroDd1m8rE9oXI%2BsGQhJDlzxfdnpa3vSDbpVyAaSSQkw5TIP8gN73d0WeiSlqwA2J7ms%2B4VxL5Ur%2BipGAMhEHJMpqMtkWprxjYvolfVvoCHEL4EkaK%2B5qbuDBXruklXTFFHdoM380xIYgUAmbOsMNgC1d%2BXIG42%2FTTz0znbNSZIe4jqxxlz4mdX4QeKOnK%2BGetDEJdY439QbViPjm%2FI4RVxbfQJeBkEBnscrW8DStXPOxAC0USEKgS8uSjG8Go8FuFOQPrk7rk5NO5Dcwk7qi6It%2FOCctClWLFjl%2BEhDe10nkjbWYgD9rocAO%2BebzUdiF6ieM1aU3Cl8P4BjBqlD9Aya479a3Fd0ZUI8vt%2FNvmcpfUtu4fsqG6Bv1otO7BEcsRRecKDMTavj6KoOMhw8gkwzweZ1hgyYIPzryvYCpig5ojCHMIWGuIdISfKRcO2QHA%2F%2B7ciDf3Xy5mkmun7SD2whyiP7xN3TNnl18gJt9CcuQseZmgoGG8YwmWnExNJaloa6xbtkiQB%2B0t3KZMawi2pIuV8ZBoECHXHWZV1MB8N465KIMz8Ux8vFfxUYqPHAlinhIa0FoXg0NZw0hIFIEpcMnMJul97wGOqUB0cFOXxLp5p9FViyVP48ccokzqHvPlnDGRU1CAI8DwpzydHYJ3x0eutBoTo2ioF0t2ePDIbN8Ztn352qk1NJwwbYtDHDh%2FfPwN%2FGO6wBSwJjIc3U3UKAykDCgaaFZKhmMC1qy36cL7jSFSWVjcJ7ZBXBKJk%2B8uNNurTIwQhn9MLLJ6Uqspq4qQJVOhJHC2qYedAO7G1evqp8f1WpgPd9mpXooAbI%2F&X-Amz-Signature=0c5a0120f264cda2369085462244a3ef365854ae648e04c07edf66153acbaaac&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB7F33LF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGmbXgssZRLe3TSBItRjlFqL1Uu3tcSe5pIP4ppxA1AVAiBsolGH2N5gC6xVkpdEfe%2Fav5EGN%2Fnpk46arGw81RRScCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMojunEQ6c4WMcCcY4KtwDQohtP%2Fj8XitDgXzBm3f8dY9At2II3b93ee7B5iTa3nxlOoAMTF85%2BOBK%2FwxSwjTkqHxG5fkAcR00lus%2BthL%2FcwEfRJrv63ciPZvRjOn%2BW06ZdAufVmZFY1RcekQ3kno1A7agvvC7U1uStHFKWREmiM0bn16%2B3pdPjCwHB%2By59B%2BQUph5opm7UiLz5NyboBRKfQmR8ejSDiJUBHDKorliuFToccPdKFPXLpTrGTFbNQMwjEF5qKjCrhd1ROpfYzu3Uj2uR0aQRp6Wn7mZzGba63DrslukDGeZuyxnHHosYD87HfMe0B9Jn9tPC6IEGAB2qjs542B4kiDYDRvvBpd8K9mHnGHQzAJd3TDcW7SMUL9YgdblrmlhmjmmCa6EYAw1ikftzYb%2FiZM0%2BXO94TaCWt2gSBpB89NJFFd1bN8M88J6eBiqpsBKH%2F0gAVOyXRno7CphPq6cWQBpWEc6frW78bQNAIFh%2FI4PCHGoUiXV4V%2BuKVRTJeZ5%2F4jfN4Y4%2BvJF4Tcr8OcVlOcxeJDvCgBrQ8eZ54%2FwKd2O3%2FadC1%2FrOWL9GyzndCDEJ5q%2B8eWCYkEXaHqAI77rFhGa1EzVxtFwqcVs1kPWz3Zcp0jysfR41j%2BXUV45zucsdPih%2BUswyqT3vAY6pgEYE%2BT80p08NdyYg6E4pjxuyWsA58BK7Msbj9TId95BvtKkNlrN8byaQyfUIPVTm0PU%2B8IDJyGXFsDTs3O6i%2FmtQes4eSpBBo5tuDa%2F%2BwTqZ9gQU78sfYeDF%2BCW6bf8oZiguBBkbbTB7lFUlRKIiS3C%2B%2BZu%2Fp9fG6%2BAkAs9e7ijuD1hPDdFezadbIgsiU0dn1v1UJUJR%2BqfpAc9VEobfchQVv4MxgOC&X-Amz-Signature=dee133bf86ca0aeb43347398f335a6e16aecef3b1f61edfed5ae2b762711afb0&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6XQXT6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCds3c6jG0%2B%2FzQ%2FQUgvY%2FN%2FQlt%2BvQI1y74LVnD15sKmywIgRWij6kXK0XTpDNtB3vfPJNzSYk3HAZcLpQl1XbXFQFgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9GE%2FZfGNdmFhKvzircA9oFvkF%2F46R6QTL3xfQjf%2BHpshZEGXn8f7GQhCJO8BJsW%2F13fk%2FSEbWPBrNXdbnPSU%2Fa80AfmETVCPGPpQ8XBSrOdG8kUPtKE8HlNYO%2Bsx3PwJg6nzj4FanN%2F0I7VYnK%2FMVsEtg6QnM45CPonz73LgNZ1wYKByRSET%2BAUfGY5uX1GFOmTTjakmz0RQ3Ov428GWaI%2FZKZ0htngVdW41%2FXHIxCWrVDcVcGWSM488yd2869tS16uLVWktKzQRAlAIDdkv1TxGU59SeKBGqggpyVTa1WaseLWk8bX6VpXa74THJEau41zR7bcQ3CioSmDG5uBdpbwFXfBos%2BZ8wFWgBbV25AcHzkd19QG%2F30VW6FZEkGlltpLxOIs90uwPe3p7BcC8GULzQIHccy3L8FGZ6AaxICrTZN8yh6KSO30lqsA4%2FKb64dug7SWPdOVOt1tyx618RCbd34a8vV%2Bp8%2Bz30ddKjI5Dps9QTpMswjDtI4Pa51obxpSNYacS0V4TZYe0gcE9MrcR7jNsaPcmrP1A%2FgOwOWaj%2BdmmWcTpKQd8NN%2Blyt8JvKOwcSyg%2Br1b30SyDz2FgPBb2rt4pDNRLaiYv3j9U1wFXO0AwB83ZDXrZgf8JamFGtqWvUEbZCDqIqMKqk97wGOqUBq0afSx34EEQPGdKcEjgp1PZODPI08mzkPyMZxjrhB3dTb7NWHL3jbKk%2BEfgnGAWS1gX2O6svXiR3lUIuyiKRZiPhMHIy%2FJXQP5qkG%2BuIhyC%2BOkOPl4XUM8gAdHIQ87mn7PPmzFPBtwUOelZGqvjQLptfn90uWCeXgxP0a%2BtgDVCodjlqUzXVtMAaeKR8WbNey1w%2F4IUlNcF%2Fl5CukZcfrelqwhRI&X-Amz-Signature=5a93621a67a291d78612fbb1e0dae58ae7c558171c1359bf4acd9121986b72dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WJK4KTD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH0xNKuRXDVj7nns%2BVI0NENhntVJABYYZLRiJ%2FKhLa8zAiEA4YhWUyS0MC6TRsS351mwGZiFhNE5yZeNibQ%2Bao3eqUIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGVZEtAoEQzVXT9%2BBCrcA6l8gzLHXmYrqP5xiYewARdVsA4CewW9Lgr1ddNkAt3v94UsOlBwVRshy4RntTOjAtGzdCvCbG1%2FpKuWsEuBfackTSXKlVdp7%2FYvBb1t3nduEqlFnog2XC9W8Y5pBPF%2B9PkU1L15wXTufRJPsu%2FUvVz06KuHSocSKjXgcuaG%2FVXOWMVzQFJEsuM4XVZrlulfbl48C4aCb1VHF9jXA2IoD0V6kujcnCWxD2aNkxmlizt3tilu3Jyc1slYhoP5SyrCOUxdLyHIz7ko6oJvnab67MG36dUk3m1JRZV6VofNF3o4KMiXlXhg8oHBiq%2B2RPqjy%2F7c%2FBoZqA6sXWvg9pm74teqvTa4QHjMLgvEqs0SN0LUF0NplzusqHWoDT3X7S9oa9h56iIgToKlpmJ3JqWCCc96%2B570bzUl3W0RMoPSeNqMXBsox1VEoDei2fUTuYEgWqhXi5YmExUzPBeowYkAoDb0zSzGC%2B1sUUSPsYoBMe4t7ZvMr7IsTZR6yphM8sqWPqaxrVr64gwsjwNEkdwY0JbUSqBKTswljvUmV7XyOBPJqFEcq9hHtir6UhwzIRXOevoPu7fFWezIabwLmgoC0HadEMsORKrhD%2FGV66YOI01itVXjIoQYpgivGek0MJik97wGOqUBmyKVxuPhL0g8%2FPrXX%2F83qnoRr0RWBDQyd5yGq7hbI7jgNK6wdsryyI9t0txoMeWORG%2FyMMG5fUsMJXAUixbeta13UdysWjEZ3elvhfYPPdCqxMUBnhCzpTdUQso2dEULEQZ80grN7fnXM%2BiblRJq%2FoPRkLIlcnwEMaLtTwj9xpMKCev3GGGh1qweUEolx1Q7bbxgiBPODEIZO5Xe6tYAljP2RhlP&X-Amz-Signature=f89dad7e2691d9b4211f99f599b0c1cba3a94f141bd25182adc0b4346aa777d9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WJK4KTD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH0xNKuRXDVj7nns%2BVI0NENhntVJABYYZLRiJ%2FKhLa8zAiEA4YhWUyS0MC6TRsS351mwGZiFhNE5yZeNibQ%2Bao3eqUIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGVZEtAoEQzVXT9%2BBCrcA6l8gzLHXmYrqP5xiYewARdVsA4CewW9Lgr1ddNkAt3v94UsOlBwVRshy4RntTOjAtGzdCvCbG1%2FpKuWsEuBfackTSXKlVdp7%2FYvBb1t3nduEqlFnog2XC9W8Y5pBPF%2B9PkU1L15wXTufRJPsu%2FUvVz06KuHSocSKjXgcuaG%2FVXOWMVzQFJEsuM4XVZrlulfbl48C4aCb1VHF9jXA2IoD0V6kujcnCWxD2aNkxmlizt3tilu3Jyc1slYhoP5SyrCOUxdLyHIz7ko6oJvnab67MG36dUk3m1JRZV6VofNF3o4KMiXlXhg8oHBiq%2B2RPqjy%2F7c%2FBoZqA6sXWvg9pm74teqvTa4QHjMLgvEqs0SN0LUF0NplzusqHWoDT3X7S9oa9h56iIgToKlpmJ3JqWCCc96%2B570bzUl3W0RMoPSeNqMXBsox1VEoDei2fUTuYEgWqhXi5YmExUzPBeowYkAoDb0zSzGC%2B1sUUSPsYoBMe4t7ZvMr7IsTZR6yphM8sqWPqaxrVr64gwsjwNEkdwY0JbUSqBKTswljvUmV7XyOBPJqFEcq9hHtir6UhwzIRXOevoPu7fFWezIabwLmgoC0HadEMsORKrhD%2FGV66YOI01itVXjIoQYpgivGek0MJik97wGOqUBmyKVxuPhL0g8%2FPrXX%2F83qnoRr0RWBDQyd5yGq7hbI7jgNK6wdsryyI9t0txoMeWORG%2FyMMG5fUsMJXAUixbeta13UdysWjEZ3elvhfYPPdCqxMUBnhCzpTdUQso2dEULEQZ80grN7fnXM%2BiblRJq%2FoPRkLIlcnwEMaLtTwj9xpMKCev3GGGh1qweUEolx1Q7bbxgiBPODEIZO5Xe6tYAljP2RhlP&X-Amz-Signature=1adcf86dfba4d08073a1a4bfd65efc4aaa8798461d3c92caad994396dae26915&X-Amz-SignedHeaders=host&x-id=GetObject)

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
