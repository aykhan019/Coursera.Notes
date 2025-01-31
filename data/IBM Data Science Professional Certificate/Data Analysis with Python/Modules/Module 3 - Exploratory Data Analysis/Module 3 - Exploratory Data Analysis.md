

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QSV2VBH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBT7DyUPp%2B7L1xMGVrOoWygQ25JKEBpl33NDvoKY0dDgIhANSEN8VS1wLuNkeFrJjRsYRePeM5fS2HhmYd%2BcXQ5BFyKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwmvlQTlB%2FTymnR9Dsq3ANW0zsHl5XPMn%2Foqb8hggw4iwI9GwrOFDrAxzhREnSNKNqIlYg3zBOwHATIvI%2BrC%2F5av5%2BFxd6kZf%2BC9byHiP0ntYrjcbgVIeYTRdjJIoiEb%2BCG5FdB4DJAO5%2FN%2FJ6a0ur637IJ0Zmo0qBShMhUO17CKCZQDz8MdoN1uxj%2B5ZjSTwMj0M6EyA%2F6881iSqbGjymzNH4VEJL6ow%2F4eYiETBSy52QaBEjCyup%2BMXexV%2BO5ibLE2gSwhJNUVP%2B4AAav7gcERI6q92HB6eZlvFhMlIPnlP06NAZHOHRRN%2F4OOPxXPPfvZW%2BDoBNuZnEZ11VmVQRK8zFg3OXetyWPZjqArXk0p2fuYfbAX6ny6h2d8CkJ0%2BpF1YnQeg25DvEy9yy5cq%2F2UOxQkabqjJdA%2FHqla%2Bk6Y9Ka6b8EHvw9XcJJq5BNWQyW23fn8lbjXjibKoxfnp39dfjjp%2BfekMyFLrVpqsIn0X05lPIhxpnvwd3EvN5nlVGGrV5PCtuihkE4IuwW6MqlneE1MR9eVN8k2ApsYx3f%2FYyugB3oAP8maKsJnODt%2B7s14IcR4RUzQfTX5kKKFsdpXXXLytMfPCxrRo8f7%2F6qZ24FWcWBpjO2W3s51Wi4qYwSiVDQrkk23bBG8zCIpPS8BjqkAck0OQzduyNsFMhojqDRwL66Poagt1fbQFMWNTKemPLUPr9XEruy5XC%2FxNu3q48H7ga3M1VGt1Rje5DHnI1Kf3%2Bp1xSscORBY0yw9On8A4KtWG0ZWDgUhr38FXOzqphT6YcZy9h0gUOXCTKhuFUT5J2CpBh8L6qHi%2F3LPZunkzJLnIIwtI7rbWbLii4l2JbRgj0eb6WOzFQ4Ukf1C2ISqGYWyKi1&X-Amz-Signature=43d6fd41e049b8ca8e981c4e18e1b81b32d393d07a9f3755ea688b4599bed40b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QSV2VBH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBT7DyUPp%2B7L1xMGVrOoWygQ25JKEBpl33NDvoKY0dDgIhANSEN8VS1wLuNkeFrJjRsYRePeM5fS2HhmYd%2BcXQ5BFyKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwmvlQTlB%2FTymnR9Dsq3ANW0zsHl5XPMn%2Foqb8hggw4iwI9GwrOFDrAxzhREnSNKNqIlYg3zBOwHATIvI%2BrC%2F5av5%2BFxd6kZf%2BC9byHiP0ntYrjcbgVIeYTRdjJIoiEb%2BCG5FdB4DJAO5%2FN%2FJ6a0ur637IJ0Zmo0qBShMhUO17CKCZQDz8MdoN1uxj%2B5ZjSTwMj0M6EyA%2F6881iSqbGjymzNH4VEJL6ow%2F4eYiETBSy52QaBEjCyup%2BMXexV%2BO5ibLE2gSwhJNUVP%2B4AAav7gcERI6q92HB6eZlvFhMlIPnlP06NAZHOHRRN%2F4OOPxXPPfvZW%2BDoBNuZnEZ11VmVQRK8zFg3OXetyWPZjqArXk0p2fuYfbAX6ny6h2d8CkJ0%2BpF1YnQeg25DvEy9yy5cq%2F2UOxQkabqjJdA%2FHqla%2Bk6Y9Ka6b8EHvw9XcJJq5BNWQyW23fn8lbjXjibKoxfnp39dfjjp%2BfekMyFLrVpqsIn0X05lPIhxpnvwd3EvN5nlVGGrV5PCtuihkE4IuwW6MqlneE1MR9eVN8k2ApsYx3f%2FYyugB3oAP8maKsJnODt%2B7s14IcR4RUzQfTX5kKKFsdpXXXLytMfPCxrRo8f7%2F6qZ24FWcWBpjO2W3s51Wi4qYwSiVDQrkk23bBG8zCIpPS8BjqkAck0OQzduyNsFMhojqDRwL66Poagt1fbQFMWNTKemPLUPr9XEruy5XC%2FxNu3q48H7ga3M1VGt1Rje5DHnI1Kf3%2Bp1xSscORBY0yw9On8A4KtWG0ZWDgUhr38FXOzqphT6YcZy9h0gUOXCTKhuFUT5J2CpBh8L6qHi%2F3LPZunkzJLnIIwtI7rbWbLii4l2JbRgj0eb6WOzFQ4Ukf1C2ISqGYWyKi1&X-Amz-Signature=8b33f41169aff5252d22eaf25d9cff40719dae3b9de6e66fd1fc261d09751fbb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QSV2VBH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBT7DyUPp%2B7L1xMGVrOoWygQ25JKEBpl33NDvoKY0dDgIhANSEN8VS1wLuNkeFrJjRsYRePeM5fS2HhmYd%2BcXQ5BFyKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwmvlQTlB%2FTymnR9Dsq3ANW0zsHl5XPMn%2Foqb8hggw4iwI9GwrOFDrAxzhREnSNKNqIlYg3zBOwHATIvI%2BrC%2F5av5%2BFxd6kZf%2BC9byHiP0ntYrjcbgVIeYTRdjJIoiEb%2BCG5FdB4DJAO5%2FN%2FJ6a0ur637IJ0Zmo0qBShMhUO17CKCZQDz8MdoN1uxj%2B5ZjSTwMj0M6EyA%2F6881iSqbGjymzNH4VEJL6ow%2F4eYiETBSy52QaBEjCyup%2BMXexV%2BO5ibLE2gSwhJNUVP%2B4AAav7gcERI6q92HB6eZlvFhMlIPnlP06NAZHOHRRN%2F4OOPxXPPfvZW%2BDoBNuZnEZ11VmVQRK8zFg3OXetyWPZjqArXk0p2fuYfbAX6ny6h2d8CkJ0%2BpF1YnQeg25DvEy9yy5cq%2F2UOxQkabqjJdA%2FHqla%2Bk6Y9Ka6b8EHvw9XcJJq5BNWQyW23fn8lbjXjibKoxfnp39dfjjp%2BfekMyFLrVpqsIn0X05lPIhxpnvwd3EvN5nlVGGrV5PCtuihkE4IuwW6MqlneE1MR9eVN8k2ApsYx3f%2FYyugB3oAP8maKsJnODt%2B7s14IcR4RUzQfTX5kKKFsdpXXXLytMfPCxrRo8f7%2F6qZ24FWcWBpjO2W3s51Wi4qYwSiVDQrkk23bBG8zCIpPS8BjqkAck0OQzduyNsFMhojqDRwL66Poagt1fbQFMWNTKemPLUPr9XEruy5XC%2FxNu3q48H7ga3M1VGt1Rje5DHnI1Kf3%2Bp1xSscORBY0yw9On8A4KtWG0ZWDgUhr38FXOzqphT6YcZy9h0gUOXCTKhuFUT5J2CpBh8L6qHi%2F3LPZunkzJLnIIwtI7rbWbLii4l2JbRgj0eb6WOzFQ4Ukf1C2ISqGYWyKi1&X-Amz-Signature=e98424336b28020ba9d5c50ddbe232fb255d7da8a1c2c79a01fef7d4ba8ab3f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQVDTL3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbVWq%2F0Q10jXAfmu8c83%2FiFdNzs1H8BArf29G2dSmjWAiEA%2FROZPwMWcy335CCQKQJCZQ12Cpor1Jsrmeibzp2m12gqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiFzEq4eoz3xR%2FEWyrcA1VquYmFwao%2FZTJbqXmHY9t8FciSRJIyJffRI98nou7jFwdOHDk20wJzh19nK9ioJfMRfW0QaSD7VW4h4QH401vWYeBIpcJab5pR4dJLZW%2BDH90eZYInAkZSKkyZycbzcLjQXVQawNj9y2%2BWoRSJqi9K9Rlola0U6ZN3CMcFPqHyTFXdzEri1GOAPLvOq0IdEBiJ5O7QPHFYNLsBZn9fl9tKzTwu9pLrz6NoPg97nZSZZX7q2iAM9vsGshOzY4Akpinuwt4NxabLRuzhyWMthrZQZU8i3JMT51QT%2BFfhmnx%2B4Vmn7F%2B9DHY563bPw51T80oTOyH7%2FtjiFnjb4p2JFnSKswqzXzaOrxbIrY966N%2FH30sEEI1CnONJTRrwERH7oO9o2TFpAao6YExUn1GJwHdf%2FnadcQpsWNxPBRY9OCNYuQSFxMSAtmvsNY1haimREMYz9tCYQou1HM52F1DxWHqr4%2BR73EpDwxEmu3acExud%2BOuv3bCV%2Fqtiac5iMBY6HQ8hNjCM7cs2%2BZ4Fqj%2BVgmGn0klIf59cDCVeYXI%2BpWe1Du0mMXBq%2BRXdF%2BTYn1VAtfu8l%2FObyJaAPYqyvHZPC4yl9xrBdOSEenmmvyYlb0dy4i1a78yR0IkspphGMMej9LwGOqUB%2B%2BQHK%2BU8a8TfVt8P4b0bR8SShU7UQmbca7qqjaGoGkW4R6aDEaH%2BiJq67eRHx5RloKPMVZNx9QLDCxmSjSjpLQnuDGRigisYLTSwFQTP6wFWJvgWPMTXTodZNoOcz48olQJqh28sNs3HinR5DDUm16OWGVXY8WqMWlrb1eUzVfl%2Bg5xT60q%2BrsPOZ2xl3omcKggCtWZfKg06RQe2vjkBgxM8eyHF&X-Amz-Signature=2807b1317a19148c6b7ffe79a5e07ee43c535a659b4cdcf0fb4f9fa938acc3c3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQVDTL3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbVWq%2F0Q10jXAfmu8c83%2FiFdNzs1H8BArf29G2dSmjWAiEA%2FROZPwMWcy335CCQKQJCZQ12Cpor1Jsrmeibzp2m12gqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiFzEq4eoz3xR%2FEWyrcA1VquYmFwao%2FZTJbqXmHY9t8FciSRJIyJffRI98nou7jFwdOHDk20wJzh19nK9ioJfMRfW0QaSD7VW4h4QH401vWYeBIpcJab5pR4dJLZW%2BDH90eZYInAkZSKkyZycbzcLjQXVQawNj9y2%2BWoRSJqi9K9Rlola0U6ZN3CMcFPqHyTFXdzEri1GOAPLvOq0IdEBiJ5O7QPHFYNLsBZn9fl9tKzTwu9pLrz6NoPg97nZSZZX7q2iAM9vsGshOzY4Akpinuwt4NxabLRuzhyWMthrZQZU8i3JMT51QT%2BFfhmnx%2B4Vmn7F%2B9DHY563bPw51T80oTOyH7%2FtjiFnjb4p2JFnSKswqzXzaOrxbIrY966N%2FH30sEEI1CnONJTRrwERH7oO9o2TFpAao6YExUn1GJwHdf%2FnadcQpsWNxPBRY9OCNYuQSFxMSAtmvsNY1haimREMYz9tCYQou1HM52F1DxWHqr4%2BR73EpDwxEmu3acExud%2BOuv3bCV%2Fqtiac5iMBY6HQ8hNjCM7cs2%2BZ4Fqj%2BVgmGn0klIf59cDCVeYXI%2BpWe1Du0mMXBq%2BRXdF%2BTYn1VAtfu8l%2FObyJaAPYqyvHZPC4yl9xrBdOSEenmmvyYlb0dy4i1a78yR0IkspphGMMej9LwGOqUB%2B%2BQHK%2BU8a8TfVt8P4b0bR8SShU7UQmbca7qqjaGoGkW4R6aDEaH%2BiJq67eRHx5RloKPMVZNx9QLDCxmSjSjpLQnuDGRigisYLTSwFQTP6wFWJvgWPMTXTodZNoOcz48olQJqh28sNs3HinR5DDUm16OWGVXY8WqMWlrb1eUzVfl%2Bg5xT60q%2BrsPOZ2xl3omcKggCtWZfKg06RQe2vjkBgxM8eyHF&X-Amz-Signature=1c90c30d156129e6d18d7ead7294b41996033293e584a041264619fece05bcab&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQVDTL3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbVWq%2F0Q10jXAfmu8c83%2FiFdNzs1H8BArf29G2dSmjWAiEA%2FROZPwMWcy335CCQKQJCZQ12Cpor1Jsrmeibzp2m12gqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiFzEq4eoz3xR%2FEWyrcA1VquYmFwao%2FZTJbqXmHY9t8FciSRJIyJffRI98nou7jFwdOHDk20wJzh19nK9ioJfMRfW0QaSD7VW4h4QH401vWYeBIpcJab5pR4dJLZW%2BDH90eZYInAkZSKkyZycbzcLjQXVQawNj9y2%2BWoRSJqi9K9Rlola0U6ZN3CMcFPqHyTFXdzEri1GOAPLvOq0IdEBiJ5O7QPHFYNLsBZn9fl9tKzTwu9pLrz6NoPg97nZSZZX7q2iAM9vsGshOzY4Akpinuwt4NxabLRuzhyWMthrZQZU8i3JMT51QT%2BFfhmnx%2B4Vmn7F%2B9DHY563bPw51T80oTOyH7%2FtjiFnjb4p2JFnSKswqzXzaOrxbIrY966N%2FH30sEEI1CnONJTRrwERH7oO9o2TFpAao6YExUn1GJwHdf%2FnadcQpsWNxPBRY9OCNYuQSFxMSAtmvsNY1haimREMYz9tCYQou1HM52F1DxWHqr4%2BR73EpDwxEmu3acExud%2BOuv3bCV%2Fqtiac5iMBY6HQ8hNjCM7cs2%2BZ4Fqj%2BVgmGn0klIf59cDCVeYXI%2BpWe1Du0mMXBq%2BRXdF%2BTYn1VAtfu8l%2FObyJaAPYqyvHZPC4yl9xrBdOSEenmmvyYlb0dy4i1a78yR0IkspphGMMej9LwGOqUB%2B%2BQHK%2BU8a8TfVt8P4b0bR8SShU7UQmbca7qqjaGoGkW4R6aDEaH%2BiJq67eRHx5RloKPMVZNx9QLDCxmSjSjpLQnuDGRigisYLTSwFQTP6wFWJvgWPMTXTodZNoOcz48olQJqh28sNs3HinR5DDUm16OWGVXY8WqMWlrb1eUzVfl%2Bg5xT60q%2BrsPOZ2xl3omcKggCtWZfKg06RQe2vjkBgxM8eyHF&X-Amz-Signature=ee5223e27c9b54d1fa0c9ceee80de91e9ce240439574a82240539d4d9f13131b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQVDTL3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbVWq%2F0Q10jXAfmu8c83%2FiFdNzs1H8BArf29G2dSmjWAiEA%2FROZPwMWcy335CCQKQJCZQ12Cpor1Jsrmeibzp2m12gqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiFzEq4eoz3xR%2FEWyrcA1VquYmFwao%2FZTJbqXmHY9t8FciSRJIyJffRI98nou7jFwdOHDk20wJzh19nK9ioJfMRfW0QaSD7VW4h4QH401vWYeBIpcJab5pR4dJLZW%2BDH90eZYInAkZSKkyZycbzcLjQXVQawNj9y2%2BWoRSJqi9K9Rlola0U6ZN3CMcFPqHyTFXdzEri1GOAPLvOq0IdEBiJ5O7QPHFYNLsBZn9fl9tKzTwu9pLrz6NoPg97nZSZZX7q2iAM9vsGshOzY4Akpinuwt4NxabLRuzhyWMthrZQZU8i3JMT51QT%2BFfhmnx%2B4Vmn7F%2B9DHY563bPw51T80oTOyH7%2FtjiFnjb4p2JFnSKswqzXzaOrxbIrY966N%2FH30sEEI1CnONJTRrwERH7oO9o2TFpAao6YExUn1GJwHdf%2FnadcQpsWNxPBRY9OCNYuQSFxMSAtmvsNY1haimREMYz9tCYQou1HM52F1DxWHqr4%2BR73EpDwxEmu3acExud%2BOuv3bCV%2Fqtiac5iMBY6HQ8hNjCM7cs2%2BZ4Fqj%2BVgmGn0klIf59cDCVeYXI%2BpWe1Du0mMXBq%2BRXdF%2BTYn1VAtfu8l%2FObyJaAPYqyvHZPC4yl9xrBdOSEenmmvyYlb0dy4i1a78yR0IkspphGMMej9LwGOqUB%2B%2BQHK%2BU8a8TfVt8P4b0bR8SShU7UQmbca7qqjaGoGkW4R6aDEaH%2BiJq67eRHx5RloKPMVZNx9QLDCxmSjSjpLQnuDGRigisYLTSwFQTP6wFWJvgWPMTXTodZNoOcz48olQJqh28sNs3HinR5DDUm16OWGVXY8WqMWlrb1eUzVfl%2Bg5xT60q%2BrsPOZ2xl3omcKggCtWZfKg06RQe2vjkBgxM8eyHF&X-Amz-Signature=626a9ddf61439814e3de5c496452a17aa0f3c1e67133ffab81ddbe6ee27aa9db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQVDTL3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbVWq%2F0Q10jXAfmu8c83%2FiFdNzs1H8BArf29G2dSmjWAiEA%2FROZPwMWcy335CCQKQJCZQ12Cpor1Jsrmeibzp2m12gqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiFzEq4eoz3xR%2FEWyrcA1VquYmFwao%2FZTJbqXmHY9t8FciSRJIyJffRI98nou7jFwdOHDk20wJzh19nK9ioJfMRfW0QaSD7VW4h4QH401vWYeBIpcJab5pR4dJLZW%2BDH90eZYInAkZSKkyZycbzcLjQXVQawNj9y2%2BWoRSJqi9K9Rlola0U6ZN3CMcFPqHyTFXdzEri1GOAPLvOq0IdEBiJ5O7QPHFYNLsBZn9fl9tKzTwu9pLrz6NoPg97nZSZZX7q2iAM9vsGshOzY4Akpinuwt4NxabLRuzhyWMthrZQZU8i3JMT51QT%2BFfhmnx%2B4Vmn7F%2B9DHY563bPw51T80oTOyH7%2FtjiFnjb4p2JFnSKswqzXzaOrxbIrY966N%2FH30sEEI1CnONJTRrwERH7oO9o2TFpAao6YExUn1GJwHdf%2FnadcQpsWNxPBRY9OCNYuQSFxMSAtmvsNY1haimREMYz9tCYQou1HM52F1DxWHqr4%2BR73EpDwxEmu3acExud%2BOuv3bCV%2Fqtiac5iMBY6HQ8hNjCM7cs2%2BZ4Fqj%2BVgmGn0klIf59cDCVeYXI%2BpWe1Du0mMXBq%2BRXdF%2BTYn1VAtfu8l%2FObyJaAPYqyvHZPC4yl9xrBdOSEenmmvyYlb0dy4i1a78yR0IkspphGMMej9LwGOqUB%2B%2BQHK%2BU8a8TfVt8P4b0bR8SShU7UQmbca7qqjaGoGkW4R6aDEaH%2BiJq67eRHx5RloKPMVZNx9QLDCxmSjSjpLQnuDGRigisYLTSwFQTP6wFWJvgWPMTXTodZNoOcz48olQJqh28sNs3HinR5DDUm16OWGVXY8WqMWlrb1eUzVfl%2Bg5xT60q%2BrsPOZ2xl3omcKggCtWZfKg06RQe2vjkBgxM8eyHF&X-Amz-Signature=3c71455b3c1dfeb3e262a10a2133c7aace593702cebab1e96053fd53e2a22b97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQVDTL3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbVWq%2F0Q10jXAfmu8c83%2FiFdNzs1H8BArf29G2dSmjWAiEA%2FROZPwMWcy335CCQKQJCZQ12Cpor1Jsrmeibzp2m12gqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiFzEq4eoz3xR%2FEWyrcA1VquYmFwao%2FZTJbqXmHY9t8FciSRJIyJffRI98nou7jFwdOHDk20wJzh19nK9ioJfMRfW0QaSD7VW4h4QH401vWYeBIpcJab5pR4dJLZW%2BDH90eZYInAkZSKkyZycbzcLjQXVQawNj9y2%2BWoRSJqi9K9Rlola0U6ZN3CMcFPqHyTFXdzEri1GOAPLvOq0IdEBiJ5O7QPHFYNLsBZn9fl9tKzTwu9pLrz6NoPg97nZSZZX7q2iAM9vsGshOzY4Akpinuwt4NxabLRuzhyWMthrZQZU8i3JMT51QT%2BFfhmnx%2B4Vmn7F%2B9DHY563bPw51T80oTOyH7%2FtjiFnjb4p2JFnSKswqzXzaOrxbIrY966N%2FH30sEEI1CnONJTRrwERH7oO9o2TFpAao6YExUn1GJwHdf%2FnadcQpsWNxPBRY9OCNYuQSFxMSAtmvsNY1haimREMYz9tCYQou1HM52F1DxWHqr4%2BR73EpDwxEmu3acExud%2BOuv3bCV%2Fqtiac5iMBY6HQ8hNjCM7cs2%2BZ4Fqj%2BVgmGn0klIf59cDCVeYXI%2BpWe1Du0mMXBq%2BRXdF%2BTYn1VAtfu8l%2FObyJaAPYqyvHZPC4yl9xrBdOSEenmmvyYlb0dy4i1a78yR0IkspphGMMej9LwGOqUB%2B%2BQHK%2BU8a8TfVt8P4b0bR8SShU7UQmbca7qqjaGoGkW4R6aDEaH%2BiJq67eRHx5RloKPMVZNx9QLDCxmSjSjpLQnuDGRigisYLTSwFQTP6wFWJvgWPMTXTodZNoOcz48olQJqh28sNs3HinR5DDUm16OWGVXY8WqMWlrb1eUzVfl%2Bg5xT60q%2BrsPOZ2xl3omcKggCtWZfKg06RQe2vjkBgxM8eyHF&X-Amz-Signature=8a91d99c5e7e9c636068782399957225e29dd9a98f9ea6e7ab93407b2b671af7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROJCK3D6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDV%2FZcEJpuyHQRAYOxLlj1A5ZoLTupmMFtOVG8H6NAcSQIhALvsV59TJMnE0%2BsKIf%2Bj6qqDPcH0KFCYqvg1bvND80K2KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqbYJZoWVVYUDBmpEq3AOYwxAHTLQ8LhvW7xy6ulSppqIujcC6fLh144rdsL8dIJgc822qyRpl4%2FD1sLOAtX7nzUuRvxZHuUZxu3tRojm8tMrZJgbFO%2Bc9JLwG8ykiXGv9uDQ%2BBIddjkcU%2FC7htZhGyLub2QCgsZLFKQgOV0lUV6W5zVPUcRusJnW0caBHFpgNdLtYDtRVTWmtFBG02WhQkwcKrT6%2F8iiTfhpiCfQA%2BnDL5mAURE5V%2FTP1PhC6FFgDKGDiHxMeoZTsMqUanJBqqagGb1aUkRnqF1eoRnrQNRUDwKR9KfT9lMT%2FeCcqzeOBCV%2BYX%2F%2FszEWSwVa59baD%2FQjuraJ17H2FK3n41loM%2BAZkazSjAHk4xbmB9oUiQtqr9eYbGUTBMUCkY7jNoHT9uqbBjg0qcup2bkszfhxf9TJeY%2BFXhcMDbKc3grVOe1H4h3e8TnJs7FSij8oGv8WFc4nvUUHOAOPYM6jHw0yfO8qWPVx3nxO%2B04ij5rNjR0eRWX1w0A%2BA%2BlscyP4%2FuGr5d1%2FqyIftHQRSDvknBd1exMgKK8o1TXXn02OxmQHSjf8Y8l7%2BVej9iycoEUyU07cs82P9hfcG0f1znKBx6GvRRQizgGC%2BXP29F1QVxkSPfDz0Pi3OrzuH%2BxMmnjD7o%2FS8BjqkAasY4iNQiM5DyEHzc%2F891kG0xabBrlJGzbHAP%2FkY4mLc%2Bpg6LqyR3c%2B%2FhXPSvezpXLd%2FsCCp2Kd%2FdXpPIGhSv%2F3pqfSqPbgaVIhKXyUFrxqRFKfvbju3r80DYsTsXFrAVelZsYcK6P3cMiQtYJ4xe7lUC3KvT7wkOlA0HEAAknhXZVMGapl%2BdZfW1TjjwkXkC%2BpYdICY8CaarzzSB89csFVPlSlY&X-Amz-Signature=a2a94b35c2b2e83642a6692e7b1665b1e7997dfa6e644862e260fc60fa8cd880&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZBKHPJK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDwnCwBfPTT%2FYb3ji8gsXcgoQeRgBeGsBceaQGvHEawtAiEA3rXlhIyIYC8ivgBjfVsZEOiAw6TfMpC56p2L%2BX0%2FMxEqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbY3srbzcbrCFpBEyrcA%2BPqW6a%2FdodosCeSUSj9QL6McQ7hrcz3p2VZiKMUB7raAdOYhafiK6vzLkx1DIJcPNkDfKoRKQL9oJaRi8sbRBQy5SIiVRMAixdiOFeixnNWripdoMzT3UJWVIc%2Fux%2Bmnrmon2N48Yp5YgSjBjtJ2Uarf7sYMg1s%2FU8p%2F0Yvu%2Baq%2FXv3XY4hjVUKDe1UplOXPm4c7bNL8TqS33m8TVtRuo%2FMc1iGETH1z6mPqLfOOJN3NR4DX2FxrZzZmHw5dHZwEij05DW0XxhWEZyih%2B%2BrVgtdPNB8q71HCXkDei5Sm0TtFP%2Fa7UUWJWtBOlCoR4JO369tURZ7ywieR3b%2BChvJGgUYHLcH8v77DV8bTJgzxzWgSn4GRK3ZDxczuOw7U4fq12HwoboWaJQ81poCDxM4YgfD2DcY5VinlL4uTr1SN4pAYModeRRwcx4wWUDdsREzESoBYLPStF%2Bmfm1U28vm9g7qWgj%2B9tGVbDtWHxZzRbn53tmwwo8GBLsfdYlheExIb4EX6NVGfj%2B9GikKx93zr9fpsXksrDwoTm09gyPmEtRUhHkJWR31Jiutds4H6WPuFUbYQ0LxvijrPjPzMyhi7SBd5Romu0qhtECQ%2FXYFl794LdgALhSMtHS%2Fk3oBMIik9LwGOqUBfwPwWhnNriQAy742hYHqDq6F3cEsESla1CkS%2FiMOyERFAyeBkhQTuJK95H8J%2Fb0FJLDEDHFEodStV4USLVXGv%2FwMC%2B1OdA%2FmVoXqyfphIfUvowqAwrEKOutNbLo3lScQSOXAcQaHqzUavqbGzJhDHJbw7Pm%2FY1RfRHLQ98oNv0pOq6FlqzYYQaOYo4CbSjKnurBkOR%2FYtex6r%2FdEuvMlfQ1Biudd&X-Amz-Signature=ebd958cd7f0c3d02593320f785293c45079511b0ca3c20dd960b2d58f0906e34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQVDTL3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbVWq%2F0Q10jXAfmu8c83%2FiFdNzs1H8BArf29G2dSmjWAiEA%2FROZPwMWcy335CCQKQJCZQ12Cpor1Jsrmeibzp2m12gqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiFzEq4eoz3xR%2FEWyrcA1VquYmFwao%2FZTJbqXmHY9t8FciSRJIyJffRI98nou7jFwdOHDk20wJzh19nK9ioJfMRfW0QaSD7VW4h4QH401vWYeBIpcJab5pR4dJLZW%2BDH90eZYInAkZSKkyZycbzcLjQXVQawNj9y2%2BWoRSJqi9K9Rlola0U6ZN3CMcFPqHyTFXdzEri1GOAPLvOq0IdEBiJ5O7QPHFYNLsBZn9fl9tKzTwu9pLrz6NoPg97nZSZZX7q2iAM9vsGshOzY4Akpinuwt4NxabLRuzhyWMthrZQZU8i3JMT51QT%2BFfhmnx%2B4Vmn7F%2B9DHY563bPw51T80oTOyH7%2FtjiFnjb4p2JFnSKswqzXzaOrxbIrY966N%2FH30sEEI1CnONJTRrwERH7oO9o2TFpAao6YExUn1GJwHdf%2FnadcQpsWNxPBRY9OCNYuQSFxMSAtmvsNY1haimREMYz9tCYQou1HM52F1DxWHqr4%2BR73EpDwxEmu3acExud%2BOuv3bCV%2Fqtiac5iMBY6HQ8hNjCM7cs2%2BZ4Fqj%2BVgmGn0klIf59cDCVeYXI%2BpWe1Du0mMXBq%2BRXdF%2BTYn1VAtfu8l%2FObyJaAPYqyvHZPC4yl9xrBdOSEenmmvyYlb0dy4i1a78yR0IkspphGMMej9LwGOqUB%2B%2BQHK%2BU8a8TfVt8P4b0bR8SShU7UQmbca7qqjaGoGkW4R6aDEaH%2BiJq67eRHx5RloKPMVZNx9QLDCxmSjSjpLQnuDGRigisYLTSwFQTP6wFWJvgWPMTXTodZNoOcz48olQJqh28sNs3HinR5DDUm16OWGVXY8WqMWlrb1eUzVfl%2Bg5xT60q%2BrsPOZ2xl3omcKggCtWZfKg06RQe2vjkBgxM8eyHF&X-Amz-Signature=9d76cc8adbaf675f7e965f70d4b74c22f25304c736d56f56b9b7d5b7e9955692&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQVDTL3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbVWq%2F0Q10jXAfmu8c83%2FiFdNzs1H8BArf29G2dSmjWAiEA%2FROZPwMWcy335CCQKQJCZQ12Cpor1Jsrmeibzp2m12gqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiFzEq4eoz3xR%2FEWyrcA1VquYmFwao%2FZTJbqXmHY9t8FciSRJIyJffRI98nou7jFwdOHDk20wJzh19nK9ioJfMRfW0QaSD7VW4h4QH401vWYeBIpcJab5pR4dJLZW%2BDH90eZYInAkZSKkyZycbzcLjQXVQawNj9y2%2BWoRSJqi9K9Rlola0U6ZN3CMcFPqHyTFXdzEri1GOAPLvOq0IdEBiJ5O7QPHFYNLsBZn9fl9tKzTwu9pLrz6NoPg97nZSZZX7q2iAM9vsGshOzY4Akpinuwt4NxabLRuzhyWMthrZQZU8i3JMT51QT%2BFfhmnx%2B4Vmn7F%2B9DHY563bPw51T80oTOyH7%2FtjiFnjb4p2JFnSKswqzXzaOrxbIrY966N%2FH30sEEI1CnONJTRrwERH7oO9o2TFpAao6YExUn1GJwHdf%2FnadcQpsWNxPBRY9OCNYuQSFxMSAtmvsNY1haimREMYz9tCYQou1HM52F1DxWHqr4%2BR73EpDwxEmu3acExud%2BOuv3bCV%2Fqtiac5iMBY6HQ8hNjCM7cs2%2BZ4Fqj%2BVgmGn0klIf59cDCVeYXI%2BpWe1Du0mMXBq%2BRXdF%2BTYn1VAtfu8l%2FObyJaAPYqyvHZPC4yl9xrBdOSEenmmvyYlb0dy4i1a78yR0IkspphGMMej9LwGOqUB%2B%2BQHK%2BU8a8TfVt8P4b0bR8SShU7UQmbca7qqjaGoGkW4R6aDEaH%2BiJq67eRHx5RloKPMVZNx9QLDCxmSjSjpLQnuDGRigisYLTSwFQTP6wFWJvgWPMTXTodZNoOcz48olQJqh28sNs3HinR5DDUm16OWGVXY8WqMWlrb1eUzVfl%2Bg5xT60q%2BrsPOZ2xl3omcKggCtWZfKg06RQe2vjkBgxM8eyHF&X-Amz-Signature=404ec5b0d0e216c393d46d810370a4194c8684451833515152bda8353ca77912&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQVDTL3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbVWq%2F0Q10jXAfmu8c83%2FiFdNzs1H8BArf29G2dSmjWAiEA%2FROZPwMWcy335CCQKQJCZQ12Cpor1Jsrmeibzp2m12gqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiFzEq4eoz3xR%2FEWyrcA1VquYmFwao%2FZTJbqXmHY9t8FciSRJIyJffRI98nou7jFwdOHDk20wJzh19nK9ioJfMRfW0QaSD7VW4h4QH401vWYeBIpcJab5pR4dJLZW%2BDH90eZYInAkZSKkyZycbzcLjQXVQawNj9y2%2BWoRSJqi9K9Rlola0U6ZN3CMcFPqHyTFXdzEri1GOAPLvOq0IdEBiJ5O7QPHFYNLsBZn9fl9tKzTwu9pLrz6NoPg97nZSZZX7q2iAM9vsGshOzY4Akpinuwt4NxabLRuzhyWMthrZQZU8i3JMT51QT%2BFfhmnx%2B4Vmn7F%2B9DHY563bPw51T80oTOyH7%2FtjiFnjb4p2JFnSKswqzXzaOrxbIrY966N%2FH30sEEI1CnONJTRrwERH7oO9o2TFpAao6YExUn1GJwHdf%2FnadcQpsWNxPBRY9OCNYuQSFxMSAtmvsNY1haimREMYz9tCYQou1HM52F1DxWHqr4%2BR73EpDwxEmu3acExud%2BOuv3bCV%2Fqtiac5iMBY6HQ8hNjCM7cs2%2BZ4Fqj%2BVgmGn0klIf59cDCVeYXI%2BpWe1Du0mMXBq%2BRXdF%2BTYn1VAtfu8l%2FObyJaAPYqyvHZPC4yl9xrBdOSEenmmvyYlb0dy4i1a78yR0IkspphGMMej9LwGOqUB%2B%2BQHK%2BU8a8TfVt8P4b0bR8SShU7UQmbca7qqjaGoGkW4R6aDEaH%2BiJq67eRHx5RloKPMVZNx9QLDCxmSjSjpLQnuDGRigisYLTSwFQTP6wFWJvgWPMTXTodZNoOcz48olQJqh28sNs3HinR5DDUm16OWGVXY8WqMWlrb1eUzVfl%2Bg5xT60q%2BrsPOZ2xl3omcKggCtWZfKg06RQe2vjkBgxM8eyHF&X-Amz-Signature=4d175c2802ec9b77198d2a29d244fbacaf49101f6d368e8d58b697b0cf94ed4e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652QESZ77%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCd4WaxjVxYSJxhgl%2F2QJQfBSrVPLQmp7O4hxApc2d7gwIgStkTgcOGspp5a2BIcPTg9UVwhznzy2VMg7Mr%2BPHBdY4qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOIllMqPidn6P9vHircA6sdWesX7m0PgpqmS1SPXRfwcMzHPLQzfkc%2BA7C25G8eJKX7%2FMfz8ZERvNexwBwyjsMmcVzOvGJbhqKm8Rhr8c71d5AKwTOjiroHFijS3hhrwLTJwkrewDnJwXSSVn94TECKppC2Bn5fQE%2BijEYPahFgLE928JNQe6nVZWCTwEwWiXF27fRmTL8fLCnTIUsVzSae4oSTIZETQEi5u5Qh1hwLa3kJrspRWgWE5e4%2F2O96L0gnK0wV%2FVrjfSSI1U94wiuYmSQXbMAmBEOh%2BIbQ2YrwaaI1veXOvOoX6W%2F93KukfVj9yseHe2HL9uQGVNrzfjs6Wut7bSLxl3Jt9f9Vk0IpoYuDsrqZ5ocT%2BhxHa4i%2F7vKPj9%2Bc4BbHMj2oWVxQhAlCvjoBl28qJpHQ%2Bd7%2BRa1ePqGM3ifg6eRDrxjRDQrgDxS5z2KyDiPbd0ptLHlOqvo9EKaxElnfjzB2vXUAeJIiw9kvkVJhoQXXQlrR8RvB73KueIh9tzmJuAVsYU0XXM64NlnKgFtfU8NV286l4bLQsEo%2BIh7nIrAfewcvu2NANhE%2FXDUdwffbJ3xZ7z6V3jzt8Ngh0b11CfGuQSD6WxQi6E01p5RjHb154XXb%2Fg9llBBy5bh4SicLfSegMM%2Bj9LwGOqUBbPV1dzEAx2ztSbjz0pZ%2FhVH9%2FMNnjtt5eZHnbwHfvOZCSpGQJv2hN%2BuDAf8dG9Lb72eq4mBp5KdJm07%2F56L18MfNRpppUsYcjV6wm5PFguBEOUr3kxO9z6Ji1KzBaWVSQZBZK3T2FTt8Z8Abmuz1mJWRDMQBA1A%2B7dZ9X%2FPcuzkX2uAUqHpwAQHwThDzUSBb2SySCsnE6JpOARfvDmeDc2G5790Q&X-Amz-Signature=b84d0ad7913cc2ea9b9e79b8ecac9016c8afb7cf254217b02a48fb9eb9c11973&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ6BNSLN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCf04qm%2BZb1n6aNunZdCIAQvUJvlrj%2FM9PNdXpVUlEu4AIhAPJTV2vkitWUi6M3lPXs%2BELic4nkbr%2FjNzSKPXQs0UMEKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGfjHf7YEOlNiHXA4q3AM0YjBQKiz3EQ1fAbKhDdeCpUFISGXg38zQ4G506Gc7tozl8Jkiu%2BqU7J8eTGObymBQZs%2FkNgq3b7%2Fvqnb2D2EhSBgE%2By9m3P9b3BsruEzIz6ddXq6H5sl%2FcmmR4kWJnAG9j6IVAOMhLfXAx7%2FmGd6dybW6idZ2fdXt2umn7gTn2klbFZXZOxWD03lticNnDYYRxUxNC3AaR6H74CXJHdtUHzGh3%2FdAbFJQPE5pdrtNinkZjWVMzkDKB2xt2Qn4Sq8jcbt3PNOtpHzPKesqLeVMIKC5U36J2kIYncnQROToeA938HQbfOqfKhTOO4mXbJ7JvauVAni2sL6NKoNIJ2D5EHpNXH6jvtaL2S2qgadH2qpXr66onsMoRtLRZgg4ewqD9Gmxi%2BOPKYGavUxXaluW9d32GfK364b1Xd0WwCgwO0iAfbj1%2Bh4ESrvnXP5Eq2eZuXonz1XUZLnpnEhQK88S6zErUwXBgSMfAyf%2Fky%2BgiL4fzcyjbPQruu5zPmIfiEBihnp9DJlSDauaNlk45BwqXMnifLIYojTLOq4xv%2FlCe%2BlRYz08R1EGi8M2Q3FqlBpNCFlgrbCaI9C4vzytdfkjPKIMZfSHBrJmCe1NKS8wkRLe8nlz7FuGT5taQjCIpPS8BjqkAd2GheuBNptJidnHQPld8mKi2JV%2FXC%2FpbdzLjItsgNUaqovlU0A5fsCDnuwpZl0WtZDXBpYR0qSg6%2F0Unnr7A7t9%2FMaJ0eoXJfmGl0WLP0utAZpYUUylXUB1Z4tZ3tsdVtU5ZMtYLzweOA1SXwGrzl8IKIlfN22UJaP00PQPbFs6WDoyYaIszzSzxtqzv0ePqIUwKxnJsVjjeQuDLe%2BpEcRCnvUe&X-Amz-Signature=30985da4cbaf2e1ca8bb2a1726953103805b3ba7d4c72c99d6dc72b10de04f4b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XCGZGRO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwCG2ki51PrbIyrVao5al3kSSEJh6PsWFCJabu9OnXTgIgfeWmgyGVd8gEvuKTrx2PcFTm3oqgw6Yf4jS8cEgjtCMqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDgtbK0Yb2jZrN8cvSrcA%2FbTkY6PEraERhG8RP6ZX7IV9Ewp8OvT2JUIM%2BzcybrXExTkXmA5aMsacxMNjkDCzsKgZXUDIWMWUVeuYpn0I%2FC1z3CW%2BuwIx%2FGI7gZnvkYq87wJ4BotGkwC%2BcR49Judiu6bASEXVRP6zuNn1Azr3huDpFXjuxctPllF7BbeAkOQvb%2FP%2BjKEqixE6VQs%2BOeaWbgqmX%2FOsPASS84oHS6kdkZxNClzk%2BIvWwTGpLXh%2B%2BcSHon81ZV24ADpYMPeOsukkw4G98dGOhPTSSjXL2HjDZFIiNTev%2B%2BunlFw%2Fk%2Fsm%2B%2BHDQB0SJhHlEV4SNW1tn%2FLq57xmCu3JTQHKsfIo5YhYZxGgg4knVYhDVdmk3IddVQrrQGGgUYbLjOFToK4gd0H14t9KniNK%2Bn8p9gQs0ydtVqFO3TzLL8l3F%2BmR%2FtobrrHokP9XiIjwExUXQ7O3guQrvwgQQv%2FdskHyTyVYtCzcXYFlCRLJCzJexyXKfOeXdnwkGSPkAur0AVIUszaGIQsPlQgFGHGnq9i3SZOV1c8OnUUERNlxSy6cw1SB85G6gZcSwfGS1x1IJbXmzCbcu2FAEQx5m20G7iqOXS5RMFM2HMMW%2FmiVmsf2MM7M5vANIFXbUDNCEdX7gBkVugTMNyj9LwGOqUBUe5KXiPuxtM1Nfk0dBPG5C%2FfDfvenq9i7mOmDa2%2BcZ0wqC4ywazSYJwnThbFxOCqf4pbh8kI3oCpBWToOB6PX3Yvu8BQao4Sg4kUqE0NLYiXAglR6kiaUttTAufn7ElgRbNDcbXNqF%2BbM6yO%2Bgoz8mU%2Bmi35Z2oX9OYPj8WdEGtCCkpH8yfeX4lUcHuFUgmvLYoA2ymLvP2pOsUQVuQEsx5tcH1J&X-Amz-Signature=a3766d074e430f24d8990a98f5fd098555ab93f013e4ea609097f63bdbb7c1fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663BABJZQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCheflW8GUa2S2pBLJ7T36YLztuWI0dEFitLG3iIUIBBwIgB3ayWIPVTIdJINfr6Im5whFWdxvgg8d4t1KSuumVLVYqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDYdDRXeU0Q%2BPsRWiSrcA5G1TbpgVnyPfsnij6wOFIUM6qhw94%2B%2FWouoHJ0qiaKuLMdDeIg2%2F7qXKrPxLMN7W1Ohpksw%2B9M6pU0gAGeuZP55UpL1nzAWsN2uvGbNVTApxDmvp%2BbbWDa4ZS%2BYScvGJqs4LCRjd5FBZDRzPCr%2FvMI7G%2FgGJ0k0iqFJrYWLVdQwXC4zXojx0wk1S3cu2c8ncdt%2F5RDo8psBaBSaDr9OrRn1wWor0MJjkUm2wXN%2B9zb6Hs1wYaISm%2FpZciPTX5BZrVsyrtdP1wYCQJNYF7M6Vn8bsjV9Ncu4BHTGg4P%2FjdBk%2B8Vu5TCO1jXMeVa7LcmIOSZ6WwNeKUjSNfX7S6fX0koOE3k6%2BKxSag9YjUNIAbS1PkWWD8QEbwmfcTXR4rCKqTgWA3fp7%2FlKeO1feSAKmQMTs6McwQZPR808nBxdRWqKbWmpZE0nQBf8KWGleUwLrWCOmRc4ev0OJDhQ%2BjH4tpm4pjjQAilbIUBgvXXrWKF35UmScHKT%2BtEWkztQ%2Bq57Z7W4xiuyx03Gnic6H6iTlj4Zbv0jdlEVkRn%2BL%2FvsQwHXJAaD%2FMr7sod0FpvICngV6WeAZSTjUb%2BUWm7kjP3plJn4%2BCr%2F2tK5XburqdYqgBQaATmuRV0c%2BSZsUs0KMO6j9LwGOqUBBE56EExSmxw2dGTatKpBqZQh6DF82XG2PmRZaKd8CegFJT0%2BLr8xgO%2B8oRuBjOvJQAbdq7js0OaUCXJzreEHxc6vYF2Fa41GKgesL7VPbjSFtcHoVH3jgHjrJjvpa%2FGu6GT8fPa4HBo4R%2BJ53IcGpIIcK7Hl0LwmBDn6R54YsRUinGKsMwOnkJxcJc%2BHIGkDAqewW0KMR%2BssWKDUEnyADqhZS%2Bgx&X-Amz-Signature=1efc14cbc0beb72466025681601995af114030f241f4c7f0f5e435d27013f13c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663BABJZQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCheflW8GUa2S2pBLJ7T36YLztuWI0dEFitLG3iIUIBBwIgB3ayWIPVTIdJINfr6Im5whFWdxvgg8d4t1KSuumVLVYqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDYdDRXeU0Q%2BPsRWiSrcA5G1TbpgVnyPfsnij6wOFIUM6qhw94%2B%2FWouoHJ0qiaKuLMdDeIg2%2F7qXKrPxLMN7W1Ohpksw%2B9M6pU0gAGeuZP55UpL1nzAWsN2uvGbNVTApxDmvp%2BbbWDa4ZS%2BYScvGJqs4LCRjd5FBZDRzPCr%2FvMI7G%2FgGJ0k0iqFJrYWLVdQwXC4zXojx0wk1S3cu2c8ncdt%2F5RDo8psBaBSaDr9OrRn1wWor0MJjkUm2wXN%2B9zb6Hs1wYaISm%2FpZciPTX5BZrVsyrtdP1wYCQJNYF7M6Vn8bsjV9Ncu4BHTGg4P%2FjdBk%2B8Vu5TCO1jXMeVa7LcmIOSZ6WwNeKUjSNfX7S6fX0koOE3k6%2BKxSag9YjUNIAbS1PkWWD8QEbwmfcTXR4rCKqTgWA3fp7%2FlKeO1feSAKmQMTs6McwQZPR808nBxdRWqKbWmpZE0nQBf8KWGleUwLrWCOmRc4ev0OJDhQ%2BjH4tpm4pjjQAilbIUBgvXXrWKF35UmScHKT%2BtEWkztQ%2Bq57Z7W4xiuyx03Gnic6H6iTlj4Zbv0jdlEVkRn%2BL%2FvsQwHXJAaD%2FMr7sod0FpvICngV6WeAZSTjUb%2BUWm7kjP3plJn4%2BCr%2F2tK5XburqdYqgBQaATmuRV0c%2BSZsUs0KMO6j9LwGOqUBBE56EExSmxw2dGTatKpBqZQh6DF82XG2PmRZaKd8CegFJT0%2BLr8xgO%2B8oRuBjOvJQAbdq7js0OaUCXJzreEHxc6vYF2Fa41GKgesL7VPbjSFtcHoVH3jgHjrJjvpa%2FGu6GT8fPa4HBo4R%2BJ53IcGpIIcK7Hl0LwmBDn6R54YsRUinGKsMwOnkJxcJc%2BHIGkDAqewW0KMR%2BssWKDUEnyADqhZS%2Bgx&X-Amz-Signature=41901b723bfde0dee01f407e621ac24bac5e68cf8c00b7509eb9b43650f26404&X-Amz-SignedHeaders=host&x-id=GetObject)

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
