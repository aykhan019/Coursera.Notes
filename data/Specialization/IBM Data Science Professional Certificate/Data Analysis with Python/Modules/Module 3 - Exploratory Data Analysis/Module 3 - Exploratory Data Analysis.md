

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFGPY5EY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEs4H%2F41ryk2GR1%2F9qBk6AIuGbnA%2B5qhwMWOSNsMzOu0AiEAmL2kT567WKzifTI2jUpw8HiV7fOEQVOTh2JtU2ghvAUqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMiAOXe2oT28r6FgyrcA%2BI2wgoQenDpIo5wX%2Biu8pNR%2Fw8r1j6jFd%2FPc1a3WdhVmV%2FErmawlljv0UjWiWeUYcjiJsgPQThSy3RyqcfbFhik82YzlxHp2KeS29MXPQbNyhtmrPQOJyGxqdwKXUxPU8Zku9RA376IsyKT1FPnDN8o7aCB2XszfqePNynteQ2yNN5%2Bzcl%2BOUMI%2FbV9gsrmySU%2BPLDa0ntftK1GrVqcIwajGw9K4naNsiB5oYizTLEqQ0umbOqGCUwaXf4%2BUwbLgB%2FMiOIh5q8CKzjMrPQ%2BY5OBx4leQJxQNyryDfMlSBpLYBJhQkEZlx8TOGp27KrQD2VxaEymdGrRHigLX6Odx4M49JfEMNs5e8ZTIluWO5mKbqmhWpxsCOBNqfgPgcJw%2F%2FQkbBEMEeUkkgvJMRD1XN3R9jBqf5QY3CtJMyN1y8A4KdUTa2J9KA59qiTsUbJTpRFU4fu1mH%2F72845Gy9KBzL7QDAxpL%2BhyyaIAcWLugR9PBMxcm7dEIpCDiH3qRgjNrAYUVTWXA71IZDu4LfXUzVmyixZvOdErQBRRORz42qjeLCuuBi3G2JXcmFqC1bwgMhOcuP5FbGz0wg%2BoIgGCDFF23khO3yJuB%2BAS6XbaVAh3QodebbJe9dknPgXMLHF77wGOqUBk4lc0t0qToesqZWBLMxYhVMw9y9HH94J7nWSfu03tVrX90lgxszmmcUR2%2BIWj0jFtuTpDfOmp6t%2BXQKAj3eXkx50QH4axFRFFhT2b8TikMc2zr35p8CpCUwsD4vRAlXMPSNNMgNVyrD4a4pt0FRPN403NGWHqUuRNll1fM5tCNdFl8bjfUGMvSs5bQ%2FNhG%2Bl%2F1njaiCq9RhGQzZstP0wd%2F4yUV3B&X-Amz-Signature=f8523923dcc57e207dd4fdec7fabbf966a173a5323902227848f712d976b0cb2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFGPY5EY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEs4H%2F41ryk2GR1%2F9qBk6AIuGbnA%2B5qhwMWOSNsMzOu0AiEAmL2kT567WKzifTI2jUpw8HiV7fOEQVOTh2JtU2ghvAUqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMiAOXe2oT28r6FgyrcA%2BI2wgoQenDpIo5wX%2Biu8pNR%2Fw8r1j6jFd%2FPc1a3WdhVmV%2FErmawlljv0UjWiWeUYcjiJsgPQThSy3RyqcfbFhik82YzlxHp2KeS29MXPQbNyhtmrPQOJyGxqdwKXUxPU8Zku9RA376IsyKT1FPnDN8o7aCB2XszfqePNynteQ2yNN5%2Bzcl%2BOUMI%2FbV9gsrmySU%2BPLDa0ntftK1GrVqcIwajGw9K4naNsiB5oYizTLEqQ0umbOqGCUwaXf4%2BUwbLgB%2FMiOIh5q8CKzjMrPQ%2BY5OBx4leQJxQNyryDfMlSBpLYBJhQkEZlx8TOGp27KrQD2VxaEymdGrRHigLX6Odx4M49JfEMNs5e8ZTIluWO5mKbqmhWpxsCOBNqfgPgcJw%2F%2FQkbBEMEeUkkgvJMRD1XN3R9jBqf5QY3CtJMyN1y8A4KdUTa2J9KA59qiTsUbJTpRFU4fu1mH%2F72845Gy9KBzL7QDAxpL%2BhyyaIAcWLugR9PBMxcm7dEIpCDiH3qRgjNrAYUVTWXA71IZDu4LfXUzVmyixZvOdErQBRRORz42qjeLCuuBi3G2JXcmFqC1bwgMhOcuP5FbGz0wg%2BoIgGCDFF23khO3yJuB%2BAS6XbaVAh3QodebbJe9dknPgXMLHF77wGOqUBk4lc0t0qToesqZWBLMxYhVMw9y9HH94J7nWSfu03tVrX90lgxszmmcUR2%2BIWj0jFtuTpDfOmp6t%2BXQKAj3eXkx50QH4axFRFFhT2b8TikMc2zr35p8CpCUwsD4vRAlXMPSNNMgNVyrD4a4pt0FRPN403NGWHqUuRNll1fM5tCNdFl8bjfUGMvSs5bQ%2FNhG%2Bl%2F1njaiCq9RhGQzZstP0wd%2F4yUV3B&X-Amz-Signature=d5de579663bc1a902396975231efb6da2acc2c3af5532c52854d09e43936e445&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFGPY5EY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEs4H%2F41ryk2GR1%2F9qBk6AIuGbnA%2B5qhwMWOSNsMzOu0AiEAmL2kT567WKzifTI2jUpw8HiV7fOEQVOTh2JtU2ghvAUqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMiAOXe2oT28r6FgyrcA%2BI2wgoQenDpIo5wX%2Biu8pNR%2Fw8r1j6jFd%2FPc1a3WdhVmV%2FErmawlljv0UjWiWeUYcjiJsgPQThSy3RyqcfbFhik82YzlxHp2KeS29MXPQbNyhtmrPQOJyGxqdwKXUxPU8Zku9RA376IsyKT1FPnDN8o7aCB2XszfqePNynteQ2yNN5%2Bzcl%2BOUMI%2FbV9gsrmySU%2BPLDa0ntftK1GrVqcIwajGw9K4naNsiB5oYizTLEqQ0umbOqGCUwaXf4%2BUwbLgB%2FMiOIh5q8CKzjMrPQ%2BY5OBx4leQJxQNyryDfMlSBpLYBJhQkEZlx8TOGp27KrQD2VxaEymdGrRHigLX6Odx4M49JfEMNs5e8ZTIluWO5mKbqmhWpxsCOBNqfgPgcJw%2F%2FQkbBEMEeUkkgvJMRD1XN3R9jBqf5QY3CtJMyN1y8A4KdUTa2J9KA59qiTsUbJTpRFU4fu1mH%2F72845Gy9KBzL7QDAxpL%2BhyyaIAcWLugR9PBMxcm7dEIpCDiH3qRgjNrAYUVTWXA71IZDu4LfXUzVmyixZvOdErQBRRORz42qjeLCuuBi3G2JXcmFqC1bwgMhOcuP5FbGz0wg%2BoIgGCDFF23khO3yJuB%2BAS6XbaVAh3QodebbJe9dknPgXMLHF77wGOqUBk4lc0t0qToesqZWBLMxYhVMw9y9HH94J7nWSfu03tVrX90lgxszmmcUR2%2BIWj0jFtuTpDfOmp6t%2BXQKAj3eXkx50QH4axFRFFhT2b8TikMc2zr35p8CpCUwsD4vRAlXMPSNNMgNVyrD4a4pt0FRPN403NGWHqUuRNll1fM5tCNdFl8bjfUGMvSs5bQ%2FNhG%2Bl%2F1njaiCq9RhGQzZstP0wd%2F4yUV3B&X-Amz-Signature=74dad8b95ee31842359edf5c9caa8eff8164764ba5e70aea41f470017cd87b70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4DWPFU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4k84qiirKJhLTREpJESYJOz2%2BoP7RTfat%2FbFKmv4UCAiAnEib%2FrRz2h7zQ0tJR3cAJJsuLLpt9d%2Ber73ExJ48ndCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGeE1JSwNcWU1%2FTW1KtwDRxUNJXLqFw2huFqPTPM7umWk8HZKpWSMNlbQNETYZIH3TMDwn0RwX%2B7pPtrgucqlvsALlr2UKnXqlHFsbK0cmOtJr329KsRHXjbH28G1rqL2QVC%2BvAMdx8rLH4tSAjrR9FOQ%2F1%2BqSZ2atdX%2BIKjFJkx6DYcMbkk7z%2F0jOZdRZ6GIa5bE36bjoTAqO0lphPwaHZhU2jrBdjrwyapyF3teH%2Fk2BfDhskmDi2oDrWOTJ%2FHLew3e1xuvyTGBw1EzSRSvHP66XsyZS3JwUurizEmttMTzkMkkpBVmdqDvko1XhdG2HJlOM4uIu%2BlfvuTMgMgOiXHRxad1ICyX8HKctfDqae73pig0ZiBglsAuaECGOvfq2On0YLPMpHH7oiBsaV7hhFyWj41EEuCnbDanzjHxhz1Q9QWa9uxiKr0wmSCE5k7eZu9Pc1cd0w6Evsw70UH95AssHxQhZC%2BfsIS6jh9yaNZ0zDrQd1QnJaKEm7keOlIaYemWz6e6pe%2FEnjD9vdeHS4fsc%2BmpqhAUX33Ci7s9D3ieP5LuhZqZvxc8N9NJzikrUEypmPZn7Ek%2BRiQ0ujYblsmFp6hbKeGlYeEB9B0yyKDEpJyX%2FbibpnQuQILP2eV%2FJsmiTa%2Flb%2FUrIl8w4sXvvAY6pgHCYYECOo5ScadcgpbmA1gHVLwbHmqQ85BimlCiySP84yvOlg6HVm%2FM9Hf0SYxGFPcEfDlTYUwx5%2FFwJ7UjSX%2FAwI2ci54dVTzka0llpIJGcXajg3lKdiEC3OeHj9JCo93%2B1J1%2FH7WQ6acULt3KhvMEE1Q7%2BGWFRooKi%2F%2F5gjrZ5zj9b0cpzrZEjKa%2BwwmUSPttFBo80H4QMa9El1Ssdy619AbKABED&X-Amz-Signature=52c40ea86d3e7e30ef80a98b200c7d54b2613adff1fcbf00edbeb33c292e79e9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4DWPFU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4k84qiirKJhLTREpJESYJOz2%2BoP7RTfat%2FbFKmv4UCAiAnEib%2FrRz2h7zQ0tJR3cAJJsuLLpt9d%2Ber73ExJ48ndCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGeE1JSwNcWU1%2FTW1KtwDRxUNJXLqFw2huFqPTPM7umWk8HZKpWSMNlbQNETYZIH3TMDwn0RwX%2B7pPtrgucqlvsALlr2UKnXqlHFsbK0cmOtJr329KsRHXjbH28G1rqL2QVC%2BvAMdx8rLH4tSAjrR9FOQ%2F1%2BqSZ2atdX%2BIKjFJkx6DYcMbkk7z%2F0jOZdRZ6GIa5bE36bjoTAqO0lphPwaHZhU2jrBdjrwyapyF3teH%2Fk2BfDhskmDi2oDrWOTJ%2FHLew3e1xuvyTGBw1EzSRSvHP66XsyZS3JwUurizEmttMTzkMkkpBVmdqDvko1XhdG2HJlOM4uIu%2BlfvuTMgMgOiXHRxad1ICyX8HKctfDqae73pig0ZiBglsAuaECGOvfq2On0YLPMpHH7oiBsaV7hhFyWj41EEuCnbDanzjHxhz1Q9QWa9uxiKr0wmSCE5k7eZu9Pc1cd0w6Evsw70UH95AssHxQhZC%2BfsIS6jh9yaNZ0zDrQd1QnJaKEm7keOlIaYemWz6e6pe%2FEnjD9vdeHS4fsc%2BmpqhAUX33Ci7s9D3ieP5LuhZqZvxc8N9NJzikrUEypmPZn7Ek%2BRiQ0ujYblsmFp6hbKeGlYeEB9B0yyKDEpJyX%2FbibpnQuQILP2eV%2FJsmiTa%2Flb%2FUrIl8w4sXvvAY6pgHCYYECOo5ScadcgpbmA1gHVLwbHmqQ85BimlCiySP84yvOlg6HVm%2FM9Hf0SYxGFPcEfDlTYUwx5%2FFwJ7UjSX%2FAwI2ci54dVTzka0llpIJGcXajg3lKdiEC3OeHj9JCo93%2B1J1%2FH7WQ6acULt3KhvMEE1Q7%2BGWFRooKi%2F%2F5gjrZ5zj9b0cpzrZEjKa%2BwwmUSPttFBo80H4QMa9El1Ssdy619AbKABED&X-Amz-Signature=fa085f9f5b74defa4bca58bb1c178bed70988b8409180500d586cb5a44180b02&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4DWPFU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4k84qiirKJhLTREpJESYJOz2%2BoP7RTfat%2FbFKmv4UCAiAnEib%2FrRz2h7zQ0tJR3cAJJsuLLpt9d%2Ber73ExJ48ndCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGeE1JSwNcWU1%2FTW1KtwDRxUNJXLqFw2huFqPTPM7umWk8HZKpWSMNlbQNETYZIH3TMDwn0RwX%2B7pPtrgucqlvsALlr2UKnXqlHFsbK0cmOtJr329KsRHXjbH28G1rqL2QVC%2BvAMdx8rLH4tSAjrR9FOQ%2F1%2BqSZ2atdX%2BIKjFJkx6DYcMbkk7z%2F0jOZdRZ6GIa5bE36bjoTAqO0lphPwaHZhU2jrBdjrwyapyF3teH%2Fk2BfDhskmDi2oDrWOTJ%2FHLew3e1xuvyTGBw1EzSRSvHP66XsyZS3JwUurizEmttMTzkMkkpBVmdqDvko1XhdG2HJlOM4uIu%2BlfvuTMgMgOiXHRxad1ICyX8HKctfDqae73pig0ZiBglsAuaECGOvfq2On0YLPMpHH7oiBsaV7hhFyWj41EEuCnbDanzjHxhz1Q9QWa9uxiKr0wmSCE5k7eZu9Pc1cd0w6Evsw70UH95AssHxQhZC%2BfsIS6jh9yaNZ0zDrQd1QnJaKEm7keOlIaYemWz6e6pe%2FEnjD9vdeHS4fsc%2BmpqhAUX33Ci7s9D3ieP5LuhZqZvxc8N9NJzikrUEypmPZn7Ek%2BRiQ0ujYblsmFp6hbKeGlYeEB9B0yyKDEpJyX%2FbibpnQuQILP2eV%2FJsmiTa%2Flb%2FUrIl8w4sXvvAY6pgHCYYECOo5ScadcgpbmA1gHVLwbHmqQ85BimlCiySP84yvOlg6HVm%2FM9Hf0SYxGFPcEfDlTYUwx5%2FFwJ7UjSX%2FAwI2ci54dVTzka0llpIJGcXajg3lKdiEC3OeHj9JCo93%2B1J1%2FH7WQ6acULt3KhvMEE1Q7%2BGWFRooKi%2F%2F5gjrZ5zj9b0cpzrZEjKa%2BwwmUSPttFBo80H4QMa9El1Ssdy619AbKABED&X-Amz-Signature=b1e87e289aee385f81f27533b16968cf11e2a8a8c72679ddabf6f7db617f9dea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4DWPFU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4k84qiirKJhLTREpJESYJOz2%2BoP7RTfat%2FbFKmv4UCAiAnEib%2FrRz2h7zQ0tJR3cAJJsuLLpt9d%2Ber73ExJ48ndCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGeE1JSwNcWU1%2FTW1KtwDRxUNJXLqFw2huFqPTPM7umWk8HZKpWSMNlbQNETYZIH3TMDwn0RwX%2B7pPtrgucqlvsALlr2UKnXqlHFsbK0cmOtJr329KsRHXjbH28G1rqL2QVC%2BvAMdx8rLH4tSAjrR9FOQ%2F1%2BqSZ2atdX%2BIKjFJkx6DYcMbkk7z%2F0jOZdRZ6GIa5bE36bjoTAqO0lphPwaHZhU2jrBdjrwyapyF3teH%2Fk2BfDhskmDi2oDrWOTJ%2FHLew3e1xuvyTGBw1EzSRSvHP66XsyZS3JwUurizEmttMTzkMkkpBVmdqDvko1XhdG2HJlOM4uIu%2BlfvuTMgMgOiXHRxad1ICyX8HKctfDqae73pig0ZiBglsAuaECGOvfq2On0YLPMpHH7oiBsaV7hhFyWj41EEuCnbDanzjHxhz1Q9QWa9uxiKr0wmSCE5k7eZu9Pc1cd0w6Evsw70UH95AssHxQhZC%2BfsIS6jh9yaNZ0zDrQd1QnJaKEm7keOlIaYemWz6e6pe%2FEnjD9vdeHS4fsc%2BmpqhAUX33Ci7s9D3ieP5LuhZqZvxc8N9NJzikrUEypmPZn7Ek%2BRiQ0ujYblsmFp6hbKeGlYeEB9B0yyKDEpJyX%2FbibpnQuQILP2eV%2FJsmiTa%2Flb%2FUrIl8w4sXvvAY6pgHCYYECOo5ScadcgpbmA1gHVLwbHmqQ85BimlCiySP84yvOlg6HVm%2FM9Hf0SYxGFPcEfDlTYUwx5%2FFwJ7UjSX%2FAwI2ci54dVTzka0llpIJGcXajg3lKdiEC3OeHj9JCo93%2B1J1%2FH7WQ6acULt3KhvMEE1Q7%2BGWFRooKi%2F%2F5gjrZ5zj9b0cpzrZEjKa%2BwwmUSPttFBo80H4QMa9El1Ssdy619AbKABED&X-Amz-Signature=5c366bdc247d71bda819680edd9eb397af6a46e546c9bd10cd6f98bc739dba6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4DWPFU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4k84qiirKJhLTREpJESYJOz2%2BoP7RTfat%2FbFKmv4UCAiAnEib%2FrRz2h7zQ0tJR3cAJJsuLLpt9d%2Ber73ExJ48ndCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGeE1JSwNcWU1%2FTW1KtwDRxUNJXLqFw2huFqPTPM7umWk8HZKpWSMNlbQNETYZIH3TMDwn0RwX%2B7pPtrgucqlvsALlr2UKnXqlHFsbK0cmOtJr329KsRHXjbH28G1rqL2QVC%2BvAMdx8rLH4tSAjrR9FOQ%2F1%2BqSZ2atdX%2BIKjFJkx6DYcMbkk7z%2F0jOZdRZ6GIa5bE36bjoTAqO0lphPwaHZhU2jrBdjrwyapyF3teH%2Fk2BfDhskmDi2oDrWOTJ%2FHLew3e1xuvyTGBw1EzSRSvHP66XsyZS3JwUurizEmttMTzkMkkpBVmdqDvko1XhdG2HJlOM4uIu%2BlfvuTMgMgOiXHRxad1ICyX8HKctfDqae73pig0ZiBglsAuaECGOvfq2On0YLPMpHH7oiBsaV7hhFyWj41EEuCnbDanzjHxhz1Q9QWa9uxiKr0wmSCE5k7eZu9Pc1cd0w6Evsw70UH95AssHxQhZC%2BfsIS6jh9yaNZ0zDrQd1QnJaKEm7keOlIaYemWz6e6pe%2FEnjD9vdeHS4fsc%2BmpqhAUX33Ci7s9D3ieP5LuhZqZvxc8N9NJzikrUEypmPZn7Ek%2BRiQ0ujYblsmFp6hbKeGlYeEB9B0yyKDEpJyX%2FbibpnQuQILP2eV%2FJsmiTa%2Flb%2FUrIl8w4sXvvAY6pgHCYYECOo5ScadcgpbmA1gHVLwbHmqQ85BimlCiySP84yvOlg6HVm%2FM9Hf0SYxGFPcEfDlTYUwx5%2FFwJ7UjSX%2FAwI2ci54dVTzka0llpIJGcXajg3lKdiEC3OeHj9JCo93%2B1J1%2FH7WQ6acULt3KhvMEE1Q7%2BGWFRooKi%2F%2F5gjrZ5zj9b0cpzrZEjKa%2BwwmUSPttFBo80H4QMa9El1Ssdy619AbKABED&X-Amz-Signature=304c1f26f6bd1b263ecb1854b526d768a570fd320951752ed926fc08dba9effa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4DWPFU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4k84qiirKJhLTREpJESYJOz2%2BoP7RTfat%2FbFKmv4UCAiAnEib%2FrRz2h7zQ0tJR3cAJJsuLLpt9d%2Ber73ExJ48ndCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGeE1JSwNcWU1%2FTW1KtwDRxUNJXLqFw2huFqPTPM7umWk8HZKpWSMNlbQNETYZIH3TMDwn0RwX%2B7pPtrgucqlvsALlr2UKnXqlHFsbK0cmOtJr329KsRHXjbH28G1rqL2QVC%2BvAMdx8rLH4tSAjrR9FOQ%2F1%2BqSZ2atdX%2BIKjFJkx6DYcMbkk7z%2F0jOZdRZ6GIa5bE36bjoTAqO0lphPwaHZhU2jrBdjrwyapyF3teH%2Fk2BfDhskmDi2oDrWOTJ%2FHLew3e1xuvyTGBw1EzSRSvHP66XsyZS3JwUurizEmttMTzkMkkpBVmdqDvko1XhdG2HJlOM4uIu%2BlfvuTMgMgOiXHRxad1ICyX8HKctfDqae73pig0ZiBglsAuaECGOvfq2On0YLPMpHH7oiBsaV7hhFyWj41EEuCnbDanzjHxhz1Q9QWa9uxiKr0wmSCE5k7eZu9Pc1cd0w6Evsw70UH95AssHxQhZC%2BfsIS6jh9yaNZ0zDrQd1QnJaKEm7keOlIaYemWz6e6pe%2FEnjD9vdeHS4fsc%2BmpqhAUX33Ci7s9D3ieP5LuhZqZvxc8N9NJzikrUEypmPZn7Ek%2BRiQ0ujYblsmFp6hbKeGlYeEB9B0yyKDEpJyX%2FbibpnQuQILP2eV%2FJsmiTa%2Flb%2FUrIl8w4sXvvAY6pgHCYYECOo5ScadcgpbmA1gHVLwbHmqQ85BimlCiySP84yvOlg6HVm%2FM9Hf0SYxGFPcEfDlTYUwx5%2FFwJ7UjSX%2FAwI2ci54dVTzka0llpIJGcXajg3lKdiEC3OeHj9JCo93%2B1J1%2FH7WQ6acULt3KhvMEE1Q7%2BGWFRooKi%2F%2F5gjrZ5zj9b0cpzrZEjKa%2BwwmUSPttFBo80H4QMa9El1Ssdy619AbKABED&X-Amz-Signature=e197483d5d50742a386c6459ef958eb4a2fec724052226fe048b50486b73df14&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W26I4YAU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGkvG7E1D7ySW%2Fu7UzIUGobAIS3OhHKtEjyA33r55SdpAiEAjVAO1ODYIXMUmsL%2BzdZi4AR1aDBrIRzTdxvhb6phBd4qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF8mNYbaiu1mHJUB%2FSrcAw2bovy3B1bOC1zDfC8XnNA0prku1rgfaxqleb6fFRQ1Tx3fM6dwVSumZKGNzdMZXVLv7asLCRfzIL4iIytTK7CYijPNbPL%2F2IS0slXIdwEYFiP9L8l9GaXLrf0OfYIbLwZhxFcDUEZwhp4Ed3WcEtmJcc0KZr41sQ486gq6eIMsKx7YtmeQZybqgJei0SoASpeSz4YD1ZZLXjZh2HfnyPL8YbwASWFsuWPiIHFP5C2cDdKEcllPHKcYOMfxoHpQ%2FZcV1dtBepVbsdCEeVPnrSZqJwdQiaWX60lxiZVWD0aWunaVSgH6CYobDNQ51tgzYrJuD5SUAagT1qpFTZRUjyOF8TptVc5jaPl9vblAkgbFfyDCPRneO0Jt%2BBxT%2FrWf%2BwZqveCv0AkxvrL%2FALVq13ITRPh4724ttMrgBPn%2F8Z%2FRT%2FyARimjdcYcvpInTsFN9VO4U2R4dC8PbYGVFuYy%2FFYfceGvXtaTO48Q7gDOFAl330TNthJleFIPnGEtDlpDsWCkhx01Ne%2FFI0M%2BMHVjcZaQ8wtfIFLuCqu7Pv5YsDgiYW89E7D6WK3jRF5JYQoOCUB%2BBGRHwRqAhm3e6DhUyxMPg4rI66nJKY6HE8cdQg2uuyZxJ%2BOxqaQStXAUMOTF77wGOqUB9N44okDr3vBhk7%2FNVxRSEs00pz1DDSIFAjGVqlMQS0Og5YHaN7wH7QdS9PFBPdvuTVeqFSxpbGn9X0R8YBGkMzzXY2DTtIhPJWWhX6OAsFdj%2BNqyM6pP9wyIiOMTf%2FgPLFCJg2yyQBQIBeQ3GllcwToG%2BocswMu4bgo5kJo%2Fhtv%2F40skuuci29wi65aNt7vIwa3yRMutYxO5EzRrlmaRoOm7vSEh&X-Amz-Signature=b5afbbb72ce2b7ac62b69f03edcae88ec990b7127287eb19cca6d4c64d0dbeca&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN6X7FYZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQz1GrcmEzyO3VhCP1ix79SFt8Pq3kYN%2FX60T5VhjxTAiAytNhVaIgnWo9ZilGvclm6CjifEdc1%2FOtsYqp7Py%2BCESqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCRQPJQH0vmWg3nPOKtwD2EM1IMRnZmE35UrCxWS2dUCmJYgs2dJJ6WbROv05f90PFyCp%2BsZDcbBQfH4zsf6l0UzeIhK%2BhW23Zd41DlVGcXD%2BIzS%2BO9xm%2BYEVm599S92Aw75YH%2FQyudlveqg4GsGbF%2FM3gu%2FH190Wu68SIM3W9F0by%2B%2FGa1MtekFKR%2BsJKNUgwLbmydEFnYq7HGVY8mmK8j6oX262is%2BtXyTG%2BN25E6qhIh2GaKqTNvo2WGrWwHnPEXCG%2BcHsYquGydPZOpu6MiEFAZfzUqTPTxm%2Bg9vla%2By4%2FkeF7MRL4QrvXIFsmo%2Fx%2FmFpHbmCy3foqRDYvwAFIWXR6kX05mr0I3XNUmCvIQoznG799y5NO9M4y%2FU8ngqZAWLiQEZsZnysnRrfzhIX0YlQF3Y%2BZEono%2FHz218zGagk68YX3Vn7WVRhidb%2F5F%2BZBNb2zxvnRNdUE3zed1yoBNkXHVg4X%2FI0p%2FMf8ZbnpHqFKFWo%2FF839ObLlq6%2FvSA3QkxxDLKwEs460dUV4ALWGy%2FjuKdpPMMJK5ijnHwuIw%2B0SNv8ZDFVg0G9JtHnnvElAcPRAzhsJJU0aazFOOvrA2PM2JxrbfnF6vNZ1QXmX5l%2FMgWJlfbRdYVJaBru1FUmUNqN%2F64K%2Br4uj%2FwwycXvvAY6pgHPbiUL%2B7Y%2BBCIs%2F%2BeXqQDFKG7CbKpYI%2F6lB%2Fvu%2BRBockbRkuhCi3MSHcrNY7QFfSGhq%2FQhvoPuQuwgAeXPdqpIMfgcznKJ%2BXjGRCejkrWASdGfQnUBASCI8vuwO%2B8x8ShQDKX%2BuC0fUQRdEyQmxO0SBt5pJW4sDtvWPE7aRybO34N1A4zAYsI%2FN9gieRyNAw1il9IsKPKEeKFOG6tAiSHC3LKeGCfo&X-Amz-Signature=6f68f201d8209ce331d2f9abe33dcec313806ed8a79e72c6f83a17d9183575de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4DWPFU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4k84qiirKJhLTREpJESYJOz2%2BoP7RTfat%2FbFKmv4UCAiAnEib%2FrRz2h7zQ0tJR3cAJJsuLLpt9d%2Ber73ExJ48ndCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGeE1JSwNcWU1%2FTW1KtwDRxUNJXLqFw2huFqPTPM7umWk8HZKpWSMNlbQNETYZIH3TMDwn0RwX%2B7pPtrgucqlvsALlr2UKnXqlHFsbK0cmOtJr329KsRHXjbH28G1rqL2QVC%2BvAMdx8rLH4tSAjrR9FOQ%2F1%2BqSZ2atdX%2BIKjFJkx6DYcMbkk7z%2F0jOZdRZ6GIa5bE36bjoTAqO0lphPwaHZhU2jrBdjrwyapyF3teH%2Fk2BfDhskmDi2oDrWOTJ%2FHLew3e1xuvyTGBw1EzSRSvHP66XsyZS3JwUurizEmttMTzkMkkpBVmdqDvko1XhdG2HJlOM4uIu%2BlfvuTMgMgOiXHRxad1ICyX8HKctfDqae73pig0ZiBglsAuaECGOvfq2On0YLPMpHH7oiBsaV7hhFyWj41EEuCnbDanzjHxhz1Q9QWa9uxiKr0wmSCE5k7eZu9Pc1cd0w6Evsw70UH95AssHxQhZC%2BfsIS6jh9yaNZ0zDrQd1QnJaKEm7keOlIaYemWz6e6pe%2FEnjD9vdeHS4fsc%2BmpqhAUX33Ci7s9D3ieP5LuhZqZvxc8N9NJzikrUEypmPZn7Ek%2BRiQ0ujYblsmFp6hbKeGlYeEB9B0yyKDEpJyX%2FbibpnQuQILP2eV%2FJsmiTa%2Flb%2FUrIl8w4sXvvAY6pgHCYYECOo5ScadcgpbmA1gHVLwbHmqQ85BimlCiySP84yvOlg6HVm%2FM9Hf0SYxGFPcEfDlTYUwx5%2FFwJ7UjSX%2FAwI2ci54dVTzka0llpIJGcXajg3lKdiEC3OeHj9JCo93%2B1J1%2FH7WQ6acULt3KhvMEE1Q7%2BGWFRooKi%2F%2F5gjrZ5zj9b0cpzrZEjKa%2BwwmUSPttFBo80H4QMa9El1Ssdy619AbKABED&X-Amz-Signature=ca62e843882773f6034d32109e983781ab0247cd2bffce1f25326a536bf4ab70&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4DWPFU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4k84qiirKJhLTREpJESYJOz2%2BoP7RTfat%2FbFKmv4UCAiAnEib%2FrRz2h7zQ0tJR3cAJJsuLLpt9d%2Ber73ExJ48ndCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGeE1JSwNcWU1%2FTW1KtwDRxUNJXLqFw2huFqPTPM7umWk8HZKpWSMNlbQNETYZIH3TMDwn0RwX%2B7pPtrgucqlvsALlr2UKnXqlHFsbK0cmOtJr329KsRHXjbH28G1rqL2QVC%2BvAMdx8rLH4tSAjrR9FOQ%2F1%2BqSZ2atdX%2BIKjFJkx6DYcMbkk7z%2F0jOZdRZ6GIa5bE36bjoTAqO0lphPwaHZhU2jrBdjrwyapyF3teH%2Fk2BfDhskmDi2oDrWOTJ%2FHLew3e1xuvyTGBw1EzSRSvHP66XsyZS3JwUurizEmttMTzkMkkpBVmdqDvko1XhdG2HJlOM4uIu%2BlfvuTMgMgOiXHRxad1ICyX8HKctfDqae73pig0ZiBglsAuaECGOvfq2On0YLPMpHH7oiBsaV7hhFyWj41EEuCnbDanzjHxhz1Q9QWa9uxiKr0wmSCE5k7eZu9Pc1cd0w6Evsw70UH95AssHxQhZC%2BfsIS6jh9yaNZ0zDrQd1QnJaKEm7keOlIaYemWz6e6pe%2FEnjD9vdeHS4fsc%2BmpqhAUX33Ci7s9D3ieP5LuhZqZvxc8N9NJzikrUEypmPZn7Ek%2BRiQ0ujYblsmFp6hbKeGlYeEB9B0yyKDEpJyX%2FbibpnQuQILP2eV%2FJsmiTa%2Flb%2FUrIl8w4sXvvAY6pgHCYYECOo5ScadcgpbmA1gHVLwbHmqQ85BimlCiySP84yvOlg6HVm%2FM9Hf0SYxGFPcEfDlTYUwx5%2FFwJ7UjSX%2FAwI2ci54dVTzka0llpIJGcXajg3lKdiEC3OeHj9JCo93%2B1J1%2FH7WQ6acULt3KhvMEE1Q7%2BGWFRooKi%2F%2F5gjrZ5zj9b0cpzrZEjKa%2BwwmUSPttFBo80H4QMa9El1Ssdy619AbKABED&X-Amz-Signature=c8f93723ce59eb3b5427c1d2fae2856848852213627ae4ca748df6771b6c2c8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4DWPFU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF4k84qiirKJhLTREpJESYJOz2%2BoP7RTfat%2FbFKmv4UCAiAnEib%2FrRz2h7zQ0tJR3cAJJsuLLpt9d%2Ber73ExJ48ndCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGeE1JSwNcWU1%2FTW1KtwDRxUNJXLqFw2huFqPTPM7umWk8HZKpWSMNlbQNETYZIH3TMDwn0RwX%2B7pPtrgucqlvsALlr2UKnXqlHFsbK0cmOtJr329KsRHXjbH28G1rqL2QVC%2BvAMdx8rLH4tSAjrR9FOQ%2F1%2BqSZ2atdX%2BIKjFJkx6DYcMbkk7z%2F0jOZdRZ6GIa5bE36bjoTAqO0lphPwaHZhU2jrBdjrwyapyF3teH%2Fk2BfDhskmDi2oDrWOTJ%2FHLew3e1xuvyTGBw1EzSRSvHP66XsyZS3JwUurizEmttMTzkMkkpBVmdqDvko1XhdG2HJlOM4uIu%2BlfvuTMgMgOiXHRxad1ICyX8HKctfDqae73pig0ZiBglsAuaECGOvfq2On0YLPMpHH7oiBsaV7hhFyWj41EEuCnbDanzjHxhz1Q9QWa9uxiKr0wmSCE5k7eZu9Pc1cd0w6Evsw70UH95AssHxQhZC%2BfsIS6jh9yaNZ0zDrQd1QnJaKEm7keOlIaYemWz6e6pe%2FEnjD9vdeHS4fsc%2BmpqhAUX33Ci7s9D3ieP5LuhZqZvxc8N9NJzikrUEypmPZn7Ek%2BRiQ0ujYblsmFp6hbKeGlYeEB9B0yyKDEpJyX%2FbibpnQuQILP2eV%2FJsmiTa%2Flb%2FUrIl8w4sXvvAY6pgHCYYECOo5ScadcgpbmA1gHVLwbHmqQ85BimlCiySP84yvOlg6HVm%2FM9Hf0SYxGFPcEfDlTYUwx5%2FFwJ7UjSX%2FAwI2ci54dVTzka0llpIJGcXajg3lKdiEC3OeHj9JCo93%2B1J1%2FH7WQ6acULt3KhvMEE1Q7%2BGWFRooKi%2F%2F5gjrZ5zj9b0cpzrZEjKa%2BwwmUSPttFBo80H4QMa9El1Ssdy619AbKABED&X-Amz-Signature=6b2785acef5e17d08011ea87bec132e73e0a47270a375c98123ffd728f267db0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDDEMW5Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBQ2Ilc9ofKw7QVc6aKb8WzaSNFeRWMOYDmaF4%2Fh8wt4AiBLlTY%2BGR2klxrUhQaMLVil8PfD2E%2FLDvK0HuHCCURS%2BSqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8XfJBznifU4yin%2FqKtwDszKf3tliFnBRVdFaPkaOw6GMWXaoHp5r1DENbRXr2zxbMe4deJ0Df2MdZjhlOP%2FC7TAvkq34sxRLFWt1JfGBdxXnBsHqqzzpTysAZ56i1D7iru1IijwR%2B9G6GQvPubjHCvhZQJQUtIj96t%2Fiq44iMwJ21cwC1trIj8pzU3LIQJTYWtShz%2FvE%2FO3NO%2FqfM6pjQ58G2UVi2Xw4y4x%2FQHg3vwrzVb9m%2BBfUm835HyvGEp948FWbF7p4XfcXtK%2Ff351v82rQA8MjwxeoZ108KvPD5UkZve58XHJ1q49Di9hhIktQ1gpwryrtL06IlL3iynZKNakcmwJyraUAq9xEaXF6Bv3B5nlb1nFiYqvYsbgOrIFVVV9GW2q7x5tj%2B1qWl%2FYRCC0SADcOmW4iaZKm2bOsJxlzlVbkmrxx50BhELVMm4ZU1VEGrajftwkcyR%2Bbj8CXJCbmsa%2FynfI0kBkdrxPe3nIBxGImv7OLQyoxzHIlYDoGvW1s%2B2%2BWNaTYpViktrJjrYoPUqQ%2BzhlxLVJyEuwPvmUWCfnL2%2BMCYdYEQ%2ByUY1grYq3mbQK8aJahqD4mArPZWPQysVIDAus5dOk9v2i5PyIDmKe93Dc2PHiCa401BufTw0NNAsb8w7yj4aEw5MXvvAY6pgEuW7WToqIHmroQd4AaRJ5795vuH%2BMvjd3XflaiFH5YCRhdjvpa435q6OJRkRESRXf7k1CfJsa79Kl3M8PH%2BKgEq9OOkCRXb3m7kmTn4Sulfiv193tWS2N%2FdQ1NX6ekjeysocvUitBNbwQH9gM9i8bseX4EG5598XYCEuJCcr8RgBFtEyDlPR5krxQ%2FLopighgHaq4aRx4hx0S2yOSwnWaZiqpPpZqI&X-Amz-Signature=df27370276e8b4a0b8bdf2507107614f302ec3df4c12eb08413c06bbd354deaa&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJWKJQA6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICfEtVEnV5XH2kRYgg0fjfYL9fqCtyZGPWCUs76MEE1qAiAkGR90yAaDXSjfc5F0hnn1vsE58O1Po5dWOAlXuvuYgSqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM98DEJPwas%2B%2Bjpm0EKtwDmPiBvVCvQRJhgdfqD5sjNqiGGSYSOJy%2F08NEK0ocBy0dLSv5s5ZefeEscBnfRXYZWBrlM7aNwq3H41cmqwDAH8T6xKfLACg1AARO9CdgvKFTYPp5A%2BlT9LXspYBTWaolK6F8TvDHJEwxgz2IwKWRTz3kZ43eZTS9C6fcll5HDAv%2B6Z5%2BWcXDMDO1UKH%2FZmQVsK6%2BNWF7qLeUbYzi8h6yUcx58XYKCgPgJbtgI%2BZ2qsjzzP6Cq1Db2HpgAKd0xGOfakCSSFpBy0xcH3%2F5qXalO72ymF4GG%2FNECWI55nTbg8mT49MFqs21WUR8T2mpDL4xdZwXZuSvQUC2P6ti8FqRGMOPVxRNNAWAc1WAnObDpzrK7vmqpqyQr3o6QtAqZRcUeTBkDweL6wOb8U%2FybgekDj9vYf%2FvSZYqPH5yXDKhwGHUDkdhb1mGiE0yLbXDplmj6m5e1YCj4m9bTAUaKKLI3%2FY0mFGUEWo%2Ff2qFEQd9XS9QxR6yFdUMaMLiq%2BR3sdTYlaodhOr%2BAG3iW3B22zgUSY2yQJ9ALy4QMTJzCeX0cT47XE9ke8MhnDYuFb7m%2FwpyE4fy447o0l0L9ivHI8tf45RWOORu%2FIpIHucS5k%2BhX4E6pzLUsKILgYV1QsEwnMXvvAY6pgFKCQg0KeY0%2FvfEjnEnXV%2BLv2JrZ1fTdSpmEq9JCnCQzBSxzaHWjZgfcJBM%2BfXJs7vyDgEyEb%2F%2FlhGXXKpIJzCE4XjL7IULst17h68G0OAdjUyP3WDcpLPVg5pf6PPUmdaPr8NCuEP5W25YuE0AE6F%2FSHGHmMFH7R4X0Z7UGXLcwg8j9V9bZIvABHbmbALavu1Idj3Is7vGYHggtTErxqAzYSdu6yox&X-Amz-Signature=7719edfa0facd02e4d2c7a45b0e511fc1da13d0f0bb2ae541067b49f9bd0d7de&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BFV52Z4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICaRAEhIHFCh7S%2Boyj2RKBFgATk%2F5wYbbzDiV2%2F9HchJAiA8iz8J%2FfqhfX4dCGnblBiZTx8nSfdqSn0QyzUxera1UCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGL%2FY%2FZ5TyA3%2FggM8KtwDhPxgK2tphkAOQjxaNBNQkm8rnRlh%2FEY2mp74aLdhMSQulEgSVXq6gZ7wM7H5m5uklSGkidnMnRadNXj8YO72mfle5WpY7%2FTLS7j%2FF%2BI9dhN0DuDjDuSNyW48mbw%2BYYVRjJNpL6mhvBYzrRiCTXjoRmivp6kCWx2VbNC3pyTRoAZsmjTBG6r7FTOts4mAt3sYBB6Vwdxo4ZD72k9Kk65LGquPrRgkw4E9SQFAUICRI5F4r4JbRzHZfGervMOUt8jFclGyMqaEjzAdRq0apcsGE2rN%2BLyacRwtOPTk%2B%2F20lsVn2qq1S6Z7rPwf0ortjEax9a%2F1g41ITsG097J1uwRIjBfS5VHL1C53zZNy0Z4NDmH%2Fv31U4130VQI090HN2trpQAQAddlYbV9vCkiz83uVNcUaETTGLUwGMyR%2Ff9XlFE4iKnt80Fo3fvAjMFPcpRQsn2dlRugHlxXe3bMrYR4OkRN8z74%2BhS8Q0dgmxqzd6it849uhysn5NEFGu%2FOP6mjJ%2B1zALgtG0fmpgHp3Yx%2FmOqnG3OoggVQoRdZcJ1uU9she0Om1DKdYrIxGArw%2FjS5mN3RKLRpLw%2BU%2Fb%2BSoOr%2F9FDHrH2TNoCygCydh3toC4r6Rf2scxVraO%2BssH2Awk8bvvAY6pgEErN0Xs3y9H540Zc9%2BJS9qFAP5LEg0S%2BHRz9fEMp%2Bst0qH9fFQ2iSTwFCOGwZ6lqngDDAbRiYjWe8wgwGB9Vifggwc7zsO%2FS23IrAkLIpDD3u9gkem1RrncJSf45MvZV1125G0qI1uNET%2FPFy5t%2Fa8xUbT8rD6aD5pPDVo%2FyzXQHkKpBX1nWN9PjtfUJT8vES7gwwcU81T9nCd7evkFETYCxktWV5E&X-Amz-Signature=86b3450fa54dd0d662e67b3230a084b6702d803e088b1ddcfa933d718012cc43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAIGWH56%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNXYv2h%2BbNBg1jWNYZTIfZGBmNnBgKZDJXVyXzGdXwTQIgbIcdxI3yqHCwvUNFIG6yHcGq3YtqNFAyn%2FmCd4jWDlkqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIlMLkAZrYBf7midCrcA4YqFJ4jwXjylysrqHEeCf04bMrDd0wX6yhMGauuZ%2BPS2xc6RyyfxWLzoD4PCUo1dvePosMc8FcztJj4d0zwVhGjuM9mZxUozMquA8%2B0tddYETB25Cj2E0AwiVP1t0NIfDkWyHjLm8BT26lHarpdDAzKYSLR%2BWx%2FBQLPvxijE%2FFGecqJ4EXS5%2BEJMTP9GXIfR60LAK68SgUkOx9s6ccgXwH5riPW8HAVde9SFIRhrth45xzqtRLGUVGUW3GKo6u5A9rfXf6FvZN6s3yIqKiJP1QTG2L4UN%2F3l6yffGPQnI0sGA6IXQRg89Viv03C%2Bu6PSPsog7N5DE7CHhF2Z9EuEiiBg26lq7RWF8%2BGWPM24tgklybOvYUWdEcbc%2BvKkkmgb9qYAP%2F%2Ffjh5PZODPCMSa63A0MLve%2BTz3a0EJCE1EBWdpvgTPSWTQQaH3X2tid5i4drbxQ918kDYqGhZfw4zJAqluf4CONaRywHDy9yTBuSB7ORFH8qL6gYlur7lVfc%2F973h5VE0tvrGZ0q4jT1%2FzJ%2B%2BIEcKgWPwA%2F7yxrcYXq0xbKQzhDUfOcDiyCl9e%2FIbguGZUX4tjpVklXnZboLq5dIiOoXs2me4ZRKMtrtBa%2Baek%2F5S4xC8g8GKZvZ1MIbF77wGOqUBat0IE08DC%2FREDpekw8aBZETTSnA4LZip%2FZio5FN74G%2FVZa4Tn1didWNbnbtBMudCBA8Z04OwnaeucJmPb7ELwTLgw01FF%2Bpz4MrlTKSS9XhIWgR5VY%2BuZKbWKhdD%2B9NU5oGlAh%2BPPrbhhYXuFMdInn8cRclYkEroc%2Fqy3942go1drOliHVrLlpKzF5CTG7Mm5V4h7h1w44w2kCe%2F0BMIUM6W7IOB&X-Amz-Signature=b69a23329fa8e7f4d486a6e466fbf00e1b77c31b92bab12492d8adc6569cba79&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAIGWH56%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNXYv2h%2BbNBg1jWNYZTIfZGBmNnBgKZDJXVyXzGdXwTQIgbIcdxI3yqHCwvUNFIG6yHcGq3YtqNFAyn%2FmCd4jWDlkqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIlMLkAZrYBf7midCrcA4YqFJ4jwXjylysrqHEeCf04bMrDd0wX6yhMGauuZ%2BPS2xc6RyyfxWLzoD4PCUo1dvePosMc8FcztJj4d0zwVhGjuM9mZxUozMquA8%2B0tddYETB25Cj2E0AwiVP1t0NIfDkWyHjLm8BT26lHarpdDAzKYSLR%2BWx%2FBQLPvxijE%2FFGecqJ4EXS5%2BEJMTP9GXIfR60LAK68SgUkOx9s6ccgXwH5riPW8HAVde9SFIRhrth45xzqtRLGUVGUW3GKo6u5A9rfXf6FvZN6s3yIqKiJP1QTG2L4UN%2F3l6yffGPQnI0sGA6IXQRg89Viv03C%2Bu6PSPsog7N5DE7CHhF2Z9EuEiiBg26lq7RWF8%2BGWPM24tgklybOvYUWdEcbc%2BvKkkmgb9qYAP%2F%2Ffjh5PZODPCMSa63A0MLve%2BTz3a0EJCE1EBWdpvgTPSWTQQaH3X2tid5i4drbxQ918kDYqGhZfw4zJAqluf4CONaRywHDy9yTBuSB7ORFH8qL6gYlur7lVfc%2F973h5VE0tvrGZ0q4jT1%2FzJ%2B%2BIEcKgWPwA%2F7yxrcYXq0xbKQzhDUfOcDiyCl9e%2FIbguGZUX4tjpVklXnZboLq5dIiOoXs2me4ZRKMtrtBa%2Baek%2F5S4xC8g8GKZvZ1MIbF77wGOqUBat0IE08DC%2FREDpekw8aBZETTSnA4LZip%2FZio5FN74G%2FVZa4Tn1didWNbnbtBMudCBA8Z04OwnaeucJmPb7ELwTLgw01FF%2Bpz4MrlTKSS9XhIWgR5VY%2BuZKbWKhdD%2B9NU5oGlAh%2BPPrbhhYXuFMdInn8cRclYkEroc%2Fqy3942go1drOliHVrLlpKzF5CTG7Mm5V4h7h1w44w2kCe%2F0BMIUM6W7IOB&X-Amz-Signature=ecb15ffc3092fb6c54ebfb10c1c20abf2065472fc16917645573d5dc67582853&X-Amz-SignedHeaders=host&x-id=GetObject)

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
