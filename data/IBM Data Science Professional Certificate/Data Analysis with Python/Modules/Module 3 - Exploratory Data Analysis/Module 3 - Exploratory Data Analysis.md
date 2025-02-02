

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVTXLWZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQX0cnj76ITfEyeMdOXx1SYdLPx63EJbJuByFkFrtS2gIgcwBYTK%2B5EfsbqVH8%2Fe%2F5De%2BzeljOxVbsyJ6lRoaXLvcqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXD90vT3ZUYmikq4SrcA6EtD4Cv8J%2Bg%2B3Y5BXh11RFNEE4rJg%2BITGePm7p6Zy7HhWwAnrD8l3BvPWdOVLgtjC%2FmF2lSMQYDQtaMh2OwXQK9LMnaF7Y8VPEP2ZSSGGkpW3jK%2BICOMxeHNWH2JptVlgzsWcXpkyhh9FMC7uf3Sm%2BLy5%2Ff9VtQq8NO74YOCsC9jwRSDHUx9fjiiL73r8j4Aff6re%2FOj2Qd4V4OFAl2g%2F3Tcyt1y8FBD%2FOLdOKlQkM5eBv3MZpqqgR3Ad1Us45cIHCIhUaboEv2QOdnndDTW4ilYQ0zUjl72OdQv8wmrFmj88TgfdjuyyWfriTsqLhM6fxubBlL%2FHZqtt6L2ow5dIaFKL7E2R1OsvF%2BTkjjN50mQbfb51oiNmieJ88vSBifz4UVfTnHyXKv35EQb14VKC4dVLaCi0YaLQDzR6SkENaOyh2%2B2ED9eb3mWaYVyuVOAmfJyXfHwj8p%2FaDXlCztYbq1kQhGgorsaoCd0%2BcQfhXGNgfJ5SIOPf76N61XJSicxYLupXAVJWYNPGs0rSvnAqTpOu9MKVyLg5mwTFVewtiK97MiWfgpLPAYep3F%2Be2tLub6hppCZ1OfZZ4AP%2F5bZjIikYJ3Y8gmIH6UuwYHSJVNlIcnZOZ4IElifZQLMKLa%2FrwGOqUBeAIxb7vf32172YVNPD%2FOHemv7T3ghGmtMv24X0XbAwnCIoRu8j1t0t7KhbAhlTU1PNli%2FntLvZ%2FCERPTodE0spo2l37kPgICoO3U19ZwoZI99DJhhHYHMYA6N1HDl0S5ZXaHpJnsAQlmbqxJl%2Bo7SCfzXeeMUJIekgMWUeIuNaYoIgJ0Acn%2BzqCOgQ8Bw8qKxNkLGlmRAqiG2eBnfHASs7kew9IH&X-Amz-Signature=6e8241cc4e48235778d94dbcd0a8595b5eb8bf3ed2d4bb1c5cf8049c79c6106f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVTXLWZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQX0cnj76ITfEyeMdOXx1SYdLPx63EJbJuByFkFrtS2gIgcwBYTK%2B5EfsbqVH8%2Fe%2F5De%2BzeljOxVbsyJ6lRoaXLvcqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXD90vT3ZUYmikq4SrcA6EtD4Cv8J%2Bg%2B3Y5BXh11RFNEE4rJg%2BITGePm7p6Zy7HhWwAnrD8l3BvPWdOVLgtjC%2FmF2lSMQYDQtaMh2OwXQK9LMnaF7Y8VPEP2ZSSGGkpW3jK%2BICOMxeHNWH2JptVlgzsWcXpkyhh9FMC7uf3Sm%2BLy5%2Ff9VtQq8NO74YOCsC9jwRSDHUx9fjiiL73r8j4Aff6re%2FOj2Qd4V4OFAl2g%2F3Tcyt1y8FBD%2FOLdOKlQkM5eBv3MZpqqgR3Ad1Us45cIHCIhUaboEv2QOdnndDTW4ilYQ0zUjl72OdQv8wmrFmj88TgfdjuyyWfriTsqLhM6fxubBlL%2FHZqtt6L2ow5dIaFKL7E2R1OsvF%2BTkjjN50mQbfb51oiNmieJ88vSBifz4UVfTnHyXKv35EQb14VKC4dVLaCi0YaLQDzR6SkENaOyh2%2B2ED9eb3mWaYVyuVOAmfJyXfHwj8p%2FaDXlCztYbq1kQhGgorsaoCd0%2BcQfhXGNgfJ5SIOPf76N61XJSicxYLupXAVJWYNPGs0rSvnAqTpOu9MKVyLg5mwTFVewtiK97MiWfgpLPAYep3F%2Be2tLub6hppCZ1OfZZ4AP%2F5bZjIikYJ3Y8gmIH6UuwYHSJVNlIcnZOZ4IElifZQLMKLa%2FrwGOqUBeAIxb7vf32172YVNPD%2FOHemv7T3ghGmtMv24X0XbAwnCIoRu8j1t0t7KhbAhlTU1PNli%2FntLvZ%2FCERPTodE0spo2l37kPgICoO3U19ZwoZI99DJhhHYHMYA6N1HDl0S5ZXaHpJnsAQlmbqxJl%2Bo7SCfzXeeMUJIekgMWUeIuNaYoIgJ0Acn%2BzqCOgQ8Bw8qKxNkLGlmRAqiG2eBnfHASs7kew9IH&X-Amz-Signature=8770d7cc89cfd70a91a02e9e04da89bfcf709d89bdb004939e6259b886095a23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVTXLWZQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQX0cnj76ITfEyeMdOXx1SYdLPx63EJbJuByFkFrtS2gIgcwBYTK%2B5EfsbqVH8%2Fe%2F5De%2BzeljOxVbsyJ6lRoaXLvcqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXD90vT3ZUYmikq4SrcA6EtD4Cv8J%2Bg%2B3Y5BXh11RFNEE4rJg%2BITGePm7p6Zy7HhWwAnrD8l3BvPWdOVLgtjC%2FmF2lSMQYDQtaMh2OwXQK9LMnaF7Y8VPEP2ZSSGGkpW3jK%2BICOMxeHNWH2JptVlgzsWcXpkyhh9FMC7uf3Sm%2BLy5%2Ff9VtQq8NO74YOCsC9jwRSDHUx9fjiiL73r8j4Aff6re%2FOj2Qd4V4OFAl2g%2F3Tcyt1y8FBD%2FOLdOKlQkM5eBv3MZpqqgR3Ad1Us45cIHCIhUaboEv2QOdnndDTW4ilYQ0zUjl72OdQv8wmrFmj88TgfdjuyyWfriTsqLhM6fxubBlL%2FHZqtt6L2ow5dIaFKL7E2R1OsvF%2BTkjjN50mQbfb51oiNmieJ88vSBifz4UVfTnHyXKv35EQb14VKC4dVLaCi0YaLQDzR6SkENaOyh2%2B2ED9eb3mWaYVyuVOAmfJyXfHwj8p%2FaDXlCztYbq1kQhGgorsaoCd0%2BcQfhXGNgfJ5SIOPf76N61XJSicxYLupXAVJWYNPGs0rSvnAqTpOu9MKVyLg5mwTFVewtiK97MiWfgpLPAYep3F%2Be2tLub6hppCZ1OfZZ4AP%2F5bZjIikYJ3Y8gmIH6UuwYHSJVNlIcnZOZ4IElifZQLMKLa%2FrwGOqUBeAIxb7vf32172YVNPD%2FOHemv7T3ghGmtMv24X0XbAwnCIoRu8j1t0t7KhbAhlTU1PNli%2FntLvZ%2FCERPTodE0spo2l37kPgICoO3U19ZwoZI99DJhhHYHMYA6N1HDl0S5ZXaHpJnsAQlmbqxJl%2Bo7SCfzXeeMUJIekgMWUeIuNaYoIgJ0Acn%2BzqCOgQ8Bw8qKxNkLGlmRAqiG2eBnfHASs7kew9IH&X-Amz-Signature=6ae337538852a60df106f80c4769efc745ee0af8febcf22119c568e434b44098&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBQXTI7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvyuVHJJwj9IJtbzLj8FQctvX7C5KRYI2fXHS2PHLnbAiEA1j5Sm7QYKUwKRQr21h78rX7QVmTmxC7ViaMDgHWOSA8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8o9i3TuxjxIrrTsircA7zjCrYE%2FgRRYE9Afhm3ZginIBEjllqvHkR%2Bwx%2FVXAaVk8d0OK08R2p3G7n4bh4CcCfgWW%2FetQwFoQVynY937mLap7FKi0DhRHk8ghsFD0ReotYfD0yZPKlnOQ%2FUIl1QHdKM5Aon1ICAa3jsu17jGtvMm%2BLNMCNk9p4kj8eCG5G28tQpiqHUMPFMfz%2BhrVs3F%2BQorFpnfYXdIC59G0QLaF%2BW8oy0KgvLjoRMVGMVNyXNcWum1vVV8LarW40l%2Fs5e3ixj5P9j34JvS62KGZ%2FjgQx2JaSgRWuSKZgeqCuCwqbTtuy5fNzRi78HwBnaZuvHPYoLfhDrtDb%2FnhUaZHjpzRzsg0wHdckZ1ua4AgKx68TkPNjfMBKJ0Ji9P58yHvU7oDN3Crz7aP730ron1ypfrvuWaUsONdNoHbay1YxaeYChe7b%2BF50eU81kM7nxVXgNFkx0B7VwbPk65D%2B7oo93KKxP4Uw8lTeXfPterxI3xRH%2FeIIj3e57HooDWOoqKHfDyIuQP6Iz249pi%2BAeTuL5cECNOsUtcR9YpBTfWVioJljjPmeWWF5cPS2qe6oouEdn41F6DELx4yQjdZzJucS071KE%2Fst3BkvFtfOFa4ISONbQBCxplcnDkvSUEtEcMMPY%2FrwGOqUBJsTulVBjDakQiV2GZvkIXYbcGN46vK7S1tSouX0P3LE51ktWgxTtvhjUNYZLmRIbbPpQfClD%2B0Xi%2BYF1f7AOn%2FlmHVKO2FEzLcoMZDeQ97yJ84613pu9Lnltueo08PdE%2FFOzBXQkSIlt%2FwhHwShWVGrCIwZjUUmHqkNH0RQHi6JQNby%2BKlLR0oaJjwOm57Dc1psmyR9BI01riVN42%2FpDnBKRc21Y&X-Amz-Signature=270bed85bc6559062af366cb34527487fa814fb5754fc33dbef82bdb95c33271&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBQXTI7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvyuVHJJwj9IJtbzLj8FQctvX7C5KRYI2fXHS2PHLnbAiEA1j5Sm7QYKUwKRQr21h78rX7QVmTmxC7ViaMDgHWOSA8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8o9i3TuxjxIrrTsircA7zjCrYE%2FgRRYE9Afhm3ZginIBEjllqvHkR%2Bwx%2FVXAaVk8d0OK08R2p3G7n4bh4CcCfgWW%2FetQwFoQVynY937mLap7FKi0DhRHk8ghsFD0ReotYfD0yZPKlnOQ%2FUIl1QHdKM5Aon1ICAa3jsu17jGtvMm%2BLNMCNk9p4kj8eCG5G28tQpiqHUMPFMfz%2BhrVs3F%2BQorFpnfYXdIC59G0QLaF%2BW8oy0KgvLjoRMVGMVNyXNcWum1vVV8LarW40l%2Fs5e3ixj5P9j34JvS62KGZ%2FjgQx2JaSgRWuSKZgeqCuCwqbTtuy5fNzRi78HwBnaZuvHPYoLfhDrtDb%2FnhUaZHjpzRzsg0wHdckZ1ua4AgKx68TkPNjfMBKJ0Ji9P58yHvU7oDN3Crz7aP730ron1ypfrvuWaUsONdNoHbay1YxaeYChe7b%2BF50eU81kM7nxVXgNFkx0B7VwbPk65D%2B7oo93KKxP4Uw8lTeXfPterxI3xRH%2FeIIj3e57HooDWOoqKHfDyIuQP6Iz249pi%2BAeTuL5cECNOsUtcR9YpBTfWVioJljjPmeWWF5cPS2qe6oouEdn41F6DELx4yQjdZzJucS071KE%2Fst3BkvFtfOFa4ISONbQBCxplcnDkvSUEtEcMMPY%2FrwGOqUBJsTulVBjDakQiV2GZvkIXYbcGN46vK7S1tSouX0P3LE51ktWgxTtvhjUNYZLmRIbbPpQfClD%2B0Xi%2BYF1f7AOn%2FlmHVKO2FEzLcoMZDeQ97yJ84613pu9Lnltueo08PdE%2FFOzBXQkSIlt%2FwhHwShWVGrCIwZjUUmHqkNH0RQHi6JQNby%2BKlLR0oaJjwOm57Dc1psmyR9BI01riVN42%2FpDnBKRc21Y&X-Amz-Signature=07b584be7918cdb5e8fd336208a392ca050ecd73c625e2c9257184fb6e5a2029&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBQXTI7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvyuVHJJwj9IJtbzLj8FQctvX7C5KRYI2fXHS2PHLnbAiEA1j5Sm7QYKUwKRQr21h78rX7QVmTmxC7ViaMDgHWOSA8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8o9i3TuxjxIrrTsircA7zjCrYE%2FgRRYE9Afhm3ZginIBEjllqvHkR%2Bwx%2FVXAaVk8d0OK08R2p3G7n4bh4CcCfgWW%2FetQwFoQVynY937mLap7FKi0DhRHk8ghsFD0ReotYfD0yZPKlnOQ%2FUIl1QHdKM5Aon1ICAa3jsu17jGtvMm%2BLNMCNk9p4kj8eCG5G28tQpiqHUMPFMfz%2BhrVs3F%2BQorFpnfYXdIC59G0QLaF%2BW8oy0KgvLjoRMVGMVNyXNcWum1vVV8LarW40l%2Fs5e3ixj5P9j34JvS62KGZ%2FjgQx2JaSgRWuSKZgeqCuCwqbTtuy5fNzRi78HwBnaZuvHPYoLfhDrtDb%2FnhUaZHjpzRzsg0wHdckZ1ua4AgKx68TkPNjfMBKJ0Ji9P58yHvU7oDN3Crz7aP730ron1ypfrvuWaUsONdNoHbay1YxaeYChe7b%2BF50eU81kM7nxVXgNFkx0B7VwbPk65D%2B7oo93KKxP4Uw8lTeXfPterxI3xRH%2FeIIj3e57HooDWOoqKHfDyIuQP6Iz249pi%2BAeTuL5cECNOsUtcR9YpBTfWVioJljjPmeWWF5cPS2qe6oouEdn41F6DELx4yQjdZzJucS071KE%2Fst3BkvFtfOFa4ISONbQBCxplcnDkvSUEtEcMMPY%2FrwGOqUBJsTulVBjDakQiV2GZvkIXYbcGN46vK7S1tSouX0P3LE51ktWgxTtvhjUNYZLmRIbbPpQfClD%2B0Xi%2BYF1f7AOn%2FlmHVKO2FEzLcoMZDeQ97yJ84613pu9Lnltueo08PdE%2FFOzBXQkSIlt%2FwhHwShWVGrCIwZjUUmHqkNH0RQHi6JQNby%2BKlLR0oaJjwOm57Dc1psmyR9BI01riVN42%2FpDnBKRc21Y&X-Amz-Signature=ba53379b590594e9c2ada9432b9954c6e9bde03438416234149ab793346f42ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBQXTI7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvyuVHJJwj9IJtbzLj8FQctvX7C5KRYI2fXHS2PHLnbAiEA1j5Sm7QYKUwKRQr21h78rX7QVmTmxC7ViaMDgHWOSA8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8o9i3TuxjxIrrTsircA7zjCrYE%2FgRRYE9Afhm3ZginIBEjllqvHkR%2Bwx%2FVXAaVk8d0OK08R2p3G7n4bh4CcCfgWW%2FetQwFoQVynY937mLap7FKi0DhRHk8ghsFD0ReotYfD0yZPKlnOQ%2FUIl1QHdKM5Aon1ICAa3jsu17jGtvMm%2BLNMCNk9p4kj8eCG5G28tQpiqHUMPFMfz%2BhrVs3F%2BQorFpnfYXdIC59G0QLaF%2BW8oy0KgvLjoRMVGMVNyXNcWum1vVV8LarW40l%2Fs5e3ixj5P9j34JvS62KGZ%2FjgQx2JaSgRWuSKZgeqCuCwqbTtuy5fNzRi78HwBnaZuvHPYoLfhDrtDb%2FnhUaZHjpzRzsg0wHdckZ1ua4AgKx68TkPNjfMBKJ0Ji9P58yHvU7oDN3Crz7aP730ron1ypfrvuWaUsONdNoHbay1YxaeYChe7b%2BF50eU81kM7nxVXgNFkx0B7VwbPk65D%2B7oo93KKxP4Uw8lTeXfPterxI3xRH%2FeIIj3e57HooDWOoqKHfDyIuQP6Iz249pi%2BAeTuL5cECNOsUtcR9YpBTfWVioJljjPmeWWF5cPS2qe6oouEdn41F6DELx4yQjdZzJucS071KE%2Fst3BkvFtfOFa4ISONbQBCxplcnDkvSUEtEcMMPY%2FrwGOqUBJsTulVBjDakQiV2GZvkIXYbcGN46vK7S1tSouX0P3LE51ktWgxTtvhjUNYZLmRIbbPpQfClD%2B0Xi%2BYF1f7AOn%2FlmHVKO2FEzLcoMZDeQ97yJ84613pu9Lnltueo08PdE%2FFOzBXQkSIlt%2FwhHwShWVGrCIwZjUUmHqkNH0RQHi6JQNby%2BKlLR0oaJjwOm57Dc1psmyR9BI01riVN42%2FpDnBKRc21Y&X-Amz-Signature=f67daccd390b40cbba14498062e3489d3d2e72bfd8ab96172e170144ac2bca89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBQXTI7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvyuVHJJwj9IJtbzLj8FQctvX7C5KRYI2fXHS2PHLnbAiEA1j5Sm7QYKUwKRQr21h78rX7QVmTmxC7ViaMDgHWOSA8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8o9i3TuxjxIrrTsircA7zjCrYE%2FgRRYE9Afhm3ZginIBEjllqvHkR%2Bwx%2FVXAaVk8d0OK08R2p3G7n4bh4CcCfgWW%2FetQwFoQVynY937mLap7FKi0DhRHk8ghsFD0ReotYfD0yZPKlnOQ%2FUIl1QHdKM5Aon1ICAa3jsu17jGtvMm%2BLNMCNk9p4kj8eCG5G28tQpiqHUMPFMfz%2BhrVs3F%2BQorFpnfYXdIC59G0QLaF%2BW8oy0KgvLjoRMVGMVNyXNcWum1vVV8LarW40l%2Fs5e3ixj5P9j34JvS62KGZ%2FjgQx2JaSgRWuSKZgeqCuCwqbTtuy5fNzRi78HwBnaZuvHPYoLfhDrtDb%2FnhUaZHjpzRzsg0wHdckZ1ua4AgKx68TkPNjfMBKJ0Ji9P58yHvU7oDN3Crz7aP730ron1ypfrvuWaUsONdNoHbay1YxaeYChe7b%2BF50eU81kM7nxVXgNFkx0B7VwbPk65D%2B7oo93KKxP4Uw8lTeXfPterxI3xRH%2FeIIj3e57HooDWOoqKHfDyIuQP6Iz249pi%2BAeTuL5cECNOsUtcR9YpBTfWVioJljjPmeWWF5cPS2qe6oouEdn41F6DELx4yQjdZzJucS071KE%2Fst3BkvFtfOFa4ISONbQBCxplcnDkvSUEtEcMMPY%2FrwGOqUBJsTulVBjDakQiV2GZvkIXYbcGN46vK7S1tSouX0P3LE51ktWgxTtvhjUNYZLmRIbbPpQfClD%2B0Xi%2BYF1f7AOn%2FlmHVKO2FEzLcoMZDeQ97yJ84613pu9Lnltueo08PdE%2FFOzBXQkSIlt%2FwhHwShWVGrCIwZjUUmHqkNH0RQHi6JQNby%2BKlLR0oaJjwOm57Dc1psmyR9BI01riVN42%2FpDnBKRc21Y&X-Amz-Signature=7df14a33aae276e8b5fbad553ff151099b6f5c62c3cc5413286c6f98829f967e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBQXTI7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvyuVHJJwj9IJtbzLj8FQctvX7C5KRYI2fXHS2PHLnbAiEA1j5Sm7QYKUwKRQr21h78rX7QVmTmxC7ViaMDgHWOSA8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8o9i3TuxjxIrrTsircA7zjCrYE%2FgRRYE9Afhm3ZginIBEjllqvHkR%2Bwx%2FVXAaVk8d0OK08R2p3G7n4bh4CcCfgWW%2FetQwFoQVynY937mLap7FKi0DhRHk8ghsFD0ReotYfD0yZPKlnOQ%2FUIl1QHdKM5Aon1ICAa3jsu17jGtvMm%2BLNMCNk9p4kj8eCG5G28tQpiqHUMPFMfz%2BhrVs3F%2BQorFpnfYXdIC59G0QLaF%2BW8oy0KgvLjoRMVGMVNyXNcWum1vVV8LarW40l%2Fs5e3ixj5P9j34JvS62KGZ%2FjgQx2JaSgRWuSKZgeqCuCwqbTtuy5fNzRi78HwBnaZuvHPYoLfhDrtDb%2FnhUaZHjpzRzsg0wHdckZ1ua4AgKx68TkPNjfMBKJ0Ji9P58yHvU7oDN3Crz7aP730ron1ypfrvuWaUsONdNoHbay1YxaeYChe7b%2BF50eU81kM7nxVXgNFkx0B7VwbPk65D%2B7oo93KKxP4Uw8lTeXfPterxI3xRH%2FeIIj3e57HooDWOoqKHfDyIuQP6Iz249pi%2BAeTuL5cECNOsUtcR9YpBTfWVioJljjPmeWWF5cPS2qe6oouEdn41F6DELx4yQjdZzJucS071KE%2Fst3BkvFtfOFa4ISONbQBCxplcnDkvSUEtEcMMPY%2FrwGOqUBJsTulVBjDakQiV2GZvkIXYbcGN46vK7S1tSouX0P3LE51ktWgxTtvhjUNYZLmRIbbPpQfClD%2B0Xi%2BYF1f7AOn%2FlmHVKO2FEzLcoMZDeQ97yJ84613pu9Lnltueo08PdE%2FFOzBXQkSIlt%2FwhHwShWVGrCIwZjUUmHqkNH0RQHi6JQNby%2BKlLR0oaJjwOm57Dc1psmyR9BI01riVN42%2FpDnBKRc21Y&X-Amz-Signature=80a6303b466463eb007ef5736b238b0403cae804582d06e8357d8c510cb83d12&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWI6ZFEV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICf3gaIBptwpzO5DAIh6%2BGygYgt7fi1%2B6A%2BUzbw8mj%2BkAiEAvIloPfcoobLQ%2BTxVxFCwNgmFt7nzg0QmI%2BhmIYmVTPkqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB76j2BDnidwBg3tPyrcAwCyW41QfkUcIYLCct%2B11VoGFSCJkZexPaLTDkTexbyQocq2tyr%2BJ7qahQw0DWLGTiF7PCW%2Bs4AxeyuZecdYu%2Bna00cOo8ihLYMAV%2FnXOUWM1bSXNnBnK5s1gR2tXAsTehOPpI1sKi9AYrJh4%2FRiMZiCwcNrrfhK3lqJfTcLcKG491E4av7%2BO%2B1Tv7JKqd0OP%2BWFGslDl7A1vMz7W%2Bf%2BDz0pcab%2FDAt7uQ4p3%2BOJyGehZyRk8UZ83ftbduhM6vdVXcDFslvZHyt6N2NUJkAwwZ01iL2q7Lyhv4LkObLtdZEO1oAfH8w%2BwhwIBvy5MhADtKHxdvPBDxItix%2BqkkDGolh0ocARzH8cOyPaMa2Hb6vMODXcEfcTgrDeLSqOuD3sY%2Bk55R%2F%2Fw09AwAHwplB32M7MLJAJDcULtWhqpuvxyYaRjSVhoH1Eoy5S9Jbui3ClMqfFOYa7JCdCA4tfOlO0MLV1vhY7jhntX4a1LSHwHlqPS7X5fNgN4Hu%2Bwy0%2FTgFarSUxiS8onljmhspGRx1M0Veztrjpbi6RdIySPBc3snJd58pzKfg8z3c1rl23C8lkKH6K%2FHEyPaZzbc6ffQHHzRoxJd8D7h8TLBLuo0mIy5q%2FOEvCtGOUhYVwaidCMKXl%2FrwGOqUBk4Iuyug1VP6d3mmhQ8zbeJVZRtblsiJ7up8%2FrdN%2B72BSMEIFL0wne6v0vqMVDigEzUH286%2FvFsyfj8qFDosVi%2BVR8C4wic89UvxjoFG5BwZ2fe%2B1QTUR1jqFHimzKJ4NSIPV8IH9NH%2BUQLclcJRrSiPBOePuKGzj%2FhHzz788ICUaO73%2BdcdDbkrP3QO1Q9fFuNhNZj5sTeH3WBkhuClF8BlF6Vfd&X-Amz-Signature=4324049aeccd1f118b9dc53576af0fc2fcc38742bff1cb87480f50829a3de7cc&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIVZK3TC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECochPonGRGJL%2BjeuxLbueAXf4pZu%2F0jnU2ZOPEHVQBAiBrOCGX0QYkd9Owf7KpnEalCWFqkKl8EdtIqd%2Bba5tEzSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0WRUwxyLm1dAA7ftKtwDeA4vBziyMHCz4M15%2FZKAoCMiQfKnIZkvv9TSSnBgJ%2BDfaoLHptcPA9byk%2F0X3uqf8xXhvsjW5mzJAakiNqb71YU7QHjI7x49yAdVBH20%2BsgnmMv0LiqV3TzcJw2NX09tNHJBQfg72D55RKEbPAdTI2jukJP3r%2BCJEUgUA20S1H0MJf3dnDH7rBl9TVBM0%2FGIfIgkCb7MbTKYUEfybB7Q2bqHeIICSg9gLF5xc4H3VvuEAIh2RnKhNnnkdbgxxHp2gxKrLRgkeY3ru9FdS%2BEfP7zS56jbqJJ6ZDd0%2B2BracLAQl5xjoHUVT%2BOXkd1iz%2FGHJLjokJUAyGl4jFwGRj3k6LBP9oQk247c6JQ27%2FcglteXvjExwtDsMK6I6FX%2B6M8OqHidbeC2bjt2uzuiq%2BQXgCW03p1JUhB6qJLn0exgyclTozFOSjT126VhBLE5wsm9Fd4A4HwGpj9G8Gpxtf%2FqD%2Fb19PVYXXb%2BHTtUaOPJAp18VoDZ3r0%2FHYiCBdzd0kCK4YVE2aKAQM7bLK6Zlzqvo4%2B84%2Fm3pqO8Y1zhs1Fv6d5MHtWRzmTKbz1qj7fA5cdiOHCRLA0AkU6gxGp7IZmiD2IBZqEGw3GSdr8OOP1kED0SpEf7AJ72ECWIaMwst%2F%2BvAY6pgHXFYN7tej03qeYbrsS6gn91C8fgOWqQpIZkA8LIYW68%2B%2FrHmm8aq0y7BePIrr65xJRRCMQROKX7m%2BTpnmfVmGiSf4tVfJud3dEG0uvjTKE5s7bUnLUQOIrN8RParvthO%2FodYRSG2p0QnaIbeyWh%2FJyx71nAsR03bYmSDBEuUlPUAKPsGVIoUGibrUhc30668R%2BIE5ZjCeewSH5C4GlZwuKoO2oF0OR&X-Amz-Signature=86e46ea5192e5c22e23794bc79e726ebea7a08c055c45f8340ed0c985e95c330&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBQXTI7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvyuVHJJwj9IJtbzLj8FQctvX7C5KRYI2fXHS2PHLnbAiEA1j5Sm7QYKUwKRQr21h78rX7QVmTmxC7ViaMDgHWOSA8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8o9i3TuxjxIrrTsircA7zjCrYE%2FgRRYE9Afhm3ZginIBEjllqvHkR%2Bwx%2FVXAaVk8d0OK08R2p3G7n4bh4CcCfgWW%2FetQwFoQVynY937mLap7FKi0DhRHk8ghsFD0ReotYfD0yZPKlnOQ%2FUIl1QHdKM5Aon1ICAa3jsu17jGtvMm%2BLNMCNk9p4kj8eCG5G28tQpiqHUMPFMfz%2BhrVs3F%2BQorFpnfYXdIC59G0QLaF%2BW8oy0KgvLjoRMVGMVNyXNcWum1vVV8LarW40l%2Fs5e3ixj5P9j34JvS62KGZ%2FjgQx2JaSgRWuSKZgeqCuCwqbTtuy5fNzRi78HwBnaZuvHPYoLfhDrtDb%2FnhUaZHjpzRzsg0wHdckZ1ua4AgKx68TkPNjfMBKJ0Ji9P58yHvU7oDN3Crz7aP730ron1ypfrvuWaUsONdNoHbay1YxaeYChe7b%2BF50eU81kM7nxVXgNFkx0B7VwbPk65D%2B7oo93KKxP4Uw8lTeXfPterxI3xRH%2FeIIj3e57HooDWOoqKHfDyIuQP6Iz249pi%2BAeTuL5cECNOsUtcR9YpBTfWVioJljjPmeWWF5cPS2qe6oouEdn41F6DELx4yQjdZzJucS071KE%2Fst3BkvFtfOFa4ISONbQBCxplcnDkvSUEtEcMMPY%2FrwGOqUBJsTulVBjDakQiV2GZvkIXYbcGN46vK7S1tSouX0P3LE51ktWgxTtvhjUNYZLmRIbbPpQfClD%2B0Xi%2BYF1f7AOn%2FlmHVKO2FEzLcoMZDeQ97yJ84613pu9Lnltueo08PdE%2FFOzBXQkSIlt%2FwhHwShWVGrCIwZjUUmHqkNH0RQHi6JQNby%2BKlLR0oaJjwOm57Dc1psmyR9BI01riVN42%2FpDnBKRc21Y&X-Amz-Signature=f58bc91ea2a943067c396274707a2b2d83194b8c1fc5f017018cfd3def429c2f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBQXTI7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvyuVHJJwj9IJtbzLj8FQctvX7C5KRYI2fXHS2PHLnbAiEA1j5Sm7QYKUwKRQr21h78rX7QVmTmxC7ViaMDgHWOSA8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8o9i3TuxjxIrrTsircA7zjCrYE%2FgRRYE9Afhm3ZginIBEjllqvHkR%2Bwx%2FVXAaVk8d0OK08R2p3G7n4bh4CcCfgWW%2FetQwFoQVynY937mLap7FKi0DhRHk8ghsFD0ReotYfD0yZPKlnOQ%2FUIl1QHdKM5Aon1ICAa3jsu17jGtvMm%2BLNMCNk9p4kj8eCG5G28tQpiqHUMPFMfz%2BhrVs3F%2BQorFpnfYXdIC59G0QLaF%2BW8oy0KgvLjoRMVGMVNyXNcWum1vVV8LarW40l%2Fs5e3ixj5P9j34JvS62KGZ%2FjgQx2JaSgRWuSKZgeqCuCwqbTtuy5fNzRi78HwBnaZuvHPYoLfhDrtDb%2FnhUaZHjpzRzsg0wHdckZ1ua4AgKx68TkPNjfMBKJ0Ji9P58yHvU7oDN3Crz7aP730ron1ypfrvuWaUsONdNoHbay1YxaeYChe7b%2BF50eU81kM7nxVXgNFkx0B7VwbPk65D%2B7oo93KKxP4Uw8lTeXfPterxI3xRH%2FeIIj3e57HooDWOoqKHfDyIuQP6Iz249pi%2BAeTuL5cECNOsUtcR9YpBTfWVioJljjPmeWWF5cPS2qe6oouEdn41F6DELx4yQjdZzJucS071KE%2Fst3BkvFtfOFa4ISONbQBCxplcnDkvSUEtEcMMPY%2FrwGOqUBJsTulVBjDakQiV2GZvkIXYbcGN46vK7S1tSouX0P3LE51ktWgxTtvhjUNYZLmRIbbPpQfClD%2B0Xi%2BYF1f7AOn%2FlmHVKO2FEzLcoMZDeQ97yJ84613pu9Lnltueo08PdE%2FFOzBXQkSIlt%2FwhHwShWVGrCIwZjUUmHqkNH0RQHi6JQNby%2BKlLR0oaJjwOm57Dc1psmyR9BI01riVN42%2FpDnBKRc21Y&X-Amz-Signature=60f8034df96fbf27d24f3be0c4f709d1e346c361454ff1247c97b894b93e69c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBQXTI7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvyuVHJJwj9IJtbzLj8FQctvX7C5KRYI2fXHS2PHLnbAiEA1j5Sm7QYKUwKRQr21h78rX7QVmTmxC7ViaMDgHWOSA8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8o9i3TuxjxIrrTsircA7zjCrYE%2FgRRYE9Afhm3ZginIBEjllqvHkR%2Bwx%2FVXAaVk8d0OK08R2p3G7n4bh4CcCfgWW%2FetQwFoQVynY937mLap7FKi0DhRHk8ghsFD0ReotYfD0yZPKlnOQ%2FUIl1QHdKM5Aon1ICAa3jsu17jGtvMm%2BLNMCNk9p4kj8eCG5G28tQpiqHUMPFMfz%2BhrVs3F%2BQorFpnfYXdIC59G0QLaF%2BW8oy0KgvLjoRMVGMVNyXNcWum1vVV8LarW40l%2Fs5e3ixj5P9j34JvS62KGZ%2FjgQx2JaSgRWuSKZgeqCuCwqbTtuy5fNzRi78HwBnaZuvHPYoLfhDrtDb%2FnhUaZHjpzRzsg0wHdckZ1ua4AgKx68TkPNjfMBKJ0Ji9P58yHvU7oDN3Crz7aP730ron1ypfrvuWaUsONdNoHbay1YxaeYChe7b%2BF50eU81kM7nxVXgNFkx0B7VwbPk65D%2B7oo93KKxP4Uw8lTeXfPterxI3xRH%2FeIIj3e57HooDWOoqKHfDyIuQP6Iz249pi%2BAeTuL5cECNOsUtcR9YpBTfWVioJljjPmeWWF5cPS2qe6oouEdn41F6DELx4yQjdZzJucS071KE%2Fst3BkvFtfOFa4ISONbQBCxplcnDkvSUEtEcMMPY%2FrwGOqUBJsTulVBjDakQiV2GZvkIXYbcGN46vK7S1tSouX0P3LE51ktWgxTtvhjUNYZLmRIbbPpQfClD%2B0Xi%2BYF1f7AOn%2FlmHVKO2FEzLcoMZDeQ97yJ84613pu9Lnltueo08PdE%2FFOzBXQkSIlt%2FwhHwShWVGrCIwZjUUmHqkNH0RQHi6JQNby%2BKlLR0oaJjwOm57Dc1psmyR9BI01riVN42%2FpDnBKRc21Y&X-Amz-Signature=8e5c82f772f8d6daa42142196a1e34ce49650e823fc9b84a8521999b1eaf2e8b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646QSH5PI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaWfPo7jQfnjTCwub0mgvJRmmncdp%2BeYtLPK%2B3FeK5vQIgT%2Ft0sKAasX9Pf0LolIwaNacWDk747czSlZvOB2s6HTMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADdZkEFlNgx%2FWb2aSrcA538gwlIY%2FvfDRfuzpPOh6xdiWToIP%2BdOd4y3LU1J%2BsHUoeLQGX4fsNPJ2ynzUzXLzERiIMpkTA7%2FgIw9wmHBNAllqutHU0V7NQWHxAMqwu3bKK30WpMhpyp%2FoFYn%2BKtNPPs0VK03aR4XWsKN8ppe%2BHaW4u2lPA%2BRxj5%2BhzN4ASA77VYa6X6mAEY2olZXXjEka1L6PW%2BkPzCKEJC1AZ27hJYgdDlXjETAbnm9HGcnKeXmIh064KUG6K2obQiaft9tX7%2FMuhyReTnRN97SOzHCUyxG%2B5E%2FvQVsglyW8Rt7pemVdMNKo88zH0CBqhSGlgGza21x3vPGWsNRVKPtqRHI0rjDjPzO3LSWpwMjOLFi%2FTdLo3%2Bs41omtG0MYGPY6mWUDbdhPRhSXmcOACMrmkhcLAhrSCQ4FZCy81PF8%2BoxwlWTGM59eQqrn9aWb91jVHrsri1f2l6yQUpIWy9ScYsX8w%2FezzrPYPTJ3h%2F2l34nDLnRCV4oex9Pu%2Bm0E%2F%2BqGj9R%2FtpykarWQxO4tsFshRciM0KAuBuyd6PqmmTYzwc%2B8CGtV9tSLlcpcrRohhKVGQJVfK%2BjYTffogFnopziIHktSZGs4zPtfiS2iLx98iubGWtuvFzrXw%2BEfx5KA3TMLTY%2FrwGOqUB7p7QMJopx6A0p44vKnhUs6A%2FUHZz6XES3tFuIcxIttUONqLkkfraMvqP1%2BqB8ngAQe5JvSk41aOPyl7vJonNBOubYOs380tkeWDJEXrTMAbPuryG6M1EScYLCwYI5SUzfwwT9c1wffo3fnK6RzP47dQlSPyABndycHjBVi1cv5r6w8Gpg62PYtw8SoU%2BIcPk0f6SoRJd8HHHteyJ2K6pbPZGjz3%2B&X-Amz-Signature=9d4a98853e757858aad658caf634e6c353a49a4b032d7511789342649525f372&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWHBOU4Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUs1LvxWgb9rLd%2FJQnvCJ8HnyhgjTGEkRfZRzRzVtSXAiAxjb%2FHbKHVCTnxpJC7cJRV2xvsKYQob2C7SvkPDIqsYiqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhETeZsMNxDfIX%2B6sKtwDsOWgjUVObnPMhKSFrXGBt2oh8MGbcdaa17c3qZiJx%2BqxeIbgwerdyGhGVcJW9Izf1negW5j%2B2cmGtXfhNq%2F4nCz3c0SOpAgwYTZoVexjQysRRF7W%2FNlE%2BscZ%2BblgILZv4fGrrLQdsLMFIrFBC8YRxZiO4YwSMWED753KZBoZ32zF69ot4gt%2BDNxeA1txO0aH4KmkRn6%2FGY9CzcWUEF2qazk2W8r4YTeUuWLKAHitJXckfc8GIMAFEmf9f6YE3KALRgbOdppqwlBLy0a32KPFGE%2F9ObEzzpHCTkNVwLHGp%2FMKSRa3Xi32hJvphXdBwFIwkYbd8l8u76XlW34z6TilQjHSFvUoH51%2Bf1XVINzbiQRJXZV9jyLBOHFxgWEvfXT7tKZGkqoQIwcH%2B5sxfdDgme3aCvPZPWsUwj0hPAFnegZ7VqGyD4fjTmLmrNPPEekAV4I16ODsrutxJtQCgdQJWCvrK53AS8NTesQbhQ8TyIWUh4I1HaDbQzrsx3TincPPAHgBDuXG5BeeFNu0aBKdJrR0n0MdaMrsFVW0KEeK9Z0cMF0w8V48XnD6uALejH67QfI9Jnm7dCMcI4vyA3rt6v82VwNhy%2FGeM5mwxffvSnUL1KtEpUE5SWDKOEEwh9v%2BvAY6pgGhSaXhGNMIVVlemmBtuKpf6sCYB7SR8Ds7zhW5b%2Bfhx%2BbdW%2F6llCUODmPLCDhvzc13z1Cds8pfpifzbkDh%2BicB%2Fw0g22ugyCrQyOopysVkQ6d8kkllarseYmjP6FFDu7%2BEJwh3ifHbER5ScUVj4fQwabN3EJT277Fc0K7HqiANVwGLRNiKWjxerlfIIemhcQ7FEDp8fT04jCFrdRM4Lqh8VKUCkI1M&X-Amz-Signature=7ca2a7d6c092a0eca66dc41fcc8bcce3c72eabbdd521dfd3db52394d058650dc&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ATHE44N%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDL%2BstRet2rhvstkRNw3tyS3W%2FAdRIu5Qn3BWDaFWMxSgIgWWsIDFk2hQDTjGH9%2Fps9cXXzHS5SVT3755BTNkUCeE8qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH2H3j8IemAL8M9uXSrcA4ftH8c9tOirMWfSk5vq3vQRTZ0%2FFFWKw2nJC%2BXxhCLP5j83MQgRVJ0r7tvEJUXs3bdOG%2BHWjDoN8MZZY3vM1lIjzRzIuxF8Aj3P09v31atCDFidGvouw51ISL1yvUCXmxQWjE%2BQN04EZ1WWqm%2BPWxf%2Bl2zMNxjdBhLBgfp9JLSf4yeBulLs0ifT6KtvQ7FoVy8uhINlh3U9DbmMgOQrHDmGuWluGZxtuwXnIb9JEqZSCKwUQAkB0wER9G51IDrQEGOJUt45rHG7zqZPS7MR9ujMU3LgTjMDGOzDVcVWnOgdaHWjZxC%2FffTVxAWV643fPQ%2Fjv6BLmUKOzoRRWW%2FzjHrwc3yJM%2BlOSGpRRnv%2FhVS2%2BCj0GFcJAA2ltfBh55pZdXF1u7sMB3HS9BOTAec6XV1G1hBHYJE4tGfcyRxjlJEQGqhCBgeSPaZnxFYdmG3no6lxUx8fBZwsZupuPn6pNJVLv3K%2Fdt0OT%2FNmVM8A%2BG3hUtLIkKQD7NAQH7sKEIZAJnfbo9XCG9P4%2F%2BBl%2BsECLUB4QvJWvO3Q44%2Bdgg0ywhKzllitZo1LaCWEUFD4eiX4XKaD8JT0X%2F96e%2F8N7GZIUPFK8gJv9OvMCjS5QnwYgFQLWNTFVK%2FQDEK4e%2B9EMJWO%2FrwGOqUBAy9ScqYHBUMzXk0PjiY4jQ1w9tpJjwZHVRwit88w3geD7Gnf0DsmU7s4of8mtrw8NxdAQqjjWDgK2p1%2BXpfgI3abPD4wr6SglhOKKr4uj%2BIpTakCls7sENGssfuxAdG3ooGQvdCdKcdMQYyF6GpaUkA%2Fg0dG2peMk08kZawUGfPc0Y9SRnSpAF5d6GTPfdLFd90ecBqkbZg7EOevs2lijEDolGUp&X-Amz-Signature=395eee435e83b893f50a625573c0be2dd7ad23bd3045201c0b9b1d2c53bddeea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STZU4NB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuuVy2%2FQnVAqG8qzY3LbguP%2FWG9kq5HCfH0TI66Ytw5wIhALWo8WZsN3KO0HaUrRqakJ15YHRUNe%2BBZVDDkMaHTR43KogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B1hmQagxV6i4xMUQq3ANcCzdLcA26ZQcRf%2FhATjOGg9kipB9%2B5T%2FnS3P8EIjszXWk04MjvJij241G3uPhbzvTds0F4SO5p1ucI%2FWFwyjomp8phgZs%2FRt0csuDk52VIxyuMNFAfYPRRgV1HOkx%2FtZD1zr82nJdI8bhPjCKWsfSvnWJPV3OvAfQdlCMv60l0q5DCHLC2oBRI8W48x2qfbbTprcogv3vohp%2BbAvyk%2BD7pRuUXY8YxKYrBlR2y7%2Fgc4ja1VrBmX4ce4PuaM5tsZ7eUU00KPQ60whxo0hhtGAq3byu%2FU7T6IV3WoNJWc%2F44X8IlRx5bQaApdiXq%2FTGUDkaI52SfI5PhPEFzHR9IpYNoW2XX9S4pw5VFo6kpD4du8FFMWESno9a0a640etb%2B9PQQgs57Sx36QgiPOxNDSEr0G%2BLyICbNnBAj9dfimcxwaIeip6Ju%2BmEuJ%2BVVe8wPJsLJlHK9seFmRptMCc%2BPMz8tciPLUkar0i%2FA2vtvGVDRCfotcKWDmUWipQ4XRmjDou1ktqI89NeFRgZKu%2BxZ4U5gnspHILdqg%2Bc5KnhgcNK2vW%2F7f406jDntQgHFb%2BUkF6QmUps%2FSB8kI0Wd16D%2Bn2sEEJ2yB3GpvOKu7d%2BRJqYlHhpupaJgkkxT489PjCH2%2F68BjqkAbF%2BEfbeUTjpaqISgsULwULjZhWyEY5SvcRImwAmeN7HvpK0HuEyvr18jXMKdXSJbNZN%2BQHfKjmUyKq1CHuD4iafF4%2Bw5J0tyMVGZ6SPvex1hL%2F4fAPfjV4MYd%2Be4M5f0wylp5ntnoihP381uGAxPStw4M8Y%2BU%2B2UrXSXKTUrsPs4RYLRGp5fz2%2FEpLgOUWOQIbV4ogVe5R7GXgJ84EBUhlTQy9M&X-Amz-Signature=76d28f5eed7ae407703aacdb6d3da55a8496c9c926d3a882284bcc4b69b187bc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STZU4NB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuuVy2%2FQnVAqG8qzY3LbguP%2FWG9kq5HCfH0TI66Ytw5wIhALWo8WZsN3KO0HaUrRqakJ15YHRUNe%2BBZVDDkMaHTR43KogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B1hmQagxV6i4xMUQq3ANcCzdLcA26ZQcRf%2FhATjOGg9kipB9%2B5T%2FnS3P8EIjszXWk04MjvJij241G3uPhbzvTds0F4SO5p1ucI%2FWFwyjomp8phgZs%2FRt0csuDk52VIxyuMNFAfYPRRgV1HOkx%2FtZD1zr82nJdI8bhPjCKWsfSvnWJPV3OvAfQdlCMv60l0q5DCHLC2oBRI8W48x2qfbbTprcogv3vohp%2BbAvyk%2BD7pRuUXY8YxKYrBlR2y7%2Fgc4ja1VrBmX4ce4PuaM5tsZ7eUU00KPQ60whxo0hhtGAq3byu%2FU7T6IV3WoNJWc%2F44X8IlRx5bQaApdiXq%2FTGUDkaI52SfI5PhPEFzHR9IpYNoW2XX9S4pw5VFo6kpD4du8FFMWESno9a0a640etb%2B9PQQgs57Sx36QgiPOxNDSEr0G%2BLyICbNnBAj9dfimcxwaIeip6Ju%2BmEuJ%2BVVe8wPJsLJlHK9seFmRptMCc%2BPMz8tciPLUkar0i%2FA2vtvGVDRCfotcKWDmUWipQ4XRmjDou1ktqI89NeFRgZKu%2BxZ4U5gnspHILdqg%2Bc5KnhgcNK2vW%2F7f406jDntQgHFb%2BUkF6QmUps%2FSB8kI0Wd16D%2Bn2sEEJ2yB3GpvOKu7d%2BRJqYlHhpupaJgkkxT489PjCH2%2F68BjqkAbF%2BEfbeUTjpaqISgsULwULjZhWyEY5SvcRImwAmeN7HvpK0HuEyvr18jXMKdXSJbNZN%2BQHfKjmUyKq1CHuD4iafF4%2Bw5J0tyMVGZ6SPvex1hL%2F4fAPfjV4MYd%2Be4M5f0wylp5ntnoihP381uGAxPStw4M8Y%2BU%2B2UrXSXKTUrsPs4RYLRGp5fz2%2FEpLgOUWOQIbV4ogVe5R7GXgJ84EBUhlTQy9M&X-Amz-Signature=07e992af05fcc864dbf6ff042143cd266db678270fb9f1939cef04388748f834&X-Amz-SignedHeaders=host&x-id=GetObject)

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
