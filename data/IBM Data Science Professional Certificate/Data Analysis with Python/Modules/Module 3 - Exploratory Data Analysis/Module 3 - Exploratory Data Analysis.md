

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPD3M5BS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIANBxUxc5oqH4LwRmZSh1xMzayJFxhbULnpbIZ%2BakoUDAiAerFA0wrKGVmju0kz7ZNfl%2BF%2BdlSZCKRh83s%2FsNkDsLir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMEcLDZ2GfwuPN6%2BU6KtwDzdgBDFweDrDJ0a7im2sFKAhOmUzJfx2F49AmMpARQsvlksqe8p4X%2F%2BjQUfoTDX8bOqV%2FkjoNqN2JpZkMKy9QGZAgilc9gQvoPNXICAIE8sCLvEJPD1kZlvUKK6cRK2zs2HLndlmNlyBqe%2Fx94DcQlAyB6Juzr%2B%2BTtGDSQzyIEOhR6btnanPM4TBx4JwSY7eUdgHzafCmu9sZ%2F9tH0e7fSuqJGGo0E30UjRKdJ3gZX3NsiHVO0jKam4XjKrCgbnOOKGTE%2FDlJNZGR8GboWwG5tY73WA71tLS3f5l8wkNRVZJAsRV1VKynJ1GGGyJ%2BmzFYrrCO0x7F8J1MHdwzIaiMbgEL1Rgko134Ik5kOUAu6oPvhJeMijjdIpZSNL4QRhU3TnPzqFnFwiD%2FOiHPrxodRW3jRvXzILVvctDMXT3oHKbGDsKuw3ilE8C7Id3N8bMeBdZdWEBzsUpknNWaNdpxYN2RnCPVHfctDAdwnseFlCO5G0DvSHjrk%2Brn5xBgGxyND3zH62VlKjWvQG283OR7RYxq3oKRDZ9G6SIMLnYdVD%2BmtJ9EnAQ6gq8bQ%2Bhsj2j6rQ52Xx%2B1lv41euzcLu6KOUutg1pJFmeHKRVGYmC5gQoTyIcv0kypR0FBsJww7ruOvQY6pgGqondzcon8djnjEBQjnZC%2F2KxpO5AT5c%2F3stJ82fIo12Y63Mx6DklXy6oYj%2F6OP7A9S%2FhqM%2F4MmsvH9fhwlFIxyxPYWScxgoSJzED8Zn9cglrUDMVbhBfStV0LOFJBLcd1FWMEgJg%2BAuBjUSqnjsqLDdpgX4aDpqCTEFElnnkqlzkwquu12PjH%2FVH1JUv%2FcEFPV5PWwRy2qkBGflegf7hBLs4v9DQG&X-Amz-Signature=3fcd9791a888a8686f86357f0586999ec75a399d5f5795924c2881e2fc1922ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPD3M5BS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIANBxUxc5oqH4LwRmZSh1xMzayJFxhbULnpbIZ%2BakoUDAiAerFA0wrKGVmju0kz7ZNfl%2BF%2BdlSZCKRh83s%2FsNkDsLir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMEcLDZ2GfwuPN6%2BU6KtwDzdgBDFweDrDJ0a7im2sFKAhOmUzJfx2F49AmMpARQsvlksqe8p4X%2F%2BjQUfoTDX8bOqV%2FkjoNqN2JpZkMKy9QGZAgilc9gQvoPNXICAIE8sCLvEJPD1kZlvUKK6cRK2zs2HLndlmNlyBqe%2Fx94DcQlAyB6Juzr%2B%2BTtGDSQzyIEOhR6btnanPM4TBx4JwSY7eUdgHzafCmu9sZ%2F9tH0e7fSuqJGGo0E30UjRKdJ3gZX3NsiHVO0jKam4XjKrCgbnOOKGTE%2FDlJNZGR8GboWwG5tY73WA71tLS3f5l8wkNRVZJAsRV1VKynJ1GGGyJ%2BmzFYrrCO0x7F8J1MHdwzIaiMbgEL1Rgko134Ik5kOUAu6oPvhJeMijjdIpZSNL4QRhU3TnPzqFnFwiD%2FOiHPrxodRW3jRvXzILVvctDMXT3oHKbGDsKuw3ilE8C7Id3N8bMeBdZdWEBzsUpknNWaNdpxYN2RnCPVHfctDAdwnseFlCO5G0DvSHjrk%2Brn5xBgGxyND3zH62VlKjWvQG283OR7RYxq3oKRDZ9G6SIMLnYdVD%2BmtJ9EnAQ6gq8bQ%2Bhsj2j6rQ52Xx%2B1lv41euzcLu6KOUutg1pJFmeHKRVGYmC5gQoTyIcv0kypR0FBsJww7ruOvQY6pgGqondzcon8djnjEBQjnZC%2F2KxpO5AT5c%2F3stJ82fIo12Y63Mx6DklXy6oYj%2F6OP7A9S%2FhqM%2F4MmsvH9fhwlFIxyxPYWScxgoSJzED8Zn9cglrUDMVbhBfStV0LOFJBLcd1FWMEgJg%2BAuBjUSqnjsqLDdpgX4aDpqCTEFElnnkqlzkwquu12PjH%2FVH1JUv%2FcEFPV5PWwRy2qkBGflegf7hBLs4v9DQG&X-Amz-Signature=7b307f8dff6b5d51667dbebf1344f33746ae1224146a47a3801a103445fc3d9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPD3M5BS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIANBxUxc5oqH4LwRmZSh1xMzayJFxhbULnpbIZ%2BakoUDAiAerFA0wrKGVmju0kz7ZNfl%2BF%2BdlSZCKRh83s%2FsNkDsLir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMEcLDZ2GfwuPN6%2BU6KtwDzdgBDFweDrDJ0a7im2sFKAhOmUzJfx2F49AmMpARQsvlksqe8p4X%2F%2BjQUfoTDX8bOqV%2FkjoNqN2JpZkMKy9QGZAgilc9gQvoPNXICAIE8sCLvEJPD1kZlvUKK6cRK2zs2HLndlmNlyBqe%2Fx94DcQlAyB6Juzr%2B%2BTtGDSQzyIEOhR6btnanPM4TBx4JwSY7eUdgHzafCmu9sZ%2F9tH0e7fSuqJGGo0E30UjRKdJ3gZX3NsiHVO0jKam4XjKrCgbnOOKGTE%2FDlJNZGR8GboWwG5tY73WA71tLS3f5l8wkNRVZJAsRV1VKynJ1GGGyJ%2BmzFYrrCO0x7F8J1MHdwzIaiMbgEL1Rgko134Ik5kOUAu6oPvhJeMijjdIpZSNL4QRhU3TnPzqFnFwiD%2FOiHPrxodRW3jRvXzILVvctDMXT3oHKbGDsKuw3ilE8C7Id3N8bMeBdZdWEBzsUpknNWaNdpxYN2RnCPVHfctDAdwnseFlCO5G0DvSHjrk%2Brn5xBgGxyND3zH62VlKjWvQG283OR7RYxq3oKRDZ9G6SIMLnYdVD%2BmtJ9EnAQ6gq8bQ%2Bhsj2j6rQ52Xx%2B1lv41euzcLu6KOUutg1pJFmeHKRVGYmC5gQoTyIcv0kypR0FBsJww7ruOvQY6pgGqondzcon8djnjEBQjnZC%2F2KxpO5AT5c%2F3stJ82fIo12Y63Mx6DklXy6oYj%2F6OP7A9S%2FhqM%2F4MmsvH9fhwlFIxyxPYWScxgoSJzED8Zn9cglrUDMVbhBfStV0LOFJBLcd1FWMEgJg%2BAuBjUSqnjsqLDdpgX4aDpqCTEFElnnkqlzkwquu12PjH%2FVH1JUv%2FcEFPV5PWwRy2qkBGflegf7hBLs4v9DQG&X-Amz-Signature=19c3123b9150b43b97299f81b32c0143fc93d9a64facbce7c6e5eef4e592514f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RQTQCCP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHX5aQy8bHqFEDq7Lj7B4Rsx9P%2FxUbUwuJ5ka%2Fyzh3upAiAjBKrVxMWpuu1KvOw1fdER4isZQgzEtVFuxRIiVC7zKyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMerDV5uJ40JN6BAVEKtwD3VTvukd8ceB3eMxpoEGRKbtgfG7ZPpQYhO0FzfYfZIG5mMih%2BbnEU7K1C6O1AZ30TZXJwqJTtI1gNxW3DUh0HjVAvgu7kXlTA9ZMDqjJ%2BLNeXm04%2B%2BcrUq%2BuPRqem8nGohMLZCIS6%2BAqsdXD1z9QzS0qiPmEdiqvOthZHZfWXg%2BdqYLhDuCycVRDXUoAFiHttQ2thGXMr9hMzPDOXZzKs1PZvDzKaH%2BaM6AEo6BWc%2Bqjh%2F4kgIbgsqmNlUqgp58fYklj55cFbnEkMYuyjebOqx09RnWBFQoTUnx3wj6Qinu9XkpCZZ%2B7Cms5gl41oOTQX%2BE1ayulfHpTdaT6wrSAjNoX8OAeWAJzBaCQu1UwQ3L26PEue6u5fJzi%2Fvm7huKAceMxLtvmLuuPuaO5wlXL9L%2BdUitvrndxfnXwHSVQWuzZW3okMXTajvg9CulKe0F2XSK9n4%2BcCrr47XOcrct1KlyOEdwJ%2FPFkLEWwtxIr%2BmxEBzVqo3V1gN6FcLBa2B1HtPEAc604wNZr89D%2Bd5JOGk8I7lsnPGhKJITluC98Gmvn5fpblewWjrzq7%2FGiDPO11X5LtDHNNz%2Be18dlt1KKJICrXVsNTynIl3K7T8mC%2FFKBezycQ%2FkyDKIefcYwrryOvQY6pgGX4hCEFk6BL%2F%2BOWFhS8AQ1Ag39JVTGOj868dC3e%2B%2FvB8XIAqFnoEhonDHtbwZbEEtzTCOhK4WfhILyEaoKgRjJ70igEmF3hkXEtQ3AWlB2y0rVhc4hJ7zn%2B8iTlbp%2BXP6Kb7KGPQoPh%2BV4qtkm13oif90bZxkGPJDnL3ML5ltFXs3TWWOFaRKYZ1n6DXeZSS3At2Jn8mhL7YQpOnQY6pcMRAzi605u&X-Amz-Signature=e2b250e4e6d90cc06e7a6cb2865c8e841840ad6579cc3cdd4f541d80bfb53e26&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RQTQCCP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHX5aQy8bHqFEDq7Lj7B4Rsx9P%2FxUbUwuJ5ka%2Fyzh3upAiAjBKrVxMWpuu1KvOw1fdER4isZQgzEtVFuxRIiVC7zKyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMerDV5uJ40JN6BAVEKtwD3VTvukd8ceB3eMxpoEGRKbtgfG7ZPpQYhO0FzfYfZIG5mMih%2BbnEU7K1C6O1AZ30TZXJwqJTtI1gNxW3DUh0HjVAvgu7kXlTA9ZMDqjJ%2BLNeXm04%2B%2BcrUq%2BuPRqem8nGohMLZCIS6%2BAqsdXD1z9QzS0qiPmEdiqvOthZHZfWXg%2BdqYLhDuCycVRDXUoAFiHttQ2thGXMr9hMzPDOXZzKs1PZvDzKaH%2BaM6AEo6BWc%2Bqjh%2F4kgIbgsqmNlUqgp58fYklj55cFbnEkMYuyjebOqx09RnWBFQoTUnx3wj6Qinu9XkpCZZ%2B7Cms5gl41oOTQX%2BE1ayulfHpTdaT6wrSAjNoX8OAeWAJzBaCQu1UwQ3L26PEue6u5fJzi%2Fvm7huKAceMxLtvmLuuPuaO5wlXL9L%2BdUitvrndxfnXwHSVQWuzZW3okMXTajvg9CulKe0F2XSK9n4%2BcCrr47XOcrct1KlyOEdwJ%2FPFkLEWwtxIr%2BmxEBzVqo3V1gN6FcLBa2B1HtPEAc604wNZr89D%2Bd5JOGk8I7lsnPGhKJITluC98Gmvn5fpblewWjrzq7%2FGiDPO11X5LtDHNNz%2Be18dlt1KKJICrXVsNTynIl3K7T8mC%2FFKBezycQ%2FkyDKIefcYwrryOvQY6pgGX4hCEFk6BL%2F%2BOWFhS8AQ1Ag39JVTGOj868dC3e%2B%2FvB8XIAqFnoEhonDHtbwZbEEtzTCOhK4WfhILyEaoKgRjJ70igEmF3hkXEtQ3AWlB2y0rVhc4hJ7zn%2B8iTlbp%2BXP6Kb7KGPQoPh%2BV4qtkm13oif90bZxkGPJDnL3ML5ltFXs3TWWOFaRKYZ1n6DXeZSS3At2Jn8mhL7YQpOnQY6pcMRAzi605u&X-Amz-Signature=df0ab83e0a5165f76a8d0e5b0b2d35d4248f2beb34312af372c057511756e811&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RQTQCCP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHX5aQy8bHqFEDq7Lj7B4Rsx9P%2FxUbUwuJ5ka%2Fyzh3upAiAjBKrVxMWpuu1KvOw1fdER4isZQgzEtVFuxRIiVC7zKyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMerDV5uJ40JN6BAVEKtwD3VTvukd8ceB3eMxpoEGRKbtgfG7ZPpQYhO0FzfYfZIG5mMih%2BbnEU7K1C6O1AZ30TZXJwqJTtI1gNxW3DUh0HjVAvgu7kXlTA9ZMDqjJ%2BLNeXm04%2B%2BcrUq%2BuPRqem8nGohMLZCIS6%2BAqsdXD1z9QzS0qiPmEdiqvOthZHZfWXg%2BdqYLhDuCycVRDXUoAFiHttQ2thGXMr9hMzPDOXZzKs1PZvDzKaH%2BaM6AEo6BWc%2Bqjh%2F4kgIbgsqmNlUqgp58fYklj55cFbnEkMYuyjebOqx09RnWBFQoTUnx3wj6Qinu9XkpCZZ%2B7Cms5gl41oOTQX%2BE1ayulfHpTdaT6wrSAjNoX8OAeWAJzBaCQu1UwQ3L26PEue6u5fJzi%2Fvm7huKAceMxLtvmLuuPuaO5wlXL9L%2BdUitvrndxfnXwHSVQWuzZW3okMXTajvg9CulKe0F2XSK9n4%2BcCrr47XOcrct1KlyOEdwJ%2FPFkLEWwtxIr%2BmxEBzVqo3V1gN6FcLBa2B1HtPEAc604wNZr89D%2Bd5JOGk8I7lsnPGhKJITluC98Gmvn5fpblewWjrzq7%2FGiDPO11X5LtDHNNz%2Be18dlt1KKJICrXVsNTynIl3K7T8mC%2FFKBezycQ%2FkyDKIefcYwrryOvQY6pgGX4hCEFk6BL%2F%2BOWFhS8AQ1Ag39JVTGOj868dC3e%2B%2FvB8XIAqFnoEhonDHtbwZbEEtzTCOhK4WfhILyEaoKgRjJ70igEmF3hkXEtQ3AWlB2y0rVhc4hJ7zn%2B8iTlbp%2BXP6Kb7KGPQoPh%2BV4qtkm13oif90bZxkGPJDnL3ML5ltFXs3TWWOFaRKYZ1n6DXeZSS3At2Jn8mhL7YQpOnQY6pcMRAzi605u&X-Amz-Signature=d84b3bf5c1ed937beeba2bf99c44c88edef5854b2080dab648030278b7c75b07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RQTQCCP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHX5aQy8bHqFEDq7Lj7B4Rsx9P%2FxUbUwuJ5ka%2Fyzh3upAiAjBKrVxMWpuu1KvOw1fdER4isZQgzEtVFuxRIiVC7zKyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMerDV5uJ40JN6BAVEKtwD3VTvukd8ceB3eMxpoEGRKbtgfG7ZPpQYhO0FzfYfZIG5mMih%2BbnEU7K1C6O1AZ30TZXJwqJTtI1gNxW3DUh0HjVAvgu7kXlTA9ZMDqjJ%2BLNeXm04%2B%2BcrUq%2BuPRqem8nGohMLZCIS6%2BAqsdXD1z9QzS0qiPmEdiqvOthZHZfWXg%2BdqYLhDuCycVRDXUoAFiHttQ2thGXMr9hMzPDOXZzKs1PZvDzKaH%2BaM6AEo6BWc%2Bqjh%2F4kgIbgsqmNlUqgp58fYklj55cFbnEkMYuyjebOqx09RnWBFQoTUnx3wj6Qinu9XkpCZZ%2B7Cms5gl41oOTQX%2BE1ayulfHpTdaT6wrSAjNoX8OAeWAJzBaCQu1UwQ3L26PEue6u5fJzi%2Fvm7huKAceMxLtvmLuuPuaO5wlXL9L%2BdUitvrndxfnXwHSVQWuzZW3okMXTajvg9CulKe0F2XSK9n4%2BcCrr47XOcrct1KlyOEdwJ%2FPFkLEWwtxIr%2BmxEBzVqo3V1gN6FcLBa2B1HtPEAc604wNZr89D%2Bd5JOGk8I7lsnPGhKJITluC98Gmvn5fpblewWjrzq7%2FGiDPO11X5LtDHNNz%2Be18dlt1KKJICrXVsNTynIl3K7T8mC%2FFKBezycQ%2FkyDKIefcYwrryOvQY6pgGX4hCEFk6BL%2F%2BOWFhS8AQ1Ag39JVTGOj868dC3e%2B%2FvB8XIAqFnoEhonDHtbwZbEEtzTCOhK4WfhILyEaoKgRjJ70igEmF3hkXEtQ3AWlB2y0rVhc4hJ7zn%2B8iTlbp%2BXP6Kb7KGPQoPh%2BV4qtkm13oif90bZxkGPJDnL3ML5ltFXs3TWWOFaRKYZ1n6DXeZSS3At2Jn8mhL7YQpOnQY6pcMRAzi605u&X-Amz-Signature=fb75187b737dc4c0e47a27ff29b1deaa0cb028be199770e04d4fc9d9e2a70a1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RQTQCCP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHX5aQy8bHqFEDq7Lj7B4Rsx9P%2FxUbUwuJ5ka%2Fyzh3upAiAjBKrVxMWpuu1KvOw1fdER4isZQgzEtVFuxRIiVC7zKyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMerDV5uJ40JN6BAVEKtwD3VTvukd8ceB3eMxpoEGRKbtgfG7ZPpQYhO0FzfYfZIG5mMih%2BbnEU7K1C6O1AZ30TZXJwqJTtI1gNxW3DUh0HjVAvgu7kXlTA9ZMDqjJ%2BLNeXm04%2B%2BcrUq%2BuPRqem8nGohMLZCIS6%2BAqsdXD1z9QzS0qiPmEdiqvOthZHZfWXg%2BdqYLhDuCycVRDXUoAFiHttQ2thGXMr9hMzPDOXZzKs1PZvDzKaH%2BaM6AEo6BWc%2Bqjh%2F4kgIbgsqmNlUqgp58fYklj55cFbnEkMYuyjebOqx09RnWBFQoTUnx3wj6Qinu9XkpCZZ%2B7Cms5gl41oOTQX%2BE1ayulfHpTdaT6wrSAjNoX8OAeWAJzBaCQu1UwQ3L26PEue6u5fJzi%2Fvm7huKAceMxLtvmLuuPuaO5wlXL9L%2BdUitvrndxfnXwHSVQWuzZW3okMXTajvg9CulKe0F2XSK9n4%2BcCrr47XOcrct1KlyOEdwJ%2FPFkLEWwtxIr%2BmxEBzVqo3V1gN6FcLBa2B1HtPEAc604wNZr89D%2Bd5JOGk8I7lsnPGhKJITluC98Gmvn5fpblewWjrzq7%2FGiDPO11X5LtDHNNz%2Be18dlt1KKJICrXVsNTynIl3K7T8mC%2FFKBezycQ%2FkyDKIefcYwrryOvQY6pgGX4hCEFk6BL%2F%2BOWFhS8AQ1Ag39JVTGOj868dC3e%2B%2FvB8XIAqFnoEhonDHtbwZbEEtzTCOhK4WfhILyEaoKgRjJ70igEmF3hkXEtQ3AWlB2y0rVhc4hJ7zn%2B8iTlbp%2BXP6Kb7KGPQoPh%2BV4qtkm13oif90bZxkGPJDnL3ML5ltFXs3TWWOFaRKYZ1n6DXeZSS3At2Jn8mhL7YQpOnQY6pcMRAzi605u&X-Amz-Signature=e10ae5216fc239a3594c450c8edfe8a03b6abf2d0b8eb68981acfde1b76b83f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RQTQCCP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHX5aQy8bHqFEDq7Lj7B4Rsx9P%2FxUbUwuJ5ka%2Fyzh3upAiAjBKrVxMWpuu1KvOw1fdER4isZQgzEtVFuxRIiVC7zKyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMerDV5uJ40JN6BAVEKtwD3VTvukd8ceB3eMxpoEGRKbtgfG7ZPpQYhO0FzfYfZIG5mMih%2BbnEU7K1C6O1AZ30TZXJwqJTtI1gNxW3DUh0HjVAvgu7kXlTA9ZMDqjJ%2BLNeXm04%2B%2BcrUq%2BuPRqem8nGohMLZCIS6%2BAqsdXD1z9QzS0qiPmEdiqvOthZHZfWXg%2BdqYLhDuCycVRDXUoAFiHttQ2thGXMr9hMzPDOXZzKs1PZvDzKaH%2BaM6AEo6BWc%2Bqjh%2F4kgIbgsqmNlUqgp58fYklj55cFbnEkMYuyjebOqx09RnWBFQoTUnx3wj6Qinu9XkpCZZ%2B7Cms5gl41oOTQX%2BE1ayulfHpTdaT6wrSAjNoX8OAeWAJzBaCQu1UwQ3L26PEue6u5fJzi%2Fvm7huKAceMxLtvmLuuPuaO5wlXL9L%2BdUitvrndxfnXwHSVQWuzZW3okMXTajvg9CulKe0F2XSK9n4%2BcCrr47XOcrct1KlyOEdwJ%2FPFkLEWwtxIr%2BmxEBzVqo3V1gN6FcLBa2B1HtPEAc604wNZr89D%2Bd5JOGk8I7lsnPGhKJITluC98Gmvn5fpblewWjrzq7%2FGiDPO11X5LtDHNNz%2Be18dlt1KKJICrXVsNTynIl3K7T8mC%2FFKBezycQ%2FkyDKIefcYwrryOvQY6pgGX4hCEFk6BL%2F%2BOWFhS8AQ1Ag39JVTGOj868dC3e%2B%2FvB8XIAqFnoEhonDHtbwZbEEtzTCOhK4WfhILyEaoKgRjJ70igEmF3hkXEtQ3AWlB2y0rVhc4hJ7zn%2B8iTlbp%2BXP6Kb7KGPQoPh%2BV4qtkm13oif90bZxkGPJDnL3ML5ltFXs3TWWOFaRKYZ1n6DXeZSS3At2Jn8mhL7YQpOnQY6pcMRAzi605u&X-Amz-Signature=d0d86eaf9a41487ce21bfef2bddbff7ca0395cf9a2ab20a56a4b13df037e64dd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWFJU5CQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCV8CH905Rk%2F8WUGsfbxMA4iwHqJWLZBjObddEgs4c7twIhAPfztVw4Wz0yi%2FivYr0HTECUXY5dPnhbb%2B1KXRoOzIplKv8DCEoQABoMNjM3NDIzMTgzODA1IgzdVcugZ%2FyduyUP9LAq3AMqgVSAMdw%2BOM0za04TnYQpyKEm7xDbdBvX4%2BTma%2B%2FniRUem70EC3psSZ%2FdpHcT4pf2T6Qq%2BAa85GQuadPf1v%2FaQZc71RxuEoDaY41zRqyRfUXnAzpgXquCq0JEyxzrE5o6BXyg6uYtk6xSkq4eLaGiWRmXwa7uVNNaZlZnkZA3%2FXtWm1rvJsRg6pTlJHgIvzDDXSo2i26%2BYTdMZSqS2Qv%2FB7oPJV12qvcrDDQ7sa8tRE4xK5Lu5uyv33WX51gSNvgCdE%2Bm2xxU7Nd2uRfvRxtpEvceNMVEF1JNlBaL9n6btb0JTzVjP3PCNS4j57PgisU%2FC1anabVrnba%2B42N4eehs0IOXbmN5RJH39D1RkJ%2FumG4ZbFICBIYfLbKnhuRZjMPWxjrYWa48aAOAREEsA%2FXaMFkz0mg5XkdEtAzl5MYxbs4k%2FywGNElqtnOgMNsCofh6KOFTX1f9CNR6SwYE9kPaA4WZ%2FKUaSFy8LBDSMuWFy01REdr3ddulgrivJ9SNcD3zyKua69%2FqsIOYvVeClhA8hnr%2BdZ29iZdwtwdweA1cC9VxZyCDuV5tfmU3BL5d5CHcDyqE9SnKNJRJpChPvMafiwPgGBvcN36fIoVZoprObbYWDT1DxiPwp2FBLzDCuo69BjqkAdFn2Ze1YZg5IJic0yKHtlDKR5XCiOI0RFmCaFYQpwGeindghKkvnqJTwUnfVpr9zE%2ByemwYxADVsP4JZM%2FnZRKZ4He4FDPz6YDqMH%2FBdXYK5IiquN%2FSFpR0ns5%2B8DBm8y%2BA5kmIZZ15%2F5ohdKtbZdbJ8DIy%2BNgSu8%2FdBx5Fn%2B%2Blp54tT22EupHxPvCLt8U%2Fqr6ZlP%2BZ8Z6xawtt42T%2FUiMuKdB%2F&X-Amz-Signature=2c24be08374d8e060ee54983217f04a6ca80e9e641c50101d71bc6e5e4923ceb&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTUWWDDO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDvZM2nMnBdr2b8zjgWbaLs02lE%2FVkmiIV4KUxN7ZaRuAIhAMUvrHQxOXugXtWc8jmsBmFDZcx6qhMoMLrcr%2BsFH2iDKv8DCEoQABoMNjM3NDIzMTgzODA1Igzm%2FoqZsytnej69qbAq3APmpREM%2FzO%2FUy0DGD9gZQSR8g01n9iIZSw%2F3DbrxeW1QIJi5BqgfTdcmJfEkeKxSJeSE9u1XliKdYxO7qrqYjCqlUhLvBwQjjHQa14TAliQvAn8oNE7EWucUdZFAS4mb%2FcAMtnXgqiUpltm%2Btknqah%2B1cNNf0C1GR5uDCBWR3Ir0LKYH%2Bqeo%2F8DIsVY2ytuuewAwq75VjHrty84WEHDu97GRKQeE%2Ftzg4TaLWRMl6JfcQ5uFp6YLDjG3y9Hf2Sg79gTO%2BHJDwCOM9COShVMSGcTAbNbYFifDgh3LxeKwwu%2B%2F6HE8StXu%2FcDIDCYFksoGOm69APqsF%2F%2F5drI%2BA8X7RewGGqqx06ZEHktLCer0wGxEuBjQOJv09BLZhKg%2BoIaWqefrXZRufsOdAxQD4vEaDgM2oiP3PfiA5WEkkhsXq7Ewyzk9gYV4k1fU2IX0%2Bogo6IiVg9j1XgnfLk9SWYznGnm5fry2AJyuZ0D6GNQqalvzblS6PJ4t%2FZKpwdpQK6YGOAkakS%2BNo4v2RrwKmPEpeOOo1BZ7hX%2FB1dI3Dn11yKgA1WFDU0Ma5SyMQO3c12ANI1ddaay%2BeIh9iqFxRUol842eqO%2Belw91LJHx6tIhydwTSoevuLwc1KMD%2FUgDTDQuo69BjqkAX2dl0tHsutRXGdXT33041YOBc2ydywMbUihf0oE6lNzNI54Gcqyo15ewGv%2FyIfSNtMCt%2BEfk%2FVKIG%2FlGtr1ivxV5pQuNyGvHkoHzAgciVdZ8U9aWpPjC1eVW6szQZTrhieV4LA7LmLSMdA7U4TTcK0NJN5Hyk3P44gO%2B2syqYjtCQwsSUxL0OwXztHpxeotv3VScVQTZh6lTAgCijJX%2FfaPvOrF&X-Amz-Signature=5934583e8255f8aebe37a9cd29915d7a3f6c1576218389fbd482e2347c6af71e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RQTQCCP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHX5aQy8bHqFEDq7Lj7B4Rsx9P%2FxUbUwuJ5ka%2Fyzh3upAiAjBKrVxMWpuu1KvOw1fdER4isZQgzEtVFuxRIiVC7zKyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMerDV5uJ40JN6BAVEKtwD3VTvukd8ceB3eMxpoEGRKbtgfG7ZPpQYhO0FzfYfZIG5mMih%2BbnEU7K1C6O1AZ30TZXJwqJTtI1gNxW3DUh0HjVAvgu7kXlTA9ZMDqjJ%2BLNeXm04%2B%2BcrUq%2BuPRqem8nGohMLZCIS6%2BAqsdXD1z9QzS0qiPmEdiqvOthZHZfWXg%2BdqYLhDuCycVRDXUoAFiHttQ2thGXMr9hMzPDOXZzKs1PZvDzKaH%2BaM6AEo6BWc%2Bqjh%2F4kgIbgsqmNlUqgp58fYklj55cFbnEkMYuyjebOqx09RnWBFQoTUnx3wj6Qinu9XkpCZZ%2B7Cms5gl41oOTQX%2BE1ayulfHpTdaT6wrSAjNoX8OAeWAJzBaCQu1UwQ3L26PEue6u5fJzi%2Fvm7huKAceMxLtvmLuuPuaO5wlXL9L%2BdUitvrndxfnXwHSVQWuzZW3okMXTajvg9CulKe0F2XSK9n4%2BcCrr47XOcrct1KlyOEdwJ%2FPFkLEWwtxIr%2BmxEBzVqo3V1gN6FcLBa2B1HtPEAc604wNZr89D%2Bd5JOGk8I7lsnPGhKJITluC98Gmvn5fpblewWjrzq7%2FGiDPO11X5LtDHNNz%2Be18dlt1KKJICrXVsNTynIl3K7T8mC%2FFKBezycQ%2FkyDKIefcYwrryOvQY6pgGX4hCEFk6BL%2F%2BOWFhS8AQ1Ag39JVTGOj868dC3e%2B%2FvB8XIAqFnoEhonDHtbwZbEEtzTCOhK4WfhILyEaoKgRjJ70igEmF3hkXEtQ3AWlB2y0rVhc4hJ7zn%2B8iTlbp%2BXP6Kb7KGPQoPh%2BV4qtkm13oif90bZxkGPJDnL3ML5ltFXs3TWWOFaRKYZ1n6DXeZSS3At2Jn8mhL7YQpOnQY6pcMRAzi605u&X-Amz-Signature=54c2e835f6dac09cf67a1782800c557d5c61a96f6c0a0911dceb865ad8703a30&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RQTQCCP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHX5aQy8bHqFEDq7Lj7B4Rsx9P%2FxUbUwuJ5ka%2Fyzh3upAiAjBKrVxMWpuu1KvOw1fdER4isZQgzEtVFuxRIiVC7zKyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMerDV5uJ40JN6BAVEKtwD3VTvukd8ceB3eMxpoEGRKbtgfG7ZPpQYhO0FzfYfZIG5mMih%2BbnEU7K1C6O1AZ30TZXJwqJTtI1gNxW3DUh0HjVAvgu7kXlTA9ZMDqjJ%2BLNeXm04%2B%2BcrUq%2BuPRqem8nGohMLZCIS6%2BAqsdXD1z9QzS0qiPmEdiqvOthZHZfWXg%2BdqYLhDuCycVRDXUoAFiHttQ2thGXMr9hMzPDOXZzKs1PZvDzKaH%2BaM6AEo6BWc%2Bqjh%2F4kgIbgsqmNlUqgp58fYklj55cFbnEkMYuyjebOqx09RnWBFQoTUnx3wj6Qinu9XkpCZZ%2B7Cms5gl41oOTQX%2BE1ayulfHpTdaT6wrSAjNoX8OAeWAJzBaCQu1UwQ3L26PEue6u5fJzi%2Fvm7huKAceMxLtvmLuuPuaO5wlXL9L%2BdUitvrndxfnXwHSVQWuzZW3okMXTajvg9CulKe0F2XSK9n4%2BcCrr47XOcrct1KlyOEdwJ%2FPFkLEWwtxIr%2BmxEBzVqo3V1gN6FcLBa2B1HtPEAc604wNZr89D%2Bd5JOGk8I7lsnPGhKJITluC98Gmvn5fpblewWjrzq7%2FGiDPO11X5LtDHNNz%2Be18dlt1KKJICrXVsNTynIl3K7T8mC%2FFKBezycQ%2FkyDKIefcYwrryOvQY6pgGX4hCEFk6BL%2F%2BOWFhS8AQ1Ag39JVTGOj868dC3e%2B%2FvB8XIAqFnoEhonDHtbwZbEEtzTCOhK4WfhILyEaoKgRjJ70igEmF3hkXEtQ3AWlB2y0rVhc4hJ7zn%2B8iTlbp%2BXP6Kb7KGPQoPh%2BV4qtkm13oif90bZxkGPJDnL3ML5ltFXs3TWWOFaRKYZ1n6DXeZSS3At2Jn8mhL7YQpOnQY6pcMRAzi605u&X-Amz-Signature=cd0f9d6286b5bd7d97312f9bc6df49f8b0e213e4a53bb65e1c2ef45d6a1604f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RQTQCCP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHX5aQy8bHqFEDq7Lj7B4Rsx9P%2FxUbUwuJ5ka%2Fyzh3upAiAjBKrVxMWpuu1KvOw1fdER4isZQgzEtVFuxRIiVC7zKyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMerDV5uJ40JN6BAVEKtwD3VTvukd8ceB3eMxpoEGRKbtgfG7ZPpQYhO0FzfYfZIG5mMih%2BbnEU7K1C6O1AZ30TZXJwqJTtI1gNxW3DUh0HjVAvgu7kXlTA9ZMDqjJ%2BLNeXm04%2B%2BcrUq%2BuPRqem8nGohMLZCIS6%2BAqsdXD1z9QzS0qiPmEdiqvOthZHZfWXg%2BdqYLhDuCycVRDXUoAFiHttQ2thGXMr9hMzPDOXZzKs1PZvDzKaH%2BaM6AEo6BWc%2Bqjh%2F4kgIbgsqmNlUqgp58fYklj55cFbnEkMYuyjebOqx09RnWBFQoTUnx3wj6Qinu9XkpCZZ%2B7Cms5gl41oOTQX%2BE1ayulfHpTdaT6wrSAjNoX8OAeWAJzBaCQu1UwQ3L26PEue6u5fJzi%2Fvm7huKAceMxLtvmLuuPuaO5wlXL9L%2BdUitvrndxfnXwHSVQWuzZW3okMXTajvg9CulKe0F2XSK9n4%2BcCrr47XOcrct1KlyOEdwJ%2FPFkLEWwtxIr%2BmxEBzVqo3V1gN6FcLBa2B1HtPEAc604wNZr89D%2Bd5JOGk8I7lsnPGhKJITluC98Gmvn5fpblewWjrzq7%2FGiDPO11X5LtDHNNz%2Be18dlt1KKJICrXVsNTynIl3K7T8mC%2FFKBezycQ%2FkyDKIefcYwrryOvQY6pgGX4hCEFk6BL%2F%2BOWFhS8AQ1Ag39JVTGOj868dC3e%2B%2FvB8XIAqFnoEhonDHtbwZbEEtzTCOhK4WfhILyEaoKgRjJ70igEmF3hkXEtQ3AWlB2y0rVhc4hJ7zn%2B8iTlbp%2BXP6Kb7KGPQoPh%2BV4qtkm13oif90bZxkGPJDnL3ML5ltFXs3TWWOFaRKYZ1n6DXeZSS3At2Jn8mhL7YQpOnQY6pcMRAzi605u&X-Amz-Signature=d66a81c8a074d87383a5d402ad5bfb47024fe84478d1a62551f053029c28f54d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OV3IA7R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCApSjkLdtbKLmmoKuj3%2F1TPkOQ%2BvwqEuBax7EQfMkh4AIhAK5WtJQdpmdkZZ8PBI58yAatMMdC4fbmedPspBdF3O2AKv8DCEoQABoMNjM3NDIzMTgzODA1IgwdYK9KhzYKEc0K9ecq3APlkLewMgNcZ24g2RBnDgkx6Ks1qvzVt1j6hR%2B8f1Q2SHf2pxlS3iTKXCsp%2B%2Bv85MBLD0iLOiJo6V57Kr0h65Jp7poNC%2BF%2Bz6BWjatczHXe6QyVhNX6du6ze0IzddfDADpzAcQVNRR9u0DuZkLwKcG2UMRv7rloUuHvFfTObXCNDvQnbhw6XJQCRUxQFIadeGdfW%2F70lJA0wtW%2BlgL2J6bZ%2BC8GyhG098KduXM0UEgrSX%2BM81mimyHP4fImpn%2FE4GGZnz0UmmJRO99Rzb65vYOEgjRdDPot1XYHwoy2HieisZV%2BtkQF5NQmTOPY7LSZxs%2FEcqgfneQjSRECxmdL1%2FAkmW1emB7tkxzAC6rRp87s5I9ds2CTlK5MPcUVfDU5dNcqpZ9gs6VhzsCyy7S0z9%2F3TMG%2BTh1wuthxXk0bcHKdg2aVoo27QGpPXUA5YblezDgQDCbClE7uxIsTHsNf5GHgGZatG2s67UFT%2F0aTuDJHRfyJzrQgzwZiDpIzwYoln2ICp8vZU5lthdeJhH5qBy4uKVCdN7AuSs1qT78ExraPxCvJxt2Cs0z5q41iBi9rmu45ErWnNpf4Dpzsi2pGJIDz32w4bxJNeRsRt%2BOqcXwP4PUeLsXpwZA4ov6IQzDGuo69BjqkAWOwbyM7zU2JCrrBh34dYj8Y1c9Vwos%2BYnEl%2FpfcS%2F4lTxTusa4Omn2cp%2B8Wgh5S6CJASh7nOBKC7btnOdH33AdjMB2%2BPcvxomfAXEB8lSmG8TnlFSikKTYI4ti5GaQlmZIaMow4lTqeI57ZI7qcNTV9PvlQK5qRzgbek%2B0s5xvlltUKURc7e4t%2BjdHVWp%2F2ypFCfmKaXhlbeSSoZNcZqiv0fDVI&X-Amz-Signature=a2a48707b098eb4274de69bccee05c8ddffb314f2b7d6f37b99dc8b267ba93d4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP4F5TSC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIAurj12KvFQY2exsL%2Bv9Cbwk4rqGlmESPoynJK%2FPNF4RAiAcLWNxg6SW6wc8wIaeM3V4skJU34csRNsCpKS97bVXzSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMnj4EUcV34p8eJn7gKtwD3yEOiiIVzfyrsJbZPRpW7zysmOK1%2BI5teQL3%2BkW7%2FlWlqRKbD%2B084pEGxpHXLtXwUMm0n0Ew5txCIS%2Fko8JUKQX7mF%2B11IwAzs25Yi4%2BQhr1MStZHBULAG7TRazktOfyT%2F6fEKae0PaCuaQww4xtRe3S1GkBShQ7lgRnFDiZiaT07etMhUvbIDN8DxFqeL9yxtLz2Twxkw0FCR8RsQZflb8%2BAEsNYtobeEzEM11zgsMtMmlFecZTKKlNWK6Fm4gDn0%2BZ2bti%2FQeIZ%2BDgLzpCysKSHBbbxsT6m7MjvRdWY8zQzIXeKFG4N04JM8Mfwge16sA8AZub0IIU8gtBmL5rFb0jYkbG30vW7BC9mHR0cw2P8BdExJVvMqMOhUxSfIVCFDpT17S8vaQWJieO4pQitkg%2B%2FbOdFRBx8f7K7herrDesO2m6Q45YDPsdSybnel0x6cofKCCAVfsRvo98150BvukNY%2BSC0DK3QgeZI14gPhtxfN62P69of%2Bwxh08gbm5k8MtLWexlHtNT9wa5ejmcnJ9FjNd7z4dEuB2ZhBnHWgWbYq9in59B1KTg9P8tU15uFROvUeone65wsbanGEeFKHiiiENgpSPcrxvTKo0SOanUhA3F9x4YPv5%2Bi1owjbyOvQY6pgGC4zss4L5%2FpUqs92%2F3khMrVFVxotRCRYdRWHAtWpqapOVPhzydbz5jOuq4wQVzQ9hIxIzTDfGY5G488n6dwugQ2pFX9PlApGPFefRpBq4uF1%2B%2BK%2BbECSWHcwZCqk6dYHEUBtks6ORw2AKN6H0nmnkp%2FgJt8LE02jHV%2BWqIvcSaEcS5yOqECxKNhn6P02D2GybmDGO8ATEXCSJbfVu7PDa8zRYd0UXS&X-Amz-Signature=647491d8db1229e319408b36c8229360a5d43ca2bb51f93de46e6c538b6bba10&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7MLMQQH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDMFjltFm4ZJeK6l7L8vClQn5d6wuEQF7mpymzgfTVaNQIgb5Waofn9wGBDzhGWsLbvJrDS0p3RQ4ZS0jfpOVKcRm8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDEfsQQrcd%2FL4oBZfgircAzyateWX6QIOauVgx9DFbsh%2B4BaB%2F715uGLTpTQro%2BJI5G5nPfOPAvbg2lTkJdNWAgWYGuFTSzTN0rrlaHyZiIYiewDsWg68KIYrd%2F8A32gV2hbX0rj2gBfFRAI51G46jf3eso0kT9EEl46rFV%2BHmr5Ece5uz85tB1t%2FLRh69VmjEuvSecfbdrF8quKkIx5JcBmbujCF%2FeihIG18O7UmxRQdTX9c3yZ6Y2GSnR4VKGHikdO%2FWrxNz6fnL19aOheIIAFVV%2B5OPFyvDlvR6wTW6I7e8POWkL0sRO4oU5CFF4v2e5L%2BzkJ8iznDSWXSRFDBMYNBbi4kPC6zuR9qJHGkXPpPGVBpj7Lsx3rRRYYAs8Ib81oDbWabIYeg%2FnwGM8HtYrCfjfSXhGVrnE%2FKYnJb3%2Ftgqw%2BgHiROnyobpZtYpM0I9soBcZCyMU9y7Bba8NBETovddUVj2UfFU92eCDfIPA5wNBuW2GYY6v2TRxWJVU81sfiLyIfoXn7X%2BBwwUJ%2BRtZlBRWCVQNczXPhhjVwpMyb%2FoYvmMHlcsikNQul2clQAesO1SKIY%2FAZf6izkoA9hudB%2FbIBC7oOz86VTsWqabE4wl4bMGJlOlfyKvJlkxMe%2BfFBAczT2aINFLukxMOe6jr0GOqUBdm3NKw4EILlrtFonNLqIwxqYZnbO2Buk04ObSiZRkqPEGjOvvSPsF8YuYwZyJxZ4nwJsMuQRlH2nmryMTt5Pdgo%2BiSgHWZ32AOl14gOQJk31UpTAH4eT4oyPlD0ILTO5T9cUafCtCAkHiAwXHzfk4zjXbmcGZsfhwyqnIEr0libV9oip2TwolkJK2XphTpn08tFMicHnJ8lbRv64Qi0fROixl9fk&X-Amz-Signature=96af7fb8ac5fbfd7a677176c0223d10cd7a9b5fe67a9a12c9db223a859c5de03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YLX6KJT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDNZcrIQDMKJnt%2B6L5Kfca4SKZtWFR5NR%2BSVTvIREBTBwIhAKN%2BXKVC%2FxT5c%2FWN3aHgwG2PgPiNvgRm69pcKNj0iGo7Kv8DCEoQABoMNjM3NDIzMTgzODA1IgyCu%2BY%2FWv4W9rmrIWEq3AOPIXXlHhTcOj1Am8od%2FrstOJLrQi6gfEx%2BpOKyJulxwA0wfMqsDYJSdniUDLnrnfyVh9EHSQRAxMZN0HBdm5eUDi8eB7bS%2F9SOjmcfouf7jJ3tqw4n1TZ88D3F%2FMw7AUV%2FW7kEBuRPZfwY7r3tPBe5Z5FwCBbzfOzhdE0J3y%2BcxyWIbuLkmqN2uZCFbS9CUeuwadB%2BF7l9IecpQBTRv15uCqeGz72LBYoXNY3jPeFzRIqp0TErdIX7ywLBLajl6C2JFKmZ%2BopYr%2BAZa09a2SGpeW4qAYSvH1D7%2BCH3dd1nv3caNnqBIdk3slEa9CeS6%2BwI9Nkiyt7%2FNwyQzOJ52SMXKfik8cNuKmGsof9ZtJguwIJxjrkVm5yLgiwimGdNUvAagLbciURtaIETLk9VpKa9yQg1AFwIp%2BSEwZ6%2FEAfIZc9D%2BdG53NqPLNp2wCnLhOvSTBXkXdw1PDURHjHefq6ZlxtKOcWKQqNVwQE3O8JM%2BcnzjnJNh2%2B31j64RhvNP%2Bh%2FFb3N483LcN8DiU0MNF0aFfeVnmPYTzOSpIFcCN7erzHBLQ0Y7gBaFFjSx8tQ41h91Q6%2BEwWN%2F20c7rSzEkArDKv%2BoW7nj2z3W35Dzp35DMe40n5%2FCw8P9ya%2FHDCMvI69BjqkAZ4gtyOT7M18jYCVGZj%2Ft8ipGpmcYfuhbcq33EMLZ%2BIVTL1I2nzdHNZfdez0FeGpgBAeHm36MR9iVv2si3yl65e1aVeq8OGLOK5WV3UYqOrfKb%2FMfwc5pMRBeKTraA2u7pAdq5VdsmwTytzwV9apS%2B75GvW%2BfNa77qvTj%2FMe1Iz%2BTLkmO9bZStG8QYVBOQCoGHJax7LN2BNLZDlxAqMjOhcp%2BceL&X-Amz-Signature=e81b2d3b042ae34c00930f1a02b13d8700e3b17cfc095056590e630088e55401&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YLX6KJT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDNZcrIQDMKJnt%2B6L5Kfca4SKZtWFR5NR%2BSVTvIREBTBwIhAKN%2BXKVC%2FxT5c%2FWN3aHgwG2PgPiNvgRm69pcKNj0iGo7Kv8DCEoQABoMNjM3NDIzMTgzODA1IgyCu%2BY%2FWv4W9rmrIWEq3AOPIXXlHhTcOj1Am8od%2FrstOJLrQi6gfEx%2BpOKyJulxwA0wfMqsDYJSdniUDLnrnfyVh9EHSQRAxMZN0HBdm5eUDi8eB7bS%2F9SOjmcfouf7jJ3tqw4n1TZ88D3F%2FMw7AUV%2FW7kEBuRPZfwY7r3tPBe5Z5FwCBbzfOzhdE0J3y%2BcxyWIbuLkmqN2uZCFbS9CUeuwadB%2BF7l9IecpQBTRv15uCqeGz72LBYoXNY3jPeFzRIqp0TErdIX7ywLBLajl6C2JFKmZ%2BopYr%2BAZa09a2SGpeW4qAYSvH1D7%2BCH3dd1nv3caNnqBIdk3slEa9CeS6%2BwI9Nkiyt7%2FNwyQzOJ52SMXKfik8cNuKmGsof9ZtJguwIJxjrkVm5yLgiwimGdNUvAagLbciURtaIETLk9VpKa9yQg1AFwIp%2BSEwZ6%2FEAfIZc9D%2BdG53NqPLNp2wCnLhOvSTBXkXdw1PDURHjHefq6ZlxtKOcWKQqNVwQE3O8JM%2BcnzjnJNh2%2B31j64RhvNP%2Bh%2FFb3N483LcN8DiU0MNF0aFfeVnmPYTzOSpIFcCN7erzHBLQ0Y7gBaFFjSx8tQ41h91Q6%2BEwWN%2F20c7rSzEkArDKv%2BoW7nj2z3W35Dzp35DMe40n5%2FCw8P9ya%2FHDCMvI69BjqkAZ4gtyOT7M18jYCVGZj%2Ft8ipGpmcYfuhbcq33EMLZ%2BIVTL1I2nzdHNZfdez0FeGpgBAeHm36MR9iVv2si3yl65e1aVeq8OGLOK5WV3UYqOrfKb%2FMfwc5pMRBeKTraA2u7pAdq5VdsmwTytzwV9apS%2B75GvW%2BfNa77qvTj%2FMe1Iz%2BTLkmO9bZStG8QYVBOQCoGHJax7LN2BNLZDlxAqMjOhcp%2BceL&X-Amz-Signature=dd22dceb6cfe8e13de884f5ce176c4028bd04780a2a65868f0feb9762d68914d&X-Amz-SignedHeaders=host&x-id=GetObject)

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
