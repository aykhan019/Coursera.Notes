

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QP3CW4D%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2B2EORTZcBEF929bfA5R2GIgPxQJpDjLKC3Z37w8FglAIgeMqdofv7mwItRCYbfAjhS0pmFz2t%2FXbNmB17Gy8I%2FPgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQqmIcHTBGpTD9QwSrcA2r9v0K%2FmId3DhSs5kYjpv9VwRVafstuF95HIsvnQscR1d3sw1MPs26lpPz9%2FBGo5hKfovdeJ8o1z0yCpDZHsfKLc5xHeUlKi%2BrMF0AiznWUqEpGaji7g4epBwoav3OIpkHpMDGn4fe5lLYpWs%2F66QkxtQ2o72xqffe6Gw9UkuYwOtxo1R1Q93LQLN%2FhpY0eHMUYQCIujdN6fuAL%2BDm2THas%2BGYYFdrNoffWP4%2FJ9rcql98QbQRj%2FzzzfPo9vErqFVf8JsDDiKCweHxh2978TmwMWLjKO%2BOxnAHYJ05F5EYNVsVRbypUC2jJThWHrTeinzK1FzGgOE38V5yc8XtDYaO3tj2uJEOetXUH839kZLygi5nCUl%2BONoclR6uK6cAYvzDHSq30fuPVuqLzaU%2BrlvH3UZWmw85POnGLWcQ1kR3k4YDpaLsY6h%2FpYYM2dC2gf4R8S3jLIPXgCms7ByE7j%2FMOAxDbosZLF2VSAb%2B3Gtpuo2RwGTuBuRlp1l8PZ5NADXSOWhs0v%2FcRkoX7VxDg4EicMXzWf9tTAofmH8MWTepM3H2r%2FWpkCGmWBYWcY5LxY2UgcVAzqk3m9uyUqzEBHPrld6Miq%2B35%2F0Y9OVGRn6six5RpnrspikEeaKV9MOik97wGOqUBSFeajtw0ccxZcWSJWguSQXOuVRR5YeGzWQReaogS%2FiGxCb2K%2FjI%2Fp%2FE8EfH8Yt%2FaSeZJQU0a4vdla5ThoooLQOANCdfZ6Y7KAQJz5wuv1qjQzsRM8JQgl51aFyQBBHRZeNPe2%2Bmqf2LhZD4IU%2FuppXIg39g0P%2FRQLkvCtQ%2Ba3Jop2HhMOmUqT7oBEOs8dSfzr9lh3ly%2FW8BUguaXlZvLXcABf6PH&X-Amz-Signature=12fb92512d39fbf9ad2413034c4c5167c7ea9af46cdb9870368bad64caaf3109&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QP3CW4D%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2B2EORTZcBEF929bfA5R2GIgPxQJpDjLKC3Z37w8FglAIgeMqdofv7mwItRCYbfAjhS0pmFz2t%2FXbNmB17Gy8I%2FPgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQqmIcHTBGpTD9QwSrcA2r9v0K%2FmId3DhSs5kYjpv9VwRVafstuF95HIsvnQscR1d3sw1MPs26lpPz9%2FBGo5hKfovdeJ8o1z0yCpDZHsfKLc5xHeUlKi%2BrMF0AiznWUqEpGaji7g4epBwoav3OIpkHpMDGn4fe5lLYpWs%2F66QkxtQ2o72xqffe6Gw9UkuYwOtxo1R1Q93LQLN%2FhpY0eHMUYQCIujdN6fuAL%2BDm2THas%2BGYYFdrNoffWP4%2FJ9rcql98QbQRj%2FzzzfPo9vErqFVf8JsDDiKCweHxh2978TmwMWLjKO%2BOxnAHYJ05F5EYNVsVRbypUC2jJThWHrTeinzK1FzGgOE38V5yc8XtDYaO3tj2uJEOetXUH839kZLygi5nCUl%2BONoclR6uK6cAYvzDHSq30fuPVuqLzaU%2BrlvH3UZWmw85POnGLWcQ1kR3k4YDpaLsY6h%2FpYYM2dC2gf4R8S3jLIPXgCms7ByE7j%2FMOAxDbosZLF2VSAb%2B3Gtpuo2RwGTuBuRlp1l8PZ5NADXSOWhs0v%2FcRkoX7VxDg4EicMXzWf9tTAofmH8MWTepM3H2r%2FWpkCGmWBYWcY5LxY2UgcVAzqk3m9uyUqzEBHPrld6Miq%2B35%2F0Y9OVGRn6six5RpnrspikEeaKV9MOik97wGOqUBSFeajtw0ccxZcWSJWguSQXOuVRR5YeGzWQReaogS%2FiGxCb2K%2FjI%2Fp%2FE8EfH8Yt%2FaSeZJQU0a4vdla5ThoooLQOANCdfZ6Y7KAQJz5wuv1qjQzsRM8JQgl51aFyQBBHRZeNPe2%2Bmqf2LhZD4IU%2FuppXIg39g0P%2FRQLkvCtQ%2Ba3Jop2HhMOmUqT7oBEOs8dSfzr9lh3ly%2FW8BUguaXlZvLXcABf6PH&X-Amz-Signature=7873815fefdbc3f4c8c89f2ff34418718fd6ccb2c0c54fe092d5180f15da8c14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QP3CW4D%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2B2EORTZcBEF929bfA5R2GIgPxQJpDjLKC3Z37w8FglAIgeMqdofv7mwItRCYbfAjhS0pmFz2t%2FXbNmB17Gy8I%2FPgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQqmIcHTBGpTD9QwSrcA2r9v0K%2FmId3DhSs5kYjpv9VwRVafstuF95HIsvnQscR1d3sw1MPs26lpPz9%2FBGo5hKfovdeJ8o1z0yCpDZHsfKLc5xHeUlKi%2BrMF0AiznWUqEpGaji7g4epBwoav3OIpkHpMDGn4fe5lLYpWs%2F66QkxtQ2o72xqffe6Gw9UkuYwOtxo1R1Q93LQLN%2FhpY0eHMUYQCIujdN6fuAL%2BDm2THas%2BGYYFdrNoffWP4%2FJ9rcql98QbQRj%2FzzzfPo9vErqFVf8JsDDiKCweHxh2978TmwMWLjKO%2BOxnAHYJ05F5EYNVsVRbypUC2jJThWHrTeinzK1FzGgOE38V5yc8XtDYaO3tj2uJEOetXUH839kZLygi5nCUl%2BONoclR6uK6cAYvzDHSq30fuPVuqLzaU%2BrlvH3UZWmw85POnGLWcQ1kR3k4YDpaLsY6h%2FpYYM2dC2gf4R8S3jLIPXgCms7ByE7j%2FMOAxDbosZLF2VSAb%2B3Gtpuo2RwGTuBuRlp1l8PZ5NADXSOWhs0v%2FcRkoX7VxDg4EicMXzWf9tTAofmH8MWTepM3H2r%2FWpkCGmWBYWcY5LxY2UgcVAzqk3m9uyUqzEBHPrld6Miq%2B35%2F0Y9OVGRn6six5RpnrspikEeaKV9MOik97wGOqUBSFeajtw0ccxZcWSJWguSQXOuVRR5YeGzWQReaogS%2FiGxCb2K%2FjI%2Fp%2FE8EfH8Yt%2FaSeZJQU0a4vdla5ThoooLQOANCdfZ6Y7KAQJz5wuv1qjQzsRM8JQgl51aFyQBBHRZeNPe2%2Bmqf2LhZD4IU%2FuppXIg39g0P%2FRQLkvCtQ%2Ba3Jop2HhMOmUqT7oBEOs8dSfzr9lh3ly%2FW8BUguaXlZvLXcABf6PH&X-Amz-Signature=a20d0b06fe5e5d9906ec6ea97d4c13a8822e4471314c1637234b769be31a9fe9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULIJ4GK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBzh41L%2BiJqlDYLT0PrkbCUeH4ZU2WRB7N%2BSMbz9%2BSzQIgdIHIhUuWLo8ucZjFU2JojZMklMbBpE%2B7RhPQbedCUHYqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqHeoE1aw71HI3U0yrcA2JccQPxUfxQVyoH%2BGpA1%2BHFQqrsSCds7P4JIoZd8NrFxBphY2ONzD5qwssdFtuFVvKWuNK5Rk2GMNrbWWKXeg8QjM8lFVpzMxTY33rHvIL69XNl3waPBo4o%2FxIDKtl4AwIGIhBf7ImgnGI4azH%2B2PoNtHyW7JkTe%2Fp7nzF8n%2BAq2Qgpx%2FRwafg5lfxnbzAMaBXIiK91pm%2BaFl5XqkJKCVL%2FMICzC%2BOnZe6Q0DGEwK2xkfA8w%2BoDHNU67G0v%2B2ki0wDyo%2BQ%2BLtcQyVYjEIXdziLOJBQ3cWzce16THGCJGq3KWCcIKG6t%2F4LkKac4ArWvzNVHBvolqulMXFtwwkkMLHeQkojZcS9B%2FcRncpDW2Sr73%2B5KPN79g9cTu6Q%2FoO0FM67cmXgvWygF111bEpqW2pb7LIsWIz7WIR7QP9OBWFNNVUU%2FSrtejJiio%2BQ%2F%2Bkq%2F6lI%2BeNWIcFI4hMSC7xgSzxcELg3krV64d0PaBStH2olwIk0x5ScZlSWAb6mrrraxp8qnFvr46ij2r3H7vLzNzwZHHNVSgPcoIbeKae8BxV2%2F3O2gbLiPXCZPQ9LmWNRIMNFhjteVpDZopG1PXkkMv7HkhDR0jg0DVmOE2%2FRTyK7QmW%2BDCE35nhk%2BKh%2FoMPfN97wGOqUBzZsMnuz1n5ipe9TNMyMijEk0Ai6K7XQmG1MMhNgjhEvxckwpLt%2FaN%2FY7N7c1JWEq6zyct9xPpQcK%2B%2F4WaCNizYWdK6UDC7axkjPEG%2Fc%2BX%2FxZ1PjMX8bTi6Q7WnO1gkD9%2BYRsEC1RtCB6dMrpmpWy6v7X36bQI%2BY1rKniBrlRDWdjPfkSc3iPomzSL1YVhgwdrUTz9wA0F2Stzw%2BswZdezCBKmRPN&X-Amz-Signature=5ce8a8605b7f6ce36b191a8a0511cfae56cf31799b8f527cfe691f388a7dcc06&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULIJ4GK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBzh41L%2BiJqlDYLT0PrkbCUeH4ZU2WRB7N%2BSMbz9%2BSzQIgdIHIhUuWLo8ucZjFU2JojZMklMbBpE%2B7RhPQbedCUHYqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqHeoE1aw71HI3U0yrcA2JccQPxUfxQVyoH%2BGpA1%2BHFQqrsSCds7P4JIoZd8NrFxBphY2ONzD5qwssdFtuFVvKWuNK5Rk2GMNrbWWKXeg8QjM8lFVpzMxTY33rHvIL69XNl3waPBo4o%2FxIDKtl4AwIGIhBf7ImgnGI4azH%2B2PoNtHyW7JkTe%2Fp7nzF8n%2BAq2Qgpx%2FRwafg5lfxnbzAMaBXIiK91pm%2BaFl5XqkJKCVL%2FMICzC%2BOnZe6Q0DGEwK2xkfA8w%2BoDHNU67G0v%2B2ki0wDyo%2BQ%2BLtcQyVYjEIXdziLOJBQ3cWzce16THGCJGq3KWCcIKG6t%2F4LkKac4ArWvzNVHBvolqulMXFtwwkkMLHeQkojZcS9B%2FcRncpDW2Sr73%2B5KPN79g9cTu6Q%2FoO0FM67cmXgvWygF111bEpqW2pb7LIsWIz7WIR7QP9OBWFNNVUU%2FSrtejJiio%2BQ%2F%2Bkq%2F6lI%2BeNWIcFI4hMSC7xgSzxcELg3krV64d0PaBStH2olwIk0x5ScZlSWAb6mrrraxp8qnFvr46ij2r3H7vLzNzwZHHNVSgPcoIbeKae8BxV2%2F3O2gbLiPXCZPQ9LmWNRIMNFhjteVpDZopG1PXkkMv7HkhDR0jg0DVmOE2%2FRTyK7QmW%2BDCE35nhk%2BKh%2FoMPfN97wGOqUBzZsMnuz1n5ipe9TNMyMijEk0Ai6K7XQmG1MMhNgjhEvxckwpLt%2FaN%2FY7N7c1JWEq6zyct9xPpQcK%2B%2F4WaCNizYWdK6UDC7axkjPEG%2Fc%2BX%2FxZ1PjMX8bTi6Q7WnO1gkD9%2BYRsEC1RtCB6dMrpmpWy6v7X36bQI%2BY1rKniBrlRDWdjPfkSc3iPomzSL1YVhgwdrUTz9wA0F2Stzw%2BswZdezCBKmRPN&X-Amz-Signature=842f8699f8b770a1a2a68f1a3424eba2fa194adeea96ebfb3083be3aa082ca4c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULIJ4GK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBzh41L%2BiJqlDYLT0PrkbCUeH4ZU2WRB7N%2BSMbz9%2BSzQIgdIHIhUuWLo8ucZjFU2JojZMklMbBpE%2B7RhPQbedCUHYqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqHeoE1aw71HI3U0yrcA2JccQPxUfxQVyoH%2BGpA1%2BHFQqrsSCds7P4JIoZd8NrFxBphY2ONzD5qwssdFtuFVvKWuNK5Rk2GMNrbWWKXeg8QjM8lFVpzMxTY33rHvIL69XNl3waPBo4o%2FxIDKtl4AwIGIhBf7ImgnGI4azH%2B2PoNtHyW7JkTe%2Fp7nzF8n%2BAq2Qgpx%2FRwafg5lfxnbzAMaBXIiK91pm%2BaFl5XqkJKCVL%2FMICzC%2BOnZe6Q0DGEwK2xkfA8w%2BoDHNU67G0v%2B2ki0wDyo%2BQ%2BLtcQyVYjEIXdziLOJBQ3cWzce16THGCJGq3KWCcIKG6t%2F4LkKac4ArWvzNVHBvolqulMXFtwwkkMLHeQkojZcS9B%2FcRncpDW2Sr73%2B5KPN79g9cTu6Q%2FoO0FM67cmXgvWygF111bEpqW2pb7LIsWIz7WIR7QP9OBWFNNVUU%2FSrtejJiio%2BQ%2F%2Bkq%2F6lI%2BeNWIcFI4hMSC7xgSzxcELg3krV64d0PaBStH2olwIk0x5ScZlSWAb6mrrraxp8qnFvr46ij2r3H7vLzNzwZHHNVSgPcoIbeKae8BxV2%2F3O2gbLiPXCZPQ9LmWNRIMNFhjteVpDZopG1PXkkMv7HkhDR0jg0DVmOE2%2FRTyK7QmW%2BDCE35nhk%2BKh%2FoMPfN97wGOqUBzZsMnuz1n5ipe9TNMyMijEk0Ai6K7XQmG1MMhNgjhEvxckwpLt%2FaN%2FY7N7c1JWEq6zyct9xPpQcK%2B%2F4WaCNizYWdK6UDC7axkjPEG%2Fc%2BX%2FxZ1PjMX8bTi6Q7WnO1gkD9%2BYRsEC1RtCB6dMrpmpWy6v7X36bQI%2BY1rKniBrlRDWdjPfkSc3iPomzSL1YVhgwdrUTz9wA0F2Stzw%2BswZdezCBKmRPN&X-Amz-Signature=e6d320f7f8d402f19ec0fd14fb52761142e7818c6fd38215dd8c78b5e8d61046&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULIJ4GK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBzh41L%2BiJqlDYLT0PrkbCUeH4ZU2WRB7N%2BSMbz9%2BSzQIgdIHIhUuWLo8ucZjFU2JojZMklMbBpE%2B7RhPQbedCUHYqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqHeoE1aw71HI3U0yrcA2JccQPxUfxQVyoH%2BGpA1%2BHFQqrsSCds7P4JIoZd8NrFxBphY2ONzD5qwssdFtuFVvKWuNK5Rk2GMNrbWWKXeg8QjM8lFVpzMxTY33rHvIL69XNl3waPBo4o%2FxIDKtl4AwIGIhBf7ImgnGI4azH%2B2PoNtHyW7JkTe%2Fp7nzF8n%2BAq2Qgpx%2FRwafg5lfxnbzAMaBXIiK91pm%2BaFl5XqkJKCVL%2FMICzC%2BOnZe6Q0DGEwK2xkfA8w%2BoDHNU67G0v%2B2ki0wDyo%2BQ%2BLtcQyVYjEIXdziLOJBQ3cWzce16THGCJGq3KWCcIKG6t%2F4LkKac4ArWvzNVHBvolqulMXFtwwkkMLHeQkojZcS9B%2FcRncpDW2Sr73%2B5KPN79g9cTu6Q%2FoO0FM67cmXgvWygF111bEpqW2pb7LIsWIz7WIR7QP9OBWFNNVUU%2FSrtejJiio%2BQ%2F%2Bkq%2F6lI%2BeNWIcFI4hMSC7xgSzxcELg3krV64d0PaBStH2olwIk0x5ScZlSWAb6mrrraxp8qnFvr46ij2r3H7vLzNzwZHHNVSgPcoIbeKae8BxV2%2F3O2gbLiPXCZPQ9LmWNRIMNFhjteVpDZopG1PXkkMv7HkhDR0jg0DVmOE2%2FRTyK7QmW%2BDCE35nhk%2BKh%2FoMPfN97wGOqUBzZsMnuz1n5ipe9TNMyMijEk0Ai6K7XQmG1MMhNgjhEvxckwpLt%2FaN%2FY7N7c1JWEq6zyct9xPpQcK%2B%2F4WaCNizYWdK6UDC7axkjPEG%2Fc%2BX%2FxZ1PjMX8bTi6Q7WnO1gkD9%2BYRsEC1RtCB6dMrpmpWy6v7X36bQI%2BY1rKniBrlRDWdjPfkSc3iPomzSL1YVhgwdrUTz9wA0F2Stzw%2BswZdezCBKmRPN&X-Amz-Signature=f08b25f6a922dcd67acd3f2a3971b6477aa1088bdacda50d169ccf32af8e88a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULIJ4GK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBzh41L%2BiJqlDYLT0PrkbCUeH4ZU2WRB7N%2BSMbz9%2BSzQIgdIHIhUuWLo8ucZjFU2JojZMklMbBpE%2B7RhPQbedCUHYqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqHeoE1aw71HI3U0yrcA2JccQPxUfxQVyoH%2BGpA1%2BHFQqrsSCds7P4JIoZd8NrFxBphY2ONzD5qwssdFtuFVvKWuNK5Rk2GMNrbWWKXeg8QjM8lFVpzMxTY33rHvIL69XNl3waPBo4o%2FxIDKtl4AwIGIhBf7ImgnGI4azH%2B2PoNtHyW7JkTe%2Fp7nzF8n%2BAq2Qgpx%2FRwafg5lfxnbzAMaBXIiK91pm%2BaFl5XqkJKCVL%2FMICzC%2BOnZe6Q0DGEwK2xkfA8w%2BoDHNU67G0v%2B2ki0wDyo%2BQ%2BLtcQyVYjEIXdziLOJBQ3cWzce16THGCJGq3KWCcIKG6t%2F4LkKac4ArWvzNVHBvolqulMXFtwwkkMLHeQkojZcS9B%2FcRncpDW2Sr73%2B5KPN79g9cTu6Q%2FoO0FM67cmXgvWygF111bEpqW2pb7LIsWIz7WIR7QP9OBWFNNVUU%2FSrtejJiio%2BQ%2F%2Bkq%2F6lI%2BeNWIcFI4hMSC7xgSzxcELg3krV64d0PaBStH2olwIk0x5ScZlSWAb6mrrraxp8qnFvr46ij2r3H7vLzNzwZHHNVSgPcoIbeKae8BxV2%2F3O2gbLiPXCZPQ9LmWNRIMNFhjteVpDZopG1PXkkMv7HkhDR0jg0DVmOE2%2FRTyK7QmW%2BDCE35nhk%2BKh%2FoMPfN97wGOqUBzZsMnuz1n5ipe9TNMyMijEk0Ai6K7XQmG1MMhNgjhEvxckwpLt%2FaN%2FY7N7c1JWEq6zyct9xPpQcK%2B%2F4WaCNizYWdK6UDC7axkjPEG%2Fc%2BX%2FxZ1PjMX8bTi6Q7WnO1gkD9%2BYRsEC1RtCB6dMrpmpWy6v7X36bQI%2BY1rKniBrlRDWdjPfkSc3iPomzSL1YVhgwdrUTz9wA0F2Stzw%2BswZdezCBKmRPN&X-Amz-Signature=383819e88b060be8562f1cefe75cd8b5f2d3c49645df077d7ea91327e5c5e190&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULIJ4GK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBzh41L%2BiJqlDYLT0PrkbCUeH4ZU2WRB7N%2BSMbz9%2BSzQIgdIHIhUuWLo8ucZjFU2JojZMklMbBpE%2B7RhPQbedCUHYqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqHeoE1aw71HI3U0yrcA2JccQPxUfxQVyoH%2BGpA1%2BHFQqrsSCds7P4JIoZd8NrFxBphY2ONzD5qwssdFtuFVvKWuNK5Rk2GMNrbWWKXeg8QjM8lFVpzMxTY33rHvIL69XNl3waPBo4o%2FxIDKtl4AwIGIhBf7ImgnGI4azH%2B2PoNtHyW7JkTe%2Fp7nzF8n%2BAq2Qgpx%2FRwafg5lfxnbzAMaBXIiK91pm%2BaFl5XqkJKCVL%2FMICzC%2BOnZe6Q0DGEwK2xkfA8w%2BoDHNU67G0v%2B2ki0wDyo%2BQ%2BLtcQyVYjEIXdziLOJBQ3cWzce16THGCJGq3KWCcIKG6t%2F4LkKac4ArWvzNVHBvolqulMXFtwwkkMLHeQkojZcS9B%2FcRncpDW2Sr73%2B5KPN79g9cTu6Q%2FoO0FM67cmXgvWygF111bEpqW2pb7LIsWIz7WIR7QP9OBWFNNVUU%2FSrtejJiio%2BQ%2F%2Bkq%2F6lI%2BeNWIcFI4hMSC7xgSzxcELg3krV64d0PaBStH2olwIk0x5ScZlSWAb6mrrraxp8qnFvr46ij2r3H7vLzNzwZHHNVSgPcoIbeKae8BxV2%2F3O2gbLiPXCZPQ9LmWNRIMNFhjteVpDZopG1PXkkMv7HkhDR0jg0DVmOE2%2FRTyK7QmW%2BDCE35nhk%2BKh%2FoMPfN97wGOqUBzZsMnuz1n5ipe9TNMyMijEk0Ai6K7XQmG1MMhNgjhEvxckwpLt%2FaN%2FY7N7c1JWEq6zyct9xPpQcK%2B%2F4WaCNizYWdK6UDC7axkjPEG%2Fc%2BX%2FxZ1PjMX8bTi6Q7WnO1gkD9%2BYRsEC1RtCB6dMrpmpWy6v7X36bQI%2BY1rKniBrlRDWdjPfkSc3iPomzSL1YVhgwdrUTz9wA0F2Stzw%2BswZdezCBKmRPN&X-Amz-Signature=1f1b2752fed6fa0abf7d3b0a7337f7637d6e2ca427bbb0f9f1829bedaa2068d1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666I5RK3QU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbecw6OLBPvpOXN3pf6XwRS20136xOuimLrsUDlvecsAiEAp7Jyn%2FNmwYZJc7DAAXnkH2AzK27dbU48c8tI48poOiQqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGRdpw1KvQlEBcXXiSrcA8Ha2YdnjJhmrIpfrmCeCvYvB28JUTvOphDQ%2FXAFBSQ6KLyV79us9Sv41ZkkOqu8RN64jIq3lpsn5l1YN9zLutmw61GM0gvSdlk96JJyaGJkppQ%2FGYCy3QIdSWwifqrwDNzDuVOVOennZOLBiaRTS5RoodfCTZMOZNxPsGHTkHwqncF38WTGiqhTi4UGHUe3LQ3jZwfwfGeVsL6H%2FhaY9ir0t4AiOvIjGDIhikbFVJUulfHI057Spzk1lqhBQE4qs7yFVhu0mrloBCtUynqNGiPu8vxWzsu%2BVSEzDDs2tCVU6nJMvGogXkw96Mw58OS31dDXpQRcecYMNEYblIDcLO6K0KYj5z3dpqPGRTbdDtvVekr56%2BSoBQBjODtzYccOd1mbDzcHluTn0ykknTpBd7qDpJzADoH6AvtSIBTUfBf6Q1Kp6QXkOpVnheB5SJSepejw%2FUnvadskUx1%2F%2BIgleKXnGFJwDD9QH4u6iMCRFt%2BRZaPnT8fugw1mawTMxPSyxVtPThCiJXpHtQDK3ZFr2FUnzaY%2BnODZuj06lRXKuCnoz600Rkvdl9FiwTzfecJP0IrcwiV7O%2BnRSdq5DUqxc9qsyROwpug2y31pQk2hxmj1GrvkzRlCoY9ljvfZMMmk97wGOqUBCGtU99UqiXWjeHGIzYCUic3c%2BjZzI3%2FgzLGQXB5C7hyJ7aMaLcN63DNOeQLih7Suzig3MjjGVAWB3A5TngcZDuwFljkn8F7FLnEHd9k0Wl4LQ07C%2F79UkZtpTVM1YuJ56vOPMtAD%2FICf4FyJZAMgbnO%2B1L5GCSK5u7lZ0U3vba3pC%2Byg%2FUiOHpTYZbcV1nmHv444V%2BYgriycE%2FzE2yI4Bag68uHF&X-Amz-Signature=76488143146092b6e94319f3052c759a7d3e26596647ee043fe25e03bf575e24&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVZPPDSF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGY504W3m%2B8FZJaGN2hRfAPEzLzxUR46zno3GgtqqRcgIhAO%2FATSvbl8wdWE0Id%2BGGzb%2F30Vb80V2QOAuPf2f%2Fwom0KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZFwcAFJ5xH1CFIdIq3AO97R1EeZyUXeXnttuPX10R2gQucCBOChbWLLLHAf4Bl%2B70dRXyQ6HsY206Db9HxGJJlHNqchwxGB9XhwfHTvZh3zkvyRpY%2BToGfVj3NtOkSC7nm7kxakBmmE73bxmKaR37ua%2F5XraXOSe7OaUaNa7T1cciyZX%2FURC5Y3YaiPf%2BRVGAuJL29z90ybgN3ezJFpNMINBpVoAtu1Y2%2FY0d9oUFIe832%2BA2yvuJiBayWyY8R0FuLq%2FHnALSB%2FX7P2mMO%2Fb8GilDGYPcg49C4QH3c1DYnOToY1qTQ9rtYgLRTN0IEaXlhbL10LE6N4ZEvd44qPTimSSYyrfRM1u56Bs096bnicyTffpl%2BYIZ3Rj5fGODPFxOgmzOThRR4bARdUOiopGvrsaUa8vsr3W9FtMX1ri7349sdy22DBL4%2FQXnnpkuKFJbpXszrQTEtiqsWKe%2BUZxA61ptW81bImiMUcyAetHsNi8BNwLe%2F9B3vmrU3KyV8zhuBPUn3WxAeIWftlFHZQaCNwMecQfQOIiUPxey5d42acbxAzlIA3nH8tJKbgJMkxaUSShLaHOurdAIC05hD8AOkmRU%2B3FiLypgjVmFpwkahere0OMjePQdRElpJIauXuOGNMh4BTWoAJQ9RTChpPe8BjqkARQEOGs0JCofMnHDnD4vvXWeXhBWm1JEvoPtcWQQTiy4ya0%2F6J8PyAfQ4sBqLIjadfjVRpiAJIG9Ddd0Ue4oBfn%2FowYvY6OHpew2nVT3jwekzOcAJp%2Bi3A%2BW%2B8%2F9G7pKdVWV2w4x4drTdIxy8eEB3bZRsICliNohzpaRWiLxXZUgC1kZBbx%2Fj6pSRb3dTqNt5WpH8EYU7ikPl7mE%2BU4JfPnWHv3O&X-Amz-Signature=41ddefccdaf56e56122b2208781e7227ce3731b6cbf23e13bdae46196e6e20a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULIJ4GK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBzh41L%2BiJqlDYLT0PrkbCUeH4ZU2WRB7N%2BSMbz9%2BSzQIgdIHIhUuWLo8ucZjFU2JojZMklMbBpE%2B7RhPQbedCUHYqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqHeoE1aw71HI3U0yrcA2JccQPxUfxQVyoH%2BGpA1%2BHFQqrsSCds7P4JIoZd8NrFxBphY2ONzD5qwssdFtuFVvKWuNK5Rk2GMNrbWWKXeg8QjM8lFVpzMxTY33rHvIL69XNl3waPBo4o%2FxIDKtl4AwIGIhBf7ImgnGI4azH%2B2PoNtHyW7JkTe%2Fp7nzF8n%2BAq2Qgpx%2FRwafg5lfxnbzAMaBXIiK91pm%2BaFl5XqkJKCVL%2FMICzC%2BOnZe6Q0DGEwK2xkfA8w%2BoDHNU67G0v%2B2ki0wDyo%2BQ%2BLtcQyVYjEIXdziLOJBQ3cWzce16THGCJGq3KWCcIKG6t%2F4LkKac4ArWvzNVHBvolqulMXFtwwkkMLHeQkojZcS9B%2FcRncpDW2Sr73%2B5KPN79g9cTu6Q%2FoO0FM67cmXgvWygF111bEpqW2pb7LIsWIz7WIR7QP9OBWFNNVUU%2FSrtejJiio%2BQ%2F%2Bkq%2F6lI%2BeNWIcFI4hMSC7xgSzxcELg3krV64d0PaBStH2olwIk0x5ScZlSWAb6mrrraxp8qnFvr46ij2r3H7vLzNzwZHHNVSgPcoIbeKae8BxV2%2F3O2gbLiPXCZPQ9LmWNRIMNFhjteVpDZopG1PXkkMv7HkhDR0jg0DVmOE2%2FRTyK7QmW%2BDCE35nhk%2BKh%2FoMPfN97wGOqUBzZsMnuz1n5ipe9TNMyMijEk0Ai6K7XQmG1MMhNgjhEvxckwpLt%2FaN%2FY7N7c1JWEq6zyct9xPpQcK%2B%2F4WaCNizYWdK6UDC7axkjPEG%2Fc%2BX%2FxZ1PjMX8bTi6Q7WnO1gkD9%2BYRsEC1RtCB6dMrpmpWy6v7X36bQI%2BY1rKniBrlRDWdjPfkSc3iPomzSL1YVhgwdrUTz9wA0F2Stzw%2BswZdezCBKmRPN&X-Amz-Signature=a272eeeb0edcac370c3d2f3b60774df1de27a8afd1d998e6f3a5cb9595c4734d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULIJ4GK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBzh41L%2BiJqlDYLT0PrkbCUeH4ZU2WRB7N%2BSMbz9%2BSzQIgdIHIhUuWLo8ucZjFU2JojZMklMbBpE%2B7RhPQbedCUHYqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqHeoE1aw71HI3U0yrcA2JccQPxUfxQVyoH%2BGpA1%2BHFQqrsSCds7P4JIoZd8NrFxBphY2ONzD5qwssdFtuFVvKWuNK5Rk2GMNrbWWKXeg8QjM8lFVpzMxTY33rHvIL69XNl3waPBo4o%2FxIDKtl4AwIGIhBf7ImgnGI4azH%2B2PoNtHyW7JkTe%2Fp7nzF8n%2BAq2Qgpx%2FRwafg5lfxnbzAMaBXIiK91pm%2BaFl5XqkJKCVL%2FMICzC%2BOnZe6Q0DGEwK2xkfA8w%2BoDHNU67G0v%2B2ki0wDyo%2BQ%2BLtcQyVYjEIXdziLOJBQ3cWzce16THGCJGq3KWCcIKG6t%2F4LkKac4ArWvzNVHBvolqulMXFtwwkkMLHeQkojZcS9B%2FcRncpDW2Sr73%2B5KPN79g9cTu6Q%2FoO0FM67cmXgvWygF111bEpqW2pb7LIsWIz7WIR7QP9OBWFNNVUU%2FSrtejJiio%2BQ%2F%2Bkq%2F6lI%2BeNWIcFI4hMSC7xgSzxcELg3krV64d0PaBStH2olwIk0x5ScZlSWAb6mrrraxp8qnFvr46ij2r3H7vLzNzwZHHNVSgPcoIbeKae8BxV2%2F3O2gbLiPXCZPQ9LmWNRIMNFhjteVpDZopG1PXkkMv7HkhDR0jg0DVmOE2%2FRTyK7QmW%2BDCE35nhk%2BKh%2FoMPfN97wGOqUBzZsMnuz1n5ipe9TNMyMijEk0Ai6K7XQmG1MMhNgjhEvxckwpLt%2FaN%2FY7N7c1JWEq6zyct9xPpQcK%2B%2F4WaCNizYWdK6UDC7axkjPEG%2Fc%2BX%2FxZ1PjMX8bTi6Q7WnO1gkD9%2BYRsEC1RtCB6dMrpmpWy6v7X36bQI%2BY1rKniBrlRDWdjPfkSc3iPomzSL1YVhgwdrUTz9wA0F2Stzw%2BswZdezCBKmRPN&X-Amz-Signature=e38a2005b2d4319e4256e4fed5a95b5d41cb8263f41af8695feda598fac89240&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULIJ4GK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBzh41L%2BiJqlDYLT0PrkbCUeH4ZU2WRB7N%2BSMbz9%2BSzQIgdIHIhUuWLo8ucZjFU2JojZMklMbBpE%2B7RhPQbedCUHYqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqHeoE1aw71HI3U0yrcA2JccQPxUfxQVyoH%2BGpA1%2BHFQqrsSCds7P4JIoZd8NrFxBphY2ONzD5qwssdFtuFVvKWuNK5Rk2GMNrbWWKXeg8QjM8lFVpzMxTY33rHvIL69XNl3waPBo4o%2FxIDKtl4AwIGIhBf7ImgnGI4azH%2B2PoNtHyW7JkTe%2Fp7nzF8n%2BAq2Qgpx%2FRwafg5lfxnbzAMaBXIiK91pm%2BaFl5XqkJKCVL%2FMICzC%2BOnZe6Q0DGEwK2xkfA8w%2BoDHNU67G0v%2B2ki0wDyo%2BQ%2BLtcQyVYjEIXdziLOJBQ3cWzce16THGCJGq3KWCcIKG6t%2F4LkKac4ArWvzNVHBvolqulMXFtwwkkMLHeQkojZcS9B%2FcRncpDW2Sr73%2B5KPN79g9cTu6Q%2FoO0FM67cmXgvWygF111bEpqW2pb7LIsWIz7WIR7QP9OBWFNNVUU%2FSrtejJiio%2BQ%2F%2Bkq%2F6lI%2BeNWIcFI4hMSC7xgSzxcELg3krV64d0PaBStH2olwIk0x5ScZlSWAb6mrrraxp8qnFvr46ij2r3H7vLzNzwZHHNVSgPcoIbeKae8BxV2%2F3O2gbLiPXCZPQ9LmWNRIMNFhjteVpDZopG1PXkkMv7HkhDR0jg0DVmOE2%2FRTyK7QmW%2BDCE35nhk%2BKh%2FoMPfN97wGOqUBzZsMnuz1n5ipe9TNMyMijEk0Ai6K7XQmG1MMhNgjhEvxckwpLt%2FaN%2FY7N7c1JWEq6zyct9xPpQcK%2B%2F4WaCNizYWdK6UDC7axkjPEG%2Fc%2BX%2FxZ1PjMX8bTi6Q7WnO1gkD9%2BYRsEC1RtCB6dMrpmpWy6v7X36bQI%2BY1rKniBrlRDWdjPfkSc3iPomzSL1YVhgwdrUTz9wA0F2Stzw%2BswZdezCBKmRPN&X-Amz-Signature=721f91823112d889a5f73f6c52521df2fcfaeaca8912e679f328ce4e3605598c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BAUX4MX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICas8qi7t3ha2WSsz57c2p3HJR1QU8T1uRlZWpuuHThyAiADpLlS637n8rq5VyqzS5grK1rvDnFM9S%2B7LqKsLv%2BdeiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlPI8CKDF6bAyIkQ1KtwDlqL9P7l7hOEffUpf1GwK%2FBmzL%2FTcckjxJet3%2FfSl5EvXD3hk2x8XsyohCAUuf8mrnrUpU2Y5hu8ELI81ZuRJC82VuK%2BTpDCD2eTvdjM0rNGtfeu0qlJP4iTWb9Xdxj81pSYt2R6DMOFcY89BTyo06AhphhiqhJPiFFzT8bd0WYonlp25%2FiDYplVp3Qr5XelatkHcsfh29wMGhnNAi8Kqvmp55covwlASQcmp977YjBfAZnGYrhWF59GPSZbszPxJ%2Bt9OV6r%2B0sPIGqf2UxL3Xc8fF11wqch5xd%2BNsclZ2m0%2FE%2Fehr%2BipYcn3Yz1v20tWmT6qa5azQUfN7fD81saBGHbBR2CN4iw5zD8F%2BPsDBgBIwpiqQtAIKbJNhkXdvlT1FhnMiEKd6F1R405tNQEnAcmfXkTSxT%2BIebwSLfRt4d8Oh9P945OWBY2lBf7nTZX7yGjGfBPeEau0LwdDB%2F3ob0ZrmfVd5BPyckBfsk8CLtrol9lXwGApxRwrZ6sDUGHMFeRNK5Dl%2FCRJAZQvynr5dNxvpZaTAfqBuif0VQw1dXIYrIm%2FGF%2BRabzBjoxGdhbMAu7pvIi1x4taR6uccMjJpuHtJ7%2Fko4Zk57kvxZLwyiL3Tz83CtBVY84iNZgw4aT3vAY6pgHzVgCEYVvH69cld4ZJ53Ry2qPUvMsQhQzRrk8%2FnOCnsIJ48mf1UTF8eC2yNiIHkPKYgn4tBZcGoboWbzULSGNh0AyvBndnCADb9Vu9d9s80OPQeojXMBBlsvA7XyLPOTMMsekBNuVh5%2BAtNudBVeEeVjvj6lQO6H0NfXgy92S%2F4TkUZm%2FYw7V%2F%2BWxM3sPQcsRoX03qkK6goZbYMx%2Ba5PYGX6SKm4ks&X-Amz-Signature=dc7fe24754835c92e8f1ad846d855dcc2d1d119d816aa5c04be5dd47b252a847&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4ML6JGV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbOvKELljWUILmfAxyb1LaEP%2BcqdJ5RjYYF0TczU8YgQIgA1xBdy1HqeyBDKbHqfzJWQfgZgCMty99xhORrYbgSvcqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHOFdOc1R7sQqKV22ircA5DqxmnjpIrzRKqP2%2FTXLg9BRfewXSuGLI0bN77ramDRW6oaJ7BWUmB1cPgPTYkvwoy7lOGrLDTq4P7VfxBCemhqsQWbnrr4eRwLEjowFlObdnAU9DoCxIW7u84zUVokV7m1A4tOiRKKtusCB8Rr1yV%2BimV8wUMm80rzAgdL9wCqWfaAsfvXr39RO7Toj2%2FYwDDPYrwn%2B5vgdDa0Hp0KJK75I%2FsPZNiSpLLFsVgymtLL%2FlgH9%2FpOqc14hhheviNvMe3E2q5%2BTB6n6tU9aT3WXxwTc1byxD8VR%2Frk5s0qI%2BBNWt72wCSASRGf7I7IMfiblxTo010rYqtEc%2BKHl0U484q6TKNi3es6Zk2NgydaeNJJgPBzx8yIf%2BnkPFFXhwqqN3XSVps1Ju2bWWc04a1uGof5t1xS%2BJaUASG3rbYGXbXOeNxceKQ3Gi2ZZW1U4oIbDoyYBnli9w2jJcTx4Df%2FcIIpLgXaKtfmMH5aRmVFtDCOqOJaZN5uKNEDMG85E%2F%2FMahHVVrZ1TUXBe0BVaLjx0Np1Wnc8x5pK5tUm0fNwtqMj2AQK9LdJ7qEzA71tnR9m2F8rYcySn6r1jCyb0V3Mkgfs25TwxFXLgdDRkEI8v0i6rN%2Bjm46BC1AZSF4IMMek97wGOqUBix9KYd07DaK%2BGRICcdY%2BJtg39Pl%2B8wTsaFU73RpunkEDKnceByiHcJhLSQn76aPxbXvOACLV2MpEjRUt8lIVU4icCKJBKV3UL%2BwwwBaS%2BkFEpqH8za8Y9t0D6K436K6ivvxViN%2Bum5acVtLYNUqRRx0PYsgAsqdnv6kKMWXFeVqMRZnQfktnBQ%2F%2B2FX%2BkFQOrRYVouIIk6D6kdUt2vVePHuSpf3n&X-Amz-Signature=537b47995f0b30266c046e510816d46fa7891e29815d0a382560566bfa4b2220&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOW64PP4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDCud4WrlQrhNKCu2rV1W7mOs%2BU5C2jVOU0ZdA9NdD5MAiEA21MdkqS2fqM%2BYN%2Fnj7SekvA8DNI9NxHtjcNvSPAhuZUqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEwJerkKxgruG58XTSrcA390rIoGDx02RXY%2FPzqAoXfNmjs525VAUJE7ns3jdIAN1PWup5kvOhyfI0L9Q%2F1EEZTjMYaJR2YRPNULzAfZo4vTyOQwEEIU358ZblSBnJ0ytD%2BIGi2%2FFIli8THSdny5EQ36vj9JY6ZSpXWQ8f4n%2BoIzAH2An2qysTUDppu3bpLYPBOLVJq0DHgXsgC3OOvHC%2BnOpQWVaEW2JdCyrzQM%2F1LBn%2BdpMzfiEf2e%2FGNS1UeO9kFwpX5GKFB2TOrYrZoaTMuuVl9E%2ByNokWk5TcZ0Rbyli%2FbSVOVDt4tLnx0549GImMalWSrKifn788FiQPjWqmHjXVWMAFxYz74sODU8IufUw%2FHE2egtNTYXapJyfCLxns%2FJavh9g8hfggsDjzYgi2e%2FLVW5n%2FcL6COSpz8N06bsld%2B8gSYNVgtMyXoVWSG7KunOadZTpfmtVkaAHBqOqjs1tEa537iqm4L126V5YZ2opgXQ9C7FS2Ir8R0JXk7Lk%2F2oA4%2Bo4YLQT2hUTnjr9XQ%2FM7e2OYNo4T8VtgEK83vRsFQ9%2BTloxd%2B8w%2BZYpgo0DGBwUgDF6maSRi76Vb4fYcTXhHsPMY6O2WDuyreOkHNtR9OjGEJLy3%2BsCe%2BjLxtCuzc%2BTsh9sC3py1hIML6k97wGOqUBMiKkY2Sx%2BT%2F%2FUaaPYOfoAyJOmk2kcBGwNp2n6%2FCMAKyS1bhF3bl5uZlPkLCfcK%2FRqjaedeMaLxp2u0d5N%2BPFmsSe6ZPDtlDlI669FK2z1Zhb5yP45gm6dtj6bEi%2BkJ0p88b12qyb5KvcRJpqdtvgO2FvRU1RDn9w4drR%2FSkMCqKarU564t89TeknVU5romEOiew5NhMyhZxEAc7pzClbfokEQSY4&X-Amz-Signature=850d1ab878ecb882eea27f563088de187426b483701c49b61bc5fd27089d9633&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF2CXOCC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBHdDsr%2FBttebyc%2FmQHxj6QTjfkrD%2BszHdL3xR3P3tJAiBtM5xySAQBbwsX4ebiWdiJshBiHYv%2Bp2%2BmmLiDGwy5%2FCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9%2FrEeFZwopDSbTNaKtwDJqNYQZ3JqDHxs4xHwyAQTqGckt62MsO5hToxUR9%2Bqqm%2FIZSHEQcWq3AXFJhenIipn8rDIsVx1z%2BIWZNjJhnjUnX5mVVNCX3cy%2FD2nry9ylTZh6lxTdvoSIY%2B72qoXEdbF8jkmLKskSKFY41vcPoBLLzdt9%2BLvn7wh2D1wBoWE0woZTp%2BSytDmMN9PVRwTcZJ5HBB2mNa10eZmy%2FkDXI3HyXyy3QB7GBCO26Wij8aQLZiEhCd5oGaoEm5R6GUbx6ZJ7G%2B39HialDeyyOvZPp4OmADB5BqEF5RHOXvklJngkKF0hHWpvSFUEnk7E%2FKegU5%2FfxrkeUNjXo%2B%2Bu8liqG8mJX61ll2MX96Ul3fSU313Ah35r69o4IEFgIwNy4IPoOHLt9nFW3IfubjR4da4V6y41EHNSm%2FhFw%2BVMaLK5YxSINdnmJ6JsDcx0Xs2onBMcNXIOY88pkvm9GBHu3%2Bo0T3RF4SHnQ%2BqMxwGcc8tzBwO0mLBrgQmosQI7X3mHfRv5Hlwd%2BazGfq1ydoJ%2F%2B8x4X6mQCzR0vMjCHxX8dfga3NnEtPuFMMTzgCKHkMZUpCNJ86ZgIQf6QXNVRo9LNxalgDYU08IOzHTL1J7RCufKd0Q5pbhHgx1xSPiL%2F8gp8w1KT3vAY6pgG8h%2BxtadeYP6LV%2BcnLex%2BPs47d%2F0Zg6PW%2BoCTmfsjb09NRVNblOXaj3qmVdQfasm5kLJtbV5sp5V8shuP4HLtdy%2FVvGqdK0RUNIs9BrQn7CHuZ6KoJF6P%2BmwuHlW16VbslpMivwjmYPSI%2B9gc0ZSwAuW%2FBa72LJ%2FzlNVDXMPMttMKglENvIFGiclAyepA58DhYoGDjxjcrpbSwd3gE5UibC%2F9tH%2FwK&X-Amz-Signature=2cee6cfd9bd7cca83a4d2bd3d677d688c6a4891526a220f3af0dd77be24befd2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF2CXOCC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBHdDsr%2FBttebyc%2FmQHxj6QTjfkrD%2BszHdL3xR3P3tJAiBtM5xySAQBbwsX4ebiWdiJshBiHYv%2Bp2%2BmmLiDGwy5%2FCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9%2FrEeFZwopDSbTNaKtwDJqNYQZ3JqDHxs4xHwyAQTqGckt62MsO5hToxUR9%2Bqqm%2FIZSHEQcWq3AXFJhenIipn8rDIsVx1z%2BIWZNjJhnjUnX5mVVNCX3cy%2FD2nry9ylTZh6lxTdvoSIY%2B72qoXEdbF8jkmLKskSKFY41vcPoBLLzdt9%2BLvn7wh2D1wBoWE0woZTp%2BSytDmMN9PVRwTcZJ5HBB2mNa10eZmy%2FkDXI3HyXyy3QB7GBCO26Wij8aQLZiEhCd5oGaoEm5R6GUbx6ZJ7G%2B39HialDeyyOvZPp4OmADB5BqEF5RHOXvklJngkKF0hHWpvSFUEnk7E%2FKegU5%2FfxrkeUNjXo%2B%2Bu8liqG8mJX61ll2MX96Ul3fSU313Ah35r69o4IEFgIwNy4IPoOHLt9nFW3IfubjR4da4V6y41EHNSm%2FhFw%2BVMaLK5YxSINdnmJ6JsDcx0Xs2onBMcNXIOY88pkvm9GBHu3%2Bo0T3RF4SHnQ%2BqMxwGcc8tzBwO0mLBrgQmosQI7X3mHfRv5Hlwd%2BazGfq1ydoJ%2F%2B8x4X6mQCzR0vMjCHxX8dfga3NnEtPuFMMTzgCKHkMZUpCNJ86ZgIQf6QXNVRo9LNxalgDYU08IOzHTL1J7RCufKd0Q5pbhHgx1xSPiL%2F8gp8w1KT3vAY6pgG8h%2BxtadeYP6LV%2BcnLex%2BPs47d%2F0Zg6PW%2BoCTmfsjb09NRVNblOXaj3qmVdQfasm5kLJtbV5sp5V8shuP4HLtdy%2FVvGqdK0RUNIs9BrQn7CHuZ6KoJF6P%2BmwuHlW16VbslpMivwjmYPSI%2B9gc0ZSwAuW%2FBa72LJ%2FzlNVDXMPMttMKglENvIFGiclAyepA58DhYoGDjxjcrpbSwd3gE5UibC%2F9tH%2FwK&X-Amz-Signature=1bfa74bae521ea1b7069c48c8fd1c33c90592c63388db3c75e97a76dc4bba7ee&X-Amz-SignedHeaders=host&x-id=GetObject)

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
