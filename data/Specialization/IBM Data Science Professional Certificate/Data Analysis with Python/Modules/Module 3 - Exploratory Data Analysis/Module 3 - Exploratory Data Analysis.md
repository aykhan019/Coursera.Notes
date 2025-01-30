

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SR5FIHJJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIExCsVTg5ZkfzwQlo9yrDOznmCZ3CKIvwPtSqLAqvWEcAiEA9Fy8HNddhhA3yt2YIutY6oUfHQ9NFWLC32qJto59OvUqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKBO%2FJ3TlZrcfgUVxSrcA8bH%2Bc6nIMKTnXLJZR9oVFfSABVXrxaSx3LLmoWaYzjgAQz1yZHXvdeCRJWkhNbbAPxhpzBWzPmNXbMP%2FR%2FSdh3qPP7VGy8m%2Bf5ok4zZFLJwYiQBdiIawwskidYo9qy4gpBJQz33%2Fh9gdPhONX2B75qzTIEuCxukMT2jg12%2BeUMoqJVSqe7x%2FyxvB7gNMuYCnnPTApzS%2BPJnmKv3acpdBHL6Bsn1ur%2FGMDN221sJ72fcNnrfAm54RcKb8buWLtFfLnXVyr8ZB5b3qx%2F4eM2Z4kuP8J2c8W5YxWwmW4fM1QwbFAkwES4nQDqiLFfTI%2FX80teJ11oz4bCN2xvNMcsBxZlleIeLq3EOFrutdIoiBYbN%2FcebVFZ0rSnF6gQAtCaubilYBYFO%2BVwB1YMCFLGcCwomkltQ0chamhk7lCUYs4fgIHRXFBDN6BERMIGvN2OuboZt%2BS5ZqcIJMmUhXgjP9IUabT0wmv3tUnPm2H43qLoyV%2FDENHhcJlskcxDhuIfyriUs%2FqVN5J1xpa9YFZwrkAwbIZtAqpc4OpocWF%2FqS5UXFdZihiT8Q3CB49AE9xkv9ZsnnTWqnw1S1z1QwZY2FvbV7KdGV4FiqUhHQYyEZ8cDMvy9%2FlUu7L9hJHpDMJmH7LwGOqUBhyWG29i2mxxI1ZVE%2FsWXNE1fRWD8dDinT1%2BYCOzKOJv7moDoryhagUZx2BlgsqV8iZQl9vUKTVLnn8ADImWZvODQrnkmzQlD4UN78lwd%2F%2BU2vQ873efD2P0VuIHRhupBV4es%2FWbzuBxCXwwyW7QEWA5641aiduVRNBUiRevEaoAh%2BfCSFIaC9ud262xvj4q9wrjm6hi81qo2JkNWoMy8b7rmX0Fy&X-Amz-Signature=4cc62cfaf6b49db2278bb9841a2c362fc4bcc9aaf40e6bbae74fda660389bbb6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SR5FIHJJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIExCsVTg5ZkfzwQlo9yrDOznmCZ3CKIvwPtSqLAqvWEcAiEA9Fy8HNddhhA3yt2YIutY6oUfHQ9NFWLC32qJto59OvUqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKBO%2FJ3TlZrcfgUVxSrcA8bH%2Bc6nIMKTnXLJZR9oVFfSABVXrxaSx3LLmoWaYzjgAQz1yZHXvdeCRJWkhNbbAPxhpzBWzPmNXbMP%2FR%2FSdh3qPP7VGy8m%2Bf5ok4zZFLJwYiQBdiIawwskidYo9qy4gpBJQz33%2Fh9gdPhONX2B75qzTIEuCxukMT2jg12%2BeUMoqJVSqe7x%2FyxvB7gNMuYCnnPTApzS%2BPJnmKv3acpdBHL6Bsn1ur%2FGMDN221sJ72fcNnrfAm54RcKb8buWLtFfLnXVyr8ZB5b3qx%2F4eM2Z4kuP8J2c8W5YxWwmW4fM1QwbFAkwES4nQDqiLFfTI%2FX80teJ11oz4bCN2xvNMcsBxZlleIeLq3EOFrutdIoiBYbN%2FcebVFZ0rSnF6gQAtCaubilYBYFO%2BVwB1YMCFLGcCwomkltQ0chamhk7lCUYs4fgIHRXFBDN6BERMIGvN2OuboZt%2BS5ZqcIJMmUhXgjP9IUabT0wmv3tUnPm2H43qLoyV%2FDENHhcJlskcxDhuIfyriUs%2FqVN5J1xpa9YFZwrkAwbIZtAqpc4OpocWF%2FqS5UXFdZihiT8Q3CB49AE9xkv9ZsnnTWqnw1S1z1QwZY2FvbV7KdGV4FiqUhHQYyEZ8cDMvy9%2FlUu7L9hJHpDMJmH7LwGOqUBhyWG29i2mxxI1ZVE%2FsWXNE1fRWD8dDinT1%2BYCOzKOJv7moDoryhagUZx2BlgsqV8iZQl9vUKTVLnn8ADImWZvODQrnkmzQlD4UN78lwd%2F%2BU2vQ873efD2P0VuIHRhupBV4es%2FWbzuBxCXwwyW7QEWA5641aiduVRNBUiRevEaoAh%2BfCSFIaC9ud262xvj4q9wrjm6hi81qo2JkNWoMy8b7rmX0Fy&X-Amz-Signature=5f89fe462ed4275754aad4bb3f22f2bff1a87e9d30f4d5d6d5ec4de160f0c517&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SR5FIHJJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIExCsVTg5ZkfzwQlo9yrDOznmCZ3CKIvwPtSqLAqvWEcAiEA9Fy8HNddhhA3yt2YIutY6oUfHQ9NFWLC32qJto59OvUqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKBO%2FJ3TlZrcfgUVxSrcA8bH%2Bc6nIMKTnXLJZR9oVFfSABVXrxaSx3LLmoWaYzjgAQz1yZHXvdeCRJWkhNbbAPxhpzBWzPmNXbMP%2FR%2FSdh3qPP7VGy8m%2Bf5ok4zZFLJwYiQBdiIawwskidYo9qy4gpBJQz33%2Fh9gdPhONX2B75qzTIEuCxukMT2jg12%2BeUMoqJVSqe7x%2FyxvB7gNMuYCnnPTApzS%2BPJnmKv3acpdBHL6Bsn1ur%2FGMDN221sJ72fcNnrfAm54RcKb8buWLtFfLnXVyr8ZB5b3qx%2F4eM2Z4kuP8J2c8W5YxWwmW4fM1QwbFAkwES4nQDqiLFfTI%2FX80teJ11oz4bCN2xvNMcsBxZlleIeLq3EOFrutdIoiBYbN%2FcebVFZ0rSnF6gQAtCaubilYBYFO%2BVwB1YMCFLGcCwomkltQ0chamhk7lCUYs4fgIHRXFBDN6BERMIGvN2OuboZt%2BS5ZqcIJMmUhXgjP9IUabT0wmv3tUnPm2H43qLoyV%2FDENHhcJlskcxDhuIfyriUs%2FqVN5J1xpa9YFZwrkAwbIZtAqpc4OpocWF%2FqS5UXFdZihiT8Q3CB49AE9xkv9ZsnnTWqnw1S1z1QwZY2FvbV7KdGV4FiqUhHQYyEZ8cDMvy9%2FlUu7L9hJHpDMJmH7LwGOqUBhyWG29i2mxxI1ZVE%2FsWXNE1fRWD8dDinT1%2BYCOzKOJv7moDoryhagUZx2BlgsqV8iZQl9vUKTVLnn8ADImWZvODQrnkmzQlD4UN78lwd%2F%2BU2vQ873efD2P0VuIHRhupBV4es%2FWbzuBxCXwwyW7QEWA5641aiduVRNBUiRevEaoAh%2BfCSFIaC9ud262xvj4q9wrjm6hi81qo2JkNWoMy8b7rmX0Fy&X-Amz-Signature=2b9e2abb5b042fbe4ef51a6b2609d0bb456234f8ec38b7d5204f0973b04195d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DVHKNNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDyHScqjp2fG%2Fo%2FS2G%2FpGuub%2FajEzgAmilqh8DWNpvBAiAS3RMZZhoXqyDvUIplU9%2Bdae2B0op6lHWRc76Ud2nGLSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FU6fhbYzjfXg1XSbKtwDdnmmQohVHkzUZWnE9CdJCzI%2FckH4jx0IL0X4pXR%2FJlcIl31QMsoSdBd5nSKw2esYo202s7mDRA%2FDVjzdR8ZQcAp0HehCNTsg4soCM1qiVbWUpASWd6mPpuTlk4eEHtMadoTvzI1rcKRi%2Fpn7oRj01ySaEfU1QnfgF0aRDvrl0ou3Mp4CHvNBooVPhq7ElPUYlCx6bqW59qCDAv5G248R%2BwQqHk6ENboF4dVIPJ1WWDT0tFtOEupT53jwfaW41JgfsFlnv9%2BV5f9QAKClsAdsY8ClWLSbKuzN%2FcF2igwfrbxlAxn2hOK83FwYgSt3hB4F%2FOj6FSfBeVc6dc7boPMFcAKHroHs68uNhqutgYPkCZzJGVsP6xPzkw05VFu5dO%2BVa6pUtNSdv7RoklFeC7KOKMFZv15GLz76DRbCy1PNRCjzWiSFxmLZSb0kkLduH30pGVSxFncPmbde9PX5XgbGgZfe2nxc%2F7CHRDQ9aSQ9fHDSSJT5Olqkfb0kP5YUcQYvXigPHLgSwHox95oQfpEFr8pKxruMQJxAzRAg3nt%2BCHMYp6mvV93iXb7EUPuScs6RymmmvHw3R1gzrp%2FIXlHzVYUWyK8QwyZFuYG7LEw9lgQGWyNqATklKOfBkYow6obsvAY6pgE%2B9ouyUcWm61fEn54w4u6NNQ4nLkW0X54TgvWFfhewBMI1%2BM38dW8yztKH53m5HRPEECi07yftToNzfj%2FrL4kxr1j6glF%2FjaF6N9ROSW6BNktbiTHUVH54%2B8%2BvInhbGvWVGJff9elSGXA%2FnUwjCcEWxtyULbr73AyzzM8M5CZK7U2%2BYeYEYZd%2BTmp2T%2FvIgzfRoXl%2B4RaIk%2F5RZNKTA7EtUef0hsRI&X-Amz-Signature=9c2b7a714728165a777774f0190ded07b7270ea81d3062e4fcae36a326ed01c3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DVHKNNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDyHScqjp2fG%2Fo%2FS2G%2FpGuub%2FajEzgAmilqh8DWNpvBAiAS3RMZZhoXqyDvUIplU9%2Bdae2B0op6lHWRc76Ud2nGLSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FU6fhbYzjfXg1XSbKtwDdnmmQohVHkzUZWnE9CdJCzI%2FckH4jx0IL0X4pXR%2FJlcIl31QMsoSdBd5nSKw2esYo202s7mDRA%2FDVjzdR8ZQcAp0HehCNTsg4soCM1qiVbWUpASWd6mPpuTlk4eEHtMadoTvzI1rcKRi%2Fpn7oRj01ySaEfU1QnfgF0aRDvrl0ou3Mp4CHvNBooVPhq7ElPUYlCx6bqW59qCDAv5G248R%2BwQqHk6ENboF4dVIPJ1WWDT0tFtOEupT53jwfaW41JgfsFlnv9%2BV5f9QAKClsAdsY8ClWLSbKuzN%2FcF2igwfrbxlAxn2hOK83FwYgSt3hB4F%2FOj6FSfBeVc6dc7boPMFcAKHroHs68uNhqutgYPkCZzJGVsP6xPzkw05VFu5dO%2BVa6pUtNSdv7RoklFeC7KOKMFZv15GLz76DRbCy1PNRCjzWiSFxmLZSb0kkLduH30pGVSxFncPmbde9PX5XgbGgZfe2nxc%2F7CHRDQ9aSQ9fHDSSJT5Olqkfb0kP5YUcQYvXigPHLgSwHox95oQfpEFr8pKxruMQJxAzRAg3nt%2BCHMYp6mvV93iXb7EUPuScs6RymmmvHw3R1gzrp%2FIXlHzVYUWyK8QwyZFuYG7LEw9lgQGWyNqATklKOfBkYow6obsvAY6pgE%2B9ouyUcWm61fEn54w4u6NNQ4nLkW0X54TgvWFfhewBMI1%2BM38dW8yztKH53m5HRPEECi07yftToNzfj%2FrL4kxr1j6glF%2FjaF6N9ROSW6BNktbiTHUVH54%2B8%2BvInhbGvWVGJff9elSGXA%2FnUwjCcEWxtyULbr73AyzzM8M5CZK7U2%2BYeYEYZd%2BTmp2T%2FvIgzfRoXl%2B4RaIk%2F5RZNKTA7EtUef0hsRI&X-Amz-Signature=ee16776765d00ad8f60e9173f3813e63e76e1b228349e92f503eb9f4c126afd4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DVHKNNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDyHScqjp2fG%2Fo%2FS2G%2FpGuub%2FajEzgAmilqh8DWNpvBAiAS3RMZZhoXqyDvUIplU9%2Bdae2B0op6lHWRc76Ud2nGLSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FU6fhbYzjfXg1XSbKtwDdnmmQohVHkzUZWnE9CdJCzI%2FckH4jx0IL0X4pXR%2FJlcIl31QMsoSdBd5nSKw2esYo202s7mDRA%2FDVjzdR8ZQcAp0HehCNTsg4soCM1qiVbWUpASWd6mPpuTlk4eEHtMadoTvzI1rcKRi%2Fpn7oRj01ySaEfU1QnfgF0aRDvrl0ou3Mp4CHvNBooVPhq7ElPUYlCx6bqW59qCDAv5G248R%2BwQqHk6ENboF4dVIPJ1WWDT0tFtOEupT53jwfaW41JgfsFlnv9%2BV5f9QAKClsAdsY8ClWLSbKuzN%2FcF2igwfrbxlAxn2hOK83FwYgSt3hB4F%2FOj6FSfBeVc6dc7boPMFcAKHroHs68uNhqutgYPkCZzJGVsP6xPzkw05VFu5dO%2BVa6pUtNSdv7RoklFeC7KOKMFZv15GLz76DRbCy1PNRCjzWiSFxmLZSb0kkLduH30pGVSxFncPmbde9PX5XgbGgZfe2nxc%2F7CHRDQ9aSQ9fHDSSJT5Olqkfb0kP5YUcQYvXigPHLgSwHox95oQfpEFr8pKxruMQJxAzRAg3nt%2BCHMYp6mvV93iXb7EUPuScs6RymmmvHw3R1gzrp%2FIXlHzVYUWyK8QwyZFuYG7LEw9lgQGWyNqATklKOfBkYow6obsvAY6pgE%2B9ouyUcWm61fEn54w4u6NNQ4nLkW0X54TgvWFfhewBMI1%2BM38dW8yztKH53m5HRPEECi07yftToNzfj%2FrL4kxr1j6glF%2FjaF6N9ROSW6BNktbiTHUVH54%2B8%2BvInhbGvWVGJff9elSGXA%2FnUwjCcEWxtyULbr73AyzzM8M5CZK7U2%2BYeYEYZd%2BTmp2T%2FvIgzfRoXl%2B4RaIk%2F5RZNKTA7EtUef0hsRI&X-Amz-Signature=8becf49318a3d99739c3ad12ae9ed4069c035d5b962f28c5f8bf429e37102f26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DVHKNNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDyHScqjp2fG%2Fo%2FS2G%2FpGuub%2FajEzgAmilqh8DWNpvBAiAS3RMZZhoXqyDvUIplU9%2Bdae2B0op6lHWRc76Ud2nGLSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FU6fhbYzjfXg1XSbKtwDdnmmQohVHkzUZWnE9CdJCzI%2FckH4jx0IL0X4pXR%2FJlcIl31QMsoSdBd5nSKw2esYo202s7mDRA%2FDVjzdR8ZQcAp0HehCNTsg4soCM1qiVbWUpASWd6mPpuTlk4eEHtMadoTvzI1rcKRi%2Fpn7oRj01ySaEfU1QnfgF0aRDvrl0ou3Mp4CHvNBooVPhq7ElPUYlCx6bqW59qCDAv5G248R%2BwQqHk6ENboF4dVIPJ1WWDT0tFtOEupT53jwfaW41JgfsFlnv9%2BV5f9QAKClsAdsY8ClWLSbKuzN%2FcF2igwfrbxlAxn2hOK83FwYgSt3hB4F%2FOj6FSfBeVc6dc7boPMFcAKHroHs68uNhqutgYPkCZzJGVsP6xPzkw05VFu5dO%2BVa6pUtNSdv7RoklFeC7KOKMFZv15GLz76DRbCy1PNRCjzWiSFxmLZSb0kkLduH30pGVSxFncPmbde9PX5XgbGgZfe2nxc%2F7CHRDQ9aSQ9fHDSSJT5Olqkfb0kP5YUcQYvXigPHLgSwHox95oQfpEFr8pKxruMQJxAzRAg3nt%2BCHMYp6mvV93iXb7EUPuScs6RymmmvHw3R1gzrp%2FIXlHzVYUWyK8QwyZFuYG7LEw9lgQGWyNqATklKOfBkYow6obsvAY6pgE%2B9ouyUcWm61fEn54w4u6NNQ4nLkW0X54TgvWFfhewBMI1%2BM38dW8yztKH53m5HRPEECi07yftToNzfj%2FrL4kxr1j6glF%2FjaF6N9ROSW6BNktbiTHUVH54%2B8%2BvInhbGvWVGJff9elSGXA%2FnUwjCcEWxtyULbr73AyzzM8M5CZK7U2%2BYeYEYZd%2BTmp2T%2FvIgzfRoXl%2B4RaIk%2F5RZNKTA7EtUef0hsRI&X-Amz-Signature=30453db869b8b321de7ab855f86716bc8d5230791a69e6baedcd8694dcc1c2dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DVHKNNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDyHScqjp2fG%2Fo%2FS2G%2FpGuub%2FajEzgAmilqh8DWNpvBAiAS3RMZZhoXqyDvUIplU9%2Bdae2B0op6lHWRc76Ud2nGLSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FU6fhbYzjfXg1XSbKtwDdnmmQohVHkzUZWnE9CdJCzI%2FckH4jx0IL0X4pXR%2FJlcIl31QMsoSdBd5nSKw2esYo202s7mDRA%2FDVjzdR8ZQcAp0HehCNTsg4soCM1qiVbWUpASWd6mPpuTlk4eEHtMadoTvzI1rcKRi%2Fpn7oRj01ySaEfU1QnfgF0aRDvrl0ou3Mp4CHvNBooVPhq7ElPUYlCx6bqW59qCDAv5G248R%2BwQqHk6ENboF4dVIPJ1WWDT0tFtOEupT53jwfaW41JgfsFlnv9%2BV5f9QAKClsAdsY8ClWLSbKuzN%2FcF2igwfrbxlAxn2hOK83FwYgSt3hB4F%2FOj6FSfBeVc6dc7boPMFcAKHroHs68uNhqutgYPkCZzJGVsP6xPzkw05VFu5dO%2BVa6pUtNSdv7RoklFeC7KOKMFZv15GLz76DRbCy1PNRCjzWiSFxmLZSb0kkLduH30pGVSxFncPmbde9PX5XgbGgZfe2nxc%2F7CHRDQ9aSQ9fHDSSJT5Olqkfb0kP5YUcQYvXigPHLgSwHox95oQfpEFr8pKxruMQJxAzRAg3nt%2BCHMYp6mvV93iXb7EUPuScs6RymmmvHw3R1gzrp%2FIXlHzVYUWyK8QwyZFuYG7LEw9lgQGWyNqATklKOfBkYow6obsvAY6pgE%2B9ouyUcWm61fEn54w4u6NNQ4nLkW0X54TgvWFfhewBMI1%2BM38dW8yztKH53m5HRPEECi07yftToNzfj%2FrL4kxr1j6glF%2FjaF6N9ROSW6BNktbiTHUVH54%2B8%2BvInhbGvWVGJff9elSGXA%2FnUwjCcEWxtyULbr73AyzzM8M5CZK7U2%2BYeYEYZd%2BTmp2T%2FvIgzfRoXl%2B4RaIk%2F5RZNKTA7EtUef0hsRI&X-Amz-Signature=165a04a06c02b12d3cf4bbab541215219121ac5e70aa1872d2df28d174becfb9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DVHKNNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDyHScqjp2fG%2Fo%2FS2G%2FpGuub%2FajEzgAmilqh8DWNpvBAiAS3RMZZhoXqyDvUIplU9%2Bdae2B0op6lHWRc76Ud2nGLSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FU6fhbYzjfXg1XSbKtwDdnmmQohVHkzUZWnE9CdJCzI%2FckH4jx0IL0X4pXR%2FJlcIl31QMsoSdBd5nSKw2esYo202s7mDRA%2FDVjzdR8ZQcAp0HehCNTsg4soCM1qiVbWUpASWd6mPpuTlk4eEHtMadoTvzI1rcKRi%2Fpn7oRj01ySaEfU1QnfgF0aRDvrl0ou3Mp4CHvNBooVPhq7ElPUYlCx6bqW59qCDAv5G248R%2BwQqHk6ENboF4dVIPJ1WWDT0tFtOEupT53jwfaW41JgfsFlnv9%2BV5f9QAKClsAdsY8ClWLSbKuzN%2FcF2igwfrbxlAxn2hOK83FwYgSt3hB4F%2FOj6FSfBeVc6dc7boPMFcAKHroHs68uNhqutgYPkCZzJGVsP6xPzkw05VFu5dO%2BVa6pUtNSdv7RoklFeC7KOKMFZv15GLz76DRbCy1PNRCjzWiSFxmLZSb0kkLduH30pGVSxFncPmbde9PX5XgbGgZfe2nxc%2F7CHRDQ9aSQ9fHDSSJT5Olqkfb0kP5YUcQYvXigPHLgSwHox95oQfpEFr8pKxruMQJxAzRAg3nt%2BCHMYp6mvV93iXb7EUPuScs6RymmmvHw3R1gzrp%2FIXlHzVYUWyK8QwyZFuYG7LEw9lgQGWyNqATklKOfBkYow6obsvAY6pgE%2B9ouyUcWm61fEn54w4u6NNQ4nLkW0X54TgvWFfhewBMI1%2BM38dW8yztKH53m5HRPEECi07yftToNzfj%2FrL4kxr1j6glF%2FjaF6N9ROSW6BNktbiTHUVH54%2B8%2BvInhbGvWVGJff9elSGXA%2FnUwjCcEWxtyULbr73AyzzM8M5CZK7U2%2BYeYEYZd%2BTmp2T%2FvIgzfRoXl%2B4RaIk%2F5RZNKTA7EtUef0hsRI&X-Amz-Signature=04d16e45ed4d902a433b1845e6171f55cd02149690be128040de0e7d3c18ea89&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK2EZH5C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrYrj%2FvT%2BsThNJVIr9PNYX%2FblUKMClW%2FADEx6ihgNY9QIhAPLrjAjkc2%2BpWQd5pyax4bUt9DmsEhvYpRlnDDtxCcTlKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxThs4iPgqvi8fAEUoq3APXgy1WXRyH770lPKw8nOEgADXYg7ROU%2BqmNqMBqvjbj442NY%2BzO%2BTFWIFMyuC%2FCMM8%2B4zTQbrnCrba2KSlgYrbmhrKV%2Fov24WYJIIzL9AxfPjtNXHeKVQS22aKzIf0qtxxcJiU6nmwWYFWKGyi1O3x99n5DyE%2FDIqcDPDIYjGAajgfncovoyOdlXHKOQ66HAsEJFc6LyqwzHJ%2FJ2zYjCQSNWicXpcRp%2BtmOQ8B2HoFtYud%2FBa0PGn5nR%2FQResSNMC2KG9nkKNYjfNq4mn2tR2x%2BAbRemRErOrltSOaRHNOnuMG1nc%2F2NHoTeMAafKn%2F63TpKYMJC6VM%2BkuziRBgYBeH5B0XrJhxyBzUy%2FJDf%2FkZKR7c8PefFqWLE7W9W%2Ft6NTnZ%2Fxd%2BWbzFh8W38XyEQ9WLdF7AFYy9Yb2Jx2Hv%2B2kvt%2BsxzZumlTqNUz%2FoA7RQIHmZiYNSSq6nfDuL75e3v6cLlU7Y7x1sSXpWumQ8bWy5T05lVLJnrvxdXcEIjSY66PWGqPYmS3m3R2jfkudqeuzEFjpqEsTLJh74qy8xV3gkHTziH8xddDNRf28ANtQl4%2B8y4sphcmd%2Bjm5sdZO7BEAtOVzv%2BO3fUucrCCQveQ7AdOMBBX9iMA9wep3TDC6huy8BjqkAYE%2By8%2BFj19OKmNJmGhFNCEihqPYYTQ6IM4xNsNWBPzYIszslfGTs7TUOCHNXdVG3eNG4EtCZi2e9ERnLdJSvnqbJsWN4IQy9S8c1i6EhxeAdwcgChCye1pKX7YQOrgHVMZFVJW2HgzELvpGq6EnD0nVat%2B6HWNDOFqZET7NES9U6x2Yg%2FianQgmiA96%2FPdjdujbgSMAX%2FiC1HrmblWdKK9pNgWq&X-Amz-Signature=8141759cbafd280e29bf1c2fa028cf0a553f29a0dc04284750a8c2dea97d00c7&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJP6FN3D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHySnhVYz2aPs5PLXYPQk0lLMt2hgbZenWam3hZug%2BBwAiEA5DYkIzrNBIfki3s87NoFnLEl3LjIGGl1UECBSBsEOc8qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqWPH%2BRY0DLDXGN5yrcAyEMHx5y0MeM%2F1WvP3IboLmJADQAjRQi999VQ6RGjwjE4YXgtLthaXBkth9vAppjsKscjAs3ZV6FQTWiik4NBtNH1U699Ir43%2FKiFBVGxEDmFAWRZnGsLxBz6CkbIN5BIEJ%2BaFngE5dsq0rFkSyxQV2w2O4B2CP5%2BwqFxtZV2YAcO61uwnGeO3vvpgnRO17LOrbWhLkl%2FpHHvcMCgWtzOnp%2F65Z8OUZS5wjnJetyuuOaTAmENO1rGt8xQy6QH5xwybSz%2FQRoz%2FtCmWcyufrW%2BFOrXeYpqbxbYpyeDgQv8Rk7LUJG0rldmUU8PLf7p1BHokh2RiJyCeeoXTKe1FppUK3RO6ZP8tWANkp2fMx7ORu4IGgQIqRoYXNJfj%2BGAYRm%2BbMHeMWS85TIkLHc00yf%2BMkq5kvJJuj3kw9aA20T3QqXGsjs1CzRZvrJD4%2FUoqSDIz36%2Fvl0M44pMjKtAp9vnDAbZOeXaL2eKskUFQaD0Cgerz2FISYduk5KC6JG4t7G%2FQ6ZUjTryTuQdgW1FEEUfDuSZLkBBf6BZxlHTJZaOB98jGqUveSrlgvQmc0FmZAyX%2F%2B435exlQU3t2AVn4wErFKiOec8tWOgcjzC3PqwMxYPeoGySy9udY%2B6c1yMMJOH7LwGOqUBXB8VQo%2BgyJqCQA8UpVfmkUVNQ%2BSMxm6I%2BIxXmUufGFZAsMATzy%2Bn5vKDisOI7QejxtEPsvwlqnNTpxh30fYY5gjsE6XxnR%2B4IVD7uuq4GZmSYhmhu9lumuwrqdwnw6tD2wkdbHNB1BhF7dMDlrRA2wKa1Iy2Nx5xhwAoyHne4QdiPFZqe6eqQXY45dfHav9nvW9101wBUeXF2IVYC8UEJGeoqIrz&X-Amz-Signature=3d8dc98a2783b99eea283a97d4bf29b155447036dc5374ce5485a1ff0ee7f7d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DVHKNNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDyHScqjp2fG%2Fo%2FS2G%2FpGuub%2FajEzgAmilqh8DWNpvBAiAS3RMZZhoXqyDvUIplU9%2Bdae2B0op6lHWRc76Ud2nGLSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FU6fhbYzjfXg1XSbKtwDdnmmQohVHkzUZWnE9CdJCzI%2FckH4jx0IL0X4pXR%2FJlcIl31QMsoSdBd5nSKw2esYo202s7mDRA%2FDVjzdR8ZQcAp0HehCNTsg4soCM1qiVbWUpASWd6mPpuTlk4eEHtMadoTvzI1rcKRi%2Fpn7oRj01ySaEfU1QnfgF0aRDvrl0ou3Mp4CHvNBooVPhq7ElPUYlCx6bqW59qCDAv5G248R%2BwQqHk6ENboF4dVIPJ1WWDT0tFtOEupT53jwfaW41JgfsFlnv9%2BV5f9QAKClsAdsY8ClWLSbKuzN%2FcF2igwfrbxlAxn2hOK83FwYgSt3hB4F%2FOj6FSfBeVc6dc7boPMFcAKHroHs68uNhqutgYPkCZzJGVsP6xPzkw05VFu5dO%2BVa6pUtNSdv7RoklFeC7KOKMFZv15GLz76DRbCy1PNRCjzWiSFxmLZSb0kkLduH30pGVSxFncPmbde9PX5XgbGgZfe2nxc%2F7CHRDQ9aSQ9fHDSSJT5Olqkfb0kP5YUcQYvXigPHLgSwHox95oQfpEFr8pKxruMQJxAzRAg3nt%2BCHMYp6mvV93iXb7EUPuScs6RymmmvHw3R1gzrp%2FIXlHzVYUWyK8QwyZFuYG7LEw9lgQGWyNqATklKOfBkYow6obsvAY6pgE%2B9ouyUcWm61fEn54w4u6NNQ4nLkW0X54TgvWFfhewBMI1%2BM38dW8yztKH53m5HRPEECi07yftToNzfj%2FrL4kxr1j6glF%2FjaF6N9ROSW6BNktbiTHUVH54%2B8%2BvInhbGvWVGJff9elSGXA%2FnUwjCcEWxtyULbr73AyzzM8M5CZK7U2%2BYeYEYZd%2BTmp2T%2FvIgzfRoXl%2B4RaIk%2F5RZNKTA7EtUef0hsRI&X-Amz-Signature=1cb8a5d8e2ab38f14d1d5a89629fc9e42ac7e73d5ad934866bf8e0dce81c8a9c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DVHKNNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDyHScqjp2fG%2Fo%2FS2G%2FpGuub%2FajEzgAmilqh8DWNpvBAiAS3RMZZhoXqyDvUIplU9%2Bdae2B0op6lHWRc76Ud2nGLSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FU6fhbYzjfXg1XSbKtwDdnmmQohVHkzUZWnE9CdJCzI%2FckH4jx0IL0X4pXR%2FJlcIl31QMsoSdBd5nSKw2esYo202s7mDRA%2FDVjzdR8ZQcAp0HehCNTsg4soCM1qiVbWUpASWd6mPpuTlk4eEHtMadoTvzI1rcKRi%2Fpn7oRj01ySaEfU1QnfgF0aRDvrl0ou3Mp4CHvNBooVPhq7ElPUYlCx6bqW59qCDAv5G248R%2BwQqHk6ENboF4dVIPJ1WWDT0tFtOEupT53jwfaW41JgfsFlnv9%2BV5f9QAKClsAdsY8ClWLSbKuzN%2FcF2igwfrbxlAxn2hOK83FwYgSt3hB4F%2FOj6FSfBeVc6dc7boPMFcAKHroHs68uNhqutgYPkCZzJGVsP6xPzkw05VFu5dO%2BVa6pUtNSdv7RoklFeC7KOKMFZv15GLz76DRbCy1PNRCjzWiSFxmLZSb0kkLduH30pGVSxFncPmbde9PX5XgbGgZfe2nxc%2F7CHRDQ9aSQ9fHDSSJT5Olqkfb0kP5YUcQYvXigPHLgSwHox95oQfpEFr8pKxruMQJxAzRAg3nt%2BCHMYp6mvV93iXb7EUPuScs6RymmmvHw3R1gzrp%2FIXlHzVYUWyK8QwyZFuYG7LEw9lgQGWyNqATklKOfBkYow6obsvAY6pgE%2B9ouyUcWm61fEn54w4u6NNQ4nLkW0X54TgvWFfhewBMI1%2BM38dW8yztKH53m5HRPEECi07yftToNzfj%2FrL4kxr1j6glF%2FjaF6N9ROSW6BNktbiTHUVH54%2B8%2BvInhbGvWVGJff9elSGXA%2FnUwjCcEWxtyULbr73AyzzM8M5CZK7U2%2BYeYEYZd%2BTmp2T%2FvIgzfRoXl%2B4RaIk%2F5RZNKTA7EtUef0hsRI&X-Amz-Signature=f4fe2db96c024d8cccc7d4c63607f53891c98eec95f40e3fa68f96884ca572e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DVHKNNU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDyHScqjp2fG%2Fo%2FS2G%2FpGuub%2FajEzgAmilqh8DWNpvBAiAS3RMZZhoXqyDvUIplU9%2Bdae2B0op6lHWRc76Ud2nGLSqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FU6fhbYzjfXg1XSbKtwDdnmmQohVHkzUZWnE9CdJCzI%2FckH4jx0IL0X4pXR%2FJlcIl31QMsoSdBd5nSKw2esYo202s7mDRA%2FDVjzdR8ZQcAp0HehCNTsg4soCM1qiVbWUpASWd6mPpuTlk4eEHtMadoTvzI1rcKRi%2Fpn7oRj01ySaEfU1QnfgF0aRDvrl0ou3Mp4CHvNBooVPhq7ElPUYlCx6bqW59qCDAv5G248R%2BwQqHk6ENboF4dVIPJ1WWDT0tFtOEupT53jwfaW41JgfsFlnv9%2BV5f9QAKClsAdsY8ClWLSbKuzN%2FcF2igwfrbxlAxn2hOK83FwYgSt3hB4F%2FOj6FSfBeVc6dc7boPMFcAKHroHs68uNhqutgYPkCZzJGVsP6xPzkw05VFu5dO%2BVa6pUtNSdv7RoklFeC7KOKMFZv15GLz76DRbCy1PNRCjzWiSFxmLZSb0kkLduH30pGVSxFncPmbde9PX5XgbGgZfe2nxc%2F7CHRDQ9aSQ9fHDSSJT5Olqkfb0kP5YUcQYvXigPHLgSwHox95oQfpEFr8pKxruMQJxAzRAg3nt%2BCHMYp6mvV93iXb7EUPuScs6RymmmvHw3R1gzrp%2FIXlHzVYUWyK8QwyZFuYG7LEw9lgQGWyNqATklKOfBkYow6obsvAY6pgE%2B9ouyUcWm61fEn54w4u6NNQ4nLkW0X54TgvWFfhewBMI1%2BM38dW8yztKH53m5HRPEECi07yftToNzfj%2FrL4kxr1j6glF%2FjaF6N9ROSW6BNktbiTHUVH54%2B8%2BvInhbGvWVGJff9elSGXA%2FnUwjCcEWxtyULbr73AyzzM8M5CZK7U2%2BYeYEYZd%2BTmp2T%2FvIgzfRoXl%2B4RaIk%2F5RZNKTA7EtUef0hsRI&X-Amz-Signature=8139a477c7f2340aacfab4123223d25c9189a6913c35ea23aff825bed7cfd1c2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6VIVCOY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDv1NCiN17atRs%2F4fvPBZ7Y0t1FU052rWhsFIoChD%2FWjAIgbAFdpbjSVVaQzXLr5e6LWNABrPg4qUsrR0cNEVGrjeYqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHZQDQRGN2%2FbG9BpWCrcA15LHVp5QKsDvr4V2HggvIJqU5SwVe6%2BNiKwM7nj5ZuIU3EYh1Aj2Z%2B1mzcZWrJ%2B7BdOJ%2B1Ta8%2FO%2BpWdg9BZWCCxmF8g7YK1CCtwSFtpWZNVnH%2BSN6sr%2F28PWM6StdzrxkvZtHu3QpMnP%2Fvw%2F%2BEr061iFbiecHsUMypXt%2Bw4rlrdt1kZs4oIzSIRoeBfUD3Of8NR5b%2FMt2qNRwtu6YeQCIe332xCZw1ETUGlUoJv3UZev1uPu9sO4s8Ro09GKMWifEatk%2F5ISSXdJ20amth2Gn9Spdn5tKn9v1VY6N%2FbU33Cjn2YA5%2FXEaiefpK83tm8aiLmzwYXmJUAaWWXgdmlIJc3%2FZsMJ7UDhxxDsov6UKwJH9sstxcGLP3n3XvnJ37GjFJ5bXibC2QFy74dslfkRlrNY18QgghmDzUxAcbPTAKwilwBcJn20conBLwvqFPtHzG8%2BtQ1oO5xwfL%2F0K8GvUJ5IHWEPajo7SVPkXIwmCWDrC63GmqymZWDvXn7kAEVkaiLhNqWFuS22%2BzNUyZ7z%2Fz%2BGpeaJ1ykSc0RlmVg1lqAU1S8tdIP2NcGomuBdSA%2B%2B8aAwV1I18TqwYtSAmItumNhNA8Q36kEmMvDJkLnN2khWOuN%2FLP2YN5%2BuT4yMMCG7LwGOqUBsdsF9LeKUWVpaiwaNj0NhFILwjeylDFnL2iAgPtrWVb55TVM9XT%2BseEdz4F271xSrsYCXO7kl1KnfE72AJfIJ85zRDLqqhKAiUT1xfbfXHpD6YkUxeBuBl374bCuJtSCSA5%2B3qm5VQ%2B1nQGs5YqS9Yv2TmwFku3%2Bc5mpzSol8x4dBFA6F9mCmDiksSQ37fhuKqM309JQTqqUvd3dqK4DMr%2Fp%2B6WT&X-Amz-Signature=c67f651b00441eeb2515b623a26421ac26decae5a3230cc065512ff184ac4919&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V3BZFIG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGeFGYiAc65MzDRKyEa91PQuKgJt87KUVkTPUB8jdhOSAiEAx8MSa4uytbkr5MwBbWwBaoTVegE7jZmDpRYU6kdgLt8qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNWLHwr8C6FiH3NsnyrcAz%2BpJTzBx7mOD5%2FoYbaeLUE%2Fly%2BRqf8Cb%2Bj1l2sUFtY1QNYItvfCiiUPWw1EE%2FQ1aOurFrYQc%2F9ySB%2FLN5oaPPYoEzQkVZeZEiqVm9Ghxma9bOsIEMXeoMHfbLI4Gz3RE%2BTIgCQhga3KFUdjZJIAg1zzVHW1Vx2XqsbUMGetPifq87RZQO9T1P8yjHaRXQAztWMeXQxAAf5PGpZQ5WuIUm2MeqAACFHPTvFf%2BuBbhmnd%2FYTRv%2BV45uAUBVJeXsVpBPNRYhIY17SXhu8Jaf21PWU3%2FJ%2BTjT8amGtPjgTJrk%2BJnT4yaosowV70dEHyCOlSki0BUKvTJtu7qyRbbdivTRGOWRq5oAbNuVzFrjL6lriziza6AA2okW2FHh%2BkHnKpev7Py7r7Zhp9Apq8bc2bv6EpgFSIM%2FcqUcYNK%2FtnpR6at1gFTSkA36Xj7R1IYqBe%2FAHk8jaxqPn7bZ3Pb5ffd0I4LAFK%2BH5EwUURkup95EtQ52cIqM91BvC5mYAlUz7JN2jxZdz1uyKUbut3B5b6GArGOugcNP7%2BzBPHUEQbuxfvFWuXcI6Y2bB%2F%2FTzett7WcjGRrqorNOKHAvvf3erG%2B8dOslgSBeg35ABulxv71fAvbQWNANml%2BaCzk6B%2FMIGH7LwGOqUB3tfXvBXjcOzVSiIJMojwLfNV4akTifZJc27FW0qyZcMzGikn7oE9WBs7FdVIAmjq1Gu%2FSnCtFluKDPLxutY7wAOysg%2F%2BLqUR30LXRv9PqKJkhE9rzfaIxOwg%2BkMADyt%2BMQK6M5fBQgocMOZk23nq18YUeni%2B6WZW0iHEyH6BoH9V2A9H%2F2mHQ0%2BVLPkSem6MrosBtsQmXAbuILYxMjR9R%2FAPZKFV&X-Amz-Signature=7fc65614923f3ecf48353334c20f80912d333ce0df590d4048e9e8a7c20fafdb&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6G5NESE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbZRzeWDiFw31iYkflL98V3myNzOr3HHBDPl1ZBDrZTAiEAvWR%2BuJdvzFxilPUVcVh1JzHi0L8KrAcdQiWn8ielQOsqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMN6Us5VzSzt6HtbmircA2XpUSrOxhWHuTmFi1DIp56mfBI6%2F0zmrCzfV%2FGvXugrlDl20Z1WB14Frwqvi2HogVvPCROf4ACROKsASP5HoycmQ95YAKaD7%2B7pcWolyxi%2Fifymoy2EfWugGVsIdKP6HnWele4RVebsLzsTnRrKaEMdKnDN8Ea2GK%2F4eSyJKzEIugGEssn1%2Fn85qF%2F6CWTosAwOhDvddCPBfLCSmhNPU0eqIo1J8UT27B3oKotM5LxfKEhwA31s4iSgZ8urPNxoBNBZCGtcJVPiCNmBCffwNs7pQskSJ5GVTPYGf98yBPL9PTdV%2B%2BhmlsTPpQDLbO%2FqNnmYYbh0liPHNY9BcvvAPHDJWbRSaU%2BNzJKPckYbOSAck6JeD2QPAu5Op1rAjXugs%2BPZXu0bJk2QGD%2BQY1sTMksESi23P0Ef%2F78f3WNzzLcpkGRfs%2BUtw4WTHvtcwU1143qwrZ%2BPHuKCfT45epsorDAs4TJZvhxqN%2F16GX31TvEpgoetJiUA879r6kktZd2SAvNv2c%2FucbMRxykfdT%2Fs8LfZwKokf5nWoRn%2BSkOxZlOYZFapTnnshKsIgR1vfBG3rNGHeRoTgnZ0D0TLCvLNVcBJyL6JqPRgmyubpRfYqktCijD7HtPmLpWzpJWuMIOH7LwGOqUBVKa2J2NHNGLiGejhvos0cqWmqGfOawNYVq8A3%2Bx9p9URS77upzxlWIqKWWVJkGwXdHnMm0S615A2HXBu5HPeEsyWqo1Eug7LG4VZmR6zINIaBSafLY%2FmLBxeYAi9FOf4zbM88yef6B6u1WoX7Dl4P7TfXOdxQJl%2BE%2FHIHI96DjqrhpxVHLFDvVbc1cPG5whIpBwHGmFS06ex8QXf0JMnY0ekAvjG&X-Amz-Signature=156833fb9226f42e5f8da89d5375b9b4796ef340fe91a101eb8257c75790ee6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W4PXBVH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYAH7YMr60F2TRSELBHSW3pCDK6LRYWLzPW%2B7Mb5poLAiAKWVO7viVP4HcAY1eiHj%2BWBTD%2BJST0SjAgMDX2CJ9nmyqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr3JJxkFSrC12wqpxKtwDb28ZGShHfuY3Ni7rPWfKwMoHNwwPe6OACqbkLrex8QWGv8kFXsTdIRkasESxH5FMSaU8sdF7A5DMyZtvxR8%2B9inCO5j7%2FURMzvGftENgNE9egQshVXU5dBpfuwr5kE34RbuBgc%2Fyh2pWLxXz26dICOMbDw%2Bz77mIBAB9caTn0vo3OusKg7awTjwuGRuIlQB32ClFKG4T6iNgH4WVaE5scZvvFmMkcY5OQhW4Wgmfor3YL9e30%2FtpmyWnEj3yQ%2B%2FTweLv%2F%2B2qfS6iYq0ZD%2BrR962LFhPGrbCtRk7vSxoB2tdLhqSQB%2BUNczm2xL8%2BvLfGT4AmhQM3lGLhzicDMhsuQltZHGNIjvGu2CpIpxHNFUxmr6n06Zs%2Fte565hgmGbIllqv34rnQ9mHtqNxNndByUItnYGhp01WlvdwSueMg%2BMaZjQGXBCKulArOrr6GeUQuhI5%2FEoDq64AZSt08NI6RZBUA2OwG%2FMszDcs5VOO6C2i%2FqOauLSNkNcHTiNdOdddpxxUUcdm%2F8umT%2BsmKcaWWrV8wBA7T%2FVYAQJSkMswjDs7pcuzdkJBbop7%2FOP12qsX8qBJwJOHzND3HzXitQWCuCEbOtx67SNYcqkBnYCuGdZ0z3506%2FvoybJsIXF4w6obsvAY6pgGLDJDzgnJ31lMZHRhcGKT7FZ%2FNwoXdS7fftHQZupObNkQ7DetBvMyNsGHWTTg8%2BPOrbe82kCp4t4zAmG1plWyycNfm7U0CDTUF8QJPD0iuL5gBovCVcTIXiidMBhu6dqJX96Coiz5FnA48nRtx9Gkqb%2F3zvPOOA4TnE3tKSuxCMDaB5iHFOnoiUu01Z6pR8GhnIyF4LvL1%2Fhb0KBgRZJSBeGOgTlMO&X-Amz-Signature=75367811cdcb961940eb278f0af5402b49473031d2410939cb02d6eda2d35a40&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W4PXBVH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYAH7YMr60F2TRSELBHSW3pCDK6LRYWLzPW%2B7Mb5poLAiAKWVO7viVP4HcAY1eiHj%2BWBTD%2BJST0SjAgMDX2CJ9nmyqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr3JJxkFSrC12wqpxKtwDb28ZGShHfuY3Ni7rPWfKwMoHNwwPe6OACqbkLrex8QWGv8kFXsTdIRkasESxH5FMSaU8sdF7A5DMyZtvxR8%2B9inCO5j7%2FURMzvGftENgNE9egQshVXU5dBpfuwr5kE34RbuBgc%2Fyh2pWLxXz26dICOMbDw%2Bz77mIBAB9caTn0vo3OusKg7awTjwuGRuIlQB32ClFKG4T6iNgH4WVaE5scZvvFmMkcY5OQhW4Wgmfor3YL9e30%2FtpmyWnEj3yQ%2B%2FTweLv%2F%2B2qfS6iYq0ZD%2BrR962LFhPGrbCtRk7vSxoB2tdLhqSQB%2BUNczm2xL8%2BvLfGT4AmhQM3lGLhzicDMhsuQltZHGNIjvGu2CpIpxHNFUxmr6n06Zs%2Fte565hgmGbIllqv34rnQ9mHtqNxNndByUItnYGhp01WlvdwSueMg%2BMaZjQGXBCKulArOrr6GeUQuhI5%2FEoDq64AZSt08NI6RZBUA2OwG%2FMszDcs5VOO6C2i%2FqOauLSNkNcHTiNdOdddpxxUUcdm%2F8umT%2BsmKcaWWrV8wBA7T%2FVYAQJSkMswjDs7pcuzdkJBbop7%2FOP12qsX8qBJwJOHzND3HzXitQWCuCEbOtx67SNYcqkBnYCuGdZ0z3506%2FvoybJsIXF4w6obsvAY6pgGLDJDzgnJ31lMZHRhcGKT7FZ%2FNwoXdS7fftHQZupObNkQ7DetBvMyNsGHWTTg8%2BPOrbe82kCp4t4zAmG1plWyycNfm7U0CDTUF8QJPD0iuL5gBovCVcTIXiidMBhu6dqJX96Coiz5FnA48nRtx9Gkqb%2F3zvPOOA4TnE3tKSuxCMDaB5iHFOnoiUu01Z6pR8GhnIyF4LvL1%2Fhb0KBgRZJSBeGOgTlMO&X-Amz-Signature=6d8e0d66468e4c8852f9868ad60bf52600ad4e35d38668a0316f212b12833a80&X-Amz-SignedHeaders=host&x-id=GetObject)

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
