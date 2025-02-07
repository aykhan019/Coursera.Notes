

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMBOWO53%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCleL9HG1Zd1d1%2FVpCj9Etkx0Il7q27Rtq3Mq0TNxpKxAIgMlY%2Fsz52NxCQmZIi5sI08hVagmV46Tss4WXHZN%2Fm1rQq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBWvUt%2BplhRj%2FQYEmCrcA1j2TxweLutSjUKJDaKVQQa7ftI44HVLacpr091fxOLGOB7%2BMK7cSPEHXK6Ii8X%2F%2BtDjFYdgIitdw32oBOrhx3QAUgIdzBF16beowv6Ewr5z5Y%2F0ASqjjfYUgWKoWvK%2FJIw2wSTigXFfSXEMwBhNomcM7dSlND8PBsSQCnq1O5ZcFv6M5d72w0gxY9BqJL%2FgX5HJu7OrFDwMI2CnisHFBlpVgm4mihNHBLmRpSziufTDJutYpkFDmmUDNiYHUiZZHi8hwdtzPXeZdYOz0GyQ9P%2BAnUXtUuiZrGs6aAtt2cQFzzTE88E%2Fo9gY35WVZH1q1sSCXjJ1sfoEqbhHKHN0MZdeqHQiGBwyLKXGvuD1m75UEfBHVzs2QxSywJQSTwZjwjnuMqFOVZS5M1EjRYNDUyLtLye7bMznCcWLN91CYDBx93divD4o8uirvZLEmT5YI1kAyhYoVYNjJeS4ePV9ToVF7nb%2BlVnXm3zLJ8De1Hj6jMGx%2B2oGvRoPr1lZhSELzyfGaEDlSrK%2BSW2NwOouFzufvnG4pNZ%2BDcBz8Gz1Jg5eIMie4xPhB%2BBBiy2bvpHoFzdoi7XE0CTn77U7oQVi8joHPwfdv7Uzw%2Fg7y%2Ff6hsb%2FGp7AFhQDmO0SRyOtMJT8mL0GOqUBFcE5I%2BahCtrBXozb7IrT6rOu%2Bv%2BRuKQZFDvAm%2BfstD5EoJWyQXOEBIJMFxO5pMvtVnDrUCkziZj%2F%2FUhhc%2F566vHDafAuNN6Zwb95x4a6qlYJREI9okMxUQwFlx5ZmFL0gX9UtYA2BSuik8TN4uRn%2Buf%2BupyKX2wCxzZCp9w5m57THEpTb9X6fN4cj%2BkHbc7U10xpW3YM1wl2MJ6S85k20yK84gnc&X-Amz-Signature=812e1f5829b96f8360634262ac8d0f55c50e9cba7c782c3e2a60ffecaad3f972&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMBOWO53%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCleL9HG1Zd1d1%2FVpCj9Etkx0Il7q27Rtq3Mq0TNxpKxAIgMlY%2Fsz52NxCQmZIi5sI08hVagmV46Tss4WXHZN%2Fm1rQq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBWvUt%2BplhRj%2FQYEmCrcA1j2TxweLutSjUKJDaKVQQa7ftI44HVLacpr091fxOLGOB7%2BMK7cSPEHXK6Ii8X%2F%2BtDjFYdgIitdw32oBOrhx3QAUgIdzBF16beowv6Ewr5z5Y%2F0ASqjjfYUgWKoWvK%2FJIw2wSTigXFfSXEMwBhNomcM7dSlND8PBsSQCnq1O5ZcFv6M5d72w0gxY9BqJL%2FgX5HJu7OrFDwMI2CnisHFBlpVgm4mihNHBLmRpSziufTDJutYpkFDmmUDNiYHUiZZHi8hwdtzPXeZdYOz0GyQ9P%2BAnUXtUuiZrGs6aAtt2cQFzzTE88E%2Fo9gY35WVZH1q1sSCXjJ1sfoEqbhHKHN0MZdeqHQiGBwyLKXGvuD1m75UEfBHVzs2QxSywJQSTwZjwjnuMqFOVZS5M1EjRYNDUyLtLye7bMznCcWLN91CYDBx93divD4o8uirvZLEmT5YI1kAyhYoVYNjJeS4ePV9ToVF7nb%2BlVnXm3zLJ8De1Hj6jMGx%2B2oGvRoPr1lZhSELzyfGaEDlSrK%2BSW2NwOouFzufvnG4pNZ%2BDcBz8Gz1Jg5eIMie4xPhB%2BBBiy2bvpHoFzdoi7XE0CTn77U7oQVi8joHPwfdv7Uzw%2Fg7y%2Ff6hsb%2FGp7AFhQDmO0SRyOtMJT8mL0GOqUBFcE5I%2BahCtrBXozb7IrT6rOu%2Bv%2BRuKQZFDvAm%2BfstD5EoJWyQXOEBIJMFxO5pMvtVnDrUCkziZj%2F%2FUhhc%2F566vHDafAuNN6Zwb95x4a6qlYJREI9okMxUQwFlx5ZmFL0gX9UtYA2BSuik8TN4uRn%2Buf%2BupyKX2wCxzZCp9w5m57THEpTb9X6fN4cj%2BkHbc7U10xpW3YM1wl2MJ6S85k20yK84gnc&X-Amz-Signature=7a45a9bfb769c6287a1f971c22aea8890a46a5d334e17636b1ea419ccf3075f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMBOWO53%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCleL9HG1Zd1d1%2FVpCj9Etkx0Il7q27Rtq3Mq0TNxpKxAIgMlY%2Fsz52NxCQmZIi5sI08hVagmV46Tss4WXHZN%2Fm1rQq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBWvUt%2BplhRj%2FQYEmCrcA1j2TxweLutSjUKJDaKVQQa7ftI44HVLacpr091fxOLGOB7%2BMK7cSPEHXK6Ii8X%2F%2BtDjFYdgIitdw32oBOrhx3QAUgIdzBF16beowv6Ewr5z5Y%2F0ASqjjfYUgWKoWvK%2FJIw2wSTigXFfSXEMwBhNomcM7dSlND8PBsSQCnq1O5ZcFv6M5d72w0gxY9BqJL%2FgX5HJu7OrFDwMI2CnisHFBlpVgm4mihNHBLmRpSziufTDJutYpkFDmmUDNiYHUiZZHi8hwdtzPXeZdYOz0GyQ9P%2BAnUXtUuiZrGs6aAtt2cQFzzTE88E%2Fo9gY35WVZH1q1sSCXjJ1sfoEqbhHKHN0MZdeqHQiGBwyLKXGvuD1m75UEfBHVzs2QxSywJQSTwZjwjnuMqFOVZS5M1EjRYNDUyLtLye7bMznCcWLN91CYDBx93divD4o8uirvZLEmT5YI1kAyhYoVYNjJeS4ePV9ToVF7nb%2BlVnXm3zLJ8De1Hj6jMGx%2B2oGvRoPr1lZhSELzyfGaEDlSrK%2BSW2NwOouFzufvnG4pNZ%2BDcBz8Gz1Jg5eIMie4xPhB%2BBBiy2bvpHoFzdoi7XE0CTn77U7oQVi8joHPwfdv7Uzw%2Fg7y%2Ff6hsb%2FGp7AFhQDmO0SRyOtMJT8mL0GOqUBFcE5I%2BahCtrBXozb7IrT6rOu%2Bv%2BRuKQZFDvAm%2BfstD5EoJWyQXOEBIJMFxO5pMvtVnDrUCkziZj%2F%2FUhhc%2F566vHDafAuNN6Zwb95x4a6qlYJREI9okMxUQwFlx5ZmFL0gX9UtYA2BSuik8TN4uRn%2Buf%2BupyKX2wCxzZCp9w5m57THEpTb9X6fN4cj%2BkHbc7U10xpW3YM1wl2MJ6S85k20yK84gnc&X-Amz-Signature=9f93f0e47be4cfbdde2375e3d83f698508472c1bd21ca678194cbf43230edee2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YWTDPZ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC%2BVgxTLj9FOmYl5idPfXkoN3W7pHFMN7DWexxRmrkW5QIhAKel1z%2F2gN9CivLF%2Frcd9lq1BeuGDVO8pWxnqLqgLgIrKv8DCHoQABoMNjM3NDIzMTgzODA1IgwrrA2IVZ8hJnpE5gIq3APxgKw1OZVazB3dp1J2qZ4BBBn0WudiqqwsUFO5dxKjd8j2uCnEjs1FYkXZXyKtTwLOZuwo9DlnxQrCVLmFV2nU4PoZTynX%2FdrXls%2BiGdjqzo0Db9c8W4GiBy%2FRXaE2tEPo7csjOOcLQYLdp09IXGQTW%2BkN5z8mA%2F2pZ03SFnn3iq10FSNKMBFUEHhxAzMMJ1IT5UZSJ9a74qjpaHAHthwIqhhJtBPTm8ttVcDwJT0SP11Si0Jgtp8Y77ICaR6SFfU3Gf10fsyOqmEoFZmJE5DtgY5LzRmXtZaDnqwnkXXPFbcZ00pERqAAFf%2BAZjbeGS5%2FBQVRbVzBZXtgTm1icFQaKINrtf30FUAZMg%2BQH6p8kZsgh51t3EWgp5AT1%2B9ZexqlnhzR2RduMtHaL1GhZN9EBpjAZv8Fei%2Fu4ZfvCxkSLW9Lr1xpxl6asTutrLiXEY0NFCd7zrOexqJ4GJ3UQaYCyud9TBpQ85GuutPm%2Bg7%2BZqjiUUIRzZw1%2F0OXDgIR996NdJsnO582ZZpTiVFMm0ozbtsNIpDBSlw0KWbw%2Bl35FWqm4p0pnrqUUZy45RG77zNtIPno6UaBTETNwh87J7QEqTe7op7uczjlyMwQPLFAbkFoHVgfcw7zfJbcvTDX%2B5i9BjqkARurYHGFkH%2FcnMX3E3oPahDI1I0R5p7r0OYEedDxLL4q8WdHzbyf0cLYpGvptc1lsbGyxI8tILgFcCVQ8HcdLph%2Bk8rYB8faf5ol%2Bita2tM4Xp%2B%2BhuKzXB3H%2Fdo%2B5KObxXSk48ly41JMoXHEXMNp8jjWfX8zfu2H98KzZPF%2FsPBfBtUZnwkVdjSyJIhT1xwktIZv110L1z3QJ%2FNqSYw50KNvnGAb&X-Amz-Signature=01c4d61a69354cc6be141a7e140885f28cb13992ce5b23614b06d1cd93eeed95&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YWTDPZ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC%2BVgxTLj9FOmYl5idPfXkoN3W7pHFMN7DWexxRmrkW5QIhAKel1z%2F2gN9CivLF%2Frcd9lq1BeuGDVO8pWxnqLqgLgIrKv8DCHoQABoMNjM3NDIzMTgzODA1IgwrrA2IVZ8hJnpE5gIq3APxgKw1OZVazB3dp1J2qZ4BBBn0WudiqqwsUFO5dxKjd8j2uCnEjs1FYkXZXyKtTwLOZuwo9DlnxQrCVLmFV2nU4PoZTynX%2FdrXls%2BiGdjqzo0Db9c8W4GiBy%2FRXaE2tEPo7csjOOcLQYLdp09IXGQTW%2BkN5z8mA%2F2pZ03SFnn3iq10FSNKMBFUEHhxAzMMJ1IT5UZSJ9a74qjpaHAHthwIqhhJtBPTm8ttVcDwJT0SP11Si0Jgtp8Y77ICaR6SFfU3Gf10fsyOqmEoFZmJE5DtgY5LzRmXtZaDnqwnkXXPFbcZ00pERqAAFf%2BAZjbeGS5%2FBQVRbVzBZXtgTm1icFQaKINrtf30FUAZMg%2BQH6p8kZsgh51t3EWgp5AT1%2B9ZexqlnhzR2RduMtHaL1GhZN9EBpjAZv8Fei%2Fu4ZfvCxkSLW9Lr1xpxl6asTutrLiXEY0NFCd7zrOexqJ4GJ3UQaYCyud9TBpQ85GuutPm%2Bg7%2BZqjiUUIRzZw1%2F0OXDgIR996NdJsnO582ZZpTiVFMm0ozbtsNIpDBSlw0KWbw%2Bl35FWqm4p0pnrqUUZy45RG77zNtIPno6UaBTETNwh87J7QEqTe7op7uczjlyMwQPLFAbkFoHVgfcw7zfJbcvTDX%2B5i9BjqkARurYHGFkH%2FcnMX3E3oPahDI1I0R5p7r0OYEedDxLL4q8WdHzbyf0cLYpGvptc1lsbGyxI8tILgFcCVQ8HcdLph%2Bk8rYB8faf5ol%2Bita2tM4Xp%2B%2BhuKzXB3H%2Fdo%2B5KObxXSk48ly41JMoXHEXMNp8jjWfX8zfu2H98KzZPF%2FsPBfBtUZnwkVdjSyJIhT1xwktIZv110L1z3QJ%2FNqSYw50KNvnGAb&X-Amz-Signature=9d59ddfaeff6d4b2730b4c8abae454bb5bf4b8368dc0c3472d02384994621baf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YWTDPZ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC%2BVgxTLj9FOmYl5idPfXkoN3W7pHFMN7DWexxRmrkW5QIhAKel1z%2F2gN9CivLF%2Frcd9lq1BeuGDVO8pWxnqLqgLgIrKv8DCHoQABoMNjM3NDIzMTgzODA1IgwrrA2IVZ8hJnpE5gIq3APxgKw1OZVazB3dp1J2qZ4BBBn0WudiqqwsUFO5dxKjd8j2uCnEjs1FYkXZXyKtTwLOZuwo9DlnxQrCVLmFV2nU4PoZTynX%2FdrXls%2BiGdjqzo0Db9c8W4GiBy%2FRXaE2tEPo7csjOOcLQYLdp09IXGQTW%2BkN5z8mA%2F2pZ03SFnn3iq10FSNKMBFUEHhxAzMMJ1IT5UZSJ9a74qjpaHAHthwIqhhJtBPTm8ttVcDwJT0SP11Si0Jgtp8Y77ICaR6SFfU3Gf10fsyOqmEoFZmJE5DtgY5LzRmXtZaDnqwnkXXPFbcZ00pERqAAFf%2BAZjbeGS5%2FBQVRbVzBZXtgTm1icFQaKINrtf30FUAZMg%2BQH6p8kZsgh51t3EWgp5AT1%2B9ZexqlnhzR2RduMtHaL1GhZN9EBpjAZv8Fei%2Fu4ZfvCxkSLW9Lr1xpxl6asTutrLiXEY0NFCd7zrOexqJ4GJ3UQaYCyud9TBpQ85GuutPm%2Bg7%2BZqjiUUIRzZw1%2F0OXDgIR996NdJsnO582ZZpTiVFMm0ozbtsNIpDBSlw0KWbw%2Bl35FWqm4p0pnrqUUZy45RG77zNtIPno6UaBTETNwh87J7QEqTe7op7uczjlyMwQPLFAbkFoHVgfcw7zfJbcvTDX%2B5i9BjqkARurYHGFkH%2FcnMX3E3oPahDI1I0R5p7r0OYEedDxLL4q8WdHzbyf0cLYpGvptc1lsbGyxI8tILgFcCVQ8HcdLph%2Bk8rYB8faf5ol%2Bita2tM4Xp%2B%2BhuKzXB3H%2Fdo%2B5KObxXSk48ly41JMoXHEXMNp8jjWfX8zfu2H98KzZPF%2FsPBfBtUZnwkVdjSyJIhT1xwktIZv110L1z3QJ%2FNqSYw50KNvnGAb&X-Amz-Signature=701fd3bb7df7e95fe210e595b7bcd73f9087ab9a27187d36729d2363eb1e8165&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YWTDPZ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC%2BVgxTLj9FOmYl5idPfXkoN3W7pHFMN7DWexxRmrkW5QIhAKel1z%2F2gN9CivLF%2Frcd9lq1BeuGDVO8pWxnqLqgLgIrKv8DCHoQABoMNjM3NDIzMTgzODA1IgwrrA2IVZ8hJnpE5gIq3APxgKw1OZVazB3dp1J2qZ4BBBn0WudiqqwsUFO5dxKjd8j2uCnEjs1FYkXZXyKtTwLOZuwo9DlnxQrCVLmFV2nU4PoZTynX%2FdrXls%2BiGdjqzo0Db9c8W4GiBy%2FRXaE2tEPo7csjOOcLQYLdp09IXGQTW%2BkN5z8mA%2F2pZ03SFnn3iq10FSNKMBFUEHhxAzMMJ1IT5UZSJ9a74qjpaHAHthwIqhhJtBPTm8ttVcDwJT0SP11Si0Jgtp8Y77ICaR6SFfU3Gf10fsyOqmEoFZmJE5DtgY5LzRmXtZaDnqwnkXXPFbcZ00pERqAAFf%2BAZjbeGS5%2FBQVRbVzBZXtgTm1icFQaKINrtf30FUAZMg%2BQH6p8kZsgh51t3EWgp5AT1%2B9ZexqlnhzR2RduMtHaL1GhZN9EBpjAZv8Fei%2Fu4ZfvCxkSLW9Lr1xpxl6asTutrLiXEY0NFCd7zrOexqJ4GJ3UQaYCyud9TBpQ85GuutPm%2Bg7%2BZqjiUUIRzZw1%2F0OXDgIR996NdJsnO582ZZpTiVFMm0ozbtsNIpDBSlw0KWbw%2Bl35FWqm4p0pnrqUUZy45RG77zNtIPno6UaBTETNwh87J7QEqTe7op7uczjlyMwQPLFAbkFoHVgfcw7zfJbcvTDX%2B5i9BjqkARurYHGFkH%2FcnMX3E3oPahDI1I0R5p7r0OYEedDxLL4q8WdHzbyf0cLYpGvptc1lsbGyxI8tILgFcCVQ8HcdLph%2Bk8rYB8faf5ol%2Bita2tM4Xp%2B%2BhuKzXB3H%2Fdo%2B5KObxXSk48ly41JMoXHEXMNp8jjWfX8zfu2H98KzZPF%2FsPBfBtUZnwkVdjSyJIhT1xwktIZv110L1z3QJ%2FNqSYw50KNvnGAb&X-Amz-Signature=b1bad6fb6b17aa5e1518c45c863243a36f8a33788ab95b87676196b1e06db876&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YWTDPZ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC%2BVgxTLj9FOmYl5idPfXkoN3W7pHFMN7DWexxRmrkW5QIhAKel1z%2F2gN9CivLF%2Frcd9lq1BeuGDVO8pWxnqLqgLgIrKv8DCHoQABoMNjM3NDIzMTgzODA1IgwrrA2IVZ8hJnpE5gIq3APxgKw1OZVazB3dp1J2qZ4BBBn0WudiqqwsUFO5dxKjd8j2uCnEjs1FYkXZXyKtTwLOZuwo9DlnxQrCVLmFV2nU4PoZTynX%2FdrXls%2BiGdjqzo0Db9c8W4GiBy%2FRXaE2tEPo7csjOOcLQYLdp09IXGQTW%2BkN5z8mA%2F2pZ03SFnn3iq10FSNKMBFUEHhxAzMMJ1IT5UZSJ9a74qjpaHAHthwIqhhJtBPTm8ttVcDwJT0SP11Si0Jgtp8Y77ICaR6SFfU3Gf10fsyOqmEoFZmJE5DtgY5LzRmXtZaDnqwnkXXPFbcZ00pERqAAFf%2BAZjbeGS5%2FBQVRbVzBZXtgTm1icFQaKINrtf30FUAZMg%2BQH6p8kZsgh51t3EWgp5AT1%2B9ZexqlnhzR2RduMtHaL1GhZN9EBpjAZv8Fei%2Fu4ZfvCxkSLW9Lr1xpxl6asTutrLiXEY0NFCd7zrOexqJ4GJ3UQaYCyud9TBpQ85GuutPm%2Bg7%2BZqjiUUIRzZw1%2F0OXDgIR996NdJsnO582ZZpTiVFMm0ozbtsNIpDBSlw0KWbw%2Bl35FWqm4p0pnrqUUZy45RG77zNtIPno6UaBTETNwh87J7QEqTe7op7uczjlyMwQPLFAbkFoHVgfcw7zfJbcvTDX%2B5i9BjqkARurYHGFkH%2FcnMX3E3oPahDI1I0R5p7r0OYEedDxLL4q8WdHzbyf0cLYpGvptc1lsbGyxI8tILgFcCVQ8HcdLph%2Bk8rYB8faf5ol%2Bita2tM4Xp%2B%2BhuKzXB3H%2Fdo%2B5KObxXSk48ly41JMoXHEXMNp8jjWfX8zfu2H98KzZPF%2FsPBfBtUZnwkVdjSyJIhT1xwktIZv110L1z3QJ%2FNqSYw50KNvnGAb&X-Amz-Signature=05775a00aeb3ec0f534dc5e6f40ce7253a49fdbc492885508ee437a18b112138&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YWTDPZ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC%2BVgxTLj9FOmYl5idPfXkoN3W7pHFMN7DWexxRmrkW5QIhAKel1z%2F2gN9CivLF%2Frcd9lq1BeuGDVO8pWxnqLqgLgIrKv8DCHoQABoMNjM3NDIzMTgzODA1IgwrrA2IVZ8hJnpE5gIq3APxgKw1OZVazB3dp1J2qZ4BBBn0WudiqqwsUFO5dxKjd8j2uCnEjs1FYkXZXyKtTwLOZuwo9DlnxQrCVLmFV2nU4PoZTynX%2FdrXls%2BiGdjqzo0Db9c8W4GiBy%2FRXaE2tEPo7csjOOcLQYLdp09IXGQTW%2BkN5z8mA%2F2pZ03SFnn3iq10FSNKMBFUEHhxAzMMJ1IT5UZSJ9a74qjpaHAHthwIqhhJtBPTm8ttVcDwJT0SP11Si0Jgtp8Y77ICaR6SFfU3Gf10fsyOqmEoFZmJE5DtgY5LzRmXtZaDnqwnkXXPFbcZ00pERqAAFf%2BAZjbeGS5%2FBQVRbVzBZXtgTm1icFQaKINrtf30FUAZMg%2BQH6p8kZsgh51t3EWgp5AT1%2B9ZexqlnhzR2RduMtHaL1GhZN9EBpjAZv8Fei%2Fu4ZfvCxkSLW9Lr1xpxl6asTutrLiXEY0NFCd7zrOexqJ4GJ3UQaYCyud9TBpQ85GuutPm%2Bg7%2BZqjiUUIRzZw1%2F0OXDgIR996NdJsnO582ZZpTiVFMm0ozbtsNIpDBSlw0KWbw%2Bl35FWqm4p0pnrqUUZy45RG77zNtIPno6UaBTETNwh87J7QEqTe7op7uczjlyMwQPLFAbkFoHVgfcw7zfJbcvTDX%2B5i9BjqkARurYHGFkH%2FcnMX3E3oPahDI1I0R5p7r0OYEedDxLL4q8WdHzbyf0cLYpGvptc1lsbGyxI8tILgFcCVQ8HcdLph%2Bk8rYB8faf5ol%2Bita2tM4Xp%2B%2BhuKzXB3H%2Fdo%2B5KObxXSk48ly41JMoXHEXMNp8jjWfX8zfu2H98KzZPF%2FsPBfBtUZnwkVdjSyJIhT1xwktIZv110L1z3QJ%2FNqSYw50KNvnGAb&X-Amz-Signature=83a72ce9764d655e593ee77047540ef6b26b53c519132d53ffb6d0e93d0b1939&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX2HIIUC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQChBbWSiWqizfdiDEpWU50wyNWJLLa7TB6Q4cGKrxhk7wIhAJ9bTRF3BahBddoTrxeX1ZA%2BGqqlR4z5gT9byNJwDG04Kv8DCHoQABoMNjM3NDIzMTgzODA1IgyvmVg4F9so8lqu2rAq3ANbtpZISy70SuNn3NannwMbSfkus55hMCF6NCa2ez8CEkuHmmWCq1QRBFfqwKdXwbmrfx3a1wb2gh18kPho5w%2BlzpYKj8lQtOssc0nVA4y4CdORsQrePhDxkgnO8Pr3cZ4sLbCfWVuciWG5rHmBC5b5epGXxo2VTfvvnf4dbH9NS8b6XuIiKHTCbBouBe%2Bk50BGmZMU6B%2F1%2FzK%2BxLJaaIR31qVlyya%2FWPx9IVwKq0wKmp9c1U1Ma%2B2mwiEY3XmxtdPY%2F1UjAeKVFiUX2DKzwE7GK%2BXwJ2AegtgXUcjt2fmFF3l2k%2BE4hytYM12mx0jjHoRVIfC78%2FTP%2F1xACt1RMkYvmjINcaUJEeAOKhsBk%2Fza0DE3IIc8Wr1soH0JBinIMa4VC7wN8tOLZwTD3Fb5KuH2h5kwfJz3%2BHP%2Fl%2FQ5g8ohGAxbTPQuKTnL0zcvCid5Hi1bfuy%2BUf61XiZB2S3mRC6Acxk5JV7HGR4xVaDYjMV87gKdXd5hYBB8GaXarMuQ%2BvK%2FL8Vuf3n%2B4kWHCZDCb3r3zIfR8IhQZhtlJwpkDsKRvqIGgK%2Fe3TLm%2BBMd%2FUrCvL2m7luXhwK9ffp67M%2BpV6ahvvs7HPLngL7OYZoOTkSPIWmw4sfKOh7fQVK%2BQzCy%2FJi9BjqkASNFpw0OpXasyujNKs3dQFTxYXu4dasFz%2BbNuF5WdYiXYTT4KLttTs5mbg8D%2FjHy11ex%2FmBc7Fz9Cz1zEK0JjpHNJ60OInNAYPa%2B5AMKRtNS5zDm2dwFycwkR4A%2BVmIGT5fdIYkI5IlEFwdPPOlAAGYcrKwEkzWOU%2BN15eOtFtnwAyJu48F7NmuA2ZYUQeNJNujVReILTQPXK0WZk5Xm85f6OYL1&X-Amz-Signature=fab143549b1a7a464a8ac3f9b27e87fd04a018964254cfcaf01cf6a764aa974c&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMLEYZVT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCCZRrhhEJbtOmHP7VvUPhR%2FNtdQ7p79VN8EWt8rIFKEgIhAJ07V1KjTW8G%2BUo4kWPbsrzODMPsg6my%2F5QELJpeJV5sKv8DCHoQABoMNjM3NDIzMTgzODA1Igz8%2FDZGciMOocARO40q3APmamt9eD3Fo99fWOePxQFxMT0%2B09BNNT4gPwQgbzGS4ieQ2KpLVTWIsFhYTgO0%2FVzDpkV5jKPu2CeERgeTvDm8cKfHm6jyfeg%2BIHxfOtjF6qF%2BLwynx3NiIGay8%2FFaiJFGttmVJQ1deAxY3SC2dZFCKBd2GMWUtGdo%2Fs%2Bo%2F9JS8B8CJPzGS07nDS%2F1NuJWcpAK5ifyaejD%2FHoo50oNzFECKatfrLLkiYfI3ZBEwt4LBU3kp9J%2BAwptrNg5iei9Y%2BPuXVhS9RV1eK8%2BdvTtfCVpCVJBq0KBDHXhfim%2F9onZTPt1%2BMk0Uc8OokmBV67RzHgrz4cuXi7%2BnwWxfLQl76FCDHCPORCx9lLtFVoOi9IHIDJQNLq%2BBHHhIbXKWtI9tHIjWaoW9LQmlVYzFVlD%2Fbpca%2FY3%2Fz8MC%2FqDMEQnD0BNR8NNsfGkLVkTOr3SAPrr4V2xQR9gEBpiCgwmch5lIntecSqc4fCw0zJieU0W61QE3eDAOhQrG2JIKAoSelaax79QIeMDiMLQi5%2BGGlY3%2FGebd1n0KOb20YdTi2Xft9xOd8oOGCp%2BO3CbceaUS22eKEc96%2BN58uzJYQIc6zuJfDFunS4g2oG7fb4P2pCPtU62cOwBMSRhh%2Bg5%2B3EdvTCE%2FJi9BjqkAaOc1GV8zTLZaAm2dqyaXlSkoeTrXTWJgwC9Fq8jAdJ1JMYGp%2BVm4L4guPTFBRMXJgoDExXHcWE36F6erGVdj7mui33LYQ56PpzqDNyp6EAoAJSvzBD0c3H1MfxXkh18K4TaVUQIE23OLfeW2Flo6IikUjx%2Fsos0X%2BySkXjUMoWkknggWF9vKQgLtp9scTFGr6FZ%2F4n6yfJJXTRX%2Bp%2BXAGpcZoHQ&X-Amz-Signature=7233d9c768de0955aeb32513c9e6a0367e1a8dbc0ba8cdfeee2ee74d4ff484f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YWTDPZ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC%2BVgxTLj9FOmYl5idPfXkoN3W7pHFMN7DWexxRmrkW5QIhAKel1z%2F2gN9CivLF%2Frcd9lq1BeuGDVO8pWxnqLqgLgIrKv8DCHoQABoMNjM3NDIzMTgzODA1IgwrrA2IVZ8hJnpE5gIq3APxgKw1OZVazB3dp1J2qZ4BBBn0WudiqqwsUFO5dxKjd8j2uCnEjs1FYkXZXyKtTwLOZuwo9DlnxQrCVLmFV2nU4PoZTynX%2FdrXls%2BiGdjqzo0Db9c8W4GiBy%2FRXaE2tEPo7csjOOcLQYLdp09IXGQTW%2BkN5z8mA%2F2pZ03SFnn3iq10FSNKMBFUEHhxAzMMJ1IT5UZSJ9a74qjpaHAHthwIqhhJtBPTm8ttVcDwJT0SP11Si0Jgtp8Y77ICaR6SFfU3Gf10fsyOqmEoFZmJE5DtgY5LzRmXtZaDnqwnkXXPFbcZ00pERqAAFf%2BAZjbeGS5%2FBQVRbVzBZXtgTm1icFQaKINrtf30FUAZMg%2BQH6p8kZsgh51t3EWgp5AT1%2B9ZexqlnhzR2RduMtHaL1GhZN9EBpjAZv8Fei%2Fu4ZfvCxkSLW9Lr1xpxl6asTutrLiXEY0NFCd7zrOexqJ4GJ3UQaYCyud9TBpQ85GuutPm%2Bg7%2BZqjiUUIRzZw1%2F0OXDgIR996NdJsnO582ZZpTiVFMm0ozbtsNIpDBSlw0KWbw%2Bl35FWqm4p0pnrqUUZy45RG77zNtIPno6UaBTETNwh87J7QEqTe7op7uczjlyMwQPLFAbkFoHVgfcw7zfJbcvTDX%2B5i9BjqkARurYHGFkH%2FcnMX3E3oPahDI1I0R5p7r0OYEedDxLL4q8WdHzbyf0cLYpGvptc1lsbGyxI8tILgFcCVQ8HcdLph%2Bk8rYB8faf5ol%2Bita2tM4Xp%2B%2BhuKzXB3H%2Fdo%2B5KObxXSk48ly41JMoXHEXMNp8jjWfX8zfu2H98KzZPF%2FsPBfBtUZnwkVdjSyJIhT1xwktIZv110L1z3QJ%2FNqSYw50KNvnGAb&X-Amz-Signature=1339a0741b0943cccba27bc20398b64591598404495886d2053a35d337d944ec&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YWTDPZ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC%2BVgxTLj9FOmYl5idPfXkoN3W7pHFMN7DWexxRmrkW5QIhAKel1z%2F2gN9CivLF%2Frcd9lq1BeuGDVO8pWxnqLqgLgIrKv8DCHoQABoMNjM3NDIzMTgzODA1IgwrrA2IVZ8hJnpE5gIq3APxgKw1OZVazB3dp1J2qZ4BBBn0WudiqqwsUFO5dxKjd8j2uCnEjs1FYkXZXyKtTwLOZuwo9DlnxQrCVLmFV2nU4PoZTynX%2FdrXls%2BiGdjqzo0Db9c8W4GiBy%2FRXaE2tEPo7csjOOcLQYLdp09IXGQTW%2BkN5z8mA%2F2pZ03SFnn3iq10FSNKMBFUEHhxAzMMJ1IT5UZSJ9a74qjpaHAHthwIqhhJtBPTm8ttVcDwJT0SP11Si0Jgtp8Y77ICaR6SFfU3Gf10fsyOqmEoFZmJE5DtgY5LzRmXtZaDnqwnkXXPFbcZ00pERqAAFf%2BAZjbeGS5%2FBQVRbVzBZXtgTm1icFQaKINrtf30FUAZMg%2BQH6p8kZsgh51t3EWgp5AT1%2B9ZexqlnhzR2RduMtHaL1GhZN9EBpjAZv8Fei%2Fu4ZfvCxkSLW9Lr1xpxl6asTutrLiXEY0NFCd7zrOexqJ4GJ3UQaYCyud9TBpQ85GuutPm%2Bg7%2BZqjiUUIRzZw1%2F0OXDgIR996NdJsnO582ZZpTiVFMm0ozbtsNIpDBSlw0KWbw%2Bl35FWqm4p0pnrqUUZy45RG77zNtIPno6UaBTETNwh87J7QEqTe7op7uczjlyMwQPLFAbkFoHVgfcw7zfJbcvTDX%2B5i9BjqkARurYHGFkH%2FcnMX3E3oPahDI1I0R5p7r0OYEedDxLL4q8WdHzbyf0cLYpGvptc1lsbGyxI8tILgFcCVQ8HcdLph%2Bk8rYB8faf5ol%2Bita2tM4Xp%2B%2BhuKzXB3H%2Fdo%2B5KObxXSk48ly41JMoXHEXMNp8jjWfX8zfu2H98KzZPF%2FsPBfBtUZnwkVdjSyJIhT1xwktIZv110L1z3QJ%2FNqSYw50KNvnGAb&X-Amz-Signature=548492d0e4fd1fb0452540e53b0cbe2f1f1fc14e0895dff92eb562799bb4f6b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YWTDPZ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC%2BVgxTLj9FOmYl5idPfXkoN3W7pHFMN7DWexxRmrkW5QIhAKel1z%2F2gN9CivLF%2Frcd9lq1BeuGDVO8pWxnqLqgLgIrKv8DCHoQABoMNjM3NDIzMTgzODA1IgwrrA2IVZ8hJnpE5gIq3APxgKw1OZVazB3dp1J2qZ4BBBn0WudiqqwsUFO5dxKjd8j2uCnEjs1FYkXZXyKtTwLOZuwo9DlnxQrCVLmFV2nU4PoZTynX%2FdrXls%2BiGdjqzo0Db9c8W4GiBy%2FRXaE2tEPo7csjOOcLQYLdp09IXGQTW%2BkN5z8mA%2F2pZ03SFnn3iq10FSNKMBFUEHhxAzMMJ1IT5UZSJ9a74qjpaHAHthwIqhhJtBPTm8ttVcDwJT0SP11Si0Jgtp8Y77ICaR6SFfU3Gf10fsyOqmEoFZmJE5DtgY5LzRmXtZaDnqwnkXXPFbcZ00pERqAAFf%2BAZjbeGS5%2FBQVRbVzBZXtgTm1icFQaKINrtf30FUAZMg%2BQH6p8kZsgh51t3EWgp5AT1%2B9ZexqlnhzR2RduMtHaL1GhZN9EBpjAZv8Fei%2Fu4ZfvCxkSLW9Lr1xpxl6asTutrLiXEY0NFCd7zrOexqJ4GJ3UQaYCyud9TBpQ85GuutPm%2Bg7%2BZqjiUUIRzZw1%2F0OXDgIR996NdJsnO582ZZpTiVFMm0ozbtsNIpDBSlw0KWbw%2Bl35FWqm4p0pnrqUUZy45RG77zNtIPno6UaBTETNwh87J7QEqTe7op7uczjlyMwQPLFAbkFoHVgfcw7zfJbcvTDX%2B5i9BjqkARurYHGFkH%2FcnMX3E3oPahDI1I0R5p7r0OYEedDxLL4q8WdHzbyf0cLYpGvptc1lsbGyxI8tILgFcCVQ8HcdLph%2Bk8rYB8faf5ol%2Bita2tM4Xp%2B%2BhuKzXB3H%2Fdo%2B5KObxXSk48ly41JMoXHEXMNp8jjWfX8zfu2H98KzZPF%2FsPBfBtUZnwkVdjSyJIhT1xwktIZv110L1z3QJ%2FNqSYw50KNvnGAb&X-Amz-Signature=7aff3ac8582d65e12d49c00fed188b9ddd4bebdf0542b6e327b4f082d10c8124&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTMYXPC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDGT9UTTbmyuWe%2BHT%2BU49i0pNJTEQnghVldWkT4JQprAgIhAKvP0it2z6MWUCGHxagkLRzRNCn44zmIH6pv6GMkDV4gKv8DCHoQABoMNjM3NDIzMTgzODA1Igx6sIrmIy%2FcyHnAtH0q3AP8vL6zW%2FNyKKcJZCinRwOyBG4biGdcOlZXtC7SVHq9ASv8%2BRraEaS5Wwm38wdazQFxgXx3X9%2BFzjDNEDs%2BzJOE%2FhBiSk9h3AIalA9P4q9bTRsbvjqU%2FYMvP%2FXH0GuFwO3oBSZneFK%2BFMkDHHxM%2FYYiOfOcMgJLjWDOG6PnMZ%2B%2Bz6C0WprvIwTxZPw3dVuXCi%2FNhHdBmrMKOhMxV%2FtFs%2F2MqjlA%2F38WUOgjJA74c6af43xHmmu%2BLQSys8X4iH%2FbAyS4c2%2Bwm5yoAgOZDKyeSpcFpjxlXid0XuZ8J4GTT6uSL11gaIRckqdTL0ZSeJjofCboO4WuCQEncPE0v8y%2FzohkrE73vrUCNyYQjmphmfL12naKas7pp8GyPoazTuX9Fj4FvAmnhfuKC7wh89GBoRzvtRWCyN3nMh9fGd9U%2FjvnvUvA0C5TkeMG0MVOgxEjv8oMKAAYyQuvJzQPGjNmKKb4cxAD4%2BGxbCWthqa%2BFZUMLaJOJ06ETVUvzzw0eGwDgAiGu2bYXDs8iUOY4JLpYfo652oNC7L0Ow9cvBlItA11JYFYJsPeZIVav5SxIi8guDS%2F8vRflC96DhapJOSAG4zBYDRyVGJp08L3FzcNJCHud0tSJogjPdt6VGtbBjCc%2FJi9BjqkAVOKvVXIqAzdTHgGr6%2FKf%2F9O%2BwBTl6R7cPa%2Fm9GO1UynmYeJfqlaccazMDtWIeM0RsgteVuS9OfWFxuJ9f9YKV7M%2Fx40TMiNt1pwejIHft9kW5yIqMbzuI3K%2FYlEhBWCYcceWLN7xmThqVpUqESiPDLYKFHyPX5%2FFW1fngKjnasmBHEvUIaZ1M%2FAxpITaE%2Fqsvz%2BYn57eq4MZrlzcoS7L%2Bw9R9oo&X-Amz-Signature=104ed745e7977bd60f3b96477837c4e715defe3c911bcb62ab7606aeb59fc629&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAMFUQP3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDN%2BvIMVLUPSAWNUluiHVj0z%2BucZs25jv%2FmIMdk0h9FvQIgXj%2FfF0lGRjPRSoG8xPnxerShcnn8XBthSTmylUz%2FO9oq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDGAXgX33%2FujZ%2BiDTlircA3hvmKcu7Hku2gI186xACQVe8x03qP6e%2Fkm8dnRy9OrnyC30NzcwiyPJczXCeKAfW8Qwb2yPreREMygnz5rwfvrZF7bahz4dVok9WjmsAFkKNPDTDQx23LK7O4ZxZcYD8tuOx3K3t2DipxG3ZSyb%2FkbDQpaiyuJ3f01yjvHXXQyjNOX3P4yUqRspSPHROiH3WuSEPuzucE9vZaWSXQysxd5Vw8g8RbeJeWTF5Sz6NXag5FYG3l0oaK1IRkgtNJrWz1wpsliLiLMQfprSPi8xiCkvHDfyVS2gMVZF4u2CYEHtDSoPeM%2F1KStBoCGTAtJh%2FS4klKD61nXh9JntGI0mxs1nZBWU5KN6SC1E8Ev28WkdSRRZlBQj4iDaW3jjQIsOxHFYQBycJoKmof0V8eJth7kJWXNuxOjUZan5STISWYeZKElw1%2FScfggnaB3OQoFeQtsD63wiRzegKQ2q52ctXhVbqyatErWVbJpABLATedZ3wjmdb37Ey3NKHkN5Bu7vfnN76nzcTIX329DOAxmgw30QcetsISnlS3EVz2%2BhncD4cUi3QHdi%2FBXWlWTVQ9KxNF8YmvApaudt2dA601eSsEM4jpXTOjJi2pbr9BcfDC%2Fyj77kVeAt1cEJLZCIMKL8mL0GOqUBPaxdWIV1LcLKvxS3tYsfS7EvsPDuHRhf7DvsADWaiKLS%2Bt3O1d%2F2wvNaXuZNe%2F9LiANGEwzIvkRb3eoy9GRuenoNb86cO%2FrPQF3bsi6ssKpO1yVvikeSx6AjEosRKsxuq7TNGt4kV5OVJ3pfLDaHjMuCPPSnnhEW0DcWWWOYOKToNYNDi3WgwIPfF1cleHO8mPqWgrw9ayvDwmABEtQR%2Fck2xIkJ&X-Amz-Signature=88d5558c9f8f5eebc5c3dc701708d684ef9f9b9d1ba9a825fa30739f028258d9&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN3665IH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCYKF%2FlvMRc%2FOqBUnsqHPki7dM2uVKZIdmR4HC2HUN5BAIgR4%2B9HXmMIw0%2F85gjhnk8wdyftAFxZDwCqHftrFQSXSMq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKC%2Bb9%2FxUpunN3L8jCrcAz3o0L3BMVK6cijcjWinax%2FWkBQ8AISStIXM0Lc9U0s4eLblxNXHFImUd3491eZCNqz3LP1wvnpDXIxSNW9mwqbpROht2UYV4Xs2Mo%2B8F8W15VRxFiPx6N3505AbN6%2BLis%2FfKbRLj2EiXLZxo6dMTCGZipfCKlPgRfD%2B8t4FZTv%2Bmq75OclPK1hrUKyurZ4F7WictS0LVS9nZnMS4MBK7asGVp2LRS0yG0C90VjaD4ZXnW505mwWY1aLZlgJH%2BftElGVu0NZQNfhhbHAb91ykaji0ab%2F2iWaVkMKB6DUZ5zUuABX3Ccy6bIT2myYiCTUerTH6RX8oealNypBks3P5ztILiyduF87Ah5%2F0DEgrWZ73S%2BpLVoCdQzSSLkK9%2F3BXNtufXr5PDLmHbSmQQc6zhN3DYOJ%2FXxZybcNz5TG7GOGDOBagscTEUDcBRsnDrb7TSxN3Jazz2kHpwZSukipsivQSg%2F9Z2OEyBiayi7%2BDoFDlei1UT52SqwQUp3FnD0kkZ%2FZfJYWMyRJwQSfjKI6frImegry8LaoTnee%2FjoI8lm2BOFsXJL6f8Jv%2FMpfLklUqQE9MZGdvSTb2tPccbPp68765AjGQWohiBxGaGzQ0CDH%2BYLLX0W%2FlzdSOBjHMOj7mL0GOqUBeer7sjdI5yQLzw3mIvHPTmbrbLNEtDm6vlg%2B5ueGwoZxh9ITun5Z%2BZJpU8hejUTAB%2BgwrghmEbiQtL5gnPfI3d07k4fPZ%2B9n7NAcgzcs6P0fHSSux%2FYSbRreN7YuLShR87FhIOSXT0l9eSoMQ7v4AfBpdufOIbdc6%2BQSsgbsKphlOss2LMQ2YsiDLK1kNwbVMefXFJnYC8r%2B2XrxU%2F5tSfISN2Mn&X-Amz-Signature=2f34680e072760756c1539cd93ab873f872a13fe04cf1f38e7c54b7041315864&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPEKALDV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDPwx9ZjCeX7w8u2GnoFtb2In8T8Hl%2FF%2BmitlKtpRlCQAIgbRLCqdmtLzWVgVSnE5pyUenWoE%2F5OjDqf%2FIsNBZNm68q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIqAsrVw4rndatLA2ircA0IN14Vxg3fVcWXGAGZ9kH1032EFNQaWoYVuo%2F8uKgbQVetPhHFUE5tEIhammkGNRH3AMv1RMp2iAYeFyceiVyOgWK6MIE7%2BJ4cduozvsak9GpYfLjs6%2F9Ahx6gfeMEKTV5XN6BX2h2laBxMargAQLue03xr4jb1TiCgbspxgJRt%2B3HBM6UvkrCicFd0QiW16iq9%2BF%2BNLpRwAYlNUQvl5u9U8D53CiRLv5ksRYDaTZUTGTPl%2B4LtOB6zea7QXSs8Ub4QVMfnxgyu7g%2Bgw8MyI%2FWg5pgP2wd4vGBxDH4HgyNqkncls8BuqNPdkriYjzS5wvFCkmJlZa7X4wHWmik9lF9nT9i8QWV7WaLrbWVQDgEf3MQrU6c%2FkOz%2FyBUPtCOc2zwQx5QZiAxdK%2BC3HitbSVBWPoUYYWvUIlVAINqvR6EdddoVfIrOGIEiR%2FJvsGfudWHxQrMzAqXaRSic25HAboZ1DTvIDHjf3Ea%2FEWCY8H8owl5%2FyzWxSg3XuSy3A9gjwgVagAbJY7F2ZZPtalM4hf8bjKSkiIN1mMdWQVswZ5ra%2BtDJNFAIeHXORIwYZPcysBsqPy%2FmjjP71X9FYpN7dfseQ%2Fbb%2FPBlx6Z1FKIQJ4Aq13A1v%2FdPCh18%2FO4mMND7mL0GOqUBrALrhmgprjmLykHgJQ%2Bn0RJZYLRpV68%2FsjwZCcrZDn4yHK1Q%2Bl89J3UI6olCERz1C6FfeuWhO21MFxFwY1VU166RTlXLmN9WyjqPV%2FyLdnAQCsfWRsi9tlgTkLm321D%2FNVsp2qq8PFEsDuM1x63URWESUsAKxrpjQv7w1ya6r8GmwabRgQHm5CALsqxC5NGcxOFxGJAl2S2xkQUTB7bx%2B45MHOk3&X-Amz-Signature=520f0995007c885abe7976aea0aa73a3288dda39fc1daa1faeecd426dd12b156&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPEKALDV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDPwx9ZjCeX7w8u2GnoFtb2In8T8Hl%2FF%2BmitlKtpRlCQAIgbRLCqdmtLzWVgVSnE5pyUenWoE%2F5OjDqf%2FIsNBZNm68q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIqAsrVw4rndatLA2ircA0IN14Vxg3fVcWXGAGZ9kH1032EFNQaWoYVuo%2F8uKgbQVetPhHFUE5tEIhammkGNRH3AMv1RMp2iAYeFyceiVyOgWK6MIE7%2BJ4cduozvsak9GpYfLjs6%2F9Ahx6gfeMEKTV5XN6BX2h2laBxMargAQLue03xr4jb1TiCgbspxgJRt%2B3HBM6UvkrCicFd0QiW16iq9%2BF%2BNLpRwAYlNUQvl5u9U8D53CiRLv5ksRYDaTZUTGTPl%2B4LtOB6zea7QXSs8Ub4QVMfnxgyu7g%2Bgw8MyI%2FWg5pgP2wd4vGBxDH4HgyNqkncls8BuqNPdkriYjzS5wvFCkmJlZa7X4wHWmik9lF9nT9i8QWV7WaLrbWVQDgEf3MQrU6c%2FkOz%2FyBUPtCOc2zwQx5QZiAxdK%2BC3HitbSVBWPoUYYWvUIlVAINqvR6EdddoVfIrOGIEiR%2FJvsGfudWHxQrMzAqXaRSic25HAboZ1DTvIDHjf3Ea%2FEWCY8H8owl5%2FyzWxSg3XuSy3A9gjwgVagAbJY7F2ZZPtalM4hf8bjKSkiIN1mMdWQVswZ5ra%2BtDJNFAIeHXORIwYZPcysBsqPy%2FmjjP71X9FYpN7dfseQ%2Fbb%2FPBlx6Z1FKIQJ4Aq13A1v%2FdPCh18%2FO4mMND7mL0GOqUBrALrhmgprjmLykHgJQ%2Bn0RJZYLRpV68%2FsjwZCcrZDn4yHK1Q%2Bl89J3UI6olCERz1C6FfeuWhO21MFxFwY1VU166RTlXLmN9WyjqPV%2FyLdnAQCsfWRsi9tlgTkLm321D%2FNVsp2qq8PFEsDuM1x63URWESUsAKxrpjQv7w1ya6r8GmwabRgQHm5CALsqxC5NGcxOFxGJAl2S2xkQUTB7bx%2B45MHOk3&X-Amz-Signature=91dc6900ca6437f3ad17e6bd6165a0eed3eab5ef943404f185cf010399da377a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
