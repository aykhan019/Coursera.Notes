

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7RC6VZQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBmBmrYKXjUPPxAJ2UDyO%2FgWz2WsJJ0HirbhN8x2UHN8AiEA4z3lj0yL%2Bz%2BHFsocGZrRk%2B5ucG6I6cqBLXsgyyw23Ooq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDAw9F0edM4nJwidGzyrcAxnvNoZAHr4kRBcTaEjZeLx2T%2BKteJgJE%2Batvq5iKUg15GzNaV0zZ%2F7o38qj8dcLU6rRkWgzi6zxYi6%2B32AibM0pKnU6JoDimNwFS7q1HMy6JoFQkKY2p4wc2cvV%2B4UyxHrpxGmlKTQb2OnE2HZ%2BpXYEH0Lzw8qe0OwEOGdA3v%2B6N1tFjhB67isTXRI5F0MoH%2B5QpoQZrHFJ2S6b18xyTkDgLO01ObmwLgejbOPQjB6cDqfUpoKuhbseLjOJyJg6x8r01TOHDZszNc6cwmAwdcF8x3oFEFxX7CFquRYUYijwPveUPTnH2wrAuEluAAFfGhTjMRXLGNzHENKQP%2B%2FPD9Oodz74AgZfVYdb8n26tHy4EV54dRGIJN0rldOxShK7RL9PxdvEdJ1wLS3G%2B7Vv6Z80SEF7uSOaRBiFV0LTQiwmX8Uf4TknGm7vhL44CW7JltM8hTMhzlQBvw7pNCSmeV%2FuCo0aP45jktKwN9THIVP3%2Fc%2FQFa28aiCLIwSLK8Lfifknb7lW69gXy7QfWXDZgLKepV3Zo2BJwNfJgOwdL5aHl0iJHu4FLmrLAC986RhvzJy4JzgwN8XsUQzLgOdxf1whnnJdH9Q1Z3XxDmxHUpUWuonCbmJTElb3koXGMInEmL0GOqUBL5pjXpzs1%2BfayS%2Fm99f%2BtCsc%2F6s4nsdUJ9u1b0384czXUB9joVaye3kQ7dyjkTyJ1VYu3PqxY2xifIqhqVmnNVKEjny5jcOiHBelVWt87nLOTSadTJlU%2Bd6baj69xdl895UQRFFStQQ9xm5cTVeHLKNiv%2BcJD0msuYd6On5LFM4MOka3aK%2FsVLbdawYTChv9VRukcE5Ekedyu6aefs303VNxZL35&X-Amz-Signature=b678c42eb5f71ff16a3c03e5b477f1cd52a36274ae31224fc93f23ffd5c87aa4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7RC6VZQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBmBmrYKXjUPPxAJ2UDyO%2FgWz2WsJJ0HirbhN8x2UHN8AiEA4z3lj0yL%2Bz%2BHFsocGZrRk%2B5ucG6I6cqBLXsgyyw23Ooq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDAw9F0edM4nJwidGzyrcAxnvNoZAHr4kRBcTaEjZeLx2T%2BKteJgJE%2Batvq5iKUg15GzNaV0zZ%2F7o38qj8dcLU6rRkWgzi6zxYi6%2B32AibM0pKnU6JoDimNwFS7q1HMy6JoFQkKY2p4wc2cvV%2B4UyxHrpxGmlKTQb2OnE2HZ%2BpXYEH0Lzw8qe0OwEOGdA3v%2B6N1tFjhB67isTXRI5F0MoH%2B5QpoQZrHFJ2S6b18xyTkDgLO01ObmwLgejbOPQjB6cDqfUpoKuhbseLjOJyJg6x8r01TOHDZszNc6cwmAwdcF8x3oFEFxX7CFquRYUYijwPveUPTnH2wrAuEluAAFfGhTjMRXLGNzHENKQP%2B%2FPD9Oodz74AgZfVYdb8n26tHy4EV54dRGIJN0rldOxShK7RL9PxdvEdJ1wLS3G%2B7Vv6Z80SEF7uSOaRBiFV0LTQiwmX8Uf4TknGm7vhL44CW7JltM8hTMhzlQBvw7pNCSmeV%2FuCo0aP45jktKwN9THIVP3%2Fc%2FQFa28aiCLIwSLK8Lfifknb7lW69gXy7QfWXDZgLKepV3Zo2BJwNfJgOwdL5aHl0iJHu4FLmrLAC986RhvzJy4JzgwN8XsUQzLgOdxf1whnnJdH9Q1Z3XxDmxHUpUWuonCbmJTElb3koXGMInEmL0GOqUBL5pjXpzs1%2BfayS%2Fm99f%2BtCsc%2F6s4nsdUJ9u1b0384czXUB9joVaye3kQ7dyjkTyJ1VYu3PqxY2xifIqhqVmnNVKEjny5jcOiHBelVWt87nLOTSadTJlU%2Bd6baj69xdl895UQRFFStQQ9xm5cTVeHLKNiv%2BcJD0msuYd6On5LFM4MOka3aK%2FsVLbdawYTChv9VRukcE5Ekedyu6aefs303VNxZL35&X-Amz-Signature=791d511ef20e3072b65682cb0a5cce6283d8c04a8512d1c8cbae09ca2f38ccde&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7RC6VZQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBmBmrYKXjUPPxAJ2UDyO%2FgWz2WsJJ0HirbhN8x2UHN8AiEA4z3lj0yL%2Bz%2BHFsocGZrRk%2B5ucG6I6cqBLXsgyyw23Ooq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDAw9F0edM4nJwidGzyrcAxnvNoZAHr4kRBcTaEjZeLx2T%2BKteJgJE%2Batvq5iKUg15GzNaV0zZ%2F7o38qj8dcLU6rRkWgzi6zxYi6%2B32AibM0pKnU6JoDimNwFS7q1HMy6JoFQkKY2p4wc2cvV%2B4UyxHrpxGmlKTQb2OnE2HZ%2BpXYEH0Lzw8qe0OwEOGdA3v%2B6N1tFjhB67isTXRI5F0MoH%2B5QpoQZrHFJ2S6b18xyTkDgLO01ObmwLgejbOPQjB6cDqfUpoKuhbseLjOJyJg6x8r01TOHDZszNc6cwmAwdcF8x3oFEFxX7CFquRYUYijwPveUPTnH2wrAuEluAAFfGhTjMRXLGNzHENKQP%2B%2FPD9Oodz74AgZfVYdb8n26tHy4EV54dRGIJN0rldOxShK7RL9PxdvEdJ1wLS3G%2B7Vv6Z80SEF7uSOaRBiFV0LTQiwmX8Uf4TknGm7vhL44CW7JltM8hTMhzlQBvw7pNCSmeV%2FuCo0aP45jktKwN9THIVP3%2Fc%2FQFa28aiCLIwSLK8Lfifknb7lW69gXy7QfWXDZgLKepV3Zo2BJwNfJgOwdL5aHl0iJHu4FLmrLAC986RhvzJy4JzgwN8XsUQzLgOdxf1whnnJdH9Q1Z3XxDmxHUpUWuonCbmJTElb3koXGMInEmL0GOqUBL5pjXpzs1%2BfayS%2Fm99f%2BtCsc%2F6s4nsdUJ9u1b0384czXUB9joVaye3kQ7dyjkTyJ1VYu3PqxY2xifIqhqVmnNVKEjny5jcOiHBelVWt87nLOTSadTJlU%2Bd6baj69xdl895UQRFFStQQ9xm5cTVeHLKNiv%2BcJD0msuYd6On5LFM4MOka3aK%2FsVLbdawYTChv9VRukcE5Ekedyu6aefs303VNxZL35&X-Amz-Signature=a74fb964d190b272ba2b3cd26e3c99a56a39866b56d09ddc58cd0200a515672d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577Y6RUM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIH5PAiB%2BMNFyLHyxXvnc13wcPvKxrDnhPUsGyq%2BiAfpMAiEA6PzZEWWOokFWJPe7DGZ13KgLNADIqYXvOWV%2B8OwuOkgq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDGyqB2I9vmKGMzYMuSrcA%2FaspPoaIgtc7pOkgGuDsGMPDaJiqddSbcc1yPxvtRwR2ZmRl%2BudviDUiAVygqbYtZm1JhhBr7bPETrwxdyhhs6NwXPuvp%2FR%2FIqm6u7CLdSdkzXc5xhB5XjT6%2B9Ftry%2BC2UHyln0mVI5LEu3qr2v8MGChHVqVMESIk1eNmSGOKj7uZpkQjzm7RXqTos3rD9jvXMPj1tVuQ7EEo1bwKEHUC13j64a7drSj0qlpJldlqOGoZzVbvjnVduqnHbJ%2B0MmtDTEI7xvAcl%2BJFlLyi1HMvdnGMObyVRavulmKa422QAZm4CNhdFgk6VH0nWqkAXsd0vKM%2BbkdlkQVkbOks43jPK9qmW2HFhslBinm%2BxnG3ti713wy7%2BWDeGnmu5AxWwG0t1Wx2p04znr4h7QxvDNqroGwYy5OgUH5%2BR9IlZBHd6Yo6CuJjNNITSx0PcXluDDV%2BX8tMgqW3nSEE8OptkIkkKkNvBXAxzQqks0SpEyc7DXGX4MxdPfBdD7KytEoVcNygZlt7pSbEq0X6H7tFQxrFy3uOQWBR%2Bk8lOXtiQkUpUBpC6SeHyZ9kkDbgldLXsYnBW5TFixT9qXiK9i7sikGAI4ANYoblQTuaI3IYH8KSCyZdz%2BZxOwfOBIfJHtMNzDmL0GOqUBGi0Fw3HcXSdFcRMH%2Bg2ESC4ogXs%2F59HQi6Raf1psFoodKz%2Ft91ZcMR7ggi%2Bm%2FIitMkdsYKiU2YVISd1TfupWCMZLACePG3XNk6iw8zFktukRgcJqZMsjpIbSXrx66sEF3bXRF0PhuuJdrsHRfLRiki3ctvYbgKRtgClQSCz6OSMqwbz2JqESkfhvWl4OK7C6Xp8B5bt2foLe5%2FKNqjZH3rBk3KSs&X-Amz-Signature=285c7df23429f44e15a1535f22565735a1b2e0702a84185826abf7ddc7fa74a3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577Y6RUM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIH5PAiB%2BMNFyLHyxXvnc13wcPvKxrDnhPUsGyq%2BiAfpMAiEA6PzZEWWOokFWJPe7DGZ13KgLNADIqYXvOWV%2B8OwuOkgq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDGyqB2I9vmKGMzYMuSrcA%2FaspPoaIgtc7pOkgGuDsGMPDaJiqddSbcc1yPxvtRwR2ZmRl%2BudviDUiAVygqbYtZm1JhhBr7bPETrwxdyhhs6NwXPuvp%2FR%2FIqm6u7CLdSdkzXc5xhB5XjT6%2B9Ftry%2BC2UHyln0mVI5LEu3qr2v8MGChHVqVMESIk1eNmSGOKj7uZpkQjzm7RXqTos3rD9jvXMPj1tVuQ7EEo1bwKEHUC13j64a7drSj0qlpJldlqOGoZzVbvjnVduqnHbJ%2B0MmtDTEI7xvAcl%2BJFlLyi1HMvdnGMObyVRavulmKa422QAZm4CNhdFgk6VH0nWqkAXsd0vKM%2BbkdlkQVkbOks43jPK9qmW2HFhslBinm%2BxnG3ti713wy7%2BWDeGnmu5AxWwG0t1Wx2p04znr4h7QxvDNqroGwYy5OgUH5%2BR9IlZBHd6Yo6CuJjNNITSx0PcXluDDV%2BX8tMgqW3nSEE8OptkIkkKkNvBXAxzQqks0SpEyc7DXGX4MxdPfBdD7KytEoVcNygZlt7pSbEq0X6H7tFQxrFy3uOQWBR%2Bk8lOXtiQkUpUBpC6SeHyZ9kkDbgldLXsYnBW5TFixT9qXiK9i7sikGAI4ANYoblQTuaI3IYH8KSCyZdz%2BZxOwfOBIfJHtMNzDmL0GOqUBGi0Fw3HcXSdFcRMH%2Bg2ESC4ogXs%2F59HQi6Raf1psFoodKz%2Ft91ZcMR7ggi%2Bm%2FIitMkdsYKiU2YVISd1TfupWCMZLACePG3XNk6iw8zFktukRgcJqZMsjpIbSXrx66sEF3bXRF0PhuuJdrsHRfLRiki3ctvYbgKRtgClQSCz6OSMqwbz2JqESkfhvWl4OK7C6Xp8B5bt2foLe5%2FKNqjZH3rBk3KSs&X-Amz-Signature=b6118d65c3b298fe4494923d75214b6c81edd4341b4ddf49913435bbf2341eb0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577Y6RUM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIH5PAiB%2BMNFyLHyxXvnc13wcPvKxrDnhPUsGyq%2BiAfpMAiEA6PzZEWWOokFWJPe7DGZ13KgLNADIqYXvOWV%2B8OwuOkgq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDGyqB2I9vmKGMzYMuSrcA%2FaspPoaIgtc7pOkgGuDsGMPDaJiqddSbcc1yPxvtRwR2ZmRl%2BudviDUiAVygqbYtZm1JhhBr7bPETrwxdyhhs6NwXPuvp%2FR%2FIqm6u7CLdSdkzXc5xhB5XjT6%2B9Ftry%2BC2UHyln0mVI5LEu3qr2v8MGChHVqVMESIk1eNmSGOKj7uZpkQjzm7RXqTos3rD9jvXMPj1tVuQ7EEo1bwKEHUC13j64a7drSj0qlpJldlqOGoZzVbvjnVduqnHbJ%2B0MmtDTEI7xvAcl%2BJFlLyi1HMvdnGMObyVRavulmKa422QAZm4CNhdFgk6VH0nWqkAXsd0vKM%2BbkdlkQVkbOks43jPK9qmW2HFhslBinm%2BxnG3ti713wy7%2BWDeGnmu5AxWwG0t1Wx2p04znr4h7QxvDNqroGwYy5OgUH5%2BR9IlZBHd6Yo6CuJjNNITSx0PcXluDDV%2BX8tMgqW3nSEE8OptkIkkKkNvBXAxzQqks0SpEyc7DXGX4MxdPfBdD7KytEoVcNygZlt7pSbEq0X6H7tFQxrFy3uOQWBR%2Bk8lOXtiQkUpUBpC6SeHyZ9kkDbgldLXsYnBW5TFixT9qXiK9i7sikGAI4ANYoblQTuaI3IYH8KSCyZdz%2BZxOwfOBIfJHtMNzDmL0GOqUBGi0Fw3HcXSdFcRMH%2Bg2ESC4ogXs%2F59HQi6Raf1psFoodKz%2Ft91ZcMR7ggi%2Bm%2FIitMkdsYKiU2YVISd1TfupWCMZLACePG3XNk6iw8zFktukRgcJqZMsjpIbSXrx66sEF3bXRF0PhuuJdrsHRfLRiki3ctvYbgKRtgClQSCz6OSMqwbz2JqESkfhvWl4OK7C6Xp8B5bt2foLe5%2FKNqjZH3rBk3KSs&X-Amz-Signature=129ff26b0b221412ea576b1d9cf00c871d72e311ccbb9cf1e88a7915cde2d492&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577Y6RUM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIH5PAiB%2BMNFyLHyxXvnc13wcPvKxrDnhPUsGyq%2BiAfpMAiEA6PzZEWWOokFWJPe7DGZ13KgLNADIqYXvOWV%2B8OwuOkgq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDGyqB2I9vmKGMzYMuSrcA%2FaspPoaIgtc7pOkgGuDsGMPDaJiqddSbcc1yPxvtRwR2ZmRl%2BudviDUiAVygqbYtZm1JhhBr7bPETrwxdyhhs6NwXPuvp%2FR%2FIqm6u7CLdSdkzXc5xhB5XjT6%2B9Ftry%2BC2UHyln0mVI5LEu3qr2v8MGChHVqVMESIk1eNmSGOKj7uZpkQjzm7RXqTos3rD9jvXMPj1tVuQ7EEo1bwKEHUC13j64a7drSj0qlpJldlqOGoZzVbvjnVduqnHbJ%2B0MmtDTEI7xvAcl%2BJFlLyi1HMvdnGMObyVRavulmKa422QAZm4CNhdFgk6VH0nWqkAXsd0vKM%2BbkdlkQVkbOks43jPK9qmW2HFhslBinm%2BxnG3ti713wy7%2BWDeGnmu5AxWwG0t1Wx2p04znr4h7QxvDNqroGwYy5OgUH5%2BR9IlZBHd6Yo6CuJjNNITSx0PcXluDDV%2BX8tMgqW3nSEE8OptkIkkKkNvBXAxzQqks0SpEyc7DXGX4MxdPfBdD7KytEoVcNygZlt7pSbEq0X6H7tFQxrFy3uOQWBR%2Bk8lOXtiQkUpUBpC6SeHyZ9kkDbgldLXsYnBW5TFixT9qXiK9i7sikGAI4ANYoblQTuaI3IYH8KSCyZdz%2BZxOwfOBIfJHtMNzDmL0GOqUBGi0Fw3HcXSdFcRMH%2Bg2ESC4ogXs%2F59HQi6Raf1psFoodKz%2Ft91ZcMR7ggi%2Bm%2FIitMkdsYKiU2YVISd1TfupWCMZLACePG3XNk6iw8zFktukRgcJqZMsjpIbSXrx66sEF3bXRF0PhuuJdrsHRfLRiki3ctvYbgKRtgClQSCz6OSMqwbz2JqESkfhvWl4OK7C6Xp8B5bt2foLe5%2FKNqjZH3rBk3KSs&X-Amz-Signature=b8a82f6ee4d243868daced4aadb7645d03fe292dd2b7b2e1b4441362ea1cbcc9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577Y6RUM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIH5PAiB%2BMNFyLHyxXvnc13wcPvKxrDnhPUsGyq%2BiAfpMAiEA6PzZEWWOokFWJPe7DGZ13KgLNADIqYXvOWV%2B8OwuOkgq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDGyqB2I9vmKGMzYMuSrcA%2FaspPoaIgtc7pOkgGuDsGMPDaJiqddSbcc1yPxvtRwR2ZmRl%2BudviDUiAVygqbYtZm1JhhBr7bPETrwxdyhhs6NwXPuvp%2FR%2FIqm6u7CLdSdkzXc5xhB5XjT6%2B9Ftry%2BC2UHyln0mVI5LEu3qr2v8MGChHVqVMESIk1eNmSGOKj7uZpkQjzm7RXqTos3rD9jvXMPj1tVuQ7EEo1bwKEHUC13j64a7drSj0qlpJldlqOGoZzVbvjnVduqnHbJ%2B0MmtDTEI7xvAcl%2BJFlLyi1HMvdnGMObyVRavulmKa422QAZm4CNhdFgk6VH0nWqkAXsd0vKM%2BbkdlkQVkbOks43jPK9qmW2HFhslBinm%2BxnG3ti713wy7%2BWDeGnmu5AxWwG0t1Wx2p04znr4h7QxvDNqroGwYy5OgUH5%2BR9IlZBHd6Yo6CuJjNNITSx0PcXluDDV%2BX8tMgqW3nSEE8OptkIkkKkNvBXAxzQqks0SpEyc7DXGX4MxdPfBdD7KytEoVcNygZlt7pSbEq0X6H7tFQxrFy3uOQWBR%2Bk8lOXtiQkUpUBpC6SeHyZ9kkDbgldLXsYnBW5TFixT9qXiK9i7sikGAI4ANYoblQTuaI3IYH8KSCyZdz%2BZxOwfOBIfJHtMNzDmL0GOqUBGi0Fw3HcXSdFcRMH%2Bg2ESC4ogXs%2F59HQi6Raf1psFoodKz%2Ft91ZcMR7ggi%2Bm%2FIitMkdsYKiU2YVISd1TfupWCMZLACePG3XNk6iw8zFktukRgcJqZMsjpIbSXrx66sEF3bXRF0PhuuJdrsHRfLRiki3ctvYbgKRtgClQSCz6OSMqwbz2JqESkfhvWl4OK7C6Xp8B5bt2foLe5%2FKNqjZH3rBk3KSs&X-Amz-Signature=68a96f82700f734064a09ebe50919c905225e12679bcbecd6c0feffff801064d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577Y6RUM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIH5PAiB%2BMNFyLHyxXvnc13wcPvKxrDnhPUsGyq%2BiAfpMAiEA6PzZEWWOokFWJPe7DGZ13KgLNADIqYXvOWV%2B8OwuOkgq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDGyqB2I9vmKGMzYMuSrcA%2FaspPoaIgtc7pOkgGuDsGMPDaJiqddSbcc1yPxvtRwR2ZmRl%2BudviDUiAVygqbYtZm1JhhBr7bPETrwxdyhhs6NwXPuvp%2FR%2FIqm6u7CLdSdkzXc5xhB5XjT6%2B9Ftry%2BC2UHyln0mVI5LEu3qr2v8MGChHVqVMESIk1eNmSGOKj7uZpkQjzm7RXqTos3rD9jvXMPj1tVuQ7EEo1bwKEHUC13j64a7drSj0qlpJldlqOGoZzVbvjnVduqnHbJ%2B0MmtDTEI7xvAcl%2BJFlLyi1HMvdnGMObyVRavulmKa422QAZm4CNhdFgk6VH0nWqkAXsd0vKM%2BbkdlkQVkbOks43jPK9qmW2HFhslBinm%2BxnG3ti713wy7%2BWDeGnmu5AxWwG0t1Wx2p04znr4h7QxvDNqroGwYy5OgUH5%2BR9IlZBHd6Yo6CuJjNNITSx0PcXluDDV%2BX8tMgqW3nSEE8OptkIkkKkNvBXAxzQqks0SpEyc7DXGX4MxdPfBdD7KytEoVcNygZlt7pSbEq0X6H7tFQxrFy3uOQWBR%2Bk8lOXtiQkUpUBpC6SeHyZ9kkDbgldLXsYnBW5TFixT9qXiK9i7sikGAI4ANYoblQTuaI3IYH8KSCyZdz%2BZxOwfOBIfJHtMNzDmL0GOqUBGi0Fw3HcXSdFcRMH%2Bg2ESC4ogXs%2F59HQi6Raf1psFoodKz%2Ft91ZcMR7ggi%2Bm%2FIitMkdsYKiU2YVISd1TfupWCMZLACePG3XNk6iw8zFktukRgcJqZMsjpIbSXrx66sEF3bXRF0PhuuJdrsHRfLRiki3ctvYbgKRtgClQSCz6OSMqwbz2JqESkfhvWl4OK7C6Xp8B5bt2foLe5%2FKNqjZH3rBk3KSs&X-Amz-Signature=46cda02ccd79876baee8091f477144a1b17526e7b3b42a59ecdaa3316cb59f6d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FS32YYL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC4x6oYFqtFmg0ggqUMz2yBN3endSkyI0%2B1tHPjnqdWBwIhAOqFVaQLoVzURgN6aXjcOM1hB6TyisVcaUW3u5cLz5qpKv8DCHgQABoMNjM3NDIzMTgzODA1Igz7DyHXPeKN%2B5pP02Qq3AObNUU5JrAE8myAPXZ%2Br00DiaMg7qd1i28qi46uXmmMUujSfPz5EdlX5Nnla4vYmKljn2MWfH9grUhlaObeR5kVpszmfXRo%2Fbts22e1aOyJf7xkPrx9k%2BlWDPMg3buxg%2ByHBOgZJbOK%2Bg%2B4n%2B8hqqaDmgleodcl2xQXYhj%2BfkkV2y2ChPcYP13np6aQIXIvC2AlRYlA1vt7R7oZmJ%2B8g8a0LEXkTfwd%2FavSnU0b6POMRiZxEx%2BkroG6FZy02qBeVW6hDDNE4c70WSI9FOXvMgbCJqAUZG48g9KCa9fqBQsapTg%2FDoMq3yz4ZkORTEnMiTLhMj3r54FRnnt%2F46Q49nHzVAypXfH3rrWryfGXuqqyE%2BzI1Oy4bA5OqvZ5sNE9gdoXXvzNQrZ68%2FnmGSH3hiZ6wWaYwXb%2BODiVWVhVyjV3eKyT5ToguvnuWGwKWN79Ldf3br%2BeWdYbSy5k2iaS0%2FrVPd3ZXZSdIx1rf%2Fv4WxrGPLbr%2BEs6uZB5eNyBAqc654whPlCq96QO9%2FmAcpz5Z9LJB3J%2BvMCOzDx4KYC9QoNjT5OXLlNWtndBrejzye4PFUKMqZLIjFxVJjKovNqR94SMFSWOFVOd2NLmN7%2Bpy7oJZlGuaG7IrwNMQwtJnDDcw5i9BjqkARr2X8%2B2aOUATNLVab2%2BQbHwIGBNvN%2BuNRAKpSrClMUAbPN4aken0FklKaQe%2FlFU8M5ztH%2Bq1Qup41gOQ3WPW%2Fdtj41dGdCizXcvS2JvsTVVGSj4w8Jgp7zlPnKZjrUP%2BuaWpFAn9wn%2FXNmAK4i7iRrb8A0j2wnd%2FuJ6P9Yy1WptKI0%2Bsh81CstgdtZ016VB0nOGfgDGV9%2BhZBoIhng86OxOWi6I&X-Amz-Signature=8a6ec1c35174a20fdaeee2052e4885179c007678a6f785952b824121a24b3688&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGTPLN4R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCKLiog057L9JnqpjoMMy1nhtXG7AJUQjH%2BBDzf8McimgIhAMz2ukY%2FAq%2FA1X8drl73bdIeCpL5U0M%2FpMQkz32qj%2BPTKv8DCHgQABoMNjM3NDIzMTgzODA1Igz%2BOPrsvY7GhhhqAXwq3APr%2FstkcgmoIpgSwBHgJcXn6uP0aN%2BUaBanOQqXDP22pb%2BuTLPepkslqv54TFz7ovgvFxUacgGnqCP3T5P0THr2z%2FhqxkzCzaN5G7gHukqK6KDnUXyO22GsuYYO4Q6NHZ7W5Ar%2BIHwh5kw6USi1ph6hgEGk81YU8luC1hfjLRPqBtqK%2BIR2lLBDSudN1X3ZSy4ejYiAYFKeaQP1vN%2BvNh7bNH7iapuPUIaXm8DfNomGhofo0tZaiYOYhfmHfcbSw1yLjRuG%2BKCC18dLUgaZbo5jb2PlD92fKWRfT1O655jgP8ay6khTyFM%2FV4khv3N6liYAILbtiDjxQ%2FqXzcJxU46HHPioZbExLGBAuQwruO8CIhM%2BxA%2BCdKnteKwxbUcLvm9%2Fmevz%2FPTeKvpim8lZ%2F95nJcQ1ocCmi0Gme%2Fe%2Fijm2wm%2Fb%2BBW7R6WR0PrfCrnBa9Cxw8o5WlHWXWYA0T40cKG9gK8EEpRsNvYGki6bpDSIITRWwik5HMlWWyLdZDNaT9JSWMBrj7f4OOKbr6Vk%2Fvdo3KjPPjgGdT4H%2BBuN5cgtgQWhf3%2FEWfIUVcDzszLZodQ7kQvLwcvFp7mvPRLfTRINR9Ofsoio1eD4du%2BF8x9u9Mziv6%2FAGKEXpAxNDjCSxJi9BjqkASLdlWl1enLs1cZ4OvxPFtjjES7lWvu28%2BAi%2FsOfndOEuRx48XtwZGUw55OzxowA6Kt1r0FetwG3rw7fmRI7u2fQJisrMBy%2BoIrz7R5FektB9dnV9fCUMI6fmiX9RqIXm6CfbwoZLZjANIKC9d%2ByqUySqn5%2BrxGqjCAlP5%2FeFleuuuRHP%2FZS%2FpGgOWCvhmXjlzmP81NhA7SHT%2BMJsoR5CtRlUgzk&X-Amz-Signature=2cef8189d7c553f04939fafd24fbfbf237378ec09d762c7d9b0666144e7a1c40&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577Y6RUM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIH5PAiB%2BMNFyLHyxXvnc13wcPvKxrDnhPUsGyq%2BiAfpMAiEA6PzZEWWOokFWJPe7DGZ13KgLNADIqYXvOWV%2B8OwuOkgq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDGyqB2I9vmKGMzYMuSrcA%2FaspPoaIgtc7pOkgGuDsGMPDaJiqddSbcc1yPxvtRwR2ZmRl%2BudviDUiAVygqbYtZm1JhhBr7bPETrwxdyhhs6NwXPuvp%2FR%2FIqm6u7CLdSdkzXc5xhB5XjT6%2B9Ftry%2BC2UHyln0mVI5LEu3qr2v8MGChHVqVMESIk1eNmSGOKj7uZpkQjzm7RXqTos3rD9jvXMPj1tVuQ7EEo1bwKEHUC13j64a7drSj0qlpJldlqOGoZzVbvjnVduqnHbJ%2B0MmtDTEI7xvAcl%2BJFlLyi1HMvdnGMObyVRavulmKa422QAZm4CNhdFgk6VH0nWqkAXsd0vKM%2BbkdlkQVkbOks43jPK9qmW2HFhslBinm%2BxnG3ti713wy7%2BWDeGnmu5AxWwG0t1Wx2p04znr4h7QxvDNqroGwYy5OgUH5%2BR9IlZBHd6Yo6CuJjNNITSx0PcXluDDV%2BX8tMgqW3nSEE8OptkIkkKkNvBXAxzQqks0SpEyc7DXGX4MxdPfBdD7KytEoVcNygZlt7pSbEq0X6H7tFQxrFy3uOQWBR%2Bk8lOXtiQkUpUBpC6SeHyZ9kkDbgldLXsYnBW5TFixT9qXiK9i7sikGAI4ANYoblQTuaI3IYH8KSCyZdz%2BZxOwfOBIfJHtMNzDmL0GOqUBGi0Fw3HcXSdFcRMH%2Bg2ESC4ogXs%2F59HQi6Raf1psFoodKz%2Ft91ZcMR7ggi%2Bm%2FIitMkdsYKiU2YVISd1TfupWCMZLACePG3XNk6iw8zFktukRgcJqZMsjpIbSXrx66sEF3bXRF0PhuuJdrsHRfLRiki3ctvYbgKRtgClQSCz6OSMqwbz2JqESkfhvWl4OK7C6Xp8B5bt2foLe5%2FKNqjZH3rBk3KSs&X-Amz-Signature=c56cf960d440ad57515e4111a02b0f00e7e8831648f8b7c1f77aca3cfd2a2f5c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577Y6RUM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIH5PAiB%2BMNFyLHyxXvnc13wcPvKxrDnhPUsGyq%2BiAfpMAiEA6PzZEWWOokFWJPe7DGZ13KgLNADIqYXvOWV%2B8OwuOkgq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDGyqB2I9vmKGMzYMuSrcA%2FaspPoaIgtc7pOkgGuDsGMPDaJiqddSbcc1yPxvtRwR2ZmRl%2BudviDUiAVygqbYtZm1JhhBr7bPETrwxdyhhs6NwXPuvp%2FR%2FIqm6u7CLdSdkzXc5xhB5XjT6%2B9Ftry%2BC2UHyln0mVI5LEu3qr2v8MGChHVqVMESIk1eNmSGOKj7uZpkQjzm7RXqTos3rD9jvXMPj1tVuQ7EEo1bwKEHUC13j64a7drSj0qlpJldlqOGoZzVbvjnVduqnHbJ%2B0MmtDTEI7xvAcl%2BJFlLyi1HMvdnGMObyVRavulmKa422QAZm4CNhdFgk6VH0nWqkAXsd0vKM%2BbkdlkQVkbOks43jPK9qmW2HFhslBinm%2BxnG3ti713wy7%2BWDeGnmu5AxWwG0t1Wx2p04znr4h7QxvDNqroGwYy5OgUH5%2BR9IlZBHd6Yo6CuJjNNITSx0PcXluDDV%2BX8tMgqW3nSEE8OptkIkkKkNvBXAxzQqks0SpEyc7DXGX4MxdPfBdD7KytEoVcNygZlt7pSbEq0X6H7tFQxrFy3uOQWBR%2Bk8lOXtiQkUpUBpC6SeHyZ9kkDbgldLXsYnBW5TFixT9qXiK9i7sikGAI4ANYoblQTuaI3IYH8KSCyZdz%2BZxOwfOBIfJHtMNzDmL0GOqUBGi0Fw3HcXSdFcRMH%2Bg2ESC4ogXs%2F59HQi6Raf1psFoodKz%2Ft91ZcMR7ggi%2Bm%2FIitMkdsYKiU2YVISd1TfupWCMZLACePG3XNk6iw8zFktukRgcJqZMsjpIbSXrx66sEF3bXRF0PhuuJdrsHRfLRiki3ctvYbgKRtgClQSCz6OSMqwbz2JqESkfhvWl4OK7C6Xp8B5bt2foLe5%2FKNqjZH3rBk3KSs&X-Amz-Signature=1e5a026a9e7f197a50e863c6fe598b516e10e567d565b6e8051a32b880fad52b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577Y6RUM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIH5PAiB%2BMNFyLHyxXvnc13wcPvKxrDnhPUsGyq%2BiAfpMAiEA6PzZEWWOokFWJPe7DGZ13KgLNADIqYXvOWV%2B8OwuOkgq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDGyqB2I9vmKGMzYMuSrcA%2FaspPoaIgtc7pOkgGuDsGMPDaJiqddSbcc1yPxvtRwR2ZmRl%2BudviDUiAVygqbYtZm1JhhBr7bPETrwxdyhhs6NwXPuvp%2FR%2FIqm6u7CLdSdkzXc5xhB5XjT6%2B9Ftry%2BC2UHyln0mVI5LEu3qr2v8MGChHVqVMESIk1eNmSGOKj7uZpkQjzm7RXqTos3rD9jvXMPj1tVuQ7EEo1bwKEHUC13j64a7drSj0qlpJldlqOGoZzVbvjnVduqnHbJ%2B0MmtDTEI7xvAcl%2BJFlLyi1HMvdnGMObyVRavulmKa422QAZm4CNhdFgk6VH0nWqkAXsd0vKM%2BbkdlkQVkbOks43jPK9qmW2HFhslBinm%2BxnG3ti713wy7%2BWDeGnmu5AxWwG0t1Wx2p04znr4h7QxvDNqroGwYy5OgUH5%2BR9IlZBHd6Yo6CuJjNNITSx0PcXluDDV%2BX8tMgqW3nSEE8OptkIkkKkNvBXAxzQqks0SpEyc7DXGX4MxdPfBdD7KytEoVcNygZlt7pSbEq0X6H7tFQxrFy3uOQWBR%2Bk8lOXtiQkUpUBpC6SeHyZ9kkDbgldLXsYnBW5TFixT9qXiK9i7sikGAI4ANYoblQTuaI3IYH8KSCyZdz%2BZxOwfOBIfJHtMNzDmL0GOqUBGi0Fw3HcXSdFcRMH%2Bg2ESC4ogXs%2F59HQi6Raf1psFoodKz%2Ft91ZcMR7ggi%2Bm%2FIitMkdsYKiU2YVISd1TfupWCMZLACePG3XNk6iw8zFktukRgcJqZMsjpIbSXrx66sEF3bXRF0PhuuJdrsHRfLRiki3ctvYbgKRtgClQSCz6OSMqwbz2JqESkfhvWl4OK7C6Xp8B5bt2foLe5%2FKNqjZH3rBk3KSs&X-Amz-Signature=f15db47fa79cf0372fc9ed093d45051c625f1262d0d0913ace66577522a9ac85&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUGSPDZS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICeV73wG6SzlOftH3nEJ2i5sBft%2BWR1DTwNwF6KgPckcAiEA1x5Z5SFite%2FxXusyTxQFpVlfkQkc2P8ggaQUg4KE7csq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDOCub97nxQHYrW%2FwbircA7NZIIaiHq3I2lhDm1YRCIW48Jl2WOjOBBp1Tb8XaJhRAlcuwxImezFI0%2FpCKuK21k25KUVCCa%2Fg6DopcHI2gVPwo41TeRk9dmg%2FCJwBhl8eEbTUsDtZVwR3492nLQD0JsGmX1n7C2xGiGdSbd%2F6ZXhfMEKs0Z7K3jZYZj4hjGc98TlzV63MJiL1sjFUfNzqyBut7wBuKh5Nt18vghNI7yua%2BjvmIKHKsFLgvtNR8eN4jd5jXsrkblMQ6fZU3nHuAr4FQoNDcfZlIM%2BLD7DKvF0rEsuytAA0u283lmu2K2FDdRLOMsWyk78%2B%2Bl0QzowWr8HLkFjcXI5uxAtO9BZYzyz6f3zey0H%2FWkeqMk5L%2F56QZo%2BHJfIjqdqhj2AdSAWKkYBSHYLEKMQnLOLeues71lj4p70QpUSH9iuRxRRfdacyo0Voo7GXxLJQhSoFmEDKdTUxwL3PTjddnfYDt7N%2BaOdhesRxHDgp9QmG%2FlaanlT%2FTA4ABrBeicraS9XnbqdL29Ud39V0huX6Z%2FsiUUhvE9N4xgawDwSAM3R7eFf6KzSw%2BOszj8Cz1GjPU4zLm2OGLnqhmiGkoehOG%2BUutT2Mmm0GZREaOvXhgZILAljvDw6hpURkX%2BTiXNvnLbrOMJvEmL0GOqUBMe4mkLx1XOF6x3kqZs0%2FaSxM5gFB2c%2ByqemS9BEp2djJPIdUu5KLzGaRX4SvlHTcUPVIUVDIgiuUmBe5iePhho2E63dKoEKAjAgHfh8rQq%2BhNWggZU7aB59Y9c%2FcnWI3wXCk2fgTfOUW9n8mIudi4SPPLcR6F%2B6JmO1cXvaRqefkHguVVYGJ9N%2FITanrYOSlgpLRCap95JF7XO2uu7YmV6W9leWR&X-Amz-Signature=550811152d618b27290fe384938a172af3dd42e1345edd795b8cda948d79270b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYP3P3RB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCxyEmB6rwGjZlVgvoQnEM37TV%2FCPjdyQbKl0SLM0C%2BtAIhAKdhG1%2B4sjYFb4Juk%2BIYVunE97ASB5qyB3o9PUkMEJV%2BKv8DCHgQABoMNjM3NDIzMTgzODA1IgzqEC%2BPlkUuNB2bVUQq3APgv9FXGHa5jFYZovx6CkM5FF9Pf%2BvVeaY9isTy%2F3cDnRzvwrc0h0pgiDZxk3yp2ntCDX%2B8wkh9hAuOKQVye2cygDDPhmaD0zHj%2ByNSqQ28EM%2FOafTizVnx29Vo8AIv6PCNHwDR%2BlP4OB1%2BhGgPuWBUN6R3aTWknIt3qtgBdZWCkNp103DHyBiBcO4HbMx1AhJxG2emDjX5NwHrdK3kwop4tspR%2BP3DEZT8FuchjK4v0u5IZFicSBAaavsLhwjm6RG0gQ2hfhV5V51Timj0bWntnNAeepmF3P8yQjQ56JfBspWVwDYbl5hp3rp2LqEL8cBy0jog71k701GED%2Ftat2rDaNPLYK2CKPsM%2ByvXTYPRzRxx21OvKJD7czT1F18BZav4gdPnVjJtSWdA1EsQ%2BJtaE1YybOFBEqGYVDnIYXu3IOATHVURrcJ%2F5mq4L77VtJOX5PxPfm9pYUzwbHkVAj0XFPwOgvp5i6pqXnsafUSpJojWHlSCsX6dsKOmnLhTMPClrJixUbeoG87Lf%2B%2F0HktS2aGDTWAqXdn7glslAyNkwQXx4fgXd2ce%2BoTNWGEGbIlLKq4LE%2Bg99KD3oSDr5ICfBUmrioi7vP6DsXZ5BjpjAYUl7yNPP1FfDO1C%2FzC4xJi9BjqkAdBwj2j0%2BH8bPWhUFtX8tSvWqfkzdOygtoNA3rb3OrlgefGpfOtSDi0hNseAgA56HKNLDpHpks%2Bn3kpx2V0KkfcN9UMomTJ9I7UO3kFrP65Uk77UwdAbGbQZtFJT35KHGJh59h7Okz9BWHp4tbG1oEdQG06YRWqzxGBkw06aEHR%2FeKy3A0w9Tv3LxWbSMahboycKnnGOSFMIfPFkUGdmXci%2FTjja&X-Amz-Signature=42d095239ca7922d609adb75923077579d59d6a307e339fd5b4a15fd2c3a24e3&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLEKWVO3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDREF8zX2cn3an%2FVwQaiHhB7%2Bz0QdUP96wnVOkqy6BYFQIgKb121K8l9ULtAwNbsnSRLvulOfwjMBp1p1gQh%2FBqAyAq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDAGxucoPqU5IfsCwSircA%2F5zyiPKrRas6Lc532R8xDQXfgtB6X8xjOY%2FO8HEKPJDq1dCjk9LphxltukMOPLT6Z4IlLjBNk7v8b2emiCF3AK62m1JSnkADMGYWcYxTZ8BZiVmNaD34IzG8VnxqYW%2FaEKuGIOJ0LwbE%2FEycDUQOP7DBr7sH11c%2BzSFhFfRKdUR7aJrrpE54NDJ9lzY7CiEsXOmqViFZoBUEpgcPS98SlLw4FqG3n%2B4iDV8X8Jz2%2FAhuKPxNXxZqPwGoddRIsP8u1KW5xIjuwm3BZqHoKu3wdzx%2BNxwf2bePI2qTMbrJLzYuJd5Vez30AMCURhrRwmd7wJpDbV556wG2yWUBT1Gu59kFqwDyC%2Fy%2FU6cdKtWdiyjvv12xFrZJY%2BoPaA2kJIRzzhEz97RZTBD4igci40au3XljuoQghABgkBfAzRqEs2YqrfOFDULl%2Bx1kFl2mKWDntUvMCWOaW%2BjpwsEh%2BUaeZd3zdYyyvF8mdRzyrcinIGWhO5hwB0rQex7T39HruDn49F%2BXe2plgiG34PNBVo2FKPfAIUMyGsOoUw7b1cAb1VL1STCharkJ4LA%2FiqrUSk31heKmqKq7pFKAsYq5HbwdEebUpLL8VO5cD59kSVeQj2kmH4GgGON%2FCncyO1tMIbEmL0GOqUBDkKUws%2F8ruLUutrxtBBVwh26Wo0qFEDrXB2CamyQ8LGqMxgxt02WX0WEQFJDVKL9MFTX4KbDguKs9xu3n7F5YmvzEPwxsX63FBUFcWSol708OdsoNviYGaPGQzv8el18uiRW84GLKZSojlhtHk%2FhOr2KpzHMvU8fqmfPrJyrqg8xhRYnuRrUQd%2BlMqFDdRWeOXH%2F2mwcNy0LDlH%2BCpAK8RZvAzcd&X-Amz-Signature=f63359a8dbd00a7f86af27259a0276af90384847c62930e061710e56834a9cfd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626FDE7SV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHxV7cjeUva47EMSUvCmoCkLJmS8HVWd2oCY11X1E2vBAiAdaHqWpE9SbHIOu9TQ68DVQktAu%2FRgo37TWChShs1oaSr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMBvTPBB%2FPFTqAle3pKtwDsuADRgzoPMblkuhMVyf3QT%2By2y9pm%2FGhLXillTK61IGSgRfgeviqjAmbdbseqqagyIZOsckWmOhndcWBD5b%2BHnQNirp7kjW0rdWfHaifjkTX%2FUXanEUfae2ZkgIgVHMIXKI5PpeFPnk%2B9jbJ5aS2Os0QfU7dyXY%2FWwBFVEZ5kpSPsdWOxZ%2B%2FupLT%2BH0jgFn0UvPD7YElCqQQ78b%2BrPunW%2F9n2jk7cVFxs9ufknuQY4vUX0IxndDCJ5og1xZ1E9Brdh3YXmLe5pzZET%2FABwaWZ5uXpUZeOjNklcXTt1tAB6dnk17x%2BpF2S%2FJLrBepu4I%2FJX1tDCgyeROMyvp%2FjBhY87WJIX0YPW2hkjbCLLhziQg9k7FFM6oEFXdm1q8B4%2BXz76MXK13UmqJaMZqCpR3x5IbzH69PzaRMTqRK3vr%2FmHmOHGFp%2BLotq%2FADh0js478qxlWFwDG6fFrD%2FCmbUIVPT7MbDnIKptLRMyhMMWF0uY%2F05rqwftOVPZxC2w7oamXifuhFo1KrMWfaOXfFmYvF6rfAkg3lynUI7jJSKp391dEsGPqxLaICz0KXqEWXuWJRIQY57YTWO9OOxKb4WLI5Mo3TcLywh1i6t6quiOp%2FPSy4if9fT1dPiZj5qPgwo8SYvQY6pgEa9oBj85MKQDRo0C%2BbyhFHdNlKozxg1fskxa1FQ5rT5WWP9E%2BB7%2B2oozUvl9FIXmyUEz0040R2PhEFKp4rnuBwSGxQ%2FKcdeghbgxeYYeMkFFd8PzFGQRCItsYYUxMRHxGIYORnWpX9liVXk3MJTOpcbRZ%2FqQZMgMbVRDh4R%2FcUKfWu6XGcnaBpBP1GLhxzkMKMtY4ksSF8UA1rfbheI4KRtwJDKVDL&X-Amz-Signature=273dad8df7a499a52967386872295bfd85a182c4b0bb3cff9e86a25042616fbf&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626FDE7SV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHxV7cjeUva47EMSUvCmoCkLJmS8HVWd2oCY11X1E2vBAiAdaHqWpE9SbHIOu9TQ68DVQktAu%2FRgo37TWChShs1oaSr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMBvTPBB%2FPFTqAle3pKtwDsuADRgzoPMblkuhMVyf3QT%2By2y9pm%2FGhLXillTK61IGSgRfgeviqjAmbdbseqqagyIZOsckWmOhndcWBD5b%2BHnQNirp7kjW0rdWfHaifjkTX%2FUXanEUfae2ZkgIgVHMIXKI5PpeFPnk%2B9jbJ5aS2Os0QfU7dyXY%2FWwBFVEZ5kpSPsdWOxZ%2B%2FupLT%2BH0jgFn0UvPD7YElCqQQ78b%2BrPunW%2F9n2jk7cVFxs9ufknuQY4vUX0IxndDCJ5og1xZ1E9Brdh3YXmLe5pzZET%2FABwaWZ5uXpUZeOjNklcXTt1tAB6dnk17x%2BpF2S%2FJLrBepu4I%2FJX1tDCgyeROMyvp%2FjBhY87WJIX0YPW2hkjbCLLhziQg9k7FFM6oEFXdm1q8B4%2BXz76MXK13UmqJaMZqCpR3x5IbzH69PzaRMTqRK3vr%2FmHmOHGFp%2BLotq%2FADh0js478qxlWFwDG6fFrD%2FCmbUIVPT7MbDnIKptLRMyhMMWF0uY%2F05rqwftOVPZxC2w7oamXifuhFo1KrMWfaOXfFmYvF6rfAkg3lynUI7jJSKp391dEsGPqxLaICz0KXqEWXuWJRIQY57YTWO9OOxKb4WLI5Mo3TcLywh1i6t6quiOp%2FPSy4if9fT1dPiZj5qPgwo8SYvQY6pgEa9oBj85MKQDRo0C%2BbyhFHdNlKozxg1fskxa1FQ5rT5WWP9E%2BB7%2B2oozUvl9FIXmyUEz0040R2PhEFKp4rnuBwSGxQ%2FKcdeghbgxeYYeMkFFd8PzFGQRCItsYYUxMRHxGIYORnWpX9liVXk3MJTOpcbRZ%2FqQZMgMbVRDh4R%2FcUKfWu6XGcnaBpBP1GLhxzkMKMtY4ksSF8UA1rfbheI4KRtwJDKVDL&X-Amz-Signature=d532ef3ae2d7f3856ae4f707e94b92a14155a5c49ccc04156bbffdf95b14389f&X-Amz-SignedHeaders=host&x-id=GetObject)

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
