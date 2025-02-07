

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QGTPKZD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDpX3md7IzHY5sJx34NrZKd%2F5lBsRmVsofbPpfucW7BkgIhAN7Ukm8U0SfH67%2BkzJAHQaAJyn7r7NFwJeD6jKF93QtvKv8DCHEQABoMNjM3NDIzMTgzODA1Igw5T%2B0QaYG%2FKUrP5EIq3AMfQIQajvI7rz8K914JmJ3eKShvMmaSe82D%2BxQKu3iKfHZLaSMM%2BBAsFNXXJisXOqeUtcy%2BaRf1Zy4tt%2BFJ5gF%2FKSChFSPSMI50y%2B0uzYQmtrHnx0cmu2WTM7mW4xJKz49WkYifEekJ4AntRl1gcb3HN4dJ1IAN2iEzpS1AWlP0GeBj16D5ZF1r4wjnO%2F0xaEtpljUnnCznWH90G8d5taJ9bgW25VyIIH43jb0FjA6oIjRUaKGFFh9uSaaPuFYmMMsbpppw%2Blw0FBi0GVgCaMIXg18UybQDUxHM3CAZ%2FxHUJwK%2BIfkbxx8ZpO%2FVGVh39UMrZGT7Q5JE67iO%2BEdOStxSq2qscWv0KmzsqkhnnrN8sM6v5%2FyBsmX73mSHVo7jrM2O%2BAdVyK6QzaXpSalRGglFOSnBNrl57spKcqPQxPzDJhdqgHXyzqP0rksGfxhU5IpIgFcyICNheeA1H9We60p%2BET4lHOa8aqQAOpvUZXo0bWzIhoxy75pN4HZzTzqz0AoBaM%2BpB577JMN1JntA7CjyzX1NRVMMiHjypvNlmf8RlwqG58UqRwVhx6P6qthyXum02P7dlTJ9lLv4%2FDcLEGufYaRu8YCFaQ7aVBdqbCzVS8xwqmme6GzydRJcQDDL%2BZa9BjqkAVK0Re9gz064G29LoJRlytIbEgINCyMDHuujmrIMcSJvhkAS%2FKXMtJpgih3tZs1OWgLdWUf9oCUT4AnX%2FwPMGlYLtOO3VcZKV4cM5qV6NnDeT%2FhCbCQIgmB39HeZRV2jRhg8cRQPZU1jQr9YPgVMdSVdCVpiHm4niM0FM2HL2sH40hNekdERIUXTqo8UR4JnpOTUnz1u90%2BzYYsAz2fwSp8y3hMr&X-Amz-Signature=b4fdd9b338f9993cc630a133ffef358d900b39dea83f611631454d9abca3fbd9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QGTPKZD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDpX3md7IzHY5sJx34NrZKd%2F5lBsRmVsofbPpfucW7BkgIhAN7Ukm8U0SfH67%2BkzJAHQaAJyn7r7NFwJeD6jKF93QtvKv8DCHEQABoMNjM3NDIzMTgzODA1Igw5T%2B0QaYG%2FKUrP5EIq3AMfQIQajvI7rz8K914JmJ3eKShvMmaSe82D%2BxQKu3iKfHZLaSMM%2BBAsFNXXJisXOqeUtcy%2BaRf1Zy4tt%2BFJ5gF%2FKSChFSPSMI50y%2B0uzYQmtrHnx0cmu2WTM7mW4xJKz49WkYifEekJ4AntRl1gcb3HN4dJ1IAN2iEzpS1AWlP0GeBj16D5ZF1r4wjnO%2F0xaEtpljUnnCznWH90G8d5taJ9bgW25VyIIH43jb0FjA6oIjRUaKGFFh9uSaaPuFYmMMsbpppw%2Blw0FBi0GVgCaMIXg18UybQDUxHM3CAZ%2FxHUJwK%2BIfkbxx8ZpO%2FVGVh39UMrZGT7Q5JE67iO%2BEdOStxSq2qscWv0KmzsqkhnnrN8sM6v5%2FyBsmX73mSHVo7jrM2O%2BAdVyK6QzaXpSalRGglFOSnBNrl57spKcqPQxPzDJhdqgHXyzqP0rksGfxhU5IpIgFcyICNheeA1H9We60p%2BET4lHOa8aqQAOpvUZXo0bWzIhoxy75pN4HZzTzqz0AoBaM%2BpB577JMN1JntA7CjyzX1NRVMMiHjypvNlmf8RlwqG58UqRwVhx6P6qthyXum02P7dlTJ9lLv4%2FDcLEGufYaRu8YCFaQ7aVBdqbCzVS8xwqmme6GzydRJcQDDL%2BZa9BjqkAVK0Re9gz064G29LoJRlytIbEgINCyMDHuujmrIMcSJvhkAS%2FKXMtJpgih3tZs1OWgLdWUf9oCUT4AnX%2FwPMGlYLtOO3VcZKV4cM5qV6NnDeT%2FhCbCQIgmB39HeZRV2jRhg8cRQPZU1jQr9YPgVMdSVdCVpiHm4niM0FM2HL2sH40hNekdERIUXTqo8UR4JnpOTUnz1u90%2BzYYsAz2fwSp8y3hMr&X-Amz-Signature=76b3a90d8e353ac1565e2740109bb19586b50d31f36b2d5ddd1f75cae8a0af38&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QGTPKZD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDpX3md7IzHY5sJx34NrZKd%2F5lBsRmVsofbPpfucW7BkgIhAN7Ukm8U0SfH67%2BkzJAHQaAJyn7r7NFwJeD6jKF93QtvKv8DCHEQABoMNjM3NDIzMTgzODA1Igw5T%2B0QaYG%2FKUrP5EIq3AMfQIQajvI7rz8K914JmJ3eKShvMmaSe82D%2BxQKu3iKfHZLaSMM%2BBAsFNXXJisXOqeUtcy%2BaRf1Zy4tt%2BFJ5gF%2FKSChFSPSMI50y%2B0uzYQmtrHnx0cmu2WTM7mW4xJKz49WkYifEekJ4AntRl1gcb3HN4dJ1IAN2iEzpS1AWlP0GeBj16D5ZF1r4wjnO%2F0xaEtpljUnnCznWH90G8d5taJ9bgW25VyIIH43jb0FjA6oIjRUaKGFFh9uSaaPuFYmMMsbpppw%2Blw0FBi0GVgCaMIXg18UybQDUxHM3CAZ%2FxHUJwK%2BIfkbxx8ZpO%2FVGVh39UMrZGT7Q5JE67iO%2BEdOStxSq2qscWv0KmzsqkhnnrN8sM6v5%2FyBsmX73mSHVo7jrM2O%2BAdVyK6QzaXpSalRGglFOSnBNrl57spKcqPQxPzDJhdqgHXyzqP0rksGfxhU5IpIgFcyICNheeA1H9We60p%2BET4lHOa8aqQAOpvUZXo0bWzIhoxy75pN4HZzTzqz0AoBaM%2BpB577JMN1JntA7CjyzX1NRVMMiHjypvNlmf8RlwqG58UqRwVhx6P6qthyXum02P7dlTJ9lLv4%2FDcLEGufYaRu8YCFaQ7aVBdqbCzVS8xwqmme6GzydRJcQDDL%2BZa9BjqkAVK0Re9gz064G29LoJRlytIbEgINCyMDHuujmrIMcSJvhkAS%2FKXMtJpgih3tZs1OWgLdWUf9oCUT4AnX%2FwPMGlYLtOO3VcZKV4cM5qV6NnDeT%2FhCbCQIgmB39HeZRV2jRhg8cRQPZU1jQr9YPgVMdSVdCVpiHm4niM0FM2HL2sH40hNekdERIUXTqo8UR4JnpOTUnz1u90%2BzYYsAz2fwSp8y3hMr&X-Amz-Signature=578cdbe4f9ef2bd6207df79e64c29f5bf8c0cb2272b98f3b7ae6d84718769d72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=7535bf63cc9ee08272f70cc3423aa2944f877bad5425ad7ce1a915c6e2e86e8f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=fc109ca42e8a82f52444f795b133d780105fff9deaff1f18cced69ba7dc28b23&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=eb3621356493fb79914d83b9b8c76c1932597ce31f8c15e37a979a53c1a10b5e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=5159908530e329b6b4bdd345602b3c93d475a93732aa0b98a74f4a0665cca6a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=996bd08c948b5ea76a50b87922a765fc6aea7bcbba61db834fce61d33eee0f2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=762fe662f175a8d724d35e21825c088026c764278c71dccf59348a25bbefa6f3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FFBTRI7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCGke7Ec8ACrz%2FxYXAsZMGfUqsVa%2Fp4SjNsI8RLbq1wQwIgWETuKfGOGLEoJUQ4sJI1kWnksiBA4kJSz%2FaSLrGUZ%2Bwq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDv5Awm%2FqXoyFLysESrcA51f%2BtxKGnuMQ9WQZtAX0ZDenzY8KagWsxYkPmokQJDoy%2BUuP%2BWeigdCK3T8p1puKRpPWzYeLRhXupypAzoB1T6Q59rAH5DkgG2OWeku3tjuadx%2B7XOWLBB5frpS1RGfYxpou5OOZ%2FocjwKnAu%2B%2B%2F%2FEU%2BBhJ4BeVkhcjHdsmQaSW2J5gAiFlrrAACVYdfZZUkPbwQ6VHNRNcdC%2FKQff6wM1iOfO7vzfikJK1wHVaNU3ppuEFv%2BhH8946ezTqKqzQSPc6G4TVRVjrVpRV0pWZ%2BwZDmophngPXgW5vwbft3sKstFadtFLEwGUAu9wgqPnwi2f2KWoqQVM7VFqwBWAcGsLWFmHuAvbaGmrlQTFpQERr3mpOuqNIG5P1drBmQVKWeesN1dRD20U2wx0L4U1DCI%2BndSb9i2nAenXHUlN%2BRE%2BKHpJDDGZTr1GC%2BPUQtLFVCfK4UhGDvqGoWzFp4d%2Bvt5tXpSwxJUt1nQ0DNIzkC7UlK0btmikZQ1u2xM%2FPl%2FvmNICkS8aaNbWPoVbRiLBpCA50fyAw289hFnevxJMuDz12%2F03NhoVgzj38ewVTQ8LqHQVDMMicByO6dHKVJ058y44o5dWuYTHL7xKsKnYmB9wiRpthVvarHvGsD7AkMIL6lr0GOqUBxzdlNzp3pNmDFtcwapXWAaPuiXW5mpANb1pxQsGGZ06xDnt0UARM1y%2FrMnIm3uZ9X0hIE1ffZ8tvZ%2FpWu0uwNcLwTgNs%2F8fY2jLipC3iQW8sY0Rodz1%2B6F7d4nTocmffpMpql6%2BD3s16vyefOjt03XuX1AaZ1aew54GrcTr9KWC8rtS1XWqSGfzYQEybPR9Ja4dwUXXGzfDh8QeKfG1fU3RcsnZ7&X-Amz-Signature=8ab4a19197835a73f33edb6eacb2bfa53a01c9d9160fc40a3de5d75354306e13&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5MSUET2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCrvUwISx5wIIes%2FT69sgzobVHk5AVhSX%2F6YF5TvIkmvQIgB4cvA4Y8c5GjUdKcV72QsD0oBDJDEpmPag1ALEPl71Yq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDIYhRl6uzYC%2BlFyF8CrcAzUyLzr3xEHFgHe8E3yylMPtQYL6KyhoqBW5rNiGVyxR3XdqCIkVL%2FXtpqT8xzQXPTL4FEi%2BxEgAjt4QPtnlOMw3XxX4TProJl90XdcLt5X9ct3tD2VSYIA2Ohm%2FlCwnnJ%2FiP%2BilsI49pSJToq5Go9Ts1ZZCeJiDpy4ugXwCrnS7fGod3P4fFBbE8VQHYH1p%2FIHCAi%2B8DCLeAhYXGmcu%2FTJGHfBRO58NhR0zwFyOTxasVEcyJ0Lq9UAh9SJ1rf%2Feeb%2FwVq4vsrFRu0Ug%2BDTRfCplGeYfb2NBJlK5vbbr%2FAgSic8pRIJBTp5Rt1TgUrzCIlla0OTMxfVwQzIDXyMYfEt%2B7HVCEEr8ipUqWTRV8g6bPglBUDhU5LOhQtLXhiXg72YebWZb5bm97HdeIgnyLj0%2BX%2FeGBd3KHnL801EBbyrGZheEw86h8fGZltlWxoDnvnHnOedTHCeL0QjjmhcdurMmFafEiF2mSB1qwEHqQPEXkaVJ%2BTn0ko9wZFcSlWrYUuk5vVqctoMlZgTjjCvwmDM7AjF6olSS54yHesgtQ7l6VufBKiByR0czdewAenlDigBNhbApqUEeZJUiKgQeWGI04nl9BOQlAoe039BaP3zybG%2BE69WR%2Fp7AusdeMMD5lr0GOqUBl962tgmKHhHwFEOti2yQnargV7YzvECoCJi8Fw4QJlBBqs77IuJb1uxcNA9gto6WvNEUAGZq4IkEYHJwWOKdKUmK5HNM40W0wzH7v0BTzzZzwL1oXuJqESxeamM1W8Cw%2BLUOWixTEIoAoRPYBflpShofQZl82ROBnPxAzlLc05X2eAwYvFqu38hfCJlAXagv9kcUJS%2FCI2s8AJKwBXw2Q1pRTOIG&X-Amz-Signature=6e2d663a5185dce74487a1d3f12e8c2a5de648eec02137b126247167ed82da3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=d3f783fa023de1a0463437f91613f335e63ed89193b28e70ecea9c07dcc0a887&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=b1b060de0b84808ae366f08b5ea9932ef6e7c66f1c4da7f9e26ff8fa391f26a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=23e1b6d28b92979e2aa5ade724796798e91bf566d97c3c5c4337c93d2ac8b0bd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2N3NO7Q%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICq0RUEYBpIhfCT3%2F8ficKU%2B0eebKeTEoTgqHZWpa7h%2BAiEAnQfXSiZP9kaJ041haBQa1G0SHrRvab6BaLAJoX14JD8q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNsPA6eQSmJJQ4gv7yrcA%2BHxoRyEi4zliNeQyVhoGjSsA0Ga9ZI37EDW%2FsB7uUWSWq7KZXU30vx7bZsJ25xRBpk5%2Bi3RNERvSTOvqMTcmmSjS%2B7FWbeQvZr4rLS2RM%2BlJrvKYz6fGxDq%2BJhr4DKB%2BpZaTRrIM50WP5wuZyd%2FmMEBb8ihFN7Ov3YQgrpabny8aywbgCrWo7zPdz8INg5AELMN10JbJGBkEmCezmNupAZbiLr%2BYv1hpNXw5KtdBo4qfW%2FXeA5GVE%2FV8xTfJSh7e3snW%2FiNuwe3b%2FqyG2mkbXgNYfoS53wSzh7RLL%2B2SQxej8iAgHITyk9WfZ6nXnNpiU%2FpBjRSAE1BYRUaCOIFSP5fgmtvS4Mfwk7oq2u4cRaIv6sERjoslP4emkviqAAgwoxrpUrVeEORZ88HvaU6PwO2JWQr%2FtoOvYlyU%2FcFrDeZ4QPHtk56mhZ8hul3vx9f%2FGD2NNgdOW8SmSp82HX4cpfI5jwBmaU%2Bylz4MtFFSaZj0d3Uttr4auQbk%2BAlDWKrOAnJoyhbGuhk%2BOfGO57cmR77hPl6T%2F2xgNVtXDlrEJrSjNyxqOVipvh85CWzEFRxu45Xk3lAydraOzM030HsqxTPz2CHbIfHOoOJq6HXWGzcUcTszOlx2B%2BJ8sz0MNX5lr0GOqUB1nWPG5N3mLcwCsyOlY5uL8xrkgwUeKTfzkSpS8ZfzwrA%2B3UDT87zQYtSEoGuJxusZNnj3BznkU3pTxeNvwv1TivwlPTnEgHHhwVCZSPkIorVi4XTX4SvUI6EootBGA%2BQRgSmCkTWHf2kwV%2Buz%2FIaqbHx%2FyWLW7I5v5y%2BymPAYmDZFHwyKvL3l9NWgeknWM39D72Wnu7HkbMROJ7%2FVPYLxs%2Bmw6pY&X-Amz-Signature=4ce98c6b3def9886474064f5e50a7411028b257d14acd70de1fe2ae2b170ee21&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOVKREIP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIFJI2XKonT%2BsyfaXD91zKmNFqJ4v9D3OSONTIux1AnhZAiBDvTO1jLZWUUs%2FPstb9TK57y81NlNEszJQIvlKuha3byr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM8pqzXe1mrk%2FnHP%2FXKtwDBu80F83TK6gRDOpaGfnRKlAfuY8sfbJya9HYu29GlLxZd4Nsamacgu220OYPE%2BuIlU1%2FMomNFBt2KnVZ5Q6nTYExqyne90rziiFJO63UvBbQMiyWpKrby%2BqKYCzOX6kvO7TomgXLzRWsHded14aO70abvaesdZ%2BNH5orH211VIh4I5IVkXk9GHs64ww%2Fz741N%2BioyM6b19d2fPvEtd28Tqj46JCkJNWfPXVC%2BsPk3hiTE1bElNevd7A%2FxhQNgpz%2BDvEwqGmNoCQUZ72o85fMiTs3N%2B6jdCsIXhN%2FePoGPjPSnA8M%2BiMuZ7FQoGOi54kSC5T311BR%2BBoKaVod3Qz91Z8F0Eik7bzXviRPGqdwI0i2SFLmZ%2BglLWi3%2FI302jqepQXluBSfqz%2BZpIOzzCQ8YGvVbmuxakKkT9qV6lM4N43IwbSKP1YsZyBXSZiMeR3AIObD70Yw25ZuNglZy23Ep7LeZz1WW%2F%2BEutl%2FV2w3jDczthytuwLD51JgqQ7FjVWkHs3HPbF8gCpdPpmVzbnDHJSRbNwQTu2Eei8Qxui8AXsRfeTWpoEgDlOd1vrW575JeD%2Brrfv9A0aXKonw7VVIiRp3jdEtc%2BTcYLfgGjP2iboLrIX1psq%2BTnjE0VEwnPqWvQY6pgHbdgtkjJV9YcYtZXVgyaulslkw2ZxBt8Vn1IkrAvHPSja2YvggtTiYF9JCod1KYM1O23FrDreO4JrALVWKPd6YsfnHlRjmTysQE78rzcy6%2FQr7uZ%2B67YMU09lxIqK1BkYThcdYKVJ9pitITX6%2FVYf%2BAMgchUuvHhOWxHIIXmNJppOUp%2BmWIe7NOzT5p1nwpCMt1lyN5Kmy94A8PI3%2BIh%2FTRtTGl5mj&X-Amz-Signature=d147f95021117b43234875fdd759e82bb2003fc521ee3b187978a54d5473e437&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S73E2HME%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQD%2BSGUQ%2BKPWNa%2B89ZITB6PWyxJo3uBy9FWQ1DbYSRJdjAIhANhaZrcUMs8lnWI3Cdzd0cQXIf8J2dFokcjLzCyZjWWVKv8DCHEQABoMNjM3NDIzMTgzODA1IgyJkRwmCp9KKTi2wnYq3ANUga%2B6eVu6lfTDt%2FMV%2BSDQARXGw379NHaEBG5EGUrbRknvVJVy1tlU9sHm0sk5ZTAu7fAeXPwmift%2BTV7REtfR%2FkX4S%2BPrrv3Xi2%2B708m9g1qhubQjselAqZMIkRW15CAArgbShOyGMqDr%2B%2BouZAo8uI0O3nzVmlXGp3Ldgje4bFqjSfv4m4jqWRzfNW%2FV3niu5obAKBaft8ldW53L2FpMRGRlthCjICIJj6hLMZi6wf6y%2FM2ZooUvcbvjXTTRAsKjIeburZqTymFAI%2BXoS%2FW30fygpsR6C9wi1DujVNN06%2BbEQRPZm3birkcYYJLKh81jDnpRzfXmQ0bd%2Bap6YknQhzyruYAXQeDquSXPB3MDAJegPMqvhpOxD8TVbu48twonwk7A1A2f%2BNbM%2FDb7sMFkg1cRupPv%2BjAQhq7r7q1qZjjPf12HP%2B0zL%2Fm8M%2FoUakaMgiCXuGzPH8W6NISizGqloOs1iqBHHTo7JXA5eibvz4ZOwmbiwRtPxqMrsAJ0BkjCGQDKTvOW4%2B1XbhfGEI6moq1oMqiIlepA9u7IEHLeSf0iRbz%2FGSvT3sDwWU0rvPDP2IZfDtNHYa0ERWhv%2BeTNUtRoqpPWHPbtNS5Y0Met7OY31Uh9LvUxUoCiODCB%2Bpa9BjqkAWunvyvydQ28IEHNUnOvm%2FcQcfcNksUFM6GwPWSMsh7xNDRbaj3WPkWwy5DFIL%2BWihkuErJasLVqQWGH1rWELuJSsRJ4t9Vrza4IwvsioW2NkBy%2BWh4QO3gwACg%2FUWAqXnXSw%2FknNjchZGGY8tRw4CosIfte7SOfAnmXGXKmhcKPzzUKazXKGo4dFfUbVGQsACKSywUIqSbAYz9izSaHjdokPhdM&X-Amz-Signature=1c169a069ed30416fb30a78601e74866157ecc0e9cd8ba41138a72efc909934a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSXSOHM2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIDosx7pvflJUjqQeJsVhJjRnkk5kQiwogWWtIW0VH2rIAiEAv%2FS8okwU%2BJUsVItmPmV9Acacapwazi%2FrJoL52Oc4%2F%2F0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNHCy%2FD%2FP2LOAQihYCrcA%2B%2Fi0rZsYNO4JHDkc9AWkzanej6K2HPvZmA7BcESpSTiPFl5NjddcTHYQBXlsWFzXE2I%2BskQp6PD0r8qpksvqQbRTsOKfeTgNQw79%2BJTxL5rUfl4Dss4VOqKRa%2FseVHGaJBeCvdCf3EGyjqKwVtvpiQkERppRKvdAE2agtJwVQE8vKI9se98o0iuqk%2FJ4kh%2FUm6D6OkcqyV8HGif8%2BtFHcADiCS3%2B9I0FQmAK74M1fr%2Bjf6KdEVq%2F9hhrY2tGxK3GPa3Je8GrjZ%2F1jco1DEmqllkzKkvt6zbGVlaPAJphHQv7CuU9l2a8yAtbo77GlyNO5olRa%2BAUMMaJQlnfVRSx4k6sKq6QhGPi4A%2BxmLMu%2FZYdlUfON993Fp6%2FZPJ%2FY6w6megzNQTGCrDbLwybC7pobEZ8GTt%2FwOAUhfYw9nwSyYTrQRc6FoZnEO08a0os%2F4wt77wgwrm%2BHaVfFpNJQwYQADe3zVSdOo9HUGccynLt603Nt%2FEEFeL9VOZpOBA%2BZeMhNRsXeA1DvzrnuPROp33wtJ58SJvmuS6zHV9fMdbb%2B9GXazLz4X86vQuuk%2B4aIaATeX0oSbD8QlUBMi3St9lHPnly45OvB5zz0TALdbs%2B4qIXDRs1dbistPcs1zjMJL6lr0GOqUBYreSGiQPgZR2MeN3k%2FA1gtbJj4fM2%2BcvOvazymVjwJ1f%2FkYOEtyv1pVzTiLPFVgqohPjqPSTGoR4y6XvKjPZxDN8rh3wFkI0e1EH%2B3CCak7miEhJ2SoFEheM4wwfSjc2TTLwSS5S4Ov9MVt2vNhwfWJzqHBQFZpsERbHn%2BXXb9Rtef66SylDDDhMdn8lTws6JihCb9JbftIOi%2Frjxt4T0GHPavd5&X-Amz-Signature=109d871f30cf999ef3c845fb32865f84b9e3066d371b934b03872f89f60ca175&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSXSOHM2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIDosx7pvflJUjqQeJsVhJjRnkk5kQiwogWWtIW0VH2rIAiEAv%2FS8okwU%2BJUsVItmPmV9Acacapwazi%2FrJoL52Oc4%2F%2F0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNHCy%2FD%2FP2LOAQihYCrcA%2B%2Fi0rZsYNO4JHDkc9AWkzanej6K2HPvZmA7BcESpSTiPFl5NjddcTHYQBXlsWFzXE2I%2BskQp6PD0r8qpksvqQbRTsOKfeTgNQw79%2BJTxL5rUfl4Dss4VOqKRa%2FseVHGaJBeCvdCf3EGyjqKwVtvpiQkERppRKvdAE2agtJwVQE8vKI9se98o0iuqk%2FJ4kh%2FUm6D6OkcqyV8HGif8%2BtFHcADiCS3%2B9I0FQmAK74M1fr%2Bjf6KdEVq%2F9hhrY2tGxK3GPa3Je8GrjZ%2F1jco1DEmqllkzKkvt6zbGVlaPAJphHQv7CuU9l2a8yAtbo77GlyNO5olRa%2BAUMMaJQlnfVRSx4k6sKq6QhGPi4A%2BxmLMu%2FZYdlUfON993Fp6%2FZPJ%2FY6w6megzNQTGCrDbLwybC7pobEZ8GTt%2FwOAUhfYw9nwSyYTrQRc6FoZnEO08a0os%2F4wt77wgwrm%2BHaVfFpNJQwYQADe3zVSdOo9HUGccynLt603Nt%2FEEFeL9VOZpOBA%2BZeMhNRsXeA1DvzrnuPROp33wtJ58SJvmuS6zHV9fMdbb%2B9GXazLz4X86vQuuk%2B4aIaATeX0oSbD8QlUBMi3St9lHPnly45OvB5zz0TALdbs%2B4qIXDRs1dbistPcs1zjMJL6lr0GOqUBYreSGiQPgZR2MeN3k%2FA1gtbJj4fM2%2BcvOvazymVjwJ1f%2FkYOEtyv1pVzTiLPFVgqohPjqPSTGoR4y6XvKjPZxDN8rh3wFkI0e1EH%2B3CCak7miEhJ2SoFEheM4wwfSjc2TTLwSS5S4Ov9MVt2vNhwfWJzqHBQFZpsERbHn%2BXXb9Rtef66SylDDDhMdn8lTws6JihCb9JbftIOi%2Frjxt4T0GHPavd5&X-Amz-Signature=a1b1e325c51e1b0ad9626118945b79d9ab6e57a9cb19407f3d0c66ba995ea40d&X-Amz-SignedHeaders=host&x-id=GetObject)

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
