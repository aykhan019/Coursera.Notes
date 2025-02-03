

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNM3U2IZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID4Gx8YPdLMySowFIuvORr5qmKTgRmHQfP0BjLkiEyF1AiADH3dS615ZloT1r%2F9prfRqXM6HRPvzkjT%2BDR1NzeZtbiqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtfcSaAFoSfGsrPdMKtwDk7v9pSwgKzw0MiGRNkE%2FO%2BgwKiKk2CHimNBBx1AnftG%2FBfvfZ9ax6woKfHENt4EA7MEGj%2FukZMXfz7yW4h9BPO5PvyfjrZQl84ecuTJl26TrNTJv4T%2BqmjUUupnSgpFEX6G7aDATOJbFsOW4hS6Sie90iUp7Aw5%2Baw27X2go2qLadrGwUyapwHzkmWMIzKoeb79Lanscqblp3OSSRyVgo5NNwwqkG%2FTcYno2Zz0mTeLl7gTtra9WkUdW9JjhncIKCmpZrR3axdfFvWv%2FT6mtTS0B2DuMSXWNws1QzNicaVnPIP8VxTF%2F%2Bx4TRuOKX8KAGLfWjG9b%2BG1UNHdkn%2FIH5gWxzQyxJKUB1ztZu7ofHT89EkiKto1X0TAggJKLOzFbJgsyp7%2B6yZi2wCRCWebOgsdNv0GyFzniZ%2Fmyhb%2F7WpqzUDRO4MnV3KSwikAoJz1NV1ZNVOyZnf61dxm84DE7BCz%2BbEJTBVy%2FuLEdrm01VaKkOwN5uG0DuKbuLIPKI01EjdQCSMJ7pDO6z9ApYsLDXKZFyfndxSPh0DzNHRo34VrrlScMYL%2F90zlPjwTXzMxS8UA80fIzMIzy9Dqa6oFUpo99uB%2BoKbPQr5EY6gwCmZsWeGRmc%2B3R6%2Ft1lFwwn7qBvQY6pgFGuuFqqoGpuvtsgBtKvYivPK0Qusu26lhRRfyrB39PoWvvKyU6O7WT1MwFamg5QAmA9BgkETBtx0PemC2yc7iaqBBZ%2BznxHpIZp29BDfBUttEmMDivavKe0NmTZ4ipfpJ%2F%2FmaeBP8nVcaGCB1RcxCxGyjSjXoG654PRXYAfeySGWABhQVsfh93LZ2V4JHvhCkxDg%2BbQYCcmQAs2%2FBGOTb27BtG4NWl&X-Amz-Signature=52aaec21f843b00ed21131cd7fec3739ee17f895b0d2a1940b22b1861d27912d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNM3U2IZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID4Gx8YPdLMySowFIuvORr5qmKTgRmHQfP0BjLkiEyF1AiADH3dS615ZloT1r%2F9prfRqXM6HRPvzkjT%2BDR1NzeZtbiqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtfcSaAFoSfGsrPdMKtwDk7v9pSwgKzw0MiGRNkE%2FO%2BgwKiKk2CHimNBBx1AnftG%2FBfvfZ9ax6woKfHENt4EA7MEGj%2FukZMXfz7yW4h9BPO5PvyfjrZQl84ecuTJl26TrNTJv4T%2BqmjUUupnSgpFEX6G7aDATOJbFsOW4hS6Sie90iUp7Aw5%2Baw27X2go2qLadrGwUyapwHzkmWMIzKoeb79Lanscqblp3OSSRyVgo5NNwwqkG%2FTcYno2Zz0mTeLl7gTtra9WkUdW9JjhncIKCmpZrR3axdfFvWv%2FT6mtTS0B2DuMSXWNws1QzNicaVnPIP8VxTF%2F%2Bx4TRuOKX8KAGLfWjG9b%2BG1UNHdkn%2FIH5gWxzQyxJKUB1ztZu7ofHT89EkiKto1X0TAggJKLOzFbJgsyp7%2B6yZi2wCRCWebOgsdNv0GyFzniZ%2Fmyhb%2F7WpqzUDRO4MnV3KSwikAoJz1NV1ZNVOyZnf61dxm84DE7BCz%2BbEJTBVy%2FuLEdrm01VaKkOwN5uG0DuKbuLIPKI01EjdQCSMJ7pDO6z9ApYsLDXKZFyfndxSPh0DzNHRo34VrrlScMYL%2F90zlPjwTXzMxS8UA80fIzMIzy9Dqa6oFUpo99uB%2BoKbPQr5EY6gwCmZsWeGRmc%2B3R6%2Ft1lFwwn7qBvQY6pgFGuuFqqoGpuvtsgBtKvYivPK0Qusu26lhRRfyrB39PoWvvKyU6O7WT1MwFamg5QAmA9BgkETBtx0PemC2yc7iaqBBZ%2BznxHpIZp29BDfBUttEmMDivavKe0NmTZ4ipfpJ%2F%2FmaeBP8nVcaGCB1RcxCxGyjSjXoG654PRXYAfeySGWABhQVsfh93LZ2V4JHvhCkxDg%2BbQYCcmQAs2%2FBGOTb27BtG4NWl&X-Amz-Signature=8e2469f45628cc3e0d7f847a8dce18a6803f6be56d0f5fe6d0b98e204c36cc8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNM3U2IZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID4Gx8YPdLMySowFIuvORr5qmKTgRmHQfP0BjLkiEyF1AiADH3dS615ZloT1r%2F9prfRqXM6HRPvzkjT%2BDR1NzeZtbiqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtfcSaAFoSfGsrPdMKtwDk7v9pSwgKzw0MiGRNkE%2FO%2BgwKiKk2CHimNBBx1AnftG%2FBfvfZ9ax6woKfHENt4EA7MEGj%2FukZMXfz7yW4h9BPO5PvyfjrZQl84ecuTJl26TrNTJv4T%2BqmjUUupnSgpFEX6G7aDATOJbFsOW4hS6Sie90iUp7Aw5%2Baw27X2go2qLadrGwUyapwHzkmWMIzKoeb79Lanscqblp3OSSRyVgo5NNwwqkG%2FTcYno2Zz0mTeLl7gTtra9WkUdW9JjhncIKCmpZrR3axdfFvWv%2FT6mtTS0B2DuMSXWNws1QzNicaVnPIP8VxTF%2F%2Bx4TRuOKX8KAGLfWjG9b%2BG1UNHdkn%2FIH5gWxzQyxJKUB1ztZu7ofHT89EkiKto1X0TAggJKLOzFbJgsyp7%2B6yZi2wCRCWebOgsdNv0GyFzniZ%2Fmyhb%2F7WpqzUDRO4MnV3KSwikAoJz1NV1ZNVOyZnf61dxm84DE7BCz%2BbEJTBVy%2FuLEdrm01VaKkOwN5uG0DuKbuLIPKI01EjdQCSMJ7pDO6z9ApYsLDXKZFyfndxSPh0DzNHRo34VrrlScMYL%2F90zlPjwTXzMxS8UA80fIzMIzy9Dqa6oFUpo99uB%2BoKbPQr5EY6gwCmZsWeGRmc%2B3R6%2Ft1lFwwn7qBvQY6pgFGuuFqqoGpuvtsgBtKvYivPK0Qusu26lhRRfyrB39PoWvvKyU6O7WT1MwFamg5QAmA9BgkETBtx0PemC2yc7iaqBBZ%2BznxHpIZp29BDfBUttEmMDivavKe0NmTZ4ipfpJ%2F%2FmaeBP8nVcaGCB1RcxCxGyjSjXoG654PRXYAfeySGWABhQVsfh93LZ2V4JHvhCkxDg%2BbQYCcmQAs2%2FBGOTb27BtG4NWl&X-Amz-Signature=e1f591220c5acb13c243a1645fe98d2dda4c756bc7584c16f31fff90327e8f77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRK4JHK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICE1AGAgQ478WZ7X7ljIhLFCIHT%2FyrEzIbZTqkWavuC9AiEApfkjZZiDVF%2BJ%2FT86cWaj8Ne4s21%2FdkFfzKSHxrV5RlMqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIJvbEZz6xn2V7yqCrcA6uaVVvTVQbdNCimz4E4Yl%2FnjbQe1fCa%2FDzvp5dj2G0ie6D%2BKlFJymOunBjfNcK9WeC1Vlt205fo55wzvIO9uZ%2FQCppJ6RDZINzMGHb9eDG%2Fan6vtUkPBrG6JVj8SlQcrPDZL9SOXW9vMy5Z2daiQy47XUZT3T2JT60OR1EmffF0uYOitoV5zHP78nHRRTaKa%2F0%2F6cQq%2FlSBnNRe4JYWPWe%2FOJuNuyvAnoOdPraRQLZWpNaNpbpFtYNKq%2B5AgzEHuNdho%2F8HA7bqyG7wR3k5g10aIBM4Eo83jCjdg1dAYrusbcNhxYj6KR8MZXtHejOUD71f9sIUkH52tW%2BxWTY3Z1byA2cvOWvtkMnZVjjjIZJ9mzf6JpxEj1DSKrOOFRGt5Lpudcvaoa6dUXt%2FdnhVtocJyRdHW7zhdQnp0PHIzOVfs4eJlAhJpByFMG10gVaODX5oFYryM6oIp%2FSzKAbIWLE4Q8MTgmvA7q2yWxcHcZdHX3LcUtFC4dPtIyZiKPUnHiupcx3qSTQg71%2FOxr2iQfDmjaLHn8g1asUCFyh2ajmJyx3Tt4O%2BwA5FxlyenyhN5GE1mW%2FnMVWS%2FuitFEn2rXFVHKo1Pag9BMn8p%2FLEiQecHuGsD1Jp0p2GXWCbMJW6gb0GOqUBx1hw%2BLKbcWrPZxUBtt2OZDEVuFyibNbigo6LFCP8td%2B5koB17DLkpyKGGRPLorI7Vew5Oa9NnYJS9oV0ivVmbcdXn5kNx49OJ%2BNR9QksRi7QLhEi%2Fok7utjhSfYAl5g30KN5y%2F%2FiAw6AEyKIRQy21EEh59gkfPKSvxoXRKC5N7qafcNoXelKfVOfq%2FPy9KcFCg3jQtF2hr1HuMPYbD%2BlmQxjIfRv&X-Amz-Signature=1387d5b37137b2118431c20047bea2bcbe73a5800d79a7befaa9e08806973e1e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRK4JHK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICE1AGAgQ478WZ7X7ljIhLFCIHT%2FyrEzIbZTqkWavuC9AiEApfkjZZiDVF%2BJ%2FT86cWaj8Ne4s21%2FdkFfzKSHxrV5RlMqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIJvbEZz6xn2V7yqCrcA6uaVVvTVQbdNCimz4E4Yl%2FnjbQe1fCa%2FDzvp5dj2G0ie6D%2BKlFJymOunBjfNcK9WeC1Vlt205fo55wzvIO9uZ%2FQCppJ6RDZINzMGHb9eDG%2Fan6vtUkPBrG6JVj8SlQcrPDZL9SOXW9vMy5Z2daiQy47XUZT3T2JT60OR1EmffF0uYOitoV5zHP78nHRRTaKa%2F0%2F6cQq%2FlSBnNRe4JYWPWe%2FOJuNuyvAnoOdPraRQLZWpNaNpbpFtYNKq%2B5AgzEHuNdho%2F8HA7bqyG7wR3k5g10aIBM4Eo83jCjdg1dAYrusbcNhxYj6KR8MZXtHejOUD71f9sIUkH52tW%2BxWTY3Z1byA2cvOWvtkMnZVjjjIZJ9mzf6JpxEj1DSKrOOFRGt5Lpudcvaoa6dUXt%2FdnhVtocJyRdHW7zhdQnp0PHIzOVfs4eJlAhJpByFMG10gVaODX5oFYryM6oIp%2FSzKAbIWLE4Q8MTgmvA7q2yWxcHcZdHX3LcUtFC4dPtIyZiKPUnHiupcx3qSTQg71%2FOxr2iQfDmjaLHn8g1asUCFyh2ajmJyx3Tt4O%2BwA5FxlyenyhN5GE1mW%2FnMVWS%2FuitFEn2rXFVHKo1Pag9BMn8p%2FLEiQecHuGsD1Jp0p2GXWCbMJW6gb0GOqUBx1hw%2BLKbcWrPZxUBtt2OZDEVuFyibNbigo6LFCP8td%2B5koB17DLkpyKGGRPLorI7Vew5Oa9NnYJS9oV0ivVmbcdXn5kNx49OJ%2BNR9QksRi7QLhEi%2Fok7utjhSfYAl5g30KN5y%2F%2FiAw6AEyKIRQy21EEh59gkfPKSvxoXRKC5N7qafcNoXelKfVOfq%2FPy9KcFCg3jQtF2hr1HuMPYbD%2BlmQxjIfRv&X-Amz-Signature=d49b29067ba3334c551c801b886e3cbf4279d1943a7b0643b1b221e61325e5ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRK4JHK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICE1AGAgQ478WZ7X7ljIhLFCIHT%2FyrEzIbZTqkWavuC9AiEApfkjZZiDVF%2BJ%2FT86cWaj8Ne4s21%2FdkFfzKSHxrV5RlMqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIJvbEZz6xn2V7yqCrcA6uaVVvTVQbdNCimz4E4Yl%2FnjbQe1fCa%2FDzvp5dj2G0ie6D%2BKlFJymOunBjfNcK9WeC1Vlt205fo55wzvIO9uZ%2FQCppJ6RDZINzMGHb9eDG%2Fan6vtUkPBrG6JVj8SlQcrPDZL9SOXW9vMy5Z2daiQy47XUZT3T2JT60OR1EmffF0uYOitoV5zHP78nHRRTaKa%2F0%2F6cQq%2FlSBnNRe4JYWPWe%2FOJuNuyvAnoOdPraRQLZWpNaNpbpFtYNKq%2B5AgzEHuNdho%2F8HA7bqyG7wR3k5g10aIBM4Eo83jCjdg1dAYrusbcNhxYj6KR8MZXtHejOUD71f9sIUkH52tW%2BxWTY3Z1byA2cvOWvtkMnZVjjjIZJ9mzf6JpxEj1DSKrOOFRGt5Lpudcvaoa6dUXt%2FdnhVtocJyRdHW7zhdQnp0PHIzOVfs4eJlAhJpByFMG10gVaODX5oFYryM6oIp%2FSzKAbIWLE4Q8MTgmvA7q2yWxcHcZdHX3LcUtFC4dPtIyZiKPUnHiupcx3qSTQg71%2FOxr2iQfDmjaLHn8g1asUCFyh2ajmJyx3Tt4O%2BwA5FxlyenyhN5GE1mW%2FnMVWS%2FuitFEn2rXFVHKo1Pag9BMn8p%2FLEiQecHuGsD1Jp0p2GXWCbMJW6gb0GOqUBx1hw%2BLKbcWrPZxUBtt2OZDEVuFyibNbigo6LFCP8td%2B5koB17DLkpyKGGRPLorI7Vew5Oa9NnYJS9oV0ivVmbcdXn5kNx49OJ%2BNR9QksRi7QLhEi%2Fok7utjhSfYAl5g30KN5y%2F%2FiAw6AEyKIRQy21EEh59gkfPKSvxoXRKC5N7qafcNoXelKfVOfq%2FPy9KcFCg3jQtF2hr1HuMPYbD%2BlmQxjIfRv&X-Amz-Signature=391fcc9fcaf4ff19b09c603646e08419de92283faf8b07a3749468b7da29e3a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRK4JHK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICE1AGAgQ478WZ7X7ljIhLFCIHT%2FyrEzIbZTqkWavuC9AiEApfkjZZiDVF%2BJ%2FT86cWaj8Ne4s21%2FdkFfzKSHxrV5RlMqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIJvbEZz6xn2V7yqCrcA6uaVVvTVQbdNCimz4E4Yl%2FnjbQe1fCa%2FDzvp5dj2G0ie6D%2BKlFJymOunBjfNcK9WeC1Vlt205fo55wzvIO9uZ%2FQCppJ6RDZINzMGHb9eDG%2Fan6vtUkPBrG6JVj8SlQcrPDZL9SOXW9vMy5Z2daiQy47XUZT3T2JT60OR1EmffF0uYOitoV5zHP78nHRRTaKa%2F0%2F6cQq%2FlSBnNRe4JYWPWe%2FOJuNuyvAnoOdPraRQLZWpNaNpbpFtYNKq%2B5AgzEHuNdho%2F8HA7bqyG7wR3k5g10aIBM4Eo83jCjdg1dAYrusbcNhxYj6KR8MZXtHejOUD71f9sIUkH52tW%2BxWTY3Z1byA2cvOWvtkMnZVjjjIZJ9mzf6JpxEj1DSKrOOFRGt5Lpudcvaoa6dUXt%2FdnhVtocJyRdHW7zhdQnp0PHIzOVfs4eJlAhJpByFMG10gVaODX5oFYryM6oIp%2FSzKAbIWLE4Q8MTgmvA7q2yWxcHcZdHX3LcUtFC4dPtIyZiKPUnHiupcx3qSTQg71%2FOxr2iQfDmjaLHn8g1asUCFyh2ajmJyx3Tt4O%2BwA5FxlyenyhN5GE1mW%2FnMVWS%2FuitFEn2rXFVHKo1Pag9BMn8p%2FLEiQecHuGsD1Jp0p2GXWCbMJW6gb0GOqUBx1hw%2BLKbcWrPZxUBtt2OZDEVuFyibNbigo6LFCP8td%2B5koB17DLkpyKGGRPLorI7Vew5Oa9NnYJS9oV0ivVmbcdXn5kNx49OJ%2BNR9QksRi7QLhEi%2Fok7utjhSfYAl5g30KN5y%2F%2FiAw6AEyKIRQy21EEh59gkfPKSvxoXRKC5N7qafcNoXelKfVOfq%2FPy9KcFCg3jQtF2hr1HuMPYbD%2BlmQxjIfRv&X-Amz-Signature=29da861687e09533c5998df16e68817a44de55d40398b34a8b2150ea45515b95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRK4JHK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICE1AGAgQ478WZ7X7ljIhLFCIHT%2FyrEzIbZTqkWavuC9AiEApfkjZZiDVF%2BJ%2FT86cWaj8Ne4s21%2FdkFfzKSHxrV5RlMqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIJvbEZz6xn2V7yqCrcA6uaVVvTVQbdNCimz4E4Yl%2FnjbQe1fCa%2FDzvp5dj2G0ie6D%2BKlFJymOunBjfNcK9WeC1Vlt205fo55wzvIO9uZ%2FQCppJ6RDZINzMGHb9eDG%2Fan6vtUkPBrG6JVj8SlQcrPDZL9SOXW9vMy5Z2daiQy47XUZT3T2JT60OR1EmffF0uYOitoV5zHP78nHRRTaKa%2F0%2F6cQq%2FlSBnNRe4JYWPWe%2FOJuNuyvAnoOdPraRQLZWpNaNpbpFtYNKq%2B5AgzEHuNdho%2F8HA7bqyG7wR3k5g10aIBM4Eo83jCjdg1dAYrusbcNhxYj6KR8MZXtHejOUD71f9sIUkH52tW%2BxWTY3Z1byA2cvOWvtkMnZVjjjIZJ9mzf6JpxEj1DSKrOOFRGt5Lpudcvaoa6dUXt%2FdnhVtocJyRdHW7zhdQnp0PHIzOVfs4eJlAhJpByFMG10gVaODX5oFYryM6oIp%2FSzKAbIWLE4Q8MTgmvA7q2yWxcHcZdHX3LcUtFC4dPtIyZiKPUnHiupcx3qSTQg71%2FOxr2iQfDmjaLHn8g1asUCFyh2ajmJyx3Tt4O%2BwA5FxlyenyhN5GE1mW%2FnMVWS%2FuitFEn2rXFVHKo1Pag9BMn8p%2FLEiQecHuGsD1Jp0p2GXWCbMJW6gb0GOqUBx1hw%2BLKbcWrPZxUBtt2OZDEVuFyibNbigo6LFCP8td%2B5koB17DLkpyKGGRPLorI7Vew5Oa9NnYJS9oV0ivVmbcdXn5kNx49OJ%2BNR9QksRi7QLhEi%2Fok7utjhSfYAl5g30KN5y%2F%2FiAw6AEyKIRQy21EEh59gkfPKSvxoXRKC5N7qafcNoXelKfVOfq%2FPy9KcFCg3jQtF2hr1HuMPYbD%2BlmQxjIfRv&X-Amz-Signature=1558467f7b42634f4ff4d0ee140bb9fdd8f56e641023147feac28906689e905b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRK4JHK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICE1AGAgQ478WZ7X7ljIhLFCIHT%2FyrEzIbZTqkWavuC9AiEApfkjZZiDVF%2BJ%2FT86cWaj8Ne4s21%2FdkFfzKSHxrV5RlMqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIJvbEZz6xn2V7yqCrcA6uaVVvTVQbdNCimz4E4Yl%2FnjbQe1fCa%2FDzvp5dj2G0ie6D%2BKlFJymOunBjfNcK9WeC1Vlt205fo55wzvIO9uZ%2FQCppJ6RDZINzMGHb9eDG%2Fan6vtUkPBrG6JVj8SlQcrPDZL9SOXW9vMy5Z2daiQy47XUZT3T2JT60OR1EmffF0uYOitoV5zHP78nHRRTaKa%2F0%2F6cQq%2FlSBnNRe4JYWPWe%2FOJuNuyvAnoOdPraRQLZWpNaNpbpFtYNKq%2B5AgzEHuNdho%2F8HA7bqyG7wR3k5g10aIBM4Eo83jCjdg1dAYrusbcNhxYj6KR8MZXtHejOUD71f9sIUkH52tW%2BxWTY3Z1byA2cvOWvtkMnZVjjjIZJ9mzf6JpxEj1DSKrOOFRGt5Lpudcvaoa6dUXt%2FdnhVtocJyRdHW7zhdQnp0PHIzOVfs4eJlAhJpByFMG10gVaODX5oFYryM6oIp%2FSzKAbIWLE4Q8MTgmvA7q2yWxcHcZdHX3LcUtFC4dPtIyZiKPUnHiupcx3qSTQg71%2FOxr2iQfDmjaLHn8g1asUCFyh2ajmJyx3Tt4O%2BwA5FxlyenyhN5GE1mW%2FnMVWS%2FuitFEn2rXFVHKo1Pag9BMn8p%2FLEiQecHuGsD1Jp0p2GXWCbMJW6gb0GOqUBx1hw%2BLKbcWrPZxUBtt2OZDEVuFyibNbigo6LFCP8td%2B5koB17DLkpyKGGRPLorI7Vew5Oa9NnYJS9oV0ivVmbcdXn5kNx49OJ%2BNR9QksRi7QLhEi%2Fok7utjhSfYAl5g30KN5y%2F%2FiAw6AEyKIRQy21EEh59gkfPKSvxoXRKC5N7qafcNoXelKfVOfq%2FPy9KcFCg3jQtF2hr1HuMPYbD%2BlmQxjIfRv&X-Amz-Signature=2a494f9b5a794945153e703977cd380256aaf33e20ea76b3f66e35d6076a96a2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQAADCRM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuKm0WC6XDit2DtFf8lRUyZ9yApI0%2B1WZVFnmsTGEy3wIhALSSL5tDg7x2fM8r8LuY1akOVI%2FZT7FFUSEkbt1RZ%2BEGKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuShj5Cuy1nuK3WrAq3AM37NuzSsa5YcmzDL8cBOFZbEc4fhpYBmzSBjmXUEpbJ5dH0fHdg0PwEnXduIqMHQBDm%2FKgDlmB2eEgP119mIIhpLKMXgb5MlrpriC7KF3GemUtT98T3mMjfRIOGCn4VZfcLg81OMUKU7piPAZcM0RfmVoeoLF6hwbaWU5WghDK%2BVe959FKAeKeNCyQBsXhaRjPY3Anfh8ApdTelgGx8VmU%2B7DOyeg88laTcSMAn5TRrS1uwMIv5l0%2B8cfHcs%2Fy9fMWaNeqIIc7evj86NDnobg4J%2BVhV4hM1PLoQWGyd4Ghg6RGkPQN4mazc35hqHngH%2BdTU0p9er6WlPHSUu76A%2F60r6Lc%2BjWidNIGGSZER7TnQh8lhsZePvYJKuHyGPDeh%2B6j9Sz0w6EG4Vr2SDQG24%2FAME9ymecPmkloAOxW77pg6ozMY6kAtEk9NnwXNDbO9jvUWoO7tEzo6fL%2FdyQ9f39HsblSxdnfRN0yzmaHWhRdVBdYXhpmO7w9dstrAS2RRXDvzTdvSuJEAUdKixMsvUx2uvnEF04kpmosM1d7g5Panm9hG2mjG%2BRDoxjAnr2SRopxaDLVhxA8ZBulooxi%2Fj3pzGK3vPSctSjT9y%2BWU%2FBKFFMiutMU9b6AiiBwDzD7uYG9BjqkAbqb2yfMh3Mq1QubrldBS8QqJhbUJJPj1X6PdDlNwP5vBMKS%2FOd2KLFtNnY6%2FSzhFx9cFUq5aFE9aH5oqXdqEXGnVB16rUiXHOq7%2F30uvjXQPhMmfA5kgadoVKxueWQG8Cj47lb4%2BA68ojDJVU2j%2FbU2hj0nGQ8uFbhAvbAq1be9VyRThh1EV6UOb34ZDmcTfA2B56izsGshmVqMGAelBEp3NU8o&X-Amz-Signature=a76953744030e1866eaa29e6e6afd58c43f7ef31eb1bfc2d5573c037ff493f5c&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCLJAYTA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHggMWbSeNCGpGzjrwJk%2BO8ZkAVd0a57cGJqc%2FHjZOlbAiEAzIrotAAa9s9p88A3npBSZxYKaFwgMUZfdrvj%2BKTQevwqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBymHAc%2B6MhSmsAU2ircA1JuXMT%2BEwOCRwD7C6aUwKm0%2F%2Bp%2FrBfxAT8p7P%2BP%2FUK7IhZ%2FZHAm2mx3vpRAp1y5AxGH82%2BFKCwiRbnsZ%2BChdElfS1XKEsGgtPzSaynjacchOPZvmiGpX3ZwBTh7el03NdFoLzhzLmuicnOr0rZOKVws8vJ%2BtWEVxhqou1ohqEtvTJZfnQfQwJO6KjSkkCyzqVx8vYSNfnodLVhN9PMpvenlodqHGF1gvd8pTtyobA%2FDjVREW4Fihp8khM2F6DfD586d4E7WG%2Fp6lmt6MjSqHVxG2Sau4p%2FMWENFD01BOF%2BcyGgzqpOa93h7ughYB9FPDNQv1N63RLJy1Kyx0a%2BDxYmczwCGGGWlpt4Hek%2BdCn29qw7qd98YmGhikQNlFVhM%2BB%2BqtRgW8Q6JOisld4S7W3TsxinSP809NdrAlZOrfsPid8gmTBo4PvUGLglIc9L08do%2FqsUs%2B8vL9fHsBh%2BksI8QmxLJgPFKAhX%2FdmLw9qryrYcLoJ4PM4nFMjMoz8r5WI9WOvVvVA2u19cudwAKfNrBfV4Mym7I9DCqut0GpPstjxrxLMcW4uibbrYxAZN2Z5Icf9Em1exBjcjKGeYyCh0dyUGqqpvAlRCfqzkf1OJ2uFdS7CvIzhO4J%2BvcMOi5gb0GOqUBbaresgRObxlZKwK6hLOBYKrfH4I2IATdf8w2I0B%2BrCy%2FtqIb5bQqmest%2FZS8CSUpQ0npMdu7XPWL5L0ewDE3uAiIrPlJCn%2FNobHieroO9T2PNd2zLd20yANfPmLct1YVPjq4ihGYSlo1uOXenQQ68gFgfjRP%2B4QTdNwSSYwLqrkg%2Bbj7PyWIaFhUkKg6ST%2FEgLQfB%2Bhj6EDKnl4NgGT%2BIF3K%2BnjG&X-Amz-Signature=fb4aef54f4b9efe8ec32dcf049c7d54e44608dc0e591862c3db62bf52e2b73dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRK4JHK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICE1AGAgQ478WZ7X7ljIhLFCIHT%2FyrEzIbZTqkWavuC9AiEApfkjZZiDVF%2BJ%2FT86cWaj8Ne4s21%2FdkFfzKSHxrV5RlMqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIJvbEZz6xn2V7yqCrcA6uaVVvTVQbdNCimz4E4Yl%2FnjbQe1fCa%2FDzvp5dj2G0ie6D%2BKlFJymOunBjfNcK9WeC1Vlt205fo55wzvIO9uZ%2FQCppJ6RDZINzMGHb9eDG%2Fan6vtUkPBrG6JVj8SlQcrPDZL9SOXW9vMy5Z2daiQy47XUZT3T2JT60OR1EmffF0uYOitoV5zHP78nHRRTaKa%2F0%2F6cQq%2FlSBnNRe4JYWPWe%2FOJuNuyvAnoOdPraRQLZWpNaNpbpFtYNKq%2B5AgzEHuNdho%2F8HA7bqyG7wR3k5g10aIBM4Eo83jCjdg1dAYrusbcNhxYj6KR8MZXtHejOUD71f9sIUkH52tW%2BxWTY3Z1byA2cvOWvtkMnZVjjjIZJ9mzf6JpxEj1DSKrOOFRGt5Lpudcvaoa6dUXt%2FdnhVtocJyRdHW7zhdQnp0PHIzOVfs4eJlAhJpByFMG10gVaODX5oFYryM6oIp%2FSzKAbIWLE4Q8MTgmvA7q2yWxcHcZdHX3LcUtFC4dPtIyZiKPUnHiupcx3qSTQg71%2FOxr2iQfDmjaLHn8g1asUCFyh2ajmJyx3Tt4O%2BwA5FxlyenyhN5GE1mW%2FnMVWS%2FuitFEn2rXFVHKo1Pag9BMn8p%2FLEiQecHuGsD1Jp0p2GXWCbMJW6gb0GOqUBx1hw%2BLKbcWrPZxUBtt2OZDEVuFyibNbigo6LFCP8td%2B5koB17DLkpyKGGRPLorI7Vew5Oa9NnYJS9oV0ivVmbcdXn5kNx49OJ%2BNR9QksRi7QLhEi%2Fok7utjhSfYAl5g30KN5y%2F%2FiAw6AEyKIRQy21EEh59gkfPKSvxoXRKC5N7qafcNoXelKfVOfq%2FPy9KcFCg3jQtF2hr1HuMPYbD%2BlmQxjIfRv&X-Amz-Signature=97ff02643452582607432541cfd26f6c2e5effb4428ee38b5841027555f9b6c7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRK4JHK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICE1AGAgQ478WZ7X7ljIhLFCIHT%2FyrEzIbZTqkWavuC9AiEApfkjZZiDVF%2BJ%2FT86cWaj8Ne4s21%2FdkFfzKSHxrV5RlMqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIJvbEZz6xn2V7yqCrcA6uaVVvTVQbdNCimz4E4Yl%2FnjbQe1fCa%2FDzvp5dj2G0ie6D%2BKlFJymOunBjfNcK9WeC1Vlt205fo55wzvIO9uZ%2FQCppJ6RDZINzMGHb9eDG%2Fan6vtUkPBrG6JVj8SlQcrPDZL9SOXW9vMy5Z2daiQy47XUZT3T2JT60OR1EmffF0uYOitoV5zHP78nHRRTaKa%2F0%2F6cQq%2FlSBnNRe4JYWPWe%2FOJuNuyvAnoOdPraRQLZWpNaNpbpFtYNKq%2B5AgzEHuNdho%2F8HA7bqyG7wR3k5g10aIBM4Eo83jCjdg1dAYrusbcNhxYj6KR8MZXtHejOUD71f9sIUkH52tW%2BxWTY3Z1byA2cvOWvtkMnZVjjjIZJ9mzf6JpxEj1DSKrOOFRGt5Lpudcvaoa6dUXt%2FdnhVtocJyRdHW7zhdQnp0PHIzOVfs4eJlAhJpByFMG10gVaODX5oFYryM6oIp%2FSzKAbIWLE4Q8MTgmvA7q2yWxcHcZdHX3LcUtFC4dPtIyZiKPUnHiupcx3qSTQg71%2FOxr2iQfDmjaLHn8g1asUCFyh2ajmJyx3Tt4O%2BwA5FxlyenyhN5GE1mW%2FnMVWS%2FuitFEn2rXFVHKo1Pag9BMn8p%2FLEiQecHuGsD1Jp0p2GXWCbMJW6gb0GOqUBx1hw%2BLKbcWrPZxUBtt2OZDEVuFyibNbigo6LFCP8td%2B5koB17DLkpyKGGRPLorI7Vew5Oa9NnYJS9oV0ivVmbcdXn5kNx49OJ%2BNR9QksRi7QLhEi%2Fok7utjhSfYAl5g30KN5y%2F%2FiAw6AEyKIRQy21EEh59gkfPKSvxoXRKC5N7qafcNoXelKfVOfq%2FPy9KcFCg3jQtF2hr1HuMPYbD%2BlmQxjIfRv&X-Amz-Signature=b11f96a54f8d7211ccadabfe27f3c978c4a80b590fe95077b4c182c61485b484&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRK4JHK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICE1AGAgQ478WZ7X7ljIhLFCIHT%2FyrEzIbZTqkWavuC9AiEApfkjZZiDVF%2BJ%2FT86cWaj8Ne4s21%2FdkFfzKSHxrV5RlMqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIIJvbEZz6xn2V7yqCrcA6uaVVvTVQbdNCimz4E4Yl%2FnjbQe1fCa%2FDzvp5dj2G0ie6D%2BKlFJymOunBjfNcK9WeC1Vlt205fo55wzvIO9uZ%2FQCppJ6RDZINzMGHb9eDG%2Fan6vtUkPBrG6JVj8SlQcrPDZL9SOXW9vMy5Z2daiQy47XUZT3T2JT60OR1EmffF0uYOitoV5zHP78nHRRTaKa%2F0%2F6cQq%2FlSBnNRe4JYWPWe%2FOJuNuyvAnoOdPraRQLZWpNaNpbpFtYNKq%2B5AgzEHuNdho%2F8HA7bqyG7wR3k5g10aIBM4Eo83jCjdg1dAYrusbcNhxYj6KR8MZXtHejOUD71f9sIUkH52tW%2BxWTY3Z1byA2cvOWvtkMnZVjjjIZJ9mzf6JpxEj1DSKrOOFRGt5Lpudcvaoa6dUXt%2FdnhVtocJyRdHW7zhdQnp0PHIzOVfs4eJlAhJpByFMG10gVaODX5oFYryM6oIp%2FSzKAbIWLE4Q8MTgmvA7q2yWxcHcZdHX3LcUtFC4dPtIyZiKPUnHiupcx3qSTQg71%2FOxr2iQfDmjaLHn8g1asUCFyh2ajmJyx3Tt4O%2BwA5FxlyenyhN5GE1mW%2FnMVWS%2FuitFEn2rXFVHKo1Pag9BMn8p%2FLEiQecHuGsD1Jp0p2GXWCbMJW6gb0GOqUBx1hw%2BLKbcWrPZxUBtt2OZDEVuFyibNbigo6LFCP8td%2B5koB17DLkpyKGGRPLorI7Vew5Oa9NnYJS9oV0ivVmbcdXn5kNx49OJ%2BNR9QksRi7QLhEi%2Fok7utjhSfYAl5g30KN5y%2F%2FiAw6AEyKIRQy21EEh59gkfPKSvxoXRKC5N7qafcNoXelKfVOfq%2FPy9KcFCg3jQtF2hr1HuMPYbD%2BlmQxjIfRv&X-Amz-Signature=0cfb16bd2907cd3c14dea5829f7c947b0cbc3c515fa30b4dbda83427e9847b64&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT2C5XXL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCo605r0cwSD1cZexfRCSqXpHQx44sgKoVp2JqNOz3WeAIgDhvjOx4uqPOTUPX1ie9uQvnXqmDO3HLjQMZNkaVPjYcqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLjAOb1%2ByXZKRpNmQyrcA%2BCV4iq%2Fmr5qgNKqVjxtz8jgBQcdcRRBE9oTV2DNjKz9ec2t%2FHmb7vm%2FJmBT9%2BMeaisN%2FDZsIqufeu21s0ODrglWYeh5DCf8M2QXDZti4oLpYDaNJj%2FMURKBEyQDFPKP%2FGMLu5MtEV8Qz0JQfPLcdoykszUWgYpPMOXHydO4jJE%2FgoaVsyczndf1wxfGe7sZytUNSJk3Lr2hIYEXICrgw66mYbH%2BWaRIIW1wG96gUFDmipz8InQ5fvHGDpKMDPmHMMjTd7WtIv6BC0WINetybUdUHl7r5UlrQ2DwFJok%2BVOps4MLCJPvq4HWWli5FtLMDWKlnwMYQir%2FTdz6eFzNDiHYFETojDpdCscIXiukNOLXr02p7pBP0U4w0gxTDm%2FEpcn7hzfmc5NNuBpaoK56dZjKsrwi4N1Wb8mCs3ZcuDnT%2FxAvY1nriOBizShJ%2BkDQqKy0I9wwel3IiXEk9RpPlfDQvhZvTWN7VqBoyAjkwqUKmJIY0S3BsnWYLgiTiNUeFKlmrwVjXx5i0yNHL58%2FOHKZS7K27FbdeP4pnVRTEIPaKXEYFsB8K%2Bdq%2BL6iYMEcGaHNFZc5i4Jo%2FHgSQnCsXQYBdxvV3pPmzREGb1tbLmBbdsblXVw8Nm3Sz8TMMJO6gb0GOqUBlTKbp3G4R6qXi5kz9hob57fDE83e61PxGAmwUkuQ3BTLPnS3J%2FoG%2FQFVpCuQWbJxVgHzk0zKmxF%2FAn04SsOyrPTEdGfPqkm3gQdmFJGL73%2F8TItmTpA81KSD1QhzvnQ%2BCzMP7VwBySSVfVkpM%2FzTa%2F%2FTZoAY18vDzUv5g%2BA5zcOf2v01tBPtnd3AvNeJszgyONLq%2FC%2BkofHUXmEb%2BTlqLIhmaenu&X-Amz-Signature=22a774e0ab751c9f960f464d9b9a45de079000f46ee5a1f1ccb4435562650656&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QD7J6JZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF468Xw7lkwl8jZ0FzWtJTjV3doIpYLTZ4qXs6wBscYvAiEAocFr4HVdeB04asz680%2FdB%2B56F%2FdkMsNcA10BlTYM2bwqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOThGdreYt88cN%2FuaCrcA7rXPaM2ZnshXIrXyfUkllA6GiKTt5IisEOqkyjSZfuvCMuPfMDWVytXpcctiUMVqSGNmMfdXhyYuWoMuD%2Fhi9XgQK5wTlPz895U%2Fkd42ywIm1QsE6Dv%2BqGfPo4lQT%2FQY%2BF26lYMIIf1%2BRM%2Bq0lBK7AWDIBV7uO7V2c2cCpnqPvLUwlrYtXPfx3pl4cNglvoHdfCsl1IPt%2F%2BAE7TFrlLGLsaxS8aUVywbP8ssosVCMJHcjuuETpKRB6U0fLGo4suRlbzRF%2FmRh9NEKojbdTiSVUlMKEY5IJV8uzUZsv1tpomXxqyAfqrH89zsAIc3r8CtT%2B72HUkTRAQq2Z6e4LeLWVlncyk5L8T9Z0RIKLnbFsJxoEIBl%2FOjDOVGbFxAWd%2B9WAjiZVSDrNGhGYGD%2BWzSs6c5aY7sFG2ZkmdiOFTRQeYX6j9Fpm8p2Vewi4hIlzf%2BpnEdRJyY35M05w7BCCI88uu45Dz49mUTT6GMRC4qpNrYW5%2BGWOBj1YDEt5BtNvdWuiYyYX0QDrf6g%2Fg1JHFEllC%2BbXJ4RsUzs3%2B%2BDpZNKb2HoXKPeMUz2VUIVYHiJT1lzqAS1Yi6Np7my2st2wQQFec0nKCnJ0715mzC2hBkRBJaNVD%2B6hjBwC4fqbKMM26gb0GOqUBfrC7LRj1cLb7zyKiIQFvSYWwlIUkynaqJgXngxD69uY6gqxW3bP1G5x97yyqsWNaEpOsJxN6L1EHT52BEzkW8LFEQlch4mCXdlZH7LuHHGp%2B09mEYo9cnIlGgk1nn8LBzGgaWPSiByDz1M3JVdPNFGL7qSVlN495vs1T%2BhkyEJ%2FJ1x8ZUtuoW8SSMXJ5uHDThIs9wav9NovHLh3fZ96wD8KxXNUU&X-Amz-Signature=80d0ec25bdd0111ae05e83acaea03cc520d09f8f9b26d024f68779887b0e559d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOVLCZ6N%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFnEtBvth7zTsZC8EmhgmgfOPVb1iaeul%2Furmwk2Ykx%2BAiBSosObtA1ldq3ZeE8pN%2BirTyYwuFHw8lV01c5xda2kKSqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBBoJSkZM8w%2FekIwAKtwDGSeOWPpujrHBpEoBLWABRajIP9%2FPJG7W6jrt59V%2F4I0tS8WH9k8ZzdYDfKuN%2BCaC6O5FlPzCQcKvuGzeBBwgh0g43BXd6kiAdDssPd0j1xoZ%2BcLGr9aYyy9dv84MvCz5CCFI1MQHJhsVwoOMkiq8gd1ULO7Rgw7HLMIkNqhn0RKlHN4sQzq4w4kBvIt%2BGPSy39V5etYXyNPYaYaaOWqSSMo9Bmt56ZzZswdc5Q0k2B6x%2B0rf6FrwpIPfStyUPhIs1oTScww7dRSSyowV1HQHP9AHJ6iACivlklUBmlCyfzaSb4KELbJDiV%2FZEb9TCYyvHRBlPVGlBlaOxSx4ebf5kcBA5Pe24vRwncbpXuc2tcguyzwrCGPAIC9MWBFN0BgAeEVTcKvwkrQy7%2FJRsAfnKmI%2Bdj8NAF0p5jwYkx8XuJ2JTN86OWnai7mYNQTFmzj804Arwv5ls2AQyGJDNS1s41W5A7tch1WBg3wwM1rViBadX2PvVuoREC%2BN3ojpHBXHOWMCgiDbCbMQ0427qFjoQk%2BXAla3XzjpPfxfiVodaamLLQcpwWeMEjBhVz%2BTIxsd99YLnZktADL24el9BIb%2BKp8LTfvuxXDn7xOsxj6rtOxrfciuh7tbOlCobTUwh7qBvQY6pgGIbemP7uGs0PE7%2BQPm2DkiMJYo34xl%2BMz5N30lZPAolMw0xG5t%2Bdbw%2Bvv%2FlEnnHn2qCJq3Am7%2B8ayanucAT1Bn4rNBOLmCWC%2Bu1bS8NsHHCAeT%2BlooLdC8lXa%2BLczvovJqEE2yZSjf%2BNUrGzwvPY1tp8ZXsb%2F%2Fs%2FfXMQdaQy%2BkHfvxkNWFUc%2BJUkslUzVh11i9rsvtaM5MFeWBxYgc0q9a7HDW455m&X-Amz-Signature=35727e5517b6bd4a471669e1c794850841ee092ee51d997073f5dbac2dfdc96c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOQWUKNF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6Cle074i1d4vJ6zCMJ1EohBSZd2z5OVT1Tg%2FqLXQo0gIhAON9qOS4Mmy12D4DsBzaDs%2FtjUMM0wNUDxRP%2F8WMKYQEKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySZAJe3qDtbeKP1bwq3ANUNRj6ERdDzwDUDD9%2BM3QzN98SpZlSAPOaCxFlM1bE6KYWm6jkSaHw8U6%2FT%2FKHR5xEegI0YcGz8Ab0ytSiNCxMeCgAZpycHJGsKdEi6exHQ83vwBYXy0dhmx6a2Fp%2FbJl73OCqRM3Tpmp6rsqyu1SChAYulb41iUkqRL3cdirSrPnPTcDQuabTnJrtb%2F3Y%2BNyoo0cEFX0Lxzz%2BSxJ%2Bsl0aQGzjDfgtKPfsID0jZvq2lC4Jr%2BrvRigo9PdhsKrvs9v3lB4vu%2FSNoj84DX%2BKayFopumWg%2FWMzyo0aTuEaNa8bgQqtFnHHWNe0bz5Ojhd%2B1JfiH4Lo4DnxETZPo%2FO%2BBNsCS5pZ5s9EScg2Uab1sEkcVsETJ5AiXwozrYj09CMnDMEjUYUWY0IPwuDrz04T%2Fvy3C1gwR5MQfykFcP0HSrlq0isSRaruzPa20fbagFYsHLgh1EuR0jP799tUE8mohIa6%2BCHnB7sb52iDlTrjkv%2FxoHtoYwUcU%2F0ricgbGvRdv2qZjpgEc417zS2ufw6%2F4JmbIFzU202mdSV8npVJIEOB%2Fpx1CjlUyG%2FsYDQtpyMnA%2FN9%2FkueqxPrVbNCtgvonlCAglxtcwZiDeevKWmycWwJHUa6D5KVw1zgooglDDeuYG9BjqkAULFbhMcONi0c8FOEX1mP%2BIblOdOuMDbUnUA%2FI4EB2SL2C7FZTx64cMQuIyYRFNccQUDx1wXpRYhRI6tuX9ws9QvcvnaoxCj%2FEVMTEuT%2By86JF%2FGi%2FaETYA6hX7yr4o7VX%2Bn%2BJMSANnQMfC43JqWg5tj2iwPjPC04HxaQ11pEeo6CQDa7Bw6%2BW5i2%2BASvVsbG4RTXbZ4xKvUPtJm%2BwEY82LnXuQ0&X-Amz-Signature=9a189db349e884071ad15736465c632d68fecfb7b5a7e89c34a9c713c578418d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOQWUKNF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6Cle074i1d4vJ6zCMJ1EohBSZd2z5OVT1Tg%2FqLXQo0gIhAON9qOS4Mmy12D4DsBzaDs%2FtjUMM0wNUDxRP%2F8WMKYQEKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySZAJe3qDtbeKP1bwq3ANUNRj6ERdDzwDUDD9%2BM3QzN98SpZlSAPOaCxFlM1bE6KYWm6jkSaHw8U6%2FT%2FKHR5xEegI0YcGz8Ab0ytSiNCxMeCgAZpycHJGsKdEi6exHQ83vwBYXy0dhmx6a2Fp%2FbJl73OCqRM3Tpmp6rsqyu1SChAYulb41iUkqRL3cdirSrPnPTcDQuabTnJrtb%2F3Y%2BNyoo0cEFX0Lxzz%2BSxJ%2Bsl0aQGzjDfgtKPfsID0jZvq2lC4Jr%2BrvRigo9PdhsKrvs9v3lB4vu%2FSNoj84DX%2BKayFopumWg%2FWMzyo0aTuEaNa8bgQqtFnHHWNe0bz5Ojhd%2B1JfiH4Lo4DnxETZPo%2FO%2BBNsCS5pZ5s9EScg2Uab1sEkcVsETJ5AiXwozrYj09CMnDMEjUYUWY0IPwuDrz04T%2Fvy3C1gwR5MQfykFcP0HSrlq0isSRaruzPa20fbagFYsHLgh1EuR0jP799tUE8mohIa6%2BCHnB7sb52iDlTrjkv%2FxoHtoYwUcU%2F0ricgbGvRdv2qZjpgEc417zS2ufw6%2F4JmbIFzU202mdSV8npVJIEOB%2Fpx1CjlUyG%2FsYDQtpyMnA%2FN9%2FkueqxPrVbNCtgvonlCAglxtcwZiDeevKWmycWwJHUa6D5KVw1zgooglDDeuYG9BjqkAULFbhMcONi0c8FOEX1mP%2BIblOdOuMDbUnUA%2FI4EB2SL2C7FZTx64cMQuIyYRFNccQUDx1wXpRYhRI6tuX9ws9QvcvnaoxCj%2FEVMTEuT%2By86JF%2FGi%2FaETYA6hX7yr4o7VX%2Bn%2BJMSANnQMfC43JqWg5tj2iwPjPC04HxaQ11pEeo6CQDa7Bw6%2BW5i2%2BASvVsbG4RTXbZ4xKvUPtJm%2BwEY82LnXuQ0&X-Amz-Signature=c2d360b64a313c29a7a1cdce39b1f51f16589eafaa60636343f8df54d6dda29e&X-Amz-SignedHeaders=host&x-id=GetObject)

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
