

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYWT72YZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJO4a%2FVi2WV%2B7nQTso%2BTpYsGuBbRWQlwnUXeM4ctCMOwIgal2ztyVHgDfYOynnedpEYcAT6zzHGRNSG3MaIkWEQ2MqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOKE%2BVdokBXPXxGi3CrcAyFT7agDCQIo1Lqg6kQ1krJJahUvbQ1MdHPjcfw0Wao5f%2BCcWSQPH5D4d4AnSpEKv2QcS5sfruZ7EJqnyU0c1l0JAhsB4IZPBNevdYURK9dhz3X0eko6WBSBH%2F8ZA%2B9HFilEBDrCUB4hWVukHg5KuNr7DwESBZoctrA0%2F1U20lc6k9LzO8KxPr%2FGJECJR838kdBQLPI6vYbY8MvfB1GtMWxN4zHY1mJVR5%2B05pDHTIckyrcORVkbht2sRYK%2B7UIc%2FkmpJ49VTc8ZK362bRqKOA81ZDMZlX9LuCugEC5unVVCnBmyHdjMUPlb3oZ6dzcEmgk%2F34cGcOkLP6vovi%2FSHqUSoy0MGg6LEEDHyl7FEMrhQw%2BbNNakRY1YKhIOv2r%2FTRUUgJ%2F0Cz1xHCm7aO5GIQ%2F1Ya83J0RLmdGuFOlN54Grd9AcrEKCrh8kNncFIWa73IsDOcGoWnT%2B7tCfAUel3p%2B%2FYcoPmZKghD6KfmROOgHu3QWvuwXJNs2XknX7L7LMY59116P56jYWJWviS56rHI38UlismpRtVdAkobqg7biceuyS1mQ7ost1dY%2BlO5ylqKcUMQT6TCYEK2%2FJx38CKMBR%2FjZIkvtP8MAnRpsMkJm%2BRjlqURvOb2H15xmnMIqc%2FLwGOqUB99eqp9ssoY2OGYqUfbzsJX51esFGERqteDDURmRvTMJYFMyu05bKbgKaXxR8D0I2kZ1M4vSyIJgK7GA%2BwbRPwZaE1RQcGphjXA8T46YT1W2W4HZC7kYQ0EgG9Df9K35OM3I%2BbpV8GPv%2F31mC%2B7n9MDk8Y49Qj0lsBjuYuDqSF2DdPvBiOEs%2By0Bwoi4ngoBW1Yjs0rDkwrCztnvpRV5MsarV4LHU&X-Amz-Signature=b3cb3c777678d5446e3aebb7cb2f31ff678f9c48f01d6443f37103d12fef2fca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYWT72YZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJO4a%2FVi2WV%2B7nQTso%2BTpYsGuBbRWQlwnUXeM4ctCMOwIgal2ztyVHgDfYOynnedpEYcAT6zzHGRNSG3MaIkWEQ2MqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOKE%2BVdokBXPXxGi3CrcAyFT7agDCQIo1Lqg6kQ1krJJahUvbQ1MdHPjcfw0Wao5f%2BCcWSQPH5D4d4AnSpEKv2QcS5sfruZ7EJqnyU0c1l0JAhsB4IZPBNevdYURK9dhz3X0eko6WBSBH%2F8ZA%2B9HFilEBDrCUB4hWVukHg5KuNr7DwESBZoctrA0%2F1U20lc6k9LzO8KxPr%2FGJECJR838kdBQLPI6vYbY8MvfB1GtMWxN4zHY1mJVR5%2B05pDHTIckyrcORVkbht2sRYK%2B7UIc%2FkmpJ49VTc8ZK362bRqKOA81ZDMZlX9LuCugEC5unVVCnBmyHdjMUPlb3oZ6dzcEmgk%2F34cGcOkLP6vovi%2FSHqUSoy0MGg6LEEDHyl7FEMrhQw%2BbNNakRY1YKhIOv2r%2FTRUUgJ%2F0Cz1xHCm7aO5GIQ%2F1Ya83J0RLmdGuFOlN54Grd9AcrEKCrh8kNncFIWa73IsDOcGoWnT%2B7tCfAUel3p%2B%2FYcoPmZKghD6KfmROOgHu3QWvuwXJNs2XknX7L7LMY59116P56jYWJWviS56rHI38UlismpRtVdAkobqg7biceuyS1mQ7ost1dY%2BlO5ylqKcUMQT6TCYEK2%2FJx38CKMBR%2FjZIkvtP8MAnRpsMkJm%2BRjlqURvOb2H15xmnMIqc%2FLwGOqUB99eqp9ssoY2OGYqUfbzsJX51esFGERqteDDURmRvTMJYFMyu05bKbgKaXxR8D0I2kZ1M4vSyIJgK7GA%2BwbRPwZaE1RQcGphjXA8T46YT1W2W4HZC7kYQ0EgG9Df9K35OM3I%2BbpV8GPv%2F31mC%2B7n9MDk8Y49Qj0lsBjuYuDqSF2DdPvBiOEs%2By0Bwoi4ngoBW1Yjs0rDkwrCztnvpRV5MsarV4LHU&X-Amz-Signature=a4c9fb5e22a82cad19617b31ea4cb4295672267bc1eaca8e9b9578b5efbaa2cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYWT72YZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJO4a%2FVi2WV%2B7nQTso%2BTpYsGuBbRWQlwnUXeM4ctCMOwIgal2ztyVHgDfYOynnedpEYcAT6zzHGRNSG3MaIkWEQ2MqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOKE%2BVdokBXPXxGi3CrcAyFT7agDCQIo1Lqg6kQ1krJJahUvbQ1MdHPjcfw0Wao5f%2BCcWSQPH5D4d4AnSpEKv2QcS5sfruZ7EJqnyU0c1l0JAhsB4IZPBNevdYURK9dhz3X0eko6WBSBH%2F8ZA%2B9HFilEBDrCUB4hWVukHg5KuNr7DwESBZoctrA0%2F1U20lc6k9LzO8KxPr%2FGJECJR838kdBQLPI6vYbY8MvfB1GtMWxN4zHY1mJVR5%2B05pDHTIckyrcORVkbht2sRYK%2B7UIc%2FkmpJ49VTc8ZK362bRqKOA81ZDMZlX9LuCugEC5unVVCnBmyHdjMUPlb3oZ6dzcEmgk%2F34cGcOkLP6vovi%2FSHqUSoy0MGg6LEEDHyl7FEMrhQw%2BbNNakRY1YKhIOv2r%2FTRUUgJ%2F0Cz1xHCm7aO5GIQ%2F1Ya83J0RLmdGuFOlN54Grd9AcrEKCrh8kNncFIWa73IsDOcGoWnT%2B7tCfAUel3p%2B%2FYcoPmZKghD6KfmROOgHu3QWvuwXJNs2XknX7L7LMY59116P56jYWJWviS56rHI38UlismpRtVdAkobqg7biceuyS1mQ7ost1dY%2BlO5ylqKcUMQT6TCYEK2%2FJx38CKMBR%2FjZIkvtP8MAnRpsMkJm%2BRjlqURvOb2H15xmnMIqc%2FLwGOqUB99eqp9ssoY2OGYqUfbzsJX51esFGERqteDDURmRvTMJYFMyu05bKbgKaXxR8D0I2kZ1M4vSyIJgK7GA%2BwbRPwZaE1RQcGphjXA8T46YT1W2W4HZC7kYQ0EgG9Df9K35OM3I%2BbpV8GPv%2F31mC%2B7n9MDk8Y49Qj0lsBjuYuDqSF2DdPvBiOEs%2By0Bwoi4ngoBW1Yjs0rDkwrCztnvpRV5MsarV4LHU&X-Amz-Signature=1f39f6ff71b32507856267458cd5155240bc7713b0ca9caaa02a204f7d89252f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPXUPNRE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHc7sBnRxak4RA%2FC05FwHKcfnqvsQSyu3%2FMISBen8uETAiEAmy3MZHwvx%2BEVlNy3EbuOO3eXCTTENwTMBspZJmlbekYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwtJDUtK%2FMsGdX4VCrcAxUVYG63sJM93QLoiUa7UzMnZLZAhpF0l%2B%2Fn0jtO8xdDMOqADmWQT%2FdHokHeuWCEKso4NGnV%2F0uE3ih2P4gxSuDKZ76ZuavoZWD%2FCpSDcCyusZUbCJgSM3Kdm5mbFj7OMCFeoTC0t%2Fn1TP%2BlKNyQJIrsduQxkXrBqZHWIS30jkEtoXTPUO9jlPPawmqfGBn2VshpMo%2BB0rXfwdiCHkEMW2iGPzOr8hQmfxi9yYTyA34c5DKZgItyoGep2PBamnDtVzCap98nC%2FA6aQgalwKfRNclX5InVmEoqMYU0QXmwyh9TNShMPVkfRT70gX2Hoc5jbHyaZHTeoT29MaRI9n9OLceoyItkBouAarmY3z7RQITzBQp%2BU%2FxRPNgp1iUH2YPElJEEzBDsXxjKxoVSoE9uBkhrrdFZLWHb0nc%2Fk3388%2FW8NOfaUlUzX1NFpas0QAC7Xz%2BF4NRwvZxVWfkU%2FGQiSxH06fmiBwFjoXnpmTmt2D%2Bcp5HzYTDBkQrTc%2FdC94EhCdX8vqiQzQFdf5idXTiBJmCbXjsPg%2B%2FUymYwMhouLVYE0dIuUbLm5eaTi7AARGl%2BHW7h7h9lPMgvVHZgAmWYeSfisNE9cuyRQG0G20Wtv2NUXQSrUQCQ8JTzIUSMKGc%2FLwGOqUB7s6ZDgLO3xRYDNqj4A9IkvHmd0EWwgNyV6Fkv%2BQND%2B2avAaaPindF92GGUaCMSkOwgQmFeQN6fwVeH%2FFxsj%2Fp0yTk8BUtnMgAVJRTeCCCJydEKHaLf7Nn3uB8OXgBNN345ySuyHmIbJOhz6vPuLDCJLa7txDlJwnokBnWefovqI%2Fs4%2FWKoI6MwMECqBDmJmsO7il4eb26eJbDAimYvOMVlOyc9rk&X-Amz-Signature=9e1c5d55f59bca0ea32399d596f982c273872b61cbe7016b9f4d114019f4b87b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPXUPNRE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHc7sBnRxak4RA%2FC05FwHKcfnqvsQSyu3%2FMISBen8uETAiEAmy3MZHwvx%2BEVlNy3EbuOO3eXCTTENwTMBspZJmlbekYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwtJDUtK%2FMsGdX4VCrcAxUVYG63sJM93QLoiUa7UzMnZLZAhpF0l%2B%2Fn0jtO8xdDMOqADmWQT%2FdHokHeuWCEKso4NGnV%2F0uE3ih2P4gxSuDKZ76ZuavoZWD%2FCpSDcCyusZUbCJgSM3Kdm5mbFj7OMCFeoTC0t%2Fn1TP%2BlKNyQJIrsduQxkXrBqZHWIS30jkEtoXTPUO9jlPPawmqfGBn2VshpMo%2BB0rXfwdiCHkEMW2iGPzOr8hQmfxi9yYTyA34c5DKZgItyoGep2PBamnDtVzCap98nC%2FA6aQgalwKfRNclX5InVmEoqMYU0QXmwyh9TNShMPVkfRT70gX2Hoc5jbHyaZHTeoT29MaRI9n9OLceoyItkBouAarmY3z7RQITzBQp%2BU%2FxRPNgp1iUH2YPElJEEzBDsXxjKxoVSoE9uBkhrrdFZLWHb0nc%2Fk3388%2FW8NOfaUlUzX1NFpas0QAC7Xz%2BF4NRwvZxVWfkU%2FGQiSxH06fmiBwFjoXnpmTmt2D%2Bcp5HzYTDBkQrTc%2FdC94EhCdX8vqiQzQFdf5idXTiBJmCbXjsPg%2B%2FUymYwMhouLVYE0dIuUbLm5eaTi7AARGl%2BHW7h7h9lPMgvVHZgAmWYeSfisNE9cuyRQG0G20Wtv2NUXQSrUQCQ8JTzIUSMKGc%2FLwGOqUB7s6ZDgLO3xRYDNqj4A9IkvHmd0EWwgNyV6Fkv%2BQND%2B2avAaaPindF92GGUaCMSkOwgQmFeQN6fwVeH%2FFxsj%2Fp0yTk8BUtnMgAVJRTeCCCJydEKHaLf7Nn3uB8OXgBNN345ySuyHmIbJOhz6vPuLDCJLa7txDlJwnokBnWefovqI%2Fs4%2FWKoI6MwMECqBDmJmsO7il4eb26eJbDAimYvOMVlOyc9rk&X-Amz-Signature=b5f837d7a0966e6a43a83daded63e1c8ddb183e3e82706f92a520d60cdf1a3a0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPXUPNRE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHc7sBnRxak4RA%2FC05FwHKcfnqvsQSyu3%2FMISBen8uETAiEAmy3MZHwvx%2BEVlNy3EbuOO3eXCTTENwTMBspZJmlbekYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwtJDUtK%2FMsGdX4VCrcAxUVYG63sJM93QLoiUa7UzMnZLZAhpF0l%2B%2Fn0jtO8xdDMOqADmWQT%2FdHokHeuWCEKso4NGnV%2F0uE3ih2P4gxSuDKZ76ZuavoZWD%2FCpSDcCyusZUbCJgSM3Kdm5mbFj7OMCFeoTC0t%2Fn1TP%2BlKNyQJIrsduQxkXrBqZHWIS30jkEtoXTPUO9jlPPawmqfGBn2VshpMo%2BB0rXfwdiCHkEMW2iGPzOr8hQmfxi9yYTyA34c5DKZgItyoGep2PBamnDtVzCap98nC%2FA6aQgalwKfRNclX5InVmEoqMYU0QXmwyh9TNShMPVkfRT70gX2Hoc5jbHyaZHTeoT29MaRI9n9OLceoyItkBouAarmY3z7RQITzBQp%2BU%2FxRPNgp1iUH2YPElJEEzBDsXxjKxoVSoE9uBkhrrdFZLWHb0nc%2Fk3388%2FW8NOfaUlUzX1NFpas0QAC7Xz%2BF4NRwvZxVWfkU%2FGQiSxH06fmiBwFjoXnpmTmt2D%2Bcp5HzYTDBkQrTc%2FdC94EhCdX8vqiQzQFdf5idXTiBJmCbXjsPg%2B%2FUymYwMhouLVYE0dIuUbLm5eaTi7AARGl%2BHW7h7h9lPMgvVHZgAmWYeSfisNE9cuyRQG0G20Wtv2NUXQSrUQCQ8JTzIUSMKGc%2FLwGOqUB7s6ZDgLO3xRYDNqj4A9IkvHmd0EWwgNyV6Fkv%2BQND%2B2avAaaPindF92GGUaCMSkOwgQmFeQN6fwVeH%2FFxsj%2Fp0yTk8BUtnMgAVJRTeCCCJydEKHaLf7Nn3uB8OXgBNN345ySuyHmIbJOhz6vPuLDCJLa7txDlJwnokBnWefovqI%2Fs4%2FWKoI6MwMECqBDmJmsO7il4eb26eJbDAimYvOMVlOyc9rk&X-Amz-Signature=d4420f91ffded7274191f8977926a2188848e9e6d325396435aa0a4980a98970&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPXUPNRE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHc7sBnRxak4RA%2FC05FwHKcfnqvsQSyu3%2FMISBen8uETAiEAmy3MZHwvx%2BEVlNy3EbuOO3eXCTTENwTMBspZJmlbekYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwtJDUtK%2FMsGdX4VCrcAxUVYG63sJM93QLoiUa7UzMnZLZAhpF0l%2B%2Fn0jtO8xdDMOqADmWQT%2FdHokHeuWCEKso4NGnV%2F0uE3ih2P4gxSuDKZ76ZuavoZWD%2FCpSDcCyusZUbCJgSM3Kdm5mbFj7OMCFeoTC0t%2Fn1TP%2BlKNyQJIrsduQxkXrBqZHWIS30jkEtoXTPUO9jlPPawmqfGBn2VshpMo%2BB0rXfwdiCHkEMW2iGPzOr8hQmfxi9yYTyA34c5DKZgItyoGep2PBamnDtVzCap98nC%2FA6aQgalwKfRNclX5InVmEoqMYU0QXmwyh9TNShMPVkfRT70gX2Hoc5jbHyaZHTeoT29MaRI9n9OLceoyItkBouAarmY3z7RQITzBQp%2BU%2FxRPNgp1iUH2YPElJEEzBDsXxjKxoVSoE9uBkhrrdFZLWHb0nc%2Fk3388%2FW8NOfaUlUzX1NFpas0QAC7Xz%2BF4NRwvZxVWfkU%2FGQiSxH06fmiBwFjoXnpmTmt2D%2Bcp5HzYTDBkQrTc%2FdC94EhCdX8vqiQzQFdf5idXTiBJmCbXjsPg%2B%2FUymYwMhouLVYE0dIuUbLm5eaTi7AARGl%2BHW7h7h9lPMgvVHZgAmWYeSfisNE9cuyRQG0G20Wtv2NUXQSrUQCQ8JTzIUSMKGc%2FLwGOqUB7s6ZDgLO3xRYDNqj4A9IkvHmd0EWwgNyV6Fkv%2BQND%2B2avAaaPindF92GGUaCMSkOwgQmFeQN6fwVeH%2FFxsj%2Fp0yTk8BUtnMgAVJRTeCCCJydEKHaLf7Nn3uB8OXgBNN345ySuyHmIbJOhz6vPuLDCJLa7txDlJwnokBnWefovqI%2Fs4%2FWKoI6MwMECqBDmJmsO7il4eb26eJbDAimYvOMVlOyc9rk&X-Amz-Signature=a7e53be7d1c06d6e5e42b21a51d428052177439bf56eb26cb4c3938195944676&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPXUPNRE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHc7sBnRxak4RA%2FC05FwHKcfnqvsQSyu3%2FMISBen8uETAiEAmy3MZHwvx%2BEVlNy3EbuOO3eXCTTENwTMBspZJmlbekYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwtJDUtK%2FMsGdX4VCrcAxUVYG63sJM93QLoiUa7UzMnZLZAhpF0l%2B%2Fn0jtO8xdDMOqADmWQT%2FdHokHeuWCEKso4NGnV%2F0uE3ih2P4gxSuDKZ76ZuavoZWD%2FCpSDcCyusZUbCJgSM3Kdm5mbFj7OMCFeoTC0t%2Fn1TP%2BlKNyQJIrsduQxkXrBqZHWIS30jkEtoXTPUO9jlPPawmqfGBn2VshpMo%2BB0rXfwdiCHkEMW2iGPzOr8hQmfxi9yYTyA34c5DKZgItyoGep2PBamnDtVzCap98nC%2FA6aQgalwKfRNclX5InVmEoqMYU0QXmwyh9TNShMPVkfRT70gX2Hoc5jbHyaZHTeoT29MaRI9n9OLceoyItkBouAarmY3z7RQITzBQp%2BU%2FxRPNgp1iUH2YPElJEEzBDsXxjKxoVSoE9uBkhrrdFZLWHb0nc%2Fk3388%2FW8NOfaUlUzX1NFpas0QAC7Xz%2BF4NRwvZxVWfkU%2FGQiSxH06fmiBwFjoXnpmTmt2D%2Bcp5HzYTDBkQrTc%2FdC94EhCdX8vqiQzQFdf5idXTiBJmCbXjsPg%2B%2FUymYwMhouLVYE0dIuUbLm5eaTi7AARGl%2BHW7h7h9lPMgvVHZgAmWYeSfisNE9cuyRQG0G20Wtv2NUXQSrUQCQ8JTzIUSMKGc%2FLwGOqUB7s6ZDgLO3xRYDNqj4A9IkvHmd0EWwgNyV6Fkv%2BQND%2B2avAaaPindF92GGUaCMSkOwgQmFeQN6fwVeH%2FFxsj%2Fp0yTk8BUtnMgAVJRTeCCCJydEKHaLf7Nn3uB8OXgBNN345ySuyHmIbJOhz6vPuLDCJLa7txDlJwnokBnWefovqI%2Fs4%2FWKoI6MwMECqBDmJmsO7il4eb26eJbDAimYvOMVlOyc9rk&X-Amz-Signature=9a04580bcfcf511b599f7e1a757eb11d30b1ef67642ef547cf90a411c029198e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPXUPNRE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHc7sBnRxak4RA%2FC05FwHKcfnqvsQSyu3%2FMISBen8uETAiEAmy3MZHwvx%2BEVlNy3EbuOO3eXCTTENwTMBspZJmlbekYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwtJDUtK%2FMsGdX4VCrcAxUVYG63sJM93QLoiUa7UzMnZLZAhpF0l%2B%2Fn0jtO8xdDMOqADmWQT%2FdHokHeuWCEKso4NGnV%2F0uE3ih2P4gxSuDKZ76ZuavoZWD%2FCpSDcCyusZUbCJgSM3Kdm5mbFj7OMCFeoTC0t%2Fn1TP%2BlKNyQJIrsduQxkXrBqZHWIS30jkEtoXTPUO9jlPPawmqfGBn2VshpMo%2BB0rXfwdiCHkEMW2iGPzOr8hQmfxi9yYTyA34c5DKZgItyoGep2PBamnDtVzCap98nC%2FA6aQgalwKfRNclX5InVmEoqMYU0QXmwyh9TNShMPVkfRT70gX2Hoc5jbHyaZHTeoT29MaRI9n9OLceoyItkBouAarmY3z7RQITzBQp%2BU%2FxRPNgp1iUH2YPElJEEzBDsXxjKxoVSoE9uBkhrrdFZLWHb0nc%2Fk3388%2FW8NOfaUlUzX1NFpas0QAC7Xz%2BF4NRwvZxVWfkU%2FGQiSxH06fmiBwFjoXnpmTmt2D%2Bcp5HzYTDBkQrTc%2FdC94EhCdX8vqiQzQFdf5idXTiBJmCbXjsPg%2B%2FUymYwMhouLVYE0dIuUbLm5eaTi7AARGl%2BHW7h7h9lPMgvVHZgAmWYeSfisNE9cuyRQG0G20Wtv2NUXQSrUQCQ8JTzIUSMKGc%2FLwGOqUB7s6ZDgLO3xRYDNqj4A9IkvHmd0EWwgNyV6Fkv%2BQND%2B2avAaaPindF92GGUaCMSkOwgQmFeQN6fwVeH%2FFxsj%2Fp0yTk8BUtnMgAVJRTeCCCJydEKHaLf7Nn3uB8OXgBNN345ySuyHmIbJOhz6vPuLDCJLa7txDlJwnokBnWefovqI%2Fs4%2FWKoI6MwMECqBDmJmsO7il4eb26eJbDAimYvOMVlOyc9rk&X-Amz-Signature=5070ed6ccbbf1ebb11f08343cce544ea7b3eaa116d92da2c3d20ab3e0430d652&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLMTL53D%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFYp%2BEzQetoOvtDwCVBnl9cW%2FWFs0Egqg9OAQIelDECAiBpWWiZEiCfMlCMCFj9zBp83B5a0Z81wuiB0OF1kRQnUSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUiJ3%2BiAgNj2lq6vLKtwDYQDAOTryJwLSIYmhMzYv%2F98FGj8fk1nxBMIxrsi%2BsAXteQlwTFt5ys0Z8Qlcp7zdQFTgdgPQKzSvzWNaLL2VHcbV%2Bu8JszCIJO0f9p6FR7KFPryFSD5Mk0NaUPanWKhwNPkIa17Z5kviot0IthPpH2o9cdFqic6J6tZhQTykWE8J4zfHztJ2eCMnb7%2FcBhPd%2FjVT4zs7OwiJk7QJdgUFSYqVzIWUeIgmLxy2zvCWQTCK7N2KNU7jg2R%2B375xSzNJtTpa1s0eGeaudz8LRzUPJUzg7Lj65s1Vrd0vWoOdAInV5MDfDdJFhoIY33kovUpQn2SnGth77Y%2BKg53jTldhf8DD4q3333w96pPyk0SF3T679bmlD2vgewWr78DuzJX%2F2rdkp3v9LMCRgd%2FlxPl6M6EPoDApgRO4uO01lf4yUygidDQWGccwypwoHq2duAzAP6xV0f0W%2FvPAXR02EPsOU%2BVWIb%2FvvWroEtgGyTVy3pwboZdH6P6hjYnmmAW7CObi2FIdSAGnI12eFykW6hKpGSZhc4thuOhPPKh9rG%2FMvRd4yMH0rSFOTUYLb7ZdhxVM8E7BlbxDS7z%2B7hqjEW1XoM76gcPeXNoyRr%2FE%2Fq0GwCoEmdgANTGFWOawUAMw%2BZv8vAY6pgE85fYlB5mt%2BfB%2BpK3VLGSdqaMl%2FGug9YEgqMPBeYtf2yEh5j%2FSITG01DWUXIp2qVkLBjB92dI1X3nWBIO3dBhVK2zh660X4ERbjNa%2FBsuWgPp0sUJITBaeNSQQX%2FqLaahPR8ADthuB36RBamvBi3%2FO48v7KMz%2F3ozpIMA5bwo9R4lJ19m7utOi0StTZtBufHjv5owhu7yZStumVq19WV3G9H7yWjCN&X-Amz-Signature=607917e1d6fb04ecf652242a5c28ef84691d812c69805f569787dc769a127fc3&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7UVPFPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDVmvCmkCa2j1l%2ByIBsR68zIZ48hI4D72jox%2BCIs2ELtAiEArpQFlC1bRGQWKQj2p0JOJ6%2BEYdQontLu6LI4OxtyhDEqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1Bb%2FOjH2svIfhJeyrcAwzlgVrA5dJSvsZnWd0ooWnYEI7RLN7%2FpaJ0WGff1odPYT6Z3tM%2Fs%2BH1XxYj1aRJYCcRu7uEs7zct4oapdo37pJXQI0Z4PID0tWTibSHf%2FGsKepWrg4lZ5NIMxjzH2e0EeX0Gh17oX%2BcCiunYFrv5mb4az%2BiMVYgLPskNkAeCk46iHUhKMdyfN8XJZnAZgVEL59OqpSEE4CJ1XdBvQdKKi0WTwWijsc1kUuiQnH7vtXQnqYVVc1zGX6gT9AtSjPU4Rf50cyRS8nSplhGkKF%2BB8WVh5tL87%2FHudhP9%2FQPCit%2FI6jzw59uahQ88u82Nw6tALNAY7lA5T9ITXYdPda1BfjmloYZv%2BffSGb%2FMe9V24fBSCHYNVFT7T1WpWZXUlGZ3iimxd58VCYMITkYafhOiyr9hiQhQKiyVLH71%2BQ5RYX6gGvdmdkH4%2Fod9hbYV0BeQ8TPau5oQTw%2FSf33YfBP%2BvaPBAYxizYfm9RKfLgCfT2ZmL9e3FVrTkE2OIF7ojlho%2BYeixBMPwUMVkZzsrLd%2BfXe41s%2FndIFMLiXAdfNhKxceBUIy6wMuoqWaGVIcCekp3%2FigNU7l59er4yKixrUG8oXsJ8MGy3BdsSzd9pkK2WC4vVtUjfzNNSjUJizMNac%2FLwGOqUBKc8o4M9hPvd3Qr51w1wfYVzBdlD5Hybfj9zNuogpsIsvWKsLIdSEeioiMj22TpBFO2eT5Ln8VCVxOmM6gl9Xml%2FgXyRPdBj5C0Dqiy3S58ZMGqpvZliv6HGPyrBeO%2FGC%2BCJOCLXZX8juu73LpYwMWLPI00n%2B09YZ19rLbcb69%2FbqM5CWpa1SkQqad%2FJtz3zw81YcrOzR94PGVuhhM6tmNEcYSTbF&X-Amz-Signature=1cd79c4a127c731c7a9390f4ea829aba03ca8239562271f8943c03def185674e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPXUPNRE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHc7sBnRxak4RA%2FC05FwHKcfnqvsQSyu3%2FMISBen8uETAiEAmy3MZHwvx%2BEVlNy3EbuOO3eXCTTENwTMBspZJmlbekYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwtJDUtK%2FMsGdX4VCrcAxUVYG63sJM93QLoiUa7UzMnZLZAhpF0l%2B%2Fn0jtO8xdDMOqADmWQT%2FdHokHeuWCEKso4NGnV%2F0uE3ih2P4gxSuDKZ76ZuavoZWD%2FCpSDcCyusZUbCJgSM3Kdm5mbFj7OMCFeoTC0t%2Fn1TP%2BlKNyQJIrsduQxkXrBqZHWIS30jkEtoXTPUO9jlPPawmqfGBn2VshpMo%2BB0rXfwdiCHkEMW2iGPzOr8hQmfxi9yYTyA34c5DKZgItyoGep2PBamnDtVzCap98nC%2FA6aQgalwKfRNclX5InVmEoqMYU0QXmwyh9TNShMPVkfRT70gX2Hoc5jbHyaZHTeoT29MaRI9n9OLceoyItkBouAarmY3z7RQITzBQp%2BU%2FxRPNgp1iUH2YPElJEEzBDsXxjKxoVSoE9uBkhrrdFZLWHb0nc%2Fk3388%2FW8NOfaUlUzX1NFpas0QAC7Xz%2BF4NRwvZxVWfkU%2FGQiSxH06fmiBwFjoXnpmTmt2D%2Bcp5HzYTDBkQrTc%2FdC94EhCdX8vqiQzQFdf5idXTiBJmCbXjsPg%2B%2FUymYwMhouLVYE0dIuUbLm5eaTi7AARGl%2BHW7h7h9lPMgvVHZgAmWYeSfisNE9cuyRQG0G20Wtv2NUXQSrUQCQ8JTzIUSMKGc%2FLwGOqUB7s6ZDgLO3xRYDNqj4A9IkvHmd0EWwgNyV6Fkv%2BQND%2B2avAaaPindF92GGUaCMSkOwgQmFeQN6fwVeH%2FFxsj%2Fp0yTk8BUtnMgAVJRTeCCCJydEKHaLf7Nn3uB8OXgBNN345ySuyHmIbJOhz6vPuLDCJLa7txDlJwnokBnWefovqI%2Fs4%2FWKoI6MwMECqBDmJmsO7il4eb26eJbDAimYvOMVlOyc9rk&X-Amz-Signature=cba05cf6ef15b0d01fd424c2374ec54b214a19a1f22c8ab8aee223c49b5a956a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPXUPNRE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHc7sBnRxak4RA%2FC05FwHKcfnqvsQSyu3%2FMISBen8uETAiEAmy3MZHwvx%2BEVlNy3EbuOO3eXCTTENwTMBspZJmlbekYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwtJDUtK%2FMsGdX4VCrcAxUVYG63sJM93QLoiUa7UzMnZLZAhpF0l%2B%2Fn0jtO8xdDMOqADmWQT%2FdHokHeuWCEKso4NGnV%2F0uE3ih2P4gxSuDKZ76ZuavoZWD%2FCpSDcCyusZUbCJgSM3Kdm5mbFj7OMCFeoTC0t%2Fn1TP%2BlKNyQJIrsduQxkXrBqZHWIS30jkEtoXTPUO9jlPPawmqfGBn2VshpMo%2BB0rXfwdiCHkEMW2iGPzOr8hQmfxi9yYTyA34c5DKZgItyoGep2PBamnDtVzCap98nC%2FA6aQgalwKfRNclX5InVmEoqMYU0QXmwyh9TNShMPVkfRT70gX2Hoc5jbHyaZHTeoT29MaRI9n9OLceoyItkBouAarmY3z7RQITzBQp%2BU%2FxRPNgp1iUH2YPElJEEzBDsXxjKxoVSoE9uBkhrrdFZLWHb0nc%2Fk3388%2FW8NOfaUlUzX1NFpas0QAC7Xz%2BF4NRwvZxVWfkU%2FGQiSxH06fmiBwFjoXnpmTmt2D%2Bcp5HzYTDBkQrTc%2FdC94EhCdX8vqiQzQFdf5idXTiBJmCbXjsPg%2B%2FUymYwMhouLVYE0dIuUbLm5eaTi7AARGl%2BHW7h7h9lPMgvVHZgAmWYeSfisNE9cuyRQG0G20Wtv2NUXQSrUQCQ8JTzIUSMKGc%2FLwGOqUB7s6ZDgLO3xRYDNqj4A9IkvHmd0EWwgNyV6Fkv%2BQND%2B2avAaaPindF92GGUaCMSkOwgQmFeQN6fwVeH%2FFxsj%2Fp0yTk8BUtnMgAVJRTeCCCJydEKHaLf7Nn3uB8OXgBNN345ySuyHmIbJOhz6vPuLDCJLa7txDlJwnokBnWefovqI%2Fs4%2FWKoI6MwMECqBDmJmsO7il4eb26eJbDAimYvOMVlOyc9rk&X-Amz-Signature=82693308d00ae8fa8915f0f2951d52bd624d3afb3e32094f5405f586dddc3d46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPXUPNRE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHc7sBnRxak4RA%2FC05FwHKcfnqvsQSyu3%2FMISBen8uETAiEAmy3MZHwvx%2BEVlNy3EbuOO3eXCTTENwTMBspZJmlbekYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwtJDUtK%2FMsGdX4VCrcAxUVYG63sJM93QLoiUa7UzMnZLZAhpF0l%2B%2Fn0jtO8xdDMOqADmWQT%2FdHokHeuWCEKso4NGnV%2F0uE3ih2P4gxSuDKZ76ZuavoZWD%2FCpSDcCyusZUbCJgSM3Kdm5mbFj7OMCFeoTC0t%2Fn1TP%2BlKNyQJIrsduQxkXrBqZHWIS30jkEtoXTPUO9jlPPawmqfGBn2VshpMo%2BB0rXfwdiCHkEMW2iGPzOr8hQmfxi9yYTyA34c5DKZgItyoGep2PBamnDtVzCap98nC%2FA6aQgalwKfRNclX5InVmEoqMYU0QXmwyh9TNShMPVkfRT70gX2Hoc5jbHyaZHTeoT29MaRI9n9OLceoyItkBouAarmY3z7RQITzBQp%2BU%2FxRPNgp1iUH2YPElJEEzBDsXxjKxoVSoE9uBkhrrdFZLWHb0nc%2Fk3388%2FW8NOfaUlUzX1NFpas0QAC7Xz%2BF4NRwvZxVWfkU%2FGQiSxH06fmiBwFjoXnpmTmt2D%2Bcp5HzYTDBkQrTc%2FdC94EhCdX8vqiQzQFdf5idXTiBJmCbXjsPg%2B%2FUymYwMhouLVYE0dIuUbLm5eaTi7AARGl%2BHW7h7h9lPMgvVHZgAmWYeSfisNE9cuyRQG0G20Wtv2NUXQSrUQCQ8JTzIUSMKGc%2FLwGOqUB7s6ZDgLO3xRYDNqj4A9IkvHmd0EWwgNyV6Fkv%2BQND%2B2avAaaPindF92GGUaCMSkOwgQmFeQN6fwVeH%2FFxsj%2Fp0yTk8BUtnMgAVJRTeCCCJydEKHaLf7Nn3uB8OXgBNN345ySuyHmIbJOhz6vPuLDCJLa7txDlJwnokBnWefovqI%2Fs4%2FWKoI6MwMECqBDmJmsO7il4eb26eJbDAimYvOMVlOyc9rk&X-Amz-Signature=a7c68055291c275347bfe5f2745f5a519ef3bccc105b8f86ad968a78c3d51f1c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR44G32A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlvcO4EjwvDTdQktvqp1oXmMjFG3%2BkVSaqm2Z5PQODZAiEAjeSybkHvi9deABSqxhfrn92ARnsJQ5kzzS8AOuYjLPUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLxLJPqL1%2FdgBE3%2BKSrcA0NenB7az9lMI%2FwMUteqGTqyAgj5oT4i8zOv4j8tFAOgU55PPQdmLaQud%2FR%2B2nKxcbg%2Bi4rAHygFkgYUP9kZ8%2BdYgUoGIFROlEs4eFzENDe8gv3D0EUrpuYwhwsLJelMuxEXG0u2HmL2e04%2F4rOPdn02ZULGMiANnBHwBrh%2B8xkxhfcLlMNRPoZQ2tCJ7PzlxWFha3rzqo25rseWkhpDB18WMb7u%2FEla4bZr6o3SeoxBLLVddCbLSR94jsAzA0MYfC%2FNlG2ZeDdVmelpZ9m79SM0Cvm%2BThOD3Cv0%2BFyopSn1%2FuMpigOtroqr7%2Fov4ktFzcgQr3J2hXjBlHE%2FHmuE74izTnjoklbSg4CUxV7uafq%2FZOkFZwftq7D2CvB88K5XCZrBpkifLus2J%2BSXJTrL%2FjYboomj%2BKYiMK16v0LoXZpKK4DsmZ2dw%2BDfoGc3833hHlaH5PN8ZMiTKuMw2D%2Fdqy4JOShScG7DCt%2FbYo2Gh2PWpK%2BFxgZyHqhXrVVoIO1rsq7cOqg9nXVqpmR4hdSFlEVEZ%2Fi1RZAzMPxaSdPMOIHsSi2cN57zIOXY8ySIVKLAghpjPJ23jii42ZD8247WzlA9KpcLTgqS6WmCKrML0AG6MpHMVSRQcvlSCZdDMPib%2FLwGOqUBLS5d0J%2F%2FOb8nEuOJw2ipl2kHMbvsU98db2aBAim0LiTTF83wz9Vtewi44SaV4lxex22hERQizu3%2F5E3U858Oth5my7uk7YcQRPAmeKFEuiC2er7WUvsWZy4eOY4a9Cu%2F2WDRZvUro%2FitF8s7XBZlE14u3V1HtP7u54ANziXPeW%2FqryR%2BHF4gjFYvuWjzVLjnrWab%2F3KD6qffgUqgS8c3g67g86Da&X-Amz-Signature=9b0ea6cec96f2b11e695d7ae73199fd8602c37ec453b5b2844099b46f017f3f4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KH3UVBA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdNhQWLLSUT6BhoVKvaKLMGQtxl%2B6TD9adA1zFb%2BhRQAIhAIR9WNVcjtsjxZh9z2opP0BBmLPwWylOWXoGxTHwujUDKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxSSxsxTtZGHIIZsEq3AOEUYWN8Q4cCKX4hAgWlN%2B18KyGomzmHUzocd%2BkJ5IUijoZVanNOfQAlYRNIvqRHyHyycK%2BW%2BYeCHZoSWPyndh65L5IjW51%2BPxxiuReMKa2iZ3TwDpPjsB6IxTMMrET1BYV6bv7%2BqfPFfKsJdBladtB7LRHaUVr6ZyJpvV5nqWZ8Zmim50oJOuc2ZGQ20aq7IgxhLQdxHEyX6ximQ%2FMzbrJMK19D10YGmD5iqn7hxsncRyieQ4eAPnD%2FJrl8JxOi7KVarQfOXsrs%2F5wmRsN4eCWtK4szTSOKmJkxv4M8Y%2Fwoodm6X1gtWc4IFLH34S4sVwg%2Ffpjimj39MlSVwWXc6u6M3JwxwVDgThPPqwzC3D%2Bvn9Ka3S2%2BZXQidoCpkJXxvzEakd4Z3PjqB%2B7xj9ZK497CVKrcTxoCZ2Y%2Bf9N5E25UWxdwOYL1WXB52tywA%2BBqhhN0pjWM%2FuaDN%2Bst%2FS66K0YYJEU43HORRYGDqpjE2B0gfvQNwAFR%2B74mbrnbGXy0jj8yT9zfEMtyczf6E1qw5KSKnDFPH7EQ2U1%2FYZdldiR4WAW7F%2BRw0GF32Z7TSGGkl3bZJy9YKymo37cHD39LJv1gozFFvU3xPo0orcClbi8GfP%2FYzLH%2BEh7VsApbDDgm%2Fy8BjqkAbj9uuln8fmATZ4ED34H3uzahR8VHuWWb3vATmhFYiE4mSmPn5HdJefQIDHCBHJ1Jw6kYB0Yfx%2F%2Brhi8bhFagzNXuM%2FXzVhly7H8S4fhi3gGnT1jflK%2FBZi4l4beJ9IIfOBeTRE5VwyMwuFiwdcQCzt%2F65QnSkXOYgyB2mVazt7Rv4ZYQLIa216ccqNDu%2FjRyH6sB3mOLPIOxd0wYflTRNO%2F2TG8&X-Amz-Signature=8ca1cb9a389ecf022592ea85d507c6e275be5b0853206d4ead8e41df679d37f6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SG3C6W6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqE6U9lOgRreF74Z7Nr27Kr8IF9zczg86g61gDFVMgEAIhANFjtrMjEC5d8mo3Xm1lwllnBNhY0SUIcOePGMxroY1fKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQFo23pA7U5heONusq3ANLPLmajIGjCUDjeghEIWi35xwKhVtoXFJSrl7Qck6r8pQW4FII%2B%2FA0dOHJpHowjqpEU%2BloUpYwTlNL6shDi49MbUReXzFqchz7ZakrBulIGUUZbJabZku67dLW5alrYdSq3CRihHkpelyufB7A%2FeypgE9dcw5zs6%2F3NoVA0EO779eW8FoDafPtioLPy6e1z%2FIKDsAwZhw8I%2FkSPM5CFsqxvxtN0kUhF0dqO1ohQkyDZZKteqXSoFdA1l90b%2BD0QbEI%2F7%2BZwaf56K0hv9slO2GrBDX91cOi2rwf6kuEokKKyIgsmvhDKBjxdLZ3yTxEJOLcZRCQ9WXgoIdSrPyXffuBuBqW4Br6G1ECctWv5oIe%2F6Ibb31cqqKyjvRELNNhqJy7unmuAgn4LPc2xlB%2B8ZmXmWfxiCUm0kxu0OE8zWvxXUCbfTpciRsqIMYbAVL%2F4iu4B%2FYzkSCmQ3LAoP47BQBeNJm1rgobBM%2Bw%2BTwCsf7U605vF%2FFkWT%2B4DO6PkbeVqJ4bLDM9ky24p%2Bk8PQiFYxpPl6%2Bwcb3xXaag7VKhoyQkflop7pWZrJz6hi637o%2F0Sd00MBFnM4ULT%2FKkKMsdcBFsvD8pZPY1Fb0ycP2Gq7gh05cPTFV%2Bssd17A%2FizTDTnPy8BjqkAY%2BF9J04IfumzScg9roGt3unJV1zqayLoBbSxYAOxRgk8r6YIdq7qioTCpJlF1j1vccXJ%2FoOyfw40Nf%2F6WWFZZPzkrNN4iITN193zW7gPAc%2FnmrWK57TWPl2UOw4%2BitahK0VDg99%2FL2q1JQf%2Fhqe6rI9Ri3NLCNPSFEEZx51jctPbgN8HiC3ya%2FFIBw4WW1JGW0nzaAu%2BmjKwAf5A1V1P5J17NxC&X-Amz-Signature=793a22a967789139789edc409d2f9c28396584c6d9f202e510a4afa83bd485bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVXZXZ6Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJxSnbJQzhi55CJNyE4ftcZRVzjUW1fU3bZKzLofNt4gIhAK0Sj8GWVDUOX19kRnHkngPXZBzkJuROj7vsIbPAn4gOKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLWJbQXvr1xcLFp9oq3ANeIwI36gMGucYwmhnUhLA0ZHT5jO6mJ4fAURRm2zlxPyMbg8kBpwPmJm59fFH48lvUmVg1TkamH%2BEVctxOExFctsGaElqEKCpYTTjNjE2Pr82NTRiJZtf1jjmlQ34qEC64ieSbPLefcKtsNlKa%2B1PKmpp%2BDYp6vX7UM5sJMbyFPfP0Oy%2B%2FyOpM%2BHTg%2BPDoF%2BhVWDvU2EBlgveJpYGHvukpLZiwHyrTxhAk5hpmTlsvkOOAsrjodeGUHz5eZ4nvRIJfPA%2B%2BjlyQ7cxKmdz4XA1QDHHODut3ERu6AWbaKO%2FZLIwDIcsJNNqJXwDpNUYZuYaK0O2xAE7crZvcagGD2kQ8xOeg50l0JuqYHsNEsx%2Fz4AiyHhyQos50wxlh2tZRnJgXw34LkqfP56IZWKx4NT%2FUshiavIm435kLlN5xwrkscvl%2FxMtiivv3p9Y6I7zHJcrRKXaiXYb5dC3i8O7b%2FR%2BCFKTKKgl%2BzFHhgrI%2FLL1W%2B%2BDVx4uuxkeIqJZAu3jNhHYEo7de5W6L2TKZKtK4d977gZJBuQPmWaBoqOIYRg1V7S4pnRASvUwcgmhvefSBr%2Bck7YnS1ID4UCxmwKP3VG2vVpJdB%2BV0oHrsHWAuE4t21AJLjc2vuxDiR%2BBgETCynPy8BjqkAVKV2pHyTT2aAipBRX%2Fxvyeprl%2BQwHwPCyAh3zstO57LL%2BveyJ6op5Bb5QlMohJMqZamBXU3ZOpbEBjWOV5hK8z7m9Kmc8u6ZAlXwleIqHz5PCXZ8dQnBvy28Cn9Ev9Fa1QT6BZnGCUjYx9YoTD1tHy8iLMIg50GGaT7PJV47giWVZoTKib38eCBWtRYzC8gFI0HR3OzTcZoqEIWvocjRIwo7X6T&X-Amz-Signature=a80a35a1344e9a3ac320141e3ebe579849d7e4bb8da66cdfe5e91c2421a10317&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVXZXZ6Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJxSnbJQzhi55CJNyE4ftcZRVzjUW1fU3bZKzLofNt4gIhAK0Sj8GWVDUOX19kRnHkngPXZBzkJuROj7vsIbPAn4gOKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLWJbQXvr1xcLFp9oq3ANeIwI36gMGucYwmhnUhLA0ZHT5jO6mJ4fAURRm2zlxPyMbg8kBpwPmJm59fFH48lvUmVg1TkamH%2BEVctxOExFctsGaElqEKCpYTTjNjE2Pr82NTRiJZtf1jjmlQ34qEC64ieSbPLefcKtsNlKa%2B1PKmpp%2BDYp6vX7UM5sJMbyFPfP0Oy%2B%2FyOpM%2BHTg%2BPDoF%2BhVWDvU2EBlgveJpYGHvukpLZiwHyrTxhAk5hpmTlsvkOOAsrjodeGUHz5eZ4nvRIJfPA%2B%2BjlyQ7cxKmdz4XA1QDHHODut3ERu6AWbaKO%2FZLIwDIcsJNNqJXwDpNUYZuYaK0O2xAE7crZvcagGD2kQ8xOeg50l0JuqYHsNEsx%2Fz4AiyHhyQos50wxlh2tZRnJgXw34LkqfP56IZWKx4NT%2FUshiavIm435kLlN5xwrkscvl%2FxMtiivv3p9Y6I7zHJcrRKXaiXYb5dC3i8O7b%2FR%2BCFKTKKgl%2BzFHhgrI%2FLL1W%2B%2BDVx4uuxkeIqJZAu3jNhHYEo7de5W6L2TKZKtK4d977gZJBuQPmWaBoqOIYRg1V7S4pnRASvUwcgmhvefSBr%2Bck7YnS1ID4UCxmwKP3VG2vVpJdB%2BV0oHrsHWAuE4t21AJLjc2vuxDiR%2BBgETCynPy8BjqkAVKV2pHyTT2aAipBRX%2Fxvyeprl%2BQwHwPCyAh3zstO57LL%2BveyJ6op5Bb5QlMohJMqZamBXU3ZOpbEBjWOV5hK8z7m9Kmc8u6ZAlXwleIqHz5PCXZ8dQnBvy28Cn9Ev9Fa1QT6BZnGCUjYx9YoTD1tHy8iLMIg50GGaT7PJV47giWVZoTKib38eCBWtRYzC8gFI0HR3OzTcZoqEIWvocjRIwo7X6T&X-Amz-Signature=b0d6d1203144c84f01902d27717f4b886f6cf49d74eb52736665e07f5b8cbf25&X-Amz-SignedHeaders=host&x-id=GetObject)

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
