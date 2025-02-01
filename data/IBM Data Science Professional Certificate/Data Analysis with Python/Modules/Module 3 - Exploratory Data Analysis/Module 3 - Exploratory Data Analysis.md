

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYOVDIB6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGUViEFYF2awT7yNXJtCZkqbs6uIcFgXs%2B43PzviJCbwIgEjiqlV%2FwC8fs5kw1rKELdqakJq1MJefTWe0Hz79ESUoqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDyvZm3icu3%2B0GbXKircA0cUDSZuOfOL520O9DFRLYdhsFFFrl2su0bCfgJAA6fEkcrTbCAPbTHnzsUyb0LUoQ%2BkFdzcmed17Szi962MBeWIIcoVDeGvtyf76NCV2S1nvoIX62e5uLf9Pg3E9QtA58XomuF0vxC%2Bz49V0097Koqzb%2FhX%2FfOGjyhZb9rDSWlby7DZmPX6jwGrcSrTzfSqgljP9V%2BJFB%2FNGXqsOMajDs3I%2F%2Bz6ooKHiZs%2BleLzIzgZ3hydtjyTTPWg9C4Bw3i6%2BuN888Ae5JjcToN%2BfucB0M59JWmmihAlsqJgK%2F%2FmskOdJoZQ0oeigatlsfo0Tcd0cNf0AvctAQlDgUP3gxd8PQwStSgBg8ZwWqGtz5W4g9QUg%2BrozagTxG69no7qpi6%2BZjopXOdNvaApBBOvqqtVb%2B2aKZXw2dUdjQG3KgWPFB7DaE1rvoC%2B2GyTFqGSamVo2kh0Se6BwVRcrFmxLBlYbysivF0nq3rfiKGHGg0Fevc3saQMiNXn%2B1d%2FjXyqApI%2BWYXlKyqPNaBci22JoakdbaI1R7DYRmHGMKJRhPCQ0iOCr1LTruwraTtNLvIz6xNhcZ5z3Ingb%2BP98T29QvnTuJ38EwZku%2FiRdUEJNO4xrNiDH9QM5vDOifbODqmxMO2w%2BrwGOqUB7CV8XNznS8Rrstv%2BKNtzWYExUhMYDTcDc7T23dIIObrYO6qDFzob8oUewF20kxV5wKH1nhTokcNcDtvxWidAak8SmFOHfGMm94YO5muFJA%2FyjzB1sr6Q3nbMmTjh6CXrZv0DpTf3MfJ70ias%2Fiz1fcGgSlC%2BZOsFyhGfQyt0FdjhnKJZaIU1BbMoDvAYKEjpaEc5PLmGdAGe%2BSToUbG3o%2FyokYSv&X-Amz-Signature=558750e95d92a15c849a41084774d76bcdbd64298cbccef3d5543c9f270df0cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYOVDIB6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGUViEFYF2awT7yNXJtCZkqbs6uIcFgXs%2B43PzviJCbwIgEjiqlV%2FwC8fs5kw1rKELdqakJq1MJefTWe0Hz79ESUoqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDyvZm3icu3%2B0GbXKircA0cUDSZuOfOL520O9DFRLYdhsFFFrl2su0bCfgJAA6fEkcrTbCAPbTHnzsUyb0LUoQ%2BkFdzcmed17Szi962MBeWIIcoVDeGvtyf76NCV2S1nvoIX62e5uLf9Pg3E9QtA58XomuF0vxC%2Bz49V0097Koqzb%2FhX%2FfOGjyhZb9rDSWlby7DZmPX6jwGrcSrTzfSqgljP9V%2BJFB%2FNGXqsOMajDs3I%2F%2Bz6ooKHiZs%2BleLzIzgZ3hydtjyTTPWg9C4Bw3i6%2BuN888Ae5JjcToN%2BfucB0M59JWmmihAlsqJgK%2F%2FmskOdJoZQ0oeigatlsfo0Tcd0cNf0AvctAQlDgUP3gxd8PQwStSgBg8ZwWqGtz5W4g9QUg%2BrozagTxG69no7qpi6%2BZjopXOdNvaApBBOvqqtVb%2B2aKZXw2dUdjQG3KgWPFB7DaE1rvoC%2B2GyTFqGSamVo2kh0Se6BwVRcrFmxLBlYbysivF0nq3rfiKGHGg0Fevc3saQMiNXn%2B1d%2FjXyqApI%2BWYXlKyqPNaBci22JoakdbaI1R7DYRmHGMKJRhPCQ0iOCr1LTruwraTtNLvIz6xNhcZ5z3Ingb%2BP98T29QvnTuJ38EwZku%2FiRdUEJNO4xrNiDH9QM5vDOifbODqmxMO2w%2BrwGOqUB7CV8XNznS8Rrstv%2BKNtzWYExUhMYDTcDc7T23dIIObrYO6qDFzob8oUewF20kxV5wKH1nhTokcNcDtvxWidAak8SmFOHfGMm94YO5muFJA%2FyjzB1sr6Q3nbMmTjh6CXrZv0DpTf3MfJ70ias%2Fiz1fcGgSlC%2BZOsFyhGfQyt0FdjhnKJZaIU1BbMoDvAYKEjpaEc5PLmGdAGe%2BSToUbG3o%2FyokYSv&X-Amz-Signature=7ba29f83733c76fcedf35fa8884e08a6838ff4b04a24740b8ab9ef3d8cfb4c8e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYOVDIB6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGUViEFYF2awT7yNXJtCZkqbs6uIcFgXs%2B43PzviJCbwIgEjiqlV%2FwC8fs5kw1rKELdqakJq1MJefTWe0Hz79ESUoqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDyvZm3icu3%2B0GbXKircA0cUDSZuOfOL520O9DFRLYdhsFFFrl2su0bCfgJAA6fEkcrTbCAPbTHnzsUyb0LUoQ%2BkFdzcmed17Szi962MBeWIIcoVDeGvtyf76NCV2S1nvoIX62e5uLf9Pg3E9QtA58XomuF0vxC%2Bz49V0097Koqzb%2FhX%2FfOGjyhZb9rDSWlby7DZmPX6jwGrcSrTzfSqgljP9V%2BJFB%2FNGXqsOMajDs3I%2F%2Bz6ooKHiZs%2BleLzIzgZ3hydtjyTTPWg9C4Bw3i6%2BuN888Ae5JjcToN%2BfucB0M59JWmmihAlsqJgK%2F%2FmskOdJoZQ0oeigatlsfo0Tcd0cNf0AvctAQlDgUP3gxd8PQwStSgBg8ZwWqGtz5W4g9QUg%2BrozagTxG69no7qpi6%2BZjopXOdNvaApBBOvqqtVb%2B2aKZXw2dUdjQG3KgWPFB7DaE1rvoC%2B2GyTFqGSamVo2kh0Se6BwVRcrFmxLBlYbysivF0nq3rfiKGHGg0Fevc3saQMiNXn%2B1d%2FjXyqApI%2BWYXlKyqPNaBci22JoakdbaI1R7DYRmHGMKJRhPCQ0iOCr1LTruwraTtNLvIz6xNhcZ5z3Ingb%2BP98T29QvnTuJ38EwZku%2FiRdUEJNO4xrNiDH9QM5vDOifbODqmxMO2w%2BrwGOqUB7CV8XNznS8Rrstv%2BKNtzWYExUhMYDTcDc7T23dIIObrYO6qDFzob8oUewF20kxV5wKH1nhTokcNcDtvxWidAak8SmFOHfGMm94YO5muFJA%2FyjzB1sr6Q3nbMmTjh6CXrZv0DpTf3MfJ70ias%2Fiz1fcGgSlC%2BZOsFyhGfQyt0FdjhnKJZaIU1BbMoDvAYKEjpaEc5PLmGdAGe%2BSToUbG3o%2FyokYSv&X-Amz-Signature=074fb6662c1af8821974f9f1bb67693340bf42bfb12db98765413404a47042e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKBY6CWH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F9oeVjkBVb7bHdOYYo%2B4fCvhzz0wdkJHWa%2FGLXY0ZOwIga4eBFQYnD70OfwPlGcyT2Fddp4ENRZhyGDh8n%2Fu%2Fc7oqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFL1pEMNU8SLj%2F%2BjOircA0J2oaBOWXCGKhnhOUQ8%2Bt37b6rchc%2BJ%2Fn5uXAMzYKYJ6Q%2BmCHJKwOUTSm%2BM%2BQ4radqppZocFT%2B%2BVwK5QSWzf3kthm8XAghsZgirwHoQyfUz8DY6kcZSn90gRI1D%2FVkwMBbLM2XlEYu2cBoO4f2iBs%2B2yXYRV411InXWzbFs75yh1vjLsw2BfCAUnAu91LSPkd%2B96mG94wrtvTQEMW8Ny9PTum9UdXfEaimwHS86fQhlZ7psI9nhG8EW0fuJ67BFqi3wDfxzYpef5m5K3jbER0Ck4bU61nkhHfACoTghC4P%2BOtOLlLxrqkxQT1%2Bl%2FWhhppma9%2FIebqjUSyZ4M83vVVp%2ByVfR%2FqGe2SfeACzdPvkwpQiA62Jsd%2F18hdz5CAyzRKwesZ2nG%2BbRiQERyCcLonj9MhAxidc5IHKmDLFKOe8LtOl33%2FNoiLP5%2BLcoAnn%2BrXp07IdkWzyYNM4dsPP65mabr6V0li8%2B%2FaK5emqBFCYyRhrFfPcnuaaaLcJEzp%2FBmwieHAX0X3NFrwtqeGyktUxt5eC682Y0FNpFhaLIdculjgvUdR1T8Eh9p4GM2SGeUYZMpuw6XWXWRZjDcU7ioj81WTonYa2L3S48G2dsEevP2n98Znx33apVIbTzMPSw%2BrwGOqUB1y%2F0yyLGdU0DwNyeX5cB6HHarEc1Y%2BeuXAiHDY66Pvjd1b3fF1eJbExXEUolJ%2FUS5jzHyWCSGYhuB4NL7fr5CgcjDUKLiyt9CVPWvr7PeEMnZHuq0RPK6DUa%2B48aAfSPLOK02PLQM83H8y2ZJXQbxMZlxTOhbcAv7yD26HJIdEfDqzubM9ASuuHBE1XvgXC%2B7%2Bt7txrp61FqNlql3Fuobf1Y8XN4&X-Amz-Signature=210de4084e02b17fea37f3541763458d08c4f5c151b2506c7fb37b426c92da20&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKBY6CWH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F9oeVjkBVb7bHdOYYo%2B4fCvhzz0wdkJHWa%2FGLXY0ZOwIga4eBFQYnD70OfwPlGcyT2Fddp4ENRZhyGDh8n%2Fu%2Fc7oqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFL1pEMNU8SLj%2F%2BjOircA0J2oaBOWXCGKhnhOUQ8%2Bt37b6rchc%2BJ%2Fn5uXAMzYKYJ6Q%2BmCHJKwOUTSm%2BM%2BQ4radqppZocFT%2B%2BVwK5QSWzf3kthm8XAghsZgirwHoQyfUz8DY6kcZSn90gRI1D%2FVkwMBbLM2XlEYu2cBoO4f2iBs%2B2yXYRV411InXWzbFs75yh1vjLsw2BfCAUnAu91LSPkd%2B96mG94wrtvTQEMW8Ny9PTum9UdXfEaimwHS86fQhlZ7psI9nhG8EW0fuJ67BFqi3wDfxzYpef5m5K3jbER0Ck4bU61nkhHfACoTghC4P%2BOtOLlLxrqkxQT1%2Bl%2FWhhppma9%2FIebqjUSyZ4M83vVVp%2ByVfR%2FqGe2SfeACzdPvkwpQiA62Jsd%2F18hdz5CAyzRKwesZ2nG%2BbRiQERyCcLonj9MhAxidc5IHKmDLFKOe8LtOl33%2FNoiLP5%2BLcoAnn%2BrXp07IdkWzyYNM4dsPP65mabr6V0li8%2B%2FaK5emqBFCYyRhrFfPcnuaaaLcJEzp%2FBmwieHAX0X3NFrwtqeGyktUxt5eC682Y0FNpFhaLIdculjgvUdR1T8Eh9p4GM2SGeUYZMpuw6XWXWRZjDcU7ioj81WTonYa2L3S48G2dsEevP2n98Znx33apVIbTzMPSw%2BrwGOqUB1y%2F0yyLGdU0DwNyeX5cB6HHarEc1Y%2BeuXAiHDY66Pvjd1b3fF1eJbExXEUolJ%2FUS5jzHyWCSGYhuB4NL7fr5CgcjDUKLiyt9CVPWvr7PeEMnZHuq0RPK6DUa%2B48aAfSPLOK02PLQM83H8y2ZJXQbxMZlxTOhbcAv7yD26HJIdEfDqzubM9ASuuHBE1XvgXC%2B7%2Bt7txrp61FqNlql3Fuobf1Y8XN4&X-Amz-Signature=d51d64b894e6bf5f8b79bad37e3a6b1fef3790855867f1ca63d19a469f05fa10&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKBY6CWH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F9oeVjkBVb7bHdOYYo%2B4fCvhzz0wdkJHWa%2FGLXY0ZOwIga4eBFQYnD70OfwPlGcyT2Fddp4ENRZhyGDh8n%2Fu%2Fc7oqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFL1pEMNU8SLj%2F%2BjOircA0J2oaBOWXCGKhnhOUQ8%2Bt37b6rchc%2BJ%2Fn5uXAMzYKYJ6Q%2BmCHJKwOUTSm%2BM%2BQ4radqppZocFT%2B%2BVwK5QSWzf3kthm8XAghsZgirwHoQyfUz8DY6kcZSn90gRI1D%2FVkwMBbLM2XlEYu2cBoO4f2iBs%2B2yXYRV411InXWzbFs75yh1vjLsw2BfCAUnAu91LSPkd%2B96mG94wrtvTQEMW8Ny9PTum9UdXfEaimwHS86fQhlZ7psI9nhG8EW0fuJ67BFqi3wDfxzYpef5m5K3jbER0Ck4bU61nkhHfACoTghC4P%2BOtOLlLxrqkxQT1%2Bl%2FWhhppma9%2FIebqjUSyZ4M83vVVp%2ByVfR%2FqGe2SfeACzdPvkwpQiA62Jsd%2F18hdz5CAyzRKwesZ2nG%2BbRiQERyCcLonj9MhAxidc5IHKmDLFKOe8LtOl33%2FNoiLP5%2BLcoAnn%2BrXp07IdkWzyYNM4dsPP65mabr6V0li8%2B%2FaK5emqBFCYyRhrFfPcnuaaaLcJEzp%2FBmwieHAX0X3NFrwtqeGyktUxt5eC682Y0FNpFhaLIdculjgvUdR1T8Eh9p4GM2SGeUYZMpuw6XWXWRZjDcU7ioj81WTonYa2L3S48G2dsEevP2n98Znx33apVIbTzMPSw%2BrwGOqUB1y%2F0yyLGdU0DwNyeX5cB6HHarEc1Y%2BeuXAiHDY66Pvjd1b3fF1eJbExXEUolJ%2FUS5jzHyWCSGYhuB4NL7fr5CgcjDUKLiyt9CVPWvr7PeEMnZHuq0RPK6DUa%2B48aAfSPLOK02PLQM83H8y2ZJXQbxMZlxTOhbcAv7yD26HJIdEfDqzubM9ASuuHBE1XvgXC%2B7%2Bt7txrp61FqNlql3Fuobf1Y8XN4&X-Amz-Signature=c3198bf433ae1699ea68350d0ba132b0039df86b9db25aee071634843af9278d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKBY6CWH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F9oeVjkBVb7bHdOYYo%2B4fCvhzz0wdkJHWa%2FGLXY0ZOwIga4eBFQYnD70OfwPlGcyT2Fddp4ENRZhyGDh8n%2Fu%2Fc7oqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFL1pEMNU8SLj%2F%2BjOircA0J2oaBOWXCGKhnhOUQ8%2Bt37b6rchc%2BJ%2Fn5uXAMzYKYJ6Q%2BmCHJKwOUTSm%2BM%2BQ4radqppZocFT%2B%2BVwK5QSWzf3kthm8XAghsZgirwHoQyfUz8DY6kcZSn90gRI1D%2FVkwMBbLM2XlEYu2cBoO4f2iBs%2B2yXYRV411InXWzbFs75yh1vjLsw2BfCAUnAu91LSPkd%2B96mG94wrtvTQEMW8Ny9PTum9UdXfEaimwHS86fQhlZ7psI9nhG8EW0fuJ67BFqi3wDfxzYpef5m5K3jbER0Ck4bU61nkhHfACoTghC4P%2BOtOLlLxrqkxQT1%2Bl%2FWhhppma9%2FIebqjUSyZ4M83vVVp%2ByVfR%2FqGe2SfeACzdPvkwpQiA62Jsd%2F18hdz5CAyzRKwesZ2nG%2BbRiQERyCcLonj9MhAxidc5IHKmDLFKOe8LtOl33%2FNoiLP5%2BLcoAnn%2BrXp07IdkWzyYNM4dsPP65mabr6V0li8%2B%2FaK5emqBFCYyRhrFfPcnuaaaLcJEzp%2FBmwieHAX0X3NFrwtqeGyktUxt5eC682Y0FNpFhaLIdculjgvUdR1T8Eh9p4GM2SGeUYZMpuw6XWXWRZjDcU7ioj81WTonYa2L3S48G2dsEevP2n98Znx33apVIbTzMPSw%2BrwGOqUB1y%2F0yyLGdU0DwNyeX5cB6HHarEc1Y%2BeuXAiHDY66Pvjd1b3fF1eJbExXEUolJ%2FUS5jzHyWCSGYhuB4NL7fr5CgcjDUKLiyt9CVPWvr7PeEMnZHuq0RPK6DUa%2B48aAfSPLOK02PLQM83H8y2ZJXQbxMZlxTOhbcAv7yD26HJIdEfDqzubM9ASuuHBE1XvgXC%2B7%2Bt7txrp61FqNlql3Fuobf1Y8XN4&X-Amz-Signature=7f716807bdbf74b4a812b2cfe289b146a4d2196524cfa1b280b9404495f78c40&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKBY6CWH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F9oeVjkBVb7bHdOYYo%2B4fCvhzz0wdkJHWa%2FGLXY0ZOwIga4eBFQYnD70OfwPlGcyT2Fddp4ENRZhyGDh8n%2Fu%2Fc7oqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFL1pEMNU8SLj%2F%2BjOircA0J2oaBOWXCGKhnhOUQ8%2Bt37b6rchc%2BJ%2Fn5uXAMzYKYJ6Q%2BmCHJKwOUTSm%2BM%2BQ4radqppZocFT%2B%2BVwK5QSWzf3kthm8XAghsZgirwHoQyfUz8DY6kcZSn90gRI1D%2FVkwMBbLM2XlEYu2cBoO4f2iBs%2B2yXYRV411InXWzbFs75yh1vjLsw2BfCAUnAu91LSPkd%2B96mG94wrtvTQEMW8Ny9PTum9UdXfEaimwHS86fQhlZ7psI9nhG8EW0fuJ67BFqi3wDfxzYpef5m5K3jbER0Ck4bU61nkhHfACoTghC4P%2BOtOLlLxrqkxQT1%2Bl%2FWhhppma9%2FIebqjUSyZ4M83vVVp%2ByVfR%2FqGe2SfeACzdPvkwpQiA62Jsd%2F18hdz5CAyzRKwesZ2nG%2BbRiQERyCcLonj9MhAxidc5IHKmDLFKOe8LtOl33%2FNoiLP5%2BLcoAnn%2BrXp07IdkWzyYNM4dsPP65mabr6V0li8%2B%2FaK5emqBFCYyRhrFfPcnuaaaLcJEzp%2FBmwieHAX0X3NFrwtqeGyktUxt5eC682Y0FNpFhaLIdculjgvUdR1T8Eh9p4GM2SGeUYZMpuw6XWXWRZjDcU7ioj81WTonYa2L3S48G2dsEevP2n98Znx33apVIbTzMPSw%2BrwGOqUB1y%2F0yyLGdU0DwNyeX5cB6HHarEc1Y%2BeuXAiHDY66Pvjd1b3fF1eJbExXEUolJ%2FUS5jzHyWCSGYhuB4NL7fr5CgcjDUKLiyt9CVPWvr7PeEMnZHuq0RPK6DUa%2B48aAfSPLOK02PLQM83H8y2ZJXQbxMZlxTOhbcAv7yD26HJIdEfDqzubM9ASuuHBE1XvgXC%2B7%2Bt7txrp61FqNlql3Fuobf1Y8XN4&X-Amz-Signature=7ca17ca9417762bcc01511678371ee735cdcd537a1a6b7dc9e3c084727ae7be5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKBY6CWH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F9oeVjkBVb7bHdOYYo%2B4fCvhzz0wdkJHWa%2FGLXY0ZOwIga4eBFQYnD70OfwPlGcyT2Fddp4ENRZhyGDh8n%2Fu%2Fc7oqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFL1pEMNU8SLj%2F%2BjOircA0J2oaBOWXCGKhnhOUQ8%2Bt37b6rchc%2BJ%2Fn5uXAMzYKYJ6Q%2BmCHJKwOUTSm%2BM%2BQ4radqppZocFT%2B%2BVwK5QSWzf3kthm8XAghsZgirwHoQyfUz8DY6kcZSn90gRI1D%2FVkwMBbLM2XlEYu2cBoO4f2iBs%2B2yXYRV411InXWzbFs75yh1vjLsw2BfCAUnAu91LSPkd%2B96mG94wrtvTQEMW8Ny9PTum9UdXfEaimwHS86fQhlZ7psI9nhG8EW0fuJ67BFqi3wDfxzYpef5m5K3jbER0Ck4bU61nkhHfACoTghC4P%2BOtOLlLxrqkxQT1%2Bl%2FWhhppma9%2FIebqjUSyZ4M83vVVp%2ByVfR%2FqGe2SfeACzdPvkwpQiA62Jsd%2F18hdz5CAyzRKwesZ2nG%2BbRiQERyCcLonj9MhAxidc5IHKmDLFKOe8LtOl33%2FNoiLP5%2BLcoAnn%2BrXp07IdkWzyYNM4dsPP65mabr6V0li8%2B%2FaK5emqBFCYyRhrFfPcnuaaaLcJEzp%2FBmwieHAX0X3NFrwtqeGyktUxt5eC682Y0FNpFhaLIdculjgvUdR1T8Eh9p4GM2SGeUYZMpuw6XWXWRZjDcU7ioj81WTonYa2L3S48G2dsEevP2n98Znx33apVIbTzMPSw%2BrwGOqUB1y%2F0yyLGdU0DwNyeX5cB6HHarEc1Y%2BeuXAiHDY66Pvjd1b3fF1eJbExXEUolJ%2FUS5jzHyWCSGYhuB4NL7fr5CgcjDUKLiyt9CVPWvr7PeEMnZHuq0RPK6DUa%2B48aAfSPLOK02PLQM83H8y2ZJXQbxMZlxTOhbcAv7yD26HJIdEfDqzubM9ASuuHBE1XvgXC%2B7%2Bt7txrp61FqNlql3Fuobf1Y8XN4&X-Amz-Signature=c2b6af0ffe2ccd33a5ba93f0a0f624e4e3cd078395685015dd6b187b4552bf6a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCXL6LGC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMY9NDS7MBU9c7RyFPiSKEThu4jf1OGxRonVHkNM8ykwIgLvPEFZB5vKZYywUIrweHkuNrfBwU3X13Z%2Bx6XIzLZ4cqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOKaKgsoHxxnw0s9%2FyrcA2hEzI7MS8XPW95z6rs%2B%2BLIgtvM4QTUg91PjNH5nqja%2B5b9eqMBMo5wgyIBGS%2FEw7pHg7g8MHsaMgjzdlsJfCgGX5IQ0BYyhnXBdtCxXYwtaxQcadn12wJgkvveJEaWxkDQDumWi%2BHCtrGZJH%2B7VhY9l9UzotcG6UDXlo5Fh3buNfw3tY6nBHvOw%2Bc4i9jfHfZlE5itDpLZKeogBf5hBQ5dzHHuoQfvY5NJBiwQQdhANHzmSGUdyerdxHa9v4Rj97nQrJ8xLgNxBujB6DLg5WP2raCftN9UfzGYThcQlmOBMzxEdXb3V7SdLh2j6PCMBazDMkTHOdwBQoX2DFMTamS3BogALfmk9aVOCrXk7DYsnrXYygmhqutNxwV1YGIzsPvLlmaT9OEbRwHDB1%2BzO4cfCEHtXnvAwYw1GQ3kgC8cnn2Z3tGXjohkuYJeVCJBt4kh4jThZFO%2F%2F5jigrgDGxBX%2Fdae4m3mq7RFTR8UQMuYqYygI2vZyaECcmy8MwCwHsbovjHIfJqWHC8Us1GK3Gl1uVcvtMCiUiJ7VyZlzh0vG7y5cGnhZuZAoTTqD7ghO8%2FASqhZKSLJzNGJtCc4HlPHhjS3vnZi0v2Y1xYkt%2B1u86i5XDtOXVMnygdKJMMqx%2BrwGOqUBMyBPy59uEktaLPzjBjBGknsv2ESMxk%2FHz136UsDcieDhnyDo53MthLCLJElTmpJAZT2OO8sV7B%2BnE9CuYso2P%2B3XyHygyuZP725vtPlmvgOs93G4TjClCH0pMU8S02qZUcwYD8t%2B8vLBKTEBSOsXodXHz%2F%2F7E1bAh5rCVLAjDmQ1Z2k1Y8mNnVjBlbIZ3iRWtJBwjmhTCbC8YDFHMSaGoA5I%2BODc&X-Amz-Signature=287aba0d1295d978950fa6e4d03429d04596fcd5fbfc7cc51d9f09bdb31913f9&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A6EDDYD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcRLNrQxTGt5%2BgCvzKhd%2BEOkISFLF7MIXcpzYktGFPpAIhAO4Z126svO0zJUL4QJ6JHtQNoGYH8jzpvhNjWaHSYh3FKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxx5dX9zShK%2FErv4tAq3APLA2%2BuEEQ2RAdNsV6agrPNi%2FjfLW6xF3wtnXIFCCI7SmCu00WVY0j9oI2W%2FzKHfU2h8O%2BHwkz%2BLioiiFwYQhwLSJxsxl4p5f0v8zUlt29YwkmFNOAhZ7dnB2a9JAyPe6GjGmO2u%2FUG3pXyZZeIH1Evt4vgA9RjACV%2BLlFaYKfIaVQ%2B8%2BsJO1LGIrMoUAWtb7V3UjFrPyqE5J%2FqYc%2Botq74GfGoBlSTID%2BZd22Oxi5wo97UX3toGAgU4JhrvuWp%2Bc5IapRfFWJh9QmPFkmKHBiIGmlCqLgxRePWETiS5f5CYdBQIgW2u4F3Tjf4ylM517D3aoFi1tAp6TiQX2oU%2BDRE6K3MVwsmzU7WoQN1G6Qkyc%2F2pev%2FtrLTfRSTP%2BTJI9tACKhDE32UOz0ZOJMjPmsCuqownY%2FCzGDeU7vfkmZefruixJ1krWDcpaQ1Q%2B%2FQGIkKXtdQqO4v9E5Q2mGDdZJFIT%2FDrRTJe11j8V2WOWp5MmBLXdz2wQEvdrDrtGwCu5jPakNvVTGGeKbFmwi8xbsZ7WnOmJmfwfMsp0MgSEBbXXfirasReC4o7xbZI4ODyBLHSBbz0ZzAUqD9RbIWsFgKgaqWBGvykl2lK8B%2F36eyAEwDZQ0FrcAb8X0NKjD3sPq8BjqkAZ%2BnfDISMNUlcmqeotgbB0VQQrfneZisj53eTw6BZbOzUc0DcLQXyhWgV8lQ5F4DvMAwx0YhyKlFIJVub9r9xJ03ad7wuCrQrt5Sq42myFD9AwMWOgBeonYlNTHEJ2JUPo0gRrpwJbwffbk%2Bfe34810ZhfM4qed2eFKlpLecjH6lgLxlAR4gbLVKwb3mNdx6ZVaJHWHpjcS8g5oo4K3tgmwrjEP6&X-Amz-Signature=4dd9ed9f94ade166346567c9925b5914b28ad65de8a16c6baffd58ede4a85228&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKBY6CWH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F9oeVjkBVb7bHdOYYo%2B4fCvhzz0wdkJHWa%2FGLXY0ZOwIga4eBFQYnD70OfwPlGcyT2Fddp4ENRZhyGDh8n%2Fu%2Fc7oqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFL1pEMNU8SLj%2F%2BjOircA0J2oaBOWXCGKhnhOUQ8%2Bt37b6rchc%2BJ%2Fn5uXAMzYKYJ6Q%2BmCHJKwOUTSm%2BM%2BQ4radqppZocFT%2B%2BVwK5QSWzf3kthm8XAghsZgirwHoQyfUz8DY6kcZSn90gRI1D%2FVkwMBbLM2XlEYu2cBoO4f2iBs%2B2yXYRV411InXWzbFs75yh1vjLsw2BfCAUnAu91LSPkd%2B96mG94wrtvTQEMW8Ny9PTum9UdXfEaimwHS86fQhlZ7psI9nhG8EW0fuJ67BFqi3wDfxzYpef5m5K3jbER0Ck4bU61nkhHfACoTghC4P%2BOtOLlLxrqkxQT1%2Bl%2FWhhppma9%2FIebqjUSyZ4M83vVVp%2ByVfR%2FqGe2SfeACzdPvkwpQiA62Jsd%2F18hdz5CAyzRKwesZ2nG%2BbRiQERyCcLonj9MhAxidc5IHKmDLFKOe8LtOl33%2FNoiLP5%2BLcoAnn%2BrXp07IdkWzyYNM4dsPP65mabr6V0li8%2B%2FaK5emqBFCYyRhrFfPcnuaaaLcJEzp%2FBmwieHAX0X3NFrwtqeGyktUxt5eC682Y0FNpFhaLIdculjgvUdR1T8Eh9p4GM2SGeUYZMpuw6XWXWRZjDcU7ioj81WTonYa2L3S48G2dsEevP2n98Znx33apVIbTzMPSw%2BrwGOqUB1y%2F0yyLGdU0DwNyeX5cB6HHarEc1Y%2BeuXAiHDY66Pvjd1b3fF1eJbExXEUolJ%2FUS5jzHyWCSGYhuB4NL7fr5CgcjDUKLiyt9CVPWvr7PeEMnZHuq0RPK6DUa%2B48aAfSPLOK02PLQM83H8y2ZJXQbxMZlxTOhbcAv7yD26HJIdEfDqzubM9ASuuHBE1XvgXC%2B7%2Bt7txrp61FqNlql3Fuobf1Y8XN4&X-Amz-Signature=9a3f60ec9db3bba666231f80374c17b5d2e67d964b484a42185e407040f4d13b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKBY6CWH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F9oeVjkBVb7bHdOYYo%2B4fCvhzz0wdkJHWa%2FGLXY0ZOwIga4eBFQYnD70OfwPlGcyT2Fddp4ENRZhyGDh8n%2Fu%2Fc7oqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFL1pEMNU8SLj%2F%2BjOircA0J2oaBOWXCGKhnhOUQ8%2Bt37b6rchc%2BJ%2Fn5uXAMzYKYJ6Q%2BmCHJKwOUTSm%2BM%2BQ4radqppZocFT%2B%2BVwK5QSWzf3kthm8XAghsZgirwHoQyfUz8DY6kcZSn90gRI1D%2FVkwMBbLM2XlEYu2cBoO4f2iBs%2B2yXYRV411InXWzbFs75yh1vjLsw2BfCAUnAu91LSPkd%2B96mG94wrtvTQEMW8Ny9PTum9UdXfEaimwHS86fQhlZ7psI9nhG8EW0fuJ67BFqi3wDfxzYpef5m5K3jbER0Ck4bU61nkhHfACoTghC4P%2BOtOLlLxrqkxQT1%2Bl%2FWhhppma9%2FIebqjUSyZ4M83vVVp%2ByVfR%2FqGe2SfeACzdPvkwpQiA62Jsd%2F18hdz5CAyzRKwesZ2nG%2BbRiQERyCcLonj9MhAxidc5IHKmDLFKOe8LtOl33%2FNoiLP5%2BLcoAnn%2BrXp07IdkWzyYNM4dsPP65mabr6V0li8%2B%2FaK5emqBFCYyRhrFfPcnuaaaLcJEzp%2FBmwieHAX0X3NFrwtqeGyktUxt5eC682Y0FNpFhaLIdculjgvUdR1T8Eh9p4GM2SGeUYZMpuw6XWXWRZjDcU7ioj81WTonYa2L3S48G2dsEevP2n98Znx33apVIbTzMPSw%2BrwGOqUB1y%2F0yyLGdU0DwNyeX5cB6HHarEc1Y%2BeuXAiHDY66Pvjd1b3fF1eJbExXEUolJ%2FUS5jzHyWCSGYhuB4NL7fr5CgcjDUKLiyt9CVPWvr7PeEMnZHuq0RPK6DUa%2B48aAfSPLOK02PLQM83H8y2ZJXQbxMZlxTOhbcAv7yD26HJIdEfDqzubM9ASuuHBE1XvgXC%2B7%2Bt7txrp61FqNlql3Fuobf1Y8XN4&X-Amz-Signature=123c353a4693ddd621c6aff2e85c6a4eee1198002c60916a4c7444a3583575b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKBY6CWH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F9oeVjkBVb7bHdOYYo%2B4fCvhzz0wdkJHWa%2FGLXY0ZOwIga4eBFQYnD70OfwPlGcyT2Fddp4ENRZhyGDh8n%2Fu%2Fc7oqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFL1pEMNU8SLj%2F%2BjOircA0J2oaBOWXCGKhnhOUQ8%2Bt37b6rchc%2BJ%2Fn5uXAMzYKYJ6Q%2BmCHJKwOUTSm%2BM%2BQ4radqppZocFT%2B%2BVwK5QSWzf3kthm8XAghsZgirwHoQyfUz8DY6kcZSn90gRI1D%2FVkwMBbLM2XlEYu2cBoO4f2iBs%2B2yXYRV411InXWzbFs75yh1vjLsw2BfCAUnAu91LSPkd%2B96mG94wrtvTQEMW8Ny9PTum9UdXfEaimwHS86fQhlZ7psI9nhG8EW0fuJ67BFqi3wDfxzYpef5m5K3jbER0Ck4bU61nkhHfACoTghC4P%2BOtOLlLxrqkxQT1%2Bl%2FWhhppma9%2FIebqjUSyZ4M83vVVp%2ByVfR%2FqGe2SfeACzdPvkwpQiA62Jsd%2F18hdz5CAyzRKwesZ2nG%2BbRiQERyCcLonj9MhAxidc5IHKmDLFKOe8LtOl33%2FNoiLP5%2BLcoAnn%2BrXp07IdkWzyYNM4dsPP65mabr6V0li8%2B%2FaK5emqBFCYyRhrFfPcnuaaaLcJEzp%2FBmwieHAX0X3NFrwtqeGyktUxt5eC682Y0FNpFhaLIdculjgvUdR1T8Eh9p4GM2SGeUYZMpuw6XWXWRZjDcU7ioj81WTonYa2L3S48G2dsEevP2n98Znx33apVIbTzMPSw%2BrwGOqUB1y%2F0yyLGdU0DwNyeX5cB6HHarEc1Y%2BeuXAiHDY66Pvjd1b3fF1eJbExXEUolJ%2FUS5jzHyWCSGYhuB4NL7fr5CgcjDUKLiyt9CVPWvr7PeEMnZHuq0RPK6DUa%2B48aAfSPLOK02PLQM83H8y2ZJXQbxMZlxTOhbcAv7yD26HJIdEfDqzubM9ASuuHBE1XvgXC%2B7%2Bt7txrp61FqNlql3Fuobf1Y8XN4&X-Amz-Signature=87f0fdf62788f8b279f1bdd59d0283a8889e69e97e5f52d7401a1d47aed7f3bd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDT6A4MS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDx0mpXhPXelVIJSbuEUdojIBqc2DebiZFjxU8qmM%2FPdQIgAfvQPfOy2PCt7D8b2Y1DptpLTrrcWw6YI2%2FkuJcvxHwqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGOJaV1CGX%2BNntDuircA0akEQT1IDQOCxf%2F2nhyAvgh4YgxDMNI9fSmDfJucEzg6UCcygI78PRRXED4YdmUuxoMiW7yUwE1EutARfCRc6waU3LCsZWI0luc4cEHnqsAuieMTth3j8I1fWCfdYm33HSRTzOH2C6UfVIhKNdrB2Jj4Qf3TSryj5xQmzB6onyfrhYcEnpQu12ozfQgcXQpf8nfb5OJgcqrOmyzL6Wbavu3E0CFZsKN4vQbaon1U3FHzvsmKz6PW6FrAZs%2FNwqTONfGpuQXIDJk%2FhcW9yKcyVUb7AaBFEK6gh%2FEyVM7JQzG66PGjb9OZnSRziOgXr16r0qoqYFHFBRTNhdBdCznaHsJ2bt8LPutH%2BOG7rnIIkAfrNYrp3v3keKaRxt29m1wv4wBjW%2FEnBavRYGenm7u%2FqNPhpq1njLwD8vczUfqnybEl20dEw0dn%2B0kiudXFzfI9Oq5o6zxE%2Bw1yNSq7xNpvbACbl7zoz%2BT38KT%2FOY3UQqREQS9WUnS72GMGZjOi15izxDWGwIuZTbcEdOvUrNe73Uj0EUw6ehNCMXeVE%2FpHgjHGVutaBLOIbYwvoW0jXiT0prHhBT0mCesWR1k%2FngaNZ21Y8d4%2BP3d8EbO3Jb%2BecaS3Ol1Ah5cmeMGaeTLMICx%2BrwGOqUBQBj8WsG%2BqDIu%2FqelsFBJn7BxZab44YpAwn3YnCnnfHzEY1EJYIT8wBgH6%2B6TyZAuJsOuEhNO%2Fd%2BXar64Xqg8wRz1tRthXs9kzrjb1hlNu5%2FxWQ8Tq%2FNoupufanbyxiJesQLEE79V9Q4Fn%2B9CuD853HIF5%2BdhcWgd21QAOSXkvSpQVWFZyrttbDzEfQkQCOF6iUDx9WBD9M3L%2FJIZM6q%2FFt%2FzovlM&X-Amz-Signature=e4ee3a9b6357f2c1ead4c11d2c1da9adf1b306932273c1aa1962d0629aec7e40&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSFZLOVT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnLZaKLZECkleH%2BbcuI9e0Ch61vByXvMQC8GPFNn4GMAIhANjmRYe93M9kWa%2FByN4erBv4wjjL%2BCF%2F5fzwUjATTBg3KogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFb%2Bv%2B%2BOG%2FBAZx5g8q3AP%2FX105jKusBglYp%2B1AXkfGkqqHz69Hc7r2hDkWxiKr4kE8XcDV2tezFWmoDZJs%2B4FlsxxUrq9knClaHRxZpFrn2r9%2BoD0Sd7TqdRcP7syrrTZo9dG%2BFhh44l8AygEVUk9PbLRXVfKHfaW%2BM7O9llSbI6qeAAV6ajsOL2P4pBYd7WPVYxf%2FGHfOp4WC7Mbl1lBCirTMsKNWVOqB2Umymd2aAnWImw49Dn8Oe%2FaUfP6RBPVDKOTxnybl6LZ7tH9JGo0xpSUZPNtXhshEdy9QGtHfpl90l3LoSZCi1Pm6aAX0ghM31mxfCywCU7bonH7FBQR20MLnEq7En%2ForqmvlyZ9aIyLOSXJOMy9bEJD8hwFs3XQOoPXZKeI8OwBPqqlz4qsboPYVUITZg2uuTSHikqNyforY3%2BVH2DAR3tnjcEOG19iMnZk47D4o1j8QroIR%2BUkgZ%2FhqO00noCUy1sqlriAJCtg3UO4jj4TjSPBPbCqs3A9l6CNu6oln1FApvZvwID%2BZPK%2Fu0y0ildy9KICM6NBZ0DANrbdz92RtgWEaot5ubFFDmbUVOzavQtrHYHxMY%2BHanmel9xEpScuE1ev7NqOHb8xIkGg1nzyyihxTTb7mLxdeFp2myB0REzh%2F5DC4sfq8BjqkARL04AdeaiJM%2FgSTZua6Cu3orH%2FZ8iRdMVAszo3zWGrH9bwc8p6VLMo%2BkuH1ViXQzXkIIDRrVm92%2F49hAskXxqYd8hLfhDQPktl8vHBo5qbjk45vEXe6r41chxqivjTlUnzAn0%2F6%2FtyZ5ULiOndWkdQuJbhwIHC0iP8LHIQHiSZlWW7v6d21w56c0xm1%2F3%2BnvZPKtX6MsXSi%2BHtAMjKDKFk79WoJ&X-Amz-Signature=26a194464ac363630cf86f97082be34cfdcabd3bb205f197e8cb6faeca47e922&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUVC4Z47%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDu%2B2GkxRwO3S0LXSYJFl9IPmGTslBaEgP4NKXvNKmA4AiEAyx8ZXub0xxRx7s%2F8Q83JuBcz2tBE2eEsJgMydydNYFoqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFGoCY%2BuTGkhuNo0SyrcA0XdvaO53%2BSWapAtQZt8YFTkTe5zzVTosufS5YRFUy4PnRAJEwQzrA%2BQ4%2FjdkJa%2B0UgkM%2BVrplbRIm54ZwCNzZgOY64IU32rhOWln1LPvY%2FyvUUMA2%2BbwzA47v71wJXUkoxYUqU6VTwfK2QAifvy%2Bt235aIaeQAoh3CSiHndM%2FIaXehVvDbRU%2BcY4kSjQ5%2BpdQSMkQeTGKVv12lFWnW09BEa%2BeJyhtZakBUAHwieocd9ES69m7r3MOkBMwMNvFgQ%2BDCKrO7htXxAvYHqML9YQldwcNNMzTSq2H%2BKqlZaNzzWoUX5c2OfLb9kfeyw8vsiE8JnHsoDVY2noG8VpHFbv3UsMVXise8YsyjmAygMcXc38Uphf0SUHe7f3M3urd0JcTlY2SSNvrCylCFfi4LVh9nonOBa%2BJM48wOdymG5VYFRV%2B0%2BgT%2FR5PuaE7dXsRyUDBEYJERIJEvZCDdQmgccIw3HIKN0QKzGvq6JSkdD8OMvBlukxW%2FXPcmMnV8n%2BFALqActxE0pe%2FZBqHeQSZo9ZzjiUqLh8dBNWQzz4fEzLHhzvHi9%2F7tuqLS4DytdOr0ulAtRODo92D%2Bs7gI6Lurz6FfsUjZ2%2FvN06JZRDRwAXkjKci53%2FQd4nRYBxqq2MNex%2BrwGOqUBZATCYpwzuYeBjlu95AYEyKe%2BPafYEUV%2BhE4QKkgQGke8LJFRKjk%2FNVrGzWUXdAhT8Roa6tJIrurR3yL%2FEORYDotSU0FB7V5b0YYcNeZJX5qyzFx0MtgD%2FQjZOJHudlXZZdYrKtOWoL%2FGX72WoG72iGxRyyWbS%2Fvqg%2FIOmFcArD4b3ZNYB%2F%2FCW%2FHXQ1iNEgEBQH329IgnXuwga%2B3yS5A7GZvR5A03&X-Amz-Signature=2f01f5598be5e23812d8f4456fd6dd13ac5f61f400122914172b6b6bbedbeff9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJVHM7SL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA83UFWFVEk8QqSYxjN0rILYD82VFoniASz%2FXvoGJvNnAiEAiMnqw0%2B%2BYALZJ%2BDog%2FfEIeTFw7qm7GpABwZ5TlcyBpIqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2BrJjc57g4UV68PiyrcAxXRpfiqe9x5SdW%2BAoktBF5B41V6msD%2BWJtS4CYG296ztFepAq3EFD4kg7jO%2BAfXpJ%2F0y42ZKtZcaD8y%2F%2BnsuPO3XThFNpOi%2BkgPkuAqIwYOs0rbnWjlfxAnvHcWtLiYPU6A3kzqEKFduQBSZPJJNJwsAtwszB4DzBVaN8iUz73pLoCOyv9h8hNnb1iQlrAU5va%2FVT8AmLV%2BNQe4Akr%2B67eh22neoVnejHrfNgOxv7rLuuI3JUpcq19DRnWzPhY7FJch8Sihx5sxHGr2nZcY57HA6IALQ6wB4JgEcokOobPeUtybh6ZME7PcWbviyltlJDG3mmKfyUoavK62YQcfk4SiKT%2FDRJQmyfaRaOYaDT2ybC8ME9ROowjh8Qc78UHQf2jnZqVDS4WGjeBhkYYMdVpQCU1R0%2Bp6kST%2Bbdq4BxdQYCsPCvCvCw2CStpdBmbDohMZZMtKQdH0kVc2xUtL%2BLIE2JMLhYA9lcKWfDk05QvmLIBfvxaAmgtYq1RkjtY7Ek4ZMTl%2Fp%2Fzx2TJ28cXMn3jhnypth2kXJ1RFHQ9jtDPSJCXKjQ2OcozMcAAKZf6jASrnTepZdRHfkGrIFzS2V8jbG2WkXdpcQaNASQHzV8chgUptNaqThIHfaxxQMJ%2Bx%2BrwGOqUBVSYzdyXY83TZUvs%2BvcMfJoSeoXGXzc8%2F8xpRZdlT2CPGbWPCBvmOdI9x13y5QDjUeX55pYAKevFWsVWCJauTUPukDDIz4FjOuIokYK44pwV%2Fx6e%2FYHClqyaSBYYRL372WJcBf0g%2BFHSn6hO7dfyfsqUlKRH3Dn96dzE%2FYx7FfYbcv4p73fn29MaIzAKym8nd9iKIAL9LeAD8w7QWOPzplv2xn74O&X-Amz-Signature=5f2afe99751d0fa56f8f3e5fb82617955138d89cfcf1118c6a13a1510b29193b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJVHM7SL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA83UFWFVEk8QqSYxjN0rILYD82VFoniASz%2FXvoGJvNnAiEAiMnqw0%2B%2BYALZJ%2BDog%2FfEIeTFw7qm7GpABwZ5TlcyBpIqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2BrJjc57g4UV68PiyrcAxXRpfiqe9x5SdW%2BAoktBF5B41V6msD%2BWJtS4CYG296ztFepAq3EFD4kg7jO%2BAfXpJ%2F0y42ZKtZcaD8y%2F%2BnsuPO3XThFNpOi%2BkgPkuAqIwYOs0rbnWjlfxAnvHcWtLiYPU6A3kzqEKFduQBSZPJJNJwsAtwszB4DzBVaN8iUz73pLoCOyv9h8hNnb1iQlrAU5va%2FVT8AmLV%2BNQe4Akr%2B67eh22neoVnejHrfNgOxv7rLuuI3JUpcq19DRnWzPhY7FJch8Sihx5sxHGr2nZcY57HA6IALQ6wB4JgEcokOobPeUtybh6ZME7PcWbviyltlJDG3mmKfyUoavK62YQcfk4SiKT%2FDRJQmyfaRaOYaDT2ybC8ME9ROowjh8Qc78UHQf2jnZqVDS4WGjeBhkYYMdVpQCU1R0%2Bp6kST%2Bbdq4BxdQYCsPCvCvCw2CStpdBmbDohMZZMtKQdH0kVc2xUtL%2BLIE2JMLhYA9lcKWfDk05QvmLIBfvxaAmgtYq1RkjtY7Ek4ZMTl%2Fp%2Fzx2TJ28cXMn3jhnypth2kXJ1RFHQ9jtDPSJCXKjQ2OcozMcAAKZf6jASrnTepZdRHfkGrIFzS2V8jbG2WkXdpcQaNASQHzV8chgUptNaqThIHfaxxQMJ%2Bx%2BrwGOqUBVSYzdyXY83TZUvs%2BvcMfJoSeoXGXzc8%2F8xpRZdlT2CPGbWPCBvmOdI9x13y5QDjUeX55pYAKevFWsVWCJauTUPukDDIz4FjOuIokYK44pwV%2Fx6e%2FYHClqyaSBYYRL372WJcBf0g%2BFHSn6hO7dfyfsqUlKRH3Dn96dzE%2FYx7FfYbcv4p73fn29MaIzAKym8nd9iKIAL9LeAD8w7QWOPzplv2xn74O&X-Amz-Signature=a10acbf9c879bc2001a9034bceba1b5aee9cfab25022d53cd8543dace2b0ebde&X-Amz-SignedHeaders=host&x-id=GetObject)

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
