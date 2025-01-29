

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QTODNSP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAc6JW6MQ5bVo9LiN5N1U5c6jFPaXg089fR4EwDUhRcgAiEAoZXJoXyineug8oBjNvuu%2BiEB%2Bhqba72C1%2F%2BvPWVEfzgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOCVnmXeJMC%2FP7jjircA3Wbn%2BScMcB6dTwthP2vPyESNsaNGN3phen1Bpex%2FW%2FxwxzhcV9QKBneGIIMyI4AFPxbwEBmWMS2%2B%2B%2BxBUkPINO%2BDvIrCl9n%2F2uTpF32%2FEWVfKUL7x2JmYlMHJFIXQ%2BPQ4Zb8IaGYNZSKpxcVG%2BbRwTooQBb%2FLNKoSsmmbX9wqDnlT%2FWr7%2FbAc1btxQ5kq0y4suVKqs2QiRtXDZctvsgBZ8469%2BkgvzhHdQ4aB1Cjws1HxKNdPSJWy06oFE4X4aU1SrkqKfIF%2B2rZjbRv%2BMAH8OzO42YNtspxOONpH5yclwQc46w%2FhGmIxK2pWVaDTxbCbUorjEX7bVyIJ4SViNRfXHkJJEjZDFzQJTRmfZoaBzwzQsQ5qvX9LueasgoKDbfEMOulbj1FtWUnPfxs609hwdYdRUotiYMfMa0nNTyTxlKERTxbuLbZodGS1jzv8%2BGf786Al9mLLp%2FgoxKMXkSOzUE9yMvwUEjM0WwbRvk%2Fiqd2JWu%2F79x9XxrF41T4GKeEjsrhqvyczawjiGdrb0SQKL3SOADwo9P6pbbd0jRZis8Xe8XwJ92pfq3YX%2BYNbWMwO3Nzsq%2B2VMg6NFPhA2pCIl4FV1D8yP0GPnR6Hxb8hMikQa%2FJMKJEjUA5%2FHaMML%2B57wGOqUBMG0zDyoKUWP%2B%2B60nmT3XaV0lUBXQzz5qoh%2FIvxvgJglIE0aTpYn4Kbs4wn4CMJLpZ0XqyRLm4jlyRnKgJBEM3Xm1Y5JSDEv55CCi%2FbgRqbIm6Z53ItfXh0i53M8FCCazzg0yKh0IXN60zTmyv1gxxfeR3i24vXxzb%2BT1Y26WyehreMRlR3Clv%2FQjFy0YzJfsvCc4wA6T9vQ511wR9qvrWjKgyZDR&X-Amz-Signature=60c2ddeccbe6428e827e739cb61088dda8aa89004ef70cfc9e1a2a02b4540344&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QTODNSP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAc6JW6MQ5bVo9LiN5N1U5c6jFPaXg089fR4EwDUhRcgAiEAoZXJoXyineug8oBjNvuu%2BiEB%2Bhqba72C1%2F%2BvPWVEfzgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOCVnmXeJMC%2FP7jjircA3Wbn%2BScMcB6dTwthP2vPyESNsaNGN3phen1Bpex%2FW%2FxwxzhcV9QKBneGIIMyI4AFPxbwEBmWMS2%2B%2B%2BxBUkPINO%2BDvIrCl9n%2F2uTpF32%2FEWVfKUL7x2JmYlMHJFIXQ%2BPQ4Zb8IaGYNZSKpxcVG%2BbRwTooQBb%2FLNKoSsmmbX9wqDnlT%2FWr7%2FbAc1btxQ5kq0y4suVKqs2QiRtXDZctvsgBZ8469%2BkgvzhHdQ4aB1Cjws1HxKNdPSJWy06oFE4X4aU1SrkqKfIF%2B2rZjbRv%2BMAH8OzO42YNtspxOONpH5yclwQc46w%2FhGmIxK2pWVaDTxbCbUorjEX7bVyIJ4SViNRfXHkJJEjZDFzQJTRmfZoaBzwzQsQ5qvX9LueasgoKDbfEMOulbj1FtWUnPfxs609hwdYdRUotiYMfMa0nNTyTxlKERTxbuLbZodGS1jzv8%2BGf786Al9mLLp%2FgoxKMXkSOzUE9yMvwUEjM0WwbRvk%2Fiqd2JWu%2F79x9XxrF41T4GKeEjsrhqvyczawjiGdrb0SQKL3SOADwo9P6pbbd0jRZis8Xe8XwJ92pfq3YX%2BYNbWMwO3Nzsq%2B2VMg6NFPhA2pCIl4FV1D8yP0GPnR6Hxb8hMikQa%2FJMKJEjUA5%2FHaMML%2B57wGOqUBMG0zDyoKUWP%2B%2B60nmT3XaV0lUBXQzz5qoh%2FIvxvgJglIE0aTpYn4Kbs4wn4CMJLpZ0XqyRLm4jlyRnKgJBEM3Xm1Y5JSDEv55CCi%2FbgRqbIm6Z53ItfXh0i53M8FCCazzg0yKh0IXN60zTmyv1gxxfeR3i24vXxzb%2BT1Y26WyehreMRlR3Clv%2FQjFy0YzJfsvCc4wA6T9vQ511wR9qvrWjKgyZDR&X-Amz-Signature=c7abb41d6af52c9567252ee6b47813c84a91c0f0b719bcd277ce6eabc86d6d72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QTODNSP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAc6JW6MQ5bVo9LiN5N1U5c6jFPaXg089fR4EwDUhRcgAiEAoZXJoXyineug8oBjNvuu%2BiEB%2Bhqba72C1%2F%2BvPWVEfzgqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOCVnmXeJMC%2FP7jjircA3Wbn%2BScMcB6dTwthP2vPyESNsaNGN3phen1Bpex%2FW%2FxwxzhcV9QKBneGIIMyI4AFPxbwEBmWMS2%2B%2B%2BxBUkPINO%2BDvIrCl9n%2F2uTpF32%2FEWVfKUL7x2JmYlMHJFIXQ%2BPQ4Zb8IaGYNZSKpxcVG%2BbRwTooQBb%2FLNKoSsmmbX9wqDnlT%2FWr7%2FbAc1btxQ5kq0y4suVKqs2QiRtXDZctvsgBZ8469%2BkgvzhHdQ4aB1Cjws1HxKNdPSJWy06oFE4X4aU1SrkqKfIF%2B2rZjbRv%2BMAH8OzO42YNtspxOONpH5yclwQc46w%2FhGmIxK2pWVaDTxbCbUorjEX7bVyIJ4SViNRfXHkJJEjZDFzQJTRmfZoaBzwzQsQ5qvX9LueasgoKDbfEMOulbj1FtWUnPfxs609hwdYdRUotiYMfMa0nNTyTxlKERTxbuLbZodGS1jzv8%2BGf786Al9mLLp%2FgoxKMXkSOzUE9yMvwUEjM0WwbRvk%2Fiqd2JWu%2F79x9XxrF41T4GKeEjsrhqvyczawjiGdrb0SQKL3SOADwo9P6pbbd0jRZis8Xe8XwJ92pfq3YX%2BYNbWMwO3Nzsq%2B2VMg6NFPhA2pCIl4FV1D8yP0GPnR6Hxb8hMikQa%2FJMKJEjUA5%2FHaMML%2B57wGOqUBMG0zDyoKUWP%2B%2B60nmT3XaV0lUBXQzz5qoh%2FIvxvgJglIE0aTpYn4Kbs4wn4CMJLpZ0XqyRLm4jlyRnKgJBEM3Xm1Y5JSDEv55CCi%2FbgRqbIm6Z53ItfXh0i53M8FCCazzg0yKh0IXN60zTmyv1gxxfeR3i24vXxzb%2BT1Y26WyehreMRlR3Clv%2FQjFy0YzJfsvCc4wA6T9vQ511wR9qvrWjKgyZDR&X-Amz-Signature=eeaed4aa384117072f8abef3420eddcf5534ce640d019c707aa618b09313c2f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJMPJ5GE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9qdkhaZYPen1H5Igfb6pkDkH89UKYuuOMsXnBNBrJCwIhAL7YecOpDvkaEk2OyWYP%2Fo5VGbRq11uMbtDbRU15IqGKKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymijuJcHT%2BYuk7vF8q3AO9IvPJWlXsqfNdiBNiIRSZeqGz3iL53WD6UxBlSGvnVTj6K0YiKNIsyd9g%2FzSayIUXdc9potAf1BfeYub0RgNWeCNIOb6UiDQkG%2BSn2hXydBe9g1q%2BlvFzs3uow8Lnu4Dzo3syyZqwU%2FPDgdAGv25a%2By4Sg5uzLKubm5IoIVUMJZIKxb6jSWqt%2FKaCrN1d6SqMwSOit8hK2mh%2FjPauQ2eR17RQjrUfmbdd7TnahfNNn%2B1chivt8UDpasxpsMb4rPz4KwrzrelEEG2QyNVi0EyZcGZbjA92xm0UlFNIg%2FNKifBkkFdoGY3Z%2BOram8AJRZh7FDXnWAoQJrIk5GUcyN8gOYrzraIMHF9fImQKC8CPU2mrLGyToDIkMKh98GrFNIkHHv38ksM%2BggLVIT127DrAL3ot78YMSrPrbFKLaKjRz5wQ3HPteHW7aXpBgREwUyAxw2zDqqymqmPoDGAfz7wilo3EBZzasHmnSA53D6%2FoKJ%2BW41L76YjggYYoGaCTG4tN3DM6bhgH3LeFJ05fXwsH08ffv5l26%2FaElLfjuctsItHneItI0LXHbfZ%2FjKGNSpd57h6FnydtxuKWXY2t%2FAl7q60%2BKp%2FlBCvuIkiCibi2vuv2JUXKnhXsNrdMyDDB%2Fue8BjqkARJ5dcnlwVSqs2ve8SrsfbQW5d2swUwHQW41aoYDmirDMYWRXEGTeKthuZKT8f3DmBA3IS2sCY%2BijpoPkVM1cZ8C7CdebhUYfQNZ7EU4ZoTvfYLB5L8cgcEsowSRI5nitzr1qQ3gMuEzQ%2BESLQ%2BEuVeMqY60eosHX14u0aA7WNRBlMnUkzLS1h7JUwNfkizpZeo6wDNovggR1m%2Fpv2SoiAtyrjIQ&X-Amz-Signature=64bc760db706778bd64a2068ddff95b043406170c7b00d07ce245369a72690bc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJMPJ5GE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9qdkhaZYPen1H5Igfb6pkDkH89UKYuuOMsXnBNBrJCwIhAL7YecOpDvkaEk2OyWYP%2Fo5VGbRq11uMbtDbRU15IqGKKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymijuJcHT%2BYuk7vF8q3AO9IvPJWlXsqfNdiBNiIRSZeqGz3iL53WD6UxBlSGvnVTj6K0YiKNIsyd9g%2FzSayIUXdc9potAf1BfeYub0RgNWeCNIOb6UiDQkG%2BSn2hXydBe9g1q%2BlvFzs3uow8Lnu4Dzo3syyZqwU%2FPDgdAGv25a%2By4Sg5uzLKubm5IoIVUMJZIKxb6jSWqt%2FKaCrN1d6SqMwSOit8hK2mh%2FjPauQ2eR17RQjrUfmbdd7TnahfNNn%2B1chivt8UDpasxpsMb4rPz4KwrzrelEEG2QyNVi0EyZcGZbjA92xm0UlFNIg%2FNKifBkkFdoGY3Z%2BOram8AJRZh7FDXnWAoQJrIk5GUcyN8gOYrzraIMHF9fImQKC8CPU2mrLGyToDIkMKh98GrFNIkHHv38ksM%2BggLVIT127DrAL3ot78YMSrPrbFKLaKjRz5wQ3HPteHW7aXpBgREwUyAxw2zDqqymqmPoDGAfz7wilo3EBZzasHmnSA53D6%2FoKJ%2BW41L76YjggYYoGaCTG4tN3DM6bhgH3LeFJ05fXwsH08ffv5l26%2FaElLfjuctsItHneItI0LXHbfZ%2FjKGNSpd57h6FnydtxuKWXY2t%2FAl7q60%2BKp%2FlBCvuIkiCibi2vuv2JUXKnhXsNrdMyDDB%2Fue8BjqkARJ5dcnlwVSqs2ve8SrsfbQW5d2swUwHQW41aoYDmirDMYWRXEGTeKthuZKT8f3DmBA3IS2sCY%2BijpoPkVM1cZ8C7CdebhUYfQNZ7EU4ZoTvfYLB5L8cgcEsowSRI5nitzr1qQ3gMuEzQ%2BESLQ%2BEuVeMqY60eosHX14u0aA7WNRBlMnUkzLS1h7JUwNfkizpZeo6wDNovggR1m%2Fpv2SoiAtyrjIQ&X-Amz-Signature=3ceaf2d2f5ad987dad3db04d9c62c8c817e17f4a868627fe06ad6cc4928a8b24&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJMPJ5GE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9qdkhaZYPen1H5Igfb6pkDkH89UKYuuOMsXnBNBrJCwIhAL7YecOpDvkaEk2OyWYP%2Fo5VGbRq11uMbtDbRU15IqGKKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymijuJcHT%2BYuk7vF8q3AO9IvPJWlXsqfNdiBNiIRSZeqGz3iL53WD6UxBlSGvnVTj6K0YiKNIsyd9g%2FzSayIUXdc9potAf1BfeYub0RgNWeCNIOb6UiDQkG%2BSn2hXydBe9g1q%2BlvFzs3uow8Lnu4Dzo3syyZqwU%2FPDgdAGv25a%2By4Sg5uzLKubm5IoIVUMJZIKxb6jSWqt%2FKaCrN1d6SqMwSOit8hK2mh%2FjPauQ2eR17RQjrUfmbdd7TnahfNNn%2B1chivt8UDpasxpsMb4rPz4KwrzrelEEG2QyNVi0EyZcGZbjA92xm0UlFNIg%2FNKifBkkFdoGY3Z%2BOram8AJRZh7FDXnWAoQJrIk5GUcyN8gOYrzraIMHF9fImQKC8CPU2mrLGyToDIkMKh98GrFNIkHHv38ksM%2BggLVIT127DrAL3ot78YMSrPrbFKLaKjRz5wQ3HPteHW7aXpBgREwUyAxw2zDqqymqmPoDGAfz7wilo3EBZzasHmnSA53D6%2FoKJ%2BW41L76YjggYYoGaCTG4tN3DM6bhgH3LeFJ05fXwsH08ffv5l26%2FaElLfjuctsItHneItI0LXHbfZ%2FjKGNSpd57h6FnydtxuKWXY2t%2FAl7q60%2BKp%2FlBCvuIkiCibi2vuv2JUXKnhXsNrdMyDDB%2Fue8BjqkARJ5dcnlwVSqs2ve8SrsfbQW5d2swUwHQW41aoYDmirDMYWRXEGTeKthuZKT8f3DmBA3IS2sCY%2BijpoPkVM1cZ8C7CdebhUYfQNZ7EU4ZoTvfYLB5L8cgcEsowSRI5nitzr1qQ3gMuEzQ%2BESLQ%2BEuVeMqY60eosHX14u0aA7WNRBlMnUkzLS1h7JUwNfkizpZeo6wDNovggR1m%2Fpv2SoiAtyrjIQ&X-Amz-Signature=d7b49ca06259214bd13065d8e9a53f50cdbea7374b6888890e824a180df82f73&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJMPJ5GE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9qdkhaZYPen1H5Igfb6pkDkH89UKYuuOMsXnBNBrJCwIhAL7YecOpDvkaEk2OyWYP%2Fo5VGbRq11uMbtDbRU15IqGKKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymijuJcHT%2BYuk7vF8q3AO9IvPJWlXsqfNdiBNiIRSZeqGz3iL53WD6UxBlSGvnVTj6K0YiKNIsyd9g%2FzSayIUXdc9potAf1BfeYub0RgNWeCNIOb6UiDQkG%2BSn2hXydBe9g1q%2BlvFzs3uow8Lnu4Dzo3syyZqwU%2FPDgdAGv25a%2By4Sg5uzLKubm5IoIVUMJZIKxb6jSWqt%2FKaCrN1d6SqMwSOit8hK2mh%2FjPauQ2eR17RQjrUfmbdd7TnahfNNn%2B1chivt8UDpasxpsMb4rPz4KwrzrelEEG2QyNVi0EyZcGZbjA92xm0UlFNIg%2FNKifBkkFdoGY3Z%2BOram8AJRZh7FDXnWAoQJrIk5GUcyN8gOYrzraIMHF9fImQKC8CPU2mrLGyToDIkMKh98GrFNIkHHv38ksM%2BggLVIT127DrAL3ot78YMSrPrbFKLaKjRz5wQ3HPteHW7aXpBgREwUyAxw2zDqqymqmPoDGAfz7wilo3EBZzasHmnSA53D6%2FoKJ%2BW41L76YjggYYoGaCTG4tN3DM6bhgH3LeFJ05fXwsH08ffv5l26%2FaElLfjuctsItHneItI0LXHbfZ%2FjKGNSpd57h6FnydtxuKWXY2t%2FAl7q60%2BKp%2FlBCvuIkiCibi2vuv2JUXKnhXsNrdMyDDB%2Fue8BjqkARJ5dcnlwVSqs2ve8SrsfbQW5d2swUwHQW41aoYDmirDMYWRXEGTeKthuZKT8f3DmBA3IS2sCY%2BijpoPkVM1cZ8C7CdebhUYfQNZ7EU4ZoTvfYLB5L8cgcEsowSRI5nitzr1qQ3gMuEzQ%2BESLQ%2BEuVeMqY60eosHX14u0aA7WNRBlMnUkzLS1h7JUwNfkizpZeo6wDNovggR1m%2Fpv2SoiAtyrjIQ&X-Amz-Signature=adefb2ed24c03657c1c1d9450bd6f9af1a7a2a0be3d2014315153e6b61ead46b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJMPJ5GE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9qdkhaZYPen1H5Igfb6pkDkH89UKYuuOMsXnBNBrJCwIhAL7YecOpDvkaEk2OyWYP%2Fo5VGbRq11uMbtDbRU15IqGKKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymijuJcHT%2BYuk7vF8q3AO9IvPJWlXsqfNdiBNiIRSZeqGz3iL53WD6UxBlSGvnVTj6K0YiKNIsyd9g%2FzSayIUXdc9potAf1BfeYub0RgNWeCNIOb6UiDQkG%2BSn2hXydBe9g1q%2BlvFzs3uow8Lnu4Dzo3syyZqwU%2FPDgdAGv25a%2By4Sg5uzLKubm5IoIVUMJZIKxb6jSWqt%2FKaCrN1d6SqMwSOit8hK2mh%2FjPauQ2eR17RQjrUfmbdd7TnahfNNn%2B1chivt8UDpasxpsMb4rPz4KwrzrelEEG2QyNVi0EyZcGZbjA92xm0UlFNIg%2FNKifBkkFdoGY3Z%2BOram8AJRZh7FDXnWAoQJrIk5GUcyN8gOYrzraIMHF9fImQKC8CPU2mrLGyToDIkMKh98GrFNIkHHv38ksM%2BggLVIT127DrAL3ot78YMSrPrbFKLaKjRz5wQ3HPteHW7aXpBgREwUyAxw2zDqqymqmPoDGAfz7wilo3EBZzasHmnSA53D6%2FoKJ%2BW41L76YjggYYoGaCTG4tN3DM6bhgH3LeFJ05fXwsH08ffv5l26%2FaElLfjuctsItHneItI0LXHbfZ%2FjKGNSpd57h6FnydtxuKWXY2t%2FAl7q60%2BKp%2FlBCvuIkiCibi2vuv2JUXKnhXsNrdMyDDB%2Fue8BjqkARJ5dcnlwVSqs2ve8SrsfbQW5d2swUwHQW41aoYDmirDMYWRXEGTeKthuZKT8f3DmBA3IS2sCY%2BijpoPkVM1cZ8C7CdebhUYfQNZ7EU4ZoTvfYLB5L8cgcEsowSRI5nitzr1qQ3gMuEzQ%2BESLQ%2BEuVeMqY60eosHX14u0aA7WNRBlMnUkzLS1h7JUwNfkizpZeo6wDNovggR1m%2Fpv2SoiAtyrjIQ&X-Amz-Signature=378b892b8d5ea83d3d2b25554dbb3f99ea1bbcd36601775b3cadeb1248c94256&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJMPJ5GE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9qdkhaZYPen1H5Igfb6pkDkH89UKYuuOMsXnBNBrJCwIhAL7YecOpDvkaEk2OyWYP%2Fo5VGbRq11uMbtDbRU15IqGKKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymijuJcHT%2BYuk7vF8q3AO9IvPJWlXsqfNdiBNiIRSZeqGz3iL53WD6UxBlSGvnVTj6K0YiKNIsyd9g%2FzSayIUXdc9potAf1BfeYub0RgNWeCNIOb6UiDQkG%2BSn2hXydBe9g1q%2BlvFzs3uow8Lnu4Dzo3syyZqwU%2FPDgdAGv25a%2By4Sg5uzLKubm5IoIVUMJZIKxb6jSWqt%2FKaCrN1d6SqMwSOit8hK2mh%2FjPauQ2eR17RQjrUfmbdd7TnahfNNn%2B1chivt8UDpasxpsMb4rPz4KwrzrelEEG2QyNVi0EyZcGZbjA92xm0UlFNIg%2FNKifBkkFdoGY3Z%2BOram8AJRZh7FDXnWAoQJrIk5GUcyN8gOYrzraIMHF9fImQKC8CPU2mrLGyToDIkMKh98GrFNIkHHv38ksM%2BggLVIT127DrAL3ot78YMSrPrbFKLaKjRz5wQ3HPteHW7aXpBgREwUyAxw2zDqqymqmPoDGAfz7wilo3EBZzasHmnSA53D6%2FoKJ%2BW41L76YjggYYoGaCTG4tN3DM6bhgH3LeFJ05fXwsH08ffv5l26%2FaElLfjuctsItHneItI0LXHbfZ%2FjKGNSpd57h6FnydtxuKWXY2t%2FAl7q60%2BKp%2FlBCvuIkiCibi2vuv2JUXKnhXsNrdMyDDB%2Fue8BjqkARJ5dcnlwVSqs2ve8SrsfbQW5d2swUwHQW41aoYDmirDMYWRXEGTeKthuZKT8f3DmBA3IS2sCY%2BijpoPkVM1cZ8C7CdebhUYfQNZ7EU4ZoTvfYLB5L8cgcEsowSRI5nitzr1qQ3gMuEzQ%2BESLQ%2BEuVeMqY60eosHX14u0aA7WNRBlMnUkzLS1h7JUwNfkizpZeo6wDNovggR1m%2Fpv2SoiAtyrjIQ&X-Amz-Signature=e1a23732a5cee4f4c0248bdd21ed84d9a174cc18a970e602f9af875af6b905d3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRL6DHFG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHINYbAVleTmcHRbSq2LkoK7CaAbM1DUfyNRbvrhnxODAiA8q%2BhXbvnKLBTsARryIGkq3P%2FSaAcl7W5kYfsL4u3v9CqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjjKmwnaRkUnCtN8EKtwD8KUZGncoGExJI6uniKYLu9XSfsnGo05%2FCg5bEVoc8tJrcX6W0syZSsDjGQrJaOoCMMKxgzWGqIP9yXwUYd%2BM7AbkKk7lRyR%2BXLl2X%2B7iVq6JIFEY90qj541iuAgrNM%2FP0bSyVyRebnrqOCQiY67QTF8%2BOhU7QhuQnA3fP3aclIOpNWf33B1AlUcMg5VKBqjAKrBuN9u7zGc4BOoO%2BcdAUx2R32mGMSB27Ep1CMt6Jcy5KrE7NrHGyaS021%2F%2B6Ng25H4h%2FTTlaRUfotgsXknOm9snKnUSJRuCGA9oDHI3vMlhBISTrmli8wsVBsiLvZjC1cjjq4ge%2Fk9IvTi2F%2FD%2BkBvGmtJ5%2ByXsdcOwIf1tj%2FuaZeLTjxorGoqX%2F%2FbaNgIvoCmehkddN7R20Hu868etgW6QaNALPMVYpodan%2BttubySo9knI1Twaj7lCypTfUCjW%2BTPJmQ8mb8b3FTiIrPXZryKdBNAcbPXcsCAZkwMKt%2FAKB%2FMu1iSKyLTg3Ta7WTSbfGoi6CsW5TtTvZd%2B0D0QrcPCnnlTNum4TximczPkwI0J0IyNhErld8Xon6OXxzsD80kn%2F%2B%2FDqeXYRVZFyJeaOkSRwhKZdNxNljliqNR%2Fm0XIH%2FmgrLuGsVoMm4wqOPnvAY6pgE6P7L9QYog8%2FoPXxl3c60EK1SeFxIjvpq0dZPbhF1xjJGFyaZSWAM4QHbTClnw9PzYTSec%2BpSwnkBXvQVERCktwi6a8KhxdUeXYd%2FMLASXbQ%2B3oAGR3qUqe2Z8%2FFpCVLZp%2F7nGHs4xQ%2B8%2ByG0MQE6IH5EklgAhT%2FWU0V2GRXtxXY1ps1loKMu7nwmobBalraAzVYVbOSfkRdy5sexaEdqmE8Q9dV9y&X-Amz-Signature=940e1be6842bba9385e05b3954665c8a9da4bf453b10f3e4848584e1cd4cedb4&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PFOO5S6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB0GgEUcrmHPZwCrGkA3xwTEBrOygn5v%2BGo2t9T8gu05AiA%2BSxIv28q3Qbrdrj3NOrl4bZHIFHa7do5HdcRGRrAewyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMU7KRKrBKw049RhORKtwDBIoiw76aZg7s18JZqT5rJ9NKQ5MdEOL5EpawRnT1dFxkYtUJNXyweQyqAc7goKZQy2aTr%2F3uJgrKhYeKoJFdRyDK79Msf35LOJZXKi9w%2FFPcLboFlDkyTTChlyce6agEOJOS9PUeiO2xjiCdoMeldw5crYGYiNZUjUJBqiOu1b252okkeHsfI1LcVqpeCv8QsWWDygPup%2FpWqtBXXyOGVaK6jwHL6a%2BaqFf4zg8pxr45SYq4bUzujB%2Fgg5t5No1NegpIWKkLMxo%2BIUug%2FE2%2Fi%2FrIuPZf8EDVVvAO4o07KGINSENaaBsqx2k8UR80Ki%2BULMLUn%2F1QLXXN2lbOG5kj1m%2Fv0WSZC2FG0rnZYusAqUL24IoydWErKKAww1GweumXa5VDf2s8%2BlXClYeqCtskvaZ%2BxcYzRlfsLgOHg7ygY6uCLcKt4wZUbkNQmDG7wyOdRisHcRZCJ6JUol9XOx4QF%2F5zcXmrR3AVDPPsyQv76Xrzj2Iaw%2FYuSNa8Vb9BP8BRLT7i4GwaEN3EEJoLRAfT6bJEFci8RJBuU%2BJENTYZne%2BYjTLz%2Bvk%2F%2FXE2gjCT%2BXjqdxj0jbfJjDscGM%2F6UGXZHHufmr3Jtvt6sCpmQL9ydS%2B80rfhjwcbTD4KYh4wvOPnvAY6pgH11jx9DkGp4RxUi2VIpba4G7%2Fp4gmTChsCENK1sOLXKXw7XWCeTw%2BLFO4IYTPeFUvu%2BvqvGikdRihiWC74G7Ttw%2FNXRgKkweOVCSoMospJGhAVho%2B0MEQpSuRXuSQCHlOfI5XgSdBNcwSC58Bjl5aFW5iUPkKx54rccgqdnI4ooY2lLvaBefuKSDymdcdmiFxpXEsy3%2FXbF%2BSayM9hwQopP1mxmPfk&X-Amz-Signature=6b36de9b0b03fa83ad74a36a2b30e1c93c35f32cb458b22887a7f5fe58b2014d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJMPJ5GE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9qdkhaZYPen1H5Igfb6pkDkH89UKYuuOMsXnBNBrJCwIhAL7YecOpDvkaEk2OyWYP%2Fo5VGbRq11uMbtDbRU15IqGKKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymijuJcHT%2BYuk7vF8q3AO9IvPJWlXsqfNdiBNiIRSZeqGz3iL53WD6UxBlSGvnVTj6K0YiKNIsyd9g%2FzSayIUXdc9potAf1BfeYub0RgNWeCNIOb6UiDQkG%2BSn2hXydBe9g1q%2BlvFzs3uow8Lnu4Dzo3syyZqwU%2FPDgdAGv25a%2By4Sg5uzLKubm5IoIVUMJZIKxb6jSWqt%2FKaCrN1d6SqMwSOit8hK2mh%2FjPauQ2eR17RQjrUfmbdd7TnahfNNn%2B1chivt8UDpasxpsMb4rPz4KwrzrelEEG2QyNVi0EyZcGZbjA92xm0UlFNIg%2FNKifBkkFdoGY3Z%2BOram8AJRZh7FDXnWAoQJrIk5GUcyN8gOYrzraIMHF9fImQKC8CPU2mrLGyToDIkMKh98GrFNIkHHv38ksM%2BggLVIT127DrAL3ot78YMSrPrbFKLaKjRz5wQ3HPteHW7aXpBgREwUyAxw2zDqqymqmPoDGAfz7wilo3EBZzasHmnSA53D6%2FoKJ%2BW41L76YjggYYoGaCTG4tN3DM6bhgH3LeFJ05fXwsH08ffv5l26%2FaElLfjuctsItHneItI0LXHbfZ%2FjKGNSpd57h6FnydtxuKWXY2t%2FAl7q60%2BKp%2FlBCvuIkiCibi2vuv2JUXKnhXsNrdMyDDB%2Fue8BjqkARJ5dcnlwVSqs2ve8SrsfbQW5d2swUwHQW41aoYDmirDMYWRXEGTeKthuZKT8f3DmBA3IS2sCY%2BijpoPkVM1cZ8C7CdebhUYfQNZ7EU4ZoTvfYLB5L8cgcEsowSRI5nitzr1qQ3gMuEzQ%2BESLQ%2BEuVeMqY60eosHX14u0aA7WNRBlMnUkzLS1h7JUwNfkizpZeo6wDNovggR1m%2Fpv2SoiAtyrjIQ&X-Amz-Signature=195c47a72ff7b1d92d42b7f30eb292d23b2abfddada2127b21099c0d70a1cb02&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJMPJ5GE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9qdkhaZYPen1H5Igfb6pkDkH89UKYuuOMsXnBNBrJCwIhAL7YecOpDvkaEk2OyWYP%2Fo5VGbRq11uMbtDbRU15IqGKKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymijuJcHT%2BYuk7vF8q3AO9IvPJWlXsqfNdiBNiIRSZeqGz3iL53WD6UxBlSGvnVTj6K0YiKNIsyd9g%2FzSayIUXdc9potAf1BfeYub0RgNWeCNIOb6UiDQkG%2BSn2hXydBe9g1q%2BlvFzs3uow8Lnu4Dzo3syyZqwU%2FPDgdAGv25a%2By4Sg5uzLKubm5IoIVUMJZIKxb6jSWqt%2FKaCrN1d6SqMwSOit8hK2mh%2FjPauQ2eR17RQjrUfmbdd7TnahfNNn%2B1chivt8UDpasxpsMb4rPz4KwrzrelEEG2QyNVi0EyZcGZbjA92xm0UlFNIg%2FNKifBkkFdoGY3Z%2BOram8AJRZh7FDXnWAoQJrIk5GUcyN8gOYrzraIMHF9fImQKC8CPU2mrLGyToDIkMKh98GrFNIkHHv38ksM%2BggLVIT127DrAL3ot78YMSrPrbFKLaKjRz5wQ3HPteHW7aXpBgREwUyAxw2zDqqymqmPoDGAfz7wilo3EBZzasHmnSA53D6%2FoKJ%2BW41L76YjggYYoGaCTG4tN3DM6bhgH3LeFJ05fXwsH08ffv5l26%2FaElLfjuctsItHneItI0LXHbfZ%2FjKGNSpd57h6FnydtxuKWXY2t%2FAl7q60%2BKp%2FlBCvuIkiCibi2vuv2JUXKnhXsNrdMyDDB%2Fue8BjqkARJ5dcnlwVSqs2ve8SrsfbQW5d2swUwHQW41aoYDmirDMYWRXEGTeKthuZKT8f3DmBA3IS2sCY%2BijpoPkVM1cZ8C7CdebhUYfQNZ7EU4ZoTvfYLB5L8cgcEsowSRI5nitzr1qQ3gMuEzQ%2BESLQ%2BEuVeMqY60eosHX14u0aA7WNRBlMnUkzLS1h7JUwNfkizpZeo6wDNovggR1m%2Fpv2SoiAtyrjIQ&X-Amz-Signature=0ffc483a7d8187c2b703134a863c014e5e683e46cfae42d993d1e2a1f1f17112&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJMPJ5GE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9qdkhaZYPen1H5Igfb6pkDkH89UKYuuOMsXnBNBrJCwIhAL7YecOpDvkaEk2OyWYP%2Fo5VGbRq11uMbtDbRU15IqGKKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymijuJcHT%2BYuk7vF8q3AO9IvPJWlXsqfNdiBNiIRSZeqGz3iL53WD6UxBlSGvnVTj6K0YiKNIsyd9g%2FzSayIUXdc9potAf1BfeYub0RgNWeCNIOb6UiDQkG%2BSn2hXydBe9g1q%2BlvFzs3uow8Lnu4Dzo3syyZqwU%2FPDgdAGv25a%2By4Sg5uzLKubm5IoIVUMJZIKxb6jSWqt%2FKaCrN1d6SqMwSOit8hK2mh%2FjPauQ2eR17RQjrUfmbdd7TnahfNNn%2B1chivt8UDpasxpsMb4rPz4KwrzrelEEG2QyNVi0EyZcGZbjA92xm0UlFNIg%2FNKifBkkFdoGY3Z%2BOram8AJRZh7FDXnWAoQJrIk5GUcyN8gOYrzraIMHF9fImQKC8CPU2mrLGyToDIkMKh98GrFNIkHHv38ksM%2BggLVIT127DrAL3ot78YMSrPrbFKLaKjRz5wQ3HPteHW7aXpBgREwUyAxw2zDqqymqmPoDGAfz7wilo3EBZzasHmnSA53D6%2FoKJ%2BW41L76YjggYYoGaCTG4tN3DM6bhgH3LeFJ05fXwsH08ffv5l26%2FaElLfjuctsItHneItI0LXHbfZ%2FjKGNSpd57h6FnydtxuKWXY2t%2FAl7q60%2BKp%2FlBCvuIkiCibi2vuv2JUXKnhXsNrdMyDDB%2Fue8BjqkARJ5dcnlwVSqs2ve8SrsfbQW5d2swUwHQW41aoYDmirDMYWRXEGTeKthuZKT8f3DmBA3IS2sCY%2BijpoPkVM1cZ8C7CdebhUYfQNZ7EU4ZoTvfYLB5L8cgcEsowSRI5nitzr1qQ3gMuEzQ%2BESLQ%2BEuVeMqY60eosHX14u0aA7WNRBlMnUkzLS1h7JUwNfkizpZeo6wDNovggR1m%2Fpv2SoiAtyrjIQ&X-Amz-Signature=9b6be135f17e6e1a2fc32093f0679ece9612aa5f72062752c1be42838e592873&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NX5HGUK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2Fxb0Co0p5HqhbGkLPz2wdpRQt%2BYZWIl9rJ1%2FBsw9%2BTAiBqRhgU0hqmFhQGAtbKrVK6Q6gaslM6ox7XVX2bE%2BzyQyqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHs86ab3ZTq0%2B7MjBKtwDySEXd3wtiZRHFEMO%2FEDJUp7W21KELySdV%2BCJe5yTu0EUti5aHiqGwGwBTX04UeXJWNy6SJ%2ByjH%2BJmEhyrWeYo%2Fc2DTLl0zPoRwGkqD%2B4DK649puVvD78lZIdva5T%2FDYxa3j7OCqXX3cTKCRCkrR6H8pJ8osiEWvB483YFtyJCJiFj3dvQVXVyALwa2ZS%2F4Gk4yybVediZ1pu7fWHdC9Y93q%2F%2ByxwCpEVo9qT9E6jWHaVHEOuuqOSDnTiXSZQn5w2UQIkUduagZHmb1J0lq9qejJYrOlne%2F4oBLmn2FB%2FqYad5eVHr3xL3iSauzyrcgj7awydZROX8reRZ0G2QXbxHneMZ%2FtjLcWW60W30oEQKPmPREp9KmjqC1PCvdZ6cZIpNs6JXZpCFmSzk4vipzs0WfsOK4mbJrw2y45QoVbnbGmQVNYxhEMwJnMBWdMaS50b2F5B3af%2FbCIcr4x4dwzL7kOK%2BAl916OQUpmnbjREC%2FTaBjf1Fso4%2F79TomgfQCZ6xDOKIv7aJZj5va%2F3%2B9b5Ee09%2BuYuCRdhum3VGLKV6kKsRTwO231jmbwceakphIieMxrK7WEHYVhx6W76dGkQyS7icqKT0b33QaeLh%2F9OaFzlJUb44pRd2dPv8xYwy%2F7nvAY6pgETEyzMrr4bqm8zfiYl4iNWbqLwtrzJA0nD5IGZ0vtaZbqlf6DBUFxkbeDMQgBIMIcRjhdCvDqClEwo2snpM5zahUtq5%2BVh4kPqpN4kVgU%2B1r%2BmQW1dVYp5NvgyUN6QpRlfPWeipeuSwneQyN9zs74JrlivPVMlLCTzl%2FOUO2uMS50zFezLHet2h2L1dH%2F4zv45gC9Wl1HFQy5GpGejTVgDKzUj7cIC&X-Amz-Signature=6ea0003ffc44f987ad8658a90fac8e9ef9ffef0275a5dcffaf6b28eb0601f1de&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTP2YXHB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDbxIBYUZLUCU%2B6VLjHP7L%2BWGPl5chTOjizEcaYWRZwgIgLVOMJS6pvEuj072TVCF1FcV2vOZoy9TL4dvI6a6dNUAqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOvSh%2BJUVkCKKmzEjSrcA%2BEdGcqwWJM1kihiMmURnKyrLaVz8A1pFZy3yEGngHg5SF%2BCuCXJTEIv1uq7a3kpA6VwrqSRCZh7zR6nyC4t5KkYpciGMd5xEvJawJnzybRI0coav6HBHqFble0d4kROuEhuvHeoApzsyloiMGB5cy6USvkdRO30WUOdl26V4FFLZWIGm96dnFaOo1b6gbd%2BBXLLF64h%2FS9bJzeEFkc0sDYzw5kO1Iunts%2B0oybSCb4gTVCadAxfFqYSAcnJ39Rck316ElEYvKVnTPoyxIHV%2FPLu%2F1uKbY4gsr1wgqfnIWqEm7YH2CI2MTG0ln7mYMDywssE0u9X7nJQSazQ%2FeU4YOVwwCCfF1RtTx%2B9h41XtMlF4Yvc4f08o990jbyKlgDn8bemstTu%2BoH%2BRhMmxVi2B8s9o303jhmld14Ua91%2Fo8QE8fPD7bpnwMmwxG7W2IXjjuCyw6v9mVcUpyUggHF8vfZEKlgQdYH2ZfmACY9AMvhzwDFBaErXeZBqifisBadk7%2BZPUqxzW2hAMAPRfVCYZnR0BSN%2Fir5jNAc7xmQJyN8DiK6GNpOJrVDJLYfkNWHDGl4v5fo7xbkRSn9N2FTTLjV3n6ouMSiPn8Hutup6qMslmExLNUsmMbS6N%2BDWMKnj57wGOqUBZqpMusvj2prJYPSZGPxzSBSmx7wabA0FItfLQ1HAq0AMSm0ghW0oRhSzcovjg73m8Vm1Nbnv7JJwRdNC%2BpY07Wb%2FCgqf4105J5FQo0VYtgy4ZSvOy%2BsiE1oRI6o4kuYEyvhriRqnUB6SvUZ2HskmHSmbRMBwsdiaJqo%2BmCQlMpWOGwzlA2GjoMqrfrEeoLTEBPHdij2iCiZOKjdNBlMi9OLop4p9&X-Amz-Signature=8bd4ef0ab14a3a7a1d5a86e5b43bb3f53e84b3bfc2ed25357fe8e1f75677882c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NCQHCY3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBatPLXRe20s6RtjQxMKHdAdLdRouwg%2BMr1acOrriyiAIgQJLGDX5pxMGRTuIQ2P%2FF6knlWo561ArKrFO%2BVpK2j14qiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADf06M63dGARBbQSSrcA676RnpTBh%2BL2vUQPEesXtX5fR1xeGgX2xTC6zPW2hBP7HNZd8qq6Pj8LW8rc%2FXfeJMmj%2FJZheVRyDoyGtJv%2BThCx1ACHHG2WS0pG7Se0RnSLNuGsXs6CjBYaPjDBRDkWT%2FNv6o2417L1sxxnK0fiPapkGt87a%2BOyGp33wOUs1D5eURnTPXNBAKeHAfw9bp%2FYcCH9G86tNfAZ1TLoGrZKT03QyvA%2F%2F4HcmQao9yUgN9FlGXxTr%2F76jn3NOSOQSjkMbmWMQ4YN0zu8nvO4yQOY%2BVb3Ao9QzA9ekBNpIUy4F84S5UhIjBlsWKHtqHbrfP5J9vrJ70QN9hvHN8v%2FiK5fFmLVu6uINqm4SfGwwsL4l0JguOSg9WZKFZ4xu4nskRXKeybWkWU6%2FXk%2F%2Fk10v3V5MDq2rmyYg6c2%2BdOAta72QR9BEJ4GOP22BczDTt0NMaYNEzDm5V8smS5z6Hs1vN5xuU9f%2B1gujJc25n3OQcsrigYSskgXaOwAldrtjdkl%2BT8NO0KdVYsCw%2BUkDar1d9SSzQ13QmUXbZhGF0rDh115p9sWuQDYERg%2Buf0qHNDrzh7c4rTI4hvfYMYBySzkSoUwUPioauYobA596GNFPC2TWCrT9UqhUjR2ff7grknMM%2Fj57wGOqUBuvsjEYa7GHmVfXv5WyDdK5bkBcHkyTWMNq7FyoH%2FrXGXQiN0Rvsfa23T%2Bm%2F92obp9qzlfzi53AxIaw5Hy0qoe%2BwdlBiwckIlV2ipVgGYwjwqekoxQXXvLerggirD9EvyWcMkKzs0TBp9GcD6pMaV3pTSexPNG5%2FbQIyH%2FhXYK5U5Ge6EJfexP84imxckQWBE%2B5qxnTby9jxS%2BzUAq1fHByjFkUdY&X-Amz-Signature=464e7efd2195e942707e46816e5d1cb775adf8bec770167a7e5a7972f973f917&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJKDZ5T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWS6TP5rJOPsAgUF6BrHRj%2BtnyZAVUc%2B2Coy1xUoDHQAiAouRPcJ%2Bket5WxnuPrIf6yyu1OHWxFWGUnrlrqMYkdsiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTei6yIjKiU5R9NgnKtwDjPWttxfPahQCMhXsf7EKgJ5ZL77l6leUBHbfLAbYlw13eBtnDFIhzIYyLIFUdEGUmf27uLZvyJ%2FhKx8ZY7jVF35XHLeK4pYzW%2FzAIVtDf%2FoLR6ioqc2H5VVdhcEkeErU1odfKifopQVHXSXMl0BtNcyuL8YzWqdYQud3WiZvsE4NgoeIAGeo1%2BDOvHSeD6yfxMO8YYQDNvewWvWOwMyzv7%2FHpcf0%2BAizD2EooD%2BvKcgOiqHAdXA6RHHukS2mxmsYOFfJIem94NqRGjmd55Jt96jwD3MXkBM%2FNgjKyp6ZFkizVSlv1P0NLysh0cMhrHHPxdHlAswbSaCGEfnbxBB%2BjYmttps%2BV8juLrpG89wXE4HXTgei8AoSBfmZ4YR2oDKwT1dAMBq%2BYPMjOWnBt7jkRJ1w8f5e2tXMMj6feFqSpxh2tYNBg3SbRo8SgLNdO94HFTuG8KgBHRIIM%2BAufyqEtWyQ%2BtueRp%2BhQ%2FCdAFXLkHBiQ%2ByvCOlkntnDUKD3OfNKwIXBzrlh9k47LuuH0yu3fpRFkE37D5dBOyMiXryUYM5fICNRMVKKUz%2BXmfebvdWS8c5x1O9byZ3hOEUmBMDfIjWsmMuVXz5zg1wr6%2B1Tz%2Fxmo6zpbl6x4JdKxiowtP7nvAY6pgGM8YSS7I6YICEoyo1rMUejNwHVuPk4hAa9gf01NCrK6K29SvOh0uoXztSHd6%2F%2FmbPXQKcjBZDiS7KENV5hSKjCzqfEve7hfdkGBWTEd4Pdc4tE8jeT5AtBxk9IIfjAbucCTf7mhmlFCR85nzVv1E6FXLxsje9fhmpWgaCCnuNTAYyy24%2BG9AOVuw4Ksmi0KF%2BKytxagLQ3w%2BMuG84GwWPW7X%2FlbpcK&X-Amz-Signature=5ea00ae322454744225a442026b60aa58de1a69c4325b69e25190a01e81135b9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJKDZ5T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWS6TP5rJOPsAgUF6BrHRj%2BtnyZAVUc%2B2Coy1xUoDHQAiAouRPcJ%2Bket5WxnuPrIf6yyu1OHWxFWGUnrlrqMYkdsiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTei6yIjKiU5R9NgnKtwDjPWttxfPahQCMhXsf7EKgJ5ZL77l6leUBHbfLAbYlw13eBtnDFIhzIYyLIFUdEGUmf27uLZvyJ%2FhKx8ZY7jVF35XHLeK4pYzW%2FzAIVtDf%2FoLR6ioqc2H5VVdhcEkeErU1odfKifopQVHXSXMl0BtNcyuL8YzWqdYQud3WiZvsE4NgoeIAGeo1%2BDOvHSeD6yfxMO8YYQDNvewWvWOwMyzv7%2FHpcf0%2BAizD2EooD%2BvKcgOiqHAdXA6RHHukS2mxmsYOFfJIem94NqRGjmd55Jt96jwD3MXkBM%2FNgjKyp6ZFkizVSlv1P0NLysh0cMhrHHPxdHlAswbSaCGEfnbxBB%2BjYmttps%2BV8juLrpG89wXE4HXTgei8AoSBfmZ4YR2oDKwT1dAMBq%2BYPMjOWnBt7jkRJ1w8f5e2tXMMj6feFqSpxh2tYNBg3SbRo8SgLNdO94HFTuG8KgBHRIIM%2BAufyqEtWyQ%2BtueRp%2BhQ%2FCdAFXLkHBiQ%2ByvCOlkntnDUKD3OfNKwIXBzrlh9k47LuuH0yu3fpRFkE37D5dBOyMiXryUYM5fICNRMVKKUz%2BXmfebvdWS8c5x1O9byZ3hOEUmBMDfIjWsmMuVXz5zg1wr6%2B1Tz%2Fxmo6zpbl6x4JdKxiowtP7nvAY6pgGM8YSS7I6YICEoyo1rMUejNwHVuPk4hAa9gf01NCrK6K29SvOh0uoXztSHd6%2F%2FmbPXQKcjBZDiS7KENV5hSKjCzqfEve7hfdkGBWTEd4Pdc4tE8jeT5AtBxk9IIfjAbucCTf7mhmlFCR85nzVv1E6FXLxsje9fhmpWgaCCnuNTAYyy24%2BG9AOVuw4Ksmi0KF%2BKytxagLQ3w%2BMuG84GwWPW7X%2FlbpcK&X-Amz-Signature=7fb3c5d91d02c548b25deb78089ed432e2a90a14c9d06196f5ff1ce2dc178a97&X-Amz-SignedHeaders=host&x-id=GetObject)

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
