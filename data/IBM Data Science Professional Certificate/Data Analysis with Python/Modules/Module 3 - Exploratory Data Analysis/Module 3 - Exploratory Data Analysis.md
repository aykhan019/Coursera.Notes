

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3CQPUC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCULb50x9MCfCpG92X9DBb194s6rBzv%2FFw%2F5bSZwpsmBAIhAIFxAMjVXjJiAi7V2afCYeteHntAxqTACrw4IuqcMu9zKv8DCBQQABoMNjM3NDIzMTgzODA1IgxbzgTzhYEjyfTtQhEq3APR%2Fueu6L9pFgcFdL8dunVhD8%2FbNj9z%2FU10V4AQxPwRCRRTVVoPC%2BNEFGNRZmr5cpSyEciWHrZrf8JYN03QmWYHWMcXJZL%2BE3p2mWxoo7aymkIK6PqcaRkjHqsf35SiXRBVb2f22lO0wxPSdD9cY1QBlDkmkmJgOpjweqh6xkGXcoOZHubV81j%2BWnFCpXu04BytzmWzXjTrqJJfEcJCD6jhdtl5%2BX%2Bk5GistXL1Ra3oIbbRFgTC6IGBCuC5UG3DQGsnktvKF9%2F5%2FAFaauK5UY2hulIuSdKDQt7RIMZHsG%2Bh3HrDcehvYENGKnfOSU9f5PzsAHYXGUj%2F1gsF8va73zB8p2jwooH0bWp%2Fx9xKyTrba7%2F5eWrO4cjEzUeIzlHvRTOcix5sf8M7Hk0EqRKawqiigXXyw6Cm2JhOf%2FesqCK90PVmY7rrHyCuW048PBLFrBaPtmpQYKMUNLv%2BSq4ENZkIN9LO6knOAbgAfbLzGWM6n%2FAkKyzHHv21WLYpQ8gzLo%2BoMqA0Aky736mhwBPt8MYLU%2FhCwkHUEGf7b6m0s7L3PUCbxOOG3fGa2EBJZrDcQVRT4bZpdy9YCgVAJfEhD1CRSOvHYBWq%2B2trTv2ENCV7LU4gSRNILAPnk5TqITDh0oK9BjqkAZJiYf9E0Pb5Xxln8m%2B22ZpH37vrUEBb2bKHRJLoo2c9Ocz2Cc2Dd9t2DxxqIo6%2FOOH1F8hGjuHQ5HdLrE9JSDFp5SnsqAqclHcI7QO4cOnPyiAwczMo5CpXQ%2BvX0xSb7LGHi7gK7sO3zFKqsEK3%2Fu6DrZ8LiHpZGair5kjFT%2BSoO8NFD%2BxpbdVodR6BrG%2B98J0HcyRVyF9iydVnKCSgtre5RW43&X-Amz-Signature=a0cf0996c411bdd7fd7dbe426174c17fba60b6d9632037fdeda1c286c57e362a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3CQPUC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCULb50x9MCfCpG92X9DBb194s6rBzv%2FFw%2F5bSZwpsmBAIhAIFxAMjVXjJiAi7V2afCYeteHntAxqTACrw4IuqcMu9zKv8DCBQQABoMNjM3NDIzMTgzODA1IgxbzgTzhYEjyfTtQhEq3APR%2Fueu6L9pFgcFdL8dunVhD8%2FbNj9z%2FU10V4AQxPwRCRRTVVoPC%2BNEFGNRZmr5cpSyEciWHrZrf8JYN03QmWYHWMcXJZL%2BE3p2mWxoo7aymkIK6PqcaRkjHqsf35SiXRBVb2f22lO0wxPSdD9cY1QBlDkmkmJgOpjweqh6xkGXcoOZHubV81j%2BWnFCpXu04BytzmWzXjTrqJJfEcJCD6jhdtl5%2BX%2Bk5GistXL1Ra3oIbbRFgTC6IGBCuC5UG3DQGsnktvKF9%2F5%2FAFaauK5UY2hulIuSdKDQt7RIMZHsG%2Bh3HrDcehvYENGKnfOSU9f5PzsAHYXGUj%2F1gsF8va73zB8p2jwooH0bWp%2Fx9xKyTrba7%2F5eWrO4cjEzUeIzlHvRTOcix5sf8M7Hk0EqRKawqiigXXyw6Cm2JhOf%2FesqCK90PVmY7rrHyCuW048PBLFrBaPtmpQYKMUNLv%2BSq4ENZkIN9LO6knOAbgAfbLzGWM6n%2FAkKyzHHv21WLYpQ8gzLo%2BoMqA0Aky736mhwBPt8MYLU%2FhCwkHUEGf7b6m0s7L3PUCbxOOG3fGa2EBJZrDcQVRT4bZpdy9YCgVAJfEhD1CRSOvHYBWq%2B2trTv2ENCV7LU4gSRNILAPnk5TqITDh0oK9BjqkAZJiYf9E0Pb5Xxln8m%2B22ZpH37vrUEBb2bKHRJLoo2c9Ocz2Cc2Dd9t2DxxqIo6%2FOOH1F8hGjuHQ5HdLrE9JSDFp5SnsqAqclHcI7QO4cOnPyiAwczMo5CpXQ%2BvX0xSb7LGHi7gK7sO3zFKqsEK3%2Fu6DrZ8LiHpZGair5kjFT%2BSoO8NFD%2BxpbdVodR6BrG%2B98J0HcyRVyF9iydVnKCSgtre5RW43&X-Amz-Signature=fe0b3c564b397f9adf588aa0e5a3ac8bcc70a3f9c284c08683c2b197c5cdc6e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3CQPUC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCULb50x9MCfCpG92X9DBb194s6rBzv%2FFw%2F5bSZwpsmBAIhAIFxAMjVXjJiAi7V2afCYeteHntAxqTACrw4IuqcMu9zKv8DCBQQABoMNjM3NDIzMTgzODA1IgxbzgTzhYEjyfTtQhEq3APR%2Fueu6L9pFgcFdL8dunVhD8%2FbNj9z%2FU10V4AQxPwRCRRTVVoPC%2BNEFGNRZmr5cpSyEciWHrZrf8JYN03QmWYHWMcXJZL%2BE3p2mWxoo7aymkIK6PqcaRkjHqsf35SiXRBVb2f22lO0wxPSdD9cY1QBlDkmkmJgOpjweqh6xkGXcoOZHubV81j%2BWnFCpXu04BytzmWzXjTrqJJfEcJCD6jhdtl5%2BX%2Bk5GistXL1Ra3oIbbRFgTC6IGBCuC5UG3DQGsnktvKF9%2F5%2FAFaauK5UY2hulIuSdKDQt7RIMZHsG%2Bh3HrDcehvYENGKnfOSU9f5PzsAHYXGUj%2F1gsF8va73zB8p2jwooH0bWp%2Fx9xKyTrba7%2F5eWrO4cjEzUeIzlHvRTOcix5sf8M7Hk0EqRKawqiigXXyw6Cm2JhOf%2FesqCK90PVmY7rrHyCuW048PBLFrBaPtmpQYKMUNLv%2BSq4ENZkIN9LO6knOAbgAfbLzGWM6n%2FAkKyzHHv21WLYpQ8gzLo%2BoMqA0Aky736mhwBPt8MYLU%2FhCwkHUEGf7b6m0s7L3PUCbxOOG3fGa2EBJZrDcQVRT4bZpdy9YCgVAJfEhD1CRSOvHYBWq%2B2trTv2ENCV7LU4gSRNILAPnk5TqITDh0oK9BjqkAZJiYf9E0Pb5Xxln8m%2B22ZpH37vrUEBb2bKHRJLoo2c9Ocz2Cc2Dd9t2DxxqIo6%2FOOH1F8hGjuHQ5HdLrE9JSDFp5SnsqAqclHcI7QO4cOnPyiAwczMo5CpXQ%2BvX0xSb7LGHi7gK7sO3zFKqsEK3%2Fu6DrZ8LiHpZGair5kjFT%2BSoO8NFD%2BxpbdVodR6BrG%2B98J0HcyRVyF9iydVnKCSgtre5RW43&X-Amz-Signature=3d92ca7200c7c8fb80c39032548c5facadc25982707786b5dc25d182dca5bf3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF3MTTGN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGr%2FYbY1Te6wJ%2FVIVR4CxdA9yYLo3vlrVzxo6AdHn8FQIhALIXk7%2F0Y8h%2FaQAR2QUaVXbxVJ5UEdhk5S6IhUfmBAX%2BKv8DCBUQABoMNjM3NDIzMTgzODA1IgzPXQnLHI6pyEuW2ywq3AO2KZECB0R%2F5FytHF9QHKK%2FxBb36Ux05B4r2isOsV93geGo5lF5CY%2Fvyz8S6wlpa8VNZjzQ4X3UvBidhIV9HDr1YYrS1MrpkOGm58ywqpR7tTEepy0saq0kffAnHR%2BMzWWe%2Ft8ayRIETvHR%2F3X43uOp6STBB7btN%2Fn0Sgf4w7HGrxu86gN%2BkCD9jFFy%2Fgk7%2Frlo0%2FdgVqlBi84DQfVx7mOcT5hMGvszbKmILtLgc3TcLNy2h2iLvVUuYnm3m%2BZ6fBbQUNo38lIADTuyhA9eRuG7oQ0RTXQgOsRZiUWfnNsQPVK7XbVipN%2Bxjd75Kva2Hft3EmEGHSaDAPtCuKJLy%2BFqFfLQ3EwIm4gIO1CZGXypnCxBFobzd08nwmUjeHRfVYrpg45kwu0nvWAxJwGH1V5YyJl9QoO7U3pY%2B9OuuFLQLYTHKqPUiLFPMKyI91772jsFLya7z7ofg6eRHWc0mUn7yYemnBLc2El486t8KQQWzVpBGA8jCqDyUa8iaqqY5yB5eoa6S2096vOkVBZ7Q4tsQkK3f8o1KVC%2FdVbEjGQoDhe4n9dZzlfmCwNN5Yjzm2rZzfoo6MnIlU1Lc0UikziHbzYKysZ1STZGJqJ36%2BAqiW9dwLuRaOuLaHkhwzCc04K9BjqkAbi9zJjFacn4W30Tznzq2upKePFhx87R99pPgGpe14nwvv8oQXc29LWXxGyok3XEdBm%2Fm2Z6Ria3zwv8eF0yUjjmyEhp7KLgwNIeymNGLPv0BPC1yFGUUcMSC6bUoQpH5y31JQDHd3VQDKeiyo8q9Mf5981Ol8aJPqosfWkyBOJYY5s5tPNS9NNbIjzNKXXBKQzNjqp0UYc8QfLrxv0BMsWfBaIk&X-Amz-Signature=58b354d71c0d0c4832d5059693465b2c16bb3d5806600060f4c13a19ecaeb8b2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF3MTTGN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGr%2FYbY1Te6wJ%2FVIVR4CxdA9yYLo3vlrVzxo6AdHn8FQIhALIXk7%2F0Y8h%2FaQAR2QUaVXbxVJ5UEdhk5S6IhUfmBAX%2BKv8DCBUQABoMNjM3NDIzMTgzODA1IgzPXQnLHI6pyEuW2ywq3AO2KZECB0R%2F5FytHF9QHKK%2FxBb36Ux05B4r2isOsV93geGo5lF5CY%2Fvyz8S6wlpa8VNZjzQ4X3UvBidhIV9HDr1YYrS1MrpkOGm58ywqpR7tTEepy0saq0kffAnHR%2BMzWWe%2Ft8ayRIETvHR%2F3X43uOp6STBB7btN%2Fn0Sgf4w7HGrxu86gN%2BkCD9jFFy%2Fgk7%2Frlo0%2FdgVqlBi84DQfVx7mOcT5hMGvszbKmILtLgc3TcLNy2h2iLvVUuYnm3m%2BZ6fBbQUNo38lIADTuyhA9eRuG7oQ0RTXQgOsRZiUWfnNsQPVK7XbVipN%2Bxjd75Kva2Hft3EmEGHSaDAPtCuKJLy%2BFqFfLQ3EwIm4gIO1CZGXypnCxBFobzd08nwmUjeHRfVYrpg45kwu0nvWAxJwGH1V5YyJl9QoO7U3pY%2B9OuuFLQLYTHKqPUiLFPMKyI91772jsFLya7z7ofg6eRHWc0mUn7yYemnBLc2El486t8KQQWzVpBGA8jCqDyUa8iaqqY5yB5eoa6S2096vOkVBZ7Q4tsQkK3f8o1KVC%2FdVbEjGQoDhe4n9dZzlfmCwNN5Yjzm2rZzfoo6MnIlU1Lc0UikziHbzYKysZ1STZGJqJ36%2BAqiW9dwLuRaOuLaHkhwzCc04K9BjqkAbi9zJjFacn4W30Tznzq2upKePFhx87R99pPgGpe14nwvv8oQXc29LWXxGyok3XEdBm%2Fm2Z6Ria3zwv8eF0yUjjmyEhp7KLgwNIeymNGLPv0BPC1yFGUUcMSC6bUoQpH5y31JQDHd3VQDKeiyo8q9Mf5981Ol8aJPqosfWkyBOJYY5s5tPNS9NNbIjzNKXXBKQzNjqp0UYc8QfLrxv0BMsWfBaIk&X-Amz-Signature=469d61618dcb2812d1d321fa82abe32b98ea0c5f94f702b138015480d9bfce29&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF3MTTGN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGr%2FYbY1Te6wJ%2FVIVR4CxdA9yYLo3vlrVzxo6AdHn8FQIhALIXk7%2F0Y8h%2FaQAR2QUaVXbxVJ5UEdhk5S6IhUfmBAX%2BKv8DCBUQABoMNjM3NDIzMTgzODA1IgzPXQnLHI6pyEuW2ywq3AO2KZECB0R%2F5FytHF9QHKK%2FxBb36Ux05B4r2isOsV93geGo5lF5CY%2Fvyz8S6wlpa8VNZjzQ4X3UvBidhIV9HDr1YYrS1MrpkOGm58ywqpR7tTEepy0saq0kffAnHR%2BMzWWe%2Ft8ayRIETvHR%2F3X43uOp6STBB7btN%2Fn0Sgf4w7HGrxu86gN%2BkCD9jFFy%2Fgk7%2Frlo0%2FdgVqlBi84DQfVx7mOcT5hMGvszbKmILtLgc3TcLNy2h2iLvVUuYnm3m%2BZ6fBbQUNo38lIADTuyhA9eRuG7oQ0RTXQgOsRZiUWfnNsQPVK7XbVipN%2Bxjd75Kva2Hft3EmEGHSaDAPtCuKJLy%2BFqFfLQ3EwIm4gIO1CZGXypnCxBFobzd08nwmUjeHRfVYrpg45kwu0nvWAxJwGH1V5YyJl9QoO7U3pY%2B9OuuFLQLYTHKqPUiLFPMKyI91772jsFLya7z7ofg6eRHWc0mUn7yYemnBLc2El486t8KQQWzVpBGA8jCqDyUa8iaqqY5yB5eoa6S2096vOkVBZ7Q4tsQkK3f8o1KVC%2FdVbEjGQoDhe4n9dZzlfmCwNN5Yjzm2rZzfoo6MnIlU1Lc0UikziHbzYKysZ1STZGJqJ36%2BAqiW9dwLuRaOuLaHkhwzCc04K9BjqkAbi9zJjFacn4W30Tznzq2upKePFhx87R99pPgGpe14nwvv8oQXc29LWXxGyok3XEdBm%2Fm2Z6Ria3zwv8eF0yUjjmyEhp7KLgwNIeymNGLPv0BPC1yFGUUcMSC6bUoQpH5y31JQDHd3VQDKeiyo8q9Mf5981Ol8aJPqosfWkyBOJYY5s5tPNS9NNbIjzNKXXBKQzNjqp0UYc8QfLrxv0BMsWfBaIk&X-Amz-Signature=3b2f50c8c20fca17251dcda0db0be9346a5d62d29b430be9ad4ae874ea0678b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF3MTTGN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGr%2FYbY1Te6wJ%2FVIVR4CxdA9yYLo3vlrVzxo6AdHn8FQIhALIXk7%2F0Y8h%2FaQAR2QUaVXbxVJ5UEdhk5S6IhUfmBAX%2BKv8DCBUQABoMNjM3NDIzMTgzODA1IgzPXQnLHI6pyEuW2ywq3AO2KZECB0R%2F5FytHF9QHKK%2FxBb36Ux05B4r2isOsV93geGo5lF5CY%2Fvyz8S6wlpa8VNZjzQ4X3UvBidhIV9HDr1YYrS1MrpkOGm58ywqpR7tTEepy0saq0kffAnHR%2BMzWWe%2Ft8ayRIETvHR%2F3X43uOp6STBB7btN%2Fn0Sgf4w7HGrxu86gN%2BkCD9jFFy%2Fgk7%2Frlo0%2FdgVqlBi84DQfVx7mOcT5hMGvszbKmILtLgc3TcLNy2h2iLvVUuYnm3m%2BZ6fBbQUNo38lIADTuyhA9eRuG7oQ0RTXQgOsRZiUWfnNsQPVK7XbVipN%2Bxjd75Kva2Hft3EmEGHSaDAPtCuKJLy%2BFqFfLQ3EwIm4gIO1CZGXypnCxBFobzd08nwmUjeHRfVYrpg45kwu0nvWAxJwGH1V5YyJl9QoO7U3pY%2B9OuuFLQLYTHKqPUiLFPMKyI91772jsFLya7z7ofg6eRHWc0mUn7yYemnBLc2El486t8KQQWzVpBGA8jCqDyUa8iaqqY5yB5eoa6S2096vOkVBZ7Q4tsQkK3f8o1KVC%2FdVbEjGQoDhe4n9dZzlfmCwNN5Yjzm2rZzfoo6MnIlU1Lc0UikziHbzYKysZ1STZGJqJ36%2BAqiW9dwLuRaOuLaHkhwzCc04K9BjqkAbi9zJjFacn4W30Tznzq2upKePFhx87R99pPgGpe14nwvv8oQXc29LWXxGyok3XEdBm%2Fm2Z6Ria3zwv8eF0yUjjmyEhp7KLgwNIeymNGLPv0BPC1yFGUUcMSC6bUoQpH5y31JQDHd3VQDKeiyo8q9Mf5981Ol8aJPqosfWkyBOJYY5s5tPNS9NNbIjzNKXXBKQzNjqp0UYc8QfLrxv0BMsWfBaIk&X-Amz-Signature=17698ef58e22e65f6679d77742f4e877884e2ae822873c1e5cdb1c45c9215b6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF3MTTGN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGr%2FYbY1Te6wJ%2FVIVR4CxdA9yYLo3vlrVzxo6AdHn8FQIhALIXk7%2F0Y8h%2FaQAR2QUaVXbxVJ5UEdhk5S6IhUfmBAX%2BKv8DCBUQABoMNjM3NDIzMTgzODA1IgzPXQnLHI6pyEuW2ywq3AO2KZECB0R%2F5FytHF9QHKK%2FxBb36Ux05B4r2isOsV93geGo5lF5CY%2Fvyz8S6wlpa8VNZjzQ4X3UvBidhIV9HDr1YYrS1MrpkOGm58ywqpR7tTEepy0saq0kffAnHR%2BMzWWe%2Ft8ayRIETvHR%2F3X43uOp6STBB7btN%2Fn0Sgf4w7HGrxu86gN%2BkCD9jFFy%2Fgk7%2Frlo0%2FdgVqlBi84DQfVx7mOcT5hMGvszbKmILtLgc3TcLNy2h2iLvVUuYnm3m%2BZ6fBbQUNo38lIADTuyhA9eRuG7oQ0RTXQgOsRZiUWfnNsQPVK7XbVipN%2Bxjd75Kva2Hft3EmEGHSaDAPtCuKJLy%2BFqFfLQ3EwIm4gIO1CZGXypnCxBFobzd08nwmUjeHRfVYrpg45kwu0nvWAxJwGH1V5YyJl9QoO7U3pY%2B9OuuFLQLYTHKqPUiLFPMKyI91772jsFLya7z7ofg6eRHWc0mUn7yYemnBLc2El486t8KQQWzVpBGA8jCqDyUa8iaqqY5yB5eoa6S2096vOkVBZ7Q4tsQkK3f8o1KVC%2FdVbEjGQoDhe4n9dZzlfmCwNN5Yjzm2rZzfoo6MnIlU1Lc0UikziHbzYKysZ1STZGJqJ36%2BAqiW9dwLuRaOuLaHkhwzCc04K9BjqkAbi9zJjFacn4W30Tznzq2upKePFhx87R99pPgGpe14nwvv8oQXc29LWXxGyok3XEdBm%2Fm2Z6Ria3zwv8eF0yUjjmyEhp7KLgwNIeymNGLPv0BPC1yFGUUcMSC6bUoQpH5y31JQDHd3VQDKeiyo8q9Mf5981Ol8aJPqosfWkyBOJYY5s5tPNS9NNbIjzNKXXBKQzNjqp0UYc8QfLrxv0BMsWfBaIk&X-Amz-Signature=d08e02ac818b183d942a524af8f3c4e97cc3a0ba688f1ae5fb3c9cffa9b4e3f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF3MTTGN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGr%2FYbY1Te6wJ%2FVIVR4CxdA9yYLo3vlrVzxo6AdHn8FQIhALIXk7%2F0Y8h%2FaQAR2QUaVXbxVJ5UEdhk5S6IhUfmBAX%2BKv8DCBUQABoMNjM3NDIzMTgzODA1IgzPXQnLHI6pyEuW2ywq3AO2KZECB0R%2F5FytHF9QHKK%2FxBb36Ux05B4r2isOsV93geGo5lF5CY%2Fvyz8S6wlpa8VNZjzQ4X3UvBidhIV9HDr1YYrS1MrpkOGm58ywqpR7tTEepy0saq0kffAnHR%2BMzWWe%2Ft8ayRIETvHR%2F3X43uOp6STBB7btN%2Fn0Sgf4w7HGrxu86gN%2BkCD9jFFy%2Fgk7%2Frlo0%2FdgVqlBi84DQfVx7mOcT5hMGvszbKmILtLgc3TcLNy2h2iLvVUuYnm3m%2BZ6fBbQUNo38lIADTuyhA9eRuG7oQ0RTXQgOsRZiUWfnNsQPVK7XbVipN%2Bxjd75Kva2Hft3EmEGHSaDAPtCuKJLy%2BFqFfLQ3EwIm4gIO1CZGXypnCxBFobzd08nwmUjeHRfVYrpg45kwu0nvWAxJwGH1V5YyJl9QoO7U3pY%2B9OuuFLQLYTHKqPUiLFPMKyI91772jsFLya7z7ofg6eRHWc0mUn7yYemnBLc2El486t8KQQWzVpBGA8jCqDyUa8iaqqY5yB5eoa6S2096vOkVBZ7Q4tsQkK3f8o1KVC%2FdVbEjGQoDhe4n9dZzlfmCwNN5Yjzm2rZzfoo6MnIlU1Lc0UikziHbzYKysZ1STZGJqJ36%2BAqiW9dwLuRaOuLaHkhwzCc04K9BjqkAbi9zJjFacn4W30Tznzq2upKePFhx87R99pPgGpe14nwvv8oQXc29LWXxGyok3XEdBm%2Fm2Z6Ria3zwv8eF0yUjjmyEhp7KLgwNIeymNGLPv0BPC1yFGUUcMSC6bUoQpH5y31JQDHd3VQDKeiyo8q9Mf5981Ol8aJPqosfWkyBOJYY5s5tPNS9NNbIjzNKXXBKQzNjqp0UYc8QfLrxv0BMsWfBaIk&X-Amz-Signature=ce757cbd5b453317843ef126437fbf5bb5fd6359ec6e9b6d00976c1e653746bf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STXBIOE4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT%2FARuEUhAlD%2FXQqdulMaQGFgmlv%2BqOATZzP8y%2BYNd7QIhAOOcWJ17LsGvyeHtyeO4IgdSh2C7sviGXtkEIlaBlNOHKv8DCBUQABoMNjM3NDIzMTgzODA1Igytt4oNfaaU3BWSEwgq3APxhPYW3RWMAB9FThoXsmErAfADW1r8Hwhux9EcXgwAuh82MlStRwXoiEXgeLT9GmMB1ehdJUGnEJRgKmUS%2FqHDiaf3MmrrxrSEOLIJgEukz0L3VfAp1Zyi6n7gsKJ5eLRGu55Jw10SWUJv9tU5dp0ri9I3MxKPRt27n1iemm%2FZGQnDPpuc5gAbzYMsXKm7N8%2F42pg40CwxRLvi5yzBuHaI%2BcenA%2BBjZVf1d%2FpWCzLXvUpnQvlKvbQeFX6WSDBslu5TvaDTTXZ3E3guEq1niXhK72xCGEx4%2FQqmi3Reb7f1b92jTX2%2BXotvuhvPJygD8Pd%2B2tB1lrH0EWUve98LeItpr%2FCEJJTi71P3qH61CdY0hRnRwEb0PiC%2BfCzEcWhP4OHdX15ALgNrsB4wOkujvAMyOmJkug8LMZLmAAxLY8wkl99kGn2MCkYbPEQIIzdINMWfdVHjfwnzWnxitDyES8B6QGS7B1nmONdqOsKkM8ext2kkODnRagvgc8LJDrnzsW2gBXrpGbP8Qc%2BG8XapsphHXdzoOT0AhRpGDrbZ6pdkMTPnjFzXxT2RhvxYFI6hZ5vY%2F2ViSzncR7aJ3dPp18PmiNcj4veVbROV19og%2FbNxSuqI3xssnjPb%2FJVk%2BjDP04K9BjqkAW7%2B2MkhV7k4R6LLsuHrVHMLjtOe2p74klwZIsufzb5RZsGJ6GBi4HUpC3Kdt2ggojN3C4MjypyXDhjjtQl7xnXVfTnfnSmtOhgw%2FU0J%2Bvob%2BZlpT1rgdRFEqewKh6aYASnJjuacqZ3pvCrcnkqJ8zmGTl1vppTejVuPcO%2B7ihTbqxY663kBRyrIlmQVq6mbkYQW71aBlVFjfq6NXn0mIsjWUw7v&X-Amz-Signature=ea206e3960dba34d97120caf44233115496baffaafa309cf9189ebd9dd60d233&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5YF6QAP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBfOvpvspPZQAqga2275HvIevvax9Y9WwdZYAN6oFStuAiEAjkhIq3lId0DWyZ1teo69BStB0Qufa8F2VM3uuQ0cVwUq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDA7v5VYwwlQDTaCV5ircA44XrZcQnuk4dHpDTw649lxPFejB4YLXpcW5uWK55%2FD%2BDYrIaup4cNZXNv0esbCIy8oQyG9JxlKJIt7papszz9bD%2BBNYxKL90dOJ2AhQrEeCfTgK%2BenS3AQgCklKJl3lt2AURl8Y1RAJq2%2Fw3mIUFpsG69N5hLXLITC2CYiOTyRuhaOyPtEm7i7bZVA8AboFXCeyt6u5hafZfPfMasBL%2BwPV6Vv6M2v%2BEFUcrKpmbN2mm9k5%2FDrS2mDzFAj%2FSjg8BxAYfW18cbua8RMFTddOexfr%2Bsk8nxVie7yvQCkx3ol8TbdEX7QRkCofX3APR9JUWq9dJphlE1A1pzsCPA2dkCt7La2cn2HeekPgBRU8YOw5y9kndaH7WPP8aM1%2FqODQRwZBKBRwUYmgGRHHe3jKaMoOs1%2FXh1JM3b6Ro1lPMncYVg00lH2fncKC1x2vlEvJXtaLEvFXUmH7ml036tlg3uLESarDrKqtsyl2QpU6L8WrULm7tjTcQ%2BZ7ilHLHfmaORHVkHQg%2Fo%2FbW27G5LoQvZAcdwJ1mDTUJqmhjAm2%2Bd6VJa5wHCetVnXfJGwyirPTfzXT5OkYIXljab4Y4GgTSVpgT1eYliLkfarCVeCm5HKDvhfHcYinvs6gJxyzMNHSgr0GOqUBIjNXElQVvnkIipMHQB0t8wp8TAUt0Dwz4N5LSe3wFiP1Fhoi4qNDsGVbhi%2FlGGKS1SkCCNtPy1wSPqvcnXEhXf61In%2BEs93YYHU0FDaaLFavhUvAfpqOSBehfUNFmibWVHdrD7cXxH3gJihWjDesF5oXVeLZPD0r9Vl5kBNb5SXox8NuddPt2%2BXvqMVx73fNteogyovuLFZ9Kt5iiqpTqfBvCRH9&X-Amz-Signature=330a5aa646fdfd0e4235e32b4d74dbb788a1f6f68917f901209e1c8ffefb33b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF3MTTGN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGr%2FYbY1Te6wJ%2FVIVR4CxdA9yYLo3vlrVzxo6AdHn8FQIhALIXk7%2F0Y8h%2FaQAR2QUaVXbxVJ5UEdhk5S6IhUfmBAX%2BKv8DCBUQABoMNjM3NDIzMTgzODA1IgzPXQnLHI6pyEuW2ywq3AO2KZECB0R%2F5FytHF9QHKK%2FxBb36Ux05B4r2isOsV93geGo5lF5CY%2Fvyz8S6wlpa8VNZjzQ4X3UvBidhIV9HDr1YYrS1MrpkOGm58ywqpR7tTEepy0saq0kffAnHR%2BMzWWe%2Ft8ayRIETvHR%2F3X43uOp6STBB7btN%2Fn0Sgf4w7HGrxu86gN%2BkCD9jFFy%2Fgk7%2Frlo0%2FdgVqlBi84DQfVx7mOcT5hMGvszbKmILtLgc3TcLNy2h2iLvVUuYnm3m%2BZ6fBbQUNo38lIADTuyhA9eRuG7oQ0RTXQgOsRZiUWfnNsQPVK7XbVipN%2Bxjd75Kva2Hft3EmEGHSaDAPtCuKJLy%2BFqFfLQ3EwIm4gIO1CZGXypnCxBFobzd08nwmUjeHRfVYrpg45kwu0nvWAxJwGH1V5YyJl9QoO7U3pY%2B9OuuFLQLYTHKqPUiLFPMKyI91772jsFLya7z7ofg6eRHWc0mUn7yYemnBLc2El486t8KQQWzVpBGA8jCqDyUa8iaqqY5yB5eoa6S2096vOkVBZ7Q4tsQkK3f8o1KVC%2FdVbEjGQoDhe4n9dZzlfmCwNN5Yjzm2rZzfoo6MnIlU1Lc0UikziHbzYKysZ1STZGJqJ36%2BAqiW9dwLuRaOuLaHkhwzCc04K9BjqkAbi9zJjFacn4W30Tznzq2upKePFhx87R99pPgGpe14nwvv8oQXc29LWXxGyok3XEdBm%2Fm2Z6Ria3zwv8eF0yUjjmyEhp7KLgwNIeymNGLPv0BPC1yFGUUcMSC6bUoQpH5y31JQDHd3VQDKeiyo8q9Mf5981Ol8aJPqosfWkyBOJYY5s5tPNS9NNbIjzNKXXBKQzNjqp0UYc8QfLrxv0BMsWfBaIk&X-Amz-Signature=d20ea05f00d751ca0689c25bdbc7b7b0e999bfd8b96b3107bc8b0f08dcfebfd9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF3MTTGN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGr%2FYbY1Te6wJ%2FVIVR4CxdA9yYLo3vlrVzxo6AdHn8FQIhALIXk7%2F0Y8h%2FaQAR2QUaVXbxVJ5UEdhk5S6IhUfmBAX%2BKv8DCBUQABoMNjM3NDIzMTgzODA1IgzPXQnLHI6pyEuW2ywq3AO2KZECB0R%2F5FytHF9QHKK%2FxBb36Ux05B4r2isOsV93geGo5lF5CY%2Fvyz8S6wlpa8VNZjzQ4X3UvBidhIV9HDr1YYrS1MrpkOGm58ywqpR7tTEepy0saq0kffAnHR%2BMzWWe%2Ft8ayRIETvHR%2F3X43uOp6STBB7btN%2Fn0Sgf4w7HGrxu86gN%2BkCD9jFFy%2Fgk7%2Frlo0%2FdgVqlBi84DQfVx7mOcT5hMGvszbKmILtLgc3TcLNy2h2iLvVUuYnm3m%2BZ6fBbQUNo38lIADTuyhA9eRuG7oQ0RTXQgOsRZiUWfnNsQPVK7XbVipN%2Bxjd75Kva2Hft3EmEGHSaDAPtCuKJLy%2BFqFfLQ3EwIm4gIO1CZGXypnCxBFobzd08nwmUjeHRfVYrpg45kwu0nvWAxJwGH1V5YyJl9QoO7U3pY%2B9OuuFLQLYTHKqPUiLFPMKyI91772jsFLya7z7ofg6eRHWc0mUn7yYemnBLc2El486t8KQQWzVpBGA8jCqDyUa8iaqqY5yB5eoa6S2096vOkVBZ7Q4tsQkK3f8o1KVC%2FdVbEjGQoDhe4n9dZzlfmCwNN5Yjzm2rZzfoo6MnIlU1Lc0UikziHbzYKysZ1STZGJqJ36%2BAqiW9dwLuRaOuLaHkhwzCc04K9BjqkAbi9zJjFacn4W30Tznzq2upKePFhx87R99pPgGpe14nwvv8oQXc29LWXxGyok3XEdBm%2Fm2Z6Ria3zwv8eF0yUjjmyEhp7KLgwNIeymNGLPv0BPC1yFGUUcMSC6bUoQpH5y31JQDHd3VQDKeiyo8q9Mf5981Ol8aJPqosfWkyBOJYY5s5tPNS9NNbIjzNKXXBKQzNjqp0UYc8QfLrxv0BMsWfBaIk&X-Amz-Signature=29c70a0aea6718d1e1317dcf0fc368c6dc1edf90996f404d5b9872b258aae575&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF3MTTGN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGr%2FYbY1Te6wJ%2FVIVR4CxdA9yYLo3vlrVzxo6AdHn8FQIhALIXk7%2F0Y8h%2FaQAR2QUaVXbxVJ5UEdhk5S6IhUfmBAX%2BKv8DCBUQABoMNjM3NDIzMTgzODA1IgzPXQnLHI6pyEuW2ywq3AO2KZECB0R%2F5FytHF9QHKK%2FxBb36Ux05B4r2isOsV93geGo5lF5CY%2Fvyz8S6wlpa8VNZjzQ4X3UvBidhIV9HDr1YYrS1MrpkOGm58ywqpR7tTEepy0saq0kffAnHR%2BMzWWe%2Ft8ayRIETvHR%2F3X43uOp6STBB7btN%2Fn0Sgf4w7HGrxu86gN%2BkCD9jFFy%2Fgk7%2Frlo0%2FdgVqlBi84DQfVx7mOcT5hMGvszbKmILtLgc3TcLNy2h2iLvVUuYnm3m%2BZ6fBbQUNo38lIADTuyhA9eRuG7oQ0RTXQgOsRZiUWfnNsQPVK7XbVipN%2Bxjd75Kva2Hft3EmEGHSaDAPtCuKJLy%2BFqFfLQ3EwIm4gIO1CZGXypnCxBFobzd08nwmUjeHRfVYrpg45kwu0nvWAxJwGH1V5YyJl9QoO7U3pY%2B9OuuFLQLYTHKqPUiLFPMKyI91772jsFLya7z7ofg6eRHWc0mUn7yYemnBLc2El486t8KQQWzVpBGA8jCqDyUa8iaqqY5yB5eoa6S2096vOkVBZ7Q4tsQkK3f8o1KVC%2FdVbEjGQoDhe4n9dZzlfmCwNN5Yjzm2rZzfoo6MnIlU1Lc0UikziHbzYKysZ1STZGJqJ36%2BAqiW9dwLuRaOuLaHkhwzCc04K9BjqkAbi9zJjFacn4W30Tznzq2upKePFhx87R99pPgGpe14nwvv8oQXc29LWXxGyok3XEdBm%2Fm2Z6Ria3zwv8eF0yUjjmyEhp7KLgwNIeymNGLPv0BPC1yFGUUcMSC6bUoQpH5y31JQDHd3VQDKeiyo8q9Mf5981Ol8aJPqosfWkyBOJYY5s5tPNS9NNbIjzNKXXBKQzNjqp0UYc8QfLrxv0BMsWfBaIk&X-Amz-Signature=d2bcfb67198561324f6dcd35949f26dc6f063099dd7491efd96a92eb1e7b3f5e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5LEAU6J%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDZ8ovkJsDF5vgpp0rtZG1jeUSNqnD080Y17omIBa9vwIgINUcPKFLPQh2Ujqnstey7XEHtWa1S2h1FS%2FqG%2FjSEqwq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDDv8GwT0i1FYKIwO8ircA5Di8t3NfZg80KaOd2c4d5xcZcuzTUrmHKihMACKIHA3hF8KJWdHwY4N0fd4dEQ2sOCbUEJ4blUkzpHYkjlzT%2BRb21RMOPEUEC8NQREVj%2FqfHv%2FLP7GMlheP7vc3azgbyKlHDXyRt08oo9ZKN9v%2BVj5nH6iRYarjm%2BVSW69Ia6j5FHTx18Vjd%2Fw21h1gZc9BdMIUNIdEyRw63k7SiTvIiYD1NsnCXYgKoa7WMgAjMRoa1XMJXwXHu2q9y3Nd2CAPtSlvGJa7lt4GT5jzjOe6JlzYpnfg6f5nHU40p4jL8zBY5zBlq9PfJiSDATulTHzeAV3dKOWFuFRDPmy1CYTq4wYjgcj%2BHySh8k%2BLViWF2Y4L4zmKqZYyGWuCgpDSTHYGj362K3kHyXmFy%2B%2F%2BaXdNQVntwrRuDIzI9GX8%2BqrCEnwYKsiP9ToegmU%2FZ1Zp2smilnzOjBVBIHpL%2FowPseSBwTFMsZX94yNVYJosp%2Fsf2Ch2o1uba68tRxGuhg%2BD51U7B6qvOI6b3W7K0%2BlzF2%2B8cXILAj5goSq1BYmzKv1AK8v9N3KbBREUouePth%2BHE%2FA2tEKqzuOmJPJP3u%2FqVha6JkxtCXsk%2BOtji41BXHyE9XCrY%2FA5pwqIiddTuZu2MOTSgr0GOqUBRfcsFq%2B08T3vdLJkWlSCgHx6UwtQbHmn453cuF%2BMjYhp%2BcI0gYdFM631ZNehw%2FM9jpEpnKR39DSLGQb3fkS4R38YgJcJO3em%2Fhaj4vei2nUF3Un73oWSqceC9fxHBHSw1JAhCb0IQ71%2F4Yor0gBGByX1AeHjxBF%2FCO3GyEiUFAgMbUOUuyOkY%2B6jOWs5aWpyFYYivrDrXymFEaayPrR8aBEZupby&X-Amz-Signature=082317be9bb5c75aa3b182729388bd851d58b9a3043bf5785363a6facbf0acf3&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M7E6B4K%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHw%2Fc6McCDMAtE3DezZoWWSKQnt7KIw%2Bb1p8IbtHWBFrAiEAvf7Sg831CNAYZ0iTeOMMC2Rf%2BUP8qKPFsnUD4f5eeq0q%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDKeXGWnqddsK05R8myrcA5HAUZax9wHl1Mkk%2B5AdjJBL8Vvynpa7gbq99DsNAfrGv8fb0vM23jYSWZ8OpgRWEtQlHwZJHGeuVXLio%2FI%2B%2BVszjwin3Oj4BYZdapjx9g3el5UI8f2NlVjRKRuQKUfFh9W2SfwY7qQxr59Hoh5kmuN2xT9LPGMelZNoLFQEJwDiHVs%2F6ysv%2F1pwc6ks3g8RzD4TYdkDU4DEIj5DSdvZOPmpRluL8d4txiIu70cUsyDPqcJUA5QGciur02agtb7uhaI0b0ycsVVbHPTr1joyTH7XBHCQO%2Bq%2Bh3StDvXXExY1GOXipMTtL2kH0Fi%2FhVZlL79SosIgL%2FfIV71xbKx0hK2YL3FYGsQr8VUdsOeul2wCDedYVQaDROm6xGx%2BwyM8ONUqIRmMs47t1EGksEzvN3qzSP3B6%2FWJ%2B3jAd7QE6fKSgeZElxuTg5EI8t17Kqe8VL6DQK%2F9OJnGpDoBG1T%2BgMPlzUOCuFqtvgjvkzZkf3YKBtH0dCVDA9wzs9yPyvhj6OocnU2D%2Ff0bhE7y3h6MjNScRdaf14H7lXwz9vFAPL430RcF2QfFQMUtnOfaS%2B7Q4OiuBLpmATdUHT3HiqhXikfooJHCZ8rX4TsbehxFIXUBDPC4OU0Y8BkyNGvLMPnSgr0GOqUBo97H9LI%2FUPIO5OMLGd6%2Fuk33QWRy60LB8lwKCMuZBnjP77XAIWtetoWKHpPvOPcsTOae3Ve%2B1N9tekLDslv6UEcZp4AQf%2BGeNEsu0vyjgHoS3YZrY0TEiuImHLxIdSkY%2F4nLtDY2RjQwhXZRgBWY3kkZoMgAqMOpxih7Y%2FObe%2Fxnu4JUwfbI%2BDu3FTNGR9xLrl7Mue1SL7pabnLt5tOJf2M6pPnC&X-Amz-Signature=6280f1f1f1e41bb52e3ec0154a0967a2f05ff0eb96ecaff56bc86c1626875edf&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOKAHWFY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8Ni8k3AIn2k5M79%2BAxtVUEddCQkgk99y2ydy33jB6FgIgD0x3D3VTZ8hXV2iJqlxRMbMBhJBSlIwZCaBYU2FN3ZAq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDFy2rQQfRXrl4M1M6yrcA7AyMOO7%2BDALyR0mI1IW8TuMRTtpq%2FBwdlUUxx0OSzO84qQd0CkaAdYAuUn4WzYl%2ByRXT4WhMPxcQx3I7hy1o9K7vppW%2FJWEbxfmmwbDlNvdr5%2FHZZ3znobvU%2FWQd2WeFZOMC4%2FI6S4ozzrZcxF%2B1KYIclQb%2BjmZ%2Fd1GoZ4T9fSY8YPe9ufXFxXZNNeOvz96fDKKGld16bTjJCzvI7cNev8HRWWreqOOl1PEemusP0t7V%2BDDm0Oagb7PcMFSwZzvQua7XaCsuYPwGy%2FlAi4ChgJwD2w01ABV2XsgBx4UmaQ%2Fz4x6y9B09%2F5gfcEpzSWU2c460DjEuqcSxbPmSl2r4%2FA3yn1ImzsA2JvO%2BhlHJIw1id9%2B%2FKQuun2be7kpkxIyDhQeWdkiaX%2FlF5BoWwqxSS0H9gelavDN3CoKguyTxgiqvSq9jDmCQkqfVKp71g9af7nzXWPF%2BfDLrhz5PVvmK5LaysYQmt6oKH7aFXtp4%2FoCDB8n%2BVGrdu9JzLY5pzZybRIdvQ8J5rpkmi%2B5f1cNFqzxKWjJTwfpuULwN0rep4LlIT%2FEQ6Ou%2B8WvS5rCNHGKoGfFwZax3IXjIZRRlRg03nvSAmweaO3TmBHqlnNiiBBz4cYs7%2BxL89iBvlNMML%2FTgr0GOqUBdopiYa86SNz8ID1F6hlxCl3HKoAzgNjA3KxnbtKesoEnpfxix7ARCAvuMh69eOmH4HHoM6T89CfedTRWABTV7H14vBWMVYsevzJjFTMacgaoOFRxqOdbK70yqpB3IKh2oc54KOyFTmpMlyXp1tCUHPRs7v4fOJU3ylSJlUqg5UHuhTBxD62Td7HRXuMM3jrrcz1QGb6cV2D0rBbkpNaTW2eUCB0Q&X-Amz-Signature=51859c119a679c6e4ad15c0ef547e65ed14a5acd2a152c048900483268587ce1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKNF5JVA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxS6nN%2FnEMfj3tccvnguIigpbcWHCzn2FpO4JewB%2BDCwIgdlpfxuwc1mCXCT3SRkn9%2B7SBbTcGwCTbtGNw5B7g81Yq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDI2hbDfs5nfPU%2B4PZSrcA4BlIETD2h0JIT2C54nDnVP2V6Qt83LQqzVVdJvNyRen4rWZzmijel%2BjfUB%2BMyDeZPFuTfu8Mpzdlwmz3S6K30vQ9GeS3skWnGQfMU%2FkpGlKb2NmJemTgZTMw%2BPtLfeYVhJYEmsXkhRxqnt45sNNBEnjP4hbhqF6q7f7PYxXM5qrtH4zCJrhubEBLntvW0v55XnznhoGr62iTP3XKnLajqpYfEbxxO46IwZ%2FughyPUH613ReXPH1QQyyUhN8nDOVT8sK1xBUvms6HzdLZvQ4%2F7i41QzPGzbHbZkTxLdJBaSOnIoMUlu2lVIKtjzYxgDlEWK9FGAFzVWclXZrDfUzEue6T9wAVP2EaiU2dmJxygXj8rXtuAbLiVpn7ZHZEY2alrjtodQaPs3PNt9Rlul2Dns0ByWCrDHpcLjYz7w4S3d20eLgoZVa%2FJPwQTe0%2FKqjgQKOAJns7M39lZC%2FvlFCqwiuEBR9JVjfTwN%2BcBtZbmVEzDrHcwV8HtqF7Gp0j9NAwb8sxbibChWmhanZUiERdj9%2BNV8g3aGue6e02dee73uDZKoxQXww7yU0hmFR0Gkwui8cI3PrGfbNQzPCV7ckmwXCgXoMC1Vqv%2Bitl6NLCFvcjyBB6vLI1J1Ij1WwMNHSgr0GOqUBxLWS%2BQJEOm6eAX1xuSqH4yN25DAmobFMSHQFxEWAWGD3vzNGvX3M1Y4tLjGdo5MfiAoyInXfcn9kEIo84ZLPFa8w1AcO98FJHal%2FxoviNhWtrdD9lP3tZMUKDVStuMT1sEtaFDM2cB3JtgmjBet2jdIhJmLMTcqJ1ycAlxAyvBXaipZ3uEYvmaM0OSpT09hpwVD%2BgY5uXHEQyqLTA3IX6ftBUicj&X-Amz-Signature=a20e1ce3ebbbff5a96dc3f695b288845a4883533e98dd005bbf8ecda77d7857b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKNF5JVA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxS6nN%2FnEMfj3tccvnguIigpbcWHCzn2FpO4JewB%2BDCwIgdlpfxuwc1mCXCT3SRkn9%2B7SBbTcGwCTbtGNw5B7g81Yq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDI2hbDfs5nfPU%2B4PZSrcA4BlIETD2h0JIT2C54nDnVP2V6Qt83LQqzVVdJvNyRen4rWZzmijel%2BjfUB%2BMyDeZPFuTfu8Mpzdlwmz3S6K30vQ9GeS3skWnGQfMU%2FkpGlKb2NmJemTgZTMw%2BPtLfeYVhJYEmsXkhRxqnt45sNNBEnjP4hbhqF6q7f7PYxXM5qrtH4zCJrhubEBLntvW0v55XnznhoGr62iTP3XKnLajqpYfEbxxO46IwZ%2FughyPUH613ReXPH1QQyyUhN8nDOVT8sK1xBUvms6HzdLZvQ4%2F7i41QzPGzbHbZkTxLdJBaSOnIoMUlu2lVIKtjzYxgDlEWK9FGAFzVWclXZrDfUzEue6T9wAVP2EaiU2dmJxygXj8rXtuAbLiVpn7ZHZEY2alrjtodQaPs3PNt9Rlul2Dns0ByWCrDHpcLjYz7w4S3d20eLgoZVa%2FJPwQTe0%2FKqjgQKOAJns7M39lZC%2FvlFCqwiuEBR9JVjfTwN%2BcBtZbmVEzDrHcwV8HtqF7Gp0j9NAwb8sxbibChWmhanZUiERdj9%2BNV8g3aGue6e02dee73uDZKoxQXww7yU0hmFR0Gkwui8cI3PrGfbNQzPCV7ckmwXCgXoMC1Vqv%2Bitl6NLCFvcjyBB6vLI1J1Ij1WwMNHSgr0GOqUBxLWS%2BQJEOm6eAX1xuSqH4yN25DAmobFMSHQFxEWAWGD3vzNGvX3M1Y4tLjGdo5MfiAoyInXfcn9kEIo84ZLPFa8w1AcO98FJHal%2FxoviNhWtrdD9lP3tZMUKDVStuMT1sEtaFDM2cB3JtgmjBet2jdIhJmLMTcqJ1ycAlxAyvBXaipZ3uEYvmaM0OSpT09hpwVD%2BgY5uXHEQyqLTA3IX6ftBUicj&X-Amz-Signature=5cdc8c0983af526de1096d83fb672bdc19d296b18a1b864660e5915ef5f63615&X-Amz-SignedHeaders=host&x-id=GetObject)

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
