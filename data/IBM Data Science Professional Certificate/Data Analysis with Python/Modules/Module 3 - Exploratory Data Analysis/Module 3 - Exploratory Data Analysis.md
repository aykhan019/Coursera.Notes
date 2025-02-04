

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YYN63HO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIAPslam3RrmkITu5dTsTHmlX0f3pse66UYxacMktKhVeAiBvY8PmpfjssTfrDikdX%2FsxSwhXNKyhJQVUaMQ3v34yxir%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMLvFqJ%2FuJf1Ng4icxKtwDbhsYSRtYqIZPnkmia2DYVruGsKxWnMpMlpR3qShkAhilan%2BeqS5XjbGebk6KH2ar%2BZsuCmLcmbWvLYIM7bF%2BkyaiotyqJn7ev471G3AhLYVi6YMNxfoOXlJ8jlXsOHoVl9PUohR4NS2RN7rLvlyAD0zlrQVd0XXeib4%2Bkko73Bl5b44opsnEAi05BK7xC5AIig%2BDstaMi8GbcLBhptULRbb3kQMTMdHfrFAk1LWSIwJsQjdtiFRjk6ALCCjb6mLwaT1saD2Lv5zNMUO%2F%2FexNm4OUAT7%2B4NAFbNG68c7L2FkL0g1xPkdNKBPQVrMkuWo%2FfOur4xn8XAPRyKmJ7ZjhrxcFzV4eFTSNXKj2XP5n8Km%2Fz7zUJOO5juLwuhWc0FIrX%2BA%2BBHbghtjHFLC9J1noTSSsHaFID%2BBc0Xccws3JyiKK3XLIHFjZSw3eSiZkQ3E9%2B%2BVMNek6p8C%2BXQ2PGTQL4xz%2FS2tj9hHu%2B6Y%2Fo85QpX57PMVkYKIaAjapQzxBbJnoaAxSTvaaQ19VSEdorqCnD7GmZYkE05z8wSKlU0jjxgFWk%2BoqpjnT0J5ImnCFvEG%2F7FUfggCmi3pXuN3ZNO%2FoHPXCf67cf5bv0v7%2Fsjei5Gac8CXNfXnuxdSC8tcwv6GGvQY6pgFHAGyv3HW2Fs1biDNf8c0g7SpE54aIzNGxvBFD9EA7ye8hWrhHuFlFmXpKrwyrv6r0Tf2NWoKwlyZ%2BKCmHYfP4T8OojEEbfpo9xdqYZGUT6uE%2BSHNaAvvHCU2UoL4xtFiAZutNEbJAe7ofEpDRLjVWaRLUgh5OOouRA8oMqlAfw5hZGNzu3Y%2FwoIf%2F4v%2FvD%2BHxJUn1yAgeIXxu2Y%2BE4fS%2B%2BYOf7jwL&X-Amz-Signature=a18b1a751b80d135d56ce75790465253761b82a40eecfb45218a884f31d9d68d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YYN63HO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIAPslam3RrmkITu5dTsTHmlX0f3pse66UYxacMktKhVeAiBvY8PmpfjssTfrDikdX%2FsxSwhXNKyhJQVUaMQ3v34yxir%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMLvFqJ%2FuJf1Ng4icxKtwDbhsYSRtYqIZPnkmia2DYVruGsKxWnMpMlpR3qShkAhilan%2BeqS5XjbGebk6KH2ar%2BZsuCmLcmbWvLYIM7bF%2BkyaiotyqJn7ev471G3AhLYVi6YMNxfoOXlJ8jlXsOHoVl9PUohR4NS2RN7rLvlyAD0zlrQVd0XXeib4%2Bkko73Bl5b44opsnEAi05BK7xC5AIig%2BDstaMi8GbcLBhptULRbb3kQMTMdHfrFAk1LWSIwJsQjdtiFRjk6ALCCjb6mLwaT1saD2Lv5zNMUO%2F%2FexNm4OUAT7%2B4NAFbNG68c7L2FkL0g1xPkdNKBPQVrMkuWo%2FfOur4xn8XAPRyKmJ7ZjhrxcFzV4eFTSNXKj2XP5n8Km%2Fz7zUJOO5juLwuhWc0FIrX%2BA%2BBHbghtjHFLC9J1noTSSsHaFID%2BBc0Xccws3JyiKK3XLIHFjZSw3eSiZkQ3E9%2B%2BVMNek6p8C%2BXQ2PGTQL4xz%2FS2tj9hHu%2B6Y%2Fo85QpX57PMVkYKIaAjapQzxBbJnoaAxSTvaaQ19VSEdorqCnD7GmZYkE05z8wSKlU0jjxgFWk%2BoqpjnT0J5ImnCFvEG%2F7FUfggCmi3pXuN3ZNO%2FoHPXCf67cf5bv0v7%2Fsjei5Gac8CXNfXnuxdSC8tcwv6GGvQY6pgFHAGyv3HW2Fs1biDNf8c0g7SpE54aIzNGxvBFD9EA7ye8hWrhHuFlFmXpKrwyrv6r0Tf2NWoKwlyZ%2BKCmHYfP4T8OojEEbfpo9xdqYZGUT6uE%2BSHNaAvvHCU2UoL4xtFiAZutNEbJAe7ofEpDRLjVWaRLUgh5OOouRA8oMqlAfw5hZGNzu3Y%2FwoIf%2F4v%2FvD%2BHxJUn1yAgeIXxu2Y%2BE4fS%2B%2BYOf7jwL&X-Amz-Signature=76ef2b36eae42e469a9bb65856873186d27d84515aaaa89e954ab2526ab39ea5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YYN63HO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIAPslam3RrmkITu5dTsTHmlX0f3pse66UYxacMktKhVeAiBvY8PmpfjssTfrDikdX%2FsxSwhXNKyhJQVUaMQ3v34yxir%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMLvFqJ%2FuJf1Ng4icxKtwDbhsYSRtYqIZPnkmia2DYVruGsKxWnMpMlpR3qShkAhilan%2BeqS5XjbGebk6KH2ar%2BZsuCmLcmbWvLYIM7bF%2BkyaiotyqJn7ev471G3AhLYVi6YMNxfoOXlJ8jlXsOHoVl9PUohR4NS2RN7rLvlyAD0zlrQVd0XXeib4%2Bkko73Bl5b44opsnEAi05BK7xC5AIig%2BDstaMi8GbcLBhptULRbb3kQMTMdHfrFAk1LWSIwJsQjdtiFRjk6ALCCjb6mLwaT1saD2Lv5zNMUO%2F%2FexNm4OUAT7%2B4NAFbNG68c7L2FkL0g1xPkdNKBPQVrMkuWo%2FfOur4xn8XAPRyKmJ7ZjhrxcFzV4eFTSNXKj2XP5n8Km%2Fz7zUJOO5juLwuhWc0FIrX%2BA%2BBHbghtjHFLC9J1noTSSsHaFID%2BBc0Xccws3JyiKK3XLIHFjZSw3eSiZkQ3E9%2B%2BVMNek6p8C%2BXQ2PGTQL4xz%2FS2tj9hHu%2B6Y%2Fo85QpX57PMVkYKIaAjapQzxBbJnoaAxSTvaaQ19VSEdorqCnD7GmZYkE05z8wSKlU0jjxgFWk%2BoqpjnT0J5ImnCFvEG%2F7FUfggCmi3pXuN3ZNO%2FoHPXCf67cf5bv0v7%2Fsjei5Gac8CXNfXnuxdSC8tcwv6GGvQY6pgFHAGyv3HW2Fs1biDNf8c0g7SpE54aIzNGxvBFD9EA7ye8hWrhHuFlFmXpKrwyrv6r0Tf2NWoKwlyZ%2BKCmHYfP4T8OojEEbfpo9xdqYZGUT6uE%2BSHNaAvvHCU2UoL4xtFiAZutNEbJAe7ofEpDRLjVWaRLUgh5OOouRA8oMqlAfw5hZGNzu3Y%2FwoIf%2F4v%2FvD%2BHxJUn1yAgeIXxu2Y%2BE4fS%2B%2BYOf7jwL&X-Amz-Signature=82fedb0192b23a7c978fc961d3190e3e43d859122768bda40d2eb6355ff12fc8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTTKSVB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCF8LJ8icQdozjbbeUV2u%2FBFIhTOcQgD%2FgApBmXY0Z9KQIgE%2FLFnUz%2BrRydTb%2Bxbrr5KhPL8fYY6uhw1HivPKa7VGMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJvnxEIVbNjHHu1plSrcA4X%2BCTwI4DjQxE2fNESsdRg50wwmR7WJF%2FqzSETVUmrzHfJwB84W85WYDaqkc2CDNs%2F5r1nDfvpKS0SzI%2B%2FTF4aZNQkseor4rw8hBDOXcD%2F3hAQiDEe9JbgtkKZxa6gIGOG%2F2pDQ5VWcnbS3Jd%2FffHMKztReUZxiNOSqa4xEGysLFtuUCTMknykr6v6f76DBo3pA01ujpyxhG3ITIk%2BmlO0vGQSvnff91d6c5TcvdEiHtaBmo%2BFimn%2FNKcXJUI4FvDnRtPtW%2FLL4pYv%2BrAnayPdtzoscVM3nyqx72ru%2Be3rmeHr%2B1Nx2WueVUU%2FS7KqGiDZ1R9O99JsZdS5mQUo0AMqqMSMt2HpWUv4cZrTtqXC%2FP6%2FDNSeW7sd7ubQZHkOQkRMvjxElifluCxYpatQ08RgM2Glu08ylw3wad%2BQTF1Yf1blNE9NLJ01bkNIG1ATftWTKmYH1imVON%2BlhjMUrAkmU3s0ihaWmBU64KuBThVV3oMqWvAGpR68uuPvjr8d6q8MQjUSUFbVXD5%2FLlsusE%2BNFNfwLMCpZ%2B%2FNiYAugkWQcLgElGYYbCkyke6effVDObVuM0me7rd3fPnBYRY%2BpssV70ITf6LuxdRJjzj%2F1UgOb%2F%2F%2BD2egZo6qfQIZPMOWihr0GOqUBY509v55JOsz%2BJHkKb9lI8rYoOKJAHzML%2F4UPjLvpmZ4Z5qo%2B0%2FRckCrkvGmBw8Nw2n6IyYOcWFR04eE8znpk7WNkjIxCpzlTjvtbeFIEn6zHgcnldMt50lHLQl76tzetZWeC2jSamylqQPM7gdHWVfaijp8Gc0%2FpgD9ERoT%2BcFoqkZaxtwbGkoCPmhzHIGdrimYIMPnq0%2Byd%2BmurV9Jc5xESUfNP&X-Amz-Signature=6dd30002a1e6eb68ebde80ebff19be4e66ab9398814e9e764b23dd7bf5783642&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTTKSVB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCF8LJ8icQdozjbbeUV2u%2FBFIhTOcQgD%2FgApBmXY0Z9KQIgE%2FLFnUz%2BrRydTb%2Bxbrr5KhPL8fYY6uhw1HivPKa7VGMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJvnxEIVbNjHHu1plSrcA4X%2BCTwI4DjQxE2fNESsdRg50wwmR7WJF%2FqzSETVUmrzHfJwB84W85WYDaqkc2CDNs%2F5r1nDfvpKS0SzI%2B%2FTF4aZNQkseor4rw8hBDOXcD%2F3hAQiDEe9JbgtkKZxa6gIGOG%2F2pDQ5VWcnbS3Jd%2FffHMKztReUZxiNOSqa4xEGysLFtuUCTMknykr6v6f76DBo3pA01ujpyxhG3ITIk%2BmlO0vGQSvnff91d6c5TcvdEiHtaBmo%2BFimn%2FNKcXJUI4FvDnRtPtW%2FLL4pYv%2BrAnayPdtzoscVM3nyqx72ru%2Be3rmeHr%2B1Nx2WueVUU%2FS7KqGiDZ1R9O99JsZdS5mQUo0AMqqMSMt2HpWUv4cZrTtqXC%2FP6%2FDNSeW7sd7ubQZHkOQkRMvjxElifluCxYpatQ08RgM2Glu08ylw3wad%2BQTF1Yf1blNE9NLJ01bkNIG1ATftWTKmYH1imVON%2BlhjMUrAkmU3s0ihaWmBU64KuBThVV3oMqWvAGpR68uuPvjr8d6q8MQjUSUFbVXD5%2FLlsusE%2BNFNfwLMCpZ%2B%2FNiYAugkWQcLgElGYYbCkyke6effVDObVuM0me7rd3fPnBYRY%2BpssV70ITf6LuxdRJjzj%2F1UgOb%2F%2F%2BD2egZo6qfQIZPMOWihr0GOqUBY509v55JOsz%2BJHkKb9lI8rYoOKJAHzML%2F4UPjLvpmZ4Z5qo%2B0%2FRckCrkvGmBw8Nw2n6IyYOcWFR04eE8znpk7WNkjIxCpzlTjvtbeFIEn6zHgcnldMt50lHLQl76tzetZWeC2jSamylqQPM7gdHWVfaijp8Gc0%2FpgD9ERoT%2BcFoqkZaxtwbGkoCPmhzHIGdrimYIMPnq0%2Byd%2BmurV9Jc5xESUfNP&X-Amz-Signature=af39a2df2e2abbd3bfbffc64c4c463b8c34a0ead846fa275cc0465702e9c658e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTTKSVB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCF8LJ8icQdozjbbeUV2u%2FBFIhTOcQgD%2FgApBmXY0Z9KQIgE%2FLFnUz%2BrRydTb%2Bxbrr5KhPL8fYY6uhw1HivPKa7VGMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJvnxEIVbNjHHu1plSrcA4X%2BCTwI4DjQxE2fNESsdRg50wwmR7WJF%2FqzSETVUmrzHfJwB84W85WYDaqkc2CDNs%2F5r1nDfvpKS0SzI%2B%2FTF4aZNQkseor4rw8hBDOXcD%2F3hAQiDEe9JbgtkKZxa6gIGOG%2F2pDQ5VWcnbS3Jd%2FffHMKztReUZxiNOSqa4xEGysLFtuUCTMknykr6v6f76DBo3pA01ujpyxhG3ITIk%2BmlO0vGQSvnff91d6c5TcvdEiHtaBmo%2BFimn%2FNKcXJUI4FvDnRtPtW%2FLL4pYv%2BrAnayPdtzoscVM3nyqx72ru%2Be3rmeHr%2B1Nx2WueVUU%2FS7KqGiDZ1R9O99JsZdS5mQUo0AMqqMSMt2HpWUv4cZrTtqXC%2FP6%2FDNSeW7sd7ubQZHkOQkRMvjxElifluCxYpatQ08RgM2Glu08ylw3wad%2BQTF1Yf1blNE9NLJ01bkNIG1ATftWTKmYH1imVON%2BlhjMUrAkmU3s0ihaWmBU64KuBThVV3oMqWvAGpR68uuPvjr8d6q8MQjUSUFbVXD5%2FLlsusE%2BNFNfwLMCpZ%2B%2FNiYAugkWQcLgElGYYbCkyke6effVDObVuM0me7rd3fPnBYRY%2BpssV70ITf6LuxdRJjzj%2F1UgOb%2F%2F%2BD2egZo6qfQIZPMOWihr0GOqUBY509v55JOsz%2BJHkKb9lI8rYoOKJAHzML%2F4UPjLvpmZ4Z5qo%2B0%2FRckCrkvGmBw8Nw2n6IyYOcWFR04eE8znpk7WNkjIxCpzlTjvtbeFIEn6zHgcnldMt50lHLQl76tzetZWeC2jSamylqQPM7gdHWVfaijp8Gc0%2FpgD9ERoT%2BcFoqkZaxtwbGkoCPmhzHIGdrimYIMPnq0%2Byd%2BmurV9Jc5xESUfNP&X-Amz-Signature=94bf935f0720764aa42f43758cd6760600e5ac9b5799475a28e776140cfb2c58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTTKSVB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCF8LJ8icQdozjbbeUV2u%2FBFIhTOcQgD%2FgApBmXY0Z9KQIgE%2FLFnUz%2BrRydTb%2Bxbrr5KhPL8fYY6uhw1HivPKa7VGMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJvnxEIVbNjHHu1plSrcA4X%2BCTwI4DjQxE2fNESsdRg50wwmR7WJF%2FqzSETVUmrzHfJwB84W85WYDaqkc2CDNs%2F5r1nDfvpKS0SzI%2B%2FTF4aZNQkseor4rw8hBDOXcD%2F3hAQiDEe9JbgtkKZxa6gIGOG%2F2pDQ5VWcnbS3Jd%2FffHMKztReUZxiNOSqa4xEGysLFtuUCTMknykr6v6f76DBo3pA01ujpyxhG3ITIk%2BmlO0vGQSvnff91d6c5TcvdEiHtaBmo%2BFimn%2FNKcXJUI4FvDnRtPtW%2FLL4pYv%2BrAnayPdtzoscVM3nyqx72ru%2Be3rmeHr%2B1Nx2WueVUU%2FS7KqGiDZ1R9O99JsZdS5mQUo0AMqqMSMt2HpWUv4cZrTtqXC%2FP6%2FDNSeW7sd7ubQZHkOQkRMvjxElifluCxYpatQ08RgM2Glu08ylw3wad%2BQTF1Yf1blNE9NLJ01bkNIG1ATftWTKmYH1imVON%2BlhjMUrAkmU3s0ihaWmBU64KuBThVV3oMqWvAGpR68uuPvjr8d6q8MQjUSUFbVXD5%2FLlsusE%2BNFNfwLMCpZ%2B%2FNiYAugkWQcLgElGYYbCkyke6effVDObVuM0me7rd3fPnBYRY%2BpssV70ITf6LuxdRJjzj%2F1UgOb%2F%2F%2BD2egZo6qfQIZPMOWihr0GOqUBY509v55JOsz%2BJHkKb9lI8rYoOKJAHzML%2F4UPjLvpmZ4Z5qo%2B0%2FRckCrkvGmBw8Nw2n6IyYOcWFR04eE8znpk7WNkjIxCpzlTjvtbeFIEn6zHgcnldMt50lHLQl76tzetZWeC2jSamylqQPM7gdHWVfaijp8Gc0%2FpgD9ERoT%2BcFoqkZaxtwbGkoCPmhzHIGdrimYIMPnq0%2Byd%2BmurV9Jc5xESUfNP&X-Amz-Signature=ab1b1973672d6bee9b29de793a499a02738b2c2be39039962b49a99f9cb42763&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTTKSVB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCF8LJ8icQdozjbbeUV2u%2FBFIhTOcQgD%2FgApBmXY0Z9KQIgE%2FLFnUz%2BrRydTb%2Bxbrr5KhPL8fYY6uhw1HivPKa7VGMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJvnxEIVbNjHHu1plSrcA4X%2BCTwI4DjQxE2fNESsdRg50wwmR7WJF%2FqzSETVUmrzHfJwB84W85WYDaqkc2CDNs%2F5r1nDfvpKS0SzI%2B%2FTF4aZNQkseor4rw8hBDOXcD%2F3hAQiDEe9JbgtkKZxa6gIGOG%2F2pDQ5VWcnbS3Jd%2FffHMKztReUZxiNOSqa4xEGysLFtuUCTMknykr6v6f76DBo3pA01ujpyxhG3ITIk%2BmlO0vGQSvnff91d6c5TcvdEiHtaBmo%2BFimn%2FNKcXJUI4FvDnRtPtW%2FLL4pYv%2BrAnayPdtzoscVM3nyqx72ru%2Be3rmeHr%2B1Nx2WueVUU%2FS7KqGiDZ1R9O99JsZdS5mQUo0AMqqMSMt2HpWUv4cZrTtqXC%2FP6%2FDNSeW7sd7ubQZHkOQkRMvjxElifluCxYpatQ08RgM2Glu08ylw3wad%2BQTF1Yf1blNE9NLJ01bkNIG1ATftWTKmYH1imVON%2BlhjMUrAkmU3s0ihaWmBU64KuBThVV3oMqWvAGpR68uuPvjr8d6q8MQjUSUFbVXD5%2FLlsusE%2BNFNfwLMCpZ%2B%2FNiYAugkWQcLgElGYYbCkyke6effVDObVuM0me7rd3fPnBYRY%2BpssV70ITf6LuxdRJjzj%2F1UgOb%2F%2F%2BD2egZo6qfQIZPMOWihr0GOqUBY509v55JOsz%2BJHkKb9lI8rYoOKJAHzML%2F4UPjLvpmZ4Z5qo%2B0%2FRckCrkvGmBw8Nw2n6IyYOcWFR04eE8znpk7WNkjIxCpzlTjvtbeFIEn6zHgcnldMt50lHLQl76tzetZWeC2jSamylqQPM7gdHWVfaijp8Gc0%2FpgD9ERoT%2BcFoqkZaxtwbGkoCPmhzHIGdrimYIMPnq0%2Byd%2BmurV9Jc5xESUfNP&X-Amz-Signature=dd7f49472d1037bb82e76995e9043e7bf4484eec1fcf9f7fcd414cad73296136&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTTKSVB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCF8LJ8icQdozjbbeUV2u%2FBFIhTOcQgD%2FgApBmXY0Z9KQIgE%2FLFnUz%2BrRydTb%2Bxbrr5KhPL8fYY6uhw1HivPKa7VGMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJvnxEIVbNjHHu1plSrcA4X%2BCTwI4DjQxE2fNESsdRg50wwmR7WJF%2FqzSETVUmrzHfJwB84W85WYDaqkc2CDNs%2F5r1nDfvpKS0SzI%2B%2FTF4aZNQkseor4rw8hBDOXcD%2F3hAQiDEe9JbgtkKZxa6gIGOG%2F2pDQ5VWcnbS3Jd%2FffHMKztReUZxiNOSqa4xEGysLFtuUCTMknykr6v6f76DBo3pA01ujpyxhG3ITIk%2BmlO0vGQSvnff91d6c5TcvdEiHtaBmo%2BFimn%2FNKcXJUI4FvDnRtPtW%2FLL4pYv%2BrAnayPdtzoscVM3nyqx72ru%2Be3rmeHr%2B1Nx2WueVUU%2FS7KqGiDZ1R9O99JsZdS5mQUo0AMqqMSMt2HpWUv4cZrTtqXC%2FP6%2FDNSeW7sd7ubQZHkOQkRMvjxElifluCxYpatQ08RgM2Glu08ylw3wad%2BQTF1Yf1blNE9NLJ01bkNIG1ATftWTKmYH1imVON%2BlhjMUrAkmU3s0ihaWmBU64KuBThVV3oMqWvAGpR68uuPvjr8d6q8MQjUSUFbVXD5%2FLlsusE%2BNFNfwLMCpZ%2B%2FNiYAugkWQcLgElGYYbCkyke6effVDObVuM0me7rd3fPnBYRY%2BpssV70ITf6LuxdRJjzj%2F1UgOb%2F%2F%2BD2egZo6qfQIZPMOWihr0GOqUBY509v55JOsz%2BJHkKb9lI8rYoOKJAHzML%2F4UPjLvpmZ4Z5qo%2B0%2FRckCrkvGmBw8Nw2n6IyYOcWFR04eE8znpk7WNkjIxCpzlTjvtbeFIEn6zHgcnldMt50lHLQl76tzetZWeC2jSamylqQPM7gdHWVfaijp8Gc0%2FpgD9ERoT%2BcFoqkZaxtwbGkoCPmhzHIGdrimYIMPnq0%2Byd%2BmurV9Jc5xESUfNP&X-Amz-Signature=edc20f69a834d482503f6c16ae12d86c77a391f4ce559c3eec04f6241c2fe6f8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665W63O7S7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQDd7xhY%2FOkMsQ%2BCoYAu%2BhaTKUjyXOBAU0m%2BIBTWNWry%2FQIhAP4aRaLcMYAmLBhTjEiT9sF%2BcPXsLT73O2knbds25Xh2Kv8DCCUQABoMNjM3NDIzMTgzODA1IgwRtppnjcTYz9hg7j0q3AMQagjhsQ9Wy6iNEzBk1ID6AoYRdgA5F8bmg4gslCtnPmiE04mxqXq510CAVjoBAK8ZMhy%2Fk8GIJ%2FCF5gJFybuWtk6owl8kq3dHktPWXJa72Y1XtY5GKOZiKmGjn1ozfmWFmFcVgfQIPbELTSG2dOge85fPfwBRVtutpOR8syw7gwHZ7HMQeenj8eg4jo%2BazleQu53W%2B4fCqoxo3jDGqVegdmhc0G9s4eZ8C9CwlIql9cgieFb3h9%2BWzyQkL8v6pra6ZPT7BA1WcqL%2BH1yJXDW1vw4zdQ3joybGSGe2cZl0xOMeDExuJrJ6%2Fk62clki%2B1Yheu%2Bc5yl3793mY5Jw7%2FR4WvmH97vGK91zo0AnIRltCBlz89%2Fcc9%2FU1W%2BleL7bi5%2FsGPwOR0d6QUuUslfRNycxVFV1V9y%2FD5RNuuMvmZL9NlEU2WxBBN41FsQllThbOcqHupPRgh9H%2BDCLJsmvXNskH5HV3if1IegRNh7ZVN%2FeQkr%2FVEYfHgO6O%2F6OhlS8lDRsKC3XP6uxG75WZ4d8uCvLEaA2DRZIdEZ%2FoE7tEKu2AJYIJIXqcHZBkVHFD0p25ttHnm%2FNmbjKdxoTJah%2BVFQ6mqQFHmTKyN0GJYHmNsMgBI1hVGbN%2F6h9kHFmdTCMooa9BjqkAeKu%2B9NdTRtBovJfYS0zMH3CkpUy1BJOiQUjYFeU2els%2Fb7yA0kwT75YIDl%2FchBmMBE8iI0JIv1CbR1E1xx6Of0FoW%2FNzdhPIG8IFKUc9p58LNbgTkYvTO3NVj%2B0J5CZKdgdPzQZ%2F7RHz83WzEq%2FydJOa88YKRWe6S22FD1aqyogpFnZuL2eiGvH%2FFD4QI1uPiSCrJQaUJAShmdJXlHIp0MUbwx2&X-Amz-Signature=c23f251969dd5928c281a33b8df7579a3edded787486f33561b3a017bb8a2405&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFMIJCX4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCUSBiyN6D4RM2WJ4rMjq%2F7One%2B3uqSzrzV%2FLC2PcG9uwIgTufpegUCMwINDq8QswRLJeN1C6D7ylHf%2FST4HbBwlmUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDI4ope6qeLtwGyrptyrcAwP0b97d8s%2BjPXSUXu4ozBEObI7YGeGCHWSfAFApAfzx87giFc1XG6%2FgeNEmS%2B0bSVmYlh%2FZoU0SNyAHm0KRRqpf2tKwiJtBq1CcXg87%2Fgpy3BRcdhOLFmNINO44ScNNl52ojgNfFyQjJ3q7mTymcSZV4eXYZOdwC9%2B6bKxdqoba2kBxoP7LNVoLAUEc4iAo9XrNhCJ%2FBTCaS9JgwmmU2HzXs1O6LbQfu7SPT%2BOrC7T%2BFIS4xTp%2BIVJvsG1e6yyMnqS5W5Inkgmx2xd6QClxRWmphyk%2F6kF1SIpIJ3GX38sq10SvQ8jHTLb3tRyshQT8oONHUIcfwxn6D2VOUsVZ61tLrlC620PQ2QPaSML%2B3Ra7kCtMoZ0MrptfVCBqMZbf5Z9wxArFPNfRANtpgnyokT3ZomIZgEenSX3ZB%2BtnUftYX7SN2IZg34Te2rs8Dgc0E7xyYnP0Oiud0ezTgWLnX4bU%2FCoyrGS%2FYvXWwC0DMiG%2FwRrhC7CeLYgeqGVDNd%2BOSUkr47%2BZq%2BLIorwuIp%2Bg247XeyobsVUqk05w9e4PAzH%2Fvqygs0kFbCtAY4IO2zaPltxq1%2Fn9wyxPKu2EH79JEMD%2F5kT9S87ujnPUzWnPRZiktXMKrv4jOy7oPttdMI2ihr0GOqUB04KS%2FJWr3thtfzs48rJINFMBDkDRV%2F%2FHStKVbGaCRpckbKykixmwBvb3vVgnmdwzx55HCfB0Cy3A9SG1nA9PfeQj72OlgbAxIhuBF7XdmhdkQA1EdNc%2BToyZF74godjveh1gV2PGTOte6HQm%2Bl3X9nMLcq7yLM5UiN%2FL4hyTjiehJltyqaKt9k9P%2Bfre%2Fdp3zSRFPGo5VSnMIFERs17FsZ3ItBWH&X-Amz-Signature=9deba083373ac8dd64e38c4f7a79d81e9f43f65f06c9b98c74a2d85652c5b1cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTTKSVB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCF8LJ8icQdozjbbeUV2u%2FBFIhTOcQgD%2FgApBmXY0Z9KQIgE%2FLFnUz%2BrRydTb%2Bxbrr5KhPL8fYY6uhw1HivPKa7VGMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJvnxEIVbNjHHu1plSrcA4X%2BCTwI4DjQxE2fNESsdRg50wwmR7WJF%2FqzSETVUmrzHfJwB84W85WYDaqkc2CDNs%2F5r1nDfvpKS0SzI%2B%2FTF4aZNQkseor4rw8hBDOXcD%2F3hAQiDEe9JbgtkKZxa6gIGOG%2F2pDQ5VWcnbS3Jd%2FffHMKztReUZxiNOSqa4xEGysLFtuUCTMknykr6v6f76DBo3pA01ujpyxhG3ITIk%2BmlO0vGQSvnff91d6c5TcvdEiHtaBmo%2BFimn%2FNKcXJUI4FvDnRtPtW%2FLL4pYv%2BrAnayPdtzoscVM3nyqx72ru%2Be3rmeHr%2B1Nx2WueVUU%2FS7KqGiDZ1R9O99JsZdS5mQUo0AMqqMSMt2HpWUv4cZrTtqXC%2FP6%2FDNSeW7sd7ubQZHkOQkRMvjxElifluCxYpatQ08RgM2Glu08ylw3wad%2BQTF1Yf1blNE9NLJ01bkNIG1ATftWTKmYH1imVON%2BlhjMUrAkmU3s0ihaWmBU64KuBThVV3oMqWvAGpR68uuPvjr8d6q8MQjUSUFbVXD5%2FLlsusE%2BNFNfwLMCpZ%2B%2FNiYAugkWQcLgElGYYbCkyke6effVDObVuM0me7rd3fPnBYRY%2BpssV70ITf6LuxdRJjzj%2F1UgOb%2F%2F%2BD2egZo6qfQIZPMOWihr0GOqUBY509v55JOsz%2BJHkKb9lI8rYoOKJAHzML%2F4UPjLvpmZ4Z5qo%2B0%2FRckCrkvGmBw8Nw2n6IyYOcWFR04eE8znpk7WNkjIxCpzlTjvtbeFIEn6zHgcnldMt50lHLQl76tzetZWeC2jSamylqQPM7gdHWVfaijp8Gc0%2FpgD9ERoT%2BcFoqkZaxtwbGkoCPmhzHIGdrimYIMPnq0%2Byd%2BmurV9Jc5xESUfNP&X-Amz-Signature=a883f06a168a10a2438d1d013f70b2ab58e6b7163a2177db7483892afdfcac01&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTTKSVB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCF8LJ8icQdozjbbeUV2u%2FBFIhTOcQgD%2FgApBmXY0Z9KQIgE%2FLFnUz%2BrRydTb%2Bxbrr5KhPL8fYY6uhw1HivPKa7VGMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJvnxEIVbNjHHu1plSrcA4X%2BCTwI4DjQxE2fNESsdRg50wwmR7WJF%2FqzSETVUmrzHfJwB84W85WYDaqkc2CDNs%2F5r1nDfvpKS0SzI%2B%2FTF4aZNQkseor4rw8hBDOXcD%2F3hAQiDEe9JbgtkKZxa6gIGOG%2F2pDQ5VWcnbS3Jd%2FffHMKztReUZxiNOSqa4xEGysLFtuUCTMknykr6v6f76DBo3pA01ujpyxhG3ITIk%2BmlO0vGQSvnff91d6c5TcvdEiHtaBmo%2BFimn%2FNKcXJUI4FvDnRtPtW%2FLL4pYv%2BrAnayPdtzoscVM3nyqx72ru%2Be3rmeHr%2B1Nx2WueVUU%2FS7KqGiDZ1R9O99JsZdS5mQUo0AMqqMSMt2HpWUv4cZrTtqXC%2FP6%2FDNSeW7sd7ubQZHkOQkRMvjxElifluCxYpatQ08RgM2Glu08ylw3wad%2BQTF1Yf1blNE9NLJ01bkNIG1ATftWTKmYH1imVON%2BlhjMUrAkmU3s0ihaWmBU64KuBThVV3oMqWvAGpR68uuPvjr8d6q8MQjUSUFbVXD5%2FLlsusE%2BNFNfwLMCpZ%2B%2FNiYAugkWQcLgElGYYbCkyke6effVDObVuM0me7rd3fPnBYRY%2BpssV70ITf6LuxdRJjzj%2F1UgOb%2F%2F%2BD2egZo6qfQIZPMOWihr0GOqUBY509v55JOsz%2BJHkKb9lI8rYoOKJAHzML%2F4UPjLvpmZ4Z5qo%2B0%2FRckCrkvGmBw8Nw2n6IyYOcWFR04eE8znpk7WNkjIxCpzlTjvtbeFIEn6zHgcnldMt50lHLQl76tzetZWeC2jSamylqQPM7gdHWVfaijp8Gc0%2FpgD9ERoT%2BcFoqkZaxtwbGkoCPmhzHIGdrimYIMPnq0%2Byd%2BmurV9Jc5xESUfNP&X-Amz-Signature=6aaf4f82ebc06edeb51f8f9684dc0a2bccd2421b52b174087d15273e08d4e19e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTTKSVB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCF8LJ8icQdozjbbeUV2u%2FBFIhTOcQgD%2FgApBmXY0Z9KQIgE%2FLFnUz%2BrRydTb%2Bxbrr5KhPL8fYY6uhw1HivPKa7VGMq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJvnxEIVbNjHHu1plSrcA4X%2BCTwI4DjQxE2fNESsdRg50wwmR7WJF%2FqzSETVUmrzHfJwB84W85WYDaqkc2CDNs%2F5r1nDfvpKS0SzI%2B%2FTF4aZNQkseor4rw8hBDOXcD%2F3hAQiDEe9JbgtkKZxa6gIGOG%2F2pDQ5VWcnbS3Jd%2FffHMKztReUZxiNOSqa4xEGysLFtuUCTMknykr6v6f76DBo3pA01ujpyxhG3ITIk%2BmlO0vGQSvnff91d6c5TcvdEiHtaBmo%2BFimn%2FNKcXJUI4FvDnRtPtW%2FLL4pYv%2BrAnayPdtzoscVM3nyqx72ru%2Be3rmeHr%2B1Nx2WueVUU%2FS7KqGiDZ1R9O99JsZdS5mQUo0AMqqMSMt2HpWUv4cZrTtqXC%2FP6%2FDNSeW7sd7ubQZHkOQkRMvjxElifluCxYpatQ08RgM2Glu08ylw3wad%2BQTF1Yf1blNE9NLJ01bkNIG1ATftWTKmYH1imVON%2BlhjMUrAkmU3s0ihaWmBU64KuBThVV3oMqWvAGpR68uuPvjr8d6q8MQjUSUFbVXD5%2FLlsusE%2BNFNfwLMCpZ%2B%2FNiYAugkWQcLgElGYYbCkyke6effVDObVuM0me7rd3fPnBYRY%2BpssV70ITf6LuxdRJjzj%2F1UgOb%2F%2F%2BD2egZo6qfQIZPMOWihr0GOqUBY509v55JOsz%2BJHkKb9lI8rYoOKJAHzML%2F4UPjLvpmZ4Z5qo%2B0%2FRckCrkvGmBw8Nw2n6IyYOcWFR04eE8znpk7WNkjIxCpzlTjvtbeFIEn6zHgcnldMt50lHLQl76tzetZWeC2jSamylqQPM7gdHWVfaijp8Gc0%2FpgD9ERoT%2BcFoqkZaxtwbGkoCPmhzHIGdrimYIMPnq0%2Byd%2BmurV9Jc5xESUfNP&X-Amz-Signature=f447d3956f3936f82b9dc4a1ba72d539e69d248d7a159c7f84ca14c02fc93361&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YH6APROK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIH2v%2F2L563r5HXvc8pO6LwShoqPSf6Rb2YZVeCQHM3akAiBBO9IoKqc88xtXYpR9UtOrkROEX0q30q7C%2FTnneaexmir%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMcYjourH%2FdJfiksXAKtwDC44wyS0n6yeePrYm85gbf%2BEJWTl%2BebYu%2BiQQ5s38XdO1gZvt7KVthSpERtEYdQXktM2%2BScqLqmIy6fSZuHoO8MrhP%2FL3kXYQiIVhjCIazfs70e8mok3UNbzNP0opThrMoff1WU7WpFDKCvvzVUl%2BkXNSvT%2FHLzkjXhYZ4iiJrIVSLEs6sgzgCvvqrOmB3bBEOjVbHPbiEl5GaAB2j1iBVYPJ3%2FKmvyVBTQ7hRu%2BNdM%2B%2FXxXWVqzlIoqPUoC1ywQwUxteZh1Pn0qL5al%2FN1Fy6vs1gia%2FvANbneAgmvfaGtCBYffA%2FfYiTBel7QJG59lC5Gcb92A%2FaL7%2F6boCu4RQXvV0rEDFyoWItbX5SQiXwE%2BZr7dIyRDGIv89E%2F9B8UPB57UiiNxG%2FtdOfkdIHRHncfB3fmHp1O%2FOH%2BU60vVmitx%2BBZ0%2F%2FIoz0HbVz%2B%2B99hhW6tgnDJwCZJhzHWuehclFrTp5lllz3dEp786UEnBFFqKQc%2Br3vkSa%2BSbh3RyBP2x7%2FF7wP0SLK6dXwjMrlFjwdr9tQ2IGWmR6Xx61wOmgyklBtfOCEAfKhyGGoZoROCMG40C7uiuZBKCXsQmij1WBMr7CgA3vnJJSNBuznmUyZa8QvQmnhCwiu4fz4mYw7aGGvQY6pgGD87fdesQxMHDK%2F2yHw%2FDurWbvz3IricCatyOtxMwAPEQ81RE5gz%2FLerG7lw8RG3UtV4JxgWXEMQQKCjNYYtXDjLfB059N4crewgAxpWgGKKRJnx3puuUMYORtDnM1ciz98nXuLwaWEP%2FdEXfSW4mTIEGz3tAddE1tqsElKjiufcn1sUhWQ0bR5lXt9Jf3ksV9oXrpmGDgBAChLAnyoX0P7nsFDNvK&X-Amz-Signature=2ad653f13e82e296b78c9e89555310939fedc3b7658a46d275c9a2d2a528c1af&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BFUZFON%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIDrREQf%2BybXELxncBBN4dyteNXP%2FyUfnZ730EZe9y7bqAiEAxmnhTQFlu8RWp4cWLg6EYhLYzIAXsYY1EtI%2Bq86OjLYq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDP0FJD40aqRQ3I0fnCrcA9xOdKBJQk0nmxI6yxRPBU5FUQ%2FkPp4cA97AAWL4%2FTkOkj9clBqOyaF%2FEmfQa2Hz9nZ48MlVRs8W%2FtsTlRp0T9Mo%2Fy05y10vhLj4rWgz57498tvvqNrqNP7h8%2B2VExDPqE4KIPYR8VglS0UwKEL50tMP6V33FuZ6sizB%2FLXQVAUgmT8Al2MLYN%2F6j7FhetBEUlBhfIl3Cyh0TSPQ5MnPY9NmjK3a9Pvh%2BXl6Q0swsFdnh5Mz8hL7x%2BBbw2LhERRM7lG0G7orct%2FOX7zufGHsMVm4hj5qDj2rLD4wKeHBE80WETdD1FZavjhJiunbpYMEcRB%2FXN8EZEpQ4JYEC1uk2howtwRqfZ00iP2HMuuem30t53M9OVizWVfCCaE9Vpi%2BuU18a9gqNUjbVdwpeFNKqeqVgNI9AhjzNZekkEUq16cqBEpDX6nEvbCKqibaSGaZgU6jOfGORNwy3Gf2tz4Kbb%2Feu35463s0GBUBo04yc0Xy84ByqRT4%2BdgbAZKgDqthAN6CkvhZXqeY7qTfmiACJ211vIBDc0X5DFaA3D4SXhNMTyKP3uyPN1VgvjNYpkH%2ByNbxPjvQ6IgJRl5EtuHd2LGXbZ145G6LECUFBLb3EKycLWBnRrFiHyAHvZKcMIyihr0GOqUBbsRHq1OumnqZpA4rXMTh2SoeDykBtCbKwCq7cUjqKyQqu2xBzSxv9H%2Ba7ndINwHJnRt%2B%2FDUnbtPuP6AqPlXGPHy0kllqVToqPrxAUAZlQyLMpL5QdbeH80hUr1tAV9bLCPwMiIQi0fyP64afybaPqzRiH1wRtUIHUyiGOfk48WcLNSG2bmJ5VUjOJva1xlMRePU1og6zTvUpe%2BPKzUR8Pjxb9fBa&X-Amz-Signature=cfff93b7f726c3e218940db6aaa0e3d4ba85b9802a8b3fdda930d7641eb67b1b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LR6KNCP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIAZ4q6SDCK9OyXk1QIH1IXaE%2Bhe211YpfKYFqs%2FbSmknAiBzVBITYvXVr59D0y%2FRmohyxPvV0sZVzk%2BdQoVwjSZpfCr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMgeniUYp3Cje7gEoGKtwDHVb4%2Fh5oYX2G%2BMLnUZ9Wp4E2hHErNeGd6VimJL1fhEL%2FsU4qVHL5A9Jcmy4L%2FXS4%2BHJUR1IHzxF3iyc5xA8WEAFUthDr%2Bc%2F5vCcYuKkBMlQgb8TWgjVm%2B3uucLgPW0%2BBw4KomZPKielJCWTJe2LHFHafMS5g9q%2BnJnzvMG9qmlPrO6Q7GAqKjcRyJQ2mNc6rGEkqnDnMThCTWGIyEyx7s%2FgvLt8g1IoeIVoAX%2FrMSOBZ54LH6L1p1H1yrgV39qsbVwzLczWdEA%2FgrNSHIF9ReePkLM7KvUq4CnAxFA2dT2Sfu3OEMWEjVqkUWioQ2C%2BvHK2Fz9gW3nNLE4IPw07hPWQR75K8Bg7J%2BTyXDt84ClW6yqvEdeRGTlyS1o46EPWBmGMUB4bcjm57flubW1lmUEeeUyq4ii8DUaUlBK82CwHrKGbZbomOOwSaccDuY5TI3ld3bqkVng1tB7nET%2BbHaOhmYjHApul3svDnZf%2FzVUmqaEg0SY%2FAqhm2J%2F6xGG8BabBrZFF%2Fpo5fbKciZNcnIjHVTRSnz%2B5W1KEeOPrBXQ7gkXkuSbhpqaHOzcB%2F48j4aNT4fNb40GH8qI6Sn8V1yb%2BBjnD6G5MgDIxoy3DZO6JDEX8SmrqBsifJTaQwmaKGvQY6pgELOiKTcN1iUV7PxXK34yhhfl%2Fnm1uJ1zYapN4l24PA%2FiOdc%2BIeWfu4XtL7%2FWhgMgcGsb5AqKxlbAXuW%2FfhRRymN5zo8FqYGre%2FfEFuucsWXNrnfJd82MtAKcw%2BmNDpYGVPsHVubgIe56iO4MN0KJTXs7zzk4PfxA9VPa8saUtxzL1KD8TxkH0g16u5F3d1SJaN6Wk%2BC0%2FLhzLc4OdahxfGfztOrIkk&X-Amz-Signature=e82af9f43fce35317a04840b6c5cffe737957a9f316fe1d014e7ade9a2761274&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627OHN2NY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCID6PMxysY18s48rzklgYi2pfDk6v4H7xYTeQeee1nQpOAiA3FyBGv%2FlheZpX5XDwRRneJMoZ09JrAbzbfZVb6sMZRSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIM53OGcPnpqeCqWOQVKtwDckN6F85DOuTbY5%2FNiOhXg9PndOYJcTwNnL2AfBY2NQVDUDZlT%2Fysamwuiwmut8P8dE%2FUereQMbG2568QfuH7sYZmu3KoSya%2FW9UijCRHaw%2FjPBQGOP6dGEtcsAk%2BnGJ5u%2Fi58RyXlU%2FHAbpvD4mS8CFqvMgB%2B43XxifpS5VE9ephoIjnDCDzPAobjKn6uh%2B%2B4hckUozSFC%2FIDElJwNmnFeaKetV8HPtIAI6AV9M2lHknkEEFs8ggqT8mGE3gTc0c9j9Job1pLKWV3zqyfShFoOGY5jbYxAzEio3Fwd1B6OKG04Wwm1qohlTLXbc2CDoED80L7opjmf%2Bb7iV6WBVswOPHAOLi8edEeKn%2FMgqLsa3405V8ZNQTAZfgtNX95DuQlgRD3fcDtuB%2BEZHkicnWjdxOKNdyEPW8jwSON2qwRmMhKJlvK5Bwt2jE%2BdzhWiRAhGr4wYVHKEZq9GdMMcYLIdWSw6Gua%2FxSzU0q%2FzFB2zvha%2FWDnrOiGLjsADAMKvimqHzpqbUIOVtssC%2FtgCH5JNHgSHFWGrisTUdVBhkDzLpsQX0lP%2BrMwa8YAuVh4l9Fi6Q9dxe4kcFMSVKguu9h1sfEGkW0tZxVW%2BNrjqHLfCzv1%2F3cxYbQRprNMpswz6GGvQY6pgEcZcG6SKompCyR6ykmUXqFwfCahX6ETta4ZR8lznw3ti0QqgJcVycJbo2j2%2Bc7K5L3agGN2hfbx0XXe0h29MoWKoL000Y27%2BRDUteFIIqELXkygkDLgk22vtqnf%2F9GPUJtI1YNF5PiI7rzHbTqiBhn4Wx5OE6sh56F8XcS0YGuWwY%2Fzp6h6rTeLHuP%2BYqEdNhmtRz0B9yt29MsZKWLPs%2B3oJlhHDXB&X-Amz-Signature=50b362a3527611f86879b0eb3183f6a94d50500b9c38e6d15803643329c8ea14&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627OHN2NY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCID6PMxysY18s48rzklgYi2pfDk6v4H7xYTeQeee1nQpOAiA3FyBGv%2FlheZpX5XDwRRneJMoZ09JrAbzbfZVb6sMZRSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIM53OGcPnpqeCqWOQVKtwDckN6F85DOuTbY5%2FNiOhXg9PndOYJcTwNnL2AfBY2NQVDUDZlT%2Fysamwuiwmut8P8dE%2FUereQMbG2568QfuH7sYZmu3KoSya%2FW9UijCRHaw%2FjPBQGOP6dGEtcsAk%2BnGJ5u%2Fi58RyXlU%2FHAbpvD4mS8CFqvMgB%2B43XxifpS5VE9ephoIjnDCDzPAobjKn6uh%2B%2B4hckUozSFC%2FIDElJwNmnFeaKetV8HPtIAI6AV9M2lHknkEEFs8ggqT8mGE3gTc0c9j9Job1pLKWV3zqyfShFoOGY5jbYxAzEio3Fwd1B6OKG04Wwm1qohlTLXbc2CDoED80L7opjmf%2Bb7iV6WBVswOPHAOLi8edEeKn%2FMgqLsa3405V8ZNQTAZfgtNX95DuQlgRD3fcDtuB%2BEZHkicnWjdxOKNdyEPW8jwSON2qwRmMhKJlvK5Bwt2jE%2BdzhWiRAhGr4wYVHKEZq9GdMMcYLIdWSw6Gua%2FxSzU0q%2FzFB2zvha%2FWDnrOiGLjsADAMKvimqHzpqbUIOVtssC%2FtgCH5JNHgSHFWGrisTUdVBhkDzLpsQX0lP%2BrMwa8YAuVh4l9Fi6Q9dxe4kcFMSVKguu9h1sfEGkW0tZxVW%2BNrjqHLfCzv1%2F3cxYbQRprNMpswz6GGvQY6pgEcZcG6SKompCyR6ykmUXqFwfCahX6ETta4ZR8lznw3ti0QqgJcVycJbo2j2%2Bc7K5L3agGN2hfbx0XXe0h29MoWKoL000Y27%2BRDUteFIIqELXkygkDLgk22vtqnf%2F9GPUJtI1YNF5PiI7rzHbTqiBhn4Wx5OE6sh56F8XcS0YGuWwY%2Fzp6h6rTeLHuP%2BYqEdNhmtRz0B9yt29MsZKWLPs%2B3oJlhHDXB&X-Amz-Signature=1d8b44740f88f016f4a44aac1e429ebd1abcf9c672e5fc5413a50df4ab4f269a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
