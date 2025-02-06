

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K7CISAR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCQjo2utqSmTrdTj8C%2B6PjBV11P6TmHiBUt%2FNEbsOODiAIhAPqyUin%2FFGW3W1v9Q6%2BRj0RjgJ9IBJnaiouOeW7YaV70Kv8DCGMQABoMNjM3NDIzMTgzODA1Igy7fGgU9TyTqUohZNgq3AO51TCKdUfFq90NXVjq%2FEJqwFZQYInphNH4jB4dD6dsUxx1Oe0UdcAxUe%2FYH8TthL8CwD9i%2Fjo5hHAo21brGI67Ex%2FgaJnKJeqwWLRM7pXBsM29vrBQsn6XuIXpIMKWkCnpePyycBytqiUc8PQDwKTHRlvdLmkzCE7NzqrvxzxJmuCWXUN1m6nQEWvvFYvz5yFG3Dm474l1gI6ed59G5me5tuiAKvqxnoiRiIrAmWhufdjYcM0tyr03BIadEwdRLN76qJKDKYomuFlqvvMRGxtF0TYaPygDgPfERtjecmdxHiMW5KJviQfu2ud4fCM43UhGzbfOxbkP4yZc5DXanGeWqw%2B0iHOSfG1bLML7fLAL7di9JS11cmwbp9ludriceLmX1H94kTwo1KEHmTUGolXf9utj5tmqNYowuXuuvqqYgaxXV2vq9cFXc6cXzSDD94yN3tSaT6Mfa8x6MUY8dTQv68Hp2et3%2FBDw6Q2Q3XzWr3KG7pL6xpn9csdPw9gCfBWWFy6WN3R1540RortEyTpIVgG0UNG63MwHC1p3T7iLcHSvndDzT5YgMWhSQcDeqowqpm%2B1NJa8YOrxW5XEU0zzE9RQ%2Fir3LhqNjnl8u9ttA9TTuHQ%2F5jYLp7RU8jDn%2B5O9BjqkAUiUenzXZ%2B9dJSLASJFnP4lYVB5Mw4qQG8i5gc0BfAk6arasZcmLyELcqbIq%2BAbTLOJntvKWYEwFVhSrZdXLzBKGaKLTSOaTNO7o0scfMdvFHPgYlqTS9ONkfm4JTYnOHpZ2qmkrrKMhBqNqgz4CaC5%2BKtP50XVgDF6d8gsMJ6%2BZ15cOaVCsgEEaA76I2LVXoty5nMJuce3ricvlmjX9PvOu%2By3Y&X-Amz-Signature=2062d708f651b136940c020d44a52b3b6029e7c1770c5525bd0bdd14db6dab44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K7CISAR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCQjo2utqSmTrdTj8C%2B6PjBV11P6TmHiBUt%2FNEbsOODiAIhAPqyUin%2FFGW3W1v9Q6%2BRj0RjgJ9IBJnaiouOeW7YaV70Kv8DCGMQABoMNjM3NDIzMTgzODA1Igy7fGgU9TyTqUohZNgq3AO51TCKdUfFq90NXVjq%2FEJqwFZQYInphNH4jB4dD6dsUxx1Oe0UdcAxUe%2FYH8TthL8CwD9i%2Fjo5hHAo21brGI67Ex%2FgaJnKJeqwWLRM7pXBsM29vrBQsn6XuIXpIMKWkCnpePyycBytqiUc8PQDwKTHRlvdLmkzCE7NzqrvxzxJmuCWXUN1m6nQEWvvFYvz5yFG3Dm474l1gI6ed59G5me5tuiAKvqxnoiRiIrAmWhufdjYcM0tyr03BIadEwdRLN76qJKDKYomuFlqvvMRGxtF0TYaPygDgPfERtjecmdxHiMW5KJviQfu2ud4fCM43UhGzbfOxbkP4yZc5DXanGeWqw%2B0iHOSfG1bLML7fLAL7di9JS11cmwbp9ludriceLmX1H94kTwo1KEHmTUGolXf9utj5tmqNYowuXuuvqqYgaxXV2vq9cFXc6cXzSDD94yN3tSaT6Mfa8x6MUY8dTQv68Hp2et3%2FBDw6Q2Q3XzWr3KG7pL6xpn9csdPw9gCfBWWFy6WN3R1540RortEyTpIVgG0UNG63MwHC1p3T7iLcHSvndDzT5YgMWhSQcDeqowqpm%2B1NJa8YOrxW5XEU0zzE9RQ%2Fir3LhqNjnl8u9ttA9TTuHQ%2F5jYLp7RU8jDn%2B5O9BjqkAUiUenzXZ%2B9dJSLASJFnP4lYVB5Mw4qQG8i5gc0BfAk6arasZcmLyELcqbIq%2BAbTLOJntvKWYEwFVhSrZdXLzBKGaKLTSOaTNO7o0scfMdvFHPgYlqTS9ONkfm4JTYnOHpZ2qmkrrKMhBqNqgz4CaC5%2BKtP50XVgDF6d8gsMJ6%2BZ15cOaVCsgEEaA76I2LVXoty5nMJuce3ricvlmjX9PvOu%2By3Y&X-Amz-Signature=ec584f9ae23d6498eb3f27ce764b911388cfcfcce393496dd7cb199cb06822d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K7CISAR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCQjo2utqSmTrdTj8C%2B6PjBV11P6TmHiBUt%2FNEbsOODiAIhAPqyUin%2FFGW3W1v9Q6%2BRj0RjgJ9IBJnaiouOeW7YaV70Kv8DCGMQABoMNjM3NDIzMTgzODA1Igy7fGgU9TyTqUohZNgq3AO51TCKdUfFq90NXVjq%2FEJqwFZQYInphNH4jB4dD6dsUxx1Oe0UdcAxUe%2FYH8TthL8CwD9i%2Fjo5hHAo21brGI67Ex%2FgaJnKJeqwWLRM7pXBsM29vrBQsn6XuIXpIMKWkCnpePyycBytqiUc8PQDwKTHRlvdLmkzCE7NzqrvxzxJmuCWXUN1m6nQEWvvFYvz5yFG3Dm474l1gI6ed59G5me5tuiAKvqxnoiRiIrAmWhufdjYcM0tyr03BIadEwdRLN76qJKDKYomuFlqvvMRGxtF0TYaPygDgPfERtjecmdxHiMW5KJviQfu2ud4fCM43UhGzbfOxbkP4yZc5DXanGeWqw%2B0iHOSfG1bLML7fLAL7di9JS11cmwbp9ludriceLmX1H94kTwo1KEHmTUGolXf9utj5tmqNYowuXuuvqqYgaxXV2vq9cFXc6cXzSDD94yN3tSaT6Mfa8x6MUY8dTQv68Hp2et3%2FBDw6Q2Q3XzWr3KG7pL6xpn9csdPw9gCfBWWFy6WN3R1540RortEyTpIVgG0UNG63MwHC1p3T7iLcHSvndDzT5YgMWhSQcDeqowqpm%2B1NJa8YOrxW5XEU0zzE9RQ%2Fir3LhqNjnl8u9ttA9TTuHQ%2F5jYLp7RU8jDn%2B5O9BjqkAUiUenzXZ%2B9dJSLASJFnP4lYVB5Mw4qQG8i5gc0BfAk6arasZcmLyELcqbIq%2BAbTLOJntvKWYEwFVhSrZdXLzBKGaKLTSOaTNO7o0scfMdvFHPgYlqTS9ONkfm4JTYnOHpZ2qmkrrKMhBqNqgz4CaC5%2BKtP50XVgDF6d8gsMJ6%2BZ15cOaVCsgEEaA76I2LVXoty5nMJuce3ricvlmjX9PvOu%2By3Y&X-Amz-Signature=af005c9e0baa26e508ee2719ed04cea76649f986172cbbdd1a0fcc7be1465eb0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644NEYAD6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDsltrdweF%2B7AvBE7Why4q%2BU1YEO0zR3dxTXWZ6wE%2FS1AiEA8PsRTbRnIqFhFQgqE%2F0EEKN1HWSF3qZcadVWLCepFvAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDD7v4XREONc9PV42RyrcA5GPSnzqU%2F0n%2FqX9Gen9LdjmkvUnrbx6WfsoOgluiBcF1dcVorFPIR0%2FeG%2F8u%2BKLgn2Xusba9ql%2BRsFnUdqhdDfH8ab%2Bz%2BovPeXBGjXubRobu5MTnGUhHcfHRhNDGrEWFjGrVQeqqmjV0kjUnUvevz0VbG9cL1kGjPmCeaa0rTPh6Y%2FCj6EjUM9ibwNtq8VqUJ7xPMj%2FH8nOoV%2BaQP6gNhlrmaPV6kd%2BLuAmM%2FkEMz5H1sLNR5ounZJh%2BKsHIy78VGQy4%2F82LaQ%2Bmj4JF1md40VrMDJm%2BAQp2VTKmFvGkJUV0XWMIhRCDSUZcmjcIVWD%2FeBflcsyPNGFhKdO2KqpMAyUHFD9MQF%2FP5tQgOqqMhYK14izyMMVskznMSV8aaIdc7ydGHWxtQhQWQSNQT8K3lncyh5CetCEYPcMNabcBlyH4HacVSMngKRnfnrxK0ao8rD4pNTTcrwbkardziZQXMnXg7wMcispRixU3hk1J7qgEdTh%2B6nkAhZBmW3kPGksVuDDwlienzgZx6VKXvGNEzues9zGjzMNo4%2FFXrY5YJy71pJEE6%2FCBXsTJ67NtyMxrl9Ir20bk%2FKGm6VNtFJwzI3qzLfZeD4a0%2FNLpUj4sIuneobwtCE%2FIO%2BqSq9zMNH7k70GOqUBfc57QDe6UCd2p1t1VTjfTIasUEiyY4k6FBdkIBom%2BbJuamRSRM2xxPmBBHd3uxXvCA1XLG%2BhtTtGw1IwSjx11VL5g8Rd7u3VUVg%2FZdtWT3%2F6yz2Tr6%2Fxa3dygKroCyS%2FtWxA6s6Wjzq9Hy87XQwHUmdzU0hXcZcJ3gRoYfBtNhD9O7C12pjgne4u9lYCDi%2BarohFdzUjWBMb9buzz2JrnHO0NUTM&X-Amz-Signature=0855dc304592dc050cddccb4613836ef24b46746b796c89d6d921b37e2a2f08d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644NEYAD6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDsltrdweF%2B7AvBE7Why4q%2BU1YEO0zR3dxTXWZ6wE%2FS1AiEA8PsRTbRnIqFhFQgqE%2F0EEKN1HWSF3qZcadVWLCepFvAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDD7v4XREONc9PV42RyrcA5GPSnzqU%2F0n%2FqX9Gen9LdjmkvUnrbx6WfsoOgluiBcF1dcVorFPIR0%2FeG%2F8u%2BKLgn2Xusba9ql%2BRsFnUdqhdDfH8ab%2Bz%2BovPeXBGjXubRobu5MTnGUhHcfHRhNDGrEWFjGrVQeqqmjV0kjUnUvevz0VbG9cL1kGjPmCeaa0rTPh6Y%2FCj6EjUM9ibwNtq8VqUJ7xPMj%2FH8nOoV%2BaQP6gNhlrmaPV6kd%2BLuAmM%2FkEMz5H1sLNR5ounZJh%2BKsHIy78VGQy4%2F82LaQ%2Bmj4JF1md40VrMDJm%2BAQp2VTKmFvGkJUV0XWMIhRCDSUZcmjcIVWD%2FeBflcsyPNGFhKdO2KqpMAyUHFD9MQF%2FP5tQgOqqMhYK14izyMMVskznMSV8aaIdc7ydGHWxtQhQWQSNQT8K3lncyh5CetCEYPcMNabcBlyH4HacVSMngKRnfnrxK0ao8rD4pNTTcrwbkardziZQXMnXg7wMcispRixU3hk1J7qgEdTh%2B6nkAhZBmW3kPGksVuDDwlienzgZx6VKXvGNEzues9zGjzMNo4%2FFXrY5YJy71pJEE6%2FCBXsTJ67NtyMxrl9Ir20bk%2FKGm6VNtFJwzI3qzLfZeD4a0%2FNLpUj4sIuneobwtCE%2FIO%2BqSq9zMNH7k70GOqUBfc57QDe6UCd2p1t1VTjfTIasUEiyY4k6FBdkIBom%2BbJuamRSRM2xxPmBBHd3uxXvCA1XLG%2BhtTtGw1IwSjx11VL5g8Rd7u3VUVg%2FZdtWT3%2F6yz2Tr6%2Fxa3dygKroCyS%2FtWxA6s6Wjzq9Hy87XQwHUmdzU0hXcZcJ3gRoYfBtNhD9O7C12pjgne4u9lYCDi%2BarohFdzUjWBMb9buzz2JrnHO0NUTM&X-Amz-Signature=4056aa5323bba7db77494983d6ce3ea63457c490d87b484285dfc5b0bd709604&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644NEYAD6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDsltrdweF%2B7AvBE7Why4q%2BU1YEO0zR3dxTXWZ6wE%2FS1AiEA8PsRTbRnIqFhFQgqE%2F0EEKN1HWSF3qZcadVWLCepFvAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDD7v4XREONc9PV42RyrcA5GPSnzqU%2F0n%2FqX9Gen9LdjmkvUnrbx6WfsoOgluiBcF1dcVorFPIR0%2FeG%2F8u%2BKLgn2Xusba9ql%2BRsFnUdqhdDfH8ab%2Bz%2BovPeXBGjXubRobu5MTnGUhHcfHRhNDGrEWFjGrVQeqqmjV0kjUnUvevz0VbG9cL1kGjPmCeaa0rTPh6Y%2FCj6EjUM9ibwNtq8VqUJ7xPMj%2FH8nOoV%2BaQP6gNhlrmaPV6kd%2BLuAmM%2FkEMz5H1sLNR5ounZJh%2BKsHIy78VGQy4%2F82LaQ%2Bmj4JF1md40VrMDJm%2BAQp2VTKmFvGkJUV0XWMIhRCDSUZcmjcIVWD%2FeBflcsyPNGFhKdO2KqpMAyUHFD9MQF%2FP5tQgOqqMhYK14izyMMVskznMSV8aaIdc7ydGHWxtQhQWQSNQT8K3lncyh5CetCEYPcMNabcBlyH4HacVSMngKRnfnrxK0ao8rD4pNTTcrwbkardziZQXMnXg7wMcispRixU3hk1J7qgEdTh%2B6nkAhZBmW3kPGksVuDDwlienzgZx6VKXvGNEzues9zGjzMNo4%2FFXrY5YJy71pJEE6%2FCBXsTJ67NtyMxrl9Ir20bk%2FKGm6VNtFJwzI3qzLfZeD4a0%2FNLpUj4sIuneobwtCE%2FIO%2BqSq9zMNH7k70GOqUBfc57QDe6UCd2p1t1VTjfTIasUEiyY4k6FBdkIBom%2BbJuamRSRM2xxPmBBHd3uxXvCA1XLG%2BhtTtGw1IwSjx11VL5g8Rd7u3VUVg%2FZdtWT3%2F6yz2Tr6%2Fxa3dygKroCyS%2FtWxA6s6Wjzq9Hy87XQwHUmdzU0hXcZcJ3gRoYfBtNhD9O7C12pjgne4u9lYCDi%2BarohFdzUjWBMb9buzz2JrnHO0NUTM&X-Amz-Signature=f8d9f974f5d12c1dad88c40697c7aef98d3c3d1403f0e5191abb6e486ae766b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644NEYAD6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDsltrdweF%2B7AvBE7Why4q%2BU1YEO0zR3dxTXWZ6wE%2FS1AiEA8PsRTbRnIqFhFQgqE%2F0EEKN1HWSF3qZcadVWLCepFvAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDD7v4XREONc9PV42RyrcA5GPSnzqU%2F0n%2FqX9Gen9LdjmkvUnrbx6WfsoOgluiBcF1dcVorFPIR0%2FeG%2F8u%2BKLgn2Xusba9ql%2BRsFnUdqhdDfH8ab%2Bz%2BovPeXBGjXubRobu5MTnGUhHcfHRhNDGrEWFjGrVQeqqmjV0kjUnUvevz0VbG9cL1kGjPmCeaa0rTPh6Y%2FCj6EjUM9ibwNtq8VqUJ7xPMj%2FH8nOoV%2BaQP6gNhlrmaPV6kd%2BLuAmM%2FkEMz5H1sLNR5ounZJh%2BKsHIy78VGQy4%2F82LaQ%2Bmj4JF1md40VrMDJm%2BAQp2VTKmFvGkJUV0XWMIhRCDSUZcmjcIVWD%2FeBflcsyPNGFhKdO2KqpMAyUHFD9MQF%2FP5tQgOqqMhYK14izyMMVskznMSV8aaIdc7ydGHWxtQhQWQSNQT8K3lncyh5CetCEYPcMNabcBlyH4HacVSMngKRnfnrxK0ao8rD4pNTTcrwbkardziZQXMnXg7wMcispRixU3hk1J7qgEdTh%2B6nkAhZBmW3kPGksVuDDwlienzgZx6VKXvGNEzues9zGjzMNo4%2FFXrY5YJy71pJEE6%2FCBXsTJ67NtyMxrl9Ir20bk%2FKGm6VNtFJwzI3qzLfZeD4a0%2FNLpUj4sIuneobwtCE%2FIO%2BqSq9zMNH7k70GOqUBfc57QDe6UCd2p1t1VTjfTIasUEiyY4k6FBdkIBom%2BbJuamRSRM2xxPmBBHd3uxXvCA1XLG%2BhtTtGw1IwSjx11VL5g8Rd7u3VUVg%2FZdtWT3%2F6yz2Tr6%2Fxa3dygKroCyS%2FtWxA6s6Wjzq9Hy87XQwHUmdzU0hXcZcJ3gRoYfBtNhD9O7C12pjgne4u9lYCDi%2BarohFdzUjWBMb9buzz2JrnHO0NUTM&X-Amz-Signature=f19b49e1eb93d1d7a2695100c1138e0ff353f1435909be11a758cb764fb25240&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644NEYAD6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDsltrdweF%2B7AvBE7Why4q%2BU1YEO0zR3dxTXWZ6wE%2FS1AiEA8PsRTbRnIqFhFQgqE%2F0EEKN1HWSF3qZcadVWLCepFvAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDD7v4XREONc9PV42RyrcA5GPSnzqU%2F0n%2FqX9Gen9LdjmkvUnrbx6WfsoOgluiBcF1dcVorFPIR0%2FeG%2F8u%2BKLgn2Xusba9ql%2BRsFnUdqhdDfH8ab%2Bz%2BovPeXBGjXubRobu5MTnGUhHcfHRhNDGrEWFjGrVQeqqmjV0kjUnUvevz0VbG9cL1kGjPmCeaa0rTPh6Y%2FCj6EjUM9ibwNtq8VqUJ7xPMj%2FH8nOoV%2BaQP6gNhlrmaPV6kd%2BLuAmM%2FkEMz5H1sLNR5ounZJh%2BKsHIy78VGQy4%2F82LaQ%2Bmj4JF1md40VrMDJm%2BAQp2VTKmFvGkJUV0XWMIhRCDSUZcmjcIVWD%2FeBflcsyPNGFhKdO2KqpMAyUHFD9MQF%2FP5tQgOqqMhYK14izyMMVskznMSV8aaIdc7ydGHWxtQhQWQSNQT8K3lncyh5CetCEYPcMNabcBlyH4HacVSMngKRnfnrxK0ao8rD4pNTTcrwbkardziZQXMnXg7wMcispRixU3hk1J7qgEdTh%2B6nkAhZBmW3kPGksVuDDwlienzgZx6VKXvGNEzues9zGjzMNo4%2FFXrY5YJy71pJEE6%2FCBXsTJ67NtyMxrl9Ir20bk%2FKGm6VNtFJwzI3qzLfZeD4a0%2FNLpUj4sIuneobwtCE%2FIO%2BqSq9zMNH7k70GOqUBfc57QDe6UCd2p1t1VTjfTIasUEiyY4k6FBdkIBom%2BbJuamRSRM2xxPmBBHd3uxXvCA1XLG%2BhtTtGw1IwSjx11VL5g8Rd7u3VUVg%2FZdtWT3%2F6yz2Tr6%2Fxa3dygKroCyS%2FtWxA6s6Wjzq9Hy87XQwHUmdzU0hXcZcJ3gRoYfBtNhD9O7C12pjgne4u9lYCDi%2BarohFdzUjWBMb9buzz2JrnHO0NUTM&X-Amz-Signature=6909f9e9a930db8f812ab87e13c9d7f3d4979e4443470c649d60146c68e03190&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644NEYAD6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDsltrdweF%2B7AvBE7Why4q%2BU1YEO0zR3dxTXWZ6wE%2FS1AiEA8PsRTbRnIqFhFQgqE%2F0EEKN1HWSF3qZcadVWLCepFvAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDD7v4XREONc9PV42RyrcA5GPSnzqU%2F0n%2FqX9Gen9LdjmkvUnrbx6WfsoOgluiBcF1dcVorFPIR0%2FeG%2F8u%2BKLgn2Xusba9ql%2BRsFnUdqhdDfH8ab%2Bz%2BovPeXBGjXubRobu5MTnGUhHcfHRhNDGrEWFjGrVQeqqmjV0kjUnUvevz0VbG9cL1kGjPmCeaa0rTPh6Y%2FCj6EjUM9ibwNtq8VqUJ7xPMj%2FH8nOoV%2BaQP6gNhlrmaPV6kd%2BLuAmM%2FkEMz5H1sLNR5ounZJh%2BKsHIy78VGQy4%2F82LaQ%2Bmj4JF1md40VrMDJm%2BAQp2VTKmFvGkJUV0XWMIhRCDSUZcmjcIVWD%2FeBflcsyPNGFhKdO2KqpMAyUHFD9MQF%2FP5tQgOqqMhYK14izyMMVskznMSV8aaIdc7ydGHWxtQhQWQSNQT8K3lncyh5CetCEYPcMNabcBlyH4HacVSMngKRnfnrxK0ao8rD4pNTTcrwbkardziZQXMnXg7wMcispRixU3hk1J7qgEdTh%2B6nkAhZBmW3kPGksVuDDwlienzgZx6VKXvGNEzues9zGjzMNo4%2FFXrY5YJy71pJEE6%2FCBXsTJ67NtyMxrl9Ir20bk%2FKGm6VNtFJwzI3qzLfZeD4a0%2FNLpUj4sIuneobwtCE%2FIO%2BqSq9zMNH7k70GOqUBfc57QDe6UCd2p1t1VTjfTIasUEiyY4k6FBdkIBom%2BbJuamRSRM2xxPmBBHd3uxXvCA1XLG%2BhtTtGw1IwSjx11VL5g8Rd7u3VUVg%2FZdtWT3%2F6yz2Tr6%2Fxa3dygKroCyS%2FtWxA6s6Wjzq9Hy87XQwHUmdzU0hXcZcJ3gRoYfBtNhD9O7C12pjgne4u9lYCDi%2BarohFdzUjWBMb9buzz2JrnHO0NUTM&X-Amz-Signature=880fd25f33be8376b3996e619956c5fe7803489c47ad208f038801a22b124675&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3ZY7C4A%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDtTvUVcMArBsksVrNtGPQim56GtV2bGtasxxLbea87XwIgXJ2HnzJhNeNVWlPE9tP9QZhk%2Bs2tQ8nzb53n3cn7oooq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDAYQjb3sakUmLS14QyrcA4EA0BbToIOJUPW9YTJvUspwvxZPWcHC3yXYmUgIRJssPpzyVITrhmDhxxGvnIJOENzEhb88z1ABVAivUXJCuTvplv0fWYHxhLjK5Vy76xiwST9Q4955tboXr7Jsi%2Bn5Hug0prGKpNqHty3Mko0W0ZPQPwEYvF4oZABAabDxBfBeGWtC5e07sDgDVauxetkqIgRxazI70gx%2FbddoCGAQqjoNUqJP%2B1zQ2aoEW839Y3uWmXFTKub8VBc%2BmaFgW%2FIdJu46a6%2FcmEY5ISGvrfbU9GftBcVN8uTnr5gtVXIWM%2FFQEbB7OS8WCJFvGgQWokDLyr24Nb50Xfvxkvc%2F%2F1Ay3bwrbBeHrlrtErN2aSpNMrrjY3IvkO%2FHgytEiDzNU6uGL5AYjfGpeT8Go3%2F3eSZt9fA3Ri2bzM3dxwDRhuSu%2BWPH%2Bh7jlM%2BnCxxOaIw4JrlaNXa%2Ftb1m1VjuD9bN1NFhyy2HssLTvDuG8Vf0SuHUvq3yg2BOQ8cYHApuy2Q%2B60rZW4mDn5c9hxzIScLnJj9NHS3PQQg6T0AlORZZiMN6EWF9z0OYFFnuotKLc1g38m6wvi95rVEQyX7hL0D0Mrq6Sl34Qtz%2BSgPM2v0kybJiWyAQo9cwYlC71CCbW37yMPf7k70GOqUBHQSlXdeAg0Rk2b2rz17Gj5y4%2B64MGNnygzxxyGFBQ4OQS%2B4GN40y7rg8wi6s%2BmEDlevwAO9N1pNPwNTr6CvrUgOYfkCGcunmBgJJGigKdvDapSrmusGZ0MTUnK14wQR7yp5KeuO8rp%2F5uQbO4DAkTmP9B08%2F6GuUEHGh2%2BYJIp8biJNSy8crjqYdRPQWqrGHt97XX9TBL2ynSspBETL0uXZ7b%2B9i&X-Amz-Signature=9fd95d630e411b630e7571098360f9b327f7730200aa671e61d99dc7691bb922&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC5WGANV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIF1VdCMzd5y3z9hs0qTaT1SLfat6uVq33pGXVZZPSjL4AiBjjH4cTlsVNE4p3YjbX0Je9akIHlDd%2F3vJU1XaUu0yYSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMqTqHoMw7u8Lvn59pKtwDV8jyVcuWPcYf4Bm5Kk21kkpQ5PP6R4xqPXhjkN9ukrYP%2BWXc%2Bj03q6JUOexuhGU%2F1Cloz0UtEd%2BKbD87sFiyhM91gfToJ1kf%2BeBXe9LjGA1ad2ED4LiCYII25oMINGPRVg9NtbN3B%2BtfCn1Rhl1kGNe%2F7GtrQ0PLOFsTaWJyuWKgWthH%2BvcooWIaOPRRU7tUxBlwc8Gsp%2Fs%2FuwotO5JHL6Ez%2FfXopvArIa%2Bbyr1zUsqFkhfxqULEGaI%2BLvXXHEht4T4bHREZVH%2FsBQoPcaz%2FRoHGcB0gspmcJ2mZiaas8ZoLhThTKO7lAPVMlJCAwO0ViPwxgY%2BmZuzIj5OsfIKleIUxsYv9M5KoXz7q2zD%2FqUiJvpyrZM%2BNzvjTTF1ubO94nokFhBufB44F2DFtvp%2BUPerfkp66eoVolOgpLApcngFtYonVHz8MMTDkxsEl2Wr6B%2FXitG3jyl88W1cu9W%2Be%2F146KxVJMk7Fj5ED%2FwhpvR0dGRv9KrUtoBcNpolUjGyCbEUVHdrEq7ARThaAigAKGasWjLGNUZXZj6IsV27LEeNoGmT5VACL%2FKdiOiIlnAvxx1iiTTqF22CnwLr2l0eCQlbfCzzuYXTHPcuGkmeX5KXG5sw0T57oECRYAhgwmfuTvQY6pgGtK1sWxwS6rCUP4EZOuhNPhpazydLMNngDyuqClhm5W5ahkYWlrt4OB4Y%2Bh32%2FaGJgunP%2FMkzHbpfjN1QaeBYu%2BSuMGR7Z5iRxiRSj8oO6utgUeJLMJSw1ad6%2Fcn13qWdYbb0CC9x%2F94mSVRY1sVxe6mRfLH9NBWIQLEC8R7OljoB2vzJ8bY6b9X2aEhsvQHoKT1KJr6d6hxcsY3uXCo3w021BkqHP&X-Amz-Signature=5ed5d006f28ca9cf6817e0397d5edcac9ff5699a43ba7afc8a473ab2ec8816a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644NEYAD6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDsltrdweF%2B7AvBE7Why4q%2BU1YEO0zR3dxTXWZ6wE%2FS1AiEA8PsRTbRnIqFhFQgqE%2F0EEKN1HWSF3qZcadVWLCepFvAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDD7v4XREONc9PV42RyrcA5GPSnzqU%2F0n%2FqX9Gen9LdjmkvUnrbx6WfsoOgluiBcF1dcVorFPIR0%2FeG%2F8u%2BKLgn2Xusba9ql%2BRsFnUdqhdDfH8ab%2Bz%2BovPeXBGjXubRobu5MTnGUhHcfHRhNDGrEWFjGrVQeqqmjV0kjUnUvevz0VbG9cL1kGjPmCeaa0rTPh6Y%2FCj6EjUM9ibwNtq8VqUJ7xPMj%2FH8nOoV%2BaQP6gNhlrmaPV6kd%2BLuAmM%2FkEMz5H1sLNR5ounZJh%2BKsHIy78VGQy4%2F82LaQ%2Bmj4JF1md40VrMDJm%2BAQp2VTKmFvGkJUV0XWMIhRCDSUZcmjcIVWD%2FeBflcsyPNGFhKdO2KqpMAyUHFD9MQF%2FP5tQgOqqMhYK14izyMMVskznMSV8aaIdc7ydGHWxtQhQWQSNQT8K3lncyh5CetCEYPcMNabcBlyH4HacVSMngKRnfnrxK0ao8rD4pNTTcrwbkardziZQXMnXg7wMcispRixU3hk1J7qgEdTh%2B6nkAhZBmW3kPGksVuDDwlienzgZx6VKXvGNEzues9zGjzMNo4%2FFXrY5YJy71pJEE6%2FCBXsTJ67NtyMxrl9Ir20bk%2FKGm6VNtFJwzI3qzLfZeD4a0%2FNLpUj4sIuneobwtCE%2FIO%2BqSq9zMNH7k70GOqUBfc57QDe6UCd2p1t1VTjfTIasUEiyY4k6FBdkIBom%2BbJuamRSRM2xxPmBBHd3uxXvCA1XLG%2BhtTtGw1IwSjx11VL5g8Rd7u3VUVg%2FZdtWT3%2F6yz2Tr6%2Fxa3dygKroCyS%2FtWxA6s6Wjzq9Hy87XQwHUmdzU0hXcZcJ3gRoYfBtNhD9O7C12pjgne4u9lYCDi%2BarohFdzUjWBMb9buzz2JrnHO0NUTM&X-Amz-Signature=f80279ece73f409d607a83a3bffd7ec28fa95a0acde67788f1e2c46ac784375b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644NEYAD6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDsltrdweF%2B7AvBE7Why4q%2BU1YEO0zR3dxTXWZ6wE%2FS1AiEA8PsRTbRnIqFhFQgqE%2F0EEKN1HWSF3qZcadVWLCepFvAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDD7v4XREONc9PV42RyrcA5GPSnzqU%2F0n%2FqX9Gen9LdjmkvUnrbx6WfsoOgluiBcF1dcVorFPIR0%2FeG%2F8u%2BKLgn2Xusba9ql%2BRsFnUdqhdDfH8ab%2Bz%2BovPeXBGjXubRobu5MTnGUhHcfHRhNDGrEWFjGrVQeqqmjV0kjUnUvevz0VbG9cL1kGjPmCeaa0rTPh6Y%2FCj6EjUM9ibwNtq8VqUJ7xPMj%2FH8nOoV%2BaQP6gNhlrmaPV6kd%2BLuAmM%2FkEMz5H1sLNR5ounZJh%2BKsHIy78VGQy4%2F82LaQ%2Bmj4JF1md40VrMDJm%2BAQp2VTKmFvGkJUV0XWMIhRCDSUZcmjcIVWD%2FeBflcsyPNGFhKdO2KqpMAyUHFD9MQF%2FP5tQgOqqMhYK14izyMMVskznMSV8aaIdc7ydGHWxtQhQWQSNQT8K3lncyh5CetCEYPcMNabcBlyH4HacVSMngKRnfnrxK0ao8rD4pNTTcrwbkardziZQXMnXg7wMcispRixU3hk1J7qgEdTh%2B6nkAhZBmW3kPGksVuDDwlienzgZx6VKXvGNEzues9zGjzMNo4%2FFXrY5YJy71pJEE6%2FCBXsTJ67NtyMxrl9Ir20bk%2FKGm6VNtFJwzI3qzLfZeD4a0%2FNLpUj4sIuneobwtCE%2FIO%2BqSq9zMNH7k70GOqUBfc57QDe6UCd2p1t1VTjfTIasUEiyY4k6FBdkIBom%2BbJuamRSRM2xxPmBBHd3uxXvCA1XLG%2BhtTtGw1IwSjx11VL5g8Rd7u3VUVg%2FZdtWT3%2F6yz2Tr6%2Fxa3dygKroCyS%2FtWxA6s6Wjzq9Hy87XQwHUmdzU0hXcZcJ3gRoYfBtNhD9O7C12pjgne4u9lYCDi%2BarohFdzUjWBMb9buzz2JrnHO0NUTM&X-Amz-Signature=8825af88692436b28edc26f18e3aec376d095d83a30664ea6287a57edb83dc30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644NEYAD6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIDsltrdweF%2B7AvBE7Why4q%2BU1YEO0zR3dxTXWZ6wE%2FS1AiEA8PsRTbRnIqFhFQgqE%2F0EEKN1HWSF3qZcadVWLCepFvAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDD7v4XREONc9PV42RyrcA5GPSnzqU%2F0n%2FqX9Gen9LdjmkvUnrbx6WfsoOgluiBcF1dcVorFPIR0%2FeG%2F8u%2BKLgn2Xusba9ql%2BRsFnUdqhdDfH8ab%2Bz%2BovPeXBGjXubRobu5MTnGUhHcfHRhNDGrEWFjGrVQeqqmjV0kjUnUvevz0VbG9cL1kGjPmCeaa0rTPh6Y%2FCj6EjUM9ibwNtq8VqUJ7xPMj%2FH8nOoV%2BaQP6gNhlrmaPV6kd%2BLuAmM%2FkEMz5H1sLNR5ounZJh%2BKsHIy78VGQy4%2F82LaQ%2Bmj4JF1md40VrMDJm%2BAQp2VTKmFvGkJUV0XWMIhRCDSUZcmjcIVWD%2FeBflcsyPNGFhKdO2KqpMAyUHFD9MQF%2FP5tQgOqqMhYK14izyMMVskznMSV8aaIdc7ydGHWxtQhQWQSNQT8K3lncyh5CetCEYPcMNabcBlyH4HacVSMngKRnfnrxK0ao8rD4pNTTcrwbkardziZQXMnXg7wMcispRixU3hk1J7qgEdTh%2B6nkAhZBmW3kPGksVuDDwlienzgZx6VKXvGNEzues9zGjzMNo4%2FFXrY5YJy71pJEE6%2FCBXsTJ67NtyMxrl9Ir20bk%2FKGm6VNtFJwzI3qzLfZeD4a0%2FNLpUj4sIuneobwtCE%2FIO%2BqSq9zMNH7k70GOqUBfc57QDe6UCd2p1t1VTjfTIasUEiyY4k6FBdkIBom%2BbJuamRSRM2xxPmBBHd3uxXvCA1XLG%2BhtTtGw1IwSjx11VL5g8Rd7u3VUVg%2FZdtWT3%2F6yz2Tr6%2Fxa3dygKroCyS%2FtWxA6s6Wjzq9Hy87XQwHUmdzU0hXcZcJ3gRoYfBtNhD9O7C12pjgne4u9lYCDi%2BarohFdzUjWBMb9buzz2JrnHO0NUTM&X-Amz-Signature=a75325dc0b5ec0efa66b840eb1c483b2feb5f81e732806e6c5ed77f71722799c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJMUWREE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDHkN%2FyPPE%2FMRJl4rf13H2WmM9Wx%2FNzEkvljiQzdwzPZQIgQ%2FhCuSOMEvsYHtYJ3WUPH8xZHu8QuYd3qYa%2Fam%2FSnB4q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDCjyfzwH%2FnpRT2QRrircA52s%2BLFQZCu1H0EDN0O2bPzcgHLjfVxCmZk3JK%2BlxM4v3yITcVOR7dvSNkIIWl001ntKz7dS%2ByzBU9ZwxnB8iB5K5W22MtXbfkkJZ5w0%2BmNorw5TUiivDwx5CiZe4Ciepw5qHQKFexlt48pd2JlqQXhzEPoeJjp8qbakn%2FNJ6Ssu9aRFkDzhZDVKebHTwVNRGcNvYOVh3iJOtrRJyaruigdH9aJbFUOA%2Bi1eLLSHFuLy%2BDCOsvBox0kpufQZ4cbcVwtgjOQ7gQSbuhJBDa9JnxeeFX2G2qC8P%2FFuNnV3bFdNeVGbBUYTC2Vga29YneIvd%2FyVxuM%2Fk2ThI5t%2BC3tkZZzEcuc0vvGKMj0%2FdiUuvO8Rqorl54xusdwdZBOufXJdo2Audq99I6xUidoKMPJ9m6PlFoPpz1ZWrE%2FFxxvjakgUfjUpq0c4E3yC2uBFrnlM382cudZiTh23tG77l49O1vO1BfWpZtg9MN6U6NjwB17uwjf6ZJDraAhlXkBNvGGTj%2FVwmgPN7VKDEUJCjkAVvl1M%2BoURuTJKjT%2FUy5OIABvteYc6YpJsXPjFgwWxKDXBlFukYCdKKs0X7WS6LxO%2BVkXKt5xRfZzZLCYXHEsr8f0C0%2B66R%2FSKUe8IaIrhMJr7k70GOqUBdTtQa8OmBh9WrXswW9W5IS3h%2BBH630aXLKUr594efw3DHYlAAEJq3ZKHH0qFCeKaV0tc39yf2OByOnC5nns9N%2B6kIB4ttk8Ue7CagqOnbzpCQfRgepgt%2FlWy2g%2BZuVcmjkQo2cg39QDWK31FrBDOzp98SuE%2FReBKeY5yTxsXm9wnoh1D3dDsiRIpM0knr4Tyi%2BfwVpWLWXT2Dl7%2Fua0twCdjFdhz&X-Amz-Signature=f923ac6d1c066d25900a5cfa4d3f30cbf29f036c8045dcafb803b03608768b0e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LMQTZXV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIEHdsDXdZttcCsSiHww7ICAbCYtkCZoVeUJIRSjXNGJOAiAzg50OWlwlchaqFE19gA3Q4rAkdG5YuVaglEdqfI10wyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMsO%2BRSy4apdCl0x2MKtwDIH2BhhAfdflwTB47ELkEFlZL4b4AxMaT%2F%2FTtI00ExtzMIFNC%2BnFkfOfYpldG8TcEhWD0wzT3Tkk5V1GevvB3MAvKYtLQKPbiApBuKafdWoRsjFpTiEcBFBltCmmRMr%2BBqyTXfXgPnc291H82k7jrXeSVwXREV9BY%2FZqd%2BhvuO2AFkenlMVZyjwtRS8mJZOUhklrMRqsS5csS1cQ2s%2FBsT%2BVGOPlOJauhybgpn45E5Avtdet%2FVv48QcYFS%2BYql5ELEwBMYs6O%2BsBjvQ0L81qWmA8mpDi3gN5guxO8Jv7V6fxXGPIJk93In8buLeZbeoiE4hgCX9rxRz9rggXcgCTHqWsQbNiajKeybcRHCDgNAPOHaAaIh1w4aGWkuWVj6ud9tuoq1q1HaRuZswuojq6Yql%2BnwEdwHVlwLw6JJEVVyuUhcHyRTU%2FO3eSchoBk6VVVOudb08i84ntlw8QdfhHlaBr7FOaeTzfxpTG9AELcTnT6oxjRMgrtd2Sayd1SrdzB1Ox%2BC28eB%2FA9mXqbdmWsscVnSDSlPtqGbHpgpusabwZpstxkAmFHNNy0ArcJbPkNAKrDjpC3zrRSP%2F3ExchnvzjfZUQU6nKtagBDnccUX72xidz%2BAFkOP%2Ffw60Iw3PuTvQY6pgEU%2BYaBvgwrZ4BS0LgoJDiBSXovlDA6EJ4ui0L8LWKZFiidzXzrMXl2A%2FSfGlajphzWy%2BdTHgaDNmPA4rhEfuWhPvq15y%2B2YDsgsr6tImya3O3l7HTP5RwQ%2FwJCG98%2BSg%2BppfxPwrMQQ9cDf7lPafAs%2FSHm%2BJaEIoEWW%2FB3lBfOrNYeam5i9y6f7wqdo%2B7rU9AzKxEAwGqp4cnkiG%2Bu%2Bx5F%2BPGgSkBh&X-Amz-Signature=dceac1c838616a087868340d3bad55bf0c66c4a3eeb1ab43045ec29208f69982&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QU3B25EI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDG5qkTMdAc9%2BIu5b4bd2lGyFq1HXSBATRi98ZDB2S4AwIgQJ29IXcdSsordjzVuC7TMj9Qm05m2kWKdhVJiBKQpz0q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDORSGJkr5J8VfAZBdircA5oUF8%2Bqf4DqjQWnFN1YYEylpHcuJGNDilGkBkOYoJ5Ati7bsYytj3fYjI7Pks1zYDzEGgtFD9cemmVdXpOpPNnbKafRjf6qkZaTe%2FfwwVhafnHs09n57D4PnZR5bWy%2FJ0cxRpcEWdhjk4nqr%2FXb%2FMqixeN6WEmEjdmRxXc%2Be3UJ0B3xbtKjLocIckHSC45TXi1jDLw9OqySXmw8rFq8WkIn9QkJo8Hac%2BeDAM5bPVmyXvdTrE8hUCJ7fmfcWU%2FwiHpxaSbV4yG%2FZW1CVZlnxsAMKmg0sgXhmcaxr%2BRSIsFJBIRHsxgohg71PlT7bLSY3XP72aKNFLVjKHltuwmSjxdGk2i5o4egRfBIpdktz5S4lKQTcST13p%2BIjCpnhcNy4HfPURGwq0PPdQa5CQ64aTHV3VJhj2yywIhE75ctmgCsHQzEqhf32pn12dTOyGxbpmTAn0yZ05IAe8XdfQXBBgrfO5tkbY9%2Bk%2FOQGaftICL3H9i1P8lYS385lhsMvK8Fs%2F7r6vfuiq9LpgUTRR5DRgwDe%2FDInrgopgUFo0yOXYUO%2BW5RKnVDUQ6%2FPVfQMZuQkEIn0bEroAkB3Nr6NedjumxmdwvjfoNYf5mNXNSrd%2Bs5k7TaqwwVXhE0W7xFMJz7k70GOqUBePUvI8LlBXu1NaNMbn%2FQcQ33o6X0L06vjhH0kuh3gPrGDvTCcfDgg2gjHr2oUaaa3ZeddOG6zGBRODOSYcwdaK4iXkTuwAJ2%2B%2FTk5Y83egvT5j8%2BUc4LyeiDLLbqjQh5Rv7ss%2F1kwXlN1%2BthF8f0VRKg%2BxhQY%2Fkw9bIRskZucNNov%2FlsS%2FdWLOhHUNrutvvsR16PC4u8IhPQeBSApiotgxmy5I8C&X-Amz-Signature=2fa5bec1b02ed495e986bac9e2e77cf067ebf667bd8f30ccd6d32248bd786093&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GFGVVS4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIB8uViHiAqsE%2BWDVnv7pbxAA%2B4mx8VmSMaMLpvpwbF%2B9AiEAgjoxPXvh9lmRFb9ZpJV1gaLBRKuhMAvdlZhari15Qakq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDOI32D%2BCH3zn44kSvircA1EHfDB9EzqntLrRBnhfZQjFgs7bFZx5VoP34vapj60KoSRKmniqI9kPRRNCkFH6SLjiIGB2u2efwBH%2BjWazcH%2FRvj%2BKikKgwPEgRp9870zNs9ZdPLtQtxvUX1Ic%2FBWkoBa5dFWqKuZDq5p5UndvK5JctRaU4yDGrGXu%2BZtbGs80Ehc2v6loiedx88T5BBWdSsg%2FkZHhGwoZQq2ZGfIH%2B1xHtmW6vxKrUU0aLiYy9YioC5ypJSDxgV1icH0tAVXVeFqoWfpxGqpdt9oR1WPzb0HF7enQQDlDYFkMWw%2F%2BqgZfrEgGBftT6MxFeNoiEyr0Y9Sr6%2BKmCDHySXkmQyEJ%2FgOXTMQ0zjCWqOdLToczSu%2FVd1D7aPH7HXScVHEc4t8sSMWD4nF5ewHBrBgL8YSn7iT3V%2BXN0Wa7KhfVMhL6ybMQASngvx%2B06273Ip1NR5TCiO5%2Fch%2BVv5Ah6A1P5EisOsw%2BIBXBQ5jglWjOJ4IXc2vgbrtw1xG7RSOqYpBKr2GZdBn6T5pooMlfq0GZFLB%2BQuBdNpsrF5P8NijxXYn5GTDwzZmelOx3o4Ysy6rwPsSBnSGIX8lA5nmkGCQcAzLduub%2BwFqUlTXbHOsyesyKxNbWldp27qY2cxmw%2FG5jMPP7k70GOqUBUv0qvg5lSNDnOQtG%2FU%2F5LPjuJhY%2Fl%2FXATWXAqgjm7c9a0bGuemuwWRxQ8K8bZOPk094zJhT6FRWXkXpRUUpMAsUSkT8bvvwAuwo6l8uNcFFOrN2MT8SrevmQbUKxiRKNU7RFK0MnI%2Bu6sLmtdKQ6MbxbikP07oTBwi08ecxd3IUsSX13VJfCVPSwOFV8AT0lxWGq0%2FNaTiy%2BSqzog6pAWiox0Gof&X-Amz-Signature=5c57dbfc51b163973dd704755dd6f1fac5d06027e24fe1ed25723ec24171c76d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GFGVVS4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIB8uViHiAqsE%2BWDVnv7pbxAA%2B4mx8VmSMaMLpvpwbF%2B9AiEAgjoxPXvh9lmRFb9ZpJV1gaLBRKuhMAvdlZhari15Qakq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDOI32D%2BCH3zn44kSvircA1EHfDB9EzqntLrRBnhfZQjFgs7bFZx5VoP34vapj60KoSRKmniqI9kPRRNCkFH6SLjiIGB2u2efwBH%2BjWazcH%2FRvj%2BKikKgwPEgRp9870zNs9ZdPLtQtxvUX1Ic%2FBWkoBa5dFWqKuZDq5p5UndvK5JctRaU4yDGrGXu%2BZtbGs80Ehc2v6loiedx88T5BBWdSsg%2FkZHhGwoZQq2ZGfIH%2B1xHtmW6vxKrUU0aLiYy9YioC5ypJSDxgV1icH0tAVXVeFqoWfpxGqpdt9oR1WPzb0HF7enQQDlDYFkMWw%2F%2BqgZfrEgGBftT6MxFeNoiEyr0Y9Sr6%2BKmCDHySXkmQyEJ%2FgOXTMQ0zjCWqOdLToczSu%2FVd1D7aPH7HXScVHEc4t8sSMWD4nF5ewHBrBgL8YSn7iT3V%2BXN0Wa7KhfVMhL6ybMQASngvx%2B06273Ip1NR5TCiO5%2Fch%2BVv5Ah6A1P5EisOsw%2BIBXBQ5jglWjOJ4IXc2vgbrtw1xG7RSOqYpBKr2GZdBn6T5pooMlfq0GZFLB%2BQuBdNpsrF5P8NijxXYn5GTDwzZmelOx3o4Ysy6rwPsSBnSGIX8lA5nmkGCQcAzLduub%2BwFqUlTXbHOsyesyKxNbWldp27qY2cxmw%2FG5jMPP7k70GOqUBUv0qvg5lSNDnOQtG%2FU%2F5LPjuJhY%2Fl%2FXATWXAqgjm7c9a0bGuemuwWRxQ8K8bZOPk094zJhT6FRWXkXpRUUpMAsUSkT8bvvwAuwo6l8uNcFFOrN2MT8SrevmQbUKxiRKNU7RFK0MnI%2Bu6sLmtdKQ6MbxbikP07oTBwi08ecxd3IUsSX13VJfCVPSwOFV8AT0lxWGq0%2FNaTiy%2BSqzog6pAWiox0Gof&X-Amz-Signature=05d75126bcf7678cba958449ae4d04b40d205aa4abfacc78e813546c376e80bc&X-Amz-SignedHeaders=host&x-id=GetObject)

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
