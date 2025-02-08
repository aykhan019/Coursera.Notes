

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAGVJ2OT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIHfpwn7vrWQMvWuAO51o%2BdOTpjfG%2BxJzzHMlF0H97zdJAiASqDcEjsIhfD7j%2BADjEEb3s%2BW09BNUsDn00xKT1ICa2iqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjt%2BwBS0aY%2BvQHMKkKtwDq%2B12OtJi3ukjf4VdPprrGh201aCz%2FeG2AAOdTk5tb9eHuP3ONiE42QW9gx%2FxrNUbwUZcJrfQ9YcyJsJlDvxz%2ByznRDDnQRJ3LM%2FsZYbt0nwfvcvohN0iQR%2Fcyd9akwYnqPBNZxRDzIT%2B6itBBEvu0ZzfWomHir3sY3BxyYTPHg7HbI9odPZww6yvuF8SEKANB238VmZxzoPulFlL4xZK5kQqik3ie4cU6Xo%2BUUh%2FOU5C0gKNwi4c3obq2%2BTtP%2BUyPYTw%2BhcN8DaIIQdcd%2FFj2HFngf4SQPADqeUNF4OC%2FTbOQYbXmFoJacoE%2Br0z6C3RiSDcp9baP9IzvhO9FnjcFkQGuIQDA%2BPbpYQp%2Fl3xBgNrVb4Evopz2hMEnt5KeaH42D9Tmn4EAngoswUr2iphVjF1ZhwWlz3TZH%2FJtnwqCYdYptKDxpbu92npxh2TW4naw55ocrdv2%2BwXaPvcGsSpXGfIk0jfGg6JPujVQtAE8sXzLC5xvEUdovPrB6PfeT4AXylqcWiVvO0rUSaPBsYg6tWvyTc%2B7ZpwFlW1GW6dX7K1CgQQoV3H01ERD0Gn%2FvEOiWMyb%2FVqZPcPD8YS3wziBxwTVxWDx9NSkLWlLmTE0EYmvoN%2Fxyn2Rl3t5LowkZabvQY6pgHZo%2BM9GHe28P9VNVP99gQh8WCb%2FKu6%2BiOT0zUje0usJChIe7RaDSs0AmLhCm%2B55sJr6dAiopCynkO4NS%2BKi6VrvAYkThWkuEBNJI%2F1CqTcIye9EVY2sXWI9y8EUvMhdJ%2BMZkMai4BL1FZOB5Mo7IC33KxT2m7MdmElvvG8ZjAI%2FqlZqVMN3FxXrCEPyftzekD4W1um7quXnYCd10XHcFkzX9DrLPWv&X-Amz-Signature=a2dfaad334c73ddcaf4a3f054d3976ab97cf52e030185c6d57434a6e47bff55a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAGVJ2OT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIHfpwn7vrWQMvWuAO51o%2BdOTpjfG%2BxJzzHMlF0H97zdJAiASqDcEjsIhfD7j%2BADjEEb3s%2BW09BNUsDn00xKT1ICa2iqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjt%2BwBS0aY%2BvQHMKkKtwDq%2B12OtJi3ukjf4VdPprrGh201aCz%2FeG2AAOdTk5tb9eHuP3ONiE42QW9gx%2FxrNUbwUZcJrfQ9YcyJsJlDvxz%2ByznRDDnQRJ3LM%2FsZYbt0nwfvcvohN0iQR%2Fcyd9akwYnqPBNZxRDzIT%2B6itBBEvu0ZzfWomHir3sY3BxyYTPHg7HbI9odPZww6yvuF8SEKANB238VmZxzoPulFlL4xZK5kQqik3ie4cU6Xo%2BUUh%2FOU5C0gKNwi4c3obq2%2BTtP%2BUyPYTw%2BhcN8DaIIQdcd%2FFj2HFngf4SQPADqeUNF4OC%2FTbOQYbXmFoJacoE%2Br0z6C3RiSDcp9baP9IzvhO9FnjcFkQGuIQDA%2BPbpYQp%2Fl3xBgNrVb4Evopz2hMEnt5KeaH42D9Tmn4EAngoswUr2iphVjF1ZhwWlz3TZH%2FJtnwqCYdYptKDxpbu92npxh2TW4naw55ocrdv2%2BwXaPvcGsSpXGfIk0jfGg6JPujVQtAE8sXzLC5xvEUdovPrB6PfeT4AXylqcWiVvO0rUSaPBsYg6tWvyTc%2B7ZpwFlW1GW6dX7K1CgQQoV3H01ERD0Gn%2FvEOiWMyb%2FVqZPcPD8YS3wziBxwTVxWDx9NSkLWlLmTE0EYmvoN%2Fxyn2Rl3t5LowkZabvQY6pgHZo%2BM9GHe28P9VNVP99gQh8WCb%2FKu6%2BiOT0zUje0usJChIe7RaDSs0AmLhCm%2B55sJr6dAiopCynkO4NS%2BKi6VrvAYkThWkuEBNJI%2F1CqTcIye9EVY2sXWI9y8EUvMhdJ%2BMZkMai4BL1FZOB5Mo7IC33KxT2m7MdmElvvG8ZjAI%2FqlZqVMN3FxXrCEPyftzekD4W1um7quXnYCd10XHcFkzX9DrLPWv&X-Amz-Signature=b9dc93fbb29e96bb46b45db7e36b9aeb2ca7d62e038823a69dcdfdb98a756881&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAGVJ2OT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIHfpwn7vrWQMvWuAO51o%2BdOTpjfG%2BxJzzHMlF0H97zdJAiASqDcEjsIhfD7j%2BADjEEb3s%2BW09BNUsDn00xKT1ICa2iqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjt%2BwBS0aY%2BvQHMKkKtwDq%2B12OtJi3ukjf4VdPprrGh201aCz%2FeG2AAOdTk5tb9eHuP3ONiE42QW9gx%2FxrNUbwUZcJrfQ9YcyJsJlDvxz%2ByznRDDnQRJ3LM%2FsZYbt0nwfvcvohN0iQR%2Fcyd9akwYnqPBNZxRDzIT%2B6itBBEvu0ZzfWomHir3sY3BxyYTPHg7HbI9odPZww6yvuF8SEKANB238VmZxzoPulFlL4xZK5kQqik3ie4cU6Xo%2BUUh%2FOU5C0gKNwi4c3obq2%2BTtP%2BUyPYTw%2BhcN8DaIIQdcd%2FFj2HFngf4SQPADqeUNF4OC%2FTbOQYbXmFoJacoE%2Br0z6C3RiSDcp9baP9IzvhO9FnjcFkQGuIQDA%2BPbpYQp%2Fl3xBgNrVb4Evopz2hMEnt5KeaH42D9Tmn4EAngoswUr2iphVjF1ZhwWlz3TZH%2FJtnwqCYdYptKDxpbu92npxh2TW4naw55ocrdv2%2BwXaPvcGsSpXGfIk0jfGg6JPujVQtAE8sXzLC5xvEUdovPrB6PfeT4AXylqcWiVvO0rUSaPBsYg6tWvyTc%2B7ZpwFlW1GW6dX7K1CgQQoV3H01ERD0Gn%2FvEOiWMyb%2FVqZPcPD8YS3wziBxwTVxWDx9NSkLWlLmTE0EYmvoN%2Fxyn2Rl3t5LowkZabvQY6pgHZo%2BM9GHe28P9VNVP99gQh8WCb%2FKu6%2BiOT0zUje0usJChIe7RaDSs0AmLhCm%2B55sJr6dAiopCynkO4NS%2BKi6VrvAYkThWkuEBNJI%2F1CqTcIye9EVY2sXWI9y8EUvMhdJ%2BMZkMai4BL1FZOB5Mo7IC33KxT2m7MdmElvvG8ZjAI%2FqlZqVMN3FxXrCEPyftzekD4W1um7quXnYCd10XHcFkzX9DrLPWv&X-Amz-Signature=d3f18b056fcb0b9c2387c20c8133a4d5afb850d51323cdea9d37cf2d2504f0da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3SGXY7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCWiZodtTeLQcsi3h%2BYDFvfdx3EURNFzgHxR1RkUawcNwIgTpvN9f2hE%2BD1irrWMHzwgjCpo%2FRfzqtO%2ByP0ufJYJR8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDMM4p4pUBny2XeNIircA2qOn4iJn67lIa9OrAjsVQaiG%2FSP9n7aKEO4tdCJp2OpEi8W4TghBXt83C9Y56Cue70QuEYdZdyeIMFDHTvj%2F9MPJciQxxdz9KFbzXdu%2FEB5IhrJU33gXwwgCcUXlA1H3uVoS9wAWdUTeaRgd8wcHkvXtBkFhNnVA4gtfZ%2FtO3gi4ShYVwZxbs98bUCcGnWNYT3pA02tHKEchjKPUNIUWoA4F9qDssXUpuqrnSQmSB8sEynErU0IyNS%2BdouogUvMg8NXJMnl8YG6%2FidlgmzEqVjRpG9hXSH0gJIcCv38CVppHcpOdF18wrIEoQGYnS1om7%2FSLw5EzVwPNxQs%2BrZwNZ9nIwOPiSbtqjVVb6%2FZHofAC3ihWuupaSeJozjGF5RE63d8UB3YNcvdtQbncFE85%2FweTFG4AbgcgjRa78iMGE1Q5VDgbAmP%2B6DRRpzR1yPqSYSGUqRgMHr3RtqIPEBJoIhKoCVX4o9kC2j42YNkBOHYBDY5z7oI1IbKrBnE3QgMRMewlmekcUzjwgKfn0t72u0JjElKgBechcHUe%2FGzE7ScXSdJPIqQLAgKqSKs5zuphtq9lMGkkn9%2FumKLDQzdRS6guEWLDJAUI803xcy2B2YlMAyx5C3iFBVDrWUyMPGVm70GOqUBUi2kyq1Eemte50CUce57j7%2FIgY%2FpJGFoyV%2B5g7%2BAsh6JKBlZgsGmUc7cEMSLS0KIq0vA3rS%2F%2BtuXBVB%2B%2FLXrk9QOLJsApJlH%2F6GQ43TGmb73jxVSb%2B4XAtjpzWtrx2skTd2cRJUkPoTVfWu1Bwnz31%2BUdT4PeCxVBUV7iwPSmQelYf0AQ81Tbt1Z4Bo11J9hH9vb8LcfBGhGSkirrR%2BydE%2BqB9qI&X-Amz-Signature=968aa45c748e92da8842f16888f48b28517fdc458728c107da0a74f86852b5b9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3SGXY7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCWiZodtTeLQcsi3h%2BYDFvfdx3EURNFzgHxR1RkUawcNwIgTpvN9f2hE%2BD1irrWMHzwgjCpo%2FRfzqtO%2ByP0ufJYJR8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDMM4p4pUBny2XeNIircA2qOn4iJn67lIa9OrAjsVQaiG%2FSP9n7aKEO4tdCJp2OpEi8W4TghBXt83C9Y56Cue70QuEYdZdyeIMFDHTvj%2F9MPJciQxxdz9KFbzXdu%2FEB5IhrJU33gXwwgCcUXlA1H3uVoS9wAWdUTeaRgd8wcHkvXtBkFhNnVA4gtfZ%2FtO3gi4ShYVwZxbs98bUCcGnWNYT3pA02tHKEchjKPUNIUWoA4F9qDssXUpuqrnSQmSB8sEynErU0IyNS%2BdouogUvMg8NXJMnl8YG6%2FidlgmzEqVjRpG9hXSH0gJIcCv38CVppHcpOdF18wrIEoQGYnS1om7%2FSLw5EzVwPNxQs%2BrZwNZ9nIwOPiSbtqjVVb6%2FZHofAC3ihWuupaSeJozjGF5RE63d8UB3YNcvdtQbncFE85%2FweTFG4AbgcgjRa78iMGE1Q5VDgbAmP%2B6DRRpzR1yPqSYSGUqRgMHr3RtqIPEBJoIhKoCVX4o9kC2j42YNkBOHYBDY5z7oI1IbKrBnE3QgMRMewlmekcUzjwgKfn0t72u0JjElKgBechcHUe%2FGzE7ScXSdJPIqQLAgKqSKs5zuphtq9lMGkkn9%2FumKLDQzdRS6guEWLDJAUI803xcy2B2YlMAyx5C3iFBVDrWUyMPGVm70GOqUBUi2kyq1Eemte50CUce57j7%2FIgY%2FpJGFoyV%2B5g7%2BAsh6JKBlZgsGmUc7cEMSLS0KIq0vA3rS%2F%2BtuXBVB%2B%2FLXrk9QOLJsApJlH%2F6GQ43TGmb73jxVSb%2B4XAtjpzWtrx2skTd2cRJUkPoTVfWu1Bwnz31%2BUdT4PeCxVBUV7iwPSmQelYf0AQ81Tbt1Z4Bo11J9hH9vb8LcfBGhGSkirrR%2BydE%2BqB9qI&X-Amz-Signature=911e291832ed6abfbe09d56c0d5f00f6b945fcfd7915b734ad9fab538981b03c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3SGXY7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCWiZodtTeLQcsi3h%2BYDFvfdx3EURNFzgHxR1RkUawcNwIgTpvN9f2hE%2BD1irrWMHzwgjCpo%2FRfzqtO%2ByP0ufJYJR8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDMM4p4pUBny2XeNIircA2qOn4iJn67lIa9OrAjsVQaiG%2FSP9n7aKEO4tdCJp2OpEi8W4TghBXt83C9Y56Cue70QuEYdZdyeIMFDHTvj%2F9MPJciQxxdz9KFbzXdu%2FEB5IhrJU33gXwwgCcUXlA1H3uVoS9wAWdUTeaRgd8wcHkvXtBkFhNnVA4gtfZ%2FtO3gi4ShYVwZxbs98bUCcGnWNYT3pA02tHKEchjKPUNIUWoA4F9qDssXUpuqrnSQmSB8sEynErU0IyNS%2BdouogUvMg8NXJMnl8YG6%2FidlgmzEqVjRpG9hXSH0gJIcCv38CVppHcpOdF18wrIEoQGYnS1om7%2FSLw5EzVwPNxQs%2BrZwNZ9nIwOPiSbtqjVVb6%2FZHofAC3ihWuupaSeJozjGF5RE63d8UB3YNcvdtQbncFE85%2FweTFG4AbgcgjRa78iMGE1Q5VDgbAmP%2B6DRRpzR1yPqSYSGUqRgMHr3RtqIPEBJoIhKoCVX4o9kC2j42YNkBOHYBDY5z7oI1IbKrBnE3QgMRMewlmekcUzjwgKfn0t72u0JjElKgBechcHUe%2FGzE7ScXSdJPIqQLAgKqSKs5zuphtq9lMGkkn9%2FumKLDQzdRS6guEWLDJAUI803xcy2B2YlMAyx5C3iFBVDrWUyMPGVm70GOqUBUi2kyq1Eemte50CUce57j7%2FIgY%2FpJGFoyV%2B5g7%2BAsh6JKBlZgsGmUc7cEMSLS0KIq0vA3rS%2F%2BtuXBVB%2B%2FLXrk9QOLJsApJlH%2F6GQ43TGmb73jxVSb%2B4XAtjpzWtrx2skTd2cRJUkPoTVfWu1Bwnz31%2BUdT4PeCxVBUV7iwPSmQelYf0AQ81Tbt1Z4Bo11J9hH9vb8LcfBGhGSkirrR%2BydE%2BqB9qI&X-Amz-Signature=eba13c551d0285e077f707e36a525998d897fda2a61056b934a7caa08a3281d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3SGXY7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCWiZodtTeLQcsi3h%2BYDFvfdx3EURNFzgHxR1RkUawcNwIgTpvN9f2hE%2BD1irrWMHzwgjCpo%2FRfzqtO%2ByP0ufJYJR8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDMM4p4pUBny2XeNIircA2qOn4iJn67lIa9OrAjsVQaiG%2FSP9n7aKEO4tdCJp2OpEi8W4TghBXt83C9Y56Cue70QuEYdZdyeIMFDHTvj%2F9MPJciQxxdz9KFbzXdu%2FEB5IhrJU33gXwwgCcUXlA1H3uVoS9wAWdUTeaRgd8wcHkvXtBkFhNnVA4gtfZ%2FtO3gi4ShYVwZxbs98bUCcGnWNYT3pA02tHKEchjKPUNIUWoA4F9qDssXUpuqrnSQmSB8sEynErU0IyNS%2BdouogUvMg8NXJMnl8YG6%2FidlgmzEqVjRpG9hXSH0gJIcCv38CVppHcpOdF18wrIEoQGYnS1om7%2FSLw5EzVwPNxQs%2BrZwNZ9nIwOPiSbtqjVVb6%2FZHofAC3ihWuupaSeJozjGF5RE63d8UB3YNcvdtQbncFE85%2FweTFG4AbgcgjRa78iMGE1Q5VDgbAmP%2B6DRRpzR1yPqSYSGUqRgMHr3RtqIPEBJoIhKoCVX4o9kC2j42YNkBOHYBDY5z7oI1IbKrBnE3QgMRMewlmekcUzjwgKfn0t72u0JjElKgBechcHUe%2FGzE7ScXSdJPIqQLAgKqSKs5zuphtq9lMGkkn9%2FumKLDQzdRS6guEWLDJAUI803xcy2B2YlMAyx5C3iFBVDrWUyMPGVm70GOqUBUi2kyq1Eemte50CUce57j7%2FIgY%2FpJGFoyV%2B5g7%2BAsh6JKBlZgsGmUc7cEMSLS0KIq0vA3rS%2F%2BtuXBVB%2B%2FLXrk9QOLJsApJlH%2F6GQ43TGmb73jxVSb%2B4XAtjpzWtrx2skTd2cRJUkPoTVfWu1Bwnz31%2BUdT4PeCxVBUV7iwPSmQelYf0AQ81Tbt1Z4Bo11J9hH9vb8LcfBGhGSkirrR%2BydE%2BqB9qI&X-Amz-Signature=02a04f90e066a35bf587879c7e3cfb764749fcd641bc34f1b21b8bfae4a41152&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3SGXY7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCWiZodtTeLQcsi3h%2BYDFvfdx3EURNFzgHxR1RkUawcNwIgTpvN9f2hE%2BD1irrWMHzwgjCpo%2FRfzqtO%2ByP0ufJYJR8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDMM4p4pUBny2XeNIircA2qOn4iJn67lIa9OrAjsVQaiG%2FSP9n7aKEO4tdCJp2OpEi8W4TghBXt83C9Y56Cue70QuEYdZdyeIMFDHTvj%2F9MPJciQxxdz9KFbzXdu%2FEB5IhrJU33gXwwgCcUXlA1H3uVoS9wAWdUTeaRgd8wcHkvXtBkFhNnVA4gtfZ%2FtO3gi4ShYVwZxbs98bUCcGnWNYT3pA02tHKEchjKPUNIUWoA4F9qDssXUpuqrnSQmSB8sEynErU0IyNS%2BdouogUvMg8NXJMnl8YG6%2FidlgmzEqVjRpG9hXSH0gJIcCv38CVppHcpOdF18wrIEoQGYnS1om7%2FSLw5EzVwPNxQs%2BrZwNZ9nIwOPiSbtqjVVb6%2FZHofAC3ihWuupaSeJozjGF5RE63d8UB3YNcvdtQbncFE85%2FweTFG4AbgcgjRa78iMGE1Q5VDgbAmP%2B6DRRpzR1yPqSYSGUqRgMHr3RtqIPEBJoIhKoCVX4o9kC2j42YNkBOHYBDY5z7oI1IbKrBnE3QgMRMewlmekcUzjwgKfn0t72u0JjElKgBechcHUe%2FGzE7ScXSdJPIqQLAgKqSKs5zuphtq9lMGkkn9%2FumKLDQzdRS6guEWLDJAUI803xcy2B2YlMAyx5C3iFBVDrWUyMPGVm70GOqUBUi2kyq1Eemte50CUce57j7%2FIgY%2FpJGFoyV%2B5g7%2BAsh6JKBlZgsGmUc7cEMSLS0KIq0vA3rS%2F%2BtuXBVB%2B%2FLXrk9QOLJsApJlH%2F6GQ43TGmb73jxVSb%2B4XAtjpzWtrx2skTd2cRJUkPoTVfWu1Bwnz31%2BUdT4PeCxVBUV7iwPSmQelYf0AQ81Tbt1Z4Bo11J9hH9vb8LcfBGhGSkirrR%2BydE%2BqB9qI&X-Amz-Signature=503a6225d8dcae24fbf3d90437c4f52046efa29002ee89ddc63ad1fd77345829&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3SGXY7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCWiZodtTeLQcsi3h%2BYDFvfdx3EURNFzgHxR1RkUawcNwIgTpvN9f2hE%2BD1irrWMHzwgjCpo%2FRfzqtO%2ByP0ufJYJR8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDMM4p4pUBny2XeNIircA2qOn4iJn67lIa9OrAjsVQaiG%2FSP9n7aKEO4tdCJp2OpEi8W4TghBXt83C9Y56Cue70QuEYdZdyeIMFDHTvj%2F9MPJciQxxdz9KFbzXdu%2FEB5IhrJU33gXwwgCcUXlA1H3uVoS9wAWdUTeaRgd8wcHkvXtBkFhNnVA4gtfZ%2FtO3gi4ShYVwZxbs98bUCcGnWNYT3pA02tHKEchjKPUNIUWoA4F9qDssXUpuqrnSQmSB8sEynErU0IyNS%2BdouogUvMg8NXJMnl8YG6%2FidlgmzEqVjRpG9hXSH0gJIcCv38CVppHcpOdF18wrIEoQGYnS1om7%2FSLw5EzVwPNxQs%2BrZwNZ9nIwOPiSbtqjVVb6%2FZHofAC3ihWuupaSeJozjGF5RE63d8UB3YNcvdtQbncFE85%2FweTFG4AbgcgjRa78iMGE1Q5VDgbAmP%2B6DRRpzR1yPqSYSGUqRgMHr3RtqIPEBJoIhKoCVX4o9kC2j42YNkBOHYBDY5z7oI1IbKrBnE3QgMRMewlmekcUzjwgKfn0t72u0JjElKgBechcHUe%2FGzE7ScXSdJPIqQLAgKqSKs5zuphtq9lMGkkn9%2FumKLDQzdRS6guEWLDJAUI803xcy2B2YlMAyx5C3iFBVDrWUyMPGVm70GOqUBUi2kyq1Eemte50CUce57j7%2FIgY%2FpJGFoyV%2B5g7%2BAsh6JKBlZgsGmUc7cEMSLS0KIq0vA3rS%2F%2BtuXBVB%2B%2FLXrk9QOLJsApJlH%2F6GQ43TGmb73jxVSb%2B4XAtjpzWtrx2skTd2cRJUkPoTVfWu1Bwnz31%2BUdT4PeCxVBUV7iwPSmQelYf0AQ81Tbt1Z4Bo11J9hH9vb8LcfBGhGSkirrR%2BydE%2BqB9qI&X-Amz-Signature=cb107ac40336479b114b0c27d987cdf81fabed6bad1ff96bfc724798ed4408fb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUEMZTVI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDO0WZj%2FKLPosrStAACNInR3vE9U60%2F9616EF6ccF%2F0vAIhAL72d0OKQ8VOcBG2QU2SFlwZrYmNk479h9HQwfo%2BdVCjKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdUyWlvETBgWhDS%2Fgq3APA11IdJt5%2BHByiE%2B8NxTLXTVMS8ActJXto%2BtEieltW%2F7r4W4%2B%2B32e3V8Ojmtu%2BZUO%2BHMD6%2BMTGBx5j0ZEsIn68lYi2FUT%2BXn9xt5QtlxIaTDLqM641LMpCJQMOpn2bbbhfAN7dO6DKEi9xmJNt0Dmx4pPYVfWQuxztoOp2SPXJGwcPKYWpwx357ovVfGf2fKufbfAc2Ds%2B8Z%2FbEqP4%2ByvG7UN6TgBDmVNIB4b66x1txD4TkF%2FGe9d30hxBD5erxTcWjmErkZ%2FPoROBvoYGZ%2BGxdA3180OB661qtUKPh8UCyZCXUxQcEDAuwHffpGFpUEpoXhy8h%2FjvpoUD9Qt706tkQoq7vdQCUxdXTjWDZ%2BmRT44pOlK8btxOpKNHLqwxiT%2F3dLweiyG%2F4llxO6Yk5rHEBtFrP9swrTYCYc7IpqFaKS70lT%2BCSHnaLlu4NGxaUEMqYKuNoFVTmBIFUQGsHwAqLJBUXzz5L%2B%2Bi843USzuoKu3jPHvOd45n%2BeWN%2FDT3bICQAU7ohfPC4caJAZEB8ILbFKJTrEQo%2F22%2BhGITgFhq7wvfbpaVGemnLebarXIEepZGyLPnCUw7GY1YHTP7r%2FjWLcSskUKtKJKmzYiWw5YvdMI3E%2FrAxF2z%2Fk6LRDCIlpu9BjqkAUGgNo8ZUowtU4BlXQ2uWm8PVjc3lZpfoql60creMsLSNBwu%2BZDqVDjCWrpjjHL9GLHqHryhpnIBJ%2Bz7e8xZ6ZM0OKFYzI7G7bJTK64eh48Me5xzbxeNwpodoZ%2BweMoDgKjAB%2BotV6fFyD%2BoKtEg%2B7rbv5OoKgUNJcztRt38vlCahswvnPLCfIZoxjnmJ1qxQiII54xPC2mF5GvnoQ5uKu1qJmrX&X-Amz-Signature=8b5f89bab7a798c1f872c4101d1bd018d45a37334c25455b3b205eedb42d7ea2&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBWI3YOF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQC5EICY2KX%2FlzFuaOR6vLB7wW6bvrYIrVafLHQwxdXsfAIhAKRSZklihQO0OyNYlZ2UXH5xh4axYZEbG4W%2Fcc%2FOf5PhKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxoQd2GdT5XFMzK6Gkq3AM0c7564tKi28WMUmyo2PNHBQbMYpYBIhHv1C%2BHwzcXJpEGjc9T5OPRjhDPR4Fq%2Fs6guOqfwzziYn%2B0d%2Fy2dDChCSpqa1%2FzFKCey4go09mleqm09RkxZvVQejX8tyMqR12Qm%2F77QXtJNO9%2BPxd%2B5p7rlP9X0Tp3Quf2nWRGzqzskygkIqtDJqNQvh4wLpl5Kq6JD%2BjZ8VlqnHRWMj9Yfz4BBxaqed2G8nzMn6BPW8mjywrZQvl8ynre1OrSYq%2B9lYu0%2BeyaoN2bTQkAIb1nsIIYqvfbqlIHR7R%2BLK%2FcBUtCn6tLCpJ3FGeSFGYaqZIkM5n3QozCDJ3kYH7%2FnFY%2BLSSq2%2BT8XdbSkFDd5w9qHHqGbppQH%2BcoiWDz2d%2FN5gHsaMftLfbB2HQ%2BZ%2F5Uim7GwQrSdQB7Nc8UshYegl4MrfxAXRFw2mY2mbFlVXoY6oVn9Yijr83GWGnS5kW%2FSmEARpmscMBOUAjN2hzcSkV5M2KC5tP6rsjrS4yhpseUiy1KP4xUI27fIboBm%2FCqK3HSSIxVl7fsE8yNMEDhzzqrCUQ6rsg03LHvjTMnF1H79CMM3CQLj3OBwe3cq5rTN6mClT5W3g%2F4cFRGySmtVReeGN00sxHXTYRMDhBDoY0t7zDulZu9BjqkAWFAj33TMfUMXGeSiRfVtVyuaf40kFz2rNe0LET1kOnbBhVKSMaAJFjZbsGHBN%2B0KtRoLunMHV6tQ7oGNtwAmAgn2Xw3lNO%2B7G%2FQ%2Bl8kgXJEncMFqnyVPTOyNBwoAlQ6mkShtySti%2FtPJ9dFiHYGEYH%2BKiKWEKgN4dYMtMOrRhNymkjcheudYNQEos4hwOajtHsnxvkXAf3r0e12ib0w1w8niDir&X-Amz-Signature=94f525d3033cd952ffcf46fa049bc4e036c4cb777c772fcd222be77b5b1ccd79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3SGXY7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCWiZodtTeLQcsi3h%2BYDFvfdx3EURNFzgHxR1RkUawcNwIgTpvN9f2hE%2BD1irrWMHzwgjCpo%2FRfzqtO%2ByP0ufJYJR8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDMM4p4pUBny2XeNIircA2qOn4iJn67lIa9OrAjsVQaiG%2FSP9n7aKEO4tdCJp2OpEi8W4TghBXt83C9Y56Cue70QuEYdZdyeIMFDHTvj%2F9MPJciQxxdz9KFbzXdu%2FEB5IhrJU33gXwwgCcUXlA1H3uVoS9wAWdUTeaRgd8wcHkvXtBkFhNnVA4gtfZ%2FtO3gi4ShYVwZxbs98bUCcGnWNYT3pA02tHKEchjKPUNIUWoA4F9qDssXUpuqrnSQmSB8sEynErU0IyNS%2BdouogUvMg8NXJMnl8YG6%2FidlgmzEqVjRpG9hXSH0gJIcCv38CVppHcpOdF18wrIEoQGYnS1om7%2FSLw5EzVwPNxQs%2BrZwNZ9nIwOPiSbtqjVVb6%2FZHofAC3ihWuupaSeJozjGF5RE63d8UB3YNcvdtQbncFE85%2FweTFG4AbgcgjRa78iMGE1Q5VDgbAmP%2B6DRRpzR1yPqSYSGUqRgMHr3RtqIPEBJoIhKoCVX4o9kC2j42YNkBOHYBDY5z7oI1IbKrBnE3QgMRMewlmekcUzjwgKfn0t72u0JjElKgBechcHUe%2FGzE7ScXSdJPIqQLAgKqSKs5zuphtq9lMGkkn9%2FumKLDQzdRS6guEWLDJAUI803xcy2B2YlMAyx5C3iFBVDrWUyMPGVm70GOqUBUi2kyq1Eemte50CUce57j7%2FIgY%2FpJGFoyV%2B5g7%2BAsh6JKBlZgsGmUc7cEMSLS0KIq0vA3rS%2F%2BtuXBVB%2B%2FLXrk9QOLJsApJlH%2F6GQ43TGmb73jxVSb%2B4XAtjpzWtrx2skTd2cRJUkPoTVfWu1Bwnz31%2BUdT4PeCxVBUV7iwPSmQelYf0AQ81Tbt1Z4Bo11J9hH9vb8LcfBGhGSkirrR%2BydE%2BqB9qI&X-Amz-Signature=4b3e7241e66828c3f602e13b5aff6cfab595f9125a9ba7e0ad2d393f263b2765&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3SGXY7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCWiZodtTeLQcsi3h%2BYDFvfdx3EURNFzgHxR1RkUawcNwIgTpvN9f2hE%2BD1irrWMHzwgjCpo%2FRfzqtO%2ByP0ufJYJR8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDMM4p4pUBny2XeNIircA2qOn4iJn67lIa9OrAjsVQaiG%2FSP9n7aKEO4tdCJp2OpEi8W4TghBXt83C9Y56Cue70QuEYdZdyeIMFDHTvj%2F9MPJciQxxdz9KFbzXdu%2FEB5IhrJU33gXwwgCcUXlA1H3uVoS9wAWdUTeaRgd8wcHkvXtBkFhNnVA4gtfZ%2FtO3gi4ShYVwZxbs98bUCcGnWNYT3pA02tHKEchjKPUNIUWoA4F9qDssXUpuqrnSQmSB8sEynErU0IyNS%2BdouogUvMg8NXJMnl8YG6%2FidlgmzEqVjRpG9hXSH0gJIcCv38CVppHcpOdF18wrIEoQGYnS1om7%2FSLw5EzVwPNxQs%2BrZwNZ9nIwOPiSbtqjVVb6%2FZHofAC3ihWuupaSeJozjGF5RE63d8UB3YNcvdtQbncFE85%2FweTFG4AbgcgjRa78iMGE1Q5VDgbAmP%2B6DRRpzR1yPqSYSGUqRgMHr3RtqIPEBJoIhKoCVX4o9kC2j42YNkBOHYBDY5z7oI1IbKrBnE3QgMRMewlmekcUzjwgKfn0t72u0JjElKgBechcHUe%2FGzE7ScXSdJPIqQLAgKqSKs5zuphtq9lMGkkn9%2FumKLDQzdRS6guEWLDJAUI803xcy2B2YlMAyx5C3iFBVDrWUyMPGVm70GOqUBUi2kyq1Eemte50CUce57j7%2FIgY%2FpJGFoyV%2B5g7%2BAsh6JKBlZgsGmUc7cEMSLS0KIq0vA3rS%2F%2BtuXBVB%2B%2FLXrk9QOLJsApJlH%2F6GQ43TGmb73jxVSb%2B4XAtjpzWtrx2skTd2cRJUkPoTVfWu1Bwnz31%2BUdT4PeCxVBUV7iwPSmQelYf0AQ81Tbt1Z4Bo11J9hH9vb8LcfBGhGSkirrR%2BydE%2BqB9qI&X-Amz-Signature=fba29bedfe48d48200fe19d089e8bcbbf0e9f1b075e1611b0e6e1866b8119ab8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3SGXY7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCWiZodtTeLQcsi3h%2BYDFvfdx3EURNFzgHxR1RkUawcNwIgTpvN9f2hE%2BD1irrWMHzwgjCpo%2FRfzqtO%2ByP0ufJYJR8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDMM4p4pUBny2XeNIircA2qOn4iJn67lIa9OrAjsVQaiG%2FSP9n7aKEO4tdCJp2OpEi8W4TghBXt83C9Y56Cue70QuEYdZdyeIMFDHTvj%2F9MPJciQxxdz9KFbzXdu%2FEB5IhrJU33gXwwgCcUXlA1H3uVoS9wAWdUTeaRgd8wcHkvXtBkFhNnVA4gtfZ%2FtO3gi4ShYVwZxbs98bUCcGnWNYT3pA02tHKEchjKPUNIUWoA4F9qDssXUpuqrnSQmSB8sEynErU0IyNS%2BdouogUvMg8NXJMnl8YG6%2FidlgmzEqVjRpG9hXSH0gJIcCv38CVppHcpOdF18wrIEoQGYnS1om7%2FSLw5EzVwPNxQs%2BrZwNZ9nIwOPiSbtqjVVb6%2FZHofAC3ihWuupaSeJozjGF5RE63d8UB3YNcvdtQbncFE85%2FweTFG4AbgcgjRa78iMGE1Q5VDgbAmP%2B6DRRpzR1yPqSYSGUqRgMHr3RtqIPEBJoIhKoCVX4o9kC2j42YNkBOHYBDY5z7oI1IbKrBnE3QgMRMewlmekcUzjwgKfn0t72u0JjElKgBechcHUe%2FGzE7ScXSdJPIqQLAgKqSKs5zuphtq9lMGkkn9%2FumKLDQzdRS6guEWLDJAUI803xcy2B2YlMAyx5C3iFBVDrWUyMPGVm70GOqUBUi2kyq1Eemte50CUce57j7%2FIgY%2FpJGFoyV%2B5g7%2BAsh6JKBlZgsGmUc7cEMSLS0KIq0vA3rS%2F%2BtuXBVB%2B%2FLXrk9QOLJsApJlH%2F6GQ43TGmb73jxVSb%2B4XAtjpzWtrx2skTd2cRJUkPoTVfWu1Bwnz31%2BUdT4PeCxVBUV7iwPSmQelYf0AQ81Tbt1Z4Bo11J9hH9vb8LcfBGhGSkirrR%2BydE%2BqB9qI&X-Amz-Signature=715992aa56bb01db72ba1686c99214bc37f5df3910d9a99c4e160f5150e564fc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SR56LDT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDnqLCwCu8aHp5l6qI%2BrzJAKyEu4XVgA55sZO%2Ftgte9kwIhAJi5vvFNeSLkxS8lJIKPucbK8e0wGWzXGDUTww%2B9Z2J%2FKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE43FGjDmejRHRDckq3AOZEvfjHq%2BXcI2RSsVD0xe63zd83emb1OfegMmNOtalrSaePE5K7eGiYMYNrqkAeiYRWXFFqge6znl2r6kwiMKy5nKoo%2Bha8nwWt2e2ssNVyzmnEtXqiouFlYyc7Vew26%2BtRDBIHmzAGL2iJTq9TKDI4pDZIKI5oOwdP4YFa1F3ujOO%2Fg0QoAPY8EFdLdEGojKEqBt7YpVHiHS3Ww6VGlUAfnGmi94g2YMko7j94x41msLiNxrj4fo860edj9HMBhyORCaaRpFFByYHRCfrC5Kb45nutXQKIjBgpWY0JvZDhD25mG2IHNzYVdNuv3DWYWmw4wynr09YbWBPo9%2FeM8fynV1Rn5lKtxZNZe83JO6gDYLsvh6mu7kn3d6sD4XeTfPSbFlCXhFG6PzHlfKDO3aqqhXiJpLQLhyyLHRaOff%2BB%2Fy%2FHMuGuetedLiS1zszKRtdkHYIU2T17vPPcsxAyZmYiwBwybVTBZc241PpPOvv%2BShojNpQTD0lJtYPZQ5U17fyF%2BoRUD72JoLU2o38MMICwNksNyLI279XKjXNiyhxlnwU0cy4dOacfyNqDLkGFk2jDqkRiJHIvjqpHMYeaXdQaYoBW1qXRv9aB%2Bg3Ju%2FIf8xi3fi4hQ9OBdBnJDDvlZu9BjqkASByJVVgvmVfQqNONtoP0UnIey9xUrNs3sByxBhcvJDwNov%2Fje5xbnayh0vtR8TkaA8p1onRjlVHLL4dqsmG5VHfqzfgDLAdwSnOkc8sCaoh2JGBqOgMt421L%2BmVZNlxEZXlDy%2F58aw%2BU0lk6M4p3M%2FuNUs2ftN9y87AnWwe6HWAFX307UOjinB%2BMbvrVdwv395beU1hGPIpjNLPM27jrDDH3LFV&X-Amz-Signature=8055cb1824f07496b8e3e5cf5a0ac5ae21f697855dfc3252bb69683ce7a1e057&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GQIZI6J%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIBtd%2BAylwdPp5UgmyRawazFujW0845xRwiQpYopv%2FUSeAiEAy1G%2BIUyOnfxPsptUSSbbBrwZKl%2BK1C2pAIIRoHh%2FQYUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIJ1vPXduOhGVlsE9yrcAwWI%2FXywHRJosfeNoYcTnuwAp6I4DYl3GUzn5dqYLmnt9FYxTZHJGWkH9z3kY0QAoMKGs0FzoCKVghBovpWKeXJtGnlDLndsaPFaUL81RAk9f8Ml6XptkBozuRUijvHN4MqaxyA3DSmvS8SM8wBOikOJRo1TVMkxhwj7bgsaCi3W2cE%2BrFfyIFzlNBn2N3vq69TLDOrecyxQ3FK0yyvWgSeL0PK8jUmBpO%2FufVYQJUQNJr5gcElkEn7AzX8PhP7sEWdTTrE3b4wPHFypDB5DeGUN%2FD4f1zkIfy%2FqlmPEcBLmF8%2FCmxV8ZKLs4b%2FSLdCD%2Bg25k9VSHPiLgLBtO1za6dWvAu%2FO1pZHIDMn71JcGKbPLZSVWKzSTfxSpEEDKVEQ9CzsujXktlJjCV5XOenBqBIXuWBRKj1X29hogNk3QxSsoKCH9%2BOeAa2ux3wSoUpg1IvdI6GLgqooQFpSTdaSrTRkAhrjWAgwaT9936CRjfQAY%2BYGn6pkvs5TxGeT9VDQOz8%2BXsNeTBU%2FfP7qX7%2BGYfaO2Zf%2FxzyyfBQbRNjJ5gqWtH6nTAeNQ206qZ%2BRMxcH0TboTQqY%2Bgj%2BEntqgTFNUsyoYCePCfSHq923dnYDA2KGvp3%2FLfrdPuZycVctMKKWm70GOqUBU0eVMun42nBwFPd7Jp6y5CcU2umd1N2Pwor3nOQ6DzJ1cseINAlOhSloKJT4la4y8bUBUJfh1DiocOHahdLMtzvHUKDYOaqBjmibUVQorZPRKHO6z86eZ4pLMC468suv%2B3pj05Cz1UWBnWXJXdq71mlrNnkqpxooXUJOdCDDqX%2BzY3DlnVPeCaRYXHjSGJBGJuLMka7seHOu9Zd0yk0rbgeMOjjq&X-Amz-Signature=42850c57e9ae6590dcdcd2546c739b421e70e0405859baa4a4361eb36f0dcc0e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OE5DYKO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIEyrGGTdYYriehptrM6eaxdiTEF3G4GBKUBa0eM6%2Bc9zAiEAs8XjUKsxMAoDpgBtS7NsmChX5NUXYfNAraFJ4aq8SNIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKdA64rG5Nv5UIXRXCrcA4oWxXMKdg02vekeaKitiVVCDXHkeKdS4jItuhglNvp1g01RliH8B9T5h5mKigsvuwcKwu5ErGWe0Gf7EQj1zVjOu93417Mg83iJ3ic9aip%2F%2FiCo8QapmP4u9h2MKMsGha74VaJRoxfl%2BRDW9fa0hXAh4AviWUdFfIUDk30KOzSrZRNSsl4pH3pGSvUD8GKSJnyhAuajpxtkKtVC8g4rhZVmosIgHyKDyrKPWT8d6yRF%2FMcRtqY8SqxUij7PjY2bGQkiwXo7YhJ4c3jhbU9quwTnPa1Ajjg%2FGfwzY4GONCa65ov6S3zlG1bB4TZqtff3zbvfH6D5wFr9ywe6CRqKs7C0dHq3By13M4EygoKjVE2x%2FpXA172J%2FLTDTmuIipoA0tul6hRkz1owEP6BAbx%2BxjB%2FtkdF2DCjKpRpyUmxPlSOwYjjsc3UUehRmECRwsL5Ketcy1vOAKAyMMV2RIDPuY6p5CRk2JPz713s2yZxZ4m4Pq0IsCwZYX0k8hXP0Bvo2o3FtcK2WQ%2F4jwLXGx%2BUT8vztjtXp4GAITKns%2Fbj9FT6VRlP43oDpsbCwWVYhtgOMARqbuMhRnXySp57rHgrecQm7LmztLOhJpOAnEGG%2BqQx8JjQ%2FKi5nAK%2BJsdXMOSVm70GOqUBT%2BfQiKWG3YChBwP77UofRv%2B0GTss5T%2BcFo59VaR4%2BtoDOaKxuLcz%2B2XuUJ2B%2BmMNUx9XKZBaxrgKMBxcZ6EfyG%2Fb3puIjrdzRet2hlsqJ5Oi3zMxT2eoYHMvgPxzPJ3sMNG2hUMQkGw1Ym3DzGMDDaVvl8Bbu6QuLquo6Hsx5moM1NyqgLSIpCsVn%2BUF%2B4Y0YBT6aGuRUI92voRp1s76BZ1ta2uL&X-Amz-Signature=757625bf688a6ab1a3d73c49914d3db5080b36740bd6e0cd315c29e0df918bc1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5LSMYAE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIAK2qa8isutasylxHOF%2Fr%2Bp1afxKE8JqxflVXTG54EKxAiEA70stJZ0G2jPJhRLzm5JzGlXV32vMG9KWvtMiT%2BoGY2oqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEWzSOoGLpmKOYX17ircAyfuzj9hBoAcSVERVLy4KIF2hOCE9TL6vrm4%2FHr122T%2FjFfEJLpI7%2F5wO55QeuLKTmurey4Vepbbhq6vuOotLVOaxwUWhcCUYtqQVVTzCgVXxNauSjm0iEEZ0c0p7NcHWgluLjfkb3JksAfnbu3sA%2Fk7XOf4pE9HlyzKqtnC7xxAl7rsyAtee%2BIkrlsQs7zfHXVYmjGo%2FM7DBkvHun1Dq6yo4krN9PUqkyYSUIv3dyI5DUP3AW7oY9kJOPvcl%2BMScF1JoFyDDt44uAeJZTOxP52xqcLsIWN38KMUQ5tc0IoOxOosXA0azHwvbY9DMPdZBKgYeELOHIomiP3RDVILyEmR80xlfj10XlmwiOSjs3iSdfMLx5dA2PnMlJdQcjYHewRfVB2250UVCVX%2BxI2UuNW2yeX2iqDSFzx46hduRXTvEPptFCvFwVaON4EMbVy5fVrtOj14ub9veQxRswP0xY8U5uWAl1brflkhLwCZ56CbN0Ihosstv7czDji1BDRrQiy0rwUvJtg1Ba3HB37Tdy7REv0jCplBnUfM9FGtcHdKXey3a9UnMhu1vTDRPXf1kOBBeEN7L14e1tadx1FgEuskeEoCCx3CTFunr6W6XbPHdSkZE3Xy3CxhCq3YMPCVm70GOqUBBP1wQPGW7hIpdU71oDHtexkFiHABIhIu5%2FPwKThzJiOXeBe%2BietT9Cv8UYnithIrjlrBtXJiMTZ0sbg%2BziQdjG3Haxic61iDCaq2ODlrPlwuiMQ9GjOXBYNNsxOKoTPSZeauuY1st5E89r41I2ePVymFa40U8cdAtDoLUMNUqa50VGo3wXDHPi5qIs9VckVBeXsrKAPh%2BVruIFn1NcmjjdcYHouB&X-Amz-Signature=ead3c206b6844437dac8cb45ef17e96f91f96df29d0f329577043db75e2e165b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5LSMYAE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIAK2qa8isutasylxHOF%2Fr%2Bp1afxKE8JqxflVXTG54EKxAiEA70stJZ0G2jPJhRLzm5JzGlXV32vMG9KWvtMiT%2BoGY2oqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEWzSOoGLpmKOYX17ircAyfuzj9hBoAcSVERVLy4KIF2hOCE9TL6vrm4%2FHr122T%2FjFfEJLpI7%2F5wO55QeuLKTmurey4Vepbbhq6vuOotLVOaxwUWhcCUYtqQVVTzCgVXxNauSjm0iEEZ0c0p7NcHWgluLjfkb3JksAfnbu3sA%2Fk7XOf4pE9HlyzKqtnC7xxAl7rsyAtee%2BIkrlsQs7zfHXVYmjGo%2FM7DBkvHun1Dq6yo4krN9PUqkyYSUIv3dyI5DUP3AW7oY9kJOPvcl%2BMScF1JoFyDDt44uAeJZTOxP52xqcLsIWN38KMUQ5tc0IoOxOosXA0azHwvbY9DMPdZBKgYeELOHIomiP3RDVILyEmR80xlfj10XlmwiOSjs3iSdfMLx5dA2PnMlJdQcjYHewRfVB2250UVCVX%2BxI2UuNW2yeX2iqDSFzx46hduRXTvEPptFCvFwVaON4EMbVy5fVrtOj14ub9veQxRswP0xY8U5uWAl1brflkhLwCZ56CbN0Ihosstv7czDji1BDRrQiy0rwUvJtg1Ba3HB37Tdy7REv0jCplBnUfM9FGtcHdKXey3a9UnMhu1vTDRPXf1kOBBeEN7L14e1tadx1FgEuskeEoCCx3CTFunr6W6XbPHdSkZE3Xy3CxhCq3YMPCVm70GOqUBBP1wQPGW7hIpdU71oDHtexkFiHABIhIu5%2FPwKThzJiOXeBe%2BietT9Cv8UYnithIrjlrBtXJiMTZ0sbg%2BziQdjG3Haxic61iDCaq2ODlrPlwuiMQ9GjOXBYNNsxOKoTPSZeauuY1st5E89r41I2ePVymFa40U8cdAtDoLUMNUqa50VGo3wXDHPi5qIs9VckVBeXsrKAPh%2BVruIFn1NcmjjdcYHouB&X-Amz-Signature=b49477073c8e1ab8a9240aa76a574270b3ee9adab6008f94f767ecd9fa674bd9&X-Amz-SignedHeaders=host&x-id=GetObject)

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
