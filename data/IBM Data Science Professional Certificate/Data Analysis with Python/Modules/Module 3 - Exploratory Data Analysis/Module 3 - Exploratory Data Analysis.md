

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466576N7HHA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQD66f0%2FCLwA9V3LPpG%2Fxlt841SH7QEIn1yxagaotQg6AgIgA8vExEm6rLPsnduXplZOttuatd6rmetQwlDjfYrsy2sq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDLQbQ2%2F5uB49U7Ib3ircA3xfOw4gretV%2Fc3GZGgzSC1ZayUZjpalUcDKd5YJr4HBros06xj6emyPTCXJ58JHuop3Xam1T6e%2BETaq2zh8ZG%2BfxahMtEM39y9BLaoGapsKpAbuk%2FXqgtFyPhopLTUHwGVN%2BZmjXWmqgooI%2Fm4plSxMTNMWPADKMl8jW%2BlaTR1UGugPTGj6v%2F%2BHFV7UnSwrg5KTlLUfrRpYV%2BLg8TtL%2FfxDdOkzv3uh6oHtwmA2Qa%2BNID202ULN%2BPGlLo7PYwgyL%2FY8Exq3zKAnk5p9tp5ZYmWwJNDfs0PR%2FOcXxHWjGDX7blcCA8MbSi37x3HOxD3SyZahoTluf6YLEfjdtamH9jblpxal9OzwycU4MG%2FEY%2BqG%2B7A9ufgLDGsCB%2FkSvWxtSoLWpT1rZFOENrWIMPaI1MoDdwjctQrSWkBKn7FN51P%2F%2FPwrx0L3V27iCqY1jvKYgnzRxrrjAkCbfYVj%2B%2F5uBCCa9EGsMcCvs1q3rXINal3E5m6nsQlQDKEzCgn4BcYx1AVGohujptd8Xkk%2BDIj8HJuxnnj%2BHUA02hDP6tg7C5QYesYaFMVhm4aiDfjh%2BJpitlByNsFHTJgChXM%2BxkK7sVXHt4pHWivvbh7LmNODbbLHHDylJRjzoEjLkgixMJ7Kg70GOqUBur0%2BYVD3ky8lFIwB6YHysk18n3fwPMalk3ryRtvWAvVviMMMm4iYI0CAWnkkaz5HrLGhNeqqc3C8Vb3%2FvovqZnankm5cnuu0NC2qqJJAx%2BDLsuLhiSLPkqbJ37P%2FVOhkcIlzQOlH64YQ6j9F3rTTyt1J%2F2AN49fBzrIxBKQO3RNnuLohhZbG5d57PcnVcNOUdnbebYGFCIMTBAe0esu31htTIZBA&X-Amz-Signature=89133bd01e4c06c62eeaab28831bec7ad0c7676cc0c1673089a32759c0041187&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466576N7HHA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQD66f0%2FCLwA9V3LPpG%2Fxlt841SH7QEIn1yxagaotQg6AgIgA8vExEm6rLPsnduXplZOttuatd6rmetQwlDjfYrsy2sq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDLQbQ2%2F5uB49U7Ib3ircA3xfOw4gretV%2Fc3GZGgzSC1ZayUZjpalUcDKd5YJr4HBros06xj6emyPTCXJ58JHuop3Xam1T6e%2BETaq2zh8ZG%2BfxahMtEM39y9BLaoGapsKpAbuk%2FXqgtFyPhopLTUHwGVN%2BZmjXWmqgooI%2Fm4plSxMTNMWPADKMl8jW%2BlaTR1UGugPTGj6v%2F%2BHFV7UnSwrg5KTlLUfrRpYV%2BLg8TtL%2FfxDdOkzv3uh6oHtwmA2Qa%2BNID202ULN%2BPGlLo7PYwgyL%2FY8Exq3zKAnk5p9tp5ZYmWwJNDfs0PR%2FOcXxHWjGDX7blcCA8MbSi37x3HOxD3SyZahoTluf6YLEfjdtamH9jblpxal9OzwycU4MG%2FEY%2BqG%2B7A9ufgLDGsCB%2FkSvWxtSoLWpT1rZFOENrWIMPaI1MoDdwjctQrSWkBKn7FN51P%2F%2FPwrx0L3V27iCqY1jvKYgnzRxrrjAkCbfYVj%2B%2F5uBCCa9EGsMcCvs1q3rXINal3E5m6nsQlQDKEzCgn4BcYx1AVGohujptd8Xkk%2BDIj8HJuxnnj%2BHUA02hDP6tg7C5QYesYaFMVhm4aiDfjh%2BJpitlByNsFHTJgChXM%2BxkK7sVXHt4pHWivvbh7LmNODbbLHHDylJRjzoEjLkgixMJ7Kg70GOqUBur0%2BYVD3ky8lFIwB6YHysk18n3fwPMalk3ryRtvWAvVviMMMm4iYI0CAWnkkaz5HrLGhNeqqc3C8Vb3%2FvovqZnankm5cnuu0NC2qqJJAx%2BDLsuLhiSLPkqbJ37P%2FVOhkcIlzQOlH64YQ6j9F3rTTyt1J%2F2AN49fBzrIxBKQO3RNnuLohhZbG5d57PcnVcNOUdnbebYGFCIMTBAe0esu31htTIZBA&X-Amz-Signature=9d6e07bbaf4893f547f60cb5e99cc675ab8c7c54831e59b5ae2800e4aaa50cb0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466576N7HHA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQD66f0%2FCLwA9V3LPpG%2Fxlt841SH7QEIn1yxagaotQg6AgIgA8vExEm6rLPsnduXplZOttuatd6rmetQwlDjfYrsy2sq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDLQbQ2%2F5uB49U7Ib3ircA3xfOw4gretV%2Fc3GZGgzSC1ZayUZjpalUcDKd5YJr4HBros06xj6emyPTCXJ58JHuop3Xam1T6e%2BETaq2zh8ZG%2BfxahMtEM39y9BLaoGapsKpAbuk%2FXqgtFyPhopLTUHwGVN%2BZmjXWmqgooI%2Fm4plSxMTNMWPADKMl8jW%2BlaTR1UGugPTGj6v%2F%2BHFV7UnSwrg5KTlLUfrRpYV%2BLg8TtL%2FfxDdOkzv3uh6oHtwmA2Qa%2BNID202ULN%2BPGlLo7PYwgyL%2FY8Exq3zKAnk5p9tp5ZYmWwJNDfs0PR%2FOcXxHWjGDX7blcCA8MbSi37x3HOxD3SyZahoTluf6YLEfjdtamH9jblpxal9OzwycU4MG%2FEY%2BqG%2B7A9ufgLDGsCB%2FkSvWxtSoLWpT1rZFOENrWIMPaI1MoDdwjctQrSWkBKn7FN51P%2F%2FPwrx0L3V27iCqY1jvKYgnzRxrrjAkCbfYVj%2B%2F5uBCCa9EGsMcCvs1q3rXINal3E5m6nsQlQDKEzCgn4BcYx1AVGohujptd8Xkk%2BDIj8HJuxnnj%2BHUA02hDP6tg7C5QYesYaFMVhm4aiDfjh%2BJpitlByNsFHTJgChXM%2BxkK7sVXHt4pHWivvbh7LmNODbbLHHDylJRjzoEjLkgixMJ7Kg70GOqUBur0%2BYVD3ky8lFIwB6YHysk18n3fwPMalk3ryRtvWAvVviMMMm4iYI0CAWnkkaz5HrLGhNeqqc3C8Vb3%2FvovqZnankm5cnuu0NC2qqJJAx%2BDLsuLhiSLPkqbJ37P%2FVOhkcIlzQOlH64YQ6j9F3rTTyt1J%2F2AN49fBzrIxBKQO3RNnuLohhZbG5d57PcnVcNOUdnbebYGFCIMTBAe0esu31htTIZBA&X-Amz-Signature=32d461e1d8442f010e6abcd4650fc74b68d51517d8e4b3c77cd42ebc1ec7ecf6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F3BY7ZK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICM%2FLofstXcdpJXKoOChSW2wL59UBjIhi3eJG%2Br3YVi9AiAdQDb96aUQ%2F3p8bIbiHXcGSVVs6yRfVriA7oNZkAD1Fir%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMs%2BB1o0JCvQbzUHiDKtwDAgdN2FzHo18VeW1oGhZLopU1VVoom1y8Z4oFxp51%2BFi%2F8UDErNPmXs8cOw9dhzn0octpHWKvpKhyJbjMfQZ%2FbJbdv9kyQEH36LoJwLrKWAxKLMkKsvP2T%2F3iPw3f6PnyC2NBIW%2BvudFSQe1SKnYPAJ%2B3HhicIHlYO3Wq1KRC5EYgovjmRmVFMqqnCztIvLEh2Y6VhSvDkDBujs%2B2mMY6KwRwg01HKszLA4NiFN5W1YXTgy3Rx7mgtXEgxa%2FqYtERhwSVsW1dF9oEbT2jWujq6B%2F1rHdpEOpCsnb8bAk5zXCi1Jsp6KXMLlu4sqjeJ8o89Y%2ByD06XECvZYbLAuhLdgb5bRg%2BisAVRdrBEOk1LFSED2lasRuLeawQGZkubGOsDB6m6oBeOAGcODEEOj%2B5kywkcvgjT3nwUtMxYGTScZZVb8KgQiJCQGhd%2BRis5n6e5lnAu8WfB9M1UUiERACQl2qbGDhYNvoc8c4n4Yf3SCpbBS1YbrhgYKz%2F8H1dL%2BhOh6XMCNSOIIcx6BF2iVDVb3Bl3mDbkgrwagK5hvyLD%2B8nVxEdghP0mGrAsWjwTHNpe8k%2FX4CGur3ePsVH%2BL0B7eI%2BzhUBYbbAUmZbQ%2BsTfY88R8T1K5N5Qqxr9Czsww8qDvQY6pgHlPEDP%2Bf8Z3%2BAwZEM2K1saGnUo7j4Tj21GuNi5FweVSfn6or8t7SKpXD%2BcYj5xiJ%2Fs4QViCN05r6JdwVrJL0GamhCUg%2BcLYH7ymtMPzV%2FG3Ahxq18PzdcPfreNeoL9K4paW6hbCMKmwSackJKj%2BkevEPQKHy%2FysBaRJQPzFl2YLH37RNpe7U4%2BYDBY0724IdH074MEWp8TdT0jPOVM8ZpnhPcXIMfm&X-Amz-Signature=496638eb453a51b716bae8ce7317daf6d6b545d45b8a7d43ad1a2c3a14a1dfa2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F3BY7ZK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICM%2FLofstXcdpJXKoOChSW2wL59UBjIhi3eJG%2Br3YVi9AiAdQDb96aUQ%2F3p8bIbiHXcGSVVs6yRfVriA7oNZkAD1Fir%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMs%2BB1o0JCvQbzUHiDKtwDAgdN2FzHo18VeW1oGhZLopU1VVoom1y8Z4oFxp51%2BFi%2F8UDErNPmXs8cOw9dhzn0octpHWKvpKhyJbjMfQZ%2FbJbdv9kyQEH36LoJwLrKWAxKLMkKsvP2T%2F3iPw3f6PnyC2NBIW%2BvudFSQe1SKnYPAJ%2B3HhicIHlYO3Wq1KRC5EYgovjmRmVFMqqnCztIvLEh2Y6VhSvDkDBujs%2B2mMY6KwRwg01HKszLA4NiFN5W1YXTgy3Rx7mgtXEgxa%2FqYtERhwSVsW1dF9oEbT2jWujq6B%2F1rHdpEOpCsnb8bAk5zXCi1Jsp6KXMLlu4sqjeJ8o89Y%2ByD06XECvZYbLAuhLdgb5bRg%2BisAVRdrBEOk1LFSED2lasRuLeawQGZkubGOsDB6m6oBeOAGcODEEOj%2B5kywkcvgjT3nwUtMxYGTScZZVb8KgQiJCQGhd%2BRis5n6e5lnAu8WfB9M1UUiERACQl2qbGDhYNvoc8c4n4Yf3SCpbBS1YbrhgYKz%2F8H1dL%2BhOh6XMCNSOIIcx6BF2iVDVb3Bl3mDbkgrwagK5hvyLD%2B8nVxEdghP0mGrAsWjwTHNpe8k%2FX4CGur3ePsVH%2BL0B7eI%2BzhUBYbbAUmZbQ%2BsTfY88R8T1K5N5Qqxr9Czsww8qDvQY6pgHlPEDP%2Bf8Z3%2BAwZEM2K1saGnUo7j4Tj21GuNi5FweVSfn6or8t7SKpXD%2BcYj5xiJ%2Fs4QViCN05r6JdwVrJL0GamhCUg%2BcLYH7ymtMPzV%2FG3Ahxq18PzdcPfreNeoL9K4paW6hbCMKmwSackJKj%2BkevEPQKHy%2FysBaRJQPzFl2YLH37RNpe7U4%2BYDBY0724IdH074MEWp8TdT0jPOVM8ZpnhPcXIMfm&X-Amz-Signature=2a06032914c710bac3a006eab030d5eb5d197fe3932f54ef5a51e340bcb029d8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F3BY7ZK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICM%2FLofstXcdpJXKoOChSW2wL59UBjIhi3eJG%2Br3YVi9AiAdQDb96aUQ%2F3p8bIbiHXcGSVVs6yRfVriA7oNZkAD1Fir%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMs%2BB1o0JCvQbzUHiDKtwDAgdN2FzHo18VeW1oGhZLopU1VVoom1y8Z4oFxp51%2BFi%2F8UDErNPmXs8cOw9dhzn0octpHWKvpKhyJbjMfQZ%2FbJbdv9kyQEH36LoJwLrKWAxKLMkKsvP2T%2F3iPw3f6PnyC2NBIW%2BvudFSQe1SKnYPAJ%2B3HhicIHlYO3Wq1KRC5EYgovjmRmVFMqqnCztIvLEh2Y6VhSvDkDBujs%2B2mMY6KwRwg01HKszLA4NiFN5W1YXTgy3Rx7mgtXEgxa%2FqYtERhwSVsW1dF9oEbT2jWujq6B%2F1rHdpEOpCsnb8bAk5zXCi1Jsp6KXMLlu4sqjeJ8o89Y%2ByD06XECvZYbLAuhLdgb5bRg%2BisAVRdrBEOk1LFSED2lasRuLeawQGZkubGOsDB6m6oBeOAGcODEEOj%2B5kywkcvgjT3nwUtMxYGTScZZVb8KgQiJCQGhd%2BRis5n6e5lnAu8WfB9M1UUiERACQl2qbGDhYNvoc8c4n4Yf3SCpbBS1YbrhgYKz%2F8H1dL%2BhOh6XMCNSOIIcx6BF2iVDVb3Bl3mDbkgrwagK5hvyLD%2B8nVxEdghP0mGrAsWjwTHNpe8k%2FX4CGur3ePsVH%2BL0B7eI%2BzhUBYbbAUmZbQ%2BsTfY88R8T1K5N5Qqxr9Czsww8qDvQY6pgHlPEDP%2Bf8Z3%2BAwZEM2K1saGnUo7j4Tj21GuNi5FweVSfn6or8t7SKpXD%2BcYj5xiJ%2Fs4QViCN05r6JdwVrJL0GamhCUg%2BcLYH7ymtMPzV%2FG3Ahxq18PzdcPfreNeoL9K4paW6hbCMKmwSackJKj%2BkevEPQKHy%2FysBaRJQPzFl2YLH37RNpe7U4%2BYDBY0724IdH074MEWp8TdT0jPOVM8ZpnhPcXIMfm&X-Amz-Signature=9bd8e89742c4592b4dd8a9b901b8e14a30f122876c550d4953da012699da67e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F3BY7ZK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICM%2FLofstXcdpJXKoOChSW2wL59UBjIhi3eJG%2Br3YVi9AiAdQDb96aUQ%2F3p8bIbiHXcGSVVs6yRfVriA7oNZkAD1Fir%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMs%2BB1o0JCvQbzUHiDKtwDAgdN2FzHo18VeW1oGhZLopU1VVoom1y8Z4oFxp51%2BFi%2F8UDErNPmXs8cOw9dhzn0octpHWKvpKhyJbjMfQZ%2FbJbdv9kyQEH36LoJwLrKWAxKLMkKsvP2T%2F3iPw3f6PnyC2NBIW%2BvudFSQe1SKnYPAJ%2B3HhicIHlYO3Wq1KRC5EYgovjmRmVFMqqnCztIvLEh2Y6VhSvDkDBujs%2B2mMY6KwRwg01HKszLA4NiFN5W1YXTgy3Rx7mgtXEgxa%2FqYtERhwSVsW1dF9oEbT2jWujq6B%2F1rHdpEOpCsnb8bAk5zXCi1Jsp6KXMLlu4sqjeJ8o89Y%2ByD06XECvZYbLAuhLdgb5bRg%2BisAVRdrBEOk1LFSED2lasRuLeawQGZkubGOsDB6m6oBeOAGcODEEOj%2B5kywkcvgjT3nwUtMxYGTScZZVb8KgQiJCQGhd%2BRis5n6e5lnAu8WfB9M1UUiERACQl2qbGDhYNvoc8c4n4Yf3SCpbBS1YbrhgYKz%2F8H1dL%2BhOh6XMCNSOIIcx6BF2iVDVb3Bl3mDbkgrwagK5hvyLD%2B8nVxEdghP0mGrAsWjwTHNpe8k%2FX4CGur3ePsVH%2BL0B7eI%2BzhUBYbbAUmZbQ%2BsTfY88R8T1K5N5Qqxr9Czsww8qDvQY6pgHlPEDP%2Bf8Z3%2BAwZEM2K1saGnUo7j4Tj21GuNi5FweVSfn6or8t7SKpXD%2BcYj5xiJ%2Fs4QViCN05r6JdwVrJL0GamhCUg%2BcLYH7ymtMPzV%2FG3Ahxq18PzdcPfreNeoL9K4paW6hbCMKmwSackJKj%2BkevEPQKHy%2FysBaRJQPzFl2YLH37RNpe7U4%2BYDBY0724IdH074MEWp8TdT0jPOVM8ZpnhPcXIMfm&X-Amz-Signature=139332b068cd1ce0d064c2de965496306571ec2fd05475e89361770fe116aff8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F3BY7ZK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICM%2FLofstXcdpJXKoOChSW2wL59UBjIhi3eJG%2Br3YVi9AiAdQDb96aUQ%2F3p8bIbiHXcGSVVs6yRfVriA7oNZkAD1Fir%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMs%2BB1o0JCvQbzUHiDKtwDAgdN2FzHo18VeW1oGhZLopU1VVoom1y8Z4oFxp51%2BFi%2F8UDErNPmXs8cOw9dhzn0octpHWKvpKhyJbjMfQZ%2FbJbdv9kyQEH36LoJwLrKWAxKLMkKsvP2T%2F3iPw3f6PnyC2NBIW%2BvudFSQe1SKnYPAJ%2B3HhicIHlYO3Wq1KRC5EYgovjmRmVFMqqnCztIvLEh2Y6VhSvDkDBujs%2B2mMY6KwRwg01HKszLA4NiFN5W1YXTgy3Rx7mgtXEgxa%2FqYtERhwSVsW1dF9oEbT2jWujq6B%2F1rHdpEOpCsnb8bAk5zXCi1Jsp6KXMLlu4sqjeJ8o89Y%2ByD06XECvZYbLAuhLdgb5bRg%2BisAVRdrBEOk1LFSED2lasRuLeawQGZkubGOsDB6m6oBeOAGcODEEOj%2B5kywkcvgjT3nwUtMxYGTScZZVb8KgQiJCQGhd%2BRis5n6e5lnAu8WfB9M1UUiERACQl2qbGDhYNvoc8c4n4Yf3SCpbBS1YbrhgYKz%2F8H1dL%2BhOh6XMCNSOIIcx6BF2iVDVb3Bl3mDbkgrwagK5hvyLD%2B8nVxEdghP0mGrAsWjwTHNpe8k%2FX4CGur3ePsVH%2BL0B7eI%2BzhUBYbbAUmZbQ%2BsTfY88R8T1K5N5Qqxr9Czsww8qDvQY6pgHlPEDP%2Bf8Z3%2BAwZEM2K1saGnUo7j4Tj21GuNi5FweVSfn6or8t7SKpXD%2BcYj5xiJ%2Fs4QViCN05r6JdwVrJL0GamhCUg%2BcLYH7ymtMPzV%2FG3Ahxq18PzdcPfreNeoL9K4paW6hbCMKmwSackJKj%2BkevEPQKHy%2FysBaRJQPzFl2YLH37RNpe7U4%2BYDBY0724IdH074MEWp8TdT0jPOVM8ZpnhPcXIMfm&X-Amz-Signature=99bc5fcae2ec32ca8aa3a74a4b6bd9f5b49418599700ba0a9b1ca0c9b946f78b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F3BY7ZK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICM%2FLofstXcdpJXKoOChSW2wL59UBjIhi3eJG%2Br3YVi9AiAdQDb96aUQ%2F3p8bIbiHXcGSVVs6yRfVriA7oNZkAD1Fir%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMs%2BB1o0JCvQbzUHiDKtwDAgdN2FzHo18VeW1oGhZLopU1VVoom1y8Z4oFxp51%2BFi%2F8UDErNPmXs8cOw9dhzn0octpHWKvpKhyJbjMfQZ%2FbJbdv9kyQEH36LoJwLrKWAxKLMkKsvP2T%2F3iPw3f6PnyC2NBIW%2BvudFSQe1SKnYPAJ%2B3HhicIHlYO3Wq1KRC5EYgovjmRmVFMqqnCztIvLEh2Y6VhSvDkDBujs%2B2mMY6KwRwg01HKszLA4NiFN5W1YXTgy3Rx7mgtXEgxa%2FqYtERhwSVsW1dF9oEbT2jWujq6B%2F1rHdpEOpCsnb8bAk5zXCi1Jsp6KXMLlu4sqjeJ8o89Y%2ByD06XECvZYbLAuhLdgb5bRg%2BisAVRdrBEOk1LFSED2lasRuLeawQGZkubGOsDB6m6oBeOAGcODEEOj%2B5kywkcvgjT3nwUtMxYGTScZZVb8KgQiJCQGhd%2BRis5n6e5lnAu8WfB9M1UUiERACQl2qbGDhYNvoc8c4n4Yf3SCpbBS1YbrhgYKz%2F8H1dL%2BhOh6XMCNSOIIcx6BF2iVDVb3Bl3mDbkgrwagK5hvyLD%2B8nVxEdghP0mGrAsWjwTHNpe8k%2FX4CGur3ePsVH%2BL0B7eI%2BzhUBYbbAUmZbQ%2BsTfY88R8T1K5N5Qqxr9Czsww8qDvQY6pgHlPEDP%2Bf8Z3%2BAwZEM2K1saGnUo7j4Tj21GuNi5FweVSfn6or8t7SKpXD%2BcYj5xiJ%2Fs4QViCN05r6JdwVrJL0GamhCUg%2BcLYH7ymtMPzV%2FG3Ahxq18PzdcPfreNeoL9K4paW6hbCMKmwSackJKj%2BkevEPQKHy%2FysBaRJQPzFl2YLH37RNpe7U4%2BYDBY0724IdH074MEWp8TdT0jPOVM8ZpnhPcXIMfm&X-Amz-Signature=0b7de39eabf724e8c43750c381e99b8701580958b4523e385380d50cc4a7fe23&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HWMH4JE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQCPZITXoqoXojDzYQqFfU3J8U7dbnzIzlWORbEE0zyWbQIhAOQpVSAAwp%2F8YeCsbyBdqyC6DmlgLNKFGBilOHLU7XJ7Kv8DCBkQABoMNjM3NDIzMTgzODA1Igz5Esqgr4G796qbtsMq3AOhl%2FkBzn6CpIsGl5DCYUeGc0KtINv0sC4E6D2dCQzlvbIKakHmpQLnmS%2BvUCrWqv8nflPZcV4H%2FAbfZPZ5LUpgNaFk%2FIJ6tFXANFrKMWhL02YPX0pZGA89Q2ATytd3tj6s1YLpMdNPG4VXyVoG6yLS50cFLWhN%2BPUuht4OVjUbOWv48rpS7ztM6QafQidKuA02uDdw0qxQXeHNv8lzTOk%2FjLuq2UcYKAO%2BizcdM4h5HAgMMHxL%2B2wkY%2F11wAGbuxAgA0%2FQm8%2F%2Fm3V5ANrdAWMmZZqs%2FQ8HGvTjk6oEN4tL%2B7DJmd%2BP1bHfiR%2BuO5b5%2BD1jS7Bk5plue7%2BdidxKO3c4rktSnKcpIRa8ShK9k8R3LfwsdGKrl4Y6DA7E%2FCMHnh6xLpxwTPO9CMhNUGqv%2BUpmLL%2BmfAzrCPeCq7CyGWJ47m3RcgBvnkyZLmoHdE9NSSa13DHF682ft07CX4PN0VK3nOJoK4ZHdp%2FkbkJDQ%2BCSgk%2BN7m3jbEsMu%2FQFxwT3Yrqtbnd2IuOfTOwJ1W%2B6yCnmzmM7Mcszw7uKrBM%2BuSGBvSMEmIQEvZBpo3K4V1vHui%2FlaanMJoVDXkliv5S4sIRJMYgA09O8enonPVRLjnk%2FbcJl3htzqT2XbUxtzDDDyoO9BjqkAWwHzJfggRif%2BnaqH8YzbpThDvgTuicodqAblt16HgAhzgKml8KpJ5AThNtlQ%2FNwK9Y0Pi%2FIJdsaSUUnDhhUXScXt35ZxUhe%2FfLCmtJohbRK210zjfrcQeEvZGM6sAjYhOgOZ%2FOpiEk2oLARtWRok0sAObKJSfFXHUiwp4VWfGQSvyptoXowin83rUHFoXMudw6nFbvvsC72%2Byr1ow4WM5ZtBnS2&X-Amz-Signature=f98b66229d3a67aec6992a67b63c4d191035e43c2ce06b43e2cf5448ba180b71&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662BQREVL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICvmyKx44KfE57Yp%2F7D5uJj66wo8ugSxfbh1IAHPVMl1AiAGcvShpMynpj%2FX6R5eziFwrH9eJ6ehsDPUf5tF2BrOTCr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMOYIr8xwu%2BXiqIDHfKtwD%2FXJ7SptSsbo7DZd7RlJA4Mk6j1KiSsCRSaylv9qe7VTiCReFW5ad64T1ApH5vrFiRWnBSJHj%2BJRKsHtQNw0j18fkjmFGA976zgQFenZLFOZOO%2BK0zprjyiBs7UB2X4HSJFLU36zztSAUlQLD0tn3XFPmH36VzyKa2iVP9EPW7hRkECvs0tZUdEUaZfRQA7%2FNiOyZm514z7xKkfEpu2FQYXlEFR4nJwcDs3hY7wJNmaJlDbOqSvmgjTHUPsn8qHbwLTsM0HcU3vCibVMkS0SVavtK6sjN9wAWoLUjRl%2FF%2B9DNfLMkP5OWWmQcCGr2BzuIUeEwKU%2BFEjneT99r9yP%2F9LAUycjauuPPm6FG2i4UQvgWIyBkRyPBy0ehLud7On9oPKxBvt97XPXBM%2BkivO2lymN0AHvpMtq8mnGnec0c%2ByVT8b0TI1qnZtKzZvPPRcN2GqYytqwAQQUbgNDwoKhHAIF7IDEn8odEWZT1GTiO%2FSpgJYgN%2Fag9QGEGT8ULD5GY8oQ99dnqLkXG6JyRWA6s3WxX4bEBgaGI0bgPlCknIGLC66ShXGMLEkJ8%2BBasklOOjEAPoiElqts8w81jV%2Bh5qJEgkAXeaP1n9nZ1vZcr5ny0V%2FLI1m8wr5%2B%2BaSUwpsqDvQY6pgH7o0dp664TlhwQnLn0662QQ%2BE1S9Gc4B7g7SB9GEksG4Cxk2K035Ir1ZMSJiywkbt3e7D005Cv5mrW1BDEYmvpyxWkVUwSMA%2BcHL1Cqg4KwIJW1FmLFRFxwuHEtW2otVx4RbFoiQoE%2Fhgz7vUa4HW9jGyc2gPiDGbHnYA%2Fb1rCdJVnfisg8%2B%2FV%2F7O8l6qezxdLIFv1P5XoWO2RSD1DD56Twkc3wqkk&X-Amz-Signature=04772164c7b9124d3c70b2da774f49d6c2885f23dd7035939a18f23dea2709c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F3BY7ZK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICM%2FLofstXcdpJXKoOChSW2wL59UBjIhi3eJG%2Br3YVi9AiAdQDb96aUQ%2F3p8bIbiHXcGSVVs6yRfVriA7oNZkAD1Fir%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMs%2BB1o0JCvQbzUHiDKtwDAgdN2FzHo18VeW1oGhZLopU1VVoom1y8Z4oFxp51%2BFi%2F8UDErNPmXs8cOw9dhzn0octpHWKvpKhyJbjMfQZ%2FbJbdv9kyQEH36LoJwLrKWAxKLMkKsvP2T%2F3iPw3f6PnyC2NBIW%2BvudFSQe1SKnYPAJ%2B3HhicIHlYO3Wq1KRC5EYgovjmRmVFMqqnCztIvLEh2Y6VhSvDkDBujs%2B2mMY6KwRwg01HKszLA4NiFN5W1YXTgy3Rx7mgtXEgxa%2FqYtERhwSVsW1dF9oEbT2jWujq6B%2F1rHdpEOpCsnb8bAk5zXCi1Jsp6KXMLlu4sqjeJ8o89Y%2ByD06XECvZYbLAuhLdgb5bRg%2BisAVRdrBEOk1LFSED2lasRuLeawQGZkubGOsDB6m6oBeOAGcODEEOj%2B5kywkcvgjT3nwUtMxYGTScZZVb8KgQiJCQGhd%2BRis5n6e5lnAu8WfB9M1UUiERACQl2qbGDhYNvoc8c4n4Yf3SCpbBS1YbrhgYKz%2F8H1dL%2BhOh6XMCNSOIIcx6BF2iVDVb3Bl3mDbkgrwagK5hvyLD%2B8nVxEdghP0mGrAsWjwTHNpe8k%2FX4CGur3ePsVH%2BL0B7eI%2BzhUBYbbAUmZbQ%2BsTfY88R8T1K5N5Qqxr9Czsww8qDvQY6pgHlPEDP%2Bf8Z3%2BAwZEM2K1saGnUo7j4Tj21GuNi5FweVSfn6or8t7SKpXD%2BcYj5xiJ%2Fs4QViCN05r6JdwVrJL0GamhCUg%2BcLYH7ymtMPzV%2FG3Ahxq18PzdcPfreNeoL9K4paW6hbCMKmwSackJKj%2BkevEPQKHy%2FysBaRJQPzFl2YLH37RNpe7U4%2BYDBY0724IdH074MEWp8TdT0jPOVM8ZpnhPcXIMfm&X-Amz-Signature=87bc30574245bff5516b7b672fd7d26d0a2ecbeed48d887d8e81918fe2c84765&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F3BY7ZK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICM%2FLofstXcdpJXKoOChSW2wL59UBjIhi3eJG%2Br3YVi9AiAdQDb96aUQ%2F3p8bIbiHXcGSVVs6yRfVriA7oNZkAD1Fir%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMs%2BB1o0JCvQbzUHiDKtwDAgdN2FzHo18VeW1oGhZLopU1VVoom1y8Z4oFxp51%2BFi%2F8UDErNPmXs8cOw9dhzn0octpHWKvpKhyJbjMfQZ%2FbJbdv9kyQEH36LoJwLrKWAxKLMkKsvP2T%2F3iPw3f6PnyC2NBIW%2BvudFSQe1SKnYPAJ%2B3HhicIHlYO3Wq1KRC5EYgovjmRmVFMqqnCztIvLEh2Y6VhSvDkDBujs%2B2mMY6KwRwg01HKszLA4NiFN5W1YXTgy3Rx7mgtXEgxa%2FqYtERhwSVsW1dF9oEbT2jWujq6B%2F1rHdpEOpCsnb8bAk5zXCi1Jsp6KXMLlu4sqjeJ8o89Y%2ByD06XECvZYbLAuhLdgb5bRg%2BisAVRdrBEOk1LFSED2lasRuLeawQGZkubGOsDB6m6oBeOAGcODEEOj%2B5kywkcvgjT3nwUtMxYGTScZZVb8KgQiJCQGhd%2BRis5n6e5lnAu8WfB9M1UUiERACQl2qbGDhYNvoc8c4n4Yf3SCpbBS1YbrhgYKz%2F8H1dL%2BhOh6XMCNSOIIcx6BF2iVDVb3Bl3mDbkgrwagK5hvyLD%2B8nVxEdghP0mGrAsWjwTHNpe8k%2FX4CGur3ePsVH%2BL0B7eI%2BzhUBYbbAUmZbQ%2BsTfY88R8T1K5N5Qqxr9Czsww8qDvQY6pgHlPEDP%2Bf8Z3%2BAwZEM2K1saGnUo7j4Tj21GuNi5FweVSfn6or8t7SKpXD%2BcYj5xiJ%2Fs4QViCN05r6JdwVrJL0GamhCUg%2BcLYH7ymtMPzV%2FG3Ahxq18PzdcPfreNeoL9K4paW6hbCMKmwSackJKj%2BkevEPQKHy%2FysBaRJQPzFl2YLH37RNpe7U4%2BYDBY0724IdH074MEWp8TdT0jPOVM8ZpnhPcXIMfm&X-Amz-Signature=697641ae264a533fff8f52996a71a2c5123d55b5aad4f048813b144f06522f1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F3BY7ZK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICM%2FLofstXcdpJXKoOChSW2wL59UBjIhi3eJG%2Br3YVi9AiAdQDb96aUQ%2F3p8bIbiHXcGSVVs6yRfVriA7oNZkAD1Fir%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMs%2BB1o0JCvQbzUHiDKtwDAgdN2FzHo18VeW1oGhZLopU1VVoom1y8Z4oFxp51%2BFi%2F8UDErNPmXs8cOw9dhzn0octpHWKvpKhyJbjMfQZ%2FbJbdv9kyQEH36LoJwLrKWAxKLMkKsvP2T%2F3iPw3f6PnyC2NBIW%2BvudFSQe1SKnYPAJ%2B3HhicIHlYO3Wq1KRC5EYgovjmRmVFMqqnCztIvLEh2Y6VhSvDkDBujs%2B2mMY6KwRwg01HKszLA4NiFN5W1YXTgy3Rx7mgtXEgxa%2FqYtERhwSVsW1dF9oEbT2jWujq6B%2F1rHdpEOpCsnb8bAk5zXCi1Jsp6KXMLlu4sqjeJ8o89Y%2ByD06XECvZYbLAuhLdgb5bRg%2BisAVRdrBEOk1LFSED2lasRuLeawQGZkubGOsDB6m6oBeOAGcODEEOj%2B5kywkcvgjT3nwUtMxYGTScZZVb8KgQiJCQGhd%2BRis5n6e5lnAu8WfB9M1UUiERACQl2qbGDhYNvoc8c4n4Yf3SCpbBS1YbrhgYKz%2F8H1dL%2BhOh6XMCNSOIIcx6BF2iVDVb3Bl3mDbkgrwagK5hvyLD%2B8nVxEdghP0mGrAsWjwTHNpe8k%2FX4CGur3ePsVH%2BL0B7eI%2BzhUBYbbAUmZbQ%2BsTfY88R8T1K5N5Qqxr9Czsww8qDvQY6pgHlPEDP%2Bf8Z3%2BAwZEM2K1saGnUo7j4Tj21GuNi5FweVSfn6or8t7SKpXD%2BcYj5xiJ%2Fs4QViCN05r6JdwVrJL0GamhCUg%2BcLYH7ymtMPzV%2FG3Ahxq18PzdcPfreNeoL9K4paW6hbCMKmwSackJKj%2BkevEPQKHy%2FysBaRJQPzFl2YLH37RNpe7U4%2BYDBY0724IdH074MEWp8TdT0jPOVM8ZpnhPcXIMfm&X-Amz-Signature=f2e84a1aa64204a686602cae8ed1110e0b7db941a82a0f1361b260d8f62a82be&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663J65P3XX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIBZ6srv9lY43%2BN5vn50%2BJPCPXyHNNChQ6FcxlpTPDG7WAiEAp11uSVY8SRwfMrXlw4CEMMa%2B0I5wO1025nstfjwCwL8q%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDIGyTfBIQsG95xAP5ircAzMfjRfhdcGqRLvMuPX81dQaBD3xVfU%2BGT10Oz4ObGSGSZHcpMdHjPty4A7FqpdAGqYr6ge3ZSSgMUtIdaDtJhTd1Dl%2BlQtr7qi%2BdW%2Foik7npX6kh9JLj9o%2B6EvtsMTvpJexBM7o36fazgcEJ5GiI78WhwyH0%2Fn9gb4GZDmThmnzAw494XOb7Jp8k9zkfSltXw2DQAblTGSl%2BFKtjuFtNG4ml4jQNzHGspN5ha%2BLCfAkvLs9GxIvCRqm3ZGmL8yp6wZiC2qWHcobNvecHt43lEi9an3p7zVUXa2tRv1epkXhxk7ZBJBpR4zwjVRJU%2FF3bpcT8ExvoWvM8FB7BlWn4w0z%2F3skxxEOvNq2vf1yiDa%2F7MpNnKMnyZM3iLMspOWTeubAIT6EDYETPp%2BrGa6gMBsdDyxZRu9SRxgl%2FNY1hwV2r0j%2FQj3RanQ0HIF2sh4W4EsVq7X4X8LfCb3iuZqJCWstDcMzNtSuFveI%2F8Mf0dLqr3S6p%2FqKz8P2xwc0JLkV6o%2BjreCadU2yIV7TXkLom5cOQZaxgBR8cwLkvupc5q9RoC5ZSuQ6%2FkYhjoxtBRKel5S8X%2FqUr23df1wCfXi5q8dUWQRhwZj0yqqHb4nvdHaxcTo8Hof5JIvd4pXsMM7Kg70GOqUBxZFneEsz6Cmy%2BbBn24keQpvRtjWblee9RBw4Y8hgYQGUr7EL5i5inpbLN7vTPB1pOED%2FF7C4CBNN2p1fHjUw4%2FfgnXF2EHSOQCU54WBKc0t6dJVQ4MG1roGZ8OYQwkveUQ4PcXiN1M82IuOGxe9q2cBiXNWkF36upYrnie8jJSGoCaE%2BDJ5MSl2SFZ25JX3m86DITadC2VNiEGw0JNbWBENIm8%2Fu&X-Amz-Signature=238bda420c1fdf27fa982c52d20b09507a05a801be42a2b69fa756948f1ae76c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYADGNDC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQCzJX9k9GjT5y3yBhNKiSSp1KJk2uibOH3fXO%2Fbhnm8fgIhAOAQzyB9nT7pzb%2Bb4O%2B9ynDCwq0xKj3v5HD5omXUC9aRKv8DCBkQABoMNjM3NDIzMTgzODA1IgyBF636kNQy7HjnGhUq3AN4GYOHp%2BsP7F35V1siISFTo0BStMmY5Lz1iTwbbhmH8odHOWyDZa1bWhRZIXNIprpkCkbSf%2FeqPo3kzP4%2BLT%2FCrkszAWKV6tdqvyrvLoh3dfkqLSIEhXkFSvvY28Qg%2FsKP23JCpDJwGrA2r6fIam0nbJozgUxxvcbxi1wwq%2BtT9nHnGuhxPRvTxFU2ADH0hOn0HmaU54CraVX2YrE6aMdlW20SYOr2XKmg9SCXRG3QMUYbguy13YvD0sjEYn79FBh%2Bl8JCCpCstH1pG2nwbjA6C8E5Z5lDqzmrejTv8yuCpMzRuX7o44%2Bzh5jmoSrUwr8FflyiYYdozwu5AENO%2F77gYlUWLxIoK5xPkzROdec39v8CVPpVRv%2F0GcE0SgLYe4zN%2FdiMRqjLwfopU114okbn4LtFhF21Jh4W6vQGpQgjS5fZmUL55N1T%2BkBMKAXWxMz1v1rZs%2FdFd1jAj7kurOQaOQJnTg51Y%2FAxX69ZdYJ8xUa3lL5RSOdAfY7rnjhe6w%2FX%2FCmuHB%2Fe5cMhXlzbvGGIxImT4wOzc5QW7i45JOjWdPQztDrz00VjSj%2Bjv5Mq48fD0yMzYYU%2FBAMu66wuw0qYE%2Fej5Uqyd2eNdjonLoIE4t7DGpMHBIuzhIU8YTDByoO9BjqkAV8r2pEqj2TIL3XIc%2By4ShSGLLXef%2FO25ToL0zHl8G4nBpN4uNBR5cRVCHXobPqJbfHR003kHu53E9uzjMvsfPC7KJE2x3FzTUbJ3RjLBGd5kND5NEIPXfUWePb8iPAsPz39flNSWmSjk6Cj2fAjIGrZCxY1klYv4EiuFG6UBK8vbo4pJVubSwxxztlIBWHxXLe6VBeX9LOMkPe4zDHOlgB66wBV&X-Amz-Signature=14b97aebf2780357310b1d51d33248d520708aa754ed2465076968a815c4f148&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTNCMQD4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQCLHSuz7SYiYtv%2BnO0FnITL0cuCWp%2Fkhm7nKdIcqO8HXgIhAIDjSTMe4uIPdSbqTgkKAhZ50emBMoDDiajTRcx69KfFKv8DCBkQABoMNjM3NDIzMTgzODA1IgyYRo59nBaTyLsaenUq3AOxadyrRYHyoEuahKRp1FniVcfSZfDg4Czxk64FjmeaIMMwypzUfu0EnA%2Fpa6e8DpoF9iUBOqrWvKsLwSCikHmeLfVcgeOXGxm2gz2Xcy5U8It6OpSzjIvd2YqCQE88Vcoootpf6TplybC77%2FTXZ12Xf1H%2FYKHc1406EMpO8aTPz7j7MStMLlbXRYiwB%2FZSfS%2BPXU%2BlrSgBxSuCixfxSKOezuLO9t1AvnHXPL6PF8MS75tmtygaF1bpweVG6R33vnW8pfob9r1TbxLDBS6QnSd8Bys9zzWDLPo1l25VFDwxN07VHlRJtyf%2FrqsMVyCP9G4x5JMpxLhLGrhDCNpyMFe496WLuzM0eb%2B%2BDtHS7eD6QEp3lhZY8DDxxV9QjSU6otD9bFng5U4Fvwy2eZqWmkk9U%2BCtORzssw1E3BrVWc1y2iARZohgo3B9ij0dw6lVzv8SWt8mknlbT0%2FEE8NBVuwjVd1X1o8C0pvgFhWeZhFqsu%2BNBNf8wV96I9g5UOiqo37wvJskLXus1Ocoxo6uaAmRvjpNqy4Ex%2FF6Ghw%2B0QUBSzoP2H8RBukqDPs8jVoGPX4Val3rLY5L1vN2J0Z3RqR5zdfvYz1y8KfK0qADg7Cj7MgIGZjG9h3bi5cBozCuyoO9BjqkAVHMr7DYCVPcf9wG6OGB%2FEkBrT6y6O%2BO8PExAiZghG7YUO7LXCbz3TPNStqXnFMLwJK6IyR%2FoH0E4CiLKqEJcs7ghryuc3z692bvz8ZN5KJ8gXnRQdOGKDsrBjIhaT1fA7PK9tU41a95R2YTkBkBJGWDCRar%2BCdab2LWMXELeQUNzB7l7k3%2Bv9nLmTiB9IpZypNRCEqOhywO8OJ%2FQ6c5vnN6UjXT&X-Amz-Signature=ef9ebf86a79b1c420f3ba0b9708d0874cec8d0b555d862edddf9e4e6a8b57cd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCBANH4D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIExxGKHnVdCNfTeWPhlJ8LuBB4H6sXQS%2BJQFYP33I3EDAiEAhIUzfKkfTKVV6zqABWd1sKyZtYhydiHbDqeBTR8MHqIq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDLGdS7wFM6WGE%2FtNtyrcAxTw0Nq76gjiJPHkVfLBmKTeu5dXSZdYZln9IOiTriPL%2Bv5GWjbHhs%2BCVzNMFUyOeVrHpIKMDiwB5ttDX3v1HRLLnWc%2FfI63BAw4VRpkZUv1vGiboyf7ek1FlzMa741CRE3PzWJ2eN%2FE5Ced%2Fg1wMNKMRoymoWYx0oeBBZITFOsY2fYLwOQH75fl7Pup2ZgKvV2yVJJwpAcvdA%2FtthDJtVWHS6KSgbOgViOIpsA0CqN8%2F7XIBqekD5zlQiVI5Sx5Nar88zXQS5iExPVCrGgYBxJqCMY%2B9Qv9JpEVJTiT%2BzJLKcbSDRIJW2DrN5m2cGQqKXrJBvnQTI5fVgDst2yGsWvINJ0Jz%2BJs7gVSLbJkJZoo%2FagulEEnLrPpQ8AZM2Zu5%2FO5WGztHk6a8eLANvW0dLMf4WrYQOkskYLOf8ZWcfZnn8MltRUqfU0mC8nYt%2Be9phm6JgfK61UinBa%2FxZUh9bNBz5VldjvjP%2BEWQsRgTiSPxjgApEi4NmQ0bTWiOGXwkwQt5L4LOBPS0Bt2h%2BktcEky4WUZxBhklrHDH2YwkWouU%2Bk7aNB1Y5zkh4hXgLXdWqeOE%2Fg7YL%2BnR5YEE7qb5F3av1%2FKZCJ959oILoAnYWL4f5wJ0016MebT50kbMNPKg70GOqUBdccWxOfTwQVotgX3SD0pKv%2FMG4lKkePSz%2BxQJ%2FSNS4cSqpDmcaQe964l0y6qFKIJz4f2O%2BPbVs00z2xE7PPJt5aus2GLOyYuSAQg3aV10IbWfwfnFuofm1wKWEGyVF7giLgfku7jxyAtMnn0xE7DIETYpaW5aUaKnxhXk5LaZgcgQhf3hzjvIpt%2FN0uywgrF31XNL86ZOlm0RUdYDsnElVIGz4mG&X-Amz-Signature=a313b46ba77cfdab50400f2eca2e2a23dec4f25ae2836a4e58ad89f15a845109&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCBANH4D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIExxGKHnVdCNfTeWPhlJ8LuBB4H6sXQS%2BJQFYP33I3EDAiEAhIUzfKkfTKVV6zqABWd1sKyZtYhydiHbDqeBTR8MHqIq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDLGdS7wFM6WGE%2FtNtyrcAxTw0Nq76gjiJPHkVfLBmKTeu5dXSZdYZln9IOiTriPL%2Bv5GWjbHhs%2BCVzNMFUyOeVrHpIKMDiwB5ttDX3v1HRLLnWc%2FfI63BAw4VRpkZUv1vGiboyf7ek1FlzMa741CRE3PzWJ2eN%2FE5Ced%2Fg1wMNKMRoymoWYx0oeBBZITFOsY2fYLwOQH75fl7Pup2ZgKvV2yVJJwpAcvdA%2FtthDJtVWHS6KSgbOgViOIpsA0CqN8%2F7XIBqekD5zlQiVI5Sx5Nar88zXQS5iExPVCrGgYBxJqCMY%2B9Qv9JpEVJTiT%2BzJLKcbSDRIJW2DrN5m2cGQqKXrJBvnQTI5fVgDst2yGsWvINJ0Jz%2BJs7gVSLbJkJZoo%2FagulEEnLrPpQ8AZM2Zu5%2FO5WGztHk6a8eLANvW0dLMf4WrYQOkskYLOf8ZWcfZnn8MltRUqfU0mC8nYt%2Be9phm6JgfK61UinBa%2FxZUh9bNBz5VldjvjP%2BEWQsRgTiSPxjgApEi4NmQ0bTWiOGXwkwQt5L4LOBPS0Bt2h%2BktcEky4WUZxBhklrHDH2YwkWouU%2Bk7aNB1Y5zkh4hXgLXdWqeOE%2Fg7YL%2BnR5YEE7qb5F3av1%2FKZCJ959oILoAnYWL4f5wJ0016MebT50kbMNPKg70GOqUBdccWxOfTwQVotgX3SD0pKv%2FMG4lKkePSz%2BxQJ%2FSNS4cSqpDmcaQe964l0y6qFKIJz4f2O%2BPbVs00z2xE7PPJt5aus2GLOyYuSAQg3aV10IbWfwfnFuofm1wKWEGyVF7giLgfku7jxyAtMnn0xE7DIETYpaW5aUaKnxhXk5LaZgcgQhf3hzjvIpt%2FN0uywgrF31XNL86ZOlm0RUdYDsnElVIGz4mG&X-Amz-Signature=7cdc57b1ac466ad2dceab94ff24add0fd93034e15364fae6b48ac29aaae2c868&X-Amz-SignedHeaders=host&x-id=GetObject)

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
