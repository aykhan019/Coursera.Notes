

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWRFG6Q5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEIG5PtbBrA0LL6QDbZF%2BokxvdAV56K%2BAFt2rrUjkT1uAiEAgrLSSzWFbk1oS2Da4KgNMT9UtmY%2F7ccxtFq0iACJQ3cqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJr9RSNXbXAqtET%2B%2ByrcA0WMCEzQ4ZX%2FiaaJ7lC773jHTnPnVxfL2n4xBCOaLvoViesss9XAiXz9HzSQv4NYOOWUVi4kOPN%2FHQPiJqNh8xuJUNHC58jePZjkL0zeVoNazDpQW6NBg%2BGsv%2FOWM2FfnNSw5h%2BcDkmyTRu88jsp7BfEwDg0JveTR313uWyGgAFnrDt4lWl%2BpGsUPCiSFw9bdGEWJ6A0qjP89wa%2FSkT%2BAkj4hMWEc9I%2BOESynEmuQMQ393stQULzXc1GPWM%2FCM%2Br5JOSuiYrO7V9RAXGjPGmg7t%2F%2BKVyy4Mii%2BGz%2Bsh6hjIVdNPrArbaeifc3aM1aSs24lfMzlGngfoV1uOEu8kq67qofsOUZgpV9Rdwk0hoZ1u%2FZuGIhnXyt%2Fxh5zYDXvP6b9%2Fz%2BkFmjBmG54ISIJrcdonTGcpyuQnLESrxdYvR4ptPmtacuF2Ofmrxc4mkczm5y7WK2S5aDMwARPgzJZSQEMYYY99zF5AhAMW5ahax3EypEPg2y46KglqJI0KAmH2VlCTPN132A1ztoem6T7bzr6EuxfJvAiKJf6TTNNnxQvihWJne21PXIE884jPkFEVIaRbhXrDD3RJHaVfFgKHkFdFfp3mYyVFhRP39RL9TitCSZ79Lhi1kck0Ntv3lMMbQ8LwGOqUB%2Bev6AhrSIdf%2FaM88QGmbQZ1K6Y8pWR%2BEHG8%2FYbxyPSx2xOTlaWtexan3hP%2BZj%2FBraZyrDr5hPvJXtLitCObq4UkCHOaweoouYuy8B%2FsGTY%2F8LxkjWRFaJ22cDNV5LfRukkV2bbHwvh3QWrsCqNM2nBSBk3ISzH4STt6YQKc67lOyZK%2FsrZHRPk3Kvlz%2FcnRIS%2F%2BiwCHb67wkTrCKD%2FMGuPvouwN2&X-Amz-Signature=efcf77917d89c9fd930e1f40ff395c8480f71d6a5f2ce2a4dab9ec5a526be552&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWRFG6Q5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEIG5PtbBrA0LL6QDbZF%2BokxvdAV56K%2BAFt2rrUjkT1uAiEAgrLSSzWFbk1oS2Da4KgNMT9UtmY%2F7ccxtFq0iACJQ3cqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJr9RSNXbXAqtET%2B%2ByrcA0WMCEzQ4ZX%2FiaaJ7lC773jHTnPnVxfL2n4xBCOaLvoViesss9XAiXz9HzSQv4NYOOWUVi4kOPN%2FHQPiJqNh8xuJUNHC58jePZjkL0zeVoNazDpQW6NBg%2BGsv%2FOWM2FfnNSw5h%2BcDkmyTRu88jsp7BfEwDg0JveTR313uWyGgAFnrDt4lWl%2BpGsUPCiSFw9bdGEWJ6A0qjP89wa%2FSkT%2BAkj4hMWEc9I%2BOESynEmuQMQ393stQULzXc1GPWM%2FCM%2Br5JOSuiYrO7V9RAXGjPGmg7t%2F%2BKVyy4Mii%2BGz%2Bsh6hjIVdNPrArbaeifc3aM1aSs24lfMzlGngfoV1uOEu8kq67qofsOUZgpV9Rdwk0hoZ1u%2FZuGIhnXyt%2Fxh5zYDXvP6b9%2Fz%2BkFmjBmG54ISIJrcdonTGcpyuQnLESrxdYvR4ptPmtacuF2Ofmrxc4mkczm5y7WK2S5aDMwARPgzJZSQEMYYY99zF5AhAMW5ahax3EypEPg2y46KglqJI0KAmH2VlCTPN132A1ztoem6T7bzr6EuxfJvAiKJf6TTNNnxQvihWJne21PXIE884jPkFEVIaRbhXrDD3RJHaVfFgKHkFdFfp3mYyVFhRP39RL9TitCSZ79Lhi1kck0Ntv3lMMbQ8LwGOqUB%2Bev6AhrSIdf%2FaM88QGmbQZ1K6Y8pWR%2BEHG8%2FYbxyPSx2xOTlaWtexan3hP%2BZj%2FBraZyrDr5hPvJXtLitCObq4UkCHOaweoouYuy8B%2FsGTY%2F8LxkjWRFaJ22cDNV5LfRukkV2bbHwvh3QWrsCqNM2nBSBk3ISzH4STt6YQKc67lOyZK%2FsrZHRPk3Kvlz%2FcnRIS%2F%2BiwCHb67wkTrCKD%2FMGuPvouwN2&X-Amz-Signature=f4b00802b0f7793f26136f7482cb30adbc8f5351cc223c549c767cdc88173190&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWRFG6Q5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEIG5PtbBrA0LL6QDbZF%2BokxvdAV56K%2BAFt2rrUjkT1uAiEAgrLSSzWFbk1oS2Da4KgNMT9UtmY%2F7ccxtFq0iACJQ3cqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJr9RSNXbXAqtET%2B%2ByrcA0WMCEzQ4ZX%2FiaaJ7lC773jHTnPnVxfL2n4xBCOaLvoViesss9XAiXz9HzSQv4NYOOWUVi4kOPN%2FHQPiJqNh8xuJUNHC58jePZjkL0zeVoNazDpQW6NBg%2BGsv%2FOWM2FfnNSw5h%2BcDkmyTRu88jsp7BfEwDg0JveTR313uWyGgAFnrDt4lWl%2BpGsUPCiSFw9bdGEWJ6A0qjP89wa%2FSkT%2BAkj4hMWEc9I%2BOESynEmuQMQ393stQULzXc1GPWM%2FCM%2Br5JOSuiYrO7V9RAXGjPGmg7t%2F%2BKVyy4Mii%2BGz%2Bsh6hjIVdNPrArbaeifc3aM1aSs24lfMzlGngfoV1uOEu8kq67qofsOUZgpV9Rdwk0hoZ1u%2FZuGIhnXyt%2Fxh5zYDXvP6b9%2Fz%2BkFmjBmG54ISIJrcdonTGcpyuQnLESrxdYvR4ptPmtacuF2Ofmrxc4mkczm5y7WK2S5aDMwARPgzJZSQEMYYY99zF5AhAMW5ahax3EypEPg2y46KglqJI0KAmH2VlCTPN132A1ztoem6T7bzr6EuxfJvAiKJf6TTNNnxQvihWJne21PXIE884jPkFEVIaRbhXrDD3RJHaVfFgKHkFdFfp3mYyVFhRP39RL9TitCSZ79Lhi1kck0Ntv3lMMbQ8LwGOqUB%2Bev6AhrSIdf%2FaM88QGmbQZ1K6Y8pWR%2BEHG8%2FYbxyPSx2xOTlaWtexan3hP%2BZj%2FBraZyrDr5hPvJXtLitCObq4UkCHOaweoouYuy8B%2FsGTY%2F8LxkjWRFaJ22cDNV5LfRukkV2bbHwvh3QWrsCqNM2nBSBk3ISzH4STt6YQKc67lOyZK%2FsrZHRPk3Kvlz%2FcnRIS%2F%2BiwCHb67wkTrCKD%2FMGuPvouwN2&X-Amz-Signature=7aebf457e8cbdc6c571d97a7877ede18516c187fd531027befa100a667d561bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP256BVC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEF9K0oQ2CL61XrQARLVAKfED%2Fyt%2F3nu5qjlME0%2BerrHAiEAm5xXIu4K%2BveRjF06CfbRBJo2y4f7BHk5ZQKkqcl%2B2PQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN6AJVVRM5VXv6g5LSrcA0TJE%2B5T%2BDYSOIJhXrff5h1466vkeNFegZU1muNxKCUuQdCaJE49TcoZ6n2zg9DILT93XVKKkM8smCIOjNH3hEQud2TYnXwHouI7lRxgJWzB%2FocYM1l5KPRfUaNcvvUnTBBLW%2B9fk%2FYu7HzIMz%2FvptwnalUtHiwMyZXRCPPfXKtv4me0r1%2Bj1wNwOthqhX2GP7NZ85YSlL4%2FrsvpMxUmDVoYp97VHDKZ5ih1txh2P8DCVjlv3HjvszPnD9%2Ff0%2BMzdkzvs6i1sEYcKG55RenXVqYljcAn4qCCuNcqdZa8fyF%2BLFT4FAAk%2Biko4OfDeMWAb%2FFTW%2ByKervkO%2BMmLuesae3JLvwrzqmTk9XW8XdBQqSWhk8Kpc2b7vhnNhvLU9gRM476aMCFtx6RcoiCw%2FzF14kMkznBFwi1w%2BXBD%2BINOzmKSXzk6wjWMA2h9LWr%2BOTWpWQDJU9iMjyQwpSNPHj6dsit7k5OjWz%2FesYa%2B9hjq4O1k%2FkZPLPWFpSkFMkZicDZWwkUFLTl5sf%2BUdqQ%2ByJG8Wy46elEw%2BOwCTk%2BVn%2F2Stor5y%2BVjMY%2B7yI94P95yFkspwTTg9uf2iLDAqSEWx8Ga5Kb%2BHaWS8x4Ppa4LuoK4p3bHKA%2FdiLdouJSpAhjMJLQ8LwGOqUBWhSz060Cm60Ig6M8DYh8wgzRZANJPVz%2Fwx9FVqe0ecJDtU9%2BJVJDFXu49GN0JhaqFjAKmSW%2BB8X%2FcwZhnxjRWP6smP4BYo1KCJ%2FKEijrW6G3X1inujM1dJodteyDyuiQzL4SQYsl4ZSViQGUZ3ne1%2FoNShgsxUfPloIqayp2AwbJzYFOKo2ZJgyb0jKEHt%2BGdtS6wUCFFc%2BmlmsDx%2FDaQgKAUp3h&X-Amz-Signature=a4018c2a61c89f42c59e7714b7ebee2a7e199fd34f823034ba062ad60855689e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP256BVC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEF9K0oQ2CL61XrQARLVAKfED%2Fyt%2F3nu5qjlME0%2BerrHAiEAm5xXIu4K%2BveRjF06CfbRBJo2y4f7BHk5ZQKkqcl%2B2PQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN6AJVVRM5VXv6g5LSrcA0TJE%2B5T%2BDYSOIJhXrff5h1466vkeNFegZU1muNxKCUuQdCaJE49TcoZ6n2zg9DILT93XVKKkM8smCIOjNH3hEQud2TYnXwHouI7lRxgJWzB%2FocYM1l5KPRfUaNcvvUnTBBLW%2B9fk%2FYu7HzIMz%2FvptwnalUtHiwMyZXRCPPfXKtv4me0r1%2Bj1wNwOthqhX2GP7NZ85YSlL4%2FrsvpMxUmDVoYp97VHDKZ5ih1txh2P8DCVjlv3HjvszPnD9%2Ff0%2BMzdkzvs6i1sEYcKG55RenXVqYljcAn4qCCuNcqdZa8fyF%2BLFT4FAAk%2Biko4OfDeMWAb%2FFTW%2ByKervkO%2BMmLuesae3JLvwrzqmTk9XW8XdBQqSWhk8Kpc2b7vhnNhvLU9gRM476aMCFtx6RcoiCw%2FzF14kMkznBFwi1w%2BXBD%2BINOzmKSXzk6wjWMA2h9LWr%2BOTWpWQDJU9iMjyQwpSNPHj6dsit7k5OjWz%2FesYa%2B9hjq4O1k%2FkZPLPWFpSkFMkZicDZWwkUFLTl5sf%2BUdqQ%2ByJG8Wy46elEw%2BOwCTk%2BVn%2F2Stor5y%2BVjMY%2B7yI94P95yFkspwTTg9uf2iLDAqSEWx8Ga5Kb%2BHaWS8x4Ppa4LuoK4p3bHKA%2FdiLdouJSpAhjMJLQ8LwGOqUBWhSz060Cm60Ig6M8DYh8wgzRZANJPVz%2Fwx9FVqe0ecJDtU9%2BJVJDFXu49GN0JhaqFjAKmSW%2BB8X%2FcwZhnxjRWP6smP4BYo1KCJ%2FKEijrW6G3X1inujM1dJodteyDyuiQzL4SQYsl4ZSViQGUZ3ne1%2FoNShgsxUfPloIqayp2AwbJzYFOKo2ZJgyb0jKEHt%2BGdtS6wUCFFc%2BmlmsDx%2FDaQgKAUp3h&X-Amz-Signature=e6eeb44c0c0b544d4e4fa5fb0b2c6033231a1470332f6447e351bc74af219c81&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP256BVC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEF9K0oQ2CL61XrQARLVAKfED%2Fyt%2F3nu5qjlME0%2BerrHAiEAm5xXIu4K%2BveRjF06CfbRBJo2y4f7BHk5ZQKkqcl%2B2PQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN6AJVVRM5VXv6g5LSrcA0TJE%2B5T%2BDYSOIJhXrff5h1466vkeNFegZU1muNxKCUuQdCaJE49TcoZ6n2zg9DILT93XVKKkM8smCIOjNH3hEQud2TYnXwHouI7lRxgJWzB%2FocYM1l5KPRfUaNcvvUnTBBLW%2B9fk%2FYu7HzIMz%2FvptwnalUtHiwMyZXRCPPfXKtv4me0r1%2Bj1wNwOthqhX2GP7NZ85YSlL4%2FrsvpMxUmDVoYp97VHDKZ5ih1txh2P8DCVjlv3HjvszPnD9%2Ff0%2BMzdkzvs6i1sEYcKG55RenXVqYljcAn4qCCuNcqdZa8fyF%2BLFT4FAAk%2Biko4OfDeMWAb%2FFTW%2ByKervkO%2BMmLuesae3JLvwrzqmTk9XW8XdBQqSWhk8Kpc2b7vhnNhvLU9gRM476aMCFtx6RcoiCw%2FzF14kMkznBFwi1w%2BXBD%2BINOzmKSXzk6wjWMA2h9LWr%2BOTWpWQDJU9iMjyQwpSNPHj6dsit7k5OjWz%2FesYa%2B9hjq4O1k%2FkZPLPWFpSkFMkZicDZWwkUFLTl5sf%2BUdqQ%2ByJG8Wy46elEw%2BOwCTk%2BVn%2F2Stor5y%2BVjMY%2B7yI94P95yFkspwTTg9uf2iLDAqSEWx8Ga5Kb%2BHaWS8x4Ppa4LuoK4p3bHKA%2FdiLdouJSpAhjMJLQ8LwGOqUBWhSz060Cm60Ig6M8DYh8wgzRZANJPVz%2Fwx9FVqe0ecJDtU9%2BJVJDFXu49GN0JhaqFjAKmSW%2BB8X%2FcwZhnxjRWP6smP4BYo1KCJ%2FKEijrW6G3X1inujM1dJodteyDyuiQzL4SQYsl4ZSViQGUZ3ne1%2FoNShgsxUfPloIqayp2AwbJzYFOKo2ZJgyb0jKEHt%2BGdtS6wUCFFc%2BmlmsDx%2FDaQgKAUp3h&X-Amz-Signature=ddfb6a5da45a24cdddbda2d1d13c3efc0cce5cf3224d9aaf25a05608deab6a35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP256BVC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEF9K0oQ2CL61XrQARLVAKfED%2Fyt%2F3nu5qjlME0%2BerrHAiEAm5xXIu4K%2BveRjF06CfbRBJo2y4f7BHk5ZQKkqcl%2B2PQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN6AJVVRM5VXv6g5LSrcA0TJE%2B5T%2BDYSOIJhXrff5h1466vkeNFegZU1muNxKCUuQdCaJE49TcoZ6n2zg9DILT93XVKKkM8smCIOjNH3hEQud2TYnXwHouI7lRxgJWzB%2FocYM1l5KPRfUaNcvvUnTBBLW%2B9fk%2FYu7HzIMz%2FvptwnalUtHiwMyZXRCPPfXKtv4me0r1%2Bj1wNwOthqhX2GP7NZ85YSlL4%2FrsvpMxUmDVoYp97VHDKZ5ih1txh2P8DCVjlv3HjvszPnD9%2Ff0%2BMzdkzvs6i1sEYcKG55RenXVqYljcAn4qCCuNcqdZa8fyF%2BLFT4FAAk%2Biko4OfDeMWAb%2FFTW%2ByKervkO%2BMmLuesae3JLvwrzqmTk9XW8XdBQqSWhk8Kpc2b7vhnNhvLU9gRM476aMCFtx6RcoiCw%2FzF14kMkznBFwi1w%2BXBD%2BINOzmKSXzk6wjWMA2h9LWr%2BOTWpWQDJU9iMjyQwpSNPHj6dsit7k5OjWz%2FesYa%2B9hjq4O1k%2FkZPLPWFpSkFMkZicDZWwkUFLTl5sf%2BUdqQ%2ByJG8Wy46elEw%2BOwCTk%2BVn%2F2Stor5y%2BVjMY%2B7yI94P95yFkspwTTg9uf2iLDAqSEWx8Ga5Kb%2BHaWS8x4Ppa4LuoK4p3bHKA%2FdiLdouJSpAhjMJLQ8LwGOqUBWhSz060Cm60Ig6M8DYh8wgzRZANJPVz%2Fwx9FVqe0ecJDtU9%2BJVJDFXu49GN0JhaqFjAKmSW%2BB8X%2FcwZhnxjRWP6smP4BYo1KCJ%2FKEijrW6G3X1inujM1dJodteyDyuiQzL4SQYsl4ZSViQGUZ3ne1%2FoNShgsxUfPloIqayp2AwbJzYFOKo2ZJgyb0jKEHt%2BGdtS6wUCFFc%2BmlmsDx%2FDaQgKAUp3h&X-Amz-Signature=737b1cdf2756865c1da61a1aef293714be62b112d659385df3c0410a09e0634a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP256BVC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEF9K0oQ2CL61XrQARLVAKfED%2Fyt%2F3nu5qjlME0%2BerrHAiEAm5xXIu4K%2BveRjF06CfbRBJo2y4f7BHk5ZQKkqcl%2B2PQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN6AJVVRM5VXv6g5LSrcA0TJE%2B5T%2BDYSOIJhXrff5h1466vkeNFegZU1muNxKCUuQdCaJE49TcoZ6n2zg9DILT93XVKKkM8smCIOjNH3hEQud2TYnXwHouI7lRxgJWzB%2FocYM1l5KPRfUaNcvvUnTBBLW%2B9fk%2FYu7HzIMz%2FvptwnalUtHiwMyZXRCPPfXKtv4me0r1%2Bj1wNwOthqhX2GP7NZ85YSlL4%2FrsvpMxUmDVoYp97VHDKZ5ih1txh2P8DCVjlv3HjvszPnD9%2Ff0%2BMzdkzvs6i1sEYcKG55RenXVqYljcAn4qCCuNcqdZa8fyF%2BLFT4FAAk%2Biko4OfDeMWAb%2FFTW%2ByKervkO%2BMmLuesae3JLvwrzqmTk9XW8XdBQqSWhk8Kpc2b7vhnNhvLU9gRM476aMCFtx6RcoiCw%2FzF14kMkznBFwi1w%2BXBD%2BINOzmKSXzk6wjWMA2h9LWr%2BOTWpWQDJU9iMjyQwpSNPHj6dsit7k5OjWz%2FesYa%2B9hjq4O1k%2FkZPLPWFpSkFMkZicDZWwkUFLTl5sf%2BUdqQ%2ByJG8Wy46elEw%2BOwCTk%2BVn%2F2Stor5y%2BVjMY%2B7yI94P95yFkspwTTg9uf2iLDAqSEWx8Ga5Kb%2BHaWS8x4Ppa4LuoK4p3bHKA%2FdiLdouJSpAhjMJLQ8LwGOqUBWhSz060Cm60Ig6M8DYh8wgzRZANJPVz%2Fwx9FVqe0ecJDtU9%2BJVJDFXu49GN0JhaqFjAKmSW%2BB8X%2FcwZhnxjRWP6smP4BYo1KCJ%2FKEijrW6G3X1inujM1dJodteyDyuiQzL4SQYsl4ZSViQGUZ3ne1%2FoNShgsxUfPloIqayp2AwbJzYFOKo2ZJgyb0jKEHt%2BGdtS6wUCFFc%2BmlmsDx%2FDaQgKAUp3h&X-Amz-Signature=8aba06adb4c3da7fd18f40beca92fe4df068aae817cfc847ed448a5ec66feecf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP256BVC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEF9K0oQ2CL61XrQARLVAKfED%2Fyt%2F3nu5qjlME0%2BerrHAiEAm5xXIu4K%2BveRjF06CfbRBJo2y4f7BHk5ZQKkqcl%2B2PQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN6AJVVRM5VXv6g5LSrcA0TJE%2B5T%2BDYSOIJhXrff5h1466vkeNFegZU1muNxKCUuQdCaJE49TcoZ6n2zg9DILT93XVKKkM8smCIOjNH3hEQud2TYnXwHouI7lRxgJWzB%2FocYM1l5KPRfUaNcvvUnTBBLW%2B9fk%2FYu7HzIMz%2FvptwnalUtHiwMyZXRCPPfXKtv4me0r1%2Bj1wNwOthqhX2GP7NZ85YSlL4%2FrsvpMxUmDVoYp97VHDKZ5ih1txh2P8DCVjlv3HjvszPnD9%2Ff0%2BMzdkzvs6i1sEYcKG55RenXVqYljcAn4qCCuNcqdZa8fyF%2BLFT4FAAk%2Biko4OfDeMWAb%2FFTW%2ByKervkO%2BMmLuesae3JLvwrzqmTk9XW8XdBQqSWhk8Kpc2b7vhnNhvLU9gRM476aMCFtx6RcoiCw%2FzF14kMkznBFwi1w%2BXBD%2BINOzmKSXzk6wjWMA2h9LWr%2BOTWpWQDJU9iMjyQwpSNPHj6dsit7k5OjWz%2FesYa%2B9hjq4O1k%2FkZPLPWFpSkFMkZicDZWwkUFLTl5sf%2BUdqQ%2ByJG8Wy46elEw%2BOwCTk%2BVn%2F2Stor5y%2BVjMY%2B7yI94P95yFkspwTTg9uf2iLDAqSEWx8Ga5Kb%2BHaWS8x4Ppa4LuoK4p3bHKA%2FdiLdouJSpAhjMJLQ8LwGOqUBWhSz060Cm60Ig6M8DYh8wgzRZANJPVz%2Fwx9FVqe0ecJDtU9%2BJVJDFXu49GN0JhaqFjAKmSW%2BB8X%2FcwZhnxjRWP6smP4BYo1KCJ%2FKEijrW6G3X1inujM1dJodteyDyuiQzL4SQYsl4ZSViQGUZ3ne1%2FoNShgsxUfPloIqayp2AwbJzYFOKo2ZJgyb0jKEHt%2BGdtS6wUCFFc%2BmlmsDx%2FDaQgKAUp3h&X-Amz-Signature=8fdfa4506af2626a28a9bc91f7423a563d0857e4871b76b1effa181d5838bee3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BORI7MR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHcmkqlvcnD6Ir4OTWzaSARcarXfpFOatppcF6FboPLwIgEXb7dfc1HELtYze%2FrXRX3JSiFpxCF4BYaITwM7m6mLoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLGpJ%2BAQwTbK%2BEKMircA4HHGhbCpWextALNoMb6jZ3ZOAhG92yt2XIeC9udkD3XOSfqdmRwJcRxyRXk3P%2F3Md401qXvxFvVuKdoamEzk01sXeILKWpVz5msYFCu4HBBWfPjkzCM3AWD46LeSD1fhDsXXjrfPqiKNcfLydhCGY1gxsA1fAkKhjsUekLX70aF%2Bh7FA9Kw4GSRPpt4zntqXyzjtsjJCxMatOBzl8%2F%2BMGA9rKlV%2BriRrOCufBlW1TvmSZF7a64RXLqLgmzk7CD9ojk8UfcsMFL9ejDregj42zA8jgO%2Bu91WUxaLLqc5TjU540kvJZOujn3xLWYNTx0ZQwCupI%2BSYGa9jXkZNjSyo9VOntG6D8l0t%2F1PjWO2lZ6sGKlJjeTI9QS%2BkQqH2hwqWhMFlcgurI7QsuA06X7%2Buwi%2F1vZi7iJbBAbBuOUW%2FPTziWumMEmG5kIy%2B6CHdwsPqdlNa715xFMr6xaqY%2BbTNkgsQFJrvncJnhzcp4QK0xioHTmqwb%2FodSUsVtIGOe27rPf216%2BkpOTAnWgLfixv5nOmvd0YpoYI9RqjkhPekEiVWNQGhuSQ0t7cZXeeYebURAH0HSnjQXiOmOuGKeE7DBXXhuLn3seKejAtD5OzHP%2FhqwJSn2ak8C%2FIubQ6MMPQ8LwGOqUBG5PW%2FdmuYuWoS5NNUZczy9eCkM01CbNWz8ARUG5jh8XYLvbh4WwAvBWuIjiIVPYgV8V%2BV5CwfLjBWorCwNrUTLoe1Npo59YC%2FVlWlg2yucVWJvKo9CPwR0PiR3BqL8zOhFpoPu5FA7k5c4qMTgvz7y2uePbh2WR%2FKYhFe1SU1LgFexV5uYxooS3PqmhGCdVg6B2Qy%2FbLCgbIIXARXhNxk9nVdUQE&X-Amz-Signature=08841d05c98876fdb7576f75386bed3359e7cb45ad8bfef2e3a2d445861d02ff&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KNJP6KB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9HMrp%2BZT9rpT6%2BkJTp0L1kdIGEg66jG%2BMQ82AwaE25QIgWTQ3LCf7sz6aU5ClozE49I6N9pCzDMv4%2FwhHEHi%2B3gUqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIoiTYPLbu6VsYe3CrcA6VBm0gyKUTirHBMsqtIr9NvcTAJHNJROZFDToOWIgnZsrK88vhrFFK1sCcTkFnkusS4A8ud393jpWq4RagqHtYglTEG6Dv8dRTgSJ5ThGigKJKFN2K3ftBnfsBCPqt9q%2B2P1Py31nJI%2FhpgeYYEvmRdhOpwJbC0bXjJH7O9S2FVUjY%2BMzHps5GR9KFp5S3j4mw%2FyMFeawPqDVNExSJh39AVWwMezQ%2By0dj2t8C5C21TjnPI8bSK2ncsCbGhXu%2F4OpKhHHbg%2Fe600k1%2F3J249GDb4v5Rh6KifEQpEb2PuL1X41bK%2Fg2IvPE7FAQjb4j0VEj%2FP90EinNSfUx%2FXqTnQDl8jdOGppf9nzRiv6AzXqagO66XFlk5f5WVuS3ZRShY1sLnhYkaMGGAEl7OtD6%2FbOYH4rhEnJnmci70k8WDPAWn88jB4vg8q6schTekTMoMIKzgAUQHr%2F0oVrCcml4ZRABbX72sTep2vUSdiWlrVmUpjTDFEmC1SPIgBMm3FWm0o5dwlUFSP2rULJr3SJOMG%2F3nNCGzZ0FugBn5qGznbb3qvHXvLlCSVMyRggOpMrAmPWV6DCaQW4EJYSnhi0yVJ%2BFIIqiqcmX9wCflqKvi7f9nhiZkQOkhnhkIdTlZMNzR8LwGOqUBApZGz8tZ8r4kaMfkRxodnhFi0qKigrmg7TftwsP%2BQNg1fvRp9AJCQyEr%2Fq2L%2FRqBY7Q9olLxXdDO2uRikb0dULynUH%2B0ggmHpsALjtRZ%2BhvffpM1oftS%2F6gb2h%2FD7mQuqdyjvmvYqvSsTKZQhPOVfxC1yMBjodgGXo9fyfxrkN%2BShE5PFYruF80tP1XHx8i9aK6CmKL2xZKMJ6iosWXlxWBiyWvB&X-Amz-Signature=6f6ad1790abce5017c134c5494d29db71f719fb6bf6eccc7fc35ddffaa4273b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP256BVC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEF9K0oQ2CL61XrQARLVAKfED%2Fyt%2F3nu5qjlME0%2BerrHAiEAm5xXIu4K%2BveRjF06CfbRBJo2y4f7BHk5ZQKkqcl%2B2PQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN6AJVVRM5VXv6g5LSrcA0TJE%2B5T%2BDYSOIJhXrff5h1466vkeNFegZU1muNxKCUuQdCaJE49TcoZ6n2zg9DILT93XVKKkM8smCIOjNH3hEQud2TYnXwHouI7lRxgJWzB%2FocYM1l5KPRfUaNcvvUnTBBLW%2B9fk%2FYu7HzIMz%2FvptwnalUtHiwMyZXRCPPfXKtv4me0r1%2Bj1wNwOthqhX2GP7NZ85YSlL4%2FrsvpMxUmDVoYp97VHDKZ5ih1txh2P8DCVjlv3HjvszPnD9%2Ff0%2BMzdkzvs6i1sEYcKG55RenXVqYljcAn4qCCuNcqdZa8fyF%2BLFT4FAAk%2Biko4OfDeMWAb%2FFTW%2ByKervkO%2BMmLuesae3JLvwrzqmTk9XW8XdBQqSWhk8Kpc2b7vhnNhvLU9gRM476aMCFtx6RcoiCw%2FzF14kMkznBFwi1w%2BXBD%2BINOzmKSXzk6wjWMA2h9LWr%2BOTWpWQDJU9iMjyQwpSNPHj6dsit7k5OjWz%2FesYa%2B9hjq4O1k%2FkZPLPWFpSkFMkZicDZWwkUFLTl5sf%2BUdqQ%2ByJG8Wy46elEw%2BOwCTk%2BVn%2F2Stor5y%2BVjMY%2B7yI94P95yFkspwTTg9uf2iLDAqSEWx8Ga5Kb%2BHaWS8x4Ppa4LuoK4p3bHKA%2FdiLdouJSpAhjMJLQ8LwGOqUBWhSz060Cm60Ig6M8DYh8wgzRZANJPVz%2Fwx9FVqe0ecJDtU9%2BJVJDFXu49GN0JhaqFjAKmSW%2BB8X%2FcwZhnxjRWP6smP4BYo1KCJ%2FKEijrW6G3X1inujM1dJodteyDyuiQzL4SQYsl4ZSViQGUZ3ne1%2FoNShgsxUfPloIqayp2AwbJzYFOKo2ZJgyb0jKEHt%2BGdtS6wUCFFc%2BmlmsDx%2FDaQgKAUp3h&X-Amz-Signature=185c3a997dc7b94e2469c13fa0d462346e6197989b43608b34c6029952bf757b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP256BVC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEF9K0oQ2CL61XrQARLVAKfED%2Fyt%2F3nu5qjlME0%2BerrHAiEAm5xXIu4K%2BveRjF06CfbRBJo2y4f7BHk5ZQKkqcl%2B2PQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN6AJVVRM5VXv6g5LSrcA0TJE%2B5T%2BDYSOIJhXrff5h1466vkeNFegZU1muNxKCUuQdCaJE49TcoZ6n2zg9DILT93XVKKkM8smCIOjNH3hEQud2TYnXwHouI7lRxgJWzB%2FocYM1l5KPRfUaNcvvUnTBBLW%2B9fk%2FYu7HzIMz%2FvptwnalUtHiwMyZXRCPPfXKtv4me0r1%2Bj1wNwOthqhX2GP7NZ85YSlL4%2FrsvpMxUmDVoYp97VHDKZ5ih1txh2P8DCVjlv3HjvszPnD9%2Ff0%2BMzdkzvs6i1sEYcKG55RenXVqYljcAn4qCCuNcqdZa8fyF%2BLFT4FAAk%2Biko4OfDeMWAb%2FFTW%2ByKervkO%2BMmLuesae3JLvwrzqmTk9XW8XdBQqSWhk8Kpc2b7vhnNhvLU9gRM476aMCFtx6RcoiCw%2FzF14kMkznBFwi1w%2BXBD%2BINOzmKSXzk6wjWMA2h9LWr%2BOTWpWQDJU9iMjyQwpSNPHj6dsit7k5OjWz%2FesYa%2B9hjq4O1k%2FkZPLPWFpSkFMkZicDZWwkUFLTl5sf%2BUdqQ%2ByJG8Wy46elEw%2BOwCTk%2BVn%2F2Stor5y%2BVjMY%2B7yI94P95yFkspwTTg9uf2iLDAqSEWx8Ga5Kb%2BHaWS8x4Ppa4LuoK4p3bHKA%2FdiLdouJSpAhjMJLQ8LwGOqUBWhSz060Cm60Ig6M8DYh8wgzRZANJPVz%2Fwx9FVqe0ecJDtU9%2BJVJDFXu49GN0JhaqFjAKmSW%2BB8X%2FcwZhnxjRWP6smP4BYo1KCJ%2FKEijrW6G3X1inujM1dJodteyDyuiQzL4SQYsl4ZSViQGUZ3ne1%2FoNShgsxUfPloIqayp2AwbJzYFOKo2ZJgyb0jKEHt%2BGdtS6wUCFFc%2BmlmsDx%2FDaQgKAUp3h&X-Amz-Signature=b92d4944c9f5d5b9b75800c9e8cba05fe7b505612807573c9f58c904952a06a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP256BVC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEF9K0oQ2CL61XrQARLVAKfED%2Fyt%2F3nu5qjlME0%2BerrHAiEAm5xXIu4K%2BveRjF06CfbRBJo2y4f7BHk5ZQKkqcl%2B2PQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN6AJVVRM5VXv6g5LSrcA0TJE%2B5T%2BDYSOIJhXrff5h1466vkeNFegZU1muNxKCUuQdCaJE49TcoZ6n2zg9DILT93XVKKkM8smCIOjNH3hEQud2TYnXwHouI7lRxgJWzB%2FocYM1l5KPRfUaNcvvUnTBBLW%2B9fk%2FYu7HzIMz%2FvptwnalUtHiwMyZXRCPPfXKtv4me0r1%2Bj1wNwOthqhX2GP7NZ85YSlL4%2FrsvpMxUmDVoYp97VHDKZ5ih1txh2P8DCVjlv3HjvszPnD9%2Ff0%2BMzdkzvs6i1sEYcKG55RenXVqYljcAn4qCCuNcqdZa8fyF%2BLFT4FAAk%2Biko4OfDeMWAb%2FFTW%2ByKervkO%2BMmLuesae3JLvwrzqmTk9XW8XdBQqSWhk8Kpc2b7vhnNhvLU9gRM476aMCFtx6RcoiCw%2FzF14kMkznBFwi1w%2BXBD%2BINOzmKSXzk6wjWMA2h9LWr%2BOTWpWQDJU9iMjyQwpSNPHj6dsit7k5OjWz%2FesYa%2B9hjq4O1k%2FkZPLPWFpSkFMkZicDZWwkUFLTl5sf%2BUdqQ%2ByJG8Wy46elEw%2BOwCTk%2BVn%2F2Stor5y%2BVjMY%2B7yI94P95yFkspwTTg9uf2iLDAqSEWx8Ga5Kb%2BHaWS8x4Ppa4LuoK4p3bHKA%2FdiLdouJSpAhjMJLQ8LwGOqUBWhSz060Cm60Ig6M8DYh8wgzRZANJPVz%2Fwx9FVqe0ecJDtU9%2BJVJDFXu49GN0JhaqFjAKmSW%2BB8X%2FcwZhnxjRWP6smP4BYo1KCJ%2FKEijrW6G3X1inujM1dJodteyDyuiQzL4SQYsl4ZSViQGUZ3ne1%2FoNShgsxUfPloIqayp2AwbJzYFOKo2ZJgyb0jKEHt%2BGdtS6wUCFFc%2BmlmsDx%2FDaQgKAUp3h&X-Amz-Signature=99deedd75eb068911b3da55ee9d711683287452f1f87233cf17c4573bb4635f9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UC3PQ44%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdih5UlrJGhrO9NtgSQghlR2PIrTcD0ml8QUmBiPZ9FQIgb2R9J1iyB41K6FRMZ4DbxmaHi5%2BcmuNNK%2BQyn%2ByQviMqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwpsVGMRC5JBP8CeCrcAy8JtH1RZPqSlmY328CWvdvYGyda%2BSbJGjtbF94yb2Rxuj5gX01SlLeeftHUTwmi%2Furhv0MDsgxiWLqYKgw4pXhLsLQme9qOTpsDO9KJFsIZMiXhVdPE%2Fvz6dyqnS6jl%2Fp1ZmZb6kfULyW1B2llNxDAfmyuM2ye2RDLoq87SJM7JHF5DziC1KU8E9P8crCENIBMtVOaaNo%2F9G8AHMnzc0x6s3zxw5UGq32YnDgAnYH2rz%2B2kExRirI9iNHDr1zv91cH%2BXcHJrrmgNWjkz6bJBty96RbiF%2Fw9%2B3woSo5EqT3Prw5dzJJiWqXjVJTdfPgt9ND7cvgt5UY%2Blw0ls3F9rARYLWB75rmtJajUoOIv4vpmp8K%2FIfYIsG6gFKP5JGadOVoyyB2tNxhKkVOx2VZ5OwJ2HKTeyAQJwIgA2uh9bMZzV7QRR4oHYnXgVMELGxUHo3iPokTr9SvLi1qS8Z57plYkSw9hxEr3DSPDIfb3WGw9hKuHdxuyvWoupIcFccT1N9OWEsbq%2FQy8PzCjwxScwPco6tvVAhmTtFBUK9onTFJF7A4eJc%2FqYaoB%2FW5CRYZZ6gveaEs2ehsiodPmOUFpPcdm9HwPepFEg8Q90lZTW2mkY6PH0B%2FfPC5kO3O1MLjR8LwGOqUBtPJ5bNMLF7HQ63shFlLHEpL3zZAs0cLaSwy8EzdIgdg%2BPSKG4lgjRtbg%2BTcdfEVpFbS%2BFeonQLsMhP8B%2FmOSzdHu7V3w14q%2BSxHh5tD26MdcaCyd8uv67NtMUwaRmPyZOMEbOFJp%2FBt1PswzJFs7Ei5kI9FYu6XqTDbZnrUstYA0Hph3JP432mTVwIHmt9rE0DHYON0H0kFiV61hOuO0KROihDP3&X-Amz-Signature=423c9783c3148b3810f2104bbc3da881f5fe341cbc7fccace08aedaf5a78084a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSV52ZV3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD43stwhPn6pd0bfageD4YCXzXJ0Y32RjCqKqtUASb64gIhAIU9uB5xf%2Fxt1z0vsflQvufDOa5SIju3pDYXJ%2B%2FM0INRKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyP8XVfvS9ikX3B94Eq3AMT4GxqmfRlwfq5zs8cL2063g27k8J0Si8cq6rqmI2upkSYsBXWPbJLulBabTLaIhDAT0AD4PBOciLPmC11brQPR984oTX%2BaXhO4d4pRzAcHBEn%2FtkNnY89lYLHRUS055U0chzg8hNyRr%2BBA9GEQ2sjKJbJkqv78MbmoZaAkQ%2FO0e8mDdOZ7vWXxAtdqJlZ8ADUWnKB7dqhBR19RunbqfnwwlsWcTH7FXijFaKva0y2gyMMMAWUVymcGY3UvgraWMbliWxj9hh0QQrkvTsCFbOKS1nouXtVqr5X1egJ95RZJoMtMeVpt7IN9ZqBRzOla6CwX6C5%2BI41q8aTCPn1gGxP665YXQESVaoh7qWb7fVl0FlDKhYEXjrNEIbB%2BB4LOPfr81owzvFiTTozaJG8%2BI3PKNqcXmgfKfGde%2BA%2BNtF%2BnmZWczaQKDUEuJ7HstP2mevK%2FLk%2FOHGxTFuA2ikoiOu7k1C5LEqVP5CVbUlbH27h%2BkW6T%2F%2Fo1WOzTWsNZSwefkTztOgMI8gyum7uTJFEBIl8ux0AXmufi8rsGOnmVecrlGEmQHS%2Bo1HYn1KIM2p58OPsPFQCpESqpSABD4DTg6BhdnnVsJlW10SwIM%2B9reBKGhe4AI2UcPqHE5THdzC40PC8BjqkAWvtcO2ys2t2%2FFK3042bxd3BDwzXRYaAJYzy%2BPYjKPF1EFUEWcuYWykxuLlA%2BZHisOENAf1%2FcFfiFVmB4HcFkaHwFmmfjLfIAWsYRl33kJnVvgymx%2Fd6zE1ey5Oql%2FXtrmvkPNh1n8wkSOt4wsxHzufId%2FFe88GRaz66A%2F41YxicgxrFBRLM3NtJcBqWxAmJQDSldZTy5mHznUmFaWGHV18S12nH&X-Amz-Signature=f172f2956485fde6370d7fed0228aff56634405d3c64ce4af1ae65a7ee8ae595&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVKYBZZC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA049jXOJAbAUyzylSaPONt8rac7nVZYkNkDKRVbswo4AiAeOLQwUuLlVaB3c8qhA1WB3g7mDlAr8MFiuQJAZkb6nCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoJ1KiKzaAXwhg4bcKtwDPP0b8qmZfR1GW0cG%2F%2FYB8QHGvci8IAo7ViLqibUschx5Vd5VKc7K8ySOwBSrTkkefCVfVNpVMb16vZ2%2Bp9tJ7TSykYq5riWLh%2FA%2F%2F699tIiGImSZaa2kK6s2Wr3QwT4vKA2lR7P%2FZpBeWwLeoESOcxZp4eRazIKpnRoQtYDKc5U%2FCBwRP0O1WeNPn256I8Di2yX6zR5dF7SGuZwUKOGoCxl%2FU0ZBJqHj2zCGQ5%2FxNsuVvlXPkfgwiY8SXGYA8Bw0A6nxissDtaTUTQX0OcSCeq%2BXZ4J7cjIxR6fUbcM1GmaamLWsrpt1c929xsx86vQBUX0UUNjcSgnPOwmzEGSN6tSyLOe50r3iU54qrjWxzONI%2FY0qL7hfW6FWgNL2dPOip6v5uexwl3C5ZoYECCCWCln%2BxDW2ijYZY1tMFzqRJnaAmDsBe0dxMT8jcT37WDCSTsF4YTK3sKBVopS5IzAPNXNwckaEU0ivbHLMwIIhbiaSKovICcVGe%2BawT5JHkeq7v9DQNcKFQ07qyRi4j78uQlM%2Bofi3YCj%2FeNm%2F4nHpTbk6EPCiEO4yzcNS6ys6jx0BR%2BpWYJ7wEUa5PKkkqs5XdkxrK3LYBTYw1HWOyCwHbTpC1Rf1i7QaT%2FuVOhAwsNDwvAY6pgFAv934EBkPDbwu0o9bFT22Cc0YtbZNjxibW4Qj%2Bj2%2FJeHFhXdsF13%2F83ZhW7kxzN09Ul1ZVBQkgWN%2FrHlQ8oJOm4EAiXXU2M277UAYlvruHeQ1AYrfDuwVdkneuWxiqUv2sTgu6Ww5uukP6Ogw6UoM%2F1OuNIdTSmxT6HUwbbHT8yl7%2FzpxcgPhv4bGIc%2FNXnyw77oMXSn7ASgfksECvIbe%2B8ssJgVC&X-Amz-Signature=fb404f86872cc71ee093aca4325e75ececf4316a347eeb3135a8976bb1091d1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JFF5HAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbcr1noC%2BzTKdTpATShPmzss0rHNezLWPp9jDrsVKZ2AiEAiq2KYe5VPSzLqJ45kpgypByfoQXUUUHHm6JribO3Yk8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAo8IDcBrHDockSoJCrcA62nNnLsPV9zYc10K4IqQ19xYQ4%2FwuMaZd5sH2HOlIRlNRw4NLCUgzgtjIFd9WetYmimgYjW2Lqcbzrk2kYMw2ViRhqtCD%2Fwvi9D%2BdKI8jXAEC9BWZbpFhLh6iPOEqjoC3ZRzTXXoKQtLSIMyfQKExnqj9YrSWBoaBnnhiaNTm%2FjqH4gm50fRhREil1AgjSuqIHzVnh5HJ0vf6n34cRiRs05HGZKAyTrSDeQEMp2Jo2nTAXD5jYiSnkztZ9698uqT8sG798KQQUZ86O6p%2FYDozV2upzKa1%2FB7EvzdE3BLa%2BVRnq95dpubf6xRDeyY4DTx3KCSK4yym4voXL%2FB3BhA24afT9uZ9uaYgscPS%2Bqs9J7N9YhVykfGcIviiPShImvGFfUisxrgHfXAv7%2F6xMA1%2FUPcg7NDarOMh863UKJKSgduXmNg0N3ZuThX9jmAmnlH0%2BOjw%2BdLj0fDVzQ0FaPRK2Qsvo795FhCRGtstR4vSrgtbBN6eySw%2BL50WsZlsiMYzUVhYTENJcVuvhITPnztMHSHA8fdF2gMG2%2B%2FZG0woU4qlT%2BCmx96uh7WeU2EjvhqIGgSf1CZZhctgBE4uKJZKyCuB9ZmI6ZkmgZEQ5PGrneNwMXKKihrMUyDovVMJnQ8LwGOqUBpPCnfEKpfFYUDYez6xsZI%2BAoxGogxK%2BQFndSk6QAgd07U6lL3UaXGNq8wErlf6PvKnnIRRcQ0hnlU9kgDzLbTBZxB1AdFyW0%2FqUs3ma%2FVZa%2FKRjHhLG2j9sCaeRq2o%2B0HjHdiqCjSvhJfmeZ0oQsdlVjLrTl%2FymMMIAphIiIjv4DV5%2FEIvDzNrDff%2BzbpJ3WzvAuxBlbQAPsNMPYXnq2aDbiJJsT&X-Amz-Signature=07848f9face51e917fe475924240580098a93ceab30b62c0b49c588e08425518&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JFF5HAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbcr1noC%2BzTKdTpATShPmzss0rHNezLWPp9jDrsVKZ2AiEAiq2KYe5VPSzLqJ45kpgypByfoQXUUUHHm6JribO3Yk8qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAo8IDcBrHDockSoJCrcA62nNnLsPV9zYc10K4IqQ19xYQ4%2FwuMaZd5sH2HOlIRlNRw4NLCUgzgtjIFd9WetYmimgYjW2Lqcbzrk2kYMw2ViRhqtCD%2Fwvi9D%2BdKI8jXAEC9BWZbpFhLh6iPOEqjoC3ZRzTXXoKQtLSIMyfQKExnqj9YrSWBoaBnnhiaNTm%2FjqH4gm50fRhREil1AgjSuqIHzVnh5HJ0vf6n34cRiRs05HGZKAyTrSDeQEMp2Jo2nTAXD5jYiSnkztZ9698uqT8sG798KQQUZ86O6p%2FYDozV2upzKa1%2FB7EvzdE3BLa%2BVRnq95dpubf6xRDeyY4DTx3KCSK4yym4voXL%2FB3BhA24afT9uZ9uaYgscPS%2Bqs9J7N9YhVykfGcIviiPShImvGFfUisxrgHfXAv7%2F6xMA1%2FUPcg7NDarOMh863UKJKSgduXmNg0N3ZuThX9jmAmnlH0%2BOjw%2BdLj0fDVzQ0FaPRK2Qsvo795FhCRGtstR4vSrgtbBN6eySw%2BL50WsZlsiMYzUVhYTENJcVuvhITPnztMHSHA8fdF2gMG2%2B%2FZG0woU4qlT%2BCmx96uh7WeU2EjvhqIGgSf1CZZhctgBE4uKJZKyCuB9ZmI6ZkmgZEQ5PGrneNwMXKKihrMUyDovVMJnQ8LwGOqUBpPCnfEKpfFYUDYez6xsZI%2BAoxGogxK%2BQFndSk6QAgd07U6lL3UaXGNq8wErlf6PvKnnIRRcQ0hnlU9kgDzLbTBZxB1AdFyW0%2FqUs3ma%2FVZa%2FKRjHhLG2j9sCaeRq2o%2B0HjHdiqCjSvhJfmeZ0oQsdlVjLrTl%2FymMMIAphIiIjv4DV5%2FEIvDzNrDff%2BzbpJ3WzvAuxBlbQAPsNMPYXnq2aDbiJJsT&X-Amz-Signature=7f2a9f5298c28c8af9accc438f2be702bec89d5f79622d51ee475a0111754c13&X-Amz-SignedHeaders=host&x-id=GetObject)

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
