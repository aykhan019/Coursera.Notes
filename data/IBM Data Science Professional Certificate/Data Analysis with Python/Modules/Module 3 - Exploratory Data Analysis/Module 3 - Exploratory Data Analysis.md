

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYLSZIWJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFKA7XLgdc0dhxkfMT3mMvWraJLQigLihdkq1VXXUiTtAiBlKN7hZHK4AKY3CBbZq9I8xG5lZH%2FhdpZZxyDqwgKfdiqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv2F2H%2BjDPZgHcIbQKtwD89jjQsbP74sf6lMt4MqtYlOqtEp9ME5AcBWXs5TAqc10Veji0xFIOHd1479uSpztjSBfZp0h6C3IDzVVMd4QqAdij7WXCLvSWXgDiLxNPS%2B7xYVCTyGQNU0XiSa4Cq5rCM6CLXYQ4oKaPd9aeilIDAC09x0A8L2%2F%2BP%2BY6eKrPZRwcFCHpLTCcmZfDqydDR55wpjMZeCvpEpB%2BnjFNJOYmZQv0viW%2BTP00JyZLYGMayXF1wPLddm%2B9Sp5oxFc7bMlENqjKOUg1PydjS3Oligo4jgcoXm2RQJTh%2FxHNG8Sb7J%2FnIQI21JWitQiF5qHXmm9rX2qQy6LOnqDe2th3E40%2Bc7%2FHyWkNgEpfUpKNbWt3W272myuR4duxGAwLHvJ4lCIP6geuVRZAo1svqyZ3gOsEzpVgEwCUU58qbzPHx30pvwcwXqX%2FBngvGyz1EVrCdFvbJPYkwwTJdyg85UMN4Zqs6BO6hYrg8lsdT3%2F3NINB3KwugAJ7u64%2FTm%2BNYQu%2BKuz%2FCGjglJ3eAZtgPKFJkiY7%2B%2FvognSbyIAIEMzeJyiX4HVWSb61GzXowIIsBEo3MbcT4eqFUNpHTIGqE8E3RYVpwcqaQciG4kZ5sMQV27PXCzzAUXnheTWOU75BK4w2qv4vAY6pgEcq9ELBLmEx4eWJigPJmpXwxhVVxrxTlNTwq12Zw7B2ti3btNlt19C5aodp7dqpS2%2BsQgRIXZxu4WO8YvT1hwTpJj%2B%2FeQt1JTu6Qz%2FSO%2BkTwORwPEl3FaJFkw4UQwy%2BZiS2mRHiEULwRC6O5rL6XIayUuNMVYEW%2BH0HY6EycVTAu9xpWfRazeEHgXMZwu%2F3p0Adf6G0Bq2RqdKwhI3UPgArECjvAXB&X-Amz-Signature=24fa2a210dcd926aa729389500b69ffe6c73f88bb2d186d97f92ff2d0c1a926b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYLSZIWJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFKA7XLgdc0dhxkfMT3mMvWraJLQigLihdkq1VXXUiTtAiBlKN7hZHK4AKY3CBbZq9I8xG5lZH%2FhdpZZxyDqwgKfdiqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv2F2H%2BjDPZgHcIbQKtwD89jjQsbP74sf6lMt4MqtYlOqtEp9ME5AcBWXs5TAqc10Veji0xFIOHd1479uSpztjSBfZp0h6C3IDzVVMd4QqAdij7WXCLvSWXgDiLxNPS%2B7xYVCTyGQNU0XiSa4Cq5rCM6CLXYQ4oKaPd9aeilIDAC09x0A8L2%2F%2BP%2BY6eKrPZRwcFCHpLTCcmZfDqydDR55wpjMZeCvpEpB%2BnjFNJOYmZQv0viW%2BTP00JyZLYGMayXF1wPLddm%2B9Sp5oxFc7bMlENqjKOUg1PydjS3Oligo4jgcoXm2RQJTh%2FxHNG8Sb7J%2FnIQI21JWitQiF5qHXmm9rX2qQy6LOnqDe2th3E40%2Bc7%2FHyWkNgEpfUpKNbWt3W272myuR4duxGAwLHvJ4lCIP6geuVRZAo1svqyZ3gOsEzpVgEwCUU58qbzPHx30pvwcwXqX%2FBngvGyz1EVrCdFvbJPYkwwTJdyg85UMN4Zqs6BO6hYrg8lsdT3%2F3NINB3KwugAJ7u64%2FTm%2BNYQu%2BKuz%2FCGjglJ3eAZtgPKFJkiY7%2B%2FvognSbyIAIEMzeJyiX4HVWSb61GzXowIIsBEo3MbcT4eqFUNpHTIGqE8E3RYVpwcqaQciG4kZ5sMQV27PXCzzAUXnheTWOU75BK4w2qv4vAY6pgEcq9ELBLmEx4eWJigPJmpXwxhVVxrxTlNTwq12Zw7B2ti3btNlt19C5aodp7dqpS2%2BsQgRIXZxu4WO8YvT1hwTpJj%2B%2FeQt1JTu6Qz%2FSO%2BkTwORwPEl3FaJFkw4UQwy%2BZiS2mRHiEULwRC6O5rL6XIayUuNMVYEW%2BH0HY6EycVTAu9xpWfRazeEHgXMZwu%2F3p0Adf6G0Bq2RqdKwhI3UPgArECjvAXB&X-Amz-Signature=55a178f5852d29b49f0e9ccee3171c6345f2ed02565159e28bc922169e710cd6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYLSZIWJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFKA7XLgdc0dhxkfMT3mMvWraJLQigLihdkq1VXXUiTtAiBlKN7hZHK4AKY3CBbZq9I8xG5lZH%2FhdpZZxyDqwgKfdiqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv2F2H%2BjDPZgHcIbQKtwD89jjQsbP74sf6lMt4MqtYlOqtEp9ME5AcBWXs5TAqc10Veji0xFIOHd1479uSpztjSBfZp0h6C3IDzVVMd4QqAdij7WXCLvSWXgDiLxNPS%2B7xYVCTyGQNU0XiSa4Cq5rCM6CLXYQ4oKaPd9aeilIDAC09x0A8L2%2F%2BP%2BY6eKrPZRwcFCHpLTCcmZfDqydDR55wpjMZeCvpEpB%2BnjFNJOYmZQv0viW%2BTP00JyZLYGMayXF1wPLddm%2B9Sp5oxFc7bMlENqjKOUg1PydjS3Oligo4jgcoXm2RQJTh%2FxHNG8Sb7J%2FnIQI21JWitQiF5qHXmm9rX2qQy6LOnqDe2th3E40%2Bc7%2FHyWkNgEpfUpKNbWt3W272myuR4duxGAwLHvJ4lCIP6geuVRZAo1svqyZ3gOsEzpVgEwCUU58qbzPHx30pvwcwXqX%2FBngvGyz1EVrCdFvbJPYkwwTJdyg85UMN4Zqs6BO6hYrg8lsdT3%2F3NINB3KwugAJ7u64%2FTm%2BNYQu%2BKuz%2FCGjglJ3eAZtgPKFJkiY7%2B%2FvognSbyIAIEMzeJyiX4HVWSb61GzXowIIsBEo3MbcT4eqFUNpHTIGqE8E3RYVpwcqaQciG4kZ5sMQV27PXCzzAUXnheTWOU75BK4w2qv4vAY6pgEcq9ELBLmEx4eWJigPJmpXwxhVVxrxTlNTwq12Zw7B2ti3btNlt19C5aodp7dqpS2%2BsQgRIXZxu4WO8YvT1hwTpJj%2B%2FeQt1JTu6Qz%2FSO%2BkTwORwPEl3FaJFkw4UQwy%2BZiS2mRHiEULwRC6O5rL6XIayUuNMVYEW%2BH0HY6EycVTAu9xpWfRazeEHgXMZwu%2F3p0Adf6G0Bq2RqdKwhI3UPgArECjvAXB&X-Amz-Signature=7a3d46ae88add7ecd3221aa2ca5a62ef2e9c9ab257a381a562aedb3091c65d29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=4f1a93dbf65c18ff8c2fde1dc7b28ca55420c8865b4473012d4b10b77f301c63&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=27149839c81954af9d7df297b39e970be0dbcfa212a35b1b4ce4fcde9b8ca8de&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=1c9fe053a7c5d168b413020cc3698cab0c7a130ebb6305c21ac987265f3d1729&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=6f8e16777277431aff21e0e57a9a1a560a5bdbe19c9a0aed90d27d6f4b924e0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=c9438ec0dc9f4b051f190c139a30a25245a733b4a3d5de780021653dd79d5161&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=4a61a3df638dd34a3a79477a509ea1290a89312e10a661ce482877b7abbb6f5d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQJCKMH3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHsxDs3ksNqjCXFcwPN3mkEEqDfZXg7w0us1Vis4KR%2FAIhAPOhOZWiMybFWHOFnF%2FnUJajQXcQfKYQ9mM2WjRUX4e1KogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwlm2ZIHw9puvXM6bMq3ANLMIhyvUwaiGUapUJ2Dh1QbMfip3fMkKyqSb4lmH1BbwC2hrPZ0i4NpBMideor8Aqx0pvsv1JXEU9IYDyYcZIBC%2FkxLVz8emNdZgg2cc5Ma4b71yUu8Be%2BadPOJmxGADNG8z4vPINoriLKIfbvp1kQa3MZf%2FMj%2BQJPUbR5DJq9VqzpsfILs6i4GGU%2B0lTvtsNbrnZ0znDo%2FhsiW%2B%2FlUj3ee0tKUybKneHJFapEBVOSD1CCoR%2B0uK62w2o1G2G9nVUHIMF00NKL7C2YmhjcJ8p6Ndr5Xa9yqCJh2fdPhPJfNP3bphY1ZrI2shHsIAGO%2BSTQMImi5WWAzGblmx58sxpZZFGozE30Z%2FKJM2F8DwNSYpTLT5iU%2FxT3W6ugi5bTh486saT2fYamJDlRVJ5vENW6O1nyGt4kEId%2FF8nIOB8Lq3YOEt5LcuhBWdIYXEuiwxxX33DQ2EqYubURXR5FX4%2FcAskWnqMybxSi21ba857xBfO39fDittgHLUG9KecYeJA5JTtCOrWIVNJ0y185NTwqWaMI%2BhPvfVdznRzFAThq%2Fn5ahCA7eqotqmdNFWKSuLEGyfWa9J0MZKglAzR%2Fru%2F2u%2BRvLURR2KeRjbs30Z480K4duf644C5bSGPK0jDZx%2Fi8BjqkAeyQzvX0obKL3FRRpDVy5fbFeAfs81vuSN8IkK1%2FrxYD4TH80cynUt8lCQT5WgDDDy2wXPSQfDipt7V%2F5eJ8OywAXU55anTDyE6Qy6IvtZXtgyM%2FK%2BalNG%2F85WjT19ILOaQJOWFxCnQ4w%2FRnD6wPlsk0mmBT1IPOV6oaG5tYoO8T%2FYS9HpbSO4OU7yMft3u98tobj%2FxiyK4%2Bxby4BbdQHkBNKAp7&X-Amz-Signature=4cdfcb18eba9bca21c644e187aaeab3fa1bbc81368436d0f04828a9d179828aa&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VETOHPJR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFvsUHvBwkliT%2F%2FUY%2FZtCajXN%2FDPc34Sh%2B7jReqxlamdAiEA%2FPBc%2FQb5fnbWoZiESB42%2FIg1xHSLQN%2FXuFgocCu8ehIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxm5vqX032HSlwvESrcA2N3PhwJEPlLDX6ICG2FdRWEjtg1xGV41wXph4qhuH0enblSILGVqnreKU3OfCv%2FBUzVUiaykX0sa7ZN6xTZODZccquLUKxx0tS%2B4moh17ysVC5Wm8PviuvGyxofvbJ2waQyeLeZ1oLmlUZ5GloOpL7dzCrPxEz3UChagsRGGX%2B33ony0xi80a1O377WMPsMRp20prjShlAD0Nce2QS1KydV21T9IZpo0CL5tg%2F%2Fu0aX%2BSo%2BhZoB2eXG3%2FTNiuTkcwF0gSFQ03UJW3mgahlonwZa7UW063yqKifebPL1IVVb1wLQw5y4eZUpSQDy5yLbfGQm7f%2B8zYA3ZMko9sCkqsEJ9lqgVdSBKO5J2n4BGU27B1Adr9QgKJlPDHd%2F6SL4Acuo6Iho%2BLE8xR0PeC3o%2BOVZX18hQtP7peF3W8a1%2BiE42lpMozSoMZBYrIL65c%2BguLLTC33v48UkPMuQEsfdNvyNJie5Hdn8lssC%2F7BBvK%2B%2FN5x%2FfnV8D94wjXhmmAKv2K3P%2FkMOT%2BPk5aNgvcjuCHlNk%2BxjTgAkPDH%2BQmU0NHRN%2FWxbHUaH0djcHDuCWC7nA5IaDwbCSRmsBg6NLun4hLpiCnLLWochyRikTqebIOBMGZO0%2FYBD9elBi7lpMOvD%2BLwGOqUBmLeHaAemPBcTITNoucRGKEXtCTYy%2BSJYCYkRImQpQZKWdPbOLCg1B7%2Bey0vsnnzsl63TrYbtOdFd%2FF1aeM3wOYVij4D3fHH1JGr1%2B0DMLxw5FlqZvpIc9kmoZ5XYgrvrYfWaqGH0OibJ0pyBSqFugERNMW6EWSGzIgD5th6Xo5DzhxEmr%2BZKjhR44Ln8IvcdBWkZhIwYI%2Bg4VF1vX7sf%2FxAR5LYj&X-Amz-Signature=17512edebbd5e6263d9d18ef9bf11b3a51b75e67b523120f7ed34c625e35358b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=b335d8df60984c0bfbf1e9529902a867caa4ec8878b18c5036e0f1504cb4df2c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=20310b180d78c4b595c58afe2170805342ab5d8a8939f0dce70457fe9cb53a5c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=40fc567d084ee19d51a199b23bdd5aaa90ce9c2cb76219e6d5ec4c1f77e9a467&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XRI2BXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJKIF0VAdfGxZv9r9GFf8WuPIMTKl30u7uJnwXAk01wAiA6tokoh%2F%2BW71l4D%2Bt7pBsa%2FDGih3U6AfaRzrGNnmn8LyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmRbDdjs5jtcH%2FC3tKtwDgs5it4J68iQ3Kn4LG%2Ba6YwR93nLxg%2Befydldkw%2FwK9lHiXzq8N4u1DpFhxZkYSGP%2FSpNsOUTX%2F2BmLBRgu%2BYxnmraD3vew2PrGVzalIfKm%2B8i%2F%2BubKm3m3movZQ2vLH%2B8FFG5wdqRz5IHRuRHCfQBWW7fyMKrbRJ9RhURUYh8Q%2BTSOTaJqIOHxY8nbhrjjIfSDCG1ETIyBMF%2Fq9xGqA2fxcTebpTaRgbARh9%2BrnU1UZW1%2FQK%2BWcXD%2BqFomwVk7TKnsjktOPJa4mcShFfnEGehSLhNmyfcLSRNv80jIWcw32v2QjCEdFl9LV%2Brhafac8i5r9YkDN6Y5Jt%2B1sgdRP1SPYwPaAnhGDhEShPp0IkW29WZFsj54EY69bJ6dBPlDqI8dmNuIPGgjsAF99OwfSS5bvWLEJNF%2Bhm1e64n%2BrEXu8LC5dmTTCf4Aa4tP61h22ZCABij84OKuhmo2uVGQsnAgMH4McU%2FKsxSPbGUH4ezdRmaWhoFYevhFV7UwGW25Tp1e%2F0ncoDT6ullnZG%2FGrapxAiY%2F%2BHBmJXzZ805ImYI7szid7r%2FUQ2UdTg%2Fs7oJ2Z%2BiokpvmJBqzUth5s1APKPtwpc2CEHHXTNdJZXX%2BpRcPXVj06DoH5df5b4xOww5Mf4vAY6pgGlzGwdrFqrKwanxmAo7KYquEOnmqa%2B6wG0C0Dj3bZJBp2SyfG6QdV68zLwJla%2FTFiG5gXHt9KlWtbFuDiaJAQt6vdGByN8IlB7ZGVzlq1L3dF0Y%2F9zd2XOYd%2BsyeRjziY8bIE1nYBIOl6a4iiB8C2mjlzD3EoyQYb2vpqSvEUiVpG3ByEJOv46xh37VkhqydYdih%2Bn3bUa3fVZ047QZnlVNiT80zGG&X-Amz-Signature=347f7ecacf38dde882194f815dadede9edb840d520dfec1b115d4080a844e9b4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TXH7S76%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHh0k%2BVeZVg2nhBpNMHnaKzdQLEjYJccvccxyfMOcnymAiBpVIdNlmSpknYCgJiMeD9GuTHNfiqpnDjPPojQh1WATCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTsvONh2y%2FyzmtfGnKtwDQRmjZ3g2KFbf5%2B0T7ZHwtdiB9h305rWQihaPcJ%2F%2Ff9NqD1EI4RWsQkEElEtpvRUTxzz2ayWFtWU2TXiIKwl8v2ii%2BsyaJiYKCF7jr45sYF3V3tf5FrBdD9%2Bi%2B%2Br2gs%2FO%2F41tFcGfUC6%2FL0FthZqi63fIoPqDlOIwcig7VWwaqwoWcdAbsEEiHYIL9FnkWPFAcZopB95xjS09s6SpQpkpq4gq1xEEuRHH6JWCa%2B2vHHiXol%2F1Bz7L0F%2FDLbrgRU9kOgGg0V0sIbcXgenhJGMzE09hDnqTlpgEfQLi548PLVInKODYOFEH%2FbHJ2ErNRvfpzlYYofnPsBG3sK7X5n6Xp3lZUOhD4o7l%2BfULZWYtQKBj1qa%2BsFV5tAS9RrDL2ArvoIjtgd8Fs7PxeMZquu1SPEr8z3rGWgZTwDuEDqecEv%2BqxB%2FpSa%2FKjSqyaa1wHI0t0j7gg0C9B9P0tpCy1HvLOUXr6GxrafqnUuDgqBx220Ki7TLtopaFilQBXp0TCh5PsCJuXeNjCazdDw38FEacEvdZ0%2Fp8lzcnnh2vm%2BOlL3M%2FF8rkTZM8WQPDSFTnqqqkYKMMkJkjyde3vWO5QJ2YHpsrlPa0hmSq6RQTMCXybBZvH99D1ZpCTXaINCkwgML4vAY6pgEtpeRq28EY1fqWLmCJQYocN%2BXQPJeAOWe3ksIJnGwjqy%2FcLFMBlpA5Sp0Nc40mCxZItC%2BSV6oMBf4tfsm5liNTHmV8CrZ63uneRQQ%2BmoyQXhis%2BupLWmHA%2BIWP041HK560rWks%2BuQlz0CMURHDe8C570P8XO%2FuvD7z6wc%2BvQhHRc6yixmzpIYKnwmRjScexH39B9ibbatk8jI8cJO6Kk5RUBzU3%2Brz&X-Amz-Signature=52a1c4cfb7b99a17c07db310e751046ea484ee3ec30a0e560c6418747473b07a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNCVJCQE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKc%2FjjwmphmcRrFdGr%2B5Xef6JkLzIneejFYstRRfqv0wIgBA74McCpgtzF2hO%2BPBVhYsjfsk7ryTfeOs5sF4gKtqoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHQ74foM5RRjlmS0kCrcA7q3r54hcmzNE%2BL25DVIyFSh4Fw%2BxnW21Qw7TDYCr0odcGnuaSLBcIwJEdxJ4g6dntymfT4fYathSVZYsMwWdLAxUKbml73Wfgl%2FYk7Yv2FELito4R57m9mo7gT67cQXS5ZzXMDAton0lMF8F7n8LMtQRhWj7aTZF6Lw6pba5F8RdnEJxJVmTPAfKwDPvwFWtq%2Fi%2BifGL9nMlySG1aAichvXc7eUw9cueYaMwhKMCOK4b6T9uQ6eg1xHfcCiPFxmoLq8afZMQGX2F23Y32j6X9AWQrDEZ9OT8QDkVgRg5I7CR%2FmnU2WIrM0xks%2Bi4JEWtdgwAnQzhzHvov2g2pfAtnMUcgqENxlXm9KwSthO28h%2B3KN6YhW%2FkY5k%2BjtGocjOCdRvBeCQBjv%2BKry8ynq5nsI6%2Fi0EI3kJMGsHb%2FqCb32LtjZFpFa9YietwCPy3rvg%2BdzvxtJhPg8%2FuieXMvcgpf7q6mwsyZ7sYz5RGiWSOn4VWvnSIqfm%2F52jrdbGqdQed7vB78RRcPn8EHQWGQ7hYjYJrQzLsRLjqdwSicMd9Fiu0ShP5E2GX8Hw3FFVz%2FzPqL6G0Gb6l%2F1WHvnV3SD%2FIz3u9qtkKs6VEczlZcvsZpzIy61ik6TJF7klZtOEMNrH%2BLwGOqUB2WCFI8ctdniWDNRL6DxlHr3u%2Bxdxn5bOJSTkT%2Bx%2BaMS%2FeOmV7S9hV3ajgyhUbvjMuGYLCLnZ3G%2FoFJqF2SNPoqWrl2RqtptnZ6BpYHYD8SSifvy2UyI2KwAEo6dGWHWUoSqQly6ZfWEpbtjIA89UBeJYqh%2F%2BoNQ7jPnOmCdgohqNgogP1fYDXZgOSAENSc4%2FXy28eG8Y7WjcmWrHvKI3i9dnjVa3&X-Amz-Signature=e56e1cf6c931b565260b80d43ae0a743283e4e9242463b4e5d45f514ed55d9c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQJCKMH3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHsxDs3ksNqjCXFcwPN3mkEEqDfZXg7w0us1Vis4KR%2FAIhAPOhOZWiMybFWHOFnF%2FnUJajQXcQfKYQ9mM2WjRUX4e1KogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwlm2ZIHw9puvXM6bMq3ANLMIhyvUwaiGUapUJ2Dh1QbMfip3fMkKyqSb4lmH1BbwC2hrPZ0i4NpBMideor8Aqx0pvsv1JXEU9IYDyYcZIBC%2FkxLVz8emNdZgg2cc5Ma4b71yUu8Be%2BadPOJmxGADNG8z4vPINoriLKIfbvp1kQa3MZf%2FMj%2BQJPUbR5DJq9VqzpsfILs6i4GGU%2B0lTvtsNbrnZ0znDo%2FhsiW%2B%2FlUj3ee0tKUybKneHJFapEBVOSD1CCoR%2B0uK62w2o1G2G9nVUHIMF00NKL7C2YmhjcJ8p6Ndr5Xa9yqCJh2fdPhPJfNP3bphY1ZrI2shHsIAGO%2BSTQMImi5WWAzGblmx58sxpZZFGozE30Z%2FKJM2F8DwNSYpTLT5iU%2FxT3W6ugi5bTh486saT2fYamJDlRVJ5vENW6O1nyGt4kEId%2FF8nIOB8Lq3YOEt5LcuhBWdIYXEuiwxxX33DQ2EqYubURXR5FX4%2FcAskWnqMybxSi21ba857xBfO39fDittgHLUG9KecYeJA5JTtCOrWIVNJ0y185NTwqWaMI%2BhPvfVdznRzFAThq%2Fn5ahCA7eqotqmdNFWKSuLEGyfWa9J0MZKglAzR%2Fru%2F2u%2BRvLURR2KeRjbs30Z480K4duf644C5bSGPK0jDZx%2Fi8BjqkAeyQzvX0obKL3FRRpDVy5fbFeAfs81vuSN8IkK1%2FrxYD4TH80cynUt8lCQT5WgDDDy2wXPSQfDipt7V%2F5eJ8OywAXU55anTDyE6Qy6IvtZXtgyM%2FK%2BalNG%2F85WjT19ILOaQJOWFxCnQ4w%2FRnD6wPlsk0mmBT1IPOV6oaG5tYoO8T%2FYS9HpbSO4OU7yMft3u98tobj%2FxiyK4%2Bxby4BbdQHkBNKAp7&X-Amz-Signature=ab6cfa97dc8bed5a34c83bf1e593f65f6b8a8831d810b795c4bc8ecc244eb093&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQJCKMH3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHsxDs3ksNqjCXFcwPN3mkEEqDfZXg7w0us1Vis4KR%2FAIhAPOhOZWiMybFWHOFnF%2FnUJajQXcQfKYQ9mM2WjRUX4e1KogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwlm2ZIHw9puvXM6bMq3ANLMIhyvUwaiGUapUJ2Dh1QbMfip3fMkKyqSb4lmH1BbwC2hrPZ0i4NpBMideor8Aqx0pvsv1JXEU9IYDyYcZIBC%2FkxLVz8emNdZgg2cc5Ma4b71yUu8Be%2BadPOJmxGADNG8z4vPINoriLKIfbvp1kQa3MZf%2FMj%2BQJPUbR5DJq9VqzpsfILs6i4GGU%2B0lTvtsNbrnZ0znDo%2FhsiW%2B%2FlUj3ee0tKUybKneHJFapEBVOSD1CCoR%2B0uK62w2o1G2G9nVUHIMF00NKL7C2YmhjcJ8p6Ndr5Xa9yqCJh2fdPhPJfNP3bphY1ZrI2shHsIAGO%2BSTQMImi5WWAzGblmx58sxpZZFGozE30Z%2FKJM2F8DwNSYpTLT5iU%2FxT3W6ugi5bTh486saT2fYamJDlRVJ5vENW6O1nyGt4kEId%2FF8nIOB8Lq3YOEt5LcuhBWdIYXEuiwxxX33DQ2EqYubURXR5FX4%2FcAskWnqMybxSi21ba857xBfO39fDittgHLUG9KecYeJA5JTtCOrWIVNJ0y185NTwqWaMI%2BhPvfVdznRzFAThq%2Fn5ahCA7eqotqmdNFWKSuLEGyfWa9J0MZKglAzR%2Fru%2F2u%2BRvLURR2KeRjbs30Z480K4duf644C5bSGPK0jDZx%2Fi8BjqkAeyQzvX0obKL3FRRpDVy5fbFeAfs81vuSN8IkK1%2FrxYD4TH80cynUt8lCQT5WgDDDy2wXPSQfDipt7V%2F5eJ8OywAXU55anTDyE6Qy6IvtZXtgyM%2FK%2BalNG%2F85WjT19ILOaQJOWFxCnQ4w%2FRnD6wPlsk0mmBT1IPOV6oaG5tYoO8T%2FYS9HpbSO4OU7yMft3u98tobj%2FxiyK4%2Bxby4BbdQHkBNKAp7&X-Amz-Signature=4043b4513afcd09854a4635f3ab5a5218bcca393a817cbee091ba2cef1a5453c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
