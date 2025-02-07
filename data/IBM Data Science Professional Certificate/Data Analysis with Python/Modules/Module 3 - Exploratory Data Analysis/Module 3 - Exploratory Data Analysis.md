

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7DWRRDM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIH74Re%2BAZ%2BFmcxVNb%2Fa5disyJ7FrtJ5bnlBOV7zvZsoZAiEAlqxIt5pHLQ7bET6yoJKbgjDbapV5hnHNorcGcgScPUkq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDOD0np8chZnuS6Ze5yrcA2dcV3Jmye6GFaNj%2FeCC4b87sd2cjaJbtfjeiJYkkxlgxa6qdohgCJgkhA6vFxGiQcUjcsbWGQfUZpVQ8pabsBzMkDkZDpFiH%2Beop4DkQoJ6u6C%2FNBvV44gn2nJZIJTgmG7qyT7ABnIbEJVYQptgMl5fPMqenNjhn2sppp6ffCFXyR%2FVjmQcgSgQSinvm1x3rhcQi2gI6naXntnhJ4q8xcrqUjcPBsDCgMuIbAFFC94hyPVnX2g2MB%2FRwjjGDc1EobOwMyO4K%2FUy9GDEGm2%2FfvchVJY6DubIQviqTiHYh9ZLzpC4UrzcitA%2Ba%2Fji42qJeja21jyhhrLs%2BMMI2uLQrcF%2BxAqfTT31Z64cAqX7eMFcgymJX9hJAhG8qgAqkopxYLiougCO5PH8gr3tKxuXGYpr8CAG23ttpGihJ0QqUIsir1Alo1wxHu2RoRg4GBi2gx%2FV14jJp1%2B1wPvSh16XqD31nGz8K%2FQDDSm1YSj%2BbYGB00Zyg8qKAP1fAjbdSZLxNLGRw2ZTd%2BauemDWWgO75%2BEIu%2FPH1PV7EMXOi82105OrrpJ9GOrLvY22S2%2FUwQsSoCYuObuf4fzV4jt3BvjKHl8X%2B%2B446LLqfA6KqJFsqviId%2F4%2BqljdCyr9EBkmMPn5lr0GOqUBYUWOnZTRYH7akne9iuCc4sBGOGciigXCUluQ0URSz0N%2BGzaVwpozkpjA%2Bjznzamb4JSsWSBRRbUd4ewTiIU7JSroyRSJNP2TfKwlkynayH7V%2B0srUC%2Fqi1H8CeL%2BE4akdBW28%2Fff4VfPpO9c%2FndLO%2FUhvj9k24sLPHaUfKL9NCNWtXGEX08bsUIzLgyoHZlMw1sMFuobGiLqvwpr1jxv1HrchVmb&X-Amz-Signature=d04ff5eabf51d3588b450e688c76c6302bf03a4c6642c8439ad3d3768036056a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7DWRRDM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIH74Re%2BAZ%2BFmcxVNb%2Fa5disyJ7FrtJ5bnlBOV7zvZsoZAiEAlqxIt5pHLQ7bET6yoJKbgjDbapV5hnHNorcGcgScPUkq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDOD0np8chZnuS6Ze5yrcA2dcV3Jmye6GFaNj%2FeCC4b87sd2cjaJbtfjeiJYkkxlgxa6qdohgCJgkhA6vFxGiQcUjcsbWGQfUZpVQ8pabsBzMkDkZDpFiH%2Beop4DkQoJ6u6C%2FNBvV44gn2nJZIJTgmG7qyT7ABnIbEJVYQptgMl5fPMqenNjhn2sppp6ffCFXyR%2FVjmQcgSgQSinvm1x3rhcQi2gI6naXntnhJ4q8xcrqUjcPBsDCgMuIbAFFC94hyPVnX2g2MB%2FRwjjGDc1EobOwMyO4K%2FUy9GDEGm2%2FfvchVJY6DubIQviqTiHYh9ZLzpC4UrzcitA%2Ba%2Fji42qJeja21jyhhrLs%2BMMI2uLQrcF%2BxAqfTT31Z64cAqX7eMFcgymJX9hJAhG8qgAqkopxYLiougCO5PH8gr3tKxuXGYpr8CAG23ttpGihJ0QqUIsir1Alo1wxHu2RoRg4GBi2gx%2FV14jJp1%2B1wPvSh16XqD31nGz8K%2FQDDSm1YSj%2BbYGB00Zyg8qKAP1fAjbdSZLxNLGRw2ZTd%2BauemDWWgO75%2BEIu%2FPH1PV7EMXOi82105OrrpJ9GOrLvY22S2%2FUwQsSoCYuObuf4fzV4jt3BvjKHl8X%2B%2B446LLqfA6KqJFsqviId%2F4%2BqljdCyr9EBkmMPn5lr0GOqUBYUWOnZTRYH7akne9iuCc4sBGOGciigXCUluQ0URSz0N%2BGzaVwpozkpjA%2Bjznzamb4JSsWSBRRbUd4ewTiIU7JSroyRSJNP2TfKwlkynayH7V%2B0srUC%2Fqi1H8CeL%2BE4akdBW28%2Fff4VfPpO9c%2FndLO%2FUhvj9k24sLPHaUfKL9NCNWtXGEX08bsUIzLgyoHZlMw1sMFuobGiLqvwpr1jxv1HrchVmb&X-Amz-Signature=a28f0999e567f8179b28cdcc7237a5d5740dc7c05a282536153fdc18f06d188b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7DWRRDM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIH74Re%2BAZ%2BFmcxVNb%2Fa5disyJ7FrtJ5bnlBOV7zvZsoZAiEAlqxIt5pHLQ7bET6yoJKbgjDbapV5hnHNorcGcgScPUkq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDOD0np8chZnuS6Ze5yrcA2dcV3Jmye6GFaNj%2FeCC4b87sd2cjaJbtfjeiJYkkxlgxa6qdohgCJgkhA6vFxGiQcUjcsbWGQfUZpVQ8pabsBzMkDkZDpFiH%2Beop4DkQoJ6u6C%2FNBvV44gn2nJZIJTgmG7qyT7ABnIbEJVYQptgMl5fPMqenNjhn2sppp6ffCFXyR%2FVjmQcgSgQSinvm1x3rhcQi2gI6naXntnhJ4q8xcrqUjcPBsDCgMuIbAFFC94hyPVnX2g2MB%2FRwjjGDc1EobOwMyO4K%2FUy9GDEGm2%2FfvchVJY6DubIQviqTiHYh9ZLzpC4UrzcitA%2Ba%2Fji42qJeja21jyhhrLs%2BMMI2uLQrcF%2BxAqfTT31Z64cAqX7eMFcgymJX9hJAhG8qgAqkopxYLiougCO5PH8gr3tKxuXGYpr8CAG23ttpGihJ0QqUIsir1Alo1wxHu2RoRg4GBi2gx%2FV14jJp1%2B1wPvSh16XqD31nGz8K%2FQDDSm1YSj%2BbYGB00Zyg8qKAP1fAjbdSZLxNLGRw2ZTd%2BauemDWWgO75%2BEIu%2FPH1PV7EMXOi82105OrrpJ9GOrLvY22S2%2FUwQsSoCYuObuf4fzV4jt3BvjKHl8X%2B%2B446LLqfA6KqJFsqviId%2F4%2BqljdCyr9EBkmMPn5lr0GOqUBYUWOnZTRYH7akne9iuCc4sBGOGciigXCUluQ0URSz0N%2BGzaVwpozkpjA%2Bjznzamb4JSsWSBRRbUd4ewTiIU7JSroyRSJNP2TfKwlkynayH7V%2B0srUC%2Fqi1H8CeL%2BE4akdBW28%2Fff4VfPpO9c%2FndLO%2FUhvj9k24sLPHaUfKL9NCNWtXGEX08bsUIzLgyoHZlMw1sMFuobGiLqvwpr1jxv1HrchVmb&X-Amz-Signature=18509d336643eb493713839b40793b6c080888755fb08d179aaa56d1be92a6ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPFDAFVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICMQwq0iqFu8GxkdVRCIzKi4ZZdNxt7kmPDhk9SkCZ4mAiEAx3MZeSWcs7oaqyOi0v3y1r1A%2Bo5v9AiIjQmV6ufeEK0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDI%2FwdcLOeuPu5NJqxCrcA6dvms%2BwITm29ZY7VdvoiWl44LPDB7ntXmu%2BbZjic9rntwg19hzQmMbhKD6y0Bmxv7qcm0vATZKyxiEtr2dtTZopBAyDUhPcOLI%2F4j5jYIIr%2Bek32ZY9wU9QdX10iH%2Fpc2IzM5An3zOFiRnnNYa%2Fpt6KP68Nsdzpguq1vGpxGNLyY8DpU585bqFE80iT4QzPy8oyHv%2BuQoGNmqSHZCPbeoaEa3sirFucSXISvKv6rvy5KcnwYT6MfBJV6Y4VMoiy2xO0LAtxNSIDw3S1Dglphlw%2FNtXwhCX6EDhJPYE3BVB%2B%2FGomtg7%2FKA9AKrCz7PhWRtg9llvQGrkYaTHcJ8ao8xsG2mUHQjvwp6i8vxmQdFSF830Gg1hygLRmFQKIkhyGVxReF24qqYcrpD1BGzz0pI3oVQGyaAnS5p2MznrQxe9ThrK%2BPpt7ksa1%2BpmzKgQK1fA08jgJKPkAGCFIu8BnWzQmlD2CDcF1meTjO6mo27RVt91ja7ERSPunv359sCQh9V6hIbjlWBkkwh8jOI15Nf2BaEiDLhFMWu9rTZyxum3Fr1BMx3xa3PnOHd%2FCys6ur3mZtEI34aIngMi6opKlNRom77z95Cgpya4L%2Fq4t%2BbSZujfZbhNtVkDLMpytMPP5lr0GOqUBQyyU63Dow0VyLaThJlJ8X3EwFNydfgk2YKwQs%2F3cPVlOZ5%2BgXxnw91cs7vQ4eWkn%2FaDbYYo3F0z3tI%2F0MSKQXUrbULNwtfJyPaWdAPExqLSfHnCYMTj1H5M8jJh38sC5tmzu%2BTtbuOhV1%2Bj9nB%2BlNhHDEbWYyhWQ9aYPB6Z%2BCVLhZKBqe%2F%2FHyMhfBvvrRrAL3RZa%2Fk915gE8p35AaaWA38QoYPkS&X-Amz-Signature=086b5dd70ae23a43e45b1f7634132b500fc1e1a888ab1b3e85c178347470668e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPFDAFVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICMQwq0iqFu8GxkdVRCIzKi4ZZdNxt7kmPDhk9SkCZ4mAiEAx3MZeSWcs7oaqyOi0v3y1r1A%2Bo5v9AiIjQmV6ufeEK0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDI%2FwdcLOeuPu5NJqxCrcA6dvms%2BwITm29ZY7VdvoiWl44LPDB7ntXmu%2BbZjic9rntwg19hzQmMbhKD6y0Bmxv7qcm0vATZKyxiEtr2dtTZopBAyDUhPcOLI%2F4j5jYIIr%2Bek32ZY9wU9QdX10iH%2Fpc2IzM5An3zOFiRnnNYa%2Fpt6KP68Nsdzpguq1vGpxGNLyY8DpU585bqFE80iT4QzPy8oyHv%2BuQoGNmqSHZCPbeoaEa3sirFucSXISvKv6rvy5KcnwYT6MfBJV6Y4VMoiy2xO0LAtxNSIDw3S1Dglphlw%2FNtXwhCX6EDhJPYE3BVB%2B%2FGomtg7%2FKA9AKrCz7PhWRtg9llvQGrkYaTHcJ8ao8xsG2mUHQjvwp6i8vxmQdFSF830Gg1hygLRmFQKIkhyGVxReF24qqYcrpD1BGzz0pI3oVQGyaAnS5p2MznrQxe9ThrK%2BPpt7ksa1%2BpmzKgQK1fA08jgJKPkAGCFIu8BnWzQmlD2CDcF1meTjO6mo27RVt91ja7ERSPunv359sCQh9V6hIbjlWBkkwh8jOI15Nf2BaEiDLhFMWu9rTZyxum3Fr1BMx3xa3PnOHd%2FCys6ur3mZtEI34aIngMi6opKlNRom77z95Cgpya4L%2Fq4t%2BbSZujfZbhNtVkDLMpytMPP5lr0GOqUBQyyU63Dow0VyLaThJlJ8X3EwFNydfgk2YKwQs%2F3cPVlOZ5%2BgXxnw91cs7vQ4eWkn%2FaDbYYo3F0z3tI%2F0MSKQXUrbULNwtfJyPaWdAPExqLSfHnCYMTj1H5M8jJh38sC5tmzu%2BTtbuOhV1%2Bj9nB%2BlNhHDEbWYyhWQ9aYPB6Z%2BCVLhZKBqe%2F%2FHyMhfBvvrRrAL3RZa%2Fk915gE8p35AaaWA38QoYPkS&X-Amz-Signature=ff1a0f8c7a3952269ed3c1f7ad29bc5cafbf9e347ae4cdd945df469b9c6e2d3d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPFDAFVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICMQwq0iqFu8GxkdVRCIzKi4ZZdNxt7kmPDhk9SkCZ4mAiEAx3MZeSWcs7oaqyOi0v3y1r1A%2Bo5v9AiIjQmV6ufeEK0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDI%2FwdcLOeuPu5NJqxCrcA6dvms%2BwITm29ZY7VdvoiWl44LPDB7ntXmu%2BbZjic9rntwg19hzQmMbhKD6y0Bmxv7qcm0vATZKyxiEtr2dtTZopBAyDUhPcOLI%2F4j5jYIIr%2Bek32ZY9wU9QdX10iH%2Fpc2IzM5An3zOFiRnnNYa%2Fpt6KP68Nsdzpguq1vGpxGNLyY8DpU585bqFE80iT4QzPy8oyHv%2BuQoGNmqSHZCPbeoaEa3sirFucSXISvKv6rvy5KcnwYT6MfBJV6Y4VMoiy2xO0LAtxNSIDw3S1Dglphlw%2FNtXwhCX6EDhJPYE3BVB%2B%2FGomtg7%2FKA9AKrCz7PhWRtg9llvQGrkYaTHcJ8ao8xsG2mUHQjvwp6i8vxmQdFSF830Gg1hygLRmFQKIkhyGVxReF24qqYcrpD1BGzz0pI3oVQGyaAnS5p2MznrQxe9ThrK%2BPpt7ksa1%2BpmzKgQK1fA08jgJKPkAGCFIu8BnWzQmlD2CDcF1meTjO6mo27RVt91ja7ERSPunv359sCQh9V6hIbjlWBkkwh8jOI15Nf2BaEiDLhFMWu9rTZyxum3Fr1BMx3xa3PnOHd%2FCys6ur3mZtEI34aIngMi6opKlNRom77z95Cgpya4L%2Fq4t%2BbSZujfZbhNtVkDLMpytMPP5lr0GOqUBQyyU63Dow0VyLaThJlJ8X3EwFNydfgk2YKwQs%2F3cPVlOZ5%2BgXxnw91cs7vQ4eWkn%2FaDbYYo3F0z3tI%2F0MSKQXUrbULNwtfJyPaWdAPExqLSfHnCYMTj1H5M8jJh38sC5tmzu%2BTtbuOhV1%2Bj9nB%2BlNhHDEbWYyhWQ9aYPB6Z%2BCVLhZKBqe%2F%2FHyMhfBvvrRrAL3RZa%2Fk915gE8p35AaaWA38QoYPkS&X-Amz-Signature=735c4e4489c2b41544fd48d4769e46022c24e4855b4d24710a1eff2f0e3e132f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPFDAFVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICMQwq0iqFu8GxkdVRCIzKi4ZZdNxt7kmPDhk9SkCZ4mAiEAx3MZeSWcs7oaqyOi0v3y1r1A%2Bo5v9AiIjQmV6ufeEK0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDI%2FwdcLOeuPu5NJqxCrcA6dvms%2BwITm29ZY7VdvoiWl44LPDB7ntXmu%2BbZjic9rntwg19hzQmMbhKD6y0Bmxv7qcm0vATZKyxiEtr2dtTZopBAyDUhPcOLI%2F4j5jYIIr%2Bek32ZY9wU9QdX10iH%2Fpc2IzM5An3zOFiRnnNYa%2Fpt6KP68Nsdzpguq1vGpxGNLyY8DpU585bqFE80iT4QzPy8oyHv%2BuQoGNmqSHZCPbeoaEa3sirFucSXISvKv6rvy5KcnwYT6MfBJV6Y4VMoiy2xO0LAtxNSIDw3S1Dglphlw%2FNtXwhCX6EDhJPYE3BVB%2B%2FGomtg7%2FKA9AKrCz7PhWRtg9llvQGrkYaTHcJ8ao8xsG2mUHQjvwp6i8vxmQdFSF830Gg1hygLRmFQKIkhyGVxReF24qqYcrpD1BGzz0pI3oVQGyaAnS5p2MznrQxe9ThrK%2BPpt7ksa1%2BpmzKgQK1fA08jgJKPkAGCFIu8BnWzQmlD2CDcF1meTjO6mo27RVt91ja7ERSPunv359sCQh9V6hIbjlWBkkwh8jOI15Nf2BaEiDLhFMWu9rTZyxum3Fr1BMx3xa3PnOHd%2FCys6ur3mZtEI34aIngMi6opKlNRom77z95Cgpya4L%2Fq4t%2BbSZujfZbhNtVkDLMpytMPP5lr0GOqUBQyyU63Dow0VyLaThJlJ8X3EwFNydfgk2YKwQs%2F3cPVlOZ5%2BgXxnw91cs7vQ4eWkn%2FaDbYYo3F0z3tI%2F0MSKQXUrbULNwtfJyPaWdAPExqLSfHnCYMTj1H5M8jJh38sC5tmzu%2BTtbuOhV1%2Bj9nB%2BlNhHDEbWYyhWQ9aYPB6Z%2BCVLhZKBqe%2F%2FHyMhfBvvrRrAL3RZa%2Fk915gE8p35AaaWA38QoYPkS&X-Amz-Signature=73c4fba03f6765b0918830abb4a3edd7a3cf366f188508db4022baeb8fbc6750&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPFDAFVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICMQwq0iqFu8GxkdVRCIzKi4ZZdNxt7kmPDhk9SkCZ4mAiEAx3MZeSWcs7oaqyOi0v3y1r1A%2Bo5v9AiIjQmV6ufeEK0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDI%2FwdcLOeuPu5NJqxCrcA6dvms%2BwITm29ZY7VdvoiWl44LPDB7ntXmu%2BbZjic9rntwg19hzQmMbhKD6y0Bmxv7qcm0vATZKyxiEtr2dtTZopBAyDUhPcOLI%2F4j5jYIIr%2Bek32ZY9wU9QdX10iH%2Fpc2IzM5An3zOFiRnnNYa%2Fpt6KP68Nsdzpguq1vGpxGNLyY8DpU585bqFE80iT4QzPy8oyHv%2BuQoGNmqSHZCPbeoaEa3sirFucSXISvKv6rvy5KcnwYT6MfBJV6Y4VMoiy2xO0LAtxNSIDw3S1Dglphlw%2FNtXwhCX6EDhJPYE3BVB%2B%2FGomtg7%2FKA9AKrCz7PhWRtg9llvQGrkYaTHcJ8ao8xsG2mUHQjvwp6i8vxmQdFSF830Gg1hygLRmFQKIkhyGVxReF24qqYcrpD1BGzz0pI3oVQGyaAnS5p2MznrQxe9ThrK%2BPpt7ksa1%2BpmzKgQK1fA08jgJKPkAGCFIu8BnWzQmlD2CDcF1meTjO6mo27RVt91ja7ERSPunv359sCQh9V6hIbjlWBkkwh8jOI15Nf2BaEiDLhFMWu9rTZyxum3Fr1BMx3xa3PnOHd%2FCys6ur3mZtEI34aIngMi6opKlNRom77z95Cgpya4L%2Fq4t%2BbSZujfZbhNtVkDLMpytMPP5lr0GOqUBQyyU63Dow0VyLaThJlJ8X3EwFNydfgk2YKwQs%2F3cPVlOZ5%2BgXxnw91cs7vQ4eWkn%2FaDbYYo3F0z3tI%2F0MSKQXUrbULNwtfJyPaWdAPExqLSfHnCYMTj1H5M8jJh38sC5tmzu%2BTtbuOhV1%2Bj9nB%2BlNhHDEbWYyhWQ9aYPB6Z%2BCVLhZKBqe%2F%2FHyMhfBvvrRrAL3RZa%2Fk915gE8p35AaaWA38QoYPkS&X-Amz-Signature=3dbb5f28a59d32c0b85a199feba6df1b3b769ecb7b17d1a1ab4cb6878f325419&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPFDAFVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICMQwq0iqFu8GxkdVRCIzKi4ZZdNxt7kmPDhk9SkCZ4mAiEAx3MZeSWcs7oaqyOi0v3y1r1A%2Bo5v9AiIjQmV6ufeEK0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDI%2FwdcLOeuPu5NJqxCrcA6dvms%2BwITm29ZY7VdvoiWl44LPDB7ntXmu%2BbZjic9rntwg19hzQmMbhKD6y0Bmxv7qcm0vATZKyxiEtr2dtTZopBAyDUhPcOLI%2F4j5jYIIr%2Bek32ZY9wU9QdX10iH%2Fpc2IzM5An3zOFiRnnNYa%2Fpt6KP68Nsdzpguq1vGpxGNLyY8DpU585bqFE80iT4QzPy8oyHv%2BuQoGNmqSHZCPbeoaEa3sirFucSXISvKv6rvy5KcnwYT6MfBJV6Y4VMoiy2xO0LAtxNSIDw3S1Dglphlw%2FNtXwhCX6EDhJPYE3BVB%2B%2FGomtg7%2FKA9AKrCz7PhWRtg9llvQGrkYaTHcJ8ao8xsG2mUHQjvwp6i8vxmQdFSF830Gg1hygLRmFQKIkhyGVxReF24qqYcrpD1BGzz0pI3oVQGyaAnS5p2MznrQxe9ThrK%2BPpt7ksa1%2BpmzKgQK1fA08jgJKPkAGCFIu8BnWzQmlD2CDcF1meTjO6mo27RVt91ja7ERSPunv359sCQh9V6hIbjlWBkkwh8jOI15Nf2BaEiDLhFMWu9rTZyxum3Fr1BMx3xa3PnOHd%2FCys6ur3mZtEI34aIngMi6opKlNRom77z95Cgpya4L%2Fq4t%2BbSZujfZbhNtVkDLMpytMPP5lr0GOqUBQyyU63Dow0VyLaThJlJ8X3EwFNydfgk2YKwQs%2F3cPVlOZ5%2BgXxnw91cs7vQ4eWkn%2FaDbYYo3F0z3tI%2F0MSKQXUrbULNwtfJyPaWdAPExqLSfHnCYMTj1H5M8jJh38sC5tmzu%2BTtbuOhV1%2Bj9nB%2BlNhHDEbWYyhWQ9aYPB6Z%2BCVLhZKBqe%2F%2FHyMhfBvvrRrAL3RZa%2Fk915gE8p35AaaWA38QoYPkS&X-Amz-Signature=e6d55c1a3999dc6ee9bdee707ede9999265c8169b2792cb47e72589c95dd4dbe&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URTEHSJ2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDL%2FjIM5xhp0zm%2FammAm0qeGc6hPAAILXk1xpmKulrg%2BAiA8kQQ%2BYTcKTLBdi1XTg2j3IoVQPGjZyDXMpENMuuAg3Sr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMK5W9z5%2Fc8qACoyB6KtwD4cnpIxr%2FdTgfeDJ1XqDPmUbloXlnd7H8MIh%2Fy6ljC5f58PgZ42qxZSYIEm7OVje5uDGNCKNrlBit%2BpZdKhOEfeYel5O275trtBkJZyRnv8Ql4f%2FQlJcjl6LaiHgDSbw8yfKGd6EzM3bUgvJwX1xSbO3cF%2BRP4pfVi1zlaC8KkVyYd78VMgHsqEuDSwPZpEU1RyTizjrA5QDO%2B8ZvKEpS6nfUQJRiRMaKnEiPzHxl3%2B99JES35a8y8Bj7IPF6JC0RBkNSO10VrBxMmc1DaQ%2BssaL2qOd69yfLLWm3pmxw%2BCiL9v%2F9PZ6Q%2BYFF6DsDNJIexpYdvvpy42gEF%2FemE3cbi6NVwSl7nRylYqA%2BnTjCAM5LbgCje0SEQOxGDnvCmmPfwdU6QnqsMCVKvaQdWxmb4JQFY51iASa2f2w2AiebGeJgaxBKIADuS94vQhNPeHNWV%2BjSEqdmRHMqQlY3RqZR9XRgY5F46iDFx%2FYh1EHNydDL3Bxc1H%2Bck8xTrNBA0554uZU3fVRWpFnNXXIsGYbFOE7CkBktEvfa2tiUIQx0fW3PQJuJk6iQhudQH15S%2BZwRFvBNyZk%2BCd4IaehkZ1RgaDm1s53h2zkxIFB5iVUrRBjEUB%2FGG0Mi4mGVrsMww%2FmWvQY6pgGELiBzUWsfNqrEEiDurzy5uuEbxe7jS55%2BQyl0zi0JkUw22uKyAKCp7EDjDY7NAxMkAFM2f11GleoGA%2Fn6V34EcKeKgBA%2FbL%2Fjarvq7RP84zDbrfIvtuAKoJp7a%2BEN58EjXyReFgCu47iuK0Z56z8n66WDPlGvAv%2FmKgXr1wuPMJ%2F9wZdamS6%2By6dK9SZjIF6sKG9vSRuB5NzjhQZGbM5WKwORphKa&X-Amz-Signature=784b5e7834b96dbd4cc4c8a886eb537ef1f3d7ed99e2b57486da638dcdc8b0b2&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z7G3BNE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIBp0TLXLPnd2JGHoHV7zRXw%2Fjg6e20unfyC9d32kMebVAiA7R1quO85%2Fxa5Pv9zbVdNr%2FoDrAHcBv7Lv3IKoRf8EMyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMG75We6C5Xq8GFSGAKtwD2nT8JaPmt3g7tU04QipgB5YoIL3h4WELZwDXHVcB8r36yxdgVGwlM9qBr5l0NYca4eq6mwfoQ8XsweU%2BZeRQTchVAI4zuHdSfY5a9oJw%2BcWNs4dJAdAJ%2BVqjbYd%2FV2jttIDCi2oAPIqpyP725TQAmuS4nLDav00IYBo5bii0LaReklI1S%2BKzR1NUjWKIuPHTM%2Fd%2BXm1NXo2TtLZO%2BdobVj5J6DvS3quTrXkdbQORh%2FH%2FD7b01SzdiQhdZbOaDDBESnjMnknsugOlKxCQ4sKdItIPaI8vIlcstADIh7NO87Jd%2F%2Fn9DuTejkOHHxndBDHZ2Jx90HHUUZccSNIxXvhZW3eqjUiIder%2BJKM3F4eSPscdgR8e1Ng6bVkNLE7GEtTFuHNUYPvKY7ne1j3BYon7EjGmJLe37yKq8egkQn35HQkHeEgOh%2BZEYgKmlBS%2B6jJgBHmbgt7EGZ6qRgAyUPt6u%2BNyYQmmkp7cXlAr6eW0dTSOK%2FLgQTCn55IdgexB%2F9q2VR58bNX3NyHzUvyJOAe%2FyLta1K78e1M1CWc6MPNkxX7oziq4vee7%2BONduO5TmNB3MhGi5QEjvArzqakvu85O%2FmfwpBGekX5%2FoQscUerj5yRL7mfU9wtVQmL1CCMwk%2FqWvQY6pgHNDfci7UwmSgW2NzSY%2FLaof9Fu5%2F6SmnfEviCmw4tA%2Bmg4QSL1L3lvJHyddIjJU52sNFeHV1hvL8gtiy8QVw3XmWGgZID5A4te12tyNk14dQfB7c6Q%2B8ftYdMMUDVdj7diTrgw3ps1H2LhF7FhJqwZTSy95sxCC9HN3LKBXjBgVI%2FSjziyYhazMTRrPcGY1klxnqpwJrDcUNcqbuKKCsRqA%2BO6m9rp&X-Amz-Signature=e726e2c1c68182d6eaa8cc99242b43235aa8a5711dd6fec578b0e028386f4d14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPFDAFVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICMQwq0iqFu8GxkdVRCIzKi4ZZdNxt7kmPDhk9SkCZ4mAiEAx3MZeSWcs7oaqyOi0v3y1r1A%2Bo5v9AiIjQmV6ufeEK0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDI%2FwdcLOeuPu5NJqxCrcA6dvms%2BwITm29ZY7VdvoiWl44LPDB7ntXmu%2BbZjic9rntwg19hzQmMbhKD6y0Bmxv7qcm0vATZKyxiEtr2dtTZopBAyDUhPcOLI%2F4j5jYIIr%2Bek32ZY9wU9QdX10iH%2Fpc2IzM5An3zOFiRnnNYa%2Fpt6KP68Nsdzpguq1vGpxGNLyY8DpU585bqFE80iT4QzPy8oyHv%2BuQoGNmqSHZCPbeoaEa3sirFucSXISvKv6rvy5KcnwYT6MfBJV6Y4VMoiy2xO0LAtxNSIDw3S1Dglphlw%2FNtXwhCX6EDhJPYE3BVB%2B%2FGomtg7%2FKA9AKrCz7PhWRtg9llvQGrkYaTHcJ8ao8xsG2mUHQjvwp6i8vxmQdFSF830Gg1hygLRmFQKIkhyGVxReF24qqYcrpD1BGzz0pI3oVQGyaAnS5p2MznrQxe9ThrK%2BPpt7ksa1%2BpmzKgQK1fA08jgJKPkAGCFIu8BnWzQmlD2CDcF1meTjO6mo27RVt91ja7ERSPunv359sCQh9V6hIbjlWBkkwh8jOI15Nf2BaEiDLhFMWu9rTZyxum3Fr1BMx3xa3PnOHd%2FCys6ur3mZtEI34aIngMi6opKlNRom77z95Cgpya4L%2Fq4t%2BbSZujfZbhNtVkDLMpytMPP5lr0GOqUBQyyU63Dow0VyLaThJlJ8X3EwFNydfgk2YKwQs%2F3cPVlOZ5%2BgXxnw91cs7vQ4eWkn%2FaDbYYo3F0z3tI%2F0MSKQXUrbULNwtfJyPaWdAPExqLSfHnCYMTj1H5M8jJh38sC5tmzu%2BTtbuOhV1%2Bj9nB%2BlNhHDEbWYyhWQ9aYPB6Z%2BCVLhZKBqe%2F%2FHyMhfBvvrRrAL3RZa%2Fk915gE8p35AaaWA38QoYPkS&X-Amz-Signature=5f7db5d8e1e5c71629cfcbe547cbff7777bcb373beed2d97dad48d1a151857be&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPFDAFVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICMQwq0iqFu8GxkdVRCIzKi4ZZdNxt7kmPDhk9SkCZ4mAiEAx3MZeSWcs7oaqyOi0v3y1r1A%2Bo5v9AiIjQmV6ufeEK0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDI%2FwdcLOeuPu5NJqxCrcA6dvms%2BwITm29ZY7VdvoiWl44LPDB7ntXmu%2BbZjic9rntwg19hzQmMbhKD6y0Bmxv7qcm0vATZKyxiEtr2dtTZopBAyDUhPcOLI%2F4j5jYIIr%2Bek32ZY9wU9QdX10iH%2Fpc2IzM5An3zOFiRnnNYa%2Fpt6KP68Nsdzpguq1vGpxGNLyY8DpU585bqFE80iT4QzPy8oyHv%2BuQoGNmqSHZCPbeoaEa3sirFucSXISvKv6rvy5KcnwYT6MfBJV6Y4VMoiy2xO0LAtxNSIDw3S1Dglphlw%2FNtXwhCX6EDhJPYE3BVB%2B%2FGomtg7%2FKA9AKrCz7PhWRtg9llvQGrkYaTHcJ8ao8xsG2mUHQjvwp6i8vxmQdFSF830Gg1hygLRmFQKIkhyGVxReF24qqYcrpD1BGzz0pI3oVQGyaAnS5p2MznrQxe9ThrK%2BPpt7ksa1%2BpmzKgQK1fA08jgJKPkAGCFIu8BnWzQmlD2CDcF1meTjO6mo27RVt91ja7ERSPunv359sCQh9V6hIbjlWBkkwh8jOI15Nf2BaEiDLhFMWu9rTZyxum3Fr1BMx3xa3PnOHd%2FCys6ur3mZtEI34aIngMi6opKlNRom77z95Cgpya4L%2Fq4t%2BbSZujfZbhNtVkDLMpytMPP5lr0GOqUBQyyU63Dow0VyLaThJlJ8X3EwFNydfgk2YKwQs%2F3cPVlOZ5%2BgXxnw91cs7vQ4eWkn%2FaDbYYo3F0z3tI%2F0MSKQXUrbULNwtfJyPaWdAPExqLSfHnCYMTj1H5M8jJh38sC5tmzu%2BTtbuOhV1%2Bj9nB%2BlNhHDEbWYyhWQ9aYPB6Z%2BCVLhZKBqe%2F%2FHyMhfBvvrRrAL3RZa%2Fk915gE8p35AaaWA38QoYPkS&X-Amz-Signature=4c2c43c7d5b8934b052ca975f3332117142a38a06f8d11d59a3fe32f24a693d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPFDAFVY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCICMQwq0iqFu8GxkdVRCIzKi4ZZdNxt7kmPDhk9SkCZ4mAiEAx3MZeSWcs7oaqyOi0v3y1r1A%2Bo5v9AiIjQmV6ufeEK0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDI%2FwdcLOeuPu5NJqxCrcA6dvms%2BwITm29ZY7VdvoiWl44LPDB7ntXmu%2BbZjic9rntwg19hzQmMbhKD6y0Bmxv7qcm0vATZKyxiEtr2dtTZopBAyDUhPcOLI%2F4j5jYIIr%2Bek32ZY9wU9QdX10iH%2Fpc2IzM5An3zOFiRnnNYa%2Fpt6KP68Nsdzpguq1vGpxGNLyY8DpU585bqFE80iT4QzPy8oyHv%2BuQoGNmqSHZCPbeoaEa3sirFucSXISvKv6rvy5KcnwYT6MfBJV6Y4VMoiy2xO0LAtxNSIDw3S1Dglphlw%2FNtXwhCX6EDhJPYE3BVB%2B%2FGomtg7%2FKA9AKrCz7PhWRtg9llvQGrkYaTHcJ8ao8xsG2mUHQjvwp6i8vxmQdFSF830Gg1hygLRmFQKIkhyGVxReF24qqYcrpD1BGzz0pI3oVQGyaAnS5p2MznrQxe9ThrK%2BPpt7ksa1%2BpmzKgQK1fA08jgJKPkAGCFIu8BnWzQmlD2CDcF1meTjO6mo27RVt91ja7ERSPunv359sCQh9V6hIbjlWBkkwh8jOI15Nf2BaEiDLhFMWu9rTZyxum3Fr1BMx3xa3PnOHd%2FCys6ur3mZtEI34aIngMi6opKlNRom77z95Cgpya4L%2Fq4t%2BbSZujfZbhNtVkDLMpytMPP5lr0GOqUBQyyU63Dow0VyLaThJlJ8X3EwFNydfgk2YKwQs%2F3cPVlOZ5%2BgXxnw91cs7vQ4eWkn%2FaDbYYo3F0z3tI%2F0MSKQXUrbULNwtfJyPaWdAPExqLSfHnCYMTj1H5M8jJh38sC5tmzu%2BTtbuOhV1%2Bj9nB%2BlNhHDEbWYyhWQ9aYPB6Z%2BCVLhZKBqe%2F%2FHyMhfBvvrRrAL3RZa%2Fk915gE8p35AaaWA38QoYPkS&X-Amz-Signature=bbf7ced3eafbd3d5de54e8e0651941bc1d2451abc8ad630599c1d76e22997aaf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665O52CDL4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCYsnm7q4V7G3Mk8Jlcr%2FmuAxkhZMiV80ZQqDv3QiqL4QIhALKTNKQP2x0YSfaYJVxDDtyqq7OQ7vsJhJGu4sm4uJW5Kv8DCHEQABoMNjM3NDIzMTgzODA1IgxjR8q3KYkEItgUgzoq3AMVNYdP50dbbcMKIfptCXfTNfnRltMwhR1X%2B5cELsj957o30PPJK9mYiDfwskjs6LCCYkY4q97DZzGxgZxnt7s73MtNBEwkjCre%2BLXlYWPEqOnPz94tL2Vkm%2FS94559KNn3qWuJ73VBZIrGDBrYSu%2FmF%2B5nhBtn2fwNsBBfDkbVobEcsU9MkPQCwwXHzypYrCL0Sz21NeZWke8XwnIaYMrJCE95W6OmPkeONFTXN3bNNKocKFzODJj%2FNuavZH%2FDgUOWdkajRMiI8cZFJo4qXiXIbJQFp7hCUKMsP6JT6ngsvr4bqHXrfiBkdqfDKrX60w9uTdZUym0HBNzRXz20nJ1XtPfSwB%2B8OltgQ5HbyCUrImZcL9xfKs4R2%2BmvEAUM4OKrjbusvEK4lNFCFnCucr5f0Xg%2Fi478RW7OYdN22UN8C2acs8xFv1bbf0cocmHs6IswgfpkeantueXCPmDlxdW36GxX4aI6hpVjqMi9KbvIbLNKyotpfJ3R1rD6UbJjHbXyR%2FPNYVnb%2FPcHiCD1hUwCW2YJJbeywDef6iurF%2BfxOJJI%2Bp3qixvzq9fvhNV1RLYz6KTNK64wflHsVd9SjdFS5pu938XqSH3Hl7KcaZlsl6i2I9jlNopqttjkrDDL%2BZa9BjqkASDIdhHMC%2BG1YkLYv6EQKwbr9jFGLYZyQVF1u7QHsM%2FGMlz0YH65wOp1cPDgOJoqre6o2vZkEyyu6PWU8yHeFZajXzCCm4a7jZXNUEoS%2BuKpGIlePxXQSMHHe1%2Fz0FsFpKw22pVeeL%2FnACSLnzGWlCKMM3sz3aZxq3wPkhYn%2Bw%2B0KPyoVsAKF1zJRAEjNxPOcKG4awwhBnAWu3G%2FWJLMlzjKtEiW&X-Amz-Signature=6e4a810ce54abcb02cc2487e16e4d0efd6471db5d2c39e950986071119df1823&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RURZZHNZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIBf7ERmt%2F0NvS%2F%2FLoVRkjTJ1bDRq5myt6rA4qmVUVEimAiAanVmoYReBDJYtgb0DxdJDqdg15FxlAVYzC4XCUvlwfyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMw00E5ConZNK30RzdKtwDIH%2FD4UoXLoAsWm7F1mD5MO9wmhZwBLSysx76tww3O%2FkhlrvXz%2B4YWkDbabFPgTTeHCasw1s8gV%2FU50tQR1SfcKmrmU9tDoBrX0N7hgUQVZOtYKFU1AYNXq1IerQDXIFJQ9pc2qtX5eCQZ2TFd5kMlAbUcd0BbpxLjycBYj4tN4z%2B6g642ukASFsb9I%2FN9eCT78SB2bLTKB8jx%2BqEt%2FaB0kTWD%2F%2BHW11BatA4HoETgvbvCBYZxP11An7WOayjQsC62dC980niD2mjLet6S1UsywvwKNRAMZ7kDEzYQbyvUG7KKWuDpN9cAl9BbJNurNhecFSVWdOSB1o81%2F750j6Mi%2B9fLYy3MQLLANsBpUIb5EA9ewisiRYcnBGE5MWLaigZHBFiSOM3uhsqOuHb%2FkTme2Y%2BoNPVCcCXxx55SpCKR70KO6cUMn48TZiTyWG1uHT3jXOQXTipaMfK2aoDGOQJDVC9efFCe6Z0roKcYV82saiZShCQY9DR%2FXw3UHM6qc9OlLzC%2BRzZTGiF%2BvZMBzkio61p1wLnAkrradRT6one2h2OkvnpcS%2F6taViHs0i80VaOinZZZdTXlgBptbrRS%2BOBaAyJFgTy0mkDEoHJOO1BYflskbfoEBG0h1AUuMwwPmWvQY6pgF6vMlrF0ypS5R9R8FSnIjqFhHA%2FDsv%2FzWUGf%2FPuJ03iDFjRQWlA4BbRhG42qGadXhIBL5yeZzhySVG3V4AFZW1jPZr8ISg7pioHkO2RAKflKFOYVB0iYXIBPHWMw%2BQ6f7KWeVPTEgWEtyjgaAsKqEJmkpFvYYv2OSmohN7BPAbLGkWrPxnP9X%2Bn4VKxJq8h7aW9483LIXk%2Fba4pRgZfQAwyab4VpWK&X-Amz-Signature=5642a1a73cb9feb156c8ffd43743853b008729bc5ea0fc4955c60ef6b2cee5c4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CESMG6Z%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCID4hCAzppcKqcYpW2RD13mmYy764Lkn%2FyknsV86UtZoEAiEA7HlGVCCQpD41VhxPqfQgZHpUTxWxeiQf9YcfeRtpVu8q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDKULFqVG%2FYgko8o1YyrcA0FxBovv8nDVxj5uNroDRsaVln2%2BftEPhKRlrzsr0halUY%2BdFJ8hF1P11F3l7mFaFgFjSLwMqcAtZ9dcNA9Pd2gWlOkvwYYsjBEESWWTyeQwNqFUId3eck954fssfXKyNL5DZtxIz5dH0st00m2sTovYR7vjWUnUm%2B6sFHY5NNk27gjWbmuf9NSUdHQwqgaFxyQMI%2Bg4uqfDJocfbjkv5Exk8%2BuXweMiJMXhY52kdQPsleD6dt6ORXE5MTu8M%2FTDo1bt3%2F6f%2FsTUwVWHQhYs8nF2MJVk2Q21TwkG6PhhCnoRR%2Bpz11B0hebhPv3loZkVX9jc04GGHiFnT3rU3vuZBHS2bBo0%2F%2FvRnDoNW1bqKCv1chZV1weNK7Rd5%2B5GRF0ASaif%2FxdXdd%2Fq9GkfcjKvA7B%2FmPYCiyvFBNKTQahuikBEK36EjY%2BDf1lIdE1GOb82vrRGkIjOm4oempwAExjTpJf3mVYA7rpJRVECQyeYxoO1MFZhxZuIez9AS8hprWHp7WhTspyylbB%2B5DQd0OgqWAdhBmk4uCmpzyIWhcvz6uRynGMaknJfW%2FAnMz6TCIcEoSPCMAQX5PYmZBQg5yRiE3IaQo2xde3gxIPp6xDpzYwVlS7B7Qyc6bdhYMeiMP%2F5lr0GOqUBtJsXjkqqEyUNptAwshsEHmMmHdkalxjnxRk9iGV%2FH0AyjGepovBR36VAN1p1SD75nMyU%2BEZPswvyD%2BLXQtNNo%2BO5RRb7L6ncCLdXjOEayszIMKbsNy07vEds3HV7SvQmzr1JM8EfobPQ%2Fwdk5176mSKDYkBXPf8KGnhzgix180gCaLGXJXAJYw7ThCifzYzJV8gbGLO4%2B2yQYfDjJDnSVdVuYAA2&X-Amz-Signature=8f922d4ce088d43a52e529fff675815411036367e5653679cfc508c5791113ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EKHA5H7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQD%2F52pP5UYzrjCU6uERt2%2FeVb8xs9oePbxQwAFaM7MwWQIgbk4EJSp95QwozPzoH7FUTjVsH4d7cLsKlUScqmW4szEq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFKLXYDyL4V6B8zKQircA5e8TJiWaC6kWKqwCfJ8xxbmJ9cT0ZP%2BZpIjDMRz0uVPe4ZbmV2Svo2OlcTuqUPcw2ZkEAx8GR7hoaam1zcE4iCay9tHNKkG6Sa4qVCHOsRIj5Yvt%2FwJYka2G7p%2FrPZbqYCSvwWhYzAE4PnPy%2FgSa0meWdfNw6hu3Wqj3de2LPNG6onWfMYZNe7eWOe2N25hqD%2BQ9ao%2Fy1429iPnyESzGOyzr9IprOIkkBoWzyptgRhjLd2Ptz0Yu1%2B5NdB4ULVsZCu6LVWOAx9p4vMFXs%2BW8zHiLOI%2BPih1uExoSZEtNEZKu%2BZvsQpQlRc7ppcwPQ75MfStGdnV9Waw2%2FxW9Szr73XN%2FeCIlfzk%2Fld0n0vgRKXtejf31QE0IpQcx5TsE5wdV2IuzspK4IRWUWmsP%2FnUeaiPFxECvsON7vXlJLx%2FPsu9KK35SULWu1AOnxjxovPrNJj4lD8IhRD9EXoQNIIyXN0pq9i3Lo00FUVMJfCuiQU9c4cdyAEivr5n%2BXX9mCHk9g3OYX3Tq7epZV0axyte0BlnnrDx4nkuj5a26IlR%2BQBHtCOcO2NeRf%2FcoVsIWYW%2BGFRv8KRTJDUw3vXdeF1eZyZFYdvIxu4jWAvPBQ%2FIAAAF8PR0W4sRVwwJS%2FyDMIX6lr0GOqUBj%2Fa0NlmAtHC%2FY0v%2FumHb7aPEvJlLvmtSXUNzi%2F1qvIsMiQKGRfig7FnSwGb7XSnd%2BsDgCxjyneY87FQN6ktbt7%2FgIl9Kj1asX7Jg6H5Xz%2Fo6nJgghDmCG0RmlUKrV9OSautsbBLNzTHkMVeBVh2s6gUqzskUApROVPTYKufNWmIoofW%2FQpz6SWl74pT4SVXINzYEEYdvgkJR1x9COCaMgdeWYaEo&X-Amz-Signature=6c0f2f3ccc334f684e82d4bf8a50f6a5aab5c144b47c0e12b82f961ca8439ca1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EKHA5H7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQD%2F52pP5UYzrjCU6uERt2%2FeVb8xs9oePbxQwAFaM7MwWQIgbk4EJSp95QwozPzoH7FUTjVsH4d7cLsKlUScqmW4szEq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFKLXYDyL4V6B8zKQircA5e8TJiWaC6kWKqwCfJ8xxbmJ9cT0ZP%2BZpIjDMRz0uVPe4ZbmV2Svo2OlcTuqUPcw2ZkEAx8GR7hoaam1zcE4iCay9tHNKkG6Sa4qVCHOsRIj5Yvt%2FwJYka2G7p%2FrPZbqYCSvwWhYzAE4PnPy%2FgSa0meWdfNw6hu3Wqj3de2LPNG6onWfMYZNe7eWOe2N25hqD%2BQ9ao%2Fy1429iPnyESzGOyzr9IprOIkkBoWzyptgRhjLd2Ptz0Yu1%2B5NdB4ULVsZCu6LVWOAx9p4vMFXs%2BW8zHiLOI%2BPih1uExoSZEtNEZKu%2BZvsQpQlRc7ppcwPQ75MfStGdnV9Waw2%2FxW9Szr73XN%2FeCIlfzk%2Fld0n0vgRKXtejf31QE0IpQcx5TsE5wdV2IuzspK4IRWUWmsP%2FnUeaiPFxECvsON7vXlJLx%2FPsu9KK35SULWu1AOnxjxovPrNJj4lD8IhRD9EXoQNIIyXN0pq9i3Lo00FUVMJfCuiQU9c4cdyAEivr5n%2BXX9mCHk9g3OYX3Tq7epZV0axyte0BlnnrDx4nkuj5a26IlR%2BQBHtCOcO2NeRf%2FcoVsIWYW%2BGFRv8KRTJDUw3vXdeF1eZyZFYdvIxu4jWAvPBQ%2FIAAAF8PR0W4sRVwwJS%2FyDMIX6lr0GOqUBj%2Fa0NlmAtHC%2FY0v%2FumHb7aPEvJlLvmtSXUNzi%2F1qvIsMiQKGRfig7FnSwGb7XSnd%2BsDgCxjyneY87FQN6ktbt7%2FgIl9Kj1asX7Jg6H5Xz%2Fo6nJgghDmCG0RmlUKrV9OSautsbBLNzTHkMVeBVh2s6gUqzskUApROVPTYKufNWmIoofW%2FQpz6SWl74pT4SVXINzYEEYdvgkJR1x9COCaMgdeWYaEo&X-Amz-Signature=81f3ff262778b31b705c157cab5f90c029d9ce001d08ed002d45dfaca6332962&X-Amz-SignedHeaders=host&x-id=GetObject)

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
