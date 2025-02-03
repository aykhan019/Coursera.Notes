

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY3UK7VV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCI8VhOOPEQjFEFUAMVy3z6qI%2FI5dwJN%2BkRjdmZni73NgIgT2QgHVoybRygkcNegEQNPP4HK82d%2BeGS9C9vFS0TPiQq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDBaD3gvVo%2BjYnri4XircAyN1bX7rLKZu%2Bg29HS%2FjueauTcsbA5uvjOjsOVs43u3zADgRGhn7w8bvrXDolNXQGcIPscJVBHOvX%2B0azhY4aMJVn%2FQpes3rzvx58GOn9SlyJKVWSyX91qAuNIJuEMR4JgjOE1kJ8i%2BqrCM9OZIPxHwxZwKSrlCStcdEnXQSRHNHQLTXSFf7V73tZRlgw0pPBAVJWRjcavzmgU9nY4CPCBBdOAUHjcmgPU9Njzyi8ZEFjMKjc86InMuk0PPks5ow3UNtf8wxuQot7QNKstAkLoGQlYFryYb7eT6tSnhIDyNRR9Iv4ZKxcU7b4n8%2FxjS7OW5lrcrdUUObmVb2zROOQJb%2FE%2Bxr19UEG3Iz%2B74%2FGCez9BMMGyicbSQIwjUYTm2jJgPetvn5dKs0tVUJZ3GF37mykSQ%2BJ1m1IVAgMbEPAS7xBYTlN9l4Zx6zl9wDDGp1rGkK%2B39SUmjV3%2ByeNcbcpo8W%2FhpjOKbxTgqTNb28qCee8QCopd3pW1TUAgeOGMjQer7clTu98YM%2BJMcHsD4r0eJT7Arou9F2NTkkikyDgNbsGuR80VaqbnbjIde1IzctN676y6tJ8hx4TMfukxAev%2B9t0hf39c0LXl2CXBg09uirdLWgckzbqXfPG5vXMKrWgb0GOqUB5Gdnpznv5Vu5AGMkWGJyziabpln5MUGRzbhH6aizK2zXjvqvWOlesMemT0g0dE8FEoX3SeQrsdNNmilm62fhW5GiRh1xbZP3cfLuy4LMzAVBXPOgOnyBGNW3aMjVXg%2FBjzPyaqArIXiiol5wwUmC9lBtZ8FKJ0G8TTj3IK4OHBgZrRWQvvRMsKLemzSn1gvmHTHEhmBJjpQscm7TRQf9eUjPoRZQ&X-Amz-Signature=237c643aa71665fd2e6da2b00387844e21301c000b3825c972ec56e5f2f96779&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY3UK7VV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCI8VhOOPEQjFEFUAMVy3z6qI%2FI5dwJN%2BkRjdmZni73NgIgT2QgHVoybRygkcNegEQNPP4HK82d%2BeGS9C9vFS0TPiQq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDBaD3gvVo%2BjYnri4XircAyN1bX7rLKZu%2Bg29HS%2FjueauTcsbA5uvjOjsOVs43u3zADgRGhn7w8bvrXDolNXQGcIPscJVBHOvX%2B0azhY4aMJVn%2FQpes3rzvx58GOn9SlyJKVWSyX91qAuNIJuEMR4JgjOE1kJ8i%2BqrCM9OZIPxHwxZwKSrlCStcdEnXQSRHNHQLTXSFf7V73tZRlgw0pPBAVJWRjcavzmgU9nY4CPCBBdOAUHjcmgPU9Njzyi8ZEFjMKjc86InMuk0PPks5ow3UNtf8wxuQot7QNKstAkLoGQlYFryYb7eT6tSnhIDyNRR9Iv4ZKxcU7b4n8%2FxjS7OW5lrcrdUUObmVb2zROOQJb%2FE%2Bxr19UEG3Iz%2B74%2FGCez9BMMGyicbSQIwjUYTm2jJgPetvn5dKs0tVUJZ3GF37mykSQ%2BJ1m1IVAgMbEPAS7xBYTlN9l4Zx6zl9wDDGp1rGkK%2B39SUmjV3%2ByeNcbcpo8W%2FhpjOKbxTgqTNb28qCee8QCopd3pW1TUAgeOGMjQer7clTu98YM%2BJMcHsD4r0eJT7Arou9F2NTkkikyDgNbsGuR80VaqbnbjIde1IzctN676y6tJ8hx4TMfukxAev%2B9t0hf39c0LXl2CXBg09uirdLWgckzbqXfPG5vXMKrWgb0GOqUB5Gdnpznv5Vu5AGMkWGJyziabpln5MUGRzbhH6aizK2zXjvqvWOlesMemT0g0dE8FEoX3SeQrsdNNmilm62fhW5GiRh1xbZP3cfLuy4LMzAVBXPOgOnyBGNW3aMjVXg%2FBjzPyaqArIXiiol5wwUmC9lBtZ8FKJ0G8TTj3IK4OHBgZrRWQvvRMsKLemzSn1gvmHTHEhmBJjpQscm7TRQf9eUjPoRZQ&X-Amz-Signature=f2c9b0a61bd7bb7959aece865832ab6edf47d414cb0e1b88c692742c6ac23d38&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY3UK7VV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCI8VhOOPEQjFEFUAMVy3z6qI%2FI5dwJN%2BkRjdmZni73NgIgT2QgHVoybRygkcNegEQNPP4HK82d%2BeGS9C9vFS0TPiQq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDBaD3gvVo%2BjYnri4XircAyN1bX7rLKZu%2Bg29HS%2FjueauTcsbA5uvjOjsOVs43u3zADgRGhn7w8bvrXDolNXQGcIPscJVBHOvX%2B0azhY4aMJVn%2FQpes3rzvx58GOn9SlyJKVWSyX91qAuNIJuEMR4JgjOE1kJ8i%2BqrCM9OZIPxHwxZwKSrlCStcdEnXQSRHNHQLTXSFf7V73tZRlgw0pPBAVJWRjcavzmgU9nY4CPCBBdOAUHjcmgPU9Njzyi8ZEFjMKjc86InMuk0PPks5ow3UNtf8wxuQot7QNKstAkLoGQlYFryYb7eT6tSnhIDyNRR9Iv4ZKxcU7b4n8%2FxjS7OW5lrcrdUUObmVb2zROOQJb%2FE%2Bxr19UEG3Iz%2B74%2FGCez9BMMGyicbSQIwjUYTm2jJgPetvn5dKs0tVUJZ3GF37mykSQ%2BJ1m1IVAgMbEPAS7xBYTlN9l4Zx6zl9wDDGp1rGkK%2B39SUmjV3%2ByeNcbcpo8W%2FhpjOKbxTgqTNb28qCee8QCopd3pW1TUAgeOGMjQer7clTu98YM%2BJMcHsD4r0eJT7Arou9F2NTkkikyDgNbsGuR80VaqbnbjIde1IzctN676y6tJ8hx4TMfukxAev%2B9t0hf39c0LXl2CXBg09uirdLWgckzbqXfPG5vXMKrWgb0GOqUB5Gdnpznv5Vu5AGMkWGJyziabpln5MUGRzbhH6aizK2zXjvqvWOlesMemT0g0dE8FEoX3SeQrsdNNmilm62fhW5GiRh1xbZP3cfLuy4LMzAVBXPOgOnyBGNW3aMjVXg%2FBjzPyaqArIXiiol5wwUmC9lBtZ8FKJ0G8TTj3IK4OHBgZrRWQvvRMsKLemzSn1gvmHTHEhmBJjpQscm7TRQf9eUjPoRZQ&X-Amz-Signature=b628f6bfa16847e44c6c71cbeee18c9fccf4c43262435b7eb67a53c902e16ffc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF7X6DGI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNli27zukWa3C10aC4n0FYiIXSuBa36Sa7F4RGP2vjyAiEA3QN78PFcRXECbP7ZRrD1fBEQuefIBUubVKVJP16KcMoq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDCHa6af8H3E72LpQvSrcA382PIvkHEB5mq7WelOCAFaftpuFOyF0rM%2BVBfhl3XIIRyTrszFBtiJEBUdo%2FxFqy%2Bn3eKMtyX8yt1l9fZWs33ge29nEQ6mnlurwMGWnW7NR9j%2BKiTiwsIjdu3oClt8mq0SSWP2520VUEhnsicBSYm9nViS7r3sSDgjk%2F5Bd6k%2B4j4r8AEqjKL%2Fewwq6r3O1oP0qeCXyLrJdiUcFKCvltEOC9tuPJ%2BltS6DAygX3rE0E1XfhVmFWDlRmry8oXYO3XJf6uz8qRRz2xEG%2F6WITlav8jlYoykvaMq1tr1y5628QFqjhgVaB9n%2FJVg4UJuqqBAx%2B40P16luvusBjCv214SJg4nAxtGKkZWl49HNxqHh3C3u8Sr8xinZoSptIPFiWEczpzkx7MQhv%2F0gG8yhDe6q6lVMFla%2FWJyVIIYfi%2Fdzel0ivcjOMzNTAyzZG410lcpVGgEOHv%2BT2k19b1%2FSM399FEqkuyv8NZicDn1wWyWiNogcUqi7JRSDuTQyArracfqTmKjBVviWHjGIN6bh%2BVHe8%2FOqgOnbi9Cz5ph1soHw4JydjfPWmmH7ryXIXxlgvx3cSkuTvZh5rQKwQwY9Si%2BNygsNoukpITzaS6jCyt5WTXYjMEbn9qIxcRPXmMKrXgb0GOqUBgv5EOMV6n15X9fzBCJqht5NjyfpFzRJnq1hU6846TBzBtrvvAGzB7pzk%2BwYb1EqUuznmumRDSfI9Un6aSSdMitAG8flaLCGqy8sQDDkaKx7OhsEh8bn5mNGC4us3nKOhYIpwo%2BodBs%2BzsHTvVGk5tjxOJvIwGCn7kaRW7GVh7d11h4B0G%2BEZS9VrVc4MRyn3Pz2HTRjqiF%2FBnX251UOnZKNFgfMy&X-Amz-Signature=04a342b96cdbf9db138ec99565046a5f523b23b2af9c998605d0357960531f09&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF7X6DGI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNli27zukWa3C10aC4n0FYiIXSuBa36Sa7F4RGP2vjyAiEA3QN78PFcRXECbP7ZRrD1fBEQuefIBUubVKVJP16KcMoq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDCHa6af8H3E72LpQvSrcA382PIvkHEB5mq7WelOCAFaftpuFOyF0rM%2BVBfhl3XIIRyTrszFBtiJEBUdo%2FxFqy%2Bn3eKMtyX8yt1l9fZWs33ge29nEQ6mnlurwMGWnW7NR9j%2BKiTiwsIjdu3oClt8mq0SSWP2520VUEhnsicBSYm9nViS7r3sSDgjk%2F5Bd6k%2B4j4r8AEqjKL%2Fewwq6r3O1oP0qeCXyLrJdiUcFKCvltEOC9tuPJ%2BltS6DAygX3rE0E1XfhVmFWDlRmry8oXYO3XJf6uz8qRRz2xEG%2F6WITlav8jlYoykvaMq1tr1y5628QFqjhgVaB9n%2FJVg4UJuqqBAx%2B40P16luvusBjCv214SJg4nAxtGKkZWl49HNxqHh3C3u8Sr8xinZoSptIPFiWEczpzkx7MQhv%2F0gG8yhDe6q6lVMFla%2FWJyVIIYfi%2Fdzel0ivcjOMzNTAyzZG410lcpVGgEOHv%2BT2k19b1%2FSM399FEqkuyv8NZicDn1wWyWiNogcUqi7JRSDuTQyArracfqTmKjBVviWHjGIN6bh%2BVHe8%2FOqgOnbi9Cz5ph1soHw4JydjfPWmmH7ryXIXxlgvx3cSkuTvZh5rQKwQwY9Si%2BNygsNoukpITzaS6jCyt5WTXYjMEbn9qIxcRPXmMKrXgb0GOqUBgv5EOMV6n15X9fzBCJqht5NjyfpFzRJnq1hU6846TBzBtrvvAGzB7pzk%2BwYb1EqUuznmumRDSfI9Un6aSSdMitAG8flaLCGqy8sQDDkaKx7OhsEh8bn5mNGC4us3nKOhYIpwo%2BodBs%2BzsHTvVGk5tjxOJvIwGCn7kaRW7GVh7d11h4B0G%2BEZS9VrVc4MRyn3Pz2HTRjqiF%2FBnX251UOnZKNFgfMy&X-Amz-Signature=0cbef8e2c9056e1a86e5cc0af818c776e03986ecb7770c12aa88a34c30c4adc3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF7X6DGI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNli27zukWa3C10aC4n0FYiIXSuBa36Sa7F4RGP2vjyAiEA3QN78PFcRXECbP7ZRrD1fBEQuefIBUubVKVJP16KcMoq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDCHa6af8H3E72LpQvSrcA382PIvkHEB5mq7WelOCAFaftpuFOyF0rM%2BVBfhl3XIIRyTrszFBtiJEBUdo%2FxFqy%2Bn3eKMtyX8yt1l9fZWs33ge29nEQ6mnlurwMGWnW7NR9j%2BKiTiwsIjdu3oClt8mq0SSWP2520VUEhnsicBSYm9nViS7r3sSDgjk%2F5Bd6k%2B4j4r8AEqjKL%2Fewwq6r3O1oP0qeCXyLrJdiUcFKCvltEOC9tuPJ%2BltS6DAygX3rE0E1XfhVmFWDlRmry8oXYO3XJf6uz8qRRz2xEG%2F6WITlav8jlYoykvaMq1tr1y5628QFqjhgVaB9n%2FJVg4UJuqqBAx%2B40P16luvusBjCv214SJg4nAxtGKkZWl49HNxqHh3C3u8Sr8xinZoSptIPFiWEczpzkx7MQhv%2F0gG8yhDe6q6lVMFla%2FWJyVIIYfi%2Fdzel0ivcjOMzNTAyzZG410lcpVGgEOHv%2BT2k19b1%2FSM399FEqkuyv8NZicDn1wWyWiNogcUqi7JRSDuTQyArracfqTmKjBVviWHjGIN6bh%2BVHe8%2FOqgOnbi9Cz5ph1soHw4JydjfPWmmH7ryXIXxlgvx3cSkuTvZh5rQKwQwY9Si%2BNygsNoukpITzaS6jCyt5WTXYjMEbn9qIxcRPXmMKrXgb0GOqUBgv5EOMV6n15X9fzBCJqht5NjyfpFzRJnq1hU6846TBzBtrvvAGzB7pzk%2BwYb1EqUuznmumRDSfI9Un6aSSdMitAG8flaLCGqy8sQDDkaKx7OhsEh8bn5mNGC4us3nKOhYIpwo%2BodBs%2BzsHTvVGk5tjxOJvIwGCn7kaRW7GVh7d11h4B0G%2BEZS9VrVc4MRyn3Pz2HTRjqiF%2FBnX251UOnZKNFgfMy&X-Amz-Signature=c8d083118dead037bd47451e9f38af95d60757737637fa3d6c7b953c1447effa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF7X6DGI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNli27zukWa3C10aC4n0FYiIXSuBa36Sa7F4RGP2vjyAiEA3QN78PFcRXECbP7ZRrD1fBEQuefIBUubVKVJP16KcMoq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDCHa6af8H3E72LpQvSrcA382PIvkHEB5mq7WelOCAFaftpuFOyF0rM%2BVBfhl3XIIRyTrszFBtiJEBUdo%2FxFqy%2Bn3eKMtyX8yt1l9fZWs33ge29nEQ6mnlurwMGWnW7NR9j%2BKiTiwsIjdu3oClt8mq0SSWP2520VUEhnsicBSYm9nViS7r3sSDgjk%2F5Bd6k%2B4j4r8AEqjKL%2Fewwq6r3O1oP0qeCXyLrJdiUcFKCvltEOC9tuPJ%2BltS6DAygX3rE0E1XfhVmFWDlRmry8oXYO3XJf6uz8qRRz2xEG%2F6WITlav8jlYoykvaMq1tr1y5628QFqjhgVaB9n%2FJVg4UJuqqBAx%2B40P16luvusBjCv214SJg4nAxtGKkZWl49HNxqHh3C3u8Sr8xinZoSptIPFiWEczpzkx7MQhv%2F0gG8yhDe6q6lVMFla%2FWJyVIIYfi%2Fdzel0ivcjOMzNTAyzZG410lcpVGgEOHv%2BT2k19b1%2FSM399FEqkuyv8NZicDn1wWyWiNogcUqi7JRSDuTQyArracfqTmKjBVviWHjGIN6bh%2BVHe8%2FOqgOnbi9Cz5ph1soHw4JydjfPWmmH7ryXIXxlgvx3cSkuTvZh5rQKwQwY9Si%2BNygsNoukpITzaS6jCyt5WTXYjMEbn9qIxcRPXmMKrXgb0GOqUBgv5EOMV6n15X9fzBCJqht5NjyfpFzRJnq1hU6846TBzBtrvvAGzB7pzk%2BwYb1EqUuznmumRDSfI9Un6aSSdMitAG8flaLCGqy8sQDDkaKx7OhsEh8bn5mNGC4us3nKOhYIpwo%2BodBs%2BzsHTvVGk5tjxOJvIwGCn7kaRW7GVh7d11h4B0G%2BEZS9VrVc4MRyn3Pz2HTRjqiF%2FBnX251UOnZKNFgfMy&X-Amz-Signature=04668741bc4bafa9b204b9fc797d2652338fd810027889749be33663d26af1a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF7X6DGI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNli27zukWa3C10aC4n0FYiIXSuBa36Sa7F4RGP2vjyAiEA3QN78PFcRXECbP7ZRrD1fBEQuefIBUubVKVJP16KcMoq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDCHa6af8H3E72LpQvSrcA382PIvkHEB5mq7WelOCAFaftpuFOyF0rM%2BVBfhl3XIIRyTrszFBtiJEBUdo%2FxFqy%2Bn3eKMtyX8yt1l9fZWs33ge29nEQ6mnlurwMGWnW7NR9j%2BKiTiwsIjdu3oClt8mq0SSWP2520VUEhnsicBSYm9nViS7r3sSDgjk%2F5Bd6k%2B4j4r8AEqjKL%2Fewwq6r3O1oP0qeCXyLrJdiUcFKCvltEOC9tuPJ%2BltS6DAygX3rE0E1XfhVmFWDlRmry8oXYO3XJf6uz8qRRz2xEG%2F6WITlav8jlYoykvaMq1tr1y5628QFqjhgVaB9n%2FJVg4UJuqqBAx%2B40P16luvusBjCv214SJg4nAxtGKkZWl49HNxqHh3C3u8Sr8xinZoSptIPFiWEczpzkx7MQhv%2F0gG8yhDe6q6lVMFla%2FWJyVIIYfi%2Fdzel0ivcjOMzNTAyzZG410lcpVGgEOHv%2BT2k19b1%2FSM399FEqkuyv8NZicDn1wWyWiNogcUqi7JRSDuTQyArracfqTmKjBVviWHjGIN6bh%2BVHe8%2FOqgOnbi9Cz5ph1soHw4JydjfPWmmH7ryXIXxlgvx3cSkuTvZh5rQKwQwY9Si%2BNygsNoukpITzaS6jCyt5WTXYjMEbn9qIxcRPXmMKrXgb0GOqUBgv5EOMV6n15X9fzBCJqht5NjyfpFzRJnq1hU6846TBzBtrvvAGzB7pzk%2BwYb1EqUuznmumRDSfI9Un6aSSdMitAG8flaLCGqy8sQDDkaKx7OhsEh8bn5mNGC4us3nKOhYIpwo%2BodBs%2BzsHTvVGk5tjxOJvIwGCn7kaRW7GVh7d11h4B0G%2BEZS9VrVc4MRyn3Pz2HTRjqiF%2FBnX251UOnZKNFgfMy&X-Amz-Signature=3ff74a16f0643697aa8223afaab13e86ea200668ec1aad2de6d2c50b3a523987&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF7X6DGI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNli27zukWa3C10aC4n0FYiIXSuBa36Sa7F4RGP2vjyAiEA3QN78PFcRXECbP7ZRrD1fBEQuefIBUubVKVJP16KcMoq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDCHa6af8H3E72LpQvSrcA382PIvkHEB5mq7WelOCAFaftpuFOyF0rM%2BVBfhl3XIIRyTrszFBtiJEBUdo%2FxFqy%2Bn3eKMtyX8yt1l9fZWs33ge29nEQ6mnlurwMGWnW7NR9j%2BKiTiwsIjdu3oClt8mq0SSWP2520VUEhnsicBSYm9nViS7r3sSDgjk%2F5Bd6k%2B4j4r8AEqjKL%2Fewwq6r3O1oP0qeCXyLrJdiUcFKCvltEOC9tuPJ%2BltS6DAygX3rE0E1XfhVmFWDlRmry8oXYO3XJf6uz8qRRz2xEG%2F6WITlav8jlYoykvaMq1tr1y5628QFqjhgVaB9n%2FJVg4UJuqqBAx%2B40P16luvusBjCv214SJg4nAxtGKkZWl49HNxqHh3C3u8Sr8xinZoSptIPFiWEczpzkx7MQhv%2F0gG8yhDe6q6lVMFla%2FWJyVIIYfi%2Fdzel0ivcjOMzNTAyzZG410lcpVGgEOHv%2BT2k19b1%2FSM399FEqkuyv8NZicDn1wWyWiNogcUqi7JRSDuTQyArracfqTmKjBVviWHjGIN6bh%2BVHe8%2FOqgOnbi9Cz5ph1soHw4JydjfPWmmH7ryXIXxlgvx3cSkuTvZh5rQKwQwY9Si%2BNygsNoukpITzaS6jCyt5WTXYjMEbn9qIxcRPXmMKrXgb0GOqUBgv5EOMV6n15X9fzBCJqht5NjyfpFzRJnq1hU6846TBzBtrvvAGzB7pzk%2BwYb1EqUuznmumRDSfI9Un6aSSdMitAG8flaLCGqy8sQDDkaKx7OhsEh8bn5mNGC4us3nKOhYIpwo%2BodBs%2BzsHTvVGk5tjxOJvIwGCn7kaRW7GVh7d11h4B0G%2BEZS9VrVc4MRyn3Pz2HTRjqiF%2FBnX251UOnZKNFgfMy&X-Amz-Signature=6fd47755b6ec07f1bea4f1514ae21b61ae0df3a79854da648783c7f581d42837&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCMWA6Z3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZCmVzXbr6cYoQ9SZsZVui5I2vo2HparJusMUI7aOmXwIgSdsA%2F6Ow3X8oRf2YMhfUA7uW7E5gbKwZHqZZIkFgNe8q%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDLOgQZuGRE7PLBDi3ircA5Q8OyeM3K7HDcNUGJi9zxLdvrSrRGHk7h9yTxyJhVlijpmBqHPs%2F5cgEEDRnlLfvsqlr%2Fyj1hAkB%2FQTnJ%2BzrYPjq2xmothy%2FRW7UtQsfXac1CkJDqJktNk9kwgkAEOPl4M%2F5RSLqP1WovrqNHbBLiTDwlD52LZkdnL9%2BLoq9M0QWjHH3mafHhIZuDUG7NCEJX8dSG3AgkuKGQDSUe8AugLndm6ipoq9cJO433gs6oiiRHgk%2BA52BmbnE%2BksMsYUR9KN0V66H6OtObK%2BytTKowsbTSh5fiASDfXMngMrnQaLpB%2FXcVD1Hz%2FeFm7p2ufu3%2FmDKmwAQW2lKxYfb%2F3xHWbiOYbMAPC7S9O%2BGUprpoNLQvFGnirlIqCZjzI1OD%2BXj91riipqf4bM8C9pTqLmQ4SWKBiFzfPlx1iHmcsgYLtj57%2BP53l%2Bs0lckEMb3xdWc%2BEAs3UYnM3rDpKydPxkxo0RAgxGIompGK%2FCiYt6UYOWkYRghi5dXZJfV%2BHvCjXhkt7NvemlNtgpaPzQIBBU8sJ9%2F0G43PTj6wOZRp90UiITsknc2T2NEVXiuXTqN0oTHCtxKjM8Kx%2FcW3Lk7hxSsCgGlCnsixvLFdodyLNN%2F9mt53naVmHFXsDEhbTRMKnWgb0GOqUBj6C0tA6s31ofH3HS%2B3%2B0%2Foe%2FO5AoqKVQkXnZW%2FaUQwcGnOyFMvKYyMTyU57g33J1iH9dd5p0jvvl4Fmu%2B9UHoyPV3DvepfPZa%2BPKARf9zUN3DxtYO38os1RmAO4SgbDBlx9tf9BtYOS8soo%2FB81dyFfferENQC38Mnr%2FxYwKGt8dyylv97oJHoP75rOiMl%2F%2BvLw%2F1Yho4DJ8H%2FFiI5yzm8yt1BXO&X-Amz-Signature=2af47a23ae954d8c5c47a99402ff63b4a15a1e3678985768a11e4c49dd2762cf&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPPDDHDU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICC6HnaNuIRMKituPWi%2Bgmwx0RJdn6sIk4UXelc5fmTGAiEA%2BPzxfRMBZjQxHGrJ9%2BHAzsszq4lvWJttpi795VHqxioq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDLxlum37XbrCfk4WYCrcAyAhP64XsuIv3dwhBQUWySAj8Rqc3yc94iq2D5PMEExsouaTisaYC1JLVwu2SBZY2AyaYTEzp6H970RHUzTR3VR7FNdBvqsl1Kg4MDOQiJ1WZ472btYG4J6w6JvYLSwx2yQFh2J%2FlEW9MPRZx2tIZ6IhgyK3CJVNfH6BNnW7J3X6x8tj82rrH3JrHNOO4At8izi5gBBtmNn6daXShQ8q8tLiiE6x5E7YJwA6tnpzQKt3CdIcwTQBR31Si%2BPWJUoeOwdQ%2FBJ1Hucm713nII8BtigaOLorEp2%2FkwSjmogxhEv2A4X5cO33Cqy70u97lJYAefCIn3PJOppDA1bNCZ2HOWAr%2BHydZRf3BTbUT7ZqJkJe%2Bve6bbe1BNlexHCW3gCXrdv5EcNS4UdqXkQOGWnEjGpGU3afgI%2BC1QpHZeDgA2KsB3mh1CTAQTk%2FAhN58xT2QkLb5Tz8ZnBDpI1K5ZsEfsTPKM98FpWb8fL5hbX158oo5%2FfAC189Ksmb%2B9M8ZM2QYZmkJgSadWz4%2BssXcZR11r0fnjh8jMEZsHn3%2FSPuQZaijlbf9zV3LLaeSfwT139zFDlltcWoG%2Bn4mMIMmukTD4UBLXaS4VTSqdLLzLAeRr7ajrX7gKvVDN1t4T8CMP7Wgb0GOqUBb9%2BZe3WrPl%2BO3HI9D5LI9u2O2BIEvVkyPFVDIE6wgYgoR9NxpKfUEvoafgka9FFBM4NAdzc3RFpKNanm8jwwXYL5QxD6%2B4J3RbA%2B6GP%2FdZU21qdAX2jw%2BQBAdsGZ3%2Fd24ZxqL%2FYYgS3FJdDZ44JPlkU%2BVbi0nDJxVbK9LFkkO8VxSKTT8IEy6qYqjoA5o4wE7O26%2BRApk4GqIbSthbLGnrgD1O9F&X-Amz-Signature=636f61bcc16b2d424f0aad8c3be2ee859c337b9777d7a86732ac10afaf3e0b68&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF7X6DGI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNli27zukWa3C10aC4n0FYiIXSuBa36Sa7F4RGP2vjyAiEA3QN78PFcRXECbP7ZRrD1fBEQuefIBUubVKVJP16KcMoq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDCHa6af8H3E72LpQvSrcA382PIvkHEB5mq7WelOCAFaftpuFOyF0rM%2BVBfhl3XIIRyTrszFBtiJEBUdo%2FxFqy%2Bn3eKMtyX8yt1l9fZWs33ge29nEQ6mnlurwMGWnW7NR9j%2BKiTiwsIjdu3oClt8mq0SSWP2520VUEhnsicBSYm9nViS7r3sSDgjk%2F5Bd6k%2B4j4r8AEqjKL%2Fewwq6r3O1oP0qeCXyLrJdiUcFKCvltEOC9tuPJ%2BltS6DAygX3rE0E1XfhVmFWDlRmry8oXYO3XJf6uz8qRRz2xEG%2F6WITlav8jlYoykvaMq1tr1y5628QFqjhgVaB9n%2FJVg4UJuqqBAx%2B40P16luvusBjCv214SJg4nAxtGKkZWl49HNxqHh3C3u8Sr8xinZoSptIPFiWEczpzkx7MQhv%2F0gG8yhDe6q6lVMFla%2FWJyVIIYfi%2Fdzel0ivcjOMzNTAyzZG410lcpVGgEOHv%2BT2k19b1%2FSM399FEqkuyv8NZicDn1wWyWiNogcUqi7JRSDuTQyArracfqTmKjBVviWHjGIN6bh%2BVHe8%2FOqgOnbi9Cz5ph1soHw4JydjfPWmmH7ryXIXxlgvx3cSkuTvZh5rQKwQwY9Si%2BNygsNoukpITzaS6jCyt5WTXYjMEbn9qIxcRPXmMKrXgb0GOqUBgv5EOMV6n15X9fzBCJqht5NjyfpFzRJnq1hU6846TBzBtrvvAGzB7pzk%2BwYb1EqUuznmumRDSfI9Un6aSSdMitAG8flaLCGqy8sQDDkaKx7OhsEh8bn5mNGC4us3nKOhYIpwo%2BodBs%2BzsHTvVGk5tjxOJvIwGCn7kaRW7GVh7d11h4B0G%2BEZS9VrVc4MRyn3Pz2HTRjqiF%2FBnX251UOnZKNFgfMy&X-Amz-Signature=9f5a47b612c3963943a74497c5cce4bd380d08e2e3eb8fde6d71166975414c54&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF7X6DGI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNli27zukWa3C10aC4n0FYiIXSuBa36Sa7F4RGP2vjyAiEA3QN78PFcRXECbP7ZRrD1fBEQuefIBUubVKVJP16KcMoq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDCHa6af8H3E72LpQvSrcA382PIvkHEB5mq7WelOCAFaftpuFOyF0rM%2BVBfhl3XIIRyTrszFBtiJEBUdo%2FxFqy%2Bn3eKMtyX8yt1l9fZWs33ge29nEQ6mnlurwMGWnW7NR9j%2BKiTiwsIjdu3oClt8mq0SSWP2520VUEhnsicBSYm9nViS7r3sSDgjk%2F5Bd6k%2B4j4r8AEqjKL%2Fewwq6r3O1oP0qeCXyLrJdiUcFKCvltEOC9tuPJ%2BltS6DAygX3rE0E1XfhVmFWDlRmry8oXYO3XJf6uz8qRRz2xEG%2F6WITlav8jlYoykvaMq1tr1y5628QFqjhgVaB9n%2FJVg4UJuqqBAx%2B40P16luvusBjCv214SJg4nAxtGKkZWl49HNxqHh3C3u8Sr8xinZoSptIPFiWEczpzkx7MQhv%2F0gG8yhDe6q6lVMFla%2FWJyVIIYfi%2Fdzel0ivcjOMzNTAyzZG410lcpVGgEOHv%2BT2k19b1%2FSM399FEqkuyv8NZicDn1wWyWiNogcUqi7JRSDuTQyArracfqTmKjBVviWHjGIN6bh%2BVHe8%2FOqgOnbi9Cz5ph1soHw4JydjfPWmmH7ryXIXxlgvx3cSkuTvZh5rQKwQwY9Si%2BNygsNoukpITzaS6jCyt5WTXYjMEbn9qIxcRPXmMKrXgb0GOqUBgv5EOMV6n15X9fzBCJqht5NjyfpFzRJnq1hU6846TBzBtrvvAGzB7pzk%2BwYb1EqUuznmumRDSfI9Un6aSSdMitAG8flaLCGqy8sQDDkaKx7OhsEh8bn5mNGC4us3nKOhYIpwo%2BodBs%2BzsHTvVGk5tjxOJvIwGCn7kaRW7GVh7d11h4B0G%2BEZS9VrVc4MRyn3Pz2HTRjqiF%2FBnX251UOnZKNFgfMy&X-Amz-Signature=33ac7d63bdd9e4cfd5dcd924279128986b1b0e013910e0495cbb632a716ee5b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF7X6DGI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNli27zukWa3C10aC4n0FYiIXSuBa36Sa7F4RGP2vjyAiEA3QN78PFcRXECbP7ZRrD1fBEQuefIBUubVKVJP16KcMoq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDCHa6af8H3E72LpQvSrcA382PIvkHEB5mq7WelOCAFaftpuFOyF0rM%2BVBfhl3XIIRyTrszFBtiJEBUdo%2FxFqy%2Bn3eKMtyX8yt1l9fZWs33ge29nEQ6mnlurwMGWnW7NR9j%2BKiTiwsIjdu3oClt8mq0SSWP2520VUEhnsicBSYm9nViS7r3sSDgjk%2F5Bd6k%2B4j4r8AEqjKL%2Fewwq6r3O1oP0qeCXyLrJdiUcFKCvltEOC9tuPJ%2BltS6DAygX3rE0E1XfhVmFWDlRmry8oXYO3XJf6uz8qRRz2xEG%2F6WITlav8jlYoykvaMq1tr1y5628QFqjhgVaB9n%2FJVg4UJuqqBAx%2B40P16luvusBjCv214SJg4nAxtGKkZWl49HNxqHh3C3u8Sr8xinZoSptIPFiWEczpzkx7MQhv%2F0gG8yhDe6q6lVMFla%2FWJyVIIYfi%2Fdzel0ivcjOMzNTAyzZG410lcpVGgEOHv%2BT2k19b1%2FSM399FEqkuyv8NZicDn1wWyWiNogcUqi7JRSDuTQyArracfqTmKjBVviWHjGIN6bh%2BVHe8%2FOqgOnbi9Cz5ph1soHw4JydjfPWmmH7ryXIXxlgvx3cSkuTvZh5rQKwQwY9Si%2BNygsNoukpITzaS6jCyt5WTXYjMEbn9qIxcRPXmMKrXgb0GOqUBgv5EOMV6n15X9fzBCJqht5NjyfpFzRJnq1hU6846TBzBtrvvAGzB7pzk%2BwYb1EqUuznmumRDSfI9Un6aSSdMitAG8flaLCGqy8sQDDkaKx7OhsEh8bn5mNGC4us3nKOhYIpwo%2BodBs%2BzsHTvVGk5tjxOJvIwGCn7kaRW7GVh7d11h4B0G%2BEZS9VrVc4MRyn3Pz2HTRjqiF%2FBnX251UOnZKNFgfMy&X-Amz-Signature=47f56c1b9b30a4373890419640b213244b84b120d1068200840ce5d22e65944a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625SVHDX4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMnWXQM10eL7zkSgGOcki%2FNy2IdBhqf8FYV2TxV6177QIhAIDnVLjkGCeIxLd1sGXUJnGwZYQYny703agfmFvGSSpaKv8DCBAQABoMNjM3NDIzMTgzODA1IgzJyr3lk7EJ6iJUvW0q3APrcyVhoYEHPC%2FS7JUk7LusjCnzixQDrnjNK6zaEKGEQKl1RdVidbIoGqlHQIYBzskUpcDzkgA%2BQ5%2BGVvyAha7ejtPmQzBsM1i5Mb0JDchVzrUUANs9NSBqr5sgKq%2BFOLxt32N3oAu9xtwpsR4LHeANQmUpwc3zxxhT1TzefzdnMOnl1g4KwoUScDjlw2BuR4cxnBhyqBeeovao6IM90WTpvJHlsQCvUPJmIgqjlYgNeHCUxUPfEs8sD4HriumZ3d7XHFfvMRXWv3dzs2AuRKdckedxK4RS6wi0Kh7L8wO6CAZ6lMlwb9rgGnBvo0QdwPcqz5KMGbcpFK3cWiGnUH2F1E6CEPrC%2Fvcl2p9Jw3mowngw66o%2BrFEAHmf2xyPw1%2BBdI1Ni2BkYgxQcaLCAgcjVeLxT0LCVxXIMD6mwaK5FwNPqgYWT6mFQ1BFpzZ3CrbLhWO%2B0rjvjfqY93SBphnmQCWoweR%2Blux2mIp5alBeOuzL4TscMNa%2FkE%2BYFYf%2Bv9y%2FTsSR4ZcpeSI4oD4dA9u0tcY8sp3W%2BiMr1NvKscfCbWOLl4BTk73QVj%2BsI4Qd6huQPYBzQbeIWAi3k42wCPAFQC9m2wjSS0IFLXp6A61nKgLRK1ZKpbw6bPGf%2B8zCk1oG9BjqkAVkoAfmLSz9InW8FE%2F2mGuaK%2Fz4tEqdebq8QgaUNsMw5OUrvrquUY8COAhPpPj65cJbtqYz94NfcOgpT1DZmxylCWwnB4IFvHdMmbqChF90nD%2FlOPIDO%2FQemxgyIOHIErTfUCp%2Bl%2FbC6%2FTaljFxBGf3vYLqmxJJgiqI4wTC4N6KVQ0SQbtZZAjIT3iMZvhMrV1hM0zq%2B7DlO0%2FS%2BssIVmR4cP4Ky&X-Amz-Signature=8664c86874290b12d7bc9f46ae5d2b1d34c9fb46760743b2b09a9b34981ead3a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBAMQVGN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGl9KOmtIoB2qFjlz0TUMvAapuAWiJzxYGopFMAKJSdOAiEAmelcIdQVj%2FrUjYhjhMJ0ynF9An9rhOtCouDstjAOX6Qq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDHyD4BpxCtu4q0zWYyrcA2OhjfTN4nbT3sJUUpNl9wbzQ4OzCBcpCZUsfy90Cy1ArLUUIzkhlDCd8MTvpyzcSt4BysVUyPZEVTtCqVwCbE0qfi3MSGADSn65D40pRe9LStsMaXxRj66tteqlj03EPxviMmDsidgBcMQ5vGlrRwrJmEMTLXKufzAsJXC2aQQY9fgoZbhxc4oQbfHQ%2F9DmcjX%2BMgnL%2F0wGOf4zfMowk76KerlszKt5Gagh9TzzsmKTz6TQxV%2F1kaOg4J3zvqLoIVol30aqSTfT4QXhiTknQc3a%2BdnvC7TDnbvfIZYICj0XArds33trH7ABoNlBQif4LsaMrXMNZvdKtz5kgUjG27rbxUlIVHTn93jN0KGjct2nCkOiRVm1jagVVaQ3roQbhVWQjiBUs6tOOIgKzze5l7ClyFZpUrefNO%2F%2FhsfJjGairN9ZXWokMW3H6E9og28299VKTkN5Dq%2B3gJeg7UqEFx25Y4%2Fv84M5eQ4yVz1%2Bs4mpowgT7%2B9krGvYoaYz5K%2FWfB4yrfaiC%2B1mF%2BH2MZodwsdADrO0buvOr%2BW379nf6FC7sp54d%2F8X%2BtYToc6hCirNUAHuj7h5XT2qxqmk22Osq6XubWaQWYXpcHe5Xkr4tNmVNOOcfWPxdDt%2B2YyHMPzWgb0GOqUB%2BXufEyAY5u4OLu8Dbb%2Fu5EVm2vLBPFYOEVbUvgOfeRBFAk2742gSsGe%2B52np%2BI8WQSYJNtA0CKGCOscVcaSHMHIjh0KYFwRbudzzTGXEK%2BO31d3r9TDdScB%2FVSziOQN%2BMn7wEhIUYBBw7D6B2PK8ojPvEIF%2BUny2ggvueonaBao2nxmMjwApQaSSqaH6fRb4qudS5VjqPzqliLSmCtyRonTJ4vYU&X-Amz-Signature=ab9687d3eb74b58c95f093059dc99b0ccc785fed02191429ba50b62f01bd2acc&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674Z62RF7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBY0qaYuqZz0E5bAoUi4n7Nwxf29PmIFMqdWl8S5OHzyAiA02HjBKc3bYN9JABnkcFMWJRsBTwHUGpTvmQlg9s7duir%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMdYobo1hKVnL5pZ%2BGKtwDDFbidpC1siYPnG1I6WLrA0ZK8UY0zT%2BIl3Ns5Y1ODGp16SGMeUbFP5RgCZAllNFn66Ifn%2BX8MVKJg5n9yPB0ECNQWi15NkXiUzqG5TNhCmOPEDZx2V3Q7VppbwmprQNACtYAUa%2F5o9%2BuBtcim3ohxgdLJ2Shoc2kELcbvy%2BeDzO5fHnf481TSTceqwTTiyzBEHCZDv4kEghFOHo8Meg6MiYhc7PHwWTt8wmM4JZIs%2F0gr5DiYe1FaatGAf6scJk%2FI2JBx7FVUhyUaZzxrK1CKSW7GUQGvSBft1Zhic9uqyIQAEJBiQzUKVwQjdwfLVBaRIMdJkmamBTnxqrNbppaXhcZkIZVAS%2FmecLd7rjWQ0BXHBcXLai%2Fj1CXMwIa0XA48f%2BRiAXThYRsTtYDV3oFipNAE1aBkjecbL9g35aqJ8kPrqJUbRT7cjW7W04BtVwtpPSU%2FnYyOwcWYlNJNk%2FD2VJ4qXgkouCgl%2FS7cYKZL%2FlCAF8dFfKrsFfGDRN9KszH4zaPw13%2FNCxg6yXlvSf5bmOAGwOXx4%2FsVQ434r23s2t57BTokMm7SDhIIjCbbTRs9Mh8PmbcxzHjm9HKJBKiUdJ4IwkpkfpmgnBJtXdGWSOLxfMRsOQyG3uqpu0wn9aBvQY6pgF0NrKabM%2BYutblYCBK6vypMzvywGSV1FY7brTLlClD8ZW4tOhjv8D3DVzgL1mI1J5pdoPZPBix5sJe3kD5Y3pB1QrESyqBwkdcPlgqfzuRDDLpF%2B8yYGzjy7j%2FkUr1U%2FLr3wTkstOhoKiP7cTI7sqrBjOrK1anRigDybm0l7FS7vna9UZudKS19tL8SyinJIcZmsHMok9hLEWH6OX8L8zmmgKLz%2B9L&X-Amz-Signature=c7662094d5a4dc8ff67ea5afbaeb3bbe3b2641cbceb43beec91939f72d8cdffe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O7X2Z5M%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFh40WSaDNZXF%2Bemk%2F%2FXPynHdUBOlWekbRilOaL3z9bEAiBjODmer11eZnryuJ9W2n1kw3HFFdNvfnhJ2Y3%2BaPsuZCr%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMt9mhVT6da1RgoS3OKtwDsrYuOnzsd%2BJ1DnVjA1xCZ50Gs1Qw%2F0yN7JcCYsEnei5IOg1Q8AVt1PuRmZJJAK3Q7OX8m7nN1kpjuQBtmhEHiazvwXTMqTBoQIPXwujXTc1GkNw%2FwJnpR8jKs8tz0LnJQ9W2JSwDPhrZvs4G3hcGCgi7%2ByU4H5rsUTJewIvHR6quSKSj1bfsJD%2F%2FtDqJZIVf0ZGU2QQlb%2B2CkpmffDTRBZR%2BQZFW1BDrkMCIa8gwEPJWyf%2FhFPEacvzAIXWuYEw03t%2BMp6JG96eJ9bGnDQkNqfcjtKC6B8787fnZxci%2BaOg8ZPoDVoVEauAX2CyL12toGzMfOjYFHoPbFLGwTTAp97SmZ04N77VjtTdsvycn7C%2B1sRjPvegyE1q89nXqhyHjn0bHvFzEBXHcj8Gt%2FH5k%2Fej1xo1cuRay5MvFkpf9jtnVP3pLrSMgUerm%2BUVNoiphrKYG4jxBDn1jx2AeybzhILmmLr6b3gwJDsG3Jx4JQ2IxB3Ad0ZAdRUEbmX5Ily2Dm5hlkpu2t8QrbQbnPlq%2FtqN%2F4YLAh%2FYjODT%2FsmbwLjR%2FpWW%2FVqnOFeCao8CRIK1hbyaLKYVBjVt8pfz%2Bse%2B8OtQTk3GgPhIN07rfklB8YIsQ12VinS64n3Fek0wwyNaBvQY6pgEI%2BSQFFW%2FwBh1bp8rovQ7Vwq%2FqA7t4ABypqEYlhEqfRMHQXqjzs%2FGj7u%2BnvZL6JPxdiPavQ7b%2Fjbit33KM4%2F1HRVAR41FH%2FSKocGxX%2Bv6QpB5deFg1tMhkKNB54xjfYsjlDTYR41gVqTNU%2FDe97AVkNkL7wGEAkopOk%2Bld3Czadgyh%2BDEjuSMdmtm5i3o%2FpmJbQUxi2BbeVNqIGbtwlKJ6jEmDMc2S&X-Amz-Signature=5d8abff7c7648c4cb17fa6523eec2b23c7ea42fa95a100bf0d6111fc2976ddce&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O7X2Z5M%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFh40WSaDNZXF%2Bemk%2F%2FXPynHdUBOlWekbRilOaL3z9bEAiBjODmer11eZnryuJ9W2n1kw3HFFdNvfnhJ2Y3%2BaPsuZCr%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMt9mhVT6da1RgoS3OKtwDsrYuOnzsd%2BJ1DnVjA1xCZ50Gs1Qw%2F0yN7JcCYsEnei5IOg1Q8AVt1PuRmZJJAK3Q7OX8m7nN1kpjuQBtmhEHiazvwXTMqTBoQIPXwujXTc1GkNw%2FwJnpR8jKs8tz0LnJQ9W2JSwDPhrZvs4G3hcGCgi7%2ByU4H5rsUTJewIvHR6quSKSj1bfsJD%2F%2FtDqJZIVf0ZGU2QQlb%2B2CkpmffDTRBZR%2BQZFW1BDrkMCIa8gwEPJWyf%2FhFPEacvzAIXWuYEw03t%2BMp6JG96eJ9bGnDQkNqfcjtKC6B8787fnZxci%2BaOg8ZPoDVoVEauAX2CyL12toGzMfOjYFHoPbFLGwTTAp97SmZ04N77VjtTdsvycn7C%2B1sRjPvegyE1q89nXqhyHjn0bHvFzEBXHcj8Gt%2FH5k%2Fej1xo1cuRay5MvFkpf9jtnVP3pLrSMgUerm%2BUVNoiphrKYG4jxBDn1jx2AeybzhILmmLr6b3gwJDsG3Jx4JQ2IxB3Ad0ZAdRUEbmX5Ily2Dm5hlkpu2t8QrbQbnPlq%2FtqN%2F4YLAh%2FYjODT%2FsmbwLjR%2FpWW%2FVqnOFeCao8CRIK1hbyaLKYVBjVt8pfz%2Bse%2B8OtQTk3GgPhIN07rfklB8YIsQ12VinS64n3Fek0wwyNaBvQY6pgEI%2BSQFFW%2FwBh1bp8rovQ7Vwq%2FqA7t4ABypqEYlhEqfRMHQXqjzs%2FGj7u%2BnvZL6JPxdiPavQ7b%2Fjbit33KM4%2F1HRVAR41FH%2FSKocGxX%2Bv6QpB5deFg1tMhkKNB54xjfYsjlDTYR41gVqTNU%2FDe97AVkNkL7wGEAkopOk%2Bld3Czadgyh%2BDEjuSMdmtm5i3o%2FpmJbQUxi2BbeVNqIGbtwlKJ6jEmDMc2S&X-Amz-Signature=0b78e550899febbebf95c20d17661d98e8c20cdc15d53f627e2e55db139a4586&X-Amz-SignedHeaders=host&x-id=GetObject)

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
