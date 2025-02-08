

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632PFRDOJ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDvhFgumCaYsbLfFY3B9fp%2BCCq6qURQfMSEC0ITDhoHmAiEA%2FVgQVv3CQtkB8TUV8%2BtVFg0ZKnDdQF6QJLUu%2BtBXRMsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPpc9D6RXSfTmBDmxircA9t4bbWouAqJDaU%2FPvIOTl9Zlbdv4ygfREbqNU6%2FibfxnVsMr%2BWw6ZNt1NWxeuonwC3UUNK6c%2BmH%2B%2FIqkU48Lm7Bb7Cn1I5eIpo71QqkLzL%2Fq0pVNRBP3XK0d8MngDMj%2BMNggNizp8RnIvmzrGzWkIYZ%2BhCArkc7KtWPJu3Lp6qwCcSAj1Ck5KMhD4lNUGG8jyud0lTea5cTW7ImqqHFXxS5mXc4q3TGgaNkOZ%2B0JBNR4WMFzKq7mDym9y%2BxaTfeIL3ka0ZXfPCFQFibGzQDaWbbFz7EMtC%2FER%2BNPdGTJb%2FENkKmvKWlmiKSi9KwiC6TE0tFLTgb0bSvZ0hRILWeO99hyPjswZXlUyfRe%2B28keTF8AffhhN5OKlVqw%2BqS45hOLAjYXEJxdxZ78SQEI7V67m7Xo8nEFH69tyOqGZ8loVz%2BM3pq%2FbS1paaqd6FqbDgf5izE5kIRifK9fl70KAc6DqCAyLlma%2B4jKsgdFexFjq6SpL3FDF4EutIjxsHfyLe9%2FtrasLrCHA6CbIK82dz1DpdjFZfk4Yq3HZwsHPFwiGjKbRSkqZuLtZFzrFqtsc50kpILZehKZtUrp3B580pDTCkcoaLMpfUJ0UkhkA4p6ZSy7yaIKFKqqNjEwKjMOqNnL0GOqUB1deh5c3Kt%2FenPJFBXVPKB7IgkYllwwrRIYkaqEZrnmnDeXW691Fwe0gvqvTWQp7XeZrQr4pA3LrW3cosFUtPeIRiVn7oNjEDiNUmkam86MzeM3D7xu3uwCMxo7p6U1BYMD%2BWKSPhal9g367Yjm2FVt4JIQ80EX9129fvtKTUAgtdDRX7ntN6aztMkWcstcu1xS1BICB25B0rLI%2FSjrneXO7AWcJy&X-Amz-Signature=4c6f189e43d030f263c9984324413a8550beaa455389882cf9337bf7edf105e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632PFRDOJ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDvhFgumCaYsbLfFY3B9fp%2BCCq6qURQfMSEC0ITDhoHmAiEA%2FVgQVv3CQtkB8TUV8%2BtVFg0ZKnDdQF6QJLUu%2BtBXRMsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPpc9D6RXSfTmBDmxircA9t4bbWouAqJDaU%2FPvIOTl9Zlbdv4ygfREbqNU6%2FibfxnVsMr%2BWw6ZNt1NWxeuonwC3UUNK6c%2BmH%2B%2FIqkU48Lm7Bb7Cn1I5eIpo71QqkLzL%2Fq0pVNRBP3XK0d8MngDMj%2BMNggNizp8RnIvmzrGzWkIYZ%2BhCArkc7KtWPJu3Lp6qwCcSAj1Ck5KMhD4lNUGG8jyud0lTea5cTW7ImqqHFXxS5mXc4q3TGgaNkOZ%2B0JBNR4WMFzKq7mDym9y%2BxaTfeIL3ka0ZXfPCFQFibGzQDaWbbFz7EMtC%2FER%2BNPdGTJb%2FENkKmvKWlmiKSi9KwiC6TE0tFLTgb0bSvZ0hRILWeO99hyPjswZXlUyfRe%2B28keTF8AffhhN5OKlVqw%2BqS45hOLAjYXEJxdxZ78SQEI7V67m7Xo8nEFH69tyOqGZ8loVz%2BM3pq%2FbS1paaqd6FqbDgf5izE5kIRifK9fl70KAc6DqCAyLlma%2B4jKsgdFexFjq6SpL3FDF4EutIjxsHfyLe9%2FtrasLrCHA6CbIK82dz1DpdjFZfk4Yq3HZwsHPFwiGjKbRSkqZuLtZFzrFqtsc50kpILZehKZtUrp3B580pDTCkcoaLMpfUJ0UkhkA4p6ZSy7yaIKFKqqNjEwKjMOqNnL0GOqUB1deh5c3Kt%2FenPJFBXVPKB7IgkYllwwrRIYkaqEZrnmnDeXW691Fwe0gvqvTWQp7XeZrQr4pA3LrW3cosFUtPeIRiVn7oNjEDiNUmkam86MzeM3D7xu3uwCMxo7p6U1BYMD%2BWKSPhal9g367Yjm2FVt4JIQ80EX9129fvtKTUAgtdDRX7ntN6aztMkWcstcu1xS1BICB25B0rLI%2FSjrneXO7AWcJy&X-Amz-Signature=7734a8df6a34fb44458bb851759780cfed24e3ff147e575d6427f1afe830ba21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632PFRDOJ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDvhFgumCaYsbLfFY3B9fp%2BCCq6qURQfMSEC0ITDhoHmAiEA%2FVgQVv3CQtkB8TUV8%2BtVFg0ZKnDdQF6QJLUu%2BtBXRMsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPpc9D6RXSfTmBDmxircA9t4bbWouAqJDaU%2FPvIOTl9Zlbdv4ygfREbqNU6%2FibfxnVsMr%2BWw6ZNt1NWxeuonwC3UUNK6c%2BmH%2B%2FIqkU48Lm7Bb7Cn1I5eIpo71QqkLzL%2Fq0pVNRBP3XK0d8MngDMj%2BMNggNizp8RnIvmzrGzWkIYZ%2BhCArkc7KtWPJu3Lp6qwCcSAj1Ck5KMhD4lNUGG8jyud0lTea5cTW7ImqqHFXxS5mXc4q3TGgaNkOZ%2B0JBNR4WMFzKq7mDym9y%2BxaTfeIL3ka0ZXfPCFQFibGzQDaWbbFz7EMtC%2FER%2BNPdGTJb%2FENkKmvKWlmiKSi9KwiC6TE0tFLTgb0bSvZ0hRILWeO99hyPjswZXlUyfRe%2B28keTF8AffhhN5OKlVqw%2BqS45hOLAjYXEJxdxZ78SQEI7V67m7Xo8nEFH69tyOqGZ8loVz%2BM3pq%2FbS1paaqd6FqbDgf5izE5kIRifK9fl70KAc6DqCAyLlma%2B4jKsgdFexFjq6SpL3FDF4EutIjxsHfyLe9%2FtrasLrCHA6CbIK82dz1DpdjFZfk4Yq3HZwsHPFwiGjKbRSkqZuLtZFzrFqtsc50kpILZehKZtUrp3B580pDTCkcoaLMpfUJ0UkhkA4p6ZSy7yaIKFKqqNjEwKjMOqNnL0GOqUB1deh5c3Kt%2FenPJFBXVPKB7IgkYllwwrRIYkaqEZrnmnDeXW691Fwe0gvqvTWQp7XeZrQr4pA3LrW3cosFUtPeIRiVn7oNjEDiNUmkam86MzeM3D7xu3uwCMxo7p6U1BYMD%2BWKSPhal9g367Yjm2FVt4JIQ80EX9129fvtKTUAgtdDRX7ntN6aztMkWcstcu1xS1BICB25B0rLI%2FSjrneXO7AWcJy&X-Amz-Signature=bc81f55e8d8b6cef468862eac78a37d91cf240ba26f3dccfd31cc8471c06775d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKZLSOL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGsJK1VUTjPN3sh%2B1m5SRPolgmTDef5wZ9HvvQBNqPqgAiEA8VHUmESOKF7ff27JgypcEKUtCE%2BKu%2BnLvYzZTXvHaBUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOM%2F8dEG6DftvBZjnSrcA1jM%2FmUrvVwiOYnqLtomEeSC87J%2Fcrv%2BDrSduYQCOdzzG1QPi9ID%2B63MpoN%2FCW7Zva8IAh%2FxyFIiALz7B%2B4E2mQ6IqHrQ8KPjFF77cBgnjjvWcitTwz6rbcJtM6mkuNwBdbSrsc8Ynqg%2FoS2ABk10DWr0YXO2ujY%2Fz0L1c3FbW1N9Nnsl7QCMgV2LxbHFoAJPuHGEgcPeJV0BnDDLYW0L5TxSWIj7t2OhhFpmGCSc6A7vo1RSQBs4HpVtpZBooAXjAtouwtOP030GN7dtHsiUWPB6lYOOLZ3Tn4siOvmeR6YQQDuRCfFXLZV4OJotHB5%2BQMoRA%2B4sHu7iht4kFcCih4w7cJsqL%2BnYiGYrJ5nZ3YNmtyN8UgIndC8NuP5pkK13yvT9XY3sAPv1VEJW%2FyK0XvexbiRbboDTdCUF41bNqHz9q1lk6CfK5gYtYDPBSvbTiqh%2BMLwN7SVfReJHLr5B3uWVDf3n2BPw1YzaWsYARR6dekgbA9gvo6mIxGli%2Bxxgvvw005jkBxh11tEdqP71Xsb%2BeN8HZxrq35nk12FhFZkDHVNcJA1iE8A94IRqXRPB9xJbjQpEqnulxTIC1KMEZ818aOELy2m2Z16yLRZIACyFBUsMRG%2Fo1CtQNjNMNeOnL0GOqUBc%2FYx1Dh%2BI3J02CRJbEevalkxIXr0Xs%2BBdMnE7phKFDFvhXgx7oOhM%2B5gRyXg%2FQJ7e0UuEj93kOB2NwzotCGKq0p8tQzk7PGOrsO%2BUHUiKoxHolj5juaA0GxqJBybLNfoyJqm5rJDp69e%2B%2Fdrv2%2B5W5EVrqDlp%2B3qQg6k8LdN4A6PYlQQLUFPx2o08BhBGcVEekWWgqdEgIuc6%2FRjg1SyJm7cCADA&X-Amz-Signature=88b8f0efe380abe7f064ac1d4faf63555b02a5b9d69cb298f933abda646aff96&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKZLSOL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGsJK1VUTjPN3sh%2B1m5SRPolgmTDef5wZ9HvvQBNqPqgAiEA8VHUmESOKF7ff27JgypcEKUtCE%2BKu%2BnLvYzZTXvHaBUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOM%2F8dEG6DftvBZjnSrcA1jM%2FmUrvVwiOYnqLtomEeSC87J%2Fcrv%2BDrSduYQCOdzzG1QPi9ID%2B63MpoN%2FCW7Zva8IAh%2FxyFIiALz7B%2B4E2mQ6IqHrQ8KPjFF77cBgnjjvWcitTwz6rbcJtM6mkuNwBdbSrsc8Ynqg%2FoS2ABk10DWr0YXO2ujY%2Fz0L1c3FbW1N9Nnsl7QCMgV2LxbHFoAJPuHGEgcPeJV0BnDDLYW0L5TxSWIj7t2OhhFpmGCSc6A7vo1RSQBs4HpVtpZBooAXjAtouwtOP030GN7dtHsiUWPB6lYOOLZ3Tn4siOvmeR6YQQDuRCfFXLZV4OJotHB5%2BQMoRA%2B4sHu7iht4kFcCih4w7cJsqL%2BnYiGYrJ5nZ3YNmtyN8UgIndC8NuP5pkK13yvT9XY3sAPv1VEJW%2FyK0XvexbiRbboDTdCUF41bNqHz9q1lk6CfK5gYtYDPBSvbTiqh%2BMLwN7SVfReJHLr5B3uWVDf3n2BPw1YzaWsYARR6dekgbA9gvo6mIxGli%2Bxxgvvw005jkBxh11tEdqP71Xsb%2BeN8HZxrq35nk12FhFZkDHVNcJA1iE8A94IRqXRPB9xJbjQpEqnulxTIC1KMEZ818aOELy2m2Z16yLRZIACyFBUsMRG%2Fo1CtQNjNMNeOnL0GOqUBc%2FYx1Dh%2BI3J02CRJbEevalkxIXr0Xs%2BBdMnE7phKFDFvhXgx7oOhM%2B5gRyXg%2FQJ7e0UuEj93kOB2NwzotCGKq0p8tQzk7PGOrsO%2BUHUiKoxHolj5juaA0GxqJBybLNfoyJqm5rJDp69e%2B%2Fdrv2%2B5W5EVrqDlp%2B3qQg6k8LdN4A6PYlQQLUFPx2o08BhBGcVEekWWgqdEgIuc6%2FRjg1SyJm7cCADA&X-Amz-Signature=4c3e30dc182c0a81048327eca25c62d2f9792be765e845532205571389d08694&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKZLSOL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGsJK1VUTjPN3sh%2B1m5SRPolgmTDef5wZ9HvvQBNqPqgAiEA8VHUmESOKF7ff27JgypcEKUtCE%2BKu%2BnLvYzZTXvHaBUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOM%2F8dEG6DftvBZjnSrcA1jM%2FmUrvVwiOYnqLtomEeSC87J%2Fcrv%2BDrSduYQCOdzzG1QPi9ID%2B63MpoN%2FCW7Zva8IAh%2FxyFIiALz7B%2B4E2mQ6IqHrQ8KPjFF77cBgnjjvWcitTwz6rbcJtM6mkuNwBdbSrsc8Ynqg%2FoS2ABk10DWr0YXO2ujY%2Fz0L1c3FbW1N9Nnsl7QCMgV2LxbHFoAJPuHGEgcPeJV0BnDDLYW0L5TxSWIj7t2OhhFpmGCSc6A7vo1RSQBs4HpVtpZBooAXjAtouwtOP030GN7dtHsiUWPB6lYOOLZ3Tn4siOvmeR6YQQDuRCfFXLZV4OJotHB5%2BQMoRA%2B4sHu7iht4kFcCih4w7cJsqL%2BnYiGYrJ5nZ3YNmtyN8UgIndC8NuP5pkK13yvT9XY3sAPv1VEJW%2FyK0XvexbiRbboDTdCUF41bNqHz9q1lk6CfK5gYtYDPBSvbTiqh%2BMLwN7SVfReJHLr5B3uWVDf3n2BPw1YzaWsYARR6dekgbA9gvo6mIxGli%2Bxxgvvw005jkBxh11tEdqP71Xsb%2BeN8HZxrq35nk12FhFZkDHVNcJA1iE8A94IRqXRPB9xJbjQpEqnulxTIC1KMEZ818aOELy2m2Z16yLRZIACyFBUsMRG%2Fo1CtQNjNMNeOnL0GOqUBc%2FYx1Dh%2BI3J02CRJbEevalkxIXr0Xs%2BBdMnE7phKFDFvhXgx7oOhM%2B5gRyXg%2FQJ7e0UuEj93kOB2NwzotCGKq0p8tQzk7PGOrsO%2BUHUiKoxHolj5juaA0GxqJBybLNfoyJqm5rJDp69e%2B%2Fdrv2%2B5W5EVrqDlp%2B3qQg6k8LdN4A6PYlQQLUFPx2o08BhBGcVEekWWgqdEgIuc6%2FRjg1SyJm7cCADA&X-Amz-Signature=50fd04b734dcbeec8eaca4dffbe10ce04f6b84c9f442453cfc05d597fbafe259&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKZLSOL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGsJK1VUTjPN3sh%2B1m5SRPolgmTDef5wZ9HvvQBNqPqgAiEA8VHUmESOKF7ff27JgypcEKUtCE%2BKu%2BnLvYzZTXvHaBUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOM%2F8dEG6DftvBZjnSrcA1jM%2FmUrvVwiOYnqLtomEeSC87J%2Fcrv%2BDrSduYQCOdzzG1QPi9ID%2B63MpoN%2FCW7Zva8IAh%2FxyFIiALz7B%2B4E2mQ6IqHrQ8KPjFF77cBgnjjvWcitTwz6rbcJtM6mkuNwBdbSrsc8Ynqg%2FoS2ABk10DWr0YXO2ujY%2Fz0L1c3FbW1N9Nnsl7QCMgV2LxbHFoAJPuHGEgcPeJV0BnDDLYW0L5TxSWIj7t2OhhFpmGCSc6A7vo1RSQBs4HpVtpZBooAXjAtouwtOP030GN7dtHsiUWPB6lYOOLZ3Tn4siOvmeR6YQQDuRCfFXLZV4OJotHB5%2BQMoRA%2B4sHu7iht4kFcCih4w7cJsqL%2BnYiGYrJ5nZ3YNmtyN8UgIndC8NuP5pkK13yvT9XY3sAPv1VEJW%2FyK0XvexbiRbboDTdCUF41bNqHz9q1lk6CfK5gYtYDPBSvbTiqh%2BMLwN7SVfReJHLr5B3uWVDf3n2BPw1YzaWsYARR6dekgbA9gvo6mIxGli%2Bxxgvvw005jkBxh11tEdqP71Xsb%2BeN8HZxrq35nk12FhFZkDHVNcJA1iE8A94IRqXRPB9xJbjQpEqnulxTIC1KMEZ818aOELy2m2Z16yLRZIACyFBUsMRG%2Fo1CtQNjNMNeOnL0GOqUBc%2FYx1Dh%2BI3J02CRJbEevalkxIXr0Xs%2BBdMnE7phKFDFvhXgx7oOhM%2B5gRyXg%2FQJ7e0UuEj93kOB2NwzotCGKq0p8tQzk7PGOrsO%2BUHUiKoxHolj5juaA0GxqJBybLNfoyJqm5rJDp69e%2B%2Fdrv2%2B5W5EVrqDlp%2B3qQg6k8LdN4A6PYlQQLUFPx2o08BhBGcVEekWWgqdEgIuc6%2FRjg1SyJm7cCADA&X-Amz-Signature=15cff1d9a0a39b1d497f26c8dd9557b9b09808ab387a52009abb6ed324ae16d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKZLSOL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGsJK1VUTjPN3sh%2B1m5SRPolgmTDef5wZ9HvvQBNqPqgAiEA8VHUmESOKF7ff27JgypcEKUtCE%2BKu%2BnLvYzZTXvHaBUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOM%2F8dEG6DftvBZjnSrcA1jM%2FmUrvVwiOYnqLtomEeSC87J%2Fcrv%2BDrSduYQCOdzzG1QPi9ID%2B63MpoN%2FCW7Zva8IAh%2FxyFIiALz7B%2B4E2mQ6IqHrQ8KPjFF77cBgnjjvWcitTwz6rbcJtM6mkuNwBdbSrsc8Ynqg%2FoS2ABk10DWr0YXO2ujY%2Fz0L1c3FbW1N9Nnsl7QCMgV2LxbHFoAJPuHGEgcPeJV0BnDDLYW0L5TxSWIj7t2OhhFpmGCSc6A7vo1RSQBs4HpVtpZBooAXjAtouwtOP030GN7dtHsiUWPB6lYOOLZ3Tn4siOvmeR6YQQDuRCfFXLZV4OJotHB5%2BQMoRA%2B4sHu7iht4kFcCih4w7cJsqL%2BnYiGYrJ5nZ3YNmtyN8UgIndC8NuP5pkK13yvT9XY3sAPv1VEJW%2FyK0XvexbiRbboDTdCUF41bNqHz9q1lk6CfK5gYtYDPBSvbTiqh%2BMLwN7SVfReJHLr5B3uWVDf3n2BPw1YzaWsYARR6dekgbA9gvo6mIxGli%2Bxxgvvw005jkBxh11tEdqP71Xsb%2BeN8HZxrq35nk12FhFZkDHVNcJA1iE8A94IRqXRPB9xJbjQpEqnulxTIC1KMEZ818aOELy2m2Z16yLRZIACyFBUsMRG%2Fo1CtQNjNMNeOnL0GOqUBc%2FYx1Dh%2BI3J02CRJbEevalkxIXr0Xs%2BBdMnE7phKFDFvhXgx7oOhM%2B5gRyXg%2FQJ7e0UuEj93kOB2NwzotCGKq0p8tQzk7PGOrsO%2BUHUiKoxHolj5juaA0GxqJBybLNfoyJqm5rJDp69e%2B%2Fdrv2%2B5W5EVrqDlp%2B3qQg6k8LdN4A6PYlQQLUFPx2o08BhBGcVEekWWgqdEgIuc6%2FRjg1SyJm7cCADA&X-Amz-Signature=c2040b647a5146511a5d247e75dc67c3ed80c091bcd3bb09dd3d128b28662bed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKZLSOL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGsJK1VUTjPN3sh%2B1m5SRPolgmTDef5wZ9HvvQBNqPqgAiEA8VHUmESOKF7ff27JgypcEKUtCE%2BKu%2BnLvYzZTXvHaBUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOM%2F8dEG6DftvBZjnSrcA1jM%2FmUrvVwiOYnqLtomEeSC87J%2Fcrv%2BDrSduYQCOdzzG1QPi9ID%2B63MpoN%2FCW7Zva8IAh%2FxyFIiALz7B%2B4E2mQ6IqHrQ8KPjFF77cBgnjjvWcitTwz6rbcJtM6mkuNwBdbSrsc8Ynqg%2FoS2ABk10DWr0YXO2ujY%2Fz0L1c3FbW1N9Nnsl7QCMgV2LxbHFoAJPuHGEgcPeJV0BnDDLYW0L5TxSWIj7t2OhhFpmGCSc6A7vo1RSQBs4HpVtpZBooAXjAtouwtOP030GN7dtHsiUWPB6lYOOLZ3Tn4siOvmeR6YQQDuRCfFXLZV4OJotHB5%2BQMoRA%2B4sHu7iht4kFcCih4w7cJsqL%2BnYiGYrJ5nZ3YNmtyN8UgIndC8NuP5pkK13yvT9XY3sAPv1VEJW%2FyK0XvexbiRbboDTdCUF41bNqHz9q1lk6CfK5gYtYDPBSvbTiqh%2BMLwN7SVfReJHLr5B3uWVDf3n2BPw1YzaWsYARR6dekgbA9gvo6mIxGli%2Bxxgvvw005jkBxh11tEdqP71Xsb%2BeN8HZxrq35nk12FhFZkDHVNcJA1iE8A94IRqXRPB9xJbjQpEqnulxTIC1KMEZ818aOELy2m2Z16yLRZIACyFBUsMRG%2Fo1CtQNjNMNeOnL0GOqUBc%2FYx1Dh%2BI3J02CRJbEevalkxIXr0Xs%2BBdMnE7phKFDFvhXgx7oOhM%2B5gRyXg%2FQJ7e0UuEj93kOB2NwzotCGKq0p8tQzk7PGOrsO%2BUHUiKoxHolj5juaA0GxqJBybLNfoyJqm5rJDp69e%2B%2Fdrv2%2B5W5EVrqDlp%2B3qQg6k8LdN4A6PYlQQLUFPx2o08BhBGcVEekWWgqdEgIuc6%2FRjg1SyJm7cCADA&X-Amz-Signature=0d3bc99fdccd87e2764540b4ed8e07fa656cf9d54560cb5ae9750556c5a17afa&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665VCNB6W%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIBG%2FQcZqOoAVO%2FcfrKHICq916aPcuBZai8dcSmGraSA3AiBR19SOPhwj%2BbReSdAUpD7L9rQ0Ouwe2JAnBGeP5R4DjCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfod78PC1QxJsagz0KtwDzKgQZEGHayoIpaID7LCK%2FfynCLYK%2Bsnab0lslWCyjsVKTzEy7DY8gmokj87bg0PrCsrX%2B0D04B2PjWldqVFAEcsnZwz1Diphu62BnMVV%2BnGOB3tk9Dm7hwvv1MhRY59%2FmiP3xj4%2BMlxVu4PB4aKkQ6po4YYbIN76xLLj%2B%2B7n8snannm0K2%2FO%2Fs8eYXRlEEK6EDs%2FG7N%2FAa4QQ25kMuC0bax4FWQ69bCJd%2Bj3NKMWtZKA%2FpqPmzmSLEe0BrcPkYxe7lRrqtrXgUYkRti3oMWBCdc8uYJEfClzZQHX0uuz8E9TWekx3Kae5%2FtfeCNW4WyciyGHnvs0vKLqlCv6dR3EOUXT1Y3b9vZhDdWYLEkde%2BClKpQuPvE%2FsQlJ66jk5jgodaiBQol9GGqAzbbiUofpKLzMqTHys5E0jaAelL7Wtvf57l7fm%2FQoDeYRDpCcgVT192AaDZExMgmNhTRb%2Fw9IUsGx1RhpiHusiw7X04uS6kZLFd87AjdUT3egPQ7VU%2FhJI7QMisHYfGPjdLiFUEmcF0aqgh9sUljnYHLS%2F6XrMmFZob1NoeFvHToDZnpVRtT1%2Bx23ncw8OXMVUXcndj9BCnNdF6WKgJOst3wfaZKypzn4d5UIwpr0EpG4%2FYYw1I6cvQY6pgHnzWpL%2BbkNbd2gwbCiBj%2FArhw7RTszTUKRXdX98VdE4E%2Fe%2BdwI8i85ufbtZw7tSgLG7YZN2fFzMGTbkMrFoFN6UJYhHNx%2FwXobQOfGsRHyjxK%2B%2FmhoL%2FS%2BSaZqcCh8sI1Zo7iI6Ht2SCyX3QwZxUGhaGw87CT%2By6BefjmcBgTsQgouaNf3aOzusw%2BpUYCcUFmOlqfWqwiE%2BIw%2BD7fnIWG2J1kEHC9U&X-Amz-Signature=71e259d7579e3e6d9ef6f15890f2cb8a7644006fb594797979a6b4ddbc351d78&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YALTUEA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIBEl6gwINphz9K6JSAT9SXZrAWd7eSmWcIcJ1x3InTtWAiAdvlzT%2Fw2cGI99nIcLPgMhfkkKz7FJruBRU6SV44yVMSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD5PSteHlySGg2QDMKtwDhouwLe80XSBKOQu%2BWTIAFZ85BHTrgMQ4OVwujDo3xfwhJprRVNn17hZ3gWajDzTVDZITmTNMPPQuM7N%2Bx29Kzn57vg5OSCexBSkptIaMpcHlyT2pm4N9CTqImab6Zl0%2FbP3oQhKQt3pcNRFpIEJdbpg66Y3B5zHCPRvXLSAFmV7C3AkMitzkWArZDMUI8EbuozqOjKCp45WLLmQ9E3aOwsLc6gq9K8E2gYVRmIh%2FgVJC47YbOxshdEuboyZKK2bD7J1vKFgQ15AtjfD5BvqYjNywUMFLrpIuE4IzCP%2FKAjdJDk7ldzbYSsrky%2FJtd0vO%2BgYEAi4RfMXd9EyNsspsmNXefJKxaxZH9hZ5twgE7DD8fAAJ%2BZpcGd35c2kvbLigfpwavhfPT6t6bVICSNXsXio4JKuboZhIZ0UlM48a9Ag2rsA3oGXoZyV6pu0auFJRwWWpJQUVK3fxBJ3ZhfTaqKQ6IiAqTahpg0Glo0bcBODJB%2BBrTAwLCbx8aSKWvBJubZXFXr6maer85YqcyDXTmsBplX%2FO2C0C37BHBPDTYWG1aaXnfNSbe1nmbwdSNI3NitqstulRmg177Mmrwy0KMvg2SJDQJNxk1OW8pvyqA%2BbP1onicTK%2FNeX%2Fhmkw9Y2cvQY6pgFAy69fWGjSgWWb5BRsGtu7t%2Fn%2BNKSnNeKmOmr1bTze3Khsf6mDzm2bSd69dr0nGTeOR9%2FTx0ZwczwTEHDRZcyl%2FxnCvP%2FARwu6CiQS0RANpeotMU4lKfD4e%2ByDJAA7%2BFMppVheFJPeLCEsv8JuqHSWW1iXxD84OS31pGrxxjZww%2B6z4mX9as16PyprI7gYXJ9LxJC2KmUyCKdS5%2ByYRrUZj7Nb8Xxy&X-Amz-Signature=09a3b324cc247423f916cc3e58f0b4f92c687cad9add8cf837fc477ccbea2be5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKZLSOL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGsJK1VUTjPN3sh%2B1m5SRPolgmTDef5wZ9HvvQBNqPqgAiEA8VHUmESOKF7ff27JgypcEKUtCE%2BKu%2BnLvYzZTXvHaBUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOM%2F8dEG6DftvBZjnSrcA1jM%2FmUrvVwiOYnqLtomEeSC87J%2Fcrv%2BDrSduYQCOdzzG1QPi9ID%2B63MpoN%2FCW7Zva8IAh%2FxyFIiALz7B%2B4E2mQ6IqHrQ8KPjFF77cBgnjjvWcitTwz6rbcJtM6mkuNwBdbSrsc8Ynqg%2FoS2ABk10DWr0YXO2ujY%2Fz0L1c3FbW1N9Nnsl7QCMgV2LxbHFoAJPuHGEgcPeJV0BnDDLYW0L5TxSWIj7t2OhhFpmGCSc6A7vo1RSQBs4HpVtpZBooAXjAtouwtOP030GN7dtHsiUWPB6lYOOLZ3Tn4siOvmeR6YQQDuRCfFXLZV4OJotHB5%2BQMoRA%2B4sHu7iht4kFcCih4w7cJsqL%2BnYiGYrJ5nZ3YNmtyN8UgIndC8NuP5pkK13yvT9XY3sAPv1VEJW%2FyK0XvexbiRbboDTdCUF41bNqHz9q1lk6CfK5gYtYDPBSvbTiqh%2BMLwN7SVfReJHLr5B3uWVDf3n2BPw1YzaWsYARR6dekgbA9gvo6mIxGli%2Bxxgvvw005jkBxh11tEdqP71Xsb%2BeN8HZxrq35nk12FhFZkDHVNcJA1iE8A94IRqXRPB9xJbjQpEqnulxTIC1KMEZ818aOELy2m2Z16yLRZIACyFBUsMRG%2Fo1CtQNjNMNeOnL0GOqUBc%2FYx1Dh%2BI3J02CRJbEevalkxIXr0Xs%2BBdMnE7phKFDFvhXgx7oOhM%2B5gRyXg%2FQJ7e0UuEj93kOB2NwzotCGKq0p8tQzk7PGOrsO%2BUHUiKoxHolj5juaA0GxqJBybLNfoyJqm5rJDp69e%2B%2Fdrv2%2B5W5EVrqDlp%2B3qQg6k8LdN4A6PYlQQLUFPx2o08BhBGcVEekWWgqdEgIuc6%2FRjg1SyJm7cCADA&X-Amz-Signature=22cc8e1275695f445333f39b78b5ace3fccecf580ae27df6a42ab3720ca99b82&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKZLSOL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGsJK1VUTjPN3sh%2B1m5SRPolgmTDef5wZ9HvvQBNqPqgAiEA8VHUmESOKF7ff27JgypcEKUtCE%2BKu%2BnLvYzZTXvHaBUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOM%2F8dEG6DftvBZjnSrcA1jM%2FmUrvVwiOYnqLtomEeSC87J%2Fcrv%2BDrSduYQCOdzzG1QPi9ID%2B63MpoN%2FCW7Zva8IAh%2FxyFIiALz7B%2B4E2mQ6IqHrQ8KPjFF77cBgnjjvWcitTwz6rbcJtM6mkuNwBdbSrsc8Ynqg%2FoS2ABk10DWr0YXO2ujY%2Fz0L1c3FbW1N9Nnsl7QCMgV2LxbHFoAJPuHGEgcPeJV0BnDDLYW0L5TxSWIj7t2OhhFpmGCSc6A7vo1RSQBs4HpVtpZBooAXjAtouwtOP030GN7dtHsiUWPB6lYOOLZ3Tn4siOvmeR6YQQDuRCfFXLZV4OJotHB5%2BQMoRA%2B4sHu7iht4kFcCih4w7cJsqL%2BnYiGYrJ5nZ3YNmtyN8UgIndC8NuP5pkK13yvT9XY3sAPv1VEJW%2FyK0XvexbiRbboDTdCUF41bNqHz9q1lk6CfK5gYtYDPBSvbTiqh%2BMLwN7SVfReJHLr5B3uWVDf3n2BPw1YzaWsYARR6dekgbA9gvo6mIxGli%2Bxxgvvw005jkBxh11tEdqP71Xsb%2BeN8HZxrq35nk12FhFZkDHVNcJA1iE8A94IRqXRPB9xJbjQpEqnulxTIC1KMEZ818aOELy2m2Z16yLRZIACyFBUsMRG%2Fo1CtQNjNMNeOnL0GOqUBc%2FYx1Dh%2BI3J02CRJbEevalkxIXr0Xs%2BBdMnE7phKFDFvhXgx7oOhM%2B5gRyXg%2FQJ7e0UuEj93kOB2NwzotCGKq0p8tQzk7PGOrsO%2BUHUiKoxHolj5juaA0GxqJBybLNfoyJqm5rJDp69e%2B%2Fdrv2%2B5W5EVrqDlp%2B3qQg6k8LdN4A6PYlQQLUFPx2o08BhBGcVEekWWgqdEgIuc6%2FRjg1SyJm7cCADA&X-Amz-Signature=73afa89e811a1658a58f8e26af88f88b3944cace27baa4fdbc002714c23e787d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKZLSOL7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGsJK1VUTjPN3sh%2B1m5SRPolgmTDef5wZ9HvvQBNqPqgAiEA8VHUmESOKF7ff27JgypcEKUtCE%2BKu%2BnLvYzZTXvHaBUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOM%2F8dEG6DftvBZjnSrcA1jM%2FmUrvVwiOYnqLtomEeSC87J%2Fcrv%2BDrSduYQCOdzzG1QPi9ID%2B63MpoN%2FCW7Zva8IAh%2FxyFIiALz7B%2B4E2mQ6IqHrQ8KPjFF77cBgnjjvWcitTwz6rbcJtM6mkuNwBdbSrsc8Ynqg%2FoS2ABk10DWr0YXO2ujY%2Fz0L1c3FbW1N9Nnsl7QCMgV2LxbHFoAJPuHGEgcPeJV0BnDDLYW0L5TxSWIj7t2OhhFpmGCSc6A7vo1RSQBs4HpVtpZBooAXjAtouwtOP030GN7dtHsiUWPB6lYOOLZ3Tn4siOvmeR6YQQDuRCfFXLZV4OJotHB5%2BQMoRA%2B4sHu7iht4kFcCih4w7cJsqL%2BnYiGYrJ5nZ3YNmtyN8UgIndC8NuP5pkK13yvT9XY3sAPv1VEJW%2FyK0XvexbiRbboDTdCUF41bNqHz9q1lk6CfK5gYtYDPBSvbTiqh%2BMLwN7SVfReJHLr5B3uWVDf3n2BPw1YzaWsYARR6dekgbA9gvo6mIxGli%2Bxxgvvw005jkBxh11tEdqP71Xsb%2BeN8HZxrq35nk12FhFZkDHVNcJA1iE8A94IRqXRPB9xJbjQpEqnulxTIC1KMEZ818aOELy2m2Z16yLRZIACyFBUsMRG%2Fo1CtQNjNMNeOnL0GOqUBc%2FYx1Dh%2BI3J02CRJbEevalkxIXr0Xs%2BBdMnE7phKFDFvhXgx7oOhM%2B5gRyXg%2FQJ7e0UuEj93kOB2NwzotCGKq0p8tQzk7PGOrsO%2BUHUiKoxHolj5juaA0GxqJBybLNfoyJqm5rJDp69e%2B%2Fdrv2%2B5W5EVrqDlp%2B3qQg6k8LdN4A6PYlQQLUFPx2o08BhBGcVEekWWgqdEgIuc6%2FRjg1SyJm7cCADA&X-Amz-Signature=8fdc454ddd8f90ee738cf0414b70d5b2e00551893ce0a3a9c9ea7ca4e34fbdd3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI5YVOWN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD4zySTayAJLyzbghvdc76UokIbaE%2BF%2FOwWj5rIXusSIAIgAIT5LKMfNWUXEbgE3ShWqMDZK9jRY8oBphdF7H4Ze%2FIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEyDLabWWhNpDsN4XSrcA9kLKs7stmedfxGm0Zsc7EEZiZ7ofu%2Bs%2BsrvlW2u6vtY7Ti5%2Bc%2FU9FscZ9lrDNJJS5f5LOvmNhfm1X1G3ZdEDbN1UYf2ptio3Y4%2FDm8Q%2FYj7AoBrmFcTeuR6zqhI%2FPUVV2HW6SyOp36oCrbF3jR15AYAA4ndqGuPYeF9HbwfECQm%2BX7pEWbjfGaAfChZgoxYRhFspUKfbZK9AXgkRqMygs%2FzfhzSvCLoc67RV1FvhfyK9%2FZ9xDrZVxSp3%2FYiCxu0QWPGvt1EcJyXOJkJqFi8kRpi3QNNDQTWIy199lBGwmxskcDvBWIx40Yg%2BmHNoRVR0FpO%2BesgJO3ZWfUcIN9GkrDGG0upurqgtGWL3jCcqoeQ7PWhllvfg%2FoI4O7hqod6aqvdEx34BWT42o3uYtZfDS1Pj9oXXQr065vn0zdmsgHReFOuJdhfz9T1VDJJNw3mS7%2Bvrrwrsc6b2DiOlw6VYnfpSzRm83ItJ9ZiUv93zzwHY%2BSpAW5wNwlLnKXWE0guPDWfyYU4WUBhXkwfm0TiSsP0U%2BMxVD%2BRD14y8U07m%2BSEco0O5RlTmyIeuUQy3q%2BIkUN%2FKfQOtMNJd3DmZpx7tSIhw%2Fpc%2Fp%2FkxHIOyhQR6DweaZo07LYYOSU%2BrSUTMNSOnL0GOqUBR%2BgDo3D9fEebkJNtdn08M5L2Txt9Mjb0FeigeKvpoO8qtQJM7xLhLCZidTRIaZgtkmuJirWg9Lzz1rV0W4O7fuOhiL8z9iiJkLdHxTku%2FCike327MIiZkh%2FKeyjdMNyVD3pBkoLRbsJ6x%2BFj76tRqC2x7oBP4l%2BqcaJc9CJ0v7%2BLj30qcvDI0MwQK9sGIQKrSuUUtdpgh07a9ZRiR26%2B%2BWegRYQB&X-Amz-Signature=8df6e3141988a51dcdc574b3ceb85349402c603ba7decd5ccae54e42872892f9&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZGN5MVV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCuVbiJyhlbrJfRad4M53v7vRNz4kEKfOD2tVGfueVo0AIgVDSxiP%2F4pL36dfa7%2Fyhy3MRf6vg7a5zs7%2FeKpRkcocEqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOnR%2B2w3wIerAwH4QyrcA%2FjiREV7ybhAlULWmEPvPz1gTF%2BZYMlcWX5h0fXJ6CH78sm1J2xuS4PEWczMoP2Bt8YWGWP9W%2FkBY8e5NrdvXsNP88u7H2S4FqpNeDc1kMB58GXfMgp7aKxqDVpAIdsrRQhUeUadtEqZcI2vuEBX0wao7D0yPNTBuOT30U4I2xIjDWQcdEaV84YTLXirm8g6eAZBP7Jrt6yTE6jZ%2BmCPOiYiLOrFt6%2F6h4AFzYzI%2FibsbevWAPAwYg34lMUx%2BX4tQW%2BYyb51UeU0qqyEc41%2FxoI97tWzNyZEv6ZLwnQrTbRzY2uUafySyKNuWW7qfaaa04uIOEodIpCj6ypdvPacC9nI%2ByZZ%2FD%2F2qCsZuGsf9ih0HHgllC%2Bs42TAhHk5K3nN98%2FyRJUqPX9hBRjy4TB%2BrLe0ieyhQ8YyX3rom48yXF4ggDD37hJdg%2BTEC6zALPWHJmj7cGWmB1X0WL%2BP3gajLodcDB98sA3zZ58Ywj4CkaL9QwGEFjp30z7bxEYX0i2VN9Y31herucwVTKUsBIIfct%2BTUFH%2FjvYi4%2B6Jd%2F5HlNfcL1Mu%2B8kM9ndumuXUZFrKs%2FDywHlcZGVFBJ5J7yXNjJrz6NiLhJ56vJ2CIuHxYPLmUta61rTi2MXvPKPAMNSOnL0GOqUBV3J6h%2FdkOvt9MHqwVB749sg3ZW2yzFO6zbRXl2qvV%2F3o0m20qPAQvarCQcVjm1gtZQHxw5FehWu2ueTSZS3IDWDrXO5hZ5vfu7xSCd3XIzquRLK%2FXRYilLF5y2xOrsZG2%2F0vuagoHptvk6iy4Go5NmCuLapeM6R59OU18Z50EtK8PcTOhRnhRC%2Bjd2x0ykhSLPUJuDWHsmSBMxbZCtx4qHk6Hyyz&X-Amz-Signature=9cb7e7046445fb37eed37ae597e331391ae210d8910c41b811ba5f99cbb64671&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4BZCYV5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDAj2vXc2j68iicB2TOaa89Vd%2BwnO%2F3cce7Pz7E3cNpTQIgF59QKAw1u0G8cJTU0V5tZg%2BrxlTJGqCw4%2Fkj%2Fz6Z2u0qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDbtSZKGRwCuZJ9CqCrcAz4Yxa%2Fw89rURyiQPMxuaOuV4g7bjicLLE7zDHlqkryCowXcUWaR7lHmvehj%2Fck%2FdQvEtWdm%2B%2BvAgafPa470rH5QZ9xGzqKaZiBiQXNRDtfMff6Z8e9Z%2FRisN7WnVFWIgdJO9EvmfYXhxVzrZtTbT4sShe2JrorptCXBy%2F4UGhZnCD0No0qHRv66ZzF4qW7XInqVsiLArbhBrPVs50wQdiYaRP%2FFdKhMeP5jJJufkiMSPOkwRuirA0i65igYpU0QZYhVUU%2FURkXr3vVKD346EMY8KkZhiCq8yDlkwyBRWPcmGOZ2YXRbq6Spk%2BvoHgoBEu6yZ2UA1G5yJrWl9sOYskBNueswuMvt7YS0pGFRkMxJnh8mgeyCWgX%2BKoWPWDcs6UqFn6POXa81zd%2BhOYKmbXk52nBnWBe37vcwgNZ8tUzIGRr4QLI1tTtuSjeAR6h7H9B72kHdKe9uh7NrGhIdJcpAIen5ukOoa43aaguLj36Bv8Zpc2YlSxGcv6%2BawhqI2T3r6j0hN%2BLywWo0vApGQWMpwCJPE%2B4Bh6Who72fmUGHB5LUIJ6WFlHqfB4tc8jivESjNQynY%2FbxMPtsPYAIZx1NzBLxT6atZg4e6eKSGtGW5ukGGRooYiIQYCGCMKyOnL0GOqUBR5xD4W9cByzA2ZCmFcSaP3u6SEWlpTIzrk6Vekm%2BemNoKBElI9WJdLg1PIpiR6%2FpFlBY37RqG68lfBY6mhACxc5vZxJw8DMqi%2FU8GD4mbABbbzmlMa6N1MbJSmCnhfdu7hYt7Ndu5Mq77VF6CIWtCG0OYHW4rK3CktZY2tBapIkFgpnPb19cQx2K5ld9zpdCwbSHp0lBoIHFhO%2Fg6GRhXPS0bhae&X-Amz-Signature=cf104a8db9e0a7380babd6c27e8f6a4e4fb269926667091b041f9c502ca71874&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKR53C3A%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCIvHnyM3zIfWzaMHZ%2FeAHfaTaDeoC6YAkgSptZ8ECeIgIhAMZHiBmo%2FXIn7BbDz8SP%2BltUE5Umg1sbWU9rllxgP9HgKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPLKaODEkaWtsIcJgq3AP1OzGlTXTUvdUkWEsItbjPVsLj7tV2H5Ti2mBJE4HXtkKS1PobdOH5ar3giNP4X0HdaUO%2ByUCoQmj2H5vG7WY1Dp7iTI1GkXD3m%2Fjz%2FnZyiWNzaWcGkjLEdcZx5YQg9EnzU4zSWRZygeaAl4fra9uHl8LW6PwJQaxHYYqcbBk8EmWUSNsghuuSFuGfrY9f41V6zUZtEuYUBzMVofQ7ib2fQzrHO6OdqDeoXtimcWgEJaQeoPIqYVCm28EaWkSQoM49Wrbf4LAbh8NOatOpWsv42PbJtgmxDxCfkhAQ4GTtnKqZ00Xf16gTAYz9KzNUoWumqa40EofwutpjG363PrjooG4C3zz5kNdolZfb3JfISI2SON%2F%2BORAsfV1KTqsduEU%2BhjtNURIfurF9gZebHzFV1byOYyO6dvpMmapnpm1WGwXRiw1hGyPIMMagJAuUm2771LnPeAYuToPSy14CQQQH9iyz5q%2FQWPNZvknXq%2BeoGDOjBtjTVDnq%2Bg6yc3K5xwOkQo5iVp9YhB7BLpfixw%2FSxXhUAoQMjNziir04cjyIribNOorkIEA8fCUic7SmFY0BOdY5jrqBukNUVm%2F%2B2GIdVv4TI1Zaj2onA5ewvc55amIzeqgoOIq3yW2XzjDUjpy9BjqkAbRi888X8EDfJGsYE8tiOS73u3%2BZOXoQ%2FtWAA1bALSeTh%2FZuMEbfk0P%2BNtWGd%2BdwRMRH9kD8ZYUilnn3Ub9vfZlaNCnHzxy0I%2Fu0UYIXbliUAZ1g0bpAcc3%2BsJxPN%2Fpq9epoEm9nrKt%2BnAn70uZZV5X1kQwIdh829PXXzvqDcLgURpwth9fy07HTpKTHrPPrJRYQysLfPow3NeDWtl8LjFBFAFj%2B&X-Amz-Signature=6fb3333a14115920adfc100e0db516b0679026462f8957707880acd3c9743a71&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKR53C3A%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCIvHnyM3zIfWzaMHZ%2FeAHfaTaDeoC6YAkgSptZ8ECeIgIhAMZHiBmo%2FXIn7BbDz8SP%2BltUE5Umg1sbWU9rllxgP9HgKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPLKaODEkaWtsIcJgq3AP1OzGlTXTUvdUkWEsItbjPVsLj7tV2H5Ti2mBJE4HXtkKS1PobdOH5ar3giNP4X0HdaUO%2ByUCoQmj2H5vG7WY1Dp7iTI1GkXD3m%2Fjz%2FnZyiWNzaWcGkjLEdcZx5YQg9EnzU4zSWRZygeaAl4fra9uHl8LW6PwJQaxHYYqcbBk8EmWUSNsghuuSFuGfrY9f41V6zUZtEuYUBzMVofQ7ib2fQzrHO6OdqDeoXtimcWgEJaQeoPIqYVCm28EaWkSQoM49Wrbf4LAbh8NOatOpWsv42PbJtgmxDxCfkhAQ4GTtnKqZ00Xf16gTAYz9KzNUoWumqa40EofwutpjG363PrjooG4C3zz5kNdolZfb3JfISI2SON%2F%2BORAsfV1KTqsduEU%2BhjtNURIfurF9gZebHzFV1byOYyO6dvpMmapnpm1WGwXRiw1hGyPIMMagJAuUm2771LnPeAYuToPSy14CQQQH9iyz5q%2FQWPNZvknXq%2BeoGDOjBtjTVDnq%2Bg6yc3K5xwOkQo5iVp9YhB7BLpfixw%2FSxXhUAoQMjNziir04cjyIribNOorkIEA8fCUic7SmFY0BOdY5jrqBukNUVm%2F%2B2GIdVv4TI1Zaj2onA5ewvc55amIzeqgoOIq3yW2XzjDUjpy9BjqkAbRi888X8EDfJGsYE8tiOS73u3%2BZOXoQ%2FtWAA1bALSeTh%2FZuMEbfk0P%2BNtWGd%2BdwRMRH9kD8ZYUilnn3Ub9vfZlaNCnHzxy0I%2Fu0UYIXbliUAZ1g0bpAcc3%2BsJxPN%2Fpq9epoEm9nrKt%2BnAn70uZZV5X1kQwIdh829PXXzvqDcLgURpwth9fy07HTpKTHrPPrJRYQysLfPow3NeDWtl8LjFBFAFj%2B&X-Amz-Signature=b50abf26688ae8a3812fcddd6153eba6856e57f0ea43cc9d6adc12b869a91071&X-Amz-SignedHeaders=host&x-id=GetObject)

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
