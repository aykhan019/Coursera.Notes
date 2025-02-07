

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGPDSP5O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCoOqDdlt6YdXrN05yrjxJD1XSD3pXoro0XqKtvT%2F%2BDegIhAPAQyMugf%2BJEkaAkIyEKO6alaVALsV%2FTtL3rO9K%2BLY6dKv8DCHsQABoMNjM3NDIzMTgzODA1Igy8%2F99yja1EQECMcJsq3ANCez5i0g4vo55SEz%2FWl5sL18jSvvmHD9h%2FoxwSpqjqO1ZVOPKBrlWzdFp3e%2B%2BZVQKGCkoEZS7iQQA0SagEQkxyolFwjofxeVgeL93Z5fSvs1yLCG9jcDZcJ30UvWs%2BKlgixV%2BFJ47CWp4v3HnvxtFq6MvAYUSysctQCmtYsAaTIwv4t4KKFO5CQtuRu4gQbGgnim%2FvNxlI2I2Dd%2FHAo0WNBZnKCDQJdPsu6vnscNhv8zpO4dhTfQDhUTlEWh7eQ0xxxuKpj9JAy%2FvSEDcNWFA3xfV%2BAJFhrM7XvS3BZ9xWKPypAhKwWM08bDofBZNzXIGrA33AOy9BbwSPqFBX%2BQOnZ1NbGJ1XSxTaTE0KEw3kYKmbzNcqHhE%2FC1RuUx%2FhIegRXdR04%2FSyf5UhL6e735cEyCdHVXHEwFTeRIXY1Idlko6jss%2FfNE1eDXLmuk0GYHVL%2FmClEpZAFHr65f5FOUVV%2FhmdueXqSp63CsyIoq5PlbAfi4pS%2B19lzB%2FJpCeHHR2P1thTDnv9MCHxLTrsLv%2FqwEgqL7nDuOTRJM7%2FwZAcupBuhPwOD3BziP7pzJLR1EmHBCwHfEpx5%2BipyYpjpvyEaDKZVmKUKXsaMvWCaeh5sm1prPn1A1LLt6rE7jCkmZm9BjqkAT9mXQjpalpXg%2BKw6G9V6HVRab7fxHXKjR6DMR3nSamr3bt6oCHcX9XpT43R1GD9yy7C6wyRXxeLndkoX3EwV6K8qlNGx2WEItmxXmKP6wo9Yy0hUuYQVMZV3LyWxyzIILycCkeIGb7CZ4OF%2BRO57GQ%2FAgJi8gmbSNF%2Bu2AZ0JxzPUN%2BHr3eu9LHJzdW6%2FFuS7lw002WWbsFN8e2oTFjXGvRkIiq&X-Amz-Signature=5faf8d72f229e953ecc0026dd77407ba692965412155a075a1fe0f103cc3b4fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGPDSP5O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCoOqDdlt6YdXrN05yrjxJD1XSD3pXoro0XqKtvT%2F%2BDegIhAPAQyMugf%2BJEkaAkIyEKO6alaVALsV%2FTtL3rO9K%2BLY6dKv8DCHsQABoMNjM3NDIzMTgzODA1Igy8%2F99yja1EQECMcJsq3ANCez5i0g4vo55SEz%2FWl5sL18jSvvmHD9h%2FoxwSpqjqO1ZVOPKBrlWzdFp3e%2B%2BZVQKGCkoEZS7iQQA0SagEQkxyolFwjofxeVgeL93Z5fSvs1yLCG9jcDZcJ30UvWs%2BKlgixV%2BFJ47CWp4v3HnvxtFq6MvAYUSysctQCmtYsAaTIwv4t4KKFO5CQtuRu4gQbGgnim%2FvNxlI2I2Dd%2FHAo0WNBZnKCDQJdPsu6vnscNhv8zpO4dhTfQDhUTlEWh7eQ0xxxuKpj9JAy%2FvSEDcNWFA3xfV%2BAJFhrM7XvS3BZ9xWKPypAhKwWM08bDofBZNzXIGrA33AOy9BbwSPqFBX%2BQOnZ1NbGJ1XSxTaTE0KEw3kYKmbzNcqHhE%2FC1RuUx%2FhIegRXdR04%2FSyf5UhL6e735cEyCdHVXHEwFTeRIXY1Idlko6jss%2FfNE1eDXLmuk0GYHVL%2FmClEpZAFHr65f5FOUVV%2FhmdueXqSp63CsyIoq5PlbAfi4pS%2B19lzB%2FJpCeHHR2P1thTDnv9MCHxLTrsLv%2FqwEgqL7nDuOTRJM7%2FwZAcupBuhPwOD3BziP7pzJLR1EmHBCwHfEpx5%2BipyYpjpvyEaDKZVmKUKXsaMvWCaeh5sm1prPn1A1LLt6rE7jCkmZm9BjqkAT9mXQjpalpXg%2BKw6G9V6HVRab7fxHXKjR6DMR3nSamr3bt6oCHcX9XpT43R1GD9yy7C6wyRXxeLndkoX3EwV6K8qlNGx2WEItmxXmKP6wo9Yy0hUuYQVMZV3LyWxyzIILycCkeIGb7CZ4OF%2BRO57GQ%2FAgJi8gmbSNF%2Bu2AZ0JxzPUN%2BHr3eu9LHJzdW6%2FFuS7lw002WWbsFN8e2oTFjXGvRkIiq&X-Amz-Signature=b1fda964b608ba3eeff57637741753a6916292af20a0ca9fb19b460a11c81bfa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGPDSP5O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCoOqDdlt6YdXrN05yrjxJD1XSD3pXoro0XqKtvT%2F%2BDegIhAPAQyMugf%2BJEkaAkIyEKO6alaVALsV%2FTtL3rO9K%2BLY6dKv8DCHsQABoMNjM3NDIzMTgzODA1Igy8%2F99yja1EQECMcJsq3ANCez5i0g4vo55SEz%2FWl5sL18jSvvmHD9h%2FoxwSpqjqO1ZVOPKBrlWzdFp3e%2B%2BZVQKGCkoEZS7iQQA0SagEQkxyolFwjofxeVgeL93Z5fSvs1yLCG9jcDZcJ30UvWs%2BKlgixV%2BFJ47CWp4v3HnvxtFq6MvAYUSysctQCmtYsAaTIwv4t4KKFO5CQtuRu4gQbGgnim%2FvNxlI2I2Dd%2FHAo0WNBZnKCDQJdPsu6vnscNhv8zpO4dhTfQDhUTlEWh7eQ0xxxuKpj9JAy%2FvSEDcNWFA3xfV%2BAJFhrM7XvS3BZ9xWKPypAhKwWM08bDofBZNzXIGrA33AOy9BbwSPqFBX%2BQOnZ1NbGJ1XSxTaTE0KEw3kYKmbzNcqHhE%2FC1RuUx%2FhIegRXdR04%2FSyf5UhL6e735cEyCdHVXHEwFTeRIXY1Idlko6jss%2FfNE1eDXLmuk0GYHVL%2FmClEpZAFHr65f5FOUVV%2FhmdueXqSp63CsyIoq5PlbAfi4pS%2B19lzB%2FJpCeHHR2P1thTDnv9MCHxLTrsLv%2FqwEgqL7nDuOTRJM7%2FwZAcupBuhPwOD3BziP7pzJLR1EmHBCwHfEpx5%2BipyYpjpvyEaDKZVmKUKXsaMvWCaeh5sm1prPn1A1LLt6rE7jCkmZm9BjqkAT9mXQjpalpXg%2BKw6G9V6HVRab7fxHXKjR6DMR3nSamr3bt6oCHcX9XpT43R1GD9yy7C6wyRXxeLndkoX3EwV6K8qlNGx2WEItmxXmKP6wo9Yy0hUuYQVMZV3LyWxyzIILycCkeIGb7CZ4OF%2BRO57GQ%2FAgJi8gmbSNF%2Bu2AZ0JxzPUN%2BHr3eu9LHJzdW6%2FFuS7lw002WWbsFN8e2oTFjXGvRkIiq&X-Amz-Signature=f82e2473a754d4b089e23bb11c4016a10d60aa8364adc4fc5de55a35c7d35bc9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RFQVTGZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCkrYK34OqI5GV2X2H7xkO%2FCFH6pJM766QJBekVQG7dEwIgdrM%2FaVmBd6mcQtccYyhf1mBWmV0tbxyFCQlMSoCGNWoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNpaKu6Eb4BBxIl8fyrcA6wsGE%2FDarGa%2F8DuGo03bKQXNqBaZilSdrM22PNhcVl6vF923Uh85XfVVJziDppryopoCpJSNCkzzIjcydhLvthMj3d%2BWBs9ty7zFOdJv8Jx6Ao0C5qd%2FlihyeenzURnlm6bLcGLYrrBGKMfgxsREArwdDjavKCnqyAj2vhyzTLe%2Bd9SyYl4PyKZZ051sF2jqGp0D%2BlQbsJCb8Amf289y3VXMzVhv%2Fh5qpMoPkUOigFy5As5GcN3qcbUfx9hLK%2F0casrk%2BadaP6lD%2FmpD8mAtBqI2TmWPFBLqW3lVKEorCQZU76zDV2CyZeE9oZW0Om8wW86hOC5Lit3iLFMKQDljOLNfwXHlOqbkt%2Bu2ppuQ6ImuYkZCppk6TLeuo8IT8aOh8r2Zo%2B7Nsd9HdT68faYhhiX0bBKyA3LuM8Z0N0rFKJD1lo0HeTq8Ywt2IzlpAXNn8zILd%2FT4n9Iypkl6A6L31IWFMKpAe1YZqNEn9zSK0MrhS02Qex3PQ%2BWMF4GjXJUPifvw7cFPefH%2BfBFRqKNKwIMEAI1WzlnJ4UDb8gl9b%2Fb7%2FxJaXmEXepn9%2B5iiPLgJNc%2FdqyyguW1MMHDXdIYoPzVnVqHewmTordXxtzjWiKtFZ%2BeUStRJ7qtH3wqMO6Zmb0GOqUBMJ2EY85uqn8lAX%2FhOwFwU4mfZAW1MfCK3cyGX0k%2BbjlAXr9AqkN%2BwukGmdjENo8KT1glEnxdGnnwh2%2FRgibTqqhiGk7ZAi2LsfRcLxc3OvzprdI5vi9veSginTlCD0KzK4uR2K%2FeSk%2FWm%2BqIFfSQQLsPpJXuvy8pu8ocyIqyrk76qEjgYjG97gvI0BvB1pNhXqoqUnvMxNSaZRc2Gte0vYmENul8&X-Amz-Signature=e2d1cbeb4b76e8d034f9ef9b0da8bf6fef659cffb8f965250f00e6e3c00cb8a3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RFQVTGZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCkrYK34OqI5GV2X2H7xkO%2FCFH6pJM766QJBekVQG7dEwIgdrM%2FaVmBd6mcQtccYyhf1mBWmV0tbxyFCQlMSoCGNWoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNpaKu6Eb4BBxIl8fyrcA6wsGE%2FDarGa%2F8DuGo03bKQXNqBaZilSdrM22PNhcVl6vF923Uh85XfVVJziDppryopoCpJSNCkzzIjcydhLvthMj3d%2BWBs9ty7zFOdJv8Jx6Ao0C5qd%2FlihyeenzURnlm6bLcGLYrrBGKMfgxsREArwdDjavKCnqyAj2vhyzTLe%2Bd9SyYl4PyKZZ051sF2jqGp0D%2BlQbsJCb8Amf289y3VXMzVhv%2Fh5qpMoPkUOigFy5As5GcN3qcbUfx9hLK%2F0casrk%2BadaP6lD%2FmpD8mAtBqI2TmWPFBLqW3lVKEorCQZU76zDV2CyZeE9oZW0Om8wW86hOC5Lit3iLFMKQDljOLNfwXHlOqbkt%2Bu2ppuQ6ImuYkZCppk6TLeuo8IT8aOh8r2Zo%2B7Nsd9HdT68faYhhiX0bBKyA3LuM8Z0N0rFKJD1lo0HeTq8Ywt2IzlpAXNn8zILd%2FT4n9Iypkl6A6L31IWFMKpAe1YZqNEn9zSK0MrhS02Qex3PQ%2BWMF4GjXJUPifvw7cFPefH%2BfBFRqKNKwIMEAI1WzlnJ4UDb8gl9b%2Fb7%2FxJaXmEXepn9%2B5iiPLgJNc%2FdqyyguW1MMHDXdIYoPzVnVqHewmTordXxtzjWiKtFZ%2BeUStRJ7qtH3wqMO6Zmb0GOqUBMJ2EY85uqn8lAX%2FhOwFwU4mfZAW1MfCK3cyGX0k%2BbjlAXr9AqkN%2BwukGmdjENo8KT1glEnxdGnnwh2%2FRgibTqqhiGk7ZAi2LsfRcLxc3OvzprdI5vi9veSginTlCD0KzK4uR2K%2FeSk%2FWm%2BqIFfSQQLsPpJXuvy8pu8ocyIqyrk76qEjgYjG97gvI0BvB1pNhXqoqUnvMxNSaZRc2Gte0vYmENul8&X-Amz-Signature=6cb3adc783e8ac874c34c9e6f28d41c12710a23779db2f459b246f8933481f66&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RFQVTGZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCkrYK34OqI5GV2X2H7xkO%2FCFH6pJM766QJBekVQG7dEwIgdrM%2FaVmBd6mcQtccYyhf1mBWmV0tbxyFCQlMSoCGNWoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNpaKu6Eb4BBxIl8fyrcA6wsGE%2FDarGa%2F8DuGo03bKQXNqBaZilSdrM22PNhcVl6vF923Uh85XfVVJziDppryopoCpJSNCkzzIjcydhLvthMj3d%2BWBs9ty7zFOdJv8Jx6Ao0C5qd%2FlihyeenzURnlm6bLcGLYrrBGKMfgxsREArwdDjavKCnqyAj2vhyzTLe%2Bd9SyYl4PyKZZ051sF2jqGp0D%2BlQbsJCb8Amf289y3VXMzVhv%2Fh5qpMoPkUOigFy5As5GcN3qcbUfx9hLK%2F0casrk%2BadaP6lD%2FmpD8mAtBqI2TmWPFBLqW3lVKEorCQZU76zDV2CyZeE9oZW0Om8wW86hOC5Lit3iLFMKQDljOLNfwXHlOqbkt%2Bu2ppuQ6ImuYkZCppk6TLeuo8IT8aOh8r2Zo%2B7Nsd9HdT68faYhhiX0bBKyA3LuM8Z0N0rFKJD1lo0HeTq8Ywt2IzlpAXNn8zILd%2FT4n9Iypkl6A6L31IWFMKpAe1YZqNEn9zSK0MrhS02Qex3PQ%2BWMF4GjXJUPifvw7cFPefH%2BfBFRqKNKwIMEAI1WzlnJ4UDb8gl9b%2Fb7%2FxJaXmEXepn9%2B5iiPLgJNc%2FdqyyguW1MMHDXdIYoPzVnVqHewmTordXxtzjWiKtFZ%2BeUStRJ7qtH3wqMO6Zmb0GOqUBMJ2EY85uqn8lAX%2FhOwFwU4mfZAW1MfCK3cyGX0k%2BbjlAXr9AqkN%2BwukGmdjENo8KT1glEnxdGnnwh2%2FRgibTqqhiGk7ZAi2LsfRcLxc3OvzprdI5vi9veSginTlCD0KzK4uR2K%2FeSk%2FWm%2BqIFfSQQLsPpJXuvy8pu8ocyIqyrk76qEjgYjG97gvI0BvB1pNhXqoqUnvMxNSaZRc2Gte0vYmENul8&X-Amz-Signature=e9f846eade05def7e697e94d32d281305e0591fd887cd54d848d5f26e37c87e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RFQVTGZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCkrYK34OqI5GV2X2H7xkO%2FCFH6pJM766QJBekVQG7dEwIgdrM%2FaVmBd6mcQtccYyhf1mBWmV0tbxyFCQlMSoCGNWoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNpaKu6Eb4BBxIl8fyrcA6wsGE%2FDarGa%2F8DuGo03bKQXNqBaZilSdrM22PNhcVl6vF923Uh85XfVVJziDppryopoCpJSNCkzzIjcydhLvthMj3d%2BWBs9ty7zFOdJv8Jx6Ao0C5qd%2FlihyeenzURnlm6bLcGLYrrBGKMfgxsREArwdDjavKCnqyAj2vhyzTLe%2Bd9SyYl4PyKZZ051sF2jqGp0D%2BlQbsJCb8Amf289y3VXMzVhv%2Fh5qpMoPkUOigFy5As5GcN3qcbUfx9hLK%2F0casrk%2BadaP6lD%2FmpD8mAtBqI2TmWPFBLqW3lVKEorCQZU76zDV2CyZeE9oZW0Om8wW86hOC5Lit3iLFMKQDljOLNfwXHlOqbkt%2Bu2ppuQ6ImuYkZCppk6TLeuo8IT8aOh8r2Zo%2B7Nsd9HdT68faYhhiX0bBKyA3LuM8Z0N0rFKJD1lo0HeTq8Ywt2IzlpAXNn8zILd%2FT4n9Iypkl6A6L31IWFMKpAe1YZqNEn9zSK0MrhS02Qex3PQ%2BWMF4GjXJUPifvw7cFPefH%2BfBFRqKNKwIMEAI1WzlnJ4UDb8gl9b%2Fb7%2FxJaXmEXepn9%2B5iiPLgJNc%2FdqyyguW1MMHDXdIYoPzVnVqHewmTordXxtzjWiKtFZ%2BeUStRJ7qtH3wqMO6Zmb0GOqUBMJ2EY85uqn8lAX%2FhOwFwU4mfZAW1MfCK3cyGX0k%2BbjlAXr9AqkN%2BwukGmdjENo8KT1glEnxdGnnwh2%2FRgibTqqhiGk7ZAi2LsfRcLxc3OvzprdI5vi9veSginTlCD0KzK4uR2K%2FeSk%2FWm%2BqIFfSQQLsPpJXuvy8pu8ocyIqyrk76qEjgYjG97gvI0BvB1pNhXqoqUnvMxNSaZRc2Gte0vYmENul8&X-Amz-Signature=27619fce8d5ee14851d12090e115a3653895d58380e7ced64e88ea9e0a781501&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RFQVTGZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCkrYK34OqI5GV2X2H7xkO%2FCFH6pJM766QJBekVQG7dEwIgdrM%2FaVmBd6mcQtccYyhf1mBWmV0tbxyFCQlMSoCGNWoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNpaKu6Eb4BBxIl8fyrcA6wsGE%2FDarGa%2F8DuGo03bKQXNqBaZilSdrM22PNhcVl6vF923Uh85XfVVJziDppryopoCpJSNCkzzIjcydhLvthMj3d%2BWBs9ty7zFOdJv8Jx6Ao0C5qd%2FlihyeenzURnlm6bLcGLYrrBGKMfgxsREArwdDjavKCnqyAj2vhyzTLe%2Bd9SyYl4PyKZZ051sF2jqGp0D%2BlQbsJCb8Amf289y3VXMzVhv%2Fh5qpMoPkUOigFy5As5GcN3qcbUfx9hLK%2F0casrk%2BadaP6lD%2FmpD8mAtBqI2TmWPFBLqW3lVKEorCQZU76zDV2CyZeE9oZW0Om8wW86hOC5Lit3iLFMKQDljOLNfwXHlOqbkt%2Bu2ppuQ6ImuYkZCppk6TLeuo8IT8aOh8r2Zo%2B7Nsd9HdT68faYhhiX0bBKyA3LuM8Z0N0rFKJD1lo0HeTq8Ywt2IzlpAXNn8zILd%2FT4n9Iypkl6A6L31IWFMKpAe1YZqNEn9zSK0MrhS02Qex3PQ%2BWMF4GjXJUPifvw7cFPefH%2BfBFRqKNKwIMEAI1WzlnJ4UDb8gl9b%2Fb7%2FxJaXmEXepn9%2B5iiPLgJNc%2FdqyyguW1MMHDXdIYoPzVnVqHewmTordXxtzjWiKtFZ%2BeUStRJ7qtH3wqMO6Zmb0GOqUBMJ2EY85uqn8lAX%2FhOwFwU4mfZAW1MfCK3cyGX0k%2BbjlAXr9AqkN%2BwukGmdjENo8KT1glEnxdGnnwh2%2FRgibTqqhiGk7ZAi2LsfRcLxc3OvzprdI5vi9veSginTlCD0KzK4uR2K%2FeSk%2FWm%2BqIFfSQQLsPpJXuvy8pu8ocyIqyrk76qEjgYjG97gvI0BvB1pNhXqoqUnvMxNSaZRc2Gte0vYmENul8&X-Amz-Signature=86d6f466e37d764174b4c1f449952500f09aebbbb1c330f4d95e2cbaaf1f07a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RFQVTGZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCkrYK34OqI5GV2X2H7xkO%2FCFH6pJM766QJBekVQG7dEwIgdrM%2FaVmBd6mcQtccYyhf1mBWmV0tbxyFCQlMSoCGNWoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNpaKu6Eb4BBxIl8fyrcA6wsGE%2FDarGa%2F8DuGo03bKQXNqBaZilSdrM22PNhcVl6vF923Uh85XfVVJziDppryopoCpJSNCkzzIjcydhLvthMj3d%2BWBs9ty7zFOdJv8Jx6Ao0C5qd%2FlihyeenzURnlm6bLcGLYrrBGKMfgxsREArwdDjavKCnqyAj2vhyzTLe%2Bd9SyYl4PyKZZ051sF2jqGp0D%2BlQbsJCb8Amf289y3VXMzVhv%2Fh5qpMoPkUOigFy5As5GcN3qcbUfx9hLK%2F0casrk%2BadaP6lD%2FmpD8mAtBqI2TmWPFBLqW3lVKEorCQZU76zDV2CyZeE9oZW0Om8wW86hOC5Lit3iLFMKQDljOLNfwXHlOqbkt%2Bu2ppuQ6ImuYkZCppk6TLeuo8IT8aOh8r2Zo%2B7Nsd9HdT68faYhhiX0bBKyA3LuM8Z0N0rFKJD1lo0HeTq8Ywt2IzlpAXNn8zILd%2FT4n9Iypkl6A6L31IWFMKpAe1YZqNEn9zSK0MrhS02Qex3PQ%2BWMF4GjXJUPifvw7cFPefH%2BfBFRqKNKwIMEAI1WzlnJ4UDb8gl9b%2Fb7%2FxJaXmEXepn9%2B5iiPLgJNc%2FdqyyguW1MMHDXdIYoPzVnVqHewmTordXxtzjWiKtFZ%2BeUStRJ7qtH3wqMO6Zmb0GOqUBMJ2EY85uqn8lAX%2FhOwFwU4mfZAW1MfCK3cyGX0k%2BbjlAXr9AqkN%2BwukGmdjENo8KT1glEnxdGnnwh2%2FRgibTqqhiGk7ZAi2LsfRcLxc3OvzprdI5vi9veSginTlCD0KzK4uR2K%2FeSk%2FWm%2BqIFfSQQLsPpJXuvy8pu8ocyIqyrk76qEjgYjG97gvI0BvB1pNhXqoqUnvMxNSaZRc2Gte0vYmENul8&X-Amz-Signature=ad8c6590f8b5705f2c0cb5c97b1eb54dff3ba0d8ba7a9c8f2341b57f6fa208d6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6O74NCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIFePGZ9qFRuCtQNA8jKeeFdWBq6ziV9Gw3ubNsJlqL9fAiEA7EmrvMPh3i4JYH5iYSJMe4wOIswI6ZgcKjMEtpCLODMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDAM3lvp7k%2FngQrYGwSrcA8cOw7Cl0%2FYFxcMqrbAM%2BQwbU6dd6r5Q9aKdo45U8R4cuEyxC1nt6DKLetfeoKw1oj2OH%2B5C3dOkcJxmlW86kET%2BILG8XaF7dcFTymSbP7C6vm1LsSvZppwwV%2BzlRJ01EFTnnvRBUzNhBcgSZSqEulNqKm05DmM0CEhL%2B%2BsSo4Ix%2BLfLJfNN8smAXLlcK9gt%2FPMm2J9WUe60rjCz3lcv0Z0be2QAk6XskGZnAJBM0TYzSpZ5PAWZpwIF%2FrjFPwAXgdy5uXw7eZ8jfXPL6erfVLAdrMxQp0A%2BXJl6dIaECBS1JBSMAid7z8a%2B5lULgT6GcaSdug%2F%2BgVz7YPOje8PFHSuldRncpkwQ3QlBAWGdDg6sJLDw%2Fcn6YpwsR0gOE1kKKEYcfAEpMzDHP90MyZXuhXdUjwXk5TZ4EbFOLQWVIClx6HwK42MSqRdq44CQ%2BK9LEsmLHQZ%2FgyEVPNwBKP%2BUQqLPStUJkISZ2xKL8HYCvfmlhD4O4kBlIFV2QTrLfWx6WLXYP%2FOe%2BsEMwYQxE0K%2FWgxn0zt9McJQB46sADFGQMvQ%2F50%2FNk4cLr4YzCh3zYTEL9kC0nUjkXP36gzf%2FgS1PAZH6hGZ5NIYu%2B5BjvnfvGBnBl4UMYPcxTwm%2FI%2BCMNSZmb0GOqUBVuekwBCpcZcdEyJAzDtaegvsFa8nJzH8%2FA%2BEvgdq86%2BL5%2B7ZCVPkqvLvu6%2FhNjcf76wcyqVR3%2FCUb1OMoWdfkFFpTyR3vU3Ht19%2BsIsxVDblDt5cz0zBfd%2B6nnhNEr8e5RsRzEAen3iE0tSMdh4G0weSE7e0ZNAlvQgLjTtihP8tKpZfXBLM0AGwjgcWxrVO8eM2UHbR6Cmg44nmA9uUbD7eAjVh&X-Amz-Signature=e5b2d2793b67b23d70ac90d8bb508b79d34d91e866c9c974dbf0b83987ece7be&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LXUDG6V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDRxLhEnAZyBwQ%2Fr1JXPo6lrkMe3prlEzTgX9H%2F2wdkQQIhAIrlPWkxp8JLOGoaJovdAVPmg5YvFKs7EFDQNvlSmX7%2BKv8DCHsQABoMNjM3NDIzMTgzODA1IgzesjRUAFmk1PSrg3Yq3ANDDHh2E566NG%2B%2FTxrt3%2FexlFK1KgiUJVtkBzdHeHqw9aGYxCw%2FbxPztPF7s9Ycmh90YOXkaLpWI4di93b0QML64xf67ubchcq0WogM7z%2Fb39adnwKybbiuBGFqJ7WIQGIn4ZwSM63WamshEKPgoOXw102mevp9L9jmeBHt74CNdjvv1vzmXzUhZXvItw3vivixMs%2BCSGpH8EPcVvBLHf7fIl9Vy2GGFvATL7NXux0Vi2%2BTwpJQ9WaSI%2B82YSIRHkIsVEg9tyFPd421AhO1DHYR8fASoj3%2F8vzwarVKch%2FmVeeR%2BcZhN%2FnDuanBX6LMYROT4mof9BDy9J5J0SW9cQ2GsDwzpzbc3AQDfkR5ELeaNe1x3utBwRtr%2FdNWYzJAFzQR9qR%2BlWUk9dny9rnfo82jEZGnyQVykq5c4ZvGiG1SapUIvtLhj9b4M12ZcqhZOYjmotmbsFfF1u%2BE0n9i01qPYRA%2F73a%2FgVv%2B%2BGipyoSd%2Bz8Et0mxwek%2BPkHz269UnQMA4lj03lPWJYR45jGfjfRNRE99y1EWH0%2FWU%2BwPHCtN%2Bw8VrF4SZKUA%2BKUiAa1v3kQCvke%2Fqyy4Ahh0vtoYzQ%2BqTEce32a5efTqXZmbC5fgBmjoAkuaPRrodfhaozD8mZm9BjqkAWmdvhIGaDER1D5x8TWw4mUf%2F0qVergVYLaY84BNUKK%2FPsgRLUvoYTjcvbkbTCgINXlevW0bzVAatKyhsis1qztvjz%2BO6EVdalImWTxVbHof9zxpjM44isEPasMhArmahdNJ5Vc1gGn1pyMaO8Ux8j3FMny%2F4oyXrDUOzufrzID7iZ9HBDKlnKDbcbcdgZST%2Bc01btGGJB9yQ3Ibj0RAIQ%2FHqoe6&X-Amz-Signature=b02b4f7a6f46d7e8abd9d29fb656821e0bafb36aae4943036809dbafe7cbac70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RFQVTGZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCkrYK34OqI5GV2X2H7xkO%2FCFH6pJM766QJBekVQG7dEwIgdrM%2FaVmBd6mcQtccYyhf1mBWmV0tbxyFCQlMSoCGNWoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNpaKu6Eb4BBxIl8fyrcA6wsGE%2FDarGa%2F8DuGo03bKQXNqBaZilSdrM22PNhcVl6vF923Uh85XfVVJziDppryopoCpJSNCkzzIjcydhLvthMj3d%2BWBs9ty7zFOdJv8Jx6Ao0C5qd%2FlihyeenzURnlm6bLcGLYrrBGKMfgxsREArwdDjavKCnqyAj2vhyzTLe%2Bd9SyYl4PyKZZ051sF2jqGp0D%2BlQbsJCb8Amf289y3VXMzVhv%2Fh5qpMoPkUOigFy5As5GcN3qcbUfx9hLK%2F0casrk%2BadaP6lD%2FmpD8mAtBqI2TmWPFBLqW3lVKEorCQZU76zDV2CyZeE9oZW0Om8wW86hOC5Lit3iLFMKQDljOLNfwXHlOqbkt%2Bu2ppuQ6ImuYkZCppk6TLeuo8IT8aOh8r2Zo%2B7Nsd9HdT68faYhhiX0bBKyA3LuM8Z0N0rFKJD1lo0HeTq8Ywt2IzlpAXNn8zILd%2FT4n9Iypkl6A6L31IWFMKpAe1YZqNEn9zSK0MrhS02Qex3PQ%2BWMF4GjXJUPifvw7cFPefH%2BfBFRqKNKwIMEAI1WzlnJ4UDb8gl9b%2Fb7%2FxJaXmEXepn9%2B5iiPLgJNc%2FdqyyguW1MMHDXdIYoPzVnVqHewmTordXxtzjWiKtFZ%2BeUStRJ7qtH3wqMO6Zmb0GOqUBMJ2EY85uqn8lAX%2FhOwFwU4mfZAW1MfCK3cyGX0k%2BbjlAXr9AqkN%2BwukGmdjENo8KT1glEnxdGnnwh2%2FRgibTqqhiGk7ZAi2LsfRcLxc3OvzprdI5vi9veSginTlCD0KzK4uR2K%2FeSk%2FWm%2BqIFfSQQLsPpJXuvy8pu8ocyIqyrk76qEjgYjG97gvI0BvB1pNhXqoqUnvMxNSaZRc2Gte0vYmENul8&X-Amz-Signature=0b918a7c857003a2f7c36b28bff63923790629c0b52513449d7115ea809ea3f9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RFQVTGZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCkrYK34OqI5GV2X2H7xkO%2FCFH6pJM766QJBekVQG7dEwIgdrM%2FaVmBd6mcQtccYyhf1mBWmV0tbxyFCQlMSoCGNWoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNpaKu6Eb4BBxIl8fyrcA6wsGE%2FDarGa%2F8DuGo03bKQXNqBaZilSdrM22PNhcVl6vF923Uh85XfVVJziDppryopoCpJSNCkzzIjcydhLvthMj3d%2BWBs9ty7zFOdJv8Jx6Ao0C5qd%2FlihyeenzURnlm6bLcGLYrrBGKMfgxsREArwdDjavKCnqyAj2vhyzTLe%2Bd9SyYl4PyKZZ051sF2jqGp0D%2BlQbsJCb8Amf289y3VXMzVhv%2Fh5qpMoPkUOigFy5As5GcN3qcbUfx9hLK%2F0casrk%2BadaP6lD%2FmpD8mAtBqI2TmWPFBLqW3lVKEorCQZU76zDV2CyZeE9oZW0Om8wW86hOC5Lit3iLFMKQDljOLNfwXHlOqbkt%2Bu2ppuQ6ImuYkZCppk6TLeuo8IT8aOh8r2Zo%2B7Nsd9HdT68faYhhiX0bBKyA3LuM8Z0N0rFKJD1lo0HeTq8Ywt2IzlpAXNn8zILd%2FT4n9Iypkl6A6L31IWFMKpAe1YZqNEn9zSK0MrhS02Qex3PQ%2BWMF4GjXJUPifvw7cFPefH%2BfBFRqKNKwIMEAI1WzlnJ4UDb8gl9b%2Fb7%2FxJaXmEXepn9%2B5iiPLgJNc%2FdqyyguW1MMHDXdIYoPzVnVqHewmTordXxtzjWiKtFZ%2BeUStRJ7qtH3wqMO6Zmb0GOqUBMJ2EY85uqn8lAX%2FhOwFwU4mfZAW1MfCK3cyGX0k%2BbjlAXr9AqkN%2BwukGmdjENo8KT1glEnxdGnnwh2%2FRgibTqqhiGk7ZAi2LsfRcLxc3OvzprdI5vi9veSginTlCD0KzK4uR2K%2FeSk%2FWm%2BqIFfSQQLsPpJXuvy8pu8ocyIqyrk76qEjgYjG97gvI0BvB1pNhXqoqUnvMxNSaZRc2Gte0vYmENul8&X-Amz-Signature=4a90d8ece575d42435656d40d59c746bd57ae951158dfb4bf78c0b3336413b24&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RFQVTGZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCkrYK34OqI5GV2X2H7xkO%2FCFH6pJM766QJBekVQG7dEwIgdrM%2FaVmBd6mcQtccYyhf1mBWmV0tbxyFCQlMSoCGNWoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNpaKu6Eb4BBxIl8fyrcA6wsGE%2FDarGa%2F8DuGo03bKQXNqBaZilSdrM22PNhcVl6vF923Uh85XfVVJziDppryopoCpJSNCkzzIjcydhLvthMj3d%2BWBs9ty7zFOdJv8Jx6Ao0C5qd%2FlihyeenzURnlm6bLcGLYrrBGKMfgxsREArwdDjavKCnqyAj2vhyzTLe%2Bd9SyYl4PyKZZ051sF2jqGp0D%2BlQbsJCb8Amf289y3VXMzVhv%2Fh5qpMoPkUOigFy5As5GcN3qcbUfx9hLK%2F0casrk%2BadaP6lD%2FmpD8mAtBqI2TmWPFBLqW3lVKEorCQZU76zDV2CyZeE9oZW0Om8wW86hOC5Lit3iLFMKQDljOLNfwXHlOqbkt%2Bu2ppuQ6ImuYkZCppk6TLeuo8IT8aOh8r2Zo%2B7Nsd9HdT68faYhhiX0bBKyA3LuM8Z0N0rFKJD1lo0HeTq8Ywt2IzlpAXNn8zILd%2FT4n9Iypkl6A6L31IWFMKpAe1YZqNEn9zSK0MrhS02Qex3PQ%2BWMF4GjXJUPifvw7cFPefH%2BfBFRqKNKwIMEAI1WzlnJ4UDb8gl9b%2Fb7%2FxJaXmEXepn9%2B5iiPLgJNc%2FdqyyguW1MMHDXdIYoPzVnVqHewmTordXxtzjWiKtFZ%2BeUStRJ7qtH3wqMO6Zmb0GOqUBMJ2EY85uqn8lAX%2FhOwFwU4mfZAW1MfCK3cyGX0k%2BbjlAXr9AqkN%2BwukGmdjENo8KT1glEnxdGnnwh2%2FRgibTqqhiGk7ZAi2LsfRcLxc3OvzprdI5vi9veSginTlCD0KzK4uR2K%2FeSk%2FWm%2BqIFfSQQLsPpJXuvy8pu8ocyIqyrk76qEjgYjG97gvI0BvB1pNhXqoqUnvMxNSaZRc2Gte0vYmENul8&X-Amz-Signature=9a7f5a1d8673aac65af02193890e9467e4b530c8ffb8202d103edeb84e21aa73&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AZZONVN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDO%2BAiJ%2FyyUAsqMdv0HRQ71qa1I6F6T3Xd9gKVeuI3rnwIhAM6jJxqewNzKZwW40Ku7kX0%2FxfJF42A7zBki1k2bO2nqKv8DCHsQABoMNjM3NDIzMTgzODA1IgzufNiaKRl3qIs%2BB9Aq3AM1gLT5TPcyat80mi%2Fc2rrjQP4MvWU7sMkMbNRP27yrnRS1372R9U9rA4rJTTVMSPikC0ZCwEITEwHWC5MRgCjRRrINiso5vfsslw2c02BYKwTXkgIc8WsvJAF4wZIwfZmapQ0tiQdXwcuXBEGQRl6nzp30nRDX6tGF5W0l8KuUFk5xU9x1FfA3WRMTGmwiSTm6cJLO5LAEjgudz6pqoSLuCsjjIwKaPfl7A9Kp9Rdz3MIYHBMiHE%2FeZOqBuucJmU96bcMqB%2B2sAGgk0e7cixid4l6%2FPTECeg6kbd2xW3kEZlUDXjdvspFMuVMWbtiW4WKo1kFWFbdScEJsO1h0eH37aJoExxD2vmG46xMIMRyvpNS%2BpwfX2BbFNTBlSDQtVtCrfLVc2cITyjhEX7MUvenO9wayidg2HxeOP09WLUa2EfV8kI4%2BQ2Ali%2BmIthThXHl0LmQfdt8JP54yd3RdpNF5KJYzrKoe4uibnvMOPCuCZWep3GUUNdgDHk4wJ6npSVDxWrRRUE9CrZtUDaA7rDlUVs6wszYc8p6nuku9oPY8lqrLr916GT9NRqI1WsLWgD5uKlOav%2B%2FW2ZU%2FjJllD80Kpxok971GPoiAxF6tonLOgrvuC98azi4lAad2qzDAmZm9BjqkAXP49eQfOgDSvlZFQxZVBCEtG82TL2ShToSMY3lKwxsBOOO4gCG8njCMgnfYaBgI%2BmrWb0FT%2FfwIDFgFcGbhUbERDSJ7FX7WHbGwRBiEPP8wFCsbNRlEODUx1BibOKPCmsPwKGTWfpdxIdS1FbCGxJ6bdsGJhUJyx6Qqi5z8O%2FhSo7%2FVezq5TeZChyKilGjsH9FQnMsrAd98ZQSEbgGmnsCS0Yx7&X-Amz-Signature=976d158ac481b4e342fbc33814d961b1c229cc1ae94ecf214f77e4e869043b9c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZLU3YF5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIH4wyTjspk5aCnOUFT4CAH%2B6Mz9Qny4EZ%2BF6BgKInN5%2FAiA0ylEFwAzjxGHcYr0VJcLXu59aYt9s%2BgD4mFSpnbOBrSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMvP4nhtVZ%2BAcV7VAKKtwD0luXVTIPqeGaJ81hoITgkVnD%2FxzTpG7OFwjUzSXFbOgWh1C1WaDeG%2BrXO2dhjmmT9O1sVMwM9r7PR73HeWl6tGnRx%2FQl4zNevG%2BSjXCgR80S7BHv7wmQtUB%2BB5ZJxIAFqmUew3vpuF2XoXYyzR8IuDjPdVi7UF66o96qiMc8Gxd14oZI78F5WTY6qvgkFr0jpBI3V8mxJawSE1t664x7tC3DEqq1QOyarhHhYkly3frfzfn5tw1XX050Frd%2BWJkisyP1TTgnVYv7amJgWaLADYZAl8uvVVaKZrFWtTHJjDRSoPlU1L383%2FdxlHUOxwxO6Cu8r6%2BUrsneYJjSGTZLOZNUhvW6k2mJZfU00XaVx9hnP7KqTDJstrb2a96571gh6fSfOEKQmRraFQGQTwXsTSPv9EAhOM%2FSKBMizMWm49gxgQbjv2g8lm8%2F%2FaybhigMHIZ7bM6JYwuyuDUbOblMja4WZI5wPiEE5jdItxYw2rOuhdHDrm7P9LTfJzBfemH7NJFJ7Gb8z%2B47SzjxkxwKWEcvLRGCB6GHbXVjIP7no%2B%2B3neOAFog6YOZUmyjsj3tvgP%2BqWj1I8U%2BVFDKCwDLDJI3Ihh303wDpsSHAfsH8YX21hcolloYk7On%2BaZ0wt5mZvQY6pgGuL6SaEw%2BRz09p4HU5C31S9%2FpBdCki7%2Fck%2BW%2FRTXBQRzMZrpa5dJFUIg1eHMpTeSrp9hobearz9JpyQ%2FtWwdDxJ27V4JXBezA8hcQzpRx5hjGcjC7fGo4KdV97jBTc0QfxrxubTSjZ9uHP%2Bxqzyp%2BWdDiITskW3%2F7Vj65lg09fh%2BA2we4zcAO0DgX%2BHJUAiIv4Y9lNQAZxXAQEYFZNkC4vguMlNYWZ&X-Amz-Signature=9ece7c1f1444dcd9e7bff82f72ebfeb6d20f0f189a1a9a28a90e9c34b1a23f1f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULFCHBIF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCZm4bLF6dUx2RyC39p9PVY5wCLOiPf%2BcfTlTnvK6rATQIgVUM6tvTFvAlvFGWmAjqOuCW3qDPbu9Csj%2BdGtLskBDgq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDGwaE3YEd3AtcMurESrcAxoH%2BiJRVrYsgdwtJNaUd55qxpiwYJYPyvixkpxm2vXCDXmBO%2FBCvhY7Nd7wmF3kMgBuOHlYmFbgoIRzMbSdbg%2FWbmXP5z5wo5hD380sviFaa4BmQ22Yjxurhs%2BpbqEW%2FvtaqB7xF7oJ1Yem4tofIsnstFnWhRRyLYagco2cOjDO9OZUsWRofQ71fSf4eFpD0RnRWeuZnDphuYYzQz6OimyBqM20Z%2BJK6789l%2FFOU5ZpbJVGSsVA3pz5afYHnKZgV3ZoYrYS%2B0CSQeHvs88s9j5W8nMc3VbkkP9GHDoLLuXcyPntIDMku%2FNIB2ccTyYXfJ%2Bjo6PKXBB0sXBiFa2ko9sTKBpf6YHTx3Boj%2BgbWWae75ipwB2BeDDFQ%2FID7jw%2FERCXudFs%2FBEZIa8oc1LpWQalPpaOimX%2FYXPlF8bdnj38giRvFs5%2F5aPPs6PfVGAPjJ4kP7V2GRrxsEQILtAuX74tGtc1bHsMR821cLfSlocbreeSekXQiA4FqqiR6sSJn3nGUNMvQPNXtxrmILmVWT%2BIXGpPtFfW%2BzzImVP3YXGT%2FZ%2FVzvHnkztK4Leri0SD5173pjpokeR8fLXIhoD0eZlakgQjMOTfEQB4Ggvg30CN0bAEwVuQtEGrasYbMJOamb0GOqUB9xHbQBisKhsB%2FDjvCiR0oFLdN42n6Vg64Cb3Tov%2F%2B5DitW2xO18EtN3FEojjm%2BY30RwyTYAvxbsP9bB%2BkDjUo3VA%2BQB%2BQ1nKKb%2F0WLkepuIoBrv%2Bre0Wy4ShrIoPRzxmRpFn%2B4TUhNIj1HaBQqu7%2BBV7aNNJ5D%2Bfim2hjDG0xOMWvwWmNd7VOH%2FYM0ByHUT7EXhlLuhmz7gvb1wdHVMNkI9oTAJp&X-Amz-Signature=ef9d7c1dcd9a5b4288b8a71d92f661e14e6d74a9bcd40ccc2e7a39a708b20413&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP2BZB7W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCfm9Q4aLPzXldP5Pe2cqSRbJo5GlAUHP5%2BKjtyGabM8AIgE55uYuGTOeAfN%2BmEzRxAgwxhQAnF5MYU%2FodG5R6wyisq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDBHL9BB1b13DkHnu7SrcA3m7LMbYwxe%2FXj2THJhgsh8V2ICCZdFWigfqhvsyu8Qtopn7Txp%2BxXszI7cteJskFbMeSIZ0%2BGTH5m8x%2FZeS13mf2EyT%2FKuTbPHlu5Uq7VXvH2ocathhzJjhO0Lzpq9hDWaPgG3usyGTRtwW8R1kBwyvye57EDu6gVvQCpYJ2%2FNMvbUX5v9jpO5av5qTXVDGrzMVYUCmY%2BJTnLcBNLOm6t9Sn619id5XMnWWhisWuRPNvdXwMEKe8GILRRSklcZL%2Bymfwr%2BVKmDI2HA29%2FiY2wKFZgrYWpzbkAyctHfXNcMaE6B1SV2nA3XnBlUK%2FgWPHDdtcAWvdChLfpNrTY8gzX7l1mnTcJwgvZm0%2F8offORJ6QEwh2NA4NyXbuE%2FnOHAxRAePpAw7IW8ci6eRgFrLZaL4%2B31KIvR7M8YcNwToDmrDz8%2Bd5Ed7km96Biz%2BZzwaZ7VHbtS5cwGASo%2BEXmEcdOhUY5NmEmUv08SsKUaXgEd4X2gYyQOtNH8yVLzi7kJK1W%2BH9eCRzdYeh%2BTezpA9Cvjh4TI3R3AWJagOJsrHQDmIHe7UqYXawt9KFzZ%2FTr4d4JqsEMRUZaQ5RPx2veE81kcoAt0H87d8Qdy5ZY0rX5YQnMRVyez3wPdGdBlMJiZmb0GOqUBAsNXgU9QPHf1oYXK73Vz0SfcEgJNlJ9OdiBIzBsM5mtiuTs8juSqEOCtiWudmdguxFZ09TGdZpIS3lv%2Bpov%2BvGrqmTn79ugOpI3mDm8XTkr%2FrmcaeWYKkFKrdtEKlK3a6pW%2FPEENCPCstUuztkvoBclblr1A%2FbPEsVM1juI56u9ZfEjDW90StbwMDYntcJldDlVK0eAV9OEjWwUsTshN84Ys1Zjc&X-Amz-Signature=9caba43e4f8b5f17fd6829efa9291657a63f354be6559499bd5afdd64b1ac336&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP2BZB7W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCfm9Q4aLPzXldP5Pe2cqSRbJo5GlAUHP5%2BKjtyGabM8AIgE55uYuGTOeAfN%2BmEzRxAgwxhQAnF5MYU%2FodG5R6wyisq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDBHL9BB1b13DkHnu7SrcA3m7LMbYwxe%2FXj2THJhgsh8V2ICCZdFWigfqhvsyu8Qtopn7Txp%2BxXszI7cteJskFbMeSIZ0%2BGTH5m8x%2FZeS13mf2EyT%2FKuTbPHlu5Uq7VXvH2ocathhzJjhO0Lzpq9hDWaPgG3usyGTRtwW8R1kBwyvye57EDu6gVvQCpYJ2%2FNMvbUX5v9jpO5av5qTXVDGrzMVYUCmY%2BJTnLcBNLOm6t9Sn619id5XMnWWhisWuRPNvdXwMEKe8GILRRSklcZL%2Bymfwr%2BVKmDI2HA29%2FiY2wKFZgrYWpzbkAyctHfXNcMaE6B1SV2nA3XnBlUK%2FgWPHDdtcAWvdChLfpNrTY8gzX7l1mnTcJwgvZm0%2F8offORJ6QEwh2NA4NyXbuE%2FnOHAxRAePpAw7IW8ci6eRgFrLZaL4%2B31KIvR7M8YcNwToDmrDz8%2Bd5Ed7km96Biz%2BZzwaZ7VHbtS5cwGASo%2BEXmEcdOhUY5NmEmUv08SsKUaXgEd4X2gYyQOtNH8yVLzi7kJK1W%2BH9eCRzdYeh%2BTezpA9Cvjh4TI3R3AWJagOJsrHQDmIHe7UqYXawt9KFzZ%2FTr4d4JqsEMRUZaQ5RPx2veE81kcoAt0H87d8Qdy5ZY0rX5YQnMRVyez3wPdGdBlMJiZmb0GOqUBAsNXgU9QPHf1oYXK73Vz0SfcEgJNlJ9OdiBIzBsM5mtiuTs8juSqEOCtiWudmdguxFZ09TGdZpIS3lv%2Bpov%2BvGrqmTn79ugOpI3mDm8XTkr%2FrmcaeWYKkFKrdtEKlK3a6pW%2FPEENCPCstUuztkvoBclblr1A%2FbPEsVM1juI56u9ZfEjDW90StbwMDYntcJldDlVK0eAV9OEjWwUsTshN84Ys1Zjc&X-Amz-Signature=e54e169140e2a746c4e518875b2a682262f3225b2b02172339576ec150225b14&X-Amz-SignedHeaders=host&x-id=GetObject)

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
