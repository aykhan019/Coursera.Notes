

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=a2fb8131b41298e4ee1f4090aa7be5dbaaa821c273df816b684b9df62a9af4a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=60f4bafbe2995ebe3aa60bfb4f393eeb80f201c812ba37eaf17120825ca35582&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVEEJ2T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGymL5Yk6yovzuZJ%2FBegfu3vqoyNnxjNTSLBcYkAfuXgAiAuOA4bDkwvJa62sTYGbjoouSeoV%2B%2BytKIpBeDT4i8JFyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnJpAQprgEemt18%2BRKtwD6E8bt8BAwFkS%2Fr6t5%2B1A8AwYUcU4Eh9tay6BJH5z6nDPyJBn9X1gLHBCioQz4P%2B8Qfn1gEOt2U1pQMyLzhgaEYJBNw3ji1Dk6NdgynQM6v6AA1f%2BoZufZlOIN3Jc5B2vktfBAwax0dZTCfo6c0Kg6%2FE6bWyBCzzwG0mXIOfPCyj3IsYfQd%2FJcOp4f3tuN0ucQXpCWq5VcbdxOMMNg9TwQ3kYbu%2B71gRxiHcMGzIad7JZG9k%2FhHKV8WRWrFErhgL7vamFPmvDipAsTIbgm4%2B0SEtE348kcPq5uYclKkR2kdSaKVsNtR1FkoCP9zloBfyON3JvC9pnwH9JBdAQ4Qxn05%2FRAhAUr%2BbYkaZsIqIM9Ng51NzeoS5pVs%2FTArxPRheVyB1jf32gGZbVTplPtTxSFCc38MPftRFk2lSUXBYtglJYBUlYlsbnHi8GeV%2F9HsqEAcjZfcKCCvyxLbN52rBOyimx%2Be%2F%2BOHb%2Fi91mL0IiNDlkyGR6kYILkPnxBNnWcea7Zn%2BINN2tEqDarUcKMqRZuol%2BodsvHjvbd9J9AWrZhOkACGOM8Ppfk1gwcbkInCJrjwSYU3Zpw6KmucWNNcnd1MJ%2FzhAPvA1GlW8LVNNfvkYWSXcrlGPDlwa8OG4w146cvQY6pgG4JQADrZL6vvWSGgyIA%2B0mQDwkWrQMLS9szB2PlY59CP%2FgdLgbvOs1BdNPdvGPu6yQhwBI%2FJ2aJ4inTNrnggfEpPxCi%2FrqEQ1Czduu2yj7EGtMvOikDC86kpOfxNTcnhtILQsfkdA3%2Bn2zCzi0RVj1Z9Z8CD02JZTWxtucLw9NI1NKqlTcQQ5ZSbEj%2F7DJEVJoACq%2FlM7GqfcsrUOyhGzBt4icqIs3&X-Amz-Signature=6e3553797f690bdf51a14db9554b6ad11490ee511e6d3958a00840efdb8a70b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OTFW5I5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD0zqG29msali3Ad5U7SNfvylhJs2rmx9JZwXvhKwU24gIgY1KZ%2BTBFk3aVVqTcNfdkHihxlzjMOSn77EAoazoyu9IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3rfLqHrHKoeCUNfCrcA4wNs5ULmyKHZwMpepsqJjEGTIQmxnoJnhhLN%2BHrOxDcdpLHonwgbXl5TcCXfKdOZX%2B8THoF%2Bnz9AHBU1Y1kj59f8cU3nPrNEZizPmBNCCxpGY0NwwGp1pe%2B5OLIyTfmKNxogtvxGkMuMbwbtImUT2cWtZbb%2BI9O2KnEbDpWHhyjMcvUjOSdMvcCUYIAtW7EnUaGqLBxKCxx609qz%2BYnYEbWpWcfDQQQpRoChEXJ%2FgfUie8yToEHHCiXkO%2FMGQWVnYsga5%2B%2FtkOrREBTdtM1MpgE6Vi%2B693OitWjJqXPydDLkv%2BejafDGdM4%2FOe%2FsgOPnmefFO1yyO9q0J3q5GlFyrqlDaXQIyStNDchZiEzrMYXd8AkjC506B%2FbaHKz0zT%2FnJw1FOATZmFrzi%2BvDTXedH7ebhRBdmAy7YlrVFk09Wd68dG14spSd3krqwPPW1zMRPw0w0sWpwXeE6tZU62j4cpGayXkG0i7FAdbjcroepySIzaIHfDGyU%2B5AuCftOOrmCJeIqa5rXhS041Z1DhwBmMPhABptPeyb5OORNAT1vH5b4rYA%2FvGDMptFT9bhpfrJJNyI1KAjziWqqyfDr2yKhkZ%2B%2BApKcyAGjLxN%2BY8hZJf5t4mEvNT2Lau75DQMNuOnL0GOqUBiBsTPHkgTe7aN84A7dEy49cvwdzUnmrcFb9rN3umuaB53l%2FdWIijxC9cKRLtT%2B%2FdbQTVDYNUJBGjsHkETANCmoj8wrGQWdSlZxySHE2awWMRZcAMTXnWC%2BZki0iL07jFD7M%2FvIujztg%2FcIELeFv1bZnzFeGZA4EiSGL6eLYMPHm5tT19Mh2AxnaMf%2FW2JnMGcKCmfhM4%2FKexpBi7K8RrZOoJ69e%2B&X-Amz-Signature=92c213b96950e5f98154e503f575c13d3e56bc7cb146ae39342d7a01b42fadce&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OTFW5I5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD0zqG29msali3Ad5U7SNfvylhJs2rmx9JZwXvhKwU24gIgY1KZ%2BTBFk3aVVqTcNfdkHihxlzjMOSn77EAoazoyu9IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3rfLqHrHKoeCUNfCrcA4wNs5ULmyKHZwMpepsqJjEGTIQmxnoJnhhLN%2BHrOxDcdpLHonwgbXl5TcCXfKdOZX%2B8THoF%2Bnz9AHBU1Y1kj59f8cU3nPrNEZizPmBNCCxpGY0NwwGp1pe%2B5OLIyTfmKNxogtvxGkMuMbwbtImUT2cWtZbb%2BI9O2KnEbDpWHhyjMcvUjOSdMvcCUYIAtW7EnUaGqLBxKCxx609qz%2BYnYEbWpWcfDQQQpRoChEXJ%2FgfUie8yToEHHCiXkO%2FMGQWVnYsga5%2B%2FtkOrREBTdtM1MpgE6Vi%2B693OitWjJqXPydDLkv%2BejafDGdM4%2FOe%2FsgOPnmefFO1yyO9q0J3q5GlFyrqlDaXQIyStNDchZiEzrMYXd8AkjC506B%2FbaHKz0zT%2FnJw1FOATZmFrzi%2BvDTXedH7ebhRBdmAy7YlrVFk09Wd68dG14spSd3krqwPPW1zMRPw0w0sWpwXeE6tZU62j4cpGayXkG0i7FAdbjcroepySIzaIHfDGyU%2B5AuCftOOrmCJeIqa5rXhS041Z1DhwBmMPhABptPeyb5OORNAT1vH5b4rYA%2FvGDMptFT9bhpfrJJNyI1KAjziWqqyfDr2yKhkZ%2B%2BApKcyAGjLxN%2BY8hZJf5t4mEvNT2Lau75DQMNuOnL0GOqUBiBsTPHkgTe7aN84A7dEy49cvwdzUnmrcFb9rN3umuaB53l%2FdWIijxC9cKRLtT%2B%2FdbQTVDYNUJBGjsHkETANCmoj8wrGQWdSlZxySHE2awWMRZcAMTXnWC%2BZki0iL07jFD7M%2FvIujztg%2FcIELeFv1bZnzFeGZA4EiSGL6eLYMPHm5tT19Mh2AxnaMf%2FW2JnMGcKCmfhM4%2FKexpBi7K8RrZOoJ69e%2B&X-Amz-Signature=a885c7f1385e36b655c3c762a6c5c096c2cc1df75bda234dc0b35ad127ada046&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OTFW5I5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD0zqG29msali3Ad5U7SNfvylhJs2rmx9JZwXvhKwU24gIgY1KZ%2BTBFk3aVVqTcNfdkHihxlzjMOSn77EAoazoyu9IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3rfLqHrHKoeCUNfCrcA4wNs5ULmyKHZwMpepsqJjEGTIQmxnoJnhhLN%2BHrOxDcdpLHonwgbXl5TcCXfKdOZX%2B8THoF%2Bnz9AHBU1Y1kj59f8cU3nPrNEZizPmBNCCxpGY0NwwGp1pe%2B5OLIyTfmKNxogtvxGkMuMbwbtImUT2cWtZbb%2BI9O2KnEbDpWHhyjMcvUjOSdMvcCUYIAtW7EnUaGqLBxKCxx609qz%2BYnYEbWpWcfDQQQpRoChEXJ%2FgfUie8yToEHHCiXkO%2FMGQWVnYsga5%2B%2FtkOrREBTdtM1MpgE6Vi%2B693OitWjJqXPydDLkv%2BejafDGdM4%2FOe%2FsgOPnmefFO1yyO9q0J3q5GlFyrqlDaXQIyStNDchZiEzrMYXd8AkjC506B%2FbaHKz0zT%2FnJw1FOATZmFrzi%2BvDTXedH7ebhRBdmAy7YlrVFk09Wd68dG14spSd3krqwPPW1zMRPw0w0sWpwXeE6tZU62j4cpGayXkG0i7FAdbjcroepySIzaIHfDGyU%2B5AuCftOOrmCJeIqa5rXhS041Z1DhwBmMPhABptPeyb5OORNAT1vH5b4rYA%2FvGDMptFT9bhpfrJJNyI1KAjziWqqyfDr2yKhkZ%2B%2BApKcyAGjLxN%2BY8hZJf5t4mEvNT2Lau75DQMNuOnL0GOqUBiBsTPHkgTe7aN84A7dEy49cvwdzUnmrcFb9rN3umuaB53l%2FdWIijxC9cKRLtT%2B%2FdbQTVDYNUJBGjsHkETANCmoj8wrGQWdSlZxySHE2awWMRZcAMTXnWC%2BZki0iL07jFD7M%2FvIujztg%2FcIELeFv1bZnzFeGZA4EiSGL6eLYMPHm5tT19Mh2AxnaMf%2FW2JnMGcKCmfhM4%2FKexpBi7K8RrZOoJ69e%2B&X-Amz-Signature=64d5a3185a6e17d715688b2b3c461a09d818df895e11ba50510c63f20e478199&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OTFW5I5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD0zqG29msali3Ad5U7SNfvylhJs2rmx9JZwXvhKwU24gIgY1KZ%2BTBFk3aVVqTcNfdkHihxlzjMOSn77EAoazoyu9IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3rfLqHrHKoeCUNfCrcA4wNs5ULmyKHZwMpepsqJjEGTIQmxnoJnhhLN%2BHrOxDcdpLHonwgbXl5TcCXfKdOZX%2B8THoF%2Bnz9AHBU1Y1kj59f8cU3nPrNEZizPmBNCCxpGY0NwwGp1pe%2B5OLIyTfmKNxogtvxGkMuMbwbtImUT2cWtZbb%2BI9O2KnEbDpWHhyjMcvUjOSdMvcCUYIAtW7EnUaGqLBxKCxx609qz%2BYnYEbWpWcfDQQQpRoChEXJ%2FgfUie8yToEHHCiXkO%2FMGQWVnYsga5%2B%2FtkOrREBTdtM1MpgE6Vi%2B693OitWjJqXPydDLkv%2BejafDGdM4%2FOe%2FsgOPnmefFO1yyO9q0J3q5GlFyrqlDaXQIyStNDchZiEzrMYXd8AkjC506B%2FbaHKz0zT%2FnJw1FOATZmFrzi%2BvDTXedH7ebhRBdmAy7YlrVFk09Wd68dG14spSd3krqwPPW1zMRPw0w0sWpwXeE6tZU62j4cpGayXkG0i7FAdbjcroepySIzaIHfDGyU%2B5AuCftOOrmCJeIqa5rXhS041Z1DhwBmMPhABptPeyb5OORNAT1vH5b4rYA%2FvGDMptFT9bhpfrJJNyI1KAjziWqqyfDr2yKhkZ%2B%2BApKcyAGjLxN%2BY8hZJf5t4mEvNT2Lau75DQMNuOnL0GOqUBiBsTPHkgTe7aN84A7dEy49cvwdzUnmrcFb9rN3umuaB53l%2FdWIijxC9cKRLtT%2B%2FdbQTVDYNUJBGjsHkETANCmoj8wrGQWdSlZxySHE2awWMRZcAMTXnWC%2BZki0iL07jFD7M%2FvIujztg%2FcIELeFv1bZnzFeGZA4EiSGL6eLYMPHm5tT19Mh2AxnaMf%2FW2JnMGcKCmfhM4%2FKexpBi7K8RrZOoJ69e%2B&X-Amz-Signature=1d2b90e8d37a28beb00699286bac7651366a3432fe5a92d83e54f096989e309c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OTFW5I5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD0zqG29msali3Ad5U7SNfvylhJs2rmx9JZwXvhKwU24gIgY1KZ%2BTBFk3aVVqTcNfdkHihxlzjMOSn77EAoazoyu9IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3rfLqHrHKoeCUNfCrcA4wNs5ULmyKHZwMpepsqJjEGTIQmxnoJnhhLN%2BHrOxDcdpLHonwgbXl5TcCXfKdOZX%2B8THoF%2Bnz9AHBU1Y1kj59f8cU3nPrNEZizPmBNCCxpGY0NwwGp1pe%2B5OLIyTfmKNxogtvxGkMuMbwbtImUT2cWtZbb%2BI9O2KnEbDpWHhyjMcvUjOSdMvcCUYIAtW7EnUaGqLBxKCxx609qz%2BYnYEbWpWcfDQQQpRoChEXJ%2FgfUie8yToEHHCiXkO%2FMGQWVnYsga5%2B%2FtkOrREBTdtM1MpgE6Vi%2B693OitWjJqXPydDLkv%2BejafDGdM4%2FOe%2FsgOPnmefFO1yyO9q0J3q5GlFyrqlDaXQIyStNDchZiEzrMYXd8AkjC506B%2FbaHKz0zT%2FnJw1FOATZmFrzi%2BvDTXedH7ebhRBdmAy7YlrVFk09Wd68dG14spSd3krqwPPW1zMRPw0w0sWpwXeE6tZU62j4cpGayXkG0i7FAdbjcroepySIzaIHfDGyU%2B5AuCftOOrmCJeIqa5rXhS041Z1DhwBmMPhABptPeyb5OORNAT1vH5b4rYA%2FvGDMptFT9bhpfrJJNyI1KAjziWqqyfDr2yKhkZ%2B%2BApKcyAGjLxN%2BY8hZJf5t4mEvNT2Lau75DQMNuOnL0GOqUBiBsTPHkgTe7aN84A7dEy49cvwdzUnmrcFb9rN3umuaB53l%2FdWIijxC9cKRLtT%2B%2FdbQTVDYNUJBGjsHkETANCmoj8wrGQWdSlZxySHE2awWMRZcAMTXnWC%2BZki0iL07jFD7M%2FvIujztg%2FcIELeFv1bZnzFeGZA4EiSGL6eLYMPHm5tT19Mh2AxnaMf%2FW2JnMGcKCmfhM4%2FKexpBi7K8RrZOoJ69e%2B&X-Amz-Signature=2fda051bc67536ff0012a9c14506abf825c690aba58e508472450525823f60e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OTFW5I5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD0zqG29msali3Ad5U7SNfvylhJs2rmx9JZwXvhKwU24gIgY1KZ%2BTBFk3aVVqTcNfdkHihxlzjMOSn77EAoazoyu9IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3rfLqHrHKoeCUNfCrcA4wNs5ULmyKHZwMpepsqJjEGTIQmxnoJnhhLN%2BHrOxDcdpLHonwgbXl5TcCXfKdOZX%2B8THoF%2Bnz9AHBU1Y1kj59f8cU3nPrNEZizPmBNCCxpGY0NwwGp1pe%2B5OLIyTfmKNxogtvxGkMuMbwbtImUT2cWtZbb%2BI9O2KnEbDpWHhyjMcvUjOSdMvcCUYIAtW7EnUaGqLBxKCxx609qz%2BYnYEbWpWcfDQQQpRoChEXJ%2FgfUie8yToEHHCiXkO%2FMGQWVnYsga5%2B%2FtkOrREBTdtM1MpgE6Vi%2B693OitWjJqXPydDLkv%2BejafDGdM4%2FOe%2FsgOPnmefFO1yyO9q0J3q5GlFyrqlDaXQIyStNDchZiEzrMYXd8AkjC506B%2FbaHKz0zT%2FnJw1FOATZmFrzi%2BvDTXedH7ebhRBdmAy7YlrVFk09Wd68dG14spSd3krqwPPW1zMRPw0w0sWpwXeE6tZU62j4cpGayXkG0i7FAdbjcroepySIzaIHfDGyU%2B5AuCftOOrmCJeIqa5rXhS041Z1DhwBmMPhABptPeyb5OORNAT1vH5b4rYA%2FvGDMptFT9bhpfrJJNyI1KAjziWqqyfDr2yKhkZ%2B%2BApKcyAGjLxN%2BY8hZJf5t4mEvNT2Lau75DQMNuOnL0GOqUBiBsTPHkgTe7aN84A7dEy49cvwdzUnmrcFb9rN3umuaB53l%2FdWIijxC9cKRLtT%2B%2FdbQTVDYNUJBGjsHkETANCmoj8wrGQWdSlZxySHE2awWMRZcAMTXnWC%2BZki0iL07jFD7M%2FvIujztg%2FcIELeFv1bZnzFeGZA4EiSGL6eLYMPHm5tT19Mh2AxnaMf%2FW2JnMGcKCmfhM4%2FKexpBi7K8RrZOoJ69e%2B&X-Amz-Signature=1d6c91035f2c02d03b17bc4e6a8a513adb2e78d1b69fd279792d4623614d19ae&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PATAXYH%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIEpleZF2bRffkJxWK%2B662wV1tuGKmr14MXlQ0kiNN196AiEAg6b%2BhBwn9NZDHBriofcHaMpxuZE2luWfki300ETxf%2FAqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKSNDYIe0oCz3Y0ZzyrcA6SmM5KQoXDFAZiSrTR0KVcNEJJkA6EO0N%2BGG8q1p89CrLQJzWpArtoHZrf75acGjy26jEPGy4AIOfyZMggU0IzxnKn9PcPjuyJlwtKELyR0yo03U3phuU4bAkMI8hqC8K9HX5aXARKoZ%2F82owX1C2XElX7qTA2PE2sWbsVPAq2%2BtG8Q4%2BoCoa%2B9pCrmV2eCEslDjJVkuF74eCSeZqs3mWoHbDqToeDxNQThz1KgLurPO0iItpC7FQBJW5zDL6imbSLMR5Oa22PfnUH44rBXWfwqaTxFW6yc6fRCwCz1y4t5YQ%2BwI5T%2F8pPnJSDPrW%2ByoM73HkJieXE9Un6U%2B3bB9CPZfxGbqKMywqnWZipb7shDjyTx381dFE2uOzapnYiVEoVKRt9zNdyhVRGHlVNFyYFLi4BLysVLwrX7LEwgOv%2FwGRInF86gvt0TWotNOV1uQbRWjSxIMlYYvvBpkBjdCmHVFPyS9kIMlu1tA5ImL1A2YztRODMliuyYC9BNGiyz6yQHrwcpYP71yQu9p3COAt0Jmb%2FAeeolshSpqNsySrIa6BIuSIhlxodL4U%2BNvasFvHMgncotMPtMsHLHGPEYOs6X5ZVDbUtKIgKQRcnZqQQk1XdRvEJ7mJz%2F%2FF5fMIGOnL0GOqUBYDYAwqevFrZEf2f7%2FdOsWompxx7EdWRyjTKBHKwlHqcL0m8mBZMHT5x%2Bs0%2BixVLlVgzjK5doioky%2BfJ8rhN%2FRnQJ1Y7a9XmX%2Fac4sWnfJH5wO3Ky9pjofx2TplF0l2X5EotbStyr65wMRQiDMfHldOZlHdC8oAMOAyEms3ik6d3UNHoftYGK7OHpIP945LFLsilUa2CE2eZMnTZSmBGmKIEaiON0&X-Amz-Signature=8d9e82d0dd5ad9fc2b3b2697d689416676146246fd133325c1a7918a29a01629&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LVWN44T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDr9XiWFamRAAeY4Dd3fVgKZ7V4KRH5yV4xEF761qDN3AIhAKxPl8gTZ6hk2hfp3sPChXcd4IGL2vHU6ad00CEry3XpKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzl3e9wF6LEjfr7wDgq3AMp22uJvXtzHmWPkYzIvFnANBrFRbVLmJtVsEGi7FPSDGD%2F8g82vGozYgthYSJ79nsEyq0N3FwOKxGVoFMfFVuBT8XmIPxk3HoMFybgXjdw0TlAXtEDrIa7pQDMenvKD1VdILfXiTgwFcw55imrwts%2BVBTKRB%2F4S29eiHob1bjgI1WM4BqEowy2L7woiWEmbtbvRvPSuoGzcST94xdOfffVBkLLwB8ysdqV%2Bkpu3o865DuwCp2%2FkzBt1aC9wl6lwyM444bRX4E1NaVvbCSbf%2B0P9g4SJ6KtRewi9DkL4ATsYyj7rlZwaaOANOC133%2FG1bpN%2BeSHp54BR03Ci9F5NucY6gS54hbLyo23W32lBXU%2BcrZFAEIv%2B%2FPlchfFLVuFkRHesTrK9RmciCAQVIewDEwz%2F7cxgfMzo9TCH2ycpT7H8b0EZBeoUrDmBd5n1qsG%2FmU%2FYbyIncyO3SNNswDGD9HUNXRAesE2CGevKzPjWUPFCNKBLyFHIXxwDa7FuN1ioHjapXf0%2FeBFmW04i2fYnR84Q8TWl%2FLGk54r3BRcqN%2BxT%2BanMrSQPfslcPjnfZfecjmkjr7vx3Nk9mAe1QVhSG0AsdNzXoFXZlaCJNhtJwjNo1Ie5lUIEfj3pbk%2F0jCHjpy9BjqkAeqeIUmpyC7ElRFv2tVy2KccWQl9zDOLh6%2Fq9w2Ach510FvTcMlBv1qSbH8QhP0BWjD3vT2EzvgQIwFH8c3T%2Fxvb3HTBTC4ujCfwKSTACBbluFkkHZ%2F4sxe8in53quLDKIAGpEZ%2BQMq2GgkmUwGGyXa5jqHVpAky38T1wfaVkQCrLaLJ65n17DJxhpwSiT7CljGdGYfwvrk9JF5DgeJb%2F%2FY3kRKY&X-Amz-Signature=bd6ea1f034050f156f072e5ad67bab6897441e79f4733bafaeedea81f1a02f76&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OTFW5I5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD0zqG29msali3Ad5U7SNfvylhJs2rmx9JZwXvhKwU24gIgY1KZ%2BTBFk3aVVqTcNfdkHihxlzjMOSn77EAoazoyu9IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3rfLqHrHKoeCUNfCrcA4wNs5ULmyKHZwMpepsqJjEGTIQmxnoJnhhLN%2BHrOxDcdpLHonwgbXl5TcCXfKdOZX%2B8THoF%2Bnz9AHBU1Y1kj59f8cU3nPrNEZizPmBNCCxpGY0NwwGp1pe%2B5OLIyTfmKNxogtvxGkMuMbwbtImUT2cWtZbb%2BI9O2KnEbDpWHhyjMcvUjOSdMvcCUYIAtW7EnUaGqLBxKCxx609qz%2BYnYEbWpWcfDQQQpRoChEXJ%2FgfUie8yToEHHCiXkO%2FMGQWVnYsga5%2B%2FtkOrREBTdtM1MpgE6Vi%2B693OitWjJqXPydDLkv%2BejafDGdM4%2FOe%2FsgOPnmefFO1yyO9q0J3q5GlFyrqlDaXQIyStNDchZiEzrMYXd8AkjC506B%2FbaHKz0zT%2FnJw1FOATZmFrzi%2BvDTXedH7ebhRBdmAy7YlrVFk09Wd68dG14spSd3krqwPPW1zMRPw0w0sWpwXeE6tZU62j4cpGayXkG0i7FAdbjcroepySIzaIHfDGyU%2B5AuCftOOrmCJeIqa5rXhS041Z1DhwBmMPhABptPeyb5OORNAT1vH5b4rYA%2FvGDMptFT9bhpfrJJNyI1KAjziWqqyfDr2yKhkZ%2B%2BApKcyAGjLxN%2BY8hZJf5t4mEvNT2Lau75DQMNuOnL0GOqUBiBsTPHkgTe7aN84A7dEy49cvwdzUnmrcFb9rN3umuaB53l%2FdWIijxC9cKRLtT%2B%2FdbQTVDYNUJBGjsHkETANCmoj8wrGQWdSlZxySHE2awWMRZcAMTXnWC%2BZki0iL07jFD7M%2FvIujztg%2FcIELeFv1bZnzFeGZA4EiSGL6eLYMPHm5tT19Mh2AxnaMf%2FW2JnMGcKCmfhM4%2FKexpBi7K8RrZOoJ69e%2B&X-Amz-Signature=ab708995c199dc156f04fc113263a4fe9ef664500484ec767522aca332d10ce9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OTFW5I5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD0zqG29msali3Ad5U7SNfvylhJs2rmx9JZwXvhKwU24gIgY1KZ%2BTBFk3aVVqTcNfdkHihxlzjMOSn77EAoazoyu9IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3rfLqHrHKoeCUNfCrcA4wNs5ULmyKHZwMpepsqJjEGTIQmxnoJnhhLN%2BHrOxDcdpLHonwgbXl5TcCXfKdOZX%2B8THoF%2Bnz9AHBU1Y1kj59f8cU3nPrNEZizPmBNCCxpGY0NwwGp1pe%2B5OLIyTfmKNxogtvxGkMuMbwbtImUT2cWtZbb%2BI9O2KnEbDpWHhyjMcvUjOSdMvcCUYIAtW7EnUaGqLBxKCxx609qz%2BYnYEbWpWcfDQQQpRoChEXJ%2FgfUie8yToEHHCiXkO%2FMGQWVnYsga5%2B%2FtkOrREBTdtM1MpgE6Vi%2B693OitWjJqXPydDLkv%2BejafDGdM4%2FOe%2FsgOPnmefFO1yyO9q0J3q5GlFyrqlDaXQIyStNDchZiEzrMYXd8AkjC506B%2FbaHKz0zT%2FnJw1FOATZmFrzi%2BvDTXedH7ebhRBdmAy7YlrVFk09Wd68dG14spSd3krqwPPW1zMRPw0w0sWpwXeE6tZU62j4cpGayXkG0i7FAdbjcroepySIzaIHfDGyU%2B5AuCftOOrmCJeIqa5rXhS041Z1DhwBmMPhABptPeyb5OORNAT1vH5b4rYA%2FvGDMptFT9bhpfrJJNyI1KAjziWqqyfDr2yKhkZ%2B%2BApKcyAGjLxN%2BY8hZJf5t4mEvNT2Lau75DQMNuOnL0GOqUBiBsTPHkgTe7aN84A7dEy49cvwdzUnmrcFb9rN3umuaB53l%2FdWIijxC9cKRLtT%2B%2FdbQTVDYNUJBGjsHkETANCmoj8wrGQWdSlZxySHE2awWMRZcAMTXnWC%2BZki0iL07jFD7M%2FvIujztg%2FcIELeFv1bZnzFeGZA4EiSGL6eLYMPHm5tT19Mh2AxnaMf%2FW2JnMGcKCmfhM4%2FKexpBi7K8RrZOoJ69e%2B&X-Amz-Signature=8014171554e8b45f6ffc91d77355091c5ffb8778470b57c3528813e315a1b6d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OTFW5I5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD0zqG29msali3Ad5U7SNfvylhJs2rmx9JZwXvhKwU24gIgY1KZ%2BTBFk3aVVqTcNfdkHihxlzjMOSn77EAoazoyu9IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF3rfLqHrHKoeCUNfCrcA4wNs5ULmyKHZwMpepsqJjEGTIQmxnoJnhhLN%2BHrOxDcdpLHonwgbXl5TcCXfKdOZX%2B8THoF%2Bnz9AHBU1Y1kj59f8cU3nPrNEZizPmBNCCxpGY0NwwGp1pe%2B5OLIyTfmKNxogtvxGkMuMbwbtImUT2cWtZbb%2BI9O2KnEbDpWHhyjMcvUjOSdMvcCUYIAtW7EnUaGqLBxKCxx609qz%2BYnYEbWpWcfDQQQpRoChEXJ%2FgfUie8yToEHHCiXkO%2FMGQWVnYsga5%2B%2FtkOrREBTdtM1MpgE6Vi%2B693OitWjJqXPydDLkv%2BejafDGdM4%2FOe%2FsgOPnmefFO1yyO9q0J3q5GlFyrqlDaXQIyStNDchZiEzrMYXd8AkjC506B%2FbaHKz0zT%2FnJw1FOATZmFrzi%2BvDTXedH7ebhRBdmAy7YlrVFk09Wd68dG14spSd3krqwPPW1zMRPw0w0sWpwXeE6tZU62j4cpGayXkG0i7FAdbjcroepySIzaIHfDGyU%2B5AuCftOOrmCJeIqa5rXhS041Z1DhwBmMPhABptPeyb5OORNAT1vH5b4rYA%2FvGDMptFT9bhpfrJJNyI1KAjziWqqyfDr2yKhkZ%2B%2BApKcyAGjLxN%2BY8hZJf5t4mEvNT2Lau75DQMNuOnL0GOqUBiBsTPHkgTe7aN84A7dEy49cvwdzUnmrcFb9rN3umuaB53l%2FdWIijxC9cKRLtT%2B%2FdbQTVDYNUJBGjsHkETANCmoj8wrGQWdSlZxySHE2awWMRZcAMTXnWC%2BZki0iL07jFD7M%2FvIujztg%2FcIELeFv1bZnzFeGZA4EiSGL6eLYMPHm5tT19Mh2AxnaMf%2FW2JnMGcKCmfhM4%2FKexpBi7K8RrZOoJ69e%2B&X-Amz-Signature=f0b01a9f8530650e1beade97281a1cb6738782fabcf9ae61605e61de9d42fec6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663P74A4P2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDrdOYZhKu0QqAO1KAsBqG8aesodAujnNZt9eUBnfCWDgIgLq84p2Kno8fTDPNkqPNORzNCTssBVDt5HF%2FvBWpZ9p0qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM8WcGl8GnaLeX2yYyrcA68rb%2B8l2W8VC0KIGF4Ydwwdr6xfCsf3Z2BWPMaY9A0pHmJ23t%2FsTsYFqI1TxksFdMCOkIBfkp8lkW0m6uS28IGDVKF6AWiL2jbBxcqbPVE0SwpoCljlJU8XXcdf7k4PAXeOSjWyBIK6FXM5I%2FZr8KhXcdXA42B2e72nBrnsx3GcOpuJicK%2BbVu0rYkN7MOBzIJX6yEF9JNLyLcXPo0WTKywJ60D5OD8JdxmlGqmyb1RILI2q6mLv7eRD%2F%2FbaIr1sdjP5F1GpPOTfWCscBOCYqmAWPhDBFZd5UjIH3n33HKTLtElMo0io9B9DsU%2FawXWbhrRrcT6JAOtY8PmyzXJI9MD6AM2IX0IaIQHOnzssBdxl%2BGHnFO6GTH7uyToLxK3ipK%2FkU61B3wFq3hJ3%2Fl0ZVhST3akiZvFswZ1pRou9VAfBwFrPL8R9R%2BR%2BNnGZddY5qSpDXl7Q0GVKkUxmVHNQKgGpmV9YGgcwHBK4E%2F59Y2QQEOoKgxN1XPXvWb9U91VRiUQsLq5kWTOjohMT3TEkeWQaqbwYyjHDc39P1QcP5WM48ewr2slJvdywRggDrmWA7t%2BwM5iuRyZK7DRZo7wDTA0zUHod5qGO%2FVL24Uzx3QpB0h6Pqo%2FYm25%2FsXqMKeOnL0GOqUBBKDhKouYcjri0HYZpo9LJzvP4bjxHdR0l8MK1wEvvVt3YnCOhXsmWVa62pNOLRQg4fgXcb0TttkNoZEuSEEpB0BYM1yzrwOTlmAwqk1Ee%2FhOl5pM8wI6Wg13oGwANSIEjKO6kT4kzSXw9SZGje9O1T9Z2RIZC1H6o%2BgiI0OAvGeXxqG%2BAk3rtqastsoWFXwMTQXIP4sGO9zYBPi9AT18B4FH3hE%2F&X-Amz-Signature=4d418053e91e72dafba1031a0710e459ec5f8fbe46db32f0d07e09d36894259e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DUKS4LD%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD4RRLtRn854jgFy%2FxO8bGZeL5QscqoX6XhpXIAFfb%2F5AIgUkImkAUT6NJXEhmSdBzK2M5SuNt4eqP3y8S8mVCn4ocqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6asG6gn8lwdcz2tircA6M0FtiEx9nb3UVkZc0gGNud0IY0K1ruR8Xasm8n6zQM5kGuTOavjIwBShLBMboCBwpU0cXe85tXLMRfseVb2jZrxv32fWx4UBx7l6pgYeSXhRlFHoKKwWNIgCoUVRYjdBasqem3W1VXMhkfjXLK%2BdNKhxTTdOmisBiQ3Po7UR6Vthvl1HipZL7AoA3wueNpDtpYdC8AyxtyQqY%2FKQqO5s%2BaHDniXrdcPfUMZwJZkTNb4EYLPM2nPy9pS8heMBXg0T%2BtXaJUK%2BiiMuoL%2B3IYajDlHVMJ163kgL1J76v8MfasCk1MKC9aPJWxt9NNzsXvsWIKAWh48vXT5s1APO%2FTKFxGsOyQuqr%2Fr10vu03V0enDKYIny%2FyEJbIkMDUFpvn6ffmkbyD9RV2tOw4IEUbVJn2sgVi8%2BhBSQ%2FY%2F4dKV2Djg8U3GSnvmbKOMKSGguUyOkBMAcKHF%2F5HezyyKJ7Wie7WWU6vBnP4mgVh%2BlfrZN2PsztQgeONVsts1PvuwpBQLp03xAXNTGvZk9TYCGS7VXX3ePjWolmfIEFrx5vV9m0rDHnsHswUhD6w2gfLYVXKiHkdE%2Feehf%2BDiW8kSaK%2FzV6JdzRrTXtPtNZaypINpAZWc3MPNTLlE1drQUs9zMJqOnL0GOqUB44klVop4NohcUUApikVW5%2FLx6lcFPBYVcDxeNhYuAJN5pKplM%2FE2vA5CEgEt9I1TUspFQuZ7Aitu7G4n9Qi%2FjeFg8eOp59eCtUGCzE%2FymK4VwJJH4xiuPwMHd2pmclxJcNOwxqeAsOvxKvobylWAsJlDoYYJTAav%2B2vikfi4b%2B%2FaZ6JqT6AroVbAtq1pbtevTrv7CkJ6XuMTON%2FszGym%2FfDLNuo0&X-Amz-Signature=9ceb720c0a50f4bf2b14db64deb5ca8cdd3e1ea538e574785bcea0a8cb0ef7db&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625JJ2R4Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHVwtxDjGpkoaIAA5ZHOp9HY5Jfq4U3ZxlaLN%2BAb5pasAiBi51jTaapecc59cEAoMy1bDb8ao8v%2B%2BIN54B8mN%2BtlOSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwiu0ZqEjwhH1vugEKtwDDCow1uE%2Bw%2B1c2ZSDfeoJzsB%2BdyhOvDavNoEqoRfd%2FSTfZnNwR1vS7Bg5VfYGSgsWQQkQCGCA3fm22AoOCFz2uuBfJ%2Ff%2B%2BB5kwZdMpdkcP6Hx7gDJOyjco3nazM7MLbCmisaYD55lLFgI7schShfYfEfC4%2FitWE9WEAUmaS5SdGV2zl%2Fuh2u7YdsOMhlwwWWeXjv8yd9aRnXLoZnTswR%2BSmeiBUxGhTBquppow3gGCYjDpN2LJYNOK5c%2FyjCBY4fsTPt0dANsXL9aULnXAsPDHIUYcSZ7s72yzW6kUPWet4cE7zDMIKd8yA%2BY1bYstOvQQEyWXcGNV4P0OC6IZox3Fi4jM2hfyLL%2FTDZacz7t6pkk%2BR0nW%2FmK%2BF6veZZAJ3GKlg2Mwqexdw47ol5MHQm80Z%2FHDahL7wOa93riworWLMPwCL%2Bc8M7kOSoXopyz3Cz%2FsRkbivsSpvMLfb3ZLg8%2BefmJlbgHWXOfQPobCofz3BChAh7EDa9OwcD74LfNba1wfamPKXEYiAXPBAfuPPpEdUPnLu10ZR0K%2BtlyLFsOJjRiHQVYmvqr2Th1V9Glsx4rht%2FK1cQNjrcWAF0FS0jKgH%2FEHu0waZlqsup4ms0mRtVa9uxn1cNHgnPDXn4wpY6cvQY6pgHB9SZe%2Fw6SYwVcDfpUv7HAhC4N0gCCtf0%2BcQLSUhz%2B7aaXeeDnNfEhuywxgenehkE2mkeY28UjlmH9ykdEwWkgb8nDTcvu9k%2Flbm%2FAdwLQVuqCeaqEMsy4y1SP5KLkPqnRUu9ph4IVdq4c2ImADrgrQ1A0AEEl3YP%2Fx5uXQlWHtpDR1HknQiEcB%2F3225JU82VtBHz6z45QWFff7K0tIhyC83aEoUOR&X-Amz-Signature=e0f3a394e95d44f83d8c0dccb66ce6c8ca7c6de26ad9a0689c92c51c9efc0049&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C3NRNIB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIH5hDeUULgXxve62fLMRXkXfbGzQQlKv8In5XraMyiQyAiAOBp1KBGz5linrYNbv3Tt1in9uCuxsTCeoh2H5GB%2FXESqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcRfNQ%2BP%2BuGPAUbXAKtwDH4fWluQZ%2BOxiux%2BHIEokkEDZpLeRUVZvJN%2B4UeVNEPa0hRs6CSlmTCqSvt1CP1HbtAB0VSnylP60jWsiUvyXlN4n6ivthl91YxVn5mYw15CgO87BK%2F8gqqAcmVtYGmrll2PyZusxotWjldyYCFyqPV8hz8zTqYV4pVosicvXrlEGqOp4V6YgigJeIsk5h0UNL42ovE%2FRuSToonT8l2mBPoPvnmtWvnYyVBUJWRvd3glqRci6ZKcg5NivI%2BZRCZiW6TbwWZ2aIUASbkIJw6d1U9iYMpPoC%2FABpppKJTmY1IujGgCI7fD4MZ5CQAF5UsH427cCb0afGPgl9IV5B0Yw2HZvIkgoCEiO53HXvHg8If8p4xYjo%2BKbiYbdCQaolM82xS5DIdRuPjFPmBBB%2B2QAN75vmc7o%2BkMFaIrZ3Q%2FOFSsAFBj7NuvmEUqaC1qPnJEQ%2Ff9iwP8cKXLOAtfyFyeyNfmG%2BM15%2Fczg1GkwC4R6WbSb6RZd4EIVnXkev3vVqu%2Bi3GXoPYBaaPCIn68fw83BU9QACsNGlU5KOsAnAQJNs8%2Fp6T2OQecKo3xxTP1gntg%2F0JQje%2Bk%2F2dfXp8VaVdq7b1unTf0JyQj8pSgSR6Pp777JBpBbe15ybuj13eQwvo6cvQY6pgEoARU2FmuAYoxPWp43bN9N%2BBIjOPEiP0ju%2FOfPNm%2BtU8P810L77QxlRyg01ChOPQaY1CItx1CZd7s4phQBbKoC24z2wBiVVW947cxiWzS044G88GrDdDb5yS39uVpQcDVxjz%2BeNmo2IcSBB%2Bj0BE2C9soeM94o8oaDrdtSh8N61K14TlBMCaK%2FTdmyEmpulaCQKwC4juMtLDAwASu7Ji0HbJOMLIUa&X-Amz-Signature=542a94145bb0750125b7996ec6d5ee2360a9406291c11421f189b8f1a521fc32&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C3NRNIB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIH5hDeUULgXxve62fLMRXkXfbGzQQlKv8In5XraMyiQyAiAOBp1KBGz5linrYNbv3Tt1in9uCuxsTCeoh2H5GB%2FXESqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcRfNQ%2BP%2BuGPAUbXAKtwDH4fWluQZ%2BOxiux%2BHIEokkEDZpLeRUVZvJN%2B4UeVNEPa0hRs6CSlmTCqSvt1CP1HbtAB0VSnylP60jWsiUvyXlN4n6ivthl91YxVn5mYw15CgO87BK%2F8gqqAcmVtYGmrll2PyZusxotWjldyYCFyqPV8hz8zTqYV4pVosicvXrlEGqOp4V6YgigJeIsk5h0UNL42ovE%2FRuSToonT8l2mBPoPvnmtWvnYyVBUJWRvd3glqRci6ZKcg5NivI%2BZRCZiW6TbwWZ2aIUASbkIJw6d1U9iYMpPoC%2FABpppKJTmY1IujGgCI7fD4MZ5CQAF5UsH427cCb0afGPgl9IV5B0Yw2HZvIkgoCEiO53HXvHg8If8p4xYjo%2BKbiYbdCQaolM82xS5DIdRuPjFPmBBB%2B2QAN75vmc7o%2BkMFaIrZ3Q%2FOFSsAFBj7NuvmEUqaC1qPnJEQ%2Ff9iwP8cKXLOAtfyFyeyNfmG%2BM15%2Fczg1GkwC4R6WbSb6RZd4EIVnXkev3vVqu%2Bi3GXoPYBaaPCIn68fw83BU9QACsNGlU5KOsAnAQJNs8%2Fp6T2OQecKo3xxTP1gntg%2F0JQje%2Bk%2F2dfXp8VaVdq7b1unTf0JyQj8pSgSR6Pp777JBpBbe15ybuj13eQwvo6cvQY6pgEoARU2FmuAYoxPWp43bN9N%2BBIjOPEiP0ju%2FOfPNm%2BtU8P810L77QxlRyg01ChOPQaY1CItx1CZd7s4phQBbKoC24z2wBiVVW947cxiWzS044G88GrDdDb5yS39uVpQcDVxjz%2BeNmo2IcSBB%2Bj0BE2C9soeM94o8oaDrdtSh8N61K14TlBMCaK%2FTdmyEmpulaCQKwC4juMtLDAwASu7Ji0HbJOMLIUa&X-Amz-Signature=c236c7ccc1b19ce0aa51a03dc62a8f4a04c62e7c15f647b6df19bbbbe2b2ad03&X-Amz-SignedHeaders=host&x-id=GetObject)

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
