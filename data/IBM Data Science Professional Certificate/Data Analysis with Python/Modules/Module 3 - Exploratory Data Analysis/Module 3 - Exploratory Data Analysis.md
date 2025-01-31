

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPDAELIT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGvEC9mym7opXBLaXjb5kSMeIcAumexrlRg1ZTPhQhBYAiEAnxWCiSFB%2Bqf3MGVgsfps%2B2y030QemyE4Ybzra%2BzLCbcqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIcUpHYD5iMr0yBOtSrcA5oAOtokD%2BdBh3Lwwf1r5vy8SOcowPctLBb%2FaSWCNRyu5eWlM050npHFAiCSia8XbCnFMSeJBpZKC%2FJNn7C7VmooLLv9PtkH5yNVkhvAk01pNpfBI1SVVVYwHPzMuYThKrWlse5y1FjrWvxv3U1PUqNUJDzRaBurIvqZvHed5QV5mxHhJLiTahVeWXgnCauwbFx3Go%2Fa68fri9fXGw0NDsdvlaWp5cTDNmma706sepgZFHgJRie4TIqLwwohk9nz6W4F2Q%2F6%2BDRwGYpj2uJ1ppscAiyNrdaiq9r1QkuFtTqutGDUYPAOBMtTRIB32xN96Q%2FIkjszFj2s8dnAUwvXqiph4TJKduknpsIgLn%2BJDDr9j4Ko743086bIaSYmxbFuoKRL9%2Fw%2FsAMGVnlGzVEGQjTzi0bQUaOVkzzlrq%2B5hoQb7RPe32jU02GvVUCj8DJZfWI%2B13ISbK%2Fq84XZQAe14zMdX2nI8numW7GKczmtXR3%2BUHROzz3KkIVKkMmx6uqH8BR0MR9uC%2FqckCB7uANVmwFqtET7piT7kPfeNVOjXFp2iD4dq9qg1H%2Bi4Op1gJs9ncQp50g1iAT%2Fn4Y%2BYOFE3RkVijbeKytpOXEnbGKDx6menAOXdjeWVomm2aElMPOP87wGOqUBBuze4R3lQuCNO%2BtrwrjDtjLo67HwgZdvH%2BrFkgnIQ6MyCMRroXasSWmLpUGTVe6tXSrlr0S4aEFNQJ7rn62337YUlDcy8MZ%2B9elLuZuAnpmeDt7S1olpUVvtdS%2FrtySosl2JbHw6gEcRdYauUmJCiYfBNRFOm0iTV%2Bf2ncpVIoXOhRa6Pp6OVff2vqBoz9ZYGbQtlm5%2FEyr9i%2BH1MmlmkNmW1Sbx&X-Amz-Signature=ee7d24072f5b46860e95e70fe5bb955525f48ce7536078102c1f23a88087c565&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPDAELIT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGvEC9mym7opXBLaXjb5kSMeIcAumexrlRg1ZTPhQhBYAiEAnxWCiSFB%2Bqf3MGVgsfps%2B2y030QemyE4Ybzra%2BzLCbcqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIcUpHYD5iMr0yBOtSrcA5oAOtokD%2BdBh3Lwwf1r5vy8SOcowPctLBb%2FaSWCNRyu5eWlM050npHFAiCSia8XbCnFMSeJBpZKC%2FJNn7C7VmooLLv9PtkH5yNVkhvAk01pNpfBI1SVVVYwHPzMuYThKrWlse5y1FjrWvxv3U1PUqNUJDzRaBurIvqZvHed5QV5mxHhJLiTahVeWXgnCauwbFx3Go%2Fa68fri9fXGw0NDsdvlaWp5cTDNmma706sepgZFHgJRie4TIqLwwohk9nz6W4F2Q%2F6%2BDRwGYpj2uJ1ppscAiyNrdaiq9r1QkuFtTqutGDUYPAOBMtTRIB32xN96Q%2FIkjszFj2s8dnAUwvXqiph4TJKduknpsIgLn%2BJDDr9j4Ko743086bIaSYmxbFuoKRL9%2Fw%2FsAMGVnlGzVEGQjTzi0bQUaOVkzzlrq%2B5hoQb7RPe32jU02GvVUCj8DJZfWI%2B13ISbK%2Fq84XZQAe14zMdX2nI8numW7GKczmtXR3%2BUHROzz3KkIVKkMmx6uqH8BR0MR9uC%2FqckCB7uANVmwFqtET7piT7kPfeNVOjXFp2iD4dq9qg1H%2Bi4Op1gJs9ncQp50g1iAT%2Fn4Y%2BYOFE3RkVijbeKytpOXEnbGKDx6menAOXdjeWVomm2aElMPOP87wGOqUBBuze4R3lQuCNO%2BtrwrjDtjLo67HwgZdvH%2BrFkgnIQ6MyCMRroXasSWmLpUGTVe6tXSrlr0S4aEFNQJ7rn62337YUlDcy8MZ%2B9elLuZuAnpmeDt7S1olpUVvtdS%2FrtySosl2JbHw6gEcRdYauUmJCiYfBNRFOm0iTV%2Bf2ncpVIoXOhRa6Pp6OVff2vqBoz9ZYGbQtlm5%2FEyr9i%2BH1MmlmkNmW1Sbx&X-Amz-Signature=4ee8001e4aaf09899944c47856ae1833e6d5c8439509bf5dad7f8a71820f215e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPDAELIT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGvEC9mym7opXBLaXjb5kSMeIcAumexrlRg1ZTPhQhBYAiEAnxWCiSFB%2Bqf3MGVgsfps%2B2y030QemyE4Ybzra%2BzLCbcqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIcUpHYD5iMr0yBOtSrcA5oAOtokD%2BdBh3Lwwf1r5vy8SOcowPctLBb%2FaSWCNRyu5eWlM050npHFAiCSia8XbCnFMSeJBpZKC%2FJNn7C7VmooLLv9PtkH5yNVkhvAk01pNpfBI1SVVVYwHPzMuYThKrWlse5y1FjrWvxv3U1PUqNUJDzRaBurIvqZvHed5QV5mxHhJLiTahVeWXgnCauwbFx3Go%2Fa68fri9fXGw0NDsdvlaWp5cTDNmma706sepgZFHgJRie4TIqLwwohk9nz6W4F2Q%2F6%2BDRwGYpj2uJ1ppscAiyNrdaiq9r1QkuFtTqutGDUYPAOBMtTRIB32xN96Q%2FIkjszFj2s8dnAUwvXqiph4TJKduknpsIgLn%2BJDDr9j4Ko743086bIaSYmxbFuoKRL9%2Fw%2FsAMGVnlGzVEGQjTzi0bQUaOVkzzlrq%2B5hoQb7RPe32jU02GvVUCj8DJZfWI%2B13ISbK%2Fq84XZQAe14zMdX2nI8numW7GKczmtXR3%2BUHROzz3KkIVKkMmx6uqH8BR0MR9uC%2FqckCB7uANVmwFqtET7piT7kPfeNVOjXFp2iD4dq9qg1H%2Bi4Op1gJs9ncQp50g1iAT%2Fn4Y%2BYOFE3RkVijbeKytpOXEnbGKDx6menAOXdjeWVomm2aElMPOP87wGOqUBBuze4R3lQuCNO%2BtrwrjDtjLo67HwgZdvH%2BrFkgnIQ6MyCMRroXasSWmLpUGTVe6tXSrlr0S4aEFNQJ7rn62337YUlDcy8MZ%2B9elLuZuAnpmeDt7S1olpUVvtdS%2FrtySosl2JbHw6gEcRdYauUmJCiYfBNRFOm0iTV%2Bf2ncpVIoXOhRa6Pp6OVff2vqBoz9ZYGbQtlm5%2FEyr9i%2BH1MmlmkNmW1Sbx&X-Amz-Signature=c54a96255498fe95f71ee7dee7fc0b82d0c39c9832c1f5a2bf259df2e5e73e84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGO3ZORZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFj7vahhG49gv9QLVlpnnDF%2BaXXzHtg8d0j8p2wxbYT4AiA8Kb8aduM8pBSqxT%2FF%2B%2FZUuKFufp0el%2BehfoB5eqLkOCqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwDFWimuKX%2BKrPtgNKtwDaMXGTrxJJW4TpavIq65Xpzf5therIkzbj35qOWSbFI49u8ltTInnKVSnHZ3EuKai3nh%2FJRyVEWG7nuIDQ98Z2aRD32NMZyKVaYd%2B2Ackmez%2BfWITP0gs2QddoM%2BNMmM8JbR7t7yO6vTmn5kdY0wE6brtmNx84%2BiD8S%2BCLcrO0ueGDmc2rXsJQa2WhlGprbTzwrkRUSBANabD%2BEja1yJMS%2F7nOpFQ5RAXpygi9LiqUYMIZLNYNqBIpzxIPYJUpJyKpkeQtxnwM0pf6x9VJKlDkSf5%2FGcB4gVRvAiQRzUvtP4jyjjAY1Dt8vS%2BCVLgE10rwbAHrSL9qToVesbdTyQJye9JvvJFR1rhJYmua%2BPoM8cnALAG2%2BIzWu1s5PcgwweGbn1B4qDnumSPhgZnDWfOinHRJqTKo45xLtaHcdV7yXFiJJTgpMCYMkQDFEp8pyALow9K9sr4x5Zl1cXHvmO%2FSDbbRrO0U8Lu6PXzkBPc50hCW%2BQyMoqGpx%2Fdbk6rIP7y4LrkEh%2BfUNnb2%2BxCcm40gpgcsLrdYZ%2B8kC2KzhkVnsYCmZ3f9%2F9Gew5pYlREPBWmAxNBg4DK5Dk%2F7WZ3lAI290IoWp95fXD7aVU%2FEgrRB54B%2BXd6B%2BsRvquS9t0wn4%2FzvAY6pgFdxKqMQwOjy90bjjfElu92VD5ObGgqLOJa4zjmGytfJxXjCA%2BdQ0ElX3DDiF5J9baB7srs6R5kuc3Tt%2F6Dhvwx%2FBosYtZWntuaB68%2BPy5tonCBvWCcDQXyzRM%2BR%2BB2WoyTJXk4QUzq7LGD8NRqXFbXTyGFiSkM%2FsVR5kUmDjRn36S4gVQAWPS8gJswJXX8Kl3yvKbuP63TapyAzoRbycryBtWtyVTR&X-Amz-Signature=5651c123704aa2e6c8c99c56eadec380cccd020ce39881f8fa4b436a645ed0b4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGO3ZORZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFj7vahhG49gv9QLVlpnnDF%2BaXXzHtg8d0j8p2wxbYT4AiA8Kb8aduM8pBSqxT%2FF%2B%2FZUuKFufp0el%2BehfoB5eqLkOCqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwDFWimuKX%2BKrPtgNKtwDaMXGTrxJJW4TpavIq65Xpzf5therIkzbj35qOWSbFI49u8ltTInnKVSnHZ3EuKai3nh%2FJRyVEWG7nuIDQ98Z2aRD32NMZyKVaYd%2B2Ackmez%2BfWITP0gs2QddoM%2BNMmM8JbR7t7yO6vTmn5kdY0wE6brtmNx84%2BiD8S%2BCLcrO0ueGDmc2rXsJQa2WhlGprbTzwrkRUSBANabD%2BEja1yJMS%2F7nOpFQ5RAXpygi9LiqUYMIZLNYNqBIpzxIPYJUpJyKpkeQtxnwM0pf6x9VJKlDkSf5%2FGcB4gVRvAiQRzUvtP4jyjjAY1Dt8vS%2BCVLgE10rwbAHrSL9qToVesbdTyQJye9JvvJFR1rhJYmua%2BPoM8cnALAG2%2BIzWu1s5PcgwweGbn1B4qDnumSPhgZnDWfOinHRJqTKo45xLtaHcdV7yXFiJJTgpMCYMkQDFEp8pyALow9K9sr4x5Zl1cXHvmO%2FSDbbRrO0U8Lu6PXzkBPc50hCW%2BQyMoqGpx%2Fdbk6rIP7y4LrkEh%2BfUNnb2%2BxCcm40gpgcsLrdYZ%2B8kC2KzhkVnsYCmZ3f9%2F9Gew5pYlREPBWmAxNBg4DK5Dk%2F7WZ3lAI290IoWp95fXD7aVU%2FEgrRB54B%2BXd6B%2BsRvquS9t0wn4%2FzvAY6pgFdxKqMQwOjy90bjjfElu92VD5ObGgqLOJa4zjmGytfJxXjCA%2BdQ0ElX3DDiF5J9baB7srs6R5kuc3Tt%2F6Dhvwx%2FBosYtZWntuaB68%2BPy5tonCBvWCcDQXyzRM%2BR%2BB2WoyTJXk4QUzq7LGD8NRqXFbXTyGFiSkM%2FsVR5kUmDjRn36S4gVQAWPS8gJswJXX8Kl3yvKbuP63TapyAzoRbycryBtWtyVTR&X-Amz-Signature=150c9ba543667e7a62f3f2687b482d07d575c13153d2369adf78d7a900506a0a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGO3ZORZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFj7vahhG49gv9QLVlpnnDF%2BaXXzHtg8d0j8p2wxbYT4AiA8Kb8aduM8pBSqxT%2FF%2B%2FZUuKFufp0el%2BehfoB5eqLkOCqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwDFWimuKX%2BKrPtgNKtwDaMXGTrxJJW4TpavIq65Xpzf5therIkzbj35qOWSbFI49u8ltTInnKVSnHZ3EuKai3nh%2FJRyVEWG7nuIDQ98Z2aRD32NMZyKVaYd%2B2Ackmez%2BfWITP0gs2QddoM%2BNMmM8JbR7t7yO6vTmn5kdY0wE6brtmNx84%2BiD8S%2BCLcrO0ueGDmc2rXsJQa2WhlGprbTzwrkRUSBANabD%2BEja1yJMS%2F7nOpFQ5RAXpygi9LiqUYMIZLNYNqBIpzxIPYJUpJyKpkeQtxnwM0pf6x9VJKlDkSf5%2FGcB4gVRvAiQRzUvtP4jyjjAY1Dt8vS%2BCVLgE10rwbAHrSL9qToVesbdTyQJye9JvvJFR1rhJYmua%2BPoM8cnALAG2%2BIzWu1s5PcgwweGbn1B4qDnumSPhgZnDWfOinHRJqTKo45xLtaHcdV7yXFiJJTgpMCYMkQDFEp8pyALow9K9sr4x5Zl1cXHvmO%2FSDbbRrO0U8Lu6PXzkBPc50hCW%2BQyMoqGpx%2Fdbk6rIP7y4LrkEh%2BfUNnb2%2BxCcm40gpgcsLrdYZ%2B8kC2KzhkVnsYCmZ3f9%2F9Gew5pYlREPBWmAxNBg4DK5Dk%2F7WZ3lAI290IoWp95fXD7aVU%2FEgrRB54B%2BXd6B%2BsRvquS9t0wn4%2FzvAY6pgFdxKqMQwOjy90bjjfElu92VD5ObGgqLOJa4zjmGytfJxXjCA%2BdQ0ElX3DDiF5J9baB7srs6R5kuc3Tt%2F6Dhvwx%2FBosYtZWntuaB68%2BPy5tonCBvWCcDQXyzRM%2BR%2BB2WoyTJXk4QUzq7LGD8NRqXFbXTyGFiSkM%2FsVR5kUmDjRn36S4gVQAWPS8gJswJXX8Kl3yvKbuP63TapyAzoRbycryBtWtyVTR&X-Amz-Signature=02662b0ad303b8c82d009826ed2dab9f4b1435c8fe2b3af1cd1728080488ae60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGO3ZORZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFj7vahhG49gv9QLVlpnnDF%2BaXXzHtg8d0j8p2wxbYT4AiA8Kb8aduM8pBSqxT%2FF%2B%2FZUuKFufp0el%2BehfoB5eqLkOCqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwDFWimuKX%2BKrPtgNKtwDaMXGTrxJJW4TpavIq65Xpzf5therIkzbj35qOWSbFI49u8ltTInnKVSnHZ3EuKai3nh%2FJRyVEWG7nuIDQ98Z2aRD32NMZyKVaYd%2B2Ackmez%2BfWITP0gs2QddoM%2BNMmM8JbR7t7yO6vTmn5kdY0wE6brtmNx84%2BiD8S%2BCLcrO0ueGDmc2rXsJQa2WhlGprbTzwrkRUSBANabD%2BEja1yJMS%2F7nOpFQ5RAXpygi9LiqUYMIZLNYNqBIpzxIPYJUpJyKpkeQtxnwM0pf6x9VJKlDkSf5%2FGcB4gVRvAiQRzUvtP4jyjjAY1Dt8vS%2BCVLgE10rwbAHrSL9qToVesbdTyQJye9JvvJFR1rhJYmua%2BPoM8cnALAG2%2BIzWu1s5PcgwweGbn1B4qDnumSPhgZnDWfOinHRJqTKo45xLtaHcdV7yXFiJJTgpMCYMkQDFEp8pyALow9K9sr4x5Zl1cXHvmO%2FSDbbRrO0U8Lu6PXzkBPc50hCW%2BQyMoqGpx%2Fdbk6rIP7y4LrkEh%2BfUNnb2%2BxCcm40gpgcsLrdYZ%2B8kC2KzhkVnsYCmZ3f9%2F9Gew5pYlREPBWmAxNBg4DK5Dk%2F7WZ3lAI290IoWp95fXD7aVU%2FEgrRB54B%2BXd6B%2BsRvquS9t0wn4%2FzvAY6pgFdxKqMQwOjy90bjjfElu92VD5ObGgqLOJa4zjmGytfJxXjCA%2BdQ0ElX3DDiF5J9baB7srs6R5kuc3Tt%2F6Dhvwx%2FBosYtZWntuaB68%2BPy5tonCBvWCcDQXyzRM%2BR%2BB2WoyTJXk4QUzq7LGD8NRqXFbXTyGFiSkM%2FsVR5kUmDjRn36S4gVQAWPS8gJswJXX8Kl3yvKbuP63TapyAzoRbycryBtWtyVTR&X-Amz-Signature=aa7f31f6e1159fac7af543fb2e56e183a0b7c4879e7a6cfdc5a34392a689d7dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGO3ZORZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFj7vahhG49gv9QLVlpnnDF%2BaXXzHtg8d0j8p2wxbYT4AiA8Kb8aduM8pBSqxT%2FF%2B%2FZUuKFufp0el%2BehfoB5eqLkOCqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwDFWimuKX%2BKrPtgNKtwDaMXGTrxJJW4TpavIq65Xpzf5therIkzbj35qOWSbFI49u8ltTInnKVSnHZ3EuKai3nh%2FJRyVEWG7nuIDQ98Z2aRD32NMZyKVaYd%2B2Ackmez%2BfWITP0gs2QddoM%2BNMmM8JbR7t7yO6vTmn5kdY0wE6brtmNx84%2BiD8S%2BCLcrO0ueGDmc2rXsJQa2WhlGprbTzwrkRUSBANabD%2BEja1yJMS%2F7nOpFQ5RAXpygi9LiqUYMIZLNYNqBIpzxIPYJUpJyKpkeQtxnwM0pf6x9VJKlDkSf5%2FGcB4gVRvAiQRzUvtP4jyjjAY1Dt8vS%2BCVLgE10rwbAHrSL9qToVesbdTyQJye9JvvJFR1rhJYmua%2BPoM8cnALAG2%2BIzWu1s5PcgwweGbn1B4qDnumSPhgZnDWfOinHRJqTKo45xLtaHcdV7yXFiJJTgpMCYMkQDFEp8pyALow9K9sr4x5Zl1cXHvmO%2FSDbbRrO0U8Lu6PXzkBPc50hCW%2BQyMoqGpx%2Fdbk6rIP7y4LrkEh%2BfUNnb2%2BxCcm40gpgcsLrdYZ%2B8kC2KzhkVnsYCmZ3f9%2F9Gew5pYlREPBWmAxNBg4DK5Dk%2F7WZ3lAI290IoWp95fXD7aVU%2FEgrRB54B%2BXd6B%2BsRvquS9t0wn4%2FzvAY6pgFdxKqMQwOjy90bjjfElu92VD5ObGgqLOJa4zjmGytfJxXjCA%2BdQ0ElX3DDiF5J9baB7srs6R5kuc3Tt%2F6Dhvwx%2FBosYtZWntuaB68%2BPy5tonCBvWCcDQXyzRM%2BR%2BB2WoyTJXk4QUzq7LGD8NRqXFbXTyGFiSkM%2FsVR5kUmDjRn36S4gVQAWPS8gJswJXX8Kl3yvKbuP63TapyAzoRbycryBtWtyVTR&X-Amz-Signature=b69aee00da5d7c5a113ae0dad49ad4a0ea26e73e8ac0506d17fe144e0937bb3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGO3ZORZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFj7vahhG49gv9QLVlpnnDF%2BaXXzHtg8d0j8p2wxbYT4AiA8Kb8aduM8pBSqxT%2FF%2B%2FZUuKFufp0el%2BehfoB5eqLkOCqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwDFWimuKX%2BKrPtgNKtwDaMXGTrxJJW4TpavIq65Xpzf5therIkzbj35qOWSbFI49u8ltTInnKVSnHZ3EuKai3nh%2FJRyVEWG7nuIDQ98Z2aRD32NMZyKVaYd%2B2Ackmez%2BfWITP0gs2QddoM%2BNMmM8JbR7t7yO6vTmn5kdY0wE6brtmNx84%2BiD8S%2BCLcrO0ueGDmc2rXsJQa2WhlGprbTzwrkRUSBANabD%2BEja1yJMS%2F7nOpFQ5RAXpygi9LiqUYMIZLNYNqBIpzxIPYJUpJyKpkeQtxnwM0pf6x9VJKlDkSf5%2FGcB4gVRvAiQRzUvtP4jyjjAY1Dt8vS%2BCVLgE10rwbAHrSL9qToVesbdTyQJye9JvvJFR1rhJYmua%2BPoM8cnALAG2%2BIzWu1s5PcgwweGbn1B4qDnumSPhgZnDWfOinHRJqTKo45xLtaHcdV7yXFiJJTgpMCYMkQDFEp8pyALow9K9sr4x5Zl1cXHvmO%2FSDbbRrO0U8Lu6PXzkBPc50hCW%2BQyMoqGpx%2Fdbk6rIP7y4LrkEh%2BfUNnb2%2BxCcm40gpgcsLrdYZ%2B8kC2KzhkVnsYCmZ3f9%2F9Gew5pYlREPBWmAxNBg4DK5Dk%2F7WZ3lAI290IoWp95fXD7aVU%2FEgrRB54B%2BXd6B%2BsRvquS9t0wn4%2FzvAY6pgFdxKqMQwOjy90bjjfElu92VD5ObGgqLOJa4zjmGytfJxXjCA%2BdQ0ElX3DDiF5J9baB7srs6R5kuc3Tt%2F6Dhvwx%2FBosYtZWntuaB68%2BPy5tonCBvWCcDQXyzRM%2BR%2BB2WoyTJXk4QUzq7LGD8NRqXFbXTyGFiSkM%2FsVR5kUmDjRn36S4gVQAWPS8gJswJXX8Kl3yvKbuP63TapyAzoRbycryBtWtyVTR&X-Amz-Signature=794675f7917d619b668e0c41eee1c73d4ba2b6fe101401c048cfcb5d44edb6c2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPNZTBRG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTHgofDEBt2HCFT5cutXCNrfjJcbL2zX%2FpyJCm9%2F6ShQIhAL%2BIaq735ZXqwqaRfVf5nr%2F%2F6KK9MsQtV0UOD%2ByZPxGoKogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwnDydFl8LuzRGdDQsq3AOnZjgTgnUqLf7lbvaMzSNNYKEM3KAR4vWquDnafoPueCEG1jbblLkGdZwaFbVrGZTASsEuI5IbGx8%2BwO7WBp3vWZtVJeKWIIgx4ZD4kYUqzpKJYljy7V5MZuDUNQNZ2uVm0KF3qGNA%2FjAH%2FQznO6JJVxWBl8zpnHGJphfTpaR2oKvqcsmDlhrNoRZDwWHeA5qUj%2FGXLdAatvcgorClfhjZvm7TZB6pFcSfyna33ZZZ%2BIIQSjg4D7y%2FGWMdvzXVzgGWEMtxquy7yWhL6mJEUIiNFpFyPgUk%2Bys5jJRpUB5pH%2Be5gjN3uctDMUdkxn4nGoYDjuv5O%2BZQEkdM7EbRTWAktM992GNroRFkN0lVW5NYbhsnoo7PTEiGrGzxuyVuagP51ZX9w7Y5IwgpJwekUivtZhbCoO1vLayXJco%2FeSvIcoRHUmN9WYHLgzvGl0VmMRqV6W%2BaUUXgSjkmo6Uj8N23SaHBvEtVydvo0s0Lm2za0g0a1JvWg99Kp0G8EvGBCsG0g93rLzBY1M%2BGuxqVM0Gwtveqio9swU%2BOT7251otB5JEJjnDAOfEwRtRVxX22BKVO3MUhbjfLCtGh1CXw10JhCVWZCUUz4wHvqGggb9eGJRNgp3t9te%2FfVrCFJzCxj%2FO8BjqkAZApxaPY%2F03FhcRsen28b6krmo%2F09O%2BvTMldLUMrcMrQuYLoeVzpuiDgecqZ0G%2B8KE5tPQu8XV4HyHUhZCaaVA%2FRNpYDvexdyFemDHNnRSxrX9vIwcNlmRWkK%2FjJzjZXTZSfvTheTywD2%2BObzYvFRR0RTpYior%2Bzmb%2FYt4Qsl%2Bix1ehyRJEqt7Y9lX5XxzKPsILP8gyV7kCl4N9LFytd8gQnNtK9&X-Amz-Signature=efee059bb02e86b0824f256ac3eef8bb19177a980990e7f3b7c4b5125c79ce8d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWWBYX6T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU0spIVkY8ywDpmTgQGpLmLSXK%2Bt2Wa6s2pLZX0p8j%2BAiEA%2FV%2BC3Gp0woGtJKJvPbBjBhX4DIGXnuNduGcjFEJWvv8qiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGxzB9BACJhLS67gGSrcAwEtrgJz4SZ1UZQt19f8IV6Se9bBEc6hceAsme2nKdLlcjxKE8q2hmpPFhFoILKw292aOLML%2Fy3vqwvWPVEjRSUzGcTTnUpOigKIiK2c6xR63%2BNWmSl%2BpkdHRz%2Bpxlw7w%2BHi8guS7Pk%2BxQdLzCFqpE2LMyxSC5GeXRPcreLmXT5lBvSAfmsDzQROdqCCELcDyBQLJ3HyPO3cG9sj0ZPl4My9LWO1vbddW2gCm%2BZwH0To%2BuK5fNQRPEfwxe%2FZ10rCiNm2YIoXVuMTasS%2BTnSWwfU%2Fmmbkbad5MUXyzEHz3bXwpp8h5hLr1Neg0p7BseBrUJEJDDOGwoNaBaAADZJ%2F2CTLLRsx79TRNtIQB2zThXyzibePL%2Fuvi%2BEgcurYB5DGHP3IPbFZAgQIavaU%2F7%2F9l1AEmcR0TGAmyia6BGFGqvGg7KVxD5I8DYdNfwMbdxbN3jR40mZFmPmOaP6Wpwr4%2FAhkAQ5XD6qDlqFCJvjvjsH%2BHPFnb%2BzYh9e7vWYkFLed7kxvnnnSvg8QKyZ6EPeaIx8LzDCPvATbUGbvIXWJJl51H3fgGjGOZcFb5IrZwMWS0JCRN4wYkTta4BaBNRPvbV%2Bezk15bs4zSvlgW5ktSXYSemA%2Fv%2FF4tmGioKnYMOiQ87wGOqUBK0Ngj0g45QY5R9%2By6NxRxyT02wk014m40pEP3NVJ6pNo4BZ3Bq%2Bdp%2F8fF66qIJwiRTRiq2If5ePUoSGVxf%2Bu8WySXcuv44CFA5wSSmNY2AiWq8rkcV%2BZVcVD9fQJfoliRM7A1uelzAK9YTytlIicOs%2B9Rbw00cUpKVKqmxQyCne3BCywmy0R5xSDXXAi630gWJU12Bhgn%2FT9q6xe9hIcTO74DVNE&X-Amz-Signature=0e717250234ea1fbb55b8cfe70ea00f4f18e527355e5363adbf706d5b730251c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGO3ZORZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFj7vahhG49gv9QLVlpnnDF%2BaXXzHtg8d0j8p2wxbYT4AiA8Kb8aduM8pBSqxT%2FF%2B%2FZUuKFufp0el%2BehfoB5eqLkOCqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwDFWimuKX%2BKrPtgNKtwDaMXGTrxJJW4TpavIq65Xpzf5therIkzbj35qOWSbFI49u8ltTInnKVSnHZ3EuKai3nh%2FJRyVEWG7nuIDQ98Z2aRD32NMZyKVaYd%2B2Ackmez%2BfWITP0gs2QddoM%2BNMmM8JbR7t7yO6vTmn5kdY0wE6brtmNx84%2BiD8S%2BCLcrO0ueGDmc2rXsJQa2WhlGprbTzwrkRUSBANabD%2BEja1yJMS%2F7nOpFQ5RAXpygi9LiqUYMIZLNYNqBIpzxIPYJUpJyKpkeQtxnwM0pf6x9VJKlDkSf5%2FGcB4gVRvAiQRzUvtP4jyjjAY1Dt8vS%2BCVLgE10rwbAHrSL9qToVesbdTyQJye9JvvJFR1rhJYmua%2BPoM8cnALAG2%2BIzWu1s5PcgwweGbn1B4qDnumSPhgZnDWfOinHRJqTKo45xLtaHcdV7yXFiJJTgpMCYMkQDFEp8pyALow9K9sr4x5Zl1cXHvmO%2FSDbbRrO0U8Lu6PXzkBPc50hCW%2BQyMoqGpx%2Fdbk6rIP7y4LrkEh%2BfUNnb2%2BxCcm40gpgcsLrdYZ%2B8kC2KzhkVnsYCmZ3f9%2F9Gew5pYlREPBWmAxNBg4DK5Dk%2F7WZ3lAI290IoWp95fXD7aVU%2FEgrRB54B%2BXd6B%2BsRvquS9t0wn4%2FzvAY6pgFdxKqMQwOjy90bjjfElu92VD5ObGgqLOJa4zjmGytfJxXjCA%2BdQ0ElX3DDiF5J9baB7srs6R5kuc3Tt%2F6Dhvwx%2FBosYtZWntuaB68%2BPy5tonCBvWCcDQXyzRM%2BR%2BB2WoyTJXk4QUzq7LGD8NRqXFbXTyGFiSkM%2FsVR5kUmDjRn36S4gVQAWPS8gJswJXX8Kl3yvKbuP63TapyAzoRbycryBtWtyVTR&X-Amz-Signature=1336a543b03136b37780b7e816ebaa0f41f21709e873961b6f2ea944d6a7d63d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGO3ZORZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFj7vahhG49gv9QLVlpnnDF%2BaXXzHtg8d0j8p2wxbYT4AiA8Kb8aduM8pBSqxT%2FF%2B%2FZUuKFufp0el%2BehfoB5eqLkOCqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwDFWimuKX%2BKrPtgNKtwDaMXGTrxJJW4TpavIq65Xpzf5therIkzbj35qOWSbFI49u8ltTInnKVSnHZ3EuKai3nh%2FJRyVEWG7nuIDQ98Z2aRD32NMZyKVaYd%2B2Ackmez%2BfWITP0gs2QddoM%2BNMmM8JbR7t7yO6vTmn5kdY0wE6brtmNx84%2BiD8S%2BCLcrO0ueGDmc2rXsJQa2WhlGprbTzwrkRUSBANabD%2BEja1yJMS%2F7nOpFQ5RAXpygi9LiqUYMIZLNYNqBIpzxIPYJUpJyKpkeQtxnwM0pf6x9VJKlDkSf5%2FGcB4gVRvAiQRzUvtP4jyjjAY1Dt8vS%2BCVLgE10rwbAHrSL9qToVesbdTyQJye9JvvJFR1rhJYmua%2BPoM8cnALAG2%2BIzWu1s5PcgwweGbn1B4qDnumSPhgZnDWfOinHRJqTKo45xLtaHcdV7yXFiJJTgpMCYMkQDFEp8pyALow9K9sr4x5Zl1cXHvmO%2FSDbbRrO0U8Lu6PXzkBPc50hCW%2BQyMoqGpx%2Fdbk6rIP7y4LrkEh%2BfUNnb2%2BxCcm40gpgcsLrdYZ%2B8kC2KzhkVnsYCmZ3f9%2F9Gew5pYlREPBWmAxNBg4DK5Dk%2F7WZ3lAI290IoWp95fXD7aVU%2FEgrRB54B%2BXd6B%2BsRvquS9t0wn4%2FzvAY6pgFdxKqMQwOjy90bjjfElu92VD5ObGgqLOJa4zjmGytfJxXjCA%2BdQ0ElX3DDiF5J9baB7srs6R5kuc3Tt%2F6Dhvwx%2FBosYtZWntuaB68%2BPy5tonCBvWCcDQXyzRM%2BR%2BB2WoyTJXk4QUzq7LGD8NRqXFbXTyGFiSkM%2FsVR5kUmDjRn36S4gVQAWPS8gJswJXX8Kl3yvKbuP63TapyAzoRbycryBtWtyVTR&X-Amz-Signature=5bd55e21471a57de3f2edc4ce960a3991b75199cf90dd31767c5bb12911b923a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGO3ZORZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFj7vahhG49gv9QLVlpnnDF%2BaXXzHtg8d0j8p2wxbYT4AiA8Kb8aduM8pBSqxT%2FF%2B%2FZUuKFufp0el%2BehfoB5eqLkOCqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwDFWimuKX%2BKrPtgNKtwDaMXGTrxJJW4TpavIq65Xpzf5therIkzbj35qOWSbFI49u8ltTInnKVSnHZ3EuKai3nh%2FJRyVEWG7nuIDQ98Z2aRD32NMZyKVaYd%2B2Ackmez%2BfWITP0gs2QddoM%2BNMmM8JbR7t7yO6vTmn5kdY0wE6brtmNx84%2BiD8S%2BCLcrO0ueGDmc2rXsJQa2WhlGprbTzwrkRUSBANabD%2BEja1yJMS%2F7nOpFQ5RAXpygi9LiqUYMIZLNYNqBIpzxIPYJUpJyKpkeQtxnwM0pf6x9VJKlDkSf5%2FGcB4gVRvAiQRzUvtP4jyjjAY1Dt8vS%2BCVLgE10rwbAHrSL9qToVesbdTyQJye9JvvJFR1rhJYmua%2BPoM8cnALAG2%2BIzWu1s5PcgwweGbn1B4qDnumSPhgZnDWfOinHRJqTKo45xLtaHcdV7yXFiJJTgpMCYMkQDFEp8pyALow9K9sr4x5Zl1cXHvmO%2FSDbbRrO0U8Lu6PXzkBPc50hCW%2BQyMoqGpx%2Fdbk6rIP7y4LrkEh%2BfUNnb2%2BxCcm40gpgcsLrdYZ%2B8kC2KzhkVnsYCmZ3f9%2F9Gew5pYlREPBWmAxNBg4DK5Dk%2F7WZ3lAI290IoWp95fXD7aVU%2FEgrRB54B%2BXd6B%2BsRvquS9t0wn4%2FzvAY6pgFdxKqMQwOjy90bjjfElu92VD5ObGgqLOJa4zjmGytfJxXjCA%2BdQ0ElX3DDiF5J9baB7srs6R5kuc3Tt%2F6Dhvwx%2FBosYtZWntuaB68%2BPy5tonCBvWCcDQXyzRM%2BR%2BB2WoyTJXk4QUzq7LGD8NRqXFbXTyGFiSkM%2FsVR5kUmDjRn36S4gVQAWPS8gJswJXX8Kl3yvKbuP63TapyAzoRbycryBtWtyVTR&X-Amz-Signature=2509b74b7ab3cc58c47871e719ffb95c3871acd45ade103251f7eb02424f2e83&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPRTW2VG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDJfKtrdV1Qby4QZmDYdBqg4po%2FyZoQorBEIKOd68RnLAiBsDZAumAk62nVKinQ6PLq3vef7KwK05spnpi16BVOTFyqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIyq30WeSOFc7JudMKtwDefVxH7CiGe3qmMHZuJeM017v8f6ej4NgN6pYWXBwluv7XlgzO4LSrtFibMnkQ%2BkmpxbBoogZSJGg325OFwI6uHjAw2qb2VZOgN1ThMBeXRZYSsIJo0Fn%2FLa9rzm%2BYQqfM%2FC%2BH4I5XjaPFhHqOywdqll2AH1K4ZlDz923XswzBMa8X4y32gGJpev6q7M9mIYt4jXWWCXm58%2FJjYIq4Ce0gdjFXWXLMJ%2Fmt71tegN8YyqPiUTpjPWjRhSkT%2FeMqzNY358z%2BrLwwD8G3BCdIF3F1GdqVTCCZWtiLtNi9TdhjskiOiww20LqhsmDWBFcYeGPLxgnrdLbduceulPj8qWtaLC%2BrRRfGLMwJYdtcI9jvATRCBh4Y71MRChyEiCEsjgThzp2yVQNfpG4Xdbx1ivT8HUb1fJZFwWGFAKIzOqWbFEa07eAnOHBnJUTs8ROXYwJDDw4BlE%2FpVKF9XQhzfEziRicsVzQ71YhQWAdx3QXDGkVz2bbAZE4xStzhUzcW8ipEa03ZOgfdLi6kThpwapIKpRN5AJU%2B4F%2BchhnQ%2BBMzYMTxrzeAtfeeSi9CYM%2Bx5hjSNAgmM1eL8z0KZwGaK8f7uMD1h2jknD12pUoB3Q73IHmZVKU6iLJVXDUosUwpo%2FzvAY6pgGqmj32rFyQxl3tgRHh00tj72oq6BTHusZxNnPDbrqCHQs6%2FkGucHE5B2r5GfydlPvt4NujJuNnCUFk3PzHSKpbJa%2BgMHSGf73e8AEZZ%2B5Sw1bcYlaX3pGsCUQVvryDkSd8yyKoxkwnFzH3ng045oGqlxM0c9Pyhs%2FvO5jIetOKQrHDXdkfche787oYXna7FI8FCNviZjJ7bwVcaEdQ0nvI9XRaGJSt&X-Amz-Signature=03ecbbb1abff1972e635503f47c5b63fac31ff10c8263f489043fbc6f5dfa927&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIYOGNJ4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPamhJYXqozncNFHk%2FAo9VY%2FCcXw36XtA9D4hVoOzTYQIhAJ%2FXfmkXnwwVVuRK52N0LZaUKVMSWmTVlLW7q4jkTR5LKogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw3qup8tsbqPUyuxIMq3ANgNs5W66ksSlEB6RK7i8yOxzCMcXFnhwIA0yVnh5vXRDKAyCMWMKLlhYdWKMlosKDILVk4RsTDqNIKkskcWUScqYtbSiaTABakq8cgvNiva9JVULvnCOfFjPHFgXxGqxy4BFY%2F5HC83lBV93sdXXyesiljmaueqadlpMzTHQcPWKLl1WLwpzzv8ENt7uFxWWrwOOVgqlWyWxy5TpCmpNEoqrT2BYXVpm6ZgdhEdHu2GjQcZVnor%2FlNz82xT6vrKhermwjH5NeHzVjK8be8VpcYtm26Ydhmfd7I1L20qwVrlZr7ouaepyj2n9GrXY5M7Hf%2Fn8TNGNU1RA3nUUElDheMlmsJS%2FnrBdXWtl87EpYWbDFGuCyKM0lfKAe2QzKM4K999UoX%2FApau%2BlEB9wA8mh311R4jC%2BqaFcL5sG1YLZ0xc6CsHDaAkekGS%2FpFQGjeVhyICJmZFCZmCKyiGTk0%2B0IPrQnzhwKQf9nMeg85mDqu%2B41zBZySzXoKKWkYaJ0T4epSycVcBMsiJaj8pTTqG4VR4wbtB0Pc3ePFyTj7FrHslIrcpMvm%2FCFw0S54B8kRQ0KJQPk1fhRlrRT21%2F%2FTGGkjy6fcFo369zPAf1nN0J7DmsVbp9L%2Fb9lSmQdhzDQj%2FO8BjqkAft8oK1b8PLlve%2Fel0YXYT%2FjUyX5r11hNetoOGwuIk8lx9EDnU9sk8703Q6oAoDKPLLm5K0L8dH8c2nBhO9Da%2FcMIvRyXpduMLKFEjj%2B3T4C4lJdI4xybfuKA8rSoFd9fe%2BlXwfYzKOzwgf2%2FQazRsZaGkxEa4G70UZelx5gJaNx8dSRAhxMwsIGbwRnmBXj10omP5Shv1JesFMKRM4mCnh5UNPw&X-Amz-Signature=be2f9801828cc073acd1fb86f6327b8996d363d7b6ba49893f3b5179c87a3ddf&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIPCAFWJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD63oHPhgaStpESqW9LcX2GHBJos59c118wMpzCYFmlUgIhAJdQscT%2BErnwcqX%2Bx%2FH0tcCSSvKBNbcPL0WpoCxFgpAmKogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzWn83Uy7%2BW%2FduguVQq3AMZOmvgXtfvDTTkIiVXswGd%2Ff08pYWMJvNfeHcFJKh2C8PhMsaj5B8TiSFmbmdJ%2Fq4iiDD9KdsWBurZJ26IyLJLrh8BoIiua5LofuKpEKu3jaZ6AKGM7JF2O4zvbc9A%2FDiq4Va1oxsLPNyLxfV0tzEOPR5zQRPLIaIthJFf1NiF7HySVS9sVv%2BzKjepOQfCw6XSk3JcRTiqbctgQLFE3tVP7NbUTW53UfK1uE5h7U1IbzIIx09ZiRsnbpSLYV%2BjbcSvS%2BydFscXDfsaXIzODEDV7rd69%2BPT5XlS%2BwcHO538MW3BYlDlZMAfxMiWOAX43adaVbSxDj7NGpX7qVyveRdBndilplusT130E7OjDdRH7LBM5jTBXSg4Guh%2FdSQa1QihQUV9yhMQm3Et4Gc3oL%2F9AKnytOThKpmGTPV9yY3YGJCVuo8sK8hm3Yhd2uqQ2zWWdI92MUsg7FrQUZOVh9gpYVutN2f5RuxB6%2FQWnxguqA8G9%2FneWGqQ6s16cEZAvxbryelLxxCDlbB5XzJqsAFEIT23fYn98eoSyZbNdSw%2FV%2F5XFPtHVESVmfRiRZ3pXaW%2BI05pl4ijstfmsQasNiB9Es%2F0aIGG7NFHBzsA8HYVeCrnnnMRJga7e3W6%2FDDOj%2FO8BjqkAVwBHWz0Syl9YsgOWfNga0fXWyfW49l0qDvatHvIbFD5UvE5SXEjwGroYoXhwk8FSObfDOpGBvlbFklIENBgfJ%2FL5N0Zsdq%2FF2QBCRe0H7FfNQzrJsSGMxxExjfgExAWQ75BhvK7IqG8uhA2vS%2F%2FRVwQFUCWDAyxSO%2BzZBApSPWt6J0omYR1Ml0jT82s2ULgyzBU6pMOlyizQIZ3m%2FS%2BpnU96XYe&X-Amz-Signature=fe56418223a7dcef1885675edea4725343c3b3bbbff05946ccc3268cb08dd2c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZACMBE5U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG5jfEh8ak6%2BH4tTeWASpuuTkJy%2FdFf7I9dMTQQjMdB3AiEAungqsfdSMJJY1vAf6woSU9%2FjSd1wDsfQu5366nAj020qiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMIMDQNfJh0b2BY6aircA8mYV2%2BKddQWjtlfq8jAK3PbbyjhkBhnvOKuOYQIsNh4nB2JYH3nuKO1oQgo3f1A4mef09fqsTQ9Q9Z4OjEHBujRRzYfJsuw%2BvTb2OgIatknQaPSB5ChhL6bNSKmBnVfmp21zdPAcVqpNH5Fq%2F0ZCZE7w4CG8y927Q1m7uEQQFmFv9KKIcJqKLMUpw8xQMTDbBtY0Rej3UZkKV1wfh%2BRbKtcGOn9Q19FQUv%2BKqkByNN8ixj7zmTNvepUI80Oso4VS%2FTlLnpOV3qYyXeghcXsp4vFxOp5ZlPbwds%2BNpL%2F9EG5QCiITq6Vqhmhm%2BVlP1uDUew1ZehTtUOm5AGP6daU4Id1uuyMEayWwKwaE81N%2BUDTntAvDXb392m2B2Im9ElAA4Ehktp2S6K5JbIF6mBfv%2F0cZWZx6KOC5MXs6ILZzhs8kwuPQleSGJIcIRCPJLuQ13sL5hk2q49ADOWxNLQNRxFyEig7lj3L6mFi06r%2FfJ0dJegIamk7JTVTPP69N6ityEQphqBvo9Z74fgMu8JX%2Fs7EReIfYsN5pCbBlRJ6uI556px7Dk6gpPsBJ7WoUzl0oGLbXaPODOsWVRfy0NS0zImed7f0eaoOfKdJPKF2%2FQd1oJHqr1mIqJiCp4MFMJ6P87wGOqUBejUbbtXM%2BIQ6XHrPjOcaU8TRpuGD1vVvjjBhECjUgHJOy%2F%2B%2BDBXJMSPBcqlGe4mdekzuSRzvKr76H4Y9NVfHmL0Jshs1sOwZxvk3anpLDHhBQFM7WMda%2F16hFJTGcDKvp%2F2teGV2zHM00va7v3UUNXnGM97xjzT0av8wd838jdFk3L2lxouqvkuDPGkV8tj%2BEXR6L8tLj3565FfP4qhlmgMfggvl&X-Amz-Signature=65b8986f92d174385ba58c6e60312086c65464f93f3e4def048e07422a74b355&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZACMBE5U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG5jfEh8ak6%2BH4tTeWASpuuTkJy%2FdFf7I9dMTQQjMdB3AiEAungqsfdSMJJY1vAf6woSU9%2FjSd1wDsfQu5366nAj020qiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMIMDQNfJh0b2BY6aircA8mYV2%2BKddQWjtlfq8jAK3PbbyjhkBhnvOKuOYQIsNh4nB2JYH3nuKO1oQgo3f1A4mef09fqsTQ9Q9Z4OjEHBujRRzYfJsuw%2BvTb2OgIatknQaPSB5ChhL6bNSKmBnVfmp21zdPAcVqpNH5Fq%2F0ZCZE7w4CG8y927Q1m7uEQQFmFv9KKIcJqKLMUpw8xQMTDbBtY0Rej3UZkKV1wfh%2BRbKtcGOn9Q19FQUv%2BKqkByNN8ixj7zmTNvepUI80Oso4VS%2FTlLnpOV3qYyXeghcXsp4vFxOp5ZlPbwds%2BNpL%2F9EG5QCiITq6Vqhmhm%2BVlP1uDUew1ZehTtUOm5AGP6daU4Id1uuyMEayWwKwaE81N%2BUDTntAvDXb392m2B2Im9ElAA4Ehktp2S6K5JbIF6mBfv%2F0cZWZx6KOC5MXs6ILZzhs8kwuPQleSGJIcIRCPJLuQ13sL5hk2q49ADOWxNLQNRxFyEig7lj3L6mFi06r%2FfJ0dJegIamk7JTVTPP69N6ityEQphqBvo9Z74fgMu8JX%2Fs7EReIfYsN5pCbBlRJ6uI556px7Dk6gpPsBJ7WoUzl0oGLbXaPODOsWVRfy0NS0zImed7f0eaoOfKdJPKF2%2FQd1oJHqr1mIqJiCp4MFMJ6P87wGOqUBejUbbtXM%2BIQ6XHrPjOcaU8TRpuGD1vVvjjBhECjUgHJOy%2F%2B%2BDBXJMSPBcqlGe4mdekzuSRzvKr76H4Y9NVfHmL0Jshs1sOwZxvk3anpLDHhBQFM7WMda%2F16hFJTGcDKvp%2F2teGV2zHM00va7v3UUNXnGM97xjzT0av8wd838jdFk3L2lxouqvkuDPGkV8tj%2BEXR6L8tLj3565FfP4qhlmgMfggvl&X-Amz-Signature=4ba808e53271f96870fedcc6a3522506b6b5c19b606173b218601d19b5916346&X-Amz-SignedHeaders=host&x-id=GetObject)

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
