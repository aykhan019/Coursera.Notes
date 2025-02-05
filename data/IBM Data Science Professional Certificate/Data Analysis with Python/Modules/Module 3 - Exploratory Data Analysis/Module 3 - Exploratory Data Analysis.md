

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3UD72NR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDuiNWJB3k4VKeNvpaOqRgrlGssezOUwUaL7u0LPT1afQIhAOMcJIATYgM5O0erchxzfUQhaCL16FbC6nmYTkzP62FaKv8DCEoQABoMNjM3NDIzMTgzODA1IgzcmGA49Z3mviicWiUq3APscsyAzthSHSEXdsxx5w4QfcnxssS%2FW8aiSyiDH0rdHYQbxQ5Q4PmCxU1j1O6Ybf8ilsAuel310JwIZ5jyuLKmPSsYo7dtV5Yj0tL6AbWuLjzU%2BzZUFOGfRRC4V9TfFQMu2lu1%2B6e0qGkySYxWCcQw5JJuGvvUsztdlAITQ%2Bn6ullExbn%2BBPJ384q4dAM9Lb74T7JOf9zczh9od4tTCnrSZcyFY6G7aZTfPII17NTynubAKboiB4gAIQlnQm9GIs6u3uGQZAv9KJE9xht2qBlQuhG4x%2BDs00eB9MMW%2B9KsfVYsLYjirgeGE6sfJrcotw4atlg9%2FYT4bdTaboi9qomRsSPJkte6zLb5MwL6Au1cVyqepOeSKEMgg%2FKKFfkVfGonFRCLZgvkY5MPWZ5hE7x5e1YQVMkoou5dL23XOtyPP7e8ZTHxk6CjOAz9LMTj4UQGD%2FJjPxJenNnjOrIp3HaT7I1Prmb6GJBlF5j9RHuy8qcfRNtBZqB5U%2Ff2e5coMHOynaVbYqWSKATQnSu%2BtPw%2F%2B%2FHcJ13z4peShr3XpfOsQIRKwf%2FqkySuCYXHZEWi5D5vx38XYrnc9s7IBcocpXQ4gmM6biIsykxngJ2vUfG40tK49rgrQPYMSmg7gjCLvI69BjqkAQa3xNu8F1pBOjK7ENCSwG%2FqirhCJicpZ5hrBravnGVx7H4GPZSSaYzMXM7Fj%2FMfnqIXHj5%2Bzgr8Y%2Bwa9MCQAeFKjoCT0BmZTpaXWaMsGz3U4MsCwigSsB8i77zpcNFQheYPIuHE%2FxjrLtTSl0xCwLY%2FnH7jl1LvILBuYSX3quUoV07DdGS%2BSPhYk6mZoKZOTLj%2BjPyD7lvOnITHmyGiud4W3Jt8&X-Amz-Signature=8f9fba0fc33e7136c28f8ec7795d82e5a07a66e8e681c64ec244dfe26f276d51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3UD72NR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDuiNWJB3k4VKeNvpaOqRgrlGssezOUwUaL7u0LPT1afQIhAOMcJIATYgM5O0erchxzfUQhaCL16FbC6nmYTkzP62FaKv8DCEoQABoMNjM3NDIzMTgzODA1IgzcmGA49Z3mviicWiUq3APscsyAzthSHSEXdsxx5w4QfcnxssS%2FW8aiSyiDH0rdHYQbxQ5Q4PmCxU1j1O6Ybf8ilsAuel310JwIZ5jyuLKmPSsYo7dtV5Yj0tL6AbWuLjzU%2BzZUFOGfRRC4V9TfFQMu2lu1%2B6e0qGkySYxWCcQw5JJuGvvUsztdlAITQ%2Bn6ullExbn%2BBPJ384q4dAM9Lb74T7JOf9zczh9od4tTCnrSZcyFY6G7aZTfPII17NTynubAKboiB4gAIQlnQm9GIs6u3uGQZAv9KJE9xht2qBlQuhG4x%2BDs00eB9MMW%2B9KsfVYsLYjirgeGE6sfJrcotw4atlg9%2FYT4bdTaboi9qomRsSPJkte6zLb5MwL6Au1cVyqepOeSKEMgg%2FKKFfkVfGonFRCLZgvkY5MPWZ5hE7x5e1YQVMkoou5dL23XOtyPP7e8ZTHxk6CjOAz9LMTj4UQGD%2FJjPxJenNnjOrIp3HaT7I1Prmb6GJBlF5j9RHuy8qcfRNtBZqB5U%2Ff2e5coMHOynaVbYqWSKATQnSu%2BtPw%2F%2B%2FHcJ13z4peShr3XpfOsQIRKwf%2FqkySuCYXHZEWi5D5vx38XYrnc9s7IBcocpXQ4gmM6biIsykxngJ2vUfG40tK49rgrQPYMSmg7gjCLvI69BjqkAQa3xNu8F1pBOjK7ENCSwG%2FqirhCJicpZ5hrBravnGVx7H4GPZSSaYzMXM7Fj%2FMfnqIXHj5%2Bzgr8Y%2Bwa9MCQAeFKjoCT0BmZTpaXWaMsGz3U4MsCwigSsB8i77zpcNFQheYPIuHE%2FxjrLtTSl0xCwLY%2FnH7jl1LvILBuYSX3quUoV07DdGS%2BSPhYk6mZoKZOTLj%2BjPyD7lvOnITHmyGiud4W3Jt8&X-Amz-Signature=efca22480b8e78be525e5b317d90cd7658e975698a6b89107acb4d06a0726d7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3UD72NR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDuiNWJB3k4VKeNvpaOqRgrlGssezOUwUaL7u0LPT1afQIhAOMcJIATYgM5O0erchxzfUQhaCL16FbC6nmYTkzP62FaKv8DCEoQABoMNjM3NDIzMTgzODA1IgzcmGA49Z3mviicWiUq3APscsyAzthSHSEXdsxx5w4QfcnxssS%2FW8aiSyiDH0rdHYQbxQ5Q4PmCxU1j1O6Ybf8ilsAuel310JwIZ5jyuLKmPSsYo7dtV5Yj0tL6AbWuLjzU%2BzZUFOGfRRC4V9TfFQMu2lu1%2B6e0qGkySYxWCcQw5JJuGvvUsztdlAITQ%2Bn6ullExbn%2BBPJ384q4dAM9Lb74T7JOf9zczh9od4tTCnrSZcyFY6G7aZTfPII17NTynubAKboiB4gAIQlnQm9GIs6u3uGQZAv9KJE9xht2qBlQuhG4x%2BDs00eB9MMW%2B9KsfVYsLYjirgeGE6sfJrcotw4atlg9%2FYT4bdTaboi9qomRsSPJkte6zLb5MwL6Au1cVyqepOeSKEMgg%2FKKFfkVfGonFRCLZgvkY5MPWZ5hE7x5e1YQVMkoou5dL23XOtyPP7e8ZTHxk6CjOAz9LMTj4UQGD%2FJjPxJenNnjOrIp3HaT7I1Prmb6GJBlF5j9RHuy8qcfRNtBZqB5U%2Ff2e5coMHOynaVbYqWSKATQnSu%2BtPw%2F%2B%2FHcJ13z4peShr3XpfOsQIRKwf%2FqkySuCYXHZEWi5D5vx38XYrnc9s7IBcocpXQ4gmM6biIsykxngJ2vUfG40tK49rgrQPYMSmg7gjCLvI69BjqkAQa3xNu8F1pBOjK7ENCSwG%2FqirhCJicpZ5hrBravnGVx7H4GPZSSaYzMXM7Fj%2FMfnqIXHj5%2Bzgr8Y%2Bwa9MCQAeFKjoCT0BmZTpaXWaMsGz3U4MsCwigSsB8i77zpcNFQheYPIuHE%2FxjrLtTSl0xCwLY%2FnH7jl1LvILBuYSX3quUoV07DdGS%2BSPhYk6mZoKZOTLj%2BjPyD7lvOnITHmyGiud4W3Jt8&X-Amz-Signature=8d549abd53f65154a98ad7d6f857c08490718915f8f98a4cea40f77574d53d38&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF2JYKLS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIArr1K6BPdND%2BxlSGCP8WbMPi3uitLdS1IJJ1ZFpXLiyAiEAnA9el6hanCgs%2FR3IWIuAD7fK6HtK6debX%2BjI4gJrGTIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHOYHcr%2B5nIZo6kKjircAxSGZ9BFCzJtY6RDMtG1YN2yYe0YuCqwKOI8KTX1wQULW1ozQCL583yzQFCu6B51uIXow%2FLUKj%2FxVplp84Zh5CbVYnCmCMsZA8azyoabn%2B%2BcoCRWb1MtDfyUqZrbZiADxaK0OTHSbbJ%2F72BOAdNyZlGjMKHQcHnHcQbYcoVg3bdpRFjddtmjZJvDDOCcNvLyJtMQoUdRXS4RX6D0zd6gq%2Fsdc63WUcpQaf8GLhreY%2FLXwgrpWbRgXdRifJJHnYLRHi8omSQFapa60OW9f2m3dDWsd2WZaoJAMwWdY0THCbkhwsOPEQFDfeww0bh8zI2w0CGBOXPeMUoLcf5GuTdpeGfzJEwC47i8PuUPM%2FijAICE%2B6l9RBkVvun8ZZ5uAyuClg2b3oOua5vYjWgbqsSe%2Bw9V5948Jl8Owkhg10ESuQHAXx9yPQBxHqDszPOPAOSlhw4%2F7g5OFi1%2Fe4EdkdKPzDw%2F7VJT1bT%2BKb9HRTCdCQeawjG31NGfKY9YI%2BW%2F1Q0In5iwquV1hgAmKySwhP55kqOF8g8eX6%2B9QkQsolCqjcrwLaQfsr98KsJaJgKqbbGCrY8o%2FQmXSdByaXQjJXmvaGlq1TclSZUVy682RGxhfHWi6stVFaLnqc8jV4PqMLa6jr0GOqUB%2BNBvPanv4lyzZPb1WzKTxEr4MRs76BMmWiXMpP6J1UTDpDY6POG498loSPqGdDh9Bv4REeMPrQzIJAsAtWvXUmpDrkS6fR8d1L9s%2F4xIIcyQ5RTAcgLqMU68LbHMQky1qye%2FE6F46QWJhHcLC6uznDsrUoSUM0tt5ibTg4Nbt19zTO7FlUshptiaOoBmHF%2B0ie4BgPVfOWM2RIArjYipHwrZpSrW&X-Amz-Signature=6d9801934869454cfe3dcb4798836eb906646a9fc4b5b9211c26aff19be38db0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF2JYKLS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIArr1K6BPdND%2BxlSGCP8WbMPi3uitLdS1IJJ1ZFpXLiyAiEAnA9el6hanCgs%2FR3IWIuAD7fK6HtK6debX%2BjI4gJrGTIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHOYHcr%2B5nIZo6kKjircAxSGZ9BFCzJtY6RDMtG1YN2yYe0YuCqwKOI8KTX1wQULW1ozQCL583yzQFCu6B51uIXow%2FLUKj%2FxVplp84Zh5CbVYnCmCMsZA8azyoabn%2B%2BcoCRWb1MtDfyUqZrbZiADxaK0OTHSbbJ%2F72BOAdNyZlGjMKHQcHnHcQbYcoVg3bdpRFjddtmjZJvDDOCcNvLyJtMQoUdRXS4RX6D0zd6gq%2Fsdc63WUcpQaf8GLhreY%2FLXwgrpWbRgXdRifJJHnYLRHi8omSQFapa60OW9f2m3dDWsd2WZaoJAMwWdY0THCbkhwsOPEQFDfeww0bh8zI2w0CGBOXPeMUoLcf5GuTdpeGfzJEwC47i8PuUPM%2FijAICE%2B6l9RBkVvun8ZZ5uAyuClg2b3oOua5vYjWgbqsSe%2Bw9V5948Jl8Owkhg10ESuQHAXx9yPQBxHqDszPOPAOSlhw4%2F7g5OFi1%2Fe4EdkdKPzDw%2F7VJT1bT%2BKb9HRTCdCQeawjG31NGfKY9YI%2BW%2F1Q0In5iwquV1hgAmKySwhP55kqOF8g8eX6%2B9QkQsolCqjcrwLaQfsr98KsJaJgKqbbGCrY8o%2FQmXSdByaXQjJXmvaGlq1TclSZUVy682RGxhfHWi6stVFaLnqc8jV4PqMLa6jr0GOqUB%2BNBvPanv4lyzZPb1WzKTxEr4MRs76BMmWiXMpP6J1UTDpDY6POG498loSPqGdDh9Bv4REeMPrQzIJAsAtWvXUmpDrkS6fR8d1L9s%2F4xIIcyQ5RTAcgLqMU68LbHMQky1qye%2FE6F46QWJhHcLC6uznDsrUoSUM0tt5ibTg4Nbt19zTO7FlUshptiaOoBmHF%2B0ie4BgPVfOWM2RIArjYipHwrZpSrW&X-Amz-Signature=9b1348c3dbedaec8b595da26ffd8edd4783f7855b8b7e1a8e419eb4a5d080089&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF2JYKLS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIArr1K6BPdND%2BxlSGCP8WbMPi3uitLdS1IJJ1ZFpXLiyAiEAnA9el6hanCgs%2FR3IWIuAD7fK6HtK6debX%2BjI4gJrGTIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHOYHcr%2B5nIZo6kKjircAxSGZ9BFCzJtY6RDMtG1YN2yYe0YuCqwKOI8KTX1wQULW1ozQCL583yzQFCu6B51uIXow%2FLUKj%2FxVplp84Zh5CbVYnCmCMsZA8azyoabn%2B%2BcoCRWb1MtDfyUqZrbZiADxaK0OTHSbbJ%2F72BOAdNyZlGjMKHQcHnHcQbYcoVg3bdpRFjddtmjZJvDDOCcNvLyJtMQoUdRXS4RX6D0zd6gq%2Fsdc63WUcpQaf8GLhreY%2FLXwgrpWbRgXdRifJJHnYLRHi8omSQFapa60OW9f2m3dDWsd2WZaoJAMwWdY0THCbkhwsOPEQFDfeww0bh8zI2w0CGBOXPeMUoLcf5GuTdpeGfzJEwC47i8PuUPM%2FijAICE%2B6l9RBkVvun8ZZ5uAyuClg2b3oOua5vYjWgbqsSe%2Bw9V5948Jl8Owkhg10ESuQHAXx9yPQBxHqDszPOPAOSlhw4%2F7g5OFi1%2Fe4EdkdKPzDw%2F7VJT1bT%2BKb9HRTCdCQeawjG31NGfKY9YI%2BW%2F1Q0In5iwquV1hgAmKySwhP55kqOF8g8eX6%2B9QkQsolCqjcrwLaQfsr98KsJaJgKqbbGCrY8o%2FQmXSdByaXQjJXmvaGlq1TclSZUVy682RGxhfHWi6stVFaLnqc8jV4PqMLa6jr0GOqUB%2BNBvPanv4lyzZPb1WzKTxEr4MRs76BMmWiXMpP6J1UTDpDY6POG498loSPqGdDh9Bv4REeMPrQzIJAsAtWvXUmpDrkS6fR8d1L9s%2F4xIIcyQ5RTAcgLqMU68LbHMQky1qye%2FE6F46QWJhHcLC6uznDsrUoSUM0tt5ibTg4Nbt19zTO7FlUshptiaOoBmHF%2B0ie4BgPVfOWM2RIArjYipHwrZpSrW&X-Amz-Signature=f019ae0b6abdede8a9b282b67538333ea7374ba5bb0e2d8ee74ff5699b8faf65&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF2JYKLS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIArr1K6BPdND%2BxlSGCP8WbMPi3uitLdS1IJJ1ZFpXLiyAiEAnA9el6hanCgs%2FR3IWIuAD7fK6HtK6debX%2BjI4gJrGTIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHOYHcr%2B5nIZo6kKjircAxSGZ9BFCzJtY6RDMtG1YN2yYe0YuCqwKOI8KTX1wQULW1ozQCL583yzQFCu6B51uIXow%2FLUKj%2FxVplp84Zh5CbVYnCmCMsZA8azyoabn%2B%2BcoCRWb1MtDfyUqZrbZiADxaK0OTHSbbJ%2F72BOAdNyZlGjMKHQcHnHcQbYcoVg3bdpRFjddtmjZJvDDOCcNvLyJtMQoUdRXS4RX6D0zd6gq%2Fsdc63WUcpQaf8GLhreY%2FLXwgrpWbRgXdRifJJHnYLRHi8omSQFapa60OW9f2m3dDWsd2WZaoJAMwWdY0THCbkhwsOPEQFDfeww0bh8zI2w0CGBOXPeMUoLcf5GuTdpeGfzJEwC47i8PuUPM%2FijAICE%2B6l9RBkVvun8ZZ5uAyuClg2b3oOua5vYjWgbqsSe%2Bw9V5948Jl8Owkhg10ESuQHAXx9yPQBxHqDszPOPAOSlhw4%2F7g5OFi1%2Fe4EdkdKPzDw%2F7VJT1bT%2BKb9HRTCdCQeawjG31NGfKY9YI%2BW%2F1Q0In5iwquV1hgAmKySwhP55kqOF8g8eX6%2B9QkQsolCqjcrwLaQfsr98KsJaJgKqbbGCrY8o%2FQmXSdByaXQjJXmvaGlq1TclSZUVy682RGxhfHWi6stVFaLnqc8jV4PqMLa6jr0GOqUB%2BNBvPanv4lyzZPb1WzKTxEr4MRs76BMmWiXMpP6J1UTDpDY6POG498loSPqGdDh9Bv4REeMPrQzIJAsAtWvXUmpDrkS6fR8d1L9s%2F4xIIcyQ5RTAcgLqMU68LbHMQky1qye%2FE6F46QWJhHcLC6uznDsrUoSUM0tt5ibTg4Nbt19zTO7FlUshptiaOoBmHF%2B0ie4BgPVfOWM2RIArjYipHwrZpSrW&X-Amz-Signature=e487b2cbcd77f27ee875c56af46f8d7e8caeeafea53fea255b9025f869318cdd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF2JYKLS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIArr1K6BPdND%2BxlSGCP8WbMPi3uitLdS1IJJ1ZFpXLiyAiEAnA9el6hanCgs%2FR3IWIuAD7fK6HtK6debX%2BjI4gJrGTIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHOYHcr%2B5nIZo6kKjircAxSGZ9BFCzJtY6RDMtG1YN2yYe0YuCqwKOI8KTX1wQULW1ozQCL583yzQFCu6B51uIXow%2FLUKj%2FxVplp84Zh5CbVYnCmCMsZA8azyoabn%2B%2BcoCRWb1MtDfyUqZrbZiADxaK0OTHSbbJ%2F72BOAdNyZlGjMKHQcHnHcQbYcoVg3bdpRFjddtmjZJvDDOCcNvLyJtMQoUdRXS4RX6D0zd6gq%2Fsdc63WUcpQaf8GLhreY%2FLXwgrpWbRgXdRifJJHnYLRHi8omSQFapa60OW9f2m3dDWsd2WZaoJAMwWdY0THCbkhwsOPEQFDfeww0bh8zI2w0CGBOXPeMUoLcf5GuTdpeGfzJEwC47i8PuUPM%2FijAICE%2B6l9RBkVvun8ZZ5uAyuClg2b3oOua5vYjWgbqsSe%2Bw9V5948Jl8Owkhg10ESuQHAXx9yPQBxHqDszPOPAOSlhw4%2F7g5OFi1%2Fe4EdkdKPzDw%2F7VJT1bT%2BKb9HRTCdCQeawjG31NGfKY9YI%2BW%2F1Q0In5iwquV1hgAmKySwhP55kqOF8g8eX6%2B9QkQsolCqjcrwLaQfsr98KsJaJgKqbbGCrY8o%2FQmXSdByaXQjJXmvaGlq1TclSZUVy682RGxhfHWi6stVFaLnqc8jV4PqMLa6jr0GOqUB%2BNBvPanv4lyzZPb1WzKTxEr4MRs76BMmWiXMpP6J1UTDpDY6POG498loSPqGdDh9Bv4REeMPrQzIJAsAtWvXUmpDrkS6fR8d1L9s%2F4xIIcyQ5RTAcgLqMU68LbHMQky1qye%2FE6F46QWJhHcLC6uznDsrUoSUM0tt5ibTg4Nbt19zTO7FlUshptiaOoBmHF%2B0ie4BgPVfOWM2RIArjYipHwrZpSrW&X-Amz-Signature=39b92d25e554988f50bb17a877c2bd8b3f40084e8b5399ad28d10f603b5938f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF2JYKLS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIArr1K6BPdND%2BxlSGCP8WbMPi3uitLdS1IJJ1ZFpXLiyAiEAnA9el6hanCgs%2FR3IWIuAD7fK6HtK6debX%2BjI4gJrGTIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHOYHcr%2B5nIZo6kKjircAxSGZ9BFCzJtY6RDMtG1YN2yYe0YuCqwKOI8KTX1wQULW1ozQCL583yzQFCu6B51uIXow%2FLUKj%2FxVplp84Zh5CbVYnCmCMsZA8azyoabn%2B%2BcoCRWb1MtDfyUqZrbZiADxaK0OTHSbbJ%2F72BOAdNyZlGjMKHQcHnHcQbYcoVg3bdpRFjddtmjZJvDDOCcNvLyJtMQoUdRXS4RX6D0zd6gq%2Fsdc63WUcpQaf8GLhreY%2FLXwgrpWbRgXdRifJJHnYLRHi8omSQFapa60OW9f2m3dDWsd2WZaoJAMwWdY0THCbkhwsOPEQFDfeww0bh8zI2w0CGBOXPeMUoLcf5GuTdpeGfzJEwC47i8PuUPM%2FijAICE%2B6l9RBkVvun8ZZ5uAyuClg2b3oOua5vYjWgbqsSe%2Bw9V5948Jl8Owkhg10ESuQHAXx9yPQBxHqDszPOPAOSlhw4%2F7g5OFi1%2Fe4EdkdKPzDw%2F7VJT1bT%2BKb9HRTCdCQeawjG31NGfKY9YI%2BW%2F1Q0In5iwquV1hgAmKySwhP55kqOF8g8eX6%2B9QkQsolCqjcrwLaQfsr98KsJaJgKqbbGCrY8o%2FQmXSdByaXQjJXmvaGlq1TclSZUVy682RGxhfHWi6stVFaLnqc8jV4PqMLa6jr0GOqUB%2BNBvPanv4lyzZPb1WzKTxEr4MRs76BMmWiXMpP6J1UTDpDY6POG498loSPqGdDh9Bv4REeMPrQzIJAsAtWvXUmpDrkS6fR8d1L9s%2F4xIIcyQ5RTAcgLqMU68LbHMQky1qye%2FE6F46QWJhHcLC6uznDsrUoSUM0tt5ibTg4Nbt19zTO7FlUshptiaOoBmHF%2B0ie4BgPVfOWM2RIArjYipHwrZpSrW&X-Amz-Signature=e52dd634d5ad4befa9ba7c34746cc53b6b160fefcc03e9c541b086b859fdf931&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTGIUWUF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIECsc%2BrzZcJ%2BfI0QyLr6sygvsNWNVzyH%2FTmw4lN57FUXAiEA73rHP9BpN4njCiAW8GiOhvNkJImSXTzYRcmMx74QTUwq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHT3gUfA7G%2FZiae9KyrcA1j9sxnQENtTw3DavL7UL0%2BhhA1Kd6lwvPiEIqK0gJlCAQubfyc%2BIC%2B1OciXpSF%2BbM7WdGB9hTQpc9KHrwM84bhX3nY8K5WqMv%2FIeHtD7LNnRNeMqqfFrSc8WW97pcRHAqw3ZB3QB2pDxTABqh3gahWCcqMqJ%2FYKHA7zTspOPZEoQtRNTQGZRPg%2FmgLJiaVMjKDDphKLOtBKmo0iR4o7PztSWr04Z0HRlaNHwir3%2B9ZOEl2QTsltF01OYH%2BKJhI1o4UwbGF%2FKkcR38awnNxmEFpTEgXPdJZrgB7otKm%2F98o4KbT9bFVujYIM0LNQeyQhrm7J%2F%2FBPJ20cZAHmYuzhj5cYi24BLWbBTRji1dgDqjIQo%2FaSr7vFcJ0iTJCNc0t1ftYKF22x8Kj3v%2B1PqpcdLZ%2F3WsowO2AcNvOmP%2BdzJkusL2mLVUqjFi8j43KnOxyVRAIFhyv595gHyRK8AoaztCUKGeyHGJ0qdaq%2FTRsbV2i8g1lt0f12bCg52XCaFwfaHkO6Uawn5bvR4cO5zQNlBtzxBNPF5me6ETo6nSFsQSQ9AKqrSNQGaSoD7c%2Bf%2B2X3htSd4BlNQd%2FIwDCUck1iUvuzMifkQD6bSimi8%2BPZ%2FRNYmhz3wUHLEj9IWmiqMMC6jr0GOqUBlaE1kPDmRI3E55qBdOOCkbHVTwCtgu9L0r%2Bz9V5SsbDx6TAFyBhooUEOjz9jCoyVDK3RK8ELFgYXuZFQ%2FPZMjM%2FtVcrQsnsoXf58kItOyjK084rO8ncGayXBm5R4M2ClnjrKA6GVtrsotgX4JqLhRodAIoz2p5sAUQrqM2EmpwcVNW1RhTHRc0s863uv9LKUSSVFLYkVuLPds56wQVArzUCcYYtQ&X-Amz-Signature=61e447f52f61524f40bff28bcce409bad4176ad13e699f19ee09eec7ec0500c6&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RPGIW3Q%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDCJhm%2FWkpw2wwK7Mg0lh2FIZvN7ltjRNZ2b645%2BuyaAwIgKSg6MxhMn5iOlM2XIFReZ3ypFMxr%2FQ3MGsGgt%2FOMSEEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJpSOilI%2BEZuSdtAQyrcA0mRMhDSi4J6w3wabmG4MeXD6fy9yCsED8CpotkUv4QsZOYgaoKiTLyIq5%2FKpegWfRlik6vUNhz4C5xf%2BMGRsnQMBR0dT0zWiXsaMsa6USms6ZSqkbuoly0CMdO0xRhCijFhxnKMTh1stAGJNfPcdx%2BcrR63fbWDlqSkrIBxvqooTQXARxE7P1MGKjfYJ8RZQ6K%2BPEdlsPfHlD50BQ4XxZ3PDqfDfa%2BoDeOT9c%2FPofwgk9dfJrmmBGmJvuTH%2BRteFvcD2WSOhfBRK8vWssy%2BioRpA4miyPP3BIPx%2BAdLV0zJRb5j3Xq5CdqI3kC2KUtmHvQNlMnMDO8OvnkJIIu22glVknQEe3n7ybKR2PJsoVT7U01XGgUHVJaWZnI8cz%2BQgU9uW%2BWAmUyo7CLY6J1ubMUeYURQCCxf3Ww921CA0l0nBJ2sqDBsygQVaMnVcrY1x6BFzDLb7VUpI%2BBXO90%2F8V8SL4HLlAAqjyIvfjumX0y3LtM1rZFxRHc3RhhnSzBt5Wfb3dcYBhOQX3hq%2FpCr3DB1icY9tNITg951rDu%2BYc6nweS9CTJxnOpzGtLIaMFBUEcTJOSL2Rds5w0JzVaLCA1ogwk%2FsWYe9w5OgQwu37PEZ8Hbnv2wIROWZ%2BdYMNC6jr0GOqUBeN2qWbMouNa2kYLQO%2FR1fhhqhHVO7klV4QVUTfzRk0toMKt2NlT5YnSRMmDYnaKjTQ6%2FWo%2FPx8DZFaYgWbdaghA1my0EOmb27sWCSSTgHVe8xAC7ib6rX9jqShlVONWWM9E6MrtNwKyOSkVp9Vs6AJNpJzLPL5%2F2ffFDLtp4iojLjA2RGcZPbjDtH2KAvzS71nnLA%2BbNM%2FzOm0oCKGpkzA0%2BHn6c&X-Amz-Signature=628ef1815d9ba0521613f60f7f94c221f126ee75971d636a9d60eb5fb02a53b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF2JYKLS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIArr1K6BPdND%2BxlSGCP8WbMPi3uitLdS1IJJ1ZFpXLiyAiEAnA9el6hanCgs%2FR3IWIuAD7fK6HtK6debX%2BjI4gJrGTIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHOYHcr%2B5nIZo6kKjircAxSGZ9BFCzJtY6RDMtG1YN2yYe0YuCqwKOI8KTX1wQULW1ozQCL583yzQFCu6B51uIXow%2FLUKj%2FxVplp84Zh5CbVYnCmCMsZA8azyoabn%2B%2BcoCRWb1MtDfyUqZrbZiADxaK0OTHSbbJ%2F72BOAdNyZlGjMKHQcHnHcQbYcoVg3bdpRFjddtmjZJvDDOCcNvLyJtMQoUdRXS4RX6D0zd6gq%2Fsdc63WUcpQaf8GLhreY%2FLXwgrpWbRgXdRifJJHnYLRHi8omSQFapa60OW9f2m3dDWsd2WZaoJAMwWdY0THCbkhwsOPEQFDfeww0bh8zI2w0CGBOXPeMUoLcf5GuTdpeGfzJEwC47i8PuUPM%2FijAICE%2B6l9RBkVvun8ZZ5uAyuClg2b3oOua5vYjWgbqsSe%2Bw9V5948Jl8Owkhg10ESuQHAXx9yPQBxHqDszPOPAOSlhw4%2F7g5OFi1%2Fe4EdkdKPzDw%2F7VJT1bT%2BKb9HRTCdCQeawjG31NGfKY9YI%2BW%2F1Q0In5iwquV1hgAmKySwhP55kqOF8g8eX6%2B9QkQsolCqjcrwLaQfsr98KsJaJgKqbbGCrY8o%2FQmXSdByaXQjJXmvaGlq1TclSZUVy682RGxhfHWi6stVFaLnqc8jV4PqMLa6jr0GOqUB%2BNBvPanv4lyzZPb1WzKTxEr4MRs76BMmWiXMpP6J1UTDpDY6POG498loSPqGdDh9Bv4REeMPrQzIJAsAtWvXUmpDrkS6fR8d1L9s%2F4xIIcyQ5RTAcgLqMU68LbHMQky1qye%2FE6F46QWJhHcLC6uznDsrUoSUM0tt5ibTg4Nbt19zTO7FlUshptiaOoBmHF%2B0ie4BgPVfOWM2RIArjYipHwrZpSrW&X-Amz-Signature=1ccc8c8409b33ac235648a15ac37d3b35d852e974039b991dcf769f056dbd899&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF2JYKLS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIArr1K6BPdND%2BxlSGCP8WbMPi3uitLdS1IJJ1ZFpXLiyAiEAnA9el6hanCgs%2FR3IWIuAD7fK6HtK6debX%2BjI4gJrGTIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHOYHcr%2B5nIZo6kKjircAxSGZ9BFCzJtY6RDMtG1YN2yYe0YuCqwKOI8KTX1wQULW1ozQCL583yzQFCu6B51uIXow%2FLUKj%2FxVplp84Zh5CbVYnCmCMsZA8azyoabn%2B%2BcoCRWb1MtDfyUqZrbZiADxaK0OTHSbbJ%2F72BOAdNyZlGjMKHQcHnHcQbYcoVg3bdpRFjddtmjZJvDDOCcNvLyJtMQoUdRXS4RX6D0zd6gq%2Fsdc63WUcpQaf8GLhreY%2FLXwgrpWbRgXdRifJJHnYLRHi8omSQFapa60OW9f2m3dDWsd2WZaoJAMwWdY0THCbkhwsOPEQFDfeww0bh8zI2w0CGBOXPeMUoLcf5GuTdpeGfzJEwC47i8PuUPM%2FijAICE%2B6l9RBkVvun8ZZ5uAyuClg2b3oOua5vYjWgbqsSe%2Bw9V5948Jl8Owkhg10ESuQHAXx9yPQBxHqDszPOPAOSlhw4%2F7g5OFi1%2Fe4EdkdKPzDw%2F7VJT1bT%2BKb9HRTCdCQeawjG31NGfKY9YI%2BW%2F1Q0In5iwquV1hgAmKySwhP55kqOF8g8eX6%2B9QkQsolCqjcrwLaQfsr98KsJaJgKqbbGCrY8o%2FQmXSdByaXQjJXmvaGlq1TclSZUVy682RGxhfHWi6stVFaLnqc8jV4PqMLa6jr0GOqUB%2BNBvPanv4lyzZPb1WzKTxEr4MRs76BMmWiXMpP6J1UTDpDY6POG498loSPqGdDh9Bv4REeMPrQzIJAsAtWvXUmpDrkS6fR8d1L9s%2F4xIIcyQ5RTAcgLqMU68LbHMQky1qye%2FE6F46QWJhHcLC6uznDsrUoSUM0tt5ibTg4Nbt19zTO7FlUshptiaOoBmHF%2B0ie4BgPVfOWM2RIArjYipHwrZpSrW&X-Amz-Signature=1ece29b5b0f74a2ecc621d902fb0ed8bd02b6faf2dcf55534f9dce8f17c807fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF2JYKLS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIArr1K6BPdND%2BxlSGCP8WbMPi3uitLdS1IJJ1ZFpXLiyAiEAnA9el6hanCgs%2FR3IWIuAD7fK6HtK6debX%2BjI4gJrGTIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHOYHcr%2B5nIZo6kKjircAxSGZ9BFCzJtY6RDMtG1YN2yYe0YuCqwKOI8KTX1wQULW1ozQCL583yzQFCu6B51uIXow%2FLUKj%2FxVplp84Zh5CbVYnCmCMsZA8azyoabn%2B%2BcoCRWb1MtDfyUqZrbZiADxaK0OTHSbbJ%2F72BOAdNyZlGjMKHQcHnHcQbYcoVg3bdpRFjddtmjZJvDDOCcNvLyJtMQoUdRXS4RX6D0zd6gq%2Fsdc63WUcpQaf8GLhreY%2FLXwgrpWbRgXdRifJJHnYLRHi8omSQFapa60OW9f2m3dDWsd2WZaoJAMwWdY0THCbkhwsOPEQFDfeww0bh8zI2w0CGBOXPeMUoLcf5GuTdpeGfzJEwC47i8PuUPM%2FijAICE%2B6l9RBkVvun8ZZ5uAyuClg2b3oOua5vYjWgbqsSe%2Bw9V5948Jl8Owkhg10ESuQHAXx9yPQBxHqDszPOPAOSlhw4%2F7g5OFi1%2Fe4EdkdKPzDw%2F7VJT1bT%2BKb9HRTCdCQeawjG31NGfKY9YI%2BW%2F1Q0In5iwquV1hgAmKySwhP55kqOF8g8eX6%2B9QkQsolCqjcrwLaQfsr98KsJaJgKqbbGCrY8o%2FQmXSdByaXQjJXmvaGlq1TclSZUVy682RGxhfHWi6stVFaLnqc8jV4PqMLa6jr0GOqUB%2BNBvPanv4lyzZPb1WzKTxEr4MRs76BMmWiXMpP6J1UTDpDY6POG498loSPqGdDh9Bv4REeMPrQzIJAsAtWvXUmpDrkS6fR8d1L9s%2F4xIIcyQ5RTAcgLqMU68LbHMQky1qye%2FE6F46QWJhHcLC6uznDsrUoSUM0tt5ibTg4Nbt19zTO7FlUshptiaOoBmHF%2B0ie4BgPVfOWM2RIArjYipHwrZpSrW&X-Amz-Signature=983d44a33716f6b77a1c6bf97d8823511e2bd1394bf4fddd593684e1ebe44987&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQD6VOTI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFYwvmdvu%2F9tDu4nRDg0VHUPn8cJwzgQJVcNH3caXEztAiBCJ2d9BQp1HHlEmeWuPfSM3qYEhaoab8wAajkMWOwxCyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMhR9AEVVcc8c8i359KtwDd87h6YBdd9F2cFNPLSm7m2EfLcman3tv0HiTBakxM4jso5lyaA9UJRM%2FP3JtRB2rGvvkI0IJ4gWF6xaZ2yQe99LmITfzpdpAFYsuMmydeyOIN%2F9ySNuaJm4SlJMMnUiz2Mej3wiEy1FF%2BNbeyWu0Pb3No7A8xotR0ARjgj4IzmqfpQ7YE%2FbJm8JVFx8aC5vCLsZrXm5oUrNSVTcSlUI6H0mfYidDZx1U3LYKqsehENAl1Gm7CzjCqtw03xUFF0BRKcuyrNOHSMIcxY4vLcAzNCHn91IJRVxWXJkjNSRUjScSO7xs9pxoIA%2FAjJZtVzX4TxLJD2l3u6pcyyAdscOfnqnmnPALAch3tM0TfNVkdPQ6cVmjWVFYSAeJTWkPNIgD1aI%2FnJMWd9GEZpoUbPqtdQ8PCQkABJcbjQSVf5tZwI3iKxx4x4kxRHGHNiV64QWCeFKeSuktRYMkwki1qqRoLer2BnWMGbGRDIGKl8qFX9hVrWbusLVFMC%2BIP06PYKPpAcX1ioNzbpOJP4R%2FsSrfVu4ced3jlIQbYKBM74EVDDPQKIkAU5S4CmIUgwh1zFJptmPeMop3wOVF8xV7YOJqi4rcizMZb%2B8hinJzk4%2FTf%2BDsM7cc4Wi8xGflzLAwmbqOvQY6pgGrM3lH5SnZt5P2WRLZnFrENmospxzoR%2FVlbH3zZNyUE5dKZ8%2F%2BtImM9GwB3dBJnEx%2BP4eBkCBUdDgrQOd4KOHzmGPyl66toy1KpO%2FWQcQO8NfSzAdTZ8KOQkq1U1dFXV2v3yPYKDdKRgRgtHiHTOchGASOZ%2BKprmQ6jQoKffxJW%2BCFvXRY1tpQMsgzzmn3tkk1iG0YpAnvnFa2J%2FWgmMu7YruRjygn&X-Amz-Signature=7062fc6c0a5ba9c69c57d5dad958e2eed39cab723612ed712dc082be52644ea2&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVOKEURJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQC%2FEAzHCLc%2Bw%2FoWXEZpDj%2FCT%2FVoN%2F4oym8S0jD911fK0gIgR9N70Fpbmo%2BQBge78KzbrPjYjljwsUujyX83tewHWt8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBIaS3cFPIzi4Dkz9yrcAwPgwrGnSijIc8VSwV1uhh8qkEcN4A5gTmN7PfM8wPRSSxI6jq%2FPhxIyVXWg07Pe5VU7fz4UDBFOB7xrJzMz6xnFHHol%2BOAY1%2BHnI%2Faie%2Bs2Boq34gF32pKnCfnLdrLydsAC%2FSMg0qlqHDqpo92TOO%2BeK7XPhz9YI2QvrA14oxUfYiCb1uZXBLkaF2tM5%2BgklMBFwS%2BM%2FwfLxcUAL8KpTsA2VRq14ecaiMCQmlKRHjGg6FlhcmlQKo7IdZCS%2BE0fECNAH6SFAmJc2fRjz9VX5D%2BgVkOXdexJ7WzhJ8OD61tLviZwWkPm6%2BE2IH26w6M6GnInt5unt96UyPisEYVKgiXZ4HVb1zG5KfDwSENgcpgnXzqAd04bsXKXIYBMrmuuEoe0e0%2Fq9oRKwECnIxDA5muofKDgb25ugFl5uR79oQmh37ppmWbJKTcIlOevVpo%2B5pXCCRFMZ531wuR0k3YOKB6DKNPV%2BVDsGSUxaZ9fEsWJR3SJdSIKu84SIXQAWTigxs1CQwBhzbXOAeA1kQUU42abHs3CJvfH4fouVA4DWzeIxlq2bbIcVZPkBJNMoe96WwW8Xxmd7KXq7sNkdtgoOAQx1Cp7wp66CLpY519SPE8NsCuAHf0wrjhHedHxMLW6jr0GOqUBMf8rp2laP5O6xkzzjg%2FFxWScaJDC1rBsfjhb8ZBgGD4A7sVdreBa6B0yQObFnk0DWiCp1Afrv%2Fw9m56C2ff5IWOsUQswKelTgNdei1u1rohRWIfpcCTxqsIljiAysOGZp3FbI4tZ0mdLYPiD6ZqAK9V3nCCVpjY19Y12fi%2BFKMp43HIRO%2BHnwUiInjHrILEX3PkzzKTrir9K%2B2ubePGhDWxYLabC&X-Amz-Signature=6d97c0baac5d40478f61a8dffb64fea2d118cb9531a7da7f7ab44268c007c13f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWRZPKPU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCTnYSRsw%2Bq61GmBuoXRz1iSf0hVVAQqWmr%2Bq1Lu3fcAwIhAPwNMa%2FHr2FnqNgRxzGxzqMS4XISlwuZH0gKY%2BwWyU10Kv8DCEoQABoMNjM3NDIzMTgzODA1Igz%2F1MSUmcY0mzYLRJQq3AMCEOl48hg23x9M8vQYDOgx88UcAZogVlWZNhr32e9WhTt5gvRFB5K%2FiMkmGi8HXVU6r8Lchk3CuUpTEz4Br%2FiULmIf9ePL%2B%2FzpdsLc%2Bc0g72h2ElnJZdJS%2Bs%2F8mM52Bh1qxf7h34%2BorZ%2FfgSr%2FGA7uA6YowyJLg3E%2BmKJjyaz1BR09HRPeKQZStEYsmm9bxAF6HzfY1LoJK0iSLq6vTsEsDviOfy00XI130tXGCu9F1xN2kSVPswxxCaKaEhnClccJA54spwXdUuLP6MB1tKdvq%2BBOH%2BfGR%2Fw70jINfxZY4OL8u0%2FVrr%2FyFCIzheDYfwl%2FbiuCluFrOEa1jPX1owxe86%2BVceEIlPTLNEsNVK1WNqVXYKayDJGUKRPn2gL3lvRX%2BxRMh9hxslS2C%2FX8HRKvLW5%2FurBZ%2F0W9sie6d5JeFy6kg2gIJvnfzKGMlrJS6PRFSUoIAJHqFy%2FstkadCd%2FmX5IwEazAtVMpj%2FNnT9Dl3VxUeKOGc1vD1ma2E01IROxNRZlSkW0Z05vfThDNn0dBA9Xz6hvmgpJhX9hcZ6gtbl6R0n144S3r05PRPVgPX4V%2BePeNgqeixaA0AfGDQ0hXCeLgmIQilVAZ4dQzchpgo4EjxEPhSBWMWOYe3jDcuo69BjqkAehdP19DTKk0ewmxMFqgEVER0r4VwsstSQzbO5gI1BJSituvtGs5BoR4Q96wQNCkX80YzruED1PnxIPGdKG5KEZIfVXLiOp0v%2BYB86Hk5rtXyG1lvE5nh%2Bj5IPAKwoge5eBEf%2FzRzD69wruePWVopxJlpftbCS2jV9xEIexsj2rZySUjBmxXS8rJS58m%2FHUqt5xW1Zs6%2BQIvYJGgLLhnE3WbWlas&X-Amz-Signature=211018babeeda976c3a6006a4351ca05da3fd02da44439cb526a0528decf45b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDJAL733%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIBb%2BoSa%2BgH%2FnwhsslhqaEMLZyGvGegm%2FXiRBsEKDX3%2B8AiEAj7tMvTuRXE5hke8hVhBcAsgSlAhnxeCR4U%2B3foOSGRcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDF5qRtfXC8bkbQ%2FnryrcA5csI5g2sBpO9Lmft6i5v0gEGlGw0Z7RGgLpHDaAvUlAgZCgytLn8r4JfeQ8ukUx4puyMO8D72rcgWz4bQ%2FARxzs17rmkHwW3Za1WUXBNdSHoMvESkyRCz2rizV%2Bn14k8drmxKS%2BbdgnU%2FWPuIuJBfQWpxOFegIBJpyju%2FiVcXDIl4xpuq0be6PO9W4%2F%2FA2qHk%2BTf38ZY%2FIocOwsPS%2Blii62BjyD8bWr4HmL0iIYgDeLUDtk2YX%2BwYV8UukiwW%2Bq1vBKFDlbAXJmwWMWoKpHQPENucp5g42%2FWydbK3R2QIru0uSxtrN92%2FWVptOmU4pvciWBU8knkBgfnbIyJ1pKNX3BIIRgaWzmAupG77UGv%2FTpxh1flj%2BFux15xUNCOdoYhqiqrrMe%2Bp5HHxsrv9ZPh3K5OfM2Ekfum34pcNL%2F8iZTSMjkp8lEX2y%2FYSJ%2FnxQkam1A8mSCucym9hsBWILmpvQmuNlAaEK%2B1dOUUV5nZH38MHzQQkNDV1IpKzyi7KmAFQjstrhdx%2BeuQnBcus9ZoFkzR1DXMuhmGxoR%2BoYxWbqmVChRwj0sni1q66F2lh6n%2BrN9Dg8ow3%2BfWsbdQIPoLi1C1AV%2Bdjrlu0bGNiurmDnc3690%2FneaDeppjgZiMMC6jr0GOqUBOe0n%2FK4Nz8fee7MC3qI%2Bt8dsiaef83oXZDVKQCIaJlULtjznxmPpWIloLY%2B%2BZ%2Fl9M16IJC2siHnAlgZxSoiXOsGEpp2n1DeImIbkh%2F1gCqJ%2BOg3TRQAtSQoPlDxa1Rb2GOdDqsMDlkfqUia%2B9mpFpM6wEjc8PRq0SGHKyUNFuHSVPqTYHR4ftAOA6CuJbvQNYQewbPLH4oYbqzn1LrOLNe0B4VFm&X-Amz-Signature=6f0f7cddb1d305e10d71a4b314b4bff42bf27cead8552ed804e89f3fc190ffac&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDJAL733%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIBb%2BoSa%2BgH%2FnwhsslhqaEMLZyGvGegm%2FXiRBsEKDX3%2B8AiEAj7tMvTuRXE5hke8hVhBcAsgSlAhnxeCR4U%2B3foOSGRcq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDF5qRtfXC8bkbQ%2FnryrcA5csI5g2sBpO9Lmft6i5v0gEGlGw0Z7RGgLpHDaAvUlAgZCgytLn8r4JfeQ8ukUx4puyMO8D72rcgWz4bQ%2FARxzs17rmkHwW3Za1WUXBNdSHoMvESkyRCz2rizV%2Bn14k8drmxKS%2BbdgnU%2FWPuIuJBfQWpxOFegIBJpyju%2FiVcXDIl4xpuq0be6PO9W4%2F%2FA2qHk%2BTf38ZY%2FIocOwsPS%2Blii62BjyD8bWr4HmL0iIYgDeLUDtk2YX%2BwYV8UukiwW%2Bq1vBKFDlbAXJmwWMWoKpHQPENucp5g42%2FWydbK3R2QIru0uSxtrN92%2FWVptOmU4pvciWBU8knkBgfnbIyJ1pKNX3BIIRgaWzmAupG77UGv%2FTpxh1flj%2BFux15xUNCOdoYhqiqrrMe%2Bp5HHxsrv9ZPh3K5OfM2Ekfum34pcNL%2F8iZTSMjkp8lEX2y%2FYSJ%2FnxQkam1A8mSCucym9hsBWILmpvQmuNlAaEK%2B1dOUUV5nZH38MHzQQkNDV1IpKzyi7KmAFQjstrhdx%2BeuQnBcus9ZoFkzR1DXMuhmGxoR%2BoYxWbqmVChRwj0sni1q66F2lh6n%2BrN9Dg8ow3%2BfWsbdQIPoLi1C1AV%2Bdjrlu0bGNiurmDnc3690%2FneaDeppjgZiMMC6jr0GOqUBOe0n%2FK4Nz8fee7MC3qI%2Bt8dsiaef83oXZDVKQCIaJlULtjznxmPpWIloLY%2B%2BZ%2Fl9M16IJC2siHnAlgZxSoiXOsGEpp2n1DeImIbkh%2F1gCqJ%2BOg3TRQAtSQoPlDxa1Rb2GOdDqsMDlkfqUia%2B9mpFpM6wEjc8PRq0SGHKyUNFuHSVPqTYHR4ftAOA6CuJbvQNYQewbPLH4oYbqzn1LrOLNe0B4VFm&X-Amz-Signature=006abb55752bfe80498a3bacedb348da001ac8448b817f271bc19c1872726032&X-Amz-SignedHeaders=host&x-id=GetObject)

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
