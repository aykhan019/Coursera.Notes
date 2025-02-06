

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFHCQAWT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIBFLQUvtHRPphnzvgXjg5rs3Z%2Fu0sMGEv3hp4L2XfWs%2BAiAhUP5cfVvgvxdNY79nE%2BfCOBSuD0B9YOpo6i2LqSu%2Biyr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMCVU%2BE%2Bh7HLs0cyUjKtwDKbMTPiN2YxaH23zBraateTjXzTJX9BbQ90XwbdugAR%2Bshl5Nd3nOp3OOJ1w68ouYuCihniw%2BjDCs0ceiqQ6puFHKO5j3okqoQ173c7lpj3qWk8vJYGSnPBuZlnnoc5n1GYFN1QISxIfQV%2BPsftcmJo36atwg5B1G6Qr729efIPjeFLwpPFLzM36ChKoWxyCMBPPgmH%2BQtMYEXR0B59aL%2FApbawG6H6oRolqxYDGGdsPEodki02ctw0dTZLq3RubEfN1kLK1JIbaT9E6EGp%2Fb0E8MmDnHlLd2CBsGwgDBVyi%2BtWNW6yrS67h5ddQhZGfankds8J06pA5P3ogyKyWTdlbApCLFpSCHpAYRoT%2FUsaVJlkqsNBxXAQRnt2Pz4TwmSzl8WaCpUn3h60%2BVtbErw2PrjSlJm2Cu5h5Z%2FnIzoAsmnHu4%2B1l90J6ekKPG%2BxYX791Xkh9X9F7qAnRPwFAX0%2B9Y65ypS2FlQAAxCUfp%2B%2FFKlnkLtFmSDYSqpTgGUPUOqMRlHUs5pOlMGkhnn2gfJA2JxXMQC6gj8gSikHxd7iY0rT0fioUVfQpm%2FVl9NSeSqQbjb5HH4Dg8HMteEUZpOkdKlzuF5jNWNLwJd7x0eBMxaktU0ECX5iGnSvIwj%2F2UvQY6pgF0XoJD1UE2Oiq8VvfAB%2Fa3L4z28OUexG2dMCOOo3yXpxZQRGbB8ytkwSoQDqmAAVM%2FMNPG6zA%2F95pJuC7wgSG0ZmFPEkV7T1I1BpMYDewXltyrjB%2FbtFAKVp8qWnI6pJcjGi6sotXAGtGfkhz42m%2FIg8Evik%2BDV7HBao4hmS5R%2FVctTWH6a91W2xQS9qUI2I2D3pZemhaLu5PUORr0fIDXz8Kl2ADy&X-Amz-Signature=ea522abde8ff045a996cd79418fdb6d2a1a98bf31ffaaac3c7645e9c9d5feca3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFHCQAWT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIBFLQUvtHRPphnzvgXjg5rs3Z%2Fu0sMGEv3hp4L2XfWs%2BAiAhUP5cfVvgvxdNY79nE%2BfCOBSuD0B9YOpo6i2LqSu%2Biyr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMCVU%2BE%2Bh7HLs0cyUjKtwDKbMTPiN2YxaH23zBraateTjXzTJX9BbQ90XwbdugAR%2Bshl5Nd3nOp3OOJ1w68ouYuCihniw%2BjDCs0ceiqQ6puFHKO5j3okqoQ173c7lpj3qWk8vJYGSnPBuZlnnoc5n1GYFN1QISxIfQV%2BPsftcmJo36atwg5B1G6Qr729efIPjeFLwpPFLzM36ChKoWxyCMBPPgmH%2BQtMYEXR0B59aL%2FApbawG6H6oRolqxYDGGdsPEodki02ctw0dTZLq3RubEfN1kLK1JIbaT9E6EGp%2Fb0E8MmDnHlLd2CBsGwgDBVyi%2BtWNW6yrS67h5ddQhZGfankds8J06pA5P3ogyKyWTdlbApCLFpSCHpAYRoT%2FUsaVJlkqsNBxXAQRnt2Pz4TwmSzl8WaCpUn3h60%2BVtbErw2PrjSlJm2Cu5h5Z%2FnIzoAsmnHu4%2B1l90J6ekKPG%2BxYX791Xkh9X9F7qAnRPwFAX0%2B9Y65ypS2FlQAAxCUfp%2B%2FFKlnkLtFmSDYSqpTgGUPUOqMRlHUs5pOlMGkhnn2gfJA2JxXMQC6gj8gSikHxd7iY0rT0fioUVfQpm%2FVl9NSeSqQbjb5HH4Dg8HMteEUZpOkdKlzuF5jNWNLwJd7x0eBMxaktU0ECX5iGnSvIwj%2F2UvQY6pgF0XoJD1UE2Oiq8VvfAB%2Fa3L4z28OUexG2dMCOOo3yXpxZQRGbB8ytkwSoQDqmAAVM%2FMNPG6zA%2F95pJuC7wgSG0ZmFPEkV7T1I1BpMYDewXltyrjB%2FbtFAKVp8qWnI6pJcjGi6sotXAGtGfkhz42m%2FIg8Evik%2BDV7HBao4hmS5R%2FVctTWH6a91W2xQS9qUI2I2D3pZemhaLu5PUORr0fIDXz8Kl2ADy&X-Amz-Signature=6d46ea4d71317e24d1aed8583c997ea89790d61a643cc6e0549ca6429a260403&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFHCQAWT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIBFLQUvtHRPphnzvgXjg5rs3Z%2Fu0sMGEv3hp4L2XfWs%2BAiAhUP5cfVvgvxdNY79nE%2BfCOBSuD0B9YOpo6i2LqSu%2Biyr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMCVU%2BE%2Bh7HLs0cyUjKtwDKbMTPiN2YxaH23zBraateTjXzTJX9BbQ90XwbdugAR%2Bshl5Nd3nOp3OOJ1w68ouYuCihniw%2BjDCs0ceiqQ6puFHKO5j3okqoQ173c7lpj3qWk8vJYGSnPBuZlnnoc5n1GYFN1QISxIfQV%2BPsftcmJo36atwg5B1G6Qr729efIPjeFLwpPFLzM36ChKoWxyCMBPPgmH%2BQtMYEXR0B59aL%2FApbawG6H6oRolqxYDGGdsPEodki02ctw0dTZLq3RubEfN1kLK1JIbaT9E6EGp%2Fb0E8MmDnHlLd2CBsGwgDBVyi%2BtWNW6yrS67h5ddQhZGfankds8J06pA5P3ogyKyWTdlbApCLFpSCHpAYRoT%2FUsaVJlkqsNBxXAQRnt2Pz4TwmSzl8WaCpUn3h60%2BVtbErw2PrjSlJm2Cu5h5Z%2FnIzoAsmnHu4%2B1l90J6ekKPG%2BxYX791Xkh9X9F7qAnRPwFAX0%2B9Y65ypS2FlQAAxCUfp%2B%2FFKlnkLtFmSDYSqpTgGUPUOqMRlHUs5pOlMGkhnn2gfJA2JxXMQC6gj8gSikHxd7iY0rT0fioUVfQpm%2FVl9NSeSqQbjb5HH4Dg8HMteEUZpOkdKlzuF5jNWNLwJd7x0eBMxaktU0ECX5iGnSvIwj%2F2UvQY6pgF0XoJD1UE2Oiq8VvfAB%2Fa3L4z28OUexG2dMCOOo3yXpxZQRGbB8ytkwSoQDqmAAVM%2FMNPG6zA%2F95pJuC7wgSG0ZmFPEkV7T1I1BpMYDewXltyrjB%2FbtFAKVp8qWnI6pJcjGi6sotXAGtGfkhz42m%2FIg8Evik%2BDV7HBao4hmS5R%2FVctTWH6a91W2xQS9qUI2I2D3pZemhaLu5PUORr0fIDXz8Kl2ADy&X-Amz-Signature=bff5ff0548d549f6812c4cb541cd55e3a9e356a34d5bab1a33ed25797b63613b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOTKZAUZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCd3Q%2FE2jjPoFKVjSECnk2fDM8owNkNhIfESjUy5ioRKgIhANavu%2BPzZ%2FNhlIHlNyfrsi6dp1XWwEND%2FJL1fiGpuagaKv8DCGgQABoMNjM3NDIzMTgzODA1Igx1NaiGhHjxzXohOMwq3AMw%2Bbfg%2FW%2B2wKYf4oQG%2FJ4MmPp5y3MdxqZNNxYUZHVf6FBn%2Fb0aqZQtCU2ca6EFYXoQYktCfDOLme3GdGwM2rnrHLu%2Fodilr1gfydto8sue7JCsBcViN74FX6M7tlFitPkSKfkakZi4h4iRl8XJgEal3QVvfRwSqmw0mFpnhN3A3nNWi%2BlnSFweMsRAAqcqrqwAkth4j4jkiYyyCjkDYjRdjSWA%2FUpJlKHqQuTNA35kyTM6lcPWIU%2F5IhRATzl6SjYjb9f7yK3u%2BC3vpMpdWJy6ic5xzkDDgle5kcL%2FjBkTwYO1e16xOR2upJSpiB1S%2BRDiZQh72mb47%2FN%2BYVSj06mlcMhL5sG4ZRXrab7yODP4c%2B1z3cVTnch19OdDHL%2B85NHprmUsCl6%2FF9bejnK73TQydxPK2IiK7MSJmO4Vq6XNbXQHkaszLXc2puyLNRXd7tVlOjRqutvngvSJLpVJaFL2vHl63NSzW3u9lPj%2FzOraNVS3ODF7NuLRrMdaqxoa9qj8G5y4JsWitMLu5KyyZe%2B5Pjsf9Iv57RIrKZp2kYEFMUJ4f3k3uLlY9viY1lshbtnsxHCWl83pld9CKVy6Tk3hSRIgeY0Yo32%2FJ4xveFj9gLteutfmLqXdzbYE0TC%2F%2FZS9BjqkAXyMkbb4fxH%2FPJHPbRTHPdKkdwfyuZTZylxYPjC2iIhoe1AKBjiPea8D9GrJpokNOR8O5SMnu9mGH4uTbBjIFV7Ast3qh1jkDCog7slszbYS2ABNt9QnBQumO0UrWiht2FFFBFlwfnz8v668HsIICCxkf1kvlMgEiAvTGaMoHAhoBJ%2BdGHlmuoAMQeCqbdYFqw6bjlFxnPee7UrJV%2FqIviEY%2BTrg&X-Amz-Signature=1514bf5907b2d284e582e6bf8569aec716f1952ff168b5386b8cd94f78968663&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOTKZAUZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCd3Q%2FE2jjPoFKVjSECnk2fDM8owNkNhIfESjUy5ioRKgIhANavu%2BPzZ%2FNhlIHlNyfrsi6dp1XWwEND%2FJL1fiGpuagaKv8DCGgQABoMNjM3NDIzMTgzODA1Igx1NaiGhHjxzXohOMwq3AMw%2Bbfg%2FW%2B2wKYf4oQG%2FJ4MmPp5y3MdxqZNNxYUZHVf6FBn%2Fb0aqZQtCU2ca6EFYXoQYktCfDOLme3GdGwM2rnrHLu%2Fodilr1gfydto8sue7JCsBcViN74FX6M7tlFitPkSKfkakZi4h4iRl8XJgEal3QVvfRwSqmw0mFpnhN3A3nNWi%2BlnSFweMsRAAqcqrqwAkth4j4jkiYyyCjkDYjRdjSWA%2FUpJlKHqQuTNA35kyTM6lcPWIU%2F5IhRATzl6SjYjb9f7yK3u%2BC3vpMpdWJy6ic5xzkDDgle5kcL%2FjBkTwYO1e16xOR2upJSpiB1S%2BRDiZQh72mb47%2FN%2BYVSj06mlcMhL5sG4ZRXrab7yODP4c%2B1z3cVTnch19OdDHL%2B85NHprmUsCl6%2FF9bejnK73TQydxPK2IiK7MSJmO4Vq6XNbXQHkaszLXc2puyLNRXd7tVlOjRqutvngvSJLpVJaFL2vHl63NSzW3u9lPj%2FzOraNVS3ODF7NuLRrMdaqxoa9qj8G5y4JsWitMLu5KyyZe%2B5Pjsf9Iv57RIrKZp2kYEFMUJ4f3k3uLlY9viY1lshbtnsxHCWl83pld9CKVy6Tk3hSRIgeY0Yo32%2FJ4xveFj9gLteutfmLqXdzbYE0TC%2F%2FZS9BjqkAXyMkbb4fxH%2FPJHPbRTHPdKkdwfyuZTZylxYPjC2iIhoe1AKBjiPea8D9GrJpokNOR8O5SMnu9mGH4uTbBjIFV7Ast3qh1jkDCog7slszbYS2ABNt9QnBQumO0UrWiht2FFFBFlwfnz8v668HsIICCxkf1kvlMgEiAvTGaMoHAhoBJ%2BdGHlmuoAMQeCqbdYFqw6bjlFxnPee7UrJV%2FqIviEY%2BTrg&X-Amz-Signature=fdb21ed0a677aee171d7753b20cb21a4557a51dcde30393753181de66a1cbe42&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOTKZAUZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCd3Q%2FE2jjPoFKVjSECnk2fDM8owNkNhIfESjUy5ioRKgIhANavu%2BPzZ%2FNhlIHlNyfrsi6dp1XWwEND%2FJL1fiGpuagaKv8DCGgQABoMNjM3NDIzMTgzODA1Igx1NaiGhHjxzXohOMwq3AMw%2Bbfg%2FW%2B2wKYf4oQG%2FJ4MmPp5y3MdxqZNNxYUZHVf6FBn%2Fb0aqZQtCU2ca6EFYXoQYktCfDOLme3GdGwM2rnrHLu%2Fodilr1gfydto8sue7JCsBcViN74FX6M7tlFitPkSKfkakZi4h4iRl8XJgEal3QVvfRwSqmw0mFpnhN3A3nNWi%2BlnSFweMsRAAqcqrqwAkth4j4jkiYyyCjkDYjRdjSWA%2FUpJlKHqQuTNA35kyTM6lcPWIU%2F5IhRATzl6SjYjb9f7yK3u%2BC3vpMpdWJy6ic5xzkDDgle5kcL%2FjBkTwYO1e16xOR2upJSpiB1S%2BRDiZQh72mb47%2FN%2BYVSj06mlcMhL5sG4ZRXrab7yODP4c%2B1z3cVTnch19OdDHL%2B85NHprmUsCl6%2FF9bejnK73TQydxPK2IiK7MSJmO4Vq6XNbXQHkaszLXc2puyLNRXd7tVlOjRqutvngvSJLpVJaFL2vHl63NSzW3u9lPj%2FzOraNVS3ODF7NuLRrMdaqxoa9qj8G5y4JsWitMLu5KyyZe%2B5Pjsf9Iv57RIrKZp2kYEFMUJ4f3k3uLlY9viY1lshbtnsxHCWl83pld9CKVy6Tk3hSRIgeY0Yo32%2FJ4xveFj9gLteutfmLqXdzbYE0TC%2F%2FZS9BjqkAXyMkbb4fxH%2FPJHPbRTHPdKkdwfyuZTZylxYPjC2iIhoe1AKBjiPea8D9GrJpokNOR8O5SMnu9mGH4uTbBjIFV7Ast3qh1jkDCog7slszbYS2ABNt9QnBQumO0UrWiht2FFFBFlwfnz8v668HsIICCxkf1kvlMgEiAvTGaMoHAhoBJ%2BdGHlmuoAMQeCqbdYFqw6bjlFxnPee7UrJV%2FqIviEY%2BTrg&X-Amz-Signature=6446d723468e1b841d6813cca523f5767c5f1c768b7e1f366c4edb8106d430af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOTKZAUZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCd3Q%2FE2jjPoFKVjSECnk2fDM8owNkNhIfESjUy5ioRKgIhANavu%2BPzZ%2FNhlIHlNyfrsi6dp1XWwEND%2FJL1fiGpuagaKv8DCGgQABoMNjM3NDIzMTgzODA1Igx1NaiGhHjxzXohOMwq3AMw%2Bbfg%2FW%2B2wKYf4oQG%2FJ4MmPp5y3MdxqZNNxYUZHVf6FBn%2Fb0aqZQtCU2ca6EFYXoQYktCfDOLme3GdGwM2rnrHLu%2Fodilr1gfydto8sue7JCsBcViN74FX6M7tlFitPkSKfkakZi4h4iRl8XJgEal3QVvfRwSqmw0mFpnhN3A3nNWi%2BlnSFweMsRAAqcqrqwAkth4j4jkiYyyCjkDYjRdjSWA%2FUpJlKHqQuTNA35kyTM6lcPWIU%2F5IhRATzl6SjYjb9f7yK3u%2BC3vpMpdWJy6ic5xzkDDgle5kcL%2FjBkTwYO1e16xOR2upJSpiB1S%2BRDiZQh72mb47%2FN%2BYVSj06mlcMhL5sG4ZRXrab7yODP4c%2B1z3cVTnch19OdDHL%2B85NHprmUsCl6%2FF9bejnK73TQydxPK2IiK7MSJmO4Vq6XNbXQHkaszLXc2puyLNRXd7tVlOjRqutvngvSJLpVJaFL2vHl63NSzW3u9lPj%2FzOraNVS3ODF7NuLRrMdaqxoa9qj8G5y4JsWitMLu5KyyZe%2B5Pjsf9Iv57RIrKZp2kYEFMUJ4f3k3uLlY9viY1lshbtnsxHCWl83pld9CKVy6Tk3hSRIgeY0Yo32%2FJ4xveFj9gLteutfmLqXdzbYE0TC%2F%2FZS9BjqkAXyMkbb4fxH%2FPJHPbRTHPdKkdwfyuZTZylxYPjC2iIhoe1AKBjiPea8D9GrJpokNOR8O5SMnu9mGH4uTbBjIFV7Ast3qh1jkDCog7slszbYS2ABNt9QnBQumO0UrWiht2FFFBFlwfnz8v668HsIICCxkf1kvlMgEiAvTGaMoHAhoBJ%2BdGHlmuoAMQeCqbdYFqw6bjlFxnPee7UrJV%2FqIviEY%2BTrg&X-Amz-Signature=e76a1bebe42a74fd187e1e124eddde8b167d193608bb865191fdcaee72256e36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOTKZAUZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCd3Q%2FE2jjPoFKVjSECnk2fDM8owNkNhIfESjUy5ioRKgIhANavu%2BPzZ%2FNhlIHlNyfrsi6dp1XWwEND%2FJL1fiGpuagaKv8DCGgQABoMNjM3NDIzMTgzODA1Igx1NaiGhHjxzXohOMwq3AMw%2Bbfg%2FW%2B2wKYf4oQG%2FJ4MmPp5y3MdxqZNNxYUZHVf6FBn%2Fb0aqZQtCU2ca6EFYXoQYktCfDOLme3GdGwM2rnrHLu%2Fodilr1gfydto8sue7JCsBcViN74FX6M7tlFitPkSKfkakZi4h4iRl8XJgEal3QVvfRwSqmw0mFpnhN3A3nNWi%2BlnSFweMsRAAqcqrqwAkth4j4jkiYyyCjkDYjRdjSWA%2FUpJlKHqQuTNA35kyTM6lcPWIU%2F5IhRATzl6SjYjb9f7yK3u%2BC3vpMpdWJy6ic5xzkDDgle5kcL%2FjBkTwYO1e16xOR2upJSpiB1S%2BRDiZQh72mb47%2FN%2BYVSj06mlcMhL5sG4ZRXrab7yODP4c%2B1z3cVTnch19OdDHL%2B85NHprmUsCl6%2FF9bejnK73TQydxPK2IiK7MSJmO4Vq6XNbXQHkaszLXc2puyLNRXd7tVlOjRqutvngvSJLpVJaFL2vHl63NSzW3u9lPj%2FzOraNVS3ODF7NuLRrMdaqxoa9qj8G5y4JsWitMLu5KyyZe%2B5Pjsf9Iv57RIrKZp2kYEFMUJ4f3k3uLlY9viY1lshbtnsxHCWl83pld9CKVy6Tk3hSRIgeY0Yo32%2FJ4xveFj9gLteutfmLqXdzbYE0TC%2F%2FZS9BjqkAXyMkbb4fxH%2FPJHPbRTHPdKkdwfyuZTZylxYPjC2iIhoe1AKBjiPea8D9GrJpokNOR8O5SMnu9mGH4uTbBjIFV7Ast3qh1jkDCog7slszbYS2ABNt9QnBQumO0UrWiht2FFFBFlwfnz8v668HsIICCxkf1kvlMgEiAvTGaMoHAhoBJ%2BdGHlmuoAMQeCqbdYFqw6bjlFxnPee7UrJV%2FqIviEY%2BTrg&X-Amz-Signature=b81b2ec1be60e9286ac5a530b117046d4c10a9bee7af654c0986098ec124803c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOTKZAUZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCd3Q%2FE2jjPoFKVjSECnk2fDM8owNkNhIfESjUy5ioRKgIhANavu%2BPzZ%2FNhlIHlNyfrsi6dp1XWwEND%2FJL1fiGpuagaKv8DCGgQABoMNjM3NDIzMTgzODA1Igx1NaiGhHjxzXohOMwq3AMw%2Bbfg%2FW%2B2wKYf4oQG%2FJ4MmPp5y3MdxqZNNxYUZHVf6FBn%2Fb0aqZQtCU2ca6EFYXoQYktCfDOLme3GdGwM2rnrHLu%2Fodilr1gfydto8sue7JCsBcViN74FX6M7tlFitPkSKfkakZi4h4iRl8XJgEal3QVvfRwSqmw0mFpnhN3A3nNWi%2BlnSFweMsRAAqcqrqwAkth4j4jkiYyyCjkDYjRdjSWA%2FUpJlKHqQuTNA35kyTM6lcPWIU%2F5IhRATzl6SjYjb9f7yK3u%2BC3vpMpdWJy6ic5xzkDDgle5kcL%2FjBkTwYO1e16xOR2upJSpiB1S%2BRDiZQh72mb47%2FN%2BYVSj06mlcMhL5sG4ZRXrab7yODP4c%2B1z3cVTnch19OdDHL%2B85NHprmUsCl6%2FF9bejnK73TQydxPK2IiK7MSJmO4Vq6XNbXQHkaszLXc2puyLNRXd7tVlOjRqutvngvSJLpVJaFL2vHl63NSzW3u9lPj%2FzOraNVS3ODF7NuLRrMdaqxoa9qj8G5y4JsWitMLu5KyyZe%2B5Pjsf9Iv57RIrKZp2kYEFMUJ4f3k3uLlY9viY1lshbtnsxHCWl83pld9CKVy6Tk3hSRIgeY0Yo32%2FJ4xveFj9gLteutfmLqXdzbYE0TC%2F%2FZS9BjqkAXyMkbb4fxH%2FPJHPbRTHPdKkdwfyuZTZylxYPjC2iIhoe1AKBjiPea8D9GrJpokNOR8O5SMnu9mGH4uTbBjIFV7Ast3qh1jkDCog7slszbYS2ABNt9QnBQumO0UrWiht2FFFBFlwfnz8v668HsIICCxkf1kvlMgEiAvTGaMoHAhoBJ%2BdGHlmuoAMQeCqbdYFqw6bjlFxnPee7UrJV%2FqIviEY%2BTrg&X-Amz-Signature=83b0b6f1c15c1f179b35015eccf5cc4e5f5df22aa28040b07a6289a18a8c491d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVNAZUFC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDZZYM5E%2BePUFkWWfqvhIp%2F9AY6jXiEr9sK8oxjz7hGpAIhAMCGqA4j%2B6sXimZj4sPkoRIQiprOrJSQsUqQ0ZpnCb80Kv8DCGgQABoMNjM3NDIzMTgzODA1Igzke7D%2BMLbl6NbqEFoq3ANjLnAe1xbWRdPYv4lA2HZ4Ra4PFr%2F6usFob8P8vKLvKgv1wG2PifGCvSr1AKLzxTWza%2BsSs0hDFwRewlAHDpvPGhkepAGZT83t0ig0RIJ2%2FBO92fa1ad3JzktnIqMThbL77NADdYAYJ5M5Ad2hO4wRFZrfT%2FvArEQinkPSQ3k98hgr82Kk3vobxJZhQ2J5DTehShDv%2BTFzWQU17LR28DDv%2Ficdayn756OQrSihK%2B0kmbOH6tVMvl0Wl4Wms6doHiKJ2HVaO2QVW2Io2%2BcbB3qmUlimE3QPnb6azIkaL8TkfQC89GWfZ01Ohc3obDs2pNF3ouW0xOvSpVFvl1I5QoskjuiW6VxcDC5Jd1mWShXU5siSvvi3%2Bdn%2B298QpaHV8%2FYuBjToIHkiKuk387WZcJ85goHrJU1OXhXFVeqcj7LhbEMY%2F4UAQt48O3ex3Q2DTNN0WRJ6%2BI3bztHOgh66fSahLRIgIiD%2BwMRWEjqhNx%2BzkOrFoD0%2FVoQ4lIwwytIpVybX%2BuPiamuJJ6%2BAzO4hTaUFm6AnLOFJnKiRZpiB6%2Bp%2F5lz5k8Y0wPdbUP8ej9MWaBzQN9BNj9rMVVFvCJx9AzwKXDbXTa2v%2BmXz78GPuQZYi6jK8JMe1NxF6spzGDCw%2FZS9BjqkAdHguQ8hYEJNGXBJ6SHYwiz1pcWwMb9L%2F5CPynazDkeAVCPVk1OEYyJnhuyjqWSlWyR1GZgP6gKG4PmyevuksD5JvJ7kgfUgsRrjK%2B4BDHnt7aTsAeu3lW4UfhvPrFnD6EKsPieEZXiKJ8FN13E%2FftDv4n%2F0NgE3xEVxUunqbgyuqGNaL4sqQQGB%2Bqc6q%2BQ20D03OH3MPvyVdxcoFzz8ArM%2FBp3q&X-Amz-Signature=9018abf75105a8bc9d7279219faea9dc8a57e403f2cc8b1152a14173558b7454&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNCH7OL3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQCjt1pURy8Oz7kQFnXZv04co42gWf1pv1dR8TAJmNYArwIgNa0l3ZOplFIdgaoAajLijrHt7pNUypZaeCsVZMIbNioq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDLQlPyKifzTeZuOKIyrcA7GojR1BRW9QkDC0aTD3GDZUAFj25euHLyoxJIfBcElq1NQ3KWwev7pS0NdVoCaWUx10CKlG9zDkGvNJPYUyFX%2BClfIlwrEkpYM895XrCTcObAWWJmY1dM1iU5h4ChIxl6th4LmwDflvLaS3x%2BWgDWorAwlfh73NpUqEi7GdywrYVBwAIyzOeAchf40F7XKiugDP1WCOwfKDtIDU2TzR7VaZ6PgcY6Yao60VzaAkV1RQUjRC2PhATW3DyoFA55clFC0LjmJYWPAav3rdYIS3KzQFrstDINdPWxqD0BeGODEdGmd9nVhvtt7Bz0zhUwcLMbGoV2H44oNPGwm8pGOKnO0NcE20tQNEImlasgZoINzvcWX5ovOdZaqmsrPiRQNXCBqmMivZWv8cDwoxfSh6bqfw65N89LWX7B4pI5tz3pyskJSRjRQ0hidafEFc0Kn9oUHLAWPe476BFvZL6t%2Fs3QYMCc790PELBR4tVp2dsBDOnirL%2BcF5S3re%2BuWw43YOqq6G2eFsN43E6oaZhLbbcsEiknYN6NVh5aOSEgZxFRD76OjPdDSr0uIlzXMGW%2FGfT94Ma5b70uFKUtEXajEZdUcrJsGFugMgRWedG3aqP1i%2BJvdq%2BAHlEodmMORNMMP9lL0GOqUB83m4DjQXylWVdytxxp8KmL%2BY2DLjqLixjvy%2B01MoXzqBiSR2u1%2BGA0kOLfCL%2BZtDOfDC7XgsDPXR36IM%2BENCAlXaxz%2B1%2BdOINXpBWuhq5HfonOj3HPdaGJUZQ58Gv2SOb1uYVd%2BkrqAMJv7lp6w%2BXD18DF0mrFfdnnCyLZfgfPODq7gv4Z3ne3EJ1tvoCTlXzEDrzCmLKVw3zpHbTgJO3%2FaXjaR0&X-Amz-Signature=4959e2f83fa08f574c62adac1674567e21459fc2b24720e5d288dbcc7a3a88bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOTKZAUZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCd3Q%2FE2jjPoFKVjSECnk2fDM8owNkNhIfESjUy5ioRKgIhANavu%2BPzZ%2FNhlIHlNyfrsi6dp1XWwEND%2FJL1fiGpuagaKv8DCGgQABoMNjM3NDIzMTgzODA1Igx1NaiGhHjxzXohOMwq3AMw%2Bbfg%2FW%2B2wKYf4oQG%2FJ4MmPp5y3MdxqZNNxYUZHVf6FBn%2Fb0aqZQtCU2ca6EFYXoQYktCfDOLme3GdGwM2rnrHLu%2Fodilr1gfydto8sue7JCsBcViN74FX6M7tlFitPkSKfkakZi4h4iRl8XJgEal3QVvfRwSqmw0mFpnhN3A3nNWi%2BlnSFweMsRAAqcqrqwAkth4j4jkiYyyCjkDYjRdjSWA%2FUpJlKHqQuTNA35kyTM6lcPWIU%2F5IhRATzl6SjYjb9f7yK3u%2BC3vpMpdWJy6ic5xzkDDgle5kcL%2FjBkTwYO1e16xOR2upJSpiB1S%2BRDiZQh72mb47%2FN%2BYVSj06mlcMhL5sG4ZRXrab7yODP4c%2B1z3cVTnch19OdDHL%2B85NHprmUsCl6%2FF9bejnK73TQydxPK2IiK7MSJmO4Vq6XNbXQHkaszLXc2puyLNRXd7tVlOjRqutvngvSJLpVJaFL2vHl63NSzW3u9lPj%2FzOraNVS3ODF7NuLRrMdaqxoa9qj8G5y4JsWitMLu5KyyZe%2B5Pjsf9Iv57RIrKZp2kYEFMUJ4f3k3uLlY9viY1lshbtnsxHCWl83pld9CKVy6Tk3hSRIgeY0Yo32%2FJ4xveFj9gLteutfmLqXdzbYE0TC%2F%2FZS9BjqkAXyMkbb4fxH%2FPJHPbRTHPdKkdwfyuZTZylxYPjC2iIhoe1AKBjiPea8D9GrJpokNOR8O5SMnu9mGH4uTbBjIFV7Ast3qh1jkDCog7slszbYS2ABNt9QnBQumO0UrWiht2FFFBFlwfnz8v668HsIICCxkf1kvlMgEiAvTGaMoHAhoBJ%2BdGHlmuoAMQeCqbdYFqw6bjlFxnPee7UrJV%2FqIviEY%2BTrg&X-Amz-Signature=53d428bff7da93f6332bfc32c6995e39a9daeff4f0498f6b982e68f17ef1c78e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOTKZAUZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCd3Q%2FE2jjPoFKVjSECnk2fDM8owNkNhIfESjUy5ioRKgIhANavu%2BPzZ%2FNhlIHlNyfrsi6dp1XWwEND%2FJL1fiGpuagaKv8DCGgQABoMNjM3NDIzMTgzODA1Igx1NaiGhHjxzXohOMwq3AMw%2Bbfg%2FW%2B2wKYf4oQG%2FJ4MmPp5y3MdxqZNNxYUZHVf6FBn%2Fb0aqZQtCU2ca6EFYXoQYktCfDOLme3GdGwM2rnrHLu%2Fodilr1gfydto8sue7JCsBcViN74FX6M7tlFitPkSKfkakZi4h4iRl8XJgEal3QVvfRwSqmw0mFpnhN3A3nNWi%2BlnSFweMsRAAqcqrqwAkth4j4jkiYyyCjkDYjRdjSWA%2FUpJlKHqQuTNA35kyTM6lcPWIU%2F5IhRATzl6SjYjb9f7yK3u%2BC3vpMpdWJy6ic5xzkDDgle5kcL%2FjBkTwYO1e16xOR2upJSpiB1S%2BRDiZQh72mb47%2FN%2BYVSj06mlcMhL5sG4ZRXrab7yODP4c%2B1z3cVTnch19OdDHL%2B85NHprmUsCl6%2FF9bejnK73TQydxPK2IiK7MSJmO4Vq6XNbXQHkaszLXc2puyLNRXd7tVlOjRqutvngvSJLpVJaFL2vHl63NSzW3u9lPj%2FzOraNVS3ODF7NuLRrMdaqxoa9qj8G5y4JsWitMLu5KyyZe%2B5Pjsf9Iv57RIrKZp2kYEFMUJ4f3k3uLlY9viY1lshbtnsxHCWl83pld9CKVy6Tk3hSRIgeY0Yo32%2FJ4xveFj9gLteutfmLqXdzbYE0TC%2F%2FZS9BjqkAXyMkbb4fxH%2FPJHPbRTHPdKkdwfyuZTZylxYPjC2iIhoe1AKBjiPea8D9GrJpokNOR8O5SMnu9mGH4uTbBjIFV7Ast3qh1jkDCog7slszbYS2ABNt9QnBQumO0UrWiht2FFFBFlwfnz8v668HsIICCxkf1kvlMgEiAvTGaMoHAhoBJ%2BdGHlmuoAMQeCqbdYFqw6bjlFxnPee7UrJV%2FqIviEY%2BTrg&X-Amz-Signature=4040022a2ff81ac3d7a12d3e2e1dc6299304f521852e2c464bf414a4ff4416dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOTKZAUZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCd3Q%2FE2jjPoFKVjSECnk2fDM8owNkNhIfESjUy5ioRKgIhANavu%2BPzZ%2FNhlIHlNyfrsi6dp1XWwEND%2FJL1fiGpuagaKv8DCGgQABoMNjM3NDIzMTgzODA1Igx1NaiGhHjxzXohOMwq3AMw%2Bbfg%2FW%2B2wKYf4oQG%2FJ4MmPp5y3MdxqZNNxYUZHVf6FBn%2Fb0aqZQtCU2ca6EFYXoQYktCfDOLme3GdGwM2rnrHLu%2Fodilr1gfydto8sue7JCsBcViN74FX6M7tlFitPkSKfkakZi4h4iRl8XJgEal3QVvfRwSqmw0mFpnhN3A3nNWi%2BlnSFweMsRAAqcqrqwAkth4j4jkiYyyCjkDYjRdjSWA%2FUpJlKHqQuTNA35kyTM6lcPWIU%2F5IhRATzl6SjYjb9f7yK3u%2BC3vpMpdWJy6ic5xzkDDgle5kcL%2FjBkTwYO1e16xOR2upJSpiB1S%2BRDiZQh72mb47%2FN%2BYVSj06mlcMhL5sG4ZRXrab7yODP4c%2B1z3cVTnch19OdDHL%2B85NHprmUsCl6%2FF9bejnK73TQydxPK2IiK7MSJmO4Vq6XNbXQHkaszLXc2puyLNRXd7tVlOjRqutvngvSJLpVJaFL2vHl63NSzW3u9lPj%2FzOraNVS3ODF7NuLRrMdaqxoa9qj8G5y4JsWitMLu5KyyZe%2B5Pjsf9Iv57RIrKZp2kYEFMUJ4f3k3uLlY9viY1lshbtnsxHCWl83pld9CKVy6Tk3hSRIgeY0Yo32%2FJ4xveFj9gLteutfmLqXdzbYE0TC%2F%2FZS9BjqkAXyMkbb4fxH%2FPJHPbRTHPdKkdwfyuZTZylxYPjC2iIhoe1AKBjiPea8D9GrJpokNOR8O5SMnu9mGH4uTbBjIFV7Ast3qh1jkDCog7slszbYS2ABNt9QnBQumO0UrWiht2FFFBFlwfnz8v668HsIICCxkf1kvlMgEiAvTGaMoHAhoBJ%2BdGHlmuoAMQeCqbdYFqw6bjlFxnPee7UrJV%2FqIviEY%2BTrg&X-Amz-Signature=e872394811f34e623c014c59577455050fc1b8cd2c0b073bfca6bac96573eee4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDRMY7GZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDcCUEGwEVaRgpZ0x6iogKM22ePEVBEew2A%2FbQxntA0twIhAIW%2FRdJqw2gfe%2FT8SLTMJuDZ1nYpLxF%2FSDQBKbJV4bQeKv8DCGgQABoMNjM3NDIzMTgzODA1IgzTiW4AadPpBPEePpsq3AMAF62nUzIIOPG1k4WWcaFkW6uZxBKh758k%2BYg27mqy9qh8SI4r3oEXb2Qeq2ouSbIv7NcD4DdKh4RhFwOHqkDKHu8ieRbjehDV88l6NJ%2By9NnGve1jJkpvqxbpoS9cNuU0eDZgpcEMimfb8OarCpeKWhJuUSO3Cv47C5HU527P8%2FURnJ63xW2zezWQIEGANv9%2FCzRDK4XPq5JrOBXcxk4kA7RtlHHgxCPBNBr4Ys0OuHezkzz1rdD6Aq%2F281N77SqUazHcA4cMFspEG0LowMNsLT9wnOjY0G5yIIHS6m5FRjs1HBcL4W5e4jRaoe%2Br1f0qj0blic45g7%2F8%2BxgmtNdEi6ee1iMUGSeLofRZOkdSuK1%2FQ595UE2vZxCLbQXTL007Coed2J%2BMKTgH4i%2BmkkBqfAZRIDqFQTM7o9hlLKqaedAS3qowaFAQEc%2B9fHNZZ6NSlrYfEsdCzq27BNhPG1BtAUQzBjt18uyB7xN6rN6EnyDZAOjW4rNE3B%2B9qdXSLgAg4A%2BaU70%2FmcjcPUrhIQU88%2BM0tuNtAKvkueaoZ5FwIWKEL31OY3yVvRJtEtUr0Wcm09n1O4NFFc%2Bg52bwWRTt7gjuG7fQZP6JIW5gcCIjrTvyXJtruNesWZmgxjCk%2FZS9BjqkAZi9vDf1u9jl6rCXVcgrt6jynph0PWX4L%2F0X%2Bb8piwAZ4lvdzCYROJq%2FS2nDCMlrfUhf5zEQBtMp%2BxBHTjOz%2FFNAUAPhWx9WQr7Os4TH3pXY4CiHEICtwTJhzjZ35wlcQeq%2BqbzuOjdI5WUTwOGH05Ozuv%2BZYgXCdSKlhJ%2BMoenc3hooq1ng9%2F8hPav4aq8cjlzxGw2INy1EAlvaky0RkzuX114q&X-Amz-Signature=19e3ba09c911bb622019b473525be9ab1f0f3ed32162cbe0793ccc3bbcc39802&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QM55QRIO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIGoVlJU2NatYBzR7%2Bc1hNllfFLiyg%2F9uA%2FYH%2FxAfueuoAiEA2SB1Hf0YLU%2FeJzCMMorJwEGPyTKs2JcS5Bjhafylxkkq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDLX4C8vzbRBJoPMenCrcA82FWc3NQB%2FcEHOHRxISSRcLRi0vgLNg%2BdUy2zZoNnCmxorQ9Cg5BzfwhmsHNgaNtGpf3dhYUzYFd4jB2lgmvHfw8oEBEYLT3spC%2BmoKT6zAx9F0tynmhwrV3HC1Bq1T%2BFBO72RxEAa1Ide1cK3upm2u2XXSxPjwEok0iq3Xhuo4rr7Bil63SeKF1wBMtJedjBaTCaK0BSPTGeePJa0mIfiY8TdQaHCcYY%2FWu0PhRvquKhaA8RCxj534xixVFetVmM0iwnKH6X1LXpKRHCtIMr0aXVzpsRMr7b8J%2FbED3vsUa%2Bizrizud5BO3Len2s3PHHSFmeTfHArlSCp%2Bq0UqF%2F3IJSXqu3KZkXUIP7Dq5xbxvxOdK1dMBR2E6qWo8jCEgI7RQfg10SGP8e7geRL%2F7OeLTaZvC3ES2T9lDlPKz4JsDNjcC8epNmQYWFENK9wio3eqwbWRlRkIwRhtnYyAmMW0tqWoinGGrpzj8bUEYB0aU5Aqh6GsxLrUIqBFlJUxfGE6hAVcVs2mF65jLz2S9Om8hobIaXCYlsK%2F1FQjcnX29cpPr8wXS%2Btom1HyAdL%2FhWhvcv280KEkpPc%2FgJ13JnE5b90XaPgU9kYxLwQhshNxx4xF0VsMTB%2F35FK8MNj9lL0GOqUBdiD0Bv3VKgdPWJD%2FfZ21hb69xbdB0SnWSfsgqpMpiMT9oxU6ltQXWX9GS02oAkh83ZBcIRXgsQLQrR0zp5S1i3HcPND3hpStjeTPkrADdHdZ7poeFm6Z8Euj%2BnegepVkzCEDEsZqmIx74Lfcu0zkHH6iom7q4vMGrrpozUBV8Pjg1VACZyBXNR1e%2Bf%2B8CIrUyb67qLNvzVZZ4Oj270ICdqs1yrTP&X-Amz-Signature=fce80061f6f54664ee5df40fff9e1d32cc1142772aba5f9f11d7570811bc67de&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RKWCDHG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQCwEQ2w%2B%2Bd33DNbFjbBC6HrOamTJVg3IqjRKx2aym4YNwIhAOOlFGXuWoNxRYiI%2BfWBlMickfDcUkzRTCkMKAEl3WSJKv8DCGgQABoMNjM3NDIzMTgzODA1Igz8iyMNch7gS%2FBs1J0q3AMPkiiMilDDNo9mOd%2FeC5F6JcFeSSdenegAw6I%2FiJrl6T%2BojGA4VH0mVvPQAZmYvLP3xxPGpeNM7Y7RMCmqBGGq9uWE4YycBDHw2%2FLu0B1Z8wKbSR6pUyqeeRuBuO0aeFOlRkDFf%2FlecBhltjNGiwUY%2FqvjhaOoVHXRRTDD5qXqHfg72HkFmIgK%2FB7kQB5IBksX1DMdtj00TGwuRzu1kAZkTWhAGrNQVF3Q%2FwCThYr527JjFq%2BCaEoqa7Vp7Gcwqh5H1%2BPBiwmFg9t8vOlVHe4hDe8qWXl5vkJXVjh3QSxighhNE3ygxOMY3WidiZRqU2ybMPsUZGgBxTpgEllFnAZgF6lYBVoKT78gKBRr8xLAkotLVwTjNXc1UTarSMFz%2BwfVOtKqRq%2FZHoTTGDJ5RMts3sSDIaTQ30PmoUFhuTkBpBFV%2BRQX2p%2BI7oYhyLRir%2FjoFw5%2BC83OEcr5x%2B4f5K8shAKku2%2B0pDnmn8HBlfApa%2B%2Fg2Y2OM6DIEEX1QsFtVHmAmJ92X63t%2BEoW1%2FccAYzlz67SjACVxTctmsxANOV%2FD3z0U3oOYlZFWNk%2BzVlRa173u9p0Z1incnydJcbbPHtlD8%2F7pNnj1iPC%2BbshI5NaP%2BOxjf%2FAvtDARI7nmzDo%2FZS9BjqkAdYyfH7bweGqE5vs1qzx5PNVufYO2Z13psyb5okFQVQVRsAP2zw7qKBTdHicR10A1KES%2BCL%2BZ6HKfRHdtghXDc%2BomDXBwSVL51qeH6ZpviHHkI4YKmsv9PcZQZ%2BzGr4wY8mrVFLTsLovgQ%2FqRkinACdIdaPEDJVWUtZ%2FrzsCojrEHAUDyi7Ogz2LB49%2FE1Y%2Bv2qkuInJ8wyX7aLzlJ0vQh2jNfJ0&X-Amz-Signature=f591368d832cd909665aa3318ed28d0345c45f59b437fbcf03535dfc25a76578&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BHL6MR2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIB5FV5PiZnHcjm1IxSXxG%2F%2FcVPzKjxvhs2MiEP8SQ9H9AiAF4J5WmlTmBMDtVhyof5fZzbu9oLLvHjhhommU0UrC0Sr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMeTQ1bW8fAiGqWWK2KtwDPlUDfzpKjmk5nHJmDfEMtKHHdzBfb7qTX1TqqquW8yWLyjxWQXceQs%2B0rt1fjWvOXwIzuJBECkNouNX2aC%2BgBO5kzVipoIt9pH%2BmcDH7h3yTQpj0bRPVYsjSaStNHjfx1rk7dJ2Uq5sSh4qxnx%2BWdi7XhS2N%2BxzZRWc20N7ExMwuVaW8Uuhat98vwdpat%2Bqq7BhgGGzemLsvH0CVgGvEArb0pG2q1MdpMXP2qneSkmentfMsV%2Bge5efMkZyPaSlKwN7mNilN5d46EX1HZ8MQGD479iK9D0E1pWXqMi31ynld4vt3vEQHXuSiBMpfBaRexmSPQvzOVzNBV0Omef9iKBInl%2Fj385rKJUW0QjrErRkK35KyUaSre8zJHRHfK%2BnLUUNcKS2h6mAK0HEU3RKjpGhQF%2Byhz8YRh7%2F1yZQAZpgVI45AnRQQD7LzdSf2PMJ%2B1V4ouJUnEZPSHD0AiOAiVbJMsFIg2auZgDNk8iDJiAm6pqm8xv2gyla1xffcqxwwr60fiVeFQGgHtnP2plQI%2FKqTr7SpizW2ISKrZi86t11itJV10ajEDO9qKWdCTKeghkGd5YQCCQiWjfa46FogJoc0wzTJLXmpFgbGOG4IyjPCbK90IRuniyLehxowqf2UvQY6pgF1TuDXFPs7dHeu5zP6Gh6lC2vWOSbVo1J36Lk9fj2XN5eM6ahXzaL1qK27hW%2F%2B3%2BQcQUSjBj9Xudgfvz5ygChqv2DXntRV5tPLQqPnDJ%2F7BEGgao4Lgf1tqP%2Fl8gipjytuCWhA46CmTwv%2Fsu%2BJBC5zvz09KbNxZTi0Aez81Qf8BYP0nYj7YQKXqjRQctvX4g6seLOyeargb%2BfPj1%2FSNI8SK%2BmU4g9g&X-Amz-Signature=4ba973df17d65265e0d1dae3edae2df9455960c10be36b91e8e07ad9c65c073d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BHL6MR2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIB5FV5PiZnHcjm1IxSXxG%2F%2FcVPzKjxvhs2MiEP8SQ9H9AiAF4J5WmlTmBMDtVhyof5fZzbu9oLLvHjhhommU0UrC0Sr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMeTQ1bW8fAiGqWWK2KtwDPlUDfzpKjmk5nHJmDfEMtKHHdzBfb7qTX1TqqquW8yWLyjxWQXceQs%2B0rt1fjWvOXwIzuJBECkNouNX2aC%2BgBO5kzVipoIt9pH%2BmcDH7h3yTQpj0bRPVYsjSaStNHjfx1rk7dJ2Uq5sSh4qxnx%2BWdi7XhS2N%2BxzZRWc20N7ExMwuVaW8Uuhat98vwdpat%2Bqq7BhgGGzemLsvH0CVgGvEArb0pG2q1MdpMXP2qneSkmentfMsV%2Bge5efMkZyPaSlKwN7mNilN5d46EX1HZ8MQGD479iK9D0E1pWXqMi31ynld4vt3vEQHXuSiBMpfBaRexmSPQvzOVzNBV0Omef9iKBInl%2Fj385rKJUW0QjrErRkK35KyUaSre8zJHRHfK%2BnLUUNcKS2h6mAK0HEU3RKjpGhQF%2Byhz8YRh7%2F1yZQAZpgVI45AnRQQD7LzdSf2PMJ%2B1V4ouJUnEZPSHD0AiOAiVbJMsFIg2auZgDNk8iDJiAm6pqm8xv2gyla1xffcqxwwr60fiVeFQGgHtnP2plQI%2FKqTr7SpizW2ISKrZi86t11itJV10ajEDO9qKWdCTKeghkGd5YQCCQiWjfa46FogJoc0wzTJLXmpFgbGOG4IyjPCbK90IRuniyLehxowqf2UvQY6pgF1TuDXFPs7dHeu5zP6Gh6lC2vWOSbVo1J36Lk9fj2XN5eM6ahXzaL1qK27hW%2F%2B3%2BQcQUSjBj9Xudgfvz5ygChqv2DXntRV5tPLQqPnDJ%2F7BEGgao4Lgf1tqP%2Fl8gipjytuCWhA46CmTwv%2Fsu%2BJBC5zvz09KbNxZTi0Aez81Qf8BYP0nYj7YQKXqjRQctvX4g6seLOyeargb%2BfPj1%2FSNI8SK%2BmU4g9g&X-Amz-Signature=fa35b3d1138fa67f173d3873bca97b9b6a380e3a8a01e6bb9016097b8b8c45c3&X-Amz-SignedHeaders=host&x-id=GetObject)

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
