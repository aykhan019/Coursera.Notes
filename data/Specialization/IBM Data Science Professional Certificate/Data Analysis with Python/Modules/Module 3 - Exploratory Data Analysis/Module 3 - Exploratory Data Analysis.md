

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XUBUDQY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbT631uAnEenPLSYYu5v4hAk6EG91R4kx7o8EfhMQKdwIgX2zyvWJzE%2BpX2wjC1xl2BDSsQ%2B0AEql8QYd2XT4HUeIqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDRWaXZdj4oi9OrTMircAzMXQ2PHlAJO6%2Fnlox2D2l%2FDUoBDp28KDak8sRNK9brD90m5wQM%2FfE%2B424EcAu54KyeKMuRrTKhq6PuwWY5MwmNygdx9nwPrxAhdcRNoiXfZf9zKML16hgTJIncMY%2B3fh8lE6LodKVs4QIurjh5E45c1PJX3N0Z64qQTheSJKU8Xyn7rmtVwi%2B4S1T7n8iueZVKWKQj3HmovIlXoJPr5%2FSdkXotQ%2FHIdpGcKQMAVRukmGIxTP4t9qMzHazz8JqK4lhOYOrWk%2Bxng%2B3H3NGfXVp8cM0bGW8yGmg9nJecEXeBne5h4aqS%2F6QuJtDEOEpWnv82d%2BCcziD8ClyAZ8qqQuQuvsuowMOA%2BzhGXSLHWyNFSeBQ3c58v9bbAoL%2F%2FM3ACdiymXImjpvDjUIK6xDtvylIDXK75AfO66eucWUOFU7upImMC%2F2g3JIIRGHhsuhoUQCKf0LPHOITq0KwsMZRLPqA6jO3ebbScQRuVkJjhxsLnNPUv4tYF3%2F%2FJxLCvNIf60ZTzTeIyXLyX7TbWk0Buwc4QLWQ6qGPKLzESQBUhEOXocC9BoIEujDpWQsgPVwKkvQhWPrUpL3cyJ%2BmPRL53FeZO7Mo6QG7WATZG00YAryef4ytAH%2FDsbzUwl867MMnQ8LwGOqUBHbSVv2QH8Mj26%2BvKImVkR4XcgbMhAe7mF0BBr4YardfNixKnFm6fDES2WKnEcRtgO10Xkk8RDjFRb%2FadFiczQ0ujDQY93N3tA5iBRHSVAMN%2FJ%2BeWDxpIZ%2BrDBrKz1fjKNhp4lS9Mob%2FkLLjoVdDvhvdPw7fmJfjGrrIheTIYEwBXrTfz2%2FaDOck4SURvENepRgz4LDJALE%2BC0dd1UWtMtIAJxz0o&X-Amz-Signature=10cea448a36f62fdcf8e25966dc72fc213d47cef3cc4c324009fe73785debe98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XUBUDQY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbT631uAnEenPLSYYu5v4hAk6EG91R4kx7o8EfhMQKdwIgX2zyvWJzE%2BpX2wjC1xl2BDSsQ%2B0AEql8QYd2XT4HUeIqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDRWaXZdj4oi9OrTMircAzMXQ2PHlAJO6%2Fnlox2D2l%2FDUoBDp28KDak8sRNK9brD90m5wQM%2FfE%2B424EcAu54KyeKMuRrTKhq6PuwWY5MwmNygdx9nwPrxAhdcRNoiXfZf9zKML16hgTJIncMY%2B3fh8lE6LodKVs4QIurjh5E45c1PJX3N0Z64qQTheSJKU8Xyn7rmtVwi%2B4S1T7n8iueZVKWKQj3HmovIlXoJPr5%2FSdkXotQ%2FHIdpGcKQMAVRukmGIxTP4t9qMzHazz8JqK4lhOYOrWk%2Bxng%2B3H3NGfXVp8cM0bGW8yGmg9nJecEXeBne5h4aqS%2F6QuJtDEOEpWnv82d%2BCcziD8ClyAZ8qqQuQuvsuowMOA%2BzhGXSLHWyNFSeBQ3c58v9bbAoL%2F%2FM3ACdiymXImjpvDjUIK6xDtvylIDXK75AfO66eucWUOFU7upImMC%2F2g3JIIRGHhsuhoUQCKf0LPHOITq0KwsMZRLPqA6jO3ebbScQRuVkJjhxsLnNPUv4tYF3%2F%2FJxLCvNIf60ZTzTeIyXLyX7TbWk0Buwc4QLWQ6qGPKLzESQBUhEOXocC9BoIEujDpWQsgPVwKkvQhWPrUpL3cyJ%2BmPRL53FeZO7Mo6QG7WATZG00YAryef4ytAH%2FDsbzUwl867MMnQ8LwGOqUBHbSVv2QH8Mj26%2BvKImVkR4XcgbMhAe7mF0BBr4YardfNixKnFm6fDES2WKnEcRtgO10Xkk8RDjFRb%2FadFiczQ0ujDQY93N3tA5iBRHSVAMN%2FJ%2BeWDxpIZ%2BrDBrKz1fjKNhp4lS9Mob%2FkLLjoVdDvhvdPw7fmJfjGrrIheTIYEwBXrTfz2%2FaDOck4SURvENepRgz4LDJALE%2BC0dd1UWtMtIAJxz0o&X-Amz-Signature=875172102fc81b48bb7bd523cac0e16703feb4044d493408b1c364a2e1cc37ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XUBUDQY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbT631uAnEenPLSYYu5v4hAk6EG91R4kx7o8EfhMQKdwIgX2zyvWJzE%2BpX2wjC1xl2BDSsQ%2B0AEql8QYd2XT4HUeIqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDRWaXZdj4oi9OrTMircAzMXQ2PHlAJO6%2Fnlox2D2l%2FDUoBDp28KDak8sRNK9brD90m5wQM%2FfE%2B424EcAu54KyeKMuRrTKhq6PuwWY5MwmNygdx9nwPrxAhdcRNoiXfZf9zKML16hgTJIncMY%2B3fh8lE6LodKVs4QIurjh5E45c1PJX3N0Z64qQTheSJKU8Xyn7rmtVwi%2B4S1T7n8iueZVKWKQj3HmovIlXoJPr5%2FSdkXotQ%2FHIdpGcKQMAVRukmGIxTP4t9qMzHazz8JqK4lhOYOrWk%2Bxng%2B3H3NGfXVp8cM0bGW8yGmg9nJecEXeBne5h4aqS%2F6QuJtDEOEpWnv82d%2BCcziD8ClyAZ8qqQuQuvsuowMOA%2BzhGXSLHWyNFSeBQ3c58v9bbAoL%2F%2FM3ACdiymXImjpvDjUIK6xDtvylIDXK75AfO66eucWUOFU7upImMC%2F2g3JIIRGHhsuhoUQCKf0LPHOITq0KwsMZRLPqA6jO3ebbScQRuVkJjhxsLnNPUv4tYF3%2F%2FJxLCvNIf60ZTzTeIyXLyX7TbWk0Buwc4QLWQ6qGPKLzESQBUhEOXocC9BoIEujDpWQsgPVwKkvQhWPrUpL3cyJ%2BmPRL53FeZO7Mo6QG7WATZG00YAryef4ytAH%2FDsbzUwl867MMnQ8LwGOqUBHbSVv2QH8Mj26%2BvKImVkR4XcgbMhAe7mF0BBr4YardfNixKnFm6fDES2WKnEcRtgO10Xkk8RDjFRb%2FadFiczQ0ujDQY93N3tA5iBRHSVAMN%2FJ%2BeWDxpIZ%2BrDBrKz1fjKNhp4lS9Mob%2FkLLjoVdDvhvdPw7fmJfjGrrIheTIYEwBXrTfz2%2FaDOck4SURvENepRgz4LDJALE%2BC0dd1UWtMtIAJxz0o&X-Amz-Signature=3335d587dff749f6c53de46e5fde8304e0cdbf149444ee552b11d460b9bed854&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQWXTLO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPBpe%2BO%2BvjD0vcCCwMztyp3SLlQObHYd3INLquyOAPAiAzVtXmha3YLWZX21QYyRhFRDtK33cfqekjr8HDmNJuVCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7b1knC7DoWi24wt9KtwD6%2BqJGqaV3UBpubvi4gaXArsGBUIuLxATXEYW24dbl4hzWYB0bJ6epViUaoRuwm2CdiSuDMxICvGuOeEuwYIvf%2Fdwa%2FGtK8IAq45BL7BjVTfn3qvx2%2B%2FuBUMwUuKSDVik697UG16hCeTb6cwfVKrrcYQARHqkOtr4noN%2B0buofnBgNnUIDjByCDX1I6E3baSuqTO4Q3Qk4QpIuPogmILYdagP76Ru%2FVyrROGY6BlEyzChBmyyQdXoLRkth2NnnoghLvlAs03f4vWiZpOvPgyKwDyAsYy689tPzqCORChgVLnFXc5iY49A3S7fhHz8ZgZNtrnhhJoeN9WXlGhhknUoNAffNB%2FxERGOgRnOiz%2FLsVt9poDikuwE9I93%2BpqjS7wEFXKg%2BAaYBrm5dML0Hpe%2FQKHeqMQY4%2F3HPHg0rtAkd%2B2w8Y8GG2QVY5ywtLYu4ScyAbT8zgixVMebFi5%2FkEW8RTae0rd3rklz63%2FRB4r4xpNflq2HZjgvePOZjirKlNlS3HGHz8w%2F%2B9MorOJvUMwIME5J2BnGlgBaZzomQa7%2FWViT2aCsG6%2FbRbnolNXthFyt7w79JI6Oep%2BiSDzkzi5bciMLPHSSd9Q0NKMmMBa9h6Sn7f1FUwb6DQhbzZ0w3NHwvAY6pgGCjFh4ndOx91%2B%2Bzha5v5qWUhw8H4Nu%2BHLg0lrl7jUMAUhRp9gHUMbEhTqTapiZaaMkInaML8Ybk%2FisAwl26f9JLUagnTBb40weqi%2BZpJoJTtT1xpR75aam%2FZmLDR5gdeQmzazcycCNKufH14bdHLO%2BxcRP1mtiRSVQ40mN%2Brmm2ECN%2FOGSwokf%2F3ndogIZk2IiyHr7i1mfMtKtXCDdDuCPu1omCO8b&X-Amz-Signature=e524dfdc7e718b0e8f0735ec9c651d14ed6db2c7edbd1c7cd15b41eaf3efacab&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQWXTLO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPBpe%2BO%2BvjD0vcCCwMztyp3SLlQObHYd3INLquyOAPAiAzVtXmha3YLWZX21QYyRhFRDtK33cfqekjr8HDmNJuVCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7b1knC7DoWi24wt9KtwD6%2BqJGqaV3UBpubvi4gaXArsGBUIuLxATXEYW24dbl4hzWYB0bJ6epViUaoRuwm2CdiSuDMxICvGuOeEuwYIvf%2Fdwa%2FGtK8IAq45BL7BjVTfn3qvx2%2B%2FuBUMwUuKSDVik697UG16hCeTb6cwfVKrrcYQARHqkOtr4noN%2B0buofnBgNnUIDjByCDX1I6E3baSuqTO4Q3Qk4QpIuPogmILYdagP76Ru%2FVyrROGY6BlEyzChBmyyQdXoLRkth2NnnoghLvlAs03f4vWiZpOvPgyKwDyAsYy689tPzqCORChgVLnFXc5iY49A3S7fhHz8ZgZNtrnhhJoeN9WXlGhhknUoNAffNB%2FxERGOgRnOiz%2FLsVt9poDikuwE9I93%2BpqjS7wEFXKg%2BAaYBrm5dML0Hpe%2FQKHeqMQY4%2F3HPHg0rtAkd%2B2w8Y8GG2QVY5ywtLYu4ScyAbT8zgixVMebFi5%2FkEW8RTae0rd3rklz63%2FRB4r4xpNflq2HZjgvePOZjirKlNlS3HGHz8w%2F%2B9MorOJvUMwIME5J2BnGlgBaZzomQa7%2FWViT2aCsG6%2FbRbnolNXthFyt7w79JI6Oep%2BiSDzkzi5bciMLPHSSd9Q0NKMmMBa9h6Sn7f1FUwb6DQhbzZ0w3NHwvAY6pgGCjFh4ndOx91%2B%2Bzha5v5qWUhw8H4Nu%2BHLg0lrl7jUMAUhRp9gHUMbEhTqTapiZaaMkInaML8Ybk%2FisAwl26f9JLUagnTBb40weqi%2BZpJoJTtT1xpR75aam%2FZmLDR5gdeQmzazcycCNKufH14bdHLO%2BxcRP1mtiRSVQ40mN%2Brmm2ECN%2FOGSwokf%2F3ndogIZk2IiyHr7i1mfMtKtXCDdDuCPu1omCO8b&X-Amz-Signature=d777eefdf450da4691ae23c9296f9b6b6d12914aab03e071b5fb6dcec9a429da&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQWXTLO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPBpe%2BO%2BvjD0vcCCwMztyp3SLlQObHYd3INLquyOAPAiAzVtXmha3YLWZX21QYyRhFRDtK33cfqekjr8HDmNJuVCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7b1knC7DoWi24wt9KtwD6%2BqJGqaV3UBpubvi4gaXArsGBUIuLxATXEYW24dbl4hzWYB0bJ6epViUaoRuwm2CdiSuDMxICvGuOeEuwYIvf%2Fdwa%2FGtK8IAq45BL7BjVTfn3qvx2%2B%2FuBUMwUuKSDVik697UG16hCeTb6cwfVKrrcYQARHqkOtr4noN%2B0buofnBgNnUIDjByCDX1I6E3baSuqTO4Q3Qk4QpIuPogmILYdagP76Ru%2FVyrROGY6BlEyzChBmyyQdXoLRkth2NnnoghLvlAs03f4vWiZpOvPgyKwDyAsYy689tPzqCORChgVLnFXc5iY49A3S7fhHz8ZgZNtrnhhJoeN9WXlGhhknUoNAffNB%2FxERGOgRnOiz%2FLsVt9poDikuwE9I93%2BpqjS7wEFXKg%2BAaYBrm5dML0Hpe%2FQKHeqMQY4%2F3HPHg0rtAkd%2B2w8Y8GG2QVY5ywtLYu4ScyAbT8zgixVMebFi5%2FkEW8RTae0rd3rklz63%2FRB4r4xpNflq2HZjgvePOZjirKlNlS3HGHz8w%2F%2B9MorOJvUMwIME5J2BnGlgBaZzomQa7%2FWViT2aCsG6%2FbRbnolNXthFyt7w79JI6Oep%2BiSDzkzi5bciMLPHSSd9Q0NKMmMBa9h6Sn7f1FUwb6DQhbzZ0w3NHwvAY6pgGCjFh4ndOx91%2B%2Bzha5v5qWUhw8H4Nu%2BHLg0lrl7jUMAUhRp9gHUMbEhTqTapiZaaMkInaML8Ybk%2FisAwl26f9JLUagnTBb40weqi%2BZpJoJTtT1xpR75aam%2FZmLDR5gdeQmzazcycCNKufH14bdHLO%2BxcRP1mtiRSVQ40mN%2Brmm2ECN%2FOGSwokf%2F3ndogIZk2IiyHr7i1mfMtKtXCDdDuCPu1omCO8b&X-Amz-Signature=56a3a74ac4e0e587b03594edac80a1313ea67834cdacfd84cd746b75e581459d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQWXTLO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPBpe%2BO%2BvjD0vcCCwMztyp3SLlQObHYd3INLquyOAPAiAzVtXmha3YLWZX21QYyRhFRDtK33cfqekjr8HDmNJuVCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7b1knC7DoWi24wt9KtwD6%2BqJGqaV3UBpubvi4gaXArsGBUIuLxATXEYW24dbl4hzWYB0bJ6epViUaoRuwm2CdiSuDMxICvGuOeEuwYIvf%2Fdwa%2FGtK8IAq45BL7BjVTfn3qvx2%2B%2FuBUMwUuKSDVik697UG16hCeTb6cwfVKrrcYQARHqkOtr4noN%2B0buofnBgNnUIDjByCDX1I6E3baSuqTO4Q3Qk4QpIuPogmILYdagP76Ru%2FVyrROGY6BlEyzChBmyyQdXoLRkth2NnnoghLvlAs03f4vWiZpOvPgyKwDyAsYy689tPzqCORChgVLnFXc5iY49A3S7fhHz8ZgZNtrnhhJoeN9WXlGhhknUoNAffNB%2FxERGOgRnOiz%2FLsVt9poDikuwE9I93%2BpqjS7wEFXKg%2BAaYBrm5dML0Hpe%2FQKHeqMQY4%2F3HPHg0rtAkd%2B2w8Y8GG2QVY5ywtLYu4ScyAbT8zgixVMebFi5%2FkEW8RTae0rd3rklz63%2FRB4r4xpNflq2HZjgvePOZjirKlNlS3HGHz8w%2F%2B9MorOJvUMwIME5J2BnGlgBaZzomQa7%2FWViT2aCsG6%2FbRbnolNXthFyt7w79JI6Oep%2BiSDzkzi5bciMLPHSSd9Q0NKMmMBa9h6Sn7f1FUwb6DQhbzZ0w3NHwvAY6pgGCjFh4ndOx91%2B%2Bzha5v5qWUhw8H4Nu%2BHLg0lrl7jUMAUhRp9gHUMbEhTqTapiZaaMkInaML8Ybk%2FisAwl26f9JLUagnTBb40weqi%2BZpJoJTtT1xpR75aam%2FZmLDR5gdeQmzazcycCNKufH14bdHLO%2BxcRP1mtiRSVQ40mN%2Brmm2ECN%2FOGSwokf%2F3ndogIZk2IiyHr7i1mfMtKtXCDdDuCPu1omCO8b&X-Amz-Signature=c591e315b8839f6c764bba1490d54cd4c73d19c85050cd34364ba3b69b848019&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQWXTLO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPBpe%2BO%2BvjD0vcCCwMztyp3SLlQObHYd3INLquyOAPAiAzVtXmha3YLWZX21QYyRhFRDtK33cfqekjr8HDmNJuVCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7b1knC7DoWi24wt9KtwD6%2BqJGqaV3UBpubvi4gaXArsGBUIuLxATXEYW24dbl4hzWYB0bJ6epViUaoRuwm2CdiSuDMxICvGuOeEuwYIvf%2Fdwa%2FGtK8IAq45BL7BjVTfn3qvx2%2B%2FuBUMwUuKSDVik697UG16hCeTb6cwfVKrrcYQARHqkOtr4noN%2B0buofnBgNnUIDjByCDX1I6E3baSuqTO4Q3Qk4QpIuPogmILYdagP76Ru%2FVyrROGY6BlEyzChBmyyQdXoLRkth2NnnoghLvlAs03f4vWiZpOvPgyKwDyAsYy689tPzqCORChgVLnFXc5iY49A3S7fhHz8ZgZNtrnhhJoeN9WXlGhhknUoNAffNB%2FxERGOgRnOiz%2FLsVt9poDikuwE9I93%2BpqjS7wEFXKg%2BAaYBrm5dML0Hpe%2FQKHeqMQY4%2F3HPHg0rtAkd%2B2w8Y8GG2QVY5ywtLYu4ScyAbT8zgixVMebFi5%2FkEW8RTae0rd3rklz63%2FRB4r4xpNflq2HZjgvePOZjirKlNlS3HGHz8w%2F%2B9MorOJvUMwIME5J2BnGlgBaZzomQa7%2FWViT2aCsG6%2FbRbnolNXthFyt7w79JI6Oep%2BiSDzkzi5bciMLPHSSd9Q0NKMmMBa9h6Sn7f1FUwb6DQhbzZ0w3NHwvAY6pgGCjFh4ndOx91%2B%2Bzha5v5qWUhw8H4Nu%2BHLg0lrl7jUMAUhRp9gHUMbEhTqTapiZaaMkInaML8Ybk%2FisAwl26f9JLUagnTBb40weqi%2BZpJoJTtT1xpR75aam%2FZmLDR5gdeQmzazcycCNKufH14bdHLO%2BxcRP1mtiRSVQ40mN%2Brmm2ECN%2FOGSwokf%2F3ndogIZk2IiyHr7i1mfMtKtXCDdDuCPu1omCO8b&X-Amz-Signature=4d4d350d87deeacb1351c79da9782b1d370e20065fcdcb61fb976f74a55b1e64&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQWXTLO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPBpe%2BO%2BvjD0vcCCwMztyp3SLlQObHYd3INLquyOAPAiAzVtXmha3YLWZX21QYyRhFRDtK33cfqekjr8HDmNJuVCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7b1knC7DoWi24wt9KtwD6%2BqJGqaV3UBpubvi4gaXArsGBUIuLxATXEYW24dbl4hzWYB0bJ6epViUaoRuwm2CdiSuDMxICvGuOeEuwYIvf%2Fdwa%2FGtK8IAq45BL7BjVTfn3qvx2%2B%2FuBUMwUuKSDVik697UG16hCeTb6cwfVKrrcYQARHqkOtr4noN%2B0buofnBgNnUIDjByCDX1I6E3baSuqTO4Q3Qk4QpIuPogmILYdagP76Ru%2FVyrROGY6BlEyzChBmyyQdXoLRkth2NnnoghLvlAs03f4vWiZpOvPgyKwDyAsYy689tPzqCORChgVLnFXc5iY49A3S7fhHz8ZgZNtrnhhJoeN9WXlGhhknUoNAffNB%2FxERGOgRnOiz%2FLsVt9poDikuwE9I93%2BpqjS7wEFXKg%2BAaYBrm5dML0Hpe%2FQKHeqMQY4%2F3HPHg0rtAkd%2B2w8Y8GG2QVY5ywtLYu4ScyAbT8zgixVMebFi5%2FkEW8RTae0rd3rklz63%2FRB4r4xpNflq2HZjgvePOZjirKlNlS3HGHz8w%2F%2B9MorOJvUMwIME5J2BnGlgBaZzomQa7%2FWViT2aCsG6%2FbRbnolNXthFyt7w79JI6Oep%2BiSDzkzi5bciMLPHSSd9Q0NKMmMBa9h6Sn7f1FUwb6DQhbzZ0w3NHwvAY6pgGCjFh4ndOx91%2B%2Bzha5v5qWUhw8H4Nu%2BHLg0lrl7jUMAUhRp9gHUMbEhTqTapiZaaMkInaML8Ybk%2FisAwl26f9JLUagnTBb40weqi%2BZpJoJTtT1xpR75aam%2FZmLDR5gdeQmzazcycCNKufH14bdHLO%2BxcRP1mtiRSVQ40mN%2Brmm2ECN%2FOGSwokf%2F3ndogIZk2IiyHr7i1mfMtKtXCDdDuCPu1omCO8b&X-Amz-Signature=354e7a8966e2463f07774ac1f72508718bf964951187e7b6d8e9d43cd6d1a4d6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LIGEVKR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCy9uHZ9ZBQinf%2B1sG2zl1da%2FZyFwzYannjINRpGyHvGAIhAPx1z4Mc2LjWpR5GkwLxLn%2BoDCpxmCKnZUcilWAHKUv7KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRF6vuYsH8f7JZ0HAq3APfANijVd7Qvh9RHlwhbf607mi9ukhbpDc%2Bwyljnmv0kATsvGXOl3B%2FfyWpdQ6hBsvuJSbpHWulgSHwmWY05y5zFQhXM21zVDHzJl2Ervx1umeSlRnDSweAtdQ77qJDsRweq72tAKw9QD%2FGGIsV5diXMlNbmCK4sPKZ8SOl1vjhFS1bWGbiUU%2FjonTaZTnXjv%2BeKTir59NpoKzPF3M3dzyYnl08o0pqFQzrk6e5BXEQg46ssnV25v%2Fz4fBH9ZhHASd4DnJJ0CnCbfkOsbNpETm3etnywtLcirm6wg%2BxBnwpBUX0lQSKzkmAmtD1%2FaqMwYYmIKWMuX2sbytQzwYCIImo460%2BcYsb5KUrMd70yGgsx%2FIlhXZk8b9FoV3psiZOyK2%2Bi%2BdWmusQw%2BPqiitTemZhS2W1pog8DFzJEWIObcPHaRzb%2BO%2B9d3a1jWv%2BP2Hm3htld%2BHBLruR9h4LREnvt5Z9ob8yYso9%2BwsCssfY6gIq%2F0WaJQiBoyIYW4BaMK8W7xEDD5yscQYQZccGq2h5DmxmwDOgIfA2lt%2F8zDPo7vC2vvyYYpdKjW8LvNj9XXZ6hZ0ffppcQOnwFkYBcvYWsO85TROdXUXERV4bk%2FjWVFdoUL%2Br4jrOvxnARsLIKDCI0PC8BjqkAYSiZR6B3fvkLxX%2BYSgpcRejOl3k%2FaOgFHGut6iJHrPmY9qs22I72%2Bj61rv76WA19TK4d4gYBER%2FoC0%2FIos2V3duzkkQBUc%2FFRBC1D%2BWEndH5t6nU7Iq459kiXPmjih%2BbL69vwCa3DSbiVPuUEDj7Aq6Ub4YnKlNVaj%2BC%2F3HfZ0ikIJSg26Z1mc%2FxkGWHNYDZwkzcY7bm03QuwzAO3GSQ%2BefsSNF&X-Amz-Signature=8c2cf64417cb73b5f9afe6db43a48fe0c789f7ea162f6537a699a22a26399577&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAIZ4PHX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH4G5fRriS%2F579D33b3mu9zHKlj4Jh95MhLNRoy6KHQ4AiASOdBj%2BlQqW9mG60P9aTHk1LGtY0iH%2BQ8DSH3NvFVkkCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6LIzRA1OQtlYuhSIKtwDUz3Ay4P%2B0Q8yf091z8YJTeqXgp5B44hJvGgYnbr7eLCL6Xl0SR0%2F8vGngHnX8lFSnC0zQG6PnoipS%2BwlrSRFF3dtZAxB3Zn%2BT7umJDnLtjUvXI8K8nj2RP%2BiEkx%2BxxoBYIJRtNhMKAq6J1RPDN77F75b8xf77GWCeggWfDOyIb0N2FyITjKWwmWMu838nPm9xYjsBpOFkO%2FxMVwI%2BDnDHY%2FfoD%2Biqi6CdUvIfJYkcKh95Kag4Nlxk0Osku512T2vFl3OaPjweANcVlsfFdEtzyNl74mJkUp9hzbWxrGKizmwV6wpfq1DM4l4ba%2F0DV2rTdeZ1UjPJRLt54FJaSkTjb65TF5YCK6HKtZt3%2FIKv3k1chO68o8l84Rwmn4KYGpCR08QyuO1gZW7XSsiHUn8moB8lEyeMzd4UZJIgT6OraYPWBSo8i6qqVG346FDg03CXsNJJk1XKrM08PP8t7mW7wb0s4ERF2Izf3dWHHFWNHsfOrXIAM6SHe38uZ0lDM8GjXdCBBOQGpewyiDmXwS3VPmMOiPRG4ZrkkuCFO2BwCdKM5VQ7oI38vzXv8q1IpK2eoOSByvQmRZqqzitLFUQfRXZnO2UEJRPCWZfPVIqUgn6mEO5g4R9mRiSPxEwhdDwvAY6pgF2pg8Ij27fCF90%2FCSwchz1cFpnWunxYMbOuHj5kvuKL9802KRmHlDJgoX2caEqzxhKall1lM52IisLcOwJx3ecg8wYwVpNUPAghaMhDRdoUN5F2WSCz35DI4pLhQXFVhSNkELBgYfcoUiZPQacHd9xkuDBR%2FBdEccQjoTCVoFmaB9JBVrIl6gACu7VnJ%2BgtMILqS4G%2Fo7VrD%2FpWQAJmolIm65F%2BuJ9&X-Amz-Signature=50281fa0d0cb714e7ffa41245bf0a8d0e1db96c625d92ce73b5e8c8e052cbf35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQWXTLO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPBpe%2BO%2BvjD0vcCCwMztyp3SLlQObHYd3INLquyOAPAiAzVtXmha3YLWZX21QYyRhFRDtK33cfqekjr8HDmNJuVCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7b1knC7DoWi24wt9KtwD6%2BqJGqaV3UBpubvi4gaXArsGBUIuLxATXEYW24dbl4hzWYB0bJ6epViUaoRuwm2CdiSuDMxICvGuOeEuwYIvf%2Fdwa%2FGtK8IAq45BL7BjVTfn3qvx2%2B%2FuBUMwUuKSDVik697UG16hCeTb6cwfVKrrcYQARHqkOtr4noN%2B0buofnBgNnUIDjByCDX1I6E3baSuqTO4Q3Qk4QpIuPogmILYdagP76Ru%2FVyrROGY6BlEyzChBmyyQdXoLRkth2NnnoghLvlAs03f4vWiZpOvPgyKwDyAsYy689tPzqCORChgVLnFXc5iY49A3S7fhHz8ZgZNtrnhhJoeN9WXlGhhknUoNAffNB%2FxERGOgRnOiz%2FLsVt9poDikuwE9I93%2BpqjS7wEFXKg%2BAaYBrm5dML0Hpe%2FQKHeqMQY4%2F3HPHg0rtAkd%2B2w8Y8GG2QVY5ywtLYu4ScyAbT8zgixVMebFi5%2FkEW8RTae0rd3rklz63%2FRB4r4xpNflq2HZjgvePOZjirKlNlS3HGHz8w%2F%2B9MorOJvUMwIME5J2BnGlgBaZzomQa7%2FWViT2aCsG6%2FbRbnolNXthFyt7w79JI6Oep%2BiSDzkzi5bciMLPHSSd9Q0NKMmMBa9h6Sn7f1FUwb6DQhbzZ0w3NHwvAY6pgGCjFh4ndOx91%2B%2Bzha5v5qWUhw8H4Nu%2BHLg0lrl7jUMAUhRp9gHUMbEhTqTapiZaaMkInaML8Ybk%2FisAwl26f9JLUagnTBb40weqi%2BZpJoJTtT1xpR75aam%2FZmLDR5gdeQmzazcycCNKufH14bdHLO%2BxcRP1mtiRSVQ40mN%2Brmm2ECN%2FOGSwokf%2F3ndogIZk2IiyHr7i1mfMtKtXCDdDuCPu1omCO8b&X-Amz-Signature=962ccd1edd71d38affeafc70432d91dcdfefb4c7ef57d6a7e79c0d090e1527c6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQWXTLO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPBpe%2BO%2BvjD0vcCCwMztyp3SLlQObHYd3INLquyOAPAiAzVtXmha3YLWZX21QYyRhFRDtK33cfqekjr8HDmNJuVCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7b1knC7DoWi24wt9KtwD6%2BqJGqaV3UBpubvi4gaXArsGBUIuLxATXEYW24dbl4hzWYB0bJ6epViUaoRuwm2CdiSuDMxICvGuOeEuwYIvf%2Fdwa%2FGtK8IAq45BL7BjVTfn3qvx2%2B%2FuBUMwUuKSDVik697UG16hCeTb6cwfVKrrcYQARHqkOtr4noN%2B0buofnBgNnUIDjByCDX1I6E3baSuqTO4Q3Qk4QpIuPogmILYdagP76Ru%2FVyrROGY6BlEyzChBmyyQdXoLRkth2NnnoghLvlAs03f4vWiZpOvPgyKwDyAsYy689tPzqCORChgVLnFXc5iY49A3S7fhHz8ZgZNtrnhhJoeN9WXlGhhknUoNAffNB%2FxERGOgRnOiz%2FLsVt9poDikuwE9I93%2BpqjS7wEFXKg%2BAaYBrm5dML0Hpe%2FQKHeqMQY4%2F3HPHg0rtAkd%2B2w8Y8GG2QVY5ywtLYu4ScyAbT8zgixVMebFi5%2FkEW8RTae0rd3rklz63%2FRB4r4xpNflq2HZjgvePOZjirKlNlS3HGHz8w%2F%2B9MorOJvUMwIME5J2BnGlgBaZzomQa7%2FWViT2aCsG6%2FbRbnolNXthFyt7w79JI6Oep%2BiSDzkzi5bciMLPHSSd9Q0NKMmMBa9h6Sn7f1FUwb6DQhbzZ0w3NHwvAY6pgGCjFh4ndOx91%2B%2Bzha5v5qWUhw8H4Nu%2BHLg0lrl7jUMAUhRp9gHUMbEhTqTapiZaaMkInaML8Ybk%2FisAwl26f9JLUagnTBb40weqi%2BZpJoJTtT1xpR75aam%2FZmLDR5gdeQmzazcycCNKufH14bdHLO%2BxcRP1mtiRSVQ40mN%2Brmm2ECN%2FOGSwokf%2F3ndogIZk2IiyHr7i1mfMtKtXCDdDuCPu1omCO8b&X-Amz-Signature=d30397700dc854e71f46d413b054e84c55c314c6a18ecbe4c36d958aa81324c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYQWXTLO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqPBpe%2BO%2BvjD0vcCCwMztyp3SLlQObHYd3INLquyOAPAiAzVtXmha3YLWZX21QYyRhFRDtK33cfqekjr8HDmNJuVCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7b1knC7DoWi24wt9KtwD6%2BqJGqaV3UBpubvi4gaXArsGBUIuLxATXEYW24dbl4hzWYB0bJ6epViUaoRuwm2CdiSuDMxICvGuOeEuwYIvf%2Fdwa%2FGtK8IAq45BL7BjVTfn3qvx2%2B%2FuBUMwUuKSDVik697UG16hCeTb6cwfVKrrcYQARHqkOtr4noN%2B0buofnBgNnUIDjByCDX1I6E3baSuqTO4Q3Qk4QpIuPogmILYdagP76Ru%2FVyrROGY6BlEyzChBmyyQdXoLRkth2NnnoghLvlAs03f4vWiZpOvPgyKwDyAsYy689tPzqCORChgVLnFXc5iY49A3S7fhHz8ZgZNtrnhhJoeN9WXlGhhknUoNAffNB%2FxERGOgRnOiz%2FLsVt9poDikuwE9I93%2BpqjS7wEFXKg%2BAaYBrm5dML0Hpe%2FQKHeqMQY4%2F3HPHg0rtAkd%2B2w8Y8GG2QVY5ywtLYu4ScyAbT8zgixVMebFi5%2FkEW8RTae0rd3rklz63%2FRB4r4xpNflq2HZjgvePOZjirKlNlS3HGHz8w%2F%2B9MorOJvUMwIME5J2BnGlgBaZzomQa7%2FWViT2aCsG6%2FbRbnolNXthFyt7w79JI6Oep%2BiSDzkzi5bciMLPHSSd9Q0NKMmMBa9h6Sn7f1FUwb6DQhbzZ0w3NHwvAY6pgGCjFh4ndOx91%2B%2Bzha5v5qWUhw8H4Nu%2BHLg0lrl7jUMAUhRp9gHUMbEhTqTapiZaaMkInaML8Ybk%2FisAwl26f9JLUagnTBb40weqi%2BZpJoJTtT1xpR75aam%2FZmLDR5gdeQmzazcycCNKufH14bdHLO%2BxcRP1mtiRSVQ40mN%2Brmm2ECN%2FOGSwokf%2F3ndogIZk2IiyHr7i1mfMtKtXCDdDuCPu1omCO8b&X-Amz-Signature=7f284f731d043fd7c02f296d6a70e16b96325bc3a5ed21ae510cbbf950e4a76f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KLANEIX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4eDh1FA3bXFX1BYbd13czZXkTZCiN8oXaahzwhCSEpwIgdrH9Tcei72x68kEEYoVmH%2BgJxZed4PbLyvvO%2B%2Flau%2BoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnHAFk25eUdwAoFXSrcA0SyK04l%2FL0%2BTHVTie3wLfSblGxOy2wW%2FpTexOpZ81R8Zb2wjOn55uE0xOr0XM%2FSPP2IHJv6KeoZXeUApJnrczssfI5Gv0KFiaYt2uKZ%2FKAUkqMPiOHErKlvRTB8YP21%2B%2FSBE0vPHoHK8IgX%2B73NnBUOzxax%2B1V3QrUgV2W3Nr4bgDwYXul%2FjPNsYxPkzGtjaNZ5lde6uECvTSVANksFmmL6rYBAeMgCV6sO7mlDdkRSX6KrbC9Yq4nZ5EhgkvtmHNLiFIOad42QTX%2FyqOeSyFKGsXl1HaDP7zlNFNFqA%2F3%2FeEoCIQwTXo8wSUdmSK4qDR7wMAI5qdTBI6gn5cXCKxuy%2BHdFSuxMEca8pfMGW1cdYM3d6eec6E2zEnnujA3i1vue3Zab5VL3TUNc4tK3Cfpfer7VLPm%2FZD4Rn339KgF05RR86SMREQ09qsoHS%2BR2UwyjtjBBmPO0KJubujQ6HXnWTYwGtUtAOnIHJI%2FYFQvH2Wo567nK2AugSYSCdOjtFJ6fhULxoF4cRKy3yc2MEBqB8j7jg2mDcoZxg0IEsxXn7dOllMUci6ngrqjUsGIb1zJu3j2PDpwUq1rpVKl4FLlPY8VlCsijh1GkutkSQhngCvNNFyU4ZSHtIa4dMJPR8LwGOqUBIUtBj%2BlgrpUL76DG0%2BBwhp%2B%2BbZV1K91yEvmIBJLqkb7%2Bkc%2F0%2F%2FnskFV1GMfxG6P4bfd2IUJ6fUxargg0%2Bijk0Xhg0u8hF1TF0VDfcQ%2Bfb0St%2Fz%2F3wlA2iogdI9fbnPnVjFoacVObzffYNdsqDEoBSWDN7LbfiIscz4uHtBr86zveqxtckAvpN4IQSyVG5%2BZav2Ne5pqFxVCyZDKS1km361xDq8jS&X-Amz-Signature=08814720d7b2e7dfe8963743d4ffa6a9e5cd3c230e9e63d31ee32b8443c6d62b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DZFFD4E%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9mFdleP1d%2FIcgtiU8MbWGwGWzckE6V0cJQMDzTSkfcAiAXKvenaNpORE5sJxkWwvpO84O7mNjNxjJ4Up3XcBN7QCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtkGk2uNO%2FFpyN4o2KtwD2u99q%2FVRDgRLZZWsUemheqk%2BJzzhsH87VI0fLBLCXFfFlf2%2FYcIgMnbMhH7najzz84EHiSDPddmcUdTCIrr9HBYSZk2VU0xdni3QrHfp4DHqLIF1DsSTVQ8gE3%2FLbKcOMKregPPWc9sqNTB6vt0Q%2BjWsrLwFU4h4Ux1fqP0qKUztLUgpctpSwdxFQC8KQHtq%2BPdlUNqMcXkYZw%2BBDXwQ2F0NrIjn%2B8yOfjZ%2F9HM5mdUGaPe1e5Lm0Di%2BWOpSzcQC6xripnUcFkmcn%2FWZWjgma2sUNUPoUWWywR7yxBjTx87OcvdGv5gu1BID26KcE836WXcMDdxNSZCNibsRSS9GoPN7gsFDZCo8N%2BNsktDKr11IQ1D4t56%2Fq1Gy%2BoG6gVFFZs6UAP2A%2B5ctyCXL8AmCECIFBOSkvAzNV91yrxQZjUQEGYo1CXtWt%2BdnJ5%2F4pGDYJdbuCCT7Auj35TOyEl9fylv%2BUvDcHc74kHvv4U1Ih2V2EpJIYMBoDAqT5Lr6%2Fp5XQFHCLUnBNi3pmuwaPeYaDqfb1CSlFDUdOo5s6P4si3zf8n%2Bc6b6%2FI1%2Fxb8dSkQRoqFRptPwTD2z64NiqSdzo91p1mtsAbxfbBRGqNCtKhLKH0nckYgQClxwIWVowh9DwvAY6pgFcWVXGTTESsKPfA9cQMYj0HMNUBcMp%2FRyFf9EG6kwLSxAFAnDeKyDht8aCw5H1zxxAEwspA7i5HY8TyaFWZEtS6l4hO2rJCMjY5d58ETlYVNRNAC4BffQwYXXHgbUUbPmI8M1raE5KpRIp1QmUtKS7AoJNqet3PVyXYFymWPrnhg2yTjLhI04nJoVBXulianAzgK08KcTqYW0rFxJFQubAyDS6K8R6&X-Amz-Signature=2d71b45991eae97adb73473dcd43a46a30db03f3de631260a051274d790bee1e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTX4NJD2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAStrnEW8c3NslA9zDgWFA6160jHKQRz8y27qutfaO9OAiA689l2OrTBpTeTugdw9%2FNPQhMkUBsiaaL8gZFpYI2hXCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnw1mS73jEZCNXpOHKtwDpnRMAXAEnYEiYAGNXQbEaFQz1PuNlhCHiQb865qEipQ9BusKwCzvwEDoKNDWLwoHd6ndjOp%2BfT9wEna12S1CIZkEYSCzTQGcMwFa%2Fi%2BB2QsVU1%2Bw295Y1beFBV3xN74jtbl2yO9Uvmj07IuZnAC4tJvRviVYhEa4M4wzmVRYghk3FbPrkiHwVsNFH%2BNcars9mAsFsUL3pSfVIdzEya3MN6GmKKBK%2BE1qQOpC87gMumT8ZixZq%2BTj76J6LKeDvoCDHdspEceiGrN01MXZ%2B9TIgVDz8uzR0onUxpeEzgxMpo8%2F2hFc8M3lgPPfvZmj3v39yiC1pyvF3d0aHQUSNa5Olgfa5ZQc9FN%2FES5E4%2FSPLc9i%2BtAQDHj4FpxVuROPUvVG0K3Dsk7a0QnP3xTzVWywwJcWMddEmLvHNOTNGb9prh28uD4htdYqCLgsQNNQpWlGQdawOg1pJi2MKdGL8vs0uKCqE2EyPDlVuwv4puSHNEAqkuOh4qAuGz%2FdPeNbUMF6Iunoy8UQCTIU6tlAhjKwxSm4KFBzdHNnmb2ZC1N2%2FpKgjBNI6ZrSPuJI8%2B6pGkMgpv2Olr%2B8YcF%2B6I2iglBrIlYplWWOsHhAlYIimEkhpEmeR%2BXCLmTI3EmtO08wkdDwvAY6pgGTF%2BpVTQlcz39TKVcTWY5ZpO%2F9c0gwOihMZUOWokH0EYcI3AGdmjqRhdUNGqG0KUOUVYqftaZXrl5n8XRANSeZn0n%2FJUP6btLn1JZXhnfxmCo%2B6cWQwIlUE5bmXjv9vykH8krfD43XLOJtY4dlF6sut%2BrHNVFWAPi%2BznFGpbx2chPSWLChTBPxpuIoTbqH0zSK49tTwYTRAhbiAx2wmOUisRGl8JA6&X-Amz-Signature=ce8d5067d92339b74b0670f6d948f49180f86a7f91c6abac7114893fc000e521&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PVPSXL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIXRKwxBsMyraFcuFL3YeZjkZNQhMbJPQnbBSiQdHTmAiAPcWzuCKYqTj5OJ0tiLuPJWd%2BtQa3%2FFoLdgTTWK8r9eyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7m28vUYnoEUN3RhBKtwD65eYwQr9InnLs9PTsDdUlZ7a46HP5VgncEpl83D8dzGj5eQD%2F%2Fzgez5sP4mz%2FZU5yzMzNH5v6j3rleOzhvy6iVXecRQBLGZuZT4fJkFsVaiJ9QD5xrKkkUdk4tHFMDjaxK7x%2FEGygMh1iASqrxSd8WBp7RcdqjzU7SlEBt4NISYK6rE7t%2FT4cdU5GueKwsk%2BI%2BST%2BWSNtcH5RehvuFv7HnpKmPpF9nqT965RPKp1nDIjc1c3pCAKLuufFJclq20p%2BOl9CD4zZOeN9d8mzvhJ5LYv2cWSDHOrpERcNtKA%2FFmxJhfWrNFWi%2FYuxtFGOt%2BH6XOtC2VSF9nujUlAfxzugtFDBrzXALN9vVz76jjHS8FhfBAa5Sag87fOqlUs42cOvBS55QxABeYIS76AIiIEP7yWKJ41nPX0RvO0PHc0oYV2iAFyKLh%2FpyzYupj6s6%2BOByuc7IMr5RViXbIUK3rosRbZx4skMhmg53EyMVZaRuyeVUqE6NIyEhH3Ll3FrCPvsurh%2B7TD6mU184%2B5yb3CZnd6t3mpcpxPDykXMqS1lATdX38wsvSsclr162ndyO%2Bu00dBNOQTb4Anyd1QpaFP%2BWcVj7ojtk7haJ9zyHFatpIB4EHC%2FQgFnWv2wUIwiNDwvAY6pgGVqxyS%2FhdvYDgrkyqFhe4wfPRhhmtV3XdK%2FjmsoISdtXusSNTjPujCQUYxBcOIzvXSJdE2GQ8A9c1I2UbNYKPFdicBZPEaY4sNixBJnYQC9wbmSFI%2BHd4ewN2k6YABMDfnoFxlL6t9zvdasr7bffAphlW%2Bgp3pIScbq3f0%2F73YH%2FuZKNQG9bFZq3VmCuq%2BuivSd0%2Fo0iZeO377pgys9cF0%2B2jAuKKd&X-Amz-Signature=f6e6ffbb71492cc3bf1a33dc178bdea310608a0dd46ed882b1565a5aa2a8005c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PVPSXL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIXRKwxBsMyraFcuFL3YeZjkZNQhMbJPQnbBSiQdHTmAiAPcWzuCKYqTj5OJ0tiLuPJWd%2BtQa3%2FFoLdgTTWK8r9eyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7m28vUYnoEUN3RhBKtwD65eYwQr9InnLs9PTsDdUlZ7a46HP5VgncEpl83D8dzGj5eQD%2F%2Fzgez5sP4mz%2FZU5yzMzNH5v6j3rleOzhvy6iVXecRQBLGZuZT4fJkFsVaiJ9QD5xrKkkUdk4tHFMDjaxK7x%2FEGygMh1iASqrxSd8WBp7RcdqjzU7SlEBt4NISYK6rE7t%2FT4cdU5GueKwsk%2BI%2BST%2BWSNtcH5RehvuFv7HnpKmPpF9nqT965RPKp1nDIjc1c3pCAKLuufFJclq20p%2BOl9CD4zZOeN9d8mzvhJ5LYv2cWSDHOrpERcNtKA%2FFmxJhfWrNFWi%2FYuxtFGOt%2BH6XOtC2VSF9nujUlAfxzugtFDBrzXALN9vVz76jjHS8FhfBAa5Sag87fOqlUs42cOvBS55QxABeYIS76AIiIEP7yWKJ41nPX0RvO0PHc0oYV2iAFyKLh%2FpyzYupj6s6%2BOByuc7IMr5RViXbIUK3rosRbZx4skMhmg53EyMVZaRuyeVUqE6NIyEhH3Ll3FrCPvsurh%2B7TD6mU184%2B5yb3CZnd6t3mpcpxPDykXMqS1lATdX38wsvSsclr162ndyO%2Bu00dBNOQTb4Anyd1QpaFP%2BWcVj7ojtk7haJ9zyHFatpIB4EHC%2FQgFnWv2wUIwiNDwvAY6pgGVqxyS%2FhdvYDgrkyqFhe4wfPRhhmtV3XdK%2FjmsoISdtXusSNTjPujCQUYxBcOIzvXSJdE2GQ8A9c1I2UbNYKPFdicBZPEaY4sNixBJnYQC9wbmSFI%2BHd4ewN2k6YABMDfnoFxlL6t9zvdasr7bffAphlW%2Bgp3pIScbq3f0%2F73YH%2FuZKNQG9bFZq3VmCuq%2BuivSd0%2Fo0iZeO377pgys9cF0%2B2jAuKKd&X-Amz-Signature=7b16eba171e8ddc2009ff1ebf248e30d1123d33b66241ebb5bb4c208c9423ff4&X-Amz-SignedHeaders=host&x-id=GetObject)

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
