

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUGT3RH5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGPADKsYDzXH9mMHm6YacZ%2F%2BYXSDuU8LBPR%2FgTc9Al5fAiEAkKpV%2FORP1DBJEADk5NULCtSPu%2BGiYQ0iaOdcSyikppQqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPsKJPjD%2BkB53d5ESCrcA%2F9NSksY5ZOEq0Zn37bcI2qaOljif7lfwVqu1cEd83sGKVNoeb94Pyy2BFPW8FCcUypz87usJYEsqZohlbdbJrHjKsK7qNhWbjY%2FLMBe%2Bc56xUMNu%2FrHMMBnUUIwiLykfc4hloVa5y2YAcfGWgRXjtMpaGY5ERzOkFN1FakgsGn7W4r%2FaN8Mdi6NxxF7arebj1Zox6FWVlpA5fY64mhUyKWhmAK7Oil8dM%2BpTQ%2FUdfI3NqkBusD0mmjBHthkH1fI8idL6IlrUpQJ1cM9u5zcUK%2FV%2B7tkiEWVCb3U%2F7ZfA3v7wQNYM%2Fz0VINzBQ7j8AKSadwbI5SDFsxriZhRXGQobYYGC4oneZ8O2uGWZjjoxqv7cWIzqmcfht%2Ba4prattSga8vSV5ODkuZn%2BeRHBLD9b6InN9iqYkXJ1cNzyek8EFSTGKMNmWLYKVPvLGg8Bq7Zkqxyx6CqKT8EWoshaRBVwpUaxsey383yG4eqHmH59eA7W4Hs1Zi%2BZpB3qJr2zFqIK4YZvl8Ck8FRSRvZLyFOXcwG7RHBgGzYC%2BIJ9S7OkYB9xIoFjzYDo9XJVv3Cwsq1jG9QAMMJW7utKp8zUdhfR1DBdZC%2Frv3bH243LOZMBV8vpyCAbZ7Ny8hmc62bMIGR%2FrwGOqUB0za5wGhC4LwZAK7Hm8%2Fn09l9B0tRqE%2BwS3C5wq29ZDY4KNHICaotOS1IDqchw8f%2BVLNIXCP7j8OUXB%2FUWuOxWeIILP%2F%2FWYKHX2vOgegkrLQnW9VDNBSGypoV%2BNNKuwiD64QP7w%2F%2FVJVkloaoyzAaWuzdKyy8b8SfWDXwN7Vwt6j69lm5OKmccQvneCWQX8UadmA6DoTnKxktvNypKC49zknUc7t0&X-Amz-Signature=f6beaeb1a645b9bea7883a21cfc20e98091640acbd3d640c77f9aa36b0da7ac4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUGT3RH5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGPADKsYDzXH9mMHm6YacZ%2F%2BYXSDuU8LBPR%2FgTc9Al5fAiEAkKpV%2FORP1DBJEADk5NULCtSPu%2BGiYQ0iaOdcSyikppQqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPsKJPjD%2BkB53d5ESCrcA%2F9NSksY5ZOEq0Zn37bcI2qaOljif7lfwVqu1cEd83sGKVNoeb94Pyy2BFPW8FCcUypz87usJYEsqZohlbdbJrHjKsK7qNhWbjY%2FLMBe%2Bc56xUMNu%2FrHMMBnUUIwiLykfc4hloVa5y2YAcfGWgRXjtMpaGY5ERzOkFN1FakgsGn7W4r%2FaN8Mdi6NxxF7arebj1Zox6FWVlpA5fY64mhUyKWhmAK7Oil8dM%2BpTQ%2FUdfI3NqkBusD0mmjBHthkH1fI8idL6IlrUpQJ1cM9u5zcUK%2FV%2B7tkiEWVCb3U%2F7ZfA3v7wQNYM%2Fz0VINzBQ7j8AKSadwbI5SDFsxriZhRXGQobYYGC4oneZ8O2uGWZjjoxqv7cWIzqmcfht%2Ba4prattSga8vSV5ODkuZn%2BeRHBLD9b6InN9iqYkXJ1cNzyek8EFSTGKMNmWLYKVPvLGg8Bq7Zkqxyx6CqKT8EWoshaRBVwpUaxsey383yG4eqHmH59eA7W4Hs1Zi%2BZpB3qJr2zFqIK4YZvl8Ck8FRSRvZLyFOXcwG7RHBgGzYC%2BIJ9S7OkYB9xIoFjzYDo9XJVv3Cwsq1jG9QAMMJW7utKp8zUdhfR1DBdZC%2Frv3bH243LOZMBV8vpyCAbZ7Ny8hmc62bMIGR%2FrwGOqUB0za5wGhC4LwZAK7Hm8%2Fn09l9B0tRqE%2BwS3C5wq29ZDY4KNHICaotOS1IDqchw8f%2BVLNIXCP7j8OUXB%2FUWuOxWeIILP%2F%2FWYKHX2vOgegkrLQnW9VDNBSGypoV%2BNNKuwiD64QP7w%2F%2FVJVkloaoyzAaWuzdKyy8b8SfWDXwN7Vwt6j69lm5OKmccQvneCWQX8UadmA6DoTnKxktvNypKC49zknUc7t0&X-Amz-Signature=a58ca2b5283d7116eee9f2c4948e49e180a789359b73fc6278056769e13a453e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUGT3RH5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGPADKsYDzXH9mMHm6YacZ%2F%2BYXSDuU8LBPR%2FgTc9Al5fAiEAkKpV%2FORP1DBJEADk5NULCtSPu%2BGiYQ0iaOdcSyikppQqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPsKJPjD%2BkB53d5ESCrcA%2F9NSksY5ZOEq0Zn37bcI2qaOljif7lfwVqu1cEd83sGKVNoeb94Pyy2BFPW8FCcUypz87usJYEsqZohlbdbJrHjKsK7qNhWbjY%2FLMBe%2Bc56xUMNu%2FrHMMBnUUIwiLykfc4hloVa5y2YAcfGWgRXjtMpaGY5ERzOkFN1FakgsGn7W4r%2FaN8Mdi6NxxF7arebj1Zox6FWVlpA5fY64mhUyKWhmAK7Oil8dM%2BpTQ%2FUdfI3NqkBusD0mmjBHthkH1fI8idL6IlrUpQJ1cM9u5zcUK%2FV%2B7tkiEWVCb3U%2F7ZfA3v7wQNYM%2Fz0VINzBQ7j8AKSadwbI5SDFsxriZhRXGQobYYGC4oneZ8O2uGWZjjoxqv7cWIzqmcfht%2Ba4prattSga8vSV5ODkuZn%2BeRHBLD9b6InN9iqYkXJ1cNzyek8EFSTGKMNmWLYKVPvLGg8Bq7Zkqxyx6CqKT8EWoshaRBVwpUaxsey383yG4eqHmH59eA7W4Hs1Zi%2BZpB3qJr2zFqIK4YZvl8Ck8FRSRvZLyFOXcwG7RHBgGzYC%2BIJ9S7OkYB9xIoFjzYDo9XJVv3Cwsq1jG9QAMMJW7utKp8zUdhfR1DBdZC%2Frv3bH243LOZMBV8vpyCAbZ7Ny8hmc62bMIGR%2FrwGOqUB0za5wGhC4LwZAK7Hm8%2Fn09l9B0tRqE%2BwS3C5wq29ZDY4KNHICaotOS1IDqchw8f%2BVLNIXCP7j8OUXB%2FUWuOxWeIILP%2F%2FWYKHX2vOgegkrLQnW9VDNBSGypoV%2BNNKuwiD64QP7w%2F%2FVJVkloaoyzAaWuzdKyy8b8SfWDXwN7Vwt6j69lm5OKmccQvneCWQX8UadmA6DoTnKxktvNypKC49zknUc7t0&X-Amz-Signature=878c462a2aaf673f99c5c8e9e57cb2fc275b392ca3dacda64cd4f6d4552dc86e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REABTWKF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrcBjERooDnw6uQKovvREJU%2FNUCi1WIecEPD9K3u0L7AiEAp3Y%2FMzo%2FCji4P3rhbrQ1ga16YQMazMVbwcLiCNH%2BHQoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx8yJrba4Lm8NgB%2ByrcA9VRWOVud1cI7N%2FAI8XZ2EdWgP%2FYi3FGQAsB6xezlIVzm3hRLox%2Fv4HmAxEAcBWu1AUpQpxtjZvK%2FDt2buXkEE%2FDJnjVswSM8kprrYVFtTQ6kxQQQ8KpzXzg39eazS%2BwGYaFtZ9Vc26zX5Zxv3gR6OvLcsL7MGIS6OUGwavdjzvy3Qwp1MVta%2F2hfXZZeOmc3BtrjowsT4LeZ8gDW47Q5UTYO3Y9Ofa9PazUMPF7JpTCr09gzLuxIs0RC1SOZFuptRaCYBUe9%2F8UMW3X58OCEuzuqdeayKSCfRRxe37D71CTTSTqxw%2FNhaZwcJ7rgzEijBVRIfMvaI4%2FyLMZO3DxcBoOU44moh2jbItaXdYX2HTQptAsuEKn43xhxM%2FrXbb3Cbm7MjtUnkQwLhzl5WynKp57pnuAPFPNbxwBmr7XMB9gLNW%2BTghPqAqNaUf%2BsEihXU4IPyYQLEWphs7MnjhoXf9nMEem1XiH8dg84tuBk2EPEq75wMC5tCUAPDqn3NvJXbmN0pWoVqG31zSKi1xt4cCmhF2nN5IZLDKTAtyTWZUpwaiYGUZHHKyamM12ly9zfqhuCCJHIDtVKEeCUTimRswqSykJXgs4DbJMe77ZDnd4OBWFtAnDooBVi%2F5kMPPA%2FbwGOqUBHm1se8Y15vLFiyVZXJ4r%2BaP6mzL8FoQLZhyZn%2F%2ByFYV0pVaDFNe92BAzsoG5nD0RVAnA4e%2Fr560HY%2FzxeD%2FV2uFNMC4eof9%2Fewgwq%2BYE4A%2FDMxJfnUF6ByqeSDhwJ7ieyLnir9gt6vDwA8BUnZ5DXe73sxH6qzo9kn3OZJ1%2BoT281Dqrs65E%2Fr4qB%2BplZobhbsTs27UjDHrFbY3w4spaWFloIN4l&X-Amz-Signature=082c452a47f016cd5fcdcf3220bea7371b8a00fd94a69e5bc6f2fc8832c6495a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REABTWKF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrcBjERooDnw6uQKovvREJU%2FNUCi1WIecEPD9K3u0L7AiEAp3Y%2FMzo%2FCji4P3rhbrQ1ga16YQMazMVbwcLiCNH%2BHQoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx8yJrba4Lm8NgB%2ByrcA9VRWOVud1cI7N%2FAI8XZ2EdWgP%2FYi3FGQAsB6xezlIVzm3hRLox%2Fv4HmAxEAcBWu1AUpQpxtjZvK%2FDt2buXkEE%2FDJnjVswSM8kprrYVFtTQ6kxQQQ8KpzXzg39eazS%2BwGYaFtZ9Vc26zX5Zxv3gR6OvLcsL7MGIS6OUGwavdjzvy3Qwp1MVta%2F2hfXZZeOmc3BtrjowsT4LeZ8gDW47Q5UTYO3Y9Ofa9PazUMPF7JpTCr09gzLuxIs0RC1SOZFuptRaCYBUe9%2F8UMW3X58OCEuzuqdeayKSCfRRxe37D71CTTSTqxw%2FNhaZwcJ7rgzEijBVRIfMvaI4%2FyLMZO3DxcBoOU44moh2jbItaXdYX2HTQptAsuEKn43xhxM%2FrXbb3Cbm7MjtUnkQwLhzl5WynKp57pnuAPFPNbxwBmr7XMB9gLNW%2BTghPqAqNaUf%2BsEihXU4IPyYQLEWphs7MnjhoXf9nMEem1XiH8dg84tuBk2EPEq75wMC5tCUAPDqn3NvJXbmN0pWoVqG31zSKi1xt4cCmhF2nN5IZLDKTAtyTWZUpwaiYGUZHHKyamM12ly9zfqhuCCJHIDtVKEeCUTimRswqSykJXgs4DbJMe77ZDnd4OBWFtAnDooBVi%2F5kMPPA%2FbwGOqUBHm1se8Y15vLFiyVZXJ4r%2BaP6mzL8FoQLZhyZn%2F%2ByFYV0pVaDFNe92BAzsoG5nD0RVAnA4e%2Fr560HY%2FzxeD%2FV2uFNMC4eof9%2Fewgwq%2BYE4A%2FDMxJfnUF6ByqeSDhwJ7ieyLnir9gt6vDwA8BUnZ5DXe73sxH6qzo9kn3OZJ1%2BoT281Dqrs65E%2Fr4qB%2BplZobhbsTs27UjDHrFbY3w4spaWFloIN4l&X-Amz-Signature=94d2cfe6b5f115d4ad25fbc4eeba3bf7273879f4a70bc238055928311f402878&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REABTWKF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrcBjERooDnw6uQKovvREJU%2FNUCi1WIecEPD9K3u0L7AiEAp3Y%2FMzo%2FCji4P3rhbrQ1ga16YQMazMVbwcLiCNH%2BHQoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx8yJrba4Lm8NgB%2ByrcA9VRWOVud1cI7N%2FAI8XZ2EdWgP%2FYi3FGQAsB6xezlIVzm3hRLox%2Fv4HmAxEAcBWu1AUpQpxtjZvK%2FDt2buXkEE%2FDJnjVswSM8kprrYVFtTQ6kxQQQ8KpzXzg39eazS%2BwGYaFtZ9Vc26zX5Zxv3gR6OvLcsL7MGIS6OUGwavdjzvy3Qwp1MVta%2F2hfXZZeOmc3BtrjowsT4LeZ8gDW47Q5UTYO3Y9Ofa9PazUMPF7JpTCr09gzLuxIs0RC1SOZFuptRaCYBUe9%2F8UMW3X58OCEuzuqdeayKSCfRRxe37D71CTTSTqxw%2FNhaZwcJ7rgzEijBVRIfMvaI4%2FyLMZO3DxcBoOU44moh2jbItaXdYX2HTQptAsuEKn43xhxM%2FrXbb3Cbm7MjtUnkQwLhzl5WynKp57pnuAPFPNbxwBmr7XMB9gLNW%2BTghPqAqNaUf%2BsEihXU4IPyYQLEWphs7MnjhoXf9nMEem1XiH8dg84tuBk2EPEq75wMC5tCUAPDqn3NvJXbmN0pWoVqG31zSKi1xt4cCmhF2nN5IZLDKTAtyTWZUpwaiYGUZHHKyamM12ly9zfqhuCCJHIDtVKEeCUTimRswqSykJXgs4DbJMe77ZDnd4OBWFtAnDooBVi%2F5kMPPA%2FbwGOqUBHm1se8Y15vLFiyVZXJ4r%2BaP6mzL8FoQLZhyZn%2F%2ByFYV0pVaDFNe92BAzsoG5nD0RVAnA4e%2Fr560HY%2FzxeD%2FV2uFNMC4eof9%2Fewgwq%2BYE4A%2FDMxJfnUF6ByqeSDhwJ7ieyLnir9gt6vDwA8BUnZ5DXe73sxH6qzo9kn3OZJ1%2BoT281Dqrs65E%2Fr4qB%2BplZobhbsTs27UjDHrFbY3w4spaWFloIN4l&X-Amz-Signature=1be42e6775af50ecbdbc277b6c2f4d205f12d1b5de787ebcdc7e9ba28aed81b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REABTWKF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrcBjERooDnw6uQKovvREJU%2FNUCi1WIecEPD9K3u0L7AiEAp3Y%2FMzo%2FCji4P3rhbrQ1ga16YQMazMVbwcLiCNH%2BHQoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx8yJrba4Lm8NgB%2ByrcA9VRWOVud1cI7N%2FAI8XZ2EdWgP%2FYi3FGQAsB6xezlIVzm3hRLox%2Fv4HmAxEAcBWu1AUpQpxtjZvK%2FDt2buXkEE%2FDJnjVswSM8kprrYVFtTQ6kxQQQ8KpzXzg39eazS%2BwGYaFtZ9Vc26zX5Zxv3gR6OvLcsL7MGIS6OUGwavdjzvy3Qwp1MVta%2F2hfXZZeOmc3BtrjowsT4LeZ8gDW47Q5UTYO3Y9Ofa9PazUMPF7JpTCr09gzLuxIs0RC1SOZFuptRaCYBUe9%2F8UMW3X58OCEuzuqdeayKSCfRRxe37D71CTTSTqxw%2FNhaZwcJ7rgzEijBVRIfMvaI4%2FyLMZO3DxcBoOU44moh2jbItaXdYX2HTQptAsuEKn43xhxM%2FrXbb3Cbm7MjtUnkQwLhzl5WynKp57pnuAPFPNbxwBmr7XMB9gLNW%2BTghPqAqNaUf%2BsEihXU4IPyYQLEWphs7MnjhoXf9nMEem1XiH8dg84tuBk2EPEq75wMC5tCUAPDqn3NvJXbmN0pWoVqG31zSKi1xt4cCmhF2nN5IZLDKTAtyTWZUpwaiYGUZHHKyamM12ly9zfqhuCCJHIDtVKEeCUTimRswqSykJXgs4DbJMe77ZDnd4OBWFtAnDooBVi%2F5kMPPA%2FbwGOqUBHm1se8Y15vLFiyVZXJ4r%2BaP6mzL8FoQLZhyZn%2F%2ByFYV0pVaDFNe92BAzsoG5nD0RVAnA4e%2Fr560HY%2FzxeD%2FV2uFNMC4eof9%2Fewgwq%2BYE4A%2FDMxJfnUF6ByqeSDhwJ7ieyLnir9gt6vDwA8BUnZ5DXe73sxH6qzo9kn3OZJ1%2BoT281Dqrs65E%2Fr4qB%2BplZobhbsTs27UjDHrFbY3w4spaWFloIN4l&X-Amz-Signature=419209f36455a696864a0ddd271d4b4186c3a9205f826b0e408ed3087288007d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REABTWKF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrcBjERooDnw6uQKovvREJU%2FNUCi1WIecEPD9K3u0L7AiEAp3Y%2FMzo%2FCji4P3rhbrQ1ga16YQMazMVbwcLiCNH%2BHQoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx8yJrba4Lm8NgB%2ByrcA9VRWOVud1cI7N%2FAI8XZ2EdWgP%2FYi3FGQAsB6xezlIVzm3hRLox%2Fv4HmAxEAcBWu1AUpQpxtjZvK%2FDt2buXkEE%2FDJnjVswSM8kprrYVFtTQ6kxQQQ8KpzXzg39eazS%2BwGYaFtZ9Vc26zX5Zxv3gR6OvLcsL7MGIS6OUGwavdjzvy3Qwp1MVta%2F2hfXZZeOmc3BtrjowsT4LeZ8gDW47Q5UTYO3Y9Ofa9PazUMPF7JpTCr09gzLuxIs0RC1SOZFuptRaCYBUe9%2F8UMW3X58OCEuzuqdeayKSCfRRxe37D71CTTSTqxw%2FNhaZwcJ7rgzEijBVRIfMvaI4%2FyLMZO3DxcBoOU44moh2jbItaXdYX2HTQptAsuEKn43xhxM%2FrXbb3Cbm7MjtUnkQwLhzl5WynKp57pnuAPFPNbxwBmr7XMB9gLNW%2BTghPqAqNaUf%2BsEihXU4IPyYQLEWphs7MnjhoXf9nMEem1XiH8dg84tuBk2EPEq75wMC5tCUAPDqn3NvJXbmN0pWoVqG31zSKi1xt4cCmhF2nN5IZLDKTAtyTWZUpwaiYGUZHHKyamM12ly9zfqhuCCJHIDtVKEeCUTimRswqSykJXgs4DbJMe77ZDnd4OBWFtAnDooBVi%2F5kMPPA%2FbwGOqUBHm1se8Y15vLFiyVZXJ4r%2BaP6mzL8FoQLZhyZn%2F%2ByFYV0pVaDFNe92BAzsoG5nD0RVAnA4e%2Fr560HY%2FzxeD%2FV2uFNMC4eof9%2Fewgwq%2BYE4A%2FDMxJfnUF6ByqeSDhwJ7ieyLnir9gt6vDwA8BUnZ5DXe73sxH6qzo9kn3OZJ1%2BoT281Dqrs65E%2Fr4qB%2BplZobhbsTs27UjDHrFbY3w4spaWFloIN4l&X-Amz-Signature=06144b240b4a0499fee37a7b8125e8ac4762c93994b20c9e9ed3bcbc906d16fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REABTWKF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrcBjERooDnw6uQKovvREJU%2FNUCi1WIecEPD9K3u0L7AiEAp3Y%2FMzo%2FCji4P3rhbrQ1ga16YQMazMVbwcLiCNH%2BHQoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx8yJrba4Lm8NgB%2ByrcA9VRWOVud1cI7N%2FAI8XZ2EdWgP%2FYi3FGQAsB6xezlIVzm3hRLox%2Fv4HmAxEAcBWu1AUpQpxtjZvK%2FDt2buXkEE%2FDJnjVswSM8kprrYVFtTQ6kxQQQ8KpzXzg39eazS%2BwGYaFtZ9Vc26zX5Zxv3gR6OvLcsL7MGIS6OUGwavdjzvy3Qwp1MVta%2F2hfXZZeOmc3BtrjowsT4LeZ8gDW47Q5UTYO3Y9Ofa9PazUMPF7JpTCr09gzLuxIs0RC1SOZFuptRaCYBUe9%2F8UMW3X58OCEuzuqdeayKSCfRRxe37D71CTTSTqxw%2FNhaZwcJ7rgzEijBVRIfMvaI4%2FyLMZO3DxcBoOU44moh2jbItaXdYX2HTQptAsuEKn43xhxM%2FrXbb3Cbm7MjtUnkQwLhzl5WynKp57pnuAPFPNbxwBmr7XMB9gLNW%2BTghPqAqNaUf%2BsEihXU4IPyYQLEWphs7MnjhoXf9nMEem1XiH8dg84tuBk2EPEq75wMC5tCUAPDqn3NvJXbmN0pWoVqG31zSKi1xt4cCmhF2nN5IZLDKTAtyTWZUpwaiYGUZHHKyamM12ly9zfqhuCCJHIDtVKEeCUTimRswqSykJXgs4DbJMe77ZDnd4OBWFtAnDooBVi%2F5kMPPA%2FbwGOqUBHm1se8Y15vLFiyVZXJ4r%2BaP6mzL8FoQLZhyZn%2F%2ByFYV0pVaDFNe92BAzsoG5nD0RVAnA4e%2Fr560HY%2FzxeD%2FV2uFNMC4eof9%2Fewgwq%2BYE4A%2FDMxJfnUF6ByqeSDhwJ7ieyLnir9gt6vDwA8BUnZ5DXe73sxH6qzo9kn3OZJ1%2BoT281Dqrs65E%2Fr4qB%2BplZobhbsTs27UjDHrFbY3w4spaWFloIN4l&X-Amz-Signature=162814122e266d77e23176afd32c9de36174b9cd5359e51f89a48ee9f41ef3d9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPUF3WEX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkvpPj1z4coW59V2L3NXyDaYPf2VcRzAriEk6FrG2drAIhAJpkHQHD2f2RgqhTNN%2FAk%2FOlefhcPHJ%2BDV9RvWuJN9tjKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz1br17YHJGq%2BD6F2Qq3AN33AG3OAJIPl9UrYxYXZCBHuT1ZD%2FLRO3pVPHXYxlmfxEZgRt6fzudRE4u2JGdsK9wDZaBxQ4ojbhFMIpmOEdcGCU2l8RDSS091RI7VoqHocKsru47VRxL%2B1AdnWJAXduZTJ93Z3Mu8VdxooN59Z8Y9%2FdapRBerQqhYa1kzj7hhItA7T%2Fw3lpBpN00X6DuOZ3vyWIsJ1rY8noz%2BcsHxCHU5fnpe3KDM5wdd8Lc08PxKKe%2FPWizAO42yEQZyA8kLoQgqOTTuSLPdMHx4hziD8kL4UfsvPYdjgBi2aqkwFzwr82aOPII3xAq7OONNjoFCfMeFwn02gMO3OsQ5GSqdYOVor%2FvJr%2Bn2OkNy7thZdqF3DXVErxgvYsZXxKQKb5Pq3P822mUhJC5suDdiDotH%2BbhmNwM%2FIHnQRweTtq%2BVTEKEZh4GwL0V%2FUFq959Ja9cuOkR%2Fs9JhJa0JWBWzbTLTeT2zErrEivag%2FTVTwcHf3apEn8C7HMNpFCz4dXXxBiGrwfyknw7X%2FalrhyWn%2BoVtP8Jp9yY1VwKsKHtj4AnRLPRXe4PfZB2IxrLIqO6%2FdtfhMs4HqQrKpDb%2BD42Ge8BAZlHK06Ex7M79xvE3%2FOF6z1FyWbGTMpesNS3XKMAWTDXvf28BjqkAfLNVyjmWhrwZJnJQVmIbKDrppcISGfhXlSTWKzW77Q8xPu%2FgLzqHFE0IOSVc9fxUOD2pKg3XSWMDiNqGl4j3JTyu%2Bh85%2BIUTxfr5J%2F8syPCv5wJ39vCz3JGixQJd04QissE%2FNZPNDX9lVkiW2wb5JiM2afvzDlr1RNPNjf44vQYmm9cou7hwdNA6o04cKEYCZqUt1ib%2B0yv0p5CYZio%2FG9pUlDn&X-Amz-Signature=0ad9a6e45b00876fca60e4921c6bda69bc83314e35caf785cd8f7f3ce1c17e00&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD3KQV46%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBR26IycBOWZRHWz3onMrjZIwdwNHgZh2YqyVcQvR5zsAiBalzVCtufXYvNx1DkrMn60SxIhrreRpXMw8V057hSI4yqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM810tp65975n3rJg9KtwDPr59t3%2B3A%2FDBIqIwLVvJPIg%2Fg9CNvPIBl%2FXhGeOmVAReJYDL3taeul4MjiHK4eKzZpmfmX8Jq52lOpByo%2Fqv0VroXEJs52FUTiZBtwbL5UpegMrY8AzAmgXWRAb5BSxWo4cwHDl53XmrlkmZJYAdxlrJMuyIGrlY54T%2BAtN7IE3MG9s7mvRW5GU8CoegzCkYWD6pERbS9TejLAW8p5c7HHxwYVZGkzRnC5jNsjNOHwNsi3Q8O%2Fs65q%2FuPdGae77mje7qggBubbHcpEWf9A%2F%2F%2Bzk976utsdkTzRPcH3nOi2chwGWotpYrY28XQp9I%2BykES%2BXWVUfseg56l8Bl9foby1qduU6DervAU64OGYf%2FvyNPz%2B%2B0663HIoq9VeCPrAEWV5B3YWT7uR4fccrio1JnFAjbfAFeeHn1b8OPGNvuk%2BhyCdt%2FaC7kvgGZfPZ0qSP2h8stxzyYGWdyvPWuuCylHbGpp4BW34JH6U%2Bu8Dt81HnX6ExSOqTqp%2By%2Fwy%2BddftoWaankvzmBTY6eIEXxboUbdDhWcjPHOK25d8SuGJ7FsOvfPe5IgSs9NMm1xsZ21G3ZKmGnvqqTUWH%2F3H19x81FXNvo5ZBpRLhpjTQNC18DevahQJAxuuI2%2BmjBnswicL9vAY6pgHOnF%2FlC%2B7aXmwJtiqcbfKF3xyPzXWw8UmwHigzIT2KYN%2Fb%2Fb7RtwpPxwBOwqbiGRt7BU9h5JZG3nTYhcZvxgMvZCfh2iPiKOvdRgJvP9mseEmJzIf8UtBjkm3z%2FJpKz8aKkHJ4PEVrck4R9JLDB6ifwbnXltY0U43bKL4f9tW5pbmXnhWqmzTx1Zi65m85X8ICnYm1tiSGd%2FOcnx6fbNGXVgRsjUsQ&X-Amz-Signature=52a3e835ea3df7b0e4667934529420cc407b8516e928bdb5d5c2fd7a4303631a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REABTWKF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrcBjERooDnw6uQKovvREJU%2FNUCi1WIecEPD9K3u0L7AiEAp3Y%2FMzo%2FCji4P3rhbrQ1ga16YQMazMVbwcLiCNH%2BHQoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx8yJrba4Lm8NgB%2ByrcA9VRWOVud1cI7N%2FAI8XZ2EdWgP%2FYi3FGQAsB6xezlIVzm3hRLox%2Fv4HmAxEAcBWu1AUpQpxtjZvK%2FDt2buXkEE%2FDJnjVswSM8kprrYVFtTQ6kxQQQ8KpzXzg39eazS%2BwGYaFtZ9Vc26zX5Zxv3gR6OvLcsL7MGIS6OUGwavdjzvy3Qwp1MVta%2F2hfXZZeOmc3BtrjowsT4LeZ8gDW47Q5UTYO3Y9Ofa9PazUMPF7JpTCr09gzLuxIs0RC1SOZFuptRaCYBUe9%2F8UMW3X58OCEuzuqdeayKSCfRRxe37D71CTTSTqxw%2FNhaZwcJ7rgzEijBVRIfMvaI4%2FyLMZO3DxcBoOU44moh2jbItaXdYX2HTQptAsuEKn43xhxM%2FrXbb3Cbm7MjtUnkQwLhzl5WynKp57pnuAPFPNbxwBmr7XMB9gLNW%2BTghPqAqNaUf%2BsEihXU4IPyYQLEWphs7MnjhoXf9nMEem1XiH8dg84tuBk2EPEq75wMC5tCUAPDqn3NvJXbmN0pWoVqG31zSKi1xt4cCmhF2nN5IZLDKTAtyTWZUpwaiYGUZHHKyamM12ly9zfqhuCCJHIDtVKEeCUTimRswqSykJXgs4DbJMe77ZDnd4OBWFtAnDooBVi%2F5kMPPA%2FbwGOqUBHm1se8Y15vLFiyVZXJ4r%2BaP6mzL8FoQLZhyZn%2F%2ByFYV0pVaDFNe92BAzsoG5nD0RVAnA4e%2Fr560HY%2FzxeD%2FV2uFNMC4eof9%2Fewgwq%2BYE4A%2FDMxJfnUF6ByqeSDhwJ7ieyLnir9gt6vDwA8BUnZ5DXe73sxH6qzo9kn3OZJ1%2BoT281Dqrs65E%2Fr4qB%2BplZobhbsTs27UjDHrFbY3w4spaWFloIN4l&X-Amz-Signature=c6fc687e43f423faa5c0d6de098d58c7f52f5d1616713a71eb12a3a0c4e86a1d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REABTWKF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrcBjERooDnw6uQKovvREJU%2FNUCi1WIecEPD9K3u0L7AiEAp3Y%2FMzo%2FCji4P3rhbrQ1ga16YQMazMVbwcLiCNH%2BHQoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx8yJrba4Lm8NgB%2ByrcA9VRWOVud1cI7N%2FAI8XZ2EdWgP%2FYi3FGQAsB6xezlIVzm3hRLox%2Fv4HmAxEAcBWu1AUpQpxtjZvK%2FDt2buXkEE%2FDJnjVswSM8kprrYVFtTQ6kxQQQ8KpzXzg39eazS%2BwGYaFtZ9Vc26zX5Zxv3gR6OvLcsL7MGIS6OUGwavdjzvy3Qwp1MVta%2F2hfXZZeOmc3BtrjowsT4LeZ8gDW47Q5UTYO3Y9Ofa9PazUMPF7JpTCr09gzLuxIs0RC1SOZFuptRaCYBUe9%2F8UMW3X58OCEuzuqdeayKSCfRRxe37D71CTTSTqxw%2FNhaZwcJ7rgzEijBVRIfMvaI4%2FyLMZO3DxcBoOU44moh2jbItaXdYX2HTQptAsuEKn43xhxM%2FrXbb3Cbm7MjtUnkQwLhzl5WynKp57pnuAPFPNbxwBmr7XMB9gLNW%2BTghPqAqNaUf%2BsEihXU4IPyYQLEWphs7MnjhoXf9nMEem1XiH8dg84tuBk2EPEq75wMC5tCUAPDqn3NvJXbmN0pWoVqG31zSKi1xt4cCmhF2nN5IZLDKTAtyTWZUpwaiYGUZHHKyamM12ly9zfqhuCCJHIDtVKEeCUTimRswqSykJXgs4DbJMe77ZDnd4OBWFtAnDooBVi%2F5kMPPA%2FbwGOqUBHm1se8Y15vLFiyVZXJ4r%2BaP6mzL8FoQLZhyZn%2F%2ByFYV0pVaDFNe92BAzsoG5nD0RVAnA4e%2Fr560HY%2FzxeD%2FV2uFNMC4eof9%2Fewgwq%2BYE4A%2FDMxJfnUF6ByqeSDhwJ7ieyLnir9gt6vDwA8BUnZ5DXe73sxH6qzo9kn3OZJ1%2BoT281Dqrs65E%2Fr4qB%2BplZobhbsTs27UjDHrFbY3w4spaWFloIN4l&X-Amz-Signature=b68b696007dcd199e2fef7a242371bf0d561c8c0dbbdab6c985f19d07d580352&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REABTWKF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrcBjERooDnw6uQKovvREJU%2FNUCi1WIecEPD9K3u0L7AiEAp3Y%2FMzo%2FCji4P3rhbrQ1ga16YQMazMVbwcLiCNH%2BHQoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx8yJrba4Lm8NgB%2ByrcA9VRWOVud1cI7N%2FAI8XZ2EdWgP%2FYi3FGQAsB6xezlIVzm3hRLox%2Fv4HmAxEAcBWu1AUpQpxtjZvK%2FDt2buXkEE%2FDJnjVswSM8kprrYVFtTQ6kxQQQ8KpzXzg39eazS%2BwGYaFtZ9Vc26zX5Zxv3gR6OvLcsL7MGIS6OUGwavdjzvy3Qwp1MVta%2F2hfXZZeOmc3BtrjowsT4LeZ8gDW47Q5UTYO3Y9Ofa9PazUMPF7JpTCr09gzLuxIs0RC1SOZFuptRaCYBUe9%2F8UMW3X58OCEuzuqdeayKSCfRRxe37D71CTTSTqxw%2FNhaZwcJ7rgzEijBVRIfMvaI4%2FyLMZO3DxcBoOU44moh2jbItaXdYX2HTQptAsuEKn43xhxM%2FrXbb3Cbm7MjtUnkQwLhzl5WynKp57pnuAPFPNbxwBmr7XMB9gLNW%2BTghPqAqNaUf%2BsEihXU4IPyYQLEWphs7MnjhoXf9nMEem1XiH8dg84tuBk2EPEq75wMC5tCUAPDqn3NvJXbmN0pWoVqG31zSKi1xt4cCmhF2nN5IZLDKTAtyTWZUpwaiYGUZHHKyamM12ly9zfqhuCCJHIDtVKEeCUTimRswqSykJXgs4DbJMe77ZDnd4OBWFtAnDooBVi%2F5kMPPA%2FbwGOqUBHm1se8Y15vLFiyVZXJ4r%2BaP6mzL8FoQLZhyZn%2F%2ByFYV0pVaDFNe92BAzsoG5nD0RVAnA4e%2Fr560HY%2FzxeD%2FV2uFNMC4eof9%2Fewgwq%2BYE4A%2FDMxJfnUF6ByqeSDhwJ7ieyLnir9gt6vDwA8BUnZ5DXe73sxH6qzo9kn3OZJ1%2BoT281Dqrs65E%2Fr4qB%2BplZobhbsTs27UjDHrFbY3w4spaWFloIN4l&X-Amz-Signature=4b80adc8233405236338a864ec55d678b5feab87266be54075e8f0af8734c28e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLS7KHQN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEywsoLHvIVlKItfru7tU5NzJw1OXPpKK9lDNWiEDLgoAiEA0%2BMPsm%2BjLuJTwvCv2kh63lNLGIb6adrB2OidmUHf1MUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCZ89sM2lp4RjwzpMSrcA9gtC%2F4W7naRorHFxi2auzJL3Fj2Ks3PbSvFr7z3fV9SvFccDWgd8%2Bti9nlXUNrsbKLdZ6ow9DQ9QMGlY%2BLPhk1sJzmaMCGStE%2FIJLsengL6ErD1p65dJbH0ikIP9FLmoBA5pJCfY8afzcxztC4DTMNi8%2FnRtVvyPTRRck3ulgXhgjHZs%2FF57NLYFaeMicH51yyiMm%2BT5fD4riZxE9GunbiPM877lxHPjZ%2BSsuH9%2BXrnFMwln13%2Frb6XUhVPF5avDIpcEXFhx5SDKJxjyNg88UT%2BTc7X2eSIp0DgnWGv4ihK8w5tlf7Uu3PqgTg6PBHqUM4ZxBBOAuFPtwMVzbkLH2AzaqZw6ABucpc42crPwbUZe4sT%2B70KNvfOS2lf1CSRSTuhC9Ot7%2F5FW%2FKw1G532ikIHDpNMy21o%2BLwIrPSsAACFn3BfdMUZF9UOyuxlxghVfUBx5I3QwihGGdSdZeJ5jkxXds2Lo82reZ7oGjYZqzx75dH1Qu7Va1LWjHGlKBf40zmVqwx95EaNvOmk%2FB4HyTLEZsleKiBNQHuiwuXcnovljmky41lJTLtP4LQLhB%2F9fNBmEwMEWugZxviUVY8CTn7hiLnMRrp6L9YJmrRp%2FoKSuZvVjNbWR52BmtDMKW7%2FbwGOqUBdHmwcRQi9nxwSNgCRQgj40pHqxlyl1NxPMVm3fBdTskRNSeW9yrmWqQmr%2FJR%2B2xdxgUYkVJdqxMxvrtDUV9VWsxenvOtv%2F7axrs%2BLoUaivStm%2FNJIDEDnZYILo26po75XBjfcjo0MeVTZe3Mh%2Bq5l1krAixhbYZ7JzDWq4a3tvkbKjjDqBdgLal2uuSeG7EPw7caCZ5%2F3GNiparpTrIBPC5C%2BeS%2B&X-Amz-Signature=5cf429b0945f433206d3c51303ac4534d497febbfcbfce60643ff7a5558bb166&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G6G73V5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkB3yII2rM8%2FG9hI%2FR%2BqL3frv81xYfO0Td1WJ2oH%2FfLQIgJgZ5RuwYBVRZLUP0orHzbyq9WmSfxbsH61Y1uOpRU98qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPNStWnxN92PoeYaeSrcA3OROr9nu6CyI3AX1XhkOO1yb3Buu1xANWnpdLxAXvM1wqf7FRbRc66%2FUQC6SMh8409rc8wMYD0ZvD%2B0THkEYwvrW9ti8%2BZD33k%2Br9UnGUhdCTzCyPUdMhfEv67KOQ%2FsRmtlswZKJ2IOYL1vgaRJDbqo7Ku7KxX1mU2QqxdIRIh9nyErzh9yJxrVZ2JwC5dgTqXyb1mr4kRNlruSeShyFRmgQRGluRPmFNsBiq%2BXLCYnR0HjRnCyWtARM18KtNQcTs1ul6U%2FVh%2F55qMqtfZuX5GJNHbmyo5br8MlzbjrhY3Y%2BDnEbR%2B5Q60Y%2BUPolE%2F3uVw8BKqZjDAyDxzNdtLQrrMlK5EVMrmUx7PLuhiE9lGrIoQ5z89mKsQ4XHgGTu9J4ELBh9ROSOKhRGa08Ki%2FZ4%2BMUBuNXwqjQtOwyv06HC57qdlTvxCJol%2FJUbjaS0R1pITseQ1VJQSLvSR4xIsZmkfa4XaQxLP%2FM0q6%2FkYl%2BryDuVD%2Bz4te0RADE4TJdkSYQwmOMpsExBfUD9cOBajLoUjweHYbf07cPRFMHQOzwBiYdJ3Ru0F3yq%2FeaSK41a2xkfUDmG8NZ7lnufFwRErRi0M%2FhnWuCc5ctALNvAFH4b8mmRKij5D1OvbsAwCSMOO4%2FbwGOqUBao93ljqyQ2s1IgHtVcTDLwgqlcf8VRimch5I%2FSDisLWwMhxyt41BAek2AWXz3C5PLoWM%2B8e4jbhAXwr9sMG4LoyudqbhwCqTxnVxPW5DPjawt3bOZOV%2BYwA%2Bx%2FmdsKlGFfAcDmIu2FgAewTHEfPFyR3fYYDoGiJirrNn2iaxtEqxRttUvUjnhoJ%2F2v6lqIjg9brJm7jbRQWUpbr5%2FrMYLiO1qGAS&X-Amz-Signature=9b0134cc28e5676468877bc5bf21e4c5b10c3e7c1647c5511e80cf83339e79b4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662POJVDFK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeTODrWY%2BcT0e9oC9I1dhCpFdXEgKZS2BSXP3%2FdoKaggIgbKPCv%2Bb5TfqTAFtqtPC4LPd79rOI9aJVqwLXA%2Fmzh20qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJjFYcwR545%2BZku2myrcA873G0mCN2OMk3rxzJvDguOoE3pBH5ZA89x6hRFUJsfQkTwqIMxWRI3H6wRjTQ6Owwwqr0Mx3yIE8qngk0suW5ECL%2BSPUA3IO%2F248ZxAkFtbZffRp6Q3bwA9VfrjpI1pbR9SuGqkkliZcTDZXCNA2O4LG8JYEIpD0ntbSLV1HTkpr3JNdeBzd1LGaTJ4TI23iUyimYV0B8%2Fp7fP5CQFqztp8Xx207EgaQ2SOPMTSQ%2FEbGOySCtvQUE2%2F4hNU8uH1fXid0CQ5pbHI5u4ExitY2FC7WeawXcM%2FGgBdBUn1BgTWnO51vi%2FC9S3PQcHkrSeS5%2F9zeBOVhjBuzKMuBbGyneIMfh10oQgwp16e8Sr63fbR%2Ben9Z4GBNnySnpRrF0T6uwI32k8OR55WPtdGFLJLZNibZpqsrAHmzO06DkdUz3KtQNtdHsIDGLSAN6LDy2Beu2N0Td0ThjethBQ%2BB0RbmE0UKGaxxTtrQs%2BH6C%2Bg94%2BkIdJzgQg5DOBoasmP2KTqux58Ytj5%2Bm19riKGiIoihv9v%2BFNhcEHOwTCDG%2FvlVRxVvQCQ18uhHiE6BtopL0g6g1MpFp4mJ5ISMMIKzshAAdHjCOBafM%2F2tRky2pRDD4LavDYNxgbAJCP5zxp5MMrC%2FbwGOqUBT1aZxqN6cKicGJs%2BP44TPwGkC3038c0taZqqYH%2BuuxdtV5kjjHl%2Bly6y60ADPqbC%2Fy7Ucljv76IH6misxxEbxr7Yr1i5Tb7wiPYK8IX2NDguvWj1y%2Ba%2BlDtOD8Txzc%2Fa31pa%2F7nWeOfCBoJQlbR0e8AbsDAnCacKnqdhmHiG9Ee2dDeqtl0LHEb7yxf7zt5UX7zonnPJf0DwGofUZgd4FuGCfTy4&X-Amz-Signature=3f1c5356cfde874932b01d25356cba69016525854b447d298e25f9d8406410df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V52NFQC2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFJdnkynl8RVxhSPZPVRc44Yw2EKIuyUgKK5z%2Fr96673AiALh60%2BvzassH0WhICUE%2FM2gwUI8Ahai%2FfW8jSTsAg%2FbCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtAXG2lQmFnjG7DnNKtwDSxPDOaIiEwxznGL4EUCT5rIyAAeGywFNEpu4kh%2FsHAKOqE%2BlByJ76RyyjYQu1De5WXYHKWVB9LCutona4TZonYo6U8B5NnZaM1JSSKiM%2Fi6zaMYbCfq2hbfXieeOMjQATDy3BS%2BR7LuRJbhu1NlE%2FPR1knQE5tnvKO0HbEE2WuuIBvSmXxXQyCu1l%2BufOiNDlN%2FXwaMZBYxdA%2BZqt07zCn%2BM4EcrnNRN0eQMtuHjjqtfkQ1AVKd3OoqjFwOwT%2B9DJnlePeh5SIbJY8nk6Eh6QDLAJDGk%2BdKhl95Ak%2BsRx5w3LAKSPb4scSKzY0IBJdanUEDpLp%2FgkiMDU8wXK6VRPFodHqrsw%2B14qFFNdrthoz3PZGYyLMfv%2B3buoarqZqjo%2FgFqeuVl4fZ7TP3feviFBajJhYZWv6zfWcDjpH1247T44efc2bJgt69McrNW4syWU3Aw6f3B9EB7vb7Ag%2FdDxLpFFeJnJGK%2FxUI3T29jL5up7fN47nZfstPvjOSC7dd8%2B%2FRpm6%2F378up0MpNj%2B%2BHBhStL5JZnWtNJOwxmKTQGFwC%2BduH0N9IWx%2BzF%2Fk%2Fr3AK1wjKgACW8rn8JC6kcyU9kjaXyPQKN0nJnk7g4F0aL2OAaXNi9J4RXQj08kcwtsL9vAY6pgGsbSHfRo6KH%2FrDrucXEbKA40M2i6uUzLmJN6HGCskUIVAPIX2unEYbyDNZsaLEVSh8lrdxgeGTjT55Dl1tum%2F94r2AnxlxPhJbVT%2FYuvMtr%2FHwE1vSRSIp3w%2FTrUHZtXJFAOZZ56jvQu5QPQ7qHGgcV6HsoeW3IGfE3a0JSWhdXThOy%2BWfrU5lADiU7nD5EttQciDvk8xSBzFM4K8P0RkWFjv73%2BfJ&X-Amz-Signature=286f8f7fcd4303f1271563d257b0accbab6bb8054ccdced2de9947c34767ffb1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V52NFQC2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFJdnkynl8RVxhSPZPVRc44Yw2EKIuyUgKK5z%2Fr96673AiALh60%2BvzassH0WhICUE%2FM2gwUI8Ahai%2FfW8jSTsAg%2FbCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtAXG2lQmFnjG7DnNKtwDSxPDOaIiEwxznGL4EUCT5rIyAAeGywFNEpu4kh%2FsHAKOqE%2BlByJ76RyyjYQu1De5WXYHKWVB9LCutona4TZonYo6U8B5NnZaM1JSSKiM%2Fi6zaMYbCfq2hbfXieeOMjQATDy3BS%2BR7LuRJbhu1NlE%2FPR1knQE5tnvKO0HbEE2WuuIBvSmXxXQyCu1l%2BufOiNDlN%2FXwaMZBYxdA%2BZqt07zCn%2BM4EcrnNRN0eQMtuHjjqtfkQ1AVKd3OoqjFwOwT%2B9DJnlePeh5SIbJY8nk6Eh6QDLAJDGk%2BdKhl95Ak%2BsRx5w3LAKSPb4scSKzY0IBJdanUEDpLp%2FgkiMDU8wXK6VRPFodHqrsw%2B14qFFNdrthoz3PZGYyLMfv%2B3buoarqZqjo%2FgFqeuVl4fZ7TP3feviFBajJhYZWv6zfWcDjpH1247T44efc2bJgt69McrNW4syWU3Aw6f3B9EB7vb7Ag%2FdDxLpFFeJnJGK%2FxUI3T29jL5up7fN47nZfstPvjOSC7dd8%2B%2FRpm6%2F378up0MpNj%2B%2BHBhStL5JZnWtNJOwxmKTQGFwC%2BduH0N9IWx%2BzF%2Fk%2Fr3AK1wjKgACW8rn8JC6kcyU9kjaXyPQKN0nJnk7g4F0aL2OAaXNi9J4RXQj08kcwtsL9vAY6pgGsbSHfRo6KH%2FrDrucXEbKA40M2i6uUzLmJN6HGCskUIVAPIX2unEYbyDNZsaLEVSh8lrdxgeGTjT55Dl1tum%2F94r2AnxlxPhJbVT%2FYuvMtr%2FHwE1vSRSIp3w%2FTrUHZtXJFAOZZ56jvQu5QPQ7qHGgcV6HsoeW3IGfE3a0JSWhdXThOy%2BWfrU5lADiU7nD5EttQciDvk8xSBzFM4K8P0RkWFjv73%2BfJ&X-Amz-Signature=642f0693411648acadfae6b4273b5c0c3ebcd7b47825aa03981b949dfd507731&X-Amz-SignedHeaders=host&x-id=GetObject)

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
