

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCOEYVK7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhPOPPdnrLwR%2BLzOoX7eVAdRsjTLapMaH%2FjidgzqjxDAiEAs3IYi7tfEdDbXVVyG84iuoiQWAMq5mEDeBYjChVg8QQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOd0sAwPM4fuZs%2BqCrcA1UHqsZS2w6Y9z0f8vPMzDPr3NdtEbwgOleCMf1A67%2B%2FXI1%2FeKMFLh%2F6w2cWVL1lFzWgN9WIZi5y8XQVuekd7pvemz8WPUvOSd9MVJ9fQ8QNCdKMAlwhX2mfPfcc1GkPVE05e3wjjVf9rAV8dSlqqtkUEpp7Q8fDJ%2Bzln4efZ8Xz9kY%2BsoFI0Nf%2FYaSQKwE%2FkxCBIG9cp1W%2BVRc8X4mndH5G5yEZrwO1r05sfp6s%2F7YM4aRF1jiuSRoAPUKr9fpkhUKxfZ%2BjJzNm3elUC2XPmXZQsLg5hXw0gySheNcJ1Coa%2FvLmyuN0RJ%2BJNmEvkLcPmUI0WT3k2ug1hgrbUGaIXPNveCPSxyxCgrb30fcUi026pR9NE0IQqmMWkKOxdYFXaP%2FMA8ZHfe2JqwFRyXp%2Bv9UmYzYpVfXH5IzLyLOgkVlkD5l5eBrm8Ja%2FBSXIOjA3hT%2BH6bjhhAq%2BOmGWk%2F69%2FGocdamkV7zgtaPaVGwJZhoUtCIQVSRGbsKvSbR9vVtJv1yuty9UReU7XSeogKazcIi54OnFWGyTbmMEVGuoG%2Bq2RvjcPO%2FEuNbY2M3%2FoEojBBSPThqCvdS%2B8mdBODGeiobrkJRNcLHGO16MlZq9nxrysRYqkkRBUQXNLPAIMOv06bwGOqUBf9w8LWImxA9LRQdRo2ZXj1BdhLHgIuZzVj58y0bq2ykqyuEyfdOaNViV17kYBUUAdmLS0Lc2z01TlUFqadRgcUb4x9IXpc2JlfkkIk5oqkz3ctPj3mUKIqL7IhHpOroIQCcOSEP9PCfr%2B36Xw9xkEWL%2BHRhw8VaqiER7oHLIDs4Wjg7hiOYdrfDas0VbMwe4kORM7zdmEZHPi2doSwFRpSX4wUy5&X-Amz-Signature=d31ba0616f1c1bd5b6e666ffacb39ebcb44f1760ec710c02c31f6d5f0f785d27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCOEYVK7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhPOPPdnrLwR%2BLzOoX7eVAdRsjTLapMaH%2FjidgzqjxDAiEAs3IYi7tfEdDbXVVyG84iuoiQWAMq5mEDeBYjChVg8QQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOd0sAwPM4fuZs%2BqCrcA1UHqsZS2w6Y9z0f8vPMzDPr3NdtEbwgOleCMf1A67%2B%2FXI1%2FeKMFLh%2F6w2cWVL1lFzWgN9WIZi5y8XQVuekd7pvemz8WPUvOSd9MVJ9fQ8QNCdKMAlwhX2mfPfcc1GkPVE05e3wjjVf9rAV8dSlqqtkUEpp7Q8fDJ%2Bzln4efZ8Xz9kY%2BsoFI0Nf%2FYaSQKwE%2FkxCBIG9cp1W%2BVRc8X4mndH5G5yEZrwO1r05sfp6s%2F7YM4aRF1jiuSRoAPUKr9fpkhUKxfZ%2BjJzNm3elUC2XPmXZQsLg5hXw0gySheNcJ1Coa%2FvLmyuN0RJ%2BJNmEvkLcPmUI0WT3k2ug1hgrbUGaIXPNveCPSxyxCgrb30fcUi026pR9NE0IQqmMWkKOxdYFXaP%2FMA8ZHfe2JqwFRyXp%2Bv9UmYzYpVfXH5IzLyLOgkVlkD5l5eBrm8Ja%2FBSXIOjA3hT%2BH6bjhhAq%2BOmGWk%2F69%2FGocdamkV7zgtaPaVGwJZhoUtCIQVSRGbsKvSbR9vVtJv1yuty9UReU7XSeogKazcIi54OnFWGyTbmMEVGuoG%2Bq2RvjcPO%2FEuNbY2M3%2FoEojBBSPThqCvdS%2B8mdBODGeiobrkJRNcLHGO16MlZq9nxrysRYqkkRBUQXNLPAIMOv06bwGOqUBf9w8LWImxA9LRQdRo2ZXj1BdhLHgIuZzVj58y0bq2ykqyuEyfdOaNViV17kYBUUAdmLS0Lc2z01TlUFqadRgcUb4x9IXpc2JlfkkIk5oqkz3ctPj3mUKIqL7IhHpOroIQCcOSEP9PCfr%2B36Xw9xkEWL%2BHRhw8VaqiER7oHLIDs4Wjg7hiOYdrfDas0VbMwe4kORM7zdmEZHPi2doSwFRpSX4wUy5&X-Amz-Signature=67dd4425f1d03f0e851b6464abf68182b9a922472b76bc0b6027924514daada5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCOEYVK7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhPOPPdnrLwR%2BLzOoX7eVAdRsjTLapMaH%2FjidgzqjxDAiEAs3IYi7tfEdDbXVVyG84iuoiQWAMq5mEDeBYjChVg8QQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOd0sAwPM4fuZs%2BqCrcA1UHqsZS2w6Y9z0f8vPMzDPr3NdtEbwgOleCMf1A67%2B%2FXI1%2FeKMFLh%2F6w2cWVL1lFzWgN9WIZi5y8XQVuekd7pvemz8WPUvOSd9MVJ9fQ8QNCdKMAlwhX2mfPfcc1GkPVE05e3wjjVf9rAV8dSlqqtkUEpp7Q8fDJ%2Bzln4efZ8Xz9kY%2BsoFI0Nf%2FYaSQKwE%2FkxCBIG9cp1W%2BVRc8X4mndH5G5yEZrwO1r05sfp6s%2F7YM4aRF1jiuSRoAPUKr9fpkhUKxfZ%2BjJzNm3elUC2XPmXZQsLg5hXw0gySheNcJ1Coa%2FvLmyuN0RJ%2BJNmEvkLcPmUI0WT3k2ug1hgrbUGaIXPNveCPSxyxCgrb30fcUi026pR9NE0IQqmMWkKOxdYFXaP%2FMA8ZHfe2JqwFRyXp%2Bv9UmYzYpVfXH5IzLyLOgkVlkD5l5eBrm8Ja%2FBSXIOjA3hT%2BH6bjhhAq%2BOmGWk%2F69%2FGocdamkV7zgtaPaVGwJZhoUtCIQVSRGbsKvSbR9vVtJv1yuty9UReU7XSeogKazcIi54OnFWGyTbmMEVGuoG%2Bq2RvjcPO%2FEuNbY2M3%2FoEojBBSPThqCvdS%2B8mdBODGeiobrkJRNcLHGO16MlZq9nxrysRYqkkRBUQXNLPAIMOv06bwGOqUBf9w8LWImxA9LRQdRo2ZXj1BdhLHgIuZzVj58y0bq2ykqyuEyfdOaNViV17kYBUUAdmLS0Lc2z01TlUFqadRgcUb4x9IXpc2JlfkkIk5oqkz3ctPj3mUKIqL7IhHpOroIQCcOSEP9PCfr%2B36Xw9xkEWL%2BHRhw8VaqiER7oHLIDs4Wjg7hiOYdrfDas0VbMwe4kORM7zdmEZHPi2doSwFRpSX4wUy5&X-Amz-Signature=c7d107e34a17cd966fcebd627d4137c4d63b0d4d5c60e185c1845e5e9a204ca0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NHSFQUT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQPgzCDjLfdqukCl1qGHvqzUVlghODxXkECOxt122EcAiAflXeqjEdoN6OhM0e9x%2BWLpPv%2FNXvreT8vR%2BH1KlaY4yqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbk0N8TGfDD80kk3IKtwD8fJTEkDb1gmdj3XZBHhsuRzfF8zepWgifCk5fa0ymgFvT04as8eKIgiyZBpu6xwe%2B%2B2Pn1CEk%2FzpyZ0LwVHYjfJt9sJDNhHXyaud0lAcWiKWZ5X5qCR8tr07QsoQx3h24AwPaR4L6xRDspWTwYc2PILpiRvpcCkxB4j0AXWUZZLSwm%2FMDI%2BqMp0ppT1BGLfVNrG9ysxdoj6M1sZoKHaxYb4ALjQ1P6cTbSXPuyqnV5CTtn8O7dySgL6C5OllbI2Hl3ttJpTIfZBqKGOI6j9vNEx2QsZezLX1JwJI4rX6KMHqCk2vNErcNUKlkAH9seHNUO6G2PY%2B8Idxbb%2BjPY5vaDX2xSViV9CShdNcyI0momkdBQydaOXyavtLGORPB4EtFVGKYSq%2F83dAy1SgWXJDavGD30t89iw71nUx4523kexf%2FKIPQEd%2Ba%2FMX9%2BwNVUbvkyZzLK4zVKCUWh2%2F%2F%2Bqp3g1rq5nqG0VrKqIwjjutrKCbt0nnOJnD%2Fq0jV%2FoQ6FSzP1L%2FnfQAuv9oF4Js0ikUSr89G7XghloNzfBtTY1rXA2NcAznngkm9b7biUqQ7bl8NOhnSQLzT6QEnOB%2FxgZYg8PDow76pxR4%2BOiDuxczDztf%2FHKFAO5scF4AV5kwyvTpvAY6pgGH%2FBDNTyxaKR0%2BxaH%2FirzKsg5TO8IzI%2FlVS0WgL4tvczTKY3RnJnE4NpCnPiaJkixA9WVkAbNnqfs%2F%2BZEu%2F8GPyxf91AKJYa381tUxqh8mFPIT2MfF9bTq%2FKX5oBP4%2FREyri0tjiKdtR1TWa5pb4wXWKPJA7kj8edlbgQ%2FPBpEDod5SQgcD54cKNy5k65XqVjyVUKsDr1Dm6H3Uxza4WpZQEmplHZm&X-Amz-Signature=630c46f2d4869585c5b68f253d36ef9fb0c424a82ed3993c2f4d0904b7df738f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NHSFQUT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQPgzCDjLfdqukCl1qGHvqzUVlghODxXkECOxt122EcAiAflXeqjEdoN6OhM0e9x%2BWLpPv%2FNXvreT8vR%2BH1KlaY4yqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbk0N8TGfDD80kk3IKtwD8fJTEkDb1gmdj3XZBHhsuRzfF8zepWgifCk5fa0ymgFvT04as8eKIgiyZBpu6xwe%2B%2B2Pn1CEk%2FzpyZ0LwVHYjfJt9sJDNhHXyaud0lAcWiKWZ5X5qCR8tr07QsoQx3h24AwPaR4L6xRDspWTwYc2PILpiRvpcCkxB4j0AXWUZZLSwm%2FMDI%2BqMp0ppT1BGLfVNrG9ysxdoj6M1sZoKHaxYb4ALjQ1P6cTbSXPuyqnV5CTtn8O7dySgL6C5OllbI2Hl3ttJpTIfZBqKGOI6j9vNEx2QsZezLX1JwJI4rX6KMHqCk2vNErcNUKlkAH9seHNUO6G2PY%2B8Idxbb%2BjPY5vaDX2xSViV9CShdNcyI0momkdBQydaOXyavtLGORPB4EtFVGKYSq%2F83dAy1SgWXJDavGD30t89iw71nUx4523kexf%2FKIPQEd%2Ba%2FMX9%2BwNVUbvkyZzLK4zVKCUWh2%2F%2F%2Bqp3g1rq5nqG0VrKqIwjjutrKCbt0nnOJnD%2Fq0jV%2FoQ6FSzP1L%2FnfQAuv9oF4Js0ikUSr89G7XghloNzfBtTY1rXA2NcAznngkm9b7biUqQ7bl8NOhnSQLzT6QEnOB%2FxgZYg8PDow76pxR4%2BOiDuxczDztf%2FHKFAO5scF4AV5kwyvTpvAY6pgGH%2FBDNTyxaKR0%2BxaH%2FirzKsg5TO8IzI%2FlVS0WgL4tvczTKY3RnJnE4NpCnPiaJkixA9WVkAbNnqfs%2F%2BZEu%2F8GPyxf91AKJYa381tUxqh8mFPIT2MfF9bTq%2FKX5oBP4%2FREyri0tjiKdtR1TWa5pb4wXWKPJA7kj8edlbgQ%2FPBpEDod5SQgcD54cKNy5k65XqVjyVUKsDr1Dm6H3Uxza4WpZQEmplHZm&X-Amz-Signature=0f66a9c73527aa6e6103aaecc8ee0a8e1d30b3c4291fb73f95734c3bc8c248f1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NHSFQUT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQPgzCDjLfdqukCl1qGHvqzUVlghODxXkECOxt122EcAiAflXeqjEdoN6OhM0e9x%2BWLpPv%2FNXvreT8vR%2BH1KlaY4yqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbk0N8TGfDD80kk3IKtwD8fJTEkDb1gmdj3XZBHhsuRzfF8zepWgifCk5fa0ymgFvT04as8eKIgiyZBpu6xwe%2B%2B2Pn1CEk%2FzpyZ0LwVHYjfJt9sJDNhHXyaud0lAcWiKWZ5X5qCR8tr07QsoQx3h24AwPaR4L6xRDspWTwYc2PILpiRvpcCkxB4j0AXWUZZLSwm%2FMDI%2BqMp0ppT1BGLfVNrG9ysxdoj6M1sZoKHaxYb4ALjQ1P6cTbSXPuyqnV5CTtn8O7dySgL6C5OllbI2Hl3ttJpTIfZBqKGOI6j9vNEx2QsZezLX1JwJI4rX6KMHqCk2vNErcNUKlkAH9seHNUO6G2PY%2B8Idxbb%2BjPY5vaDX2xSViV9CShdNcyI0momkdBQydaOXyavtLGORPB4EtFVGKYSq%2F83dAy1SgWXJDavGD30t89iw71nUx4523kexf%2FKIPQEd%2Ba%2FMX9%2BwNVUbvkyZzLK4zVKCUWh2%2F%2F%2Bqp3g1rq5nqG0VrKqIwjjutrKCbt0nnOJnD%2Fq0jV%2FoQ6FSzP1L%2FnfQAuv9oF4Js0ikUSr89G7XghloNzfBtTY1rXA2NcAznngkm9b7biUqQ7bl8NOhnSQLzT6QEnOB%2FxgZYg8PDow76pxR4%2BOiDuxczDztf%2FHKFAO5scF4AV5kwyvTpvAY6pgGH%2FBDNTyxaKR0%2BxaH%2FirzKsg5TO8IzI%2FlVS0WgL4tvczTKY3RnJnE4NpCnPiaJkixA9WVkAbNnqfs%2F%2BZEu%2F8GPyxf91AKJYa381tUxqh8mFPIT2MfF9bTq%2FKX5oBP4%2FREyri0tjiKdtR1TWa5pb4wXWKPJA7kj8edlbgQ%2FPBpEDod5SQgcD54cKNy5k65XqVjyVUKsDr1Dm6H3Uxza4WpZQEmplHZm&X-Amz-Signature=4939bfe84c223ec7b738120eecf600c5bc8428892d5ad78fc16400b618e75129&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NHSFQUT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQPgzCDjLfdqukCl1qGHvqzUVlghODxXkECOxt122EcAiAflXeqjEdoN6OhM0e9x%2BWLpPv%2FNXvreT8vR%2BH1KlaY4yqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbk0N8TGfDD80kk3IKtwD8fJTEkDb1gmdj3XZBHhsuRzfF8zepWgifCk5fa0ymgFvT04as8eKIgiyZBpu6xwe%2B%2B2Pn1CEk%2FzpyZ0LwVHYjfJt9sJDNhHXyaud0lAcWiKWZ5X5qCR8tr07QsoQx3h24AwPaR4L6xRDspWTwYc2PILpiRvpcCkxB4j0AXWUZZLSwm%2FMDI%2BqMp0ppT1BGLfVNrG9ysxdoj6M1sZoKHaxYb4ALjQ1P6cTbSXPuyqnV5CTtn8O7dySgL6C5OllbI2Hl3ttJpTIfZBqKGOI6j9vNEx2QsZezLX1JwJI4rX6KMHqCk2vNErcNUKlkAH9seHNUO6G2PY%2B8Idxbb%2BjPY5vaDX2xSViV9CShdNcyI0momkdBQydaOXyavtLGORPB4EtFVGKYSq%2F83dAy1SgWXJDavGD30t89iw71nUx4523kexf%2FKIPQEd%2Ba%2FMX9%2BwNVUbvkyZzLK4zVKCUWh2%2F%2F%2Bqp3g1rq5nqG0VrKqIwjjutrKCbt0nnOJnD%2Fq0jV%2FoQ6FSzP1L%2FnfQAuv9oF4Js0ikUSr89G7XghloNzfBtTY1rXA2NcAznngkm9b7biUqQ7bl8NOhnSQLzT6QEnOB%2FxgZYg8PDow76pxR4%2BOiDuxczDztf%2FHKFAO5scF4AV5kwyvTpvAY6pgGH%2FBDNTyxaKR0%2BxaH%2FirzKsg5TO8IzI%2FlVS0WgL4tvczTKY3RnJnE4NpCnPiaJkixA9WVkAbNnqfs%2F%2BZEu%2F8GPyxf91AKJYa381tUxqh8mFPIT2MfF9bTq%2FKX5oBP4%2FREyri0tjiKdtR1TWa5pb4wXWKPJA7kj8edlbgQ%2FPBpEDod5SQgcD54cKNy5k65XqVjyVUKsDr1Dm6H3Uxza4WpZQEmplHZm&X-Amz-Signature=9b869464df9d9a1db581ac37520bf80216a563dcbae08c3efe3dd0334351d949&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NHSFQUT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQPgzCDjLfdqukCl1qGHvqzUVlghODxXkECOxt122EcAiAflXeqjEdoN6OhM0e9x%2BWLpPv%2FNXvreT8vR%2BH1KlaY4yqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbk0N8TGfDD80kk3IKtwD8fJTEkDb1gmdj3XZBHhsuRzfF8zepWgifCk5fa0ymgFvT04as8eKIgiyZBpu6xwe%2B%2B2Pn1CEk%2FzpyZ0LwVHYjfJt9sJDNhHXyaud0lAcWiKWZ5X5qCR8tr07QsoQx3h24AwPaR4L6xRDspWTwYc2PILpiRvpcCkxB4j0AXWUZZLSwm%2FMDI%2BqMp0ppT1BGLfVNrG9ysxdoj6M1sZoKHaxYb4ALjQ1P6cTbSXPuyqnV5CTtn8O7dySgL6C5OllbI2Hl3ttJpTIfZBqKGOI6j9vNEx2QsZezLX1JwJI4rX6KMHqCk2vNErcNUKlkAH9seHNUO6G2PY%2B8Idxbb%2BjPY5vaDX2xSViV9CShdNcyI0momkdBQydaOXyavtLGORPB4EtFVGKYSq%2F83dAy1SgWXJDavGD30t89iw71nUx4523kexf%2FKIPQEd%2Ba%2FMX9%2BwNVUbvkyZzLK4zVKCUWh2%2F%2F%2Bqp3g1rq5nqG0VrKqIwjjutrKCbt0nnOJnD%2Fq0jV%2FoQ6FSzP1L%2FnfQAuv9oF4Js0ikUSr89G7XghloNzfBtTY1rXA2NcAznngkm9b7biUqQ7bl8NOhnSQLzT6QEnOB%2FxgZYg8PDow76pxR4%2BOiDuxczDztf%2FHKFAO5scF4AV5kwyvTpvAY6pgGH%2FBDNTyxaKR0%2BxaH%2FirzKsg5TO8IzI%2FlVS0WgL4tvczTKY3RnJnE4NpCnPiaJkixA9WVkAbNnqfs%2F%2BZEu%2F8GPyxf91AKJYa381tUxqh8mFPIT2MfF9bTq%2FKX5oBP4%2FREyri0tjiKdtR1TWa5pb4wXWKPJA7kj8edlbgQ%2FPBpEDod5SQgcD54cKNy5k65XqVjyVUKsDr1Dm6H3Uxza4WpZQEmplHZm&X-Amz-Signature=5c5723ef511f3021ab2280d84877205297836eb5bffadd2b1b0c4beabf53e864&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NHSFQUT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQPgzCDjLfdqukCl1qGHvqzUVlghODxXkECOxt122EcAiAflXeqjEdoN6OhM0e9x%2BWLpPv%2FNXvreT8vR%2BH1KlaY4yqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbk0N8TGfDD80kk3IKtwD8fJTEkDb1gmdj3XZBHhsuRzfF8zepWgifCk5fa0ymgFvT04as8eKIgiyZBpu6xwe%2B%2B2Pn1CEk%2FzpyZ0LwVHYjfJt9sJDNhHXyaud0lAcWiKWZ5X5qCR8tr07QsoQx3h24AwPaR4L6xRDspWTwYc2PILpiRvpcCkxB4j0AXWUZZLSwm%2FMDI%2BqMp0ppT1BGLfVNrG9ysxdoj6M1sZoKHaxYb4ALjQ1P6cTbSXPuyqnV5CTtn8O7dySgL6C5OllbI2Hl3ttJpTIfZBqKGOI6j9vNEx2QsZezLX1JwJI4rX6KMHqCk2vNErcNUKlkAH9seHNUO6G2PY%2B8Idxbb%2BjPY5vaDX2xSViV9CShdNcyI0momkdBQydaOXyavtLGORPB4EtFVGKYSq%2F83dAy1SgWXJDavGD30t89iw71nUx4523kexf%2FKIPQEd%2Ba%2FMX9%2BwNVUbvkyZzLK4zVKCUWh2%2F%2F%2Bqp3g1rq5nqG0VrKqIwjjutrKCbt0nnOJnD%2Fq0jV%2FoQ6FSzP1L%2FnfQAuv9oF4Js0ikUSr89G7XghloNzfBtTY1rXA2NcAznngkm9b7biUqQ7bl8NOhnSQLzT6QEnOB%2FxgZYg8PDow76pxR4%2BOiDuxczDztf%2FHKFAO5scF4AV5kwyvTpvAY6pgGH%2FBDNTyxaKR0%2BxaH%2FirzKsg5TO8IzI%2FlVS0WgL4tvczTKY3RnJnE4NpCnPiaJkixA9WVkAbNnqfs%2F%2BZEu%2F8GPyxf91AKJYa381tUxqh8mFPIT2MfF9bTq%2FKX5oBP4%2FREyri0tjiKdtR1TWa5pb4wXWKPJA7kj8edlbgQ%2FPBpEDod5SQgcD54cKNy5k65XqVjyVUKsDr1Dm6H3Uxza4WpZQEmplHZm&X-Amz-Signature=35ed6d25712aa6d4fd6ba87a5263d30024c729bd3ec56367c3d7aa29baa6ae7f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GYI2KAP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtwW1sszot7P%2F0hdNieUsx6LtYy%2FvIzKaWhDIg6OypaAiBOkW3WLJp%2Bm4PDKn2axZ%2BQ49nrHNa5fVn%2BiR9xqKE6QyqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY22X9I9uJm1asJO4KtwD2T7WqdZI%2FcoHTfpXsuHwvPVfeg0zLbPkY6BhVPSZs7XEe7kWuFUoCQR7b9EznM3znEapk%2BRjyal24%2Bwk6m7VwqwvR7J3ZbYje2IGrRTERx4j5DpOaoud%2F2hxOT1RtkDFDQYmPIgXd8Sk%2FWAxlVJQcNzLhEUTSFwO1C%2Fj6sjkTgID0N9WoM3nOLXl62gaUS700R24TQYb3CFy3U72lu%2BwDkQBklF3FEGzGpSRUF2hJDD7jqRgtwpgstxcygP7g%2FYIsdqU5lw2%2FJ5nWEbdsMK350ZDp%2BnwxdTk0rg7zIgyMjDRzPv3JGKo1bkNSeQ3eazvgtzDQXK0FEGyBp2QyqiywBkmece1aRgYvnbruBq5Op%2BV8lXa0X%2BHkjSVRPry0q1s4z6fi0jkOyWpwi%2BDEN9Tkk7KYHSajJ4HQrC5DRLG5e2b7NOil4nrGqnKHE3B%2FLgWOlHwpg4zxY4pMX%2Fu08h6U8DOqaDRv%2FM4o1THd1ghh2eqIe7yLtS%2FKS%2BIZo%2F%2FAIw10%2F29L6QClCBACM01%2FXNuKG1l4WxjtJj5mbpuSxe8dK3TQqBE5FwRvzIqFQ1V9pitqVu%2BHfdiqGARQMV%2BWw1qzI6USGhbmSQsYKVIbCIlMRbCd0IXOYEFBX1hh6Qw%2BPTpvAY6pgH1%2FkxxPAiVygqknJYqxqGVvcIH6iqbUn3iVe1BDG7n0YmHxfKi1LFtlFZeEPB0MoZY0JaekDe4MllI%2BGvZzMBLlHZlWQRpuEO9k%2BbKaoz5oFRQYhGjyxB1wYw7blv4E%2BBOXTRjcuvY%2BLzDCJYpk%2Fgv7m1AkAeF%2F5j3nSmIEvHOmYG809pui8yxuTiKv6ab8eeK5lTsJqb2wGzHr2%2Bw5ObfjXUkjXGA&X-Amz-Signature=0b1658a895937111e7703fefa2ef31c7f6ccf2314c10a8f31d36c46e9c7fc19d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FK2GWQ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICqrmnw0sVat4XgJUL5yW2GCsmbhUdipZqpb4OcwDszxAiEAxtpOof4MHN3e%2FNYfc1OG9PkDr8npjWYEo3uJowEknkIqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB4Ojinl6puFBq%2BmdircA%2F4iQOgmCvG0S0OQLOCgAh3F15rpWCHTIBbpD2TKiHoN5xwWsIqDanhpg98cj6iml%2BIP0pAjOvvxrAl98%2BaO4yPbgbBFEr4DLtkySuVwt%2FJQUsaCgS3vUFzs3AOPOunTEw4bFZ3mJdtpfXvZxic7LGYzuYXraRY7T4YC3lQ8z3sSLTg4cEJFD4Ve96vCXNl4vzqXXD0fflMfzDNSSfBjYsZe8rQr6Vgx32%2BOWln0hX18ea3lNP1YffPJ1%2B55UM0ZRSw0H0WKsaUUTDowZi4zlxmDaS4g7F7FHZACvuJar%2FQCXwd%2BF5PRrSd7F0Er5e8xOcKqpDnnp8O5WCqQ6ur3P8C8OCbU8Jd%2BGk8D8AL53HpnAhW4dUf0WyZM0k9a1aiNUvW64p3IsnagAWtx%2BwivJbPDHY4XehAwlorfBS4A%2BJItnjjL0AcvldEcbtApzF%2B1aTX0zia%2FLo%2FQ2DyzmJVsT45tzjtJ180tWyjQEKwJxeJ9MlEvDbqPfNOS4Q3%2B1Dc4gOyyKCqi1cqGCac7Ai%2FXeZEhiW547B6ii%2BuXxe2avzUOHww97jLtdVo7cKTitIisKS3BviGZ012%2BT50oLFGtbNpmDRdCpZHQrDBfUazeov4KxMGM7%2B3uFCm301%2FNMP706bwGOqUBuYeleso3gdcMHOTB8rINFk0H9Lp3FSzomaXpA7pRk2YnKpyKYu2LEpBU1aYAFJjj2muLpBvPacdk0KFZEn%2FBCluPC8GOopa4%2FTxY1o6Nm2XHPicgxFZvVgCJH2M2PfuLVVP2jmm%2BcxBF7%2FvKPvtUXXhSYxX6fJsvTpj2lD0DERKn3efKyDW7V5anY7Zl2lb4wlQDjVLzLJjxwsEVh%2BbaaKcbsGCa&X-Amz-Signature=1da54bb435d6a1fdbb1afe5803330de677922b332395f30017e020440b6ed92c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NHSFQUT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQPgzCDjLfdqukCl1qGHvqzUVlghODxXkECOxt122EcAiAflXeqjEdoN6OhM0e9x%2BWLpPv%2FNXvreT8vR%2BH1KlaY4yqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbk0N8TGfDD80kk3IKtwD8fJTEkDb1gmdj3XZBHhsuRzfF8zepWgifCk5fa0ymgFvT04as8eKIgiyZBpu6xwe%2B%2B2Pn1CEk%2FzpyZ0LwVHYjfJt9sJDNhHXyaud0lAcWiKWZ5X5qCR8tr07QsoQx3h24AwPaR4L6xRDspWTwYc2PILpiRvpcCkxB4j0AXWUZZLSwm%2FMDI%2BqMp0ppT1BGLfVNrG9ysxdoj6M1sZoKHaxYb4ALjQ1P6cTbSXPuyqnV5CTtn8O7dySgL6C5OllbI2Hl3ttJpTIfZBqKGOI6j9vNEx2QsZezLX1JwJI4rX6KMHqCk2vNErcNUKlkAH9seHNUO6G2PY%2B8Idxbb%2BjPY5vaDX2xSViV9CShdNcyI0momkdBQydaOXyavtLGORPB4EtFVGKYSq%2F83dAy1SgWXJDavGD30t89iw71nUx4523kexf%2FKIPQEd%2Ba%2FMX9%2BwNVUbvkyZzLK4zVKCUWh2%2F%2F%2Bqp3g1rq5nqG0VrKqIwjjutrKCbt0nnOJnD%2Fq0jV%2FoQ6FSzP1L%2FnfQAuv9oF4Js0ikUSr89G7XghloNzfBtTY1rXA2NcAznngkm9b7biUqQ7bl8NOhnSQLzT6QEnOB%2FxgZYg8PDow76pxR4%2BOiDuxczDztf%2FHKFAO5scF4AV5kwyvTpvAY6pgGH%2FBDNTyxaKR0%2BxaH%2FirzKsg5TO8IzI%2FlVS0WgL4tvczTKY3RnJnE4NpCnPiaJkixA9WVkAbNnqfs%2F%2BZEu%2F8GPyxf91AKJYa381tUxqh8mFPIT2MfF9bTq%2FKX5oBP4%2FREyri0tjiKdtR1TWa5pb4wXWKPJA7kj8edlbgQ%2FPBpEDod5SQgcD54cKNy5k65XqVjyVUKsDr1Dm6H3Uxza4WpZQEmplHZm&X-Amz-Signature=9ea9903dffd65f9a059f323820c7c8200a65e3c289434ef475a5e7064ad8ffe7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NHSFQUT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQPgzCDjLfdqukCl1qGHvqzUVlghODxXkECOxt122EcAiAflXeqjEdoN6OhM0e9x%2BWLpPv%2FNXvreT8vR%2BH1KlaY4yqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbk0N8TGfDD80kk3IKtwD8fJTEkDb1gmdj3XZBHhsuRzfF8zepWgifCk5fa0ymgFvT04as8eKIgiyZBpu6xwe%2B%2B2Pn1CEk%2FzpyZ0LwVHYjfJt9sJDNhHXyaud0lAcWiKWZ5X5qCR8tr07QsoQx3h24AwPaR4L6xRDspWTwYc2PILpiRvpcCkxB4j0AXWUZZLSwm%2FMDI%2BqMp0ppT1BGLfVNrG9ysxdoj6M1sZoKHaxYb4ALjQ1P6cTbSXPuyqnV5CTtn8O7dySgL6C5OllbI2Hl3ttJpTIfZBqKGOI6j9vNEx2QsZezLX1JwJI4rX6KMHqCk2vNErcNUKlkAH9seHNUO6G2PY%2B8Idxbb%2BjPY5vaDX2xSViV9CShdNcyI0momkdBQydaOXyavtLGORPB4EtFVGKYSq%2F83dAy1SgWXJDavGD30t89iw71nUx4523kexf%2FKIPQEd%2Ba%2FMX9%2BwNVUbvkyZzLK4zVKCUWh2%2F%2F%2Bqp3g1rq5nqG0VrKqIwjjutrKCbt0nnOJnD%2Fq0jV%2FoQ6FSzP1L%2FnfQAuv9oF4Js0ikUSr89G7XghloNzfBtTY1rXA2NcAznngkm9b7biUqQ7bl8NOhnSQLzT6QEnOB%2FxgZYg8PDow76pxR4%2BOiDuxczDztf%2FHKFAO5scF4AV5kwyvTpvAY6pgGH%2FBDNTyxaKR0%2BxaH%2FirzKsg5TO8IzI%2FlVS0WgL4tvczTKY3RnJnE4NpCnPiaJkixA9WVkAbNnqfs%2F%2BZEu%2F8GPyxf91AKJYa381tUxqh8mFPIT2MfF9bTq%2FKX5oBP4%2FREyri0tjiKdtR1TWa5pb4wXWKPJA7kj8edlbgQ%2FPBpEDod5SQgcD54cKNy5k65XqVjyVUKsDr1Dm6H3Uxza4WpZQEmplHZm&X-Amz-Signature=7107207688e9671706c387f34d2879216ccbcde3e1bb864bff14da997e4241bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NHSFQUT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQPgzCDjLfdqukCl1qGHvqzUVlghODxXkECOxt122EcAiAflXeqjEdoN6OhM0e9x%2BWLpPv%2FNXvreT8vR%2BH1KlaY4yqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbk0N8TGfDD80kk3IKtwD8fJTEkDb1gmdj3XZBHhsuRzfF8zepWgifCk5fa0ymgFvT04as8eKIgiyZBpu6xwe%2B%2B2Pn1CEk%2FzpyZ0LwVHYjfJt9sJDNhHXyaud0lAcWiKWZ5X5qCR8tr07QsoQx3h24AwPaR4L6xRDspWTwYc2PILpiRvpcCkxB4j0AXWUZZLSwm%2FMDI%2BqMp0ppT1BGLfVNrG9ysxdoj6M1sZoKHaxYb4ALjQ1P6cTbSXPuyqnV5CTtn8O7dySgL6C5OllbI2Hl3ttJpTIfZBqKGOI6j9vNEx2QsZezLX1JwJI4rX6KMHqCk2vNErcNUKlkAH9seHNUO6G2PY%2B8Idxbb%2BjPY5vaDX2xSViV9CShdNcyI0momkdBQydaOXyavtLGORPB4EtFVGKYSq%2F83dAy1SgWXJDavGD30t89iw71nUx4523kexf%2FKIPQEd%2Ba%2FMX9%2BwNVUbvkyZzLK4zVKCUWh2%2F%2F%2Bqp3g1rq5nqG0VrKqIwjjutrKCbt0nnOJnD%2Fq0jV%2FoQ6FSzP1L%2FnfQAuv9oF4Js0ikUSr89G7XghloNzfBtTY1rXA2NcAznngkm9b7biUqQ7bl8NOhnSQLzT6QEnOB%2FxgZYg8PDow76pxR4%2BOiDuxczDztf%2FHKFAO5scF4AV5kwyvTpvAY6pgGH%2FBDNTyxaKR0%2BxaH%2FirzKsg5TO8IzI%2FlVS0WgL4tvczTKY3RnJnE4NpCnPiaJkixA9WVkAbNnqfs%2F%2BZEu%2F8GPyxf91AKJYa381tUxqh8mFPIT2MfF9bTq%2FKX5oBP4%2FREyri0tjiKdtR1TWa5pb4wXWKPJA7kj8edlbgQ%2FPBpEDod5SQgcD54cKNy5k65XqVjyVUKsDr1Dm6H3Uxza4WpZQEmplHZm&X-Amz-Signature=e02d92e3edbce439a6f57c0a28cf35bb9c191caa3347387271209a89722cf1f3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBNDPHHN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1pZ38ZT6VLHbouoyVyXR9wt8tjgnIaqhRPzhdXrc0WgIhAKzA79LhihW7uQR0GA4vOYQ3VdyDVhcICvwWHHWgRhfwKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXuS44xxnb1J7BtDMq3AOKuERgkqIAxOKAAGGx%2FOq%2FvZfrHoeVPbeOIUUBPHiJMtwQ8HsmT0I%2FZY1pdFJdHEt2AhE4WrRpubrPLTn9OCuZzNFXkHYd9L%2F41zIXi6noLp9N1uekFbumtKD9R84AfW7EBcE%2BGYy4%2FPdWhHu6zfc0%2FfYBWdlSBKDy0t%2FwHYvZzsaa9g7JpO3uMJlQI2P3YT2Yjjo1uxha979ZS1dgqwu0e%2FqA6gmnDR9zvAkAEcNKe4JEIVLcjoy77RHSlFgZ4FxYpfXephpT3SMJn85ril1fXhSrwAUfmrGZqNR2NZeuR31mMqFgI%2FAPpyZat7mW4vvaBhQytV5FBIuLXYg7ufuPhKlGzW148of%2BbB%2B8TuA6fAtjyTHh%2BaHY7O%2BJv%2FUvkmrku2ntbmteGTF77bvKMnqzVYcP9mySGgJAxXUaTuBer5fRPeHfq%2BLRiNu69qq8U3lZORtcT3aT3xg2SgAd8mTjdQZIrgj5bvL9F3bkp9P5xk0ktWFfBkWAAg70VE65k1BfrOV0IwcQA6qcBevq%2FyDdpFk5Z4IoyjBfEbV3MGP6C3Ksfb1X8Ng0oqUNplt6OQzto7mXQw6%2BYugF9VV6wfEkVkPq5ls6gu%2F3oN701gDnVH2da56GBPC%2BKJcFvTDT9em8BjqkAWb3IWJHqOu707vLh7YicM7JXrkAi9CrFwjw0ktLD%2BY4CARGPCEFxjtyMZm6bDz9lNpZwvStT5UCSTcwxDMGcJr9a8VEsN%2FdteJ%2B4DzdHGbKaF82UKqPtCKJb%2FBRyovQkfiCNrXwfCLLJR72eETzZqJQ8J7BAAvriVoG%2BzXHOM3zrbANolCxKgFhNWEeVRoU4sYJtVaJES72U%2FRlvHytsIYjb2yS&X-Amz-Signature=72e4693901e60c6a8a972afbb554df4357cf5ed0c8b06f33aa6c9fa6ab7ef97c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYBVOOV2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWKkPaMVaCeiPcTuj4wBSR9qwFFruDcpIMeNMbqchGuAiEA%2B9okOTk85Vo8xVzc8JNWFyUQlmAVUMuUgdTOw2%2FYkLQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDefn4WTpckbInONRircA%2FCKFCSlklWC6jxdlymiq4v4CZEBRhW1rcm%2FueT%2FAG3Rvwen%2BhR3I3k5IXjX8JrjvUXquunOKZ4gohRXiHLEasT5kA0YqJ2bzdj3Zcb8tA9MNkLpWHqC5wI54dzyfIhtVEIYi86OgxJOic4kzk8AaP1YRKOTznYMyYBBv3kf4F5d2c2Rfr7jUY995gggFiN3FFtuKwMFZtlqmmLHGLffFw%2FP%2FpZSlEvnFVxtKRfd8dkddRE4CMvfx02AyBmkKbMqqHpUuerhCIxa98eh8siMqv2Zq5r3YIOE48FZceAEy3DZVJxAlD3slRMKL8AdUd0Q%2FKLepoT4fykud4mbSRtZtls8z0RKrdchUKXyUV%2BNFsFjm8SGNzw5BVakIK9uF%2FVBZ9QvY2O7L0ds4PgrdCuj94XpFfUkOVZqbuukjQN9CiN52WPK%2Br1kn4ocw4c5G1oMW9ohPxMqyDFaujPgyA62ZeP2OuNjjK0kL8kwORY6M3TOjzgD0ewq5YxDv3V%2FG%2FQKNf7b5gKrzaZNS6qJnBks%2BGgVvMdh5Tfms1rxrSh3V6eI3jdSpuWZf%2FW7fKuBauqeYDs2ER3DtqdEle33XWRr42ztkWbgFnILIkhZ7ByKBx5AuasMBTIbtlCRNyuVMPf06bwGOqUBrkNeEJSnZ5EMm7z36%2F0Mm0apCn3T8Wntc7VG%2B5VTVyxfCnY2OD9Kf2XnNVym9efqml2PN2s6FtpRFQa9Z0XNMwqW7d%2FkHu8LZ0aSCEus5ZE1y1wfHmaoi93GahjnIRFZXf6qPgfKHh6C1vxxUIksfvY1iVYE%2BDzRO%2BlrcfpH7wNw%2BXGxMHtsNJxo5IlkBMShWoFmBwpBaNQxKeYtELoaWi3jecdA&X-Amz-Signature=a8cffd1bf7630eebab048fec3887c0f5a6ae9960ed08c2af39b2e0fa020f4a3d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFBEQUBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGiitHfW6Fzo8XSC4bkezK2IRPIQIgGkYWwStRpZawhQAiEAkf2tNngjvd%2F552UKIK0NeTu9%2FSg%2B5As2hq%2FR1UPUT3oqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE9Lt3sL%2FmjsZf3iUSrcAy01%2FCSqUk2pORgL2Up5cQF4XwUnSfwRlrDfV9QkUSUOkwi7ZZeuuq5FzPenDzHPzotOiZ0ig%2FqKRLNjyFz0j9JuwN5hOc%2B2J5QfwBgwxwDaBqcM18aVy1k4%2Fl6nf3qjNqp0kbdqiM%2Fh4lfrHAdhyCU1mbHPrDPV7Zd3QOcori3YL4rJt%2BPjuq7xDsA8SwXgZj5ttd3VIS4rRGTTyc0EKI8AZJFNjDy2YJsN9IJDP2zQKuGVfJYuGH53dcfe4JJu1yrfzL%2Fd0WwmT7BaYK4i%2BJZtThoexW6whuZAZGMENEJm4nnxG7g0hShynbL136xQsAiPdzmpaXuvKtGXNtWPFrBd9ZNwYf5WNhitRfyyIsWsHMU56Q11rJQVPzMhItlKw03%2FnXAor5kQJ7pHaNy7GT7ZH7yXA4hU6kv%2Fzzs%2Ft2rLNKs4yB%2B%2FcmTS7AREfGIs0J0zVpOXxjGlAnyC%2FHqds5Upz%2B%2FmEwoI%2B8ybuP00TNGTcPxUySFkDTZusg%2BclZgROkZtH9X3YO2aH%2FIaNGNBpDoCxEZYBmTGaDvUxHbUyAYzVR2AxNpAABZl4FeUoGIELBk0SDoU35JaaskSIR1IEp5k2r4x52uAMAznDxSS%2FDPXy5XZRk3sn3DLu9nUMOz06bwGOqUBndg%2Bb3PWOrKShgC2yT8FheKCp3lRDB5iuGRHkJJNbTjoGNeq5aTJ7xJiKI8c%2BzmA%2BbKa%2F0sKPTr70vbjZ4lqXc8n7KYUkTqP9pKSz92fW9No2gF7rMf4O%2FS0gypw83X3p06ppqIr0e2UbnStv0I7Rcx27bhKX340BG%2FWH2MWg2ssNO0SDhLDmJu8tsMo%2B8X4NfY4H6kvNWDOFCtExX5wuWVK%2Fh6r&X-Amz-Signature=b676dce0e0d8a9f8351cd7db6669c84749a1e53a6eb6121c5050b52243f678c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662NQDPF2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCk5HZoGn%2FaDtFNDvsyOX5ddF8ZGnsyKHnQ7BmdedQeEwIhAMKBNiou0hsbJTC9oEsrLKT1I1lPQWfk9LuDuWoKI3CIKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXmeUESfsTy%2BgFxi0q3AMjzNUC1iBTyFyO8Thstd2U%2Byhi6kwY0Ixlj7%2FVJhy65Ec9nbANnQlRIdCJwYvW2JORf2kSOxgK2bCo8SwC2w8M%2F6BaSvXTu22%2BEajYW7irngdu6ooqs%2B0vRZBFFQJudU%2F0jPitg4XuydBls28NWBSilPe3TnAuSHRtbtq7TsTLGsQlQsscrQDD2ARZkUgOqWS6MKNVI8u6LcHOFLPrsvFSToPCeOfGOLyRRAOFXjpY8KetcY8T%2FALOVsWAw%2FJg6ZKxYg1k%2BBn6YDqATB7VD0Qlna4OnxOWIc3m6ML9TNE%2B0Ng4bfL2NSSm52OqcvxilLYqp98CxWanGd%2BHmPH9O9WFgN9HpIZIOpccDVXrUpGKfFHQHY01zJsMi%2BtXQW2RaOBYpTM%2B42jU0qq69vL1bXlC0XaoRhPtKqkyBmpbhvT53D9jHJUiXZrR8UZNsipSCCDvv11%2BE4PZ3AEW3O24aYoivYOVcjAtqV2JSdOCEm5k1LQnPVixQ3Sd4%2BAgXmre1P9qXiONFM4rE%2BeKDXVmVLZu8d8Xc75I9PI2v98f7PX6iOE%2BpyzcucasuKaPGKcqOQsb4UG8k6T4rPwFJJAlNoc%2Bs0jbkkdCQqKTl%2BhcZYYfvujp5ZuWRWfbICwg8zDA9em8BjqkAfnBAZPFPMQ%2FoUfeOtlneep3YPNeLecuBds5tQXwP%2F%2BimGWWgVePPMRyWQz3hzQxuSGn87mTuSBKF1DqMqQLYqLelElqn56bLagkxjYVZpZDAmY%2B6DmBDyh%2FK7szh%2Fv2drQQ9W4zqQPGEFQO4otvJIKT3znn5gjGYZ8kfj9rWh%2BCHQ7xzcYD0An5rR0ZrL%2BvHgCia5lIPtjL1LhV7nC8uwvSvmk5&X-Amz-Signature=a59e444dea3ddc735f312cb24555f541439089e04133e1440339fbeec6dbf53d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662NQDPF2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCk5HZoGn%2FaDtFNDvsyOX5ddF8ZGnsyKHnQ7BmdedQeEwIhAMKBNiou0hsbJTC9oEsrLKT1I1lPQWfk9LuDuWoKI3CIKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXmeUESfsTy%2BgFxi0q3AMjzNUC1iBTyFyO8Thstd2U%2Byhi6kwY0Ixlj7%2FVJhy65Ec9nbANnQlRIdCJwYvW2JORf2kSOxgK2bCo8SwC2w8M%2F6BaSvXTu22%2BEajYW7irngdu6ooqs%2B0vRZBFFQJudU%2F0jPitg4XuydBls28NWBSilPe3TnAuSHRtbtq7TsTLGsQlQsscrQDD2ARZkUgOqWS6MKNVI8u6LcHOFLPrsvFSToPCeOfGOLyRRAOFXjpY8KetcY8T%2FALOVsWAw%2FJg6ZKxYg1k%2BBn6YDqATB7VD0Qlna4OnxOWIc3m6ML9TNE%2B0Ng4bfL2NSSm52OqcvxilLYqp98CxWanGd%2BHmPH9O9WFgN9HpIZIOpccDVXrUpGKfFHQHY01zJsMi%2BtXQW2RaOBYpTM%2B42jU0qq69vL1bXlC0XaoRhPtKqkyBmpbhvT53D9jHJUiXZrR8UZNsipSCCDvv11%2BE4PZ3AEW3O24aYoivYOVcjAtqV2JSdOCEm5k1LQnPVixQ3Sd4%2BAgXmre1P9qXiONFM4rE%2BeKDXVmVLZu8d8Xc75I9PI2v98f7PX6iOE%2BpyzcucasuKaPGKcqOQsb4UG8k6T4rPwFJJAlNoc%2Bs0jbkkdCQqKTl%2BhcZYYfvujp5ZuWRWfbICwg8zDA9em8BjqkAfnBAZPFPMQ%2FoUfeOtlneep3YPNeLecuBds5tQXwP%2F%2BimGWWgVePPMRyWQz3hzQxuSGn87mTuSBKF1DqMqQLYqLelElqn56bLagkxjYVZpZDAmY%2B6DmBDyh%2FK7szh%2Fv2drQQ9W4zqQPGEFQO4otvJIKT3znn5gjGYZ8kfj9rWh%2BCHQ7xzcYD0An5rR0ZrL%2BvHgCia5lIPtjL1LhV7nC8uwvSvmk5&X-Amz-Signature=1d5984784b84238802eeaf63154f9f35eb335a4d10ee2b2b75e42f96871f5875&X-Amz-SignedHeaders=host&x-id=GetObject)

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
