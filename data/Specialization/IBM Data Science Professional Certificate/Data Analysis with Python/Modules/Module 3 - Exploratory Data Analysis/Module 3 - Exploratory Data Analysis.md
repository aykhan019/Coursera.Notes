

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEMXFDF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIGaRL8vbFYKkByrV6AG1pI6bojOsD4x6InSColZLPhKcAiAjMsz0wcIwUhkcPvCbbmvHXVqU1FyqOmYnsTOT8f8seyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMti4IIgQkRBDlVbvdKtwDhyM9m8wovyBO3xzTJ5Q6HedZ40yh6fmiVejI2W2esVD5GlFkgTBW6d7Gsq3m0kBeSG3AZ7pS7aIW6vsRL%2Bzeu5zarT%2FqcS4aYgbutazBytwOQjVdUnNEbMZOMtR7kcr%2FkGxwFnGfuhh7p%2BIy%2FXOPCP9WL8rFKOhfo%2FzG4Cw54xKeeSG02OpTlC%2BSPZK2SIzRoC79KVNJ4%2FzVgP4Q3gHQrALATLPvrUILla8ztIk5QuoSNm348WNhTL6iw%2BE7fhOn0EsrCFA%2FTxgLbPN1Gb2CElGF%2B8lgqPGQUgLNpzFa74UKszBPoDV%2FMMck%2FFsKfTpI%2FyP5%2F0nz1lqwpdfa1%2Fl8bPJazQd3qhlpLgwGGp%2BQpxyoVMcfxTZwGXfCJkBJyaaS9Ht8Z%2BAIAnF0Pi8E3wbd0BGsWZbAbagGF4%2BmN6TsS1drb%2Bm%2FK8HnhFh7E5FMEWwA5W0iCIZnw6LNP5PLUXAQcv%2F16dGCFJ6B3i3ux0pp65WHKPJBfu3RpAWNuKksF7xXRySPrxjR%2FisQvsIoZWfkFcD%2BWvc3BFHH9AS5sgsiAJUxFPnTCOVQmogDoirWAmdF%2Fn6L0RxYmCwpsdetNOrd4sUXwFmvXQ2P6RsWv9VwiYnvWRx5mAu9maffVbIwuJDnvAY6pgGMwQaEkzVycCySo8ee39sOj0fsJV6WUJdFwQR%2BNz88kT7TsG8nI8E%2FZPzA4HFAvTPwkSA1QMp0yd04sCxO1M3%2F5e%2FKjZqvZPhx9HmzLXykthJWSGO2G%2FNpNftxH08PPJu%2F22vVSBioDuWE4GDWIPcn6oN%2Bo3w1yuvBgXi3PK60Lp2%2FphMFFMHba6MyTk6H0g2avj%2FJXnsV0niKwaGEOLka46Dy1CTM&X-Amz-Signature=64900631fdd4fa1e6df12263000e69f95f16a2ab9cff13d6023ff118fe1a8456&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEMXFDF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIGaRL8vbFYKkByrV6AG1pI6bojOsD4x6InSColZLPhKcAiAjMsz0wcIwUhkcPvCbbmvHXVqU1FyqOmYnsTOT8f8seyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMti4IIgQkRBDlVbvdKtwDhyM9m8wovyBO3xzTJ5Q6HedZ40yh6fmiVejI2W2esVD5GlFkgTBW6d7Gsq3m0kBeSG3AZ7pS7aIW6vsRL%2Bzeu5zarT%2FqcS4aYgbutazBytwOQjVdUnNEbMZOMtR7kcr%2FkGxwFnGfuhh7p%2BIy%2FXOPCP9WL8rFKOhfo%2FzG4Cw54xKeeSG02OpTlC%2BSPZK2SIzRoC79KVNJ4%2FzVgP4Q3gHQrALATLPvrUILla8ztIk5QuoSNm348WNhTL6iw%2BE7fhOn0EsrCFA%2FTxgLbPN1Gb2CElGF%2B8lgqPGQUgLNpzFa74UKszBPoDV%2FMMck%2FFsKfTpI%2FyP5%2F0nz1lqwpdfa1%2Fl8bPJazQd3qhlpLgwGGp%2BQpxyoVMcfxTZwGXfCJkBJyaaS9Ht8Z%2BAIAnF0Pi8E3wbd0BGsWZbAbagGF4%2BmN6TsS1drb%2Bm%2FK8HnhFh7E5FMEWwA5W0iCIZnw6LNP5PLUXAQcv%2F16dGCFJ6B3i3ux0pp65WHKPJBfu3RpAWNuKksF7xXRySPrxjR%2FisQvsIoZWfkFcD%2BWvc3BFHH9AS5sgsiAJUxFPnTCOVQmogDoirWAmdF%2Fn6L0RxYmCwpsdetNOrd4sUXwFmvXQ2P6RsWv9VwiYnvWRx5mAu9maffVbIwuJDnvAY6pgGMwQaEkzVycCySo8ee39sOj0fsJV6WUJdFwQR%2BNz88kT7TsG8nI8E%2FZPzA4HFAvTPwkSA1QMp0yd04sCxO1M3%2F5e%2FKjZqvZPhx9HmzLXykthJWSGO2G%2FNpNftxH08PPJu%2F22vVSBioDuWE4GDWIPcn6oN%2Bo3w1yuvBgXi3PK60Lp2%2FphMFFMHba6MyTk6H0g2avj%2FJXnsV0niKwaGEOLka46Dy1CTM&X-Amz-Signature=c9919285ccb7d630d64fc3158caadf6f99f9304b48ebf1a81d9e27ef74782223&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FEMXFDF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIGaRL8vbFYKkByrV6AG1pI6bojOsD4x6InSColZLPhKcAiAjMsz0wcIwUhkcPvCbbmvHXVqU1FyqOmYnsTOT8f8seyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMti4IIgQkRBDlVbvdKtwDhyM9m8wovyBO3xzTJ5Q6HedZ40yh6fmiVejI2W2esVD5GlFkgTBW6d7Gsq3m0kBeSG3AZ7pS7aIW6vsRL%2Bzeu5zarT%2FqcS4aYgbutazBytwOQjVdUnNEbMZOMtR7kcr%2FkGxwFnGfuhh7p%2BIy%2FXOPCP9WL8rFKOhfo%2FzG4Cw54xKeeSG02OpTlC%2BSPZK2SIzRoC79KVNJ4%2FzVgP4Q3gHQrALATLPvrUILla8ztIk5QuoSNm348WNhTL6iw%2BE7fhOn0EsrCFA%2FTxgLbPN1Gb2CElGF%2B8lgqPGQUgLNpzFa74UKszBPoDV%2FMMck%2FFsKfTpI%2FyP5%2F0nz1lqwpdfa1%2Fl8bPJazQd3qhlpLgwGGp%2BQpxyoVMcfxTZwGXfCJkBJyaaS9Ht8Z%2BAIAnF0Pi8E3wbd0BGsWZbAbagGF4%2BmN6TsS1drb%2Bm%2FK8HnhFh7E5FMEWwA5W0iCIZnw6LNP5PLUXAQcv%2F16dGCFJ6B3i3ux0pp65WHKPJBfu3RpAWNuKksF7xXRySPrxjR%2FisQvsIoZWfkFcD%2BWvc3BFHH9AS5sgsiAJUxFPnTCOVQmogDoirWAmdF%2Fn6L0RxYmCwpsdetNOrd4sUXwFmvXQ2P6RsWv9VwiYnvWRx5mAu9maffVbIwuJDnvAY6pgGMwQaEkzVycCySo8ee39sOj0fsJV6WUJdFwQR%2BNz88kT7TsG8nI8E%2FZPzA4HFAvTPwkSA1QMp0yd04sCxO1M3%2F5e%2FKjZqvZPhx9HmzLXykthJWSGO2G%2FNpNftxH08PPJu%2F22vVSBioDuWE4GDWIPcn6oN%2Bo3w1yuvBgXi3PK60Lp2%2FphMFFMHba6MyTk6H0g2avj%2FJXnsV0niKwaGEOLka46Dy1CTM&X-Amz-Signature=e038bbde6d0db71aa22147ae1652989e0d15f341cd20c87d06052978e73d2906&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6JJ4KI3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDq%2FAoJtGM%2FmS00SJADLTv%2BwPltsn6U0K5uU%2BU0BRFjjAIhALwmutQ5mUf35SsoNv9BCFNqrgYtagxyVbgxN9N8MwAnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPU3Pu7NBZ8shuSM4q3ANgE6wMLTr%2BOrilUISVEIebLl95uOZGCxxvQwvaX2K0kzHRjhC7P9v%2BNy0QbfDYlVpr0Yk68dyMSDWqsSohzdQs2aSsmju1PlNTcFUmydF6f0R6T%2FYzkPBVQ2ILNVYhkl5pEJ0eagqz32Vx76%2F1E%2FPXQdmCde0xw%2BKqrIYItxuDwH%2F1Sbmg19ySvUz0NhaXbKyoLjxBb0QuleSGWcXLarRqUaA9Q4ThmTVvh5fWZIXUBA9K%2F%2FPPDsRKmrL753s%2Fx%2BIcT6WmVkDx6KP41q9%2BOlyfSPjhxkK%2Fdm7sEDqTbrIQ%2BbDyvSLiG5xOzBaZOVlAkyi5Lhnso%2BCBelEBkNIDtVoTz5PC7Wka1m%2Fz0SdvWLO6VdIgOvhxjuvbNUebwWS36UbtDUSDIZWdqlzcLw2mG%2Bm20hn5cRvcFVdqbomfCQfq6Gi0m0XFJ29GpoWgy7zDFHAif99vZ6szFag5xzzXtbGZ3g2qJJAOPMr4p4G2BHz3CWPyYZPJl%2FQy5m5xnTVKbhvLkqqTWnQjLy1LNLnXAu%2BZ7AzfGIzpd9QW8wjjfmCTHLg%2BfiGs7ypQ8MZVUMx%2BAiU08ONgr3ASoHhtzhUf63KP7TpnmuaqLJ17DtT1plLye2Jf9SwJC1uFmUdSZDD5j%2Be8BjqkAbd1BmJzwTdmxVl1hXeGfmctt1aQjCVoKzc4QXbM8jJbUM7LNb%2FYpwTf1zsxiZvx0yVZ7SBILEyTxXDhIYv8JTH1iQKaxLF5ySIqQjQ3z6azxmEGW2xzFv382a%2BC4pCvs90WMBQKVJ%2FbW6SYwBGistjsKRbRvpRXDOx5Ysd95d0CDOlzf3dCMA4ypG6Wb74XYWRy7oGBZE60z3JtlIeLjXs3hU4I&X-Amz-Signature=850c987366ef5d29a78e010cbc60e9827d27b2b5530b54c281e406918d52d9f8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6JJ4KI3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDq%2FAoJtGM%2FmS00SJADLTv%2BwPltsn6U0K5uU%2BU0BRFjjAIhALwmutQ5mUf35SsoNv9BCFNqrgYtagxyVbgxN9N8MwAnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPU3Pu7NBZ8shuSM4q3ANgE6wMLTr%2BOrilUISVEIebLl95uOZGCxxvQwvaX2K0kzHRjhC7P9v%2BNy0QbfDYlVpr0Yk68dyMSDWqsSohzdQs2aSsmju1PlNTcFUmydF6f0R6T%2FYzkPBVQ2ILNVYhkl5pEJ0eagqz32Vx76%2F1E%2FPXQdmCde0xw%2BKqrIYItxuDwH%2F1Sbmg19ySvUz0NhaXbKyoLjxBb0QuleSGWcXLarRqUaA9Q4ThmTVvh5fWZIXUBA9K%2F%2FPPDsRKmrL753s%2Fx%2BIcT6WmVkDx6KP41q9%2BOlyfSPjhxkK%2Fdm7sEDqTbrIQ%2BbDyvSLiG5xOzBaZOVlAkyi5Lhnso%2BCBelEBkNIDtVoTz5PC7Wka1m%2Fz0SdvWLO6VdIgOvhxjuvbNUebwWS36UbtDUSDIZWdqlzcLw2mG%2Bm20hn5cRvcFVdqbomfCQfq6Gi0m0XFJ29GpoWgy7zDFHAif99vZ6szFag5xzzXtbGZ3g2qJJAOPMr4p4G2BHz3CWPyYZPJl%2FQy5m5xnTVKbhvLkqqTWnQjLy1LNLnXAu%2BZ7AzfGIzpd9QW8wjjfmCTHLg%2BfiGs7ypQ8MZVUMx%2BAiU08ONgr3ASoHhtzhUf63KP7TpnmuaqLJ17DtT1plLye2Jf9SwJC1uFmUdSZDD5j%2Be8BjqkAbd1BmJzwTdmxVl1hXeGfmctt1aQjCVoKzc4QXbM8jJbUM7LNb%2FYpwTf1zsxiZvx0yVZ7SBILEyTxXDhIYv8JTH1iQKaxLF5ySIqQjQ3z6azxmEGW2xzFv382a%2BC4pCvs90WMBQKVJ%2FbW6SYwBGistjsKRbRvpRXDOx5Ysd95d0CDOlzf3dCMA4ypG6Wb74XYWRy7oGBZE60z3JtlIeLjXs3hU4I&X-Amz-Signature=a757fcf8e4ac0ea2987b1e33279d77ac428abb9785cf5bd747244f3d82b8537d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6JJ4KI3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDq%2FAoJtGM%2FmS00SJADLTv%2BwPltsn6U0K5uU%2BU0BRFjjAIhALwmutQ5mUf35SsoNv9BCFNqrgYtagxyVbgxN9N8MwAnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPU3Pu7NBZ8shuSM4q3ANgE6wMLTr%2BOrilUISVEIebLl95uOZGCxxvQwvaX2K0kzHRjhC7P9v%2BNy0QbfDYlVpr0Yk68dyMSDWqsSohzdQs2aSsmju1PlNTcFUmydF6f0R6T%2FYzkPBVQ2ILNVYhkl5pEJ0eagqz32Vx76%2F1E%2FPXQdmCde0xw%2BKqrIYItxuDwH%2F1Sbmg19ySvUz0NhaXbKyoLjxBb0QuleSGWcXLarRqUaA9Q4ThmTVvh5fWZIXUBA9K%2F%2FPPDsRKmrL753s%2Fx%2BIcT6WmVkDx6KP41q9%2BOlyfSPjhxkK%2Fdm7sEDqTbrIQ%2BbDyvSLiG5xOzBaZOVlAkyi5Lhnso%2BCBelEBkNIDtVoTz5PC7Wka1m%2Fz0SdvWLO6VdIgOvhxjuvbNUebwWS36UbtDUSDIZWdqlzcLw2mG%2Bm20hn5cRvcFVdqbomfCQfq6Gi0m0XFJ29GpoWgy7zDFHAif99vZ6szFag5xzzXtbGZ3g2qJJAOPMr4p4G2BHz3CWPyYZPJl%2FQy5m5xnTVKbhvLkqqTWnQjLy1LNLnXAu%2BZ7AzfGIzpd9QW8wjjfmCTHLg%2BfiGs7ypQ8MZVUMx%2BAiU08ONgr3ASoHhtzhUf63KP7TpnmuaqLJ17DtT1plLye2Jf9SwJC1uFmUdSZDD5j%2Be8BjqkAbd1BmJzwTdmxVl1hXeGfmctt1aQjCVoKzc4QXbM8jJbUM7LNb%2FYpwTf1zsxiZvx0yVZ7SBILEyTxXDhIYv8JTH1iQKaxLF5ySIqQjQ3z6azxmEGW2xzFv382a%2BC4pCvs90WMBQKVJ%2FbW6SYwBGistjsKRbRvpRXDOx5Ysd95d0CDOlzf3dCMA4ypG6Wb74XYWRy7oGBZE60z3JtlIeLjXs3hU4I&X-Amz-Signature=be2f35327ccc4195663ab9c453cd0afcd1e5f27951831400424befa92bc0cdb9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6JJ4KI3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDq%2FAoJtGM%2FmS00SJADLTv%2BwPltsn6U0K5uU%2BU0BRFjjAIhALwmutQ5mUf35SsoNv9BCFNqrgYtagxyVbgxN9N8MwAnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPU3Pu7NBZ8shuSM4q3ANgE6wMLTr%2BOrilUISVEIebLl95uOZGCxxvQwvaX2K0kzHRjhC7P9v%2BNy0QbfDYlVpr0Yk68dyMSDWqsSohzdQs2aSsmju1PlNTcFUmydF6f0R6T%2FYzkPBVQ2ILNVYhkl5pEJ0eagqz32Vx76%2F1E%2FPXQdmCde0xw%2BKqrIYItxuDwH%2F1Sbmg19ySvUz0NhaXbKyoLjxBb0QuleSGWcXLarRqUaA9Q4ThmTVvh5fWZIXUBA9K%2F%2FPPDsRKmrL753s%2Fx%2BIcT6WmVkDx6KP41q9%2BOlyfSPjhxkK%2Fdm7sEDqTbrIQ%2BbDyvSLiG5xOzBaZOVlAkyi5Lhnso%2BCBelEBkNIDtVoTz5PC7Wka1m%2Fz0SdvWLO6VdIgOvhxjuvbNUebwWS36UbtDUSDIZWdqlzcLw2mG%2Bm20hn5cRvcFVdqbomfCQfq6Gi0m0XFJ29GpoWgy7zDFHAif99vZ6szFag5xzzXtbGZ3g2qJJAOPMr4p4G2BHz3CWPyYZPJl%2FQy5m5xnTVKbhvLkqqTWnQjLy1LNLnXAu%2BZ7AzfGIzpd9QW8wjjfmCTHLg%2BfiGs7ypQ8MZVUMx%2BAiU08ONgr3ASoHhtzhUf63KP7TpnmuaqLJ17DtT1plLye2Jf9SwJC1uFmUdSZDD5j%2Be8BjqkAbd1BmJzwTdmxVl1hXeGfmctt1aQjCVoKzc4QXbM8jJbUM7LNb%2FYpwTf1zsxiZvx0yVZ7SBILEyTxXDhIYv8JTH1iQKaxLF5ySIqQjQ3z6azxmEGW2xzFv382a%2BC4pCvs90WMBQKVJ%2FbW6SYwBGistjsKRbRvpRXDOx5Ysd95d0CDOlzf3dCMA4ypG6Wb74XYWRy7oGBZE60z3JtlIeLjXs3hU4I&X-Amz-Signature=695deff58177a4517d730a91d771962f90882e8281009450b33acf0b63dee4ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6JJ4KI3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDq%2FAoJtGM%2FmS00SJADLTv%2BwPltsn6U0K5uU%2BU0BRFjjAIhALwmutQ5mUf35SsoNv9BCFNqrgYtagxyVbgxN9N8MwAnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPU3Pu7NBZ8shuSM4q3ANgE6wMLTr%2BOrilUISVEIebLl95uOZGCxxvQwvaX2K0kzHRjhC7P9v%2BNy0QbfDYlVpr0Yk68dyMSDWqsSohzdQs2aSsmju1PlNTcFUmydF6f0R6T%2FYzkPBVQ2ILNVYhkl5pEJ0eagqz32Vx76%2F1E%2FPXQdmCde0xw%2BKqrIYItxuDwH%2F1Sbmg19ySvUz0NhaXbKyoLjxBb0QuleSGWcXLarRqUaA9Q4ThmTVvh5fWZIXUBA9K%2F%2FPPDsRKmrL753s%2Fx%2BIcT6WmVkDx6KP41q9%2BOlyfSPjhxkK%2Fdm7sEDqTbrIQ%2BbDyvSLiG5xOzBaZOVlAkyi5Lhnso%2BCBelEBkNIDtVoTz5PC7Wka1m%2Fz0SdvWLO6VdIgOvhxjuvbNUebwWS36UbtDUSDIZWdqlzcLw2mG%2Bm20hn5cRvcFVdqbomfCQfq6Gi0m0XFJ29GpoWgy7zDFHAif99vZ6szFag5xzzXtbGZ3g2qJJAOPMr4p4G2BHz3CWPyYZPJl%2FQy5m5xnTVKbhvLkqqTWnQjLy1LNLnXAu%2BZ7AzfGIzpd9QW8wjjfmCTHLg%2BfiGs7ypQ8MZVUMx%2BAiU08ONgr3ASoHhtzhUf63KP7TpnmuaqLJ17DtT1plLye2Jf9SwJC1uFmUdSZDD5j%2Be8BjqkAbd1BmJzwTdmxVl1hXeGfmctt1aQjCVoKzc4QXbM8jJbUM7LNb%2FYpwTf1zsxiZvx0yVZ7SBILEyTxXDhIYv8JTH1iQKaxLF5ySIqQjQ3z6azxmEGW2xzFv382a%2BC4pCvs90WMBQKVJ%2FbW6SYwBGistjsKRbRvpRXDOx5Ysd95d0CDOlzf3dCMA4ypG6Wb74XYWRy7oGBZE60z3JtlIeLjXs3hU4I&X-Amz-Signature=dcbfb61ee7405e3e9775593e87c09603326d3bd34b5407b93b455beb663c4a80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6JJ4KI3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDq%2FAoJtGM%2FmS00SJADLTv%2BwPltsn6U0K5uU%2BU0BRFjjAIhALwmutQ5mUf35SsoNv9BCFNqrgYtagxyVbgxN9N8MwAnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPU3Pu7NBZ8shuSM4q3ANgE6wMLTr%2BOrilUISVEIebLl95uOZGCxxvQwvaX2K0kzHRjhC7P9v%2BNy0QbfDYlVpr0Yk68dyMSDWqsSohzdQs2aSsmju1PlNTcFUmydF6f0R6T%2FYzkPBVQ2ILNVYhkl5pEJ0eagqz32Vx76%2F1E%2FPXQdmCde0xw%2BKqrIYItxuDwH%2F1Sbmg19ySvUz0NhaXbKyoLjxBb0QuleSGWcXLarRqUaA9Q4ThmTVvh5fWZIXUBA9K%2F%2FPPDsRKmrL753s%2Fx%2BIcT6WmVkDx6KP41q9%2BOlyfSPjhxkK%2Fdm7sEDqTbrIQ%2BbDyvSLiG5xOzBaZOVlAkyi5Lhnso%2BCBelEBkNIDtVoTz5PC7Wka1m%2Fz0SdvWLO6VdIgOvhxjuvbNUebwWS36UbtDUSDIZWdqlzcLw2mG%2Bm20hn5cRvcFVdqbomfCQfq6Gi0m0XFJ29GpoWgy7zDFHAif99vZ6szFag5xzzXtbGZ3g2qJJAOPMr4p4G2BHz3CWPyYZPJl%2FQy5m5xnTVKbhvLkqqTWnQjLy1LNLnXAu%2BZ7AzfGIzpd9QW8wjjfmCTHLg%2BfiGs7ypQ8MZVUMx%2BAiU08ONgr3ASoHhtzhUf63KP7TpnmuaqLJ17DtT1plLye2Jf9SwJC1uFmUdSZDD5j%2Be8BjqkAbd1BmJzwTdmxVl1hXeGfmctt1aQjCVoKzc4QXbM8jJbUM7LNb%2FYpwTf1zsxiZvx0yVZ7SBILEyTxXDhIYv8JTH1iQKaxLF5ySIqQjQ3z6azxmEGW2xzFv382a%2BC4pCvs90WMBQKVJ%2FbW6SYwBGistjsKRbRvpRXDOx5Ysd95d0CDOlzf3dCMA4ypG6Wb74XYWRy7oGBZE60z3JtlIeLjXs3hU4I&X-Amz-Signature=39f65dbcacacc8fc975fd8c6661ccf31a49f19e7c8380774f87972332d02fe8d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLZ756HL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBIM69gD5ee%2F82SN4dYfbWrctHQKy7S1mCOTUr3HGwN5AiEAtbKhmm9SJZCLrCyQz%2FTN6bo4l%2FVS5drbMS6qHuGB1P8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIWzS4ykQ2ORrBblGCrcA5IUQzGr5mjvqwpsH%2FsDM5Wdc60qyL8SB5qHkHjEnhvs4%2BVh0hc9IUh122bt7AgYj2l467pOUxjJx6deeNskfUl4zkTnYjOIRhx%2FBfHJlciI09KYso7uj0CPX9Dpcveg8lFdKjbatooCpShp8s79ZPYT2RsLQLG5rMELHnKtGH97wU2jZkR7FMXUp6OAq8rkWa1ydYHRP4YqAd7GQw1XdT8Akt0p72WAmPlV9iM%2FtGdKUk%2FfEfP8wngTM6pRWzu1vCINNTuHOOTaEXf9QsUbLvrlZUIzer%2FUnTC540cTtYibyi%2F%2FR99Un0fTTqZwQ3LU0gfwYGtjYtEzlQdFEIzzV5LHAN%2FzqOFVSOsvALbfCxe4V%2B8U6%2F520s7KV5fUjGPu9FQieiGGmQqyc5c%2Fl6QCTOfNh2A39Yn2TMvfleHA3waRgHLcxPAph2K6UO9I3DWuX70nabmkW26U78f4txwZCpZVdODpbu%2FXI4o3gTSAQ1HsbKeZZNRSyJX713SwmZ%2FG8hx0TJNotmdakMM1F7Z5QrrGssUfaSGo6XCEvwXS%2F%2FJ98pSMC45Az76Z302BehMVUr10WUh5Vn%2Fl246OBIUic%2FONZV%2Fgbc7z3W2Vzuh6ZFQllgoCAiMP1nf7c8qEMLmQ57wGOqUBi2zhFpqaWTaC1dAPtT31b0Zu9GZch%2BW%2BfOtFJJW2WTaid%2BsECqbjpVgAAn%2FZujq%2FJFYCtzBM7IxwCF26B381ezbUKin0v5VtSgB1e%2FIlFwEy9c834vR3wjUNqpMHJbkWG5prlk4zNy2dApX7KukX%2Bq8StXWBbp0LH%2FwLHqsjoti4mbdXme%2F%2BqNRr4l3P0ayIw%2B6BZ%2FuVj1Cir34J%2B8Q5S7uuObje&X-Amz-Signature=c641c036bcef89d7846c8e7d60a8a8d74fbe1ce5be962e94b153aef36565bc4f&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPWWBFCD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQCRN3FQ1d11OFvC2UNsPsYGY%2FKKyoemMwPy40D%2Fj18fTwIhAM04gbpf%2Bk%2B2iI7pPR57OKjQ7j8MaNiK2y48Tww1VdGlKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOiEpVS8H4pX2S%2FU4q3AMuWWuOQHiDrrDDZftD9BbvzNSUuDA9ycw%2BKKgtnyiNhI7iy%2FO5cEo%2BS%2FJ71ziyX4dZj%2FHPW8aH0nf3iDYjiFjaQeKMfMn6pX2EX4WIB8fa4JfFceaIL9SwVRQcAGxBD2CjSX0u55hO9lguHoKtfWPdcBHaTY6wO%2Fi9kYfwnoOgMI08C2zstwcX2IX5k%2BWURXChk7PiPsCNMuQuYZ0PGokfBvRpIDRiUOVBuIVYstuys%2B5WvcnE%2BdYsY8UaTyr%2F2oAFh%2BomuR%2Bd2ZkCfrLR4Wt4AM%2F%2FPyr0LbPxIt%2BDjCmswio9S9hhtexv0esKfiM4uIRQCK2UtabXUg%2Ft35EbtxYqWywOnVS0%2BqSl04Q9qOY6bfo8TLPwJ4mZOw1FVkloliHoNNkujnLk%2FJ2sRd4QEJ5gO%2FFw6k5AHikzbtUj6MDPXDeYnTomE1o4IARLVHe655Zr9hP%2Fi0Pm4%2FluRrcAeDTgaoukQAD9fvk6qVbT%2FQNl3Sg4cRjadzHk35OqahnMbts%2BOKA%2BrAOG0jc2U1UgYuN2vUPBCVfXflza8MsjJk9FCWwRcxwz8nGXc3qIdApgwvUe%2FeeFeWqL9MBj%2BVeWI7uVFzMMqBfHukSE00RKzV66KiIxflXjlCdLA%2Bbs2TDvkOe8BjqkAZGqBQudL4hPUz06qkMvzOUDgNksxfpwFTRTGaOOKki9OovMysqAIx7RDyvmDoGO6bbq0pDJA6sksnjXFNmni7QM0yxdcU2tAXwH%2B9V7Ji3x5fASERkQyws1FutDhg8WBLcKSc96ehLq070C%2BwWAKGGUrEh89AXo8YDUM%2BMSdAUoI1Zl%2Fjpk03IiMAoq09t%2BWepxfsNPTffNB4QwxLQ8jikDc3m1&X-Amz-Signature=60373dc287c5da78d1e68fc5d9cf867b605f81168b30c25a32c1bce93f9a5eb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6JJ4KI3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDq%2FAoJtGM%2FmS00SJADLTv%2BwPltsn6U0K5uU%2BU0BRFjjAIhALwmutQ5mUf35SsoNv9BCFNqrgYtagxyVbgxN9N8MwAnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPU3Pu7NBZ8shuSM4q3ANgE6wMLTr%2BOrilUISVEIebLl95uOZGCxxvQwvaX2K0kzHRjhC7P9v%2BNy0QbfDYlVpr0Yk68dyMSDWqsSohzdQs2aSsmju1PlNTcFUmydF6f0R6T%2FYzkPBVQ2ILNVYhkl5pEJ0eagqz32Vx76%2F1E%2FPXQdmCde0xw%2BKqrIYItxuDwH%2F1Sbmg19ySvUz0NhaXbKyoLjxBb0QuleSGWcXLarRqUaA9Q4ThmTVvh5fWZIXUBA9K%2F%2FPPDsRKmrL753s%2Fx%2BIcT6WmVkDx6KP41q9%2BOlyfSPjhxkK%2Fdm7sEDqTbrIQ%2BbDyvSLiG5xOzBaZOVlAkyi5Lhnso%2BCBelEBkNIDtVoTz5PC7Wka1m%2Fz0SdvWLO6VdIgOvhxjuvbNUebwWS36UbtDUSDIZWdqlzcLw2mG%2Bm20hn5cRvcFVdqbomfCQfq6Gi0m0XFJ29GpoWgy7zDFHAif99vZ6szFag5xzzXtbGZ3g2qJJAOPMr4p4G2BHz3CWPyYZPJl%2FQy5m5xnTVKbhvLkqqTWnQjLy1LNLnXAu%2BZ7AzfGIzpd9QW8wjjfmCTHLg%2BfiGs7ypQ8MZVUMx%2BAiU08ONgr3ASoHhtzhUf63KP7TpnmuaqLJ17DtT1plLye2Jf9SwJC1uFmUdSZDD5j%2Be8BjqkAbd1BmJzwTdmxVl1hXeGfmctt1aQjCVoKzc4QXbM8jJbUM7LNb%2FYpwTf1zsxiZvx0yVZ7SBILEyTxXDhIYv8JTH1iQKaxLF5ySIqQjQ3z6azxmEGW2xzFv382a%2BC4pCvs90WMBQKVJ%2FbW6SYwBGistjsKRbRvpRXDOx5Ysd95d0CDOlzf3dCMA4ypG6Wb74XYWRy7oGBZE60z3JtlIeLjXs3hU4I&X-Amz-Signature=695576290f3334b6ff374428d85ccb076c9ae30a524d9ea0b9ebf154f139704b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6JJ4KI3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDq%2FAoJtGM%2FmS00SJADLTv%2BwPltsn6U0K5uU%2BU0BRFjjAIhALwmutQ5mUf35SsoNv9BCFNqrgYtagxyVbgxN9N8MwAnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPU3Pu7NBZ8shuSM4q3ANgE6wMLTr%2BOrilUISVEIebLl95uOZGCxxvQwvaX2K0kzHRjhC7P9v%2BNy0QbfDYlVpr0Yk68dyMSDWqsSohzdQs2aSsmju1PlNTcFUmydF6f0R6T%2FYzkPBVQ2ILNVYhkl5pEJ0eagqz32Vx76%2F1E%2FPXQdmCde0xw%2BKqrIYItxuDwH%2F1Sbmg19ySvUz0NhaXbKyoLjxBb0QuleSGWcXLarRqUaA9Q4ThmTVvh5fWZIXUBA9K%2F%2FPPDsRKmrL753s%2Fx%2BIcT6WmVkDx6KP41q9%2BOlyfSPjhxkK%2Fdm7sEDqTbrIQ%2BbDyvSLiG5xOzBaZOVlAkyi5Lhnso%2BCBelEBkNIDtVoTz5PC7Wka1m%2Fz0SdvWLO6VdIgOvhxjuvbNUebwWS36UbtDUSDIZWdqlzcLw2mG%2Bm20hn5cRvcFVdqbomfCQfq6Gi0m0XFJ29GpoWgy7zDFHAif99vZ6szFag5xzzXtbGZ3g2qJJAOPMr4p4G2BHz3CWPyYZPJl%2FQy5m5xnTVKbhvLkqqTWnQjLy1LNLnXAu%2BZ7AzfGIzpd9QW8wjjfmCTHLg%2BfiGs7ypQ8MZVUMx%2BAiU08ONgr3ASoHhtzhUf63KP7TpnmuaqLJ17DtT1plLye2Jf9SwJC1uFmUdSZDD5j%2Be8BjqkAbd1BmJzwTdmxVl1hXeGfmctt1aQjCVoKzc4QXbM8jJbUM7LNb%2FYpwTf1zsxiZvx0yVZ7SBILEyTxXDhIYv8JTH1iQKaxLF5ySIqQjQ3z6azxmEGW2xzFv382a%2BC4pCvs90WMBQKVJ%2FbW6SYwBGistjsKRbRvpRXDOx5Ysd95d0CDOlzf3dCMA4ypG6Wb74XYWRy7oGBZE60z3JtlIeLjXs3hU4I&X-Amz-Signature=1c63a409d5870a49e933f75d8f5c7bdfe998d5761e78bf0ceb3af8831a167b71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6JJ4KI3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDq%2FAoJtGM%2FmS00SJADLTv%2BwPltsn6U0K5uU%2BU0BRFjjAIhALwmutQ5mUf35SsoNv9BCFNqrgYtagxyVbgxN9N8MwAnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPU3Pu7NBZ8shuSM4q3ANgE6wMLTr%2BOrilUISVEIebLl95uOZGCxxvQwvaX2K0kzHRjhC7P9v%2BNy0QbfDYlVpr0Yk68dyMSDWqsSohzdQs2aSsmju1PlNTcFUmydF6f0R6T%2FYzkPBVQ2ILNVYhkl5pEJ0eagqz32Vx76%2F1E%2FPXQdmCde0xw%2BKqrIYItxuDwH%2F1Sbmg19ySvUz0NhaXbKyoLjxBb0QuleSGWcXLarRqUaA9Q4ThmTVvh5fWZIXUBA9K%2F%2FPPDsRKmrL753s%2Fx%2BIcT6WmVkDx6KP41q9%2BOlyfSPjhxkK%2Fdm7sEDqTbrIQ%2BbDyvSLiG5xOzBaZOVlAkyi5Lhnso%2BCBelEBkNIDtVoTz5PC7Wka1m%2Fz0SdvWLO6VdIgOvhxjuvbNUebwWS36UbtDUSDIZWdqlzcLw2mG%2Bm20hn5cRvcFVdqbomfCQfq6Gi0m0XFJ29GpoWgy7zDFHAif99vZ6szFag5xzzXtbGZ3g2qJJAOPMr4p4G2BHz3CWPyYZPJl%2FQy5m5xnTVKbhvLkqqTWnQjLy1LNLnXAu%2BZ7AzfGIzpd9QW8wjjfmCTHLg%2BfiGs7ypQ8MZVUMx%2BAiU08ONgr3ASoHhtzhUf63KP7TpnmuaqLJ17DtT1plLye2Jf9SwJC1uFmUdSZDD5j%2Be8BjqkAbd1BmJzwTdmxVl1hXeGfmctt1aQjCVoKzc4QXbM8jJbUM7LNb%2FYpwTf1zsxiZvx0yVZ7SBILEyTxXDhIYv8JTH1iQKaxLF5ySIqQjQ3z6azxmEGW2xzFv382a%2BC4pCvs90WMBQKVJ%2FbW6SYwBGistjsKRbRvpRXDOx5Ysd95d0CDOlzf3dCMA4ypG6Wb74XYWRy7oGBZE60z3JtlIeLjXs3hU4I&X-Amz-Signature=0889e72153a03a45cd0b9916dedef8c814dc770cf37ea7d455859c71e09b9377&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGMI6PSB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIHyxeLp32iu1woM0vE6jPxSOhKMDJSCxEiSkPKFjFw9oAiBQ2PCVHyyZjjza4YXAH9opzjXxIexvOd6kLidc7DQfmSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQyff6JeOg0ueOITUKtwDxntA2wOpDYD2BcvQg4ZCmFHxrP9GrKus0GDX9kb0q4wx%2BX2eaPeQUq1fe6Xw7GqNZRNyzextnTG%2F%2BnPMXguV%2BQhk7%2BWHieFKJ5PLayj8eR4NbpEhNjQQZHpFLQSOLyowAt15IrS3wyqG8Xe39hoZ9cQSZbZB3TY2KptU52HbzF5ezb9QegMmAchL3p1sixZvCUrlZCwLACWSVwwdBhGQOmkCSc%2B%2BbuPU0iSJ%2FWjCEAc5MgC3LTPajiDaLyfqiAlwOvvtZ1HX9PGjN%2F8hOwUsIO85aMGcJ9UVM5OdwzJJM9XYLJhc%2BWlYxQr898%2FD4tx8zPDI%2FdQFNOnru27H6T%2FMRyzJqZpx5nSWh8QWExHh1%2BD4Ab223S4e9vzZgaUBHUQc6OE%2B5ulTlocbcT5Pjlv%2FNIFupmQ6p1%2F9bzqZqqDcxFQWMWZSdNFPPgivAD4l2P1XgtftutwoeJO5mB9T09SQh63Kh2Yq7xCt%2Bv43qiKuDebNR4W5218FEaV0mR%2FgyIypYRCcgz7wfLcS34Ms6rvYM4KpO%2B7fwHIMAfKPID2TWDubqye%2FLk6by%2BEm3Ejjb9VeJivItccg8ZWZt%2Bc%2F43mPziFC1rWRKaYMmHlqCBdMgPlGMgUFILVSuqBa0YIwmJDnvAY6pgEeIaGQ3W3uYYSM6sPfokcrVTTbYPzC4Tp5csNOYWlQ5SvN0mxs8TPxqgf6TmLT8IjadV9uhI4rMPi5fcSCRRwAtuLQgxAolvIQJ%2FzSlvT%2FgmxvkI5dQAA9aQDQX0smU8O5dD0hCCKBI7SoKZImoWw%2BtmWoEQjKtoO2KeACNwHHDWkuWlKL2CHCvsIdAjZDb%2B3nCoeEctgcdPR6i9%2FtQxjzm86P2ZXc&X-Amz-Signature=33ab20eadbbecb127630ccd38349e53d7c4bd26e3fa64c1801b3d8b5535f2d0a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHQGDYTT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQDjkE19Hlw%2FcD7OxnJ7bourb3kCY8PSUeA7HhZdBcW5XgIgImtrNe7fJeU02444Wejsydsk%2B0A281E2qTsEbYdotRoqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNUYaN29n5wjeVdFHircAxfBc49abEHM56ENe0F3ACkEcm5a1WJ1Jnry1HjeSwxvJ69QXo0sRz9Z58L38RxGAHd%2BD4WjKMx9wBIudp0RnTiEeFfJ7XVh9QTV3GGz6xw46IsYSU6bSW%2BQbwX90FL7gvEzbAUxPjH6mgPAepUxuwEzrEStCn7F5ynfPTX4OSUrCNrvR6qPu2P99B9t0CBYEB60nlmzWIEi49%2BuVWwuluX67jbs5PU6MlZ8skgHNv%2FO5hsTRoyaTIuWnNWjNYqC%2B5SA5qATN35L4SEKlMQvauR7xqOG1cvMaDl6hs23CUzi6vORxqUvp1BkTVSHAS0lxXoOzKuJEGNGnn0XkYmVlIUoepCJ7bWbsXzYgW%2FwT9WWqqSjHyF2zTZ8iH4UdCAkcL27McUbV5P5jG5glW%2FWtzZHPKntqSxs3Vv0I4WVarJj1LS%2F30lEfaUTB57WBYrobT8OgNG0Zl2UiEhouJ6dutBsOebCdMxkm7F5qQJ0%2BKVP%2BhybTsuZXAmrcApz91hNABKgC0EEtuA4jnG12GQ3GYJ6iddD0uh4okbJbLXiJw2Ckj7b5Wp4DwFPbFMEPkrOzxCwP9AbgFLBGJo7jt390MNLee6yyvqQL2UKspfk6%2FMmCSLJ8CAvGnweELaaMNKQ57wGOqUBue95Cih%2FtH6RMTsZ2wwZe75GGQDPfocnyhqdGomRnkpRzyn80UacWiei%2Fez8zrhlgp%2BXpEjHXx4nDv5xhBILtK2nThp0tdx7ZDK70%2F8EVkudk1FgiJCbW57czJ4i0Xb7BhwYceWyalXNEWTpkekmdzC%2FTeMMNxcGFVupfR%2BBoFfN2qYDgRzPrBofcc0sPPLB1paJtYX6cDDfSjnEVSOxie89Q3ce&X-Amz-Signature=9c508d3f50e2c93e2d76b6a74f54fa8b8bbe81753365f5ed8df23f5460ed0ba9&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW4JGEGE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIDr9p7x3NFaKWqFVGD%2BxFZNznOHFHQRF9Lbl3YGl12U5AiEA%2BX6LIveKprZNc2P%2F1yQoy9ZxDomykM%2Fajd9SiR213I8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJfUMY9%2FsSRMmFokYSrcA2HnaKCl%2FwwridQfry%2FNRKU3KKUFqFMkUmSkZy0YAOsluTFC6VNkXH0maZME2CXRUsJISfei1LhWFEL8NhndPfGKcRJiRNqb69o%2BnNLlPdAUKW6nlmk9R7zIUewdLE658XN3PbN5ZSzBBVihRPIpc70Ju6AuXwG90HHPANWT5QcoyFWQuZz%2Fv9NPqQJtOMWGJBIlaDn%2BvF6ImB6mbs0aU9K9U4f%2BjDLGi%2BNhMzqTI1%2BvTNaKfPiV3Pj%2B95paxQi4nNd099qer03H%2FGusA%2BfTjH10DFneFPq%2FnDPevF9HnwFzz35RpgOFwGKAaQL%2FG4CHdhJxSrNuzqYDcl3Y2NrOPsfvhWJ8mAoxa0Rlfg%2FoaCiHbcmyatJVHa%2B%2BJm9VdS8GiUaJH1oBWGyW%2FxTGf7CaG5FYIN9VMVwUpnHL8BtI%2BAvfKkopkpCdbBiswdKG3RKhleDOME5A%2BcTy80%2FuO3jhBxNEOWP5SjbVa3XmecEJ7MZM8jIi9dMJ%2BDVoodfKWoSCQfv%2FScn0sdUXNy2Ya7%2FaIPNIutAPfqnQJJrucEOj5FWZGkKT3W33m7PtuJVqE3UNVIpAYRDkKTbmsEvdUy%2BxyHG2TeSaKdDUiSb68eLl5RlDA9X40o7sED0Wq8iLMMqQ57wGOqUBRdvz44ucSyZZ032LOwjFhZEaRPc4%2BlAGo0blDxk0mVaDelwvXNw5IZ4WM7relpow2yj95mwTVcOUek5IhXeuPs4TWPhk5QWwO8RqyG4fPTayE1JrtlUFVSqEocp0TGq0U%2FKoMvDcmJRCcJYGYIrkQjq%2FdAdLhiv4uSqClabOuSPehjmIvOqoC6xdH2nlMJmi8z3NvmFiVoSndF2mmG1lqKgyYTHU&X-Amz-Signature=e2084315c97792dfdfc33ea7c79e376fd633d28e99c7deea15e56218a18cab6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMTH4EXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIErB7KS8cBIzOCVRs8mpx%2FvWxBjsDnIODYMSK8dpgEQ2AiEAtE1bDT6RaReP2uXoT1wmn2wUr0zR9ttsMAoJ6n34z9kqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDVqcbYhUxb99afp1SrcAy3PctmwuVr3%2BQ1esqM22bG5mQkg%2BRhTjjRKfcFFFk2CDqq20X%2FtXtkO9rp6Flwr85g1NzKHYqnbJoaGUbknTxcwN3FG83V%2BReXOC0r3iIOavE%2Fiz9sMpxkJD%2F2KLd7XXmkkdHTi6GbArOGbPD9WwZvXodnYatMtzdTpE2xCasWe1ji9057QN8E78wzOKtzkt%2F5JPFcm2F%2BzhqJDG6TrjldbRVBwfogVJSiwdm2undvhFFPmceaHBSIxxRkHIrlxT1lAHCRcf%2BPuPvvdrDoprqwqPsc%2FMjDamgVQgqal6TmcMKP5oN8h5Mu8XoA9tYUj8529x%2FS9WBH0POjaoORAZ8j1lVSb8SX4VokB1jnIUxFnUDZDGD%2F4s5i%2FJ94v9qiLvxwGlBflJD1mqM0oqJK6OWE4AtLkZ3NJcV1Ym5G1jZnjcmNK7maxHwsUr9uYAgjzpB0%2BHP8Qqdxooj89ck2lOn%2FUjjmwx3YfR89p2iTt%2FhLFE0RkTKcIt45E2%2FJsaF7C7utN0Yz2sr%2BiRaOH8ZRzB7fqXmPBnr6TxheTclYOqaAZC9y2DFFrnIsNAJU0KSiriSyoafTmnG4gFu8CVgBQJjE7mTpkSe0%2BIGrAqR5W7AXL7E%2Fwvr0%2B1mREsyWFMPuP57wGOqUBH9alF6DyC2FBYSWzHA7WS8%2FMBAkLRGJsGlsc1%2BXdEGXiWaN6Wqj4oS0a5P0XYoBwJagLDckXpR3gSZRfmKn6CpmqeeRO3u%2BTZ8vOtDbXbzbfOjaEzdi8ZsL247iNR6ShXD%2BtqUVB2ZueW9pal1aLIK8e%2BFigCUJh1iXxoSh90gJX%2Fg4c7uQNk8qn4Tj47pOl7X6zZ0mbz8axqkLA0fqVcsiUpOxy&X-Amz-Signature=6478c427c1bd5e2494d9276424fc964070ac05c758ff925c02c134fc71120692&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMTH4EXE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIErB7KS8cBIzOCVRs8mpx%2FvWxBjsDnIODYMSK8dpgEQ2AiEAtE1bDT6RaReP2uXoT1wmn2wUr0zR9ttsMAoJ6n34z9kqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDVqcbYhUxb99afp1SrcAy3PctmwuVr3%2BQ1esqM22bG5mQkg%2BRhTjjRKfcFFFk2CDqq20X%2FtXtkO9rp6Flwr85g1NzKHYqnbJoaGUbknTxcwN3FG83V%2BReXOC0r3iIOavE%2Fiz9sMpxkJD%2F2KLd7XXmkkdHTi6GbArOGbPD9WwZvXodnYatMtzdTpE2xCasWe1ji9057QN8E78wzOKtzkt%2F5JPFcm2F%2BzhqJDG6TrjldbRVBwfogVJSiwdm2undvhFFPmceaHBSIxxRkHIrlxT1lAHCRcf%2BPuPvvdrDoprqwqPsc%2FMjDamgVQgqal6TmcMKP5oN8h5Mu8XoA9tYUj8529x%2FS9WBH0POjaoORAZ8j1lVSb8SX4VokB1jnIUxFnUDZDGD%2F4s5i%2FJ94v9qiLvxwGlBflJD1mqM0oqJK6OWE4AtLkZ3NJcV1Ym5G1jZnjcmNK7maxHwsUr9uYAgjzpB0%2BHP8Qqdxooj89ck2lOn%2FUjjmwx3YfR89p2iTt%2FhLFE0RkTKcIt45E2%2FJsaF7C7utN0Yz2sr%2BiRaOH8ZRzB7fqXmPBnr6TxheTclYOqaAZC9y2DFFrnIsNAJU0KSiriSyoafTmnG4gFu8CVgBQJjE7mTpkSe0%2BIGrAqR5W7AXL7E%2Fwvr0%2B1mREsyWFMPuP57wGOqUBH9alF6DyC2FBYSWzHA7WS8%2FMBAkLRGJsGlsc1%2BXdEGXiWaN6Wqj4oS0a5P0XYoBwJagLDckXpR3gSZRfmKn6CpmqeeRO3u%2BTZ8vOtDbXbzbfOjaEzdi8ZsL247iNR6ShXD%2BtqUVB2ZueW9pal1aLIK8e%2BFigCUJh1iXxoSh90gJX%2Fg4c7uQNk8qn4Tj47pOl7X6zZ0mbz8axqkLA0fqVcsiUpOxy&X-Amz-Signature=884b07f99df8abf742de374f2dad15368ff3d0b4564d6c3868d60534aa2dffc9&X-Amz-SignedHeaders=host&x-id=GetObject)

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
