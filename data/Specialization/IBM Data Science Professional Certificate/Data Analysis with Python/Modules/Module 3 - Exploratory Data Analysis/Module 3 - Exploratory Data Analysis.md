

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKJST4S6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0st0gSH%2FnHPwt20YTuAYvIs67eGCDp%2Fvh5vA80ObtIQIgcZa%2BIc1hAkXNXa6HL2A7arX1BVNAKj9p%2BTQ3%2ByTpeoUqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLnSG52jjjam5s9dJyrcA%2FjOBHJBm8VKBdsU2EjmHt5L%2F2BeocCJq8rPPohdZq7a1AHxsHoimsl5niisjoAWZ86gErdZqI40jJCGrcNFi2wa6XaXTJ4ZrAyedjVl985eEGYjEbxgGOFN5xw0CdRCgc4MDT2fWAyApvNVICPE1FxSBE8hT7dioqudMgs%2Fi1TcgHH7y8rmo5eHUK9OBLqVig2ILey9UIxvNQ%2FXVjFxxAr1er5QwD5VjhPn2vHVQrkznv%2BgOgcV%2Fps%2Bx7fHGlAKRMgRKC1kyMYTc08vHPhojOqn%2Bomvq8631RHGxX2Q912J4Q3vTDmp1i7nZGw9BItqd5iR6Xq8uhR1X8ovCsK8BCQJoyHlOFFnA6PjhFf%2FEJ7TWYnpiwxnHuRyY%2B93GCWtdKW83iKcBY1IDdinnm6NNkCVClVqeRAZN3QHhlzgwHBWwcgEAwt%2FIThCoayRGLa85Ij4N0Y6Sl4EX9hCeTYqKYM2Hdtq%2FGRUrBBAl81a9KHDyCBV2nD348T1TEGrr2aed80zz6FcSaE4vGYeF9MlbNBwZdgAhor24ZMlGLAFQYj%2BzF1H3y41km0YnSI0q915asB4CHjB3eoLQa9mIL1%2BQSrnPb%2BdPTgYGomZ317Xcfyj%2BpkgLvaVsvv%2Bqof6MNqK7bwGOqUBX3xigXCE5cGj41A2TJsbVAS6zdS%2BGJtiqAj4TLudrk2rtkI2FHoWD8xFgCruqoj1BaSAod17Op%2B1BhytD3sv9nKCkkXmqCybYq7YEF8c7IsmmdcEFiiJ4ejqFUL2t6RhRYwMhMTN4h0uQWdAWS8SkKUdY93Z7%2F%2BYWJria%2BOT5RFcjrupqGss11q9Z6Wn077enQEodlvlpeBHcf3h%2B0UoAVdGfO25&X-Amz-Signature=30e4ca74625f736cb6d3c081801bf5c21ec7fb4709e707ae07ceb1aee34e49e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKJST4S6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0st0gSH%2FnHPwt20YTuAYvIs67eGCDp%2Fvh5vA80ObtIQIgcZa%2BIc1hAkXNXa6HL2A7arX1BVNAKj9p%2BTQ3%2ByTpeoUqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLnSG52jjjam5s9dJyrcA%2FjOBHJBm8VKBdsU2EjmHt5L%2F2BeocCJq8rPPohdZq7a1AHxsHoimsl5niisjoAWZ86gErdZqI40jJCGrcNFi2wa6XaXTJ4ZrAyedjVl985eEGYjEbxgGOFN5xw0CdRCgc4MDT2fWAyApvNVICPE1FxSBE8hT7dioqudMgs%2Fi1TcgHH7y8rmo5eHUK9OBLqVig2ILey9UIxvNQ%2FXVjFxxAr1er5QwD5VjhPn2vHVQrkznv%2BgOgcV%2Fps%2Bx7fHGlAKRMgRKC1kyMYTc08vHPhojOqn%2Bomvq8631RHGxX2Q912J4Q3vTDmp1i7nZGw9BItqd5iR6Xq8uhR1X8ovCsK8BCQJoyHlOFFnA6PjhFf%2FEJ7TWYnpiwxnHuRyY%2B93GCWtdKW83iKcBY1IDdinnm6NNkCVClVqeRAZN3QHhlzgwHBWwcgEAwt%2FIThCoayRGLa85Ij4N0Y6Sl4EX9hCeTYqKYM2Hdtq%2FGRUrBBAl81a9KHDyCBV2nD348T1TEGrr2aed80zz6FcSaE4vGYeF9MlbNBwZdgAhor24ZMlGLAFQYj%2BzF1H3y41km0YnSI0q915asB4CHjB3eoLQa9mIL1%2BQSrnPb%2BdPTgYGomZ317Xcfyj%2BpkgLvaVsvv%2Bqof6MNqK7bwGOqUBX3xigXCE5cGj41A2TJsbVAS6zdS%2BGJtiqAj4TLudrk2rtkI2FHoWD8xFgCruqoj1BaSAod17Op%2B1BhytD3sv9nKCkkXmqCybYq7YEF8c7IsmmdcEFiiJ4ejqFUL2t6RhRYwMhMTN4h0uQWdAWS8SkKUdY93Z7%2F%2BYWJria%2BOT5RFcjrupqGss11q9Z6Wn077enQEodlvlpeBHcf3h%2B0UoAVdGfO25&X-Amz-Signature=93a7f8eeb6ce33d29264defec907530b7182199514898c34a0e6936c80d22db5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKJST4S6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0st0gSH%2FnHPwt20YTuAYvIs67eGCDp%2Fvh5vA80ObtIQIgcZa%2BIc1hAkXNXa6HL2A7arX1BVNAKj9p%2BTQ3%2ByTpeoUqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLnSG52jjjam5s9dJyrcA%2FjOBHJBm8VKBdsU2EjmHt5L%2F2BeocCJq8rPPohdZq7a1AHxsHoimsl5niisjoAWZ86gErdZqI40jJCGrcNFi2wa6XaXTJ4ZrAyedjVl985eEGYjEbxgGOFN5xw0CdRCgc4MDT2fWAyApvNVICPE1FxSBE8hT7dioqudMgs%2Fi1TcgHH7y8rmo5eHUK9OBLqVig2ILey9UIxvNQ%2FXVjFxxAr1er5QwD5VjhPn2vHVQrkznv%2BgOgcV%2Fps%2Bx7fHGlAKRMgRKC1kyMYTc08vHPhojOqn%2Bomvq8631RHGxX2Q912J4Q3vTDmp1i7nZGw9BItqd5iR6Xq8uhR1X8ovCsK8BCQJoyHlOFFnA6PjhFf%2FEJ7TWYnpiwxnHuRyY%2B93GCWtdKW83iKcBY1IDdinnm6NNkCVClVqeRAZN3QHhlzgwHBWwcgEAwt%2FIThCoayRGLa85Ij4N0Y6Sl4EX9hCeTYqKYM2Hdtq%2FGRUrBBAl81a9KHDyCBV2nD348T1TEGrr2aed80zz6FcSaE4vGYeF9MlbNBwZdgAhor24ZMlGLAFQYj%2BzF1H3y41km0YnSI0q915asB4CHjB3eoLQa9mIL1%2BQSrnPb%2BdPTgYGomZ317Xcfyj%2BpkgLvaVsvv%2Bqof6MNqK7bwGOqUBX3xigXCE5cGj41A2TJsbVAS6zdS%2BGJtiqAj4TLudrk2rtkI2FHoWD8xFgCruqoj1BaSAod17Op%2B1BhytD3sv9nKCkkXmqCybYq7YEF8c7IsmmdcEFiiJ4ejqFUL2t6RhRYwMhMTN4h0uQWdAWS8SkKUdY93Z7%2F%2BYWJria%2BOT5RFcjrupqGss11q9Z6Wn077enQEodlvlpeBHcf3h%2B0UoAVdGfO25&X-Amz-Signature=7df729a696366505bbac4460dcfdf78d720d60c6271b29790536f5abc5b71953&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTGBGTSL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHgxYUIQZMpFxngkBpyq7CHypYD7EYTNgnZ5CZ%2BERFgpAiAnJORF5iKLxgG1CTyOW6WSsqfHk5o4lD34zM5WPtxbFCqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRQAycHUWijCjL%2BrVKtwD1g1fs4Cm22%2B%2BhbNbkaMPhAzB3XMPlx%2BpS3K5GZjyyISvwz%2BM8bS3X3vk9DyZLI6xiJTeg%2F6DCW7xxir5uFrfQZ%2FQGb4VjQ3v%2B05t3yoNi7Pzv17PSA77OPuFv9ll%2BYmemN5ODO6l12s14kWg0R3rhGmXul8DexOIa%2FHkXVG2fPnkkrQfJaVMW7cAc6rIp6qLwkQsRp22vdE2dvStb%2Fl4VV2ls6hcWf%2FmS2NtEpyQ8m96ah0WLe26BoBZAhBGvYw5UoTUzdMTMRUL%2BkVXTNGzkoPDz9Pfqf0RHbGHduBGq8ICXKacq7nKzM80WUrBrAonboJjiyZhlmn9kMCebjvqoKdplicHDNJdFqJMPVOgZr7GpQecQixB4uoHUwpZd3vQ0nwseT9nsVVP44cXajCw0Kfpr%2F93YDduORRm1d9Ntp2T7JT7tJf%2FxUYASHnKNAlVp%2BzJTKkePBkKvW1ckD74LdLTRqQPbHxewkECr9NX4opMOHzWF7B8HY2hbvqfhy8b1b7ROkblWrUpzxV%2Fhy49tNtV8CbGHx1FlMJhWon3D2ixKnzjigq2MIxMrE6krDDlpcDBBL0fLAr2E5WsGVsvDpSvLKAPImdJgYqDdw9x307WwuDMy8qRdqsUIfww8ortvAY6pgEX98aGtdiJRGu8nsefJyXSRlM6hHOHpfJ2Gsi4osplnGSDjswXN893cePX6phiCRV06XWA7MOfGD0MbR%2Bo6A%2Bhds%2FG0CBFi1Rfe3gNAGrkHrLOnk3PsYRncw72TGqLL03lSi5zvd0Zn6q8h3p8SVch0o8erSV6EaMJ0w0WUjaOKc%2Fjxzkly8NeHkOIy%2BzF50UYSfmpvdnP6Jmv%2BtAXCCsl%2FrG7%2B%2BcB&X-Amz-Signature=99a23a6e7108dd3af36f64fec9fa4df646462092dc87b22a5a8b44d27d5a12e3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTGBGTSL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHgxYUIQZMpFxngkBpyq7CHypYD7EYTNgnZ5CZ%2BERFgpAiAnJORF5iKLxgG1CTyOW6WSsqfHk5o4lD34zM5WPtxbFCqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRQAycHUWijCjL%2BrVKtwD1g1fs4Cm22%2B%2BhbNbkaMPhAzB3XMPlx%2BpS3K5GZjyyISvwz%2BM8bS3X3vk9DyZLI6xiJTeg%2F6DCW7xxir5uFrfQZ%2FQGb4VjQ3v%2B05t3yoNi7Pzv17PSA77OPuFv9ll%2BYmemN5ODO6l12s14kWg0R3rhGmXul8DexOIa%2FHkXVG2fPnkkrQfJaVMW7cAc6rIp6qLwkQsRp22vdE2dvStb%2Fl4VV2ls6hcWf%2FmS2NtEpyQ8m96ah0WLe26BoBZAhBGvYw5UoTUzdMTMRUL%2BkVXTNGzkoPDz9Pfqf0RHbGHduBGq8ICXKacq7nKzM80WUrBrAonboJjiyZhlmn9kMCebjvqoKdplicHDNJdFqJMPVOgZr7GpQecQixB4uoHUwpZd3vQ0nwseT9nsVVP44cXajCw0Kfpr%2F93YDduORRm1d9Ntp2T7JT7tJf%2FxUYASHnKNAlVp%2BzJTKkePBkKvW1ckD74LdLTRqQPbHxewkECr9NX4opMOHzWF7B8HY2hbvqfhy8b1b7ROkblWrUpzxV%2Fhy49tNtV8CbGHx1FlMJhWon3D2ixKnzjigq2MIxMrE6krDDlpcDBBL0fLAr2E5WsGVsvDpSvLKAPImdJgYqDdw9x307WwuDMy8qRdqsUIfww8ortvAY6pgEX98aGtdiJRGu8nsefJyXSRlM6hHOHpfJ2Gsi4osplnGSDjswXN893cePX6phiCRV06XWA7MOfGD0MbR%2Bo6A%2Bhds%2FG0CBFi1Rfe3gNAGrkHrLOnk3PsYRncw72TGqLL03lSi5zvd0Zn6q8h3p8SVch0o8erSV6EaMJ0w0WUjaOKc%2Fjxzkly8NeHkOIy%2BzF50UYSfmpvdnP6Jmv%2BtAXCCsl%2FrG7%2B%2BcB&X-Amz-Signature=1f12244a770f393501d11d7b015a007104139d5594600b53a62854121ab35a2a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTGBGTSL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHgxYUIQZMpFxngkBpyq7CHypYD7EYTNgnZ5CZ%2BERFgpAiAnJORF5iKLxgG1CTyOW6WSsqfHk5o4lD34zM5WPtxbFCqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRQAycHUWijCjL%2BrVKtwD1g1fs4Cm22%2B%2BhbNbkaMPhAzB3XMPlx%2BpS3K5GZjyyISvwz%2BM8bS3X3vk9DyZLI6xiJTeg%2F6DCW7xxir5uFrfQZ%2FQGb4VjQ3v%2B05t3yoNi7Pzv17PSA77OPuFv9ll%2BYmemN5ODO6l12s14kWg0R3rhGmXul8DexOIa%2FHkXVG2fPnkkrQfJaVMW7cAc6rIp6qLwkQsRp22vdE2dvStb%2Fl4VV2ls6hcWf%2FmS2NtEpyQ8m96ah0WLe26BoBZAhBGvYw5UoTUzdMTMRUL%2BkVXTNGzkoPDz9Pfqf0RHbGHduBGq8ICXKacq7nKzM80WUrBrAonboJjiyZhlmn9kMCebjvqoKdplicHDNJdFqJMPVOgZr7GpQecQixB4uoHUwpZd3vQ0nwseT9nsVVP44cXajCw0Kfpr%2F93YDduORRm1d9Ntp2T7JT7tJf%2FxUYASHnKNAlVp%2BzJTKkePBkKvW1ckD74LdLTRqQPbHxewkECr9NX4opMOHzWF7B8HY2hbvqfhy8b1b7ROkblWrUpzxV%2Fhy49tNtV8CbGHx1FlMJhWon3D2ixKnzjigq2MIxMrE6krDDlpcDBBL0fLAr2E5WsGVsvDpSvLKAPImdJgYqDdw9x307WwuDMy8qRdqsUIfww8ortvAY6pgEX98aGtdiJRGu8nsefJyXSRlM6hHOHpfJ2Gsi4osplnGSDjswXN893cePX6phiCRV06XWA7MOfGD0MbR%2Bo6A%2Bhds%2FG0CBFi1Rfe3gNAGrkHrLOnk3PsYRncw72TGqLL03lSi5zvd0Zn6q8h3p8SVch0o8erSV6EaMJ0w0WUjaOKc%2Fjxzkly8NeHkOIy%2BzF50UYSfmpvdnP6Jmv%2BtAXCCsl%2FrG7%2B%2BcB&X-Amz-Signature=5e6408debc29c5d9ac8875ece8ec20c70d8ee45cc07d170f855889d9b27101da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTGBGTSL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHgxYUIQZMpFxngkBpyq7CHypYD7EYTNgnZ5CZ%2BERFgpAiAnJORF5iKLxgG1CTyOW6WSsqfHk5o4lD34zM5WPtxbFCqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRQAycHUWijCjL%2BrVKtwD1g1fs4Cm22%2B%2BhbNbkaMPhAzB3XMPlx%2BpS3K5GZjyyISvwz%2BM8bS3X3vk9DyZLI6xiJTeg%2F6DCW7xxir5uFrfQZ%2FQGb4VjQ3v%2B05t3yoNi7Pzv17PSA77OPuFv9ll%2BYmemN5ODO6l12s14kWg0R3rhGmXul8DexOIa%2FHkXVG2fPnkkrQfJaVMW7cAc6rIp6qLwkQsRp22vdE2dvStb%2Fl4VV2ls6hcWf%2FmS2NtEpyQ8m96ah0WLe26BoBZAhBGvYw5UoTUzdMTMRUL%2BkVXTNGzkoPDz9Pfqf0RHbGHduBGq8ICXKacq7nKzM80WUrBrAonboJjiyZhlmn9kMCebjvqoKdplicHDNJdFqJMPVOgZr7GpQecQixB4uoHUwpZd3vQ0nwseT9nsVVP44cXajCw0Kfpr%2F93YDduORRm1d9Ntp2T7JT7tJf%2FxUYASHnKNAlVp%2BzJTKkePBkKvW1ckD74LdLTRqQPbHxewkECr9NX4opMOHzWF7B8HY2hbvqfhy8b1b7ROkblWrUpzxV%2Fhy49tNtV8CbGHx1FlMJhWon3D2ixKnzjigq2MIxMrE6krDDlpcDBBL0fLAr2E5WsGVsvDpSvLKAPImdJgYqDdw9x307WwuDMy8qRdqsUIfww8ortvAY6pgEX98aGtdiJRGu8nsefJyXSRlM6hHOHpfJ2Gsi4osplnGSDjswXN893cePX6phiCRV06XWA7MOfGD0MbR%2Bo6A%2Bhds%2FG0CBFi1Rfe3gNAGrkHrLOnk3PsYRncw72TGqLL03lSi5zvd0Zn6q8h3p8SVch0o8erSV6EaMJ0w0WUjaOKc%2Fjxzkly8NeHkOIy%2BzF50UYSfmpvdnP6Jmv%2BtAXCCsl%2FrG7%2B%2BcB&X-Amz-Signature=4307141d2d66991c088278e6fc719f2508e2e80937e6edf642f2d555a3442d07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTGBGTSL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHgxYUIQZMpFxngkBpyq7CHypYD7EYTNgnZ5CZ%2BERFgpAiAnJORF5iKLxgG1CTyOW6WSsqfHk5o4lD34zM5WPtxbFCqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRQAycHUWijCjL%2BrVKtwD1g1fs4Cm22%2B%2BhbNbkaMPhAzB3XMPlx%2BpS3K5GZjyyISvwz%2BM8bS3X3vk9DyZLI6xiJTeg%2F6DCW7xxir5uFrfQZ%2FQGb4VjQ3v%2B05t3yoNi7Pzv17PSA77OPuFv9ll%2BYmemN5ODO6l12s14kWg0R3rhGmXul8DexOIa%2FHkXVG2fPnkkrQfJaVMW7cAc6rIp6qLwkQsRp22vdE2dvStb%2Fl4VV2ls6hcWf%2FmS2NtEpyQ8m96ah0WLe26BoBZAhBGvYw5UoTUzdMTMRUL%2BkVXTNGzkoPDz9Pfqf0RHbGHduBGq8ICXKacq7nKzM80WUrBrAonboJjiyZhlmn9kMCebjvqoKdplicHDNJdFqJMPVOgZr7GpQecQixB4uoHUwpZd3vQ0nwseT9nsVVP44cXajCw0Kfpr%2F93YDduORRm1d9Ntp2T7JT7tJf%2FxUYASHnKNAlVp%2BzJTKkePBkKvW1ckD74LdLTRqQPbHxewkECr9NX4opMOHzWF7B8HY2hbvqfhy8b1b7ROkblWrUpzxV%2Fhy49tNtV8CbGHx1FlMJhWon3D2ixKnzjigq2MIxMrE6krDDlpcDBBL0fLAr2E5WsGVsvDpSvLKAPImdJgYqDdw9x307WwuDMy8qRdqsUIfww8ortvAY6pgEX98aGtdiJRGu8nsefJyXSRlM6hHOHpfJ2Gsi4osplnGSDjswXN893cePX6phiCRV06XWA7MOfGD0MbR%2Bo6A%2Bhds%2FG0CBFi1Rfe3gNAGrkHrLOnk3PsYRncw72TGqLL03lSi5zvd0Zn6q8h3p8SVch0o8erSV6EaMJ0w0WUjaOKc%2Fjxzkly8NeHkOIy%2BzF50UYSfmpvdnP6Jmv%2BtAXCCsl%2FrG7%2B%2BcB&X-Amz-Signature=9caeb8fda8ac2723d468069b213138253ad061fa606dd64a37d9c9179c5d5119&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTGBGTSL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHgxYUIQZMpFxngkBpyq7CHypYD7EYTNgnZ5CZ%2BERFgpAiAnJORF5iKLxgG1CTyOW6WSsqfHk5o4lD34zM5WPtxbFCqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRQAycHUWijCjL%2BrVKtwD1g1fs4Cm22%2B%2BhbNbkaMPhAzB3XMPlx%2BpS3K5GZjyyISvwz%2BM8bS3X3vk9DyZLI6xiJTeg%2F6DCW7xxir5uFrfQZ%2FQGb4VjQ3v%2B05t3yoNi7Pzv17PSA77OPuFv9ll%2BYmemN5ODO6l12s14kWg0R3rhGmXul8DexOIa%2FHkXVG2fPnkkrQfJaVMW7cAc6rIp6qLwkQsRp22vdE2dvStb%2Fl4VV2ls6hcWf%2FmS2NtEpyQ8m96ah0WLe26BoBZAhBGvYw5UoTUzdMTMRUL%2BkVXTNGzkoPDz9Pfqf0RHbGHduBGq8ICXKacq7nKzM80WUrBrAonboJjiyZhlmn9kMCebjvqoKdplicHDNJdFqJMPVOgZr7GpQecQixB4uoHUwpZd3vQ0nwseT9nsVVP44cXajCw0Kfpr%2F93YDduORRm1d9Ntp2T7JT7tJf%2FxUYASHnKNAlVp%2BzJTKkePBkKvW1ckD74LdLTRqQPbHxewkECr9NX4opMOHzWF7B8HY2hbvqfhy8b1b7ROkblWrUpzxV%2Fhy49tNtV8CbGHx1FlMJhWon3D2ixKnzjigq2MIxMrE6krDDlpcDBBL0fLAr2E5WsGVsvDpSvLKAPImdJgYqDdw9x307WwuDMy8qRdqsUIfww8ortvAY6pgEX98aGtdiJRGu8nsefJyXSRlM6hHOHpfJ2Gsi4osplnGSDjswXN893cePX6phiCRV06XWA7MOfGD0MbR%2Bo6A%2Bhds%2FG0CBFi1Rfe3gNAGrkHrLOnk3PsYRncw72TGqLL03lSi5zvd0Zn6q8h3p8SVch0o8erSV6EaMJ0w0WUjaOKc%2Fjxzkly8NeHkOIy%2BzF50UYSfmpvdnP6Jmv%2BtAXCCsl%2FrG7%2B%2BcB&X-Amz-Signature=85e8cf5c5766d3a99684d800d1720cccfab8d334159ed67406857b9fb2897e01&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ONANTPF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWPHep83VSnPvJwwlu9z1ROoFrcRphgjXKQTeO0NBBKwIhANFINA%2B8PlrMPaAM34wM%2B5Kj7mhsV%2BUhbQL47TWYjl6NKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzs6CuTSHgLQeTbmskq3AN9KccYCsMg7S%2B1ExkfYhaEJxeLSa2CKSxzw8KFsvp2u1w%2BpyqsdeRcTp7QgLU9UJO%2B9cY9Srsrdql9deTGWHNDEBaWnwz4HyGs9IWwQTy4PzDwD7M7lvwTkYHm52Jq%2Fe0vultdQn1kgRJwoEByV%2BC4Y%2BL1Y0n1Eq%2BO0Y5TKyUnkiPKUXHiCS6YgbO%2BKnFOrv5u6nsUlxnyiS09gdWbFY1X4xYTL7aDtO3RP3Syt%2FKxIfTIf6EXrJM7QEGoeG2slml%2FYOiUFCk46rO8S7%2FJ32uOWesLWjdZNuCvnNC1JsYyEIgwSSlAupIN0H8Hopc58dyvnviKCD5Jf3VGsCPZhYBFn5vIospmJIy5Sj4yfeIlQ7gJzbbXjQIMzayqAdLGiTMUH8qak1h%2FfzEzkphqS1xPEcoDYytqDcClw1llfi03MnVVjuViteX5bTrfTg8JScowzkBWWYEFPMOUI1c2o3nB%2FEj1C01YIO4QV7PXGS1VmYWRCyjgwuMSgFbkJuSdfTJVrranTllIsd53xLWDE8lujzyvdt41e6OSYmaCJ7UYZu5EB75epx5qBlTcWgaKYkXVDgAPn03CbcOUTnMhfnUSf%2BROnZpEFNUeMC322d8vGofBbqTpzNB%2BCEXXIzCpi%2B28BjqkAaFXFZgYJrxiYxuQX5M%2BS9U%2FnuqNgwjdSYhenOw%2Bj%2FN3Iw51%2FOtXajZ09IfSkFXWJACe87JM%2FPVm4Fu6Eg8qa8o3fTPq85Cg1Mw%2BVN9cCu6j6tHkzQriby2UPv7yqkXP6Vy8G695JavU6Rdgx00U4ZyeC6xX0k021fiqrjXNQNiIWLkSbhGdW%2FVWZdk%2F%2Bvx8q4SCvpYVqp1iJx1Oh5BcFb%2BpK%2FEo&X-Amz-Signature=177490c92ea355730fc3c6bec57961376eebd471d8cd13e49baf24dc2a92c841&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJXDLUK2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK6079KhIRtUdazEh6q9jBFKYNnoEVjj8ohfK9U497WAIgXM41I3V3OAwHOlC9DDnEFNjSJhW3Ji%2Ffp3JKwxIFeMkqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMv%2FaGaGJMoDBTa9byrcAy6%2Fit7WJ44mO6fHqgNacgGnBnfXjuHsOUSezTnxfbYQ%2B6iLw46s00OD%2BNrbkp3nD0z%2B1TWoRj1%2Frpq3R9DQJDXTDCf57DkoG%2Fd0YSEh94PZEuqA4v3j%2FP1%2BndWP2pLLl%2FftzzBwlIIniCr6Cy1WUeSpk6%2FQldYPpGm0MQDCykACwOCR6tGKBWbClrb2%2Fcc%2F6lG26lyJf0OOXd4KZvz75k9EwbRGt%2BFdN0uXE9iN%2FEnCNrpDk3h0E80H7zZTxVDONMd%2B71J9ibml8M96TuxD844GozsFbjFROdjaQMveYu6jt9XANtkOTWUJp3S%2FF89GYQkbdxn91snRVCDaDvdp5t0kXaiR%2Bh%2BbTIpU0Ei1N9AbBXn1LjE47U%2Fl5aHNDGDXrJnJjZUXAMWj0mYm6z1UxcQWp2tVTqju9%2Bb5qxG%2B%2BeCFQBai3LOSpIAokZArIBV44Bub2pmn7Cic3bOYzdAOad0CykacDFFPONweJJ0i6O4cwCAtZwMoCvSV8pzIucCLPSIoIlH1b46NCoM%2BArAtD9ZX7BaFJRoFWlh8zrWuuhLt40LmFu0UkMjtMy9WGrKWAu%2BlndZhXo92%2BKlFvQFYFbXdjmo41yH6Tw%2Fyka9rC0zDFVABxsHaWpgbKtcMMISL7bwGOqUBuxA2sCJLSLLTFghLEE1A2%2BlPfDd%2FnndbmW5rG1AESPdbD12yU9gSxmCpCXwfQ5ir9tPDmrbvQo0G8VRDjtfj1syDh9xAVka2adweWTrQZPKEC2WAVnQoXBmTY1BbVwlWhhKgkGs6wFCTE54M8TeFHx5yxdRudG4C0t%2Bqk%2BwvfiiPHyWKhHvIKoCXiP6eUP4%2FA9%2FMQlpHwPdVVyqAlWWFMJSkNva2&X-Amz-Signature=a9390277f8a4eb4a3ff314e7b12cce1520f2bcbfa76a81f66cd7eaba76974b40&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTGBGTSL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHgxYUIQZMpFxngkBpyq7CHypYD7EYTNgnZ5CZ%2BERFgpAiAnJORF5iKLxgG1CTyOW6WSsqfHk5o4lD34zM5WPtxbFCqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRQAycHUWijCjL%2BrVKtwD1g1fs4Cm22%2B%2BhbNbkaMPhAzB3XMPlx%2BpS3K5GZjyyISvwz%2BM8bS3X3vk9DyZLI6xiJTeg%2F6DCW7xxir5uFrfQZ%2FQGb4VjQ3v%2B05t3yoNi7Pzv17PSA77OPuFv9ll%2BYmemN5ODO6l12s14kWg0R3rhGmXul8DexOIa%2FHkXVG2fPnkkrQfJaVMW7cAc6rIp6qLwkQsRp22vdE2dvStb%2Fl4VV2ls6hcWf%2FmS2NtEpyQ8m96ah0WLe26BoBZAhBGvYw5UoTUzdMTMRUL%2BkVXTNGzkoPDz9Pfqf0RHbGHduBGq8ICXKacq7nKzM80WUrBrAonboJjiyZhlmn9kMCebjvqoKdplicHDNJdFqJMPVOgZr7GpQecQixB4uoHUwpZd3vQ0nwseT9nsVVP44cXajCw0Kfpr%2F93YDduORRm1d9Ntp2T7JT7tJf%2FxUYASHnKNAlVp%2BzJTKkePBkKvW1ckD74LdLTRqQPbHxewkECr9NX4opMOHzWF7B8HY2hbvqfhy8b1b7ROkblWrUpzxV%2Fhy49tNtV8CbGHx1FlMJhWon3D2ixKnzjigq2MIxMrE6krDDlpcDBBL0fLAr2E5WsGVsvDpSvLKAPImdJgYqDdw9x307WwuDMy8qRdqsUIfww8ortvAY6pgEX98aGtdiJRGu8nsefJyXSRlM6hHOHpfJ2Gsi4osplnGSDjswXN893cePX6phiCRV06XWA7MOfGD0MbR%2Bo6A%2Bhds%2FG0CBFi1Rfe3gNAGrkHrLOnk3PsYRncw72TGqLL03lSi5zvd0Zn6q8h3p8SVch0o8erSV6EaMJ0w0WUjaOKc%2Fjxzkly8NeHkOIy%2BzF50UYSfmpvdnP6Jmv%2BtAXCCsl%2FrG7%2B%2BcB&X-Amz-Signature=929ac348db8edab0ba01d21e8023d14da72c60869c0c37a222b86dbb074b71f6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTGBGTSL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHgxYUIQZMpFxngkBpyq7CHypYD7EYTNgnZ5CZ%2BERFgpAiAnJORF5iKLxgG1CTyOW6WSsqfHk5o4lD34zM5WPtxbFCqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRQAycHUWijCjL%2BrVKtwD1g1fs4Cm22%2B%2BhbNbkaMPhAzB3XMPlx%2BpS3K5GZjyyISvwz%2BM8bS3X3vk9DyZLI6xiJTeg%2F6DCW7xxir5uFrfQZ%2FQGb4VjQ3v%2B05t3yoNi7Pzv17PSA77OPuFv9ll%2BYmemN5ODO6l12s14kWg0R3rhGmXul8DexOIa%2FHkXVG2fPnkkrQfJaVMW7cAc6rIp6qLwkQsRp22vdE2dvStb%2Fl4VV2ls6hcWf%2FmS2NtEpyQ8m96ah0WLe26BoBZAhBGvYw5UoTUzdMTMRUL%2BkVXTNGzkoPDz9Pfqf0RHbGHduBGq8ICXKacq7nKzM80WUrBrAonboJjiyZhlmn9kMCebjvqoKdplicHDNJdFqJMPVOgZr7GpQecQixB4uoHUwpZd3vQ0nwseT9nsVVP44cXajCw0Kfpr%2F93YDduORRm1d9Ntp2T7JT7tJf%2FxUYASHnKNAlVp%2BzJTKkePBkKvW1ckD74LdLTRqQPbHxewkECr9NX4opMOHzWF7B8HY2hbvqfhy8b1b7ROkblWrUpzxV%2Fhy49tNtV8CbGHx1FlMJhWon3D2ixKnzjigq2MIxMrE6krDDlpcDBBL0fLAr2E5WsGVsvDpSvLKAPImdJgYqDdw9x307WwuDMy8qRdqsUIfww8ortvAY6pgEX98aGtdiJRGu8nsefJyXSRlM6hHOHpfJ2Gsi4osplnGSDjswXN893cePX6phiCRV06XWA7MOfGD0MbR%2Bo6A%2Bhds%2FG0CBFi1Rfe3gNAGrkHrLOnk3PsYRncw72TGqLL03lSi5zvd0Zn6q8h3p8SVch0o8erSV6EaMJ0w0WUjaOKc%2Fjxzkly8NeHkOIy%2BzF50UYSfmpvdnP6Jmv%2BtAXCCsl%2FrG7%2B%2BcB&X-Amz-Signature=7189b7ab5d0292945a76807854e1881295fa4472440648772d77c2d1ed41d0eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTGBGTSL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHgxYUIQZMpFxngkBpyq7CHypYD7EYTNgnZ5CZ%2BERFgpAiAnJORF5iKLxgG1CTyOW6WSsqfHk5o4lD34zM5WPtxbFCqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRQAycHUWijCjL%2BrVKtwD1g1fs4Cm22%2B%2BhbNbkaMPhAzB3XMPlx%2BpS3K5GZjyyISvwz%2BM8bS3X3vk9DyZLI6xiJTeg%2F6DCW7xxir5uFrfQZ%2FQGb4VjQ3v%2B05t3yoNi7Pzv17PSA77OPuFv9ll%2BYmemN5ODO6l12s14kWg0R3rhGmXul8DexOIa%2FHkXVG2fPnkkrQfJaVMW7cAc6rIp6qLwkQsRp22vdE2dvStb%2Fl4VV2ls6hcWf%2FmS2NtEpyQ8m96ah0WLe26BoBZAhBGvYw5UoTUzdMTMRUL%2BkVXTNGzkoPDz9Pfqf0RHbGHduBGq8ICXKacq7nKzM80WUrBrAonboJjiyZhlmn9kMCebjvqoKdplicHDNJdFqJMPVOgZr7GpQecQixB4uoHUwpZd3vQ0nwseT9nsVVP44cXajCw0Kfpr%2F93YDduORRm1d9Ntp2T7JT7tJf%2FxUYASHnKNAlVp%2BzJTKkePBkKvW1ckD74LdLTRqQPbHxewkECr9NX4opMOHzWF7B8HY2hbvqfhy8b1b7ROkblWrUpzxV%2Fhy49tNtV8CbGHx1FlMJhWon3D2ixKnzjigq2MIxMrE6krDDlpcDBBL0fLAr2E5WsGVsvDpSvLKAPImdJgYqDdw9x307WwuDMy8qRdqsUIfww8ortvAY6pgEX98aGtdiJRGu8nsefJyXSRlM6hHOHpfJ2Gsi4osplnGSDjswXN893cePX6phiCRV06XWA7MOfGD0MbR%2Bo6A%2Bhds%2FG0CBFi1Rfe3gNAGrkHrLOnk3PsYRncw72TGqLL03lSi5zvd0Zn6q8h3p8SVch0o8erSV6EaMJ0w0WUjaOKc%2Fjxzkly8NeHkOIy%2BzF50UYSfmpvdnP6Jmv%2BtAXCCsl%2FrG7%2B%2BcB&X-Amz-Signature=283cbfbe25579202ccf49eaddaacab23d8334553976c998dcb4d3313b7b21fb0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L3TRX6M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmOPPNdttj%2F8yEfuvBWWyGR6WrDz5MBvX5jN1mWFW9BgIgHMxV%2FkDpgIxgxWLw5uGJf%2BnDS7OKE3rfyIGLrDQKY%2BcqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDODWm1PqIf%2FiafOBECrcA%2F8tnSOnPoD1shUjMRcbVi9GUbuNPJQfBj9fuPIt04F%2BE%2FtgV9%2FSyUPZE3S%2FhFHMenEVX1rqpeehnmxYBbKvDj2C%2Fk9GYnjHIbI7zlyxB%2Bpf%2B03mEKtmUoFsh1z8d49OZu32vLFE6mnk1ZN663xbFUdBNk9jOq04ZASZO5KT1li5vmBjvoE5bAdi69OB7e%2Br0ouuWEycqaVZPbidrBFxF6K6MSg7dMydXxGUSkiR69%2FytcArkcLcKEXlTO0EcY6aHvl0jVqUX27xM1MkGd6oh0JGFLcmxe213GXZTJOCrYQF39kaozYTVqM8iPXrtX6f4%2FUzlChrrXHzFkTpw3SValq8a5G57E1VDCxQoBfuUXVu6BWxAiDSVIUqKHe1SQi7KuWuc6Ens0OLh5uzRmoTV7Ep0Q6xtBbaoXv9GZ37IOYj8Izv86o5DzEebxgqHaeVUY%2B63NwjctgwvPgKd4Qs67u86bA%2F2RG%2BaOTmd%2FgkCBKsaP0rHPeo68wJKvejNYcJudG%2BWTn%2FSUXlpl6a2YdQke%2Bl14x1p0WJn14TrNu8m9fGzWXRSDLi5Kftbop7t7YfLluh9b4FXPQzAXw09vEyvnpAambR0b%2BWWqkM%2Bho9h9yNh6Y3mVEPkbyspj45MIiL7bwGOqUB87p6bUJ7k9PtSoWmE%2Bw%2BZThHppT1fdXgC6enoEBipcjqnd59PN7kC37tTa5AdY36FlIS0r%2F5sdWUVzbEKzR0LL%2BBIlRKaiirE0B8clhqeZUKaFbsL%2FACmsnQNULWY1oknzRa%2Fj8OpMJcW672a%2Ba3epxNXhUAkT78tlsXWpLQAz2h7YyqGXSvdHdyztTpUyNOSYIcRgnWdl38MMw6ywEEDlWkxTgw&X-Amz-Signature=cf0914e10a856bc60da359ce1b9bb8e19d0401fb26ade826314b672d956a028c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7IIZHWY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmmEih3GwTRp%2FVEO8Ie8EYqOP0viGBPXEqs5CInt5M9AiEAg%2FFYf6VpS8ksp62bQAy0x47ts0brxOGo6vouvFHLTzUqiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMaRpJ60sHAnNQXzFSrcAzsFZthkmpDu5312iHnxY1GgyZ16SndFpo6SlkorlTux1WA558WCo7gJa4Jr0zFEG0sBB4LtWsBu9DGstATnXjTtK1WAL15h7nIYwfy1F%2FX%2BDgZaD2yo5ATBmlhtYOXuHPLzF5PKU9uFQhvSSaFkcPRaJs3VQjBkMZxxZLaLdXMyNZX6hyvuBXFYc5YbShvqRpZiqX9OyGrrgjSkV6D947ZTACiLX9co9rxCno1c5PoWFg8tZ1RwUm5D8sDdO3YsY91GUp%2Fpap1GsH3TZT9ERz1RZe1iuWQEXwjBatdDq2JWqIraIoyKI%2BlM4Voj8qb0cwALs6%2FTioqJqtogzdA9lPdSQIn8uz3mx6p31rKA1%2Fdvd0GchH5djQModZT4TzQ78o7MFklrwDvR4%2BXiD4O%2F3f84zsCEeuDo5Yv%2BmaiNE4Tody22Vi9DD6eBpjFQ0VpR9RDtajdrfrWk%2Bp8I%2FgytZEDciPgEe0S2N54A2Ri%2F30CMZgwEM3WtVynKAmhiMkdCzZOKNyZWAYnLIsVvzt1TefC8%2B424uZGydQEIZ2mn2sQ1%2B7P9m5FRF3XWq3PabOqZGzC6aoBBgQpe2VuMJZ0tPIWMAT%2BJMni5BEXTGWFfabwnH%2FV193rl3jv%2BEJXFMPKK7bwGOqUBlEEF%2FJxuzEjy6anmTY4ZZMVOB7MUuyWT%2FukRLbcLWPjWAuX6FHGcrxONRgLGCMFF8lM43cX1h5US1ONUF3INYCyBBedXwsRnW%2FkRnKaxvSQ7d48tNPyPAGqUJJx5C5K0tv1no8N3IPVkjyNPWx%2BH1N6ESKwXjOsgGXl6DTAPJLSDXfBRM9KYr78TM3SyHdawrSuq0K1ngaUG7P7FSDy0WCbVvdVy&X-Amz-Signature=18033ef324b38168798696f8c42ad973026e50250b01818258f0e0db3c0c9588&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3QN42YW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1pI155h6oQ8nHuUUz0d3KOxPQnLg4qj2hpVvrMwg2UQIgW0W5A6OiH3BgYj2A%2Fh5tshxfMZ1bp1fCZfeHwR5xu6QqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPPBX6G%2FXQ8HNQVdZSrcA8sLFcdJzGkX8SD1hqqJwgnNtUYOiLnbHro%2Bf%2F9UZeCoS4CQcQWs9HVzugUcrrZqDp3XUqxGeSiljwyvCuBIJwE0w3fJKvayfQK%2BpSn53aCCtJCjE50WTwrNBVpzdf4dEvgbFnJqoHBJSpxWIunF13Kw5VK5DNwQRcDyZdC560%2FIN5fxCfZhTb0StC9EVbKTFI62T9ecdJyxlc%2BGotK6BzPvuS8521mEdN2%2FXZoLreIGlWgclLWRu7C%2BwscadyM80rvD3YAp1f1WW4zoYvvmtSbgeX2gryU2lDBfEmXv0vrvao%2F%2BA3n6v%2BrRCqQHXtWNJZ0jb56uoJ9dwJloJ2h2hdjmgO6l0bBqtJcPi76l%2FV64weLdgkuRTpk44nN3ksWnIuEj0C2ooIIDcK3aZu4nA5wDqjG7%2F%2BmHKrMUHSooLWy5lm7EwnKVkEsSEq65Uq1%2FJUKyynfoUfYieM3vqUR5V4OnVOoy6Rlh59yepwcbtG16qv%2BJKVeUzJGKoRxrcF0ABIUV6gNzc82ykksqFFNVkYFjYsNilbgMi75NFuxfKdUMGH%2FJPMhOx1RE7GGn68YJhxcTHzrhpIF%2Fi1CaYEihMrLU7j1pa0HVquwK6tsMRRot6B6rQRHzyqODwXqFMJ2M7bwGOqUBkUw9Ta9OE%2FmOXPRrGMscj%2BDA5VW%2F04psz3oiN2DXALOpwFdi1plI7EmqT%2BvbeVFWWpgneI%2FOgUUQhezob3m40i2nkZf7ljPG%2BSub1X67S7A6J%2FGWvKRMdLxPjBnbybOdKKvnOTJvOZp7WORRIFBUfro08dzq9D2j7g3o%2FN%2FkxQhPTZp7F352YWzVzObY7ZwWnJkFSI2fhbq%2FsGvIP578vrlBRgJk&X-Amz-Signature=2546741a075d233fd40ea97cbff938e250756cbaab8be08e576f0c72cb199539&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UV3YM3WN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID0BkC67%2FIU%2B%2F9YQCGxIaTxsWc6QdRiF3510HdSfVsHhAiBzrCtqtsSf3YYBt2YVHSBd%2B575YHqSp5B8SgRk8aa%2FhCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgsQkLMO80LXVuI6JKtwDiLimqWuerdsAUIiXIZTntwMUsbBhoebx7W7o7AsNEiyMjnYyXD2z5GtOAqCIxderUlRqo9fNxJIwhOat8r2rFDDNvACYqIM2PyNNDUID02j%2BfG9a3VVy%2BbtsugE1zZf0Lg1TNzLbXjT3J1QsaOktPfMP0JIvNt0MaVbVtB2Y59VNAgy%2BCSlICbNNwMitCFlA%2FWeUPuwrgx0wG4ROdwPVzyauCmf%2B7WQtAvdqWRvN2juaPwMijBTolg3HSrLRkoLVRDvKG3ZD2GlNL2oZVVqLT4KtWjlunsyucZFvnVd7p4SAvT0b%2Bn4z6rt1D0FHiTTA64sp4e9Dp4ao3FdzAa4lnoMTTxsgBwerpwHFiaU2RdDYyct8zO3fMUirwEeggVavx7U%2FlX6TszSRn1YKA1nB3fZhGNfZ4ijrLwobKjI8kXB2fUnVQZ%2FQUXVJ%2Bg9nE0tvN2cA4Yk0%2BzrgFvOev3N6pM1imeHIchB2jQCx%2B4hs7fgC%2B51lw2w0%2FBS8DY1jPQElwd9n7wR2UJyeSrAVVFXXTZ1gSQWzBqwPn4BgJbAzi12wxcRL2i%2BMWelXDVU00FYUpILGVnYCP5NawRbBo8HINhZKP1t4%2B0W1gpzDqRUcdtys9%2FtswHMGGUUZC%2BMwx4vtvAY6pgGRnxHZNub3MqTQR%2BbXGtjEO83yJpm%2BmFw7o5jp8Q0ySENZ7%2B0Y8qyZmsItWVf9bsNyC7R8I2OeN0Asw476E0mej6NQIdCg3za2RGPIk5XjW8DWal9Rli3NEc8hlf2Cfw76W7vSYn5c9ditvYyeG2VuA8mCIqjNnlnsdYTQQqXGWY3N%2F2WPSnEY%2FZ%2BU87Cpa8%2FC7oB2GiqX3e3QYkKJevqBxSQXNJ4H&X-Amz-Signature=ec5183b728ae35c141261d5542c5cfbaaf811cf13fd0fe76b233d7f1a9f301ba&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UV3YM3WN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID0BkC67%2FIU%2B%2F9YQCGxIaTxsWc6QdRiF3510HdSfVsHhAiBzrCtqtsSf3YYBt2YVHSBd%2B575YHqSp5B8SgRk8aa%2FhCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgsQkLMO80LXVuI6JKtwDiLimqWuerdsAUIiXIZTntwMUsbBhoebx7W7o7AsNEiyMjnYyXD2z5GtOAqCIxderUlRqo9fNxJIwhOat8r2rFDDNvACYqIM2PyNNDUID02j%2BfG9a3VVy%2BbtsugE1zZf0Lg1TNzLbXjT3J1QsaOktPfMP0JIvNt0MaVbVtB2Y59VNAgy%2BCSlICbNNwMitCFlA%2FWeUPuwrgx0wG4ROdwPVzyauCmf%2B7WQtAvdqWRvN2juaPwMijBTolg3HSrLRkoLVRDvKG3ZD2GlNL2oZVVqLT4KtWjlunsyucZFvnVd7p4SAvT0b%2Bn4z6rt1D0FHiTTA64sp4e9Dp4ao3FdzAa4lnoMTTxsgBwerpwHFiaU2RdDYyct8zO3fMUirwEeggVavx7U%2FlX6TszSRn1YKA1nB3fZhGNfZ4ijrLwobKjI8kXB2fUnVQZ%2FQUXVJ%2Bg9nE0tvN2cA4Yk0%2BzrgFvOev3N6pM1imeHIchB2jQCx%2B4hs7fgC%2B51lw2w0%2FBS8DY1jPQElwd9n7wR2UJyeSrAVVFXXTZ1gSQWzBqwPn4BgJbAzi12wxcRL2i%2BMWelXDVU00FYUpILGVnYCP5NawRbBo8HINhZKP1t4%2B0W1gpzDqRUcdtys9%2FtswHMGGUUZC%2BMwx4vtvAY6pgGRnxHZNub3MqTQR%2BbXGtjEO83yJpm%2BmFw7o5jp8Q0ySENZ7%2B0Y8qyZmsItWVf9bsNyC7R8I2OeN0Asw476E0mej6NQIdCg3za2RGPIk5XjW8DWal9Rli3NEc8hlf2Cfw76W7vSYn5c9ditvYyeG2VuA8mCIqjNnlnsdYTQQqXGWY3N%2F2WPSnEY%2FZ%2BU87Cpa8%2FC7oB2GiqX3e3QYkKJevqBxSQXNJ4H&X-Amz-Signature=f4d9e0de7ee4ec6f6b7d99a3c3f450b6b74d9792618cf8d6e1d4f6daa497a108&X-Amz-SignedHeaders=host&x-id=GetObject)

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
