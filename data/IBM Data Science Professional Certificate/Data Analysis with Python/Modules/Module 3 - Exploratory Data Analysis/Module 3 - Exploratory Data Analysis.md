

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PTM6ABX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJDy4UbClFTLpFEFWrD2GoOTpDHCq8dpdLFHhzEeXhvAiAPdEC9Uc9R%2F9l%2BczjW9sSgmOWc102EXVlcA%2Fg0HKPlsCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM3e3137AQ8Trk5UxXKtwDVeUhtFL%2FAYJxLNXN5vn7BJYPmRAkn4SK6BS96EhMyHYDPGjL%2BDzOzLhWRjSA9MG6raprscNp%2BW234VIOzy4BazEq9n%2BWngtpblqRyjEheNBIHhFVjodAyqb%2BPyNt22ohEAzVxodX%2B811TaY3GNoTkHZOjvH1AD%2FVUWW61pJBm0%2B1ePXqmzKMdm9QXq2sqjx7BzbdrXiJMXrH5Pa%2BySZ8xTr2VesqgeoddUYNEEPJ52JTgSkZ9YlkFXyunqgdTIzF0flUK6JMyaMabnGSwT3HqHupw7TyF5apP3xg%2B3%2Bc6bMDLQQ7XkrlaSstvZWzTcKM%2BEq2xjzlnlxekpLQB9caf92y4iKyXho4jn2%2FjpJm4ebmmfYQoHbDGovZs%2BivHIXU0SO%2B2Td3boA3yZ%2B12BCJg3U2Zsjbhysh5WAbyO0NqzN6zNq1X39O1arZcnQ3Gh4260YOOCTyZFNaVo%2F4b%2BAuZphd4aEPjGJesbSbij3sfj5slndzNVIJ2S0UEgQ8hZRECy%2F0nw%2B0%2F%2BEZCSL%2BdrhsCZtc4Wz9xY%2FP1q6%2Fa0J0nMiBQShO7Tb4cWFM18CJpfHKuk2gFP7SDp27Zm%2BgVIPJ6fNddb2aWWq8CbJaLTwzsGuXCH7vY7zKxERBboMw2vOBvQY6pgEHteKr694XbAVlVbuoyXGGeNrht4YZxHFGrA8d0UvVWT5L%2F0K8C%2F148Nmi8pN8NUGVP7zfxz%2B5%2B7i0ZpvKDtMH9ZOBw%2F8NDEmEQB72%2B%2BqmDfwDcJBd5vjWrzSAKkf7mb0Ojd3C2HeHKd46zVGbmGY03HMiINP%2FGluFkzaVvRQ8efUYleNyRKDzkdcwhMIE91Vh4uGKRnoVMAz3yZtm00ZZP3THNNnh&X-Amz-Signature=97a458ea72838dd19e06fa4458df470ddc9750cd7540b87cb360dc696dd174b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PTM6ABX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJDy4UbClFTLpFEFWrD2GoOTpDHCq8dpdLFHhzEeXhvAiAPdEC9Uc9R%2F9l%2BczjW9sSgmOWc102EXVlcA%2Fg0HKPlsCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM3e3137AQ8Trk5UxXKtwDVeUhtFL%2FAYJxLNXN5vn7BJYPmRAkn4SK6BS96EhMyHYDPGjL%2BDzOzLhWRjSA9MG6raprscNp%2BW234VIOzy4BazEq9n%2BWngtpblqRyjEheNBIHhFVjodAyqb%2BPyNt22ohEAzVxodX%2B811TaY3GNoTkHZOjvH1AD%2FVUWW61pJBm0%2B1ePXqmzKMdm9QXq2sqjx7BzbdrXiJMXrH5Pa%2BySZ8xTr2VesqgeoddUYNEEPJ52JTgSkZ9YlkFXyunqgdTIzF0flUK6JMyaMabnGSwT3HqHupw7TyF5apP3xg%2B3%2Bc6bMDLQQ7XkrlaSstvZWzTcKM%2BEq2xjzlnlxekpLQB9caf92y4iKyXho4jn2%2FjpJm4ebmmfYQoHbDGovZs%2BivHIXU0SO%2B2Td3boA3yZ%2B12BCJg3U2Zsjbhysh5WAbyO0NqzN6zNq1X39O1arZcnQ3Gh4260YOOCTyZFNaVo%2F4b%2BAuZphd4aEPjGJesbSbij3sfj5slndzNVIJ2S0UEgQ8hZRECy%2F0nw%2B0%2F%2BEZCSL%2BdrhsCZtc4Wz9xY%2FP1q6%2Fa0J0nMiBQShO7Tb4cWFM18CJpfHKuk2gFP7SDp27Zm%2BgVIPJ6fNddb2aWWq8CbJaLTwzsGuXCH7vY7zKxERBboMw2vOBvQY6pgEHteKr694XbAVlVbuoyXGGeNrht4YZxHFGrA8d0UvVWT5L%2F0K8C%2F148Nmi8pN8NUGVP7zfxz%2B5%2B7i0ZpvKDtMH9ZOBw%2F8NDEmEQB72%2B%2BqmDfwDcJBd5vjWrzSAKkf7mb0Ojd3C2HeHKd46zVGbmGY03HMiINP%2FGluFkzaVvRQ8efUYleNyRKDzkdcwhMIE91Vh4uGKRnoVMAz3yZtm00ZZP3THNNnh&X-Amz-Signature=510cbe97f27af794c159be8a80ae0b4b94b1a176433bc13f508a405f19ad598c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PTM6ABX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJDy4UbClFTLpFEFWrD2GoOTpDHCq8dpdLFHhzEeXhvAiAPdEC9Uc9R%2F9l%2BczjW9sSgmOWc102EXVlcA%2Fg0HKPlsCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIM3e3137AQ8Trk5UxXKtwDVeUhtFL%2FAYJxLNXN5vn7BJYPmRAkn4SK6BS96EhMyHYDPGjL%2BDzOzLhWRjSA9MG6raprscNp%2BW234VIOzy4BazEq9n%2BWngtpblqRyjEheNBIHhFVjodAyqb%2BPyNt22ohEAzVxodX%2B811TaY3GNoTkHZOjvH1AD%2FVUWW61pJBm0%2B1ePXqmzKMdm9QXq2sqjx7BzbdrXiJMXrH5Pa%2BySZ8xTr2VesqgeoddUYNEEPJ52JTgSkZ9YlkFXyunqgdTIzF0flUK6JMyaMabnGSwT3HqHupw7TyF5apP3xg%2B3%2Bc6bMDLQQ7XkrlaSstvZWzTcKM%2BEq2xjzlnlxekpLQB9caf92y4iKyXho4jn2%2FjpJm4ebmmfYQoHbDGovZs%2BivHIXU0SO%2B2Td3boA3yZ%2B12BCJg3U2Zsjbhysh5WAbyO0NqzN6zNq1X39O1arZcnQ3Gh4260YOOCTyZFNaVo%2F4b%2BAuZphd4aEPjGJesbSbij3sfj5slndzNVIJ2S0UEgQ8hZRECy%2F0nw%2B0%2F%2BEZCSL%2BdrhsCZtc4Wz9xY%2FP1q6%2Fa0J0nMiBQShO7Tb4cWFM18CJpfHKuk2gFP7SDp27Zm%2BgVIPJ6fNddb2aWWq8CbJaLTwzsGuXCH7vY7zKxERBboMw2vOBvQY6pgEHteKr694XbAVlVbuoyXGGeNrht4YZxHFGrA8d0UvVWT5L%2F0K8C%2F148Nmi8pN8NUGVP7zfxz%2B5%2B7i0ZpvKDtMH9ZOBw%2F8NDEmEQB72%2B%2BqmDfwDcJBd5vjWrzSAKkf7mb0Ojd3C2HeHKd46zVGbmGY03HMiINP%2FGluFkzaVvRQ8efUYleNyRKDzkdcwhMIE91Vh4uGKRnoVMAz3yZtm00ZZP3THNNnh&X-Amz-Signature=fa7e4b0063b557aa0083e3315f41eb2940b3647f2d8293f6c0a3e0735199966e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQJDHYU7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIVh3fBi6GAUmpNIdVEXWgYGSYhDz0DplkgUH9s%2FXekwIgBfQhVj9C1HPEKnzXz3zZE0qFX5XGq5Y1X2xzt3hKiAIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHZtLvfVxVjTRKJlCSrcA%2B0OgQdKbadHuqMVWABlXSTOfjTfudCxW8FYwkwsnRm3PlSht33mpOijtHLqzaOVfdMHHe%2FMApLUw9Z8p%2B5lmJWXrZoVapZCqFUlgfSK12USeHAfG%2BFMJ29%2FCdheOcamUXwyAwGHQKvu481pLPG2RSJGtkrGrbYpbTwZlktcuih68ZwKzmOciKAH%2FxFnHQtVqxTHdNEaFA%2FnPhSgghFINMRRGme8iBwHOpwrGVmFxP7HuJE0EQFE3JmNP%2FXHkxx5G8PDENoZYqf2RPxprNZGhvyQQi1W68UcHlKbSTZs%2FfhG5dF5G5qJcjqKXVzri8pmSCtpPrqnJiI2ryI74TGo43T23fN8%2FPO%2Fc71x8qJYh4YVXtgmOrI4uZXMCLkIOvVDCnVxLWviWisCkb7U7S3NUyWcS8GU2w%2FnNK9h2S29jJ1p5ihvDvQ%2FrSP5fd0E34CMznsAxvwiyzMN804AT%2F05D3TvhDh91EeAEPaJZ4qWKgTliR87gA6%2FoYdoqv4YfzzJu9SjFPCHvuvwJMR1pe65ISTHdznFAMgLl1nzpTbFFdl2y3eV6R7i88IjftK4z%2FzCi6Ogzk2dvXU4J%2Blt0nyPkiKCi325yM2UGMaXzmER1KkSYXbkm9yzPaKa7OUnMKjzgb0GOqUBP3l1xt2MHvMryMq6gpsr7ND64zS1dHjBuDfUW%2B2oKca0rjrnM%2BK7Sm5C6jVwoeNqsZV%2FWgd300ftrvQMEOAW1ewTb98P7ehgKP0Cvz8nHADvjlskrAVYot3k%2BDjermyPHID1V7oNix%2FJsDKRY8sXyXJJGznAviput0URI2JlSWLCrZCl6zRwzcO57WYecyiltD6xlaNUKYH6FCi8CZTi8JfU%2BP0T&X-Amz-Signature=52f11164df8ca90617b48f4868a4aa6572f213be44b0d63fb45f858f9959b0ee&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQJDHYU7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIVh3fBi6GAUmpNIdVEXWgYGSYhDz0DplkgUH9s%2FXekwIgBfQhVj9C1HPEKnzXz3zZE0qFX5XGq5Y1X2xzt3hKiAIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHZtLvfVxVjTRKJlCSrcA%2B0OgQdKbadHuqMVWABlXSTOfjTfudCxW8FYwkwsnRm3PlSht33mpOijtHLqzaOVfdMHHe%2FMApLUw9Z8p%2B5lmJWXrZoVapZCqFUlgfSK12USeHAfG%2BFMJ29%2FCdheOcamUXwyAwGHQKvu481pLPG2RSJGtkrGrbYpbTwZlktcuih68ZwKzmOciKAH%2FxFnHQtVqxTHdNEaFA%2FnPhSgghFINMRRGme8iBwHOpwrGVmFxP7HuJE0EQFE3JmNP%2FXHkxx5G8PDENoZYqf2RPxprNZGhvyQQi1W68UcHlKbSTZs%2FfhG5dF5G5qJcjqKXVzri8pmSCtpPrqnJiI2ryI74TGo43T23fN8%2FPO%2Fc71x8qJYh4YVXtgmOrI4uZXMCLkIOvVDCnVxLWviWisCkb7U7S3NUyWcS8GU2w%2FnNK9h2S29jJ1p5ihvDvQ%2FrSP5fd0E34CMznsAxvwiyzMN804AT%2F05D3TvhDh91EeAEPaJZ4qWKgTliR87gA6%2FoYdoqv4YfzzJu9SjFPCHvuvwJMR1pe65ISTHdznFAMgLl1nzpTbFFdl2y3eV6R7i88IjftK4z%2FzCi6Ogzk2dvXU4J%2Blt0nyPkiKCi325yM2UGMaXzmER1KkSYXbkm9yzPaKa7OUnMKjzgb0GOqUBP3l1xt2MHvMryMq6gpsr7ND64zS1dHjBuDfUW%2B2oKca0rjrnM%2BK7Sm5C6jVwoeNqsZV%2FWgd300ftrvQMEOAW1ewTb98P7ehgKP0Cvz8nHADvjlskrAVYot3k%2BDjermyPHID1V7oNix%2FJsDKRY8sXyXJJGznAviput0URI2JlSWLCrZCl6zRwzcO57WYecyiltD6xlaNUKYH6FCi8CZTi8JfU%2BP0T&X-Amz-Signature=7f21840f2047f7880f1591273cbc130dfc9a92948ece987ac53c5d45c3a6598c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQJDHYU7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIVh3fBi6GAUmpNIdVEXWgYGSYhDz0DplkgUH9s%2FXekwIgBfQhVj9C1HPEKnzXz3zZE0qFX5XGq5Y1X2xzt3hKiAIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHZtLvfVxVjTRKJlCSrcA%2B0OgQdKbadHuqMVWABlXSTOfjTfudCxW8FYwkwsnRm3PlSht33mpOijtHLqzaOVfdMHHe%2FMApLUw9Z8p%2B5lmJWXrZoVapZCqFUlgfSK12USeHAfG%2BFMJ29%2FCdheOcamUXwyAwGHQKvu481pLPG2RSJGtkrGrbYpbTwZlktcuih68ZwKzmOciKAH%2FxFnHQtVqxTHdNEaFA%2FnPhSgghFINMRRGme8iBwHOpwrGVmFxP7HuJE0EQFE3JmNP%2FXHkxx5G8PDENoZYqf2RPxprNZGhvyQQi1W68UcHlKbSTZs%2FfhG5dF5G5qJcjqKXVzri8pmSCtpPrqnJiI2ryI74TGo43T23fN8%2FPO%2Fc71x8qJYh4YVXtgmOrI4uZXMCLkIOvVDCnVxLWviWisCkb7U7S3NUyWcS8GU2w%2FnNK9h2S29jJ1p5ihvDvQ%2FrSP5fd0E34CMznsAxvwiyzMN804AT%2F05D3TvhDh91EeAEPaJZ4qWKgTliR87gA6%2FoYdoqv4YfzzJu9SjFPCHvuvwJMR1pe65ISTHdznFAMgLl1nzpTbFFdl2y3eV6R7i88IjftK4z%2FzCi6Ogzk2dvXU4J%2Blt0nyPkiKCi325yM2UGMaXzmER1KkSYXbkm9yzPaKa7OUnMKjzgb0GOqUBP3l1xt2MHvMryMq6gpsr7ND64zS1dHjBuDfUW%2B2oKca0rjrnM%2BK7Sm5C6jVwoeNqsZV%2FWgd300ftrvQMEOAW1ewTb98P7ehgKP0Cvz8nHADvjlskrAVYot3k%2BDjermyPHID1V7oNix%2FJsDKRY8sXyXJJGznAviput0URI2JlSWLCrZCl6zRwzcO57WYecyiltD6xlaNUKYH6FCi8CZTi8JfU%2BP0T&X-Amz-Signature=b91e15fd61b627c997e0d3981b486c9c427d2bae00af5c846e94619569ac215f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQJDHYU7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIVh3fBi6GAUmpNIdVEXWgYGSYhDz0DplkgUH9s%2FXekwIgBfQhVj9C1HPEKnzXz3zZE0qFX5XGq5Y1X2xzt3hKiAIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHZtLvfVxVjTRKJlCSrcA%2B0OgQdKbadHuqMVWABlXSTOfjTfudCxW8FYwkwsnRm3PlSht33mpOijtHLqzaOVfdMHHe%2FMApLUw9Z8p%2B5lmJWXrZoVapZCqFUlgfSK12USeHAfG%2BFMJ29%2FCdheOcamUXwyAwGHQKvu481pLPG2RSJGtkrGrbYpbTwZlktcuih68ZwKzmOciKAH%2FxFnHQtVqxTHdNEaFA%2FnPhSgghFINMRRGme8iBwHOpwrGVmFxP7HuJE0EQFE3JmNP%2FXHkxx5G8PDENoZYqf2RPxprNZGhvyQQi1W68UcHlKbSTZs%2FfhG5dF5G5qJcjqKXVzri8pmSCtpPrqnJiI2ryI74TGo43T23fN8%2FPO%2Fc71x8qJYh4YVXtgmOrI4uZXMCLkIOvVDCnVxLWviWisCkb7U7S3NUyWcS8GU2w%2FnNK9h2S29jJ1p5ihvDvQ%2FrSP5fd0E34CMznsAxvwiyzMN804AT%2F05D3TvhDh91EeAEPaJZ4qWKgTliR87gA6%2FoYdoqv4YfzzJu9SjFPCHvuvwJMR1pe65ISTHdznFAMgLl1nzpTbFFdl2y3eV6R7i88IjftK4z%2FzCi6Ogzk2dvXU4J%2Blt0nyPkiKCi325yM2UGMaXzmER1KkSYXbkm9yzPaKa7OUnMKjzgb0GOqUBP3l1xt2MHvMryMq6gpsr7ND64zS1dHjBuDfUW%2B2oKca0rjrnM%2BK7Sm5C6jVwoeNqsZV%2FWgd300ftrvQMEOAW1ewTb98P7ehgKP0Cvz8nHADvjlskrAVYot3k%2BDjermyPHID1V7oNix%2FJsDKRY8sXyXJJGznAviput0URI2JlSWLCrZCl6zRwzcO57WYecyiltD6xlaNUKYH6FCi8CZTi8JfU%2BP0T&X-Amz-Signature=eb5c21f7522f1735ce4e10d390c82e8741373ae56f6c3078494c9f0abcf7d413&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQJDHYU7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIVh3fBi6GAUmpNIdVEXWgYGSYhDz0DplkgUH9s%2FXekwIgBfQhVj9C1HPEKnzXz3zZE0qFX5XGq5Y1X2xzt3hKiAIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHZtLvfVxVjTRKJlCSrcA%2B0OgQdKbadHuqMVWABlXSTOfjTfudCxW8FYwkwsnRm3PlSht33mpOijtHLqzaOVfdMHHe%2FMApLUw9Z8p%2B5lmJWXrZoVapZCqFUlgfSK12USeHAfG%2BFMJ29%2FCdheOcamUXwyAwGHQKvu481pLPG2RSJGtkrGrbYpbTwZlktcuih68ZwKzmOciKAH%2FxFnHQtVqxTHdNEaFA%2FnPhSgghFINMRRGme8iBwHOpwrGVmFxP7HuJE0EQFE3JmNP%2FXHkxx5G8PDENoZYqf2RPxprNZGhvyQQi1W68UcHlKbSTZs%2FfhG5dF5G5qJcjqKXVzri8pmSCtpPrqnJiI2ryI74TGo43T23fN8%2FPO%2Fc71x8qJYh4YVXtgmOrI4uZXMCLkIOvVDCnVxLWviWisCkb7U7S3NUyWcS8GU2w%2FnNK9h2S29jJ1p5ihvDvQ%2FrSP5fd0E34CMznsAxvwiyzMN804AT%2F05D3TvhDh91EeAEPaJZ4qWKgTliR87gA6%2FoYdoqv4YfzzJu9SjFPCHvuvwJMR1pe65ISTHdznFAMgLl1nzpTbFFdl2y3eV6R7i88IjftK4z%2FzCi6Ogzk2dvXU4J%2Blt0nyPkiKCi325yM2UGMaXzmER1KkSYXbkm9yzPaKa7OUnMKjzgb0GOqUBP3l1xt2MHvMryMq6gpsr7ND64zS1dHjBuDfUW%2B2oKca0rjrnM%2BK7Sm5C6jVwoeNqsZV%2FWgd300ftrvQMEOAW1ewTb98P7ehgKP0Cvz8nHADvjlskrAVYot3k%2BDjermyPHID1V7oNix%2FJsDKRY8sXyXJJGznAviput0URI2JlSWLCrZCl6zRwzcO57WYecyiltD6xlaNUKYH6FCi8CZTi8JfU%2BP0T&X-Amz-Signature=9a2de4949a301696e21b992091127d0c3e14d082e21d990da14849f8bb32326a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQJDHYU7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIVh3fBi6GAUmpNIdVEXWgYGSYhDz0DplkgUH9s%2FXekwIgBfQhVj9C1HPEKnzXz3zZE0qFX5XGq5Y1X2xzt3hKiAIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHZtLvfVxVjTRKJlCSrcA%2B0OgQdKbadHuqMVWABlXSTOfjTfudCxW8FYwkwsnRm3PlSht33mpOijtHLqzaOVfdMHHe%2FMApLUw9Z8p%2B5lmJWXrZoVapZCqFUlgfSK12USeHAfG%2BFMJ29%2FCdheOcamUXwyAwGHQKvu481pLPG2RSJGtkrGrbYpbTwZlktcuih68ZwKzmOciKAH%2FxFnHQtVqxTHdNEaFA%2FnPhSgghFINMRRGme8iBwHOpwrGVmFxP7HuJE0EQFE3JmNP%2FXHkxx5G8PDENoZYqf2RPxprNZGhvyQQi1W68UcHlKbSTZs%2FfhG5dF5G5qJcjqKXVzri8pmSCtpPrqnJiI2ryI74TGo43T23fN8%2FPO%2Fc71x8qJYh4YVXtgmOrI4uZXMCLkIOvVDCnVxLWviWisCkb7U7S3NUyWcS8GU2w%2FnNK9h2S29jJ1p5ihvDvQ%2FrSP5fd0E34CMznsAxvwiyzMN804AT%2F05D3TvhDh91EeAEPaJZ4qWKgTliR87gA6%2FoYdoqv4YfzzJu9SjFPCHvuvwJMR1pe65ISTHdznFAMgLl1nzpTbFFdl2y3eV6R7i88IjftK4z%2FzCi6Ogzk2dvXU4J%2Blt0nyPkiKCi325yM2UGMaXzmER1KkSYXbkm9yzPaKa7OUnMKjzgb0GOqUBP3l1xt2MHvMryMq6gpsr7ND64zS1dHjBuDfUW%2B2oKca0rjrnM%2BK7Sm5C6jVwoeNqsZV%2FWgd300ftrvQMEOAW1ewTb98P7ehgKP0Cvz8nHADvjlskrAVYot3k%2BDjermyPHID1V7oNix%2FJsDKRY8sXyXJJGznAviput0URI2JlSWLCrZCl6zRwzcO57WYecyiltD6xlaNUKYH6FCi8CZTi8JfU%2BP0T&X-Amz-Signature=af84657d2310f4ad5abf998d7506eeb638f875d4fea58db287798365c6a399f7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VJMXYRQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEvzziMGEOGsdGAjxfra%2Btxkfv0gyjdOYHCoVZcIi908AiBhvJZ%2FfayxinDQXniquhgmsFofhlC3jKqf09K2%2Bel5Vir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMazV9%2F02A1Sd6CHzDKtwDrIBDxDwA%2B7BsQq8tpg7YOWr4QRO%2FtOCNdP6f8PnlZePV8FI0E%2Fe13ixWbzLHPPIeK5ADj08FkfrgjstfgOoH%2BPkVw9%2BP892FTVLTG43o%2F9BUK3OkEptZWMvZkM6bnabj7MFSMqeKsReK3FwyqESdTgomab1%2Bnf0i4lTl6kvBopxcFUJy9c5PIr5gDEXL3thkmNHj4GqEqNIHuplvjZ6fL2tvVwYd5KJaAcZYvBlXab4sjW1xaHS%2FWthlqdIpMlm5jeRfexjJscBS2JVYAUgBjF1KC72Di1ZYO87W37mGezVMLkhbr%2BZUsF97BZHN%2BwJc8jK9hyskCTfxFkEbUt0NvBhrN0TAaxw8SiklhKhF7f%2BBksiJfdT9TeN2%2Byom49eRwOQRVsLqXU6eWrrcoA5CWaWi3IbipfuTx0DrV1Yn4UjfbL7CvNTQroU6RButzYx6wwf0LdKc8ARUjy5KbH3E7PPu3TOoIFUGWCmz7POC1%2BPaZf43l0Q7G9t3xXJIshZ9w7%2Fa06g2Zt6e9UbckVIt9MRiByxU%2B09nevmTj6P8Epkij1gdLrY9jGhVtu1xh38l2Rp4V37NqEZaYfqZXi4HJB45fbYf3zdHlWRLTG4TWn6OtA%2FuIK4KlwiwEZQwjvOBvQY6pgGm41HLIg1N9RHThXZ9O4vq0j1Y9FOZH10qxXvj4IT9FtQydst68c3d2keU1gjQA3iixhT7hA%2BOmiatOv0PARU5uVlKCuW7JbAh6TQRGO6jfPKQ1E%2FODwLMSNQP22binpe0n6a40IaF%2B9DQXP8CTYD2w93R6pEFa0DA0Hy5vqzp84c4e5pHftMmfdqiKu%2BxzoH0TbdSkqk387pYym3DBv2A8Ai2y%2BZI&X-Amz-Signature=8bec3c229ee4534ea73c3d69f4558fc163d8f7620dcabbb6ac1e49ce36669c58&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMFH6RMO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKkA2zv%2BfBGDyb3UuVb%2B7i40RO1Z6EbL0BMx4sV%2FUiZAiEAkB%2FrOdQpbCkoADrIkD1wfv4SU5dzjs4ffAkeJZzfYhMq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDdoNBjlq34SBq5LYircAw3GylFgVj%2B3pQOiV6mAT0GJxfFoO4sUkjzl8E6aZKBt1DEvTbRecIFeQc2vTM3WVQ6Jj9gfzKl8yQYFxlAgfJRA41EHt%2BG8RVrFPLsn9PhVGsVNRBBFGTRiMmJKWGQuULzF4fZQhehJ4GNp%2FY6iAeqJMj1NFz03O%2FPD%2Fj12v%2BvSRmyzkdA%2BAb6P2KEhPoVM%2BHW1F6vFBg%2F9Gdtgidkea%2BeYPZfrvHn80G1wT4OiL640d5g5%2BlMMEqiw3vTDQWD%2BAJPGX%2FPMwCK3Ks4sSvfC6bCMnDg8WkbMIZWE%2FOd%2FDm5plUnU6L4gzvCY0RsFUhz3TdGsA3BCQPNgd3LeqonY%2F7uf2NYqOa9ThH9nSY%2FgDF6WaU%2Fgv3c3bMKNX%2F5AuR7YCwcj2mdU5b5%2BgLob2Is5Cc7REBJnvQeqczM7XU4D1hedzahXKtVQGqTCuJgVZH2%2B1HYGkUfo0ERixsZCM8oUNL%2BIp793NiDBxGCj4h5sd6zpDG0kaw04dldPCIVKwslws27nFTK4hQ2nguIF96KGWImpvy2BFaHx3RKHDijeqCBlN7hlw2UFlmA2GB6iS9TOYEH8mOa2kvaTsf15TISH7sYkNmTtSNXppOZVj%2F%2FN1WtxsGep1Lqm%2Bul2308FMIX0gb0GOqUBQJqqsNw14dLSYe2uJ4Qyu8lPSs8qqfOPQLraMOVL2MBSoGVxo1neeKzvWbIASCujMAzWSKELmEuNPyMQkJgNP1YlPJNoDee42rP8UIy7FMuu5FA%2FtSE8iwEGxKG7A00hfNLrvHx4kOxvn%2FesWLBH9L3DGyLBy9p%2BFj2rMegcP08cQUd%2BieguUj8JWJNCuGhDj4r%2B6rXUP50akozqm2ICiI6JwGfP&X-Amz-Signature=7c22c236bd0aa94e5275d5c95b7ffb7558803a34c7e013f7c8ab2c32cd134fce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQJDHYU7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIVh3fBi6GAUmpNIdVEXWgYGSYhDz0DplkgUH9s%2FXekwIgBfQhVj9C1HPEKnzXz3zZE0qFX5XGq5Y1X2xzt3hKiAIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHZtLvfVxVjTRKJlCSrcA%2B0OgQdKbadHuqMVWABlXSTOfjTfudCxW8FYwkwsnRm3PlSht33mpOijtHLqzaOVfdMHHe%2FMApLUw9Z8p%2B5lmJWXrZoVapZCqFUlgfSK12USeHAfG%2BFMJ29%2FCdheOcamUXwyAwGHQKvu481pLPG2RSJGtkrGrbYpbTwZlktcuih68ZwKzmOciKAH%2FxFnHQtVqxTHdNEaFA%2FnPhSgghFINMRRGme8iBwHOpwrGVmFxP7HuJE0EQFE3JmNP%2FXHkxx5G8PDENoZYqf2RPxprNZGhvyQQi1W68UcHlKbSTZs%2FfhG5dF5G5qJcjqKXVzri8pmSCtpPrqnJiI2ryI74TGo43T23fN8%2FPO%2Fc71x8qJYh4YVXtgmOrI4uZXMCLkIOvVDCnVxLWviWisCkb7U7S3NUyWcS8GU2w%2FnNK9h2S29jJ1p5ihvDvQ%2FrSP5fd0E34CMznsAxvwiyzMN804AT%2F05D3TvhDh91EeAEPaJZ4qWKgTliR87gA6%2FoYdoqv4YfzzJu9SjFPCHvuvwJMR1pe65ISTHdznFAMgLl1nzpTbFFdl2y3eV6R7i88IjftK4z%2FzCi6Ogzk2dvXU4J%2Blt0nyPkiKCi325yM2UGMaXzmER1KkSYXbkm9yzPaKa7OUnMKjzgb0GOqUBP3l1xt2MHvMryMq6gpsr7ND64zS1dHjBuDfUW%2B2oKca0rjrnM%2BK7Sm5C6jVwoeNqsZV%2FWgd300ftrvQMEOAW1ewTb98P7ehgKP0Cvz8nHADvjlskrAVYot3k%2BDjermyPHID1V7oNix%2FJsDKRY8sXyXJJGznAviput0URI2JlSWLCrZCl6zRwzcO57WYecyiltD6xlaNUKYH6FCi8CZTi8JfU%2BP0T&X-Amz-Signature=62a4e400a33073fc1a46442671cea81b7619512a7776e4b8a467f228fbbb0119&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQJDHYU7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIVh3fBi6GAUmpNIdVEXWgYGSYhDz0DplkgUH9s%2FXekwIgBfQhVj9C1HPEKnzXz3zZE0qFX5XGq5Y1X2xzt3hKiAIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHZtLvfVxVjTRKJlCSrcA%2B0OgQdKbadHuqMVWABlXSTOfjTfudCxW8FYwkwsnRm3PlSht33mpOijtHLqzaOVfdMHHe%2FMApLUw9Z8p%2B5lmJWXrZoVapZCqFUlgfSK12USeHAfG%2BFMJ29%2FCdheOcamUXwyAwGHQKvu481pLPG2RSJGtkrGrbYpbTwZlktcuih68ZwKzmOciKAH%2FxFnHQtVqxTHdNEaFA%2FnPhSgghFINMRRGme8iBwHOpwrGVmFxP7HuJE0EQFE3JmNP%2FXHkxx5G8PDENoZYqf2RPxprNZGhvyQQi1W68UcHlKbSTZs%2FfhG5dF5G5qJcjqKXVzri8pmSCtpPrqnJiI2ryI74TGo43T23fN8%2FPO%2Fc71x8qJYh4YVXtgmOrI4uZXMCLkIOvVDCnVxLWviWisCkb7U7S3NUyWcS8GU2w%2FnNK9h2S29jJ1p5ihvDvQ%2FrSP5fd0E34CMznsAxvwiyzMN804AT%2F05D3TvhDh91EeAEPaJZ4qWKgTliR87gA6%2FoYdoqv4YfzzJu9SjFPCHvuvwJMR1pe65ISTHdznFAMgLl1nzpTbFFdl2y3eV6R7i88IjftK4z%2FzCi6Ogzk2dvXU4J%2Blt0nyPkiKCi325yM2UGMaXzmER1KkSYXbkm9yzPaKa7OUnMKjzgb0GOqUBP3l1xt2MHvMryMq6gpsr7ND64zS1dHjBuDfUW%2B2oKca0rjrnM%2BK7Sm5C6jVwoeNqsZV%2FWgd300ftrvQMEOAW1ewTb98P7ehgKP0Cvz8nHADvjlskrAVYot3k%2BDjermyPHID1V7oNix%2FJsDKRY8sXyXJJGznAviput0URI2JlSWLCrZCl6zRwzcO57WYecyiltD6xlaNUKYH6FCi8CZTi8JfU%2BP0T&X-Amz-Signature=089d0b8f87e647dee623da0b9ef2529d35810291b5ccb86be71386c8691abe3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQJDHYU7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIVh3fBi6GAUmpNIdVEXWgYGSYhDz0DplkgUH9s%2FXekwIgBfQhVj9C1HPEKnzXz3zZE0qFX5XGq5Y1X2xzt3hKiAIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHZtLvfVxVjTRKJlCSrcA%2B0OgQdKbadHuqMVWABlXSTOfjTfudCxW8FYwkwsnRm3PlSht33mpOijtHLqzaOVfdMHHe%2FMApLUw9Z8p%2B5lmJWXrZoVapZCqFUlgfSK12USeHAfG%2BFMJ29%2FCdheOcamUXwyAwGHQKvu481pLPG2RSJGtkrGrbYpbTwZlktcuih68ZwKzmOciKAH%2FxFnHQtVqxTHdNEaFA%2FnPhSgghFINMRRGme8iBwHOpwrGVmFxP7HuJE0EQFE3JmNP%2FXHkxx5G8PDENoZYqf2RPxprNZGhvyQQi1W68UcHlKbSTZs%2FfhG5dF5G5qJcjqKXVzri8pmSCtpPrqnJiI2ryI74TGo43T23fN8%2FPO%2Fc71x8qJYh4YVXtgmOrI4uZXMCLkIOvVDCnVxLWviWisCkb7U7S3NUyWcS8GU2w%2FnNK9h2S29jJ1p5ihvDvQ%2FrSP5fd0E34CMznsAxvwiyzMN804AT%2F05D3TvhDh91EeAEPaJZ4qWKgTliR87gA6%2FoYdoqv4YfzzJu9SjFPCHvuvwJMR1pe65ISTHdznFAMgLl1nzpTbFFdl2y3eV6R7i88IjftK4z%2FzCi6Ogzk2dvXU4J%2Blt0nyPkiKCi325yM2UGMaXzmER1KkSYXbkm9yzPaKa7OUnMKjzgb0GOqUBP3l1xt2MHvMryMq6gpsr7ND64zS1dHjBuDfUW%2B2oKca0rjrnM%2BK7Sm5C6jVwoeNqsZV%2FWgd300ftrvQMEOAW1ewTb98P7ehgKP0Cvz8nHADvjlskrAVYot3k%2BDjermyPHID1V7oNix%2FJsDKRY8sXyXJJGznAviput0URI2JlSWLCrZCl6zRwzcO57WYecyiltD6xlaNUKYH6FCi8CZTi8JfU%2BP0T&X-Amz-Signature=3689fa2257449c682d6f32274a5f1f183b99dad809f3bf7afe6e03e05362d874&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4RUFXCM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmk7tVFCgtF7pmobOkq5rAGhLufs7Xtn0uCszbNTHQ4AIgMSiSbSlo6fnv9A9KJv%2BCmlJRS30oqbwNwKG0uMEua%2Fkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDFDXE511f19MxL4K9yrcA5EgL%2BqKG04Bp%2Fx1bkYxgsdcn2W1%2BXCgxZtMWgg9ChW%2BgUA9B8smkZ%2FqEU%2Fi%2FJrOUmZxjeGAiV3Dw31NKMETnW1qKHXSBsFw0d5W%2FhZKA9goBNaXZZcAtkbpXjHOwIVJNxcszCAm0q5r4jZFnu46dqtxbDUnHVc3Lq5MJwSvRhkPvQdGiq5MiDJQoIw3529TtFZuVar%2Fg%2FR%2ButodSRn0qHCXuQlm7cRAEu0BRUrNgPYLxOPcxd1voZihxrX1YPscvtMY%2BgUSbcI0CNRk4ezKD3sU7Eja2XRUl2ClNL789kCqp3GakVVOW7q%2BdX7D5%2BMfa3vUYXwj%2B9F24ld44kgG518M3Gi1nIhR5Y3oD1u2vRDj0WD1Ur%2BE0xm8neAQNaVbkFJd7UWLRZlT5Awrgxlr0Wi8Bv%2BPY7um2nAW3M3icKL9teC%2BqKDANhiS1Y9MtfT%2Bde0rEcxvlvoSZEQcrcvChTsOzJbs4%2FIslazUaONOzdfTdylBuEqJU9nsuFCPaasjwt54f4jgjD3UP9VrsGfo6f6NFgLG%2BOpXn4kI7yYZcJ%2Bkdiq%2FOK8eY15ZLemk0huvWAeUxiDUs%2BSHl45iQRHuLSJl5nSFMOEw5Skb7XkHjnHaUz83Qu7f38sUUwVfMOTygb0GOqUBzET7X%2FV95X5Kg2%2Bf6gTjRtG7%2B6Pnsfr6DWPszvkOgo83Mj5tPkOwo6Cv2lSQy9HJTnOWbJvYunAJFd6cy6gjGoUZ6GS94ZxGTnk9AdmMWw3SYXiICIrLVqNUaeIIUPb8lhWqhFIjezXOC40VljIL9OCQPsE5LrRHZv4kEUpWwMQaynEOmv6Z1hEmPIk6qML5VBVJHnCC4%2FtVocDfbQNb4wzasZ1l&X-Amz-Signature=d3676e998cc18d5804f1620057378ba73a1b5b6e0c0c4231e4aba2614d2ce424&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX3IDJXR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5BZF6vQGdWDdMZvKz9%2FTc6%2B84DZnMqhe%2FwvlIz45RDQIgG14LO3NfPIGR81gRdX1nEm9kENUhCv22osKkJNTOI0Mq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHVXoNuyi2o9IHy5XSrcA93cWHoqbvTl%2FmcE8poUwzynuvr2X6Y23Akp6Q%2FeMxg6kxa9V%2FZMPwBEjwBMVXY8oZMnB3KSDKOonDQV002P2Zg3mDAGc%2B87Dv5XhVGl4pCYvSmwu0OYQXMwkZ5%2B8JNixBkPSoPMyq%2FRAHEGccQZ%2FKgOm8U111VDqSiG1XJl6aB8VpEMDs9ICOfD0I9uEATkKeEeu8j2eAc4dWlRFcvnDjZiECeq78rg9ZKHOBPoLmiyXnvmoFISuFur%2BhylaH1w%2BIpaawgImQ9ltBepGLPI0lZ60jJJW4%2BUKnykikLZb90WdDsMbNwndVUR%2BAGBUcKUwW%2BJpqKV78M4O3Muomd0JNeEmwGez4ML3KXDn%2BzxasNMwuZpDoAl28GHsdNTfPHM7tRGP34793Ysi%2FDWrOZJccu8grsNGB37SixZYxvOR7wJffIlQDrNncyAdsATi4PXhPMTj7B0L57Zf1nik%2BAjBoktKaWT6uc%2Fa0mjKzLA6nOHXIiSNPFah9F1kC8vW%2BDAdsjTd4XRddUIaVCx7oUQ%2Bcee5Qa7gsH0aw%2B3ng1HjBewBLXgPEq9pnPg5opW0FipINE4SMgXLUY0lQqhJAFV0KOtIEKI1lXXAiGxGvQ2q%2FJfMssLDj21gwPmoOM9MKPzgb0GOqUBdRT%2F5eSUjH%2FGuH0IjqfTTn4scx2%2Fhdd4GqZhshObm2rqQ2X1OgL6fbWU87nOnHZdLLX7KbHqh04GNCgjxGrRY88%2BK7Ybol6QTH8ixcxtLRKw3%2FO91McNjPQ%2FGfRlYfRI3yj8AWMibLahhxMujQBxlhp7BBow8de2qCDhIARUVWEempECT4BMnkgdcoLVNgn6%2B4eF2cGSPXKsgwg1skiEhawVA4s2&X-Amz-Signature=ca1b9fef011b59612e31917a220d2ae2cc706202b411669610cae3f05ce768fa&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FKBXUSN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFx3ohtdyySUAeZKikaaxruISvhcHUUrmaZi%2Fm%2FrcMbSAiAxcqYjDSsWrI3Jmk6gIGu%2BVsoA3KOiuzGj9Ld%2BUgGmPSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMMM%2FWp8Zq6s3u%2FXgvKtwDCWzMoTvblQwGXLUmrHaqbL4qCxHmHxzY6qNBlNVtX3ILEOdoBsmvnSsiAE2WsA94M1x51ppqkrxkbmsANsG8v4HR6ppMk1ayQW8X6pHwXVP6AoFFLwqFL24pVdzRj2O6b7oP5FXybu0XgwmcV0yEdacJ4XFkIJQdMui6ILvrUQ9p23ikR1NzMYcHK7d2VZP9PAoXIOp707v15Dl9NuIcWPztrpkc1riHxzRnM68blH8IGgDHSv5NXSagZxSxJS16uRUlf49I47nlrdopMZqGbWPujiU%2FyNWh0AaFZYgnAVpMWwGeizo83X5ZPmOd%2BA11pwIVPrkvDdJnG6Dl2%2BO3M8R5ecV%2Bz6wDWwDjJBjLdWrKxs6sLSGLtGCbBGlpae9CYVgU31IUIoGIS0mj7GudTu5bPZCsiQJfs8vWhnqXhMbK9iq4sJqnrygKHo8QzlqcPITx9DwvLb4Czkd6bwoi9FKMPsNf012qYAXxDCNOn2SCfQflqsDHfrzQScCPMns6Bf7bUszcUhDKU2KhPoDZByKL6RRdGj9ngJuU1MS%2B1VGkwhf0F3wgZ8BMCfN7ahO4LDa%2Fl%2FMTtDHHHauE2kHQagPk97e4IDvDBvw6vqA8%2BFx4i0Z8zD3fx6MftYAwk%2FOBvQY6pgFzLV3%2FBBM20QjXxcLp3WAb54%2B4g%2FePTyVX2BnaO79W6oEs5UchG0SEPTyEr3zNGvRUj5dmxdggmxn0MuEcNNqLewCUgQvUmhLa6z7sJ3sLJq8AKeR6kL7RUFjqWt6fOkKdzmZ7DWONo0B6JgijTY90rrPMwNkZ7hMLDze45MHYC1qmRwCw430mEx8TGYOjHzgE45TCnwhOP2rOjT%2FXEt%2FKGLpa2E9Y&X-Amz-Signature=b1f0509a7d7b60a7581b18906e470ca739fb293fbbdb4184ec3df794173fe133&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GHCPLKT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD69qbgXGw06UsstL8iewRP%2FqFpDxMOul4rdHBUZWiODQIhAOPWcsIOu6n2Zo3dW%2FaST1umv%2BooZBFnAE%2BZcbI7chIVKv8DCBEQABoMNjM3NDIzMTgzODA1IgzZRUuS9uB2VP%2FXnpAq3ANhrJV7mWdv8%2BiDgFr7lMoWuHWIfYiohz0hoiEdvAtayY843Pdlyn6sufgEFTJYtYABlzqWJan0sdFE02qyMNm1YIbJ6meC4T2J0ApyOmcsHsDQPDaABlh0sYH92Uzbv3ORqavA%2BSHV8KgpWw9Rqg13e8X59a8gzS789iJPuMgLnJrq1E2SycWtv5wOV%2Bp6ftFdYvYt5iA56gdYp4xDTWtJX5xBTZywTeHplc4eaGufr5YVpdwtubdskLfs0N9ktkfX3tzgX5BsvYzDshcxm6sl5MG7V1oUwhJhTbJF9Q2iQh4yK9mmleIXz0OQCRMmrPVpBdVRq1kjYudvjLD9erhgyf15L8m93E6iRpWBziWRadtYKO8lyg%2BkA01qKLKSZB4qf8U90nNLQf2IVneQst1X212cKwnB8iYq3jhjKUeEVTptWK7MNfBVityJx9YVajnM00PL5CpmU9b%2FnjF%2Bpo8VIz%2B4zqyh%2FUOe5TZ4AI3FZ6eEgKQLMbAw1lSen7NY7k9vODLa2ZgBCCPk%2Fk7YUQxsOI%2FIYBNXKgRoMcuwoG%2BcB%2B%2FDSN6QchqdGz9xjHK92p1mAlcywL59uOHDrOBzbA6gYbdFePKz8MPwr%2ByCOZZ%2FrH2IWlwJYP7dzUqsIzCo84G9BjqkAVfKpKbt%2FmoBQQ%2BFGisHV9uH6ixD6bAaJplwl63dl%2FvspFtOavAzVosSXyCjzjHmx6IoKv%2FEIOi14TLq%2FUFeUrGeMIkTvX85DzOai1zwb45m0hxng3copjr0DkANF2eWYKDmcEVqM7ewbGJJc9v9IGLQpo0ZsUf9FaWI6ZWpWnZ3mjOR2YEh7u8YEvSjPpFuT22utmWK9Y5WJozYeLNqHA2QOQie&X-Amz-Signature=3876c1fecaf6592e18b7ffe558994fb2ee4d10d72677e7e2a8ae9b25e6f683fb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GHCPLKT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD69qbgXGw06UsstL8iewRP%2FqFpDxMOul4rdHBUZWiODQIhAOPWcsIOu6n2Zo3dW%2FaST1umv%2BooZBFnAE%2BZcbI7chIVKv8DCBEQABoMNjM3NDIzMTgzODA1IgzZRUuS9uB2VP%2FXnpAq3ANhrJV7mWdv8%2BiDgFr7lMoWuHWIfYiohz0hoiEdvAtayY843Pdlyn6sufgEFTJYtYABlzqWJan0sdFE02qyMNm1YIbJ6meC4T2J0ApyOmcsHsDQPDaABlh0sYH92Uzbv3ORqavA%2BSHV8KgpWw9Rqg13e8X59a8gzS789iJPuMgLnJrq1E2SycWtv5wOV%2Bp6ftFdYvYt5iA56gdYp4xDTWtJX5xBTZywTeHplc4eaGufr5YVpdwtubdskLfs0N9ktkfX3tzgX5BsvYzDshcxm6sl5MG7V1oUwhJhTbJF9Q2iQh4yK9mmleIXz0OQCRMmrPVpBdVRq1kjYudvjLD9erhgyf15L8m93E6iRpWBziWRadtYKO8lyg%2BkA01qKLKSZB4qf8U90nNLQf2IVneQst1X212cKwnB8iYq3jhjKUeEVTptWK7MNfBVityJx9YVajnM00PL5CpmU9b%2FnjF%2Bpo8VIz%2B4zqyh%2FUOe5TZ4AI3FZ6eEgKQLMbAw1lSen7NY7k9vODLa2ZgBCCPk%2Fk7YUQxsOI%2FIYBNXKgRoMcuwoG%2BcB%2B%2FDSN6QchqdGz9xjHK92p1mAlcywL59uOHDrOBzbA6gYbdFePKz8MPwr%2ByCOZZ%2FrH2IWlwJYP7dzUqsIzCo84G9BjqkAVfKpKbt%2FmoBQQ%2BFGisHV9uH6ixD6bAaJplwl63dl%2FvspFtOavAzVosSXyCjzjHmx6IoKv%2FEIOi14TLq%2FUFeUrGeMIkTvX85DzOai1zwb45m0hxng3copjr0DkANF2eWYKDmcEVqM7ewbGJJc9v9IGLQpo0ZsUf9FaWI6ZWpWnZ3mjOR2YEh7u8YEvSjPpFuT22utmWK9Y5WJozYeLNqHA2QOQie&X-Amz-Signature=cf8639dff1e23ea5b0dc19fd8ce44fe3eef52c9c4fd9b9282e20a49246dc6ba5&X-Amz-SignedHeaders=host&x-id=GetObject)

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
