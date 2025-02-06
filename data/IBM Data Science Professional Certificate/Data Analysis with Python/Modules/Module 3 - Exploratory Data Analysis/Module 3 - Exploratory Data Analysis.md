

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LC7SYAA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCej28B8pPV3TSQCK%2BWrGk3AXNq%2B4lqyuF1bYy%2Fc0sSFgIgEbhrzyfBs6JsNArrWe75l5MHUlTWNrYBXeTuKaQAb60q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMBgPo8zTqlHR8g9vCrcAzA58DbxTtx0uFHVnadPl59fCEssaBf9si0y8SCyyv7tjmQmuS%2BGNAQCEN%2B4rTGXtJp635NQpe%2BTEat7nS653iFrccko5RrjTGudOAaycDY2BByDHdlRq8RL6x6gmZRRGweYn6NzEsJ8dYN1FjPtb1WtyrG%2FjGUet4QhdMr4HBuCprB2cbeXaG3vjWQTZEHVJ4dCEFiqHsrRjTGXhFPEAlgxZwfNn7hweGyesrJMKPsmwOf1RvjYbaSC6sEWUsgrqjmbmPU9bGuJFt2o8dosygFMQPK4IByrd8UIxakTCOePETsSVScRJNU4iwb7P5oKnFGGNprjXLhTNAu9J48Q%2FKpB88QnIekgWhn%2BxlPXxutEoVl9TvOkUd2ApfI7GLsndraeYHCNhrhZbdxLK1pH5VkDxmV6dwZvTzHAFz%2BuL7hY6gcvMCg7QB3PJ5dvdvCEpeNBdqc%2FbZWnF3lSnJ0gGr8mer4wo9SOTb9yH2kkULEMyuT5qPTqQxc6DX87%2B8Nl5XE5XfmShbVk03TxI0slnhMLU8feMnZF8rEaOYYphIo1%2B9rqCsPz8uFYLj3AscgWHDiqYGoBLtyJXqe5g%2Bdz0ILWMEToNLO%2FcVV7%2FyDq1FPU5PAyudWB4hinK4s0MLiZkb0GOqUBvRIX%2BjIEgLMIU%2BTpqQ3x1Lqvl3VXLu%2FbqsO9JtSVfoX2DT%2B%2Bw2Oi0JtiT4EVr8V9MJ2ozUrrC9CW6pa0usBQEYIUOT1x8itfU73KZA6Yhg3ft4iNjD3r%2FQFg04LVtOTKQhTtZrsijmXJNmRzuRocg5XKzVWWHqL41FYa%2FboaXAfDUGn3stYWgi%2Bs2Wyzx14%2BDkhtpUSH%2BGSd5UoT7TmxzlyzEKXx&X-Amz-Signature=d72400673ec88649e233dfde6d90fc1bae19867bd1aeb9113410e0bdc6be44ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LC7SYAA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCej28B8pPV3TSQCK%2BWrGk3AXNq%2B4lqyuF1bYy%2Fc0sSFgIgEbhrzyfBs6JsNArrWe75l5MHUlTWNrYBXeTuKaQAb60q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMBgPo8zTqlHR8g9vCrcAzA58DbxTtx0uFHVnadPl59fCEssaBf9si0y8SCyyv7tjmQmuS%2BGNAQCEN%2B4rTGXtJp635NQpe%2BTEat7nS653iFrccko5RrjTGudOAaycDY2BByDHdlRq8RL6x6gmZRRGweYn6NzEsJ8dYN1FjPtb1WtyrG%2FjGUet4QhdMr4HBuCprB2cbeXaG3vjWQTZEHVJ4dCEFiqHsrRjTGXhFPEAlgxZwfNn7hweGyesrJMKPsmwOf1RvjYbaSC6sEWUsgrqjmbmPU9bGuJFt2o8dosygFMQPK4IByrd8UIxakTCOePETsSVScRJNU4iwb7P5oKnFGGNprjXLhTNAu9J48Q%2FKpB88QnIekgWhn%2BxlPXxutEoVl9TvOkUd2ApfI7GLsndraeYHCNhrhZbdxLK1pH5VkDxmV6dwZvTzHAFz%2BuL7hY6gcvMCg7QB3PJ5dvdvCEpeNBdqc%2FbZWnF3lSnJ0gGr8mer4wo9SOTb9yH2kkULEMyuT5qPTqQxc6DX87%2B8Nl5XE5XfmShbVk03TxI0slnhMLU8feMnZF8rEaOYYphIo1%2B9rqCsPz8uFYLj3AscgWHDiqYGoBLtyJXqe5g%2Bdz0ILWMEToNLO%2FcVV7%2FyDq1FPU5PAyudWB4hinK4s0MLiZkb0GOqUBvRIX%2BjIEgLMIU%2BTpqQ3x1Lqvl3VXLu%2FbqsO9JtSVfoX2DT%2B%2Bw2Oi0JtiT4EVr8V9MJ2ozUrrC9CW6pa0usBQEYIUOT1x8itfU73KZA6Yhg3ft4iNjD3r%2FQFg04LVtOTKQhTtZrsijmXJNmRzuRocg5XKzVWWHqL41FYa%2FboaXAfDUGn3stYWgi%2Bs2Wyzx14%2BDkhtpUSH%2BGSd5UoT7TmxzlyzEKXx&X-Amz-Signature=8fe2dd2fcbe52e27d9da1acf7d09376cd7a435cc4a365879291f32b846cb421e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LC7SYAA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCej28B8pPV3TSQCK%2BWrGk3AXNq%2B4lqyuF1bYy%2Fc0sSFgIgEbhrzyfBs6JsNArrWe75l5MHUlTWNrYBXeTuKaQAb60q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMBgPo8zTqlHR8g9vCrcAzA58DbxTtx0uFHVnadPl59fCEssaBf9si0y8SCyyv7tjmQmuS%2BGNAQCEN%2B4rTGXtJp635NQpe%2BTEat7nS653iFrccko5RrjTGudOAaycDY2BByDHdlRq8RL6x6gmZRRGweYn6NzEsJ8dYN1FjPtb1WtyrG%2FjGUet4QhdMr4HBuCprB2cbeXaG3vjWQTZEHVJ4dCEFiqHsrRjTGXhFPEAlgxZwfNn7hweGyesrJMKPsmwOf1RvjYbaSC6sEWUsgrqjmbmPU9bGuJFt2o8dosygFMQPK4IByrd8UIxakTCOePETsSVScRJNU4iwb7P5oKnFGGNprjXLhTNAu9J48Q%2FKpB88QnIekgWhn%2BxlPXxutEoVl9TvOkUd2ApfI7GLsndraeYHCNhrhZbdxLK1pH5VkDxmV6dwZvTzHAFz%2BuL7hY6gcvMCg7QB3PJ5dvdvCEpeNBdqc%2FbZWnF3lSnJ0gGr8mer4wo9SOTb9yH2kkULEMyuT5qPTqQxc6DX87%2B8Nl5XE5XfmShbVk03TxI0slnhMLU8feMnZF8rEaOYYphIo1%2B9rqCsPz8uFYLj3AscgWHDiqYGoBLtyJXqe5g%2Bdz0ILWMEToNLO%2FcVV7%2FyDq1FPU5PAyudWB4hinK4s0MLiZkb0GOqUBvRIX%2BjIEgLMIU%2BTpqQ3x1Lqvl3VXLu%2FbqsO9JtSVfoX2DT%2B%2Bw2Oi0JtiT4EVr8V9MJ2ozUrrC9CW6pa0usBQEYIUOT1x8itfU73KZA6Yhg3ft4iNjD3r%2FQFg04LVtOTKQhTtZrsijmXJNmRzuRocg5XKzVWWHqL41FYa%2FboaXAfDUGn3stYWgi%2Bs2Wyzx14%2BDkhtpUSH%2BGSd5UoT7TmxzlyzEKXx&X-Amz-Signature=25d2621bb303246eb495f9d0750c922e23ec0ced014adc062b31aed8bb27bd6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633D6OT5V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIGhuVEVGmeXBv3od6hKyLlz9dR2%2B9MLQChDkAMkyCr%2FGAiEAzSJSOtFiq26xodb%2B7%2FVMClcMP1fwkROsCVAazK6Koygq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGD9muqUhnwsALZT6CrcA8ycek8TbD6TSnEkRbfMiwiRvw3CTnB1cdO1qEMRXuRQnMxw7C6m2%2F1Z7r4jy8a212RHQBiyHnByXlEJY92QGH85OUrpOAuzv0JIN8AVknqaT6lTNUxCSawD0g%2BVWGwSw04s6wDw8Lf93lJszJsUIlPaQFswVjthjLZUcVcBvqENtKj4M9zYaSAPbDVtPh1Pq9oVIW7MG54hj0uDrMUsLIJVtBFkBgvJsn4AGe%2FZYc%2BmKnPt%2FJhL%2FMG3WdrXCa2gYBOVKqwGKryBJFqlI7l9B3yF2PUoNxZ2S5LCfUOQ8NGsEC6TTNJqA00tUbGZhQuwbC4M8WipXEc72Xev4efdi7QWgGpVw9Tb0sxYxgHVjJeJPf6QvQBOPv4yLjXMpkuJRMVGhiv3Lfxr9K8RHdX2A1AEAB5nVwJxiTYOXhlxM%2Bkz77WZPasVJMn0CAHix5e%2FyEAJ6DgTiFrI1tUtQlYB%2FMjhTzGt3sfrF%2FrV6%2BWqSg1eFTJRkdNijWDbInnPkds%2BTCzRvMZU7UktMXXPKGn9Vb0sv2YDoM0DZBlujDN5nLA759A0IS6dHFtzd6Y0PxDCOMP%2FenDm3X4ubT6KGYhvrR9cfQo2HldNX37ZVH3sKdaRNmJMxw5mx%2F5Cc%2BR4MPuYkb0GOqUB5GTgDSw4D6NBU8ym0e8r06INyPanyA3pMCoAemls9RCp2xmtvi0J15nIwSeh%2FMFcd6FKItdzdeeU72%2FVpYLWLRgGisN0gzEMRwaZXrZ%2B2mpMRI1Q0MzH55I%2Bros8g%2B3SvhsWTq3b%2FWLpC0ClM5vkyoR9og146KUTebw0gFNZAyz%2BYVTKY9tHYKHQyFTxg395b%2BQQEdddDyvKx11Ro1WefmmWInSq&X-Amz-Signature=65f443a2301dee08e8863f936e8819e496a993eb32bd9c71aab83b94357dbd1e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633D6OT5V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIGhuVEVGmeXBv3od6hKyLlz9dR2%2B9MLQChDkAMkyCr%2FGAiEAzSJSOtFiq26xodb%2B7%2FVMClcMP1fwkROsCVAazK6Koygq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGD9muqUhnwsALZT6CrcA8ycek8TbD6TSnEkRbfMiwiRvw3CTnB1cdO1qEMRXuRQnMxw7C6m2%2F1Z7r4jy8a212RHQBiyHnByXlEJY92QGH85OUrpOAuzv0JIN8AVknqaT6lTNUxCSawD0g%2BVWGwSw04s6wDw8Lf93lJszJsUIlPaQFswVjthjLZUcVcBvqENtKj4M9zYaSAPbDVtPh1Pq9oVIW7MG54hj0uDrMUsLIJVtBFkBgvJsn4AGe%2FZYc%2BmKnPt%2FJhL%2FMG3WdrXCa2gYBOVKqwGKryBJFqlI7l9B3yF2PUoNxZ2S5LCfUOQ8NGsEC6TTNJqA00tUbGZhQuwbC4M8WipXEc72Xev4efdi7QWgGpVw9Tb0sxYxgHVjJeJPf6QvQBOPv4yLjXMpkuJRMVGhiv3Lfxr9K8RHdX2A1AEAB5nVwJxiTYOXhlxM%2Bkz77WZPasVJMn0CAHix5e%2FyEAJ6DgTiFrI1tUtQlYB%2FMjhTzGt3sfrF%2FrV6%2BWqSg1eFTJRkdNijWDbInnPkds%2BTCzRvMZU7UktMXXPKGn9Vb0sv2YDoM0DZBlujDN5nLA759A0IS6dHFtzd6Y0PxDCOMP%2FenDm3X4ubT6KGYhvrR9cfQo2HldNX37ZVH3sKdaRNmJMxw5mx%2F5Cc%2BR4MPuYkb0GOqUB5GTgDSw4D6NBU8ym0e8r06INyPanyA3pMCoAemls9RCp2xmtvi0J15nIwSeh%2FMFcd6FKItdzdeeU72%2FVpYLWLRgGisN0gzEMRwaZXrZ%2B2mpMRI1Q0MzH55I%2Bros8g%2B3SvhsWTq3b%2FWLpC0ClM5vkyoR9og146KUTebw0gFNZAyz%2BYVTKY9tHYKHQyFTxg395b%2BQQEdddDyvKx11Ro1WefmmWInSq&X-Amz-Signature=45d2b6b28eaa6e6649a4362ae112610c703ac19ead2502ac32a59463fa2aa3a5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633D6OT5V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIGhuVEVGmeXBv3od6hKyLlz9dR2%2B9MLQChDkAMkyCr%2FGAiEAzSJSOtFiq26xodb%2B7%2FVMClcMP1fwkROsCVAazK6Koygq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGD9muqUhnwsALZT6CrcA8ycek8TbD6TSnEkRbfMiwiRvw3CTnB1cdO1qEMRXuRQnMxw7C6m2%2F1Z7r4jy8a212RHQBiyHnByXlEJY92QGH85OUrpOAuzv0JIN8AVknqaT6lTNUxCSawD0g%2BVWGwSw04s6wDw8Lf93lJszJsUIlPaQFswVjthjLZUcVcBvqENtKj4M9zYaSAPbDVtPh1Pq9oVIW7MG54hj0uDrMUsLIJVtBFkBgvJsn4AGe%2FZYc%2BmKnPt%2FJhL%2FMG3WdrXCa2gYBOVKqwGKryBJFqlI7l9B3yF2PUoNxZ2S5LCfUOQ8NGsEC6TTNJqA00tUbGZhQuwbC4M8WipXEc72Xev4efdi7QWgGpVw9Tb0sxYxgHVjJeJPf6QvQBOPv4yLjXMpkuJRMVGhiv3Lfxr9K8RHdX2A1AEAB5nVwJxiTYOXhlxM%2Bkz77WZPasVJMn0CAHix5e%2FyEAJ6DgTiFrI1tUtQlYB%2FMjhTzGt3sfrF%2FrV6%2BWqSg1eFTJRkdNijWDbInnPkds%2BTCzRvMZU7UktMXXPKGn9Vb0sv2YDoM0DZBlujDN5nLA759A0IS6dHFtzd6Y0PxDCOMP%2FenDm3X4ubT6KGYhvrR9cfQo2HldNX37ZVH3sKdaRNmJMxw5mx%2F5Cc%2BR4MPuYkb0GOqUB5GTgDSw4D6NBU8ym0e8r06INyPanyA3pMCoAemls9RCp2xmtvi0J15nIwSeh%2FMFcd6FKItdzdeeU72%2FVpYLWLRgGisN0gzEMRwaZXrZ%2B2mpMRI1Q0MzH55I%2Bros8g%2B3SvhsWTq3b%2FWLpC0ClM5vkyoR9og146KUTebw0gFNZAyz%2BYVTKY9tHYKHQyFTxg395b%2BQQEdddDyvKx11Ro1WefmmWInSq&X-Amz-Signature=1cca87e24c4f9a3bab89db8e36290eafe7c2f7906e48c6951c39dbbce40d0fd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633D6OT5V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIGhuVEVGmeXBv3od6hKyLlz9dR2%2B9MLQChDkAMkyCr%2FGAiEAzSJSOtFiq26xodb%2B7%2FVMClcMP1fwkROsCVAazK6Koygq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGD9muqUhnwsALZT6CrcA8ycek8TbD6TSnEkRbfMiwiRvw3CTnB1cdO1qEMRXuRQnMxw7C6m2%2F1Z7r4jy8a212RHQBiyHnByXlEJY92QGH85OUrpOAuzv0JIN8AVknqaT6lTNUxCSawD0g%2BVWGwSw04s6wDw8Lf93lJszJsUIlPaQFswVjthjLZUcVcBvqENtKj4M9zYaSAPbDVtPh1Pq9oVIW7MG54hj0uDrMUsLIJVtBFkBgvJsn4AGe%2FZYc%2BmKnPt%2FJhL%2FMG3WdrXCa2gYBOVKqwGKryBJFqlI7l9B3yF2PUoNxZ2S5LCfUOQ8NGsEC6TTNJqA00tUbGZhQuwbC4M8WipXEc72Xev4efdi7QWgGpVw9Tb0sxYxgHVjJeJPf6QvQBOPv4yLjXMpkuJRMVGhiv3Lfxr9K8RHdX2A1AEAB5nVwJxiTYOXhlxM%2Bkz77WZPasVJMn0CAHix5e%2FyEAJ6DgTiFrI1tUtQlYB%2FMjhTzGt3sfrF%2FrV6%2BWqSg1eFTJRkdNijWDbInnPkds%2BTCzRvMZU7UktMXXPKGn9Vb0sv2YDoM0DZBlujDN5nLA759A0IS6dHFtzd6Y0PxDCOMP%2FenDm3X4ubT6KGYhvrR9cfQo2HldNX37ZVH3sKdaRNmJMxw5mx%2F5Cc%2BR4MPuYkb0GOqUB5GTgDSw4D6NBU8ym0e8r06INyPanyA3pMCoAemls9RCp2xmtvi0J15nIwSeh%2FMFcd6FKItdzdeeU72%2FVpYLWLRgGisN0gzEMRwaZXrZ%2B2mpMRI1Q0MzH55I%2Bros8g%2B3SvhsWTq3b%2FWLpC0ClM5vkyoR9og146KUTebw0gFNZAyz%2BYVTKY9tHYKHQyFTxg395b%2BQQEdddDyvKx11Ro1WefmmWInSq&X-Amz-Signature=9af9ec2b46370412a5cb1ed6b2837b92aa1f687e02efae24ea3f36106502bace&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633D6OT5V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIGhuVEVGmeXBv3od6hKyLlz9dR2%2B9MLQChDkAMkyCr%2FGAiEAzSJSOtFiq26xodb%2B7%2FVMClcMP1fwkROsCVAazK6Koygq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGD9muqUhnwsALZT6CrcA8ycek8TbD6TSnEkRbfMiwiRvw3CTnB1cdO1qEMRXuRQnMxw7C6m2%2F1Z7r4jy8a212RHQBiyHnByXlEJY92QGH85OUrpOAuzv0JIN8AVknqaT6lTNUxCSawD0g%2BVWGwSw04s6wDw8Lf93lJszJsUIlPaQFswVjthjLZUcVcBvqENtKj4M9zYaSAPbDVtPh1Pq9oVIW7MG54hj0uDrMUsLIJVtBFkBgvJsn4AGe%2FZYc%2BmKnPt%2FJhL%2FMG3WdrXCa2gYBOVKqwGKryBJFqlI7l9B3yF2PUoNxZ2S5LCfUOQ8NGsEC6TTNJqA00tUbGZhQuwbC4M8WipXEc72Xev4efdi7QWgGpVw9Tb0sxYxgHVjJeJPf6QvQBOPv4yLjXMpkuJRMVGhiv3Lfxr9K8RHdX2A1AEAB5nVwJxiTYOXhlxM%2Bkz77WZPasVJMn0CAHix5e%2FyEAJ6DgTiFrI1tUtQlYB%2FMjhTzGt3sfrF%2FrV6%2BWqSg1eFTJRkdNijWDbInnPkds%2BTCzRvMZU7UktMXXPKGn9Vb0sv2YDoM0DZBlujDN5nLA759A0IS6dHFtzd6Y0PxDCOMP%2FenDm3X4ubT6KGYhvrR9cfQo2HldNX37ZVH3sKdaRNmJMxw5mx%2F5Cc%2BR4MPuYkb0GOqUB5GTgDSw4D6NBU8ym0e8r06INyPanyA3pMCoAemls9RCp2xmtvi0J15nIwSeh%2FMFcd6FKItdzdeeU72%2FVpYLWLRgGisN0gzEMRwaZXrZ%2B2mpMRI1Q0MzH55I%2Bros8g%2B3SvhsWTq3b%2FWLpC0ClM5vkyoR9og146KUTebw0gFNZAyz%2BYVTKY9tHYKHQyFTxg395b%2BQQEdddDyvKx11Ro1WefmmWInSq&X-Amz-Signature=f07fd617e88557fdf2030ba09896eae680866d46bd95f475f15949481b2c95e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633D6OT5V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIGhuVEVGmeXBv3od6hKyLlz9dR2%2B9MLQChDkAMkyCr%2FGAiEAzSJSOtFiq26xodb%2B7%2FVMClcMP1fwkROsCVAazK6Koygq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGD9muqUhnwsALZT6CrcA8ycek8TbD6TSnEkRbfMiwiRvw3CTnB1cdO1qEMRXuRQnMxw7C6m2%2F1Z7r4jy8a212RHQBiyHnByXlEJY92QGH85OUrpOAuzv0JIN8AVknqaT6lTNUxCSawD0g%2BVWGwSw04s6wDw8Lf93lJszJsUIlPaQFswVjthjLZUcVcBvqENtKj4M9zYaSAPbDVtPh1Pq9oVIW7MG54hj0uDrMUsLIJVtBFkBgvJsn4AGe%2FZYc%2BmKnPt%2FJhL%2FMG3WdrXCa2gYBOVKqwGKryBJFqlI7l9B3yF2PUoNxZ2S5LCfUOQ8NGsEC6TTNJqA00tUbGZhQuwbC4M8WipXEc72Xev4efdi7QWgGpVw9Tb0sxYxgHVjJeJPf6QvQBOPv4yLjXMpkuJRMVGhiv3Lfxr9K8RHdX2A1AEAB5nVwJxiTYOXhlxM%2Bkz77WZPasVJMn0CAHix5e%2FyEAJ6DgTiFrI1tUtQlYB%2FMjhTzGt3sfrF%2FrV6%2BWqSg1eFTJRkdNijWDbInnPkds%2BTCzRvMZU7UktMXXPKGn9Vb0sv2YDoM0DZBlujDN5nLA759A0IS6dHFtzd6Y0PxDCOMP%2FenDm3X4ubT6KGYhvrR9cfQo2HldNX37ZVH3sKdaRNmJMxw5mx%2F5Cc%2BR4MPuYkb0GOqUB5GTgDSw4D6NBU8ym0e8r06INyPanyA3pMCoAemls9RCp2xmtvi0J15nIwSeh%2FMFcd6FKItdzdeeU72%2FVpYLWLRgGisN0gzEMRwaZXrZ%2B2mpMRI1Q0MzH55I%2Bros8g%2B3SvhsWTq3b%2FWLpC0ClM5vkyoR9og146KUTebw0gFNZAyz%2BYVTKY9tHYKHQyFTxg395b%2BQQEdddDyvKx11Ro1WefmmWInSq&X-Amz-Signature=f173d930d8bd9e95e88c67a34e6ba11bf8d25bc4e71357b00fb413ea39fe8353&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5VP7VF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDcsG%2FPz7VZV2D1BD7CDrMgOh1c3byZHh6qj3MZaKkU7AIgJIoO8FnyU8B3IoduxWQFtQl93uwrGbe9yWG0UzJ3taAq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDKCaoWsdc7BVlmqk1yrcAziO%2B%2B%2F3lDWn5jUePyq4tN3awppHiskFzX5hhICtv1ZPKwYd1G%2BWEw9Dz2YIHgHuZxIGTDXmKzgH2IvOa3sRooGOLfd3x1tlEBiIfGU4u06j0N%2F%2Fmf0Cy%2FK5Ldoios0y0DbUxliASUptSA%2F83Mt3ksCC78ZYAepuR5wA8AuTa8wEheup%2Fw9TtvSuzag5TE9bQMU5SQS4GtRiX%2BWOxnO0IoWRi2Iv9yEeQ8QelmgwmL0gX1l2%2BLWmkuAlG7hkT600M0cH1%2B9CBg85wLO0VfkuRD0do3YXDGb6G%2BY%2BPlRRDby2zd0Zea4tvBjQbTJQz%2FoJq8OGr5EqUrjwo1JSObk5CeGGWjjMmbY5vbqTlN6QhrEDzmKxuYtDxibDAE6sM6hpt6hQN0Y%2BZlowY884aeQ8sHzBvS%2BFLEoDYE44RK9Swjcst3Zz7zOW7F46WPwnPp0GemVNDD1HcCBro4cEQHLq02ZpaUEqVkq5247NTDyXvRXNrrImuOCDhlJlKpM%2FSult6NB1f6%2B9rpFzSeOlkECgOx%2FN1kr%2FjHEdAAqSAn6cFtW3zvhPJwyCmJ0WkShOfiV2u2ygeLnZcquXffetAbe345HFmAfkMD5PqEv1lNhLfX039YALh08AJXkkKrCyMM6Zkb0GOqUBKGHUmofWHD8VeVgeP9CHk9D1xPfGc5LLAIA19YgY%2BYRnhhdCxIMqyyYoWDg%2BkLTyU2P51Ow4kQj18LDrYZPiroGJsFtWcJlfSbXqTndMfAxmIwkSJzn9XIKy3mdZIR%2BnJzpTXTjtCmbcZIrRiSWW3degGvnzB849olnVDST58Av6xaZmiu%2BBXMMYAvxcYiFwIRu4MGhCUV%2BMa53mKwsXkQA%2FoG%2Bd&X-Amz-Signature=7db7493626f7a5643576d7c960f287f3b3782f1bd74b4fa1e6d7af71c0e0d9fc&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EFS56UW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIH%2F5YEA6SR1fMMOI6jwjeH%2Bb1xzoTJdTyl759NRu%2B87fAiEAzpA2gGbGD6Xyca7oTOzqcAxAihBhjA3SI4mt4WX%2BGkgq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDCo1NbuVLSKz%2FYl5GyrcA6OOB9z%2FjhRFI8WBFFxRcrXagpJtyZ9S%2FYLBzI4oDEkcOp3VcXIfNZaTixoieclI0G9rrcMNdFmyaHogcMypTL6GONKVorO4jpUsaLnq6l%2Bu63tKQ2wN0wSiTkCYlu8L2RVXFnL1zflmksMhymjHXY%2FmpJMatQ8NLs1zFL4Pp2Z5xcN2VZSt7NsvDJ7WgSyrr%2FwKLnDdJ1FbeP65HC7bGIHIuczF7hth6%2B%2B2oN2B%2B8%2FixqOO0x74D5wCR2xEUcF89sdA9g%2F3qq8gvCdW6wsAUJ0kfob2z1twqIcoGoj74pQp%2FlPkXoHaBlZxz65Nvk0p36znaNrhMzZdXYPAiT%2F4DGo3WfnBJbnl5fjJ2EqFPCOZhZ5Ac6X551UIKDlYS19GzO0C9galsaZNyQSoW88jn47FFQuOAnLSNZkT%2Flrv5xPackbmJPiQx%2FxG6T6eaV0iWVc3B44lgFlVyNFjgzotoJ5TMGLTHt9K%2F5uM3%2FcG7YpplptC8h11hRrq5gCgkrz2aD8UxMA0qkIOzvUkaj4lajvWTYthAfYdqBaKhL2jzY2dhxDXHVaGhF1R56%2Bfaio0QGaeYXqPlnIgcbPsKdTil9MLOks%2BUUDPIfB897nI69Gp2HpSow5SbtKmLyRNMOeYkb0GOqUBoWn%2B4RAKaYI7KW6gBRO8wFDnRfVG9kKDbtt20Ske1HIhUbJh1gH%2BE8jYmaY%2BLyOzeGj8VzGP1649hYFU5Z6TyHqWLEi6bZmvABOPdHMZx%2Fi%2B7RJDjZ%2FF%2BFBU0BIllHI%2BLhaTiIsvHe5emOhcpOpyqu0Kg%2F%2BzWcxVXG5nFeMYQ8bND2LcWgeBgJMedawOGElW%2BriMaaRNzTPrWOvYzs7V6oYWZCMq&X-Amz-Signature=4514462176af523d7c06881fa0a7fa64ead1f2799aed078ddfffe52debfc4141&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633D6OT5V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIGhuVEVGmeXBv3od6hKyLlz9dR2%2B9MLQChDkAMkyCr%2FGAiEAzSJSOtFiq26xodb%2B7%2FVMClcMP1fwkROsCVAazK6Koygq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGD9muqUhnwsALZT6CrcA8ycek8TbD6TSnEkRbfMiwiRvw3CTnB1cdO1qEMRXuRQnMxw7C6m2%2F1Z7r4jy8a212RHQBiyHnByXlEJY92QGH85OUrpOAuzv0JIN8AVknqaT6lTNUxCSawD0g%2BVWGwSw04s6wDw8Lf93lJszJsUIlPaQFswVjthjLZUcVcBvqENtKj4M9zYaSAPbDVtPh1Pq9oVIW7MG54hj0uDrMUsLIJVtBFkBgvJsn4AGe%2FZYc%2BmKnPt%2FJhL%2FMG3WdrXCa2gYBOVKqwGKryBJFqlI7l9B3yF2PUoNxZ2S5LCfUOQ8NGsEC6TTNJqA00tUbGZhQuwbC4M8WipXEc72Xev4efdi7QWgGpVw9Tb0sxYxgHVjJeJPf6QvQBOPv4yLjXMpkuJRMVGhiv3Lfxr9K8RHdX2A1AEAB5nVwJxiTYOXhlxM%2Bkz77WZPasVJMn0CAHix5e%2FyEAJ6DgTiFrI1tUtQlYB%2FMjhTzGt3sfrF%2FrV6%2BWqSg1eFTJRkdNijWDbInnPkds%2BTCzRvMZU7UktMXXPKGn9Vb0sv2YDoM0DZBlujDN5nLA759A0IS6dHFtzd6Y0PxDCOMP%2FenDm3X4ubT6KGYhvrR9cfQo2HldNX37ZVH3sKdaRNmJMxw5mx%2F5Cc%2BR4MPuYkb0GOqUB5GTgDSw4D6NBU8ym0e8r06INyPanyA3pMCoAemls9RCp2xmtvi0J15nIwSeh%2FMFcd6FKItdzdeeU72%2FVpYLWLRgGisN0gzEMRwaZXrZ%2B2mpMRI1Q0MzH55I%2Bros8g%2B3SvhsWTq3b%2FWLpC0ClM5vkyoR9og146KUTebw0gFNZAyz%2BYVTKY9tHYKHQyFTxg395b%2BQQEdddDyvKx11Ro1WefmmWInSq&X-Amz-Signature=a7da75078ec590d5d8d2883678a14949e0ee5597109b9ce623b7ae2898aa9cfa&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633D6OT5V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIGhuVEVGmeXBv3od6hKyLlz9dR2%2B9MLQChDkAMkyCr%2FGAiEAzSJSOtFiq26xodb%2B7%2FVMClcMP1fwkROsCVAazK6Koygq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGD9muqUhnwsALZT6CrcA8ycek8TbD6TSnEkRbfMiwiRvw3CTnB1cdO1qEMRXuRQnMxw7C6m2%2F1Z7r4jy8a212RHQBiyHnByXlEJY92QGH85OUrpOAuzv0JIN8AVknqaT6lTNUxCSawD0g%2BVWGwSw04s6wDw8Lf93lJszJsUIlPaQFswVjthjLZUcVcBvqENtKj4M9zYaSAPbDVtPh1Pq9oVIW7MG54hj0uDrMUsLIJVtBFkBgvJsn4AGe%2FZYc%2BmKnPt%2FJhL%2FMG3WdrXCa2gYBOVKqwGKryBJFqlI7l9B3yF2PUoNxZ2S5LCfUOQ8NGsEC6TTNJqA00tUbGZhQuwbC4M8WipXEc72Xev4efdi7QWgGpVw9Tb0sxYxgHVjJeJPf6QvQBOPv4yLjXMpkuJRMVGhiv3Lfxr9K8RHdX2A1AEAB5nVwJxiTYOXhlxM%2Bkz77WZPasVJMn0CAHix5e%2FyEAJ6DgTiFrI1tUtQlYB%2FMjhTzGt3sfrF%2FrV6%2BWqSg1eFTJRkdNijWDbInnPkds%2BTCzRvMZU7UktMXXPKGn9Vb0sv2YDoM0DZBlujDN5nLA759A0IS6dHFtzd6Y0PxDCOMP%2FenDm3X4ubT6KGYhvrR9cfQo2HldNX37ZVH3sKdaRNmJMxw5mx%2F5Cc%2BR4MPuYkb0GOqUB5GTgDSw4D6NBU8ym0e8r06INyPanyA3pMCoAemls9RCp2xmtvi0J15nIwSeh%2FMFcd6FKItdzdeeU72%2FVpYLWLRgGisN0gzEMRwaZXrZ%2B2mpMRI1Q0MzH55I%2Bros8g%2B3SvhsWTq3b%2FWLpC0ClM5vkyoR9og146KUTebw0gFNZAyz%2BYVTKY9tHYKHQyFTxg395b%2BQQEdddDyvKx11Ro1WefmmWInSq&X-Amz-Signature=089bb0ce07f3b2b1dd6b8d869b6e036ec569a7085155fab6afff9272edca4902&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633D6OT5V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIGhuVEVGmeXBv3od6hKyLlz9dR2%2B9MLQChDkAMkyCr%2FGAiEAzSJSOtFiq26xodb%2B7%2FVMClcMP1fwkROsCVAazK6Koygq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGD9muqUhnwsALZT6CrcA8ycek8TbD6TSnEkRbfMiwiRvw3CTnB1cdO1qEMRXuRQnMxw7C6m2%2F1Z7r4jy8a212RHQBiyHnByXlEJY92QGH85OUrpOAuzv0JIN8AVknqaT6lTNUxCSawD0g%2BVWGwSw04s6wDw8Lf93lJszJsUIlPaQFswVjthjLZUcVcBvqENtKj4M9zYaSAPbDVtPh1Pq9oVIW7MG54hj0uDrMUsLIJVtBFkBgvJsn4AGe%2FZYc%2BmKnPt%2FJhL%2FMG3WdrXCa2gYBOVKqwGKryBJFqlI7l9B3yF2PUoNxZ2S5LCfUOQ8NGsEC6TTNJqA00tUbGZhQuwbC4M8WipXEc72Xev4efdi7QWgGpVw9Tb0sxYxgHVjJeJPf6QvQBOPv4yLjXMpkuJRMVGhiv3Lfxr9K8RHdX2A1AEAB5nVwJxiTYOXhlxM%2Bkz77WZPasVJMn0CAHix5e%2FyEAJ6DgTiFrI1tUtQlYB%2FMjhTzGt3sfrF%2FrV6%2BWqSg1eFTJRkdNijWDbInnPkds%2BTCzRvMZU7UktMXXPKGn9Vb0sv2YDoM0DZBlujDN5nLA759A0IS6dHFtzd6Y0PxDCOMP%2FenDm3X4ubT6KGYhvrR9cfQo2HldNX37ZVH3sKdaRNmJMxw5mx%2F5Cc%2BR4MPuYkb0GOqUB5GTgDSw4D6NBU8ym0e8r06INyPanyA3pMCoAemls9RCp2xmtvi0J15nIwSeh%2FMFcd6FKItdzdeeU72%2FVpYLWLRgGisN0gzEMRwaZXrZ%2B2mpMRI1Q0MzH55I%2Bros8g%2B3SvhsWTq3b%2FWLpC0ClM5vkyoR9og146KUTebw0gFNZAyz%2BYVTKY9tHYKHQyFTxg395b%2BQQEdddDyvKx11Ro1WefmmWInSq&X-Amz-Signature=76934410dd8cd9cd4157213a18df8ece615b01ece9004bf256a7fdbb1a65f239&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5XB7R5Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQDlmu0HfAXsDTfAOD7Z6RFRq5gymQFmwcgavhsNso3W9QIhAPcXuhUjOtSOIGFDi8QvRp5ybUqFyZJTdiufM9Fa2TvxKv8DCFcQABoMNjM3NDIzMTgzODA1IgyfEBmp8zPsdl66mCkq3APbl98kuboQwPrPLwNP3vMUgpK5h52dQDOjTk8aADu4YoULV9KYKkrpvzPBevlXI9f2UEXySalw0ff1fZf9k5mgvoQ4Bg3PUpVRrtPriVMxD2BOrfiFHoztajCZSa2KU5cXyGuLhobnPvX71rTrepPiGRf68zn2K12VKwPeJFC6xSjBO56nN6%2B19tk%2BjTXAgqU1bKv2FWHxASiBxn%2FfpQrfHgtPjgvFKIIwQIf7C4nylmdatvAbyRS88cg4Evp3rCN3UhlMLiK0XYsoz9QsmjvGO%2FaOs%2FVfqxFkF7IYveMOT1ix2DVhu%2BZAgcJ0sDjhafybutvIEbxJXZogU2omGcFnajEpNQ38T%2FMHJDvI%2F21riosj3LC65C8o1pema8goDH9YN0qGyE%2Bvpb0d9AYzN7qU8Dr%2BhBcVrPRyskGTJYeU4B%2FAMKOD5fbF6GKC7eqOVCVBWadoVWULAsk12%2FGQq4k6SiG7o8nfWuWlxJ%2FDUt9LgB55SOxicdscLTiFCTbRArsvGI1gzmKgTfg0%2Bhx2tTbHDCN69VW1ICXHavlfTBT0hJ%2FAFTe%2FYi%2B0OviPieKdc%2FDCc0q9H9MDOA5iohTBzzb3dwshM4BNsY2KJveZCNuBlflP5fIc8vGQK7Dk0zCpmZG9BjqkAWxHuNFUeu%2F09YSWAUugv0PIbNZimBqcpdzYGjFL4Q3VUsBVp%2FXJT%2FGFH9fYdUeoMytuV07yW2f5syrDpOVaqBeuk9STVFNOMrydvppo4LV2qctLSFglfRNz5QIQeIuR3V57MkVIJisphgX3mX0waURZM0MuOTAkmlKLWL2fCkuwecaeHUUnbUKPxYyiDQDuj9DfZVFxZ5HZ4kNoG77vFyXOdRBf&X-Amz-Signature=ff030a1491e7a2128155e7566253ab654f2c6bb7fe7030e3216342ec5a7719ca&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW7SPFT7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIDeTMOwyjqW6VRCfgqz8FnuIJUtVMcFOmLd4fsuQ5RxKAiAQeKnV9CyYF7L9WfUZxFAxIBXZHpazxnKSez0rv%2BoA0ir%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMoloShqtgOXLN2IJoKtwD44b00XPMHyKTRkmnRPIU2D8Hft%2B4T%2BWVPjrHhWqOSI1meok38ic%2B5XJtHdChQhDIypP9s3I7x65%2BBY1OTvq4CG6no87QiqyVzekb%2FusiZ5jwS%2B4jfBKIdVj8Yhx%2Bzj3lYI7xEUYGMgLu5xXenLoCFYVdH7JWL%2FmfWMhGifrVMmwJiHv93XVoQZ1H3hTfi5MDEdKV6a2Top0Vby8NExeOh7OoSl%2FQOQDjAx69GMKkj8f2j%2B07WIzogDeO0P2vumfX3JeYlhBIQLVorYaAgtVmc95ftcl1JXci%2B%2BcXiOdBCoa%2BPA5Gs0wjeZsRwvc7IZtTmQqXWOd34pxwfLnO%2BtzMxZJW%2B%2FA%2BJlv2DPGZL4juVRbe1r%2FsJEubLzzB3sbju85bg5KdirjEk87nzZ%2BO%2BX20zTXJj7kO%2F6o74n1cpN6IvMJDyIU49Gv3EBx5POdpDPf5LgGW40cz7CgIo93WECnwZ0C7o23Tne4xL2Ba89zwsxwJjXeiuWVfWUxMvWLvCxDZBKN5BpSWshwGCJEulIIwXkBumEUwC3WHObKlMJsuVWpYXRRdjMreOkSGS108R1ddf4sZq7YsGx%2B6EqUqsB%2BCY7ZjATJu7Cs1iq6SyU5yKni6MxgvtKWqBaR40QAwkpmRvQY6pgHZ89p%2FG7a%2BwcsrDuvKmT6H%2Fbzkw0VY2PKvbRd4GGCHA7x20lU3XSOiPZ9v5wZ1cCaZM41arM5CKc%2Buqw0uWU8K0RzVIrMh6CxQYbbIRnXyKkcV70WL%2FvW5R8Xdlk3LMPIglnH0jVfPjBExS%2FjrzhbWtIX0WEO8cS%2BwLdKy7sOX2KSnf7EdT94vaEzzgSanc9qNMychqcMejye73XGT%2FgNLpfP4k73M&X-Amz-Signature=e526aa9ae3f0a410c5326e33e61264db039f3fa4ff6d67bf1827909e0d0c6a6b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UZZTXHL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIEVQLDkZZQ1VahspDfeiYxLHctO5JTeTC4y4bQ8vMt6DAiBFYBId%2Fr3DRzeA7WR0WwX5RLx7Yjhf5wuKnhspsmGOmyr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMgKW6HVCmkslu5qaGKtwD31kSEuD1dRCpxNlsCIiZndf4FoazQmW0TvPNyJQHDrlNSIH%2FtWsoKF1GoY4uePSZcbKHNwxLTBBcw5x6rDvEYINMRgdUfIonyc1OgBE%2Bezh2a6f%2FEs5vf%2F2rILQZptzQrSuCHf9JUHOVvZOg2r9p7HyFuACqO%2Bpp6ZD2dQu70c5rlpbbAbuuDj1Kx1HC6lU2alxmh0VFAQVLZqzilnJ4j%2Bdpxz5WBRTF0yr931JYf2Pq%2FMq1a8Bd3o2nKAgJpW9naAQdXOyTp%2Fo1xckdHxQ9COq64eDAjQRUsLB1WIS3vSIdGYLoIlItU29o2vjGtL5nMYcupXrZlq5XuautbJVbI41izUwAHMFT7waD5O6%2BKLGlcfie%2BMoXOjZy0cRvegNUg5A4tLeLj6U5LRjjDnHcqfAsFvbl4ih6yYruwEOe9wLvoWf6iGNxLjyxKise5UbyGt3gENXWB1w30kVekHZcrzVFfNbo8khSc%2BECaQuqu%2F7MwIyzRZRxPOVbAaX8g3Gt9XfKKy4GdPbghZL3vcOlIbBXx%2BI6L7YVAzVz%2FTbu8YTPc4XqnwVOJqZ8h%2FvZN4BVEfdl8PQjM4qT7D0PmyyUCZMGKd9wr74Z%2FB09SauzDuAu3eMsbFrMBorDzaAwoJmRvQY6pgGHufF2SfWBx%2FRJtm7dNwQcqQ%2FzQfM7EmSyOkVOO3VjStIzcbBXd4MyQWVUFEOA%2B0OmopfWyIJuYib6sOmGd%2BxeQKT3qZIy4hTcJhQCr0zFYECvde%2FdT%2FO937Wlwpt94e24fl2W%2FwaK7yaNyllTaaLrPjpfPGMsOm9iJYcsadRg10TeHaH%2FT2U3%2Ba8C8SYksR9pRghOa6edYhWsdeWYjJkK3LW%2BnE0a&X-Amz-Signature=d1dbfa5f404e98aa5762087ead38000a3d2a108ef1f633cf504f9fa7178d1a6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X64BP6RA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIDDwrXy1EL%2B0mM1oyivdX8GYJUx8sK0X7sXOZM06SgWIAiAmMoPtlNX90GupYmGo3a8unaY1kIkRrPvBQ2CwA28sVSr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMOAzUcJJcBd%2B%2Bm54RKtwD5A3PnAPK7Sv7YEd0xf3O92MWZQDKyWHAKLBxv%2FwOPu7sA%2BluR3SUxAepJ53Rz3GOqjfRz%2BtIU3X428cNC6zxExRT9Nc0JkCzpCfk92w7lYShrY0%2BFiKkKpozBS2iUgeN%2FcPy8wFWOBs5FjP%2FY41FPiz1nOD5tFYt545%2FKR7YasUV0nFSqA2PknSlET6IQDgcr6Hy1Oyaf6CYUORBkg6m4iKgmVA0rBHBgKqavg9m2IXrPKbnzSTclZ8pQChbi%2FztJDEw1i5ducChVeX%2Bzg0dvAZiMTV43YR6N3kZ2IUSsX8Jmd4tmi%2FuVGVctezdmEoimWW2CrtDXDgL%2BYUBInrtuytEE%2Bzq2KvDZvMZc2K34E2OHyc5EWjSHYj7SFida6Ioxs3WExhQCCrjJcWzZAP2EY1wcJZWPhSIulXRGne40gvEUckeJOkzH%2BnvFAGSH2AOa%2FkoJtforXmqW3rjoO22U4yc2%2B7BuS371%2FHRX%2FtjA%2FFbk5qQgbt%2ByWWsFgTM90LsDeR6%2BPc4Ct%2BrP4ny%2FLmR0oRfe76T5xeGJ6ZWVpsJvUCrPjjrus8HSu0sCmK54FcN4EPIk1NfFlwBQQwGMy9Ln31L6a3K47osh7iUERXEENhEpAvNrw1OVC%2BllcAwt5mRvQY6pgFwRomElBCStspx7dqoQg%2B6jwc4y5j8Ix7O%2Br5F1fIcqjg0I1IpK1HrOJmba2QwR0Y3BJilgSufI76nxj6wRfC8CXHZGV8JC4sGjjIeAJMsaAu7Jv%2Faqr5z6SBPV85YoHaYpdPFdS2RDnmwg0%2BapP1F8pjZsegBbcITAYvAOBfgwPg8PDCkNJnJckos8lx1jBfg65GCmfrxTvuFPas9bdxrge%2BwXs39&X-Amz-Signature=5841ff5cf852f828205dab6e04be8229b952be338bf3c8916654693f1f6659cb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X64BP6RA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIDDwrXy1EL%2B0mM1oyivdX8GYJUx8sK0X7sXOZM06SgWIAiAmMoPtlNX90GupYmGo3a8unaY1kIkRrPvBQ2CwA28sVSr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMOAzUcJJcBd%2B%2Bm54RKtwD5A3PnAPK7Sv7YEd0xf3O92MWZQDKyWHAKLBxv%2FwOPu7sA%2BluR3SUxAepJ53Rz3GOqjfRz%2BtIU3X428cNC6zxExRT9Nc0JkCzpCfk92w7lYShrY0%2BFiKkKpozBS2iUgeN%2FcPy8wFWOBs5FjP%2FY41FPiz1nOD5tFYt545%2FKR7YasUV0nFSqA2PknSlET6IQDgcr6Hy1Oyaf6CYUORBkg6m4iKgmVA0rBHBgKqavg9m2IXrPKbnzSTclZ8pQChbi%2FztJDEw1i5ducChVeX%2Bzg0dvAZiMTV43YR6N3kZ2IUSsX8Jmd4tmi%2FuVGVctezdmEoimWW2CrtDXDgL%2BYUBInrtuytEE%2Bzq2KvDZvMZc2K34E2OHyc5EWjSHYj7SFida6Ioxs3WExhQCCrjJcWzZAP2EY1wcJZWPhSIulXRGne40gvEUckeJOkzH%2BnvFAGSH2AOa%2FkoJtforXmqW3rjoO22U4yc2%2B7BuS371%2FHRX%2FtjA%2FFbk5qQgbt%2ByWWsFgTM90LsDeR6%2BPc4Ct%2BrP4ny%2FLmR0oRfe76T5xeGJ6ZWVpsJvUCrPjjrus8HSu0sCmK54FcN4EPIk1NfFlwBQQwGMy9Ln31L6a3K47osh7iUERXEENhEpAvNrw1OVC%2BllcAwt5mRvQY6pgFwRomElBCStspx7dqoQg%2B6jwc4y5j8Ix7O%2Br5F1fIcqjg0I1IpK1HrOJmba2QwR0Y3BJilgSufI76nxj6wRfC8CXHZGV8JC4sGjjIeAJMsaAu7Jv%2Faqr5z6SBPV85YoHaYpdPFdS2RDnmwg0%2BapP1F8pjZsegBbcITAYvAOBfgwPg8PDCkNJnJckos8lx1jBfg65GCmfrxTvuFPas9bdxrge%2BwXs39&X-Amz-Signature=7c9fd98736f78e69809be1b3050760e25e8cfaaf0cc75dd1b4e1a9b99c6eee22&X-Amz-SignedHeaders=host&x-id=GetObject)

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
