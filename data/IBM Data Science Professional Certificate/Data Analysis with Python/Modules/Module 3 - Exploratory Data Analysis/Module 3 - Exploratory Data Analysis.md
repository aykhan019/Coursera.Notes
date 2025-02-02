

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM433BSP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFP8eIzYf7RN%2FTu5PVn1CCtGQgvUYbbKIiatBSy8LH8rAiAqZP7opFake6%2BgIxWZCIzHETQ9%2F8X%2BcYKaReAhaF4piSqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXd7aIbEcVuVOTroEKtwDiilxphr7dUKGrUYkvDyJPe1uxegbOLZugdg7xdnAb0L8BetUBEYovICobqN5NFimA8O6EO2%2FIdPIqE1RXSn5WDDHDsXj8I3veS3%2FcHF4xqTevnGAH32e9fNGMzfebF1ggAORKwa0UADOABV53FUl1wPK8zfWEetPewQ%2BpUb5PlM9qlIBrJoH9SrVJG7%2FSlf%2BvuCXyFOnfNy7YppK99%2FSr27ckgcsKzkLX1ElY9GEbmJyWDvYSqACn%2FFbu3MTWEYlPkFWBOGw197KoQTSIn0EH4txFlgjIiKPpLyN9ey57mwRWngZk%2BWfAxJrEMEwKyQSAQDdUAN04O53SpX5moFmZSip8isrAxYK666yRZ7aRh2V%2Fz0HcPFHB51J%2BWpIoURvp92MBFQkHZ7WnfNMEHzVVRzvMJjT2OhRj5njQoIIGmBCWj7YJAWyB8Eco3ijcTHCDThymX6pede2PljxDuXtETq%2BpWPdv2kcKQYlsCtkxr1lBuKioprSeg%2BowHeQJ%2FNm54mpur4wQYQpofDg9ZwjtO8tlY80FZgiym3uWeb%2BxFRWAqYcoHxv%2FvrJLl3K1IX5QyqGCKQNkBYCpL%2B9SPZeGrBNEP950u2l76X%2F4LUo35TEy6bNQaiiTrsEmagwoOH7vAY6pgFVBf7o7Zu3mikprEe7Oblrt0sLW%2BHziptUztKafo%2FquJQa7CMuDIlUTifNcspvsuubabng6sY2utVh4RB95o%2BxlLV1hjMhiVjEsScs3Q4xIA6Hgrw30Wh%2BKyFf74qOQ0uP%2FLjrKrb2AYFtfXfG2pIwZVvuZVgFpOF%2B10bCrpMF7phWH2ivYrQ6LO15N%2B9lulCTQVq%2BWIVkM%2B1DVlkcjmjjifV7LU%2FP&X-Amz-Signature=3a28971cb99fcb9eb545fba311e8bd92bb5d6000d2af768a29169407a1ec262a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM433BSP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFP8eIzYf7RN%2FTu5PVn1CCtGQgvUYbbKIiatBSy8LH8rAiAqZP7opFake6%2BgIxWZCIzHETQ9%2F8X%2BcYKaReAhaF4piSqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXd7aIbEcVuVOTroEKtwDiilxphr7dUKGrUYkvDyJPe1uxegbOLZugdg7xdnAb0L8BetUBEYovICobqN5NFimA8O6EO2%2FIdPIqE1RXSn5WDDHDsXj8I3veS3%2FcHF4xqTevnGAH32e9fNGMzfebF1ggAORKwa0UADOABV53FUl1wPK8zfWEetPewQ%2BpUb5PlM9qlIBrJoH9SrVJG7%2FSlf%2BvuCXyFOnfNy7YppK99%2FSr27ckgcsKzkLX1ElY9GEbmJyWDvYSqACn%2FFbu3MTWEYlPkFWBOGw197KoQTSIn0EH4txFlgjIiKPpLyN9ey57mwRWngZk%2BWfAxJrEMEwKyQSAQDdUAN04O53SpX5moFmZSip8isrAxYK666yRZ7aRh2V%2Fz0HcPFHB51J%2BWpIoURvp92MBFQkHZ7WnfNMEHzVVRzvMJjT2OhRj5njQoIIGmBCWj7YJAWyB8Eco3ijcTHCDThymX6pede2PljxDuXtETq%2BpWPdv2kcKQYlsCtkxr1lBuKioprSeg%2BowHeQJ%2FNm54mpur4wQYQpofDg9ZwjtO8tlY80FZgiym3uWeb%2BxFRWAqYcoHxv%2FvrJLl3K1IX5QyqGCKQNkBYCpL%2B9SPZeGrBNEP950u2l76X%2F4LUo35TEy6bNQaiiTrsEmagwoOH7vAY6pgFVBf7o7Zu3mikprEe7Oblrt0sLW%2BHziptUztKafo%2FquJQa7CMuDIlUTifNcspvsuubabng6sY2utVh4RB95o%2BxlLV1hjMhiVjEsScs3Q4xIA6Hgrw30Wh%2BKyFf74qOQ0uP%2FLjrKrb2AYFtfXfG2pIwZVvuZVgFpOF%2B10bCrpMF7phWH2ivYrQ6LO15N%2B9lulCTQVq%2BWIVkM%2B1DVlkcjmjjifV7LU%2FP&X-Amz-Signature=ffd4566becad4712ada462885b87f0dae566564ce1c1dab4b70d960c77e01fa6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM433BSP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFP8eIzYf7RN%2FTu5PVn1CCtGQgvUYbbKIiatBSy8LH8rAiAqZP7opFake6%2BgIxWZCIzHETQ9%2F8X%2BcYKaReAhaF4piSqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXd7aIbEcVuVOTroEKtwDiilxphr7dUKGrUYkvDyJPe1uxegbOLZugdg7xdnAb0L8BetUBEYovICobqN5NFimA8O6EO2%2FIdPIqE1RXSn5WDDHDsXj8I3veS3%2FcHF4xqTevnGAH32e9fNGMzfebF1ggAORKwa0UADOABV53FUl1wPK8zfWEetPewQ%2BpUb5PlM9qlIBrJoH9SrVJG7%2FSlf%2BvuCXyFOnfNy7YppK99%2FSr27ckgcsKzkLX1ElY9GEbmJyWDvYSqACn%2FFbu3MTWEYlPkFWBOGw197KoQTSIn0EH4txFlgjIiKPpLyN9ey57mwRWngZk%2BWfAxJrEMEwKyQSAQDdUAN04O53SpX5moFmZSip8isrAxYK666yRZ7aRh2V%2Fz0HcPFHB51J%2BWpIoURvp92MBFQkHZ7WnfNMEHzVVRzvMJjT2OhRj5njQoIIGmBCWj7YJAWyB8Eco3ijcTHCDThymX6pede2PljxDuXtETq%2BpWPdv2kcKQYlsCtkxr1lBuKioprSeg%2BowHeQJ%2FNm54mpur4wQYQpofDg9ZwjtO8tlY80FZgiym3uWeb%2BxFRWAqYcoHxv%2FvrJLl3K1IX5QyqGCKQNkBYCpL%2B9SPZeGrBNEP950u2l76X%2F4LUo35TEy6bNQaiiTrsEmagwoOH7vAY6pgFVBf7o7Zu3mikprEe7Oblrt0sLW%2BHziptUztKafo%2FquJQa7CMuDIlUTifNcspvsuubabng6sY2utVh4RB95o%2BxlLV1hjMhiVjEsScs3Q4xIA6Hgrw30Wh%2BKyFf74qOQ0uP%2FLjrKrb2AYFtfXfG2pIwZVvuZVgFpOF%2B10bCrpMF7phWH2ivYrQ6LO15N%2B9lulCTQVq%2BWIVkM%2B1DVlkcjmjjifV7LU%2FP&X-Amz-Signature=ea386cce8252419ea40fee45ad94de7a83f02fa037e9e2708faa6fc5f4854bd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WSVHWE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpZXJtG57oGLrMoLDPL3zfFZMlcIXJ9HBtTZn7WzVUEgIgdq9CGyqknYtU2F5HVsv%2FxEA%2BouKv6BORMeA1JJR3lmwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPt1wLuzBWHq2iyGCrcAzWpvXRu%2BUgxCYZ65%2BMOf6PK2pxlOb%2BznO7oo7dJpZaFEurArguVqmjr57%2BLj0DOWm0NULYPg0dxNkS%2FrOsE3NW3zcmufJw0%2B85v2mJAZ%2Bwh8L1JARUFJviqMbX1hjL659SdbrfZ9rXxBzUhU26veKfJVSdDKPBfKMhBiEMTt13B4B1mAnXZ22H%2FQ0qk5%2FbaKTOt0YH49zqS3h45tny99ewU06SmUyp89jF2qcmXr3aTh%2B6g%2FEiFBn%2FofR5fdeQnsFM5kcYbnZ75OZgd%2ByMLvR9G70qg5xitP5LNO7r1efDADuw%2BwZsr1BHhLw8is%2BlsZDw20EwPA2CbGKcB37hcNrILNXzQtZxYYLv40VIr1pEdpdYiNe2mColM%2BUB0dREYjw%2BcXU2ZNqOW2m8dMpoVCzWfvzc6Paykoc8NIHilOGt%2B4drov%2ByW%2BZ7iVPdNyU76qxRCuzNA7zTBzZzgBZht2VKLMYJRCtdZmxKs6Z7IHpvMVKWsJv8BfyOYLGOCxjXkENla1qdsnFeR0I809dMKTUIx%2FVGca579HKvxknrY7qcE7ZgCcx0j00Kr9y8q7g1rx25ckfBhkc4t4C7MXJ9IktSEgA%2FLTcH9ZhgGUKJBtaMBIBo6%2Bg%2Fswfm44%2FllMPeb%2FLwGOqUBB8cuyA0dAktx%2BmF%2F0m1S7MDMN5N6%2B47tMYjKF71a5EqwtQQCudioQoR4I4v640ViCShG8%2BTHsylGCZl1SxDuHkDkXcdBSozgfnj78AhNneJAcZzVPaDHWokhq5zR3mbXxGPEd%2F%2BBpP2s2fEsMUlJA6l%2B6yLUCDTDOMtv0bVFAWZWf2W6E63w%2B0CFSJGtgafvece2VmlRfKVEHlz41EA3TjdcnUmS&X-Amz-Signature=617e16f8309271f9872e87bd4c514de51fdf224a843172c84514cf935d12627a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WSVHWE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpZXJtG57oGLrMoLDPL3zfFZMlcIXJ9HBtTZn7WzVUEgIgdq9CGyqknYtU2F5HVsv%2FxEA%2BouKv6BORMeA1JJR3lmwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPt1wLuzBWHq2iyGCrcAzWpvXRu%2BUgxCYZ65%2BMOf6PK2pxlOb%2BznO7oo7dJpZaFEurArguVqmjr57%2BLj0DOWm0NULYPg0dxNkS%2FrOsE3NW3zcmufJw0%2B85v2mJAZ%2Bwh8L1JARUFJviqMbX1hjL659SdbrfZ9rXxBzUhU26veKfJVSdDKPBfKMhBiEMTt13B4B1mAnXZ22H%2FQ0qk5%2FbaKTOt0YH49zqS3h45tny99ewU06SmUyp89jF2qcmXr3aTh%2B6g%2FEiFBn%2FofR5fdeQnsFM5kcYbnZ75OZgd%2ByMLvR9G70qg5xitP5LNO7r1efDADuw%2BwZsr1BHhLw8is%2BlsZDw20EwPA2CbGKcB37hcNrILNXzQtZxYYLv40VIr1pEdpdYiNe2mColM%2BUB0dREYjw%2BcXU2ZNqOW2m8dMpoVCzWfvzc6Paykoc8NIHilOGt%2B4drov%2ByW%2BZ7iVPdNyU76qxRCuzNA7zTBzZzgBZht2VKLMYJRCtdZmxKs6Z7IHpvMVKWsJv8BfyOYLGOCxjXkENla1qdsnFeR0I809dMKTUIx%2FVGca579HKvxknrY7qcE7ZgCcx0j00Kr9y8q7g1rx25ckfBhkc4t4C7MXJ9IktSEgA%2FLTcH9ZhgGUKJBtaMBIBo6%2Bg%2Fswfm44%2FllMPeb%2FLwGOqUBB8cuyA0dAktx%2BmF%2F0m1S7MDMN5N6%2B47tMYjKF71a5EqwtQQCudioQoR4I4v640ViCShG8%2BTHsylGCZl1SxDuHkDkXcdBSozgfnj78AhNneJAcZzVPaDHWokhq5zR3mbXxGPEd%2F%2BBpP2s2fEsMUlJA6l%2B6yLUCDTDOMtv0bVFAWZWf2W6E63w%2B0CFSJGtgafvece2VmlRfKVEHlz41EA3TjdcnUmS&X-Amz-Signature=3d2ec89b1ccd9135095cb9f376f6160b3935b585fec78c2db21f4c9b864c5301&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WSVHWE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpZXJtG57oGLrMoLDPL3zfFZMlcIXJ9HBtTZn7WzVUEgIgdq9CGyqknYtU2F5HVsv%2FxEA%2BouKv6BORMeA1JJR3lmwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPt1wLuzBWHq2iyGCrcAzWpvXRu%2BUgxCYZ65%2BMOf6PK2pxlOb%2BznO7oo7dJpZaFEurArguVqmjr57%2BLj0DOWm0NULYPg0dxNkS%2FrOsE3NW3zcmufJw0%2B85v2mJAZ%2Bwh8L1JARUFJviqMbX1hjL659SdbrfZ9rXxBzUhU26veKfJVSdDKPBfKMhBiEMTt13B4B1mAnXZ22H%2FQ0qk5%2FbaKTOt0YH49zqS3h45tny99ewU06SmUyp89jF2qcmXr3aTh%2B6g%2FEiFBn%2FofR5fdeQnsFM5kcYbnZ75OZgd%2ByMLvR9G70qg5xitP5LNO7r1efDADuw%2BwZsr1BHhLw8is%2BlsZDw20EwPA2CbGKcB37hcNrILNXzQtZxYYLv40VIr1pEdpdYiNe2mColM%2BUB0dREYjw%2BcXU2ZNqOW2m8dMpoVCzWfvzc6Paykoc8NIHilOGt%2B4drov%2ByW%2BZ7iVPdNyU76qxRCuzNA7zTBzZzgBZht2VKLMYJRCtdZmxKs6Z7IHpvMVKWsJv8BfyOYLGOCxjXkENla1qdsnFeR0I809dMKTUIx%2FVGca579HKvxknrY7qcE7ZgCcx0j00Kr9y8q7g1rx25ckfBhkc4t4C7MXJ9IktSEgA%2FLTcH9ZhgGUKJBtaMBIBo6%2Bg%2Fswfm44%2FllMPeb%2FLwGOqUBB8cuyA0dAktx%2BmF%2F0m1S7MDMN5N6%2B47tMYjKF71a5EqwtQQCudioQoR4I4v640ViCShG8%2BTHsylGCZl1SxDuHkDkXcdBSozgfnj78AhNneJAcZzVPaDHWokhq5zR3mbXxGPEd%2F%2BBpP2s2fEsMUlJA6l%2B6yLUCDTDOMtv0bVFAWZWf2W6E63w%2B0CFSJGtgafvece2VmlRfKVEHlz41EA3TjdcnUmS&X-Amz-Signature=c4fb8a258eb5725cfe5f40b38f7c8349158c139b27f8179b4012d545aaa09d5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WSVHWE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpZXJtG57oGLrMoLDPL3zfFZMlcIXJ9HBtTZn7WzVUEgIgdq9CGyqknYtU2F5HVsv%2FxEA%2BouKv6BORMeA1JJR3lmwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPt1wLuzBWHq2iyGCrcAzWpvXRu%2BUgxCYZ65%2BMOf6PK2pxlOb%2BznO7oo7dJpZaFEurArguVqmjr57%2BLj0DOWm0NULYPg0dxNkS%2FrOsE3NW3zcmufJw0%2B85v2mJAZ%2Bwh8L1JARUFJviqMbX1hjL659SdbrfZ9rXxBzUhU26veKfJVSdDKPBfKMhBiEMTt13B4B1mAnXZ22H%2FQ0qk5%2FbaKTOt0YH49zqS3h45tny99ewU06SmUyp89jF2qcmXr3aTh%2B6g%2FEiFBn%2FofR5fdeQnsFM5kcYbnZ75OZgd%2ByMLvR9G70qg5xitP5LNO7r1efDADuw%2BwZsr1BHhLw8is%2BlsZDw20EwPA2CbGKcB37hcNrILNXzQtZxYYLv40VIr1pEdpdYiNe2mColM%2BUB0dREYjw%2BcXU2ZNqOW2m8dMpoVCzWfvzc6Paykoc8NIHilOGt%2B4drov%2ByW%2BZ7iVPdNyU76qxRCuzNA7zTBzZzgBZht2VKLMYJRCtdZmxKs6Z7IHpvMVKWsJv8BfyOYLGOCxjXkENla1qdsnFeR0I809dMKTUIx%2FVGca579HKvxknrY7qcE7ZgCcx0j00Kr9y8q7g1rx25ckfBhkc4t4C7MXJ9IktSEgA%2FLTcH9ZhgGUKJBtaMBIBo6%2Bg%2Fswfm44%2FllMPeb%2FLwGOqUBB8cuyA0dAktx%2BmF%2F0m1S7MDMN5N6%2B47tMYjKF71a5EqwtQQCudioQoR4I4v640ViCShG8%2BTHsylGCZl1SxDuHkDkXcdBSozgfnj78AhNneJAcZzVPaDHWokhq5zR3mbXxGPEd%2F%2BBpP2s2fEsMUlJA6l%2B6yLUCDTDOMtv0bVFAWZWf2W6E63w%2B0CFSJGtgafvece2VmlRfKVEHlz41EA3TjdcnUmS&X-Amz-Signature=81954a935d8a982a43eaf1e464260dbea462a31840e951758dc001f6f0763dd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WSVHWE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpZXJtG57oGLrMoLDPL3zfFZMlcIXJ9HBtTZn7WzVUEgIgdq9CGyqknYtU2F5HVsv%2FxEA%2BouKv6BORMeA1JJR3lmwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPt1wLuzBWHq2iyGCrcAzWpvXRu%2BUgxCYZ65%2BMOf6PK2pxlOb%2BznO7oo7dJpZaFEurArguVqmjr57%2BLj0DOWm0NULYPg0dxNkS%2FrOsE3NW3zcmufJw0%2B85v2mJAZ%2Bwh8L1JARUFJviqMbX1hjL659SdbrfZ9rXxBzUhU26veKfJVSdDKPBfKMhBiEMTt13B4B1mAnXZ22H%2FQ0qk5%2FbaKTOt0YH49zqS3h45tny99ewU06SmUyp89jF2qcmXr3aTh%2B6g%2FEiFBn%2FofR5fdeQnsFM5kcYbnZ75OZgd%2ByMLvR9G70qg5xitP5LNO7r1efDADuw%2BwZsr1BHhLw8is%2BlsZDw20EwPA2CbGKcB37hcNrILNXzQtZxYYLv40VIr1pEdpdYiNe2mColM%2BUB0dREYjw%2BcXU2ZNqOW2m8dMpoVCzWfvzc6Paykoc8NIHilOGt%2B4drov%2ByW%2BZ7iVPdNyU76qxRCuzNA7zTBzZzgBZht2VKLMYJRCtdZmxKs6Z7IHpvMVKWsJv8BfyOYLGOCxjXkENla1qdsnFeR0I809dMKTUIx%2FVGca579HKvxknrY7qcE7ZgCcx0j00Kr9y8q7g1rx25ckfBhkc4t4C7MXJ9IktSEgA%2FLTcH9ZhgGUKJBtaMBIBo6%2Bg%2Fswfm44%2FllMPeb%2FLwGOqUBB8cuyA0dAktx%2BmF%2F0m1S7MDMN5N6%2B47tMYjKF71a5EqwtQQCudioQoR4I4v640ViCShG8%2BTHsylGCZl1SxDuHkDkXcdBSozgfnj78AhNneJAcZzVPaDHWokhq5zR3mbXxGPEd%2F%2BBpP2s2fEsMUlJA6l%2B6yLUCDTDOMtv0bVFAWZWf2W6E63w%2B0CFSJGtgafvece2VmlRfKVEHlz41EA3TjdcnUmS&X-Amz-Signature=094d20878268e69de1440edee5754ce81c7322787822b9f4ec44d2daa6212af5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WSVHWE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpZXJtG57oGLrMoLDPL3zfFZMlcIXJ9HBtTZn7WzVUEgIgdq9CGyqknYtU2F5HVsv%2FxEA%2BouKv6BORMeA1JJR3lmwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPt1wLuzBWHq2iyGCrcAzWpvXRu%2BUgxCYZ65%2BMOf6PK2pxlOb%2BznO7oo7dJpZaFEurArguVqmjr57%2BLj0DOWm0NULYPg0dxNkS%2FrOsE3NW3zcmufJw0%2B85v2mJAZ%2Bwh8L1JARUFJviqMbX1hjL659SdbrfZ9rXxBzUhU26veKfJVSdDKPBfKMhBiEMTt13B4B1mAnXZ22H%2FQ0qk5%2FbaKTOt0YH49zqS3h45tny99ewU06SmUyp89jF2qcmXr3aTh%2B6g%2FEiFBn%2FofR5fdeQnsFM5kcYbnZ75OZgd%2ByMLvR9G70qg5xitP5LNO7r1efDADuw%2BwZsr1BHhLw8is%2BlsZDw20EwPA2CbGKcB37hcNrILNXzQtZxYYLv40VIr1pEdpdYiNe2mColM%2BUB0dREYjw%2BcXU2ZNqOW2m8dMpoVCzWfvzc6Paykoc8NIHilOGt%2B4drov%2ByW%2BZ7iVPdNyU76qxRCuzNA7zTBzZzgBZht2VKLMYJRCtdZmxKs6Z7IHpvMVKWsJv8BfyOYLGOCxjXkENla1qdsnFeR0I809dMKTUIx%2FVGca579HKvxknrY7qcE7ZgCcx0j00Kr9y8q7g1rx25ckfBhkc4t4C7MXJ9IktSEgA%2FLTcH9ZhgGUKJBtaMBIBo6%2Bg%2Fswfm44%2FllMPeb%2FLwGOqUBB8cuyA0dAktx%2BmF%2F0m1S7MDMN5N6%2B47tMYjKF71a5EqwtQQCudioQoR4I4v640ViCShG8%2BTHsylGCZl1SxDuHkDkXcdBSozgfnj78AhNneJAcZzVPaDHWokhq5zR3mbXxGPEd%2F%2BBpP2s2fEsMUlJA6l%2B6yLUCDTDOMtv0bVFAWZWf2W6E63w%2B0CFSJGtgafvece2VmlRfKVEHlz41EA3TjdcnUmS&X-Amz-Signature=4402509899e264c16ca3713670d25c78954cab977bfa0f82fdc71e5ed98494f8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3SCFV7P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEfsNQVivlmFNyOpok4ljBwlaHjE1wacT4NtbviZkAF5AiEA7rsYN0BJUjwgyrdog1%2BOrkpnjazczBjTN9A1PyxSVewqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKW4PQRIf57v%2FIZjeSrcA439p1r90pVm7qTCeMXj%2BkCJwQ0JvFiweDMZL%2F0KbzSIHqEP7IT9UQhBt6F7zowV%2FGW1nO7Wcv6%2FNAG6NpImqMtqWI2aZXQ87xnbQX%2B%2FKoQL6%2FnL%2FjG%2FK4GZ%2BGNq9%2B3YRdgwnaiOq20Q%2FuYBcy8H%2B3RLs9lrTf2%2F%2BHahx2c8b2xW0m7v%2FbfXor1YpN4LjxYq3Q1Ta%2B0R7NQKQ%2FhNa9RwZGo3KD6hUlpNKCX0sa6lQV03EG5ag86lSTSRwtsWRVVKeArDatAP2KJFVi5xzGQ0APhBjZKvzPZ0J6YHTzO5V8%2Bqu89O7P5yhc%2Ftyrp%2FlqaE1nfsHXYR4GwSeiuVRbtrNRcSMX5s0OibBTjF4U6CEF%2Baa5Q4NGx7RTxbeuS3AR%2BuJPCC9lGtLE1Hw%2BjclmKX3GWBnZVCW5ITFK3Hci16O7lh2oOvm85upeliLCam6vdiWZEe%2FTrwog3TkZD44UL5pYrt5PNr4ATEgU1E6dhzJQGOsQWhqM0rlDzJ4%2BK2WS94%2FXz1w8Yu2kbu981UOd50vHZ1VLmOAE%2FePnvi%2Bf4uRphOZGa%2FBOSt4MBNwqHTUaQ9i6svuejG1fEG4mbRCYofOCDNoO3ivMH7DQgHm9qorV4bXREGZQilhtoPvmTaMNub%2FLwGOqUBxHxJGrz5sg8erVKb7pytSOT27XCKUPrjDhQ6n8xxIB3Rx3YfZERjF1z6DozOG%2Fh4S0ZKNDUAtb1Cr5xeF7Z5K%2FqOOxtLChGc5oDCbgiWC1vUP9Kki%2BFFbwEbTdnP14m3Q6upE6VSb9pYukeHXxI5mVLP7ifzV7cuytttFY1mL44%2BF7aqpyYDZeBJdGIDOQ2JANwU0MMg3TLT9LV3dAQAmidTOlzM&X-Amz-Signature=0ac385e93a3ecb2b673fd3549e28dacf5091975347c41dc1236b4155ea22200e&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466644XYYCQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FxOpz%2F0WWCXKPga9EI0tkTfu%2Bs7vOhjb9ZDXQ1xY5vwIhAL%2B6xk53KgqruHK9MGTq1gB9VqJ3xNPhY%2B2DQv05swaTKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2FGycjpm35y5o2V%2BEq3AND6Sw0qt9AwjvhoTPfNEppKpBROex4tfJXfSG8ySTfQ1gfiQSEgkOODsqpyUp%2BscgNpAE1YFvFjhQ29u0JHjNrN2rbCyLd7w6X%2FplpFitypoVzP0kc7BS%2FPQCl03wQwJG9PVowF%2FYCNd1S0WRoB1Flz7rOXgAUJ4%2FFcf3PBFJR0chWqCMwXd%2FkvxrWPdkkGd5qmUDfUaejjObrvSYxVDl8LbiQ7Qws104lXEyLexR2paAy9hLzOnnBM%2FoBsDNjkNzg2hc5eaSornIb%2FrEEmhwzMR09vZkV74KpohWKeYNZ4OniaJ6xQhgsVYlBKZjddRr%2F4wiHZtKFlZbQ4JqZ3YcTkfkS4JdjCjq3g7yO1dB4f%2FquT9EL95k9Zw%2BL2qtpq5Sk3Tgw80yeonieC29i36A7XZuCefi1h5nWAwMCa0%2B0k0PTABBYpwyUcMK6nQ8txTxwWCL3zXNQnQVEAXgvmSiIQoEdyzy56MlOyhxvlNDuXLzv%2BEgxyvKgxsx5VZy76ZjfTp2bGgz9%2Bad4bnxgP1DDEvsyLUa647gJVzfHH%2BEKLEbWMQDBe9PXsGgnnO37Db8IAj8fUDVh5%2F%2BMCWqsPb25MJJdzE7Q%2FpK9Sq2r0ILvc2VU2X35Z7zf8rmlqzCWnPy8BjqkAQ2UXdekoERDl74YdXZCMtpbrEL%2FztkzM7AZ3gZTKKspicet1qth5wtnt39wywy1VoMkz9nFkX%2BsgSeR8k3HnbiT4eFVQWElo9DYK5c8NoJQoCMgP%2BuW2W8C93XvEtKnHycSIa0d%2BVAhFjcApeHd3tN4Vj52W3W%2BabuDQs2PcKsQhL%2FvxZTLb4p3S8I62aCuFdwaz7adPHTcmKVlMJOA8meVNmc3&X-Amz-Signature=114f216baf88304344797d1d54b9890ef1e0233ffcc060c50fd2e3feb970afd7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WSVHWE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpZXJtG57oGLrMoLDPL3zfFZMlcIXJ9HBtTZn7WzVUEgIgdq9CGyqknYtU2F5HVsv%2FxEA%2BouKv6BORMeA1JJR3lmwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPt1wLuzBWHq2iyGCrcAzWpvXRu%2BUgxCYZ65%2BMOf6PK2pxlOb%2BznO7oo7dJpZaFEurArguVqmjr57%2BLj0DOWm0NULYPg0dxNkS%2FrOsE3NW3zcmufJw0%2B85v2mJAZ%2Bwh8L1JARUFJviqMbX1hjL659SdbrfZ9rXxBzUhU26veKfJVSdDKPBfKMhBiEMTt13B4B1mAnXZ22H%2FQ0qk5%2FbaKTOt0YH49zqS3h45tny99ewU06SmUyp89jF2qcmXr3aTh%2B6g%2FEiFBn%2FofR5fdeQnsFM5kcYbnZ75OZgd%2ByMLvR9G70qg5xitP5LNO7r1efDADuw%2BwZsr1BHhLw8is%2BlsZDw20EwPA2CbGKcB37hcNrILNXzQtZxYYLv40VIr1pEdpdYiNe2mColM%2BUB0dREYjw%2BcXU2ZNqOW2m8dMpoVCzWfvzc6Paykoc8NIHilOGt%2B4drov%2ByW%2BZ7iVPdNyU76qxRCuzNA7zTBzZzgBZht2VKLMYJRCtdZmxKs6Z7IHpvMVKWsJv8BfyOYLGOCxjXkENla1qdsnFeR0I809dMKTUIx%2FVGca579HKvxknrY7qcE7ZgCcx0j00Kr9y8q7g1rx25ckfBhkc4t4C7MXJ9IktSEgA%2FLTcH9ZhgGUKJBtaMBIBo6%2Bg%2Fswfm44%2FllMPeb%2FLwGOqUBB8cuyA0dAktx%2BmF%2F0m1S7MDMN5N6%2B47tMYjKF71a5EqwtQQCudioQoR4I4v640ViCShG8%2BTHsylGCZl1SxDuHkDkXcdBSozgfnj78AhNneJAcZzVPaDHWokhq5zR3mbXxGPEd%2F%2BBpP2s2fEsMUlJA6l%2B6yLUCDTDOMtv0bVFAWZWf2W6E63w%2B0CFSJGtgafvece2VmlRfKVEHlz41EA3TjdcnUmS&X-Amz-Signature=089fa84d79aa9bb441e471933c2fb8620e9e87192fe48108ca8115355c52d7fb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WSVHWE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpZXJtG57oGLrMoLDPL3zfFZMlcIXJ9HBtTZn7WzVUEgIgdq9CGyqknYtU2F5HVsv%2FxEA%2BouKv6BORMeA1JJR3lmwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPt1wLuzBWHq2iyGCrcAzWpvXRu%2BUgxCYZ65%2BMOf6PK2pxlOb%2BznO7oo7dJpZaFEurArguVqmjr57%2BLj0DOWm0NULYPg0dxNkS%2FrOsE3NW3zcmufJw0%2B85v2mJAZ%2Bwh8L1JARUFJviqMbX1hjL659SdbrfZ9rXxBzUhU26veKfJVSdDKPBfKMhBiEMTt13B4B1mAnXZ22H%2FQ0qk5%2FbaKTOt0YH49zqS3h45tny99ewU06SmUyp89jF2qcmXr3aTh%2B6g%2FEiFBn%2FofR5fdeQnsFM5kcYbnZ75OZgd%2ByMLvR9G70qg5xitP5LNO7r1efDADuw%2BwZsr1BHhLw8is%2BlsZDw20EwPA2CbGKcB37hcNrILNXzQtZxYYLv40VIr1pEdpdYiNe2mColM%2BUB0dREYjw%2BcXU2ZNqOW2m8dMpoVCzWfvzc6Paykoc8NIHilOGt%2B4drov%2ByW%2BZ7iVPdNyU76qxRCuzNA7zTBzZzgBZht2VKLMYJRCtdZmxKs6Z7IHpvMVKWsJv8BfyOYLGOCxjXkENla1qdsnFeR0I809dMKTUIx%2FVGca579HKvxknrY7qcE7ZgCcx0j00Kr9y8q7g1rx25ckfBhkc4t4C7MXJ9IktSEgA%2FLTcH9ZhgGUKJBtaMBIBo6%2Bg%2Fswfm44%2FllMPeb%2FLwGOqUBB8cuyA0dAktx%2BmF%2F0m1S7MDMN5N6%2B47tMYjKF71a5EqwtQQCudioQoR4I4v640ViCShG8%2BTHsylGCZl1SxDuHkDkXcdBSozgfnj78AhNneJAcZzVPaDHWokhq5zR3mbXxGPEd%2F%2BBpP2s2fEsMUlJA6l%2B6yLUCDTDOMtv0bVFAWZWf2W6E63w%2B0CFSJGtgafvece2VmlRfKVEHlz41EA3TjdcnUmS&X-Amz-Signature=4956f1100e684a850fc4e288d35dfeffb97953e555be60e6561bc465e5b9069e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WSVHWE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpZXJtG57oGLrMoLDPL3zfFZMlcIXJ9HBtTZn7WzVUEgIgdq9CGyqknYtU2F5HVsv%2FxEA%2BouKv6BORMeA1JJR3lmwqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPt1wLuzBWHq2iyGCrcAzWpvXRu%2BUgxCYZ65%2BMOf6PK2pxlOb%2BznO7oo7dJpZaFEurArguVqmjr57%2BLj0DOWm0NULYPg0dxNkS%2FrOsE3NW3zcmufJw0%2B85v2mJAZ%2Bwh8L1JARUFJviqMbX1hjL659SdbrfZ9rXxBzUhU26veKfJVSdDKPBfKMhBiEMTt13B4B1mAnXZ22H%2FQ0qk5%2FbaKTOt0YH49zqS3h45tny99ewU06SmUyp89jF2qcmXr3aTh%2B6g%2FEiFBn%2FofR5fdeQnsFM5kcYbnZ75OZgd%2ByMLvR9G70qg5xitP5LNO7r1efDADuw%2BwZsr1BHhLw8is%2BlsZDw20EwPA2CbGKcB37hcNrILNXzQtZxYYLv40VIr1pEdpdYiNe2mColM%2BUB0dREYjw%2BcXU2ZNqOW2m8dMpoVCzWfvzc6Paykoc8NIHilOGt%2B4drov%2ByW%2BZ7iVPdNyU76qxRCuzNA7zTBzZzgBZht2VKLMYJRCtdZmxKs6Z7IHpvMVKWsJv8BfyOYLGOCxjXkENla1qdsnFeR0I809dMKTUIx%2FVGca579HKvxknrY7qcE7ZgCcx0j00Kr9y8q7g1rx25ckfBhkc4t4C7MXJ9IktSEgA%2FLTcH9ZhgGUKJBtaMBIBo6%2Bg%2Fswfm44%2FllMPeb%2FLwGOqUBB8cuyA0dAktx%2BmF%2F0m1S7MDMN5N6%2B47tMYjKF71a5EqwtQQCudioQoR4I4v640ViCShG8%2BTHsylGCZl1SxDuHkDkXcdBSozgfnj78AhNneJAcZzVPaDHWokhq5zR3mbXxGPEd%2F%2BBpP2s2fEsMUlJA6l%2B6yLUCDTDOMtv0bVFAWZWf2W6E63w%2B0CFSJGtgafvece2VmlRfKVEHlz41EA3TjdcnUmS&X-Amz-Signature=7828a996522d8516517004b6927b1a86e2edabb751981cb36273d3704800d119&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S42VMGJJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDq9PVNkn0uNFnKj5NErD5KIZ4SohQKkApDaNs82VJBewIhAO72%2BKVRqG0exV6tnZcuhFCoRMLSBCO8AOXqhgV6UwecKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igywmh6JGr1nhEIB6C4q3APbakQabsXjJ0i1sCO39ZPwjzRd4Kxle4WycgQyUW6Xam45BHZZbK8lpNWBu2tKScMr4rYjNXkldTMTwz%2FGLtnd6exAYCt7Qp5TxNts%2BP7FA0wQV3Z61U2Ry%2F7XcGEqU6B4GM03tleJsud8eVA%2FyIVlrKKf%2B4r%2FzjvoGztbafZ0%2Fk3DoWumSVhc9lD8E7jqMfU08zdRuzlBOU62N0hhApAUL5ZGOHKuXInQKLOj91N5C8o%2FsA4x%2FDlnYFOtLX8yf6tHzqVIbnDJSCJJrW42cZsryuOiWENkue6MUeWSQzTXWk%2Bi11Snnir2bRejIh3XHu94K6hL5Slp45YBkljykF5bRA%2Fp7CqG62LyrWeH3xC1bhkd2OKMv6zqGjQuqzGtsV1G2T2KiClJZoTQrjL0Q3woPNJN1ZTinsStjM9uLIt0pyq%2FCctLINC5R5ixZK5cKWPRpqnFBzzWO74Tbw%2BzSyeGYrsJ%2BDWcQ0q59yLVr44Yn42%2BNGJpEL5yMTh1aHSDDK0QRuJoFUuWo%2BymAedpokbLutqKwOfCNUajJA4l4E2IVI%2B4gORCiCTvPePDnAXcjerMEd96LupDLMGEblRBQfVp%2BZNqlp1N4nAPYv8zPnJwfK8jHC%2B9M6HOYGuUxzDam%2Fy8BjqkAQKKcnro%2B%2B7HnFk9R22gBJiB3eKoJjPXnG34V1TlYa4uG5vDn5QIEYdiE8QJoMCsMVIypoyagDAhXh1lgehHKNfP6rugESrZFrzf8DTKDySlE04DyMyhwvvD56ESQxennjr5wjiDsN3H15dRmgVidnpK4xc%2BISXOzGyX5BxSWOcsKZBfvAPHa9H7GcqtCSw5fKm7cQCdUmFujGCVIze3lQwU7i4u&X-Amz-Signature=6d77cf63db25fe3cbe8ca011a5c0cea08f9d267478f570ad3f43ea74b6adb2fe&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666IBXCDN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCG9dO7IPzRx51%2FT1sKF7m6CQPUVAwC1eJe7YVzuFu0tgIgNcvTUZUNpiuwtZEG9HX3xCc9Q3H%2FRmrPHPLN4ci2058qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKB0AapL5b5yj8osuyrcAyPgEswNxGpmIIuhkygv6M7T76NMBT56Kpz0yMD4no5hIhkMLRh1nynrOOuZQVi9aARMeIjhq0%2FIY2UBy16XgDECWOEhdtFQTSdtvEThu7SfSDe9KMYbFeSjoc%2Bh8uj7CpH9h1WJFMxE4hNRc%2BNIoMcaxP06EC7dJdwWkbEtowXITqUvTz3Dg7%2BfAq3aM9ppjAemj8Ja2AbxLiT9rQHsFPTUtXLHJHpgKT84tSEX6g9wRDKMIvReE8olIno43UMOJWppQSyb9I9qC81d%2F1O8tFj5L9E7iIYRkterhdy0yAXdCHhVcdbWbXcpNF0kPkExASWb3UjwBz%2FIyE6qAJKMESOFiIhyYH816zhT27j4sP0EfEJqjrvGgWANKMS0zddn34el4ZrQ7lXXXVH%2Fwi3slsZiRhtLoW6NnLQYwIbXwCMtm9Rjg5dp%2FsmGaET1euo%2FbsnhcvFrL6n78RXid9vkldtzug0ROCMwdpQcvSA4g7JIDAXQoTa%2F2Jc9fWW4mSTj5f2ftVt0K%2BVxUYe3Wpm86tcQt5klLI16Ug4AOgX89Qmf7d9MXaJa5aVyl3GGnN%2F1p3MwARhI8it47fuJX2VLPRW4KbEA3nI0poOUwQnid%2BBL%2Fz%2B%2BVPvEzry%2FkcmJMOyb%2FLwGOqUByCfH4IwS7l9RrOoljbBJOiA6VEvP51zeVPQzvEq2uTSgs5Gft6AZ7yAAomzyoye0qWaSQz4y47LreFuQa%2Bcpkt6RUZiCyEqIomjBWceQ4N1gKohsmTDvOjiXWmMog%2FLOD6HyQPgLfBqkAF9qNC6f6tlTeLO8CKM0gVYFhDmdkMh7763Ix9bKuXLtJuu6JRvxGFP52I8rbeMZLR%2Ff4vF83EzMZ2Mp&X-Amz-Signature=ea35ebd2d24f701588fd41c2f381f54008b6748539e35ed5fcab78502921706a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB7H4IQL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDTYVOgg%2BdWncc09N5s0Vr8EwNTNqk5TfP%2F1f%2BxaCpc7AiAtUE5kZsClUbMSOhEHLm727gd9IvtazkNTO1N3JCTUIyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBpk2B%2BmnaJaldPXWKtwDC8E4PcUydkacKCQkWmwQnDQimOu2eSTjF5%2Fzts0M5BnHeGegRxwi%2Fmm4y5DWKZdE%2F51eBHWTX7BnWSjgzRwhmxDQP8Icd2C9n%2BLj%2F9MpdmvO1HOQL9Mh3DKWQadFYbSYcawB6T9ZZzZT1DmeQEnQ2baide8VOIPYhTOfWwud%2FpvMrtnhle2aurhc0UA7mn26xT43mb7O26tl8qpAlcewii9j3XsEwtp4sh%2FWV8GSRZC2W%2Bj49s%2BuLKDnOSyikBAYMc4U5HTi2SWkP%2FipZH3G3Aoq%2BpA%2FMhByb4kq%2BVb%2FZOturuD1TG7txKlZrru75LhsJ8AJBiFnqgMWtOmgKi3Uc6FOrzzlV%2FsVVCS7aA0WmzHQ%2FDk70%2BRR%2F8wFJ0RhvOoa9VUnxmud3BOrutv0NUoP0TG%2F3CVCNR%2FrVunvVrH4LUvtquhqNhgqNJKHy9CQBmYrC%2FJc3BxCCU33iaRsS0rKWoN5EUvucrMgZPw3qQb6kK%2BiJK0jTXs2egjIs4SlPiNQvaYGCqUSSPoctJ3VS%2FasW8jS%2FWPVEItxQAyDZ4ssvpBycYxdcQWLudCdfWdi44X6qRQxu%2BHlMwe0kRT%2FLDO4%2BWm%2F9dfFccuWEfkgVIdAUKphisQw46xOeQz3EPMw65v8vAY6pgFSnWkomTmKg2xHDvd3tBk39e2LbkrIdoYh1XEGs%2BBp03miFH4dnWix7%2BTeLho7jPE2Yuh1LDhZuCnSiQznX22Nmn9NqvosF3DVgAKZmRtYXDY4pKgmt2dXSCnkztTyamq9HgWn6L%2BRDxCOVPqdxHKVPrIjBX8Y4se22NBmVBpIA1dKeFpZ%2BbV6%2FJWj7s7zVu1JBzfqg1Nez03%2Fo5dIj3K6NivjctaU&X-Amz-Signature=ba251b92b970052b4509f1249360e9e1f3720e7d20ba93ecd6b8e276f5d043cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UDYNCZE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAHh%2BMteDMvbi%2FzGYeUUlNzvTKd5qte6TfjseD8fa5OUAiEA1MyDOfLts3YqP%2FZjsCTax%2FqGBuu9l2yokypWWxXnWMQqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGxMpC5QJzCyzoSZircA71fe9axHzipKNbtnEqgb5MdpZXqMmvNfKonan%2BbnclnLRip3EX9qTBl7792SZgqt0dAlwQ%2FfskCpv%2BkrWFeqDNSIJX35AxI%2FrVmW6kXVMmHKOOhz25GJfhZOxy3Xr%2FhLU0Uh1t2pA78yuttFo3VATkAtV%2Fy3je9XPBYKTFz8yopaOnq2N1eZJCLabRZSFYQhKM2sHeYZzyl9T2Q19e4UKc99vk%2FtrdZhJk%2BswiE%2F6fyBU5jziSEMQIHLp%2Fv%2F%2BwwnIYq0%2B1QHuWtr5KrE3WDH4yUWOOXRGS%2Fyl00jA8IX2DY%2BZVdTjVgDavPmBTpWH8asdRJ4czyUDTehnj23UMj2D4wZoSRNij8L%2BLBGfl6v%2F5%2B%2Bn1Fmt3Zcoe5KMBDCHcmadatcEh5KJfuZdEba%2BQNZTxsfXNtZDGQMNGBPLE55ZZL8egKxyR3zB2Blev7wx8KVI0ONKthyxIoFr%2Bkcw%2FjPbECqCXgMf%2BJ5BXXU1IJMzEbViIj8Nmwdk%2FWvKnqq3AbepP1vcKJxIM1fZSdBWI1kLzmnLJ4rmMPp%2BSqxUtx2FehBXYQFADMsUdwGEMwNeswcQcZo17q7dw%2B3KVT%2FOWKYxL%2B8X5nv1HnlgYXBQwl3apZDx08IeOn%2Bg5E5YRdMIDh%2B7wGOqUBTLFUZq0iFZKqtMgP6HDDS3PHO7T5f1BgzOhr%2B%2FaH%2Frdef5mQ4i3yNRnuSTFA5unuS8aCwA%2Bd8h%2FO7g0Ox0CjXrS0xQkOBPTViWTg1VN%2B%2FUUff107zJuk7PZMG4KKYaNMyWM5gmXHvVEuureI2xRT4hwE3%2BCALRiCER84StcnPwKAzzFR0Hbah6du%2FPZiNtgvj2JK1wmr4RQqUd6xRGrrASrpP%2Bce&X-Amz-Signature=023b132510a115a4bfe7b4cae5343d91394366e1b086235f576cdd6c71b6d365&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UDYNCZE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAHh%2BMteDMvbi%2FzGYeUUlNzvTKd5qte6TfjseD8fa5OUAiEA1MyDOfLts3YqP%2FZjsCTax%2FqGBuu9l2yokypWWxXnWMQqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGxMpC5QJzCyzoSZircA71fe9axHzipKNbtnEqgb5MdpZXqMmvNfKonan%2BbnclnLRip3EX9qTBl7792SZgqt0dAlwQ%2FfskCpv%2BkrWFeqDNSIJX35AxI%2FrVmW6kXVMmHKOOhz25GJfhZOxy3Xr%2FhLU0Uh1t2pA78yuttFo3VATkAtV%2Fy3je9XPBYKTFz8yopaOnq2N1eZJCLabRZSFYQhKM2sHeYZzyl9T2Q19e4UKc99vk%2FtrdZhJk%2BswiE%2F6fyBU5jziSEMQIHLp%2Fv%2F%2BwwnIYq0%2B1QHuWtr5KrE3WDH4yUWOOXRGS%2Fyl00jA8IX2DY%2BZVdTjVgDavPmBTpWH8asdRJ4czyUDTehnj23UMj2D4wZoSRNij8L%2BLBGfl6v%2F5%2B%2Bn1Fmt3Zcoe5KMBDCHcmadatcEh5KJfuZdEba%2BQNZTxsfXNtZDGQMNGBPLE55ZZL8egKxyR3zB2Blev7wx8KVI0ONKthyxIoFr%2Bkcw%2FjPbECqCXgMf%2BJ5BXXU1IJMzEbViIj8Nmwdk%2FWvKnqq3AbepP1vcKJxIM1fZSdBWI1kLzmnLJ4rmMPp%2BSqxUtx2FehBXYQFADMsUdwGEMwNeswcQcZo17q7dw%2B3KVT%2FOWKYxL%2B8X5nv1HnlgYXBQwl3apZDx08IeOn%2Bg5E5YRdMIDh%2B7wGOqUBTLFUZq0iFZKqtMgP6HDDS3PHO7T5f1BgzOhr%2B%2FaH%2Frdef5mQ4i3yNRnuSTFA5unuS8aCwA%2Bd8h%2FO7g0Ox0CjXrS0xQkOBPTViWTg1VN%2B%2FUUff107zJuk7PZMG4KKYaNMyWM5gmXHvVEuureI2xRT4hwE3%2BCALRiCER84StcnPwKAzzFR0Hbah6du%2FPZiNtgvj2JK1wmr4RQqUd6xRGrrASrpP%2Bce&X-Amz-Signature=9c5ce78d07a33018a73943b24d138e9abb504f5c50ddaded44714a74d1da11de&X-Amz-SignedHeaders=host&x-id=GetObject)

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
