

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AL4NJGS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYDPXc7H7xCeOWjPuyh6vWEST8mnva23S3VJJksA%2F2OAIhAPfjc7kSIPvG1CMgCPs9bjUo8uKqGWFO3ks9%2BIBTwaMRKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKkGxVm8SJSE5wpGIq3AM%2B%2BOXxq1tEMK4sLcc3C1ycOFujUOsr0reiOryjd2CC4Z%2B5pJ6oR%2BGyhLf6hUtrzLfIY0T0oas%2BOfToscFg4njaLMQZY1TZMjlUdbjA0ko1RB775dDcJtHboPqQUlo5W54B1ZLRcJJA%2FdukjP6RHVGsLP1TLQItpC2nKrGi9gkFXTflisNrknnq0m6%2BUlyJenBprw99HcXtZRaQZrUmwJaczoUMldC2n4jJlhTOvYqckIbK%2BnLSWzmooEKD2Uoq3b7y%2Fm2WtZ%2BvTqE5lnUn6VdrPhas6ntpjXdXF6cyNAX51HpqJDbS5CeArHh2nY3O1oVhXU0DYUuxfQ7wvXtFUChEZS5gdCnbDLh10RZD0YRH5jZl7cHzihJfRWk6tDJIGIBKSlYCMoKR%2BlLp5Y4gNUKJ61FRmk6Uh5vgoLLU94kNqVTYLPAyD6mKxBC2O8ACvuRJm6Q7G5hFiKTpt7kZenmRUB%2FcmbJ2Ls4yofhp5%2FHum5lpUOyNvzDSn7m4VAMy3qZgMgo1ABcAxi7N%2FP9RRe32yu7%2BiSYEvclUQf2Tq9tvgMmnfZLoWuBFAH%2BhG70n4u1IqZYczhTW%2FwGgMFeg4h9K4PaCLjcWTXKN%2Ft2KVBMkE2e8KLTwBj6theQoeDC76%2By8BjqkAQc1aiQX9xuax68C4PKmd%2FxKHErrSH1oI72JmvAe0MuCutUgRBbDIGYsSpDxTrfKDz65jd0mmpgRWXme3jsqqxOY6idt6htkwR7DTwGAwsTUdfBd%2BmU%2FlMf466KktRZCkxsepwvdTWn%2BNaltGyzchoSaMj10KhQ%2FiSjqry0CWMIlywuUb6wzSYNDIUufmJq3wTIKNm5cox7F8OefQcIEeJursKFd&X-Amz-Signature=3064e602180f78adf92f24568183a7263d95d75d6460eeda8efcde3fa926cd86&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AL4NJGS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYDPXc7H7xCeOWjPuyh6vWEST8mnva23S3VJJksA%2F2OAIhAPfjc7kSIPvG1CMgCPs9bjUo8uKqGWFO3ks9%2BIBTwaMRKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKkGxVm8SJSE5wpGIq3AM%2B%2BOXxq1tEMK4sLcc3C1ycOFujUOsr0reiOryjd2CC4Z%2B5pJ6oR%2BGyhLf6hUtrzLfIY0T0oas%2BOfToscFg4njaLMQZY1TZMjlUdbjA0ko1RB775dDcJtHboPqQUlo5W54B1ZLRcJJA%2FdukjP6RHVGsLP1TLQItpC2nKrGi9gkFXTflisNrknnq0m6%2BUlyJenBprw99HcXtZRaQZrUmwJaczoUMldC2n4jJlhTOvYqckIbK%2BnLSWzmooEKD2Uoq3b7y%2Fm2WtZ%2BvTqE5lnUn6VdrPhas6ntpjXdXF6cyNAX51HpqJDbS5CeArHh2nY3O1oVhXU0DYUuxfQ7wvXtFUChEZS5gdCnbDLh10RZD0YRH5jZl7cHzihJfRWk6tDJIGIBKSlYCMoKR%2BlLp5Y4gNUKJ61FRmk6Uh5vgoLLU94kNqVTYLPAyD6mKxBC2O8ACvuRJm6Q7G5hFiKTpt7kZenmRUB%2FcmbJ2Ls4yofhp5%2FHum5lpUOyNvzDSn7m4VAMy3qZgMgo1ABcAxi7N%2FP9RRe32yu7%2BiSYEvclUQf2Tq9tvgMmnfZLoWuBFAH%2BhG70n4u1IqZYczhTW%2FwGgMFeg4h9K4PaCLjcWTXKN%2Ft2KVBMkE2e8KLTwBj6theQoeDC76%2By8BjqkAQc1aiQX9xuax68C4PKmd%2FxKHErrSH1oI72JmvAe0MuCutUgRBbDIGYsSpDxTrfKDz65jd0mmpgRWXme3jsqqxOY6idt6htkwR7DTwGAwsTUdfBd%2BmU%2FlMf466KktRZCkxsepwvdTWn%2BNaltGyzchoSaMj10KhQ%2FiSjqry0CWMIlywuUb6wzSYNDIUufmJq3wTIKNm5cox7F8OefQcIEeJursKFd&X-Amz-Signature=12f1cec8f8dc602b84e2bfa7264b533dd1cfec797afbe1e5c44269443e3001c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AL4NJGS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYDPXc7H7xCeOWjPuyh6vWEST8mnva23S3VJJksA%2F2OAIhAPfjc7kSIPvG1CMgCPs9bjUo8uKqGWFO3ks9%2BIBTwaMRKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKkGxVm8SJSE5wpGIq3AM%2B%2BOXxq1tEMK4sLcc3C1ycOFujUOsr0reiOryjd2CC4Z%2B5pJ6oR%2BGyhLf6hUtrzLfIY0T0oas%2BOfToscFg4njaLMQZY1TZMjlUdbjA0ko1RB775dDcJtHboPqQUlo5W54B1ZLRcJJA%2FdukjP6RHVGsLP1TLQItpC2nKrGi9gkFXTflisNrknnq0m6%2BUlyJenBprw99HcXtZRaQZrUmwJaczoUMldC2n4jJlhTOvYqckIbK%2BnLSWzmooEKD2Uoq3b7y%2Fm2WtZ%2BvTqE5lnUn6VdrPhas6ntpjXdXF6cyNAX51HpqJDbS5CeArHh2nY3O1oVhXU0DYUuxfQ7wvXtFUChEZS5gdCnbDLh10RZD0YRH5jZl7cHzihJfRWk6tDJIGIBKSlYCMoKR%2BlLp5Y4gNUKJ61FRmk6Uh5vgoLLU94kNqVTYLPAyD6mKxBC2O8ACvuRJm6Q7G5hFiKTpt7kZenmRUB%2FcmbJ2Ls4yofhp5%2FHum5lpUOyNvzDSn7m4VAMy3qZgMgo1ABcAxi7N%2FP9RRe32yu7%2BiSYEvclUQf2Tq9tvgMmnfZLoWuBFAH%2BhG70n4u1IqZYczhTW%2FwGgMFeg4h9K4PaCLjcWTXKN%2Ft2KVBMkE2e8KLTwBj6theQoeDC76%2By8BjqkAQc1aiQX9xuax68C4PKmd%2FxKHErrSH1oI72JmvAe0MuCutUgRBbDIGYsSpDxTrfKDz65jd0mmpgRWXme3jsqqxOY6idt6htkwR7DTwGAwsTUdfBd%2BmU%2FlMf466KktRZCkxsepwvdTWn%2BNaltGyzchoSaMj10KhQ%2FiSjqry0CWMIlywuUb6wzSYNDIUufmJq3wTIKNm5cox7F8OefQcIEeJursKFd&X-Amz-Signature=371a27bb0acc175c42daa36906be0865ba600799572fbb7f4ff16ecae741b451&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYNQ4N6L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGLU7wCu5N4mPBBszoMwPH07eMYrtti%2Bx4aY%2Fs1%2B%2FoT1AiBRmIvVrW%2B6M6wIdUnkkYwKzG9adLaJrW3x9psnoiuNsiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFRm3EbTrrg%2B6abtDKtwDO9sIvM2XUi6hgGoByhLDlhGyxPmua9y%2FzXvJVI7o7VJpGEvOYO4p9oHMzkB5juBVRzE%2FJOY7MOXHdurFirZYsQ8IVE2qH%2FwXuewiVqw35v6k%2BBDVFUqnf6cwLExi85FMfJmVVghDXBN%2BNWqE2l7MyjKo2L4XjGkzpmFZlLWycbP9TpiESeHhvYV8Ru0ggiOnssEj7q0jffG1pQrfl4WSXwQwL7KMugJOsbXBGliZMu3%2F95Lvmrj%2Fwh4dQ2WQ5WRFXsq%2BYwO%2BpMoXgfrL6COjie8uLG3J49R2kWkq1%2BxFiHsK2L%2FYbMwC4A03WnmylKPaOWbRzGGgjd%2FZd3Es8MDtV51fKua0FYiq7YV3EA9AJrdnril6LEEVeQ6W21kxqPE7r0TH1bSj8O8lmlEKVDjcQo4fxKZSXNsgeILR2ZFDZt64JKi6%2B3vdq1kADLoyvCphllD3fesrKTjIjvJfud0hxEicZoqAdkccLlqSNeDtg8adceHz1VCEzrb%2B40WpPMbLQXIxmcWwMJSdhHzS9IPty2me4Hbu1YmgxMBEzz0iOD99dp0jahHPDq87X%2B0mf4NmzabLKvMEuL%2F%2FmHmi3cI1S%2B384gwmKZ4ZO9fC8PWT3OFWweHRDX9eMowUbqsw1%2BvsvAY6pgEfLejNmmAtVWD6zRPxEw5NbsuaxKizbdxjVeqZe%2FxT0GvFEdSRXx19211fKaDqirzYXvsF%2FkH9luR0sEkKEvZIwzMFV8NQTF5IF%2FbBpFjrzUs6FGGaO5Lllx9fYnBudcq%2F%2FEI8kmT3Iu%2FbRDKBgp%2FIpGjtSC7O9aGPLvMiVv7lPTuDvgtq4jONX8AdmkY7sAJYJxHdi5XXTp7Ry65gDCxQZYfnY%2FQq&X-Amz-Signature=fe549603cdc8c81307f1207992e2ff7bb542979396fe3683806731074b9a77f2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYNQ4N6L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGLU7wCu5N4mPBBszoMwPH07eMYrtti%2Bx4aY%2Fs1%2B%2FoT1AiBRmIvVrW%2B6M6wIdUnkkYwKzG9adLaJrW3x9psnoiuNsiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFRm3EbTrrg%2B6abtDKtwDO9sIvM2XUi6hgGoByhLDlhGyxPmua9y%2FzXvJVI7o7VJpGEvOYO4p9oHMzkB5juBVRzE%2FJOY7MOXHdurFirZYsQ8IVE2qH%2FwXuewiVqw35v6k%2BBDVFUqnf6cwLExi85FMfJmVVghDXBN%2BNWqE2l7MyjKo2L4XjGkzpmFZlLWycbP9TpiESeHhvYV8Ru0ggiOnssEj7q0jffG1pQrfl4WSXwQwL7KMugJOsbXBGliZMu3%2F95Lvmrj%2Fwh4dQ2WQ5WRFXsq%2BYwO%2BpMoXgfrL6COjie8uLG3J49R2kWkq1%2BxFiHsK2L%2FYbMwC4A03WnmylKPaOWbRzGGgjd%2FZd3Es8MDtV51fKua0FYiq7YV3EA9AJrdnril6LEEVeQ6W21kxqPE7r0TH1bSj8O8lmlEKVDjcQo4fxKZSXNsgeILR2ZFDZt64JKi6%2B3vdq1kADLoyvCphllD3fesrKTjIjvJfud0hxEicZoqAdkccLlqSNeDtg8adceHz1VCEzrb%2B40WpPMbLQXIxmcWwMJSdhHzS9IPty2me4Hbu1YmgxMBEzz0iOD99dp0jahHPDq87X%2B0mf4NmzabLKvMEuL%2F%2FmHmi3cI1S%2B384gwmKZ4ZO9fC8PWT3OFWweHRDX9eMowUbqsw1%2BvsvAY6pgEfLejNmmAtVWD6zRPxEw5NbsuaxKizbdxjVeqZe%2FxT0GvFEdSRXx19211fKaDqirzYXvsF%2FkH9luR0sEkKEvZIwzMFV8NQTF5IF%2FbBpFjrzUs6FGGaO5Lllx9fYnBudcq%2F%2FEI8kmT3Iu%2FbRDKBgp%2FIpGjtSC7O9aGPLvMiVv7lPTuDvgtq4jONX8AdmkY7sAJYJxHdi5XXTp7Ry65gDCxQZYfnY%2FQq&X-Amz-Signature=c3b2d24336e7682d68c51bdd1a332d5cd9fea103fc9fc113909e6f0865259416&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYNQ4N6L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGLU7wCu5N4mPBBszoMwPH07eMYrtti%2Bx4aY%2Fs1%2B%2FoT1AiBRmIvVrW%2B6M6wIdUnkkYwKzG9adLaJrW3x9psnoiuNsiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFRm3EbTrrg%2B6abtDKtwDO9sIvM2XUi6hgGoByhLDlhGyxPmua9y%2FzXvJVI7o7VJpGEvOYO4p9oHMzkB5juBVRzE%2FJOY7MOXHdurFirZYsQ8IVE2qH%2FwXuewiVqw35v6k%2BBDVFUqnf6cwLExi85FMfJmVVghDXBN%2BNWqE2l7MyjKo2L4XjGkzpmFZlLWycbP9TpiESeHhvYV8Ru0ggiOnssEj7q0jffG1pQrfl4WSXwQwL7KMugJOsbXBGliZMu3%2F95Lvmrj%2Fwh4dQ2WQ5WRFXsq%2BYwO%2BpMoXgfrL6COjie8uLG3J49R2kWkq1%2BxFiHsK2L%2FYbMwC4A03WnmylKPaOWbRzGGgjd%2FZd3Es8MDtV51fKua0FYiq7YV3EA9AJrdnril6LEEVeQ6W21kxqPE7r0TH1bSj8O8lmlEKVDjcQo4fxKZSXNsgeILR2ZFDZt64JKi6%2B3vdq1kADLoyvCphllD3fesrKTjIjvJfud0hxEicZoqAdkccLlqSNeDtg8adceHz1VCEzrb%2B40WpPMbLQXIxmcWwMJSdhHzS9IPty2me4Hbu1YmgxMBEzz0iOD99dp0jahHPDq87X%2B0mf4NmzabLKvMEuL%2F%2FmHmi3cI1S%2B384gwmKZ4ZO9fC8PWT3OFWweHRDX9eMowUbqsw1%2BvsvAY6pgEfLejNmmAtVWD6zRPxEw5NbsuaxKizbdxjVeqZe%2FxT0GvFEdSRXx19211fKaDqirzYXvsF%2FkH9luR0sEkKEvZIwzMFV8NQTF5IF%2FbBpFjrzUs6FGGaO5Lllx9fYnBudcq%2F%2FEI8kmT3Iu%2FbRDKBgp%2FIpGjtSC7O9aGPLvMiVv7lPTuDvgtq4jONX8AdmkY7sAJYJxHdi5XXTp7Ry65gDCxQZYfnY%2FQq&X-Amz-Signature=d853eb5f5e9bb510c5d76353a5ae612ee0f037424d187c6fb4ebc84253659561&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYNQ4N6L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGLU7wCu5N4mPBBszoMwPH07eMYrtti%2Bx4aY%2Fs1%2B%2FoT1AiBRmIvVrW%2B6M6wIdUnkkYwKzG9adLaJrW3x9psnoiuNsiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFRm3EbTrrg%2B6abtDKtwDO9sIvM2XUi6hgGoByhLDlhGyxPmua9y%2FzXvJVI7o7VJpGEvOYO4p9oHMzkB5juBVRzE%2FJOY7MOXHdurFirZYsQ8IVE2qH%2FwXuewiVqw35v6k%2BBDVFUqnf6cwLExi85FMfJmVVghDXBN%2BNWqE2l7MyjKo2L4XjGkzpmFZlLWycbP9TpiESeHhvYV8Ru0ggiOnssEj7q0jffG1pQrfl4WSXwQwL7KMugJOsbXBGliZMu3%2F95Lvmrj%2Fwh4dQ2WQ5WRFXsq%2BYwO%2BpMoXgfrL6COjie8uLG3J49R2kWkq1%2BxFiHsK2L%2FYbMwC4A03WnmylKPaOWbRzGGgjd%2FZd3Es8MDtV51fKua0FYiq7YV3EA9AJrdnril6LEEVeQ6W21kxqPE7r0TH1bSj8O8lmlEKVDjcQo4fxKZSXNsgeILR2ZFDZt64JKi6%2B3vdq1kADLoyvCphllD3fesrKTjIjvJfud0hxEicZoqAdkccLlqSNeDtg8adceHz1VCEzrb%2B40WpPMbLQXIxmcWwMJSdhHzS9IPty2me4Hbu1YmgxMBEzz0iOD99dp0jahHPDq87X%2B0mf4NmzabLKvMEuL%2F%2FmHmi3cI1S%2B384gwmKZ4ZO9fC8PWT3OFWweHRDX9eMowUbqsw1%2BvsvAY6pgEfLejNmmAtVWD6zRPxEw5NbsuaxKizbdxjVeqZe%2FxT0GvFEdSRXx19211fKaDqirzYXvsF%2FkH9luR0sEkKEvZIwzMFV8NQTF5IF%2FbBpFjrzUs6FGGaO5Lllx9fYnBudcq%2F%2FEI8kmT3Iu%2FbRDKBgp%2FIpGjtSC7O9aGPLvMiVv7lPTuDvgtq4jONX8AdmkY7sAJYJxHdi5XXTp7Ry65gDCxQZYfnY%2FQq&X-Amz-Signature=999f42a29aaf15acc93982da9ffe11c2873076738d56b2cf16be3a881b2e3b46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYNQ4N6L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGLU7wCu5N4mPBBszoMwPH07eMYrtti%2Bx4aY%2Fs1%2B%2FoT1AiBRmIvVrW%2B6M6wIdUnkkYwKzG9adLaJrW3x9psnoiuNsiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFRm3EbTrrg%2B6abtDKtwDO9sIvM2XUi6hgGoByhLDlhGyxPmua9y%2FzXvJVI7o7VJpGEvOYO4p9oHMzkB5juBVRzE%2FJOY7MOXHdurFirZYsQ8IVE2qH%2FwXuewiVqw35v6k%2BBDVFUqnf6cwLExi85FMfJmVVghDXBN%2BNWqE2l7MyjKo2L4XjGkzpmFZlLWycbP9TpiESeHhvYV8Ru0ggiOnssEj7q0jffG1pQrfl4WSXwQwL7KMugJOsbXBGliZMu3%2F95Lvmrj%2Fwh4dQ2WQ5WRFXsq%2BYwO%2BpMoXgfrL6COjie8uLG3J49R2kWkq1%2BxFiHsK2L%2FYbMwC4A03WnmylKPaOWbRzGGgjd%2FZd3Es8MDtV51fKua0FYiq7YV3EA9AJrdnril6LEEVeQ6W21kxqPE7r0TH1bSj8O8lmlEKVDjcQo4fxKZSXNsgeILR2ZFDZt64JKi6%2B3vdq1kADLoyvCphllD3fesrKTjIjvJfud0hxEicZoqAdkccLlqSNeDtg8adceHz1VCEzrb%2B40WpPMbLQXIxmcWwMJSdhHzS9IPty2me4Hbu1YmgxMBEzz0iOD99dp0jahHPDq87X%2B0mf4NmzabLKvMEuL%2F%2FmHmi3cI1S%2B384gwmKZ4ZO9fC8PWT3OFWweHRDX9eMowUbqsw1%2BvsvAY6pgEfLejNmmAtVWD6zRPxEw5NbsuaxKizbdxjVeqZe%2FxT0GvFEdSRXx19211fKaDqirzYXvsF%2FkH9luR0sEkKEvZIwzMFV8NQTF5IF%2FbBpFjrzUs6FGGaO5Lllx9fYnBudcq%2F%2FEI8kmT3Iu%2FbRDKBgp%2FIpGjtSC7O9aGPLvMiVv7lPTuDvgtq4jONX8AdmkY7sAJYJxHdi5XXTp7Ry65gDCxQZYfnY%2FQq&X-Amz-Signature=c3a613ca6dc4190dd3ac4135ba08504408aaf675ce9f6d29ca0c23dc4c22df50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYNQ4N6L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGLU7wCu5N4mPBBszoMwPH07eMYrtti%2Bx4aY%2Fs1%2B%2FoT1AiBRmIvVrW%2B6M6wIdUnkkYwKzG9adLaJrW3x9psnoiuNsiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFRm3EbTrrg%2B6abtDKtwDO9sIvM2XUi6hgGoByhLDlhGyxPmua9y%2FzXvJVI7o7VJpGEvOYO4p9oHMzkB5juBVRzE%2FJOY7MOXHdurFirZYsQ8IVE2qH%2FwXuewiVqw35v6k%2BBDVFUqnf6cwLExi85FMfJmVVghDXBN%2BNWqE2l7MyjKo2L4XjGkzpmFZlLWycbP9TpiESeHhvYV8Ru0ggiOnssEj7q0jffG1pQrfl4WSXwQwL7KMugJOsbXBGliZMu3%2F95Lvmrj%2Fwh4dQ2WQ5WRFXsq%2BYwO%2BpMoXgfrL6COjie8uLG3J49R2kWkq1%2BxFiHsK2L%2FYbMwC4A03WnmylKPaOWbRzGGgjd%2FZd3Es8MDtV51fKua0FYiq7YV3EA9AJrdnril6LEEVeQ6W21kxqPE7r0TH1bSj8O8lmlEKVDjcQo4fxKZSXNsgeILR2ZFDZt64JKi6%2B3vdq1kADLoyvCphllD3fesrKTjIjvJfud0hxEicZoqAdkccLlqSNeDtg8adceHz1VCEzrb%2B40WpPMbLQXIxmcWwMJSdhHzS9IPty2me4Hbu1YmgxMBEzz0iOD99dp0jahHPDq87X%2B0mf4NmzabLKvMEuL%2F%2FmHmi3cI1S%2B384gwmKZ4ZO9fC8PWT3OFWweHRDX9eMowUbqsw1%2BvsvAY6pgEfLejNmmAtVWD6zRPxEw5NbsuaxKizbdxjVeqZe%2FxT0GvFEdSRXx19211fKaDqirzYXvsF%2FkH9luR0sEkKEvZIwzMFV8NQTF5IF%2FbBpFjrzUs6FGGaO5Lllx9fYnBudcq%2F%2FEI8kmT3Iu%2FbRDKBgp%2FIpGjtSC7O9aGPLvMiVv7lPTuDvgtq4jONX8AdmkY7sAJYJxHdi5XXTp7Ry65gDCxQZYfnY%2FQq&X-Amz-Signature=aeb94136f7a7b910ee6f882583a5e2733a1e0b31833d27e73a1df1242bcd7014&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEE5TRSR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWT5V84n6GQPDzxID9Z%2F8OfBV0i7TyfN3mph8x8jev4wIhAIb7jGRroJDxbwWm164x2ZYFB7x43Qfrn3htdg0CdTGLKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz8CSaIYkc1DphI4lEq3AOEZi362rurNaB7gWTmUFEpYuwEWpJRC85rmgiT3LTy02EBBDCzSh8lFXVJTm0XWQGseFGyWFQJMuDyI61NUGfNq71oVNoSYwye6gGjfccncRXayqPT7u9Tuc%2F%2BvggCNHkuf6ikIZhSVGDfwDrvyPq%2BUyPKtSh9C6Q9xuaSYmAYAOjx5%2B26xITHyOgBbfTKKUwYzomGYXe5IhXXnCpL%2Bw5YNAXMYEOjfiwO6qsRK0fd6Ql5Dp%2B%2FxRrQBktH0tdiVKFNDm1Wn%2Fk8ZuGmlsLbolIJgTgDR%2FWJ45B8Vm4QYCN0gZk6ycVp8KrWjDtE8NiVY0tMoH0FA588kIYF5aExDAB895hiM6vVeTwilPe%2Buc8N8%2FsBpsHLduPGPKthG%2FLqusYxYBcmc0ZX%2FQXmrLeOMmY0LFzZUrfNqFA3D2mU%2F2xhUp7k%2BvrakkYeQN4e%2FTmdaZbMCDwf%2FYeqWpqOi7DzGknzIcGJ7nefnD7MuiFZWnnqt24cvVBPtFcgG70FVQPR%2Fv1EzzSZvsJqmsilLbxwJuzmLuvuEJIflUGkbXX8rP7%2BrDVJjb8VnkbKRZYRnCsgMNTMZX6ysKgrxDruiz4GY4ljIe2T7NUHBOBERII4xjymZSxcW0FmvyNoFoCPTjCp6%2By8BjqkAdZxe5RfakQnhLDV6Hq7zouQUU8wyLyvUkHG0MAGyfVE7wtJtGv5dR%2FhlTmegDccTOp5GLRCmMrABClj5LYJ0mcGpWoxnn38k0tJkd4T6uxXrEkbmJ2YC%2Bsa6baSaDkk46Sqzu%2BS9z7huE%2BEM5Uy8jqjAHRDprYjREMv4V2mX%2BtIhysluRI%2B1N9kwhGV3DwFfdL%2FbIjdrc7DZs%2F5u3WH1cO6N5iW&X-Amz-Signature=bbf5f4b7c443974c98ac6549f7f9030485cf0c116ab519c88198cce30e2eedb1&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA7E5FD4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDH4Sn9gC6Ga2B25ZaLbqoZ5avgrSsS3Uh%2BR0oxkHRY4AiEAvwWv2X17NZ%2F%2BCVt4wXZhzgpMqvRcwAFkHDGcHoB%2Fmw0qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMOIAa9DZdDE7JCv3CrcA2xMioI1%2BtezWxRZXGdDzvuUTeswX9%2FDrg10MbCONY%2FI2Q5fUqwUoCXcQ2S2vEMe4yEHnmWZyKQs%2BdlhOvNhB9Y4LOZKPnTseYqUjwW9qOEZu1GKyWYnvbnp%2F1uSjfqK5YRwQby4zLPuiEpqH5EuY2oHbPTl7RnEIRTxUed20tpUc9QYWduHEIrvUhsThps7pWptGHvxhX%2BAatv7jPo%2BpHV8QbcnVO2bPlJ7bjX205ShvT9phbUSqNbjKy82c2v%2B8CucPKLu1PicpuvDE%2B67V%2FNiPXBylDGlE%2FumQw6Y7Y6pomrGCIigP6NCNWnKsLDPis83epcpMU1WxykD3GacAcmE2wVV8jAGObmGDvOs8%2BRE5wGE4hRJpm%2BT71fStbUV3LTPX0NvudfvKtai8fi%2Fr5KorvHU2BwhfzpKu3Ipyy3kUIP%2FG2lJnNrJsBz9E%2BSj6TIYdazccUksKG20b%2FNQdYrg1BbsgKpXwIWnhkmC54DwOCJjTC0QchPzrPxstZyyqyDuayL60bSskz3ji1r7FVM2%2Fxv5QIwCvpFBgJ461YOCOys1Zyu%2FFVG51TpBc7HzQ%2Bpjx5KxrHh30SRxb9ZcXfve5lIT%2Ba%2FkVkaGd2PEtvbKSVdsXwr2p%2Fz3mUluMLnr7LwGOqUBr%2FPthlERh08gy7piDXqaJ10yqPAiAfe90xf%2FJbk0Z6vwfDxjPC5yzsB92y7kY4Sw8FGOKT9is1PWWXOO7KSzORBodGCOkNqALUNyUOfH%2F%2B4GlP9pEpslnTCSzzQqCJjQzM%2B4a%2BahiyrEOhH%2BRk0xyApfvGF91w9NgMcXYOZ9SBZlyA0Rzwi5x%2B%2BYCWf3K4QGO71q8N3ckX0SVUFiIctTzMnr8TzK&X-Amz-Signature=1b9b87d953eb21f05d69b025cf3ab7aefe3e866c7c81d30a74d179f3b0022221&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYNQ4N6L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGLU7wCu5N4mPBBszoMwPH07eMYrtti%2Bx4aY%2Fs1%2B%2FoT1AiBRmIvVrW%2B6M6wIdUnkkYwKzG9adLaJrW3x9psnoiuNsiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFRm3EbTrrg%2B6abtDKtwDO9sIvM2XUi6hgGoByhLDlhGyxPmua9y%2FzXvJVI7o7VJpGEvOYO4p9oHMzkB5juBVRzE%2FJOY7MOXHdurFirZYsQ8IVE2qH%2FwXuewiVqw35v6k%2BBDVFUqnf6cwLExi85FMfJmVVghDXBN%2BNWqE2l7MyjKo2L4XjGkzpmFZlLWycbP9TpiESeHhvYV8Ru0ggiOnssEj7q0jffG1pQrfl4WSXwQwL7KMugJOsbXBGliZMu3%2F95Lvmrj%2Fwh4dQ2WQ5WRFXsq%2BYwO%2BpMoXgfrL6COjie8uLG3J49R2kWkq1%2BxFiHsK2L%2FYbMwC4A03WnmylKPaOWbRzGGgjd%2FZd3Es8MDtV51fKua0FYiq7YV3EA9AJrdnril6LEEVeQ6W21kxqPE7r0TH1bSj8O8lmlEKVDjcQo4fxKZSXNsgeILR2ZFDZt64JKi6%2B3vdq1kADLoyvCphllD3fesrKTjIjvJfud0hxEicZoqAdkccLlqSNeDtg8adceHz1VCEzrb%2B40WpPMbLQXIxmcWwMJSdhHzS9IPty2me4Hbu1YmgxMBEzz0iOD99dp0jahHPDq87X%2B0mf4NmzabLKvMEuL%2F%2FmHmi3cI1S%2B384gwmKZ4ZO9fC8PWT3OFWweHRDX9eMowUbqsw1%2BvsvAY6pgEfLejNmmAtVWD6zRPxEw5NbsuaxKizbdxjVeqZe%2FxT0GvFEdSRXx19211fKaDqirzYXvsF%2FkH9luR0sEkKEvZIwzMFV8NQTF5IF%2FbBpFjrzUs6FGGaO5Lllx9fYnBudcq%2F%2FEI8kmT3Iu%2FbRDKBgp%2FIpGjtSC7O9aGPLvMiVv7lPTuDvgtq4jONX8AdmkY7sAJYJxHdi5XXTp7Ry65gDCxQZYfnY%2FQq&X-Amz-Signature=ebc3ee94a426b8416255cadbc1dad7213ae7c62bba641217a08817697bda8ac8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYNQ4N6L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGLU7wCu5N4mPBBszoMwPH07eMYrtti%2Bx4aY%2Fs1%2B%2FoT1AiBRmIvVrW%2B6M6wIdUnkkYwKzG9adLaJrW3x9psnoiuNsiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFRm3EbTrrg%2B6abtDKtwDO9sIvM2XUi6hgGoByhLDlhGyxPmua9y%2FzXvJVI7o7VJpGEvOYO4p9oHMzkB5juBVRzE%2FJOY7MOXHdurFirZYsQ8IVE2qH%2FwXuewiVqw35v6k%2BBDVFUqnf6cwLExi85FMfJmVVghDXBN%2BNWqE2l7MyjKo2L4XjGkzpmFZlLWycbP9TpiESeHhvYV8Ru0ggiOnssEj7q0jffG1pQrfl4WSXwQwL7KMugJOsbXBGliZMu3%2F95Lvmrj%2Fwh4dQ2WQ5WRFXsq%2BYwO%2BpMoXgfrL6COjie8uLG3J49R2kWkq1%2BxFiHsK2L%2FYbMwC4A03WnmylKPaOWbRzGGgjd%2FZd3Es8MDtV51fKua0FYiq7YV3EA9AJrdnril6LEEVeQ6W21kxqPE7r0TH1bSj8O8lmlEKVDjcQo4fxKZSXNsgeILR2ZFDZt64JKi6%2B3vdq1kADLoyvCphllD3fesrKTjIjvJfud0hxEicZoqAdkccLlqSNeDtg8adceHz1VCEzrb%2B40WpPMbLQXIxmcWwMJSdhHzS9IPty2me4Hbu1YmgxMBEzz0iOD99dp0jahHPDq87X%2B0mf4NmzabLKvMEuL%2F%2FmHmi3cI1S%2B384gwmKZ4ZO9fC8PWT3OFWweHRDX9eMowUbqsw1%2BvsvAY6pgEfLejNmmAtVWD6zRPxEw5NbsuaxKizbdxjVeqZe%2FxT0GvFEdSRXx19211fKaDqirzYXvsF%2FkH9luR0sEkKEvZIwzMFV8NQTF5IF%2FbBpFjrzUs6FGGaO5Lllx9fYnBudcq%2F%2FEI8kmT3Iu%2FbRDKBgp%2FIpGjtSC7O9aGPLvMiVv7lPTuDvgtq4jONX8AdmkY7sAJYJxHdi5XXTp7Ry65gDCxQZYfnY%2FQq&X-Amz-Signature=1f117d585ec505267fa53f8173043c94955a501971f68fe04a23146455f58d5b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYNQ4N6L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGLU7wCu5N4mPBBszoMwPH07eMYrtti%2Bx4aY%2Fs1%2B%2FoT1AiBRmIvVrW%2B6M6wIdUnkkYwKzG9adLaJrW3x9psnoiuNsiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFRm3EbTrrg%2B6abtDKtwDO9sIvM2XUi6hgGoByhLDlhGyxPmua9y%2FzXvJVI7o7VJpGEvOYO4p9oHMzkB5juBVRzE%2FJOY7MOXHdurFirZYsQ8IVE2qH%2FwXuewiVqw35v6k%2BBDVFUqnf6cwLExi85FMfJmVVghDXBN%2BNWqE2l7MyjKo2L4XjGkzpmFZlLWycbP9TpiESeHhvYV8Ru0ggiOnssEj7q0jffG1pQrfl4WSXwQwL7KMugJOsbXBGliZMu3%2F95Lvmrj%2Fwh4dQ2WQ5WRFXsq%2BYwO%2BpMoXgfrL6COjie8uLG3J49R2kWkq1%2BxFiHsK2L%2FYbMwC4A03WnmylKPaOWbRzGGgjd%2FZd3Es8MDtV51fKua0FYiq7YV3EA9AJrdnril6LEEVeQ6W21kxqPE7r0TH1bSj8O8lmlEKVDjcQo4fxKZSXNsgeILR2ZFDZt64JKi6%2B3vdq1kADLoyvCphllD3fesrKTjIjvJfud0hxEicZoqAdkccLlqSNeDtg8adceHz1VCEzrb%2B40WpPMbLQXIxmcWwMJSdhHzS9IPty2me4Hbu1YmgxMBEzz0iOD99dp0jahHPDq87X%2B0mf4NmzabLKvMEuL%2F%2FmHmi3cI1S%2B384gwmKZ4ZO9fC8PWT3OFWweHRDX9eMowUbqsw1%2BvsvAY6pgEfLejNmmAtVWD6zRPxEw5NbsuaxKizbdxjVeqZe%2FxT0GvFEdSRXx19211fKaDqirzYXvsF%2FkH9luR0sEkKEvZIwzMFV8NQTF5IF%2FbBpFjrzUs6FGGaO5Lllx9fYnBudcq%2F%2FEI8kmT3Iu%2FbRDKBgp%2FIpGjtSC7O9aGPLvMiVv7lPTuDvgtq4jONX8AdmkY7sAJYJxHdi5XXTp7Ry65gDCxQZYfnY%2FQq&X-Amz-Signature=dcd32a82e69fe0ad87905d7078a2984ab692b1d77a974335fb9197dd287d06f7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677R24EUX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAJvXofoXTFrWx1T8%2Btuy4tX2M%2BD67TSEnFxv7xmAoOwIhAOUft62TedC5%2FfObbTBnGU3w0eroGjT9DmddaCHs5s%2BFKogECKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxc699lqWhlZUEMApkq3ANow0Z%2FIKpFSUWgVqC%2FOgc9pzrdj%2FaGpfV5jmQNBGS1OOSTeuraj5n%2BgRYUCF0OpxuMCXGudcNdMLYO5vhegRbWRD3m9zFzlcRQXm%2FTrR6pHcVKQSyPw3MY%2FGI5hudzDWj55TXEobz%2FqquLJtuygatca75pwh%2Fcz%2BCgHiaIii%2BqnrM%2Bb0unIpnFnWvUAmS8eVfWd9lMnqX%2FQBotcqfQo8ogjT5H1%2BqdA%2BQHnCWw%2B%2FXqrums34tat1D%2FyqmSQTnRdBTvj7RrQq0O0bMkgZG8tbiarX7P1KYSIXpTxH5yye1AHKTW6kx2%2FrZ6PC4I5TGLNMxk7E%2B%2BM6QkQurFfPZ%2FOBF6ICOil%2FpatnZia9ypiQy3eZ2c2%2BUYEkXidxX1KwzmAZ%2BC4ri42dHepQ4AED5MEM%2FK7CKlyKPl%2FlmIbkHiHXeaoJUkjGGS1F8ljuZyZuoTSSxUNwf64fjrwBg9tXNm2ptDTxgfVRvfLEHhTIq%2F1jzdD9LRtbHmoWLrekcvI1skmM4lJQve92hcu%2FA94nG0YL2GmOAq2RnsOC8HIXtbnz2f5Nee1vihpxer0Rtd78pzbyEHJuBkpw907oHkMOHph8QM3fUdZaKlgzd2RadxAoe6R%2F0PBKEYe%2FVwjvx8STD47uy8BjqkAb1ZCX4M3xLPtiNVYUrlcLUKbW4Qf0R38ugmYPH%2FpL%2FwpA2xm%2FfS%2F%2FEjjIuwNJXAqJrlmF92HoYObkQQU3j7FdIeUHwJlduuseNiD6cbowlzGDxwPeW7d1AWbMaMolnJvDHfg7aCtKW%2FbcoqYYPAQtjGkOXiK%2FCT8Yu827ExQ88LEWzQsKCP97AMB%2BoN5Vi5kkYjiZ0Z0AzY8%2FJpifkwJ0a0FUW4&X-Amz-Signature=d1877025af369c2c9dfa4c8fc55fa7502972fe9f8aef47e8cf983bf09aef0d14&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC5T5UTJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBi8ta2k10IyYvgahE8L7T%2FVEgjjJcV6NDXo7I0l2xXSAiBZB%2FScVfBGtrspPwRdC9euhzEr%2BpvwpPGXsTjhBFU4pCqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrjkCcNQhPyBrMdA5KtwDJoOTyHsYjGqWjoONUZv5yvl4vyHTic1BfoPUOvkceQUgVcJtoB1FSGvukW%2BFgD2PFKfCjOPPIUtXVoJYl8HnqCJ174qeybYBZiG%2Fxe%2FMN5aWqHATlhqI9wGcIEOX2VtUkzv5ra%2Fl53667akNMbEbO9hfRWFzpAcTx3b9RmUy%2BZt9Ur%2B7gJL9x4hFu40%2FRxwt%2FbQ2U9CTSU0WtzX8v698cJFPKL%2BrLfIWdFuGHCKLm8Z2jOTq3EwNCRUIU8CXUNvZYas1cpmFBjpeYipMIZlZFpZg0RZpa55l2XmQ6Oe1XHPD4VCdLLOf0gk1vRu8f0SskGAE1Zt75PWdF9FD02yGlCo%2FEPrLenafqXTjDvFjQnQE04RTwVVAIWnTLUyT3LOMQTgCDvh7LV85RqpWQsimQcfFN5EfUpSgux%2FbquxUOfowebN2uOKeRxs2Mc8FZJ01Tjc48pR2l%2Fn3Pn%2BnFoDfDewG8qjFSfOl0bs4i2XimtRkblGdH126Msa2pCV3TmLnMmbh2ZNY2ZOgbndWa7Dnt25Vlb8voqXfQkYVq7l24gXvuNgyhPuqfUzERLhc69kB998BYAgCbrUsRNRw8i9LvnKmmveHKUqQ%2BN%2F6IOUu33h%2FUifIXCbhy1XFe4cwhOzsvAY6pgEFeLLchHSvPxIIQI9Pjuua3n2vJ5BtVSsgMSkxtgTd0%2Fu3ERkkKaJZDQwEL3EY676AvlaPgTW1yG4vv%2FbZsmQxnpfTovOnyh0xCtXKoX6W4c4jvX3ryyrDHu2LkQpVviRSfcVayvRiEzkzQL5x%2BIeJgEdFUoImMZ8SNMjj2H5pmNE38TupAoWhdew8T8WyUXxMWgIF6TKmWYCl%2FuP1JZs0lOHC0M8%2F&X-Amz-Signature=29b5fbed1991026f29dbf63e8d00884b2fbd201b1443f73d56955490335a841f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZU2THRVE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjyFyvwFadCeC1CtveFQVDXvOHglpjKejiAaKWnUPpAwIhALc7ZBgMrOb3S3Xjua8ml59Cf5L1sONrG6BU8kXDuKKJKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzbvlFSEGCatiLBJo0q3AOPGyFCBvcwc6l%2FGy9G04bwWSPDjmQWPlXOYzIySay5TAdM0ZY%2B6Y%2BlEQEbMMe47ZAf9d5OX8FmtNikXl%2BLk%2FHRNoMi7t6%2FyEgbCSpfAtJdN7ImGJa%2FnmZuByJ5TL8WKyzkg2pPIoPixR96Uwv%2FuJwx71o710nXK%2FQPWpQT1nIvs%2FcWDegqyrG8DSbKJF5TcFJtAk1NqpHQMW45nY29NU0EnRhtbt1f863mMMLHkAE3YjZzK9KbB%2Beyr5jmRwwcjK19tdnH9WqU1uH8TYacO%2BHwbWUAxPZI5NcBp7K6RTOPJY%2B4xyRVd7RSYgOPWl5NoZ08SMtF7te1rvs%2FZVMEIRMc%2BZN2oihyOIBYuwBMckS27uJ2NUNjhpu%2FFrbrRMS4PpRgHFiQ6M2k%2BNMqS6T51e7FMcCb238PJrWlOtskkRNIrKjbwRldedN8rPJQaYROyrPj0rKSBVV3Mh0mkGpk2Ln%2BRPLVKmofd9zzEI6%2F2209T2Bi3e0k5v0ae1Hp9H716xrlSX2IHTRu5gpkRRcf%2BFCFgtIHddi%2BXr7IJFshiQIntNSjBmBrX4pP2tCERdxmIZkmZgg9u%2F8%2BQpfiFIgtyCL24R4Gbj9rdTA%2F%2FtVe1Akte4dI9V%2BBMCrH07B0EjC16%2By8BjqkAaD1Fp5zaSEz1nR3yVXQyIaLZqwYnzKj8k%2FAaoyjywRszk2DrBk3AR0qrH6C4s6JiAh1FwlvNIrnYcMeqkYpBqeXlDupK7zuteIfxHAOI7tASl9FMtdsssDcPp1GM4wqjOYkRjiuUZc1gQYWntsyjJiiDrQZQkaRL0FPbKX5mTsdhgT31eqe8kagLOTGk3ZfLAzToQkxyaObWblyMnpkhAzEKRHT&X-Amz-Signature=a3685aa51dace15b132dc954eff72e6e2fc3f38096372aa557c6ddc91e9a31df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL72F72X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEnIxyvPop0HkMv%2BsWp2e78VLrZHWlAVScvE81HaOkpyAiEA3i5I1sFcoMjqaTn50tExe0l2N%2BqOfVZ09NQObcmL4msqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGNUW1bZwW3gvl6l7CrcA%2BOldQwmGCfVddNKvpeAM5RRi8GZfO7dmBZYsrR2E%2Bvtezc%2FmMdEMRu6Y3AcSkFW6SQa2e9Hs2Xe86hFBM7hP6Esmb6vj50N%2BcAUy4pmbVpJc9byzs0iDnv3ib4%2BDjdTv22kacLsd1R1LawcvTB9ZC4oAX5a8WRHhdwp%2FA%2Biu4sVXlBgxnga2bB3k3XFo4Ujw0M0LuCQHONsj4Up%2FXBBo6KeLjy7vsNI8pPlRc%2BNunsitncMkehPk9oFfL6KQ2qXMyZvt4EiADBMznZegXWpFtHWqIhcC8EbFxy%2BRaI5txK%2B2tLLlpO1Zopjpz81azsInGkTaT717wropCiohkM%2FOcdG9MX2TL%2FPjKfDDCdos3XyQfiQkD54i4JLrPhcJ2yAKaE%2BGdM88R7bdPXpjjAgvDKv6MgHd0bYBpp%2B8veEvTjDIDy6BetY0f%2BoYi%2FLxSICBCYw9n69T%2BYI%2BaEqM0%2BfrDZq%2BcOh52MdnSKzbK8xxxpXHLdR6F1R3jWb4SCa6ypMBYwYAozUYRLdbFWGT4177coC8KLtgDAsF6nZ2QJcyNFrIe%2FKwh%2BRHA9rQPl7dJ47LAtVsQE4X75qaEuj%2F%2BMvmT8oCsUMidc4Qghjif3sJFYBmEEhfBnUvi%2B9F3ZsMIbr7LwGOqUB6uFcXFR2MbsT%2FBpdhE1copoOzw1nRzrh7E0D1fetPn5R3O7qirPfK%2FWwDvazIR%2Fj5Mkpof4xzn9zlQBWpTni1ZAJnYsZBk%2B4TG3QExgMnADBEGklKrQWktJVGvj6DAmQgwxhZ55HpLFMZiGXb5PobIsnT96ZNuOEWgY5OPqBhc3Ans9Wix0sd3boVqQ3Du6GYPT0LbeFjKVIDaZxGovRzKqVaRmX&X-Amz-Signature=5b39125592730a1ad6a5a264d8628ad8026433883f3857d070fb868dd5b4f7e3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL72F72X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEnIxyvPop0HkMv%2BsWp2e78VLrZHWlAVScvE81HaOkpyAiEA3i5I1sFcoMjqaTn50tExe0l2N%2BqOfVZ09NQObcmL4msqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGNUW1bZwW3gvl6l7CrcA%2BOldQwmGCfVddNKvpeAM5RRi8GZfO7dmBZYsrR2E%2Bvtezc%2FmMdEMRu6Y3AcSkFW6SQa2e9Hs2Xe86hFBM7hP6Esmb6vj50N%2BcAUy4pmbVpJc9byzs0iDnv3ib4%2BDjdTv22kacLsd1R1LawcvTB9ZC4oAX5a8WRHhdwp%2FA%2Biu4sVXlBgxnga2bB3k3XFo4Ujw0M0LuCQHONsj4Up%2FXBBo6KeLjy7vsNI8pPlRc%2BNunsitncMkehPk9oFfL6KQ2qXMyZvt4EiADBMznZegXWpFtHWqIhcC8EbFxy%2BRaI5txK%2B2tLLlpO1Zopjpz81azsInGkTaT717wropCiohkM%2FOcdG9MX2TL%2FPjKfDDCdos3XyQfiQkD54i4JLrPhcJ2yAKaE%2BGdM88R7bdPXpjjAgvDKv6MgHd0bYBpp%2B8veEvTjDIDy6BetY0f%2BoYi%2FLxSICBCYw9n69T%2BYI%2BaEqM0%2BfrDZq%2BcOh52MdnSKzbK8xxxpXHLdR6F1R3jWb4SCa6ypMBYwYAozUYRLdbFWGT4177coC8KLtgDAsF6nZ2QJcyNFrIe%2FKwh%2BRHA9rQPl7dJ47LAtVsQE4X75qaEuj%2F%2BMvmT8oCsUMidc4Qghjif3sJFYBmEEhfBnUvi%2B9F3ZsMIbr7LwGOqUB6uFcXFR2MbsT%2FBpdhE1copoOzw1nRzrh7E0D1fetPn5R3O7qirPfK%2FWwDvazIR%2Fj5Mkpof4xzn9zlQBWpTni1ZAJnYsZBk%2B4TG3QExgMnADBEGklKrQWktJVGvj6DAmQgwxhZ55HpLFMZiGXb5PobIsnT96ZNuOEWgY5OPqBhc3Ans9Wix0sd3boVqQ3Du6GYPT0LbeFjKVIDaZxGovRzKqVaRmX&X-Amz-Signature=9adaaf0ae125675961e2037ffcbaa024dc41ffb882bef361702c46b5a74a26ec&X-Amz-SignedHeaders=host&x-id=GetObject)

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
