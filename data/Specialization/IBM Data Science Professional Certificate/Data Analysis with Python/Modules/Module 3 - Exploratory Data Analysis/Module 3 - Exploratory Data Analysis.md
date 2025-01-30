

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLX44FKR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0A2ISLYQfKm4NWiisLVCqKu6dj2pKENTxZGedKYMl2wIhAI2WpoBkZCiB2aEQyK4ofk5vo9ERhHuRL%2BOJ634BXTwCKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzPPtDjA7z4HuF4Decq3AMTzWx%2BWgVU9NVlyqUCW35gp4ZkUIs%2Fb4GIckCzZ44j1mpCLMW0I2PU6fIjiidUX9ullnRm8k1o40UYs0ZfU7%2F45URfv3Qve8%2FaCfe%2BZkVOWX7pj9bn1bIj9mMGcal3Rh7c1kYCE7YDoHtKld5FQqoQBkSiYBPCHfF7MvuI%2FvwaPUVHSyi2ulBHfo34ma6CJqG9jApC4li880Oj9C%2BRKPY2vN%2Bx1lIxCJSIP8P2YKwRu3sPQgGrWb0EtIdjVFkee6duS%2FPeWi79jMmEk5fGM6AhKZG8GhCxSdqrErz5UQZTvhiqZaBRa%2BQn9uCY91%2BA4ThMCc5h%2F9NCEV%2BmQvJ67kIkNnV4BfLHKVPW0JOqaUgeLrGWcBVcWBvLaz2qgo09tC1O2Mr6jVr4NxBIhUE77%2B5uWq%2FYxJI1C%2BYwNezJ958sJei5CqhBBc9d%2FheI6BUgi%2FBgCN9YGZ6UY1rZnWCs2c8cS0vHRiz077TEqwdKFreDuKSuiwLG7ID%2B0nltXyHJSaNcY032MdhPsbnyIwfs0t8BGzkIYVIxaQ3ixq3ch1GeSD4jidJ7VXt1dAPGo0C%2FdoQ%2FUeYG%2BaOygXPprvlT%2BA6GFxlGTLZU0SWuTgkOkHKYGp85T4Srtw7666H8aTDVje%2B8BjqkAYFNyulgd%2Fumjj04oFPo17iQXhc6EbAWE46Z%2FxgnYSVRwia0fHqmfcj7ML4plQtOKM7PQSr6FKhTDTqjczEfRr0uHwjvYPsA1mC117wscgtK%2BEc5md9Rdv5LezImZWFy2Vjv1NIZe73gJ%2FVgRqcXb0uxo3DBSyTgXGI%2BA0%2FLMJEXfPWiCcaRmNM8jdeQKHvOk13pdch0c2uZP7mUVA7wYPQF4K8q&X-Amz-Signature=2d8d56d4e2deff73f94382f6e22e0053ea41dfda3351e3ad1b78231fb4945b37&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLX44FKR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0A2ISLYQfKm4NWiisLVCqKu6dj2pKENTxZGedKYMl2wIhAI2WpoBkZCiB2aEQyK4ofk5vo9ERhHuRL%2BOJ634BXTwCKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzPPtDjA7z4HuF4Decq3AMTzWx%2BWgVU9NVlyqUCW35gp4ZkUIs%2Fb4GIckCzZ44j1mpCLMW0I2PU6fIjiidUX9ullnRm8k1o40UYs0ZfU7%2F45URfv3Qve8%2FaCfe%2BZkVOWX7pj9bn1bIj9mMGcal3Rh7c1kYCE7YDoHtKld5FQqoQBkSiYBPCHfF7MvuI%2FvwaPUVHSyi2ulBHfo34ma6CJqG9jApC4li880Oj9C%2BRKPY2vN%2Bx1lIxCJSIP8P2YKwRu3sPQgGrWb0EtIdjVFkee6duS%2FPeWi79jMmEk5fGM6AhKZG8GhCxSdqrErz5UQZTvhiqZaBRa%2BQn9uCY91%2BA4ThMCc5h%2F9NCEV%2BmQvJ67kIkNnV4BfLHKVPW0JOqaUgeLrGWcBVcWBvLaz2qgo09tC1O2Mr6jVr4NxBIhUE77%2B5uWq%2FYxJI1C%2BYwNezJ958sJei5CqhBBc9d%2FheI6BUgi%2FBgCN9YGZ6UY1rZnWCs2c8cS0vHRiz077TEqwdKFreDuKSuiwLG7ID%2B0nltXyHJSaNcY032MdhPsbnyIwfs0t8BGzkIYVIxaQ3ixq3ch1GeSD4jidJ7VXt1dAPGo0C%2FdoQ%2FUeYG%2BaOygXPprvlT%2BA6GFxlGTLZU0SWuTgkOkHKYGp85T4Srtw7666H8aTDVje%2B8BjqkAYFNyulgd%2Fumjj04oFPo17iQXhc6EbAWE46Z%2FxgnYSVRwia0fHqmfcj7ML4plQtOKM7PQSr6FKhTDTqjczEfRr0uHwjvYPsA1mC117wscgtK%2BEc5md9Rdv5LezImZWFy2Vjv1NIZe73gJ%2FVgRqcXb0uxo3DBSyTgXGI%2BA0%2FLMJEXfPWiCcaRmNM8jdeQKHvOk13pdch0c2uZP7mUVA7wYPQF4K8q&X-Amz-Signature=e2f697daed7d4802e12c62894d906e1049572800170e2f4cc9cf55afd4f2a162&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLX44FKR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0A2ISLYQfKm4NWiisLVCqKu6dj2pKENTxZGedKYMl2wIhAI2WpoBkZCiB2aEQyK4ofk5vo9ERhHuRL%2BOJ634BXTwCKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzPPtDjA7z4HuF4Decq3AMTzWx%2BWgVU9NVlyqUCW35gp4ZkUIs%2Fb4GIckCzZ44j1mpCLMW0I2PU6fIjiidUX9ullnRm8k1o40UYs0ZfU7%2F45URfv3Qve8%2FaCfe%2BZkVOWX7pj9bn1bIj9mMGcal3Rh7c1kYCE7YDoHtKld5FQqoQBkSiYBPCHfF7MvuI%2FvwaPUVHSyi2ulBHfo34ma6CJqG9jApC4li880Oj9C%2BRKPY2vN%2Bx1lIxCJSIP8P2YKwRu3sPQgGrWb0EtIdjVFkee6duS%2FPeWi79jMmEk5fGM6AhKZG8GhCxSdqrErz5UQZTvhiqZaBRa%2BQn9uCY91%2BA4ThMCc5h%2F9NCEV%2BmQvJ67kIkNnV4BfLHKVPW0JOqaUgeLrGWcBVcWBvLaz2qgo09tC1O2Mr6jVr4NxBIhUE77%2B5uWq%2FYxJI1C%2BYwNezJ958sJei5CqhBBc9d%2FheI6BUgi%2FBgCN9YGZ6UY1rZnWCs2c8cS0vHRiz077TEqwdKFreDuKSuiwLG7ID%2B0nltXyHJSaNcY032MdhPsbnyIwfs0t8BGzkIYVIxaQ3ixq3ch1GeSD4jidJ7VXt1dAPGo0C%2FdoQ%2FUeYG%2BaOygXPprvlT%2BA6GFxlGTLZU0SWuTgkOkHKYGp85T4Srtw7666H8aTDVje%2B8BjqkAYFNyulgd%2Fumjj04oFPo17iQXhc6EbAWE46Z%2FxgnYSVRwia0fHqmfcj7ML4plQtOKM7PQSr6FKhTDTqjczEfRr0uHwjvYPsA1mC117wscgtK%2BEc5md9Rdv5LezImZWFy2Vjv1NIZe73gJ%2FVgRqcXb0uxo3DBSyTgXGI%2BA0%2FLMJEXfPWiCcaRmNM8jdeQKHvOk13pdch0c2uZP7mUVA7wYPQF4K8q&X-Amz-Signature=6aeb5cc7dbfd3236136c9a64bfbc27ac027853bed303f372a612f383c7ff1ac4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOX2XX3I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkOAUU9ZIHEe%2BZ%2FEvgaFmfqZ0TuQLn9zFBFURuPVXNtAiBdjW6p0zqUH%2FNwrDj5LVdP9vnYvGmQKgM61zm3%2Fhl3CyqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkUowA1V6OCB8BXt0KtwDsTyAPKxt%2FD2N611OARVzp7ZISJ63NthRVI8pHmjoCoJg5w8680Bh3V1vfVIU5hDkv9ulVsvG1GLEoMpPrORfnB6roYrGMQrHAGqgXb3CSlcxAtdl31Wz97hHy0ow1%2F2nUDk4RR3N5V0D394jhZj9MIimNl%2BME8284%2FVbSc9g6bCteZIKPc6fmEHMSQw3A3ByL%2BmZGq%2ByiWwXat22ivY0UL4JThHGStoRdrOj1sCKOVPwA8NDzebIWjsgL3F6ZqkJsPmITESftbxZn94RKesVog7RkKTeyfQXuSpFWABajNLLx4%2FaMieYJQW4uwzw0YCh%2F%2BX1RLAHTzmmJYWB4YIkUgRaFRiMWE%2BTxn%2BabyWnc%2BluZyis%2B6JeCOD5aGJFNZswBIgqSz1rWHnz6jchq06MhoXbh5XZOdo63tEthQKXt1Yk2gXFyyiegBqjArDJAEgiBJfeAS%2B3yNe1qiXVbwqe3vzNPTZwlZ50R%2FabwjKpI8gKlrw2bOOBXaI9PBYWXRtUqgvxA%2F3HIdwJ%2FhXBnR9p4I3iJd8gnx%2FOyetSDPHGeOJxR%2FPDiRG1%2BkOQiw5vyIR9z8gWqtxlinJ1bXdSOzriN7cO8QQdQHUSSYTvHcwwWFjQ2V9HxCNj0PBu2bIw3Y3vvAY6pgFlfgsV%2Bj0%2Bpno8vp1ZczfBLHUBicNkjTBb3a7LD52KKRtcqIkU%2BoqQhdhDgoA2zmmk0uXtRwnveqfXHUuGI1lRB3OG2LUW98swvOQBrTfW9toyP3ImDiJwg1tmwDGuHJ0G67OLwVrS%2BYQYK0CH4QXxRuOcakIh7r37UL2JtCBtWI8jQJm8yqhoNH0mcQh5Ip3Rkcx6X4fkD1jA54WhfFGkWcdCx8DR&X-Amz-Signature=c054fd083c191f670826015a6d1a30f454e14780dfbe83c621375572c528f7da&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOX2XX3I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkOAUU9ZIHEe%2BZ%2FEvgaFmfqZ0TuQLn9zFBFURuPVXNtAiBdjW6p0zqUH%2FNwrDj5LVdP9vnYvGmQKgM61zm3%2Fhl3CyqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkUowA1V6OCB8BXt0KtwDsTyAPKxt%2FD2N611OARVzp7ZISJ63NthRVI8pHmjoCoJg5w8680Bh3V1vfVIU5hDkv9ulVsvG1GLEoMpPrORfnB6roYrGMQrHAGqgXb3CSlcxAtdl31Wz97hHy0ow1%2F2nUDk4RR3N5V0D394jhZj9MIimNl%2BME8284%2FVbSc9g6bCteZIKPc6fmEHMSQw3A3ByL%2BmZGq%2ByiWwXat22ivY0UL4JThHGStoRdrOj1sCKOVPwA8NDzebIWjsgL3F6ZqkJsPmITESftbxZn94RKesVog7RkKTeyfQXuSpFWABajNLLx4%2FaMieYJQW4uwzw0YCh%2F%2BX1RLAHTzmmJYWB4YIkUgRaFRiMWE%2BTxn%2BabyWnc%2BluZyis%2B6JeCOD5aGJFNZswBIgqSz1rWHnz6jchq06MhoXbh5XZOdo63tEthQKXt1Yk2gXFyyiegBqjArDJAEgiBJfeAS%2B3yNe1qiXVbwqe3vzNPTZwlZ50R%2FabwjKpI8gKlrw2bOOBXaI9PBYWXRtUqgvxA%2F3HIdwJ%2FhXBnR9p4I3iJd8gnx%2FOyetSDPHGeOJxR%2FPDiRG1%2BkOQiw5vyIR9z8gWqtxlinJ1bXdSOzriN7cO8QQdQHUSSYTvHcwwWFjQ2V9HxCNj0PBu2bIw3Y3vvAY6pgFlfgsV%2Bj0%2Bpno8vp1ZczfBLHUBicNkjTBb3a7LD52KKRtcqIkU%2BoqQhdhDgoA2zmmk0uXtRwnveqfXHUuGI1lRB3OG2LUW98swvOQBrTfW9toyP3ImDiJwg1tmwDGuHJ0G67OLwVrS%2BYQYK0CH4QXxRuOcakIh7r37UL2JtCBtWI8jQJm8yqhoNH0mcQh5Ip3Rkcx6X4fkD1jA54WhfFGkWcdCx8DR&X-Amz-Signature=435e43c89dcb0cdd37f579024fc7423fb1fec69566cf4d4c77a58ac0cf1d1d56&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOX2XX3I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkOAUU9ZIHEe%2BZ%2FEvgaFmfqZ0TuQLn9zFBFURuPVXNtAiBdjW6p0zqUH%2FNwrDj5LVdP9vnYvGmQKgM61zm3%2Fhl3CyqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkUowA1V6OCB8BXt0KtwDsTyAPKxt%2FD2N611OARVzp7ZISJ63NthRVI8pHmjoCoJg5w8680Bh3V1vfVIU5hDkv9ulVsvG1GLEoMpPrORfnB6roYrGMQrHAGqgXb3CSlcxAtdl31Wz97hHy0ow1%2F2nUDk4RR3N5V0D394jhZj9MIimNl%2BME8284%2FVbSc9g6bCteZIKPc6fmEHMSQw3A3ByL%2BmZGq%2ByiWwXat22ivY0UL4JThHGStoRdrOj1sCKOVPwA8NDzebIWjsgL3F6ZqkJsPmITESftbxZn94RKesVog7RkKTeyfQXuSpFWABajNLLx4%2FaMieYJQW4uwzw0YCh%2F%2BX1RLAHTzmmJYWB4YIkUgRaFRiMWE%2BTxn%2BabyWnc%2BluZyis%2B6JeCOD5aGJFNZswBIgqSz1rWHnz6jchq06MhoXbh5XZOdo63tEthQKXt1Yk2gXFyyiegBqjArDJAEgiBJfeAS%2B3yNe1qiXVbwqe3vzNPTZwlZ50R%2FabwjKpI8gKlrw2bOOBXaI9PBYWXRtUqgvxA%2F3HIdwJ%2FhXBnR9p4I3iJd8gnx%2FOyetSDPHGeOJxR%2FPDiRG1%2BkOQiw5vyIR9z8gWqtxlinJ1bXdSOzriN7cO8QQdQHUSSYTvHcwwWFjQ2V9HxCNj0PBu2bIw3Y3vvAY6pgFlfgsV%2Bj0%2Bpno8vp1ZczfBLHUBicNkjTBb3a7LD52KKRtcqIkU%2BoqQhdhDgoA2zmmk0uXtRwnveqfXHUuGI1lRB3OG2LUW98swvOQBrTfW9toyP3ImDiJwg1tmwDGuHJ0G67OLwVrS%2BYQYK0CH4QXxRuOcakIh7r37UL2JtCBtWI8jQJm8yqhoNH0mcQh5Ip3Rkcx6X4fkD1jA54WhfFGkWcdCx8DR&X-Amz-Signature=9d69a6b675ccefc60f770ad09f094826a851e38eaa624d16f487e125e7625074&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOX2XX3I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkOAUU9ZIHEe%2BZ%2FEvgaFmfqZ0TuQLn9zFBFURuPVXNtAiBdjW6p0zqUH%2FNwrDj5LVdP9vnYvGmQKgM61zm3%2Fhl3CyqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkUowA1V6OCB8BXt0KtwDsTyAPKxt%2FD2N611OARVzp7ZISJ63NthRVI8pHmjoCoJg5w8680Bh3V1vfVIU5hDkv9ulVsvG1GLEoMpPrORfnB6roYrGMQrHAGqgXb3CSlcxAtdl31Wz97hHy0ow1%2F2nUDk4RR3N5V0D394jhZj9MIimNl%2BME8284%2FVbSc9g6bCteZIKPc6fmEHMSQw3A3ByL%2BmZGq%2ByiWwXat22ivY0UL4JThHGStoRdrOj1sCKOVPwA8NDzebIWjsgL3F6ZqkJsPmITESftbxZn94RKesVog7RkKTeyfQXuSpFWABajNLLx4%2FaMieYJQW4uwzw0YCh%2F%2BX1RLAHTzmmJYWB4YIkUgRaFRiMWE%2BTxn%2BabyWnc%2BluZyis%2B6JeCOD5aGJFNZswBIgqSz1rWHnz6jchq06MhoXbh5XZOdo63tEthQKXt1Yk2gXFyyiegBqjArDJAEgiBJfeAS%2B3yNe1qiXVbwqe3vzNPTZwlZ50R%2FabwjKpI8gKlrw2bOOBXaI9PBYWXRtUqgvxA%2F3HIdwJ%2FhXBnR9p4I3iJd8gnx%2FOyetSDPHGeOJxR%2FPDiRG1%2BkOQiw5vyIR9z8gWqtxlinJ1bXdSOzriN7cO8QQdQHUSSYTvHcwwWFjQ2V9HxCNj0PBu2bIw3Y3vvAY6pgFlfgsV%2Bj0%2Bpno8vp1ZczfBLHUBicNkjTBb3a7LD52KKRtcqIkU%2BoqQhdhDgoA2zmmk0uXtRwnveqfXHUuGI1lRB3OG2LUW98swvOQBrTfW9toyP3ImDiJwg1tmwDGuHJ0G67OLwVrS%2BYQYK0CH4QXxRuOcakIh7r37UL2JtCBtWI8jQJm8yqhoNH0mcQh5Ip3Rkcx6X4fkD1jA54WhfFGkWcdCx8DR&X-Amz-Signature=e0ba4711ab833631aaeb423a09382bf7f0727309f7a7e1fa9745bde58bd9837a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOX2XX3I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkOAUU9ZIHEe%2BZ%2FEvgaFmfqZ0TuQLn9zFBFURuPVXNtAiBdjW6p0zqUH%2FNwrDj5LVdP9vnYvGmQKgM61zm3%2Fhl3CyqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkUowA1V6OCB8BXt0KtwDsTyAPKxt%2FD2N611OARVzp7ZISJ63NthRVI8pHmjoCoJg5w8680Bh3V1vfVIU5hDkv9ulVsvG1GLEoMpPrORfnB6roYrGMQrHAGqgXb3CSlcxAtdl31Wz97hHy0ow1%2F2nUDk4RR3N5V0D394jhZj9MIimNl%2BME8284%2FVbSc9g6bCteZIKPc6fmEHMSQw3A3ByL%2BmZGq%2ByiWwXat22ivY0UL4JThHGStoRdrOj1sCKOVPwA8NDzebIWjsgL3F6ZqkJsPmITESftbxZn94RKesVog7RkKTeyfQXuSpFWABajNLLx4%2FaMieYJQW4uwzw0YCh%2F%2BX1RLAHTzmmJYWB4YIkUgRaFRiMWE%2BTxn%2BabyWnc%2BluZyis%2B6JeCOD5aGJFNZswBIgqSz1rWHnz6jchq06MhoXbh5XZOdo63tEthQKXt1Yk2gXFyyiegBqjArDJAEgiBJfeAS%2B3yNe1qiXVbwqe3vzNPTZwlZ50R%2FabwjKpI8gKlrw2bOOBXaI9PBYWXRtUqgvxA%2F3HIdwJ%2FhXBnR9p4I3iJd8gnx%2FOyetSDPHGeOJxR%2FPDiRG1%2BkOQiw5vyIR9z8gWqtxlinJ1bXdSOzriN7cO8QQdQHUSSYTvHcwwWFjQ2V9HxCNj0PBu2bIw3Y3vvAY6pgFlfgsV%2Bj0%2Bpno8vp1ZczfBLHUBicNkjTBb3a7LD52KKRtcqIkU%2BoqQhdhDgoA2zmmk0uXtRwnveqfXHUuGI1lRB3OG2LUW98swvOQBrTfW9toyP3ImDiJwg1tmwDGuHJ0G67OLwVrS%2BYQYK0CH4QXxRuOcakIh7r37UL2JtCBtWI8jQJm8yqhoNH0mcQh5Ip3Rkcx6X4fkD1jA54WhfFGkWcdCx8DR&X-Amz-Signature=047f5521a96e1458fdcad7067210b49c691de48215aa51e4a0bdba24718bce72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOX2XX3I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkOAUU9ZIHEe%2BZ%2FEvgaFmfqZ0TuQLn9zFBFURuPVXNtAiBdjW6p0zqUH%2FNwrDj5LVdP9vnYvGmQKgM61zm3%2Fhl3CyqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkUowA1V6OCB8BXt0KtwDsTyAPKxt%2FD2N611OARVzp7ZISJ63NthRVI8pHmjoCoJg5w8680Bh3V1vfVIU5hDkv9ulVsvG1GLEoMpPrORfnB6roYrGMQrHAGqgXb3CSlcxAtdl31Wz97hHy0ow1%2F2nUDk4RR3N5V0D394jhZj9MIimNl%2BME8284%2FVbSc9g6bCteZIKPc6fmEHMSQw3A3ByL%2BmZGq%2ByiWwXat22ivY0UL4JThHGStoRdrOj1sCKOVPwA8NDzebIWjsgL3F6ZqkJsPmITESftbxZn94RKesVog7RkKTeyfQXuSpFWABajNLLx4%2FaMieYJQW4uwzw0YCh%2F%2BX1RLAHTzmmJYWB4YIkUgRaFRiMWE%2BTxn%2BabyWnc%2BluZyis%2B6JeCOD5aGJFNZswBIgqSz1rWHnz6jchq06MhoXbh5XZOdo63tEthQKXt1Yk2gXFyyiegBqjArDJAEgiBJfeAS%2B3yNe1qiXVbwqe3vzNPTZwlZ50R%2FabwjKpI8gKlrw2bOOBXaI9PBYWXRtUqgvxA%2F3HIdwJ%2FhXBnR9p4I3iJd8gnx%2FOyetSDPHGeOJxR%2FPDiRG1%2BkOQiw5vyIR9z8gWqtxlinJ1bXdSOzriN7cO8QQdQHUSSYTvHcwwWFjQ2V9HxCNj0PBu2bIw3Y3vvAY6pgFlfgsV%2Bj0%2Bpno8vp1ZczfBLHUBicNkjTBb3a7LD52KKRtcqIkU%2BoqQhdhDgoA2zmmk0uXtRwnveqfXHUuGI1lRB3OG2LUW98swvOQBrTfW9toyP3ImDiJwg1tmwDGuHJ0G67OLwVrS%2BYQYK0CH4QXxRuOcakIh7r37UL2JtCBtWI8jQJm8yqhoNH0mcQh5Ip3Rkcx6X4fkD1jA54WhfFGkWcdCx8DR&X-Amz-Signature=bdfc19ac19bc72bec66b64ad66935f3003bf94c7e3682488843073051f7e3771&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC44FF73%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2B5Y6x%2FWcLkzKgSsLoFpfcsMCtngxRgFqH%2FM7cBgrlLAiEAlnsexF18CTHVBCJbsXTXTJpl2QhKu7tgKijnfLCMtrUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFoh5wZcAkrdPCADbCrcA0y3rF5ZslpNPw9JoWh6kTtBBvqc%2BASpsdrZWHH%2FvlVaJn4MEywclwfBJnmKkV0W4d2e%2F56FmZUFqAIgy8n6OHXbF0K%2F7mnGgAzbiyNtjoFn49aCJtpZTtZ5sWTkOhUiz4Afr4i3vqXz5as1pe44T40%2FLLD7iJRYlvxH6QT40NRogIEoGysE0o76EWOFBDvyT2%2FgKIYbg4248VuI1t5tb8XxGit4iJReE46037d%2BRRRghT9F3jJletZHkFYFt75vjKevvx3GnPhDVt5CvGtezjGC01ftw1HfV3f9RvbE4hf0J%2BAeTYvbVIrCGhea%2BXNBnRHgvhEnjbxwzJsT5n10VH3zzbRWmwOEAOFAA50K2fCGiylKHnn140Rmtvjc97Xq2QCVR2m%2Bvs%2FLOrsUsUVjXXnHEHqx3uPL0u4E%2BJE0MJDvPzHk4al2C%2F%2B6IEG7FrK%2BLC3oSJeYi4WVbQ2dZUMQZUYPPXPTBbfVrm%2FXZBDPEZymxNnL292FMhvJjJTGQ6Q6dJPR2U1xh%2FJ3LnOmV3ntaYuhf3V6R0F4txZEIL0ofhayPlPksQVWvNXtPHcM5xDa%2FjrWfEyfgUBelk4LmrF6Li4JqyMs0pt30%2FmH%2BQ4bNy5s6CdolbPd%2BLIdos94MPSN77wGOqUBEwxElEnWzaEjzJJqQJx8IzTKPQquGtn%2FT2Jb%2FXlIqpfF8VzyF1RPkoQJhmDA3CyawkS0MMSTKYzP8BX3lqXcdPf9pW73I5BzX%2FFDGvtj0%2FmaLwKIB79YNxr6nenRXApuq1%2FyPCaGF90YxingPIcMzux8mzEoTZCCBH1eG5LK0H92NhoyKs%2BkLM6KIdIQifFmHKjIzzufaUUR8nDe%2BAWJrOa1oXS3&X-Amz-Signature=ab51004fd1c3e10fdd9b704b6aaeebda28813d6ee6f7383e202887a6ef6aa313&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTWETCA7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRgDBnvUKRH%2BstuRVtIM8SMGTrMDxmEQ5N7rTtqSrH8gIgQ4qLrqjbhNqOF5WvcNPmy2GTXiYjAzWY86wqqD4n9nkqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAsZFHf8pDqiA5wtkyrcA76zihKHj1Nvk7imi45zTrqPqrgWMTzFkNpGE68KrBvA0EjEy4mNQdIlWT9UMHqi5IWJHJieYOKY4en3uzGV7X9i9IeNyomTVhUuYDObCD%2BP8kboi7fUXJVQ6YBiphMeLtXEIXbWhV2BgSwmRivdDFQGcncKlSIFLcC9d%2FTotjxf6P0tKKNjbcZwcvhz4EwSYaJc6EvkGhHkkPuCEgrFFAJVcLNe%2BN46ipDpsSbwcl3RMzU%2BtGXwVx73GmYU7pYBXWESMDAqlEqoNB9Qprwj%2FZIeDFhZBRo0WO%2FFex3gxy56%2BsYTBkGJku1oVzQJAyCfV4SZH8oh6N5gO%2B4BtxEB3FXdC1y3iUjniegIRy6Z7lV%2FiO95n%2F%2BPUh224aKdh%2Fomdf7zuCJWIi%2FoUR9vSNtA%2FonRRInarH45rvNIWdHAPwZbOwwwOswe2vSV8abtfIjh6hQ36Kw5ZQ37lzLUpV%2B3jVVJdKPW5OEVeVPiADVbVN3%2BNnfOcupuf4SVlpTh5r%2BZrISL6iuPFWbfkMcPl9w2Rrkwvyzme7YmdQBX6OiEbcwcIIBhYosELBE1iVg2kS8176vFM4Z0bkxQAtWK9Kxe1urAMyYjqvWxxYtDOv7Qeef90GO2Mq7vA%2BLa4N6uMPGN77wGOqUB9HS6egHiVPa2E9LJyWrHp98i772UWZNuDW2AXdpuc2k%2Fav6O6kKFYuAjY2KvX%2F88YFTSruIohn1IUENJCyn0wQ7GyEF%2FNM7j1ay7%2FYcARB1ZvUDxtndZF9UPwTB4IO2U8W4y%2Bl07Dqkpix%2F1ptPMq02b7pYlQsn1t9wEtAcGS%2BHCTQ4I3HU%2FckTG801OHhLv3p%2BhVRqb2h2n%2F54qBjMo0F2WioFY&X-Amz-Signature=858c0fd601c618a127f31b30edac958a343555483a65b95f6fe794660cfd96a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOX2XX3I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkOAUU9ZIHEe%2BZ%2FEvgaFmfqZ0TuQLn9zFBFURuPVXNtAiBdjW6p0zqUH%2FNwrDj5LVdP9vnYvGmQKgM61zm3%2Fhl3CyqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkUowA1V6OCB8BXt0KtwDsTyAPKxt%2FD2N611OARVzp7ZISJ63NthRVI8pHmjoCoJg5w8680Bh3V1vfVIU5hDkv9ulVsvG1GLEoMpPrORfnB6roYrGMQrHAGqgXb3CSlcxAtdl31Wz97hHy0ow1%2F2nUDk4RR3N5V0D394jhZj9MIimNl%2BME8284%2FVbSc9g6bCteZIKPc6fmEHMSQw3A3ByL%2BmZGq%2ByiWwXat22ivY0UL4JThHGStoRdrOj1sCKOVPwA8NDzebIWjsgL3F6ZqkJsPmITESftbxZn94RKesVog7RkKTeyfQXuSpFWABajNLLx4%2FaMieYJQW4uwzw0YCh%2F%2BX1RLAHTzmmJYWB4YIkUgRaFRiMWE%2BTxn%2BabyWnc%2BluZyis%2B6JeCOD5aGJFNZswBIgqSz1rWHnz6jchq06MhoXbh5XZOdo63tEthQKXt1Yk2gXFyyiegBqjArDJAEgiBJfeAS%2B3yNe1qiXVbwqe3vzNPTZwlZ50R%2FabwjKpI8gKlrw2bOOBXaI9PBYWXRtUqgvxA%2F3HIdwJ%2FhXBnR9p4I3iJd8gnx%2FOyetSDPHGeOJxR%2FPDiRG1%2BkOQiw5vyIR9z8gWqtxlinJ1bXdSOzriN7cO8QQdQHUSSYTvHcwwWFjQ2V9HxCNj0PBu2bIw3Y3vvAY6pgFlfgsV%2Bj0%2Bpno8vp1ZczfBLHUBicNkjTBb3a7LD52KKRtcqIkU%2BoqQhdhDgoA2zmmk0uXtRwnveqfXHUuGI1lRB3OG2LUW98swvOQBrTfW9toyP3ImDiJwg1tmwDGuHJ0G67OLwVrS%2BYQYK0CH4QXxRuOcakIh7r37UL2JtCBtWI8jQJm8yqhoNH0mcQh5Ip3Rkcx6X4fkD1jA54WhfFGkWcdCx8DR&X-Amz-Signature=290ed7d9b0f9bf52639b887c5f6412d93cda4a6341b2bea82ac3d98dfac70720&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOX2XX3I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkOAUU9ZIHEe%2BZ%2FEvgaFmfqZ0TuQLn9zFBFURuPVXNtAiBdjW6p0zqUH%2FNwrDj5LVdP9vnYvGmQKgM61zm3%2Fhl3CyqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkUowA1V6OCB8BXt0KtwDsTyAPKxt%2FD2N611OARVzp7ZISJ63NthRVI8pHmjoCoJg5w8680Bh3V1vfVIU5hDkv9ulVsvG1GLEoMpPrORfnB6roYrGMQrHAGqgXb3CSlcxAtdl31Wz97hHy0ow1%2F2nUDk4RR3N5V0D394jhZj9MIimNl%2BME8284%2FVbSc9g6bCteZIKPc6fmEHMSQw3A3ByL%2BmZGq%2ByiWwXat22ivY0UL4JThHGStoRdrOj1sCKOVPwA8NDzebIWjsgL3F6ZqkJsPmITESftbxZn94RKesVog7RkKTeyfQXuSpFWABajNLLx4%2FaMieYJQW4uwzw0YCh%2F%2BX1RLAHTzmmJYWB4YIkUgRaFRiMWE%2BTxn%2BabyWnc%2BluZyis%2B6JeCOD5aGJFNZswBIgqSz1rWHnz6jchq06MhoXbh5XZOdo63tEthQKXt1Yk2gXFyyiegBqjArDJAEgiBJfeAS%2B3yNe1qiXVbwqe3vzNPTZwlZ50R%2FabwjKpI8gKlrw2bOOBXaI9PBYWXRtUqgvxA%2F3HIdwJ%2FhXBnR9p4I3iJd8gnx%2FOyetSDPHGeOJxR%2FPDiRG1%2BkOQiw5vyIR9z8gWqtxlinJ1bXdSOzriN7cO8QQdQHUSSYTvHcwwWFjQ2V9HxCNj0PBu2bIw3Y3vvAY6pgFlfgsV%2Bj0%2Bpno8vp1ZczfBLHUBicNkjTBb3a7LD52KKRtcqIkU%2BoqQhdhDgoA2zmmk0uXtRwnveqfXHUuGI1lRB3OG2LUW98swvOQBrTfW9toyP3ImDiJwg1tmwDGuHJ0G67OLwVrS%2BYQYK0CH4QXxRuOcakIh7r37UL2JtCBtWI8jQJm8yqhoNH0mcQh5Ip3Rkcx6X4fkD1jA54WhfFGkWcdCx8DR&X-Amz-Signature=c50de9660e404d94e48ce1915fecad710a4fd0a423f1c1796660f4ccdd46eec3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOX2XX3I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkOAUU9ZIHEe%2BZ%2FEvgaFmfqZ0TuQLn9zFBFURuPVXNtAiBdjW6p0zqUH%2FNwrDj5LVdP9vnYvGmQKgM61zm3%2Fhl3CyqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkUowA1V6OCB8BXt0KtwDsTyAPKxt%2FD2N611OARVzp7ZISJ63NthRVI8pHmjoCoJg5w8680Bh3V1vfVIU5hDkv9ulVsvG1GLEoMpPrORfnB6roYrGMQrHAGqgXb3CSlcxAtdl31Wz97hHy0ow1%2F2nUDk4RR3N5V0D394jhZj9MIimNl%2BME8284%2FVbSc9g6bCteZIKPc6fmEHMSQw3A3ByL%2BmZGq%2ByiWwXat22ivY0UL4JThHGStoRdrOj1sCKOVPwA8NDzebIWjsgL3F6ZqkJsPmITESftbxZn94RKesVog7RkKTeyfQXuSpFWABajNLLx4%2FaMieYJQW4uwzw0YCh%2F%2BX1RLAHTzmmJYWB4YIkUgRaFRiMWE%2BTxn%2BabyWnc%2BluZyis%2B6JeCOD5aGJFNZswBIgqSz1rWHnz6jchq06MhoXbh5XZOdo63tEthQKXt1Yk2gXFyyiegBqjArDJAEgiBJfeAS%2B3yNe1qiXVbwqe3vzNPTZwlZ50R%2FabwjKpI8gKlrw2bOOBXaI9PBYWXRtUqgvxA%2F3HIdwJ%2FhXBnR9p4I3iJd8gnx%2FOyetSDPHGeOJxR%2FPDiRG1%2BkOQiw5vyIR9z8gWqtxlinJ1bXdSOzriN7cO8QQdQHUSSYTvHcwwWFjQ2V9HxCNj0PBu2bIw3Y3vvAY6pgFlfgsV%2Bj0%2Bpno8vp1ZczfBLHUBicNkjTBb3a7LD52KKRtcqIkU%2BoqQhdhDgoA2zmmk0uXtRwnveqfXHUuGI1lRB3OG2LUW98swvOQBrTfW9toyP3ImDiJwg1tmwDGuHJ0G67OLwVrS%2BYQYK0CH4QXxRuOcakIh7r37UL2JtCBtWI8jQJm8yqhoNH0mcQh5Ip3Rkcx6X4fkD1jA54WhfFGkWcdCx8DR&X-Amz-Signature=9c8567c13b0492bdc677e1530252226bff532625ae37aa751e69bd96f0a3ab91&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGDN3PUL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpQt0s21Nc1sTUrX85ngcJ1eqqaszDcpbB1R526QB9pAiEAlZWklf7tqVJlLFNAzmgHiWd7GFLYn2SrLNeye0AZcicqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIInky1bHNjmhAop%2FSrcA4AKQXX8UpU8EdEBHxOkYa9iKzospnIdhMRrHhomrOW7DMAHqpVyz9lAij6YjqUlEJCx8VceD%2F%2FLDpVKQsKt6UqAQAEv9gvCdDqo1Np%2Bni04LX24R%2BsE34w%2BGwGEHnYvH6%2B9P3HJuKpsNUGLzJKVsQRSe%2FOibazKHf8D%2FDet6U64noNjZn6YDlJYM%2BHcLaruhxVadOsJuzDaCDzlVr%2FI7hVKelKsL0aX1Bft9SuYfdyIxoG4j73kfBNfhQDKEIZPhggWwo69nIfFiQlaPmkN5Y0SBt%2FgKcjXgj%2BNehkJ4vQqozSENkQuTv8P%2BikidiucWdQvHPa%2BKMMyEYrQcGFarD8%2Bi9dPDi2HqMlUoxVpyLG6Zcw8LWuRaLTpj%2BS3pJ7TuSNhrvHJKqpvoRuW3fXmfYrHsQCdqWUGaoLr9dHRbj%2BuZxeBkNB8JGmc99KMxe6QFxsuuceBBGRq4sndBGXqQDcvOLneYQyatQx%2FXEI6FrEqd5l1xCggFNxwMKgJuLbkjIU%2B9I5HEY50o6zrvevXjs%2Be160UcaX%2FwO%2FdPV02ku2CiiWQ4JP0wqa%2BSQxctegts9neN6B0udnVWxokSBtUCWcNys4Df8h4nG6kqa9AOZNcfyxpB3fZQyIPyBmkMPWN77wGOqUBwRSUYo8a0Hc8tzC0XSqlXwW7sA6cCP%2BHuImGAJynFM2REnXPx1TH9985957vGT7n635aH%2FyjaJhfGO4NBphMlcgvCmUWh6K3MpDYA7Yo7p%2BXuP9DgbAiVIjztvfTupYgEoJhK%2FMeKSeFeqLylAuJhM9aCmXuwhbNt%2BUTXvTxvJQi7jrWXuzNQIQohI5%2FGpBUVeNgFtIFJwRI5yXDOa%2FC6JdP%2FS0N&X-Amz-Signature=19b33b86b34ece6cfe242c1130d88cb091712278598da69e6d75bc889bf81df5&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVOYLJPJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyvApvIsPx6qPVWebe2bfe3wtSX%2BviVEOiX3nVQQhTQAIhAOX4qEO4BSM%2FFFv51BefAkMw5eNBCXoP%2FxHh8XXOqpSjKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxQjOICieD9C72vpnYq3AN5i9fgdexQDihdZ9vwzyEMFikHXz53rQktsZltg31b4AHnhEVOTU0V1%2BaY8Q1%2Fr%2B1fcLXi1Ij%2FykDUh7uNIdbV9U0p6OB9Hy7yjiKA6zASn4ycEFycK1iClfjWqME3DOgJUnPcfC3DMY6liL0CptX243XMF%2BwaM5tRHavQwVgzR%2FLryEl30ZTAvtfhgOCbfZBZ4XWFvQ%2FCXWAu3SrrGYLH%2BII8aMDSbPoA2fEIITU7wJiE0%2Bk4FoCUJX36kIq%2B0nzPDKjx%2B%2FKyWjaN3ubKrdw0dELvlXWltwDD%2BhQ%2BStLZ%2F%2FSMk%2FDf0cEVkiStXHRwZ1hJVXatfnhb21GojTcoM63l8DqduUCO6uc86NDVJOEErKLQygwrnrSf1AheGXGXnodZ6Ln6y%2BzZz%2BKEDoPOyTajI8nIA7%2FyLtRMahteLxv2XGw%2Bwfjz%2F74xsHfEklLPSmAieBX9vLZlflxsEgrfpwYTUPpabvU4mBMXQd5nCV9m4eZXtwqi9kYKkKIq0XykaeO8Za4yxRjnkHgTWZMdElVGwOln2LkSYNdxCJF6%2Bddq4sZSlyrFhUPEiz3CsjpWLHUcRZmstLd4uFt2dPwe7Ds7fcoTKKFfFt3dDizLYWuX1sY0%2F2XDgNDtHvw01TDEju%2B8BjqkAQQlJZF4ZLJNaQYJNxaoG1V7PPR6DFbUfOHB7B1oK59bmnzhuIIk36bXoIykZnDwERBjyu0R9XK0YF0uufhEPIUUyZ81SsS6WFywxLNN88taBVRjkGoR0YKBHl8BvlevaHSvUgDT12K5Y5CMzRA7rKn%2BkUNUQvduMBLNHAB2VM0w9Ga1BYtiRZVBouq7%2FfJPryxXT14RAsRjZpvUy3JbgZDz4ynz&X-Amz-Signature=e53a3ac194ff604a20c15d8200874e1b8fac00d152f87860e7eef9f43cb053ba&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FDHTKHI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID4gkuXKjiL9zQ5kXKq%2Bkau7iOsoaBgsv%2FSl2Rl5nTamAiBFQc450%2FlBt0IKITEX2E1e7xkYvfgCQtmTeAuzjTndKCqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1jEasMMlPbJshkGKKtwDaRHAhX7%2FkiyQRzNQamYqwe0MBTC1FVaFHLOSFW3Horr1eM2pKeq0LlduD5j7HntjHwTOw0q6wCGXt980UW79DMLE2hlZj%2BpSYErIMp1aTowAThW%2BYj6YZW0Z8WBfbPJLG%2FQVYR%2BNJf9PKIwRoJRLDPHVJwxBTPjEIp8XyE%2BaO8%2BTtPsx2RNYd9HoVPLANXC77QHn4mVHvYKDiG2NlR1LkZJuNCvDEA2L5fIDa%2FSFnTdVqtGgjhKdhVO8uqZCN9yod%2F9bAkfMOGTgMQOo1nw42NJxRw5gDm6%2BOVg3p3HEwKYpcAUyymOZiLWSlC28Mszb4XxtN%2BCx8hNOZIDEokDTLpxKlPvacgAjNJviG3pQbJ5h9bnkMg44tiPGuSzAvfSHdOIKMOhp2a3o8DBpGrMDYKkBmeDLJwWkQDlvzXuTFz8Bkq%2FFi25i533GaeqdnfaWWv5I5oPERyLlZ%2BPVhCES8JHOTvr3tYZSLX%2B%2FbekQxATWPvnhc0Rdbv7vUs3IV2TTZN2y16q9co6AwT6uWOwA7aZoE7T37C0jv5l0cMLadqJ9okNNPNmQPYdnDcHvVlhCym5jWctuSRC5BM17ixvVryCU9rIwntDg3vrKqVneh2aJU2KuvtwTbzeeOf0wpI7vvAY6pgEC9DbOWgORVjqhVDId72Gv8v06DXnG17dxRo9CbaF9Sj1G5UnUz7YhuvgOUZ9i2xZNKQBq8Che97qnhmeM5tzP3i1qHx%2Fw06dJakc%2FwqnY2ImBcvkA%2BZ0O%2FnL%2FwTQ1D5CzhK7LWxS1biZqH5S95roCl1cAtmRL1mD40%2BvVC0t0YcUThhoZpS3rGKP2STI6mHutph%2FVUSj1ltnSU3RnztfVZy61ynWe&X-Amz-Signature=08822b05392217de3d18cc92faf68261532044cdded48ea77a908ce677e29d67&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYTRCFAR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzKXabi2kAZPv08ExuG5cT5MhqGcGPkDdOgnohjJp6uAIgPObKSmhWAnmI2IOUoF7QPqYCLetHJazQy8T92vYnrHkqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAwtGF4wxZe12MmXZCrcAyogWh90lvr41Y%2B4Hj0xZHpLeMwLicQky5K8kOO4ivHR0mIkYKbT6VsA61iHEvRAJ6wmnQr4xD7BNkhkHLIHFadza4VRDlbjsEWpJCrXVbHvjyiZhfYVvI8y9xkLpIhTf3nATATKh4qKDwP2lo75TS6kR%2F1U%2Fm3PIzc8qwk6cIyMaAXGEtkfvACT07eOXc5%2BD5SFRGDAzqeuiiNejNq%2FWyqy%2FUDna8Ir%2B%2ByXyGxccTGldDYHnlUmYqn%2FikLvdZZZ5acYITxexcyq%2FsoLIcujIID%2FxvLs5gIYQxdciJTufnWnx4UaVogZ5bvz%2BNPqJYRbMs8gKcWLLAqnCNzekDsS4Slvhcs%2BMWXTyPFnYuAY31RQTcPfNquy0BbtbhEIp%2B2PDiuY1BM3gvWVYIrwbulRR0vFG9CyXQU60OIXyasX71fmIn2w9mk9YGnRBIgeiSm3E9jRJM%2BFuHS0dEDXbb4h2EDaqxNr2QVGuJKj9wcnYxqxeQ4SUBXGqaA6Z7ikwtnw7YVWsWVolGhNCsDStcLa%2FJhFCnI2jpWMHuoJiuAUlPlIZQdppb4bpUIfcLAc6all2i0QyLvN2Jk2fKD9o3cbACD6AlivtEg2MVBcrzXweZZ%2FstDSPexpX%2BmBOabiMKGO77wGOqUB4X%2BoVLvp%2BGm6odoH3Q2%2BaGlgRghTHr74XwMh0sXWwXvDk3XFjCsXYgb9MhbaQqdu0hyBFZLwi2fA4m%2BOXXe%2F3wx7hzYKTh3PVA6I1x6PkOBH1vs5HXEK1K4QBG%2Bi8PKwXk0Ly6BZgM9JxMAKBnsh5qUub2XTjSVFWqni9jYO6sO7ZjQqCgmg0aqiUEL%2Ba%2FSbyvkGr9CjpuT4nohGArtPWTXKMlku&X-Amz-Signature=339a59d6c498f3d2a79fd646025fb396baabea762762c62a09eac10728d00876&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYTRCFAR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzKXabi2kAZPv08ExuG5cT5MhqGcGPkDdOgnohjJp6uAIgPObKSmhWAnmI2IOUoF7QPqYCLetHJazQy8T92vYnrHkqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAwtGF4wxZe12MmXZCrcAyogWh90lvr41Y%2B4Hj0xZHpLeMwLicQky5K8kOO4ivHR0mIkYKbT6VsA61iHEvRAJ6wmnQr4xD7BNkhkHLIHFadza4VRDlbjsEWpJCrXVbHvjyiZhfYVvI8y9xkLpIhTf3nATATKh4qKDwP2lo75TS6kR%2F1U%2Fm3PIzc8qwk6cIyMaAXGEtkfvACT07eOXc5%2BD5SFRGDAzqeuiiNejNq%2FWyqy%2FUDna8Ir%2B%2ByXyGxccTGldDYHnlUmYqn%2FikLvdZZZ5acYITxexcyq%2FsoLIcujIID%2FxvLs5gIYQxdciJTufnWnx4UaVogZ5bvz%2BNPqJYRbMs8gKcWLLAqnCNzekDsS4Slvhcs%2BMWXTyPFnYuAY31RQTcPfNquy0BbtbhEIp%2B2PDiuY1BM3gvWVYIrwbulRR0vFG9CyXQU60OIXyasX71fmIn2w9mk9YGnRBIgeiSm3E9jRJM%2BFuHS0dEDXbb4h2EDaqxNr2QVGuJKj9wcnYxqxeQ4SUBXGqaA6Z7ikwtnw7YVWsWVolGhNCsDStcLa%2FJhFCnI2jpWMHuoJiuAUlPlIZQdppb4bpUIfcLAc6all2i0QyLvN2Jk2fKD9o3cbACD6AlivtEg2MVBcrzXweZZ%2FstDSPexpX%2BmBOabiMKGO77wGOqUB4X%2BoVLvp%2BGm6odoH3Q2%2BaGlgRghTHr74XwMh0sXWwXvDk3XFjCsXYgb9MhbaQqdu0hyBFZLwi2fA4m%2BOXXe%2F3wx7hzYKTh3PVA6I1x6PkOBH1vs5HXEK1K4QBG%2Bi8PKwXk0Ly6BZgM9JxMAKBnsh5qUub2XTjSVFWqni9jYO6sO7ZjQqCgmg0aqiUEL%2Ba%2FSbyvkGr9CjpuT4nohGArtPWTXKMlku&X-Amz-Signature=fdac8e3e120788c5ddaee3f82605121c14e8daa278779189d8f37bf590523c97&X-Amz-SignedHeaders=host&x-id=GetObject)

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
