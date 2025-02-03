

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DI6CNEO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHvENjcg8QML9Jwje8ZjJLrnsk89BwfEsRbr96Fojbl3AiBD2cYeg63qPxLudd9suHDJD4AD1qhf%2FCEcey%2FzTnA0Wir%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMbSS55E6%2BP1CqjE9mKtwDdYN3dbyhKEJbTCLqGU5DtOklM9FI2tYVebBP2bhtXxgzHcugifhDoFtbnH5KHp4tPIETe%2Fp7Y1%2BXsWh2oiHT%2FRhC%2BJSdqV0%2FfNL0aug9T4qbgFp4VNv2%2FPvM7G7zmeCqSpBhn%2BvqB8O8B35QxYX1qealtAie6kNgvuzoio9ohmo%2BXFm9SdjdaXRXcgAiv9BROAPWobLqfVCRFq9pSED3FmCJ3oKcvutQDDf%2B6rXYPEOL%2BKk%2FFXRPFzks8Jg9lmAQHz5ZB%2FRXW5%2BKKpqahKGWh%2Bf3SkpvARzLBtbNvNrKIRjQAS%2FKNcTFEBnuz0Ace4eXA2bM7c7laquuexXMLW8TyFbyuKQ5tYW0Hs%2FoLPwdeC1PSTfSmqvRMt3ZO%2BaM1kKX2deNIWKgG1U0B5FJG3loDczGisGlq093Px%2FkcK0QNNcqEuDVzHsTWsFVmS8YaO4Da%2B6uAi3JKbLE5hhD0To5vrrERNeljzrj%2BINLSDleu93PRV97lxogwJs5UPobLr5Bf8opV%2FVzf04RPIzVg57POsyzsA7db7F07gzjPXR0Jnh%2Bh5uJ9S6msOcdkLpjUykOmqnT0BN3gPNhscOisj9paTv%2BqKz9U7Z9F%2FyDf8zZaVjJ0T7v2KKzafV%2FlZ0w7o2DvQY6pgFIbJTZebAnDUJ73IHSyI4CSxHeX76EC3j92cmg1FLwv4Al2w6UMkYjpjO2IOBIfokEOfIfv1aekU2kvebMddMt3Y0qYNZq7dIQSfA7s9coe59JJ7q8h4L6LnFYQavbISDiGI1VI4XlQkFE8TGZhVZMfsBAXK5xcuXsCy9XCBYbmmjom9LCU0aTE3DQGNnYI2qehDeihYMYbTzL%2F0vSwnXu9ESzG%2FWI&X-Amz-Signature=0380d569ab2d43fb66a38b7d9016380ad11de462a1091a7586dfe6412c478642&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DI6CNEO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHvENjcg8QML9Jwje8ZjJLrnsk89BwfEsRbr96Fojbl3AiBD2cYeg63qPxLudd9suHDJD4AD1qhf%2FCEcey%2FzTnA0Wir%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMbSS55E6%2BP1CqjE9mKtwDdYN3dbyhKEJbTCLqGU5DtOklM9FI2tYVebBP2bhtXxgzHcugifhDoFtbnH5KHp4tPIETe%2Fp7Y1%2BXsWh2oiHT%2FRhC%2BJSdqV0%2FfNL0aug9T4qbgFp4VNv2%2FPvM7G7zmeCqSpBhn%2BvqB8O8B35QxYX1qealtAie6kNgvuzoio9ohmo%2BXFm9SdjdaXRXcgAiv9BROAPWobLqfVCRFq9pSED3FmCJ3oKcvutQDDf%2B6rXYPEOL%2BKk%2FFXRPFzks8Jg9lmAQHz5ZB%2FRXW5%2BKKpqahKGWh%2Bf3SkpvARzLBtbNvNrKIRjQAS%2FKNcTFEBnuz0Ace4eXA2bM7c7laquuexXMLW8TyFbyuKQ5tYW0Hs%2FoLPwdeC1PSTfSmqvRMt3ZO%2BaM1kKX2deNIWKgG1U0B5FJG3loDczGisGlq093Px%2FkcK0QNNcqEuDVzHsTWsFVmS8YaO4Da%2B6uAi3JKbLE5hhD0To5vrrERNeljzrj%2BINLSDleu93PRV97lxogwJs5UPobLr5Bf8opV%2FVzf04RPIzVg57POsyzsA7db7F07gzjPXR0Jnh%2Bh5uJ9S6msOcdkLpjUykOmqnT0BN3gPNhscOisj9paTv%2BqKz9U7Z9F%2FyDf8zZaVjJ0T7v2KKzafV%2FlZ0w7o2DvQY6pgFIbJTZebAnDUJ73IHSyI4CSxHeX76EC3j92cmg1FLwv4Al2w6UMkYjpjO2IOBIfokEOfIfv1aekU2kvebMddMt3Y0qYNZq7dIQSfA7s9coe59JJ7q8h4L6LnFYQavbISDiGI1VI4XlQkFE8TGZhVZMfsBAXK5xcuXsCy9XCBYbmmjom9LCU0aTE3DQGNnYI2qehDeihYMYbTzL%2F0vSwnXu9ESzG%2FWI&X-Amz-Signature=217f442fd2bb9da3f2772cbbdd7f9df1315ce7345066b5ff1c57c97ef03671c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DI6CNEO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHvENjcg8QML9Jwje8ZjJLrnsk89BwfEsRbr96Fojbl3AiBD2cYeg63qPxLudd9suHDJD4AD1qhf%2FCEcey%2FzTnA0Wir%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMbSS55E6%2BP1CqjE9mKtwDdYN3dbyhKEJbTCLqGU5DtOklM9FI2tYVebBP2bhtXxgzHcugifhDoFtbnH5KHp4tPIETe%2Fp7Y1%2BXsWh2oiHT%2FRhC%2BJSdqV0%2FfNL0aug9T4qbgFp4VNv2%2FPvM7G7zmeCqSpBhn%2BvqB8O8B35QxYX1qealtAie6kNgvuzoio9ohmo%2BXFm9SdjdaXRXcgAiv9BROAPWobLqfVCRFq9pSED3FmCJ3oKcvutQDDf%2B6rXYPEOL%2BKk%2FFXRPFzks8Jg9lmAQHz5ZB%2FRXW5%2BKKpqahKGWh%2Bf3SkpvARzLBtbNvNrKIRjQAS%2FKNcTFEBnuz0Ace4eXA2bM7c7laquuexXMLW8TyFbyuKQ5tYW0Hs%2FoLPwdeC1PSTfSmqvRMt3ZO%2BaM1kKX2deNIWKgG1U0B5FJG3loDczGisGlq093Px%2FkcK0QNNcqEuDVzHsTWsFVmS8YaO4Da%2B6uAi3JKbLE5hhD0To5vrrERNeljzrj%2BINLSDleu93PRV97lxogwJs5UPobLr5Bf8opV%2FVzf04RPIzVg57POsyzsA7db7F07gzjPXR0Jnh%2Bh5uJ9S6msOcdkLpjUykOmqnT0BN3gPNhscOisj9paTv%2BqKz9U7Z9F%2FyDf8zZaVjJ0T7v2KKzafV%2FlZ0w7o2DvQY6pgFIbJTZebAnDUJ73IHSyI4CSxHeX76EC3j92cmg1FLwv4Al2w6UMkYjpjO2IOBIfokEOfIfv1aekU2kvebMddMt3Y0qYNZq7dIQSfA7s9coe59JJ7q8h4L6LnFYQavbISDiGI1VI4XlQkFE8TGZhVZMfsBAXK5xcuXsCy9XCBYbmmjom9LCU0aTE3DQGNnYI2qehDeihYMYbTzL%2F0vSwnXu9ESzG%2FWI&X-Amz-Signature=1ee3aeeb23c8767104fc3ccfeb3ee7eb0122830159f165f2fdb8d44dac6dd87b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTUCAXQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuo2tSK%2F4DLLxDxs0rR1fy49vyakHXUgt1ByQnFTDKIAiEAi55TvpZ6YvAb4m4ANiHyblmWS%2BEGuvDIFcbeX3UESKAq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBLhsg83zVSKkGhX%2BCrcA%2BkMSi%2B9SsIyNUItj7kyXtDLQHnexct%2BGOOXJXhFss1iIOk9BVduishmqr1qIMAi4gcJfsNavZhsIV8bIVGKn1KebwIO3lBFm4euw%2FOlwLB0UhJZC7%2Fb8s%2FLQT%2Buvahx25W6W0XP5XWOUWf9uTHX%2FsrW9N8h9%2F%2F3%2Bxjydn3Z%2FXzf9IVsIHzEQgHUQp%2BWuRsqHHAzhv7Q8GhqiCXEuNxT2gvvtTtsAlyihxDybXWgsUtSmrSaEyqHm6yLfCckvyKRDNFOv7WgRpwu0Zap2mJfuSeN5gvYj7rURsGEmj6Ol62TmS1j7YM7UCe9qQsVhzqhGlpmJQQ3b%2Fw6OUk7gSy8PxO49pQDLFQdSVNWSIW9YXr0F82KdSEkRoHXPI9ToX4YtY9X7xXYySopgIT0%2Fnyld9ez4lUi79WjmvAmFIY4fhcKEw9SlpGpuCmoAocB0GnxlX%2FKZfbgvDHLvZDACl4oKyLs1qINNUCnRP%2BpvFs2u2efBjnU3T0KCUpzYEvP7wMKc9FGtkKV0lfgRmMauvpl0rSGeRyjfaltNMbT6xDz%2FZmOxoJFqYuMYZw9UgQnLvkG10R%2Fuuok6iqoXOgb38DZhcSkV4h4EaMK8q6lr5GtHJz5n63c14ps%2BBOoWagXMOONg70GOqUBOMkGtHt1bhSVSltxmJjgukf4BgakrGBh1v6JmEk0S%2BFTE9dMICn4A7KY1LLTuJZ15uHu7v6rVjYgHIKQyEfiNZQ3fvUrwF%2BN3PKisYFXEiBlE2J5QnzbQ2KZDV9bnxY72vr4sBO8YvNFvMeunBQ6BDKYrNzcGbHSRBXp8Id1u07U908A0tcsdl%2FkuOU52GvPl7UHWjtzyzsJods95HcOS1ZoFVDK&X-Amz-Signature=5b2c84e4be3172f95dfb6978d7cf47fe685abf4670e76ae007822d662bf3d52d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTUCAXQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuo2tSK%2F4DLLxDxs0rR1fy49vyakHXUgt1ByQnFTDKIAiEAi55TvpZ6YvAb4m4ANiHyblmWS%2BEGuvDIFcbeX3UESKAq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBLhsg83zVSKkGhX%2BCrcA%2BkMSi%2B9SsIyNUItj7kyXtDLQHnexct%2BGOOXJXhFss1iIOk9BVduishmqr1qIMAi4gcJfsNavZhsIV8bIVGKn1KebwIO3lBFm4euw%2FOlwLB0UhJZC7%2Fb8s%2FLQT%2Buvahx25W6W0XP5XWOUWf9uTHX%2FsrW9N8h9%2F%2F3%2Bxjydn3Z%2FXzf9IVsIHzEQgHUQp%2BWuRsqHHAzhv7Q8GhqiCXEuNxT2gvvtTtsAlyihxDybXWgsUtSmrSaEyqHm6yLfCckvyKRDNFOv7WgRpwu0Zap2mJfuSeN5gvYj7rURsGEmj6Ol62TmS1j7YM7UCe9qQsVhzqhGlpmJQQ3b%2Fw6OUk7gSy8PxO49pQDLFQdSVNWSIW9YXr0F82KdSEkRoHXPI9ToX4YtY9X7xXYySopgIT0%2Fnyld9ez4lUi79WjmvAmFIY4fhcKEw9SlpGpuCmoAocB0GnxlX%2FKZfbgvDHLvZDACl4oKyLs1qINNUCnRP%2BpvFs2u2efBjnU3T0KCUpzYEvP7wMKc9FGtkKV0lfgRmMauvpl0rSGeRyjfaltNMbT6xDz%2FZmOxoJFqYuMYZw9UgQnLvkG10R%2Fuuok6iqoXOgb38DZhcSkV4h4EaMK8q6lr5GtHJz5n63c14ps%2BBOoWagXMOONg70GOqUBOMkGtHt1bhSVSltxmJjgukf4BgakrGBh1v6JmEk0S%2BFTE9dMICn4A7KY1LLTuJZ15uHu7v6rVjYgHIKQyEfiNZQ3fvUrwF%2BN3PKisYFXEiBlE2J5QnzbQ2KZDV9bnxY72vr4sBO8YvNFvMeunBQ6BDKYrNzcGbHSRBXp8Id1u07U908A0tcsdl%2FkuOU52GvPl7UHWjtzyzsJods95HcOS1ZoFVDK&X-Amz-Signature=a1422d8b71fe74c34ae92b4518539fc5baea6a4ec5697845f6e2f0d56ae711ca&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTUCAXQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuo2tSK%2F4DLLxDxs0rR1fy49vyakHXUgt1ByQnFTDKIAiEAi55TvpZ6YvAb4m4ANiHyblmWS%2BEGuvDIFcbeX3UESKAq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBLhsg83zVSKkGhX%2BCrcA%2BkMSi%2B9SsIyNUItj7kyXtDLQHnexct%2BGOOXJXhFss1iIOk9BVduishmqr1qIMAi4gcJfsNavZhsIV8bIVGKn1KebwIO3lBFm4euw%2FOlwLB0UhJZC7%2Fb8s%2FLQT%2Buvahx25W6W0XP5XWOUWf9uTHX%2FsrW9N8h9%2F%2F3%2Bxjydn3Z%2FXzf9IVsIHzEQgHUQp%2BWuRsqHHAzhv7Q8GhqiCXEuNxT2gvvtTtsAlyihxDybXWgsUtSmrSaEyqHm6yLfCckvyKRDNFOv7WgRpwu0Zap2mJfuSeN5gvYj7rURsGEmj6Ol62TmS1j7YM7UCe9qQsVhzqhGlpmJQQ3b%2Fw6OUk7gSy8PxO49pQDLFQdSVNWSIW9YXr0F82KdSEkRoHXPI9ToX4YtY9X7xXYySopgIT0%2Fnyld9ez4lUi79WjmvAmFIY4fhcKEw9SlpGpuCmoAocB0GnxlX%2FKZfbgvDHLvZDACl4oKyLs1qINNUCnRP%2BpvFs2u2efBjnU3T0KCUpzYEvP7wMKc9FGtkKV0lfgRmMauvpl0rSGeRyjfaltNMbT6xDz%2FZmOxoJFqYuMYZw9UgQnLvkG10R%2Fuuok6iqoXOgb38DZhcSkV4h4EaMK8q6lr5GtHJz5n63c14ps%2BBOoWagXMOONg70GOqUBOMkGtHt1bhSVSltxmJjgukf4BgakrGBh1v6JmEk0S%2BFTE9dMICn4A7KY1LLTuJZ15uHu7v6rVjYgHIKQyEfiNZQ3fvUrwF%2BN3PKisYFXEiBlE2J5QnzbQ2KZDV9bnxY72vr4sBO8YvNFvMeunBQ6BDKYrNzcGbHSRBXp8Id1u07U908A0tcsdl%2FkuOU52GvPl7UHWjtzyzsJods95HcOS1ZoFVDK&X-Amz-Signature=69252f6a4e9d3d3f5439772f8b3c24d0d366cba6bb030e10eb7a7049d80f9096&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTUCAXQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuo2tSK%2F4DLLxDxs0rR1fy49vyakHXUgt1ByQnFTDKIAiEAi55TvpZ6YvAb4m4ANiHyblmWS%2BEGuvDIFcbeX3UESKAq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBLhsg83zVSKkGhX%2BCrcA%2BkMSi%2B9SsIyNUItj7kyXtDLQHnexct%2BGOOXJXhFss1iIOk9BVduishmqr1qIMAi4gcJfsNavZhsIV8bIVGKn1KebwIO3lBFm4euw%2FOlwLB0UhJZC7%2Fb8s%2FLQT%2Buvahx25W6W0XP5XWOUWf9uTHX%2FsrW9N8h9%2F%2F3%2Bxjydn3Z%2FXzf9IVsIHzEQgHUQp%2BWuRsqHHAzhv7Q8GhqiCXEuNxT2gvvtTtsAlyihxDybXWgsUtSmrSaEyqHm6yLfCckvyKRDNFOv7WgRpwu0Zap2mJfuSeN5gvYj7rURsGEmj6Ol62TmS1j7YM7UCe9qQsVhzqhGlpmJQQ3b%2Fw6OUk7gSy8PxO49pQDLFQdSVNWSIW9YXr0F82KdSEkRoHXPI9ToX4YtY9X7xXYySopgIT0%2Fnyld9ez4lUi79WjmvAmFIY4fhcKEw9SlpGpuCmoAocB0GnxlX%2FKZfbgvDHLvZDACl4oKyLs1qINNUCnRP%2BpvFs2u2efBjnU3T0KCUpzYEvP7wMKc9FGtkKV0lfgRmMauvpl0rSGeRyjfaltNMbT6xDz%2FZmOxoJFqYuMYZw9UgQnLvkG10R%2Fuuok6iqoXOgb38DZhcSkV4h4EaMK8q6lr5GtHJz5n63c14ps%2BBOoWagXMOONg70GOqUBOMkGtHt1bhSVSltxmJjgukf4BgakrGBh1v6JmEk0S%2BFTE9dMICn4A7KY1LLTuJZ15uHu7v6rVjYgHIKQyEfiNZQ3fvUrwF%2BN3PKisYFXEiBlE2J5QnzbQ2KZDV9bnxY72vr4sBO8YvNFvMeunBQ6BDKYrNzcGbHSRBXp8Id1u07U908A0tcsdl%2FkuOU52GvPl7UHWjtzyzsJods95HcOS1ZoFVDK&X-Amz-Signature=f087a9f9db6a9689d1e09c1e275eb8cd02b6a695b7d9bad12fd41a4d97620fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTUCAXQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuo2tSK%2F4DLLxDxs0rR1fy49vyakHXUgt1ByQnFTDKIAiEAi55TvpZ6YvAb4m4ANiHyblmWS%2BEGuvDIFcbeX3UESKAq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBLhsg83zVSKkGhX%2BCrcA%2BkMSi%2B9SsIyNUItj7kyXtDLQHnexct%2BGOOXJXhFss1iIOk9BVduishmqr1qIMAi4gcJfsNavZhsIV8bIVGKn1KebwIO3lBFm4euw%2FOlwLB0UhJZC7%2Fb8s%2FLQT%2Buvahx25W6W0XP5XWOUWf9uTHX%2FsrW9N8h9%2F%2F3%2Bxjydn3Z%2FXzf9IVsIHzEQgHUQp%2BWuRsqHHAzhv7Q8GhqiCXEuNxT2gvvtTtsAlyihxDybXWgsUtSmrSaEyqHm6yLfCckvyKRDNFOv7WgRpwu0Zap2mJfuSeN5gvYj7rURsGEmj6Ol62TmS1j7YM7UCe9qQsVhzqhGlpmJQQ3b%2Fw6OUk7gSy8PxO49pQDLFQdSVNWSIW9YXr0F82KdSEkRoHXPI9ToX4YtY9X7xXYySopgIT0%2Fnyld9ez4lUi79WjmvAmFIY4fhcKEw9SlpGpuCmoAocB0GnxlX%2FKZfbgvDHLvZDACl4oKyLs1qINNUCnRP%2BpvFs2u2efBjnU3T0KCUpzYEvP7wMKc9FGtkKV0lfgRmMauvpl0rSGeRyjfaltNMbT6xDz%2FZmOxoJFqYuMYZw9UgQnLvkG10R%2Fuuok6iqoXOgb38DZhcSkV4h4EaMK8q6lr5GtHJz5n63c14ps%2BBOoWagXMOONg70GOqUBOMkGtHt1bhSVSltxmJjgukf4BgakrGBh1v6JmEk0S%2BFTE9dMICn4A7KY1LLTuJZ15uHu7v6rVjYgHIKQyEfiNZQ3fvUrwF%2BN3PKisYFXEiBlE2J5QnzbQ2KZDV9bnxY72vr4sBO8YvNFvMeunBQ6BDKYrNzcGbHSRBXp8Id1u07U908A0tcsdl%2FkuOU52GvPl7UHWjtzyzsJods95HcOS1ZoFVDK&X-Amz-Signature=eacd3f4a420a5584c7faec9893517b6e2e81e7914fb7ea482275287e8aa70364&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTUCAXQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuo2tSK%2F4DLLxDxs0rR1fy49vyakHXUgt1ByQnFTDKIAiEAi55TvpZ6YvAb4m4ANiHyblmWS%2BEGuvDIFcbeX3UESKAq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBLhsg83zVSKkGhX%2BCrcA%2BkMSi%2B9SsIyNUItj7kyXtDLQHnexct%2BGOOXJXhFss1iIOk9BVduishmqr1qIMAi4gcJfsNavZhsIV8bIVGKn1KebwIO3lBFm4euw%2FOlwLB0UhJZC7%2Fb8s%2FLQT%2Buvahx25W6W0XP5XWOUWf9uTHX%2FsrW9N8h9%2F%2F3%2Bxjydn3Z%2FXzf9IVsIHzEQgHUQp%2BWuRsqHHAzhv7Q8GhqiCXEuNxT2gvvtTtsAlyihxDybXWgsUtSmrSaEyqHm6yLfCckvyKRDNFOv7WgRpwu0Zap2mJfuSeN5gvYj7rURsGEmj6Ol62TmS1j7YM7UCe9qQsVhzqhGlpmJQQ3b%2Fw6OUk7gSy8PxO49pQDLFQdSVNWSIW9YXr0F82KdSEkRoHXPI9ToX4YtY9X7xXYySopgIT0%2Fnyld9ez4lUi79WjmvAmFIY4fhcKEw9SlpGpuCmoAocB0GnxlX%2FKZfbgvDHLvZDACl4oKyLs1qINNUCnRP%2BpvFs2u2efBjnU3T0KCUpzYEvP7wMKc9FGtkKV0lfgRmMauvpl0rSGeRyjfaltNMbT6xDz%2FZmOxoJFqYuMYZw9UgQnLvkG10R%2Fuuok6iqoXOgb38DZhcSkV4h4EaMK8q6lr5GtHJz5n63c14ps%2BBOoWagXMOONg70GOqUBOMkGtHt1bhSVSltxmJjgukf4BgakrGBh1v6JmEk0S%2BFTE9dMICn4A7KY1LLTuJZ15uHu7v6rVjYgHIKQyEfiNZQ3fvUrwF%2BN3PKisYFXEiBlE2J5QnzbQ2KZDV9bnxY72vr4sBO8YvNFvMeunBQ6BDKYrNzcGbHSRBXp8Id1u07U908A0tcsdl%2FkuOU52GvPl7UHWjtzyzsJods95HcOS1ZoFVDK&X-Amz-Signature=df784886e0b0c5f67f4edbd1afbc0477118433ddf59997ed0ccbd2209e9eb0d2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HEJ4KPK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC67s6foYkvTqy22wG4X4F5siLCAPdnhbdHMCsvd5uvygIge9WFtXWABvwM81mgvczOHMS9%2Bt2ASof35mXOWqey520q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDKgtuSVh4CcB42JEircAx%2BFhZk0ScFu5xmagpVL7%2B1k%2BfVzSzg25kPwWR%2FEfsHxfHkQPFhc8B4JTJYOXr0vf6MNc4btExAdV7Q7Bn0xKxSS4EKsY41qVsHgHF5h0HD6Ari6JGwZNcl51W8vwVfKfI9%2FvQbT8g5x5XcZWH%2FYb8V9hi6qwy8MqLcMR217jhtvDPKpnW7WxUb0YNFnnK8dCwCEeF21xaW%2BYkrs2VaOBOJhVBiy%2B97B7tmoLlSZPthreUmZdyRmqv4H%2FphPkk5KlEJUdSXKxOXe0aUFOomcp4rtfJv6QqMyVBwPchNY2gRA91l7nz4%2FUohNjc8nDh4cIXgB3euEHRRBpDXMZBd5azacRkXShKWGCINoNKiHWA6aUIaceJeIbS2bazPx9r8bMRB9zClalwKdwBGv4CXwDkPwoMnvLeJLds9ziW43WGM8UpQQ7vmBnaBpwgW3O9vIksl%2FZRiEsD4KYYAUm9qn3E1rsXk02AJ9Ep%2BWL6qAGlD%2BdmmHFFDeU1NdDmcP%2BmWMdxnLD2rEDR%2BMqXMnvrHk120dXFbt%2F9Y1GDpT2Lz5rJzzIJL6J97GAOJIWUPYb0TzftuIoum5Q6FmmLe7AhJAAdlbibdQgY3N9ZqfoFPORl8cIe%2BQkCtGEtrK8v2YMNGNg70GOqUBZzEeaydBD3uYId3%2FNUNb6IrogNFgZMCdevm2fXRn83NDmKfjs%2FY0Yql6q7qzthIxabpiCrSHpeIbCzzeYtng0LDW29rd%2FBOjjhl62tqZ%2Fu6Psn0wfHs4Y7DgF30h480ywodqbugyItgDJLJi31FBFzAqCmnAVjvBp6Zn0MF40WzfPDaxjL97D4ZwDSnT7hRkjXY9uqmDB8HSF27v2thhxpSLSCls&X-Amz-Signature=b072eb449cc045d064bfc37499c9f063ee51548e6f2076965a5641abb8bc1df3&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJB6HBET%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH%2FRqW0O%2FVSDE1UjBvKgta2%2BztfqhRotNrb3iLfEWillAiEAjtXS3Hwjdm%2BxObNfpe%2FOfTuSkbtoughdaIoeVZy8Fcwq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDIXyEgiszQ4UIHVVcSrcAws6n%2BVYsTEpSY6rL8F1Y2WzvA8XTrwWGS1HsR%2BdzQjSA1gnfJbTX8L1xkIi9nGYMRRDKyUVLPdL6QvDFEUGOC8KNoKayN5HLll92Mqo%2FUm3WvXnKFwCUAjvsg8QNkjftrbqIc6GY2y97y%2BKoKJRW3AzfQuXt5G4vbAHXCuEjSqjI07NcCVeMaxzXuFrc4sn9I06eT%2F3xhz1RzTOesQ24BPw0iBirwIw1uuDJt9W1uJZ0ns09CQHdCFaaUSOHmlb7X6mUyrnupXHzfKEBJQWVPcAacUgVo1s%2BKAfAcobXbEAnFKii1gm5uuzQfW7ELho24Y0%2FkI657JrgTiWQ0Rbnn0%2FiMbGESrv8AHYJmjysfWbh%2BgrsSeiII%2BcbqQFiQrLKTvMr6FQHOLdbCQP7iDMX%2BecsaEoZItlF5n8nu7i2MIfOuXvL5dvxuHQG3Esz4PCRDZ%2FKtA%2B02k%2FjUrKQX51D46h3p%2BVVv1UvakhIb9kkIXkYNkSE7RgDNh8yN3rdRgdaF8GoICTLdF1sMvOm3gfCGBChQsCq0GX9mwKf%2BY%2FjxCZQKuCZ2WgcGlNQUxF%2F2ARcaRwi8jT17dDcr3%2Bp0lQCQFtB2eKMjW%2Bhy5qxD%2B2vndWc1Oe4MwsmvWChPLvMOiNg70GOqUBHYded%2F0GQPxnpLLcFngCl0ajZNZzsqvXjGgw8k4j2%2FbK7wHSIDCAh3olHAy0sjeZof5eX7TKPOAQ%2Fdtm362OCxOQ2yKzw8LeNJh0nyQ9oANzAJs52vs9W7x26EVw88S1L3Tka6%2BWYOM2%2Bkrfkdqp6hNkB6ASwhcwg1QhmprlSt88OT%2FUM6oOdk4r2%2F5g1CeCptyMGJ25kKmiEEqcYgcFtPbKB3Ij&X-Amz-Signature=161a8346e423d2f23d0930e56f3787ff03ac3e243fa3e99f4f87264169b1cf96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTUCAXQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuo2tSK%2F4DLLxDxs0rR1fy49vyakHXUgt1ByQnFTDKIAiEAi55TvpZ6YvAb4m4ANiHyblmWS%2BEGuvDIFcbeX3UESKAq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBLhsg83zVSKkGhX%2BCrcA%2BkMSi%2B9SsIyNUItj7kyXtDLQHnexct%2BGOOXJXhFss1iIOk9BVduishmqr1qIMAi4gcJfsNavZhsIV8bIVGKn1KebwIO3lBFm4euw%2FOlwLB0UhJZC7%2Fb8s%2FLQT%2Buvahx25W6W0XP5XWOUWf9uTHX%2FsrW9N8h9%2F%2F3%2Bxjydn3Z%2FXzf9IVsIHzEQgHUQp%2BWuRsqHHAzhv7Q8GhqiCXEuNxT2gvvtTtsAlyihxDybXWgsUtSmrSaEyqHm6yLfCckvyKRDNFOv7WgRpwu0Zap2mJfuSeN5gvYj7rURsGEmj6Ol62TmS1j7YM7UCe9qQsVhzqhGlpmJQQ3b%2Fw6OUk7gSy8PxO49pQDLFQdSVNWSIW9YXr0F82KdSEkRoHXPI9ToX4YtY9X7xXYySopgIT0%2Fnyld9ez4lUi79WjmvAmFIY4fhcKEw9SlpGpuCmoAocB0GnxlX%2FKZfbgvDHLvZDACl4oKyLs1qINNUCnRP%2BpvFs2u2efBjnU3T0KCUpzYEvP7wMKc9FGtkKV0lfgRmMauvpl0rSGeRyjfaltNMbT6xDz%2FZmOxoJFqYuMYZw9UgQnLvkG10R%2Fuuok6iqoXOgb38DZhcSkV4h4EaMK8q6lr5GtHJz5n63c14ps%2BBOoWagXMOONg70GOqUBOMkGtHt1bhSVSltxmJjgukf4BgakrGBh1v6JmEk0S%2BFTE9dMICn4A7KY1LLTuJZ15uHu7v6rVjYgHIKQyEfiNZQ3fvUrwF%2BN3PKisYFXEiBlE2J5QnzbQ2KZDV9bnxY72vr4sBO8YvNFvMeunBQ6BDKYrNzcGbHSRBXp8Id1u07U908A0tcsdl%2FkuOU52GvPl7UHWjtzyzsJods95HcOS1ZoFVDK&X-Amz-Signature=34d6fea28ec9de59aaebbd469829bf1deb19219011afc320764d67accd71005a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTUCAXQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuo2tSK%2F4DLLxDxs0rR1fy49vyakHXUgt1ByQnFTDKIAiEAi55TvpZ6YvAb4m4ANiHyblmWS%2BEGuvDIFcbeX3UESKAq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBLhsg83zVSKkGhX%2BCrcA%2BkMSi%2B9SsIyNUItj7kyXtDLQHnexct%2BGOOXJXhFss1iIOk9BVduishmqr1qIMAi4gcJfsNavZhsIV8bIVGKn1KebwIO3lBFm4euw%2FOlwLB0UhJZC7%2Fb8s%2FLQT%2Buvahx25W6W0XP5XWOUWf9uTHX%2FsrW9N8h9%2F%2F3%2Bxjydn3Z%2FXzf9IVsIHzEQgHUQp%2BWuRsqHHAzhv7Q8GhqiCXEuNxT2gvvtTtsAlyihxDybXWgsUtSmrSaEyqHm6yLfCckvyKRDNFOv7WgRpwu0Zap2mJfuSeN5gvYj7rURsGEmj6Ol62TmS1j7YM7UCe9qQsVhzqhGlpmJQQ3b%2Fw6OUk7gSy8PxO49pQDLFQdSVNWSIW9YXr0F82KdSEkRoHXPI9ToX4YtY9X7xXYySopgIT0%2Fnyld9ez4lUi79WjmvAmFIY4fhcKEw9SlpGpuCmoAocB0GnxlX%2FKZfbgvDHLvZDACl4oKyLs1qINNUCnRP%2BpvFs2u2efBjnU3T0KCUpzYEvP7wMKc9FGtkKV0lfgRmMauvpl0rSGeRyjfaltNMbT6xDz%2FZmOxoJFqYuMYZw9UgQnLvkG10R%2Fuuok6iqoXOgb38DZhcSkV4h4EaMK8q6lr5GtHJz5n63c14ps%2BBOoWagXMOONg70GOqUBOMkGtHt1bhSVSltxmJjgukf4BgakrGBh1v6JmEk0S%2BFTE9dMICn4A7KY1LLTuJZ15uHu7v6rVjYgHIKQyEfiNZQ3fvUrwF%2BN3PKisYFXEiBlE2J5QnzbQ2KZDV9bnxY72vr4sBO8YvNFvMeunBQ6BDKYrNzcGbHSRBXp8Id1u07U908A0tcsdl%2FkuOU52GvPl7UHWjtzyzsJods95HcOS1ZoFVDK&X-Amz-Signature=b2678946e9d6f3d8c6599f79f76ca0e12cfadf51afea6ee6bf6f9519567e7c34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTUCAXQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuo2tSK%2F4DLLxDxs0rR1fy49vyakHXUgt1ByQnFTDKIAiEAi55TvpZ6YvAb4m4ANiHyblmWS%2BEGuvDIFcbeX3UESKAq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDBLhsg83zVSKkGhX%2BCrcA%2BkMSi%2B9SsIyNUItj7kyXtDLQHnexct%2BGOOXJXhFss1iIOk9BVduishmqr1qIMAi4gcJfsNavZhsIV8bIVGKn1KebwIO3lBFm4euw%2FOlwLB0UhJZC7%2Fb8s%2FLQT%2Buvahx25W6W0XP5XWOUWf9uTHX%2FsrW9N8h9%2F%2F3%2Bxjydn3Z%2FXzf9IVsIHzEQgHUQp%2BWuRsqHHAzhv7Q8GhqiCXEuNxT2gvvtTtsAlyihxDybXWgsUtSmrSaEyqHm6yLfCckvyKRDNFOv7WgRpwu0Zap2mJfuSeN5gvYj7rURsGEmj6Ol62TmS1j7YM7UCe9qQsVhzqhGlpmJQQ3b%2Fw6OUk7gSy8PxO49pQDLFQdSVNWSIW9YXr0F82KdSEkRoHXPI9ToX4YtY9X7xXYySopgIT0%2Fnyld9ez4lUi79WjmvAmFIY4fhcKEw9SlpGpuCmoAocB0GnxlX%2FKZfbgvDHLvZDACl4oKyLs1qINNUCnRP%2BpvFs2u2efBjnU3T0KCUpzYEvP7wMKc9FGtkKV0lfgRmMauvpl0rSGeRyjfaltNMbT6xDz%2FZmOxoJFqYuMYZw9UgQnLvkG10R%2Fuuok6iqoXOgb38DZhcSkV4h4EaMK8q6lr5GtHJz5n63c14ps%2BBOoWagXMOONg70GOqUBOMkGtHt1bhSVSltxmJjgukf4BgakrGBh1v6JmEk0S%2BFTE9dMICn4A7KY1LLTuJZ15uHu7v6rVjYgHIKQyEfiNZQ3fvUrwF%2BN3PKisYFXEiBlE2J5QnzbQ2KZDV9bnxY72vr4sBO8YvNFvMeunBQ6BDKYrNzcGbHSRBXp8Id1u07U908A0tcsdl%2FkuOU52GvPl7UHWjtzyzsJods95HcOS1ZoFVDK&X-Amz-Signature=087d5ab505056540a825d3c95a4cd41fd3d6401c887bee7ff9bd8490cbf4ee03&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKBHO7XV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICIRBgy5PkSHgSkli6FW1XJwc0AIqRqAe0Qyv8E%2FQhraAiEAwDyStpnpqWzAD9lQgTSqSYZnLkBuBWZfIVUhVEycclkq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDB%2BJ1DqAtE6oAfTAWSrcA8eD3xvhC3ZoHvqjT%2FzIWEEJ65%2B3xzRMA6jbRYEyp4j0GYjRGXHAQcZvYp%2BCcgkWPbJ7HDfhMJJCiGgsl1fZaFbjLy1WEQ8FSpTrYlf5OD4ovud%2FpeZyUbOmE4Pk2DfObsOvQrTFGLEcBFigUgq04fxVBoxmLtCxIgKYIWd1drVPeP9W6Tph23%2BVePKjHSZ%2FFKUFXYVb6dfmPVqenMEtdtQVRD1aumaTcirHVU84FGfZIzDG7ceW5yTIokJ1Y%2BuE4D%2FHnhJ67ADGpuCu%2FLKJY1yxG6c4nb57KXiuUe588d%2FljpI0zdZ8icC4Bg6BSGECdGf16H9rkCGUdCv7rvU4zRwt9Hr61i0CuLg9IAhHMqICOFHHdZosUIaCF4V0Jm6gIFClF03hsbqY%2BcbJi%2BJnKZTDvtZJCgokPvmWTMEArXGM%2Bt3dbnxSeqANVXVVAKAdZA%2FwLJY5yMDE05Bbyt6FawEftyPBdTLrnjIJAo1XIulZ3sBfPV0J0VRzo9uMIZsOOg7cBSMBSV%2BNSa6Wv0Ke1HSBkzS5q6d8zWgyMSWqEsFTiz3RYym4RYPH7wbjPWPsEvgOktp1oujemVjzvlU6KxqAnlzvMpQqcIWz2MLtKZ4eXyPKcsd7aOtrGtWgMLiNg70GOqUB0PKDd9svTp%2BgUbnE1IAJ8BquEHCdtkLvdlLJZhPnG8oLyqvD4goZcajfJCUVQfLnJ0MG%2BY8hsS%2FYPuqhsS91B31UzoMzk8q0TbGHROljjkFGdEwU6mdHBLP%2F4NKjLvbiTiUWvIpTMoHDmZXPl3Eu%2FS9cjcCOFlm3%2BwGOsBTP0MJdv4A61pwcHuc2mGH3XXuY2I73KaG5Q99OA76NClIm3rWBd0mL&X-Amz-Signature=3be42f664d5a60042b8f8e15dcff3c61ded7434a69f8c6c88a4a42816a381c37&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFDMJRF6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHx5ZR%2FdKXdm9zHUmc5molJGqx9MKYaMXy64TjDoy0LLAiEA%2FOAyYMF8Mm79APUCmTUrXW6QsPNfbxgEIPXfpobYC0gq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDPpBEOtomhTkPjPGLyrcA4pruliWc78d1gbpUOUWxL4vgKcN6MOS8gO3GuTad0lgZ%2FNueQTmOCqMUuiwvUUGLWHQRzj25bmaXSu4TXT07dC2%2F20hvqbvuO0E%2F%2BEB1sdKrIAvoGDBncKrbO4Ww%2FobCrOXusN1yG%2FM%2Bn%2FIfdH5y4aGdCz6ZlD%2FFGNMFyk%2BZ8tF9qE9Y87gMNaIDpA%2BYXBnUmt9GwzXG62nCzOQfiiWDzhM1At3uSzAsaH3f%2BKZ6i8o%2FOHdv6dv5qVUIyJzZ83210n7CGQ5UYh6kfZrpePJND7gk7RdYqBJyCeOhyT25HEtx8w65P0Xr5hv0jHkg%2BHQJKfoTfYhHCVPBgpUpVqzu6GR7Wp%2FVNMD%2FYE2ccG4WVoxgrV92prytHZ6td7YWNDLTzf5F30oD7lZfuSGt3XYvaHiVKUJfFHTgSYAJGjOWZl2BZj2mBHfUATW7hULwbltqvam5wiN6vOAf6CCHJwYfMgJL8b5MmH3GUkHxR3pweG9ZnXuuG7AecipwiE69N8hmI3xN6kOnIkJ%2FGY64R8%2F5nw7a4cCbjjis2PbYCjzEAIBRtwaQ1A5JRdaHlGyR4M%2B7dR6%2F%2Bw1tPKEJW4gARCUeGWTORbivPtshkBgT2muqMkRhkbVAoKCG9XQMNxyMKGNg70GOqUBNLe8eKDHhw2s0V%2BwPijYsnrTIZTFpHxV%2BavaXu6Vp2fXyDiuiqjxHhKElTrcFaeNYsVEw1U29LEG3acb%2F5uCR5QzcfmJER1BrEv8Kmm1Ugq4ecAvjP%2Bqg7mnbAj%2FPGTV5QhxjYpeMufxKeAxlKU%2F8F7a4aAsATJTQt0%2FEB0iFISbNyliZOQajf90ZgPWsDNDZ4MaRPb6VgORjHp%2BxXraIgxUOK0T&X-Amz-Signature=62efabbd7cf2fc5b1335bcfa9689f040ec41ea1431425106688064e675b71ab1&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X243TLHB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEYbnlXOhQ1cLFjWXPUI%2BbOfdof8GYbK3JT6nPvyTMfQIhAPrxf6ulYmahuFFtoSgLG8Il3ziQqtuUtAnnJL2o4JfhKv8DCBcQABoMNjM3NDIzMTgzODA1IgwiwS3pYPWGJrBrGlAq3APwAFQQaz0zsg%2BtCs6WObuMQHAOU6b1gm%2FRL46qHyu7UVQvHMwNEb06I%2FggXqhcwBeFpBDvS%2BXGxC%2BOBDEHPQiJfeFk%2BHfJjGwY47M7bRwqQi064mHs7knxrw1eOdWFvio6%2F%2FOEAPUKhfv8nTTONhs9AAqf1l%2FbyRyB0mXjb92rZ4xPnsIWnFzT2abObiRVpI%2FFdKI0M%2BciDaEca%2BNTRX58Rf065vPI42B7TVROt%2BOIB1%2F6E%2FLIL8YWXNYLFuxW%2BcYYNXYCsQTAFDT7hbWkVvDQWgcA8B0nPZddkAG4jvO07nhRkXChOaKCvyyoUuWNDiv42m%2FkSHeb7AfgKR%2F6cJZxNTFGPrYCgL7RbTdQqR0WhTZ5WlJ0UydOsCbDwbGEYPXqewQdYmpeUCTqIy0JwKW8zgtHr2ZegWsaCj8JM89rx8hReyrs%2Fx%2BZxzDONYl%2FIfIX7xnRHRX3Vs08drf8G7YeXLXZRUkwGpZprygNDKG3nrTagDgAlm%2FjP6e7u4OkgazuxSSpNZgV5ilLsCS%2BdZwSHqrxxTP%2BDj7%2FR59vCrrX1gFb98sgRs3rfzAGDfzJU3jEhW9GrDBMcSBQT9s9CP3%2FjwlWu5Q1kyRzQaqeVH6%2BJmHJxOxuWap5U2qXiDDXjYO9BjqkAYY8ChGLh%2Bunbloyqn%2Fss0Pf0obEFQwqP29LGAvuA%2FSjG9ggzzXI9sgEzn6LvLcCzCPYzJ%2FyWBb5B2DrDgnJoqqyPEaNuMP1r7%2Bq9Pdqb%2BwquqENZjy7b%2F%2FfiQRlzftuKzC0u6n8RdvbnBk5T4BTrKHiG2I9A2Lhyz0VXkR5q0IOOkwDfxknCiZ00JGt6rSwzLn2PbuF9ShldS59wC04QWnPjuK%2F&X-Amz-Signature=5086791a88a7e1c298eee911c24dd619d52718cfeccd347b7c16e93a3da866b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYAXX4A7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQhUjSooyFfqQ9vlgPmdAPpyv9ibnN4dp4r8kBy8OP%2BQIgKKKiVhMDTFada7fOYlUlAHvtTrUSaxNwb7f4iEeXqbEq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDLlG03z%2FzVWBWsuD8SrcA7OH7E%2FP0EnycDcR7qSQlq3d1H4iCPSo5oao4mhj5y%2FwGhv54wJra2d8ZqVc8QWjvW4v%2FniJBUwfTuRU6J5WUK8k6MKDbk%2FxxhjeMns0l8%2Bfl0VLBrnMHu1K1YLz0%2BUZ5qXxp%2FkP0R%2BJj000QbBh9aHXaRdjBJ6ygy8rSncwRm38sm6Jky2FqZ39nufbk3uXfJcEjeB1I6GGYxlOlfl9lu%2FVEZLIPxTGhdQBpZswVq98MxwdbyjCE6XXN55267IMHYb8hyXN75nOa77ipkwWMi1yBMZK1HWGgbfaR8EVt%2FIEq3SC%2BIhqQbXEnEyL6H1zPvyc2gR0cL%2BorNcSgoH4wVwe7Fy5fNv0UgjxyLoyMFYQNpc5bh3G7lpU%2Bsf%2F%2BT%2FB5WQR%2F3qu4YCVDmKnBqAjg5wbULeyTSmQzxr61b0uh2v5RvYEoqTo5%2B9yrJiFHUoKgaJBVhtxzcm694RqlBID%2BIH9HJJ%2BrjptD6JuS0sqFFi2dOZrluJA04T3ohy7mwc0TxNUAjFZbR%2BH7Y1IIybxSPSVlvOGSXWj0PqOdkjd6wrc7UDkouNxEBerEWBrrR2ebXFvlDERdCi3GTvYQc7A%2FCyVGMlIZQIM4RRDUqdvkjsDOgEu9IlRCmomXM8MMLiNg70GOqUBPb2x%2BOvgCRulrCiFSaJGtoFttH85T%2Bj%2Btd2z8ZLuh2tWVxraG3wsRaQTG1IOXMmgeRoWHS9b4VTIrQO1sU4NDgfFrezL8Q2dSJEGTCm65Y4mgGo%2BwNkI2wJEUd9l7v%2Fm3ztQYZp4rA1tF6OENv%2FiGKZbTq057xhLUm1P6keVZyJHfJCBRpRWQBCryZNhVmC7xMkJh1gEMkS%2F2BwrPbsUr7T6lu2G&X-Amz-Signature=e6881cffead30a4998b5862e907edf72658f58347003fd81f81b14a8c6228409&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYAXX4A7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQhUjSooyFfqQ9vlgPmdAPpyv9ibnN4dp4r8kBy8OP%2BQIgKKKiVhMDTFada7fOYlUlAHvtTrUSaxNwb7f4iEeXqbEq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDLlG03z%2FzVWBWsuD8SrcA7OH7E%2FP0EnycDcR7qSQlq3d1H4iCPSo5oao4mhj5y%2FwGhv54wJra2d8ZqVc8QWjvW4v%2FniJBUwfTuRU6J5WUK8k6MKDbk%2FxxhjeMns0l8%2Bfl0VLBrnMHu1K1YLz0%2BUZ5qXxp%2FkP0R%2BJj000QbBh9aHXaRdjBJ6ygy8rSncwRm38sm6Jky2FqZ39nufbk3uXfJcEjeB1I6GGYxlOlfl9lu%2FVEZLIPxTGhdQBpZswVq98MxwdbyjCE6XXN55267IMHYb8hyXN75nOa77ipkwWMi1yBMZK1HWGgbfaR8EVt%2FIEq3SC%2BIhqQbXEnEyL6H1zPvyc2gR0cL%2BorNcSgoH4wVwe7Fy5fNv0UgjxyLoyMFYQNpc5bh3G7lpU%2Bsf%2F%2BT%2FB5WQR%2F3qu4YCVDmKnBqAjg5wbULeyTSmQzxr61b0uh2v5RvYEoqTo5%2B9yrJiFHUoKgaJBVhtxzcm694RqlBID%2BIH9HJJ%2BrjptD6JuS0sqFFi2dOZrluJA04T3ohy7mwc0TxNUAjFZbR%2BH7Y1IIybxSPSVlvOGSXWj0PqOdkjd6wrc7UDkouNxEBerEWBrrR2ebXFvlDERdCi3GTvYQc7A%2FCyVGMlIZQIM4RRDUqdvkjsDOgEu9IlRCmomXM8MMLiNg70GOqUBPb2x%2BOvgCRulrCiFSaJGtoFttH85T%2Bj%2Btd2z8ZLuh2tWVxraG3wsRaQTG1IOXMmgeRoWHS9b4VTIrQO1sU4NDgfFrezL8Q2dSJEGTCm65Y4mgGo%2BwNkI2wJEUd9l7v%2Fm3ztQYZp4rA1tF6OENv%2FiGKZbTq057xhLUm1P6keVZyJHfJCBRpRWQBCryZNhVmC7xMkJh1gEMkS%2F2BwrPbsUr7T6lu2G&X-Amz-Signature=e4b9e04a0e211f7a93f0e0e97850fe0dd3b25770caa8a42dcf0e0f5d6fe1cb85&X-Amz-SignedHeaders=host&x-id=GetObject)

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
