

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQBIQWWU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBBsA04hYXAccQrQAUQM0X%2BYqCUFGKr%2Be9q4WJx4fxjQIhAIDVEVNvlD2n73AyVJCGhwin8ZpIfx%2B3DmfL3C4Dn4xfKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxTTLkubi3mBBHMUTgq3AMuIyrLweD9X2KF0LcPMyyajASqnzFDzv%2BeYkiZfXpN1A%2B17FKDhK0TVLRGu8DFF6Vo6dQLp5LhhmpcG0AaniAWCX9E%2F3f6968nBiulXl%2B9oLNUomwtuEGSNTqn%2F1CsI%2Bs0KgfgdSo36kNA6hZvk77dhNQJv%2B96JvmAwpIADuegsUp8Me89VrKIgu94A2FPrPKgZvigRaahPzscXqb%2F%2F%2FRuuMPunPt1xOpeWZVR60ryOSaS0%2B9sl2%2B2ebGTF15GGtrzkh0Xid4%2FIL%2FZWz9dQkz6MNED2yrvhIzNY3O5u4XVecKpzSDH%2FJnUCIaToEnhkFzrUSRkSaRAr%2FCG1MShpxcQbvVFs4qzacE2YIDkrchmbz6IMv3o2s%2Bqk1irIt1zgEYMX5YTyHRKWnNei89Y8WO2sBBXD3CIdYI760Y0epZ8cV1kk%2FngnEZrVllTEr1tDZKac%2FxIZsP0d2sRdecFy%2FdNc%2FA8n7%2BljvtDX9ClrDVNvUvlixPY6O8bQEDSAngVzWWDDyknkCklHCX%2BxhP4adEdsfOUP9UYBazXW86Gf2%2Fb9m2EATcmL%2B1I47t56wXmjtYMSNtCY5Pq63mRH3jTD02tycmJvWOyAtvjig%2B%2FSRu%2FnGvQFLFkBWHQThLrXzDSpPe8BjqkASmCHRA2cpRVMp27i60tTv183k9Rahmm6uJ4c71JlHj6D1erhCETz%2FVvIUrMPS9wuzkVPSoO6pavbJtQs86QfcJHePDfqTFcpE4wEzUDNMnRKLtZFFrxvZbAqI6VVRu7odYSI082jFCJWblmWMA1KsoTaGDuoT2n866PtQkUiLslg1lOswW7MLMGnJZ3P4i3Mx1OukJP9Zrd026RT277yg2Vvf5Y&X-Amz-Signature=6409955e7de04ccb40b7b06e3738344998a5c3d32acaf64feb2876626bcbbb3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQBIQWWU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBBsA04hYXAccQrQAUQM0X%2BYqCUFGKr%2Be9q4WJx4fxjQIhAIDVEVNvlD2n73AyVJCGhwin8ZpIfx%2B3DmfL3C4Dn4xfKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxTTLkubi3mBBHMUTgq3AMuIyrLweD9X2KF0LcPMyyajASqnzFDzv%2BeYkiZfXpN1A%2B17FKDhK0TVLRGu8DFF6Vo6dQLp5LhhmpcG0AaniAWCX9E%2F3f6968nBiulXl%2B9oLNUomwtuEGSNTqn%2F1CsI%2Bs0KgfgdSo36kNA6hZvk77dhNQJv%2B96JvmAwpIADuegsUp8Me89VrKIgu94A2FPrPKgZvigRaahPzscXqb%2F%2F%2FRuuMPunPt1xOpeWZVR60ryOSaS0%2B9sl2%2B2ebGTF15GGtrzkh0Xid4%2FIL%2FZWz9dQkz6MNED2yrvhIzNY3O5u4XVecKpzSDH%2FJnUCIaToEnhkFzrUSRkSaRAr%2FCG1MShpxcQbvVFs4qzacE2YIDkrchmbz6IMv3o2s%2Bqk1irIt1zgEYMX5YTyHRKWnNei89Y8WO2sBBXD3CIdYI760Y0epZ8cV1kk%2FngnEZrVllTEr1tDZKac%2FxIZsP0d2sRdecFy%2FdNc%2FA8n7%2BljvtDX9ClrDVNvUvlixPY6O8bQEDSAngVzWWDDyknkCklHCX%2BxhP4adEdsfOUP9UYBazXW86Gf2%2Fb9m2EATcmL%2B1I47t56wXmjtYMSNtCY5Pq63mRH3jTD02tycmJvWOyAtvjig%2B%2FSRu%2FnGvQFLFkBWHQThLrXzDSpPe8BjqkASmCHRA2cpRVMp27i60tTv183k9Rahmm6uJ4c71JlHj6D1erhCETz%2FVvIUrMPS9wuzkVPSoO6pavbJtQs86QfcJHePDfqTFcpE4wEzUDNMnRKLtZFFrxvZbAqI6VVRu7odYSI082jFCJWblmWMA1KsoTaGDuoT2n866PtQkUiLslg1lOswW7MLMGnJZ3P4i3Mx1OukJP9Zrd026RT277yg2Vvf5Y&X-Amz-Signature=cb3c21253cd334acc673ea39d2028869cec4683b15fac350a8954166f100abb2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQBIQWWU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBBsA04hYXAccQrQAUQM0X%2BYqCUFGKr%2Be9q4WJx4fxjQIhAIDVEVNvlD2n73AyVJCGhwin8ZpIfx%2B3DmfL3C4Dn4xfKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxTTLkubi3mBBHMUTgq3AMuIyrLweD9X2KF0LcPMyyajASqnzFDzv%2BeYkiZfXpN1A%2B17FKDhK0TVLRGu8DFF6Vo6dQLp5LhhmpcG0AaniAWCX9E%2F3f6968nBiulXl%2B9oLNUomwtuEGSNTqn%2F1CsI%2Bs0KgfgdSo36kNA6hZvk77dhNQJv%2B96JvmAwpIADuegsUp8Me89VrKIgu94A2FPrPKgZvigRaahPzscXqb%2F%2F%2FRuuMPunPt1xOpeWZVR60ryOSaS0%2B9sl2%2B2ebGTF15GGtrzkh0Xid4%2FIL%2FZWz9dQkz6MNED2yrvhIzNY3O5u4XVecKpzSDH%2FJnUCIaToEnhkFzrUSRkSaRAr%2FCG1MShpxcQbvVFs4qzacE2YIDkrchmbz6IMv3o2s%2Bqk1irIt1zgEYMX5YTyHRKWnNei89Y8WO2sBBXD3CIdYI760Y0epZ8cV1kk%2FngnEZrVllTEr1tDZKac%2FxIZsP0d2sRdecFy%2FdNc%2FA8n7%2BljvtDX9ClrDVNvUvlixPY6O8bQEDSAngVzWWDDyknkCklHCX%2BxhP4adEdsfOUP9UYBazXW86Gf2%2Fb9m2EATcmL%2B1I47t56wXmjtYMSNtCY5Pq63mRH3jTD02tycmJvWOyAtvjig%2B%2FSRu%2FnGvQFLFkBWHQThLrXzDSpPe8BjqkASmCHRA2cpRVMp27i60tTv183k9Rahmm6uJ4c71JlHj6D1erhCETz%2FVvIUrMPS9wuzkVPSoO6pavbJtQs86QfcJHePDfqTFcpE4wEzUDNMnRKLtZFFrxvZbAqI6VVRu7odYSI082jFCJWblmWMA1KsoTaGDuoT2n866PtQkUiLslg1lOswW7MLMGnJZ3P4i3Mx1OukJP9Zrd026RT277yg2Vvf5Y&X-Amz-Signature=e160913f457d575f3413de5620c5cd8a4c9bb0a404dc82bf92076f713cdfaec3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=cd3bd99a2661c6018e74233111ecf76e1721af4a6530b7c2eee6550a532b4d44&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=6daf16bf6c9b00d7c4ce48fe54fb64f432d01ba02b212dea30f35cd90d5c667d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=92b0c616aa0f3140ac85d36f12c689f0ef085202540fc80a9281f5f3fc50af01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=f19ca8e9f176fe1e1fb85dd2f5c728f2f8e50df0905acda11284b1d0a39a20e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=b4fcf9be045bab6e3c76841d9937247fee51845594836edd314905a5824621ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=831cbec21b767ff7724a91293e65af0dc0774056a2b24c429ca846c2f1e0aa1b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXLBOSSN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2RMw1ZPiz2Ude8MjMgQAoZu%2FYueobrdCGFPE1mz3jLAIgRI2igUXZ8%2BXHkeHj%2BKgIDk8HMjkV%2BRYjp%2B0GMQKpRfQqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2BblUneAKwpKABXEyrcA%2F6s8pWA5k9Xl6TtctM5W9v9lw8Ltgtxws5lQfnd24DDvHWmFi7yrIsThef4mk030PNR0nXt3ij1nfRSVoY44ULQLhDx2ifhZ%2F9YVt7jQ9nrL2sntBPV1BKUlqN6SLDKJEShfP0v46p2DIl0nfNZI%2FtWQmLRj7nkCxHjUzm2YKU23Pb6kl9ex5anFwewTLUxZVjx%2FDqEOj3s8SGWSvcPKkKaxlSNw%2FGH6h8sClxGAIspU5BMsF14S31w5DO8dihZ6UPFpBG48ea5flVOkM13qUijvh6bYsQrn%2B0h1UWBW%2BfUqbBpmf6TLrL%2BM4khYdPorqE27PdVbj80qqf6UukySes2z8F%2F58J2vJt0wYsjcHIzaxWvSz%2B%2FOsPA8X%2Fz6EnRxqmPpVqgc%2B4%2FWqEpRuPniDBRaRJd02wrFqYacTuzoi%2B5hmTXhQzP3hKqjhn2OZfiJRiZvscUEinJE%2BPzfYMkWCpJ31fvSYgilC3coJEJM0n2HIs2eUhZJWs8gqtHNZCIZ%2BMfM1NhBVE%2Fg3jtpjimiWIxWY%2BopMcRuCBtexX76f6IK%2B2GOo5JgmNhnwB35WCGUnMKE54dztMcD3iA287KlREY%2FsXlQqa1IssoQ7KZZQ4Uot9fdlEB5Ew2vB1VMKyk97wGOqUBZPhacVTStDnDQ8HvJEIQSDmGQEogmjzmT%2FjctMx2hGuIFjAMDXgQBx%2BFymP%2BRxFuLezy1wKE4mlWs%2FzBRBAWLx%2FLJosyxtFHTNokM0osqEbR0U5ind8h5DZD7ia6ppE4uOgUcMDVP%2Fj4%2BIC1t2bC%2FzpvK6Lk5BNEhyoKSoXT0cUnet9MYtSg%2Bd4lkfS%2BEIw7wccSG1IFnpZ2t%2BIucoTZHmTSzQJ6&X-Amz-Signature=5b375f5ca5c8355c1e36d2365f6654d509e6ef54683c7abf7a538b3391176e79&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654NWIFBA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBDMTORRsafy9J3sKku5MbfFJueaIaHpb%2Bg4%2Bebk2DojAiEAxnyeGI%2Bfm18gRoyH5zunn94MLx0Eh17Gqs39fD%2FX5AEqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQ%2BJ1HEYKKFauB1fircA8W1F1eAH06HXLu6vhfOfJyMEE3xAD8S7Ph2Tw3Cd3uo76gU1mNGjTGG2%2F39%2FECK2aNkdd4Klj1h8rMFYwn7J5rANobmI0hUpTPDgsnOQQzQgBBEYy5PByrbzvnAE2uSju%2Bny0BFIyH7IehbyLMlrBtSi1EHwLUPP4vK9Vps8fsm%2BvF1scMJ2DGYpda%2F9P7BjiTh7Q8Q83jR2vnRsY2VQdFjvDfc4pA94RCX9oQekP4o2ddY2IYi42pSalSAdmMn%2FcfDRiU8uIm4ybw4FMDDHA8OdfENapIf4VDmdTFu5GEllV9H2wNVy7%2B62MjFfYk5Djv2IO%2F9xQ2%2BgK40UT4w2AXm%2ByyHJch5AEQHbynys2BIkR%2FfgP%2F42M0wHyTPU%2B23jKu5QI2%2FdXO2ZvTU5ASaFQIvrZSZ60CI5HuF2abAYMxtlA4MoSdOWC0sQ4zx5Fv86Fyb3B0twwu3ZkVA6aHAcqU56Ak%2FvhsIcUF7WIs0cYzD3VgsAONB4LNlEDoGxAsk2%2FKTb0n0mE4jSqVAR7LaqFguUlaQEQEhtGW9sLWAZb0QI5CKjl%2F5R7pSLPP7vAtAjnkjIfRJBSHAuX0zJIgqqXinxfON3Aph0VvGjPK7YY%2B9NTXYeY0jKhHEUNNoMKyk97wGOqUBQiQlrcIjA5c7G2It5R4dAUKztB7okS%2F%2FrJK9QXLjkZF8gMQok8IR1QO5qohxlR8rqBjaWc0Wj4OKuh67J3jO2JND0CcQniGxR6yyj%2BI4Nxb2%2FKEVV64wGC8HEnm0%2BmMf%2BtbjfotQr5HmJgYJmDHSkiznVmNeCfsvQkcwZDSSYv3NoGrO5mqS3O624r30H6kCxGPLfR5rvOOUCzGL%2FL4RNSXXaXRv&X-Amz-Signature=71f98240ee5b8347e3f4e9165759eec12bfb55cbd1772e7eb320f045d4c594da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=0bb181ed407b5cc69036e656d8540622051ee7af7ffcf53f937f6e5b1ebea3b9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=0693b0f9c92b78ec41005f2f004c2c54cce007dfcdcc86b9dcb1bbad9613a2f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCY4EIIE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHOP9%2Fjy4ueqOEOOBXAVISZ60C220Y5%2FxBe%2F9hos527%2BAiBqJbRfozRMqSLBpX5RHQP2Z%2FysLn1SdsSlZ86SmJ0uSCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWgQ6niqUyw7cl3nKtwDBA4Q8PcDYd%2BsAPoMsCFwos%2BVdcPVR03ZqT8tsY7U6aTXmVIsEL7DnNxBxS5OmCD57l1HKZ6CEUQN%2FAdvdqTmtZinOGrdQYDZyRwYhkh9%2FpL91a5YxpV3L%2Fr0zJbonrifKxe6IKJYEew1OCn59ZDOb5IsnE2i1hGxoym%2FRpRNV9BeCPMYL0D5OUMDBN92ynZ7EGBVqxA9FjUh1%2F84FyWCfvfdHEM1MbW90lb3o0ctIzysYpnkmnbaKEr%2FRKQkr7NQ8JLSUp5JSD3%2B%2BnMDLgLUT1iSaYpjxuHCoEOrRIu6qhO3gIEZJbv%2FarJBurkIBoS7ilzsaPE6x5zKS%2Bh2BhXTSw5FD4yX8pe3Fp8nzWHp1puOl9f3cjuqsYvSsyFxRAPjLQeyE%2FMWlr1KP2C0rjUQkFi0Yu498X06Xz3oXFBgoMzlvWwStSOUdmQiLiPvitN3t9lD9DNfCbA4xtyTB98I2j8kbnX8RrDogulDsJoI9WQfHfmA9cyRWhbYXsTacjcBvOBKGwYv6sQCPkphste8ppIl%2FGHIsvF46u16MxV4sgB5eLWjfKCpf2%2FB93qVXWZheiFcuiO0qO%2Fi9fbIP4vj0xxHXb8ap8UlFcfZhsMLMsdGbwnjxCaZAf3xp00w0aT3vAY6pgFUgTsNcZti3K9uoy4JrflZn%2Bso1G6gth0dduvZmOd3RE4SGIr%2Bk2qUg4WbUYu6lYDc6EU24xx%2FUeIE25hj2NXJe5CWa2Q9bvl7b4bAjc7745xy0bwIXH7GVlvpN78sqlWhAoWJ5%2BV8w5oxN50A4jVdBiUHVoCA6PyL0x1CZnH0UORM0Fk8StOnWKNyjF%2FCJdGYO2GztOg%2BXymToMc19YGeyZnIotc0&X-Amz-Signature=565ee90dddbeaa1f6b459afde3877acff458a5d5dd0c0e3b8029545c4da44dd7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNKAKDU3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuu2zRHvXhNhwEhL2KdGakDPD5mBNBqf4h%2Bh9wCrT92wIhANpiVRplJbZrsOPyjj%2B%2BWJN4hlsHkCtu5uuiMl4C5mIXKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqvXhRfRGURq8sNSQq3AOYvtOah3KK58JdFj%2BdMXsk%2Fm3sVUjPTRfrFFJ8NtfZuY2R7nSutK9sOvYE%2F1iqzRD%2F%2FAkEymW6w6Qz2pu25Wn6MZ7xgp3vc5JLcSKXPW6KnnNkTFkpu8L6TmRapr%2FAxC49Z19KGr024WwURT3ffS1%2B%2BgfME0lyooXuzeZE6GhJPV0jrG2ZOFlLQrRRBANY8Xn69RY35U2G37lUmPXSIN%2BCjLU57a8MfKyaJFw3%2BWkSHf3X9FMykYnZFlRQxi%2BwkEJO8CqHfX7mR%2B6%2FgUM0ca8GJY5ydGTZP%2FU27UtC7xnxNEZ%2BUuacwvWeqoQQcehjhwP%2F315aUPxoMthdjbfIb4CID3mr4CHjkz6rZibj3CLvzhOr5vGLELo4NB8gRi4D2SvNKDWjI0fDwGkBk331nTGWU6ObaiqRCS5WKNdsyoDOuWjHsWLXPNdX7AdCe87Y0PBOGqABTYO7c9q55rGXWz%2FGtfLhKhbWvJskZEEOmQ21cDsvl8gGOPaHCCnRL92nEDcbU7pL3wy85SjrqvXz8JZUMh37BRogsgjLnHMFw%2F1eB4eJs6LDScgiaanfKKbi6LA5HahJarwoTcc6yLus%2BWTLHu9%2BhFiTaDMJX8eeWYoV3woERU%2B1IyWLoloyXzDJpPe8BjqkAXPOxTdnXtRACzRItfBw0sIkpfYrnCiKgq94Y6ehqcHtD0ZP1Il29h3sWtZ6FltzVoCzpkDTZEjMH9uObVzMSTh5pg3KpOwYHyySFbXm3bHvdRs3c71ci2uFEvcyWysMmoDOC4kJysY1MaJG46U3HYoEVHZImv7CIHtNv2%2BfJc53QtUczEM8U%2FncCWjneYwwKWh45FAtsPYF7tsezz6VgCol%2F8ve&X-Amz-Signature=3b5d263613dd4c3e13780942e42a7a6bfa5b7ffb674d57823cf98435ccffd10b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL3KMYQG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDGjZTE1Jf3gxZ%2FqLDbjMUKjO18hG%2BHI8T6YWEtzO2FUAiEAlC8JJKrQNtlzEIIGocS%2BJKwAEEFaAZ9j3haiUaewPI4qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYaZWo2sNZ4f9a%2FlCrcA1%2BJ3ZQqt1moZ2wTit3knJai2roTyGXoTru%2FvrKopM71oFq5PQSmbTcYKi0WHibFHDvbiKrK3g85r2OFXfCUbkxLbiZyk2ph0uj2%2BJpZTBQzj6DCyAXWX7sYXftMj02X4sm872Nn6Hr9UCNUzHy2aTAcDumCiOBk1XRRFWHy%2B29RC%2FtzRU1zTXftnBigootDRE6UBalZXlS5ct7AVLv4WbWKNb2aHKm3no82OkXmJxOAaC0g%2Fiic%2BHOaRCTUVlC2%2BZ5yI3YsRm3BUmDc4B6%2FBRgJdg4BJLvTj%2FUUwbvcw2ifGFWzOyJFwMSC1v1BzaVJr4lsWdBqtKB24BAmTfkfZmwzkz04c2iOW8gbocH3pGTh8TCFeTIgKHK45rtqhA0cFjnvv5I9Igo%2BaFJZf%2BZ2YHdhP6MQYiqWFAYC5MNuCAQsMuZFRAwCXkm11ElLazMB6%2BUAje3P1voZ4TV5NLv3Fet8VDRyFNJxA6CLpFu05DV28WIK6LvKhS8Bdt4sORXael0%2FD%2BjE6vo%2FOewFELfc2OoiX%2Fzls%2F%2FOJl2GXcV%2BIf6Cg2FiM%2BQEmY9S31tdpSeKcpkqrtdQBarbE1VBEWDfmQTMSaTCvlc%2Bzj1eo0fiwlDD6ffaqNquaTgtvIKFMKik97wGOqUBEynDTIBW%2FcsIIVhXmryRpE3r1OQ4jj4FSmgRB5pZdtuhGDojfF7%2F63dpYuJVYQYk85Kr3fUiVbAVatOJhgYbnM1RPBmQmCkt9pKo7m1O%2FEhF%2F1TnK6VwFOtKVcAn8gZs7mBx13JAF2b9tuqViratWezQ30zXR%2BfkrF%2F7TPJ3pejp7M4wZpjaotwYQwzKnrLbJyBBFbw%2BHAAxkuMvBZsDMVyGh2CX&X-Amz-Signature=8e96bd8677e7bc3efbb1fcfd8f42fccc82b66423d6924f45fc5fee4debf25129&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTZD2NOO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyQ4JNJsqImZqVMRpvhkMVaywTJtzZkaM%2BXBFEKGDw2AIhAP34i2tYYAyeayNoM%2FDelLSE4iI61cbk2%2F%2FHSKsvP9hzKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrUMftVC7RbXkA2B0q3APB2nK0G0nsvsxQ2BWAL0X6cHIYg5YSYCyUNpLPpxAMf1nm3hDVVEgdGvhd7Plo%2FXecohqZzsZcNhzGdTv%2Bo%2FNUcMmmvxtfvJ9vw66of1CJ%2BMGVoDgBnIH21QaQ34Kp7IrUYalXyaACRHyOcQhJraVtzpiPtH6UCI8FbZqxZ3ahBVkKj3EJGbJRwWY%2FyqgslIchNFiwMKJiOCXNhdzxxuPfA%2FLh0N4MaNKGogPFt2u%2BxDW8fpFH50hi1oetwnHy%2FVfejl0D5FJ%2FSQffj3o3Zi1clrAXoWsLaF3w4bUaMy%2FdR3VfaZwfKKQFUBYa4mPqQJG0e0AijGSmtcbg6jFZgOVz%2FLxDoiRn1NNtAD477%2FsUPVU7iWyye%2BNMfHhFfR3teecUdt1rw995GDakp1IV1OWpD4oDVgjmLht8dEsaQYZAt21voySbHNG%2FmGRsxHknntQubvHgpreCZDXmfaaDG6hbr0L1BF%2BpFBWgVtMfIPTJpsc%2BWc6ZDtUMLu%2BeTvSh0bI7GZr6JE1psCK%2B1YB9IDY%2Bb475PeoyE3%2BNreixSknABsiBPxuOtyUBC645hMv2bI%2FLo6GcSsScLdlUk75e%2BdQ%2FsqKBIjzPXJhFg3IReEkX1Y8%2FApfysljd%2FPCCcjDIpPe8BjqkAfRKZ3eXksFU3e2l%2FF4KU5WZ2N4DSZvE7dEWWw0YQxpK2DBA6hFHyNcntkBAqAGB2aQW6EN36SdnGoenM9UFyH4lZLMD2vDzclmUb%2Bnlvbl9AaaJcJao0HGfajaDwrHEPYZaTWF6wMuOLz%2BfQ05%2FSo4bkC55NZ%2FVmSp%2F8zg2MNKZxdECAp1d8sEcghr1134YSknvZZAsCMz1aTCrs1IVHfN%2FZsWr&X-Amz-Signature=960ec4b4a79edb8be89d5cffcf3d860ffb109d332c0962a8daedb3630d5bc464&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XRAFEGD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2BhWTaHVdCd4gzHIHpeQdJ6uwYddCAbGUCtflz%2FrI8MAiANXUnDk0IqDLNmlilE9uZJnJhSFe2%2BzsCOCQLv3aKdECqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEXpNUf%2FPAD5CzKn4KtwDTrSDn8mBg5s3qN5JOTsNb3aeeth8b6gRjLd%2FeiFCpdnxxFECfo58hkrmdVwmsBYCr9wWcMs2LpUbqFIGTuskDdXWNOhNZAGmdA%2BLCTSn9J6x33oDJugo%2F87GngrGK3Ng8bmliNyNkQdnOrHH3krymhEjOzY%2FoIEpx5Xmyyt0YMdzI3oPPzMO61q%2FT%2F%2FTFoaekk%2FfVRfwF0ZAMJJHFhkGHg7JnmljjUghtQrYpQT2kC1Xja9%2FGocSCy8XMFeORLm%2BvZhPZhtCQ6W7sYqA1a%2BKO5GI1DGl5oEbS%2BPjifeU3NwTArR9JdsMCd7F54qXLR3m2syFrLE7xP87R8QC1qKa7CWx%2FyeBeb%2FZ5Tp8iYO9TzdryNWT3UHmKbrKbtfQtUG7Lv6N9pe%2BQjtGYCAgyFih57t%2FxTpzrD7kbk10zvPCiMx8eipvqL%2BULadu8n2yRA4Fd4%2B62bgnCRF76%2F0UgzZFYLBovFtFQbhrkx8yGuf1%2BeKPU8UIbvsACy4ue8IFy8W4r42n8ikqRSTtsHYByqgambAtcMMZS0P9EY78DZqq4ebnNnf2GpQk5E%2BeR91w8BLEG14F%2BMBfqZa7VkbIwml6YVGZsKwxFfKfyg7wR4945rsgYQcYclpqC6TY2wQwjsz3vAY6pgEbxXaYcVjmKVHzmxK6oUkzIq%2BlP2%2FtZV0pVtAGG3iHM2Dk19Zlqf%2BxqkeqIatL9p5mHVeC%2FCdn5taId15lb%2FJYOFoMXUvM74gTYIiamMZrfzSaWUnCtuOJkRYz1ntt4%2FNxyIa9p2phZ5ukAH%2BKfiHabVXKuR3USqoivhOpcMQB%2BzVckgvsHH%2FJUEGh0wC7bm%2F%2BW7w3J93pZfriehHISXYEZbCI1T47&X-Amz-Signature=8f862537e7e31ba899dd8935d4a20b70bb206078d3b0e25e9a2fdbc0f23531e2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XRAFEGD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2BhWTaHVdCd4gzHIHpeQdJ6uwYddCAbGUCtflz%2FrI8MAiANXUnDk0IqDLNmlilE9uZJnJhSFe2%2BzsCOCQLv3aKdECqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEXpNUf%2FPAD5CzKn4KtwDTrSDn8mBg5s3qN5JOTsNb3aeeth8b6gRjLd%2FeiFCpdnxxFECfo58hkrmdVwmsBYCr9wWcMs2LpUbqFIGTuskDdXWNOhNZAGmdA%2BLCTSn9J6x33oDJugo%2F87GngrGK3Ng8bmliNyNkQdnOrHH3krymhEjOzY%2FoIEpx5Xmyyt0YMdzI3oPPzMO61q%2FT%2F%2FTFoaekk%2FfVRfwF0ZAMJJHFhkGHg7JnmljjUghtQrYpQT2kC1Xja9%2FGocSCy8XMFeORLm%2BvZhPZhtCQ6W7sYqA1a%2BKO5GI1DGl5oEbS%2BPjifeU3NwTArR9JdsMCd7F54qXLR3m2syFrLE7xP87R8QC1qKa7CWx%2FyeBeb%2FZ5Tp8iYO9TzdryNWT3UHmKbrKbtfQtUG7Lv6N9pe%2BQjtGYCAgyFih57t%2FxTpzrD7kbk10zvPCiMx8eipvqL%2BULadu8n2yRA4Fd4%2B62bgnCRF76%2F0UgzZFYLBovFtFQbhrkx8yGuf1%2BeKPU8UIbvsACy4ue8IFy8W4r42n8ikqRSTtsHYByqgambAtcMMZS0P9EY78DZqq4ebnNnf2GpQk5E%2BeR91w8BLEG14F%2BMBfqZa7VkbIwml6YVGZsKwxFfKfyg7wR4945rsgYQcYclpqC6TY2wQwjsz3vAY6pgEbxXaYcVjmKVHzmxK6oUkzIq%2BlP2%2FtZV0pVtAGG3iHM2Dk19Zlqf%2BxqkeqIatL9p5mHVeC%2FCdn5taId15lb%2FJYOFoMXUvM74gTYIiamMZrfzSaWUnCtuOJkRYz1ntt4%2FNxyIa9p2phZ5ukAH%2BKfiHabVXKuR3USqoivhOpcMQB%2BzVckgvsHH%2FJUEGh0wC7bm%2F%2BW7w3J93pZfriehHISXYEZbCI1T47&X-Amz-Signature=c9ed996d9a1821901336028c932be6a27a113e53141f4336d4503225070c8c29&X-Amz-SignedHeaders=host&x-id=GetObject)

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
