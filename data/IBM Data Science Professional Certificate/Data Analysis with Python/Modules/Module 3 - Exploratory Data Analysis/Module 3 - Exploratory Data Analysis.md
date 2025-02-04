

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2T554DM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCrsh4Me2JwQAR8AVjDbmQT7V0E2G08x8OW3agVKgbcmwIhAJaWZv7aQVlYpQdedw4vEaV5B8gG2ZEdiQdLC83%2FTwGpKv8DCCYQABoMNjM3NDIzMTgzODA1Igw0XnLFBm3QISiExqwq3AMNh8KZgVqCmR%2BG%2FlwIO%2BPthNvIvmdcf6rfwZsS7ohBGZYJW7DFFA2pXPPfVsQeuLurxl%2FvFi3UMW%2Bg%2F%2BJKpmDhJaYTL3PMNCJK3EUu%2Fl2CCaRmfZCenrkRbOi9SDo6O0k7FG7uXxXpxmR%2BNFX8RygCSa%2BwSJyg%2Btj9u%2FaWU135x5Ij1cbR3HhQsW%2BIj99uOdiTO2mQBH8I2NyohRRY0pRVbxxhDsaiDLlDSmOqsB36f6Hfs5fHrQPLep914q4NxmHerw99gr3bMkxsplbxfHJuiPKO6siWJyM5pN9%2Bh64Dcf8pvP2HqAZMmeuy9yo51lQ%2FyobiyfJOnC2fH9Aa7cF3fNpmD3%2BJVkzcYGZclxuvgZ3rp63%2FSmybojrnZE8ImBmgPB%2BewrzBZaiM7jIFOCigOkbhIgNgY1eXlO1MUrvrtKIr4Hd5zAxhlm5apexuOF3uOlynbu5DO6FKoan2GKRJiZYaFrVjAe268QEd2%2B5rTu0rrulfEMssONC%2BqhbeRYzbxTtc1IP766ngMQdo89fU%2B89dgjAxeV%2BuQJvzn6pW2dRVjSlLUCARGl7DPjyg6g5JXzlMFdhzzGikTUk3%2BMCsOL05O6zI4Cj9ArraN%2FLFi5I90XDlgF2k0uWCzzCKv4a9BjqkAfwC20T%2BLkpECmiFHPUK0d6ExQyCf%2BLZLh%2F5zDVpavM26Xxya0wtS4bskHx04pj%2BiY24fi6lBgH51wtcjSMw8jU6XTFiTD4n%2BQdeou78NliS972daVdtQx7JODGx6EB7m%2FE%2BvDY20b9zGe195nHANbbGjzFwl8m0KlkS%2Bhu6aVbviCB9YjTQoMoGy6VakRoKvkWYkqgwh8RVqPyLKTwW5nE%2Figuv&X-Amz-Signature=6205d9e353b2ddd756ae38127eaadbff686ebcb516bab6b6ddc90661a1651b0a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2T554DM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCrsh4Me2JwQAR8AVjDbmQT7V0E2G08x8OW3agVKgbcmwIhAJaWZv7aQVlYpQdedw4vEaV5B8gG2ZEdiQdLC83%2FTwGpKv8DCCYQABoMNjM3NDIzMTgzODA1Igw0XnLFBm3QISiExqwq3AMNh8KZgVqCmR%2BG%2FlwIO%2BPthNvIvmdcf6rfwZsS7ohBGZYJW7DFFA2pXPPfVsQeuLurxl%2FvFi3UMW%2Bg%2F%2BJKpmDhJaYTL3PMNCJK3EUu%2Fl2CCaRmfZCenrkRbOi9SDo6O0k7FG7uXxXpxmR%2BNFX8RygCSa%2BwSJyg%2Btj9u%2FaWU135x5Ij1cbR3HhQsW%2BIj99uOdiTO2mQBH8I2NyohRRY0pRVbxxhDsaiDLlDSmOqsB36f6Hfs5fHrQPLep914q4NxmHerw99gr3bMkxsplbxfHJuiPKO6siWJyM5pN9%2Bh64Dcf8pvP2HqAZMmeuy9yo51lQ%2FyobiyfJOnC2fH9Aa7cF3fNpmD3%2BJVkzcYGZclxuvgZ3rp63%2FSmybojrnZE8ImBmgPB%2BewrzBZaiM7jIFOCigOkbhIgNgY1eXlO1MUrvrtKIr4Hd5zAxhlm5apexuOF3uOlynbu5DO6FKoan2GKRJiZYaFrVjAe268QEd2%2B5rTu0rrulfEMssONC%2BqhbeRYzbxTtc1IP766ngMQdo89fU%2B89dgjAxeV%2BuQJvzn6pW2dRVjSlLUCARGl7DPjyg6g5JXzlMFdhzzGikTUk3%2BMCsOL05O6zI4Cj9ArraN%2FLFi5I90XDlgF2k0uWCzzCKv4a9BjqkAfwC20T%2BLkpECmiFHPUK0d6ExQyCf%2BLZLh%2F5zDVpavM26Xxya0wtS4bskHx04pj%2BiY24fi6lBgH51wtcjSMw8jU6XTFiTD4n%2BQdeou78NliS972daVdtQx7JODGx6EB7m%2FE%2BvDY20b9zGe195nHANbbGjzFwl8m0KlkS%2Bhu6aVbviCB9YjTQoMoGy6VakRoKvkWYkqgwh8RVqPyLKTwW5nE%2Figuv&X-Amz-Signature=4afe9be790973c908baf841085fcd090a36cd51a9bfc95dc057836e8bff2749c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2T554DM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCrsh4Me2JwQAR8AVjDbmQT7V0E2G08x8OW3agVKgbcmwIhAJaWZv7aQVlYpQdedw4vEaV5B8gG2ZEdiQdLC83%2FTwGpKv8DCCYQABoMNjM3NDIzMTgzODA1Igw0XnLFBm3QISiExqwq3AMNh8KZgVqCmR%2BG%2FlwIO%2BPthNvIvmdcf6rfwZsS7ohBGZYJW7DFFA2pXPPfVsQeuLurxl%2FvFi3UMW%2Bg%2F%2BJKpmDhJaYTL3PMNCJK3EUu%2Fl2CCaRmfZCenrkRbOi9SDo6O0k7FG7uXxXpxmR%2BNFX8RygCSa%2BwSJyg%2Btj9u%2FaWU135x5Ij1cbR3HhQsW%2BIj99uOdiTO2mQBH8I2NyohRRY0pRVbxxhDsaiDLlDSmOqsB36f6Hfs5fHrQPLep914q4NxmHerw99gr3bMkxsplbxfHJuiPKO6siWJyM5pN9%2Bh64Dcf8pvP2HqAZMmeuy9yo51lQ%2FyobiyfJOnC2fH9Aa7cF3fNpmD3%2BJVkzcYGZclxuvgZ3rp63%2FSmybojrnZE8ImBmgPB%2BewrzBZaiM7jIFOCigOkbhIgNgY1eXlO1MUrvrtKIr4Hd5zAxhlm5apexuOF3uOlynbu5DO6FKoan2GKRJiZYaFrVjAe268QEd2%2B5rTu0rrulfEMssONC%2BqhbeRYzbxTtc1IP766ngMQdo89fU%2B89dgjAxeV%2BuQJvzn6pW2dRVjSlLUCARGl7DPjyg6g5JXzlMFdhzzGikTUk3%2BMCsOL05O6zI4Cj9ArraN%2FLFi5I90XDlgF2k0uWCzzCKv4a9BjqkAfwC20T%2BLkpECmiFHPUK0d6ExQyCf%2BLZLh%2F5zDVpavM26Xxya0wtS4bskHx04pj%2BiY24fi6lBgH51wtcjSMw8jU6XTFiTD4n%2BQdeou78NliS972daVdtQx7JODGx6EB7m%2FE%2BvDY20b9zGe195nHANbbGjzFwl8m0KlkS%2Bhu6aVbviCB9YjTQoMoGy6VakRoKvkWYkqgwh8RVqPyLKTwW5nE%2Figuv&X-Amz-Signature=8325f919422045ecce751d87c3f605b86be929d412951914f08311f175d1b26c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTBS7CLM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBUvWNsI7Myp7z0aU4T3s%2BtCp3qVG%2F7E9Yo%2BIIjSOyrkAiEA%2F4iv4DQaCS3MOWxBb1Qq%2BGYc7UABxA%2BOtqX9p%2Bd8YGAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDEt%2B4L6DdAZmUXI8HCrcAzujz5I2CofNB6oNmxxViSvncmHLP0BE5uBndvoFYtBZDo7vvrx3miqR5lwtij6Fqsu3sWEx5gSKbG0nKx6mx7Kdc0k1f%2FhPhRF1fz4JR5RX8Oyk9XrblvFGza8UWtBhP0vN4Z9aBDcWPdYXeRI8cZ3U3w1yqrrugXThXCKXlsRHRYsu6n5q5V006Be9297oq6e%2FcEhuwpe3LMjehhC%2BmYBUHr82TMWHtvddxGfO2mUkRMERbyJhkwJQ%2Bgi18mHSihcCwjdlyWGekA%2BUYvdelK%2Bj4ey9UKSExlnS5fq6CNxUyEeeTPbyVuVht8SHDePwbRdZPpKnwZ8fSu5R2u4yEvFSvUcNEqiBCaKy9MPCs9r1nDa2ts5c7uxb2htHIbAdzVmsphNJiVicVp1UpYvoAO%2BP9YRIXk4keO1yMgza%2BXfKbbBIsQKIf%2FYrCcOAuHLPuoMYqB2Unt3Vswe1%2BCdPiU%2FO%2BkWGx9iVJ65n2Hy2mEC4Lpd25%2Bp%2BeYkbqvZaN149UtdFjjTWG3twpDj8g7kPIWzd3TcQpyu2ghjbWSvLHxUAgkAX7Vhfb8r4R%2B2%2BdcBoDNiIUjv0ADsue%2BbWo%2FVYKFn2PKaI11%2BlvdP9Ny7%2BQOlOpVk%2BA%2FX1aPpbSkg7MLS%2Bhr0GOqUBRXuqOvvHs1nHEPq8hIK8zXbXNEnHIpxlGI6t91zY6nCbpEsbvBFWw%2F7mM0gICnW4zfvWaqoXqJb5Z4iTqMG%2BdjyzWZ%2FktweXAAmJwa4yEFYNuUfynsRSJaNNNgwtg2ffm36x6eDun3lZKrFXorLHc%2FF2LB9BD4s5DdmjZ5Zy8Jtd1UQ0qGWrQEGcCFhwFjlVB5g8z8o5R%2BrvTB%2FuQEgu%2Bq73kBoU&X-Amz-Signature=1bf7ae8d3b5a5758f7d6113b7cc11f82d7df8f5517de6bca0b1e7d8424096b0f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTBS7CLM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBUvWNsI7Myp7z0aU4T3s%2BtCp3qVG%2F7E9Yo%2BIIjSOyrkAiEA%2F4iv4DQaCS3MOWxBb1Qq%2BGYc7UABxA%2BOtqX9p%2Bd8YGAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDEt%2B4L6DdAZmUXI8HCrcAzujz5I2CofNB6oNmxxViSvncmHLP0BE5uBndvoFYtBZDo7vvrx3miqR5lwtij6Fqsu3sWEx5gSKbG0nKx6mx7Kdc0k1f%2FhPhRF1fz4JR5RX8Oyk9XrblvFGza8UWtBhP0vN4Z9aBDcWPdYXeRI8cZ3U3w1yqrrugXThXCKXlsRHRYsu6n5q5V006Be9297oq6e%2FcEhuwpe3LMjehhC%2BmYBUHr82TMWHtvddxGfO2mUkRMERbyJhkwJQ%2Bgi18mHSihcCwjdlyWGekA%2BUYvdelK%2Bj4ey9UKSExlnS5fq6CNxUyEeeTPbyVuVht8SHDePwbRdZPpKnwZ8fSu5R2u4yEvFSvUcNEqiBCaKy9MPCs9r1nDa2ts5c7uxb2htHIbAdzVmsphNJiVicVp1UpYvoAO%2BP9YRIXk4keO1yMgza%2BXfKbbBIsQKIf%2FYrCcOAuHLPuoMYqB2Unt3Vswe1%2BCdPiU%2FO%2BkWGx9iVJ65n2Hy2mEC4Lpd25%2Bp%2BeYkbqvZaN149UtdFjjTWG3twpDj8g7kPIWzd3TcQpyu2ghjbWSvLHxUAgkAX7Vhfb8r4R%2B2%2BdcBoDNiIUjv0ADsue%2BbWo%2FVYKFn2PKaI11%2BlvdP9Ny7%2BQOlOpVk%2BA%2FX1aPpbSkg7MLS%2Bhr0GOqUBRXuqOvvHs1nHEPq8hIK8zXbXNEnHIpxlGI6t91zY6nCbpEsbvBFWw%2F7mM0gICnW4zfvWaqoXqJb5Z4iTqMG%2BdjyzWZ%2FktweXAAmJwa4yEFYNuUfynsRSJaNNNgwtg2ffm36x6eDun3lZKrFXorLHc%2FF2LB9BD4s5DdmjZ5Zy8Jtd1UQ0qGWrQEGcCFhwFjlVB5g8z8o5R%2BrvTB%2FuQEgu%2Bq73kBoU&X-Amz-Signature=437a20df957399cdf47380ae8a14bf4db4df4a613a17354dac13aa6ac21bfd64&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTBS7CLM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBUvWNsI7Myp7z0aU4T3s%2BtCp3qVG%2F7E9Yo%2BIIjSOyrkAiEA%2F4iv4DQaCS3MOWxBb1Qq%2BGYc7UABxA%2BOtqX9p%2Bd8YGAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDEt%2B4L6DdAZmUXI8HCrcAzujz5I2CofNB6oNmxxViSvncmHLP0BE5uBndvoFYtBZDo7vvrx3miqR5lwtij6Fqsu3sWEx5gSKbG0nKx6mx7Kdc0k1f%2FhPhRF1fz4JR5RX8Oyk9XrblvFGza8UWtBhP0vN4Z9aBDcWPdYXeRI8cZ3U3w1yqrrugXThXCKXlsRHRYsu6n5q5V006Be9297oq6e%2FcEhuwpe3LMjehhC%2BmYBUHr82TMWHtvddxGfO2mUkRMERbyJhkwJQ%2Bgi18mHSihcCwjdlyWGekA%2BUYvdelK%2Bj4ey9UKSExlnS5fq6CNxUyEeeTPbyVuVht8SHDePwbRdZPpKnwZ8fSu5R2u4yEvFSvUcNEqiBCaKy9MPCs9r1nDa2ts5c7uxb2htHIbAdzVmsphNJiVicVp1UpYvoAO%2BP9YRIXk4keO1yMgza%2BXfKbbBIsQKIf%2FYrCcOAuHLPuoMYqB2Unt3Vswe1%2BCdPiU%2FO%2BkWGx9iVJ65n2Hy2mEC4Lpd25%2Bp%2BeYkbqvZaN149UtdFjjTWG3twpDj8g7kPIWzd3TcQpyu2ghjbWSvLHxUAgkAX7Vhfb8r4R%2B2%2BdcBoDNiIUjv0ADsue%2BbWo%2FVYKFn2PKaI11%2BlvdP9Ny7%2BQOlOpVk%2BA%2FX1aPpbSkg7MLS%2Bhr0GOqUBRXuqOvvHs1nHEPq8hIK8zXbXNEnHIpxlGI6t91zY6nCbpEsbvBFWw%2F7mM0gICnW4zfvWaqoXqJb5Z4iTqMG%2BdjyzWZ%2FktweXAAmJwa4yEFYNuUfynsRSJaNNNgwtg2ffm36x6eDun3lZKrFXorLHc%2FF2LB9BD4s5DdmjZ5Zy8Jtd1UQ0qGWrQEGcCFhwFjlVB5g8z8o5R%2BrvTB%2FuQEgu%2Bq73kBoU&X-Amz-Signature=b1106040c9bc8da6fa7bbe4a758647cc35ab6ef1db9f6cc1160933e9c1599431&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTBS7CLM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBUvWNsI7Myp7z0aU4T3s%2BtCp3qVG%2F7E9Yo%2BIIjSOyrkAiEA%2F4iv4DQaCS3MOWxBb1Qq%2BGYc7UABxA%2BOtqX9p%2Bd8YGAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDEt%2B4L6DdAZmUXI8HCrcAzujz5I2CofNB6oNmxxViSvncmHLP0BE5uBndvoFYtBZDo7vvrx3miqR5lwtij6Fqsu3sWEx5gSKbG0nKx6mx7Kdc0k1f%2FhPhRF1fz4JR5RX8Oyk9XrblvFGza8UWtBhP0vN4Z9aBDcWPdYXeRI8cZ3U3w1yqrrugXThXCKXlsRHRYsu6n5q5V006Be9297oq6e%2FcEhuwpe3LMjehhC%2BmYBUHr82TMWHtvddxGfO2mUkRMERbyJhkwJQ%2Bgi18mHSihcCwjdlyWGekA%2BUYvdelK%2Bj4ey9UKSExlnS5fq6CNxUyEeeTPbyVuVht8SHDePwbRdZPpKnwZ8fSu5R2u4yEvFSvUcNEqiBCaKy9MPCs9r1nDa2ts5c7uxb2htHIbAdzVmsphNJiVicVp1UpYvoAO%2BP9YRIXk4keO1yMgza%2BXfKbbBIsQKIf%2FYrCcOAuHLPuoMYqB2Unt3Vswe1%2BCdPiU%2FO%2BkWGx9iVJ65n2Hy2mEC4Lpd25%2Bp%2BeYkbqvZaN149UtdFjjTWG3twpDj8g7kPIWzd3TcQpyu2ghjbWSvLHxUAgkAX7Vhfb8r4R%2B2%2BdcBoDNiIUjv0ADsue%2BbWo%2FVYKFn2PKaI11%2BlvdP9Ny7%2BQOlOpVk%2BA%2FX1aPpbSkg7MLS%2Bhr0GOqUBRXuqOvvHs1nHEPq8hIK8zXbXNEnHIpxlGI6t91zY6nCbpEsbvBFWw%2F7mM0gICnW4zfvWaqoXqJb5Z4iTqMG%2BdjyzWZ%2FktweXAAmJwa4yEFYNuUfynsRSJaNNNgwtg2ffm36x6eDun3lZKrFXorLHc%2FF2LB9BD4s5DdmjZ5Zy8Jtd1UQ0qGWrQEGcCFhwFjlVB5g8z8o5R%2BrvTB%2FuQEgu%2Bq73kBoU&X-Amz-Signature=035c7e7e0b808d9ca32b37ab730fcec0b568d2ff121cd2c5e5534883454fbd9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTBS7CLM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBUvWNsI7Myp7z0aU4T3s%2BtCp3qVG%2F7E9Yo%2BIIjSOyrkAiEA%2F4iv4DQaCS3MOWxBb1Qq%2BGYc7UABxA%2BOtqX9p%2Bd8YGAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDEt%2B4L6DdAZmUXI8HCrcAzujz5I2CofNB6oNmxxViSvncmHLP0BE5uBndvoFYtBZDo7vvrx3miqR5lwtij6Fqsu3sWEx5gSKbG0nKx6mx7Kdc0k1f%2FhPhRF1fz4JR5RX8Oyk9XrblvFGza8UWtBhP0vN4Z9aBDcWPdYXeRI8cZ3U3w1yqrrugXThXCKXlsRHRYsu6n5q5V006Be9297oq6e%2FcEhuwpe3LMjehhC%2BmYBUHr82TMWHtvddxGfO2mUkRMERbyJhkwJQ%2Bgi18mHSihcCwjdlyWGekA%2BUYvdelK%2Bj4ey9UKSExlnS5fq6CNxUyEeeTPbyVuVht8SHDePwbRdZPpKnwZ8fSu5R2u4yEvFSvUcNEqiBCaKy9MPCs9r1nDa2ts5c7uxb2htHIbAdzVmsphNJiVicVp1UpYvoAO%2BP9YRIXk4keO1yMgza%2BXfKbbBIsQKIf%2FYrCcOAuHLPuoMYqB2Unt3Vswe1%2BCdPiU%2FO%2BkWGx9iVJ65n2Hy2mEC4Lpd25%2Bp%2BeYkbqvZaN149UtdFjjTWG3twpDj8g7kPIWzd3TcQpyu2ghjbWSvLHxUAgkAX7Vhfb8r4R%2B2%2BdcBoDNiIUjv0ADsue%2BbWo%2FVYKFn2PKaI11%2BlvdP9Ny7%2BQOlOpVk%2BA%2FX1aPpbSkg7MLS%2Bhr0GOqUBRXuqOvvHs1nHEPq8hIK8zXbXNEnHIpxlGI6t91zY6nCbpEsbvBFWw%2F7mM0gICnW4zfvWaqoXqJb5Z4iTqMG%2BdjyzWZ%2FktweXAAmJwa4yEFYNuUfynsRSJaNNNgwtg2ffm36x6eDun3lZKrFXorLHc%2FF2LB9BD4s5DdmjZ5Zy8Jtd1UQ0qGWrQEGcCFhwFjlVB5g8z8o5R%2BrvTB%2FuQEgu%2Bq73kBoU&X-Amz-Signature=b48c610fba4ae10cba502348d4070345e3a753474946801b59c9c4dce8aba713&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTBS7CLM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBUvWNsI7Myp7z0aU4T3s%2BtCp3qVG%2F7E9Yo%2BIIjSOyrkAiEA%2F4iv4DQaCS3MOWxBb1Qq%2BGYc7UABxA%2BOtqX9p%2Bd8YGAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDEt%2B4L6DdAZmUXI8HCrcAzujz5I2CofNB6oNmxxViSvncmHLP0BE5uBndvoFYtBZDo7vvrx3miqR5lwtij6Fqsu3sWEx5gSKbG0nKx6mx7Kdc0k1f%2FhPhRF1fz4JR5RX8Oyk9XrblvFGza8UWtBhP0vN4Z9aBDcWPdYXeRI8cZ3U3w1yqrrugXThXCKXlsRHRYsu6n5q5V006Be9297oq6e%2FcEhuwpe3LMjehhC%2BmYBUHr82TMWHtvddxGfO2mUkRMERbyJhkwJQ%2Bgi18mHSihcCwjdlyWGekA%2BUYvdelK%2Bj4ey9UKSExlnS5fq6CNxUyEeeTPbyVuVht8SHDePwbRdZPpKnwZ8fSu5R2u4yEvFSvUcNEqiBCaKy9MPCs9r1nDa2ts5c7uxb2htHIbAdzVmsphNJiVicVp1UpYvoAO%2BP9YRIXk4keO1yMgza%2BXfKbbBIsQKIf%2FYrCcOAuHLPuoMYqB2Unt3Vswe1%2BCdPiU%2FO%2BkWGx9iVJ65n2Hy2mEC4Lpd25%2Bp%2BeYkbqvZaN149UtdFjjTWG3twpDj8g7kPIWzd3TcQpyu2ghjbWSvLHxUAgkAX7Vhfb8r4R%2B2%2BdcBoDNiIUjv0ADsue%2BbWo%2FVYKFn2PKaI11%2BlvdP9Ny7%2BQOlOpVk%2BA%2FX1aPpbSkg7MLS%2Bhr0GOqUBRXuqOvvHs1nHEPq8hIK8zXbXNEnHIpxlGI6t91zY6nCbpEsbvBFWw%2F7mM0gICnW4zfvWaqoXqJb5Z4iTqMG%2BdjyzWZ%2FktweXAAmJwa4yEFYNuUfynsRSJaNNNgwtg2ffm36x6eDun3lZKrFXorLHc%2FF2LB9BD4s5DdmjZ5Zy8Jtd1UQ0qGWrQEGcCFhwFjlVB5g8z8o5R%2BrvTB%2FuQEgu%2Bq73kBoU&X-Amz-Signature=9d5fa20ab39b0e146343dcae01ef5e646296fc3fa7096bdc13d8c32cb90086b3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W6HLZII%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQCMkYWCVAR4ojsDTogz%2B6FbMzwPKStGOBCsP3Q28yJVVwIgbEgoruN0OH5V8%2B60rhh%2Fz%2BlT0vh3uD7Tuj7hkQd112Qq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMw32ucUrRr%2BTYzcPircAyz0IWI%2FKjpa2aUBOw%2FbWVK83vCKv6WJuiOWweG1DsEKVY6UrF8Q9x%2BZFlpPHU6aZI3QWJPC%2BTrjoimu17EGlmfjW8%2BBVGjQ1u58EP%2FTJ%2F3aYtFMIDrVjbFMD83N0RIIz0sWog9MsIPIZV5lhPO1ShkIcdK8FSQXDNKcLhaWXxAqX23JePCNOXkV%2FKGIQcMRHerpwcWInYHQ3z3ELeDw7FClgomSg9vf7Jot08R0MtiaMpQdcoDTGn3Zqiq3UpOPoC3gwqNxGMwfqzmvIFnnZXY1twNHVx6DCpqLYJjD5SaCzyd66ZXzdL660UnWN1l7EaY7srgsAc5Oqd0NMGZZ7G%2Fd1%2FYW27sDTCFlEdR%2FO47yeY9K%2Fo7fg%2Bsl1uPZDyEQaz3a%2Fthqpb2X9%2BsNk9spyU1FiWBy7Wj5JGePPMmCD2S7%2BijRNru4bhGJd%2BWQ0vpdFy%2F116qL38dDZ1x%2B3aIT5JPWRZ%2FubITSJB2KYZz8ccZKmljcxmOnfVojhyeOSc1r7bQWSRTjabicdX6ikiTx7w0yPJW%2B4NDe5tCrnpZfWyaS13mIVyq729%2BNTTpJS80gbZ5pCrf%2BAOHwY1NxLwV2ipIKBzlSQXi%2FmGuy13xy63UtWKdF2FAPtr3Fs61vMMe%2Bhr0GOqUBKkxcj%2B5WLG7u7BMXarFny5RiUrrp4hPapM0Ncpi6ysQ1TYbekpKgZ096IC%2F6tOMo8QwcTllecMMZOdXdICnjiQudf5hzSCu5ViqaZQ%2FpH1stKwaoRDSjAGtf0hCixQ%2FGiPfoCbGPhfxeDFjpf84KdQbdGcBVFqtD%2FWGNzRiDM5aakTNkgopzZ63i7HdkwSvySnTRCpSQz3mJLs8U%2B4eBYq8yAoQ7&X-Amz-Signature=6afe93014a58affb9202007fdb8b6804ad89768f6416b434bf7d0a0e0df3636e&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657KMOK5N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIGq6nUjxEVQ1UyYeaeLZGBZpwSYQpkCfWP%2FDN8YwnWQeAiEAq0FFo4nrSmrgjt6ZjMNB2dqh75gTzwKUwsVgKxMehNQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAm%2BlwZLyBp63GG6XSrcA2RUmx0Eb33IUFbU2poxHq9F0fHyWB0eSvXY%2FERdxaICzFkkS8o3bzRsbOr5H2rjD0UfS6HUvN7QtMrTQzLlms6XkMLxqDieaLEfZ1sYEO%2BpcK1Mqj%2BB7hc%2FsK%2FvCRNyAOm8Qx1VbIZ5ZLfI01G1gJuBAFaQXXA%2FrBVlD0QdBNQdWLiIbf1VNxH0OJe9TVJKLhF1UZ470pQhNexSoCF0IbBl8Yr9QMBpAS9gbMMwIKJBLFFxZuDAuR9wqpoPH%2FKOFFSWsDWlJj4ndrVVRvEDVpr8IwR4XLHJZwJJ16FPdkvpn8%2FLdS%2FReBJJQZA77%2B%2Fe6BXHU7p52SOYJguvdTYPv8JwKuFFlKpiJ3wevNLFo%2BKzXgXZzCWhylzLWpDgA9ZOJvVbEf5ZHFhhZbu3woE110Qd3tdkVjxDoc7M7WZ6to9nRoCr%2B%2F9EgjdzbF%2BuoyyL7Zn4wtAI6u0GFVHYKhZIYMjPaCc9TbGPSaoTyUpTGOkQUSL3kjQZp%2B2mjqW5frVkwSUJSwM3mZiZKBAnkN9qTSHa4ei5V2sYLqEQgDIaEIq0Gv3x0w8oHDQrQ7rKyqJkS1kc%2F1%2FrOrxoyd6DaOYP%2BHMeI8XZ3UwuXNFmffAMkR7l9m%2BM%2Ffg2Jqejnd9QMLa%2Fhr0GOqUBhsD3aJRyu3WukquD9pKGMYsiNR0VA40N9%2B65XkKkFUbSupNNcUcaeI2t1603oN%2BcStD9eZMv3KzSG8hEw6UrryelHvBlSsBzWivoZlmw5ndF%2FtOQB5n6Nz3dI4Ys1VZgE650Aw%2BILZUc%2B1rhTXSC07e4%2Fa%2BRFeFOUnuYxK0XeUMrxy7iuoFJqhlxbEv0TO8dEaaT2TV%2BASTpkU8HF8jZpvAL8tBi&X-Amz-Signature=3a5741d8e0bd1df7d02cb578a6ffa0714273484bbedb92171c36f6fd1f649b9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTBS7CLM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBUvWNsI7Myp7z0aU4T3s%2BtCp3qVG%2F7E9Yo%2BIIjSOyrkAiEA%2F4iv4DQaCS3MOWxBb1Qq%2BGYc7UABxA%2BOtqX9p%2Bd8YGAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDEt%2B4L6DdAZmUXI8HCrcAzujz5I2CofNB6oNmxxViSvncmHLP0BE5uBndvoFYtBZDo7vvrx3miqR5lwtij6Fqsu3sWEx5gSKbG0nKx6mx7Kdc0k1f%2FhPhRF1fz4JR5RX8Oyk9XrblvFGza8UWtBhP0vN4Z9aBDcWPdYXeRI8cZ3U3w1yqrrugXThXCKXlsRHRYsu6n5q5V006Be9297oq6e%2FcEhuwpe3LMjehhC%2BmYBUHr82TMWHtvddxGfO2mUkRMERbyJhkwJQ%2Bgi18mHSihcCwjdlyWGekA%2BUYvdelK%2Bj4ey9UKSExlnS5fq6CNxUyEeeTPbyVuVht8SHDePwbRdZPpKnwZ8fSu5R2u4yEvFSvUcNEqiBCaKy9MPCs9r1nDa2ts5c7uxb2htHIbAdzVmsphNJiVicVp1UpYvoAO%2BP9YRIXk4keO1yMgza%2BXfKbbBIsQKIf%2FYrCcOAuHLPuoMYqB2Unt3Vswe1%2BCdPiU%2FO%2BkWGx9iVJ65n2Hy2mEC4Lpd25%2Bp%2BeYkbqvZaN149UtdFjjTWG3twpDj8g7kPIWzd3TcQpyu2ghjbWSvLHxUAgkAX7Vhfb8r4R%2B2%2BdcBoDNiIUjv0ADsue%2BbWo%2FVYKFn2PKaI11%2BlvdP9Ny7%2BQOlOpVk%2BA%2FX1aPpbSkg7MLS%2Bhr0GOqUBRXuqOvvHs1nHEPq8hIK8zXbXNEnHIpxlGI6t91zY6nCbpEsbvBFWw%2F7mM0gICnW4zfvWaqoXqJb5Z4iTqMG%2BdjyzWZ%2FktweXAAmJwa4yEFYNuUfynsRSJaNNNgwtg2ffm36x6eDun3lZKrFXorLHc%2FF2LB9BD4s5DdmjZ5Zy8Jtd1UQ0qGWrQEGcCFhwFjlVB5g8z8o5R%2BrvTB%2FuQEgu%2Bq73kBoU&X-Amz-Signature=4e8457461ff8c813f7d1554da9f660d42bf07595034eea9e68a56bac7af8211b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTBS7CLM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBUvWNsI7Myp7z0aU4T3s%2BtCp3qVG%2F7E9Yo%2BIIjSOyrkAiEA%2F4iv4DQaCS3MOWxBb1Qq%2BGYc7UABxA%2BOtqX9p%2Bd8YGAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDEt%2B4L6DdAZmUXI8HCrcAzujz5I2CofNB6oNmxxViSvncmHLP0BE5uBndvoFYtBZDo7vvrx3miqR5lwtij6Fqsu3sWEx5gSKbG0nKx6mx7Kdc0k1f%2FhPhRF1fz4JR5RX8Oyk9XrblvFGza8UWtBhP0vN4Z9aBDcWPdYXeRI8cZ3U3w1yqrrugXThXCKXlsRHRYsu6n5q5V006Be9297oq6e%2FcEhuwpe3LMjehhC%2BmYBUHr82TMWHtvddxGfO2mUkRMERbyJhkwJQ%2Bgi18mHSihcCwjdlyWGekA%2BUYvdelK%2Bj4ey9UKSExlnS5fq6CNxUyEeeTPbyVuVht8SHDePwbRdZPpKnwZ8fSu5R2u4yEvFSvUcNEqiBCaKy9MPCs9r1nDa2ts5c7uxb2htHIbAdzVmsphNJiVicVp1UpYvoAO%2BP9YRIXk4keO1yMgza%2BXfKbbBIsQKIf%2FYrCcOAuHLPuoMYqB2Unt3Vswe1%2BCdPiU%2FO%2BkWGx9iVJ65n2Hy2mEC4Lpd25%2Bp%2BeYkbqvZaN149UtdFjjTWG3twpDj8g7kPIWzd3TcQpyu2ghjbWSvLHxUAgkAX7Vhfb8r4R%2B2%2BdcBoDNiIUjv0ADsue%2BbWo%2FVYKFn2PKaI11%2BlvdP9Ny7%2BQOlOpVk%2BA%2FX1aPpbSkg7MLS%2Bhr0GOqUBRXuqOvvHs1nHEPq8hIK8zXbXNEnHIpxlGI6t91zY6nCbpEsbvBFWw%2F7mM0gICnW4zfvWaqoXqJb5Z4iTqMG%2BdjyzWZ%2FktweXAAmJwa4yEFYNuUfynsRSJaNNNgwtg2ffm36x6eDun3lZKrFXorLHc%2FF2LB9BD4s5DdmjZ5Zy8Jtd1UQ0qGWrQEGcCFhwFjlVB5g8z8o5R%2BrvTB%2FuQEgu%2Bq73kBoU&X-Amz-Signature=4aa9b2e13cc526f67eb9dd79198b83365a9aff03c41a138ccaa7a91c177f2dae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTBS7CLM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIBUvWNsI7Myp7z0aU4T3s%2BtCp3qVG%2F7E9Yo%2BIIjSOyrkAiEA%2F4iv4DQaCS3MOWxBb1Qq%2BGYc7UABxA%2BOtqX9p%2Bd8YGAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDEt%2B4L6DdAZmUXI8HCrcAzujz5I2CofNB6oNmxxViSvncmHLP0BE5uBndvoFYtBZDo7vvrx3miqR5lwtij6Fqsu3sWEx5gSKbG0nKx6mx7Kdc0k1f%2FhPhRF1fz4JR5RX8Oyk9XrblvFGza8UWtBhP0vN4Z9aBDcWPdYXeRI8cZ3U3w1yqrrugXThXCKXlsRHRYsu6n5q5V006Be9297oq6e%2FcEhuwpe3LMjehhC%2BmYBUHr82TMWHtvddxGfO2mUkRMERbyJhkwJQ%2Bgi18mHSihcCwjdlyWGekA%2BUYvdelK%2Bj4ey9UKSExlnS5fq6CNxUyEeeTPbyVuVht8SHDePwbRdZPpKnwZ8fSu5R2u4yEvFSvUcNEqiBCaKy9MPCs9r1nDa2ts5c7uxb2htHIbAdzVmsphNJiVicVp1UpYvoAO%2BP9YRIXk4keO1yMgza%2BXfKbbBIsQKIf%2FYrCcOAuHLPuoMYqB2Unt3Vswe1%2BCdPiU%2FO%2BkWGx9iVJ65n2Hy2mEC4Lpd25%2Bp%2BeYkbqvZaN149UtdFjjTWG3twpDj8g7kPIWzd3TcQpyu2ghjbWSvLHxUAgkAX7Vhfb8r4R%2B2%2BdcBoDNiIUjv0ADsue%2BbWo%2FVYKFn2PKaI11%2BlvdP9Ny7%2BQOlOpVk%2BA%2FX1aPpbSkg7MLS%2Bhr0GOqUBRXuqOvvHs1nHEPq8hIK8zXbXNEnHIpxlGI6t91zY6nCbpEsbvBFWw%2F7mM0gICnW4zfvWaqoXqJb5Z4iTqMG%2BdjyzWZ%2FktweXAAmJwa4yEFYNuUfynsRSJaNNNgwtg2ffm36x6eDun3lZKrFXorLHc%2FF2LB9BD4s5DdmjZ5Zy8Jtd1UQ0qGWrQEGcCFhwFjlVB5g8z8o5R%2BrvTB%2FuQEgu%2Bq73kBoU&X-Amz-Signature=8b93182f3430e4365510571791b14ca472efb5536eed64fb64e7d44de92518c5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTNNX5NK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIFiufRJCG5BGOFPvZYU5XjfniJsGeyMgNf%2FmrjDKPENbAiEAw3xVviDFaC0SLkC6CaDFGPz3EvuY0IVwGcBRh6FMSbgq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDP4KPfjVAOLMR7poKircA8hNWAOtBFxxknSDq2MXysG7wdkJV6v319pzkg7jr9l2CD7E57ux5f1J9DfmGfIbLy7%2Fog%2Bqa%2BMWirGVa7J0xmUyf%2Flj7Axwu3F%2BsiLxDgwmiBzJlE7%2B8e3M0Hoote%2F29L6bN%2FtU3w%2BGGwxlV%2FCspF1J32ANRqbqGj9rutx8V6qDlf0PvqI0htp4kJw86mXEdSwJVfBNABNq%2BkKBnOre9KMI0Ce4Q%2Fnz7Zo%2BrFf7Sej3hFrs2POia2Rvu9tb%2BTf5pHC5l%2FeAFyxMtbYPbTdIvUGvMoJin2OVfT18%2FuAoSbGrLkZVF7aFSObh9TPRP0NggEFeW0E7hfUChgLdVbd6Rz4hwGbXt700eWzHgvi8VmYodAgvEMvny0Veokk3MT0brlDBN2dFuut%2Ft9XyLnCfdCYYldryEdjXwsFsrCNudw0BGBGf1jB4huPW%2B4U%2FkXbeo4WzWUvz2mAfJ4aM9dGQD5vO8339wiKdEGAcKLPLCuW5A9ftxXfapcMVEzWp0qcRq8tZIlupEtWdYPSlHLHYl4Pnn9cKCPEW3o80pEjJWmo9NOzHw%2FDmdzvxpfD5%2FOZxVLrgQvHftkHbFkspk5aLzFOYZna89CQzih4DqAcTgb0C3%2F5hM5DDiE4Oe9uJMPG%2Bhr0GOqUBJ6FzYxwUHNXBDG7%2FHmVUNTTvb8OhUmiYFsQRGg8ueTxtoEJrrjFyg5ZYgqitNshPrM18IwzL6vD5FuoZA0WPwbjnWqgAxnxAwDSdeXNS0IBEcJjetW4zGHnlQ%2FXMTb4aP5k%2Bui3JOCwQGL7HXOIr6hvPSscMiCBHROhjGU4JGSDhbb2M3%2F4iL98PdZoKYdTX7aVwgH2TGgxv8iUecrffWb8LnGVi&X-Amz-Signature=950632fb9610306356481d4d081e887b02d6cc9fb36b6708520d3305586967e1&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SO6BWXLE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIG4v2Zt978sYAhf8SNX7WAhfVcKyZk7qX%2Ff6fQpI3cwrAiEAx2pGyOCdbVxhEGIiEVDgwCwaUrcZwpgwCFt4DWA7x9Yq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNZAGMMQk3u8Tm9oXyrcA%2Bu7YydasGGq4gaKowiKrmThIetp67dQWUHcx4GK%2FF25%2FZ4OFK4yWdRr4t0GKh3h4S6xfVkXn6gssM9k7xZCNthao6OiBYSFp7w4QxmUvv9i46JVAw73iwTMu743rz9ApIx5l2XcAcXyHTWywi24KvkiP%2FRRgcjDKyilkZpLitGJ48BZajyxovxTLSWo8b9KNHP%2FRcYdwSCxNM4l3nBE2OuxgzX%2FZn5NjM78D1bn3fF1Z10HVRUHBfqjqxKh%2Bsl01ljNGDgGJT66XilDUG2yRyoSKaqVQ5g%2BcURDgEOVqj8e5ys67mpIprZDhHMEikfGQUSgY2vOlqVxIfHho41hlFSnRV7akdLkKvbfFeoFVsKAuGQaKqUYvNVmdOnntTP4HgHshwCqrhM5pV6xE6YenJcPHeGremU7iW%2FEs9TPL8Fn2lrCDMT1quF%2Bu75cSD01hVHSr4TNCVMjM7pIp%2F3meRLs8zPRTHA5REJCXOiKgvm7Ontfe2eiV6oR5u9KPf6ES7oS%2B7GcZUrBg%2B%2FkQ6mcBs2JSc6SBY8%2FWW9y0Jp5HdQ6rRNtDhkI8Q1iynU%2FWcFa4egpwigtGRPXNNXAZZHirVRlrPNndDTPvxSOlFnAtO0oDofeJkS7rvCYsrXHMIS%2Fhr0GOqUBl5WkSFrYKd7kQxTYz6WZgFMPvKaWpNbRT%2FWUyOXdSRCTnIl7m%2F07HQTrzfSDQJbruzLx%2Bcatcw%2FdzfE2RmGJKXrhyqQIlvJi8Fh7L5GMdCNqGIcUn1lRegtQz0GlMUQ7u6%2F2Y00GeVF5leNcFSvNl0xrjsD7gf7TNcmMeVzgFM8WV0%2FeugL5Q1kgZIhITVVhuqjllUKU6itxzLh2F2waBOiGeVyy&X-Amz-Signature=e4880105a0b6032a812bd1dbda75761efe57944c9a96774a8c24f0168786842c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XATG3STZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIDhkFtD4JvYw%2BlwMUq6ozju15KGGTf5VasKlRV323%2Fe%2BAiAKsC4b8kHdSu%2BQTIeqlBOJhIHSq4c7mClHAzFr0tEjHir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMfNB%2BzwWKayf0fkDHKtwD7ZhbA5wSXgew0n%2FA2DI1ANBjM0P74Dv3uYdhEqIY5ykd%2BkS8InfTGVAa2V%2BF4pD4ToPFCiA7S3kzOcqrlw3P9HFSNYtaAs5JlyxF8UWxPSEJrWsROiOTqEC2J0nhRI%2B3lV5pr6p9nc5%2FOj5LEV22QzsJTR%2BuPesyEiWn9bhtfENaBENluMoSKOVRrMLEfYEwJllMJoT7G70yi43qmjfTYuA00dDUZDRg%2BzV60m6iItCO9f6QvCnRFG%2BAOpfMm228t2QhvwBDQvhleF9oZfjI3SNG%2FjMKOCVn7L%2FoPPX0MXbLtdERkLEsUfVL72VEX5828LIrnXPSs3Id%2FPzBrpDL4Tcfus80DxgRFAIeoVj32272OZzbwTnJ%2BUFqpJptw0I%2B9XZgOHlIjXGM6ABJkLF1Qy8mKThH2IZ46FMXKdHHt29QWvTIsqI3oLien3G6wWdU%2BGq0s6S%2BS2iAAH1ViOAkdBvOujGEYJRicSq8M6nfgRmBx61dzLtIVXqolwc6ulR%2BcBRPmaUdXuzmX05kKtnKUfeBw2WmNm58b7sg5cUScrVVNVerb0e2bl7MHsA%2FtlP2ewvaJsrcWfMJxmPAEiD5EKy5g409gI6Z3SUNR%2FUOJ2joY4Bvrj5%2BQCVN%2BGow776GvQY6pgHhN7lZ0pI%2FZHauJ%2B0ZNAfXKzLWtuwqp57DW%2BPgxeYTs9CBy3qvxDEBxBd0MktmV9iY1OjsGwHhtkudOuYz7UQlnZOca0sKendauPEgXpkb44A%2B8t%2F%2B7Fo1npHJFpYnDP9OXjGs%2FXYOPVWAN0SCalX6F2csCnmowiG8vRiOVmVKN4cO7sk%2BnJyjC8jV4naFdiZg0DAMDrqF1qt2dF6hVLp22jWvY19B&X-Amz-Signature=c20a7f0a33269ab15104752880fe2f2e18a9dadc7bc0d0b25d38086f6a150dce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB4JIRBJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCBdPGaTpbdfWhgdvokLAR2Llpi2LiyixnI5iV6osjl1gIhAKW45uIY7sMxLDZ%2BzX9NBDNekZjhEaZaIn7nL4fjQWIsKv8DCCYQABoMNjM3NDIzMTgzODA1IgwlWu66h3soFkwNHwIq3AO8x652%2B5VzDNObPlf%2F7EHrmmJFcDfZ%2ByODAXDC%2FuAMlctAVejYn1yo584ax33NyWpsx6ydo0Y33Lltym3F4pyZQSgEmMa4%2BDdRMHK3IZkix%2FBQH8hF4Aor%2BQkj4Y4CNnnN0%2FXNVj9h7tmqF0JU3cdeTyFuwOSJIWPeu5gflqJj7YweHAUVWnM3FPxrKTh7XtwpG%2FUUeM%2BgyFI0mqGNNWvolJl1QaOoUAkrVQarhWhqCbkmo%2BHjxCfJ9IA3Z2NPKsPXUc%2FkND9nbfw8xc2kMjougl%2FBld2IN%2BnlYdZ56kwYObxOkbsR1l8EXGDIBQ0AtdWVkn8xcPRZJ%2BpJpOM4thKnNGcyTrJtmAOcKQiWczOGvWbQvpdB%2FP2R93Qc1QAM2cVjwwVbB5CAWwIwf4M66v5uXtrhqbBNdXZdZsU23k5LYdnVzha610HiKAS8Y9obMp%2FG2bnbYRk3i03fenAX6twxsod8KW2snFMw1BHB%2B9Koo4D1pVN2lenMA6yRiinvUQBq5kFXCn%2FfGl9vekoj8NikxRdmjew8E%2F%2BdG4wQTOToOPcU%2FVBPyhXw4QAwc9K6OITrwDO51Z6t%2FuVS6ygDl3srA8VF7rHqSzR5Xc2vzcmTX4QTEUgYMYbe9Bs8GDDgvoa9BjqkAWrHOdbKJTKq3Xp99CdTbwgZGlo3WJVpIPQuEM8OjANru3dRqmIKrZTYuGllqN7p%2FM5Jim2kc5%2Bfw%2BUqoDLBEFzmj%2B8kbySiGyOjm%2Fjw2w06XZTIqy3Uqo1xddFJ9khOdAkCbfp69F6lAjJG1E%2BzVNxytSbbAvOOBpIC5grMpQ8InPpiiMrDHIPes4NAQmyo6ULWm5aUMh4ZCi52di6DaZUjpx90&X-Amz-Signature=b0cbf7396c766b2a7cb1072ffd420c59406221e2ada57cbccad8053bd64a1806&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB4JIRBJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCBdPGaTpbdfWhgdvokLAR2Llpi2LiyixnI5iV6osjl1gIhAKW45uIY7sMxLDZ%2BzX9NBDNekZjhEaZaIn7nL4fjQWIsKv8DCCYQABoMNjM3NDIzMTgzODA1IgwlWu66h3soFkwNHwIq3AO8x652%2B5VzDNObPlf%2F7EHrmmJFcDfZ%2ByODAXDC%2FuAMlctAVejYn1yo584ax33NyWpsx6ydo0Y33Lltym3F4pyZQSgEmMa4%2BDdRMHK3IZkix%2FBQH8hF4Aor%2BQkj4Y4CNnnN0%2FXNVj9h7tmqF0JU3cdeTyFuwOSJIWPeu5gflqJj7YweHAUVWnM3FPxrKTh7XtwpG%2FUUeM%2BgyFI0mqGNNWvolJl1QaOoUAkrVQarhWhqCbkmo%2BHjxCfJ9IA3Z2NPKsPXUc%2FkND9nbfw8xc2kMjougl%2FBld2IN%2BnlYdZ56kwYObxOkbsR1l8EXGDIBQ0AtdWVkn8xcPRZJ%2BpJpOM4thKnNGcyTrJtmAOcKQiWczOGvWbQvpdB%2FP2R93Qc1QAM2cVjwwVbB5CAWwIwf4M66v5uXtrhqbBNdXZdZsU23k5LYdnVzha610HiKAS8Y9obMp%2FG2bnbYRk3i03fenAX6twxsod8KW2snFMw1BHB%2B9Koo4D1pVN2lenMA6yRiinvUQBq5kFXCn%2FfGl9vekoj8NikxRdmjew8E%2F%2BdG4wQTOToOPcU%2FVBPyhXw4QAwc9K6OITrwDO51Z6t%2FuVS6ygDl3srA8VF7rHqSzR5Xc2vzcmTX4QTEUgYMYbe9Bs8GDDgvoa9BjqkAWrHOdbKJTKq3Xp99CdTbwgZGlo3WJVpIPQuEM8OjANru3dRqmIKrZTYuGllqN7p%2FM5Jim2kc5%2Bfw%2BUqoDLBEFzmj%2B8kbySiGyOjm%2Fjw2w06XZTIqy3Uqo1xddFJ9khOdAkCbfp69F6lAjJG1E%2BzVNxytSbbAvOOBpIC5grMpQ8InPpiiMrDHIPes4NAQmyo6ULWm5aUMh4ZCi52di6DaZUjpx90&X-Amz-Signature=e03a2c2791921f8dc4be12756b7a5eee5b87d91f29df8e98a8778c93c90f0406&X-Amz-SignedHeaders=host&x-id=GetObject)

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
