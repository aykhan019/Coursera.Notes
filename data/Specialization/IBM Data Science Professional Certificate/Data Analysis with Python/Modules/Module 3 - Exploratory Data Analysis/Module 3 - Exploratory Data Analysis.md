

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSEAYYLL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQDto%2BBkt60VuJv4A16zI9U6bT7rqeDLrw5w86NNF%2BNLOgIhAKpBCMT7XPlz0adGz4ceHdCDCmlm2jzl8%2FdAKrLKuWbnKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZPwH1WM1Oyo2N8z4q3APFh9J69Eib5QP7ZAy2v8kqRwEyzic7alPmeRG8vJ17GXW5MMOh6SsX7f3DtROgwVuuZqjMAS9TPm2ERoDPW4j4ILDxvPB0uE%2F78jktUhzbqdUYOvE6OpVMYaMe4pu9m2aQjNfcb9lT2fTCtyGXw96LwlorPO2HuobdH4v7LcfyI00%2BcLrgswjDiv7BiSUuPDtUp7M%2BEolNgv5aTq2WxYdBzwDd6%2BQgLRY6gNTToUF4nQhVCvd3bE3%2F2iR1esw8vlhaXQ8oebIk3uMPXXGG0jDysfXaHtfEJTOvRyg3sMsaw0EnqbZAz7Q2BhFKitI3unsPgSqS52xg5hyfQzfZ2xNlmkUwrJ42upv6yCLHbg6zT%2FfyUPYvWsejj8tBK%2B7wS7GgUPE%2F434e%2Fd%2FQC6jToZQg1SWJ%2Fw9jA%2Bnm8st%2BGzPjJ7oAD8KTtpnWwNuGNpVH8zTSxnKLKqXRwe2rQSIDR1UxGfMW6bbjFZ61b2q0YTUI8XoJYWHFCzZNw3K4hR%2B7TwO4P2yfcE4%2BY5%2Bv881OMf3U6kZmjf8dt359uyKm%2BYNtc6Sujhcbplyo6oIX1BMnkALeWCQt%2BGsSdMjV6RsXv50vPw6cg5cKzEbUCj1JmIuOl86y9Ok%2FwWAe9%2BCKhTDp5%2BW8BjqkAYEnzt89shvG9TCnjkNuMMPk5utnxgaguNdvQjmBLNliQnY2V2IVVQSwxXCfA2UPgMg%2BR4VtW1sQwQnKRplvM20nBmKoggciXU2p6hplo%2FUXvFW0sjoch8s9I4pWWmIrO7kyki7Y34K1UymHGyalwNJNVJWF84R%2FQ08Olz62NLjpaGf0nEqZwwhMw%2FwF7l18eShotUeIZALmkC8HZGfRG%2Bx8tjfR&X-Amz-Signature=b274a200a8e079c64211d1fb5a92812e3b40e1b0e51f385cb7763eaff4c854b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSEAYYLL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQDto%2BBkt60VuJv4A16zI9U6bT7rqeDLrw5w86NNF%2BNLOgIhAKpBCMT7XPlz0adGz4ceHdCDCmlm2jzl8%2FdAKrLKuWbnKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZPwH1WM1Oyo2N8z4q3APFh9J69Eib5QP7ZAy2v8kqRwEyzic7alPmeRG8vJ17GXW5MMOh6SsX7f3DtROgwVuuZqjMAS9TPm2ERoDPW4j4ILDxvPB0uE%2F78jktUhzbqdUYOvE6OpVMYaMe4pu9m2aQjNfcb9lT2fTCtyGXw96LwlorPO2HuobdH4v7LcfyI00%2BcLrgswjDiv7BiSUuPDtUp7M%2BEolNgv5aTq2WxYdBzwDd6%2BQgLRY6gNTToUF4nQhVCvd3bE3%2F2iR1esw8vlhaXQ8oebIk3uMPXXGG0jDysfXaHtfEJTOvRyg3sMsaw0EnqbZAz7Q2BhFKitI3unsPgSqS52xg5hyfQzfZ2xNlmkUwrJ42upv6yCLHbg6zT%2FfyUPYvWsejj8tBK%2B7wS7GgUPE%2F434e%2Fd%2FQC6jToZQg1SWJ%2Fw9jA%2Bnm8st%2BGzPjJ7oAD8KTtpnWwNuGNpVH8zTSxnKLKqXRwe2rQSIDR1UxGfMW6bbjFZ61b2q0YTUI8XoJYWHFCzZNw3K4hR%2B7TwO4P2yfcE4%2BY5%2Bv881OMf3U6kZmjf8dt359uyKm%2BYNtc6Sujhcbplyo6oIX1BMnkALeWCQt%2BGsSdMjV6RsXv50vPw6cg5cKzEbUCj1JmIuOl86y9Ok%2FwWAe9%2BCKhTDp5%2BW8BjqkAYEnzt89shvG9TCnjkNuMMPk5utnxgaguNdvQjmBLNliQnY2V2IVVQSwxXCfA2UPgMg%2BR4VtW1sQwQnKRplvM20nBmKoggciXU2p6hplo%2FUXvFW0sjoch8s9I4pWWmIrO7kyki7Y34K1UymHGyalwNJNVJWF84R%2FQ08Olz62NLjpaGf0nEqZwwhMw%2FwF7l18eShotUeIZALmkC8HZGfRG%2Bx8tjfR&X-Amz-Signature=dcf0b965b6e7d4cfd612f96adde0e77b214d25ec67daa5d773247437692c6b69&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSEAYYLL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQDto%2BBkt60VuJv4A16zI9U6bT7rqeDLrw5w86NNF%2BNLOgIhAKpBCMT7XPlz0adGz4ceHdCDCmlm2jzl8%2FdAKrLKuWbnKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZPwH1WM1Oyo2N8z4q3APFh9J69Eib5QP7ZAy2v8kqRwEyzic7alPmeRG8vJ17GXW5MMOh6SsX7f3DtROgwVuuZqjMAS9TPm2ERoDPW4j4ILDxvPB0uE%2F78jktUhzbqdUYOvE6OpVMYaMe4pu9m2aQjNfcb9lT2fTCtyGXw96LwlorPO2HuobdH4v7LcfyI00%2BcLrgswjDiv7BiSUuPDtUp7M%2BEolNgv5aTq2WxYdBzwDd6%2BQgLRY6gNTToUF4nQhVCvd3bE3%2F2iR1esw8vlhaXQ8oebIk3uMPXXGG0jDysfXaHtfEJTOvRyg3sMsaw0EnqbZAz7Q2BhFKitI3unsPgSqS52xg5hyfQzfZ2xNlmkUwrJ42upv6yCLHbg6zT%2FfyUPYvWsejj8tBK%2B7wS7GgUPE%2F434e%2Fd%2FQC6jToZQg1SWJ%2Fw9jA%2Bnm8st%2BGzPjJ7oAD8KTtpnWwNuGNpVH8zTSxnKLKqXRwe2rQSIDR1UxGfMW6bbjFZ61b2q0YTUI8XoJYWHFCzZNw3K4hR%2B7TwO4P2yfcE4%2BY5%2Bv881OMf3U6kZmjf8dt359uyKm%2BYNtc6Sujhcbplyo6oIX1BMnkALeWCQt%2BGsSdMjV6RsXv50vPw6cg5cKzEbUCj1JmIuOl86y9Ok%2FwWAe9%2BCKhTDp5%2BW8BjqkAYEnzt89shvG9TCnjkNuMMPk5utnxgaguNdvQjmBLNliQnY2V2IVVQSwxXCfA2UPgMg%2BR4VtW1sQwQnKRplvM20nBmKoggciXU2p6hplo%2FUXvFW0sjoch8s9I4pWWmIrO7kyki7Y34K1UymHGyalwNJNVJWF84R%2FQ08Olz62NLjpaGf0nEqZwwhMw%2FwF7l18eShotUeIZALmkC8HZGfRG%2Bx8tjfR&X-Amz-Signature=cf6f4200022163afe9abfaa1a80c8ca10654081f328d02f399813f21b95e5c1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LGSIJUS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDtYHo1K1CH6dYzMKry9RstJFBUSBtchCDkXMKylN6A2gIgA1FDt%2FYegoHDQ3uuMzXk8Qs8NK3Yj5Vj%2Fz4uZQvkyTEqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbWugKCCWPJUC7kDyrcA33m1V1sMA1WM8uipSuBCOugwxhUaC24M3VQvvTm0pO%2B%2FoomThrbNumEP75t2Vr%2Bj3ClFklVBNWgk2wfoDObM86ZjTH8c%2B9yIKEy0PwCP5n7SS5A2P8ajUgqDoHIOTKE%2Bo6AJbwjZq%2BZYBUBnfNT3irH28Vh%2BoQlILE9eS3C6W15iLKjkcqHnahs7AgZn3cKFxIRxaFSC0GsVHCMavlzxs7nenxyfh%2FpPBXlt7CDtVFSRVg9gVuLpBUbNhqB0smvPeux7N8QHdEhe60GopwrwlRY%2Bm303LUVghSJRv%2F2sZX5X7V0eMtKeUScdB%2FLUoe8ezwNQIlVvwEM%2Fi%2BBE7wTFHAQe8%2FghGUdA9JgRVmScQ%2FWHbZ8VrECrIsCyn5pmtMU%2BBmqQgV1uUKO09yqpSgfh8%2FidZuXbRRhiHqvD3yu8UiNW6Qq0YKmm4pTPiAmG7XgGnfpwD2YLClHSGuA4r%2FXVSWonxD8iinBoh%2FAf9g9CmoKsGsT5xseV8418G9hoxyjf%2BwFqV5QcRuQeIdvvTVj4%2BQiAmuFEiwKTONKtGJMkfAk%2FOYw6EXlZSh%2BmZ5usN57TmRaRbADtmQQY3zRAnKWczTv%2BJSJ4qXwOBOBbQUvJ7XX6o3EBkSzLxxC6PbrMJbo5bwGOqUBZYD%2B3VqNhyfCswvE%2FMTUSJvY7bZKCzaAD2wgM1hWpewzYJtPxRnbK%2B9f49CK4KCFi0qSRquHfu0c1J%2B7SgJfOe5Uu6PUHkaGmqygltTSi3tBjB0sJyHbXMEXrweNnGb2Rv2f67eTPQHFlul2flF%2FUsifTY8VPsf1jg5ZLwlG%2BzdN1KpCAFLJIhF0v%2BWtbL5O03vgSIYr2Al%2BRH7JgytE9cZSicBC&X-Amz-Signature=4848ec42d26be01057c03152907bce735f543c61eef5b490bb0993a388bf369e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LGSIJUS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDtYHo1K1CH6dYzMKry9RstJFBUSBtchCDkXMKylN6A2gIgA1FDt%2FYegoHDQ3uuMzXk8Qs8NK3Yj5Vj%2Fz4uZQvkyTEqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbWugKCCWPJUC7kDyrcA33m1V1sMA1WM8uipSuBCOugwxhUaC24M3VQvvTm0pO%2B%2FoomThrbNumEP75t2Vr%2Bj3ClFklVBNWgk2wfoDObM86ZjTH8c%2B9yIKEy0PwCP5n7SS5A2P8ajUgqDoHIOTKE%2Bo6AJbwjZq%2BZYBUBnfNT3irH28Vh%2BoQlILE9eS3C6W15iLKjkcqHnahs7AgZn3cKFxIRxaFSC0GsVHCMavlzxs7nenxyfh%2FpPBXlt7CDtVFSRVg9gVuLpBUbNhqB0smvPeux7N8QHdEhe60GopwrwlRY%2Bm303LUVghSJRv%2F2sZX5X7V0eMtKeUScdB%2FLUoe8ezwNQIlVvwEM%2Fi%2BBE7wTFHAQe8%2FghGUdA9JgRVmScQ%2FWHbZ8VrECrIsCyn5pmtMU%2BBmqQgV1uUKO09yqpSgfh8%2FidZuXbRRhiHqvD3yu8UiNW6Qq0YKmm4pTPiAmG7XgGnfpwD2YLClHSGuA4r%2FXVSWonxD8iinBoh%2FAf9g9CmoKsGsT5xseV8418G9hoxyjf%2BwFqV5QcRuQeIdvvTVj4%2BQiAmuFEiwKTONKtGJMkfAk%2FOYw6EXlZSh%2BmZ5usN57TmRaRbADtmQQY3zRAnKWczTv%2BJSJ4qXwOBOBbQUvJ7XX6o3EBkSzLxxC6PbrMJbo5bwGOqUBZYD%2B3VqNhyfCswvE%2FMTUSJvY7bZKCzaAD2wgM1hWpewzYJtPxRnbK%2B9f49CK4KCFi0qSRquHfu0c1J%2B7SgJfOe5Uu6PUHkaGmqygltTSi3tBjB0sJyHbXMEXrweNnGb2Rv2f67eTPQHFlul2flF%2FUsifTY8VPsf1jg5ZLwlG%2BzdN1KpCAFLJIhF0v%2BWtbL5O03vgSIYr2Al%2BRH7JgytE9cZSicBC&X-Amz-Signature=ed3f26425b2a21932c407e53609b94a379633956686d05c8e2f840cd8db158b4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LGSIJUS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDtYHo1K1CH6dYzMKry9RstJFBUSBtchCDkXMKylN6A2gIgA1FDt%2FYegoHDQ3uuMzXk8Qs8NK3Yj5Vj%2Fz4uZQvkyTEqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbWugKCCWPJUC7kDyrcA33m1V1sMA1WM8uipSuBCOugwxhUaC24M3VQvvTm0pO%2B%2FoomThrbNumEP75t2Vr%2Bj3ClFklVBNWgk2wfoDObM86ZjTH8c%2B9yIKEy0PwCP5n7SS5A2P8ajUgqDoHIOTKE%2Bo6AJbwjZq%2BZYBUBnfNT3irH28Vh%2BoQlILE9eS3C6W15iLKjkcqHnahs7AgZn3cKFxIRxaFSC0GsVHCMavlzxs7nenxyfh%2FpPBXlt7CDtVFSRVg9gVuLpBUbNhqB0smvPeux7N8QHdEhe60GopwrwlRY%2Bm303LUVghSJRv%2F2sZX5X7V0eMtKeUScdB%2FLUoe8ezwNQIlVvwEM%2Fi%2BBE7wTFHAQe8%2FghGUdA9JgRVmScQ%2FWHbZ8VrECrIsCyn5pmtMU%2BBmqQgV1uUKO09yqpSgfh8%2FidZuXbRRhiHqvD3yu8UiNW6Qq0YKmm4pTPiAmG7XgGnfpwD2YLClHSGuA4r%2FXVSWonxD8iinBoh%2FAf9g9CmoKsGsT5xseV8418G9hoxyjf%2BwFqV5QcRuQeIdvvTVj4%2BQiAmuFEiwKTONKtGJMkfAk%2FOYw6EXlZSh%2BmZ5usN57TmRaRbADtmQQY3zRAnKWczTv%2BJSJ4qXwOBOBbQUvJ7XX6o3EBkSzLxxC6PbrMJbo5bwGOqUBZYD%2B3VqNhyfCswvE%2FMTUSJvY7bZKCzaAD2wgM1hWpewzYJtPxRnbK%2B9f49CK4KCFi0qSRquHfu0c1J%2B7SgJfOe5Uu6PUHkaGmqygltTSi3tBjB0sJyHbXMEXrweNnGb2Rv2f67eTPQHFlul2flF%2FUsifTY8VPsf1jg5ZLwlG%2BzdN1KpCAFLJIhF0v%2BWtbL5O03vgSIYr2Al%2BRH7JgytE9cZSicBC&X-Amz-Signature=628420e0368b88eb8bcd2dee651c6736699c6d51b88199364ea3f8c99474b364&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LGSIJUS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDtYHo1K1CH6dYzMKry9RstJFBUSBtchCDkXMKylN6A2gIgA1FDt%2FYegoHDQ3uuMzXk8Qs8NK3Yj5Vj%2Fz4uZQvkyTEqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbWugKCCWPJUC7kDyrcA33m1V1sMA1WM8uipSuBCOugwxhUaC24M3VQvvTm0pO%2B%2FoomThrbNumEP75t2Vr%2Bj3ClFklVBNWgk2wfoDObM86ZjTH8c%2B9yIKEy0PwCP5n7SS5A2P8ajUgqDoHIOTKE%2Bo6AJbwjZq%2BZYBUBnfNT3irH28Vh%2BoQlILE9eS3C6W15iLKjkcqHnahs7AgZn3cKFxIRxaFSC0GsVHCMavlzxs7nenxyfh%2FpPBXlt7CDtVFSRVg9gVuLpBUbNhqB0smvPeux7N8QHdEhe60GopwrwlRY%2Bm303LUVghSJRv%2F2sZX5X7V0eMtKeUScdB%2FLUoe8ezwNQIlVvwEM%2Fi%2BBE7wTFHAQe8%2FghGUdA9JgRVmScQ%2FWHbZ8VrECrIsCyn5pmtMU%2BBmqQgV1uUKO09yqpSgfh8%2FidZuXbRRhiHqvD3yu8UiNW6Qq0YKmm4pTPiAmG7XgGnfpwD2YLClHSGuA4r%2FXVSWonxD8iinBoh%2FAf9g9CmoKsGsT5xseV8418G9hoxyjf%2BwFqV5QcRuQeIdvvTVj4%2BQiAmuFEiwKTONKtGJMkfAk%2FOYw6EXlZSh%2BmZ5usN57TmRaRbADtmQQY3zRAnKWczTv%2BJSJ4qXwOBOBbQUvJ7XX6o3EBkSzLxxC6PbrMJbo5bwGOqUBZYD%2B3VqNhyfCswvE%2FMTUSJvY7bZKCzaAD2wgM1hWpewzYJtPxRnbK%2B9f49CK4KCFi0qSRquHfu0c1J%2B7SgJfOe5Uu6PUHkaGmqygltTSi3tBjB0sJyHbXMEXrweNnGb2Rv2f67eTPQHFlul2flF%2FUsifTY8VPsf1jg5ZLwlG%2BzdN1KpCAFLJIhF0v%2BWtbL5O03vgSIYr2Al%2BRH7JgytE9cZSicBC&X-Amz-Signature=2ce46cede6f2241e34984a7a8f260f99d18397a70d13e39ead56119006b8fe9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LGSIJUS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDtYHo1K1CH6dYzMKry9RstJFBUSBtchCDkXMKylN6A2gIgA1FDt%2FYegoHDQ3uuMzXk8Qs8NK3Yj5Vj%2Fz4uZQvkyTEqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbWugKCCWPJUC7kDyrcA33m1V1sMA1WM8uipSuBCOugwxhUaC24M3VQvvTm0pO%2B%2FoomThrbNumEP75t2Vr%2Bj3ClFklVBNWgk2wfoDObM86ZjTH8c%2B9yIKEy0PwCP5n7SS5A2P8ajUgqDoHIOTKE%2Bo6AJbwjZq%2BZYBUBnfNT3irH28Vh%2BoQlILE9eS3C6W15iLKjkcqHnahs7AgZn3cKFxIRxaFSC0GsVHCMavlzxs7nenxyfh%2FpPBXlt7CDtVFSRVg9gVuLpBUbNhqB0smvPeux7N8QHdEhe60GopwrwlRY%2Bm303LUVghSJRv%2F2sZX5X7V0eMtKeUScdB%2FLUoe8ezwNQIlVvwEM%2Fi%2BBE7wTFHAQe8%2FghGUdA9JgRVmScQ%2FWHbZ8VrECrIsCyn5pmtMU%2BBmqQgV1uUKO09yqpSgfh8%2FidZuXbRRhiHqvD3yu8UiNW6Qq0YKmm4pTPiAmG7XgGnfpwD2YLClHSGuA4r%2FXVSWonxD8iinBoh%2FAf9g9CmoKsGsT5xseV8418G9hoxyjf%2BwFqV5QcRuQeIdvvTVj4%2BQiAmuFEiwKTONKtGJMkfAk%2FOYw6EXlZSh%2BmZ5usN57TmRaRbADtmQQY3zRAnKWczTv%2BJSJ4qXwOBOBbQUvJ7XX6o3EBkSzLxxC6PbrMJbo5bwGOqUBZYD%2B3VqNhyfCswvE%2FMTUSJvY7bZKCzaAD2wgM1hWpewzYJtPxRnbK%2B9f49CK4KCFi0qSRquHfu0c1J%2B7SgJfOe5Uu6PUHkaGmqygltTSi3tBjB0sJyHbXMEXrweNnGb2Rv2f67eTPQHFlul2flF%2FUsifTY8VPsf1jg5ZLwlG%2BzdN1KpCAFLJIhF0v%2BWtbL5O03vgSIYr2Al%2BRH7JgytE9cZSicBC&X-Amz-Signature=91baab8ef3c5242bb161008188918ebd07c774afc701030c3b402a752e7af8ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LGSIJUS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDtYHo1K1CH6dYzMKry9RstJFBUSBtchCDkXMKylN6A2gIgA1FDt%2FYegoHDQ3uuMzXk8Qs8NK3Yj5Vj%2Fz4uZQvkyTEqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbWugKCCWPJUC7kDyrcA33m1V1sMA1WM8uipSuBCOugwxhUaC24M3VQvvTm0pO%2B%2FoomThrbNumEP75t2Vr%2Bj3ClFklVBNWgk2wfoDObM86ZjTH8c%2B9yIKEy0PwCP5n7SS5A2P8ajUgqDoHIOTKE%2Bo6AJbwjZq%2BZYBUBnfNT3irH28Vh%2BoQlILE9eS3C6W15iLKjkcqHnahs7AgZn3cKFxIRxaFSC0GsVHCMavlzxs7nenxyfh%2FpPBXlt7CDtVFSRVg9gVuLpBUbNhqB0smvPeux7N8QHdEhe60GopwrwlRY%2Bm303LUVghSJRv%2F2sZX5X7V0eMtKeUScdB%2FLUoe8ezwNQIlVvwEM%2Fi%2BBE7wTFHAQe8%2FghGUdA9JgRVmScQ%2FWHbZ8VrECrIsCyn5pmtMU%2BBmqQgV1uUKO09yqpSgfh8%2FidZuXbRRhiHqvD3yu8UiNW6Qq0YKmm4pTPiAmG7XgGnfpwD2YLClHSGuA4r%2FXVSWonxD8iinBoh%2FAf9g9CmoKsGsT5xseV8418G9hoxyjf%2BwFqV5QcRuQeIdvvTVj4%2BQiAmuFEiwKTONKtGJMkfAk%2FOYw6EXlZSh%2BmZ5usN57TmRaRbADtmQQY3zRAnKWczTv%2BJSJ4qXwOBOBbQUvJ7XX6o3EBkSzLxxC6PbrMJbo5bwGOqUBZYD%2B3VqNhyfCswvE%2FMTUSJvY7bZKCzaAD2wgM1hWpewzYJtPxRnbK%2B9f49CK4KCFi0qSRquHfu0c1J%2B7SgJfOe5Uu6PUHkaGmqygltTSi3tBjB0sJyHbXMEXrweNnGb2Rv2f67eTPQHFlul2flF%2FUsifTY8VPsf1jg5ZLwlG%2BzdN1KpCAFLJIhF0v%2BWtbL5O03vgSIYr2Al%2BRH7JgytE9cZSicBC&X-Amz-Signature=593ac2498e900c8d2e1817a863827e619f4b7cf7b7ac11fe176b45279a4bf39e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFFT6NX4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQC5uRFi2iGzgQs2NymQw5eBClEX0K2%2B9DhceEaw5FkUswIhALqeYacZ9OMdm5MT0HerhkP8CpWqwN4djR04AcfJZrJ2KogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLBOXEZ%2F6VARtAVvUq3AP8YuWSGXtRgTi8T09qrVnv1or45EMTjfePVuVWFxZrJa%2FFnN3rdxDM7Ul8Zt9J6bZ%2FpTTh8dovKc1KtySfyeEiguqEo1YrTnBL9sIp22tRLXf%2BqZh3J2%2FiqbdxdeuuZhpgTj2xh7b5VbVk9%2FWIHqf153Q6rAcp5uqqzVGty1vgOR3Stn52rs7JnuJ57IJ5VrCZg3FwsGDQ8FSk%2FBBlEAPEKXoBhNdOJM6ofOen1epL2HCnEuUiy2sKGZZwg46p5CJoh3ujpYbiHuzzAdeVOjZSDO4SG9thfsWEknfVhBpM%2BlvjJTPao8qKlnzX1mCgyWIzSjREOCKmTfZkEDpM2Cww0q73KYi3MtawK6NayH0Qsw%2FoAX%2F8YCla61t6lNfBkyT6rkJbKhJJI31%2Bt1Pdy5mQRNwsw44JlZcIPBMTXbUbcxaXoYP%2FJ3LkJ2iOYJ2ZE6CTRtmp7V2sGR9rskUV3DWU9agS1pf%2FhDqy51JJFaRHdXl%2F3japHpEd6uLb%2FHKRcxjfEnpGOogofy%2B9CZtC1%2FyAfD5fZJpVuwQrYTP9oaNDhRx9d2UiJrk552dXScCL%2Fa2xBs4N6b3ZfUxFsh3h0CjYAnER%2BFOPIp0l%2BSUGEbiW5Pk25Dmzud0yDiIE0jD%2B5%2BW8BjqkAUxTnJgC3LP%2BJ5hOZJFW9U8JkueZU1DCKpHHaYu7b8921%2BZ7x730oQVF0Gs%2B7%2BTp2C5QIjwshHtPv0IdFAXSpzEvUXX6gp5uoQx6oQ%2FsuSJgRHGZpWBVINDY9BZsRkquOlIBaIkrEsllmmA6%2BZ9io30PKRbq7su3Qfr%2BEUuq4TlClU27%2BeFGGjyC%2B5uT6BGOK6wEv%2FVwmQg471CnAPN%2Bsiq6PQY%2F&X-Amz-Signature=79f602c68903957fe8a8c858850d9efcc715d5afa4c4d800622981140c27f942&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6UDFNJ2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDCkFVBmvUCSg0L1SPA8ni0MhRgC06QvE4%2BKkEW%2B5JTFwIgLKOYfWOhE3vdc71EuIPOtkyVMgdL9nJ9gkMJOVKbu50qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOzkbQQzy1NAbhPRzCrcA4Ftx3slMq5gd07%2FaWAUoVqAprFHPb6irLqaMrxw2HKn5mJ3hW%2B0691yM%2FEpinIx23uCiSZsRVDhCzy58MUA693o2sIpF11IiRoo%2BpjWnDow2jDGnqz56fb12PM0pFjcJJX0xQYzTsKVbTkkqs44exmdWyCq6Me57rmYZ5jMZM7vVRRmvvDllKELMm3Oq3keybV7Tt1y4mMlAHrzSyJ2Wdx48%2BG2%2F0Csn3Nn9l68stK%2Ff0vdIr9MStz0GHC%2Fyd5rhBaini5ID5H4LGKF9uBvgTtSLHfO2UU5FHAya3568d1%2BvZESF%2BOTOtsEkggvclED52BUhaQkNLjR4Pf8yrDoGRxEHF%2BG10leqHWSSy11XR5kuH7di3llIyTmoq8xOtbh9QsASiw1r7duNE7F5Dh%2BEtpti%2FvU7iKq69Z0i5T2T4XeaQyAYEN%2FL8Vxx0CwYf4TeIfTMkW2Tm26OPRkoxVUdp4caYcJeEEPRIfN94aff38ngUUdG3uaPlGxytytxNSq%2Fkag3gZAKWiDonZ4eQEofOM7FXYMKN1l5c5uyLPYDz2FXU7%2FqLG7VwLYzqhb62JM5apd45jfRvUXhaXDK4InA8huQ40K9k7AW%2B%2FkTWUvpDcZNNGsvGcYOs3Edg1AMO7n5bwGOqUBp4Nm%2FFjZC8Rnu%2Fcjrp1xoCg0CpdjBIGkjGnXnncwZiwvFhotv6VB%2BjCeCH2gm6uUnkhUlsmPBe6vLTWFUzztkIIW1gBfY4H0BUHK0Z6uKbv1woRJzxC%2B0EA3rifgpq99O87Z07eTR6JpY559SOopzlZDmu4vywJyP276cZSI9SQ%2BUCMNSh11dKNvfzyXNovK8Zp03omjCwcQp7eE0r%2F01HioJsIX&X-Amz-Signature=d3367664e6b773cc7d8dabda4853d5b6519f87d64a2dbf7bb44889df66cb3142&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LGSIJUS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDtYHo1K1CH6dYzMKry9RstJFBUSBtchCDkXMKylN6A2gIgA1FDt%2FYegoHDQ3uuMzXk8Qs8NK3Yj5Vj%2Fz4uZQvkyTEqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbWugKCCWPJUC7kDyrcA33m1V1sMA1WM8uipSuBCOugwxhUaC24M3VQvvTm0pO%2B%2FoomThrbNumEP75t2Vr%2Bj3ClFklVBNWgk2wfoDObM86ZjTH8c%2B9yIKEy0PwCP5n7SS5A2P8ajUgqDoHIOTKE%2Bo6AJbwjZq%2BZYBUBnfNT3irH28Vh%2BoQlILE9eS3C6W15iLKjkcqHnahs7AgZn3cKFxIRxaFSC0GsVHCMavlzxs7nenxyfh%2FpPBXlt7CDtVFSRVg9gVuLpBUbNhqB0smvPeux7N8QHdEhe60GopwrwlRY%2Bm303LUVghSJRv%2F2sZX5X7V0eMtKeUScdB%2FLUoe8ezwNQIlVvwEM%2Fi%2BBE7wTFHAQe8%2FghGUdA9JgRVmScQ%2FWHbZ8VrECrIsCyn5pmtMU%2BBmqQgV1uUKO09yqpSgfh8%2FidZuXbRRhiHqvD3yu8UiNW6Qq0YKmm4pTPiAmG7XgGnfpwD2YLClHSGuA4r%2FXVSWonxD8iinBoh%2FAf9g9CmoKsGsT5xseV8418G9hoxyjf%2BwFqV5QcRuQeIdvvTVj4%2BQiAmuFEiwKTONKtGJMkfAk%2FOYw6EXlZSh%2BmZ5usN57TmRaRbADtmQQY3zRAnKWczTv%2BJSJ4qXwOBOBbQUvJ7XX6o3EBkSzLxxC6PbrMJbo5bwGOqUBZYD%2B3VqNhyfCswvE%2FMTUSJvY7bZKCzaAD2wgM1hWpewzYJtPxRnbK%2B9f49CK4KCFi0qSRquHfu0c1J%2B7SgJfOe5Uu6PUHkaGmqygltTSi3tBjB0sJyHbXMEXrweNnGb2Rv2f67eTPQHFlul2flF%2FUsifTY8VPsf1jg5ZLwlG%2BzdN1KpCAFLJIhF0v%2BWtbL5O03vgSIYr2Al%2BRH7JgytE9cZSicBC&X-Amz-Signature=ca21a5cc065305f93ab4f780ba700ceded0f9a675f77290a080c10952f621c20&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LGSIJUS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDtYHo1K1CH6dYzMKry9RstJFBUSBtchCDkXMKylN6A2gIgA1FDt%2FYegoHDQ3uuMzXk8Qs8NK3Yj5Vj%2Fz4uZQvkyTEqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbWugKCCWPJUC7kDyrcA33m1V1sMA1WM8uipSuBCOugwxhUaC24M3VQvvTm0pO%2B%2FoomThrbNumEP75t2Vr%2Bj3ClFklVBNWgk2wfoDObM86ZjTH8c%2B9yIKEy0PwCP5n7SS5A2P8ajUgqDoHIOTKE%2Bo6AJbwjZq%2BZYBUBnfNT3irH28Vh%2BoQlILE9eS3C6W15iLKjkcqHnahs7AgZn3cKFxIRxaFSC0GsVHCMavlzxs7nenxyfh%2FpPBXlt7CDtVFSRVg9gVuLpBUbNhqB0smvPeux7N8QHdEhe60GopwrwlRY%2Bm303LUVghSJRv%2F2sZX5X7V0eMtKeUScdB%2FLUoe8ezwNQIlVvwEM%2Fi%2BBE7wTFHAQe8%2FghGUdA9JgRVmScQ%2FWHbZ8VrECrIsCyn5pmtMU%2BBmqQgV1uUKO09yqpSgfh8%2FidZuXbRRhiHqvD3yu8UiNW6Qq0YKmm4pTPiAmG7XgGnfpwD2YLClHSGuA4r%2FXVSWonxD8iinBoh%2FAf9g9CmoKsGsT5xseV8418G9hoxyjf%2BwFqV5QcRuQeIdvvTVj4%2BQiAmuFEiwKTONKtGJMkfAk%2FOYw6EXlZSh%2BmZ5usN57TmRaRbADtmQQY3zRAnKWczTv%2BJSJ4qXwOBOBbQUvJ7XX6o3EBkSzLxxC6PbrMJbo5bwGOqUBZYD%2B3VqNhyfCswvE%2FMTUSJvY7bZKCzaAD2wgM1hWpewzYJtPxRnbK%2B9f49CK4KCFi0qSRquHfu0c1J%2B7SgJfOe5Uu6PUHkaGmqygltTSi3tBjB0sJyHbXMEXrweNnGb2Rv2f67eTPQHFlul2flF%2FUsifTY8VPsf1jg5ZLwlG%2BzdN1KpCAFLJIhF0v%2BWtbL5O03vgSIYr2Al%2BRH7JgytE9cZSicBC&X-Amz-Signature=89b90f686fbfe9c35fa37708abfc76aefe4a8ea037e1c0cf7cf5166f8ad1f97d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LGSIJUS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDtYHo1K1CH6dYzMKry9RstJFBUSBtchCDkXMKylN6A2gIgA1FDt%2FYegoHDQ3uuMzXk8Qs8NK3Yj5Vj%2Fz4uZQvkyTEqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbWugKCCWPJUC7kDyrcA33m1V1sMA1WM8uipSuBCOugwxhUaC24M3VQvvTm0pO%2B%2FoomThrbNumEP75t2Vr%2Bj3ClFklVBNWgk2wfoDObM86ZjTH8c%2B9yIKEy0PwCP5n7SS5A2P8ajUgqDoHIOTKE%2Bo6AJbwjZq%2BZYBUBnfNT3irH28Vh%2BoQlILE9eS3C6W15iLKjkcqHnahs7AgZn3cKFxIRxaFSC0GsVHCMavlzxs7nenxyfh%2FpPBXlt7CDtVFSRVg9gVuLpBUbNhqB0smvPeux7N8QHdEhe60GopwrwlRY%2Bm303LUVghSJRv%2F2sZX5X7V0eMtKeUScdB%2FLUoe8ezwNQIlVvwEM%2Fi%2BBE7wTFHAQe8%2FghGUdA9JgRVmScQ%2FWHbZ8VrECrIsCyn5pmtMU%2BBmqQgV1uUKO09yqpSgfh8%2FidZuXbRRhiHqvD3yu8UiNW6Qq0YKmm4pTPiAmG7XgGnfpwD2YLClHSGuA4r%2FXVSWonxD8iinBoh%2FAf9g9CmoKsGsT5xseV8418G9hoxyjf%2BwFqV5QcRuQeIdvvTVj4%2BQiAmuFEiwKTONKtGJMkfAk%2FOYw6EXlZSh%2BmZ5usN57TmRaRbADtmQQY3zRAnKWczTv%2BJSJ4qXwOBOBbQUvJ7XX6o3EBkSzLxxC6PbrMJbo5bwGOqUBZYD%2B3VqNhyfCswvE%2FMTUSJvY7bZKCzaAD2wgM1hWpewzYJtPxRnbK%2B9f49CK4KCFi0qSRquHfu0c1J%2B7SgJfOe5Uu6PUHkaGmqygltTSi3tBjB0sJyHbXMEXrweNnGb2Rv2f67eTPQHFlul2flF%2FUsifTY8VPsf1jg5ZLwlG%2BzdN1KpCAFLJIhF0v%2BWtbL5O03vgSIYr2Al%2BRH7JgytE9cZSicBC&X-Amz-Signature=de5676956bb5ed4513c3fc8afd1e79b8693b49c00fd42c18fa57c8d711cb8409&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YWKRSMQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQDnUFf2aAZ478mBux75EIsunqys01zOMEQ4jybU4UtkPQIhAIpFpVUERSAIbNV%2Bpl21vSqJiSVo9RaGnG%2FjiFcqit5uKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzzF13Fo%2BoZuojfYXsq3AMWUmO%2BTtBtS1crgto2dfqEVQJUN5bwkP%2BBtLBasZptQxRF4pQpJ5PoC579gyNEQeYrdaM%2FGPW4Q72rxoRWIaw6kSN2r8TuChVX4NHmWgez%2BKMy3unMqamDtVhgCi1ln7lBNFPQ34Bp2oCDsdt7hfkypCIDX4gx8ll1XwUTGxf0lEV6%2FCklTuI0VLzUIBtXMkYHjV6mbgHg3TZGMbbURlNDtliQtaKyCfX4qhFP2PzQogm5BxBTT7bUA20f27I9sKJB0EzsEGK8VMval54Yhd7fa11zAZthrUtULblSfgt6bo0YEAmVd%2BaopjFjCI8nqkJDYFotkfXvTO5aVkkwcbLZj3PKuVlvR9eptxDnsZp%2F3dFwgup0GjksbOTIEPtbD9i0G6RUiusF8Nn9Uz5TcPp0GbsoRKVh2pdJNdQSLG6aUyTx8ljvPH0wTKrAq1ZZbeuSedbJkZi3fbUEpvcS9%2F9E71IjCgXTRuiNJtMgQUavLERHWjqkcKkmaISy3aeqdTEDTmwdInf7ovsLrdcWkH8973zt8UGk2h%2BQ6lNQqDyn2O61SkWqKXq6w41lDDsyCNfgM5o9D1yGk2VsiyViTAnMFS1Tl9peHnluxV824k9046zVcRkmqaiIctiATzDq5%2BW8BjqkAWFmmEt%2B%2BwZ4ZrHfaeakkpKbXvHGVN0C%2Bke4pWGFwdVbzzty3u3fYaex%2Fyv42j9A0kOLNU4dgrsOxI%2FCImQiePRmV2I4tyxeN0cM5yk%2F9y%2BsjEdot0696pHE1GjirSpf6Ws93XQe7nOseiV2mhiXabiYMLuzYKhMWW3iACA9FTtRYmL4UywwfsKGtLPYDK3Gu0pMiu3faZy%2Fn39RxV9pfr7mfpQn&X-Amz-Signature=5bab47d3fa3cc88cdd48c93b087f8475e46daacad93ea185b0e481b537b99f0e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6LFVYFR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQCYZIO54nBTgIvSgHwQCOwl9Nj5bTnAbKdxTAlhlHZgAwIhAL6fI57fmqVZxYxVSILNOBxNa793zAUHdFYrsIADJcQYKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw6Fa1buglGwWhX3nsq3AMzxKBYvrbGDWuA9BHzpuIs1pUi2aeQt3cT8XSKPmsy6q6hVVX4cs1liMGA8naq%2FySnBuaao%2B5Z%2BN8PRhlvCHhUTmrvPhuzPQBLGuBE7Ombe1fBZoHiXG7EG7Nteo4UoKWLvGZJ9sFNBRavzoJ2X30LR%2BKNZvOkd2zuK%2BtLYYClQ%2F%2BVDMqiZtTm9AfbhNiGY0m2Gcr2CgO3ANaSb4pyDdJ4MjtZJV2LDMNspy5a7E4e0rK6PvaUllcvDIGZaUM6tE5Lxc7mlSAxtT1KGJDCl%2BqgptbX7Rmix3%2BGh6KH%2BTjwNdNPLtRdu5GIkH0b4Jd9EYN0mOWq%2Faztj3kxVn%2BTZvWiar2GELob1nFwH50e5Yb%2Br2XCntTjhQBbOEvqBG0UAgwL3GcH8hs82Woi3c3TczoGNsneYxgwYIvJ21xrftiQ84OitrNpzZJydcAtmDv53xeiCkVphbQSs06evjAb%2Bvvgi%2BQF1CCNa2jTR6MYsF9KDuCB5Vzf79cvAmDIKGZP9%2FQAXkSFBLEGZdcHJxhxRsMI2gzBViiuAkmI8znFg4SExHfr%2FZ41BbxeK4szz354zFuV7W7Dn6D9181qzbbZfqxSGW9Uq5aGli4OU1ER4%2BXuqN6FMhqWXrqlhK1mkDCX6OW8BjqkAY4cXrTfgNAVOg9ZKBYFOhNVxS36w%2BvRfzpRFNHP0rn%2F3AgEUDs8dMvZVG5doo%2FgZwW0ATy1Fdyw1Qj1aZt77G1bZnXRLd8tch6dzLN06DX9mabHF4nzwJlW%2BlO1XvqohJxKgLZaHtt2pAkH9xuuFt7MAq1%2BRZ7P7ND5wO4cP%2F7%2FlMbE9c1uuSmEaHRhBNceNVqhik6EesoCkpn74sOX%2BoZMUqDE&X-Amz-Signature=15c3091c5824a47c1c8240b638e8d95677cc0d5fd2e8f5aa2ab46148006b4dfb&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665W56R4W%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQD%2BfEEkNwr5ZdHX8cNmQszu6AJr7e%2FJxlkEQyT3WmczngIgS2Ctbv6Xhi9H5nRKE9dFBmi51N5oQq3icvuneihtzPMqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLs5pyeI%2F8uTzyV%2FfircA7COiy0jxNV0hsyMvPiVl1UqM7zaLKfesDjN7tIfxMnjgI8z6aGmmg6CD2sNAAPYWWhgkJD6%2BeDb56fMHv7h5DbLkU7uRUNDL%2BptkjAn%2FViY%2FRnsd0FWGTS7RAE3JQILFZttKyIazNHLTcVikFxRLDOPK094pf7Gf6edq6hHojbdBggl3UKL4ckwStT2q8uPs%2FWzFiVh3ma45QVZ3i80OCJoN8GZUz3zdzfnJegaoz8g3liyXOont4usYWfWCCskakvnBCTerh1bJF0PtsXSEUpUeX5Pt%2BmONrhGwDsXf9oiOrb4J15PJrJ8rgWsFEf0Eb6%2BRAV8VGSPZWAqvmCXfxMO%2BSBvAy3K4whoSTvDRjRMI92ZrbfZjQwJR3yeGtu79EyuOsYCHW7IlGXugn6W2ltOSKOWIUoaqDMLZOvLiLkfaKY8Vp026QDMbAobFQmEZ6WEy4b05o28eNRWOf3NT0vqni4MtG54HogP2yILdxZcFIAXiqhBKvFiGgYRNuDpYBnwHUjA6c6XhJNNYD44twudTLdqbk2aHSAWHKkNJun%2F7W%2B1%2BshkXqeBHxPwMJmHFizZI4%2FvF2G%2F8SHaOYj%2B6giH2Xg1Hea0Uy%2FnSrpCFum7ygCut3LycDGirvGdMM7n5bwGOqUBifqy5q0dfontVX0Xj7TW27Nk%2FsuFyt4oYKJFdcFrnanf0saggU3kRnbm%2BhSG6Wuq9nhxF%2FPEzwyXyl%2FlvvE3cOUyppLyctxOXXdWk6V7BHfANw6SEYiCWV3hce8ENvDF0DAjmGlr0RwNZAZBrs0DNiQ4Qr7nRJQO6UjFSwsIBSt%2Bat0mXmukSFnWohAK82Nm9g6PFZLWEZDelAdIs7FU2IxNCeFd&X-Amz-Signature=4530993982f436c6a719cb23797dc0879961e39ef39ce958aecffc7743e73aad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMU5JDYQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCx7oxFZ55vPAirtxxx8x0PDCxEnqqesiYV9YTr2dlDLwIganVSt1XhEQ74B3o7QzS2X4G0yzmgqU1Atkp7Oko4t%2F4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGow2dAyUKN7hEwLCrcA8AX8r%2FlnQEmBaphNGxzgwMmHuGRVXd8Ersu5Nawg7GXK5p%2F0TJ1NOpEw70clfcllDM4QNWHbQ8hdUA0KIeS%2BI%2F13%2FRrd%2B7qMi1QINBCnqmU0DiHkli7Mp9iBtP4YMkTSi%2BHVRH87TG5RY0H6KeD1X%2BTgJCn6byY%2B7b3cWgTPdmzNx7iccEROEfep0PSHHazxv0Kr%2BEcCvwQ1kU%2F62tjqGEL9C30d%2FN8uEVIYZ94%2FSvh%2FLtQBketzjX%2BMoOdrwvRHI9NVyjLJc8%2BqEpoTL2JIgzHlaMTvNjJkTyhtLJjm2b1O7iP%2BC1MhURapr1pPQA%2F7H6uP8WNdu3x0yjWMWtWc%2FPV0IYAOSWRftBLVwZSBHCUZQO4slkfx%2Fkx9ihV67OzWKG6elHz6I%2Ba1SnYbZz7k26iUxSuPp5rIY8IAcPAiwZ28z6S4ZknNDk83j%2F0aqKTSKxy0o1NzGGyAT%2F8hPZDUXtnFuDbF783RqQBlmjFCIWx3bu9rPWTp3wjIWBRmH9UEIGiwvHgsH6wDSd9377djW8qT%2F%2FmELCmtdXuUNketZGOjkyNYrUslQuwINUMTxQTJ%2FZYLQNcsQlZcvF4FZHbsD702dxvQOfEOpuQo2MOcPNmBFu4h7Aw39ew42HXMOPn5bwGOqUBF73DUAzXVprKYN9N3prZ667kqmWxO2dRqUmElqdCcX6hEVi1%2BDsc6nt6AQlOqZULvbF1wqf0G9EzRPdzwFtfsafqB67AcUEhfUfC8CRGKjWS1Wg0w1NRSVICSpdbigkFNq9t8lQ8fn6m%2BiFOkpO124b6Upy2RUPS%2Bh1VX240TPuNno2YVxfsV%2Bw9bJuZr7I8OtS7fl%2B%2FahwCgpCqRp9Cmp5kBYEI&X-Amz-Signature=275b48c1106543facbc8a36444cb2d74fe17cd3b42fbec34cd4c9793a04ae82b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMU5JDYQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCx7oxFZ55vPAirtxxx8x0PDCxEnqqesiYV9YTr2dlDLwIganVSt1XhEQ74B3o7QzS2X4G0yzmgqU1Atkp7Oko4t%2F4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGow2dAyUKN7hEwLCrcA8AX8r%2FlnQEmBaphNGxzgwMmHuGRVXd8Ersu5Nawg7GXK5p%2F0TJ1NOpEw70clfcllDM4QNWHbQ8hdUA0KIeS%2BI%2F13%2FRrd%2B7qMi1QINBCnqmU0DiHkli7Mp9iBtP4YMkTSi%2BHVRH87TG5RY0H6KeD1X%2BTgJCn6byY%2B7b3cWgTPdmzNx7iccEROEfep0PSHHazxv0Kr%2BEcCvwQ1kU%2F62tjqGEL9C30d%2FN8uEVIYZ94%2FSvh%2FLtQBketzjX%2BMoOdrwvRHI9NVyjLJc8%2BqEpoTL2JIgzHlaMTvNjJkTyhtLJjm2b1O7iP%2BC1MhURapr1pPQA%2F7H6uP8WNdu3x0yjWMWtWc%2FPV0IYAOSWRftBLVwZSBHCUZQO4slkfx%2Fkx9ihV67OzWKG6elHz6I%2Ba1SnYbZz7k26iUxSuPp5rIY8IAcPAiwZ28z6S4ZknNDk83j%2F0aqKTSKxy0o1NzGGyAT%2F8hPZDUXtnFuDbF783RqQBlmjFCIWx3bu9rPWTp3wjIWBRmH9UEIGiwvHgsH6wDSd9377djW8qT%2F%2FmELCmtdXuUNketZGOjkyNYrUslQuwINUMTxQTJ%2FZYLQNcsQlZcvF4FZHbsD702dxvQOfEOpuQo2MOcPNmBFu4h7Aw39ew42HXMOPn5bwGOqUBF73DUAzXVprKYN9N3prZ667kqmWxO2dRqUmElqdCcX6hEVi1%2BDsc6nt6AQlOqZULvbF1wqf0G9EzRPdzwFtfsafqB67AcUEhfUfC8CRGKjWS1Wg0w1NRSVICSpdbigkFNq9t8lQ8fn6m%2BiFOkpO124b6Upy2RUPS%2Bh1VX240TPuNno2YVxfsV%2Bw9bJuZr7I8OtS7fl%2B%2FahwCgpCqRp9Cmp5kBYEI&X-Amz-Signature=2eec5a3af9dcaf68bb77f1e422b8636bcbcaf5359f385fb6327126d8581a9175&X-Amz-SignedHeaders=host&x-id=GetObject)

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
