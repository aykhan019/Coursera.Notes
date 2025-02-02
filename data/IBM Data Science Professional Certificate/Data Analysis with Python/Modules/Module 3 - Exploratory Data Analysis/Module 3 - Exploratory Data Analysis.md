

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDHBWMLC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpZPMGcBQc0jdTDCBbnNedYUZ5dUYK%2FXJnM1s8ZdpeJQIgbmhSF7OZdYeOIfBAZ79bcvzMG6EKpAw7ENwLs2w7Yv0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNGGvnzP3bFNQ85OSrcAwQmFgrEGp%2F9FcRfDkWg8vxxwohEvVDXRzm3qqWUnj7ZHlKUd6QNj7QNR9o%2FgcJrKO3Z7Cw0twFKBj2tovOzvYPyWHkuD5eyTSiKWIvNUz7B8mlvpfIh6KLP0N7LOFgL69YaRv%2FI7HdtwqmBI2eobyJbqnsVIJT6uexI4h7G7cjoZ3nPuC98HuU6nAdGN2ODSliU0l75QV7Mh9gUqW8yUlqujE86o%2BOGpYO63UXLvDGz2x7qH8pPWH6x729LeBys5klWJf8YUVEf4HeLvr6YldVapnAjTUD0an4Ov%2BGkKakXa7mUI38KluEcAWrUzmBDK4Nev3hAKcyqN1bu5UBNPkwFVwoBA73T5zTqM9gYBqsfnOdUtsgQ%2FkRBulGwtjY9WKT7On5I3%2BvaUeFS9I1zHf3V4qDVnpFhuH7RvklsG0X7JjmGs%2Fzc8UZVoP5nPVIIu44dZ94mNqQ8%2F8u4jQ2wTeQNqgOhFdXFC5kVGQ8NE7A1vhmFlqtCDxCoS%2Fg6%2FEn%2F3UKEVS7TG4vjsP%2B5yfy%2BxjmpVO%2F0BKri5iqTMilTyWG1HkKQX7kfFygI3QUu1DzswwECPTi3gM%2FpH5Hpvr7Ey7BFor9QhtR09p2i7BS2PjYhSZylyipx3GbE%2FC27MNib%2FLwGOqUBR%2BBXHTkOelKn%2FC%2Bhds2Oc844SGYPi%2BPLiNoxlh%2FM%2B6sjO2DvfpnwiqP8B4i96hiwnLK2t3SqxzkvHgf4mHypPb3bZYG5kmhubjWY03lvSNfD%2FDTP8tRt6841n4Q8SuPikQnONxmYhS8FACRRfwHMjLBGlfNMmmxKSLl9u5cuR4GGFVsISPa%2BczXm0UKWHnxfwBnf0CJQ7rOLaX%2FqKyhXn%2FYYNQAV&X-Amz-Signature=f29a65bf9719c7f1a518c3d0b1e3855b3ff664b2e9ea26befaedec15e2b3ec31&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDHBWMLC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpZPMGcBQc0jdTDCBbnNedYUZ5dUYK%2FXJnM1s8ZdpeJQIgbmhSF7OZdYeOIfBAZ79bcvzMG6EKpAw7ENwLs2w7Yv0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNGGvnzP3bFNQ85OSrcAwQmFgrEGp%2F9FcRfDkWg8vxxwohEvVDXRzm3qqWUnj7ZHlKUd6QNj7QNR9o%2FgcJrKO3Z7Cw0twFKBj2tovOzvYPyWHkuD5eyTSiKWIvNUz7B8mlvpfIh6KLP0N7LOFgL69YaRv%2FI7HdtwqmBI2eobyJbqnsVIJT6uexI4h7G7cjoZ3nPuC98HuU6nAdGN2ODSliU0l75QV7Mh9gUqW8yUlqujE86o%2BOGpYO63UXLvDGz2x7qH8pPWH6x729LeBys5klWJf8YUVEf4HeLvr6YldVapnAjTUD0an4Ov%2BGkKakXa7mUI38KluEcAWrUzmBDK4Nev3hAKcyqN1bu5UBNPkwFVwoBA73T5zTqM9gYBqsfnOdUtsgQ%2FkRBulGwtjY9WKT7On5I3%2BvaUeFS9I1zHf3V4qDVnpFhuH7RvklsG0X7JjmGs%2Fzc8UZVoP5nPVIIu44dZ94mNqQ8%2F8u4jQ2wTeQNqgOhFdXFC5kVGQ8NE7A1vhmFlqtCDxCoS%2Fg6%2FEn%2F3UKEVS7TG4vjsP%2B5yfy%2BxjmpVO%2F0BKri5iqTMilTyWG1HkKQX7kfFygI3QUu1DzswwECPTi3gM%2FpH5Hpvr7Ey7BFor9QhtR09p2i7BS2PjYhSZylyipx3GbE%2FC27MNib%2FLwGOqUBR%2BBXHTkOelKn%2FC%2Bhds2Oc844SGYPi%2BPLiNoxlh%2FM%2B6sjO2DvfpnwiqP8B4i96hiwnLK2t3SqxzkvHgf4mHypPb3bZYG5kmhubjWY03lvSNfD%2FDTP8tRt6841n4Q8SuPikQnONxmYhS8FACRRfwHMjLBGlfNMmmxKSLl9u5cuR4GGFVsISPa%2BczXm0UKWHnxfwBnf0CJQ7rOLaX%2FqKyhXn%2FYYNQAV&X-Amz-Signature=cb00e2254ad85b7c8620287cda1bd8667a39b59a62ff2424b14405633a6b2f06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDHBWMLC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpZPMGcBQc0jdTDCBbnNedYUZ5dUYK%2FXJnM1s8ZdpeJQIgbmhSF7OZdYeOIfBAZ79bcvzMG6EKpAw7ENwLs2w7Yv0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNGGvnzP3bFNQ85OSrcAwQmFgrEGp%2F9FcRfDkWg8vxxwohEvVDXRzm3qqWUnj7ZHlKUd6QNj7QNR9o%2FgcJrKO3Z7Cw0twFKBj2tovOzvYPyWHkuD5eyTSiKWIvNUz7B8mlvpfIh6KLP0N7LOFgL69YaRv%2FI7HdtwqmBI2eobyJbqnsVIJT6uexI4h7G7cjoZ3nPuC98HuU6nAdGN2ODSliU0l75QV7Mh9gUqW8yUlqujE86o%2BOGpYO63UXLvDGz2x7qH8pPWH6x729LeBys5klWJf8YUVEf4HeLvr6YldVapnAjTUD0an4Ov%2BGkKakXa7mUI38KluEcAWrUzmBDK4Nev3hAKcyqN1bu5UBNPkwFVwoBA73T5zTqM9gYBqsfnOdUtsgQ%2FkRBulGwtjY9WKT7On5I3%2BvaUeFS9I1zHf3V4qDVnpFhuH7RvklsG0X7JjmGs%2Fzc8UZVoP5nPVIIu44dZ94mNqQ8%2F8u4jQ2wTeQNqgOhFdXFC5kVGQ8NE7A1vhmFlqtCDxCoS%2Fg6%2FEn%2F3UKEVS7TG4vjsP%2B5yfy%2BxjmpVO%2F0BKri5iqTMilTyWG1HkKQX7kfFygI3QUu1DzswwECPTi3gM%2FpH5Hpvr7Ey7BFor9QhtR09p2i7BS2PjYhSZylyipx3GbE%2FC27MNib%2FLwGOqUBR%2BBXHTkOelKn%2FC%2Bhds2Oc844SGYPi%2BPLiNoxlh%2FM%2B6sjO2DvfpnwiqP8B4i96hiwnLK2t3SqxzkvHgf4mHypPb3bZYG5kmhubjWY03lvSNfD%2FDTP8tRt6841n4Q8SuPikQnONxmYhS8FACRRfwHMjLBGlfNMmmxKSLl9u5cuR4GGFVsISPa%2BczXm0UKWHnxfwBnf0CJQ7rOLaX%2FqKyhXn%2FYYNQAV&X-Amz-Signature=4089afbfb79ef011f0267790cd6b5abd82fa2b1eb01520dc8d44ff12704af051&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC5Z5CMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr9Xt66m5lCtnhw8JDROdSMtQIm5Q9n6AWPMaSEadiKwIgLc4LUd%2F9dI9KnK%2BKoKpJoYG0rC1tQQmoArhiE5m2o%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEOC2tZ%2FTMG0uRTCyrcA9KuGpAJNSYxeYOE6rcVi2mBcOQiwe2AooeZZqaflLrOkyLjdfKEKmEPuT1Os3NmxQDt3XzwTq3gZUgGn%2FHmziSYD87%2Bp9gR9pvlE3mwCykj6yVUIINZIj0UFFzELS8vXr0TGby6g%2FuZdukSsNoXFqnFPCRqeCXt%2B%2BoOG0ebDvFwrO846vAUkww%2Bcdw8GKPh8lw9RJxv9cbC4HaDR8yXu28yS71D81xK5Er%2FzOj1Dvd%2FpPGORIKHy%2BgdQRGn9q8C2LGrZEjbNV0MeKj8IbR88uWmR%2Fox015sjpK6tW6F9uWL1yZTvwMVF8pc9Oucb6uadIo%2Ba%2FjwgDJCOaPKuczhE4QHknZjx3jRh5lIorBHBK7I1xW9ic2q%2BffZsOh%2FdF7mM%2BJ4tV%2B3XOiZA6NQ%2B%2F7NhnyIgY4duLvmaPhMVJeVT8viCM8UqsCZxhB37QY7sKzR82no1Dbn9JPteGLd0GY9JM6r%2FPei5CdMD0YnQuQ%2Fh7MpDXgD2aAWJFM4QC9is6SEI2%2FxRsi9G2UAUOC1lKXlEHF737HQq6maRvgPNv3fYCvFqNuiGDVlvtNd4ZB8Ulhfl3ijrNNMDV9BMX2TA9ohMb6vv4kWTJbfPsmTEiifMVtcvSms9xxbzo4orm0HMNyb%2FLwGOqUBLVdd%2FEUy7tHg7ZhUDx6XpOGzpM5WFyVrZk%2FJghhttzVj3Q9YxQlZ4duz9v7q%2FOuXdb4BXt19mTelCMxzH1FY37P355klTlWeto%2BLIDSeMdqUTXf2Ig22wviPcUqBt8iQWKFNOlrABfdv9ZUFfyNqXIBr5eJXmmBeX5HAARtoIx6HACVmFM9hXAgoZMuXIjc1GYaZeOBXlIJa8kAwcpdnhgRnmAZi&X-Amz-Signature=ccf80a10e9e9e9fd3aeef5d5799402bb5a69cf9a96faefe9b3f94e21880f7aa4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC5Z5CMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr9Xt66m5lCtnhw8JDROdSMtQIm5Q9n6AWPMaSEadiKwIgLc4LUd%2F9dI9KnK%2BKoKpJoYG0rC1tQQmoArhiE5m2o%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEOC2tZ%2FTMG0uRTCyrcA9KuGpAJNSYxeYOE6rcVi2mBcOQiwe2AooeZZqaflLrOkyLjdfKEKmEPuT1Os3NmxQDt3XzwTq3gZUgGn%2FHmziSYD87%2Bp9gR9pvlE3mwCykj6yVUIINZIj0UFFzELS8vXr0TGby6g%2FuZdukSsNoXFqnFPCRqeCXt%2B%2BoOG0ebDvFwrO846vAUkww%2Bcdw8GKPh8lw9RJxv9cbC4HaDR8yXu28yS71D81xK5Er%2FzOj1Dvd%2FpPGORIKHy%2BgdQRGn9q8C2LGrZEjbNV0MeKj8IbR88uWmR%2Fox015sjpK6tW6F9uWL1yZTvwMVF8pc9Oucb6uadIo%2Ba%2FjwgDJCOaPKuczhE4QHknZjx3jRh5lIorBHBK7I1xW9ic2q%2BffZsOh%2FdF7mM%2BJ4tV%2B3XOiZA6NQ%2B%2F7NhnyIgY4duLvmaPhMVJeVT8viCM8UqsCZxhB37QY7sKzR82no1Dbn9JPteGLd0GY9JM6r%2FPei5CdMD0YnQuQ%2Fh7MpDXgD2aAWJFM4QC9is6SEI2%2FxRsi9G2UAUOC1lKXlEHF737HQq6maRvgPNv3fYCvFqNuiGDVlvtNd4ZB8Ulhfl3ijrNNMDV9BMX2TA9ohMb6vv4kWTJbfPsmTEiifMVtcvSms9xxbzo4orm0HMNyb%2FLwGOqUBLVdd%2FEUy7tHg7ZhUDx6XpOGzpM5WFyVrZk%2FJghhttzVj3Q9YxQlZ4duz9v7q%2FOuXdb4BXt19mTelCMxzH1FY37P355klTlWeto%2BLIDSeMdqUTXf2Ig22wviPcUqBt8iQWKFNOlrABfdv9ZUFfyNqXIBr5eJXmmBeX5HAARtoIx6HACVmFM9hXAgoZMuXIjc1GYaZeOBXlIJa8kAwcpdnhgRnmAZi&X-Amz-Signature=ce8f0e79083b0000ed41e6ce3c3e74e1da2124bdc3fbddbce1dbb00264e8d79c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC5Z5CMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr9Xt66m5lCtnhw8JDROdSMtQIm5Q9n6AWPMaSEadiKwIgLc4LUd%2F9dI9KnK%2BKoKpJoYG0rC1tQQmoArhiE5m2o%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEOC2tZ%2FTMG0uRTCyrcA9KuGpAJNSYxeYOE6rcVi2mBcOQiwe2AooeZZqaflLrOkyLjdfKEKmEPuT1Os3NmxQDt3XzwTq3gZUgGn%2FHmziSYD87%2Bp9gR9pvlE3mwCykj6yVUIINZIj0UFFzELS8vXr0TGby6g%2FuZdukSsNoXFqnFPCRqeCXt%2B%2BoOG0ebDvFwrO846vAUkww%2Bcdw8GKPh8lw9RJxv9cbC4HaDR8yXu28yS71D81xK5Er%2FzOj1Dvd%2FpPGORIKHy%2BgdQRGn9q8C2LGrZEjbNV0MeKj8IbR88uWmR%2Fox015sjpK6tW6F9uWL1yZTvwMVF8pc9Oucb6uadIo%2Ba%2FjwgDJCOaPKuczhE4QHknZjx3jRh5lIorBHBK7I1xW9ic2q%2BffZsOh%2FdF7mM%2BJ4tV%2B3XOiZA6NQ%2B%2F7NhnyIgY4duLvmaPhMVJeVT8viCM8UqsCZxhB37QY7sKzR82no1Dbn9JPteGLd0GY9JM6r%2FPei5CdMD0YnQuQ%2Fh7MpDXgD2aAWJFM4QC9is6SEI2%2FxRsi9G2UAUOC1lKXlEHF737HQq6maRvgPNv3fYCvFqNuiGDVlvtNd4ZB8Ulhfl3ijrNNMDV9BMX2TA9ohMb6vv4kWTJbfPsmTEiifMVtcvSms9xxbzo4orm0HMNyb%2FLwGOqUBLVdd%2FEUy7tHg7ZhUDx6XpOGzpM5WFyVrZk%2FJghhttzVj3Q9YxQlZ4duz9v7q%2FOuXdb4BXt19mTelCMxzH1FY37P355klTlWeto%2BLIDSeMdqUTXf2Ig22wviPcUqBt8iQWKFNOlrABfdv9ZUFfyNqXIBr5eJXmmBeX5HAARtoIx6HACVmFM9hXAgoZMuXIjc1GYaZeOBXlIJa8kAwcpdnhgRnmAZi&X-Amz-Signature=2e9523a3159bff54c867e815e6f8f2c1274dcd285f22110cc325e1c34a8638ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC5Z5CMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr9Xt66m5lCtnhw8JDROdSMtQIm5Q9n6AWPMaSEadiKwIgLc4LUd%2F9dI9KnK%2BKoKpJoYG0rC1tQQmoArhiE5m2o%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEOC2tZ%2FTMG0uRTCyrcA9KuGpAJNSYxeYOE6rcVi2mBcOQiwe2AooeZZqaflLrOkyLjdfKEKmEPuT1Os3NmxQDt3XzwTq3gZUgGn%2FHmziSYD87%2Bp9gR9pvlE3mwCykj6yVUIINZIj0UFFzELS8vXr0TGby6g%2FuZdukSsNoXFqnFPCRqeCXt%2B%2BoOG0ebDvFwrO846vAUkww%2Bcdw8GKPh8lw9RJxv9cbC4HaDR8yXu28yS71D81xK5Er%2FzOj1Dvd%2FpPGORIKHy%2BgdQRGn9q8C2LGrZEjbNV0MeKj8IbR88uWmR%2Fox015sjpK6tW6F9uWL1yZTvwMVF8pc9Oucb6uadIo%2Ba%2FjwgDJCOaPKuczhE4QHknZjx3jRh5lIorBHBK7I1xW9ic2q%2BffZsOh%2FdF7mM%2BJ4tV%2B3XOiZA6NQ%2B%2F7NhnyIgY4duLvmaPhMVJeVT8viCM8UqsCZxhB37QY7sKzR82no1Dbn9JPteGLd0GY9JM6r%2FPei5CdMD0YnQuQ%2Fh7MpDXgD2aAWJFM4QC9is6SEI2%2FxRsi9G2UAUOC1lKXlEHF737HQq6maRvgPNv3fYCvFqNuiGDVlvtNd4ZB8Ulhfl3ijrNNMDV9BMX2TA9ohMb6vv4kWTJbfPsmTEiifMVtcvSms9xxbzo4orm0HMNyb%2FLwGOqUBLVdd%2FEUy7tHg7ZhUDx6XpOGzpM5WFyVrZk%2FJghhttzVj3Q9YxQlZ4duz9v7q%2FOuXdb4BXt19mTelCMxzH1FY37P355klTlWeto%2BLIDSeMdqUTXf2Ig22wviPcUqBt8iQWKFNOlrABfdv9ZUFfyNqXIBr5eJXmmBeX5HAARtoIx6HACVmFM9hXAgoZMuXIjc1GYaZeOBXlIJa8kAwcpdnhgRnmAZi&X-Amz-Signature=e9e18dbfd69350a228c090d1fd31491aa0d62f9dbbbac4311b235e7ccd81b31a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC5Z5CMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr9Xt66m5lCtnhw8JDROdSMtQIm5Q9n6AWPMaSEadiKwIgLc4LUd%2F9dI9KnK%2BKoKpJoYG0rC1tQQmoArhiE5m2o%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEOC2tZ%2FTMG0uRTCyrcA9KuGpAJNSYxeYOE6rcVi2mBcOQiwe2AooeZZqaflLrOkyLjdfKEKmEPuT1Os3NmxQDt3XzwTq3gZUgGn%2FHmziSYD87%2Bp9gR9pvlE3mwCykj6yVUIINZIj0UFFzELS8vXr0TGby6g%2FuZdukSsNoXFqnFPCRqeCXt%2B%2BoOG0ebDvFwrO846vAUkww%2Bcdw8GKPh8lw9RJxv9cbC4HaDR8yXu28yS71D81xK5Er%2FzOj1Dvd%2FpPGORIKHy%2BgdQRGn9q8C2LGrZEjbNV0MeKj8IbR88uWmR%2Fox015sjpK6tW6F9uWL1yZTvwMVF8pc9Oucb6uadIo%2Ba%2FjwgDJCOaPKuczhE4QHknZjx3jRh5lIorBHBK7I1xW9ic2q%2BffZsOh%2FdF7mM%2BJ4tV%2B3XOiZA6NQ%2B%2F7NhnyIgY4duLvmaPhMVJeVT8viCM8UqsCZxhB37QY7sKzR82no1Dbn9JPteGLd0GY9JM6r%2FPei5CdMD0YnQuQ%2Fh7MpDXgD2aAWJFM4QC9is6SEI2%2FxRsi9G2UAUOC1lKXlEHF737HQq6maRvgPNv3fYCvFqNuiGDVlvtNd4ZB8Ulhfl3ijrNNMDV9BMX2TA9ohMb6vv4kWTJbfPsmTEiifMVtcvSms9xxbzo4orm0HMNyb%2FLwGOqUBLVdd%2FEUy7tHg7ZhUDx6XpOGzpM5WFyVrZk%2FJghhttzVj3Q9YxQlZ4duz9v7q%2FOuXdb4BXt19mTelCMxzH1FY37P355klTlWeto%2BLIDSeMdqUTXf2Ig22wviPcUqBt8iQWKFNOlrABfdv9ZUFfyNqXIBr5eJXmmBeX5HAARtoIx6HACVmFM9hXAgoZMuXIjc1GYaZeOBXlIJa8kAwcpdnhgRnmAZi&X-Amz-Signature=8ed2601ce29903efb45fb764721ae4b8598e8a79dc1ae58ddd4a01bb4402466d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC5Z5CMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr9Xt66m5lCtnhw8JDROdSMtQIm5Q9n6AWPMaSEadiKwIgLc4LUd%2F9dI9KnK%2BKoKpJoYG0rC1tQQmoArhiE5m2o%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEOC2tZ%2FTMG0uRTCyrcA9KuGpAJNSYxeYOE6rcVi2mBcOQiwe2AooeZZqaflLrOkyLjdfKEKmEPuT1Os3NmxQDt3XzwTq3gZUgGn%2FHmziSYD87%2Bp9gR9pvlE3mwCykj6yVUIINZIj0UFFzELS8vXr0TGby6g%2FuZdukSsNoXFqnFPCRqeCXt%2B%2BoOG0ebDvFwrO846vAUkww%2Bcdw8GKPh8lw9RJxv9cbC4HaDR8yXu28yS71D81xK5Er%2FzOj1Dvd%2FpPGORIKHy%2BgdQRGn9q8C2LGrZEjbNV0MeKj8IbR88uWmR%2Fox015sjpK6tW6F9uWL1yZTvwMVF8pc9Oucb6uadIo%2Ba%2FjwgDJCOaPKuczhE4QHknZjx3jRh5lIorBHBK7I1xW9ic2q%2BffZsOh%2FdF7mM%2BJ4tV%2B3XOiZA6NQ%2B%2F7NhnyIgY4duLvmaPhMVJeVT8viCM8UqsCZxhB37QY7sKzR82no1Dbn9JPteGLd0GY9JM6r%2FPei5CdMD0YnQuQ%2Fh7MpDXgD2aAWJFM4QC9is6SEI2%2FxRsi9G2UAUOC1lKXlEHF737HQq6maRvgPNv3fYCvFqNuiGDVlvtNd4ZB8Ulhfl3ijrNNMDV9BMX2TA9ohMb6vv4kWTJbfPsmTEiifMVtcvSms9xxbzo4orm0HMNyb%2FLwGOqUBLVdd%2FEUy7tHg7ZhUDx6XpOGzpM5WFyVrZk%2FJghhttzVj3Q9YxQlZ4duz9v7q%2FOuXdb4BXt19mTelCMxzH1FY37P355klTlWeto%2BLIDSeMdqUTXf2Ig22wviPcUqBt8iQWKFNOlrABfdv9ZUFfyNqXIBr5eJXmmBeX5HAARtoIx6HACVmFM9hXAgoZMuXIjc1GYaZeOBXlIJa8kAwcpdnhgRnmAZi&X-Amz-Signature=1683520a5c9d007ebdfa6f8d5fa208e0b55806143d604761947d3547bb4da849&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZSFGPAJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx870eyG8GSNJCGJ2WoEgGFcA723bYbT2FcKCTPaBh5wIhALyfdgY2E9k5m9Ayv%2FpcWxeYuN0%2BaSUxcXDOSm36GOmeKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8q3BZYAMipXn6faQq3APvaHqNj%2Bq3ysFOViESRnva%2BqH9GWqhiQiQLWzQaA3r7htQPvYvjaEqhF1om8cCk7aIYWmuJ6KKA%2BjIJJPCnaSqNYk6PBfpgpeNn2oTEb4TW%2FNZOh8Mlf9iwI5EDzSy4EoYiPyvXMzMniyCk9ax%2Ffss1sCrn%2BF%2FRlk1UB30k8HTPLbq1yGq5ImX6RXKx7%2FiW53rSbv87BO4%2Flwsv4SvmvxiM2XIFLkxuvIh%2FIJhr5OW0Kj1INYDxcfebWYnlxRgoDqkZeC0lKUdWSe4hW4DALbaBvVJU%2BKUz7jW3mO5d6LzRcBNHu5Yk%2B4stWUGtenrVmxoZsf1RIw6JxiUExAxTKt5bs5FdwyTJUHwDsiL7vI1AihT5MyH%2Fgz4ZZF5WceitPc08jHwOIl9kXss2JOJQjK1Ux6SMqx6E5hK2ct2aGiSz1wJTbyqpeonP0DfwPTKiT9S3EAIL6mMN%2FqqnH%2Fdbtt9o8qqsa4%2FVzP%2FwCCPoI0MMOPuD0cZ7L9iewfczOuKDtJ058wPQ7T%2BLuaz8kbnd4nZbC6k%2BL2unBxcxOVL4ggcWUAWoOnyWn%2F4rv1hA7HaqVc2ywtJwFs7q%2FfR%2BY6F5i85R0mQdL3FDFhDtNROEUP%2FpaKi0r%2Fo0PxC5%2B9FMzDbm%2Fy8BjqkAS4%2BPuw%2F5%2BussIeSFNjWDIEmWLnbkNN2lsHFWUzC8yxRdN2fgHXWEe60GyYEKMub2mclGKYQh%2B5hgc2Jped9Rh54JpJUS0Y%2F2bZw70pAcb19GSSz4IsRKloQAsqvdbtblOBuUrPibUT86646ZcO3xLTp6l%2FoPQHuD%2FuFgz2PGcSFjIogJHdOQ85ddyUpz%2FVjusSM6jYM8cY7bPd8TRG%2BTDfu0fnX&X-Amz-Signature=5a55711489123a4ce6ccd88a9d29dd07dabc9ed9dd93eae650ff7c2a6f71267a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI6NOVJO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCkMKuqaGXdSO6MlaDjVvSYyNmAMzohPR0WnN4wo3QIqgIgaUbE9mmPDGr5%2F8CUYx3GR1Kkel5RDNePIg5PE0BWRa0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA2eANGLtRgHb1a5kSrcA8rEAx4BDFtPiXz2OC4puOYZ%2FUprZAxBRRT6OdDojamJy%2BzbCCEw1OEaTVHpR2hO4l%2FFxy9rGfEkR7%2FN9l6nZc43srcQokJJDPs9DR7KyiJrEi4BToUD7VRgGgcKRsEc5ygOQcHCyWqS0qDnw3uRDV8gvAztx08G11Oz1LGl6LE8bWfoTpMNrru9IeAK%2FseMl23NgT%2BQLAqMtArNHA%2BYxqCShNMTfVuz4uXxtEnIvHQ82LtZ6DcmkoP5MSj4sYXpdL0ZclGOhL34EqBf%2B%2Fpw9ENMw4tufV%2BIXmNXkPMQpGTlV%2FG9blnif0tNhO0uHc2IC1rfMXvceHUpjNXiyVSLB2pjEn7JSUXx%2F8ShmC0uHoZfqWB0Jw2cplSA4z5CwTtkySOmBqFYcGPyJJInoo4B9mQcOUjDADdZ%2Bf86GwV3GF1jVvH2yaN%2FLpQlcehppN7buqRZZD2eG4r1sfFiLDTx1jyjtGU0mSfKKIhAF3%2FyPqp3GJByAn%2B1CVKsnpd86PnjaRlZL7LqWYspW3TOYLXQaPS9LJtUy3y36r4m1aQYKKUaxyktpuRn42dcTy7M3ZXWg9Cn%2FO7VnnoppQ1AKFjqhW1BeOoxrgeEny%2FYJIXH08cgp5aIpdWlT4ev75eSMJac%2FLwGOqUB5yYrA9UsTe1ihkYcPGqDteNDAU07UR169Y7jGHDvNkDmA5I2tpzN8XU0pgeS2zDc%2B5CdTmMRTeS8212fDgQYf7KGEVo4A8nKWXDZ%2Fh1IkXxSRd%2FZnSIdI0pQ0V78frWXY8hbmamqSq%2F51SZffxKsSzYszL%2BWiQSQDKUE4o6yQEcEcvz5oqsxq5udiRPgsKLArMfnpr4ieKV6ppz0geZ09ghpgVTs&X-Amz-Signature=adbd32dca7bac6bb1ddb454b23a54e7d4696d01337fa882c1d6ee262de53e6ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC5Z5CMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr9Xt66m5lCtnhw8JDROdSMtQIm5Q9n6AWPMaSEadiKwIgLc4LUd%2F9dI9KnK%2BKoKpJoYG0rC1tQQmoArhiE5m2o%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEOC2tZ%2FTMG0uRTCyrcA9KuGpAJNSYxeYOE6rcVi2mBcOQiwe2AooeZZqaflLrOkyLjdfKEKmEPuT1Os3NmxQDt3XzwTq3gZUgGn%2FHmziSYD87%2Bp9gR9pvlE3mwCykj6yVUIINZIj0UFFzELS8vXr0TGby6g%2FuZdukSsNoXFqnFPCRqeCXt%2B%2BoOG0ebDvFwrO846vAUkww%2Bcdw8GKPh8lw9RJxv9cbC4HaDR8yXu28yS71D81xK5Er%2FzOj1Dvd%2FpPGORIKHy%2BgdQRGn9q8C2LGrZEjbNV0MeKj8IbR88uWmR%2Fox015sjpK6tW6F9uWL1yZTvwMVF8pc9Oucb6uadIo%2Ba%2FjwgDJCOaPKuczhE4QHknZjx3jRh5lIorBHBK7I1xW9ic2q%2BffZsOh%2FdF7mM%2BJ4tV%2B3XOiZA6NQ%2B%2F7NhnyIgY4duLvmaPhMVJeVT8viCM8UqsCZxhB37QY7sKzR82no1Dbn9JPteGLd0GY9JM6r%2FPei5CdMD0YnQuQ%2Fh7MpDXgD2aAWJFM4QC9is6SEI2%2FxRsi9G2UAUOC1lKXlEHF737HQq6maRvgPNv3fYCvFqNuiGDVlvtNd4ZB8Ulhfl3ijrNNMDV9BMX2TA9ohMb6vv4kWTJbfPsmTEiifMVtcvSms9xxbzo4orm0HMNyb%2FLwGOqUBLVdd%2FEUy7tHg7ZhUDx6XpOGzpM5WFyVrZk%2FJghhttzVj3Q9YxQlZ4duz9v7q%2FOuXdb4BXt19mTelCMxzH1FY37P355klTlWeto%2BLIDSeMdqUTXf2Ig22wviPcUqBt8iQWKFNOlrABfdv9ZUFfyNqXIBr5eJXmmBeX5HAARtoIx6HACVmFM9hXAgoZMuXIjc1GYaZeOBXlIJa8kAwcpdnhgRnmAZi&X-Amz-Signature=a0e64c43aeabe776106fec6f36b1f8ed7e961e604ed93799b7e9f7e35c6dc3af&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC5Z5CMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr9Xt66m5lCtnhw8JDROdSMtQIm5Q9n6AWPMaSEadiKwIgLc4LUd%2F9dI9KnK%2BKoKpJoYG0rC1tQQmoArhiE5m2o%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEOC2tZ%2FTMG0uRTCyrcA9KuGpAJNSYxeYOE6rcVi2mBcOQiwe2AooeZZqaflLrOkyLjdfKEKmEPuT1Os3NmxQDt3XzwTq3gZUgGn%2FHmziSYD87%2Bp9gR9pvlE3mwCykj6yVUIINZIj0UFFzELS8vXr0TGby6g%2FuZdukSsNoXFqnFPCRqeCXt%2B%2BoOG0ebDvFwrO846vAUkww%2Bcdw8GKPh8lw9RJxv9cbC4HaDR8yXu28yS71D81xK5Er%2FzOj1Dvd%2FpPGORIKHy%2BgdQRGn9q8C2LGrZEjbNV0MeKj8IbR88uWmR%2Fox015sjpK6tW6F9uWL1yZTvwMVF8pc9Oucb6uadIo%2Ba%2FjwgDJCOaPKuczhE4QHknZjx3jRh5lIorBHBK7I1xW9ic2q%2BffZsOh%2FdF7mM%2BJ4tV%2B3XOiZA6NQ%2B%2F7NhnyIgY4duLvmaPhMVJeVT8viCM8UqsCZxhB37QY7sKzR82no1Dbn9JPteGLd0GY9JM6r%2FPei5CdMD0YnQuQ%2Fh7MpDXgD2aAWJFM4QC9is6SEI2%2FxRsi9G2UAUOC1lKXlEHF737HQq6maRvgPNv3fYCvFqNuiGDVlvtNd4ZB8Ulhfl3ijrNNMDV9BMX2TA9ohMb6vv4kWTJbfPsmTEiifMVtcvSms9xxbzo4orm0HMNyb%2FLwGOqUBLVdd%2FEUy7tHg7ZhUDx6XpOGzpM5WFyVrZk%2FJghhttzVj3Q9YxQlZ4duz9v7q%2FOuXdb4BXt19mTelCMxzH1FY37P355klTlWeto%2BLIDSeMdqUTXf2Ig22wviPcUqBt8iQWKFNOlrABfdv9ZUFfyNqXIBr5eJXmmBeX5HAARtoIx6HACVmFM9hXAgoZMuXIjc1GYaZeOBXlIJa8kAwcpdnhgRnmAZi&X-Amz-Signature=14b768d8c4b6be7dee76e267e099d19e02b6d3520f7b4d0a951b952a8ccdf7f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC5Z5CMJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDr9Xt66m5lCtnhw8JDROdSMtQIm5Q9n6AWPMaSEadiKwIgLc4LUd%2F9dI9KnK%2BKoKpJoYG0rC1tQQmoArhiE5m2o%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEOC2tZ%2FTMG0uRTCyrcA9KuGpAJNSYxeYOE6rcVi2mBcOQiwe2AooeZZqaflLrOkyLjdfKEKmEPuT1Os3NmxQDt3XzwTq3gZUgGn%2FHmziSYD87%2Bp9gR9pvlE3mwCykj6yVUIINZIj0UFFzELS8vXr0TGby6g%2FuZdukSsNoXFqnFPCRqeCXt%2B%2BoOG0ebDvFwrO846vAUkww%2Bcdw8GKPh8lw9RJxv9cbC4HaDR8yXu28yS71D81xK5Er%2FzOj1Dvd%2FpPGORIKHy%2BgdQRGn9q8C2LGrZEjbNV0MeKj8IbR88uWmR%2Fox015sjpK6tW6F9uWL1yZTvwMVF8pc9Oucb6uadIo%2Ba%2FjwgDJCOaPKuczhE4QHknZjx3jRh5lIorBHBK7I1xW9ic2q%2BffZsOh%2FdF7mM%2BJ4tV%2B3XOiZA6NQ%2B%2F7NhnyIgY4duLvmaPhMVJeVT8viCM8UqsCZxhB37QY7sKzR82no1Dbn9JPteGLd0GY9JM6r%2FPei5CdMD0YnQuQ%2Fh7MpDXgD2aAWJFM4QC9is6SEI2%2FxRsi9G2UAUOC1lKXlEHF737HQq6maRvgPNv3fYCvFqNuiGDVlvtNd4ZB8Ulhfl3ijrNNMDV9BMX2TA9ohMb6vv4kWTJbfPsmTEiifMVtcvSms9xxbzo4orm0HMNyb%2FLwGOqUBLVdd%2FEUy7tHg7ZhUDx6XpOGzpM5WFyVrZk%2FJghhttzVj3Q9YxQlZ4duz9v7q%2FOuXdb4BXt19mTelCMxzH1FY37P355klTlWeto%2BLIDSeMdqUTXf2Ig22wviPcUqBt8iQWKFNOlrABfdv9ZUFfyNqXIBr5eJXmmBeX5HAARtoIx6HACVmFM9hXAgoZMuXIjc1GYaZeOBXlIJa8kAwcpdnhgRnmAZi&X-Amz-Signature=6df075cb4ee931b8392efde27f61d8a6162330b6d9d443e14d3c0099dbe64c7a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FMIQKCH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqwyKYUprNgiVsefR239TtHXLikrNMqses1SN0%2BIs3wQIgY2iX6KfdluFtT8c5ttnk3%2BiAs%2FdD6T%2BiL7b6eUx9WZsqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNfzXTllC1%2FI1BJcsircA8YP%2BTRJTqRKZMVpjcR7V1k9mPyfRlO8NT1ylb13jLj3iWxKoIGbeQ6lLBw0cwqCoL2z%2FkIuSt%2FdA0Z9OON%2BhpzlP4lW6h29JWn4IDRuiYTiAkQdku3guEUZIIozerDxVy5WcM%2B4wFZ1rO6qU0PWqYo0%2F1QEnMJfwBcxkCqBFl57RjG9W%2F65OJXWWAlHAlswBcV9yu07toALToLASZ39Ms9YT25WKieTIgNuMTi%2F6mytOfNgXzNynfHryhHWi40lSCoFspTtN4o7fSLK3LPs6CUmoFmEjnLRHCnCOlPdHnLrI4qZ8qTAagjtasaEn3DQHL%2FTGKRt804o3T%2BkMYe4XLv7%2FrKuix87A4Afa%2BpCAaBziutSdTESg2qVJgjgXpitHknJvtoqMdhShdS0fb32gsNGVA3DO7C6ZlRKzBsK1uH4ZJC5T3klU8jjxAZ%2FsUYy0sDea4ZNz1ueQ3DVT048VQqhYVG7cByA6m%2Brckx2SLDbOrp%2FeBcI6nHaBQxhLGwJhSEmhBErorJkqInES9eWLWj%2FpfHLSHSeZ7a49VOHX2bCus9pLiVWKBcDDk4LHZTyFwnuYWXB9ZtkPq5nL66UppWyB5ZgLLX0QyrETFRxuraXC46SDAYjy9KiNQYrMOSb%2FLwGOqUBXJJB7sTccFHLCVCY36pBNIyWb2L20ZklA%2FGuUPTN9VkrT6j7%2FYsWbZeaHBbHHw0TiMub29MGFTdPxfe0sD0HZP6N9Sf65p7EsE70mGNR8qZBrhsj%2FxqDCj%2FAyigpMfOss2FRS%2FoQTa5shYL76SXP0i9NRamvTdb2ODHIygnKwmzSa7jg%2BsTN0RK8QlJ0hZfnAb0Ct0GmytbTmE27N2xeBMll5r2s&X-Amz-Signature=02310960c84ef275d39d9f33b452b1061f31379e7a0f075bbb06237bb81c5a04&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZULLITPS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD33v72I632CAGvLPXwFsnkib1fbbvvtf7aemKfufQvogIgZ3%2BTxbDKWNFHvhUwMfTLamG%2F3yqq974wzQw1nIzw358qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK8zLXnsn4%2FW%2BXyNjircAxGuy6ZuCYNMYcRQEjtYK%2F91az2GjS1rLdv74kTT8fEC5d%2BZG8Xz54gT2rCgvaEqKf4A38dhRmbhQCC%2BKEupucuBA4Ofbxkdq7sRawbVb%2Bkh9bgmKr9UcR4WcI0VjAxPwfm3rCqGrPuHh4VlTW%2BDQW5KV5Si44ll4q%2BcBgTep05e4ltfRtjxLZYSSm4CZlRk1%2FSoIxjNOLi28kHrYvQjWgEQyxEBcrA%2FmFU2nXtrj84HBdQyIUj%2Bx8r6HmT%2BJ2O5fZIqTEJO0nmw7gWZ5TXkktAK4KKJ7VMwPOQC2QLSeGsIE0PpcUBfLbbt%2B02Lb%2FSnEyUOnBH0cc8dhP%2BTriz%2B25vKs2jalgNu1lDkHOr2UF7HLAvyMQpUPq%2Fohn6rUeokza2Z1VZJ2ZKYCzRtdHvsVCnCWtaeGF0j6pAqWRjXrzWwfLIUZtO3lQCpBd%2F5x2hLpc2Uis5PD5%2BewQZKnql1bBxerIwbV%2BYQIzbJsX47BDNdmwY3LDClBrDx4yhAlkBJb57Hj7p1i7QCriPrPrpjGKgkQH2rZYSniAs7n%2BPZJmqO1OU6Trj%2Fx7k3bxRb4cj%2Fc%2BM%2BRacoYeBlEWZBqdy9olm%2FeQqbOUHiwMq3ItLMlvGFFZuhOQtrMPC%2F9qmCMLCc%2FLwGOqUBLwlg3FrNH8GfZVX%2B%2B9o%2BODT3Pgw0Czi7D7w05A6JqNI4lLrYfQeKKk%2FUUli%2BhtnA2o86fjYNCmG7LE2%2FKmgcAIG6CdXriA1CThwbgRVua7uelzquB9OSRvXiLdfqgFmncQMQi%2F4dQxheFSyiX%2BdUnz3hVtBdCDAo%2FV%2BqYu8zvB56a6fayyXr1e0mkwl45SVo4a8eDpnBj3AtgKTbNZdt8lqZicL8&X-Amz-Signature=2ec61b51de16d2fc29e25393f88d9ff16691b74860b94e511d927b39463f5c18&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKORICMY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICoj8t%2Ft0Sxf%2F9%2Fi9eSvtPHOPEIr%2BcaU1mndkWCLQwpvAiEAg99m1r0WTeNUmh%2F9EW5xKOpbR5LMngeD%2FXJm99Vr0foqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE210n8FkcI4O7nt%2BircA%2BGvqAt%2FNdAjLt%2BUX4bqrby9EXmH8WvvENJqln7eKgT0kwvABU7h7jECFGsS0anV0%2FaxGcwGxvMDJESc1avNQYWJlM8ExTFvOAaCXYgvNaN6tvl5SEruPkGIyX6n5v7Ak7NWfOwt%2FBAwOdBbxnifIVkDz5SNWbgcwdncdaMWDfYaE5vr5cgFUjWVaRZGYAgUgxSh3qKn8Lm1b1hKerBISu%2BXC1hWYzeWrL50xENv5N%2Bc9Lm6Dj4T5f8sSWLSTO8d7lzwGqnHcIz9RqgFoX7QyGKdB1JGk3gVpC%2F7hMujpqbFHCs5ulLN1V4rSF56cR7Lg5441WP5iHXyBUETiorfqwRBAuGaERFn5s0NTc3AJIGq7m%2FzYOXTny%2B%2FT1teVk2OvqoGhN6aEUGgBamRope%2BdSFzw%2FB83pRCHJ69SF1fP7fTr1DrBZ9%2FBfVixF2piKcT2N8tfkV59djzhG8tJmz466WrlRzYCyTMOyw5FPDRiq%2B4cL3sl%2F5kzEr2YVMnxsUxu1QMqK6gI4JbWCphtOgfUxnyWgrEf0nH1zzF4cukMTH8IO8UllgTvGq0Pq9btB67GpaiNKVATk5WFplVOlm%2FwXPJjIHAZz9zkAd%2Bc2kg2FJmEwD5BlYC3wTaojoAMLOc%2FLwGOqUBTDEDZYe2A2V1tmLqnQtqHhcfVRH5GidGEQ70BtQfThp8dBSetjaFrX5BO3XK9X7rxxpemKcjW2gTv6z8nPPIDPCaclyFbTT3QFJlqLD4%2FG3DHsKSx%2BcIi3z2JxJ7dd2Kbz3mLDGL2SpxN9FYWafYxFehxjfdvcKn%2B7cIQf7Iwqbdi2IMXupLngqnYtsjqhx6GCwSqV8oBNlEPbMBn3lzE%2FLUc0O1&X-Amz-Signature=bff3e40a6f404f3b07e0df0d3229230f7defe5d75a784f0a298ab3b44a6238a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMTF6EUE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWnO0njCxQLu1PNfN2XeE%2B9rtWbVXHObxZTnenxUPwpgIhAITCrNhQI43UQczZDUPMTXqosmiN%2FAkxAJC%2Fr2XZhc7TKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzplxFqm1iWPM8rb3Aq3AMBkDmp2ZWgTxzy7464jTCvTz%2BZn%2FrsaxWPKbKMenWnRC5AVBIrI16C6tpnDYY0tOs3eXZAJ7Pb%2BmtOygyQNXFMmppmZci4ZwGDFZEKTmnUl4DkyHl8m%2BsK2Ad1JRcUZLm05LmbPnJND9QSSLwLuv0IlR1qVQtJm3p26ftccxEk7D%2FqaJbQSPrgwzTdB2nFVtWai46cac0F0lHJeIUqITlPt010cxgy8loKfIVLNiATwfpCiNsuN8XdSIQ4UeXXyz7f1dcaHHgIpAORQ5vXeGpkiZirfERADcxQf3cn4MZAWIJjT5Z2zD0MQPHWFR839JNBF9F94LWzgEx4TdBmImw9gHBvejnlhWhi6X6nWmH4nHpT7eixRMh%2FKW%2FlDKGPCj9h9fPxQqO9FgYFuGX4PsUBWPPf7NJ7z8cnih6PoCbwh%2ByqF57Dn2Ei4us924w3WQ3c8DPn75nN%2Bv7E6ph6ymFFZVtGJqpA8zwroaIyKetTPlcrhqRvx%2F7uqUM8rSIUPARLh7HSDeyh9V0gWY9OdNGAMpFw6RL2WMeeNnwk5Q%2FlqQzrCHwJmsuBcOS3j%2Fa7UN3xVUHvVOyqRcSDbbAyYw6MWZxdXbyQHoNaEozqE8kuvrnIGXIvuXYEV39KnTDum%2Fy8BjqkAW95hMAnbKsuAHfZkGVkQ0D3VSrOiqxqubz81kykINmBJJhEsMm%2B8tQYKQlLGxyYkQMw%2FsuqVGtdTaLJMndkqOxpYzzsavMgvPopTANbgHED6M1EQBjIHqcs1s6dzADwIMw5xw0QXhCqUK%2FBDvSs%2B%2B8yQGobodsrw69CAkykn3W3KeXb9Cuq6UXK%2BaVT5yo4IUeig3%2BvIMn9L94hod8oNl5vwfBI&X-Amz-Signature=caf655569d7c0b73a24149d23e6b3d79f826129fa00c1673bc91e79ea34b06d2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMTF6EUE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWnO0njCxQLu1PNfN2XeE%2B9rtWbVXHObxZTnenxUPwpgIhAITCrNhQI43UQczZDUPMTXqosmiN%2FAkxAJC%2Fr2XZhc7TKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzplxFqm1iWPM8rb3Aq3AMBkDmp2ZWgTxzy7464jTCvTz%2BZn%2FrsaxWPKbKMenWnRC5AVBIrI16C6tpnDYY0tOs3eXZAJ7Pb%2BmtOygyQNXFMmppmZci4ZwGDFZEKTmnUl4DkyHl8m%2BsK2Ad1JRcUZLm05LmbPnJND9QSSLwLuv0IlR1qVQtJm3p26ftccxEk7D%2FqaJbQSPrgwzTdB2nFVtWai46cac0F0lHJeIUqITlPt010cxgy8loKfIVLNiATwfpCiNsuN8XdSIQ4UeXXyz7f1dcaHHgIpAORQ5vXeGpkiZirfERADcxQf3cn4MZAWIJjT5Z2zD0MQPHWFR839JNBF9F94LWzgEx4TdBmImw9gHBvejnlhWhi6X6nWmH4nHpT7eixRMh%2FKW%2FlDKGPCj9h9fPxQqO9FgYFuGX4PsUBWPPf7NJ7z8cnih6PoCbwh%2ByqF57Dn2Ei4us924w3WQ3c8DPn75nN%2Bv7E6ph6ymFFZVtGJqpA8zwroaIyKetTPlcrhqRvx%2F7uqUM8rSIUPARLh7HSDeyh9V0gWY9OdNGAMpFw6RL2WMeeNnwk5Q%2FlqQzrCHwJmsuBcOS3j%2Fa7UN3xVUHvVOyqRcSDbbAyYw6MWZxdXbyQHoNaEozqE8kuvrnIGXIvuXYEV39KnTDum%2Fy8BjqkAW95hMAnbKsuAHfZkGVkQ0D3VSrOiqxqubz81kykINmBJJhEsMm%2B8tQYKQlLGxyYkQMw%2FsuqVGtdTaLJMndkqOxpYzzsavMgvPopTANbgHED6M1EQBjIHqcs1s6dzADwIMw5xw0QXhCqUK%2FBDvSs%2B%2B8yQGobodsrw69CAkykn3W3KeXb9Cuq6UXK%2BaVT5yo4IUeig3%2BvIMn9L94hod8oNl5vwfBI&X-Amz-Signature=24163892f40b1975d50e70bb4d9711437397ba48f9bd123762d0f601c10003f0&X-Amz-SignedHeaders=host&x-id=GetObject)

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
