

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3NOORTB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCM8YqRdkhDd5lnY1zn83XULn4Sl8e9hj5CIzHfDwdRyQIhAKGRQ1Ktd7ufYslmqk%2ByJFJdZy%2BG7fRhmYK%2BcM74L%2BrfKv8DCCYQABoMNjM3NDIzMTgzODA1IgxuqqBa3eMJJBIhDrcq3AO10ipfYsbizSVeCuj05s5Pc%2F5hUHNANm3ipYMs4CQ310ytDwP67Tl4RR5XbWpPl0zUQoOLwq34LJQnheUWrSNEcY15PdUnKsz%2FdLh1zeQGWtdW5AXRFCD8F8tuuj%2B7AQS516Obg0kfQHZSFX0VsCOyzT6HnKpkgFjyrw%2FzzlYpOe9ZUi48t%2FcDE467Fjc7fgRJ3qoekH2Nmaye6VyNn72YOVrES%2Bkj%2BG42f53fqgcrlPWNKp%2FPc6poK2gVlGq%2B4HG6RZUDpDq5NJEwrlxzyPosaH5w8aLS8q8qB7b%2B4h3DciQtGd90x6s7LnyRIstk%2FsqGgQxNdeHYc8kjats%2B7gcqDDuifAMCOIaz5H%2FGL9BbbBbIrwlYv8KQCZecKMRN9ZkVboTvUy9yZ75WRpo%2FzaNPW%2FUeW8V7wJpDn9JssZ73vxIiuqXGQLI84oibUXw%2FDmkSRjQ6UZlDppjowULEwGWqjQo%2B6qMBZDcEQUTPy5c5DGfE%2BsQW1UWmYiNb3m%2B7gpiiRPEueaSeOwgObdjOJag88nlbNFdFk2b3BFc2uQX3GXGd3VuxrrkeaqcPRO8OoEWep%2F74JOFBL%2Bft9wkV3E7qXk0otRjEkHqGWKeqDL%2Fkp1TK321HEtusNfJBozDmvoa9BjqkAe6GjtFuP0V34a0gT6sZxKWIdERsM%2FRst%2FtQhTWepQurMJBcy2e9aLyoziZgQzpwZutV99ej1lnUyP6%2BHffPY%2F%2Be4VA9YZsWSJK7GG%2BJtoTZgYudSD8kanXxpg46XPGTt9Ema%2FXUWcxmRx4OcsO0bQ9zbbGr3qiXi4IKHsltdcynlsNDOozfMk%2FlELSfZbIUkjBVDYopV3sRQALB8hs9%2FeOvnjSS&X-Amz-Signature=8e4b06b5f7339ac5b92d39b64ceb324888600c9dafa074d34bc712e4198f0697&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3NOORTB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCM8YqRdkhDd5lnY1zn83XULn4Sl8e9hj5CIzHfDwdRyQIhAKGRQ1Ktd7ufYslmqk%2ByJFJdZy%2BG7fRhmYK%2BcM74L%2BrfKv8DCCYQABoMNjM3NDIzMTgzODA1IgxuqqBa3eMJJBIhDrcq3AO10ipfYsbizSVeCuj05s5Pc%2F5hUHNANm3ipYMs4CQ310ytDwP67Tl4RR5XbWpPl0zUQoOLwq34LJQnheUWrSNEcY15PdUnKsz%2FdLh1zeQGWtdW5AXRFCD8F8tuuj%2B7AQS516Obg0kfQHZSFX0VsCOyzT6HnKpkgFjyrw%2FzzlYpOe9ZUi48t%2FcDE467Fjc7fgRJ3qoekH2Nmaye6VyNn72YOVrES%2Bkj%2BG42f53fqgcrlPWNKp%2FPc6poK2gVlGq%2B4HG6RZUDpDq5NJEwrlxzyPosaH5w8aLS8q8qB7b%2B4h3DciQtGd90x6s7LnyRIstk%2FsqGgQxNdeHYc8kjats%2B7gcqDDuifAMCOIaz5H%2FGL9BbbBbIrwlYv8KQCZecKMRN9ZkVboTvUy9yZ75WRpo%2FzaNPW%2FUeW8V7wJpDn9JssZ73vxIiuqXGQLI84oibUXw%2FDmkSRjQ6UZlDppjowULEwGWqjQo%2B6qMBZDcEQUTPy5c5DGfE%2BsQW1UWmYiNb3m%2B7gpiiRPEueaSeOwgObdjOJag88nlbNFdFk2b3BFc2uQX3GXGd3VuxrrkeaqcPRO8OoEWep%2F74JOFBL%2Bft9wkV3E7qXk0otRjEkHqGWKeqDL%2Fkp1TK321HEtusNfJBozDmvoa9BjqkAe6GjtFuP0V34a0gT6sZxKWIdERsM%2FRst%2FtQhTWepQurMJBcy2e9aLyoziZgQzpwZutV99ej1lnUyP6%2BHffPY%2F%2Be4VA9YZsWSJK7GG%2BJtoTZgYudSD8kanXxpg46XPGTt9Ema%2FXUWcxmRx4OcsO0bQ9zbbGr3qiXi4IKHsltdcynlsNDOozfMk%2FlELSfZbIUkjBVDYopV3sRQALB8hs9%2FeOvnjSS&X-Amz-Signature=6987dc10230b22a4130920c0631c0b51779719a36631bca8b500540650a9ee0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3NOORTB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCM8YqRdkhDd5lnY1zn83XULn4Sl8e9hj5CIzHfDwdRyQIhAKGRQ1Ktd7ufYslmqk%2ByJFJdZy%2BG7fRhmYK%2BcM74L%2BrfKv8DCCYQABoMNjM3NDIzMTgzODA1IgxuqqBa3eMJJBIhDrcq3AO10ipfYsbizSVeCuj05s5Pc%2F5hUHNANm3ipYMs4CQ310ytDwP67Tl4RR5XbWpPl0zUQoOLwq34LJQnheUWrSNEcY15PdUnKsz%2FdLh1zeQGWtdW5AXRFCD8F8tuuj%2B7AQS516Obg0kfQHZSFX0VsCOyzT6HnKpkgFjyrw%2FzzlYpOe9ZUi48t%2FcDE467Fjc7fgRJ3qoekH2Nmaye6VyNn72YOVrES%2Bkj%2BG42f53fqgcrlPWNKp%2FPc6poK2gVlGq%2B4HG6RZUDpDq5NJEwrlxzyPosaH5w8aLS8q8qB7b%2B4h3DciQtGd90x6s7LnyRIstk%2FsqGgQxNdeHYc8kjats%2B7gcqDDuifAMCOIaz5H%2FGL9BbbBbIrwlYv8KQCZecKMRN9ZkVboTvUy9yZ75WRpo%2FzaNPW%2FUeW8V7wJpDn9JssZ73vxIiuqXGQLI84oibUXw%2FDmkSRjQ6UZlDppjowULEwGWqjQo%2B6qMBZDcEQUTPy5c5DGfE%2BsQW1UWmYiNb3m%2B7gpiiRPEueaSeOwgObdjOJag88nlbNFdFk2b3BFc2uQX3GXGd3VuxrrkeaqcPRO8OoEWep%2F74JOFBL%2Bft9wkV3E7qXk0otRjEkHqGWKeqDL%2Fkp1TK321HEtusNfJBozDmvoa9BjqkAe6GjtFuP0V34a0gT6sZxKWIdERsM%2FRst%2FtQhTWepQurMJBcy2e9aLyoziZgQzpwZutV99ej1lnUyP6%2BHffPY%2F%2Be4VA9YZsWSJK7GG%2BJtoTZgYudSD8kanXxpg46XPGTt9Ema%2FXUWcxmRx4OcsO0bQ9zbbGr3qiXi4IKHsltdcynlsNDOozfMk%2FlELSfZbIUkjBVDYopV3sRQALB8hs9%2FeOvnjSS&X-Amz-Signature=6d3f89f17a8ab3b459f056338e988edc02ca959cbd1e287fb3f9520ab1099d53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRLULTXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDq5yEf%2ByT2IlgfVvXtm%2BlGU7AKzUQOO6%2Bj7cYj1Rx7WQIhAP%2BloKTjzb3XX5DKEFgWlQCk7h4vnY1HWPJUPv7SsHSQKv8DCCYQABoMNjM3NDIzMTgzODA1IgxvZKffQejrKsZh1w4q3ANiQOguiaKau1MxzNAeR96ZFLTZNqI8nGL4ZrlDKXqeTB82cpen8a6PRnCfKZQbhM%2Ba2pFtKYL1FzJy2%2BPg8AwepCjSkXlqBZLxZKMjkAB4zYSB5S9QGUtX3uQl88ICRJKOgLccYvMYT46CwZzh1ciKPz%2B4%2BzgJMRn6v8yN%2F27TaG5gnEEu91CRbt3mteHzgbAtaJP5mhavd48EMUOk9gokElOaNZeQYfCLhxjV93tb4fKpsdslEzH1JV4zLxH3uJ9nXucyCNjw6Ik0yk9M2DlfeiWakLPByTxsaZPHZg2e9AeA302r5yjwHSxtH5nKvVrW16Q5%2BwCzTnJINYIUTgDoF8HpmHnd%2BK7vJYg5gLNFuU%2FGaXC77W58sdOHIQY2w%2F5clWKG1kzj5NO5aAUj%2Bdl8XPe%2F9aGrNhHpf5uyIsoMz1B7D0LGxYXWdoCteC9Ek57cxIWhG61W68028i6XaVvJUkHsdSHOMy3nAEZmLbYt0IVHcBHu2gOtJVmsYVaESRxdqy1BTtPRGVshmRXyA5o5cAdOtEBhyotv8YxNmQu6O3%2FkaR%2F2v783%2BSWpCkEUqb9yn%2FauehYrod%2FMJiG7HPh9LVGKXdvMvzRa5KkH6DiIOTDf8Ay9f%2BeGtwq7EDCUv4a9BjqkASYUuhgEPF0SFlazAaondS3S1i%2BAbsquFS65DWP0ISyszSZIKLX9G63PAXDP%2BhRGXR%2FxPSwTKVn7cyH8Yr4b1UO243SUYwR5khUvMPPzvRy9HDisnyj1AFbPi0mR3Y2D%2Bl4kP%2BQ9S3lclYIGWGC%2FlDXToz0Ditjo08vIPO3JEEpaImiwkZ4rWzV%2FB1pKcL7%2B1Tjpu6V%2BIpZvBctATCeIOYsKWgVX&X-Amz-Signature=1a549a0d09eaaa18fa233a011ff6c70e00f5bc5d8e999ff1b29fec6e63a97cc5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRLULTXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDq5yEf%2ByT2IlgfVvXtm%2BlGU7AKzUQOO6%2Bj7cYj1Rx7WQIhAP%2BloKTjzb3XX5DKEFgWlQCk7h4vnY1HWPJUPv7SsHSQKv8DCCYQABoMNjM3NDIzMTgzODA1IgxvZKffQejrKsZh1w4q3ANiQOguiaKau1MxzNAeR96ZFLTZNqI8nGL4ZrlDKXqeTB82cpen8a6PRnCfKZQbhM%2Ba2pFtKYL1FzJy2%2BPg8AwepCjSkXlqBZLxZKMjkAB4zYSB5S9QGUtX3uQl88ICRJKOgLccYvMYT46CwZzh1ciKPz%2B4%2BzgJMRn6v8yN%2F27TaG5gnEEu91CRbt3mteHzgbAtaJP5mhavd48EMUOk9gokElOaNZeQYfCLhxjV93tb4fKpsdslEzH1JV4zLxH3uJ9nXucyCNjw6Ik0yk9M2DlfeiWakLPByTxsaZPHZg2e9AeA302r5yjwHSxtH5nKvVrW16Q5%2BwCzTnJINYIUTgDoF8HpmHnd%2BK7vJYg5gLNFuU%2FGaXC77W58sdOHIQY2w%2F5clWKG1kzj5NO5aAUj%2Bdl8XPe%2F9aGrNhHpf5uyIsoMz1B7D0LGxYXWdoCteC9Ek57cxIWhG61W68028i6XaVvJUkHsdSHOMy3nAEZmLbYt0IVHcBHu2gOtJVmsYVaESRxdqy1BTtPRGVshmRXyA5o5cAdOtEBhyotv8YxNmQu6O3%2FkaR%2F2v783%2BSWpCkEUqb9yn%2FauehYrod%2FMJiG7HPh9LVGKXdvMvzRa5KkH6DiIOTDf8Ay9f%2BeGtwq7EDCUv4a9BjqkASYUuhgEPF0SFlazAaondS3S1i%2BAbsquFS65DWP0ISyszSZIKLX9G63PAXDP%2BhRGXR%2FxPSwTKVn7cyH8Yr4b1UO243SUYwR5khUvMPPzvRy9HDisnyj1AFbPi0mR3Y2D%2Bl4kP%2BQ9S3lclYIGWGC%2FlDXToz0Ditjo08vIPO3JEEpaImiwkZ4rWzV%2FB1pKcL7%2B1Tjpu6V%2BIpZvBctATCeIOYsKWgVX&X-Amz-Signature=aa670eef9176ae73b741ccbafe2d3cca49f04e0928e09449a77d4604c8ac1b8b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRLULTXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDq5yEf%2ByT2IlgfVvXtm%2BlGU7AKzUQOO6%2Bj7cYj1Rx7WQIhAP%2BloKTjzb3XX5DKEFgWlQCk7h4vnY1HWPJUPv7SsHSQKv8DCCYQABoMNjM3NDIzMTgzODA1IgxvZKffQejrKsZh1w4q3ANiQOguiaKau1MxzNAeR96ZFLTZNqI8nGL4ZrlDKXqeTB82cpen8a6PRnCfKZQbhM%2Ba2pFtKYL1FzJy2%2BPg8AwepCjSkXlqBZLxZKMjkAB4zYSB5S9QGUtX3uQl88ICRJKOgLccYvMYT46CwZzh1ciKPz%2B4%2BzgJMRn6v8yN%2F27TaG5gnEEu91CRbt3mteHzgbAtaJP5mhavd48EMUOk9gokElOaNZeQYfCLhxjV93tb4fKpsdslEzH1JV4zLxH3uJ9nXucyCNjw6Ik0yk9M2DlfeiWakLPByTxsaZPHZg2e9AeA302r5yjwHSxtH5nKvVrW16Q5%2BwCzTnJINYIUTgDoF8HpmHnd%2BK7vJYg5gLNFuU%2FGaXC77W58sdOHIQY2w%2F5clWKG1kzj5NO5aAUj%2Bdl8XPe%2F9aGrNhHpf5uyIsoMz1B7D0LGxYXWdoCteC9Ek57cxIWhG61W68028i6XaVvJUkHsdSHOMy3nAEZmLbYt0IVHcBHu2gOtJVmsYVaESRxdqy1BTtPRGVshmRXyA5o5cAdOtEBhyotv8YxNmQu6O3%2FkaR%2F2v783%2BSWpCkEUqb9yn%2FauehYrod%2FMJiG7HPh9LVGKXdvMvzRa5KkH6DiIOTDf8Ay9f%2BeGtwq7EDCUv4a9BjqkASYUuhgEPF0SFlazAaondS3S1i%2BAbsquFS65DWP0ISyszSZIKLX9G63PAXDP%2BhRGXR%2FxPSwTKVn7cyH8Yr4b1UO243SUYwR5khUvMPPzvRy9HDisnyj1AFbPi0mR3Y2D%2Bl4kP%2BQ9S3lclYIGWGC%2FlDXToz0Ditjo08vIPO3JEEpaImiwkZ4rWzV%2FB1pKcL7%2B1Tjpu6V%2BIpZvBctATCeIOYsKWgVX&X-Amz-Signature=5651724db8d651c201dc81f81a5e4beea43de6b3bb0e02ff38a16e3d5b7c19f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRLULTXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDq5yEf%2ByT2IlgfVvXtm%2BlGU7AKzUQOO6%2Bj7cYj1Rx7WQIhAP%2BloKTjzb3XX5DKEFgWlQCk7h4vnY1HWPJUPv7SsHSQKv8DCCYQABoMNjM3NDIzMTgzODA1IgxvZKffQejrKsZh1w4q3ANiQOguiaKau1MxzNAeR96ZFLTZNqI8nGL4ZrlDKXqeTB82cpen8a6PRnCfKZQbhM%2Ba2pFtKYL1FzJy2%2BPg8AwepCjSkXlqBZLxZKMjkAB4zYSB5S9QGUtX3uQl88ICRJKOgLccYvMYT46CwZzh1ciKPz%2B4%2BzgJMRn6v8yN%2F27TaG5gnEEu91CRbt3mteHzgbAtaJP5mhavd48EMUOk9gokElOaNZeQYfCLhxjV93tb4fKpsdslEzH1JV4zLxH3uJ9nXucyCNjw6Ik0yk9M2DlfeiWakLPByTxsaZPHZg2e9AeA302r5yjwHSxtH5nKvVrW16Q5%2BwCzTnJINYIUTgDoF8HpmHnd%2BK7vJYg5gLNFuU%2FGaXC77W58sdOHIQY2w%2F5clWKG1kzj5NO5aAUj%2Bdl8XPe%2F9aGrNhHpf5uyIsoMz1B7D0LGxYXWdoCteC9Ek57cxIWhG61W68028i6XaVvJUkHsdSHOMy3nAEZmLbYt0IVHcBHu2gOtJVmsYVaESRxdqy1BTtPRGVshmRXyA5o5cAdOtEBhyotv8YxNmQu6O3%2FkaR%2F2v783%2BSWpCkEUqb9yn%2FauehYrod%2FMJiG7HPh9LVGKXdvMvzRa5KkH6DiIOTDf8Ay9f%2BeGtwq7EDCUv4a9BjqkASYUuhgEPF0SFlazAaondS3S1i%2BAbsquFS65DWP0ISyszSZIKLX9G63PAXDP%2BhRGXR%2FxPSwTKVn7cyH8Yr4b1UO243SUYwR5khUvMPPzvRy9HDisnyj1AFbPi0mR3Y2D%2Bl4kP%2BQ9S3lclYIGWGC%2FlDXToz0Ditjo08vIPO3JEEpaImiwkZ4rWzV%2FB1pKcL7%2B1Tjpu6V%2BIpZvBctATCeIOYsKWgVX&X-Amz-Signature=03ea5ca6e149deb1860a228c7ca6a56c19900edac8873c55d495673be6a888b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRLULTXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDq5yEf%2ByT2IlgfVvXtm%2BlGU7AKzUQOO6%2Bj7cYj1Rx7WQIhAP%2BloKTjzb3XX5DKEFgWlQCk7h4vnY1HWPJUPv7SsHSQKv8DCCYQABoMNjM3NDIzMTgzODA1IgxvZKffQejrKsZh1w4q3ANiQOguiaKau1MxzNAeR96ZFLTZNqI8nGL4ZrlDKXqeTB82cpen8a6PRnCfKZQbhM%2Ba2pFtKYL1FzJy2%2BPg8AwepCjSkXlqBZLxZKMjkAB4zYSB5S9QGUtX3uQl88ICRJKOgLccYvMYT46CwZzh1ciKPz%2B4%2BzgJMRn6v8yN%2F27TaG5gnEEu91CRbt3mteHzgbAtaJP5mhavd48EMUOk9gokElOaNZeQYfCLhxjV93tb4fKpsdslEzH1JV4zLxH3uJ9nXucyCNjw6Ik0yk9M2DlfeiWakLPByTxsaZPHZg2e9AeA302r5yjwHSxtH5nKvVrW16Q5%2BwCzTnJINYIUTgDoF8HpmHnd%2BK7vJYg5gLNFuU%2FGaXC77W58sdOHIQY2w%2F5clWKG1kzj5NO5aAUj%2Bdl8XPe%2F9aGrNhHpf5uyIsoMz1B7D0LGxYXWdoCteC9Ek57cxIWhG61W68028i6XaVvJUkHsdSHOMy3nAEZmLbYt0IVHcBHu2gOtJVmsYVaESRxdqy1BTtPRGVshmRXyA5o5cAdOtEBhyotv8YxNmQu6O3%2FkaR%2F2v783%2BSWpCkEUqb9yn%2FauehYrod%2FMJiG7HPh9LVGKXdvMvzRa5KkH6DiIOTDf8Ay9f%2BeGtwq7EDCUv4a9BjqkASYUuhgEPF0SFlazAaondS3S1i%2BAbsquFS65DWP0ISyszSZIKLX9G63PAXDP%2BhRGXR%2FxPSwTKVn7cyH8Yr4b1UO243SUYwR5khUvMPPzvRy9HDisnyj1AFbPi0mR3Y2D%2Bl4kP%2BQ9S3lclYIGWGC%2FlDXToz0Ditjo08vIPO3JEEpaImiwkZ4rWzV%2FB1pKcL7%2B1Tjpu6V%2BIpZvBctATCeIOYsKWgVX&X-Amz-Signature=c50156f430068b16d1032ed3c2506c5ea4cd6d50925997758f2dc52c2c93e633&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRLULTXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDq5yEf%2ByT2IlgfVvXtm%2BlGU7AKzUQOO6%2Bj7cYj1Rx7WQIhAP%2BloKTjzb3XX5DKEFgWlQCk7h4vnY1HWPJUPv7SsHSQKv8DCCYQABoMNjM3NDIzMTgzODA1IgxvZKffQejrKsZh1w4q3ANiQOguiaKau1MxzNAeR96ZFLTZNqI8nGL4ZrlDKXqeTB82cpen8a6PRnCfKZQbhM%2Ba2pFtKYL1FzJy2%2BPg8AwepCjSkXlqBZLxZKMjkAB4zYSB5S9QGUtX3uQl88ICRJKOgLccYvMYT46CwZzh1ciKPz%2B4%2BzgJMRn6v8yN%2F27TaG5gnEEu91CRbt3mteHzgbAtaJP5mhavd48EMUOk9gokElOaNZeQYfCLhxjV93tb4fKpsdslEzH1JV4zLxH3uJ9nXucyCNjw6Ik0yk9M2DlfeiWakLPByTxsaZPHZg2e9AeA302r5yjwHSxtH5nKvVrW16Q5%2BwCzTnJINYIUTgDoF8HpmHnd%2BK7vJYg5gLNFuU%2FGaXC77W58sdOHIQY2w%2F5clWKG1kzj5NO5aAUj%2Bdl8XPe%2F9aGrNhHpf5uyIsoMz1B7D0LGxYXWdoCteC9Ek57cxIWhG61W68028i6XaVvJUkHsdSHOMy3nAEZmLbYt0IVHcBHu2gOtJVmsYVaESRxdqy1BTtPRGVshmRXyA5o5cAdOtEBhyotv8YxNmQu6O3%2FkaR%2F2v783%2BSWpCkEUqb9yn%2FauehYrod%2FMJiG7HPh9LVGKXdvMvzRa5KkH6DiIOTDf8Ay9f%2BeGtwq7EDCUv4a9BjqkASYUuhgEPF0SFlazAaondS3S1i%2BAbsquFS65DWP0ISyszSZIKLX9G63PAXDP%2BhRGXR%2FxPSwTKVn7cyH8Yr4b1UO243SUYwR5khUvMPPzvRy9HDisnyj1AFbPi0mR3Y2D%2Bl4kP%2BQ9S3lclYIGWGC%2FlDXToz0Ditjo08vIPO3JEEpaImiwkZ4rWzV%2FB1pKcL7%2B1Tjpu6V%2BIpZvBctATCeIOYsKWgVX&X-Amz-Signature=a39d36fca57e5ae39acfc58df766f1fbc99172c36338655b3bcea0c1b3e53024&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOH5KWKK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIGDR0xIRJyuhLFBg9Zv3lncU9zexF9cDTNpg3I9iXxnnAiEAr78rf3K2MDC%2FGmQ4B6c3KBeMcmXg9q6GbBBggndHF9cq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAfRU41Jvc7eGZy5tCrcA6i1QNdVB1OedJnEkhRtijQvA26zDMyPQ9aADJAnAppk6ztbDpHMx2XwE5ZGoOmPAeNq%2Bs4xR7m%2B5L7g7AvXBMUB%2FtzaBw128CrTksHmieDXRpB2ic6YAvDXqpDGBJfpurIJ5p5oSbwMSzQ3H%2FocZGja6YePfQJpxp3GuulluyliHPQkRmU%2BzWbQFQL1LPz%2FVV6t11zRg72rFX117gMUt8PV%2FzwjtONLqssdRbptOQvs%2FuqkrUKDL7WovXum2p9sPj8vxyY%2FpjgNN6uD8KoxvXaFalWTGZ0RVXEskNSFpRJM4hYmA1xwb5AqaxogLMYM476zc%2BnAOie%2BL1u%2FUXL%2FqgBHWdTCejWDj5qgJAl%2FeMarSyW4hAPjEwZaZA0wuvOLfyTBtTOVC6OtIzMuXBxZNnAw8gui%2FsBm9eRPVlomOpD5GMTi3OwA1vfk3exx9rRjUen4P%2BnmWScJ3CdzU2MfdFVG4Q6NXxkEm%2BCmLPYA8ajbqb%2BqJVB04bEph3wCT3ISh8PR8Goy9c6owrTF1cyPrVVS%2BNicCZG0SrB9tSlU2pKjUJUt6PCrkTdc6qjqSpWYgIy30RQfGtQrpql5wlOcYLUUUMFRwamnt3pKkhioV7SzRKk7yRuzmAmQYiCVMLK%2Bhr0GOqUBnYYoiUaEyYBDcUnoQZX6Dxk8oQPTgGY3qEiF%2BdB24zMB7PwKhHEb%2BHUd03BXozqlor7hX6g7UBMMOP7gTE%2FjZUpApE6XueElpG0SWOJ7oDHvhsCLjjW10wHuAJMOyH7fdpHMXW17iFJLq3A6IYahsnUwyV3zoPUhkpu7H26t4s8Pn34g5I9lH0wTCNUkz1DIPcgDwCERwakbJ5DcDarjKyLsnX1z&X-Amz-Signature=06e1d60bedc069e263d7883906615b7494eed695969353ba6933cfde14e39b07&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2IQIV4T%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCcYcdG5X%2B3Nc2TQtZ7sjimkhWU0%2BND0ASQaTk9HACqkQIhANBpviQpgT7i8DGuxmxLQqaAw2VZhiJoVvdex9iKTIj1Kv8DCCYQABoMNjM3NDIzMTgzODA1IgxknRjs8N9Qn%2BmPOhYq3APfXorTlHHVGsZgk5Pm8wZ7HjgakLnKhW%2Fh51iLO%2B6BphRK7tXPUR5%2BBXbstSqeNTlgGaXBdS0GRqC02i8nRF6nY%2BgHxjzclz30XQqpBPr72YEnltfSu8ofud2BSpgMxBBMcjvbYO3sOFZhOrhHRQ9%2BR4mD1l0zKcLizil3l9WQywTRmb3%2F6Qs6EGGZE9GkVWpWHFmmtKZ%2FU%2F7oA94fiQ8ys57T0rY6%2FEFooBnPGjCmQpEy%2BKz%2FqNA6k%2Fvkjv0kB%2B3C4fRCRjQ%2BqfD%2BBC5KDD2aBYhmCXRY6Jhp2o%2F5mhawiAFxIUqRO3yk%2Bzs0s1G%2FR1V8yWj%2F6LYR5%2Fmc8JPuCrUMmVJR%2BuPFdF%2BszQRwRn%2BlsDPo67y6ZD7mwqLXHFrlpNuZOMWBWAMKs8ghhtOkSPeBJ%2Fj01TT2BkrEuQ2hZVbBIyUlbIgQtGYf37GtlDL0LuDDS%2BPsZmhmdAPddTVhUtjIUiKzJ%2Flnuflh4twLviuTxWunbF%2FFs5QdXOIAyz9sg3FCEis1k%2BMFaYu52VTWS7kyK1J%2B3Rx8p9ajg9405WeXTWJ7Hh%2FmyzUDbIx4RVAwp3Olx%2F2vnNGWTTp09zEBY1HiLeoNapw%2BXJ%2BBnGzEgQrDtqjjF20eNmLXpp%2BahDDPvoa9BjqkATUpn1JpIdR9Gx5HBKQqDbSJez4pazam%2BEVbIc05gYqzSHjRoCCgviYYhpk9T8ycTnuJJtkNyrZSK0%2FG3Z1QsFbyA2%2F1xfa80z7P0HGbCpDEN9KoFkRmKYGr1m3imGZLCIaQ8q4KV5YorT7Q7Jqp8wUOaUqOtH5TUloWgyNQA83OXxqab1%2BtIoRDPxWKUS85kfAsRiaiFDmPCLOWZMscGuxeJKjQ&X-Amz-Signature=6b16af0ac42629380e68bd9a7c504fa2d8037dbc97c6535bd3ae97e1f7d911b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRLULTXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDq5yEf%2ByT2IlgfVvXtm%2BlGU7AKzUQOO6%2Bj7cYj1Rx7WQIhAP%2BloKTjzb3XX5DKEFgWlQCk7h4vnY1HWPJUPv7SsHSQKv8DCCYQABoMNjM3NDIzMTgzODA1IgxvZKffQejrKsZh1w4q3ANiQOguiaKau1MxzNAeR96ZFLTZNqI8nGL4ZrlDKXqeTB82cpen8a6PRnCfKZQbhM%2Ba2pFtKYL1FzJy2%2BPg8AwepCjSkXlqBZLxZKMjkAB4zYSB5S9QGUtX3uQl88ICRJKOgLccYvMYT46CwZzh1ciKPz%2B4%2BzgJMRn6v8yN%2F27TaG5gnEEu91CRbt3mteHzgbAtaJP5mhavd48EMUOk9gokElOaNZeQYfCLhxjV93tb4fKpsdslEzH1JV4zLxH3uJ9nXucyCNjw6Ik0yk9M2DlfeiWakLPByTxsaZPHZg2e9AeA302r5yjwHSxtH5nKvVrW16Q5%2BwCzTnJINYIUTgDoF8HpmHnd%2BK7vJYg5gLNFuU%2FGaXC77W58sdOHIQY2w%2F5clWKG1kzj5NO5aAUj%2Bdl8XPe%2F9aGrNhHpf5uyIsoMz1B7D0LGxYXWdoCteC9Ek57cxIWhG61W68028i6XaVvJUkHsdSHOMy3nAEZmLbYt0IVHcBHu2gOtJVmsYVaESRxdqy1BTtPRGVshmRXyA5o5cAdOtEBhyotv8YxNmQu6O3%2FkaR%2F2v783%2BSWpCkEUqb9yn%2FauehYrod%2FMJiG7HPh9LVGKXdvMvzRa5KkH6DiIOTDf8Ay9f%2BeGtwq7EDCUv4a9BjqkASYUuhgEPF0SFlazAaondS3S1i%2BAbsquFS65DWP0ISyszSZIKLX9G63PAXDP%2BhRGXR%2FxPSwTKVn7cyH8Yr4b1UO243SUYwR5khUvMPPzvRy9HDisnyj1AFbPi0mR3Y2D%2Bl4kP%2BQ9S3lclYIGWGC%2FlDXToz0Ditjo08vIPO3JEEpaImiwkZ4rWzV%2FB1pKcL7%2B1Tjpu6V%2BIpZvBctATCeIOYsKWgVX&X-Amz-Signature=61df9960b8835868f4de75a353bdbe4f34e44bc62783a0372e90c7222851ca61&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRLULTXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDq5yEf%2ByT2IlgfVvXtm%2BlGU7AKzUQOO6%2Bj7cYj1Rx7WQIhAP%2BloKTjzb3XX5DKEFgWlQCk7h4vnY1HWPJUPv7SsHSQKv8DCCYQABoMNjM3NDIzMTgzODA1IgxvZKffQejrKsZh1w4q3ANiQOguiaKau1MxzNAeR96ZFLTZNqI8nGL4ZrlDKXqeTB82cpen8a6PRnCfKZQbhM%2Ba2pFtKYL1FzJy2%2BPg8AwepCjSkXlqBZLxZKMjkAB4zYSB5S9QGUtX3uQl88ICRJKOgLccYvMYT46CwZzh1ciKPz%2B4%2BzgJMRn6v8yN%2F27TaG5gnEEu91CRbt3mteHzgbAtaJP5mhavd48EMUOk9gokElOaNZeQYfCLhxjV93tb4fKpsdslEzH1JV4zLxH3uJ9nXucyCNjw6Ik0yk9M2DlfeiWakLPByTxsaZPHZg2e9AeA302r5yjwHSxtH5nKvVrW16Q5%2BwCzTnJINYIUTgDoF8HpmHnd%2BK7vJYg5gLNFuU%2FGaXC77W58sdOHIQY2w%2F5clWKG1kzj5NO5aAUj%2Bdl8XPe%2F9aGrNhHpf5uyIsoMz1B7D0LGxYXWdoCteC9Ek57cxIWhG61W68028i6XaVvJUkHsdSHOMy3nAEZmLbYt0IVHcBHu2gOtJVmsYVaESRxdqy1BTtPRGVshmRXyA5o5cAdOtEBhyotv8YxNmQu6O3%2FkaR%2F2v783%2BSWpCkEUqb9yn%2FauehYrod%2FMJiG7HPh9LVGKXdvMvzRa5KkH6DiIOTDf8Ay9f%2BeGtwq7EDCUv4a9BjqkASYUuhgEPF0SFlazAaondS3S1i%2BAbsquFS65DWP0ISyszSZIKLX9G63PAXDP%2BhRGXR%2FxPSwTKVn7cyH8Yr4b1UO243SUYwR5khUvMPPzvRy9HDisnyj1AFbPi0mR3Y2D%2Bl4kP%2BQ9S3lclYIGWGC%2FlDXToz0Ditjo08vIPO3JEEpaImiwkZ4rWzV%2FB1pKcL7%2B1Tjpu6V%2BIpZvBctATCeIOYsKWgVX&X-Amz-Signature=8a7f7372d26a6209b195d73915654869697ffa2162acbfb2c66bc01f93be01ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRLULTXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDq5yEf%2ByT2IlgfVvXtm%2BlGU7AKzUQOO6%2Bj7cYj1Rx7WQIhAP%2BloKTjzb3XX5DKEFgWlQCk7h4vnY1HWPJUPv7SsHSQKv8DCCYQABoMNjM3NDIzMTgzODA1IgxvZKffQejrKsZh1w4q3ANiQOguiaKau1MxzNAeR96ZFLTZNqI8nGL4ZrlDKXqeTB82cpen8a6PRnCfKZQbhM%2Ba2pFtKYL1FzJy2%2BPg8AwepCjSkXlqBZLxZKMjkAB4zYSB5S9QGUtX3uQl88ICRJKOgLccYvMYT46CwZzh1ciKPz%2B4%2BzgJMRn6v8yN%2F27TaG5gnEEu91CRbt3mteHzgbAtaJP5mhavd48EMUOk9gokElOaNZeQYfCLhxjV93tb4fKpsdslEzH1JV4zLxH3uJ9nXucyCNjw6Ik0yk9M2DlfeiWakLPByTxsaZPHZg2e9AeA302r5yjwHSxtH5nKvVrW16Q5%2BwCzTnJINYIUTgDoF8HpmHnd%2BK7vJYg5gLNFuU%2FGaXC77W58sdOHIQY2w%2F5clWKG1kzj5NO5aAUj%2Bdl8XPe%2F9aGrNhHpf5uyIsoMz1B7D0LGxYXWdoCteC9Ek57cxIWhG61W68028i6XaVvJUkHsdSHOMy3nAEZmLbYt0IVHcBHu2gOtJVmsYVaESRxdqy1BTtPRGVshmRXyA5o5cAdOtEBhyotv8YxNmQu6O3%2FkaR%2F2v783%2BSWpCkEUqb9yn%2FauehYrod%2FMJiG7HPh9LVGKXdvMvzRa5KkH6DiIOTDf8Ay9f%2BeGtwq7EDCUv4a9BjqkASYUuhgEPF0SFlazAaondS3S1i%2BAbsquFS65DWP0ISyszSZIKLX9G63PAXDP%2BhRGXR%2FxPSwTKVn7cyH8Yr4b1UO243SUYwR5khUvMPPzvRy9HDisnyj1AFbPi0mR3Y2D%2Bl4kP%2BQ9S3lclYIGWGC%2FlDXToz0Ditjo08vIPO3JEEpaImiwkZ4rWzV%2FB1pKcL7%2B1Tjpu6V%2BIpZvBctATCeIOYsKWgVX&X-Amz-Signature=c20fb3d806ca0839a4087c4807bfc82414e6143259706ee23e0688db1dae4e2f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUKXYO3I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIFlItDt6JK03Oz3ipYCLzmb9KsxyLNbUIGqGsJ2%2FCUCAAiBa6Hg77GwcSvYIhVJn29vGYdh6Ra8FGFs1PYtxeC%2BY%2BSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMr0vvLj9HHl6QPHD9KtwDj8ukx0DgsQ2TPkVh8pQesRMhNJLI0CtgTKbdt%2BkrbUXheopTWuWDyI2MgIJedYQN%2BWkY6b38IGqtNx1ZaYYMKEJMOunO1yPjNqBzojFwRGRvGbwGoT3ocmvfCG3fadJf6G9HP2XK66F%2FryyZJvGYGKmg7n%2BBxfnxxfcDO2%2BilOvwzT4cfCeTuF0WlnLC6eKoHCJ2lb79cyVnb9kqAvUU0%2B907LWqbyBBrkBKaQVvD%2BHmvpnpohygOlKbwcZoPU%2BUhJ8LZ2e5tHMvb%2BL0DUY45wLUn5rOYyhzwRCxImkEvjNgaNYcIbV577N6vj3kT3TSuQgOf3pQcelbyiWJ%2BRp6kmj%2BaJirxUHdV3j9nFxbrdyRBLXWgzaPsPuoALGw1dIWri9XpAiIp4QCbxsSS%2Bctq%2FiJ3LORD8bHfyKPSk1RN%2F2Ccm9s1W2XeKvTy6zyN93vC13RIRBbdLPr%2BebizL8ATSLl9vW70YULSChfgOdBNXuM9PMd8w32t2W3bs1j58L4b%2F3Jj%2FQatEEkU3Ew8n5M6uNFaJGJQ7xplVglCZDqe1ATUlLaMMZTDsF4ypYRI8zSWPN0Cgx%2FlzMz%2BIiIPDM4f5JduvM3PqNvbk4HujHxET738HWxPrVSq2eyhiYw276GvQY6pgHSVHbYsRgyqzmmpXwm1QjFtuFtpQbj838%2BEgzYiXy9w5URp1%2BlJJDX2gQpybfmD1r7E%2Bt71YOWalajSca0Bki7zzhXPSiPGmWE3Xd%2FHtaGKakgN49skrVx8LHmlB3%2BcFc%2BawI9AoFFcDsqpI9VWvLtHghKB017Kt5h1YFHEgSAtjpnqOBdCNSaUvlwx2rKxaZ2Qha9VioVfBLInbr6aqhVmztt7uc3&X-Amz-Signature=3df387da200d23500eb06b1340f263d86113c557191546dd4f4e9f8adf9d088a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6GBFDU5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIDWeinCvfXpL4hM9xe19DgFRCho5unzUWLHVoBMhjLBCAiBa2zNtQ9RkHlrYrvoDHxj8scp3uGH9T6pPFwfBaDZAICr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIM1N9zknDlpP1zkMTpKtwDUIfrWLd7PyehWHVf9qMaH9azA6xDu%2FHD7X8qZLqKXOe9WlEL0JoHmHXwCZ2bGz4B0qoBM1fWENvcOeDoPiOHYu4aljzKlk4kt09XdLUcYOF%2BAWKKu%2BOjq2jMpMdaLMqiTmqgXItSVi%2Fhi7fWY7e4gNrj2D7zQVhHQVmQ323AOf1oxXxzvDeYt4u%2BWnlbmuFNhub78RKFiXiDSJm%2FMCOzSDLnXV3MR5EVkhyjP%2FfCgvX5i6TZCZc5gzf%2FHgKIbxY3e4qy0F5sq1Wr1YQO8RViNabziGnTjAunvaN5cTjYq0dnSELF9Umq6oHqV9LTwv3zPEnzdqGaSFmUvumAXbuMEImAbhmpYXodBB9RuDW97%2Bnz4HqXnvYY%2Fj4G4ZJ7bsrbZ7EZAt1tokzkhYi6iyO1SQ0pKyEdHyqjpBmO5gqKYSadNAzeV3MzTP13e0uGmCzat%2BZqRoTlKPcE7Q81Hmsy1C13iZM7cWCII3QdcxXgRB3pXU5W0eGPooH6%2FuDLalflfi4KOatMWDODb70u77QsHVia%2BheqVpTvS%2BRCLX4S9W59HkWtx89gfO1Zi3MV5d2vBV3xM1VQK1PDlaZkCh8jFRuuqjmbQCsTnjN2t9%2FcFcC%2FMy2ugObI9jLIWCEw076GvQY6pgGm6svlCfbEzZ8gjKToYzm3T%2FwRU4udhU2Q%2F6P4u2hXkB5vIMLg7lIYB5B7Dw4NgCdRTVOHEB8H9BECY5GL3Rmao2motcBkW%2BflVr6pRlXBGMwQbpUJQhjaTMaE4zLByTwi5lAthSGQtk9t87arviuTFgSwR05hHJzkyp5LFhNqLoiyY7MWtDGmU3MrCZE5iGY9EURXUfiBL1ykiZq%2F9nWrnksXBN8o&X-Amz-Signature=eec3cfcb452e677f2852aa4de0ccc38e2978930a0e7b93a922c6c31c3e9ad616&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2CRFOR5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIGyLDGT9NqtPrAqq72AXasFFo%2B3cqIM4yu1YoseKf6MDAiA%2FrOS0HJAJOAd0NyI2lJtDrBqLPsPnYlgtSPz53TxEYSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMp%2F9p8HfuGTQSOk%2BwKtwDuL49i9WV9fbCrxdKd5MaFQKKWl1eDbpAna%2BfUXV50y2BafFeyreFcNpXeokNCFWE2b7mwEScw8XcHoRvDur0fFfOPdEAZz5D5hvXAxH3Vq6xOvk%2BJpivLwMtq4EfYI5JPvBYm0%2BvFa%2FS6NVLHM9xQdIwG9PTZM%2BdDckF%2FvqUyj4dnHjLKEK%2BrdDCa1Knv%2FSt86gKXVbE%2BUP%2FRLsn5%2BIgZhNbPx4WPW3hLjsERaMdpfHhU1C0c5QoF2ST71cTKcJbWGFriV%2FJBHHU5CB8qTLnqCSJTK6tTrc8YlR0it%2BbS6LJkD77gRw821y9MlhpeQ6OpZKChN4CCt2iY5dty1QOWDh0flbVOvmLhDSSrc2R8tnZHoVfYtCaqddmVTIuPB5lyGbiopJ8MZXvfdXGkf%2B%2Bthu9q7UP9azivEGZcRCidqWHnqDJZuvDKxvSeMQC0bju%2BpRd4v6UK6I9lbcoCsTygqNsAcAGx%2BcEG3JuUavKIWshvZ1Y19FKQpsRJZaBlPJ2bzXVZk%2FtDp3h7fjPc8JzXw21RvROEkONkjjDabSnzq14sq6kr3yHJ8EUp5uaV3%2FwWOfVEfu1pHmBelzEscHEgQ41CQIXgpFiidgLYZZv6PX9f%2FzWqrTVGf9sy%2Fcww7%2BGvQY6pgFWH1DtvACIsE%2BlgETNJWfcFwF4XRjf4Niig91xEX%2BEKPxIck8vxrKl7%2FoPy0wPMFT6%2BYq4XZv64s%2BU1sdxXfRHCTnnKzB4Qk6euSSSZ0wKwUH5Luz485siBXux0h3OAI5Mz73q%2BLjLtCKDjKyK5vD83wfPstZct7lQWGp9RE6%2B5cSxJQ1CnYTf8f7kOSwJFG2wL842J1AAg1xOCQj7nMkGAzkCPoWt&X-Amz-Signature=6904d6f31decb63797cfaf6ecd7f5efc3226bc3f4e9775f1ccbdeb6424871179&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXBSWU5W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQC0zNsNq%2Fp6CZoAnJMFlCPst0F%2FdBKsfhmntXX3775h8gIhAMOexRMcEmbEXTi%2FU116m0M%2BOANtepnXD2oiqPIlpw7CKv8DCCYQABoMNjM3NDIzMTgzODA1IgyuXlV%2BgG1%2BNQGJSCYq3AOU73Km%2FJAZ4dsrN83uZRwVjVxnge6Nhsyajp6UwJXuIvi%2Bxr8gzB3x%2FG33KThOfMriyhkpXpwrX0y9E2GvNZ06tCyiQev1EHPH%2FjssNUJYjDcu1TqhtKq3cs%2B0hUqHJv6opuxcXBfQBDQyhl98qOu2skPXz7Pnt4xBUnEO2A5KwqhCSGNMpIK%2BwLu2GtEukbKlhQJDtviVdADm8Wwpdg3dcLC0MK2x2tJ3W1akMjAovdcQESPtvJb5qZFHFSJy1Dutm7EcYhcvTiPAGhFUzZUXcKYwpWvnSPSkKGL2rx9HGUeWttr%2F0%2FxTi0qYAuJVolZm9VbkQmu73CjB5qUjd5X7zfsxM%2B5wHga96V2DgmLjVFHNbQwW9DuEw5rtZhvX86Jv4mrBrPY30OiCDhWiwyF%2FACJBILTm1t6LZ48%2FW3FokEaUC2zGK6j79Ua%2Bxbv8ZkfijEp6K36lDjVieSj%2Fp0pINNVwHTqxjTGJV%2BkvaN3K%2FzVPVT%2BQ9aq3f5YuoQcPhz%2Bw5PoZjM69Knt23HbAExMuxd5t8pWS%2BgNS9pdmBDB%2Bx%2BLSOe8nbUJtAFfrtu6rQ9xdkYDiViRHVGqig5Yg7qdeNiWodDD2MOILhsqpZ%2BHJ61Ho4Zoo2nkUIK9%2BIDDWvoa9BjqkAawZsZr6lIyf8weybIU9StLGlBjirKqNJdkrCEIEqTLtWD08VtFlQwUDu4Qosm4%2FPL%2BRObyAnmLLXa3KFcovptKUgy1lFniAl14Fa%2FblR5yXvvCVd%2F6yBidz60flkPSrRjTkegnNDGzxR1AvivYflirzK60ky%2B5e9CmSRAf9Pj5hgV6F2UYXwa9gXpM710f12q6vCQDGwKfYrcnDgyfGY8QG5xkH&X-Amz-Signature=4a896435ee8e4412e4983f6582b36f5b1f01e25596da5dc7b4a711167d82b08f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXBSWU5W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQC0zNsNq%2Fp6CZoAnJMFlCPst0F%2FdBKsfhmntXX3775h8gIhAMOexRMcEmbEXTi%2FU116m0M%2BOANtepnXD2oiqPIlpw7CKv8DCCYQABoMNjM3NDIzMTgzODA1IgyuXlV%2BgG1%2BNQGJSCYq3AOU73Km%2FJAZ4dsrN83uZRwVjVxnge6Nhsyajp6UwJXuIvi%2Bxr8gzB3x%2FG33KThOfMriyhkpXpwrX0y9E2GvNZ06tCyiQev1EHPH%2FjssNUJYjDcu1TqhtKq3cs%2B0hUqHJv6opuxcXBfQBDQyhl98qOu2skPXz7Pnt4xBUnEO2A5KwqhCSGNMpIK%2BwLu2GtEukbKlhQJDtviVdADm8Wwpdg3dcLC0MK2x2tJ3W1akMjAovdcQESPtvJb5qZFHFSJy1Dutm7EcYhcvTiPAGhFUzZUXcKYwpWvnSPSkKGL2rx9HGUeWttr%2F0%2FxTi0qYAuJVolZm9VbkQmu73CjB5qUjd5X7zfsxM%2B5wHga96V2DgmLjVFHNbQwW9DuEw5rtZhvX86Jv4mrBrPY30OiCDhWiwyF%2FACJBILTm1t6LZ48%2FW3FokEaUC2zGK6j79Ua%2Bxbv8ZkfijEp6K36lDjVieSj%2Fp0pINNVwHTqxjTGJV%2BkvaN3K%2FzVPVT%2BQ9aq3f5YuoQcPhz%2Bw5PoZjM69Knt23HbAExMuxd5t8pWS%2BgNS9pdmBDB%2Bx%2BLSOe8nbUJtAFfrtu6rQ9xdkYDiViRHVGqig5Yg7qdeNiWodDD2MOILhsqpZ%2BHJ61Ho4Zoo2nkUIK9%2BIDDWvoa9BjqkAawZsZr6lIyf8weybIU9StLGlBjirKqNJdkrCEIEqTLtWD08VtFlQwUDu4Qosm4%2FPL%2BRObyAnmLLXa3KFcovptKUgy1lFniAl14Fa%2FblR5yXvvCVd%2F6yBidz60flkPSrRjTkegnNDGzxR1AvivYflirzK60ky%2B5e9CmSRAf9Pj5hgV6F2UYXwa9gXpM710f12q6vCQDGwKfYrcnDgyfGY8QG5xkH&X-Amz-Signature=f3669c97f42fb7574567a61df6a32431db6832760e743b47a4de669341631e18&X-Amz-SignedHeaders=host&x-id=GetObject)

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
