

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XI4ZR3OT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNs3VkHA3vzPYFN%2FFd8z%2B%2BMLOz6JeRkP4pwYLHmp6BYAIhAO0hHTgoOjTtDENlhbUZ7i3wb3kv%2Bze%2FFl%2FVGnWPg3pcKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpZoskKrMjrxXi0cUq3AOt9vS2tuUDaaZ7nRzGv%2Blq31vsGbAnzAmCHJ%2FKaK7vqqcAX95uKHe2pBjbnqWQrBG8NHp%2BPMvKQ1mkZ3BvEOkN4VK2bAETcOdWzMVZp6SWy336L%2BAu%2BJcRxkpdL%2BC42ZNcu1HihbV1ZHqOL1HLKCFnGVDhvzwzXTMV39%2B1yEvgn6eU%2FtrjHo%2FJaAlaDJUeZgOYxKUSH0qqqJGM90l6hVcp%2BuJg1cXchzfk3lrlsme21WqHoD%2BlqjHft%2F7qPNjpFpowykOfLSGYF3J9Khn%2FqndJPbtxWvYxEB0Fbrb0uqCq4Nd7JW%2BHHZb4V3OheboYAiezoz40mZ8onKGCrarUZbnmS4e1ggvqobijpEyp%2BW2m90ONsTU%2FHnI8lf9xiOKEvAS8XK13uEjhGY2B%2FjMOZ96iXIcqQG2qKA%2FC95L%2FAC1ESmfIGjTkcTyp3sMTi16FY8UUSh9dg4DypDKQdv%2F1wMY4R4qcAHtUPfoA1Yl7YVMtDnhnkJvUqBJANEixpf1Tu0n2FzKylMPXogBlJeZFpMWwGI%2Fx6UghIy3nX5I62iDnrYOkibIet6KnCk7f7ez2jgj7PSBU7iQQHSS0TPsdr8hyAkSARoOiuE2vQBEUGj8RcIz%2B9CrfnDK2D2bLtzD14f68BjqkAaheuRmOKwR%2FyGuQVxYTj1O9UePJfhlKpu6PVODbxNgjCggak8l%2B3d0PaGp10WpwsL83YPguZfwdlTdwcP%2FuQAkJP3Dvtp2aEwjNL1c63S5jJTx66L4BAt60R5E0oztyQGlqdjCaFBo7fvUhPQTa2q1RquvSdT2ZAHtBalnFBdMphz4%2Fo5RDR%2FCfrc85NeWpkfRylFgYWZYDg3Yz38ZoLG1KiHo%2B&X-Amz-Signature=a19b06f50efca84d80b35b4669c48dc85d8db7c51b745a1804ca487474e1e747&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XI4ZR3OT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNs3VkHA3vzPYFN%2FFd8z%2B%2BMLOz6JeRkP4pwYLHmp6BYAIhAO0hHTgoOjTtDENlhbUZ7i3wb3kv%2Bze%2FFl%2FVGnWPg3pcKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpZoskKrMjrxXi0cUq3AOt9vS2tuUDaaZ7nRzGv%2Blq31vsGbAnzAmCHJ%2FKaK7vqqcAX95uKHe2pBjbnqWQrBG8NHp%2BPMvKQ1mkZ3BvEOkN4VK2bAETcOdWzMVZp6SWy336L%2BAu%2BJcRxkpdL%2BC42ZNcu1HihbV1ZHqOL1HLKCFnGVDhvzwzXTMV39%2B1yEvgn6eU%2FtrjHo%2FJaAlaDJUeZgOYxKUSH0qqqJGM90l6hVcp%2BuJg1cXchzfk3lrlsme21WqHoD%2BlqjHft%2F7qPNjpFpowykOfLSGYF3J9Khn%2FqndJPbtxWvYxEB0Fbrb0uqCq4Nd7JW%2BHHZb4V3OheboYAiezoz40mZ8onKGCrarUZbnmS4e1ggvqobijpEyp%2BW2m90ONsTU%2FHnI8lf9xiOKEvAS8XK13uEjhGY2B%2FjMOZ96iXIcqQG2qKA%2FC95L%2FAC1ESmfIGjTkcTyp3sMTi16FY8UUSh9dg4DypDKQdv%2F1wMY4R4qcAHtUPfoA1Yl7YVMtDnhnkJvUqBJANEixpf1Tu0n2FzKylMPXogBlJeZFpMWwGI%2Fx6UghIy3nX5I62iDnrYOkibIet6KnCk7f7ez2jgj7PSBU7iQQHSS0TPsdr8hyAkSARoOiuE2vQBEUGj8RcIz%2B9CrfnDK2D2bLtzD14f68BjqkAaheuRmOKwR%2FyGuQVxYTj1O9UePJfhlKpu6PVODbxNgjCggak8l%2B3d0PaGp10WpwsL83YPguZfwdlTdwcP%2FuQAkJP3Dvtp2aEwjNL1c63S5jJTx66L4BAt60R5E0oztyQGlqdjCaFBo7fvUhPQTa2q1RquvSdT2ZAHtBalnFBdMphz4%2Fo5RDR%2FCfrc85NeWpkfRylFgYWZYDg3Yz38ZoLG1KiHo%2B&X-Amz-Signature=5e674fae44c40c59ebf802d973635054f3e6424c3370d04fa65806cab0b38a48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XI4ZR3OT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNs3VkHA3vzPYFN%2FFd8z%2B%2BMLOz6JeRkP4pwYLHmp6BYAIhAO0hHTgoOjTtDENlhbUZ7i3wb3kv%2Bze%2FFl%2FVGnWPg3pcKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpZoskKrMjrxXi0cUq3AOt9vS2tuUDaaZ7nRzGv%2Blq31vsGbAnzAmCHJ%2FKaK7vqqcAX95uKHe2pBjbnqWQrBG8NHp%2BPMvKQ1mkZ3BvEOkN4VK2bAETcOdWzMVZp6SWy336L%2BAu%2BJcRxkpdL%2BC42ZNcu1HihbV1ZHqOL1HLKCFnGVDhvzwzXTMV39%2B1yEvgn6eU%2FtrjHo%2FJaAlaDJUeZgOYxKUSH0qqqJGM90l6hVcp%2BuJg1cXchzfk3lrlsme21WqHoD%2BlqjHft%2F7qPNjpFpowykOfLSGYF3J9Khn%2FqndJPbtxWvYxEB0Fbrb0uqCq4Nd7JW%2BHHZb4V3OheboYAiezoz40mZ8onKGCrarUZbnmS4e1ggvqobijpEyp%2BW2m90ONsTU%2FHnI8lf9xiOKEvAS8XK13uEjhGY2B%2FjMOZ96iXIcqQG2qKA%2FC95L%2FAC1ESmfIGjTkcTyp3sMTi16FY8UUSh9dg4DypDKQdv%2F1wMY4R4qcAHtUPfoA1Yl7YVMtDnhnkJvUqBJANEixpf1Tu0n2FzKylMPXogBlJeZFpMWwGI%2Fx6UghIy3nX5I62iDnrYOkibIet6KnCk7f7ez2jgj7PSBU7iQQHSS0TPsdr8hyAkSARoOiuE2vQBEUGj8RcIz%2B9CrfnDK2D2bLtzD14f68BjqkAaheuRmOKwR%2FyGuQVxYTj1O9UePJfhlKpu6PVODbxNgjCggak8l%2B3d0PaGp10WpwsL83YPguZfwdlTdwcP%2FuQAkJP3Dvtp2aEwjNL1c63S5jJTx66L4BAt60R5E0oztyQGlqdjCaFBo7fvUhPQTa2q1RquvSdT2ZAHtBalnFBdMphz4%2Fo5RDR%2FCfrc85NeWpkfRylFgYWZYDg3Yz38ZoLG1KiHo%2B&X-Amz-Signature=cf1aa2943cfa3f6c89b7dea7ba26cb4682264fa287d5b3b214fd15f28f3b356a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643B656FN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEj4Ka0T8GQNSLXSHLqXjzk61xOb6Pk1EFCPF%2FCrQJAwIhANAmdRV7dW2%2BlwC4ch4E126a2J%2F8DzcWAAxP%2BHcRkKKnKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxrhSb%2BIg3V9A35xUq3APyn6gWWOuSt38UhVXdFpcLiWGkC7pPjcSyq3T1BH396DFNYchfCuFo3a%2FhOkDacgDKMAcY%2FO%2FJQ0%2Bw%2BSpFCggfuwd3cHA4aIUrK1dvY2Zf7Ncpot2iUvn60%2BZYlryLbD6IkCTtoQiiPRsZhSZmN7GmeHM7KvQ4unmQTWzL8GBSv1RiMqQWjGesD4IlgAgtmqG1QOwouwe2NHwFnv20Zg1QTPbHI865T0l19xP%2BmKimhwqplRCuFYde1ZAF81k37c0h29cR7XCR9%2FGBRkqJQRD5Keu8Kiwe85oyxXDq0UDdPMDLRqxBUFo1TYmahr0DNE4MrnxmienPymhKCozWhkTENWDB4tkH6WM35d2cKA4xy3Y%2BVZDGLY09K%2B1Mb4XnXm52QKeFM0ta7QrnS3rwL1uAgW%2F8FhHU2imOrF5ExsQv7e9g8YO13uENjF5WM9yZgnZCxwj88eSO2jbChRiuiag2DLt0MOHIm5AyRFFs1LyOvfoypBTTw7rD7x8pGAIzSi7WznVHIcwUovFcE%2BjI6yOtvsTdty9w9cg7JuQ96UUxa14U02pBb2Mz%2FfFxGar46lJyMng8ljVfn9U1Ao9Y5LpL5Od0OihH1AqNDHCUdR7Fej7kPQL%2FBVYyeLqRBDD24f68BjqkAQHAQP%2FA0l%2FYsQxljdNCrfGBjWCEwAtwGO9ThLbPninbjk5pG79JqF%2BmtSTuZwS98Qk6tYS%2BLZCdsrfYIEuSns5RICJ5lRTcnBpNcLiVK5VkgHS7vKEMeFrU0HacCUhAX5VoWn8qA8ksbhK6TrpS25%2BL%2BP%2BY0LuRs833XDIPtdh9ZyMuSXbqEDXVdGP%2FK2Fj6Tq4wZbjYDJvEZljo9jaVGtZlrhE&X-Amz-Signature=0a08546c5165ee41d530e23c9574e32be1af210a36bc2a0ef5ae37dbddb43f1f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643B656FN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEj4Ka0T8GQNSLXSHLqXjzk61xOb6Pk1EFCPF%2FCrQJAwIhANAmdRV7dW2%2BlwC4ch4E126a2J%2F8DzcWAAxP%2BHcRkKKnKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxrhSb%2BIg3V9A35xUq3APyn6gWWOuSt38UhVXdFpcLiWGkC7pPjcSyq3T1BH396DFNYchfCuFo3a%2FhOkDacgDKMAcY%2FO%2FJQ0%2Bw%2BSpFCggfuwd3cHA4aIUrK1dvY2Zf7Ncpot2iUvn60%2BZYlryLbD6IkCTtoQiiPRsZhSZmN7GmeHM7KvQ4unmQTWzL8GBSv1RiMqQWjGesD4IlgAgtmqG1QOwouwe2NHwFnv20Zg1QTPbHI865T0l19xP%2BmKimhwqplRCuFYde1ZAF81k37c0h29cR7XCR9%2FGBRkqJQRD5Keu8Kiwe85oyxXDq0UDdPMDLRqxBUFo1TYmahr0DNE4MrnxmienPymhKCozWhkTENWDB4tkH6WM35d2cKA4xy3Y%2BVZDGLY09K%2B1Mb4XnXm52QKeFM0ta7QrnS3rwL1uAgW%2F8FhHU2imOrF5ExsQv7e9g8YO13uENjF5WM9yZgnZCxwj88eSO2jbChRiuiag2DLt0MOHIm5AyRFFs1LyOvfoypBTTw7rD7x8pGAIzSi7WznVHIcwUovFcE%2BjI6yOtvsTdty9w9cg7JuQ96UUxa14U02pBb2Mz%2FfFxGar46lJyMng8ljVfn9U1Ao9Y5LpL5Od0OihH1AqNDHCUdR7Fej7kPQL%2FBVYyeLqRBDD24f68BjqkAQHAQP%2FA0l%2FYsQxljdNCrfGBjWCEwAtwGO9ThLbPninbjk5pG79JqF%2BmtSTuZwS98Qk6tYS%2BLZCdsrfYIEuSns5RICJ5lRTcnBpNcLiVK5VkgHS7vKEMeFrU0HacCUhAX5VoWn8qA8ksbhK6TrpS25%2BL%2BP%2BY0LuRs833XDIPtdh9ZyMuSXbqEDXVdGP%2FK2Fj6Tq4wZbjYDJvEZljo9jaVGtZlrhE&X-Amz-Signature=c5e8b6b74514ad3526aff2735c7a897c41fd8e02307a2f7fcfbd62fa0e4784c7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643B656FN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEj4Ka0T8GQNSLXSHLqXjzk61xOb6Pk1EFCPF%2FCrQJAwIhANAmdRV7dW2%2BlwC4ch4E126a2J%2F8DzcWAAxP%2BHcRkKKnKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxrhSb%2BIg3V9A35xUq3APyn6gWWOuSt38UhVXdFpcLiWGkC7pPjcSyq3T1BH396DFNYchfCuFo3a%2FhOkDacgDKMAcY%2FO%2FJQ0%2Bw%2BSpFCggfuwd3cHA4aIUrK1dvY2Zf7Ncpot2iUvn60%2BZYlryLbD6IkCTtoQiiPRsZhSZmN7GmeHM7KvQ4unmQTWzL8GBSv1RiMqQWjGesD4IlgAgtmqG1QOwouwe2NHwFnv20Zg1QTPbHI865T0l19xP%2BmKimhwqplRCuFYde1ZAF81k37c0h29cR7XCR9%2FGBRkqJQRD5Keu8Kiwe85oyxXDq0UDdPMDLRqxBUFo1TYmahr0DNE4MrnxmienPymhKCozWhkTENWDB4tkH6WM35d2cKA4xy3Y%2BVZDGLY09K%2B1Mb4XnXm52QKeFM0ta7QrnS3rwL1uAgW%2F8FhHU2imOrF5ExsQv7e9g8YO13uENjF5WM9yZgnZCxwj88eSO2jbChRiuiag2DLt0MOHIm5AyRFFs1LyOvfoypBTTw7rD7x8pGAIzSi7WznVHIcwUovFcE%2BjI6yOtvsTdty9w9cg7JuQ96UUxa14U02pBb2Mz%2FfFxGar46lJyMng8ljVfn9U1Ao9Y5LpL5Od0OihH1AqNDHCUdR7Fej7kPQL%2FBVYyeLqRBDD24f68BjqkAQHAQP%2FA0l%2FYsQxljdNCrfGBjWCEwAtwGO9ThLbPninbjk5pG79JqF%2BmtSTuZwS98Qk6tYS%2BLZCdsrfYIEuSns5RICJ5lRTcnBpNcLiVK5VkgHS7vKEMeFrU0HacCUhAX5VoWn8qA8ksbhK6TrpS25%2BL%2BP%2BY0LuRs833XDIPtdh9ZyMuSXbqEDXVdGP%2FK2Fj6Tq4wZbjYDJvEZljo9jaVGtZlrhE&X-Amz-Signature=abab0ec666b68c30dc8fa9525d544ff539fc9e024519fd4f9b4500c9bcc4e52a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643B656FN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEj4Ka0T8GQNSLXSHLqXjzk61xOb6Pk1EFCPF%2FCrQJAwIhANAmdRV7dW2%2BlwC4ch4E126a2J%2F8DzcWAAxP%2BHcRkKKnKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxrhSb%2BIg3V9A35xUq3APyn6gWWOuSt38UhVXdFpcLiWGkC7pPjcSyq3T1BH396DFNYchfCuFo3a%2FhOkDacgDKMAcY%2FO%2FJQ0%2Bw%2BSpFCggfuwd3cHA4aIUrK1dvY2Zf7Ncpot2iUvn60%2BZYlryLbD6IkCTtoQiiPRsZhSZmN7GmeHM7KvQ4unmQTWzL8GBSv1RiMqQWjGesD4IlgAgtmqG1QOwouwe2NHwFnv20Zg1QTPbHI865T0l19xP%2BmKimhwqplRCuFYde1ZAF81k37c0h29cR7XCR9%2FGBRkqJQRD5Keu8Kiwe85oyxXDq0UDdPMDLRqxBUFo1TYmahr0DNE4MrnxmienPymhKCozWhkTENWDB4tkH6WM35d2cKA4xy3Y%2BVZDGLY09K%2B1Mb4XnXm52QKeFM0ta7QrnS3rwL1uAgW%2F8FhHU2imOrF5ExsQv7e9g8YO13uENjF5WM9yZgnZCxwj88eSO2jbChRiuiag2DLt0MOHIm5AyRFFs1LyOvfoypBTTw7rD7x8pGAIzSi7WznVHIcwUovFcE%2BjI6yOtvsTdty9w9cg7JuQ96UUxa14U02pBb2Mz%2FfFxGar46lJyMng8ljVfn9U1Ao9Y5LpL5Od0OihH1AqNDHCUdR7Fej7kPQL%2FBVYyeLqRBDD24f68BjqkAQHAQP%2FA0l%2FYsQxljdNCrfGBjWCEwAtwGO9ThLbPninbjk5pG79JqF%2BmtSTuZwS98Qk6tYS%2BLZCdsrfYIEuSns5RICJ5lRTcnBpNcLiVK5VkgHS7vKEMeFrU0HacCUhAX5VoWn8qA8ksbhK6TrpS25%2BL%2BP%2BY0LuRs833XDIPtdh9ZyMuSXbqEDXVdGP%2FK2Fj6Tq4wZbjYDJvEZljo9jaVGtZlrhE&X-Amz-Signature=c0d84f260c60ff6a14bff302f7ca8af2f261411c78d484cd9ad6b98a6a68cb65&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643B656FN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEj4Ka0T8GQNSLXSHLqXjzk61xOb6Pk1EFCPF%2FCrQJAwIhANAmdRV7dW2%2BlwC4ch4E126a2J%2F8DzcWAAxP%2BHcRkKKnKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxrhSb%2BIg3V9A35xUq3APyn6gWWOuSt38UhVXdFpcLiWGkC7pPjcSyq3T1BH396DFNYchfCuFo3a%2FhOkDacgDKMAcY%2FO%2FJQ0%2Bw%2BSpFCggfuwd3cHA4aIUrK1dvY2Zf7Ncpot2iUvn60%2BZYlryLbD6IkCTtoQiiPRsZhSZmN7GmeHM7KvQ4unmQTWzL8GBSv1RiMqQWjGesD4IlgAgtmqG1QOwouwe2NHwFnv20Zg1QTPbHI865T0l19xP%2BmKimhwqplRCuFYde1ZAF81k37c0h29cR7XCR9%2FGBRkqJQRD5Keu8Kiwe85oyxXDq0UDdPMDLRqxBUFo1TYmahr0DNE4MrnxmienPymhKCozWhkTENWDB4tkH6WM35d2cKA4xy3Y%2BVZDGLY09K%2B1Mb4XnXm52QKeFM0ta7QrnS3rwL1uAgW%2F8FhHU2imOrF5ExsQv7e9g8YO13uENjF5WM9yZgnZCxwj88eSO2jbChRiuiag2DLt0MOHIm5AyRFFs1LyOvfoypBTTw7rD7x8pGAIzSi7WznVHIcwUovFcE%2BjI6yOtvsTdty9w9cg7JuQ96UUxa14U02pBb2Mz%2FfFxGar46lJyMng8ljVfn9U1Ao9Y5LpL5Od0OihH1AqNDHCUdR7Fej7kPQL%2FBVYyeLqRBDD24f68BjqkAQHAQP%2FA0l%2FYsQxljdNCrfGBjWCEwAtwGO9ThLbPninbjk5pG79JqF%2BmtSTuZwS98Qk6tYS%2BLZCdsrfYIEuSns5RICJ5lRTcnBpNcLiVK5VkgHS7vKEMeFrU0HacCUhAX5VoWn8qA8ksbhK6TrpS25%2BL%2BP%2BY0LuRs833XDIPtdh9ZyMuSXbqEDXVdGP%2FK2Fj6Tq4wZbjYDJvEZljo9jaVGtZlrhE&X-Amz-Signature=4aabce99d2b4061a576900f4e50173288a0abb2f3bb40faa8e03a54a4ae45375&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643B656FN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEj4Ka0T8GQNSLXSHLqXjzk61xOb6Pk1EFCPF%2FCrQJAwIhANAmdRV7dW2%2BlwC4ch4E126a2J%2F8DzcWAAxP%2BHcRkKKnKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxrhSb%2BIg3V9A35xUq3APyn6gWWOuSt38UhVXdFpcLiWGkC7pPjcSyq3T1BH396DFNYchfCuFo3a%2FhOkDacgDKMAcY%2FO%2FJQ0%2Bw%2BSpFCggfuwd3cHA4aIUrK1dvY2Zf7Ncpot2iUvn60%2BZYlryLbD6IkCTtoQiiPRsZhSZmN7GmeHM7KvQ4unmQTWzL8GBSv1RiMqQWjGesD4IlgAgtmqG1QOwouwe2NHwFnv20Zg1QTPbHI865T0l19xP%2BmKimhwqplRCuFYde1ZAF81k37c0h29cR7XCR9%2FGBRkqJQRD5Keu8Kiwe85oyxXDq0UDdPMDLRqxBUFo1TYmahr0DNE4MrnxmienPymhKCozWhkTENWDB4tkH6WM35d2cKA4xy3Y%2BVZDGLY09K%2B1Mb4XnXm52QKeFM0ta7QrnS3rwL1uAgW%2F8FhHU2imOrF5ExsQv7e9g8YO13uENjF5WM9yZgnZCxwj88eSO2jbChRiuiag2DLt0MOHIm5AyRFFs1LyOvfoypBTTw7rD7x8pGAIzSi7WznVHIcwUovFcE%2BjI6yOtvsTdty9w9cg7JuQ96UUxa14U02pBb2Mz%2FfFxGar46lJyMng8ljVfn9U1Ao9Y5LpL5Od0OihH1AqNDHCUdR7Fej7kPQL%2FBVYyeLqRBDD24f68BjqkAQHAQP%2FA0l%2FYsQxljdNCrfGBjWCEwAtwGO9ThLbPninbjk5pG79JqF%2BmtSTuZwS98Qk6tYS%2BLZCdsrfYIEuSns5RICJ5lRTcnBpNcLiVK5VkgHS7vKEMeFrU0HacCUhAX5VoWn8qA8ksbhK6TrpS25%2BL%2BP%2BY0LuRs833XDIPtdh9ZyMuSXbqEDXVdGP%2FK2Fj6Tq4wZbjYDJvEZljo9jaVGtZlrhE&X-Amz-Signature=fac432c59f40c37ff250c1ae90e8dd78930b27949b94ec54248d26d9de00ea73&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGRC2BLN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICYuFjQ6kDkewV44DsFNIEP8S1gc0e7UO7PbtaibTl7QAiA2dhSPRLcuc27yjmxc5BYRkNYJzhQD78zZ0KxkacxbwSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMR9suInktp%2BJkvB%2B%2BKtwDKWm7vBG5%2BKEKFzCYm8Rwx1KzAT3RjqhKaZ6vTiKcHOBYT0zUHXAvmERveWnZ%2B%2FOzwAK1pjtRGqrjz4UutR0Mov%2F9snAWHZfqT2YYpBYIDqFTBAsiXWPvcJkJGNf%2BNHCaf4ulW2GTACG3oAWa0PSk%2Fti6eaCPF9kC3IxSSKiQ05ZMotQxx39oWg3Bp3SZMnSReC%2Bc6PPHiwW2oj%2Bja5t7EdF%2FMviAyx9WTPCrfnQWrN0VinopjOdT8UUaRblD9Sx%2FSp5Smb5Vvg1aSP%2FtNUJngjgQAcPpG4lD9NpNB2hh7OOVyC7LHFdw1o%2BcGvqB%2BVRa1zLHC68T6AlxQDzEq7rQzzakqftrBNoWcQYFoVmqLX9MPMfAcludmr%2FFHjD5teKkdUrD%2BfCgWI%2B4AxZtfmHmASrmAWibOlWDDhYa1BIWfmQPoNsWAewqC6i2OZlMW1bPEmnMnUpmLkmQigBkzQx4S%2BRfT3spiq7gfhgtfi%2BRCyRJqvNLpRI4ZJM7axvCqbEYwcpeN0InQKOyh6mf0iXKBDbz5geibGh5ugzMQGMi98eBQN7AQeYPMZQYPh2FKQYJC21S5%2B9LJ9fzo2w4NIY1rn8A1H0Agn74nH%2FIt8U7LquliTbW1s5xUihl%2FWww0N3%2BvAY6pgEIE8ta5NkxS90S0XONsztMesyqDtCqF1IIgOKQVPi%2Ff8I0MT33DP5TeAFCWCOQ%2FgUfzTLUuwxT4H1xlUBUphZfhA59tiH2NWq6bxeVQGKBowQQQ9wef27c2PF89miIB91x0TxqlQAMVhKZigJyNuavB8OJw4hbDgbMawbC36KIS3eA4hX2b8cYo6DliHkKAxxVlGnRY32ZG1xtou6RK%2F7CI3QNzM5B&X-Amz-Signature=7224ca79256254fdab99383a1aafb2635b0bc38ee2aae9b6a60f7d6929a3afd8&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625IC7GHO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFkfifwCDBEswiWxTu3Sio0oz8Y5X%2BOJ6xNwRJ2bvmxyAiEA6Zxjh4TeeL3sLI8nT9DxgkCZMxdQtO9Y6ikjYFn%2B1o8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF5COzN%2BbjxaaDp9nSrcA8dzRSIL3gjM1wKFhxukRQz2yCUoVDNUjYFRGQHRRNfdNjzevP9dp9WyJWLWRAof0fVJ2WpF%2BdQkGgxxGr%2FN6WhsJMueDPALUKIC96vy0Sduw5NTdS4V5389W7nQFisAtQuTEJ%2BT5pP1e4TT%2BVfmiL8pRonZII5gP1XOM04EjVi8%2FS5M%2BJTJZ1DnNF0Z8oj2dLo9SCNFaTA3AwG44WSi%2FEDiLIOeko85uSzTJxAF%2Fuw0J%2B55VlidmLINAbBJXHo1XLmllks4R03Pj22O94IfIG1jFqktP2%2FlnlxpJL5wJedRb1BvH0hmT2f65zVT6SOYxv%2FmrqLZ8DaawHM764XzujMX4ULZxfpAMpCOOTcBpWphesYp3VfZ6TybgU%2FFlWm%2BnczsQXVVF1iO0B7GUuOY1ZsR3qaAQj74zQAfwx5NiGpuP9F0fkMmuZLKZKPxq5asMRCXmkPHoiGEu5%2FXXPXptCNBRQhnnghwWYvSyZ3KQWp9PZRLFjULAiH9H0otlVvfYLvw1XaDEwnbqPKeFXKO%2Fb3VsaTgn7wlslarg4v3zpm0O1C1c5Gd77wCcCnFdRPxBiCiAPbTMPrH1j2kdjrZowZ3Ihqn4XZjZVXxOPaJzfo2vSusDywGbycCqQ%2BpMKrX%2FrwGOqUBEIHDH6%2BTnW7uUm9uijEa4UwKogkHcUWXSdhcoi%2FSeqzQ2yp2siOVgNKhYYjQD38VtZfHe4vilg4ptQCKlJQz40F7OKl1pfnO0Z2rSIIZFaL5HtWA6gMs%2Fo%2Bt83ycHM4Wonn0NSMb4B7YuyA1YGSBuRCTB79qLGmOAzQmr%2FhaA2uJakzvQX0JJHZbCzAmlX7D%2FOcQxEGSbBliY%2Fmqd6t202BPXmAk&X-Amz-Signature=f3033f502bd65d7064a147af90ca685804ebedb84bbe27d36e058dff29c4f8c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643B656FN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEj4Ka0T8GQNSLXSHLqXjzk61xOb6Pk1EFCPF%2FCrQJAwIhANAmdRV7dW2%2BlwC4ch4E126a2J%2F8DzcWAAxP%2BHcRkKKnKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxrhSb%2BIg3V9A35xUq3APyn6gWWOuSt38UhVXdFpcLiWGkC7pPjcSyq3T1BH396DFNYchfCuFo3a%2FhOkDacgDKMAcY%2FO%2FJQ0%2Bw%2BSpFCggfuwd3cHA4aIUrK1dvY2Zf7Ncpot2iUvn60%2BZYlryLbD6IkCTtoQiiPRsZhSZmN7GmeHM7KvQ4unmQTWzL8GBSv1RiMqQWjGesD4IlgAgtmqG1QOwouwe2NHwFnv20Zg1QTPbHI865T0l19xP%2BmKimhwqplRCuFYde1ZAF81k37c0h29cR7XCR9%2FGBRkqJQRD5Keu8Kiwe85oyxXDq0UDdPMDLRqxBUFo1TYmahr0DNE4MrnxmienPymhKCozWhkTENWDB4tkH6WM35d2cKA4xy3Y%2BVZDGLY09K%2B1Mb4XnXm52QKeFM0ta7QrnS3rwL1uAgW%2F8FhHU2imOrF5ExsQv7e9g8YO13uENjF5WM9yZgnZCxwj88eSO2jbChRiuiag2DLt0MOHIm5AyRFFs1LyOvfoypBTTw7rD7x8pGAIzSi7WznVHIcwUovFcE%2BjI6yOtvsTdty9w9cg7JuQ96UUxa14U02pBb2Mz%2FfFxGar46lJyMng8ljVfn9U1Ao9Y5LpL5Od0OihH1AqNDHCUdR7Fej7kPQL%2FBVYyeLqRBDD24f68BjqkAQHAQP%2FA0l%2FYsQxljdNCrfGBjWCEwAtwGO9ThLbPninbjk5pG79JqF%2BmtSTuZwS98Qk6tYS%2BLZCdsrfYIEuSns5RICJ5lRTcnBpNcLiVK5VkgHS7vKEMeFrU0HacCUhAX5VoWn8qA8ksbhK6TrpS25%2BL%2BP%2BY0LuRs833XDIPtdh9ZyMuSXbqEDXVdGP%2FK2Fj6Tq4wZbjYDJvEZljo9jaVGtZlrhE&X-Amz-Signature=da2b176aff15b71806eb8dc1429f8ae0b8f9a64cf8049e753df87c1ba223e517&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643B656FN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEj4Ka0T8GQNSLXSHLqXjzk61xOb6Pk1EFCPF%2FCrQJAwIhANAmdRV7dW2%2BlwC4ch4E126a2J%2F8DzcWAAxP%2BHcRkKKnKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxrhSb%2BIg3V9A35xUq3APyn6gWWOuSt38UhVXdFpcLiWGkC7pPjcSyq3T1BH396DFNYchfCuFo3a%2FhOkDacgDKMAcY%2FO%2FJQ0%2Bw%2BSpFCggfuwd3cHA4aIUrK1dvY2Zf7Ncpot2iUvn60%2BZYlryLbD6IkCTtoQiiPRsZhSZmN7GmeHM7KvQ4unmQTWzL8GBSv1RiMqQWjGesD4IlgAgtmqG1QOwouwe2NHwFnv20Zg1QTPbHI865T0l19xP%2BmKimhwqplRCuFYde1ZAF81k37c0h29cR7XCR9%2FGBRkqJQRD5Keu8Kiwe85oyxXDq0UDdPMDLRqxBUFo1TYmahr0DNE4MrnxmienPymhKCozWhkTENWDB4tkH6WM35d2cKA4xy3Y%2BVZDGLY09K%2B1Mb4XnXm52QKeFM0ta7QrnS3rwL1uAgW%2F8FhHU2imOrF5ExsQv7e9g8YO13uENjF5WM9yZgnZCxwj88eSO2jbChRiuiag2DLt0MOHIm5AyRFFs1LyOvfoypBTTw7rD7x8pGAIzSi7WznVHIcwUovFcE%2BjI6yOtvsTdty9w9cg7JuQ96UUxa14U02pBb2Mz%2FfFxGar46lJyMng8ljVfn9U1Ao9Y5LpL5Od0OihH1AqNDHCUdR7Fej7kPQL%2FBVYyeLqRBDD24f68BjqkAQHAQP%2FA0l%2FYsQxljdNCrfGBjWCEwAtwGO9ThLbPninbjk5pG79JqF%2BmtSTuZwS98Qk6tYS%2BLZCdsrfYIEuSns5RICJ5lRTcnBpNcLiVK5VkgHS7vKEMeFrU0HacCUhAX5VoWn8qA8ksbhK6TrpS25%2BL%2BP%2BY0LuRs833XDIPtdh9ZyMuSXbqEDXVdGP%2FK2Fj6Tq4wZbjYDJvEZljo9jaVGtZlrhE&X-Amz-Signature=8ef0053894ffac18ae4af7706d09508920b99b3f3cc784f0b1e43266e4d113d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643B656FN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEj4Ka0T8GQNSLXSHLqXjzk61xOb6Pk1EFCPF%2FCrQJAwIhANAmdRV7dW2%2BlwC4ch4E126a2J%2F8DzcWAAxP%2BHcRkKKnKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxrhSb%2BIg3V9A35xUq3APyn6gWWOuSt38UhVXdFpcLiWGkC7pPjcSyq3T1BH396DFNYchfCuFo3a%2FhOkDacgDKMAcY%2FO%2FJQ0%2Bw%2BSpFCggfuwd3cHA4aIUrK1dvY2Zf7Ncpot2iUvn60%2BZYlryLbD6IkCTtoQiiPRsZhSZmN7GmeHM7KvQ4unmQTWzL8GBSv1RiMqQWjGesD4IlgAgtmqG1QOwouwe2NHwFnv20Zg1QTPbHI865T0l19xP%2BmKimhwqplRCuFYde1ZAF81k37c0h29cR7XCR9%2FGBRkqJQRD5Keu8Kiwe85oyxXDq0UDdPMDLRqxBUFo1TYmahr0DNE4MrnxmienPymhKCozWhkTENWDB4tkH6WM35d2cKA4xy3Y%2BVZDGLY09K%2B1Mb4XnXm52QKeFM0ta7QrnS3rwL1uAgW%2F8FhHU2imOrF5ExsQv7e9g8YO13uENjF5WM9yZgnZCxwj88eSO2jbChRiuiag2DLt0MOHIm5AyRFFs1LyOvfoypBTTw7rD7x8pGAIzSi7WznVHIcwUovFcE%2BjI6yOtvsTdty9w9cg7JuQ96UUxa14U02pBb2Mz%2FfFxGar46lJyMng8ljVfn9U1Ao9Y5LpL5Od0OihH1AqNDHCUdR7Fej7kPQL%2FBVYyeLqRBDD24f68BjqkAQHAQP%2FA0l%2FYsQxljdNCrfGBjWCEwAtwGO9ThLbPninbjk5pG79JqF%2BmtSTuZwS98Qk6tYS%2BLZCdsrfYIEuSns5RICJ5lRTcnBpNcLiVK5VkgHS7vKEMeFrU0HacCUhAX5VoWn8qA8ksbhK6TrpS25%2BL%2BP%2BY0LuRs833XDIPtdh9ZyMuSXbqEDXVdGP%2FK2Fj6Tq4wZbjYDJvEZljo9jaVGtZlrhE&X-Amz-Signature=afd316bce8ec100803f65c3ce9e9dfcec6773c4ef7aba8cca93097ff676d4849&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QDTJQQN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHvsehwLJttKdHFmX4lSYtfw9GCz1Xdd0bPchJpD%2BKNHAiEAmVgHP%2F4r7pqB3%2F3fztwIJB92smscOCCrmXZS%2BvRdszoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM0SY6G9as%2F5KYvVlSrcA1QzbFtLVtpK8iNXqupIj1yLXDPBoLl%2BIC5XTZf0cPfkY8eZtpB4jXzgtA%2FVcVRF%2FJ%2FCRl%2Bj5YfIxGjuG916WQr9C1efnwXHVnrTwvM8fKXCPjBC0G68prCtTdNpvh7auif0qZTsm9hqh0WMJufj2SlYer8YxZ9aaBJH3niEnkBKWcZtnbS5Kh9zi4IDaq33xGUbQ31KBsYWPS%2FkuII69Xqvfng9Eg0M1bGXCwTWN%2BfbYvcqZ2K4aikOItcJnQ%2FLGsEDpTuDsMDmGpeGAdth%2F%2F9R3p8J7qEk05NHhiMyN%2BANHx9a2vZFmsdMMfmRqU9yhb52Fv%2FaHQ%2Bk8jXNT1uIZT6EUFY5WjlBrvJAZVvFvT1q0zpW6IuFZff6FGx4zq9AAvr0ZJNrxwfEol2OeZNERZD9dF2geN7LWV%2F%2FUfAWSoJSKjVotuMZC2LpnYUb0nRZ8FwRKTt9WF0GbBSFqKxJbTpZJv4niXE7sSkWku25QdKUDmXmEiOmpDppHWXLO87cWc%2FdED7c7dhU%2BMi2CZdMsxcRmmp%2B8UvN2DOx2m7ksx%2FlOeiw%2FGWZqo%2BuT%2B9DNLehlrvrUmEl1xcgNdC9YGYEFKM9hoWO%2F%2FD9q%2BFd%2BdQWFmjq3wcJJSpzMSSU5aeBMITe%2FrwGOqUBl6aLZid4ebR0ilpH9wbyioi18Xw69Ck50%2FWyS9wHjZC6Kp3RIinMIe0JDS9AXO3GzpB7kJfcpsO9mipawxVYlGmLdJ0DOhXMpR50%2BXeMnXSuC%2FJa9mxXG4A0RH9DabyyanNqOeb%2FuQ8PWo8EKR%2FwI%2FkA6kEU2CDUVHPnRZKfjSDMAhpJ3I7OJ26roEZMMdBtrD%2Ft4%2BJTBGqhfGY6651AleN7GHMd&X-Amz-Signature=8a5d127726269718773c61c2148a95360613c6482a1e32b84240de614c047ea1&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT4Q7NF3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFjiTZih24yI8XJVlc1muxw06UrvNZAz19L%2FPceUYXy4AiBhcwBT5zs0eJA17CCmQXUTZdX5qbPvYhq55%2F7J%2F9gRtSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjjZNoJ0aDbPQ%2BbcRKtwDmnQeQox5Gganao1jM3SFQaTpf10M4SxjhWISxpvYPRqsj5ETmaQHTB33bPUIOTgfHY7sBULurJyjjdliIlzl7sebm98aI7A2n7kjlsofA826dHnql0UjdDBCKsfLzsLOFa64Q7sS%2BY18j94iSBMKLL8EqbZC0mEnWGoCULNmvtyNGLbdmAm%2B26TQzdQ4izSSZXvtgb%2F5eV9Km%2BWQXf5kChJJ1GLiWgrniGSskHeFB79f9XeUh2at9%2BwXjYWPfunS%2Fy7iA%2FPsN1kELndTheANtmbNBlkyGNtDZQDyPIUsebA3g3tqSimRYTqvoDdbbQrKAvEHMNEnpXWhneddifHEKC0Xr0zAYkmQ4y1wh56yJvaFDaIJmek0ff4qUW6fDORA7%2Bs4kAhDBCXUex8vVMsHBWQ%2BWld58Rjd93aSrVbzey%2FZ5gdHiPdJia1Hr3YY398nuLndBhnwjo%2BCq2k0lA8EOj72y9Wu07PCyMFPb4yBs%2B5w%2FsYY%2BdK5K5Ls2fxN0rdp3Vp5bFd9aFroyLGUKpDRCRaAh7RxdhFHkJZJ%2FkzoG9O81hWZdlQXurn8daXlVj6TR2jpQomHIuXqPrJDo3WdF%2FG8LjtBB5DSr00PEwC45%2Bvvufcd68kH7VjFevMwhN7%2BvAY6pgEstqX4YIR0FFhcr3Pq%2F9ESWZUaGe3qBU7VPf6GsH%2FxSzDdpIlQ%2FF2cElWHjnkBLKSiebYXi3z5okasNS%2FHAcuRpzfJCiwTkkY0EqJAFipiBKelEJ2DTulf%2FctFrW2dsHSz%2BAYNfLP2nLo4OEYXIpwzP%2BmcWXZm3KxfmrW4F8gC9cXJO2GXcIJzqvS42N9TADhHyLjvcSEwN9U2v8FxVRQKQdTYpo0s&X-Amz-Signature=6fbda592522d0b33cded58f003aebccd63c834f58e1f8ceea27e7574e10bc232&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQZFGOSM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICTlsGyu3T0pqBPOocS7IyEET7A94fsUt0v859V399tjAiEAwZrbMqGVhP0KOxVkD2B7%2FOLrRPqa7gdB6FASwvxkYCgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN9Sfd6%2F3Ai2KUFS5yrcAxqRgatrBq3DbezLoKCu%2BWPTlGw4Jya2k8fXv%2BvAw%2B5z%2BjyIp4ENANXUv1B7ExSu%2FFPh%2Bthsa1E8ImwcQQvL9GbMYMA%2FpAxWAyCBhi3FrDf0Bb3niruSzbFfVNcG2iXW%2FUVxDvNTMQtv0wYEMnUI57mjdTT%2B7iXcLccSdDk5eVwaZXBHJ5nCnZvHV%2F8WzEbAZ%2Fa3A2wmeLrtG%2BRpO7t9Mlozix8htvOP9hPJNcPp2bmp1KnABwkBOy9%2FyQw6UBErmXl6e3WDmszbhDp0eRqBlOTXAGyYrkbXPZW0u1N2f%2F3qZx7ivnl3C%2BZNu4r1LrqRu%2Fx9rlcqCiJv63V5dzR4zZ1YfmcgTSAlCSiRdhtlDGslssJNLR9VfTAcBOnvjh27LkyB2CY9TrubO5wiAadGQ89tlmCz5rJKswTOTUAqqbkzHD%2Be51ycoDL%2BNH3IilcTKktSRWZ6l1SHc1P4QW8UmCpJ3ka89fnmEhlVp5VCJZ1PfinAi8guG1PMRrX0NntYkXVc2HgC4CwE62jO4yDGSEtEnMSx3%2FHAHLe8En%2BXygYlRWrozZBQwWvXu%2BofFHXbxc6b64PSLCGzi0b8iWqcN8ghXZyQ0S6Wue9C10V9akDvtyNCIZF44kCAWq%2BdMP7g%2FrwGOqUBtiKl8y7wUTyvUzkhm00kP6vc5l0TEuZienbV6cE1Grl6uY%2FLZxU14KnT5VHuwOyNNGu1yt40jGb2JN5R7719pt190pb%2F%2FbQkEMP2qlcJ1f7IjO%2FM2X7JiyTI7cKWoobpS8weFmDyNsiB4luqySXePWqNMk0HjRQaPooFGMuCT7ofjuGeh6V2cRMw%2FMhP6tHcoInJv5wcwSjekMzwhoy83WLKWWWK&X-Amz-Signature=cb58990863fd4159a292bc1de0d18217fa43b4fdc5bf88e2da32beaeddd0afe6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWHPXA5K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuD2xfipvQgjwog4puZpippPpmbjjh9Xs4eWjAIIFWtQIgfeorlw6FNZgrbUbJyJRQq3RXn%2FyzVFSzPJJIiecflwYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHvjkNPgmNlzA7pIuSrcAx4Mjr4T8Gof8Be8iHCOl1LEfzUtEiVtlN0ubtKp%2B%2FqLe8ognrmzsaoc4A6obtXS6W09Ghbzn8wWRFUD3sqoFyosGOir6vz7TgssElf6T9chtvvgQV9blxo6P5P51SJVsLah6Gh7z12RFdInLsqSHrzT2Ly6fUQtwOnNNQmFGqxezzZIjTk880mJ5X3Iv97FJFYNXy8O8I8BJZnREiIFqn%2Fg8bZvHCXd%2F9lteDB7q1lkuVLFcLzC39lke8ReQ4m6s2o5wxDoM3EqXPcq7clR4EgmmXmEoCZVYVr3KU1M7f2WNX14pkT0L3oa%2FAgSYzaokGaZuC7ok6C4Lj%2FMP4XD%2FPCUSrxMJ7yy5pyz%2F9mKsk8%2Ff2gz1dJsziTspQdtAtmvHmAAkZk4JBKwUFldCpYcpHJ9jCBzpFcgaUB4nGIvMJZN7jb2bJW0rxCDxQm1zLNROTSMMyVX0QA%2BjPQ36iFKuP%2BKtU0QaXYfnD1pusHKNRBzkGFNX5KxfF627se8uJ9D6U6HMp7UNQauVJjRMeLd9GT2wofD%2B9tsE31uH9MeYyelibutip9cFQN04aGWwLK%2FA88aGJBpceERwiDXqoQdMIBgH5%2FAEYMC8cvw6FqtJtNkvwD4lokpcrt8NtCcMOPh%2FrwGOqUBUEhHfFWVGgY3%2FitOLjvjSpACbA6zG%2FQyw7YHFbI06qGPmCZ0RcrvZcOotkcuE6G%2Bg3KPZOkc7uYcfu8Xd9IkP0CSTQQlVaeRCeRxss8KsKIBmBys8bDSZSr%2B2brRPKHfEW4SJb5bD3UYDFYVi2ynXaat0uw%2Bqg8bLEmYCFqFWun%2BHY7xgUcgw2%2F8X7eADCGuJWa%2FJn8wsBDBLQO%2BH4FopMAaU9Bf&X-Amz-Signature=9776973f741d71367f492b7cb27a926f5a0fb9c1fdd0dc90559cb3f9b3322af0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWHPXA5K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuD2xfipvQgjwog4puZpippPpmbjjh9Xs4eWjAIIFWtQIgfeorlw6FNZgrbUbJyJRQq3RXn%2FyzVFSzPJJIiecflwYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHvjkNPgmNlzA7pIuSrcAx4Mjr4T8Gof8Be8iHCOl1LEfzUtEiVtlN0ubtKp%2B%2FqLe8ognrmzsaoc4A6obtXS6W09Ghbzn8wWRFUD3sqoFyosGOir6vz7TgssElf6T9chtvvgQV9blxo6P5P51SJVsLah6Gh7z12RFdInLsqSHrzT2Ly6fUQtwOnNNQmFGqxezzZIjTk880mJ5X3Iv97FJFYNXy8O8I8BJZnREiIFqn%2Fg8bZvHCXd%2F9lteDB7q1lkuVLFcLzC39lke8ReQ4m6s2o5wxDoM3EqXPcq7clR4EgmmXmEoCZVYVr3KU1M7f2WNX14pkT0L3oa%2FAgSYzaokGaZuC7ok6C4Lj%2FMP4XD%2FPCUSrxMJ7yy5pyz%2F9mKsk8%2Ff2gz1dJsziTspQdtAtmvHmAAkZk4JBKwUFldCpYcpHJ9jCBzpFcgaUB4nGIvMJZN7jb2bJW0rxCDxQm1zLNROTSMMyVX0QA%2BjPQ36iFKuP%2BKtU0QaXYfnD1pusHKNRBzkGFNX5KxfF627se8uJ9D6U6HMp7UNQauVJjRMeLd9GT2wofD%2B9tsE31uH9MeYyelibutip9cFQN04aGWwLK%2FA88aGJBpceERwiDXqoQdMIBgH5%2FAEYMC8cvw6FqtJtNkvwD4lokpcrt8NtCcMOPh%2FrwGOqUBUEhHfFWVGgY3%2FitOLjvjSpACbA6zG%2FQyw7YHFbI06qGPmCZ0RcrvZcOotkcuE6G%2Bg3KPZOkc7uYcfu8Xd9IkP0CSTQQlVaeRCeRxss8KsKIBmBys8bDSZSr%2B2brRPKHfEW4SJb5bD3UYDFYVi2ynXaat0uw%2Bqg8bLEmYCFqFWun%2BHY7xgUcgw2%2F8X7eADCGuJWa%2FJn8wsBDBLQO%2BH4FopMAaU9Bf&X-Amz-Signature=7ab7c6df22305ad14fda2087a2976032c9ab5f9204584e887fd39c0f8f64c77b&X-Amz-SignedHeaders=host&x-id=GetObject)

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
