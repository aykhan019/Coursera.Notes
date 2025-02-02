

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634PUE2FY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfFcePgMmRXtVFwvM3gRH7pYlDqRc39Qa12oHWup76XgIgKJvITK8uqR8zQHUMpITXHOyhS%2FgqjkFsR1GWEy9SnQoqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA07tfzTQ9%2F%2B84nmVyrcA2dFHGyyh5GoYCscQLjJAUTKd2nATP9e77B4RSOJLolxg%2BaEDoBAipsafix53hWcvjhRIbWrY71iJ1YgdWTmmRuHF8MSd2VVTEVfow%2BaP6id36QKS%2BybLLMQIQAvOp9p8weYzH%2FkVunKNwlqYOfwLSUYbKt9vvr0VKxarPeeTMHGZvGagKMnNsQCMe1F1yUX4ZqOlN5MchyFl8MuSRqFqVpYSobmQvWWlwmNIafOJa7%2BW0Tx1LsDWvQPwpRaqA0OOJjj7oFpzuLfdSdV%2BzZHZ0Qua3cEUO4637MUYkv0q3%2B%2FCIhQtqeKVTRL02zbAbwdC7s9kyUt6ko6xuxunuUsf0nQDVF49eikIVeZiCt1uFpYrRhNzvRGL173MHlhUM262u69Q3SL2q1EDuNiPGMnY%2FcGAdlDaWkQRe8d%2BNjZ4FYBTABZOvh4F0Z4X31zoH071asDVzJUWFKGN9C42hjycgzJ0QXQ1iR4VRnHw3wosVa%2BdKZRg%2FeDYCltjPUJgWZ%2BV6JyxtcXGGOrRpNOc3p8epgc8T6AVWGVInZ8bVO3Xp2rshLhs53z9ry9DcCnTebLuzxAIgJbxMaKfuNd%2FirF64WVrjFvoYa7qeVh8qmgKpuINlzG5URleWmuz%2FeNMLDh%2B7wGOqUB7h3%2FKIR%2BQEtDLlB%2B9atoFU%2FqYiV%2FXNr0Muw1RSFyK1BW0KueDbMQRCKl9wh9bvjT7sCByD5qeD6fAjvFWJK4KqFfTLYBBdYqp786JoMnJl%2F8W%2BV%2FNVmCVyCzaKPsEMStRAFVe%2FAJqItieHcGhOWZsYcwVGUp3iinmWBcDLYm5byO2SdmMElddnlApXvyokltxuXvFQh%2F9nUAUcsmiwSzO72S5NQ6&X-Amz-Signature=dbf8dd7bff2c9dfafcd3eb2239a91a366765577d7c4926b3335adbb8788c04f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634PUE2FY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfFcePgMmRXtVFwvM3gRH7pYlDqRc39Qa12oHWup76XgIgKJvITK8uqR8zQHUMpITXHOyhS%2FgqjkFsR1GWEy9SnQoqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA07tfzTQ9%2F%2B84nmVyrcA2dFHGyyh5GoYCscQLjJAUTKd2nATP9e77B4RSOJLolxg%2BaEDoBAipsafix53hWcvjhRIbWrY71iJ1YgdWTmmRuHF8MSd2VVTEVfow%2BaP6id36QKS%2BybLLMQIQAvOp9p8weYzH%2FkVunKNwlqYOfwLSUYbKt9vvr0VKxarPeeTMHGZvGagKMnNsQCMe1F1yUX4ZqOlN5MchyFl8MuSRqFqVpYSobmQvWWlwmNIafOJa7%2BW0Tx1LsDWvQPwpRaqA0OOJjj7oFpzuLfdSdV%2BzZHZ0Qua3cEUO4637MUYkv0q3%2B%2FCIhQtqeKVTRL02zbAbwdC7s9kyUt6ko6xuxunuUsf0nQDVF49eikIVeZiCt1uFpYrRhNzvRGL173MHlhUM262u69Q3SL2q1EDuNiPGMnY%2FcGAdlDaWkQRe8d%2BNjZ4FYBTABZOvh4F0Z4X31zoH071asDVzJUWFKGN9C42hjycgzJ0QXQ1iR4VRnHw3wosVa%2BdKZRg%2FeDYCltjPUJgWZ%2BV6JyxtcXGGOrRpNOc3p8epgc8T6AVWGVInZ8bVO3Xp2rshLhs53z9ry9DcCnTebLuzxAIgJbxMaKfuNd%2FirF64WVrjFvoYa7qeVh8qmgKpuINlzG5URleWmuz%2FeNMLDh%2B7wGOqUB7h3%2FKIR%2BQEtDLlB%2B9atoFU%2FqYiV%2FXNr0Muw1RSFyK1BW0KueDbMQRCKl9wh9bvjT7sCByD5qeD6fAjvFWJK4KqFfTLYBBdYqp786JoMnJl%2F8W%2BV%2FNVmCVyCzaKPsEMStRAFVe%2FAJqItieHcGhOWZsYcwVGUp3iinmWBcDLYm5byO2SdmMElddnlApXvyokltxuXvFQh%2F9nUAUcsmiwSzO72S5NQ6&X-Amz-Signature=7265019a983811f0f06a04c42838550a0817e1159c55d2bcea0ac7fce4df48fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634PUE2FY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfFcePgMmRXtVFwvM3gRH7pYlDqRc39Qa12oHWup76XgIgKJvITK8uqR8zQHUMpITXHOyhS%2FgqjkFsR1GWEy9SnQoqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA07tfzTQ9%2F%2B84nmVyrcA2dFHGyyh5GoYCscQLjJAUTKd2nATP9e77B4RSOJLolxg%2BaEDoBAipsafix53hWcvjhRIbWrY71iJ1YgdWTmmRuHF8MSd2VVTEVfow%2BaP6id36QKS%2BybLLMQIQAvOp9p8weYzH%2FkVunKNwlqYOfwLSUYbKt9vvr0VKxarPeeTMHGZvGagKMnNsQCMe1F1yUX4ZqOlN5MchyFl8MuSRqFqVpYSobmQvWWlwmNIafOJa7%2BW0Tx1LsDWvQPwpRaqA0OOJjj7oFpzuLfdSdV%2BzZHZ0Qua3cEUO4637MUYkv0q3%2B%2FCIhQtqeKVTRL02zbAbwdC7s9kyUt6ko6xuxunuUsf0nQDVF49eikIVeZiCt1uFpYrRhNzvRGL173MHlhUM262u69Q3SL2q1EDuNiPGMnY%2FcGAdlDaWkQRe8d%2BNjZ4FYBTABZOvh4F0Z4X31zoH071asDVzJUWFKGN9C42hjycgzJ0QXQ1iR4VRnHw3wosVa%2BdKZRg%2FeDYCltjPUJgWZ%2BV6JyxtcXGGOrRpNOc3p8epgc8T6AVWGVInZ8bVO3Xp2rshLhs53z9ry9DcCnTebLuzxAIgJbxMaKfuNd%2FirF64WVrjFvoYa7qeVh8qmgKpuINlzG5URleWmuz%2FeNMLDh%2B7wGOqUB7h3%2FKIR%2BQEtDLlB%2B9atoFU%2FqYiV%2FXNr0Muw1RSFyK1BW0KueDbMQRCKl9wh9bvjT7sCByD5qeD6fAjvFWJK4KqFfTLYBBdYqp786JoMnJl%2F8W%2BV%2FNVmCVyCzaKPsEMStRAFVe%2FAJqItieHcGhOWZsYcwVGUp3iinmWBcDLYm5byO2SdmMElddnlApXvyokltxuXvFQh%2F9nUAUcsmiwSzO72S5NQ6&X-Amz-Signature=d7ce84a458f12bcf098d2260a4524bf4f93622b716d712c57fc8161acc63aa68&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664NDWMZN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNJqZoGdqYhxaxuNNXtVGimxxtBAKv4KreFuewS7DPyAiBkAtGjs7mCSH7EM3stdbonWusORrK7vJpznvueUZfkDiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BrJ6BFqKlfHlDuBbKtwDtAUy8pCpTwD3XAsDgUAnNH4%2FsSuNMFBM0YNGco9uEUDtZqvD6E967K9G1G6aczh47PeUbL%2Bi7EqGcEOIPCjLe%2FQ4ypOQP2lLsgDjHcGdsBqrcpggNfwPfUMr4pGoZMk92pnYbWkjHYGcG1oF%2BWyZlvusS%2Bn5xoj4%2F2jZe%2BQoFY4kf9zcwfa2NMf1h95UAeExuWzf3%2BPrcbEOFP2o57YMXONrSoK7DGKNeFN43U0R0F7GBp8J%2F5jE8gp8b83JSdzLGRDT2txXB%2FCLZqb57ITsDqis2%2FByvKhtEEHd3muLlC2jpzO1EwO5chLXxmOwkXVMRmaVHKeZOSsqPCyp42pcYf7zH7ZfDW8LKRGebi6puh2P1C%2Bu%2FNnXNtB09%2BrWVBBCjzk%2BcDSYVM2ou6gEA6JVyLPT7YCjsixzIuVBfj0Y4WrpZgJk0KadRV240Ca6Uz26hg%2FRI5uen%2F7oO7AOx4Dom52VU0k9q50yWF607iAIrT4pVRAeYe1LwLf5T9akV4lSZizFIBR5ZnmddemkFmNtJyzk6JO1p2QOaeRuv6oz%2FwVeUwgkVdaPetpqDrIhBsDBAiKiV%2BMM5GACkp3E4Fj%2BvVdO9Ch%2Fmc5j0%2Fa1pFneoyiXZfL5qBbg9gR3b6IwzOH7vAY6pgFYKkHWvOAPb58GJtxX78pEltCZ6eAE6USt6iwulqjJjn%2F2sn1AH1OKjm1N3xDbzwCL4nzDmyAe%2BIFJBJey22d9A3IgfbJlMSSf3%2BoSG%2F3b%2FbZ%2FL4imbOypvrfzVtzRXHXSWtQmKbfunwnIjc8K%2BHh1ikHTe8UZMOBPFt6o8REq3lbyyEx55CFLKi%2FuuoIDT3dv08%2BhiEcU5SBUBvH6h4N%2Fe7ijFVQq&X-Amz-Signature=5bba9a7627f86300d73f8625e8c022a92a3918839635b09ae44aca0c69a69633&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664NDWMZN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNJqZoGdqYhxaxuNNXtVGimxxtBAKv4KreFuewS7DPyAiBkAtGjs7mCSH7EM3stdbonWusORrK7vJpznvueUZfkDiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BrJ6BFqKlfHlDuBbKtwDtAUy8pCpTwD3XAsDgUAnNH4%2FsSuNMFBM0YNGco9uEUDtZqvD6E967K9G1G6aczh47PeUbL%2Bi7EqGcEOIPCjLe%2FQ4ypOQP2lLsgDjHcGdsBqrcpggNfwPfUMr4pGoZMk92pnYbWkjHYGcG1oF%2BWyZlvusS%2Bn5xoj4%2F2jZe%2BQoFY4kf9zcwfa2NMf1h95UAeExuWzf3%2BPrcbEOFP2o57YMXONrSoK7DGKNeFN43U0R0F7GBp8J%2F5jE8gp8b83JSdzLGRDT2txXB%2FCLZqb57ITsDqis2%2FByvKhtEEHd3muLlC2jpzO1EwO5chLXxmOwkXVMRmaVHKeZOSsqPCyp42pcYf7zH7ZfDW8LKRGebi6puh2P1C%2Bu%2FNnXNtB09%2BrWVBBCjzk%2BcDSYVM2ou6gEA6JVyLPT7YCjsixzIuVBfj0Y4WrpZgJk0KadRV240Ca6Uz26hg%2FRI5uen%2F7oO7AOx4Dom52VU0k9q50yWF607iAIrT4pVRAeYe1LwLf5T9akV4lSZizFIBR5ZnmddemkFmNtJyzk6JO1p2QOaeRuv6oz%2FwVeUwgkVdaPetpqDrIhBsDBAiKiV%2BMM5GACkp3E4Fj%2BvVdO9Ch%2Fmc5j0%2Fa1pFneoyiXZfL5qBbg9gR3b6IwzOH7vAY6pgFYKkHWvOAPb58GJtxX78pEltCZ6eAE6USt6iwulqjJjn%2F2sn1AH1OKjm1N3xDbzwCL4nzDmyAe%2BIFJBJey22d9A3IgfbJlMSSf3%2BoSG%2F3b%2FbZ%2FL4imbOypvrfzVtzRXHXSWtQmKbfunwnIjc8K%2BHh1ikHTe8UZMOBPFt6o8REq3lbyyEx55CFLKi%2FuuoIDT3dv08%2BhiEcU5SBUBvH6h4N%2Fe7ijFVQq&X-Amz-Signature=fde3cdebb8ae8f4ea540f2ba7353c1e42cf8c4927971a8db03b848183a28d8f3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664NDWMZN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNJqZoGdqYhxaxuNNXtVGimxxtBAKv4KreFuewS7DPyAiBkAtGjs7mCSH7EM3stdbonWusORrK7vJpznvueUZfkDiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BrJ6BFqKlfHlDuBbKtwDtAUy8pCpTwD3XAsDgUAnNH4%2FsSuNMFBM0YNGco9uEUDtZqvD6E967K9G1G6aczh47PeUbL%2Bi7EqGcEOIPCjLe%2FQ4ypOQP2lLsgDjHcGdsBqrcpggNfwPfUMr4pGoZMk92pnYbWkjHYGcG1oF%2BWyZlvusS%2Bn5xoj4%2F2jZe%2BQoFY4kf9zcwfa2NMf1h95UAeExuWzf3%2BPrcbEOFP2o57YMXONrSoK7DGKNeFN43U0R0F7GBp8J%2F5jE8gp8b83JSdzLGRDT2txXB%2FCLZqb57ITsDqis2%2FByvKhtEEHd3muLlC2jpzO1EwO5chLXxmOwkXVMRmaVHKeZOSsqPCyp42pcYf7zH7ZfDW8LKRGebi6puh2P1C%2Bu%2FNnXNtB09%2BrWVBBCjzk%2BcDSYVM2ou6gEA6JVyLPT7YCjsixzIuVBfj0Y4WrpZgJk0KadRV240Ca6Uz26hg%2FRI5uen%2F7oO7AOx4Dom52VU0k9q50yWF607iAIrT4pVRAeYe1LwLf5T9akV4lSZizFIBR5ZnmddemkFmNtJyzk6JO1p2QOaeRuv6oz%2FwVeUwgkVdaPetpqDrIhBsDBAiKiV%2BMM5GACkp3E4Fj%2BvVdO9Ch%2Fmc5j0%2Fa1pFneoyiXZfL5qBbg9gR3b6IwzOH7vAY6pgFYKkHWvOAPb58GJtxX78pEltCZ6eAE6USt6iwulqjJjn%2F2sn1AH1OKjm1N3xDbzwCL4nzDmyAe%2BIFJBJey22d9A3IgfbJlMSSf3%2BoSG%2F3b%2FbZ%2FL4imbOypvrfzVtzRXHXSWtQmKbfunwnIjc8K%2BHh1ikHTe8UZMOBPFt6o8REq3lbyyEx55CFLKi%2FuuoIDT3dv08%2BhiEcU5SBUBvH6h4N%2Fe7ijFVQq&X-Amz-Signature=dd0b91be5e7278ff1a11d7a1e7877598fea33c44fffae960203fbfc959030784&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664NDWMZN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNJqZoGdqYhxaxuNNXtVGimxxtBAKv4KreFuewS7DPyAiBkAtGjs7mCSH7EM3stdbonWusORrK7vJpznvueUZfkDiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BrJ6BFqKlfHlDuBbKtwDtAUy8pCpTwD3XAsDgUAnNH4%2FsSuNMFBM0YNGco9uEUDtZqvD6E967K9G1G6aczh47PeUbL%2Bi7EqGcEOIPCjLe%2FQ4ypOQP2lLsgDjHcGdsBqrcpggNfwPfUMr4pGoZMk92pnYbWkjHYGcG1oF%2BWyZlvusS%2Bn5xoj4%2F2jZe%2BQoFY4kf9zcwfa2NMf1h95UAeExuWzf3%2BPrcbEOFP2o57YMXONrSoK7DGKNeFN43U0R0F7GBp8J%2F5jE8gp8b83JSdzLGRDT2txXB%2FCLZqb57ITsDqis2%2FByvKhtEEHd3muLlC2jpzO1EwO5chLXxmOwkXVMRmaVHKeZOSsqPCyp42pcYf7zH7ZfDW8LKRGebi6puh2P1C%2Bu%2FNnXNtB09%2BrWVBBCjzk%2BcDSYVM2ou6gEA6JVyLPT7YCjsixzIuVBfj0Y4WrpZgJk0KadRV240Ca6Uz26hg%2FRI5uen%2F7oO7AOx4Dom52VU0k9q50yWF607iAIrT4pVRAeYe1LwLf5T9akV4lSZizFIBR5ZnmddemkFmNtJyzk6JO1p2QOaeRuv6oz%2FwVeUwgkVdaPetpqDrIhBsDBAiKiV%2BMM5GACkp3E4Fj%2BvVdO9Ch%2Fmc5j0%2Fa1pFneoyiXZfL5qBbg9gR3b6IwzOH7vAY6pgFYKkHWvOAPb58GJtxX78pEltCZ6eAE6USt6iwulqjJjn%2F2sn1AH1OKjm1N3xDbzwCL4nzDmyAe%2BIFJBJey22d9A3IgfbJlMSSf3%2BoSG%2F3b%2FbZ%2FL4imbOypvrfzVtzRXHXSWtQmKbfunwnIjc8K%2BHh1ikHTe8UZMOBPFt6o8REq3lbyyEx55CFLKi%2FuuoIDT3dv08%2BhiEcU5SBUBvH6h4N%2Fe7ijFVQq&X-Amz-Signature=c928882cf9d424f90adf0ab1a7c258e32fc88e3a8d099617d90c5f6eae2252eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664NDWMZN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNJqZoGdqYhxaxuNNXtVGimxxtBAKv4KreFuewS7DPyAiBkAtGjs7mCSH7EM3stdbonWusORrK7vJpznvueUZfkDiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BrJ6BFqKlfHlDuBbKtwDtAUy8pCpTwD3XAsDgUAnNH4%2FsSuNMFBM0YNGco9uEUDtZqvD6E967K9G1G6aczh47PeUbL%2Bi7EqGcEOIPCjLe%2FQ4ypOQP2lLsgDjHcGdsBqrcpggNfwPfUMr4pGoZMk92pnYbWkjHYGcG1oF%2BWyZlvusS%2Bn5xoj4%2F2jZe%2BQoFY4kf9zcwfa2NMf1h95UAeExuWzf3%2BPrcbEOFP2o57YMXONrSoK7DGKNeFN43U0R0F7GBp8J%2F5jE8gp8b83JSdzLGRDT2txXB%2FCLZqb57ITsDqis2%2FByvKhtEEHd3muLlC2jpzO1EwO5chLXxmOwkXVMRmaVHKeZOSsqPCyp42pcYf7zH7ZfDW8LKRGebi6puh2P1C%2Bu%2FNnXNtB09%2BrWVBBCjzk%2BcDSYVM2ou6gEA6JVyLPT7YCjsixzIuVBfj0Y4WrpZgJk0KadRV240Ca6Uz26hg%2FRI5uen%2F7oO7AOx4Dom52VU0k9q50yWF607iAIrT4pVRAeYe1LwLf5T9akV4lSZizFIBR5ZnmddemkFmNtJyzk6JO1p2QOaeRuv6oz%2FwVeUwgkVdaPetpqDrIhBsDBAiKiV%2BMM5GACkp3E4Fj%2BvVdO9Ch%2Fmc5j0%2Fa1pFneoyiXZfL5qBbg9gR3b6IwzOH7vAY6pgFYKkHWvOAPb58GJtxX78pEltCZ6eAE6USt6iwulqjJjn%2F2sn1AH1OKjm1N3xDbzwCL4nzDmyAe%2BIFJBJey22d9A3IgfbJlMSSf3%2BoSG%2F3b%2FbZ%2FL4imbOypvrfzVtzRXHXSWtQmKbfunwnIjc8K%2BHh1ikHTe8UZMOBPFt6o8REq3lbyyEx55CFLKi%2FuuoIDT3dv08%2BhiEcU5SBUBvH6h4N%2Fe7ijFVQq&X-Amz-Signature=617a9f193db7856d5e530f67d400e8b73c55c9bf9726a8a932861b5067567aa2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664NDWMZN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNJqZoGdqYhxaxuNNXtVGimxxtBAKv4KreFuewS7DPyAiBkAtGjs7mCSH7EM3stdbonWusORrK7vJpznvueUZfkDiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BrJ6BFqKlfHlDuBbKtwDtAUy8pCpTwD3XAsDgUAnNH4%2FsSuNMFBM0YNGco9uEUDtZqvD6E967K9G1G6aczh47PeUbL%2Bi7EqGcEOIPCjLe%2FQ4ypOQP2lLsgDjHcGdsBqrcpggNfwPfUMr4pGoZMk92pnYbWkjHYGcG1oF%2BWyZlvusS%2Bn5xoj4%2F2jZe%2BQoFY4kf9zcwfa2NMf1h95UAeExuWzf3%2BPrcbEOFP2o57YMXONrSoK7DGKNeFN43U0R0F7GBp8J%2F5jE8gp8b83JSdzLGRDT2txXB%2FCLZqb57ITsDqis2%2FByvKhtEEHd3muLlC2jpzO1EwO5chLXxmOwkXVMRmaVHKeZOSsqPCyp42pcYf7zH7ZfDW8LKRGebi6puh2P1C%2Bu%2FNnXNtB09%2BrWVBBCjzk%2BcDSYVM2ou6gEA6JVyLPT7YCjsixzIuVBfj0Y4WrpZgJk0KadRV240Ca6Uz26hg%2FRI5uen%2F7oO7AOx4Dom52VU0k9q50yWF607iAIrT4pVRAeYe1LwLf5T9akV4lSZizFIBR5ZnmddemkFmNtJyzk6JO1p2QOaeRuv6oz%2FwVeUwgkVdaPetpqDrIhBsDBAiKiV%2BMM5GACkp3E4Fj%2BvVdO9Ch%2Fmc5j0%2Fa1pFneoyiXZfL5qBbg9gR3b6IwzOH7vAY6pgFYKkHWvOAPb58GJtxX78pEltCZ6eAE6USt6iwulqjJjn%2F2sn1AH1OKjm1N3xDbzwCL4nzDmyAe%2BIFJBJey22d9A3IgfbJlMSSf3%2BoSG%2F3b%2FbZ%2FL4imbOypvrfzVtzRXHXSWtQmKbfunwnIjc8K%2BHh1ikHTe8UZMOBPFt6o8REq3lbyyEx55CFLKi%2FuuoIDT3dv08%2BhiEcU5SBUBvH6h4N%2Fe7ijFVQq&X-Amz-Signature=eeb3d9cfc8569455ff42e7791ea0e6e6a577a28819b9f03f22aac420b1bc70aa&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VK5NTNZV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFz2JImAb008DbKg4YHG0Vue0N5FhYgZpKhL2hoWkqSHAiBTkdJbOuRgy%2FTK%2FqsDTc4CEfAiMdVrhKWssrfGTjc3UyqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcjwlZaH2Gt1Gc%2FGZKtwDVquBrvnbj%2FWjAkIOPbeka%2B5zzRuJnWAQ1bCABzDMSVTyP5PqQBYl6YRxY5NEN6jRtnYgApTYJLIq%2BgrKCwQQ%2FJBGSgRSr8CBIacXZeFfthe8fiUTPDxBzwOyXja%2FpsJm%2BOqP50Xc%2FEC5O%2FO7nPedX5zuj4F3OT8zMAzTw5sYaJm09BBDEevC0YHqwX5ieRy8R7vsvx4pkW49%2FnawwhTeC4OOfd3z3QTibrA4DZ8Vp6l2y2pMDZrx%2BsaFsbJ71%2FPtf69YqfFeMm6Tv8ss4CGKDnOxYPSxdP90c1N%2FpDr4vl%2F5hOBzlgoOUMc5Tl1CosIgO96TEzgVqmDpIOREoupph6idNeMWh%2BVY6cVN5Qkr%2B9uKPGTAPBTY0qMxY0IrQkQQx9OoliTNTlrr4PYmHFD4%2FY2JArVJDlo%2FrUnJKrFwzqCnHmlFP9Y9T6z4qTH9ljNVNRP%2FN6LpSp70y55XZXkFq6ZFHfYP9%2Bu5D%2B5%2FPEle%2FyGFNYJ1H3aQeWUHSElZX0YEzsmPqd5endDQIZAqwtWhInP%2F8CVejp66%2BrSZkvbJRh5PJ6cKcUwpFZ9%2FyL6J9goIVtBpRg%2FX3X1iDWkJBwH5%2FrlSQLpijVLztta0gZZUmqZykDnvfZyE3mQ9iR4wzOH7vAY6pgH2HvLEF3xThh1Usmqi8go2cb6WKaGbj%2BtkPp95y9BdtKhffcz5hlOQSNhxyt16bxS%2FHkyMKlV1%2B5cjAaCsp0cXrYWG5GLceXk6%2F1r%2FJVN3dnYT%2FLJBw%2BLBQURY0MLeI%2BPfZPEz8zLFBrCwE6u0MxXqp2MVXdP%2FZ9yrfj0cUvBUDfApt27EwNfUFV%2B45iZE6zT%2BFP6L7BJLi3MkTSkYSzosuaaAfDu5&X-Amz-Signature=6931d03666aa62c5c31a4d0a30674d643f2ea04bc63aec683e28de8f2dc2d1f2&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623E5TJ4U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBostNEsO7scoPU9sykSwvBDKgCLNbIm9Z2IJN7U%2FiXNAiAVaRfK9T3wmvc3znw5sFfp4JHAA8xYF5wEwSl7HKKP2iqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9gwjxJZN%2FUoFkLWnKtwDi5vlN%2Bdnitj%2FB5tqkxgfM1HoohYGXwy6TCsRrMJXUXb2DB7Gw3BMT2bASbx04CUTFjjf6r0biBJ%2FBlsXsQqpr6Zl%2BXoVKfpXnZDLFBt1tKzg2yPi2138nrGPtXVaqksww96qahQLUvY5T8x4l1adwSiefR5qDxwB9jByLvPwVSPPQ5%2BZHWwL9sbedNom3A2zPY6NHcV%2FoyZRBtdyWcsDw18iw4ToB0zC6NCE%2Bmzk4mD4FbZGsGPiFMyYJfo9%2FmM3YFaMDU9EUceyQR%2FWkaRYwcnY2LWccJrwVZkYfFd9kPNp53XoirdgCpBEw9xD%2FLGOfApZue%2B493fkb0rZmWMWxfcmJTW7hRk4jzgQyfdbOFJFBnfg%2BxCgnTlytpX6UCOmQ5TmOLk%2FWG1dVI%2Bj3qpNe8qvl7yTb4zEQ%2FFoWIb9QHayY3%2FVw4i%2F6yPuRgsAE0U9%2BKwP7SdYqJW7BfO7oDZvN8Xz%2FjIFm%2Fip2PDi2Nf5JjbbD2C9hEXN9QTwcfi7ulRvT%2Fl5V8n4S3KO3uGqi%2BPeAfDMBQZrnETyJFlufXwruHgzjrFQJvoM1cvHzcIRsoDNP8Kd0NQ93rOplvaKsOZRmeuUUMu6IlhIAj%2FG%2BO0qkSRVWxlvyNuvHOLtytUwzOH7vAY6pgGF2roYixkcuYY%2Bcz48vLe0amLNeD1ifIn3YFOCV3XvmsswsBOWf7GTuMoxPhsZPc4BUp6%2By7ecjf2ivL38R4ZLlKbB7RN73DvNzG8yt%2BFVzsesumJtP0jrVWql3vbtAKqWXoM8gJsP560vmWKtDRQDrul2aFQIGhah8ec6dYHTxU7PvNfA1FgeQlx3w%2BdzzaPaZMaaqV1yMI55zftkU3fy0F7FUC%2FC&X-Amz-Signature=f27bebe965e0e0cb5bf87a4dc4e10d4067446ce5fb9f9e4d0ce28e833f7c783e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664NDWMZN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNJqZoGdqYhxaxuNNXtVGimxxtBAKv4KreFuewS7DPyAiBkAtGjs7mCSH7EM3stdbonWusORrK7vJpznvueUZfkDiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BrJ6BFqKlfHlDuBbKtwDtAUy8pCpTwD3XAsDgUAnNH4%2FsSuNMFBM0YNGco9uEUDtZqvD6E967K9G1G6aczh47PeUbL%2Bi7EqGcEOIPCjLe%2FQ4ypOQP2lLsgDjHcGdsBqrcpggNfwPfUMr4pGoZMk92pnYbWkjHYGcG1oF%2BWyZlvusS%2Bn5xoj4%2F2jZe%2BQoFY4kf9zcwfa2NMf1h95UAeExuWzf3%2BPrcbEOFP2o57YMXONrSoK7DGKNeFN43U0R0F7GBp8J%2F5jE8gp8b83JSdzLGRDT2txXB%2FCLZqb57ITsDqis2%2FByvKhtEEHd3muLlC2jpzO1EwO5chLXxmOwkXVMRmaVHKeZOSsqPCyp42pcYf7zH7ZfDW8LKRGebi6puh2P1C%2Bu%2FNnXNtB09%2BrWVBBCjzk%2BcDSYVM2ou6gEA6JVyLPT7YCjsixzIuVBfj0Y4WrpZgJk0KadRV240Ca6Uz26hg%2FRI5uen%2F7oO7AOx4Dom52VU0k9q50yWF607iAIrT4pVRAeYe1LwLf5T9akV4lSZizFIBR5ZnmddemkFmNtJyzk6JO1p2QOaeRuv6oz%2FwVeUwgkVdaPetpqDrIhBsDBAiKiV%2BMM5GACkp3E4Fj%2BvVdO9Ch%2Fmc5j0%2Fa1pFneoyiXZfL5qBbg9gR3b6IwzOH7vAY6pgFYKkHWvOAPb58GJtxX78pEltCZ6eAE6USt6iwulqjJjn%2F2sn1AH1OKjm1N3xDbzwCL4nzDmyAe%2BIFJBJey22d9A3IgfbJlMSSf3%2BoSG%2F3b%2FbZ%2FL4imbOypvrfzVtzRXHXSWtQmKbfunwnIjc8K%2BHh1ikHTe8UZMOBPFt6o8REq3lbyyEx55CFLKi%2FuuoIDT3dv08%2BhiEcU5SBUBvH6h4N%2Fe7ijFVQq&X-Amz-Signature=34c9639554dfcff0ced37b371cf7dca2f2ba06254fc06cb911ff8ab03f04594c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664NDWMZN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNJqZoGdqYhxaxuNNXtVGimxxtBAKv4KreFuewS7DPyAiBkAtGjs7mCSH7EM3stdbonWusORrK7vJpznvueUZfkDiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BrJ6BFqKlfHlDuBbKtwDtAUy8pCpTwD3XAsDgUAnNH4%2FsSuNMFBM0YNGco9uEUDtZqvD6E967K9G1G6aczh47PeUbL%2Bi7EqGcEOIPCjLe%2FQ4ypOQP2lLsgDjHcGdsBqrcpggNfwPfUMr4pGoZMk92pnYbWkjHYGcG1oF%2BWyZlvusS%2Bn5xoj4%2F2jZe%2BQoFY4kf9zcwfa2NMf1h95UAeExuWzf3%2BPrcbEOFP2o57YMXONrSoK7DGKNeFN43U0R0F7GBp8J%2F5jE8gp8b83JSdzLGRDT2txXB%2FCLZqb57ITsDqis2%2FByvKhtEEHd3muLlC2jpzO1EwO5chLXxmOwkXVMRmaVHKeZOSsqPCyp42pcYf7zH7ZfDW8LKRGebi6puh2P1C%2Bu%2FNnXNtB09%2BrWVBBCjzk%2BcDSYVM2ou6gEA6JVyLPT7YCjsixzIuVBfj0Y4WrpZgJk0KadRV240Ca6Uz26hg%2FRI5uen%2F7oO7AOx4Dom52VU0k9q50yWF607iAIrT4pVRAeYe1LwLf5T9akV4lSZizFIBR5ZnmddemkFmNtJyzk6JO1p2QOaeRuv6oz%2FwVeUwgkVdaPetpqDrIhBsDBAiKiV%2BMM5GACkp3E4Fj%2BvVdO9Ch%2Fmc5j0%2Fa1pFneoyiXZfL5qBbg9gR3b6IwzOH7vAY6pgFYKkHWvOAPb58GJtxX78pEltCZ6eAE6USt6iwulqjJjn%2F2sn1AH1OKjm1N3xDbzwCL4nzDmyAe%2BIFJBJey22d9A3IgfbJlMSSf3%2BoSG%2F3b%2FbZ%2FL4imbOypvrfzVtzRXHXSWtQmKbfunwnIjc8K%2BHh1ikHTe8UZMOBPFt6o8REq3lbyyEx55CFLKi%2FuuoIDT3dv08%2BhiEcU5SBUBvH6h4N%2Fe7ijFVQq&X-Amz-Signature=271e1e50cd3c77b6d09ec29fc776eeb3faf67dc080dad789112517dc3718b80a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664NDWMZN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNJqZoGdqYhxaxuNNXtVGimxxtBAKv4KreFuewS7DPyAiBkAtGjs7mCSH7EM3stdbonWusORrK7vJpznvueUZfkDiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BrJ6BFqKlfHlDuBbKtwDtAUy8pCpTwD3XAsDgUAnNH4%2FsSuNMFBM0YNGco9uEUDtZqvD6E967K9G1G6aczh47PeUbL%2Bi7EqGcEOIPCjLe%2FQ4ypOQP2lLsgDjHcGdsBqrcpggNfwPfUMr4pGoZMk92pnYbWkjHYGcG1oF%2BWyZlvusS%2Bn5xoj4%2F2jZe%2BQoFY4kf9zcwfa2NMf1h95UAeExuWzf3%2BPrcbEOFP2o57YMXONrSoK7DGKNeFN43U0R0F7GBp8J%2F5jE8gp8b83JSdzLGRDT2txXB%2FCLZqb57ITsDqis2%2FByvKhtEEHd3muLlC2jpzO1EwO5chLXxmOwkXVMRmaVHKeZOSsqPCyp42pcYf7zH7ZfDW8LKRGebi6puh2P1C%2Bu%2FNnXNtB09%2BrWVBBCjzk%2BcDSYVM2ou6gEA6JVyLPT7YCjsixzIuVBfj0Y4WrpZgJk0KadRV240Ca6Uz26hg%2FRI5uen%2F7oO7AOx4Dom52VU0k9q50yWF607iAIrT4pVRAeYe1LwLf5T9akV4lSZizFIBR5ZnmddemkFmNtJyzk6JO1p2QOaeRuv6oz%2FwVeUwgkVdaPetpqDrIhBsDBAiKiV%2BMM5GACkp3E4Fj%2BvVdO9Ch%2Fmc5j0%2Fa1pFneoyiXZfL5qBbg9gR3b6IwzOH7vAY6pgFYKkHWvOAPb58GJtxX78pEltCZ6eAE6USt6iwulqjJjn%2F2sn1AH1OKjm1N3xDbzwCL4nzDmyAe%2BIFJBJey22d9A3IgfbJlMSSf3%2BoSG%2F3b%2FbZ%2FL4imbOypvrfzVtzRXHXSWtQmKbfunwnIjc8K%2BHh1ikHTe8UZMOBPFt6o8REq3lbyyEx55CFLKi%2FuuoIDT3dv08%2BhiEcU5SBUBvH6h4N%2Fe7ijFVQq&X-Amz-Signature=ec0a67a642df3cfbc820880ce138d776194288420bcc17e71433c257d4fe447b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKM6D2AO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIANpC%2F2CALX2QGqk1yXULNikvTpcOzccqifVb98LsEK9AiEAkOia690RzNEi2kCMI1MotX%2BvCyvA6JplxEeE4TKE1HoqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEERAMOYowCGvIM8IircA5OSPeK8eeyrhh4Onv1bJth2b%2Fh%2FktfOfO0ApOLbP68AL0zojs0dm4zjVvicpWKR9oMXm8MCL%2FfnzdjjS42VaKWlHTOw63q0KeF0A4BA0WRkTupgbP2zFAgsYoCIP8evs6xQtNGFDyoBezQJPXHxr84%2FjfHbfy%2B06W%2FCfDLnaHK34Dbt82sgLZjwVCK0WJMMQ8Yh8cjoFB007dVSx%2FRMv0LAUXOXp507NlIZKaEIiYV9RK4yFWltONyeXcnbDxGM71NsvDEO1azSwVbUxtCdZZ7nZ2OA49B2UJEURHfviMJmnVroy%2FszZtCC3FGr%2BcvlD0Jm6hBDLdvWt8tqS0zVVVc%2FjPTwiRObQ3Ua8OCywoilw0h1zGxHVzuZ8UWQnzM%2FAs3KgwC%2FGwDOu5tE84EeDTOFQDcbUSpLnQaCLlSH%2FxY2mBHIP8HPIfjlP7aUlSbb7UuIfj8GYtEsSS5tmM%2F8EuowcVzkY1A2xWT20v8tC4EzYzpNQZiOrQZD6qtoYMpzWPRtk%2FP1v%2FRF%2F7gUl7304Ty0uPLN7YRFOr2cF3wSW%2FjZNd4VcOQl4yNnVN8enljYipHGaJ9cJVY5S%2BFvSwlohWKaD3bJ7bKkMrV8kWS1Oa9Va7ydxDr1eum8UvaJMJXh%2B7wGOqUBO7I77qoHvYPHsJHxLjih1lq4Zn8yb2w6IrNHmXrFUMlvsa35n9Bzu%2F5T6dFHEho0XjGWkdpU9ioCTOALdO7LekAx6qMjmRVfeexHHgDx0jy5N0IUfoJ%2BYkfOzTokaugEiNo0skCXn3r1ERuiTjHSahZV8yJu4ntDXm2jVfRkpb2e%2BvCPcqO8ov19Eno7BK44aqQiZ6oejC078whznJ67laJy0C4k&X-Amz-Signature=816838d3a7a178c6b8ad179c023c174bb40b5c8b247a6a2f76a99265b008fc50&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBRO2FHE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG8mLva3c7gsRk%2BlFRlKndJgculd7EH6BFSE9lJZ%2BFEIAiBl7IzqJLd9atXQeDFeAtCkJBWkgFlUlJrMXVE3J2RmliqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYfFdMeXgxUVWbT0qKtwDKMDloLDcpEv1TDAAWVQzHRW9IrS7yv0WWjQpuQEQ5PygVDTXJc4ZesvvuowJ4zNmjEplqnwltZtKGseadptWbIL8iFPfhkH1I9n5vBnRLH5pwg1kAPoBFbo%2BJbx0Wj%2BTVxQryOJS0%2FB6POIKyBl%2FPyYNVieErRngGV49Z5cvgAOF1AI%2B0uO1BFvqteEqzn4tl0eM6hNmpVewYsSLzGw%2B%2FLETUNG8lR6X%2FGlTFTOA3bfZAvD%2B0ayT6wzSWnlYRn3yboUU1LesusM3qCmLALwAtnAGdXsT875gopT8SUIHyS81ieLnfh2SQ2RNSBEShtGUaROPuLnf0VFd0qYlsVMYh2zuf9CRMBFQRWZGHLds5DHlyFYUe8cqVQIyiHgR194t1mNkAysflrnhG1vQ%2Bfv1ZZaHkZxex26E%2BFcjP1sbYYdSvDgcdynVZTRHJ%2Fpcx%2BkwweYjLM9nx2JLedoH8ov8zpK65mZFC190N2E8MnHgg2eG2KbHIzgNO9EAZQhTNdiVa4PoBZ2%2FiKNPrBYGhdm1Z20jj%2FcfCy9mxHi9G%2BbvMjNr44W%2Bphb2KxxZZwMzXibFmlVIr%2FoJB6t1QSpJ4%2Fx1TzUTTIlUVcZ8WkPwiAINqmRrZfpOoOy8v4jLEoYwjuH7vAY6pgFHcA854HViNYPrBuLHprKdwu5yRDX507%2F5KGsUhxytL%2FQT3K5YU3%2BZ7%2Fw841oBJh3v47CoHzJuRYkzQctrLM3oCeYMG3nk8aZqvfSMMH3Gm4lCxf%2BrtykKWkoJvFYDuvAvdl8qEx9P5DVT8Wy8R1SYzjcvHpzF7ELJCgun03ala8kc9k4Ng777YcosKSNg8tQJYHAHVAuTofCKwPznLRXNNiqavYmP&X-Amz-Signature=3e67312bcb62c80ada3792935ecdb6420d624a05c54b579b3b1fddaf1b0553ed&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MZONDQ5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAjwbE%2BYVHIZH0Fmjb1a%2FIrj5OBM3nN6bYZ51d7yyINQIgfispDawdeJsLQpkjwWW0UfoDTnnaKXMzALV3PQjKdt8qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPi6zzkTBqbn8FNTYCrcAzBwpcVnZkbdXeDMupUn49nuk1CWAGB7I%2Fo2eukwFtGAtAfneHinDr%2FGgI7PaRUfHEE6i%2FnBvwYxhaNiGQY%2F88fwqppUIhozSmqAKfUOaGADDx%2FWSTKIvEltY%2F059Z%2B8yfwVsSL0G5Yfw%2FaV99w1TCqsIOshUB7JaC9rRX2CwbthyoOcR2YHmR%2BBLNyq2BaKTP8XOLcw%2BAt9uefAGZdFoTraal%2FMlHTkkts4XdcK0tsfAlBACbb3b2%2Fvv8tOYqsy4qrwvejT3FVc5UdOnc%2BhJ6WLsnW1LImmJiNu7zMHPT%2B8p%2BgyNzKByf7hePhM6UnjyAf5M5ld3y7yF491DM%2BGtCirdHOl24WnMSKB1EGwOES685Y6lyXhcU3thlUwO3YT1BlMjr2hSe4nBNxZ6Vp68UJrrH%2FsZ%2FJgyphS%2FrLQOuu5obLYW7%2FrhITq1RoifIVUEJr8haJk98lgsKSmHUY1YQ5iIzYykEZOm5P9W%2BIPrftgzsFJZWqIuHK6j59HxeS%2BNLApv2QFHqm4EbJNk9dpH1JtdMATSkJ2YVyH61teVMpBk%2FfnWjnVblBLAgAlfUNqAFEQBmHgXdbjL1MKof8qpxzQENs2ZQvJ8XGMYLjaGBS79qHOHejURxxhlWj%2FMJjh%2B7wGOqUBXdVo%2BiZgbLRUroHETRFXua5r822tmjaFycP9iEbBuScby4TnOowBh98XzBKSx6zlxHUY9jkTAtqLJAD%2BcLaY24vqkBJzBlvkkDegtv5XLn%2FMPtDP%2FfdYfKUXOCBjFnLSBX8fYou8YebOACwVR7gEZHCwCi%2BAtic66Vt9dZfvD7ZxuynnwTuzdxPnlkWS1AtR4Ml3%2FJfYjCKwYqarpCZb8RxPLb0T&X-Amz-Signature=b621fbb7785cc9150bde04bec3536d8c644eda4425a3f7045923dabbdc6d8aef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSGPVRM7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDC2vNWy%2BhEv9E%2Flgm0uAeVnZ9aquffdsrnkR0HZphVugIhAMX6sVLfoeY0UKJenkYUDEaazeN2q%2FgQkOhg2nKyyivhKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igza2oLUUgfeUnhDqfkq3AMvQmZVDpo7muG90dz9vNZtC9yEl3hxwi1fORJxNdD84IeLzKlbTfr2qoqi%2Bzmj3smhYZc74GnvjQFTP5RNBB8N56J7S7%2BU%2Fp7LoqzEClu1%2Bhmp1hQ45T3yaY0rY%2B8KsdYFKO3SMHRzOlqZk61OxqydqVl93wRiVs5BAjMJuM4TExJx6sTwfB8guSZpjGCOL9rJ4zkTOtClu5r3e61%2BpyicXjSTkHg9mn9N8hVJFxM15HAvDJE%2B1HcqJ1IJQNbTwqvFdLmNucyIs0cAENw3fDdwf6KS2w282mU7b4EG24mihDPNEC935Y4EUOGfEGNPuTHPDPgT23OIfYVSzezwt9%2BZz43Uzsf03plm%2BLOz57KiT3ZsdBSQKYisCXZ%2FbN21exeAtehzZoGLtjksKHG3YcvCLkjB99LGGgM95fDXS1STf7fKuvfJ0nU88mYTm77RWw14MNVlLaRywUZnaKdDDndK4TjZzLksdKKcoFNBKORjIYpDFLNtVvfxEnilIPKvcWvvGCfc74bMDjdBtkMAUD7ftIFIDrd91u5VM1l%2FS%2F5fOtAwiUnKUoKgV%2Fx8zxg3Gh5a%2BgMOIDPOGVlsIcbhhiL67OEnOtLLdbC70VVfHRBr3mj%2FyeyQe8rKkOTEwjDW4fu8BjqkAZVXQuaIOG3e0g0Qpa4GOQ4%2BlbytTOruXuH7QQr3rbTfPTGHpWCgHhkTyM9cBJ%2FF4TjRMb0vFFMt30XWxasFnFUIKBtdBJmYisaWvguzyxDiedHr9BTC44RS6JNBJvagpXKtpwWQxQs43xCFvMSf8rKI5%2Bc%2BxV6vYN9tuWTS%2BXjmb4T7rYKaXc6s%2BcaxewXxWLyi7wGMq3AftThb9y%2Ftyp78LZ31&X-Amz-Signature=474f9c54ac9baf27a4126fd0cc08e336c2c043b2badbde33a4be0e3d0a1a24f5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSGPVRM7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDC2vNWy%2BhEv9E%2Flgm0uAeVnZ9aquffdsrnkR0HZphVugIhAMX6sVLfoeY0UKJenkYUDEaazeN2q%2FgQkOhg2nKyyivhKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igza2oLUUgfeUnhDqfkq3AMvQmZVDpo7muG90dz9vNZtC9yEl3hxwi1fORJxNdD84IeLzKlbTfr2qoqi%2Bzmj3smhYZc74GnvjQFTP5RNBB8N56J7S7%2BU%2Fp7LoqzEClu1%2Bhmp1hQ45T3yaY0rY%2B8KsdYFKO3SMHRzOlqZk61OxqydqVl93wRiVs5BAjMJuM4TExJx6sTwfB8guSZpjGCOL9rJ4zkTOtClu5r3e61%2BpyicXjSTkHg9mn9N8hVJFxM15HAvDJE%2B1HcqJ1IJQNbTwqvFdLmNucyIs0cAENw3fDdwf6KS2w282mU7b4EG24mihDPNEC935Y4EUOGfEGNPuTHPDPgT23OIfYVSzezwt9%2BZz43Uzsf03plm%2BLOz57KiT3ZsdBSQKYisCXZ%2FbN21exeAtehzZoGLtjksKHG3YcvCLkjB99LGGgM95fDXS1STf7fKuvfJ0nU88mYTm77RWw14MNVlLaRywUZnaKdDDndK4TjZzLksdKKcoFNBKORjIYpDFLNtVvfxEnilIPKvcWvvGCfc74bMDjdBtkMAUD7ftIFIDrd91u5VM1l%2FS%2F5fOtAwiUnKUoKgV%2Fx8zxg3Gh5a%2BgMOIDPOGVlsIcbhhiL67OEnOtLLdbC70VVfHRBr3mj%2FyeyQe8rKkOTEwjDW4fu8BjqkAZVXQuaIOG3e0g0Qpa4GOQ4%2BlbytTOruXuH7QQr3rbTfPTGHpWCgHhkTyM9cBJ%2FF4TjRMb0vFFMt30XWxasFnFUIKBtdBJmYisaWvguzyxDiedHr9BTC44RS6JNBJvagpXKtpwWQxQs43xCFvMSf8rKI5%2Bc%2BxV6vYN9tuWTS%2BXjmb4T7rYKaXc6s%2BcaxewXxWLyi7wGMq3AftThb9y%2Ftyp78LZ31&X-Amz-Signature=1e1c83fb79f784bd9f058f99fec1841e1bc8cf7d3e59156a1fc79eed6f414647&X-Amz-SignedHeaders=host&x-id=GetObject)

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
