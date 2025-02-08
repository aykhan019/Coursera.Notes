

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DV6IRMX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGvDCM42RaGGTk8WyKhT%2BfbsPm6xptw8%2FlE6Y7M29dgxAiEAlVrNv3I%2BBdAfK%2BG2lTgfc1HXCiy7ftJ4sNrcIWJiQH4qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPe%2BBC03fq3d3T8jQircA844Ca%2BI%2BRXG%2Bl%2BYYgjsBoD7cjsuAtUFJebzFA7uj%2BfpmiKHCm1enBuzwJ57tDYTL%2FhZh1sjrbWMsMs66svBJkG%2FXo9zMN3QK%2B29XRbRGRIDWT6KNsmsDVDW2Loq2SAF1keLdKd%2Bee9VWd1Cp6j8dnRIpsJpfKOmFNQbx%2FA616kMaI1tMk29n32BUMCGNo0Ge362jOupFH7OuBVl39nKG5yPTfW6NGImfD4kvxFB2WByxA7bv476aFx19U%2BtmWfFFmrdZaj%2FLbbn0gwaP1xBvajrh4cD5aHZKy3Qb3lBSy1dWeaq5lxo2kCBqM2g07Bn9FRKWPrDIxZVfjQFBW6z18851bCS6%2FrZ2Rvt2GeTx7LrmeKe1OKh4f6mwu1ERwczd%2FpGoOs8Z1mQ06Aw7slwD2NH%2BpGGfmgjqCISFW4a7AA50kjoCYn6e4jN1PDRZZAZZxe9a%2FKCn0wW3G0wWuX%2FUCdXVjkEoeo2mnDLno5GXo7nWpcQVK5cmk9uliZmLeFJeUMu%2Bc67uFcpg2axJKpL46bTR44xj8Ri4LiVrnEMw2Lq8hgTfPjQRiTegbf2SWqQIoCg2HeuxzgIRIPF%2Fz6oeHRr0yBkxjYyL794Gx5HDsjfBs35%2F9m9i6Kb3SK5MKyFnb0GOqUBdk%2BSrVIvRcuBrRliglh0igXSoJvbVG5qMqZBubH4tW8iSQtJ2MMJ%2FQSG1ItapQFzoKsYO4bK83auoO%2FUGrYs7u8tM59KREPtUAiCw1GVT%2F3zJWy7bQdcdRw2rB1Oj0jcP2shGAXlKlWLCByvPT5u9x5BJJNm6LESwmZzU1bxfriq1nZK5%2BhVH%2FuG4LOi2d5GQVqfgLtq0dPDJrOpHJPjvt%2FgkafI&X-Amz-Signature=982da06ccb25a26c95481fea9c932389e06735c27533759ed23e85079be62b39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DV6IRMX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGvDCM42RaGGTk8WyKhT%2BfbsPm6xptw8%2FlE6Y7M29dgxAiEAlVrNv3I%2BBdAfK%2BG2lTgfc1HXCiy7ftJ4sNrcIWJiQH4qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPe%2BBC03fq3d3T8jQircA844Ca%2BI%2BRXG%2Bl%2BYYgjsBoD7cjsuAtUFJebzFA7uj%2BfpmiKHCm1enBuzwJ57tDYTL%2FhZh1sjrbWMsMs66svBJkG%2FXo9zMN3QK%2B29XRbRGRIDWT6KNsmsDVDW2Loq2SAF1keLdKd%2Bee9VWd1Cp6j8dnRIpsJpfKOmFNQbx%2FA616kMaI1tMk29n32BUMCGNo0Ge362jOupFH7OuBVl39nKG5yPTfW6NGImfD4kvxFB2WByxA7bv476aFx19U%2BtmWfFFmrdZaj%2FLbbn0gwaP1xBvajrh4cD5aHZKy3Qb3lBSy1dWeaq5lxo2kCBqM2g07Bn9FRKWPrDIxZVfjQFBW6z18851bCS6%2FrZ2Rvt2GeTx7LrmeKe1OKh4f6mwu1ERwczd%2FpGoOs8Z1mQ06Aw7slwD2NH%2BpGGfmgjqCISFW4a7AA50kjoCYn6e4jN1PDRZZAZZxe9a%2FKCn0wW3G0wWuX%2FUCdXVjkEoeo2mnDLno5GXo7nWpcQVK5cmk9uliZmLeFJeUMu%2Bc67uFcpg2axJKpL46bTR44xj8Ri4LiVrnEMw2Lq8hgTfPjQRiTegbf2SWqQIoCg2HeuxzgIRIPF%2Fz6oeHRr0yBkxjYyL794Gx5HDsjfBs35%2F9m9i6Kb3SK5MKyFnb0GOqUBdk%2BSrVIvRcuBrRliglh0igXSoJvbVG5qMqZBubH4tW8iSQtJ2MMJ%2FQSG1ItapQFzoKsYO4bK83auoO%2FUGrYs7u8tM59KREPtUAiCw1GVT%2F3zJWy7bQdcdRw2rB1Oj0jcP2shGAXlKlWLCByvPT5u9x5BJJNm6LESwmZzU1bxfriq1nZK5%2BhVH%2FuG4LOi2d5GQVqfgLtq0dPDJrOpHJPjvt%2FgkafI&X-Amz-Signature=9d5ffb059cd5bfa4c2a20e0c9f74b743d98fdb7e15eedf9af54a944315cbe098&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DV6IRMX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGvDCM42RaGGTk8WyKhT%2BfbsPm6xptw8%2FlE6Y7M29dgxAiEAlVrNv3I%2BBdAfK%2BG2lTgfc1HXCiy7ftJ4sNrcIWJiQH4qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPe%2BBC03fq3d3T8jQircA844Ca%2BI%2BRXG%2Bl%2BYYgjsBoD7cjsuAtUFJebzFA7uj%2BfpmiKHCm1enBuzwJ57tDYTL%2FhZh1sjrbWMsMs66svBJkG%2FXo9zMN3QK%2B29XRbRGRIDWT6KNsmsDVDW2Loq2SAF1keLdKd%2Bee9VWd1Cp6j8dnRIpsJpfKOmFNQbx%2FA616kMaI1tMk29n32BUMCGNo0Ge362jOupFH7OuBVl39nKG5yPTfW6NGImfD4kvxFB2WByxA7bv476aFx19U%2BtmWfFFmrdZaj%2FLbbn0gwaP1xBvajrh4cD5aHZKy3Qb3lBSy1dWeaq5lxo2kCBqM2g07Bn9FRKWPrDIxZVfjQFBW6z18851bCS6%2FrZ2Rvt2GeTx7LrmeKe1OKh4f6mwu1ERwczd%2FpGoOs8Z1mQ06Aw7slwD2NH%2BpGGfmgjqCISFW4a7AA50kjoCYn6e4jN1PDRZZAZZxe9a%2FKCn0wW3G0wWuX%2FUCdXVjkEoeo2mnDLno5GXo7nWpcQVK5cmk9uliZmLeFJeUMu%2Bc67uFcpg2axJKpL46bTR44xj8Ri4LiVrnEMw2Lq8hgTfPjQRiTegbf2SWqQIoCg2HeuxzgIRIPF%2Fz6oeHRr0yBkxjYyL794Gx5HDsjfBs35%2F9m9i6Kb3SK5MKyFnb0GOqUBdk%2BSrVIvRcuBrRliglh0igXSoJvbVG5qMqZBubH4tW8iSQtJ2MMJ%2FQSG1ItapQFzoKsYO4bK83auoO%2FUGrYs7u8tM59KREPtUAiCw1GVT%2F3zJWy7bQdcdRw2rB1Oj0jcP2shGAXlKlWLCByvPT5u9x5BJJNm6LESwmZzU1bxfriq1nZK5%2BhVH%2FuG4LOi2d5GQVqfgLtq0dPDJrOpHJPjvt%2FgkafI&X-Amz-Signature=22818d9aaadfe38ff9e5913c85b1d372258edabc6d018db4319707363fd80a6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWOWCRQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBXqqaSFauC%2B54yOdJ51q%2FnjiKato9M8uf9%2FIb12XWfeAiAOW0B%2Bszn%2FA7eV%2FJkC1Jj%2FI00aoaKtQEe9fDva7yvoGSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8JqqO3OfEJuyS66nKtwDfflq3CF5ln6ZFZcQcmc%2FAGq5tKtAJ6cBQYMkMGos7Kb7hZKYnv26StTBo9rkSS0Mz67WR7iV0nTFRTec4JJS7ivDzMmwGOwPFzrTP7L9PfQVqEmxdOTbDNGl1MAkeCdLFKPtExcAZVNXcDb9Q0U2oAcmfREtJErF6dpewT%2BVyb6wity8321WhwL9La%2FiiAH5q9r5tOyiekPpgcU%2FfcJi8rIkyMqCv0ZSSRO5Htt6KJTtNJBiI%2BK3zkXPd3d7JSRW2SlPGEXYFVPnnSLR8JMiXWGt9nJTlvMhyWNqYTJqPi1aFhscXbK5kjtLcabpkrKJ%2BSbTY3%2B74DEa0LLIXfD0hvyBs%2Fhw7823GtfKWeBM4ooXcLZTGbwUu9i3RHw3yNyTvKagDxofc8iiPgHFkH2zDNg6ycejh6zcpK6qvZfF0pRybQg1uQ8csIIpvlgRAEJ895z00YAiXfGewpJloc8p3kKTXCoY0ha9UnLNZtasTF1rn4giCBSvJ%2BgnQrifEFi7bsPe9xhG7CZPHxmFcceW7kovGqoN0rcIPpzueA%2B9GIwZTp1qroNHme3PsZRvkXKx1NJbaQrO8eZz7GWZ3dzTvsxxDavZteMAx3A1hsc1QUFgS2AD1ycEgi%2BvmWMw5YWdvQY6pgH16kkgVbYNSH6Pu5%2Bl2LrRntRTzmg%2BX4DajcILknEoYXgNiIP49t1wYtk3lg2GVHvGzyHbMdkA%2BJiSqIzmR0HAtaIDYjeBEdr6qS7z1toj2Wtx9wX8yUBaJvsdR%2FxMSGvMGoluMpUqimDmLY1VpxEO80SJVGj28ZmRycYpkpzr98mKGH5cgOj2JH09HfSWQXIp3VMW9vv1b3KGxAAbycnxkBkDYf2c&X-Amz-Signature=287751cc599f50aa1cd8ada3cf1231f03f63d7cf2cbd89978e921b27b1c0bf2d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWOWCRQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBXqqaSFauC%2B54yOdJ51q%2FnjiKato9M8uf9%2FIb12XWfeAiAOW0B%2Bszn%2FA7eV%2FJkC1Jj%2FI00aoaKtQEe9fDva7yvoGSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8JqqO3OfEJuyS66nKtwDfflq3CF5ln6ZFZcQcmc%2FAGq5tKtAJ6cBQYMkMGos7Kb7hZKYnv26StTBo9rkSS0Mz67WR7iV0nTFRTec4JJS7ivDzMmwGOwPFzrTP7L9PfQVqEmxdOTbDNGl1MAkeCdLFKPtExcAZVNXcDb9Q0U2oAcmfREtJErF6dpewT%2BVyb6wity8321WhwL9La%2FiiAH5q9r5tOyiekPpgcU%2FfcJi8rIkyMqCv0ZSSRO5Htt6KJTtNJBiI%2BK3zkXPd3d7JSRW2SlPGEXYFVPnnSLR8JMiXWGt9nJTlvMhyWNqYTJqPi1aFhscXbK5kjtLcabpkrKJ%2BSbTY3%2B74DEa0LLIXfD0hvyBs%2Fhw7823GtfKWeBM4ooXcLZTGbwUu9i3RHw3yNyTvKagDxofc8iiPgHFkH2zDNg6ycejh6zcpK6qvZfF0pRybQg1uQ8csIIpvlgRAEJ895z00YAiXfGewpJloc8p3kKTXCoY0ha9UnLNZtasTF1rn4giCBSvJ%2BgnQrifEFi7bsPe9xhG7CZPHxmFcceW7kovGqoN0rcIPpzueA%2B9GIwZTp1qroNHme3PsZRvkXKx1NJbaQrO8eZz7GWZ3dzTvsxxDavZteMAx3A1hsc1QUFgS2AD1ycEgi%2BvmWMw5YWdvQY6pgH16kkgVbYNSH6Pu5%2Bl2LrRntRTzmg%2BX4DajcILknEoYXgNiIP49t1wYtk3lg2GVHvGzyHbMdkA%2BJiSqIzmR0HAtaIDYjeBEdr6qS7z1toj2Wtx9wX8yUBaJvsdR%2FxMSGvMGoluMpUqimDmLY1VpxEO80SJVGj28ZmRycYpkpzr98mKGH5cgOj2JH09HfSWQXIp3VMW9vv1b3KGxAAbycnxkBkDYf2c&X-Amz-Signature=55a8f2642de2cb92cb85a83faa7e4dd68e733338bd8e5bc5e08193a13b7c9519&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWOWCRQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBXqqaSFauC%2B54yOdJ51q%2FnjiKato9M8uf9%2FIb12XWfeAiAOW0B%2Bszn%2FA7eV%2FJkC1Jj%2FI00aoaKtQEe9fDva7yvoGSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8JqqO3OfEJuyS66nKtwDfflq3CF5ln6ZFZcQcmc%2FAGq5tKtAJ6cBQYMkMGos7Kb7hZKYnv26StTBo9rkSS0Mz67WR7iV0nTFRTec4JJS7ivDzMmwGOwPFzrTP7L9PfQVqEmxdOTbDNGl1MAkeCdLFKPtExcAZVNXcDb9Q0U2oAcmfREtJErF6dpewT%2BVyb6wity8321WhwL9La%2FiiAH5q9r5tOyiekPpgcU%2FfcJi8rIkyMqCv0ZSSRO5Htt6KJTtNJBiI%2BK3zkXPd3d7JSRW2SlPGEXYFVPnnSLR8JMiXWGt9nJTlvMhyWNqYTJqPi1aFhscXbK5kjtLcabpkrKJ%2BSbTY3%2B74DEa0LLIXfD0hvyBs%2Fhw7823GtfKWeBM4ooXcLZTGbwUu9i3RHw3yNyTvKagDxofc8iiPgHFkH2zDNg6ycejh6zcpK6qvZfF0pRybQg1uQ8csIIpvlgRAEJ895z00YAiXfGewpJloc8p3kKTXCoY0ha9UnLNZtasTF1rn4giCBSvJ%2BgnQrifEFi7bsPe9xhG7CZPHxmFcceW7kovGqoN0rcIPpzueA%2B9GIwZTp1qroNHme3PsZRvkXKx1NJbaQrO8eZz7GWZ3dzTvsxxDavZteMAx3A1hsc1QUFgS2AD1ycEgi%2BvmWMw5YWdvQY6pgH16kkgVbYNSH6Pu5%2Bl2LrRntRTzmg%2BX4DajcILknEoYXgNiIP49t1wYtk3lg2GVHvGzyHbMdkA%2BJiSqIzmR0HAtaIDYjeBEdr6qS7z1toj2Wtx9wX8yUBaJvsdR%2FxMSGvMGoluMpUqimDmLY1VpxEO80SJVGj28ZmRycYpkpzr98mKGH5cgOj2JH09HfSWQXIp3VMW9vv1b3KGxAAbycnxkBkDYf2c&X-Amz-Signature=eca132afe41573d4d62754a64f31f069458666cca46adaf80106b210d6019f0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWOWCRQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBXqqaSFauC%2B54yOdJ51q%2FnjiKato9M8uf9%2FIb12XWfeAiAOW0B%2Bszn%2FA7eV%2FJkC1Jj%2FI00aoaKtQEe9fDva7yvoGSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8JqqO3OfEJuyS66nKtwDfflq3CF5ln6ZFZcQcmc%2FAGq5tKtAJ6cBQYMkMGos7Kb7hZKYnv26StTBo9rkSS0Mz67WR7iV0nTFRTec4JJS7ivDzMmwGOwPFzrTP7L9PfQVqEmxdOTbDNGl1MAkeCdLFKPtExcAZVNXcDb9Q0U2oAcmfREtJErF6dpewT%2BVyb6wity8321WhwL9La%2FiiAH5q9r5tOyiekPpgcU%2FfcJi8rIkyMqCv0ZSSRO5Htt6KJTtNJBiI%2BK3zkXPd3d7JSRW2SlPGEXYFVPnnSLR8JMiXWGt9nJTlvMhyWNqYTJqPi1aFhscXbK5kjtLcabpkrKJ%2BSbTY3%2B74DEa0LLIXfD0hvyBs%2Fhw7823GtfKWeBM4ooXcLZTGbwUu9i3RHw3yNyTvKagDxofc8iiPgHFkH2zDNg6ycejh6zcpK6qvZfF0pRybQg1uQ8csIIpvlgRAEJ895z00YAiXfGewpJloc8p3kKTXCoY0ha9UnLNZtasTF1rn4giCBSvJ%2BgnQrifEFi7bsPe9xhG7CZPHxmFcceW7kovGqoN0rcIPpzueA%2B9GIwZTp1qroNHme3PsZRvkXKx1NJbaQrO8eZz7GWZ3dzTvsxxDavZteMAx3A1hsc1QUFgS2AD1ycEgi%2BvmWMw5YWdvQY6pgH16kkgVbYNSH6Pu5%2Bl2LrRntRTzmg%2BX4DajcILknEoYXgNiIP49t1wYtk3lg2GVHvGzyHbMdkA%2BJiSqIzmR0HAtaIDYjeBEdr6qS7z1toj2Wtx9wX8yUBaJvsdR%2FxMSGvMGoluMpUqimDmLY1VpxEO80SJVGj28ZmRycYpkpzr98mKGH5cgOj2JH09HfSWQXIp3VMW9vv1b3KGxAAbycnxkBkDYf2c&X-Amz-Signature=2f85d377a335116f4892fd9e2a51ab2eabe2d74d828d6d900b9bbe1149157ac4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWOWCRQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBXqqaSFauC%2B54yOdJ51q%2FnjiKato9M8uf9%2FIb12XWfeAiAOW0B%2Bszn%2FA7eV%2FJkC1Jj%2FI00aoaKtQEe9fDva7yvoGSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8JqqO3OfEJuyS66nKtwDfflq3CF5ln6ZFZcQcmc%2FAGq5tKtAJ6cBQYMkMGos7Kb7hZKYnv26StTBo9rkSS0Mz67WR7iV0nTFRTec4JJS7ivDzMmwGOwPFzrTP7L9PfQVqEmxdOTbDNGl1MAkeCdLFKPtExcAZVNXcDb9Q0U2oAcmfREtJErF6dpewT%2BVyb6wity8321WhwL9La%2FiiAH5q9r5tOyiekPpgcU%2FfcJi8rIkyMqCv0ZSSRO5Htt6KJTtNJBiI%2BK3zkXPd3d7JSRW2SlPGEXYFVPnnSLR8JMiXWGt9nJTlvMhyWNqYTJqPi1aFhscXbK5kjtLcabpkrKJ%2BSbTY3%2B74DEa0LLIXfD0hvyBs%2Fhw7823GtfKWeBM4ooXcLZTGbwUu9i3RHw3yNyTvKagDxofc8iiPgHFkH2zDNg6ycejh6zcpK6qvZfF0pRybQg1uQ8csIIpvlgRAEJ895z00YAiXfGewpJloc8p3kKTXCoY0ha9UnLNZtasTF1rn4giCBSvJ%2BgnQrifEFi7bsPe9xhG7CZPHxmFcceW7kovGqoN0rcIPpzueA%2B9GIwZTp1qroNHme3PsZRvkXKx1NJbaQrO8eZz7GWZ3dzTvsxxDavZteMAx3A1hsc1QUFgS2AD1ycEgi%2BvmWMw5YWdvQY6pgH16kkgVbYNSH6Pu5%2Bl2LrRntRTzmg%2BX4DajcILknEoYXgNiIP49t1wYtk3lg2GVHvGzyHbMdkA%2BJiSqIzmR0HAtaIDYjeBEdr6qS7z1toj2Wtx9wX8yUBaJvsdR%2FxMSGvMGoluMpUqimDmLY1VpxEO80SJVGj28ZmRycYpkpzr98mKGH5cgOj2JH09HfSWQXIp3VMW9vv1b3KGxAAbycnxkBkDYf2c&X-Amz-Signature=517db3f2540f8796952a871b4fb289c3b328b52398bec3e88c0de2471fa7a1f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWOWCRQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBXqqaSFauC%2B54yOdJ51q%2FnjiKato9M8uf9%2FIb12XWfeAiAOW0B%2Bszn%2FA7eV%2FJkC1Jj%2FI00aoaKtQEe9fDva7yvoGSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8JqqO3OfEJuyS66nKtwDfflq3CF5ln6ZFZcQcmc%2FAGq5tKtAJ6cBQYMkMGos7Kb7hZKYnv26StTBo9rkSS0Mz67WR7iV0nTFRTec4JJS7ivDzMmwGOwPFzrTP7L9PfQVqEmxdOTbDNGl1MAkeCdLFKPtExcAZVNXcDb9Q0U2oAcmfREtJErF6dpewT%2BVyb6wity8321WhwL9La%2FiiAH5q9r5tOyiekPpgcU%2FfcJi8rIkyMqCv0ZSSRO5Htt6KJTtNJBiI%2BK3zkXPd3d7JSRW2SlPGEXYFVPnnSLR8JMiXWGt9nJTlvMhyWNqYTJqPi1aFhscXbK5kjtLcabpkrKJ%2BSbTY3%2B74DEa0LLIXfD0hvyBs%2Fhw7823GtfKWeBM4ooXcLZTGbwUu9i3RHw3yNyTvKagDxofc8iiPgHFkH2zDNg6ycejh6zcpK6qvZfF0pRybQg1uQ8csIIpvlgRAEJ895z00YAiXfGewpJloc8p3kKTXCoY0ha9UnLNZtasTF1rn4giCBSvJ%2BgnQrifEFi7bsPe9xhG7CZPHxmFcceW7kovGqoN0rcIPpzueA%2B9GIwZTp1qroNHme3PsZRvkXKx1NJbaQrO8eZz7GWZ3dzTvsxxDavZteMAx3A1hsc1QUFgS2AD1ycEgi%2BvmWMw5YWdvQY6pgH16kkgVbYNSH6Pu5%2Bl2LrRntRTzmg%2BX4DajcILknEoYXgNiIP49t1wYtk3lg2GVHvGzyHbMdkA%2BJiSqIzmR0HAtaIDYjeBEdr6qS7z1toj2Wtx9wX8yUBaJvsdR%2FxMSGvMGoluMpUqimDmLY1VpxEO80SJVGj28ZmRycYpkpzr98mKGH5cgOj2JH09HfSWQXIp3VMW9vv1b3KGxAAbycnxkBkDYf2c&X-Amz-Signature=24d209cda90ff8a122f68b8047b9a9faecb612454a204f9f1a51c152ede6629c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RD7VMTTL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDaVCTqFGnnsWERbyMFYpcqc6wTDz8Bgs%2Bus9wc36fHzAIhAPIJ5Mt7kWpUVovB4hmsHVUfDVdHhsGei9e0b3ALDv8BKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsECq0bVtn1jwf2hQq3AM%2F3iK39alThPy5pDxb2PqDmfpg9PusMuOEwh7ML73qzm1lESTrFWxUd0zGIeb0HHczr4soyfPLexpii4NCIt%2F7veQ5hv6VITF1TkyRaBJlln6bv3Es4XyUXCvMDDIZlUF1gwPIV3T8peQOGwyFJZLYe9byAsGU9NAkQ9EfhmNeT2C%2F9TDbL3jR9%2BUzBxiioIfG0%2FwPkxwjw8tAkaA%2Fswn9b6vIJLArDqFUQurmidrW3pMm6TtOUdcsWv4uobsLCrNQlKDAxW03ysRrNLG5CG9KXpr3FpxMjXrvEzStRL9argEd02bEfiY6QupfdMr4WGzQHQFWF3GLdVSSSk3mbtgflKCwqWrB1Di1Ns2trjXG0TX8z%2B6c6j2LxYIALQxiu28jhIJ4dhP%2FgXgMXRyXYSAe7EQRAvMG3FaaFqTVPNRwrFEXrviP%2BFkbGoJDgmo9WMgB2YH%2Fnb%2FpVn%2BDqOdYi88o3fHJXAxJ%2FEjytDwgpAgEQltNeE8AjSfrp0kIXBpKCyIXGYS3qIAO0LXBjXlDFdCNcVvmYK6YZqyLwPgfixUaUeyPvNmrpamMExVsNWLov3zs03be2xJFkpqz1SLJn3kjlKvRPZzN9wdboI6lCvfdbwOmT8DYNF9Trx5XcDD9hJ29BjqkAZVsxRIH1s8xdQRLJYHALvQ7rvmKy91kt%2Fr7v1iBmuNMF1wNxQZOR3MUy0txFW8eVHHlj%2FfsKOMzVm8SQWlMfhIZkA6ZWm1gvQ5OoMsvJGUatHpXmyO%2FnvBxnx1xp8kpWEEN%2BU05%2Fg39dUwbnoshnWVjaWkuObNeEk4pgdzL9JlusmEaIYgu0eC4MD6fb3zPh%2FFNcyRd6ds8%2BkTK8fIVMM93Ipr9&X-Amz-Signature=ae389ce842784d72f3ad90a6b447fae407b729b6419b37a896edacb9807f8ccb&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZW4MS5J%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIC5L%2Bplef%2FObl0XH9CUUqrKXpf%2B3M%2Fi9hpX%2FixPesMKEAiEAxU9NyhoiNiXjNfmCEyCmMryCjqfTkv%2BcGuF6RuyjAF0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIJCSvypOSG0aKcuoCrcAz4CYObJlph%2FUDSEPPsbHN8BgihP8d4np7uzMuBVmU6P2T8yPo5uFH7lEpbuJS4nMnkj75HAh9ceRprcACrALfGtbgd1r4v1zehYc%2FAXq5kw96On2cSXGBH%2Bt3mN9tqHlhZue3l67sxrjbIoyjytsxjI6lFqZVwrVhDhQej0ReSWkoH7T3es4Kgxv%2Bd7L%2BTUZeRhvYNNolVU9VLEHZ%2FHzeh8i5upLlwg7DINPKu6auAx3tvC%2BfCA%2BCDaqNE%2Fw8EWcS12osABNA41WN6ctjzE1NyyPQpTz4vPrrpKQcqAMUu4fp8zB80h6VMWdn6My3kzsVp3tGXK6MAxH2rq8X7YPmP1Od5EN%2FpIPWULKf0Y9tzo9r6ceP73WUI2SJWdcduolHBifW023ha7TwXP7waOslihecGaGCukyeYh9KXi%2BBrPpEDOrfiv1jBibLJB0HSoWwo%2BNAY45BnIWQib2YRmdGrZZHKFmSZD3WnbROTTtVFnEC4ywQ0hX6qwBw22DR3CZPKpDC%2BzFftoGEbvNdNU%2FzTNxjibVsW3D1KWQ11Z5pkp6VHqdxWbtak2ok3f03Tftnblkql6vUx184Qy3Y5qRIhiOJYJxGumg1dN7spMBrAZbbutrxJIsz6%2FIIl6MPyEnb0GOqUBu2iP%2BThqf9hCKVDtJSptNik3ZD4Qc%2FZnYwpyxr8JWTHcd07j9YnvR1eY1lbeP0DCMgkTglhi3C5GdAmGlY4cOskM9F8j68eb4zS%2FHGtN9VOaIdoVuTiRczjCzQRvp5djrPXsNDfmTS4sabYhngNNg2Kt2lmMBBLnWmuGdHP%2F6P7IGr%2BFqji0%2FIGK6l08nh2DK%2BTrjRkl3vCNSDYeM218EcvlIdlp&X-Amz-Signature=d6fb6a35cf256939acf8c527045f1f147e3a98180aa4f90c0ccd2043efff35c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWOWCRQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBXqqaSFauC%2B54yOdJ51q%2FnjiKato9M8uf9%2FIb12XWfeAiAOW0B%2Bszn%2FA7eV%2FJkC1Jj%2FI00aoaKtQEe9fDva7yvoGSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8JqqO3OfEJuyS66nKtwDfflq3CF5ln6ZFZcQcmc%2FAGq5tKtAJ6cBQYMkMGos7Kb7hZKYnv26StTBo9rkSS0Mz67WR7iV0nTFRTec4JJS7ivDzMmwGOwPFzrTP7L9PfQVqEmxdOTbDNGl1MAkeCdLFKPtExcAZVNXcDb9Q0U2oAcmfREtJErF6dpewT%2BVyb6wity8321WhwL9La%2FiiAH5q9r5tOyiekPpgcU%2FfcJi8rIkyMqCv0ZSSRO5Htt6KJTtNJBiI%2BK3zkXPd3d7JSRW2SlPGEXYFVPnnSLR8JMiXWGt9nJTlvMhyWNqYTJqPi1aFhscXbK5kjtLcabpkrKJ%2BSbTY3%2B74DEa0LLIXfD0hvyBs%2Fhw7823GtfKWeBM4ooXcLZTGbwUu9i3RHw3yNyTvKagDxofc8iiPgHFkH2zDNg6ycejh6zcpK6qvZfF0pRybQg1uQ8csIIpvlgRAEJ895z00YAiXfGewpJloc8p3kKTXCoY0ha9UnLNZtasTF1rn4giCBSvJ%2BgnQrifEFi7bsPe9xhG7CZPHxmFcceW7kovGqoN0rcIPpzueA%2B9GIwZTp1qroNHme3PsZRvkXKx1NJbaQrO8eZz7GWZ3dzTvsxxDavZteMAx3A1hsc1QUFgS2AD1ycEgi%2BvmWMw5YWdvQY6pgH16kkgVbYNSH6Pu5%2Bl2LrRntRTzmg%2BX4DajcILknEoYXgNiIP49t1wYtk3lg2GVHvGzyHbMdkA%2BJiSqIzmR0HAtaIDYjeBEdr6qS7z1toj2Wtx9wX8yUBaJvsdR%2FxMSGvMGoluMpUqimDmLY1VpxEO80SJVGj28ZmRycYpkpzr98mKGH5cgOj2JH09HfSWQXIp3VMW9vv1b3KGxAAbycnxkBkDYf2c&X-Amz-Signature=d9dca7213e7438594e2e621971922e7740023a7a07fb7f7c8cdd4a53cd8a3987&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWOWCRQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBXqqaSFauC%2B54yOdJ51q%2FnjiKato9M8uf9%2FIb12XWfeAiAOW0B%2Bszn%2FA7eV%2FJkC1Jj%2FI00aoaKtQEe9fDva7yvoGSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8JqqO3OfEJuyS66nKtwDfflq3CF5ln6ZFZcQcmc%2FAGq5tKtAJ6cBQYMkMGos7Kb7hZKYnv26StTBo9rkSS0Mz67WR7iV0nTFRTec4JJS7ivDzMmwGOwPFzrTP7L9PfQVqEmxdOTbDNGl1MAkeCdLFKPtExcAZVNXcDb9Q0U2oAcmfREtJErF6dpewT%2BVyb6wity8321WhwL9La%2FiiAH5q9r5tOyiekPpgcU%2FfcJi8rIkyMqCv0ZSSRO5Htt6KJTtNJBiI%2BK3zkXPd3d7JSRW2SlPGEXYFVPnnSLR8JMiXWGt9nJTlvMhyWNqYTJqPi1aFhscXbK5kjtLcabpkrKJ%2BSbTY3%2B74DEa0LLIXfD0hvyBs%2Fhw7823GtfKWeBM4ooXcLZTGbwUu9i3RHw3yNyTvKagDxofc8iiPgHFkH2zDNg6ycejh6zcpK6qvZfF0pRybQg1uQ8csIIpvlgRAEJ895z00YAiXfGewpJloc8p3kKTXCoY0ha9UnLNZtasTF1rn4giCBSvJ%2BgnQrifEFi7bsPe9xhG7CZPHxmFcceW7kovGqoN0rcIPpzueA%2B9GIwZTp1qroNHme3PsZRvkXKx1NJbaQrO8eZz7GWZ3dzTvsxxDavZteMAx3A1hsc1QUFgS2AD1ycEgi%2BvmWMw5YWdvQY6pgH16kkgVbYNSH6Pu5%2Bl2LrRntRTzmg%2BX4DajcILknEoYXgNiIP49t1wYtk3lg2GVHvGzyHbMdkA%2BJiSqIzmR0HAtaIDYjeBEdr6qS7z1toj2Wtx9wX8yUBaJvsdR%2FxMSGvMGoluMpUqimDmLY1VpxEO80SJVGj28ZmRycYpkpzr98mKGH5cgOj2JH09HfSWQXIp3VMW9vv1b3KGxAAbycnxkBkDYf2c&X-Amz-Signature=fc20739082f59b5ca8d8d6675a878926cef2c5a89c0a6763edd6ce2f334bf52a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWOWCRQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBXqqaSFauC%2B54yOdJ51q%2FnjiKato9M8uf9%2FIb12XWfeAiAOW0B%2Bszn%2FA7eV%2FJkC1Jj%2FI00aoaKtQEe9fDva7yvoGSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8JqqO3OfEJuyS66nKtwDfflq3CF5ln6ZFZcQcmc%2FAGq5tKtAJ6cBQYMkMGos7Kb7hZKYnv26StTBo9rkSS0Mz67WR7iV0nTFRTec4JJS7ivDzMmwGOwPFzrTP7L9PfQVqEmxdOTbDNGl1MAkeCdLFKPtExcAZVNXcDb9Q0U2oAcmfREtJErF6dpewT%2BVyb6wity8321WhwL9La%2FiiAH5q9r5tOyiekPpgcU%2FfcJi8rIkyMqCv0ZSSRO5Htt6KJTtNJBiI%2BK3zkXPd3d7JSRW2SlPGEXYFVPnnSLR8JMiXWGt9nJTlvMhyWNqYTJqPi1aFhscXbK5kjtLcabpkrKJ%2BSbTY3%2B74DEa0LLIXfD0hvyBs%2Fhw7823GtfKWeBM4ooXcLZTGbwUu9i3RHw3yNyTvKagDxofc8iiPgHFkH2zDNg6ycejh6zcpK6qvZfF0pRybQg1uQ8csIIpvlgRAEJ895z00YAiXfGewpJloc8p3kKTXCoY0ha9UnLNZtasTF1rn4giCBSvJ%2BgnQrifEFi7bsPe9xhG7CZPHxmFcceW7kovGqoN0rcIPpzueA%2B9GIwZTp1qroNHme3PsZRvkXKx1NJbaQrO8eZz7GWZ3dzTvsxxDavZteMAx3A1hsc1QUFgS2AD1ycEgi%2BvmWMw5YWdvQY6pgH16kkgVbYNSH6Pu5%2Bl2LrRntRTzmg%2BX4DajcILknEoYXgNiIP49t1wYtk3lg2GVHvGzyHbMdkA%2BJiSqIzmR0HAtaIDYjeBEdr6qS7z1toj2Wtx9wX8yUBaJvsdR%2FxMSGvMGoluMpUqimDmLY1VpxEO80SJVGj28ZmRycYpkpzr98mKGH5cgOj2JH09HfSWQXIp3VMW9vv1b3KGxAAbycnxkBkDYf2c&X-Amz-Signature=44037211c258e45b0298cb4cce528bd34e17691530e03ee4fb1320f95d593053&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NG7EZJ6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIBZZRjfaRlrs6JFH2Cxp8rL2cc3jpN5qZhH%2Fa07oI1BgAiEA4gsWf6vChYn1IDs7LHNzAFzp%2BhzzfckNvZ3UCbxO5dkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNzGsvSFlaNTlDfFkircA7s9nAjlOH1iNkdE%2FNAB0CG%2F%2BZnPhFUIKkot6yJKUnftoNG2cOEGN97IrbhjrsuhhRNSEOEvXA4xiRuOS8DaHRWPwxOYbrFnR3mky9xt7%2BaShdHlbeEjMMihdAYZ8HBrj9%2BOOmWDNVb5La7htIG8NW3uEixdwvyOCCYFDljDqkCpQqM7%2BK01BZJg1awKErWdncaQvMxDrVOeL7iyvplMk9FWVZ%2FPlSEQJP8dbq33MNXP2J%2BNku4I9OplT9e0uKGVu6uQa2y0uLlRaCA7uuw8yERwOuRIYrBM9XgdGZaAIrgWUG1SZdftnX4EE8XlNrY%2Bbd7%2FUbdLXunOtHrAZ8XNaoYgiuPByqwx%2Bh0A7v6V2dYc86yt7NM%2FLHGav2Kq0YL69weOncoeG8%2B0TmL%2BzfEuoVz8h7BuLu7TJjPVlLjhs%2FZhjbSjCaUAAyfHvIjtHrXY5udNOwsvQwRl25DEktbTaHOhI1VdeV5A8vUhGbn2yxF4y0WuXRM6Vgn3aOuYsmvzvqo2WUc6wUXFWd877R9jS2pg888oCsLIJQqXhiywA2ohOoeAf0GIO1UGAXYh%2FVIHN%2FMGcFpJJ%2Fffp9QSuyUNPekFPTmE5utR5UVEyVOVe7S%2B4XFp%2BCUQEyJANf%2BaMNaFnb0GOqUBi%2FRtCZUh32EHzL56c2iFW3G3W4Frbo9FqrWBIkk5ARlEU4S%2FpOm2G1%2FHsPhSwAna00MbC4yTM4zMfh%2Fs3BfRre3bJipBGHNLmTYBV%2Bzn1bVs1DFJ3tbDwptf6crZUzBbJw1smXYmA2h9VH7zpTGXIfmxscrdKGz%2BXRZFymRHRaVB9cm9juq4ilUQdEHny5Z6oVbckBLzZksAYVpsLWDT6B%2FtBCTR&X-Amz-Signature=9593696549f3c994c5d35ebc1c7524e97054878204e244af2bf4d873e2066315&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBHUIH5M%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDyrD0gMeIP7rqkoF4lt%2B4wtEPhpXRaFN8DEEAsb9nRwwIhANF9hEQL9c55J5T14LghujVzoiqPsDvkOI07QY5npebhKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsGM6EF3vebRQ1Nv4q3AOpdBMyPO%2FsjvKNUqY9QN4Ao7COaX7ge1Llai5Bo6p%2BTEIUDI6hQu1OGphGsPZysIG9E00CdvsKl2wb6ZNv3I%2B796OFkrALVqNh5gl5RA74tw7bcbyeWYxUxMXeDiSerktPFqkvB3%2FCEuZmmi4wV3LxF7q1WQw2s882I6LhP5fOV7lLBV174l7qnz%2FVwFp3twxKnv4wufE3mdOzDef4oz4DrcyGXiXkV6q96IwYkO5NFz0mY6X9Mu6%2BPO4QsKeUkVsANiL%2FEESYhNwYuEhax5rQ3RhtvqjMo%2FImp6fCRcQGDqnoExreE8cj1%2Bwiee8ApDkBxxNb4umputhVvfveI9QaXbBHTn%2BWp68tawnFGO%2F3tNl%2FLXvHzE%2FcYnBuCo3QQBC4TOMwasGO1D3svJXTuqOgSGux3hxpHHPVAsuV3E7JUBi9i2MHnsnS2hhX0ps48IAK%2Bp1m6JfvO3ZdMWXKUqdEwv2zjaegN1h6tf0waNevdMtpf19hKz50OcTm3yLwwdc6YbVGOKpvsjxU2DKH1X0vmRD%2BrCrGp8p7xzMmq1eVwOECcugR4Jayjk0j6gSx8CbT3zUSftLyaMVT8ofRcwIjEK%2FW%2B9bf47w8d660%2B5vKTjTxHyWy%2B41AlFICTDD9hJ29BjqkATFhvaSAJyVquXItRhN0%2B305ExAr%2BboXQntCy2yd%2BJlKivKdEig%2BW3LSA4Up0%2BT11fAKpWghpvL4%2FN%2FREWpN6ffm6UGpjeq5ln%2F8bOVJ%2Fyz1jxW%2FFV5Rs2i3IYFew6YcWXXL%2FZ66sJaxmMtMwg6XwfMhmC1ob5SVBgifWL6YXrpFRnljIaT1f%2FGrRBAs%2Bi0GfKEGmsEAGUrL4k%2Fh70k6F9WYd0QL&X-Amz-Signature=5a4346bc383ae84497458464ce9eb95b5ea8c3cc86a03447d65dd3709155b6bd&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666A6JG22S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDxx1Tnu%2FS3iEqH2%2FfC6uZhrPyrRnVc9VYVQ8MBtqpj7QIhANetkHyROBxKw02ItfdwEWEDZVOpxiMJn%2FlJ9BrLmRryKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2p4Bsk9mrsu73DjUq3AM2pw75Jw%2Bri4US8Ght1zELrpnSv%2Bw6KiF35s4Y%2FpfWpBhKJkhoP1SvfeFK%2FSTPFKVF94lghnJLu5njnOqI%2FMTiTUbFyBK41JBIoNUrlzL3kYOK15QI%2BALVaqxlAih7e3pRlxvnMYra4M9rnyaMaSzM8Ml6Msk9iBYLk5ik85bCm2mGOtlg3zu2VwSrbaNsPBRRK2c7RfpbFR2fYLnKae71Q8Lu%2FTJXt2oFe2wh0PzJPhGbABnBnAVNqkqbN3hHQqk5O7NT%2F4X%2BEGT4aR7dQYsWXysbIUrKet4gSyeUZvtgYkoDvE8YE9SNnE7wF6LBEWNDOb%2FT%2FQ4Cecx1mAb4d471bKVlZHCPfVmp%2BxU%2FPN49DivW865I9rS9V%2BXgSmwPf7DNWjZGQdbtau2LnG7GPO0sv9hC5pco8eG%2F%2FOXKmIhg0w%2FggmJYMRgObvpHjXMCtaqSWLq3rIwvUYQhmVO7g2sAlBkjIajUJuKjOac31SDBXWpGiBZuI9rODP%2F704xF86SIaohTFoevjsxz%2FrEMBK2Zdry1Cf8zQFmiBgXQFVCgR2CDXDS%2BgdZgR1aK8eqMGX3JIB5%2F6meD7%2Bhic7XTnJBNVxChsfFdKJy95mqN59WCQ1YpG06dJORmtNab5TCKhp29BjqkAZCrp%2FoTIUdIS3B%2FaVh7l3%2Bfn0Kj32W273C8gvOahSUT1ThUgsBYJn7o3nEku5d%2B1BqgunH4Bo8y92vbL4zsuV1QYlBOZUnxpCb%2BRvvqgrCCBz%2FXA7Ly9fV2B9mRFXq38ITWxYT5orzI1uYZDvkoMpGhOSAACvrK14J0XK5%2FRGHGwZ2hS%2FKm1qzJr0mfS2%2FXXpN9nWVJzLgPg9dGbNNdmxiHt%2FYp&X-Amz-Signature=8349f34904628aa02fe5843c89d531479028ff76cc88fb083c78e4a08f50d8ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV7YAGOY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIAWz8LdCQk7dodyO1oqNe9VaLDbZ8GqLX3mfmMDZHFDPAiAVtSekKDAbVUUK8SrYihxetZK4hcN9e6bmLEftUTA8yyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGWfWG8XnQItY6blhKtwDVwLFbvC4sECR8QGUW3XW3%2B7BLQKmjYDt86rQYAnf4mYot8OZmgzidnpInHxDR%2BoHIW8WVmI3R4S%2BCprHK1rcTmc4CpqYv0MFfMfobonrHtPP4WLLLi6C%2BHiLgHgoYuShX4KKhZ9rCyxwh4kxau7kJX%2BCT7IgDokQ5OSUt9NMpD4YnwLTVvZChgpIX13b7%2B%2FCgKdRwgL%2FIaKi8I7BPXEE78Y1c%2B5UCPdNCh%2FvARUjORU1ciT%2BMI%2F89ab%2Fh8J%2FgQegbGv8LGpQecrRGRDNxu9H2bzXRO%2Bgz2KsK37NxWikgpyqa%2BQybnNsz4%2BvG10zO02EK%2FG6rTzS74dfEmW%2BO24F40unprAt3joAavoG2rIp%2BvLjzymjKa7eqtXuLfvHQQTmGsde84quJ%2BQafH8vFB0QkBYnJwrq%2BGevYoSg3wpLlDVuZWOukpEeCbjQkZ3Sriq6UsmYX547S6xm3GE6MP1E6ap3VIorZp7C9gW5%2FqDwPfDPgAg0KF6cKRC67AAnBVtzcmK88FMSuGtDCWwGSgZoCirY9DSvDMqq3igUvsb%2FzZe7XHyd6H2cgqx0wh6gI264x0Nfv1pxD%2FwN%2BiLM%2B8oZMuQRT9%2FMEcEms%2FECRkNIVvXUArVt%2BQSJ0ZAO0sww1IWdvQY6pgFZQoAF76q4YbqFRWW0mpVgBbQ81EIWuBmOJ74BRtGgIeLvMvRJOZlmfwUmEMgf5xhoI2c6%2F3nj4M1bay0izZN3Ic9j0bMEuHM6nQFOE%2BL7UPGq%2Fk6y0k73kgIS4ETsZOPtVXaNu04D13BvFiHaOqFYDyobPdWTkAST%2FdyeyjNAYfAXpIIhPsXKjHAcQ7DwH5bqpvvfiP9HgYqKTsjfkzI3WUn%2FXnkO&X-Amz-Signature=e02c54845325b3951acfe0b1989451bed5e327386d12722d7759f2cef1a561d6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV7YAGOY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIAWz8LdCQk7dodyO1oqNe9VaLDbZ8GqLX3mfmMDZHFDPAiAVtSekKDAbVUUK8SrYihxetZK4hcN9e6bmLEftUTA8yyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGWfWG8XnQItY6blhKtwDVwLFbvC4sECR8QGUW3XW3%2B7BLQKmjYDt86rQYAnf4mYot8OZmgzidnpInHxDR%2BoHIW8WVmI3R4S%2BCprHK1rcTmc4CpqYv0MFfMfobonrHtPP4WLLLi6C%2BHiLgHgoYuShX4KKhZ9rCyxwh4kxau7kJX%2BCT7IgDokQ5OSUt9NMpD4YnwLTVvZChgpIX13b7%2B%2FCgKdRwgL%2FIaKi8I7BPXEE78Y1c%2B5UCPdNCh%2FvARUjORU1ciT%2BMI%2F89ab%2Fh8J%2FgQegbGv8LGpQecrRGRDNxu9H2bzXRO%2Bgz2KsK37NxWikgpyqa%2BQybnNsz4%2BvG10zO02EK%2FG6rTzS74dfEmW%2BO24F40unprAt3joAavoG2rIp%2BvLjzymjKa7eqtXuLfvHQQTmGsde84quJ%2BQafH8vFB0QkBYnJwrq%2BGevYoSg3wpLlDVuZWOukpEeCbjQkZ3Sriq6UsmYX547S6xm3GE6MP1E6ap3VIorZp7C9gW5%2FqDwPfDPgAg0KF6cKRC67AAnBVtzcmK88FMSuGtDCWwGSgZoCirY9DSvDMqq3igUvsb%2FzZe7XHyd6H2cgqx0wh6gI264x0Nfv1pxD%2FwN%2BiLM%2B8oZMuQRT9%2FMEcEms%2FECRkNIVvXUArVt%2BQSJ0ZAO0sww1IWdvQY6pgFZQoAF76q4YbqFRWW0mpVgBbQ81EIWuBmOJ74BRtGgIeLvMvRJOZlmfwUmEMgf5xhoI2c6%2F3nj4M1bay0izZN3Ic9j0bMEuHM6nQFOE%2BL7UPGq%2Fk6y0k73kgIS4ETsZOPtVXaNu04D13BvFiHaOqFYDyobPdWTkAST%2FdyeyjNAYfAXpIIhPsXKjHAcQ7DwH5bqpvvfiP9HgYqKTsjfkzI3WUn%2FXnkO&X-Amz-Signature=5c5eacad7c5167d42f45b9538abb5967a365f6453fa8a8df3b24e6641190b813&X-Amz-SignedHeaders=host&x-id=GetObject)

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
