

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQU3UZRP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCMsSTSq09wlkdZSLKzYTnqMzqGuN1yDlmY%2B1KvGVBrYAIhAIYFoS6BqjEj51TifhHD7PP%2FvNmPA6hyoZVWHSK4FxQiKv8DCFoQABoMNjM3NDIzMTgzODA1IgzZvbZ%2FsEL%2FhzuHuPYq3APbz7AORkViKw7QBrD1XngrI18lIbYhxxKd%2F8%2FOAgtT761TkvNPCY0u5zH0ECWFkNlT07drPQIk6%2B2fMXX6rHbMFcVjB%2FGAfcJ26bAG7yy8K2m4mI0MZEjCRQiPfMsBOJDaehjuQ8ZRcKGoC6nxytQ0nKlJ1%2FKdOTYI0Z6kpSYYa7ZsUVATuFBMSupV7qIvrtowwUZ1ZpbmwIyBC1UPHtONM9zpzODmdeASZxrOEc03lDiAZYG2C5cS%2FZniqTxWdND6iUyXE9898EbVNsGLLw6sZ1SdHBXeqxkql498wViQUQbz82kDxZb0%2BZde%2FXQAWQhxoZAWqi7jodCGhLD0BO9T1asFgTNaVYO8tiXVtw6fJ7OrI4bw23nVa6MdxUchDvl8VUAuaCsmLJZ2knXUhm9JN8Gh3yJMQ5Wi0OaYt%2B7ul2dB2fhN%2BM9Fg2wkdji69sbOpSVw1Li8EB5CAjdUsIgURTk4eRo6L%2Bg7ZAh%2FhQPqOVdySGgxbln7fcndmOewKMSQ9TAzKCBtmFO62suoen%2BoeqhD%2B6vXY7s%2BW%2FuKpDqUNyyLSYN5dc0iv9F%2BbvYX9xvSierwKD3Jm%2FRlbxVh9fVFnNTSfOs3v7KQHYF0%2BucSI9sEj4Rw4wqROtQ%2BuDDe65G9BjqkAaquyRJ%2Bf37hDu209jiakmhGAXmsbp%2B6vk8dKZXu0h3dWDTcVgzaTkdaCuRvs2fMtJlps8TZe9SPeE7a9gu6FekuO2lAHiLGPzd6T1eWcrKEAbZnqm%2FsBvVJhH%2BQWMKu1gnzMJyyVW8LZx9bt%2BjJV9jreyQ69hYOv6d9JOh62ouZWxJG6NQ64c7g1B4TPXRw3c6E5U%2BzB%2Bhq25JpeTvwYD12cG%2F%2F&X-Amz-Signature=1a1f408de3ac4660d9c882b8c096ffdc70c6896cc4eec9b91fdcc313cbdc20bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQU3UZRP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCMsSTSq09wlkdZSLKzYTnqMzqGuN1yDlmY%2B1KvGVBrYAIhAIYFoS6BqjEj51TifhHD7PP%2FvNmPA6hyoZVWHSK4FxQiKv8DCFoQABoMNjM3NDIzMTgzODA1IgzZvbZ%2FsEL%2FhzuHuPYq3APbz7AORkViKw7QBrD1XngrI18lIbYhxxKd%2F8%2FOAgtT761TkvNPCY0u5zH0ECWFkNlT07drPQIk6%2B2fMXX6rHbMFcVjB%2FGAfcJ26bAG7yy8K2m4mI0MZEjCRQiPfMsBOJDaehjuQ8ZRcKGoC6nxytQ0nKlJ1%2FKdOTYI0Z6kpSYYa7ZsUVATuFBMSupV7qIvrtowwUZ1ZpbmwIyBC1UPHtONM9zpzODmdeASZxrOEc03lDiAZYG2C5cS%2FZniqTxWdND6iUyXE9898EbVNsGLLw6sZ1SdHBXeqxkql498wViQUQbz82kDxZb0%2BZde%2FXQAWQhxoZAWqi7jodCGhLD0BO9T1asFgTNaVYO8tiXVtw6fJ7OrI4bw23nVa6MdxUchDvl8VUAuaCsmLJZ2knXUhm9JN8Gh3yJMQ5Wi0OaYt%2B7ul2dB2fhN%2BM9Fg2wkdji69sbOpSVw1Li8EB5CAjdUsIgURTk4eRo6L%2Bg7ZAh%2FhQPqOVdySGgxbln7fcndmOewKMSQ9TAzKCBtmFO62suoen%2BoeqhD%2B6vXY7s%2BW%2FuKpDqUNyyLSYN5dc0iv9F%2BbvYX9xvSierwKD3Jm%2FRlbxVh9fVFnNTSfOs3v7KQHYF0%2BucSI9sEj4Rw4wqROtQ%2BuDDe65G9BjqkAaquyRJ%2Bf37hDu209jiakmhGAXmsbp%2B6vk8dKZXu0h3dWDTcVgzaTkdaCuRvs2fMtJlps8TZe9SPeE7a9gu6FekuO2lAHiLGPzd6T1eWcrKEAbZnqm%2FsBvVJhH%2BQWMKu1gnzMJyyVW8LZx9bt%2BjJV9jreyQ69hYOv6d9JOh62ouZWxJG6NQ64c7g1B4TPXRw3c6E5U%2BzB%2Bhq25JpeTvwYD12cG%2F%2F&X-Amz-Signature=76a890cb3b999703570ef451f0b139905279ac8a8c32626f54783235bcecdd7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQU3UZRP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCMsSTSq09wlkdZSLKzYTnqMzqGuN1yDlmY%2B1KvGVBrYAIhAIYFoS6BqjEj51TifhHD7PP%2FvNmPA6hyoZVWHSK4FxQiKv8DCFoQABoMNjM3NDIzMTgzODA1IgzZvbZ%2FsEL%2FhzuHuPYq3APbz7AORkViKw7QBrD1XngrI18lIbYhxxKd%2F8%2FOAgtT761TkvNPCY0u5zH0ECWFkNlT07drPQIk6%2B2fMXX6rHbMFcVjB%2FGAfcJ26bAG7yy8K2m4mI0MZEjCRQiPfMsBOJDaehjuQ8ZRcKGoC6nxytQ0nKlJ1%2FKdOTYI0Z6kpSYYa7ZsUVATuFBMSupV7qIvrtowwUZ1ZpbmwIyBC1UPHtONM9zpzODmdeASZxrOEc03lDiAZYG2C5cS%2FZniqTxWdND6iUyXE9898EbVNsGLLw6sZ1SdHBXeqxkql498wViQUQbz82kDxZb0%2BZde%2FXQAWQhxoZAWqi7jodCGhLD0BO9T1asFgTNaVYO8tiXVtw6fJ7OrI4bw23nVa6MdxUchDvl8VUAuaCsmLJZ2knXUhm9JN8Gh3yJMQ5Wi0OaYt%2B7ul2dB2fhN%2BM9Fg2wkdji69sbOpSVw1Li8EB5CAjdUsIgURTk4eRo6L%2Bg7ZAh%2FhQPqOVdySGgxbln7fcndmOewKMSQ9TAzKCBtmFO62suoen%2BoeqhD%2B6vXY7s%2BW%2FuKpDqUNyyLSYN5dc0iv9F%2BbvYX9xvSierwKD3Jm%2FRlbxVh9fVFnNTSfOs3v7KQHYF0%2BucSI9sEj4Rw4wqROtQ%2BuDDe65G9BjqkAaquyRJ%2Bf37hDu209jiakmhGAXmsbp%2B6vk8dKZXu0h3dWDTcVgzaTkdaCuRvs2fMtJlps8TZe9SPeE7a9gu6FekuO2lAHiLGPzd6T1eWcrKEAbZnqm%2FsBvVJhH%2BQWMKu1gnzMJyyVW8LZx9bt%2BjJV9jreyQ69hYOv6d9JOh62ouZWxJG6NQ64c7g1B4TPXRw3c6E5U%2BzB%2Bhq25JpeTvwYD12cG%2F%2F&X-Amz-Signature=1082f9f19a10e98fa6f65cf85220f6cd058a5fec901158b41a8a43568405059a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDKXJO23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCmhci%2FXcCpRIAArjrzEFpqLGejOa5mBA1gjKCbFIVMqwIgDiF9uVn%2F4as2BAxEZ6T1stIYe7pDDUlggO3c%2BQgxS9oq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMAwQWpdOQi%2FvaCMLCrcA2nQqjCU3wzVj289SO4Nz0QTur7TioM8rmAxzvdaP5AYzGrlkXGmJtJik1e%2Fn2nBVzyNRDbx%2BebsvtiB%2FHIyIVSXFw673Sl9sfRNkFasNE0rYSFeiSBr59jSOtfQIJSUdKJELwmo9WJSG4UNbYVoTzhG4jo4y883F8DlplIt9ZIiQ0ICmehAnEEhKQoQHDsbN6XX0Ss02ydIO4%2FUcI6YLJYFPu1ZoW1m0zEr7k2lHzn4dv8oiKBDcU0NWj38Lf%2B26AYX2j70e17r4dhTKJBtastBH4c5lyXxnnbDCOEPdJGl%2Brn2K248mA973dggy8J8tGrdXq4D%2BmD5I%2FPeaxvzsEc6Yj%2FNevCx9%2B5ltr4h4nFJfET7uVbR7j4WfnPUy4%2BAVepbXgFrY%2FKHW9%2BLlE2uDW6TPLq4c8440nUaV4U668aajQOQSBDa2LnjeR%2BcQ%2Bbqx%2Ft8ns8YRTo8KCU0u6JoKXmsLHkaJx9TYXT7s%2BuWxlr95gUczfrnkiwreUauvQaDMGg8qA6DD2LJB3%2FeL%2BuMEh7LGU9DpOs%2BqBVldpkR59COvKEretd2XXhBOpvJIaHqF0hUETomFEvXZJx%2BE5Vfa7tnoYK833%2FY1A9NFZAGXdGU6Wdz0wX7Um9BAxj3MLPskb0GOqUB9AZMsdL6MYmFZyuuqvqP7JVw58Ru7NnwA9r6xiDICPGZgACex9fPAb2QxtpEFqHXUN4RNFlqDt9xrC0RinBHT2VQoIfJMDHSqLGX1ohzzMlJUXWTLszUJntyp9LMkkkdnGOeRZAPo9VQyWZWCLZXeO7iLA1Xso4iOpdFQ7pGe9n3tRlSyDCsC6MkNy1XEGF3CSagX6%2BuhTXUwXkljypGHrxuOZgJ&X-Amz-Signature=bc6f3d7c176d55bde05bf52a1f196db007ad3cc24c22aeee9456669fa618afb6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDKXJO23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCmhci%2FXcCpRIAArjrzEFpqLGejOa5mBA1gjKCbFIVMqwIgDiF9uVn%2F4as2BAxEZ6T1stIYe7pDDUlggO3c%2BQgxS9oq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMAwQWpdOQi%2FvaCMLCrcA2nQqjCU3wzVj289SO4Nz0QTur7TioM8rmAxzvdaP5AYzGrlkXGmJtJik1e%2Fn2nBVzyNRDbx%2BebsvtiB%2FHIyIVSXFw673Sl9sfRNkFasNE0rYSFeiSBr59jSOtfQIJSUdKJELwmo9WJSG4UNbYVoTzhG4jo4y883F8DlplIt9ZIiQ0ICmehAnEEhKQoQHDsbN6XX0Ss02ydIO4%2FUcI6YLJYFPu1ZoW1m0zEr7k2lHzn4dv8oiKBDcU0NWj38Lf%2B26AYX2j70e17r4dhTKJBtastBH4c5lyXxnnbDCOEPdJGl%2Brn2K248mA973dggy8J8tGrdXq4D%2BmD5I%2FPeaxvzsEc6Yj%2FNevCx9%2B5ltr4h4nFJfET7uVbR7j4WfnPUy4%2BAVepbXgFrY%2FKHW9%2BLlE2uDW6TPLq4c8440nUaV4U668aajQOQSBDa2LnjeR%2BcQ%2Bbqx%2Ft8ns8YRTo8KCU0u6JoKXmsLHkaJx9TYXT7s%2BuWxlr95gUczfrnkiwreUauvQaDMGg8qA6DD2LJB3%2FeL%2BuMEh7LGU9DpOs%2BqBVldpkR59COvKEretd2XXhBOpvJIaHqF0hUETomFEvXZJx%2BE5Vfa7tnoYK833%2FY1A9NFZAGXdGU6Wdz0wX7Um9BAxj3MLPskb0GOqUB9AZMsdL6MYmFZyuuqvqP7JVw58Ru7NnwA9r6xiDICPGZgACex9fPAb2QxtpEFqHXUN4RNFlqDt9xrC0RinBHT2VQoIfJMDHSqLGX1ohzzMlJUXWTLszUJntyp9LMkkkdnGOeRZAPo9VQyWZWCLZXeO7iLA1Xso4iOpdFQ7pGe9n3tRlSyDCsC6MkNy1XEGF3CSagX6%2BuhTXUwXkljypGHrxuOZgJ&X-Amz-Signature=d33717bd97d46cef07ed021b37ffec98b7e4c07f3dcbdeead24459fbea9e69f8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDKXJO23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCmhci%2FXcCpRIAArjrzEFpqLGejOa5mBA1gjKCbFIVMqwIgDiF9uVn%2F4as2BAxEZ6T1stIYe7pDDUlggO3c%2BQgxS9oq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMAwQWpdOQi%2FvaCMLCrcA2nQqjCU3wzVj289SO4Nz0QTur7TioM8rmAxzvdaP5AYzGrlkXGmJtJik1e%2Fn2nBVzyNRDbx%2BebsvtiB%2FHIyIVSXFw673Sl9sfRNkFasNE0rYSFeiSBr59jSOtfQIJSUdKJELwmo9WJSG4UNbYVoTzhG4jo4y883F8DlplIt9ZIiQ0ICmehAnEEhKQoQHDsbN6XX0Ss02ydIO4%2FUcI6YLJYFPu1ZoW1m0zEr7k2lHzn4dv8oiKBDcU0NWj38Lf%2B26AYX2j70e17r4dhTKJBtastBH4c5lyXxnnbDCOEPdJGl%2Brn2K248mA973dggy8J8tGrdXq4D%2BmD5I%2FPeaxvzsEc6Yj%2FNevCx9%2B5ltr4h4nFJfET7uVbR7j4WfnPUy4%2BAVepbXgFrY%2FKHW9%2BLlE2uDW6TPLq4c8440nUaV4U668aajQOQSBDa2LnjeR%2BcQ%2Bbqx%2Ft8ns8YRTo8KCU0u6JoKXmsLHkaJx9TYXT7s%2BuWxlr95gUczfrnkiwreUauvQaDMGg8qA6DD2LJB3%2FeL%2BuMEh7LGU9DpOs%2BqBVldpkR59COvKEretd2XXhBOpvJIaHqF0hUETomFEvXZJx%2BE5Vfa7tnoYK833%2FY1A9NFZAGXdGU6Wdz0wX7Um9BAxj3MLPskb0GOqUB9AZMsdL6MYmFZyuuqvqP7JVw58Ru7NnwA9r6xiDICPGZgACex9fPAb2QxtpEFqHXUN4RNFlqDt9xrC0RinBHT2VQoIfJMDHSqLGX1ohzzMlJUXWTLszUJntyp9LMkkkdnGOeRZAPo9VQyWZWCLZXeO7iLA1Xso4iOpdFQ7pGe9n3tRlSyDCsC6MkNy1XEGF3CSagX6%2BuhTXUwXkljypGHrxuOZgJ&X-Amz-Signature=a95b030295fd7a1456ceb80a50e626509348ed55f4925224cd4c7291c187daf0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDKXJO23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCmhci%2FXcCpRIAArjrzEFpqLGejOa5mBA1gjKCbFIVMqwIgDiF9uVn%2F4as2BAxEZ6T1stIYe7pDDUlggO3c%2BQgxS9oq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMAwQWpdOQi%2FvaCMLCrcA2nQqjCU3wzVj289SO4Nz0QTur7TioM8rmAxzvdaP5AYzGrlkXGmJtJik1e%2Fn2nBVzyNRDbx%2BebsvtiB%2FHIyIVSXFw673Sl9sfRNkFasNE0rYSFeiSBr59jSOtfQIJSUdKJELwmo9WJSG4UNbYVoTzhG4jo4y883F8DlplIt9ZIiQ0ICmehAnEEhKQoQHDsbN6XX0Ss02ydIO4%2FUcI6YLJYFPu1ZoW1m0zEr7k2lHzn4dv8oiKBDcU0NWj38Lf%2B26AYX2j70e17r4dhTKJBtastBH4c5lyXxnnbDCOEPdJGl%2Brn2K248mA973dggy8J8tGrdXq4D%2BmD5I%2FPeaxvzsEc6Yj%2FNevCx9%2B5ltr4h4nFJfET7uVbR7j4WfnPUy4%2BAVepbXgFrY%2FKHW9%2BLlE2uDW6TPLq4c8440nUaV4U668aajQOQSBDa2LnjeR%2BcQ%2Bbqx%2Ft8ns8YRTo8KCU0u6JoKXmsLHkaJx9TYXT7s%2BuWxlr95gUczfrnkiwreUauvQaDMGg8qA6DD2LJB3%2FeL%2BuMEh7LGU9DpOs%2BqBVldpkR59COvKEretd2XXhBOpvJIaHqF0hUETomFEvXZJx%2BE5Vfa7tnoYK833%2FY1A9NFZAGXdGU6Wdz0wX7Um9BAxj3MLPskb0GOqUB9AZMsdL6MYmFZyuuqvqP7JVw58Ru7NnwA9r6xiDICPGZgACex9fPAb2QxtpEFqHXUN4RNFlqDt9xrC0RinBHT2VQoIfJMDHSqLGX1ohzzMlJUXWTLszUJntyp9LMkkkdnGOeRZAPo9VQyWZWCLZXeO7iLA1Xso4iOpdFQ7pGe9n3tRlSyDCsC6MkNy1XEGF3CSagX6%2BuhTXUwXkljypGHrxuOZgJ&X-Amz-Signature=5c38e19bed35e7315ff1af2157606321d81df2fa8dc2786068c1559a37a24ed1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDKXJO23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCmhci%2FXcCpRIAArjrzEFpqLGejOa5mBA1gjKCbFIVMqwIgDiF9uVn%2F4as2BAxEZ6T1stIYe7pDDUlggO3c%2BQgxS9oq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMAwQWpdOQi%2FvaCMLCrcA2nQqjCU3wzVj289SO4Nz0QTur7TioM8rmAxzvdaP5AYzGrlkXGmJtJik1e%2Fn2nBVzyNRDbx%2BebsvtiB%2FHIyIVSXFw673Sl9sfRNkFasNE0rYSFeiSBr59jSOtfQIJSUdKJELwmo9WJSG4UNbYVoTzhG4jo4y883F8DlplIt9ZIiQ0ICmehAnEEhKQoQHDsbN6XX0Ss02ydIO4%2FUcI6YLJYFPu1ZoW1m0zEr7k2lHzn4dv8oiKBDcU0NWj38Lf%2B26AYX2j70e17r4dhTKJBtastBH4c5lyXxnnbDCOEPdJGl%2Brn2K248mA973dggy8J8tGrdXq4D%2BmD5I%2FPeaxvzsEc6Yj%2FNevCx9%2B5ltr4h4nFJfET7uVbR7j4WfnPUy4%2BAVepbXgFrY%2FKHW9%2BLlE2uDW6TPLq4c8440nUaV4U668aajQOQSBDa2LnjeR%2BcQ%2Bbqx%2Ft8ns8YRTo8KCU0u6JoKXmsLHkaJx9TYXT7s%2BuWxlr95gUczfrnkiwreUauvQaDMGg8qA6DD2LJB3%2FeL%2BuMEh7LGU9DpOs%2BqBVldpkR59COvKEretd2XXhBOpvJIaHqF0hUETomFEvXZJx%2BE5Vfa7tnoYK833%2FY1A9NFZAGXdGU6Wdz0wX7Um9BAxj3MLPskb0GOqUB9AZMsdL6MYmFZyuuqvqP7JVw58Ru7NnwA9r6xiDICPGZgACex9fPAb2QxtpEFqHXUN4RNFlqDt9xrC0RinBHT2VQoIfJMDHSqLGX1ohzzMlJUXWTLszUJntyp9LMkkkdnGOeRZAPo9VQyWZWCLZXeO7iLA1Xso4iOpdFQ7pGe9n3tRlSyDCsC6MkNy1XEGF3CSagX6%2BuhTXUwXkljypGHrxuOZgJ&X-Amz-Signature=ac4a81253dbaaacb3c390b168c7f2924c7a4314e792603bc46aa5c9e8b548b91&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDKXJO23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCmhci%2FXcCpRIAArjrzEFpqLGejOa5mBA1gjKCbFIVMqwIgDiF9uVn%2F4as2BAxEZ6T1stIYe7pDDUlggO3c%2BQgxS9oq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMAwQWpdOQi%2FvaCMLCrcA2nQqjCU3wzVj289SO4Nz0QTur7TioM8rmAxzvdaP5AYzGrlkXGmJtJik1e%2Fn2nBVzyNRDbx%2BebsvtiB%2FHIyIVSXFw673Sl9sfRNkFasNE0rYSFeiSBr59jSOtfQIJSUdKJELwmo9WJSG4UNbYVoTzhG4jo4y883F8DlplIt9ZIiQ0ICmehAnEEhKQoQHDsbN6XX0Ss02ydIO4%2FUcI6YLJYFPu1ZoW1m0zEr7k2lHzn4dv8oiKBDcU0NWj38Lf%2B26AYX2j70e17r4dhTKJBtastBH4c5lyXxnnbDCOEPdJGl%2Brn2K248mA973dggy8J8tGrdXq4D%2BmD5I%2FPeaxvzsEc6Yj%2FNevCx9%2B5ltr4h4nFJfET7uVbR7j4WfnPUy4%2BAVepbXgFrY%2FKHW9%2BLlE2uDW6TPLq4c8440nUaV4U668aajQOQSBDa2LnjeR%2BcQ%2Bbqx%2Ft8ns8YRTo8KCU0u6JoKXmsLHkaJx9TYXT7s%2BuWxlr95gUczfrnkiwreUauvQaDMGg8qA6DD2LJB3%2FeL%2BuMEh7LGU9DpOs%2BqBVldpkR59COvKEretd2XXhBOpvJIaHqF0hUETomFEvXZJx%2BE5Vfa7tnoYK833%2FY1A9NFZAGXdGU6Wdz0wX7Um9BAxj3MLPskb0GOqUB9AZMsdL6MYmFZyuuqvqP7JVw58Ru7NnwA9r6xiDICPGZgACex9fPAb2QxtpEFqHXUN4RNFlqDt9xrC0RinBHT2VQoIfJMDHSqLGX1ohzzMlJUXWTLszUJntyp9LMkkkdnGOeRZAPo9VQyWZWCLZXeO7iLA1Xso4iOpdFQ7pGe9n3tRlSyDCsC6MkNy1XEGF3CSagX6%2BuhTXUwXkljypGHrxuOZgJ&X-Amz-Signature=291dfbd805e6a5e0ee91c369e07b79a666be01a44906d85e6e9261632cd4614d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CGTLL4I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDUokNNoXA8eV7OQ4%2FJZ9uJB12b9NLFHhfOI48pyzPcswIgQEgjryV%2F2qwUfoO0LuEwKOVnZskDE%2BDl2qeG4d4GKxMq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOe1Ml4XjFpCpSBurCrcA1nLLf03iS5bQAsEvYMuv6NEk8qqQo1NrVivJcgifXEEcTwolVANPVQkspLje%2BOAXoWmVIyDrlrhaEAwxUK5U3psgv4LMyATOS9zydF8Ri7KW%2BU1yKqvP6AhPL11yNGKw6a1oSrqndJRO%2BGZ8I5C%2BqBhWckPWiv2sY1CBNO8ryWKRBRGoP4MqANSYXnxslRxyLRbGSSsCqaDFAway3OfxhJ%2BQoJqHS23vBMP6pHqBXAMYPVDdurOGeXw1AidUyquSADdUAK8Y5LC9alMInzDnO7%2BtNfoIy05q%2FE5XZLgV713TGPnpO%2BKwEQk1FzTr5YDOX1ZzZGps8UZ46YpaQTg5QgQ%2BpZm7pHgCFnCZkOPOOK5fJQHen3FvaY6DMuRQt%2FJ6xnB%2BOWbSRJx%2BZ3qTX38I%2FD0Gv%2BUVm7ZQ1P1wxziTjcdrd7ZqyB0Yu7W8uvGTJw526q%2F2xfiudFYuUCzMgamptleczYP1M5n7WPdgr8wCju8Y7KdBpIWEud97O78f8B14IfKR0zacBUfH7bVdXvaeXT59CRZtuCXldFvjzoJJG6gz7atbrI1LtyKt32%2Bav2R5VsIGtZVnXLbHFNYA0AEaeaVlbuCAkt4m4%2F4denkWM0YR75R7IXRSjH2IV4bMKHskb0GOqUBIGJ7VsIRE0vtuhi75Ip9%2BLd03%2FvelUmA8YiJsM%2BKf0LvDA5t5mWcgX1UHkVMY6z10DIkXDjAd%2FAvwONgo8dUMiEHcdb4xQBOmXHBlNINaDyJF3soZh%2BzQKMNvfPiyBImk13mc5FHW%2FwJ2wvYz5bVPxxGG6I%2BsmWUh%2BDnS6KW%2FfNWcUF%2Fva3QHG4IxyXxhSos08KI0pgH78Pli3mezk3LNLrU%2Fbgq&X-Amz-Signature=46f8df69d4d92dd2bdf59dbbe19b9539ba270910b66fd981a20bfcc983bab470&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q6U4DY6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGmy9jbP2sLfMUTpPxUoJJZ4gon67BUToSvo6A6O%2F482AiBxyvZ%2BMfEAYf6AddaTlNg4xNQc%2F1VzA%2F51oprCdzOGKSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMgJ4PaIIYJe%2FBK%2FghKtwDcAB5KJzdzvNzb7F6AzUrAQx%2BPjC7JlCk%2F%2FMmi%2BrvT5U44lKFYRr19BBfOkkxXxEmVXvB%2BDvoI4rBqyNVYlV1jYk6KtgJI77gJxzp8gTzbfqg9lqtc%2FJfhdCPVQUObJEjZ1NmdMd03owtjnWaOyQs4o7LpMY%2FrJyiFJwGemdS4ezLfif%2Fn0UQOhUeG5ID8c50zguTA8y2WOU8k3%2FdY0hiw5UIXN7Qdqej%2FbeiVWLwwf2ogGAeQ%2BLilvP1hy3dWnc2rHwUbHsWp5irTzY2o26JPnYgZ8JKYVgxLApH1jZFkyp8fT83iDn5glkoxoUKnHNy%2B9VDqJ3Ru0jtBcTMCNHeSnNupR9cyUKCsT5P1A5Dj6R0rIZH%2BmH95YwZdcE1C2bDmGsjMbp9qdPr15%2FUw6c3qwmcWxbgNyInGbDg5dQhK%2FhxEYLhhYK%2BU4M7nRUv3LSxIeCWvyWZ8T9eh0B8Zlt9mqdebc%2FJMF%2BfzgFBu9OyDt7GUKclxYcsjJYfkwC3PgEZdN%2BTTGJxXVTAP4g%2BHNsg2o0rdrdugvz2u73CAp8MIhU94IylnA0zOoT4LAw8rnEoDKymstF87fmfoGGGP%2FqRGD7n0jNBZgfk1cm42o5C22CyV4IlWczEY7NAxFUw0%2BuRvQY6pgErGU1XA40BSD4FizoyxgzGCVpCkxc4LLfNf35ao0bdXKEgH3H%2FjR9dybrNLm4uP7EFDBBsp7jtZjDd920HJUCXyEklZrIYDM3GbUuhCh5lSB%2Fvlc1BvF4ECpqXL3W37jW6dlHSJI2DCU0ZHi5dIDcUDz7wrHV62kMM8MOJuL91WCrXTe4RB7u4G6YBR0JsuAJipvYmg%2FAnjOtDJL6G%2F2UPeTHzcs0J&X-Amz-Signature=4117452db4d00b7049cf77294429b2f429014ea43d2b2aeec8ddb3f71e369feb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDKXJO23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCmhci%2FXcCpRIAArjrzEFpqLGejOa5mBA1gjKCbFIVMqwIgDiF9uVn%2F4as2BAxEZ6T1stIYe7pDDUlggO3c%2BQgxS9oq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMAwQWpdOQi%2FvaCMLCrcA2nQqjCU3wzVj289SO4Nz0QTur7TioM8rmAxzvdaP5AYzGrlkXGmJtJik1e%2Fn2nBVzyNRDbx%2BebsvtiB%2FHIyIVSXFw673Sl9sfRNkFasNE0rYSFeiSBr59jSOtfQIJSUdKJELwmo9WJSG4UNbYVoTzhG4jo4y883F8DlplIt9ZIiQ0ICmehAnEEhKQoQHDsbN6XX0Ss02ydIO4%2FUcI6YLJYFPu1ZoW1m0zEr7k2lHzn4dv8oiKBDcU0NWj38Lf%2B26AYX2j70e17r4dhTKJBtastBH4c5lyXxnnbDCOEPdJGl%2Brn2K248mA973dggy8J8tGrdXq4D%2BmD5I%2FPeaxvzsEc6Yj%2FNevCx9%2B5ltr4h4nFJfET7uVbR7j4WfnPUy4%2BAVepbXgFrY%2FKHW9%2BLlE2uDW6TPLq4c8440nUaV4U668aajQOQSBDa2LnjeR%2BcQ%2Bbqx%2Ft8ns8YRTo8KCU0u6JoKXmsLHkaJx9TYXT7s%2BuWxlr95gUczfrnkiwreUauvQaDMGg8qA6DD2LJB3%2FeL%2BuMEh7LGU9DpOs%2BqBVldpkR59COvKEretd2XXhBOpvJIaHqF0hUETomFEvXZJx%2BE5Vfa7tnoYK833%2FY1A9NFZAGXdGU6Wdz0wX7Um9BAxj3MLPskb0GOqUB9AZMsdL6MYmFZyuuqvqP7JVw58Ru7NnwA9r6xiDICPGZgACex9fPAb2QxtpEFqHXUN4RNFlqDt9xrC0RinBHT2VQoIfJMDHSqLGX1ohzzMlJUXWTLszUJntyp9LMkkkdnGOeRZAPo9VQyWZWCLZXeO7iLA1Xso4iOpdFQ7pGe9n3tRlSyDCsC6MkNy1XEGF3CSagX6%2BuhTXUwXkljypGHrxuOZgJ&X-Amz-Signature=d50b953e34f4ec75aa0eb4e50f35067350ecd85e02044c2a715f5a94a0afa432&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDKXJO23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCmhci%2FXcCpRIAArjrzEFpqLGejOa5mBA1gjKCbFIVMqwIgDiF9uVn%2F4as2BAxEZ6T1stIYe7pDDUlggO3c%2BQgxS9oq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMAwQWpdOQi%2FvaCMLCrcA2nQqjCU3wzVj289SO4Nz0QTur7TioM8rmAxzvdaP5AYzGrlkXGmJtJik1e%2Fn2nBVzyNRDbx%2BebsvtiB%2FHIyIVSXFw673Sl9sfRNkFasNE0rYSFeiSBr59jSOtfQIJSUdKJELwmo9WJSG4UNbYVoTzhG4jo4y883F8DlplIt9ZIiQ0ICmehAnEEhKQoQHDsbN6XX0Ss02ydIO4%2FUcI6YLJYFPu1ZoW1m0zEr7k2lHzn4dv8oiKBDcU0NWj38Lf%2B26AYX2j70e17r4dhTKJBtastBH4c5lyXxnnbDCOEPdJGl%2Brn2K248mA973dggy8J8tGrdXq4D%2BmD5I%2FPeaxvzsEc6Yj%2FNevCx9%2B5ltr4h4nFJfET7uVbR7j4WfnPUy4%2BAVepbXgFrY%2FKHW9%2BLlE2uDW6TPLq4c8440nUaV4U668aajQOQSBDa2LnjeR%2BcQ%2Bbqx%2Ft8ns8YRTo8KCU0u6JoKXmsLHkaJx9TYXT7s%2BuWxlr95gUczfrnkiwreUauvQaDMGg8qA6DD2LJB3%2FeL%2BuMEh7LGU9DpOs%2BqBVldpkR59COvKEretd2XXhBOpvJIaHqF0hUETomFEvXZJx%2BE5Vfa7tnoYK833%2FY1A9NFZAGXdGU6Wdz0wX7Um9BAxj3MLPskb0GOqUB9AZMsdL6MYmFZyuuqvqP7JVw58Ru7NnwA9r6xiDICPGZgACex9fPAb2QxtpEFqHXUN4RNFlqDt9xrC0RinBHT2VQoIfJMDHSqLGX1ohzzMlJUXWTLszUJntyp9LMkkkdnGOeRZAPo9VQyWZWCLZXeO7iLA1Xso4iOpdFQ7pGe9n3tRlSyDCsC6MkNy1XEGF3CSagX6%2BuhTXUwXkljypGHrxuOZgJ&X-Amz-Signature=b7ec8e5a61d2057c3468e2c5e8d14afed262b7000f9d06031f6c98169ee9f0cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDKXJO23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCmhci%2FXcCpRIAArjrzEFpqLGejOa5mBA1gjKCbFIVMqwIgDiF9uVn%2F4as2BAxEZ6T1stIYe7pDDUlggO3c%2BQgxS9oq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMAwQWpdOQi%2FvaCMLCrcA2nQqjCU3wzVj289SO4Nz0QTur7TioM8rmAxzvdaP5AYzGrlkXGmJtJik1e%2Fn2nBVzyNRDbx%2BebsvtiB%2FHIyIVSXFw673Sl9sfRNkFasNE0rYSFeiSBr59jSOtfQIJSUdKJELwmo9WJSG4UNbYVoTzhG4jo4y883F8DlplIt9ZIiQ0ICmehAnEEhKQoQHDsbN6XX0Ss02ydIO4%2FUcI6YLJYFPu1ZoW1m0zEr7k2lHzn4dv8oiKBDcU0NWj38Lf%2B26AYX2j70e17r4dhTKJBtastBH4c5lyXxnnbDCOEPdJGl%2Brn2K248mA973dggy8J8tGrdXq4D%2BmD5I%2FPeaxvzsEc6Yj%2FNevCx9%2B5ltr4h4nFJfET7uVbR7j4WfnPUy4%2BAVepbXgFrY%2FKHW9%2BLlE2uDW6TPLq4c8440nUaV4U668aajQOQSBDa2LnjeR%2BcQ%2Bbqx%2Ft8ns8YRTo8KCU0u6JoKXmsLHkaJx9TYXT7s%2BuWxlr95gUczfrnkiwreUauvQaDMGg8qA6DD2LJB3%2FeL%2BuMEh7LGU9DpOs%2BqBVldpkR59COvKEretd2XXhBOpvJIaHqF0hUETomFEvXZJx%2BE5Vfa7tnoYK833%2FY1A9NFZAGXdGU6Wdz0wX7Um9BAxj3MLPskb0GOqUB9AZMsdL6MYmFZyuuqvqP7JVw58Ru7NnwA9r6xiDICPGZgACex9fPAb2QxtpEFqHXUN4RNFlqDt9xrC0RinBHT2VQoIfJMDHSqLGX1ohzzMlJUXWTLszUJntyp9LMkkkdnGOeRZAPo9VQyWZWCLZXeO7iLA1Xso4iOpdFQ7pGe9n3tRlSyDCsC6MkNy1XEGF3CSagX6%2BuhTXUwXkljypGHrxuOZgJ&X-Amz-Signature=000f1ec6b04d944dbb9ddbb92e2950b0c8feb441c7f73b1256962db8776064af&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XE2ODXTD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFDzuK28js%2FI33vATpxE81tgfalXpvN1gyD5ZLuBG%2FmrAiAG2LOZUdaN4DaipAKhc%2BHqvx19LeyvYJI1lHFvnidtVCr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMA4J0fsHIbLDk3QGZKtwDgZn%2FGc6CQWRA%2FTZ0jzeEt%2FUrz4Zwqrk%2FOhwCCQo54XpjSNSM3D0k2ta2ArZRXv0oTUIOTUCUmIMqmVg8gaEBg%2FHA8istIM2UKIQPV4A0CmxIDs2rivgfSaHqdL34G5E3cEGGcXGzbqZ1GrjwZdpQas6k2riQIhEeMg0%2FLT4XGWFBKP7NCkTJZfiDsWrSkXc2jj5MMP29s%2BgLVx1p%2Bxg0L57iMYROsPpz%2BgPSyW9jjPsmKDNNz0L9Z%2F4G5ODARRy6%2BYd0gM0%2BNJ7YgArE2sBb69wmcx1udrDkVlUGOqMlXAuKQ6AHYe2BPvWGAHX1y726%2FqSkxQBDfMzLhFTbpI%2B6SN51gf8K34EHwo5SgC0rvgenAUJeS4xUTuaSXr7zYCEnLnoH0m71fFnMBoPZBpWI96QPsGbJquCfboMpQymK%2FVhwJcQsQR3c5H2XNN44doTsc3zVIA%2B3K46jsgiXBzj95UitXPgWVZC0zGwDW1DD7fQyELl8D3uze2umW%2BK%2F9w6kBxjP2dXKdoAjxr%2B%2BZik34EtfG6tsGQbg5KY2GmaQT9JUyLclLuJEbOrpzRrkmzd30auFcvFm6v2MCJiP429o369nHn5uJYkWZ1gWgtVU1pZsMDNtXVYamCKbm9Ywn%2ByRvQY6pgHp5McPp9jNcWnVmQuC0%2FRsCCRRltu9Zaq4VD69lZjElZdrfO03g2%2BExQjdFLw%2Fgl9EZQHt6tgb1ng1jPw5LmseoCxdmseJM3uwIy4CgnkbA1EffwhUgz15RAc1hC7PladVHbXmPbTzPwxstVN0zCXq%2F5hJvogfL7ldg0PmRR%2BB147vlldRiSvUF252kpwdNK9H1GoippG91Pp2IcekeZkzB8IPlg51&X-Amz-Signature=0a51aeedcc6100bf6216585c2907a092f77fc5a9fd31b24a4333d494239f5c99&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRVJ5P2V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDpQa1kVvVV4MTzmA2yN%2FX55Mar19cCW2xfZv0NQb7pKwIhAI%2FpP0yxFnmtFcB1i%2F3vd9RQHoq1OopfOKpudJZCULIfKv8DCFoQABoMNjM3NDIzMTgzODA1IgxEX2lllHbtMm2zgjwq3APBaE7ao0wNW7ekzZSXoMu1Bkp3GRXK7jPref2W3TSBgIF99P%2BOf0A1G%2FaySzwP9aPt4te9mpoQLJEkQyukptzT%2FAVZL3e88FudqQ1%2BqSt3GhVN81p%2BT9tZpOGh8PqjXQJu5CoRLQLsDF9tJnSDXkujZNT2vPPch96LiM7qexiZ4uVc32o4L%2BhII0MpPaQ63gTlTayIJlcgd73pacDugH9hIWcTCP476dHVHWWQBxkNGMzDLgqmWYZnmetu9rNGhavN%2FLnGROHR%2FdA%2Fq90Zdjsllwz1uCJv4ITmSBUoofZ%2Bq3QqLm7FvHS8%2FCurhl8lXW7jyaUPR%2BD3trEdV5aijkS5ut1Pm%2Bvh9bYEOBtWSyr4Ay2oT4Rb1oCM4tlud3tK5JyTZVnWV%2FGsG4y6E%2FvrwXP5k0jg4vZZY43o1TcRTVZlOGRL%2Bq%2FyIBU2Lhe%2FcwnfDBEImY8iiuUwx7GLkRew0CgvicYyU0c1Y9vhMjpGVq%2BmOGzf0cfZUe2Kc5ajiDGASNgqoYcjxDKGObsn1%2BzbmlWjQKLwK4nXI2%2FrtG8drKiKf1an4KGMvEBFM7g9%2BbD3gmNFqzVNv5M4ViDO%2FSQCMbylRnEB8GSl1slxGlN%2B2OVva2lremoAgGnjfQ5HYzCh7JG9BjqkARshbkIC2crlmJwFGAaN%2Fsry8tsYfQoTnflJhFZPMqTTy5NWakB3J%2FqkALgetrTmPHycr0ToKSp%2BfOTl9KcQX3mzPg8PON3032nbQql0lhLp%2FEyIameEvFRTZMYTjzyZDFo8lK0lWHH2VWtTGyReOHfqE6QdpdHYhumq39iGCCOKKVDpvVpWrJAbpY7vnP%2FocwggPJ1tft2683Fb9L%2FOlaapvU2y&X-Amz-Signature=02a06840332202a28d9d843de26caa17351476677d809ea7718bba4d20aafdf6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WROBA32P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDEQfRdX7NjEOR3hf40kex7vPN%2F13xXW2QQBDrtBS39dwIhANArBfHqARoFkkcn7KnwuH3FsEC2St3wvysn%2FDQXadIjKv8DCFoQABoMNjM3NDIzMTgzODA1IgwoYxri8rr6%2BtDgzlcq3AN4z5lgsqhSx%2BIq4ic%2F57HymQngRl41%2BymLwYNiaEIbFDSi1lLb%2BykMEKa%2F01FS8If%2FeKwWaKEaUFL1S2cEcXWS2VQt6EQePcr1sHZQxfMdngitQiUdKxULsT2EUb9hnxGmFgP9thef%2BiuCX%2FK7M2MTanVPUHOObvaHfdkrw75hJzRdYz2vP3%2F9xcBuPqrGF7wSSWzND0aQx9EtcYm8f%2BJa5xS83f479j1rL5rFALT%2B3Wi1c6f2IEx9vNOdC5ysVhOme9IyeDSwN%2FCN7FlhNYmlawu3ne9kuoYyQrY8YGXtz4CaLqk3fnrpboXamthtARAftEm20q%2F2O9Fv7qCcB9qFMzOOhcpZ1Lq2VP7VHENziLkg7Xly944CqCId%2BfDVYHxls7ZQorkwRb76mOCakuBAofcoX%2BEJ0aRuIFqzrZpU%2Btitjp%2Fdko1bcb04aKByn1eyln6LnsaH8InS%2Bq7fVU8EFI3frXVQnvRWnWDqJKyMdIBI2%2FprEp3HWg0MG1K4Y7wjk5gMW68Jq5wJRGBOyScoz2H31fWNWC45%2BucWvm1QpE8Ss4%2F9JtPrK62abw%2F2Ko4TH3nr5UkmaGZJlOJTjttLIJ4tEl9oH5DMRgl1T3EhKS9m6SerLy6UFv12aDDT65G9BjqkAaCtlsJ0C5iN5kIbDVucSsq%2Fo6DfhIs7WFXA6dJak%2BWEjZotXr1ePP2WTzI2b4%2B9sKE6Jx98Ql9KHBMwYt%2BAXK82uOCF62vyT31EU8GQYWJ7aMKPjTU5PfkLtDFs%2B2gQRQ86BazXpTnvpC9fRXYeUTrUlil4MqW%2ByLUY%2F9yQcwrgJDmEIvBgkdtoDyBcNV7gXHOTuMHoqxjGflLvxmHl6Xv%2FWRQk&X-Amz-Signature=ed2ade3480ea604eae1b56af8473d39f951f088bb9aac99e0a3e546c6d754f3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6KOSXHG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIDzK7f3sSkkqx%2B7u1%2FzaAYiVMVD%2Bjc%2Bqc%2F4IyEtOe%2BTlAiAKppKIVH48UnqPoqEHZYaCNDmJeyQmaXoYgIACVdYHEyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMl%2Fp40bSinrpGekv6KtwD1pzodinO2Eznt7tfk7INopmyJyrHv%2FCIvUxd1PgFAPe%2FXD0ZYgilludpmsq7NMjvBD6d9rcug7SwBjpCcp75%2BphUn08KY7hnJSfT74J9gtkkFsY3o7uMCOhMsKh2FC330w%2FsXjkS9AeeEB0t1uBhPFW8FGelppOe%2F2vOvNgI%2F4GRBhrjBlAsFTY7fnOWt5LGrijp0XMsnpr6HkHbqHFtEJ46GvWLV9cGyVijn0wLPTJhXbo09imCks8MiFtBO5OuFEBby5JLyEZPs3CSPhWLivR7WJraj9mQV6Ni0%2BFfkbRHbNt%2BwBGzmRLahfmmMc0l3LuwoglipHeHNSZLkMVhnP9Hkc%2B3bei48ljjdwSDlUmDlrOQSEL44jigRU21uLmOUsU838JMD%2BcUgWVnpfbR13BnoJCGhzkZT4Ss%2FSh38QPl5gte55sWjsgPEPa%2F4uFXd7dfZNtsEDvnKiaWlRtqc%2BmJCg52ba5hnOyV%2Br79QSZWUPoJ0KBlR8zMg8a7LlrXbbDKj56Ysm6mpHVCPjxUg5cCN5XlNbiQzvQYN%2BfNrrWTVzE31VyNelJgcT6J8seYU8LEgL2dhZoNiiS838J8nGP4tSO4ccdzGLCItoC%2BJceN%2Bo6AANgDFu%2BOR8UwhuyRvQY6pgG7iiDGOzGZ7k%2BKl%2Bkaw2dWrrFe0C5XBb9MdONupE57ZjJ3g0fN3wuUHTPw04ktPzpXR5oXxgn2vg3EPMDEbRplW3v0pqWq78nYej%2FUHyy1afiVGCisUwojQ3NrFn9N5%2BwGLOjY1ORrBY2wMKkfx20dtVU%2FV31lVEcXP4SpFJ7%2F8rQjx6Acy6mpdloieUltvtNT1cikB%2B9AvUHSwJa8hnX0sHdKZhYX&X-Amz-Signature=711e55ca0c2560342337307c41ea9e39384a317288a9544333102c4eac94c558&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6KOSXHG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIDzK7f3sSkkqx%2B7u1%2FzaAYiVMVD%2Bjc%2Bqc%2F4IyEtOe%2BTlAiAKppKIVH48UnqPoqEHZYaCNDmJeyQmaXoYgIACVdYHEyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMl%2Fp40bSinrpGekv6KtwD1pzodinO2Eznt7tfk7INopmyJyrHv%2FCIvUxd1PgFAPe%2FXD0ZYgilludpmsq7NMjvBD6d9rcug7SwBjpCcp75%2BphUn08KY7hnJSfT74J9gtkkFsY3o7uMCOhMsKh2FC330w%2FsXjkS9AeeEB0t1uBhPFW8FGelppOe%2F2vOvNgI%2F4GRBhrjBlAsFTY7fnOWt5LGrijp0XMsnpr6HkHbqHFtEJ46GvWLV9cGyVijn0wLPTJhXbo09imCks8MiFtBO5OuFEBby5JLyEZPs3CSPhWLivR7WJraj9mQV6Ni0%2BFfkbRHbNt%2BwBGzmRLahfmmMc0l3LuwoglipHeHNSZLkMVhnP9Hkc%2B3bei48ljjdwSDlUmDlrOQSEL44jigRU21uLmOUsU838JMD%2BcUgWVnpfbR13BnoJCGhzkZT4Ss%2FSh38QPl5gte55sWjsgPEPa%2F4uFXd7dfZNtsEDvnKiaWlRtqc%2BmJCg52ba5hnOyV%2Br79QSZWUPoJ0KBlR8zMg8a7LlrXbbDKj56Ysm6mpHVCPjxUg5cCN5XlNbiQzvQYN%2BfNrrWTVzE31VyNelJgcT6J8seYU8LEgL2dhZoNiiS838J8nGP4tSO4ccdzGLCItoC%2BJceN%2Bo6AANgDFu%2BOR8UwhuyRvQY6pgG7iiDGOzGZ7k%2BKl%2Bkaw2dWrrFe0C5XBb9MdONupE57ZjJ3g0fN3wuUHTPw04ktPzpXR5oXxgn2vg3EPMDEbRplW3v0pqWq78nYej%2FUHyy1afiVGCisUwojQ3NrFn9N5%2BwGLOjY1ORrBY2wMKkfx20dtVU%2FV31lVEcXP4SpFJ7%2F8rQjx6Acy6mpdloieUltvtNT1cikB%2B9AvUHSwJa8hnX0sHdKZhYX&X-Amz-Signature=242d19d81e1ee8b731e751c743984440a20d978dd6c26d7659fc3ad9afd2889f&X-Amz-SignedHeaders=host&x-id=GetObject)

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
