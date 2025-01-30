

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AGN7KQW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAhJ%2BmXm%2Br6SkWsf2oKBYB1zG2eLumkMBerWoAsXiZ63AiAqA%2Bjs6fHZVr9PjHOMAL05LKWpYnSJw8tiD7MPrKEnZSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEhKNOfYNhXXe6l1NKtwD%2BcpG1xKSc2Q%2FkvjTKvt8shVQdwhfGWwme0935qKX%2FGIPU5NYAOEghyJgbZqKYaS4dUFbI1RuKxW8BkvD82ilV3lxsmgsUQ05UYPoBeUYJ94u1QQ9pJDlAvVfQHnG6HvE4DBrYlEd5MDF7xA7rW3s41eNg%2BG%2BRvBtqKk4HCqQbwDFSQOzE1axY%2BM5Tphh73NXH2f8ZGUQfd7s6Cbi7aNtmoWLnBxcOiEz8jiP87dQTYWPZMCj2blfHNqMjugP4xTjzojXvH6yWPILpF%2B%2FgT3Hx8QFiUpEULCNC0ilsfrm3oogMcxEoIxdOecRQShDuFRo79021Tq31xZrQTkbVPiX1pCpvBtE618JxkQDJPps2LWRFcr3nJ1a1cQdj29MB7vaaYqoYluJQe%2F19R0SmZu5LsJcauL8HUCzAkovcfiFemONKItyiNXIImKApZhP6JXfkQ%2FpgPh18B4AW5Y0HBXlxpClXgLgAyu%2FnDNdlAgEm0UJshbviyNVV6iVuqkCeItzcIoEHPO7iguQD2kM4u1UISMOXYoD0UWBxDzxaqLZ6CeujXUbJaxJOhuorKGWdO92lcHehpG34fsoBVKAItFjc%2F63D9YmBF1p%2B50pllCs6AvFCn9rpNUup4qMdj4wjPvtvAY6pgF7aKZSlI7hcgsIjpCsg7rMZ5ER3HGheMuir0nNnKn%2FdNS22mAk6mCMvZMUnySZ2vpxrAbjmnfj4NudwCtX09RIXdzFdgf0C2qB3GGtH95xOKt3dKYn86m0ROC%2FOOfQl2LCXkgNWxjFRjrE%2Fmxyzu20gCv3ZVPPJRaupB%2BigQhLxoSNXMCvNKpC8TThNMmtSnQVNX1qfqp7Snj3YPtk1SdBEYuTEcSp&X-Amz-Signature=fdd150ce2e809ee25aa50dd6e020266e8dd94dbfce660fd227d3833a7eaf4dc1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AGN7KQW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAhJ%2BmXm%2Br6SkWsf2oKBYB1zG2eLumkMBerWoAsXiZ63AiAqA%2Bjs6fHZVr9PjHOMAL05LKWpYnSJw8tiD7MPrKEnZSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEhKNOfYNhXXe6l1NKtwD%2BcpG1xKSc2Q%2FkvjTKvt8shVQdwhfGWwme0935qKX%2FGIPU5NYAOEghyJgbZqKYaS4dUFbI1RuKxW8BkvD82ilV3lxsmgsUQ05UYPoBeUYJ94u1QQ9pJDlAvVfQHnG6HvE4DBrYlEd5MDF7xA7rW3s41eNg%2BG%2BRvBtqKk4HCqQbwDFSQOzE1axY%2BM5Tphh73NXH2f8ZGUQfd7s6Cbi7aNtmoWLnBxcOiEz8jiP87dQTYWPZMCj2blfHNqMjugP4xTjzojXvH6yWPILpF%2B%2FgT3Hx8QFiUpEULCNC0ilsfrm3oogMcxEoIxdOecRQShDuFRo79021Tq31xZrQTkbVPiX1pCpvBtE618JxkQDJPps2LWRFcr3nJ1a1cQdj29MB7vaaYqoYluJQe%2F19R0SmZu5LsJcauL8HUCzAkovcfiFemONKItyiNXIImKApZhP6JXfkQ%2FpgPh18B4AW5Y0HBXlxpClXgLgAyu%2FnDNdlAgEm0UJshbviyNVV6iVuqkCeItzcIoEHPO7iguQD2kM4u1UISMOXYoD0UWBxDzxaqLZ6CeujXUbJaxJOhuorKGWdO92lcHehpG34fsoBVKAItFjc%2F63D9YmBF1p%2B50pllCs6AvFCn9rpNUup4qMdj4wjPvtvAY6pgF7aKZSlI7hcgsIjpCsg7rMZ5ER3HGheMuir0nNnKn%2FdNS22mAk6mCMvZMUnySZ2vpxrAbjmnfj4NudwCtX09RIXdzFdgf0C2qB3GGtH95xOKt3dKYn86m0ROC%2FOOfQl2LCXkgNWxjFRjrE%2Fmxyzu20gCv3ZVPPJRaupB%2BigQhLxoSNXMCvNKpC8TThNMmtSnQVNX1qfqp7Snj3YPtk1SdBEYuTEcSp&X-Amz-Signature=2629f19c3eea63c283a295604a79bd06a3a6a720559a3db00d29523a15de9f23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AGN7KQW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAhJ%2BmXm%2Br6SkWsf2oKBYB1zG2eLumkMBerWoAsXiZ63AiAqA%2Bjs6fHZVr9PjHOMAL05LKWpYnSJw8tiD7MPrKEnZSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEhKNOfYNhXXe6l1NKtwD%2BcpG1xKSc2Q%2FkvjTKvt8shVQdwhfGWwme0935qKX%2FGIPU5NYAOEghyJgbZqKYaS4dUFbI1RuKxW8BkvD82ilV3lxsmgsUQ05UYPoBeUYJ94u1QQ9pJDlAvVfQHnG6HvE4DBrYlEd5MDF7xA7rW3s41eNg%2BG%2BRvBtqKk4HCqQbwDFSQOzE1axY%2BM5Tphh73NXH2f8ZGUQfd7s6Cbi7aNtmoWLnBxcOiEz8jiP87dQTYWPZMCj2blfHNqMjugP4xTjzojXvH6yWPILpF%2B%2FgT3Hx8QFiUpEULCNC0ilsfrm3oogMcxEoIxdOecRQShDuFRo79021Tq31xZrQTkbVPiX1pCpvBtE618JxkQDJPps2LWRFcr3nJ1a1cQdj29MB7vaaYqoYluJQe%2F19R0SmZu5LsJcauL8HUCzAkovcfiFemONKItyiNXIImKApZhP6JXfkQ%2FpgPh18B4AW5Y0HBXlxpClXgLgAyu%2FnDNdlAgEm0UJshbviyNVV6iVuqkCeItzcIoEHPO7iguQD2kM4u1UISMOXYoD0UWBxDzxaqLZ6CeujXUbJaxJOhuorKGWdO92lcHehpG34fsoBVKAItFjc%2F63D9YmBF1p%2B50pllCs6AvFCn9rpNUup4qMdj4wjPvtvAY6pgF7aKZSlI7hcgsIjpCsg7rMZ5ER3HGheMuir0nNnKn%2FdNS22mAk6mCMvZMUnySZ2vpxrAbjmnfj4NudwCtX09RIXdzFdgf0C2qB3GGtH95xOKt3dKYn86m0ROC%2FOOfQl2LCXkgNWxjFRjrE%2Fmxyzu20gCv3ZVPPJRaupB%2BigQhLxoSNXMCvNKpC8TThNMmtSnQVNX1qfqp7Snj3YPtk1SdBEYuTEcSp&X-Amz-Signature=b96e070ea648a48a0eae271fa445a125a4b0820be5140820116ccc611c6b4d4c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMKQEQFL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCir4TmEhJT3JV%2BHPaC39hnS%2BPpRIdx%2F01z02QibOGgpgIhALbBHe%2FvV5hS4e8ZZF6WAUHoAQy9tG8nn6qidRmkBwa2KogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFCoWPsqGxhehmJUq3AOykYCTvaUSZqD0DyWguhU6a0InbsoCBxElnQcW4S3PXYBqFamcrftD%2FJMdAavS7vkCX6hl3GL6JUJTsoQfEVnvdqVFz40U6oH%2BRV5rlRJY1Kjww%2FK%2FmM0Z322c2iB4Re0twTnnfhth0gTRJ3KLKpmUwD7kM68rc8YAXvn%2B0o%2BVXoAACCqG66utFsKKtoZelDinbpcrtFM5z5grnUiGezK55Vs3S97%2FoSeI0964Z1p2kjPUujkhTzkjX7KQc8FpOSfgc02TVJ4lXByRdSP9UsLGojmEfP1TfCQH9w0s4hxpaHIt72TmQJi0Ib3c7bTjqu0geGEP%2BbL4%2FDsU4CR9br84z%2BlTM4c2B9j3I%2B8O4nAP9xM%2Bo8I%2B7JYcTvcEcr%2FThNX0BngkYaSZQ%2BTob01aVVLFHwYo4mkf0ZyP1vkzfZzGz%2BAw%2Fn3L4NVrAlXTsODMi8hoBPjykONom0kbZj%2FqBShyViosu3Xl0QQHNdJv7L2pO80nACRIeafKxHyNWBHTmZqyHbkafNYHPKVGHcffb%2FcUswmfLYExj%2BzZ50YILLbXHE1fE3IBCLyEYq1bCzksDfiVK2b86iI4juelHnn6SKe6ulA0PXsAsgx96d1l%2BUMXqr03m3k55nVlGyAXyTDX%2Bu28BjqkAX8lzYp%2BQRJ60nuq76UOw%2BmlxTlBG95eAStcMVjUMoBbB%2FJaEMFJD8sp7Dkb9JttGorspsbimkrQQXaeFPHtK75ewFxo4FtVTQB0GvUri9WnN0%2Bz6%2FocXuMqd7m3PK2oPBAm3zbySmKxyy6MFer%2BEakygIch2K0y8UrQ6ahvB6AffL8lUzsjuRskViRznzrVbO32WH9q2hVSVEY0a6u3ZTh4Q%2BnA&X-Amz-Signature=55f47855e50809e37ba0560e73ff25477c75ce4d4f6b0406449d15708ba71a4a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMKQEQFL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCir4TmEhJT3JV%2BHPaC39hnS%2BPpRIdx%2F01z02QibOGgpgIhALbBHe%2FvV5hS4e8ZZF6WAUHoAQy9tG8nn6qidRmkBwa2KogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFCoWPsqGxhehmJUq3AOykYCTvaUSZqD0DyWguhU6a0InbsoCBxElnQcW4S3PXYBqFamcrftD%2FJMdAavS7vkCX6hl3GL6JUJTsoQfEVnvdqVFz40U6oH%2BRV5rlRJY1Kjww%2FK%2FmM0Z322c2iB4Re0twTnnfhth0gTRJ3KLKpmUwD7kM68rc8YAXvn%2B0o%2BVXoAACCqG66utFsKKtoZelDinbpcrtFM5z5grnUiGezK55Vs3S97%2FoSeI0964Z1p2kjPUujkhTzkjX7KQc8FpOSfgc02TVJ4lXByRdSP9UsLGojmEfP1TfCQH9w0s4hxpaHIt72TmQJi0Ib3c7bTjqu0geGEP%2BbL4%2FDsU4CR9br84z%2BlTM4c2B9j3I%2B8O4nAP9xM%2Bo8I%2B7JYcTvcEcr%2FThNX0BngkYaSZQ%2BTob01aVVLFHwYo4mkf0ZyP1vkzfZzGz%2BAw%2Fn3L4NVrAlXTsODMi8hoBPjykONom0kbZj%2FqBShyViosu3Xl0QQHNdJv7L2pO80nACRIeafKxHyNWBHTmZqyHbkafNYHPKVGHcffb%2FcUswmfLYExj%2BzZ50YILLbXHE1fE3IBCLyEYq1bCzksDfiVK2b86iI4juelHnn6SKe6ulA0PXsAsgx96d1l%2BUMXqr03m3k55nVlGyAXyTDX%2Bu28BjqkAX8lzYp%2BQRJ60nuq76UOw%2BmlxTlBG95eAStcMVjUMoBbB%2FJaEMFJD8sp7Dkb9JttGorspsbimkrQQXaeFPHtK75ewFxo4FtVTQB0GvUri9WnN0%2Bz6%2FocXuMqd7m3PK2oPBAm3zbySmKxyy6MFer%2BEakygIch2K0y8UrQ6ahvB6AffL8lUzsjuRskViRznzrVbO32WH9q2hVSVEY0a6u3ZTh4Q%2BnA&X-Amz-Signature=548e1f3885ee75c8dfd7cbbb3268c51af1bc9fc3df63e717d66d44ba79ad874a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMKQEQFL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCir4TmEhJT3JV%2BHPaC39hnS%2BPpRIdx%2F01z02QibOGgpgIhALbBHe%2FvV5hS4e8ZZF6WAUHoAQy9tG8nn6qidRmkBwa2KogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFCoWPsqGxhehmJUq3AOykYCTvaUSZqD0DyWguhU6a0InbsoCBxElnQcW4S3PXYBqFamcrftD%2FJMdAavS7vkCX6hl3GL6JUJTsoQfEVnvdqVFz40U6oH%2BRV5rlRJY1Kjww%2FK%2FmM0Z322c2iB4Re0twTnnfhth0gTRJ3KLKpmUwD7kM68rc8YAXvn%2B0o%2BVXoAACCqG66utFsKKtoZelDinbpcrtFM5z5grnUiGezK55Vs3S97%2FoSeI0964Z1p2kjPUujkhTzkjX7KQc8FpOSfgc02TVJ4lXByRdSP9UsLGojmEfP1TfCQH9w0s4hxpaHIt72TmQJi0Ib3c7bTjqu0geGEP%2BbL4%2FDsU4CR9br84z%2BlTM4c2B9j3I%2B8O4nAP9xM%2Bo8I%2B7JYcTvcEcr%2FThNX0BngkYaSZQ%2BTob01aVVLFHwYo4mkf0ZyP1vkzfZzGz%2BAw%2Fn3L4NVrAlXTsODMi8hoBPjykONom0kbZj%2FqBShyViosu3Xl0QQHNdJv7L2pO80nACRIeafKxHyNWBHTmZqyHbkafNYHPKVGHcffb%2FcUswmfLYExj%2BzZ50YILLbXHE1fE3IBCLyEYq1bCzksDfiVK2b86iI4juelHnn6SKe6ulA0PXsAsgx96d1l%2BUMXqr03m3k55nVlGyAXyTDX%2Bu28BjqkAX8lzYp%2BQRJ60nuq76UOw%2BmlxTlBG95eAStcMVjUMoBbB%2FJaEMFJD8sp7Dkb9JttGorspsbimkrQQXaeFPHtK75ewFxo4FtVTQB0GvUri9WnN0%2Bz6%2FocXuMqd7m3PK2oPBAm3zbySmKxyy6MFer%2BEakygIch2K0y8UrQ6ahvB6AffL8lUzsjuRskViRznzrVbO32WH9q2hVSVEY0a6u3ZTh4Q%2BnA&X-Amz-Signature=1cc10f8ed249798f4de185c97cbf835a10da3aa84d6e212e868691b6bfc92e1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMKQEQFL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCir4TmEhJT3JV%2BHPaC39hnS%2BPpRIdx%2F01z02QibOGgpgIhALbBHe%2FvV5hS4e8ZZF6WAUHoAQy9tG8nn6qidRmkBwa2KogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFCoWPsqGxhehmJUq3AOykYCTvaUSZqD0DyWguhU6a0InbsoCBxElnQcW4S3PXYBqFamcrftD%2FJMdAavS7vkCX6hl3GL6JUJTsoQfEVnvdqVFz40U6oH%2BRV5rlRJY1Kjww%2FK%2FmM0Z322c2iB4Re0twTnnfhth0gTRJ3KLKpmUwD7kM68rc8YAXvn%2B0o%2BVXoAACCqG66utFsKKtoZelDinbpcrtFM5z5grnUiGezK55Vs3S97%2FoSeI0964Z1p2kjPUujkhTzkjX7KQc8FpOSfgc02TVJ4lXByRdSP9UsLGojmEfP1TfCQH9w0s4hxpaHIt72TmQJi0Ib3c7bTjqu0geGEP%2BbL4%2FDsU4CR9br84z%2BlTM4c2B9j3I%2B8O4nAP9xM%2Bo8I%2B7JYcTvcEcr%2FThNX0BngkYaSZQ%2BTob01aVVLFHwYo4mkf0ZyP1vkzfZzGz%2BAw%2Fn3L4NVrAlXTsODMi8hoBPjykONom0kbZj%2FqBShyViosu3Xl0QQHNdJv7L2pO80nACRIeafKxHyNWBHTmZqyHbkafNYHPKVGHcffb%2FcUswmfLYExj%2BzZ50YILLbXHE1fE3IBCLyEYq1bCzksDfiVK2b86iI4juelHnn6SKe6ulA0PXsAsgx96d1l%2BUMXqr03m3k55nVlGyAXyTDX%2Bu28BjqkAX8lzYp%2BQRJ60nuq76UOw%2BmlxTlBG95eAStcMVjUMoBbB%2FJaEMFJD8sp7Dkb9JttGorspsbimkrQQXaeFPHtK75ewFxo4FtVTQB0GvUri9WnN0%2Bz6%2FocXuMqd7m3PK2oPBAm3zbySmKxyy6MFer%2BEakygIch2K0y8UrQ6ahvB6AffL8lUzsjuRskViRznzrVbO32WH9q2hVSVEY0a6u3ZTh4Q%2BnA&X-Amz-Signature=c978d1860c7c3eb65ebe1a5fa101dabc28d775ed7db3c05dc9d62ade4ece991d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMKQEQFL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCir4TmEhJT3JV%2BHPaC39hnS%2BPpRIdx%2F01z02QibOGgpgIhALbBHe%2FvV5hS4e8ZZF6WAUHoAQy9tG8nn6qidRmkBwa2KogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFCoWPsqGxhehmJUq3AOykYCTvaUSZqD0DyWguhU6a0InbsoCBxElnQcW4S3PXYBqFamcrftD%2FJMdAavS7vkCX6hl3GL6JUJTsoQfEVnvdqVFz40U6oH%2BRV5rlRJY1Kjww%2FK%2FmM0Z322c2iB4Re0twTnnfhth0gTRJ3KLKpmUwD7kM68rc8YAXvn%2B0o%2BVXoAACCqG66utFsKKtoZelDinbpcrtFM5z5grnUiGezK55Vs3S97%2FoSeI0964Z1p2kjPUujkhTzkjX7KQc8FpOSfgc02TVJ4lXByRdSP9UsLGojmEfP1TfCQH9w0s4hxpaHIt72TmQJi0Ib3c7bTjqu0geGEP%2BbL4%2FDsU4CR9br84z%2BlTM4c2B9j3I%2B8O4nAP9xM%2Bo8I%2B7JYcTvcEcr%2FThNX0BngkYaSZQ%2BTob01aVVLFHwYo4mkf0ZyP1vkzfZzGz%2BAw%2Fn3L4NVrAlXTsODMi8hoBPjykONom0kbZj%2FqBShyViosu3Xl0QQHNdJv7L2pO80nACRIeafKxHyNWBHTmZqyHbkafNYHPKVGHcffb%2FcUswmfLYExj%2BzZ50YILLbXHE1fE3IBCLyEYq1bCzksDfiVK2b86iI4juelHnn6SKe6ulA0PXsAsgx96d1l%2BUMXqr03m3k55nVlGyAXyTDX%2Bu28BjqkAX8lzYp%2BQRJ60nuq76UOw%2BmlxTlBG95eAStcMVjUMoBbB%2FJaEMFJD8sp7Dkb9JttGorspsbimkrQQXaeFPHtK75ewFxo4FtVTQB0GvUri9WnN0%2Bz6%2FocXuMqd7m3PK2oPBAm3zbySmKxyy6MFer%2BEakygIch2K0y8UrQ6ahvB6AffL8lUzsjuRskViRznzrVbO32WH9q2hVSVEY0a6u3ZTh4Q%2BnA&X-Amz-Signature=93f43e7492a2157a0c854d15b14b39e7f003e0b24e9531a1be8a33eb00255b4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMKQEQFL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCir4TmEhJT3JV%2BHPaC39hnS%2BPpRIdx%2F01z02QibOGgpgIhALbBHe%2FvV5hS4e8ZZF6WAUHoAQy9tG8nn6qidRmkBwa2KogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFCoWPsqGxhehmJUq3AOykYCTvaUSZqD0DyWguhU6a0InbsoCBxElnQcW4S3PXYBqFamcrftD%2FJMdAavS7vkCX6hl3GL6JUJTsoQfEVnvdqVFz40U6oH%2BRV5rlRJY1Kjww%2FK%2FmM0Z322c2iB4Re0twTnnfhth0gTRJ3KLKpmUwD7kM68rc8YAXvn%2B0o%2BVXoAACCqG66utFsKKtoZelDinbpcrtFM5z5grnUiGezK55Vs3S97%2FoSeI0964Z1p2kjPUujkhTzkjX7KQc8FpOSfgc02TVJ4lXByRdSP9UsLGojmEfP1TfCQH9w0s4hxpaHIt72TmQJi0Ib3c7bTjqu0geGEP%2BbL4%2FDsU4CR9br84z%2BlTM4c2B9j3I%2B8O4nAP9xM%2Bo8I%2B7JYcTvcEcr%2FThNX0BngkYaSZQ%2BTob01aVVLFHwYo4mkf0ZyP1vkzfZzGz%2BAw%2Fn3L4NVrAlXTsODMi8hoBPjykONom0kbZj%2FqBShyViosu3Xl0QQHNdJv7L2pO80nACRIeafKxHyNWBHTmZqyHbkafNYHPKVGHcffb%2FcUswmfLYExj%2BzZ50YILLbXHE1fE3IBCLyEYq1bCzksDfiVK2b86iI4juelHnn6SKe6ulA0PXsAsgx96d1l%2BUMXqr03m3k55nVlGyAXyTDX%2Bu28BjqkAX8lzYp%2BQRJ60nuq76UOw%2BmlxTlBG95eAStcMVjUMoBbB%2FJaEMFJD8sp7Dkb9JttGorspsbimkrQQXaeFPHtK75ewFxo4FtVTQB0GvUri9WnN0%2Bz6%2FocXuMqd7m3PK2oPBAm3zbySmKxyy6MFer%2BEakygIch2K0y8UrQ6ahvB6AffL8lUzsjuRskViRznzrVbO32WH9q2hVSVEY0a6u3ZTh4Q%2BnA&X-Amz-Signature=832749216158eeb715a1b5b78755681c42afd72a3b7070236f051ef19ad07d0b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CR7DOI5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDK5YxMF1BMwtJQQzmNYnP4XkwXWglsXPWDT3Mr7vyGlQIhAIWvy2QbYMiu39QIabwGHwKb3bXLvws9E6YoEnSmJuaOKogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHMzH%2B3DRarvPeGYkq3ANk7ImOIzwWDihI1ALyANKkNufFPIcXlwj6hOQe9r0euRunB4gDubGEui8PgJj2%2BDeTZfEpl6Kn6HUhRh9hGGiuz7nBgigeNWCsZzp%2BTls7R21X%2Bh0NgBoGYNKKRBizt1aBFhaeXflYAdHMUzvAZAJH2YcMw1IVBYFxHc8MEPbN3QAsQ1gdIbT%2BUQ4UXETrvFXlHakpeQlETkkwUWdS8qkn9VZxdrKsYKMCPflJGOAprOccI8svLH5bPHiWgoLrrWixVdM4zhfDlodiWfD9fDQiz4BksfWtPC%2Bfcq49VtkxWpTxpVReXxr0E2VmN36jXKA8%2FdlmhF%2FFxA8Db12v9Ihm0%2BmyXN3Y9vLj9rLdEsAVlQbHIaZzStWCLs9UEHyScUAM5i5q5bro%2BJCcRp7VgepTBKyGTqqJezcMT2Ge3LODnwrNXgWSsWQMRYiSITlUznuVwc2ykY%2FYiOcMt6uYKzQcy42QBRQS7lNUmCb7V886xeoES49yJaLrq4f22QWN3YkVxvOc6IVewsRHjfXaK0uqn7T2BwX2boKO056FuKDR9kNlDq%2FYLfjQA1X5KfkjPJFmyqaJenfbf%2Btj0me8W0DdIjJJrH97y0NCcobA%2F3HNKzJWUz%2FoHITMNCsOpTDD%2Bu28BjqkAY%2BqdvgVE6YZefysu9uG99lPfMLfG%2BwzHDq7xZL9Ke83gZJS871EgEWrX3IQ5f5zOBEvZplGNPMILP%2BbcauSPsIv261LxDVWH0pjJxsD2i427w5CqWZIwbAL073oAaGloCxLO33q%2FPzDVXnnG%2FhnW6CDtKYWDP8t3TAROak7Djqz00xrSYh5BpByhajJjWiaQ8JI9rUHAHVttF%2BiLNWYTcJ5pXSf&X-Amz-Signature=f7d475d79d08b3a1e70dd6aedb3e1746da2847d5f88d7d1fd87e4e524697e889&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAJ5QT2P%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEA9EPECi7XqZ5ow61cCDw5MSTfcfYFX%2BBzHTR7H0JcYAiEAokjPbqRomlcAeTqqcX1QNsaFPUTN3wGHo9UBwKtpXz8qiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAGHjztbNRYNqDhfLyrcA9WPtdknFh0BZoBm%2B1HqFF0X%2BBhJyfPdWQx4lPsVefc6Tptg%2FNTCAr7piGCL9Byo9PEmB4uSukGuaYvyx%2FqRLvR1jppJQez%2BQUNcUCJLny%2BUSfLrLokHrUCOEcCOwHF%2F0f%2BzaoEjW8h%2F7zOQFtnVtoO39rN2Li2GBVJ6ScN1YSFlHMQmqKpD61fIsJLLJ4BkSi9h3tS5ZIiYI2hcDeJ5Hh2%2FdlUZPY%2BFQ6eGlyQIrfjFVpe08vqoKXTyMwPZ2RGhfQOGgUqe%2B5SWlVPVInEYq%2BlqVMlf3XTsALTclB0kW2n2siLr4oa1yLz1DPsZ3HHZbW7ioVtiXOUPKIHzdnSt%2B5W6ptkyf6Dwq6ec3d%2BECpqO8WJY53SbwgOSvhrrxWbfzPxLOyJSFCfr%2BHTjs1E15Ci2HrhNzLJlk24vareBZ%2FrKLBPyc9knf52WQx5uyhk9K9e6x7HViiuDKPBfyO732VNc0opNkYNlQDcWTTdXm%2BmrtmR1nT1lMhplDEtklwX6mP15WPcHH%2Fm4Bjius1ah%2Fao5PL0fX%2B4J3mNaAKFRsaNRbe6I37Cc%2FiuH9iMakAeL3lfTYvezQ%2BbFAMUcBnBxSSeEVX3qYWx5LY3dwHSqFLODmnDIyi4odUOA20GZMIL77bwGOqUBKHPa5EBO8xiVM3%2FKh7GUSHTvR5aQe4mZPXGDO5pmrC%2FioI7F9rgOcbpy6Pe2OnghcknzT3IgGwlkplbGod%2F5jZcV%2FXxCtq7%2FUEP%2FFynwc9ijh5DsX1mgsZi%2FO2p2Cr7SYwp%2FC9Od8iRjW%2BzQxSa5r91ICScXRI%2BpME8vTcZrcYg30EiVyi80YV8ehhMU5KKuoiwcCvXLI9JcCZ95RRrZwJH%2FVXV5&X-Amz-Signature=9351d40875f187960ac22f01bffcbc098e530692959ff7db815042570c2cc31c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMKQEQFL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCir4TmEhJT3JV%2BHPaC39hnS%2BPpRIdx%2F01z02QibOGgpgIhALbBHe%2FvV5hS4e8ZZF6WAUHoAQy9tG8nn6qidRmkBwa2KogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFCoWPsqGxhehmJUq3AOykYCTvaUSZqD0DyWguhU6a0InbsoCBxElnQcW4S3PXYBqFamcrftD%2FJMdAavS7vkCX6hl3GL6JUJTsoQfEVnvdqVFz40U6oH%2BRV5rlRJY1Kjww%2FK%2FmM0Z322c2iB4Re0twTnnfhth0gTRJ3KLKpmUwD7kM68rc8YAXvn%2B0o%2BVXoAACCqG66utFsKKtoZelDinbpcrtFM5z5grnUiGezK55Vs3S97%2FoSeI0964Z1p2kjPUujkhTzkjX7KQc8FpOSfgc02TVJ4lXByRdSP9UsLGojmEfP1TfCQH9w0s4hxpaHIt72TmQJi0Ib3c7bTjqu0geGEP%2BbL4%2FDsU4CR9br84z%2BlTM4c2B9j3I%2B8O4nAP9xM%2Bo8I%2B7JYcTvcEcr%2FThNX0BngkYaSZQ%2BTob01aVVLFHwYo4mkf0ZyP1vkzfZzGz%2BAw%2Fn3L4NVrAlXTsODMi8hoBPjykONom0kbZj%2FqBShyViosu3Xl0QQHNdJv7L2pO80nACRIeafKxHyNWBHTmZqyHbkafNYHPKVGHcffb%2FcUswmfLYExj%2BzZ50YILLbXHE1fE3IBCLyEYq1bCzksDfiVK2b86iI4juelHnn6SKe6ulA0PXsAsgx96d1l%2BUMXqr03m3k55nVlGyAXyTDX%2Bu28BjqkAX8lzYp%2BQRJ60nuq76UOw%2BmlxTlBG95eAStcMVjUMoBbB%2FJaEMFJD8sp7Dkb9JttGorspsbimkrQQXaeFPHtK75ewFxo4FtVTQB0GvUri9WnN0%2Bz6%2FocXuMqd7m3PK2oPBAm3zbySmKxyy6MFer%2BEakygIch2K0y8UrQ6ahvB6AffL8lUzsjuRskViRznzrVbO32WH9q2hVSVEY0a6u3ZTh4Q%2BnA&X-Amz-Signature=d62762d06bb0bc645bf5266ae37a4848b9abf7f45d16a66d1493b5d99cd20d31&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMKQEQFL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCir4TmEhJT3JV%2BHPaC39hnS%2BPpRIdx%2F01z02QibOGgpgIhALbBHe%2FvV5hS4e8ZZF6WAUHoAQy9tG8nn6qidRmkBwa2KogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFCoWPsqGxhehmJUq3AOykYCTvaUSZqD0DyWguhU6a0InbsoCBxElnQcW4S3PXYBqFamcrftD%2FJMdAavS7vkCX6hl3GL6JUJTsoQfEVnvdqVFz40U6oH%2BRV5rlRJY1Kjww%2FK%2FmM0Z322c2iB4Re0twTnnfhth0gTRJ3KLKpmUwD7kM68rc8YAXvn%2B0o%2BVXoAACCqG66utFsKKtoZelDinbpcrtFM5z5grnUiGezK55Vs3S97%2FoSeI0964Z1p2kjPUujkhTzkjX7KQc8FpOSfgc02TVJ4lXByRdSP9UsLGojmEfP1TfCQH9w0s4hxpaHIt72TmQJi0Ib3c7bTjqu0geGEP%2BbL4%2FDsU4CR9br84z%2BlTM4c2B9j3I%2B8O4nAP9xM%2Bo8I%2B7JYcTvcEcr%2FThNX0BngkYaSZQ%2BTob01aVVLFHwYo4mkf0ZyP1vkzfZzGz%2BAw%2Fn3L4NVrAlXTsODMi8hoBPjykONom0kbZj%2FqBShyViosu3Xl0QQHNdJv7L2pO80nACRIeafKxHyNWBHTmZqyHbkafNYHPKVGHcffb%2FcUswmfLYExj%2BzZ50YILLbXHE1fE3IBCLyEYq1bCzksDfiVK2b86iI4juelHnn6SKe6ulA0PXsAsgx96d1l%2BUMXqr03m3k55nVlGyAXyTDX%2Bu28BjqkAX8lzYp%2BQRJ60nuq76UOw%2BmlxTlBG95eAStcMVjUMoBbB%2FJaEMFJD8sp7Dkb9JttGorspsbimkrQQXaeFPHtK75ewFxo4FtVTQB0GvUri9WnN0%2Bz6%2FocXuMqd7m3PK2oPBAm3zbySmKxyy6MFer%2BEakygIch2K0y8UrQ6ahvB6AffL8lUzsjuRskViRznzrVbO32WH9q2hVSVEY0a6u3ZTh4Q%2BnA&X-Amz-Signature=25d94e3534109a5755a12d170a40b944810ba055289dcff4c721eacc85303cda&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMKQEQFL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCir4TmEhJT3JV%2BHPaC39hnS%2BPpRIdx%2F01z02QibOGgpgIhALbBHe%2FvV5hS4e8ZZF6WAUHoAQy9tG8nn6qidRmkBwa2KogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwFCoWPsqGxhehmJUq3AOykYCTvaUSZqD0DyWguhU6a0InbsoCBxElnQcW4S3PXYBqFamcrftD%2FJMdAavS7vkCX6hl3GL6JUJTsoQfEVnvdqVFz40U6oH%2BRV5rlRJY1Kjww%2FK%2FmM0Z322c2iB4Re0twTnnfhth0gTRJ3KLKpmUwD7kM68rc8YAXvn%2B0o%2BVXoAACCqG66utFsKKtoZelDinbpcrtFM5z5grnUiGezK55Vs3S97%2FoSeI0964Z1p2kjPUujkhTzkjX7KQc8FpOSfgc02TVJ4lXByRdSP9UsLGojmEfP1TfCQH9w0s4hxpaHIt72TmQJi0Ib3c7bTjqu0geGEP%2BbL4%2FDsU4CR9br84z%2BlTM4c2B9j3I%2B8O4nAP9xM%2Bo8I%2B7JYcTvcEcr%2FThNX0BngkYaSZQ%2BTob01aVVLFHwYo4mkf0ZyP1vkzfZzGz%2BAw%2Fn3L4NVrAlXTsODMi8hoBPjykONom0kbZj%2FqBShyViosu3Xl0QQHNdJv7L2pO80nACRIeafKxHyNWBHTmZqyHbkafNYHPKVGHcffb%2FcUswmfLYExj%2BzZ50YILLbXHE1fE3IBCLyEYq1bCzksDfiVK2b86iI4juelHnn6SKe6ulA0PXsAsgx96d1l%2BUMXqr03m3k55nVlGyAXyTDX%2Bu28BjqkAX8lzYp%2BQRJ60nuq76UOw%2BmlxTlBG95eAStcMVjUMoBbB%2FJaEMFJD8sp7Dkb9JttGorspsbimkrQQXaeFPHtK75ewFxo4FtVTQB0GvUri9WnN0%2Bz6%2FocXuMqd7m3PK2oPBAm3zbySmKxyy6MFer%2BEakygIch2K0y8UrQ6ahvB6AffL8lUzsjuRskViRznzrVbO32WH9q2hVSVEY0a6u3ZTh4Q%2BnA&X-Amz-Signature=3b3ba1f8e57d7a94be06c5d8a3abc44afa9c46431ef94d435086ca111cfce828&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOOHV7NE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYKgb7KKcj9gIoHpGh46bS5rPeoQOx97oqkEShlkLUlQIhAI%2FHzA%2Fc6c5%2FTduG6BeSJTA9nxj5o%2FK6B0rHp%2F2pHpI%2FKogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjDTYi5HzOIiexaSYq3APO2m8BM0QXqWqAXFlvxfzJldPwgOyIGeQB4dBT%2Bge%2BWwlqH86o9lx6Zl9tZMs%2FJUwzKF3SKlFAHFEg2BwrGHWVRhxNAbxNaYdgoatoLvTVpCXbsIaDDulQLeD2%2FIfBJsig2yM%2BpJM63vPuKPUjclHiwAUYQBjWsWWMtgRu%2FIf%2Fcp8ru%2Btgfgo7oGMD81Eugqv8W20UJZtYJ7z8Ch%2BN%2FlK6%2ByiiNN%2FG0F2Qp8ahcA8pm0hYwDVePmRV9eq5p8Bpp6YjWHeDc0Kflhu9F31BJmOHcUHPytgNiI1wFsoyL8MFEEIztZXXbfPzfnMH5PP5j496Dl1rYrlTsuRAWfTtF%2F2jxuIC3%2BzPC9vL9IGPQK4hNdfv8%2BZVJAPUp4%2B3wnef6eNGetvYQ603e3uhA41t5TPoUmT3LXNr1kecIBn%2B%2BBBukhB4y9dfrPKJWCHjjm4MyaL8DHvvfNhvFf7HQcSmYXjWm063MmGvj97iRVhn5%2B36jtAXQXQRRG17IFfvP1o23ihVCaSD0f0jmD7okMaB9Qgx2RctRiau6YPjb2HkNTyheh7dkx5b8mXFDWYQh0Hlul4S%2BhF%2FpzN4ES%2FHQPj%2BEQo36ixCkSJKcwMM5Wr%2FsUusUTyH82%2B0WeszmBKECTCA%2B%2B28BjqkAYkvko4Pbn1SJx6YFE%2FaB5hwFuZz%2FhL7GTYeSME3dq%2F0V%2FDzuT0IPZY7qxs9ct0QjdgtQ4JlNhmMGuezKtlglVc3Dtp%2FB4gZPVh4jpQlT0Y0eFtX93W9aoM6MERs6W7HKYqWUBe%2BzW6Ta%2FJ1o6Jp2z%2FUH3odYGzd2p6laijcslq%2B9n1Qo0SMEKD%2BbfZEoDev04EEabZUlQorNzK5twGpWmwhtan%2B&X-Amz-Signature=8a637b107f84848a7fef401d68a86a4eab15774afa002ea0b4fc8c7b3f65e0c7&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AQ25PH6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLaI%2FoRUvT%2B5Vk64eOJzrqYknpEjzWoHiUOLL1JjBhQQIhAJ0Dn3voOMKM9HqWOlaOAl%2B4%2BETPPL8fJ0GqhSHJXmeVKogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyd%2BfBAvtE1O7AUrDAq3AN%2F%2B5cs5FXjNM8aUHzgAY3x2VP5upFvIG5LTKFfOj7IYA4q1PMproEHGRSZlbxKW7PJ1te05GdCdt8ozlp%2F9aP89HzFV9QX%2B6mdkgCadlimoAOLItmjrWetNzXzWZ6CQTx%2B39sx5PyG7AqvaKgDQSCE5Pv7AfMRGHmqA1TYststdfQQ0JM7TzwhWJ7POd3FUyEZK8GSrL%2B%2FTFIOnwWSRXsksv0vv5xB3NchBbKuzHGoKM2YtfPSgglCRZX0%2F2xW5m7MUTHSxlyY7V2tCpL9cDDubaovd3aZk3descNLbEGlD%2FF1CNPDHTJIGNusSbCNIVNUj8ZcXjEWj4bIRIQRObXqWbwiLGwLw%2BghqCTMzLjZqOjxd7KK6yCHdSZAEE1Z8cF3qr0lS1%2BPdHeurPuLkkyvWBxEV47jwaTJi16vi22HbKHuzBDgXt4wY1ICRbipZ5dsM3%2FgsbysRQ%2FBqg%2BwNel121FCQIg7m6F3fBGv5tf8fwkmu5MWSEeP40GahHhYJA6FPHCzvcakSfZMKUdh%2F28%2BVkX8GR%2BwyDe33f0JzP30o9pki5vMH5TYC0k3TVAlWGQiC81uFIIoFR1KhoI5MluYmSa%2FzBP9cEFv%2BRLhFZWEL9xg7AhPJIva61Do9zCJ%2B%2B28BjqkAY5SHhv8prkyO1ff1hHd8uEkFOzHj9Npy%2B%2BPz9JnoP%2F4tFh%2BMWVzqWrV0NtlCCLYityC8P%2BK%2FQKY6dugEZbkcLA6%2FmQH0LbeJPCWY9pjn36%2BHRwVQg5UKnZi%2BGHapPa5XQBa9WZVnO2Fq0iUnx%2Bru7E6QK6Ye8DCbS6KQS5l0u0nRAp1pO9C4EbyC6ymJAPTnWhG2JvyqaSVYtVdSwnhAnDLEQLr&X-Amz-Signature=afe92d3120a6b6633cb9e455596a906efb1d4bedcce692a875e0a6b6aa6c71a7&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEWYFEJU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzmOHX17dJCpxxNfMr2rmMBi5x%2Bh%2BpqBx6Tk7MTF4rggIgDEFUxOMPvQz5KxbXkjfAK6trhKM1vkcNOrKc6vAuZg8qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC5OiBYU3FsQxq1bNCrcA6hhCxIHonLyI8AozrbywebQRjnkZt1IlV7jRXD0irEQm125ZjRAC6ux8NhP7FkodxrPsLWLYPrcs%2BAIx17Se6S7KwBQBF8sFnmdt4tiC4bh3OLV9lcNsCa89W3RftyPWnrYkpi2p1zyP453PqJt3aBNA27a1HOjaDs9IG4e3T%2Bse0JNCRortjWAFsKOfgDOuQAhspujnaE7XxSa6L%2FtYUQNU1NlEo%2FBd%2BwLLT0mmUv0nFzYPOsqXfFmEgT3V0iMG96GeSa%2FROvWDUJ3x2eB0YMIRTrIAxEBM%2F0kBUPyvLa1q6t%2FwK7LH%2BlGp3detTSCD6d%2FjTqECzb8AyYNOAk4dRcrM6TJ%2B%2Bcvz13EjKILVvbInmi1r6mP2%2FsMF9%2BI2bIOJ%2B6NoRAX6l9GzG1lKE8bKB%2FDeaI7yPYpnImNT8o8wwzWBu8BJ261BtMJguczCmD389SaAroMmG4X9rZskqiJ0k8kWNWEObLyrV58lyV%2Bgmm727YuJIImyo4b8bCW1s%2BZZaLbjyhMD%2B%2FZkNAfpIHR26p34gCqGXleUNh4nBHN9fZzvNHU5iuERET1cob1Vu5b5L9ocVVco4n3RxAn129tM39srrRsLkze1eRaNyiRwjChvG4y5DWB56Sha1NhMJj77bwGOqUBvMF2bbfl%2Bbvit29cj0XPA37SUwdRx6fXtwmZCn3RNdxUnQ16hV8g5aYjIZoUV%2BkwiMbB1yPaawIds7iRAQbB3UbDnexAHTsMHbZRSLPS%2FvemqIWU2yJyAFkHwVzDs7eYMwKqJ0NqYRlT%2BMRkXe6jBtzYkcFdTZlBOo5FDqg%2BdvHN%2FWoMpfGtp9S7Plv4Y5m%2BPlI%2FiqU7Hq4%2FM4xG7l%2BmWIGXHG5y&X-Amz-Signature=2d0debe6dbe66c737ccfd1827859e6666849f8b859ad26809cefb943c0e45bf7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665552TREB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTBzWydJw0ae9szOBnT93fEvQubjtgKrd5QZx0f06XuwIgbD61fAtbf2jl2RuLy2NFEOBNEyPoiVK8tlt%2FNoKL0y8qiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN0DWN2tbpQ3DeK%2BgCrcAwsm2beqLVUiAHeLaXG7D%2BbMKcLTlUk7ncf0GayhWtir8O7HYVEE%2Fm7UL4CET2gICOqBitXaeeIqLw9wHU2VC%2FdHpGhuVD6%2FnakeClN9ZT8u3a5lpHdd%2Bg4hbjDOyeje%2BatIE50gv9X8g%2F3ayDcIo23mYk12ILKY4OieJXHnWO4D248uh2f5UlcJUEjppBRY0J2eo8BtxaRyXmHmLYjtxePQsfzUpZoaSEwAPceGs7G9vwvobWrOSwoa8VkHlGgfyKlBDAp%2FSwz%2FvWDYGjqsYovzbSZDJECTsCc%2FjyfqXcKnNLRcNuZkDSelMBFbDq%2BOiIlfFDq2bb4KXT1f3GDh4WhYnyeVQBe4Ba5r5w8wU9L6l7VdbCxOFyGGQORVAuDCwnIlqk5m9P2rW%2B8jnW%2BKbHDFX5pcDDLIGNuILkZhCC8kdv%2Fx1FE%2F5nnA6EYyH%2FhHKZh%2FWaHLj%2FPcbp5DCGAymZyGxyD2MG%2BBfpaxFbvsTmGqb5SiXP7c3%2F7xXDZNE8pKmzY9FiIKyZCrG3OsSe76%2FKYCRbq5SlqJMTKVhAFjy6aH6d3L0GsSA5pB9zIcuNGEv0AgeYJFiGqcKhCRWnQvx7AVCvJtoydtPxEYro5J%2FNMbwH95aojyw1CankyyMNX67bwGOqUBfyWSlGxuy6N6aYR0Z2jIvJEL%2FMECB3R3suCa8sC1fILz6lGp%2BsYCCS%2FjUVYEHz0qulU2YddJ6rxN0c7TGpY74hcwQGSZwblY%2BwOd%2BPDJba0q5LFQbcgvj7kzNyiGdAxCkA9wqY8HUfkklZzF7YkjW53wdx21C7wKLbBgxE8GWCobXqJ4s3XeDzuONnXmAw8zc9kY%2FqjeHFPMv%2FlRQXBVkTDJHVjO&X-Amz-Signature=d7182d50269f3b21703c8f67b3c588d0336b7981a18778394699ea132fe14734&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665552TREB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTBzWydJw0ae9szOBnT93fEvQubjtgKrd5QZx0f06XuwIgbD61fAtbf2jl2RuLy2NFEOBNEyPoiVK8tlt%2FNoKL0y8qiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN0DWN2tbpQ3DeK%2BgCrcAwsm2beqLVUiAHeLaXG7D%2BbMKcLTlUk7ncf0GayhWtir8O7HYVEE%2Fm7UL4CET2gICOqBitXaeeIqLw9wHU2VC%2FdHpGhuVD6%2FnakeClN9ZT8u3a5lpHdd%2Bg4hbjDOyeje%2BatIE50gv9X8g%2F3ayDcIo23mYk12ILKY4OieJXHnWO4D248uh2f5UlcJUEjppBRY0J2eo8BtxaRyXmHmLYjtxePQsfzUpZoaSEwAPceGs7G9vwvobWrOSwoa8VkHlGgfyKlBDAp%2FSwz%2FvWDYGjqsYovzbSZDJECTsCc%2FjyfqXcKnNLRcNuZkDSelMBFbDq%2BOiIlfFDq2bb4KXT1f3GDh4WhYnyeVQBe4Ba5r5w8wU9L6l7VdbCxOFyGGQORVAuDCwnIlqk5m9P2rW%2B8jnW%2BKbHDFX5pcDDLIGNuILkZhCC8kdv%2Fx1FE%2F5nnA6EYyH%2FhHKZh%2FWaHLj%2FPcbp5DCGAymZyGxyD2MG%2BBfpaxFbvsTmGqb5SiXP7c3%2F7xXDZNE8pKmzY9FiIKyZCrG3OsSe76%2FKYCRbq5SlqJMTKVhAFjy6aH6d3L0GsSA5pB9zIcuNGEv0AgeYJFiGqcKhCRWnQvx7AVCvJtoydtPxEYro5J%2FNMbwH95aojyw1CankyyMNX67bwGOqUBfyWSlGxuy6N6aYR0Z2jIvJEL%2FMECB3R3suCa8sC1fILz6lGp%2BsYCCS%2FjUVYEHz0qulU2YddJ6rxN0c7TGpY74hcwQGSZwblY%2BwOd%2BPDJba0q5LFQbcgvj7kzNyiGdAxCkA9wqY8HUfkklZzF7YkjW53wdx21C7wKLbBgxE8GWCobXqJ4s3XeDzuONnXmAw8zc9kY%2FqjeHFPMv%2FlRQXBVkTDJHVjO&X-Amz-Signature=aa1b5d6728f5e8afe501f4195ffd138813740e2f7b1ab261a57742095856d291&X-Amz-SignedHeaders=host&x-id=GetObject)

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
