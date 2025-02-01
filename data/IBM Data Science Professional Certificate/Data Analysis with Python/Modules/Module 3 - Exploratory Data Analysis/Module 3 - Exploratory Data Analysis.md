

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQYQWT6Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDW6zxytJXQLwQn3XhcFr7d5gp%2BkWllsO%2ByQVpFMAeeiAiEA7zZXrDpN2HYyf87VkAnShVAsBx6epnOdPdijftH8zHkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNMyjAFfQTA6Z3U%2FoCrcAxEUPyLzekDRftbFHNUlrz6FHNZgrt0QViC45Y4uz5GN6TmnfUNxbMasoo8vdKBg1V9GdkLf3NqjST4NRvq6z5qA1TBtuL6DDM1m2DvFXVv1rfKQe1jEpTnbSkt%2Fkr9lIVI60dthBU1wjBkR1gl%2FGKG%2F5GNw02kS1PzZo353b0syTDWaAxahQl19BSzG1bx4nRR1no5gzFd06nDk%2FrYmXmITmyc9AHcWn4jqHU3hoV3jlk2l3tUO%2FYJzpZwGTQ8UQDGuQAxYoK7%2B016nR1P60wpk0Kj4CU2hh%2BlZ4VDFfpBAbKUDB9lEEKH94rjo8S%2Bdk1kvoiTeL6z7OhRH1zCV7Ttlp5l%2FJK6Zw1M8qZ3jNZfyUSDPeEjFYLuOaK1yu6oPwly7njXU56Znw8v%2B93V0HXroikIon5mMTsUymjxuqWwyrUhyvQ%2Flo50y7SDl8cwtxmfqpsVrTdNQKzofB4HVEZQ3VJ58YlACivFIgQw499SONujLm9rWjhkw%2BRTPdyO5%2BDvd%2B63f5lElCM04Xf6Xz7fo5jn7VGwc7FNmcFOFBsDMG%2BpKhIsDdt6DkuiOmA8RcUpOpdmL%2FfX%2BhhVRr%2Bqvu3gv88WpHJSjHqQ9iK2n0T99112sLRUd22o%2FVSy3MOik97wGOqUBC5mzRud8PPJ2KKXJDbEmfpHcdNzodvBd0riTzYPxqXZ1LdcWveBX6MMzqmXOHtipxR6ciIDeOzQhBFJeXsv0nOX1lhg6ONe6eNLUDHH1X9zZ%2FGMDUy4Ka7pJipBp%2Bo1B3fIJyRKYDL6roo6gJuzeRmxROsF8KpqsE4ABVg4LOinIzRTCkOgu0yT4rIor1veP8RzdRVqOWk58eDkhaxhmZw2Cjj4w&X-Amz-Signature=e6569b65e39bbf632f73574f573869057fdd846e9345b6477391f7525df5639a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQYQWT6Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDW6zxytJXQLwQn3XhcFr7d5gp%2BkWllsO%2ByQVpFMAeeiAiEA7zZXrDpN2HYyf87VkAnShVAsBx6epnOdPdijftH8zHkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNMyjAFfQTA6Z3U%2FoCrcAxEUPyLzekDRftbFHNUlrz6FHNZgrt0QViC45Y4uz5GN6TmnfUNxbMasoo8vdKBg1V9GdkLf3NqjST4NRvq6z5qA1TBtuL6DDM1m2DvFXVv1rfKQe1jEpTnbSkt%2Fkr9lIVI60dthBU1wjBkR1gl%2FGKG%2F5GNw02kS1PzZo353b0syTDWaAxahQl19BSzG1bx4nRR1no5gzFd06nDk%2FrYmXmITmyc9AHcWn4jqHU3hoV3jlk2l3tUO%2FYJzpZwGTQ8UQDGuQAxYoK7%2B016nR1P60wpk0Kj4CU2hh%2BlZ4VDFfpBAbKUDB9lEEKH94rjo8S%2Bdk1kvoiTeL6z7OhRH1zCV7Ttlp5l%2FJK6Zw1M8qZ3jNZfyUSDPeEjFYLuOaK1yu6oPwly7njXU56Znw8v%2B93V0HXroikIon5mMTsUymjxuqWwyrUhyvQ%2Flo50y7SDl8cwtxmfqpsVrTdNQKzofB4HVEZQ3VJ58YlACivFIgQw499SONujLm9rWjhkw%2BRTPdyO5%2BDvd%2B63f5lElCM04Xf6Xz7fo5jn7VGwc7FNmcFOFBsDMG%2BpKhIsDdt6DkuiOmA8RcUpOpdmL%2FfX%2BhhVRr%2Bqvu3gv88WpHJSjHqQ9iK2n0T99112sLRUd22o%2FVSy3MOik97wGOqUBC5mzRud8PPJ2KKXJDbEmfpHcdNzodvBd0riTzYPxqXZ1LdcWveBX6MMzqmXOHtipxR6ciIDeOzQhBFJeXsv0nOX1lhg6ONe6eNLUDHH1X9zZ%2FGMDUy4Ka7pJipBp%2Bo1B3fIJyRKYDL6roo6gJuzeRmxROsF8KpqsE4ABVg4LOinIzRTCkOgu0yT4rIor1veP8RzdRVqOWk58eDkhaxhmZw2Cjj4w&X-Amz-Signature=4a0224895fd890f57d2251b5ab0d239bc26c0fbbc5b387595ecf3967b6daacbf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQYQWT6Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDW6zxytJXQLwQn3XhcFr7d5gp%2BkWllsO%2ByQVpFMAeeiAiEA7zZXrDpN2HYyf87VkAnShVAsBx6epnOdPdijftH8zHkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNMyjAFfQTA6Z3U%2FoCrcAxEUPyLzekDRftbFHNUlrz6FHNZgrt0QViC45Y4uz5GN6TmnfUNxbMasoo8vdKBg1V9GdkLf3NqjST4NRvq6z5qA1TBtuL6DDM1m2DvFXVv1rfKQe1jEpTnbSkt%2Fkr9lIVI60dthBU1wjBkR1gl%2FGKG%2F5GNw02kS1PzZo353b0syTDWaAxahQl19BSzG1bx4nRR1no5gzFd06nDk%2FrYmXmITmyc9AHcWn4jqHU3hoV3jlk2l3tUO%2FYJzpZwGTQ8UQDGuQAxYoK7%2B016nR1P60wpk0Kj4CU2hh%2BlZ4VDFfpBAbKUDB9lEEKH94rjo8S%2Bdk1kvoiTeL6z7OhRH1zCV7Ttlp5l%2FJK6Zw1M8qZ3jNZfyUSDPeEjFYLuOaK1yu6oPwly7njXU56Znw8v%2B93V0HXroikIon5mMTsUymjxuqWwyrUhyvQ%2Flo50y7SDl8cwtxmfqpsVrTdNQKzofB4HVEZQ3VJ58YlACivFIgQw499SONujLm9rWjhkw%2BRTPdyO5%2BDvd%2B63f5lElCM04Xf6Xz7fo5jn7VGwc7FNmcFOFBsDMG%2BpKhIsDdt6DkuiOmA8RcUpOpdmL%2FfX%2BhhVRr%2Bqvu3gv88WpHJSjHqQ9iK2n0T99112sLRUd22o%2FVSy3MOik97wGOqUBC5mzRud8PPJ2KKXJDbEmfpHcdNzodvBd0riTzYPxqXZ1LdcWveBX6MMzqmXOHtipxR6ciIDeOzQhBFJeXsv0nOX1lhg6ONe6eNLUDHH1X9zZ%2FGMDUy4Ka7pJipBp%2Bo1B3fIJyRKYDL6roo6gJuzeRmxROsF8KpqsE4ABVg4LOinIzRTCkOgu0yT4rIor1veP8RzdRVqOWk58eDkhaxhmZw2Cjj4w&X-Amz-Signature=7a686d2ff6834875b067fe3166dc4ef5b9e81d859701f96f5a6e10e4023ac162&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRSQZNEU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrTmqMhysKtbYmUxJBMDnA9vFxsOd1eDCKJtuZbkViIgIhAMgWsC4ubyXx%2B5IU%2Bmb6PiIqAFEmYwyHiEpkaL9JaKZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJqHyJykBjJkMPmQ0q3APs3ToV7cU%2B7RCqCpcPPVtlGfGsMYMqqvB3a%2FL5OOR5KzRKHrzPYiWDl0kyvfvMipehzkjnsfz3vwmfafJQWmjV8%2BkryJ8YFM73STzbqzxErus%2BQwfn66YWCJmPDniijdLCMBCCqvfdGCCNrJrbGzXoj8mzAAT158qMUZigundW3NJeeDNX0HI%2FyxfdPH36YCSPtk3vKVwSMx%2Fy0H7d5aXhgb0jBpGHuabMq6QobiW%2FaSUBEGZBmDZBpadCfUhpgxL7zt%2Bimz%2FyqFrA5LIqOyi06cEYyfyLadEEKNGPl4VfmTkinxJnAPyJwFcHuJry7cSrPpZH3gJ3OCPZyUB9uLKOyCcCWaug3EVXXArfhxNyWzjvxNNKjcLfNtV6%2BwwjtipbJZ%2B%2BBgp2IIRA5VLBxMr%2BcILfeqOE2poeiMsHjOwzOV5PSxeyRAKL5rVnallm8ylXjvbEjqvE7XOrDOwpcibd1iV%2BwPfvmfMgyUm0GrQQnPMd2LyPN8mCQJy23LXcLkIPXdDcNmU9T8rG%2F1%2FzLCuEbPbWIi0gbu%2FfFiGNsb1xFCfivTw6XjzMyh%2BhbW8JXhclXqxREh8ntZCN8%2B%2F2Q7sy6FcBUMybIhAHP%2BGScJHb6YQhH1Pa3i5HFo%2BzejD6pPe8BjqkAao47Dwab0icZKW0oN8OZH4AP8TFu%2BWt054ymwNPUXPoyEjQdf99elAqaaJlyhx%2FeuHa2or7mcHt812xSMyIXiSVf3QXiQZUkgsHPKQzX9wWGfJYr6D5bdcDAWWNDrzukKnGN382AXX4rRaHSchOvMM%2F8b5Lm3HBEqVBnaW2oGnpwFlrBb5gK8EanJhXxs1n3n%2BdL8qaqpbH5AXZlK9lVaRlXNLJ&X-Amz-Signature=5ae7d1946d9c391504c1b7bb87cf646a426313e52987b8e613d1df70586c4cfc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRSQZNEU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrTmqMhysKtbYmUxJBMDnA9vFxsOd1eDCKJtuZbkViIgIhAMgWsC4ubyXx%2B5IU%2Bmb6PiIqAFEmYwyHiEpkaL9JaKZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJqHyJykBjJkMPmQ0q3APs3ToV7cU%2B7RCqCpcPPVtlGfGsMYMqqvB3a%2FL5OOR5KzRKHrzPYiWDl0kyvfvMipehzkjnsfz3vwmfafJQWmjV8%2BkryJ8YFM73STzbqzxErus%2BQwfn66YWCJmPDniijdLCMBCCqvfdGCCNrJrbGzXoj8mzAAT158qMUZigundW3NJeeDNX0HI%2FyxfdPH36YCSPtk3vKVwSMx%2Fy0H7d5aXhgb0jBpGHuabMq6QobiW%2FaSUBEGZBmDZBpadCfUhpgxL7zt%2Bimz%2FyqFrA5LIqOyi06cEYyfyLadEEKNGPl4VfmTkinxJnAPyJwFcHuJry7cSrPpZH3gJ3OCPZyUB9uLKOyCcCWaug3EVXXArfhxNyWzjvxNNKjcLfNtV6%2BwwjtipbJZ%2B%2BBgp2IIRA5VLBxMr%2BcILfeqOE2poeiMsHjOwzOV5PSxeyRAKL5rVnallm8ylXjvbEjqvE7XOrDOwpcibd1iV%2BwPfvmfMgyUm0GrQQnPMd2LyPN8mCQJy23LXcLkIPXdDcNmU9T8rG%2F1%2FzLCuEbPbWIi0gbu%2FfFiGNsb1xFCfivTw6XjzMyh%2BhbW8JXhclXqxREh8ntZCN8%2B%2F2Q7sy6FcBUMybIhAHP%2BGScJHb6YQhH1Pa3i5HFo%2BzejD6pPe8BjqkAao47Dwab0icZKW0oN8OZH4AP8TFu%2BWt054ymwNPUXPoyEjQdf99elAqaaJlyhx%2FeuHa2or7mcHt812xSMyIXiSVf3QXiQZUkgsHPKQzX9wWGfJYr6D5bdcDAWWNDrzukKnGN382AXX4rRaHSchOvMM%2F8b5Lm3HBEqVBnaW2oGnpwFlrBb5gK8EanJhXxs1n3n%2BdL8qaqpbH5AXZlK9lVaRlXNLJ&X-Amz-Signature=b44b1d751a759d5eac8ace53e433f0747f30157e8cc0a9e4f26fc2664c3e091d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRSQZNEU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrTmqMhysKtbYmUxJBMDnA9vFxsOd1eDCKJtuZbkViIgIhAMgWsC4ubyXx%2B5IU%2Bmb6PiIqAFEmYwyHiEpkaL9JaKZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJqHyJykBjJkMPmQ0q3APs3ToV7cU%2B7RCqCpcPPVtlGfGsMYMqqvB3a%2FL5OOR5KzRKHrzPYiWDl0kyvfvMipehzkjnsfz3vwmfafJQWmjV8%2BkryJ8YFM73STzbqzxErus%2BQwfn66YWCJmPDniijdLCMBCCqvfdGCCNrJrbGzXoj8mzAAT158qMUZigundW3NJeeDNX0HI%2FyxfdPH36YCSPtk3vKVwSMx%2Fy0H7d5aXhgb0jBpGHuabMq6QobiW%2FaSUBEGZBmDZBpadCfUhpgxL7zt%2Bimz%2FyqFrA5LIqOyi06cEYyfyLadEEKNGPl4VfmTkinxJnAPyJwFcHuJry7cSrPpZH3gJ3OCPZyUB9uLKOyCcCWaug3EVXXArfhxNyWzjvxNNKjcLfNtV6%2BwwjtipbJZ%2B%2BBgp2IIRA5VLBxMr%2BcILfeqOE2poeiMsHjOwzOV5PSxeyRAKL5rVnallm8ylXjvbEjqvE7XOrDOwpcibd1iV%2BwPfvmfMgyUm0GrQQnPMd2LyPN8mCQJy23LXcLkIPXdDcNmU9T8rG%2F1%2FzLCuEbPbWIi0gbu%2FfFiGNsb1xFCfivTw6XjzMyh%2BhbW8JXhclXqxREh8ntZCN8%2B%2F2Q7sy6FcBUMybIhAHP%2BGScJHb6YQhH1Pa3i5HFo%2BzejD6pPe8BjqkAao47Dwab0icZKW0oN8OZH4AP8TFu%2BWt054ymwNPUXPoyEjQdf99elAqaaJlyhx%2FeuHa2or7mcHt812xSMyIXiSVf3QXiQZUkgsHPKQzX9wWGfJYr6D5bdcDAWWNDrzukKnGN382AXX4rRaHSchOvMM%2F8b5Lm3HBEqVBnaW2oGnpwFlrBb5gK8EanJhXxs1n3n%2BdL8qaqpbH5AXZlK9lVaRlXNLJ&X-Amz-Signature=797977e28870bd6b891529bb4408dbd00843463df3324d3ba21de3931a08f162&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRSQZNEU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrTmqMhysKtbYmUxJBMDnA9vFxsOd1eDCKJtuZbkViIgIhAMgWsC4ubyXx%2B5IU%2Bmb6PiIqAFEmYwyHiEpkaL9JaKZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJqHyJykBjJkMPmQ0q3APs3ToV7cU%2B7RCqCpcPPVtlGfGsMYMqqvB3a%2FL5OOR5KzRKHrzPYiWDl0kyvfvMipehzkjnsfz3vwmfafJQWmjV8%2BkryJ8YFM73STzbqzxErus%2BQwfn66YWCJmPDniijdLCMBCCqvfdGCCNrJrbGzXoj8mzAAT158qMUZigundW3NJeeDNX0HI%2FyxfdPH36YCSPtk3vKVwSMx%2Fy0H7d5aXhgb0jBpGHuabMq6QobiW%2FaSUBEGZBmDZBpadCfUhpgxL7zt%2Bimz%2FyqFrA5LIqOyi06cEYyfyLadEEKNGPl4VfmTkinxJnAPyJwFcHuJry7cSrPpZH3gJ3OCPZyUB9uLKOyCcCWaug3EVXXArfhxNyWzjvxNNKjcLfNtV6%2BwwjtipbJZ%2B%2BBgp2IIRA5VLBxMr%2BcILfeqOE2poeiMsHjOwzOV5PSxeyRAKL5rVnallm8ylXjvbEjqvE7XOrDOwpcibd1iV%2BwPfvmfMgyUm0GrQQnPMd2LyPN8mCQJy23LXcLkIPXdDcNmU9T8rG%2F1%2FzLCuEbPbWIi0gbu%2FfFiGNsb1xFCfivTw6XjzMyh%2BhbW8JXhclXqxREh8ntZCN8%2B%2F2Q7sy6FcBUMybIhAHP%2BGScJHb6YQhH1Pa3i5HFo%2BzejD6pPe8BjqkAao47Dwab0icZKW0oN8OZH4AP8TFu%2BWt054ymwNPUXPoyEjQdf99elAqaaJlyhx%2FeuHa2or7mcHt812xSMyIXiSVf3QXiQZUkgsHPKQzX9wWGfJYr6D5bdcDAWWNDrzukKnGN382AXX4rRaHSchOvMM%2F8b5Lm3HBEqVBnaW2oGnpwFlrBb5gK8EanJhXxs1n3n%2BdL8qaqpbH5AXZlK9lVaRlXNLJ&X-Amz-Signature=0264efbf45b0960fb54fc377c0a334691c5b40713a455517d644e0a765377035&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRSQZNEU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrTmqMhysKtbYmUxJBMDnA9vFxsOd1eDCKJtuZbkViIgIhAMgWsC4ubyXx%2B5IU%2Bmb6PiIqAFEmYwyHiEpkaL9JaKZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJqHyJykBjJkMPmQ0q3APs3ToV7cU%2B7RCqCpcPPVtlGfGsMYMqqvB3a%2FL5OOR5KzRKHrzPYiWDl0kyvfvMipehzkjnsfz3vwmfafJQWmjV8%2BkryJ8YFM73STzbqzxErus%2BQwfn66YWCJmPDniijdLCMBCCqvfdGCCNrJrbGzXoj8mzAAT158qMUZigundW3NJeeDNX0HI%2FyxfdPH36YCSPtk3vKVwSMx%2Fy0H7d5aXhgb0jBpGHuabMq6QobiW%2FaSUBEGZBmDZBpadCfUhpgxL7zt%2Bimz%2FyqFrA5LIqOyi06cEYyfyLadEEKNGPl4VfmTkinxJnAPyJwFcHuJry7cSrPpZH3gJ3OCPZyUB9uLKOyCcCWaug3EVXXArfhxNyWzjvxNNKjcLfNtV6%2BwwjtipbJZ%2B%2BBgp2IIRA5VLBxMr%2BcILfeqOE2poeiMsHjOwzOV5PSxeyRAKL5rVnallm8ylXjvbEjqvE7XOrDOwpcibd1iV%2BwPfvmfMgyUm0GrQQnPMd2LyPN8mCQJy23LXcLkIPXdDcNmU9T8rG%2F1%2FzLCuEbPbWIi0gbu%2FfFiGNsb1xFCfivTw6XjzMyh%2BhbW8JXhclXqxREh8ntZCN8%2B%2F2Q7sy6FcBUMybIhAHP%2BGScJHb6YQhH1Pa3i5HFo%2BzejD6pPe8BjqkAao47Dwab0icZKW0oN8OZH4AP8TFu%2BWt054ymwNPUXPoyEjQdf99elAqaaJlyhx%2FeuHa2or7mcHt812xSMyIXiSVf3QXiQZUkgsHPKQzX9wWGfJYr6D5bdcDAWWNDrzukKnGN382AXX4rRaHSchOvMM%2F8b5Lm3HBEqVBnaW2oGnpwFlrBb5gK8EanJhXxs1n3n%2BdL8qaqpbH5AXZlK9lVaRlXNLJ&X-Amz-Signature=9355dfbcb5ec0c73fd5adf761d8d7c17e2bc8dc5159210bda6dc66e1795708f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRSQZNEU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrTmqMhysKtbYmUxJBMDnA9vFxsOd1eDCKJtuZbkViIgIhAMgWsC4ubyXx%2B5IU%2Bmb6PiIqAFEmYwyHiEpkaL9JaKZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJqHyJykBjJkMPmQ0q3APs3ToV7cU%2B7RCqCpcPPVtlGfGsMYMqqvB3a%2FL5OOR5KzRKHrzPYiWDl0kyvfvMipehzkjnsfz3vwmfafJQWmjV8%2BkryJ8YFM73STzbqzxErus%2BQwfn66YWCJmPDniijdLCMBCCqvfdGCCNrJrbGzXoj8mzAAT158qMUZigundW3NJeeDNX0HI%2FyxfdPH36YCSPtk3vKVwSMx%2Fy0H7d5aXhgb0jBpGHuabMq6QobiW%2FaSUBEGZBmDZBpadCfUhpgxL7zt%2Bimz%2FyqFrA5LIqOyi06cEYyfyLadEEKNGPl4VfmTkinxJnAPyJwFcHuJry7cSrPpZH3gJ3OCPZyUB9uLKOyCcCWaug3EVXXArfhxNyWzjvxNNKjcLfNtV6%2BwwjtipbJZ%2B%2BBgp2IIRA5VLBxMr%2BcILfeqOE2poeiMsHjOwzOV5PSxeyRAKL5rVnallm8ylXjvbEjqvE7XOrDOwpcibd1iV%2BwPfvmfMgyUm0GrQQnPMd2LyPN8mCQJy23LXcLkIPXdDcNmU9T8rG%2F1%2FzLCuEbPbWIi0gbu%2FfFiGNsb1xFCfivTw6XjzMyh%2BhbW8JXhclXqxREh8ntZCN8%2B%2F2Q7sy6FcBUMybIhAHP%2BGScJHb6YQhH1Pa3i5HFo%2BzejD6pPe8BjqkAao47Dwab0icZKW0oN8OZH4AP8TFu%2BWt054ymwNPUXPoyEjQdf99elAqaaJlyhx%2FeuHa2or7mcHt812xSMyIXiSVf3QXiQZUkgsHPKQzX9wWGfJYr6D5bdcDAWWNDrzukKnGN382AXX4rRaHSchOvMM%2F8b5Lm3HBEqVBnaW2oGnpwFlrBb5gK8EanJhXxs1n3n%2BdL8qaqpbH5AXZlK9lVaRlXNLJ&X-Amz-Signature=2c408f6b98cf6481130edb0cb563477faf88c5fc9dc67427233998081ab67a40&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIR4CXQS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7hTCnnFhaccIrgn29B0ddz7AdPZkjL5Yx6NVVCdXQ3wIgKTh7x8ieCyOTRsqUDmA7c%2F4j%2BoMe4cLDv3UKcy60EB0qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC8TnpST%2Fk6jV1WuqSrcAzblezvSVZpBjc8cM6N%2Fc8Cpwd%2BzeP7enbqJHLV2eLThP%2BFYN6NIQzjfvMnEVC%2Ft8WFwiHMNzkh41D3D31BekMgfRWomPVvZxCDDySX7vjKaLHTZVQlApYJ73XuYxmCggrHs9ItNeA93RLD1RwtfJlonLVRtO9Q9%2FSlBWph3HvUy9oKQSA5BkG%2FRCju7FIcUMB52kE3lSZg%2F4duVr7o4J7NmlN5aXLEO2lOruDHsN5%2B3t6tWtq4wyimSVmzlRi1hABie%2FCh%2BP4FIhvIYPglh%2BVbRkJB%2FKQDgqjcjIoVdZH%2B9gnt%2FQ61sdtqf5Q2Qy0SGWqNjYkFmjXs4lWkxKWgUbdVag7X81U6gnlaCVm84oQz%2FXT8XEtztvUrFJeWgQIJNJrFL6heEf5%2Bem9qxqRSOHN58YCFckyQWb1ANGxfTnF6fT%2B1aBOVQIlusqJsHxsvHs4FbiuT93Vm%2BNhA9q3l6Dk2wQrZK2VZljQbfb7LHXvc3Ql6b2aLqDJadpEh7ZI75SY%2BCw8fYg88n%2FrcwrADx%2BCy9XV6y669%2Fa0wCCyqTmCJwxc%2FptMHgGba6QfzweU%2Feau4DulCdF43NDBGUD7%2FZiVgPQPclBa976SNfc0nzWo30NChZamBWUg%2B1fFssMLWk97wGOqUBgPbnF5jPJz0vc7RjINMxbksGKiciQvygN8anF29MrVfVPFD2HvoDDpwDIE%2FapGIFTAaCvOrL3TNDTBAH14N7gwP7sQeI1zHrywzbfOz9obta8jVMrZy7P4ssOE1ZMxsYRNy%2BaaJktZxBJKgKgQGM7Kr49slB2aKWh9gDPZU3pXn%2F08hjCFSKDFGx7ZfzNNy3%2FGjTdC1DIVV%2BTmYnRGkP9lCYVs10&X-Amz-Signature=35afc798c967ad639a4b90f29257a5b65e273bb4fcd1c0baca1f744c4ddd1e05&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMF5MYLX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEMVtJMz8689zK1ljpc%2BKSQirjfYcxdItyZvepg5iJRjAiEAuLS1F1XZuooxJfYoy4MBCU7he4nJhln%2BGF2cESIiXM8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMRbWG6k3lB%2FfsdekircA9fA6kQMchbS8D3MYpGZv3LORKcmMhISHIubsq5%2Fn1KrmxcIyfRbdyYthp8B3jNj3NMX6Evd6ERwYzzwNvJ1%2F4pSQjeUfZfi11R%2Fzc3MUzLGwOHn%2FSMEIJptkYPrys9DiLaHUvuuTUbx%2Fw6FWjOooHATVs6l9stlO2euYpQ0NFv5BJo3wBadVu%2BbK3qX0A5eqAJ%2Bd4buaT0I18YHFNQmvp%2Bz0MR7RxDHoPEEUwPFRn3l%2Fl7Skuqi%2FUB5cE5UXZFNh0EWr6XHZII2r5QthxgZThDq4JzKwvtX5psQs7hOgduNV3llLzncbb%2FsObvkK4InMlaxAdLGBWaofdAn9Tm8lih2XqL9rsiClsPRnr%2FHKtcx7I4%2BLqeJNKuf2IMg0R%2Bcou6pvBRYRHjQQKIyiQOb%2BPdULSh4WJUPya6ug%2FOnaun4QmTcayWd3jPcO9RjhkL3mpgjEjJrYpEkNAcq3RPjAS1FQp6rli1LgyLiG847t82Vrh0IG7G3UK9sJ7Jx8CIWZ3XIoef7i0%2FU01nhJVccA2jYYD6sHngwWjmXBtxPb%2F7ybaZwtc%2Fe7rxrWsAdpcyd%2FHniMQ6C7h4KS3OSuDx1w0Kb4U39pNI4lJhOwGKbi2du%2F8mpxPLX0Ynr8awJMNqk97wGOqUBRvkc8tGjJJCuDLbhrlrDppGnDsvVVEDnTNku0c%2F0wb1%2BXX2kvYbJhNmCwuVXK1nP8WG0B6EMYOSKW7gjp3o%2BCRvnIsZJ43zZ%2BstKQjr%2B%2FX1C4QoOFX95n6WlESOAJdWyY4wcqXw7hEOH%2BWAIYA35dYQbQFOuAvCpYHlykAlloZTDGjuvy3WxZLlLNg%2B2joSioBY1eCJ%2FXgo0Bfj6qKWyUel1AbEd&X-Amz-Signature=a705d63111619558212a715f693b3bd75b6e955b8bc0ced5ef008806e6b361a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRSQZNEU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrTmqMhysKtbYmUxJBMDnA9vFxsOd1eDCKJtuZbkViIgIhAMgWsC4ubyXx%2B5IU%2Bmb6PiIqAFEmYwyHiEpkaL9JaKZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJqHyJykBjJkMPmQ0q3APs3ToV7cU%2B7RCqCpcPPVtlGfGsMYMqqvB3a%2FL5OOR5KzRKHrzPYiWDl0kyvfvMipehzkjnsfz3vwmfafJQWmjV8%2BkryJ8YFM73STzbqzxErus%2BQwfn66YWCJmPDniijdLCMBCCqvfdGCCNrJrbGzXoj8mzAAT158qMUZigundW3NJeeDNX0HI%2FyxfdPH36YCSPtk3vKVwSMx%2Fy0H7d5aXhgb0jBpGHuabMq6QobiW%2FaSUBEGZBmDZBpadCfUhpgxL7zt%2Bimz%2FyqFrA5LIqOyi06cEYyfyLadEEKNGPl4VfmTkinxJnAPyJwFcHuJry7cSrPpZH3gJ3OCPZyUB9uLKOyCcCWaug3EVXXArfhxNyWzjvxNNKjcLfNtV6%2BwwjtipbJZ%2B%2BBgp2IIRA5VLBxMr%2BcILfeqOE2poeiMsHjOwzOV5PSxeyRAKL5rVnallm8ylXjvbEjqvE7XOrDOwpcibd1iV%2BwPfvmfMgyUm0GrQQnPMd2LyPN8mCQJy23LXcLkIPXdDcNmU9T8rG%2F1%2FzLCuEbPbWIi0gbu%2FfFiGNsb1xFCfivTw6XjzMyh%2BhbW8JXhclXqxREh8ntZCN8%2B%2F2Q7sy6FcBUMybIhAHP%2BGScJHb6YQhH1Pa3i5HFo%2BzejD6pPe8BjqkAao47Dwab0icZKW0oN8OZH4AP8TFu%2BWt054ymwNPUXPoyEjQdf99elAqaaJlyhx%2FeuHa2or7mcHt812xSMyIXiSVf3QXiQZUkgsHPKQzX9wWGfJYr6D5bdcDAWWNDrzukKnGN382AXX4rRaHSchOvMM%2F8b5Lm3HBEqVBnaW2oGnpwFlrBb5gK8EanJhXxs1n3n%2BdL8qaqpbH5AXZlK9lVaRlXNLJ&X-Amz-Signature=d53f355c78a35ae40058d252d064dcad81823fa1c63eaaf065392ca5470f85e7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRSQZNEU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrTmqMhysKtbYmUxJBMDnA9vFxsOd1eDCKJtuZbkViIgIhAMgWsC4ubyXx%2B5IU%2Bmb6PiIqAFEmYwyHiEpkaL9JaKZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJqHyJykBjJkMPmQ0q3APs3ToV7cU%2B7RCqCpcPPVtlGfGsMYMqqvB3a%2FL5OOR5KzRKHrzPYiWDl0kyvfvMipehzkjnsfz3vwmfafJQWmjV8%2BkryJ8YFM73STzbqzxErus%2BQwfn66YWCJmPDniijdLCMBCCqvfdGCCNrJrbGzXoj8mzAAT158qMUZigundW3NJeeDNX0HI%2FyxfdPH36YCSPtk3vKVwSMx%2Fy0H7d5aXhgb0jBpGHuabMq6QobiW%2FaSUBEGZBmDZBpadCfUhpgxL7zt%2Bimz%2FyqFrA5LIqOyi06cEYyfyLadEEKNGPl4VfmTkinxJnAPyJwFcHuJry7cSrPpZH3gJ3OCPZyUB9uLKOyCcCWaug3EVXXArfhxNyWzjvxNNKjcLfNtV6%2BwwjtipbJZ%2B%2BBgp2IIRA5VLBxMr%2BcILfeqOE2poeiMsHjOwzOV5PSxeyRAKL5rVnallm8ylXjvbEjqvE7XOrDOwpcibd1iV%2BwPfvmfMgyUm0GrQQnPMd2LyPN8mCQJy23LXcLkIPXdDcNmU9T8rG%2F1%2FzLCuEbPbWIi0gbu%2FfFiGNsb1xFCfivTw6XjzMyh%2BhbW8JXhclXqxREh8ntZCN8%2B%2F2Q7sy6FcBUMybIhAHP%2BGScJHb6YQhH1Pa3i5HFo%2BzejD6pPe8BjqkAao47Dwab0icZKW0oN8OZH4AP8TFu%2BWt054ymwNPUXPoyEjQdf99elAqaaJlyhx%2FeuHa2or7mcHt812xSMyIXiSVf3QXiQZUkgsHPKQzX9wWGfJYr6D5bdcDAWWNDrzukKnGN382AXX4rRaHSchOvMM%2F8b5Lm3HBEqVBnaW2oGnpwFlrBb5gK8EanJhXxs1n3n%2BdL8qaqpbH5AXZlK9lVaRlXNLJ&X-Amz-Signature=b1fb919ca302466a5b9572e6c1ba87f51ecf72c99321f2f49214350e49709204&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRSQZNEU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrTmqMhysKtbYmUxJBMDnA9vFxsOd1eDCKJtuZbkViIgIhAMgWsC4ubyXx%2B5IU%2Bmb6PiIqAFEmYwyHiEpkaL9JaKZdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJqHyJykBjJkMPmQ0q3APs3ToV7cU%2B7RCqCpcPPVtlGfGsMYMqqvB3a%2FL5OOR5KzRKHrzPYiWDl0kyvfvMipehzkjnsfz3vwmfafJQWmjV8%2BkryJ8YFM73STzbqzxErus%2BQwfn66YWCJmPDniijdLCMBCCqvfdGCCNrJrbGzXoj8mzAAT158qMUZigundW3NJeeDNX0HI%2FyxfdPH36YCSPtk3vKVwSMx%2Fy0H7d5aXhgb0jBpGHuabMq6QobiW%2FaSUBEGZBmDZBpadCfUhpgxL7zt%2Bimz%2FyqFrA5LIqOyi06cEYyfyLadEEKNGPl4VfmTkinxJnAPyJwFcHuJry7cSrPpZH3gJ3OCPZyUB9uLKOyCcCWaug3EVXXArfhxNyWzjvxNNKjcLfNtV6%2BwwjtipbJZ%2B%2BBgp2IIRA5VLBxMr%2BcILfeqOE2poeiMsHjOwzOV5PSxeyRAKL5rVnallm8ylXjvbEjqvE7XOrDOwpcibd1iV%2BwPfvmfMgyUm0GrQQnPMd2LyPN8mCQJy23LXcLkIPXdDcNmU9T8rG%2F1%2FzLCuEbPbWIi0gbu%2FfFiGNsb1xFCfivTw6XjzMyh%2BhbW8JXhclXqxREh8ntZCN8%2B%2F2Q7sy6FcBUMybIhAHP%2BGScJHb6YQhH1Pa3i5HFo%2BzejD6pPe8BjqkAao47Dwab0icZKW0oN8OZH4AP8TFu%2BWt054ymwNPUXPoyEjQdf99elAqaaJlyhx%2FeuHa2or7mcHt812xSMyIXiSVf3QXiQZUkgsHPKQzX9wWGfJYr6D5bdcDAWWNDrzukKnGN382AXX4rRaHSchOvMM%2F8b5Lm3HBEqVBnaW2oGnpwFlrBb5gK8EanJhXxs1n3n%2BdL8qaqpbH5AXZlK9lVaRlXNLJ&X-Amz-Signature=ccc30e326eb852c23ee2fb097f83acf608027f81ae3a54b17db290743ceea15e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLEVL7NX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGTKrK%2Bi%2F7JfPiiBBUmrGcAjnufvBM%2B3o%2BNpIOBXAOwBAiAm1xQwlUMjDauKEHik%2Fr2PBEeztp7HsmrHSNbIGVVbNCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMm5xCCnwiarJllxFeKtwDZsNc5RuoZmFvjznIefkLqMix0DE76tsBfNGBExtBtPTB1Dnk6I0BDxp0kqtz3YIT8dnNQB0xK8QXlGSGT0wekc0OOHN76FakLZ0dhpUTcEM%2Fa5K8x2r8U8Bfszq2exW%2FUMW25UfEczQWosxi2QxnhtcnEEhHckyEOQ1QJfJgYkJsx4%2F%2F1aByXF%2Bfob%2B0WVrLWsDZEhkOF%2BLJg3OdwNnC%2FSLafP%2B%2FS6sZN02FuHok7PlwbVyT2RVAkWQS70YgspzfCz8TXnKTWoQRspi4x6ZJIwnFE3mKJI8hV2KyMPP%2BPrAEgnXaBDRD2k%2BhUB659liRAUNDtWrcwxnVA%2FKtLSmtYlhc8T%2BGJDAJA6SDEusMaaNd%2B8KEBqHICT2hVnGcI9qNrUYP%2B0QP1z7fsJ36%2B2Or1fvwCKGZf4FbD2SukKtcovm0%2B9UL5Adh7i0yBIyUg28VYEMAYMW27EK%2BJdtmf63M0B0YjU4HimeIIL%2FYWzf6ikwPRukpeJLDdnZ%2BXtxdEYzSAMKNPLGcWrOKu7FK5TdiD0YDQc%2Fd2SzxNPDSu6XGfF81QR67r5b4d00ctHm%2B5gL4EVwDgjbCfqa3d%2FT6Rj5rXK8UwJpA3chf9s9uHEUnjSA1MtLjrqGwcGT4PewwwKT3vAY6pgEY8nXQUaG1Yl52RismQyJQwR%2BxTnuAxrzUFZDICm6t1b%2Fk3XHbpSSSsrx4TKU43t28tBtCZbpw%2B7xhiUk6ZrQyqEe8YH9mT%2F2InBmGIb3g%2FiOEPuGdshv1Jfk8NSj2m0yvAGTe6fxbF5AKvwf9hYTvZ1JXoWJsu2oHpq5%2FaRu0eAC%2BfpTXO1n171Y7oDrq%2B284x1p6ERCKuPuujE5GCux1%2Ft%2Fqhrdv&X-Amz-Signature=d4783423b9f862b30ed48d973bb6873cafe031fedf12e37e9509b1c3fda2487e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666I5RK3QU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbecw6OLBPvpOXN3pf6XwRS20136xOuimLrsUDlvecsAiEAp7Jyn%2FNmwYZJc7DAAXnkH2AzK27dbU48c8tI48poOiQqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGRdpw1KvQlEBcXXiSrcA8Ha2YdnjJhmrIpfrmCeCvYvB28JUTvOphDQ%2FXAFBSQ6KLyV79us9Sv41ZkkOqu8RN64jIq3lpsn5l1YN9zLutmw61GM0gvSdlk96JJyaGJkppQ%2FGYCy3QIdSWwifqrwDNzDuVOVOennZOLBiaRTS5RoodfCTZMOZNxPsGHTkHwqncF38WTGiqhTi4UGHUe3LQ3jZwfwfGeVsL6H%2FhaY9ir0t4AiOvIjGDIhikbFVJUulfHI057Spzk1lqhBQE4qs7yFVhu0mrloBCtUynqNGiPu8vxWzsu%2BVSEzDDs2tCVU6nJMvGogXkw96Mw58OS31dDXpQRcecYMNEYblIDcLO6K0KYj5z3dpqPGRTbdDtvVekr56%2BSoBQBjODtzYccOd1mbDzcHluTn0ykknTpBd7qDpJzADoH6AvtSIBTUfBf6Q1Kp6QXkOpVnheB5SJSepejw%2FUnvadskUx1%2F%2BIgleKXnGFJwDD9QH4u6iMCRFt%2BRZaPnT8fugw1mawTMxPSyxVtPThCiJXpHtQDK3ZFr2FUnzaY%2BnODZuj06lRXKuCnoz600Rkvdl9FiwTzfecJP0IrcwiV7O%2BnRSdq5DUqxc9qsyROwpug2y31pQk2hxmj1GrvkzRlCoY9ljvfZMMmk97wGOqUBCGtU99UqiXWjeHGIzYCUic3c%2BjZzI3%2FgzLGQXB5C7hyJ7aMaLcN63DNOeQLih7Suzig3MjjGVAWB3A5TngcZDuwFljkn8F7FLnEHd9k0Wl4LQ07C%2F79UkZtpTVM1YuJ56vOPMtAD%2FICf4FyJZAMgbnO%2B1L5GCSK5u7lZ0U3vba3pC%2Byg%2FUiOHpTYZbcV1nmHv444V%2BYgriycE%2FzE2yI4Bag68uHF&X-Amz-Signature=0b5f764ef2012d4741574fb931421aa1be5a664ce7a352aa65df642919ea4aa9&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLPYMMTD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAcTvv9US0s9PziV0yqir3Z99%2Bh9dCiNuVg4a90wI3ffAiA0WXsO8LvJcB7WXVOsEs8xYSjTtMw9DVDKLDN%2F7DXBTiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME9%2FoRvxLvZk%2FCx0tKtwD1YN4yps2QbAHxG7P1vGcZRYLULrRptluxP4Zjt%2FOUuDyxwcS3DL0bah%2BdO9jKKL6CV8FJNdIC1R2tRgyk9v42eBo%2F8kQQGOJo86PoKlu76H6fyztn1BORvXe6cVxFe1WepFS7cMFqVEH5gIBxh5qU%2FwiRpKJmTuU2fDg9vlLMB2VKKcl0BaFZS2ImiJwORErezbN%2Bm4CnyBptBA6TS5FYAK6VJ0r%2BcLtoSINnsJeh2xXc2ZRGHCtLjQI4gVqlIc24J3aWwoOJYCf0SF%2Fr8O7T0K3g6z4ZQ4Di09dLtVwOAq0UnjA1vig69l4TG70e2PbH9S5iX9v4QM9NXh5Xn8DZ4f%2BYB4IcfCrH971G1%2F1PLCmoMZdDaYPRwfv0tV6H4fAUSeEMTYAQ6VGEj4A0mfB5KbGFfI7E5NBg183G0uNDPbxAcJFTPkjt9IGTbJAzktyraYeUi24reYNIV94k%2BVmIBcabW0tAmcz22%2BTWTyFQlfeNbdin7n%2Bv8W3Z1aKPBYrCZfhfLusm65%2FqI0chPaOC3N3Jrxm%2FT5TaRl6kzA9t%2BTKtjDmt95RnG0ULkDZCWutY1Z%2BFdDGFxjlGoJetzQlJVLp5vqnjApYLJSZR6h%2FpCQC7QaFNtmjKdDchZQwtKT3vAY6pgFPM%2Fd9aprx0L9FSHrH0UGmn2dWXC1CydlbN%2FuvsMG%2FS13QfpR%2FJ70wfZ5b8xEozaw81B6KfHbKOicjX6XB3kQRWe3vLvyckkSPCr6LOn8JvLlO5%2BDapUdZVd%2BdLOYYCSkgJsbCD8fqE9F0j4z%2FiKv3WOhGWReIt6dDTCd0mvq3Mjh%2Fnwzkcv0IzalMnW5lxUIbPizJ3NL0RJCxFepZwB8fsZchJgeW&X-Amz-Signature=f2d22be479e32ea53e3ae8c090ee6e7e5a1ba992cdcc72f9b666ec4bed44bbe8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUN4YJJZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOIu%2Feli7rVSHqxr4RVDvqks7Ou8%2Bj4jQMUzmD%2BBz6agIhAKRTG0oof5rQidqtVgi4ZWQEioIQ%2Fq9gakfi269A9A8CKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwnC19mE2wUPPvM2Ikq3AN20u3sIJKiT5G5ighC%2FEOZxFHPwWvr39jNXoRSU1ND5vk%2FUC1VPfFYcwo3tlHgHeB15c7cJpviN78xIOCuRVxm8Hp701XzCG3w4LGjNCvND5rzFFTDEPe3PJRvM408i%2BGzpTpUTF%2Full6WU0SxdN1tqhoQ9FH1yomAWpHoqiFBhmuX3GwaW6Dv7YnXT8K8w96sn3HKZo7L3nNzF7MAKm9nmk3E4WN6pGZqd%2BA80aGeeR381GGtvWFuuqOfwlbl%2BR75SPLJ4110W7uwJa0Rao%2BcuQBvxYuPkQWXin2sfh3SfAt33aGQQJUg8tFcwLD05Kq5boS3Y50X0WVuCEIWj1PUY1gN83YPPGlsNjqmnH5JWxxCl6qgOIjQeHm0I1Bke%2BlFvENQkZ0PhOwg1cUtui2qwJuvS25pQil5%2FANOQ0ZeUHkgxYiQ9imf00bLipRnFNsPaH20e0aKFBjFRsBkQ3mRFx6QsTDt1z0Z2vJb98dZMghz3dCue%2BuqLUEp8WcSpLsl5mFSsagUG%2BG%2FMPOWBmBWaXtXy%2BjwG46JZ23coGwzapRPtCQ2iGXhQfdNbitxd0D2Ja4j%2FIDDZq1%2Bj%2F3sP987Po%2BVsuB8ei8PDrN6INtOIPsR%2B0T0RG5pBHQ5gzDJpPe8BjqkAYre8Bg5Zd148WWonooFNAJUmAB2LCqisTUAaXU%2Fhp7qwiDdAj2wEJNXJxj73M7axaXwm%2FOug9VqWasBqKUNel0fKzd9m1S6KE4A%2BTiYrfkkeG%2BADqkyul5O%2FwkbPG6UjiOggsn4cwPFhPSFGtxKoxMrVUw324CQMOZC5dgxkb6%2BnW1MTvPaKVihjl4%2BLsDGpdG3K9B1KUzTEp9MaJKzWWfXKlZP&X-Amz-Signature=7cde59346ed50f7bd60d39270a25c58abe156769500a1ff38542c0fc878fc5a0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUN4YJJZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOIu%2Feli7rVSHqxr4RVDvqks7Ou8%2Bj4jQMUzmD%2BBz6agIhAKRTG0oof5rQidqtVgi4ZWQEioIQ%2Fq9gakfi269A9A8CKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwnC19mE2wUPPvM2Ikq3AN20u3sIJKiT5G5ighC%2FEOZxFHPwWvr39jNXoRSU1ND5vk%2FUC1VPfFYcwo3tlHgHeB15c7cJpviN78xIOCuRVxm8Hp701XzCG3w4LGjNCvND5rzFFTDEPe3PJRvM408i%2BGzpTpUTF%2Full6WU0SxdN1tqhoQ9FH1yomAWpHoqiFBhmuX3GwaW6Dv7YnXT8K8w96sn3HKZo7L3nNzF7MAKm9nmk3E4WN6pGZqd%2BA80aGeeR381GGtvWFuuqOfwlbl%2BR75SPLJ4110W7uwJa0Rao%2BcuQBvxYuPkQWXin2sfh3SfAt33aGQQJUg8tFcwLD05Kq5boS3Y50X0WVuCEIWj1PUY1gN83YPPGlsNjqmnH5JWxxCl6qgOIjQeHm0I1Bke%2BlFvENQkZ0PhOwg1cUtui2qwJuvS25pQil5%2FANOQ0ZeUHkgxYiQ9imf00bLipRnFNsPaH20e0aKFBjFRsBkQ3mRFx6QsTDt1z0Z2vJb98dZMghz3dCue%2BuqLUEp8WcSpLsl5mFSsagUG%2BG%2FMPOWBmBWaXtXy%2BjwG46JZ23coGwzapRPtCQ2iGXhQfdNbitxd0D2Ja4j%2FIDDZq1%2Bj%2F3sP987Po%2BVsuB8ei8PDrN6INtOIPsR%2B0T0RG5pBHQ5gzDJpPe8BjqkAYre8Bg5Zd148WWonooFNAJUmAB2LCqisTUAaXU%2Fhp7qwiDdAj2wEJNXJxj73M7axaXwm%2FOug9VqWasBqKUNel0fKzd9m1S6KE4A%2BTiYrfkkeG%2BADqkyul5O%2FwkbPG6UjiOggsn4cwPFhPSFGtxKoxMrVUw324CQMOZC5dgxkb6%2BnW1MTvPaKVihjl4%2BLsDGpdG3K9B1KUzTEp9MaJKzWWfXKlZP&X-Amz-Signature=60d179198c3bea4234a07b908f2c3cd4f6af74715a883d217d9acc8d6754c0fb&X-Amz-SignedHeaders=host&x-id=GetObject)

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
