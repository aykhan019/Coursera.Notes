

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOTG2YMD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCICrQkjHQ%2BNAXcqGk3XWFM6xpNKcYP8%2FnvHIHXTICVmfXAiBjWviuY4ermlG4MFzGhti%2BDbOzOhebFoZ771Xkqb2lIir%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMTj6GK6ppT9Omeo%2FcKtwDzfSpvaBG%2F7GibqDO6O0NQ6Ue3HV664BeUHuJE9HEtEXkhCofrtNFUupoLMhvQkEdk68TXNZH0U6%2FFJayQnoP%2Fg8lMMoozUb1Pj72aaXBg5G%2BBYjVyu32RuwkN9uySkseeeN6LefTeKk%2BQr2a6U7yQW9nmZHxD5p8FowPLm4DdobD2iR%2BnHAWbhCIJgoPfYvrTcs6L1ikoKyUoW4rBWMl4FjxExMu8X7HBSRc%2FgH3rddElhzDLoVOsyPdvrOhX5%2FqvnDOTMpurvUvehmmFMiCQKA3DbkuNY2TJ4SIoFztu%2BG8Pn20HjSDqXuhjPhL0eOeifmLLopIAXiyh1dXyACKh2dLklBvx6M%2BrDGlipl0qoofu4bhgmVksB8mHNohC5NXNPgL7gUtXDyDnkEE17wU3W2RQA6ayHoNr2REKsQHxnvvPmHShghgsXkQeRfw1%2FtsYd2oT6SAig4BdUPfrd2pl4Kbt6Ds6i5WfJWZkmwFnAyCuxwai8FYBWwM8d8qC4Jm6L7qyoUbSk0ZGiN9ssPmPBphOiTWDIBmDqjVrFjGxF0oE%2BIHk9Oo%2FkJNXU5sbEDUJTtMNjAS%2Fb1gGpeiWQdRrun3hZvSlQOFv1h2AV90wmouzFHd0k9ANZD2gDYwxpyTvQY6pgHO0FStePctkhKs2QlRfvW6ygl5P%2FDGUb1CpTdmDPXHA3uyZ4v%2FQaB%2BLWBF83yiHM8%2B%2BC9W6reYYospvo1TNUR0hSptl2jQDRyBhFnD69Vmpy3Sfe1kibYUPoU0FjHXTMZIR%2FzgWsVhqCMjZgSyJIlp4kNlB1VKdITIokNEyYbWmH5XjSjAVyi3rrl4EwQbKOpeCeAd0FpOW%2FbXxBxpEK2ZZLmJoBa5&X-Amz-Signature=0b879e55519fed5fdd9953adc175c45d0e7175f170822a740f7936822dded9bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOTG2YMD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCICrQkjHQ%2BNAXcqGk3XWFM6xpNKcYP8%2FnvHIHXTICVmfXAiBjWviuY4ermlG4MFzGhti%2BDbOzOhebFoZ771Xkqb2lIir%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMTj6GK6ppT9Omeo%2FcKtwDzfSpvaBG%2F7GibqDO6O0NQ6Ue3HV664BeUHuJE9HEtEXkhCofrtNFUupoLMhvQkEdk68TXNZH0U6%2FFJayQnoP%2Fg8lMMoozUb1Pj72aaXBg5G%2BBYjVyu32RuwkN9uySkseeeN6LefTeKk%2BQr2a6U7yQW9nmZHxD5p8FowPLm4DdobD2iR%2BnHAWbhCIJgoPfYvrTcs6L1ikoKyUoW4rBWMl4FjxExMu8X7HBSRc%2FgH3rddElhzDLoVOsyPdvrOhX5%2FqvnDOTMpurvUvehmmFMiCQKA3DbkuNY2TJ4SIoFztu%2BG8Pn20HjSDqXuhjPhL0eOeifmLLopIAXiyh1dXyACKh2dLklBvx6M%2BrDGlipl0qoofu4bhgmVksB8mHNohC5NXNPgL7gUtXDyDnkEE17wU3W2RQA6ayHoNr2REKsQHxnvvPmHShghgsXkQeRfw1%2FtsYd2oT6SAig4BdUPfrd2pl4Kbt6Ds6i5WfJWZkmwFnAyCuxwai8FYBWwM8d8qC4Jm6L7qyoUbSk0ZGiN9ssPmPBphOiTWDIBmDqjVrFjGxF0oE%2BIHk9Oo%2FkJNXU5sbEDUJTtMNjAS%2Fb1gGpeiWQdRrun3hZvSlQOFv1h2AV90wmouzFHd0k9ANZD2gDYwxpyTvQY6pgHO0FStePctkhKs2QlRfvW6ygl5P%2FDGUb1CpTdmDPXHA3uyZ4v%2FQaB%2BLWBF83yiHM8%2B%2BC9W6reYYospvo1TNUR0hSptl2jQDRyBhFnD69Vmpy3Sfe1kibYUPoU0FjHXTMZIR%2FzgWsVhqCMjZgSyJIlp4kNlB1VKdITIokNEyYbWmH5XjSjAVyi3rrl4EwQbKOpeCeAd0FpOW%2FbXxBxpEK2ZZLmJoBa5&X-Amz-Signature=d9cfbce071a7ed34138807de2ee5e604bff79fa812ddc1dd8d2308691549ed22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOTG2YMD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCICrQkjHQ%2BNAXcqGk3XWFM6xpNKcYP8%2FnvHIHXTICVmfXAiBjWviuY4ermlG4MFzGhti%2BDbOzOhebFoZ771Xkqb2lIir%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMTj6GK6ppT9Omeo%2FcKtwDzfSpvaBG%2F7GibqDO6O0NQ6Ue3HV664BeUHuJE9HEtEXkhCofrtNFUupoLMhvQkEdk68TXNZH0U6%2FFJayQnoP%2Fg8lMMoozUb1Pj72aaXBg5G%2BBYjVyu32RuwkN9uySkseeeN6LefTeKk%2BQr2a6U7yQW9nmZHxD5p8FowPLm4DdobD2iR%2BnHAWbhCIJgoPfYvrTcs6L1ikoKyUoW4rBWMl4FjxExMu8X7HBSRc%2FgH3rddElhzDLoVOsyPdvrOhX5%2FqvnDOTMpurvUvehmmFMiCQKA3DbkuNY2TJ4SIoFztu%2BG8Pn20HjSDqXuhjPhL0eOeifmLLopIAXiyh1dXyACKh2dLklBvx6M%2BrDGlipl0qoofu4bhgmVksB8mHNohC5NXNPgL7gUtXDyDnkEE17wU3W2RQA6ayHoNr2REKsQHxnvvPmHShghgsXkQeRfw1%2FtsYd2oT6SAig4BdUPfrd2pl4Kbt6Ds6i5WfJWZkmwFnAyCuxwai8FYBWwM8d8qC4Jm6L7qyoUbSk0ZGiN9ssPmPBphOiTWDIBmDqjVrFjGxF0oE%2BIHk9Oo%2FkJNXU5sbEDUJTtMNjAS%2Fb1gGpeiWQdRrun3hZvSlQOFv1h2AV90wmouzFHd0k9ANZD2gDYwxpyTvQY6pgHO0FStePctkhKs2QlRfvW6ygl5P%2FDGUb1CpTdmDPXHA3uyZ4v%2FQaB%2BLWBF83yiHM8%2B%2BC9W6reYYospvo1TNUR0hSptl2jQDRyBhFnD69Vmpy3Sfe1kibYUPoU0FjHXTMZIR%2FzgWsVhqCMjZgSyJIlp4kNlB1VKdITIokNEyYbWmH5XjSjAVyi3rrl4EwQbKOpeCeAd0FpOW%2FbXxBxpEK2ZZLmJoBa5&X-Amz-Signature=d7fdfd36a15cb698bf20ec206bcc72be2530684eceab93bedbf3802fe3dab04c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZPTTPPA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDOK9NgwexkMB%2FqUWkmbHaTyjU%2FmB1%2BMGd2pb9dBjaIZQIhAJ6YpI3ntmz3lxxnuxCz3mdi0XxdyL62fW123K4zKi%2FIKv8DCGAQABoMNjM3NDIzMTgzODA1IgxRAxGVLypW%2B9KJI68q3APdx%2Bh7Xs4fvbT8c6EhEE8culfRrtrqjLsok6hkzVz8RpaC63NwzRUtHHfKjovtoI0xSCKLV2O3Mhu8kRtuIi%2BUfVVHlB%2FqQPArHdQXs5Yo%2BGlkW8GQN30o8pNnAW4lSuy0HI97S6%2FVnti1s209dSW7%2BLM2BjNXwhvuzfnrVhl3l8izKPRfcao9SKqrQL%2BGLGr5vU1TCFm7GE77b0CTlF8aBwRLvnR5Iyw2nwCJzXQuKFzyhe4uP%2Fl7pe%2Bz1AQCL%2FCx%2BaJ5GUboY8WqYlu6SU1U8jKUodyHnPP%2BsW7JZoT%2FVAYyFFDf5ae8jzDEDVEB70YfMD6QP5Wu6pVMp3teOZt2dEV6W7226208vtlnvqp%2BXCd4WcLnWade0htc%2Bq62q62wi1j7jPTvAWcfE3V8LJAby%2BIMd8JitR2DD4YKInFnuGMukxjQXA%2BsLGH7wLvWI4te%2BdzPf7nrEwyQ5Gwzh89VxvWKCfHZJI5QXEAXP8fR%2F29ZfuJLWs2m3BRLO4lNhesvvMCi2hmOBGZZl1sqfqe5bgEw6uOagRlW9FRaeexmFvnHEB06DqH8AL3xxDI%2BGVpDq8gnkXwtWsmLfcnMaAbxolCUdEBpvjJLCXhEPxVIPnkGLND1cvOrEdzIIzCDnJO9BjqkASdOucE3y4dUp6iVQppJU1YH2itG%2By0om9PcGUItStHC1%2BkeWOyMy3CENYtnn1YGgjlLzsBjcMGsASPY%2BcEDYtrWHjN4IvaxeCVugMRxzrqwhOVKxqrAUr3PuW5JJrZ%2FX9R5UebjYAcuMYw5xUrsyxxggG1tKMdQh%2BofvgFVe97n2oYu2N08LX1sP5y2W%2FiVbHsFJJeZaTKqh8UvMlR9UkDCbV7U&X-Amz-Signature=ecd171a3cb0ce02bb33e3143b383ead407127af29019a26761ea6fa79f20650a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZPTTPPA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDOK9NgwexkMB%2FqUWkmbHaTyjU%2FmB1%2BMGd2pb9dBjaIZQIhAJ6YpI3ntmz3lxxnuxCz3mdi0XxdyL62fW123K4zKi%2FIKv8DCGAQABoMNjM3NDIzMTgzODA1IgxRAxGVLypW%2B9KJI68q3APdx%2Bh7Xs4fvbT8c6EhEE8culfRrtrqjLsok6hkzVz8RpaC63NwzRUtHHfKjovtoI0xSCKLV2O3Mhu8kRtuIi%2BUfVVHlB%2FqQPArHdQXs5Yo%2BGlkW8GQN30o8pNnAW4lSuy0HI97S6%2FVnti1s209dSW7%2BLM2BjNXwhvuzfnrVhl3l8izKPRfcao9SKqrQL%2BGLGr5vU1TCFm7GE77b0CTlF8aBwRLvnR5Iyw2nwCJzXQuKFzyhe4uP%2Fl7pe%2Bz1AQCL%2FCx%2BaJ5GUboY8WqYlu6SU1U8jKUodyHnPP%2BsW7JZoT%2FVAYyFFDf5ae8jzDEDVEB70YfMD6QP5Wu6pVMp3teOZt2dEV6W7226208vtlnvqp%2BXCd4WcLnWade0htc%2Bq62q62wi1j7jPTvAWcfE3V8LJAby%2BIMd8JitR2DD4YKInFnuGMukxjQXA%2BsLGH7wLvWI4te%2BdzPf7nrEwyQ5Gwzh89VxvWKCfHZJI5QXEAXP8fR%2F29ZfuJLWs2m3BRLO4lNhesvvMCi2hmOBGZZl1sqfqe5bgEw6uOagRlW9FRaeexmFvnHEB06DqH8AL3xxDI%2BGVpDq8gnkXwtWsmLfcnMaAbxolCUdEBpvjJLCXhEPxVIPnkGLND1cvOrEdzIIzCDnJO9BjqkASdOucE3y4dUp6iVQppJU1YH2itG%2By0om9PcGUItStHC1%2BkeWOyMy3CENYtnn1YGgjlLzsBjcMGsASPY%2BcEDYtrWHjN4IvaxeCVugMRxzrqwhOVKxqrAUr3PuW5JJrZ%2FX9R5UebjYAcuMYw5xUrsyxxggG1tKMdQh%2BofvgFVe97n2oYu2N08LX1sP5y2W%2FiVbHsFJJeZaTKqh8UvMlR9UkDCbV7U&X-Amz-Signature=88c53e9739074103c4cacd9c09ff0bdb06111cb428d536a3c2c4bed55cfc4879&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZPTTPPA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDOK9NgwexkMB%2FqUWkmbHaTyjU%2FmB1%2BMGd2pb9dBjaIZQIhAJ6YpI3ntmz3lxxnuxCz3mdi0XxdyL62fW123K4zKi%2FIKv8DCGAQABoMNjM3NDIzMTgzODA1IgxRAxGVLypW%2B9KJI68q3APdx%2Bh7Xs4fvbT8c6EhEE8culfRrtrqjLsok6hkzVz8RpaC63NwzRUtHHfKjovtoI0xSCKLV2O3Mhu8kRtuIi%2BUfVVHlB%2FqQPArHdQXs5Yo%2BGlkW8GQN30o8pNnAW4lSuy0HI97S6%2FVnti1s209dSW7%2BLM2BjNXwhvuzfnrVhl3l8izKPRfcao9SKqrQL%2BGLGr5vU1TCFm7GE77b0CTlF8aBwRLvnR5Iyw2nwCJzXQuKFzyhe4uP%2Fl7pe%2Bz1AQCL%2FCx%2BaJ5GUboY8WqYlu6SU1U8jKUodyHnPP%2BsW7JZoT%2FVAYyFFDf5ae8jzDEDVEB70YfMD6QP5Wu6pVMp3teOZt2dEV6W7226208vtlnvqp%2BXCd4WcLnWade0htc%2Bq62q62wi1j7jPTvAWcfE3V8LJAby%2BIMd8JitR2DD4YKInFnuGMukxjQXA%2BsLGH7wLvWI4te%2BdzPf7nrEwyQ5Gwzh89VxvWKCfHZJI5QXEAXP8fR%2F29ZfuJLWs2m3BRLO4lNhesvvMCi2hmOBGZZl1sqfqe5bgEw6uOagRlW9FRaeexmFvnHEB06DqH8AL3xxDI%2BGVpDq8gnkXwtWsmLfcnMaAbxolCUdEBpvjJLCXhEPxVIPnkGLND1cvOrEdzIIzCDnJO9BjqkASdOucE3y4dUp6iVQppJU1YH2itG%2By0om9PcGUItStHC1%2BkeWOyMy3CENYtnn1YGgjlLzsBjcMGsASPY%2BcEDYtrWHjN4IvaxeCVugMRxzrqwhOVKxqrAUr3PuW5JJrZ%2FX9R5UebjYAcuMYw5xUrsyxxggG1tKMdQh%2BofvgFVe97n2oYu2N08LX1sP5y2W%2FiVbHsFJJeZaTKqh8UvMlR9UkDCbV7U&X-Amz-Signature=07f8e888219d05326c37006b2022a8c31907b984ad3c647cd021a98e53f3ab4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZPTTPPA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDOK9NgwexkMB%2FqUWkmbHaTyjU%2FmB1%2BMGd2pb9dBjaIZQIhAJ6YpI3ntmz3lxxnuxCz3mdi0XxdyL62fW123K4zKi%2FIKv8DCGAQABoMNjM3NDIzMTgzODA1IgxRAxGVLypW%2B9KJI68q3APdx%2Bh7Xs4fvbT8c6EhEE8culfRrtrqjLsok6hkzVz8RpaC63NwzRUtHHfKjovtoI0xSCKLV2O3Mhu8kRtuIi%2BUfVVHlB%2FqQPArHdQXs5Yo%2BGlkW8GQN30o8pNnAW4lSuy0HI97S6%2FVnti1s209dSW7%2BLM2BjNXwhvuzfnrVhl3l8izKPRfcao9SKqrQL%2BGLGr5vU1TCFm7GE77b0CTlF8aBwRLvnR5Iyw2nwCJzXQuKFzyhe4uP%2Fl7pe%2Bz1AQCL%2FCx%2BaJ5GUboY8WqYlu6SU1U8jKUodyHnPP%2BsW7JZoT%2FVAYyFFDf5ae8jzDEDVEB70YfMD6QP5Wu6pVMp3teOZt2dEV6W7226208vtlnvqp%2BXCd4WcLnWade0htc%2Bq62q62wi1j7jPTvAWcfE3V8LJAby%2BIMd8JitR2DD4YKInFnuGMukxjQXA%2BsLGH7wLvWI4te%2BdzPf7nrEwyQ5Gwzh89VxvWKCfHZJI5QXEAXP8fR%2F29ZfuJLWs2m3BRLO4lNhesvvMCi2hmOBGZZl1sqfqe5bgEw6uOagRlW9FRaeexmFvnHEB06DqH8AL3xxDI%2BGVpDq8gnkXwtWsmLfcnMaAbxolCUdEBpvjJLCXhEPxVIPnkGLND1cvOrEdzIIzCDnJO9BjqkASdOucE3y4dUp6iVQppJU1YH2itG%2By0om9PcGUItStHC1%2BkeWOyMy3CENYtnn1YGgjlLzsBjcMGsASPY%2BcEDYtrWHjN4IvaxeCVugMRxzrqwhOVKxqrAUr3PuW5JJrZ%2FX9R5UebjYAcuMYw5xUrsyxxggG1tKMdQh%2BofvgFVe97n2oYu2N08LX1sP5y2W%2FiVbHsFJJeZaTKqh8UvMlR9UkDCbV7U&X-Amz-Signature=64ec2b499ea1ceb9485e09294bebf8bf2bf2753f099ebd503505353a4480e0b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZPTTPPA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDOK9NgwexkMB%2FqUWkmbHaTyjU%2FmB1%2BMGd2pb9dBjaIZQIhAJ6YpI3ntmz3lxxnuxCz3mdi0XxdyL62fW123K4zKi%2FIKv8DCGAQABoMNjM3NDIzMTgzODA1IgxRAxGVLypW%2B9KJI68q3APdx%2Bh7Xs4fvbT8c6EhEE8culfRrtrqjLsok6hkzVz8RpaC63NwzRUtHHfKjovtoI0xSCKLV2O3Mhu8kRtuIi%2BUfVVHlB%2FqQPArHdQXs5Yo%2BGlkW8GQN30o8pNnAW4lSuy0HI97S6%2FVnti1s209dSW7%2BLM2BjNXwhvuzfnrVhl3l8izKPRfcao9SKqrQL%2BGLGr5vU1TCFm7GE77b0CTlF8aBwRLvnR5Iyw2nwCJzXQuKFzyhe4uP%2Fl7pe%2Bz1AQCL%2FCx%2BaJ5GUboY8WqYlu6SU1U8jKUodyHnPP%2BsW7JZoT%2FVAYyFFDf5ae8jzDEDVEB70YfMD6QP5Wu6pVMp3teOZt2dEV6W7226208vtlnvqp%2BXCd4WcLnWade0htc%2Bq62q62wi1j7jPTvAWcfE3V8LJAby%2BIMd8JitR2DD4YKInFnuGMukxjQXA%2BsLGH7wLvWI4te%2BdzPf7nrEwyQ5Gwzh89VxvWKCfHZJI5QXEAXP8fR%2F29ZfuJLWs2m3BRLO4lNhesvvMCi2hmOBGZZl1sqfqe5bgEw6uOagRlW9FRaeexmFvnHEB06DqH8AL3xxDI%2BGVpDq8gnkXwtWsmLfcnMaAbxolCUdEBpvjJLCXhEPxVIPnkGLND1cvOrEdzIIzCDnJO9BjqkASdOucE3y4dUp6iVQppJU1YH2itG%2By0om9PcGUItStHC1%2BkeWOyMy3CENYtnn1YGgjlLzsBjcMGsASPY%2BcEDYtrWHjN4IvaxeCVugMRxzrqwhOVKxqrAUr3PuW5JJrZ%2FX9R5UebjYAcuMYw5xUrsyxxggG1tKMdQh%2BofvgFVe97n2oYu2N08LX1sP5y2W%2FiVbHsFJJeZaTKqh8UvMlR9UkDCbV7U&X-Amz-Signature=5f37fee6a6a1cf6a758a5fce3f27ab53d1c804a30f9e02a12a41b6bf51b7854a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZPTTPPA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDOK9NgwexkMB%2FqUWkmbHaTyjU%2FmB1%2BMGd2pb9dBjaIZQIhAJ6YpI3ntmz3lxxnuxCz3mdi0XxdyL62fW123K4zKi%2FIKv8DCGAQABoMNjM3NDIzMTgzODA1IgxRAxGVLypW%2B9KJI68q3APdx%2Bh7Xs4fvbT8c6EhEE8culfRrtrqjLsok6hkzVz8RpaC63NwzRUtHHfKjovtoI0xSCKLV2O3Mhu8kRtuIi%2BUfVVHlB%2FqQPArHdQXs5Yo%2BGlkW8GQN30o8pNnAW4lSuy0HI97S6%2FVnti1s209dSW7%2BLM2BjNXwhvuzfnrVhl3l8izKPRfcao9SKqrQL%2BGLGr5vU1TCFm7GE77b0CTlF8aBwRLvnR5Iyw2nwCJzXQuKFzyhe4uP%2Fl7pe%2Bz1AQCL%2FCx%2BaJ5GUboY8WqYlu6SU1U8jKUodyHnPP%2BsW7JZoT%2FVAYyFFDf5ae8jzDEDVEB70YfMD6QP5Wu6pVMp3teOZt2dEV6W7226208vtlnvqp%2BXCd4WcLnWade0htc%2Bq62q62wi1j7jPTvAWcfE3V8LJAby%2BIMd8JitR2DD4YKInFnuGMukxjQXA%2BsLGH7wLvWI4te%2BdzPf7nrEwyQ5Gwzh89VxvWKCfHZJI5QXEAXP8fR%2F29ZfuJLWs2m3BRLO4lNhesvvMCi2hmOBGZZl1sqfqe5bgEw6uOagRlW9FRaeexmFvnHEB06DqH8AL3xxDI%2BGVpDq8gnkXwtWsmLfcnMaAbxolCUdEBpvjJLCXhEPxVIPnkGLND1cvOrEdzIIzCDnJO9BjqkASdOucE3y4dUp6iVQppJU1YH2itG%2By0om9PcGUItStHC1%2BkeWOyMy3CENYtnn1YGgjlLzsBjcMGsASPY%2BcEDYtrWHjN4IvaxeCVugMRxzrqwhOVKxqrAUr3PuW5JJrZ%2FX9R5UebjYAcuMYw5xUrsyxxggG1tKMdQh%2BofvgFVe97n2oYu2N08LX1sP5y2W%2FiVbHsFJJeZaTKqh8UvMlR9UkDCbV7U&X-Amz-Signature=7df3c0b97358e0cfdfe48fc4a4975a5e01e68a756cfcf5e9b896da0c7117dc69&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636G5E3CH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIBYe%2BWLU1oa2v5NcyL5yOfBW5Yz3L5PoQvgtSoPSijcDAiBaQUiJ%2BHnuWMoCrAwo9UVA7XzM59PZlA12nmK0UGcs%2Byr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIM%2BVSir6FV8I4hNJvKKtwDUbt0vM2raXlcMAflRDsz9FTnFwG%2FKz%2Fg9U0cJ2X2yHUGCO3vcOfthx%2FZtwxH4hyC0Z6bhvOzB9rnbi8AS2wMue4SmtqDX3E8%2BHq3Oo3bmCyRo17koeQi14VTMoPRLAMkRcJ%2FkBLN7iZRoqMfN6tpklUx9lV1I%2Fva8Y49q6ZokepxKdOn%2FyB8ASVgoY8wMb6dB3NF9GeSQxXU87vsvhVbDNTDvH%2Biw5bzHiZrRYTL3RUW%2BbUD8qSXRjZLAnne5oapylwK8YcF3pZ8WIwuWPwCEObJj736v9quPRmkMIOf8EPYez%2Bcyy6VONoNNsbeHfxjiQ%2FoS4TcPW8dUnPWxELhTzKErJ5zQx7yTe7gRjb6R8sigpBqdBsJOVogpcxZyqF0WYa0ATM5fiXHVWU6kSxnISuQQ1vwnKFgKVdwkqaXPLjRUTkaSLbxxQga89iF%2Bv%2B22xoVz038UNwGXLF2UxnEUUygnEMDroKgVwk3kYkvXi6KWVPkljVifzwV3vmCurcsoRcgvGAKz678C0szfixnCBH0hvzPtgA5koYjALgYcrZG1qvEKxy2W3f3Vqpx1fU%2BPdtXFxwu3iN5RER4Jw9US0gO3v08LS9yBYS2YDWh1L%2BwKAMy0C%2Bt5A95TqYw7JuTvQY6pgERxmmcHuENOxrlHjkpH0RvZq9cmWllQgjLKzXO5oWihnO1fCjjbGIisn%2BiYtOTjfmuS4aNBj2VYLlJwG4xd0Pp3%2FJBAvBk8VHyar03TG4tQZiKi0HLsikfdb1UFUWUjQuVeUwOak3hDp5SFLaxKpRPpunmHjwY5BWc4cyVFWLzNvwQnfDrpQi79SHjnaX9RhmnazF2MVbbWp8COhB8jJl5TVFmqOCE&X-Amz-Signature=f43326953885cf5b9c1e2c2cba2d8dcccead3bee0482a94bbaf3593262b1626a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNKH6JCT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCllpWxmiTxhSt1dNOVu0ZbXln1gs4cU9A2oMCuPBbyAwIhAJFXOvj24Gj%2BxzIf9HJjNqE3mBZnukwkZliELY1tbo74Kv8DCGAQABoMNjM3NDIzMTgzODA1Igwy18WyJLVBmHwIzEYq3APl8e%2BdxdYb6i5LJmhyU6SgEGSWsMQGsLS8H1EwC0Em2FiLKSiDNpuiwxLYb5nRMVJEqoxM8wltVZq%2BrPLdhrtcf8ad6UXHdgcVZ7MkC%2Ff%2BptBmJP5x9wEyjrnHwVjaGOAbRVEdbFBj3Z2ASq5XBpfJIGzt19goDtmLbMdxzGcylqfyh16ro9ASXSniZkgKsLP2vQKf2vi6nm5sW1%2FRwnCGnxTIAaQtQ18oRSvmxyrnslIx7e1tD5zSIug5oN3juHpPnsfIE5B94WBgxRazMpJX3722cEjhLz69jMonJ%2B%2BgPHVYB43GG7OdwJjFqffgnhP7ERotDuUxlDwpPY0WEU24ctshSEdMVd%2BgOL%2BDcFLTAT%2BkaYeG162430J4%2F5guDr9HnJrY7P%2FeQ7G2266YsNneEFh4qZ372jQDfLA6IfFy1Iv637wFWlc5fQjpICqysyG5RCrhuiEUhB5usfJ92cHo5vq9VPDZWw253VTurMv6woFvTUGXejOfIgIZEr2o6yefr%2Fj%2Bn6%2B9sC380cTVetbMSqFBrs0cEiVnKFqLPnTxkXZfgrieVShS0WC5m%2FeIEt6pO5bLgOydlhSTgQ6luAPonFVHLqUV9iHeGGH3J3eN9qrbZTQpmZwniPsgMjC2nJO9BjqkAbjnfjcv0%2Bs5BSViYNKpf9Dn96NZHOAWeRw9qXaU05hKvWf0Ccea2tr1RDWaqJECxKxM6uBCHk5KyKZAFnk75AQ3en3jZX6qumWEqqFiFedZW%2F15YP3MnPfg7umUcGBWv9bqkudgs4BNxbjqWItrpYD3AfkZu%2F8Ss1SbIFwNWWkSQgb3odzVX2b4%2Blbpv3JMjVsxNz%2FDGM2DN1xu60Z3GwW32nSw&X-Amz-Signature=9e7bfaeb906d58181cd79d7f3f8eab27f435434d9848dbb63e5db41c3dd1ea18&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZPTTPPA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDOK9NgwexkMB%2FqUWkmbHaTyjU%2FmB1%2BMGd2pb9dBjaIZQIhAJ6YpI3ntmz3lxxnuxCz3mdi0XxdyL62fW123K4zKi%2FIKv8DCGAQABoMNjM3NDIzMTgzODA1IgxRAxGVLypW%2B9KJI68q3APdx%2Bh7Xs4fvbT8c6EhEE8culfRrtrqjLsok6hkzVz8RpaC63NwzRUtHHfKjovtoI0xSCKLV2O3Mhu8kRtuIi%2BUfVVHlB%2FqQPArHdQXs5Yo%2BGlkW8GQN30o8pNnAW4lSuy0HI97S6%2FVnti1s209dSW7%2BLM2BjNXwhvuzfnrVhl3l8izKPRfcao9SKqrQL%2BGLGr5vU1TCFm7GE77b0CTlF8aBwRLvnR5Iyw2nwCJzXQuKFzyhe4uP%2Fl7pe%2Bz1AQCL%2FCx%2BaJ5GUboY8WqYlu6SU1U8jKUodyHnPP%2BsW7JZoT%2FVAYyFFDf5ae8jzDEDVEB70YfMD6QP5Wu6pVMp3teOZt2dEV6W7226208vtlnvqp%2BXCd4WcLnWade0htc%2Bq62q62wi1j7jPTvAWcfE3V8LJAby%2BIMd8JitR2DD4YKInFnuGMukxjQXA%2BsLGH7wLvWI4te%2BdzPf7nrEwyQ5Gwzh89VxvWKCfHZJI5QXEAXP8fR%2F29ZfuJLWs2m3BRLO4lNhesvvMCi2hmOBGZZl1sqfqe5bgEw6uOagRlW9FRaeexmFvnHEB06DqH8AL3xxDI%2BGVpDq8gnkXwtWsmLfcnMaAbxolCUdEBpvjJLCXhEPxVIPnkGLND1cvOrEdzIIzCDnJO9BjqkASdOucE3y4dUp6iVQppJU1YH2itG%2By0om9PcGUItStHC1%2BkeWOyMy3CENYtnn1YGgjlLzsBjcMGsASPY%2BcEDYtrWHjN4IvaxeCVugMRxzrqwhOVKxqrAUr3PuW5JJrZ%2FX9R5UebjYAcuMYw5xUrsyxxggG1tKMdQh%2BofvgFVe97n2oYu2N08LX1sP5y2W%2FiVbHsFJJeZaTKqh8UvMlR9UkDCbV7U&X-Amz-Signature=06cc5142ba6478473b74d156eafa502db97c778bd754215c33e4a697e0d079eb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZPTTPPA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDOK9NgwexkMB%2FqUWkmbHaTyjU%2FmB1%2BMGd2pb9dBjaIZQIhAJ6YpI3ntmz3lxxnuxCz3mdi0XxdyL62fW123K4zKi%2FIKv8DCGAQABoMNjM3NDIzMTgzODA1IgxRAxGVLypW%2B9KJI68q3APdx%2Bh7Xs4fvbT8c6EhEE8culfRrtrqjLsok6hkzVz8RpaC63NwzRUtHHfKjovtoI0xSCKLV2O3Mhu8kRtuIi%2BUfVVHlB%2FqQPArHdQXs5Yo%2BGlkW8GQN30o8pNnAW4lSuy0HI97S6%2FVnti1s209dSW7%2BLM2BjNXwhvuzfnrVhl3l8izKPRfcao9SKqrQL%2BGLGr5vU1TCFm7GE77b0CTlF8aBwRLvnR5Iyw2nwCJzXQuKFzyhe4uP%2Fl7pe%2Bz1AQCL%2FCx%2BaJ5GUboY8WqYlu6SU1U8jKUodyHnPP%2BsW7JZoT%2FVAYyFFDf5ae8jzDEDVEB70YfMD6QP5Wu6pVMp3teOZt2dEV6W7226208vtlnvqp%2BXCd4WcLnWade0htc%2Bq62q62wi1j7jPTvAWcfE3V8LJAby%2BIMd8JitR2DD4YKInFnuGMukxjQXA%2BsLGH7wLvWI4te%2BdzPf7nrEwyQ5Gwzh89VxvWKCfHZJI5QXEAXP8fR%2F29ZfuJLWs2m3BRLO4lNhesvvMCi2hmOBGZZl1sqfqe5bgEw6uOagRlW9FRaeexmFvnHEB06DqH8AL3xxDI%2BGVpDq8gnkXwtWsmLfcnMaAbxolCUdEBpvjJLCXhEPxVIPnkGLND1cvOrEdzIIzCDnJO9BjqkASdOucE3y4dUp6iVQppJU1YH2itG%2By0om9PcGUItStHC1%2BkeWOyMy3CENYtnn1YGgjlLzsBjcMGsASPY%2BcEDYtrWHjN4IvaxeCVugMRxzrqwhOVKxqrAUr3PuW5JJrZ%2FX9R5UebjYAcuMYw5xUrsyxxggG1tKMdQh%2BofvgFVe97n2oYu2N08LX1sP5y2W%2FiVbHsFJJeZaTKqh8UvMlR9UkDCbV7U&X-Amz-Signature=813605a45365cf46a1b38ba299446b879520518c3224f5aacd0195510fbd9ff5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZPTTPPA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDOK9NgwexkMB%2FqUWkmbHaTyjU%2FmB1%2BMGd2pb9dBjaIZQIhAJ6YpI3ntmz3lxxnuxCz3mdi0XxdyL62fW123K4zKi%2FIKv8DCGAQABoMNjM3NDIzMTgzODA1IgxRAxGVLypW%2B9KJI68q3APdx%2Bh7Xs4fvbT8c6EhEE8culfRrtrqjLsok6hkzVz8RpaC63NwzRUtHHfKjovtoI0xSCKLV2O3Mhu8kRtuIi%2BUfVVHlB%2FqQPArHdQXs5Yo%2BGlkW8GQN30o8pNnAW4lSuy0HI97S6%2FVnti1s209dSW7%2BLM2BjNXwhvuzfnrVhl3l8izKPRfcao9SKqrQL%2BGLGr5vU1TCFm7GE77b0CTlF8aBwRLvnR5Iyw2nwCJzXQuKFzyhe4uP%2Fl7pe%2Bz1AQCL%2FCx%2BaJ5GUboY8WqYlu6SU1U8jKUodyHnPP%2BsW7JZoT%2FVAYyFFDf5ae8jzDEDVEB70YfMD6QP5Wu6pVMp3teOZt2dEV6W7226208vtlnvqp%2BXCd4WcLnWade0htc%2Bq62q62wi1j7jPTvAWcfE3V8LJAby%2BIMd8JitR2DD4YKInFnuGMukxjQXA%2BsLGH7wLvWI4te%2BdzPf7nrEwyQ5Gwzh89VxvWKCfHZJI5QXEAXP8fR%2F29ZfuJLWs2m3BRLO4lNhesvvMCi2hmOBGZZl1sqfqe5bgEw6uOagRlW9FRaeexmFvnHEB06DqH8AL3xxDI%2BGVpDq8gnkXwtWsmLfcnMaAbxolCUdEBpvjJLCXhEPxVIPnkGLND1cvOrEdzIIzCDnJO9BjqkASdOucE3y4dUp6iVQppJU1YH2itG%2By0om9PcGUItStHC1%2BkeWOyMy3CENYtnn1YGgjlLzsBjcMGsASPY%2BcEDYtrWHjN4IvaxeCVugMRxzrqwhOVKxqrAUr3PuW5JJrZ%2FX9R5UebjYAcuMYw5xUrsyxxggG1tKMdQh%2BofvgFVe97n2oYu2N08LX1sP5y2W%2FiVbHsFJJeZaTKqh8UvMlR9UkDCbV7U&X-Amz-Signature=0677c4cfd219421aa6a777418520ae451b38e74d7cdd2ce869d29237bc33ff77&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MTE2J56%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIFLObI1k5SWsAOICxCoCdcLJshcgiLqqw0rUOtY1agCYAiEArSJ5UeI9BRqldeiw9hhG%2BYSNZg00VMkGK4MX%2FGFkiA0q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDPoXk7Q7%2FuqnZZQcbircA7QCiApg5fChfKK06j3WJbVjdaIQiq%2FBER4tlR6kAblrOlj32%2Bjs4pK6lIrR%2B0kATse2o49S3POzxYmqK93MPlpaCz%2Feh8WzYZuTO8IMXUqeunT7cCoujsSeSf2AMyA%2FROP55jbXCTDH%2BGf9WuboXUWPpHlL31Kg9U95q8Ri0m7mQn5EXl3ab09Gl5bGt4Cu%2ByHgdZcfsuySn7ZamrTYK2kxQKtDEJI%2FsUJ8gDOETJe%2Fcw4NDTwk%2BdkiK00qqFI7X%2BBOeDDL3gfle%2BOW2SyjTt7%2Fo4WU3TaXZtt9Lb6QOVIqC0UuZkfgt%2BWJ7Cmm5L6mNLAFLp9vrZKwBfrvnAAayXbm1L4%2BKUwfqB9LU989cgOO%2BRUaYijMWcYl2bknQfWXZGXDxauZ351gI3Bp3FL9HF%2B0TKZV0KxFsu9G6b7dO%2FSltM89byvc3E%2B2tIgTge0TT8KYsITKZvXTjtiU34wfCvBudWJiBVnn3XjgFkfODp%2Fi0RPLxXl6EM5JaZsO7xshZjbQd8rl8N986y%2FVmnw%2FeWd9uVRtoJ3wtgrEPer3s4xKEGr5EDK3MEqvzudpkBIscNnM7N9XuwElQ9sCa20%2FiJ79c8k4Di58CBs6qJgsNY2il9Nhwyv6VJsTNJawMMack70GOqUBx6lKpRuQswa0jKQQMTTjau6gt4ul0wp7wuDJ2ukS1JER4STSqvgCkbIR%2F2%2Fq3aRgMyquj8N8rjrKG5ebtPhso5HZaIAX%2Bss9EQPPz5P0mruc3VJAzHNeUiQqeIqsYnfpzgS9Adi%2BHtWTnQym0OVSp2K2v6npEqozrnfq0Za7P4tk9q1ciQR%2BTfc%2BCjy4VxM2tDGakNbk3WUN2ciAaAXgQgWLgnBd&X-Amz-Signature=3f97d3e39c6f0fbc93a30cd1d828601dce3163fbec29e293a7855b20b66aa6f4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636OWORST%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCWCGG%2Fni2DLh3Wwut5aYBOdAAWF%2BlhyaInYK4kh2Hm0QIhAJdLUaDznDti3O4LLLUjnSwxXewTN252Zyvb%2BnUpowRjKv8DCGAQABoMNjM3NDIzMTgzODA1Igw58tdA54qHpb92sngq3AMztukFL6ewla2MLCNyQO14hKUgwzbv%2FhfjRHW3HJC9iBMgD7IgDchPkkQz%2FPK3W7kMJ2BYkyFpdxbFh%2F8F6Cq515WiIq1YC2aKR0iUxXj4DTBmlb4qHQDCKI1YQfvvdvILCFVGzEIEt0bnxSsNvxAmwRq1aATL13oO%2FmhsS9typ36TMxo1nmlT6pTzfqcxczsEOAs20zsFT2D3l12CltpoQKs9o9Li%2BuftHieuh3%2Fn%2FF6H9T%2FbMhozDP%2BOO7QUAdH9VtHvWtYEFsvLQZ%2B80lCochLbour%2FjlZBasV%2FQrGm260LrQaEIioEFsctt464MJ%2FDPX%2B9Np3qJK1fcDQHX30b0xGc%2FBK9yTUvQ5r%2FPlJ%2FuR4u%2FQeCgy0Scg8SF8v16sGUeWFYWy1NqjukKv3rzFegsmCB%2FcY70V0cC4xMzECQgMEvLtdywoXqCuN7LTOaDudXgDaI9%2FAXkt%2BxRzKz8WcViTghtRFNLW2DGBzXXKtKSRFArS2NbBJY20G697O3C9DHIB5wlkLmFqKkqz0xIDmX8vNnQm2uWPhc6XTEAqFqiR%2BgqyspZoz0TBasiUTNgATNxVsyP6RVSv84sR9zm5TexBryPsMMsdpLj3X0EUVZ2tKr4sMHPv3P4n9HszCPnJO9BjqkAbs0rnWfY2R12bvNd1IpbW5sE6h8LKyQP002l8s77IVRr2as8%2FcHQiYHmxembXDf3%2FJIs%2BpSKOSI0XA9qq6Z0vGCx3G1szlkUv1OXriFTrUFvfusRWBEL8JBGtiKvpz3zmMoAx148mKpWYv6z20rg2jWaRIQICnJeZ14zWPuFj3udxP7x%2BzdWdyJF5jeuWLBZMKbug%2BntlaI%2Fk%2Bytoa0S9oam8BX&X-Amz-Signature=e72d7eff2d338c2d507c4f71345ffe65c20fc70a80136308d4115156320e5994&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466427J5EZH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCv7RyQWDz%2F09KPQe5Ge8TE9H3t0eqWjI4hcTNH8uq5YAIhAId7i7xiEtJ%2FptPe%2BPXhK5PfVySJDDNJ7TUH1ld2T9F2Kv8DCGAQABoMNjM3NDIzMTgzODA1Igx0TzXOGefCIcXn3zkq3AOM%2F7LoXMhZJhP0CAm3TK0IrQcz4Q3l2ovtEfR6fN8GUmd1SNEgABBkLnY9A415pZvRTmUKTlx25qOHtlPEaFixFkLxyCYiuX02PadB4hnVveiK5zcPhR%2F%2FxhRaxvtL5YCEeA4m0AbHfDYYlx80fMstmeZflcLHvoIHtYl%2FhPKDaW00DgnwZuCsgF4XGYfjhysG0aOS78mboOsdmGJwpE8BRxWNDtpiXnlmoAgP%2B78sGm%2Bbh5Yxc2Oa%2F6pQI%2F0fuyHFmDuljR2Rkh0zzYpFDRO9UNcbuLv7Iy1kzl3V7F54MGXCBz8pPXUa%2F2l8Pfr4QY6T%2Bw0U%2FowIwG99bQwYkp%2FqFbgFyEWL%2Fi8mvVBUAeHTNicJwqgaqBr5AMhKr5vmroJaZS0DyaNXb%2BhrBDr753Kv3BwHB%2BVLXyM0eYOqxaLM5nfAL0pjYlOKw3t%2BLbdiO8Wsc%2BunrlldmZs0aSzfj2Bf%2Fca%2F%2FQQcaKZF9fFmLVYmYU6ZNorz3WgdXQvEqRVoPDUb9wBAmjldic7tF8JKkzLBlhjdWwYvlG%2F2%2FZvv6vofofyXU4KnCKa5U%2F06ofll6FTo4dg3LLS%2BzD6Gzr%2B2wefduQng4l53aIhyAUzFfajVzisLozIHzY3Ahhf9pjCOnJO9BjqkAW7MeLjkDKD8IB%2FJ2Nlez%2BzlFDQlh1J%2Fux4lhKWHozorvzx0GmdsBrqJPyKqS9meW5hjyT3JOS6bD7tB5D3tAQrgwx9NotyB5s7V0cMrUMuVv2Mdf9mg%2FaDSNwEZq6EpFeXdebkSpupvM4Gf%2FVmUAjqmtym9pH35jofpPOFpoWCBbwE6Mpl3XQ5vUPO6SUvH1gjHeJyNN%2B5bVbc4LmoE9M9Hw9gL&X-Amz-Signature=a8aa3bd81af7fe8263223fc9c6b06da58143a11c5cb3be177c73ec10de10899e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRHN56OY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161701Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDNW55neLe8O6I0b8ktimEEX9grZvyShtA0NmQX%2B4qN6AIgPtG%2Ffwo9CbEkgeKcd3HUMrhbw9hPubylXnVs1aTR3vMq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDIzKoE0dd1xUa2k7NCrcA%2BoJYqcMXxPMzortK4tPTmU9i1v%2BQFN88uUi8wb%2BxPcEgbwxpYlLatW2yPOAZL1NI6yCvwwREOEmk1Qqm6pq29qbhe80oskEwSIViiNRKKkV7C8XDYpVb%2FerAq8aww1RoeZfbU03igHenp%2FrLCpYT0MqSvADwM55N35OXPuObE4rc1XUKNfQnt9OYxU5gZKsM94%2B4bv5MpqqcXNmc8M2UCciMwvxjXA3opYW6X8ZFbQbEbxGOq9eert8HLZDs8obh0bCTiodQeiyax%2BFiDsM7CktEpH4QqG4FKTGakJCq1Bh%2FjzRYdO52WE7XFGfyMOubNiAoXycXNSZpIn1ROANuIgq%2FwrNRbHbUw83SDbroNQK2uUjJroMCobxkHw%2BEKkXYmDwcsFLu4R2Gj%2Fxjj5YYouJuvPVtu6OuDxrMvCoV1BjNLcoq4n0mIa9i0iyLlFxpLmu0nYiO8lYWnHUc0%2FuaNNHt5ABwVgL%2BEUWrSYapmjpdYMQy0UrVzOTEbUhNxRW5BKhdiUv89o5dnmCimWYQFYgA65reVt4l9s6Ja9wfpWBYId7M94lAqWjvzY3aZYZkwwD%2BKB883WU%2BD1zJB3%2F6fMREsAaR86j%2BlgHvyWsuKJ7hyHL28aCiGxXEHzHMJick70GOqUB3AUTDcWK1nhn686mC82DQrafDhcXbmFr91xtHZeSVOhm%2B5xoA9esqqtNhv3V3xSJPTxlQvnwP1Tu55YkiGqd8j9RD8shWPbMhAib2EEhKbdxcDg3DF5aWIYA7dJ%2BiVq3RJZS5RGa6x87DL0QN7GvezxqFe8pQPr9jaRA%2FfEKoptEjV4hB%2BF1cS2SEWyRW%2Fu64IEsVbj5XqtXmi4z8NHUFwpACPr%2B&X-Amz-Signature=475bc456d69d554deed96f4272c5594366459fec1da7209f4fca0e08cc671b83&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRHN56OY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161701Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDNW55neLe8O6I0b8ktimEEX9grZvyShtA0NmQX%2B4qN6AIgPtG%2Ffwo9CbEkgeKcd3HUMrhbw9hPubylXnVs1aTR3vMq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDIzKoE0dd1xUa2k7NCrcA%2BoJYqcMXxPMzortK4tPTmU9i1v%2BQFN88uUi8wb%2BxPcEgbwxpYlLatW2yPOAZL1NI6yCvwwREOEmk1Qqm6pq29qbhe80oskEwSIViiNRKKkV7C8XDYpVb%2FerAq8aww1RoeZfbU03igHenp%2FrLCpYT0MqSvADwM55N35OXPuObE4rc1XUKNfQnt9OYxU5gZKsM94%2B4bv5MpqqcXNmc8M2UCciMwvxjXA3opYW6X8ZFbQbEbxGOq9eert8HLZDs8obh0bCTiodQeiyax%2BFiDsM7CktEpH4QqG4FKTGakJCq1Bh%2FjzRYdO52WE7XFGfyMOubNiAoXycXNSZpIn1ROANuIgq%2FwrNRbHbUw83SDbroNQK2uUjJroMCobxkHw%2BEKkXYmDwcsFLu4R2Gj%2Fxjj5YYouJuvPVtu6OuDxrMvCoV1BjNLcoq4n0mIa9i0iyLlFxpLmu0nYiO8lYWnHUc0%2FuaNNHt5ABwVgL%2BEUWrSYapmjpdYMQy0UrVzOTEbUhNxRW5BKhdiUv89o5dnmCimWYQFYgA65reVt4l9s6Ja9wfpWBYId7M94lAqWjvzY3aZYZkwwD%2BKB883WU%2BD1zJB3%2F6fMREsAaR86j%2BlgHvyWsuKJ7hyHL28aCiGxXEHzHMJick70GOqUB3AUTDcWK1nhn686mC82DQrafDhcXbmFr91xtHZeSVOhm%2B5xoA9esqqtNhv3V3xSJPTxlQvnwP1Tu55YkiGqd8j9RD8shWPbMhAib2EEhKbdxcDg3DF5aWIYA7dJ%2BiVq3RJZS5RGa6x87DL0QN7GvezxqFe8pQPr9jaRA%2FfEKoptEjV4hB%2BF1cS2SEWyRW%2Fu64IEsVbj5XqtXmi4z8NHUFwpACPr%2B&X-Amz-Signature=8ec0d6a356a524e16227a908c26d2a2c04fb9afcd7de4e13f8ac0ee20e30e406&X-Amz-SignedHeaders=host&x-id=GetObject)

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
