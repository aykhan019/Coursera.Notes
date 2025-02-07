

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NCMAKWM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDLVGnjXYxHrJGNTQJPK%2F32KWZ0UDgIEi7sQzGvWDRcswIhAN3h0ZGVo2dlfsMmBodkEhPMzXAEw3U%2BFO0EuWuUIyreKv8DCG8QABoMNjM3NDIzMTgzODA1Igy7yn0g3VhyZ0IrAhwq3AOyWLMRL6XxzyhBc6SHquZcfdzM7eO5KgJ5agYvoQ3gQbZ6N6ZQyGGBsJaaRiItCUvZz0us1nuV9trSXScsNlrCeCz5ITgBvrJWyC%2BmT8ZNSiOhLk6osaMNSptNKOI8cW1%2B%2FANEoKi%2FyQWUriz0MURxq%2FRw0ii7T4VESAcHkDZfE8opSgvPlv9LbbLgtKHDSLVFmp9PWgRtfC2RlBO9J9ZutOKU5Yczgryz1enzmzUg1N1ZWzny1cHXi3mCeX8FqBjqiYsO5aFDcgzDljoAkCBjP64QnwScspNpg4DQ9ckcDyjI7g4YJ7bZO%2F6lKRp%2FeSKtBmXvDTKmg2K5oIuxnMFexeaVjRiV0BbaKrlzsXmHkfVwJTXDgh09SjjXnC1EHWmyaHMFepYcqSjOstKmKOuX%2FXTWtVfzqYfoZRMkYpBNZWWWxI12ZuVJ0qJ2Y1vsl7Cl0XbJjuCXskg4sh4P4Up1DTPf0Qlx9r5OujyzQm1JL0p3vF0%2FXkUPwvHxYn9nACUITAkNbjCH2ayujm3l3wYZ1b99e3QyRUqNWC6A5RUrNozeYCMUZp2KYxO15sPr6wcGK0DFFXfs22fc8hMxcNXol52PIpvRlUmdPYYYARlCw8jZQ8hvN1pwgpz91jCZv5a9BjqkATJZmge6a1B87pOcO6qfxA5bFwjRdcER%2BvnPPvLW0%2BGRCfws6Noaaq3FVnLm6fUtr69lRKQSqTlD1mh2PyTk8quNXNXHSS%2Fq0JjhoSn6SBP6nf%2FaPbX%2B3IEC0DCRbT2lWST5N238%2Ffy%2FhRzYxohhSLZLGJulKNk2iNMbx04wR3N%2FaF%2B3t1fZazTZADu50HVA1pR70NcyOmqCiWBetM71JOtE5%2FVW&X-Amz-Signature=9b93be44a80dfb9d8304f846f1f98eec4af063cfcd55bcc19f483d141fac9121&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NCMAKWM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDLVGnjXYxHrJGNTQJPK%2F32KWZ0UDgIEi7sQzGvWDRcswIhAN3h0ZGVo2dlfsMmBodkEhPMzXAEw3U%2BFO0EuWuUIyreKv8DCG8QABoMNjM3NDIzMTgzODA1Igy7yn0g3VhyZ0IrAhwq3AOyWLMRL6XxzyhBc6SHquZcfdzM7eO5KgJ5agYvoQ3gQbZ6N6ZQyGGBsJaaRiItCUvZz0us1nuV9trSXScsNlrCeCz5ITgBvrJWyC%2BmT8ZNSiOhLk6osaMNSptNKOI8cW1%2B%2FANEoKi%2FyQWUriz0MURxq%2FRw0ii7T4VESAcHkDZfE8opSgvPlv9LbbLgtKHDSLVFmp9PWgRtfC2RlBO9J9ZutOKU5Yczgryz1enzmzUg1N1ZWzny1cHXi3mCeX8FqBjqiYsO5aFDcgzDljoAkCBjP64QnwScspNpg4DQ9ckcDyjI7g4YJ7bZO%2F6lKRp%2FeSKtBmXvDTKmg2K5oIuxnMFexeaVjRiV0BbaKrlzsXmHkfVwJTXDgh09SjjXnC1EHWmyaHMFepYcqSjOstKmKOuX%2FXTWtVfzqYfoZRMkYpBNZWWWxI12ZuVJ0qJ2Y1vsl7Cl0XbJjuCXskg4sh4P4Up1DTPf0Qlx9r5OujyzQm1JL0p3vF0%2FXkUPwvHxYn9nACUITAkNbjCH2ayujm3l3wYZ1b99e3QyRUqNWC6A5RUrNozeYCMUZp2KYxO15sPr6wcGK0DFFXfs22fc8hMxcNXol52PIpvRlUmdPYYYARlCw8jZQ8hvN1pwgpz91jCZv5a9BjqkATJZmge6a1B87pOcO6qfxA5bFwjRdcER%2BvnPPvLW0%2BGRCfws6Noaaq3FVnLm6fUtr69lRKQSqTlD1mh2PyTk8quNXNXHSS%2Fq0JjhoSn6SBP6nf%2FaPbX%2B3IEC0DCRbT2lWST5N238%2Ffy%2FhRzYxohhSLZLGJulKNk2iNMbx04wR3N%2FaF%2B3t1fZazTZADu50HVA1pR70NcyOmqCiWBetM71JOtE5%2FVW&X-Amz-Signature=882bbed06e8988e0c87f3da2ce44ff0a2dcb13564857ab310a72dcae9b23f7ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NCMAKWM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDLVGnjXYxHrJGNTQJPK%2F32KWZ0UDgIEi7sQzGvWDRcswIhAN3h0ZGVo2dlfsMmBodkEhPMzXAEw3U%2BFO0EuWuUIyreKv8DCG8QABoMNjM3NDIzMTgzODA1Igy7yn0g3VhyZ0IrAhwq3AOyWLMRL6XxzyhBc6SHquZcfdzM7eO5KgJ5agYvoQ3gQbZ6N6ZQyGGBsJaaRiItCUvZz0us1nuV9trSXScsNlrCeCz5ITgBvrJWyC%2BmT8ZNSiOhLk6osaMNSptNKOI8cW1%2B%2FANEoKi%2FyQWUriz0MURxq%2FRw0ii7T4VESAcHkDZfE8opSgvPlv9LbbLgtKHDSLVFmp9PWgRtfC2RlBO9J9ZutOKU5Yczgryz1enzmzUg1N1ZWzny1cHXi3mCeX8FqBjqiYsO5aFDcgzDljoAkCBjP64QnwScspNpg4DQ9ckcDyjI7g4YJ7bZO%2F6lKRp%2FeSKtBmXvDTKmg2K5oIuxnMFexeaVjRiV0BbaKrlzsXmHkfVwJTXDgh09SjjXnC1EHWmyaHMFepYcqSjOstKmKOuX%2FXTWtVfzqYfoZRMkYpBNZWWWxI12ZuVJ0qJ2Y1vsl7Cl0XbJjuCXskg4sh4P4Up1DTPf0Qlx9r5OujyzQm1JL0p3vF0%2FXkUPwvHxYn9nACUITAkNbjCH2ayujm3l3wYZ1b99e3QyRUqNWC6A5RUrNozeYCMUZp2KYxO15sPr6wcGK0DFFXfs22fc8hMxcNXol52PIpvRlUmdPYYYARlCw8jZQ8hvN1pwgpz91jCZv5a9BjqkATJZmge6a1B87pOcO6qfxA5bFwjRdcER%2BvnPPvLW0%2BGRCfws6Noaaq3FVnLm6fUtr69lRKQSqTlD1mh2PyTk8quNXNXHSS%2Fq0JjhoSn6SBP6nf%2FaPbX%2B3IEC0DCRbT2lWST5N238%2Ffy%2FhRzYxohhSLZLGJulKNk2iNMbx04wR3N%2FaF%2B3t1fZazTZADu50HVA1pR70NcyOmqCiWBetM71JOtE5%2FVW&X-Amz-Signature=d504ec822a352c7b2a9d42ab7de569123d14cd848c61f5f2035d472c182a1e82&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCSOE6MW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwokaQp8g6vDoI78jkhWfkDjCc9gwDqqcmmOnhA7gqrAiEAlGxxDfzOAhGktTJhg68paP5SxfdkQ%2FZlFbcE0Efvpcgq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJ3Wde0SWxRCm2y3tCrcA9c%2BNIKrse3m%2FXD3CNT722WcWH5xKiRFtTc2tX6kSuJc43COUxWVYEzZ4LddCFAPm8vytDwdIlO%2FzZw8a28Exw%2BL2e0aRgX4tLl%2Fpm8YUw5f%2F3aEl5hzd67rp3Z%2FH4tiBfiOu5yY8Ry%2Bmux97%2F1fz4gg9%2FAp2quR1QeyHQNSpJBM1FRfq%2Fje0kDMDOCIuvRsYjuqxbkSfmQVeJgo9ErFpv8DQKgIVtry9JYEd14YJSt3zZIdH%2FxqI7WirBzR%2BTcbwRxXbfXXvTCvureD16K7Fh1BJNxQ7itth1BQqL9MlV3V51iEwFoV4tYRUWVPFDhiK2Zbfy197JTA0yksRxVUKVguejNC2Gf8ir8z%2FwuXe422shGYfT9%2B7BUo2cYzPtIAv%2FEAWi%2B%2BDFOljoigYxs0s%2B8baigbqPnWd7UGevXtIyfTRR4okJOmC9kYC%2Fq3nWhviu8OhlsEQNbUqEk%2Fqr8KxuGPSI8vHVsnC8V%2Fxfme405%2B3SU69sYGY56LsriHT9Dj6A%2FuRfua6OnD0Ej52FxykojrN%2F%2FQRS1hSXLIttFF6gesh2hW%2FPM7jwGsQBteqrcmVi4VQif8%2FYVtAioP8zxmc7I8OZQA1ekhENn125C1aa7ur%2FXf8cE%2F1bttAbr%2FMOy%2Blr0GOqUBdFxIkD4hiqL4qmbUvkm7BGTLk0xPvAEUyqYjGRh%2FzUwA1qxC324P3SXXDxi%2F%2FNFNhRsL%2FJ%2F10d7CwL6opLCiuJrYVNv1Mei4vZZ3WAi2CQ80fT0grYpIJJ5wc%2Fe4dNFJB6NNxX8xL5zWETSLBaMcu6bqXWKBdMg9cyuAQlyARe0gCVmlsvGlXrcOFESt3HTX%2FU2n9rhn3vwDI%2F5D9dAOeZEQlub3&X-Amz-Signature=96fd8dbecb661c23693e784734a42b94ef64033b0a9fc9956acb3cfc580b7787&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCSOE6MW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwokaQp8g6vDoI78jkhWfkDjCc9gwDqqcmmOnhA7gqrAiEAlGxxDfzOAhGktTJhg68paP5SxfdkQ%2FZlFbcE0Efvpcgq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJ3Wde0SWxRCm2y3tCrcA9c%2BNIKrse3m%2FXD3CNT722WcWH5xKiRFtTc2tX6kSuJc43COUxWVYEzZ4LddCFAPm8vytDwdIlO%2FzZw8a28Exw%2BL2e0aRgX4tLl%2Fpm8YUw5f%2F3aEl5hzd67rp3Z%2FH4tiBfiOu5yY8Ry%2Bmux97%2F1fz4gg9%2FAp2quR1QeyHQNSpJBM1FRfq%2Fje0kDMDOCIuvRsYjuqxbkSfmQVeJgo9ErFpv8DQKgIVtry9JYEd14YJSt3zZIdH%2FxqI7WirBzR%2BTcbwRxXbfXXvTCvureD16K7Fh1BJNxQ7itth1BQqL9MlV3V51iEwFoV4tYRUWVPFDhiK2Zbfy197JTA0yksRxVUKVguejNC2Gf8ir8z%2FwuXe422shGYfT9%2B7BUo2cYzPtIAv%2FEAWi%2B%2BDFOljoigYxs0s%2B8baigbqPnWd7UGevXtIyfTRR4okJOmC9kYC%2Fq3nWhviu8OhlsEQNbUqEk%2Fqr8KxuGPSI8vHVsnC8V%2Fxfme405%2B3SU69sYGY56LsriHT9Dj6A%2FuRfua6OnD0Ej52FxykojrN%2F%2FQRS1hSXLIttFF6gesh2hW%2FPM7jwGsQBteqrcmVi4VQif8%2FYVtAioP8zxmc7I8OZQA1ekhENn125C1aa7ur%2FXf8cE%2F1bttAbr%2FMOy%2Blr0GOqUBdFxIkD4hiqL4qmbUvkm7BGTLk0xPvAEUyqYjGRh%2FzUwA1qxC324P3SXXDxi%2F%2FNFNhRsL%2FJ%2F10d7CwL6opLCiuJrYVNv1Mei4vZZ3WAi2CQ80fT0grYpIJJ5wc%2Fe4dNFJB6NNxX8xL5zWETSLBaMcu6bqXWKBdMg9cyuAQlyARe0gCVmlsvGlXrcOFESt3HTX%2FU2n9rhn3vwDI%2F5D9dAOeZEQlub3&X-Amz-Signature=ce689a9e63f687e7b5c219d2f88db41a60a2cf6e1c6bd09d15acc7c09f3bd8a3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCSOE6MW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwokaQp8g6vDoI78jkhWfkDjCc9gwDqqcmmOnhA7gqrAiEAlGxxDfzOAhGktTJhg68paP5SxfdkQ%2FZlFbcE0Efvpcgq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJ3Wde0SWxRCm2y3tCrcA9c%2BNIKrse3m%2FXD3CNT722WcWH5xKiRFtTc2tX6kSuJc43COUxWVYEzZ4LddCFAPm8vytDwdIlO%2FzZw8a28Exw%2BL2e0aRgX4tLl%2Fpm8YUw5f%2F3aEl5hzd67rp3Z%2FH4tiBfiOu5yY8Ry%2Bmux97%2F1fz4gg9%2FAp2quR1QeyHQNSpJBM1FRfq%2Fje0kDMDOCIuvRsYjuqxbkSfmQVeJgo9ErFpv8DQKgIVtry9JYEd14YJSt3zZIdH%2FxqI7WirBzR%2BTcbwRxXbfXXvTCvureD16K7Fh1BJNxQ7itth1BQqL9MlV3V51iEwFoV4tYRUWVPFDhiK2Zbfy197JTA0yksRxVUKVguejNC2Gf8ir8z%2FwuXe422shGYfT9%2B7BUo2cYzPtIAv%2FEAWi%2B%2BDFOljoigYxs0s%2B8baigbqPnWd7UGevXtIyfTRR4okJOmC9kYC%2Fq3nWhviu8OhlsEQNbUqEk%2Fqr8KxuGPSI8vHVsnC8V%2Fxfme405%2B3SU69sYGY56LsriHT9Dj6A%2FuRfua6OnD0Ej52FxykojrN%2F%2FQRS1hSXLIttFF6gesh2hW%2FPM7jwGsQBteqrcmVi4VQif8%2FYVtAioP8zxmc7I8OZQA1ekhENn125C1aa7ur%2FXf8cE%2F1bttAbr%2FMOy%2Blr0GOqUBdFxIkD4hiqL4qmbUvkm7BGTLk0xPvAEUyqYjGRh%2FzUwA1qxC324P3SXXDxi%2F%2FNFNhRsL%2FJ%2F10d7CwL6opLCiuJrYVNv1Mei4vZZ3WAi2CQ80fT0grYpIJJ5wc%2Fe4dNFJB6NNxX8xL5zWETSLBaMcu6bqXWKBdMg9cyuAQlyARe0gCVmlsvGlXrcOFESt3HTX%2FU2n9rhn3vwDI%2F5D9dAOeZEQlub3&X-Amz-Signature=2a9029aa29de73bbe028de0141974a991c15c33d102d2473050e0ea2679b85df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCSOE6MW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwokaQp8g6vDoI78jkhWfkDjCc9gwDqqcmmOnhA7gqrAiEAlGxxDfzOAhGktTJhg68paP5SxfdkQ%2FZlFbcE0Efvpcgq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJ3Wde0SWxRCm2y3tCrcA9c%2BNIKrse3m%2FXD3CNT722WcWH5xKiRFtTc2tX6kSuJc43COUxWVYEzZ4LddCFAPm8vytDwdIlO%2FzZw8a28Exw%2BL2e0aRgX4tLl%2Fpm8YUw5f%2F3aEl5hzd67rp3Z%2FH4tiBfiOu5yY8Ry%2Bmux97%2F1fz4gg9%2FAp2quR1QeyHQNSpJBM1FRfq%2Fje0kDMDOCIuvRsYjuqxbkSfmQVeJgo9ErFpv8DQKgIVtry9JYEd14YJSt3zZIdH%2FxqI7WirBzR%2BTcbwRxXbfXXvTCvureD16K7Fh1BJNxQ7itth1BQqL9MlV3V51iEwFoV4tYRUWVPFDhiK2Zbfy197JTA0yksRxVUKVguejNC2Gf8ir8z%2FwuXe422shGYfT9%2B7BUo2cYzPtIAv%2FEAWi%2B%2BDFOljoigYxs0s%2B8baigbqPnWd7UGevXtIyfTRR4okJOmC9kYC%2Fq3nWhviu8OhlsEQNbUqEk%2Fqr8KxuGPSI8vHVsnC8V%2Fxfme405%2B3SU69sYGY56LsriHT9Dj6A%2FuRfua6OnD0Ej52FxykojrN%2F%2FQRS1hSXLIttFF6gesh2hW%2FPM7jwGsQBteqrcmVi4VQif8%2FYVtAioP8zxmc7I8OZQA1ekhENn125C1aa7ur%2FXf8cE%2F1bttAbr%2FMOy%2Blr0GOqUBdFxIkD4hiqL4qmbUvkm7BGTLk0xPvAEUyqYjGRh%2FzUwA1qxC324P3SXXDxi%2F%2FNFNhRsL%2FJ%2F10d7CwL6opLCiuJrYVNv1Mei4vZZ3WAi2CQ80fT0grYpIJJ5wc%2Fe4dNFJB6NNxX8xL5zWETSLBaMcu6bqXWKBdMg9cyuAQlyARe0gCVmlsvGlXrcOFESt3HTX%2FU2n9rhn3vwDI%2F5D9dAOeZEQlub3&X-Amz-Signature=aea374dffb5a4ae8935d201813d54a23eb24653c87b05d9e4c70654052bad817&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCSOE6MW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwokaQp8g6vDoI78jkhWfkDjCc9gwDqqcmmOnhA7gqrAiEAlGxxDfzOAhGktTJhg68paP5SxfdkQ%2FZlFbcE0Efvpcgq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJ3Wde0SWxRCm2y3tCrcA9c%2BNIKrse3m%2FXD3CNT722WcWH5xKiRFtTc2tX6kSuJc43COUxWVYEzZ4LddCFAPm8vytDwdIlO%2FzZw8a28Exw%2BL2e0aRgX4tLl%2Fpm8YUw5f%2F3aEl5hzd67rp3Z%2FH4tiBfiOu5yY8Ry%2Bmux97%2F1fz4gg9%2FAp2quR1QeyHQNSpJBM1FRfq%2Fje0kDMDOCIuvRsYjuqxbkSfmQVeJgo9ErFpv8DQKgIVtry9JYEd14YJSt3zZIdH%2FxqI7WirBzR%2BTcbwRxXbfXXvTCvureD16K7Fh1BJNxQ7itth1BQqL9MlV3V51iEwFoV4tYRUWVPFDhiK2Zbfy197JTA0yksRxVUKVguejNC2Gf8ir8z%2FwuXe422shGYfT9%2B7BUo2cYzPtIAv%2FEAWi%2B%2BDFOljoigYxs0s%2B8baigbqPnWd7UGevXtIyfTRR4okJOmC9kYC%2Fq3nWhviu8OhlsEQNbUqEk%2Fqr8KxuGPSI8vHVsnC8V%2Fxfme405%2B3SU69sYGY56LsriHT9Dj6A%2FuRfua6OnD0Ej52FxykojrN%2F%2FQRS1hSXLIttFF6gesh2hW%2FPM7jwGsQBteqrcmVi4VQif8%2FYVtAioP8zxmc7I8OZQA1ekhENn125C1aa7ur%2FXf8cE%2F1bttAbr%2FMOy%2Blr0GOqUBdFxIkD4hiqL4qmbUvkm7BGTLk0xPvAEUyqYjGRh%2FzUwA1qxC324P3SXXDxi%2F%2FNFNhRsL%2FJ%2F10d7CwL6opLCiuJrYVNv1Mei4vZZ3WAi2CQ80fT0grYpIJJ5wc%2Fe4dNFJB6NNxX8xL5zWETSLBaMcu6bqXWKBdMg9cyuAQlyARe0gCVmlsvGlXrcOFESt3HTX%2FU2n9rhn3vwDI%2F5D9dAOeZEQlub3&X-Amz-Signature=05751f2a6a0bd7315a446adc674fc414a0327dd185587c2fc6b0bde6c797478e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCSOE6MW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwokaQp8g6vDoI78jkhWfkDjCc9gwDqqcmmOnhA7gqrAiEAlGxxDfzOAhGktTJhg68paP5SxfdkQ%2FZlFbcE0Efvpcgq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJ3Wde0SWxRCm2y3tCrcA9c%2BNIKrse3m%2FXD3CNT722WcWH5xKiRFtTc2tX6kSuJc43COUxWVYEzZ4LddCFAPm8vytDwdIlO%2FzZw8a28Exw%2BL2e0aRgX4tLl%2Fpm8YUw5f%2F3aEl5hzd67rp3Z%2FH4tiBfiOu5yY8Ry%2Bmux97%2F1fz4gg9%2FAp2quR1QeyHQNSpJBM1FRfq%2Fje0kDMDOCIuvRsYjuqxbkSfmQVeJgo9ErFpv8DQKgIVtry9JYEd14YJSt3zZIdH%2FxqI7WirBzR%2BTcbwRxXbfXXvTCvureD16K7Fh1BJNxQ7itth1BQqL9MlV3V51iEwFoV4tYRUWVPFDhiK2Zbfy197JTA0yksRxVUKVguejNC2Gf8ir8z%2FwuXe422shGYfT9%2B7BUo2cYzPtIAv%2FEAWi%2B%2BDFOljoigYxs0s%2B8baigbqPnWd7UGevXtIyfTRR4okJOmC9kYC%2Fq3nWhviu8OhlsEQNbUqEk%2Fqr8KxuGPSI8vHVsnC8V%2Fxfme405%2B3SU69sYGY56LsriHT9Dj6A%2FuRfua6OnD0Ej52FxykojrN%2F%2FQRS1hSXLIttFF6gesh2hW%2FPM7jwGsQBteqrcmVi4VQif8%2FYVtAioP8zxmc7I8OZQA1ekhENn125C1aa7ur%2FXf8cE%2F1bttAbr%2FMOy%2Blr0GOqUBdFxIkD4hiqL4qmbUvkm7BGTLk0xPvAEUyqYjGRh%2FzUwA1qxC324P3SXXDxi%2F%2FNFNhRsL%2FJ%2F10d7CwL6opLCiuJrYVNv1Mei4vZZ3WAi2CQ80fT0grYpIJJ5wc%2Fe4dNFJB6NNxX8xL5zWETSLBaMcu6bqXWKBdMg9cyuAQlyARe0gCVmlsvGlXrcOFESt3HTX%2FU2n9rhn3vwDI%2F5D9dAOeZEQlub3&X-Amz-Signature=e3213bb8b28118d99b8e88faab0a8e11a68d802c046a405d8f201f3738edeaa4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSDYNEQN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCICIhWs9pcNCA9kvgjhCFPduJfP4%2BSirlpWNKWjzOVl49AiBSjTg5%2FhYypknvFvXTn5pMtiQn0A13DO7X2MaWcig16Sr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMtgZRb6RHeuHPC%2B%2BYKtwD9GiOmb9%2FP%2BDnAl1OrO%2BlhCFgLgQ0QQdzpltSq2jjVDO%2BzIQJ5LJe1pYFsfG6WOYlpKCI1%2BhM8ptD4MTILns3%2Fr6J23EXVUf53MIbv4DomZ%2FqAVWc3UZhQlUVoo5SrkQf2bnIjhXGAVWjR%2FcoPsrH%2FusDoFlDjVjKfzgtzxGjIRFsjYStilH8w0E%2BuXmMpdnj2y81mdJbk7Gug1SplKPdnEC0A%2F0ndTVBBKGl19StRTAIpPOGGuk6w6ImUDdq3J6PTnQKU8VGTXPzltgoAFCMbgp558LG3U0cl5cTJuMYopLNTp14zEq%2F2kBFtmf5yHCd0oCpuZfkLB8cu2A1p1XXS9UQc%2BaMyt1enNrfPBm3Olj%2F5vFfRwhUCbQoacgXkS3yShFlyPzSuMU%2FjAujXXSFD6GQx5usqsrfd3%2FZZSlEM2b0Emyx3IJ0ijIcN4LnqT0WtvfH%2F5wobo2yDszKLEDG8tCB%2BkxohuL%2Bpy6%2BSnVAQRmAp5Rw%2B3RJHSU2CjwI7IJdPxzUgXUzLPg5iPy3pzS%2FNNk%2BwEyNwTdI%2B1dPs5WcGWc7L62KThSsdZe%2Bipptg4lrS8LwP1asqjsgTZ49ninmIlIDdWRfqCh8ntg%2Bae85n68gsdH68Zm%2BPM%2BmXYkw1L%2BWvQY6pgFxnCFUKaMPKv210p5ioOdxvrYM2tALr2yfEODTC1vOEuwsbPG1uP8tfrA%2FgkfdYVlqF808DKg1uaWgglmqpqsypmGlcQQ5xyjmz9W0UDf0BlGnEeSzHlS1OxPbTcdU0pS6%2BHjrC47ZhL2tBDoNRti5DDHAqqskCC4wjirRyaliVmmypvMZM3kZ%2B1%2FG885PzSXgnevVa8lC%2FNX4lZV0F4KflgNJtmiJ&X-Amz-Signature=f7ab4d4bb6bcef9a6ab26c87b826d54c84cda03a1f68150c69c03822983b403e&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673DAUNUV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCICYbLaATc4N7nsu9QfRg9VRQ12z9D6txGzWtUolBLBjEAiBIH5SPW1aP83jw25RkmvSt0pGp4WwXR%2Bs30smZv3D9hir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMbWK2kSP2H0NxkO2NKtwDRC1utS8HRXHr3xj2cAPoMpiY9sMm4kz4i6cuDAX31wBsjmTW1yi0%2BHbY%2FRNgXK7UrnGixkdny3BYo%2B2H9zRm71M4DhPqBDRJVd7Ob958dlzIVXF3lgdMr0Lz3K8qsONN0CdnaKamS5INfDrEzq3HgZWOdpoaoSuSupAsOG%2FvfKoVAlhqcyBzoBcuozrWFBezAK9PKq6fgCQop0wSAhvImJKheBIs0BIjjBiSPXhWisbaijCuuo3hE45gZdSkZCyZO1KYBkoInYNBQa%2BXAUzmplT%2BJtmoSM5%2Ff3fx7%2Fh9mCOK17MF8OD37jVR%2FTRZo5%2BYkGPZIr3OwlRWQCpg26nlc0JXluBT7oRdDurILIC%2BFxQWf%2FltVO4iJdyJFXeXvQ9OG8XNOwULHbJZCLXfLYVf6BB10NpcHfzlPOxFDAN5KsyHDUCJy%2FeRo5ayczfjwbM2%2F05CjcB%2B25UADUnBMCD8HpVf2BcDjtFnHUmzd8dstDaa0g6qdqannpwU%2BTqkjYCM5Gc0WIBZo1hIpd5wd%2FoBHMYQ6MTSziC3INzRSCf3jE47bv2NJ%2F6MdJU1vf05SxVti1tWCZpY%2B1UlgyiOELh9NQWBHz5dqMu0P8Or%2FN1UAbU3WfJPzzBJnLLOn4Ewt7%2BWvQY6pgGahHrTf%2FFtHFAwvAH9b%2FyA%2F3%2Fj%2ByTTX87e8%2BE63H%2F9Mh6%2BtKmFH2qDx6duQ8lDclNHI9La1ivrTHoocP5mZDQUS70upww%2BxKoD42l1b9zf%2BP0uqgvsj%2BYBp6jOh9mXnBT4f4jZmRavnDynopBKblbEqWUU%2FJXLnP05%2FIZyyAnwsynbh0x01khyaDd9SFOyQGPYOX5PSnn5MAAq2JXJEVPX0HEbgt0l&X-Amz-Signature=1b458b0928f631a3d33c43b5dd4ff0a4112d68f87721c4ae728e58b38fa1413e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCSOE6MW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwokaQp8g6vDoI78jkhWfkDjCc9gwDqqcmmOnhA7gqrAiEAlGxxDfzOAhGktTJhg68paP5SxfdkQ%2FZlFbcE0Efvpcgq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJ3Wde0SWxRCm2y3tCrcA9c%2BNIKrse3m%2FXD3CNT722WcWH5xKiRFtTc2tX6kSuJc43COUxWVYEzZ4LddCFAPm8vytDwdIlO%2FzZw8a28Exw%2BL2e0aRgX4tLl%2Fpm8YUw5f%2F3aEl5hzd67rp3Z%2FH4tiBfiOu5yY8Ry%2Bmux97%2F1fz4gg9%2FAp2quR1QeyHQNSpJBM1FRfq%2Fje0kDMDOCIuvRsYjuqxbkSfmQVeJgo9ErFpv8DQKgIVtry9JYEd14YJSt3zZIdH%2FxqI7WirBzR%2BTcbwRxXbfXXvTCvureD16K7Fh1BJNxQ7itth1BQqL9MlV3V51iEwFoV4tYRUWVPFDhiK2Zbfy197JTA0yksRxVUKVguejNC2Gf8ir8z%2FwuXe422shGYfT9%2B7BUo2cYzPtIAv%2FEAWi%2B%2BDFOljoigYxs0s%2B8baigbqPnWd7UGevXtIyfTRR4okJOmC9kYC%2Fq3nWhviu8OhlsEQNbUqEk%2Fqr8KxuGPSI8vHVsnC8V%2Fxfme405%2B3SU69sYGY56LsriHT9Dj6A%2FuRfua6OnD0Ej52FxykojrN%2F%2FQRS1hSXLIttFF6gesh2hW%2FPM7jwGsQBteqrcmVi4VQif8%2FYVtAioP8zxmc7I8OZQA1ekhENn125C1aa7ur%2FXf8cE%2F1bttAbr%2FMOy%2Blr0GOqUBdFxIkD4hiqL4qmbUvkm7BGTLk0xPvAEUyqYjGRh%2FzUwA1qxC324P3SXXDxi%2F%2FNFNhRsL%2FJ%2F10d7CwL6opLCiuJrYVNv1Mei4vZZ3WAi2CQ80fT0grYpIJJ5wc%2Fe4dNFJB6NNxX8xL5zWETSLBaMcu6bqXWKBdMg9cyuAQlyARe0gCVmlsvGlXrcOFESt3HTX%2FU2n9rhn3vwDI%2F5D9dAOeZEQlub3&X-Amz-Signature=936d9f0eae301f65c088d4d8323f3287d22efa4a4c56a0dac364f07086c805ad&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCSOE6MW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwokaQp8g6vDoI78jkhWfkDjCc9gwDqqcmmOnhA7gqrAiEAlGxxDfzOAhGktTJhg68paP5SxfdkQ%2FZlFbcE0Efvpcgq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJ3Wde0SWxRCm2y3tCrcA9c%2BNIKrse3m%2FXD3CNT722WcWH5xKiRFtTc2tX6kSuJc43COUxWVYEzZ4LddCFAPm8vytDwdIlO%2FzZw8a28Exw%2BL2e0aRgX4tLl%2Fpm8YUw5f%2F3aEl5hzd67rp3Z%2FH4tiBfiOu5yY8Ry%2Bmux97%2F1fz4gg9%2FAp2quR1QeyHQNSpJBM1FRfq%2Fje0kDMDOCIuvRsYjuqxbkSfmQVeJgo9ErFpv8DQKgIVtry9JYEd14YJSt3zZIdH%2FxqI7WirBzR%2BTcbwRxXbfXXvTCvureD16K7Fh1BJNxQ7itth1BQqL9MlV3V51iEwFoV4tYRUWVPFDhiK2Zbfy197JTA0yksRxVUKVguejNC2Gf8ir8z%2FwuXe422shGYfT9%2B7BUo2cYzPtIAv%2FEAWi%2B%2BDFOljoigYxs0s%2B8baigbqPnWd7UGevXtIyfTRR4okJOmC9kYC%2Fq3nWhviu8OhlsEQNbUqEk%2Fqr8KxuGPSI8vHVsnC8V%2Fxfme405%2B3SU69sYGY56LsriHT9Dj6A%2FuRfua6OnD0Ej52FxykojrN%2F%2FQRS1hSXLIttFF6gesh2hW%2FPM7jwGsQBteqrcmVi4VQif8%2FYVtAioP8zxmc7I8OZQA1ekhENn125C1aa7ur%2FXf8cE%2F1bttAbr%2FMOy%2Blr0GOqUBdFxIkD4hiqL4qmbUvkm7BGTLk0xPvAEUyqYjGRh%2FzUwA1qxC324P3SXXDxi%2F%2FNFNhRsL%2FJ%2F10d7CwL6opLCiuJrYVNv1Mei4vZZ3WAi2CQ80fT0grYpIJJ5wc%2Fe4dNFJB6NNxX8xL5zWETSLBaMcu6bqXWKBdMg9cyuAQlyARe0gCVmlsvGlXrcOFESt3HTX%2FU2n9rhn3vwDI%2F5D9dAOeZEQlub3&X-Amz-Signature=71d8a9cec3b85b0f5010d81b0b05623feb3983ef83ee6304b0340d9e6b5923b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCSOE6MW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwokaQp8g6vDoI78jkhWfkDjCc9gwDqqcmmOnhA7gqrAiEAlGxxDfzOAhGktTJhg68paP5SxfdkQ%2FZlFbcE0Efvpcgq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDJ3Wde0SWxRCm2y3tCrcA9c%2BNIKrse3m%2FXD3CNT722WcWH5xKiRFtTc2tX6kSuJc43COUxWVYEzZ4LddCFAPm8vytDwdIlO%2FzZw8a28Exw%2BL2e0aRgX4tLl%2Fpm8YUw5f%2F3aEl5hzd67rp3Z%2FH4tiBfiOu5yY8Ry%2Bmux97%2F1fz4gg9%2FAp2quR1QeyHQNSpJBM1FRfq%2Fje0kDMDOCIuvRsYjuqxbkSfmQVeJgo9ErFpv8DQKgIVtry9JYEd14YJSt3zZIdH%2FxqI7WirBzR%2BTcbwRxXbfXXvTCvureD16K7Fh1BJNxQ7itth1BQqL9MlV3V51iEwFoV4tYRUWVPFDhiK2Zbfy197JTA0yksRxVUKVguejNC2Gf8ir8z%2FwuXe422shGYfT9%2B7BUo2cYzPtIAv%2FEAWi%2B%2BDFOljoigYxs0s%2B8baigbqPnWd7UGevXtIyfTRR4okJOmC9kYC%2Fq3nWhviu8OhlsEQNbUqEk%2Fqr8KxuGPSI8vHVsnC8V%2Fxfme405%2B3SU69sYGY56LsriHT9Dj6A%2FuRfua6OnD0Ej52FxykojrN%2F%2FQRS1hSXLIttFF6gesh2hW%2FPM7jwGsQBteqrcmVi4VQif8%2FYVtAioP8zxmc7I8OZQA1ekhENn125C1aa7ur%2FXf8cE%2F1bttAbr%2FMOy%2Blr0GOqUBdFxIkD4hiqL4qmbUvkm7BGTLk0xPvAEUyqYjGRh%2FzUwA1qxC324P3SXXDxi%2F%2FNFNhRsL%2FJ%2F10d7CwL6opLCiuJrYVNv1Mei4vZZ3WAi2CQ80fT0grYpIJJ5wc%2Fe4dNFJB6NNxX8xL5zWETSLBaMcu6bqXWKBdMg9cyuAQlyARe0gCVmlsvGlXrcOFESt3HTX%2FU2n9rhn3vwDI%2F5D9dAOeZEQlub3&X-Amz-Signature=94884c9287e97880f7f26e2f6dbe568392978ac5e0cb0f8978369aec777eaded&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZY7ENIA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDWTUGK57d6S8pouzlxZE2SZ9jZlZ%2BI3oc%2BrKYidjPWvAIhAPbYU5qqgzTB3ECvqWKjIh1I5JUtWoLRffMoxmt3Vr79Kv8DCG8QABoMNjM3NDIzMTgzODA1IgxATt5VzyGoWkPfMAIq3AM3CdiegvnJodLp67Rt0LyRss5Yz28%2ByX3VF62qZ%2B2FBZx0LnlnaNySIy0dd46HZI1BS4iEdfCwvZ9txIepaAmQ0nsdkVKtYjKkqMn%2FOC8dbo%2BQw9DTFk5AB5SgywsNoEpDGnIF1vk8%2F83JBWCmtvF%2BT0SpM0gsIWfsg3mLwOJCY3A5%2BUMsxZGo8iKPfQ6MZLd%2BNfiA70eagON1wacYDxk%2BU7DQ0dFC%2FpY3t3IBnBKTvACIpS8NvSE3dfksaZbPrOYv%2BvM95DU72OazyLcP3kFITXkk209Yd4j0IX1D7eOsX8zP9oiwW9cGC8bhyv7W1eDyX9BdmIWLBHTC5hYGQ0xvA45zGfJ%2ByqFrTxF3F05MI3A0%2Fj5roK39mAAxJpR489hPQX7xYa3aWqsVp93L5My6F85af0%2FRB%2FUHOhMdEt8lSQFgDv1Xjdz6Ff7jUU9SYT0wzTsEIgmrYkdorEJFPnL6LpaIdSAStqJPj01kSmrsg4NjkVgV32z%2FofJRtNZx%2FPIu2WeNQZ6IwsmU4E7448Y%2BOXR1ycqIutU2ewn7CZM16c0cgde47QMaViQ4eBRTJf7BzjFVQTSP6ium54dr8N6fXtG%2BnU%2FcGc2mInQMJssLfgDGu5lNi4hMvb87GjCdv5a9BjqkAX3oCB2WO2gGgzdlHrv4eYr3D6M10XH8uzqqWV0YJqxRWG2OwuAINcYw96xT5GDYV8WB9c%2FcjTOAcVNzjR4XSVWWC7T7TsFR9L9zHyfLepcGNfq3WawPzS8djHDkMuj%2FftS9RuPiYZIvf0OKAymuo1eEJkhsrya2vmlP8aUqU7VYq6rFkj1yjCOGwVmqPcdzlP4SJXV7iAp5CJobT22GzLkjMyc9&X-Amz-Signature=9d290dff60aec9e14463d26d9c7b0006e7002dd12f079bbc743af9457d495c11&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LZUN7DI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIEYaAhvyWFKEsKlj3e5JCHsDFHhoM1SNjdRU0yGMZp%2B3AiB6H9GNPxxmKyPKZqgB13eRnn21rASqBTaR%2BEY%2FArvmcir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMkO2Srk8YX8%2F9%2FqerKtwDGEr4ejBmDGiXdFh0gxo30%2BzWzPLwlVUYsFQ73htEALISpTye6pzopJg43WTLWBOXwZEC%2BKLd%2BAmYm9k0BcZ2r2qM8h3pkEomJNZ1RlvvXQrH4HkQru9NSZBTv421ugZTk22MQ8ql5TX4ZaHK0J3dva3UO2kD0STe5rwSxfXz57jiI0PegMJr9%2BbmKGYd2L2bou%2BbbX7yegmLhl68lkPZhw38kGSJfh3vOPDIRNm%2Be88EXNysUessDGwvNYdzppAHWXwsO5iNPkPF73BwuSp27L2qLBQPrXoj7MkJwXlq%2Bqsb2EjEughyYzylY4isT4rlNW5g9dqbMrnKuQq7PwO%2FG5cxbtq1MVdWS0OBIpujAqYJh80Pl0tPC%2B%2FFTIDquK8cL5lNaLiKvKRND7DMmCvb%2FEglnl673QalheV%2BuJJqfB%2FwmUK6KNqlMpvY1F%2FHmDNYSpxr35hsxHLz74oQY7T2fKQru14sFfGBlIHvVoRoG9Zm%2F%2FAsvsKYN3%2Fdt6Z6w92%2F8vG5tbJovn5gorSvr6obHyhwHOrtOGd%2FNdbeAX6Wwu5gxtjl00mU4wXonyAHEvXr93zVV0wTTjSp8j98RwqxcxW%2BgJl%2B8wi%2BpMyZw9OwrLyQjBGIAgfb445sLgYw6r6WvQY6pgED%2FZEXt6Y9qIsjLgDS1291k5CrZR4cV6uG5BB68odvH58X4Hmos3N8mJT4roIG8MrcQyChLzO0n5tRKd10khzqfcSd4Z0q9%2F9Nlp4wvy8tkcsI4tuYRXFA8%2B1SdhkoCTHuqpARQ7m0FinmsmjSEsAzA%2FSfkzcn5%2FNxLMCuC6j6eyn4TWYK6GplKn2OcK49K40NJoW0G5UAEzNRGSPu9AMxKRK2WS4j&X-Amz-Signature=400e78b557e8486389be286d53be97d6e12c90567b8ebbeb8036019db3484d8a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HDJ7LEV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIElHcWJV4VtAikAYqhTNHfamgfTyrimBtlUq9H7J0RyNAiEA3RVi%2FGSEQb%2FlXDB7IsmLE%2F3x6BiSTFnHkgoxfVduQbsq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDH30HvMo8sfx8DWgFyrcA8VraXeMUV01aWO6WpQc2SxSPS0q5wtIpdZCPOvY8ZNJMjraisjpyl4YY6%2BbFhHKeC%2FZ0dRzwLoUpPnyNPdvRgRmJz4rq7wyuRpgr%2BGZo9KhXfb6YUgLbk7BFysZU07Zq%2FARZGMcelg8%2FikrsHNdCVvtjQed4lxwnSpYoQZZTWeOHQ6EkGhxcVzjKfqPeBTfIdocI3AlVFx3VbIJhsBs0Iq%2BHgfdVX7NMWIm9YgAOZCX4pLj0VrUqnhIe9fEVGZUj%2FsFcMlGPezusvCDmJOxflCj4LSlJd6EjamSSKOpLlhjiSghXBXiImJFyVIs7Az3NekZGlNT5wqlYOSE3NYGkmlSM8GHuAVcsOXR%2FPtD7n3aSZLvBdVSTYbfzavE8NAtjQOm5LxtmCtT0%2FJCVszs%2Bmmu%2FnpyGsflFnRVqHgNW%2BNaSZGLinndhv1EQNl8y1SGALw%2F3R%2FaysXSd07Q%2F7VZpymfPW2AU78gTPCswF0FnUcgGL0%2Fdx%2B9QOrFakNXiJol0ZJSyoiQYbmAiuTLZj0UAjN9I1HtEj0ic%2FJKxgBVpgkFzTfbbXvh3GI%2BrZk2aLOatZAea0fv5YvXaEbam2swTrjdGSHoteUqdxvfy47YVvSd0GjQd9wF4smq2hrGMKy%2Flr0GOqUBkeqMW86sdB4BnZr%2BhKrzcOtKL5p8aRh95j6SHCeA17LKP%2BPXesE1m3tvL90rY17P1olZR9QOGNWgGlTuoh2krJgmL2WWsjzHPZsgv5JZMktnBGkkm0wbJDOS7o1Q%2BaFOZQP%2Fika0VYeZ7EalQPY%2FFJTaVG%2FDCv6TP%2BGG3Cm4yjnjVDlsS1kBmbl%2Fflds68cb2M1PADuecPUxHyje9p96URALfs2S&X-Amz-Signature=a11965049eecbff3999f5c0d81aed47f2bd2886cd5fb22aea235239825d7b4e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPJVG3HL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIBrQOgFDTjWaTvC%2B4Si4JlDxR1lUdCd%2BuE3PeXs5dU%2BGAiEA9IOrSb7j09IiT%2BUOc0geVk%2FB4GhW9sZeU%2BKx3B2feBMq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDK7fwRGM%2FsaY18qzcSrcA3Ri5LhxqBVOhlLzplXC%2BojkZgpP3VFWAyx7oPxTv88fr86WSUjRRl%2B75Y6hX6yxB8y17eIUaDFayuWMwkcXS94%2FKol1hEV7Jf%2BT4nsnE2yrCxFfJhBD8ifZD4f7MstCBbY5dBkrXsDF9ZCpGabm9NHpspMOQBeSQ%2B0jP3JYn9PEgj785WmH5OAEjYzCvFjmTQ3xdaQfC6Bg6OcfQxh8M6T2zgegE3grXIF5%2FLUaLcbcvNAGXwKVybXXmyhmmsW67RIOsWmCe3jBNNTYv0y74qyFjdRtBMuzsSX7BCWJINi%2B65krVea0kzT2QCOkjfjhdmtcQIxI9apPSX%2FnpvhzebNzOloW%2FjIDE2Dd3SfPWrcQJStXhQqqXQ%2FZEtWfbOa4VNffmX%2BCtzM4ZTn%2BQ%2FnhgwFX2wmubrAq7eGXHBr9MIxi6rWC%2BEVLq65XmnQRUv3A7mFXysdWoHXi1llvsoa334v8ZLiWb2rhjd9oHFB8fQxdJLHG9RUv0XTYDFhiMt71lrJzFQPveVIn7LeyPvn8Hyi6OVZ3uGwP71qUiHvt1fSHm3vsAeSaUZGTKqbXkYgNzt5bcNI2gxc9fCuGXQ3MPJY4Fyh2OcnkpiFPBI4%2Ffe1RuQVkRCLZLSCCmJtSMIu%2Flr0GOqUBlB3vAgNBe5oiKLdVcw7BHg77pGuu%2B9fXrF%2FgvcQycj39ul7UY0lpdCM5Kh5rP7Xxssm5%2F4%2BjzjEvy8IHNcym6DNLt2q6hWe4SFKEFixwHyVmCl9dVfVX9zRH0E6YXU9wPfQkSBL8HpLMOIoR7TQog78GaCtMBRK%2BsL4jN4SCxy2kD5oHNWKmGAwQwc3aZxjGkhNnNnz3GcSFj6l%2FYOT%2B5YEzZvUD&X-Amz-Signature=e7a62b759b5bf2a91734197a501473aa7740e733832d6bf8f4f8c72d29b6a70c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPJVG3HL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIBrQOgFDTjWaTvC%2B4Si4JlDxR1lUdCd%2BuE3PeXs5dU%2BGAiEA9IOrSb7j09IiT%2BUOc0geVk%2FB4GhW9sZeU%2BKx3B2feBMq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDK7fwRGM%2FsaY18qzcSrcA3Ri5LhxqBVOhlLzplXC%2BojkZgpP3VFWAyx7oPxTv88fr86WSUjRRl%2B75Y6hX6yxB8y17eIUaDFayuWMwkcXS94%2FKol1hEV7Jf%2BT4nsnE2yrCxFfJhBD8ifZD4f7MstCBbY5dBkrXsDF9ZCpGabm9NHpspMOQBeSQ%2B0jP3JYn9PEgj785WmH5OAEjYzCvFjmTQ3xdaQfC6Bg6OcfQxh8M6T2zgegE3grXIF5%2FLUaLcbcvNAGXwKVybXXmyhmmsW67RIOsWmCe3jBNNTYv0y74qyFjdRtBMuzsSX7BCWJINi%2B65krVea0kzT2QCOkjfjhdmtcQIxI9apPSX%2FnpvhzebNzOloW%2FjIDE2Dd3SfPWrcQJStXhQqqXQ%2FZEtWfbOa4VNffmX%2BCtzM4ZTn%2BQ%2FnhgwFX2wmubrAq7eGXHBr9MIxi6rWC%2BEVLq65XmnQRUv3A7mFXysdWoHXi1llvsoa334v8ZLiWb2rhjd9oHFB8fQxdJLHG9RUv0XTYDFhiMt71lrJzFQPveVIn7LeyPvn8Hyi6OVZ3uGwP71qUiHvt1fSHm3vsAeSaUZGTKqbXkYgNzt5bcNI2gxc9fCuGXQ3MPJY4Fyh2OcnkpiFPBI4%2Ffe1RuQVkRCLZLSCCmJtSMIu%2Flr0GOqUBlB3vAgNBe5oiKLdVcw7BHg77pGuu%2B9fXrF%2FgvcQycj39ul7UY0lpdCM5Kh5rP7Xxssm5%2F4%2BjzjEvy8IHNcym6DNLt2q6hWe4SFKEFixwHyVmCl9dVfVX9zRH0E6YXU9wPfQkSBL8HpLMOIoR7TQog78GaCtMBRK%2BsL4jN4SCxy2kD5oHNWKmGAwQwc3aZxjGkhNnNnz3GcSFj6l%2FYOT%2B5YEzZvUD&X-Amz-Signature=c59c4eb410f15a1b6c4deaf6514c2b14a352792e24dbcbd4f9bfff79615986c7&X-Amz-SignedHeaders=host&x-id=GetObject)

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
