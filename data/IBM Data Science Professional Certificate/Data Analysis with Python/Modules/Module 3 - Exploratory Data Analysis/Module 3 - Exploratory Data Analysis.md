

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEGIP4P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIGpMPlBab7INgOGS%2FueUN1WQ26UnvHko14UmDjOHMPVqAiEAhSs95llcBSq8fqJr0AZsWATFBzf5ZnOnxFWkUm0goCcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLGWarSkvPXhHhA6ZircA7ec7CTKCrAnPs9mOopXu6v45XmUsiUPEmx6IooL1943dq65Rko5iK%2B1EzC4wiml%2BASVzUhCGK8408ehZkjvz18cWPQ1hiIuJTaRJatcnOZ57tQpTJrBpnLuJ8ry0hPiF0ZvsgZzPxasKoNC%2Bc67MKnTZSfBdYS7X6kU0cTm959EqgFgXAw%2BAl7eIxvTQOLpfhoqtz2SIv0GJFOKaGn6QjO9BOxEqLaeUkLbEkBe%2FSGHKmKNIzDEXl1hiv2EoB6oiZPvrgbSMndRcUhWX5t32fSfDKzUXr20egUSP%2FHweAJxa777XZ2s5%2F%2FDEqv4DMKd%2FGojy6BEyXnYihDxlXU6dW5bVBmoA2eBhifLSJlv0wz%2F0MZCWNSuMSg%2F8BDj0AyY3sEX5zhr9p71S0IbBi4CGwSsBNZd6twr9P0VTZMDfxEb1tb5xyCYV1wRXOcQ8SnPzG09c%2BxWGtcEjvrvFJyrWWpCfQnLePAEFHIDez2O3ZwNLXp0v3uF6UtJ8QQGmAHOKZ8t1V3jWuBlaJ1Ztd%2B6qbaCCdikofmnD326k9lPGqPqicSUf%2Bbb5OrRrURAVlw%2FJ3JTn25YfhVZn4I6CR1n8fUYtvi3c8UiRWh5IoX4s8%2Bcu9HPX3rZA7jtXeJ%2BMNrKh70GOqUB9xx2sotzSMIn8mrbBhhEZHDWcXkR3R1sCtGAm78mBr%2B8FY56rD0GdMSv9ceGSYHgE8MmDQo4tAJ0Hq3nyuMRKPkOZHUhzPSCWr%2F8gU9XwP0GAaZwmYuBPiN4H2Y7kDwO2Fa4WzOX7gWQ7bV%2BssJalaz6FdXskMNEURxDU2SD27KZYBYYQkgfat%2FXtiLVZEF%2BRYplAhVhMuDSxCJl3yJ63KiMQdvI&X-Amz-Signature=31fd6926331332f87432c4a3fa0cd0dd8302708cb3106e04121622347f3875c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEGIP4P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIGpMPlBab7INgOGS%2FueUN1WQ26UnvHko14UmDjOHMPVqAiEAhSs95llcBSq8fqJr0AZsWATFBzf5ZnOnxFWkUm0goCcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLGWarSkvPXhHhA6ZircA7ec7CTKCrAnPs9mOopXu6v45XmUsiUPEmx6IooL1943dq65Rko5iK%2B1EzC4wiml%2BASVzUhCGK8408ehZkjvz18cWPQ1hiIuJTaRJatcnOZ57tQpTJrBpnLuJ8ry0hPiF0ZvsgZzPxasKoNC%2Bc67MKnTZSfBdYS7X6kU0cTm959EqgFgXAw%2BAl7eIxvTQOLpfhoqtz2SIv0GJFOKaGn6QjO9BOxEqLaeUkLbEkBe%2FSGHKmKNIzDEXl1hiv2EoB6oiZPvrgbSMndRcUhWX5t32fSfDKzUXr20egUSP%2FHweAJxa777XZ2s5%2F%2FDEqv4DMKd%2FGojy6BEyXnYihDxlXU6dW5bVBmoA2eBhifLSJlv0wz%2F0MZCWNSuMSg%2F8BDj0AyY3sEX5zhr9p71S0IbBi4CGwSsBNZd6twr9P0VTZMDfxEb1tb5xyCYV1wRXOcQ8SnPzG09c%2BxWGtcEjvrvFJyrWWpCfQnLePAEFHIDez2O3ZwNLXp0v3uF6UtJ8QQGmAHOKZ8t1V3jWuBlaJ1Ztd%2B6qbaCCdikofmnD326k9lPGqPqicSUf%2Bbb5OrRrURAVlw%2FJ3JTn25YfhVZn4I6CR1n8fUYtvi3c8UiRWh5IoX4s8%2Bcu9HPX3rZA7jtXeJ%2BMNrKh70GOqUB9xx2sotzSMIn8mrbBhhEZHDWcXkR3R1sCtGAm78mBr%2B8FY56rD0GdMSv9ceGSYHgE8MmDQo4tAJ0Hq3nyuMRKPkOZHUhzPSCWr%2F8gU9XwP0GAaZwmYuBPiN4H2Y7kDwO2Fa4WzOX7gWQ7bV%2BssJalaz6FdXskMNEURxDU2SD27KZYBYYQkgfat%2FXtiLVZEF%2BRYplAhVhMuDSxCJl3yJ63KiMQdvI&X-Amz-Signature=e22fa2525d3ffe8d0a003c2855c0c790a7ec020af93fae2559df34b1aef51408&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBEGIP4P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIGpMPlBab7INgOGS%2FueUN1WQ26UnvHko14UmDjOHMPVqAiEAhSs95llcBSq8fqJr0AZsWATFBzf5ZnOnxFWkUm0goCcq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLGWarSkvPXhHhA6ZircA7ec7CTKCrAnPs9mOopXu6v45XmUsiUPEmx6IooL1943dq65Rko5iK%2B1EzC4wiml%2BASVzUhCGK8408ehZkjvz18cWPQ1hiIuJTaRJatcnOZ57tQpTJrBpnLuJ8ry0hPiF0ZvsgZzPxasKoNC%2Bc67MKnTZSfBdYS7X6kU0cTm959EqgFgXAw%2BAl7eIxvTQOLpfhoqtz2SIv0GJFOKaGn6QjO9BOxEqLaeUkLbEkBe%2FSGHKmKNIzDEXl1hiv2EoB6oiZPvrgbSMndRcUhWX5t32fSfDKzUXr20egUSP%2FHweAJxa777XZ2s5%2F%2FDEqv4DMKd%2FGojy6BEyXnYihDxlXU6dW5bVBmoA2eBhifLSJlv0wz%2F0MZCWNSuMSg%2F8BDj0AyY3sEX5zhr9p71S0IbBi4CGwSsBNZd6twr9P0VTZMDfxEb1tb5xyCYV1wRXOcQ8SnPzG09c%2BxWGtcEjvrvFJyrWWpCfQnLePAEFHIDez2O3ZwNLXp0v3uF6UtJ8QQGmAHOKZ8t1V3jWuBlaJ1Ztd%2B6qbaCCdikofmnD326k9lPGqPqicSUf%2Bbb5OrRrURAVlw%2FJ3JTn25YfhVZn4I6CR1n8fUYtvi3c8UiRWh5IoX4s8%2Bcu9HPX3rZA7jtXeJ%2BMNrKh70GOqUB9xx2sotzSMIn8mrbBhhEZHDWcXkR3R1sCtGAm78mBr%2B8FY56rD0GdMSv9ceGSYHgE8MmDQo4tAJ0Hq3nyuMRKPkOZHUhzPSCWr%2F8gU9XwP0GAaZwmYuBPiN4H2Y7kDwO2Fa4WzOX7gWQ7bV%2BssJalaz6FdXskMNEURxDU2SD27KZYBYYQkgfat%2FXtiLVZEF%2BRYplAhVhMuDSxCJl3yJ63KiMQdvI&X-Amz-Signature=e23bd1768a073cd5a9e1128857fa531b7206436be1c3946b7c233751a185e6de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZBIOC7C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD0HDQcuI9BsLbDyPY%2FvZ3%2BAdPJMJw7QCFUi8xqDciDugIgDTCdeyvk5rr8s%2F7N8FvYXzjCDQdOT43TRZEyjg9EYYgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLlXfKDfkIbGFW5FySrcA%2Fm9KhL1ToDWj5z5r6CLfhhvAh2SXKvoZ8qy69D603VTI2Fg%2BHJLfh%2BnAtrQDamuW%2FChGtJoJmvbGJk3RsyfLb%2BFzO6ryEkM4C3rMvgAKcdM7cml2%2FLqjTS3IaRsjKVi3tOqNhjGqBubVQjqiQF5P9uY7WNO0o01dZZ82IR1fSa%2Bw%2BS4tkwIi5JxNr8w0xb3juPMixkauG1HIrSw2%2Fmob7RrSvoAhs81BlN4HXgWfuaMCfDki76VaVZNsF92lQ%2Bkozq80VVxq6kJGQOOimyC%2FQxCXBXnQhHd4KaOcHmUTY%2Bnm2BtzknsVEmKTiJO9Gjb%2BC5Q5jYhZeTICujMB%2Band38I5JP%2FxBotjDSondJ1KRG0oouTOohowLA3q8hHMFvGmf%2B6xudmV%2B7m%2BTe7fH5JE8jLSNgE1pfHpdpUlcD4MFT5Aayhkd7sI4ZDHQmc3PV5BPInQ%2Bobl%2FBi2jG7XElrw8VTP1946FlygbFjAqh551nwu6uNlTUqkyjP7JpGsFbBRB%2Bk4xhixVIpNQFXww5nqD%2FAskAbId5WhrzBYgbItjyNGqJ0vsKeMvmfYl5XBtN1ESuMuz2BISYSTlQF%2BDTJ3XIa2Cwq5jsr7pdZKrja9IiTeQSlXcrFtn3wCta7MJHKh70GOqUBKIcXX605kjKyj56QlNp2rl6O9bkGySufs1Vd07O3Ri8gAqeJt9tIN8XPLJkj%2BabHeKuAamqdotRJG6RT8jWZzV8GMhVpzbhJAlJhBGedaMGJn2FDXcaxChvxpYz9jbpxHrwxjvrsIirMIsqDjWe1vKJVz5OgA4CclNXLfrHLCOo14%2FB3bmBEiwlbQPoEtQeGhPbSB3JmLdw0eGt3OZQ19qKxnUXO&X-Amz-Signature=772b448c0d3815577c8d19fb63349f2ff79de5a768f3ad7d10628dd7254caedf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZBIOC7C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD0HDQcuI9BsLbDyPY%2FvZ3%2BAdPJMJw7QCFUi8xqDciDugIgDTCdeyvk5rr8s%2F7N8FvYXzjCDQdOT43TRZEyjg9EYYgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLlXfKDfkIbGFW5FySrcA%2Fm9KhL1ToDWj5z5r6CLfhhvAh2SXKvoZ8qy69D603VTI2Fg%2BHJLfh%2BnAtrQDamuW%2FChGtJoJmvbGJk3RsyfLb%2BFzO6ryEkM4C3rMvgAKcdM7cml2%2FLqjTS3IaRsjKVi3tOqNhjGqBubVQjqiQF5P9uY7WNO0o01dZZ82IR1fSa%2Bw%2BS4tkwIi5JxNr8w0xb3juPMixkauG1HIrSw2%2Fmob7RrSvoAhs81BlN4HXgWfuaMCfDki76VaVZNsF92lQ%2Bkozq80VVxq6kJGQOOimyC%2FQxCXBXnQhHd4KaOcHmUTY%2Bnm2BtzknsVEmKTiJO9Gjb%2BC5Q5jYhZeTICujMB%2Band38I5JP%2FxBotjDSondJ1KRG0oouTOohowLA3q8hHMFvGmf%2B6xudmV%2B7m%2BTe7fH5JE8jLSNgE1pfHpdpUlcD4MFT5Aayhkd7sI4ZDHQmc3PV5BPInQ%2Bobl%2FBi2jG7XElrw8VTP1946FlygbFjAqh551nwu6uNlTUqkyjP7JpGsFbBRB%2Bk4xhixVIpNQFXww5nqD%2FAskAbId5WhrzBYgbItjyNGqJ0vsKeMvmfYl5XBtN1ESuMuz2BISYSTlQF%2BDTJ3XIa2Cwq5jsr7pdZKrja9IiTeQSlXcrFtn3wCta7MJHKh70GOqUBKIcXX605kjKyj56QlNp2rl6O9bkGySufs1Vd07O3Ri8gAqeJt9tIN8XPLJkj%2BabHeKuAamqdotRJG6RT8jWZzV8GMhVpzbhJAlJhBGedaMGJn2FDXcaxChvxpYz9jbpxHrwxjvrsIirMIsqDjWe1vKJVz5OgA4CclNXLfrHLCOo14%2FB3bmBEiwlbQPoEtQeGhPbSB3JmLdw0eGt3OZQ19qKxnUXO&X-Amz-Signature=c59d03aa746440c2df97f9e352377a0e6eb10f92fe287f9bc5e8d08a1742fa6c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZBIOC7C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD0HDQcuI9BsLbDyPY%2FvZ3%2BAdPJMJw7QCFUi8xqDciDugIgDTCdeyvk5rr8s%2F7N8FvYXzjCDQdOT43TRZEyjg9EYYgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLlXfKDfkIbGFW5FySrcA%2Fm9KhL1ToDWj5z5r6CLfhhvAh2SXKvoZ8qy69D603VTI2Fg%2BHJLfh%2BnAtrQDamuW%2FChGtJoJmvbGJk3RsyfLb%2BFzO6ryEkM4C3rMvgAKcdM7cml2%2FLqjTS3IaRsjKVi3tOqNhjGqBubVQjqiQF5P9uY7WNO0o01dZZ82IR1fSa%2Bw%2BS4tkwIi5JxNr8w0xb3juPMixkauG1HIrSw2%2Fmob7RrSvoAhs81BlN4HXgWfuaMCfDki76VaVZNsF92lQ%2Bkozq80VVxq6kJGQOOimyC%2FQxCXBXnQhHd4KaOcHmUTY%2Bnm2BtzknsVEmKTiJO9Gjb%2BC5Q5jYhZeTICujMB%2Band38I5JP%2FxBotjDSondJ1KRG0oouTOohowLA3q8hHMFvGmf%2B6xudmV%2B7m%2BTe7fH5JE8jLSNgE1pfHpdpUlcD4MFT5Aayhkd7sI4ZDHQmc3PV5BPInQ%2Bobl%2FBi2jG7XElrw8VTP1946FlygbFjAqh551nwu6uNlTUqkyjP7JpGsFbBRB%2Bk4xhixVIpNQFXww5nqD%2FAskAbId5WhrzBYgbItjyNGqJ0vsKeMvmfYl5XBtN1ESuMuz2BISYSTlQF%2BDTJ3XIa2Cwq5jsr7pdZKrja9IiTeQSlXcrFtn3wCta7MJHKh70GOqUBKIcXX605kjKyj56QlNp2rl6O9bkGySufs1Vd07O3Ri8gAqeJt9tIN8XPLJkj%2BabHeKuAamqdotRJG6RT8jWZzV8GMhVpzbhJAlJhBGedaMGJn2FDXcaxChvxpYz9jbpxHrwxjvrsIirMIsqDjWe1vKJVz5OgA4CclNXLfrHLCOo14%2FB3bmBEiwlbQPoEtQeGhPbSB3JmLdw0eGt3OZQ19qKxnUXO&X-Amz-Signature=f2b7d23a998f04de62450949e73fa90753a1531fd37893a6efe7871feca5d3e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZBIOC7C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD0HDQcuI9BsLbDyPY%2FvZ3%2BAdPJMJw7QCFUi8xqDciDugIgDTCdeyvk5rr8s%2F7N8FvYXzjCDQdOT43TRZEyjg9EYYgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLlXfKDfkIbGFW5FySrcA%2Fm9KhL1ToDWj5z5r6CLfhhvAh2SXKvoZ8qy69D603VTI2Fg%2BHJLfh%2BnAtrQDamuW%2FChGtJoJmvbGJk3RsyfLb%2BFzO6ryEkM4C3rMvgAKcdM7cml2%2FLqjTS3IaRsjKVi3tOqNhjGqBubVQjqiQF5P9uY7WNO0o01dZZ82IR1fSa%2Bw%2BS4tkwIi5JxNr8w0xb3juPMixkauG1HIrSw2%2Fmob7RrSvoAhs81BlN4HXgWfuaMCfDki76VaVZNsF92lQ%2Bkozq80VVxq6kJGQOOimyC%2FQxCXBXnQhHd4KaOcHmUTY%2Bnm2BtzknsVEmKTiJO9Gjb%2BC5Q5jYhZeTICujMB%2Band38I5JP%2FxBotjDSondJ1KRG0oouTOohowLA3q8hHMFvGmf%2B6xudmV%2B7m%2BTe7fH5JE8jLSNgE1pfHpdpUlcD4MFT5Aayhkd7sI4ZDHQmc3PV5BPInQ%2Bobl%2FBi2jG7XElrw8VTP1946FlygbFjAqh551nwu6uNlTUqkyjP7JpGsFbBRB%2Bk4xhixVIpNQFXww5nqD%2FAskAbId5WhrzBYgbItjyNGqJ0vsKeMvmfYl5XBtN1ESuMuz2BISYSTlQF%2BDTJ3XIa2Cwq5jsr7pdZKrja9IiTeQSlXcrFtn3wCta7MJHKh70GOqUBKIcXX605kjKyj56QlNp2rl6O9bkGySufs1Vd07O3Ri8gAqeJt9tIN8XPLJkj%2BabHeKuAamqdotRJG6RT8jWZzV8GMhVpzbhJAlJhBGedaMGJn2FDXcaxChvxpYz9jbpxHrwxjvrsIirMIsqDjWe1vKJVz5OgA4CclNXLfrHLCOo14%2FB3bmBEiwlbQPoEtQeGhPbSB3JmLdw0eGt3OZQ19qKxnUXO&X-Amz-Signature=b26e073b06c8d37d05ecb870f7f748a2ddacff354a04c27420189d9fca0d916e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZBIOC7C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD0HDQcuI9BsLbDyPY%2FvZ3%2BAdPJMJw7QCFUi8xqDciDugIgDTCdeyvk5rr8s%2F7N8FvYXzjCDQdOT43TRZEyjg9EYYgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLlXfKDfkIbGFW5FySrcA%2Fm9KhL1ToDWj5z5r6CLfhhvAh2SXKvoZ8qy69D603VTI2Fg%2BHJLfh%2BnAtrQDamuW%2FChGtJoJmvbGJk3RsyfLb%2BFzO6ryEkM4C3rMvgAKcdM7cml2%2FLqjTS3IaRsjKVi3tOqNhjGqBubVQjqiQF5P9uY7WNO0o01dZZ82IR1fSa%2Bw%2BS4tkwIi5JxNr8w0xb3juPMixkauG1HIrSw2%2Fmob7RrSvoAhs81BlN4HXgWfuaMCfDki76VaVZNsF92lQ%2Bkozq80VVxq6kJGQOOimyC%2FQxCXBXnQhHd4KaOcHmUTY%2Bnm2BtzknsVEmKTiJO9Gjb%2BC5Q5jYhZeTICujMB%2Band38I5JP%2FxBotjDSondJ1KRG0oouTOohowLA3q8hHMFvGmf%2B6xudmV%2B7m%2BTe7fH5JE8jLSNgE1pfHpdpUlcD4MFT5Aayhkd7sI4ZDHQmc3PV5BPInQ%2Bobl%2FBi2jG7XElrw8VTP1946FlygbFjAqh551nwu6uNlTUqkyjP7JpGsFbBRB%2Bk4xhixVIpNQFXww5nqD%2FAskAbId5WhrzBYgbItjyNGqJ0vsKeMvmfYl5XBtN1ESuMuz2BISYSTlQF%2BDTJ3XIa2Cwq5jsr7pdZKrja9IiTeQSlXcrFtn3wCta7MJHKh70GOqUBKIcXX605kjKyj56QlNp2rl6O9bkGySufs1Vd07O3Ri8gAqeJt9tIN8XPLJkj%2BabHeKuAamqdotRJG6RT8jWZzV8GMhVpzbhJAlJhBGedaMGJn2FDXcaxChvxpYz9jbpxHrwxjvrsIirMIsqDjWe1vKJVz5OgA4CclNXLfrHLCOo14%2FB3bmBEiwlbQPoEtQeGhPbSB3JmLdw0eGt3OZQ19qKxnUXO&X-Amz-Signature=9944c77c29a90d2ffb1a66ee874b81f5cf27a0682664b6f2fdad437f231bc85a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZBIOC7C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD0HDQcuI9BsLbDyPY%2FvZ3%2BAdPJMJw7QCFUi8xqDciDugIgDTCdeyvk5rr8s%2F7N8FvYXzjCDQdOT43TRZEyjg9EYYgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLlXfKDfkIbGFW5FySrcA%2Fm9KhL1ToDWj5z5r6CLfhhvAh2SXKvoZ8qy69D603VTI2Fg%2BHJLfh%2BnAtrQDamuW%2FChGtJoJmvbGJk3RsyfLb%2BFzO6ryEkM4C3rMvgAKcdM7cml2%2FLqjTS3IaRsjKVi3tOqNhjGqBubVQjqiQF5P9uY7WNO0o01dZZ82IR1fSa%2Bw%2BS4tkwIi5JxNr8w0xb3juPMixkauG1HIrSw2%2Fmob7RrSvoAhs81BlN4HXgWfuaMCfDki76VaVZNsF92lQ%2Bkozq80VVxq6kJGQOOimyC%2FQxCXBXnQhHd4KaOcHmUTY%2Bnm2BtzknsVEmKTiJO9Gjb%2BC5Q5jYhZeTICujMB%2Band38I5JP%2FxBotjDSondJ1KRG0oouTOohowLA3q8hHMFvGmf%2B6xudmV%2B7m%2BTe7fH5JE8jLSNgE1pfHpdpUlcD4MFT5Aayhkd7sI4ZDHQmc3PV5BPInQ%2Bobl%2FBi2jG7XElrw8VTP1946FlygbFjAqh551nwu6uNlTUqkyjP7JpGsFbBRB%2Bk4xhixVIpNQFXww5nqD%2FAskAbId5WhrzBYgbItjyNGqJ0vsKeMvmfYl5XBtN1ESuMuz2BISYSTlQF%2BDTJ3XIa2Cwq5jsr7pdZKrja9IiTeQSlXcrFtn3wCta7MJHKh70GOqUBKIcXX605kjKyj56QlNp2rl6O9bkGySufs1Vd07O3Ri8gAqeJt9tIN8XPLJkj%2BabHeKuAamqdotRJG6RT8jWZzV8GMhVpzbhJAlJhBGedaMGJn2FDXcaxChvxpYz9jbpxHrwxjvrsIirMIsqDjWe1vKJVz5OgA4CclNXLfrHLCOo14%2FB3bmBEiwlbQPoEtQeGhPbSB3JmLdw0eGt3OZQ19qKxnUXO&X-Amz-Signature=e882637299432b408c0ab86b7726b56fb23d10753b6dc9a1e3675e723fa6c2c3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W3I7TPS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIB4nSWS6F47qnWwSLsxud5rFZJjosLkwQIYXzqYK2UJiAiEAgko4V2CquUrTm5me82U49jqtDYf3rrDARKqfN7Tto94q%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDG%2Buunq7H9%2FiQcNboSrcA74SJgd1FUx%2BxCa0JHU6nkiNjXO7OPpEN6FGCtMJwaE413uDUPQi%2FPSaIUlAN87fWxYfzQAfVqNYD7igwGcvqYzPELOyoZpEm0muO7gTi6H%2FOnqkB2rqZmJCNJTYunBComBwvMoc3tfMNOveOQvW5j2Le0ZaLhv41Jbpl2kuAHgLwUwdqKYyK9p1rr0775MgVSO4NqZN3HGrokT0YpnuxY7pVaXfW87DT7kYGuKUO1S2hEAX3aKylnpTEDB4oAoNR7NKFvqi5zC%2BqzYVzN2gRSb4n85wGw%2FMW9ztNmcSOp3veoOEjOhQB2tdm5ZMBxSgVGxzPJmgpgfO9YmY43Uu8HYkcUQe5omx12sl6PgaSSEHO2wUiLN2QJQk%2FImXPLW5uMkbJQbp1cvWnJjWcz3WYs4qPKxNV9RGIgzGLLOThvYZFEqMvT5FVhPUSIN%2BKBASj9d7QMlKo%2BqwQp%2FjoMnB0V0aHrqCQCkioLfCO4sEz1I1b%2FtujzOpadrpDQ80dxHZF3B2DcLITgvE9YmJP6uXVVg411P%2BI2kkFpHKwhBcxBnrr6%2BdSEdIf8mqSwYo6Z1lJdIb87uuOv6RT3%2BI1FNHxJ3dNOvVgcKt6uQ3EtvhLE4O8DBP8GwYZWLisXzSMNzKh70GOqUBaxD0tnJ%2B2PRZy4vSQb9u%2BTQ6EhVAVo%2BPH3X7%2FU3HGEL%2By3CDk35r%2FmKMb9WYhFbcra4V2ahGUXt0BZ9LvXpl%2Bu6H59m%2B2HDF7joWGK9ttWTSrg9bDIEJrDY3xU1JnKX9dfLnyqB%2FWsIMlYskm7vDu1MYK0DL8MYQk0SSHCoDeQQOYMgEv2zR88zXHDh91OnSqzyTZ3EN2gLMA%2FJQ0f42cTMtHub%2B&X-Amz-Signature=955722acac0b392e16218dcfe98397fdc07e362afb8393596e1a4f76fabb31a3&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655TWPC5X%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHMAcKpqri1YfXUUMuyOD%2BHGtc2Y%2FtTCeW3bvlO%2FWcOXAiB4BkLPtaEfkdc8DhNyRUvRu%2FLqHfB8iMrprqsan1dZ3ir%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMpOry79x9DBLUoQz8KtwDOpdljq2dZMdHOVdGpagL%2FRFJjuMyHJHAPpm8Vu7EFN30Rca6GFW1rO8dhYSoipFg7O2kZnwrs3nEDP71btkmWQl0yhA9w9rEQ6ul9PdE83jwpl1TocCBCAIZ0NqrFY2%2BPF1zZFfq5FxNFE8hLOiCjTOFeQLYwXrzxBGT7Gpxg6U7%2BiVHMfM%2BGnMR225TqDSJT7IhQKaPkmH00%2BlPQljRq4YXNGwBedk7zXKioVCaSzd3bczuvee7MXbhqxD9qPTB44QWELqrURwgQhrF3wE46SlKMPaEbNSuhlsPR%2BolPkUr96txLdg1ru%2BcEyNpTRJJ2jIPvm7Qq7v7eoM3tEFONVMgr3a57LbHjgQIC7bSGihTyr0c0aK3M2fg0NDeHK5%2BzElM5wjbbQx84JC%2FxDIfD%2FAdW7kwBlGixSexsSK140%2FUtoRN3D%2BgHqTIxelgPUElpo6qwhBb%2FaJ1KqinKAEYFyZCcQHjZIl9fq3oAaLuBhvbAy81b%2BzA1kBaP0y5rbSqskhafdlGd69rE%2Fu8s6AgO5HtZQwH77asEIvzOQhE1mtqhoaCD0oH8Qq4eKlkVgdGEZj4Yw8iDtaCIYaMqo88n4Cc8LMzRWvQt5fN1%2BzkaRlxiQmiRsSMCmfuQwMwzcqHvQY6pgH02og%2F0w7kK59EzIGZwzl4jc8rXMuxi1zeg%2BKQ9V4jWW37eGgN2%2F0CEQjeZirq5GHI0yDoncTbnzCwF1siT2Yuy45WTiZVFcY1r%2F8ZHNLUCsivJ7%2FiOtzGvofKH39%2Fnx%2Bk2ubVsrBe87dOQQETPBmLOSehRbhOSq7Jab5%2BuyNEnoUVCR5DQx9ff0JjaBv4RD5AlCfbCpDtK%2FQWYS2rbF4q%2F0%2Bbis6T&X-Amz-Signature=0fe296ef74d7ca5e3d958a84c9522954ce1a1114305db3e11343905e28c7e1ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZBIOC7C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD0HDQcuI9BsLbDyPY%2FvZ3%2BAdPJMJw7QCFUi8xqDciDugIgDTCdeyvk5rr8s%2F7N8FvYXzjCDQdOT43TRZEyjg9EYYgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLlXfKDfkIbGFW5FySrcA%2Fm9KhL1ToDWj5z5r6CLfhhvAh2SXKvoZ8qy69D603VTI2Fg%2BHJLfh%2BnAtrQDamuW%2FChGtJoJmvbGJk3RsyfLb%2BFzO6ryEkM4C3rMvgAKcdM7cml2%2FLqjTS3IaRsjKVi3tOqNhjGqBubVQjqiQF5P9uY7WNO0o01dZZ82IR1fSa%2Bw%2BS4tkwIi5JxNr8w0xb3juPMixkauG1HIrSw2%2Fmob7RrSvoAhs81BlN4HXgWfuaMCfDki76VaVZNsF92lQ%2Bkozq80VVxq6kJGQOOimyC%2FQxCXBXnQhHd4KaOcHmUTY%2Bnm2BtzknsVEmKTiJO9Gjb%2BC5Q5jYhZeTICujMB%2Band38I5JP%2FxBotjDSondJ1KRG0oouTOohowLA3q8hHMFvGmf%2B6xudmV%2B7m%2BTe7fH5JE8jLSNgE1pfHpdpUlcD4MFT5Aayhkd7sI4ZDHQmc3PV5BPInQ%2Bobl%2FBi2jG7XElrw8VTP1946FlygbFjAqh551nwu6uNlTUqkyjP7JpGsFbBRB%2Bk4xhixVIpNQFXww5nqD%2FAskAbId5WhrzBYgbItjyNGqJ0vsKeMvmfYl5XBtN1ESuMuz2BISYSTlQF%2BDTJ3XIa2Cwq5jsr7pdZKrja9IiTeQSlXcrFtn3wCta7MJHKh70GOqUBKIcXX605kjKyj56QlNp2rl6O9bkGySufs1Vd07O3Ri8gAqeJt9tIN8XPLJkj%2BabHeKuAamqdotRJG6RT8jWZzV8GMhVpzbhJAlJhBGedaMGJn2FDXcaxChvxpYz9jbpxHrwxjvrsIirMIsqDjWe1vKJVz5OgA4CclNXLfrHLCOo14%2FB3bmBEiwlbQPoEtQeGhPbSB3JmLdw0eGt3OZQ19qKxnUXO&X-Amz-Signature=7a06318867295c4fb379aab6ecb2122239a5807f1f5f3a0bb491c60e66acfce5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZBIOC7C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD0HDQcuI9BsLbDyPY%2FvZ3%2BAdPJMJw7QCFUi8xqDciDugIgDTCdeyvk5rr8s%2F7N8FvYXzjCDQdOT43TRZEyjg9EYYgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLlXfKDfkIbGFW5FySrcA%2Fm9KhL1ToDWj5z5r6CLfhhvAh2SXKvoZ8qy69D603VTI2Fg%2BHJLfh%2BnAtrQDamuW%2FChGtJoJmvbGJk3RsyfLb%2BFzO6ryEkM4C3rMvgAKcdM7cml2%2FLqjTS3IaRsjKVi3tOqNhjGqBubVQjqiQF5P9uY7WNO0o01dZZ82IR1fSa%2Bw%2BS4tkwIi5JxNr8w0xb3juPMixkauG1HIrSw2%2Fmob7RrSvoAhs81BlN4HXgWfuaMCfDki76VaVZNsF92lQ%2Bkozq80VVxq6kJGQOOimyC%2FQxCXBXnQhHd4KaOcHmUTY%2Bnm2BtzknsVEmKTiJO9Gjb%2BC5Q5jYhZeTICujMB%2Band38I5JP%2FxBotjDSondJ1KRG0oouTOohowLA3q8hHMFvGmf%2B6xudmV%2B7m%2BTe7fH5JE8jLSNgE1pfHpdpUlcD4MFT5Aayhkd7sI4ZDHQmc3PV5BPInQ%2Bobl%2FBi2jG7XElrw8VTP1946FlygbFjAqh551nwu6uNlTUqkyjP7JpGsFbBRB%2Bk4xhixVIpNQFXww5nqD%2FAskAbId5WhrzBYgbItjyNGqJ0vsKeMvmfYl5XBtN1ESuMuz2BISYSTlQF%2BDTJ3XIa2Cwq5jsr7pdZKrja9IiTeQSlXcrFtn3wCta7MJHKh70GOqUBKIcXX605kjKyj56QlNp2rl6O9bkGySufs1Vd07O3Ri8gAqeJt9tIN8XPLJkj%2BabHeKuAamqdotRJG6RT8jWZzV8GMhVpzbhJAlJhBGedaMGJn2FDXcaxChvxpYz9jbpxHrwxjvrsIirMIsqDjWe1vKJVz5OgA4CclNXLfrHLCOo14%2FB3bmBEiwlbQPoEtQeGhPbSB3JmLdw0eGt3OZQ19qKxnUXO&X-Amz-Signature=86a3515c592932f8a14a6a777a1c691c12ff39f75aa41a19b123d71863ad9250&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZBIOC7C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD0HDQcuI9BsLbDyPY%2FvZ3%2BAdPJMJw7QCFUi8xqDciDugIgDTCdeyvk5rr8s%2F7N8FvYXzjCDQdOT43TRZEyjg9EYYgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLlXfKDfkIbGFW5FySrcA%2Fm9KhL1ToDWj5z5r6CLfhhvAh2SXKvoZ8qy69D603VTI2Fg%2BHJLfh%2BnAtrQDamuW%2FChGtJoJmvbGJk3RsyfLb%2BFzO6ryEkM4C3rMvgAKcdM7cml2%2FLqjTS3IaRsjKVi3tOqNhjGqBubVQjqiQF5P9uY7WNO0o01dZZ82IR1fSa%2Bw%2BS4tkwIi5JxNr8w0xb3juPMixkauG1HIrSw2%2Fmob7RrSvoAhs81BlN4HXgWfuaMCfDki76VaVZNsF92lQ%2Bkozq80VVxq6kJGQOOimyC%2FQxCXBXnQhHd4KaOcHmUTY%2Bnm2BtzknsVEmKTiJO9Gjb%2BC5Q5jYhZeTICujMB%2Band38I5JP%2FxBotjDSondJ1KRG0oouTOohowLA3q8hHMFvGmf%2B6xudmV%2B7m%2BTe7fH5JE8jLSNgE1pfHpdpUlcD4MFT5Aayhkd7sI4ZDHQmc3PV5BPInQ%2Bobl%2FBi2jG7XElrw8VTP1946FlygbFjAqh551nwu6uNlTUqkyjP7JpGsFbBRB%2Bk4xhixVIpNQFXww5nqD%2FAskAbId5WhrzBYgbItjyNGqJ0vsKeMvmfYl5XBtN1ESuMuz2BISYSTlQF%2BDTJ3XIa2Cwq5jsr7pdZKrja9IiTeQSlXcrFtn3wCta7MJHKh70GOqUBKIcXX605kjKyj56QlNp2rl6O9bkGySufs1Vd07O3Ri8gAqeJt9tIN8XPLJkj%2BabHeKuAamqdotRJG6RT8jWZzV8GMhVpzbhJAlJhBGedaMGJn2FDXcaxChvxpYz9jbpxHrwxjvrsIirMIsqDjWe1vKJVz5OgA4CclNXLfrHLCOo14%2FB3bmBEiwlbQPoEtQeGhPbSB3JmLdw0eGt3OZQ19qKxnUXO&X-Amz-Signature=6d34b30649cfd51014eb9b0d522c15ef4178e0cfc8aa76802aa681eb900d2e29&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H442ZVC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDt3fQJldhKbprRiNBkZrZKy3NL3%2BNKw5dS%2BiolM4KMEAIgAcZvFZA9YqWK0Dj%2FZyT3igVbk22HhzHoT3EqHLfSBLoq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDMftCDWCd0ZCK2ig9SrcA2XzNttcRme4qDb2fl%2BD7eGD%2FrHAT7T5q2JTONtaV3lwvFtUZE3%2BD53rpFO%2Fe6qve7RMZJfLjMn3Sl66F4XNqc76ixr8ZYhbLJtq7BlrDTZPlu0q7J4e0ePhshNo%2BRsBc7jMBb2S5h8mfHtbZqOuDa9FlZKI9QfcQLwpzLku4k9fIFp36Farm6EZjTB8HvCkoMdtHjJn5ivPOz6YbhL9WxVzMqujHhBVU8EWbfdg9cF5YumZjirAGoTpVIiiQPNBBxqh%2BWoaykm56VltoXyo19z8YfRvz63759w%2FxO32q6chICdUP%2FBDguYODUBcWe1OHXXWicWHlegNANfFY8te2x%2Fp5Eex2BxII%2BYWglYJeithi1smxBHgAwVpcz2YIKienTE84j0FfYR6YzqyKL5dRv%2Fqh15nPggBYpEJLDSD1wSazDhS1eIuAa%2Bh8VjqEe1pnOCP5FHY3XNC2sTdM9GTJhZmtsloKbdW0vcGTvWrYMS5Aj4ydwdFYoHJX2zfoHkUVtjS2sxfIVxsU0Wis83vbA4rZTfLn3g88r%2BdknSDRzScRt0UsWxQqslbd8%2FyEU41M1q8j3J7cXyFcwF4Ml8TSj%2BfGQ%2BiQSdCaWIP1RGt4UU1XtKZ%2FELaoWzMSvYkMI3Kh70GOqUBTvePb3snIZ70U%2BEYqxZlsK5YcDgNVAHiN1yE%2BAz%2FHQ9MWH6c6r1g8uO7SICRdikVLYgT3%2BfP%2FTNmaHp0Ef1oA3kCwEPCKLFNioEO%2BcYOOfADGYk34Q1drJAev2mF3JGC7SNFbkeQPNMnvCYBobTvrZfZtMg2adkn6hax9m20aonMBpojN349U1xpUhMQnygVphy1o4fJHgRD1g9wdvIv92JSSWgo&X-Amz-Signature=2ec717e814b8c75fe3cd94e74882f11f5a946ffc394b62382847f0056d674bad&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNZ2GRCZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCICtLvL8GDmVfvv6alkcSAR2js%2B8Hssdp4BhRdYMm1py0AiEA1gZDzvZWObcWtiT%2F2rvJFGO8RHWkabp39kZR0G3ryLwq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDPcNMg8qBZn0WejMsyrcAwmzT3Zca0KclKx6A5TzU30SpMCyiLs9kfp%2FyiL%2Bf7ufM7dco8E1J21ml3aTf0HZUJZLO2y%2FbJfVsj0BRFZ60gNPgRdob5rSQi82%2Bs9LvqrS3EkLEMkYpTi0bp%2FPw6dYsIjkuELg8sTZHfD6LysW0vHLYbIvUY0vJE7vUvyt3mbkLR5oDEH2hLYSMddL0p4PuziPQC63ByzGDB%2BKWhMo%2FsGuHhK%2FSuiQdbrFd%2FuGIig9pochSqzXD0Fv7bU5nWUHimv5iydpByVusKrZsFOAPRMTu7NC6Gw8%2FZIrUZj8%2BwrKiZRginTkzciBHvw%2BxsHXT8pGJ2roo8OXPU%2BthMiLIjEe84WHvG5uB7lO0sshrmTMDQeP5MA9wu89ORGbK%2Ffe6nz2FarhwtDaHcamul2RmmgeatCo6sMrqJNqd9a%2F3CxX34IfrogSXegbkeZ3XaLTquXditO%2BclpV3WN1WSsBujaImWmFkvr0WpVYJu6VAp%2B9%2FkXD%2FlH1e%2Bdz0WkwwIrKszZqkZ%2FVJYxPDsbfPacAAAS1Aj3t5D%2BfPhMmoc3PWnbbgIh6Oyb%2Bf%2Bev8m42n9em1RxI9ZgzsHoUFTBqcrxDlt8Mcp74ux99m9wb%2BJPqrWGygH5Yjo9aZtemeBrZMIHLh70GOqUBuh1FRkP4AuH9ca61Op1fV08IOx9YuaYciyRQ3pvhP7nKW390DSYUzaVAKSmNpH7V7wJJnEMdjQlwBh%2BcW9v0q5JLdqRuBdofqRqXBzyIibvWMf09hExZvvF4Ywwi%2BYLmM8JjC9PJr1%2FOQ6h2NdUK%2BpcjcTn28ryClQayDsxYY7e0YMnmBYACxUm5Zym2MuqtGiHiesunqBtdFA5thHMyhoxw7Hhc&X-Amz-Signature=5a0d764202ab7648e28fa5e7afeb1f7ed3d684308a24e317047af8611207ac5d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJXIEOC5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDo7btREtU7A7HLCyEG4%2FPVtRp3u8qTbSQ1BU5b7RSzMQIhAKXPI9l7KTJ54LJ4xAM%2BKAjqWajRNOEHzaNRgYv2go3WKv8DCCsQABoMNjM3NDIzMTgzODA1Igy%2BcGOyoI5cyI9H%2FoEq3AOK80I6QW695o27%2B0%2BOq0HHxwLW2oULtG9q%2FZvklXHpy2hj2YJ6MMZmZGSariYMUjBd8vdmM9VAxMSUUsaYmWJRE7d5xWywTFUTCTDG6m8bYZh%2FRjJgXOleww1DkEFMc3dcpYl1Rb%2BrbjL2LZAy1orXWIhc3sO5JOQ2eYeVooUqE%2Fq%2B7ulFeKMQ%2BsCYtYtr8we5Khtau0mrjwkHmkqidHo8fVPmrKBU%2Bm%2BHUdxPc%2BaTMgFASTWH96J23IQLFXjZhwUIg70ozJ76GearWr%2FNOofsonh3oeTL5OXo%2BJcuYV5LMuH0UyMiMfr6DP4KJO8of0RKz%2FB4Nez6IBjLD95Pa8H66I1TScjY7GB6mk%2Fqk0VUw99ngt6Sg8EtPB3Zw4aQuBgaGCvaLzgFDDTWkg3p9DQs16aa6nyvhxOVeze5%2FG3tJE%2FfsRTYUPjRI%2BuGrfIR%2BPFL8KKNhji4kJprVU%2FJco1jI6YRI7pXRVK2cY16%2FccA3qHP%2F24GimEwFjD%2FaTTHxTweC9jLsnjZ7MxhiewYiji4KXZoIXZxqlzfB%2FyE4Z%2Fd3FffL%2B%2BYFw9weuW1TNDyIpF0Ot2Btll7JMEIuoJUQ2N7Gjy1J%2BnNXt0cNs%2BuYBxgNKQ6SZmM%2B%2BOnrgCF6zDlyoe9BjqkAdUsR51mWeUOBtfjA4NTQs3d6ZbAOAJ9z0KGAXeLpMBZi36N2KESrfYjNZirm0P7EZM09uIrEcxieg329g%2BYveFhJfRfgmBS9NqGs9xiwcwWm4JWsz6XJQqCkbIXuqc36%2B%2Bz%2FjLIY1zMbefqIOjzlF7L1thvG1t0nhH9CDJX9m8gWPq1Vi8RBNXiwUkLiIxjse%2BPZ466trZWrW7C0ZN8P5NouOhq&X-Amz-Signature=b1ca706a7a22103102bbabc5ae0aabc0df63fa654b4e9a4053264f5d416d8009&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4APH6KJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIErHrpPkdjRm9dwzb0zGQYgk%2FRP%2F0TlDjwORX0xl3uVkAiBtkDKiXnZ2NsX0ve1MjqvDWhOAar3EEXa57D02513bWyr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIME5lmv3wk5AaAtU57KtwDi9EN4rfs20EpLWOfooJwEOU3F352HMm6HjjjDuO0G6DVh6ea90EeNTuIHypfHTF%2FncymWel449NAV9%2BWPclGhiJ9xoWTPnEUoA%2BMLAAGwEUJn1RgF4yDMf%2BtK%2BLcIbp0vIGJB%2FBOlgIWYRwMVJar7f8Qecp8Jyi8VkkjQRz3ja%2BVebiv8jq5d4feVg4hCc2he619DAKrrL3nZib0hjhXnpA6g%2F4X4FLrFH%2BfuBJVVoAKI5FNPe9VGcAYWcit035ikE99mbSuX9mhoYNizRwyXtYdDBXbkKfDsBCo6xpNL5d%2Bnq%2BA5lBvgRRKwO%2BlkeeQ2gil1I7iYVJR2wYQwHjm%2FdgPK7mwrv8dl2muBUt9BRKqAXrLXcE5XavaN6vlGFFnXZ%2BNuCdY0BX6aMFDhVYEu3uPRXJm9V68Ffi66CqjtHCdiX0MQbZXeg32w3uLwA2x%2FYAx12hcLYGig4zGUWjnQuEeV1bEy%2B2xW7VDB7248Y90H0nQNt%2FSebEBH2upFAw8Ws3IsvGk2x7W%2FSYKWRLl0CJevz%2BxbeW5lfs3sSVTCSvyOWYYckqvweiHFyb3GmGCX6qbuW4l3Ork3864Nqxr23hhFlI6j14IilTcS7GxTd%2FakTZIkhRBsyHPIGgwusqHvQY6pgGBsJ1bB0LiN9nJ%2F57k1hEEQRuhMlsEwMrEza9HyIaeq9AwuK%2BIwxp%2BOexd%2Fb5pY4UsB4AIEu0K6JWbc3PqymDunl%2BugsBYN3mSYCX%2BuJow6INQjYyVW5NQdUa2fDYMmFYc5zhQ1KaokPmAh6%2Fj41Hvg5r65WHbNxavaHGrEawsS0aTNPbAyyqKkjYyYnPHVCH8p0Y105Hj1LCXZxUeIgT1XQnEseDq&X-Amz-Signature=f4e9e9a56f097aff6600c76467294b7cacdf15da4f6489b8dbd8dd9cbf4681f5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4APH6KJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIErHrpPkdjRm9dwzb0zGQYgk%2FRP%2F0TlDjwORX0xl3uVkAiBtkDKiXnZ2NsX0ve1MjqvDWhOAar3EEXa57D02513bWyr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIME5lmv3wk5AaAtU57KtwDi9EN4rfs20EpLWOfooJwEOU3F352HMm6HjjjDuO0G6DVh6ea90EeNTuIHypfHTF%2FncymWel449NAV9%2BWPclGhiJ9xoWTPnEUoA%2BMLAAGwEUJn1RgF4yDMf%2BtK%2BLcIbp0vIGJB%2FBOlgIWYRwMVJar7f8Qecp8Jyi8VkkjQRz3ja%2BVebiv8jq5d4feVg4hCc2he619DAKrrL3nZib0hjhXnpA6g%2F4X4FLrFH%2BfuBJVVoAKI5FNPe9VGcAYWcit035ikE99mbSuX9mhoYNizRwyXtYdDBXbkKfDsBCo6xpNL5d%2Bnq%2BA5lBvgRRKwO%2BlkeeQ2gil1I7iYVJR2wYQwHjm%2FdgPK7mwrv8dl2muBUt9BRKqAXrLXcE5XavaN6vlGFFnXZ%2BNuCdY0BX6aMFDhVYEu3uPRXJm9V68Ffi66CqjtHCdiX0MQbZXeg32w3uLwA2x%2FYAx12hcLYGig4zGUWjnQuEeV1bEy%2B2xW7VDB7248Y90H0nQNt%2FSebEBH2upFAw8Ws3IsvGk2x7W%2FSYKWRLl0CJevz%2BxbeW5lfs3sSVTCSvyOWYYckqvweiHFyb3GmGCX6qbuW4l3Ork3864Nqxr23hhFlI6j14IilTcS7GxTd%2FakTZIkhRBsyHPIGgwusqHvQY6pgGBsJ1bB0LiN9nJ%2F57k1hEEQRuhMlsEwMrEza9HyIaeq9AwuK%2BIwxp%2BOexd%2Fb5pY4UsB4AIEu0K6JWbc3PqymDunl%2BugsBYN3mSYCX%2BuJow6INQjYyVW5NQdUa2fDYMmFYc5zhQ1KaokPmAh6%2Fj41Hvg5r65WHbNxavaHGrEawsS0aTNPbAyyqKkjYyYnPHVCH8p0Y105Hj1LCXZxUeIgT1XQnEseDq&X-Amz-Signature=fb5b0edc1bb29dbe685102aee3da1182ac50ab2c82ac157d4bb8754dd9d60ab7&X-Amz-SignedHeaders=host&x-id=GetObject)

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
