

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662DO2KDK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiEmL%2BzTkjF1zcXhASmucf7JdHXzNnbUB2UfBmCRXNNAIhAI%2F3aboPD53HHhfxyzAzCV9McmEojw%2FCRtb1qtepZCWVKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyQZMV0yGJkLKSqlLcq3AO8OU%2FzgKiOOOhSpue4D00%2BcYz2V2Z06rpl5scrkwz3D1oN2xw15ChHGN%2BoTlLsWbvvf4GRHN%2BUcvHEkYor9QHVhoE%2BdIu6%2BBGPb6q%2BHoMYv2efKqJrcOxe3g1gKi8j4Cn9iCkXSMCJXRsHPaFDTJ4La%2FYJcXmU37HexSeN%2FbgLbOf%2FLUPImBft%2B09Eb%2BTvH1MWwuFo15RytdWyblAxKjAjXml%2BzQAAHzeOAqPjn2JfJru6qyiEKMBx6nuBlkA80Wm6ui6kpDgCGXKcyPttYbSBFjWYITOqpo4S8xCeKoL7uEIsAe%2FdJffKVp%2BTpeQ%2FmgK7DC6kK00WFBB09hzCHoQy9JEw4EWY%2BDx12UQGcTCfCCuahrbzatmGtTtpK1NIsEbt3tezv7ZBqpMkV7BO5qt3Q90ZUYMbJbL4tZt%2B8ttustS%2FqS17JvM%2B0e7%2B05JSv1eNNuB7lbkWW2vpEiPUMclRmLRfH98fEW4Js87ko%2FavhL9zvtQBCiP2z2gHhRu2HPXde86bwKT24t51xkjAbepnEQHOpceB93mdJlbuUwxw%2F86RmTSoe4lpZl%2B6l9s9JY0iJ9acMe59CGIaDtSqP3OtOwYw3654q%2F6ciCggcnqwSQEBkto7a9e2mqyZ0zDJwfi8BjqkAUFeStkGTFt%2BFzUOPtK0CoIvqe%2FTLD1PlO4oQgA2ouoBfVIayVY32gpUun6VGc%2BS%2F%2FvHTSQ%2B6glChirB40%2FJeczOkblfyV%2FFogjEiQ5vtP5t89fSS%2FsDuZPgaW5JVrPuK75KgB%2BDDMWx%2B4QVuzkT5iH%2FnPdwAbbGqmcaBo0BY33VLM8%2FtHed%2BrjFzLjbhl7A%2FUNUGQEMOtMZilPBlY9MfKqs4vWw&X-Amz-Signature=59a31bc21d1ed49806492cc356a8e0f7242449d54bd6b4f71f049209c7e988b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662DO2KDK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiEmL%2BzTkjF1zcXhASmucf7JdHXzNnbUB2UfBmCRXNNAIhAI%2F3aboPD53HHhfxyzAzCV9McmEojw%2FCRtb1qtepZCWVKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyQZMV0yGJkLKSqlLcq3AO8OU%2FzgKiOOOhSpue4D00%2BcYz2V2Z06rpl5scrkwz3D1oN2xw15ChHGN%2BoTlLsWbvvf4GRHN%2BUcvHEkYor9QHVhoE%2BdIu6%2BBGPb6q%2BHoMYv2efKqJrcOxe3g1gKi8j4Cn9iCkXSMCJXRsHPaFDTJ4La%2FYJcXmU37HexSeN%2FbgLbOf%2FLUPImBft%2B09Eb%2BTvH1MWwuFo15RytdWyblAxKjAjXml%2BzQAAHzeOAqPjn2JfJru6qyiEKMBx6nuBlkA80Wm6ui6kpDgCGXKcyPttYbSBFjWYITOqpo4S8xCeKoL7uEIsAe%2FdJffKVp%2BTpeQ%2FmgK7DC6kK00WFBB09hzCHoQy9JEw4EWY%2BDx12UQGcTCfCCuahrbzatmGtTtpK1NIsEbt3tezv7ZBqpMkV7BO5qt3Q90ZUYMbJbL4tZt%2B8ttustS%2FqS17JvM%2B0e7%2B05JSv1eNNuB7lbkWW2vpEiPUMclRmLRfH98fEW4Js87ko%2FavhL9zvtQBCiP2z2gHhRu2HPXde86bwKT24t51xkjAbepnEQHOpceB93mdJlbuUwxw%2F86RmTSoe4lpZl%2B6l9s9JY0iJ9acMe59CGIaDtSqP3OtOwYw3654q%2F6ciCggcnqwSQEBkto7a9e2mqyZ0zDJwfi8BjqkAUFeStkGTFt%2BFzUOPtK0CoIvqe%2FTLD1PlO4oQgA2ouoBfVIayVY32gpUun6VGc%2BS%2F%2FvHTSQ%2B6glChirB40%2FJeczOkblfyV%2FFogjEiQ5vtP5t89fSS%2FsDuZPgaW5JVrPuK75KgB%2BDDMWx%2B4QVuzkT5iH%2FnPdwAbbGqmcaBo0BY33VLM8%2FtHed%2BrjFzLjbhl7A%2FUNUGQEMOtMZilPBlY9MfKqs4vWw&X-Amz-Signature=e48b8cd18d559ec800f64f2304cd628b6961ce23874954bca000dfe837bc7a50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662DO2KDK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiEmL%2BzTkjF1zcXhASmucf7JdHXzNnbUB2UfBmCRXNNAIhAI%2F3aboPD53HHhfxyzAzCV9McmEojw%2FCRtb1qtepZCWVKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyQZMV0yGJkLKSqlLcq3AO8OU%2FzgKiOOOhSpue4D00%2BcYz2V2Z06rpl5scrkwz3D1oN2xw15ChHGN%2BoTlLsWbvvf4GRHN%2BUcvHEkYor9QHVhoE%2BdIu6%2BBGPb6q%2BHoMYv2efKqJrcOxe3g1gKi8j4Cn9iCkXSMCJXRsHPaFDTJ4La%2FYJcXmU37HexSeN%2FbgLbOf%2FLUPImBft%2B09Eb%2BTvH1MWwuFo15RytdWyblAxKjAjXml%2BzQAAHzeOAqPjn2JfJru6qyiEKMBx6nuBlkA80Wm6ui6kpDgCGXKcyPttYbSBFjWYITOqpo4S8xCeKoL7uEIsAe%2FdJffKVp%2BTpeQ%2FmgK7DC6kK00WFBB09hzCHoQy9JEw4EWY%2BDx12UQGcTCfCCuahrbzatmGtTtpK1NIsEbt3tezv7ZBqpMkV7BO5qt3Q90ZUYMbJbL4tZt%2B8ttustS%2FqS17JvM%2B0e7%2B05JSv1eNNuB7lbkWW2vpEiPUMclRmLRfH98fEW4Js87ko%2FavhL9zvtQBCiP2z2gHhRu2HPXde86bwKT24t51xkjAbepnEQHOpceB93mdJlbuUwxw%2F86RmTSoe4lpZl%2B6l9s9JY0iJ9acMe59CGIaDtSqP3OtOwYw3654q%2F6ciCggcnqwSQEBkto7a9e2mqyZ0zDJwfi8BjqkAUFeStkGTFt%2BFzUOPtK0CoIvqe%2FTLD1PlO4oQgA2ouoBfVIayVY32gpUun6VGc%2BS%2F%2FvHTSQ%2B6glChirB40%2FJeczOkblfyV%2FFogjEiQ5vtP5t89fSS%2FsDuZPgaW5JVrPuK75KgB%2BDDMWx%2B4QVuzkT5iH%2FnPdwAbbGqmcaBo0BY33VLM8%2FtHed%2BrjFzLjbhl7A%2FUNUGQEMOtMZilPBlY9MfKqs4vWw&X-Amz-Signature=6f7766ca309e232ba0883970863e8b0b1d569c2f389fa2c595503ac032f8aa68&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675JADHV4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9qV%2Fo4U8PhIrb9Xl3z8qDGrcTnOE83Xw93czs%2BP%2B78AiBbvds5zHRKIV5kq895dbeOBz3pnpO3LUcsWc76hbe7UyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmihdBtiXlASPeyQtKtwDhnlPiv1zRd2KM963HtdgMvRM7coDRU%2B8Z2cAWJKVG36t%2BVsSkevk46%2Fp2xadU8b%2F5HKCNl4tDfys1R0cU2gl7Zil5xrDOBEtUk2M8CBkWAZG37BcgFesOvHvEfCL3DMXlj7QSVGD90a2U24EVYT%2BcZh4RVAIhpsWWHe6vQQ2m8OtiM8mkapbyraEWZgQXHTKyupqEnOlYhKBmKFw8xv8Tsa%2BwuDp1qyezJj8BUxaVPM%2FlJrEWsK7yUcDXKOtAp65hET1FehyoOTRvNQNHTjkLyZGbNOVX%2F6v942HgcO62Ce8ayqWQ3Imi4ms9vo%2BgrClzChA1xlQ8WZudpV4rpurLFE3JL6Yqukjl42TpPqQh%2BdkYb7ylrrK9IjsSqq%2BZY%2Bao0iQ29GsyaeuIy5yYk%2FTZQuhR5x5BFspljCp8rfNkOvIsEmlf6KfbqC7eBf5UfEC6PLD0q6Ak9%2FKmSZmo324Bi3UyykKrewnITo%2BHCw72u43IhSzP8RK%2BAEn9gMcGPEYQ3tBSxYRw4h6X64UnXLOc7IVjjD1YjK20fXNYCAQKJ2SGojzWEGzwyLedOSs9HlMXgsgOsKrpUmPihSrE1RMOmRwy8zA6BFxnCixBqFS9I8E7ITb2%2FI8VKdDbLMwycH4vAY6pgGmj7sRYt2D4PYntwa35WUttsi%2Bu%2Bya%2BSqGPUOvboP6CrwJEPpcpfw8DxtfS3sQjDFg4fK%2BZ%2FlaBojneJIMv9SvkLJkoLXuHlHH1Xn0LDbsIsoktAPfCZjSUS7uZoc1AvXSg7ocx2GDsyPk%2FkD6au%2FPINJ95puyFRDp%2BwLY98bqLBoJbE9Izb6jmbK1ygaK6s9FeIq0vt9cffBFE26gd9lLxjKCdBPv&X-Amz-Signature=ccf57cec84f34bdf41339294d3e2bf70a7fe09be8a5a82c915595764bc08afec&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675JADHV4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9qV%2Fo4U8PhIrb9Xl3z8qDGrcTnOE83Xw93czs%2BP%2B78AiBbvds5zHRKIV5kq895dbeOBz3pnpO3LUcsWc76hbe7UyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmihdBtiXlASPeyQtKtwDhnlPiv1zRd2KM963HtdgMvRM7coDRU%2B8Z2cAWJKVG36t%2BVsSkevk46%2Fp2xadU8b%2F5HKCNl4tDfys1R0cU2gl7Zil5xrDOBEtUk2M8CBkWAZG37BcgFesOvHvEfCL3DMXlj7QSVGD90a2U24EVYT%2BcZh4RVAIhpsWWHe6vQQ2m8OtiM8mkapbyraEWZgQXHTKyupqEnOlYhKBmKFw8xv8Tsa%2BwuDp1qyezJj8BUxaVPM%2FlJrEWsK7yUcDXKOtAp65hET1FehyoOTRvNQNHTjkLyZGbNOVX%2F6v942HgcO62Ce8ayqWQ3Imi4ms9vo%2BgrClzChA1xlQ8WZudpV4rpurLFE3JL6Yqukjl42TpPqQh%2BdkYb7ylrrK9IjsSqq%2BZY%2Bao0iQ29GsyaeuIy5yYk%2FTZQuhR5x5BFspljCp8rfNkOvIsEmlf6KfbqC7eBf5UfEC6PLD0q6Ak9%2FKmSZmo324Bi3UyykKrewnITo%2BHCw72u43IhSzP8RK%2BAEn9gMcGPEYQ3tBSxYRw4h6X64UnXLOc7IVjjD1YjK20fXNYCAQKJ2SGojzWEGzwyLedOSs9HlMXgsgOsKrpUmPihSrE1RMOmRwy8zA6BFxnCixBqFS9I8E7ITb2%2FI8VKdDbLMwycH4vAY6pgGmj7sRYt2D4PYntwa35WUttsi%2Bu%2Bya%2BSqGPUOvboP6CrwJEPpcpfw8DxtfS3sQjDFg4fK%2BZ%2FlaBojneJIMv9SvkLJkoLXuHlHH1Xn0LDbsIsoktAPfCZjSUS7uZoc1AvXSg7ocx2GDsyPk%2FkD6au%2FPINJ95puyFRDp%2BwLY98bqLBoJbE9Izb6jmbK1ygaK6s9FeIq0vt9cffBFE26gd9lLxjKCdBPv&X-Amz-Signature=ee8be0f1a769f036747cddc7d8d32776435a5a6d1a2635479d332c74d0dd5343&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675JADHV4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9qV%2Fo4U8PhIrb9Xl3z8qDGrcTnOE83Xw93czs%2BP%2B78AiBbvds5zHRKIV5kq895dbeOBz3pnpO3LUcsWc76hbe7UyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmihdBtiXlASPeyQtKtwDhnlPiv1zRd2KM963HtdgMvRM7coDRU%2B8Z2cAWJKVG36t%2BVsSkevk46%2Fp2xadU8b%2F5HKCNl4tDfys1R0cU2gl7Zil5xrDOBEtUk2M8CBkWAZG37BcgFesOvHvEfCL3DMXlj7QSVGD90a2U24EVYT%2BcZh4RVAIhpsWWHe6vQQ2m8OtiM8mkapbyraEWZgQXHTKyupqEnOlYhKBmKFw8xv8Tsa%2BwuDp1qyezJj8BUxaVPM%2FlJrEWsK7yUcDXKOtAp65hET1FehyoOTRvNQNHTjkLyZGbNOVX%2F6v942HgcO62Ce8ayqWQ3Imi4ms9vo%2BgrClzChA1xlQ8WZudpV4rpurLFE3JL6Yqukjl42TpPqQh%2BdkYb7ylrrK9IjsSqq%2BZY%2Bao0iQ29GsyaeuIy5yYk%2FTZQuhR5x5BFspljCp8rfNkOvIsEmlf6KfbqC7eBf5UfEC6PLD0q6Ak9%2FKmSZmo324Bi3UyykKrewnITo%2BHCw72u43IhSzP8RK%2BAEn9gMcGPEYQ3tBSxYRw4h6X64UnXLOc7IVjjD1YjK20fXNYCAQKJ2SGojzWEGzwyLedOSs9HlMXgsgOsKrpUmPihSrE1RMOmRwy8zA6BFxnCixBqFS9I8E7ITb2%2FI8VKdDbLMwycH4vAY6pgGmj7sRYt2D4PYntwa35WUttsi%2Bu%2Bya%2BSqGPUOvboP6CrwJEPpcpfw8DxtfS3sQjDFg4fK%2BZ%2FlaBojneJIMv9SvkLJkoLXuHlHH1Xn0LDbsIsoktAPfCZjSUS7uZoc1AvXSg7ocx2GDsyPk%2FkD6au%2FPINJ95puyFRDp%2BwLY98bqLBoJbE9Izb6jmbK1ygaK6s9FeIq0vt9cffBFE26gd9lLxjKCdBPv&X-Amz-Signature=9d124c84f68b377cd21fa3f06a08211c2df3ca682d0b230a4a34930ec3f4060f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675JADHV4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9qV%2Fo4U8PhIrb9Xl3z8qDGrcTnOE83Xw93czs%2BP%2B78AiBbvds5zHRKIV5kq895dbeOBz3pnpO3LUcsWc76hbe7UyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmihdBtiXlASPeyQtKtwDhnlPiv1zRd2KM963HtdgMvRM7coDRU%2B8Z2cAWJKVG36t%2BVsSkevk46%2Fp2xadU8b%2F5HKCNl4tDfys1R0cU2gl7Zil5xrDOBEtUk2M8CBkWAZG37BcgFesOvHvEfCL3DMXlj7QSVGD90a2U24EVYT%2BcZh4RVAIhpsWWHe6vQQ2m8OtiM8mkapbyraEWZgQXHTKyupqEnOlYhKBmKFw8xv8Tsa%2BwuDp1qyezJj8BUxaVPM%2FlJrEWsK7yUcDXKOtAp65hET1FehyoOTRvNQNHTjkLyZGbNOVX%2F6v942HgcO62Ce8ayqWQ3Imi4ms9vo%2BgrClzChA1xlQ8WZudpV4rpurLFE3JL6Yqukjl42TpPqQh%2BdkYb7ylrrK9IjsSqq%2BZY%2Bao0iQ29GsyaeuIy5yYk%2FTZQuhR5x5BFspljCp8rfNkOvIsEmlf6KfbqC7eBf5UfEC6PLD0q6Ak9%2FKmSZmo324Bi3UyykKrewnITo%2BHCw72u43IhSzP8RK%2BAEn9gMcGPEYQ3tBSxYRw4h6X64UnXLOc7IVjjD1YjK20fXNYCAQKJ2SGojzWEGzwyLedOSs9HlMXgsgOsKrpUmPihSrE1RMOmRwy8zA6BFxnCixBqFS9I8E7ITb2%2FI8VKdDbLMwycH4vAY6pgGmj7sRYt2D4PYntwa35WUttsi%2Bu%2Bya%2BSqGPUOvboP6CrwJEPpcpfw8DxtfS3sQjDFg4fK%2BZ%2FlaBojneJIMv9SvkLJkoLXuHlHH1Xn0LDbsIsoktAPfCZjSUS7uZoc1AvXSg7ocx2GDsyPk%2FkD6au%2FPINJ95puyFRDp%2BwLY98bqLBoJbE9Izb6jmbK1ygaK6s9FeIq0vt9cffBFE26gd9lLxjKCdBPv&X-Amz-Signature=264967a69a09fe2b31a00de73d70bb58bebfc20f2328c8068ec05e2f157edb50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675JADHV4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9qV%2Fo4U8PhIrb9Xl3z8qDGrcTnOE83Xw93czs%2BP%2B78AiBbvds5zHRKIV5kq895dbeOBz3pnpO3LUcsWc76hbe7UyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmihdBtiXlASPeyQtKtwDhnlPiv1zRd2KM963HtdgMvRM7coDRU%2B8Z2cAWJKVG36t%2BVsSkevk46%2Fp2xadU8b%2F5HKCNl4tDfys1R0cU2gl7Zil5xrDOBEtUk2M8CBkWAZG37BcgFesOvHvEfCL3DMXlj7QSVGD90a2U24EVYT%2BcZh4RVAIhpsWWHe6vQQ2m8OtiM8mkapbyraEWZgQXHTKyupqEnOlYhKBmKFw8xv8Tsa%2BwuDp1qyezJj8BUxaVPM%2FlJrEWsK7yUcDXKOtAp65hET1FehyoOTRvNQNHTjkLyZGbNOVX%2F6v942HgcO62Ce8ayqWQ3Imi4ms9vo%2BgrClzChA1xlQ8WZudpV4rpurLFE3JL6Yqukjl42TpPqQh%2BdkYb7ylrrK9IjsSqq%2BZY%2Bao0iQ29GsyaeuIy5yYk%2FTZQuhR5x5BFspljCp8rfNkOvIsEmlf6KfbqC7eBf5UfEC6PLD0q6Ak9%2FKmSZmo324Bi3UyykKrewnITo%2BHCw72u43IhSzP8RK%2BAEn9gMcGPEYQ3tBSxYRw4h6X64UnXLOc7IVjjD1YjK20fXNYCAQKJ2SGojzWEGzwyLedOSs9HlMXgsgOsKrpUmPihSrE1RMOmRwy8zA6BFxnCixBqFS9I8E7ITb2%2FI8VKdDbLMwycH4vAY6pgGmj7sRYt2D4PYntwa35WUttsi%2Bu%2Bya%2BSqGPUOvboP6CrwJEPpcpfw8DxtfS3sQjDFg4fK%2BZ%2FlaBojneJIMv9SvkLJkoLXuHlHH1Xn0LDbsIsoktAPfCZjSUS7uZoc1AvXSg7ocx2GDsyPk%2FkD6au%2FPINJ95puyFRDp%2BwLY98bqLBoJbE9Izb6jmbK1ygaK6s9FeIq0vt9cffBFE26gd9lLxjKCdBPv&X-Amz-Signature=352bac3c1d7748885c513457dbaaec7e176577ceb3c3d41da186ec15660dd65f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675JADHV4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9qV%2Fo4U8PhIrb9Xl3z8qDGrcTnOE83Xw93czs%2BP%2B78AiBbvds5zHRKIV5kq895dbeOBz3pnpO3LUcsWc76hbe7UyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmihdBtiXlASPeyQtKtwDhnlPiv1zRd2KM963HtdgMvRM7coDRU%2B8Z2cAWJKVG36t%2BVsSkevk46%2Fp2xadU8b%2F5HKCNl4tDfys1R0cU2gl7Zil5xrDOBEtUk2M8CBkWAZG37BcgFesOvHvEfCL3DMXlj7QSVGD90a2U24EVYT%2BcZh4RVAIhpsWWHe6vQQ2m8OtiM8mkapbyraEWZgQXHTKyupqEnOlYhKBmKFw8xv8Tsa%2BwuDp1qyezJj8BUxaVPM%2FlJrEWsK7yUcDXKOtAp65hET1FehyoOTRvNQNHTjkLyZGbNOVX%2F6v942HgcO62Ce8ayqWQ3Imi4ms9vo%2BgrClzChA1xlQ8WZudpV4rpurLFE3JL6Yqukjl42TpPqQh%2BdkYb7ylrrK9IjsSqq%2BZY%2Bao0iQ29GsyaeuIy5yYk%2FTZQuhR5x5BFspljCp8rfNkOvIsEmlf6KfbqC7eBf5UfEC6PLD0q6Ak9%2FKmSZmo324Bi3UyykKrewnITo%2BHCw72u43IhSzP8RK%2BAEn9gMcGPEYQ3tBSxYRw4h6X64UnXLOc7IVjjD1YjK20fXNYCAQKJ2SGojzWEGzwyLedOSs9HlMXgsgOsKrpUmPihSrE1RMOmRwy8zA6BFxnCixBqFS9I8E7ITb2%2FI8VKdDbLMwycH4vAY6pgGmj7sRYt2D4PYntwa35WUttsi%2Bu%2Bya%2BSqGPUOvboP6CrwJEPpcpfw8DxtfS3sQjDFg4fK%2BZ%2FlaBojneJIMv9SvkLJkoLXuHlHH1Xn0LDbsIsoktAPfCZjSUS7uZoc1AvXSg7ocx2GDsyPk%2FkD6au%2FPINJ95puyFRDp%2BwLY98bqLBoJbE9Izb6jmbK1ygaK6s9FeIq0vt9cffBFE26gd9lLxjKCdBPv&X-Amz-Signature=289ccbaccd8434b2a0dec67b0318361024dce8935acb831f3851ca3cf39d8c43&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TB36TWK5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFlFTnK%2FJV%2Bdr9veSqEC30UpA9sICOtzLm%2B79wMmwVTXAiAn3Sn3gpb8cujD%2BUped0hjL4X%2F6sqGMf8tYmfe3RLq3SqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq2ZJKLG3rRXDcXK%2FKtwDAS7AtzaxYuAbhdgW%2BFF%2FIki76ZAbCQXjZ0ebicNrRoF3ce41mWVvI%2FWoG%2BZuwWg06BAIB8o%2F8aEI3x9V7%2Fs0MhHXh%2FTWG42Zq9GFNP2Lem%2B3jol6MC9zpgg5klJRSoIxfABEwtvmzlSarzXE9BxC0oYZ9Tr%2Bx7aMhzXwhUwS%2FtVLxPEFZN322bDDlVz5gNjccaPTb4uTU4Bc3HgT6vSOj58tx35PJvcSPOceQVzXxWzo6suILEyUnnvOf3YJBZ5pzxXp5w5FvadJjsFeiJ7nZ09rEJEdQMrZ2jQHaAnu%2BBtlGFvhlVkEviAxzLDu9ehuLAdh7G8ayOb3exyrJarAV3EmzoFCqORIcW3bZYsp6HOInKPfrUnozhQV%2FViJO2elJknO8ukQrHvSYz3VBd2h9wzUYhllWKY%2BtdBvveiksJTiLd21qr599ZtLaLI3dfiOHGYYd6Q9%2FwY5MFZkqkb3cvQwqNLHf5bkV8tbwLAqErWYHPrBHpRQX9MZTEy%2BxjGNnLetrsPj%2BiPzV9AKPuNrLRszisGhpFYT2GDUhTEE8%2FDC%2BjDzl39Jw%2FJuE244javc%2BRbtukCb0vy17Klk5rGpGYGUF6GJZf7HgGWH0X2T2UlLv6cS0ahvfZBYY78wksn4vAY6pgH8NxPP64Q%2Bd7rg9OiqiU8QDlfccBSKHzdqPDlaLbMnWrLYa7dcfymL4c4ciGHeQPrsIDyWDEPaFQc7P7UFVp23MmU8TYG9BlAabM2OsTvPe8zzN9gFQBNPKG3qdxRvKdwSOuIxr%2ByMWjK5%2Ben7RyCGRC3kHR84Jrz8di7bk9XknQYcc%2Ff7fL8a%2BEwih22gyHKVsBUqEtufzQqfgcw1PYEQkrqN%2F%2FwE&X-Amz-Signature=e0b59bd14e69b41921caf9a3c8a78dd64625fc3d504e5d2346e297fc80c5646e&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3ACQWJ2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBFvDFSVt7z3yeN0xNNLINVggMEBr1cZd5UF3jvXVU76AiEA3aljIpeL3sSvj1A%2FnxW9QRrqEv7X7C0tRnmPAyrmJicqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObJNVjt%2FlMcrRsRMSrcAwYztaHiv1Hwk4ZC6FBHD4ECJXzE491f%2F5WvE%2B1JYfAfW4h2TBrmkFV%2B8Ar1gEtG8GMc7U1vz%2FPFBNRCve9rTCBNtAVW6045ndgsnxSdWNwGXgqNUauu90EyvB4ApYr3U%2F08c5dcteEhqRJEvwZlIRjv61bTL37OH%2BLxFKUl6TWdNeNAltEGgOpVo9U%2FiyOw4bJuKIm0OM%2FmINyh6XVYTrA5QKzSyXj4JB5xxwUlrSCP99pR9okgLJlzDp4yGF%2F2ECA4zIMULeSDRhGxZqKg%2Fq%2BoZ6qovrvCeFp4BqEIRJm%2Bkvcf90eE1e8PJgt4Q2K1PC%2BaxwnF%2FV3R6eDCZ1UZyrAyEVqC7zzu2UVJkFTgsbCLQ3ADc717AUb1CBQyu3Up0xSB1pXw1XAYTcNQ3eMpLSD7NBO7F9H%2ByUUo1w%2B2bzJLZVltQm%2BRLluJE5XDR9pV%2B0pqpk18TEh9EBc75hjwRMptbxj1J04d5U59kENs%2BnNOkypQS3d8dMukVGl5MNDXR5mkjOMw3OJzjeJIg5eJ7W4E9iyy58b0lRMVPVXKVIZ9PpzKrfuL9KQSNZw2KFVqDkGx3268h6PKlsy1R%2BUfFK9uSgW0vZpgeNZOJgg81nmFLqPVSFqYR46Go3%2FlMLrL%2BLwGOqUBQ%2BCkTKJVNJ%2Bdt%2F6AFgNZDlV3U8Antf8HScSnCjZTJwgSZyX75zafJZB6mgvTm4iyGs7OwT4cxbkLQuTAHlhfqLmK%2F7tolw5UXQQ%2Fp7xMMl1Msu4wOl9EOGaSkXbtTDmXqqOUOc0qtyGOzpIXbq2zZau5pD%2BWDUUx89FznRb3k80kRTU4puJSVBTwYliHnHhZ7T%2BDpABmh7nVbfbS2jtIBWfa5pCy&X-Amz-Signature=672f79c10efc212963bea279f5a02179dea6a244eecc817d58e4f58bed930f01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675JADHV4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9qV%2Fo4U8PhIrb9Xl3z8qDGrcTnOE83Xw93czs%2BP%2B78AiBbvds5zHRKIV5kq895dbeOBz3pnpO3LUcsWc76hbe7UyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmihdBtiXlASPeyQtKtwDhnlPiv1zRd2KM963HtdgMvRM7coDRU%2B8Z2cAWJKVG36t%2BVsSkevk46%2Fp2xadU8b%2F5HKCNl4tDfys1R0cU2gl7Zil5xrDOBEtUk2M8CBkWAZG37BcgFesOvHvEfCL3DMXlj7QSVGD90a2U24EVYT%2BcZh4RVAIhpsWWHe6vQQ2m8OtiM8mkapbyraEWZgQXHTKyupqEnOlYhKBmKFw8xv8Tsa%2BwuDp1qyezJj8BUxaVPM%2FlJrEWsK7yUcDXKOtAp65hET1FehyoOTRvNQNHTjkLyZGbNOVX%2F6v942HgcO62Ce8ayqWQ3Imi4ms9vo%2BgrClzChA1xlQ8WZudpV4rpurLFE3JL6Yqukjl42TpPqQh%2BdkYb7ylrrK9IjsSqq%2BZY%2Bao0iQ29GsyaeuIy5yYk%2FTZQuhR5x5BFspljCp8rfNkOvIsEmlf6KfbqC7eBf5UfEC6PLD0q6Ak9%2FKmSZmo324Bi3UyykKrewnITo%2BHCw72u43IhSzP8RK%2BAEn9gMcGPEYQ3tBSxYRw4h6X64UnXLOc7IVjjD1YjK20fXNYCAQKJ2SGojzWEGzwyLedOSs9HlMXgsgOsKrpUmPihSrE1RMOmRwy8zA6BFxnCixBqFS9I8E7ITb2%2FI8VKdDbLMwycH4vAY6pgGmj7sRYt2D4PYntwa35WUttsi%2Bu%2Bya%2BSqGPUOvboP6CrwJEPpcpfw8DxtfS3sQjDFg4fK%2BZ%2FlaBojneJIMv9SvkLJkoLXuHlHH1Xn0LDbsIsoktAPfCZjSUS7uZoc1AvXSg7ocx2GDsyPk%2FkD6au%2FPINJ95puyFRDp%2BwLY98bqLBoJbE9Izb6jmbK1ygaK6s9FeIq0vt9cffBFE26gd9lLxjKCdBPv&X-Amz-Signature=0eb0d407ee54bfdca33fd4b22042b9c826e33e6690eeb8a93ca1f31e207b5db7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675JADHV4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9qV%2Fo4U8PhIrb9Xl3z8qDGrcTnOE83Xw93czs%2BP%2B78AiBbvds5zHRKIV5kq895dbeOBz3pnpO3LUcsWc76hbe7UyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmihdBtiXlASPeyQtKtwDhnlPiv1zRd2KM963HtdgMvRM7coDRU%2B8Z2cAWJKVG36t%2BVsSkevk46%2Fp2xadU8b%2F5HKCNl4tDfys1R0cU2gl7Zil5xrDOBEtUk2M8CBkWAZG37BcgFesOvHvEfCL3DMXlj7QSVGD90a2U24EVYT%2BcZh4RVAIhpsWWHe6vQQ2m8OtiM8mkapbyraEWZgQXHTKyupqEnOlYhKBmKFw8xv8Tsa%2BwuDp1qyezJj8BUxaVPM%2FlJrEWsK7yUcDXKOtAp65hET1FehyoOTRvNQNHTjkLyZGbNOVX%2F6v942HgcO62Ce8ayqWQ3Imi4ms9vo%2BgrClzChA1xlQ8WZudpV4rpurLFE3JL6Yqukjl42TpPqQh%2BdkYb7ylrrK9IjsSqq%2BZY%2Bao0iQ29GsyaeuIy5yYk%2FTZQuhR5x5BFspljCp8rfNkOvIsEmlf6KfbqC7eBf5UfEC6PLD0q6Ak9%2FKmSZmo324Bi3UyykKrewnITo%2BHCw72u43IhSzP8RK%2BAEn9gMcGPEYQ3tBSxYRw4h6X64UnXLOc7IVjjD1YjK20fXNYCAQKJ2SGojzWEGzwyLedOSs9HlMXgsgOsKrpUmPihSrE1RMOmRwy8zA6BFxnCixBqFS9I8E7ITb2%2FI8VKdDbLMwycH4vAY6pgGmj7sRYt2D4PYntwa35WUttsi%2Bu%2Bya%2BSqGPUOvboP6CrwJEPpcpfw8DxtfS3sQjDFg4fK%2BZ%2FlaBojneJIMv9SvkLJkoLXuHlHH1Xn0LDbsIsoktAPfCZjSUS7uZoc1AvXSg7ocx2GDsyPk%2FkD6au%2FPINJ95puyFRDp%2BwLY98bqLBoJbE9Izb6jmbK1ygaK6s9FeIq0vt9cffBFE26gd9lLxjKCdBPv&X-Amz-Signature=bb000093c4dc5458e64a53a63b1faadbd12a2893f2ff7442dbaa55b020677bce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675JADHV4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9qV%2Fo4U8PhIrb9Xl3z8qDGrcTnOE83Xw93czs%2BP%2B78AiBbvds5zHRKIV5kq895dbeOBz3pnpO3LUcsWc76hbe7UyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmihdBtiXlASPeyQtKtwDhnlPiv1zRd2KM963HtdgMvRM7coDRU%2B8Z2cAWJKVG36t%2BVsSkevk46%2Fp2xadU8b%2F5HKCNl4tDfys1R0cU2gl7Zil5xrDOBEtUk2M8CBkWAZG37BcgFesOvHvEfCL3DMXlj7QSVGD90a2U24EVYT%2BcZh4RVAIhpsWWHe6vQQ2m8OtiM8mkapbyraEWZgQXHTKyupqEnOlYhKBmKFw8xv8Tsa%2BwuDp1qyezJj8BUxaVPM%2FlJrEWsK7yUcDXKOtAp65hET1FehyoOTRvNQNHTjkLyZGbNOVX%2F6v942HgcO62Ce8ayqWQ3Imi4ms9vo%2BgrClzChA1xlQ8WZudpV4rpurLFE3JL6Yqukjl42TpPqQh%2BdkYb7ylrrK9IjsSqq%2BZY%2Bao0iQ29GsyaeuIy5yYk%2FTZQuhR5x5BFspljCp8rfNkOvIsEmlf6KfbqC7eBf5UfEC6PLD0q6Ak9%2FKmSZmo324Bi3UyykKrewnITo%2BHCw72u43IhSzP8RK%2BAEn9gMcGPEYQ3tBSxYRw4h6X64UnXLOc7IVjjD1YjK20fXNYCAQKJ2SGojzWEGzwyLedOSs9HlMXgsgOsKrpUmPihSrE1RMOmRwy8zA6BFxnCixBqFS9I8E7ITb2%2FI8VKdDbLMwycH4vAY6pgGmj7sRYt2D4PYntwa35WUttsi%2Bu%2Bya%2BSqGPUOvboP6CrwJEPpcpfw8DxtfS3sQjDFg4fK%2BZ%2FlaBojneJIMv9SvkLJkoLXuHlHH1Xn0LDbsIsoktAPfCZjSUS7uZoc1AvXSg7ocx2GDsyPk%2FkD6au%2FPINJ95puyFRDp%2BwLY98bqLBoJbE9Izb6jmbK1ygaK6s9FeIq0vt9cffBFE26gd9lLxjKCdBPv&X-Amz-Signature=46af6e718673df25acac5b7a4b4ee21ff419b5f081c519feb8fa2b1d5fbd42e7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B3HDKMA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmTPCw1MCO3FJhBuJHuYvvza%2BXCKsLLYeg58IQTYB%2FegIgFiSDa2C9E6XnFOr2GFUyOxKyjaclzkVsjZ8zUPViSxIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNymqwIyd0iJSCSnRSrcA7ZaKOaT7nJOseMnaFszvQ%2F4X0jOzp7nuCxMmq7syjmeSLQpml0lR8kVNdZ9lI3M6KwKAVUu90eFDOF0SqUYSfwV6HBfs2f5EOGI0JU4ifsCjQdUwf3NTdStFnJ3gj1NZMjFzBcGiZGQgQqUJlQQkmeA48oF%2BCR86SlT%2Ff8LrObUi%2F9hXpkrbuoR98n9qBXr6%2Bswl6EGlTR46zKCDyi1Qa0ki2Dk47kBwtiy2jBYS6RJHrm1IE6F1%2Bx%2BZPmMIVvH9NGP4MOZYEOSqqDwstthh3OXDfa39pINz04pwv93H7KU4ov50Udle0JTl%2Ba4iIImmnKbG61k88S1Lf2lpuPspq1vwn6W48Hn7OtA72p5iPQ9OcP%2Fa2v%2FuH4N2jOos%2FI6%2BoDEHoCDB15EhtYcZgfPkMGJ2yeoaDho8AZHSKcSjTVSwq1ag4UfQQzrxmXt9TCj9ttV0OBniTf6WdN4uAv1NQ4NJTBjPhYUYQIJ0EdRXcWGw%2Fz9oqH5OgwEufRDaR%2BfXTuwQz43nJEbbbLsFGhWe4p5wZtMhXgKj%2BkuA2XkLHATCT0cr1FgijA8q368zDLjXzJ7bqLTzVxU9cZO9j0GDG3%2Fty2N5q203Fnn8DbB2iFd3LZYJgK4IMw4233oMKvJ%2BLwGOqUBO6kHusb5va%2Be9l9WrM9LtP%2FtyFHdAqkh35sc0DN6S%2FzoHcd%2FINUM2O6vRowi54PMqRaJlhml0%2B3BMpqIPaxQO39jux1SrkOaJi8k3IOJRICPJNM2wXZNAkRu7ov4GSzwYiPWqIRkBf%2B%2FZHP4X7h6VjFMlRBHmUOJcNHZ0f%2FhU5UgZ7dT3ZwRUQpxgFJpV%2Ft1wAFvPc5NDhFW50rX4aPbZ15N9SMg&X-Amz-Signature=749efaa051005cac588f5c3ca240ab5debcf934c6cc5eea39f017823eeb87e2c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IFKHDRV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjopzeb7ACHsIIIJsAds4zd3KRKEcmFAwWXHzoGSyFYAiEA61chvPRJ6vl5TjcNDos09d6bc5N0DkBgDKncll%2BNI4QqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKb1h9PhUBtoQR4kPircA64Eesd23w65NxFV7nziWtdRhQY9ybpEJJ4zfgdVQrEJMi0Nfn1Kucr%2BNgOJoCG4N%2FY5Q3VPxEWjc6NgEcdT%2FwPOpRtc%2ByiR5GSE82EeHiEsy0XMyEuKpajLwP13PvcmgUSzff6y%2FyKNh8ekE5QvtvKKdWjCs5Kz2Swd6QP0qJjFR9ETZ3alkP%2Fiy1Kl2DghhoK%2Fhc9UbdZyyG1lncLV8d%2FkaVHZ5LzM0lbNQgtxiTYWbeAMjCdF1uFcuhlEAw7cHlf9mxDyqpaBZ2CsHQJ2zjCTIpN1yBBKKI3TPkJ7ox7GPxl%2BBZ6GkHuG21WdubfUsXzcdN6dAaL0jJPGwsXxaMbs4LxRQHVe%2BayZPhcoclw7i3B8nugTTdF883ijTEJb%2BNm%2BmkMuzXsqbk6ABmAwH3H7aKb4ohWzf6GaqdNYEsGwbqTq9tF6Bk1d84RD6uVycBHneGrK6NxBIyIRBsGJGKHticp2u0Tyf2%2BqzHayL2dFTuM7XUXBmEn8ibSaAe%2FZwRBzir8EBaHL3LaRM3VwpNnPegYwwroc0GG1NvFxU4W3HDlbflUYQJ%2BhSmKwQnV86%2FaIhWDWdElqmSRBG4qECPD8ZVe%2FqKYuYPJ%2B0z8YtJR0wxrhvg04aczLQnWsMPfF%2BLwGOqUBex49UTwn2jAwk5r3YxrSY%2Ftb5BP4JxlgM%2BojdfwYhHJpXHWB4d1ShbCeiaErWs9vImmSodqUbOnqGGi3Is6F0%2FbAjzLfnBQXp94fio3Wlf2Q2nYUdXVUCWoUv4syU1iSoawTJhLZ2FUrorKxFIui890JxBk4Jum9Sf5fCvB7vyZ3deMiPjOyxSQTVIbHr8llAfauvO2ozgvDpUe4jQyxnSHyxOo0&X-Amz-Signature=c42b21f54ef387464b8fca18da7244dcddf3282f6d37c3d7cf07f69ea80991b5&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UNBZXIW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbAlwAiYoSja%2FOUTWiO7DGCK7aa9Mn%2BxR99Hx%2BkuaEMAIhAO9gvuUIZlcz6GOPKDmAdotjHOWdWClXbFUHbHoAxq1OKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydpkJYVZ877EzB5Toq3ANr8HDAezPqTcpMBZsi4eNGJZvyP0dFXTV6wgGuD%2FxSm%2Bv9G3r2lkih0As%2BI9e%2FwYKi1kFPlcdhjtyNmQIJM7MqpJAuFk7R6IdbjzbWtIRK1ddqxz07N%2BX9O8XAN1HZYQGtUOyjONS1QineWoQxdeShDCKJnVfJuPqjTNkOcWsdUnDufcIn30nAJao3KfHZa7ZxBby6MzYqFfY8zDODlnmre8mxPkg%2BJwkYpb2hP8uHM5alfhx4VFFpmHyyAIMeJGSKM1fDO%2FtSTnWIEZvWxa8ZIUve%2B7pEM9aRawCx0FKnLzmZ2UFKICNsamnRluUoRRiSl7GRax0THWAFV%2BxkKLu2f8sznNjHWZ1XX4Q%2FaYhnEgxlxD00PXuxbmmyAvNXXpDHf7Youd%2B7qAc2mUlOS2WSq3GAzkANC1i7oUJPI0t4OMaQ8sQqzHG4ptTYDk%2FAfiFAj7iOEKpxaX8O1r8TZDbyntQ09TNbqCOLIcFnOy31CgakTxaMa6wf%2FAHUQ6S61UcDVZdpfWovPOIAXdbDydf5l%2B%2FjAShLdcTKsl%2Fi43zFAixxSZ3V8KJbbxoCsj9v0ZTCfpJ6MaccrAavtAbHgaAKqvQ%2FGuz24DUtXjb5hQgEtlaELkeQNAEpTBtF8TC%2Bvfi8BjqkAVB6o12esWFmCttxdpIQY3fXRwdeVPx2e%2BkSC%2B5VL4LwQ0QPVmp%2FdNdshwPP0Dwe%2FcBx3jOXJ7bw7S6c5ZfJkwXAw0%2FpHT7CU8ChpyqhfesbKHS3D%2BbCmClaJRV6SRjOVRMGv8321wBPVefZW2l4J1Uwt1YqzPlUcoTSe5KenyQ5AeDXr6N3qXKFAEzCGAn4JuVS59Ejfj1bLig2jr6Dmv7t%2F4%2B7&X-Amz-Signature=0adb5d42e894b62186bf7e8b3505433ddc25d2c7c6aa9f322d3e512d953b4cb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXKY2ZYB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCMF1AUveQ0wHM5QxXVh4oFiq9MPD2l2wEIlYOfLrEjwIgY29eEFsEZCsEB0Jq%2FjCguLlkz%2FzEttQ42YthaS23JBkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEIpMcRzIG2JIAMHOSrcA7QMorpZaz5LjlC6mlN4YXDwy532vdnbDIIOfavnVs8SAeYM4CZ71T5FsGxvAMRtOUgArxsiT3ec46GJ6D0CqVt1jJcOVwvsY8f%2BA1XBQnc1O90BkzNv6aPGy01XoCgIsrtdt40%2FwGUlFujWfCXsk5Nrv%2B9PrAsSA78S78bWSyY5O0V9B4MZgGCnU%2Fx1chL2nhEW9v90V5AQbz9qaRoZMd%2F3eEdmJaEbFKqwgg3WGSF6qpOnOjUnHEIkaTURR2r7ceXAClGgfm8UfkkFbAzCc8%2BW7sQr1kr%2F%2B4zGIe7dv62Dch7IKS6%2FXizttFWCEbZllrBH1jw4KysOS9rhK8yxGuzKD%2B5n7GaZKjoe5sTVrbRACXQBBHyVumgrfEC25yohV5iKC0l5azfdA1VZavEmVy0m%2BIgTZn23Cx6eb49uKDUaJiwwWG%2BXcR3AN9X7ClvlUtUeesbRbkmCjitPpiUZtJokGld02gHlBS9lvhDCxOczpJd4Ihb2okTr2g4u6AviooG1IdXdb2IFTx9ArY1WkUJyHwbmt5x2MOchIBUSvOTvlYQbdHBX8cyWdbW2CeeckAsNKWZr3GOZ19ChzhDjjFJp8t596X1o57oaOmgBylDWxYi1dD3e3UFnDkF6MMnG%2BLwGOqUBC%2FHhC7TKI0Qom7Im%2FMUpMv55oVD%2Bwb0oVIyYm3ba0dpaj5ONC1PWfyfQoOixHGrlv%2FjMlLWaEoPtnlqBs4%2FsJWWhEChGWaS3eU3iTRGTQ%2FR3Jb9hy7zr3nngfTgao7tGGbVHS9rktbg50KrYCEgyDBf5mgBdp8bCE%2F%2BA6XqjZM1wUk3zJBMGyZp9QqmJPED9vYFTpObIahBeym1jRXsMu1agl7iB&X-Amz-Signature=84e79985e591c2ea8f23b76cb29b59347466aaf0a4179b30a3934c3b7cb2a889&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXKY2ZYB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCMF1AUveQ0wHM5QxXVh4oFiq9MPD2l2wEIlYOfLrEjwIgY29eEFsEZCsEB0Jq%2FjCguLlkz%2FzEttQ42YthaS23JBkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEIpMcRzIG2JIAMHOSrcA7QMorpZaz5LjlC6mlN4YXDwy532vdnbDIIOfavnVs8SAeYM4CZ71T5FsGxvAMRtOUgArxsiT3ec46GJ6D0CqVt1jJcOVwvsY8f%2BA1XBQnc1O90BkzNv6aPGy01XoCgIsrtdt40%2FwGUlFujWfCXsk5Nrv%2B9PrAsSA78S78bWSyY5O0V9B4MZgGCnU%2Fx1chL2nhEW9v90V5AQbz9qaRoZMd%2F3eEdmJaEbFKqwgg3WGSF6qpOnOjUnHEIkaTURR2r7ceXAClGgfm8UfkkFbAzCc8%2BW7sQr1kr%2F%2B4zGIe7dv62Dch7IKS6%2FXizttFWCEbZllrBH1jw4KysOS9rhK8yxGuzKD%2B5n7GaZKjoe5sTVrbRACXQBBHyVumgrfEC25yohV5iKC0l5azfdA1VZavEmVy0m%2BIgTZn23Cx6eb49uKDUaJiwwWG%2BXcR3AN9X7ClvlUtUeesbRbkmCjitPpiUZtJokGld02gHlBS9lvhDCxOczpJd4Ihb2okTr2g4u6AviooG1IdXdb2IFTx9ArY1WkUJyHwbmt5x2MOchIBUSvOTvlYQbdHBX8cyWdbW2CeeckAsNKWZr3GOZ19ChzhDjjFJp8t596X1o57oaOmgBylDWxYi1dD3e3UFnDkF6MMnG%2BLwGOqUBC%2FHhC7TKI0Qom7Im%2FMUpMv55oVD%2Bwb0oVIyYm3ba0dpaj5ONC1PWfyfQoOixHGrlv%2FjMlLWaEoPtnlqBs4%2FsJWWhEChGWaS3eU3iTRGTQ%2FR3Jb9hy7zr3nngfTgao7tGGbVHS9rktbg50KrYCEgyDBf5mgBdp8bCE%2F%2BA6XqjZM1wUk3zJBMGyZp9QqmJPED9vYFTpObIahBeym1jRXsMu1agl7iB&X-Amz-Signature=4cd6a331d374446a11853d0d704f6d0db64545e12a4846f111da60d11514bf1d&X-Amz-SignedHeaders=host&x-id=GetObject)

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
