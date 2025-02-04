

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MQAVYAM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDV3NuJVFxdUUlaJNiWD2MR4UFar4meVUJXK8dXWIIe8wIgEPyU4SwypNtu178qFazmzbkRCwsRCCf2EedbJc%2BLqk4q%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDHjRXiOAAslSpVADVSrcA44G1Zc9p7lrKtz4H0dtlskdkO0gb0lu9S%2Fpe%2BR%2BWpki2DLQ2eKXNWe%2BUP2NAW9hHC9oMltl0Q9em%2BRJemDG%2BKkc3PbLQFBvF8Zn1kLlLQYIrta9sVj%2BYar8RXfhqJ3V9peOKvXd8%2BpB68G3sRCDzOw9Tj%2FftD8N6wQCW4egd4FDk8cXLeXIXcEjCP9sopDTOhr%2FV8AftkqGMkW8pCH9vERT22o0ucf%2FtwGFNFn7YprRH1EZoA7j3PI1rtsW3kclKjcOANHjqDA3k10WmJBcaxmnKh863kWF2d9je9GqGjVrvxkdWUROvobCAvT%2Fvr%2BUoApLzcEjTFNwqDcieBoe5urB3fVq%2BIjtu%2BAtCrEoaJEtwklYDIyR8huV4i4m7EYAnVvJFGVMWP00j%2B5IrW6uxWrHTpFxAcQ%2Fz%2BrYsFR8YNOGyUiRH%2BQ0Iax7VBRdM5dKmDsJlDhOkUwXwpo6QcnNfvPxUUnD0w83LlAY5xl4r7b4R4w%2BbsOjMzT70iFYz5Fah9qKrrmVfWqIMDz2aqii7W%2Fi5L6QC9rtvkx5quXUH%2FNKvBIoBUWo3Kavm4%2BwI6izzJKAB8PGbDs1YnM5IvWZtIPTqYJIxqZuaWZqYJnH924Pn1XPVinmw4fWg6SaMNeUir0GOqUBmNdqMPa8dyFP06EZEBzdgZVGhtFNR3rPqqCCu2TLcJ1Twa%2BoxoyoVMzX4ztFRtjqwwhXkNY%2Fv29d7wKI684dBMJlxyS%2BRsCJxDqz4hmNQ%2Fe904%2FeuwI%2BjRxoC%2FOLOJaXFXnSEWiKDsDEomvr119vttde0we8e781Cs3AiRF%2B8Kn0m5kH%2FpQ%2BNve%2BGmQoKxVBV8mbHtNHrlVwpFBI%2FiV33W%2BEWiFV&X-Amz-Signature=83335470eb61399cf99e1f0de49e3c542375a0ef8a9f557f1488517fe4776470&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MQAVYAM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDV3NuJVFxdUUlaJNiWD2MR4UFar4meVUJXK8dXWIIe8wIgEPyU4SwypNtu178qFazmzbkRCwsRCCf2EedbJc%2BLqk4q%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDHjRXiOAAslSpVADVSrcA44G1Zc9p7lrKtz4H0dtlskdkO0gb0lu9S%2Fpe%2BR%2BWpki2DLQ2eKXNWe%2BUP2NAW9hHC9oMltl0Q9em%2BRJemDG%2BKkc3PbLQFBvF8Zn1kLlLQYIrta9sVj%2BYar8RXfhqJ3V9peOKvXd8%2BpB68G3sRCDzOw9Tj%2FftD8N6wQCW4egd4FDk8cXLeXIXcEjCP9sopDTOhr%2FV8AftkqGMkW8pCH9vERT22o0ucf%2FtwGFNFn7YprRH1EZoA7j3PI1rtsW3kclKjcOANHjqDA3k10WmJBcaxmnKh863kWF2d9je9GqGjVrvxkdWUROvobCAvT%2Fvr%2BUoApLzcEjTFNwqDcieBoe5urB3fVq%2BIjtu%2BAtCrEoaJEtwklYDIyR8huV4i4m7EYAnVvJFGVMWP00j%2B5IrW6uxWrHTpFxAcQ%2Fz%2BrYsFR8YNOGyUiRH%2BQ0Iax7VBRdM5dKmDsJlDhOkUwXwpo6QcnNfvPxUUnD0w83LlAY5xl4r7b4R4w%2BbsOjMzT70iFYz5Fah9qKrrmVfWqIMDz2aqii7W%2Fi5L6QC9rtvkx5quXUH%2FNKvBIoBUWo3Kavm4%2BwI6izzJKAB8PGbDs1YnM5IvWZtIPTqYJIxqZuaWZqYJnH924Pn1XPVinmw4fWg6SaMNeUir0GOqUBmNdqMPa8dyFP06EZEBzdgZVGhtFNR3rPqqCCu2TLcJ1Twa%2BoxoyoVMzX4ztFRtjqwwhXkNY%2Fv29d7wKI684dBMJlxyS%2BRsCJxDqz4hmNQ%2Fe904%2FeuwI%2BjRxoC%2FOLOJaXFXnSEWiKDsDEomvr119vttde0we8e781Cs3AiRF%2B8Kn0m5kH%2FpQ%2BNve%2BGmQoKxVBV8mbHtNHrlVwpFBI%2FiV33W%2BEWiFV&X-Amz-Signature=dc07b038d9b6ae663a88172c22b35fa5b2a60bae0d0e02b5aecd97e19ea06172&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MQAVYAM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDV3NuJVFxdUUlaJNiWD2MR4UFar4meVUJXK8dXWIIe8wIgEPyU4SwypNtu178qFazmzbkRCwsRCCf2EedbJc%2BLqk4q%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDHjRXiOAAslSpVADVSrcA44G1Zc9p7lrKtz4H0dtlskdkO0gb0lu9S%2Fpe%2BR%2BWpki2DLQ2eKXNWe%2BUP2NAW9hHC9oMltl0Q9em%2BRJemDG%2BKkc3PbLQFBvF8Zn1kLlLQYIrta9sVj%2BYar8RXfhqJ3V9peOKvXd8%2BpB68G3sRCDzOw9Tj%2FftD8N6wQCW4egd4FDk8cXLeXIXcEjCP9sopDTOhr%2FV8AftkqGMkW8pCH9vERT22o0ucf%2FtwGFNFn7YprRH1EZoA7j3PI1rtsW3kclKjcOANHjqDA3k10WmJBcaxmnKh863kWF2d9je9GqGjVrvxkdWUROvobCAvT%2Fvr%2BUoApLzcEjTFNwqDcieBoe5urB3fVq%2BIjtu%2BAtCrEoaJEtwklYDIyR8huV4i4m7EYAnVvJFGVMWP00j%2B5IrW6uxWrHTpFxAcQ%2Fz%2BrYsFR8YNOGyUiRH%2BQ0Iax7VBRdM5dKmDsJlDhOkUwXwpo6QcnNfvPxUUnD0w83LlAY5xl4r7b4R4w%2BbsOjMzT70iFYz5Fah9qKrrmVfWqIMDz2aqii7W%2Fi5L6QC9rtvkx5quXUH%2FNKvBIoBUWo3Kavm4%2BwI6izzJKAB8PGbDs1YnM5IvWZtIPTqYJIxqZuaWZqYJnH924Pn1XPVinmw4fWg6SaMNeUir0GOqUBmNdqMPa8dyFP06EZEBzdgZVGhtFNR3rPqqCCu2TLcJ1Twa%2BoxoyoVMzX4ztFRtjqwwhXkNY%2Fv29d7wKI684dBMJlxyS%2BRsCJxDqz4hmNQ%2Fe904%2FeuwI%2BjRxoC%2FOLOJaXFXnSEWiKDsDEomvr119vttde0we8e781Cs3AiRF%2B8Kn0m5kH%2FpQ%2BNve%2BGmQoKxVBV8mbHtNHrlVwpFBI%2FiV33W%2BEWiFV&X-Amz-Signature=0d9f1862f239c9ea22b2dc205ad205ecc8085c316811d27a35b953c4723e2c31&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5OWLP6Q%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDlwJCeE7eAdsnK9Rk64EE4CsKTxVcSZpt4tkjTFVuptQIhAK3igczed2KOye1uLrEp%2F89i37uZtjTnndPCYFJMoByuKv8DCDcQABoMNjM3NDIzMTgzODA1IgwwvvmC0kdv65UjXC8q3AO%2FYGqdpODLnLUJw6xfw%2FP1Ux3kX8BJfUwtsHGBikeO%2B%2BQObKaW81D5kpf4tprSm5JPn%2B6N0anLUMI3MAO9h6aVNfP3N4%2BXwRWuHMngkYYP0zYnHwlJOmie34AlqmIUSSg37hL6njnBoSKmAD5gqxmh1gGOg1zFwenVt2YSjkVSJuZEYgDoQZQZOVyDP5d6011QyMeEorwNBNWa7bFfkG8%2FvGtyqY8afCQhSWmYP1CT4HGascM8nlVHTtkAa%2BTg8UmOk6vu6tLp3u%2FnjZE77fJ5VvnLvYbarGYfv8MYobqpoCp8C%2B3lbZhh1%2FYbQJVHyKeS%2BZjAojRLF28SSkt4vJD8wRugvkMVgmMxCbyQ8z%2BvcSFCMfPkrMUkQ%2FgEmqRtSMq4khmRg5%2BMn6giLBZxDj3I%2F6DKO1U4j36HqIdhKXhbAOMtvm39zgNU%2BvG%2BFl%2BR3bst%2Bygbl8I%2B79yJVNWIfMdHs4PGMsbMWgwDhJWWtjNBVte8ACT3J2TfKn9v4Y9cVjY8YsZUgjkXHL4%2B73vfaZ7xYRHNEePSPp9Sz8GWgCKzk%2BMi5R0LUpLgE3tDv1PzrO6WdKvlX8S3LirCi%2ByaCLB%2BS9PAwFC3%2BRjgh%2Bzl5hBEtFol7TbxSN%2B9TM7GvTCUlIq9BjqkAatAYLhXc3g64RpNOf4gVgXcAl3wcrLRtaaj9B8QcJWhueK%2FTA2AQcVuLPaUVwE9GRf97Rhq2AGOUIB6JQLgHDvORrbRNB0CZoc4J1MGcRKkNUzQ%2FOHJYg6ebrq5v6b%2Fr3m27R6%2BaRzlk7FX1FEaO5fbXl4glmfWJJPhDVrO%2BOxslZ1cTRmCsQqbwgPGqvj3Gex7%2BGtCHTtKgSLVlyjLqT3kyxVc&X-Amz-Signature=00a9ec41427869deb8c1c5c6bc45863ca1647bdd7572cc72a242e7522849c036&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5OWLP6Q%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDlwJCeE7eAdsnK9Rk64EE4CsKTxVcSZpt4tkjTFVuptQIhAK3igczed2KOye1uLrEp%2F89i37uZtjTnndPCYFJMoByuKv8DCDcQABoMNjM3NDIzMTgzODA1IgwwvvmC0kdv65UjXC8q3AO%2FYGqdpODLnLUJw6xfw%2FP1Ux3kX8BJfUwtsHGBikeO%2B%2BQObKaW81D5kpf4tprSm5JPn%2B6N0anLUMI3MAO9h6aVNfP3N4%2BXwRWuHMngkYYP0zYnHwlJOmie34AlqmIUSSg37hL6njnBoSKmAD5gqxmh1gGOg1zFwenVt2YSjkVSJuZEYgDoQZQZOVyDP5d6011QyMeEorwNBNWa7bFfkG8%2FvGtyqY8afCQhSWmYP1CT4HGascM8nlVHTtkAa%2BTg8UmOk6vu6tLp3u%2FnjZE77fJ5VvnLvYbarGYfv8MYobqpoCp8C%2B3lbZhh1%2FYbQJVHyKeS%2BZjAojRLF28SSkt4vJD8wRugvkMVgmMxCbyQ8z%2BvcSFCMfPkrMUkQ%2FgEmqRtSMq4khmRg5%2BMn6giLBZxDj3I%2F6DKO1U4j36HqIdhKXhbAOMtvm39zgNU%2BvG%2BFl%2BR3bst%2Bygbl8I%2B79yJVNWIfMdHs4PGMsbMWgwDhJWWtjNBVte8ACT3J2TfKn9v4Y9cVjY8YsZUgjkXHL4%2B73vfaZ7xYRHNEePSPp9Sz8GWgCKzk%2BMi5R0LUpLgE3tDv1PzrO6WdKvlX8S3LirCi%2ByaCLB%2BS9PAwFC3%2BRjgh%2Bzl5hBEtFol7TbxSN%2B9TM7GvTCUlIq9BjqkAatAYLhXc3g64RpNOf4gVgXcAl3wcrLRtaaj9B8QcJWhueK%2FTA2AQcVuLPaUVwE9GRf97Rhq2AGOUIB6JQLgHDvORrbRNB0CZoc4J1MGcRKkNUzQ%2FOHJYg6ebrq5v6b%2Fr3m27R6%2BaRzlk7FX1FEaO5fbXl4glmfWJJPhDVrO%2BOxslZ1cTRmCsQqbwgPGqvj3Gex7%2BGtCHTtKgSLVlyjLqT3kyxVc&X-Amz-Signature=566e11aa666af1b364a6165a99a3e13ec512870432c95054cfed897feeeaebf0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5OWLP6Q%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDlwJCeE7eAdsnK9Rk64EE4CsKTxVcSZpt4tkjTFVuptQIhAK3igczed2KOye1uLrEp%2F89i37uZtjTnndPCYFJMoByuKv8DCDcQABoMNjM3NDIzMTgzODA1IgwwvvmC0kdv65UjXC8q3AO%2FYGqdpODLnLUJw6xfw%2FP1Ux3kX8BJfUwtsHGBikeO%2B%2BQObKaW81D5kpf4tprSm5JPn%2B6N0anLUMI3MAO9h6aVNfP3N4%2BXwRWuHMngkYYP0zYnHwlJOmie34AlqmIUSSg37hL6njnBoSKmAD5gqxmh1gGOg1zFwenVt2YSjkVSJuZEYgDoQZQZOVyDP5d6011QyMeEorwNBNWa7bFfkG8%2FvGtyqY8afCQhSWmYP1CT4HGascM8nlVHTtkAa%2BTg8UmOk6vu6tLp3u%2FnjZE77fJ5VvnLvYbarGYfv8MYobqpoCp8C%2B3lbZhh1%2FYbQJVHyKeS%2BZjAojRLF28SSkt4vJD8wRugvkMVgmMxCbyQ8z%2BvcSFCMfPkrMUkQ%2FgEmqRtSMq4khmRg5%2BMn6giLBZxDj3I%2F6DKO1U4j36HqIdhKXhbAOMtvm39zgNU%2BvG%2BFl%2BR3bst%2Bygbl8I%2B79yJVNWIfMdHs4PGMsbMWgwDhJWWtjNBVte8ACT3J2TfKn9v4Y9cVjY8YsZUgjkXHL4%2B73vfaZ7xYRHNEePSPp9Sz8GWgCKzk%2BMi5R0LUpLgE3tDv1PzrO6WdKvlX8S3LirCi%2ByaCLB%2BS9PAwFC3%2BRjgh%2Bzl5hBEtFol7TbxSN%2B9TM7GvTCUlIq9BjqkAatAYLhXc3g64RpNOf4gVgXcAl3wcrLRtaaj9B8QcJWhueK%2FTA2AQcVuLPaUVwE9GRf97Rhq2AGOUIB6JQLgHDvORrbRNB0CZoc4J1MGcRKkNUzQ%2FOHJYg6ebrq5v6b%2Fr3m27R6%2BaRzlk7FX1FEaO5fbXl4glmfWJJPhDVrO%2BOxslZ1cTRmCsQqbwgPGqvj3Gex7%2BGtCHTtKgSLVlyjLqT3kyxVc&X-Amz-Signature=d4b6f1eb753835ba692c7198e15e7bdde94efaa40455f7604cbf86cc0293d099&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5OWLP6Q%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDlwJCeE7eAdsnK9Rk64EE4CsKTxVcSZpt4tkjTFVuptQIhAK3igczed2KOye1uLrEp%2F89i37uZtjTnndPCYFJMoByuKv8DCDcQABoMNjM3NDIzMTgzODA1IgwwvvmC0kdv65UjXC8q3AO%2FYGqdpODLnLUJw6xfw%2FP1Ux3kX8BJfUwtsHGBikeO%2B%2BQObKaW81D5kpf4tprSm5JPn%2B6N0anLUMI3MAO9h6aVNfP3N4%2BXwRWuHMngkYYP0zYnHwlJOmie34AlqmIUSSg37hL6njnBoSKmAD5gqxmh1gGOg1zFwenVt2YSjkVSJuZEYgDoQZQZOVyDP5d6011QyMeEorwNBNWa7bFfkG8%2FvGtyqY8afCQhSWmYP1CT4HGascM8nlVHTtkAa%2BTg8UmOk6vu6tLp3u%2FnjZE77fJ5VvnLvYbarGYfv8MYobqpoCp8C%2B3lbZhh1%2FYbQJVHyKeS%2BZjAojRLF28SSkt4vJD8wRugvkMVgmMxCbyQ8z%2BvcSFCMfPkrMUkQ%2FgEmqRtSMq4khmRg5%2BMn6giLBZxDj3I%2F6DKO1U4j36HqIdhKXhbAOMtvm39zgNU%2BvG%2BFl%2BR3bst%2Bygbl8I%2B79yJVNWIfMdHs4PGMsbMWgwDhJWWtjNBVte8ACT3J2TfKn9v4Y9cVjY8YsZUgjkXHL4%2B73vfaZ7xYRHNEePSPp9Sz8GWgCKzk%2BMi5R0LUpLgE3tDv1PzrO6WdKvlX8S3LirCi%2ByaCLB%2BS9PAwFC3%2BRjgh%2Bzl5hBEtFol7TbxSN%2B9TM7GvTCUlIq9BjqkAatAYLhXc3g64RpNOf4gVgXcAl3wcrLRtaaj9B8QcJWhueK%2FTA2AQcVuLPaUVwE9GRf97Rhq2AGOUIB6JQLgHDvORrbRNB0CZoc4J1MGcRKkNUzQ%2FOHJYg6ebrq5v6b%2Fr3m27R6%2BaRzlk7FX1FEaO5fbXl4glmfWJJPhDVrO%2BOxslZ1cTRmCsQqbwgPGqvj3Gex7%2BGtCHTtKgSLVlyjLqT3kyxVc&X-Amz-Signature=5acab76ca1467d4b8bfd5d739179c097450a914ff33c4b42c6585ecf08c19042&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5OWLP6Q%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDlwJCeE7eAdsnK9Rk64EE4CsKTxVcSZpt4tkjTFVuptQIhAK3igczed2KOye1uLrEp%2F89i37uZtjTnndPCYFJMoByuKv8DCDcQABoMNjM3NDIzMTgzODA1IgwwvvmC0kdv65UjXC8q3AO%2FYGqdpODLnLUJw6xfw%2FP1Ux3kX8BJfUwtsHGBikeO%2B%2BQObKaW81D5kpf4tprSm5JPn%2B6N0anLUMI3MAO9h6aVNfP3N4%2BXwRWuHMngkYYP0zYnHwlJOmie34AlqmIUSSg37hL6njnBoSKmAD5gqxmh1gGOg1zFwenVt2YSjkVSJuZEYgDoQZQZOVyDP5d6011QyMeEorwNBNWa7bFfkG8%2FvGtyqY8afCQhSWmYP1CT4HGascM8nlVHTtkAa%2BTg8UmOk6vu6tLp3u%2FnjZE77fJ5VvnLvYbarGYfv8MYobqpoCp8C%2B3lbZhh1%2FYbQJVHyKeS%2BZjAojRLF28SSkt4vJD8wRugvkMVgmMxCbyQ8z%2BvcSFCMfPkrMUkQ%2FgEmqRtSMq4khmRg5%2BMn6giLBZxDj3I%2F6DKO1U4j36HqIdhKXhbAOMtvm39zgNU%2BvG%2BFl%2BR3bst%2Bygbl8I%2B79yJVNWIfMdHs4PGMsbMWgwDhJWWtjNBVte8ACT3J2TfKn9v4Y9cVjY8YsZUgjkXHL4%2B73vfaZ7xYRHNEePSPp9Sz8GWgCKzk%2BMi5R0LUpLgE3tDv1PzrO6WdKvlX8S3LirCi%2ByaCLB%2BS9PAwFC3%2BRjgh%2Bzl5hBEtFol7TbxSN%2B9TM7GvTCUlIq9BjqkAatAYLhXc3g64RpNOf4gVgXcAl3wcrLRtaaj9B8QcJWhueK%2FTA2AQcVuLPaUVwE9GRf97Rhq2AGOUIB6JQLgHDvORrbRNB0CZoc4J1MGcRKkNUzQ%2FOHJYg6ebrq5v6b%2Fr3m27R6%2BaRzlk7FX1FEaO5fbXl4glmfWJJPhDVrO%2BOxslZ1cTRmCsQqbwgPGqvj3Gex7%2BGtCHTtKgSLVlyjLqT3kyxVc&X-Amz-Signature=efe3ff029b09876ecdf6943adb23fa007c4514fa7beec74e95bd95d1228e36f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5OWLP6Q%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDlwJCeE7eAdsnK9Rk64EE4CsKTxVcSZpt4tkjTFVuptQIhAK3igczed2KOye1uLrEp%2F89i37uZtjTnndPCYFJMoByuKv8DCDcQABoMNjM3NDIzMTgzODA1IgwwvvmC0kdv65UjXC8q3AO%2FYGqdpODLnLUJw6xfw%2FP1Ux3kX8BJfUwtsHGBikeO%2B%2BQObKaW81D5kpf4tprSm5JPn%2B6N0anLUMI3MAO9h6aVNfP3N4%2BXwRWuHMngkYYP0zYnHwlJOmie34AlqmIUSSg37hL6njnBoSKmAD5gqxmh1gGOg1zFwenVt2YSjkVSJuZEYgDoQZQZOVyDP5d6011QyMeEorwNBNWa7bFfkG8%2FvGtyqY8afCQhSWmYP1CT4HGascM8nlVHTtkAa%2BTg8UmOk6vu6tLp3u%2FnjZE77fJ5VvnLvYbarGYfv8MYobqpoCp8C%2B3lbZhh1%2FYbQJVHyKeS%2BZjAojRLF28SSkt4vJD8wRugvkMVgmMxCbyQ8z%2BvcSFCMfPkrMUkQ%2FgEmqRtSMq4khmRg5%2BMn6giLBZxDj3I%2F6DKO1U4j36HqIdhKXhbAOMtvm39zgNU%2BvG%2BFl%2BR3bst%2Bygbl8I%2B79yJVNWIfMdHs4PGMsbMWgwDhJWWtjNBVte8ACT3J2TfKn9v4Y9cVjY8YsZUgjkXHL4%2B73vfaZ7xYRHNEePSPp9Sz8GWgCKzk%2BMi5R0LUpLgE3tDv1PzrO6WdKvlX8S3LirCi%2ByaCLB%2BS9PAwFC3%2BRjgh%2Bzl5hBEtFol7TbxSN%2B9TM7GvTCUlIq9BjqkAatAYLhXc3g64RpNOf4gVgXcAl3wcrLRtaaj9B8QcJWhueK%2FTA2AQcVuLPaUVwE9GRf97Rhq2AGOUIB6JQLgHDvORrbRNB0CZoc4J1MGcRKkNUzQ%2FOHJYg6ebrq5v6b%2Fr3m27R6%2BaRzlk7FX1FEaO5fbXl4glmfWJJPhDVrO%2BOxslZ1cTRmCsQqbwgPGqvj3Gex7%2BGtCHTtKgSLVlyjLqT3kyxVc&X-Amz-Signature=4ea2680aca1f152541b2af5c440ff12bdb2527834b1735a4525efbb823eda7bf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTMXNLIH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDSE3koADe6aidPi6aJ1ScDeEM55JPRgTGXBVlSGxluqwIgTAlYVIN7bUGCjex8Ygys8LY41rFYWNAnVzwOTbf9z4gq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDIJMKhwGUx6XbvQ6RircAx4cjguuNX%2FICgbFcTZpmQyziQa77SM9xqCFG1ieTsOMG2U5jC0vKIguWfL9psyoALGQXhHtvEcYW8%2Fs9BZHWPfA7yd0KlFMawLnASqrd%2FKlAPCGL8Mm1szjmM9AAg6F6UEFvM%2BfhqwQOCKbUvuNnIFfaKRnMTnz0RZON9n2UqPMpVPQaeaaIIJCcgYByMhtbWx8yfl%2FUng8yrPKtZOnK6MLXL8FI%2BaSLMWTsQJ1p%2Fszdm69Rz%2FfEu5KCpJVulQfy0THqnoMdlcvbiBLyA4eeyhDCtOSdI6Dfs9HNyRlMW4DKNNgSZD3lp%2BULe3AuQEwAv9xrOqTiYK3%2FpGBuywI7n1ZRvtmOUrd%2BzPBah7HR%2FM%2F%2BLscqxbAQ2OciUGmpwUyTOmPI3MEJ3UFgGITfsZXevbRVRdrU5QaRT0OAPfSgwMDIA3uiVchrYAJV1RPY1795Bv6dkGQR1P%2B%2FSKztqZqMJugMCSzUxjR9TH92zASP4EP%2BHwRB2%2FKcACRSitASWsm%2BGjfI8lQuXoIn3C5lPw0Sm2HrlgQ3EwPx9LJYBhfKgPtkZfej3Mk96%2B%2BtYrcKWmwY1nPjpMdlRqzwS8fmUnPAhUfqJzxHXyL0nx2S5MFDkmjZb0kwXk60E7GRXfLMKyUir0GOqUBNj95mPVlVbTKN%2Fndj2nmqlYDThpmmwUKTnPHVP7UPKWwtZMfrOHhJBJbiLIsk7t2ELrkM8AyBqLM5eewiFtLDzd1zcSDRefqqjwW9Eez2ijyqiQnTKIDLfjOF5sPlK8wVqJiNzo2ZEPUxY%2Buo9qP3%2FAVEhnRRL1GfWnmCHJZC0g3tOMLcg53fFeahCLaQBnODqZIgT1trG82icHA3Xa7A1BaMETR&X-Amz-Signature=9dee084c726dd9ea380e0009ec28b025f4bcfa185140462b8761faea57a1449d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM4P2KO3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCouo3qTwKzsx3Ik22opakzIQulIhsbZE3ZzXom5e4VdgIhAJxPYf%2BljU8OjDpEs72oI6zQWXJgpH%2ByFwNApv71%2BePlKv8DCDcQABoMNjM3NDIzMTgzODA1Igy2tB5XMn6gHkGf%2FSMq3ANRzv0wunsp4YaDqJ5RK14sqT7AYDpoJXrSSaabQTEfSyzcL0k0rTmOgiGTAE3qux1mMwtBuymzTbJV%2FjzICJywKm7srMR2F1x21LA9l70fUFry5Brb8jl7HSDsjRaimyhKv7wx33ZxUt5LZEfsdy%2BzxkGuiN2BHFZCFnESMgs%2BlDG4AM4iCISOETPCtlmL2ghh3BwBsD%2BETcTpNTk46p8ytiUthx224r5YI3LCr9sTLvljjQXCK4RezYWU0l13fOoONbAX2z0%2BhubWFljFUR8lq7mx9KbOHJrFCUQubju8jzZu%2BbtwJNCEzz4LicIpC4CYYEgzLmxKRV1jhoivyABVkz8CpSKBoj%2FthcNisbVi2qNWEHQrVD5aQ1ETydqSM%2FSaTyD1BM7faUpy1nnlzr%2B087LNmTs2bPQVmQ0i4RPcmZOb9bPeuU6qNVzELH%2Bm7K2u7nLpYvPunTJ62X2f%2FZZmQVs3rmbxhpDFXzWaakSn7fFCGoRJtMFiqbhuUWTN603hFwCMq8hwzGQFnfWKup0XJ2Q5guXcYnsHAzJZVOzgQ5C3IblaV0lKlh8c%2Bt%2FJ8fjWrzpVbPsQTRNlMt99numz5Eydk34DBpEhjfbB35pfsKocQFjBK9slT%2BRY4zDblIq9BjqkAWYuQkr%2BweCOHcnR0I9Rpz7yPavHV2vHFoemMXjSDbsgEFm%2BkpfDblIsQrT%2FBiO%2BuTBpNTNKWy71bws1d2B0HnBK2ANkx40vCeqRMmH1bVXXe5bxqi4eLNj74dQblePjsRNGb5bMSiOdJEY9nT9H0YqKqolOFHOgHWbI1%2FS37dgT%2BwMPZh15a4iaGCE1nd36lP%2B0DbURYt5NZUmicB7YA%2FiexdsE&X-Amz-Signature=dfb30612832b6ac8ec07b7b30ebca4fbd7fa8dc65475c0535896e11383cf0ff6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5OWLP6Q%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDlwJCeE7eAdsnK9Rk64EE4CsKTxVcSZpt4tkjTFVuptQIhAK3igczed2KOye1uLrEp%2F89i37uZtjTnndPCYFJMoByuKv8DCDcQABoMNjM3NDIzMTgzODA1IgwwvvmC0kdv65UjXC8q3AO%2FYGqdpODLnLUJw6xfw%2FP1Ux3kX8BJfUwtsHGBikeO%2B%2BQObKaW81D5kpf4tprSm5JPn%2B6N0anLUMI3MAO9h6aVNfP3N4%2BXwRWuHMngkYYP0zYnHwlJOmie34AlqmIUSSg37hL6njnBoSKmAD5gqxmh1gGOg1zFwenVt2YSjkVSJuZEYgDoQZQZOVyDP5d6011QyMeEorwNBNWa7bFfkG8%2FvGtyqY8afCQhSWmYP1CT4HGascM8nlVHTtkAa%2BTg8UmOk6vu6tLp3u%2FnjZE77fJ5VvnLvYbarGYfv8MYobqpoCp8C%2B3lbZhh1%2FYbQJVHyKeS%2BZjAojRLF28SSkt4vJD8wRugvkMVgmMxCbyQ8z%2BvcSFCMfPkrMUkQ%2FgEmqRtSMq4khmRg5%2BMn6giLBZxDj3I%2F6DKO1U4j36HqIdhKXhbAOMtvm39zgNU%2BvG%2BFl%2BR3bst%2Bygbl8I%2B79yJVNWIfMdHs4PGMsbMWgwDhJWWtjNBVte8ACT3J2TfKn9v4Y9cVjY8YsZUgjkXHL4%2B73vfaZ7xYRHNEePSPp9Sz8GWgCKzk%2BMi5R0LUpLgE3tDv1PzrO6WdKvlX8S3LirCi%2ByaCLB%2BS9PAwFC3%2BRjgh%2Bzl5hBEtFol7TbxSN%2B9TM7GvTCUlIq9BjqkAatAYLhXc3g64RpNOf4gVgXcAl3wcrLRtaaj9B8QcJWhueK%2FTA2AQcVuLPaUVwE9GRf97Rhq2AGOUIB6JQLgHDvORrbRNB0CZoc4J1MGcRKkNUzQ%2FOHJYg6ebrq5v6b%2Fr3m27R6%2BaRzlk7FX1FEaO5fbXl4glmfWJJPhDVrO%2BOxslZ1cTRmCsQqbwgPGqvj3Gex7%2BGtCHTtKgSLVlyjLqT3kyxVc&X-Amz-Signature=c7782af1ff5b8c0a31bdeba0409ad6d2b4f514b30eeab530cbe7a2534c5f6692&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5OWLP6Q%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDlwJCeE7eAdsnK9Rk64EE4CsKTxVcSZpt4tkjTFVuptQIhAK3igczed2KOye1uLrEp%2F89i37uZtjTnndPCYFJMoByuKv8DCDcQABoMNjM3NDIzMTgzODA1IgwwvvmC0kdv65UjXC8q3AO%2FYGqdpODLnLUJw6xfw%2FP1Ux3kX8BJfUwtsHGBikeO%2B%2BQObKaW81D5kpf4tprSm5JPn%2B6N0anLUMI3MAO9h6aVNfP3N4%2BXwRWuHMngkYYP0zYnHwlJOmie34AlqmIUSSg37hL6njnBoSKmAD5gqxmh1gGOg1zFwenVt2YSjkVSJuZEYgDoQZQZOVyDP5d6011QyMeEorwNBNWa7bFfkG8%2FvGtyqY8afCQhSWmYP1CT4HGascM8nlVHTtkAa%2BTg8UmOk6vu6tLp3u%2FnjZE77fJ5VvnLvYbarGYfv8MYobqpoCp8C%2B3lbZhh1%2FYbQJVHyKeS%2BZjAojRLF28SSkt4vJD8wRugvkMVgmMxCbyQ8z%2BvcSFCMfPkrMUkQ%2FgEmqRtSMq4khmRg5%2BMn6giLBZxDj3I%2F6DKO1U4j36HqIdhKXhbAOMtvm39zgNU%2BvG%2BFl%2BR3bst%2Bygbl8I%2B79yJVNWIfMdHs4PGMsbMWgwDhJWWtjNBVte8ACT3J2TfKn9v4Y9cVjY8YsZUgjkXHL4%2B73vfaZ7xYRHNEePSPp9Sz8GWgCKzk%2BMi5R0LUpLgE3tDv1PzrO6WdKvlX8S3LirCi%2ByaCLB%2BS9PAwFC3%2BRjgh%2Bzl5hBEtFol7TbxSN%2B9TM7GvTCUlIq9BjqkAatAYLhXc3g64RpNOf4gVgXcAl3wcrLRtaaj9B8QcJWhueK%2FTA2AQcVuLPaUVwE9GRf97Rhq2AGOUIB6JQLgHDvORrbRNB0CZoc4J1MGcRKkNUzQ%2FOHJYg6ebrq5v6b%2Fr3m27R6%2BaRzlk7FX1FEaO5fbXl4glmfWJJPhDVrO%2BOxslZ1cTRmCsQqbwgPGqvj3Gex7%2BGtCHTtKgSLVlyjLqT3kyxVc&X-Amz-Signature=a0c35df10a2713ef389c2e1c329a478b3f65b15ba020024bef2d730e9d2f0518&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5OWLP6Q%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDlwJCeE7eAdsnK9Rk64EE4CsKTxVcSZpt4tkjTFVuptQIhAK3igczed2KOye1uLrEp%2F89i37uZtjTnndPCYFJMoByuKv8DCDcQABoMNjM3NDIzMTgzODA1IgwwvvmC0kdv65UjXC8q3AO%2FYGqdpODLnLUJw6xfw%2FP1Ux3kX8BJfUwtsHGBikeO%2B%2BQObKaW81D5kpf4tprSm5JPn%2B6N0anLUMI3MAO9h6aVNfP3N4%2BXwRWuHMngkYYP0zYnHwlJOmie34AlqmIUSSg37hL6njnBoSKmAD5gqxmh1gGOg1zFwenVt2YSjkVSJuZEYgDoQZQZOVyDP5d6011QyMeEorwNBNWa7bFfkG8%2FvGtyqY8afCQhSWmYP1CT4HGascM8nlVHTtkAa%2BTg8UmOk6vu6tLp3u%2FnjZE77fJ5VvnLvYbarGYfv8MYobqpoCp8C%2B3lbZhh1%2FYbQJVHyKeS%2BZjAojRLF28SSkt4vJD8wRugvkMVgmMxCbyQ8z%2BvcSFCMfPkrMUkQ%2FgEmqRtSMq4khmRg5%2BMn6giLBZxDj3I%2F6DKO1U4j36HqIdhKXhbAOMtvm39zgNU%2BvG%2BFl%2BR3bst%2Bygbl8I%2B79yJVNWIfMdHs4PGMsbMWgwDhJWWtjNBVte8ACT3J2TfKn9v4Y9cVjY8YsZUgjkXHL4%2B73vfaZ7xYRHNEePSPp9Sz8GWgCKzk%2BMi5R0LUpLgE3tDv1PzrO6WdKvlX8S3LirCi%2ByaCLB%2BS9PAwFC3%2BRjgh%2Bzl5hBEtFol7TbxSN%2B9TM7GvTCUlIq9BjqkAatAYLhXc3g64RpNOf4gVgXcAl3wcrLRtaaj9B8QcJWhueK%2FTA2AQcVuLPaUVwE9GRf97Rhq2AGOUIB6JQLgHDvORrbRNB0CZoc4J1MGcRKkNUzQ%2FOHJYg6ebrq5v6b%2Fr3m27R6%2BaRzlk7FX1FEaO5fbXl4glmfWJJPhDVrO%2BOxslZ1cTRmCsQqbwgPGqvj3Gex7%2BGtCHTtKgSLVlyjLqT3kyxVc&X-Amz-Signature=71b42a79ab1a7bff7045d2c199d7bfe97b3c070c039456960dec3ea1dc21dd03&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUNBW7VL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIHhZgZD5ZUX6Rqtaziq7vTx2LR9NOpaILtKVguvIjLz5AiAWFL5GWWra1NI7szWUa8nv1vfzriLayQb9TQOUTyVM%2Fir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMX9nBW5wuxggmO4x6KtwDOiZsgfCCJh%2BCCY2B52u6FlZVgywvIErgy7umAHYf2%2FdvM4PO36EeW7l7zk%2BUx%2FFEYcQGOPLRRlDwpPXYB6c8LT2wLVQ7qH4pWgny7fBX8C05bVnjVJEGWL6LHTCd5RtS9MkRyQ0POCRDSMsQbAybDAp4TtEltsj9TmXEQJjgmMD8Ov9SACyASbUpc8SbczA%2BPN60Nj5qrSMF%2FOtI63T%2FdwBWRudk1RrQ9KYPeuIJ0K%2FgoqjUM5I%2BOKPbJ18fzvYkFKyS6S9rogNe5ZjKRJEoOP2km2b0ou05E9loYtN2acsvl609oBUo7teE3ph7xDII2mOPREUD0sL3lYXeBx6hHIz4oaOI8wnkJj4TOuBNUQ747mqE07kH6LEzx33pvJmFVCWtIDIPmc0sc%2BawcJKGut39kYPrTZFzlV%2F5x3cvHzp0t1NRxfGTFEf1zMo4YifC10rVn%2B3FkfrWdJdBuo6nYIlW85loPgcDJ0jw521H0B3kXpgK9sSZAUn3hsctdz2uJt9ujZOezgxy2LjGtIGswrtunitCpjJ1R43EKvoAzCh1vApETZrpfxD5GFqWjHY8DepB45sG%2FUuptBOLWIIAn43c53hcG9Tv4nMmlL%2FEODep%2FJMJcBxEHeopLoIw%2F5OKvQY6pgH%2BepLtUEzAPa6xSLLBG2UQpAsOqrxL4w5kg5ZSDj93PXLXLt7HzNlMOWL4LjZY6xdCO9vMPbTYFfBRvj2CCvrjLqbkXRETENJfwP2CGvc7o%2Bj%2F%2BMcp%2BBG8y9cGiblV5MxYVduZZzRIDvqFuE%2FbD6vjfFh6cDflV0ib%2Bi3pAnwkyzm%2B5HBT2aLUPSqm2QLCsj01rldQ3cUVbdrfKcNJ9hdHBHWudf60&X-Amz-Signature=3b1abdb10891071154f743d8c42854c1da7d6c5bfd978124fad8a898ac8ae7ec&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SNQDU3R%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIHYECNPbtbhHQRCanF6aXMTJnLSAlBlZhnJWpoUMXVdvAiAnMLgQNCGqtFfP2oXxZ%2FtU91PV4ZRfYwl9HBkeWNSYgir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMG9WTfp8n88dMZTg6KtwD%2BGyqbSkHnwQZqf7Lmlz9HSj3Cg9xrui3LGuFHUeuJ4iwCS6Ua3%2BCej97gDGk0ifRrHLABdrveXRLq%2BwnE%2FbaFN6%2FccqRUYumvf5a3wzOSNN56c%2FRzz8J50yJgyAsFLvYO2%2BYzByicL1euhddx1wzWEpZnnlmC1CjJ0R6M6%2BtHorZiw%2FT0PoUALL1Kv4Li%2F8h0paYzp1VFlvDNPnMAfTd2cQtrY6P5vVVGRIKDwwcGu%2B%2FRx62gI76IYyH1LAWbSSFX5DFgNN7n5JExar7PZFwdUaPbsHDpOczDupRWF2AYSU6Xgpe1i5qKgpY8Rw9ZG%2BGcv%2BSru15xUdKBu6G0Eyq%2FwZnOWMeBmrOFSH2VlNmkbZnFMY3h0%2FWAvPIFbzjRt%2FG%2FpfjjPsdM3zRum2zzBtCBi5K%2FHiEWVDG%2FzSQQKuFmq%2FiWJGnYAP5LOvPxnhppINS560h0egs5W57DsE6s24awBl5u9zNZEq4AMXtcawlbEaVfPG6nhD4%2BmUHV5%2F3sYXu69Ob9Eg0sdDRltN6ByqVga6k9rejyiBQW6CYi1%2FfS92zXNhDOxZGJi6CParUJ9EJsS2u%2BH1AUp8UHlZ0jwY%2FWVmQNTMQ4wgzzXhh%2BqnM2WWpfiOGYyTE6tvc7RQwqpSKvQY6pgEoxEvLfNH1TgzBpC8ABUTXl4tkgaiHOlxogu7x7OFJRSpKcsQqnrezoIE8QZSrEEUufAqX%2BQmOTiHnRZgBKyC2wUkLeS0yhw2%2BoeCzukHH%2BTfojANEB6j%2Bqu2LNBDHnRifTTSLQ0E2EUBy%2BGzN9VdnbBNodgyZfqEpF27HfM9k7GsVdECVLo2%2BtXAOTl%2FpN62t8Lu%2FyxfcSqqmaxU5IRwHdkZEHW94&X-Amz-Signature=bc46dc6294de8f82120ed24412c496a54195b9ed026a9f80b90cc63bfc648fce&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEV6AMRN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQCoNI%2FNERIPeZLgDTxLrhDJoptzy%2B3WUxN2VlUjk6La4gIgY4LPzQVFrAW%2BvJ007GzwNvqF0IjrIuorYM5k3U8N6bAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDIm4KYZqJD%2B1TgpEhircAy%2Ff7WCcwZU8621LX5vEmVTE44lJpcdxZFgGxCFLoWi54fs0zo4lyS7IPH2ovd3CREFBKYmv%2BKDaF6KOmmeQ7Y4SH3jFiwDVwdaHX0B%2F16u%2BjHXvQbjvpU2bKSKFdX9n3o2tXhHpxnJTP9dxNFopMaZbs6%2FtZXbaNeSr4Abk%2Bv6wakaKQIeTfvFbSiiSPLCNsUHXzg8WaKh6bYo8LWcqKmSlgix1S9VZVivCm7txWM9MYcJgfk6zJnJ%2FdpC3sqD4YFId%2BlO0nr4sI21NKnd2BDowI%2BuizULEy2ERbhVG566cIzZp830MRicqlDKYQ%2FBrZTGJUjYCHi6%2Fsn9JNuUpOwOvzqwH8Nwo6nwCRIzmEgHGtXQiVSF7hz2iH9ll6UK5YlK%2FV%2BHG0l1WTwVXmInoKmMMu5fiCibQuvlRCze1j1UdT0GvpSrsZDOgY7DL8QT8z%2Fv60cHUGlPURO0px4u96%2Fa%2Bs4G9nzx5kJoGARi%2BNYdaADgFkg%2FKPdTCsKhc6s0LaF3zkmo%2Fbh6ax8ip0RxSW7bFEsmKFkCfFvZLppUNFKClKY8BxxYsdupoibSR6S%2B51AnGK2PU%2FA9O1a%2FnEwe43sJGCnfM2u0eH%2B%2FnPGxFk7Jeek4xdnzIzDCET1D%2FMKqUir0GOqUB6QAsd4r1z%2FNuN8Jpe1fgBvyZjK1xshcWm%2BpEz%2BOfF49N3z0hIiTZKuSAq%2BVDs%2Bkk39KgYd1gI1CvhHmglEMhdAinOazcTruPs%2BDFZSJIABhAQDwI52AQ%2FUtfuW6g3TSv5hvqHW0QenNqi4kj8W7nwAYULeqnfibWnK0IOTXAIlVqx7DIDUzd2T7w5Rom9UG8ptDuwA76pHg4KQ3cq77wqS4hmjZT&X-Amz-Signature=099b1b2f46557cc7d8925f60c209ebef95952c5a2df64d5487ec6728b441135f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DOTSZVP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQD2DGFSsWWea5amAcpA6rSXfLhkwDgumN6CcarsQgkBZwIgQer5MUXDCHOOGUvAK8x7MrWqFccN%2F5Nugo6onK3cMVwq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDNNNWmYOKp%2BE9RhrQircA9k9ryTAN%2FvssIdMHOjXy3mYQeQVX9hnI%2FPUaa5gqIMoO6QIa4ga55I12hSU%2FsWCCvnYgahIQ5AKc9uuoFLkJfqyMq758MScyXiq6mYvWilRNRNh7uLfFxcxE2bXBm7SSmgtYQt3SfKy0Tf5FWA5i1NpXbjnv0zvrXWbB8idMV6ikyWWW%2BeFO1zjSM6Ylefl1JS5HLJ2qY0S53WdIHeLsFQGVD67sh0wZDMnCx8%2BGqiue25Co3nXDGh08dKec%2BY%2FLqbrHh4r%2F2Y2t8CBQqWQvHYmM1qgePQe8EV%2FVyLjTAGV3BxfIhShZM69tjslORWTRURfD%2FUXqX8t6l1eIGIaj%2FX1HzTkPWC7a%2FdJaS0tCiJhyhGGZz%2FledxtLIv1kX76fWdvGKF8lphvSTBpqfcpOqpE17BnXF0pyvgtieEB5yBcrVL7bFGJGIBFwRswpx2Xbs9mY%2Fg0CT6DyULT34DQX4wQgAfhWgx7JagSxF%2FLw1mMfDgXp1ISPmIddnRwUbqzfKCsfuNbOWd%2FzFl3aswWwNojeeNw0%2FEuE6mJpPMFRY2chc%2Bns0%2B9k4CTGYBYQ0T1wsTJeAjpSxoC1AcRbyFWi6ZsWlC3tiwmTrBgqdHhjb1%2BpQ6AlqziQdFGRv3jMIGUir0GOqUBHuSuj1z7mk3UQcXM5ucDP7%2BXb%2BDBvTjLAl8Jr2ST2FNzhNeaguOZWh5xYdAI2PCFCFVb%2Blt9NVUWj3La%2BNrQPgnhIjbdrPUbc%2BWxV6I%2FSftwp8xSUiE0N%2FFtWBSWn6Kjx1qGqjYIW1e%2BT7y51ni%2FL0fjlFQCkX4sbHQgDKGNu%2FHeoQiMtugYfT4Onnn6N8uGbRhoyu323nYldxpyGpTrHW16HLFF&X-Amz-Signature=f22dc34364beadf36055b1fd9e176db29bc721459996689b66e3cd8ddef459f7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DOTSZVP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQD2DGFSsWWea5amAcpA6rSXfLhkwDgumN6CcarsQgkBZwIgQer5MUXDCHOOGUvAK8x7MrWqFccN%2F5Nugo6onK3cMVwq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDNNNWmYOKp%2BE9RhrQircA9k9ryTAN%2FvssIdMHOjXy3mYQeQVX9hnI%2FPUaa5gqIMoO6QIa4ga55I12hSU%2FsWCCvnYgahIQ5AKc9uuoFLkJfqyMq758MScyXiq6mYvWilRNRNh7uLfFxcxE2bXBm7SSmgtYQt3SfKy0Tf5FWA5i1NpXbjnv0zvrXWbB8idMV6ikyWWW%2BeFO1zjSM6Ylefl1JS5HLJ2qY0S53WdIHeLsFQGVD67sh0wZDMnCx8%2BGqiue25Co3nXDGh08dKec%2BY%2FLqbrHh4r%2F2Y2t8CBQqWQvHYmM1qgePQe8EV%2FVyLjTAGV3BxfIhShZM69tjslORWTRURfD%2FUXqX8t6l1eIGIaj%2FX1HzTkPWC7a%2FdJaS0tCiJhyhGGZz%2FledxtLIv1kX76fWdvGKF8lphvSTBpqfcpOqpE17BnXF0pyvgtieEB5yBcrVL7bFGJGIBFwRswpx2Xbs9mY%2Fg0CT6DyULT34DQX4wQgAfhWgx7JagSxF%2FLw1mMfDgXp1ISPmIddnRwUbqzfKCsfuNbOWd%2FzFl3aswWwNojeeNw0%2FEuE6mJpPMFRY2chc%2Bns0%2B9k4CTGYBYQ0T1wsTJeAjpSxoC1AcRbyFWi6ZsWlC3tiwmTrBgqdHhjb1%2BpQ6AlqziQdFGRv3jMIGUir0GOqUBHuSuj1z7mk3UQcXM5ucDP7%2BXb%2BDBvTjLAl8Jr2ST2FNzhNeaguOZWh5xYdAI2PCFCFVb%2Blt9NVUWj3La%2BNrQPgnhIjbdrPUbc%2BWxV6I%2FSftwp8xSUiE0N%2FFtWBSWn6Kjx1qGqjYIW1e%2BT7y51ni%2FL0fjlFQCkX4sbHQgDKGNu%2FHeoQiMtugYfT4Onnn6N8uGbRhoyu323nYldxpyGpTrHW16HLFF&X-Amz-Signature=4df7d33349ffa90365b525f400f2425070c6876a28f0a2d3ffa8444db2e657e8&X-Amz-SignedHeaders=host&x-id=GetObject)

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
