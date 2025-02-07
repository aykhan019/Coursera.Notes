

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PAOVNEF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIHa%2FzqwN4iTwxMA%2FBbEUTk8jQN1ViSAaigl5tHNcIfNrAiBE%2BxYH072QJ%2FB2XjbHwuGzZ4K3D11SGub7wK7p671doyr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM3GKyXuzzJA7rARshKtwDX6mPZjVtKZLlOlo2v5sbSXRRDISqY3k%2FYCr21MLm0Ju%2FvnvM56t7UVeE5AoeuPnV3ekNS9mbAX4aY9IMg1TJ3iAIuAAXnzLB0u8cT1fac5pLAEmNdOYg%2B5Q1XTo0btOTB93s4HMdG57A2kSLK7TmX4nw0xUOdA5EvzpYRzkWrzO0oCoJ440B%2F8GlSXzdbe8ne4k1xpVi3WNH4OD%2FIhzZSKTkbWrU6NxHr08e%2FW2ZrA0Yx6lSBqdqNNv0Ukmf6%2B%2BLtlyqv75luLFl6LPCLaHw8nciD1W38RVBA6ZmY9Zp8%2BOH8w6mcNKeoKhwv1MoXGFoHJ%2BTAyLXd8dPERQpc1ChtsxOSRd2RyzZ4cMphQXXlDFE5jlhLDpTmp3mqRZuFnj8X19Ob8gtdnDKu6Dt%2FXLYR%2FQEkoCa3x7Re67iv6Gvo%2FhqVXBSpxHJYgy%2FwHMDe7IIMNR%2BI6ajkBcfVkT2sgqcS55IguqPZKLZttlopFIZeylhKf21oM5CQlGXyErxgsgpzpWsppYmKuDCi9BVXetIBwwOVuZmY1iprnVFP8Dt9mCS6%2Bnb9p2NgcrJv3Ovw9vfQPFYSbMGoeUQy55GmwY3C8LR7VdIuLtqtcBU1gYNk%2FvBD4G7nu6G9hdTKH4wyZmZvQY6pgH3IkpKTDuicys%2FOREBBL7lS0eOXF0lfqIqW5OglDsv8Rc4y2eSANDoZiQzWdZ3B%2F9UiGldKqDzFxzV7xTErAuetwlxUurC7ygdmU2OKsztYvIyY%2FPW3PZ2lFPmTjNJw3%2FGObj5EiyfeINDb6x9y%2BPBSSVEmnCGvvIvhXYtjIA88ydW7kmhDxNwffRuYS%2FahZwvbhVf9PI4mOJ6fyJHKalEA2wEumlw&X-Amz-Signature=0e353d60b8cd2588ad1116006971ddd1071c244c74d5de9c064524a9261cd0e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PAOVNEF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIHa%2FzqwN4iTwxMA%2FBbEUTk8jQN1ViSAaigl5tHNcIfNrAiBE%2BxYH072QJ%2FB2XjbHwuGzZ4K3D11SGub7wK7p671doyr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM3GKyXuzzJA7rARshKtwDX6mPZjVtKZLlOlo2v5sbSXRRDISqY3k%2FYCr21MLm0Ju%2FvnvM56t7UVeE5AoeuPnV3ekNS9mbAX4aY9IMg1TJ3iAIuAAXnzLB0u8cT1fac5pLAEmNdOYg%2B5Q1XTo0btOTB93s4HMdG57A2kSLK7TmX4nw0xUOdA5EvzpYRzkWrzO0oCoJ440B%2F8GlSXzdbe8ne4k1xpVi3WNH4OD%2FIhzZSKTkbWrU6NxHr08e%2FW2ZrA0Yx6lSBqdqNNv0Ukmf6%2B%2BLtlyqv75luLFl6LPCLaHw8nciD1W38RVBA6ZmY9Zp8%2BOH8w6mcNKeoKhwv1MoXGFoHJ%2BTAyLXd8dPERQpc1ChtsxOSRd2RyzZ4cMphQXXlDFE5jlhLDpTmp3mqRZuFnj8X19Ob8gtdnDKu6Dt%2FXLYR%2FQEkoCa3x7Re67iv6Gvo%2FhqVXBSpxHJYgy%2FwHMDe7IIMNR%2BI6ajkBcfVkT2sgqcS55IguqPZKLZttlopFIZeylhKf21oM5CQlGXyErxgsgpzpWsppYmKuDCi9BVXetIBwwOVuZmY1iprnVFP8Dt9mCS6%2Bnb9p2NgcrJv3Ovw9vfQPFYSbMGoeUQy55GmwY3C8LR7VdIuLtqtcBU1gYNk%2FvBD4G7nu6G9hdTKH4wyZmZvQY6pgH3IkpKTDuicys%2FOREBBL7lS0eOXF0lfqIqW5OglDsv8Rc4y2eSANDoZiQzWdZ3B%2F9UiGldKqDzFxzV7xTErAuetwlxUurC7ygdmU2OKsztYvIyY%2FPW3PZ2lFPmTjNJw3%2FGObj5EiyfeINDb6x9y%2BPBSSVEmnCGvvIvhXYtjIA88ydW7kmhDxNwffRuYS%2FahZwvbhVf9PI4mOJ6fyJHKalEA2wEumlw&X-Amz-Signature=4b539fc38191305e9c04d29593f502394a017866be06e477bbfc595a99c1c24b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PAOVNEF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIHa%2FzqwN4iTwxMA%2FBbEUTk8jQN1ViSAaigl5tHNcIfNrAiBE%2BxYH072QJ%2FB2XjbHwuGzZ4K3D11SGub7wK7p671doyr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM3GKyXuzzJA7rARshKtwDX6mPZjVtKZLlOlo2v5sbSXRRDISqY3k%2FYCr21MLm0Ju%2FvnvM56t7UVeE5AoeuPnV3ekNS9mbAX4aY9IMg1TJ3iAIuAAXnzLB0u8cT1fac5pLAEmNdOYg%2B5Q1XTo0btOTB93s4HMdG57A2kSLK7TmX4nw0xUOdA5EvzpYRzkWrzO0oCoJ440B%2F8GlSXzdbe8ne4k1xpVi3WNH4OD%2FIhzZSKTkbWrU6NxHr08e%2FW2ZrA0Yx6lSBqdqNNv0Ukmf6%2B%2BLtlyqv75luLFl6LPCLaHw8nciD1W38RVBA6ZmY9Zp8%2BOH8w6mcNKeoKhwv1MoXGFoHJ%2BTAyLXd8dPERQpc1ChtsxOSRd2RyzZ4cMphQXXlDFE5jlhLDpTmp3mqRZuFnj8X19Ob8gtdnDKu6Dt%2FXLYR%2FQEkoCa3x7Re67iv6Gvo%2FhqVXBSpxHJYgy%2FwHMDe7IIMNR%2BI6ajkBcfVkT2sgqcS55IguqPZKLZttlopFIZeylhKf21oM5CQlGXyErxgsgpzpWsppYmKuDCi9BVXetIBwwOVuZmY1iprnVFP8Dt9mCS6%2Bnb9p2NgcrJv3Ovw9vfQPFYSbMGoeUQy55GmwY3C8LR7VdIuLtqtcBU1gYNk%2FvBD4G7nu6G9hdTKH4wyZmZvQY6pgH3IkpKTDuicys%2FOREBBL7lS0eOXF0lfqIqW5OglDsv8Rc4y2eSANDoZiQzWdZ3B%2F9UiGldKqDzFxzV7xTErAuetwlxUurC7ygdmU2OKsztYvIyY%2FPW3PZ2lFPmTjNJw3%2FGObj5EiyfeINDb6x9y%2BPBSSVEmnCGvvIvhXYtjIA88ydW7kmhDxNwffRuYS%2FahZwvbhVf9PI4mOJ6fyJHKalEA2wEumlw&X-Amz-Signature=b224b941a6d560213a5b0d78b176ac2a29963d09fe3f922860e7f5212f9b9a6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NBVXTSR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDFxAnXL3eAEtlYP5eVI17tPxG%2FL0d%2FE%2FY38IJzVL1NdwIgZ4U3%2BCb4D4K5asaddYLnEIk40LwyD5sCBb9JrD%2BmxDsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKGNwmhQV31I0HFocSrcAyvVVN3I%2BV33NYrLubk48YllbCNudPLhd1Yam2AAktIC7AEGUaqRs8XeT9iK6JtJTxecfjkkE1V8bBRkoS0jY34Y8zRQAiJ2VbcJYgV71vp%2Bs7om0rf7jekWkKF%2FUDAY0jiMyWc7fDPMg9PmWuohEoPmasTGTWazhGunUfJQxtN3cdswVRmatcodKx6K0xdPq9RpApinOvscjzvOXx%2B%2BkDj%2FihyRLvAa84zF9PistCOVsfV%2BKBDLO2JNA3EAG%2B%2BPajfcDKzRrbmHGcE8IOazdB9PuucbpY4HS9OjLxjcuDPqS%2Fw6KbBPiXlbtmdmD9GYBZM5lDgzbC2eFeQfKnwI4p9m376ehcEVq4WOQBSAZT3OvLADPLcow%2FxYFVo20yNSPSsu3DVZxhStUnWwHGhPM8RnfL2FEfICf%2FmUO1WUBtaaSbGUcH%2Bax%2BaHqY93qAa7XT5hOtNh%2BVH8pH6v6turx8tKD1rEugRAIzHKdzH%2BbKMdm1nJHyHhFvzsINPiC1fJwQQtkC3vTT7gqba28w7ZifPU7eC1zL6MWunkwgSjG4C38%2F2u8r6HjE3e4l9Vhm0upQHRG66N%2BTiY5I49AwJi5H7Gu8zSgWBP6Gvaf7Mu%2FBCQYp7BfkwBNWX2P9aaMJiZmb0GOqUBErHnlDhjrLIxWJsxlRyyxbL%2BcVHzqZbV3X5acHbo8Nb54rg5GfhT04KyctTWADHjBugyUkuT0SdyPFBi42ysbM7X6jWL93qELdrkQsXMPsPM70z8nvdg9oz4L91KuUMGMc3KLmaxABxAzdMBo7EGLL%2FJCtHQnqm8ZlkHSfb44VDiiVXmTOFhjcyKmOixqonEpv50TakbyfirVxZ8MUonj34r6C89&X-Amz-Signature=34db178b1f245f92887c37a53e408a0196f465cc642f8519d7e69dbf12b5ee05&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NBVXTSR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDFxAnXL3eAEtlYP5eVI17tPxG%2FL0d%2FE%2FY38IJzVL1NdwIgZ4U3%2BCb4D4K5asaddYLnEIk40LwyD5sCBb9JrD%2BmxDsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKGNwmhQV31I0HFocSrcAyvVVN3I%2BV33NYrLubk48YllbCNudPLhd1Yam2AAktIC7AEGUaqRs8XeT9iK6JtJTxecfjkkE1V8bBRkoS0jY34Y8zRQAiJ2VbcJYgV71vp%2Bs7om0rf7jekWkKF%2FUDAY0jiMyWc7fDPMg9PmWuohEoPmasTGTWazhGunUfJQxtN3cdswVRmatcodKx6K0xdPq9RpApinOvscjzvOXx%2B%2BkDj%2FihyRLvAa84zF9PistCOVsfV%2BKBDLO2JNA3EAG%2B%2BPajfcDKzRrbmHGcE8IOazdB9PuucbpY4HS9OjLxjcuDPqS%2Fw6KbBPiXlbtmdmD9GYBZM5lDgzbC2eFeQfKnwI4p9m376ehcEVq4WOQBSAZT3OvLADPLcow%2FxYFVo20yNSPSsu3DVZxhStUnWwHGhPM8RnfL2FEfICf%2FmUO1WUBtaaSbGUcH%2Bax%2BaHqY93qAa7XT5hOtNh%2BVH8pH6v6turx8tKD1rEugRAIzHKdzH%2BbKMdm1nJHyHhFvzsINPiC1fJwQQtkC3vTT7gqba28w7ZifPU7eC1zL6MWunkwgSjG4C38%2F2u8r6HjE3e4l9Vhm0upQHRG66N%2BTiY5I49AwJi5H7Gu8zSgWBP6Gvaf7Mu%2FBCQYp7BfkwBNWX2P9aaMJiZmb0GOqUBErHnlDhjrLIxWJsxlRyyxbL%2BcVHzqZbV3X5acHbo8Nb54rg5GfhT04KyctTWADHjBugyUkuT0SdyPFBi42ysbM7X6jWL93qELdrkQsXMPsPM70z8nvdg9oz4L91KuUMGMc3KLmaxABxAzdMBo7EGLL%2FJCtHQnqm8ZlkHSfb44VDiiVXmTOFhjcyKmOixqonEpv50TakbyfirVxZ8MUonj34r6C89&X-Amz-Signature=5cbbe5462f803418faf0cf1828c81c15a1e9b9490fe708d7377f308c3d9074ca&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NBVXTSR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDFxAnXL3eAEtlYP5eVI17tPxG%2FL0d%2FE%2FY38IJzVL1NdwIgZ4U3%2BCb4D4K5asaddYLnEIk40LwyD5sCBb9JrD%2BmxDsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKGNwmhQV31I0HFocSrcAyvVVN3I%2BV33NYrLubk48YllbCNudPLhd1Yam2AAktIC7AEGUaqRs8XeT9iK6JtJTxecfjkkE1V8bBRkoS0jY34Y8zRQAiJ2VbcJYgV71vp%2Bs7om0rf7jekWkKF%2FUDAY0jiMyWc7fDPMg9PmWuohEoPmasTGTWazhGunUfJQxtN3cdswVRmatcodKx6K0xdPq9RpApinOvscjzvOXx%2B%2BkDj%2FihyRLvAa84zF9PistCOVsfV%2BKBDLO2JNA3EAG%2B%2BPajfcDKzRrbmHGcE8IOazdB9PuucbpY4HS9OjLxjcuDPqS%2Fw6KbBPiXlbtmdmD9GYBZM5lDgzbC2eFeQfKnwI4p9m376ehcEVq4WOQBSAZT3OvLADPLcow%2FxYFVo20yNSPSsu3DVZxhStUnWwHGhPM8RnfL2FEfICf%2FmUO1WUBtaaSbGUcH%2Bax%2BaHqY93qAa7XT5hOtNh%2BVH8pH6v6turx8tKD1rEugRAIzHKdzH%2BbKMdm1nJHyHhFvzsINPiC1fJwQQtkC3vTT7gqba28w7ZifPU7eC1zL6MWunkwgSjG4C38%2F2u8r6HjE3e4l9Vhm0upQHRG66N%2BTiY5I49AwJi5H7Gu8zSgWBP6Gvaf7Mu%2FBCQYp7BfkwBNWX2P9aaMJiZmb0GOqUBErHnlDhjrLIxWJsxlRyyxbL%2BcVHzqZbV3X5acHbo8Nb54rg5GfhT04KyctTWADHjBugyUkuT0SdyPFBi42ysbM7X6jWL93qELdrkQsXMPsPM70z8nvdg9oz4L91KuUMGMc3KLmaxABxAzdMBo7EGLL%2FJCtHQnqm8ZlkHSfb44VDiiVXmTOFhjcyKmOixqonEpv50TakbyfirVxZ8MUonj34r6C89&X-Amz-Signature=785578e0d11dd2f02c623564f2bf4d457e211952be631e69a34e699ebd74401a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NBVXTSR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDFxAnXL3eAEtlYP5eVI17tPxG%2FL0d%2FE%2FY38IJzVL1NdwIgZ4U3%2BCb4D4K5asaddYLnEIk40LwyD5sCBb9JrD%2BmxDsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKGNwmhQV31I0HFocSrcAyvVVN3I%2BV33NYrLubk48YllbCNudPLhd1Yam2AAktIC7AEGUaqRs8XeT9iK6JtJTxecfjkkE1V8bBRkoS0jY34Y8zRQAiJ2VbcJYgV71vp%2Bs7om0rf7jekWkKF%2FUDAY0jiMyWc7fDPMg9PmWuohEoPmasTGTWazhGunUfJQxtN3cdswVRmatcodKx6K0xdPq9RpApinOvscjzvOXx%2B%2BkDj%2FihyRLvAa84zF9PistCOVsfV%2BKBDLO2JNA3EAG%2B%2BPajfcDKzRrbmHGcE8IOazdB9PuucbpY4HS9OjLxjcuDPqS%2Fw6KbBPiXlbtmdmD9GYBZM5lDgzbC2eFeQfKnwI4p9m376ehcEVq4WOQBSAZT3OvLADPLcow%2FxYFVo20yNSPSsu3DVZxhStUnWwHGhPM8RnfL2FEfICf%2FmUO1WUBtaaSbGUcH%2Bax%2BaHqY93qAa7XT5hOtNh%2BVH8pH6v6turx8tKD1rEugRAIzHKdzH%2BbKMdm1nJHyHhFvzsINPiC1fJwQQtkC3vTT7gqba28w7ZifPU7eC1zL6MWunkwgSjG4C38%2F2u8r6HjE3e4l9Vhm0upQHRG66N%2BTiY5I49AwJi5H7Gu8zSgWBP6Gvaf7Mu%2FBCQYp7BfkwBNWX2P9aaMJiZmb0GOqUBErHnlDhjrLIxWJsxlRyyxbL%2BcVHzqZbV3X5acHbo8Nb54rg5GfhT04KyctTWADHjBugyUkuT0SdyPFBi42ysbM7X6jWL93qELdrkQsXMPsPM70z8nvdg9oz4L91KuUMGMc3KLmaxABxAzdMBo7EGLL%2FJCtHQnqm8ZlkHSfb44VDiiVXmTOFhjcyKmOixqonEpv50TakbyfirVxZ8MUonj34r6C89&X-Amz-Signature=3af1e310f56199b09a81f0ae60a77908ce06c954832d658395dd21ffd7aa69da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NBVXTSR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDFxAnXL3eAEtlYP5eVI17tPxG%2FL0d%2FE%2FY38IJzVL1NdwIgZ4U3%2BCb4D4K5asaddYLnEIk40LwyD5sCBb9JrD%2BmxDsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKGNwmhQV31I0HFocSrcAyvVVN3I%2BV33NYrLubk48YllbCNudPLhd1Yam2AAktIC7AEGUaqRs8XeT9iK6JtJTxecfjkkE1V8bBRkoS0jY34Y8zRQAiJ2VbcJYgV71vp%2Bs7om0rf7jekWkKF%2FUDAY0jiMyWc7fDPMg9PmWuohEoPmasTGTWazhGunUfJQxtN3cdswVRmatcodKx6K0xdPq9RpApinOvscjzvOXx%2B%2BkDj%2FihyRLvAa84zF9PistCOVsfV%2BKBDLO2JNA3EAG%2B%2BPajfcDKzRrbmHGcE8IOazdB9PuucbpY4HS9OjLxjcuDPqS%2Fw6KbBPiXlbtmdmD9GYBZM5lDgzbC2eFeQfKnwI4p9m376ehcEVq4WOQBSAZT3OvLADPLcow%2FxYFVo20yNSPSsu3DVZxhStUnWwHGhPM8RnfL2FEfICf%2FmUO1WUBtaaSbGUcH%2Bax%2BaHqY93qAa7XT5hOtNh%2BVH8pH6v6turx8tKD1rEugRAIzHKdzH%2BbKMdm1nJHyHhFvzsINPiC1fJwQQtkC3vTT7gqba28w7ZifPU7eC1zL6MWunkwgSjG4C38%2F2u8r6HjE3e4l9Vhm0upQHRG66N%2BTiY5I49AwJi5H7Gu8zSgWBP6Gvaf7Mu%2FBCQYp7BfkwBNWX2P9aaMJiZmb0GOqUBErHnlDhjrLIxWJsxlRyyxbL%2BcVHzqZbV3X5acHbo8Nb54rg5GfhT04KyctTWADHjBugyUkuT0SdyPFBi42ysbM7X6jWL93qELdrkQsXMPsPM70z8nvdg9oz4L91KuUMGMc3KLmaxABxAzdMBo7EGLL%2FJCtHQnqm8ZlkHSfb44VDiiVXmTOFhjcyKmOixqonEpv50TakbyfirVxZ8MUonj34r6C89&X-Amz-Signature=67eb675cebdf5650bb1992e3a6bdca3c281a081909766f60e22ba26efe8bb7ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NBVXTSR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDFxAnXL3eAEtlYP5eVI17tPxG%2FL0d%2FE%2FY38IJzVL1NdwIgZ4U3%2BCb4D4K5asaddYLnEIk40LwyD5sCBb9JrD%2BmxDsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKGNwmhQV31I0HFocSrcAyvVVN3I%2BV33NYrLubk48YllbCNudPLhd1Yam2AAktIC7AEGUaqRs8XeT9iK6JtJTxecfjkkE1V8bBRkoS0jY34Y8zRQAiJ2VbcJYgV71vp%2Bs7om0rf7jekWkKF%2FUDAY0jiMyWc7fDPMg9PmWuohEoPmasTGTWazhGunUfJQxtN3cdswVRmatcodKx6K0xdPq9RpApinOvscjzvOXx%2B%2BkDj%2FihyRLvAa84zF9PistCOVsfV%2BKBDLO2JNA3EAG%2B%2BPajfcDKzRrbmHGcE8IOazdB9PuucbpY4HS9OjLxjcuDPqS%2Fw6KbBPiXlbtmdmD9GYBZM5lDgzbC2eFeQfKnwI4p9m376ehcEVq4WOQBSAZT3OvLADPLcow%2FxYFVo20yNSPSsu3DVZxhStUnWwHGhPM8RnfL2FEfICf%2FmUO1WUBtaaSbGUcH%2Bax%2BaHqY93qAa7XT5hOtNh%2BVH8pH6v6turx8tKD1rEugRAIzHKdzH%2BbKMdm1nJHyHhFvzsINPiC1fJwQQtkC3vTT7gqba28w7ZifPU7eC1zL6MWunkwgSjG4C38%2F2u8r6HjE3e4l9Vhm0upQHRG66N%2BTiY5I49AwJi5H7Gu8zSgWBP6Gvaf7Mu%2FBCQYp7BfkwBNWX2P9aaMJiZmb0GOqUBErHnlDhjrLIxWJsxlRyyxbL%2BcVHzqZbV3X5acHbo8Nb54rg5GfhT04KyctTWADHjBugyUkuT0SdyPFBi42ysbM7X6jWL93qELdrkQsXMPsPM70z8nvdg9oz4L91KuUMGMc3KLmaxABxAzdMBo7EGLL%2FJCtHQnqm8ZlkHSfb44VDiiVXmTOFhjcyKmOixqonEpv50TakbyfirVxZ8MUonj34r6C89&X-Amz-Signature=38d58660002e474e04dab543e6fbd6b86662b55366c958ad34d39d3d893edef0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGJIN5Y2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIGitRg41E2%2FCN3qOnkLNeGbvOk58HiImZ3O4A5AGXApxAiB5EOqCwPRZ9WKkc0dfvaz81DFA4l0nB5e3%2FFLpqjVkPCr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMAa%2Fls5NR2hCHHwB2KtwDG511cGXlEIMziomBEwX0zxs1JVtbZPdeZoEv%2B7y3sW8BR%2Fk0Wi2avFeO7%2ByM7IidpJk9zcgTgQOwRuiHt4pc2We6q4uAhcRdnwRFFUX68N8DAXeOZj%2FBZqu9O6KMaJ6fND%2Bv18oz1%2BjO2g6NL%2BxT98l5Obv1nBuGwcryfIvYd0rnBxznqvfOs6ucvMa27kQyp8s3nyAwZBKTo6Oloi7fwQR6zx%2F9X45tNZtaRPH%2F9MHtE%2BupTygQR1ZIl6aWBBZq3CY%2BbomGa%2FkB4%2FmxRdAfb%2BblncfA8uaQ4WcYARrFI8fxPlAbFUhIZVYiq5AEVqoSHV34dBLUsfCdAvoZt27CaUfgAOtlIarBvQp2gH6AV%2BOrhEStQe8%2FR8BRH0EeXHWdyV5p39UihsvKhbSlHwE9Bl4R%2BSenWcBJpl8C53ncby3Sx2EqoMU1V1zCGU2lW7q1WTHU%2B6efR%2BQTRgUE4PaypAyDbhdbS4CuZw8b1fgRULT6QIlkmhEK%2Bf68ZjqVS%2F6nERQo3fNS4qyAdPOOdTm9UGL4j8CP0n6bgHtWSZQBVOdrS4NcA1EmvAZHLPumFxsLqJS%2FOU54UTTXCwNaOS6k7nfZaHQGNJyAEjtApY67%2FwRHSJQTqjqwsi02s%2FQw0pmZvQY6pgG55yrAomfGAYjEQzOK8IK%2BeQK7imjwtvEGBlav76fZwxy1dhrA6JJIc6MWCOWtKtC9m3FRJsoHR%2FWrttVIKR6VQg1x9aQkQdrooKuwsn%2BwgE3u1o6By8Fnmk%2FIAV%2Fc0zggqxBjp2ATwDRPrzz1yvrFjf59SDGlwE6ppu222E2JD%2F34e8KvM7GXNiD53ABLfZfFwDjL61HPTL3G4P33fqV8r%2F5Rdaxh&X-Amz-Signature=23cea3529980ae91175e7d9bf08a1666091e50eb171dae9c153ad4be2d19aa5c&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQTZ2LA6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIAqNDBr7jHpz8e5DI%2B5aXqFTJ%2FAngMZFEp%2BCzPtmRF0pAiEAjEFNoGuzxAkMe5BRUEK6yt9xEO0Oh0I%2FDAIBtipKw3cq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDLF%2FYiI4K9RVGE1RGCrcAw3LwSPeWiDclmwXkPmmbj8GdJ5rdOc9A8tD9CqUx7%2BUcTnHCjjAbycrFP9%2B2xTZ%2FBQkr6GOu296cg5fwkGtonNPLJyNQ%2BpAc1QfcBND0eH8kbOYR%2BVVXWvd3NUnrZcyJ7DEbNlUh1yq43Ty2rFOWPuj0FqQ2HRY5r4IFduXSI2v%2BD5lraGMk6AbAEknRHBR3%2B6n6eU9Wyg4M8yBcMxhMtsr1qJ5xjoi2PU%2BTE9iJaYERAzWvisoX1t3wSDISwKmYfsZsmu%2BFb2oQqfhAYgA0dM%2Fw2bHK8xyE4mSiPn0Uu%2BXwcMkXTSWPoeBNLggMwwT8r98JPA7VYJCsB47Cb6czEYT3eEHRlPGXXCPx%2FKvH90sgSwo%2BAoMM7%2FF0JQzQF%2BQvmPmy1CWEAYET8L6%2F1%2FHQ%2B9mNuoPi8yi1VTfLWQ4%2ByFE0zbmu%2BwyE1%2FPCGRu8ra%2B%2FNKtQ6ZZ2vy24bp046s8A7Gds1YZROI4jbF52FwheIvO4gI7YuNcqCj3%2B4Av4sDvtlTATYnOhS0RQOhhHtIuFAlF27CEXBnPUB%2BhSKoWtkpWnThbNLKB%2For8eQJ%2BQJqMNx2lu4jvbKjIL7HqjP8LT75TZtKSAQxrdxikzY58u0sbnLKGXqhKil%2FEGH6pMK%2BZmb0GOqUBqs4KkeBlA3bkXw23VkBiTCRJv3GQM9hmpLkgttQrUiWUC4HV5VZXdwvc39944%2FYpyWb%2BKNViIRYUMaYC1m4tvS7AAHlgB%2Bm1UQUR9MeJCTXH%2BkMg6aRfRihBQWxQwW7HmeX%2BMs6QCUaKq9un%2FuX54LLbMuM%2BJDY8r%2Fb%2FV0JP8rO0qtGbE4C0tRd8ZhAYytV6XTpqpYM%2FXE3NzMUFWH0sosvoWsN5&X-Amz-Signature=ed0cefbacd88acb5b5005e1a71766d5e222fde8c887542a24f11d860edceaa13&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NBVXTSR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDFxAnXL3eAEtlYP5eVI17tPxG%2FL0d%2FE%2FY38IJzVL1NdwIgZ4U3%2BCb4D4K5asaddYLnEIk40LwyD5sCBb9JrD%2BmxDsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKGNwmhQV31I0HFocSrcAyvVVN3I%2BV33NYrLubk48YllbCNudPLhd1Yam2AAktIC7AEGUaqRs8XeT9iK6JtJTxecfjkkE1V8bBRkoS0jY34Y8zRQAiJ2VbcJYgV71vp%2Bs7om0rf7jekWkKF%2FUDAY0jiMyWc7fDPMg9PmWuohEoPmasTGTWazhGunUfJQxtN3cdswVRmatcodKx6K0xdPq9RpApinOvscjzvOXx%2B%2BkDj%2FihyRLvAa84zF9PistCOVsfV%2BKBDLO2JNA3EAG%2B%2BPajfcDKzRrbmHGcE8IOazdB9PuucbpY4HS9OjLxjcuDPqS%2Fw6KbBPiXlbtmdmD9GYBZM5lDgzbC2eFeQfKnwI4p9m376ehcEVq4WOQBSAZT3OvLADPLcow%2FxYFVo20yNSPSsu3DVZxhStUnWwHGhPM8RnfL2FEfICf%2FmUO1WUBtaaSbGUcH%2Bax%2BaHqY93qAa7XT5hOtNh%2BVH8pH6v6turx8tKD1rEugRAIzHKdzH%2BbKMdm1nJHyHhFvzsINPiC1fJwQQtkC3vTT7gqba28w7ZifPU7eC1zL6MWunkwgSjG4C38%2F2u8r6HjE3e4l9Vhm0upQHRG66N%2BTiY5I49AwJi5H7Gu8zSgWBP6Gvaf7Mu%2FBCQYp7BfkwBNWX2P9aaMJiZmb0GOqUBErHnlDhjrLIxWJsxlRyyxbL%2BcVHzqZbV3X5acHbo8Nb54rg5GfhT04KyctTWADHjBugyUkuT0SdyPFBi42ysbM7X6jWL93qELdrkQsXMPsPM70z8nvdg9oz4L91KuUMGMc3KLmaxABxAzdMBo7EGLL%2FJCtHQnqm8ZlkHSfb44VDiiVXmTOFhjcyKmOixqonEpv50TakbyfirVxZ8MUonj34r6C89&X-Amz-Signature=815499d62eb864ea4580ada758578b568966f034d7547fa25558fc98ddaba511&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NBVXTSR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDFxAnXL3eAEtlYP5eVI17tPxG%2FL0d%2FE%2FY38IJzVL1NdwIgZ4U3%2BCb4D4K5asaddYLnEIk40LwyD5sCBb9JrD%2BmxDsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKGNwmhQV31I0HFocSrcAyvVVN3I%2BV33NYrLubk48YllbCNudPLhd1Yam2AAktIC7AEGUaqRs8XeT9iK6JtJTxecfjkkE1V8bBRkoS0jY34Y8zRQAiJ2VbcJYgV71vp%2Bs7om0rf7jekWkKF%2FUDAY0jiMyWc7fDPMg9PmWuohEoPmasTGTWazhGunUfJQxtN3cdswVRmatcodKx6K0xdPq9RpApinOvscjzvOXx%2B%2BkDj%2FihyRLvAa84zF9PistCOVsfV%2BKBDLO2JNA3EAG%2B%2BPajfcDKzRrbmHGcE8IOazdB9PuucbpY4HS9OjLxjcuDPqS%2Fw6KbBPiXlbtmdmD9GYBZM5lDgzbC2eFeQfKnwI4p9m376ehcEVq4WOQBSAZT3OvLADPLcow%2FxYFVo20yNSPSsu3DVZxhStUnWwHGhPM8RnfL2FEfICf%2FmUO1WUBtaaSbGUcH%2Bax%2BaHqY93qAa7XT5hOtNh%2BVH8pH6v6turx8tKD1rEugRAIzHKdzH%2BbKMdm1nJHyHhFvzsINPiC1fJwQQtkC3vTT7gqba28w7ZifPU7eC1zL6MWunkwgSjG4C38%2F2u8r6HjE3e4l9Vhm0upQHRG66N%2BTiY5I49AwJi5H7Gu8zSgWBP6Gvaf7Mu%2FBCQYp7BfkwBNWX2P9aaMJiZmb0GOqUBErHnlDhjrLIxWJsxlRyyxbL%2BcVHzqZbV3X5acHbo8Nb54rg5GfhT04KyctTWADHjBugyUkuT0SdyPFBi42ysbM7X6jWL93qELdrkQsXMPsPM70z8nvdg9oz4L91KuUMGMc3KLmaxABxAzdMBo7EGLL%2FJCtHQnqm8ZlkHSfb44VDiiVXmTOFhjcyKmOixqonEpv50TakbyfirVxZ8MUonj34r6C89&X-Amz-Signature=3b44ce1cb18090cbb407d0b4aa7feb8b8b7eadd5237c8bae1c1c1858a3c65125&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NBVXTSR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDFxAnXL3eAEtlYP5eVI17tPxG%2FL0d%2FE%2FY38IJzVL1NdwIgZ4U3%2BCb4D4K5asaddYLnEIk40LwyD5sCBb9JrD%2BmxDsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKGNwmhQV31I0HFocSrcAyvVVN3I%2BV33NYrLubk48YllbCNudPLhd1Yam2AAktIC7AEGUaqRs8XeT9iK6JtJTxecfjkkE1V8bBRkoS0jY34Y8zRQAiJ2VbcJYgV71vp%2Bs7om0rf7jekWkKF%2FUDAY0jiMyWc7fDPMg9PmWuohEoPmasTGTWazhGunUfJQxtN3cdswVRmatcodKx6K0xdPq9RpApinOvscjzvOXx%2B%2BkDj%2FihyRLvAa84zF9PistCOVsfV%2BKBDLO2JNA3EAG%2B%2BPajfcDKzRrbmHGcE8IOazdB9PuucbpY4HS9OjLxjcuDPqS%2Fw6KbBPiXlbtmdmD9GYBZM5lDgzbC2eFeQfKnwI4p9m376ehcEVq4WOQBSAZT3OvLADPLcow%2FxYFVo20yNSPSsu3DVZxhStUnWwHGhPM8RnfL2FEfICf%2FmUO1WUBtaaSbGUcH%2Bax%2BaHqY93qAa7XT5hOtNh%2BVH8pH6v6turx8tKD1rEugRAIzHKdzH%2BbKMdm1nJHyHhFvzsINPiC1fJwQQtkC3vTT7gqba28w7ZifPU7eC1zL6MWunkwgSjG4C38%2F2u8r6HjE3e4l9Vhm0upQHRG66N%2BTiY5I49AwJi5H7Gu8zSgWBP6Gvaf7Mu%2FBCQYp7BfkwBNWX2P9aaMJiZmb0GOqUBErHnlDhjrLIxWJsxlRyyxbL%2BcVHzqZbV3X5acHbo8Nb54rg5GfhT04KyctTWADHjBugyUkuT0SdyPFBi42ysbM7X6jWL93qELdrkQsXMPsPM70z8nvdg9oz4L91KuUMGMc3KLmaxABxAzdMBo7EGLL%2FJCtHQnqm8ZlkHSfb44VDiiVXmTOFhjcyKmOixqonEpv50TakbyfirVxZ8MUonj34r6C89&X-Amz-Signature=1df41ae35673232b711fcb23f07008feabc7237eeed3219bac8df68ebe7ded93&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX2UXV55%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDCbEGYxnBhT7ugg5RSVxH1SHZzUn7uNO8WBWAs6%2B%2FFjAIgXTXyohYX7W0W808DHRQ6BfsNHCn7VNS1uuEUMv9a7mgq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDB0T%2FPVRG%2Bj2sGCGCyrcAx%2FEgwP3XWMz7HfREiNXEQ%2BYtt6vJ2u%2BmFigKv1F2cHvgcBq3ApswoRMcwn%2FRkNue4Q8mJi2ds7OIL2WPuDYtHHlMEDnHedD%2FQALoYs78GcEA9aum8YbabkCZ5Dcx2uO3dfVzM04duFmaaw5FToKIB2VU68HtLJpLevqWT0cj1XQ5hdvcLfq2XfzTUw4KUBTBt74P7fLGmRoVSoANPj7PP9rl4VJuBBjiv16LVX5SbgLq5pfH8YsT7I36Vdo5hiZTVxu6zTsmOSzbwcMNBaTViWzAr0cBbDaPVl7nIoARx%2FuljEp%2FWkZuNqO%2FtvxtqUdCFW6hSiU57m%2FsKf4WoboNDw0U9V59FI1hKKCKNVwcn3NJNBHj0TAmrR3fdKD4Z7UGZKv7gTQj9qMVG9pt1pzqPiHihlMS6FzG7LNhEjGx%2FsqH4mDzf8kyCob%2F3cLiNT0vng3JX5LYWF78t8y4n2JRtK8R3ux0dRXqxVpCCmJeujM7TvPahFlZgYoshnYZx%2BHz4%2FpqxKoEZPCiwupgjflX4BffS34T7qloM9%2FFV%2FCwQPyU5RgY0dPxdnoz01XIokVatEpnA7oKaDqlMqG4ouonQE7JOX4X5Z%2F7VgFgoRxoJX6zu6%2Fk34F6IWoM5w1MM2Zmb0GOqUBKUf9zgF7EaD%2Fkq7duyY4dhYcOt%2F4oKc%2BNSGPD7jbJyw%2FffvkL9bmDytRgeOBy73Q%2FPLLMej6MXv9URy24HjsKTgmmEW6b6zHMD0wyuTOjQAEuiLU7MPEnFCkjoDVgyhBBzTR7yglpwLjpinpfHSLqE874%2FJvOWespwOL22AacEqMU92rsKV0teJj2QphpC5Sq65dl8KdCwj8z%2B%2F5Zh00G%2F7QrkEm&X-Amz-Signature=7f5fe1a4638f29c1335fc92b9584286f3688f1fe8d473cf9261c65d702fd48d8&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GSI2MAW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCVyKRulOZrOcrmvfICK1frovEwXcFzx12%2Fld9%2BKNzJ4QIhAIbcFaMheEdoR8z0Oyzztqo8jd5jhdTyq878eEV0dNpsKv8DCHsQABoMNjM3NDIzMTgzODA1Igy8CKFNbKSbEsWdwlsq3APJQWbmuFXmCTtA7MXoUYjdclehXwcjd%2F4ECR1Ft%2B5bYkNnARr4pUMCwUAafGBgAIFTxD6cJwaFXRjKd2lmtk5RpbCgMD%2B%2FkBTTYVP4laAHfvi9L%2BTzwKkGNAFL6BfBBm1eR8ZVc9NSPVZIxNokQOX4Y5sDkRxpNFJ9oAARgJwBKFEOerb1gf3yjNJwfZ%2BZJAvE9BmbzB98Ojq53q7m%2FMcN6%2Be3aJjBclkfQ%2F95CKm%2BK54KGxTqycTCeE18l7eg3pXaIH96OI1oG%2FpxMo1J2LDIOqTsSBfG0opS3NN%2BlAOMiJG1Vc%2Fi%2B0LzMxWmJrhljN4BFjS3V4pMc%2Ft92DmiNWmcU%2FfI3MbyKmmNR%2FU9tm%2BdnFsNAUi0bE8lTcK7R3Z7ml%2B2vPEp9i%2FArEojzkAb7Wpn3aQMqQIqvU%2BnmH5AerzbYAMASKJ8kur5mxlgm8L8amaGOp2RG8DEejUlB6TIcgGs%2BoXUNxUSl%2B%2FGh%2BEo25EKZr3AJmDsrlpUowOU5kCW6Va3jWvR3TvqfKdazx7fSO%2F0wk%2FHSE2hZCZHFaVU5Lp68F3YRaZDRoPBJbmtyresZroPfwWKXFVfNt0FP38czKjKCrOPRRu%2BHT4zdRs1lqx5fWM9PsP3c9I8KrrhADDlmZm9BjqkAR%2FYeXI%2Fz1YA9DNPQAZoxh5k0WMALD%2BusM3Olt%2BpAsudOwtLF5DtJIvFRwaC80mqpzLo0EKdGBP%2FslEVcwzDG%2FcsPIfZxgn9lKXkj0YQUeU1zfQqhxJkuTo%2FFtvgJaqZ%2B%2FlNXpI2PKDJG6LK5vw5Dd8vMxfszCYRBiQEFyVH3g4GrRcDT8GZouvL%2FefoPP7wjgkIhX2Xpx1%2BHSNopFlG3vm2OtZd&X-Amz-Signature=2ec7dbe92e63e87393492fb6066ab32a96d3edc989de4334f5bbe422132927c2&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPSBH3RW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDqL4yGdisIqC9K%2BFnxXPskxBcVB%2BzChFTMLmOFd5rT6AIgRBHY1fje9RK1wJUPAIKHW3%2BZI1TzaRst8ReyfRD1mwsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDMdCWgoH8crlbF%2BmsCrcA%2BZ338upkatMwQKbAsoT3uQO4tW4M%2FJzPhCLotw3sFk86BViMO5Skjs4f%2BeClXaR6EXHyzYJU4v7hEaO0qKXQ7pRyEiaSdbT3H%2Flf0r84PTSuVMvz1AswtpPOAv1K7yiPSdq1YxSRmtM68aOIXMSGaLL3NvLRlViwmRCP8iP28Xql8LoXw%2By9ju7VWMScSESRhamnDtmJEzr0d6PNaOXLM2o3eRYh%2F6T1Jddq4OWvZ2ccdzP4hRqTBeDapA3FOzDi6OSgqz4gY9kcLU6hduF4PzPUMwUdYpEZSC3JJ3NhPcnAPSw11jzxf2rCMC6pKVR%2Bs5AhQucbEgEEXp9KOs9cea0Qnd%2F3%2BNvjZoR9HmQjn9uBS%2F1lGnn%2FYLYo%2BMwFUFFhdFyyugZcH%2BXsIlhIY0vFTLTeCEoAmWFQpO3mmttZSPxhTAMVfdBgCuX46OPmrvS6b8dipqro7OOe2%2FFKxXjIJj99yCU2mJm127%2BZ8jDBLEHYeZrLW1jP%2FkW0lebf8O3QD6ggNsarJzbP0rOK0ki5pIaNe%2BlgyBCEGXbNzYu2BdicpyW0C8hCvyTzOLxDBqfpbQ7Ix%2BYoAMbbBhFnkyTkmQaV9WEKhG9qJkJvJWxH2EZxOT%2FFXBljZB49N1WMMyZmb0GOqUBDRKFvPNu2zCRWIo3jODkbckGGmKn3w9fn2fQlO2mUe%2B49FmA7lmWM%2Bwgr%2FcsMxLJdBCJLKIsrwSU06byyV7VaLz4RosZ2booElKoVKIGsjuokRnNVGjoe0BZGiX8Zj5iNL13brJiSrdezJr58tnMmcU8PcNbO9ZZXf6%2B5MQY74CXs%2FhGZSI%2BzsIJwBUcGyxQB9TbYMaj%2BSGpzRspmhLmqWmCde6I&X-Amz-Signature=b60ae3a120f7f306b0674ae0792fb79c214e3466fb23ecca07b360a5d27f94c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSA6MPAX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCID%2BhqHoIchSy9hrkR9diElSyC4fdWQ146W5DRyUZvueTAiEAjWJ4Z392eK7ndlJ0MjkfKcfNZLoso5em9oEH%2FzQfMLoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNvqBr%2FCQj7FJ9CI6SrcA4S2ODCp4fpOQyrI7F6Q4LpMhA4hg7rK3hQdZdPaO7HzIptdqTokwQavruu8yaYknpU09l5nF48GuCacLZiMbeFXf0OU%2Bb0vWfV3rsf4sR8KmDAY1%2FOESOrlHy5xWCw55HMBtIQjUgks3D8jj%2FclAhm%2FpkkaTr56DyDFFNxJWg4tIXK5ge0fbaDaPT73Y9htRjczdqsgWT%2FO22S%2FUzXB1oB34x5pgh18NyFozoCJB0R5uzCKvQHJx4jQvkF08V1U9ZO%2BdDjhU8wg2%2BXD%2BrNHDwTUuFZ0yhi%2FZMyZRyt2cjxCxDl%2BLKenBOTPhujVJ6SJk91lwit6QlDyoqkM6ef8l%2FdKkyQBHKMscX4Pv1%2FHEZChD1hAJNhkZKTHMUiTTZLCgALCmgsnEFvn6ueqAU7y0SmmmaFQEnSXejIrh94fFa%2BGBXncrVhW%2Bx6q0zErRu9cIRg9cHCX%2Fh8K1q%2BLTKRpNLa15OjzEjppPeO02dJV832x3Jbk5cVB4BT1NVTGabuf86Fw84NQqAI1%2FDJnkGnDyL7DmU7Zx43aVDJeUC6OVZRyPxH%2Bko5dQC030NDlEXU%2FrIXSJsB3byElphpxTDyq%2Folsa9HahsWAfFg5%2FMnt2iW6ghFyNdDAR4HGeFFMMJuZmb0GOqUBGMjzBtFT58pbi6RUt9TJ3OUgRkRpaaV%2FolkNq4S4iYjQ8Qr%2BO0sUADzRemHDem%2BSC5Vf6zABzTI2G6C5d4MVnAuUheLI1ZjnMlKP6Mdh9Yusz448I5p%2FLGVhlRQD0jbF6zs7brl%2FtVomWn5VuC1dgjF%2BbonP0%2FvKAfks6%2B9MZZvt9oN8X9IbppMRWFIGk%2BFN7Y%2Bqq9OKVZPuW1RwGM9WHg%2FvFnPW&X-Amz-Signature=75ce81d5eda4a42e73f527eff0e96cf164dcf6b6b3fa9a3369680e7f56ab6ea1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSA6MPAX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCID%2BhqHoIchSy9hrkR9diElSyC4fdWQ146W5DRyUZvueTAiEAjWJ4Z392eK7ndlJ0MjkfKcfNZLoso5em9oEH%2FzQfMLoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDNvqBr%2FCQj7FJ9CI6SrcA4S2ODCp4fpOQyrI7F6Q4LpMhA4hg7rK3hQdZdPaO7HzIptdqTokwQavruu8yaYknpU09l5nF48GuCacLZiMbeFXf0OU%2Bb0vWfV3rsf4sR8KmDAY1%2FOESOrlHy5xWCw55HMBtIQjUgks3D8jj%2FclAhm%2FpkkaTr56DyDFFNxJWg4tIXK5ge0fbaDaPT73Y9htRjczdqsgWT%2FO22S%2FUzXB1oB34x5pgh18NyFozoCJB0R5uzCKvQHJx4jQvkF08V1U9ZO%2BdDjhU8wg2%2BXD%2BrNHDwTUuFZ0yhi%2FZMyZRyt2cjxCxDl%2BLKenBOTPhujVJ6SJk91lwit6QlDyoqkM6ef8l%2FdKkyQBHKMscX4Pv1%2FHEZChD1hAJNhkZKTHMUiTTZLCgALCmgsnEFvn6ueqAU7y0SmmmaFQEnSXejIrh94fFa%2BGBXncrVhW%2Bx6q0zErRu9cIRg9cHCX%2Fh8K1q%2BLTKRpNLa15OjzEjppPeO02dJV832x3Jbk5cVB4BT1NVTGabuf86Fw84NQqAI1%2FDJnkGnDyL7DmU7Zx43aVDJeUC6OVZRyPxH%2Bko5dQC030NDlEXU%2FrIXSJsB3byElphpxTDyq%2Folsa9HahsWAfFg5%2FMnt2iW6ghFyNdDAR4HGeFFMMJuZmb0GOqUBGMjzBtFT58pbi6RUt9TJ3OUgRkRpaaV%2FolkNq4S4iYjQ8Qr%2BO0sUADzRemHDem%2BSC5Vf6zABzTI2G6C5d4MVnAuUheLI1ZjnMlKP6Mdh9Yusz448I5p%2FLGVhlRQD0jbF6zs7brl%2FtVomWn5VuC1dgjF%2BbonP0%2FvKAfks6%2B9MZZvt9oN8X9IbppMRWFIGk%2BFN7Y%2Bqq9OKVZPuW1RwGM9WHg%2FvFnPW&X-Amz-Signature=0d439235fd1e40b0666d6fbb7a3bc14ad48fe14011c38f5b24dfabc968855f3a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
