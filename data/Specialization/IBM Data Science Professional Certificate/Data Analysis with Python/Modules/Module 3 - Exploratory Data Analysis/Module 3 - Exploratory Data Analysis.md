

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XES44WBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwoi%2BGa2UITvb8MnuARTXXeJORlYrWPzJj%2BPtJPtLwigIgRtWslCNUS8lsIjY2xOoPPb%2Bjb6EwWIzCB7vIUq0dGm4qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHLVGJt1GswtNRujryrcA86DVvpFoi%2BQnrUQu3j%2BsGZ4lBEs6qto1BsuOA9BAflsfZaJHG6TIDXIwfhlXRI0ytf4iMefcfwCRcqkWv7Dj70r4oG9v9r576eUdr2hQFY2cQJ1tXfvXaidwfAwPYyKAK5xh%2B%2Bdduht9t9PsJAsHyymsaevWTZjGxYjgqg6VIxdMaISkFujvjdkL%2B6Srfb92%2BCiitcObK%2FzcF23JSoizdDPOpMj1DYIjqTBU3Y%2FQbNdp7pGXBOXUnIXWC9BhELKsJ7HZLYD1CuQt2h2a05nJbDlLf3fFweHKTXzoSky7wXm711Bf0ZR17XAdZDhsZYaABYOErzAh6uB462MrHIFDzFgGs%2B4D1vWjBVWOCDzSHtZKABXrkIDuxsYjmb4OFO85%2FNplIefBrLoIltlADWPT1p6Eno%2FnMotNy1Ya6B%2B52hTgeqLYxVK9ukG1VFzgU9nMPT7b73xCCYQCTRv3EP9vcVprw8JZPsr0kQXtUmtVjiK6Ir6E%2Bw7mTWf3aa%2Fe0i9bhle2Cfvur%2Br3rR8c5D8LRMFJ0U38g3HGeaz0vYvLtIzGxhcBxTlSaosqpcrEk9rcdE4ujjFaXk1U9C8l6q%2BzDRJBqtg5pXr4K5bACeRRYIuJtl8%2Fr7Nl4fsvh3yMO3F6rwGOqUBWdBXCN0uct7NPddJUA1KFvoh2Wxq4raxm33HbsHMUmPvAs2s%2F7eDHMkk17f2QXet5ex8TI4OybjP1eWwfCmFnqwD6Th6Z7Zj5%2BBnylcmCjXzrQXMQJyKhIxUFlj%2Bf9HOgnp1t%2BKCd4fL3QDZCXuxLaGq810lq1arxCxvDLG2SGWZ%2FME90Nq%2Bwd%2Fob9Pkp3zRUlOl2tKXhNmlb7u2LEnI9VggOzxe&X-Amz-Signature=6a312ca9d82eaddd0ccdcff59bbbc5e3715616014eaa777ad887fdda24a762b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XES44WBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwoi%2BGa2UITvb8MnuARTXXeJORlYrWPzJj%2BPtJPtLwigIgRtWslCNUS8lsIjY2xOoPPb%2Bjb6EwWIzCB7vIUq0dGm4qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHLVGJt1GswtNRujryrcA86DVvpFoi%2BQnrUQu3j%2BsGZ4lBEs6qto1BsuOA9BAflsfZaJHG6TIDXIwfhlXRI0ytf4iMefcfwCRcqkWv7Dj70r4oG9v9r576eUdr2hQFY2cQJ1tXfvXaidwfAwPYyKAK5xh%2B%2Bdduht9t9PsJAsHyymsaevWTZjGxYjgqg6VIxdMaISkFujvjdkL%2B6Srfb92%2BCiitcObK%2FzcF23JSoizdDPOpMj1DYIjqTBU3Y%2FQbNdp7pGXBOXUnIXWC9BhELKsJ7HZLYD1CuQt2h2a05nJbDlLf3fFweHKTXzoSky7wXm711Bf0ZR17XAdZDhsZYaABYOErzAh6uB462MrHIFDzFgGs%2B4D1vWjBVWOCDzSHtZKABXrkIDuxsYjmb4OFO85%2FNplIefBrLoIltlADWPT1p6Eno%2FnMotNy1Ya6B%2B52hTgeqLYxVK9ukG1VFzgU9nMPT7b73xCCYQCTRv3EP9vcVprw8JZPsr0kQXtUmtVjiK6Ir6E%2Bw7mTWf3aa%2Fe0i9bhle2Cfvur%2Br3rR8c5D8LRMFJ0U38g3HGeaz0vYvLtIzGxhcBxTlSaosqpcrEk9rcdE4ujjFaXk1U9C8l6q%2BzDRJBqtg5pXr4K5bACeRRYIuJtl8%2Fr7Nl4fsvh3yMO3F6rwGOqUBWdBXCN0uct7NPddJUA1KFvoh2Wxq4raxm33HbsHMUmPvAs2s%2F7eDHMkk17f2QXet5ex8TI4OybjP1eWwfCmFnqwD6Th6Z7Zj5%2BBnylcmCjXzrQXMQJyKhIxUFlj%2Bf9HOgnp1t%2BKCd4fL3QDZCXuxLaGq810lq1arxCxvDLG2SGWZ%2FME90Nq%2Bwd%2Fob9Pkp3zRUlOl2tKXhNmlb7u2LEnI9VggOzxe&X-Amz-Signature=1b9ccf53b7e4c47a7c766557e0e3f81501a945b420be1d76e71b4af762aa1879&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XES44WBS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwoi%2BGa2UITvb8MnuARTXXeJORlYrWPzJj%2BPtJPtLwigIgRtWslCNUS8lsIjY2xOoPPb%2Bjb6EwWIzCB7vIUq0dGm4qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHLVGJt1GswtNRujryrcA86DVvpFoi%2BQnrUQu3j%2BsGZ4lBEs6qto1BsuOA9BAflsfZaJHG6TIDXIwfhlXRI0ytf4iMefcfwCRcqkWv7Dj70r4oG9v9r576eUdr2hQFY2cQJ1tXfvXaidwfAwPYyKAK5xh%2B%2Bdduht9t9PsJAsHyymsaevWTZjGxYjgqg6VIxdMaISkFujvjdkL%2B6Srfb92%2BCiitcObK%2FzcF23JSoizdDPOpMj1DYIjqTBU3Y%2FQbNdp7pGXBOXUnIXWC9BhELKsJ7HZLYD1CuQt2h2a05nJbDlLf3fFweHKTXzoSky7wXm711Bf0ZR17XAdZDhsZYaABYOErzAh6uB462MrHIFDzFgGs%2B4D1vWjBVWOCDzSHtZKABXrkIDuxsYjmb4OFO85%2FNplIefBrLoIltlADWPT1p6Eno%2FnMotNy1Ya6B%2B52hTgeqLYxVK9ukG1VFzgU9nMPT7b73xCCYQCTRv3EP9vcVprw8JZPsr0kQXtUmtVjiK6Ir6E%2Bw7mTWf3aa%2Fe0i9bhle2Cfvur%2Br3rR8c5D8LRMFJ0U38g3HGeaz0vYvLtIzGxhcBxTlSaosqpcrEk9rcdE4ujjFaXk1U9C8l6q%2BzDRJBqtg5pXr4K5bACeRRYIuJtl8%2Fr7Nl4fsvh3yMO3F6rwGOqUBWdBXCN0uct7NPddJUA1KFvoh2Wxq4raxm33HbsHMUmPvAs2s%2F7eDHMkk17f2QXet5ex8TI4OybjP1eWwfCmFnqwD6Th6Z7Zj5%2BBnylcmCjXzrQXMQJyKhIxUFlj%2Bf9HOgnp1t%2BKCd4fL3QDZCXuxLaGq810lq1arxCxvDLG2SGWZ%2FME90Nq%2Bwd%2Fob9Pkp3zRUlOl2tKXhNmlb7u2LEnI9VggOzxe&X-Amz-Signature=f23bca849df0f233b00d5caab42c007dfdeeafca550c2643b888316f33301fde&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU6MRUQN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVgdqC934VjoA2pQ3%2FgQoiy1jomI0jJgFvXKbCT2CcFAiEA%2BJKQ%2BzXQO7DhqOYIpG0mPoPyLtDDPDWdQLmUT3b%2BBoEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IVIb064r2fAGmECrcA809Vzu3i729y2BiWf2e2PU9M6u%2B1pXNzW7iepDIfR%2Blk5ve52Yu6diK1pv3APhAOSrPHbFcETLd3i3FT%2Fa88UbE7lI37Xrj1d2KKCuoCmCWRKp2W7aYetR9e8QnXFDaEbLrcQaOenwu6NmZ3dXDvoI6Y3KoKwSUIomWXVrIyRjb5%2FLOfmVq8yF4wOJaz1G6b3m3IyWcf0iVickrR%2FNjXNz5FAMpslhHu4tchzJFZuB%2B2AlKmIxoXU7b1rdK1H3iOGJsJnH%2F7Ax1nG2yUbZXKDEFF2yxet7bK30t91iDSHf1p9IKIBGEPxDcxO5euwSM0POpUYBjUM7b92g%2FlyLzPXx128Ol9xB5BjrdT7ht%2FG0MRhblYf976lAbB%2FodEoElO1W%2BmfMlQZype%2F%2B10D%2BodQv5Be8uz8K3BHAfnnPiehwt51kOvqyR0qCTqefSFdLqopmm9tYYhVa5ffsb9KeHqjg%2BfQnL%2F8mKGLKAbnxhThXNKtCELpg4nlZ0%2Fn2sZwVruH34P67efN0jijibJ%2BWFnFY1nxXJzcZ%2Bu1gSmi7AsMNP20zOZcsQGFmTp80Eve%2F8lJhol9ozWQC2fm1ELNH3d08iGun0yBI2Uk%2Bt0GhM2yvW959lCQKRzqEwrmavMOnF6rwGOqUB3KiRphlXZTD9OQWbzjpjUBxH%2FNRS%2FCgqrYIjbom0BDEDkpKpNcYZxv%2Bk2QIxHFVa3Tzr4mG71j1c7MPE6p6bSrlUAnerIVQWoigITqjSvGnexG%2B4rOECLREnyrPTUM36U3NK0F2hnoAPzzwW%2BL4rhrYYfaX9v0YseeIukrqnPwtv4ehqHTXyIpTNtIS61iB19LJupBydkHOfqK6ZWERS7UbElGJX&X-Amz-Signature=910999d53e2820dc13acb25578cf4dffb61130155dc1913683940e31874b138e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU6MRUQN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVgdqC934VjoA2pQ3%2FgQoiy1jomI0jJgFvXKbCT2CcFAiEA%2BJKQ%2BzXQO7DhqOYIpG0mPoPyLtDDPDWdQLmUT3b%2BBoEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IVIb064r2fAGmECrcA809Vzu3i729y2BiWf2e2PU9M6u%2B1pXNzW7iepDIfR%2Blk5ve52Yu6diK1pv3APhAOSrPHbFcETLd3i3FT%2Fa88UbE7lI37Xrj1d2KKCuoCmCWRKp2W7aYetR9e8QnXFDaEbLrcQaOenwu6NmZ3dXDvoI6Y3KoKwSUIomWXVrIyRjb5%2FLOfmVq8yF4wOJaz1G6b3m3IyWcf0iVickrR%2FNjXNz5FAMpslhHu4tchzJFZuB%2B2AlKmIxoXU7b1rdK1H3iOGJsJnH%2F7Ax1nG2yUbZXKDEFF2yxet7bK30t91iDSHf1p9IKIBGEPxDcxO5euwSM0POpUYBjUM7b92g%2FlyLzPXx128Ol9xB5BjrdT7ht%2FG0MRhblYf976lAbB%2FodEoElO1W%2BmfMlQZype%2F%2B10D%2BodQv5Be8uz8K3BHAfnnPiehwt51kOvqyR0qCTqefSFdLqopmm9tYYhVa5ffsb9KeHqjg%2BfQnL%2F8mKGLKAbnxhThXNKtCELpg4nlZ0%2Fn2sZwVruH34P67efN0jijibJ%2BWFnFY1nxXJzcZ%2Bu1gSmi7AsMNP20zOZcsQGFmTp80Eve%2F8lJhol9ozWQC2fm1ELNH3d08iGun0yBI2Uk%2Bt0GhM2yvW959lCQKRzqEwrmavMOnF6rwGOqUB3KiRphlXZTD9OQWbzjpjUBxH%2FNRS%2FCgqrYIjbom0BDEDkpKpNcYZxv%2Bk2QIxHFVa3Tzr4mG71j1c7MPE6p6bSrlUAnerIVQWoigITqjSvGnexG%2B4rOECLREnyrPTUM36U3NK0F2hnoAPzzwW%2BL4rhrYYfaX9v0YseeIukrqnPwtv4ehqHTXyIpTNtIS61iB19LJupBydkHOfqK6ZWERS7UbElGJX&X-Amz-Signature=03b282612419d020402856c373a6afaec81078ffaa34962d967575fb99dbb17e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU6MRUQN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVgdqC934VjoA2pQ3%2FgQoiy1jomI0jJgFvXKbCT2CcFAiEA%2BJKQ%2BzXQO7DhqOYIpG0mPoPyLtDDPDWdQLmUT3b%2BBoEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IVIb064r2fAGmECrcA809Vzu3i729y2BiWf2e2PU9M6u%2B1pXNzW7iepDIfR%2Blk5ve52Yu6diK1pv3APhAOSrPHbFcETLd3i3FT%2Fa88UbE7lI37Xrj1d2KKCuoCmCWRKp2W7aYetR9e8QnXFDaEbLrcQaOenwu6NmZ3dXDvoI6Y3KoKwSUIomWXVrIyRjb5%2FLOfmVq8yF4wOJaz1G6b3m3IyWcf0iVickrR%2FNjXNz5FAMpslhHu4tchzJFZuB%2B2AlKmIxoXU7b1rdK1H3iOGJsJnH%2F7Ax1nG2yUbZXKDEFF2yxet7bK30t91iDSHf1p9IKIBGEPxDcxO5euwSM0POpUYBjUM7b92g%2FlyLzPXx128Ol9xB5BjrdT7ht%2FG0MRhblYf976lAbB%2FodEoElO1W%2BmfMlQZype%2F%2B10D%2BodQv5Be8uz8K3BHAfnnPiehwt51kOvqyR0qCTqefSFdLqopmm9tYYhVa5ffsb9KeHqjg%2BfQnL%2F8mKGLKAbnxhThXNKtCELpg4nlZ0%2Fn2sZwVruH34P67efN0jijibJ%2BWFnFY1nxXJzcZ%2Bu1gSmi7AsMNP20zOZcsQGFmTp80Eve%2F8lJhol9ozWQC2fm1ELNH3d08iGun0yBI2Uk%2Bt0GhM2yvW959lCQKRzqEwrmavMOnF6rwGOqUB3KiRphlXZTD9OQWbzjpjUBxH%2FNRS%2FCgqrYIjbom0BDEDkpKpNcYZxv%2Bk2QIxHFVa3Tzr4mG71j1c7MPE6p6bSrlUAnerIVQWoigITqjSvGnexG%2B4rOECLREnyrPTUM36U3NK0F2hnoAPzzwW%2BL4rhrYYfaX9v0YseeIukrqnPwtv4ehqHTXyIpTNtIS61iB19LJupBydkHOfqK6ZWERS7UbElGJX&X-Amz-Signature=d026ec9c0de06058856f5f382e75525853d9dc7832787a02310c609c488106f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU6MRUQN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVgdqC934VjoA2pQ3%2FgQoiy1jomI0jJgFvXKbCT2CcFAiEA%2BJKQ%2BzXQO7DhqOYIpG0mPoPyLtDDPDWdQLmUT3b%2BBoEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IVIb064r2fAGmECrcA809Vzu3i729y2BiWf2e2PU9M6u%2B1pXNzW7iepDIfR%2Blk5ve52Yu6diK1pv3APhAOSrPHbFcETLd3i3FT%2Fa88UbE7lI37Xrj1d2KKCuoCmCWRKp2W7aYetR9e8QnXFDaEbLrcQaOenwu6NmZ3dXDvoI6Y3KoKwSUIomWXVrIyRjb5%2FLOfmVq8yF4wOJaz1G6b3m3IyWcf0iVickrR%2FNjXNz5FAMpslhHu4tchzJFZuB%2B2AlKmIxoXU7b1rdK1H3iOGJsJnH%2F7Ax1nG2yUbZXKDEFF2yxet7bK30t91iDSHf1p9IKIBGEPxDcxO5euwSM0POpUYBjUM7b92g%2FlyLzPXx128Ol9xB5BjrdT7ht%2FG0MRhblYf976lAbB%2FodEoElO1W%2BmfMlQZype%2F%2B10D%2BodQv5Be8uz8K3BHAfnnPiehwt51kOvqyR0qCTqefSFdLqopmm9tYYhVa5ffsb9KeHqjg%2BfQnL%2F8mKGLKAbnxhThXNKtCELpg4nlZ0%2Fn2sZwVruH34P67efN0jijibJ%2BWFnFY1nxXJzcZ%2Bu1gSmi7AsMNP20zOZcsQGFmTp80Eve%2F8lJhol9ozWQC2fm1ELNH3d08iGun0yBI2Uk%2Bt0GhM2yvW959lCQKRzqEwrmavMOnF6rwGOqUB3KiRphlXZTD9OQWbzjpjUBxH%2FNRS%2FCgqrYIjbom0BDEDkpKpNcYZxv%2Bk2QIxHFVa3Tzr4mG71j1c7MPE6p6bSrlUAnerIVQWoigITqjSvGnexG%2B4rOECLREnyrPTUM36U3NK0F2hnoAPzzwW%2BL4rhrYYfaX9v0YseeIukrqnPwtv4ehqHTXyIpTNtIS61iB19LJupBydkHOfqK6ZWERS7UbElGJX&X-Amz-Signature=6f219b11336c0a7f3b4f3dbfe8bb3fe76004eb7d792a6d1018170ba5d3dc1dba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU6MRUQN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVgdqC934VjoA2pQ3%2FgQoiy1jomI0jJgFvXKbCT2CcFAiEA%2BJKQ%2BzXQO7DhqOYIpG0mPoPyLtDDPDWdQLmUT3b%2BBoEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IVIb064r2fAGmECrcA809Vzu3i729y2BiWf2e2PU9M6u%2B1pXNzW7iepDIfR%2Blk5ve52Yu6diK1pv3APhAOSrPHbFcETLd3i3FT%2Fa88UbE7lI37Xrj1d2KKCuoCmCWRKp2W7aYetR9e8QnXFDaEbLrcQaOenwu6NmZ3dXDvoI6Y3KoKwSUIomWXVrIyRjb5%2FLOfmVq8yF4wOJaz1G6b3m3IyWcf0iVickrR%2FNjXNz5FAMpslhHu4tchzJFZuB%2B2AlKmIxoXU7b1rdK1H3iOGJsJnH%2F7Ax1nG2yUbZXKDEFF2yxet7bK30t91iDSHf1p9IKIBGEPxDcxO5euwSM0POpUYBjUM7b92g%2FlyLzPXx128Ol9xB5BjrdT7ht%2FG0MRhblYf976lAbB%2FodEoElO1W%2BmfMlQZype%2F%2B10D%2BodQv5Be8uz8K3BHAfnnPiehwt51kOvqyR0qCTqefSFdLqopmm9tYYhVa5ffsb9KeHqjg%2BfQnL%2F8mKGLKAbnxhThXNKtCELpg4nlZ0%2Fn2sZwVruH34P67efN0jijibJ%2BWFnFY1nxXJzcZ%2Bu1gSmi7AsMNP20zOZcsQGFmTp80Eve%2F8lJhol9ozWQC2fm1ELNH3d08iGun0yBI2Uk%2Bt0GhM2yvW959lCQKRzqEwrmavMOnF6rwGOqUB3KiRphlXZTD9OQWbzjpjUBxH%2FNRS%2FCgqrYIjbom0BDEDkpKpNcYZxv%2Bk2QIxHFVa3Tzr4mG71j1c7MPE6p6bSrlUAnerIVQWoigITqjSvGnexG%2B4rOECLREnyrPTUM36U3NK0F2hnoAPzzwW%2BL4rhrYYfaX9v0YseeIukrqnPwtv4ehqHTXyIpTNtIS61iB19LJupBydkHOfqK6ZWERS7UbElGJX&X-Amz-Signature=c6e41928be3a0e98eab36d4dfdb30b1b3d7adb01ee74d5a3e04577844d69e4e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU6MRUQN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVgdqC934VjoA2pQ3%2FgQoiy1jomI0jJgFvXKbCT2CcFAiEA%2BJKQ%2BzXQO7DhqOYIpG0mPoPyLtDDPDWdQLmUT3b%2BBoEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IVIb064r2fAGmECrcA809Vzu3i729y2BiWf2e2PU9M6u%2B1pXNzW7iepDIfR%2Blk5ve52Yu6diK1pv3APhAOSrPHbFcETLd3i3FT%2Fa88UbE7lI37Xrj1d2KKCuoCmCWRKp2W7aYetR9e8QnXFDaEbLrcQaOenwu6NmZ3dXDvoI6Y3KoKwSUIomWXVrIyRjb5%2FLOfmVq8yF4wOJaz1G6b3m3IyWcf0iVickrR%2FNjXNz5FAMpslhHu4tchzJFZuB%2B2AlKmIxoXU7b1rdK1H3iOGJsJnH%2F7Ax1nG2yUbZXKDEFF2yxet7bK30t91iDSHf1p9IKIBGEPxDcxO5euwSM0POpUYBjUM7b92g%2FlyLzPXx128Ol9xB5BjrdT7ht%2FG0MRhblYf976lAbB%2FodEoElO1W%2BmfMlQZype%2F%2B10D%2BodQv5Be8uz8K3BHAfnnPiehwt51kOvqyR0qCTqefSFdLqopmm9tYYhVa5ffsb9KeHqjg%2BfQnL%2F8mKGLKAbnxhThXNKtCELpg4nlZ0%2Fn2sZwVruH34P67efN0jijibJ%2BWFnFY1nxXJzcZ%2Bu1gSmi7AsMNP20zOZcsQGFmTp80Eve%2F8lJhol9ozWQC2fm1ELNH3d08iGun0yBI2Uk%2Bt0GhM2yvW959lCQKRzqEwrmavMOnF6rwGOqUB3KiRphlXZTD9OQWbzjpjUBxH%2FNRS%2FCgqrYIjbom0BDEDkpKpNcYZxv%2Bk2QIxHFVa3Tzr4mG71j1c7MPE6p6bSrlUAnerIVQWoigITqjSvGnexG%2B4rOECLREnyrPTUM36U3NK0F2hnoAPzzwW%2BL4rhrYYfaX9v0YseeIukrqnPwtv4ehqHTXyIpTNtIS61iB19LJupBydkHOfqK6ZWERS7UbElGJX&X-Amz-Signature=51bb8cac8f048f9a2ad05d18dc54ae8b5a17ae248fc14c7da195bd0f055b7b5b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VDEFVL3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICYsU2zb5%2B8Se5QWwmPWg9LbCPc3ZGb4bHQLuJG5WowYAiA8xjR7gddi%2FtoqDK%2BzTB1aZWq0PSpWyKmsfUyAT7iq1SqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMErpr3dxWP4eGQvvgKtwDuhPeZULGmm%2BnLKQ9KDHPLN4SYsBmN21RZkS2Sa0bhtj2LFrcA%2B4GoZjRlVMAVuXTEkA3y3BxlXt07pXD4pncJLAAY1d7NAnWtQ2MTdEwPSaGj1n1FqSazIovEneItsfQctUwDJ4zcwf%2F%2FT9gzA5LXfszG6nFzjp4NY3DYsw%2FDNv88vhhFDuQAe2z9gjHQqZZm0F6Vo8NAadcxkxlPvVtemz3cktRtFeCvdvYkTVzCnv6AEQ5NP4ZubpcBWz1tWWHCSqBWH6BHdEiHUESrEsUh8QhUkQSx28wU5Qmkdcp3JNPQ8xsK48BH4jdyluuydVMdwd%2FNOVNeC7cG999NuU8jndntWUw8VIQn2%2BtRpvy2dflY674Ule3VOaCdMp6REeBxZZmfC8YPoKR17TtP0IKwOGvEhLNmmcS9WbfxFOTiDT5kvZQUV73ZdUdU94cBTWOIJ63lVzugLVfmOSGBkWYXKB0Oixcw%2B24uXmU%2FYgCLVfKroNFVhGS72LzJnPR4ZjNy5Q%2FbPNCRLLyrnah42kKyBE77XsPfWXYonfuC3ZjiuuzMH1a879Kpd3LNZQXrFatQ4JJvMcTT%2FqQWsjCG6wSodkvzme%2FxlN0Cg6Awod9oKAS6r2VRZd9HGNBwycww8XqvAY6pgH4YxhDI%2BG0%2BncecD6xGl%2FBrJfi2HIurzFXCkAVHZNu%2FP5nH6%2Fd0L%2FBvOQ4H6%2FS2C6MVMuZ7z8p4tHAteV4xEdqQgb2Ik7bWXbMorZyRVoF3A%2BJDuQdtN4xS12oMwN%2BFU9BOii3ofWNe2jnLdHnCsWeCDCswGMXJNx6QFjXwhDzoNDyWM1tCgfRxu3ndED2kZnvFBqX0u08HN%2BUbkbkp9qQjOFcE675&X-Amz-Signature=ebbb8d29a0ab7334d28a8224d05ea9e509e9c4d1a7ec044cf93e26df2fb06a0b&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RADG2GFQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD68qlf23tqS766Nf8Cpzv8d%2FAh9t03iKHtCntyEfyfaQIhAK8ipuJHFQidFVBHRNIj3jZigPaaRnq7xt6zhqKcqKDqKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6VY2NWtVVC7zUDNQq3AN5%2BUNfBwkzr6LJpGrxkifhHsouFYuQzHEH5YRCXWOly1zW%2BCbh8rY3fwFweypQ%2FbpXedN%2BwqSvqAwhaTLlCNi9lmLvGUCbf8n7vjFyia31W6wTpYCLEKwmAH9u2xW1vDelKORYDMOib3UWrBU0K%2BPYnZn4TAYjcoobJ0KW3%2F2C3743B%2F%2FuE%2FBq5jYMXlEOgec0yxLUKIlMH%2FOqvdfqMcITS3WENG%2FxHuMVVRYKqqwoJ0n9yaxd2i7vQRVY3b%2F7wNQJJFjdbIHze%2Fa0P6B9XkJds22o92%2Fc41oysqisOxLc%2FvoFsJ5lDtBfwlTET7DDZjjcBs0aXyjl%2FJObcPVzkM7OZSAsHwx3WA3RaQqxnLxbupKbSWiwjXeyron9hlMyP6RTK9DoaLsor8YQMgoqQilNQZ6GqrCCcbsu0cAN%2Ff7zyE3xKBb8oeQU%2FfhxMgaL%2BEEVHfE54OxnOQS8XHNQ81B7L2sdfLnVJh1fDNYxO7JuaiKKrXkCduKmreFOeOPyfnJMoupjZHCHYhntl3CAr3vBUqq6UnmUjhXPlfK8%2BLdd6DKdZVpp5vyCprjYaGS68E%2BA1bNVec1Z4G8FxMehQUGhxR4WxmZ7NokTaPD447Zxga%2FA2za8nCe3w7zlqTDDxeq8BjqkAZhOjFNyLUmcP8LGFQu214%2FCPr5beOtX6efw1orkxVIBw%2BS3%2B0nPMPYnag4fceo23w7wcKgYRliwaknTI4Fodlp8XfTZ0awAOM0LqyBb%2BzEpo06GnCqdeFg5b3PhluwxPXTzW1DRnGcP4Adnj5JcCdfzaiBzGfti30ep4Q8yGUY1KvXeXIFBPxE3CoVZkFHYzdfk4fHOrv%2BRmUDu%2FaPyO6IogKFK&X-Amz-Signature=eabd01c98c80f099bf5301263093e08a2545b522ecd86f4f2cf1bcdee2317c55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU6MRUQN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVgdqC934VjoA2pQ3%2FgQoiy1jomI0jJgFvXKbCT2CcFAiEA%2BJKQ%2BzXQO7DhqOYIpG0mPoPyLtDDPDWdQLmUT3b%2BBoEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IVIb064r2fAGmECrcA809Vzu3i729y2BiWf2e2PU9M6u%2B1pXNzW7iepDIfR%2Blk5ve52Yu6diK1pv3APhAOSrPHbFcETLd3i3FT%2Fa88UbE7lI37Xrj1d2KKCuoCmCWRKp2W7aYetR9e8QnXFDaEbLrcQaOenwu6NmZ3dXDvoI6Y3KoKwSUIomWXVrIyRjb5%2FLOfmVq8yF4wOJaz1G6b3m3IyWcf0iVickrR%2FNjXNz5FAMpslhHu4tchzJFZuB%2B2AlKmIxoXU7b1rdK1H3iOGJsJnH%2F7Ax1nG2yUbZXKDEFF2yxet7bK30t91iDSHf1p9IKIBGEPxDcxO5euwSM0POpUYBjUM7b92g%2FlyLzPXx128Ol9xB5BjrdT7ht%2FG0MRhblYf976lAbB%2FodEoElO1W%2BmfMlQZype%2F%2B10D%2BodQv5Be8uz8K3BHAfnnPiehwt51kOvqyR0qCTqefSFdLqopmm9tYYhVa5ffsb9KeHqjg%2BfQnL%2F8mKGLKAbnxhThXNKtCELpg4nlZ0%2Fn2sZwVruH34P67efN0jijibJ%2BWFnFY1nxXJzcZ%2Bu1gSmi7AsMNP20zOZcsQGFmTp80Eve%2F8lJhol9ozWQC2fm1ELNH3d08iGun0yBI2Uk%2Bt0GhM2yvW959lCQKRzqEwrmavMOnF6rwGOqUB3KiRphlXZTD9OQWbzjpjUBxH%2FNRS%2FCgqrYIjbom0BDEDkpKpNcYZxv%2Bk2QIxHFVa3Tzr4mG71j1c7MPE6p6bSrlUAnerIVQWoigITqjSvGnexG%2B4rOECLREnyrPTUM36U3NK0F2hnoAPzzwW%2BL4rhrYYfaX9v0YseeIukrqnPwtv4ehqHTXyIpTNtIS61iB19LJupBydkHOfqK6ZWERS7UbElGJX&X-Amz-Signature=cb1096fb315ed6224fe76215fbf6152ebbdd445e07b7db55d5f3c3e045280b19&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU6MRUQN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVgdqC934VjoA2pQ3%2FgQoiy1jomI0jJgFvXKbCT2CcFAiEA%2BJKQ%2BzXQO7DhqOYIpG0mPoPyLtDDPDWdQLmUT3b%2BBoEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IVIb064r2fAGmECrcA809Vzu3i729y2BiWf2e2PU9M6u%2B1pXNzW7iepDIfR%2Blk5ve52Yu6diK1pv3APhAOSrPHbFcETLd3i3FT%2Fa88UbE7lI37Xrj1d2KKCuoCmCWRKp2W7aYetR9e8QnXFDaEbLrcQaOenwu6NmZ3dXDvoI6Y3KoKwSUIomWXVrIyRjb5%2FLOfmVq8yF4wOJaz1G6b3m3IyWcf0iVickrR%2FNjXNz5FAMpslhHu4tchzJFZuB%2B2AlKmIxoXU7b1rdK1H3iOGJsJnH%2F7Ax1nG2yUbZXKDEFF2yxet7bK30t91iDSHf1p9IKIBGEPxDcxO5euwSM0POpUYBjUM7b92g%2FlyLzPXx128Ol9xB5BjrdT7ht%2FG0MRhblYf976lAbB%2FodEoElO1W%2BmfMlQZype%2F%2B10D%2BodQv5Be8uz8K3BHAfnnPiehwt51kOvqyR0qCTqefSFdLqopmm9tYYhVa5ffsb9KeHqjg%2BfQnL%2F8mKGLKAbnxhThXNKtCELpg4nlZ0%2Fn2sZwVruH34P67efN0jijibJ%2BWFnFY1nxXJzcZ%2Bu1gSmi7AsMNP20zOZcsQGFmTp80Eve%2F8lJhol9ozWQC2fm1ELNH3d08iGun0yBI2Uk%2Bt0GhM2yvW959lCQKRzqEwrmavMOnF6rwGOqUB3KiRphlXZTD9OQWbzjpjUBxH%2FNRS%2FCgqrYIjbom0BDEDkpKpNcYZxv%2Bk2QIxHFVa3Tzr4mG71j1c7MPE6p6bSrlUAnerIVQWoigITqjSvGnexG%2B4rOECLREnyrPTUM36U3NK0F2hnoAPzzwW%2BL4rhrYYfaX9v0YseeIukrqnPwtv4ehqHTXyIpTNtIS61iB19LJupBydkHOfqK6ZWERS7UbElGJX&X-Amz-Signature=b2026e7b7d54f1a2728b62f9b210994ca09932066c83cc44bbcd875012ee5d5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU6MRUQN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVgdqC934VjoA2pQ3%2FgQoiy1jomI0jJgFvXKbCT2CcFAiEA%2BJKQ%2BzXQO7DhqOYIpG0mPoPyLtDDPDWdQLmUT3b%2BBoEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IVIb064r2fAGmECrcA809Vzu3i729y2BiWf2e2PU9M6u%2B1pXNzW7iepDIfR%2Blk5ve52Yu6diK1pv3APhAOSrPHbFcETLd3i3FT%2Fa88UbE7lI37Xrj1d2KKCuoCmCWRKp2W7aYetR9e8QnXFDaEbLrcQaOenwu6NmZ3dXDvoI6Y3KoKwSUIomWXVrIyRjb5%2FLOfmVq8yF4wOJaz1G6b3m3IyWcf0iVickrR%2FNjXNz5FAMpslhHu4tchzJFZuB%2B2AlKmIxoXU7b1rdK1H3iOGJsJnH%2F7Ax1nG2yUbZXKDEFF2yxet7bK30t91iDSHf1p9IKIBGEPxDcxO5euwSM0POpUYBjUM7b92g%2FlyLzPXx128Ol9xB5BjrdT7ht%2FG0MRhblYf976lAbB%2FodEoElO1W%2BmfMlQZype%2F%2B10D%2BodQv5Be8uz8K3BHAfnnPiehwt51kOvqyR0qCTqefSFdLqopmm9tYYhVa5ffsb9KeHqjg%2BfQnL%2F8mKGLKAbnxhThXNKtCELpg4nlZ0%2Fn2sZwVruH34P67efN0jijibJ%2BWFnFY1nxXJzcZ%2Bu1gSmi7AsMNP20zOZcsQGFmTp80Eve%2F8lJhol9ozWQC2fm1ELNH3d08iGun0yBI2Uk%2Bt0GhM2yvW959lCQKRzqEwrmavMOnF6rwGOqUB3KiRphlXZTD9OQWbzjpjUBxH%2FNRS%2FCgqrYIjbom0BDEDkpKpNcYZxv%2Bk2QIxHFVa3Tzr4mG71j1c7MPE6p6bSrlUAnerIVQWoigITqjSvGnexG%2B4rOECLREnyrPTUM36U3NK0F2hnoAPzzwW%2BL4rhrYYfaX9v0YseeIukrqnPwtv4ehqHTXyIpTNtIS61iB19LJupBydkHOfqK6ZWERS7UbElGJX&X-Amz-Signature=c9a64f688695b525b4856b6cadbb3349dc0697efa02dfee6efc82d5fb3ed6cea&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3PAA2KL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDptItOX0WFn9fQRh3m7WCJf1aphU6Zh4%2B%2BpwvI70m1qgIhANAjE2r8GIiM5QTFgqKdY1nm59WzRTTmqXBzhggeA7k2KogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwX7C5Q%2FpplVWj%2Bh0sq3APckOlQassKX8ST3qlCM9mDrZKI1KtOo4eZncm%2B38oqTji1zbqHeYAU31WSzPtEls8Yu%2BclIrEtF2IIOb1RWHequKOLBG7a99V9us5OEHY6EPGgJ6MIgvpXvw9Y9PAVpBB11b0ldlIHJmQaKq%2FED1kxCdxyB7idgnqpqmbd8wCycbqJp5vCvPu3oBrg8vm4eyu94snan0Wwlhn3x4NNarJ2uG7H0kQq1s18hqL%2BtQGlY8L8nwZqMV%2FZcG5OD2%2FkD3iooih%2BGv7GLPv7d4gHOl%2FK%2BGs6dZyKFad8aF847FMbn%2BD93JoNmL19EJDSZQRZ3bVplZT%2F7DEcWvqqJikA2CnQNdBsGUASBBd7MSuKUPmYKSsGaeLrV1Od1ZeYzVIToWUOgYDUSwX3ht3yut%2ByBch3s0CALIjcXm8Bpf5J5yujSjNjhdqFo8ATFMSoK4XC2nJ5BXLj6A2qISe05We0eGHS%2F%2FUA1HpCOWGczOwJ7ozejfRFzhEO%2B%2FlReBEzIkpA12dpI%2Bf5vVlxctne5EzFD7Zc%2BM8F%2Fj3qNxZ7EQLgel89oun7TtPR10Sb2NM%2BYxDsyIn%2F92TPMzfM7fMFsiG%2FOCibCgp3x4GQxIm8J8%2Be9rm5R%2FsKwK4BAHJJP9fgCTDVxeq8BjqkAdBMznwFu%2B6dx5dQH04wTiJeyZBBfJuOILELDOrGXh%2BFZQUt60rk6SnBUm3MTo14p93l66IMNyxQcAkduBg0dMVGfn7i08tA%2FcLQYhpByqDkkb4HaqLm2324VH3dFiuyQNmZr6yI5G3QpJpHZMtwkPIHtCY8uFagxI0pbbLCVE9Bg61IDoWOLhQxlLIGb8bnafmxLhcw6VxhaT0yCYINKy3GHkc5&X-Amz-Signature=fd194b0d7f33caa0405b15695ee754e6b015a3341aca8f557d1415b486609718&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQOHEYEE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGoDL5eC0RmUAj26m1GSgA615J82hbCW5vFy980QMbaMAiEAnXJW5ME0j61R3BuWLAT2bqchb8TePQwcpvW32OfBfVkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAAh6cx%2BgUQLFxqTMircA30kr7wcrvHisRpCZjbGvr9yoKB%2Fi0s4CLentw%2BpnLZlcKfc5HM%2FsP1O%2F3xNHlOXUYiXzZGyIkpbxLUSA2FeTtF3yYVIsKu0S0YcmdntB7%2BD2RYFJghEFTulqwXDRnwa5RD5rIOiiu9%2FI4r6Vy56Vthexq%2BJablQKDzecvMgWYAvXU8oWov7T0TV5PXH5uIgkMxIpPzkImjakHbexC8JqBUBGXKFWqpadC9QjJItr0HsS4XgCTlxR9ocaakaAHs7MQmMYSeqUXY94nYQNqCnjXdUGmdnRAR1OcrmPRiYX3k9gbXrEQI9P8DdH0jVcTY1T9GJIE%2BEyIfzZ6P07GCVXd26zLqhbk92wdzAxcJMP4CedfTPML49MbgZ6PfCWGcLbYeCYJmbOu2M2pl7h7eIa2JSf3z8fWYMD61a59V7fmeklvGWzORDWqPIW4Wk1m73xApeWObd5ub2BUZM%2B%2BVAnrGqt1X1roWyuyPLZ4oHWwvrmgKasnPa6LbU6ILGScn23%2Bd69ZG3xdYtQAHWvXEycYgkqyWnBeKoUkcQoh0DVg%2FVlvdoPCxggI3DJvKR39n1k2YMU9KGgHdr4Dcylb2RG9kEfJqwUfDkSERweYpplQaK5SL3A2qnaOdAoQDWMN7F6rwGOqUBj36%2BOtMjQIJv%2FI%2BJRAIKBCZwzvUvkBniN%2B0HSQExj3F3IHFCXHDwyonZCxK%2B4S1thdfOxYeOf0lT7Nh%2B3xIHO9NXWaH%2Fp1vC9UkzQE8ufUQCJ%2FdGvbgeQh%2FMf3LkeMH40ymp2otKMkOHJnGP%2B57%2By8Afy6%2Bc6PcDQV9nazebhdvUDlIAy115DU5oLxDtDx8UB6YWY5%2BipomEmCwpgLXwWeIlVv2J&X-Amz-Signature=5870b32df919fe3b0ee4f37d98f2b2681c39575dafbd96953f7badc75156cf59&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCDYPXT3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTZaf0FCMpb%2FF5QstLHVdFQH5T7%2Bu6Mn%2B9c78T4Rar9AIhAPupAmCGI%2Bqo0UWVN%2FRQERQCkPdU78ebK6eZEznm%2BD6sKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwyhMdD2ToQojqWO8wq3AMCZ8ZiIb9wBFNNyCQVrNhPTWm7IPS4M8f2%2BIYLmxh%2B8DEkKGlkTP36WgBTtTBvQl0DAkDnfhVbiWGyarFW1xZ7%2B4GtkLinv3Q0DOMS7Iklx4gL0WDLwzmZQQ8xyrqYT2NQC%2F%2FSo1CD%2Bslio%2B9j4cgpzPFoAzfWhkJRvc%2BWpJd4w%2BGl50jSoIOvm9si6kHC%2FK7vk25QdsKQ9DINti5T1BSFL%2FObOh5JbkkNBQ%2FJHQlKHZht5cWL8c%2FCWGC56Za2HGLr8DEhxk27mxdVTmsqRvx7CKU2e77bUKffVcitfGjJgufJBycnes2W0BhsNGNlVDJeWs2nuObJPGxNPBGJOSPVRIb%2BEaU7VTO3QRCafZR6FoJB737ofImQzGqynYBsNE60fRTq7y2j1WbTKDXu%2ByJ%2BLsYiZF5RT6NIVGAanoxQacWY688DJ3otGuS7Km4HLy8X446PkX7jV47efIRfMo7dlG6ain6op6164YH6V0%2Btq53nUTwlCMSHra79YDO0oIP3KoXXBwKXUXGL%2BVyIEizjsIC3TU4N5ZA25v5%2Fcas5efzr0B9u02uxOOIXs7xgeER9LXFpfB0Cl%2FGqp0SsESssu3BuL%2FL%2BAZh%2Bno0N3YaFCcNdcfLJi8XkHkz%2FnjC%2Bxeq8BjqkAcedxkpbPU36yWleLJR1OeGtp74pIH7GK2DJGhR3csbK9eQ7dXEsfbKkWEpkhCpUqhK3Lr5tAKtRaTbAIa0BcZwekRkkLdML3hn0MoDuSICZLppIKuEGfp%2FRiggc9FFHEFXBvwy6kKwjOCmBIPkUXJ68D6z8AsVS1212ZpuvHGpBbGsQU9rRteApQV%2FOb3bPAole8zHFj%2FE%2BVEeOZG4FMbFBYWxt&X-Amz-Signature=e38dfe6b07599f799aa30f7c0d2497044b38b67c0e604944cb518fc195f77f1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7GCPC27%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9ks%2FyBlS4lkVvisQLRrBh0z%2FQgxMZb4Wib6%2Bhpn2m3gIhAPUDgh%2FrTyBR6c9vrARbCtJLIma8ZWPX%2BbDx617Y1%2BljKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybMAmx5EurX5geDSQq3AOZeaODJMQtxc7FYH3EwBoch8hMQdRZQ%2BH6fJtLE8Bm5mxs0olPI5NdgnWMLGCgDAxHvXeAu0%2BjRRUbbNKkGObmQUPAMprPv9fcJ17HQplMsUDs0bHLlNuxKkYH7Kv1u2OKlcWuWXBueMdMmv3YezrR%2BYRWuiKj64lO4sAgVmTAEK8rrWWBx41sGSk1yZyOs6ImC86%2FNA1QHQqcs4FRDjbc65jmoyR65iFZEJlNFLnNQsaI82hGZzVuMPei%2Bg1tc2OkxjG4801Gawcw0Bs8xD5SuztJtoZw0iewP%2FnGCY9UAj%2FOQqyHMbampr7Pmq1KRtaUItWz3E6bIUfwcjLBKy6LtcSSNDbBo2SQEODjo58RqcyiJYVG6Je0cg5HbXbdLd9EHDkGbuyqPMXzUf%2BZkYN6hWG9nnJFspSFFTihu1JfJuMi3ZCXMYiWgvHAFrF1FcT9rg6WDOcYc%2FWvhwao4KFOUSSkAAhqgnE1NuDf6ss7tr8zKWtYz8nOUNyUhjEeWcLcho9pAiDavxH%2F9lTFQkLaQfQcmRg%2FzbakNECXcWXFIZoToeiLyeGJTBesWqEXQcSUoNy1MuGNunbs1FhXODd2DHnwD8sDQ3Fq2KnU0eJ87CdIRdUg9QJw%2B7ZQCDDNxuq8BjqkAUOK8UJk6LWcNxfB6uj7NiDKhLSHsvxLsgpgdLVsidULafBfphEFouhwEmzhcU1G4Ij3uJkvfhE96JNZw0J67HCOA4Vd8l7OteYQ8PRACQvZjbCnmwho5HyDYuOo5benBgpD0%2Ffztay6vuBQjlwkKkb4eEmHf0eYS2ZqS%2BGR%2FAF0QZ6bMT4KrSWs0NHs3oax39EluhASGXL2C%2FfJ1J4G4zoc3ATH&X-Amz-Signature=8b715e36b3e51e49cab99c49beb13e7e7894c65cb1b39255d281969475e8d260&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7GCPC27%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9ks%2FyBlS4lkVvisQLRrBh0z%2FQgxMZb4Wib6%2Bhpn2m3gIhAPUDgh%2FrTyBR6c9vrARbCtJLIma8ZWPX%2BbDx617Y1%2BljKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybMAmx5EurX5geDSQq3AOZeaODJMQtxc7FYH3EwBoch8hMQdRZQ%2BH6fJtLE8Bm5mxs0olPI5NdgnWMLGCgDAxHvXeAu0%2BjRRUbbNKkGObmQUPAMprPv9fcJ17HQplMsUDs0bHLlNuxKkYH7Kv1u2OKlcWuWXBueMdMmv3YezrR%2BYRWuiKj64lO4sAgVmTAEK8rrWWBx41sGSk1yZyOs6ImC86%2FNA1QHQqcs4FRDjbc65jmoyR65iFZEJlNFLnNQsaI82hGZzVuMPei%2Bg1tc2OkxjG4801Gawcw0Bs8xD5SuztJtoZw0iewP%2FnGCY9UAj%2FOQqyHMbampr7Pmq1KRtaUItWz3E6bIUfwcjLBKy6LtcSSNDbBo2SQEODjo58RqcyiJYVG6Je0cg5HbXbdLd9EHDkGbuyqPMXzUf%2BZkYN6hWG9nnJFspSFFTihu1JfJuMi3ZCXMYiWgvHAFrF1FcT9rg6WDOcYc%2FWvhwao4KFOUSSkAAhqgnE1NuDf6ss7tr8zKWtYz8nOUNyUhjEeWcLcho9pAiDavxH%2F9lTFQkLaQfQcmRg%2FzbakNECXcWXFIZoToeiLyeGJTBesWqEXQcSUoNy1MuGNunbs1FhXODd2DHnwD8sDQ3Fq2KnU0eJ87CdIRdUg9QJw%2B7ZQCDDNxuq8BjqkAUOK8UJk6LWcNxfB6uj7NiDKhLSHsvxLsgpgdLVsidULafBfphEFouhwEmzhcU1G4Ij3uJkvfhE96JNZw0J67HCOA4Vd8l7OteYQ8PRACQvZjbCnmwho5HyDYuOo5benBgpD0%2Ffztay6vuBQjlwkKkb4eEmHf0eYS2ZqS%2BGR%2FAF0QZ6bMT4KrSWs0NHs3oax39EluhASGXL2C%2FfJ1J4G4zoc3ATH&X-Amz-Signature=76ef30746b40e030f17c716acfbc31d4f05ee396c0ea374f3ee4f024afc9127a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
