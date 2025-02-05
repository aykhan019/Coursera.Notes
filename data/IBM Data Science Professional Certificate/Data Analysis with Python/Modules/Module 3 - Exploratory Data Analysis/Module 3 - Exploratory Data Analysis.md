

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHSYOJRP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIAc33GK12pt%2FQxTcW2k%2FyNeYkMbiZtgYiwLHUpZmZfL8AiAYvnOCJ1mDyeeQDUuiieaBeHnW%2FfDeckt%2FEY2oRr3otCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIM5A6m4eZVPmQvUUNEKtwD9T8rL3YrWvgxyCFy5DE4%2ByfvhUsRuFpAEFF48C9fmkdBBPR%2BFozrByur%2FkqdcGYrndn%2F0pT9OUbt7ZSIzmUUaehFT9A63hGehzOnS4t3M0ktpn0JjoiQEuLoRQCQimtGqzCxEQRAyQM5a3fLlFwOFIv%2Fiex4Hw9TP9vE0WDJzvmZJgiIIRSder7VTXJZDrzuJn5TfDOU5O%2FD1uZ2AU1JX24kEiIVPN1J7j4VmcD4SJAQMHuRDyGkeCcrhpHLfkYIe5ihHlI6ZwsFvTDv4z0P2pPeemibHQCgKaTkNJGU9D%2FIHytTFecK24ZxGW8pshq8d6aiuVrKUZh9wuymvccubuUBnuTwAWNE6gMo6X1ssQ4EzjxYMzu2O8Gu5fiy3lcxYAj6rkQXpzO8FpuWziIVnXPXpyB0Qazdzq2PLG5p13a7g2ynyHrHsVo0q1NcaQh3HolSmxXixekDS%2FHNOH63%2FTXaJwybVrBg8%2FmpgWXogiXPL9z%2Bb589n%2BuPOb6BkaZjdRAk0Gq3oEj1UAhASF%2FW3rkfP57HDLqODSDNlOLhcjuMiFuGKs7C%2BOIzQUYe5zvy69B4LE9HDSPpOUbdnNjAmyBCTP7HK%2FCvXamDEIo9xqTaWCFYMOnPLIuwjacwnp2OvQY6pgGS%2FW2N0%2FRW2enfKdwLrMhLwcFv2JCl1yCOiHlGkavkBjcz7J8%2BHqPtiIiYxy9sqVacudmXJNJkF5lGE3Rs7Taw5eBS8vs5lDk69PHaOHByI78giJ0llWVAE3gk5mnYx0ctZt3fGrRZTKVliOgdXX%2Fx1M7qskb8WKNtw1TxutsqkNizaBpCxr1htPYyxAJHPkG5CKddKyGhQLoqUt5y21ySH9p7pZ7K&X-Amz-Signature=420b5bec13be8407cfbc82c7c64d55f5ed2fbdce84b914b01f5555b929a4369e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHSYOJRP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIAc33GK12pt%2FQxTcW2k%2FyNeYkMbiZtgYiwLHUpZmZfL8AiAYvnOCJ1mDyeeQDUuiieaBeHnW%2FfDeckt%2FEY2oRr3otCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIM5A6m4eZVPmQvUUNEKtwD9T8rL3YrWvgxyCFy5DE4%2ByfvhUsRuFpAEFF48C9fmkdBBPR%2BFozrByur%2FkqdcGYrndn%2F0pT9OUbt7ZSIzmUUaehFT9A63hGehzOnS4t3M0ktpn0JjoiQEuLoRQCQimtGqzCxEQRAyQM5a3fLlFwOFIv%2Fiex4Hw9TP9vE0WDJzvmZJgiIIRSder7VTXJZDrzuJn5TfDOU5O%2FD1uZ2AU1JX24kEiIVPN1J7j4VmcD4SJAQMHuRDyGkeCcrhpHLfkYIe5ihHlI6ZwsFvTDv4z0P2pPeemibHQCgKaTkNJGU9D%2FIHytTFecK24ZxGW8pshq8d6aiuVrKUZh9wuymvccubuUBnuTwAWNE6gMo6X1ssQ4EzjxYMzu2O8Gu5fiy3lcxYAj6rkQXpzO8FpuWziIVnXPXpyB0Qazdzq2PLG5p13a7g2ynyHrHsVo0q1NcaQh3HolSmxXixekDS%2FHNOH63%2FTXaJwybVrBg8%2FmpgWXogiXPL9z%2Bb589n%2BuPOb6BkaZjdRAk0Gq3oEj1UAhASF%2FW3rkfP57HDLqODSDNlOLhcjuMiFuGKs7C%2BOIzQUYe5zvy69B4LE9HDSPpOUbdnNjAmyBCTP7HK%2FCvXamDEIo9xqTaWCFYMOnPLIuwjacwnp2OvQY6pgGS%2FW2N0%2FRW2enfKdwLrMhLwcFv2JCl1yCOiHlGkavkBjcz7J8%2BHqPtiIiYxy9sqVacudmXJNJkF5lGE3Rs7Taw5eBS8vs5lDk69PHaOHByI78giJ0llWVAE3gk5mnYx0ctZt3fGrRZTKVliOgdXX%2Fx1M7qskb8WKNtw1TxutsqkNizaBpCxr1htPYyxAJHPkG5CKddKyGhQLoqUt5y21ySH9p7pZ7K&X-Amz-Signature=f4335090ca4b9c73a8890885bc824a198a87e1f5a2394f0fa98054f20f83842e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHSYOJRP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIAc33GK12pt%2FQxTcW2k%2FyNeYkMbiZtgYiwLHUpZmZfL8AiAYvnOCJ1mDyeeQDUuiieaBeHnW%2FfDeckt%2FEY2oRr3otCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIM5A6m4eZVPmQvUUNEKtwD9T8rL3YrWvgxyCFy5DE4%2ByfvhUsRuFpAEFF48C9fmkdBBPR%2BFozrByur%2FkqdcGYrndn%2F0pT9OUbt7ZSIzmUUaehFT9A63hGehzOnS4t3M0ktpn0JjoiQEuLoRQCQimtGqzCxEQRAyQM5a3fLlFwOFIv%2Fiex4Hw9TP9vE0WDJzvmZJgiIIRSder7VTXJZDrzuJn5TfDOU5O%2FD1uZ2AU1JX24kEiIVPN1J7j4VmcD4SJAQMHuRDyGkeCcrhpHLfkYIe5ihHlI6ZwsFvTDv4z0P2pPeemibHQCgKaTkNJGU9D%2FIHytTFecK24ZxGW8pshq8d6aiuVrKUZh9wuymvccubuUBnuTwAWNE6gMo6X1ssQ4EzjxYMzu2O8Gu5fiy3lcxYAj6rkQXpzO8FpuWziIVnXPXpyB0Qazdzq2PLG5p13a7g2ynyHrHsVo0q1NcaQh3HolSmxXixekDS%2FHNOH63%2FTXaJwybVrBg8%2FmpgWXogiXPL9z%2Bb589n%2BuPOb6BkaZjdRAk0Gq3oEj1UAhASF%2FW3rkfP57HDLqODSDNlOLhcjuMiFuGKs7C%2BOIzQUYe5zvy69B4LE9HDSPpOUbdnNjAmyBCTP7HK%2FCvXamDEIo9xqTaWCFYMOnPLIuwjacwnp2OvQY6pgGS%2FW2N0%2FRW2enfKdwLrMhLwcFv2JCl1yCOiHlGkavkBjcz7J8%2BHqPtiIiYxy9sqVacudmXJNJkF5lGE3Rs7Taw5eBS8vs5lDk69PHaOHByI78giJ0llWVAE3gk5mnYx0ctZt3fGrRZTKVliOgdXX%2Fx1M7qskb8WKNtw1TxutsqkNizaBpCxr1htPYyxAJHPkG5CKddKyGhQLoqUt5y21ySH9p7pZ7K&X-Amz-Signature=9483b8f534c71dbf46e7a8530671c4a9efc1dac3da7854548b5c5c90d956860b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USOI42P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB0QbTFmwLJs3RvM8NkzzwVSE8rfg8UyMpXIZ9GoUjaiAiBGL8J1o4IUWu%2FMy7p6%2BxlGxpOJw%2FeYUgdEXQkHl85jmir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMTad2Kknfo8cSHs11KtwDCY4QsxKntb6UjyZfc5yOU6LHZTx8izl6lNPm7LiW5oeJ8Ql6rwm3pkjsLu25n1yotHl9wojVwQsO%2FjzmBFQr5GFtJ9gxYivcMWKtAcGgHjzbDGr26bZEYxC%2F79sq4vnwlWq7AVeB6Hc%2B0whBPFN5mlfdVUfMQJMiWO0%2BXSlR3k%2FxIhjmpDKvZK8l7K4zJg4JzGp0AVKy9xU8xjnjTxbk0e6UzKr5SoFa2rJ%2B4R%2FlwgeLlk99smzeGYaMtjvj1XBPUxwbP1biKRr2jQx9iwdUu%2BayvyChOubzi62zVN90vs5MdVIpw71mfvuhx9YsP5goYTLSCtMgUbkthVxczhdTlc6l2JlbYzARE4ASas6qfHgvQKeUMm%2FHcRODvAnZk55RDi3CBHHqHW0JE%2BHjkykbn%2FtbJH7rMHXCrFCIrH6muAcOzf1thZttXu9tFKXIxStT3rYLXyBh%2FPwChbkm8rvVETQsrWnz8INRcyglwURirL%2FvSlDpomjueS%2FkBrSqIhdrNrHz%2FSE1SQ3RO0tuwfgOJfQduDaL3AyM3y6HvZYSyD4QybtrX8ZINeJPQdW8rnr10iZcU0cxi1iosVnMzHX%2BogjLSmC4PWLcCDu6tVRyBjLO35HH4%2BwmNTxMjhcwo52OvQY6pgHCN6ofv36fxFDlNfYBVad62Wif5gmOQksmEhLZ4NHh%2BTSJYQ8Ueufaq4P70rqlPb5BHocbAZC5TiwV5nJiV%2FtmZ1dj6bT0GtGBAZVsOeLwLPsYK9KXGv8geCWV4Eenk%2FBc9i8SiDoNgRlFETEmZNqO5ucasBej8rxtQC657eU0ubrNAefiyi3CtrbyZoLryuPNwikfw0DBzWNXHbgHyg0TP6agzzY%2F&X-Amz-Signature=f1db4169e7e8b6dee3c659d97eecc0bf0aca2ea3fc1f9b75333b42a68da8e46c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USOI42P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB0QbTFmwLJs3RvM8NkzzwVSE8rfg8UyMpXIZ9GoUjaiAiBGL8J1o4IUWu%2FMy7p6%2BxlGxpOJw%2FeYUgdEXQkHl85jmir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMTad2Kknfo8cSHs11KtwDCY4QsxKntb6UjyZfc5yOU6LHZTx8izl6lNPm7LiW5oeJ8Ql6rwm3pkjsLu25n1yotHl9wojVwQsO%2FjzmBFQr5GFtJ9gxYivcMWKtAcGgHjzbDGr26bZEYxC%2F79sq4vnwlWq7AVeB6Hc%2B0whBPFN5mlfdVUfMQJMiWO0%2BXSlR3k%2FxIhjmpDKvZK8l7K4zJg4JzGp0AVKy9xU8xjnjTxbk0e6UzKr5SoFa2rJ%2B4R%2FlwgeLlk99smzeGYaMtjvj1XBPUxwbP1biKRr2jQx9iwdUu%2BayvyChOubzi62zVN90vs5MdVIpw71mfvuhx9YsP5goYTLSCtMgUbkthVxczhdTlc6l2JlbYzARE4ASas6qfHgvQKeUMm%2FHcRODvAnZk55RDi3CBHHqHW0JE%2BHjkykbn%2FtbJH7rMHXCrFCIrH6muAcOzf1thZttXu9tFKXIxStT3rYLXyBh%2FPwChbkm8rvVETQsrWnz8INRcyglwURirL%2FvSlDpomjueS%2FkBrSqIhdrNrHz%2FSE1SQ3RO0tuwfgOJfQduDaL3AyM3y6HvZYSyD4QybtrX8ZINeJPQdW8rnr10iZcU0cxi1iosVnMzHX%2BogjLSmC4PWLcCDu6tVRyBjLO35HH4%2BwmNTxMjhcwo52OvQY6pgHCN6ofv36fxFDlNfYBVad62Wif5gmOQksmEhLZ4NHh%2BTSJYQ8Ueufaq4P70rqlPb5BHocbAZC5TiwV5nJiV%2FtmZ1dj6bT0GtGBAZVsOeLwLPsYK9KXGv8geCWV4Eenk%2FBc9i8SiDoNgRlFETEmZNqO5ucasBej8rxtQC657eU0ubrNAefiyi3CtrbyZoLryuPNwikfw0DBzWNXHbgHyg0TP6agzzY%2F&X-Amz-Signature=bd7a5936e7ccbfe2cdadc94c59d9dae3819ee770288fc5076a242de531da383d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USOI42P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB0QbTFmwLJs3RvM8NkzzwVSE8rfg8UyMpXIZ9GoUjaiAiBGL8J1o4IUWu%2FMy7p6%2BxlGxpOJw%2FeYUgdEXQkHl85jmir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMTad2Kknfo8cSHs11KtwDCY4QsxKntb6UjyZfc5yOU6LHZTx8izl6lNPm7LiW5oeJ8Ql6rwm3pkjsLu25n1yotHl9wojVwQsO%2FjzmBFQr5GFtJ9gxYivcMWKtAcGgHjzbDGr26bZEYxC%2F79sq4vnwlWq7AVeB6Hc%2B0whBPFN5mlfdVUfMQJMiWO0%2BXSlR3k%2FxIhjmpDKvZK8l7K4zJg4JzGp0AVKy9xU8xjnjTxbk0e6UzKr5SoFa2rJ%2B4R%2FlwgeLlk99smzeGYaMtjvj1XBPUxwbP1biKRr2jQx9iwdUu%2BayvyChOubzi62zVN90vs5MdVIpw71mfvuhx9YsP5goYTLSCtMgUbkthVxczhdTlc6l2JlbYzARE4ASas6qfHgvQKeUMm%2FHcRODvAnZk55RDi3CBHHqHW0JE%2BHjkykbn%2FtbJH7rMHXCrFCIrH6muAcOzf1thZttXu9tFKXIxStT3rYLXyBh%2FPwChbkm8rvVETQsrWnz8INRcyglwURirL%2FvSlDpomjueS%2FkBrSqIhdrNrHz%2FSE1SQ3RO0tuwfgOJfQduDaL3AyM3y6HvZYSyD4QybtrX8ZINeJPQdW8rnr10iZcU0cxi1iosVnMzHX%2BogjLSmC4PWLcCDu6tVRyBjLO35HH4%2BwmNTxMjhcwo52OvQY6pgHCN6ofv36fxFDlNfYBVad62Wif5gmOQksmEhLZ4NHh%2BTSJYQ8Ueufaq4P70rqlPb5BHocbAZC5TiwV5nJiV%2FtmZ1dj6bT0GtGBAZVsOeLwLPsYK9KXGv8geCWV4Eenk%2FBc9i8SiDoNgRlFETEmZNqO5ucasBej8rxtQC657eU0ubrNAefiyi3CtrbyZoLryuPNwikfw0DBzWNXHbgHyg0TP6agzzY%2F&X-Amz-Signature=9395beb3543c183694743253278370f168f858f24283eeebe69f95e0542df866&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USOI42P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB0QbTFmwLJs3RvM8NkzzwVSE8rfg8UyMpXIZ9GoUjaiAiBGL8J1o4IUWu%2FMy7p6%2BxlGxpOJw%2FeYUgdEXQkHl85jmir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMTad2Kknfo8cSHs11KtwDCY4QsxKntb6UjyZfc5yOU6LHZTx8izl6lNPm7LiW5oeJ8Ql6rwm3pkjsLu25n1yotHl9wojVwQsO%2FjzmBFQr5GFtJ9gxYivcMWKtAcGgHjzbDGr26bZEYxC%2F79sq4vnwlWq7AVeB6Hc%2B0whBPFN5mlfdVUfMQJMiWO0%2BXSlR3k%2FxIhjmpDKvZK8l7K4zJg4JzGp0AVKy9xU8xjnjTxbk0e6UzKr5SoFa2rJ%2B4R%2FlwgeLlk99smzeGYaMtjvj1XBPUxwbP1biKRr2jQx9iwdUu%2BayvyChOubzi62zVN90vs5MdVIpw71mfvuhx9YsP5goYTLSCtMgUbkthVxczhdTlc6l2JlbYzARE4ASas6qfHgvQKeUMm%2FHcRODvAnZk55RDi3CBHHqHW0JE%2BHjkykbn%2FtbJH7rMHXCrFCIrH6muAcOzf1thZttXu9tFKXIxStT3rYLXyBh%2FPwChbkm8rvVETQsrWnz8INRcyglwURirL%2FvSlDpomjueS%2FkBrSqIhdrNrHz%2FSE1SQ3RO0tuwfgOJfQduDaL3AyM3y6HvZYSyD4QybtrX8ZINeJPQdW8rnr10iZcU0cxi1iosVnMzHX%2BogjLSmC4PWLcCDu6tVRyBjLO35HH4%2BwmNTxMjhcwo52OvQY6pgHCN6ofv36fxFDlNfYBVad62Wif5gmOQksmEhLZ4NHh%2BTSJYQ8Ueufaq4P70rqlPb5BHocbAZC5TiwV5nJiV%2FtmZ1dj6bT0GtGBAZVsOeLwLPsYK9KXGv8geCWV4Eenk%2FBc9i8SiDoNgRlFETEmZNqO5ucasBej8rxtQC657eU0ubrNAefiyi3CtrbyZoLryuPNwikfw0DBzWNXHbgHyg0TP6agzzY%2F&X-Amz-Signature=9536c5438ebea93485706d70fc0130c41df55fe04d5db0a5485ccb8bd53899dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USOI42P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB0QbTFmwLJs3RvM8NkzzwVSE8rfg8UyMpXIZ9GoUjaiAiBGL8J1o4IUWu%2FMy7p6%2BxlGxpOJw%2FeYUgdEXQkHl85jmir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMTad2Kknfo8cSHs11KtwDCY4QsxKntb6UjyZfc5yOU6LHZTx8izl6lNPm7LiW5oeJ8Ql6rwm3pkjsLu25n1yotHl9wojVwQsO%2FjzmBFQr5GFtJ9gxYivcMWKtAcGgHjzbDGr26bZEYxC%2F79sq4vnwlWq7AVeB6Hc%2B0whBPFN5mlfdVUfMQJMiWO0%2BXSlR3k%2FxIhjmpDKvZK8l7K4zJg4JzGp0AVKy9xU8xjnjTxbk0e6UzKr5SoFa2rJ%2B4R%2FlwgeLlk99smzeGYaMtjvj1XBPUxwbP1biKRr2jQx9iwdUu%2BayvyChOubzi62zVN90vs5MdVIpw71mfvuhx9YsP5goYTLSCtMgUbkthVxczhdTlc6l2JlbYzARE4ASas6qfHgvQKeUMm%2FHcRODvAnZk55RDi3CBHHqHW0JE%2BHjkykbn%2FtbJH7rMHXCrFCIrH6muAcOzf1thZttXu9tFKXIxStT3rYLXyBh%2FPwChbkm8rvVETQsrWnz8INRcyglwURirL%2FvSlDpomjueS%2FkBrSqIhdrNrHz%2FSE1SQ3RO0tuwfgOJfQduDaL3AyM3y6HvZYSyD4QybtrX8ZINeJPQdW8rnr10iZcU0cxi1iosVnMzHX%2BogjLSmC4PWLcCDu6tVRyBjLO35HH4%2BwmNTxMjhcwo52OvQY6pgHCN6ofv36fxFDlNfYBVad62Wif5gmOQksmEhLZ4NHh%2BTSJYQ8Ueufaq4P70rqlPb5BHocbAZC5TiwV5nJiV%2FtmZ1dj6bT0GtGBAZVsOeLwLPsYK9KXGv8geCWV4Eenk%2FBc9i8SiDoNgRlFETEmZNqO5ucasBej8rxtQC657eU0ubrNAefiyi3CtrbyZoLryuPNwikfw0DBzWNXHbgHyg0TP6agzzY%2F&X-Amz-Signature=d3c5ad570746d2a8975d253679bcca7540ef3f3167ef4cd2c134128ac1b427a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USOI42P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB0QbTFmwLJs3RvM8NkzzwVSE8rfg8UyMpXIZ9GoUjaiAiBGL8J1o4IUWu%2FMy7p6%2BxlGxpOJw%2FeYUgdEXQkHl85jmir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMTad2Kknfo8cSHs11KtwDCY4QsxKntb6UjyZfc5yOU6LHZTx8izl6lNPm7LiW5oeJ8Ql6rwm3pkjsLu25n1yotHl9wojVwQsO%2FjzmBFQr5GFtJ9gxYivcMWKtAcGgHjzbDGr26bZEYxC%2F79sq4vnwlWq7AVeB6Hc%2B0whBPFN5mlfdVUfMQJMiWO0%2BXSlR3k%2FxIhjmpDKvZK8l7K4zJg4JzGp0AVKy9xU8xjnjTxbk0e6UzKr5SoFa2rJ%2B4R%2FlwgeLlk99smzeGYaMtjvj1XBPUxwbP1biKRr2jQx9iwdUu%2BayvyChOubzi62zVN90vs5MdVIpw71mfvuhx9YsP5goYTLSCtMgUbkthVxczhdTlc6l2JlbYzARE4ASas6qfHgvQKeUMm%2FHcRODvAnZk55RDi3CBHHqHW0JE%2BHjkykbn%2FtbJH7rMHXCrFCIrH6muAcOzf1thZttXu9tFKXIxStT3rYLXyBh%2FPwChbkm8rvVETQsrWnz8INRcyglwURirL%2FvSlDpomjueS%2FkBrSqIhdrNrHz%2FSE1SQ3RO0tuwfgOJfQduDaL3AyM3y6HvZYSyD4QybtrX8ZINeJPQdW8rnr10iZcU0cxi1iosVnMzHX%2BogjLSmC4PWLcCDu6tVRyBjLO35HH4%2BwmNTxMjhcwo52OvQY6pgHCN6ofv36fxFDlNfYBVad62Wif5gmOQksmEhLZ4NHh%2BTSJYQ8Ueufaq4P70rqlPb5BHocbAZC5TiwV5nJiV%2FtmZ1dj6bT0GtGBAZVsOeLwLPsYK9KXGv8geCWV4Eenk%2FBc9i8SiDoNgRlFETEmZNqO5ucasBej8rxtQC657eU0ubrNAefiyi3CtrbyZoLryuPNwikfw0DBzWNXHbgHyg0TP6agzzY%2F&X-Amz-Signature=c7acc9bfba32976ebcbfda72d228e4f6b7123ffcb243884182b488bc97245b1f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YHUYYLF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDXC%2BFXP3O8us8YchgoInGTAAM%2FL8WopAxu0bzM7CjrhQIhAJJkwOYWm5AueJCWLRik4P%2BE06GnbEaqUZtV96CjQ44PKv8DCEgQABoMNjM3NDIzMTgzODA1IgwTmwQDopjjLlkC24Mq3AOyXMrG6VlwrnXu1H9GqKQGX43ZsDRGaXX%2B7EtZRn33Lv9HfMzk604zDTJGwd5iN13uUN2VhDEftdC8DIVnUZtfshenMEvLDt2aSoSjLb2fdMtC31R4cx5bJL6Ax0Nq4xVXNP13%2BrL5Q3mJM7q9ZA4vnisxDJhqemuHU%2BJKq1hH%2BYCZeEN22Rd40x2F5WYkB7BuaWz51HwsOxP7JcB6w1UWlTLb%2BC1wYCo9KqOozmUM24SQ28%2FGZeelyuJDhwyy3%2BOkXTcJL%2F10kmmaWpION%2BcExjNTO3vDTB%2B%2FtysPCsPsGD8RkzdI5rNPlNmCR8HSH7MoHs%2BTaSbE%2B0Yqpj1AwQ0C996YH%2FdiZKu0VsMKNwJoQPRbaE1e8Au2IbP17nele29pVQF18Lsi%2FGpx2eMY6VahgLDf3P6BTbOuxNPXtleGs%2FV4shy8ipMGSCFZfVmW1surAp42GAvKIg6MDqY9p5V%2By9CGCdsJJTt%2BjP2eUiAPtq%2FYL1YTGLpswZRN01xrEbIznHBYv4qRleUa1p%2Be59ehtFCEdPk4MoEq8EwaSvIX7FsgcnZrrt8zxbdcZZkDgkRjRFvZdBsvVPMEws7Uvkx0LYxLtveMwGWEXYt91%2B6ost89KH3%2B515MstUoEzDYgI69BjqkAVYu6bi4RHv9YMATxlhT2jZpTQoguSzgPRbCFZe7VERmuzjQqMfLa5NSA%2FjT%2BESSY84wIXT2vPpsn1EjnFlxxg%2BFKSnzTdBGcf1PbOuaVRrMplCX3e5L690T%2B2uaZtx3FAXrIk2BT%2BrHG419BXc1umHyvjkBy737Mad%2B53LlwQ9LdQiP1H9xxXvZ6s8dgIMaOyA81rDJnkADtBJoIgWLGwtsrp9r&X-Amz-Signature=fa8057e317a4bbac5aeb59f5bc51e26e4b935c54d6d8d53e72dc71fb4c709710&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2K2PAXH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDGJjw8PNTm4ainr8ZtVtzZlvfjtrl6%2B02zEvMIQDncwwIgUhFgM5khHnik3tz8gczw7H%2BIvlrmSuRYAGT9IhXpbQ4q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDAP8JxHcAclJAHm4zCrcA0SNZd%2FpWX0%2B1x3BVAfErxMqSVp5D9Dw0uBbGfluIbQsrpSAV35LX6rBetJzQJworwDkKkrC0Ux%2F6CfjjdX7ZXKh6irRuA%2BYCtCI76FLkzepKapIVK6i9HVXWMhJfXFEk3mUEKAl13UarCovfsaDZd6G0W17WtZzDndi6GA4C2UFByCmkbmg6fX8MdS%2FNOxBpI%2BRWnreRUg4tJN4FM0MVGp95g6J50UvFIDspS9AgJ1DWdUt3HyMHmkKRzKmtFjcHAH5SBmhJ29EOmDwto%2BTd4QqVrb3KtdmJh5TJNiz5gcKTPU9TBo3uzjVYyuoeoM5FEg51z5UNamTmGk1YcRN1PbyXHNxLqhmYfOUK20yRup6S2vyEbFcX1SUYSEe1hqepLHK%2FX2NRyHk%2FjmSH%2FcbjI2A7z2%2BO6eqcTXIRRYjrUfQ3MILJydPqdPf%2F%2FZb50mNXVhjhr8UH0F81y78wns4Wgrk5eB8pkRYmNxHSALFO1dS9KoLzrArAy0xVzv18%2B12YcJw53WrhbFTeniEhrI%2F7T5KfJK3H%2FM3fiIFkpDNhPlMIBOIam50GC6ihbe0LCcBB4Ay4b7CLtOcW7jg43NgCjUHCjz5MqI7OkCDoaqwYwrbcH3bjk5qNDAAIS%2FfMOGdjr0GOqUBEyuXQxtOzkUnGhxC7z0eUIJQKXYDOUQE%2B%2B7Ynr0UV5fwCWEEoYMnHaiSsZfesen5Cm45xvMfZEFwayukhLXUUZq0PcV7h3AP0kFrAPFk3ax%2BexY9qgmyGThjx%2FoWE5oWadjkvKZd33ki1H7pm1mxdK9Dxqila4v%2F7iqh%2FL17VPqWzL2SXOLSpllYMQQmc3Sa07kchNf59Q%2B6Q68SzMGqXvbHudBW&X-Amz-Signature=9f5c994b3bbb58334012b5c2a62059d64a6863390de93fd642c884ad44c40786&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USOI42P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB0QbTFmwLJs3RvM8NkzzwVSE8rfg8UyMpXIZ9GoUjaiAiBGL8J1o4IUWu%2FMy7p6%2BxlGxpOJw%2FeYUgdEXQkHl85jmir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMTad2Kknfo8cSHs11KtwDCY4QsxKntb6UjyZfc5yOU6LHZTx8izl6lNPm7LiW5oeJ8Ql6rwm3pkjsLu25n1yotHl9wojVwQsO%2FjzmBFQr5GFtJ9gxYivcMWKtAcGgHjzbDGr26bZEYxC%2F79sq4vnwlWq7AVeB6Hc%2B0whBPFN5mlfdVUfMQJMiWO0%2BXSlR3k%2FxIhjmpDKvZK8l7K4zJg4JzGp0AVKy9xU8xjnjTxbk0e6UzKr5SoFa2rJ%2B4R%2FlwgeLlk99smzeGYaMtjvj1XBPUxwbP1biKRr2jQx9iwdUu%2BayvyChOubzi62zVN90vs5MdVIpw71mfvuhx9YsP5goYTLSCtMgUbkthVxczhdTlc6l2JlbYzARE4ASas6qfHgvQKeUMm%2FHcRODvAnZk55RDi3CBHHqHW0JE%2BHjkykbn%2FtbJH7rMHXCrFCIrH6muAcOzf1thZttXu9tFKXIxStT3rYLXyBh%2FPwChbkm8rvVETQsrWnz8INRcyglwURirL%2FvSlDpomjueS%2FkBrSqIhdrNrHz%2FSE1SQ3RO0tuwfgOJfQduDaL3AyM3y6HvZYSyD4QybtrX8ZINeJPQdW8rnr10iZcU0cxi1iosVnMzHX%2BogjLSmC4PWLcCDu6tVRyBjLO35HH4%2BwmNTxMjhcwo52OvQY6pgHCN6ofv36fxFDlNfYBVad62Wif5gmOQksmEhLZ4NHh%2BTSJYQ8Ueufaq4P70rqlPb5BHocbAZC5TiwV5nJiV%2FtmZ1dj6bT0GtGBAZVsOeLwLPsYK9KXGv8geCWV4Eenk%2FBc9i8SiDoNgRlFETEmZNqO5ucasBej8rxtQC657eU0ubrNAefiyi3CtrbyZoLryuPNwikfw0DBzWNXHbgHyg0TP6agzzY%2F&X-Amz-Signature=34f4ddb18326b11cd980c63e006070bc41046a4900056a01358ca4c67078ae4f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USOI42P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB0QbTFmwLJs3RvM8NkzzwVSE8rfg8UyMpXIZ9GoUjaiAiBGL8J1o4IUWu%2FMy7p6%2BxlGxpOJw%2FeYUgdEXQkHl85jmir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMTad2Kknfo8cSHs11KtwDCY4QsxKntb6UjyZfc5yOU6LHZTx8izl6lNPm7LiW5oeJ8Ql6rwm3pkjsLu25n1yotHl9wojVwQsO%2FjzmBFQr5GFtJ9gxYivcMWKtAcGgHjzbDGr26bZEYxC%2F79sq4vnwlWq7AVeB6Hc%2B0whBPFN5mlfdVUfMQJMiWO0%2BXSlR3k%2FxIhjmpDKvZK8l7K4zJg4JzGp0AVKy9xU8xjnjTxbk0e6UzKr5SoFa2rJ%2B4R%2FlwgeLlk99smzeGYaMtjvj1XBPUxwbP1biKRr2jQx9iwdUu%2BayvyChOubzi62zVN90vs5MdVIpw71mfvuhx9YsP5goYTLSCtMgUbkthVxczhdTlc6l2JlbYzARE4ASas6qfHgvQKeUMm%2FHcRODvAnZk55RDi3CBHHqHW0JE%2BHjkykbn%2FtbJH7rMHXCrFCIrH6muAcOzf1thZttXu9tFKXIxStT3rYLXyBh%2FPwChbkm8rvVETQsrWnz8INRcyglwURirL%2FvSlDpomjueS%2FkBrSqIhdrNrHz%2FSE1SQ3RO0tuwfgOJfQduDaL3AyM3y6HvZYSyD4QybtrX8ZINeJPQdW8rnr10iZcU0cxi1iosVnMzHX%2BogjLSmC4PWLcCDu6tVRyBjLO35HH4%2BwmNTxMjhcwo52OvQY6pgHCN6ofv36fxFDlNfYBVad62Wif5gmOQksmEhLZ4NHh%2BTSJYQ8Ueufaq4P70rqlPb5BHocbAZC5TiwV5nJiV%2FtmZ1dj6bT0GtGBAZVsOeLwLPsYK9KXGv8geCWV4Eenk%2FBc9i8SiDoNgRlFETEmZNqO5ucasBej8rxtQC657eU0ubrNAefiyi3CtrbyZoLryuPNwikfw0DBzWNXHbgHyg0TP6agzzY%2F&X-Amz-Signature=629b95540de83a45c44fef906c2573b70e1f126cf53f94fb06e42a6639e68ddd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USOI42P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB0QbTFmwLJs3RvM8NkzzwVSE8rfg8UyMpXIZ9GoUjaiAiBGL8J1o4IUWu%2FMy7p6%2BxlGxpOJw%2FeYUgdEXQkHl85jmir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMTad2Kknfo8cSHs11KtwDCY4QsxKntb6UjyZfc5yOU6LHZTx8izl6lNPm7LiW5oeJ8Ql6rwm3pkjsLu25n1yotHl9wojVwQsO%2FjzmBFQr5GFtJ9gxYivcMWKtAcGgHjzbDGr26bZEYxC%2F79sq4vnwlWq7AVeB6Hc%2B0whBPFN5mlfdVUfMQJMiWO0%2BXSlR3k%2FxIhjmpDKvZK8l7K4zJg4JzGp0AVKy9xU8xjnjTxbk0e6UzKr5SoFa2rJ%2B4R%2FlwgeLlk99smzeGYaMtjvj1XBPUxwbP1biKRr2jQx9iwdUu%2BayvyChOubzi62zVN90vs5MdVIpw71mfvuhx9YsP5goYTLSCtMgUbkthVxczhdTlc6l2JlbYzARE4ASas6qfHgvQKeUMm%2FHcRODvAnZk55RDi3CBHHqHW0JE%2BHjkykbn%2FtbJH7rMHXCrFCIrH6muAcOzf1thZttXu9tFKXIxStT3rYLXyBh%2FPwChbkm8rvVETQsrWnz8INRcyglwURirL%2FvSlDpomjueS%2FkBrSqIhdrNrHz%2FSE1SQ3RO0tuwfgOJfQduDaL3AyM3y6HvZYSyD4QybtrX8ZINeJPQdW8rnr10iZcU0cxi1iosVnMzHX%2BogjLSmC4PWLcCDu6tVRyBjLO35HH4%2BwmNTxMjhcwo52OvQY6pgHCN6ofv36fxFDlNfYBVad62Wif5gmOQksmEhLZ4NHh%2BTSJYQ8Ueufaq4P70rqlPb5BHocbAZC5TiwV5nJiV%2FtmZ1dj6bT0GtGBAZVsOeLwLPsYK9KXGv8geCWV4Eenk%2FBc9i8SiDoNgRlFETEmZNqO5ucasBej8rxtQC657eU0ubrNAefiyi3CtrbyZoLryuPNwikfw0DBzWNXHbgHyg0TP6agzzY%2F&X-Amz-Signature=0e4a855a9b148d1b61d9e6a70ba7f9485f809804679d117b58dbddc11cdc61b5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DTYF5NH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIFf5EaTd29xeILKibPOeh1q6e7d4phPl67ACMjazd4anAiA5f5lERZkobUCwEFv6zWdl%2FqIuJNtROPYqvcBLQ8MDGCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMiLbwQyvQGtHw19GkKtwDJGkhqHGbQK0RlfcbYU7mp0uJi3nbNxenXW7IpRJQsRv%2FOicR%2Fl674XwPdlMt76AGDuK6vsZsBFIQVyooF9WwBKSZ3A34HA7nlZC27FblKUbag1za72G2CawImYDbZhkD23QU9NC2Egq3DmOVky0M1Jofd4IDW4ZpXLAPeI1lAjOCnElljJBzmu%2ByjK6cASwxGVcC5SuK6NdlEs33SkkWTs2bBBg%2Ff6hTrFQVS00lL9W4Tcf7uVHhESE6%2FPvBCIFO5BgOwRX8CTTtR7%2B4KNNLjHF9oyDFNQc7FqQuAso0PBiNSWoFEfuRbd1fTZGT5uEV4LGqgBkHjfUu5vL4uwvSlp3M7JrwATVtVTMqK8Ell%2B%2FrdlWd76HUdxLNUwGdQV4LzX%2B9cMjv6DYxbOF37HSiL6WiWz65Huil9tr7BiORqUr55WltmcXeM%2FxaKsLA7soo%2BpweKKdG2BitvAbWhTeAuIlyMGJtNlIHBT1SnTCjeHd8zrdoOkIrEdRcVhiqrx19i4dOuv8bFTzgxP%2FVASRAllVjrbIpZQ3DPskji3o%2FZeGdNP60Mk3pPe8LQ3OHE6du49VH%2FCjMbtRBNJCis9J8YRlTu%2BsEi466kt6V717pnENfAyHUsSJ%2BcXb2J4UwzJ2OvQY6pgHxJ0PfmJAvjyFcZLBfuNpW63%2FW91mGS%2FxHlRT1LRwxVHpDVfsgl71QLNSncPCg90%2FOwvh1y%2FptNu7fHN%2F49kutn3xfcIc%2F2yVeHxN99PMkWRpMPZQffoIX%2FlmSF9PPqKlrgM4erXEpAkgF82%2Fo5CPyDAF6Tnq7lyR137sImg052IfhU27g27TXVtltpqo7o9z7xImLfCuDY8j8q31338kI6%2B%2BiIm%2FW&X-Amz-Signature=2f4b54f04992f3d915759a1535fcbaf2745e7f1a4a3acafef9b232db9849ce95&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNIA4ZR2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIEwDwFjPMVHKkA0DUyVshvwX2W9gm9X7xD37NMz2lMbwAiEAidS0jmSP2rAF3iK1docuUdlgLzN4%2B9lZsPtNbBtzXmsq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDFe1%2BPN1ChSR0tFkPyrcAyhHAhnkU36Ffzu4yTRb6cO9H2Gk5TpbuD0O1KfuRX74bU6YsRBNW%2Bl5wTQaxjtm%2Be7ot5I0T62TvFbIi4lAFInnyU5EfwNX2x%2BWpzl8njrDWnHrIzgC13suK24LLotuTzZpzHvrLGG%2FtxyzRKInQOWjUhkQ3Spfz1VSeMflhuBFIX3yX7%2B%2FgMkT7BZhOivnK6zco1oISRIwBt6YYQQk2V8tbZAJhpJgcYc2p0i4JnKzcvEqe1ju7ZDadJKo6kHcq%2FxqgasyZev95tetLMO%2FiWlWg%2BSSspUfj7kr6JnzqUKN0j8PtuNY5ThGxW4wEOo0vb3%2BAc0%2BOPzto4pGlHWKWOw4cbQn%2BHctVP%2FXA2HkTrXRLUXFnxSGyJpPusB5SZqPZRoba8s1b0PdITzP3wld%2FNhmx1Ji84nU8ezMY4GaMsJf3NoSRk7gBH893rP%2BM7hrlJu8aSJpzosRIxvGaD9YoAd2jWoHFVvPQq4m%2BXTHbsDMkEZrwxu6GkJ%2FEHiKKdtXg9M7k7HLZwThuhzxv2H3PsvcRnMxv8gPfoLESewDNhqskFCi7t%2FytYqYddMvAb61hx9luv8%2BaQhbyvSq2QYxpWBWS%2B%2B2d9jVgKuWT7zxPJdrZ89jD19ZhQC7l8UZMMmAjr0GOqUBzdCXs%2FN69TUG7JKUjKkYKc0wOFhZ4ah%2FpTz6dKYE2w6pkzTY3Wrkt9NnY0aasgBobudR6vJerfkwAqAOYVS4g8rkuwanDkXXya0NB5mZQkyfZAvEyVD%2FVqr%2BaBsD9%2BkL51tn4XRhLcTb7YUUsfn10nARbTsRwDEtkiN0JheXa6uwLOJYCN%2FvNfcIOCWH3NI4q6Tr9c1TY9i3gF2GdUZc8ueW6hMP&X-Amz-Signature=876347dceade6e4d27eacedab88113b4bf4ec9cf8e0ee5b58267b726009d0264&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XZACTKQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQDk9c94FtPHTleDbWbHdyar213NUApygKOTfqeLGOsU1wIgafXh7BQ5u%2Bja%2BR21L71YCYjpwjcHe7UT8QMc0Sh653Uq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDBoetxPt2smh9K1U4ircA7Tnb9C5KjGDiruPfioab%2F8X%2Bql%2BrgABqNyhLb2JJmTyQ2KmOtQfvc4Las%2BsYvVv4%2Fzq6y4Di4hnc4iZZr1iWh2fkp3r7vdpTKJ2B6AXg4CgU5fF2CtMCtOXj%2BoJwYYLRZ%2BQ1FUv5eRgaJn38OwlkBVD3w8mZPQwioLa8JdE7PcXEb1DtJoVH3AeCD9rVx%2FyXWEFsW6ad2mDhgPeSXlXHBwQ0S1qV2DC9j9emlB07M6KvbCL4OjRGm%2Be0O1k9Y83h1qt1nVQooRQ4ngmJRzzX7ipAwYqf2FathY9hAi4RHZ2BLXUTq85GRX5JFEWHy87iuOSGRO7xUzfuTtisCM%2FI7LgxOQXwcXlyuB1XjL%2BrXhDqHfsBMcp1bh1O2Z%2Ff7MyP7NJfnGUyVi8odbD6V7xkqknkqHILIrkBvRzg48CVo3llTfcdOo32Oem8AnJkG9H26KkQ7Jmzv%2ByyMWDg6ujXPFtYET1vFh9Na2PAGklQ9OXIpMLUd7hiArci5slB8AMMeyhrZtpnNmVk8f52igPd5EReuZmm%2BknvdfEQ5HJHyMLqJCgzlYot4o1BQ7So5qVVAWYpNjMJuznVzWT4UOenmRK4vxXEXEJ1%2B42pLRHzO2OA1i9uEuag53e70LfMMmAjr0GOqUBheXaKIE7U8NLCyQTd62eiwBXFggsBAgCdJLCWRGpa5NTAknD98s%2FilNAsdG1EyGCeo3xMisuy8q%2BU0LcHGbZu%2Bwm8608PJ7GBK6CAftQSbfAT33qMtottg3prHxpzsXaCOVr2Rmhnm3MdYunbkIfCMBBnOF4dfxdEPn1s26SECYUjcVu4YRPqBvc5qGm6FaJfrv7eDq3hBh8C4IMWEq01kM6HEmt&X-Amz-Signature=0dee9a9f8b4b37c11dba54d78451146fb0ea70c70efa62cecb02345983f3d826&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S47TZDNM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIHg94IXxJO9xQ%2Ba02dKLQPKATjJf8ngbO4vYqZ%2FbZ%2F%2BxAiEAuvOs6PvZyIR83S2mjGaBMsO%2FW8KmFxST%2F8uCMz8FOUsq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDJjBx%2BMxAJKo3M1UICrcAxmzgrSiUmyKvVlL4nqH7DR2tVk%2F0NBxHCl4IKPvAeUFthvdRlkANwSKiCmuayyTp0pm2BQrXz9fIbU12CXw2hVFbhaGOfZ7OtakpMW0Dj6SbT291MFaoyyI86cgeOJLStYhUvhrFYlh4hbLJdpi%2BlyFyg0tndUXcDZaeRCi8UY%2Fo2wOeis%2FtAmODuvlodPb7yedJzRSTYRcdys1l6UGtsZFCEQY1RP9U8P8lWro73mJYW6%2B1lQBRCe29Veli7Vn%2B%2BQDGBUczEMYNB8uZZAuUwgSHCoCqwUElbmV0NPpLJChoilBIH2tTXnGUBXPR1pVw2qyfKMDpZpuAl1oGEzvtXVd3NO633Oo1TmLMFVhoEDFyAOTGFUef5cz%2BUMoRjbpLzTWE%2BlEIJARSO%2F2JBhJLCQV1VkFo%2Byd0wPSXpvo8ZCpJggMEnspuQe8Dna1fK5GPUWNZukTysnaqyZyvhNtNgvz4oWq77UxLQTe0ilJGssyYp6RPmXEyhRI8NSUB1NZ%2BZqUL%2B4oBj%2Fssv2CDNLuHDGgmDj1PbIoZsEjhyvLOqTl%2B3w4HQ4s%2BKN3qwQI2reeLpAHKAlbhbGb0vjVqkz3rVfI5S60Kynt6SVCbKM92Ly6A1xJxNCMMJRBevABMKedjr0GOqUBqnf5iZa9uqY5tzdo19eCLEfW9sdpuI%2FQgH2VqCN5UhXK92FU%2BwRjkZhtS3S%2Bar2FTdUgua1UllU1lNXMhs%2BGmkx2vBpeSI03xh%2F18punWvB5AIOLaAPVJA3RdhHFoHzXJk67eLd6MUHmXRtQ7Wqmzya70kJfrBG6VOn8QQ%2FtvlZMKQ3NfIk7asteNtNrSP3m1EsJftgATGfYh7uVHlsMeRYKqtdP&X-Amz-Signature=480b9c819672de5f71292917c5751ad03dfb91a02a5712b46461f3b0f76b0e33&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S47TZDNM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIHg94IXxJO9xQ%2Ba02dKLQPKATjJf8ngbO4vYqZ%2FbZ%2F%2BxAiEAuvOs6PvZyIR83S2mjGaBMsO%2FW8KmFxST%2F8uCMz8FOUsq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDJjBx%2BMxAJKo3M1UICrcAxmzgrSiUmyKvVlL4nqH7DR2tVk%2F0NBxHCl4IKPvAeUFthvdRlkANwSKiCmuayyTp0pm2BQrXz9fIbU12CXw2hVFbhaGOfZ7OtakpMW0Dj6SbT291MFaoyyI86cgeOJLStYhUvhrFYlh4hbLJdpi%2BlyFyg0tndUXcDZaeRCi8UY%2Fo2wOeis%2FtAmODuvlodPb7yedJzRSTYRcdys1l6UGtsZFCEQY1RP9U8P8lWro73mJYW6%2B1lQBRCe29Veli7Vn%2B%2BQDGBUczEMYNB8uZZAuUwgSHCoCqwUElbmV0NPpLJChoilBIH2tTXnGUBXPR1pVw2qyfKMDpZpuAl1oGEzvtXVd3NO633Oo1TmLMFVhoEDFyAOTGFUef5cz%2BUMoRjbpLzTWE%2BlEIJARSO%2F2JBhJLCQV1VkFo%2Byd0wPSXpvo8ZCpJggMEnspuQe8Dna1fK5GPUWNZukTysnaqyZyvhNtNgvz4oWq77UxLQTe0ilJGssyYp6RPmXEyhRI8NSUB1NZ%2BZqUL%2B4oBj%2Fssv2CDNLuHDGgmDj1PbIoZsEjhyvLOqTl%2B3w4HQ4s%2BKN3qwQI2reeLpAHKAlbhbGb0vjVqkz3rVfI5S60Kynt6SVCbKM92Ly6A1xJxNCMMJRBevABMKedjr0GOqUBqnf5iZa9uqY5tzdo19eCLEfW9sdpuI%2FQgH2VqCN5UhXK92FU%2BwRjkZhtS3S%2Bar2FTdUgua1UllU1lNXMhs%2BGmkx2vBpeSI03xh%2F18punWvB5AIOLaAPVJA3RdhHFoHzXJk67eLd6MUHmXRtQ7Wqmzya70kJfrBG6VOn8QQ%2FtvlZMKQ3NfIk7asteNtNrSP3m1EsJftgATGfYh7uVHlsMeRYKqtdP&X-Amz-Signature=dc37e72c4396295e967a881ff26a23b3268c17efdacb61eb13ad8eaea15c4a32&X-Amz-SignedHeaders=host&x-id=GetObject)

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
