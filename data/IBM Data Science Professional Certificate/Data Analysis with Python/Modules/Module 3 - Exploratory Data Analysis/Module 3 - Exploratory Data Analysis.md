

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2C4M7HT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBqLXO3WNIlw7O7NvlQsryuDilgUtTwLxAggGYlZuhVAIhAMBMofmVCChLyowUC1awXVsOZS1MjcBn6B5%2B%2BVAkujGHKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXWMyv8xZWWuV3waEq3AM2eUXhET5b1DEnSQPp68J5F56JsLGDuOPJYRxQToKSf46B7SgiLwchc3ZFyE7d9YPSoIORNw2EQ0vcfj5nq4QWRFdPH5oOmpfTfzjqiv0LuUx69unvHZownlGKcLkBIc1GQtDjrOi0K87LwiNjZin1LgPw4nvKHSTBRfeecQByoGrk0gv67EbseGFZpY5m0qiMDhfilc1iY5f%2BBU%2FOr1Ot87exgl3u%2BOZeNWOpRYl%2Fl2XcALRSFUi49IcFGr3hgLlJ%2BPLrQ76XgBU3nYfmtnD8Z1c7y1lYfjzu0vbhIv%2BBNeeo9uCPu4LyPgiCfksiHOGxTGiK6UHmWx9aydFFeZVtRlgfnYbWuBNlJTQaKxmbt3vOY%2BrpcofupVvdSdn4B2H9SLueXe2s%2BMim%2BHaaLE9WiKRWHLiU%2FOhJ0sArG8rRB%2FgO%2FFfAIybtTm9oq6gh3S2cqhEI%2BfMH5oENSHOwerlbyn35vUiXDLFCULIb%2B3P0I%2Fo7fDfhbcegKBSV1uuQzTExepW4D%2FjFq4ytQK%2BKA5Q6Uw15XxXGNqTYPs6B87y1zMroiQ4gkBnGISLGrL57MIecTK3QdCNRYpSqUhuYRIx1s%2BZgWnDZslisd8ENtu4WshZ%2BTfQm6kelJxN3djDQ3f68BjqkAVQDLcQqp97krQyn1VPHCN%2F0Sm6A6jdec5Gh24sxw9xqxlo3nzxJA2%2BFpGtZDtLUs%2BSy6n6oJIdv0VY8OSJSEAEoP4qZ49DgG%2BysLLweX3W2EpUESfbjVtmDBpbScpRT8dJD5bBDXDVpZXPt7UlPL9OpEPShgg0XXiZx8uIJmAveIVv8NCKfRIVKpd8opRaPChxw2P%2BCTjQKAJzlA9DEkHxAGVJy&X-Amz-Signature=81bc97ba3502010bc153fc9ac65d03b98d8504f6898754ccc8d39c338cb9c169&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2C4M7HT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBqLXO3WNIlw7O7NvlQsryuDilgUtTwLxAggGYlZuhVAIhAMBMofmVCChLyowUC1awXVsOZS1MjcBn6B5%2B%2BVAkujGHKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXWMyv8xZWWuV3waEq3AM2eUXhET5b1DEnSQPp68J5F56JsLGDuOPJYRxQToKSf46B7SgiLwchc3ZFyE7d9YPSoIORNw2EQ0vcfj5nq4QWRFdPH5oOmpfTfzjqiv0LuUx69unvHZownlGKcLkBIc1GQtDjrOi0K87LwiNjZin1LgPw4nvKHSTBRfeecQByoGrk0gv67EbseGFZpY5m0qiMDhfilc1iY5f%2BBU%2FOr1Ot87exgl3u%2BOZeNWOpRYl%2Fl2XcALRSFUi49IcFGr3hgLlJ%2BPLrQ76XgBU3nYfmtnD8Z1c7y1lYfjzu0vbhIv%2BBNeeo9uCPu4LyPgiCfksiHOGxTGiK6UHmWx9aydFFeZVtRlgfnYbWuBNlJTQaKxmbt3vOY%2BrpcofupVvdSdn4B2H9SLueXe2s%2BMim%2BHaaLE9WiKRWHLiU%2FOhJ0sArG8rRB%2FgO%2FFfAIybtTm9oq6gh3S2cqhEI%2BfMH5oENSHOwerlbyn35vUiXDLFCULIb%2B3P0I%2Fo7fDfhbcegKBSV1uuQzTExepW4D%2FjFq4ytQK%2BKA5Q6Uw15XxXGNqTYPs6B87y1zMroiQ4gkBnGISLGrL57MIecTK3QdCNRYpSqUhuYRIx1s%2BZgWnDZslisd8ENtu4WshZ%2BTfQm6kelJxN3djDQ3f68BjqkAVQDLcQqp97krQyn1VPHCN%2F0Sm6A6jdec5Gh24sxw9xqxlo3nzxJA2%2BFpGtZDtLUs%2BSy6n6oJIdv0VY8OSJSEAEoP4qZ49DgG%2BysLLweX3W2EpUESfbjVtmDBpbScpRT8dJD5bBDXDVpZXPt7UlPL9OpEPShgg0XXiZx8uIJmAveIVv8NCKfRIVKpd8opRaPChxw2P%2BCTjQKAJzlA9DEkHxAGVJy&X-Amz-Signature=0c58240c99350ca3e9a17edce0246797f4a6cb21247194ae0f63eb2cc9fa1430&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2C4M7HT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBqLXO3WNIlw7O7NvlQsryuDilgUtTwLxAggGYlZuhVAIhAMBMofmVCChLyowUC1awXVsOZS1MjcBn6B5%2B%2BVAkujGHKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXWMyv8xZWWuV3waEq3AM2eUXhET5b1DEnSQPp68J5F56JsLGDuOPJYRxQToKSf46B7SgiLwchc3ZFyE7d9YPSoIORNw2EQ0vcfj5nq4QWRFdPH5oOmpfTfzjqiv0LuUx69unvHZownlGKcLkBIc1GQtDjrOi0K87LwiNjZin1LgPw4nvKHSTBRfeecQByoGrk0gv67EbseGFZpY5m0qiMDhfilc1iY5f%2BBU%2FOr1Ot87exgl3u%2BOZeNWOpRYl%2Fl2XcALRSFUi49IcFGr3hgLlJ%2BPLrQ76XgBU3nYfmtnD8Z1c7y1lYfjzu0vbhIv%2BBNeeo9uCPu4LyPgiCfksiHOGxTGiK6UHmWx9aydFFeZVtRlgfnYbWuBNlJTQaKxmbt3vOY%2BrpcofupVvdSdn4B2H9SLueXe2s%2BMim%2BHaaLE9WiKRWHLiU%2FOhJ0sArG8rRB%2FgO%2FFfAIybtTm9oq6gh3S2cqhEI%2BfMH5oENSHOwerlbyn35vUiXDLFCULIb%2B3P0I%2Fo7fDfhbcegKBSV1uuQzTExepW4D%2FjFq4ytQK%2BKA5Q6Uw15XxXGNqTYPs6B87y1zMroiQ4gkBnGISLGrL57MIecTK3QdCNRYpSqUhuYRIx1s%2BZgWnDZslisd8ENtu4WshZ%2BTfQm6kelJxN3djDQ3f68BjqkAVQDLcQqp97krQyn1VPHCN%2F0Sm6A6jdec5Gh24sxw9xqxlo3nzxJA2%2BFpGtZDtLUs%2BSy6n6oJIdv0VY8OSJSEAEoP4qZ49DgG%2BysLLweX3W2EpUESfbjVtmDBpbScpRT8dJD5bBDXDVpZXPt7UlPL9OpEPShgg0XXiZx8uIJmAveIVv8NCKfRIVKpd8opRaPChxw2P%2BCTjQKAJzlA9DEkHxAGVJy&X-Amz-Signature=742cc128aa187c20b1889302c28b0eaddb6d009ee5542baad59b702c2a2a050d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOVPWDNF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzQMB8pPWsQI7aMm93fEOzrdNGp7Aj6SzDWyB%2Bw4WGvgIgXLNTzqZz4Ej5JgGxcpg0WKfkyA5FV%2Fgk1G%2FijgQjvbYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOAzAXD21CqIDMwPSrcA3bEG2ZuF6eWRc1LrD%2F2lN0XojvTPSoz3Q91gCtcO41XyOZJplxc5haaCpEFd1V2Wz6G2ckvhckM65mAIwDiI%2ByYodRiMzdIf3jXLN5kf1FTvuLPH7KqfRZxeG6vxZrmW3CJCAV0kF9oWPsiD7cIAI4AHcJpCc%2FatvHwtCL4XZ1ofhVQZ9FE3m4wWoxUqWOyFU%2F%2BNs%2BH8YyzTUSXr093g%2BBm1%2BjsgduDuNDN%2BDuPagJ30xypBIj4d%2BM%2Fhc0jjR6iwnJ4uF5vveroPj0uJhLdypDptRAr5G6cyySGn649TEwHJf2njhSEpuODw3fqgErNsrPNClS%2B9W8eb2yt9l5%2F9%2BUCpKHBVHwBzDKzqmYGepoiN8ij3bM6AyDc7FRsK9abX4RKdRU1L1cqih%2FO0ij9hSWkeDoCHIMwk6ml6HN7AcRiQDRaVWpSHEq7E1y%2BsovbdN7vOaqLkLVyxrpcWu0p%2BRVpOSU5S1z4aSYNTM8ht4sl%2BmEbcfNykIFJabfQOqwS26skSj4c%2BxVebuF3sXolAw4ar%2BUfL9tqIVzmNNmCLzUnYVkrbQL%2FdWxP6eiTgLqN%2FbMZYfg%2Bf8%2FcTullhR6UQ33vZb29lyu%2F87iJwTAgkkltWmtRQsAavj4J3RzZMIfb%2FrwGOqUB3ik9BSVRGnP%2FBdsKIhFOulz9hCOlPTF8t4rHCAXw0%2BYtEvyHzp3XYBrznqtvhirMbwPF2UTuCcailiu7ZUOHDASyIVLqpw3mTW1J76lyp3wYpjnIwIje8QSNcMCVSANZMgY4pUjk1wP7y3RTbRVB9cHv1mCM%2BR4E9xtaBitrh%2BIzHN96B3G1cCCVGuNykl0gxgTmA4qdlYuGuDFVFnzkFapjiduh&X-Amz-Signature=8ae1d46686f30afe46268a4cd5d3645f575596f3407f93b5e81c69ba22e843fc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOVPWDNF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzQMB8pPWsQI7aMm93fEOzrdNGp7Aj6SzDWyB%2Bw4WGvgIgXLNTzqZz4Ej5JgGxcpg0WKfkyA5FV%2Fgk1G%2FijgQjvbYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOAzAXD21CqIDMwPSrcA3bEG2ZuF6eWRc1LrD%2F2lN0XojvTPSoz3Q91gCtcO41XyOZJplxc5haaCpEFd1V2Wz6G2ckvhckM65mAIwDiI%2ByYodRiMzdIf3jXLN5kf1FTvuLPH7KqfRZxeG6vxZrmW3CJCAV0kF9oWPsiD7cIAI4AHcJpCc%2FatvHwtCL4XZ1ofhVQZ9FE3m4wWoxUqWOyFU%2F%2BNs%2BH8YyzTUSXr093g%2BBm1%2BjsgduDuNDN%2BDuPagJ30xypBIj4d%2BM%2Fhc0jjR6iwnJ4uF5vveroPj0uJhLdypDptRAr5G6cyySGn649TEwHJf2njhSEpuODw3fqgErNsrPNClS%2B9W8eb2yt9l5%2F9%2BUCpKHBVHwBzDKzqmYGepoiN8ij3bM6AyDc7FRsK9abX4RKdRU1L1cqih%2FO0ij9hSWkeDoCHIMwk6ml6HN7AcRiQDRaVWpSHEq7E1y%2BsovbdN7vOaqLkLVyxrpcWu0p%2BRVpOSU5S1z4aSYNTM8ht4sl%2BmEbcfNykIFJabfQOqwS26skSj4c%2BxVebuF3sXolAw4ar%2BUfL9tqIVzmNNmCLzUnYVkrbQL%2FdWxP6eiTgLqN%2FbMZYfg%2Bf8%2FcTullhR6UQ33vZb29lyu%2F87iJwTAgkkltWmtRQsAavj4J3RzZMIfb%2FrwGOqUB3ik9BSVRGnP%2FBdsKIhFOulz9hCOlPTF8t4rHCAXw0%2BYtEvyHzp3XYBrznqtvhirMbwPF2UTuCcailiu7ZUOHDASyIVLqpw3mTW1J76lyp3wYpjnIwIje8QSNcMCVSANZMgY4pUjk1wP7y3RTbRVB9cHv1mCM%2BR4E9xtaBitrh%2BIzHN96B3G1cCCVGuNykl0gxgTmA4qdlYuGuDFVFnzkFapjiduh&X-Amz-Signature=ec16e361d596cd4d8f1bb16ca0e795f9715699486f4448052ae4d091f13b0d0d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOVPWDNF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzQMB8pPWsQI7aMm93fEOzrdNGp7Aj6SzDWyB%2Bw4WGvgIgXLNTzqZz4Ej5JgGxcpg0WKfkyA5FV%2Fgk1G%2FijgQjvbYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOAzAXD21CqIDMwPSrcA3bEG2ZuF6eWRc1LrD%2F2lN0XojvTPSoz3Q91gCtcO41XyOZJplxc5haaCpEFd1V2Wz6G2ckvhckM65mAIwDiI%2ByYodRiMzdIf3jXLN5kf1FTvuLPH7KqfRZxeG6vxZrmW3CJCAV0kF9oWPsiD7cIAI4AHcJpCc%2FatvHwtCL4XZ1ofhVQZ9FE3m4wWoxUqWOyFU%2F%2BNs%2BH8YyzTUSXr093g%2BBm1%2BjsgduDuNDN%2BDuPagJ30xypBIj4d%2BM%2Fhc0jjR6iwnJ4uF5vveroPj0uJhLdypDptRAr5G6cyySGn649TEwHJf2njhSEpuODw3fqgErNsrPNClS%2B9W8eb2yt9l5%2F9%2BUCpKHBVHwBzDKzqmYGepoiN8ij3bM6AyDc7FRsK9abX4RKdRU1L1cqih%2FO0ij9hSWkeDoCHIMwk6ml6HN7AcRiQDRaVWpSHEq7E1y%2BsovbdN7vOaqLkLVyxrpcWu0p%2BRVpOSU5S1z4aSYNTM8ht4sl%2BmEbcfNykIFJabfQOqwS26skSj4c%2BxVebuF3sXolAw4ar%2BUfL9tqIVzmNNmCLzUnYVkrbQL%2FdWxP6eiTgLqN%2FbMZYfg%2Bf8%2FcTullhR6UQ33vZb29lyu%2F87iJwTAgkkltWmtRQsAavj4J3RzZMIfb%2FrwGOqUB3ik9BSVRGnP%2FBdsKIhFOulz9hCOlPTF8t4rHCAXw0%2BYtEvyHzp3XYBrznqtvhirMbwPF2UTuCcailiu7ZUOHDASyIVLqpw3mTW1J76lyp3wYpjnIwIje8QSNcMCVSANZMgY4pUjk1wP7y3RTbRVB9cHv1mCM%2BR4E9xtaBitrh%2BIzHN96B3G1cCCVGuNykl0gxgTmA4qdlYuGuDFVFnzkFapjiduh&X-Amz-Signature=98098299337c3a1b722653f1522a0f72f3c94b7153ca446beac7f93f6c6a8e47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOVPWDNF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzQMB8pPWsQI7aMm93fEOzrdNGp7Aj6SzDWyB%2Bw4WGvgIgXLNTzqZz4Ej5JgGxcpg0WKfkyA5FV%2Fgk1G%2FijgQjvbYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOAzAXD21CqIDMwPSrcA3bEG2ZuF6eWRc1LrD%2F2lN0XojvTPSoz3Q91gCtcO41XyOZJplxc5haaCpEFd1V2Wz6G2ckvhckM65mAIwDiI%2ByYodRiMzdIf3jXLN5kf1FTvuLPH7KqfRZxeG6vxZrmW3CJCAV0kF9oWPsiD7cIAI4AHcJpCc%2FatvHwtCL4XZ1ofhVQZ9FE3m4wWoxUqWOyFU%2F%2BNs%2BH8YyzTUSXr093g%2BBm1%2BjsgduDuNDN%2BDuPagJ30xypBIj4d%2BM%2Fhc0jjR6iwnJ4uF5vveroPj0uJhLdypDptRAr5G6cyySGn649TEwHJf2njhSEpuODw3fqgErNsrPNClS%2B9W8eb2yt9l5%2F9%2BUCpKHBVHwBzDKzqmYGepoiN8ij3bM6AyDc7FRsK9abX4RKdRU1L1cqih%2FO0ij9hSWkeDoCHIMwk6ml6HN7AcRiQDRaVWpSHEq7E1y%2BsovbdN7vOaqLkLVyxrpcWu0p%2BRVpOSU5S1z4aSYNTM8ht4sl%2BmEbcfNykIFJabfQOqwS26skSj4c%2BxVebuF3sXolAw4ar%2BUfL9tqIVzmNNmCLzUnYVkrbQL%2FdWxP6eiTgLqN%2FbMZYfg%2Bf8%2FcTullhR6UQ33vZb29lyu%2F87iJwTAgkkltWmtRQsAavj4J3RzZMIfb%2FrwGOqUB3ik9BSVRGnP%2FBdsKIhFOulz9hCOlPTF8t4rHCAXw0%2BYtEvyHzp3XYBrznqtvhirMbwPF2UTuCcailiu7ZUOHDASyIVLqpw3mTW1J76lyp3wYpjnIwIje8QSNcMCVSANZMgY4pUjk1wP7y3RTbRVB9cHv1mCM%2BR4E9xtaBitrh%2BIzHN96B3G1cCCVGuNykl0gxgTmA4qdlYuGuDFVFnzkFapjiduh&X-Amz-Signature=00a3f1f7dffcadce46d8dc1ebac1714e4a1c3d0251cc058ad6b8f8e7fe0823ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOVPWDNF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzQMB8pPWsQI7aMm93fEOzrdNGp7Aj6SzDWyB%2Bw4WGvgIgXLNTzqZz4Ej5JgGxcpg0WKfkyA5FV%2Fgk1G%2FijgQjvbYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOAzAXD21CqIDMwPSrcA3bEG2ZuF6eWRc1LrD%2F2lN0XojvTPSoz3Q91gCtcO41XyOZJplxc5haaCpEFd1V2Wz6G2ckvhckM65mAIwDiI%2ByYodRiMzdIf3jXLN5kf1FTvuLPH7KqfRZxeG6vxZrmW3CJCAV0kF9oWPsiD7cIAI4AHcJpCc%2FatvHwtCL4XZ1ofhVQZ9FE3m4wWoxUqWOyFU%2F%2BNs%2BH8YyzTUSXr093g%2BBm1%2BjsgduDuNDN%2BDuPagJ30xypBIj4d%2BM%2Fhc0jjR6iwnJ4uF5vveroPj0uJhLdypDptRAr5G6cyySGn649TEwHJf2njhSEpuODw3fqgErNsrPNClS%2B9W8eb2yt9l5%2F9%2BUCpKHBVHwBzDKzqmYGepoiN8ij3bM6AyDc7FRsK9abX4RKdRU1L1cqih%2FO0ij9hSWkeDoCHIMwk6ml6HN7AcRiQDRaVWpSHEq7E1y%2BsovbdN7vOaqLkLVyxrpcWu0p%2BRVpOSU5S1z4aSYNTM8ht4sl%2BmEbcfNykIFJabfQOqwS26skSj4c%2BxVebuF3sXolAw4ar%2BUfL9tqIVzmNNmCLzUnYVkrbQL%2FdWxP6eiTgLqN%2FbMZYfg%2Bf8%2FcTullhR6UQ33vZb29lyu%2F87iJwTAgkkltWmtRQsAavj4J3RzZMIfb%2FrwGOqUB3ik9BSVRGnP%2FBdsKIhFOulz9hCOlPTF8t4rHCAXw0%2BYtEvyHzp3XYBrznqtvhirMbwPF2UTuCcailiu7ZUOHDASyIVLqpw3mTW1J76lyp3wYpjnIwIje8QSNcMCVSANZMgY4pUjk1wP7y3RTbRVB9cHv1mCM%2BR4E9xtaBitrh%2BIzHN96B3G1cCCVGuNykl0gxgTmA4qdlYuGuDFVFnzkFapjiduh&X-Amz-Signature=af3a41e1bcaf26ef182f362bc9d00e012f9dad5fb139e15317db30fd471ac1f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOVPWDNF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzQMB8pPWsQI7aMm93fEOzrdNGp7Aj6SzDWyB%2Bw4WGvgIgXLNTzqZz4Ej5JgGxcpg0WKfkyA5FV%2Fgk1G%2FijgQjvbYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOAzAXD21CqIDMwPSrcA3bEG2ZuF6eWRc1LrD%2F2lN0XojvTPSoz3Q91gCtcO41XyOZJplxc5haaCpEFd1V2Wz6G2ckvhckM65mAIwDiI%2ByYodRiMzdIf3jXLN5kf1FTvuLPH7KqfRZxeG6vxZrmW3CJCAV0kF9oWPsiD7cIAI4AHcJpCc%2FatvHwtCL4XZ1ofhVQZ9FE3m4wWoxUqWOyFU%2F%2BNs%2BH8YyzTUSXr093g%2BBm1%2BjsgduDuNDN%2BDuPagJ30xypBIj4d%2BM%2Fhc0jjR6iwnJ4uF5vveroPj0uJhLdypDptRAr5G6cyySGn649TEwHJf2njhSEpuODw3fqgErNsrPNClS%2B9W8eb2yt9l5%2F9%2BUCpKHBVHwBzDKzqmYGepoiN8ij3bM6AyDc7FRsK9abX4RKdRU1L1cqih%2FO0ij9hSWkeDoCHIMwk6ml6HN7AcRiQDRaVWpSHEq7E1y%2BsovbdN7vOaqLkLVyxrpcWu0p%2BRVpOSU5S1z4aSYNTM8ht4sl%2BmEbcfNykIFJabfQOqwS26skSj4c%2BxVebuF3sXolAw4ar%2BUfL9tqIVzmNNmCLzUnYVkrbQL%2FdWxP6eiTgLqN%2FbMZYfg%2Bf8%2FcTullhR6UQ33vZb29lyu%2F87iJwTAgkkltWmtRQsAavj4J3RzZMIfb%2FrwGOqUB3ik9BSVRGnP%2FBdsKIhFOulz9hCOlPTF8t4rHCAXw0%2BYtEvyHzp3XYBrznqtvhirMbwPF2UTuCcailiu7ZUOHDASyIVLqpw3mTW1J76lyp3wYpjnIwIje8QSNcMCVSANZMgY4pUjk1wP7y3RTbRVB9cHv1mCM%2BR4E9xtaBitrh%2BIzHN96B3G1cCCVGuNykl0gxgTmA4qdlYuGuDFVFnzkFapjiduh&X-Amz-Signature=ad09476972f89fd4af7acab825134318891ff697fad750325d22a7e4981b935a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Q2FJ2XQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB1fQfrqwg8ul3XE5hzpnVnQSoyFNXqxjy7eLwY6r31CAiEA63RftTnv4UD955stJNofK0mdCLJH5QnGwS7wnJR8bTEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJPlomMBE4Qi9fa1WircA1n17mD4rpIkRkbDJ2LsA9q08qonOVW7qrr4DMutqSCVusTJCh4O0FXhQSoB3cDDcwbT7eQi7fhrpumEKcXhwu9i%2FO%2BGn0PJjH1t6ENoYCby1PguiQhFx1aeJptYjkJXylJHBZffwz3qSrbjqFz%2FmjfkKKQKYBgFxRCycLVfPlv2VoT5ZRTHBu0HNqmWCLCsID5VZUbc0gGOQUNm3QI%2B0RDuYd1uaTZqN49tsHv%2B8J4nO0vifnttlWtcTRtzynfYdSQH4L%2BhUOf4sExewKG3si4RqK%2BoaL79OCLeGgjTyiCqazlHdEFbVSLHrAJWRJtNNgvqgOADbEK%2BKxzHng%2B5xSOk%2BXQo8nSDub%2FBtD4%2FPSKZTVi8Km3x8l6nj%2FaJ258pJxusHIg4o1YsCsxbR%2B23DWyhnJuG9Di2P7dwEIxv%2FWmXnHVgKrtncXXsZObWNfJMGX28Ro%2FZY1c7lDV3Dd%2BsVCcqvJtC9BFoaYWeR2T587zhZKEjhc%2FaqmnC9RXuPOv8%2FpAwkZJq34K7WxbLmIFHcEZ7t5BAG0ZrI9wSEuisiOyyGl2Lpg%2F7Yiw%2Ffep7Zyf92J0Tm59IsgBXfviuKbbsUOYNzEmXP0yVpdGS6zF%2FxBMFJn%2B89TVcvU3YMEU2MN3l%2FrwGOqUBszEduffnxtVY0lry5agaz8IuguH8Sq5kZio0Fb60AKBO4bZbEppIA0i78HzCXU%2F9GNLNXC0sTuvbOTqRWCQMkXGAzIAQOeLj7SFbMOPZ2FCS3uX6BncIXDUrzuJMxFQg%2F8konUZc8Opfcztry2jx3uH2TIIwoJnzm2NaBQnByRExLbeg1jZqX%2BJYrZsKajXWHDgkKb45w2l%2BRicGQkJYTFKa8O2W&X-Amz-Signature=effe3458a976d1373b6320364659d6007b794228288834140c94ed83fc4d4789&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FNSCA3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFNKyUANm6jfngAzgFL%2F%2BL7wBnQb27Wwfjd7C4lmin6sAiEA1cUJSKVvIwazV5S2KacCGq%2BJw6gaDKfH4edZ6UDH0LUqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB7eAiuzfRDScAQ4jyrcAyuouhu%2F2wbYSsVsa%2FsWqqaSi7emN2dFm4fBUyRgCYVMEr6mn2JWkWkSZGnnYSFoXl9e50w5AoUGaIBJpPW2XSkeQU5A2%2BbqOFbkPndbhjX%2BzuL9JF9ugCLfa7YAeKXOTEQUUkJ4ZbgmyJe3TEByNVt4M%2B7KU1W05KAdP3PdJKCbLB9VX89Y7nkKYW%2BjFamYXTOcbxOLKJIeQWyuvKhh9IBEfK%2Fy9mQG3Sl81msaL%2BfTFhOfcjlWV9KDQV8QSdGgYo7Nphf%2BXqQcgwecvYdj5PSo3yII3%2F9FQLcblqU8SJbY7F9hzLgtAi%2BwXbl%2Bq8dpAHLGdxiaUjo5AmXglU8w9g0aTLPqNPfKY12CaouJtWZVAWkQ7MUchRaq882K%2Brapx5ZK4FgSuTATq4kk39nhz5neHD1r62Bfo86bmAXhRzPUyZf%2Fa7Ldnz8sCUfJ%2BZAevi7OnmshA%2F2Y8G9tZHxaqfhaooSt8YKJJALLeOnewtHYSACDDHmfTBpElqau6zvS85N22GEf5UGBZuBY08wj11dpTarCRy8z9H0VLbIAP2ELZEZc86TVmPw0onhLIt8a0mOaOOZzrDYkDaGnRbCBGPWV5FRs7wttSvjhWpMwgKtZSPBNX2olW1yHYV7mMOXX%2FrwGOqUBC%2BTN6axaR5jxcqwPDMwyW1ENJhiSGsE2LVVb50XYeuoZrCw%2FWKkJbag3zUo8UhuSZIocgum5iuxJwC97k9R5IVMhndjbfG1VoOM%2B5%2FzxSHeMVukYmKsBnz4dOhXKWRabKlb544MCwMOKnZctt%2BreYO8YRll5%2FhEEL2HXI26fDZvUtQqDQ6nWWkPP%2FDvwElyX8aTjgpx%2BrKdRdPMYXMdVWxYFV1Zf&X-Amz-Signature=ccd477d92efdf2fdd38ef4143a4d54422ec6bdb74583ee312da367cd5cc9a53d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOVPWDNF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzQMB8pPWsQI7aMm93fEOzrdNGp7Aj6SzDWyB%2Bw4WGvgIgXLNTzqZz4Ej5JgGxcpg0WKfkyA5FV%2Fgk1G%2FijgQjvbYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOAzAXD21CqIDMwPSrcA3bEG2ZuF6eWRc1LrD%2F2lN0XojvTPSoz3Q91gCtcO41XyOZJplxc5haaCpEFd1V2Wz6G2ckvhckM65mAIwDiI%2ByYodRiMzdIf3jXLN5kf1FTvuLPH7KqfRZxeG6vxZrmW3CJCAV0kF9oWPsiD7cIAI4AHcJpCc%2FatvHwtCL4XZ1ofhVQZ9FE3m4wWoxUqWOyFU%2F%2BNs%2BH8YyzTUSXr093g%2BBm1%2BjsgduDuNDN%2BDuPagJ30xypBIj4d%2BM%2Fhc0jjR6iwnJ4uF5vveroPj0uJhLdypDptRAr5G6cyySGn649TEwHJf2njhSEpuODw3fqgErNsrPNClS%2B9W8eb2yt9l5%2F9%2BUCpKHBVHwBzDKzqmYGepoiN8ij3bM6AyDc7FRsK9abX4RKdRU1L1cqih%2FO0ij9hSWkeDoCHIMwk6ml6HN7AcRiQDRaVWpSHEq7E1y%2BsovbdN7vOaqLkLVyxrpcWu0p%2BRVpOSU5S1z4aSYNTM8ht4sl%2BmEbcfNykIFJabfQOqwS26skSj4c%2BxVebuF3sXolAw4ar%2BUfL9tqIVzmNNmCLzUnYVkrbQL%2FdWxP6eiTgLqN%2FbMZYfg%2Bf8%2FcTullhR6UQ33vZb29lyu%2F87iJwTAgkkltWmtRQsAavj4J3RzZMIfb%2FrwGOqUB3ik9BSVRGnP%2FBdsKIhFOulz9hCOlPTF8t4rHCAXw0%2BYtEvyHzp3XYBrznqtvhirMbwPF2UTuCcailiu7ZUOHDASyIVLqpw3mTW1J76lyp3wYpjnIwIje8QSNcMCVSANZMgY4pUjk1wP7y3RTbRVB9cHv1mCM%2BR4E9xtaBitrh%2BIzHN96B3G1cCCVGuNykl0gxgTmA4qdlYuGuDFVFnzkFapjiduh&X-Amz-Signature=d010474a9c492f8d636482b2eb96f6a314b239a5068a04ab676b7b023d96df61&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOVPWDNF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzQMB8pPWsQI7aMm93fEOzrdNGp7Aj6SzDWyB%2Bw4WGvgIgXLNTzqZz4Ej5JgGxcpg0WKfkyA5FV%2Fgk1G%2FijgQjvbYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOAzAXD21CqIDMwPSrcA3bEG2ZuF6eWRc1LrD%2F2lN0XojvTPSoz3Q91gCtcO41XyOZJplxc5haaCpEFd1V2Wz6G2ckvhckM65mAIwDiI%2ByYodRiMzdIf3jXLN5kf1FTvuLPH7KqfRZxeG6vxZrmW3CJCAV0kF9oWPsiD7cIAI4AHcJpCc%2FatvHwtCL4XZ1ofhVQZ9FE3m4wWoxUqWOyFU%2F%2BNs%2BH8YyzTUSXr093g%2BBm1%2BjsgduDuNDN%2BDuPagJ30xypBIj4d%2BM%2Fhc0jjR6iwnJ4uF5vveroPj0uJhLdypDptRAr5G6cyySGn649TEwHJf2njhSEpuODw3fqgErNsrPNClS%2B9W8eb2yt9l5%2F9%2BUCpKHBVHwBzDKzqmYGepoiN8ij3bM6AyDc7FRsK9abX4RKdRU1L1cqih%2FO0ij9hSWkeDoCHIMwk6ml6HN7AcRiQDRaVWpSHEq7E1y%2BsovbdN7vOaqLkLVyxrpcWu0p%2BRVpOSU5S1z4aSYNTM8ht4sl%2BmEbcfNykIFJabfQOqwS26skSj4c%2BxVebuF3sXolAw4ar%2BUfL9tqIVzmNNmCLzUnYVkrbQL%2FdWxP6eiTgLqN%2FbMZYfg%2Bf8%2FcTullhR6UQ33vZb29lyu%2F87iJwTAgkkltWmtRQsAavj4J3RzZMIfb%2FrwGOqUB3ik9BSVRGnP%2FBdsKIhFOulz9hCOlPTF8t4rHCAXw0%2BYtEvyHzp3XYBrznqtvhirMbwPF2UTuCcailiu7ZUOHDASyIVLqpw3mTW1J76lyp3wYpjnIwIje8QSNcMCVSANZMgY4pUjk1wP7y3RTbRVB9cHv1mCM%2BR4E9xtaBitrh%2BIzHN96B3G1cCCVGuNykl0gxgTmA4qdlYuGuDFVFnzkFapjiduh&X-Amz-Signature=fa155b4089d0c345b521a47fbace0e68366b3757b4ddc8a640431c0b3eeed3b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOVPWDNF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzQMB8pPWsQI7aMm93fEOzrdNGp7Aj6SzDWyB%2Bw4WGvgIgXLNTzqZz4Ej5JgGxcpg0WKfkyA5FV%2Fgk1G%2FijgQjvbYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPOAzAXD21CqIDMwPSrcA3bEG2ZuF6eWRc1LrD%2F2lN0XojvTPSoz3Q91gCtcO41XyOZJplxc5haaCpEFd1V2Wz6G2ckvhckM65mAIwDiI%2ByYodRiMzdIf3jXLN5kf1FTvuLPH7KqfRZxeG6vxZrmW3CJCAV0kF9oWPsiD7cIAI4AHcJpCc%2FatvHwtCL4XZ1ofhVQZ9FE3m4wWoxUqWOyFU%2F%2BNs%2BH8YyzTUSXr093g%2BBm1%2BjsgduDuNDN%2BDuPagJ30xypBIj4d%2BM%2Fhc0jjR6iwnJ4uF5vveroPj0uJhLdypDptRAr5G6cyySGn649TEwHJf2njhSEpuODw3fqgErNsrPNClS%2B9W8eb2yt9l5%2F9%2BUCpKHBVHwBzDKzqmYGepoiN8ij3bM6AyDc7FRsK9abX4RKdRU1L1cqih%2FO0ij9hSWkeDoCHIMwk6ml6HN7AcRiQDRaVWpSHEq7E1y%2BsovbdN7vOaqLkLVyxrpcWu0p%2BRVpOSU5S1z4aSYNTM8ht4sl%2BmEbcfNykIFJabfQOqwS26skSj4c%2BxVebuF3sXolAw4ar%2BUfL9tqIVzmNNmCLzUnYVkrbQL%2FdWxP6eiTgLqN%2FbMZYfg%2Bf8%2FcTullhR6UQ33vZb29lyu%2F87iJwTAgkkltWmtRQsAavj4J3RzZMIfb%2FrwGOqUB3ik9BSVRGnP%2FBdsKIhFOulz9hCOlPTF8t4rHCAXw0%2BYtEvyHzp3XYBrznqtvhirMbwPF2UTuCcailiu7ZUOHDASyIVLqpw3mTW1J76lyp3wYpjnIwIje8QSNcMCVSANZMgY4pUjk1wP7y3RTbRVB9cHv1mCM%2BR4E9xtaBitrh%2BIzHN96B3G1cCCVGuNykl0gxgTmA4qdlYuGuDFVFnzkFapjiduh&X-Amz-Signature=1f00f73fc83fff0c1a06c8a9f5cdf8465e95679d6ee620a713fbee6b5f3e247f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KJKGDEN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGa2lOev7ayizbDaY19fgFPRjBFfgVTLHgZqDqCQ0%2FnpAiAaIAP0qnRfP40kan6yzV8mkEx1oAIrYkyONoYwyUnb0iqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxwoJ%2B5sFIPRMu6GoKtwDO8agfG7aXu%2Bct45iXPq9FpdXCyECyRBdwJaRJJmwQaTzy4fPtysLmgof91iGsO34bd4b48SEdVix9wtS4l6eUZHoqpHA1D2OleV3zxichV6dq3R3PuBD5Ueo5yUbPuI2BK1diK4QUCkw%2FXdFXD6cKlH%2BDXG6VqBEVgbjzjTAvpw6tJoYBMKIu6MM5VGjem9oVVD6XmuRIfDpXjfzjbEnKTLAG%2FVjIo5v8AylhLvNY3Y0X5DR4HJfmAZJaKvyPSotvsd3rhFdN8b9EqokD6l2IAAUajShDq5YZ0ErDMKbJFrvg4hAJUBqSoDvep%2Fu%2FNpQR%2FktaqbbhfvoMLFvwGzr8vUgQS7bIQKcG0AhUbSY0mntp51xJeXl3j9bfDFt83Z4W14pIKcvTQAL5CyNU56wKIGw62XxoQbydwCtPjClQA6ceRWoKui0ZN%2F%2BYsTn4p56wpn2bvXkXbm5eQiQ%2FdKDB3S7yVd%2BlN8fl7DO75MzdA%2FUmGj%2BEVGfVKnQZDq3Gr9N9M%2Fr1EdYY7UJbPY8%2B7JxGzkEwvHykM%2B5LxPazWVYZNWGL4Pt4GzvLIUxuGkhIFhOgt3VJd%2Bg5nKwvfjffIkSH3rVHYk1HKJZeau2t9FB2adEjExrEpRVVIuzLVMwpN3%2BvAY6pgHNrvDIfUAjfceguImJQHBnFj8TYEev0DM2nZ6%2F5A5myA93fkqsjh0%2Fkp0W8jm6dEdS%2BCwTm%2B6QiWNfg7vWrluxhEEalZwRBEVoep9OgFkFq2A0HTZKLhuJPiqBXp8SOBKo6PV0CimWcUYXWZnQpx8Vp4kb%2FbBwnHa7cIM%2F4xumGR3alGOSERkuTpaC%2F%2BiKj2yCWRwGDE35YZ5JILf%2BgW%2BzHGkPuzL7&X-Amz-Signature=7b717a2d5d5bf14c822b45568c2fb3650a6fa2a78328cb38023560e9d5ca9601&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IDC7P65%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCy3j5%2BbwfZwmQSp%2BM%2FmeBzX1rgHHDYV72DOOLDDqxp8AIgCoo6%2FWGcR%2BkU1jSMf6N1esA18OE3%2Fmlb8ytE8fq17AgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEgJgeuUcg%2Bp%2BKNFwSrcA%2FALivRU7SCr1rfL84%2B%2FXfBV8LP4lFqog%2FcrlM%2BCjAABesPG0dSyTWwGwR%2FqdHVm6Czewfbsgy9YX9h%2F6FVQgqyvh%2FWV1UA4S1WpgHDPuIPExrrKdWf15X2FrUTeStlyecCLMfRjsk%2FV2L5S8Bxv9P0wMFIb18sXJ4jpCS0NW%2Fazp5vw6IPK4G0ryRUphjoWUfmc0oTcj4mcc8Py9H%2BIdYOSUxJ3QFwtG%2Bcm%2FhUrkDzRLLV1Rx4%2FSlxOhm9BsqHytSDPzd3rT4h8pmyH5YU4W2aSPpV3pv1qqTyEZSRCkJX7ItCYnfzik9SRZ1nM9BvRHRGVbU558Qd59f1i9znbWPfUJZlohgyJMP7UkS3Y%2BlXiWsg2Qxxi5gtLeTHDAT14gBPT%2Fb83VCAxC2SG8KXBl%2BjSx34V78G%2Fnm5Z3N7kE5WCot8g1cyrC7G2wGwob5%2Bf9iBZYiM%2FaL7Y3RRedq062Fjtpgl6%2BBCL6i2yzQrq5ywhvVKywcAMJ78YztlRz7ZzNwvowJhWRDId2i8gNif%2BA4pewQnEwGEZyLyQRjwE8GQs7Io1ffKpGQUzp6BhWd60CzGOjYU1HwfCKCbRunYj2Ds9V8a1vneBD%2B8h3bedBB7X%2BwUSv28f%2FqXxzAziMKXl%2FrwGOqUBiQC035wC%2F%2FngcwMbVkMu1R3uh6gUZnmukXpAemW9z%2BIrcZt3BRBtLivAFyQsv24nCoEHFz1srvqOGHCApMwfRESQgQM3C4ekgFI7XyMRfE12cURVMeUWPPEWF7oikzCVvFWkO8itAp0ITc5uo6JttrWX8B0DuubA%2BUWcCyfMHtNN187JjWoveH5vi7N3yHSeY5PMkChs6bvcW%2B4yUYpbBw2GebW5&X-Amz-Signature=800d8c909f0d9d39436bb04c136c8ac973f3432b7af27a03eeb7df6df6b45495&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLDBWRFC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEIW1M6P9RkxYjoxAW0011nU79xr8mYReSK85XbbSo%2BHAiEArA2Wme4T5l0tMfRdKqNrtVvmyD6QiJ7wtjWHFw8E%2BDkqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK64mwfG4nXVH33NRircAyM5Cy9TQF0P%2FpRZ1wMZWNTN%2BCsPrhc5VDS%2BmkVGkr1B4XXmFE%2Be6RNsP8tQDC5WTpQ73Ozf7AL1yH3eifb8dnDwXSBFXnMG1wj4FIUCRPvtGh7CgYjNP4zKgIzMNqeITJhCx2gm0eTCdIyKNN5w33PxG3U2LC1ukqcT9Stgg6ONr9GJQlCIKXVJO2DOx6Al%2Fai0VusBqoWFxX92dYBbZh3yC1ubAS%2FBo1eO%2FnJ2eywLM6ksNQqz2aYyIZk5I65TLDn0jQa1S2hMSM26n42%2F5nQ23%2BCH%2BVxphjy5khvOKvt%2FaS98kh39gnuz4y9kNOayE%2BXDAwRqYEACDUrAzI34maGD%2BaZ%2B3o0cN6QMT8me0M87NpPsaJp2uIQyhbhLwtAe%2BcLa6xv379wbKD32zBy8muRiJ1wwUsktC%2Bc3W55IIBZi3qLWaaWJ7jIf21aTaC2guA6Gs77a5uTegKXSSS42yOWDBUHQdN%2F8PPFLLui54kYTAQPJFuZNlOXN3dPchKVCYn3%2BHc%2BFhqY0SibZ5G4mSF9gWlPxw1gY5dg0LSJRXcbovDCRxLuhNoYyvUymt7u1%2BcerhyP2f%2FVdMscmsdo9xpLsgV%2FyaAlQujDlEh%2BqBFJ24QJTgZhyoDr9QRlMMJLT%2FrwGOqUBUCpICmxV%2BJW0zXnnvjKkZggrv34Ziclh%2BMW7yz%2F%2Br2s9tJVBo8sS924Csa8V5FGbO6qPA0rq7zi%2BKIy2kRM1oRGjj6A28YedU%2BkkmFyGXjpP67ehQoCc1%2BI5yw8Lcurs6aczsZE%2FxGQwhtXwYrcyc6sQ36KOmGi9iSlb45Ti3e8SrU2IWqtmKwft%2FoBvHPXMBp7V5mhdH04ssyOqPmsoyzIIgso6&X-Amz-Signature=c1029cee90edc710300bd1148bfd7a976be43c26e7c7c0403650f0f412c083b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VS3TFDV6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkQbi4t7Et%2BVDHs1TR2NLTATGTbn%2F9mMAuDSHAXNuw7AIgJF7Hss72zfrcWeoJzy8jPf4%2F6ITImfjJgW%2FKzzlS4zEqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHk0h3MVps%2FsTHHVxircA8lsZtatqAODhBM%2BEyWhd%2BS4IWhlUGiHtJHDUDxzbOKXbyZJjVT0jXJJcqRXxhgjkLg6%2BTpUt0Z5l7DtRZb82kRIMEYfnCETenYd%2BhYFxYGLS2lzPWiPnvCxuJl8nhMT2gtGedv0wHG6VpUjueUOvcxyYvMYPHXAjISG7xqcQIF9rmUTjU4H4N2Krihtvax67nc3bIBiy%2BwdrklZcoTKdON5GFVAc%2B8J0ISGzaEMe2VAenYhFctCGHKxuh95am5prBoQ52Ec%2FVZS1m8IC6uwsqZKLmDKmV5XZtsi%2FIPllFxeMNpgIvJsncyS92%2B8Gy39JWVEmu2ObNHHUPXg9bu%2FNfVs%2FgYujmuXLGjNVDUUSFLSFPLtIcUZTC7IrkNU5WwwH7NhZ1W%2BS6T83OCxmNi08PApo75dz6ldSO1VLWXx%2B89RyV8aJMs%2Bgx6RCVkPwWxgz%2BpE5D4gS2%2BhRtTNCYH7Imw3yLeoXsMImKBYE2TLqzdooGdOZcT%2Fk5c41GPZ2KpzRcEqRY1DQouoiz4OLCoWjrWUj1lx%2FmvUeGLssPrEFgb23eL4aYhZVRWVg3Avk2iz3CBQecH8RxOlpT7sJTS2fKFZHhgTMi8r0cdcZUF3QoiOolDsADWhUC0fc3jkMKGT%2FrwGOqUBAIKc0mLhR%2Fq7AtdvJ9n37ej%2BRXaaSvdKp6vMQV7H0Jvoj50qKjKhevsNCr76YaBKFihGGHkmY7k6lj%2Btrg%2FAMEl%2FGxAb%2BicNR33yzD4F2dIpRSWLXV9fKJgA0TFFhv6ZGjM90hKhhc%2BkzeI3ftcZT9Tx7j6eTJobOnVYoJBvJ%2B6HTwrKJU3SJjzSTgIw%2FLSbGxk6EEz5MgTRq93f3ZkscbQoR0AW&X-Amz-Signature=182a3ae181f6e656f50e9b1539963e78cf9c5ad9e6182cac9d6db2542cc097ff&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VS3TFDV6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkQbi4t7Et%2BVDHs1TR2NLTATGTbn%2F9mMAuDSHAXNuw7AIgJF7Hss72zfrcWeoJzy8jPf4%2F6ITImfjJgW%2FKzzlS4zEqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHk0h3MVps%2FsTHHVxircA8lsZtatqAODhBM%2BEyWhd%2BS4IWhlUGiHtJHDUDxzbOKXbyZJjVT0jXJJcqRXxhgjkLg6%2BTpUt0Z5l7DtRZb82kRIMEYfnCETenYd%2BhYFxYGLS2lzPWiPnvCxuJl8nhMT2gtGedv0wHG6VpUjueUOvcxyYvMYPHXAjISG7xqcQIF9rmUTjU4H4N2Krihtvax67nc3bIBiy%2BwdrklZcoTKdON5GFVAc%2B8J0ISGzaEMe2VAenYhFctCGHKxuh95am5prBoQ52Ec%2FVZS1m8IC6uwsqZKLmDKmV5XZtsi%2FIPllFxeMNpgIvJsncyS92%2B8Gy39JWVEmu2ObNHHUPXg9bu%2FNfVs%2FgYujmuXLGjNVDUUSFLSFPLtIcUZTC7IrkNU5WwwH7NhZ1W%2BS6T83OCxmNi08PApo75dz6ldSO1VLWXx%2B89RyV8aJMs%2Bgx6RCVkPwWxgz%2BpE5D4gS2%2BhRtTNCYH7Imw3yLeoXsMImKBYE2TLqzdooGdOZcT%2Fk5c41GPZ2KpzRcEqRY1DQouoiz4OLCoWjrWUj1lx%2FmvUeGLssPrEFgb23eL4aYhZVRWVg3Avk2iz3CBQecH8RxOlpT7sJTS2fKFZHhgTMi8r0cdcZUF3QoiOolDsADWhUC0fc3jkMKGT%2FrwGOqUBAIKc0mLhR%2Fq7AtdvJ9n37ej%2BRXaaSvdKp6vMQV7H0Jvoj50qKjKhevsNCr76YaBKFihGGHkmY7k6lj%2Btrg%2FAMEl%2FGxAb%2BicNR33yzD4F2dIpRSWLXV9fKJgA0TFFhv6ZGjM90hKhhc%2BkzeI3ftcZT9Tx7j6eTJobOnVYoJBvJ%2B6HTwrKJU3SJjzSTgIw%2FLSbGxk6EEz5MgTRq93f3ZkscbQoR0AW&X-Amz-Signature=a9fc99da974789090ea37ba9f541ab3be8de51607dd8b10c14c15d81eb1ee6e1&X-Amz-SignedHeaders=host&x-id=GetObject)

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
