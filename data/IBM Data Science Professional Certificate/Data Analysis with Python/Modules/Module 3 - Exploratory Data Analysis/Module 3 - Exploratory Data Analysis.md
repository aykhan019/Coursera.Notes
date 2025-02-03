

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZFAVSCN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCXkVkIoHd4aMDFiZgzV8KCDZO1k0Aka0VIXuxz6KjdIQIgW0XerxCS5SBP2tntg4PL6cNa%2B%2BtnHpilvd0kggRTqo0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDG2N%2BVKxdzzcJdPVqyrcA0hu9Udpmj%2FzzK%2Fder740NWL%2F191nbYtaQhKCmZeV1s14dbUgGRa0h5%2FMCoGE1jVo0Yk9zTPPu4nhhhRVwab4QMNycanzrEGYhvCI%2BVVmdbaC1qjKJDmxOG6s8ILcr3sRtdLxJU%2BEt1o%2BJ1ma4hvVk5tjCL6rhktCiWFzjwFzpmiwVolmUYQx6%2Bm%2F3HP4ub3ACpa2D7Ikrb6E%2B52QYOsRlEHHkowuk6Nm11MQkUBOnVji0jJ65CpXb5CQ1Mm%2FFuoC5Wx88J%2FBLBUk2afEHSuQcDmDttmiO6LqHDi1PvTvTnzKWSnmm9Ef%2FoSc%2F%2FAVdsgEqreR4wkDL6Ir69DOV%2B%2FHzap1N%2Bi8jUMHVU4cIi62aFzBJEY7g7OHIVEcoaONpC%2FBmRaztsYmSodMmrO9QPhYyPLEka5BKDyvi8FIz%2FcUgqiz3Cw0HgJlsvWpmCyrFPXGEj5sXeVWnwAfmoFYud5fWtjyjZO7c08q75wiL07QH34ca5goxbPOfBuAtXttoVYXBKkI7jXj9Kze85eySnDEhtCI71NwuworekcnTsXK%2FiRhWab4wUZxwlCoSRKRRibw3WOOkGI3w0w%2Fh1iYeboSdgpsM9%2BTJFWqi2%2FA%2B44WYCGPDGT%2Bmmxkah6VABOMLH3hL0GOqUBZSulNhc%2F0watFsQ80oaJ9mwfbkJoxHZ%2Ff6NqGlQc%2BPxnygFQ5TpOexypL8paybRtbEoqEKx9VgjJjqv9gIprYQGVW%2B5YKWrplzfm89qUmmKGe1O78Zq4T%2FLqrVPM3PV7d5WosIRen%2B85aWrcjTevI1V2HpZwdgrEIUooZj9gPDnYZ5G2Rh0UuZNbkDnhM%2BCeH%2FaJ2iAB%2BrSBoRYqF8bJvu6mJNdv&X-Amz-Signature=121a973811ad7f10013a14bcb4fa6c58b433b93bfa0c9b11ea1c8b61588cc475&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZFAVSCN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCXkVkIoHd4aMDFiZgzV8KCDZO1k0Aka0VIXuxz6KjdIQIgW0XerxCS5SBP2tntg4PL6cNa%2B%2BtnHpilvd0kggRTqo0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDG2N%2BVKxdzzcJdPVqyrcA0hu9Udpmj%2FzzK%2Fder740NWL%2F191nbYtaQhKCmZeV1s14dbUgGRa0h5%2FMCoGE1jVo0Yk9zTPPu4nhhhRVwab4QMNycanzrEGYhvCI%2BVVmdbaC1qjKJDmxOG6s8ILcr3sRtdLxJU%2BEt1o%2BJ1ma4hvVk5tjCL6rhktCiWFzjwFzpmiwVolmUYQx6%2Bm%2F3HP4ub3ACpa2D7Ikrb6E%2B52QYOsRlEHHkowuk6Nm11MQkUBOnVji0jJ65CpXb5CQ1Mm%2FFuoC5Wx88J%2FBLBUk2afEHSuQcDmDttmiO6LqHDi1PvTvTnzKWSnmm9Ef%2FoSc%2F%2FAVdsgEqreR4wkDL6Ir69DOV%2B%2FHzap1N%2Bi8jUMHVU4cIi62aFzBJEY7g7OHIVEcoaONpC%2FBmRaztsYmSodMmrO9QPhYyPLEka5BKDyvi8FIz%2FcUgqiz3Cw0HgJlsvWpmCyrFPXGEj5sXeVWnwAfmoFYud5fWtjyjZO7c08q75wiL07QH34ca5goxbPOfBuAtXttoVYXBKkI7jXj9Kze85eySnDEhtCI71NwuworekcnTsXK%2FiRhWab4wUZxwlCoSRKRRibw3WOOkGI3w0w%2Fh1iYeboSdgpsM9%2BTJFWqi2%2FA%2B44WYCGPDGT%2Bmmxkah6VABOMLH3hL0GOqUBZSulNhc%2F0watFsQ80oaJ9mwfbkJoxHZ%2Ff6NqGlQc%2BPxnygFQ5TpOexypL8paybRtbEoqEKx9VgjJjqv9gIprYQGVW%2B5YKWrplzfm89qUmmKGe1O78Zq4T%2FLqrVPM3PV7d5WosIRen%2B85aWrcjTevI1V2HpZwdgrEIUooZj9gPDnYZ5G2Rh0UuZNbkDnhM%2BCeH%2FaJ2iAB%2BrSBoRYqF8bJvu6mJNdv&X-Amz-Signature=9d77bbc6ce9ad848e21090db6fe42e5df91a6bb1de83736f2434880bb84af00e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZFAVSCN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCXkVkIoHd4aMDFiZgzV8KCDZO1k0Aka0VIXuxz6KjdIQIgW0XerxCS5SBP2tntg4PL6cNa%2B%2BtnHpilvd0kggRTqo0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDG2N%2BVKxdzzcJdPVqyrcA0hu9Udpmj%2FzzK%2Fder740NWL%2F191nbYtaQhKCmZeV1s14dbUgGRa0h5%2FMCoGE1jVo0Yk9zTPPu4nhhhRVwab4QMNycanzrEGYhvCI%2BVVmdbaC1qjKJDmxOG6s8ILcr3sRtdLxJU%2BEt1o%2BJ1ma4hvVk5tjCL6rhktCiWFzjwFzpmiwVolmUYQx6%2Bm%2F3HP4ub3ACpa2D7Ikrb6E%2B52QYOsRlEHHkowuk6Nm11MQkUBOnVji0jJ65CpXb5CQ1Mm%2FFuoC5Wx88J%2FBLBUk2afEHSuQcDmDttmiO6LqHDi1PvTvTnzKWSnmm9Ef%2FoSc%2F%2FAVdsgEqreR4wkDL6Ir69DOV%2B%2FHzap1N%2Bi8jUMHVU4cIi62aFzBJEY7g7OHIVEcoaONpC%2FBmRaztsYmSodMmrO9QPhYyPLEka5BKDyvi8FIz%2FcUgqiz3Cw0HgJlsvWpmCyrFPXGEj5sXeVWnwAfmoFYud5fWtjyjZO7c08q75wiL07QH34ca5goxbPOfBuAtXttoVYXBKkI7jXj9Kze85eySnDEhtCI71NwuworekcnTsXK%2FiRhWab4wUZxwlCoSRKRRibw3WOOkGI3w0w%2Fh1iYeboSdgpsM9%2BTJFWqi2%2FA%2B44WYCGPDGT%2Bmmxkah6VABOMLH3hL0GOqUBZSulNhc%2F0watFsQ80oaJ9mwfbkJoxHZ%2Ff6NqGlQc%2BPxnygFQ5TpOexypL8paybRtbEoqEKx9VgjJjqv9gIprYQGVW%2B5YKWrplzfm89qUmmKGe1O78Zq4T%2FLqrVPM3PV7d5WosIRen%2B85aWrcjTevI1V2HpZwdgrEIUooZj9gPDnYZ5G2Rh0UuZNbkDnhM%2BCeH%2FaJ2iAB%2BrSBoRYqF8bJvu6mJNdv&X-Amz-Signature=bf86044b491f9edb2f4fe30ffc64168adf323bbab8735fc571fa5ec305c29da6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KQTHDBM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDnzIJ1ch6lmiRpsJiyyNTRiP6pora49irm2yoGEjC2dAIgR1CVMe7R5uh3WhrrGw4aYvRIsiHzGa9KuJiB599BhGkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKWJYv1Q1112l%2BqhhyrcA618J8BIgqhZPIOuiFuWTGvUknovV0%2BNhrlZBfUW6QmXhl4s2qJDv0BgPHnouLu8UUChn56uZBm781GWxKLrr0sxlPJyBh5buRRyX356LPcA0bq1dj30MJ0992B8FGmkzEWMTjD%2BnaulCfvb%2BcbvYfWPcnmbUKDCXiCIvdFv9FqCk71H7zgPJzNabWeRpMfI74LSrqrAab0PO6FROKl9dPqFSHV5GGFBTtzdA83Ax%2FXR7Nh%2Be36x%2FQEXeIVs7Uz1gjDa%2F9J7ZtGM2GPfXGRVVoq9FrWkmfxibhW5LbVP9tgdvHoENvwA3e3WRJiWTTNtp8P1zbR9z%2FKjDis3EyV0Bu880gc8ysrQtbcWr5puroZKVgw%2BeoZ8JxGavqL4lpg2NWhOe8winmDz2l5eK%2BLPVEY0fnlF1RHU53bcc44PcgjpzCEh8TAtfYvmGoHJOsHo8%2BfJ4n8dqZ0GXqRkS1NfWs63LPYTBdZ7Tmdf58CFVcRL5V7ksEO9zVsREPUoajVZZIvwfn5JDvBfI3cf4267M%2BduR8Y8mkWUqYbpRLIH3S7kFEkyn6EJmPqrPJPCMRSQL4%2Bb2el9FYf%2BtYJbNCcLJ0LyQXAR0e08P7xQ4gQn9zoNnHGZUhzo8prd8TOrMMP3hL0GOqUBDs3%2FW1mRapl9NwiY7txfjjVwUs6bdi6YCFwSSL66W5uknnDhGFTu0O%2FqdQpOBkgiBvzXAv%2F2dfI5T65MSiOw0F3wQiC3fHFIGwRqlflbFOT%2BOQOh6DxtEGYHEk%2FgSzRTzef4vzwJqSJ6Ov%2BMMX9vFMAsvrqQIHXdUiaDyjpj0W7V8cCqdUcvRad%2FgvA29tmhr%2FDNo79Ae3vVESvClpPXhZjaH6ux&X-Amz-Signature=7e0834f41f6526e6302b69e4643f48c7b620c663f2a22e8a2ffce380c9a15869&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KQTHDBM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDnzIJ1ch6lmiRpsJiyyNTRiP6pora49irm2yoGEjC2dAIgR1CVMe7R5uh3WhrrGw4aYvRIsiHzGa9KuJiB599BhGkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKWJYv1Q1112l%2BqhhyrcA618J8BIgqhZPIOuiFuWTGvUknovV0%2BNhrlZBfUW6QmXhl4s2qJDv0BgPHnouLu8UUChn56uZBm781GWxKLrr0sxlPJyBh5buRRyX356LPcA0bq1dj30MJ0992B8FGmkzEWMTjD%2BnaulCfvb%2BcbvYfWPcnmbUKDCXiCIvdFv9FqCk71H7zgPJzNabWeRpMfI74LSrqrAab0PO6FROKl9dPqFSHV5GGFBTtzdA83Ax%2FXR7Nh%2Be36x%2FQEXeIVs7Uz1gjDa%2F9J7ZtGM2GPfXGRVVoq9FrWkmfxibhW5LbVP9tgdvHoENvwA3e3WRJiWTTNtp8P1zbR9z%2FKjDis3EyV0Bu880gc8ysrQtbcWr5puroZKVgw%2BeoZ8JxGavqL4lpg2NWhOe8winmDz2l5eK%2BLPVEY0fnlF1RHU53bcc44PcgjpzCEh8TAtfYvmGoHJOsHo8%2BfJ4n8dqZ0GXqRkS1NfWs63LPYTBdZ7Tmdf58CFVcRL5V7ksEO9zVsREPUoajVZZIvwfn5JDvBfI3cf4267M%2BduR8Y8mkWUqYbpRLIH3S7kFEkyn6EJmPqrPJPCMRSQL4%2Bb2el9FYf%2BtYJbNCcLJ0LyQXAR0e08P7xQ4gQn9zoNnHGZUhzo8prd8TOrMMP3hL0GOqUBDs3%2FW1mRapl9NwiY7txfjjVwUs6bdi6YCFwSSL66W5uknnDhGFTu0O%2FqdQpOBkgiBvzXAv%2F2dfI5T65MSiOw0F3wQiC3fHFIGwRqlflbFOT%2BOQOh6DxtEGYHEk%2FgSzRTzef4vzwJqSJ6Ov%2BMMX9vFMAsvrqQIHXdUiaDyjpj0W7V8cCqdUcvRad%2FgvA29tmhr%2FDNo79Ae3vVESvClpPXhZjaH6ux&X-Amz-Signature=b69646b8091829a9b60d47f5aae3b9649093aef79ee19c8b193879ac56eb68bc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KQTHDBM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDnzIJ1ch6lmiRpsJiyyNTRiP6pora49irm2yoGEjC2dAIgR1CVMe7R5uh3WhrrGw4aYvRIsiHzGa9KuJiB599BhGkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKWJYv1Q1112l%2BqhhyrcA618J8BIgqhZPIOuiFuWTGvUknovV0%2BNhrlZBfUW6QmXhl4s2qJDv0BgPHnouLu8UUChn56uZBm781GWxKLrr0sxlPJyBh5buRRyX356LPcA0bq1dj30MJ0992B8FGmkzEWMTjD%2BnaulCfvb%2BcbvYfWPcnmbUKDCXiCIvdFv9FqCk71H7zgPJzNabWeRpMfI74LSrqrAab0PO6FROKl9dPqFSHV5GGFBTtzdA83Ax%2FXR7Nh%2Be36x%2FQEXeIVs7Uz1gjDa%2F9J7ZtGM2GPfXGRVVoq9FrWkmfxibhW5LbVP9tgdvHoENvwA3e3WRJiWTTNtp8P1zbR9z%2FKjDis3EyV0Bu880gc8ysrQtbcWr5puroZKVgw%2BeoZ8JxGavqL4lpg2NWhOe8winmDz2l5eK%2BLPVEY0fnlF1RHU53bcc44PcgjpzCEh8TAtfYvmGoHJOsHo8%2BfJ4n8dqZ0GXqRkS1NfWs63LPYTBdZ7Tmdf58CFVcRL5V7ksEO9zVsREPUoajVZZIvwfn5JDvBfI3cf4267M%2BduR8Y8mkWUqYbpRLIH3S7kFEkyn6EJmPqrPJPCMRSQL4%2Bb2el9FYf%2BtYJbNCcLJ0LyQXAR0e08P7xQ4gQn9zoNnHGZUhzo8prd8TOrMMP3hL0GOqUBDs3%2FW1mRapl9NwiY7txfjjVwUs6bdi6YCFwSSL66W5uknnDhGFTu0O%2FqdQpOBkgiBvzXAv%2F2dfI5T65MSiOw0F3wQiC3fHFIGwRqlflbFOT%2BOQOh6DxtEGYHEk%2FgSzRTzef4vzwJqSJ6Ov%2BMMX9vFMAsvrqQIHXdUiaDyjpj0W7V8cCqdUcvRad%2FgvA29tmhr%2FDNo79Ae3vVESvClpPXhZjaH6ux&X-Amz-Signature=46f020904971e5e966156c829c506f48f31688ac8e507d542894ced9b3ec6c6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KQTHDBM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDnzIJ1ch6lmiRpsJiyyNTRiP6pora49irm2yoGEjC2dAIgR1CVMe7R5uh3WhrrGw4aYvRIsiHzGa9KuJiB599BhGkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKWJYv1Q1112l%2BqhhyrcA618J8BIgqhZPIOuiFuWTGvUknovV0%2BNhrlZBfUW6QmXhl4s2qJDv0BgPHnouLu8UUChn56uZBm781GWxKLrr0sxlPJyBh5buRRyX356LPcA0bq1dj30MJ0992B8FGmkzEWMTjD%2BnaulCfvb%2BcbvYfWPcnmbUKDCXiCIvdFv9FqCk71H7zgPJzNabWeRpMfI74LSrqrAab0PO6FROKl9dPqFSHV5GGFBTtzdA83Ax%2FXR7Nh%2Be36x%2FQEXeIVs7Uz1gjDa%2F9J7ZtGM2GPfXGRVVoq9FrWkmfxibhW5LbVP9tgdvHoENvwA3e3WRJiWTTNtp8P1zbR9z%2FKjDis3EyV0Bu880gc8ysrQtbcWr5puroZKVgw%2BeoZ8JxGavqL4lpg2NWhOe8winmDz2l5eK%2BLPVEY0fnlF1RHU53bcc44PcgjpzCEh8TAtfYvmGoHJOsHo8%2BfJ4n8dqZ0GXqRkS1NfWs63LPYTBdZ7Tmdf58CFVcRL5V7ksEO9zVsREPUoajVZZIvwfn5JDvBfI3cf4267M%2BduR8Y8mkWUqYbpRLIH3S7kFEkyn6EJmPqrPJPCMRSQL4%2Bb2el9FYf%2BtYJbNCcLJ0LyQXAR0e08P7xQ4gQn9zoNnHGZUhzo8prd8TOrMMP3hL0GOqUBDs3%2FW1mRapl9NwiY7txfjjVwUs6bdi6YCFwSSL66W5uknnDhGFTu0O%2FqdQpOBkgiBvzXAv%2F2dfI5T65MSiOw0F3wQiC3fHFIGwRqlflbFOT%2BOQOh6DxtEGYHEk%2FgSzRTzef4vzwJqSJ6Ov%2BMMX9vFMAsvrqQIHXdUiaDyjpj0W7V8cCqdUcvRad%2FgvA29tmhr%2FDNo79Ae3vVESvClpPXhZjaH6ux&X-Amz-Signature=a47001c2f00fbf04930084201ba9bceeedd6a7b936dadee24b5b334cc0847f82&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KQTHDBM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDnzIJ1ch6lmiRpsJiyyNTRiP6pora49irm2yoGEjC2dAIgR1CVMe7R5uh3WhrrGw4aYvRIsiHzGa9KuJiB599BhGkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKWJYv1Q1112l%2BqhhyrcA618J8BIgqhZPIOuiFuWTGvUknovV0%2BNhrlZBfUW6QmXhl4s2qJDv0BgPHnouLu8UUChn56uZBm781GWxKLrr0sxlPJyBh5buRRyX356LPcA0bq1dj30MJ0992B8FGmkzEWMTjD%2BnaulCfvb%2BcbvYfWPcnmbUKDCXiCIvdFv9FqCk71H7zgPJzNabWeRpMfI74LSrqrAab0PO6FROKl9dPqFSHV5GGFBTtzdA83Ax%2FXR7Nh%2Be36x%2FQEXeIVs7Uz1gjDa%2F9J7ZtGM2GPfXGRVVoq9FrWkmfxibhW5LbVP9tgdvHoENvwA3e3WRJiWTTNtp8P1zbR9z%2FKjDis3EyV0Bu880gc8ysrQtbcWr5puroZKVgw%2BeoZ8JxGavqL4lpg2NWhOe8winmDz2l5eK%2BLPVEY0fnlF1RHU53bcc44PcgjpzCEh8TAtfYvmGoHJOsHo8%2BfJ4n8dqZ0GXqRkS1NfWs63LPYTBdZ7Tmdf58CFVcRL5V7ksEO9zVsREPUoajVZZIvwfn5JDvBfI3cf4267M%2BduR8Y8mkWUqYbpRLIH3S7kFEkyn6EJmPqrPJPCMRSQL4%2Bb2el9FYf%2BtYJbNCcLJ0LyQXAR0e08P7xQ4gQn9zoNnHGZUhzo8prd8TOrMMP3hL0GOqUBDs3%2FW1mRapl9NwiY7txfjjVwUs6bdi6YCFwSSL66W5uknnDhGFTu0O%2FqdQpOBkgiBvzXAv%2F2dfI5T65MSiOw0F3wQiC3fHFIGwRqlflbFOT%2BOQOh6DxtEGYHEk%2FgSzRTzef4vzwJqSJ6Ov%2BMMX9vFMAsvrqQIHXdUiaDyjpj0W7V8cCqdUcvRad%2FgvA29tmhr%2FDNo79Ae3vVESvClpPXhZjaH6ux&X-Amz-Signature=556a49b577c48880fcd42a61dede2896cf9597a65a0e2750322fa126162a9a80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KQTHDBM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDnzIJ1ch6lmiRpsJiyyNTRiP6pora49irm2yoGEjC2dAIgR1CVMe7R5uh3WhrrGw4aYvRIsiHzGa9KuJiB599BhGkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKWJYv1Q1112l%2BqhhyrcA618J8BIgqhZPIOuiFuWTGvUknovV0%2BNhrlZBfUW6QmXhl4s2qJDv0BgPHnouLu8UUChn56uZBm781GWxKLrr0sxlPJyBh5buRRyX356LPcA0bq1dj30MJ0992B8FGmkzEWMTjD%2BnaulCfvb%2BcbvYfWPcnmbUKDCXiCIvdFv9FqCk71H7zgPJzNabWeRpMfI74LSrqrAab0PO6FROKl9dPqFSHV5GGFBTtzdA83Ax%2FXR7Nh%2Be36x%2FQEXeIVs7Uz1gjDa%2F9J7ZtGM2GPfXGRVVoq9FrWkmfxibhW5LbVP9tgdvHoENvwA3e3WRJiWTTNtp8P1zbR9z%2FKjDis3EyV0Bu880gc8ysrQtbcWr5puroZKVgw%2BeoZ8JxGavqL4lpg2NWhOe8winmDz2l5eK%2BLPVEY0fnlF1RHU53bcc44PcgjpzCEh8TAtfYvmGoHJOsHo8%2BfJ4n8dqZ0GXqRkS1NfWs63LPYTBdZ7Tmdf58CFVcRL5V7ksEO9zVsREPUoajVZZIvwfn5JDvBfI3cf4267M%2BduR8Y8mkWUqYbpRLIH3S7kFEkyn6EJmPqrPJPCMRSQL4%2Bb2el9FYf%2BtYJbNCcLJ0LyQXAR0e08P7xQ4gQn9zoNnHGZUhzo8prd8TOrMMP3hL0GOqUBDs3%2FW1mRapl9NwiY7txfjjVwUs6bdi6YCFwSSL66W5uknnDhGFTu0O%2FqdQpOBkgiBvzXAv%2F2dfI5T65MSiOw0F3wQiC3fHFIGwRqlflbFOT%2BOQOh6DxtEGYHEk%2FgSzRTzef4vzwJqSJ6Ov%2BMMX9vFMAsvrqQIHXdUiaDyjpj0W7V8cCqdUcvRad%2FgvA29tmhr%2FDNo79Ae3vVESvClpPXhZjaH6ux&X-Amz-Signature=623931da7c40ac17c71ef7ed3b988197870b402f9b8d5450776cf7568e072aea&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWUXIVMU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIAc2%2F9JTlM%2Bd%2BO%2BUFx%2B0Eh%2BNvWUX6s%2F9bgMcKt9Q1dfNAiEAkCmPIvgj5u7Sy26kzAPoGzAYWhssXkzfILJW2qlq6Csq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDExYzkUpAzCAE2sujSrcA1hz5yzllJg1Z6HtiSIzhffuf617Dj7Q0VCbYpDA9gPqa96zkt1EYpuQymRGFph%2F30X2o1lTLau3AK6AwU9D%2BizefFiD0Jd4PeXyaZ0rCSze%2FV8upeebeqE5QJiXSAwi4wlNTRtDANG%2FGsgGEu2QwXrzJdxkpGk8fVbFTZErGF8rcDmZwnW%2BAP09zseP%2FsefqNcZycgF7gEgS71gyLmHzzawnvstbWLrfgqL9r5WRN2zbn%2Bxjgtx9DUJqB%2FxQVofYwn%2BtPw11fZfT%2FBsn6nfA1vo3v%2Bewef5%2FTKU9QTmO7os%2FXgHvd7LhYbJevgb1x3KR2xQL9gUA2IzSEKtIJYnFTJe77nks%2F%2FaRqgQR4QOS%2Biy%2BjG%2FtHWC56Z3qEes%2FBmbyFFgwP7uCvglSd7s5EEHJi4h9WtDb9LOAg%2B7myM882xLTh%2BPc2HEhyPGnznMRL0%2BnE1V032QtuhfvV2cZOEA2KxoUNd4qlUxpDeOsoPmJyFHeT9tywmuW6uW1GA7cyPRE67KrvOHsw457bQOAw%2FlgWRt00P6yK8FC0TIm3xvWATEml3hXGRO9NpaxIeZ%2BM9UZ2cwGqvYO7GrA4iCUk%2FyBBfb7citZWnpgw3N83nk2MNUWQGYAARz5rVAkSk1MJP3hL0GOqUBgXg2Os9LdK6sLlECU9aO36PKj0wl1XWB1te8mM5QeiWkeW56VJCH5%2FBgnuYoUDO3fZgtI2AcUYarebAGOvPbQh2Q9kfZtXuA0bPyRsi6v2pyffqaaL1yc4Kt6SJWiVnNBFJu7%2BOilou5BZMr8hPyj6pGLMwExC4M%2BWSGM2YQAXBG7FvqnSB%2FvVfSquUEdg6sat4NnPcSLCtvwOd3XvqwuuqcnEqn&X-Amz-Signature=17940f2927d718431c27e886f7d3150982afe2355f03e512e955ebccb43eecd1&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665B4LZNTD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQD3xfiYXzxRfBzoLlk7UbxOSo5aU9JTMAy4cs%2FHjjrnqgIhAJr7pEu%2FPPxsV9ZSKNKoqFFokZhtNQN6Xz63TwV2wjZcKv8DCB8QABoMNjM3NDIzMTgzODA1IgwyzpyxyZyP%2FZlfb0Qq3AO9AdXcn1aFIkT73o8fAP%2BSwbIIkD7JsCnmoLab86UqoNwy22XrA2QDcmhtOUD1eB63OaCk%2FKRsMfM39Zk%2BoBPi55K%2BpeBAbXgjfgBVdUeoe%2FMhxsbtbxJkayMImg%2BO8uI05%2F4GBHTtmdSBeDJ4VdDLFikCQZ9VKtn6cAR4mWOLhJlQbgCgvoVs66uJVs%2F0%2FjxnfK6brQYGln9kQMvvhct%2FtEKC4Z%2F5QWN9hDlDOU5FrMKGm244bP0LQGShc4XuEQl8%2Fygzi0SbJayJOG%2FtCXYEAnMZWOmTnh2SK61lV7geqYncaWEshfvqgcy%2FQc6EX3fSHSk0hIIoVOfYCVbHLvB1MSDwxz04GWOGVFSL5iBf9Z4dETj5XVzFY9nYtMi1I78N%2F4kmE3x7RdzaYTr3bRj2fb1u8YrO9D9eDghJrONQ%2BOv7O19AI1waa%2FSD48IJAVx7TvBQmiJguPDaLZQRLInN3tRBTNK80l1uCQy%2Bn9ymuJfEajNeg4MT7ShdmndELTDGra0KoIi6hdCiXyMkp4pWlooFLmF9ajZh203WMAQAkS6b7N4uy5rCNnJ9OERnwLAg2KNLL8mLk99Dx9l9%2B4MVEKMWGUmhb6nTW6M58WZF1BIbT%2B7p%2Fas73Iz4%2BjDx9oS9BjqkAXSPzPObjwIPIfLjiNGjRVGcZUI1GYEKCja9aHK0hqN3a8svzw4N04UmUh%2BCTlXLfoRbLCeaMXLNpcF9OIIr89L4ZkuPJu9Vxz81Byp7vWj%2F4a0uyS2UPzAocNhiafmaPBwuN0efKTsu%2FmbSxkaEH6KLoMgVDPMJziiJeZmPA3xC2RtGchK7qXOzL22N9QzImMM2j0UkHk7ddnbCtYeDVJgmajK1&X-Amz-Signature=b162cee163f3dc83841e49d45c1354d0a0f83e74344769b97f59ef1f2c03c784&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KQTHDBM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDnzIJ1ch6lmiRpsJiyyNTRiP6pora49irm2yoGEjC2dAIgR1CVMe7R5uh3WhrrGw4aYvRIsiHzGa9KuJiB599BhGkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKWJYv1Q1112l%2BqhhyrcA618J8BIgqhZPIOuiFuWTGvUknovV0%2BNhrlZBfUW6QmXhl4s2qJDv0BgPHnouLu8UUChn56uZBm781GWxKLrr0sxlPJyBh5buRRyX356LPcA0bq1dj30MJ0992B8FGmkzEWMTjD%2BnaulCfvb%2BcbvYfWPcnmbUKDCXiCIvdFv9FqCk71H7zgPJzNabWeRpMfI74LSrqrAab0PO6FROKl9dPqFSHV5GGFBTtzdA83Ax%2FXR7Nh%2Be36x%2FQEXeIVs7Uz1gjDa%2F9J7ZtGM2GPfXGRVVoq9FrWkmfxibhW5LbVP9tgdvHoENvwA3e3WRJiWTTNtp8P1zbR9z%2FKjDis3EyV0Bu880gc8ysrQtbcWr5puroZKVgw%2BeoZ8JxGavqL4lpg2NWhOe8winmDz2l5eK%2BLPVEY0fnlF1RHU53bcc44PcgjpzCEh8TAtfYvmGoHJOsHo8%2BfJ4n8dqZ0GXqRkS1NfWs63LPYTBdZ7Tmdf58CFVcRL5V7ksEO9zVsREPUoajVZZIvwfn5JDvBfI3cf4267M%2BduR8Y8mkWUqYbpRLIH3S7kFEkyn6EJmPqrPJPCMRSQL4%2Bb2el9FYf%2BtYJbNCcLJ0LyQXAR0e08P7xQ4gQn9zoNnHGZUhzo8prd8TOrMMP3hL0GOqUBDs3%2FW1mRapl9NwiY7txfjjVwUs6bdi6YCFwSSL66W5uknnDhGFTu0O%2FqdQpOBkgiBvzXAv%2F2dfI5T65MSiOw0F3wQiC3fHFIGwRqlflbFOT%2BOQOh6DxtEGYHEk%2FgSzRTzef4vzwJqSJ6Ov%2BMMX9vFMAsvrqQIHXdUiaDyjpj0W7V8cCqdUcvRad%2FgvA29tmhr%2FDNo79Ae3vVESvClpPXhZjaH6ux&X-Amz-Signature=c7b2e66dd984200b297345191f207e4f090d3a7a8cfa1ff340fdcd0bdaafc646&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KQTHDBM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDnzIJ1ch6lmiRpsJiyyNTRiP6pora49irm2yoGEjC2dAIgR1CVMe7R5uh3WhrrGw4aYvRIsiHzGa9KuJiB599BhGkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKWJYv1Q1112l%2BqhhyrcA618J8BIgqhZPIOuiFuWTGvUknovV0%2BNhrlZBfUW6QmXhl4s2qJDv0BgPHnouLu8UUChn56uZBm781GWxKLrr0sxlPJyBh5buRRyX356LPcA0bq1dj30MJ0992B8FGmkzEWMTjD%2BnaulCfvb%2BcbvYfWPcnmbUKDCXiCIvdFv9FqCk71H7zgPJzNabWeRpMfI74LSrqrAab0PO6FROKl9dPqFSHV5GGFBTtzdA83Ax%2FXR7Nh%2Be36x%2FQEXeIVs7Uz1gjDa%2F9J7ZtGM2GPfXGRVVoq9FrWkmfxibhW5LbVP9tgdvHoENvwA3e3WRJiWTTNtp8P1zbR9z%2FKjDis3EyV0Bu880gc8ysrQtbcWr5puroZKVgw%2BeoZ8JxGavqL4lpg2NWhOe8winmDz2l5eK%2BLPVEY0fnlF1RHU53bcc44PcgjpzCEh8TAtfYvmGoHJOsHo8%2BfJ4n8dqZ0GXqRkS1NfWs63LPYTBdZ7Tmdf58CFVcRL5V7ksEO9zVsREPUoajVZZIvwfn5JDvBfI3cf4267M%2BduR8Y8mkWUqYbpRLIH3S7kFEkyn6EJmPqrPJPCMRSQL4%2Bb2el9FYf%2BtYJbNCcLJ0LyQXAR0e08P7xQ4gQn9zoNnHGZUhzo8prd8TOrMMP3hL0GOqUBDs3%2FW1mRapl9NwiY7txfjjVwUs6bdi6YCFwSSL66W5uknnDhGFTu0O%2FqdQpOBkgiBvzXAv%2F2dfI5T65MSiOw0F3wQiC3fHFIGwRqlflbFOT%2BOQOh6DxtEGYHEk%2FgSzRTzef4vzwJqSJ6Ov%2BMMX9vFMAsvrqQIHXdUiaDyjpj0W7V8cCqdUcvRad%2FgvA29tmhr%2FDNo79Ae3vVESvClpPXhZjaH6ux&X-Amz-Signature=f46b7af7e80c61e190868eaf9c58883ac1275d500c5b74bb8f2eb3056cd40a47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KQTHDBM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDnzIJ1ch6lmiRpsJiyyNTRiP6pora49irm2yoGEjC2dAIgR1CVMe7R5uh3WhrrGw4aYvRIsiHzGa9KuJiB599BhGkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKWJYv1Q1112l%2BqhhyrcA618J8BIgqhZPIOuiFuWTGvUknovV0%2BNhrlZBfUW6QmXhl4s2qJDv0BgPHnouLu8UUChn56uZBm781GWxKLrr0sxlPJyBh5buRRyX356LPcA0bq1dj30MJ0992B8FGmkzEWMTjD%2BnaulCfvb%2BcbvYfWPcnmbUKDCXiCIvdFv9FqCk71H7zgPJzNabWeRpMfI74LSrqrAab0PO6FROKl9dPqFSHV5GGFBTtzdA83Ax%2FXR7Nh%2Be36x%2FQEXeIVs7Uz1gjDa%2F9J7ZtGM2GPfXGRVVoq9FrWkmfxibhW5LbVP9tgdvHoENvwA3e3WRJiWTTNtp8P1zbR9z%2FKjDis3EyV0Bu880gc8ysrQtbcWr5puroZKVgw%2BeoZ8JxGavqL4lpg2NWhOe8winmDz2l5eK%2BLPVEY0fnlF1RHU53bcc44PcgjpzCEh8TAtfYvmGoHJOsHo8%2BfJ4n8dqZ0GXqRkS1NfWs63LPYTBdZ7Tmdf58CFVcRL5V7ksEO9zVsREPUoajVZZIvwfn5JDvBfI3cf4267M%2BduR8Y8mkWUqYbpRLIH3S7kFEkyn6EJmPqrPJPCMRSQL4%2Bb2el9FYf%2BtYJbNCcLJ0LyQXAR0e08P7xQ4gQn9zoNnHGZUhzo8prd8TOrMMP3hL0GOqUBDs3%2FW1mRapl9NwiY7txfjjVwUs6bdi6YCFwSSL66W5uknnDhGFTu0O%2FqdQpOBkgiBvzXAv%2F2dfI5T65MSiOw0F3wQiC3fHFIGwRqlflbFOT%2BOQOh6DxtEGYHEk%2FgSzRTzef4vzwJqSJ6Ov%2BMMX9vFMAsvrqQIHXdUiaDyjpj0W7V8cCqdUcvRad%2FgvA29tmhr%2FDNo79Ae3vVESvClpPXhZjaH6ux&X-Amz-Signature=00babd43d63d2945efca708a75010e5bd72f9389861706bcdd76f11c737b66a9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDM53IRF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIAmkiKklFDENpx4FnZcD9Fb2J3ewkm4yrcgjfJXuBWZIAiBlxrwqHbiHndlG6NlJFDgzjnZAAERKjjcH677JEnXBxir%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMhD5EN4OIUuTmKSl0KtwDjeZr6lwocmRh%2BJn21zznd0HTPovyJnP8WKNvYtaSVOk8hD0LRRwr%2BZp8iMQ%2BXZtKhWvw5QmsyIsKv8xLC43FK22YBBylWQW%2Fen5A7lbU3yyTehRvGN4wrFUTzUvgsdb7rCxvW8gPWjYx2KDboxVepQQ0B%2FafzMt%2FiTawlyp0L%2ByPSs9EXBf8XRaNfS1mDclOzmSEuhLV8l7Buv1CdL328u1FYCCuEB%2FHdRQ6%2FpHbjV6xxn1zzz1fy9Ki99qCQw7i3czOE5%2Fre5rFeVC1l9GaTL%2B2AVFaQ5TjKJEEIT97%2B6Ii4GFvlFJ0BHdKrowM%2FMdDLbsKhv95gGMyUE65yeb2xQ9ydKV3qBy3%2F%2F6uUrJ9yAbmJltPyjJGuTtc8%2BlUkUJjksHRWqpUw5x8wdlOF8r9%2BHVHR496zcsWtD%2Fyqm%2Be3fZlLqWbse%2BqwBTcQHy3EjZj2z91%2B2Bo8jb59YWDPfWg5AogXkKPQKpXyyOaqCf%2FLO1byDNsHxN7Ljl8Atmu3qek0Wvcu2oFBumV%2BF1KjZ9C%2F7AgFBYEkvXoKuWUo5JcqP1lWlaFqA3Z2lavBeG9nVqsPpOGnNsPdLGDpMiZif1p8O9w50WVXtX8LWOdOFfJzrzPqXPuKJG2IXV%2Bv%2B8w9PaEvQY6pgHYiUjiJWUch7l01p35g8jFoDj1cu7pleFCmzkEE%2FckpDZ06%2BMcP7fiv6ynfuKl2rxWLt%2BDnBjTnk5b5hsMIqTs1ojgbCioipqvI%2FGvxazsO7SXYcQS4t3A6s0xETFWNB3PL%2FojBPXYEREUx6RSiVc%2BV4Q1Z%2FZ%2BwhaWXnDxdSOJNkYLUg9PVdTnRaOWV8lWoin7%2BUuXXsPp09yOvncITA5d1gDVwF8T&X-Amz-Signature=9b4f7c64043467840b4b8aa76b9c85dda304154a0b42cd49d56a871f9c39ec44&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPQUW7JH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCANwT2rrCmT5032rfHGAKjKUsXR9991idU62FzZAhX9QIgMMaLPCb9GJljA0l6M65FrsUDjp%2BKFuK%2B7clEiAE11y4q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKzYLbFMXVB%2FGiAQoyrcA2LDqJZmf74SL0XNQTzpCd%2BLMghwsNnYxNMiS4l3GhvmsYnRPBdsrf0B3YOEsq1ky8vF8q2bNECmxlt4p7PZGTCru1p6WBpX89ZGrsUd5O1EWGjhP8Xi10WYwH8aXEmkabc8AA%2Fw0oasbgCWwFMtUy2ATqssobVm0m%2Ffr7feVXnXSxA1xLd2RGfiL2qkUacuNssjGOKprWvzmNpCSQ47PURV7OUrHkBqqk%2B7Gqbr0%2F9y480hxdaR%2FhjsS6I9RMAXKkwEBmXMpF6TXCGOY2dqI7AXf7SpGsEx778PiyH%2Bch3eLkYvIwpJ55276qZoFYaQ52JCWOcisE%2Bt93J6zQ2l5%2F2NoiBpIm58wi8T3lA19Rf%2B6%2FRmS27gzLZUFtmrCKgcSfoTE5rUKEIHFm6VmT2DSjv%2FLjud3FVJummUFYGHI6%2BfO1uMKDrd0jMmYlCLzt%2Bpd5l46OXG1pDhg3A4pL7p%2BNhMfb%2BVV5xnS3vDF%2BsI%2B8u1F6LPndLh1%2F%2F6ve3%2BAErGxcmtfZP58lLo2CCcZfpN7SxfF6AAT1CFmzbU5dzA2%2FxMj99%2FNrSRrPDLuqQ%2F9Q75DV5bdXVpUmgZFDbCVYHJZV4DUVsRdXt4l2CBCp%2FIfn%2FdrrDY4DiBsmN2Li9gMOL2hL0GOqUBG3z6YL7IE1ocqyk2ZZ%2ByRROxLPg9oKPdfiVnseZXvZUgad2NEnjjIGYYnsflZPyHX7fKNmTFrDZYI6Vv%2FU4EOXIOShIHy0VKp6S5k1AfEyGdC0ShUKZ4%2FNy4%2FFkUjionpNwwP6fYG2kPudisiza3TGpLeUKopGVFK%2F%2ByVrm5AX0y6HLA%2BQyVbq1JiAcdusYGQqrhvbqsuzG3tBPY9TjuiHyzSo5N&X-Amz-Signature=6da8dabdd99a52e1677912001a3dd77e2312d8dc3126b34ea758e9bff522efd9&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OASOGBH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIE%2ByESLDkFzthKo%2FOVGeruRoybdhgK2MyFjhcSCJ4fgpAiBcojjDTlgzS9owzggw1%2Bu9hmmn90S597nrxT3Cxw1zEir%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMOOb%2BNcn%2BritaH0%2B7KtwDWl3aaprrJy2rNQdEadKD45YxluxipcyXxiTAb247f399hgUlZLbrBEWzijeI3nkD6MddSRxETFRuWZfuA%2BHKE1GjxdbTEX5uBySFeUulnro6E9Q0u95%2FHuU9%2Fb7SHto3e0UmkOku%2BEIabEIF7sbAFp21sVGbo2tpcou77%2FjdtNY8s9%2FGAVTiLnPzZlJg2wZzs%2F6xO%2BcxucxCEXB%2FJplDpZALp95JyK4RYkXrtjvU%2BkAsV02JHHdCENxwCkpHEHMIH5iyzouJBsUyJE7WZDG8KcqKjVLaeH0A2UW%2Bg40c7YSREKysjXvbU3gwHs6%2FUIud%2BePp9NMvayKbQX8DARjde2UG7txUorAxjuU1yolksNg8KuUIUhln9%2Bk2HYiCUneYyv466SHxTcxBZsctPBKvY8zSpnbHYmO7kI7GQjM1OLFkTZiP6%2FwPKaw7MYZ3HI%2BUxVrVqwQzsETQn24%2FfA02hXZlAvReXYoItUZ9LBFRm%2BLiOLsCnYi9hR%2F27aTat5IoM%2F2YBCTS6%2B7wl353NwyFVOXcXTHKShlC77SyhF5RHSferLXIZhB8CXTAU53Rv86BlfHUAMTATQjfGBmHW%2F%2FwzkvX8JB6Wmf9SGeN7nQfZuNILqbyaCt1oSpxEgkwufeEvQY6pgHj7yL8gIMlt01QKHb4Z74jsqyrg7d1cj7nKZLFePQbp0x1uPfLVPsv%2BL10l8INudU0WPnxHq5HXj9MCSB0ZKtNhjRumcdqz7b%2FTSO5PFz28mD%2Ffoe3s3RuHPeZ0rF8aqXtupU2NjzHGZ6y3sBByZiRKXYnym4TqxhLFmsZ05U71PyZT%2B6DEFyAgmD6fEmrqMZet8g000fCyFU0tAuCKglCn%2B4QB%2BBY&X-Amz-Signature=d43db07c56300474cdd8bebe08117d981014298715f14f248953545f41b31f92&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPWW75CI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCICr53%2BLOCpRhCLG%2FGpSgHl%2FJx9t4QDYk5Kr34qSgSQV1AiEAssmoXWuRcF0xSU5bogMYqfQKioGat76ASih9FI7mBPkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOeyGFwCiCBI96tKSircA%2BvREf4LHavPilkHBOh0Z2Cn5bLx8Q9uWmE5mzrhoQK6zK1p71I2Kbnzai7sHmEIWZB6oFEhkY82M5iydTKo%2F1VbN4w8SGgMC1roIbzEB2gUoBLU%2FtsFGhfzYNHNwaqbbkmZ9XIx4IdWSGwY82WSz1utQap%2BlnaE8zWZl2P%2F9reeF%2BrWokpuDDZbZfpe%2FndcoJRhWUUNc%2FvyIUep5iQdo%2Fj0uQDLcLwhy96MCw3UrYDBwB1iqMYCUJdr6S5T9yFbrjtiqB7g%2FcLpTgxtMYgybg%2Fa1Kh%2FPYJVHKf6NGA2Pzge9o3xgOkevYDLvcBLjOtFq4puhOwT54P5QLLuSqMS4HBv1Bw4V%2Bti0QrNYLRwiI5%2F%2F5RcD%2FRg7yMCcxaNC%2FHuDn3z%2BxOBYY9pQDWx0Tn9acYndmsdrSae3iUo9BDw4pjUVoSCTMTDKOhI%2Bcs%2BM42lDgpguEenlM9Ma5GorE%2BH9GUlAq%2Bp2dm0ZkoTedrjaBhfxDDOuBpSkIo%2FEM9kpFYwO34NrmsUwj2GhqU6DujDjI1%2BaRgoZ5D9IVgiBN1iM5YkMRTweYt911Asya599jGZ8dh4ye0uJtE%2BdBVLssEuPFXR680u8113if2vGnqxnfUISBC%2FAblPmQXgoO0uMIj3hL0GOqUBq6dZR1s0CxR%2FLZeqQFlw2l%2Bo%2BOhogHBxZND%2Bnk02wwU8OUglb7O8NeivEA%2Bp82fPa%2FtPUIcED0IsYvwNQ8nIa8eEEWpt9%2Bl9TA7bt5IWVdLhnocqiagG7Rx%2FkeIQ7QTObLU8JfGzvMM3xrj2DIN68RxytmdrV7BJBU6vSR4buF6c9nicBvRUkV5y8XrLNxWkUAs8%2BxKpA0TBgLxFNz%2Bu6QQibTpf&X-Amz-Signature=38a7537ec325912aee21e0fd25cfd7091a0241702b68bdfd2f962a3b7d550f63&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPWW75CI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCICr53%2BLOCpRhCLG%2FGpSgHl%2FJx9t4QDYk5Kr34qSgSQV1AiEAssmoXWuRcF0xSU5bogMYqfQKioGat76ASih9FI7mBPkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOeyGFwCiCBI96tKSircA%2BvREf4LHavPilkHBOh0Z2Cn5bLx8Q9uWmE5mzrhoQK6zK1p71I2Kbnzai7sHmEIWZB6oFEhkY82M5iydTKo%2F1VbN4w8SGgMC1roIbzEB2gUoBLU%2FtsFGhfzYNHNwaqbbkmZ9XIx4IdWSGwY82WSz1utQap%2BlnaE8zWZl2P%2F9reeF%2BrWokpuDDZbZfpe%2FndcoJRhWUUNc%2FvyIUep5iQdo%2Fj0uQDLcLwhy96MCw3UrYDBwB1iqMYCUJdr6S5T9yFbrjtiqB7g%2FcLpTgxtMYgybg%2Fa1Kh%2FPYJVHKf6NGA2Pzge9o3xgOkevYDLvcBLjOtFq4puhOwT54P5QLLuSqMS4HBv1Bw4V%2Bti0QrNYLRwiI5%2F%2F5RcD%2FRg7yMCcxaNC%2FHuDn3z%2BxOBYY9pQDWx0Tn9acYndmsdrSae3iUo9BDw4pjUVoSCTMTDKOhI%2Bcs%2BM42lDgpguEenlM9Ma5GorE%2BH9GUlAq%2Bp2dm0ZkoTedrjaBhfxDDOuBpSkIo%2FEM9kpFYwO34NrmsUwj2GhqU6DujDjI1%2BaRgoZ5D9IVgiBN1iM5YkMRTweYt911Asya599jGZ8dh4ye0uJtE%2BdBVLssEuPFXR680u8113if2vGnqxnfUISBC%2FAblPmQXgoO0uMIj3hL0GOqUBq6dZR1s0CxR%2FLZeqQFlw2l%2Bo%2BOhogHBxZND%2Bnk02wwU8OUglb7O8NeivEA%2Bp82fPa%2FtPUIcED0IsYvwNQ8nIa8eEEWpt9%2Bl9TA7bt5IWVdLhnocqiagG7Rx%2FkeIQ7QTObLU8JfGzvMM3xrj2DIN68RxytmdrV7BJBU6vSR4buF6c9nicBvRUkV5y8XrLNxWkUAs8%2BxKpA0TBgLxFNz%2Bu6QQibTpf&X-Amz-Signature=b2eccaa0f208a114b236e1cb026fadfa3bb284e9e3606f86b8baf4a711cce376&X-Amz-SignedHeaders=host&x-id=GetObject)

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
