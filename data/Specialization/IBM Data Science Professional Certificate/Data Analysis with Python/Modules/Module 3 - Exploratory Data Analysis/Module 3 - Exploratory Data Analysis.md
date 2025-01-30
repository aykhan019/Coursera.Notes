

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGFV5Q54%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDf4bgwnaW%2FNUnJeI5Jxv4LJs87TrRQ0pbxO1aB%2Bh6CqgIhALDDwuBQAYIiEGBOQJ7BMJgwzNy%2BYNUsKUzd7NH%2FKmCcKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyIIhpGecAVvUjrpKsq3APpbr4YuG2xpO8ZOgs6sVorgFXo2rUKMCV6%2FN8OAPLTjX0BD6JN6U3AB4nG70sLiS8CaLqMM8SkVsfIaA0AYDGyOGJyNkOYp3FqEIy%2FtXPm9ZwxA4WPQEQSeT2u9r00ib8er2TT8Cwtr5ij0oEmeCC3lo%2FY1ziCmxbZY%2F%2BeDM2B%2FeCWzsjGfmlZk0Ru6AxUzDMpHOkieO16yOlH%2FOuQOpWO2kMGC7DPrc3aweD5U58GSRmL8Ch0vjFsEorI272MvBQIZUJYJALPBp8%2B5oFPQHWOdfXZwZavKerWwgvNGdMiO6TqiON%2Ftd7lTGjtmlxshwMCZRoWwQ1ahFMrk11OqtjUGSAXxw1Rsgrmk9gwpdyQFrdUMEMGH%2BOGtsgx67IwGdB%2F9ufHW9NgFtp1Usn2ajak8v4UrIZBtRX6O%2FGejmakmBsY2w8xXiggBudyKVOIgFl8YctKis2Pcg%2BtDCTHCe5SMxOcwrh3AQ3Xjrg40LVi7%2BhGcWe9WeXqUQZKlMrTC0igLeLDghrVz9dukKwvu0VEWr9sPwpzRnXgCzLNoqZ3Bq%2FRgiKQtI%2BSBojG0sktIOHx67Tsvorz%2BAWiSZu3b7BGBFjxQTw560Q8of5HmBBu4c8IGcFBhTjC8h1YDzCFsuu8BjqkAYKOMhyfvdQUpQXDRw3pdH6kp%2FaJsAvk8PJSsZCecVG6t4iPV0iTT6F6w38lP%2F8NAJ%2BgDW4j92BovfeaOkemydbV7Dgo%2BvKkl7FRxKHlr0W%2BPJx9A0wlkTFl%2Bdit7xTd%2F%2FfVZARjEU4CEtQom0I4s6IKFN65dvU9lEfPigKHi0Pk2%2FJkE3C%2BV1ac%2FAbFFD4SAiQWfn7eTZngL5eMqPFvI63Li5Wm&X-Amz-Signature=1612c83021d8b8c1e7796d0486eb99676ce1575c6e7e353229291df465abee4a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGFV5Q54%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDf4bgwnaW%2FNUnJeI5Jxv4LJs87TrRQ0pbxO1aB%2Bh6CqgIhALDDwuBQAYIiEGBOQJ7BMJgwzNy%2BYNUsKUzd7NH%2FKmCcKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyIIhpGecAVvUjrpKsq3APpbr4YuG2xpO8ZOgs6sVorgFXo2rUKMCV6%2FN8OAPLTjX0BD6JN6U3AB4nG70sLiS8CaLqMM8SkVsfIaA0AYDGyOGJyNkOYp3FqEIy%2FtXPm9ZwxA4WPQEQSeT2u9r00ib8er2TT8Cwtr5ij0oEmeCC3lo%2FY1ziCmxbZY%2F%2BeDM2B%2FeCWzsjGfmlZk0Ru6AxUzDMpHOkieO16yOlH%2FOuQOpWO2kMGC7DPrc3aweD5U58GSRmL8Ch0vjFsEorI272MvBQIZUJYJALPBp8%2B5oFPQHWOdfXZwZavKerWwgvNGdMiO6TqiON%2Ftd7lTGjtmlxshwMCZRoWwQ1ahFMrk11OqtjUGSAXxw1Rsgrmk9gwpdyQFrdUMEMGH%2BOGtsgx67IwGdB%2F9ufHW9NgFtp1Usn2ajak8v4UrIZBtRX6O%2FGejmakmBsY2w8xXiggBudyKVOIgFl8YctKis2Pcg%2BtDCTHCe5SMxOcwrh3AQ3Xjrg40LVi7%2BhGcWe9WeXqUQZKlMrTC0igLeLDghrVz9dukKwvu0VEWr9sPwpzRnXgCzLNoqZ3Bq%2FRgiKQtI%2BSBojG0sktIOHx67Tsvorz%2BAWiSZu3b7BGBFjxQTw560Q8of5HmBBu4c8IGcFBhTjC8h1YDzCFsuu8BjqkAYKOMhyfvdQUpQXDRw3pdH6kp%2FaJsAvk8PJSsZCecVG6t4iPV0iTT6F6w38lP%2F8NAJ%2BgDW4j92BovfeaOkemydbV7Dgo%2BvKkl7FRxKHlr0W%2BPJx9A0wlkTFl%2Bdit7xTd%2F%2FfVZARjEU4CEtQom0I4s6IKFN65dvU9lEfPigKHi0Pk2%2FJkE3C%2BV1ac%2FAbFFD4SAiQWfn7eTZngL5eMqPFvI63Li5Wm&X-Amz-Signature=5c4652b5c81619ae3be9ac9b2d8659bc7f9626086cd6b90c7389747efa140548&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGFV5Q54%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDf4bgwnaW%2FNUnJeI5Jxv4LJs87TrRQ0pbxO1aB%2Bh6CqgIhALDDwuBQAYIiEGBOQJ7BMJgwzNy%2BYNUsKUzd7NH%2FKmCcKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyIIhpGecAVvUjrpKsq3APpbr4YuG2xpO8ZOgs6sVorgFXo2rUKMCV6%2FN8OAPLTjX0BD6JN6U3AB4nG70sLiS8CaLqMM8SkVsfIaA0AYDGyOGJyNkOYp3FqEIy%2FtXPm9ZwxA4WPQEQSeT2u9r00ib8er2TT8Cwtr5ij0oEmeCC3lo%2FY1ziCmxbZY%2F%2BeDM2B%2FeCWzsjGfmlZk0Ru6AxUzDMpHOkieO16yOlH%2FOuQOpWO2kMGC7DPrc3aweD5U58GSRmL8Ch0vjFsEorI272MvBQIZUJYJALPBp8%2B5oFPQHWOdfXZwZavKerWwgvNGdMiO6TqiON%2Ftd7lTGjtmlxshwMCZRoWwQ1ahFMrk11OqtjUGSAXxw1Rsgrmk9gwpdyQFrdUMEMGH%2BOGtsgx67IwGdB%2F9ufHW9NgFtp1Usn2ajak8v4UrIZBtRX6O%2FGejmakmBsY2w8xXiggBudyKVOIgFl8YctKis2Pcg%2BtDCTHCe5SMxOcwrh3AQ3Xjrg40LVi7%2BhGcWe9WeXqUQZKlMrTC0igLeLDghrVz9dukKwvu0VEWr9sPwpzRnXgCzLNoqZ3Bq%2FRgiKQtI%2BSBojG0sktIOHx67Tsvorz%2BAWiSZu3b7BGBFjxQTw560Q8of5HmBBu4c8IGcFBhTjC8h1YDzCFsuu8BjqkAYKOMhyfvdQUpQXDRw3pdH6kp%2FaJsAvk8PJSsZCecVG6t4iPV0iTT6F6w38lP%2F8NAJ%2BgDW4j92BovfeaOkemydbV7Dgo%2BvKkl7FRxKHlr0W%2BPJx9A0wlkTFl%2Bdit7xTd%2F%2FfVZARjEU4CEtQom0I4s6IKFN65dvU9lEfPigKHi0Pk2%2FJkE3C%2BV1ac%2FAbFFD4SAiQWfn7eTZngL5eMqPFvI63Li5Wm&X-Amz-Signature=215f664e94f594edf14b8d165f6f1215f36e6220e18faf101c70587ae9fe7343&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPCSRKO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfAgCaBIKrNks6nk2DoqemdwJ2vweSihIL2dACj1dUCAIge5xykAcV603UkoihvaZP8QFBYynyE3tnTrvl%2Fj0Mz0EqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4u1PcbYd2mZ4FS6yrcA8Ice2h2jVpSKCQynNtXzlfpljh2GJ66r9TuO%2FMZHYwHs2KeKYRWaWVJTS2Xjm%2BIjhqyGVUd9Bx6aLib4oXQg07dII24HdHrV4VSni3zgFaz3zy9pGb%2FEFAKXB3vYQLU9%2By4cmQDI%2FRlVhG4CmZnmj9JNxNIx8TAC3ClrQ55jR53SuZ4GVmegq59PQH4b%2BGTxGvbKgm0zhtzBsDLMX7Gn1%2Fc1R%2FJqhPOoxzxJ8ByfjpUlj7gGcyuogb9sbwTGC29x82hZj7YlvJfbctUnIxlCqBXJvwSTW17D9PXfSG2HBma8lcyCE9B%2FKF376QKSGBuG%2FNtNUClsFSdjTi8kFxuf4fBt4rIgvevxwiQi3Ih97%2F7f2u5luYjLkDRTgNQpcKGdN55rKjBZxm7vDiptplDCR%2FpPX%2FkLMCphJhLXU7kqoNLo18HNztdA5We%2FComDSlHE57cpxCFOf2OA1%2BJd0%2FaebJElC6T5wiHfcyW2EyJTizU%2BHG7ed1pUB5h41gv%2BcUVuSZ9D5uLb%2FFCDLaFBAUP0XKDJcItSPe%2FgXp2hno7zzCnn1%2BSD4yM5a4fVHzSI4l7LEtIeBduVK8lNCQqh9Y6Heh5m5IOsdmCOZkx7AZgDAbs%2BVpB7P%2B16z1%2FvjNaMNGx67wGOqUBePtLo4AaI99ErMnw0eTdjfYHbkqCMdn4G05oDEitXk1FS%2FCgKjWtrlK56XFxEgN2uo56DWAufAM3zB1mNg9UDOV8vWvqL%2FnIsa8%2FwJp%2Bm9TgQ8jXYdlSC6yHOw2KDC0i5l9aTUStOhq%2FFzl7nu0OW5HYolZfkynMAUNyzeGbD%2BZaQGjYFjAPj0oqHOBllq7s9K2H6H5AxPkodoY10OrMu7laCMde&X-Amz-Signature=c37a87201a73a04a73a601af5f108314094198ec4a0b8577f1b1e67d0cf440a6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPCSRKO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfAgCaBIKrNks6nk2DoqemdwJ2vweSihIL2dACj1dUCAIge5xykAcV603UkoihvaZP8QFBYynyE3tnTrvl%2Fj0Mz0EqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4u1PcbYd2mZ4FS6yrcA8Ice2h2jVpSKCQynNtXzlfpljh2GJ66r9TuO%2FMZHYwHs2KeKYRWaWVJTS2Xjm%2BIjhqyGVUd9Bx6aLib4oXQg07dII24HdHrV4VSni3zgFaz3zy9pGb%2FEFAKXB3vYQLU9%2By4cmQDI%2FRlVhG4CmZnmj9JNxNIx8TAC3ClrQ55jR53SuZ4GVmegq59PQH4b%2BGTxGvbKgm0zhtzBsDLMX7Gn1%2Fc1R%2FJqhPOoxzxJ8ByfjpUlj7gGcyuogb9sbwTGC29x82hZj7YlvJfbctUnIxlCqBXJvwSTW17D9PXfSG2HBma8lcyCE9B%2FKF376QKSGBuG%2FNtNUClsFSdjTi8kFxuf4fBt4rIgvevxwiQi3Ih97%2F7f2u5luYjLkDRTgNQpcKGdN55rKjBZxm7vDiptplDCR%2FpPX%2FkLMCphJhLXU7kqoNLo18HNztdA5We%2FComDSlHE57cpxCFOf2OA1%2BJd0%2FaebJElC6T5wiHfcyW2EyJTizU%2BHG7ed1pUB5h41gv%2BcUVuSZ9D5uLb%2FFCDLaFBAUP0XKDJcItSPe%2FgXp2hno7zzCnn1%2BSD4yM5a4fVHzSI4l7LEtIeBduVK8lNCQqh9Y6Heh5m5IOsdmCOZkx7AZgDAbs%2BVpB7P%2B16z1%2FvjNaMNGx67wGOqUBePtLo4AaI99ErMnw0eTdjfYHbkqCMdn4G05oDEitXk1FS%2FCgKjWtrlK56XFxEgN2uo56DWAufAM3zB1mNg9UDOV8vWvqL%2FnIsa8%2FwJp%2Bm9TgQ8jXYdlSC6yHOw2KDC0i5l9aTUStOhq%2FFzl7nu0OW5HYolZfkynMAUNyzeGbD%2BZaQGjYFjAPj0oqHOBllq7s9K2H6H5AxPkodoY10OrMu7laCMde&X-Amz-Signature=d2369f3d8e89ffe36d0e97174fcb52e1a63d504f9f063f1984ace13ed20efaf3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPCSRKO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfAgCaBIKrNks6nk2DoqemdwJ2vweSihIL2dACj1dUCAIge5xykAcV603UkoihvaZP8QFBYynyE3tnTrvl%2Fj0Mz0EqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4u1PcbYd2mZ4FS6yrcA8Ice2h2jVpSKCQynNtXzlfpljh2GJ66r9TuO%2FMZHYwHs2KeKYRWaWVJTS2Xjm%2BIjhqyGVUd9Bx6aLib4oXQg07dII24HdHrV4VSni3zgFaz3zy9pGb%2FEFAKXB3vYQLU9%2By4cmQDI%2FRlVhG4CmZnmj9JNxNIx8TAC3ClrQ55jR53SuZ4GVmegq59PQH4b%2BGTxGvbKgm0zhtzBsDLMX7Gn1%2Fc1R%2FJqhPOoxzxJ8ByfjpUlj7gGcyuogb9sbwTGC29x82hZj7YlvJfbctUnIxlCqBXJvwSTW17D9PXfSG2HBma8lcyCE9B%2FKF376QKSGBuG%2FNtNUClsFSdjTi8kFxuf4fBt4rIgvevxwiQi3Ih97%2F7f2u5luYjLkDRTgNQpcKGdN55rKjBZxm7vDiptplDCR%2FpPX%2FkLMCphJhLXU7kqoNLo18HNztdA5We%2FComDSlHE57cpxCFOf2OA1%2BJd0%2FaebJElC6T5wiHfcyW2EyJTizU%2BHG7ed1pUB5h41gv%2BcUVuSZ9D5uLb%2FFCDLaFBAUP0XKDJcItSPe%2FgXp2hno7zzCnn1%2BSD4yM5a4fVHzSI4l7LEtIeBduVK8lNCQqh9Y6Heh5m5IOsdmCOZkx7AZgDAbs%2BVpB7P%2B16z1%2FvjNaMNGx67wGOqUBePtLo4AaI99ErMnw0eTdjfYHbkqCMdn4G05oDEitXk1FS%2FCgKjWtrlK56XFxEgN2uo56DWAufAM3zB1mNg9UDOV8vWvqL%2FnIsa8%2FwJp%2Bm9TgQ8jXYdlSC6yHOw2KDC0i5l9aTUStOhq%2FFzl7nu0OW5HYolZfkynMAUNyzeGbD%2BZaQGjYFjAPj0oqHOBllq7s9K2H6H5AxPkodoY10OrMu7laCMde&X-Amz-Signature=5168975553bb03391b76a0ae9d011cd87081445252e08522ba88ec34175f460d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPCSRKO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfAgCaBIKrNks6nk2DoqemdwJ2vweSihIL2dACj1dUCAIge5xykAcV603UkoihvaZP8QFBYynyE3tnTrvl%2Fj0Mz0EqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4u1PcbYd2mZ4FS6yrcA8Ice2h2jVpSKCQynNtXzlfpljh2GJ66r9TuO%2FMZHYwHs2KeKYRWaWVJTS2Xjm%2BIjhqyGVUd9Bx6aLib4oXQg07dII24HdHrV4VSni3zgFaz3zy9pGb%2FEFAKXB3vYQLU9%2By4cmQDI%2FRlVhG4CmZnmj9JNxNIx8TAC3ClrQ55jR53SuZ4GVmegq59PQH4b%2BGTxGvbKgm0zhtzBsDLMX7Gn1%2Fc1R%2FJqhPOoxzxJ8ByfjpUlj7gGcyuogb9sbwTGC29x82hZj7YlvJfbctUnIxlCqBXJvwSTW17D9PXfSG2HBma8lcyCE9B%2FKF376QKSGBuG%2FNtNUClsFSdjTi8kFxuf4fBt4rIgvevxwiQi3Ih97%2F7f2u5luYjLkDRTgNQpcKGdN55rKjBZxm7vDiptplDCR%2FpPX%2FkLMCphJhLXU7kqoNLo18HNztdA5We%2FComDSlHE57cpxCFOf2OA1%2BJd0%2FaebJElC6T5wiHfcyW2EyJTizU%2BHG7ed1pUB5h41gv%2BcUVuSZ9D5uLb%2FFCDLaFBAUP0XKDJcItSPe%2FgXp2hno7zzCnn1%2BSD4yM5a4fVHzSI4l7LEtIeBduVK8lNCQqh9Y6Heh5m5IOsdmCOZkx7AZgDAbs%2BVpB7P%2B16z1%2FvjNaMNGx67wGOqUBePtLo4AaI99ErMnw0eTdjfYHbkqCMdn4G05oDEitXk1FS%2FCgKjWtrlK56XFxEgN2uo56DWAufAM3zB1mNg9UDOV8vWvqL%2FnIsa8%2FwJp%2Bm9TgQ8jXYdlSC6yHOw2KDC0i5l9aTUStOhq%2FFzl7nu0OW5HYolZfkynMAUNyzeGbD%2BZaQGjYFjAPj0oqHOBllq7s9K2H6H5AxPkodoY10OrMu7laCMde&X-Amz-Signature=17e818976d693c9ba9a31af87312125b9b31c7f472564d66539e4b4cd609fecb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPCSRKO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfAgCaBIKrNks6nk2DoqemdwJ2vweSihIL2dACj1dUCAIge5xykAcV603UkoihvaZP8QFBYynyE3tnTrvl%2Fj0Mz0EqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4u1PcbYd2mZ4FS6yrcA8Ice2h2jVpSKCQynNtXzlfpljh2GJ66r9TuO%2FMZHYwHs2KeKYRWaWVJTS2Xjm%2BIjhqyGVUd9Bx6aLib4oXQg07dII24HdHrV4VSni3zgFaz3zy9pGb%2FEFAKXB3vYQLU9%2By4cmQDI%2FRlVhG4CmZnmj9JNxNIx8TAC3ClrQ55jR53SuZ4GVmegq59PQH4b%2BGTxGvbKgm0zhtzBsDLMX7Gn1%2Fc1R%2FJqhPOoxzxJ8ByfjpUlj7gGcyuogb9sbwTGC29x82hZj7YlvJfbctUnIxlCqBXJvwSTW17D9PXfSG2HBma8lcyCE9B%2FKF376QKSGBuG%2FNtNUClsFSdjTi8kFxuf4fBt4rIgvevxwiQi3Ih97%2F7f2u5luYjLkDRTgNQpcKGdN55rKjBZxm7vDiptplDCR%2FpPX%2FkLMCphJhLXU7kqoNLo18HNztdA5We%2FComDSlHE57cpxCFOf2OA1%2BJd0%2FaebJElC6T5wiHfcyW2EyJTizU%2BHG7ed1pUB5h41gv%2BcUVuSZ9D5uLb%2FFCDLaFBAUP0XKDJcItSPe%2FgXp2hno7zzCnn1%2BSD4yM5a4fVHzSI4l7LEtIeBduVK8lNCQqh9Y6Heh5m5IOsdmCOZkx7AZgDAbs%2BVpB7P%2B16z1%2FvjNaMNGx67wGOqUBePtLo4AaI99ErMnw0eTdjfYHbkqCMdn4G05oDEitXk1FS%2FCgKjWtrlK56XFxEgN2uo56DWAufAM3zB1mNg9UDOV8vWvqL%2FnIsa8%2FwJp%2Bm9TgQ8jXYdlSC6yHOw2KDC0i5l9aTUStOhq%2FFzl7nu0OW5HYolZfkynMAUNyzeGbD%2BZaQGjYFjAPj0oqHOBllq7s9K2H6H5AxPkodoY10OrMu7laCMde&X-Amz-Signature=84836e911979dea98b90bdc3eb8c3b95f0abe40d1dbdfa3c244ee8b6cfcd3733&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPCSRKO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfAgCaBIKrNks6nk2DoqemdwJ2vweSihIL2dACj1dUCAIge5xykAcV603UkoihvaZP8QFBYynyE3tnTrvl%2Fj0Mz0EqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4u1PcbYd2mZ4FS6yrcA8Ice2h2jVpSKCQynNtXzlfpljh2GJ66r9TuO%2FMZHYwHs2KeKYRWaWVJTS2Xjm%2BIjhqyGVUd9Bx6aLib4oXQg07dII24HdHrV4VSni3zgFaz3zy9pGb%2FEFAKXB3vYQLU9%2By4cmQDI%2FRlVhG4CmZnmj9JNxNIx8TAC3ClrQ55jR53SuZ4GVmegq59PQH4b%2BGTxGvbKgm0zhtzBsDLMX7Gn1%2Fc1R%2FJqhPOoxzxJ8ByfjpUlj7gGcyuogb9sbwTGC29x82hZj7YlvJfbctUnIxlCqBXJvwSTW17D9PXfSG2HBma8lcyCE9B%2FKF376QKSGBuG%2FNtNUClsFSdjTi8kFxuf4fBt4rIgvevxwiQi3Ih97%2F7f2u5luYjLkDRTgNQpcKGdN55rKjBZxm7vDiptplDCR%2FpPX%2FkLMCphJhLXU7kqoNLo18HNztdA5We%2FComDSlHE57cpxCFOf2OA1%2BJd0%2FaebJElC6T5wiHfcyW2EyJTizU%2BHG7ed1pUB5h41gv%2BcUVuSZ9D5uLb%2FFCDLaFBAUP0XKDJcItSPe%2FgXp2hno7zzCnn1%2BSD4yM5a4fVHzSI4l7LEtIeBduVK8lNCQqh9Y6Heh5m5IOsdmCOZkx7AZgDAbs%2BVpB7P%2B16z1%2FvjNaMNGx67wGOqUBePtLo4AaI99ErMnw0eTdjfYHbkqCMdn4G05oDEitXk1FS%2FCgKjWtrlK56XFxEgN2uo56DWAufAM3zB1mNg9UDOV8vWvqL%2FnIsa8%2FwJp%2Bm9TgQ8jXYdlSC6yHOw2KDC0i5l9aTUStOhq%2FFzl7nu0OW5HYolZfkynMAUNyzeGbD%2BZaQGjYFjAPj0oqHOBllq7s9K2H6H5AxPkodoY10OrMu7laCMde&X-Amz-Signature=703eef16883b7b289ae476d5f5fdef9b98aab59808938b6ff62e312fa55395a3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJYLRDP5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDbynp%2BwYm5nEOjVOZY5470Bf8XobIrQcN0K2I%2B6gQSNwIgEwq7XsnZtMGQH7NHzZdgctVvCNn%2FrMp2XkgSzzxqj0QqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP9AyAtD70bfyu3VHSrcA9qJ6MEF8iwVaBv5xSb9YnxO%2FSsnkg%2B6O%2F8ydQ%2B6ncX9%2BCm7KwJWW%2FnDpm3QVorB66YbZIuxLYkvXI0Jzz%2BwLWneAHwS1ZzeQ7wHosFnpBvg1dcwYnCn8m9qVxTjodRfCWeXY2Gp4ITNZZfiVqfhnAam9J%2F69GpCTKycDWdvYEi7bROUrA3jGD4Q4T5u4vNBV1CtuYkIik4LPUjZyYOgNEzE4%2Fu7Q%2BJemFBZpHIV%2BuKxrmfIpAJaDKJAhIjbfVY9VkwAZU2LHjuEoXARbfSWbKc1SIts7n%2FOL3JbvgC4dYH1%2B%2BgbxCwmiqowpsOgYeAAgcpSXRB1H1i1Hz3ues6OjqLadFT89NsXN77qe4VLele02gwl8Lg89CabJO%2FpBKh%2FhAXHmLcSA8h%2B03POwDY2Op7K%2FR0NeZzNJulLQ5UvryJnXrnbuy861dTIOSksG8ttmv8gHYkdaRqrrLYr12FhuCsULvgwY04%2BAKCXl8weeq6Bl7TCbg2uxFdUENPPPLMxednHOlo2vlZ82a7PRef4Ljhi9h8vjlE9b9HL56X2DXwxlf%2FZXgAJ2fO5%2FtpZim0%2BoaKhaWiKVgvKZX8ut4jxwCgQ2AmWMWxSXAfYI9FPQCAPbDdjlvy2jd8uqnnFMJqy67wGOqUBNJSj1SAQaDnlaBGFJThtiBMYo5zPlEQPbYKPbM1Mac%2BuoPdR9CKNwscR41vbAgFfs4IPpj0HruX2c%2FlHpEhpChZsc1GXSfucAP%2BxBekJfuqU%2FKNMS7lJKIzamkLzTmNZHxNDwzYR6B5UKYCdn34tp0%2Fs1cPbDRwYzxAe4XgXiy%2BUZ0%2FPyHJOq8FOcHYPCRJ9xLhQZOUastgH8s%2BZyjr22XeFa2M4&X-Amz-Signature=7e1328ad54253bf2d7792c9ee58588a64266de95afbc3fa8e2a6fb81283572ea&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QODPP7N%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaz5uuxAZtm%2FmknnNWnZjXTqLi4iwmgtnFeVbYkGNIuQIhAMd1T%2Fm182X0HOS7jlMhJo0PD3oWa7PYMxoG2cfJoD9ZKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxe56DL204qfzELUWMq3AM3bqxAaILhbkHr7zs0%2Fk3ncnUTD%2BPz6g5MmrDLSGOVqzhXF5%2BnLxdCqXWp%2FNCULwfKoCmGKwk6a2ZGmz1hMuVSs39JxydKabdo22u3WhVehs5110L16LrtQMDzMBvHE2euHWDOEiUrzmseQ3ZUk3nGUtiPCl0%2FuE7yjfZRk%2BImHRTlRv10xvbiWt7PRI%2BdGLYeo3YqSmWns7uFdFujtefC6Lbq%2F1VtQzg6jEdlJ0Xfdmy93%2Fs0djgnngtazXblKdlmIY8FSmQjKNZPRKonX4qD%2FPbhhVgtS0aY5kFri%2Ff%2F%2FlPMAp9jygVWkHX17BJrciYd2OzrkRv9aPicNeLyrXDgbppX0MWSbUuudyo0FBjOPw9IjKOYr3D1H%2F8pCIPQbYuGAvslVqdEYts1P06yoW0NbV0azSZGG5QQBpoSpSAFl1%2B8woJBhPiKP%2Fag7zR8Yh%2FfHFm7J1p5eKDBL3VJ7npqd13ws0uYzwImElAke8XxzjFalcQ3VdXpGZFIRDdgCAv%2BMnKSAkwn6sLMndssGS%2Ba5L9OccMooX%2By0vI9kj8wJsLZyNTPLjQxkXIqUkRiO%2BSGRuCWHh%2F6ctrZ2MgIBkR3rQmjbU3p6Elabpmr3Ovs%2FDUYgxDTjWRExPdqczDJseu8BjqkARejL39nT%2Bax1iDvTB3XVt1Br8EaSOCqvA2gEFmj%2F0mpRj83l9ViVRsao0gkGxDiLp2F79hvnmrEs1GNdEmr%2FdMbXrJaLd8JHEje4t0znuMp7plob8xye1Ix85bbHXJme6pKL%2FBV47YXtRMbKrRKFp5ppmpuCUHPUh1zYt%2BiPIDKYDegrI3xbWxL61rCR4zV0Yd2AgQU7ctK%2FGC0zIftYw9Op0Ff&X-Amz-Signature=bd75c1b0fd9bddc27358939d8cb16f3aac5df0cb621015c1ce64f2eec02dc0cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPCSRKO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfAgCaBIKrNks6nk2DoqemdwJ2vweSihIL2dACj1dUCAIge5xykAcV603UkoihvaZP8QFBYynyE3tnTrvl%2Fj0Mz0EqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4u1PcbYd2mZ4FS6yrcA8Ice2h2jVpSKCQynNtXzlfpljh2GJ66r9TuO%2FMZHYwHs2KeKYRWaWVJTS2Xjm%2BIjhqyGVUd9Bx6aLib4oXQg07dII24HdHrV4VSni3zgFaz3zy9pGb%2FEFAKXB3vYQLU9%2By4cmQDI%2FRlVhG4CmZnmj9JNxNIx8TAC3ClrQ55jR53SuZ4GVmegq59PQH4b%2BGTxGvbKgm0zhtzBsDLMX7Gn1%2Fc1R%2FJqhPOoxzxJ8ByfjpUlj7gGcyuogb9sbwTGC29x82hZj7YlvJfbctUnIxlCqBXJvwSTW17D9PXfSG2HBma8lcyCE9B%2FKF376QKSGBuG%2FNtNUClsFSdjTi8kFxuf4fBt4rIgvevxwiQi3Ih97%2F7f2u5luYjLkDRTgNQpcKGdN55rKjBZxm7vDiptplDCR%2FpPX%2FkLMCphJhLXU7kqoNLo18HNztdA5We%2FComDSlHE57cpxCFOf2OA1%2BJd0%2FaebJElC6T5wiHfcyW2EyJTizU%2BHG7ed1pUB5h41gv%2BcUVuSZ9D5uLb%2FFCDLaFBAUP0XKDJcItSPe%2FgXp2hno7zzCnn1%2BSD4yM5a4fVHzSI4l7LEtIeBduVK8lNCQqh9Y6Heh5m5IOsdmCOZkx7AZgDAbs%2BVpB7P%2B16z1%2FvjNaMNGx67wGOqUBePtLo4AaI99ErMnw0eTdjfYHbkqCMdn4G05oDEitXk1FS%2FCgKjWtrlK56XFxEgN2uo56DWAufAM3zB1mNg9UDOV8vWvqL%2FnIsa8%2FwJp%2Bm9TgQ8jXYdlSC6yHOw2KDC0i5l9aTUStOhq%2FFzl7nu0OW5HYolZfkynMAUNyzeGbD%2BZaQGjYFjAPj0oqHOBllq7s9K2H6H5AxPkodoY10OrMu7laCMde&X-Amz-Signature=ab2b068fc81bef6a62cf03d54efb2eb1de86a3aaf6b013d2cb9af658bbca4f97&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPCSRKO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfAgCaBIKrNks6nk2DoqemdwJ2vweSihIL2dACj1dUCAIge5xykAcV603UkoihvaZP8QFBYynyE3tnTrvl%2Fj0Mz0EqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4u1PcbYd2mZ4FS6yrcA8Ice2h2jVpSKCQynNtXzlfpljh2GJ66r9TuO%2FMZHYwHs2KeKYRWaWVJTS2Xjm%2BIjhqyGVUd9Bx6aLib4oXQg07dII24HdHrV4VSni3zgFaz3zy9pGb%2FEFAKXB3vYQLU9%2By4cmQDI%2FRlVhG4CmZnmj9JNxNIx8TAC3ClrQ55jR53SuZ4GVmegq59PQH4b%2BGTxGvbKgm0zhtzBsDLMX7Gn1%2Fc1R%2FJqhPOoxzxJ8ByfjpUlj7gGcyuogb9sbwTGC29x82hZj7YlvJfbctUnIxlCqBXJvwSTW17D9PXfSG2HBma8lcyCE9B%2FKF376QKSGBuG%2FNtNUClsFSdjTi8kFxuf4fBt4rIgvevxwiQi3Ih97%2F7f2u5luYjLkDRTgNQpcKGdN55rKjBZxm7vDiptplDCR%2FpPX%2FkLMCphJhLXU7kqoNLo18HNztdA5We%2FComDSlHE57cpxCFOf2OA1%2BJd0%2FaebJElC6T5wiHfcyW2EyJTizU%2BHG7ed1pUB5h41gv%2BcUVuSZ9D5uLb%2FFCDLaFBAUP0XKDJcItSPe%2FgXp2hno7zzCnn1%2BSD4yM5a4fVHzSI4l7LEtIeBduVK8lNCQqh9Y6Heh5m5IOsdmCOZkx7AZgDAbs%2BVpB7P%2B16z1%2FvjNaMNGx67wGOqUBePtLo4AaI99ErMnw0eTdjfYHbkqCMdn4G05oDEitXk1FS%2FCgKjWtrlK56XFxEgN2uo56DWAufAM3zB1mNg9UDOV8vWvqL%2FnIsa8%2FwJp%2Bm9TgQ8jXYdlSC6yHOw2KDC0i5l9aTUStOhq%2FFzl7nu0OW5HYolZfkynMAUNyzeGbD%2BZaQGjYFjAPj0oqHOBllq7s9K2H6H5AxPkodoY10OrMu7laCMde&X-Amz-Signature=c9ff4b455e0531803350963f07e318e2a0d62493a15e67e06570f4b5560b48b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPCSRKO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfAgCaBIKrNks6nk2DoqemdwJ2vweSihIL2dACj1dUCAIge5xykAcV603UkoihvaZP8QFBYynyE3tnTrvl%2Fj0Mz0EqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4u1PcbYd2mZ4FS6yrcA8Ice2h2jVpSKCQynNtXzlfpljh2GJ66r9TuO%2FMZHYwHs2KeKYRWaWVJTS2Xjm%2BIjhqyGVUd9Bx6aLib4oXQg07dII24HdHrV4VSni3zgFaz3zy9pGb%2FEFAKXB3vYQLU9%2By4cmQDI%2FRlVhG4CmZnmj9JNxNIx8TAC3ClrQ55jR53SuZ4GVmegq59PQH4b%2BGTxGvbKgm0zhtzBsDLMX7Gn1%2Fc1R%2FJqhPOoxzxJ8ByfjpUlj7gGcyuogb9sbwTGC29x82hZj7YlvJfbctUnIxlCqBXJvwSTW17D9PXfSG2HBma8lcyCE9B%2FKF376QKSGBuG%2FNtNUClsFSdjTi8kFxuf4fBt4rIgvevxwiQi3Ih97%2F7f2u5luYjLkDRTgNQpcKGdN55rKjBZxm7vDiptplDCR%2FpPX%2FkLMCphJhLXU7kqoNLo18HNztdA5We%2FComDSlHE57cpxCFOf2OA1%2BJd0%2FaebJElC6T5wiHfcyW2EyJTizU%2BHG7ed1pUB5h41gv%2BcUVuSZ9D5uLb%2FFCDLaFBAUP0XKDJcItSPe%2FgXp2hno7zzCnn1%2BSD4yM5a4fVHzSI4l7LEtIeBduVK8lNCQqh9Y6Heh5m5IOsdmCOZkx7AZgDAbs%2BVpB7P%2B16z1%2FvjNaMNGx67wGOqUBePtLo4AaI99ErMnw0eTdjfYHbkqCMdn4G05oDEitXk1FS%2FCgKjWtrlK56XFxEgN2uo56DWAufAM3zB1mNg9UDOV8vWvqL%2FnIsa8%2FwJp%2Bm9TgQ8jXYdlSC6yHOw2KDC0i5l9aTUStOhq%2FFzl7nu0OW5HYolZfkynMAUNyzeGbD%2BZaQGjYFjAPj0oqHOBllq7s9K2H6H5AxPkodoY10OrMu7laCMde&X-Amz-Signature=10ae6aee37dbdc1da86ddd15a88c23373aa219e2f798532d0e4c9f74638c78bc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FD26XVT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC10wRwna%2BiVkoiHCC%2Bms4aQQvM7DPHjjclYzBIGzxJWAiA1Es7Vg2baatwhx4uwrGJp18jQNINqkkQkrSDduhNctSqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMImHQTh198FOIG6k6KtwDNMe082rrBQrjjvT1mf%2B5nuzM6tPqqKA6ePAokr262e4ylOhPsWEDWJwvM9VcJWRBKXBQoDhGqI4gTzddIAHDWn8ZOucPvbFcHPgC8osbpSNfZg1lZBg%2FOBR3Q7m7ylrFYA%2FgIHXvBHB8sxBmLQIMs%2F8CemmKrTSnF3OKqzwtXu3%2FhBX0SA6OJbfP6wGxKQo4Ll5OST1wKnZnwInKn4D3yxcoSqZz9IMDnM4X39CFVys%2BQFT8IzaS8VwtTBKjv7IaYcftJFnVC5Riy1BsoiJOBySXxT5Nt0TmJzEiU%2F67oWp1r0G6ROfQXQU7JX3Vi68FZFWFbGko5B51oyZc8yKVpEk8xTYoYh4enQx9ZYTRZDDpbY9sbqQMezFclXfOeYkJWjsgXV0SNoAGgrQycuiM9ArtJ9giAQ8VEkezZ0Cvp3LK0teklyZomci3uTb7Hqi7ORLbjuO5U8WFT10PyX15954%2BdePkRaXCOiGxgXpi6d0gHbaHVSD%2Fc8fwUecFOWRgQs4ixy2JkOqUtYEkKcLwbkItWiyf7G1awMnDha6T75LZo%2Bb1sgiWYu2fLEngo4NNFcLvMhAIoRz7GzcLFwQ4a4kgg6XVn%2FGyWypjDkZHoRDUpeoWw2Hec1wANyUw7bHrvAY6pgEqfFoKtab35TYhLi5JYziI2Nzmgs4GTcKcHvtGsiFek8WBRJvfV1f4Yn1sG15z3kWZlcCMahJvMd%2FkQx9xQ3gLTW6KR7D7Sd9dwzPkLZ6w1ECrQKFUeRV6XIC4nUFjZ%2BZjyaZvd4fjZWQk0OOl%2BENTMsCch49hgMV779UnjlkwsDbhEgCa2DxyaNHJtQBJ9nEQiACrzaMpvVkmF7j%2FIiOyPUb2suIX&X-Amz-Signature=10a5f880d01133dad9e37dbb827914b09820afd91a056bd3d90b890fe3a33e64&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDZG5AE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZmHONTw7kxL8AGvirk3Mmax%2BqlRqYwa0bjSUaTy6L9gIgM0dOBhpPPkxbDMrVEcMNpRxbJ05dCq4AJoBJMzqBwdwqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZv4VTdCOvLv8FklCrcA%2BePBELXsYG%2FW3jtKkWaCC8f25BZZ%2FlQt3DED4vw%2BmdQDJf8Bk4iaugDYNzNsdM4EgPEBTnPYXRlH706nB3sd0Y6pE0lRCfr5pEHVtAZCVLuw%2B4iSmWSC9aHFkzia%2BcmFAYNzUjfjKXK2JXaCTCTbVdbJ7h8jr81EYXcVB7fRrliLs3FoLLOdQjMkDFAbMTN3HR%2F%2Fu9ts9VYJFmrELNcG2f67bNtJeqTlrEKx8czoqTfTMUZODU9mu%2Bhb4yCoaKDNfVjk2h9ZY3ML1sA3naSscl3a%2FAY4D93maWB7NgqGsPPbcSIv73TRAktZ%2FWpQyKxfoBMRiY8xI35O5UAWqjjq8Js4imaHA9PEAaji3FU5SnR39JY10%2Be9loDlsLf22vXfpnHSnkBeLBj%2Bi%2BXOnNp8UPxsEGPJt%2F0v7euEx2z1n0%2FzycYKfGJxmOMP11fJYRnY%2FKWxLTWOH8J%2BbzrBNG8QUaYi8SyIzXwON%2FDkHJ9YaYngXThSpmK6O2RP0%2BzMYGymnCNTcSCRO7r%2B35uRgZDWop%2FYMhmz1aMuPB%2FOlPjCOjqlGM7dGvtyF99LaUzcy1IrSq1WH%2FMxLjbPpc6oFbuVRX7X2MfulGAv%2FkMAfvPromBWlG2Hz0%2BDlpCnwRpMP%2Bx67wGOqUBuxf0eLtjkgs9OLLhJNezxQkmr0NKgUVcAXNRaUJO1Arsy4d0yaBqCMuJZnt8fzTl2rhiqUqhey6dvJTMUTEZyXCmmq2OAfdKSbSypQ9UkfmFkmz99YclTqwQIWrJLe%2FNJ7I5Cccw6P1fK975KUMNM190lkSxYBOAwX7tVIYWqSXGVRdnLETmwPFlMZXXfR10%2BNGBcqzn4s%2BSi9rez3stKZlVj6Ff&X-Amz-Signature=c3d9fccb38392b3f50e297413d79a96195fb2c7698400ed9fbe8214415a463e9&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466233IJNWK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCa1iBz7UovwvLtCwKbcdds0fWEmOy5ShaGamo7Jitu0QIgERsczCPs7rpa2ctrOzOo3OZ19BpaxrDEbE1wSNBoDCYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOs8HaeWOIh90XY6jCrcA7txSt2HFD%2By7f7wqqNXXoc73ejqPKwq%2Fiqz4M0rRBP86i3qzkbsWIw1eMXhhkkFNoST8ZmRCjCW6sXN%2FDuaqOwZbHsgTA3%2BlFdPDuKbNDxexaHYpm%2FvSvH5RJsiXEMhAbLH2P72weJSnl94RoKa2aFQie5dnMgnfk4UpzhbOwJPAhei8AUj9gWGl5wTRPFc2uhWTi%2B5dsXBKaPS4oaCogkVVW0cBEk85Mi%2F7mQ506UJ1PULFrMxIO0VuRU6SR7Yfi0ubriBFpbDVOi%2FYxHMHYT5h505d7I6uBeHHhKIpyeAX0xQBwP8WCZLKRP7ShQ%2BRC3b3oBIkgGhlcYh7b7NlnzGRoTQmRvgmLbe2rXBPsuQ%2Bn28plJ%2FbTJx5j0vJsws09EAZpMAND9MYawHl5CoLuGcFgtk3CKDclbN15SH6GEnNd1cUG1YVeyxXtjUJzITQSwxl%2Fm59YMh5JZWUlwBLPlHzXXXzHUnZoEfALEvaVP7RA8IJ4NWJxRGxXanTgWOjdkOsQRW40sCCiNzlt6wUTczIAakOw%2FspGUZkQGC0A3Y1qoiIQMu2gkSqKjAzc89Hsz%2FxJUrEvXLvWUxye5L05nLncN02JRoADE0ddFDWsLf1F%2BCuQ7vT5zsJw30MMmx67wGOqUBSuqYIrXrRHZhailcNl8wzEFIUKMYRU7MWiWIYUrPnN4E8r72I3Yl4VrVpELzNxXtM67JWjIu%2FYRKaf58%2FeVlbo%2BqJr%2BWOH%2BuJJRb9aPdXbPC08SNTYNlb1rnWv3m7%2F%2FB5zipzaBpBG7pfF6Zhzg2YSQaolWPUVgsrJasg6YI1HyZwI3vi2QF9wwAoSH2IqvcgWHELW1nQnpo37%2F0YuV7bZcLdNw5&X-Amz-Signature=edbd793c80b37b1e636fcbe9724c8b5d4edb9698ca17b895c59c843c3017af51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQ6GAC4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBKG%2FrO0i8i8lnfKE4fTtkqxYyR8JRgtjVrL1K6iOIQgIgIyUxJ0n82mj39cnbmHGpr3LL3R0pLV70tWzCc0QJYJoqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPMi4HAuUWc6gh%2BJUyrcAyqFxGo81VieFfVTS8jZE%2Bis7NlEwxaRZjzJpqBOB2PWoKqnFUALXM3Zq0axTLoc1RZMtRG22kOXUBO7AqaZl3rqyiLyMlVq7ifoczSC3T5waSwjXcbxGyIka9krxa7DeZXdly9kw9nSMc%2F8VngOudZXWPkZG4M3p3B26WBFBogkRU%2FjrfqaBjRSR0EpKf1dIJhhniHWXpx5mjN7zOGTytG8Zcetfn4TEgmt%2FjT49Cz5he5U3V74713iL%2FHVdg1Urvij4LQ%2F8WziMPhKZOgrVk7e94BLQkFPwddd%2F3MB5HWwx0yD3CNBnQa%2FKAKQc%2FDxJobKM9iUJa6KcBsOLk8WHSaezQLpeFqxQAt4LQxjlNsBtbcY5c7C6ybxEpx3e7YaVrj0Wl4piwbXUq1MsKTyO9Qo3ZdlrJfTz81PhXzD6k9scdOWHS50UYc7BwL9PiPNTsQ%2BMwtOOHyyYbR0vIf%2BljXH4HMbxjPAgwMyLlPSTTqrteb1v%2FfoA%2Bie6TpK%2BUbEgov0sUHXMyq1fhFRRc1aeCLwQyuYcKuCnfham6A8VuOvxUs86uFtlxteGp2zIY0%2FTSPLXhzE382fWUVb5ghCI7LsTZMMLPK3Hjy8AwVb%2BvFbTpOHEIcJbWPpWB6qMMSx67wGOqUB8Q%2F3wKjZxPH2CfVD4ku69yNN0OQXxaby2V7nnPiZ6HCLL0HDE5KaQAjl6MIoSIfo8qaybgTJB%2FrPXCvfvfuUkNRnpAFDTnwbW5bfqRZREHoojxyyvZB8or9Iml1%2BcV%2FYyNXyETBYO20TK9oaW3Nuinu82XvSioa1W8UQJECVJdkMi842LuQZUzJ656iW1Oii83sg5z%2FJMXFhpj8aebJTy%2BxPrE2s&X-Amz-Signature=15b7b99cf1465f523ccf00dc2aa7ebf6d7f11c01f8e1131e4b0bfc9cf51bba05&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQ6GAC4M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBKG%2FrO0i8i8lnfKE4fTtkqxYyR8JRgtjVrL1K6iOIQgIgIyUxJ0n82mj39cnbmHGpr3LL3R0pLV70tWzCc0QJYJoqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPMi4HAuUWc6gh%2BJUyrcAyqFxGo81VieFfVTS8jZE%2Bis7NlEwxaRZjzJpqBOB2PWoKqnFUALXM3Zq0axTLoc1RZMtRG22kOXUBO7AqaZl3rqyiLyMlVq7ifoczSC3T5waSwjXcbxGyIka9krxa7DeZXdly9kw9nSMc%2F8VngOudZXWPkZG4M3p3B26WBFBogkRU%2FjrfqaBjRSR0EpKf1dIJhhniHWXpx5mjN7zOGTytG8Zcetfn4TEgmt%2FjT49Cz5he5U3V74713iL%2FHVdg1Urvij4LQ%2F8WziMPhKZOgrVk7e94BLQkFPwddd%2F3MB5HWwx0yD3CNBnQa%2FKAKQc%2FDxJobKM9iUJa6KcBsOLk8WHSaezQLpeFqxQAt4LQxjlNsBtbcY5c7C6ybxEpx3e7YaVrj0Wl4piwbXUq1MsKTyO9Qo3ZdlrJfTz81PhXzD6k9scdOWHS50UYc7BwL9PiPNTsQ%2BMwtOOHyyYbR0vIf%2BljXH4HMbxjPAgwMyLlPSTTqrteb1v%2FfoA%2Bie6TpK%2BUbEgov0sUHXMyq1fhFRRc1aeCLwQyuYcKuCnfham6A8VuOvxUs86uFtlxteGp2zIY0%2FTSPLXhzE382fWUVb5ghCI7LsTZMMLPK3Hjy8AwVb%2BvFbTpOHEIcJbWPpWB6qMMSx67wGOqUB8Q%2F3wKjZxPH2CfVD4ku69yNN0OQXxaby2V7nnPiZ6HCLL0HDE5KaQAjl6MIoSIfo8qaybgTJB%2FrPXCvfvfuUkNRnpAFDTnwbW5bfqRZREHoojxyyvZB8or9Iml1%2BcV%2FYyNXyETBYO20TK9oaW3Nuinu82XvSioa1W8UQJECVJdkMi842LuQZUzJ656iW1Oii83sg5z%2FJMXFhpj8aebJTy%2BxPrE2s&X-Amz-Signature=1376ad64bf317e824d1f2182419ba2c6a15d3ed6a6cc4f8209dcc099a6b6fae4&X-Amz-SignedHeaders=host&x-id=GetObject)

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
