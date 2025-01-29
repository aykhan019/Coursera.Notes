

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ADSMMGY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3FFXBWQzsiYyr%2FXnMdCsOJ2JFVJJaRFQuHMlbz26cYAiEA%2FS%2Bw9nu1%2F9i8CcFoaN3aDVKd38wL1PTIFlL7%2F3MOiWMqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBByL6Q53NYSR0mrGyrcAwxLBY1bOm66278FAhVbA34LEaJRN%2BCVxoUdTayFq55UgOlJHOFTzrh4LWP7m1WoBaBGNY6RWFoYrL9Mqha26BBfO%2Bw0gKE%2F3iC%2FvwElBlN3fkOh3zUr0rHkFD%2BNkj9M6rgEw1TwHZeMdQfPkeExxtScvnGyteJGaJyglxmKZT%2F7Z1YvtP1KvBnsNUp4wFIBtmpEHoNTfclSgLI3CS6QFo1RgW5FaRvOl53SwohDQwvVIoeCxVsZEzhdNrKzWElVbGkt5Z4lmpiIOR0bFYCWJkSOUNg1t5%2BIlSV0RqfitL4BLCxrskmUQisCoRKrOJZDrHnNCTNAiT33trmoHVczgb%2FOAKKVNMI8dGBAbMO48hbatGXVx8RSxxSeys2o%2BCJPnXm5LkIfZU7RDd6QBq6MkTNlKDO6hwy9AhNGjZ9%2BTqjgAvqtHmTB5i8QQYoDHVV0E0nNl8gDUOoCMxBarjX6ogUybKJRA2mSUHx%2FxIVz7GezniQeAm%2FBG0r2LHPSbu2dMxs7HZybz4xRKhbWT2cq4NQFIZjj7udMIkbLZ%2Fq1Cz8G5Tqrey79keTNako7bGMLrjlJMGLRnFye49jSvB2glhIrEUwjRfocNETmH%2BWUUJq4lacwQZXaEMjVQGaPMPqD6bwGOqUBKBTGHE%2B0bByNcJy2vWliOoP7%2BnsgHemEZw5STSWMiLUQO8gQZIsfpfF9veThuWrVM2FR9f6Pzk%2F1n9X0KlWsDkQalWQbHjASik4S%2BI5IL3MAgU7JtXfXx3wPaHcmURsd4Sf504sV%2FxXzUvkd%2BYvpJP3LTwaYP5YxRCoO0ria6oKN7A3Bx9PtINeC0rte90JQ8mFmUR6QJhMq8hrv9RzuP00TRIU%2F&X-Amz-Signature=9b4687655e3a3e4a97d310d4b9ab0d2759217a64ce81f9fcaa94863418988063&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ADSMMGY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3FFXBWQzsiYyr%2FXnMdCsOJ2JFVJJaRFQuHMlbz26cYAiEA%2FS%2Bw9nu1%2F9i8CcFoaN3aDVKd38wL1PTIFlL7%2F3MOiWMqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBByL6Q53NYSR0mrGyrcAwxLBY1bOm66278FAhVbA34LEaJRN%2BCVxoUdTayFq55UgOlJHOFTzrh4LWP7m1WoBaBGNY6RWFoYrL9Mqha26BBfO%2Bw0gKE%2F3iC%2FvwElBlN3fkOh3zUr0rHkFD%2BNkj9M6rgEw1TwHZeMdQfPkeExxtScvnGyteJGaJyglxmKZT%2F7Z1YvtP1KvBnsNUp4wFIBtmpEHoNTfclSgLI3CS6QFo1RgW5FaRvOl53SwohDQwvVIoeCxVsZEzhdNrKzWElVbGkt5Z4lmpiIOR0bFYCWJkSOUNg1t5%2BIlSV0RqfitL4BLCxrskmUQisCoRKrOJZDrHnNCTNAiT33trmoHVczgb%2FOAKKVNMI8dGBAbMO48hbatGXVx8RSxxSeys2o%2BCJPnXm5LkIfZU7RDd6QBq6MkTNlKDO6hwy9AhNGjZ9%2BTqjgAvqtHmTB5i8QQYoDHVV0E0nNl8gDUOoCMxBarjX6ogUybKJRA2mSUHx%2FxIVz7GezniQeAm%2FBG0r2LHPSbu2dMxs7HZybz4xRKhbWT2cq4NQFIZjj7udMIkbLZ%2Fq1Cz8G5Tqrey79keTNako7bGMLrjlJMGLRnFye49jSvB2glhIrEUwjRfocNETmH%2BWUUJq4lacwQZXaEMjVQGaPMPqD6bwGOqUBKBTGHE%2B0bByNcJy2vWliOoP7%2BnsgHemEZw5STSWMiLUQO8gQZIsfpfF9veThuWrVM2FR9f6Pzk%2F1n9X0KlWsDkQalWQbHjASik4S%2BI5IL3MAgU7JtXfXx3wPaHcmURsd4Sf504sV%2FxXzUvkd%2BYvpJP3LTwaYP5YxRCoO0ria6oKN7A3Bx9PtINeC0rte90JQ8mFmUR6QJhMq8hrv9RzuP00TRIU%2F&X-Amz-Signature=9feed869ec291de2a28738dc3fb2bbd4bb85f8088f04becd1527bc6659c7fe08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ADSMMGY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3FFXBWQzsiYyr%2FXnMdCsOJ2JFVJJaRFQuHMlbz26cYAiEA%2FS%2Bw9nu1%2F9i8CcFoaN3aDVKd38wL1PTIFlL7%2F3MOiWMqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBByL6Q53NYSR0mrGyrcAwxLBY1bOm66278FAhVbA34LEaJRN%2BCVxoUdTayFq55UgOlJHOFTzrh4LWP7m1WoBaBGNY6RWFoYrL9Mqha26BBfO%2Bw0gKE%2F3iC%2FvwElBlN3fkOh3zUr0rHkFD%2BNkj9M6rgEw1TwHZeMdQfPkeExxtScvnGyteJGaJyglxmKZT%2F7Z1YvtP1KvBnsNUp4wFIBtmpEHoNTfclSgLI3CS6QFo1RgW5FaRvOl53SwohDQwvVIoeCxVsZEzhdNrKzWElVbGkt5Z4lmpiIOR0bFYCWJkSOUNg1t5%2BIlSV0RqfitL4BLCxrskmUQisCoRKrOJZDrHnNCTNAiT33trmoHVczgb%2FOAKKVNMI8dGBAbMO48hbatGXVx8RSxxSeys2o%2BCJPnXm5LkIfZU7RDd6QBq6MkTNlKDO6hwy9AhNGjZ9%2BTqjgAvqtHmTB5i8QQYoDHVV0E0nNl8gDUOoCMxBarjX6ogUybKJRA2mSUHx%2FxIVz7GezniQeAm%2FBG0r2LHPSbu2dMxs7HZybz4xRKhbWT2cq4NQFIZjj7udMIkbLZ%2Fq1Cz8G5Tqrey79keTNako7bGMLrjlJMGLRnFye49jSvB2glhIrEUwjRfocNETmH%2BWUUJq4lacwQZXaEMjVQGaPMPqD6bwGOqUBKBTGHE%2B0bByNcJy2vWliOoP7%2BnsgHemEZw5STSWMiLUQO8gQZIsfpfF9veThuWrVM2FR9f6Pzk%2F1n9X0KlWsDkQalWQbHjASik4S%2BI5IL3MAgU7JtXfXx3wPaHcmURsd4Sf504sV%2FxXzUvkd%2BYvpJP3LTwaYP5YxRCoO0ria6oKN7A3Bx9PtINeC0rte90JQ8mFmUR6QJhMq8hrv9RzuP00TRIU%2F&X-Amz-Signature=8951e72148ab72b9b40b691cf8693bfcfd9bb13adae316294ba60a5e3e4440bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S22A4DLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICljwnJKsN9ZSjwou4KCgPB4Rh8uq0lUMisOMEKp6iWLAiBr8iZ9h8XceY36GgNFCPOroobwlg2d%2BrDZvgkDfwo11SqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWNeFTeUgcRHsulflKtwDOWD%2FcR9OaLahWzuZcLjDFGVDCm%2Ff2l%2FCg1pcBq0CuppMqEcavR9%2B72X6SekiOTWdWWNlHAgMrN1z63Nw0QAIrWPKsIFQ2mQ9AWSc%2BYdyDhWmvMuPobgBr0Jm90flH0p06LHx1VhBoxQGp33aIO3%2FMvoiCSDLzahj%2BQVnF8j4DwCGCblZ4zOHfBbILhxbFE%2BGefAQGJTlZB6DITGGm9LxiJzmHB9zJiJ0dbztORjfsjUZEtmJV2qKz90WsoN%2F5PdUD4cAdliTlq4zSXRfiId8D83Ab1phHmGRnxc%2FHlU2E105iRutMozgA7iQVvHkBT4ZL1FXf1fnh33p8fE8Tjf6pxLpIv7dt2UXrKlkTBET5FLvyvHWFlY%2FJJeBE4qUtZDx3%2BwcammcUdJPF4s2FoY5Yj58U7NVqnJOBTDDUVj1q%2FNcNwAjZcsu43ELS1r0HRgQhWCdqPrOsAIJhxsQ0VK4ieY2MhGXASsakWgD4sSNO2jz5tOlL6ceY7z%2BTaYdDy%2B2YpMXItSWfOwuKPug7tMh5xios3JdOI00i2W6RyU3IBBtbXH18ekXOVCiIA9LTv5vSf8sasw2Hj4ebrDv9eyNt00bIGDFAU%2BPcTUF1YvRFHR5SWWLj8e6OfSYGdgwg4TpvAY6pgFWsOor6dvPf358IUZFeAn9RnrcDwicN9mlB0jv8k6yMrUuJvXpyp%2BI0b6s%2FEs7EQPJUtebiszVi0sFu7nQ5k4hAyoIBjIk0SmcDGlT2JTA7422R5C3fAfClR3UNtJQNiKuaUpdd3n14vKcZ3oOYS4wk3H%2BotkuamzpgUPvYR1kdk4svLneKLQdMTFl2Gta9C6PnTk4UqM11FSoReWvSe%2FfQivEMHUh&X-Amz-Signature=800b040a13b030d4ece20b27c0159b963add9d0e57dfa35dd50cd90e83d7e7ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S22A4DLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICljwnJKsN9ZSjwou4KCgPB4Rh8uq0lUMisOMEKp6iWLAiBr8iZ9h8XceY36GgNFCPOroobwlg2d%2BrDZvgkDfwo11SqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWNeFTeUgcRHsulflKtwDOWD%2FcR9OaLahWzuZcLjDFGVDCm%2Ff2l%2FCg1pcBq0CuppMqEcavR9%2B72X6SekiOTWdWWNlHAgMrN1z63Nw0QAIrWPKsIFQ2mQ9AWSc%2BYdyDhWmvMuPobgBr0Jm90flH0p06LHx1VhBoxQGp33aIO3%2FMvoiCSDLzahj%2BQVnF8j4DwCGCblZ4zOHfBbILhxbFE%2BGefAQGJTlZB6DITGGm9LxiJzmHB9zJiJ0dbztORjfsjUZEtmJV2qKz90WsoN%2F5PdUD4cAdliTlq4zSXRfiId8D83Ab1phHmGRnxc%2FHlU2E105iRutMozgA7iQVvHkBT4ZL1FXf1fnh33p8fE8Tjf6pxLpIv7dt2UXrKlkTBET5FLvyvHWFlY%2FJJeBE4qUtZDx3%2BwcammcUdJPF4s2FoY5Yj58U7NVqnJOBTDDUVj1q%2FNcNwAjZcsu43ELS1r0HRgQhWCdqPrOsAIJhxsQ0VK4ieY2MhGXASsakWgD4sSNO2jz5tOlL6ceY7z%2BTaYdDy%2B2YpMXItSWfOwuKPug7tMh5xios3JdOI00i2W6RyU3IBBtbXH18ekXOVCiIA9LTv5vSf8sasw2Hj4ebrDv9eyNt00bIGDFAU%2BPcTUF1YvRFHR5SWWLj8e6OfSYGdgwg4TpvAY6pgFWsOor6dvPf358IUZFeAn9RnrcDwicN9mlB0jv8k6yMrUuJvXpyp%2BI0b6s%2FEs7EQPJUtebiszVi0sFu7nQ5k4hAyoIBjIk0SmcDGlT2JTA7422R5C3fAfClR3UNtJQNiKuaUpdd3n14vKcZ3oOYS4wk3H%2BotkuamzpgUPvYR1kdk4svLneKLQdMTFl2Gta9C6PnTk4UqM11FSoReWvSe%2FfQivEMHUh&X-Amz-Signature=7a3116525eff0e04ac4fcebd9df5c073241cbf238a8a566858f4913b587c7788&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S22A4DLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICljwnJKsN9ZSjwou4KCgPB4Rh8uq0lUMisOMEKp6iWLAiBr8iZ9h8XceY36GgNFCPOroobwlg2d%2BrDZvgkDfwo11SqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWNeFTeUgcRHsulflKtwDOWD%2FcR9OaLahWzuZcLjDFGVDCm%2Ff2l%2FCg1pcBq0CuppMqEcavR9%2B72X6SekiOTWdWWNlHAgMrN1z63Nw0QAIrWPKsIFQ2mQ9AWSc%2BYdyDhWmvMuPobgBr0Jm90flH0p06LHx1VhBoxQGp33aIO3%2FMvoiCSDLzahj%2BQVnF8j4DwCGCblZ4zOHfBbILhxbFE%2BGefAQGJTlZB6DITGGm9LxiJzmHB9zJiJ0dbztORjfsjUZEtmJV2qKz90WsoN%2F5PdUD4cAdliTlq4zSXRfiId8D83Ab1phHmGRnxc%2FHlU2E105iRutMozgA7iQVvHkBT4ZL1FXf1fnh33p8fE8Tjf6pxLpIv7dt2UXrKlkTBET5FLvyvHWFlY%2FJJeBE4qUtZDx3%2BwcammcUdJPF4s2FoY5Yj58U7NVqnJOBTDDUVj1q%2FNcNwAjZcsu43ELS1r0HRgQhWCdqPrOsAIJhxsQ0VK4ieY2MhGXASsakWgD4sSNO2jz5tOlL6ceY7z%2BTaYdDy%2B2YpMXItSWfOwuKPug7tMh5xios3JdOI00i2W6RyU3IBBtbXH18ekXOVCiIA9LTv5vSf8sasw2Hj4ebrDv9eyNt00bIGDFAU%2BPcTUF1YvRFHR5SWWLj8e6OfSYGdgwg4TpvAY6pgFWsOor6dvPf358IUZFeAn9RnrcDwicN9mlB0jv8k6yMrUuJvXpyp%2BI0b6s%2FEs7EQPJUtebiszVi0sFu7nQ5k4hAyoIBjIk0SmcDGlT2JTA7422R5C3fAfClR3UNtJQNiKuaUpdd3n14vKcZ3oOYS4wk3H%2BotkuamzpgUPvYR1kdk4svLneKLQdMTFl2Gta9C6PnTk4UqM11FSoReWvSe%2FfQivEMHUh&X-Amz-Signature=b1d194c0766b8d3e0d370189e4a6ce5b4d096ee18df0d4ccb3abfbe55f4f58b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S22A4DLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICljwnJKsN9ZSjwou4KCgPB4Rh8uq0lUMisOMEKp6iWLAiBr8iZ9h8XceY36GgNFCPOroobwlg2d%2BrDZvgkDfwo11SqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWNeFTeUgcRHsulflKtwDOWD%2FcR9OaLahWzuZcLjDFGVDCm%2Ff2l%2FCg1pcBq0CuppMqEcavR9%2B72X6SekiOTWdWWNlHAgMrN1z63Nw0QAIrWPKsIFQ2mQ9AWSc%2BYdyDhWmvMuPobgBr0Jm90flH0p06LHx1VhBoxQGp33aIO3%2FMvoiCSDLzahj%2BQVnF8j4DwCGCblZ4zOHfBbILhxbFE%2BGefAQGJTlZB6DITGGm9LxiJzmHB9zJiJ0dbztORjfsjUZEtmJV2qKz90WsoN%2F5PdUD4cAdliTlq4zSXRfiId8D83Ab1phHmGRnxc%2FHlU2E105iRutMozgA7iQVvHkBT4ZL1FXf1fnh33p8fE8Tjf6pxLpIv7dt2UXrKlkTBET5FLvyvHWFlY%2FJJeBE4qUtZDx3%2BwcammcUdJPF4s2FoY5Yj58U7NVqnJOBTDDUVj1q%2FNcNwAjZcsu43ELS1r0HRgQhWCdqPrOsAIJhxsQ0VK4ieY2MhGXASsakWgD4sSNO2jz5tOlL6ceY7z%2BTaYdDy%2B2YpMXItSWfOwuKPug7tMh5xios3JdOI00i2W6RyU3IBBtbXH18ekXOVCiIA9LTv5vSf8sasw2Hj4ebrDv9eyNt00bIGDFAU%2BPcTUF1YvRFHR5SWWLj8e6OfSYGdgwg4TpvAY6pgFWsOor6dvPf358IUZFeAn9RnrcDwicN9mlB0jv8k6yMrUuJvXpyp%2BI0b6s%2FEs7EQPJUtebiszVi0sFu7nQ5k4hAyoIBjIk0SmcDGlT2JTA7422R5C3fAfClR3UNtJQNiKuaUpdd3n14vKcZ3oOYS4wk3H%2BotkuamzpgUPvYR1kdk4svLneKLQdMTFl2Gta9C6PnTk4UqM11FSoReWvSe%2FfQivEMHUh&X-Amz-Signature=a326f3096cac704a866b941904fbe48ebc1e0f1f831218738ab1536cf862d9ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S22A4DLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICljwnJKsN9ZSjwou4KCgPB4Rh8uq0lUMisOMEKp6iWLAiBr8iZ9h8XceY36GgNFCPOroobwlg2d%2BrDZvgkDfwo11SqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWNeFTeUgcRHsulflKtwDOWD%2FcR9OaLahWzuZcLjDFGVDCm%2Ff2l%2FCg1pcBq0CuppMqEcavR9%2B72X6SekiOTWdWWNlHAgMrN1z63Nw0QAIrWPKsIFQ2mQ9AWSc%2BYdyDhWmvMuPobgBr0Jm90flH0p06LHx1VhBoxQGp33aIO3%2FMvoiCSDLzahj%2BQVnF8j4DwCGCblZ4zOHfBbILhxbFE%2BGefAQGJTlZB6DITGGm9LxiJzmHB9zJiJ0dbztORjfsjUZEtmJV2qKz90WsoN%2F5PdUD4cAdliTlq4zSXRfiId8D83Ab1phHmGRnxc%2FHlU2E105iRutMozgA7iQVvHkBT4ZL1FXf1fnh33p8fE8Tjf6pxLpIv7dt2UXrKlkTBET5FLvyvHWFlY%2FJJeBE4qUtZDx3%2BwcammcUdJPF4s2FoY5Yj58U7NVqnJOBTDDUVj1q%2FNcNwAjZcsu43ELS1r0HRgQhWCdqPrOsAIJhxsQ0VK4ieY2MhGXASsakWgD4sSNO2jz5tOlL6ceY7z%2BTaYdDy%2B2YpMXItSWfOwuKPug7tMh5xios3JdOI00i2W6RyU3IBBtbXH18ekXOVCiIA9LTv5vSf8sasw2Hj4ebrDv9eyNt00bIGDFAU%2BPcTUF1YvRFHR5SWWLj8e6OfSYGdgwg4TpvAY6pgFWsOor6dvPf358IUZFeAn9RnrcDwicN9mlB0jv8k6yMrUuJvXpyp%2BI0b6s%2FEs7EQPJUtebiszVi0sFu7nQ5k4hAyoIBjIk0SmcDGlT2JTA7422R5C3fAfClR3UNtJQNiKuaUpdd3n14vKcZ3oOYS4wk3H%2BotkuamzpgUPvYR1kdk4svLneKLQdMTFl2Gta9C6PnTk4UqM11FSoReWvSe%2FfQivEMHUh&X-Amz-Signature=f24c79b00c65c58b10d773ea111abb7da285c4a137a4dc0e2c4f8782ba9b2c57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S22A4DLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICljwnJKsN9ZSjwou4KCgPB4Rh8uq0lUMisOMEKp6iWLAiBr8iZ9h8XceY36GgNFCPOroobwlg2d%2BrDZvgkDfwo11SqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWNeFTeUgcRHsulflKtwDOWD%2FcR9OaLahWzuZcLjDFGVDCm%2Ff2l%2FCg1pcBq0CuppMqEcavR9%2B72X6SekiOTWdWWNlHAgMrN1z63Nw0QAIrWPKsIFQ2mQ9AWSc%2BYdyDhWmvMuPobgBr0Jm90flH0p06LHx1VhBoxQGp33aIO3%2FMvoiCSDLzahj%2BQVnF8j4DwCGCblZ4zOHfBbILhxbFE%2BGefAQGJTlZB6DITGGm9LxiJzmHB9zJiJ0dbztORjfsjUZEtmJV2qKz90WsoN%2F5PdUD4cAdliTlq4zSXRfiId8D83Ab1phHmGRnxc%2FHlU2E105iRutMozgA7iQVvHkBT4ZL1FXf1fnh33p8fE8Tjf6pxLpIv7dt2UXrKlkTBET5FLvyvHWFlY%2FJJeBE4qUtZDx3%2BwcammcUdJPF4s2FoY5Yj58U7NVqnJOBTDDUVj1q%2FNcNwAjZcsu43ELS1r0HRgQhWCdqPrOsAIJhxsQ0VK4ieY2MhGXASsakWgD4sSNO2jz5tOlL6ceY7z%2BTaYdDy%2B2YpMXItSWfOwuKPug7tMh5xios3JdOI00i2W6RyU3IBBtbXH18ekXOVCiIA9LTv5vSf8sasw2Hj4ebrDv9eyNt00bIGDFAU%2BPcTUF1YvRFHR5SWWLj8e6OfSYGdgwg4TpvAY6pgFWsOor6dvPf358IUZFeAn9RnrcDwicN9mlB0jv8k6yMrUuJvXpyp%2BI0b6s%2FEs7EQPJUtebiszVi0sFu7nQ5k4hAyoIBjIk0SmcDGlT2JTA7422R5C3fAfClR3UNtJQNiKuaUpdd3n14vKcZ3oOYS4wk3H%2BotkuamzpgUPvYR1kdk4svLneKLQdMTFl2Gta9C6PnTk4UqM11FSoReWvSe%2FfQivEMHUh&X-Amz-Signature=f87bd5f1f5ec38cb014e4ecede85141a0ffbdfbd92ce1bd73d606ba99b1c1450&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632WZYJ4Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDc8Z8KpEQTrqfazzSwTfVnOiPPppJxwJb5dyzkKC3xmgIgBc%2BiJqtU%2BsZJBulzfywNECLl0ZvSBQxtpmOIu5SvBDoqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAqPv6%2FEkUQMcBz8tyrcAy5JsKZnXU5elWSyr4UzFlGGPyP8J%2Fi6YhK%2BallZ6%2B2bZX7Uwwn1Z8O7egJ4fEoF4mfh4WjarrPzlYT2GFiBReTluCed1UU3IrfD07meqOw9nMvwBCOUnyAZizsxhZldqPr5Y%2FDJMszL%2FGXLox7iv1cmLrLzMAxBdgn7oTvv%2Fw9yQPtZMeUvbsXo8Q6yFcsUj6xF2PXPsocPbweNO2wgBoFttO75aT7kuTxkuRSsDrbjyC9r56JAMH5UZLtidhTJad4Yf%2F2W%2BrluWqSGo96afp6tFiV6QF7r3fzfiPYvUeiRMfQPayIt6gwW3PeTeO6l3xC1ezQ3yM7%2BcbvYx39CftTHOO44Tj6mgHz6Ou8mgDg9y78FkemWGCBs5tnKSCAfYaOerRnw8zdV%2Be%2Fi%2FPNZg3TMQHbM2TMyq%2FaMXlf7m0v3TVaztWRuAz2RmV9gR6MtPR882blf%2Blla%2FS%2FfrHtMQS4I9641ayO3cS6psRYDYAR5IPg2tbw8LXZ4%2FuuzTmM93Zt8Ana9JoM%2FcBFa5nDHJUE9AK86U71CtDTIG1ndE%2F1A2l74DhjS7mrl15XQq%2BQhcQRsWMlBM9B7GmQNobkBeX9zGf4553tPiUFnkFFs7%2BdVxuBxj7fA%2FnRcr9LxMNWD6bwGOqUB%2Fjp4FfbXZONVcP%2BxklDkOA4Z%2Bp0M%2BT6dV%2FGC1l8G3%2Bmjwy05ZE%2FaHc1Wg36msHPSpCgO3l9KP3SvanSD8%2BJ0Pfm8M8MjuNtyMXzUEWPYsISIxTQ3xUZzBJi%2F3zWkmGyap7qjKkLQyCi2IJv8fTWUielWin0pFZ2i%2FAJWcxa85Ap24u45%2FNqmR4j7V7yTYynU23Da4g4WZK40UTGp3rmPERT6lybq&X-Amz-Signature=9694c1d7e9971e91b858f290a52b1e8a24ab2e5c9341d68cd273b48b6abaf34d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PQOG3AU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHK6i8iK6fBd2EzQlOeDJxS%2BA7%2BaEN%2BDj9KMZbzzDYBWAiA8I2ChLbMNvprSrq4m8vkV3PVUpLGNtMOttwYvrmHGXyqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLA5Hq9mbl2uK7iQpKtwDr%2B8MS386p4uCzE6iMSFpyZEHtd%2Bq0qJhqeQBzErnHgYLA0W%2FoPWVFFserhqsNperIDOZ99M%2BKXXAy%2Frj7dher3l1oyqaLNBUga%2BcRHrSBeaL4XHu1n99nCCFtO2J31OsAaStKhjK5fMAoQGYlDF7J5OqBkEK89kbsLWtkzLBzCzTXYeWZBMuhptuOYuGtCgdw7kv%2B8FsGu2jdiT3wFZ4gCDwiNTimggDRe2t5tOLh9sjKcPVdiekxC7tWrP9J4I0VSUdmjXHSJ4rREuQxkJclCATZ2RCf6n%2FU1F3hH1H%2BNIiuugPUbN0Ixdlu8sRUDbJujnQYcdT6drAGvpSKmna1ryMeXOmlACuOpd6RcNkV5IyiZcv%2BjXU9T33SrE1qANNBtDZUO%2FHvKZISB94S8A5%2B31h0wSddSCFRMSWwJX%2FQ6DPbeTTJsat7Q3xZpOIqb%2BEywHY%2FDg4aM81AWf1hqzLK5sXAs3rue0vciM%2BNtlWHJnsNNzZswrcI1HtBB6BAvD5lYDlOlkINa2NZBidWIbY2et%2B57HKmrxRlOrV0fCKPIlE6xLQ%2BK2GBh%2F%2BbfcK68qFEXzmU5SYCn8S5sjOH7dpLjnFn0ZSo8kDsk6ET%2F%2FNL554AMJfU1J3ZvRoW8EwroTpvAY6pgFNQzpNi8i5%2FtMiuc%2BNdTi%2BTi253Cix95uz5DZolbDIPtDqLwUrXvJN8T2ndNR5Uf9BOxk9Wj2lvajnPx5yi20rbzOy7nSqjUhOq7xALQK%2B3YL%2ByECnj2p96o3aB8DJ6omp112cwewpfP5YlXukyZKPgMDB94z8sufE%2B4ebaM6xqtNbPS%2FCy0s%2BM5SdRUrvXNCf3xRbkGmP9tTsovlIm8J%2FiUEte4G2&X-Amz-Signature=8ed612d0964dad20d453017b591a054523eb03cc76eae2888d87afae5c33d44d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S22A4DLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICljwnJKsN9ZSjwou4KCgPB4Rh8uq0lUMisOMEKp6iWLAiBr8iZ9h8XceY36GgNFCPOroobwlg2d%2BrDZvgkDfwo11SqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWNeFTeUgcRHsulflKtwDOWD%2FcR9OaLahWzuZcLjDFGVDCm%2Ff2l%2FCg1pcBq0CuppMqEcavR9%2B72X6SekiOTWdWWNlHAgMrN1z63Nw0QAIrWPKsIFQ2mQ9AWSc%2BYdyDhWmvMuPobgBr0Jm90flH0p06LHx1VhBoxQGp33aIO3%2FMvoiCSDLzahj%2BQVnF8j4DwCGCblZ4zOHfBbILhxbFE%2BGefAQGJTlZB6DITGGm9LxiJzmHB9zJiJ0dbztORjfsjUZEtmJV2qKz90WsoN%2F5PdUD4cAdliTlq4zSXRfiId8D83Ab1phHmGRnxc%2FHlU2E105iRutMozgA7iQVvHkBT4ZL1FXf1fnh33p8fE8Tjf6pxLpIv7dt2UXrKlkTBET5FLvyvHWFlY%2FJJeBE4qUtZDx3%2BwcammcUdJPF4s2FoY5Yj58U7NVqnJOBTDDUVj1q%2FNcNwAjZcsu43ELS1r0HRgQhWCdqPrOsAIJhxsQ0VK4ieY2MhGXASsakWgD4sSNO2jz5tOlL6ceY7z%2BTaYdDy%2B2YpMXItSWfOwuKPug7tMh5xios3JdOI00i2W6RyU3IBBtbXH18ekXOVCiIA9LTv5vSf8sasw2Hj4ebrDv9eyNt00bIGDFAU%2BPcTUF1YvRFHR5SWWLj8e6OfSYGdgwg4TpvAY6pgFWsOor6dvPf358IUZFeAn9RnrcDwicN9mlB0jv8k6yMrUuJvXpyp%2BI0b6s%2FEs7EQPJUtebiszVi0sFu7nQ5k4hAyoIBjIk0SmcDGlT2JTA7422R5C3fAfClR3UNtJQNiKuaUpdd3n14vKcZ3oOYS4wk3H%2BotkuamzpgUPvYR1kdk4svLneKLQdMTFl2Gta9C6PnTk4UqM11FSoReWvSe%2FfQivEMHUh&X-Amz-Signature=fa1ec358acf427a9fcb6d2dd643ee05ecf71fe7ff70070a3d63afcb8533cdf5f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S22A4DLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICljwnJKsN9ZSjwou4KCgPB4Rh8uq0lUMisOMEKp6iWLAiBr8iZ9h8XceY36GgNFCPOroobwlg2d%2BrDZvgkDfwo11SqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWNeFTeUgcRHsulflKtwDOWD%2FcR9OaLahWzuZcLjDFGVDCm%2Ff2l%2FCg1pcBq0CuppMqEcavR9%2B72X6SekiOTWdWWNlHAgMrN1z63Nw0QAIrWPKsIFQ2mQ9AWSc%2BYdyDhWmvMuPobgBr0Jm90flH0p06LHx1VhBoxQGp33aIO3%2FMvoiCSDLzahj%2BQVnF8j4DwCGCblZ4zOHfBbILhxbFE%2BGefAQGJTlZB6DITGGm9LxiJzmHB9zJiJ0dbztORjfsjUZEtmJV2qKz90WsoN%2F5PdUD4cAdliTlq4zSXRfiId8D83Ab1phHmGRnxc%2FHlU2E105iRutMozgA7iQVvHkBT4ZL1FXf1fnh33p8fE8Tjf6pxLpIv7dt2UXrKlkTBET5FLvyvHWFlY%2FJJeBE4qUtZDx3%2BwcammcUdJPF4s2FoY5Yj58U7NVqnJOBTDDUVj1q%2FNcNwAjZcsu43ELS1r0HRgQhWCdqPrOsAIJhxsQ0VK4ieY2MhGXASsakWgD4sSNO2jz5tOlL6ceY7z%2BTaYdDy%2B2YpMXItSWfOwuKPug7tMh5xios3JdOI00i2W6RyU3IBBtbXH18ekXOVCiIA9LTv5vSf8sasw2Hj4ebrDv9eyNt00bIGDFAU%2BPcTUF1YvRFHR5SWWLj8e6OfSYGdgwg4TpvAY6pgFWsOor6dvPf358IUZFeAn9RnrcDwicN9mlB0jv8k6yMrUuJvXpyp%2BI0b6s%2FEs7EQPJUtebiszVi0sFu7nQ5k4hAyoIBjIk0SmcDGlT2JTA7422R5C3fAfClR3UNtJQNiKuaUpdd3n14vKcZ3oOYS4wk3H%2BotkuamzpgUPvYR1kdk4svLneKLQdMTFl2Gta9C6PnTk4UqM11FSoReWvSe%2FfQivEMHUh&X-Amz-Signature=6463e4bd45a76ecb1358450d15849c6fae1b1e6aaadff921414b895b492d84a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S22A4DLM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICljwnJKsN9ZSjwou4KCgPB4Rh8uq0lUMisOMEKp6iWLAiBr8iZ9h8XceY36GgNFCPOroobwlg2d%2BrDZvgkDfwo11SqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWNeFTeUgcRHsulflKtwDOWD%2FcR9OaLahWzuZcLjDFGVDCm%2Ff2l%2FCg1pcBq0CuppMqEcavR9%2B72X6SekiOTWdWWNlHAgMrN1z63Nw0QAIrWPKsIFQ2mQ9AWSc%2BYdyDhWmvMuPobgBr0Jm90flH0p06LHx1VhBoxQGp33aIO3%2FMvoiCSDLzahj%2BQVnF8j4DwCGCblZ4zOHfBbILhxbFE%2BGefAQGJTlZB6DITGGm9LxiJzmHB9zJiJ0dbztORjfsjUZEtmJV2qKz90WsoN%2F5PdUD4cAdliTlq4zSXRfiId8D83Ab1phHmGRnxc%2FHlU2E105iRutMozgA7iQVvHkBT4ZL1FXf1fnh33p8fE8Tjf6pxLpIv7dt2UXrKlkTBET5FLvyvHWFlY%2FJJeBE4qUtZDx3%2BwcammcUdJPF4s2FoY5Yj58U7NVqnJOBTDDUVj1q%2FNcNwAjZcsu43ELS1r0HRgQhWCdqPrOsAIJhxsQ0VK4ieY2MhGXASsakWgD4sSNO2jz5tOlL6ceY7z%2BTaYdDy%2B2YpMXItSWfOwuKPug7tMh5xios3JdOI00i2W6RyU3IBBtbXH18ekXOVCiIA9LTv5vSf8sasw2Hj4ebrDv9eyNt00bIGDFAU%2BPcTUF1YvRFHR5SWWLj8e6OfSYGdgwg4TpvAY6pgFWsOor6dvPf358IUZFeAn9RnrcDwicN9mlB0jv8k6yMrUuJvXpyp%2BI0b6s%2FEs7EQPJUtebiszVi0sFu7nQ5k4hAyoIBjIk0SmcDGlT2JTA7422R5C3fAfClR3UNtJQNiKuaUpdd3n14vKcZ3oOYS4wk3H%2BotkuamzpgUPvYR1kdk4svLneKLQdMTFl2Gta9C6PnTk4UqM11FSoReWvSe%2FfQivEMHUh&X-Amz-Signature=84b808b2673a52961f7c9c287d691b24814f2dcf37f933ef8bfbabc2d9b46e33&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZN6VVSK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgyAr65ySa%2F8r4iVNe4pVphBTie%2BC69%2FLT%2FVH20owfIAiEAro7PZ%2FCBOfgpqFRuLkb18Ajbl2xdZbhqHsmLH%2BPOr4YqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBNoruSAyDpLmCiflCrcA2sOEOtgGSbq%2BSa1n8rXOuhF6vaVpxL7O%2BgzQm2WA2wmHl5Oyykj6rlkxzIg%2F9iAhgY%2BKg2S9LGIE0M0bJaXvCXB%2FV67t0exWxD7vSCLoe5oBItyWf5y8iUceGAYVO1NLqeguWRWRFwK9Cs0cYSFBdL2fIhNwrN3IQEb2VeDSZghTwnRzUEiTJyMsYCc0Zs0pXLt26XXtbsWFA%2Bi9sl4T3kmMEbKMCugx1fLM4ztEHHbezquL7mW%2Fh01MMi6ROvyUfbR5BTmAPH2VTlinhhxZiDRUchV2MsN8SZA%2Bht14icxQTGg9bApnNpVyFg9iIyP1MkiMJalyJ%2BRmZzD1fDy%2FRtTELzh2AVFOFMO2brjJyTWZn59gCRwlo94Ku7eAWFUfiQ%2F0%2FKOz5JFcM0zzuo6P6QUKS1mss40rfQYrJoziMbXaA0soQwIfKv7ucGW4t2IdWCAYD8cnbiM4wI82tpEkaxrMAo2UQpYsKAnrNOTJof%2FI91tBQ2oZe%2BWydRI%2FZE4fBZ%2BgAKtCYqkc3lgACs2HOTGGW8tO4wOuK6mlks6bE70xKdL5seG7EXkLel2WkA1qvf%2FJXeplow%2BviusMEijR9fc9rZjhvZ2Ww6flMBySq3R1JlQvDPlnWpPigHcMNWD6bwGOqUBaStInBkvNPgGfCwysKUn33SZtAfvBAqPqyYTK7vqryUEClMABj7YjoSjk19dXu%2BvTQlPt469om%2FbmsqqUN%2BFTFD7PyXMOxJc4BhnJg8xzcm0DE4DUUrRJmnIUmrxehs5fKg9KynM%2F0D8Fyo34dhGrziSszUSb0nELBcQEcltGaQKFfz0bjPbufMsm2ezO6AZNLpAnA9mfyIFAOP82BkoyEaQvp2T&X-Amz-Signature=edfc1a4f8e2a188068a6cafe35e9fd047b80ee537b17c4f9848da5bb1623c3f6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644SWIX23%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNL9Dpd6AZYQE7CMrYcaJiuo9kquaUaNObL5eU4fJI0QIgeMOQnDJ8vIzTbnOpaM8O43VEUyWgAS1DTqrauWSJ2Y8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInxgKRo%2FTyQw2BsaSrcA90GuzhrawvFigotfQRQ%2B5zdEXue4Am%2BPVVnKCSMMIQdj6aY5D8%2F8pfRTo5ZPI80Gwdho20gyBy6OixX78fZiW%2BMaHC1CTytYO6zDmgTzTUxavsjGmiz%2BiUlZvJpsGczr9QFT4LwiLPGn8Hml4LFZoNoN92WNKK2SzaugZpyEvKxynb3eXbc5%2BRaiSAQENILSnJsy%2B8DvTM%2Bq1WvkxtshDXRDkFevdM318rCOsZM4elTU49OOP%2BL3MwRxdpgCxlCD5tSDzCNXkWL9NmmvRDABI9v58vouFublp%2BUK4PykllrXPGgoZmFSMYSuvLIDlJD9m7XgBGFNnACaPM2fV1MH%2FtAJvT5KArA2kFEVt4p92YsyQBLE1oCnTYNidmPfqk9fvsQmCLTSUVfOHUIs8XCjKxOAse5Prp%2B1G2eSUdnBfozHidfzAyt5iJ3U1cduc0dSHqs%2FcE83N4cS65cuomgsZxy4iwuojBG0kaI6lUk%2BYXkMQCvDiHsoX8l58bznDbhrzW0tUWIh7cX39gqN3RmdMMkmu6N1fqcqsd%2FA0U%2BfVSzcZlKf5Qyr5Erg1QfUbg%2BpEcSAzRxK%2F4K%2BQfRQs2A%2FvVDLbWdqhjNGvtEx8s6ojhGlWFrdntjIWm6GGn%2FMLSD6bwGOqUBoX41YQ6e5Izbjh%2Fsw9Xsw4YPQXqI3%2BG7mBBqL2EvNGYDf%2BNkbBX6MUv2f7LoJrZQPXDcdnPtp7dSlxgJHyyNf9tC2RFj4AZX1IrCrmloC1vHN%2BCwFpLanEhD9ZvY9V6xJIs54%2FU95NGDXrWvwVXrn0GRFSSNGMT637yOIPcRYLgGcfuKsTYA871RqHgXXlP6dJTtdIlziDMywlTA4KZLZWLA0h6O&X-Amz-Signature=44c6826063f44afff4f8215f1e93349bdff79f4c6ad46ea599adbb467f6fcb5c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLDNKKG7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClPnxZD3TkHS2ummr7UQfBjAsSUoPoDfeXYokxTbKxkAiEAzJ6LDHLWzMB6SviU6WWkdiBt6kU7k4CEuxDyVT3BHd8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHadvkxMZcll06VWbircA3lNLnqftjl9nkJiRp4vYw%2BmUlAI1htVg%2BOR5iSTsZjQftH%2FEpX6sOc1oPHymmmwG9v42ilNTVPhp83m%2Byr%2FJqbL63I5p8HccWOETQjkrMhrj0PDe9hNbCTLRoM4GpLPohBPRbSqIBAj1iNyMlCa%2FlUlv25mydoqdmDer76iR0%2FE7MpXzxfSbUE2lSzwDFipZAg%2BMpnCq8LOZJs9l75rkyFsSOCvvAu8%2FGO8uIQ1jKSmHITA2IflLVyPI6TUtSECylvc5A%2BknxiXqIhl7tr1ULlfj4691JzKJ7Lc%2FaskQ0gbqpM%2FjC%2Fhh0OkNOytfc%2B2njYKgQ1g6kRlTfE63Nv4eXhAlE%2FofCzpuhVoKtfpE3NCfYr3WHq3uWby8mv5THIQ0XMNxoSfmM40MEpDTMr5FjVwoDkuPs17t1RM7wec0VKdWNDjYb7jhC6knSRCJppEVO4HfBv6I5wBtTuL1aSXeRY5OZgrN1hVyXGacNA1nAObKnAPikDlxPeXX69dFwvHQJfsTP2TLwoY%2FPXd0WfoMdKxKP5dLkVatg1W8kAPyn5lNrHrfJsLlLG%2BqhXoh9XJZR5g4sKmDYThMQ%2BTwNiVhoQt4Ks%2B4MPuHkwgU4GcL1ni2SdDhRD7n5hnPNwtMOCD6bwGOqUBiJec%2FIZwNSkUADNeF7doZgU7rS%2BLTkXsYAAZzuHOP%2FFQ2kt1Ki9yzVQhRyPer0VUEgkfByU7OHlTjEk48VSVF2JrYLPHiPO6s1m%2F6dxxORD0UgWN%2BHfALduvIQtCgOUSVXo7RNUKr0TK2h5jT5GmV1ERrxnqI%2BmfVFOtahdobq3nzuBuU552amm3KVKg6YmHIXhJWHKvus85MpdSGGC3pAMOqfb7&X-Amz-Signature=2d7e78a238c3c078b42321768299a981ad5566e4bfd797221fc6163275ec7e0e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRZW7IVJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBno%2BfK4HbO%2BMHntTB%2BcHHPNznMk3kcD5LkrVYpwoWXEAiBDp9RFLmLU23l1TbS1UPV3jsmlVsPUfbo2E0jBl9c9bCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8fpkMZA2DJKbuvGlKtwDwqSZVUQVH9i4sn58IEDnWmxP4MAGR7I33UZjfvaD8Ure8WKEdelsSVF0LzwQVG9C0Qe8yOZeRN%2BRBDNvhG4JEB7Wh06e58Yg6annTQ0MdFwTXiEus%2FQoqXyzwsVoBAE1sRLxMUUwsb1Nh4ItRPMH39%2FCM3dPjq5EraLuygWj7Co0xkMXJmwkQ8dAaY2V3%2Bom8Qz%2FMSEZbdz3ilqyKGa6eRA5Hjv1zZFeC92mp4Hw0CuO16z4Bf1Vu5heGW3hAJLfr6GV5NUvsYa8GngUcZxLC0smy3G8fDB1LAunoVr7nFMjgrp66zXddCTEmkNZzlOY%2BL3yPgZmkpVamHpqp%2BQJHdLnDy6dWgHoKR2ZFxmv1%2BD8c8Zpw0s%2FmdewwnBwu4YrpUHH9MSdTioJXK5VkIz0NVFUkGMEbpAkNpOtnko4jBPMiIDrVWfxrIOEvt%2F9SrjxbO%2BIjJDhGIC%2F7grn7mids1xoiQKpsEM%2BYNcYIelaYxwEBArhU48wCR0T6lLQkP1mYAaa5gEd9ujG2fpNl3N1anFx9u5wvHaSFsdMEC9GbQFKQ8Ng4J8J6sGY3lsVkw%2BF2mGXDc2497%2B2BLDnxQg1b2%2BvVNLNYOC8Dw3tsY1Z5w78mY8AxSXp7wMI7xQw6oPpvAY6pgGm%2BOwingkPJSBHfzgZUHv0eL5GagUvBKGG4YTwRD0tQFMQ05oxrpoiSA5ut8bG%2BhuGdc8wDtdjFBiyXXA%2FW4FXZ%2BaJpu0n%2FaeSy30gpYqzcexLi1%2Fz2jeLH1C4YU1VDY5r3%2F5J%2BNFlfdc3k2pkJFehjggvRGG3i41xBZv7%2B7vvksTE8O8uy5U2a7cskVC54JP2%2FUnliLHiOT9E8lqmYDMHm1H62PeO&X-Amz-Signature=60fefe72ebc909c00a58340a51aa730beefac3ff5e82979a7841acb950abb86d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRZW7IVJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBno%2BfK4HbO%2BMHntTB%2BcHHPNznMk3kcD5LkrVYpwoWXEAiBDp9RFLmLU23l1TbS1UPV3jsmlVsPUfbo2E0jBl9c9bCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8fpkMZA2DJKbuvGlKtwDwqSZVUQVH9i4sn58IEDnWmxP4MAGR7I33UZjfvaD8Ure8WKEdelsSVF0LzwQVG9C0Qe8yOZeRN%2BRBDNvhG4JEB7Wh06e58Yg6annTQ0MdFwTXiEus%2FQoqXyzwsVoBAE1sRLxMUUwsb1Nh4ItRPMH39%2FCM3dPjq5EraLuygWj7Co0xkMXJmwkQ8dAaY2V3%2Bom8Qz%2FMSEZbdz3ilqyKGa6eRA5Hjv1zZFeC92mp4Hw0CuO16z4Bf1Vu5heGW3hAJLfr6GV5NUvsYa8GngUcZxLC0smy3G8fDB1LAunoVr7nFMjgrp66zXddCTEmkNZzlOY%2BL3yPgZmkpVamHpqp%2BQJHdLnDy6dWgHoKR2ZFxmv1%2BD8c8Zpw0s%2FmdewwnBwu4YrpUHH9MSdTioJXK5VkIz0NVFUkGMEbpAkNpOtnko4jBPMiIDrVWfxrIOEvt%2F9SrjxbO%2BIjJDhGIC%2F7grn7mids1xoiQKpsEM%2BYNcYIelaYxwEBArhU48wCR0T6lLQkP1mYAaa5gEd9ujG2fpNl3N1anFx9u5wvHaSFsdMEC9GbQFKQ8Ng4J8J6sGY3lsVkw%2BF2mGXDc2497%2B2BLDnxQg1b2%2BvVNLNYOC8Dw3tsY1Z5w78mY8AxSXp7wMI7xQw6oPpvAY6pgGm%2BOwingkPJSBHfzgZUHv0eL5GagUvBKGG4YTwRD0tQFMQ05oxrpoiSA5ut8bG%2BhuGdc8wDtdjFBiyXXA%2FW4FXZ%2BaJpu0n%2FaeSy30gpYqzcexLi1%2Fz2jeLH1C4YU1VDY5r3%2F5J%2BNFlfdc3k2pkJFehjggvRGG3i41xBZv7%2B7vvksTE8O8uy5U2a7cskVC54JP2%2FUnliLHiOT9E8lqmYDMHm1H62PeO&X-Amz-Signature=56c0382f7f7d8e7820f5786afa13bcae8c4e968d3943ad665156bf2df9765870&X-Amz-SignedHeaders=host&x-id=GetObject)

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
