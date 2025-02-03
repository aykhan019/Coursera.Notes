

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UJU3KKL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1R%2FNYPBjnN5Wmy1ieQ1SVRGB%2BOF1kiKiuS85zuntDIAiBkfx0ai3qoLNnMqxJuhVVVT1PSTERLPMprG46uWeS6UCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl7yfPgJW1khqCXgDKtwDWc3hxeOiQQ0fHYW0n%2BZIVi%2FYKiZrBmcBAt9S6U2ZK%2BaNEFjQXQpnQBzy9NqXamOgFEnXH8fl%2FRAH8k%2F0fICuPmFvYSFXLTsr89iRK%2BsFIzikha%2BS%2FG3iwAOdevU5Ay9f7st5c4vmww6fDYSuHZQHZIO4inZDWz%2FK4LUfAID6NX%2FHfAzfFay05vPDkVhXV3TIZCh6bLveHS9RI4BQwybEchyyX%2F4h5NAoG30JSm7W5WvAcZTYGf5ScNXaxbCH7lVobl%2FRJAZlIyxe7dFnJo4xQrecdRtkJ2rF9VM%2BaOFkmuw%2B%2B7bpPKrUMRBY4KGufUSi%2FQsQEkG%2BVKh6Qd19B6i18e64HEYdSEhdhBypAwOVrQj3ylnzcPqQOFTMXo%2FfUnd83NFYUfLKDmTbJ3dA18xftPUQJX8fxpDYS6jw%2B%2FEq8VaUGXCNVE3W1gb6lqVGge0Zl4zjeA22F4HU%2F2nKgPYkAa0t5F2lgTl99UIJ7e1yLd1V0sLcDUm40uvtaAdKyPMZOW4ZCJhBqmTFHDP6MsJ6oqjTDjpiTyalc1y5DaOoRYbAOaSrQmjoYlzwRdCqQzZPIVy1I9PpZ7hkMJfKCNgdbvcyY22rLj%2F%2FqjtG4A03%2FjXz6mtRmB%2BBx9QCcHEwir%2BAvQY6pgFBjwGEi2XfPt5lHEaWFAqDhBHewY33VM8XftWD0Thz99cirdT45Q1ED0qktqB98HOWrNhZ%2FZRvxwDE8FcH9t1m9p6hGklal5RDoUOaBFFcPr1bSejy7HIf064oQmCVVe2REJ%2BMczbOnXbvKAYErD4eQ9PXDFvZ%2FmUhenful6IlcrgDslbdYlwE%2B%2FSDHss%2FjeWD4Zr6zDuQq46BWGZBGhtD0VuzEToN&X-Amz-Signature=ed503a452663d8d58a5a89229de29db5e63afaf19edd0542dd5741552fb2511f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UJU3KKL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1R%2FNYPBjnN5Wmy1ieQ1SVRGB%2BOF1kiKiuS85zuntDIAiBkfx0ai3qoLNnMqxJuhVVVT1PSTERLPMprG46uWeS6UCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl7yfPgJW1khqCXgDKtwDWc3hxeOiQQ0fHYW0n%2BZIVi%2FYKiZrBmcBAt9S6U2ZK%2BaNEFjQXQpnQBzy9NqXamOgFEnXH8fl%2FRAH8k%2F0fICuPmFvYSFXLTsr89iRK%2BsFIzikha%2BS%2FG3iwAOdevU5Ay9f7st5c4vmww6fDYSuHZQHZIO4inZDWz%2FK4LUfAID6NX%2FHfAzfFay05vPDkVhXV3TIZCh6bLveHS9RI4BQwybEchyyX%2F4h5NAoG30JSm7W5WvAcZTYGf5ScNXaxbCH7lVobl%2FRJAZlIyxe7dFnJo4xQrecdRtkJ2rF9VM%2BaOFkmuw%2B%2B7bpPKrUMRBY4KGufUSi%2FQsQEkG%2BVKh6Qd19B6i18e64HEYdSEhdhBypAwOVrQj3ylnzcPqQOFTMXo%2FfUnd83NFYUfLKDmTbJ3dA18xftPUQJX8fxpDYS6jw%2B%2FEq8VaUGXCNVE3W1gb6lqVGge0Zl4zjeA22F4HU%2F2nKgPYkAa0t5F2lgTl99UIJ7e1yLd1V0sLcDUm40uvtaAdKyPMZOW4ZCJhBqmTFHDP6MsJ6oqjTDjpiTyalc1y5DaOoRYbAOaSrQmjoYlzwRdCqQzZPIVy1I9PpZ7hkMJfKCNgdbvcyY22rLj%2F%2FqjtG4A03%2FjXz6mtRmB%2BBx9QCcHEwir%2BAvQY6pgFBjwGEi2XfPt5lHEaWFAqDhBHewY33VM8XftWD0Thz99cirdT45Q1ED0qktqB98HOWrNhZ%2FZRvxwDE8FcH9t1m9p6hGklal5RDoUOaBFFcPr1bSejy7HIf064oQmCVVe2REJ%2BMczbOnXbvKAYErD4eQ9PXDFvZ%2FmUhenful6IlcrgDslbdYlwE%2B%2FSDHss%2FjeWD4Zr6zDuQq46BWGZBGhtD0VuzEToN&X-Amz-Signature=c3edf35ac1dc9d0a603416baed888df9e26a82d1ab7d7dfcc2781e2129041cf6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UJU3KKL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1R%2FNYPBjnN5Wmy1ieQ1SVRGB%2BOF1kiKiuS85zuntDIAiBkfx0ai3qoLNnMqxJuhVVVT1PSTERLPMprG46uWeS6UCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl7yfPgJW1khqCXgDKtwDWc3hxeOiQQ0fHYW0n%2BZIVi%2FYKiZrBmcBAt9S6U2ZK%2BaNEFjQXQpnQBzy9NqXamOgFEnXH8fl%2FRAH8k%2F0fICuPmFvYSFXLTsr89iRK%2BsFIzikha%2BS%2FG3iwAOdevU5Ay9f7st5c4vmww6fDYSuHZQHZIO4inZDWz%2FK4LUfAID6NX%2FHfAzfFay05vPDkVhXV3TIZCh6bLveHS9RI4BQwybEchyyX%2F4h5NAoG30JSm7W5WvAcZTYGf5ScNXaxbCH7lVobl%2FRJAZlIyxe7dFnJo4xQrecdRtkJ2rF9VM%2BaOFkmuw%2B%2B7bpPKrUMRBY4KGufUSi%2FQsQEkG%2BVKh6Qd19B6i18e64HEYdSEhdhBypAwOVrQj3ylnzcPqQOFTMXo%2FfUnd83NFYUfLKDmTbJ3dA18xftPUQJX8fxpDYS6jw%2B%2FEq8VaUGXCNVE3W1gb6lqVGge0Zl4zjeA22F4HU%2F2nKgPYkAa0t5F2lgTl99UIJ7e1yLd1V0sLcDUm40uvtaAdKyPMZOW4ZCJhBqmTFHDP6MsJ6oqjTDjpiTyalc1y5DaOoRYbAOaSrQmjoYlzwRdCqQzZPIVy1I9PpZ7hkMJfKCNgdbvcyY22rLj%2F%2FqjtG4A03%2FjXz6mtRmB%2BBx9QCcHEwir%2BAvQY6pgFBjwGEi2XfPt5lHEaWFAqDhBHewY33VM8XftWD0Thz99cirdT45Q1ED0qktqB98HOWrNhZ%2FZRvxwDE8FcH9t1m9p6hGklal5RDoUOaBFFcPr1bSejy7HIf064oQmCVVe2REJ%2BMczbOnXbvKAYErD4eQ9PXDFvZ%2FmUhenful6IlcrgDslbdYlwE%2B%2FSDHss%2FjeWD4Zr6zDuQq46BWGZBGhtD0VuzEToN&X-Amz-Signature=7e60e4d2a47b79ae491a13c2ac9a804eaf32e0952a6566915ec8869bca123668&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQNIKGCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8GjTUD9KOqdPl64xIwgt3HpUM4Yy6PZeqbMVd8nUk3AiBqEF6945wxfveLnCYxEQKaMiGWMsQocE5kSRQU%2BB6K9CqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixeNGZHaR8w3TR2GKtwDldK9yfmOpjgbJ5xFE%2B1Uiz90yspKpDGEEigk335Q5hkA5W2sbeDgLbQMGVIr%2FlbVZcPCllkv6z4APzyts3fZTBMKcr3TTPDtmx5lWder4Jo1JMUjZ1NTyiYZXyenLGHC9fjvUyrT%2FKosn055OrhnHiQd9yBpivJbBUC6imoM6YLVWnB%2BY3a%2Bn%2FQtS2oz0zmRgKXmLe2Xeo5S56%2BpXesewpmL323jF%2BmtDWk%2BcBrei1gL%2FAzo%2BUF11lTwmPBJql4ZhaCor4j0kzjefLy4%2Bl7%2FJrarZwnUEXskixjuPebkmZMG%2F4%2Fk1lQJ4AZuX2T5t8plpCqUsK9R%2B69zY4jb0xsyomxKrUbGf7kIhU6on1IO2x8AeEIA%2Bm3%2FUApUrPrivI72uw%2FM%2BE8gS51SO6aXzQzkymRARHdCcOzqsccdBlZDlgK0xyzmkDlj9qKHmAGM5iZi%2FsEf7gMWCBfkL6edj54c4HNQRYOS6ty4KljNLujnU79fRL1at2jviAdurF0T%2FI%2B7COVqLQEfUXYW%2FtLGbjkS2FK1mtyYzPLFCFL%2BfAzi%2BYfQCXFMGOJ0P691mS4KYFYdG0Ih%2BDt4n1M16cQIThSFCesUyeXhs9Rs5DA0eNCw7s8qBR2%2B6Jq7OZ%2BkCmIwpr%2BAvQY6pgGZDfBfJcbk7Wk4dswpS6pThqKLlx3h4tGN22UzUgcQA9uy4%2B5vdeKo%2FqENUgy1wYVWqTPvq%2BgeP5RPj%2BHyD59MSREJVrf1%2FZOiDRXJ1ehUVXqCSCWoPsLhZeMesmNbdPyMDLsnpJmFwGqPN03zl7NyUAJRxDM1BHpdBpLJyI190goBwHCUBCyk7yJNjVqzWgmL3f%2BrZwTWuOSPhCzSK35FWnIP8YL0&X-Amz-Signature=a208fb82c3ab43a00bef8d48626f11ed168d671e49888aa230b0828bb226c692&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQNIKGCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8GjTUD9KOqdPl64xIwgt3HpUM4Yy6PZeqbMVd8nUk3AiBqEF6945wxfveLnCYxEQKaMiGWMsQocE5kSRQU%2BB6K9CqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixeNGZHaR8w3TR2GKtwDldK9yfmOpjgbJ5xFE%2B1Uiz90yspKpDGEEigk335Q5hkA5W2sbeDgLbQMGVIr%2FlbVZcPCllkv6z4APzyts3fZTBMKcr3TTPDtmx5lWder4Jo1JMUjZ1NTyiYZXyenLGHC9fjvUyrT%2FKosn055OrhnHiQd9yBpivJbBUC6imoM6YLVWnB%2BY3a%2Bn%2FQtS2oz0zmRgKXmLe2Xeo5S56%2BpXesewpmL323jF%2BmtDWk%2BcBrei1gL%2FAzo%2BUF11lTwmPBJql4ZhaCor4j0kzjefLy4%2Bl7%2FJrarZwnUEXskixjuPebkmZMG%2F4%2Fk1lQJ4AZuX2T5t8plpCqUsK9R%2B69zY4jb0xsyomxKrUbGf7kIhU6on1IO2x8AeEIA%2Bm3%2FUApUrPrivI72uw%2FM%2BE8gS51SO6aXzQzkymRARHdCcOzqsccdBlZDlgK0xyzmkDlj9qKHmAGM5iZi%2FsEf7gMWCBfkL6edj54c4HNQRYOS6ty4KljNLujnU79fRL1at2jviAdurF0T%2FI%2B7COVqLQEfUXYW%2FtLGbjkS2FK1mtyYzPLFCFL%2BfAzi%2BYfQCXFMGOJ0P691mS4KYFYdG0Ih%2BDt4n1M16cQIThSFCesUyeXhs9Rs5DA0eNCw7s8qBR2%2B6Jq7OZ%2BkCmIwpr%2BAvQY6pgGZDfBfJcbk7Wk4dswpS6pThqKLlx3h4tGN22UzUgcQA9uy4%2B5vdeKo%2FqENUgy1wYVWqTPvq%2BgeP5RPj%2BHyD59MSREJVrf1%2FZOiDRXJ1ehUVXqCSCWoPsLhZeMesmNbdPyMDLsnpJmFwGqPN03zl7NyUAJRxDM1BHpdBpLJyI190goBwHCUBCyk7yJNjVqzWgmL3f%2BrZwTWuOSPhCzSK35FWnIP8YL0&X-Amz-Signature=40c9f84750a373accfad445451b2949fec56ece9a2e0ec9bc713dedda22e25a6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQNIKGCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8GjTUD9KOqdPl64xIwgt3HpUM4Yy6PZeqbMVd8nUk3AiBqEF6945wxfveLnCYxEQKaMiGWMsQocE5kSRQU%2BB6K9CqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixeNGZHaR8w3TR2GKtwDldK9yfmOpjgbJ5xFE%2B1Uiz90yspKpDGEEigk335Q5hkA5W2sbeDgLbQMGVIr%2FlbVZcPCllkv6z4APzyts3fZTBMKcr3TTPDtmx5lWder4Jo1JMUjZ1NTyiYZXyenLGHC9fjvUyrT%2FKosn055OrhnHiQd9yBpivJbBUC6imoM6YLVWnB%2BY3a%2Bn%2FQtS2oz0zmRgKXmLe2Xeo5S56%2BpXesewpmL323jF%2BmtDWk%2BcBrei1gL%2FAzo%2BUF11lTwmPBJql4ZhaCor4j0kzjefLy4%2Bl7%2FJrarZwnUEXskixjuPebkmZMG%2F4%2Fk1lQJ4AZuX2T5t8plpCqUsK9R%2B69zY4jb0xsyomxKrUbGf7kIhU6on1IO2x8AeEIA%2Bm3%2FUApUrPrivI72uw%2FM%2BE8gS51SO6aXzQzkymRARHdCcOzqsccdBlZDlgK0xyzmkDlj9qKHmAGM5iZi%2FsEf7gMWCBfkL6edj54c4HNQRYOS6ty4KljNLujnU79fRL1at2jviAdurF0T%2FI%2B7COVqLQEfUXYW%2FtLGbjkS2FK1mtyYzPLFCFL%2BfAzi%2BYfQCXFMGOJ0P691mS4KYFYdG0Ih%2BDt4n1M16cQIThSFCesUyeXhs9Rs5DA0eNCw7s8qBR2%2B6Jq7OZ%2BkCmIwpr%2BAvQY6pgGZDfBfJcbk7Wk4dswpS6pThqKLlx3h4tGN22UzUgcQA9uy4%2B5vdeKo%2FqENUgy1wYVWqTPvq%2BgeP5RPj%2BHyD59MSREJVrf1%2FZOiDRXJ1ehUVXqCSCWoPsLhZeMesmNbdPyMDLsnpJmFwGqPN03zl7NyUAJRxDM1BHpdBpLJyI190goBwHCUBCyk7yJNjVqzWgmL3f%2BrZwTWuOSPhCzSK35FWnIP8YL0&X-Amz-Signature=d5af5f5103ef1df693a2f5a91ce8ec476b3732f29c81bb6721f013eb3714c553&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQNIKGCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8GjTUD9KOqdPl64xIwgt3HpUM4Yy6PZeqbMVd8nUk3AiBqEF6945wxfveLnCYxEQKaMiGWMsQocE5kSRQU%2BB6K9CqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixeNGZHaR8w3TR2GKtwDldK9yfmOpjgbJ5xFE%2B1Uiz90yspKpDGEEigk335Q5hkA5W2sbeDgLbQMGVIr%2FlbVZcPCllkv6z4APzyts3fZTBMKcr3TTPDtmx5lWder4Jo1JMUjZ1NTyiYZXyenLGHC9fjvUyrT%2FKosn055OrhnHiQd9yBpivJbBUC6imoM6YLVWnB%2BY3a%2Bn%2FQtS2oz0zmRgKXmLe2Xeo5S56%2BpXesewpmL323jF%2BmtDWk%2BcBrei1gL%2FAzo%2BUF11lTwmPBJql4ZhaCor4j0kzjefLy4%2Bl7%2FJrarZwnUEXskixjuPebkmZMG%2F4%2Fk1lQJ4AZuX2T5t8plpCqUsK9R%2B69zY4jb0xsyomxKrUbGf7kIhU6on1IO2x8AeEIA%2Bm3%2FUApUrPrivI72uw%2FM%2BE8gS51SO6aXzQzkymRARHdCcOzqsccdBlZDlgK0xyzmkDlj9qKHmAGM5iZi%2FsEf7gMWCBfkL6edj54c4HNQRYOS6ty4KljNLujnU79fRL1at2jviAdurF0T%2FI%2B7COVqLQEfUXYW%2FtLGbjkS2FK1mtyYzPLFCFL%2BfAzi%2BYfQCXFMGOJ0P691mS4KYFYdG0Ih%2BDt4n1M16cQIThSFCesUyeXhs9Rs5DA0eNCw7s8qBR2%2B6Jq7OZ%2BkCmIwpr%2BAvQY6pgGZDfBfJcbk7Wk4dswpS6pThqKLlx3h4tGN22UzUgcQA9uy4%2B5vdeKo%2FqENUgy1wYVWqTPvq%2BgeP5RPj%2BHyD59MSREJVrf1%2FZOiDRXJ1ehUVXqCSCWoPsLhZeMesmNbdPyMDLsnpJmFwGqPN03zl7NyUAJRxDM1BHpdBpLJyI190goBwHCUBCyk7yJNjVqzWgmL3f%2BrZwTWuOSPhCzSK35FWnIP8YL0&X-Amz-Signature=73b145d2b8ac08b0330a84f3026bd8aa9285ef1ea85d1134f93acc18d93c5e98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQNIKGCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8GjTUD9KOqdPl64xIwgt3HpUM4Yy6PZeqbMVd8nUk3AiBqEF6945wxfveLnCYxEQKaMiGWMsQocE5kSRQU%2BB6K9CqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixeNGZHaR8w3TR2GKtwDldK9yfmOpjgbJ5xFE%2B1Uiz90yspKpDGEEigk335Q5hkA5W2sbeDgLbQMGVIr%2FlbVZcPCllkv6z4APzyts3fZTBMKcr3TTPDtmx5lWder4Jo1JMUjZ1NTyiYZXyenLGHC9fjvUyrT%2FKosn055OrhnHiQd9yBpivJbBUC6imoM6YLVWnB%2BY3a%2Bn%2FQtS2oz0zmRgKXmLe2Xeo5S56%2BpXesewpmL323jF%2BmtDWk%2BcBrei1gL%2FAzo%2BUF11lTwmPBJql4ZhaCor4j0kzjefLy4%2Bl7%2FJrarZwnUEXskixjuPebkmZMG%2F4%2Fk1lQJ4AZuX2T5t8plpCqUsK9R%2B69zY4jb0xsyomxKrUbGf7kIhU6on1IO2x8AeEIA%2Bm3%2FUApUrPrivI72uw%2FM%2BE8gS51SO6aXzQzkymRARHdCcOzqsccdBlZDlgK0xyzmkDlj9qKHmAGM5iZi%2FsEf7gMWCBfkL6edj54c4HNQRYOS6ty4KljNLujnU79fRL1at2jviAdurF0T%2FI%2B7COVqLQEfUXYW%2FtLGbjkS2FK1mtyYzPLFCFL%2BfAzi%2BYfQCXFMGOJ0P691mS4KYFYdG0Ih%2BDt4n1M16cQIThSFCesUyeXhs9Rs5DA0eNCw7s8qBR2%2B6Jq7OZ%2BkCmIwpr%2BAvQY6pgGZDfBfJcbk7Wk4dswpS6pThqKLlx3h4tGN22UzUgcQA9uy4%2B5vdeKo%2FqENUgy1wYVWqTPvq%2BgeP5RPj%2BHyD59MSREJVrf1%2FZOiDRXJ1ehUVXqCSCWoPsLhZeMesmNbdPyMDLsnpJmFwGqPN03zl7NyUAJRxDM1BHpdBpLJyI190goBwHCUBCyk7yJNjVqzWgmL3f%2BrZwTWuOSPhCzSK35FWnIP8YL0&X-Amz-Signature=7fa0622e93165dcfce42e55a5939e2b8dfdf8b24f0c759e8be5b6ec748f62bf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQNIKGCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8GjTUD9KOqdPl64xIwgt3HpUM4Yy6PZeqbMVd8nUk3AiBqEF6945wxfveLnCYxEQKaMiGWMsQocE5kSRQU%2BB6K9CqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixeNGZHaR8w3TR2GKtwDldK9yfmOpjgbJ5xFE%2B1Uiz90yspKpDGEEigk335Q5hkA5W2sbeDgLbQMGVIr%2FlbVZcPCllkv6z4APzyts3fZTBMKcr3TTPDtmx5lWder4Jo1JMUjZ1NTyiYZXyenLGHC9fjvUyrT%2FKosn055OrhnHiQd9yBpivJbBUC6imoM6YLVWnB%2BY3a%2Bn%2FQtS2oz0zmRgKXmLe2Xeo5S56%2BpXesewpmL323jF%2BmtDWk%2BcBrei1gL%2FAzo%2BUF11lTwmPBJql4ZhaCor4j0kzjefLy4%2Bl7%2FJrarZwnUEXskixjuPebkmZMG%2F4%2Fk1lQJ4AZuX2T5t8plpCqUsK9R%2B69zY4jb0xsyomxKrUbGf7kIhU6on1IO2x8AeEIA%2Bm3%2FUApUrPrivI72uw%2FM%2BE8gS51SO6aXzQzkymRARHdCcOzqsccdBlZDlgK0xyzmkDlj9qKHmAGM5iZi%2FsEf7gMWCBfkL6edj54c4HNQRYOS6ty4KljNLujnU79fRL1at2jviAdurF0T%2FI%2B7COVqLQEfUXYW%2FtLGbjkS2FK1mtyYzPLFCFL%2BfAzi%2BYfQCXFMGOJ0P691mS4KYFYdG0Ih%2BDt4n1M16cQIThSFCesUyeXhs9Rs5DA0eNCw7s8qBR2%2B6Jq7OZ%2BkCmIwpr%2BAvQY6pgGZDfBfJcbk7Wk4dswpS6pThqKLlx3h4tGN22UzUgcQA9uy4%2B5vdeKo%2FqENUgy1wYVWqTPvq%2BgeP5RPj%2BHyD59MSREJVrf1%2FZOiDRXJ1ehUVXqCSCWoPsLhZeMesmNbdPyMDLsnpJmFwGqPN03zl7NyUAJRxDM1BHpdBpLJyI190goBwHCUBCyk7yJNjVqzWgmL3f%2BrZwTWuOSPhCzSK35FWnIP8YL0&X-Amz-Signature=2a90350ebaf25b008e22cc625f53f01c30f6c0967d06b5c9bca105fc4b483f75&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REHSSV33%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHp%2Bcpqftc2f4AIcGDvaLYyj%2Bzd%2B1uqpx32%2BCwvzfJzZAiBbpnmIycwNtRUOcvNhsCYoDx%2F6Vr8jyLSU2ahMVr5cDyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMktoXMLTSPaGLVF0gKtwD0swxIw6TFBBcQMh5glSObMEiMPAPOyOOtKiAcHGJEF1tAlx%2BTaGfXJMRQNMuVIHa2pnxhegFUON6RFlgovawglYDgcO%2FlWI8HRJYD07PWh%2BtQ8KFaqGCgZ%2FQ%2Fdut4puWMvOu8p398mot4N8infhrZ0B3fVFi3vJwhFFypBMl8QxDO%2BpkNf1mxBgjTVs1R406oAgw0use%2F3jiX44CzW9JD%2BPg98CEoXIQSDZoalbydA%2Bpbdne4cHQnzna4TjSmG4%2F2dTsruM3jio9JpigcJxIB2cHZgB9v8Ixxr2QQbMEGLseF9wNyORfNAJ4CtjvGwYpDeUc6xA5x%2BiWDDSK2qRR6wElhR%2FcvpQZl%2BtTAgx5KyugaTlF7zu%2F8GwWkxCyroH7qzYP4vDWlg06bH3QDMcyMN9WbsnbGr4%2B69%2BASrOxskB0oAM7HY9llaIZaBwKqVkgLdaYnfCRSV76iZUeXwP7U3j9Eg%2BibRZiEc%2F8R2yIFcB%2BK4yucPrf%2F2DTWG1TUlTjFzRezSSFK%2BHujAL9nfhplgZdJbbSUhbiwR7Rw1oCo4NMg%2FEyHnnX0tZ964UNL7mm3%2B%2FO6CompTJPMjJzQgBUPvp%2Bf0ZuROBouLt4wr0ptDHv1BySIuW3EOYDDkowub%2BAvQY6pgEK5bPnD1gp3FMH5Yg%2BWTjNgdJWFy7KZnly6ZIuOZZ4T2rLUjw94BOPP9t2tLjEgv2whIR9YDeknM5U%2BAnxqPQuWPQUk7etxxZGiYtQDa5Z07X0JtaZQAJjuq3Jg4cqoSAoBtvDIByc4f2e4V2LmvsopaPa267qh1Z9DKF2nAZz0Jl6Ahe5rAAFX2EUe9AgLibp2VHjYlFHTKO%2BKCdqCsoCf3cAPbe2&X-Amz-Signature=6dc66b949eae77978377fc167a72c7ffb8e11fa8a54bb68bd2ac6c917310dee4&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE6AWIJL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDz7hIqTQvy2Ggi9xjG6G7BasUWPa6IArRA4Qk32IRgFQIgbjF4c5bW%2BOhIXMY0fZLfk1hJdqnjAf%2FabuVw1GvRE7gqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM0WlneIUg3CULigOircA8yb5pH2pauHrnLJxTJZpiQjfgBJY472K7txIGefbRYRfQJtPQ8gDk6MUvTTYQXeBUn9V8vCtajPndeoMy3azHkaxSDpvv9szX9vPcdXR1%2B7TWnaSs58RQ45jF%2FEeRTqdHBPRUTQysE8J765d22PDbvFIGafUHQavdJNqzwAcaL0lmfEqxubJPg%2BBnjxmF5hF6DqWIMquXUbXbGXPbp01Yh5IU2AYIjOA%2FPwg2ElNbeZwdnRGnORWscWPA6WxcHszW9BOBl1MzKf6JkcbKtwVztSXKjNBPg1lDHJmbxUf9T4WFrPPkIPH8jSDjUasCRYFughIRR%2B0xhVJTtXQnksM9yBH3sBvBoK0MbNjv%2BXhITVmjZa863s%2Fzs6B4KZp%2Fjp%2F%2FhSepuVK12tCx0K8pPTJ7kS8gJ7JXUUZX3%2FkZOmlnxsOhkgZ4Sp6m0xwCHP9nbaJuC1J5sKcNfEXWvSgRTi88wLQWySs45VSPskmxZ19zhPHq0Nuq0NVyGahliYHklVaMcA4tMsPuCUtM8S12H3wwDS6O3xDUpZmc79VywQFiKCwxAs9uiJoKI2MmgDH4ecdvZGlfRrF%2B50yL6yTpU22gFGgMjDR0CzvEPqUpCFToNUhzAbcO6gYfcUJWGLMLi%2FgL0GOqUB%2FFOLbMW60xTB1H9Cnrql%2Bg1DV8IJy3Xvd8uFCFLBcVchN4iY99PpFKpJ8h%2B52aEvQv1v2ip%2FVVNlQGEyAr8LBOb%2FVDvsaUzRMcYX%2Bdd0UzNMewx%2Bbm5FEMCsEuv5ZYoaRSm71Y7rhuXPC5yXFVhHmAr5AlaIPJlRURCKLK3DMMm75%2FCQ%2FaKJmjxpLswMeLuyL4sVF78pUcDvPyz%2BvvltqMpM7Jlf&X-Amz-Signature=24661ec03a3e1efa3053d28596e32335a0c609f2bb0d954311765e618bda3754&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQNIKGCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8GjTUD9KOqdPl64xIwgt3HpUM4Yy6PZeqbMVd8nUk3AiBqEF6945wxfveLnCYxEQKaMiGWMsQocE5kSRQU%2BB6K9CqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixeNGZHaR8w3TR2GKtwDldK9yfmOpjgbJ5xFE%2B1Uiz90yspKpDGEEigk335Q5hkA5W2sbeDgLbQMGVIr%2FlbVZcPCllkv6z4APzyts3fZTBMKcr3TTPDtmx5lWder4Jo1JMUjZ1NTyiYZXyenLGHC9fjvUyrT%2FKosn055OrhnHiQd9yBpivJbBUC6imoM6YLVWnB%2BY3a%2Bn%2FQtS2oz0zmRgKXmLe2Xeo5S56%2BpXesewpmL323jF%2BmtDWk%2BcBrei1gL%2FAzo%2BUF11lTwmPBJql4ZhaCor4j0kzjefLy4%2Bl7%2FJrarZwnUEXskixjuPebkmZMG%2F4%2Fk1lQJ4AZuX2T5t8plpCqUsK9R%2B69zY4jb0xsyomxKrUbGf7kIhU6on1IO2x8AeEIA%2Bm3%2FUApUrPrivI72uw%2FM%2BE8gS51SO6aXzQzkymRARHdCcOzqsccdBlZDlgK0xyzmkDlj9qKHmAGM5iZi%2FsEf7gMWCBfkL6edj54c4HNQRYOS6ty4KljNLujnU79fRL1at2jviAdurF0T%2FI%2B7COVqLQEfUXYW%2FtLGbjkS2FK1mtyYzPLFCFL%2BfAzi%2BYfQCXFMGOJ0P691mS4KYFYdG0Ih%2BDt4n1M16cQIThSFCesUyeXhs9Rs5DA0eNCw7s8qBR2%2B6Jq7OZ%2BkCmIwpr%2BAvQY6pgGZDfBfJcbk7Wk4dswpS6pThqKLlx3h4tGN22UzUgcQA9uy4%2B5vdeKo%2FqENUgy1wYVWqTPvq%2BgeP5RPj%2BHyD59MSREJVrf1%2FZOiDRXJ1ehUVXqCSCWoPsLhZeMesmNbdPyMDLsnpJmFwGqPN03zl7NyUAJRxDM1BHpdBpLJyI190goBwHCUBCyk7yJNjVqzWgmL3f%2BrZwTWuOSPhCzSK35FWnIP8YL0&X-Amz-Signature=b3fd134b497e5a2e5b99dd9ae17655b9dd5be67644e414d19342c57a9d9dc8b1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQNIKGCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8GjTUD9KOqdPl64xIwgt3HpUM4Yy6PZeqbMVd8nUk3AiBqEF6945wxfveLnCYxEQKaMiGWMsQocE5kSRQU%2BB6K9CqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixeNGZHaR8w3TR2GKtwDldK9yfmOpjgbJ5xFE%2B1Uiz90yspKpDGEEigk335Q5hkA5W2sbeDgLbQMGVIr%2FlbVZcPCllkv6z4APzyts3fZTBMKcr3TTPDtmx5lWder4Jo1JMUjZ1NTyiYZXyenLGHC9fjvUyrT%2FKosn055OrhnHiQd9yBpivJbBUC6imoM6YLVWnB%2BY3a%2Bn%2FQtS2oz0zmRgKXmLe2Xeo5S56%2BpXesewpmL323jF%2BmtDWk%2BcBrei1gL%2FAzo%2BUF11lTwmPBJql4ZhaCor4j0kzjefLy4%2Bl7%2FJrarZwnUEXskixjuPebkmZMG%2F4%2Fk1lQJ4AZuX2T5t8plpCqUsK9R%2B69zY4jb0xsyomxKrUbGf7kIhU6on1IO2x8AeEIA%2Bm3%2FUApUrPrivI72uw%2FM%2BE8gS51SO6aXzQzkymRARHdCcOzqsccdBlZDlgK0xyzmkDlj9qKHmAGM5iZi%2FsEf7gMWCBfkL6edj54c4HNQRYOS6ty4KljNLujnU79fRL1at2jviAdurF0T%2FI%2B7COVqLQEfUXYW%2FtLGbjkS2FK1mtyYzPLFCFL%2BfAzi%2BYfQCXFMGOJ0P691mS4KYFYdG0Ih%2BDt4n1M16cQIThSFCesUyeXhs9Rs5DA0eNCw7s8qBR2%2B6Jq7OZ%2BkCmIwpr%2BAvQY6pgGZDfBfJcbk7Wk4dswpS6pThqKLlx3h4tGN22UzUgcQA9uy4%2B5vdeKo%2FqENUgy1wYVWqTPvq%2BgeP5RPj%2BHyD59MSREJVrf1%2FZOiDRXJ1ehUVXqCSCWoPsLhZeMesmNbdPyMDLsnpJmFwGqPN03zl7NyUAJRxDM1BHpdBpLJyI190goBwHCUBCyk7yJNjVqzWgmL3f%2BrZwTWuOSPhCzSK35FWnIP8YL0&X-Amz-Signature=4fc5eaa201276edc5a2b6321b67d8f1545ee912afde9f320981490987f532ad1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQNIKGCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8GjTUD9KOqdPl64xIwgt3HpUM4Yy6PZeqbMVd8nUk3AiBqEF6945wxfveLnCYxEQKaMiGWMsQocE5kSRQU%2BB6K9CqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMixeNGZHaR8w3TR2GKtwDldK9yfmOpjgbJ5xFE%2B1Uiz90yspKpDGEEigk335Q5hkA5W2sbeDgLbQMGVIr%2FlbVZcPCllkv6z4APzyts3fZTBMKcr3TTPDtmx5lWder4Jo1JMUjZ1NTyiYZXyenLGHC9fjvUyrT%2FKosn055OrhnHiQd9yBpivJbBUC6imoM6YLVWnB%2BY3a%2Bn%2FQtS2oz0zmRgKXmLe2Xeo5S56%2BpXesewpmL323jF%2BmtDWk%2BcBrei1gL%2FAzo%2BUF11lTwmPBJql4ZhaCor4j0kzjefLy4%2Bl7%2FJrarZwnUEXskixjuPebkmZMG%2F4%2Fk1lQJ4AZuX2T5t8plpCqUsK9R%2B69zY4jb0xsyomxKrUbGf7kIhU6on1IO2x8AeEIA%2Bm3%2FUApUrPrivI72uw%2FM%2BE8gS51SO6aXzQzkymRARHdCcOzqsccdBlZDlgK0xyzmkDlj9qKHmAGM5iZi%2FsEf7gMWCBfkL6edj54c4HNQRYOS6ty4KljNLujnU79fRL1at2jviAdurF0T%2FI%2B7COVqLQEfUXYW%2FtLGbjkS2FK1mtyYzPLFCFL%2BfAzi%2BYfQCXFMGOJ0P691mS4KYFYdG0Ih%2BDt4n1M16cQIThSFCesUyeXhs9Rs5DA0eNCw7s8qBR2%2B6Jq7OZ%2BkCmIwpr%2BAvQY6pgGZDfBfJcbk7Wk4dswpS6pThqKLlx3h4tGN22UzUgcQA9uy4%2B5vdeKo%2FqENUgy1wYVWqTPvq%2BgeP5RPj%2BHyD59MSREJVrf1%2FZOiDRXJ1ehUVXqCSCWoPsLhZeMesmNbdPyMDLsnpJmFwGqPN03zl7NyUAJRxDM1BHpdBpLJyI190goBwHCUBCyk7yJNjVqzWgmL3f%2BrZwTWuOSPhCzSK35FWnIP8YL0&X-Amz-Signature=f7405b49ab42f6f20f0f937cc0a762b44e6a9402ca2ee5ee0d77953231b4fb5b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AFIKTKN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZFLu%2FZg1fR5GnFzJadj2FIujceBuLakmKoYE0H%2FSgsgIgCeYetof7qZXl7oU8vVUOT%2FcAXGqhLz%2BiHysacXJ02vkqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKqRG0%2FHzsNKem8doyrcA4uD6OPPlyzuMxq95IrEV5%2FKurEv6iCmgohTZt7JWRXRRtzBKnPqvDmp99UhY%2BnkxsweqrtWDWKmRzOZXe2xb%2FmYVhECUUrsxXZWOHjsgzoQVnIBtleaneFEiVM6D8MgCyM6U7Y71nBxRivP9MLHFok%2BMEqY4wXBiZS%2BWhmexDFhgMi%2F6N3%2FcgMnacCtlPiuUY6h9agqDZMh1Xqx33PirHXyXj6G7w56HwPNuvc8xrZSNhEnlVVKO4epId%2BEXfJW%2BBjy3iXMWoRCBLePR%2FX28dptFi5KbUGuwy6xqu94jYdMWsYoYCuaJwupZomUVxLgZYkmBvk8J8XjSegBxTfEW2WlBtvaT1C1xHcV%2BhR4tAlHZolXlnUUsWOSoN3AHLAVOpNDD%2FlYw%2FKrZXtMqPn47OscGQOVJqr27Ilj1zul8XS0UeNJAJBYwf031MR%2Fsv5omqVCWzj0JTuhzXvXB%2BlxPdf2CuDk0iyWc4BrugGlEFVs76ctm7Pqt8%2BlLVDnu1M5aTOdRPdQMaYJfDOMh0MNaW7lfzWyT58nn4dHs2ZumcqM786m8ilLOQN7JgYvNi6%2FvdUO0QoF1NYSpH%2F%2B2LNtblSPsZtjKpPA6KA%2FEet2NOjncpeKQED805%2BEXMmTMMq%2FgL0GOqUBICDVNaz2JMchlOpgbDucT6BPtnk8zeR0rLbQoBOtKQOJJRFw%2BBFmYxVyoUpUBESO6CYNuNGN2bejmkOhLhVzn4%2BWZvT2UjtxvOest17RWJTDFg4wA%2BToAwCNlKhAaTj6KwA68s7C5eBz%2Bj16H010NHznJFLNXOe%2FuBMRv4fctRJnZKBr%2BdK0%2Bw7aopYMGnPBR41jT5IfEr%2Fbng%2BFVBLt4Fyh%2FWuo&X-Amz-Signature=ce31f27d4d9cc1942ff0288612a2cd97c5a0ba8c381ea69de500175e6f426f44&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3QIFJUL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEIueBkoPxpuR23SNMMxzAiwgryQRHigCWRQ%2B5W%2BZhxXAiEAm8qabJQgTa5VKoqAXfRNnI6pr1wvgtzYS%2Fz4vecgI9oqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNjo3XqaVa0wlOc3aCrcAwZKnukQfKUCoNNzlRuesZdT%2Bx7LWN7ZpqgSUYlRetmPmpJ5HYXXCswHqK8m7jv1S4uxCLb%2BsBMhurCfSF1VhmfvCVkiaF%2B1qy%2B%2BOENgsQ8CYhO5c5gg7XqOrYgNXZyTo%2BsAxjwvIWaBMbAS5bZyX3ZmiccSj9lS47bVa1qlqWzABsT%2B02PRyIHzFq8SvzbYBztqo%2BIYyCCHpgxm3vDugTLhpcANiBE%2FxOuUUC4TRQWV%2B6nypl3hEqmpfVoYoRZwtE7BAoBzl9vMJZzRCZ%2FmukWjoQPD9Yn1HY4L6jJJl%2BjrCfmPd11mOQZ%2BxOKzF%2BsL4z17tRDrQ9hb876hkfrt4ySpfhSSxz%2B7SA1Nk0mTwwCKb%2Fch5Q9XOW%2FDsWkXczBAKQXTtiMVM%2F83rCKwLJ34tSRhiRyaR%2BE3bSCn6TcTRXrHKIaepcDQBJuH1rmh%2B2z9P7YjBOvnwsQX%2BoQdJJyos2wTZjiEwMZgl7%2B2WFmKwOE0nKq5cvwpWORnbk0RuuMA19AKp6B4UWpYVqOAikXvsrSvb9b1fkKv8pJefn53uX%2BjgfJosmZZ2Gv08M5DWZIpLdBaHG7%2B9XW0LEF0%2FIYYVNIZSE8DniPZRRVWNl3TUxH7jPQPeF4xyv6OkNSfML3AgL0GOqUB7AZfS01ySSxkKHqWpRPkdcAbqK1BJivlDbs7Wi2rrS2Hb7u5gMbNuqYHYQ%2F%2FjF9MsLX9%2FjJ6W6KBS01wherJ3woKJ8nA0Md%2FjRc%2Bpw7qETemx1MY5UNVkXHaBZjC9ufkpyfXQLzOos4yrse7f5zVLiFV6QKKwsK60l8DEgXxNTA3Bla8SZ0BFhTO5VCCPelVN2%2FNPBncMET7mO%2Feg9DoOGeZIbm5&X-Amz-Signature=51a128e03a58fe2b13b558d595b55dbf6a151e501228c3b15cd2f9606af4094d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M6HIKIL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClWd7xqqeISi9mrADSHcfGRKkrV1qdvxJLwO%2FzcoLOkAiBIX8K%2BGYGxnwfpPaS0ap9lRI71HLfjpPmhDU4yqPS3tyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMk9UsseU2jgJg%2F6yHKtwDywyXXIQ3dBaYcKPrKdka8xOCESljRlqVl54KLnSXQcs6oyfcwxdJSVxe9LB0YsLInwKJPM1dejsyHgzI45aCA%2FB6Y77fwWZ1kWHR9hsO%2BIbRhHfHIZLShzk0YF9QqGkKgi2sGUSloDCwI7DwSl069wRDdNZ35av2eTz8LGYTOzZQLgEwWZG0rMKSlMd8g90woofFDENIB%2BBsExhRgylpp1MYlPOBFV08MzO55wN1YplJhEtgedIVgV00c05T7Qel%2FZTV5yxjGoWGpviqFb2dd6W9%2BdPsF5SsURgSOik5NqCO4BbV%2B1%2BwZUWSBVH6d%2BTJ9A8QOgdlEAhrR3WCLb6WQuWrxmSysuIkabi8HNpvp2qHtN%2FZclD6IkK7H8Qj%2B07cCtJVNx2gSkF1bYH%2FWbyDb6MjLNJ4LlASMrH1IEGX71MkmFxrJ9gx4kR5QTfsq3SZS5eY0ko3SxjGQ82pR3lFWgGvVdXb%2BXSF0%2F9%2B2thiSbl%2F8vlnO2agdJze7z5jkTWi5cB%2FEcWFnBVAibqIRs2AJqVPtkRGMAzZISRux5vVZ8VlRPolIFkD9o6MMnj2lDq5Yn3%2Bw1ASUgT%2FomJRWHDV9fLFU3Hj9HQcgYQ9NyCTnxcA8zULOR1335cO%2B54wwr%2BAvQY6pgEYjAOYigtszqK98hJnC4WnV6Ra9q39ZQ%2BbKSftURsNx235uK8aaXSgHSdtecvrbvaw4o0eQpxFEDsnPC88mTAd%2F2Sj9Pj4PFt58ks%2Be%2Fbccq2NUQH3z9Z4YA%2BrlDIKFn3PhfioxxQ7WqFFCoOd%2F0Yl0heIWZoVQ2%2FBgM40n9mEuM9Ezmy%2BGxG%2BzhRF2OAv5mFDkFwXM6%2BsI4AQwq30PIiIh%2FjZks%2Bi&X-Amz-Signature=5e20d421ede977eb066bcfe7375fc2d6b5ecc7eb6602873929bd370a61078fb5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBAXS7PK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6VYbMj6gmvWBd7%2BV56l1etPAaPl6pwLW2jAp8YtYVZAiEAg6J1VU23rZSIILHukNFODIvhckuwd0jX35X5leQO2DoqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEg%2F8sbD13WEP9iaEyrcA56Sa9Zjy83qY2qUfmdLlRbwrnHawcxFZv4O4IMmzglyqL7C6o%2FcrR0FgsGkXrn7bqxDghOqB39L1xP1VnlMJQm2t6dvvwz4aNJ0Tf2ZIT73r8o7BeWw62khQWqZZj3AVMD7tmIWlPNef4zJTVsVz62ASgd7C1zTVNTCUNgX0dRvmgZ38CIWypiGgCJdWNj%2FLqB0XrbNGpVGCdGduI5xliPcoy%2FGQG7xdJzzq0QQduTRozpgdWYeR5Cr%2BUlG5oijSidN6GxDUtNClKaDw%2F3c30vNw2Og0VWlMTbLVWpmFtGvcKnHlyUwxUf5WyQ6vBNqZ4Uyw%2FeIVfYOpZXfmkaXfum79%2BjZwyBnBR95VquNKXxGZ67BNftrzxB3Z40e%2FZh9bdvvqjipbplEbi76sXyRoQhG0Blmca3ZBWFqayOYVDWRMv7SW782%2FsdID9I%2Futv7o%2BsiDL69z53WByySug3EF4q%2BLbz2K85I2GbXZ6EmM3brsSVtG5q08KU%2FgVJxsVI%2FKCCfqRFSSf3DRWpHYQ24NYfklm21%2FpkKsvqc7pT%2F54riAVWZ7L7lweQ7ANzDzQYwnD81iBJgXQObPBQcNlx8SEfq5lgGntpdVUeammoLvvLBhI%2Fd3vHOPnIyLbPyMLW%2FgL0GOqUBjXv0E08y4simvINzZb%2Bz%2Ftv4AT5ASZpMOQr4J8%2F2uUd0bveqEFn7KHZu8BcbOsftCG5QigISlcDokyh1SOyXgGMQbfZZQXvZGHOon3clMTJgI5vl67iJ5ZT26gzFejzDDgbf8hcvPWEm%2FbjhGJDkP91KmpcCJOyp2%2BT4qcXwLx26d3UbRireS9TOypHIjUInUmlTzOXjKagUsbOrm8%2FQEETF%2Fo3k&X-Amz-Signature=677dc69ad8b03b16890b152a36ee5211f207bab8c2e7f62a533b56962cffc0ea&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBAXS7PK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6VYbMj6gmvWBd7%2BV56l1etPAaPl6pwLW2jAp8YtYVZAiEAg6J1VU23rZSIILHukNFODIvhckuwd0jX35X5leQO2DoqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEg%2F8sbD13WEP9iaEyrcA56Sa9Zjy83qY2qUfmdLlRbwrnHawcxFZv4O4IMmzglyqL7C6o%2FcrR0FgsGkXrn7bqxDghOqB39L1xP1VnlMJQm2t6dvvwz4aNJ0Tf2ZIT73r8o7BeWw62khQWqZZj3AVMD7tmIWlPNef4zJTVsVz62ASgd7C1zTVNTCUNgX0dRvmgZ38CIWypiGgCJdWNj%2FLqB0XrbNGpVGCdGduI5xliPcoy%2FGQG7xdJzzq0QQduTRozpgdWYeR5Cr%2BUlG5oijSidN6GxDUtNClKaDw%2F3c30vNw2Og0VWlMTbLVWpmFtGvcKnHlyUwxUf5WyQ6vBNqZ4Uyw%2FeIVfYOpZXfmkaXfum79%2BjZwyBnBR95VquNKXxGZ67BNftrzxB3Z40e%2FZh9bdvvqjipbplEbi76sXyRoQhG0Blmca3ZBWFqayOYVDWRMv7SW782%2FsdID9I%2Futv7o%2BsiDL69z53WByySug3EF4q%2BLbz2K85I2GbXZ6EmM3brsSVtG5q08KU%2FgVJxsVI%2FKCCfqRFSSf3DRWpHYQ24NYfklm21%2FpkKsvqc7pT%2F54riAVWZ7L7lweQ7ANzDzQYwnD81iBJgXQObPBQcNlx8SEfq5lgGntpdVUeammoLvvLBhI%2Fd3vHOPnIyLbPyMLW%2FgL0GOqUBjXv0E08y4simvINzZb%2Bz%2Ftv4AT5ASZpMOQr4J8%2F2uUd0bveqEFn7KHZu8BcbOsftCG5QigISlcDokyh1SOyXgGMQbfZZQXvZGHOon3clMTJgI5vl67iJ5ZT26gzFejzDDgbf8hcvPWEm%2FbjhGJDkP91KmpcCJOyp2%2BT4qcXwLx26d3UbRireS9TOypHIjUInUmlTzOXjKagUsbOrm8%2FQEETF%2Fo3k&X-Amz-Signature=b7da9af52a0de3bdc7efeed930049645cdcfd7cb8b1ff090e7631d7fa667f7fc&X-Amz-SignedHeaders=host&x-id=GetObject)

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
