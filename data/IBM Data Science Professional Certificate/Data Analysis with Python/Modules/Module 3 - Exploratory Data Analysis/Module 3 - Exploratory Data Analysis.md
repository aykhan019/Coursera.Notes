

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIKJWGCJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCh6fsHAdSvDMhA8c5zqyjOv8jykUc5c8swF3PGu8ZXGgIgObt%2FiqzGfnL8KLhILKFiDWItSG%2FM7i4h1Sc6U3nrlHQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOIxNqPaXcIj6dpsRSrcA53oDbqv11fyxY0WbdZZ1SnmbTkU%2F0dg0cKhIO9jpPH9ZHHo46aUPzuCkjtex7pc2ARR3QhqikaTaqmoQQeC5WFQrmLmB50ogOpOhhin2TUhY0%2FqCZLb8EvoleynuKYBmQ5y5WLmHD3g8%2BnUJ2%2B9t7IF6JxyK4UscO1S3vs1XrbSbfbZ8SLLnjYgAru27j8ezghXRdEPdmVcqp95R%2By10xNozcb46xSUfXxiIO9z1rvCSK8xHQjFicp%2F5V71cWsXd4Wp98%2FvLRYCQgLK7RusC2toMRapclman0mJRuNtf7fyq9fdw0hUwLHb98tQoa2RfjcLVqsaqdocuMIAl2nWq%2FC1m6dhMim6hKNMJzhzMTADG08OFwlO3VTvnHpvw06ZhRaG1b31bKPMydctg1JrnaYi3%2B0lMSQnSLV68IJluXAdHMWP%2Fd0Yr6tsKn5HNa1whpj8Bgv5kETHS%2BJLfT6pku4ex7wkLHYpYA6Al3vWKqIK8HAuG4Y4qQXDPJEMAwjwxLUCnixkceT2RTqCzX3ISrqFJZZVDkvFp6PmTGvwtzc9iW8PJlpgz8u62PyWGiKgOnUlkeoPbpuAbo%2BBr6pvTiWHOVXnRpeKcCORtfGCZFD7TBM5pHEOA3lKK9f5MO%2F49LwGOqUB50Wl7rPv695yv8YvBChZrVVU2DMe1qtzhBsYXHG80zqZ3BIEtT2gmfs8EZhRVxX6NqEvcH3vyE128tGQUlr3WnsHoNlX30Qo6F68Xb7ALDtJJZia%2BJAhI7AmBwZRwem%2BiHVWzdq61Kl7l73r1ltIxwpiDQevWZPB5sVdOo1P3%2FfuG97t%2BcTY%2B1KN%2FWTMBfhRWn44xmQOAjXzC3rr51kFJDYYi21g&X-Amz-Signature=c69953688a22a758451a4e8a2eacd8ac1425f19fcbfea224aa9fb4a94d7e7b0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIKJWGCJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCh6fsHAdSvDMhA8c5zqyjOv8jykUc5c8swF3PGu8ZXGgIgObt%2FiqzGfnL8KLhILKFiDWItSG%2FM7i4h1Sc6U3nrlHQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOIxNqPaXcIj6dpsRSrcA53oDbqv11fyxY0WbdZZ1SnmbTkU%2F0dg0cKhIO9jpPH9ZHHo46aUPzuCkjtex7pc2ARR3QhqikaTaqmoQQeC5WFQrmLmB50ogOpOhhin2TUhY0%2FqCZLb8EvoleynuKYBmQ5y5WLmHD3g8%2BnUJ2%2B9t7IF6JxyK4UscO1S3vs1XrbSbfbZ8SLLnjYgAru27j8ezghXRdEPdmVcqp95R%2By10xNozcb46xSUfXxiIO9z1rvCSK8xHQjFicp%2F5V71cWsXd4Wp98%2FvLRYCQgLK7RusC2toMRapclman0mJRuNtf7fyq9fdw0hUwLHb98tQoa2RfjcLVqsaqdocuMIAl2nWq%2FC1m6dhMim6hKNMJzhzMTADG08OFwlO3VTvnHpvw06ZhRaG1b31bKPMydctg1JrnaYi3%2B0lMSQnSLV68IJluXAdHMWP%2Fd0Yr6tsKn5HNa1whpj8Bgv5kETHS%2BJLfT6pku4ex7wkLHYpYA6Al3vWKqIK8HAuG4Y4qQXDPJEMAwjwxLUCnixkceT2RTqCzX3ISrqFJZZVDkvFp6PmTGvwtzc9iW8PJlpgz8u62PyWGiKgOnUlkeoPbpuAbo%2BBr6pvTiWHOVXnRpeKcCORtfGCZFD7TBM5pHEOA3lKK9f5MO%2F49LwGOqUB50Wl7rPv695yv8YvBChZrVVU2DMe1qtzhBsYXHG80zqZ3BIEtT2gmfs8EZhRVxX6NqEvcH3vyE128tGQUlr3WnsHoNlX30Qo6F68Xb7ALDtJJZia%2BJAhI7AmBwZRwem%2BiHVWzdq61Kl7l73r1ltIxwpiDQevWZPB5sVdOo1P3%2FfuG97t%2BcTY%2B1KN%2FWTMBfhRWn44xmQOAjXzC3rr51kFJDYYi21g&X-Amz-Signature=586bbd3f2d6e24b598bab3e343b1309b9ca6ff1d9465a0a3afb8fd49a37f40cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIKJWGCJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCh6fsHAdSvDMhA8c5zqyjOv8jykUc5c8swF3PGu8ZXGgIgObt%2FiqzGfnL8KLhILKFiDWItSG%2FM7i4h1Sc6U3nrlHQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOIxNqPaXcIj6dpsRSrcA53oDbqv11fyxY0WbdZZ1SnmbTkU%2F0dg0cKhIO9jpPH9ZHHo46aUPzuCkjtex7pc2ARR3QhqikaTaqmoQQeC5WFQrmLmB50ogOpOhhin2TUhY0%2FqCZLb8EvoleynuKYBmQ5y5WLmHD3g8%2BnUJ2%2B9t7IF6JxyK4UscO1S3vs1XrbSbfbZ8SLLnjYgAru27j8ezghXRdEPdmVcqp95R%2By10xNozcb46xSUfXxiIO9z1rvCSK8xHQjFicp%2F5V71cWsXd4Wp98%2FvLRYCQgLK7RusC2toMRapclman0mJRuNtf7fyq9fdw0hUwLHb98tQoa2RfjcLVqsaqdocuMIAl2nWq%2FC1m6dhMim6hKNMJzhzMTADG08OFwlO3VTvnHpvw06ZhRaG1b31bKPMydctg1JrnaYi3%2B0lMSQnSLV68IJluXAdHMWP%2Fd0Yr6tsKn5HNa1whpj8Bgv5kETHS%2BJLfT6pku4ex7wkLHYpYA6Al3vWKqIK8HAuG4Y4qQXDPJEMAwjwxLUCnixkceT2RTqCzX3ISrqFJZZVDkvFp6PmTGvwtzc9iW8PJlpgz8u62PyWGiKgOnUlkeoPbpuAbo%2BBr6pvTiWHOVXnRpeKcCORtfGCZFD7TBM5pHEOA3lKK9f5MO%2F49LwGOqUB50Wl7rPv695yv8YvBChZrVVU2DMe1qtzhBsYXHG80zqZ3BIEtT2gmfs8EZhRVxX6NqEvcH3vyE128tGQUlr3WnsHoNlX30Qo6F68Xb7ALDtJJZia%2BJAhI7AmBwZRwem%2BiHVWzdq61Kl7l73r1ltIxwpiDQevWZPB5sVdOo1P3%2FfuG97t%2BcTY%2B1KN%2FWTMBfhRWn44xmQOAjXzC3rr51kFJDYYi21g&X-Amz-Signature=54d0aed0f4b6d50950a2192f14db89035b0d93097d8ba6e027c21a33b537cf32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH5FKMVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2Sqz85LNXb9qoUdpS1AjsWPbDpS2lqKDbMDCmrxw0ZgIhALCcGlBw0Z8qk5aGmfLLweNcgkjf8rEATkT%2FIzFOMYITKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwE8NrtsiAT%2BFvWYkUq3ANM57oakzc2hrj1YEZriR8QcB2Y9PQfJwObkBF%2Bn8Ip0SiTxvW92ze8pItP8I1o2X0F87xfOjhcm6dxni5dW9u%2FwsKl6%2FCIAM7ZYfrFT%2BCZo2O3QO2Cs2UIdldPANK4U8J1dn5E4LLxSh6uFuKG%2BDRQFBxqrlctdH0TNleJrJBJXc7QBpSNaZ9mPC7qDWU0sF4JjVOOQDjay1MR%2FU4fvT5csgCgv2df47vWgyc2afsro%2Bte7OFf0brKqA3d92a%2B4bk1Ff%2FXEBqngaAaOEDmn6Aaj9i8dluIhmQyxKt5o0hx8nIeN5s2fJqXqgFdNouwMotgcStsy0uFVJP%2BK6Bgw3oCux5yPHb65tm4Y1X3roShfRI1%2FyOcHPhRjNNRn2EcB9rNSk1fbgVEVkJLCdQD0igPzTOR77G3boGq5rG06zuv7wyWvlRqGzDc0Lg8GDaLkhsP9MjnVs2sVj8S0hyi6SnD0p3upA3ANvplHgZMTNHLx1F6jdQio4dVlKmtAJPY8qAstT6y0iFqVOwyK1ghi5JTvoceFYQWqaRz7RFL021%2BHBp52NUjzeD369kOiNcS7Frj2VTNQfFp3OWnt4UdEAs%2F2rBWcLvICQzfAcVYH1NG2MrYy6JXrnBLUL2OPTD0%2BPS8BjqkAcr%2Bpxez1kG%2FsutJIo8FHOsNc8ktGDhO2ULykI%2FoofXUzvHtIBhl2eU9HD%2F7QT2vVtmxjssaQeFMIcfyrqJBKHdY%2Fo%2BhgRAHSA46yHc8Fc1M647PKgjZtGL%2BtJHeHkxz2Qtg1KgOrX6oFvU6LM5wQubjIcKY4ZknPG4gu7xgyFeyVSpmUFZ3co3by8sA2klLgKpEKV9MYqcHOYZqHpuCioudG7Yp&X-Amz-Signature=2c9bb70a44d1902e0ff73c3d9b3312aa73ee75981f42a318b33df429e9bcc2c1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH5FKMVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2Sqz85LNXb9qoUdpS1AjsWPbDpS2lqKDbMDCmrxw0ZgIhALCcGlBw0Z8qk5aGmfLLweNcgkjf8rEATkT%2FIzFOMYITKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwE8NrtsiAT%2BFvWYkUq3ANM57oakzc2hrj1YEZriR8QcB2Y9PQfJwObkBF%2Bn8Ip0SiTxvW92ze8pItP8I1o2X0F87xfOjhcm6dxni5dW9u%2FwsKl6%2FCIAM7ZYfrFT%2BCZo2O3QO2Cs2UIdldPANK4U8J1dn5E4LLxSh6uFuKG%2BDRQFBxqrlctdH0TNleJrJBJXc7QBpSNaZ9mPC7qDWU0sF4JjVOOQDjay1MR%2FU4fvT5csgCgv2df47vWgyc2afsro%2Bte7OFf0brKqA3d92a%2B4bk1Ff%2FXEBqngaAaOEDmn6Aaj9i8dluIhmQyxKt5o0hx8nIeN5s2fJqXqgFdNouwMotgcStsy0uFVJP%2BK6Bgw3oCux5yPHb65tm4Y1X3roShfRI1%2FyOcHPhRjNNRn2EcB9rNSk1fbgVEVkJLCdQD0igPzTOR77G3boGq5rG06zuv7wyWvlRqGzDc0Lg8GDaLkhsP9MjnVs2sVj8S0hyi6SnD0p3upA3ANvplHgZMTNHLx1F6jdQio4dVlKmtAJPY8qAstT6y0iFqVOwyK1ghi5JTvoceFYQWqaRz7RFL021%2BHBp52NUjzeD369kOiNcS7Frj2VTNQfFp3OWnt4UdEAs%2F2rBWcLvICQzfAcVYH1NG2MrYy6JXrnBLUL2OPTD0%2BPS8BjqkAcr%2Bpxez1kG%2FsutJIo8FHOsNc8ktGDhO2ULykI%2FoofXUzvHtIBhl2eU9HD%2F7QT2vVtmxjssaQeFMIcfyrqJBKHdY%2Fo%2BhgRAHSA46yHc8Fc1M647PKgjZtGL%2BtJHeHkxz2Qtg1KgOrX6oFvU6LM5wQubjIcKY4ZknPG4gu7xgyFeyVSpmUFZ3co3by8sA2klLgKpEKV9MYqcHOYZqHpuCioudG7Yp&X-Amz-Signature=8cdc3c27ebc26ee2c382f266fbae2c0e70a40cad854ac1c0a80fa34356ec4a92&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH5FKMVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2Sqz85LNXb9qoUdpS1AjsWPbDpS2lqKDbMDCmrxw0ZgIhALCcGlBw0Z8qk5aGmfLLweNcgkjf8rEATkT%2FIzFOMYITKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwE8NrtsiAT%2BFvWYkUq3ANM57oakzc2hrj1YEZriR8QcB2Y9PQfJwObkBF%2Bn8Ip0SiTxvW92ze8pItP8I1o2X0F87xfOjhcm6dxni5dW9u%2FwsKl6%2FCIAM7ZYfrFT%2BCZo2O3QO2Cs2UIdldPANK4U8J1dn5E4LLxSh6uFuKG%2BDRQFBxqrlctdH0TNleJrJBJXc7QBpSNaZ9mPC7qDWU0sF4JjVOOQDjay1MR%2FU4fvT5csgCgv2df47vWgyc2afsro%2Bte7OFf0brKqA3d92a%2B4bk1Ff%2FXEBqngaAaOEDmn6Aaj9i8dluIhmQyxKt5o0hx8nIeN5s2fJqXqgFdNouwMotgcStsy0uFVJP%2BK6Bgw3oCux5yPHb65tm4Y1X3roShfRI1%2FyOcHPhRjNNRn2EcB9rNSk1fbgVEVkJLCdQD0igPzTOR77G3boGq5rG06zuv7wyWvlRqGzDc0Lg8GDaLkhsP9MjnVs2sVj8S0hyi6SnD0p3upA3ANvplHgZMTNHLx1F6jdQio4dVlKmtAJPY8qAstT6y0iFqVOwyK1ghi5JTvoceFYQWqaRz7RFL021%2BHBp52NUjzeD369kOiNcS7Frj2VTNQfFp3OWnt4UdEAs%2F2rBWcLvICQzfAcVYH1NG2MrYy6JXrnBLUL2OPTD0%2BPS8BjqkAcr%2Bpxez1kG%2FsutJIo8FHOsNc8ktGDhO2ULykI%2FoofXUzvHtIBhl2eU9HD%2F7QT2vVtmxjssaQeFMIcfyrqJBKHdY%2Fo%2BhgRAHSA46yHc8Fc1M647PKgjZtGL%2BtJHeHkxz2Qtg1KgOrX6oFvU6LM5wQubjIcKY4ZknPG4gu7xgyFeyVSpmUFZ3co3by8sA2klLgKpEKV9MYqcHOYZqHpuCioudG7Yp&X-Amz-Signature=b87e1177aabcca23325bc389eba51b8e2ff73686b9b7702a564dcec3dcc9d057&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH5FKMVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2Sqz85LNXb9qoUdpS1AjsWPbDpS2lqKDbMDCmrxw0ZgIhALCcGlBw0Z8qk5aGmfLLweNcgkjf8rEATkT%2FIzFOMYITKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwE8NrtsiAT%2BFvWYkUq3ANM57oakzc2hrj1YEZriR8QcB2Y9PQfJwObkBF%2Bn8Ip0SiTxvW92ze8pItP8I1o2X0F87xfOjhcm6dxni5dW9u%2FwsKl6%2FCIAM7ZYfrFT%2BCZo2O3QO2Cs2UIdldPANK4U8J1dn5E4LLxSh6uFuKG%2BDRQFBxqrlctdH0TNleJrJBJXc7QBpSNaZ9mPC7qDWU0sF4JjVOOQDjay1MR%2FU4fvT5csgCgv2df47vWgyc2afsro%2Bte7OFf0brKqA3d92a%2B4bk1Ff%2FXEBqngaAaOEDmn6Aaj9i8dluIhmQyxKt5o0hx8nIeN5s2fJqXqgFdNouwMotgcStsy0uFVJP%2BK6Bgw3oCux5yPHb65tm4Y1X3roShfRI1%2FyOcHPhRjNNRn2EcB9rNSk1fbgVEVkJLCdQD0igPzTOR77G3boGq5rG06zuv7wyWvlRqGzDc0Lg8GDaLkhsP9MjnVs2sVj8S0hyi6SnD0p3upA3ANvplHgZMTNHLx1F6jdQio4dVlKmtAJPY8qAstT6y0iFqVOwyK1ghi5JTvoceFYQWqaRz7RFL021%2BHBp52NUjzeD369kOiNcS7Frj2VTNQfFp3OWnt4UdEAs%2F2rBWcLvICQzfAcVYH1NG2MrYy6JXrnBLUL2OPTD0%2BPS8BjqkAcr%2Bpxez1kG%2FsutJIo8FHOsNc8ktGDhO2ULykI%2FoofXUzvHtIBhl2eU9HD%2F7QT2vVtmxjssaQeFMIcfyrqJBKHdY%2Fo%2BhgRAHSA46yHc8Fc1M647PKgjZtGL%2BtJHeHkxz2Qtg1KgOrX6oFvU6LM5wQubjIcKY4ZknPG4gu7xgyFeyVSpmUFZ3co3by8sA2klLgKpEKV9MYqcHOYZqHpuCioudG7Yp&X-Amz-Signature=d32a8413af1e04b8f74fa609f4521135ce805dbb834ec8b130d7d9e2f13117b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH5FKMVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2Sqz85LNXb9qoUdpS1AjsWPbDpS2lqKDbMDCmrxw0ZgIhALCcGlBw0Z8qk5aGmfLLweNcgkjf8rEATkT%2FIzFOMYITKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwE8NrtsiAT%2BFvWYkUq3ANM57oakzc2hrj1YEZriR8QcB2Y9PQfJwObkBF%2Bn8Ip0SiTxvW92ze8pItP8I1o2X0F87xfOjhcm6dxni5dW9u%2FwsKl6%2FCIAM7ZYfrFT%2BCZo2O3QO2Cs2UIdldPANK4U8J1dn5E4LLxSh6uFuKG%2BDRQFBxqrlctdH0TNleJrJBJXc7QBpSNaZ9mPC7qDWU0sF4JjVOOQDjay1MR%2FU4fvT5csgCgv2df47vWgyc2afsro%2Bte7OFf0brKqA3d92a%2B4bk1Ff%2FXEBqngaAaOEDmn6Aaj9i8dluIhmQyxKt5o0hx8nIeN5s2fJqXqgFdNouwMotgcStsy0uFVJP%2BK6Bgw3oCux5yPHb65tm4Y1X3roShfRI1%2FyOcHPhRjNNRn2EcB9rNSk1fbgVEVkJLCdQD0igPzTOR77G3boGq5rG06zuv7wyWvlRqGzDc0Lg8GDaLkhsP9MjnVs2sVj8S0hyi6SnD0p3upA3ANvplHgZMTNHLx1F6jdQio4dVlKmtAJPY8qAstT6y0iFqVOwyK1ghi5JTvoceFYQWqaRz7RFL021%2BHBp52NUjzeD369kOiNcS7Frj2VTNQfFp3OWnt4UdEAs%2F2rBWcLvICQzfAcVYH1NG2MrYy6JXrnBLUL2OPTD0%2BPS8BjqkAcr%2Bpxez1kG%2FsutJIo8FHOsNc8ktGDhO2ULykI%2FoofXUzvHtIBhl2eU9HD%2F7QT2vVtmxjssaQeFMIcfyrqJBKHdY%2Fo%2BhgRAHSA46yHc8Fc1M647PKgjZtGL%2BtJHeHkxz2Qtg1KgOrX6oFvU6LM5wQubjIcKY4ZknPG4gu7xgyFeyVSpmUFZ3co3by8sA2klLgKpEKV9MYqcHOYZqHpuCioudG7Yp&X-Amz-Signature=678d21481d0da997535e4b5e1b01755e6c7bb175a63ede06ea83f137c282a3ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH5FKMVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2Sqz85LNXb9qoUdpS1AjsWPbDpS2lqKDbMDCmrxw0ZgIhALCcGlBw0Z8qk5aGmfLLweNcgkjf8rEATkT%2FIzFOMYITKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwE8NrtsiAT%2BFvWYkUq3ANM57oakzc2hrj1YEZriR8QcB2Y9PQfJwObkBF%2Bn8Ip0SiTxvW92ze8pItP8I1o2X0F87xfOjhcm6dxni5dW9u%2FwsKl6%2FCIAM7ZYfrFT%2BCZo2O3QO2Cs2UIdldPANK4U8J1dn5E4LLxSh6uFuKG%2BDRQFBxqrlctdH0TNleJrJBJXc7QBpSNaZ9mPC7qDWU0sF4JjVOOQDjay1MR%2FU4fvT5csgCgv2df47vWgyc2afsro%2Bte7OFf0brKqA3d92a%2B4bk1Ff%2FXEBqngaAaOEDmn6Aaj9i8dluIhmQyxKt5o0hx8nIeN5s2fJqXqgFdNouwMotgcStsy0uFVJP%2BK6Bgw3oCux5yPHb65tm4Y1X3roShfRI1%2FyOcHPhRjNNRn2EcB9rNSk1fbgVEVkJLCdQD0igPzTOR77G3boGq5rG06zuv7wyWvlRqGzDc0Lg8GDaLkhsP9MjnVs2sVj8S0hyi6SnD0p3upA3ANvplHgZMTNHLx1F6jdQio4dVlKmtAJPY8qAstT6y0iFqVOwyK1ghi5JTvoceFYQWqaRz7RFL021%2BHBp52NUjzeD369kOiNcS7Frj2VTNQfFp3OWnt4UdEAs%2F2rBWcLvICQzfAcVYH1NG2MrYy6JXrnBLUL2OPTD0%2BPS8BjqkAcr%2Bpxez1kG%2FsutJIo8FHOsNc8ktGDhO2ULykI%2FoofXUzvHtIBhl2eU9HD%2F7QT2vVtmxjssaQeFMIcfyrqJBKHdY%2Fo%2BhgRAHSA46yHc8Fc1M647PKgjZtGL%2BtJHeHkxz2Qtg1KgOrX6oFvU6LM5wQubjIcKY4ZknPG4gu7xgyFeyVSpmUFZ3co3by8sA2klLgKpEKV9MYqcHOYZqHpuCioudG7Yp&X-Amz-Signature=869b257529cac6c7784b1ab03c51b7983761b54737056afb263f6f9f4e9f9850&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTR5IXHJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJZIiYgq3HzVVGfmWte%2Fvqfc4L63DJAgkhp5jhzWjIOwIgYLfL0ASVjHz0I3dH63r1CJ1jSlex7SbqAEr3HmW%2Fl8AqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAtjlqedjGXKT2p7UircA%2FQSLLS6aL%2B4gN9atzmNlNdGQwj%2Fsa%2FxIrECe07LPvRTwXDR3nVgMicFlqFWZNI01FNaVAsrv2NJMc9KXhm0%2FEHJnXjTLRAbih6njLrc3tAr3tw%2FLVOnWV6U5wvqOGrC2rHn590wnkgNH99ee1ddX0F10oqv9WRBYRidZI0W5%2B3unWj7s41s0eMNiGgv3xkiXawCHu2NWBH9lV7Zm0wPlnxq6cKp8z7j7RxWIJKsmQLvFOdxW1DCzczMzJgm9xQduBcSV%2FI5md2rKRVa6O15%2F5go8H8Uzze1QmkzMKr8vt%2BTVvD3QwJE7svVWYekz4TScA%2BhOr%2Fhe2StDDVV7buIDkw3rMbAEmHfyCZYmyhY7UR5ERLWyPikU13s6Fqz36PlXOtpxocATO7mzn%2F3qrWkLjIAyZHXoqXbec7LO0H8fDL8m3Gzk%2BiZytLwRA%2Fihkcfx08%2F8TqWxj4V%2B5YI6kafVf4hwd2MIiQRtQZ66fuQxXU8EBVLaJrZRwUxwAzdCSWLzmvBbryYAQ1jnOoL4S%2Ba2tnbyoQTpE8p%2BlfHOUSZ%2FmyMqU7JKPBml4tzACdT%2BsU7WyGrnngT6v%2B3hQYeJ9iw%2B6qLyM4EfEX4qIQcLl%2FtEV5FgJ8nSgNVQ8PPg8pnMMP49LwGOqUBAYyKBA77JIknz92dmklCnfZylsCP3353pJLVZByT0P4%2B9z4WqO83EWcPY7jVYGMDGCSVxQGDYM1kdaiEtAd7jDBaaTTFK7QiHA2Ct0v5pRNHIMy8HsXHFT2GV%2F6Tt0irxvPWFlhBINSDde1ei4pZXzK%2FG1TmScUahbuh94xd%2BSzq0TDfvHCp30K4K%2BU3USmXTrnER7BpwAxJM3NFI0Bz4lUccrH2&X-Amz-Signature=ed7650e11920c390c586cd8a93a027ddae2e781f15f8ea23e898ba6cb918e18d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YUPKY2C%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0fIe68%2BYLDbv1J60hG8U61kM5iIy4JF6MLhx2ce%2B9SQIhAO3UcjqJev4sb8b7zFbPoF%2Feqqj9EpZSSBJPQ%2FUOkffgKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvZE9kdRlLv78xnTYq3ANXcBS96usqa99pseYTquGyVMjjynL1H9lKa45MH2j7Qezvk3TGaFwCtPrrqg1WHpZre5lz9D2gBvLNEm3F0G9YVH1rk9%2F%2B2jNQEWf7ezkUCCUHnBzO308Y2IIOVM5X26R682s%2F495TtUG2g3TDwDKf2EikSu598RJ%2FiUtG4HREkZ5SLuoQTq66ymiOcjsUSRpMCQXKuenGmoZSj%2BROmiYNxmyv1JSGB6Zmt%2BeXQuk%2FfCOFSr2knrB0F9Q7vTFDxoylAf5KUFx9G%2F1p5I8tm6Z3%2FMaJmNCcUKWgzzyGhVtVj2im7TGJyy8U1LnJaqYtOdIylr%2FycNxAqIyYFu2qj7hiFZj%2BNpQNVFg2SbC9VE%2BcWvaS6sHN7Msee%2FCn9KzP%2BFAlpALxRqJBmd2MiouseWFReoekF3Ut3jdeF%2BguJx%2BEQSwT%2B8wp54JVcfWtX3NAa1ssS%2B7HhDcM10MPuUHyx7voDEcQ5Dp3qlpOl%2B50IIe1mxVyNUDYOo7f7HJLk5g%2FwBqGHu4lN2atB06Uk4Bpm4Ro3io2JEC%2FGm49yV4%2FKvo7BRNI%2BjY0cnxcAse9e9ZqQdTjV74ah3X4%2FAzH33Hrr4iuxfNePp%2FpMVhEtaMAZrhPtRZaCfqIHOD6NAUu9jDf%2BPS8BjqkAcI5A7DTyv0nUQQrtfSFBM8oxD5pQmlkOwJewVJ1%2FjDfctCTXEwjPqG2HrLuESfm5xmG7MHfMxguxXBfm4gbHGn8qGhn%2BKXMl%2FvjXksT2RWJWqY5k8soQuovayLdTXZhh9txQ9VnddWJauX8b8o8i4fontNkx6Q8EO3iVIPzkhq3CaR8twF1Zix%2Bv3Y0gdqn%2FCW83W7Z6NgjbQY%2B8o6GkXgf0oN%2B&X-Amz-Signature=39ff16d63cce08990ce33974f0e7f376bb982d0e677053066ebdb30d58936b0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH5FKMVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2Sqz85LNXb9qoUdpS1AjsWPbDpS2lqKDbMDCmrxw0ZgIhALCcGlBw0Z8qk5aGmfLLweNcgkjf8rEATkT%2FIzFOMYITKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwE8NrtsiAT%2BFvWYkUq3ANM57oakzc2hrj1YEZriR8QcB2Y9PQfJwObkBF%2Bn8Ip0SiTxvW92ze8pItP8I1o2X0F87xfOjhcm6dxni5dW9u%2FwsKl6%2FCIAM7ZYfrFT%2BCZo2O3QO2Cs2UIdldPANK4U8J1dn5E4LLxSh6uFuKG%2BDRQFBxqrlctdH0TNleJrJBJXc7QBpSNaZ9mPC7qDWU0sF4JjVOOQDjay1MR%2FU4fvT5csgCgv2df47vWgyc2afsro%2Bte7OFf0brKqA3d92a%2B4bk1Ff%2FXEBqngaAaOEDmn6Aaj9i8dluIhmQyxKt5o0hx8nIeN5s2fJqXqgFdNouwMotgcStsy0uFVJP%2BK6Bgw3oCux5yPHb65tm4Y1X3roShfRI1%2FyOcHPhRjNNRn2EcB9rNSk1fbgVEVkJLCdQD0igPzTOR77G3boGq5rG06zuv7wyWvlRqGzDc0Lg8GDaLkhsP9MjnVs2sVj8S0hyi6SnD0p3upA3ANvplHgZMTNHLx1F6jdQio4dVlKmtAJPY8qAstT6y0iFqVOwyK1ghi5JTvoceFYQWqaRz7RFL021%2BHBp52NUjzeD369kOiNcS7Frj2VTNQfFp3OWnt4UdEAs%2F2rBWcLvICQzfAcVYH1NG2MrYy6JXrnBLUL2OPTD0%2BPS8BjqkAcr%2Bpxez1kG%2FsutJIo8FHOsNc8ktGDhO2ULykI%2FoofXUzvHtIBhl2eU9HD%2F7QT2vVtmxjssaQeFMIcfyrqJBKHdY%2Fo%2BhgRAHSA46yHc8Fc1M647PKgjZtGL%2BtJHeHkxz2Qtg1KgOrX6oFvU6LM5wQubjIcKY4ZknPG4gu7xgyFeyVSpmUFZ3co3by8sA2klLgKpEKV9MYqcHOYZqHpuCioudG7Yp&X-Amz-Signature=0b6f4c54a1ef9ddde1f9a2166468880bcd9936c9780d11e8d0c5dcf8ac07184c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH5FKMVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2Sqz85LNXb9qoUdpS1AjsWPbDpS2lqKDbMDCmrxw0ZgIhALCcGlBw0Z8qk5aGmfLLweNcgkjf8rEATkT%2FIzFOMYITKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwE8NrtsiAT%2BFvWYkUq3ANM57oakzc2hrj1YEZriR8QcB2Y9PQfJwObkBF%2Bn8Ip0SiTxvW92ze8pItP8I1o2X0F87xfOjhcm6dxni5dW9u%2FwsKl6%2FCIAM7ZYfrFT%2BCZo2O3QO2Cs2UIdldPANK4U8J1dn5E4LLxSh6uFuKG%2BDRQFBxqrlctdH0TNleJrJBJXc7QBpSNaZ9mPC7qDWU0sF4JjVOOQDjay1MR%2FU4fvT5csgCgv2df47vWgyc2afsro%2Bte7OFf0brKqA3d92a%2B4bk1Ff%2FXEBqngaAaOEDmn6Aaj9i8dluIhmQyxKt5o0hx8nIeN5s2fJqXqgFdNouwMotgcStsy0uFVJP%2BK6Bgw3oCux5yPHb65tm4Y1X3roShfRI1%2FyOcHPhRjNNRn2EcB9rNSk1fbgVEVkJLCdQD0igPzTOR77G3boGq5rG06zuv7wyWvlRqGzDc0Lg8GDaLkhsP9MjnVs2sVj8S0hyi6SnD0p3upA3ANvplHgZMTNHLx1F6jdQio4dVlKmtAJPY8qAstT6y0iFqVOwyK1ghi5JTvoceFYQWqaRz7RFL021%2BHBp52NUjzeD369kOiNcS7Frj2VTNQfFp3OWnt4UdEAs%2F2rBWcLvICQzfAcVYH1NG2MrYy6JXrnBLUL2OPTD0%2BPS8BjqkAcr%2Bpxez1kG%2FsutJIo8FHOsNc8ktGDhO2ULykI%2FoofXUzvHtIBhl2eU9HD%2F7QT2vVtmxjssaQeFMIcfyrqJBKHdY%2Fo%2BhgRAHSA46yHc8Fc1M647PKgjZtGL%2BtJHeHkxz2Qtg1KgOrX6oFvU6LM5wQubjIcKY4ZknPG4gu7xgyFeyVSpmUFZ3co3by8sA2klLgKpEKV9MYqcHOYZqHpuCioudG7Yp&X-Amz-Signature=b522ffedb2f57fefbe56fba96272311c83721386d958f8513310d6aa4c257a46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH5FKMVP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2Sqz85LNXb9qoUdpS1AjsWPbDpS2lqKDbMDCmrxw0ZgIhALCcGlBw0Z8qk5aGmfLLweNcgkjf8rEATkT%2FIzFOMYITKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwE8NrtsiAT%2BFvWYkUq3ANM57oakzc2hrj1YEZriR8QcB2Y9PQfJwObkBF%2Bn8Ip0SiTxvW92ze8pItP8I1o2X0F87xfOjhcm6dxni5dW9u%2FwsKl6%2FCIAM7ZYfrFT%2BCZo2O3QO2Cs2UIdldPANK4U8J1dn5E4LLxSh6uFuKG%2BDRQFBxqrlctdH0TNleJrJBJXc7QBpSNaZ9mPC7qDWU0sF4JjVOOQDjay1MR%2FU4fvT5csgCgv2df47vWgyc2afsro%2Bte7OFf0brKqA3d92a%2B4bk1Ff%2FXEBqngaAaOEDmn6Aaj9i8dluIhmQyxKt5o0hx8nIeN5s2fJqXqgFdNouwMotgcStsy0uFVJP%2BK6Bgw3oCux5yPHb65tm4Y1X3roShfRI1%2FyOcHPhRjNNRn2EcB9rNSk1fbgVEVkJLCdQD0igPzTOR77G3boGq5rG06zuv7wyWvlRqGzDc0Lg8GDaLkhsP9MjnVs2sVj8S0hyi6SnD0p3upA3ANvplHgZMTNHLx1F6jdQio4dVlKmtAJPY8qAstT6y0iFqVOwyK1ghi5JTvoceFYQWqaRz7RFL021%2BHBp52NUjzeD369kOiNcS7Frj2VTNQfFp3OWnt4UdEAs%2F2rBWcLvICQzfAcVYH1NG2MrYy6JXrnBLUL2OPTD0%2BPS8BjqkAcr%2Bpxez1kG%2FsutJIo8FHOsNc8ktGDhO2ULykI%2FoofXUzvHtIBhl2eU9HD%2F7QT2vVtmxjssaQeFMIcfyrqJBKHdY%2Fo%2BhgRAHSA46yHc8Fc1M647PKgjZtGL%2BtJHeHkxz2Qtg1KgOrX6oFvU6LM5wQubjIcKY4ZknPG4gu7xgyFeyVSpmUFZ3co3by8sA2klLgKpEKV9MYqcHOYZqHpuCioudG7Yp&X-Amz-Signature=7395a30fbd6b4b40c2fda49f56913417d2c7acce8ff68b0dcbaaf324d501d2c5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XSBXPRH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBlWIKf5tsEGPBpocEVRUA9NtOPs6wDCIS7atQ1nBwoPAiBLMkWrWEsemvHfg2pKGYTj735O1likh9W7nIEtoMv%2FtSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkzlMs6d5N824Hg3WKtwDXIHjsXoefGWbIbSZ%2FHWwkrsSz%2FQri4D5KWnZK2OR%2FILrLLw8luqCt8p0sAZJ3GBcdNnsjLHFo1kM6b99TLM7wWQn1ERlQSnxSJEp%2BDKPq5zy1Z60DilHRZ0%2BU2ptiuusXfE0lGZka9ib6YO5A91hpJJTMKOmlsNB3B18e3NAvqKJMRleHJgQtx1rLg5hOkPvnCyG7%2Fz0c3EiYoZdKkBG2WU9dZEFqMiP%2Fxj35IaPedrhEo06VcxUkmWWnC9JLvx2Qv9CpjdlPVXuEeLzS8aSGrXxvO%2BaiG%2BgZGgRGGTjXJjxRBav9aqag2NRciRx4fV5XMsgK9%2FFbw4mNFFtl4KoVcZuMbf9Y8h79c%2B9FghPA%2BE2pBDXb3WjL7AZ%2FsDXSUJxAAOJl%2BWhpFP4rMbUQi0oF3jaNAJ%2FQOShR9Z7YPApTrd38PQLIlUqfglay4JBLr7jH%2BbC7Ow5VgZJkpHcTDSw4bGg1fJ6Ow%2FuuQK8zD63nja6TdAU3VkAS%2FE9GlOHDZ1uFJbN3kJFAkP8fkRZlQHApCrcJSU7Q6hfdEViMEnodS6aWYKWo7Pnfgph6lvQG2SQ1uP09XBRJ7BxixTsFoGSb0TjwPIJvsSubARanYNOagEDiM7KWk7%2BT4pWTXAwhfj0vAY6pgETtXx4jCx8HxYV4qhB4ErmyoWYD34nykrMBQGILg8Eoor7Fksr6sH9SG8391JaG49FKBzAEkQaeb5v3dRQYtlfgq%2FwxDeatY9L2M0ADdQYEAFz%2BHfYgKRuYRjS6yO2mmaKPV6DjpsQpYiAWM4UQLjlFJl8UCCQ3QL6dEqk%2BtJjvhNejsE0Re9teDtECJe%2F7z5eM62KYBl3c1Zmk0ky0agrsjz7nCI%2F&X-Amz-Signature=2ffcb3bb64c8cc88606340c9159898f6b728a3f5e3f10370481c6ac2e92c9f0d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672VXE5T4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXSNvyKhijHM3unAEBBdWX0AMRbs3dymCbp6xL%2BefhYQIhAJDPUSNa0kWwgkoYCja6%2F0v25dxaXjl3QptNhBYs3S8iKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmCHwsi%2FmOPt68VnMq3AND%2FtgcXfgZXertpcx2V3BexpX9kYMnJpzP2WIXMCmj3XrAc%2F7TDP%2Fzqo4XjPVIK%2BCCt8aet3sKPUBZXVIIpJlhNqrSjtRb4eKu7bH89d%2BLMH7WScP0fsYbtZyANK0UEJVWEW4wJ1RSVm3OahoWpNfG2RORdZvhq2%2FXf8%2BttCNB0yUoNzLt%2FrKZotpYI7GSYRa6tLfyYF4az8xOQhA%2Bv4jWIFnOHu86fvanB9KQOBuS%2F0bX%2BXMlXCuJeTkbaWWuoMlkplwrl8ixea%2FO155whIpSy%2BCcRhS57yXpWzXOZBokTbYet3isIAh4ZHdwvQgAtNOrToRjXj3%2BGi6ml9G4A6YnZzhcpcOf%2F2XYwmx985IIdz%2FyJY15BUu79LcX0ub78kTX9BY%2BdL21mC6BueD9ueHyn7oy3pqmyHXhhBgryo8LeFa9nX4nsXyK6OC2sVNGQN7%2BfYq8La4KYApY7Y9J4NGp79HfHQOjcDRkRXazgU2m8vDEnc0kSQ9dDp9Y0aw2ApX7kZxnefOskMuGZMRcHEv7jUozklriScKIdqQJ1EMOfHy6CWrNkOEEztm1P%2FSIAZUXbZ1lz2uSEeCFCJFyhS4lvcPC6PCbJ19UUrOjmt0kJk%2FhImF8aWpw92tD5zC9%2BPS8BjqkAfkgAinSHgNpuWDn5fXVcfsPF6%2Bl8bXZghMYK7cP4Bkr5ZKScysxP0j8vI6xG4sezeI14j9J1H2VFyEYTaI1IPlcMG16B%2BVLtXuAshi%2BH8BfGQbQ4qQeKFDG3SK4qkkT8UedOPHZYSPvLSuOg2GiiZmBLLEWFAgL9j525nXgWBEJW6ZJE%2F34cChpOnaVew4mdjN0%2FdOjo1y78FC7Gs8QDORlL4wW&X-Amz-Signature=57f77a9595b9f286b2c7cbe5883826a86e231398893e4803ab1b553da3d2f28d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4YU4GYB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGG90Lvjrg8pFHCYFUYRotNqGzUhysL9ObYWUZjFoCAhAiBtFBqVBxHVwEuIgdN5vhelpZjczydIxEvgAcbn5LmHcCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPcjItXHNFTyTWSy2KtwDDVjREAmiYPBFa5EbjLRmLM5YT9Q%2Fh36SdJ%2B0IfllboApI5Zzx648HoAQDi3%2BTNxeqLPBtvMaHkgzgAH6V5LjEDw516kJlfptHiKEAJgpunau38b6ljN86NMbsY%2BpKtVnnmMpMBd0%2B9N%2B7xGB3Yu5T1ZaTf9cPFvZ0l7vXUddaITJu%2BKASVY07mwTHXu24Izi1MkMzrOh%2FFi8TWiExcukf0k4wJzTLjmyK5QaiMpkwUFtfgikK8pvc%2FsWAEVTCNUcunMmMGBD3%2FRy3J2uFuylbK%2BFBQJnHwBikyax0TjOOhhb%2FO02YrrswXdxQ5kl6%2BJFpo%2BSajsBecpkGMkZwecfue1hANeNZvivJ8ghZs%2B1Bq4mrWnP9BrQkhjrwmHgJWPJwWSU7GYWfZmkqCM9Pwm8YbVt2ZGkt26kY1alISLwCgGaACd8Zwx4qiE04Sm1UCOpeOMkbPyo9zKWzc%2BX8QOLPVfgUVhp1JS0n5TbkTgm%2Frunnb78dZXHEWADMrrHV15oe%2Fl0tfWnA2DEIeD1S4dQuxDJEAxQp5IP95pzb1wGfdepuQWRH6Tn0aE%2BwZebwPsfQ3J2%2Fhey3gur5LqFHGoVpuuszpjz2Nw2yKg2oeiJOAS6J19nk4MsiqSIAm8wvvj0vAY6pgEAzIMBfnHJKInTrSkwBqx%2FMlLu124k6MPqK%2FZWzu%2B5YoWTAKkEVqBtI5Weq6le7r1UXjOI1IkYH34DpNjrzu%2BpO4Ex%2BKufamWVC3NsYT%2FeB9Bx75xdCqrCvD%2B05Yu3JPIk%2BWgw6lzUliG2fclLRmv6qcFeIYSkV62EGY0u75KIur1nyW5VdJDXD4jKeEdOl1FNGweK59SElUxUU7bVXioL%2ByEPr9zv&X-Amz-Signature=08a1f3135e19247d0cafdd782bbe361587404d124757e120445ece7887c55a79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2VAFRUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnFY2ODzkt0WEzVwTHLb3n%2Fb21h1KldTt9EqqI2uJWTAiEAtJv7Jm8SbZGvMhu1GImlF7myHY0bIKVOFCCHgTanXtIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIoQK1%2FZvLyqa%2BMi1ircA5jWPnfAgQonfRhqf%2BJRVgHHDMAuwwOUqMlgGomyNunQEsBvzFU%2BvnJhqbcqurEIsA23ZNunOXVSLb7GvkuFt0dqYeo24RRWklRwFe0BR3l4RWEU%2FQcB2j4yHydZQaDFFaK6xIv1%2Bv1wKTQ%2BE5upvqPIGQitm59hJT77FjIxDP5HOqBI5UEsklxvf5El1LnsxblGurQtXpK6W5AQpzizFFw0XY8pb%2FFwLPyX5U%2Fe%2BEw7b9Irw20PxmCS5JmoN69wiVB5KXLOVz9vSXgMZVBFgdhddUKCI6OSnIo%2BXH1%2FDgAWu9g7daogkYpmOC8Gq8SVTuadJZlSYkfDNI3aV9ePTtrd84CWUGAnEzZcXjkjXj5%2FDqfK6CmXx%2B3zP5AIUIqNiSCyQOU%2FXNCHikyy6Hq08nmuzybUGKoh7b6OmBiC%2FhEumnu6FNRl1ys4ZaSaKOmdoA%2BX6zmyV%2BXsHhlSgRURujq8u6l2SUE2zpHDDU5iMKXgYKHTALYYR7GWnabWJE35%2FahoNz0G6%2FCkNHIkqOfxuXrm5bzMMPsAH0gEKGLHwO9TX0aGwLNl0vAdOvOOu%2Bf5aMsj1f3BPQL5h2HQ4HNImbwDRV5iyZbC5aRhPou6edRQpCJvQqBVPBLtP8kOMMD49LwGOqUB7onaUAtp6kl%2FgdlXjkxToR43UGLmKDiPAQg21DRCFAgo%2Bfm1tnS46K4IGEa1REFmD32%2Bm11tkcpYhAWjJJcxpMtNobcxhA5omov1U9k6t6kkWumzJ%2BnS8VOnlvP%2FJfi9vsWyXFzU%2BTn3n8CqPgT%2FhiWE2QX7IxG6Sj%2BM0g2%2B5sOlCKCnDdtGW1LFkHvJRrgnn7qHIbYJPkvJWFA4Tc52qnzWgqFp&X-Amz-Signature=50637269d39461b49ecc806aa540369338c50d4c62fc695a8e036bdc9dd3bdeb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2VAFRUQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnFY2ODzkt0WEzVwTHLb3n%2Fb21h1KldTt9EqqI2uJWTAiEAtJv7Jm8SbZGvMhu1GImlF7myHY0bIKVOFCCHgTanXtIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIoQK1%2FZvLyqa%2BMi1ircA5jWPnfAgQonfRhqf%2BJRVgHHDMAuwwOUqMlgGomyNunQEsBvzFU%2BvnJhqbcqurEIsA23ZNunOXVSLb7GvkuFt0dqYeo24RRWklRwFe0BR3l4RWEU%2FQcB2j4yHydZQaDFFaK6xIv1%2Bv1wKTQ%2BE5upvqPIGQitm59hJT77FjIxDP5HOqBI5UEsklxvf5El1LnsxblGurQtXpK6W5AQpzizFFw0XY8pb%2FFwLPyX5U%2Fe%2BEw7b9Irw20PxmCS5JmoN69wiVB5KXLOVz9vSXgMZVBFgdhddUKCI6OSnIo%2BXH1%2FDgAWu9g7daogkYpmOC8Gq8SVTuadJZlSYkfDNI3aV9ePTtrd84CWUGAnEzZcXjkjXj5%2FDqfK6CmXx%2B3zP5AIUIqNiSCyQOU%2FXNCHikyy6Hq08nmuzybUGKoh7b6OmBiC%2FhEumnu6FNRl1ys4ZaSaKOmdoA%2BX6zmyV%2BXsHhlSgRURujq8u6l2SUE2zpHDDU5iMKXgYKHTALYYR7GWnabWJE35%2FahoNz0G6%2FCkNHIkqOfxuXrm5bzMMPsAH0gEKGLHwO9TX0aGwLNl0vAdOvOOu%2Bf5aMsj1f3BPQL5h2HQ4HNImbwDRV5iyZbC5aRhPou6edRQpCJvQqBVPBLtP8kOMMD49LwGOqUB7onaUAtp6kl%2FgdlXjkxToR43UGLmKDiPAQg21DRCFAgo%2Bfm1tnS46K4IGEa1REFmD32%2Bm11tkcpYhAWjJJcxpMtNobcxhA5omov1U9k6t6kkWumzJ%2BnS8VOnlvP%2FJfi9vsWyXFzU%2BTn3n8CqPgT%2FhiWE2QX7IxG6Sj%2BM0g2%2B5sOlCKCnDdtGW1LFkHvJRrgnn7qHIbYJPkvJWFA4Tc52qnzWgqFp&X-Amz-Signature=7bce59226b0c71fdaec5691a92399e041f6bbd146176b11df9286de9cf3713ef&X-Amz-SignedHeaders=host&x-id=GetObject)

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
