

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWO5CH2P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIGnk5KBpb8uAm6FMeh6W6v89YDrF02E6%2FvUxfFJWAWdCAiEAtHVkuy8VkBe2ApQa9wtJUSHhnqrSfEg%2FNPuvNGNuuyoq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDLIan0SGiI5v%2FTWL2yrcA3TUP0ag0PlzDUZpyZALs3MpaRpfpWdm0uQcIwlaZEBkPvP2pVouxwvAe57ii7RHxtpCePiziPAjBHfAvsEZBAiTV%2FpzES%2Bpf6xI9A2YE5xaE2ddIEkqqxQSZu70rHBp0fOpsO%2F2oKeAXUUOioW2PMVotFBgpL25LbrncmhhvpzTCmabilrnKcn7qSVfW76QLp45ffHb5IQJAX5OVo6gcbQgLpcB8hCj95Ds%2FQDbbhyU9%2Bqkc4hBHKVYCecVr2lRBFawOCCMjIwNy1GwBaobpWiVK0rZjpI81a9Eo9gMhK08W%2BHqkgOie9CzbB10vn9Ho5sSfTqwAvYM6VO6bu8M2x54y9Q%2FkOvxLjR2XyiU40U3FFqkmJgLM%2FjfRMF9GiVCh2NtH0J5U1UH9HrAMoxEnPB2e5GeFFwEc6jT0C79Sd5JgLrarLuG8OzlW8HTQF1yFn29Zp%2FL3nCJ2qGwCLi%2F0YL1oFQMhUGWi40hSiqhZBCrn4kHswJHygItDE7iBxfTTVXpAOV3YPID%2F6Bwp3qRi%2BUcSG3E9NDvJ3R4ZPacUJZjLI2s4%2FZvMt%2F5MOsrqNyOJAy%2FN9NtPXzrvvzmCWsNpTlV6FWs18sD9RU1i2PcLnj0ot3rXbMiYrD2qHP1MMTSk70GOqUBPuWfsujOMWnbYHjcG%2BeauZwkEf4A2PkscfPwP7bvhPVgy9gYzbuoiWHUOfpM14SfreQs6lhCJmKeu2Ftg%2BPoxLYiQphSlvZ4%2FQ5TO9HldMSG5R32JDXDihYn6fI%2FhKl2L1EzyczaTqQ4BejUfwsQAwMobMuKk6ZYB2%2FRiocvS8kv6kh%2BP3x3Sa2zGs6MCB7DBYtEQ2pz29o04zfyEIFqkAMJOcYz&X-Amz-Signature=bfb250ed8a9ebca8fa36348ed9ee8fa94d665c7e460abca031d765bc74a6c1ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWO5CH2P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIGnk5KBpb8uAm6FMeh6W6v89YDrF02E6%2FvUxfFJWAWdCAiEAtHVkuy8VkBe2ApQa9wtJUSHhnqrSfEg%2FNPuvNGNuuyoq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDLIan0SGiI5v%2FTWL2yrcA3TUP0ag0PlzDUZpyZALs3MpaRpfpWdm0uQcIwlaZEBkPvP2pVouxwvAe57ii7RHxtpCePiziPAjBHfAvsEZBAiTV%2FpzES%2Bpf6xI9A2YE5xaE2ddIEkqqxQSZu70rHBp0fOpsO%2F2oKeAXUUOioW2PMVotFBgpL25LbrncmhhvpzTCmabilrnKcn7qSVfW76QLp45ffHb5IQJAX5OVo6gcbQgLpcB8hCj95Ds%2FQDbbhyU9%2Bqkc4hBHKVYCecVr2lRBFawOCCMjIwNy1GwBaobpWiVK0rZjpI81a9Eo9gMhK08W%2BHqkgOie9CzbB10vn9Ho5sSfTqwAvYM6VO6bu8M2x54y9Q%2FkOvxLjR2XyiU40U3FFqkmJgLM%2FjfRMF9GiVCh2NtH0J5U1UH9HrAMoxEnPB2e5GeFFwEc6jT0C79Sd5JgLrarLuG8OzlW8HTQF1yFn29Zp%2FL3nCJ2qGwCLi%2F0YL1oFQMhUGWi40hSiqhZBCrn4kHswJHygItDE7iBxfTTVXpAOV3YPID%2F6Bwp3qRi%2BUcSG3E9NDvJ3R4ZPacUJZjLI2s4%2FZvMt%2F5MOsrqNyOJAy%2FN9NtPXzrvvzmCWsNpTlV6FWs18sD9RU1i2PcLnj0ot3rXbMiYrD2qHP1MMTSk70GOqUBPuWfsujOMWnbYHjcG%2BeauZwkEf4A2PkscfPwP7bvhPVgy9gYzbuoiWHUOfpM14SfreQs6lhCJmKeu2Ftg%2BPoxLYiQphSlvZ4%2FQ5TO9HldMSG5R32JDXDihYn6fI%2FhKl2L1EzyczaTqQ4BejUfwsQAwMobMuKk6ZYB2%2FRiocvS8kv6kh%2BP3x3Sa2zGs6MCB7DBYtEQ2pz29o04zfyEIFqkAMJOcYz&X-Amz-Signature=c37d75bfcc16aa736c762e823ffb1eccda6299f9249f8588b3a9b180d39420dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWO5CH2P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIGnk5KBpb8uAm6FMeh6W6v89YDrF02E6%2FvUxfFJWAWdCAiEAtHVkuy8VkBe2ApQa9wtJUSHhnqrSfEg%2FNPuvNGNuuyoq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDLIan0SGiI5v%2FTWL2yrcA3TUP0ag0PlzDUZpyZALs3MpaRpfpWdm0uQcIwlaZEBkPvP2pVouxwvAe57ii7RHxtpCePiziPAjBHfAvsEZBAiTV%2FpzES%2Bpf6xI9A2YE5xaE2ddIEkqqxQSZu70rHBp0fOpsO%2F2oKeAXUUOioW2PMVotFBgpL25LbrncmhhvpzTCmabilrnKcn7qSVfW76QLp45ffHb5IQJAX5OVo6gcbQgLpcB8hCj95Ds%2FQDbbhyU9%2Bqkc4hBHKVYCecVr2lRBFawOCCMjIwNy1GwBaobpWiVK0rZjpI81a9Eo9gMhK08W%2BHqkgOie9CzbB10vn9Ho5sSfTqwAvYM6VO6bu8M2x54y9Q%2FkOvxLjR2XyiU40U3FFqkmJgLM%2FjfRMF9GiVCh2NtH0J5U1UH9HrAMoxEnPB2e5GeFFwEc6jT0C79Sd5JgLrarLuG8OzlW8HTQF1yFn29Zp%2FL3nCJ2qGwCLi%2F0YL1oFQMhUGWi40hSiqhZBCrn4kHswJHygItDE7iBxfTTVXpAOV3YPID%2F6Bwp3qRi%2BUcSG3E9NDvJ3R4ZPacUJZjLI2s4%2FZvMt%2F5MOsrqNyOJAy%2FN9NtPXzrvvzmCWsNpTlV6FWs18sD9RU1i2PcLnj0ot3rXbMiYrD2qHP1MMTSk70GOqUBPuWfsujOMWnbYHjcG%2BeauZwkEf4A2PkscfPwP7bvhPVgy9gYzbuoiWHUOfpM14SfreQs6lhCJmKeu2Ftg%2BPoxLYiQphSlvZ4%2FQ5TO9HldMSG5R32JDXDihYn6fI%2FhKl2L1EzyczaTqQ4BejUfwsQAwMobMuKk6ZYB2%2FRiocvS8kv6kh%2BP3x3Sa2zGs6MCB7DBYtEQ2pz29o04zfyEIFqkAMJOcYz&X-Amz-Signature=32f14329007230a4800c356ebf99da25f95cdefaa03915dc51f16902a912312d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPMJEBNV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCICgAknTp%2B9Xm%2B6bW9ffbwuNbYbXsDgqYREjKgQa8PB21AiEA1FYrJEoN82BaVbwS71Nxf2NPfV746on5nwEFlTRKCg0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN0KtBKRvrcz7u6gvircA0pM46dK%2BzWEyDUIqYdCCtSDdbEcq%2B1%2BWpQheGQO4NOXjyNyfjoo7ZZ4TiHxFgCTUfUFSqviEtCyH0WyuS91fTZneklyWbLVtv1aPD8MSXYVTLzKmVrxRa9HAjfsrqghPKQr794DMBvR05Pq01oiE8Sut0PElLuHTl4TB4T6AWhYZD5eLNZpRipiG9YCyQ5iQlUCvUuJpz%2BwMNNzO9Vs4xkKqnpuR%2FO3bECoHyYDnoM5WqlUgovrWudMCgaviXX38K4pxTWdCrrOGjE%2FSyjmwW6tzXRuVZwiwipbRA5OYx%2BO5XsmgaqlxcjCWn6ucrH5fQtTk96OGO8rBLp0nxG5YuVugw%2FbezZCWzQ%2B9nGnjYXqsKP4EZt4PJkcmxW8MEDrbHKq4FHgE%2B6NS5YiusPAqtgxKP7cZCau0Xx3%2FlX%2FFl6W7tR9Peb6CeYqIdKmsQfPJtjo55qOeeGc0ZLMjTTlNXGGBFr7i58cAG5cBHtSci%2FvH3Z%2F0QUZu%2BNz8fTVf8cvEdDSzqm1wTKvUvWceVTqNnmDAzQLvk87Fd3ejJRNAGwxIWFKXvKvjLXcmQnp9SBOXgLuOwjPfbg9QmJsrABs8HwMzbGBMOmzK96x6MMb6fWw9nprGgOV147ZM2EnMMjRk70GOqUBv3fXCzEEoXUzJ%2Fljltw5pXlgVdA1lv0gx9z6z3n2RRUBCIEnv4yz6cqGQToQmqC3VXKKyhbPBWiHYyppwPJJIn7HSlulmMZUhEk2TO2FWJOQI%2FWwmFG4dqyliTIlxiee1%2BqbyZp2ryhsvIjnmMasfctTe7B2GGIMR%2BHdUumFFW4LjmMq9OkKyYk%2Bje5pt14V2IsaE9Lr7C8AQyaXt0WClGf2nf0N&X-Amz-Signature=53cfb7a9b5f7e4b96a9ae75a8bcf950fd688697599e5630dc69560ec58bbc0bb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPMJEBNV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCICgAknTp%2B9Xm%2B6bW9ffbwuNbYbXsDgqYREjKgQa8PB21AiEA1FYrJEoN82BaVbwS71Nxf2NPfV746on5nwEFlTRKCg0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN0KtBKRvrcz7u6gvircA0pM46dK%2BzWEyDUIqYdCCtSDdbEcq%2B1%2BWpQheGQO4NOXjyNyfjoo7ZZ4TiHxFgCTUfUFSqviEtCyH0WyuS91fTZneklyWbLVtv1aPD8MSXYVTLzKmVrxRa9HAjfsrqghPKQr794DMBvR05Pq01oiE8Sut0PElLuHTl4TB4T6AWhYZD5eLNZpRipiG9YCyQ5iQlUCvUuJpz%2BwMNNzO9Vs4xkKqnpuR%2FO3bECoHyYDnoM5WqlUgovrWudMCgaviXX38K4pxTWdCrrOGjE%2FSyjmwW6tzXRuVZwiwipbRA5OYx%2BO5XsmgaqlxcjCWn6ucrH5fQtTk96OGO8rBLp0nxG5YuVugw%2FbezZCWzQ%2B9nGnjYXqsKP4EZt4PJkcmxW8MEDrbHKq4FHgE%2B6NS5YiusPAqtgxKP7cZCau0Xx3%2FlX%2FFl6W7tR9Peb6CeYqIdKmsQfPJtjo55qOeeGc0ZLMjTTlNXGGBFr7i58cAG5cBHtSci%2FvH3Z%2F0QUZu%2BNz8fTVf8cvEdDSzqm1wTKvUvWceVTqNnmDAzQLvk87Fd3ejJRNAGwxIWFKXvKvjLXcmQnp9SBOXgLuOwjPfbg9QmJsrABs8HwMzbGBMOmzK96x6MMb6fWw9nprGgOV147ZM2EnMMjRk70GOqUBv3fXCzEEoXUzJ%2Fljltw5pXlgVdA1lv0gx9z6z3n2RRUBCIEnv4yz6cqGQToQmqC3VXKKyhbPBWiHYyppwPJJIn7HSlulmMZUhEk2TO2FWJOQI%2FWwmFG4dqyliTIlxiee1%2BqbyZp2ryhsvIjnmMasfctTe7B2GGIMR%2BHdUumFFW4LjmMq9OkKyYk%2Bje5pt14V2IsaE9Lr7C8AQyaXt0WClGf2nf0N&X-Amz-Signature=1234c397ec0345ef94b74b556cb8591ddab4fc598baa7fc0ab1ea031bf9d34cf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPMJEBNV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCICgAknTp%2B9Xm%2B6bW9ffbwuNbYbXsDgqYREjKgQa8PB21AiEA1FYrJEoN82BaVbwS71Nxf2NPfV746on5nwEFlTRKCg0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN0KtBKRvrcz7u6gvircA0pM46dK%2BzWEyDUIqYdCCtSDdbEcq%2B1%2BWpQheGQO4NOXjyNyfjoo7ZZ4TiHxFgCTUfUFSqviEtCyH0WyuS91fTZneklyWbLVtv1aPD8MSXYVTLzKmVrxRa9HAjfsrqghPKQr794DMBvR05Pq01oiE8Sut0PElLuHTl4TB4T6AWhYZD5eLNZpRipiG9YCyQ5iQlUCvUuJpz%2BwMNNzO9Vs4xkKqnpuR%2FO3bECoHyYDnoM5WqlUgovrWudMCgaviXX38K4pxTWdCrrOGjE%2FSyjmwW6tzXRuVZwiwipbRA5OYx%2BO5XsmgaqlxcjCWn6ucrH5fQtTk96OGO8rBLp0nxG5YuVugw%2FbezZCWzQ%2B9nGnjYXqsKP4EZt4PJkcmxW8MEDrbHKq4FHgE%2B6NS5YiusPAqtgxKP7cZCau0Xx3%2FlX%2FFl6W7tR9Peb6CeYqIdKmsQfPJtjo55qOeeGc0ZLMjTTlNXGGBFr7i58cAG5cBHtSci%2FvH3Z%2F0QUZu%2BNz8fTVf8cvEdDSzqm1wTKvUvWceVTqNnmDAzQLvk87Fd3ejJRNAGwxIWFKXvKvjLXcmQnp9SBOXgLuOwjPfbg9QmJsrABs8HwMzbGBMOmzK96x6MMb6fWw9nprGgOV147ZM2EnMMjRk70GOqUBv3fXCzEEoXUzJ%2Fljltw5pXlgVdA1lv0gx9z6z3n2RRUBCIEnv4yz6cqGQToQmqC3VXKKyhbPBWiHYyppwPJJIn7HSlulmMZUhEk2TO2FWJOQI%2FWwmFG4dqyliTIlxiee1%2BqbyZp2ryhsvIjnmMasfctTe7B2GGIMR%2BHdUumFFW4LjmMq9OkKyYk%2Bje5pt14V2IsaE9Lr7C8AQyaXt0WClGf2nf0N&X-Amz-Signature=163c383aaa5625744570589f0e7d967331e532cc1fdfcd4a3ebce6313cb0897b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPMJEBNV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCICgAknTp%2B9Xm%2B6bW9ffbwuNbYbXsDgqYREjKgQa8PB21AiEA1FYrJEoN82BaVbwS71Nxf2NPfV746on5nwEFlTRKCg0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN0KtBKRvrcz7u6gvircA0pM46dK%2BzWEyDUIqYdCCtSDdbEcq%2B1%2BWpQheGQO4NOXjyNyfjoo7ZZ4TiHxFgCTUfUFSqviEtCyH0WyuS91fTZneklyWbLVtv1aPD8MSXYVTLzKmVrxRa9HAjfsrqghPKQr794DMBvR05Pq01oiE8Sut0PElLuHTl4TB4T6AWhYZD5eLNZpRipiG9YCyQ5iQlUCvUuJpz%2BwMNNzO9Vs4xkKqnpuR%2FO3bECoHyYDnoM5WqlUgovrWudMCgaviXX38K4pxTWdCrrOGjE%2FSyjmwW6tzXRuVZwiwipbRA5OYx%2BO5XsmgaqlxcjCWn6ucrH5fQtTk96OGO8rBLp0nxG5YuVugw%2FbezZCWzQ%2B9nGnjYXqsKP4EZt4PJkcmxW8MEDrbHKq4FHgE%2B6NS5YiusPAqtgxKP7cZCau0Xx3%2FlX%2FFl6W7tR9Peb6CeYqIdKmsQfPJtjo55qOeeGc0ZLMjTTlNXGGBFr7i58cAG5cBHtSci%2FvH3Z%2F0QUZu%2BNz8fTVf8cvEdDSzqm1wTKvUvWceVTqNnmDAzQLvk87Fd3ejJRNAGwxIWFKXvKvjLXcmQnp9SBOXgLuOwjPfbg9QmJsrABs8HwMzbGBMOmzK96x6MMb6fWw9nprGgOV147ZM2EnMMjRk70GOqUBv3fXCzEEoXUzJ%2Fljltw5pXlgVdA1lv0gx9z6z3n2RRUBCIEnv4yz6cqGQToQmqC3VXKKyhbPBWiHYyppwPJJIn7HSlulmMZUhEk2TO2FWJOQI%2FWwmFG4dqyliTIlxiee1%2BqbyZp2ryhsvIjnmMasfctTe7B2GGIMR%2BHdUumFFW4LjmMq9OkKyYk%2Bje5pt14V2IsaE9Lr7C8AQyaXt0WClGf2nf0N&X-Amz-Signature=47fee7e200a5d7cdc3de3ae1b0b8efa54bdcb1854f811c7982c5afba39b125af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPMJEBNV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCICgAknTp%2B9Xm%2B6bW9ffbwuNbYbXsDgqYREjKgQa8PB21AiEA1FYrJEoN82BaVbwS71Nxf2NPfV746on5nwEFlTRKCg0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN0KtBKRvrcz7u6gvircA0pM46dK%2BzWEyDUIqYdCCtSDdbEcq%2B1%2BWpQheGQO4NOXjyNyfjoo7ZZ4TiHxFgCTUfUFSqviEtCyH0WyuS91fTZneklyWbLVtv1aPD8MSXYVTLzKmVrxRa9HAjfsrqghPKQr794DMBvR05Pq01oiE8Sut0PElLuHTl4TB4T6AWhYZD5eLNZpRipiG9YCyQ5iQlUCvUuJpz%2BwMNNzO9Vs4xkKqnpuR%2FO3bECoHyYDnoM5WqlUgovrWudMCgaviXX38K4pxTWdCrrOGjE%2FSyjmwW6tzXRuVZwiwipbRA5OYx%2BO5XsmgaqlxcjCWn6ucrH5fQtTk96OGO8rBLp0nxG5YuVugw%2FbezZCWzQ%2B9nGnjYXqsKP4EZt4PJkcmxW8MEDrbHKq4FHgE%2B6NS5YiusPAqtgxKP7cZCau0Xx3%2FlX%2FFl6W7tR9Peb6CeYqIdKmsQfPJtjo55qOeeGc0ZLMjTTlNXGGBFr7i58cAG5cBHtSci%2FvH3Z%2F0QUZu%2BNz8fTVf8cvEdDSzqm1wTKvUvWceVTqNnmDAzQLvk87Fd3ejJRNAGwxIWFKXvKvjLXcmQnp9SBOXgLuOwjPfbg9QmJsrABs8HwMzbGBMOmzK96x6MMb6fWw9nprGgOV147ZM2EnMMjRk70GOqUBv3fXCzEEoXUzJ%2Fljltw5pXlgVdA1lv0gx9z6z3n2RRUBCIEnv4yz6cqGQToQmqC3VXKKyhbPBWiHYyppwPJJIn7HSlulmMZUhEk2TO2FWJOQI%2FWwmFG4dqyliTIlxiee1%2BqbyZp2ryhsvIjnmMasfctTe7B2GGIMR%2BHdUumFFW4LjmMq9OkKyYk%2Bje5pt14V2IsaE9Lr7C8AQyaXt0WClGf2nf0N&X-Amz-Signature=c6f50a5343e9a747b2d36240debbdba6f7a1f39fbf7ad6a2a30b83e6a9689d83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPMJEBNV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCICgAknTp%2B9Xm%2B6bW9ffbwuNbYbXsDgqYREjKgQa8PB21AiEA1FYrJEoN82BaVbwS71Nxf2NPfV746on5nwEFlTRKCg0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN0KtBKRvrcz7u6gvircA0pM46dK%2BzWEyDUIqYdCCtSDdbEcq%2B1%2BWpQheGQO4NOXjyNyfjoo7ZZ4TiHxFgCTUfUFSqviEtCyH0WyuS91fTZneklyWbLVtv1aPD8MSXYVTLzKmVrxRa9HAjfsrqghPKQr794DMBvR05Pq01oiE8Sut0PElLuHTl4TB4T6AWhYZD5eLNZpRipiG9YCyQ5iQlUCvUuJpz%2BwMNNzO9Vs4xkKqnpuR%2FO3bECoHyYDnoM5WqlUgovrWudMCgaviXX38K4pxTWdCrrOGjE%2FSyjmwW6tzXRuVZwiwipbRA5OYx%2BO5XsmgaqlxcjCWn6ucrH5fQtTk96OGO8rBLp0nxG5YuVugw%2FbezZCWzQ%2B9nGnjYXqsKP4EZt4PJkcmxW8MEDrbHKq4FHgE%2B6NS5YiusPAqtgxKP7cZCau0Xx3%2FlX%2FFl6W7tR9Peb6CeYqIdKmsQfPJtjo55qOeeGc0ZLMjTTlNXGGBFr7i58cAG5cBHtSci%2FvH3Z%2F0QUZu%2BNz8fTVf8cvEdDSzqm1wTKvUvWceVTqNnmDAzQLvk87Fd3ejJRNAGwxIWFKXvKvjLXcmQnp9SBOXgLuOwjPfbg9QmJsrABs8HwMzbGBMOmzK96x6MMb6fWw9nprGgOV147ZM2EnMMjRk70GOqUBv3fXCzEEoXUzJ%2Fljltw5pXlgVdA1lv0gx9z6z3n2RRUBCIEnv4yz6cqGQToQmqC3VXKKyhbPBWiHYyppwPJJIn7HSlulmMZUhEk2TO2FWJOQI%2FWwmFG4dqyliTIlxiee1%2BqbyZp2ryhsvIjnmMasfctTe7B2GGIMR%2BHdUumFFW4LjmMq9OkKyYk%2Bje5pt14V2IsaE9Lr7C8AQyaXt0WClGf2nf0N&X-Amz-Signature=bfcb65fe2ed8f015cd22035cee0125cb23b2965820d1f1aa554754469a3531df&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RUSE45U%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIF1DNZy1gInNMpw99oOtTqkPDILSRZr59dMRYYwXcTFPAiEAzHfu3IjO1h284ReMMC98JiRr1L6FQgD3pm%2FD7iZJEHIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDD5%2BirYKggD%2FeCf20SrcA%2BLEHfcQbHMV9Rgkv8tuCA7kpKT1Yx8b6w5NioOREKlJLMJqsV606f7pSAdAjd4WS%2Bd0%2Bn0C9Lx4ctfX6n6b5fmlGHorGztNVEcQvRcSlLBFQWv0My%2BUMs8u5SiffrNhQWH1%2BgivPPjSIG6EAvd7JGwFED9%2BH%2FS48a5hGnFijL7PVlD5pYtnnaqTSOp0lgdCyk2p9nxv6WiR7dxGfPUJrLFk1STc9e%2BUQbRO6XW9JrZbNt%2FdcOGY68foS6x2l3GcxnNHnVVHKlAjeKBAqwM02DZ1vSDCO6ZW9nidJO1J0OV6Wilxtn4Np%2BoRpV21pPyGA%2BpgUBooMx4puRIk7GRwS%2F0JY9pTvsiCAizDCwAJzoidfJkJ4pYmWqmJ75eNh0vzfHfshHIiSvgzMSyEbvYLx6lK9mKxv2g0DoIJdhrg4duOPn%2BGtnbYlcCFT54W6CzCptodG8FaRZmW0e9pu8c7ELjaID9I9zOn2uDi92AiJtBuyI8cc80j78yTVlfYlVENZSo7OMYeO9eSJoV8HhKClZIWE90HViRvt8NlrxgGTnrRHOaeOWG%2FS%2BfM0w8ETyHwZjYjQ5E9ZMAgezyn1FK4KiUyQlwz0PXAZIKjtOL5uhEykmEGjuWedbDqs6%2BfMJXRk70GOqUBUrp%2ByKYTpJrJaUu4SM%2B1KNZujznWFvkN5Br2Qm8yQoI3eJ0OVkCOIERjgRmPK1XAABBbQzNodJeyCjcqHj8pEFYsmRg55HCnAoH%2F5vLypdGf%2FtFd%2FtB8BPVQ%2BgSYYqR%2FHVNfYKIhzY5paS43qzZ3A3KMd0wbd8ieDNFrMcHUGJ3s2TrAu6vFQmRX3l1wgiWQkcSqWdaYHokbX1wNqd6D55gqJhom&X-Amz-Signature=860f515bf60fbd2745e63874ed5b81b77a7590126e9d9bedad2d88ae26abcb1a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QXRV322%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDj0A6fX6lhIWvP5IbyTTjB5rvk9ghUPIKVzDFatFSt2wIhAM%2FsyfJks5R1mkeZy8x4iyj50v6r7OzDR3CFSj1YbxS7Kv8DCGIQABoMNjM3NDIzMTgzODA1IgyY0vaVluyyOt9xziwq3AOD7jFbhIjxQ8fq0HOH4PnubsrNx%2FlnM01FR%2FMyN3A4BNDTxNMhpnLm91dYwnkn44njOjHbBFN41QahULV1msZM8CL9f%2BPOusjUkFeJ6RsyDZP8xRxBPfVBfzTutf62T%2FtoYXVtz%2FKdYdaq385w0Awb5T976jsSjuz%2BZwgPkhWDJraSTa8Nj%2B2YkmakY1JcXpqYtRdZSe0%2BrkolJnd%2Ffs8aioIJymeILkKv8bKvkiJKBiaVbgUxQMbn%2FIUVxBuVP5ZAmYkHlfQb9KoMKu%2BwSPgsMpnOwRXE%2Ff5XAX9aI0qPIiT4qlIwThY7aT%2FZdIQklzzyot%2FDyti7onrlJ%2FLt8koiq2NDFfOGZioKDDh7M1Gm8lurHcylNiYXA%2FEUCk1J3KqlnCepy9SSa5VM5xLULRl%2BvzEnfGSTNqUcQBerPW%2BrA5UMYWBv6pAWLPtcyDUJLPK8sMeyjCEniqFioQcxNEG2KBsWDVTdM5H6nmCVganRCCM2I4VyeaJxoVfQ%2Fiybn%2FBq90ZJ5qDbsbC5%2ByosPbUaVbCBlYh2C0mlhMug2dIzJWRqeNCY4wPtSYzLe1boatP0cbtNRaSdJBb%2FwSrA0uh7MkuEEyaR1WM9ru3B0x0SKlR%2BR4O7f8SA2wbjNTCb0ZO9BjqkAWj8lzUN0Q9Cp4tq35GDsuhnF2NbFgNoiO22gUzDIn8hePs84lB4qzBl17YyuIeKqHYYPN4uq3cuVC7wdZoKX5ACy1FDQhnjNahtktlA04vzn%2BXh4lsi4yHxik8OmVyazZJ4kokOI7praUuWX%2BT1Maouv1W7KGvGK%2F3oRs69p5yw2S0BfO950cSyTTrswWbKh2j7vk5h4NCu0dkdvfVq9icUVLL4&X-Amz-Signature=18f663baf1a0fefa69f2c38dfef3d2b45632f3a4a76d8bdbf91c0d43edf4ece3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPMJEBNV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCICgAknTp%2B9Xm%2B6bW9ffbwuNbYbXsDgqYREjKgQa8PB21AiEA1FYrJEoN82BaVbwS71Nxf2NPfV746on5nwEFlTRKCg0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN0KtBKRvrcz7u6gvircA0pM46dK%2BzWEyDUIqYdCCtSDdbEcq%2B1%2BWpQheGQO4NOXjyNyfjoo7ZZ4TiHxFgCTUfUFSqviEtCyH0WyuS91fTZneklyWbLVtv1aPD8MSXYVTLzKmVrxRa9HAjfsrqghPKQr794DMBvR05Pq01oiE8Sut0PElLuHTl4TB4T6AWhYZD5eLNZpRipiG9YCyQ5iQlUCvUuJpz%2BwMNNzO9Vs4xkKqnpuR%2FO3bECoHyYDnoM5WqlUgovrWudMCgaviXX38K4pxTWdCrrOGjE%2FSyjmwW6tzXRuVZwiwipbRA5OYx%2BO5XsmgaqlxcjCWn6ucrH5fQtTk96OGO8rBLp0nxG5YuVugw%2FbezZCWzQ%2B9nGnjYXqsKP4EZt4PJkcmxW8MEDrbHKq4FHgE%2B6NS5YiusPAqtgxKP7cZCau0Xx3%2FlX%2FFl6W7tR9Peb6CeYqIdKmsQfPJtjo55qOeeGc0ZLMjTTlNXGGBFr7i58cAG5cBHtSci%2FvH3Z%2F0QUZu%2BNz8fTVf8cvEdDSzqm1wTKvUvWceVTqNnmDAzQLvk87Fd3ejJRNAGwxIWFKXvKvjLXcmQnp9SBOXgLuOwjPfbg9QmJsrABs8HwMzbGBMOmzK96x6MMb6fWw9nprGgOV147ZM2EnMMjRk70GOqUBv3fXCzEEoXUzJ%2Fljltw5pXlgVdA1lv0gx9z6z3n2RRUBCIEnv4yz6cqGQToQmqC3VXKKyhbPBWiHYyppwPJJIn7HSlulmMZUhEk2TO2FWJOQI%2FWwmFG4dqyliTIlxiee1%2BqbyZp2ryhsvIjnmMasfctTe7B2GGIMR%2BHdUumFFW4LjmMq9OkKyYk%2Bje5pt14V2IsaE9Lr7C8AQyaXt0WClGf2nf0N&X-Amz-Signature=c76b8ce5e1ee692aa7a5a6360ecfb27397afc7bf6e37214a7d885d5384d0d867&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPMJEBNV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCICgAknTp%2B9Xm%2B6bW9ffbwuNbYbXsDgqYREjKgQa8PB21AiEA1FYrJEoN82BaVbwS71Nxf2NPfV746on5nwEFlTRKCg0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN0KtBKRvrcz7u6gvircA0pM46dK%2BzWEyDUIqYdCCtSDdbEcq%2B1%2BWpQheGQO4NOXjyNyfjoo7ZZ4TiHxFgCTUfUFSqviEtCyH0WyuS91fTZneklyWbLVtv1aPD8MSXYVTLzKmVrxRa9HAjfsrqghPKQr794DMBvR05Pq01oiE8Sut0PElLuHTl4TB4T6AWhYZD5eLNZpRipiG9YCyQ5iQlUCvUuJpz%2BwMNNzO9Vs4xkKqnpuR%2FO3bECoHyYDnoM5WqlUgovrWudMCgaviXX38K4pxTWdCrrOGjE%2FSyjmwW6tzXRuVZwiwipbRA5OYx%2BO5XsmgaqlxcjCWn6ucrH5fQtTk96OGO8rBLp0nxG5YuVugw%2FbezZCWzQ%2B9nGnjYXqsKP4EZt4PJkcmxW8MEDrbHKq4FHgE%2B6NS5YiusPAqtgxKP7cZCau0Xx3%2FlX%2FFl6W7tR9Peb6CeYqIdKmsQfPJtjo55qOeeGc0ZLMjTTlNXGGBFr7i58cAG5cBHtSci%2FvH3Z%2F0QUZu%2BNz8fTVf8cvEdDSzqm1wTKvUvWceVTqNnmDAzQLvk87Fd3ejJRNAGwxIWFKXvKvjLXcmQnp9SBOXgLuOwjPfbg9QmJsrABs8HwMzbGBMOmzK96x6MMb6fWw9nprGgOV147ZM2EnMMjRk70GOqUBv3fXCzEEoXUzJ%2Fljltw5pXlgVdA1lv0gx9z6z3n2RRUBCIEnv4yz6cqGQToQmqC3VXKKyhbPBWiHYyppwPJJIn7HSlulmMZUhEk2TO2FWJOQI%2FWwmFG4dqyliTIlxiee1%2BqbyZp2ryhsvIjnmMasfctTe7B2GGIMR%2BHdUumFFW4LjmMq9OkKyYk%2Bje5pt14V2IsaE9Lr7C8AQyaXt0WClGf2nf0N&X-Amz-Signature=d1042d988fa3cd1b0be38387df0b290b652007b17522ff7402ce1f599b300f53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPMJEBNV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCICgAknTp%2B9Xm%2B6bW9ffbwuNbYbXsDgqYREjKgQa8PB21AiEA1FYrJEoN82BaVbwS71Nxf2NPfV746on5nwEFlTRKCg0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN0KtBKRvrcz7u6gvircA0pM46dK%2BzWEyDUIqYdCCtSDdbEcq%2B1%2BWpQheGQO4NOXjyNyfjoo7ZZ4TiHxFgCTUfUFSqviEtCyH0WyuS91fTZneklyWbLVtv1aPD8MSXYVTLzKmVrxRa9HAjfsrqghPKQr794DMBvR05Pq01oiE8Sut0PElLuHTl4TB4T6AWhYZD5eLNZpRipiG9YCyQ5iQlUCvUuJpz%2BwMNNzO9Vs4xkKqnpuR%2FO3bECoHyYDnoM5WqlUgovrWudMCgaviXX38K4pxTWdCrrOGjE%2FSyjmwW6tzXRuVZwiwipbRA5OYx%2BO5XsmgaqlxcjCWn6ucrH5fQtTk96OGO8rBLp0nxG5YuVugw%2FbezZCWzQ%2B9nGnjYXqsKP4EZt4PJkcmxW8MEDrbHKq4FHgE%2B6NS5YiusPAqtgxKP7cZCau0Xx3%2FlX%2FFl6W7tR9Peb6CeYqIdKmsQfPJtjo55qOeeGc0ZLMjTTlNXGGBFr7i58cAG5cBHtSci%2FvH3Z%2F0QUZu%2BNz8fTVf8cvEdDSzqm1wTKvUvWceVTqNnmDAzQLvk87Fd3ejJRNAGwxIWFKXvKvjLXcmQnp9SBOXgLuOwjPfbg9QmJsrABs8HwMzbGBMOmzK96x6MMb6fWw9nprGgOV147ZM2EnMMjRk70GOqUBv3fXCzEEoXUzJ%2Fljltw5pXlgVdA1lv0gx9z6z3n2RRUBCIEnv4yz6cqGQToQmqC3VXKKyhbPBWiHYyppwPJJIn7HSlulmMZUhEk2TO2FWJOQI%2FWwmFG4dqyliTIlxiee1%2BqbyZp2ryhsvIjnmMasfctTe7B2GGIMR%2BHdUumFFW4LjmMq9OkKyYk%2Bje5pt14V2IsaE9Lr7C8AQyaXt0WClGf2nf0N&X-Amz-Signature=2b23349329f80e8cb4425814155cf824e3d6bbd0047ca735a617e0e7ec218de6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666F4J6FOL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCi84WGZI35Pw8J8JIYXkYi2hjLby36gNf0egL%2FZ71KQwIgCouGrPrlaUwTRQFcYoPeW%2BnGaasO5Ts0y4OVMDcxxVsq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDEc3xgYkcPiYD1AX1ircA4BNHAcw737%2B6lnC7i2epen9wMHDzq6sTn6FofEx523AuXiMil%2FfSJ89%2FFoQhjfWU9Q3k%2BZarBYrz1t6G849L8YHEDy08scnjJ9zKKDeUPCYv7ULldtNMc3fjLqivqXe6mKLdPm5568AmBl%2FBPbFZEJzl7V0YNdPvTh4Hn7JMCoMq50QR55UnVcjQznB1VCfBmkcHLhW5s0Rhf1Q33TbsGgWcdeTc%2FqfauwhLrQhoYX9pUsnFV8Kl41c5ic8ars8p9E%2FWCFxDgSh02YUOdDVurwMKS8EKwfrQVZIWGlDipWWwLvMLefxrvXEZkmDp%2BAWla1dsQlyObqTPWUY7CdO2s3pW6iW5t%2FqayZXZd5g5Dcq3flFYRcYEMhThBJTjzteF5IYqeiR5lcnNCzM8pxTjutPcy0yfkVFeBVGVfqBLNUhBZez65SR83pSJph8vdtDuC9jDVzzv%2B3ooGOl90rel3bUrrh5MKYLfcQaKuaVQO8s%2BWFTqXMfiqWRktgnpDrgvgjCm%2B%2FyP0ND3wnfIZ9Esy4jRjsBFYeUTbXGxeW3t5dCf9WprwwqC7CE81aL4KfHxBH5GfCV%2BCAv3YxPxrnn2GMUzi5E3iCP8244nGCMHs4YUGERlX3w9trpOWjEMMbRk70GOqUBPHEt0e0Dg2tu1l0z%2B2vUbkkd3myMbib4r9ykg16vL%2F%2BbMO2qWCl4T78eUonG0L7q%2FtphLIR8ugMIVVfqZCh2CZjCPrgbX2nCEXLzf8Gmv9f4uxTFy7aQEuC32xHUYWt3dwUW0agQx%2BRfQwjaNTpcOf2uLGRqa2D5Pj0JKOfRfBHQNK6dQ6eskrvjgYVNmcvIZtmW1JEd6%2Blvaa3mitmq3gvS9rb0&X-Amz-Signature=949e4581185b00747f223f6842bb0dd2564e60f59c8cb66539c886b9f4f6b77b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FV5AY3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDIKP%2Bi73D%2BXQLLxcG0j8bLaN9zZC%2FH2QgsatBiseIq9QIhAMomDbwPwZi64pOyg9cn1R%2BFN9G9zpDC8H8ntFASxoQhKv8DCGIQABoMNjM3NDIzMTgzODA1Igw9LCXru7qkYwfRBowq3AMTPqMqLsGRGivJ6bcYlcM5Kc6RzbvDZslj1reaCFUzffJtg74lhSpVC5XM5KAoAZR%2FtosWppJN1%2F2G7x6EPTZwh2ob5QMj5DlVwcbUydXKGY8P9rP%2FSM9risN%2FbHHU4Y8w8He8DC6A21yJnFLfzHkON0kNPGv%2BAfy1wJsbpb3%2BhbyMTW%2Ffi8TgeGF59Zagmxj0mcestpfg%2BPJV%2BerNHmmt2MXYUZp%2FTVZLWwp%2FB3yD2n1uHZYDGKzhOUv0WjuUmPXrBs5rITn77xPVdivocPm4TFmNkMCHz0ZOZ%2FIZ%2BwUJqAEL4Vl6cB3uhccaSHkFKi11LCwQvoiHpELEy4jLOTJAhRjk%2Fjlf6fRsHYCQdzHyvQeID4sFL6v0Fy%2B67lP2phN5MjFhdqwkatU3Vaid1w52bqDy4YV9FYExEez7AH2B9o3Ki%2FEHSrYd72hje734Y601l49PxUgvqa%2FbHKSBLtahA7y7AoEIihYloDRpx8YizsAnz5kHSznU%2B6yJ%2B4r3VBz%2Fz6BT7y2t2bfHUmcWoH%2BtGxOeOOLyva%2FX17OOEisgb8Xn1O%2FnPT53yf0Pvv1Ycqjd2i5lC2IHdT8J%2FfyporK3%2BZPoLXr1yhUSJVxkVwB0QQLgsAHLNDCVthPQkjCW0ZO9BjqkASTSv2TkqXTVItf3ozeb8aSI8MwvsD7FDFEZhxGL38w%2FInIL5gRmBJ786UaI0d40191HmmynBzwW6lUxDFebPo8SBFIvHFV6aNawPr25BPnk7V2cEQiiru2dyO1B6q6H4tbOgqLyI3jyLVGR%2B67jBKVhXzWV9v%2BtBOYp%2BILqoyOElM1POE5V3yHSj49d%2BA9SFOFO8my9Knd1laV1wJsNKmQ9RwI1&X-Amz-Signature=88f0a8e8d78f2673b418d14b3c7d2d66c2d54d265d8b0f3f242b42fb8b896527&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LK5C7SV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDAVVbhKdKKBCnWSYjqUHL2JQNLCQ0Fu5y9CcC4kpZLKgIhAKFkhadgNVnXSQ4rdTyCdpiNWRkPRrEvWpkXonWnr%2F0JKv8DCGIQABoMNjM3NDIzMTgzODA1IgwapdibcgJKM%2B1%2BpSEq3AOTwGpiW%2B2AaLTaW%2B1%2FNayifXq%2BwKEdGihwjf04zPEuNKCCxL2QYOJySjVbeyWz%2B0f8v1yH%2Bnx7eopWzc14a2VMOP1bxxzMWpsOwZTWoZ4CNHAddGi9CG9b%2BlE17JzIHdJpCrjDJKLuJsxSn8gaL1yzyn%2FlQlOp818AlPA%2FWu9d3LlVowB%2F%2B6SLpsCXgHvF4GfjSJvAyegpv6CFzwzd3BtTfWpRdWw%2B1jWskUdcT4NDGOK4CM19FGQI6feSmecenk1XHFQkfkIGPdHLMghzeVpkLkltw2UpQ7nTJl2V3jtegcQXjfjr1NZfY89G3B2O5sF8T%2BQIhgqw%2FLX22%2BcBGii4eQRCnLckFxy0S9R7UP5kclsbZoug%2FdsGso8WM%2BEdYiAYmninjZv4RZUeDuf4USzb3IsV2%2BuGkKRBrdI%2B3czfLhjpxnTTvR%2Fd%2Fng2zWh8QS%2B%2B8pc%2BszS0zfA0n7gC4reqMMTChsINbOJTpmG6QxNzI%2FREut0vebjb2BhbUgxfrU4Fv7K76i1Zs4%2FCFrqVn7C1P4eGppFpCVtvbPYxxA4EWdkZ9wM6hR3vlDlurvXtFVj9urEt6jPuxsHfiFpzrfMd8OUX5UgiTOoAA9vbdYMiwenfvp4BrIasEb82fDCK0ZO9BjqkATzP3LtXAc3eDwEM5NQHonopSpD2xDVonmQavPeQqchIQ613H4B7z6XpTfLzHGRFve0lOZxmR%2F6oGdozsXCb7BevscW2fXPbPg04JRe5gjS9ebWlKjTlOjdu9SQ26b8Cr%2BXb7qqqK1HsR893btUrIlk55RDKidb9u%2F6lFLTPJE9EisGSmcJfAAZ5o6B7RNBBmcOCcC4RPEKmS%2BmIH5SQmcxnJXM0&X-Amz-Signature=7520126113c3aea0f2bb8e808acee44e5bb52e0b1c973c0261533ac6da68b495&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNPW7HXD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIHLT8NJJCbNPmjx6pLyBmF1Edn7uWBz8srwXuNCCxvoBAiEAw3BfEnHUJoPVWMLeHPFc%2BhtCfULHNQU5%2B5NKPHQiq0sq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJulrnykkK2kzW0%2F0SrcA2yKIuL3ZCwo0Of8dr5AXd40g%2BXExEopmfNfELy1Lzy1Q%2F5lWxifAluCwrppXni%2BcNRIZ11Vg05DSGis2NEeufzh1nKOOcrwdn1zJfacj9VHA43hvia779weby1SkInnJ0m95mjwbXqGMm%2FpvRwUdzXeWKXUh2dpXTbdb8xidLJWVlG%2FLbwku1pc%2B1O3ATwuxkGiYUrxLe2LqtdsO6tko%2BFtPN4gLGbMRFEP%2BkIwBysZob6nd9Y4cPwewzcn175thFxGb2vdLTJAsgtZRl7zKBpAMx7yY49BHE34izjV3%2FmTIGmo48oTeuDy%2B%2FDeQg1nRPaM%2FHbj%2F3nfs7z6zeKex8CRZrtpuTZ5dTAwt4jCZoje1f0K3tCc5YbOYKijOU48LVsEZQpN0RqdYhjEOOD643aAPp6cQ8HwGqpr2ECW8dWrzR7Xh3j%2FSWdTNVfOqQtyoB1PspSqvW%2FEMvpyrNSHtbNzgFD2JHN%2FIHlitJPN0HOWab5QOVwNRQ5fnIWvePcdZvsynL6PYypGIiwvJ3Turo07gOF70lHTRAoTagBgHjv%2FdlP6%2BDGLm2ZjH0v0dUgjyCcKWgwnNdsmgqTdf20lWHQVjNvKCjGi%2BUJ5g0X0Kp0HMlhZREPa0BI7hJJ7MMXRk70GOqUBmA%2BhWfoY8NP7NuiTCPzy6uvvIAMMXVJ7BLP30MTLZxGNBTMmg9thl8w6RobZ3h5le%2Fgul8VlU49XTzoba%2F8%2BpuziASZV9jenRSV8iEbdfZ2FkOJTuAfZVY4wOepHjUIbOqfT%2BtcYKDd%2FMR5riMrsDZioP0wnLZhifN3xttD3QInStvEWr4N6bi8VF6HEBeKszGqs24sJc%2BKTDc%2B%2F8X7DRSyvETri&X-Amz-Signature=c98bb13b2bc9f665dd8eb94b3a787dfe7ad858ab8197d9ce99f12ba0e6069d17&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNPW7HXD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIHLT8NJJCbNPmjx6pLyBmF1Edn7uWBz8srwXuNCCxvoBAiEAw3BfEnHUJoPVWMLeHPFc%2BhtCfULHNQU5%2B5NKPHQiq0sq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJulrnykkK2kzW0%2F0SrcA2yKIuL3ZCwo0Of8dr5AXd40g%2BXExEopmfNfELy1Lzy1Q%2F5lWxifAluCwrppXni%2BcNRIZ11Vg05DSGis2NEeufzh1nKOOcrwdn1zJfacj9VHA43hvia779weby1SkInnJ0m95mjwbXqGMm%2FpvRwUdzXeWKXUh2dpXTbdb8xidLJWVlG%2FLbwku1pc%2B1O3ATwuxkGiYUrxLe2LqtdsO6tko%2BFtPN4gLGbMRFEP%2BkIwBysZob6nd9Y4cPwewzcn175thFxGb2vdLTJAsgtZRl7zKBpAMx7yY49BHE34izjV3%2FmTIGmo48oTeuDy%2B%2FDeQg1nRPaM%2FHbj%2F3nfs7z6zeKex8CRZrtpuTZ5dTAwt4jCZoje1f0K3tCc5YbOYKijOU48LVsEZQpN0RqdYhjEOOD643aAPp6cQ8HwGqpr2ECW8dWrzR7Xh3j%2FSWdTNVfOqQtyoB1PspSqvW%2FEMvpyrNSHtbNzgFD2JHN%2FIHlitJPN0HOWab5QOVwNRQ5fnIWvePcdZvsynL6PYypGIiwvJ3Turo07gOF70lHTRAoTagBgHjv%2FdlP6%2BDGLm2ZjH0v0dUgjyCcKWgwnNdsmgqTdf20lWHQVjNvKCjGi%2BUJ5g0X0Kp0HMlhZREPa0BI7hJJ7MMXRk70GOqUBmA%2BhWfoY8NP7NuiTCPzy6uvvIAMMXVJ7BLP30MTLZxGNBTMmg9thl8w6RobZ3h5le%2Fgul8VlU49XTzoba%2F8%2BpuziASZV9jenRSV8iEbdfZ2FkOJTuAfZVY4wOepHjUIbOqfT%2BtcYKDd%2FMR5riMrsDZioP0wnLZhifN3xttD3QInStvEWr4N6bi8VF6HEBeKszGqs24sJc%2BKTDc%2B%2F8X7DRSyvETri&X-Amz-Signature=467783713c84d4c1f49d178093220eebc8d74a003497a395081b01e0e321dfad&X-Amz-SignedHeaders=host&x-id=GetObject)

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
