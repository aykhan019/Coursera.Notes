

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SASMKXZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIADBmlD9ia7awRec7inE8%2B6%2FfriVuPYpZjZysdb06b9FAiEAs8W9KMh3HswVNFYCX%2BMpYwcQQAX2U5nIj9IYG4Qw8LsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFDEFRuVV0f%2BVuzvCrcA%2Fie2FtZwO14sEpiOQFksEbHrq%2BOKQ9ymyC1uYX4p42KBbatUz1MvMMBH%2BwVKr%2Fa1DNS6LlFmJ4El2zKZPcyUp9OI4ounUh9FGFUL5u9FmUwsrmeTNX0NtzUHrT8xQVFli6FQBqktAZDfYkwQqFtxrwqFasg8zi8zZGqXFFYLdCf8aw0yESZmrVgtbOuSdYK9AosmXRyge8tCjCMZCWD8%2FqZPpjwVtoSj%2B9dupKtbciXn6bPKlgvmhgQYw%2FIJr%2FdES9pHhT1xw7imIuKbllKavcWEqSY8G6L0Pm3nXeuIC6fQHytBR7gd1OtAZTBqeZnS%2FsLSmtV0xYKKWlqDIl5nqoUjQZPxawOYc9eQ00eubauNy%2BWjF7A4Euwo%2BEvbZWhiacLUtf4uhUK%2F25RZJvbbuc%2B4a2ikJhg32VTRePjDzG%2FQ5xQOO2M%2FoLpY6YVfet1ZXwpVec7Y86vkO05NXFlnLwV94hLL7NLvPfwQs44%2FP7D0plN14QUseeMxvFnu%2BCEv%2Fjy0OPsSyN7WIDm0qI1NR6CiZBqR8qQwVqUCXajd6%2B0qV%2FaVwnkJBYacVa%2BrXOp%2B6E9APTCj4fgD%2B03h9QP9b3MIXTobF4SUf7Nl3ten6hotcqjtwdLmLsaqijOMOS76bwGOqUBhabVTVWf4NLnlITktdxqJd9Ob99rcL8hZcHuHTQ1i31atDEAvbjbSJ%2Bu2IBeEpeGJGdwpvnqslRInf9IbORhyI1oY8vFS4PWhGIAWKGzaaoILZu%2Bqb%2BmMcOPOiKZNLb5VqXRDneMM88bRG0sFvJhM4nzpw%2FDT2A6relWntQdZQsRhIrz%2Bt6%2FiA9u8JL1Vwd0potIG19a5fcTSYw%2FX8Qr%2BJmGp50W&X-Amz-Signature=7f7a29cd393b0c7dadf2d4f502bee219c6f834fe74da47dc5f3af24452938356&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SASMKXZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIADBmlD9ia7awRec7inE8%2B6%2FfriVuPYpZjZysdb06b9FAiEAs8W9KMh3HswVNFYCX%2BMpYwcQQAX2U5nIj9IYG4Qw8LsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFDEFRuVV0f%2BVuzvCrcA%2Fie2FtZwO14sEpiOQFksEbHrq%2BOKQ9ymyC1uYX4p42KBbatUz1MvMMBH%2BwVKr%2Fa1DNS6LlFmJ4El2zKZPcyUp9OI4ounUh9FGFUL5u9FmUwsrmeTNX0NtzUHrT8xQVFli6FQBqktAZDfYkwQqFtxrwqFasg8zi8zZGqXFFYLdCf8aw0yESZmrVgtbOuSdYK9AosmXRyge8tCjCMZCWD8%2FqZPpjwVtoSj%2B9dupKtbciXn6bPKlgvmhgQYw%2FIJr%2FdES9pHhT1xw7imIuKbllKavcWEqSY8G6L0Pm3nXeuIC6fQHytBR7gd1OtAZTBqeZnS%2FsLSmtV0xYKKWlqDIl5nqoUjQZPxawOYc9eQ00eubauNy%2BWjF7A4Euwo%2BEvbZWhiacLUtf4uhUK%2F25RZJvbbuc%2B4a2ikJhg32VTRePjDzG%2FQ5xQOO2M%2FoLpY6YVfet1ZXwpVec7Y86vkO05NXFlnLwV94hLL7NLvPfwQs44%2FP7D0plN14QUseeMxvFnu%2BCEv%2Fjy0OPsSyN7WIDm0qI1NR6CiZBqR8qQwVqUCXajd6%2B0qV%2FaVwnkJBYacVa%2BrXOp%2B6E9APTCj4fgD%2B03h9QP9b3MIXTobF4SUf7Nl3ten6hotcqjtwdLmLsaqijOMOS76bwGOqUBhabVTVWf4NLnlITktdxqJd9Ob99rcL8hZcHuHTQ1i31atDEAvbjbSJ%2Bu2IBeEpeGJGdwpvnqslRInf9IbORhyI1oY8vFS4PWhGIAWKGzaaoILZu%2Bqb%2BmMcOPOiKZNLb5VqXRDneMM88bRG0sFvJhM4nzpw%2FDT2A6relWntQdZQsRhIrz%2Bt6%2FiA9u8JL1Vwd0potIG19a5fcTSYw%2FX8Qr%2BJmGp50W&X-Amz-Signature=d9980f54ee6bbb69c120de8f396ae3818ee4e2172b2670bbb10c9a76ba7450bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SASMKXZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIADBmlD9ia7awRec7inE8%2B6%2FfriVuPYpZjZysdb06b9FAiEAs8W9KMh3HswVNFYCX%2BMpYwcQQAX2U5nIj9IYG4Qw8LsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFDEFRuVV0f%2BVuzvCrcA%2Fie2FtZwO14sEpiOQFksEbHrq%2BOKQ9ymyC1uYX4p42KBbatUz1MvMMBH%2BwVKr%2Fa1DNS6LlFmJ4El2zKZPcyUp9OI4ounUh9FGFUL5u9FmUwsrmeTNX0NtzUHrT8xQVFli6FQBqktAZDfYkwQqFtxrwqFasg8zi8zZGqXFFYLdCf8aw0yESZmrVgtbOuSdYK9AosmXRyge8tCjCMZCWD8%2FqZPpjwVtoSj%2B9dupKtbciXn6bPKlgvmhgQYw%2FIJr%2FdES9pHhT1xw7imIuKbllKavcWEqSY8G6L0Pm3nXeuIC6fQHytBR7gd1OtAZTBqeZnS%2FsLSmtV0xYKKWlqDIl5nqoUjQZPxawOYc9eQ00eubauNy%2BWjF7A4Euwo%2BEvbZWhiacLUtf4uhUK%2F25RZJvbbuc%2B4a2ikJhg32VTRePjDzG%2FQ5xQOO2M%2FoLpY6YVfet1ZXwpVec7Y86vkO05NXFlnLwV94hLL7NLvPfwQs44%2FP7D0plN14QUseeMxvFnu%2BCEv%2Fjy0OPsSyN7WIDm0qI1NR6CiZBqR8qQwVqUCXajd6%2B0qV%2FaVwnkJBYacVa%2BrXOp%2B6E9APTCj4fgD%2B03h9QP9b3MIXTobF4SUf7Nl3ten6hotcqjtwdLmLsaqijOMOS76bwGOqUBhabVTVWf4NLnlITktdxqJd9Ob99rcL8hZcHuHTQ1i31atDEAvbjbSJ%2Bu2IBeEpeGJGdwpvnqslRInf9IbORhyI1oY8vFS4PWhGIAWKGzaaoILZu%2Bqb%2BmMcOPOiKZNLb5VqXRDneMM88bRG0sFvJhM4nzpw%2FDT2A6relWntQdZQsRhIrz%2Bt6%2FiA9u8JL1Vwd0potIG19a5fcTSYw%2FX8Qr%2BJmGp50W&X-Amz-Signature=e17ebf1db2ec46ea54af03b7de84f000f7e9cb642b7969a021ce477a1b352491&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3HUWTY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsc5vH5dLt25RpQ29XstiKhpGOXlGVenXwr4zy8336wwIgbRj4ff2Sp1M0LqGq6s6zyY7qd9IanS%2BDV%2BCnJImbe%2FsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBE6m4YHTNrMbtrjyrcA8uQKOqqwP195VXGB%2FZ6mTBH6KwRrOFZYnS01UzpTlq2hb2HJxZnDHoog4uD6KWSXvp7yEup7upgqGmBeUEs6JnSJ43TuzJEH7FsLGRXL8vNaT1pjE9FghQ39edmFd69QQWYZiYgX6WJIUDhcqwqn%2B%2F4a7cJVhMyuwSkR5fnufA6HpzhxDV5m1RBcBK%2FX4DuF36NwC9zzXhHrVW9c15TNwW1K3XE0ntPVrTUgnhuj6tK%2FvTSTHbCeDuTNB%2BRyh7%2FwE8sKSuWsJswX%2Fnu039R3Jh5HV%2FhaRLDzLD2YafbUVT%2FamOkO4z3%2FwvbtyZIJ140A5R2MjClV8ytwlUzgG9c9EDomQnaWRzQ1pzxjYrBNq3AjCCF1tK90TwE%2BkuQtVSOBdk2TVIDub99dEyY9f0Ziv7K7o%2Fhlw0n6U4QrY5dO7U%2B9GEL8X21%2F0EAOSd424g5zmV4PBJzLL9FbSn58kspoYDl5PuO80c05YWkNEQvx3%2F2%2F%2FPHe4C1DaSp9T8m%2FiYzDMmGDteXqzBBkjI%2BVnu1dqt4heYkI3D9t9eqaFl%2Fgid2XDEU%2FpzGhRMCUBvBNXyVBLsfyCDRvz7CssjFEGGxqSy3cRPOwSPkkkQl66lWST6YUmaLUQJhleWDONaxMJq86bwGOqUBGLTTWhxai1zphcjLY1F%2FtHIDXAwsmGyBU6ckNcmlQ8t53kAXPZOBFrcRRwXC%2Flol7L6EsUrnWWFFmTjoZuo988L9jjDHsKoLVYZo%2FWtr0gcBcs3cv4zVZe29X6R%2FnXCxCMftWjkIsH4SdraZ%2Bem0WpQ042ruaWKu%2BNDxZnKlH%2FTyau4q065gQSuiqGRs5YjsUNMZ1ME%2FImgyWy%2BnvZ1TvHtxwPdZ&X-Amz-Signature=e5c33cd56fc7a4edc1bd62ac8dea62cbca07d39b0395931760ea5411480d2e0e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3HUWTY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsc5vH5dLt25RpQ29XstiKhpGOXlGVenXwr4zy8336wwIgbRj4ff2Sp1M0LqGq6s6zyY7qd9IanS%2BDV%2BCnJImbe%2FsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBE6m4YHTNrMbtrjyrcA8uQKOqqwP195VXGB%2FZ6mTBH6KwRrOFZYnS01UzpTlq2hb2HJxZnDHoog4uD6KWSXvp7yEup7upgqGmBeUEs6JnSJ43TuzJEH7FsLGRXL8vNaT1pjE9FghQ39edmFd69QQWYZiYgX6WJIUDhcqwqn%2B%2F4a7cJVhMyuwSkR5fnufA6HpzhxDV5m1RBcBK%2FX4DuF36NwC9zzXhHrVW9c15TNwW1K3XE0ntPVrTUgnhuj6tK%2FvTSTHbCeDuTNB%2BRyh7%2FwE8sKSuWsJswX%2Fnu039R3Jh5HV%2FhaRLDzLD2YafbUVT%2FamOkO4z3%2FwvbtyZIJ140A5R2MjClV8ytwlUzgG9c9EDomQnaWRzQ1pzxjYrBNq3AjCCF1tK90TwE%2BkuQtVSOBdk2TVIDub99dEyY9f0Ziv7K7o%2Fhlw0n6U4QrY5dO7U%2B9GEL8X21%2F0EAOSd424g5zmV4PBJzLL9FbSn58kspoYDl5PuO80c05YWkNEQvx3%2F2%2F%2FPHe4C1DaSp9T8m%2FiYzDMmGDteXqzBBkjI%2BVnu1dqt4heYkI3D9t9eqaFl%2Fgid2XDEU%2FpzGhRMCUBvBNXyVBLsfyCDRvz7CssjFEGGxqSy3cRPOwSPkkkQl66lWST6YUmaLUQJhleWDONaxMJq86bwGOqUBGLTTWhxai1zphcjLY1F%2FtHIDXAwsmGyBU6ckNcmlQ8t53kAXPZOBFrcRRwXC%2Flol7L6EsUrnWWFFmTjoZuo988L9jjDHsKoLVYZo%2FWtr0gcBcs3cv4zVZe29X6R%2FnXCxCMftWjkIsH4SdraZ%2Bem0WpQ042ruaWKu%2BNDxZnKlH%2FTyau4q065gQSuiqGRs5YjsUNMZ1ME%2FImgyWy%2BnvZ1TvHtxwPdZ&X-Amz-Signature=f9386ae900d5ca383c732e22d88ce9cc9bf1d57248a7ff47ab4a4679fb028c5f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3HUWTY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsc5vH5dLt25RpQ29XstiKhpGOXlGVenXwr4zy8336wwIgbRj4ff2Sp1M0LqGq6s6zyY7qd9IanS%2BDV%2BCnJImbe%2FsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBE6m4YHTNrMbtrjyrcA8uQKOqqwP195VXGB%2FZ6mTBH6KwRrOFZYnS01UzpTlq2hb2HJxZnDHoog4uD6KWSXvp7yEup7upgqGmBeUEs6JnSJ43TuzJEH7FsLGRXL8vNaT1pjE9FghQ39edmFd69QQWYZiYgX6WJIUDhcqwqn%2B%2F4a7cJVhMyuwSkR5fnufA6HpzhxDV5m1RBcBK%2FX4DuF36NwC9zzXhHrVW9c15TNwW1K3XE0ntPVrTUgnhuj6tK%2FvTSTHbCeDuTNB%2BRyh7%2FwE8sKSuWsJswX%2Fnu039R3Jh5HV%2FhaRLDzLD2YafbUVT%2FamOkO4z3%2FwvbtyZIJ140A5R2MjClV8ytwlUzgG9c9EDomQnaWRzQ1pzxjYrBNq3AjCCF1tK90TwE%2BkuQtVSOBdk2TVIDub99dEyY9f0Ziv7K7o%2Fhlw0n6U4QrY5dO7U%2B9GEL8X21%2F0EAOSd424g5zmV4PBJzLL9FbSn58kspoYDl5PuO80c05YWkNEQvx3%2F2%2F%2FPHe4C1DaSp9T8m%2FiYzDMmGDteXqzBBkjI%2BVnu1dqt4heYkI3D9t9eqaFl%2Fgid2XDEU%2FpzGhRMCUBvBNXyVBLsfyCDRvz7CssjFEGGxqSy3cRPOwSPkkkQl66lWST6YUmaLUQJhleWDONaxMJq86bwGOqUBGLTTWhxai1zphcjLY1F%2FtHIDXAwsmGyBU6ckNcmlQ8t53kAXPZOBFrcRRwXC%2Flol7L6EsUrnWWFFmTjoZuo988L9jjDHsKoLVYZo%2FWtr0gcBcs3cv4zVZe29X6R%2FnXCxCMftWjkIsH4SdraZ%2Bem0WpQ042ruaWKu%2BNDxZnKlH%2FTyau4q065gQSuiqGRs5YjsUNMZ1ME%2FImgyWy%2BnvZ1TvHtxwPdZ&X-Amz-Signature=9f67ef345523a0ee7345100265e149c41e205848e31bd1178b0b74652a7d6800&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3HUWTY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsc5vH5dLt25RpQ29XstiKhpGOXlGVenXwr4zy8336wwIgbRj4ff2Sp1M0LqGq6s6zyY7qd9IanS%2BDV%2BCnJImbe%2FsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBE6m4YHTNrMbtrjyrcA8uQKOqqwP195VXGB%2FZ6mTBH6KwRrOFZYnS01UzpTlq2hb2HJxZnDHoog4uD6KWSXvp7yEup7upgqGmBeUEs6JnSJ43TuzJEH7FsLGRXL8vNaT1pjE9FghQ39edmFd69QQWYZiYgX6WJIUDhcqwqn%2B%2F4a7cJVhMyuwSkR5fnufA6HpzhxDV5m1RBcBK%2FX4DuF36NwC9zzXhHrVW9c15TNwW1K3XE0ntPVrTUgnhuj6tK%2FvTSTHbCeDuTNB%2BRyh7%2FwE8sKSuWsJswX%2Fnu039R3Jh5HV%2FhaRLDzLD2YafbUVT%2FamOkO4z3%2FwvbtyZIJ140A5R2MjClV8ytwlUzgG9c9EDomQnaWRzQ1pzxjYrBNq3AjCCF1tK90TwE%2BkuQtVSOBdk2TVIDub99dEyY9f0Ziv7K7o%2Fhlw0n6U4QrY5dO7U%2B9GEL8X21%2F0EAOSd424g5zmV4PBJzLL9FbSn58kspoYDl5PuO80c05YWkNEQvx3%2F2%2F%2FPHe4C1DaSp9T8m%2FiYzDMmGDteXqzBBkjI%2BVnu1dqt4heYkI3D9t9eqaFl%2Fgid2XDEU%2FpzGhRMCUBvBNXyVBLsfyCDRvz7CssjFEGGxqSy3cRPOwSPkkkQl66lWST6YUmaLUQJhleWDONaxMJq86bwGOqUBGLTTWhxai1zphcjLY1F%2FtHIDXAwsmGyBU6ckNcmlQ8t53kAXPZOBFrcRRwXC%2Flol7L6EsUrnWWFFmTjoZuo988L9jjDHsKoLVYZo%2FWtr0gcBcs3cv4zVZe29X6R%2FnXCxCMftWjkIsH4SdraZ%2Bem0WpQ042ruaWKu%2BNDxZnKlH%2FTyau4q065gQSuiqGRs5YjsUNMZ1ME%2FImgyWy%2BnvZ1TvHtxwPdZ&X-Amz-Signature=fb6adab89d9870aa81119a438ba99d78f458634140eeeaa64ed857094d3f2d98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3HUWTY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsc5vH5dLt25RpQ29XstiKhpGOXlGVenXwr4zy8336wwIgbRj4ff2Sp1M0LqGq6s6zyY7qd9IanS%2BDV%2BCnJImbe%2FsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBE6m4YHTNrMbtrjyrcA8uQKOqqwP195VXGB%2FZ6mTBH6KwRrOFZYnS01UzpTlq2hb2HJxZnDHoog4uD6KWSXvp7yEup7upgqGmBeUEs6JnSJ43TuzJEH7FsLGRXL8vNaT1pjE9FghQ39edmFd69QQWYZiYgX6WJIUDhcqwqn%2B%2F4a7cJVhMyuwSkR5fnufA6HpzhxDV5m1RBcBK%2FX4DuF36NwC9zzXhHrVW9c15TNwW1K3XE0ntPVrTUgnhuj6tK%2FvTSTHbCeDuTNB%2BRyh7%2FwE8sKSuWsJswX%2Fnu039R3Jh5HV%2FhaRLDzLD2YafbUVT%2FamOkO4z3%2FwvbtyZIJ140A5R2MjClV8ytwlUzgG9c9EDomQnaWRzQ1pzxjYrBNq3AjCCF1tK90TwE%2BkuQtVSOBdk2TVIDub99dEyY9f0Ziv7K7o%2Fhlw0n6U4QrY5dO7U%2B9GEL8X21%2F0EAOSd424g5zmV4PBJzLL9FbSn58kspoYDl5PuO80c05YWkNEQvx3%2F2%2F%2FPHe4C1DaSp9T8m%2FiYzDMmGDteXqzBBkjI%2BVnu1dqt4heYkI3D9t9eqaFl%2Fgid2XDEU%2FpzGhRMCUBvBNXyVBLsfyCDRvz7CssjFEGGxqSy3cRPOwSPkkkQl66lWST6YUmaLUQJhleWDONaxMJq86bwGOqUBGLTTWhxai1zphcjLY1F%2FtHIDXAwsmGyBU6ckNcmlQ8t53kAXPZOBFrcRRwXC%2Flol7L6EsUrnWWFFmTjoZuo988L9jjDHsKoLVYZo%2FWtr0gcBcs3cv4zVZe29X6R%2FnXCxCMftWjkIsH4SdraZ%2Bem0WpQ042ruaWKu%2BNDxZnKlH%2FTyau4q065gQSuiqGRs5YjsUNMZ1ME%2FImgyWy%2BnvZ1TvHtxwPdZ&X-Amz-Signature=662a94c80765585c21b0c639df1de18478820559e492f86b3b2c962a413bba0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3HUWTY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsc5vH5dLt25RpQ29XstiKhpGOXlGVenXwr4zy8336wwIgbRj4ff2Sp1M0LqGq6s6zyY7qd9IanS%2BDV%2BCnJImbe%2FsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBE6m4YHTNrMbtrjyrcA8uQKOqqwP195VXGB%2FZ6mTBH6KwRrOFZYnS01UzpTlq2hb2HJxZnDHoog4uD6KWSXvp7yEup7upgqGmBeUEs6JnSJ43TuzJEH7FsLGRXL8vNaT1pjE9FghQ39edmFd69QQWYZiYgX6WJIUDhcqwqn%2B%2F4a7cJVhMyuwSkR5fnufA6HpzhxDV5m1RBcBK%2FX4DuF36NwC9zzXhHrVW9c15TNwW1K3XE0ntPVrTUgnhuj6tK%2FvTSTHbCeDuTNB%2BRyh7%2FwE8sKSuWsJswX%2Fnu039R3Jh5HV%2FhaRLDzLD2YafbUVT%2FamOkO4z3%2FwvbtyZIJ140A5R2MjClV8ytwlUzgG9c9EDomQnaWRzQ1pzxjYrBNq3AjCCF1tK90TwE%2BkuQtVSOBdk2TVIDub99dEyY9f0Ziv7K7o%2Fhlw0n6U4QrY5dO7U%2B9GEL8X21%2F0EAOSd424g5zmV4PBJzLL9FbSn58kspoYDl5PuO80c05YWkNEQvx3%2F2%2F%2FPHe4C1DaSp9T8m%2FiYzDMmGDteXqzBBkjI%2BVnu1dqt4heYkI3D9t9eqaFl%2Fgid2XDEU%2FpzGhRMCUBvBNXyVBLsfyCDRvz7CssjFEGGxqSy3cRPOwSPkkkQl66lWST6YUmaLUQJhleWDONaxMJq86bwGOqUBGLTTWhxai1zphcjLY1F%2FtHIDXAwsmGyBU6ckNcmlQ8t53kAXPZOBFrcRRwXC%2Flol7L6EsUrnWWFFmTjoZuo988L9jjDHsKoLVYZo%2FWtr0gcBcs3cv4zVZe29X6R%2FnXCxCMftWjkIsH4SdraZ%2Bem0WpQ042ruaWKu%2BNDxZnKlH%2FTyau4q065gQSuiqGRs5YjsUNMZ1ME%2FImgyWy%2BnvZ1TvHtxwPdZ&X-Amz-Signature=ddf0d6acdde87bde69486fbbe511ad72e7a935dbc3150262f2bf7a78c0505ce3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGY6JI3E%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHm03Qs3CL1TanCpxjMSY8UKQgs0ThbUlvt1S%2FWqdsqLAiAiRYxgBO9Kv%2BPIiQX3OYB8lsZlx1x%2B0FJBFSjxXmyaKiqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoGp8Gi1zpumaZZA1KtwDmUWXAuiEdsGNLDOEoyOjy7%2Bmfvci4%2BZeCsA4CjL%2BElPMAciBStzbS2jDmw0oVn51nFrVRvdP1I7tNYIgOUP9%2Bcr4PEgaY6hxk4o7YG17KKMsxWXUb3UWAUR7cwkWbHQ%2FOt7%2FTgM3jfhBVMqvn8iBsS2WgrGvandQ59v0gh3F7udAEtGDFqTU%2FKDagucOKRwebTkemq4izHU8Leo6nkZO6bEjXsbhZJqsj3J8ED%2F1fLT6E74%2Ba9DrVEaRhU9ePtXnuUe0ZeBuQ08%2B3pnSxif1WvNBQZRUT%2F7tOVFEi27Uywr77dns7iMf3VBna%2B27XX3PeUBesMGaYO0FunACJi0gKvT1NHUXW1SMS%2BqNUm8xJ0fpdEjbXwDGQNNuOH3UI8u0i5puR539cdGLt8BKTt6wxLW2LtGbSzX0E3JWG4%2FEXODzYZt88DMpnetoeHoREYw3Kq2Wk%2FUDfnPh%2FPv5DP%2Fi%2FshuKxaSheSHhvATvlPU%2B02aUD%2By5VJhfbTMQXQlOYnhNl%2FboHOt%2BYnydrHoEcAzKxiOYi%2B9lpyx4U5t7v%2BqB85WSb0yAyP6xnXIu7CTk2rqZeuAm2feofISQ7Bc3wSl3BC8igRUFYXf%2BFTMFNnNBDfcVv8Q39%2FbqUARc%2BkwrbzpvAY6pgGFA%2BrrhtWNSOxpOhMVEQ7tExWb9Jcy88j%2BrWi3Pzyh1X%2FnPoJ10k2wpuMZC1juQqsE8edJbXuZHElot45butRHBMFRjswx8Ayv9s9t%2Be8FFbhJchm2KY3pxQEpIR5B1NtylQVbGITERXqkGeCIvNIYYWk1xbpfN3EVMiiAzzCpmBhv%2FAQiteCxq6x%2F4vaijdMOARtCT87%2B0RteUa4z7v8f4oreGzfe&X-Amz-Signature=9945d91703432c83d0ef34b0ab4049233d3a93bf46b62f3152e5bc3bbd128f4d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PKFCJEX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFcRjdmlpalnHGueHt5lbA8ER%2F3baG5x8r%2Fup0PA24lQIgMXz%2B5ze72%2FGbDsrVvCkNMLsWvKscScZExhdVxUIFK%2BEqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD%2FOk2VxsV5oAGGJwyrcA0KPWgprSTQRyYskWwB%2F0Uyom4FNrzyPdBU6eeuh%2FSSHaLEN4mHrYJM511VIn5Q%2B6Hi%2BFs5gvrswJ45YIRdzKRx%2BZ9ihiOoBH3DkANn7QTCjcmHWdlvSjMzVWpoHFhXafzJseEDO8moHe%2BZWzikzYNH7kZ%2BS%2B%2BQxPgFLT0pknUncXL8XAvKpNax%2BKQH5Kao12sF6EyFDw8x7ZUCl2LxznIVX1KW5DiYyn%2BgjpqHA9BGnpL4HlfmnI5NbscomEhDomvgXP4DgpOGpVhtOlZxoRiySjVigfL4fO%2F%2FCLgD30l3Ps6F1fACYC%2FikHjQevxOvgPpnn49%2BC0A3dc6Kvm1vmxBzN31ckQI1dwEPXUBptGIVmdLvAK0QE1tGYFqQu3njXp7O8OjCTiZAUPH74HQvZbKGMiWmJX0SBCNjZo7A3daqnwPjWbUd8554daIkvqCwB%2BnKvWqvESQOKpViXV05p9FwgmQBiXfs2JE8U%2F7r92EWeChwCniTqP8O%2FjC%2FLcN2YP95ZAxUVM7S5e4t9A0wrUKZGJWmWsN8XLjX0DMfYhD8jjV4jYzNGjV1RmRur2JaS4mjE8931Ir63LI9HdMlwB%2BK9LWI984%2BrZ7HVnpbFu09VpH4HltOoRnxXWBVMPq76bwGOqUB0obZ47XwSiuXUVWogrHRk9wBiTVQ%2BMNMMDpFByZ2iVBZ5zp1jqFjSVCSCTI%2BRw0WumWcfC3V%2F5laDaiT9LCs5%2BHe57VAizszuCpEVmtSdM2g0UrYjPuC1NLTIHdBooto%2FXIH%2FtOU28UESHa1qcAhN8B%2FQd8dqEDvrADfg1rG712s6w530aiS85lRZcU1CuX4trD394cFEJ44rJe4iQ0YmlJwXkqV&X-Amz-Signature=c04a218390c0a7caa9b9ab446c25837a0e1d1c53fe0cbad01ddbbc73009ee3bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3HUWTY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsc5vH5dLt25RpQ29XstiKhpGOXlGVenXwr4zy8336wwIgbRj4ff2Sp1M0LqGq6s6zyY7qd9IanS%2BDV%2BCnJImbe%2FsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBE6m4YHTNrMbtrjyrcA8uQKOqqwP195VXGB%2FZ6mTBH6KwRrOFZYnS01UzpTlq2hb2HJxZnDHoog4uD6KWSXvp7yEup7upgqGmBeUEs6JnSJ43TuzJEH7FsLGRXL8vNaT1pjE9FghQ39edmFd69QQWYZiYgX6WJIUDhcqwqn%2B%2F4a7cJVhMyuwSkR5fnufA6HpzhxDV5m1RBcBK%2FX4DuF36NwC9zzXhHrVW9c15TNwW1K3XE0ntPVrTUgnhuj6tK%2FvTSTHbCeDuTNB%2BRyh7%2FwE8sKSuWsJswX%2Fnu039R3Jh5HV%2FhaRLDzLD2YafbUVT%2FamOkO4z3%2FwvbtyZIJ140A5R2MjClV8ytwlUzgG9c9EDomQnaWRzQ1pzxjYrBNq3AjCCF1tK90TwE%2BkuQtVSOBdk2TVIDub99dEyY9f0Ziv7K7o%2Fhlw0n6U4QrY5dO7U%2B9GEL8X21%2F0EAOSd424g5zmV4PBJzLL9FbSn58kspoYDl5PuO80c05YWkNEQvx3%2F2%2F%2FPHe4C1DaSp9T8m%2FiYzDMmGDteXqzBBkjI%2BVnu1dqt4heYkI3D9t9eqaFl%2Fgid2XDEU%2FpzGhRMCUBvBNXyVBLsfyCDRvz7CssjFEGGxqSy3cRPOwSPkkkQl66lWST6YUmaLUQJhleWDONaxMJq86bwGOqUBGLTTWhxai1zphcjLY1F%2FtHIDXAwsmGyBU6ckNcmlQ8t53kAXPZOBFrcRRwXC%2Flol7L6EsUrnWWFFmTjoZuo988L9jjDHsKoLVYZo%2FWtr0gcBcs3cv4zVZe29X6R%2FnXCxCMftWjkIsH4SdraZ%2Bem0WpQ042ruaWKu%2BNDxZnKlH%2FTyau4q065gQSuiqGRs5YjsUNMZ1ME%2FImgyWy%2BnvZ1TvHtxwPdZ&X-Amz-Signature=74944d9d7951e2858a3b541a28b602034938eacd9e691f8eda456daa9489c79e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3HUWTY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsc5vH5dLt25RpQ29XstiKhpGOXlGVenXwr4zy8336wwIgbRj4ff2Sp1M0LqGq6s6zyY7qd9IanS%2BDV%2BCnJImbe%2FsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBE6m4YHTNrMbtrjyrcA8uQKOqqwP195VXGB%2FZ6mTBH6KwRrOFZYnS01UzpTlq2hb2HJxZnDHoog4uD6KWSXvp7yEup7upgqGmBeUEs6JnSJ43TuzJEH7FsLGRXL8vNaT1pjE9FghQ39edmFd69QQWYZiYgX6WJIUDhcqwqn%2B%2F4a7cJVhMyuwSkR5fnufA6HpzhxDV5m1RBcBK%2FX4DuF36NwC9zzXhHrVW9c15TNwW1K3XE0ntPVrTUgnhuj6tK%2FvTSTHbCeDuTNB%2BRyh7%2FwE8sKSuWsJswX%2Fnu039R3Jh5HV%2FhaRLDzLD2YafbUVT%2FamOkO4z3%2FwvbtyZIJ140A5R2MjClV8ytwlUzgG9c9EDomQnaWRzQ1pzxjYrBNq3AjCCF1tK90TwE%2BkuQtVSOBdk2TVIDub99dEyY9f0Ziv7K7o%2Fhlw0n6U4QrY5dO7U%2B9GEL8X21%2F0EAOSd424g5zmV4PBJzLL9FbSn58kspoYDl5PuO80c05YWkNEQvx3%2F2%2F%2FPHe4C1DaSp9T8m%2FiYzDMmGDteXqzBBkjI%2BVnu1dqt4heYkI3D9t9eqaFl%2Fgid2XDEU%2FpzGhRMCUBvBNXyVBLsfyCDRvz7CssjFEGGxqSy3cRPOwSPkkkQl66lWST6YUmaLUQJhleWDONaxMJq86bwGOqUBGLTTWhxai1zphcjLY1F%2FtHIDXAwsmGyBU6ckNcmlQ8t53kAXPZOBFrcRRwXC%2Flol7L6EsUrnWWFFmTjoZuo988L9jjDHsKoLVYZo%2FWtr0gcBcs3cv4zVZe29X6R%2FnXCxCMftWjkIsH4SdraZ%2Bem0WpQ042ruaWKu%2BNDxZnKlH%2FTyau4q065gQSuiqGRs5YjsUNMZ1ME%2FImgyWy%2BnvZ1TvHtxwPdZ&X-Amz-Signature=45ca900b34aafcb942ef4d3e7708a13cbd99f0946d08c1dac9c09fc9bbf0fe50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3HUWTY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsc5vH5dLt25RpQ29XstiKhpGOXlGVenXwr4zy8336wwIgbRj4ff2Sp1M0LqGq6s6zyY7qd9IanS%2BDV%2BCnJImbe%2FsqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBE6m4YHTNrMbtrjyrcA8uQKOqqwP195VXGB%2FZ6mTBH6KwRrOFZYnS01UzpTlq2hb2HJxZnDHoog4uD6KWSXvp7yEup7upgqGmBeUEs6JnSJ43TuzJEH7FsLGRXL8vNaT1pjE9FghQ39edmFd69QQWYZiYgX6WJIUDhcqwqn%2B%2F4a7cJVhMyuwSkR5fnufA6HpzhxDV5m1RBcBK%2FX4DuF36NwC9zzXhHrVW9c15TNwW1K3XE0ntPVrTUgnhuj6tK%2FvTSTHbCeDuTNB%2BRyh7%2FwE8sKSuWsJswX%2Fnu039R3Jh5HV%2FhaRLDzLD2YafbUVT%2FamOkO4z3%2FwvbtyZIJ140A5R2MjClV8ytwlUzgG9c9EDomQnaWRzQ1pzxjYrBNq3AjCCF1tK90TwE%2BkuQtVSOBdk2TVIDub99dEyY9f0Ziv7K7o%2Fhlw0n6U4QrY5dO7U%2B9GEL8X21%2F0EAOSd424g5zmV4PBJzLL9FbSn58kspoYDl5PuO80c05YWkNEQvx3%2F2%2F%2FPHe4C1DaSp9T8m%2FiYzDMmGDteXqzBBkjI%2BVnu1dqt4heYkI3D9t9eqaFl%2Fgid2XDEU%2FpzGhRMCUBvBNXyVBLsfyCDRvz7CssjFEGGxqSy3cRPOwSPkkkQl66lWST6YUmaLUQJhleWDONaxMJq86bwGOqUBGLTTWhxai1zphcjLY1F%2FtHIDXAwsmGyBU6ckNcmlQ8t53kAXPZOBFrcRRwXC%2Flol7L6EsUrnWWFFmTjoZuo988L9jjDHsKoLVYZo%2FWtr0gcBcs3cv4zVZe29X6R%2FnXCxCMftWjkIsH4SdraZ%2Bem0WpQ042ruaWKu%2BNDxZnKlH%2FTyau4q065gQSuiqGRs5YjsUNMZ1ME%2FImgyWy%2BnvZ1TvHtxwPdZ&X-Amz-Signature=345653625b6de19cd281cf56ea904c414a6a5543c0b8b50a9212a7e196980cfe&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPBFTHGO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD23b2yTfRqnBoDEzEhOzS5HMyTjE6tymNqrBVXbhf9GwIhAMzKpTnHo9KU7yLMiL5xQkezNsd6hTojiKjBDd28A7ATKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzm37SBXpGWDE4%2F63kq3AOXIE44%2BKxNDdeQVUTiyx3kNgXr0aW3OrtKkTpuWMMGqf1QigsRwOHIxPEgIjiPdoIASphSXWPcswMbRRx77i5PoKRqW6GBb6S7MWYXmtvUcjL5HoGxLd6oBrbVC5HxqAYi4kUxebWLJiJhxqq0YiPTBF%2BPt%2B6x1nGnQVnnTdw37FpyRsIqCwkYpW7ySSeKt6RTL9mRcSVMqRaPGnfwWQQV1pcg%2FhEC7k%2BUjR4oLl5Pbgcmibx5udhWcYNXoNB%2FKmODqg4K%2FDqQZIPxL%2BNcP91DA6H6XsrcZl1NY4bMbHF%2BRDb6E3KCxtNJaGI036avvs8al6o8OM6YpIddENQom%2BMMtuFEtRmaPLMuZQCIE4rwsTzWy6HWViKav8Wg%2FH16dKE7y2MyfNJWzq6vBCcdaFFgvKlaFagHTT5vqHacWtxmbcVorzGQDuZU700sN37xSDkmjboMi%2Fue%2BwTP%2FiQkMuy0p6fL5UA4HqcMbln2TcjAfM0AeNxkaeyzEBRB0XgoocqQSVpR0zPnhEyrWYVwT26gSbOd0I2DmYaSTpiBPrQ%2BL77FHT9RAldbkK1oVG2sL1QNHUf%2Bq%2BfTwNdfV%2BJKGuXd0aW%2B%2BxfXDjdpnFqS9lxdUjZbVwg4T7dLCDhQcDDXu%2Bm8BjqkAVRHXUU2QeZOC5%2FeK%2FuxWj24%2FloSZFDYLsoVG8QtgAeVlWXX90WzX0fYhEaDLQ3%2BWpgLpwuwQQO0Ojq7Fby88Sqml%2BWmdGnvL3K1aVWhAhNs2H3YgZCiZXFEqOY2IT1WGPv7S3BWuzXkW1lUIq%2BFz4vuSGFg0BqAY6A%2FgZYctZRwIRrZrXe2Z60saYBWoj4wo2hnwKNSAwrkU3vQc19L3th4EQrN&X-Amz-Signature=6b1ff982e52a9a62819a0311cf61ef834e7d35d82dcc8e95728e1ba6d200abc0&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C63QAVH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJ2xLK07tsJSviVZf0beJeNyVHFDOTkauXSxkwOPvw1wIhAILmv2p1qFwnsrvDycNOEmDF6iGCN6BZTWZ9mc2CqHqwKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx85y0hlJ%2B%2F4udRLsYq3AMypx4m43lobJ2TBZOYkQWTMe%2BqWbQ8UOA0ihKMBpvsSoKiZUPJB0%2FJRqI5%2FcQDVqKMXhPsRXUEvo4ejlQnQ9MIYPmASXhAD3aLzCu9wnTt6OO811YgudfciLFgAh4IvM4uk7BaQ1w3mzc3Vi1hja5XnRrD4nBcoexvuMPVlgtG7dx8kFQbYCd1gjc1JAtdKwXpffh1EVPnYkWir0bvJLnL1LWaB7EiwQqvRiYx0PhAI5Bif%2FJ5nqxOpiHUDtyeXvmlBrU7kGlM88xOUee9yhLfAlO%2Bi6mh7CgoDloXpD5R9cv%2BDQFfhwhvZ4fInakEXOfeqFBy8EnRpNMzitxOLaSs6bieJupY%2F4wL%2FAZdWBCcje0qYQOXuGg0621NMzMSg1FcN1OEruyLQfBEMfqyJu2JlRtXqrjYaCjKV8FXgmTblhifY%2FUIQeVhvgA5TcZPAycGo6W26XjIjChCPoqNhreAawY0IDAmVC%2FR82lzCVW32Kog8ix%2BH4Zscyqe%2BOGrcyryBV5MChIhTWznGPMsXyW8ASgK3Abt6s0Z5w7ZPeZlbMSFa79PeZpwdu%2FhqIny4JV9OPLnJ24rKQX7H9AJ%2Fy2QOEIaIJ37FdCLPB8%2FsnaBlXefJG6htd2sre1VxTD%2Fu%2Bm8BjqkARbP5JQ18QbRlp3IVoHamhDsFvlLRdf%2FmvI%2BPo2ENojiRC2SelucZLraucC7%2BwBOq7w4EbpXKnCTOxalpQKLwXEktZ5drH7usJ3%2Bn787mkXN6xRt5f1cipfdF7kpxzWqcyfy%2F4eGVyIh3f6AYn91fjvEN1vJDFrc2PlCw72N%2Bg2xX9bFpQ3N3m8akxd5lfFe1%2BCS%2FHrrxIVqvKWWxx372XmEI70G&X-Amz-Signature=af0ae86dbf50aea4e749fffddaef57c12c58fd260b8b1d3deed16e931c8f6baf&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672MEG7HK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfi5RQtLEXKUIb4uMswuwRy3k0piDI0uv2gMERsncO2QIgYptPL3Z8frhXiwxbgoyA2mNGQoBbTGTFE1UU%2Fg07X5oqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOojGgiNUnGnmdgJdSrcA6xEvC%2BmS0oT0TO7PUew61PvhCBC22nq7zx%2FEHeBjY7me5Dl8DwXQ4ImRp47v1J9SfMZP9aUt1dsUdJwwRky%2FZFuSsO7Q3YXzFK0ufMp40pVDUKwf2KXnl6ElpgHnPEuqzeBtL0mUl6Gng6qY43xolaW2%2FwpsLZv3d6fEwIsonBfgicNwKfxfjeGM0mlFauJGrtl4jBv%2FgEIvbmjp1yEuSQXAEov29hB5%2B7agfzpNN2Olz2zNB8W8vxf0BvccohpSZgVaTjZvUML7QvazWhBPuAxBXFOPmwV4kbJO8qE4QDc00WPFMarKcVCCblndgQWXbq8z9cAlnUABMfXBNbeV1IOMHmLgfWbF4OBRCgm%2FG0zJJP6E%2BuUz21EOu28WmqdPMzQPu5g5hweypmg9rdV8G6tebmT686Ar22HuiYpPWov1yQkQnVtZvZGYCniFMh6qLzZqK%2Bbmus1u6rb8N%2BxsKlN5md8RkEJJo34cz8NCmvq2egrzxfdzMNqtNPuCBdjLcRg1oTRvm9x%2B4cMBHu%2BPfUGjpv%2FGB4f3Rb0SLOPlgWZkt9x9hThKP0VfRYxqV5J26XNRaDEW9rpBeBBaKrxK%2FHq%2FZshCkXEZxPCWZyZj2dKyehHqLrCulFVpg0qMOG76bwGOqUBzHa1V5I%2FqIE0sypwlWau4pm%2BcdqZIda3O%2BU5944MnvwgbExXncyPdbOIBps5qXk%2BLfBvouwmkPcFle0H%2B1GT8vNy2dO9Wa2IEfNVixfHDVZP%2FyKPN5%2Bmhutl9pAWhox6Jqgty26SAOnkUS9RN1%2B%2FsUqCLU1PUtzvuq%2FFxa%2FKZc7dZU54mhOB%2B1tb%2FzvwHTDICYLmdCKkTwkWxqtvNN0tvjw5Z8%2Fv&X-Amz-Signature=b14b43d1716ee1f6035e3985cfb25a77d9c043fe13959c68b5e4d70f1942f7c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5AWF7RU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS%2B4sBZUJE48bvqHJLiUpY17biGnKztzF3joj19kk3xAIhAPIvbeL3sEjpahGZ5iO98SvQpdhRvGsLhgBesM9npZPLKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHAGwKEOwfXQHbNFcq3ANcTQmAMcStllfq01tvM1m1vOPE11AJNCpPWh3oFQSFJ4VCw8I7wNc2BfkiDLu23yQIeOTw8mGoUwQq5Ocb4vX3BRCl%2Fpmx0OefycH77MD7EsjSo9PfWiv6T%2FQmID0S3x6Lbsr2b2R%2Bcrs1PXvOHWtL4QqPLriKPY7xtvNiWs%2BNu2dgWY8xua46EQcadI15n6%2B0pFXQl1Z2oLyFViepapf1NgNQ1EdPsJro81x7TGwAHR%2Beyeq9%2FPKM4k%2F9U7eLTY%2FJ13h2jFvGIgVb6WcADkEJWT8VY%2BIJbXWK1XOqlkaEOmYldVv%2BmCQ7tgIt3GU4noU69OT0MuEHb2i6l%2B1NqaUh%2Bh2Df9VKFFBAroTXSMB0JqOGK7j3XTo%2BwobcB6uSSZSn8Lf3LcGpsDrxFtBOlDOJ7X%2Bdygos%2B5EuGrbpS%2FTjRrPKddPuwoag%2FzonJL6Q0CLmj%2FEifdP59osvlP%2BA5aAFz%2FWKV%2FeX44wXHP%2FooVFLe0ztecsnJSckmQTJ3DBjnyJZhImeDSuZoEINU2jJ9FP12pVpNUBqcjezfTEO5DgZ0UhsjCGYldcf6Mc9Vhqs1%2Be9hh81Tmx8xAqI5POI182%2FqBUGP2amEOcI8bXV8POt9I%2B8dR05ygTuw2C1CTCSvOm8BjqkAf7xuCDusM70Iy%2BChNG%2BgFUw72LDTiXogATDFb4nv09fj35EeaoXjDWqMjXh3Gpp0NhgxlBZ8clsiW8zGQS8jb%2BUyGT%2BjsyWllRMzUkT%2Fjy0H8zFSDoN7PI%2BpY5up5d0IdG4rMn%2BYFCW%2FbXjl3V%2FA7sfgqAz236aw6lX6U6ZAMObCfLSMq3YM1c%2FAoM2%2Bh5lkdxQ2PsZp1mF6MXm0NmnRjp25K0Q&X-Amz-Signature=dedf0716b332f50b70a16dc3ffa3e507fff905cad20f9b2cec5d7dc523412c74&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5AWF7RU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS%2B4sBZUJE48bvqHJLiUpY17biGnKztzF3joj19kk3xAIhAPIvbeL3sEjpahGZ5iO98SvQpdhRvGsLhgBesM9npZPLKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHAGwKEOwfXQHbNFcq3ANcTQmAMcStllfq01tvM1m1vOPE11AJNCpPWh3oFQSFJ4VCw8I7wNc2BfkiDLu23yQIeOTw8mGoUwQq5Ocb4vX3BRCl%2Fpmx0OefycH77MD7EsjSo9PfWiv6T%2FQmID0S3x6Lbsr2b2R%2Bcrs1PXvOHWtL4QqPLriKPY7xtvNiWs%2BNu2dgWY8xua46EQcadI15n6%2B0pFXQl1Z2oLyFViepapf1NgNQ1EdPsJro81x7TGwAHR%2Beyeq9%2FPKM4k%2F9U7eLTY%2FJ13h2jFvGIgVb6WcADkEJWT8VY%2BIJbXWK1XOqlkaEOmYldVv%2BmCQ7tgIt3GU4noU69OT0MuEHb2i6l%2B1NqaUh%2Bh2Df9VKFFBAroTXSMB0JqOGK7j3XTo%2BwobcB6uSSZSn8Lf3LcGpsDrxFtBOlDOJ7X%2Bdygos%2B5EuGrbpS%2FTjRrPKddPuwoag%2FzonJL6Q0CLmj%2FEifdP59osvlP%2BA5aAFz%2FWKV%2FeX44wXHP%2FooVFLe0ztecsnJSckmQTJ3DBjnyJZhImeDSuZoEINU2jJ9FP12pVpNUBqcjezfTEO5DgZ0UhsjCGYldcf6Mc9Vhqs1%2Be9hh81Tmx8xAqI5POI182%2FqBUGP2amEOcI8bXV8POt9I%2B8dR05ygTuw2C1CTCSvOm8BjqkAf7xuCDusM70Iy%2BChNG%2BgFUw72LDTiXogATDFb4nv09fj35EeaoXjDWqMjXh3Gpp0NhgxlBZ8clsiW8zGQS8jb%2BUyGT%2BjsyWllRMzUkT%2Fjy0H8zFSDoN7PI%2BpY5up5d0IdG4rMn%2BYFCW%2FbXjl3V%2FA7sfgqAz236aw6lX6U6ZAMObCfLSMq3YM1c%2FAoM2%2Bh5lkdxQ2PsZp1mF6MXm0NmnRjp25K0Q&X-Amz-Signature=bb5b8193a9f61ad1b7df8d72e7808a56fbed9f0ac9f5fc938e72de3e57d08c42&X-Amz-SignedHeaders=host&x-id=GetObject)

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
