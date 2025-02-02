

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY6LQXZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9MhOp3dupUAOL4YhYn2PGgduda99Su7hJsivzmf6b%2FAiBGnJQKQumjz1D3j3Ys2YUpKwlM4MbG3oA6LDqv%2BaPYaSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEEsUHU0jSIDk82tYKtwDSdZ%2F%2FUreFJqIv1CYBZNshN3tIibmydljtowipD0ehIe36OjqpWR%2FE5GKzm9tCNVGE8hBRaJ5tJv5RnRRLL%2BPys1h0R%2FLI5KuOsp10nUUJelrYyhgSXpx7whwylQnFPURIcMGU6zFPtVbpbhqLxnS4Rpw6LP3roSoAmJfxCpETBWJbC2AgLMMuRbdr8MjOlFFgr8bBKRSPwHwXWKjpKi74SRFSIqjehZateN2RCQCqMjiylOp7fYUlx58mCtrUo%2FNhZhMHOPoJ2Fxqi8YwyAgYB%2F2HzE5JAeJfnnqKeaAkzSP%2BZt5Fb%2FBNILwBPlrAOjsMFxAsQL6zOFmWpmLJJfqjUerl8siOqeIc3vx7FPcwqhdQuWp7OFloJA40lTW3MQGOoPRUz%2BPxywrCB3mefeCKrpLBo%2FUNUh92NaTsf66oOJGL%2BHQOmEsszttzqsbc7ZpDQ8wcfuiFOtwHOd7JiqO9nW46XtXZWMF7CviP6XERmb0lwSRlAiK%2BEX8cFHCYPZBpi6v%2FRYOESezWs63jt4ELyS%2BKeJeub2FVXlJaqjsMyC2MRcXTtGDj5Tts9Avsgss58sw3JTFYPK5IjyHrFx6uDJGycJnzRf2K%2F7Kkmj8f%2F6VrZ4abutmcuw2O2wwmLr9vAY6pgGsqEknP5fP6T5bu%2FyvIqSZgrlQ4PFptZpL9joEx14StnmbdRIodR3rAYx94AdoAuX28uOCezzvnv0TmasEbVnNOiBy4zAipqYH374rLj3EMpnl8iI3UMQK7iDEkFzW5QHp9MDtVeeShQJonS6P2dKm1h29J%2BMvjVRqbzWB4mKI64CrBREzPzYq7IlyLKgJRmBLOU6NI0GxxtY3B0F73OK1vnGBa1LK&X-Amz-Signature=dd269cf5e56bcdcd8f4fb2731ad0c1d3963ad2eec8e7e2224702427b4086064e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY6LQXZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9MhOp3dupUAOL4YhYn2PGgduda99Su7hJsivzmf6b%2FAiBGnJQKQumjz1D3j3Ys2YUpKwlM4MbG3oA6LDqv%2BaPYaSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEEsUHU0jSIDk82tYKtwDSdZ%2F%2FUreFJqIv1CYBZNshN3tIibmydljtowipD0ehIe36OjqpWR%2FE5GKzm9tCNVGE8hBRaJ5tJv5RnRRLL%2BPys1h0R%2FLI5KuOsp10nUUJelrYyhgSXpx7whwylQnFPURIcMGU6zFPtVbpbhqLxnS4Rpw6LP3roSoAmJfxCpETBWJbC2AgLMMuRbdr8MjOlFFgr8bBKRSPwHwXWKjpKi74SRFSIqjehZateN2RCQCqMjiylOp7fYUlx58mCtrUo%2FNhZhMHOPoJ2Fxqi8YwyAgYB%2F2HzE5JAeJfnnqKeaAkzSP%2BZt5Fb%2FBNILwBPlrAOjsMFxAsQL6zOFmWpmLJJfqjUerl8siOqeIc3vx7FPcwqhdQuWp7OFloJA40lTW3MQGOoPRUz%2BPxywrCB3mefeCKrpLBo%2FUNUh92NaTsf66oOJGL%2BHQOmEsszttzqsbc7ZpDQ8wcfuiFOtwHOd7JiqO9nW46XtXZWMF7CviP6XERmb0lwSRlAiK%2BEX8cFHCYPZBpi6v%2FRYOESezWs63jt4ELyS%2BKeJeub2FVXlJaqjsMyC2MRcXTtGDj5Tts9Avsgss58sw3JTFYPK5IjyHrFx6uDJGycJnzRf2K%2F7Kkmj8f%2F6VrZ4abutmcuw2O2wwmLr9vAY6pgGsqEknP5fP6T5bu%2FyvIqSZgrlQ4PFptZpL9joEx14StnmbdRIodR3rAYx94AdoAuX28uOCezzvnv0TmasEbVnNOiBy4zAipqYH374rLj3EMpnl8iI3UMQK7iDEkFzW5QHp9MDtVeeShQJonS6P2dKm1h29J%2BMvjVRqbzWB4mKI64CrBREzPzYq7IlyLKgJRmBLOU6NI0GxxtY3B0F73OK1vnGBa1LK&X-Amz-Signature=7f818bb517b157aea78ccd1ca39328b69d705c28cc91fb69effdcfb5cc316dc3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY6LQXZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9MhOp3dupUAOL4YhYn2PGgduda99Su7hJsivzmf6b%2FAiBGnJQKQumjz1D3j3Ys2YUpKwlM4MbG3oA6LDqv%2BaPYaSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEEsUHU0jSIDk82tYKtwDSdZ%2F%2FUreFJqIv1CYBZNshN3tIibmydljtowipD0ehIe36OjqpWR%2FE5GKzm9tCNVGE8hBRaJ5tJv5RnRRLL%2BPys1h0R%2FLI5KuOsp10nUUJelrYyhgSXpx7whwylQnFPURIcMGU6zFPtVbpbhqLxnS4Rpw6LP3roSoAmJfxCpETBWJbC2AgLMMuRbdr8MjOlFFgr8bBKRSPwHwXWKjpKi74SRFSIqjehZateN2RCQCqMjiylOp7fYUlx58mCtrUo%2FNhZhMHOPoJ2Fxqi8YwyAgYB%2F2HzE5JAeJfnnqKeaAkzSP%2BZt5Fb%2FBNILwBPlrAOjsMFxAsQL6zOFmWpmLJJfqjUerl8siOqeIc3vx7FPcwqhdQuWp7OFloJA40lTW3MQGOoPRUz%2BPxywrCB3mefeCKrpLBo%2FUNUh92NaTsf66oOJGL%2BHQOmEsszttzqsbc7ZpDQ8wcfuiFOtwHOd7JiqO9nW46XtXZWMF7CviP6XERmb0lwSRlAiK%2BEX8cFHCYPZBpi6v%2FRYOESezWs63jt4ELyS%2BKeJeub2FVXlJaqjsMyC2MRcXTtGDj5Tts9Avsgss58sw3JTFYPK5IjyHrFx6uDJGycJnzRf2K%2F7Kkmj8f%2F6VrZ4abutmcuw2O2wwmLr9vAY6pgGsqEknP5fP6T5bu%2FyvIqSZgrlQ4PFptZpL9joEx14StnmbdRIodR3rAYx94AdoAuX28uOCezzvnv0TmasEbVnNOiBy4zAipqYH374rLj3EMpnl8iI3UMQK7iDEkFzW5QHp9MDtVeeShQJonS6P2dKm1h29J%2BMvjVRqbzWB4mKI64CrBREzPzYq7IlyLKgJRmBLOU6NI0GxxtY3B0F73OK1vnGBa1LK&X-Amz-Signature=97fca750e92284dbf4d081271744f8a31e275dd1b786b1fc77de39dae56938bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNZBJPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmEcIVCNsimvbNZ%2FQVTDIosK6s%2BV94aA2yvfnP9f7dAAiA3xgzFnMHAFtfgS8Onz0S6d1E8TcKky1YytLvx4KNygyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp2wllEZRc9CNIymiKtwDVV7iEinZyafGWvyRdNzlfj4qHFuH1vlxnlI6KkWQhISc6kX%2BS%2Fs4LqM0kuSMOmluldMd6PBsSfd7LWOG%2FdAOox%2BbLhhSdWl2OsrGwvKJNnVrFBXyYW%2Bi3K8qJR7RNt5aIdrFkIj3DAGNzVx3zX7ayXn7KRFuACPwA1fwxnhNxOiVUATRsGNvmD48miYkkGOsj7pWd0cWQA%2Bc17RWQD653W%2Fvkom09LGBv3AOsyTrk%2F%2B%2FnNTBpuDdmVZAYzc3cjc7P8Z832GTEYgf%2B1qoeuZMb2Kvti7Lxcvr0S5GDAUZvQ7BLDgeWZRUwcfWHwQO%2BDtAaxbAqo%2F0nSj%2Bc3P1JyNRUxxC7O%2BtfQBHmqMnxSzaqIuxdWmf8iJtk3wr%2FP0YJoh3BxwAmQijwLskVeDUl28ayTvxsCVDxrAbasLcxXkr6CuPkQQw5TmYRYNHyxg36INTeq7y79G5j1ZH4krlkifX4HZTIC%2B0G2wPEd8Bks%2FQRLhq4JRhllqPcFpRHCQc9cibJhEX6A2HalFU%2Fkasu%2BMCWNFZ3kFlEq0Uw8RP%2F5qI6zUKw%2Bc2k9XnH89DaKftu%2BpZjC46QxiXKWduCBqArpzMYFfEJB2pxsHJxtbxuwYWvfCXdkKqq7pRYbdKb0owxLb9vAY6pgGkW3EACeLxGFJwh%2BC%2B8ip%2B%2BMbd%2FLj0SwL8jRl1EiGggBX5O1EKRSUg2qPSsaDFnKkV5hGr8tqPeJATRKONpEphWQEYbXbdJaFnFMeMM8JVM7ADEi2mvCdeYy%2B08xXzDiFEAD20Tnx1N8rM%2BelDj0Oj9b%2FwgHnd%2FN4DQ0CAsQQvMeHZIvHSyLceU1Iuqy%2BgkpPkYnsvHLCgwekr5VWb90RdNW2HSHEH&X-Amz-Signature=b698e2f17e334d5eb12686ca6c2e969ee5f7b905dffad415b7c70591625deb58&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNZBJPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmEcIVCNsimvbNZ%2FQVTDIosK6s%2BV94aA2yvfnP9f7dAAiA3xgzFnMHAFtfgS8Onz0S6d1E8TcKky1YytLvx4KNygyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp2wllEZRc9CNIymiKtwDVV7iEinZyafGWvyRdNzlfj4qHFuH1vlxnlI6KkWQhISc6kX%2BS%2Fs4LqM0kuSMOmluldMd6PBsSfd7LWOG%2FdAOox%2BbLhhSdWl2OsrGwvKJNnVrFBXyYW%2Bi3K8qJR7RNt5aIdrFkIj3DAGNzVx3zX7ayXn7KRFuACPwA1fwxnhNxOiVUATRsGNvmD48miYkkGOsj7pWd0cWQA%2Bc17RWQD653W%2Fvkom09LGBv3AOsyTrk%2F%2B%2FnNTBpuDdmVZAYzc3cjc7P8Z832GTEYgf%2B1qoeuZMb2Kvti7Lxcvr0S5GDAUZvQ7BLDgeWZRUwcfWHwQO%2BDtAaxbAqo%2F0nSj%2Bc3P1JyNRUxxC7O%2BtfQBHmqMnxSzaqIuxdWmf8iJtk3wr%2FP0YJoh3BxwAmQijwLskVeDUl28ayTvxsCVDxrAbasLcxXkr6CuPkQQw5TmYRYNHyxg36INTeq7y79G5j1ZH4krlkifX4HZTIC%2B0G2wPEd8Bks%2FQRLhq4JRhllqPcFpRHCQc9cibJhEX6A2HalFU%2Fkasu%2BMCWNFZ3kFlEq0Uw8RP%2F5qI6zUKw%2Bc2k9XnH89DaKftu%2BpZjC46QxiXKWduCBqArpzMYFfEJB2pxsHJxtbxuwYWvfCXdkKqq7pRYbdKb0owxLb9vAY6pgGkW3EACeLxGFJwh%2BC%2B8ip%2B%2BMbd%2FLj0SwL8jRl1EiGggBX5O1EKRSUg2qPSsaDFnKkV5hGr8tqPeJATRKONpEphWQEYbXbdJaFnFMeMM8JVM7ADEi2mvCdeYy%2B08xXzDiFEAD20Tnx1N8rM%2BelDj0Oj9b%2FwgHnd%2FN4DQ0CAsQQvMeHZIvHSyLceU1Iuqy%2BgkpPkYnsvHLCgwekr5VWb90RdNW2HSHEH&X-Amz-Signature=ec1af14eb4b12919c99d3b122a7f25a2c0debb012b66091bb959235e129f134f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNZBJPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmEcIVCNsimvbNZ%2FQVTDIosK6s%2BV94aA2yvfnP9f7dAAiA3xgzFnMHAFtfgS8Onz0S6d1E8TcKky1YytLvx4KNygyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp2wllEZRc9CNIymiKtwDVV7iEinZyafGWvyRdNzlfj4qHFuH1vlxnlI6KkWQhISc6kX%2BS%2Fs4LqM0kuSMOmluldMd6PBsSfd7LWOG%2FdAOox%2BbLhhSdWl2OsrGwvKJNnVrFBXyYW%2Bi3K8qJR7RNt5aIdrFkIj3DAGNzVx3zX7ayXn7KRFuACPwA1fwxnhNxOiVUATRsGNvmD48miYkkGOsj7pWd0cWQA%2Bc17RWQD653W%2Fvkom09LGBv3AOsyTrk%2F%2B%2FnNTBpuDdmVZAYzc3cjc7P8Z832GTEYgf%2B1qoeuZMb2Kvti7Lxcvr0S5GDAUZvQ7BLDgeWZRUwcfWHwQO%2BDtAaxbAqo%2F0nSj%2Bc3P1JyNRUxxC7O%2BtfQBHmqMnxSzaqIuxdWmf8iJtk3wr%2FP0YJoh3BxwAmQijwLskVeDUl28ayTvxsCVDxrAbasLcxXkr6CuPkQQw5TmYRYNHyxg36INTeq7y79G5j1ZH4krlkifX4HZTIC%2B0G2wPEd8Bks%2FQRLhq4JRhllqPcFpRHCQc9cibJhEX6A2HalFU%2Fkasu%2BMCWNFZ3kFlEq0Uw8RP%2F5qI6zUKw%2Bc2k9XnH89DaKftu%2BpZjC46QxiXKWduCBqArpzMYFfEJB2pxsHJxtbxuwYWvfCXdkKqq7pRYbdKb0owxLb9vAY6pgGkW3EACeLxGFJwh%2BC%2B8ip%2B%2BMbd%2FLj0SwL8jRl1EiGggBX5O1EKRSUg2qPSsaDFnKkV5hGr8tqPeJATRKONpEphWQEYbXbdJaFnFMeMM8JVM7ADEi2mvCdeYy%2B08xXzDiFEAD20Tnx1N8rM%2BelDj0Oj9b%2FwgHnd%2FN4DQ0CAsQQvMeHZIvHSyLceU1Iuqy%2BgkpPkYnsvHLCgwekr5VWb90RdNW2HSHEH&X-Amz-Signature=9480c4c1c405dc5c70395b4a03a8a25282621ef1dacf7b33e029931b55ce9eb5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNZBJPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmEcIVCNsimvbNZ%2FQVTDIosK6s%2BV94aA2yvfnP9f7dAAiA3xgzFnMHAFtfgS8Onz0S6d1E8TcKky1YytLvx4KNygyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp2wllEZRc9CNIymiKtwDVV7iEinZyafGWvyRdNzlfj4qHFuH1vlxnlI6KkWQhISc6kX%2BS%2Fs4LqM0kuSMOmluldMd6PBsSfd7LWOG%2FdAOox%2BbLhhSdWl2OsrGwvKJNnVrFBXyYW%2Bi3K8qJR7RNt5aIdrFkIj3DAGNzVx3zX7ayXn7KRFuACPwA1fwxnhNxOiVUATRsGNvmD48miYkkGOsj7pWd0cWQA%2Bc17RWQD653W%2Fvkom09LGBv3AOsyTrk%2F%2B%2FnNTBpuDdmVZAYzc3cjc7P8Z832GTEYgf%2B1qoeuZMb2Kvti7Lxcvr0S5GDAUZvQ7BLDgeWZRUwcfWHwQO%2BDtAaxbAqo%2F0nSj%2Bc3P1JyNRUxxC7O%2BtfQBHmqMnxSzaqIuxdWmf8iJtk3wr%2FP0YJoh3BxwAmQijwLskVeDUl28ayTvxsCVDxrAbasLcxXkr6CuPkQQw5TmYRYNHyxg36INTeq7y79G5j1ZH4krlkifX4HZTIC%2B0G2wPEd8Bks%2FQRLhq4JRhllqPcFpRHCQc9cibJhEX6A2HalFU%2Fkasu%2BMCWNFZ3kFlEq0Uw8RP%2F5qI6zUKw%2Bc2k9XnH89DaKftu%2BpZjC46QxiXKWduCBqArpzMYFfEJB2pxsHJxtbxuwYWvfCXdkKqq7pRYbdKb0owxLb9vAY6pgGkW3EACeLxGFJwh%2BC%2B8ip%2B%2BMbd%2FLj0SwL8jRl1EiGggBX5O1EKRSUg2qPSsaDFnKkV5hGr8tqPeJATRKONpEphWQEYbXbdJaFnFMeMM8JVM7ADEi2mvCdeYy%2B08xXzDiFEAD20Tnx1N8rM%2BelDj0Oj9b%2FwgHnd%2FN4DQ0CAsQQvMeHZIvHSyLceU1Iuqy%2BgkpPkYnsvHLCgwekr5VWb90RdNW2HSHEH&X-Amz-Signature=45637de9e15578b476d012d48907ff5ab70552f7026620b792db7e566f8f2bbb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNZBJPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmEcIVCNsimvbNZ%2FQVTDIosK6s%2BV94aA2yvfnP9f7dAAiA3xgzFnMHAFtfgS8Onz0S6d1E8TcKky1YytLvx4KNygyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp2wllEZRc9CNIymiKtwDVV7iEinZyafGWvyRdNzlfj4qHFuH1vlxnlI6KkWQhISc6kX%2BS%2Fs4LqM0kuSMOmluldMd6PBsSfd7LWOG%2FdAOox%2BbLhhSdWl2OsrGwvKJNnVrFBXyYW%2Bi3K8qJR7RNt5aIdrFkIj3DAGNzVx3zX7ayXn7KRFuACPwA1fwxnhNxOiVUATRsGNvmD48miYkkGOsj7pWd0cWQA%2Bc17RWQD653W%2Fvkom09LGBv3AOsyTrk%2F%2B%2FnNTBpuDdmVZAYzc3cjc7P8Z832GTEYgf%2B1qoeuZMb2Kvti7Lxcvr0S5GDAUZvQ7BLDgeWZRUwcfWHwQO%2BDtAaxbAqo%2F0nSj%2Bc3P1JyNRUxxC7O%2BtfQBHmqMnxSzaqIuxdWmf8iJtk3wr%2FP0YJoh3BxwAmQijwLskVeDUl28ayTvxsCVDxrAbasLcxXkr6CuPkQQw5TmYRYNHyxg36INTeq7y79G5j1ZH4krlkifX4HZTIC%2B0G2wPEd8Bks%2FQRLhq4JRhllqPcFpRHCQc9cibJhEX6A2HalFU%2Fkasu%2BMCWNFZ3kFlEq0Uw8RP%2F5qI6zUKw%2Bc2k9XnH89DaKftu%2BpZjC46QxiXKWduCBqArpzMYFfEJB2pxsHJxtbxuwYWvfCXdkKqq7pRYbdKb0owxLb9vAY6pgGkW3EACeLxGFJwh%2BC%2B8ip%2B%2BMbd%2FLj0SwL8jRl1EiGggBX5O1EKRSUg2qPSsaDFnKkV5hGr8tqPeJATRKONpEphWQEYbXbdJaFnFMeMM8JVM7ADEi2mvCdeYy%2B08xXzDiFEAD20Tnx1N8rM%2BelDj0Oj9b%2FwgHnd%2FN4DQ0CAsQQvMeHZIvHSyLceU1Iuqy%2BgkpPkYnsvHLCgwekr5VWb90RdNW2HSHEH&X-Amz-Signature=56b682574912ead5dd385dc1257c5c381c5902dfac79ed387b503e267d19e70e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNZBJPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmEcIVCNsimvbNZ%2FQVTDIosK6s%2BV94aA2yvfnP9f7dAAiA3xgzFnMHAFtfgS8Onz0S6d1E8TcKky1YytLvx4KNygyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp2wllEZRc9CNIymiKtwDVV7iEinZyafGWvyRdNzlfj4qHFuH1vlxnlI6KkWQhISc6kX%2BS%2Fs4LqM0kuSMOmluldMd6PBsSfd7LWOG%2FdAOox%2BbLhhSdWl2OsrGwvKJNnVrFBXyYW%2Bi3K8qJR7RNt5aIdrFkIj3DAGNzVx3zX7ayXn7KRFuACPwA1fwxnhNxOiVUATRsGNvmD48miYkkGOsj7pWd0cWQA%2Bc17RWQD653W%2Fvkom09LGBv3AOsyTrk%2F%2B%2FnNTBpuDdmVZAYzc3cjc7P8Z832GTEYgf%2B1qoeuZMb2Kvti7Lxcvr0S5GDAUZvQ7BLDgeWZRUwcfWHwQO%2BDtAaxbAqo%2F0nSj%2Bc3P1JyNRUxxC7O%2BtfQBHmqMnxSzaqIuxdWmf8iJtk3wr%2FP0YJoh3BxwAmQijwLskVeDUl28ayTvxsCVDxrAbasLcxXkr6CuPkQQw5TmYRYNHyxg36INTeq7y79G5j1ZH4krlkifX4HZTIC%2B0G2wPEd8Bks%2FQRLhq4JRhllqPcFpRHCQc9cibJhEX6A2HalFU%2Fkasu%2BMCWNFZ3kFlEq0Uw8RP%2F5qI6zUKw%2Bc2k9XnH89DaKftu%2BpZjC46QxiXKWduCBqArpzMYFfEJB2pxsHJxtbxuwYWvfCXdkKqq7pRYbdKb0owxLb9vAY6pgGkW3EACeLxGFJwh%2BC%2B8ip%2B%2BMbd%2FLj0SwL8jRl1EiGggBX5O1EKRSUg2qPSsaDFnKkV5hGr8tqPeJATRKONpEphWQEYbXbdJaFnFMeMM8JVM7ADEi2mvCdeYy%2B08xXzDiFEAD20Tnx1N8rM%2BelDj0Oj9b%2FwgHnd%2FN4DQ0CAsQQvMeHZIvHSyLceU1Iuqy%2BgkpPkYnsvHLCgwekr5VWb90RdNW2HSHEH&X-Amz-Signature=90e237ff9a61bbccf1fdad57daba0d547025c4ff904a773c7ea9124994997fd8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QROYRFJE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAShAm7%2FpgQQ%2FhKd%2FqGx7kw8dKF1gpLhK6r7H64UJ7NGAiAufTGr3h1QrFxlwo9IH2BSLJOHc%2FDVA2Y8431wDetYMSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRkmpqz4V1vDsJT8eKtwDxfVnjoAligJ7ocSPPZ3rhr6VS35O7HWMCJ17ohSLHMyrchGBejiQoujAd0wWjHltX8rkPEON8j5oiuSPCGCJXqGnOBkxguK4%2B3Sy0oWrf7j61BYyBxmfmFBQWD3jnr3pENGXlV%2FG3wQ61Ocz81xl1j8GUchtEcnm%2BPT6ATchzxI%2B2KlNTWfwGC25%2FYnc04Y%2BbuVJvX0YHTkJIj%2F%2B5Q2V%2FsdFPyN%2F%2FVZbkie6NQ4wMyB4Lg1oqQSvelZI1fN0fo6obJgS9qEtVc9O8hMDsowurU5RsEWCdhXaYCuLIcYDF715ieo6yioYNuZ0dnbQsodPrPmKkKpCIG6til7FQnp3cwfVWIYAwT02RvJhKJT7w1zyhieOBq4G3ACPFw6MTj3DhuXobPIXO7SEb3NVl7R5CJ3%2BVc%2Fu35%2B23zNGzm0QGBSUU1WdGO0%2Fny3JvlNxaa6XWKnIFmKCDsZLaL8S9Aw1eDIxfc09LzPMa%2FPLhqgH8uaZP0xyweUZaZXkv%2B4mWIAB%2FU5%2BNvmDnWTfwAGCTEWm7DPWIEVa7Jt9kag1qK1Gs01vSx%2B8th7JrLK4obob%2F3QIS7XPNCkPV1BhW%2FIvSICZt9cgJauxxH%2FtjPsp0IIT2Pkkncx0Ty2wvZBrmtYwoLz9vAY6pgE9nZ9KJbtDELhPZ601CVWhdQyGT4Oi2gv%2BXIfSE3pBVNT4YuveuEXIK8UJjXIDfU0Aik%2F8FbvDk%2BiYMgmzjCLovgsESbftcShROmqLKdclRXFwGe1kYOxizj%2FxZtDCGroRsMuwS5ChQcP6VzElJWjYzkKrekwlHpQggs%2B%2F5zy84WZa7GSKkytjr6U3IAnCYqiGtaC2Ei6zXMY5XacrZDZWjSyaSvgo&X-Amz-Signature=93e6c407160257c7752b4d8e8a502ed202d41bc3db82d91565701437fb78a0e5&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674VTWDJL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHPKQvYh0e8H3bQ4s%2BCo53snHxNRNGhV5%2FEFJZn%2Bk4cwIgO9E6TWGOaVx9oPJzV6VG1ux7bWkQqFpgMFB9JcqvRzIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOH0IPHnNnXzR%2FDJaircA%2BGw8oKJnW8h7YbZlUPi%2Fq4BwY4pa%2BTfHF86nAvP3AzHnWsosmSsr%2FOg8sRYhaziYlGFXhw6QCXw1LR1sjS4Vi%2FPK1aN%2FIIrGIy8Jq%2FMg%2FItTshGS1rx0CQej0vYIVXjURonHF%2Btn6YvZD3anEV60ATQcidZXngwiKk2VSOFld4C3ysFo2z1AIlrk8FyPCBoe797seSI5qWOCq2SdS5HHPR9TxcTVC3HBGLiE5Ykml0HWDP0EmYbG4mqMiLfEPKwVhRNEhRvCHyUGxwYf6MgUnQQuOz7rr8nAEF0QBKo%2FZNe0I4xBZ82Des1kotjAtZSgHMbTW5e8%2BSptLENbWmN6Pud%2FmWXyzd7jPNwrjcgXS4Hbnq6I5ZIazUL3PQxjug9gbzFVTaBjhaDOBzS%2BWi1gBMgyK8Dow5MSlHWygQ3hP0rgV5T2eSZLPFy5srj2tVUo59jHQ0qe%2F5vZNuTbnynMse6luc%2Fx%2Flp18BpCDLBVd5TgJPQuf8B2mKITJXLhqUxoMWLBRvWH0Wjol3%2BXchFJ0cXhqD%2F3ifv1qdi78s1iHAS6019dShCwSyc%2B7IVZZRtqOhTLMLQ1ppqFji%2F0ANGPtP5FOigi36Xn9%2FRO0EIc8R%2F2U4u3PqmeiYgzaR0MNS5%2FbwGOqUBYDrN3k8926wZW0j441yj0dQr5TMvfnmyt0bgebSa8kDf3m38aTHFcFs%2F36bMFRPcudcoposVzlkGMKgTfJdg5jxbtJ7OhXCX6hP3XZhMiZkjjdWu9%2BeV1dhiXaBZYzkZsbuv32xKplmfV9%2B8smPtY0%2FSfELP16qWMz%2Bbdx48vq%2FhHVYnu%2BTbOXPdtRAN3V7aqGX2oL4feFmRvKVJ5ry3cK%2FctjRF&X-Amz-Signature=6479d56bf69201b64aaae4310d571d4523254019bb79006500303d9729262b21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNZBJPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmEcIVCNsimvbNZ%2FQVTDIosK6s%2BV94aA2yvfnP9f7dAAiA3xgzFnMHAFtfgS8Onz0S6d1E8TcKky1YytLvx4KNygyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp2wllEZRc9CNIymiKtwDVV7iEinZyafGWvyRdNzlfj4qHFuH1vlxnlI6KkWQhISc6kX%2BS%2Fs4LqM0kuSMOmluldMd6PBsSfd7LWOG%2FdAOox%2BbLhhSdWl2OsrGwvKJNnVrFBXyYW%2Bi3K8qJR7RNt5aIdrFkIj3DAGNzVx3zX7ayXn7KRFuACPwA1fwxnhNxOiVUATRsGNvmD48miYkkGOsj7pWd0cWQA%2Bc17RWQD653W%2Fvkom09LGBv3AOsyTrk%2F%2B%2FnNTBpuDdmVZAYzc3cjc7P8Z832GTEYgf%2B1qoeuZMb2Kvti7Lxcvr0S5GDAUZvQ7BLDgeWZRUwcfWHwQO%2BDtAaxbAqo%2F0nSj%2Bc3P1JyNRUxxC7O%2BtfQBHmqMnxSzaqIuxdWmf8iJtk3wr%2FP0YJoh3BxwAmQijwLskVeDUl28ayTvxsCVDxrAbasLcxXkr6CuPkQQw5TmYRYNHyxg36INTeq7y79G5j1ZH4krlkifX4HZTIC%2B0G2wPEd8Bks%2FQRLhq4JRhllqPcFpRHCQc9cibJhEX6A2HalFU%2Fkasu%2BMCWNFZ3kFlEq0Uw8RP%2F5qI6zUKw%2Bc2k9XnH89DaKftu%2BpZjC46QxiXKWduCBqArpzMYFfEJB2pxsHJxtbxuwYWvfCXdkKqq7pRYbdKb0owxLb9vAY6pgGkW3EACeLxGFJwh%2BC%2B8ip%2B%2BMbd%2FLj0SwL8jRl1EiGggBX5O1EKRSUg2qPSsaDFnKkV5hGr8tqPeJATRKONpEphWQEYbXbdJaFnFMeMM8JVM7ADEi2mvCdeYy%2B08xXzDiFEAD20Tnx1N8rM%2BelDj0Oj9b%2FwgHnd%2FN4DQ0CAsQQvMeHZIvHSyLceU1Iuqy%2BgkpPkYnsvHLCgwekr5VWb90RdNW2HSHEH&X-Amz-Signature=91e3b9a96dc148f0769aedf5a8e23dd683e7ac3982ccff3cebe570e5aba914f4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNZBJPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmEcIVCNsimvbNZ%2FQVTDIosK6s%2BV94aA2yvfnP9f7dAAiA3xgzFnMHAFtfgS8Onz0S6d1E8TcKky1YytLvx4KNygyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp2wllEZRc9CNIymiKtwDVV7iEinZyafGWvyRdNzlfj4qHFuH1vlxnlI6KkWQhISc6kX%2BS%2Fs4LqM0kuSMOmluldMd6PBsSfd7LWOG%2FdAOox%2BbLhhSdWl2OsrGwvKJNnVrFBXyYW%2Bi3K8qJR7RNt5aIdrFkIj3DAGNzVx3zX7ayXn7KRFuACPwA1fwxnhNxOiVUATRsGNvmD48miYkkGOsj7pWd0cWQA%2Bc17RWQD653W%2Fvkom09LGBv3AOsyTrk%2F%2B%2FnNTBpuDdmVZAYzc3cjc7P8Z832GTEYgf%2B1qoeuZMb2Kvti7Lxcvr0S5GDAUZvQ7BLDgeWZRUwcfWHwQO%2BDtAaxbAqo%2F0nSj%2Bc3P1JyNRUxxC7O%2BtfQBHmqMnxSzaqIuxdWmf8iJtk3wr%2FP0YJoh3BxwAmQijwLskVeDUl28ayTvxsCVDxrAbasLcxXkr6CuPkQQw5TmYRYNHyxg36INTeq7y79G5j1ZH4krlkifX4HZTIC%2B0G2wPEd8Bks%2FQRLhq4JRhllqPcFpRHCQc9cibJhEX6A2HalFU%2Fkasu%2BMCWNFZ3kFlEq0Uw8RP%2F5qI6zUKw%2Bc2k9XnH89DaKftu%2BpZjC46QxiXKWduCBqArpzMYFfEJB2pxsHJxtbxuwYWvfCXdkKqq7pRYbdKb0owxLb9vAY6pgGkW3EACeLxGFJwh%2BC%2B8ip%2B%2BMbd%2FLj0SwL8jRl1EiGggBX5O1EKRSUg2qPSsaDFnKkV5hGr8tqPeJATRKONpEphWQEYbXbdJaFnFMeMM8JVM7ADEi2mvCdeYy%2B08xXzDiFEAD20Tnx1N8rM%2BelDj0Oj9b%2FwgHnd%2FN4DQ0CAsQQvMeHZIvHSyLceU1Iuqy%2BgkpPkYnsvHLCgwekr5VWb90RdNW2HSHEH&X-Amz-Signature=c958fe16beb978ef4a3313088a62df2c3e47f95db9e6b17f614ca492eb36ec56&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNZBJPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmEcIVCNsimvbNZ%2FQVTDIosK6s%2BV94aA2yvfnP9f7dAAiA3xgzFnMHAFtfgS8Onz0S6d1E8TcKky1YytLvx4KNygyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp2wllEZRc9CNIymiKtwDVV7iEinZyafGWvyRdNzlfj4qHFuH1vlxnlI6KkWQhISc6kX%2BS%2Fs4LqM0kuSMOmluldMd6PBsSfd7LWOG%2FdAOox%2BbLhhSdWl2OsrGwvKJNnVrFBXyYW%2Bi3K8qJR7RNt5aIdrFkIj3DAGNzVx3zX7ayXn7KRFuACPwA1fwxnhNxOiVUATRsGNvmD48miYkkGOsj7pWd0cWQA%2Bc17RWQD653W%2Fvkom09LGBv3AOsyTrk%2F%2B%2FnNTBpuDdmVZAYzc3cjc7P8Z832GTEYgf%2B1qoeuZMb2Kvti7Lxcvr0S5GDAUZvQ7BLDgeWZRUwcfWHwQO%2BDtAaxbAqo%2F0nSj%2Bc3P1JyNRUxxC7O%2BtfQBHmqMnxSzaqIuxdWmf8iJtk3wr%2FP0YJoh3BxwAmQijwLskVeDUl28ayTvxsCVDxrAbasLcxXkr6CuPkQQw5TmYRYNHyxg36INTeq7y79G5j1ZH4krlkifX4HZTIC%2B0G2wPEd8Bks%2FQRLhq4JRhllqPcFpRHCQc9cibJhEX6A2HalFU%2Fkasu%2BMCWNFZ3kFlEq0Uw8RP%2F5qI6zUKw%2Bc2k9XnH89DaKftu%2BpZjC46QxiXKWduCBqArpzMYFfEJB2pxsHJxtbxuwYWvfCXdkKqq7pRYbdKb0owxLb9vAY6pgGkW3EACeLxGFJwh%2BC%2B8ip%2B%2BMbd%2FLj0SwL8jRl1EiGggBX5O1EKRSUg2qPSsaDFnKkV5hGr8tqPeJATRKONpEphWQEYbXbdJaFnFMeMM8JVM7ADEi2mvCdeYy%2B08xXzDiFEAD20Tnx1N8rM%2BelDj0Oj9b%2FwgHnd%2FN4DQ0CAsQQvMeHZIvHSyLceU1Iuqy%2BgkpPkYnsvHLCgwekr5VWb90RdNW2HSHEH&X-Amz-Signature=da37c03be22833893a17b505564b87a11946575f6aa759bafd4834fca7e813c9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGRNC7BS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5%2FpokwAttplciAvuC2MvWyVSAW68rGm%2F61vk8Xn%2BZVwIgSepqTwajyOGLPf5tRVlDgFrKzHY1mwTTNABfMm1BkhUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK8%2B5b%2FSoOQGgkliUyrcA1jjxOjihLDk3F16kGXyiJBhyBeCAqiwbjvRfl0OgNyezdU2MuGxjoqrXHX0oLG5cDNa7a8YiGAPbQh9BInl1C07VWIPmNydfQ4z6b3HHNelVX3O3ky%2BaAhmABhFmZjS6Yic9eqidfgnE5s%2BsBr8%2FlBjuqUS1U%2BoXFP9uPcvVz%2F7SRQF7o4mN3P7bBgBMEPEV%2BkXue6e6Zn0qAh%2BQAoHQ%2FbvnY%2BoREUgGl%2F9RMkAG4b2ICatFSmDvntjqNakyFRzpyM6CmeVXiVqR4b1CKil4pVXCs%2BNxUBMx127dpgrti6HzpmgUslHdqMeLhoaXv0Dxen7vHgzHExL%2BR3gn24D9wmBew8Jfd1HH2brGfWQVLn2Ns4rT1Z8LgPMkOZRX0NS28JY33mavZnpDI%2BiDX1CKmqUNC%2BwfgDBrQZUIaHhQCT6nZeyDdvOPAweBf2HNnld%2F4ikTNfy4tmJMe%2Bst1%2FF7lKRjJXWHEWwWyBMMVL8cE68v44g1F5Z8v8xR26D0pzrCRThq7yguXw5f9tYfAZkb0v0D6035qOoLfrRcL7fZTgxeiGaGfKjkbph8MbiKUlPp7KEQR5JaMIb4jcgvKP9ivlYndJ1PCW7KT0BfR5OMi445uWfV65Qvbg%2B0juTMIjC%2FbwGOqUBEot9AlkTKBsRYADoNw3ZEBxKW6egAtx3KkF6d7n%2FDdCivMDwnIFljh4Ic8Ic2wMytZrLc6WxDqDSYNyCkwr18yTahtYlFuwmLMplQkuLK%2FxC9m7FNPCvSNIy33ZCJAUTlvsE4XWPb1LXnMcg4DBMVLAyC548Ao92ZPf20PNp9OTxNJZLxKDWr3koiOKWp2%2F6OHeDpeYEImvbHRrEbmKsnKJFd2qo&X-Amz-Signature=7a6b49e6d755dc85d5533e624a360d774361e0ecb59cb040d88fa3ce1e6ee9d3&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSBMVWSN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeNB0wl9EhK4LuHMSsCy%2F82AyHOiBotpxvTJLHc%2Bvl3AIgEn16ugN%2FXYSzMkFLl%2FqwwfggSaApXjZjL4TMNWYA%2B%2B8qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNR7h81iMN0%2F0RRNqSrcA81Nd56QksdxigTDK9cOB3Gm3obARfW3uBxMOLh%2BG2TiVFOozbRXotFYjCOLoWCYY0s3SS8VQbYQpYTBYtPlTAWZO939%2Bvf1x9DmuF5MW5BNhFO5Bt9GZJ%2Fzqo62N%2BAX2NqoV7lz0j52WaetMhddTBNCZK%2F4jBgutNpjOB44iy95sH%2FuebEBg3%2FtPQeKFO1f6VughLTA1UIyf7SEsn4y89Va7GqKPErTPP4F1js%2BFv9I7RhwLgx8Us31PBtD3x7MkKQFzWMjhkD3GARuc%2FpTyhjgH%2BJiC36S3VcS1%2FfywUlXWaQqSMU5ZDTBDASsWSV7Yhm927q5KGNDUFApDeAT8cRqIO2qs4FBrRlw8TT3EIAqc5uvsk9WJPk%2B16btfFiL6e8Q3Kgr%2B%2FZWLSo%2BqIDt%2B%2F9IR05UntI32U7xYafgu2fUkAjQUJ078mJpjVo0eQ3l2MxReT1%2FG5fdZa92ukntTXHuBIOh%2FJPkDMAvknoJWIwoeuOMxFhiMRkwxFjWppUM0BOW8WUqWf1CzgeE9y%2FBsUFlIfr83XL1um%2BVlVODPaWBTpJg0z59Zzj%2BJ4hryhkySNFRW7zo03E2NMgKuhJ2u1R1jd5JzulE7aV4ZVYuCccPR82sUltcVsrpS70RMOW%2F%2FbwGOqUB3Q3U2ZYHLga5%2BOo4cvKGcI5wfMbfyzNsnRDxzDQkwYjof2CdAd8DGp72MISv%2FiNYxepp6sL67pzrFCyQ4QeSN2JKTeyfcEm6wrQjhjXhSoVdVEa7gGkkmQcqtWkmP%2BMVUDAXBRSR3w4BA%2F7HOrBvn%2Fo%2FjCMQJKbjhsV5Xq02s35RbXM0E9P%2Bs2Hpb1pJrf8lJNGQ1ISUfmK3FXOHeL5pTiXa%2BeSe&X-Amz-Signature=4581d63b02c12446e35f9596c6dc13283765a73ed82a4e2a392e7e38f58f067c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXXQUQF4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGUNUSUinD1BBO3sZh0u2rrOAA5Yf2uZJ4mbQX7GrVNuAiEAuyh0oYfHtbNIS2kLRgBr4A59WI9wGrGW3dGGpoEJ%2Be0qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKonterjl9GyaK9f3CrcA5MSy23xCSa3yR2bc8T9fykLM8C8tNwi70AufntDmro62NeesWJGu1Z7Jrvq%2FKzbannttsYFv0qhYnh8mIoOnViVZJ34ssgPFudqpN8wgE%2BEBtajI8gA4GlMc5%2BF5qZ6MN9SNgf9d4MoaU352%2BHjD8x9krDZpk2XsH23OB4J7JlG1MH6jCOT7qMIu%2BCALaedrAhWAGrj%2BC6wtpSG%2F1UBg0xzcpO1Yz%2BhDHFjeRfFStMrH5KlUsOfpScEKy22UGQbhRFfW4c7lylVkVoblmuVTWt8XI5kFpQklFxfaVe%2BL%2FYKPDGk86aqeT7AyR05s7I%2BKRtEPGBx5oRQUAp55sn1GK04hTXz4R1jrI545Zrho8Xgl%2BDPa%2FRUT2jCSNoM4fHbSmw%2BVQKBtOUiUIhxMfO9aSG7o0fUY%2BCo9em%2F6sNg0XC0meRyZf8RJgVyXOWZsMgzs8ySOZ8dDfuwi9b%2FAmqfAKK86Mk0oFyK1yPzleCZ11BkEPniaFRb52NipV4Y6Kg9UEPJdvIoG3dxXM7guLraXIBJ4yJ0RUKqV8Xvdu2JHQT4yDJxCzPcawTeIWP7zskYcsEZcOEdIVVBq9yXh677zJE6HQIRni0kJX8r%2Fit%2FvSzUaaHmpZmz1LPDiL75MLu5%2FbwGOqUBIdwLv69Mr8XNIPtKCv1Z0ltLJEuaq8NJZh31Y5CXTQ3IJHXID1nPmld7eUreyt2wFls1uV%2B9nFz4Rowhw9EYQIXKuGv%2Bej1rJd3FwHmJAi2SSPJWiwblhngXsKI%2B%2Ff0HKzlUOchTHvD4JxKfqm%2FkbzdnaACzwfHhCWQn4VyZjHNc46%2BmNaOEe8YiH10xrLLSeLD8tm3AMISUvfR%2FIQoztx1pE7qx&X-Amz-Signature=e0cc85cf2e5cbfdf32d34112cab5ac2364269d5be3793f8240419145338987b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N6PESYQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC6Rr%2FBQROhvte7DE2OiOjw6MOi8nMlBHLwwBlmi2wHBAiAmQj1ken2HL8o5YGETWYXjtL0SBGMyjQw4hisFj0%2FOCyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFMZ94B5%2FkXSy5fslKtwDIpO%2Bc%2B1xzmIYi6oH3ghK6mqn3ednCWx%2Bi1AkTgFw2SxJhr25rOMQQqobZboJAQECUPdu1qZxTKe9YyMaIMidxKc8hKsmwUJ2%2FslZ0kXqgHetUjL2oDzvxSrq3%2FfhekOB7zstCqKHa2wWZSo6ZYzt4Yxo%2B20Va8SB20cUXHQGUjRyncc6NCzlE1pwh%2FSp%2BiYu2XtV%2FsqOUwADfr8TyNUxpIPdnhagJYslhihD34YrRH6sexUHG6nsRBgPzM2PXcwgLQbdPTUEXQY8b0uCEiItQrX6dAwlJSroE7L2Kij3m9I9etU4tdjxjs7ItNYI73gEYPDmUpW05zj3sLTuOOgT0WXmiBONuzJE%2BmwRmFEc%2F9jOkYzR4xlQwWnya800CXryGVuOl%2Bi%2FBi7tyFyrM9rSJJd1Tu5KqbN4nmwqN3fUvpAbAs%2F1XkveKQcxqT63eWe%2Be1ZQYBybjkwsEiiRnZH0BEwsWgCto%2B4qYSxSmQf87UcHmI9wxI0QEVWIKd2%2FZQY%2BZdmtPcBwUvubeiPbo6l5f%2Ft5DXMY6GsrTldsRM1%2BbnJiz7rwxonmnG7bLQN2c3Rgnl3cHxw21lPhe0jF8eWl73Wb4Anjyi%2FH8M9vm74rlDn4Yxq3sxmiGmKZhWAwu7n9vAY6pgEJcPr2WQkY2XcEOrPmHviBI7GAq%2FN3yIx1VKoxhzRfXqX3ykuIhTzM2SKFnLwhhtngEZoZNGvI04JU1AvIO7r0bZ3U56bIg4YFZURbN%2FlFrVuQJkUlU8rCHLhPJAb%2FZJDMKJOwaYok3HpkAFuP6dh8kz1Nd4a2xjffkAnyKxPshTcnZxgu1imU%2F%2BOKJ%2FiO6A0f3xTzw%2BMd6xG8YokWLENiWSWjrei7&X-Amz-Signature=f3b2d425ede69e6e37a10c9a3b898427289d336f34b9d80e2ccb1158eaa336e6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N6PESYQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC6Rr%2FBQROhvte7DE2OiOjw6MOi8nMlBHLwwBlmi2wHBAiAmQj1ken2HL8o5YGETWYXjtL0SBGMyjQw4hisFj0%2FOCyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFMZ94B5%2FkXSy5fslKtwDIpO%2Bc%2B1xzmIYi6oH3ghK6mqn3ednCWx%2Bi1AkTgFw2SxJhr25rOMQQqobZboJAQECUPdu1qZxTKe9YyMaIMidxKc8hKsmwUJ2%2FslZ0kXqgHetUjL2oDzvxSrq3%2FfhekOB7zstCqKHa2wWZSo6ZYzt4Yxo%2B20Va8SB20cUXHQGUjRyncc6NCzlE1pwh%2FSp%2BiYu2XtV%2FsqOUwADfr8TyNUxpIPdnhagJYslhihD34YrRH6sexUHG6nsRBgPzM2PXcwgLQbdPTUEXQY8b0uCEiItQrX6dAwlJSroE7L2Kij3m9I9etU4tdjxjs7ItNYI73gEYPDmUpW05zj3sLTuOOgT0WXmiBONuzJE%2BmwRmFEc%2F9jOkYzR4xlQwWnya800CXryGVuOl%2Bi%2FBi7tyFyrM9rSJJd1Tu5KqbN4nmwqN3fUvpAbAs%2F1XkveKQcxqT63eWe%2Be1ZQYBybjkwsEiiRnZH0BEwsWgCto%2B4qYSxSmQf87UcHmI9wxI0QEVWIKd2%2FZQY%2BZdmtPcBwUvubeiPbo6l5f%2Ft5DXMY6GsrTldsRM1%2BbnJiz7rwxonmnG7bLQN2c3Rgnl3cHxw21lPhe0jF8eWl73Wb4Anjyi%2FH8M9vm74rlDn4Yxq3sxmiGmKZhWAwu7n9vAY6pgEJcPr2WQkY2XcEOrPmHviBI7GAq%2FN3yIx1VKoxhzRfXqX3ykuIhTzM2SKFnLwhhtngEZoZNGvI04JU1AvIO7r0bZ3U56bIg4YFZURbN%2FlFrVuQJkUlU8rCHLhPJAb%2FZJDMKJOwaYok3HpkAFuP6dh8kz1Nd4a2xjffkAnyKxPshTcnZxgu1imU%2F%2BOKJ%2FiO6A0f3xTzw%2BMd6xG8YokWLENiWSWjrei7&X-Amz-Signature=703b32cda2e03b258ccb1ec9585948b1ace29b25613d1480d01569a600cc906c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
