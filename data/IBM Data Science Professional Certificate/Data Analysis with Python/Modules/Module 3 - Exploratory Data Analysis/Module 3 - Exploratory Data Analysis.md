

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z24LFJC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCICAYbfBYlFV58d7sHbEXYsDYh03fuEqQKTgVUk5W41YKAiBj1c0znBMG0IRIt%2BG%2FwqYpslS4AH%2BYwX9MJ6WrY%2FDIgyr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIM2QNPDxzYFNR47u8XKtwDXKc%2FDQEqyqA67blidn3WajzDnrnDekLb9FqZjDeRBurPH6GbWhfaw6sDGcAMEE6seoJL6YkY%2FH9vjRWjw6hZCg8%2BNvdRYsTCX3okXu63P%2Fdi3l8x0w2J6734r%2F8vkMLvi%2B%2B6c9UTan9sdkVHg5QnIqis76tRI7Sy5P1aInw6Xh7nUUoOC4nR27Vvxl2f21AAR1HZJaYKKs1tyiE5NL1%2BJcxtHo481T7gMgWXiXyMJXiWC30Nqpe5iz9Yf3zNI0EDgxIa3ERIaz8Mws5oPyamxuzRm%2FwtLcxm31VBdkM26NrDXmw%2F2EC5VCnJ4MJCzsWQQnmM9oGpCCumz7JTLVwZLBj0Rwlmjq7sh%2By3lbsoeUoa%2FH2D0qn01k2Fkpaxr3SkzpPea2lpmP5ITW2P%2FWDGgG6mCVsCoUgn8kGgbS49m6KMy7pImADoqcKBC4wLVwJZnSIMklTfIiEhwjh2DxTQfgj5hxaES8LmqUxhKEVW4C%2BBudCIbk5dPg0AlwwGsrWwIAuIyIijk1YRA6fguKcedzAGJuXJwfOO3%2BVbogjF4RxsPg7kkNbmy4HaIoRRMNETDePtUUzAhH1U6K8LQmk7o4czZ4hj8MDeUTmA8Nf94o6prDXJPuZe9LKWsUww5uqFvQY6pgHG4UXWy%2F94zklbjV%2Be%2FUncgiOQtKFhH62CTNoOy6fI0bsHG7PmL2sMRwX%2BExQJI6%2F%2FCZv4vvo32B6oVsoAT69I8hH6AwsGtvq5phJ6jWl2obE%2BeEfoKqekGeZ3BjBe1oD2DgmoNUSTK7VTXH5GWzDDsQO4P4K7WZOYBdFPd2r9ITIAmwGveHVSJeNqMlU1g2Nqc2zq3ybztH1in27Gb5fhJhKPSx%2BQ&X-Amz-Signature=6815e81ee94a1a580e474a82c39d37079823d5ab0a0cb872bab71e7fe9c170f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z24LFJC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCICAYbfBYlFV58d7sHbEXYsDYh03fuEqQKTgVUk5W41YKAiBj1c0znBMG0IRIt%2BG%2FwqYpslS4AH%2BYwX9MJ6WrY%2FDIgyr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIM2QNPDxzYFNR47u8XKtwDXKc%2FDQEqyqA67blidn3WajzDnrnDekLb9FqZjDeRBurPH6GbWhfaw6sDGcAMEE6seoJL6YkY%2FH9vjRWjw6hZCg8%2BNvdRYsTCX3okXu63P%2Fdi3l8x0w2J6734r%2F8vkMLvi%2B%2B6c9UTan9sdkVHg5QnIqis76tRI7Sy5P1aInw6Xh7nUUoOC4nR27Vvxl2f21AAR1HZJaYKKs1tyiE5NL1%2BJcxtHo481T7gMgWXiXyMJXiWC30Nqpe5iz9Yf3zNI0EDgxIa3ERIaz8Mws5oPyamxuzRm%2FwtLcxm31VBdkM26NrDXmw%2F2EC5VCnJ4MJCzsWQQnmM9oGpCCumz7JTLVwZLBj0Rwlmjq7sh%2By3lbsoeUoa%2FH2D0qn01k2Fkpaxr3SkzpPea2lpmP5ITW2P%2FWDGgG6mCVsCoUgn8kGgbS49m6KMy7pImADoqcKBC4wLVwJZnSIMklTfIiEhwjh2DxTQfgj5hxaES8LmqUxhKEVW4C%2BBudCIbk5dPg0AlwwGsrWwIAuIyIijk1YRA6fguKcedzAGJuXJwfOO3%2BVbogjF4RxsPg7kkNbmy4HaIoRRMNETDePtUUzAhH1U6K8LQmk7o4czZ4hj8MDeUTmA8Nf94o6prDXJPuZe9LKWsUww5uqFvQY6pgHG4UXWy%2F94zklbjV%2Be%2FUncgiOQtKFhH62CTNoOy6fI0bsHG7PmL2sMRwX%2BExQJI6%2F%2FCZv4vvo32B6oVsoAT69I8hH6AwsGtvq5phJ6jWl2obE%2BeEfoKqekGeZ3BjBe1oD2DgmoNUSTK7VTXH5GWzDDsQO4P4K7WZOYBdFPd2r9ITIAmwGveHVSJeNqMlU1g2Nqc2zq3ybztH1in27Gb5fhJhKPSx%2BQ&X-Amz-Signature=e3bfbf558acaee7818b383b985a5ded037df30f6e5b592abac7679e5e8a41e69&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z24LFJC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCICAYbfBYlFV58d7sHbEXYsDYh03fuEqQKTgVUk5W41YKAiBj1c0znBMG0IRIt%2BG%2FwqYpslS4AH%2BYwX9MJ6WrY%2FDIgyr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIM2QNPDxzYFNR47u8XKtwDXKc%2FDQEqyqA67blidn3WajzDnrnDekLb9FqZjDeRBurPH6GbWhfaw6sDGcAMEE6seoJL6YkY%2FH9vjRWjw6hZCg8%2BNvdRYsTCX3okXu63P%2Fdi3l8x0w2J6734r%2F8vkMLvi%2B%2B6c9UTan9sdkVHg5QnIqis76tRI7Sy5P1aInw6Xh7nUUoOC4nR27Vvxl2f21AAR1HZJaYKKs1tyiE5NL1%2BJcxtHo481T7gMgWXiXyMJXiWC30Nqpe5iz9Yf3zNI0EDgxIa3ERIaz8Mws5oPyamxuzRm%2FwtLcxm31VBdkM26NrDXmw%2F2EC5VCnJ4MJCzsWQQnmM9oGpCCumz7JTLVwZLBj0Rwlmjq7sh%2By3lbsoeUoa%2FH2D0qn01k2Fkpaxr3SkzpPea2lpmP5ITW2P%2FWDGgG6mCVsCoUgn8kGgbS49m6KMy7pImADoqcKBC4wLVwJZnSIMklTfIiEhwjh2DxTQfgj5hxaES8LmqUxhKEVW4C%2BBudCIbk5dPg0AlwwGsrWwIAuIyIijk1YRA6fguKcedzAGJuXJwfOO3%2BVbogjF4RxsPg7kkNbmy4HaIoRRMNETDePtUUzAhH1U6K8LQmk7o4czZ4hj8MDeUTmA8Nf94o6prDXJPuZe9LKWsUww5uqFvQY6pgHG4UXWy%2F94zklbjV%2Be%2FUncgiOQtKFhH62CTNoOy6fI0bsHG7PmL2sMRwX%2BExQJI6%2F%2FCZv4vvo32B6oVsoAT69I8hH6AwsGtvq5phJ6jWl2obE%2BeEfoKqekGeZ3BjBe1oD2DgmoNUSTK7VTXH5GWzDDsQO4P4K7WZOYBdFPd2r9ITIAmwGveHVSJeNqMlU1g2Nqc2zq3ybztH1in27Gb5fhJhKPSx%2BQ&X-Amz-Signature=7188e74bdc27409f3520f0277603b8ec4909a5ae2ec9f6a687abf949d8d433ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AE54YWI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQC5HLJEaHqOX6ptBB9Pw3wY2FX3HW6qJfE4SPjkOVNcWwIhAOi5qtKfdAXofdRSXG0uzpyoARIwcgADKtjBTFpGt61dKv8DCCMQABoMNjM3NDIzMTgzODA1IgySQ6rnTwRCvcoABJ8q3AOuS4YCxKY3Wb4tU7ejKbER%2FSmSWv4OsVAvgENh36HZcx2Uw%2FGVH%2BWUVFbzG7LjwVh3w%2FHEtTF8Bw7gkIjtsd6FwlgTexa66sGNlZ3Lz54OvjMcR1et8fR%2BlKOYfPazmXBwr2BCt2PAx15idM%2F36AKL4r1Fzv3UW9x7%2FSMU2Q%2Bs2yTi9DcByHednhMuVaA%2BR5nkqChgqs%2BHTN3JGMDZO7zbBhqIX%2BgzAL1hlrK649Qh114Oqfed3ENsgthcdhsa4kSXfwVRNrScpA3HRpRxOJkQoV1Nc4HEiGtZvTvX1ts%2BfA66RxH2t7KbIiO9ByDuIo%2FDpWmzrQzIL6gPY3NVbCPS6XHVmv%2FeOmJC9mKxvxO2QX0pV5fzzYFhAHIfoee0uL1%2FcrwT8mGF8ZP1uXZp2Dlou62WCqekpRtII6NgknrlnfHj9uIjWTr%2BLAVsNEPhWBvrqFxQTYdFeOyJHQDUpqAXvpyoxpi8ktSTVotl6eaG4SjoHU6fq5vSsWDXjiJouSoBufQsAk4QmHL2uaMVtSgvGJTdCl5GtDVu9aCbtWwcsV77nwFisUHjJkX9tVEdel4s8Xx%2BepEbZ%2B%2FcPLEvL7hk63SY2n%2FXCo%2FrWI7hjncFaTYbGjBR%2FHvq9r7%2B7jDc6YW9BjqkAYs3GPmJjNz8qPzSf1UrRovJ7bPOlsP8%2Fjet5XBDp7Lu5nzd0%2FU3MF6%2BW6Jb2RNlfjeEYITaj4nJmPwz3jjTz3uFbsIPZ5z%2BaH3pFiGl3vLzcEdMED7y3mzRqD7%2FuUVly%2FIc3uAqG%2BNv0HeVe%2BQo87RU3w8Z8H7V3nSGQ87fpw3j%2FchvPccDPy1bcyIKtvqIr7EZxOseievDVgujj1VdfC4x%2FDUA&X-Amz-Signature=a0b2181d8c1673f70d10ad429b3e34689e11420af0330b16735b92ee512f82a8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AE54YWI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQC5HLJEaHqOX6ptBB9Pw3wY2FX3HW6qJfE4SPjkOVNcWwIhAOi5qtKfdAXofdRSXG0uzpyoARIwcgADKtjBTFpGt61dKv8DCCMQABoMNjM3NDIzMTgzODA1IgySQ6rnTwRCvcoABJ8q3AOuS4YCxKY3Wb4tU7ejKbER%2FSmSWv4OsVAvgENh36HZcx2Uw%2FGVH%2BWUVFbzG7LjwVh3w%2FHEtTF8Bw7gkIjtsd6FwlgTexa66sGNlZ3Lz54OvjMcR1et8fR%2BlKOYfPazmXBwr2BCt2PAx15idM%2F36AKL4r1Fzv3UW9x7%2FSMU2Q%2Bs2yTi9DcByHednhMuVaA%2BR5nkqChgqs%2BHTN3JGMDZO7zbBhqIX%2BgzAL1hlrK649Qh114Oqfed3ENsgthcdhsa4kSXfwVRNrScpA3HRpRxOJkQoV1Nc4HEiGtZvTvX1ts%2BfA66RxH2t7KbIiO9ByDuIo%2FDpWmzrQzIL6gPY3NVbCPS6XHVmv%2FeOmJC9mKxvxO2QX0pV5fzzYFhAHIfoee0uL1%2FcrwT8mGF8ZP1uXZp2Dlou62WCqekpRtII6NgknrlnfHj9uIjWTr%2BLAVsNEPhWBvrqFxQTYdFeOyJHQDUpqAXvpyoxpi8ktSTVotl6eaG4SjoHU6fq5vSsWDXjiJouSoBufQsAk4QmHL2uaMVtSgvGJTdCl5GtDVu9aCbtWwcsV77nwFisUHjJkX9tVEdel4s8Xx%2BepEbZ%2B%2FcPLEvL7hk63SY2n%2FXCo%2FrWI7hjncFaTYbGjBR%2FHvq9r7%2B7jDc6YW9BjqkAYs3GPmJjNz8qPzSf1UrRovJ7bPOlsP8%2Fjet5XBDp7Lu5nzd0%2FU3MF6%2BW6Jb2RNlfjeEYITaj4nJmPwz3jjTz3uFbsIPZ5z%2BaH3pFiGl3vLzcEdMED7y3mzRqD7%2FuUVly%2FIc3uAqG%2BNv0HeVe%2BQo87RU3w8Z8H7V3nSGQ87fpw3j%2FchvPccDPy1bcyIKtvqIr7EZxOseievDVgujj1VdfC4x%2FDUA&X-Amz-Signature=46c1b8b4be7024596e16caf3108de955a08e26a8f8b61a786f812866b8c61203&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AE54YWI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQC5HLJEaHqOX6ptBB9Pw3wY2FX3HW6qJfE4SPjkOVNcWwIhAOi5qtKfdAXofdRSXG0uzpyoARIwcgADKtjBTFpGt61dKv8DCCMQABoMNjM3NDIzMTgzODA1IgySQ6rnTwRCvcoABJ8q3AOuS4YCxKY3Wb4tU7ejKbER%2FSmSWv4OsVAvgENh36HZcx2Uw%2FGVH%2BWUVFbzG7LjwVh3w%2FHEtTF8Bw7gkIjtsd6FwlgTexa66sGNlZ3Lz54OvjMcR1et8fR%2BlKOYfPazmXBwr2BCt2PAx15idM%2F36AKL4r1Fzv3UW9x7%2FSMU2Q%2Bs2yTi9DcByHednhMuVaA%2BR5nkqChgqs%2BHTN3JGMDZO7zbBhqIX%2BgzAL1hlrK649Qh114Oqfed3ENsgthcdhsa4kSXfwVRNrScpA3HRpRxOJkQoV1Nc4HEiGtZvTvX1ts%2BfA66RxH2t7KbIiO9ByDuIo%2FDpWmzrQzIL6gPY3NVbCPS6XHVmv%2FeOmJC9mKxvxO2QX0pV5fzzYFhAHIfoee0uL1%2FcrwT8mGF8ZP1uXZp2Dlou62WCqekpRtII6NgknrlnfHj9uIjWTr%2BLAVsNEPhWBvrqFxQTYdFeOyJHQDUpqAXvpyoxpi8ktSTVotl6eaG4SjoHU6fq5vSsWDXjiJouSoBufQsAk4QmHL2uaMVtSgvGJTdCl5GtDVu9aCbtWwcsV77nwFisUHjJkX9tVEdel4s8Xx%2BepEbZ%2B%2FcPLEvL7hk63SY2n%2FXCo%2FrWI7hjncFaTYbGjBR%2FHvq9r7%2B7jDc6YW9BjqkAYs3GPmJjNz8qPzSf1UrRovJ7bPOlsP8%2Fjet5XBDp7Lu5nzd0%2FU3MF6%2BW6Jb2RNlfjeEYITaj4nJmPwz3jjTz3uFbsIPZ5z%2BaH3pFiGl3vLzcEdMED7y3mzRqD7%2FuUVly%2FIc3uAqG%2BNv0HeVe%2BQo87RU3w8Z8H7V3nSGQ87fpw3j%2FchvPccDPy1bcyIKtvqIr7EZxOseievDVgujj1VdfC4x%2FDUA&X-Amz-Signature=0b5330bd77ba876681b037b0232856d5e07efdf7f677963c24366a30e3f94b80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AE54YWI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQC5HLJEaHqOX6ptBB9Pw3wY2FX3HW6qJfE4SPjkOVNcWwIhAOi5qtKfdAXofdRSXG0uzpyoARIwcgADKtjBTFpGt61dKv8DCCMQABoMNjM3NDIzMTgzODA1IgySQ6rnTwRCvcoABJ8q3AOuS4YCxKY3Wb4tU7ejKbER%2FSmSWv4OsVAvgENh36HZcx2Uw%2FGVH%2BWUVFbzG7LjwVh3w%2FHEtTF8Bw7gkIjtsd6FwlgTexa66sGNlZ3Lz54OvjMcR1et8fR%2BlKOYfPazmXBwr2BCt2PAx15idM%2F36AKL4r1Fzv3UW9x7%2FSMU2Q%2Bs2yTi9DcByHednhMuVaA%2BR5nkqChgqs%2BHTN3JGMDZO7zbBhqIX%2BgzAL1hlrK649Qh114Oqfed3ENsgthcdhsa4kSXfwVRNrScpA3HRpRxOJkQoV1Nc4HEiGtZvTvX1ts%2BfA66RxH2t7KbIiO9ByDuIo%2FDpWmzrQzIL6gPY3NVbCPS6XHVmv%2FeOmJC9mKxvxO2QX0pV5fzzYFhAHIfoee0uL1%2FcrwT8mGF8ZP1uXZp2Dlou62WCqekpRtII6NgknrlnfHj9uIjWTr%2BLAVsNEPhWBvrqFxQTYdFeOyJHQDUpqAXvpyoxpi8ktSTVotl6eaG4SjoHU6fq5vSsWDXjiJouSoBufQsAk4QmHL2uaMVtSgvGJTdCl5GtDVu9aCbtWwcsV77nwFisUHjJkX9tVEdel4s8Xx%2BepEbZ%2B%2FcPLEvL7hk63SY2n%2FXCo%2FrWI7hjncFaTYbGjBR%2FHvq9r7%2B7jDc6YW9BjqkAYs3GPmJjNz8qPzSf1UrRovJ7bPOlsP8%2Fjet5XBDp7Lu5nzd0%2FU3MF6%2BW6Jb2RNlfjeEYITaj4nJmPwz3jjTz3uFbsIPZ5z%2BaH3pFiGl3vLzcEdMED7y3mzRqD7%2FuUVly%2FIc3uAqG%2BNv0HeVe%2BQo87RU3w8Z8H7V3nSGQ87fpw3j%2FchvPccDPy1bcyIKtvqIr7EZxOseievDVgujj1VdfC4x%2FDUA&X-Amz-Signature=f48623c172975fec49a0150a2716aa5b3db7aed98fc1362fddaecd9e12fd1b89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AE54YWI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQC5HLJEaHqOX6ptBB9Pw3wY2FX3HW6qJfE4SPjkOVNcWwIhAOi5qtKfdAXofdRSXG0uzpyoARIwcgADKtjBTFpGt61dKv8DCCMQABoMNjM3NDIzMTgzODA1IgySQ6rnTwRCvcoABJ8q3AOuS4YCxKY3Wb4tU7ejKbER%2FSmSWv4OsVAvgENh36HZcx2Uw%2FGVH%2BWUVFbzG7LjwVh3w%2FHEtTF8Bw7gkIjtsd6FwlgTexa66sGNlZ3Lz54OvjMcR1et8fR%2BlKOYfPazmXBwr2BCt2PAx15idM%2F36AKL4r1Fzv3UW9x7%2FSMU2Q%2Bs2yTi9DcByHednhMuVaA%2BR5nkqChgqs%2BHTN3JGMDZO7zbBhqIX%2BgzAL1hlrK649Qh114Oqfed3ENsgthcdhsa4kSXfwVRNrScpA3HRpRxOJkQoV1Nc4HEiGtZvTvX1ts%2BfA66RxH2t7KbIiO9ByDuIo%2FDpWmzrQzIL6gPY3NVbCPS6XHVmv%2FeOmJC9mKxvxO2QX0pV5fzzYFhAHIfoee0uL1%2FcrwT8mGF8ZP1uXZp2Dlou62WCqekpRtII6NgknrlnfHj9uIjWTr%2BLAVsNEPhWBvrqFxQTYdFeOyJHQDUpqAXvpyoxpi8ktSTVotl6eaG4SjoHU6fq5vSsWDXjiJouSoBufQsAk4QmHL2uaMVtSgvGJTdCl5GtDVu9aCbtWwcsV77nwFisUHjJkX9tVEdel4s8Xx%2BepEbZ%2B%2FcPLEvL7hk63SY2n%2FXCo%2FrWI7hjncFaTYbGjBR%2FHvq9r7%2B7jDc6YW9BjqkAYs3GPmJjNz8qPzSf1UrRovJ7bPOlsP8%2Fjet5XBDp7Lu5nzd0%2FU3MF6%2BW6Jb2RNlfjeEYITaj4nJmPwz3jjTz3uFbsIPZ5z%2BaH3pFiGl3vLzcEdMED7y3mzRqD7%2FuUVly%2FIc3uAqG%2BNv0HeVe%2BQo87RU3w8Z8H7V3nSGQ87fpw3j%2FchvPccDPy1bcyIKtvqIr7EZxOseievDVgujj1VdfC4x%2FDUA&X-Amz-Signature=efee55c542361dedfa94f29c7c8bde95f00d2d001130854ffd188496ec69214d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AE54YWI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQC5HLJEaHqOX6ptBB9Pw3wY2FX3HW6qJfE4SPjkOVNcWwIhAOi5qtKfdAXofdRSXG0uzpyoARIwcgADKtjBTFpGt61dKv8DCCMQABoMNjM3NDIzMTgzODA1IgySQ6rnTwRCvcoABJ8q3AOuS4YCxKY3Wb4tU7ejKbER%2FSmSWv4OsVAvgENh36HZcx2Uw%2FGVH%2BWUVFbzG7LjwVh3w%2FHEtTF8Bw7gkIjtsd6FwlgTexa66sGNlZ3Lz54OvjMcR1et8fR%2BlKOYfPazmXBwr2BCt2PAx15idM%2F36AKL4r1Fzv3UW9x7%2FSMU2Q%2Bs2yTi9DcByHednhMuVaA%2BR5nkqChgqs%2BHTN3JGMDZO7zbBhqIX%2BgzAL1hlrK649Qh114Oqfed3ENsgthcdhsa4kSXfwVRNrScpA3HRpRxOJkQoV1Nc4HEiGtZvTvX1ts%2BfA66RxH2t7KbIiO9ByDuIo%2FDpWmzrQzIL6gPY3NVbCPS6XHVmv%2FeOmJC9mKxvxO2QX0pV5fzzYFhAHIfoee0uL1%2FcrwT8mGF8ZP1uXZp2Dlou62WCqekpRtII6NgknrlnfHj9uIjWTr%2BLAVsNEPhWBvrqFxQTYdFeOyJHQDUpqAXvpyoxpi8ktSTVotl6eaG4SjoHU6fq5vSsWDXjiJouSoBufQsAk4QmHL2uaMVtSgvGJTdCl5GtDVu9aCbtWwcsV77nwFisUHjJkX9tVEdel4s8Xx%2BepEbZ%2B%2FcPLEvL7hk63SY2n%2FXCo%2FrWI7hjncFaTYbGjBR%2FHvq9r7%2B7jDc6YW9BjqkAYs3GPmJjNz8qPzSf1UrRovJ7bPOlsP8%2Fjet5XBDp7Lu5nzd0%2FU3MF6%2BW6Jb2RNlfjeEYITaj4nJmPwz3jjTz3uFbsIPZ5z%2BaH3pFiGl3vLzcEdMED7y3mzRqD7%2FuUVly%2FIc3uAqG%2BNv0HeVe%2BQo87RU3w8Z8H7V3nSGQ87fpw3j%2FchvPccDPy1bcyIKtvqIr7EZxOseievDVgujj1VdfC4x%2FDUA&X-Amz-Signature=12cab227741a2798839f26e2cb53fbb79e2b1c92e5699ea9101e1fc51739f662&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSKLGIDI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQDeaaHuR%2F6qB3X4%2Fm9VgVvywRwocc%2Bb2devSOZo5B99cgIhAOQ95ykOmuCoTNMsmvZNA7MI%2BiNH6JEpONGln8BUgikDKv8DCCMQABoMNjM3NDIzMTgzODA1IgyJ4xpLAZVi47ji0bMq3ANbbXjfDThL4fskX8tuJ3Jfa1qf%2BRwpnUAPQdMPuvUZLIOmTHfRzBIKkdvjSQyq610mG2NKeBbvwzUMQgkw6%2BUjopelCay2cnm2wFcrwKTyMtd9PPj7DWsVilQPnJ2DDQSYHKJR4iP%2BMXlvohWb1saoOXiSXHRGH2aM%2FjjqHVNWraBzAJWhXb6YzyhDkWEjg5wW52dHTL9CdnoQwi6of3Vlp9GZJI145p8fD%2F88S9VCVkNCag%2Bf9ycPQn1RoAfbu0SxAzmw8HlD3AjffjpiqrDXA%2Fz78Hv9byKFFlfjwCgdzPH2dSJesnH2CVqyaKOSCvDXfA23zDn5uUaEH8FsL1zBpR2QuJcwMZT6vwft5KPeD1jzHX8c2tLxOrKCXaCJ%2B%2B1OTFlgbvOag23fuvD20SHJwjFr13AltMqi2OgaTotkJ6yOXm2N3XdvgpF0CV6ibboKtUz46v76R3ZN4h%2BzyvcNpvypi23sA3kN9QdpVFXgPTbqMeXiaBAVM6Buzc5s8r7KBUrFsqw0%2B%2BN48sGAdMiA0pYbxYP71CdWeSgQY8qv49yvRSOIgGFKG%2BTcq1Aidg%2Bgf3VRsdjOComIRItAiyl4hwWMfhnxmfAPvArLApHKCAgFgP53Nxm0Ny%2BJ%2FDCp6YW9BjqkAWdfaVvbxWpDt2%2FUbEtdE%2BlZoofVagXNIil0qs5Lyiio8%2BrS%2BRbG8f%2BHbSZchaV1e15VTZjVcrXznWkgEIEUyCSpHYU0Pxxk%2B8h7v3DZ7ONpyTfnzP0ZBPsTbUZhzVt1AtRclL3uhMY7V4yAt72CXzw5fJpJijzShpl%2BzERTqJUaW0Oak%2Bz22T%2BqfI293OG7V0SauQKqkh4RuBKMPELHpi55xhkG&X-Amz-Signature=21ead10ab265ffd1587dd326862ce74603d3d6fcd3cb390e1024d64fa82c10ca&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZ27V6K3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCID%2BnPWXy%2FRVIaf2e%2B7COnJ2Vr2FQx8WqzqTm5AVzDFANAiEA9FxJ36sNxtRwQqKHTyMhkIula1JliVNxVCWXz0Z6DaAq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDLyqvFz8ALHudt571SrcAyPkzlQ5KkZqVrk8I1nUu54XaBwMENDylt6zvX%2BWMcVIEmetaLedlodJcKxzf5mB6%2FhUSjVjuxyFE%2BIBwzACkn4nC7HJDNut1dSlPgy7sEG9Ybtwchm26GesTh9gO2Sut11mL%2FuG4oUXKfoaZXS6pSl2QVfmgqiyXOVZE1i%2Bl8yqfHprviZhVyqqpl7nHxln%2BAZgYpnoh5XaszB9Xkl02pDnNVTiNMHkkDodtRydrL8ZCrC8gmXxNyFhEi6w9vxvCj5HWu5YBfiK%2FCZJ2U9ktyKUeoJ%2BYuirDUUuUekJfh%2BUSi%2F2LyWUUGRt%2FmmFsqFWl%2BjY9pJ%2FCRHBqmZ9clXwwMvBLhQ5y6O4cIKGlvNR%2BdpSgueH8S57WHVimUiSp%2B7XQefCmFGJCHK7431PC9P3cruxuGQ95wlXv8aSgmfEWCdoVqUfTLCP31hmoH1jOb46oSmq2xX4MelGJEy7Ez7ylUN2KPEPpc9nolBo%2Fx4zHsmUs2UcfFuLxNgdS5XYEjGx9CK6lAyAn2WTIVkd8EEeTWf6C8eREp6I6XQOyX5mMewbqiRoQBnOIqTl7Px5jMppyvdSHVdpDiHlY9Of4C8lInBgQLX1gAzm80Z3AxKCyfZSQRiHEQPyUr3v1DuHMJTphb0GOqUBvLU5ffYzWYDwo9M91t208Pji%2B2jQnWHR1pMD73A6c%2BJ%2FTh3aIBTBnAVwnxVkI%2B2x4GXgvfKVchunPdZ7SUphtzN5RHsp2sqnSnad4fQMC%2BZC9BnkJLQUB9VIIdCkFenXX17CwSNGMuexkw1QZFcsz7OGmpV26rYl6JUdT6wBZuTd8cfBDRB8wmNKGNcm%2FCTYuYGxsda2ElGBRIqTfl0WDgaiR9TS&X-Amz-Signature=a85f9b7cb79b90b808fb21b27a5a96f65a3667e8e95de02d0d442f8e2ad2e374&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AE54YWI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQC5HLJEaHqOX6ptBB9Pw3wY2FX3HW6qJfE4SPjkOVNcWwIhAOi5qtKfdAXofdRSXG0uzpyoARIwcgADKtjBTFpGt61dKv8DCCMQABoMNjM3NDIzMTgzODA1IgySQ6rnTwRCvcoABJ8q3AOuS4YCxKY3Wb4tU7ejKbER%2FSmSWv4OsVAvgENh36HZcx2Uw%2FGVH%2BWUVFbzG7LjwVh3w%2FHEtTF8Bw7gkIjtsd6FwlgTexa66sGNlZ3Lz54OvjMcR1et8fR%2BlKOYfPazmXBwr2BCt2PAx15idM%2F36AKL4r1Fzv3UW9x7%2FSMU2Q%2Bs2yTi9DcByHednhMuVaA%2BR5nkqChgqs%2BHTN3JGMDZO7zbBhqIX%2BgzAL1hlrK649Qh114Oqfed3ENsgthcdhsa4kSXfwVRNrScpA3HRpRxOJkQoV1Nc4HEiGtZvTvX1ts%2BfA66RxH2t7KbIiO9ByDuIo%2FDpWmzrQzIL6gPY3NVbCPS6XHVmv%2FeOmJC9mKxvxO2QX0pV5fzzYFhAHIfoee0uL1%2FcrwT8mGF8ZP1uXZp2Dlou62WCqekpRtII6NgknrlnfHj9uIjWTr%2BLAVsNEPhWBvrqFxQTYdFeOyJHQDUpqAXvpyoxpi8ktSTVotl6eaG4SjoHU6fq5vSsWDXjiJouSoBufQsAk4QmHL2uaMVtSgvGJTdCl5GtDVu9aCbtWwcsV77nwFisUHjJkX9tVEdel4s8Xx%2BepEbZ%2B%2FcPLEvL7hk63SY2n%2FXCo%2FrWI7hjncFaTYbGjBR%2FHvq9r7%2B7jDc6YW9BjqkAYs3GPmJjNz8qPzSf1UrRovJ7bPOlsP8%2Fjet5XBDp7Lu5nzd0%2FU3MF6%2BW6Jb2RNlfjeEYITaj4nJmPwz3jjTz3uFbsIPZ5z%2BaH3pFiGl3vLzcEdMED7y3mzRqD7%2FuUVly%2FIc3uAqG%2BNv0HeVe%2BQo87RU3w8Z8H7V3nSGQ87fpw3j%2FchvPccDPy1bcyIKtvqIr7EZxOseievDVgujj1VdfC4x%2FDUA&X-Amz-Signature=142b0c10f11414abb231e489f7212ca5473ccdb8146446e75da90c778cec61b9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AE54YWI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQC5HLJEaHqOX6ptBB9Pw3wY2FX3HW6qJfE4SPjkOVNcWwIhAOi5qtKfdAXofdRSXG0uzpyoARIwcgADKtjBTFpGt61dKv8DCCMQABoMNjM3NDIzMTgzODA1IgySQ6rnTwRCvcoABJ8q3AOuS4YCxKY3Wb4tU7ejKbER%2FSmSWv4OsVAvgENh36HZcx2Uw%2FGVH%2BWUVFbzG7LjwVh3w%2FHEtTF8Bw7gkIjtsd6FwlgTexa66sGNlZ3Lz54OvjMcR1et8fR%2BlKOYfPazmXBwr2BCt2PAx15idM%2F36AKL4r1Fzv3UW9x7%2FSMU2Q%2Bs2yTi9DcByHednhMuVaA%2BR5nkqChgqs%2BHTN3JGMDZO7zbBhqIX%2BgzAL1hlrK649Qh114Oqfed3ENsgthcdhsa4kSXfwVRNrScpA3HRpRxOJkQoV1Nc4HEiGtZvTvX1ts%2BfA66RxH2t7KbIiO9ByDuIo%2FDpWmzrQzIL6gPY3NVbCPS6XHVmv%2FeOmJC9mKxvxO2QX0pV5fzzYFhAHIfoee0uL1%2FcrwT8mGF8ZP1uXZp2Dlou62WCqekpRtII6NgknrlnfHj9uIjWTr%2BLAVsNEPhWBvrqFxQTYdFeOyJHQDUpqAXvpyoxpi8ktSTVotl6eaG4SjoHU6fq5vSsWDXjiJouSoBufQsAk4QmHL2uaMVtSgvGJTdCl5GtDVu9aCbtWwcsV77nwFisUHjJkX9tVEdel4s8Xx%2BepEbZ%2B%2FcPLEvL7hk63SY2n%2FXCo%2FrWI7hjncFaTYbGjBR%2FHvq9r7%2B7jDc6YW9BjqkAYs3GPmJjNz8qPzSf1UrRovJ7bPOlsP8%2Fjet5XBDp7Lu5nzd0%2FU3MF6%2BW6Jb2RNlfjeEYITaj4nJmPwz3jjTz3uFbsIPZ5z%2BaH3pFiGl3vLzcEdMED7y3mzRqD7%2FuUVly%2FIc3uAqG%2BNv0HeVe%2BQo87RU3w8Z8H7V3nSGQ87fpw3j%2FchvPccDPy1bcyIKtvqIr7EZxOseievDVgujj1VdfC4x%2FDUA&X-Amz-Signature=3d494a4b2cb43eed790f5edcc1d8561f951d35ac34e0c776c0ba3de947709620&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AE54YWI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQC5HLJEaHqOX6ptBB9Pw3wY2FX3HW6qJfE4SPjkOVNcWwIhAOi5qtKfdAXofdRSXG0uzpyoARIwcgADKtjBTFpGt61dKv8DCCMQABoMNjM3NDIzMTgzODA1IgySQ6rnTwRCvcoABJ8q3AOuS4YCxKY3Wb4tU7ejKbER%2FSmSWv4OsVAvgENh36HZcx2Uw%2FGVH%2BWUVFbzG7LjwVh3w%2FHEtTF8Bw7gkIjtsd6FwlgTexa66sGNlZ3Lz54OvjMcR1et8fR%2BlKOYfPazmXBwr2BCt2PAx15idM%2F36AKL4r1Fzv3UW9x7%2FSMU2Q%2Bs2yTi9DcByHednhMuVaA%2BR5nkqChgqs%2BHTN3JGMDZO7zbBhqIX%2BgzAL1hlrK649Qh114Oqfed3ENsgthcdhsa4kSXfwVRNrScpA3HRpRxOJkQoV1Nc4HEiGtZvTvX1ts%2BfA66RxH2t7KbIiO9ByDuIo%2FDpWmzrQzIL6gPY3NVbCPS6XHVmv%2FeOmJC9mKxvxO2QX0pV5fzzYFhAHIfoee0uL1%2FcrwT8mGF8ZP1uXZp2Dlou62WCqekpRtII6NgknrlnfHj9uIjWTr%2BLAVsNEPhWBvrqFxQTYdFeOyJHQDUpqAXvpyoxpi8ktSTVotl6eaG4SjoHU6fq5vSsWDXjiJouSoBufQsAk4QmHL2uaMVtSgvGJTdCl5GtDVu9aCbtWwcsV77nwFisUHjJkX9tVEdel4s8Xx%2BepEbZ%2B%2FcPLEvL7hk63SY2n%2FXCo%2FrWI7hjncFaTYbGjBR%2FHvq9r7%2B7jDc6YW9BjqkAYs3GPmJjNz8qPzSf1UrRovJ7bPOlsP8%2Fjet5XBDp7Lu5nzd0%2FU3MF6%2BW6Jb2RNlfjeEYITaj4nJmPwz3jjTz3uFbsIPZ5z%2BaH3pFiGl3vLzcEdMED7y3mzRqD7%2FuUVly%2FIc3uAqG%2BNv0HeVe%2BQo87RU3w8Z8H7V3nSGQ87fpw3j%2FchvPccDPy1bcyIKtvqIr7EZxOseievDVgujj1VdfC4x%2FDUA&X-Amz-Signature=ae79e4ee2729b3931d1e6da0582608bed7fed3ef756d00c8cfd9744f7b90006a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YX5NJEDY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQCXJHPtIGm9x9QIu0BAVbN4Yi%2FLfJMImMoHBAUC7r3T8gIgFS4qpilGpVcdBNpn5AeMk5eJNY%2BpmJ2jjE%2BMhjjRwp8q%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDLumK8a7eZ%2BuTLH7MCrcA0NYlKSAlMWZHjchliUrwataa1l%2FH6%2FnXJFZjQWCnetARetzPl3RadOl07poCr7DYBJEA49%2F7yxfMxPj265VScme1nw6DSzPgSyRUkGG4%2FU7RCfsC7RpzbcIZA27zgJ3UYnEqg4qGrz1IPhgZkul9%2BpIoBjWTP88pLvQ6QNBO4JUQAtAyqIY%2BBLJpSozOy7eT7kFIXHZP40zLv4ej0%2BvJOBtNvviYCtLbSK8y9PG6yyl3DsWrXW7lhyPHNaLMdcgmr4SH0RoSo5v2z7fpLKMe0KTcxJUkqUD1ZXBFD134Ugt43L1%2B%2B7ax3yRnrL4Txn3%2BUUk7MVMmtfj5edACQEnRTNYz%2FFn9FZpYjwrQg3bcT61sEftWOkpZ5wFlPezYHoeDCT5JppvotUOFzz0RgU3FwiUKWV5ZNp%2BlEwdtE23ElrdFwR58tsfUvo4ke3EeFoijPZO93lZKgbKFu07IN3vOm2EgbS50H0ywkUUnWYS26%2FWNmRoCIbirOPUFYRRRvlSXxOLwRjmYr4mB0CFsB6anfz2ZtzBu0oWkfY5%2FJRddShCxfsMkWazm9CDYjZpnJB2l2fDAPMsiWfUR6zRVt%2BHbM10WkkvA63E3c6goduZkyzz%2FPwHDTm6iDsLZ5U9MP%2Fohb0GOqUBXZE2bgvVD7qTis1gxSpQQprI1FaCj5CbHyx%2BH%2FrFj%2B8J%2B7KA0DmaeTy3xamoRTZrH0tXaYltpo8v2QaZCRzNvztSa8eQdKyTQleuiI3FdT1aTZ%2BCiUD5HVtGewldBFwWHeUcpKptUr3Kkb2rkxq9%2FB6PR%2FcXWA1EMa%2BzLnPBlxkcqRy9LPwOl8TqWY%2FjkrKt7r1ahhDN13EV9w5Er0F0JpCBAM8d&X-Amz-Signature=85f39db4e287aff5e3571557adc129d16de72cad19c80c8a15a854c644fc59ad&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAEB4W5V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCICgRKhhOTnS%2BGRWu5zcInb%2F2HMr9d24PYYm6HUDPb55SAiEAoSJNuNuOivVBoVdbs66NdW2bngVE9Mk9rvT8tB37y1Yq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDCBPdwCKzkcy%2BqG3HCrcA8Mzh6d10JeQ8LdR73gBcP5Xi%2BRpPHZR6yJE2v8%2BlzuH3O0ZwimmeKr48sFCag8uEjp6A6B2VobRVxLb3fuZenzAD0Yz7Tnu4hQRTkIGfnh8rX541vIbTvHc2TS309JzIAcR%2BM%2F9Gh9sJlxLELaDHu4529wrbqyXASM0LznV%2FIBNUGWwU3wsEiu9uS6Lu8qL1RuioA52rVqIaRvkisoKXYWtRQ7bw6X3kpxmev0M0ecAylCjoIIZQcLfKmp2MtI9MbR3CeQCz0IMEe3AG4r6EJLTq%2BeFB4WyAElFcac8GVr4xDwyPCG7nM4tI6%2BbrhNemQ1k8zgFbQ79Fqs2zo%2BDDxGlLhKXm18zJyf2u3malYuDPEvm%2BKlLKTFbWSYAnVcsVjCa0tMDWcIo38HGwDj%2BVUB16yKyicELFkYtXeSk88UmEJoFORmR8tFAD1gMoJTTkEtAYJy6cK27WXC0y1C9vO4PF6L%2B0dgukF3Vlt4AJHeXo4Cm7YWQZi3KZGap0lrDbn%2BZrVx3ztgU0%2F1zP%2BLN%2FtOFn2R765AIVaijQUjxthxWTi819Ea8qwrCKRK%2BvcgFK0slmyiCjBTHPuWAdJwMV3OyMDfXH%2BRxv55qsBN%2B0Qt88p6jEXpkqJkBumtzMObphb0GOqUBkxDu3YkiIxl9njo215asM18x7Yy2FsFNNvG7L%2F4H00cFUGUFCM2aGYsnaIr2TsU7owRokbHQ75vrctIbp4%2F6P%2BGL7FZh%2BOOSKO5HPoOqRoCyamnGqCxaj8NO2JTXvYf0jDDkTTz3Y2jjkM3puiYi2FDAiXEfUw6lpc2SMfMKjzvYjEOvSVhwmzfbs6Q0GKdxJ5od6EC1hhxgKrXR96BQ0%2B3Gl1V8&X-Amz-Signature=c941bd239af280f860c4fcd4baf614e96b0c447fd220197bd5aeb5bb836f16d0&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEMKDKOI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQDUdKt8ul8ie3IhTjDCcLt7IPTIPPlD4lldzHmOMUFm%2FgIhAI9b16KeZiGCeVvpp%2FvsOD3O2149DyF%2B2qXxr89dhzAJKv8DCCMQABoMNjM3NDIzMTgzODA1Igzs4u8FiGX4MEJEEsMq3AOVv43Rk33l1qaFQGY4OHMK6B5Nt5RJl2ebY084nkA5mfTxC5FdPr6a6x0374TPZmAnCreVHe8wkOh3VDiT2JVuD5tiIlBD0AelSqRyixWvmBKr6g4hNJVWCiFtbIESL%2BW3n7AyjKjwvJ1rk9liZKsDkkJoXqzEKvFECsdKZe0k%2Bb6keqhPc8NHkJJR1q7mWmyDZt%2BS5LrnrmDXk6d%2B2cdSzWoLR4ZqCElQsLPA6y0VJGoBwbUfVNEiYD2fBwIIORfCDKzGWLcMBUz7yZ2Ck%2BANyxsvZkB3rs1bpal1Sno2acHsu5at7rbIKPNSD8nnDYaWWbiHBmXJc1Dm0JiUhbzbxfA7GyrVak%2F4xXQKka5ZAZ4%2BizZufzLpZWPe6363ZpN3TUlR3o07TgVoJs9CM%2FTIm4OMyNTNOkYkV9mqutN%2BSV3fznWfrzhzF5gi1UKDfyk3qL2V7A9%2FotkR6wmfB%2BbKWy9CIUzbd6SqjuNyJ%2F2u9vYW60RbmHbdcZPsS9VYfeo43GgwkDfBV1h46A7pL7y2nwqCoD5N4JWtiEmiV9iCClTjseDToORrkZ3XnCfS2rOu7YmDUlrdlfwnjh8DorFCVeuGUaGUes0kv6e%2BDesgExOa%2BXoEJJ2zOxM8DjD26IW9BjqkAX161RgFc1EnAuWqnu1lr%2F7uEP%2FldTAkWqKh7OSPbToEcV1M1QYZPvVd9ouZGYwmjQG4h%2FPPOBt8%2FPmqlgz95xyNVlNslVNy1YLiAmG429g8RQc7%2Fv3jG8H%2FHWWvo13GAukdqfHfE6jLyIeskxWiBn%2FIYRIBe3qkS9vxEuSzAOt8sW8jOHt27MKTkhGMZjiDBErTuZe53GdtrBFy%2FJIObd7Nosc2&X-Amz-Signature=7c494476df9bb9106dae62f15292a6c5b853aa5c449a0fde4b0496c234360df8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIA4O22X%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQCS4kNPyD65GEVKj%2Ffo893deeHc3CxF7BMBlaIErJSRaAIgKpPTwwHdXxGTVF75iHdDUpXxx%2Fu4XwnmxnYcgKRnC1Eq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHW%2BxGUdnJNgX7dRCSrcA7vosNcccB%2Frie1uHuObb%2FSdrtt9UooSpTf7CW2etpNcGKcPiq0n7%2FeWagJ6LspRHxfmDjMbxkoiz4%2FgAmkZMOTEvzV1RfE0KcVa1ZrxvgSc5WN2yx%2BMVYcOz8%2B4QAPxJMqiMAUwGjAv0F9VrOl3Ga1c0kqoKix4%2B83oWjSUEsJEheR0MQtHYj2QWo84l3Ys5y0mzct6l91jBMutVqMVgL7F1Kj%2FNCOUC4%2F7BpBlWydWIGeQlcnErzk6bXv6N2Ffgek2oaRd2YVR%2Bs20ZU%2BLU%2BA78mW7kn49Nlb%2BOry2bn5apdQI3rWfScZmSbm%2BEVFdx5K7v1n%2BsrXh%2BVWR2JX2R4Z8rZWR%2BOmIjwzluBJXTnKSMTQaaVfJBUHiyfOK1TPFmSdmLPWjRJ9dXuTviCk72Up7BtMCnhSBdrsICioW6h30C6ZocQT4Jmex%2Fcrz197V1e1hG894h1vrdKg6mkRblNISbISEHx%2FYSHHcyaYm%2Bh0aYXYCCxzvxtV1KxspuI1qx7KKxBApRz5JkgX4t7HBukCLtG6oSDinw2qu9GwCs8zITJKUcNrCLXRo7PGmbnX4BwsIM%2BQq3agWrd%2BEwZMEJ0lH2lgA95yo%2FU%2Bm0%2F3DtHhPk%2BdWL%2BxOFsCZbrfFMNPphb0GOqUBnfKS2jk6AudGn4frvg3ZmBIrkPMoYjH%2BQeRiSlLZYsvGlsAvXhrMV2vLTYw6%2FeZATvbgjWSu0GitG2TUBPCvVeHOrXWzJMd%2BOcaTx4HLjId8oVXZ5WF9pw4BLP%2Bak29POB5s6k%2FPX88b1oj3dd75GwcrtKA9G0OcJJ5SoM2xmf%2Buxp5bWVee3nzslkg2yBVp6%2FpYQ784vYcPXTLgURovqqb1qAdJ&X-Amz-Signature=db0b197e196a75e3c809d6b8d98d2846d27c023b3250e5d9948da532ca26cf3c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIA4O22X%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQCS4kNPyD65GEVKj%2Ffo893deeHc3CxF7BMBlaIErJSRaAIgKpPTwwHdXxGTVF75iHdDUpXxx%2Fu4XwnmxnYcgKRnC1Eq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDHW%2BxGUdnJNgX7dRCSrcA7vosNcccB%2Frie1uHuObb%2FSdrtt9UooSpTf7CW2etpNcGKcPiq0n7%2FeWagJ6LspRHxfmDjMbxkoiz4%2FgAmkZMOTEvzV1RfE0KcVa1ZrxvgSc5WN2yx%2BMVYcOz8%2B4QAPxJMqiMAUwGjAv0F9VrOl3Ga1c0kqoKix4%2B83oWjSUEsJEheR0MQtHYj2QWo84l3Ys5y0mzct6l91jBMutVqMVgL7F1Kj%2FNCOUC4%2F7BpBlWydWIGeQlcnErzk6bXv6N2Ffgek2oaRd2YVR%2Bs20ZU%2BLU%2BA78mW7kn49Nlb%2BOry2bn5apdQI3rWfScZmSbm%2BEVFdx5K7v1n%2BsrXh%2BVWR2JX2R4Z8rZWR%2BOmIjwzluBJXTnKSMTQaaVfJBUHiyfOK1TPFmSdmLPWjRJ9dXuTviCk72Up7BtMCnhSBdrsICioW6h30C6ZocQT4Jmex%2Fcrz197V1e1hG894h1vrdKg6mkRblNISbISEHx%2FYSHHcyaYm%2Bh0aYXYCCxzvxtV1KxspuI1qx7KKxBApRz5JkgX4t7HBukCLtG6oSDinw2qu9GwCs8zITJKUcNrCLXRo7PGmbnX4BwsIM%2BQq3agWrd%2BEwZMEJ0lH2lgA95yo%2FU%2Bm0%2F3DtHhPk%2BdWL%2BxOFsCZbrfFMNPphb0GOqUBnfKS2jk6AudGn4frvg3ZmBIrkPMoYjH%2BQeRiSlLZYsvGlsAvXhrMV2vLTYw6%2FeZATvbgjWSu0GitG2TUBPCvVeHOrXWzJMd%2BOcaTx4HLjId8oVXZ5WF9pw4BLP%2Bak29POB5s6k%2FPX88b1oj3dd75GwcrtKA9G0OcJJ5SoM2xmf%2Buxp5bWVee3nzslkg2yBVp6%2FpYQ784vYcPXTLgURovqqb1qAdJ&X-Amz-Signature=02c86017a042f21270c06aae1772380ab68c20bc4b6b55f71bf55a0df3528080&X-Amz-SignedHeaders=host&x-id=GetObject)

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
