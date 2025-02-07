

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LTNOSAL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD%2FCJJX1wDEhaXi%2F0yZp5Tg5ES89%2BGa6dLqpU%2FzYFcyOQIgYimEs6Lp9KhgpRm4uBNYUy36Hdi2Y86fETlEyDpmv9cq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLARZ5qCv0SleK6cHSrcA4cvttR%2BwRArCv6yRisxhY402EYR1QbRmsMSJEMgcKyDqLJqdZ6LMN0GcFtN2VDZTBj1zH8x0OwEc0wVfx8BVgMN68HjGpbdz2sJI1m2nWc5Eti%2FjekIpD0ZLzhiGJ%2F9h%2FglCRzFZIvDV9I6lTXmApjVCRYyyVsryVAVIBLcUr6B%2BI9F07nPU371rQMs1s3hz5sKg2%2Bq%2FsnWlIZqPlESZ4nkUIWxu6%2F6VQKJ%2Bah9vFbgicNz65WH3EklHCG3Gwg3pLLoyHSDpVSMSpS%2FpziaihEe%2FWjAVcG%2FfQygEtAC9sEZXYMbNoNxzxjPZclUhWf0Gfe9JJftwCgsX3n8UlTdyZaq76gdS1jqOLg9wD7TLQsmoP%2B932A6ZNczZ%2BFxyqdh8yWRm7fDLBfWkF1K9tpKqV1EnIy83Qc4TGXXriJqY65I7%2BVdQ%2BYSByTx4SWZe%2F8VLR4MVK%2F%2BcgwQ952jVlbDScLhZmBSXtqoz%2BFkM%2BBJfBzGEORsywuBhPt4fCFOORLqS3WmSytustz7xPWKPobCcbHqLFKhn4iLjcdS9bkDk8%2FPsfu8yASb1EExoAAYY%2B%2FV6Wx0h4z0ZMnTY2MpjAK%2F%2FNj1SiO3rDl1UddavKZoPEzrUaviEIMyXdCiyjLMML%2FSmb0GOqUBIbI60FMtToEPeh9cQD9RtNtNUahmxlCudJnrp8yhgurdVlK7CA1gyroools7KVwlXtrRfIM%2FX2Hw5NAyjIgbX3KkfWyCAUWCx5zQ6z%2FduPG88nn%2BN0IvYW3SK8fsNsTMGsvj%2Fww1EHaKl6KF6mLYJ5lm8jBHkh%2FnyYkVCXPFlgvSOOd6PsA9gxT67FFbw%2BN2pF%2B6SY7eJfkA3Sb50CdDgmLxstil&X-Amz-Signature=35ec6517ba5703757ad5944ef67634cc1030dfbde1a9ecd1fb19f1c27f814236&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LTNOSAL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD%2FCJJX1wDEhaXi%2F0yZp5Tg5ES89%2BGa6dLqpU%2FzYFcyOQIgYimEs6Lp9KhgpRm4uBNYUy36Hdi2Y86fETlEyDpmv9cq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLARZ5qCv0SleK6cHSrcA4cvttR%2BwRArCv6yRisxhY402EYR1QbRmsMSJEMgcKyDqLJqdZ6LMN0GcFtN2VDZTBj1zH8x0OwEc0wVfx8BVgMN68HjGpbdz2sJI1m2nWc5Eti%2FjekIpD0ZLzhiGJ%2F9h%2FglCRzFZIvDV9I6lTXmApjVCRYyyVsryVAVIBLcUr6B%2BI9F07nPU371rQMs1s3hz5sKg2%2Bq%2FsnWlIZqPlESZ4nkUIWxu6%2F6VQKJ%2Bah9vFbgicNz65WH3EklHCG3Gwg3pLLoyHSDpVSMSpS%2FpziaihEe%2FWjAVcG%2FfQygEtAC9sEZXYMbNoNxzxjPZclUhWf0Gfe9JJftwCgsX3n8UlTdyZaq76gdS1jqOLg9wD7TLQsmoP%2B932A6ZNczZ%2BFxyqdh8yWRm7fDLBfWkF1K9tpKqV1EnIy83Qc4TGXXriJqY65I7%2BVdQ%2BYSByTx4SWZe%2F8VLR4MVK%2F%2BcgwQ952jVlbDScLhZmBSXtqoz%2BFkM%2BBJfBzGEORsywuBhPt4fCFOORLqS3WmSytustz7xPWKPobCcbHqLFKhn4iLjcdS9bkDk8%2FPsfu8yASb1EExoAAYY%2B%2FV6Wx0h4z0ZMnTY2MpjAK%2F%2FNj1SiO3rDl1UddavKZoPEzrUaviEIMyXdCiyjLMML%2FSmb0GOqUBIbI60FMtToEPeh9cQD9RtNtNUahmxlCudJnrp8yhgurdVlK7CA1gyroools7KVwlXtrRfIM%2FX2Hw5NAyjIgbX3KkfWyCAUWCx5zQ6z%2FduPG88nn%2BN0IvYW3SK8fsNsTMGsvj%2Fww1EHaKl6KF6mLYJ5lm8jBHkh%2FnyYkVCXPFlgvSOOd6PsA9gxT67FFbw%2BN2pF%2B6SY7eJfkA3Sb50CdDgmLxstil&X-Amz-Signature=31973ef3b6e02ff00202206914808c30a5ce35b929aaffa7e2ba4363c0bd9154&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LTNOSAL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD%2FCJJX1wDEhaXi%2F0yZp5Tg5ES89%2BGa6dLqpU%2FzYFcyOQIgYimEs6Lp9KhgpRm4uBNYUy36Hdi2Y86fETlEyDpmv9cq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDLARZ5qCv0SleK6cHSrcA4cvttR%2BwRArCv6yRisxhY402EYR1QbRmsMSJEMgcKyDqLJqdZ6LMN0GcFtN2VDZTBj1zH8x0OwEc0wVfx8BVgMN68HjGpbdz2sJI1m2nWc5Eti%2FjekIpD0ZLzhiGJ%2F9h%2FglCRzFZIvDV9I6lTXmApjVCRYyyVsryVAVIBLcUr6B%2BI9F07nPU371rQMs1s3hz5sKg2%2Bq%2FsnWlIZqPlESZ4nkUIWxu6%2F6VQKJ%2Bah9vFbgicNz65WH3EklHCG3Gwg3pLLoyHSDpVSMSpS%2FpziaihEe%2FWjAVcG%2FfQygEtAC9sEZXYMbNoNxzxjPZclUhWf0Gfe9JJftwCgsX3n8UlTdyZaq76gdS1jqOLg9wD7TLQsmoP%2B932A6ZNczZ%2BFxyqdh8yWRm7fDLBfWkF1K9tpKqV1EnIy83Qc4TGXXriJqY65I7%2BVdQ%2BYSByTx4SWZe%2F8VLR4MVK%2F%2BcgwQ952jVlbDScLhZmBSXtqoz%2BFkM%2BBJfBzGEORsywuBhPt4fCFOORLqS3WmSytustz7xPWKPobCcbHqLFKhn4iLjcdS9bkDk8%2FPsfu8yASb1EExoAAYY%2B%2FV6Wx0h4z0ZMnTY2MpjAK%2F%2FNj1SiO3rDl1UddavKZoPEzrUaviEIMyXdCiyjLMML%2FSmb0GOqUBIbI60FMtToEPeh9cQD9RtNtNUahmxlCudJnrp8yhgurdVlK7CA1gyroools7KVwlXtrRfIM%2FX2Hw5NAyjIgbX3KkfWyCAUWCx5zQ6z%2FduPG88nn%2BN0IvYW3SK8fsNsTMGsvj%2Fww1EHaKl6KF6mLYJ5lm8jBHkh%2FnyYkVCXPFlgvSOOd6PsA9gxT67FFbw%2BN2pF%2B6SY7eJfkA3Sb50CdDgmLxstil&X-Amz-Signature=48092077fb2545b94bdd1f919e093373c58581d6d97f0c114994a8860af8fabd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQYSX7V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDEtqe3eV8zRrowsTc51ByUn9rnLMGtnyPmh77pMflEUwIhAO8u%2Fhue%2FSdi2iJMkEOd%2FM7jAW4ykIOiWW9EEZ8tkfZzKv8DCH0QABoMNjM3NDIzMTgzODA1IgxrLpBzYAcV3KTL4v8q3ANY1RMjRUGT8rp4IK0tjTf%2FwztkpQIGgdisIksTTXoK%2F4kl9JH44HmPVxO2rHvQmgAEnh8x4emRbBHrMsVO6gNycw0CT4QT5Wl6z4WvMeZBba%2B%2BwN%2Bxx73pCuZJwQyrtyJzFWso%2BZaslO6kgriPRAibqlbbzYgbnEHFXnq0zTORW4jY5%2BNSrJXku5isGsEwmJPUGdiPWT8VJ9E5kN0qUu9VOiTCbaIZb8N9kqJUxiC0wHmNBjJ2FDiz7pF7nKNI9wdAw%2FSju69nvqLbMg3q%2BkLsQwePjxRQqCQuAnRU8oO6LtFkFe%2FUOpZ8pprs1n%2BuuXaxffYP%2BE%2BK2WGOn%2BUB7%2B6uy%2FuPIEGc1zUWbU0iBynYhLsG8HpdKQaoSZohT7AiyOKGDRug5zMs7iFQ1t2FtWGXLSvilCrwA7%2F7tYoSsoDXASp3PWiAkAMcCBhQ0OSk8zIkhq7Qkvkg8hk9%2BRk9yiLPvt8LDenkT4VImFaH7RkxGDkHLuR6LerfwafcgEgXjAZsIlNBcBzEDiznX6hJd4UyUemxGT%2FLHw78oc0gQGAKFW0NnFSmb1qChr%2FmgclwpWmUIwA1x9DJajbVOj%2BZZgSu8VO7udP1Ej5klaUN%2FDBDb2X%2BJjYuQxUnqNK4KjCA05m9BjqkASaqiJmueDd%2BAZsn%2BFJBUYgt3OWBNlgpVfVHtIiIjYgc7s7v8jitMHEBzbzkSd1tugPfsJDgKMP0lN96dm9IFN4tLr2kf0k0byyP2BB46vHHwHzHgjBuyOUhMQwsofa7kKqVkj98gmcRB4p%2FtkqW%2FWiX3m0n7FqRbIJXQA5Cr0AqeYNS%2BX4owFVKPFCTivKsK4EvBgS4AbJJyqviShK9jItEhdwm&X-Amz-Signature=9d0205db9f4a2bd461fc0c7dd17b2c812285a282cd6a1022f642a65d0843ce95&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQYSX7V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDEtqe3eV8zRrowsTc51ByUn9rnLMGtnyPmh77pMflEUwIhAO8u%2Fhue%2FSdi2iJMkEOd%2FM7jAW4ykIOiWW9EEZ8tkfZzKv8DCH0QABoMNjM3NDIzMTgzODA1IgxrLpBzYAcV3KTL4v8q3ANY1RMjRUGT8rp4IK0tjTf%2FwztkpQIGgdisIksTTXoK%2F4kl9JH44HmPVxO2rHvQmgAEnh8x4emRbBHrMsVO6gNycw0CT4QT5Wl6z4WvMeZBba%2B%2BwN%2Bxx73pCuZJwQyrtyJzFWso%2BZaslO6kgriPRAibqlbbzYgbnEHFXnq0zTORW4jY5%2BNSrJXku5isGsEwmJPUGdiPWT8VJ9E5kN0qUu9VOiTCbaIZb8N9kqJUxiC0wHmNBjJ2FDiz7pF7nKNI9wdAw%2FSju69nvqLbMg3q%2BkLsQwePjxRQqCQuAnRU8oO6LtFkFe%2FUOpZ8pprs1n%2BuuXaxffYP%2BE%2BK2WGOn%2BUB7%2B6uy%2FuPIEGc1zUWbU0iBynYhLsG8HpdKQaoSZohT7AiyOKGDRug5zMs7iFQ1t2FtWGXLSvilCrwA7%2F7tYoSsoDXASp3PWiAkAMcCBhQ0OSk8zIkhq7Qkvkg8hk9%2BRk9yiLPvt8LDenkT4VImFaH7RkxGDkHLuR6LerfwafcgEgXjAZsIlNBcBzEDiznX6hJd4UyUemxGT%2FLHw78oc0gQGAKFW0NnFSmb1qChr%2FmgclwpWmUIwA1x9DJajbVOj%2BZZgSu8VO7udP1Ej5klaUN%2FDBDb2X%2BJjYuQxUnqNK4KjCA05m9BjqkASaqiJmueDd%2BAZsn%2BFJBUYgt3OWBNlgpVfVHtIiIjYgc7s7v8jitMHEBzbzkSd1tugPfsJDgKMP0lN96dm9IFN4tLr2kf0k0byyP2BB46vHHwHzHgjBuyOUhMQwsofa7kKqVkj98gmcRB4p%2FtkqW%2FWiX3m0n7FqRbIJXQA5Cr0AqeYNS%2BX4owFVKPFCTivKsK4EvBgS4AbJJyqviShK9jItEhdwm&X-Amz-Signature=cba76ea7619ada86e38de2482fabe6f01a404fcb8bbee57990667590d0200287&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQYSX7V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDEtqe3eV8zRrowsTc51ByUn9rnLMGtnyPmh77pMflEUwIhAO8u%2Fhue%2FSdi2iJMkEOd%2FM7jAW4ykIOiWW9EEZ8tkfZzKv8DCH0QABoMNjM3NDIzMTgzODA1IgxrLpBzYAcV3KTL4v8q3ANY1RMjRUGT8rp4IK0tjTf%2FwztkpQIGgdisIksTTXoK%2F4kl9JH44HmPVxO2rHvQmgAEnh8x4emRbBHrMsVO6gNycw0CT4QT5Wl6z4WvMeZBba%2B%2BwN%2Bxx73pCuZJwQyrtyJzFWso%2BZaslO6kgriPRAibqlbbzYgbnEHFXnq0zTORW4jY5%2BNSrJXku5isGsEwmJPUGdiPWT8VJ9E5kN0qUu9VOiTCbaIZb8N9kqJUxiC0wHmNBjJ2FDiz7pF7nKNI9wdAw%2FSju69nvqLbMg3q%2BkLsQwePjxRQqCQuAnRU8oO6LtFkFe%2FUOpZ8pprs1n%2BuuXaxffYP%2BE%2BK2WGOn%2BUB7%2B6uy%2FuPIEGc1zUWbU0iBynYhLsG8HpdKQaoSZohT7AiyOKGDRug5zMs7iFQ1t2FtWGXLSvilCrwA7%2F7tYoSsoDXASp3PWiAkAMcCBhQ0OSk8zIkhq7Qkvkg8hk9%2BRk9yiLPvt8LDenkT4VImFaH7RkxGDkHLuR6LerfwafcgEgXjAZsIlNBcBzEDiznX6hJd4UyUemxGT%2FLHw78oc0gQGAKFW0NnFSmb1qChr%2FmgclwpWmUIwA1x9DJajbVOj%2BZZgSu8VO7udP1Ej5klaUN%2FDBDb2X%2BJjYuQxUnqNK4KjCA05m9BjqkASaqiJmueDd%2BAZsn%2BFJBUYgt3OWBNlgpVfVHtIiIjYgc7s7v8jitMHEBzbzkSd1tugPfsJDgKMP0lN96dm9IFN4tLr2kf0k0byyP2BB46vHHwHzHgjBuyOUhMQwsofa7kKqVkj98gmcRB4p%2FtkqW%2FWiX3m0n7FqRbIJXQA5Cr0AqeYNS%2BX4owFVKPFCTivKsK4EvBgS4AbJJyqviShK9jItEhdwm&X-Amz-Signature=4814c1ad9af0c9ef65802ac6ebd9f72484dbedc38ef0089881f6f9c75e1290aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQYSX7V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDEtqe3eV8zRrowsTc51ByUn9rnLMGtnyPmh77pMflEUwIhAO8u%2Fhue%2FSdi2iJMkEOd%2FM7jAW4ykIOiWW9EEZ8tkfZzKv8DCH0QABoMNjM3NDIzMTgzODA1IgxrLpBzYAcV3KTL4v8q3ANY1RMjRUGT8rp4IK0tjTf%2FwztkpQIGgdisIksTTXoK%2F4kl9JH44HmPVxO2rHvQmgAEnh8x4emRbBHrMsVO6gNycw0CT4QT5Wl6z4WvMeZBba%2B%2BwN%2Bxx73pCuZJwQyrtyJzFWso%2BZaslO6kgriPRAibqlbbzYgbnEHFXnq0zTORW4jY5%2BNSrJXku5isGsEwmJPUGdiPWT8VJ9E5kN0qUu9VOiTCbaIZb8N9kqJUxiC0wHmNBjJ2FDiz7pF7nKNI9wdAw%2FSju69nvqLbMg3q%2BkLsQwePjxRQqCQuAnRU8oO6LtFkFe%2FUOpZ8pprs1n%2BuuXaxffYP%2BE%2BK2WGOn%2BUB7%2B6uy%2FuPIEGc1zUWbU0iBynYhLsG8HpdKQaoSZohT7AiyOKGDRug5zMs7iFQ1t2FtWGXLSvilCrwA7%2F7tYoSsoDXASp3PWiAkAMcCBhQ0OSk8zIkhq7Qkvkg8hk9%2BRk9yiLPvt8LDenkT4VImFaH7RkxGDkHLuR6LerfwafcgEgXjAZsIlNBcBzEDiznX6hJd4UyUemxGT%2FLHw78oc0gQGAKFW0NnFSmb1qChr%2FmgclwpWmUIwA1x9DJajbVOj%2BZZgSu8VO7udP1Ej5klaUN%2FDBDb2X%2BJjYuQxUnqNK4KjCA05m9BjqkASaqiJmueDd%2BAZsn%2BFJBUYgt3OWBNlgpVfVHtIiIjYgc7s7v8jitMHEBzbzkSd1tugPfsJDgKMP0lN96dm9IFN4tLr2kf0k0byyP2BB46vHHwHzHgjBuyOUhMQwsofa7kKqVkj98gmcRB4p%2FtkqW%2FWiX3m0n7FqRbIJXQA5Cr0AqeYNS%2BX4owFVKPFCTivKsK4EvBgS4AbJJyqviShK9jItEhdwm&X-Amz-Signature=6224528ddb483d142e3953855ff3cdb203bf9f9750a253ed26a73b1f854048fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQYSX7V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDEtqe3eV8zRrowsTc51ByUn9rnLMGtnyPmh77pMflEUwIhAO8u%2Fhue%2FSdi2iJMkEOd%2FM7jAW4ykIOiWW9EEZ8tkfZzKv8DCH0QABoMNjM3NDIzMTgzODA1IgxrLpBzYAcV3KTL4v8q3ANY1RMjRUGT8rp4IK0tjTf%2FwztkpQIGgdisIksTTXoK%2F4kl9JH44HmPVxO2rHvQmgAEnh8x4emRbBHrMsVO6gNycw0CT4QT5Wl6z4WvMeZBba%2B%2BwN%2Bxx73pCuZJwQyrtyJzFWso%2BZaslO6kgriPRAibqlbbzYgbnEHFXnq0zTORW4jY5%2BNSrJXku5isGsEwmJPUGdiPWT8VJ9E5kN0qUu9VOiTCbaIZb8N9kqJUxiC0wHmNBjJ2FDiz7pF7nKNI9wdAw%2FSju69nvqLbMg3q%2BkLsQwePjxRQqCQuAnRU8oO6LtFkFe%2FUOpZ8pprs1n%2BuuXaxffYP%2BE%2BK2WGOn%2BUB7%2B6uy%2FuPIEGc1zUWbU0iBynYhLsG8HpdKQaoSZohT7AiyOKGDRug5zMs7iFQ1t2FtWGXLSvilCrwA7%2F7tYoSsoDXASp3PWiAkAMcCBhQ0OSk8zIkhq7Qkvkg8hk9%2BRk9yiLPvt8LDenkT4VImFaH7RkxGDkHLuR6LerfwafcgEgXjAZsIlNBcBzEDiznX6hJd4UyUemxGT%2FLHw78oc0gQGAKFW0NnFSmb1qChr%2FmgclwpWmUIwA1x9DJajbVOj%2BZZgSu8VO7udP1Ej5klaUN%2FDBDb2X%2BJjYuQxUnqNK4KjCA05m9BjqkASaqiJmueDd%2BAZsn%2BFJBUYgt3OWBNlgpVfVHtIiIjYgc7s7v8jitMHEBzbzkSd1tugPfsJDgKMP0lN96dm9IFN4tLr2kf0k0byyP2BB46vHHwHzHgjBuyOUhMQwsofa7kKqVkj98gmcRB4p%2FtkqW%2FWiX3m0n7FqRbIJXQA5Cr0AqeYNS%2BX4owFVKPFCTivKsK4EvBgS4AbJJyqviShK9jItEhdwm&X-Amz-Signature=95d9e89e114b9715edc558321afede1dda2a63e6c42418425b70e1ef9ba2b74e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQYSX7V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDEtqe3eV8zRrowsTc51ByUn9rnLMGtnyPmh77pMflEUwIhAO8u%2Fhue%2FSdi2iJMkEOd%2FM7jAW4ykIOiWW9EEZ8tkfZzKv8DCH0QABoMNjM3NDIzMTgzODA1IgxrLpBzYAcV3KTL4v8q3ANY1RMjRUGT8rp4IK0tjTf%2FwztkpQIGgdisIksTTXoK%2F4kl9JH44HmPVxO2rHvQmgAEnh8x4emRbBHrMsVO6gNycw0CT4QT5Wl6z4WvMeZBba%2B%2BwN%2Bxx73pCuZJwQyrtyJzFWso%2BZaslO6kgriPRAibqlbbzYgbnEHFXnq0zTORW4jY5%2BNSrJXku5isGsEwmJPUGdiPWT8VJ9E5kN0qUu9VOiTCbaIZb8N9kqJUxiC0wHmNBjJ2FDiz7pF7nKNI9wdAw%2FSju69nvqLbMg3q%2BkLsQwePjxRQqCQuAnRU8oO6LtFkFe%2FUOpZ8pprs1n%2BuuXaxffYP%2BE%2BK2WGOn%2BUB7%2B6uy%2FuPIEGc1zUWbU0iBynYhLsG8HpdKQaoSZohT7AiyOKGDRug5zMs7iFQ1t2FtWGXLSvilCrwA7%2F7tYoSsoDXASp3PWiAkAMcCBhQ0OSk8zIkhq7Qkvkg8hk9%2BRk9yiLPvt8LDenkT4VImFaH7RkxGDkHLuR6LerfwafcgEgXjAZsIlNBcBzEDiznX6hJd4UyUemxGT%2FLHw78oc0gQGAKFW0NnFSmb1qChr%2FmgclwpWmUIwA1x9DJajbVOj%2BZZgSu8VO7udP1Ej5klaUN%2FDBDb2X%2BJjYuQxUnqNK4KjCA05m9BjqkASaqiJmueDd%2BAZsn%2BFJBUYgt3OWBNlgpVfVHtIiIjYgc7s7v8jitMHEBzbzkSd1tugPfsJDgKMP0lN96dm9IFN4tLr2kf0k0byyP2BB46vHHwHzHgjBuyOUhMQwsofa7kKqVkj98gmcRB4p%2FtkqW%2FWiX3m0n7FqRbIJXQA5Cr0AqeYNS%2BX4owFVKPFCTivKsK4EvBgS4AbJJyqviShK9jItEhdwm&X-Amz-Signature=94c0d34053620adb29a3f173970f7a7c4194409262e7e5feb501db5aae7d2ba3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6RA3YWT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDqmR4oyg2%2B0XPQ%2FWhZm7tHxix4RmJEDb84BucE1MPnEgIhAK7x%2FRSiIgFygcdMrsprVZBEaphLVC1wtMdHWqVWa8dSKv8DCH0QABoMNjM3NDIzMTgzODA1IgyPmjQ4tYfLA%2FJkyQwq3AOqg2ijOJFk59OAFnaUQtxD93K1GCZoVZopMcD%2FRvUtQ7uLdtWM71om0BzC%2BxzLPVwZ6vMpbZShr7FMz3oVFteGMNJH2TrutDTXffs2V3M%2FMl7P9wm3SSYyyO1i5RdYjfinJ%2B0eQOW9f0gh%2B%2F76Nl7sVeA4dg3TDDnMC6cj7eD%2Bpttt9wdDGBogXsmgA5DDTGsjnuPWwi0d6M98Nye1P8bnLT9gNfy%2Fd1buSDFnJUnlqSab9oj4IuU4F%2Fn2%2FKUGoUDfZvb9ZheaNxjWkGp0lynPzRor3lSATzUGQBF7TrgCmgtPMKgBaW3BCLnnN5UZ6Eit%2FCVw5EYhV3vID4G7gSYAbcFJF25vVqQvbxQVoESiycxWGQg1AQyhEoBpwKsrPUOYXQcnsC%2FCZ7yU0xXUrdImJj%2FibBgBdzjMNuGqLIJwFSTUU4q96xj%2Bx5SNMRPPESWuV9TJ9NPYOh1MgybSQUAxXHF7m%2FMPfS5g2Kk5wRs36p2fH1%2BsrxVUI8xUVOXtKAdqGSc0ilo%2Bf0CEB8Wf0btbQgHPXyPJr8%2Bo1fU0WOTIF9sf8kEq%2FQr5mtFiokeOmqAGvsJP%2BZC2ZdhI%2FSSUlvr%2BhpM7UkP8yiIPS4EvSVZUl4NPhAhXvGqGldP%2FOTCd0pm9BjqkAb7gHCoog5APjPynXNGek5RT2PVWLYMuGM%2B6x1cJvas%2FYPw%2BPNweBNEF5VSOK6IIBJKyKHNlglBMfePLT%2BNUjuXykq1ebNfXr3gpOWheLDGTR5T9UGZbmjUKXZ94UBmC0C49vSVWUS%2BUKGU1CgRpgRrzQAeNM%2FugFFmjKw2%2F7IPP9hYf%2Fx8xhyLR03EmKngwPHGesmp8xQXvNbSfG5Mslv%2BB17VO&X-Amz-Signature=febf91b32b7522153546dd3beb43e6920d4a4606f2f26de48504681b483ace04&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJXA3L4I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDcTm44456wrQs9uH3TbVwRcN5NVQRL6EmfAdlmcpBcYAIhAP9iGWifZ8luBVR3MPdRBAAIcQs2A9wD49gbkWKWOpOdKv8DCH0QABoMNjM3NDIzMTgzODA1IgwV1N1F9adv9INvG%2Boq3AMZSbHVUgLAqBbCzzE9VgeSHRe7ujyxqNAkvPy1drgOT7JDlQyCkfkAlxK3ayAspJQhtaV91eHlUQhyBE4r8lqB94Wc%2BjkOxPq1eznvvBO9zDs1prGZ88f98tyjCekz1e0P6bQE9Rg9V7wKiBTpYSKbPQAYWPWjAftKbc4mcz3d8%2F6CcwCIaKjVrvgN5jvQ5ekousgkOItIzjeQRhJ7LnRUwj%2Fk%2FSFrSSlGwKG8z%2FmBdJ8R2Gc2d3XVIUJtasnvDT5aVifcF2BuNA0u0ScNNAyi%2FNeOGMNq%2BxEyNCSzkyEaKVXgN7vma%2Fcymi09jAsuxGRpdTw3PJCK4hrTEslz%2BjTlzHA9NakRyMkOyICs6qpoel4CR%2FGF7t3rf0mhwtgheW3J6V8IJiUBhpJM2OUWc73tWFs60ig5XudsYOERBpNEqZRpiBgq8EXTtqBCBlB9vOvYe%2Fz9PEXOoIQDaVfZ7vuDwbEiRX9Ios5f%2Bh9%2F2goXfbDMdy%2BLIpMwb7VRU%2BnefkMP%2B6FealYRHwfyC4BKd7YwbE9D9nhzOBLAUHJM7%2BOZQ4nhRPEHEokIBli291l3prhL0OySsf8hFHRJsIXo5Qyc35MOW%2B5Ycqsu6LtTCT%2Bp8y%2FUlYiK7NFIeAwvEjDb0pm9BjqkAb7JE2wCYS7%2BhDWlb0LPhRMc1K9EC4JfCcUPoKUn0ZvrSjTnIy75nKg4UZvvXicxa0TsCcHpSWfupu0esHlHsFdqMd%2BabiivwLHgPJeEo6n%2BjThITpkWZHIZ546%2BwgQR2tuXpIisVPxHnATaiDUSowUjj7TfW8P0cKeV9WG0m1r5mOwfOXpTgA8zm0BWaklA0OuyZmigGcExb%2F5uTG9u5GEeEEbF&X-Amz-Signature=4fbe59a09cd68fcd2ec6bb45bd6e6a2fb501478d2dbf8feb111bc09ce317c680&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQYSX7V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDEtqe3eV8zRrowsTc51ByUn9rnLMGtnyPmh77pMflEUwIhAO8u%2Fhue%2FSdi2iJMkEOd%2FM7jAW4ykIOiWW9EEZ8tkfZzKv8DCH0QABoMNjM3NDIzMTgzODA1IgxrLpBzYAcV3KTL4v8q3ANY1RMjRUGT8rp4IK0tjTf%2FwztkpQIGgdisIksTTXoK%2F4kl9JH44HmPVxO2rHvQmgAEnh8x4emRbBHrMsVO6gNycw0CT4QT5Wl6z4WvMeZBba%2B%2BwN%2Bxx73pCuZJwQyrtyJzFWso%2BZaslO6kgriPRAibqlbbzYgbnEHFXnq0zTORW4jY5%2BNSrJXku5isGsEwmJPUGdiPWT8VJ9E5kN0qUu9VOiTCbaIZb8N9kqJUxiC0wHmNBjJ2FDiz7pF7nKNI9wdAw%2FSju69nvqLbMg3q%2BkLsQwePjxRQqCQuAnRU8oO6LtFkFe%2FUOpZ8pprs1n%2BuuXaxffYP%2BE%2BK2WGOn%2BUB7%2B6uy%2FuPIEGc1zUWbU0iBynYhLsG8HpdKQaoSZohT7AiyOKGDRug5zMs7iFQ1t2FtWGXLSvilCrwA7%2F7tYoSsoDXASp3PWiAkAMcCBhQ0OSk8zIkhq7Qkvkg8hk9%2BRk9yiLPvt8LDenkT4VImFaH7RkxGDkHLuR6LerfwafcgEgXjAZsIlNBcBzEDiznX6hJd4UyUemxGT%2FLHw78oc0gQGAKFW0NnFSmb1qChr%2FmgclwpWmUIwA1x9DJajbVOj%2BZZgSu8VO7udP1Ej5klaUN%2FDBDb2X%2BJjYuQxUnqNK4KjCA05m9BjqkASaqiJmueDd%2BAZsn%2BFJBUYgt3OWBNlgpVfVHtIiIjYgc7s7v8jitMHEBzbzkSd1tugPfsJDgKMP0lN96dm9IFN4tLr2kf0k0byyP2BB46vHHwHzHgjBuyOUhMQwsofa7kKqVkj98gmcRB4p%2FtkqW%2FWiX3m0n7FqRbIJXQA5Cr0AqeYNS%2BX4owFVKPFCTivKsK4EvBgS4AbJJyqviShK9jItEhdwm&X-Amz-Signature=9dd51e782cde24f1581c4431012f41cb6f22bd9036fffd958d06532b05a36472&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQYSX7V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDEtqe3eV8zRrowsTc51ByUn9rnLMGtnyPmh77pMflEUwIhAO8u%2Fhue%2FSdi2iJMkEOd%2FM7jAW4ykIOiWW9EEZ8tkfZzKv8DCH0QABoMNjM3NDIzMTgzODA1IgxrLpBzYAcV3KTL4v8q3ANY1RMjRUGT8rp4IK0tjTf%2FwztkpQIGgdisIksTTXoK%2F4kl9JH44HmPVxO2rHvQmgAEnh8x4emRbBHrMsVO6gNycw0CT4QT5Wl6z4WvMeZBba%2B%2BwN%2Bxx73pCuZJwQyrtyJzFWso%2BZaslO6kgriPRAibqlbbzYgbnEHFXnq0zTORW4jY5%2BNSrJXku5isGsEwmJPUGdiPWT8VJ9E5kN0qUu9VOiTCbaIZb8N9kqJUxiC0wHmNBjJ2FDiz7pF7nKNI9wdAw%2FSju69nvqLbMg3q%2BkLsQwePjxRQqCQuAnRU8oO6LtFkFe%2FUOpZ8pprs1n%2BuuXaxffYP%2BE%2BK2WGOn%2BUB7%2B6uy%2FuPIEGc1zUWbU0iBynYhLsG8HpdKQaoSZohT7AiyOKGDRug5zMs7iFQ1t2FtWGXLSvilCrwA7%2F7tYoSsoDXASp3PWiAkAMcCBhQ0OSk8zIkhq7Qkvkg8hk9%2BRk9yiLPvt8LDenkT4VImFaH7RkxGDkHLuR6LerfwafcgEgXjAZsIlNBcBzEDiznX6hJd4UyUemxGT%2FLHw78oc0gQGAKFW0NnFSmb1qChr%2FmgclwpWmUIwA1x9DJajbVOj%2BZZgSu8VO7udP1Ej5klaUN%2FDBDb2X%2BJjYuQxUnqNK4KjCA05m9BjqkASaqiJmueDd%2BAZsn%2BFJBUYgt3OWBNlgpVfVHtIiIjYgc7s7v8jitMHEBzbzkSd1tugPfsJDgKMP0lN96dm9IFN4tLr2kf0k0byyP2BB46vHHwHzHgjBuyOUhMQwsofa7kKqVkj98gmcRB4p%2FtkqW%2FWiX3m0n7FqRbIJXQA5Cr0AqeYNS%2BX4owFVKPFCTivKsK4EvBgS4AbJJyqviShK9jItEhdwm&X-Amz-Signature=f550ca09875c02272e2607837f0e619a29c2865e94c348a3d0282cdf5d87c48b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQYSX7V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQDEtqe3eV8zRrowsTc51ByUn9rnLMGtnyPmh77pMflEUwIhAO8u%2Fhue%2FSdi2iJMkEOd%2FM7jAW4ykIOiWW9EEZ8tkfZzKv8DCH0QABoMNjM3NDIzMTgzODA1IgxrLpBzYAcV3KTL4v8q3ANY1RMjRUGT8rp4IK0tjTf%2FwztkpQIGgdisIksTTXoK%2F4kl9JH44HmPVxO2rHvQmgAEnh8x4emRbBHrMsVO6gNycw0CT4QT5Wl6z4WvMeZBba%2B%2BwN%2Bxx73pCuZJwQyrtyJzFWso%2BZaslO6kgriPRAibqlbbzYgbnEHFXnq0zTORW4jY5%2BNSrJXku5isGsEwmJPUGdiPWT8VJ9E5kN0qUu9VOiTCbaIZb8N9kqJUxiC0wHmNBjJ2FDiz7pF7nKNI9wdAw%2FSju69nvqLbMg3q%2BkLsQwePjxRQqCQuAnRU8oO6LtFkFe%2FUOpZ8pprs1n%2BuuXaxffYP%2BE%2BK2WGOn%2BUB7%2B6uy%2FuPIEGc1zUWbU0iBynYhLsG8HpdKQaoSZohT7AiyOKGDRug5zMs7iFQ1t2FtWGXLSvilCrwA7%2F7tYoSsoDXASp3PWiAkAMcCBhQ0OSk8zIkhq7Qkvkg8hk9%2BRk9yiLPvt8LDenkT4VImFaH7RkxGDkHLuR6LerfwafcgEgXjAZsIlNBcBzEDiznX6hJd4UyUemxGT%2FLHw78oc0gQGAKFW0NnFSmb1qChr%2FmgclwpWmUIwA1x9DJajbVOj%2BZZgSu8VO7udP1Ej5klaUN%2FDBDb2X%2BJjYuQxUnqNK4KjCA05m9BjqkASaqiJmueDd%2BAZsn%2BFJBUYgt3OWBNlgpVfVHtIiIjYgc7s7v8jitMHEBzbzkSd1tugPfsJDgKMP0lN96dm9IFN4tLr2kf0k0byyP2BB46vHHwHzHgjBuyOUhMQwsofa7kKqVkj98gmcRB4p%2FtkqW%2FWiX3m0n7FqRbIJXQA5Cr0AqeYNS%2BX4owFVKPFCTivKsK4EvBgS4AbJJyqviShK9jItEhdwm&X-Amz-Signature=7ad89de3a52051ba52e27c5f174b96c2e789708975dad733c217fa9bce68aa51&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3YXGIZ5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQC0AHSwdJnRfNe%2FpZdNKlmJyykmAyDsg%2FyYGvEuYSnsJgIhAJo8goCOMUWd3DJhBXQs7jWMBHwz33Pwk1AedNRIFxCrKv8DCH0QABoMNjM3NDIzMTgzODA1Igw4plSljUpM1A3QcZoq3AONTy9b5dXe16ONPVcGdt6nZKr%2F6yBKexdySVeqta0W129lkhfxwppCOBZid0SOB%2B0Vcyg9H0fh1sdGa7a%2FVMVW65AcSd%2B0ocQ1ShQtENnY3yTzhc9NI4mOomoFHJXLjfNGq%2Fogz7nNPp92q3R7BMGjHEZF%2FgK5FHllEKPZ1jzCR3x7Mj7lNowfDA9HhamReQ%2F2DENfsLr67AA0b4DMqS1p9yrj9F8RAv7dwt0pVjSACEk5f7e60GImA%2BRT%2BtmAidOWQtwQMgeGg%2FRxusNVaOWnHjWnlzqml8IZB5QInR0xDThx6DWVzoIHo5pAFuyUEijPl2k49ouAf%2B7KMgKemVMAEvY%2BjxGAwhaqpl9%2BGlMFDkQYASm367c738ZLd8uVj0i%2BkXCc2NbmJC%2BTYQ%2BaCZZLy%2Bt%2F%2BQFm81FnbxaivURIEwoPNi6OyEt6Gl1YsQUA%2F3hgKTlNYwPeCRS3Sws5dtMEmo1k5SBpjzP5S7QdTjGWQfYf1c2qcod38oV7v4Ht85YB07x9Us4zuKRUS9SsSaNKWF%2BwAcZcAvhnyjd7EY7By2U3ORBbMjHZ6J6MxwGykEyTWtusomjan%2F3JUMdec%2BCz2%2F0v6HjfTXHkdC0WmUdm7xZXCf4zqGmg%2FsiFczD40pm9BjqkAbbEBo%2B7v9uCfm4mSTfCJ61OHaY8%2BBH8Fry8U7t4QeN%2FUyv3TPUgiJ5IYeteI6q6Y3tWWrokNkDr6EPaoBR0W4a9G4cSEy26JQ6c4zHlK4EkUQPLqnwjd6Pi1OzE%2F6ia9iCvsg3hUZFV5muDf43pEZ0516BeFo%2Fcx7Rwx8sbnhh39FogcI9lm%2BAhQ9pyRxHmDc2jSKCpTrzdioFDtfki2TyERACl&X-Amz-Signature=4fec40ae792c822fc0c598eaa57555384cf2bc73727b3a553f3ac3256dd11d1e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KAVVSJP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBUaf5M%2FlMolRkbK%2BJGrbrVkDTEGQmp6L1JQiWNoL3VZAiB9ReNbNVVlNjasybdnz83zhE%2BucmAWRhKlsq6Lf9IbSSr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMmVHVQkvDt4QCCizJKtwDVb1YR8wQ0SZwUlwrCmQ%2FUCOyJ5%2BerXYHrzMCJ5lnorAspPs%2FZq3AzDZxPNr1wyk5mfGlNJWFc4mGotUTy6S2baSLAXQ1%2Bci7pzN8PSWT8Vd80I7ZPH%2Fh49dMSEUb7WX0aUOABpFq72ucQPm%2FKe7biwICP5DEEpHPZB4p%2B4a%2BKug%2FvofJjCZpprRuYoUj5XDh%2Fgo55T7t%2B1xjAth6Ei46ARwCXXyiWPyz0Ykh6PoyjYYsx4lst6mnCPJRtJmCvyjQHqvX2zit9rd7b5%2BWp3rP7%2BWN2QjcheUMlxojbEyQFP7ZQkrTvN9T9%2BGQBIzHrWhrZpKWKCWAEBIeqyUryQu42d7yzrvkm%2BphNWgCZIZX5aNmOegyEwttzFJQ4hsNoFDBp9onBlZtXFZ%2FU4%2BUOh0cY4YNQNZiD2MYTa01vKyrqW2CiAozCQD%2FpLJkMIQciuWwxtRRjXCJ%2F4anmFG9IAnaHYybo%2FeC6rF0KYIt2GivR2ObNOsBXbaQfAlqXLur3pKwEnc0dEFBlf1KgorBQX6lxVyydehUOnyzFTIJAilzvnD88KbQqZQBHWwSX2%2FzAfTIv1WK21HGlEC71%2BtL%2B5EHPAEKDJoea1p2dGVJRwP9YYTji9EnZ9%2FO3YqGF7wwrtKZvQY6pgFxEIE0jrcaeN%2B%2F4XXUgiJMywOTmRPc0%2FfsEk0wwLNKdiqNuxIkL%2F1BM5BsCv%2B8F%2F%2BZ7oo3Z0InOS2f75DmYMM60lTfWi%2FPJSIRFCrLQfDn5n5a5a6dYSmrQI7WBGepiA8zX2CwAuEi2veHHi%2FJ%2Fvis3VTH9%2F0r5VMFKkddPYwt2vKbotmBdh2b9cZIUZ89T8pz0OdSe8ovpei%2Fym2RJFbPrcMchDpO&X-Amz-Signature=9586217fe5fa0b71a64789b60e81d085c630395bdd65e89c71beec2ad16f9b3a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AU2CVEC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCICDKP4lxQG9GIne1x10oXnJp4vz8SoWHXBoOyaZZ96nrAiEA2YuQv7icP65ERFFUTjVuSw1ZawRIMcWKra4GCn7CSKwq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDG4Gjxd%2FZajz1FzN9CrcAyULi2pRcoDsSYZq4NwPOQq7ntvw62ysAGQZdzkibh29o7pdolT3DaFsYbq1Y4Nmv0UHXAd74OrcRPcng8Ty21yMFcLhyDBn4%2FBAN67L8H8bTG6AbHzBmNANiKWTuvMziC5dGpZWgPUpedf8%2BmkxQPrjRPtWIIKY09CMLBHvdtRBCo3ytf0BoZGOfpV0QqNWjO2WZ5GSN3%2BLgmLpaBNxKwhqebNMk%2BcgLXta1nvkUQEESBM7mhWn94G4agNSS96JUvu7J3AVZU8lfTATG8%2BlqjBTag5QqAvl0228wFdgNTuDxBVxrQcpWr%2BLQH1ydu8dWwaO48AAiM%2BqoePM26s1efy7i99E5Tn0ILhbUxivKbxVkklkUFrBOjmGLCDWKWX3yLwZY0ScMOJ0PtgRLhfWmeFzddZouOVdG5vdQG0C3lkjcl8UFz4nQIPQLyI%2BfwqicjI%2FDjaKCww3zU9cGPebcSYKkRdt6h2wPPr7IIJGMQysLXz5yzpaLXIhkvmD6pC6GgHRbqJ48nNoJnVElCynaIVA9CkFzzrT4XwiW%2B3LQsXKNLpi9d0G1VUZLnuxXHEY9tbid7sRqKSu%2Bz3naFtoRpPHMFUnVlHJIGPTP%2BHtcKYY4sclvY5ZsczvaBc1MMDSmb0GOqUBzb%2BNukTa8PaIlcuS776NG0ELoYJvdR2tzJlGGt5qx%2FnEH56bk6fV87XDSO1fCmm56OKOBu30l4XpOdXCHPJE0Ucv4%2FfeXoxkr9JmmcGiekPO%2FgT8RdDNfEssGtLYdtes95PVELd%2FjRcy%2BNyg3aatqMHUUh9jqkWcsA2IXOEHeuP%2FjN4XpWGmoy3uWg7Bw%2BklHfRKnviqzFz6iuwRAOS2EQHy6jL7&X-Amz-Signature=5f9b104adf7afff4f8899e4d85041a220d3edac051219da8e10e419afe30723d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YK4MAEF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCRFrhWL4Gjna707hU6PvDOI17W1Fj4Lz7roPVl%2BRMZ6AIgMDXhU2dMmqHUlKBGaQabnHIWf2srl0TnAPQJ1vy6IcUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDMnb%2BU7KGST9q%2B5ZaCrcA6uG9SiaV87HZpgi%2BPEklXd%2FXBsY2BTiKEqeQGJxpRBIUZ8dJvE%2BaVeb8acVEA2ywGv6Fs%2Bwn3HwqIgkenP6FqZPok%2FNvYDLt7mB%2FH0nW1w7dxLtW8LgYoBACE2QpBIuPPHhaFGv%2FznTrNWcxrVOMjpEEhFzDi9B8sSP25PhOurxWAKP%2BooOe6r5eoFi4MFEIEAMLE3UFcfC3uX9WcWD1fyZPuUlllpqq4Hr84zgT96ZVumd4E92Nx68WbV0qifGi7%2FoTgKWvozvDQkB2vXAHJjHD%2BAPPGXQZiizLAOzuMferIdRhg78%2BNSUZqceY9WEFHdtEgaPQIPsNqzybk6MooaMw7A2sqYe98UJzxwI%2BkFCwDOCDYnfCChi%2FkeCTFnVuqadGv9tvVM8iwWOwPesiB2ihUIuf6TqWlk%2FvP0ZCKM%2F77XGVCHu7SYInkASIOum9T3seBRWSI68IeZsRDVVSN7YzsrjO3jnwHOSRXslac8wkszlzdyoQ9faB9kIOHnT29tYeghn9g7JHOH9Fhgpip2MEZbDR3Ruj58i0t2jeSfQHZ6no84JZgHCMk%2FEuOGCFTBW1nSTik2iSnvGYS4a8FRXUcJgoVmbEzwTUTMZ2g2uByeu2zw%2BBkDyDG4dMOzSmb0GOqUBSWckAEY0BiupN9hpTAwwI8jBZrCtuNrWAPZPjTNZr8NdqyETV%2B%2B0XeJSXovWOL%2Bft2Y5AsNt4YVV7gMK1ZSUlDZMDjJeR%2FhYrBW7ZHycj9YwwzGkIdoDt0kCclMsI%2BajdzvKo2UwIaF6naxdYUGPPEMfcJYET771j055C1aLaPUmR8%2BRFDds6NThwvJ4eDEdJAmEJeSRnrWXt1ztH7vy64m68l7k&X-Amz-Signature=c50d0d5fcd9551768d869d63d5d182a856f68252be1f32fa65df17be01488dc9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YK4MAEF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCRFrhWL4Gjna707hU6PvDOI17W1Fj4Lz7roPVl%2BRMZ6AIgMDXhU2dMmqHUlKBGaQabnHIWf2srl0TnAPQJ1vy6IcUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDMnb%2BU7KGST9q%2B5ZaCrcA6uG9SiaV87HZpgi%2BPEklXd%2FXBsY2BTiKEqeQGJxpRBIUZ8dJvE%2BaVeb8acVEA2ywGv6Fs%2Bwn3HwqIgkenP6FqZPok%2FNvYDLt7mB%2FH0nW1w7dxLtW8LgYoBACE2QpBIuPPHhaFGv%2FznTrNWcxrVOMjpEEhFzDi9B8sSP25PhOurxWAKP%2BooOe6r5eoFi4MFEIEAMLE3UFcfC3uX9WcWD1fyZPuUlllpqq4Hr84zgT96ZVumd4E92Nx68WbV0qifGi7%2FoTgKWvozvDQkB2vXAHJjHD%2BAPPGXQZiizLAOzuMferIdRhg78%2BNSUZqceY9WEFHdtEgaPQIPsNqzybk6MooaMw7A2sqYe98UJzxwI%2BkFCwDOCDYnfCChi%2FkeCTFnVuqadGv9tvVM8iwWOwPesiB2ihUIuf6TqWlk%2FvP0ZCKM%2F77XGVCHu7SYInkASIOum9T3seBRWSI68IeZsRDVVSN7YzsrjO3jnwHOSRXslac8wkszlzdyoQ9faB9kIOHnT29tYeghn9g7JHOH9Fhgpip2MEZbDR3Ruj58i0t2jeSfQHZ6no84JZgHCMk%2FEuOGCFTBW1nSTik2iSnvGYS4a8FRXUcJgoVmbEzwTUTMZ2g2uByeu2zw%2BBkDyDG4dMOzSmb0GOqUBSWckAEY0BiupN9hpTAwwI8jBZrCtuNrWAPZPjTNZr8NdqyETV%2B%2B0XeJSXovWOL%2Bft2Y5AsNt4YVV7gMK1ZSUlDZMDjJeR%2FhYrBW7ZHycj9YwwzGkIdoDt0kCclMsI%2BajdzvKo2UwIaF6naxdYUGPPEMfcJYET771j055C1aLaPUmR8%2BRFDds6NThwvJ4eDEdJAmEJeSRnrWXt1ztH7vy64m68l7k&X-Amz-Signature=195bcc4e3fa15137e9f426545cce6ccbb6d8da80713ec1492d8c255ae420bbaa&X-Amz-SignedHeaders=host&x-id=GetObject)

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
