

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XH33O5NX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICaYW4RC9AmJs%2Fh42xDqHaYL%2Bb0eJQpvc8ouFFnsPE49AiARw4ybCHQTnHAdEw%2B3byYqc7FezBv4M5AQ3fyI8bN7zyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJqwAV5Wgncq8eRnoKtwDpfTajsgLGdK5WE6pYgKsKCvHT1nrmtsdbtB5C4Mq9haBdYhR4F4BEngF%2Bn2ltP%2FfuBl7t3gxp8LcD7zH%2BHofnzRiqc9zdX43KfHkoV%2FuYm5bYVtGC8A%2BIi8Ak51qFPInjXC%2B%2F6gpMvZK%2BUldpC62xg62wZN%2BDFcbNFU348FMiwz2h%2BTvAEMFshnWIGpXPaSfZnc91gEGCzNl5Blk02O5EL3T13LFTWAz1PwhHtNqlWkDRObkEZqHMV2CznM2G928kd31P%2FFzVgujtfP2CXN6QuEjqqxZLIQjDHnvR5zqkB3vCeOS9htFZjaXr9ZF2agvQVW%2BRJHNylClUlTsc6xmnlQV4DDWQ0pjp4u9bCyiHc4kJY0hAfej%2F4nJEqyKsso4E8oZDCKEw1OLTnb%2FX4JnboiiWlkF0CfzX8RKEQ4L%2FlBSulYHfdhE2mLPOCKf5yLa4F64sdJXs8CHTFHATF803jquf78QlnCZdxANg4zjCpcQS6Az2qEaHPSWSlhZxLb5waOp02NrNVhh0%2BSZ%2FCssZaW8%2F9mm8%2BgMhRrCrF1d3zVkVC8dk3YsQP5T%2BqtLOqdPJaSTngJ4uU%2FocVPHP7QsLka5oXP%2FALftqmXY8lTWYo2NcfTNUExa8oJgtpIwncjzvAY6pgEz6ti5VpvAfqHyE9lBAU2Ky21cpprw5EoE43Eo6kV3YzFeqQUymKymtT1hpVjq%2Brzom2hHdKAjYZYfknFHMqhsFKQ5kVQCIPSFEoCEI0SohRuXB86MRlp10zCC4WWDgQIx1Gf2uLRtHDHFOWZiGyouM6uUzBFU6ibOFaFqp4lETQVsMLDM%2FwwO42srfpVUaiiG03H5u92gls8ocSDIZcj95s4JjbbA&X-Amz-Signature=197b662cee93ff416178c606ee540e7de668a01f1621ad568441173adc919eec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XH33O5NX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICaYW4RC9AmJs%2Fh42xDqHaYL%2Bb0eJQpvc8ouFFnsPE49AiARw4ybCHQTnHAdEw%2B3byYqc7FezBv4M5AQ3fyI8bN7zyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJqwAV5Wgncq8eRnoKtwDpfTajsgLGdK5WE6pYgKsKCvHT1nrmtsdbtB5C4Mq9haBdYhR4F4BEngF%2Bn2ltP%2FfuBl7t3gxp8LcD7zH%2BHofnzRiqc9zdX43KfHkoV%2FuYm5bYVtGC8A%2BIi8Ak51qFPInjXC%2B%2F6gpMvZK%2BUldpC62xg62wZN%2BDFcbNFU348FMiwz2h%2BTvAEMFshnWIGpXPaSfZnc91gEGCzNl5Blk02O5EL3T13LFTWAz1PwhHtNqlWkDRObkEZqHMV2CznM2G928kd31P%2FFzVgujtfP2CXN6QuEjqqxZLIQjDHnvR5zqkB3vCeOS9htFZjaXr9ZF2agvQVW%2BRJHNylClUlTsc6xmnlQV4DDWQ0pjp4u9bCyiHc4kJY0hAfej%2F4nJEqyKsso4E8oZDCKEw1OLTnb%2FX4JnboiiWlkF0CfzX8RKEQ4L%2FlBSulYHfdhE2mLPOCKf5yLa4F64sdJXs8CHTFHATF803jquf78QlnCZdxANg4zjCpcQS6Az2qEaHPSWSlhZxLb5waOp02NrNVhh0%2BSZ%2FCssZaW8%2F9mm8%2BgMhRrCrF1d3zVkVC8dk3YsQP5T%2BqtLOqdPJaSTngJ4uU%2FocVPHP7QsLka5oXP%2FALftqmXY8lTWYo2NcfTNUExa8oJgtpIwncjzvAY6pgEz6ti5VpvAfqHyE9lBAU2Ky21cpprw5EoE43Eo6kV3YzFeqQUymKymtT1hpVjq%2Brzom2hHdKAjYZYfknFHMqhsFKQ5kVQCIPSFEoCEI0SohRuXB86MRlp10zCC4WWDgQIx1Gf2uLRtHDHFOWZiGyouM6uUzBFU6ibOFaFqp4lETQVsMLDM%2FwwO42srfpVUaiiG03H5u92gls8ocSDIZcj95s4JjbbA&X-Amz-Signature=724f936b0a94ed1efbd9a0eedec4ebefd581ba8d96434aa3fda8ae5612e17c64&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XH33O5NX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICaYW4RC9AmJs%2Fh42xDqHaYL%2Bb0eJQpvc8ouFFnsPE49AiARw4ybCHQTnHAdEw%2B3byYqc7FezBv4M5AQ3fyI8bN7zyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJqwAV5Wgncq8eRnoKtwDpfTajsgLGdK5WE6pYgKsKCvHT1nrmtsdbtB5C4Mq9haBdYhR4F4BEngF%2Bn2ltP%2FfuBl7t3gxp8LcD7zH%2BHofnzRiqc9zdX43KfHkoV%2FuYm5bYVtGC8A%2BIi8Ak51qFPInjXC%2B%2F6gpMvZK%2BUldpC62xg62wZN%2BDFcbNFU348FMiwz2h%2BTvAEMFshnWIGpXPaSfZnc91gEGCzNl5Blk02O5EL3T13LFTWAz1PwhHtNqlWkDRObkEZqHMV2CznM2G928kd31P%2FFzVgujtfP2CXN6QuEjqqxZLIQjDHnvR5zqkB3vCeOS9htFZjaXr9ZF2agvQVW%2BRJHNylClUlTsc6xmnlQV4DDWQ0pjp4u9bCyiHc4kJY0hAfej%2F4nJEqyKsso4E8oZDCKEw1OLTnb%2FX4JnboiiWlkF0CfzX8RKEQ4L%2FlBSulYHfdhE2mLPOCKf5yLa4F64sdJXs8CHTFHATF803jquf78QlnCZdxANg4zjCpcQS6Az2qEaHPSWSlhZxLb5waOp02NrNVhh0%2BSZ%2FCssZaW8%2F9mm8%2BgMhRrCrF1d3zVkVC8dk3YsQP5T%2BqtLOqdPJaSTngJ4uU%2FocVPHP7QsLka5oXP%2FALftqmXY8lTWYo2NcfTNUExa8oJgtpIwncjzvAY6pgEz6ti5VpvAfqHyE9lBAU2Ky21cpprw5EoE43Eo6kV3YzFeqQUymKymtT1hpVjq%2Brzom2hHdKAjYZYfknFHMqhsFKQ5kVQCIPSFEoCEI0SohRuXB86MRlp10zCC4WWDgQIx1Gf2uLRtHDHFOWZiGyouM6uUzBFU6ibOFaFqp4lETQVsMLDM%2FwwO42srfpVUaiiG03H5u92gls8ocSDIZcj95s4JjbbA&X-Amz-Signature=a44204de8c2a6719a7f35f0c902e91bdab878a67e80de51fe653deac653c5060&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2IO5S2H%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8oITlWhKsdONSrGmHJdlPdMir6c%2FlX8bE3%2BQggP%2FE0wIhAO8V5Lr0q6u5%2FjMfDuiUtyXt1izsjl5tBI9ctK%2BJeWrOKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdR%2BmWyWQAsDYbgr0q3AO0fdC3pclHblXe91Tl3NYqEv9Gwd7cnHBbhybMeDcOuuAnYOgb%2FutMTo09sQBNAMoGz47yeE4KsSeVmFRBPJPb2d0Xs9vWr0M%2B8OB6r1hrUdIX4TkBYenC3h5twPH2AzAC6H%2F%2F8PayhMR4Lxh4Wd4aabJgmsRyvA63Ibx9ERoyBt2LnXPVSt7yUrLHocFZNmr69DPu2bTe4ifX7OmU%2F1bWHqIb40iwebTL8cFOIk%2BYgMtOaKD3cfqa2fRaVfPttjd6PwrqDAPf7ev6HzYs3WuvZEaFDEWWkAJAsgYUE5Avyb0O316UQ6Ygt8vA4BSctU5HBWsIkymo%2BDSMuasMLUdw07I779ta8PGWEHItqqYcbDwUY65swqu4UKrLDlhZHTeTudLPvamlvljX6U%2BZaME69lZYA%2BpilZy6u38a3sTqmbeDJu2RcukHlNNTi%2FFmBLzCiFvzfGchskyGKqPERCwK4HALqcv%2BfpdPuTi8YwgLYyJTHIJwEB135V8S9KY%2BDQQzGH2y9ksV1RZkWBmQB80Imb2umehE5AGTc0HB1gDeqPD3rdV7i6SYpTXPWIUXrr74N%2FmCPmocKO22a2TeNP5PF8MlsSj8lPXmsmaWIgqkFTtDVvOnvNSbuRgEFzDKyPO8BjqkASem6FavP866hiGb2br30xWjKcz7g6BT4%2Fm3XABBw9xmJr%2BzXjfJX9Mhnj0d1wHOb5%2Bc3R%2Bjz0Zt2YBK12ujfVpGOE5J12S%2FihbnFbWbNL1sRFV5DcjDFIYwK96TPkEma9WybRFpqOvA95oNmnRryeNtk4cAMPzyoZcjsHY8zZqYDYlJhNKsBZ%2FJHsrxc%2F2XqrhibAWvKSHHF16pHH1bhdZUJn17&X-Amz-Signature=1e93c924415ed1b940815506c45f30f86b27020455bbc8f5b687037068c6dd2a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2IO5S2H%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8oITlWhKsdONSrGmHJdlPdMir6c%2FlX8bE3%2BQggP%2FE0wIhAO8V5Lr0q6u5%2FjMfDuiUtyXt1izsjl5tBI9ctK%2BJeWrOKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdR%2BmWyWQAsDYbgr0q3AO0fdC3pclHblXe91Tl3NYqEv9Gwd7cnHBbhybMeDcOuuAnYOgb%2FutMTo09sQBNAMoGz47yeE4KsSeVmFRBPJPb2d0Xs9vWr0M%2B8OB6r1hrUdIX4TkBYenC3h5twPH2AzAC6H%2F%2F8PayhMR4Lxh4Wd4aabJgmsRyvA63Ibx9ERoyBt2LnXPVSt7yUrLHocFZNmr69DPu2bTe4ifX7OmU%2F1bWHqIb40iwebTL8cFOIk%2BYgMtOaKD3cfqa2fRaVfPttjd6PwrqDAPf7ev6HzYs3WuvZEaFDEWWkAJAsgYUE5Avyb0O316UQ6Ygt8vA4BSctU5HBWsIkymo%2BDSMuasMLUdw07I779ta8PGWEHItqqYcbDwUY65swqu4UKrLDlhZHTeTudLPvamlvljX6U%2BZaME69lZYA%2BpilZy6u38a3sTqmbeDJu2RcukHlNNTi%2FFmBLzCiFvzfGchskyGKqPERCwK4HALqcv%2BfpdPuTi8YwgLYyJTHIJwEB135V8S9KY%2BDQQzGH2y9ksV1RZkWBmQB80Imb2umehE5AGTc0HB1gDeqPD3rdV7i6SYpTXPWIUXrr74N%2FmCPmocKO22a2TeNP5PF8MlsSj8lPXmsmaWIgqkFTtDVvOnvNSbuRgEFzDKyPO8BjqkASem6FavP866hiGb2br30xWjKcz7g6BT4%2Fm3XABBw9xmJr%2BzXjfJX9Mhnj0d1wHOb5%2Bc3R%2Bjz0Zt2YBK12ujfVpGOE5J12S%2FihbnFbWbNL1sRFV5DcjDFIYwK96TPkEma9WybRFpqOvA95oNmnRryeNtk4cAMPzyoZcjsHY8zZqYDYlJhNKsBZ%2FJHsrxc%2F2XqrhibAWvKSHHF16pHH1bhdZUJn17&X-Amz-Signature=5b4885f641605c831575b7d9d39dc1a89e8e989c1ebb3f71d00d8176e034c56a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2IO5S2H%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8oITlWhKsdONSrGmHJdlPdMir6c%2FlX8bE3%2BQggP%2FE0wIhAO8V5Lr0q6u5%2FjMfDuiUtyXt1izsjl5tBI9ctK%2BJeWrOKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdR%2BmWyWQAsDYbgr0q3AO0fdC3pclHblXe91Tl3NYqEv9Gwd7cnHBbhybMeDcOuuAnYOgb%2FutMTo09sQBNAMoGz47yeE4KsSeVmFRBPJPb2d0Xs9vWr0M%2B8OB6r1hrUdIX4TkBYenC3h5twPH2AzAC6H%2F%2F8PayhMR4Lxh4Wd4aabJgmsRyvA63Ibx9ERoyBt2LnXPVSt7yUrLHocFZNmr69DPu2bTe4ifX7OmU%2F1bWHqIb40iwebTL8cFOIk%2BYgMtOaKD3cfqa2fRaVfPttjd6PwrqDAPf7ev6HzYs3WuvZEaFDEWWkAJAsgYUE5Avyb0O316UQ6Ygt8vA4BSctU5HBWsIkymo%2BDSMuasMLUdw07I779ta8PGWEHItqqYcbDwUY65swqu4UKrLDlhZHTeTudLPvamlvljX6U%2BZaME69lZYA%2BpilZy6u38a3sTqmbeDJu2RcukHlNNTi%2FFmBLzCiFvzfGchskyGKqPERCwK4HALqcv%2BfpdPuTi8YwgLYyJTHIJwEB135V8S9KY%2BDQQzGH2y9ksV1RZkWBmQB80Imb2umehE5AGTc0HB1gDeqPD3rdV7i6SYpTXPWIUXrr74N%2FmCPmocKO22a2TeNP5PF8MlsSj8lPXmsmaWIgqkFTtDVvOnvNSbuRgEFzDKyPO8BjqkASem6FavP866hiGb2br30xWjKcz7g6BT4%2Fm3XABBw9xmJr%2BzXjfJX9Mhnj0d1wHOb5%2Bc3R%2Bjz0Zt2YBK12ujfVpGOE5J12S%2FihbnFbWbNL1sRFV5DcjDFIYwK96TPkEma9WybRFpqOvA95oNmnRryeNtk4cAMPzyoZcjsHY8zZqYDYlJhNKsBZ%2FJHsrxc%2F2XqrhibAWvKSHHF16pHH1bhdZUJn17&X-Amz-Signature=cac985b8f8c116c1841daec6600611cf3482cd5c8967ead0b6a6db6fa8f248ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2IO5S2H%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8oITlWhKsdONSrGmHJdlPdMir6c%2FlX8bE3%2BQggP%2FE0wIhAO8V5Lr0q6u5%2FjMfDuiUtyXt1izsjl5tBI9ctK%2BJeWrOKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdR%2BmWyWQAsDYbgr0q3AO0fdC3pclHblXe91Tl3NYqEv9Gwd7cnHBbhybMeDcOuuAnYOgb%2FutMTo09sQBNAMoGz47yeE4KsSeVmFRBPJPb2d0Xs9vWr0M%2B8OB6r1hrUdIX4TkBYenC3h5twPH2AzAC6H%2F%2F8PayhMR4Lxh4Wd4aabJgmsRyvA63Ibx9ERoyBt2LnXPVSt7yUrLHocFZNmr69DPu2bTe4ifX7OmU%2F1bWHqIb40iwebTL8cFOIk%2BYgMtOaKD3cfqa2fRaVfPttjd6PwrqDAPf7ev6HzYs3WuvZEaFDEWWkAJAsgYUE5Avyb0O316UQ6Ygt8vA4BSctU5HBWsIkymo%2BDSMuasMLUdw07I779ta8PGWEHItqqYcbDwUY65swqu4UKrLDlhZHTeTudLPvamlvljX6U%2BZaME69lZYA%2BpilZy6u38a3sTqmbeDJu2RcukHlNNTi%2FFmBLzCiFvzfGchskyGKqPERCwK4HALqcv%2BfpdPuTi8YwgLYyJTHIJwEB135V8S9KY%2BDQQzGH2y9ksV1RZkWBmQB80Imb2umehE5AGTc0HB1gDeqPD3rdV7i6SYpTXPWIUXrr74N%2FmCPmocKO22a2TeNP5PF8MlsSj8lPXmsmaWIgqkFTtDVvOnvNSbuRgEFzDKyPO8BjqkASem6FavP866hiGb2br30xWjKcz7g6BT4%2Fm3XABBw9xmJr%2BzXjfJX9Mhnj0d1wHOb5%2Bc3R%2Bjz0Zt2YBK12ujfVpGOE5J12S%2FihbnFbWbNL1sRFV5DcjDFIYwK96TPkEma9WybRFpqOvA95oNmnRryeNtk4cAMPzyoZcjsHY8zZqYDYlJhNKsBZ%2FJHsrxc%2F2XqrhibAWvKSHHF16pHH1bhdZUJn17&X-Amz-Signature=0b081da11fdf1871a30f6935c6913fe47272ca7566a65b8f92bb57ba2d82b507&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2IO5S2H%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8oITlWhKsdONSrGmHJdlPdMir6c%2FlX8bE3%2BQggP%2FE0wIhAO8V5Lr0q6u5%2FjMfDuiUtyXt1izsjl5tBI9ctK%2BJeWrOKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdR%2BmWyWQAsDYbgr0q3AO0fdC3pclHblXe91Tl3NYqEv9Gwd7cnHBbhybMeDcOuuAnYOgb%2FutMTo09sQBNAMoGz47yeE4KsSeVmFRBPJPb2d0Xs9vWr0M%2B8OB6r1hrUdIX4TkBYenC3h5twPH2AzAC6H%2F%2F8PayhMR4Lxh4Wd4aabJgmsRyvA63Ibx9ERoyBt2LnXPVSt7yUrLHocFZNmr69DPu2bTe4ifX7OmU%2F1bWHqIb40iwebTL8cFOIk%2BYgMtOaKD3cfqa2fRaVfPttjd6PwrqDAPf7ev6HzYs3WuvZEaFDEWWkAJAsgYUE5Avyb0O316UQ6Ygt8vA4BSctU5HBWsIkymo%2BDSMuasMLUdw07I779ta8PGWEHItqqYcbDwUY65swqu4UKrLDlhZHTeTudLPvamlvljX6U%2BZaME69lZYA%2BpilZy6u38a3sTqmbeDJu2RcukHlNNTi%2FFmBLzCiFvzfGchskyGKqPERCwK4HALqcv%2BfpdPuTi8YwgLYyJTHIJwEB135V8S9KY%2BDQQzGH2y9ksV1RZkWBmQB80Imb2umehE5AGTc0HB1gDeqPD3rdV7i6SYpTXPWIUXrr74N%2FmCPmocKO22a2TeNP5PF8MlsSj8lPXmsmaWIgqkFTtDVvOnvNSbuRgEFzDKyPO8BjqkASem6FavP866hiGb2br30xWjKcz7g6BT4%2Fm3XABBw9xmJr%2BzXjfJX9Mhnj0d1wHOb5%2Bc3R%2Bjz0Zt2YBK12ujfVpGOE5J12S%2FihbnFbWbNL1sRFV5DcjDFIYwK96TPkEma9WybRFpqOvA95oNmnRryeNtk4cAMPzyoZcjsHY8zZqYDYlJhNKsBZ%2FJHsrxc%2F2XqrhibAWvKSHHF16pHH1bhdZUJn17&X-Amz-Signature=6f3266eea9c6e16ae9a728aca1bb27826b03d87a119b8ca907730d8e891c296a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2IO5S2H%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8oITlWhKsdONSrGmHJdlPdMir6c%2FlX8bE3%2BQggP%2FE0wIhAO8V5Lr0q6u5%2FjMfDuiUtyXt1izsjl5tBI9ctK%2BJeWrOKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdR%2BmWyWQAsDYbgr0q3AO0fdC3pclHblXe91Tl3NYqEv9Gwd7cnHBbhybMeDcOuuAnYOgb%2FutMTo09sQBNAMoGz47yeE4KsSeVmFRBPJPb2d0Xs9vWr0M%2B8OB6r1hrUdIX4TkBYenC3h5twPH2AzAC6H%2F%2F8PayhMR4Lxh4Wd4aabJgmsRyvA63Ibx9ERoyBt2LnXPVSt7yUrLHocFZNmr69DPu2bTe4ifX7OmU%2F1bWHqIb40iwebTL8cFOIk%2BYgMtOaKD3cfqa2fRaVfPttjd6PwrqDAPf7ev6HzYs3WuvZEaFDEWWkAJAsgYUE5Avyb0O316UQ6Ygt8vA4BSctU5HBWsIkymo%2BDSMuasMLUdw07I779ta8PGWEHItqqYcbDwUY65swqu4UKrLDlhZHTeTudLPvamlvljX6U%2BZaME69lZYA%2BpilZy6u38a3sTqmbeDJu2RcukHlNNTi%2FFmBLzCiFvzfGchskyGKqPERCwK4HALqcv%2BfpdPuTi8YwgLYyJTHIJwEB135V8S9KY%2BDQQzGH2y9ksV1RZkWBmQB80Imb2umehE5AGTc0HB1gDeqPD3rdV7i6SYpTXPWIUXrr74N%2FmCPmocKO22a2TeNP5PF8MlsSj8lPXmsmaWIgqkFTtDVvOnvNSbuRgEFzDKyPO8BjqkASem6FavP866hiGb2br30xWjKcz7g6BT4%2Fm3XABBw9xmJr%2BzXjfJX9Mhnj0d1wHOb5%2Bc3R%2Bjz0Zt2YBK12ujfVpGOE5J12S%2FihbnFbWbNL1sRFV5DcjDFIYwK96TPkEma9WybRFpqOvA95oNmnRryeNtk4cAMPzyoZcjsHY8zZqYDYlJhNKsBZ%2FJHsrxc%2F2XqrhibAWvKSHHF16pHH1bhdZUJn17&X-Amz-Signature=78885556eb7ae3d8d543ff2b1e1fcabf972e897e263204dae815357e97d31d33&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWK6UP3Z%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGbpP5ik%2BK7K7izYWS6Xp29VPgiQneIdmtHRuGxy%2FHBJAiEAu4GMUbgymMGCL30zGOE6hzs8y1IYV%2FCNwvQacmYREjQqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbP2E%2Fd15%2BhyVAYaCrcA89nAH2Ro7kV0oOLLazmsvmsbbkUizbzzPHIHPl7MeMAmY%2BCacpyixz0sKwvvyS1Qa%2FmsQhWlaxB4NLr1Jf%2BtBE9SD79kCrdtAZ1VXLe6WkEMl10NbI%2BZ%2BSRu0qpVj1H10JAMEhvF%2B2M11gIklYKqaGcvkb%2FuBVY9iz6FWHZ3ZMml4yyC%2FINn84jTswi3K7rIP3mGVXoUwRED3XdeddXup5tMmyZi%2BNtYrsqazajw0NgdyXKuV%2FlkmVVEniB%2B80zyWqwPY1x9DKj52vmsFR4fFMhTRzyS%2F4s1xRnpVuvx2YtkAFAZOh6cyBNfXZKRJR9li1WjoMcaQFVxkp9hnd6AtIoAhPxqJ6Js%2FYw52lJD8jiZdF1LfzqhvLzzTwMJBvAcPFnycBHBjzV2o6FL%2FwscXTeKalGwJJ7%2FDqUSlKcDmRZ45ZIs0SoGSkQ%2Bu%2BSwwSSm%2BK5xj0KfjJ%2F3Qvi8AXYUXeL%2FjeibuQcOW5wXMyOOwOovrsTpumj5tlnLwg2CGAFRnv8g78y1o0JZn%2BRhFv%2F7XMpJZY4CcU%2B87NhbVzP0O0WuYXfQIDytRoDw15ZF3XyEGg2qD%2BtVLejOho4TeD6fKytKNjiLceD%2FC0YrDpNrpdLGqOYXzpWdeRIkHuqMJPI87wGOqUBo72gidtSe4GI2t5gtGpTiov36hrTYDLb6IoyvWVFKUmJLn8dEj%2BNL28O886ES6Nc8kTf9fdeeD5uTSRHuoTof0Uf29DQoNHzUeQcoKNyXDbzB1Cwo9SFWgaAZmFUjjm8wJFCQlaOPhWXjyDLTkPBkINYcGNyqOeU9cWweyxpoCdryuzZD26b0a3R6sDaKkCwGbcK%2FOR7iBHGWuXRpvoVW%2BvaW9YG&X-Amz-Signature=e33eabe9a206508518b5a2a5682c17df53eaf656ef900cb3541130d980c27695&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIDWNTWB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCt%2Bwe9c%2FaKCyOANTwuN5pM%2Fc2RuDp54Mr6SE%2BVTLYOHAIgVmgUtqyKzcGFYriGjy6Ihx6O2YcoDphn7RlF5xw1qhIqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD5mfIwDMCTKeI47eSrcA5Cyh6gPN%2BxWbKYmmn8WAdqxEgagVnOTLNX%2BNqcL2l7yxebZ0kkIjzYYQVSRlf4JbRpYSHsKfbCIQCZsssujrQqGwM57QmvBFUSQeb3X8MS%2FtEkaIuX%2Bn8FtqV3FV9W8MsgDngvTeXOHbXfBR7Mi1Ie0zNctHSo69ZPeWt%2F6HsXKxF809K53KXKZNY6KSzYCdvoweKwCQunk9bvYFd9iWJfsbhJYAI8XbX%2BqPOb7%2B6ah%2FOzEIpG%2BHaqya6O7xF%2FtMj5TnoIUblXcrEiDOqIQ6s%2BUiYYLmlLMNtO762tTYNdW2RXRh7DlcSzC%2FYYLPP%2FkSBZSOgNaKr1PXFQmByhDWg99uX0Ii%2F1c%2Bh41UQSLzS0iYiiwdqt2DoupzFzrcOjZYJKZUkxcM9zjCk8ILosxUqArsdOvLd1OuvYM9R9L2iyFu%2F90dIiM4pR6M8Lkv7lQlbtdv0AR9fHbUQyi%2BfX%2FodYyxjtwszcH0HgbJMULZUKgVrY8P2qPAhbLVBis3VsZBWHnPaO4kLl30aaIV4j33gLTn9v5hq6nxEQuinFjedjPXqzTMKsfNDOiqcsIXMuo2caFIH3uF28yA3qGPJ5IHeHWG%2F1I8S7MsNm18gCzEZ1kQHdsJdzkJlqrLAMMMIrI87wGOqUBCGGKQZlnFL34SanLU2UPqgiQMU2oUk9KO%2FXpVQVGZztnJJWoj3sI4SRinHLcFvSs4alTqtaMX%2BlTUuw%2FLNU7GGu57XLMT2EOkWd%2BGFfbMGOcFShnkVVYTZPGvuG6SnDq7mbBR6K%2BWLhMHfrxD3R6w1NJrBtJzUZNrR45zgrKyhawTakl4tw8Qch6N2eBr3vuzjrDlCucnVTh7CZ3PRyu3g1Lu10Z&X-Amz-Signature=8ab26d4305244f8bf25fa745fef9dcdf5d9556dfc832c9487ede0996030212e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2IO5S2H%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8oITlWhKsdONSrGmHJdlPdMir6c%2FlX8bE3%2BQggP%2FE0wIhAO8V5Lr0q6u5%2FjMfDuiUtyXt1izsjl5tBI9ctK%2BJeWrOKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdR%2BmWyWQAsDYbgr0q3AO0fdC3pclHblXe91Tl3NYqEv9Gwd7cnHBbhybMeDcOuuAnYOgb%2FutMTo09sQBNAMoGz47yeE4KsSeVmFRBPJPb2d0Xs9vWr0M%2B8OB6r1hrUdIX4TkBYenC3h5twPH2AzAC6H%2F%2F8PayhMR4Lxh4Wd4aabJgmsRyvA63Ibx9ERoyBt2LnXPVSt7yUrLHocFZNmr69DPu2bTe4ifX7OmU%2F1bWHqIb40iwebTL8cFOIk%2BYgMtOaKD3cfqa2fRaVfPttjd6PwrqDAPf7ev6HzYs3WuvZEaFDEWWkAJAsgYUE5Avyb0O316UQ6Ygt8vA4BSctU5HBWsIkymo%2BDSMuasMLUdw07I779ta8PGWEHItqqYcbDwUY65swqu4UKrLDlhZHTeTudLPvamlvljX6U%2BZaME69lZYA%2BpilZy6u38a3sTqmbeDJu2RcukHlNNTi%2FFmBLzCiFvzfGchskyGKqPERCwK4HALqcv%2BfpdPuTi8YwgLYyJTHIJwEB135V8S9KY%2BDQQzGH2y9ksV1RZkWBmQB80Imb2umehE5AGTc0HB1gDeqPD3rdV7i6SYpTXPWIUXrr74N%2FmCPmocKO22a2TeNP5PF8MlsSj8lPXmsmaWIgqkFTtDVvOnvNSbuRgEFzDKyPO8BjqkASem6FavP866hiGb2br30xWjKcz7g6BT4%2Fm3XABBw9xmJr%2BzXjfJX9Mhnj0d1wHOb5%2Bc3R%2Bjz0Zt2YBK12ujfVpGOE5J12S%2FihbnFbWbNL1sRFV5DcjDFIYwK96TPkEma9WybRFpqOvA95oNmnRryeNtk4cAMPzyoZcjsHY8zZqYDYlJhNKsBZ%2FJHsrxc%2F2XqrhibAWvKSHHF16pHH1bhdZUJn17&X-Amz-Signature=b6552eb1afc4733b33445dbf9c1de1254d19833eefcf1928edc898ea60d482aa&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2IO5S2H%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8oITlWhKsdONSrGmHJdlPdMir6c%2FlX8bE3%2BQggP%2FE0wIhAO8V5Lr0q6u5%2FjMfDuiUtyXt1izsjl5tBI9ctK%2BJeWrOKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdR%2BmWyWQAsDYbgr0q3AO0fdC3pclHblXe91Tl3NYqEv9Gwd7cnHBbhybMeDcOuuAnYOgb%2FutMTo09sQBNAMoGz47yeE4KsSeVmFRBPJPb2d0Xs9vWr0M%2B8OB6r1hrUdIX4TkBYenC3h5twPH2AzAC6H%2F%2F8PayhMR4Lxh4Wd4aabJgmsRyvA63Ibx9ERoyBt2LnXPVSt7yUrLHocFZNmr69DPu2bTe4ifX7OmU%2F1bWHqIb40iwebTL8cFOIk%2BYgMtOaKD3cfqa2fRaVfPttjd6PwrqDAPf7ev6HzYs3WuvZEaFDEWWkAJAsgYUE5Avyb0O316UQ6Ygt8vA4BSctU5HBWsIkymo%2BDSMuasMLUdw07I779ta8PGWEHItqqYcbDwUY65swqu4UKrLDlhZHTeTudLPvamlvljX6U%2BZaME69lZYA%2BpilZy6u38a3sTqmbeDJu2RcukHlNNTi%2FFmBLzCiFvzfGchskyGKqPERCwK4HALqcv%2BfpdPuTi8YwgLYyJTHIJwEB135V8S9KY%2BDQQzGH2y9ksV1RZkWBmQB80Imb2umehE5AGTc0HB1gDeqPD3rdV7i6SYpTXPWIUXrr74N%2FmCPmocKO22a2TeNP5PF8MlsSj8lPXmsmaWIgqkFTtDVvOnvNSbuRgEFzDKyPO8BjqkASem6FavP866hiGb2br30xWjKcz7g6BT4%2Fm3XABBw9xmJr%2BzXjfJX9Mhnj0d1wHOb5%2Bc3R%2Bjz0Zt2YBK12ujfVpGOE5J12S%2FihbnFbWbNL1sRFV5DcjDFIYwK96TPkEma9WybRFpqOvA95oNmnRryeNtk4cAMPzyoZcjsHY8zZqYDYlJhNKsBZ%2FJHsrxc%2F2XqrhibAWvKSHHF16pHH1bhdZUJn17&X-Amz-Signature=fa6342ded5679004db7449550840408229fc192da88b838809c5d8ebc6f75b03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2IO5S2H%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8oITlWhKsdONSrGmHJdlPdMir6c%2FlX8bE3%2BQggP%2FE0wIhAO8V5Lr0q6u5%2FjMfDuiUtyXt1izsjl5tBI9ctK%2BJeWrOKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdR%2BmWyWQAsDYbgr0q3AO0fdC3pclHblXe91Tl3NYqEv9Gwd7cnHBbhybMeDcOuuAnYOgb%2FutMTo09sQBNAMoGz47yeE4KsSeVmFRBPJPb2d0Xs9vWr0M%2B8OB6r1hrUdIX4TkBYenC3h5twPH2AzAC6H%2F%2F8PayhMR4Lxh4Wd4aabJgmsRyvA63Ibx9ERoyBt2LnXPVSt7yUrLHocFZNmr69DPu2bTe4ifX7OmU%2F1bWHqIb40iwebTL8cFOIk%2BYgMtOaKD3cfqa2fRaVfPttjd6PwrqDAPf7ev6HzYs3WuvZEaFDEWWkAJAsgYUE5Avyb0O316UQ6Ygt8vA4BSctU5HBWsIkymo%2BDSMuasMLUdw07I779ta8PGWEHItqqYcbDwUY65swqu4UKrLDlhZHTeTudLPvamlvljX6U%2BZaME69lZYA%2BpilZy6u38a3sTqmbeDJu2RcukHlNNTi%2FFmBLzCiFvzfGchskyGKqPERCwK4HALqcv%2BfpdPuTi8YwgLYyJTHIJwEB135V8S9KY%2BDQQzGH2y9ksV1RZkWBmQB80Imb2umehE5AGTc0HB1gDeqPD3rdV7i6SYpTXPWIUXrr74N%2FmCPmocKO22a2TeNP5PF8MlsSj8lPXmsmaWIgqkFTtDVvOnvNSbuRgEFzDKyPO8BjqkASem6FavP866hiGb2br30xWjKcz7g6BT4%2Fm3XABBw9xmJr%2BzXjfJX9Mhnj0d1wHOb5%2Bc3R%2Bjz0Zt2YBK12ujfVpGOE5J12S%2FihbnFbWbNL1sRFV5DcjDFIYwK96TPkEma9WybRFpqOvA95oNmnRryeNtk4cAMPzyoZcjsHY8zZqYDYlJhNKsBZ%2FJHsrxc%2F2XqrhibAWvKSHHF16pHH1bhdZUJn17&X-Amz-Signature=42ea4de151095db7f888be64f798459661d214d3c56fd45028fa68abc1227fd3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZ3TBQFQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5H8uqyXV95xDriGC2NGR6lkDqQ%2FpLItcCCxlTfyOMpAIgN7vp%2B8d9jBqSAW%2FgfF1UlQtrw%2BSuqErW5Z31UF1tjHIqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGtTCCiL3aL9VePuyrcA7%2BMkb7l3qMNsuuigUMPJtFzdv2W7zpf64ka8fr%2B8JnkFlcgxdVSGitu%2BGjWXBhty7dD%2Baeq%2BgOfYQ3P5QQueVWDiF5b6PvoHEfQT0t8p5fiGLbJm37lDJxI69ph2ADIV39jnzXN0vMNAk45J4ANST1f%2BJf3qoSxHlMHR7Ox%2BJZLNVmX5aVQc5q5amSqc0tKgpOIgTMVlDCyHIBt8XyS9IT2Lx%2BdWiXzHBxQGNoYBP1BPdmOcnhDxObmH%2BJfQGhJ0NMv4SINb7eXFkHatAkiWiiVhmZakOw%2BDBBxNGwMb7P7GzGWfokzQGLoQrpee5lfu2ozKrglExlRY6ZnulYpPpSWCQlieZE9XI9UmXxFxQX8YTqXPBucW6MUMGXTiI9ZXD3YCLi96YjzmU7sGxXGvW3eREPh%2FusGhBbyHVYLY2pTCn%2FpVYUc3PGIaWTFrS0qmjsfHJxsf7caBBdcwsP3GFj8y0voQcgO%2FVnouh8IAsM3P4apoVEFqEExF5WN%2BS9MPXqa0pLgZCPT1gVSPm%2BZgm93GGXEwPYwSckrvORzUEIpUnhNZj0xQPmRjBRXyfAh3QeekESHYyyqaLKtvh1rEZj9TwSKiH54nx9RfNobFCirz1XLDq6fD%2FJYuk4jMMHI87wGOqUBXizWoGEaE2SBqVSj4ItTXFOhO%2BYs%2FcsVyli1%2B4BjAm0EQlNsDtcm0woAoSVufb%2B0JCiBbp8qhcjDmz4iJHh2rqT0C6%2FeQyCDZ3TffbpGjU3cLXyt3j0mRTgHYeU3Jkn1W1UQjuinckBlBnJGdpmceDyXx%2FPCrFOVOWIuI%2FeYfUToREzy%2FakCMyyBX4S3w3Kp7xPkQ9KArOPw637xjgwu8er%2BRjw1&X-Amz-Signature=a6ba4f6b28144b978e32796d1c38506dc48b6815e6293d84d00d020cae779d32&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ADBGOAK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLclmZ93A76SlBWhnrsSRSwJhYzCMbTlZoAV6S1fKcLAIhAMoWJiC%2F7URMxhC6dqVa6zWXd8KO4PhvADmOaZh%2FKs81KogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyCfCsZr14ke7NPFNAq3ANrXxxzVjYSGtJuEB8skcR2mdIr0nh%2B3RuqYKdiMejAUAMFM3E3JtGWteX9yeHtWc6bwQmjCYvNFWGWy9FGt%2FrMwGTOZEK9%2B5en4bNCZNrWwEYhRt%2BnCpvm6TMVsaG6lwaTN8P14nibSjvMZKK9WRO7sFcRoWbegS4CQlqqCaso2FagKMUiuAOM2jDeM1NlERk%2Fy8YcUfr1g%2F6Rkla4NLmNHpsV9p%2B%2F1%2FkGE%2FjXdwy4U2GVL1dhPTfrrzPjXq8%2B0gOT91TNHPdBEAIvubfRs5T7tVGpBzqU7hg6PJb0oimCJv3y7F7PIZUVxRwwzwLlV3ZGSObcOTBhijjlZATycoekEzDPtoUPySsRsEiFZLTLUS6qKYJLgPFc0QSbd0KxjoagH729W8H407fdLm9zDc0zSEqCUvdyR96cMX%2BJqzDRtFCVVSsQZnv2DuhWdnia3kgDgdLslGu05Gjv9bISLb6FA5jrGvL2LOL9YJsvTaE%2FE9ZnpHt%2FZX5GTa4%2F2reB6DclRLrS%2BL2e%2FxjYBbHltY5x5lIwqTqm%2FfPWvorFPk19MxZwGsTgFI7%2B3A9vfqKKVmJPFjOg4nHIuRUEYmYxOSSihxHVAozFCd0hu%2FESlI37P5a%2Bz7QavkcR4H3otjCTyPO8BjqkAZ91X9GmtK0vQpM0f%2Fau7A0xZ6Tl8gaeQr2Lz2iYrKwHDBVU8%2F1Hl4jbWKHVOqCmRJnjuiqvPaJbKz4iJvATdKAF%2FAmor%2Fg3TkFIXJI7mVbK9GTI1rxdr6RT3xNVtTSvQdHZm9ipjZFL36N0Y1Zq4nD0RQ8mYJ6dh%2FYQ5FofYGTBXxRmlC5Cp20UbDjLBJ36miOBnLptCu7wTPch4sdYAWE7vx%2Bs&X-Amz-Signature=926dcca941e841b0751c48cbb79c01cf6d9c61deeca2b5a6a37666b088ab2ad5&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPU3D6MK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCh0EPq5LLyzP222CWLFfVa19Gwok%2FRsmm2MdjJM50dJgIgPnxH5YE4MsILL6dorzpr8YgXJLGVYRq5NSDyXCBpgXEqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM2DdK91514tmMbThircAxWHPXXZH5C1b%2BrVYFA0cS2H9%2Bv40rccWXpilFzRzYfnmEjmyBvI18JHfRI03OzdQJMukeAhwYLcGSHq0Ap70kDl1VTV9A%2F1qlj0lFJIIMyjkM7acND4ovzRkFmRz32W2V%2FOmrmR1hcYHNbmbVXr%2F8oMnGlRyGQLs1RsJbg2DOollIHLCPXyTgzM3bKXeWq61I2HQPNnko2wW%2F5MC8N4Q5LiW%2F%2BQG02LjpluVNHmFp%2Fk%2FIFmu0LV9qWW5DM8Si04EbgO%2FHvA4o8xyw7jK1oY9V4YQsKMiLePHO39z9hMukH99pos8glVCOiFlUaSqGiUq9wO7uDheYupL8n770SVSd9uc%2Fa2ZZ3IyWl6kkVaI%2F%2F9vfcAk98zHX1qCetFVfsW6eZTIPb10TeZdIkdf63pK1ZNyxjWWZZtwtMsB05T13uGk%2B9UoWgRJOFr9wnUHCVcLroM6owBeHVp7IQQDqPZ4KXNiwgrDQjzX6Y0M4vcmOG5%2BMTPseIgbP8Q1RPG423Z4%2Fd0h%2B0eXY3q2nYE6uLrb8tL%2BZMNvd0LJmtimzW%2FMBWHaD8ZM1BVEIccLlfwh%2BLPPn0sdxAs%2FbYTZSuoU9egj9%2BVrHAEPIb5X3HSCjheyju%2BL4urUHQta728va04MJTI87wGOqUBVBgQ%2BpXr6y4fHcUVBUJ6Av4jRJU9C5BNS%2BtWeopt36Z1TxUBfJHkoY%2Fmcv3Gpqew1J93y9X5ZDgDA2lQ7nbB845GhtQJ5S3k72xEUj71uC8czbyddEA5ZyaZ7srTKexmfTSl26msHUBxrGmerSZFyfS6fCqCiRmilEfX93N4ZmJB%2B6Zf4X28QF%2Bxvgg4Pc5aHYU%2F9YplBBD7MkGYRm6H6NzrFbRa&X-Amz-Signature=17d80e4543c8a9ee2a4530def61ec1f88798680a6a02c3ab89e46552cfbe7449&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA3TV2MK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcseKE1M4HU9HsdUZLhHkVyOokh7S0sfYa7be0qabjzgIhAIrAZ%2BYa3NrGvjopMaZpxgKxk1os8yhiIoRV1VHw2LnYKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzyURFWZ2Un75XyGcq3APnY4btjhPRR%2Fg%2FmguTHcvePBZvq4w96wF9CU9z1gMIfp1KUDr3u8WXGAEGroGWka1jGLwmq8S1ZQV4u7Uq8AKsqspG13wU2xWc7un4N50ODo0olFk%2BKGkFWcILhAxCaGMUL2I07V6vStL%2B3aLFlVpymzy7HaVJDyI7q3%2FKM%2FaBNA2OY0hEoFKLXqGUaB9X7sL%2F1gSnWpOcxpnTQavxMsAIJp7EI73zYDJe%2BDYrTtvANTlssh4s5PUvt6nf%2Bto0A%2F62lqogJz%2BqtTGNIGFizse5L4%2F0djoyS3t4hfZ%2F5PR%2FeQYE0VAudQHu86dv2S5gBRxs7i7pxJWI7B6ZVjigGm7yy1lzo9DN8%2BTLIGpLi3S1uzD08FHFU0V%2FxNLjhWgCGRG7OcOOrPIu0mXzCiqlKMLMxRcAxaK8cTm6%2F9a9wcx2Ml9UUWMR%2Bw6NKIeIYqUFAOXIoXHYBOtfdJbNICPSJGC0VCzfugfqJRPETM4eLB5Qd2GOXRzni5gJDcIrWj6HZ2N0%2BV2EMg8F3KpGSK8raAIkykLhKmO0NQ7Q3qrDls%2BMdj7z3bv6O30l3sMyl4sg%2FcsOa2UyLiknGyGtgaetK5lIUnlIrDNAEvwo51e%2F1pQwVcKo%2FeILtPCM6mFUdDDLyPO8BjqkAT1HWOJS5hCaKAZ0KYFOJmvAJsu0k0jxi%2BLkIP7hNdajIXk0bcEXyOxX8%2F4auoxkBYhocTNNrlMEl9r%2BDA3RrzFgW9%2Fl2IhIv8kMeFkJ2mqECxxTTGfMptTzLzrGeZqQHxiZqqdSozmT5MKkjArv5g3TETAfRD2WwYkum2APkcIHdNrxyEslAhwRPUVUtL8ov3UjvsyeV64i0YYrv3sinPh%2BV9FK&X-Amz-Signature=528ede00cec671cae7136fa64806f612f9379656030b48455b6b75f889b8ca2d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA3TV2MK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcseKE1M4HU9HsdUZLhHkVyOokh7S0sfYa7be0qabjzgIhAIrAZ%2BYa3NrGvjopMaZpxgKxk1os8yhiIoRV1VHw2LnYKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzyURFWZ2Un75XyGcq3APnY4btjhPRR%2Fg%2FmguTHcvePBZvq4w96wF9CU9z1gMIfp1KUDr3u8WXGAEGroGWka1jGLwmq8S1ZQV4u7Uq8AKsqspG13wU2xWc7un4N50ODo0olFk%2BKGkFWcILhAxCaGMUL2I07V6vStL%2B3aLFlVpymzy7HaVJDyI7q3%2FKM%2FaBNA2OY0hEoFKLXqGUaB9X7sL%2F1gSnWpOcxpnTQavxMsAIJp7EI73zYDJe%2BDYrTtvANTlssh4s5PUvt6nf%2Bto0A%2F62lqogJz%2BqtTGNIGFizse5L4%2F0djoyS3t4hfZ%2F5PR%2FeQYE0VAudQHu86dv2S5gBRxs7i7pxJWI7B6ZVjigGm7yy1lzo9DN8%2BTLIGpLi3S1uzD08FHFU0V%2FxNLjhWgCGRG7OcOOrPIu0mXzCiqlKMLMxRcAxaK8cTm6%2F9a9wcx2Ml9UUWMR%2Bw6NKIeIYqUFAOXIoXHYBOtfdJbNICPSJGC0VCzfugfqJRPETM4eLB5Qd2GOXRzni5gJDcIrWj6HZ2N0%2BV2EMg8F3KpGSK8raAIkykLhKmO0NQ7Q3qrDls%2BMdj7z3bv6O30l3sMyl4sg%2FcsOa2UyLiknGyGtgaetK5lIUnlIrDNAEvwo51e%2F1pQwVcKo%2FeILtPCM6mFUdDDLyPO8BjqkAT1HWOJS5hCaKAZ0KYFOJmvAJsu0k0jxi%2BLkIP7hNdajIXk0bcEXyOxX8%2F4auoxkBYhocTNNrlMEl9r%2BDA3RrzFgW9%2Fl2IhIv8kMeFkJ2mqECxxTTGfMptTzLzrGeZqQHxiZqqdSozmT5MKkjArv5g3TETAfRD2WwYkum2APkcIHdNrxyEslAhwRPUVUtL8ov3UjvsyeV64i0YYrv3sinPh%2BV9FK&X-Amz-Signature=99e762f3ca51cf003c6f739b81aecb72f3c48682a33bfaddcd419e5c02b191fb&X-Amz-SignedHeaders=host&x-id=GetObject)

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
