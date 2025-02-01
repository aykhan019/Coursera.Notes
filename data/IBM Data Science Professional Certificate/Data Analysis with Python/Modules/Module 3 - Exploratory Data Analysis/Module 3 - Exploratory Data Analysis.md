

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX2MK5FR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHA7Rb7G9Lau2oOBwVybCNXkXK6LmBZolAcKEGeQ3uugIhAPxERhp3GIgIQH6JPHDcW6R3aCe3jfFZssizBua4WbcEKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FMw4lgjEyNAdI%2Bpsq3ANV2o4NUjx2%2Bkg6OFoco%2BzVjUNebpeonkDDXFZLGwmwYp3h9yOA72y5EiZzjL6%2FepMGTl5AUex8aUof8HqISRZFwrE%2B%2Fw26MECew9g9vwCUHT6OMxM28xr6w6k0fp7xrkwnK5cDDlUrdOOXAG35RWOEdMexjD%2FQipP3GFMEh%2BuewlIDTU3Tr2psGvTZvPFO%2F7FWY0vAtz80fNkvkuvdHyDkZ3VQePfC7utO6kG6Mq5KGcb5Drxl%2B4xIKyWuyGWxzyOVyItCSLAYFp79JFKk9mRG1I2L%2FHoEF1JuIi3bitlvCMLwJJ5DEeuRD9%2F%2BYYqUpm5uU83mW5KQfsdw8F54zXxDlk3L3UpMATp8TkwLIwfrdtaw5FD3pUDTq10TpwqbOiGlfZP6pKuTEmIj%2BfCM5C%2BqLutKAHpXHl%2BAd%2FhNPFdNcT6Pqc2Bt5DbX8HU6IxNzQZsqjXCUILUfnylqpSylNSvvGr2HO%2FKkCRHZ0N8kO71nGVi%2FWIOXmFsJWZ09qm7CtUzyayc8J%2Fx%2Fngv9A2ym3WCf0IR%2BBkPrgWAmsf3rvg4EhpYnuMawOJCbO9Aq8xj1XgxOncpV3FsixC%2BBRYgvkskIcWT9flZp3VxvH1THoDqXnKGmqkQ8x0hy0s7nTDO9vm8BjqkAeArnEUEKWQd7FDji0sfPQqPLe1XgHsly1Q0UDLCWeOUX3tfxk0%2F48uTzJHH9zv571ICIxe3TAW17v1%2FWkWgBj9b79%2BxAYNcYUXXzrMdGhGeqr6Hn3X4PsSBV1BHTiOPrS6eroSJy6CNvg2E%2Fy%2FTK91cKamO2XCSlKx3TNQlviTpKfkG1JnH2jAXnxnOUf1olFkLAMfKaez%2B9sJgTUecXxWpZuJF&X-Amz-Signature=6703d823b5e32085ad72e304fe1f88a7454b72f22ec401c887e12f9afe7b932e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX2MK5FR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHA7Rb7G9Lau2oOBwVybCNXkXK6LmBZolAcKEGeQ3uugIhAPxERhp3GIgIQH6JPHDcW6R3aCe3jfFZssizBua4WbcEKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FMw4lgjEyNAdI%2Bpsq3ANV2o4NUjx2%2Bkg6OFoco%2BzVjUNebpeonkDDXFZLGwmwYp3h9yOA72y5EiZzjL6%2FepMGTl5AUex8aUof8HqISRZFwrE%2B%2Fw26MECew9g9vwCUHT6OMxM28xr6w6k0fp7xrkwnK5cDDlUrdOOXAG35RWOEdMexjD%2FQipP3GFMEh%2BuewlIDTU3Tr2psGvTZvPFO%2F7FWY0vAtz80fNkvkuvdHyDkZ3VQePfC7utO6kG6Mq5KGcb5Drxl%2B4xIKyWuyGWxzyOVyItCSLAYFp79JFKk9mRG1I2L%2FHoEF1JuIi3bitlvCMLwJJ5DEeuRD9%2F%2BYYqUpm5uU83mW5KQfsdw8F54zXxDlk3L3UpMATp8TkwLIwfrdtaw5FD3pUDTq10TpwqbOiGlfZP6pKuTEmIj%2BfCM5C%2BqLutKAHpXHl%2BAd%2FhNPFdNcT6Pqc2Bt5DbX8HU6IxNzQZsqjXCUILUfnylqpSylNSvvGr2HO%2FKkCRHZ0N8kO71nGVi%2FWIOXmFsJWZ09qm7CtUzyayc8J%2Fx%2Fngv9A2ym3WCf0IR%2BBkPrgWAmsf3rvg4EhpYnuMawOJCbO9Aq8xj1XgxOncpV3FsixC%2BBRYgvkskIcWT9flZp3VxvH1THoDqXnKGmqkQ8x0hy0s7nTDO9vm8BjqkAeArnEUEKWQd7FDji0sfPQqPLe1XgHsly1Q0UDLCWeOUX3tfxk0%2F48uTzJHH9zv571ICIxe3TAW17v1%2FWkWgBj9b79%2BxAYNcYUXXzrMdGhGeqr6Hn3X4PsSBV1BHTiOPrS6eroSJy6CNvg2E%2Fy%2FTK91cKamO2XCSlKx3TNQlviTpKfkG1JnH2jAXnxnOUf1olFkLAMfKaez%2B9sJgTUecXxWpZuJF&X-Amz-Signature=52689a56ac04e1e0aeb7f21e4598749878b507fc0c81e5d0b2cd3a8dc5a7bd7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX2MK5FR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHA7Rb7G9Lau2oOBwVybCNXkXK6LmBZolAcKEGeQ3uugIhAPxERhp3GIgIQH6JPHDcW6R3aCe3jfFZssizBua4WbcEKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FMw4lgjEyNAdI%2Bpsq3ANV2o4NUjx2%2Bkg6OFoco%2BzVjUNebpeonkDDXFZLGwmwYp3h9yOA72y5EiZzjL6%2FepMGTl5AUex8aUof8HqISRZFwrE%2B%2Fw26MECew9g9vwCUHT6OMxM28xr6w6k0fp7xrkwnK5cDDlUrdOOXAG35RWOEdMexjD%2FQipP3GFMEh%2BuewlIDTU3Tr2psGvTZvPFO%2F7FWY0vAtz80fNkvkuvdHyDkZ3VQePfC7utO6kG6Mq5KGcb5Drxl%2B4xIKyWuyGWxzyOVyItCSLAYFp79JFKk9mRG1I2L%2FHoEF1JuIi3bitlvCMLwJJ5DEeuRD9%2F%2BYYqUpm5uU83mW5KQfsdw8F54zXxDlk3L3UpMATp8TkwLIwfrdtaw5FD3pUDTq10TpwqbOiGlfZP6pKuTEmIj%2BfCM5C%2BqLutKAHpXHl%2BAd%2FhNPFdNcT6Pqc2Bt5DbX8HU6IxNzQZsqjXCUILUfnylqpSylNSvvGr2HO%2FKkCRHZ0N8kO71nGVi%2FWIOXmFsJWZ09qm7CtUzyayc8J%2Fx%2Fngv9A2ym3WCf0IR%2BBkPrgWAmsf3rvg4EhpYnuMawOJCbO9Aq8xj1XgxOncpV3FsixC%2BBRYgvkskIcWT9flZp3VxvH1THoDqXnKGmqkQ8x0hy0s7nTDO9vm8BjqkAeArnEUEKWQd7FDji0sfPQqPLe1XgHsly1Q0UDLCWeOUX3tfxk0%2F48uTzJHH9zv571ICIxe3TAW17v1%2FWkWgBj9b79%2BxAYNcYUXXzrMdGhGeqr6Hn3X4PsSBV1BHTiOPrS6eroSJy6CNvg2E%2Fy%2FTK91cKamO2XCSlKx3TNQlviTpKfkG1JnH2jAXnxnOUf1olFkLAMfKaez%2B9sJgTUecXxWpZuJF&X-Amz-Signature=9e0ccb4f31880b70d567d8810c1255aa9c5157071fb7d8d930b7dd589e661206&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SL74XNU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQ7vZjrTmkk3L4Dz%2F%2FvhRK804RHfCZJjAa0XcofTTxogIhAJ3caHC%2BJm5hrqDNa6FK8sn9J%2B%2BrJcG21egUiV4C6t7nKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwljOL6DDC3FUiZ%2BuAq3AP9MN26Ymbw0DIjaegyMk8xNt8ActfSBtwOihrzx7J5GwiQkJAuTCrjgmFYh8oQGP6Q%2FaJt%2B4gWXDXsTuEZLcECDGDYI62dk87tQ%2FrZHaqDAbNlm58Fwzy2Vtnhl6cpeLw%2Fmk0AyXS6JH8fTqZcaavtlgpJDU8ewxQen5yDM0KAJzd0VFp1WLD69QgusDVR%2BYLHo5pC4IV6ZRcFZ8Fg3NbHrVqSnwZRfXWLf9c04ihMhYx5m3eN7vfvRItVG%2BSdcMONHpqOn4JtP5mPztgin%2BFxuueo5BlckoD7vZfjs0jMoL1hNhawdjHzpWJ8IlmYBCVxMerFu00m8RU6igONM4fAHZoke05687xWqreoKcjZdCKhAQ9ZBgOQ8fYJXh8tguE8yxWSuQzr2NW%2BuUdkEa2zzPTdsOxGkLKsUOwcPM8ppJlN8q0CvpyBBgahg8xJidHWe9B7yVXaJ2pu02A2DbX5UdxbY1sK00OKgErjIqAkoKTpS5unNUlcrkx%2FE1XEFJaIHoHEQJYhUCDG%2Buqh7bTQTp9W4HaomySBeUxjYFje8l9F3D4a2zghXaRwVhlG9nBe%2FtGaMT%2BFMwPRlawHxrkAOzGr234V3R0rD629MlUwFjpJubBMfWAgyzozmTCI9%2Fm8BjqkAaXQpkaNohdFBEinDiuJdm5S6KYFDUnbjFhblMve60wokC23ozTUI70hBdiNaTbTwVN6fP4t90TX6wyfB4Kc%2FWwA8ZrZ%2BrnL9ZRZJIYEH6zOMLJfMHVxmY7ftwhPPr9zUwXLlq6%2FnZnL8oC%2B2ifbjxv%2B3lK2tyClStpt7%2Fxw8KMGtpU5eMFcyE3irG1Pr%2Fb5eagLaV3PUxrbsF%2FaaMOw5fqltXmM&X-Amz-Signature=5d6cfa70518099e7dc8e268f5e3417fc461afe10c4ad0c1d5235f2559b05a22b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SL74XNU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQ7vZjrTmkk3L4Dz%2F%2FvhRK804RHfCZJjAa0XcofTTxogIhAJ3caHC%2BJm5hrqDNa6FK8sn9J%2B%2BrJcG21egUiV4C6t7nKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwljOL6DDC3FUiZ%2BuAq3AP9MN26Ymbw0DIjaegyMk8xNt8ActfSBtwOihrzx7J5GwiQkJAuTCrjgmFYh8oQGP6Q%2FaJt%2B4gWXDXsTuEZLcECDGDYI62dk87tQ%2FrZHaqDAbNlm58Fwzy2Vtnhl6cpeLw%2Fmk0AyXS6JH8fTqZcaavtlgpJDU8ewxQen5yDM0KAJzd0VFp1WLD69QgusDVR%2BYLHo5pC4IV6ZRcFZ8Fg3NbHrVqSnwZRfXWLf9c04ihMhYx5m3eN7vfvRItVG%2BSdcMONHpqOn4JtP5mPztgin%2BFxuueo5BlckoD7vZfjs0jMoL1hNhawdjHzpWJ8IlmYBCVxMerFu00m8RU6igONM4fAHZoke05687xWqreoKcjZdCKhAQ9ZBgOQ8fYJXh8tguE8yxWSuQzr2NW%2BuUdkEa2zzPTdsOxGkLKsUOwcPM8ppJlN8q0CvpyBBgahg8xJidHWe9B7yVXaJ2pu02A2DbX5UdxbY1sK00OKgErjIqAkoKTpS5unNUlcrkx%2FE1XEFJaIHoHEQJYhUCDG%2Buqh7bTQTp9W4HaomySBeUxjYFje8l9F3D4a2zghXaRwVhlG9nBe%2FtGaMT%2BFMwPRlawHxrkAOzGr234V3R0rD629MlUwFjpJubBMfWAgyzozmTCI9%2Fm8BjqkAaXQpkaNohdFBEinDiuJdm5S6KYFDUnbjFhblMve60wokC23ozTUI70hBdiNaTbTwVN6fP4t90TX6wyfB4Kc%2FWwA8ZrZ%2BrnL9ZRZJIYEH6zOMLJfMHVxmY7ftwhPPr9zUwXLlq6%2FnZnL8oC%2B2ifbjxv%2B3lK2tyClStpt7%2Fxw8KMGtpU5eMFcyE3irG1Pr%2Fb5eagLaV3PUxrbsF%2FaaMOw5fqltXmM&X-Amz-Signature=35fba6a1e548745559d446b6bb9010d6173e6e29baa9780bd2db08aaedfc9bfc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SL74XNU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQ7vZjrTmkk3L4Dz%2F%2FvhRK804RHfCZJjAa0XcofTTxogIhAJ3caHC%2BJm5hrqDNa6FK8sn9J%2B%2BrJcG21egUiV4C6t7nKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwljOL6DDC3FUiZ%2BuAq3AP9MN26Ymbw0DIjaegyMk8xNt8ActfSBtwOihrzx7J5GwiQkJAuTCrjgmFYh8oQGP6Q%2FaJt%2B4gWXDXsTuEZLcECDGDYI62dk87tQ%2FrZHaqDAbNlm58Fwzy2Vtnhl6cpeLw%2Fmk0AyXS6JH8fTqZcaavtlgpJDU8ewxQen5yDM0KAJzd0VFp1WLD69QgusDVR%2BYLHo5pC4IV6ZRcFZ8Fg3NbHrVqSnwZRfXWLf9c04ihMhYx5m3eN7vfvRItVG%2BSdcMONHpqOn4JtP5mPztgin%2BFxuueo5BlckoD7vZfjs0jMoL1hNhawdjHzpWJ8IlmYBCVxMerFu00m8RU6igONM4fAHZoke05687xWqreoKcjZdCKhAQ9ZBgOQ8fYJXh8tguE8yxWSuQzr2NW%2BuUdkEa2zzPTdsOxGkLKsUOwcPM8ppJlN8q0CvpyBBgahg8xJidHWe9B7yVXaJ2pu02A2DbX5UdxbY1sK00OKgErjIqAkoKTpS5unNUlcrkx%2FE1XEFJaIHoHEQJYhUCDG%2Buqh7bTQTp9W4HaomySBeUxjYFje8l9F3D4a2zghXaRwVhlG9nBe%2FtGaMT%2BFMwPRlawHxrkAOzGr234V3R0rD629MlUwFjpJubBMfWAgyzozmTCI9%2Fm8BjqkAaXQpkaNohdFBEinDiuJdm5S6KYFDUnbjFhblMve60wokC23ozTUI70hBdiNaTbTwVN6fP4t90TX6wyfB4Kc%2FWwA8ZrZ%2BrnL9ZRZJIYEH6zOMLJfMHVxmY7ftwhPPr9zUwXLlq6%2FnZnL8oC%2B2ifbjxv%2B3lK2tyClStpt7%2Fxw8KMGtpU5eMFcyE3irG1Pr%2Fb5eagLaV3PUxrbsF%2FaaMOw5fqltXmM&X-Amz-Signature=05f189dd5169d834dd18821aa5b3cbb7aa98d84edbd44a356d21031de051c77f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SL74XNU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQ7vZjrTmkk3L4Dz%2F%2FvhRK804RHfCZJjAa0XcofTTxogIhAJ3caHC%2BJm5hrqDNa6FK8sn9J%2B%2BrJcG21egUiV4C6t7nKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwljOL6DDC3FUiZ%2BuAq3AP9MN26Ymbw0DIjaegyMk8xNt8ActfSBtwOihrzx7J5GwiQkJAuTCrjgmFYh8oQGP6Q%2FaJt%2B4gWXDXsTuEZLcECDGDYI62dk87tQ%2FrZHaqDAbNlm58Fwzy2Vtnhl6cpeLw%2Fmk0AyXS6JH8fTqZcaavtlgpJDU8ewxQen5yDM0KAJzd0VFp1WLD69QgusDVR%2BYLHo5pC4IV6ZRcFZ8Fg3NbHrVqSnwZRfXWLf9c04ihMhYx5m3eN7vfvRItVG%2BSdcMONHpqOn4JtP5mPztgin%2BFxuueo5BlckoD7vZfjs0jMoL1hNhawdjHzpWJ8IlmYBCVxMerFu00m8RU6igONM4fAHZoke05687xWqreoKcjZdCKhAQ9ZBgOQ8fYJXh8tguE8yxWSuQzr2NW%2BuUdkEa2zzPTdsOxGkLKsUOwcPM8ppJlN8q0CvpyBBgahg8xJidHWe9B7yVXaJ2pu02A2DbX5UdxbY1sK00OKgErjIqAkoKTpS5unNUlcrkx%2FE1XEFJaIHoHEQJYhUCDG%2Buqh7bTQTp9W4HaomySBeUxjYFje8l9F3D4a2zghXaRwVhlG9nBe%2FtGaMT%2BFMwPRlawHxrkAOzGr234V3R0rD629MlUwFjpJubBMfWAgyzozmTCI9%2Fm8BjqkAaXQpkaNohdFBEinDiuJdm5S6KYFDUnbjFhblMve60wokC23ozTUI70hBdiNaTbTwVN6fP4t90TX6wyfB4Kc%2FWwA8ZrZ%2BrnL9ZRZJIYEH6zOMLJfMHVxmY7ftwhPPr9zUwXLlq6%2FnZnL8oC%2B2ifbjxv%2B3lK2tyClStpt7%2Fxw8KMGtpU5eMFcyE3irG1Pr%2Fb5eagLaV3PUxrbsF%2FaaMOw5fqltXmM&X-Amz-Signature=6bd253d4f112e4f63cf36408e0c127493c8d3fa98b06693dbf2a1cbd7b230fb6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SL74XNU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQ7vZjrTmkk3L4Dz%2F%2FvhRK804RHfCZJjAa0XcofTTxogIhAJ3caHC%2BJm5hrqDNa6FK8sn9J%2B%2BrJcG21egUiV4C6t7nKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwljOL6DDC3FUiZ%2BuAq3AP9MN26Ymbw0DIjaegyMk8xNt8ActfSBtwOihrzx7J5GwiQkJAuTCrjgmFYh8oQGP6Q%2FaJt%2B4gWXDXsTuEZLcECDGDYI62dk87tQ%2FrZHaqDAbNlm58Fwzy2Vtnhl6cpeLw%2Fmk0AyXS6JH8fTqZcaavtlgpJDU8ewxQen5yDM0KAJzd0VFp1WLD69QgusDVR%2BYLHo5pC4IV6ZRcFZ8Fg3NbHrVqSnwZRfXWLf9c04ihMhYx5m3eN7vfvRItVG%2BSdcMONHpqOn4JtP5mPztgin%2BFxuueo5BlckoD7vZfjs0jMoL1hNhawdjHzpWJ8IlmYBCVxMerFu00m8RU6igONM4fAHZoke05687xWqreoKcjZdCKhAQ9ZBgOQ8fYJXh8tguE8yxWSuQzr2NW%2BuUdkEa2zzPTdsOxGkLKsUOwcPM8ppJlN8q0CvpyBBgahg8xJidHWe9B7yVXaJ2pu02A2DbX5UdxbY1sK00OKgErjIqAkoKTpS5unNUlcrkx%2FE1XEFJaIHoHEQJYhUCDG%2Buqh7bTQTp9W4HaomySBeUxjYFje8l9F3D4a2zghXaRwVhlG9nBe%2FtGaMT%2BFMwPRlawHxrkAOzGr234V3R0rD629MlUwFjpJubBMfWAgyzozmTCI9%2Fm8BjqkAaXQpkaNohdFBEinDiuJdm5S6KYFDUnbjFhblMve60wokC23ozTUI70hBdiNaTbTwVN6fP4t90TX6wyfB4Kc%2FWwA8ZrZ%2BrnL9ZRZJIYEH6zOMLJfMHVxmY7ftwhPPr9zUwXLlq6%2FnZnL8oC%2B2ifbjxv%2B3lK2tyClStpt7%2Fxw8KMGtpU5eMFcyE3irG1Pr%2Fb5eagLaV3PUxrbsF%2FaaMOw5fqltXmM&X-Amz-Signature=ee8330f5ba3a0ea32bbd197924fec2e5933b23100e99e6d2c88aaf08575d13ba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SL74XNU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQ7vZjrTmkk3L4Dz%2F%2FvhRK804RHfCZJjAa0XcofTTxogIhAJ3caHC%2BJm5hrqDNa6FK8sn9J%2B%2BrJcG21egUiV4C6t7nKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwljOL6DDC3FUiZ%2BuAq3AP9MN26Ymbw0DIjaegyMk8xNt8ActfSBtwOihrzx7J5GwiQkJAuTCrjgmFYh8oQGP6Q%2FaJt%2B4gWXDXsTuEZLcECDGDYI62dk87tQ%2FrZHaqDAbNlm58Fwzy2Vtnhl6cpeLw%2Fmk0AyXS6JH8fTqZcaavtlgpJDU8ewxQen5yDM0KAJzd0VFp1WLD69QgusDVR%2BYLHo5pC4IV6ZRcFZ8Fg3NbHrVqSnwZRfXWLf9c04ihMhYx5m3eN7vfvRItVG%2BSdcMONHpqOn4JtP5mPztgin%2BFxuueo5BlckoD7vZfjs0jMoL1hNhawdjHzpWJ8IlmYBCVxMerFu00m8RU6igONM4fAHZoke05687xWqreoKcjZdCKhAQ9ZBgOQ8fYJXh8tguE8yxWSuQzr2NW%2BuUdkEa2zzPTdsOxGkLKsUOwcPM8ppJlN8q0CvpyBBgahg8xJidHWe9B7yVXaJ2pu02A2DbX5UdxbY1sK00OKgErjIqAkoKTpS5unNUlcrkx%2FE1XEFJaIHoHEQJYhUCDG%2Buqh7bTQTp9W4HaomySBeUxjYFje8l9F3D4a2zghXaRwVhlG9nBe%2FtGaMT%2BFMwPRlawHxrkAOzGr234V3R0rD629MlUwFjpJubBMfWAgyzozmTCI9%2Fm8BjqkAaXQpkaNohdFBEinDiuJdm5S6KYFDUnbjFhblMve60wokC23ozTUI70hBdiNaTbTwVN6fP4t90TX6wyfB4Kc%2FWwA8ZrZ%2BrnL9ZRZJIYEH6zOMLJfMHVxmY7ftwhPPr9zUwXLlq6%2FnZnL8oC%2B2ifbjxv%2B3lK2tyClStpt7%2Fxw8KMGtpU5eMFcyE3irG1Pr%2Fb5eagLaV3PUxrbsF%2FaaMOw5fqltXmM&X-Amz-Signature=9a4854489250a086cbae43479b125b635f804262383816b4884de461bd3ae668&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W67ATQBY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGAOjmCk9sQSxtOb6q%2FCz01QAbB8TdqbAqQ%2BqM2eYL4fAiAMZ41kkHU8zMOXPWvD%2FdJfqv%2FgNjO7Iv%2FWxz%2F7OeIV7CqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWNdLHZGugnXMU%2FXSKtwDBtGal9pkpisckJsJXaO03V7aD5BNjLOPkc0Rb0%2FNJ54RnMiIzdqQ94Dgh%2F2E814HMhyAxH%2BwsIQqPdI9iWhECTY0zGvc8BSlXgW379%2BaIMYptESCGhLTjK7L%2FEZB2ZkgtZh5dSppwYVyBKIqJM3IRq3jY2pJVADDMYPUxwTnUjJ%2Fg%2BG8FpVvjmfnhCDmrEyOkw8QNDg9kjC5ob1xHdUE1vF0qk29%2Beuh2d18ELfJrqL1pc4q%2B1BX8wQq%2BS6EVtn83bHXaxYUrHkoOwk9%2BaOOpemx8rofpgr6SSC8owxaUnXw8KlYwsi%2F4txaQA%2BBnr7t3SqGus9qFqVQ4FIKERIBpOtX1o626YdGxMyXYMejQZlHV0dyjYzMv9Yu7lzByoQgkCtXVUOFx7pRblURrBERGUYeCQXO0vi445s7a1hgAH83UmLK7gq8aQgh2%2FHnaTa4U682DSc7LmdKNag4lrlNe%2FDMZX9pNXgX%2BIRxQyePVtxdA%2Fg1p0emSwMZkxeLLY2T93VepbHVff2rohySowh%2BG56AbiG6SlpNH0Y3uLJCmzABQXvzbKipvzs0NtaMKicosco1HaU%2B9Bo0wg3WiB86Ug4KN%2BQGffuaWCQ3%2FGYwdxOQ7pCrXcUJiMntWtkw4ff5vAY6pgFZsLmPazaRBs2EDLnkLExatB00GchS5RyNiteNFC7qK0kyiImRLWcXJ0JNkKq2m4n6xIjHM3p%2BjnKfGcm2GEtmOiyICkuMfQggxUgExET9I%2FS0vacv854VPXz7pnUfmlb1CE8HGZnPhlBGEHg%2Bt%2BYvbBprMrIQvEIFYNTD6IZ7JTAgVoXfIyNcfkEzdf%2FyWpbBkR8tX4lfhtE50zGz594%2F49bOfnop&X-Amz-Signature=fd4c65718122fcba7094714612f2e7ac5db66184579226c49f6ea7b8d46798ae&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VQRM4TG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICom5Z%2FS18pmW1fKqNrRcxuiPctKLIf7vlP%2FqP98%2FBkjAiBWQ9QRThP2ZXvKI%2Bex%2BWrLNdtTzHjqEpCqoktq9yV4IiqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMa3x7MxKjFTegCN8LKtwDmMUru%2Bak6vrkKq3jPIC%2BUXtZYWZ9MVcNoOYq4U%2B01NpBfeIs2BlBQt3QDYD0qkTbBX%2FGfBsrq2YDi4fvnvCM0eQa1fCViN5rkX4cKlvqRek6zHY1R1YSURaulwIA4m4tvy0N%2BTDefFQDrsHyu3pGWOTjKWRoip4EDtUhpyIjrEhIgR5LVhWjBwrtUfnnrcl8c%2F1dHhiMZzuW%2FJbSB10DtlkB9TXqJZPsmCoj6zrJMCViiPCIneYES7BvQxN8GAfaZOSHF2vndt62xuD2zclvorRz8wWr2KuHz2e6Nh%2B6ihwmILJjVOB7ezFcTzLnhITlmhbt5pNmYF04I2zo6RktS%2FoJ0yh99NDvra6S5dJfFOKXtuhs8AXp4go0cMBc35FBIL3W29d4F%2BFYJ13yMJ0zy5UkXLCorkMyohG8CqS2mpnjENWgp%2F4Cpakp%2FKiaROt69v6tfLjvSm%2Bb2IqF78MHa7gt%2FGrpq%2FF%2FVvDAD8X4uPYJKlwAQjUvaFn2JC%2Bv3fNGv8HT7EUC2HZAznr1sJzsOd6j%2BRKDuuE%2FkQrfQFigkInFUSiHlK0qI7x%2Bwqp1Makz8JmkhANDVzsNZv2Lsz3VHDglDp1Wq8tYOl2syISgl2Wot5UXSUSY%2BSxukxYwo%2Fb5vAY6pgEhWEuf3EUATfScjzkEWXCn2%2FzDcCs8ezPiE7S%2Bw7SH3Uvee5M9fztNT2LI1fl3fuaPqp1YHxcePGBPnVjW91HHry3gq%2Fl5rXLI%2BEATUOa0lLBrgoDjf56bVaLPb67uzJZbs%2BwJ68CSId%2FY6f1TNueLRvI72Vw7g3HSthzBG8E13NxbyeiYBwohRVaowOVFjyw5zBjejanx2QJrANyqAwkt6GCJjRG8&X-Amz-Signature=6b1b554bc9fca826f6f7f94b2a743ce086775fbd00ca486de5e13840ddcc0155&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SL74XNU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQ7vZjrTmkk3L4Dz%2F%2FvhRK804RHfCZJjAa0XcofTTxogIhAJ3caHC%2BJm5hrqDNa6FK8sn9J%2B%2BrJcG21egUiV4C6t7nKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwljOL6DDC3FUiZ%2BuAq3AP9MN26Ymbw0DIjaegyMk8xNt8ActfSBtwOihrzx7J5GwiQkJAuTCrjgmFYh8oQGP6Q%2FaJt%2B4gWXDXsTuEZLcECDGDYI62dk87tQ%2FrZHaqDAbNlm58Fwzy2Vtnhl6cpeLw%2Fmk0AyXS6JH8fTqZcaavtlgpJDU8ewxQen5yDM0KAJzd0VFp1WLD69QgusDVR%2BYLHo5pC4IV6ZRcFZ8Fg3NbHrVqSnwZRfXWLf9c04ihMhYx5m3eN7vfvRItVG%2BSdcMONHpqOn4JtP5mPztgin%2BFxuueo5BlckoD7vZfjs0jMoL1hNhawdjHzpWJ8IlmYBCVxMerFu00m8RU6igONM4fAHZoke05687xWqreoKcjZdCKhAQ9ZBgOQ8fYJXh8tguE8yxWSuQzr2NW%2BuUdkEa2zzPTdsOxGkLKsUOwcPM8ppJlN8q0CvpyBBgahg8xJidHWe9B7yVXaJ2pu02A2DbX5UdxbY1sK00OKgErjIqAkoKTpS5unNUlcrkx%2FE1XEFJaIHoHEQJYhUCDG%2Buqh7bTQTp9W4HaomySBeUxjYFje8l9F3D4a2zghXaRwVhlG9nBe%2FtGaMT%2BFMwPRlawHxrkAOzGr234V3R0rD629MlUwFjpJubBMfWAgyzozmTCI9%2Fm8BjqkAaXQpkaNohdFBEinDiuJdm5S6KYFDUnbjFhblMve60wokC23ozTUI70hBdiNaTbTwVN6fP4t90TX6wyfB4Kc%2FWwA8ZrZ%2BrnL9ZRZJIYEH6zOMLJfMHVxmY7ftwhPPr9zUwXLlq6%2FnZnL8oC%2B2ifbjxv%2B3lK2tyClStpt7%2Fxw8KMGtpU5eMFcyE3irG1Pr%2Fb5eagLaV3PUxrbsF%2FaaMOw5fqltXmM&X-Amz-Signature=15881b251f4bdcc6df6203ff735d31250f8fdb4dbddefa5c767353fa1beb744a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SL74XNU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQ7vZjrTmkk3L4Dz%2F%2FvhRK804RHfCZJjAa0XcofTTxogIhAJ3caHC%2BJm5hrqDNa6FK8sn9J%2B%2BrJcG21egUiV4C6t7nKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwljOL6DDC3FUiZ%2BuAq3AP9MN26Ymbw0DIjaegyMk8xNt8ActfSBtwOihrzx7J5GwiQkJAuTCrjgmFYh8oQGP6Q%2FaJt%2B4gWXDXsTuEZLcECDGDYI62dk87tQ%2FrZHaqDAbNlm58Fwzy2Vtnhl6cpeLw%2Fmk0AyXS6JH8fTqZcaavtlgpJDU8ewxQen5yDM0KAJzd0VFp1WLD69QgusDVR%2BYLHo5pC4IV6ZRcFZ8Fg3NbHrVqSnwZRfXWLf9c04ihMhYx5m3eN7vfvRItVG%2BSdcMONHpqOn4JtP5mPztgin%2BFxuueo5BlckoD7vZfjs0jMoL1hNhawdjHzpWJ8IlmYBCVxMerFu00m8RU6igONM4fAHZoke05687xWqreoKcjZdCKhAQ9ZBgOQ8fYJXh8tguE8yxWSuQzr2NW%2BuUdkEa2zzPTdsOxGkLKsUOwcPM8ppJlN8q0CvpyBBgahg8xJidHWe9B7yVXaJ2pu02A2DbX5UdxbY1sK00OKgErjIqAkoKTpS5unNUlcrkx%2FE1XEFJaIHoHEQJYhUCDG%2Buqh7bTQTp9W4HaomySBeUxjYFje8l9F3D4a2zghXaRwVhlG9nBe%2FtGaMT%2BFMwPRlawHxrkAOzGr234V3R0rD629MlUwFjpJubBMfWAgyzozmTCI9%2Fm8BjqkAaXQpkaNohdFBEinDiuJdm5S6KYFDUnbjFhblMve60wokC23ozTUI70hBdiNaTbTwVN6fP4t90TX6wyfB4Kc%2FWwA8ZrZ%2BrnL9ZRZJIYEH6zOMLJfMHVxmY7ftwhPPr9zUwXLlq6%2FnZnL8oC%2B2ifbjxv%2B3lK2tyClStpt7%2Fxw8KMGtpU5eMFcyE3irG1Pr%2Fb5eagLaV3PUxrbsF%2FaaMOw5fqltXmM&X-Amz-Signature=dd8d4d838bf004b6d10942221b822ee7d324ab4a55a0313dc43e47848acbe975&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SL74XNU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQ7vZjrTmkk3L4Dz%2F%2FvhRK804RHfCZJjAa0XcofTTxogIhAJ3caHC%2BJm5hrqDNa6FK8sn9J%2B%2BrJcG21egUiV4C6t7nKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwljOL6DDC3FUiZ%2BuAq3AP9MN26Ymbw0DIjaegyMk8xNt8ActfSBtwOihrzx7J5GwiQkJAuTCrjgmFYh8oQGP6Q%2FaJt%2B4gWXDXsTuEZLcECDGDYI62dk87tQ%2FrZHaqDAbNlm58Fwzy2Vtnhl6cpeLw%2Fmk0AyXS6JH8fTqZcaavtlgpJDU8ewxQen5yDM0KAJzd0VFp1WLD69QgusDVR%2BYLHo5pC4IV6ZRcFZ8Fg3NbHrVqSnwZRfXWLf9c04ihMhYx5m3eN7vfvRItVG%2BSdcMONHpqOn4JtP5mPztgin%2BFxuueo5BlckoD7vZfjs0jMoL1hNhawdjHzpWJ8IlmYBCVxMerFu00m8RU6igONM4fAHZoke05687xWqreoKcjZdCKhAQ9ZBgOQ8fYJXh8tguE8yxWSuQzr2NW%2BuUdkEa2zzPTdsOxGkLKsUOwcPM8ppJlN8q0CvpyBBgahg8xJidHWe9B7yVXaJ2pu02A2DbX5UdxbY1sK00OKgErjIqAkoKTpS5unNUlcrkx%2FE1XEFJaIHoHEQJYhUCDG%2Buqh7bTQTp9W4HaomySBeUxjYFje8l9F3D4a2zghXaRwVhlG9nBe%2FtGaMT%2BFMwPRlawHxrkAOzGr234V3R0rD629MlUwFjpJubBMfWAgyzozmTCI9%2Fm8BjqkAaXQpkaNohdFBEinDiuJdm5S6KYFDUnbjFhblMve60wokC23ozTUI70hBdiNaTbTwVN6fP4t90TX6wyfB4Kc%2FWwA8ZrZ%2BrnL9ZRZJIYEH6zOMLJfMHVxmY7ftwhPPr9zUwXLlq6%2FnZnL8oC%2B2ifbjxv%2B3lK2tyClStpt7%2Fxw8KMGtpU5eMFcyE3irG1Pr%2Fb5eagLaV3PUxrbsF%2FaaMOw5fqltXmM&X-Amz-Signature=f6ae1b586f496c8a448e80433c1a1f133a4832201b526dc6283b481b119a1794&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466354623Q3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgcJCzxdfpshwReem1oQ79SAXr4SUYR9eheHwjDAHL5gIgQuMlzEA%2B%2Bwa5gA1gGqPrt5zfwFhSN%2BHHG4FxvAxlV9AqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3IWw9zW2aNrO37hyrcA6qMbvQMTATGLrgFy0Y317IuyNDhXofIyla%2FHOfcw%2Bd7ERTh6OiiQSmpaNDFZnVJtRe4hbyQQBSKqH1kWwQpRkaOYgkrGWi434Y2GsMzp2M7lwhvM66WpayGbrPocgFAx8GdN0o%2FVmz6tSMrvIiXCScq9MGKzn%2FC2MUb%2BbyMW5Z2WpLW7taRUaUW6UG%2BmSD9TnBDx1WB7trO7k6w%2FzeZrgEu0PgW6v04nSOrXaugmC9H4BSfggJkxZ%2FQdCOJ5a5f1kRw2mTNeELeVL7W5keO4F9kn4PyY%2Fqik62tN4Lc1Cs23J6v2dkE6I2RDM0sXO9MHJfLBONwmh%2FD3U4cp7shfdGT7EWqT%2BjQQJuV3IFPbX%2F3aG6O6lRqjagZrvCnMdkpA75fNjxvTpvlHXQB3SPVYIsccSgXYjCmOPKAzQ3B4e656SZXgdR90Q8%2BjdMTxuXoXjukA%2FUE32t4u2x5oYDfUDNL4ZDb3iHB5XGHHp5sV7YgGNInR0dLNW4X9NRNqApO4QCXY%2BjnLHZf2AyynuDRHueJp9pIdWTbVoLzxnH5NyqizjfrvECyGdmgGhb4TYvSr0fxsZKg4Hl%2FGm8JWa%2FADVxqVa5y0JQKNPzYYEA%2FG6WTgzGe3rfRdCzfVaUkMMb2%2BbwGOqUBJ%2FIEXcOz%2BLjPyM4f0PWFY2Uv5l6pLtcGQ4CH%2FX2ECvt8BsDtwqs9S0gZONFCkrh6kyFU3tcbRRrH3svEyewR1%2Bp9%2B%2B6KF9FtGh1fskK7WyWSicy1gRBPSV%2FgJ6lkHkzPUj%2BOR%2FRDgavcWucPiIEtFRbzu%2FSbVVAAb%2F0U5dQuFSO53QCAuBffx5xdxsXcJZ0T4X2KZUdkbxyZYzCU0Ko4HbtPi1Es&X-Amz-Signature=59fb8bff927500651785be224d78d963b367aaede8be0637b245d44736c8bdb1&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQESVY3P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDF52l%2F5IQUPk9Vv6JCPls3gYk9rPW1NacftbHoioY3rwIgFuWJQ%2B1%2Bcb%2BbKrTnBdutd6DTBOE43%2B6O4Aa2Gglda9YqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKyRBPFK2imPsKpp6yrcA%2Bk3fTl5%2BH%2Fsil9SA%2FqhmJiSKBT7azLBZCD3NnFPYwmgm3D5OOIWBaUdbdVC2rpA4QcUhAW6dwfFQVTnOYb%2FIUdxh%2Bea5pEzubqUJ3ItR0ycEYGcG%2BWxe%2FfB9sfcYqSPdndyo9m8BTyPqR%2BECyxRT%2BtuEQaPHPAgi%2FWrsOyDc8noQ%2Fgbe4vONEDrhfREI%2FMtY8dD1n4UN7vtbNDBKRreZ4RB1JoznHud12HY3XsldLzxOlussvFEQaLc4frkU4RuMkegrpCExi5qgt4QZ8a1EVWWhR481lm6BvzD7czBg41KHq%2BODEPjVfkfbVTYvYC%2Bw8uOLSazkvLUE2Th%2BozRs6jc8KpUUNPRL5rgAHLXcULCW%2FOsy5Y1k%2FkK8wu2APVBh38Uewb625ZNpfiFugmjDwF3iNRUu1OoeWxU7tOMKnzf3TTxii23FZOW17C2RpU1ShMhGPRvU6r0axKsjOeJzXApsQaTC8%2BgnpNYKqwvTX5jWDtMSSbuzD0o7lRNwsQezqcT0UjEBXXHQV23nm8%2Fbhz8lzWNqtxiREh7vsSiUnuPPWhixeXugRToIdvbqJo8Uqig8MNg8Wvaysw7QPGXRecYjYrSJeI86BICF6BKD5IrI3icPMnDfRBDOsFSMNj2%2BbwGOqUBT4JkBAcG5JOJr25GGiwztkuobkix%2FNZT7g00rMs7F0GePNaFSTYH35%2BZpb2a03nJdRzHomzEhuKMrmsjQrWXsvYzCdzCV4x%2FpvCr94edSbete5hNqMDkqaZZvsrwLsAtYagC3BCh2Xl2pBOrKq%2Fb79P24IwhXeOlsnOjopAjGqDS1bOm%2B7gNvnE3gnXNtmDXqZB%2Be%2FgBzAKhnzKuSwQLebHhS38v&X-Amz-Signature=3668c13be6a4dd5a4809d7f7823663d6662c4554c39791ba4f8ec459bcfd05f6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKSFVS2E%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWZh52FMpdpRSbWeYaDoXGYcY5TxfZkXeRSV2Uz%2BIwVQIgMLgB%2FxZTl4xHE89RgIMMIBj9rUMq75BCNXFUpPJKGHcqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA1WBVjWop4gDUTIVCrcA3qZUwhnWYEaOyxt8aYFLIp0LXz2rUqb7ntN4rMkQP35BvTHY55392XhJQgFusFmwPa65EWU7XJLZ77qJVLMl8lrfFnIbxSaLq7M6jIq4TNZY03DeAhLhM9EFJaOe81CfygqkzuXVRGPtAq4wVSQiofSk1VaGOD%2BTsJgfD66pBFDkzqnbzHlQGcMIVZ9IHVyZ1HK7wEQShyOqbIcYeYRL0%2Bj9IJva5B2kZtTRoSWTMrvP3tic3xaGh6XAkJjLnJNi09buJIPbjdME3wMuXXlulRuvic6ua5Us3p0ZAUPSsRCsuLkdR6a6mS0nmzYIaaWnjhqcZsxB1SXIRJewYiFuy86smjDlWD8MenCxh48%2BZVvrOtSeRxp42%2Bk%2Bso1DTAhsCPtfPaHEhBLJQLuqGH9%2BBAbLPmD0o%2BufEZ%2BwBBS7CeAUL%2BmX8hAgFdHyop0a5%2FXt9lDeFEVLs%2B1W%2Fcl5PqXowpPlIf9p4RSbmud8jI%2BeozbkcL9t9uLVLKhodcBKSH02lj9%2FGL2GQg6m4ts4Xe76WbIKyADz6ODZGhrs75UMc3dCfp%2BOIaUjrUETdp3eWnkx7mHgDJJH3MlLsllwVShhuRvW%2Br76PdFxpCT3AbHx19wHeqBiJu4EKkDNW%2B7MMX2%2BbwGOqUBYuTV3J62VpYt%2FSosuac%2FBcMDgCoNp40G5M0CRca10RivihLOCzoh349priKEt319LVu%2FetPrf3BEZzPTHXSKr9etb%2BGK9WXT3BY%2BdsHIoYPJznLqPjBLtmDsTepOh%2F%2B0DtpbSHVW3JyupdXavTtw%2F8ttg6MuiQkx%2BynBiKKgY%2F4PzfiwED3DAYBVXluUohhWDX48SnTeFSvTif0tThdP8ozCGPMc&X-Amz-Signature=3439165d0a321f6da397ed2b2e8504efbb3dfaeb8bd8c289a40e76cdd207abe3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y3RB7YA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrt6c8wnmOV96z%2FZQ5ing0EyKx5kARhv%2Fh%2FgiUFYEbxgIgaBy2NKKY%2BMezC%2B%2BBLRTYQjL3qyNLqBshpLoBsFH2CMwqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHd62JxRNXwkTA8GVCrcAzE7dh5QL7Dc26oMhxpsF%2BYSVx0pUHWKpsHxshAzXrXp%2FblD0SwEzxNDC6wbONzMr3Gkrhg%2FguLeGr%2BWzMka1Ss6%2F98Hr91%2B3n9bg1AmziC7d%2FFhBQ6neGTxc0sAV%2BAnDI009eno9zX1M3u3XRuFbReVF3wXwtX0lBomiNYMUUpiH2aF8IUZMqtsvj8W5HqxmSRmP5FCuN17Qe38IsKzQb5k4yVMU%2BLhelmBeFQABE21WCBLXM9Qr7mLyCjVcNBKcdtzp6W2%2BaDo%2BBcOheNkFijRbT7mlfnvI%2BE8crVp39rPYWBHL%2FN2Og1yUdCGIgMHntHlBcpp17TwD53F7ZLxfKZmpHCby2KLheoXPB9J9FcDdVtqfDH7XT2G7YZX0W1%2FAeCI%2FIlHTPPkqF3lLQQ%2F3%2B%2FSyu8IqBSt68zpVVHZ6ohev6gKf1Gw4J1JhS%2FX%2FQ2pVAnWX%2BOgniNfjIDzphEEeHMW18so5ogOWRyNWQmlRUJrBxmdGOd4HPicn5l3xgUny%2Fp8obA6paHUrQ5Rz66O9Oo4tP5GSxcVik0e45%2Bj239hP%2Bq%2F4D0go64o%2FSrctkUofjQ5r7PZvyD0Yfyw4S%2BoHLOCr0tg5YnP%2B%2Fas4So5%2BEQMz1r3djFFeSHakSdRMKb2%2BbwGOqUBYNhunIOIomPU3QCwsjSnRWm5zGuS0B2oLwU8cevuonEIfFEqnj4yqIuzjq8rAL%2F84yAMEX83u5o8Dh561%2BxJGbzfbOsHML2ybYiym1pksiyKfBTJBbqFhocvK9%2FNlbYolQ5kCFMWV61fPKTXL403fS%2Fb2M3svfiPAZ%2F0GYT6faBUubw6Rme2MQJalTAwihRdecr66p43y4nKzhiBSrWnNlA5x4ze&X-Amz-Signature=7050c87e65b47bf739032876ee373fd8f9589208a91f17602d947aab7c83264d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y3RB7YA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrt6c8wnmOV96z%2FZQ5ing0EyKx5kARhv%2Fh%2FgiUFYEbxgIgaBy2NKKY%2BMezC%2B%2BBLRTYQjL3qyNLqBshpLoBsFH2CMwqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHd62JxRNXwkTA8GVCrcAzE7dh5QL7Dc26oMhxpsF%2BYSVx0pUHWKpsHxshAzXrXp%2FblD0SwEzxNDC6wbONzMr3Gkrhg%2FguLeGr%2BWzMka1Ss6%2F98Hr91%2B3n9bg1AmziC7d%2FFhBQ6neGTxc0sAV%2BAnDI009eno9zX1M3u3XRuFbReVF3wXwtX0lBomiNYMUUpiH2aF8IUZMqtsvj8W5HqxmSRmP5FCuN17Qe38IsKzQb5k4yVMU%2BLhelmBeFQABE21WCBLXM9Qr7mLyCjVcNBKcdtzp6W2%2BaDo%2BBcOheNkFijRbT7mlfnvI%2BE8crVp39rPYWBHL%2FN2Og1yUdCGIgMHntHlBcpp17TwD53F7ZLxfKZmpHCby2KLheoXPB9J9FcDdVtqfDH7XT2G7YZX0W1%2FAeCI%2FIlHTPPkqF3lLQQ%2F3%2B%2FSyu8IqBSt68zpVVHZ6ohev6gKf1Gw4J1JhS%2FX%2FQ2pVAnWX%2BOgniNfjIDzphEEeHMW18so5ogOWRyNWQmlRUJrBxmdGOd4HPicn5l3xgUny%2Fp8obA6paHUrQ5Rz66O9Oo4tP5GSxcVik0e45%2Bj239hP%2Bq%2F4D0go64o%2FSrctkUofjQ5r7PZvyD0Yfyw4S%2BoHLOCr0tg5YnP%2B%2Fas4So5%2BEQMz1r3djFFeSHakSdRMKb2%2BbwGOqUBYNhunIOIomPU3QCwsjSnRWm5zGuS0B2oLwU8cevuonEIfFEqnj4yqIuzjq8rAL%2F84yAMEX83u5o8Dh561%2BxJGbzfbOsHML2ybYiym1pksiyKfBTJBbqFhocvK9%2FNlbYolQ5kCFMWV61fPKTXL403fS%2Fb2M3svfiPAZ%2F0GYT6faBUubw6Rme2MQJalTAwihRdecr66p43y4nKzhiBSrWnNlA5x4ze&X-Amz-Signature=0a4c0bff89720b4086cb77793075a95e097b766b36d5dc021439292b58a3576a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
