

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2KBLUPA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTk8pu9q%2BfkbSnGTXsrNR5qXoEceaKoTArPjAJwHJ2IgIgBK6m91%2BxVtovm6Z6kGGYHAe%2FOB0NxHRLNSB6eSe3DA0qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMxewL0sWcvTpFPt1CrcA3aPxnwR3g1qqxHhk8f3vltYW%2FGNBp5q3ZOZPNzySUkRkn1eXF4Wz0s64Jlt6MsR5t6%2B9Y%2F3phP4KDogfIk1t4eFnE0MSPVpMkjFN3On%2BTqGU5xGufqK3RqPSB5jLYaqSARWvz9osznKxgoiLG%2FbTDi1Da%2BE3cW1Kcll7%2F2%2FrJkAuamX2m7wCzCVIR%2F5mQ1PByeBWD5R8W%2F9bWxFitJKKpOoBKQRqqJof5mX%2BiEZ6q1iVymbt4U7Eb6CxZLDi%2F3hJfUUz9XmVvFfrW7SR%2FzJs6hjA9CPW4rX88sdfu%2FRM6Ez6l2BspMfZiLeiPdk9a6DSAm1DILP9L8z%2BKLYZlI1AkjnqbLHYbJckv3dhmsICT%2FS02Ys0Sw9ilaVjoVICzZ4NwCR0mA7kgLQbEvm9bH4JiWNybczMXZbfwV%2Fu59%2BVqkSAEoUlg8u2HmVhQVWZaIAK8iXY5zDnUdfAEbnJb2I6emz4Eool5AjDqkqPjCjpMzhX07BCrjMJt5KTUX2JFcmoT0CsGugXSGa9PtUNBHbQuT6Gk7SRm0hYfnBd0cdzuAHA8p81h0p3yirEIfGmf7VIN1dYJISdKiCneVKDZLdugBHkX0fxLaCaCQNPH8xLNw2ZCCCHGQRXELY08QmMJ308rwGOqUBGMN8RB02emInE9KSUZiVWJMAkqnTy1MmU54teneybA9xrGJyA3lxBEiXazDxEP%2BGEpBG8XDoSTzWgvfnYtT0g%2BaCYRYgEmJxHMPAefzUfWpmqkteYukxCRK4l6VyoDz67PXx%2BSJHmlHPFxwm9ApgkVGxEVGQZYgnQIgkFq1x8A%2FZhGy5z9icEg1Mi8aBEHBIv6ChwHty2l1lhcIMKlFWfZ7YqPzp&X-Amz-Signature=276c6d3387aac962bc529fc439efd969490e0a422ec886de1a07b2164f08fa85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2KBLUPA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTk8pu9q%2BfkbSnGTXsrNR5qXoEceaKoTArPjAJwHJ2IgIgBK6m91%2BxVtovm6Z6kGGYHAe%2FOB0NxHRLNSB6eSe3DA0qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMxewL0sWcvTpFPt1CrcA3aPxnwR3g1qqxHhk8f3vltYW%2FGNBp5q3ZOZPNzySUkRkn1eXF4Wz0s64Jlt6MsR5t6%2B9Y%2F3phP4KDogfIk1t4eFnE0MSPVpMkjFN3On%2BTqGU5xGufqK3RqPSB5jLYaqSARWvz9osznKxgoiLG%2FbTDi1Da%2BE3cW1Kcll7%2F2%2FrJkAuamX2m7wCzCVIR%2F5mQ1PByeBWD5R8W%2F9bWxFitJKKpOoBKQRqqJof5mX%2BiEZ6q1iVymbt4U7Eb6CxZLDi%2F3hJfUUz9XmVvFfrW7SR%2FzJs6hjA9CPW4rX88sdfu%2FRM6Ez6l2BspMfZiLeiPdk9a6DSAm1DILP9L8z%2BKLYZlI1AkjnqbLHYbJckv3dhmsICT%2FS02Ys0Sw9ilaVjoVICzZ4NwCR0mA7kgLQbEvm9bH4JiWNybczMXZbfwV%2Fu59%2BVqkSAEoUlg8u2HmVhQVWZaIAK8iXY5zDnUdfAEbnJb2I6emz4Eool5AjDqkqPjCjpMzhX07BCrjMJt5KTUX2JFcmoT0CsGugXSGa9PtUNBHbQuT6Gk7SRm0hYfnBd0cdzuAHA8p81h0p3yirEIfGmf7VIN1dYJISdKiCneVKDZLdugBHkX0fxLaCaCQNPH8xLNw2ZCCCHGQRXELY08QmMJ308rwGOqUBGMN8RB02emInE9KSUZiVWJMAkqnTy1MmU54teneybA9xrGJyA3lxBEiXazDxEP%2BGEpBG8XDoSTzWgvfnYtT0g%2BaCYRYgEmJxHMPAefzUfWpmqkteYukxCRK4l6VyoDz67PXx%2BSJHmlHPFxwm9ApgkVGxEVGQZYgnQIgkFq1x8A%2FZhGy5z9icEg1Mi8aBEHBIv6ChwHty2l1lhcIMKlFWfZ7YqPzp&X-Amz-Signature=b07d1eef58b2bd9c8c437988b2e0af4747fa5517a2297aaa901911e4f71d6d20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2KBLUPA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTk8pu9q%2BfkbSnGTXsrNR5qXoEceaKoTArPjAJwHJ2IgIgBK6m91%2BxVtovm6Z6kGGYHAe%2FOB0NxHRLNSB6eSe3DA0qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMxewL0sWcvTpFPt1CrcA3aPxnwR3g1qqxHhk8f3vltYW%2FGNBp5q3ZOZPNzySUkRkn1eXF4Wz0s64Jlt6MsR5t6%2B9Y%2F3phP4KDogfIk1t4eFnE0MSPVpMkjFN3On%2BTqGU5xGufqK3RqPSB5jLYaqSARWvz9osznKxgoiLG%2FbTDi1Da%2BE3cW1Kcll7%2F2%2FrJkAuamX2m7wCzCVIR%2F5mQ1PByeBWD5R8W%2F9bWxFitJKKpOoBKQRqqJof5mX%2BiEZ6q1iVymbt4U7Eb6CxZLDi%2F3hJfUUz9XmVvFfrW7SR%2FzJs6hjA9CPW4rX88sdfu%2FRM6Ez6l2BspMfZiLeiPdk9a6DSAm1DILP9L8z%2BKLYZlI1AkjnqbLHYbJckv3dhmsICT%2FS02Ys0Sw9ilaVjoVICzZ4NwCR0mA7kgLQbEvm9bH4JiWNybczMXZbfwV%2Fu59%2BVqkSAEoUlg8u2HmVhQVWZaIAK8iXY5zDnUdfAEbnJb2I6emz4Eool5AjDqkqPjCjpMzhX07BCrjMJt5KTUX2JFcmoT0CsGugXSGa9PtUNBHbQuT6Gk7SRm0hYfnBd0cdzuAHA8p81h0p3yirEIfGmf7VIN1dYJISdKiCneVKDZLdugBHkX0fxLaCaCQNPH8xLNw2ZCCCHGQRXELY08QmMJ308rwGOqUBGMN8RB02emInE9KSUZiVWJMAkqnTy1MmU54teneybA9xrGJyA3lxBEiXazDxEP%2BGEpBG8XDoSTzWgvfnYtT0g%2BaCYRYgEmJxHMPAefzUfWpmqkteYukxCRK4l6VyoDz67PXx%2BSJHmlHPFxwm9ApgkVGxEVGQZYgnQIgkFq1x8A%2FZhGy5z9icEg1Mi8aBEHBIv6ChwHty2l1lhcIMKlFWfZ7YqPzp&X-Amz-Signature=041d4d88de6aecdee3695cf1a1b6d6e5bb447958baa509a244c43550578a6726&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX5LFCIU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBuVPBE%2BB4UPr48%2FullC1GDYf1lwSAoKuKXDGzrQodtAiAPRs52NFg5lECZM9H77LNhsoAeHvyPOIrbLKLNDlqaPyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM84wn%2FMh0JN6RVIVyKtwDiGjxE%2BU5xDtkO9R6ZmENSJxBT1Gdhuie3TRDL7seQarpY%2BsE5dHV9diDCh0M833fEpVx2jRD2l9b4q73jbKuguPCIEI148YDzYFkh9Gg74ZgceEBTSjQo4zH52yRfstpTWU7AiF1z4UWW8d82MdNGsWUsbgec5lTfaO3IuSGS%2B6UiZoP%2FR6yBlx%2Foec2NWBpkwezB8Xh0261gwaem5FerrSsQ0pPEfUDQ3ZdKuInki19%2FOiXyliGVRFwXmfxcDlr7HzgzeFYTRWpLCtMsmrf%2F3zuckpZN1l2WdHKnG%2B0kuAFMurG1e7o4vj10U%2BtON9XfPvReGyG74l8I%2FZoCZGghTXd8xSZk2A4T6SVAu44KI%2BtY3XFL4TvQ60NRWRrz5WEs4AvHvPr7gbh0lDh0TnyX7zlBS63PWyR4cdg2hm%2BYgD0fUOm1OcUzKi0ZVHUHebua2BYKkpELCsB%2FbTmPVyjMBw%2F3JE%2F78G1mFP5J7%2Fkp4Fai2G3ptLqmSlszHajCc7Lwma%2FQK%2FZVq%2BmBamnVlqt8hIO9nSssz%2FTFBTbbjcYN2k1eoI%2F5Tisg6rRkgr1A6iYjkGGZ%2BNpBIxfX4v9Adbh7%2FpOfJwUwrqF9AM6A17Xrz4Bn3tscRV4qbvES5Ew7vPyvAY6pgF%2F76vWPEJOlGLzD9lh2CK9MiGZgiCosVfgcC0aQHsol8UwdlRUTCn2zsmpSg23cTOqMYFgYj8buvz6nuhqCvN%2FH6TOJwb37Cv2%2BADDD9BcrWbYGbj%2FXERmSSruLlwlhu5izJXVWsyd4Nbfwb4%2BV9O5dvum4yBLNtTol8S68foGzX%2BnjPtqUyLzwP5C%2B2R5Et9hCjxVDBQ5gYZKm%2FdF8a8WAZnyI0F2&X-Amz-Signature=120406425d4482e11fa67823fd308aaa624898ce6be352d09595831473a162f3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX5LFCIU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBuVPBE%2BB4UPr48%2FullC1GDYf1lwSAoKuKXDGzrQodtAiAPRs52NFg5lECZM9H77LNhsoAeHvyPOIrbLKLNDlqaPyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM84wn%2FMh0JN6RVIVyKtwDiGjxE%2BU5xDtkO9R6ZmENSJxBT1Gdhuie3TRDL7seQarpY%2BsE5dHV9diDCh0M833fEpVx2jRD2l9b4q73jbKuguPCIEI148YDzYFkh9Gg74ZgceEBTSjQo4zH52yRfstpTWU7AiF1z4UWW8d82MdNGsWUsbgec5lTfaO3IuSGS%2B6UiZoP%2FR6yBlx%2Foec2NWBpkwezB8Xh0261gwaem5FerrSsQ0pPEfUDQ3ZdKuInki19%2FOiXyliGVRFwXmfxcDlr7HzgzeFYTRWpLCtMsmrf%2F3zuckpZN1l2WdHKnG%2B0kuAFMurG1e7o4vj10U%2BtON9XfPvReGyG74l8I%2FZoCZGghTXd8xSZk2A4T6SVAu44KI%2BtY3XFL4TvQ60NRWRrz5WEs4AvHvPr7gbh0lDh0TnyX7zlBS63PWyR4cdg2hm%2BYgD0fUOm1OcUzKi0ZVHUHebua2BYKkpELCsB%2FbTmPVyjMBw%2F3JE%2F78G1mFP5J7%2Fkp4Fai2G3ptLqmSlszHajCc7Lwma%2FQK%2FZVq%2BmBamnVlqt8hIO9nSssz%2FTFBTbbjcYN2k1eoI%2F5Tisg6rRkgr1A6iYjkGGZ%2BNpBIxfX4v9Adbh7%2FpOfJwUwrqF9AM6A17Xrz4Bn3tscRV4qbvES5Ew7vPyvAY6pgF%2F76vWPEJOlGLzD9lh2CK9MiGZgiCosVfgcC0aQHsol8UwdlRUTCn2zsmpSg23cTOqMYFgYj8buvz6nuhqCvN%2FH6TOJwb37Cv2%2BADDD9BcrWbYGbj%2FXERmSSruLlwlhu5izJXVWsyd4Nbfwb4%2BV9O5dvum4yBLNtTol8S68foGzX%2BnjPtqUyLzwP5C%2B2R5Et9hCjxVDBQ5gYZKm%2FdF8a8WAZnyI0F2&X-Amz-Signature=fe1bdd105f81a9945faba3154fb680e3cffe2a01c174848bbb6bd84aa91cbab2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX5LFCIU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBuVPBE%2BB4UPr48%2FullC1GDYf1lwSAoKuKXDGzrQodtAiAPRs52NFg5lECZM9H77LNhsoAeHvyPOIrbLKLNDlqaPyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM84wn%2FMh0JN6RVIVyKtwDiGjxE%2BU5xDtkO9R6ZmENSJxBT1Gdhuie3TRDL7seQarpY%2BsE5dHV9diDCh0M833fEpVx2jRD2l9b4q73jbKuguPCIEI148YDzYFkh9Gg74ZgceEBTSjQo4zH52yRfstpTWU7AiF1z4UWW8d82MdNGsWUsbgec5lTfaO3IuSGS%2B6UiZoP%2FR6yBlx%2Foec2NWBpkwezB8Xh0261gwaem5FerrSsQ0pPEfUDQ3ZdKuInki19%2FOiXyliGVRFwXmfxcDlr7HzgzeFYTRWpLCtMsmrf%2F3zuckpZN1l2WdHKnG%2B0kuAFMurG1e7o4vj10U%2BtON9XfPvReGyG74l8I%2FZoCZGghTXd8xSZk2A4T6SVAu44KI%2BtY3XFL4TvQ60NRWRrz5WEs4AvHvPr7gbh0lDh0TnyX7zlBS63PWyR4cdg2hm%2BYgD0fUOm1OcUzKi0ZVHUHebua2BYKkpELCsB%2FbTmPVyjMBw%2F3JE%2F78G1mFP5J7%2Fkp4Fai2G3ptLqmSlszHajCc7Lwma%2FQK%2FZVq%2BmBamnVlqt8hIO9nSssz%2FTFBTbbjcYN2k1eoI%2F5Tisg6rRkgr1A6iYjkGGZ%2BNpBIxfX4v9Adbh7%2FpOfJwUwrqF9AM6A17Xrz4Bn3tscRV4qbvES5Ew7vPyvAY6pgF%2F76vWPEJOlGLzD9lh2CK9MiGZgiCosVfgcC0aQHsol8UwdlRUTCn2zsmpSg23cTOqMYFgYj8buvz6nuhqCvN%2FH6TOJwb37Cv2%2BADDD9BcrWbYGbj%2FXERmSSruLlwlhu5izJXVWsyd4Nbfwb4%2BV9O5dvum4yBLNtTol8S68foGzX%2BnjPtqUyLzwP5C%2B2R5Et9hCjxVDBQ5gYZKm%2FdF8a8WAZnyI0F2&X-Amz-Signature=a1aba76503124c4459065022404f337e9e3490baf79e355e627184ecd69ab6c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX5LFCIU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBuVPBE%2BB4UPr48%2FullC1GDYf1lwSAoKuKXDGzrQodtAiAPRs52NFg5lECZM9H77LNhsoAeHvyPOIrbLKLNDlqaPyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM84wn%2FMh0JN6RVIVyKtwDiGjxE%2BU5xDtkO9R6ZmENSJxBT1Gdhuie3TRDL7seQarpY%2BsE5dHV9diDCh0M833fEpVx2jRD2l9b4q73jbKuguPCIEI148YDzYFkh9Gg74ZgceEBTSjQo4zH52yRfstpTWU7AiF1z4UWW8d82MdNGsWUsbgec5lTfaO3IuSGS%2B6UiZoP%2FR6yBlx%2Foec2NWBpkwezB8Xh0261gwaem5FerrSsQ0pPEfUDQ3ZdKuInki19%2FOiXyliGVRFwXmfxcDlr7HzgzeFYTRWpLCtMsmrf%2F3zuckpZN1l2WdHKnG%2B0kuAFMurG1e7o4vj10U%2BtON9XfPvReGyG74l8I%2FZoCZGghTXd8xSZk2A4T6SVAu44KI%2BtY3XFL4TvQ60NRWRrz5WEs4AvHvPr7gbh0lDh0TnyX7zlBS63PWyR4cdg2hm%2BYgD0fUOm1OcUzKi0ZVHUHebua2BYKkpELCsB%2FbTmPVyjMBw%2F3JE%2F78G1mFP5J7%2Fkp4Fai2G3ptLqmSlszHajCc7Lwma%2FQK%2FZVq%2BmBamnVlqt8hIO9nSssz%2FTFBTbbjcYN2k1eoI%2F5Tisg6rRkgr1A6iYjkGGZ%2BNpBIxfX4v9Adbh7%2FpOfJwUwrqF9AM6A17Xrz4Bn3tscRV4qbvES5Ew7vPyvAY6pgF%2F76vWPEJOlGLzD9lh2CK9MiGZgiCosVfgcC0aQHsol8UwdlRUTCn2zsmpSg23cTOqMYFgYj8buvz6nuhqCvN%2FH6TOJwb37Cv2%2BADDD9BcrWbYGbj%2FXERmSSruLlwlhu5izJXVWsyd4Nbfwb4%2BV9O5dvum4yBLNtTol8S68foGzX%2BnjPtqUyLzwP5C%2B2R5Et9hCjxVDBQ5gYZKm%2FdF8a8WAZnyI0F2&X-Amz-Signature=43683c84182bd98e753e2cdbf501b413d4d0428d36eae3c8aeb89cee52656e59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX5LFCIU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBuVPBE%2BB4UPr48%2FullC1GDYf1lwSAoKuKXDGzrQodtAiAPRs52NFg5lECZM9H77LNhsoAeHvyPOIrbLKLNDlqaPyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM84wn%2FMh0JN6RVIVyKtwDiGjxE%2BU5xDtkO9R6ZmENSJxBT1Gdhuie3TRDL7seQarpY%2BsE5dHV9diDCh0M833fEpVx2jRD2l9b4q73jbKuguPCIEI148YDzYFkh9Gg74ZgceEBTSjQo4zH52yRfstpTWU7AiF1z4UWW8d82MdNGsWUsbgec5lTfaO3IuSGS%2B6UiZoP%2FR6yBlx%2Foec2NWBpkwezB8Xh0261gwaem5FerrSsQ0pPEfUDQ3ZdKuInki19%2FOiXyliGVRFwXmfxcDlr7HzgzeFYTRWpLCtMsmrf%2F3zuckpZN1l2WdHKnG%2B0kuAFMurG1e7o4vj10U%2BtON9XfPvReGyG74l8I%2FZoCZGghTXd8xSZk2A4T6SVAu44KI%2BtY3XFL4TvQ60NRWRrz5WEs4AvHvPr7gbh0lDh0TnyX7zlBS63PWyR4cdg2hm%2BYgD0fUOm1OcUzKi0ZVHUHebua2BYKkpELCsB%2FbTmPVyjMBw%2F3JE%2F78G1mFP5J7%2Fkp4Fai2G3ptLqmSlszHajCc7Lwma%2FQK%2FZVq%2BmBamnVlqt8hIO9nSssz%2FTFBTbbjcYN2k1eoI%2F5Tisg6rRkgr1A6iYjkGGZ%2BNpBIxfX4v9Adbh7%2FpOfJwUwrqF9AM6A17Xrz4Bn3tscRV4qbvES5Ew7vPyvAY6pgF%2F76vWPEJOlGLzD9lh2CK9MiGZgiCosVfgcC0aQHsol8UwdlRUTCn2zsmpSg23cTOqMYFgYj8buvz6nuhqCvN%2FH6TOJwb37Cv2%2BADDD9BcrWbYGbj%2FXERmSSruLlwlhu5izJXVWsyd4Nbfwb4%2BV9O5dvum4yBLNtTol8S68foGzX%2BnjPtqUyLzwP5C%2B2R5Et9hCjxVDBQ5gYZKm%2FdF8a8WAZnyI0F2&X-Amz-Signature=a652b9f7efc4854d477dc2e2a1462c8c4b54bf6762f9b2437fac3819f62a1cbb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX5LFCIU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBuVPBE%2BB4UPr48%2FullC1GDYf1lwSAoKuKXDGzrQodtAiAPRs52NFg5lECZM9H77LNhsoAeHvyPOIrbLKLNDlqaPyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM84wn%2FMh0JN6RVIVyKtwDiGjxE%2BU5xDtkO9R6ZmENSJxBT1Gdhuie3TRDL7seQarpY%2BsE5dHV9diDCh0M833fEpVx2jRD2l9b4q73jbKuguPCIEI148YDzYFkh9Gg74ZgceEBTSjQo4zH52yRfstpTWU7AiF1z4UWW8d82MdNGsWUsbgec5lTfaO3IuSGS%2B6UiZoP%2FR6yBlx%2Foec2NWBpkwezB8Xh0261gwaem5FerrSsQ0pPEfUDQ3ZdKuInki19%2FOiXyliGVRFwXmfxcDlr7HzgzeFYTRWpLCtMsmrf%2F3zuckpZN1l2WdHKnG%2B0kuAFMurG1e7o4vj10U%2BtON9XfPvReGyG74l8I%2FZoCZGghTXd8xSZk2A4T6SVAu44KI%2BtY3XFL4TvQ60NRWRrz5WEs4AvHvPr7gbh0lDh0TnyX7zlBS63PWyR4cdg2hm%2BYgD0fUOm1OcUzKi0ZVHUHebua2BYKkpELCsB%2FbTmPVyjMBw%2F3JE%2F78G1mFP5J7%2Fkp4Fai2G3ptLqmSlszHajCc7Lwma%2FQK%2FZVq%2BmBamnVlqt8hIO9nSssz%2FTFBTbbjcYN2k1eoI%2F5Tisg6rRkgr1A6iYjkGGZ%2BNpBIxfX4v9Adbh7%2FpOfJwUwrqF9AM6A17Xrz4Bn3tscRV4qbvES5Ew7vPyvAY6pgF%2F76vWPEJOlGLzD9lh2CK9MiGZgiCosVfgcC0aQHsol8UwdlRUTCn2zsmpSg23cTOqMYFgYj8buvz6nuhqCvN%2FH6TOJwb37Cv2%2BADDD9BcrWbYGbj%2FXERmSSruLlwlhu5izJXVWsyd4Nbfwb4%2BV9O5dvum4yBLNtTol8S68foGzX%2BnjPtqUyLzwP5C%2B2R5Et9hCjxVDBQ5gYZKm%2FdF8a8WAZnyI0F2&X-Amz-Signature=87d7c7bb9a622d0ec17f93e42bc35fdd83363d62a9905db8c260cd07a58ddaec&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKHSCM7T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDu7qUp0sd%2BFQvfFxi3jz8B9TwCFyqiggpuam3BPMvMaAiAm2nX3zzWb3GpEN7FXbQpZHLEgj6tFY8SJQoYD3AV9uyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBmKP2dCPQnK5L9f%2BKtwDa5r%2BOu4TtNYOdc9GfSrqN3ZY2SW2s2S28nguleMrWosQpAxYqEHVUZqFx4KvZNrosELMoAiUONDuPILP8m8r7G5f0uyLHJcOkPmEA5eZ12JNH9EB%2FPV88rWwUMlF%2FjT2GRbRiSnPinwWTellgP1pAUx7DF7v062lr8RuWotQBDjAlNUFeePJkvL2UC93t%2FcWPPlapsYhObZs2P%2FZ7%2FL2VL8jGkVn1kyQ4CKCXwEa5%2FXT0e7Eg1s%2BXP7rrva%2FhjR2fP4nHaA%2F1q6R64CeHadIl%2BGnzDY0s6YjRcH81hMSVksH%2FtSYOV1TS1H4z5yeX9yOaTcMPdIRpCmi3trfAn19wO0srMGlSeU9AGdgxA%2FIwqhX1mSIYHgL7iOlmUotv2yxfUhGrKbojsNq7Peww2udqXYd2HEZq5JNUidoPUepqeyxTMLMvwcjyarqcsh5KoNJpPlFPAnl5gq86dtXdWQxxzlB%2BOLl9vJckIM1Hl8ulmZoIfmk%2BHg707W2h8XLd3%2Bp%2Bs5r8bhj%2BOfX4%2F3icVBihx%2F6vMTaiOfWlf1yWFnDroFNZ9V5%2FC0hYRRxBIqvg7YWtO4qopDqsj82sIjM6sbZQrLYu5DfEDoyMS89lQ4VBH1E3%2FgZpVjR5P9cngowyvPyvAY6pgGIjzudfH4qsnSkwngLoqATWfV2D57S9AmuWON1vvwm6Xdn0M4KQUe%2FU0%2BRR7ifmRBH5krsOsCF%2FQuJcq2hTcM0CRugwYSHrYlV91jgKwYdQ1HGzsSdWs%2BqYd%2BqS%2BzzAB%2BuzeBPoHhICtXVjB%2Fe0qnyBAEfA5Gpqnk7Bf%2FkjENJvamE%2BfK4YP9iBOZDR8sFDJp2oEdhBWbfd2cCsNlO%2BXKfTbnfUcoN&X-Amz-Signature=67706797c1d2ae0e1ec853a1efd0c1f13d7dd7adefd921d91cc22cf717fc3b99&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z26JNRP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzRSACvZuJMDcRGi98SJY%2BfE2bzvBiirFa8SYVpJkdgAiEAnRoLV7jN%2Fz2b9EvDAKRYR4qRR7zT9E9iVCK8fy5Ob1YqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNA6MAZmKpWYl8t5xCrcA9XVXbnfFxEH4vVdHH4w3U1xNZcpfovbwhblKJ6rYiJcU%2FcdYc0NuyS3%2FrmU0eQ8ba8zKM9Y2EZSxXXP3BQqXgC9oQvEnIv1vGse6YwMEtcJZw7IIna9QbFKwwshVBNVkvD99yQVGL1wKvn3t9BcKmfkYgyVLsQxsAI79UI4vGSqM4aID%2BPWk4GWJv1Ifqss0cdgPwHFvpaFOCHPBjBFcWZkI04JIXxvMoTTBzYKoJPqGmaD0uiw5KGRlDK8OetXt30VY7zf9h9Z%2FApP4Y%2Bb5BnaYszaMHrpCZTwWs2mZqSdQB%2FTc6xSJ6jHAjmoa79nWVR3GqBLaCvPZKSVgXlH5ztv5pdHD28sajCIxzhA2Itgwd6biF0nfwQ7hz2LWLtqCWEKQd5mfATEypBjk9RplmylzRFjqrtJe3kgIZ2JrVvDkaLbM5RlvvSUS0Odc6eKBRDkV8rWDwK%2B%2BRMFgR5re7pQavzKjYH9fwmOEKJC1GSe0Tw19kQnEWFm%2F21W%2FqgNYgvHssE%2FaHx28gpLyfmlN0Tu%2FyGzzxP6taIqvWJczUusMY81%2Fvy3qCjTwZen2za%2BBqJD3pJmtUUQK5Kix%2BG%2Bo1tLURvukSS3cFgpvWFhYtCawQ0888HSPqOw2LXkMOLz8rwGOqUB0KSHRX4zDoU7LMVw9zbhiSUSNOFkO%2FIMQLg4HvyVsR%2F9pqtyGQWE9nWlM9yPlDhwCHaWObYUXtGpWt2c1dJc%2BkXe1AL%2BBb6tP0%2Bux6tl649DaxqDBS6EaR8KUZWc%2BWy%2B7I4KkUfGAsR17%2FcWeHzYAaeOf8ikYfOG1xxj6Z9g0o97QwM5mcV6dWb%2B%2BXP9AWzLp0w9TANUdZTKCVUVBQZ%2FL2n7vmFm&X-Amz-Signature=70edaf4dd6b1e46396c7bc3bb034994694138498dd6baaa59d0d8645156e5f44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX5LFCIU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBuVPBE%2BB4UPr48%2FullC1GDYf1lwSAoKuKXDGzrQodtAiAPRs52NFg5lECZM9H77LNhsoAeHvyPOIrbLKLNDlqaPyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM84wn%2FMh0JN6RVIVyKtwDiGjxE%2BU5xDtkO9R6ZmENSJxBT1Gdhuie3TRDL7seQarpY%2BsE5dHV9diDCh0M833fEpVx2jRD2l9b4q73jbKuguPCIEI148YDzYFkh9Gg74ZgceEBTSjQo4zH52yRfstpTWU7AiF1z4UWW8d82MdNGsWUsbgec5lTfaO3IuSGS%2B6UiZoP%2FR6yBlx%2Foec2NWBpkwezB8Xh0261gwaem5FerrSsQ0pPEfUDQ3ZdKuInki19%2FOiXyliGVRFwXmfxcDlr7HzgzeFYTRWpLCtMsmrf%2F3zuckpZN1l2WdHKnG%2B0kuAFMurG1e7o4vj10U%2BtON9XfPvReGyG74l8I%2FZoCZGghTXd8xSZk2A4T6SVAu44KI%2BtY3XFL4TvQ60NRWRrz5WEs4AvHvPr7gbh0lDh0TnyX7zlBS63PWyR4cdg2hm%2BYgD0fUOm1OcUzKi0ZVHUHebua2BYKkpELCsB%2FbTmPVyjMBw%2F3JE%2F78G1mFP5J7%2Fkp4Fai2G3ptLqmSlszHajCc7Lwma%2FQK%2FZVq%2BmBamnVlqt8hIO9nSssz%2FTFBTbbjcYN2k1eoI%2F5Tisg6rRkgr1A6iYjkGGZ%2BNpBIxfX4v9Adbh7%2FpOfJwUwrqF9AM6A17Xrz4Bn3tscRV4qbvES5Ew7vPyvAY6pgF%2F76vWPEJOlGLzD9lh2CK9MiGZgiCosVfgcC0aQHsol8UwdlRUTCn2zsmpSg23cTOqMYFgYj8buvz6nuhqCvN%2FH6TOJwb37Cv2%2BADDD9BcrWbYGbj%2FXERmSSruLlwlhu5izJXVWsyd4Nbfwb4%2BV9O5dvum4yBLNtTol8S68foGzX%2BnjPtqUyLzwP5C%2B2R5Et9hCjxVDBQ5gYZKm%2FdF8a8WAZnyI0F2&X-Amz-Signature=3ee27cc1cf86e8a14ba4f3157d0f46f51b43df98d6f9c3769904ffe506654d6f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX5LFCIU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBuVPBE%2BB4UPr48%2FullC1GDYf1lwSAoKuKXDGzrQodtAiAPRs52NFg5lECZM9H77LNhsoAeHvyPOIrbLKLNDlqaPyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM84wn%2FMh0JN6RVIVyKtwDiGjxE%2BU5xDtkO9R6ZmENSJxBT1Gdhuie3TRDL7seQarpY%2BsE5dHV9diDCh0M833fEpVx2jRD2l9b4q73jbKuguPCIEI148YDzYFkh9Gg74ZgceEBTSjQo4zH52yRfstpTWU7AiF1z4UWW8d82MdNGsWUsbgec5lTfaO3IuSGS%2B6UiZoP%2FR6yBlx%2Foec2NWBpkwezB8Xh0261gwaem5FerrSsQ0pPEfUDQ3ZdKuInki19%2FOiXyliGVRFwXmfxcDlr7HzgzeFYTRWpLCtMsmrf%2F3zuckpZN1l2WdHKnG%2B0kuAFMurG1e7o4vj10U%2BtON9XfPvReGyG74l8I%2FZoCZGghTXd8xSZk2A4T6SVAu44KI%2BtY3XFL4TvQ60NRWRrz5WEs4AvHvPr7gbh0lDh0TnyX7zlBS63PWyR4cdg2hm%2BYgD0fUOm1OcUzKi0ZVHUHebua2BYKkpELCsB%2FbTmPVyjMBw%2F3JE%2F78G1mFP5J7%2Fkp4Fai2G3ptLqmSlszHajCc7Lwma%2FQK%2FZVq%2BmBamnVlqt8hIO9nSssz%2FTFBTbbjcYN2k1eoI%2F5Tisg6rRkgr1A6iYjkGGZ%2BNpBIxfX4v9Adbh7%2FpOfJwUwrqF9AM6A17Xrz4Bn3tscRV4qbvES5Ew7vPyvAY6pgF%2F76vWPEJOlGLzD9lh2CK9MiGZgiCosVfgcC0aQHsol8UwdlRUTCn2zsmpSg23cTOqMYFgYj8buvz6nuhqCvN%2FH6TOJwb37Cv2%2BADDD9BcrWbYGbj%2FXERmSSruLlwlhu5izJXVWsyd4Nbfwb4%2BV9O5dvum4yBLNtTol8S68foGzX%2BnjPtqUyLzwP5C%2B2R5Et9hCjxVDBQ5gYZKm%2FdF8a8WAZnyI0F2&X-Amz-Signature=d325ef7a523e14a47fead645511b537166d3e9eb21b173a086756421f594a468&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX5LFCIU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBuVPBE%2BB4UPr48%2FullC1GDYf1lwSAoKuKXDGzrQodtAiAPRs52NFg5lECZM9H77LNhsoAeHvyPOIrbLKLNDlqaPyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM84wn%2FMh0JN6RVIVyKtwDiGjxE%2BU5xDtkO9R6ZmENSJxBT1Gdhuie3TRDL7seQarpY%2BsE5dHV9diDCh0M833fEpVx2jRD2l9b4q73jbKuguPCIEI148YDzYFkh9Gg74ZgceEBTSjQo4zH52yRfstpTWU7AiF1z4UWW8d82MdNGsWUsbgec5lTfaO3IuSGS%2B6UiZoP%2FR6yBlx%2Foec2NWBpkwezB8Xh0261gwaem5FerrSsQ0pPEfUDQ3ZdKuInki19%2FOiXyliGVRFwXmfxcDlr7HzgzeFYTRWpLCtMsmrf%2F3zuckpZN1l2WdHKnG%2B0kuAFMurG1e7o4vj10U%2BtON9XfPvReGyG74l8I%2FZoCZGghTXd8xSZk2A4T6SVAu44KI%2BtY3XFL4TvQ60NRWRrz5WEs4AvHvPr7gbh0lDh0TnyX7zlBS63PWyR4cdg2hm%2BYgD0fUOm1OcUzKi0ZVHUHebua2BYKkpELCsB%2FbTmPVyjMBw%2F3JE%2F78G1mFP5J7%2Fkp4Fai2G3ptLqmSlszHajCc7Lwma%2FQK%2FZVq%2BmBamnVlqt8hIO9nSssz%2FTFBTbbjcYN2k1eoI%2F5Tisg6rRkgr1A6iYjkGGZ%2BNpBIxfX4v9Adbh7%2FpOfJwUwrqF9AM6A17Xrz4Bn3tscRV4qbvES5Ew7vPyvAY6pgF%2F76vWPEJOlGLzD9lh2CK9MiGZgiCosVfgcC0aQHsol8UwdlRUTCn2zsmpSg23cTOqMYFgYj8buvz6nuhqCvN%2FH6TOJwb37Cv2%2BADDD9BcrWbYGbj%2FXERmSSruLlwlhu5izJXVWsyd4Nbfwb4%2BV9O5dvum4yBLNtTol8S68foGzX%2BnjPtqUyLzwP5C%2B2R5Et9hCjxVDBQ5gYZKm%2FdF8a8WAZnyI0F2&X-Amz-Signature=1e16e00e7d8ad05777b09823401dea0b7ac94e98454522157b7953072f653ea4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUT2QIAX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbx0o8Go02MEUmrGwRy7sDHOFM3YedhCvjKTm%2BRhmxygIhAKDyF540nwR%2Fv3Q0ysheIYwCWushSYLl%2FDOJ1lvN6JulKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwoQ1sxEnneYhBExYQq3ANamP6BKRolp%2BOr%2FqvvDBO%2F988QWSmNATWk8SCx31AQ8pISqPnoZCCOxoTOLuPFjXa4TurGHZMGBrfXvROrotEvKk9HSCq6p%2Bs7JgbBjoBDsrbFm%2FQuwC20CoAPGC08j3Jtkqq36XJPdoSSZeYMfW5yZ5yShftqTeTJb%2Bc%2F7Lbb%2FIz7uuSpnUWIw49L%2BKoVAP%2BA3DnWayhZuj7FQPtr45bOZhIJHc2gDggLB5KARZto6rHg8ky7rV0L5sfRq40UWZ0xVoVRZ4z4zhUKxOQucClkib5cFkRd5vxw25O%2BSGMeMo5gdFmb0ibAr6QOpFYVFrCCVUwLtg5xpc%2FPqq77p9ewrVxGu8cYhTvdN%2FXKy6D2zoMK7UYjU5yYSYbUPs71QbC2gnKnwuPYjwh1nzSBUI3XwZ7kGafSxqxTAmJiJJug2baI1F2mXNsd33nZN1jrHUKK2qjkG8upqBAfcfGC%2BrELePOISL1erE5BUh4ectwCNQMtUyU88OpxUSK5lMVP8zaGc4S1N3wQ113kb2HJ4TIeiTu5jIYY9ae9adBg4HkypbP74MU3q49wgYqXwGS2Hb73Lxwg7SemkD5PohmjrawH6vdBO26fVZwtbITcq0ZvPjfCBFUxjGVAnVKoljCs9PK8BjqkAa6uH%2BNcHKO6h9oYpJr2B%2BrXwTCWwq7dS12GaVc%2FroWb03ToAH%2Fn3AW%2BDnwmFedN0mYpagfIOVNir4eXSNKrGjDhtDp1nh%2B091GjPgpxHM75axr1Kkkt9NZvmeBr%2BQzetjNsDOhtGLE%2FVafYkAnZU9Ucs%2FoaYu521FR%2FpDDvNNk%2B2fpupXlOjX9ng%2BwkKX5O1cbd2tb4pgFIS8XArl24MhyBRVcl&X-Amz-Signature=0fe9b7d5ed095980f2eb55df7688173ca262c28816bdf7d79928ede391abbfa5&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNPVUUUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6q8QjMvhIlMHjKpFFKdy%2FB5hohRl1eWc7YmSabP0%2BagIhAIvCbbjmMASTAwpNwq0han0fYDNI9jET7JiuSi5Zbxk6KogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx6c4mVPaIJ3hQByiMq3APZ6ucGQ3OZqch2NHPLGoBokPiu0fsCJijtGLaxjgQuh7FSa9gWAkcECD3o1DC%2FsPfsC58UjflvPpd7YlW4VPn2mNTTFJr7i9us%2BA%2FpocrB87JdFsH2dWQ0SJLTYNM%2FKwvbtT447ZmAl5VGQ97kArZKKPE%2Bjp%2FZl%2FyUlZPO7nh4ZmHvO7ttJZvLYRUjO%2BFUhDSGQmLffB4IAu8qEIODG3XU5npozftO%2BW1WnhWnmZhDw2IX1AlY0oT1JuTDUPU%2B%2FSkJYWsomyj4vWZ4yLrZHBlI%2BSbrNPUUE%2B6tcx49jl4oRUcKgTt1YBNFOl2S5Nl%2Fa8eQVxjnUu5mztiL%2B5EuomtVx%2BbTkI1ZRXS%2BfmEdUylODSwNVinK8NV1tPkQ4AMnqumQMtKRNUme6NjqTnyMuQdsPYkNZ3JBSb%2B9cfYNgeGhK5831PwcErSq%2B2GQnDgSdQcJUzg%2FLAU6Cl47%2BcFNzJf8BYMFKDUa1zuZ3LRu5i6gcTosUcSP%2BbbCgFdWjkRvEGf4HI5YCuQ1DIgjLVmDkgc8x4PobShC4q0E78yf%2F3sZqonauLRyCiPa%2B5ZJA3eFC1BbHg4eZTrnVgs0K%2BW0Xh5AELaROsKdUTHF6d79THaFGG1WYqCex8%2FjcBUgIzDK8%2FK8BjqkAdLUqWqxZ0%2FOzu57XwD7ez5AhAc%2FLyXTpGm3AijoMpD3csotIGStYROQcR9MvdC09LX34h745M0jyiK3FkPi1D95IvmL0zPUanP8sxzER4fH%2BDk1i3Dm4hITui%2FDUCwSfb2gSe%2FlQwtYFpDSx0PWxzIjyrDcgO62mFmpagDvESb3zEDc3VszOaWNvTq%2FkWMmgReVSLaktdtFesa7BWyBSJ1BhYTJ&X-Amz-Signature=49b186950026d695a9c278c98d2d04b4ab029704892fa451386eb1f3ecc4845c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667B3T66NA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1Omi9QVzBGOnZralVTZSyTeUQOyypsxZCebkqPttOOAIhALGNK23crgliNbd1n7hqiGU8sgv6GVrXEsuODfht9mSKKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxI44MBXAqNsWrydVIq3AO7i58r8f9VI9iOvbfoJzTKqdSKcqaSRlZhumSCxW4T6GjH8vUg0fSxoNHLwJc2dfuHPReKQdyh7daroO4TR5z0gTD1lZwp5uUXXTdfbs4mR1QJCJf1rjoGzMviGX8wTpgJ8K2fYkANyX5sgz2p308PGbj1lOGdJ9EzXM6YEz03HjS0%2FaruprBlJQRV1IQoJq3ad14E54nHmXpb%2BuUxSsvMpi7pyrYIjWc%2FutdvtzNcaAZJv25Lq4kU36icPgJocJIe8CwytURm8TvaW9mLnSKuovU5yoGszJTRN7g6TfiYrvBZpO3z1DRhFQVaffxex%2BpSwgWHsWaNXeSKsswFTdl974gnPa9lB0Srd0OCOEcU25P3Chq68BjgHPkqt8weh%2FlAbvQ%2FMlXSJa40MfdjmggCl37G20dfs%2BgSH9FbHmVahjKCrFCjQ5jC8L7SAlyytfr%2FzHjo8EWyCettQuddAoiuZkLEsTlpVEI4c3IqNs82%2B5gUblu2llr4lln7t9E0FbMuHM2frHepCF9DDsM%2BXfR7hp%2BTVJdduaNrzoKjKpzDnkutbDTa0YdL4mPYHcU3RcfQtjGF3KM2JElSkWTLCItyVhyQsaCMt1y5NyytisAK7vU2Al3o3ynSyWlTuzD58%2FK8BjqkARK7LefOVvcsVHF4X2PBDkR4qi6sDMYf8yLCNiWMezk2e7WDLzjE4MV%2FN%2BnXkanmr%2Fw1pN%2BM6Bc7g1hCoACQjRypPMxkUuvgT9hCsUGIFGp1%2FWXnFca2vsGz5VkQOOpfWoUBVTjNoXl5KWTUlazK66l2I7wYIHjJQHANGeJGB3QUeVZfBjAMoZEPoR2hVNBYhGiVFdnVHghRVVJITyApVs5SOQty&X-Amz-Signature=d609ec70634078fa09245b788f82beeeb45cfd2354e75296c6c8c25c74185dd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ODT62DL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGq1TFIIzu%2B66B84YvKAQ6vDvc%2FQc%2FldEsyhvM7Xwf5tAiEAjaUTwqWuv3C7UaymNkyNY75cmRTJX7qzk6bax5HxGkQqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDERE9%2FR%2B11O3AkUM0ircA77FjTFKUp7Urscogl5NLwbBBgL6a1BSufElv4AcjHf3khE%2B%2BMfLMQK5NU2AYyBxCRJ7FUVtMw8vzHY3CKvMgOTwr%2Fznurfd%2BHtUzGK%2B5T%2Fhx56znfL62OGpaCfYe4jF9hD05skZ2uquVODTCy12qNBsuC6uWcB0YcKp3iufyUJYZCOf7EGYccJ%2FkBipN7tXm8p9coD3IvXpeFk%2B5y3Zf6wk9ZFF2xO5kzkcpU63EbJTg58xfylrksqnDPR9sRI0nvLJVqpA27GQ1la%2BrTxPAqweyxf5qfUduBBhUdNjLOccTsThXfkOhovjnHbH%2B6W5MbFnhe85rT42r5mBlTf8QUKwzWk%2FuLPyhas3aZ7OzVhKCIjl5wr07%2Bz%2FR2c2lc9W%2BgKePfFUjy1xl2ocT0IdmZe%2B9hEXtqrbQdb3%2FgI70s0NEiYqgj1HKGcY30d1t8hJDB1jmFfH9bvz0IMdjMN1g7dOodSymqP8ADMhAjjeIJkgRI29i%2FqYS88dqQlCDfi%2FL2%2F06m6LScMG%2FbngAMU5BnVU9SFclwcFTRrCS%2B5paPxrwkxvU3It81Pk5mnMYe5yAdlKLGCZuB6vhTDZX2s7lizNg3VwpYGwaZGCqPHe8TrYwKpXCk3GaF7HCtp%2BMOLz8rwGOqUB75jRGOBYPAgMCeA4edchCMRSnQogln3R8P%2F3Du5Rvpe2VaL4sNN2Gv5pk2p2pmyKAdgLaX7wU%2FugHg3zrbBWbEJOSVtOt%2BnX2sWScaTKg5dwwtMAHFlxLgl%2FzPWpkCYxYF%2FTHCTbEFDkwmGZmbTmG9jkPxsYmoTfkTuL3UVmXdIHSJ6MvltdHs2W%2FFsME5U%2Bfr5RcCHK%2BrHBhvDEXElaTwB8Iby5&X-Amz-Signature=c78c534412b861d712c66060ba5c428670886b96d3a66c0fddcf2ebda5269d55&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ODT62DL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGq1TFIIzu%2B66B84YvKAQ6vDvc%2FQc%2FldEsyhvM7Xwf5tAiEAjaUTwqWuv3C7UaymNkyNY75cmRTJX7qzk6bax5HxGkQqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDERE9%2FR%2B11O3AkUM0ircA77FjTFKUp7Urscogl5NLwbBBgL6a1BSufElv4AcjHf3khE%2B%2BMfLMQK5NU2AYyBxCRJ7FUVtMw8vzHY3CKvMgOTwr%2Fznurfd%2BHtUzGK%2B5T%2Fhx56znfL62OGpaCfYe4jF9hD05skZ2uquVODTCy12qNBsuC6uWcB0YcKp3iufyUJYZCOf7EGYccJ%2FkBipN7tXm8p9coD3IvXpeFk%2B5y3Zf6wk9ZFF2xO5kzkcpU63EbJTg58xfylrksqnDPR9sRI0nvLJVqpA27GQ1la%2BrTxPAqweyxf5qfUduBBhUdNjLOccTsThXfkOhovjnHbH%2B6W5MbFnhe85rT42r5mBlTf8QUKwzWk%2FuLPyhas3aZ7OzVhKCIjl5wr07%2Bz%2FR2c2lc9W%2BgKePfFUjy1xl2ocT0IdmZe%2B9hEXtqrbQdb3%2FgI70s0NEiYqgj1HKGcY30d1t8hJDB1jmFfH9bvz0IMdjMN1g7dOodSymqP8ADMhAjjeIJkgRI29i%2FqYS88dqQlCDfi%2FL2%2F06m6LScMG%2FbngAMU5BnVU9SFclwcFTRrCS%2B5paPxrwkxvU3It81Pk5mnMYe5yAdlKLGCZuB6vhTDZX2s7lizNg3VwpYGwaZGCqPHe8TrYwKpXCk3GaF7HCtp%2BMOLz8rwGOqUB75jRGOBYPAgMCeA4edchCMRSnQogln3R8P%2F3Du5Rvpe2VaL4sNN2Gv5pk2p2pmyKAdgLaX7wU%2FugHg3zrbBWbEJOSVtOt%2BnX2sWScaTKg5dwwtMAHFlxLgl%2FzPWpkCYxYF%2FTHCTbEFDkwmGZmbTmG9jkPxsYmoTfkTuL3UVmXdIHSJ6MvltdHs2W%2FFsME5U%2Bfr5RcCHK%2BrHBhvDEXElaTwB8Iby5&X-Amz-Signature=658cee667c2a0feae67d3187cc8bde9261372a186c86e91f20f936b0cab64dae&X-Amz-SignedHeaders=host&x-id=GetObject)

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
