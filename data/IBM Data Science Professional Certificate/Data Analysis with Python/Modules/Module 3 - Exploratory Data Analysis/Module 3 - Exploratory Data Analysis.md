

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEBME7JE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEr1jY0MVsFKNyDYCRTj7F4A2Winvh925n2isWkN6ZKkAiARUM5XT0ow3pj0LZ4KWWlNpcNcW7OzaGNUp%2BXARH0p1Sr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMrymtuY3frVFvteGcKtwDhIE%2FCNh%2BKDaKniAJMWtLR4sjslijEjwRepuGGsph4YJy1hGqRyHhwAOePxH162hiZfY0%2F5xob%2BWeHrojVrfUZLx4RiJWM8Vp5md05FHn5SHNvhGHNguFVtLy0lGleJSjHf5hQDU5Pftejq%2Fv78NAXZ8iXIv3YP2toDjlbZPLiKIm45P%2B4X0H%2B4cLQofmvTILRyQe20zdJ%2BcHjXFm6XNKuouXVJ4LtAPmAmiVhGzicvzBbvqWugA1ea0R4aIRpKF5OyES%2F5xYuPl1Vsb%2BS5j2h841iWBnkILj5u5oxevgAq5O1rlfd6NDlS0JylOjhT1QEXK6HUWs2EFVR01hkFoS41f8uqxpm8bXmbFDso2P9GjlrpWf9whbUk91Pme215Ge0KClE2A9nkwjHY6MECnIQ94yhEx5jke9PfWDXaBK3NPHkhC93Jgw8cPByHScazPTm4nc8MRUTzzWjbWCtvxqh5BhiKDXS8m7udCzZkq%2BCMhGUmU3hzLtGcTgXLTJ%2B2SBA%2BRc81VhaT7bMfvfJRexQE773vkjs1xYzFjVlwZZzXpWlgvpnGkZqNQRT7g0GW2098LOEWNShe58Egq%2FE%2B6h8%2FE1AD3IPm2sHUR1PMduua082sjxrMW%2BEsAB6xswzIuYvQY6pgELI7qCUHgDTvDgx397BsSkp11G8HzRKRVwWfaIczXnuJc32Qlk2Ehofy%2FQNQPbBEGVx4xEfxolnIURKSWVsezzqWMku2BubTJj2xa7Z%2BBL%2B3pgNzxfMdrO3LRdM4mp6%2FIk2WaTLkN3eUhgvpghaRxfgq6K%2BvcJxDUYTcYX8KHLJ6VFK%2B%2BVc9j%2F75BnsuaRcsm7e1OpwVW3AUlrl6VtjIvXp8L1c8gO&X-Amz-Signature=c61d1ca7ba32577b19160e725b6fa5acb8d12b7ccc842e36937721e52ebf954d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEBME7JE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEr1jY0MVsFKNyDYCRTj7F4A2Winvh925n2isWkN6ZKkAiARUM5XT0ow3pj0LZ4KWWlNpcNcW7OzaGNUp%2BXARH0p1Sr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMrymtuY3frVFvteGcKtwDhIE%2FCNh%2BKDaKniAJMWtLR4sjslijEjwRepuGGsph4YJy1hGqRyHhwAOePxH162hiZfY0%2F5xob%2BWeHrojVrfUZLx4RiJWM8Vp5md05FHn5SHNvhGHNguFVtLy0lGleJSjHf5hQDU5Pftejq%2Fv78NAXZ8iXIv3YP2toDjlbZPLiKIm45P%2B4X0H%2B4cLQofmvTILRyQe20zdJ%2BcHjXFm6XNKuouXVJ4LtAPmAmiVhGzicvzBbvqWugA1ea0R4aIRpKF5OyES%2F5xYuPl1Vsb%2BS5j2h841iWBnkILj5u5oxevgAq5O1rlfd6NDlS0JylOjhT1QEXK6HUWs2EFVR01hkFoS41f8uqxpm8bXmbFDso2P9GjlrpWf9whbUk91Pme215Ge0KClE2A9nkwjHY6MECnIQ94yhEx5jke9PfWDXaBK3NPHkhC93Jgw8cPByHScazPTm4nc8MRUTzzWjbWCtvxqh5BhiKDXS8m7udCzZkq%2BCMhGUmU3hzLtGcTgXLTJ%2B2SBA%2BRc81VhaT7bMfvfJRexQE773vkjs1xYzFjVlwZZzXpWlgvpnGkZqNQRT7g0GW2098LOEWNShe58Egq%2FE%2B6h8%2FE1AD3IPm2sHUR1PMduua082sjxrMW%2BEsAB6xswzIuYvQY6pgELI7qCUHgDTvDgx397BsSkp11G8HzRKRVwWfaIczXnuJc32Qlk2Ehofy%2FQNQPbBEGVx4xEfxolnIURKSWVsezzqWMku2BubTJj2xa7Z%2BBL%2B3pgNzxfMdrO3LRdM4mp6%2FIk2WaTLkN3eUhgvpghaRxfgq6K%2BvcJxDUYTcYX8KHLJ6VFK%2B%2BVc9j%2F75BnsuaRcsm7e1OpwVW3AUlrl6VtjIvXp8L1c8gO&X-Amz-Signature=a03ae68f99a84eed65162af14aa273aa35d988b9926e6ef48105e0f11f8f2728&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEBME7JE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEr1jY0MVsFKNyDYCRTj7F4A2Winvh925n2isWkN6ZKkAiARUM5XT0ow3pj0LZ4KWWlNpcNcW7OzaGNUp%2BXARH0p1Sr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMrymtuY3frVFvteGcKtwDhIE%2FCNh%2BKDaKniAJMWtLR4sjslijEjwRepuGGsph4YJy1hGqRyHhwAOePxH162hiZfY0%2F5xob%2BWeHrojVrfUZLx4RiJWM8Vp5md05FHn5SHNvhGHNguFVtLy0lGleJSjHf5hQDU5Pftejq%2Fv78NAXZ8iXIv3YP2toDjlbZPLiKIm45P%2B4X0H%2B4cLQofmvTILRyQe20zdJ%2BcHjXFm6XNKuouXVJ4LtAPmAmiVhGzicvzBbvqWugA1ea0R4aIRpKF5OyES%2F5xYuPl1Vsb%2BS5j2h841iWBnkILj5u5oxevgAq5O1rlfd6NDlS0JylOjhT1QEXK6HUWs2EFVR01hkFoS41f8uqxpm8bXmbFDso2P9GjlrpWf9whbUk91Pme215Ge0KClE2A9nkwjHY6MECnIQ94yhEx5jke9PfWDXaBK3NPHkhC93Jgw8cPByHScazPTm4nc8MRUTzzWjbWCtvxqh5BhiKDXS8m7udCzZkq%2BCMhGUmU3hzLtGcTgXLTJ%2B2SBA%2BRc81VhaT7bMfvfJRexQE773vkjs1xYzFjVlwZZzXpWlgvpnGkZqNQRT7g0GW2098LOEWNShe58Egq%2FE%2B6h8%2FE1AD3IPm2sHUR1PMduua082sjxrMW%2BEsAB6xswzIuYvQY6pgELI7qCUHgDTvDgx397BsSkp11G8HzRKRVwWfaIczXnuJc32Qlk2Ehofy%2FQNQPbBEGVx4xEfxolnIURKSWVsezzqWMku2BubTJj2xa7Z%2BBL%2B3pgNzxfMdrO3LRdM4mp6%2FIk2WaTLkN3eUhgvpghaRxfgq6K%2BvcJxDUYTcYX8KHLJ6VFK%2B%2BVc9j%2F75BnsuaRcsm7e1OpwVW3AUlrl6VtjIvXp8L1c8gO&X-Amz-Signature=32458ae05fb44deac86e1c614d99fed23406fded997cd5f18ad7ea44559d964f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCIJATQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmfpCn%2FokL8FmiN03tc%2F56zyepIlGdVQzDb%2BNrNg8yMwIgOlfk%2B2IgL%2FhyuY3NRMKUux73r8OVg5IdaN5MZjzkqhgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBDwGN2KKVbpsyiXaircAxlTmjjwg%2B%2FuN4f1X24Pl4XuXfJqg8iJrXL8MEZT94U8tAOra3BJXI8YrpvLgGIi1hu1IbMeD6Y%2FPWUjqcaL3AstoyihZZFrzNYadZ9wxMvV10HRObCZsQ2u2UbZQFMwfuuo65ZnjgXfpM%2BGp9dFJt%2FWrPtrHCdozbFZzFGgEJ3ZqOkFZnLoqHEuJwZoivxc6ePTgpd%2ByDLdFxZx8PHYl4qJIhQ%2B6aI9lFhlNogmeJQgtaljL%2FiAHRZ9fLcIASDeGznCmMI9GBgvnj0ANt7vJ5LwBGVYlpH8vmsbcFOOIMlo6mN1i0%2FlQRhTH3JlUZQ%2Fw8bDDK8FErxm%2FR0Y9WDPLRvo8FdtkmkiJFXkSK80GXkf9rxuXjZUt36EK4lVODDG%2BsgM8KgSADnaK%2FEwpqFbeKJwnC%2BiakKgOtYKU0RrwLdqhFwd6UV87nhw4vealZcCmxUeU6%2Fi%2Bp2AvsnypNiftAIqNcYhcF%2FFie3P7Gry2r%2ByMNOoh4dIX90%2B0NGwWFezl3OMTdmCCuAOFcYp9ECBgfJOG8clx6O8W7%2FHe%2FhbQHe6EG1vXkq7syzsWLmx%2FouEvZDGnkxN8AZs3Z55fjdtSIK%2FOrIa%2FivUfo7kHC499opCHtz4YMaU2MFIYCAKMOCKmL0GOqUBGYuAHDczRxnS6%2Ff%2FBidlq%2FWVLfPvnTI8fxzmNQkYWH5AEKbcGxt%2BT0TsO6c0iVJzRXv%2FX3QcR%2FlAelVQPMphGN2k%2FNYh%2BkV4a1BAW8qddW758dZ9VdYztZedAerN9mz8pf3ki02VwxCOJchiC9ddFPBI8pfCgDRMW5PFNCKnKILFkeq2nw9EnGpsawv%2F%2Fw%2FQ%2BWSXP6OAOKhvFrfaU0yE6hkPZ0HW&X-Amz-Signature=824470e68144b0e44db15417bbfb46a324b5243cc151674c2337aa3a2a49a192&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCIJATQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmfpCn%2FokL8FmiN03tc%2F56zyepIlGdVQzDb%2BNrNg8yMwIgOlfk%2B2IgL%2FhyuY3NRMKUux73r8OVg5IdaN5MZjzkqhgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBDwGN2KKVbpsyiXaircAxlTmjjwg%2B%2FuN4f1X24Pl4XuXfJqg8iJrXL8MEZT94U8tAOra3BJXI8YrpvLgGIi1hu1IbMeD6Y%2FPWUjqcaL3AstoyihZZFrzNYadZ9wxMvV10HRObCZsQ2u2UbZQFMwfuuo65ZnjgXfpM%2BGp9dFJt%2FWrPtrHCdozbFZzFGgEJ3ZqOkFZnLoqHEuJwZoivxc6ePTgpd%2ByDLdFxZx8PHYl4qJIhQ%2B6aI9lFhlNogmeJQgtaljL%2FiAHRZ9fLcIASDeGznCmMI9GBgvnj0ANt7vJ5LwBGVYlpH8vmsbcFOOIMlo6mN1i0%2FlQRhTH3JlUZQ%2Fw8bDDK8FErxm%2FR0Y9WDPLRvo8FdtkmkiJFXkSK80GXkf9rxuXjZUt36EK4lVODDG%2BsgM8KgSADnaK%2FEwpqFbeKJwnC%2BiakKgOtYKU0RrwLdqhFwd6UV87nhw4vealZcCmxUeU6%2Fi%2Bp2AvsnypNiftAIqNcYhcF%2FFie3P7Gry2r%2ByMNOoh4dIX90%2B0NGwWFezl3OMTdmCCuAOFcYp9ECBgfJOG8clx6O8W7%2FHe%2FhbQHe6EG1vXkq7syzsWLmx%2FouEvZDGnkxN8AZs3Z55fjdtSIK%2FOrIa%2FivUfo7kHC499opCHtz4YMaU2MFIYCAKMOCKmL0GOqUBGYuAHDczRxnS6%2Ff%2FBidlq%2FWVLfPvnTI8fxzmNQkYWH5AEKbcGxt%2BT0TsO6c0iVJzRXv%2FX3QcR%2FlAelVQPMphGN2k%2FNYh%2BkV4a1BAW8qddW758dZ9VdYztZedAerN9mz8pf3ki02VwxCOJchiC9ddFPBI8pfCgDRMW5PFNCKnKILFkeq2nw9EnGpsawv%2F%2Fw%2FQ%2BWSXP6OAOKhvFrfaU0yE6hkPZ0HW&X-Amz-Signature=5cc98de181e3fd066209a5e2ccb210355c2111c6bdd2da7a049ce44bb630028e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCIJATQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmfpCn%2FokL8FmiN03tc%2F56zyepIlGdVQzDb%2BNrNg8yMwIgOlfk%2B2IgL%2FhyuY3NRMKUux73r8OVg5IdaN5MZjzkqhgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBDwGN2KKVbpsyiXaircAxlTmjjwg%2B%2FuN4f1X24Pl4XuXfJqg8iJrXL8MEZT94U8tAOra3BJXI8YrpvLgGIi1hu1IbMeD6Y%2FPWUjqcaL3AstoyihZZFrzNYadZ9wxMvV10HRObCZsQ2u2UbZQFMwfuuo65ZnjgXfpM%2BGp9dFJt%2FWrPtrHCdozbFZzFGgEJ3ZqOkFZnLoqHEuJwZoivxc6ePTgpd%2ByDLdFxZx8PHYl4qJIhQ%2B6aI9lFhlNogmeJQgtaljL%2FiAHRZ9fLcIASDeGznCmMI9GBgvnj0ANt7vJ5LwBGVYlpH8vmsbcFOOIMlo6mN1i0%2FlQRhTH3JlUZQ%2Fw8bDDK8FErxm%2FR0Y9WDPLRvo8FdtkmkiJFXkSK80GXkf9rxuXjZUt36EK4lVODDG%2BsgM8KgSADnaK%2FEwpqFbeKJwnC%2BiakKgOtYKU0RrwLdqhFwd6UV87nhw4vealZcCmxUeU6%2Fi%2Bp2AvsnypNiftAIqNcYhcF%2FFie3P7Gry2r%2ByMNOoh4dIX90%2B0NGwWFezl3OMTdmCCuAOFcYp9ECBgfJOG8clx6O8W7%2FHe%2FhbQHe6EG1vXkq7syzsWLmx%2FouEvZDGnkxN8AZs3Z55fjdtSIK%2FOrIa%2FivUfo7kHC499opCHtz4YMaU2MFIYCAKMOCKmL0GOqUBGYuAHDczRxnS6%2Ff%2FBidlq%2FWVLfPvnTI8fxzmNQkYWH5AEKbcGxt%2BT0TsO6c0iVJzRXv%2FX3QcR%2FlAelVQPMphGN2k%2FNYh%2BkV4a1BAW8qddW758dZ9VdYztZedAerN9mz8pf3ki02VwxCOJchiC9ddFPBI8pfCgDRMW5PFNCKnKILFkeq2nw9EnGpsawv%2F%2Fw%2FQ%2BWSXP6OAOKhvFrfaU0yE6hkPZ0HW&X-Amz-Signature=73e3d95f45058e693ef09b1d4d6150a586b77e95c1a357d58f53fee1fa29f062&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCIJATQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmfpCn%2FokL8FmiN03tc%2F56zyepIlGdVQzDb%2BNrNg8yMwIgOlfk%2B2IgL%2FhyuY3NRMKUux73r8OVg5IdaN5MZjzkqhgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBDwGN2KKVbpsyiXaircAxlTmjjwg%2B%2FuN4f1X24Pl4XuXfJqg8iJrXL8MEZT94U8tAOra3BJXI8YrpvLgGIi1hu1IbMeD6Y%2FPWUjqcaL3AstoyihZZFrzNYadZ9wxMvV10HRObCZsQ2u2UbZQFMwfuuo65ZnjgXfpM%2BGp9dFJt%2FWrPtrHCdozbFZzFGgEJ3ZqOkFZnLoqHEuJwZoivxc6ePTgpd%2ByDLdFxZx8PHYl4qJIhQ%2B6aI9lFhlNogmeJQgtaljL%2FiAHRZ9fLcIASDeGznCmMI9GBgvnj0ANt7vJ5LwBGVYlpH8vmsbcFOOIMlo6mN1i0%2FlQRhTH3JlUZQ%2Fw8bDDK8FErxm%2FR0Y9WDPLRvo8FdtkmkiJFXkSK80GXkf9rxuXjZUt36EK4lVODDG%2BsgM8KgSADnaK%2FEwpqFbeKJwnC%2BiakKgOtYKU0RrwLdqhFwd6UV87nhw4vealZcCmxUeU6%2Fi%2Bp2AvsnypNiftAIqNcYhcF%2FFie3P7Gry2r%2ByMNOoh4dIX90%2B0NGwWFezl3OMTdmCCuAOFcYp9ECBgfJOG8clx6O8W7%2FHe%2FhbQHe6EG1vXkq7syzsWLmx%2FouEvZDGnkxN8AZs3Z55fjdtSIK%2FOrIa%2FivUfo7kHC499opCHtz4YMaU2MFIYCAKMOCKmL0GOqUBGYuAHDczRxnS6%2Ff%2FBidlq%2FWVLfPvnTI8fxzmNQkYWH5AEKbcGxt%2BT0TsO6c0iVJzRXv%2FX3QcR%2FlAelVQPMphGN2k%2FNYh%2BkV4a1BAW8qddW758dZ9VdYztZedAerN9mz8pf3ki02VwxCOJchiC9ddFPBI8pfCgDRMW5PFNCKnKILFkeq2nw9EnGpsawv%2F%2Fw%2FQ%2BWSXP6OAOKhvFrfaU0yE6hkPZ0HW&X-Amz-Signature=098fa0725618cdbd6e2bbc51b8f4be58e8f3fc9ed35ec7825d43a8c26d1d313e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCIJATQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmfpCn%2FokL8FmiN03tc%2F56zyepIlGdVQzDb%2BNrNg8yMwIgOlfk%2B2IgL%2FhyuY3NRMKUux73r8OVg5IdaN5MZjzkqhgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBDwGN2KKVbpsyiXaircAxlTmjjwg%2B%2FuN4f1X24Pl4XuXfJqg8iJrXL8MEZT94U8tAOra3BJXI8YrpvLgGIi1hu1IbMeD6Y%2FPWUjqcaL3AstoyihZZFrzNYadZ9wxMvV10HRObCZsQ2u2UbZQFMwfuuo65ZnjgXfpM%2BGp9dFJt%2FWrPtrHCdozbFZzFGgEJ3ZqOkFZnLoqHEuJwZoivxc6ePTgpd%2ByDLdFxZx8PHYl4qJIhQ%2B6aI9lFhlNogmeJQgtaljL%2FiAHRZ9fLcIASDeGznCmMI9GBgvnj0ANt7vJ5LwBGVYlpH8vmsbcFOOIMlo6mN1i0%2FlQRhTH3JlUZQ%2Fw8bDDK8FErxm%2FR0Y9WDPLRvo8FdtkmkiJFXkSK80GXkf9rxuXjZUt36EK4lVODDG%2BsgM8KgSADnaK%2FEwpqFbeKJwnC%2BiakKgOtYKU0RrwLdqhFwd6UV87nhw4vealZcCmxUeU6%2Fi%2Bp2AvsnypNiftAIqNcYhcF%2FFie3P7Gry2r%2ByMNOoh4dIX90%2B0NGwWFezl3OMTdmCCuAOFcYp9ECBgfJOG8clx6O8W7%2FHe%2FhbQHe6EG1vXkq7syzsWLmx%2FouEvZDGnkxN8AZs3Z55fjdtSIK%2FOrIa%2FivUfo7kHC499opCHtz4YMaU2MFIYCAKMOCKmL0GOqUBGYuAHDczRxnS6%2Ff%2FBidlq%2FWVLfPvnTI8fxzmNQkYWH5AEKbcGxt%2BT0TsO6c0iVJzRXv%2FX3QcR%2FlAelVQPMphGN2k%2FNYh%2BkV4a1BAW8qddW758dZ9VdYztZedAerN9mz8pf3ki02VwxCOJchiC9ddFPBI8pfCgDRMW5PFNCKnKILFkeq2nw9EnGpsawv%2F%2Fw%2FQ%2BWSXP6OAOKhvFrfaU0yE6hkPZ0HW&X-Amz-Signature=71506bfb7e5985244fc8cf5887539d810baff26eae7a4c7fbc0e307c22579c5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCIJATQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmfpCn%2FokL8FmiN03tc%2F56zyepIlGdVQzDb%2BNrNg8yMwIgOlfk%2B2IgL%2FhyuY3NRMKUux73r8OVg5IdaN5MZjzkqhgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBDwGN2KKVbpsyiXaircAxlTmjjwg%2B%2FuN4f1X24Pl4XuXfJqg8iJrXL8MEZT94U8tAOra3BJXI8YrpvLgGIi1hu1IbMeD6Y%2FPWUjqcaL3AstoyihZZFrzNYadZ9wxMvV10HRObCZsQ2u2UbZQFMwfuuo65ZnjgXfpM%2BGp9dFJt%2FWrPtrHCdozbFZzFGgEJ3ZqOkFZnLoqHEuJwZoivxc6ePTgpd%2ByDLdFxZx8PHYl4qJIhQ%2B6aI9lFhlNogmeJQgtaljL%2FiAHRZ9fLcIASDeGznCmMI9GBgvnj0ANt7vJ5LwBGVYlpH8vmsbcFOOIMlo6mN1i0%2FlQRhTH3JlUZQ%2Fw8bDDK8FErxm%2FR0Y9WDPLRvo8FdtkmkiJFXkSK80GXkf9rxuXjZUt36EK4lVODDG%2BsgM8KgSADnaK%2FEwpqFbeKJwnC%2BiakKgOtYKU0RrwLdqhFwd6UV87nhw4vealZcCmxUeU6%2Fi%2Bp2AvsnypNiftAIqNcYhcF%2FFie3P7Gry2r%2ByMNOoh4dIX90%2B0NGwWFezl3OMTdmCCuAOFcYp9ECBgfJOG8clx6O8W7%2FHe%2FhbQHe6EG1vXkq7syzsWLmx%2FouEvZDGnkxN8AZs3Z55fjdtSIK%2FOrIa%2FivUfo7kHC499opCHtz4YMaU2MFIYCAKMOCKmL0GOqUBGYuAHDczRxnS6%2Ff%2FBidlq%2FWVLfPvnTI8fxzmNQkYWH5AEKbcGxt%2BT0TsO6c0iVJzRXv%2FX3QcR%2FlAelVQPMphGN2k%2FNYh%2BkV4a1BAW8qddW758dZ9VdYztZedAerN9mz8pf3ki02VwxCOJchiC9ddFPBI8pfCgDRMW5PFNCKnKILFkeq2nw9EnGpsawv%2F%2Fw%2FQ%2BWSXP6OAOKhvFrfaU0yE6hkPZ0HW&X-Amz-Signature=32d788ac369d5aac14468f6d67c7714387fbd2ffef62bba1c03de820ddadceee&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3JK4C7G%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFjeYoPo5eJ6Q4XXCKxl%2FrNMZIodk26zp9SwuXaChqAlAiAwzmvDiZHXN3nVmvLBXVqF7590JbSrB2hTx25I3rFqYyr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMjstDf8bP37qhUd6AKtwDxgXyzprepsJWZPjO%2BYQ2mzjbWGn4l5CDbmM8LOvlHvKqiinfcnHqbMqaye9OCN5cVzUQStXygWBrlxS6zeS%2BaUkDng2tcAPJ4F9nm6Mbp4VXf4KO%2FNKRP71air5%2FBruguWlx%2FSCNdjKRfY8iGFIbzv%2FlIeK9EAk%2BGZ%2Fcrl8tgKJIf17hkfUKSqox3nGxlE7I27GEnE%2FiN8V2PKTmCxf16wmS0n84xW9zi5sD1V7tIAtXVKDJgWnOytNPXSO6Sqho9v5X7vMJc6HZI8OEKl1dwgZYieGYGkmMLPLcQABTQKNCvTs0LReaGIeU3RLf8ZyW7i4dQFWuSxNcUfwfVp%2FWKN7xdqSA9t2JUXNh4zgx9OKSOBUUPjHNiHvv44%2BQMRPHw92n3Eu5xnDU5taJYlgSZ41TKqp3Rt9D32pgc7Fi3wHu5RzJo5QTJOZWRiEA%2BGLrvTRnbDSoKD1snJ3P8EoP909P5bGeoBAYbEUIXClvkwI%2BXaJ4PgNR5phkEiagNgmf2X%2FOZ4KckvW6w%2Fu89txqBe3n%2BLPVAEAkfjCji3b9JmdXcPLFnMwouPEyTT25LEKpXD9wu118R1aZBKbhaBwJPtgUH2x2zFLjyQtDJozS6Ek41IFwHyv6Czfd9Pgw34qYvQY6pgE6Qa7n1CjErFRfK2JTGBwwk%2F7r7c8cuHIR1OKzClMTpViXllH4pUquUOpGjCHQlRvpjSst3Naddy1Dv7PczLYpK6%2FV%2BLrssWCa1ACialPcsZeC4LqXN36u8lTtTWjgYdtaF14WH%2F6UOm9hgz8U2KGZPKG1k7igTH%2FjxwKd8ybuqQTRJ02XCz2zL0fn6eBd8OFNf5hNuCmhGSwe7DF1HD1DeEtapwS6&X-Amz-Signature=3a4c2f1de41470650476e56fb111f68d9c0241f1b6e50a346d04dc090caa106a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q66ONWI2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQClblP1iXhC%2FatfQ6PatWmTxHzLD9GP%2B85CanA%2BeN3CugIgEQDJyaYOMU%2BmmS7ZUpcSGyMyf2199Pz0AtTeFhHijEIq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDJ5vWBu9xFBXepYLKircA1Cq9mTqm9924iLqB8v3gA5MuIPx0z%2BtMK0RPJNP1snPiL0CDKw%2BUXGnLbihKpzMYqve%2Bsy0Kte%2FeyaxJtYtcMUSyj7ba9l6PMm6EyhPloW1FvEXxf5BtkCvWT9i4C2AziSrPW%2FwgYSRHHlk55ey2xnt3Sq54J858PQlhnJ5qPbfelLGTXmKMHerHA%2BRuCo6xfAFjQCZ8SoNc7gfajWOAx43UknNNd7UHiXOsPvyhICO%2B%2FGGqH7Rb0UoFN2BYisClBu65zLiOTc0wIgxt8D0nXqQlDTyisKNx5%2BefqZIPR5z6dMQZobxBWO2gRzeZDcNkjic%2B6WSiFPoeT9eL5kJklGj5%2BVgi28a7kqYjKD55Q2Gnt4nx9RwdPqOfquDE63HrSbboLjBQYTalk1ls9HzfuNN12X%2FRrgsdvF%2FZXs6Asv4w2cM6GWnZe6kFwEEUyUL0tpCkHNn%2BMNaZHJFNJrI6x5yLUnNzBVhqWvT6VMG9eRsMETLv4blNQcyPRPez0aZ3vt29LVw%2B8mho%2FYAZ6jQUIDZlojJhdyX6MZHlI5glBGVaqo8odMkNvZmIhsAXsCZYe2BjTj82rYfwyCY7ncEbxiuY4QaG7kDQ9W%2F8xJlSVStXwoiRNoAdQIyqLW1MOmKmL0GOqUBRWSEJ4m3Wqnsh55P3Nhf1sVX40so6x%2B5Zuaf%2FoDDP8NWnKVah01%2FjWiNV6neMxytd0a9P9KJ8kOAoRmHs1Ru%2BM9Tk6MieVJpeglRC7qWy3C6ulNZybj%2Brd6pBLLVAiyl9JWvGPGPGX1yh%2B8bEUX4NUQnoCx0hUJZ2zxvBJBCvSQ%2FIAmxhYHsGeZ9gWDA8s4TxEdaUPDIuunTiOz%2BBfASXfyGM0PT&X-Amz-Signature=aaeef8ae6a658818b551dba687ff1f8d071ad134ed46a9d66af336ced81a290d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCIJATQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmfpCn%2FokL8FmiN03tc%2F56zyepIlGdVQzDb%2BNrNg8yMwIgOlfk%2B2IgL%2FhyuY3NRMKUux73r8OVg5IdaN5MZjzkqhgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBDwGN2KKVbpsyiXaircAxlTmjjwg%2B%2FuN4f1X24Pl4XuXfJqg8iJrXL8MEZT94U8tAOra3BJXI8YrpvLgGIi1hu1IbMeD6Y%2FPWUjqcaL3AstoyihZZFrzNYadZ9wxMvV10HRObCZsQ2u2UbZQFMwfuuo65ZnjgXfpM%2BGp9dFJt%2FWrPtrHCdozbFZzFGgEJ3ZqOkFZnLoqHEuJwZoivxc6ePTgpd%2ByDLdFxZx8PHYl4qJIhQ%2B6aI9lFhlNogmeJQgtaljL%2FiAHRZ9fLcIASDeGznCmMI9GBgvnj0ANt7vJ5LwBGVYlpH8vmsbcFOOIMlo6mN1i0%2FlQRhTH3JlUZQ%2Fw8bDDK8FErxm%2FR0Y9WDPLRvo8FdtkmkiJFXkSK80GXkf9rxuXjZUt36EK4lVODDG%2BsgM8KgSADnaK%2FEwpqFbeKJwnC%2BiakKgOtYKU0RrwLdqhFwd6UV87nhw4vealZcCmxUeU6%2Fi%2Bp2AvsnypNiftAIqNcYhcF%2FFie3P7Gry2r%2ByMNOoh4dIX90%2B0NGwWFezl3OMTdmCCuAOFcYp9ECBgfJOG8clx6O8W7%2FHe%2FhbQHe6EG1vXkq7syzsWLmx%2FouEvZDGnkxN8AZs3Z55fjdtSIK%2FOrIa%2FivUfo7kHC499opCHtz4YMaU2MFIYCAKMOCKmL0GOqUBGYuAHDczRxnS6%2Ff%2FBidlq%2FWVLfPvnTI8fxzmNQkYWH5AEKbcGxt%2BT0TsO6c0iVJzRXv%2FX3QcR%2FlAelVQPMphGN2k%2FNYh%2BkV4a1BAW8qddW758dZ9VdYztZedAerN9mz8pf3ki02VwxCOJchiC9ddFPBI8pfCgDRMW5PFNCKnKILFkeq2nw9EnGpsawv%2F%2Fw%2FQ%2BWSXP6OAOKhvFrfaU0yE6hkPZ0HW&X-Amz-Signature=193df85a003d549e66cc9b5115fa7cd2a18ca1f066336580fff6aee6d71e9bd6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCIJATQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmfpCn%2FokL8FmiN03tc%2F56zyepIlGdVQzDb%2BNrNg8yMwIgOlfk%2B2IgL%2FhyuY3NRMKUux73r8OVg5IdaN5MZjzkqhgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBDwGN2KKVbpsyiXaircAxlTmjjwg%2B%2FuN4f1X24Pl4XuXfJqg8iJrXL8MEZT94U8tAOra3BJXI8YrpvLgGIi1hu1IbMeD6Y%2FPWUjqcaL3AstoyihZZFrzNYadZ9wxMvV10HRObCZsQ2u2UbZQFMwfuuo65ZnjgXfpM%2BGp9dFJt%2FWrPtrHCdozbFZzFGgEJ3ZqOkFZnLoqHEuJwZoivxc6ePTgpd%2ByDLdFxZx8PHYl4qJIhQ%2B6aI9lFhlNogmeJQgtaljL%2FiAHRZ9fLcIASDeGznCmMI9GBgvnj0ANt7vJ5LwBGVYlpH8vmsbcFOOIMlo6mN1i0%2FlQRhTH3JlUZQ%2Fw8bDDK8FErxm%2FR0Y9WDPLRvo8FdtkmkiJFXkSK80GXkf9rxuXjZUt36EK4lVODDG%2BsgM8KgSADnaK%2FEwpqFbeKJwnC%2BiakKgOtYKU0RrwLdqhFwd6UV87nhw4vealZcCmxUeU6%2Fi%2Bp2AvsnypNiftAIqNcYhcF%2FFie3P7Gry2r%2ByMNOoh4dIX90%2B0NGwWFezl3OMTdmCCuAOFcYp9ECBgfJOG8clx6O8W7%2FHe%2FhbQHe6EG1vXkq7syzsWLmx%2FouEvZDGnkxN8AZs3Z55fjdtSIK%2FOrIa%2FivUfo7kHC499opCHtz4YMaU2MFIYCAKMOCKmL0GOqUBGYuAHDczRxnS6%2Ff%2FBidlq%2FWVLfPvnTI8fxzmNQkYWH5AEKbcGxt%2BT0TsO6c0iVJzRXv%2FX3QcR%2FlAelVQPMphGN2k%2FNYh%2BkV4a1BAW8qddW758dZ9VdYztZedAerN9mz8pf3ki02VwxCOJchiC9ddFPBI8pfCgDRMW5PFNCKnKILFkeq2nw9EnGpsawv%2F%2Fw%2FQ%2BWSXP6OAOKhvFrfaU0yE6hkPZ0HW&X-Amz-Signature=c12582d264b2fb8a56b2ad4f8156d411f0818c0df8055c6aa5745d416c12ce0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCIJATQC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDmfpCn%2FokL8FmiN03tc%2F56zyepIlGdVQzDb%2BNrNg8yMwIgOlfk%2B2IgL%2FhyuY3NRMKUux73r8OVg5IdaN5MZjzkqhgq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBDwGN2KKVbpsyiXaircAxlTmjjwg%2B%2FuN4f1X24Pl4XuXfJqg8iJrXL8MEZT94U8tAOra3BJXI8YrpvLgGIi1hu1IbMeD6Y%2FPWUjqcaL3AstoyihZZFrzNYadZ9wxMvV10HRObCZsQ2u2UbZQFMwfuuo65ZnjgXfpM%2BGp9dFJt%2FWrPtrHCdozbFZzFGgEJ3ZqOkFZnLoqHEuJwZoivxc6ePTgpd%2ByDLdFxZx8PHYl4qJIhQ%2B6aI9lFhlNogmeJQgtaljL%2FiAHRZ9fLcIASDeGznCmMI9GBgvnj0ANt7vJ5LwBGVYlpH8vmsbcFOOIMlo6mN1i0%2FlQRhTH3JlUZQ%2Fw8bDDK8FErxm%2FR0Y9WDPLRvo8FdtkmkiJFXkSK80GXkf9rxuXjZUt36EK4lVODDG%2BsgM8KgSADnaK%2FEwpqFbeKJwnC%2BiakKgOtYKU0RrwLdqhFwd6UV87nhw4vealZcCmxUeU6%2Fi%2Bp2AvsnypNiftAIqNcYhcF%2FFie3P7Gry2r%2ByMNOoh4dIX90%2B0NGwWFezl3OMTdmCCuAOFcYp9ECBgfJOG8clx6O8W7%2FHe%2FhbQHe6EG1vXkq7syzsWLmx%2FouEvZDGnkxN8AZs3Z55fjdtSIK%2FOrIa%2FivUfo7kHC499opCHtz4YMaU2MFIYCAKMOCKmL0GOqUBGYuAHDczRxnS6%2Ff%2FBidlq%2FWVLfPvnTI8fxzmNQkYWH5AEKbcGxt%2BT0TsO6c0iVJzRXv%2FX3QcR%2FlAelVQPMphGN2k%2FNYh%2BkV4a1BAW8qddW758dZ9VdYztZedAerN9mz8pf3ki02VwxCOJchiC9ddFPBI8pfCgDRMW5PFNCKnKILFkeq2nw9EnGpsawv%2F%2Fw%2FQ%2BWSXP6OAOKhvFrfaU0yE6hkPZ0HW&X-Amz-Signature=27e8e5bfbf5d0d6dfc4833ba70353c3dec75abcb903ddf70442b5eb0fdfa88e7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBECTHEU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDvuXo23wvoCDbeYO6CdY38MiLETqn9fWeE8bW0WVU6ZgIhAIX924NutBQzac6V0lhTJsjgaGlLe%2BKvGHAFCwZxEt4bKv8DCHYQABoMNjM3NDIzMTgzODA1IgxWhRh7YccjX4jMXz0q3APS4ajnlHYs1s9nAmrzaRK3DP3HjzYGknyGmz%2BKAi23IQSVYo1AL3mo4xt0%2FLqZkyfAG8rphnEfdXlOOP1LfYJoSE2XdS7LscXaKyPlP0Td5iHI6Ec3DpNnXJoOVJ2a5jHQ5V4zpxQbOmM9ONMyyVL%2FAPDBALsuWa0qEVZxDdBABYQn40KQyVecVSWkvROpzz56vyCVoipMPHRzmF2CkTTe4ynRBIP9kodFte9LZwwwf0rKLOd%2B%2BtmaWUXtSj4KE5WdYCWZOZDjhu9jb0xnX79E44w1%2B7QOF%2FuDP4LFIx52mF3ZaKF%2FmDaYX734purrjjlNN9bx%2FNLq5bz3Wbj8txPNv5yzfxVRSjq%2Fqx%2F4CwDBj9yzTCaCTc1ASbjlGnKThRdv4ld0SB%2FzJa0I9JPrHrEMd%2BevdVv7D9ar8EiJmWHtRXSYLmSjEMhosZnWIqTOMa80FWx%2BYlo53V%2Bktm%2FsCrKyAUH7nrq5MGINKjidKGC195500beBWF%2F9S7%2B444sTbQ%2FCZfEfHktLHeeVN4zzAeNTY3uVknsP%2BMHjShyTl2o4kAtzBqBGXHzAQIQoq15eIei1tfSwr1LioBB0nvXtX7wXi5WtalCvHzczFCfhTxyWQEFl62k6PMpCP%2B288TCsi5i9BjqkAcSJ1hAokVRLlQlhZ22c7m%2FmPZLMWTU%2B1oozM67xFwr4d6Opyjlzc0CP0pWod3jOBGRfBDcuA%2BH%2Br19Q1QOf8q89L%2BNjMmiKj6qEGADIGhsZU8N4FFLWxDNWcbR9sRcLmUhO%2Bynb2AB1lV%2F7f2qaHUOn6hiTycXlR%2FT0JeE7wTbJi5HjzloeM6z3j7NiFjBYaxnCbcRrwnQLm2lS1HxbhCS1o65I&X-Amz-Signature=26961a46226c3ff02fc226bd0a0d303b79a01d7b5585afb094308dd29748a82a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652CDL6RD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIC85AdazF24z3DdWwbcYSNJ8l0YVasCMiuR2CiJNrTrnAiEA1O5ztnzgeAd3XmyKYqaTsgqkYPSDsnib0hHNuR0IvYEq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGKKzaw5bNAjO6GAUCrcA2bmVd9NWXfrdLKAw%2BBSqdCirNXJb%2BMXmTS9vRUqqWVGcx21kOyVYtmAG0j3wtTEwUOeETbkPhjVJr%2BcP0GMeSDpkOGNwgqk25ZLYjlLcZ6A8Z%2B9rU13pHL0teCtJhmfYVQECTK8iefBkXusKP0Ipnk1QH6Bs1jYGy6I3lukBh0%2F8spmC8WVCuNgNPVb4KR%2BbcCiKDMiTk7N1DYgR8JOgoV3lYs%2F5fiC5Zcd10ISfI6RmG9p8LY37YczK8xLmbqlqsHRigaqbS1VzzuqwbonL6orH%2FKvk1p9oZkMX%2BEchSzKmjOhLlXX9unlx8qm5p0LZna%2FAfD6%2F%2FTAxR3ANGnrGZrSt34zfMCTF3hCAosHeqN6F0o8thylOmur7D6vM3jrod5R%2BIfe%2FNGZWObE5RtTtQCsnFcChCXP0Uh3XfFMut%2F0QbIWR22Hbp15zYKrqKsIHHAZWtOJOG0G4c4k%2FKzFHLbNcEC3nUKr9ssaRBAXHlugKTw6Nm1jIPDJ194zYPiakL7kxy1kuSgb%2B3I5hgoeoB2fUYs6I7Cm82OcbQ863qQPEunSkmMYHELxdFz%2Bn3KL4t%2FpDE5NjaBCtNXMqlZWE7uhyRy9CLX%2FnewdH76VdCyDUbc%2B0PTKb%2BEy71EtMIaLmL0GOqUBpJwYZwFhzLW9QuOOEHahRKVeMhVHkzU4MFROYhnWOQNrQYDHa7RIQtP6J3KApeSqaH9RUMG8jSqotMIDjjxqAEHEjsaGsDtYjEBMsTr%2Fmjyxe4njzMhXhnJHnxLCEXcDIY9MpPUJ5j1GRVeUe65%2FkNQDaPwNdqYv8maxt9haXKEqBr2CJ8Cuv2B9%2Fby5RFqJibN%2BX6Cq5uVWPISVj9%2FdP9q%2BsaxJ&X-Amz-Signature=4f5efd34096446f5e211da68909571e3f545e6cd8f1e021c5fb76739bbd4f483&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRY56DZZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIGU%2FYncmsCYcGe7Mf5LC3M4oviFQNRNHTD5wiUdSV65iAiBOf00sqiBDiEyOGDICjlJwTTwNr1emSfKOEAcXgWw9rSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMxndgxwZJTRve%2BAwlKtwDXtf5jnzLFwz4dROdszJN5CmvaTdLhkBD7mOxRN9woBRD5znUIAXJP47a9%2FM0SMTgHOSWX2aTzQtoV0afAtRhxls0l2NwKdmIo2K0c06wSq7QuA2YEWseE6O5HuIHR0ZKC57xmMmXLCf%2Bfq4vA6vvIrnNt1bZfRv6owLoBf7wPjpUyXCpoyJN8uaX4k0sV4Q%2Fd8djBWGel3lg8yX5UFA20xPwmYISG1FD8asXmiDUejLvQPshcv0mgsOM9%2Bp3MI7So5X1lJrLdrAI6ii0ZLjhait9dxkXFiOlqD%2B6WCdFjCXs%2BEhKHOfKDiK4%2FPk2sptyAFB3EkKj7X22dShy6Vv98NCIJ9sR6Jj8Sf74OutUnNMhYCneSb04nk10rdZaCwP4fIoub5yuijr40cNwqYLhAlxM2G6r41qVs3e60BaphRj3PM8YU7Xruia8CP54CuBT%2BA7yUoExg9kx4V%2B9gRyQi%2BD2P73Mld3VjMezWxPL5QHHJ1QqbEg7DBcGXy%2FeOchg%2FeYfMnbP7RSZHkHMh4NBFgrpjIBStYR3EUexxBirsQ5XjHa2p6FyfMJkFtMfdWH9doRKOl7l4qyamjSsen2xf6WDKEnXFcJe9T1XMIrXuw4QqLCS09tKGyOa0%2Bcw4IqYvQY6pgGatsmB310RwId47cgOtyMK0%2BxN0NPrDRjduKAzwxC8MUfpYUUwEKI1ycW2AcC48e6RdlBC5%2BHUftrvypkSZIK9PXWHUVnpG%2BEvG%2FtFj1Bp1LKHWhNTsYjpP%2FgzXeeyb04Z9t4t%2BJHaUBSEvxH3pTXLnUJBxFKKS4k%2BsMmJ5cqhZl0eQBULl%2BXyG2gcxOPlC26anjNwDHCSVLK3c7cR2h44X5aN54Ou&X-Amz-Signature=007275b1a9fd63031257a72f0bc185fcef316405f6e32f7dc78f664e39ca63a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKL5FQ2E%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDOo%2F5hHx%2BzbJJDVZa07fhqoFsbyAMG8odJu8fPwdzpyAIhAKfGhnq08lq37gLTxn%2BTO1Joae25PvmK80oPda5OOfIiKv8DCHYQABoMNjM3NDIzMTgzODA1Igy8pQx%2FuIZ%2BcDYBWloq3AOlgwXoujaq%2FI4m5wcDARhtwMXBplah%2Ba67I1%2FlRrjFjsVXq043%2FuC1XTnio6V5bP95NycQ1OtdIKVlLdH5LpRk8EmAVFZZ17gl5JmZjPd%2BdPBQeXOUn2SVzRCYrkEV2Jdu2%2F70oMzh7hogtD%2Fyk7FCWmeqIsTYyMBYhneM6gyJ3efcJWeUio6Sni8RXLtQzktRSWcI9V4d7u3VTQBQcRABz9%2FVsIaB20Dp%2F%2FnB3GMtko%2FaA6h2sr0OkGlBgMtyF0EhsD%2BnECRUptCXNTtMLpudlsOafhOVkIwslsbJhueSZBjBlDHhBeNpOQWmVaNcsIYQreRiWymUfRo%2Bxe1xLqQiv0gwpHwDy9QZv2hX2WQxkLvTVHn1mHSq2yhTq4yTxHaZBT89Zcx3K694RpZDTkqwCN1oJBgmYvD3r3GVPsT59zQGm2ie0cLzlGxazhsz%2BhAIIhK0tahx4DZizgaX3NojHEDj53OSxa6nYskdHeuCBh89entjr7GFphUgEe%2FOAVBA39t3tMTPjwmsGsUSaE6raiSlmusrTzqK1H%2FoM3ZvDIZXHdojjzMDRIDVRXIjh8pBkfLupHmfMNBUiwTWACOZwetzMmWooQan5ncEsGqq8xXr8WXHhoPDvS2q9DCKi5i9BjqkAbNRTcL%2FDgOAzgHaoZZ8ktttRVVPpRRPGtV%2FEt75yBIT1ESHE2gIuBp%2BFrjhUG4Ffpk3HA3vcykLn38mGqAFq4S2%2BtUc0TNYLJJKCV6gkfX4x98E01LumIob4UbckGx%2FMTxY%2Fa2lq2mzLYC5pK4%2FFZik%2F%2Fl%2BP%2Bxje7E9Tb4X8bqBQGSyHhmf9vmeWW7%2FlPcEI3%2F7ri1XW1zSjeeDi5W6HywZiwMu&X-Amz-Signature=cea62ebf10515e441ff6ebbfc32273c354e519ddb833c42a0acd5cda9e31906a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKL5FQ2E%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDOo%2F5hHx%2BzbJJDVZa07fhqoFsbyAMG8odJu8fPwdzpyAIhAKfGhnq08lq37gLTxn%2BTO1Joae25PvmK80oPda5OOfIiKv8DCHYQABoMNjM3NDIzMTgzODA1Igy8pQx%2FuIZ%2BcDYBWloq3AOlgwXoujaq%2FI4m5wcDARhtwMXBplah%2Ba67I1%2FlRrjFjsVXq043%2FuC1XTnio6V5bP95NycQ1OtdIKVlLdH5LpRk8EmAVFZZ17gl5JmZjPd%2BdPBQeXOUn2SVzRCYrkEV2Jdu2%2F70oMzh7hogtD%2Fyk7FCWmeqIsTYyMBYhneM6gyJ3efcJWeUio6Sni8RXLtQzktRSWcI9V4d7u3VTQBQcRABz9%2FVsIaB20Dp%2F%2FnB3GMtko%2FaA6h2sr0OkGlBgMtyF0EhsD%2BnECRUptCXNTtMLpudlsOafhOVkIwslsbJhueSZBjBlDHhBeNpOQWmVaNcsIYQreRiWymUfRo%2Bxe1xLqQiv0gwpHwDy9QZv2hX2WQxkLvTVHn1mHSq2yhTq4yTxHaZBT89Zcx3K694RpZDTkqwCN1oJBgmYvD3r3GVPsT59zQGm2ie0cLzlGxazhsz%2BhAIIhK0tahx4DZizgaX3NojHEDj53OSxa6nYskdHeuCBh89entjr7GFphUgEe%2FOAVBA39t3tMTPjwmsGsUSaE6raiSlmusrTzqK1H%2FoM3ZvDIZXHdojjzMDRIDVRXIjh8pBkfLupHmfMNBUiwTWACOZwetzMmWooQan5ncEsGqq8xXr8WXHhoPDvS2q9DCKi5i9BjqkAbNRTcL%2FDgOAzgHaoZZ8ktttRVVPpRRPGtV%2FEt75yBIT1ESHE2gIuBp%2BFrjhUG4Ffpk3HA3vcykLn38mGqAFq4S2%2BtUc0TNYLJJKCV6gkfX4x98E01LumIob4UbckGx%2FMTxY%2Fa2lq2mzLYC5pK4%2FFZik%2F%2Fl%2BP%2Bxje7E9Tb4X8bqBQGSyHhmf9vmeWW7%2FlPcEI3%2F7ri1XW1zSjeeDi5W6HywZiwMu&X-Amz-Signature=70a4e046cffe6d6bd8c3a1d5c4b8ef962846e7769bbdbb9f026d2f51c309bdcd&X-Amz-SignedHeaders=host&x-id=GetObject)

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
