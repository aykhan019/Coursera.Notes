

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6DMTJG2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB74%2BTo40bRJJiS5vzAoj%2BCCgugsvbLnLiFoviBhwmAfAiEA%2FK%2Bj8HUF6Ui1PzitoCiRVJJuq5vjC73awajHx3JVbngqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKcIFyoXQMq%2FTgyPoyrcA4UWSii3se%2FXRW9%2FahH9QYkFOAMp%2FwRZc6N5buLQ748GC0MzeHafWoNE%2B86qwIshU%2FqvO18sb9FTjIPBKcfIQYY4sJtxrHnoTU5HBZPHJDj07nGqvx8zoix9q2G0Z1mMtZ2VWE0F5jLu5A0VAOdAtziJGurzVkv8Dgq1yP2j196%2FuV%2BDFPc2T7lBgkRmUfADXzH2ke516jDjbDFAqzrxyxEhHmPaKFy39CaGOOWC8qYUmyUk2n5jfKQZCmgZhfYjvOnElBGXUE9ygEV3WJlutZwtsN6GL05eElaR3nrypM6ebl%2BJ73Ia8odCpKOCErsp0AdCRp6i5G3zwon%2B%2F5O1YOxTZtlXEPw01J4aAxmWoqplfyT49%2FLbme8DUQDeULtC93LnK91byIAnw0YtBv1pqjCiu%2BN8Cty3J8l3nK1X3TdcIO8f7iOYat4F9u%2BkCIczx32VC%2Bns5o3Tqy%2Fl95yB6c11pK4LSAYqslTiQLTO3aqwXz3IY8nfTymkBKQN6DkqQXR7ozbdHk865grHqlqTlQf5LPvI3vn6o8mkJZ4IWCUphHvOJgtmsdOr%2FRARau6WNM0WGWVO4dktZUkh7gR1Lp8YQvoMCUAqN5ex1%2B2yorQWu71VM%2Fspi2Apr6quMPj877wGOqUB1jvrVfZfURQLxAmxm7szD8cVpE6JZ9iP%2F1UI1x3RzDg99LcFehhbQiqBV7mk7LcemjLF%2BsS1K55JmHiM%2FBnwYtYAdkE7B7SWaPGyXDZGvyZ5GthOy9dZUBCh8HQ%2BEdsMtYY2BPsYKOWcl%2BylIbtTVrJl%2FXMGhL8CBS15Aa8um5kglvpiSXaEVLduWa9FicoEUqO69GTrvbpeFVDUuHzdWo5lmsk%2B&X-Amz-Signature=32bed812c2279932afa5fec5148cd14531d09f7511792489fbd60ff9cd4d08fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6DMTJG2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB74%2BTo40bRJJiS5vzAoj%2BCCgugsvbLnLiFoviBhwmAfAiEA%2FK%2Bj8HUF6Ui1PzitoCiRVJJuq5vjC73awajHx3JVbngqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKcIFyoXQMq%2FTgyPoyrcA4UWSii3se%2FXRW9%2FahH9QYkFOAMp%2FwRZc6N5buLQ748GC0MzeHafWoNE%2B86qwIshU%2FqvO18sb9FTjIPBKcfIQYY4sJtxrHnoTU5HBZPHJDj07nGqvx8zoix9q2G0Z1mMtZ2VWE0F5jLu5A0VAOdAtziJGurzVkv8Dgq1yP2j196%2FuV%2BDFPc2T7lBgkRmUfADXzH2ke516jDjbDFAqzrxyxEhHmPaKFy39CaGOOWC8qYUmyUk2n5jfKQZCmgZhfYjvOnElBGXUE9ygEV3WJlutZwtsN6GL05eElaR3nrypM6ebl%2BJ73Ia8odCpKOCErsp0AdCRp6i5G3zwon%2B%2F5O1YOxTZtlXEPw01J4aAxmWoqplfyT49%2FLbme8DUQDeULtC93LnK91byIAnw0YtBv1pqjCiu%2BN8Cty3J8l3nK1X3TdcIO8f7iOYat4F9u%2BkCIczx32VC%2Bns5o3Tqy%2Fl95yB6c11pK4LSAYqslTiQLTO3aqwXz3IY8nfTymkBKQN6DkqQXR7ozbdHk865grHqlqTlQf5LPvI3vn6o8mkJZ4IWCUphHvOJgtmsdOr%2FRARau6WNM0WGWVO4dktZUkh7gR1Lp8YQvoMCUAqN5ex1%2B2yorQWu71VM%2Fspi2Apr6quMPj877wGOqUB1jvrVfZfURQLxAmxm7szD8cVpE6JZ9iP%2F1UI1x3RzDg99LcFehhbQiqBV7mk7LcemjLF%2BsS1K55JmHiM%2FBnwYtYAdkE7B7SWaPGyXDZGvyZ5GthOy9dZUBCh8HQ%2BEdsMtYY2BPsYKOWcl%2BylIbtTVrJl%2FXMGhL8CBS15Aa8um5kglvpiSXaEVLduWa9FicoEUqO69GTrvbpeFVDUuHzdWo5lmsk%2B&X-Amz-Signature=b3fed186612fc384d2b0c79a7407515a895d1222f88e53fc713201e1ccda315c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6DMTJG2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB74%2BTo40bRJJiS5vzAoj%2BCCgugsvbLnLiFoviBhwmAfAiEA%2FK%2Bj8HUF6Ui1PzitoCiRVJJuq5vjC73awajHx3JVbngqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKcIFyoXQMq%2FTgyPoyrcA4UWSii3se%2FXRW9%2FahH9QYkFOAMp%2FwRZc6N5buLQ748GC0MzeHafWoNE%2B86qwIshU%2FqvO18sb9FTjIPBKcfIQYY4sJtxrHnoTU5HBZPHJDj07nGqvx8zoix9q2G0Z1mMtZ2VWE0F5jLu5A0VAOdAtziJGurzVkv8Dgq1yP2j196%2FuV%2BDFPc2T7lBgkRmUfADXzH2ke516jDjbDFAqzrxyxEhHmPaKFy39CaGOOWC8qYUmyUk2n5jfKQZCmgZhfYjvOnElBGXUE9ygEV3WJlutZwtsN6GL05eElaR3nrypM6ebl%2BJ73Ia8odCpKOCErsp0AdCRp6i5G3zwon%2B%2F5O1YOxTZtlXEPw01J4aAxmWoqplfyT49%2FLbme8DUQDeULtC93LnK91byIAnw0YtBv1pqjCiu%2BN8Cty3J8l3nK1X3TdcIO8f7iOYat4F9u%2BkCIczx32VC%2Bns5o3Tqy%2Fl95yB6c11pK4LSAYqslTiQLTO3aqwXz3IY8nfTymkBKQN6DkqQXR7ozbdHk865grHqlqTlQf5LPvI3vn6o8mkJZ4IWCUphHvOJgtmsdOr%2FRARau6WNM0WGWVO4dktZUkh7gR1Lp8YQvoMCUAqN5ex1%2B2yorQWu71VM%2Fspi2Apr6quMPj877wGOqUB1jvrVfZfURQLxAmxm7szD8cVpE6JZ9iP%2F1UI1x3RzDg99LcFehhbQiqBV7mk7LcemjLF%2BsS1K55JmHiM%2FBnwYtYAdkE7B7SWaPGyXDZGvyZ5GthOy9dZUBCh8HQ%2BEdsMtYY2BPsYKOWcl%2BylIbtTVrJl%2FXMGhL8CBS15Aa8um5kglvpiSXaEVLduWa9FicoEUqO69GTrvbpeFVDUuHzdWo5lmsk%2B&X-Amz-Signature=c3e766b00066e5468c6e0e9fd39a39dbdd9c779ba855299ba6333f9e8ffb6e89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZYLRCQ5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBO5rbQZ5DTbnf0H16S0%2FKH6X5FQfFY5J%2FCGrFR4zz0%2BAiBHGpYRXFVU3bKWu7zRwuCG%2BpYZPBbdLwqOA3urOSxOxiqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCt4foPwnLzi8WbYSKtwDVxw5X5hoPNjATZDax9pELpztg4zvbimzq%2BT17hTwI0E07rvmV%2BXmusoapAjU8GKChaebsfH7us0fwYxybev1XoH5QHGRbnujnmMo5y281im8%2BJl2X31jzCHjN0HNhjJgewX7VBo1JdoE8JKJaJNcnTwux2lIAjyxVNsxV3J0rH%2FGSbFF2JIqhNaHNk2vLLJD%2FXzNp9t%2FQmOjYr0U4%2F%2Bo2jvj0rd3dIxBRipxTsbyqZSC%2FLweYTakANT1HxySVRH63sthGHxRGZVaLISUGc7lpi03arfY939fLjC6Jo1SPwLnTNjteYwfOdPHh5mUfLQJu2vcNFkS0tKOblnQy5bxb6mFCdTqvt7gN5rmYLLFDfHJAnCROH3yYeEAhhovFvvfCXpBCULcVTqpnXAgvxWCO0VqVBcuJAO%2BcCssr7Jmo4CL9DRklQ%2FWMOD1DTNqF%2B1umIgc2kzHtD%2FBtfKhbXu0ySwAfCWjCmRZVx2mP0fIDHhS3lH9M2J4uVJkGCFIUKkilR5cv8iqikNzw9Rr%2BLooU1ipzv2xc28lxlwkzch636tcsGbSwiT3ue1JP0ExusTQs2nzR69uyvu8D5nvf3caY5TFqtXdUoi3yHs8egG2tgIy4wzkP8Nwo6MdLHwwnP3vvAY6pgEJ6dfiHXpjcA6KcX%2FaTcamFF1a81p1xzEQWrwvec3G0YevBjalO34XjAxNcP2dKjSt1gItJ%2FQZ64d79KuPP83uK70y2ddF%2BIN5snCou2ag1hWLQ9SavGrNHuSwL6HyG04Cj4goevztvq2WzKRp%2BiAGafrVEtN55JBw1%2Fpztyu5JNzJunudDygn7oiKve%2BCJ7lfD0S99GOBj8IBc4boYGHlB%2FwLQg95&X-Amz-Signature=3c827e30f66cc4b7d9cb878aa523d4376e0cfc33cbaacf60c2b1a2aae49e4988&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZYLRCQ5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBO5rbQZ5DTbnf0H16S0%2FKH6X5FQfFY5J%2FCGrFR4zz0%2BAiBHGpYRXFVU3bKWu7zRwuCG%2BpYZPBbdLwqOA3urOSxOxiqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCt4foPwnLzi8WbYSKtwDVxw5X5hoPNjATZDax9pELpztg4zvbimzq%2BT17hTwI0E07rvmV%2BXmusoapAjU8GKChaebsfH7us0fwYxybev1XoH5QHGRbnujnmMo5y281im8%2BJl2X31jzCHjN0HNhjJgewX7VBo1JdoE8JKJaJNcnTwux2lIAjyxVNsxV3J0rH%2FGSbFF2JIqhNaHNk2vLLJD%2FXzNp9t%2FQmOjYr0U4%2F%2Bo2jvj0rd3dIxBRipxTsbyqZSC%2FLweYTakANT1HxySVRH63sthGHxRGZVaLISUGc7lpi03arfY939fLjC6Jo1SPwLnTNjteYwfOdPHh5mUfLQJu2vcNFkS0tKOblnQy5bxb6mFCdTqvt7gN5rmYLLFDfHJAnCROH3yYeEAhhovFvvfCXpBCULcVTqpnXAgvxWCO0VqVBcuJAO%2BcCssr7Jmo4CL9DRklQ%2FWMOD1DTNqF%2B1umIgc2kzHtD%2FBtfKhbXu0ySwAfCWjCmRZVx2mP0fIDHhS3lH9M2J4uVJkGCFIUKkilR5cv8iqikNzw9Rr%2BLooU1ipzv2xc28lxlwkzch636tcsGbSwiT3ue1JP0ExusTQs2nzR69uyvu8D5nvf3caY5TFqtXdUoi3yHs8egG2tgIy4wzkP8Nwo6MdLHwwnP3vvAY6pgEJ6dfiHXpjcA6KcX%2FaTcamFF1a81p1xzEQWrwvec3G0YevBjalO34XjAxNcP2dKjSt1gItJ%2FQZ64d79KuPP83uK70y2ddF%2BIN5snCou2ag1hWLQ9SavGrNHuSwL6HyG04Cj4goevztvq2WzKRp%2BiAGafrVEtN55JBw1%2Fpztyu5JNzJunudDygn7oiKve%2BCJ7lfD0S99GOBj8IBc4boYGHlB%2FwLQg95&X-Amz-Signature=107a140c5baa1520d45398f4fd7053b052313fb6ee7123059406cf12f832fec9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZYLRCQ5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBO5rbQZ5DTbnf0H16S0%2FKH6X5FQfFY5J%2FCGrFR4zz0%2BAiBHGpYRXFVU3bKWu7zRwuCG%2BpYZPBbdLwqOA3urOSxOxiqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCt4foPwnLzi8WbYSKtwDVxw5X5hoPNjATZDax9pELpztg4zvbimzq%2BT17hTwI0E07rvmV%2BXmusoapAjU8GKChaebsfH7us0fwYxybev1XoH5QHGRbnujnmMo5y281im8%2BJl2X31jzCHjN0HNhjJgewX7VBo1JdoE8JKJaJNcnTwux2lIAjyxVNsxV3J0rH%2FGSbFF2JIqhNaHNk2vLLJD%2FXzNp9t%2FQmOjYr0U4%2F%2Bo2jvj0rd3dIxBRipxTsbyqZSC%2FLweYTakANT1HxySVRH63sthGHxRGZVaLISUGc7lpi03arfY939fLjC6Jo1SPwLnTNjteYwfOdPHh5mUfLQJu2vcNFkS0tKOblnQy5bxb6mFCdTqvt7gN5rmYLLFDfHJAnCROH3yYeEAhhovFvvfCXpBCULcVTqpnXAgvxWCO0VqVBcuJAO%2BcCssr7Jmo4CL9DRklQ%2FWMOD1DTNqF%2B1umIgc2kzHtD%2FBtfKhbXu0ySwAfCWjCmRZVx2mP0fIDHhS3lH9M2J4uVJkGCFIUKkilR5cv8iqikNzw9Rr%2BLooU1ipzv2xc28lxlwkzch636tcsGbSwiT3ue1JP0ExusTQs2nzR69uyvu8D5nvf3caY5TFqtXdUoi3yHs8egG2tgIy4wzkP8Nwo6MdLHwwnP3vvAY6pgEJ6dfiHXpjcA6KcX%2FaTcamFF1a81p1xzEQWrwvec3G0YevBjalO34XjAxNcP2dKjSt1gItJ%2FQZ64d79KuPP83uK70y2ddF%2BIN5snCou2ag1hWLQ9SavGrNHuSwL6HyG04Cj4goevztvq2WzKRp%2BiAGafrVEtN55JBw1%2Fpztyu5JNzJunudDygn7oiKve%2BCJ7lfD0S99GOBj8IBc4boYGHlB%2FwLQg95&X-Amz-Signature=d4b8f0360b93baaaea505b40abda8204e0a94b0df8a845922f41f97231b8964e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZYLRCQ5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBO5rbQZ5DTbnf0H16S0%2FKH6X5FQfFY5J%2FCGrFR4zz0%2BAiBHGpYRXFVU3bKWu7zRwuCG%2BpYZPBbdLwqOA3urOSxOxiqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCt4foPwnLzi8WbYSKtwDVxw5X5hoPNjATZDax9pELpztg4zvbimzq%2BT17hTwI0E07rvmV%2BXmusoapAjU8GKChaebsfH7us0fwYxybev1XoH5QHGRbnujnmMo5y281im8%2BJl2X31jzCHjN0HNhjJgewX7VBo1JdoE8JKJaJNcnTwux2lIAjyxVNsxV3J0rH%2FGSbFF2JIqhNaHNk2vLLJD%2FXzNp9t%2FQmOjYr0U4%2F%2Bo2jvj0rd3dIxBRipxTsbyqZSC%2FLweYTakANT1HxySVRH63sthGHxRGZVaLISUGc7lpi03arfY939fLjC6Jo1SPwLnTNjteYwfOdPHh5mUfLQJu2vcNFkS0tKOblnQy5bxb6mFCdTqvt7gN5rmYLLFDfHJAnCROH3yYeEAhhovFvvfCXpBCULcVTqpnXAgvxWCO0VqVBcuJAO%2BcCssr7Jmo4CL9DRklQ%2FWMOD1DTNqF%2B1umIgc2kzHtD%2FBtfKhbXu0ySwAfCWjCmRZVx2mP0fIDHhS3lH9M2J4uVJkGCFIUKkilR5cv8iqikNzw9Rr%2BLooU1ipzv2xc28lxlwkzch636tcsGbSwiT3ue1JP0ExusTQs2nzR69uyvu8D5nvf3caY5TFqtXdUoi3yHs8egG2tgIy4wzkP8Nwo6MdLHwwnP3vvAY6pgEJ6dfiHXpjcA6KcX%2FaTcamFF1a81p1xzEQWrwvec3G0YevBjalO34XjAxNcP2dKjSt1gItJ%2FQZ64d79KuPP83uK70y2ddF%2BIN5snCou2ag1hWLQ9SavGrNHuSwL6HyG04Cj4goevztvq2WzKRp%2BiAGafrVEtN55JBw1%2Fpztyu5JNzJunudDygn7oiKve%2BCJ7lfD0S99GOBj8IBc4boYGHlB%2FwLQg95&X-Amz-Signature=37d81d8db7c6a590f36abf7622435c6012c0ffc0d351997745319f6e1791f5a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZYLRCQ5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBO5rbQZ5DTbnf0H16S0%2FKH6X5FQfFY5J%2FCGrFR4zz0%2BAiBHGpYRXFVU3bKWu7zRwuCG%2BpYZPBbdLwqOA3urOSxOxiqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCt4foPwnLzi8WbYSKtwDVxw5X5hoPNjATZDax9pELpztg4zvbimzq%2BT17hTwI0E07rvmV%2BXmusoapAjU8GKChaebsfH7us0fwYxybev1XoH5QHGRbnujnmMo5y281im8%2BJl2X31jzCHjN0HNhjJgewX7VBo1JdoE8JKJaJNcnTwux2lIAjyxVNsxV3J0rH%2FGSbFF2JIqhNaHNk2vLLJD%2FXzNp9t%2FQmOjYr0U4%2F%2Bo2jvj0rd3dIxBRipxTsbyqZSC%2FLweYTakANT1HxySVRH63sthGHxRGZVaLISUGc7lpi03arfY939fLjC6Jo1SPwLnTNjteYwfOdPHh5mUfLQJu2vcNFkS0tKOblnQy5bxb6mFCdTqvt7gN5rmYLLFDfHJAnCROH3yYeEAhhovFvvfCXpBCULcVTqpnXAgvxWCO0VqVBcuJAO%2BcCssr7Jmo4CL9DRklQ%2FWMOD1DTNqF%2B1umIgc2kzHtD%2FBtfKhbXu0ySwAfCWjCmRZVx2mP0fIDHhS3lH9M2J4uVJkGCFIUKkilR5cv8iqikNzw9Rr%2BLooU1ipzv2xc28lxlwkzch636tcsGbSwiT3ue1JP0ExusTQs2nzR69uyvu8D5nvf3caY5TFqtXdUoi3yHs8egG2tgIy4wzkP8Nwo6MdLHwwnP3vvAY6pgEJ6dfiHXpjcA6KcX%2FaTcamFF1a81p1xzEQWrwvec3G0YevBjalO34XjAxNcP2dKjSt1gItJ%2FQZ64d79KuPP83uK70y2ddF%2BIN5snCou2ag1hWLQ9SavGrNHuSwL6HyG04Cj4goevztvq2WzKRp%2BiAGafrVEtN55JBw1%2Fpztyu5JNzJunudDygn7oiKve%2BCJ7lfD0S99GOBj8IBc4boYGHlB%2FwLQg95&X-Amz-Signature=4db161ef02d22fb1c0d7ab5bc203b9f531a5ecebd71a9f80e63f4aff723273ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZYLRCQ5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBO5rbQZ5DTbnf0H16S0%2FKH6X5FQfFY5J%2FCGrFR4zz0%2BAiBHGpYRXFVU3bKWu7zRwuCG%2BpYZPBbdLwqOA3urOSxOxiqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCt4foPwnLzi8WbYSKtwDVxw5X5hoPNjATZDax9pELpztg4zvbimzq%2BT17hTwI0E07rvmV%2BXmusoapAjU8GKChaebsfH7us0fwYxybev1XoH5QHGRbnujnmMo5y281im8%2BJl2X31jzCHjN0HNhjJgewX7VBo1JdoE8JKJaJNcnTwux2lIAjyxVNsxV3J0rH%2FGSbFF2JIqhNaHNk2vLLJD%2FXzNp9t%2FQmOjYr0U4%2F%2Bo2jvj0rd3dIxBRipxTsbyqZSC%2FLweYTakANT1HxySVRH63sthGHxRGZVaLISUGc7lpi03arfY939fLjC6Jo1SPwLnTNjteYwfOdPHh5mUfLQJu2vcNFkS0tKOblnQy5bxb6mFCdTqvt7gN5rmYLLFDfHJAnCROH3yYeEAhhovFvvfCXpBCULcVTqpnXAgvxWCO0VqVBcuJAO%2BcCssr7Jmo4CL9DRklQ%2FWMOD1DTNqF%2B1umIgc2kzHtD%2FBtfKhbXu0ySwAfCWjCmRZVx2mP0fIDHhS3lH9M2J4uVJkGCFIUKkilR5cv8iqikNzw9Rr%2BLooU1ipzv2xc28lxlwkzch636tcsGbSwiT3ue1JP0ExusTQs2nzR69uyvu8D5nvf3caY5TFqtXdUoi3yHs8egG2tgIy4wzkP8Nwo6MdLHwwnP3vvAY6pgEJ6dfiHXpjcA6KcX%2FaTcamFF1a81p1xzEQWrwvec3G0YevBjalO34XjAxNcP2dKjSt1gItJ%2FQZ64d79KuPP83uK70y2ddF%2BIN5snCou2ag1hWLQ9SavGrNHuSwL6HyG04Cj4goevztvq2WzKRp%2BiAGafrVEtN55JBw1%2Fpztyu5JNzJunudDygn7oiKve%2BCJ7lfD0S99GOBj8IBc4boYGHlB%2FwLQg95&X-Amz-Signature=8ca2a7d896a03e70998e9c3018ced3913bf94370669bcc0c30ae4599d31b72c7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCCRRKJ3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfxzZ4JY0zm385apoqrNWmXNQ81YOjLexBawo7aHbwEgIhAPLei8Bjdy2hX1XQDM0LMD5rA4oSA1Th%2BEwOPVWwsR5zKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxx3Dftr7tLDi8zZyEq3ANJfKwUZAS%2FDNb5FhdXxCxYPdYzSeXq2%2B3nqIHWGaZfEpEvILYf9u2pnLhmAuqbZGC6gBB%2FrKPXTOwA45vjtCf4ZO1VA%2FroNWE14%2FZgjdS3t6%2FUCG1EGmEnRX4FlQH5ER9THZwyOuZUzNSCn7gc2gRZ6K8E7dAFr3P%2FbIfhHqsDtWozih8s7k7n4Sju7YpRcjx6Oj2XZSDQpkbjNsOtG6PvuF4fMgMut9Aqda0XrqDU%2Bjsl2WjzhWfYH6idlBMBnzfLitYqw6zIgZ%2B1NjJMp%2FYFN6KbugA%2BuvpV76X5pZqY%2FskqoLSBAcoFy9JBda6m%2FMiOYnBPzl8xz%2Bpmk0jD7jDPjsWPq2T5%2FuqjNfdgahbx5DyFe9n9FqbVe7Npkh6FSGUrcUGxiYHDwdCQ%2BHMlY2crSSiQQede6yKUuVSe08OWpQ%2BFxQrAkSxRXUBBeXjfsxpB%2FF5ufcqmaAWZialGpxtHHa4Gh6wPjt60QBLjQObAneBYz07%2FAiC3pCAtbg9hnEB0StSKIR4Q%2BCE8%2BfOqpBYYLjAFh%2FicfHA6MYiaNFwCf0t39gyFMmYKzFqtscv1slSglG3HCy8nJQCciMJsD9tTB3z2tnTU3R22okbo6jFql0WpEOkaXlnj2KJKZzC5%2Fe%2B8BjqkATfP3XVayK0LBtCbESsxxV%2BiYziyhUyPxRID3w3KdW%2FNjvjTK3IDBFqLvUTnq3PKcneonY8gRWwcyXlNTmREnYqDGVWshElEBWNcGKyAJF8vOZLynrV3ybKeGocfY0T%2FznD8L6tuOl1R6TcDHStK5E53p4Zo%2BY0U6mGnANJSwZYMFvWYhFRNjrCLBQQbs9fYdSn1FvTN6QTEQF0pa2swAFsGTCEh&X-Amz-Signature=a5040d5aff760cedcc05d5a774b6772ba8715aa913fc0a74e2b777d808691457&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7WI4AQ6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD44nP%2B93vrjv4oCL9R3BlQKpj27nZhwZfQHAyjKmYlUwIhAIjpDtH35pYrB8oRIgIqzkX2Yo2jBLLPmRNpLSJBY%2BYJKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyoAddfFiOqszmSGUoq3AM81MRWRtJ8h2NKumXj2hEBse8eecPfKzZ7yhWOpT%2FpYWstwZ0XBoHMs%2FWUKarNOOhiotldYUDvC7iSU%2B4CRZtpgnKGoHI0n%2FzlIaMLJIpjrK6NZ6Ql4cev8opT2eZZboDnCpX9ezhnFyb5%2BQ%2BrbNcUYqZrgQfprB%2F88HNwN7vtEvQMcESfF1hPUGQb8G1h1ESaT797SH4SHoPCFEEC83IDdBToALBehEqxKWA6tSziUGc5ogsvqxkJnCqY1rLy3bx2mmCfTjiSmeJ09Vx5ACyvjPKs%2F9pFTo%2BiDoz4vEXjQVsGqD%2BW2dpaBAC3o1BInPNpe8QCqHEWykQDnzjF7TAYn%2FbqyVvVNuEAkUefkQtrm4I26sOT2pbzjIsQlnM6mMW%2FK2Xzb8GrqMUe3g5shuJ47IQoIm1FyUP1%2BsQLWMrauhKSKR3yGJUw1W4wtPRDLzH4LXqFvVAIg%2FejL2SZ%2BDPiG2PJS0bVmpNA3Anf3HVtkg4YZF%2FU6fAsdAqgiqME1UVup3coeoYDtn6FSPxT0s9NoVPMBe5XqloAKDwgclbhiuh9KJgJm3aRO4coPUfLWMLYQbw5gM6%2BzBlJ1OwfKsMZV31Q3Vp8U%2By5NEUSWIU4Hd%2Ffp01GQ0JfkODiTjCz%2FO%2B8BjqkAbbf56KTQrECo3HKDLXMsIoIpC6GnAqhc3YYlMjJbuwByn6PzyVnQd4QoC%2FtVgtfULNgw52xU3Gqq7jHzFOxujIFlW5qlK7iqe%2BGNrp6hiuiYYL8BqWuTd07CDb3bdkSJ%2FSOza%2FQVMnqTU92CZW1Z2zvUFiU8ayPZThIURmydYIK%2FBXIkUXVwCIJ6ZDOjHWWqlMT%2FtxRQWASQXwp5q60ebafgtEw&X-Amz-Signature=c89a53cec798c05c8167f9367f827714deea08f353ccbdde41f1205e605d8fe8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZYLRCQ5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBO5rbQZ5DTbnf0H16S0%2FKH6X5FQfFY5J%2FCGrFR4zz0%2BAiBHGpYRXFVU3bKWu7zRwuCG%2BpYZPBbdLwqOA3urOSxOxiqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCt4foPwnLzi8WbYSKtwDVxw5X5hoPNjATZDax9pELpztg4zvbimzq%2BT17hTwI0E07rvmV%2BXmusoapAjU8GKChaebsfH7us0fwYxybev1XoH5QHGRbnujnmMo5y281im8%2BJl2X31jzCHjN0HNhjJgewX7VBo1JdoE8JKJaJNcnTwux2lIAjyxVNsxV3J0rH%2FGSbFF2JIqhNaHNk2vLLJD%2FXzNp9t%2FQmOjYr0U4%2F%2Bo2jvj0rd3dIxBRipxTsbyqZSC%2FLweYTakANT1HxySVRH63sthGHxRGZVaLISUGc7lpi03arfY939fLjC6Jo1SPwLnTNjteYwfOdPHh5mUfLQJu2vcNFkS0tKOblnQy5bxb6mFCdTqvt7gN5rmYLLFDfHJAnCROH3yYeEAhhovFvvfCXpBCULcVTqpnXAgvxWCO0VqVBcuJAO%2BcCssr7Jmo4CL9DRklQ%2FWMOD1DTNqF%2B1umIgc2kzHtD%2FBtfKhbXu0ySwAfCWjCmRZVx2mP0fIDHhS3lH9M2J4uVJkGCFIUKkilR5cv8iqikNzw9Rr%2BLooU1ipzv2xc28lxlwkzch636tcsGbSwiT3ue1JP0ExusTQs2nzR69uyvu8D5nvf3caY5TFqtXdUoi3yHs8egG2tgIy4wzkP8Nwo6MdLHwwnP3vvAY6pgEJ6dfiHXpjcA6KcX%2FaTcamFF1a81p1xzEQWrwvec3G0YevBjalO34XjAxNcP2dKjSt1gItJ%2FQZ64d79KuPP83uK70y2ddF%2BIN5snCou2ag1hWLQ9SavGrNHuSwL6HyG04Cj4goevztvq2WzKRp%2BiAGafrVEtN55JBw1%2Fpztyu5JNzJunudDygn7oiKve%2BCJ7lfD0S99GOBj8IBc4boYGHlB%2FwLQg95&X-Amz-Signature=c651eee05cf644da06b56e78cda1014cd22ac86c5ec41266726f0e14c8b60e01&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZYLRCQ5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBO5rbQZ5DTbnf0H16S0%2FKH6X5FQfFY5J%2FCGrFR4zz0%2BAiBHGpYRXFVU3bKWu7zRwuCG%2BpYZPBbdLwqOA3urOSxOxiqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCt4foPwnLzi8WbYSKtwDVxw5X5hoPNjATZDax9pELpztg4zvbimzq%2BT17hTwI0E07rvmV%2BXmusoapAjU8GKChaebsfH7us0fwYxybev1XoH5QHGRbnujnmMo5y281im8%2BJl2X31jzCHjN0HNhjJgewX7VBo1JdoE8JKJaJNcnTwux2lIAjyxVNsxV3J0rH%2FGSbFF2JIqhNaHNk2vLLJD%2FXzNp9t%2FQmOjYr0U4%2F%2Bo2jvj0rd3dIxBRipxTsbyqZSC%2FLweYTakANT1HxySVRH63sthGHxRGZVaLISUGc7lpi03arfY939fLjC6Jo1SPwLnTNjteYwfOdPHh5mUfLQJu2vcNFkS0tKOblnQy5bxb6mFCdTqvt7gN5rmYLLFDfHJAnCROH3yYeEAhhovFvvfCXpBCULcVTqpnXAgvxWCO0VqVBcuJAO%2BcCssr7Jmo4CL9DRklQ%2FWMOD1DTNqF%2B1umIgc2kzHtD%2FBtfKhbXu0ySwAfCWjCmRZVx2mP0fIDHhS3lH9M2J4uVJkGCFIUKkilR5cv8iqikNzw9Rr%2BLooU1ipzv2xc28lxlwkzch636tcsGbSwiT3ue1JP0ExusTQs2nzR69uyvu8D5nvf3caY5TFqtXdUoi3yHs8egG2tgIy4wzkP8Nwo6MdLHwwnP3vvAY6pgEJ6dfiHXpjcA6KcX%2FaTcamFF1a81p1xzEQWrwvec3G0YevBjalO34XjAxNcP2dKjSt1gItJ%2FQZ64d79KuPP83uK70y2ddF%2BIN5snCou2ag1hWLQ9SavGrNHuSwL6HyG04Cj4goevztvq2WzKRp%2BiAGafrVEtN55JBw1%2Fpztyu5JNzJunudDygn7oiKve%2BCJ7lfD0S99GOBj8IBc4boYGHlB%2FwLQg95&X-Amz-Signature=579ffe7f1150cdcb955f47ff09bb227801d2981a519bb32127e2f6a6c97888dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZYLRCQ5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBO5rbQZ5DTbnf0H16S0%2FKH6X5FQfFY5J%2FCGrFR4zz0%2BAiBHGpYRXFVU3bKWu7zRwuCG%2BpYZPBbdLwqOA3urOSxOxiqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCt4foPwnLzi8WbYSKtwDVxw5X5hoPNjATZDax9pELpztg4zvbimzq%2BT17hTwI0E07rvmV%2BXmusoapAjU8GKChaebsfH7us0fwYxybev1XoH5QHGRbnujnmMo5y281im8%2BJl2X31jzCHjN0HNhjJgewX7VBo1JdoE8JKJaJNcnTwux2lIAjyxVNsxV3J0rH%2FGSbFF2JIqhNaHNk2vLLJD%2FXzNp9t%2FQmOjYr0U4%2F%2Bo2jvj0rd3dIxBRipxTsbyqZSC%2FLweYTakANT1HxySVRH63sthGHxRGZVaLISUGc7lpi03arfY939fLjC6Jo1SPwLnTNjteYwfOdPHh5mUfLQJu2vcNFkS0tKOblnQy5bxb6mFCdTqvt7gN5rmYLLFDfHJAnCROH3yYeEAhhovFvvfCXpBCULcVTqpnXAgvxWCO0VqVBcuJAO%2BcCssr7Jmo4CL9DRklQ%2FWMOD1DTNqF%2B1umIgc2kzHtD%2FBtfKhbXu0ySwAfCWjCmRZVx2mP0fIDHhS3lH9M2J4uVJkGCFIUKkilR5cv8iqikNzw9Rr%2BLooU1ipzv2xc28lxlwkzch636tcsGbSwiT3ue1JP0ExusTQs2nzR69uyvu8D5nvf3caY5TFqtXdUoi3yHs8egG2tgIy4wzkP8Nwo6MdLHwwnP3vvAY6pgEJ6dfiHXpjcA6KcX%2FaTcamFF1a81p1xzEQWrwvec3G0YevBjalO34XjAxNcP2dKjSt1gItJ%2FQZ64d79KuPP83uK70y2ddF%2BIN5snCou2ag1hWLQ9SavGrNHuSwL6HyG04Cj4goevztvq2WzKRp%2BiAGafrVEtN55JBw1%2Fpztyu5JNzJunudDygn7oiKve%2BCJ7lfD0S99GOBj8IBc4boYGHlB%2FwLQg95&X-Amz-Signature=c323c009568b791dd5e1358699bec6cb698590a2cd42d3b053b0c13864498499&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL5M4223%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAOFmnSGN0BdB81GB%2BIvEFpbc8VgeB2eAFEyq2CowmNAAiEA66dwpZ7mUz%2BJICt5GFaLPLU5HY9RghjkQ7pkKX8SQQMqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkS2kT2u%2BWM4ZwPnyrcA9kBAzW7hIzPUSBXzUEEr0gBBvKj5XeKIlqT1FuatXKsHEaI%2FCGECl%2BQgDxHJTHkNlFR38%2B483wn2tT2OxuftG%2BGOoysSZqj%2FhcHjnrkIiCnXHqlF8Go7DVcDDQzonH36NMi2z62p%2Ft48mkID%2BS5equ8PAfILefYXd77A%2Bec7qM5gb1j1ZUxMOAaqccaAB9D7s3LoWJO7RD51mkIjHmnhuJu2yKSBp6GMXVqDZtWNW%2BtCgcCNMI7k98Cknq%2F5WpST61ILZQ0x1BR5lf5Oa%2FyFnhhJUURiGJZcaEMaik31sd6fMbxqLhiy%2BmgNga7eDYxhxr%2B9mN6LCOP9MzHFcse7P4HRk2LQJBzUgcHiHcnrQDWDCdxERMLUIGslAd%2Fl%2BmIPZ5kJ15YhJvql2KoVqx2UxAwdq%2FIXa3yyRkLzxeebaps9pudKjQ1FiXJp2jIuv1VxHYbN6vCc%2FXB77GOLzDunFQiiJSxf0JjBe4E%2BDaL4CnezcgP5BK3dT2nOgtUK86WbBw%2ByOkpewQblImwD7l1CBQrCLSyaB1%2FXRZuIkYXIkAJompde6Kk%2FNBjkr1XtYBRjtqm8dccBuDxWycAD7y7mXQGafjSYJhgthtB0zlgFsMFVZFajsVu9Xis9j3eMNf877wGOqUBuFiCZqhBySgTlkKoNzUectDgFrcx81t%2FJ7yAO7gT%2FRQOJNRQKm5ITXmHLWMYMEroRzlv3XwD3WRd0Mh4v9%2Bt0Xz648wE80sXTN7A9r9bvaC%2BRfd0HSW5gFJuQTSpGgORRRaVdvzRbagIZqIqWTWED%2B%2BIXeXhZNZCy6VLXEu7FOI7tlFwRn3AcUzZ7rDrrmdBKyRDsn92QdFUGJ9P1I7jpdneheAn&X-Amz-Signature=f5f0e798677d55fd9c415a9e61337ffc5fb364b644f8ab5339c7aecc04a43221&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664U5CK3TO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC5AMC7YUvuAUjiNL4ynutmh4uYPXHrmO1BsWOPJJBCfAiEA4Zeu4Wbheo2I4qlxi49PzwwtrJA%2BMz9XC35KAbFUYvcqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCY7jmsBAuhjVdXfOSrcA9%2BXXm%2FA0q7rmKsv5IK8tzf5jPXlCvNywefkAgz5i%2BeTOOMuMDibFmoprK%2FvsoIzS8m%2BiAknyVS3nZZWmDgjG4TpUdkthoxbIFTluJ478eB4VSJICX6Mw%2BL4NCvfvt1PYlmNQkLZTGoubABV2jmdnZMqxsiyB0PlaI%2BMLL5v8Lahm8B57UH5pZ%2B8oDVcRKRz8PS7AZsLiCiaZs%2F6PuvWcHZydbXbImhUF9too%2FyIFzr73pQ93R71uA6VzPAODjEVTePzD6oz9xohBbYITLwYKddnqpFe4NWuJhE7PI0in1PeUohi2AJ2fJyI1HfseHbozzcuVjL8yVJpKNZzWLizPuMi8z4qqzymRHG13L7TLEWswW9PlvJCTUn8xK51ZbzmxeWM7wY%2Bibd1b4dS4%2BX5EVJLgrxbPPBeJfRkq0J2vg6rNxK%2FXCNnWbBkoTeS5pYJ39lX2TvIp4i5bgHpxXWDBvLnjeF4XJ1xNS8iI2uzA7g3f0z5DfRJC4cXmL6Ho8aZTvuTW%2BB21sL5L8j0FnPiy8zTKMsPEUhMeUt3ddMTP6qb27F5E89T%2FpdvmHzEzuSIlzBaWc7Ak3Jsaq4hqcb7O4NYpFfs0x078CWd%2B3QbePbNwISYifShCFRXsObJMPb877wGOqUBkrpvS4U4ZFpxAXTVyLo25zaREYYymH%2B6c6mi8t6IBp2dkd6MBWW8byNMN8QhZEZMuGRo3Jifear1fDGqKL86CXmdvECSa68VsXeMawPajcVGmnmwGe3pQzHhxIm7tcZVWEWQ65x1A84%2FU%2FXna6anee2Mr32%2BQXJVY8iAN3xDbSbcwkd4Pu2a4AR6tYvTF3%2BqHsQz6lWWDuUXZAu%2BiQrdeUm0o4LT&X-Amz-Signature=73f5a4394cda9c3146f10613821624f59d6722b66fe748d0bcfe8b4a592819ab&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4EOY6BL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BR8ekJgHVp%2FQtAvtixgktG7n3QYPKWHA3Nt8dnDzTpAIgE6l25v%2FdjheklfWLRS%2FR1%2F%2Bfxu%2BkU%2BDI2RngWl2MsAUqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIGU9GxY4Wrt2Ql7ySrcA2PDW%2F8Vpk6Bpv6YZFzlW3e2%2BIpP1k%2FCHVYj0HKjnuiuQQWocworWW8YZSyoF9KUpz9w8kKE56cpK4ifup36r0kEMmKKKKB6dxTtGC%2FiFNKyyzKEAt0g2fZas741yBsWY%2FxkDESnkdluKlnDYoRCbNW%2B5TmF28fWvPhU9d4e%2Bxlnk8pz5lXYi5m4oHzm%2BR5t1KddmGG4%2BTQZCZPH6%2FNgj%2BFoN4A7UJNsuQjMdX0STPMXkiL7Dy%2FDI7ZuQmgl39FoTTBjDs8psJzAgTdmFgN9%2FKHITZh95vtLCPtsqgmQZhlQksL23r8E7umF2U66vRxUvtvu3yCdQH1I7FF0wgwvMhnK8H3l55vgi36lT7Oept8MR7BUSdd7HvlU2hrRKbLLvxVia%2BdDg04rl6f2aZFrNYTaFk9DFd2QMimgNSlajIpjsUrg8F9y7nJE7ptXXQrraq%2BdGA9p2G683OlZxe2A7r0tkxiJbAZPwXY7mR%2Ff14lnAoG9Skghaul5wl1Vr5zcp2Z%2BuuAlCw8AM7Z76H7aJpxL%2FRIe3d6keJRyxLFYlwWlQzahxv9wry29CEK14bu%2FajFCTkT38oWoz7MSqoXynkWBElLuQpOIO1ne8XDzQi905Il1ToparOSPOTG9MOH877wGOqUBQrM9UN%2BSSl3icNsyHEwG1udmFgYT3twqK8zjtWNZvyhqDwH%2FR%2BIn4452G2We2kYETKwlO3PygROSVa1Mcfq1TU%2FbooA9bRmBCxMIDIFDdGFKH7VlmYQ6DY6lXu1mEY2oEtOOyX7Z%2FLT8dJEUQkB9mZ%2FFTZfC9idgZpR9qD%2BAhqJeQCvH%2F%2FJmZi2j16zbAaosXS%2FE7gAvqqchZAONgSBc%2Bi%2FVQLfs&X-Amz-Signature=e0c2b3bd6cec201d0903a97492af475320ad7002ca3f2049fe668ed0960dd90d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKJTNLIV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAxExGIZDdcBqvRnOia%2B21eb%2FaXgJXe4X2HGNOU61fWXAiA1wD7r3HPHajU7qW7HAoLbe2wFPlPciqfneancO9BCvCqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkxHOEpfuYT9d9IvOKtwDkhMriXw%2FaT53Q0Q1eflvTNetl%2BgtrktoFD6NsRcwl9AJMDLaNaEAOGlUH5YyLtB1ICDkxkyVfZPTlDbMOfcyRhgRya8Jh8PZGL9lN2dJWe32eb1tihS1FR3%2FJC09%2FFcXhDSYMZehfbCRSZEU5YFVMCCcKdyAWwZr%2F6Cshb7NIODAG8lRvnp60kHmChJx2rhsrTWSdDJOaTsIiwLpJ7BZT%2B1vOBDHgrhxkYDY4%2FC8KzbSCBfJCSa%2BvXFReK1NuI5Wej%2FbtsMsyOgeVd0FEicQ%2BkeJ33fM1kEsY3pFCy94COg9JY0JeIZyK7xaxswoGycKNiV0i%2FYwE3TU4FV9zlkCEfOtGPu1s%2FyPKPdphInTGzEbJBnXDBkoaDMyh9x0DKxMNtNzqnby85c6FSz45iL2tJZ0T24oMcat4HafkJjBUn1bHspyKpN6zh2K7ZU9PVIDN%2BKz7RfkmBXJeDE0LKBz5uxsVs04oaXGLO0gKbPHmPHMAkcdZvhaDX%2FtHWa2C021lh%2BMgzVZfsdDIdbAJragjtqEvAqyeXO6RSnKc2Z1hSzqu4PYB%2FVLsCaT0wHP5Jv71zTwF0K%2BAgrT%2FnGaj16C5grOWKUjx%2BeQgzyzMarc%2Boagt7aAdgzOYUGIG7swmf3vvAY6pgHJckyJk7rYuziIO67j4NS0wf%2FbvU%2BtPII8PokaVZ5U31OHCR0BB9V5m0o8o%2FElbAGuzVcH%2FI%2Bc4IRqa%2FCd4TNNPRxnD3SERBEhruABBKG91F4gEP%2BUL6%2FO6zFAtaCvlJUe1RJRmfx0pOV3JS0XaRVYajJdk0HwRjtVuPcZuwYM9%2BJKkveVnsSuO1o6mw04Z5gSxKD8ouf%2FBOgtV3lyrprhQepZZi4A&X-Amz-Signature=a0a8ac0e7ef9968d893faf64d35158dd9dd5d266aa70ca51fa883a3d125cb481&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKJTNLIV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAxExGIZDdcBqvRnOia%2B21eb%2FaXgJXe4X2HGNOU61fWXAiA1wD7r3HPHajU7qW7HAoLbe2wFPlPciqfneancO9BCvCqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkxHOEpfuYT9d9IvOKtwDkhMriXw%2FaT53Q0Q1eflvTNetl%2BgtrktoFD6NsRcwl9AJMDLaNaEAOGlUH5YyLtB1ICDkxkyVfZPTlDbMOfcyRhgRya8Jh8PZGL9lN2dJWe32eb1tihS1FR3%2FJC09%2FFcXhDSYMZehfbCRSZEU5YFVMCCcKdyAWwZr%2F6Cshb7NIODAG8lRvnp60kHmChJx2rhsrTWSdDJOaTsIiwLpJ7BZT%2B1vOBDHgrhxkYDY4%2FC8KzbSCBfJCSa%2BvXFReK1NuI5Wej%2FbtsMsyOgeVd0FEicQ%2BkeJ33fM1kEsY3pFCy94COg9JY0JeIZyK7xaxswoGycKNiV0i%2FYwE3TU4FV9zlkCEfOtGPu1s%2FyPKPdphInTGzEbJBnXDBkoaDMyh9x0DKxMNtNzqnby85c6FSz45iL2tJZ0T24oMcat4HafkJjBUn1bHspyKpN6zh2K7ZU9PVIDN%2BKz7RfkmBXJeDE0LKBz5uxsVs04oaXGLO0gKbPHmPHMAkcdZvhaDX%2FtHWa2C021lh%2BMgzVZfsdDIdbAJragjtqEvAqyeXO6RSnKc2Z1hSzqu4PYB%2FVLsCaT0wHP5Jv71zTwF0K%2BAgrT%2FnGaj16C5grOWKUjx%2BeQgzyzMarc%2Boagt7aAdgzOYUGIG7swmf3vvAY6pgHJckyJk7rYuziIO67j4NS0wf%2FbvU%2BtPII8PokaVZ5U31OHCR0BB9V5m0o8o%2FElbAGuzVcH%2FI%2Bc4IRqa%2FCd4TNNPRxnD3SERBEhruABBKG91F4gEP%2BUL6%2FO6zFAtaCvlJUe1RJRmfx0pOV3JS0XaRVYajJdk0HwRjtVuPcZuwYM9%2BJKkveVnsSuO1o6mw04Z5gSxKD8ouf%2FBOgtV3lyrprhQepZZi4A&X-Amz-Signature=58ffff4dc79cb3e4ba9d4d52bb4e299768f2239099b27c43ba1bdceb08d57b64&X-Amz-SignedHeaders=host&x-id=GetObject)

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
