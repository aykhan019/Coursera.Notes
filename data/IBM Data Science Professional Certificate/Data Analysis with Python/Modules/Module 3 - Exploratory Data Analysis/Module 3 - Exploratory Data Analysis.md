

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PN3LZG2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIA%2FyYkv%2Fxv21WWRGSLcXtg7bt6vYvHjCCB2%2B78ruxafCAiEAkEz4%2BVIzP%2BZbbR1HYLIlafm%2BhYGLmCNqRL0TrLd%2Ff2oq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDMG0sUIpTkXXvJSJyyrcAwXjX2dyAMvYrS4avE5UnUWZyYpy%2F2UHkDqmutfsI2ZPcZKIRnJgv91v%2BJgf6pyqZ9tKaecUEk5f%2FpzQ3mIva88FtXmdW%2BrHYr3frgvNoZkmJg2WJpGKuQAnjiiXMhWVo0Mzj7HrJPgKJ%2F%2BeEGFIc5xlWTqo6%2FKE%2BfMtp2f3Usb%2BPS%2FZtV0FURbViSP7nerZwKrJts8NllAZC9CgoodbMSRTajZIJ2Y8lp5JzAWqr9MCJynBwn8TXFJCkYnSybIVuWJayCDVQbR47GyVOc01x%2FB%2Fdk5D8rWSGC1WZkCeWGrsKGwKXkvgXkqoSYQR%2BjHRrFaIj%2BX1JNVdeL8vJGqxEMqW0RYCCG6tuK9ugDXpbQs8ed%2FLj24bAHOkXR1dGRHUoccyoNS%2BRbha6NzsU2eJHQxvnfOtIHqm2c2agmaPCSdrCEp%2FfQQ6OtXEPKZ3CDFccTaI8INzwfQztCqdGicoAj9ya8kNE8PPWDF2Pm4MX4LTgRhIYO09%2BiNZGjbD9cwcE01laY9Bl0gky7TPxJoNT1mpfWybIrmz4fYnFJZCDSq4NyJprgzcULlgdIn3lNBUqijL1pwYgvkfK6%2B2rrMJr2UWPHyWD0uUU5sUQLoBPCmTDvP0EOl5kb0wLFqIML%2Buh70GOqUBx19u0ZtzYtea59v3lKbZeMglnEGwV0j3JZrYfzElOAam5Bzrj0QKaShuZHwgI97y1mSCE49hzhN6ouoP5ilUC5zLufrCq%2F8Kr10TArPLLj%2B45w270cqCSDHFZYIDquNs19LT18vmp3au6tThU41PX6dun076GJEqujJ3VbGIq21ohRr2%2FXgf358JbZTtlWR5YWpICzDtTNaqUmJhAiZI1qI3vFXb&X-Amz-Signature=25a69af7ed20dd1941c2d678f8bd8d26a267dd319a9ce45981d0bfcb75e0839f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PN3LZG2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIA%2FyYkv%2Fxv21WWRGSLcXtg7bt6vYvHjCCB2%2B78ruxafCAiEAkEz4%2BVIzP%2BZbbR1HYLIlafm%2BhYGLmCNqRL0TrLd%2Ff2oq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDMG0sUIpTkXXvJSJyyrcAwXjX2dyAMvYrS4avE5UnUWZyYpy%2F2UHkDqmutfsI2ZPcZKIRnJgv91v%2BJgf6pyqZ9tKaecUEk5f%2FpzQ3mIva88FtXmdW%2BrHYr3frgvNoZkmJg2WJpGKuQAnjiiXMhWVo0Mzj7HrJPgKJ%2F%2BeEGFIc5xlWTqo6%2FKE%2BfMtp2f3Usb%2BPS%2FZtV0FURbViSP7nerZwKrJts8NllAZC9CgoodbMSRTajZIJ2Y8lp5JzAWqr9MCJynBwn8TXFJCkYnSybIVuWJayCDVQbR47GyVOc01x%2FB%2Fdk5D8rWSGC1WZkCeWGrsKGwKXkvgXkqoSYQR%2BjHRrFaIj%2BX1JNVdeL8vJGqxEMqW0RYCCG6tuK9ugDXpbQs8ed%2FLj24bAHOkXR1dGRHUoccyoNS%2BRbha6NzsU2eJHQxvnfOtIHqm2c2agmaPCSdrCEp%2FfQQ6OtXEPKZ3CDFccTaI8INzwfQztCqdGicoAj9ya8kNE8PPWDF2Pm4MX4LTgRhIYO09%2BiNZGjbD9cwcE01laY9Bl0gky7TPxJoNT1mpfWybIrmz4fYnFJZCDSq4NyJprgzcULlgdIn3lNBUqijL1pwYgvkfK6%2B2rrMJr2UWPHyWD0uUU5sUQLoBPCmTDvP0EOl5kb0wLFqIML%2Buh70GOqUBx19u0ZtzYtea59v3lKbZeMglnEGwV0j3JZrYfzElOAam5Bzrj0QKaShuZHwgI97y1mSCE49hzhN6ouoP5ilUC5zLufrCq%2F8Kr10TArPLLj%2B45w270cqCSDHFZYIDquNs19LT18vmp3au6tThU41PX6dun076GJEqujJ3VbGIq21ohRr2%2FXgf358JbZTtlWR5YWpICzDtTNaqUmJhAiZI1qI3vFXb&X-Amz-Signature=9b397e42cf6536c2b3c3cd60433365c4cf1b166fc891078d7a3de1a2585c2e58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PN3LZG2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIA%2FyYkv%2Fxv21WWRGSLcXtg7bt6vYvHjCCB2%2B78ruxafCAiEAkEz4%2BVIzP%2BZbbR1HYLIlafm%2BhYGLmCNqRL0TrLd%2Ff2oq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDMG0sUIpTkXXvJSJyyrcAwXjX2dyAMvYrS4avE5UnUWZyYpy%2F2UHkDqmutfsI2ZPcZKIRnJgv91v%2BJgf6pyqZ9tKaecUEk5f%2FpzQ3mIva88FtXmdW%2BrHYr3frgvNoZkmJg2WJpGKuQAnjiiXMhWVo0Mzj7HrJPgKJ%2F%2BeEGFIc5xlWTqo6%2FKE%2BfMtp2f3Usb%2BPS%2FZtV0FURbViSP7nerZwKrJts8NllAZC9CgoodbMSRTajZIJ2Y8lp5JzAWqr9MCJynBwn8TXFJCkYnSybIVuWJayCDVQbR47GyVOc01x%2FB%2Fdk5D8rWSGC1WZkCeWGrsKGwKXkvgXkqoSYQR%2BjHRrFaIj%2BX1JNVdeL8vJGqxEMqW0RYCCG6tuK9ugDXpbQs8ed%2FLj24bAHOkXR1dGRHUoccyoNS%2BRbha6NzsU2eJHQxvnfOtIHqm2c2agmaPCSdrCEp%2FfQQ6OtXEPKZ3CDFccTaI8INzwfQztCqdGicoAj9ya8kNE8PPWDF2Pm4MX4LTgRhIYO09%2BiNZGjbD9cwcE01laY9Bl0gky7TPxJoNT1mpfWybIrmz4fYnFJZCDSq4NyJprgzcULlgdIn3lNBUqijL1pwYgvkfK6%2B2rrMJr2UWPHyWD0uUU5sUQLoBPCmTDvP0EOl5kb0wLFqIML%2Buh70GOqUBx19u0ZtzYtea59v3lKbZeMglnEGwV0j3JZrYfzElOAam5Bzrj0QKaShuZHwgI97y1mSCE49hzhN6ouoP5ilUC5zLufrCq%2F8Kr10TArPLLj%2B45w270cqCSDHFZYIDquNs19LT18vmp3au6tThU41PX6dun076GJEqujJ3VbGIq21ohRr2%2FXgf358JbZTtlWR5YWpICzDtTNaqUmJhAiZI1qI3vFXb&X-Amz-Signature=895e7df8069eff723484f0c22cdac315e63c5572bf88081ff056033e98ed78e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XDWDSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDBWTj6XrjcdVqnTjat5b3BsYeCMN03S4TXnZNWk9rftQIgF2iPEGEpPXXu0ugFD2Xaxrxr60Fim3VNagKLrdw1fecq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDT7Axv%2FsbmZV8fIvircA4kKnnxmxNBEocoZ5Bo%2Bh%2BVDrZVjR%2FQWNdflOsj4tfr%2F40vMWSWuDZq8vghR6KvwL8aaXPn%2F3kCvWV1v0SsuqtZyE1dAoyI%2Fat00EvvXYSypriLxgN3cyB7vOQlHtewUp8ZAB8YZjVpgWABo9bgjrdLtzOKCcNygseTkba09e7Dh1NWgew9isqpNGQEqTW%2B0%2FKtd7cg7Un%2Fkz7tzcVdn2QahsMirsjqvQD4wRZpN8tF%2F5oEwPJHQ03TzOie%2B9ZMFI%2FEo3A0qERtTvaLzWZPlNIjZclDb60YJZTCqe1B9smCdSvlDKQ%2ByTNnwhzcc7hHt4DyIydFMMijwKcQtN6qQ3uwvsQBjRjJWCewq86e4lOmRA%2BAnCb88jh28OhAkt8hEMJbmuEs14zXhYjkyOC1YanyKDI8st%2BP1zDaJmCcFZYlzCyC6zsNlVjIa0KkcVSQCEIVXsT%2FGUbpLDpkgttL038cWwBRNe%2FNSOoU2w3V5%2BlXQNMEszmQ4xpKuKaGRjcvhMbMskGQdgZoCitzyl22BVlxABl9SYqFDRTHgDZnPC9Rgv20b8PpSNhZTwY4ISEi7tUT47z9JHNwCrxlS6TYvJXd0hCDlwElf2d09y6%2FAL48ERoMwgdolQY%2Bd5g0AMJ%2Buh70GOqUBL%2FyjytlhbJrTq3Fje%2FO2poCnwIuaKDop%2BGoDccUpVFebgIEYpufWDLRgrAj7Y7twFH4dG1BX1Dh4jznGA%2FTcJBuSjDrVf1m42g9fUy7bb4uIZSSBuzeefX1GwqGOS86y9CjdbjVa9lYn2mSygXUM3f4N8NqVR1JCOWNQbzBZbw4g21Y0JZDvpbkii6tiQpB26TTyXi8b28xbeSljSIjW3CDZYrcB&X-Amz-Signature=03154cb1f1f2bf254292fd2b8269922758361e14d84578588ae9d264a10a9be4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XDWDSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDBWTj6XrjcdVqnTjat5b3BsYeCMN03S4TXnZNWk9rftQIgF2iPEGEpPXXu0ugFD2Xaxrxr60Fim3VNagKLrdw1fecq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDT7Axv%2FsbmZV8fIvircA4kKnnxmxNBEocoZ5Bo%2Bh%2BVDrZVjR%2FQWNdflOsj4tfr%2F40vMWSWuDZq8vghR6KvwL8aaXPn%2F3kCvWV1v0SsuqtZyE1dAoyI%2Fat00EvvXYSypriLxgN3cyB7vOQlHtewUp8ZAB8YZjVpgWABo9bgjrdLtzOKCcNygseTkba09e7Dh1NWgew9isqpNGQEqTW%2B0%2FKtd7cg7Un%2Fkz7tzcVdn2QahsMirsjqvQD4wRZpN8tF%2F5oEwPJHQ03TzOie%2B9ZMFI%2FEo3A0qERtTvaLzWZPlNIjZclDb60YJZTCqe1B9smCdSvlDKQ%2ByTNnwhzcc7hHt4DyIydFMMijwKcQtN6qQ3uwvsQBjRjJWCewq86e4lOmRA%2BAnCb88jh28OhAkt8hEMJbmuEs14zXhYjkyOC1YanyKDI8st%2BP1zDaJmCcFZYlzCyC6zsNlVjIa0KkcVSQCEIVXsT%2FGUbpLDpkgttL038cWwBRNe%2FNSOoU2w3V5%2BlXQNMEszmQ4xpKuKaGRjcvhMbMskGQdgZoCitzyl22BVlxABl9SYqFDRTHgDZnPC9Rgv20b8PpSNhZTwY4ISEi7tUT47z9JHNwCrxlS6TYvJXd0hCDlwElf2d09y6%2FAL48ERoMwgdolQY%2Bd5g0AMJ%2Buh70GOqUBL%2FyjytlhbJrTq3Fje%2FO2poCnwIuaKDop%2BGoDccUpVFebgIEYpufWDLRgrAj7Y7twFH4dG1BX1Dh4jznGA%2FTcJBuSjDrVf1m42g9fUy7bb4uIZSSBuzeefX1GwqGOS86y9CjdbjVa9lYn2mSygXUM3f4N8NqVR1JCOWNQbzBZbw4g21Y0JZDvpbkii6tiQpB26TTyXi8b28xbeSljSIjW3CDZYrcB&X-Amz-Signature=d4afc311204d15da2762328daad044ddc158f8f60b2157cda6dfd45a2f065986&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XDWDSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDBWTj6XrjcdVqnTjat5b3BsYeCMN03S4TXnZNWk9rftQIgF2iPEGEpPXXu0ugFD2Xaxrxr60Fim3VNagKLrdw1fecq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDT7Axv%2FsbmZV8fIvircA4kKnnxmxNBEocoZ5Bo%2Bh%2BVDrZVjR%2FQWNdflOsj4tfr%2F40vMWSWuDZq8vghR6KvwL8aaXPn%2F3kCvWV1v0SsuqtZyE1dAoyI%2Fat00EvvXYSypriLxgN3cyB7vOQlHtewUp8ZAB8YZjVpgWABo9bgjrdLtzOKCcNygseTkba09e7Dh1NWgew9isqpNGQEqTW%2B0%2FKtd7cg7Un%2Fkz7tzcVdn2QahsMirsjqvQD4wRZpN8tF%2F5oEwPJHQ03TzOie%2B9ZMFI%2FEo3A0qERtTvaLzWZPlNIjZclDb60YJZTCqe1B9smCdSvlDKQ%2ByTNnwhzcc7hHt4DyIydFMMijwKcQtN6qQ3uwvsQBjRjJWCewq86e4lOmRA%2BAnCb88jh28OhAkt8hEMJbmuEs14zXhYjkyOC1YanyKDI8st%2BP1zDaJmCcFZYlzCyC6zsNlVjIa0KkcVSQCEIVXsT%2FGUbpLDpkgttL038cWwBRNe%2FNSOoU2w3V5%2BlXQNMEszmQ4xpKuKaGRjcvhMbMskGQdgZoCitzyl22BVlxABl9SYqFDRTHgDZnPC9Rgv20b8PpSNhZTwY4ISEi7tUT47z9JHNwCrxlS6TYvJXd0hCDlwElf2d09y6%2FAL48ERoMwgdolQY%2Bd5g0AMJ%2Buh70GOqUBL%2FyjytlhbJrTq3Fje%2FO2poCnwIuaKDop%2BGoDccUpVFebgIEYpufWDLRgrAj7Y7twFH4dG1BX1Dh4jznGA%2FTcJBuSjDrVf1m42g9fUy7bb4uIZSSBuzeefX1GwqGOS86y9CjdbjVa9lYn2mSygXUM3f4N8NqVR1JCOWNQbzBZbw4g21Y0JZDvpbkii6tiQpB26TTyXi8b28xbeSljSIjW3CDZYrcB&X-Amz-Signature=697a651c2759500894953a3b7d3c1beb8cb96738bc0bc17ab986d0ceb6e41f60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XDWDSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDBWTj6XrjcdVqnTjat5b3BsYeCMN03S4TXnZNWk9rftQIgF2iPEGEpPXXu0ugFD2Xaxrxr60Fim3VNagKLrdw1fecq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDT7Axv%2FsbmZV8fIvircA4kKnnxmxNBEocoZ5Bo%2Bh%2BVDrZVjR%2FQWNdflOsj4tfr%2F40vMWSWuDZq8vghR6KvwL8aaXPn%2F3kCvWV1v0SsuqtZyE1dAoyI%2Fat00EvvXYSypriLxgN3cyB7vOQlHtewUp8ZAB8YZjVpgWABo9bgjrdLtzOKCcNygseTkba09e7Dh1NWgew9isqpNGQEqTW%2B0%2FKtd7cg7Un%2Fkz7tzcVdn2QahsMirsjqvQD4wRZpN8tF%2F5oEwPJHQ03TzOie%2B9ZMFI%2FEo3A0qERtTvaLzWZPlNIjZclDb60YJZTCqe1B9smCdSvlDKQ%2ByTNnwhzcc7hHt4DyIydFMMijwKcQtN6qQ3uwvsQBjRjJWCewq86e4lOmRA%2BAnCb88jh28OhAkt8hEMJbmuEs14zXhYjkyOC1YanyKDI8st%2BP1zDaJmCcFZYlzCyC6zsNlVjIa0KkcVSQCEIVXsT%2FGUbpLDpkgttL038cWwBRNe%2FNSOoU2w3V5%2BlXQNMEszmQ4xpKuKaGRjcvhMbMskGQdgZoCitzyl22BVlxABl9SYqFDRTHgDZnPC9Rgv20b8PpSNhZTwY4ISEi7tUT47z9JHNwCrxlS6TYvJXd0hCDlwElf2d09y6%2FAL48ERoMwgdolQY%2Bd5g0AMJ%2Buh70GOqUBL%2FyjytlhbJrTq3Fje%2FO2poCnwIuaKDop%2BGoDccUpVFebgIEYpufWDLRgrAj7Y7twFH4dG1BX1Dh4jznGA%2FTcJBuSjDrVf1m42g9fUy7bb4uIZSSBuzeefX1GwqGOS86y9CjdbjVa9lYn2mSygXUM3f4N8NqVR1JCOWNQbzBZbw4g21Y0JZDvpbkii6tiQpB26TTyXi8b28xbeSljSIjW3CDZYrcB&X-Amz-Signature=c2932782261cbdcbfa36a7b53b3b2f1c4735437e5489eb0a2cb9f15c521a47f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XDWDSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDBWTj6XrjcdVqnTjat5b3BsYeCMN03S4TXnZNWk9rftQIgF2iPEGEpPXXu0ugFD2Xaxrxr60Fim3VNagKLrdw1fecq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDT7Axv%2FsbmZV8fIvircA4kKnnxmxNBEocoZ5Bo%2Bh%2BVDrZVjR%2FQWNdflOsj4tfr%2F40vMWSWuDZq8vghR6KvwL8aaXPn%2F3kCvWV1v0SsuqtZyE1dAoyI%2Fat00EvvXYSypriLxgN3cyB7vOQlHtewUp8ZAB8YZjVpgWABo9bgjrdLtzOKCcNygseTkba09e7Dh1NWgew9isqpNGQEqTW%2B0%2FKtd7cg7Un%2Fkz7tzcVdn2QahsMirsjqvQD4wRZpN8tF%2F5oEwPJHQ03TzOie%2B9ZMFI%2FEo3A0qERtTvaLzWZPlNIjZclDb60YJZTCqe1B9smCdSvlDKQ%2ByTNnwhzcc7hHt4DyIydFMMijwKcQtN6qQ3uwvsQBjRjJWCewq86e4lOmRA%2BAnCb88jh28OhAkt8hEMJbmuEs14zXhYjkyOC1YanyKDI8st%2BP1zDaJmCcFZYlzCyC6zsNlVjIa0KkcVSQCEIVXsT%2FGUbpLDpkgttL038cWwBRNe%2FNSOoU2w3V5%2BlXQNMEszmQ4xpKuKaGRjcvhMbMskGQdgZoCitzyl22BVlxABl9SYqFDRTHgDZnPC9Rgv20b8PpSNhZTwY4ISEi7tUT47z9JHNwCrxlS6TYvJXd0hCDlwElf2d09y6%2FAL48ERoMwgdolQY%2Bd5g0AMJ%2Buh70GOqUBL%2FyjytlhbJrTq3Fje%2FO2poCnwIuaKDop%2BGoDccUpVFebgIEYpufWDLRgrAj7Y7twFH4dG1BX1Dh4jznGA%2FTcJBuSjDrVf1m42g9fUy7bb4uIZSSBuzeefX1GwqGOS86y9CjdbjVa9lYn2mSygXUM3f4N8NqVR1JCOWNQbzBZbw4g21Y0JZDvpbkii6tiQpB26TTyXi8b28xbeSljSIjW3CDZYrcB&X-Amz-Signature=cb81c4dff7c85c6c5c442fb8a496284a00fd95b536a24572506537c4f898f0c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XDWDSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDBWTj6XrjcdVqnTjat5b3BsYeCMN03S4TXnZNWk9rftQIgF2iPEGEpPXXu0ugFD2Xaxrxr60Fim3VNagKLrdw1fecq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDT7Axv%2FsbmZV8fIvircA4kKnnxmxNBEocoZ5Bo%2Bh%2BVDrZVjR%2FQWNdflOsj4tfr%2F40vMWSWuDZq8vghR6KvwL8aaXPn%2F3kCvWV1v0SsuqtZyE1dAoyI%2Fat00EvvXYSypriLxgN3cyB7vOQlHtewUp8ZAB8YZjVpgWABo9bgjrdLtzOKCcNygseTkba09e7Dh1NWgew9isqpNGQEqTW%2B0%2FKtd7cg7Un%2Fkz7tzcVdn2QahsMirsjqvQD4wRZpN8tF%2F5oEwPJHQ03TzOie%2B9ZMFI%2FEo3A0qERtTvaLzWZPlNIjZclDb60YJZTCqe1B9smCdSvlDKQ%2ByTNnwhzcc7hHt4DyIydFMMijwKcQtN6qQ3uwvsQBjRjJWCewq86e4lOmRA%2BAnCb88jh28OhAkt8hEMJbmuEs14zXhYjkyOC1YanyKDI8st%2BP1zDaJmCcFZYlzCyC6zsNlVjIa0KkcVSQCEIVXsT%2FGUbpLDpkgttL038cWwBRNe%2FNSOoU2w3V5%2BlXQNMEszmQ4xpKuKaGRjcvhMbMskGQdgZoCitzyl22BVlxABl9SYqFDRTHgDZnPC9Rgv20b8PpSNhZTwY4ISEi7tUT47z9JHNwCrxlS6TYvJXd0hCDlwElf2d09y6%2FAL48ERoMwgdolQY%2Bd5g0AMJ%2Buh70GOqUBL%2FyjytlhbJrTq3Fje%2FO2poCnwIuaKDop%2BGoDccUpVFebgIEYpufWDLRgrAj7Y7twFH4dG1BX1Dh4jznGA%2FTcJBuSjDrVf1m42g9fUy7bb4uIZSSBuzeefX1GwqGOS86y9CjdbjVa9lYn2mSygXUM3f4N8NqVR1JCOWNQbzBZbw4g21Y0JZDvpbkii6tiQpB26TTyXi8b28xbeSljSIjW3CDZYrcB&X-Amz-Signature=18dfff1d9bd741179573aadb099a7016a00307db915eb7cdafbb14f91195282d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VONJ476O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCH3EeXzcfPDm1Q7ff1NFlVvqr%2FlBsj9rXdwNNRkOL8xQIhAOR1PGs1moD0KsCuR74pdAyMNW1DycqN2ubG0PiZb0UlKv8DCCoQABoMNjM3NDIzMTgzODA1IgwGM3hQ7yzxw1BLfFMq3AOefz9mc93UzMxaf%2FYSPWXXcXMx1Dpq%2F10F54ZJTc6B9LJb4fKcWRsu4QXaaz%2BfhFWPi3fvIQ%2FvfCPW0nW9UecABVvIGASgr6LzUuujZdtN6jbn7nh1zmEZyAUKp5%2B4yRUqUnweqXYPm%2FMmgZu0q8F2dFGilTPRCBi1Q9fQ9TcIdb27Ka3QIjnoSojUZURIzNKUJwuImwdHpqSnVXvCDcLjHjFlJkbOsyIsZvDC4V2b%2FRCt%2FStDOuY572a2UyGsXVqNQUAIWfTWAKhnvTExzaha3aS0szzJGAH05M%2BYvhL%2BSo6WoWvozUhWWVNRi1LEogMMasqurJI7k621imtG4A6GkVC0j9%2BU0K%2Bd5RbAbFV1P1Oxt1UHYC7ylzmX1ifsDNFSzLhBAS8CqzBgD3GSmclXHuQ1MEOq7TfsFsNogDoKNZw5njdOSZB6m49nxD80MegQiAQj1k40%2BhkEwbLB7DzUfxyWJnD95ywLCyDAwSzgcekO3rno3DEvM0Co9us6leHIINQM6JhNyWjozEfqcgexioUphANLO1QiKBVqOz7CgP%2B6sVxPe0%2F0PtAhbkcnKlkB815mAkRi8Bjg15zisAO1ZDrWSlcJpfFl2sa4Zpitw3FrCrUpPlGsaXT0ajCTroe9BjqkAfz3pswwc2GusGtfVOqypO2xd2o1KepTLlPLAhlcl8ROZFcHzp0dcpY9fizBNAWsCyUkzrdS5LELl2mN9DMvnPubwc%2B5bEuBKaIbLjPEutpxSq9P61oL2WWs2tpb53T%2BfkuTTX%2F1iKlpDtXtf7kV2arFUcL0TlY4LNnNNwwRBnKrlhPSEXitDRAJE2dMWQrs%2F%2F1e9V3ujGNzPmxZCRATXJpAhooJ&X-Amz-Signature=3e1ab152600117d52a32e72e976db213e7fa497f5e526b000ad9c50c15cac3e0&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOPLM4UR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIBimY7ba10K8hnTq8S2FFiYcY%2BjegXBaviAQQJKB02c5AiBDtmc7h9G5SHxpXGphK3DMCHvXNZBcAN9ME2wb62ZzSir%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMwzNmIoYuwDKI5LzgKtwDhApy0U4akPz3Hx%2BYWoDSoaBfhrhj1M4jKrBED51fFf17bpk0fMJOUm7LW%2FuSh1IGz9PFAoFjoOmf%2BByy3VXmp37tccza2VyWPpBlR%2BYMFB2ZkzQMm56M3899ZfeLvJq0KwmE%2BSnCniGg%2B4W8maaoIUZUx85HcVXDapgEHZq4dr12kY3klIQwhSrc%2B3JFJ%2FkDu6JC45f5BtjF%2FgdXlW%2BaJzptACHuHbZ1yASO8z7pvym3BQFotNqHjOJmOE7c0g%2FOg%2B0dWAryRE2wlGNN%2BYwWsN0HUbd1UWTxOVuG%2FllKJQi7OoUPjnUceX5GOH%2FESlC5SZ6P20ts1WKAGJrP131VBLeBLy5Ur%2Fo0ef%2B5%2FprK%2FBA4%2FEmKJAEfP63wn0sUZ2uvJiXo0hNjQG5Z5w92nLgLAU6OvdlBBSJf4n6cPfUP7SBeP%2BgXJBukxQ8l9MyFHwbc6SJnNz91WgBnEnqPWij5IMTUjqPHoEo1OHmSrp%2FMqiNv0UQwwUw%2BLMp%2BlrriZWRl0XdLNGbkx0C%2BzwKEE2viFyAmuvTJPF0zzu7q8GfjHqikS8QqGp9brqcBxcVBljvG1SPwr%2BNy0D3xbFVxqM%2F%2FG1p5mDhvI0uuTHCdTDNm%2FeWIyaCGodjlloZmcPYwzK6HvQY6pgHmcFgxU1m40DrlGP8zMR4nuHbvCumbissTcT0ASl2cex04WvlfG39uPGVi04t%2BkMUi2MIsSyiCF%2Fn4rVkDH7TNsID9NxXWJd8dALOR3KruDyo2%2FqZNGR%2FkcG7mgM0iNAEJd1uKVSUctUy4KjakjJOrHtgWEZxGHARzStSGm2KBThpEtI%2BxSf3MmbtKDnAz3Kon5zWaCyoqMojBRM1Qn%2FXM6fGNtbWp&X-Amz-Signature=736ea48052d06a02b09ce3b20bd92c6d8c4ea32877a1ce793f72e26907737d7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XDWDSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDBWTj6XrjcdVqnTjat5b3BsYeCMN03S4TXnZNWk9rftQIgF2iPEGEpPXXu0ugFD2Xaxrxr60Fim3VNagKLrdw1fecq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDT7Axv%2FsbmZV8fIvircA4kKnnxmxNBEocoZ5Bo%2Bh%2BVDrZVjR%2FQWNdflOsj4tfr%2F40vMWSWuDZq8vghR6KvwL8aaXPn%2F3kCvWV1v0SsuqtZyE1dAoyI%2Fat00EvvXYSypriLxgN3cyB7vOQlHtewUp8ZAB8YZjVpgWABo9bgjrdLtzOKCcNygseTkba09e7Dh1NWgew9isqpNGQEqTW%2B0%2FKtd7cg7Un%2Fkz7tzcVdn2QahsMirsjqvQD4wRZpN8tF%2F5oEwPJHQ03TzOie%2B9ZMFI%2FEo3A0qERtTvaLzWZPlNIjZclDb60YJZTCqe1B9smCdSvlDKQ%2ByTNnwhzcc7hHt4DyIydFMMijwKcQtN6qQ3uwvsQBjRjJWCewq86e4lOmRA%2BAnCb88jh28OhAkt8hEMJbmuEs14zXhYjkyOC1YanyKDI8st%2BP1zDaJmCcFZYlzCyC6zsNlVjIa0KkcVSQCEIVXsT%2FGUbpLDpkgttL038cWwBRNe%2FNSOoU2w3V5%2BlXQNMEszmQ4xpKuKaGRjcvhMbMskGQdgZoCitzyl22BVlxABl9SYqFDRTHgDZnPC9Rgv20b8PpSNhZTwY4ISEi7tUT47z9JHNwCrxlS6TYvJXd0hCDlwElf2d09y6%2FAL48ERoMwgdolQY%2Bd5g0AMJ%2Buh70GOqUBL%2FyjytlhbJrTq3Fje%2FO2poCnwIuaKDop%2BGoDccUpVFebgIEYpufWDLRgrAj7Y7twFH4dG1BX1Dh4jznGA%2FTcJBuSjDrVf1m42g9fUy7bb4uIZSSBuzeefX1GwqGOS86y9CjdbjVa9lYn2mSygXUM3f4N8NqVR1JCOWNQbzBZbw4g21Y0JZDvpbkii6tiQpB26TTyXi8b28xbeSljSIjW3CDZYrcB&X-Amz-Signature=c796eef80b0f5735c1e4efd188f5cd73c62c175c8f8ae46785affdefac074241&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XDWDSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDBWTj6XrjcdVqnTjat5b3BsYeCMN03S4TXnZNWk9rftQIgF2iPEGEpPXXu0ugFD2Xaxrxr60Fim3VNagKLrdw1fecq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDT7Axv%2FsbmZV8fIvircA4kKnnxmxNBEocoZ5Bo%2Bh%2BVDrZVjR%2FQWNdflOsj4tfr%2F40vMWSWuDZq8vghR6KvwL8aaXPn%2F3kCvWV1v0SsuqtZyE1dAoyI%2Fat00EvvXYSypriLxgN3cyB7vOQlHtewUp8ZAB8YZjVpgWABo9bgjrdLtzOKCcNygseTkba09e7Dh1NWgew9isqpNGQEqTW%2B0%2FKtd7cg7Un%2Fkz7tzcVdn2QahsMirsjqvQD4wRZpN8tF%2F5oEwPJHQ03TzOie%2B9ZMFI%2FEo3A0qERtTvaLzWZPlNIjZclDb60YJZTCqe1B9smCdSvlDKQ%2ByTNnwhzcc7hHt4DyIydFMMijwKcQtN6qQ3uwvsQBjRjJWCewq86e4lOmRA%2BAnCb88jh28OhAkt8hEMJbmuEs14zXhYjkyOC1YanyKDI8st%2BP1zDaJmCcFZYlzCyC6zsNlVjIa0KkcVSQCEIVXsT%2FGUbpLDpkgttL038cWwBRNe%2FNSOoU2w3V5%2BlXQNMEszmQ4xpKuKaGRjcvhMbMskGQdgZoCitzyl22BVlxABl9SYqFDRTHgDZnPC9Rgv20b8PpSNhZTwY4ISEi7tUT47z9JHNwCrxlS6TYvJXd0hCDlwElf2d09y6%2FAL48ERoMwgdolQY%2Bd5g0AMJ%2Buh70GOqUBL%2FyjytlhbJrTq3Fje%2FO2poCnwIuaKDop%2BGoDccUpVFebgIEYpufWDLRgrAj7Y7twFH4dG1BX1Dh4jznGA%2FTcJBuSjDrVf1m42g9fUy7bb4uIZSSBuzeefX1GwqGOS86y9CjdbjVa9lYn2mSygXUM3f4N8NqVR1JCOWNQbzBZbw4g21Y0JZDvpbkii6tiQpB26TTyXi8b28xbeSljSIjW3CDZYrcB&X-Amz-Signature=43919725a2623ed77ac033fd02d3979cfd58326e11ff2495aec8557df6349bec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XDWDSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDBWTj6XrjcdVqnTjat5b3BsYeCMN03S4TXnZNWk9rftQIgF2iPEGEpPXXu0ugFD2Xaxrxr60Fim3VNagKLrdw1fecq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDT7Axv%2FsbmZV8fIvircA4kKnnxmxNBEocoZ5Bo%2Bh%2BVDrZVjR%2FQWNdflOsj4tfr%2F40vMWSWuDZq8vghR6KvwL8aaXPn%2F3kCvWV1v0SsuqtZyE1dAoyI%2Fat00EvvXYSypriLxgN3cyB7vOQlHtewUp8ZAB8YZjVpgWABo9bgjrdLtzOKCcNygseTkba09e7Dh1NWgew9isqpNGQEqTW%2B0%2FKtd7cg7Un%2Fkz7tzcVdn2QahsMirsjqvQD4wRZpN8tF%2F5oEwPJHQ03TzOie%2B9ZMFI%2FEo3A0qERtTvaLzWZPlNIjZclDb60YJZTCqe1B9smCdSvlDKQ%2ByTNnwhzcc7hHt4DyIydFMMijwKcQtN6qQ3uwvsQBjRjJWCewq86e4lOmRA%2BAnCb88jh28OhAkt8hEMJbmuEs14zXhYjkyOC1YanyKDI8st%2BP1zDaJmCcFZYlzCyC6zsNlVjIa0KkcVSQCEIVXsT%2FGUbpLDpkgttL038cWwBRNe%2FNSOoU2w3V5%2BlXQNMEszmQ4xpKuKaGRjcvhMbMskGQdgZoCitzyl22BVlxABl9SYqFDRTHgDZnPC9Rgv20b8PpSNhZTwY4ISEi7tUT47z9JHNwCrxlS6TYvJXd0hCDlwElf2d09y6%2FAL48ERoMwgdolQY%2Bd5g0AMJ%2Buh70GOqUBL%2FyjytlhbJrTq3Fje%2FO2poCnwIuaKDop%2BGoDccUpVFebgIEYpufWDLRgrAj7Y7twFH4dG1BX1Dh4jznGA%2FTcJBuSjDrVf1m42g9fUy7bb4uIZSSBuzeefX1GwqGOS86y9CjdbjVa9lYn2mSygXUM3f4N8NqVR1JCOWNQbzBZbw4g21Y0JZDvpbkii6tiQpB26TTyXi8b28xbeSljSIjW3CDZYrcB&X-Amz-Signature=0f441cec61f2ba4ac0bcb20d838052aa1938abe0f855c33997ff3ead21e3dcab&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEFYERFT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQC%2FLbdBHkBgOu1odhtOk9SZ%2BKSxgQL0aF%2FzIhccbwoaFAIhANLXmrVvoD4tXh5u61qdgo%2FE0la5kmWS%2BL%2BV8ia4wdgzKv8DCCoQABoMNjM3NDIzMTgzODA1IgwRfhXYGemJaAg7VdIq3ANaqIbN9lkeuQh2FD6eBoQ83Jr6oqDbgIQ2DAY%2BK%2B10kBoorC9T8IZTJ%2BKq0hms6kozU2PTXDYDnEb%2BEkPTcP7h3tZIQzfIPtMhmTy20Qtk1jtTjWojsHDJSHPaNOw8hJHakJ8pJFvFXIg2aMpg6Z6n5PRq13paxSeeGi2s8DWvcj2f2Zz8Jx%2FL7c1mc82GTIXnk89KyzDldUBoSiY6KBG14QqWWB7dOOK%2ForFoP0YFIwePQmguszuAmHlLWF5wAIjM4p4C0ATGMwApa4Z9aB2rioeTtA87Z3UI1dZwgwBJIYoW%2F3VVUOkJXTkTlFkuzvgB5drvEoqtBY%2Fn%2FfTksbjFcbScPetMtfILNm%2FjbD07o4NMuMEsLoMD3UN1LHzt2huP%2F%2Fjj2LR9Ub%2BcCG7m%2BpptsjDe%2FO5QLQ1hyErIJFIFnvg54vF2rYNASWjeWprBO6YLhcPaIJiO2OMqsfXVI%2F5MSf2YRgb0vI40tEexQWg%2FQcty%2FddL1izaDEzU4vEGMI9YAFnk27O5WiysQD1AQvrTJy0lYni%2FhPEhf%2BPXAGy6HIaiFmyiMVAXj1UPcTAVxvuJGJPUXiwqejXtF7GLd6RgL2SmHYmuqTCuHjJQCaoW1efs6kE5wz%2F%2BsFp1nzDmroe9BjqkAS6Sm%2BVylif%2FtjmCGxbpXHUSVJHMY9Vf7hON7SGgiECxHs4TYo4UjFx3XxEa9fom7b%2FXyb2fuwj2uFXa91RSN7DnA2kjXmcL%2BIDjIR5Jf5roRIrnOkICTPNNazX5g7l4la2nvwcZJELIAm9%2FMfjCBWd1YK340ZH4hUNyl83nrbcgLCyFu1%2BQq9W%2FOYHs1f%2B%2F%2BjvFxrpE4c%2BqH6QjV09QTpEnAK89&X-Amz-Signature=fbd53bb90365b89fce4572cc57921e7af01ec57407102459008697af7a76184f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654AW7P4K%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIE6t6TXFha24caDCiohaDalMh0a4YBRyPubdOIccbYV7AiBYM6ZL7KPJHifB1RZEp1fDArGGVoAhM3kfsOw7Y5tF0Sr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMAwRw52aKKK8oKnokKtwD0qB5frfOlOYiT7Jc7mz4VfNrjwWBsDCGlElKd8s1KTtjwYbM44El%2BF5%2BmW9Z50FE7CcJL%2F8GWVGsFQymDYeRnEu7tZ4eozJoriHmX7luzzwjolzCGfq0385VQTOibVXuAVcSprVHYR48J%2Fti0uYIu2fPgj4utNMhzxUirveoJceRh6UgNFcZ%2FM5Vxav%2B3o9wxISbr04YoedVCM%2Bq4xHATYesPeD7Bvxv%2BSukIqSBM9ZnA5ahdPtf84aDWX2XxuqSIkvfn30NOuXmxO7sPmm%2FoSN1lwaW1rWLnO1sviq%2FAklWNzFlmnIvwRhHPykpeUz8IM758wKH%2FbUNNp44PJGpcZUATxGm28aAdPxCRkjZIKfP7kjoeAbSITIbNkggJkWvJYuSEpabxjNUyDhenZGlStDD6dxMf600GCTL0a6X%2BcZmrIHuHcptejNOvOOZUsOsUu5OZbxsrLcHDmPe%2FCPI4hv%2Bwz6DBcuwFsgWgTvNgBIydtJbi5XCydWjMdOjZEkXbLBiJQCY0aW1VbRq8GFlraWWNE7inUij3HPfpur%2BMFGNvntHw8pW3EjatYYGL%2FhaYKq61ELNZgI9G%2BQZsEpcALrx%2BIFCbxgz7NI8cvlB9FkEFJ1rgvfcuEcoSJUwtq6HvQY6pgEBV3FXCk9imDxtk8p%2B7C7Tkukz2%2BfWZtr3ZX6gIsbM8yNsZ1d%2B4z%2F7IVdM5koKk4jKA80MzNiuhb%2FeXqpYLSlINOJm3TLo4U6CXMQPpLZa%2FwB17lOldjg2FPZrAB7wccU2F%2F4rv4z2yVWWu1mybUekpBQyNRJmhxVoLaIv74y0PsM5UVfGdHzbvG7VwIxO1LUlPWjSULBs4RQRhsS1GdwX0tedXWHb&X-Amz-Signature=2d50ac656eb62ab8b105ca2abb46ce4a65cccba9acf8c1e838d54c85b1cf1f9a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLRDQNFE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCN7ZMnP%2BXvCI0t%2BttbagTcvajUVzLOEL70q6PJIAoICQIhAIuamE5OabYrsz%2FA8xc7bGKb%2F874yXBq%2FbhV4lsiM9oGKv8DCCoQABoMNjM3NDIzMTgzODA1Igxn4ZMoHqmlHMMn7h4q3APUvRnBCRum%2BdEkhgHZWzRRKWS%2F1tEzyL0I%2FNeNwEN8JLr72x8ucwceHv7w9P%2FaVizm0KsGUD884IH3gE7csswAAyREGHKH%2FqYotU85a0WDBQgiCjypudFam2pBOx15IzQOIT7V2kstuj%2B68HSfs9hSUBFReJIl0x%2Bs3oSsbQ7DtVz8uGafN7%2FdsUJ%2FnnMOj5MO7unGgGjJoBYrg8VGf0tZ02HV5OgDn8lP4wFl%2BjED1S4ZXLtYaOXEJOouHyENfp7MWDYHhj%2BKoQLbVMehl6x9j1aBkmVifSJubcQQ%2FRBXF%2FANxdBTDlQJO4z9s7sLdhFG9GLwCJgL%2FqoL%2F71Q9YPvbC7pFxy3A3XWefWvv9Q0TZPFyFsNaOaACTpXU5vDyT%2FuKbrtrzLQJre50qBtoaovkCg9Bt3bzKNZWTUmmz%2Bsm2utG3e7VgHrB1a3p0dd%2FuMWp1cp7QUoTWYRWz5YwJ3KuZ8Esj2lWEpYUwFuzi%2FuVnKbSSX1hBkOtj1FqabvVAYGpBpfBxpBllQzSJC2kXJFfQe3VTYxkSx1NDITt92o63Rw2S3OtBi%2BfPu8%2B4XKH4OMfy5NkMWpdlo6IBe1qyJIsXFgHvEOCuIe3lDGbndZcyCoWmxUbHotgjG%2FhTCoroe9BjqkAalju6GiBkZoDo%2BDD2m3VTbWXPLuE0vc7zL11uo%2FOLhTKNMAdJ48kwzRsf94qFYhuijAON38FpabJPYffB36rT9UI34SrJCRG5n0dGkIL12FfjeP9KqPVtrO%2BBFrwoFVRf51f4Bo%2FWH18gT%2B8UJz%2Fc1useW9U4Wz4mpjLyTgnKThx8RgYG1L4lIlDDEeoAtDAj5GGwFjboXtbR%2Fz7vD9LUzql1Ls&X-Amz-Signature=f876cd441c193ae24f558a21b2a8e97ca65549db13b631e1f71ec61825d150b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BUG2SLX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIH3ZHpwtY5rjNL0Z7DXq73Jh5qmrV4ke8xjjetL0nswYAiEAsdZS5iQB%2B3qdo%2FdpsqyaGdiYMTfhKdjH6OIFaG5%2FDmQq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDJpCDpqfToYw%2B3bB%2FSrcA%2BNa4kGvw1KSTkrnYhYn8Cn2qzXm4nCVNU7abpQKtpSOji8TgFDSfr2vu3L5Uk4i%2BxJhFlKmo1tmi52msP6%2Fab9jV%2B6XF9U%2BvkKco4hxdamB6rYiXT6ZBVwcpGcZo%2F%2BcuuT2lWN%2BDhe1Ps8KkQuNsyGwNtZuZxP8qMnmZ1973SNba23cxzSUCxx%2F78KZYfjrRDuL7ottikLJJSm65RkDvh9ogkTz7qO4SkY%2F4ZIIr4zmFMpOq2KGEMAO0yVN%2BDhlaybVax5%2BZmMglTSA5lzJkcMLxuh7PCZyeIFWh9ATwPzkORf9jyLThXOVjLwBacwaDWN2eauVgUW%2FWqt1xA8%2BVTI48g5Cla4ppIL31hXheouGuiNVx1anM5wQOaftQfu97rQXn5O%2FRFzxE2pbn3roK2zJHmZc4zTasyvsZQh5hJvGONKTPkQcZO2IV%2Bj5DJjb1eXnNCO7OOOJ7NJTH%2FGxwsQqUhNP7wYDLET9p3BQGhfL94M6B2VgA6aG9YUfur8A4EGiaUNWdy2txsWx%2Fqecxk2zmrmbdoUxgFbF8IY%2B%2B49vfJLCkxqrWOIBNSX8JKt%2BDlxaAqoACazTo1g4vmfwg1zOiczxEQyUlq5XUnuhTLiMxEmbC6D8bq0YnPwTMOiuh70GOqUBs7zIsmzlUowctDh4JyY%2BuJP6mLEzv%2FUZCGEI64zuZM%2BdqGrCZ%2FCHYfK2Bge951jSBouNc3PWjgixbaR9vys8iN4juws8Az4QEVMSJhjvp8Xj04lkWCOVhLOoVrlzpsF%2FOZTr5PsTYdgVvf%2Fhh%2BEtaZtCkWvRy4ntubW62LhQ3TmijBPE%2BiEfjTGjl2gYRddISFmXvxKs12fpV5g5Eh0zMjFves4g&X-Amz-Signature=ee1c3589865ff0f37608c14683593f4af52d0f797b3b1ad6dd97816d6da25332&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BUG2SLX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIH3ZHpwtY5rjNL0Z7DXq73Jh5qmrV4ke8xjjetL0nswYAiEAsdZS5iQB%2B3qdo%2FdpsqyaGdiYMTfhKdjH6OIFaG5%2FDmQq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDJpCDpqfToYw%2B3bB%2FSrcA%2BNa4kGvw1KSTkrnYhYn8Cn2qzXm4nCVNU7abpQKtpSOji8TgFDSfr2vu3L5Uk4i%2BxJhFlKmo1tmi52msP6%2Fab9jV%2B6XF9U%2BvkKco4hxdamB6rYiXT6ZBVwcpGcZo%2F%2BcuuT2lWN%2BDhe1Ps8KkQuNsyGwNtZuZxP8qMnmZ1973SNba23cxzSUCxx%2F78KZYfjrRDuL7ottikLJJSm65RkDvh9ogkTz7qO4SkY%2F4ZIIr4zmFMpOq2KGEMAO0yVN%2BDhlaybVax5%2BZmMglTSA5lzJkcMLxuh7PCZyeIFWh9ATwPzkORf9jyLThXOVjLwBacwaDWN2eauVgUW%2FWqt1xA8%2BVTI48g5Cla4ppIL31hXheouGuiNVx1anM5wQOaftQfu97rQXn5O%2FRFzxE2pbn3roK2zJHmZc4zTasyvsZQh5hJvGONKTPkQcZO2IV%2Bj5DJjb1eXnNCO7OOOJ7NJTH%2FGxwsQqUhNP7wYDLET9p3BQGhfL94M6B2VgA6aG9YUfur8A4EGiaUNWdy2txsWx%2Fqecxk2zmrmbdoUxgFbF8IY%2B%2B49vfJLCkxqrWOIBNSX8JKt%2BDlxaAqoACazTo1g4vmfwg1zOiczxEQyUlq5XUnuhTLiMxEmbC6D8bq0YnPwTMOiuh70GOqUBs7zIsmzlUowctDh4JyY%2BuJP6mLEzv%2FUZCGEI64zuZM%2BdqGrCZ%2FCHYfK2Bge951jSBouNc3PWjgixbaR9vys8iN4juws8Az4QEVMSJhjvp8Xj04lkWCOVhLOoVrlzpsF%2FOZTr5PsTYdgVvf%2Fhh%2BEtaZtCkWvRy4ntubW62LhQ3TmijBPE%2BiEfjTGjl2gYRddISFmXvxKs12fpV5g5Eh0zMjFves4g&X-Amz-Signature=8d12c91afb823219733422148eb5b64405bd3fdf20dc2c031e0d57157d6137d9&X-Amz-SignedHeaders=host&x-id=GetObject)

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
