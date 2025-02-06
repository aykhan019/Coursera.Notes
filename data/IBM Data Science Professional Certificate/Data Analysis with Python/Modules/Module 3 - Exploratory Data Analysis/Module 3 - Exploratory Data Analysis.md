

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z37VLEXQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIH%2FFtKnbHFSyMu5e6vTwZVzQk1lI2Qktq1pPkWZsf6PXAiEAwHmII3G6XLgQPXfnEuqfxXmdusxhlU6QifuoX7ubInYq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDFu%2BLaclgQQqZF43tyrcA9ywpMdL4pN1mQi5W4ejzHBf0fJ5V%2BNvBH19pDm5GIuB4c9U%2BxL%2Ff1Q9X38TrU9WYpEQ4NRCrjP8kcBI19xC%2FnPnWIsmhT9SoC9614hXjVFSvHVHSl2YDFPZB3iFFDrEUHtoiKNp%2FoqGA0i1ruigw04dVy2pufFyzlgpEul%2Bu0HZlCTsyAzwoUdpq3si0w0rEvC46Pms4lhkX0vy8NfoCjFLg9%2FcaE%2BLEcfb53h5YHthPCpO74o1S7mSnE4nQxWCmbfsonCnTR4nVVnVGljC9%2Fx%2BVU2t6nptIIQ8Gp8nNiW0O95OeqBBEF8OxhDYf%2B7F7UK2N96LZOxGi%2F9zZs09OwD4iUIq8FFxoc4jwWTdFacxEy%2FUix1XHNGc0IG6bl9WBTZ%2FqP5OhJ4e0evOBgsLL05mJwTyPKcfQirprQ1adqyx9NAje9nd7alwLWHlCpaWFQmtrXF9ZpXtBq8Sjz4Lwh64Be2J69iYY%2B%2BSL4FaXMzpxK%2B8b2kiezkd9AcOWIBy7dHAZVXQpHxYLpm8Nnr113I80Izk0%2FrPBD8bFgLIwvRPgVeLJufSCMVKm%2BNQ5KSbJXcQtyZ2rGHpW9ZCPoUQBjVsBPl0nNVinhNNCCVXxFw9uX9I6ANiLPIgW5xfMPLqj70GOqUBBFxvjiK5UCZAREIm1dz%2BJhgauOXpDDTVooif7Akx%2BcGc%2F6LOWEIn3u%2FhH%2BhGfHC6iXOQIwidCMOuvAjcHtafur76%2Fx5Dq23WNq50P%2FHEuzxB1kacVTrnbjHs0u3WM7pLX3nq5dG8xlQgHXr37K5F%2FW%2Fczj4fTMfk7uyCRCgbcixs4SWwGAJqfw5H2a0O6vmoZDH6zM3nmZNIqY4P12XKiC942NZu&X-Amz-Signature=c56b7df30e8f61674178203364d3d0bf924d051ac5040db836e8be3465c61616&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z37VLEXQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIH%2FFtKnbHFSyMu5e6vTwZVzQk1lI2Qktq1pPkWZsf6PXAiEAwHmII3G6XLgQPXfnEuqfxXmdusxhlU6QifuoX7ubInYq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDFu%2BLaclgQQqZF43tyrcA9ywpMdL4pN1mQi5W4ejzHBf0fJ5V%2BNvBH19pDm5GIuB4c9U%2BxL%2Ff1Q9X38TrU9WYpEQ4NRCrjP8kcBI19xC%2FnPnWIsmhT9SoC9614hXjVFSvHVHSl2YDFPZB3iFFDrEUHtoiKNp%2FoqGA0i1ruigw04dVy2pufFyzlgpEul%2Bu0HZlCTsyAzwoUdpq3si0w0rEvC46Pms4lhkX0vy8NfoCjFLg9%2FcaE%2BLEcfb53h5YHthPCpO74o1S7mSnE4nQxWCmbfsonCnTR4nVVnVGljC9%2Fx%2BVU2t6nptIIQ8Gp8nNiW0O95OeqBBEF8OxhDYf%2B7F7UK2N96LZOxGi%2F9zZs09OwD4iUIq8FFxoc4jwWTdFacxEy%2FUix1XHNGc0IG6bl9WBTZ%2FqP5OhJ4e0evOBgsLL05mJwTyPKcfQirprQ1adqyx9NAje9nd7alwLWHlCpaWFQmtrXF9ZpXtBq8Sjz4Lwh64Be2J69iYY%2B%2BSL4FaXMzpxK%2B8b2kiezkd9AcOWIBy7dHAZVXQpHxYLpm8Nnr113I80Izk0%2FrPBD8bFgLIwvRPgVeLJufSCMVKm%2BNQ5KSbJXcQtyZ2rGHpW9ZCPoUQBjVsBPl0nNVinhNNCCVXxFw9uX9I6ANiLPIgW5xfMPLqj70GOqUBBFxvjiK5UCZAREIm1dz%2BJhgauOXpDDTVooif7Akx%2BcGc%2F6LOWEIn3u%2FhH%2BhGfHC6iXOQIwidCMOuvAjcHtafur76%2Fx5Dq23WNq50P%2FHEuzxB1kacVTrnbjHs0u3WM7pLX3nq5dG8xlQgHXr37K5F%2FW%2Fczj4fTMfk7uyCRCgbcixs4SWwGAJqfw5H2a0O6vmoZDH6zM3nmZNIqY4P12XKiC942NZu&X-Amz-Signature=f49b5aafb4d15f5ccda53777a83af230d8bafc5330378fbe827947b291bf47ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z37VLEXQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIH%2FFtKnbHFSyMu5e6vTwZVzQk1lI2Qktq1pPkWZsf6PXAiEAwHmII3G6XLgQPXfnEuqfxXmdusxhlU6QifuoX7ubInYq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDFu%2BLaclgQQqZF43tyrcA9ywpMdL4pN1mQi5W4ejzHBf0fJ5V%2BNvBH19pDm5GIuB4c9U%2BxL%2Ff1Q9X38TrU9WYpEQ4NRCrjP8kcBI19xC%2FnPnWIsmhT9SoC9614hXjVFSvHVHSl2YDFPZB3iFFDrEUHtoiKNp%2FoqGA0i1ruigw04dVy2pufFyzlgpEul%2Bu0HZlCTsyAzwoUdpq3si0w0rEvC46Pms4lhkX0vy8NfoCjFLg9%2FcaE%2BLEcfb53h5YHthPCpO74o1S7mSnE4nQxWCmbfsonCnTR4nVVnVGljC9%2Fx%2BVU2t6nptIIQ8Gp8nNiW0O95OeqBBEF8OxhDYf%2B7F7UK2N96LZOxGi%2F9zZs09OwD4iUIq8FFxoc4jwWTdFacxEy%2FUix1XHNGc0IG6bl9WBTZ%2FqP5OhJ4e0evOBgsLL05mJwTyPKcfQirprQ1adqyx9NAje9nd7alwLWHlCpaWFQmtrXF9ZpXtBq8Sjz4Lwh64Be2J69iYY%2B%2BSL4FaXMzpxK%2B8b2kiezkd9AcOWIBy7dHAZVXQpHxYLpm8Nnr113I80Izk0%2FrPBD8bFgLIwvRPgVeLJufSCMVKm%2BNQ5KSbJXcQtyZ2rGHpW9ZCPoUQBjVsBPl0nNVinhNNCCVXxFw9uX9I6ANiLPIgW5xfMPLqj70GOqUBBFxvjiK5UCZAREIm1dz%2BJhgauOXpDDTVooif7Akx%2BcGc%2F6LOWEIn3u%2FhH%2BhGfHC6iXOQIwidCMOuvAjcHtafur76%2Fx5Dq23WNq50P%2FHEuzxB1kacVTrnbjHs0u3WM7pLX3nq5dG8xlQgHXr37K5F%2FW%2Fczj4fTMfk7uyCRCgbcixs4SWwGAJqfw5H2a0O6vmoZDH6zM3nmZNIqY4P12XKiC942NZu&X-Amz-Signature=318d37008ce5d35521abe7f4a66888abd9b7b00c3c4b38e205f00a21ec7f1f3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUX62OGL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD2ap6o9T0pApij%2BvGoIbYMt%2F9ICKpXM%2FnoTno1MgH1JgIhAJVNe4xV5e87IO8AllZZHw1l1qhFlsf964Qd%2BNqT6qq5Kv8DCFEQABoMNjM3NDIzMTgzODA1IgyFXmFGoE1GqebPDG4q3AN33QYWVIzKFakTWOg1m28IRtZYvLX8E2z4ETBNKWCEhwp203BXuekdGtgVA8g%2FmLtQZ6rfYQWKYZ%2FoFaWivRY9xVXj67c3z%2B0OR94IKpYlzcA2Xn92THHBiiokrSOhjawLXZcPCnPyy8QBd3tdj7mREgrf6ebWB%2BSbgNucLCupHl52jgn67g1Gkf0RVVzwjyTtVe3rqr1PA6bEb5r%2BLapMvTWktENHnSwsyS7z0mFhRXnBnyJleZ7NIEuFP0D%2F2KxJ8sCacFuE9C6MAFl29Iw3vSI5oZZtRBoll1cQxRDp2Sm0oBY9yAMEV7OYR3sdoV89T7bLlX3erYz8D2Rf5vn0Mz5tmjbnYFfLWM1cCOzq6SGJ25RSin9DyN%2FdGpQNEsHdZd2KP404WPQXlhVRZPQ8Ox1wB5i8Y4XOqWGjDYVPDAW0oTvaJMsasxmKya6XIaDMuE2wlpKJMa0UpAnoZtExLo2zOA%2FQZMQ67VGanOgPUU0UveQ5YsLzE6VLAUcucaKR%2BprUQkt%2Ff4Uqk5DrvJ5pajLnN3QbppM6D7T961wGsR97nncur1nW0sPAnE%2FKiqFFrAAqSLuk0pzwnMP9w7e%2F99yWR2wAyjFbmSO10jKm2mLskoqTJWseUPIv4DDU6o%2B9BjqkAZED6iF2q3r8HGih8RdCP9tq6qyZYxS4FMsNmi41fKJLoFEVaNVBmykorINoR8EelDchner9%2FBrXns9SekPRSrj50G00Ae1TjD4EdL7g4b%2BcodfQwYmZs9yY%2BXdoHBUGfSbazrdFh%2FoPwVc4IR1kfWt6TZzFB2I0%2BiMtrluRCrGMGJQ1NJxHqd%2FwaiT%2FthYqHimXpJwVRyUaRcOZsWl02%2B%2BdZztG&X-Amz-Signature=df7992265959e1eeb3a1ebfeafe0f60a54f24897da769349bef1cd8c17c24823&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUX62OGL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD2ap6o9T0pApij%2BvGoIbYMt%2F9ICKpXM%2FnoTno1MgH1JgIhAJVNe4xV5e87IO8AllZZHw1l1qhFlsf964Qd%2BNqT6qq5Kv8DCFEQABoMNjM3NDIzMTgzODA1IgyFXmFGoE1GqebPDG4q3AN33QYWVIzKFakTWOg1m28IRtZYvLX8E2z4ETBNKWCEhwp203BXuekdGtgVA8g%2FmLtQZ6rfYQWKYZ%2FoFaWivRY9xVXj67c3z%2B0OR94IKpYlzcA2Xn92THHBiiokrSOhjawLXZcPCnPyy8QBd3tdj7mREgrf6ebWB%2BSbgNucLCupHl52jgn67g1Gkf0RVVzwjyTtVe3rqr1PA6bEb5r%2BLapMvTWktENHnSwsyS7z0mFhRXnBnyJleZ7NIEuFP0D%2F2KxJ8sCacFuE9C6MAFl29Iw3vSI5oZZtRBoll1cQxRDp2Sm0oBY9yAMEV7OYR3sdoV89T7bLlX3erYz8D2Rf5vn0Mz5tmjbnYFfLWM1cCOzq6SGJ25RSin9DyN%2FdGpQNEsHdZd2KP404WPQXlhVRZPQ8Ox1wB5i8Y4XOqWGjDYVPDAW0oTvaJMsasxmKya6XIaDMuE2wlpKJMa0UpAnoZtExLo2zOA%2FQZMQ67VGanOgPUU0UveQ5YsLzE6VLAUcucaKR%2BprUQkt%2Ff4Uqk5DrvJ5pajLnN3QbppM6D7T961wGsR97nncur1nW0sPAnE%2FKiqFFrAAqSLuk0pzwnMP9w7e%2F99yWR2wAyjFbmSO10jKm2mLskoqTJWseUPIv4DDU6o%2B9BjqkAZED6iF2q3r8HGih8RdCP9tq6qyZYxS4FMsNmi41fKJLoFEVaNVBmykorINoR8EelDchner9%2FBrXns9SekPRSrj50G00Ae1TjD4EdL7g4b%2BcodfQwYmZs9yY%2BXdoHBUGfSbazrdFh%2FoPwVc4IR1kfWt6TZzFB2I0%2BiMtrluRCrGMGJQ1NJxHqd%2FwaiT%2FthYqHimXpJwVRyUaRcOZsWl02%2B%2BdZztG&X-Amz-Signature=f81e34d2f23c18aafd1eefe625bbe2e2869f64c3989b99951ea455f0a8f24cc1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUX62OGL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD2ap6o9T0pApij%2BvGoIbYMt%2F9ICKpXM%2FnoTno1MgH1JgIhAJVNe4xV5e87IO8AllZZHw1l1qhFlsf964Qd%2BNqT6qq5Kv8DCFEQABoMNjM3NDIzMTgzODA1IgyFXmFGoE1GqebPDG4q3AN33QYWVIzKFakTWOg1m28IRtZYvLX8E2z4ETBNKWCEhwp203BXuekdGtgVA8g%2FmLtQZ6rfYQWKYZ%2FoFaWivRY9xVXj67c3z%2B0OR94IKpYlzcA2Xn92THHBiiokrSOhjawLXZcPCnPyy8QBd3tdj7mREgrf6ebWB%2BSbgNucLCupHl52jgn67g1Gkf0RVVzwjyTtVe3rqr1PA6bEb5r%2BLapMvTWktENHnSwsyS7z0mFhRXnBnyJleZ7NIEuFP0D%2F2KxJ8sCacFuE9C6MAFl29Iw3vSI5oZZtRBoll1cQxRDp2Sm0oBY9yAMEV7OYR3sdoV89T7bLlX3erYz8D2Rf5vn0Mz5tmjbnYFfLWM1cCOzq6SGJ25RSin9DyN%2FdGpQNEsHdZd2KP404WPQXlhVRZPQ8Ox1wB5i8Y4XOqWGjDYVPDAW0oTvaJMsasxmKya6XIaDMuE2wlpKJMa0UpAnoZtExLo2zOA%2FQZMQ67VGanOgPUU0UveQ5YsLzE6VLAUcucaKR%2BprUQkt%2Ff4Uqk5DrvJ5pajLnN3QbppM6D7T961wGsR97nncur1nW0sPAnE%2FKiqFFrAAqSLuk0pzwnMP9w7e%2F99yWR2wAyjFbmSO10jKm2mLskoqTJWseUPIv4DDU6o%2B9BjqkAZED6iF2q3r8HGih8RdCP9tq6qyZYxS4FMsNmi41fKJLoFEVaNVBmykorINoR8EelDchner9%2FBrXns9SekPRSrj50G00Ae1TjD4EdL7g4b%2BcodfQwYmZs9yY%2BXdoHBUGfSbazrdFh%2FoPwVc4IR1kfWt6TZzFB2I0%2BiMtrluRCrGMGJQ1NJxHqd%2FwaiT%2FthYqHimXpJwVRyUaRcOZsWl02%2B%2BdZztG&X-Amz-Signature=e57148a4362c889f1e50e583222a866de1352c90f71178cd609891b850761f5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUX62OGL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD2ap6o9T0pApij%2BvGoIbYMt%2F9ICKpXM%2FnoTno1MgH1JgIhAJVNe4xV5e87IO8AllZZHw1l1qhFlsf964Qd%2BNqT6qq5Kv8DCFEQABoMNjM3NDIzMTgzODA1IgyFXmFGoE1GqebPDG4q3AN33QYWVIzKFakTWOg1m28IRtZYvLX8E2z4ETBNKWCEhwp203BXuekdGtgVA8g%2FmLtQZ6rfYQWKYZ%2FoFaWivRY9xVXj67c3z%2B0OR94IKpYlzcA2Xn92THHBiiokrSOhjawLXZcPCnPyy8QBd3tdj7mREgrf6ebWB%2BSbgNucLCupHl52jgn67g1Gkf0RVVzwjyTtVe3rqr1PA6bEb5r%2BLapMvTWktENHnSwsyS7z0mFhRXnBnyJleZ7NIEuFP0D%2F2KxJ8sCacFuE9C6MAFl29Iw3vSI5oZZtRBoll1cQxRDp2Sm0oBY9yAMEV7OYR3sdoV89T7bLlX3erYz8D2Rf5vn0Mz5tmjbnYFfLWM1cCOzq6SGJ25RSin9DyN%2FdGpQNEsHdZd2KP404WPQXlhVRZPQ8Ox1wB5i8Y4XOqWGjDYVPDAW0oTvaJMsasxmKya6XIaDMuE2wlpKJMa0UpAnoZtExLo2zOA%2FQZMQ67VGanOgPUU0UveQ5YsLzE6VLAUcucaKR%2BprUQkt%2Ff4Uqk5DrvJ5pajLnN3QbppM6D7T961wGsR97nncur1nW0sPAnE%2FKiqFFrAAqSLuk0pzwnMP9w7e%2F99yWR2wAyjFbmSO10jKm2mLskoqTJWseUPIv4DDU6o%2B9BjqkAZED6iF2q3r8HGih8RdCP9tq6qyZYxS4FMsNmi41fKJLoFEVaNVBmykorINoR8EelDchner9%2FBrXns9SekPRSrj50G00Ae1TjD4EdL7g4b%2BcodfQwYmZs9yY%2BXdoHBUGfSbazrdFh%2FoPwVc4IR1kfWt6TZzFB2I0%2BiMtrluRCrGMGJQ1NJxHqd%2FwaiT%2FthYqHimXpJwVRyUaRcOZsWl02%2B%2BdZztG&X-Amz-Signature=9735463d497c1e77f9d7a5a27c06f2aed82cd8da38733b7baa0a98376d8b7639&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUX62OGL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD2ap6o9T0pApij%2BvGoIbYMt%2F9ICKpXM%2FnoTno1MgH1JgIhAJVNe4xV5e87IO8AllZZHw1l1qhFlsf964Qd%2BNqT6qq5Kv8DCFEQABoMNjM3NDIzMTgzODA1IgyFXmFGoE1GqebPDG4q3AN33QYWVIzKFakTWOg1m28IRtZYvLX8E2z4ETBNKWCEhwp203BXuekdGtgVA8g%2FmLtQZ6rfYQWKYZ%2FoFaWivRY9xVXj67c3z%2B0OR94IKpYlzcA2Xn92THHBiiokrSOhjawLXZcPCnPyy8QBd3tdj7mREgrf6ebWB%2BSbgNucLCupHl52jgn67g1Gkf0RVVzwjyTtVe3rqr1PA6bEb5r%2BLapMvTWktENHnSwsyS7z0mFhRXnBnyJleZ7NIEuFP0D%2F2KxJ8sCacFuE9C6MAFl29Iw3vSI5oZZtRBoll1cQxRDp2Sm0oBY9yAMEV7OYR3sdoV89T7bLlX3erYz8D2Rf5vn0Mz5tmjbnYFfLWM1cCOzq6SGJ25RSin9DyN%2FdGpQNEsHdZd2KP404WPQXlhVRZPQ8Ox1wB5i8Y4XOqWGjDYVPDAW0oTvaJMsasxmKya6XIaDMuE2wlpKJMa0UpAnoZtExLo2zOA%2FQZMQ67VGanOgPUU0UveQ5YsLzE6VLAUcucaKR%2BprUQkt%2Ff4Uqk5DrvJ5pajLnN3QbppM6D7T961wGsR97nncur1nW0sPAnE%2FKiqFFrAAqSLuk0pzwnMP9w7e%2F99yWR2wAyjFbmSO10jKm2mLskoqTJWseUPIv4DDU6o%2B9BjqkAZED6iF2q3r8HGih8RdCP9tq6qyZYxS4FMsNmi41fKJLoFEVaNVBmykorINoR8EelDchner9%2FBrXns9SekPRSrj50G00Ae1TjD4EdL7g4b%2BcodfQwYmZs9yY%2BXdoHBUGfSbazrdFh%2FoPwVc4IR1kfWt6TZzFB2I0%2BiMtrluRCrGMGJQ1NJxHqd%2FwaiT%2FthYqHimXpJwVRyUaRcOZsWl02%2B%2BdZztG&X-Amz-Signature=eefeb5fb4dcbe36f92d6efddf9daff6646b35ec7afcc46cefacfb5bf216f6e0a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUX62OGL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD2ap6o9T0pApij%2BvGoIbYMt%2F9ICKpXM%2FnoTno1MgH1JgIhAJVNe4xV5e87IO8AllZZHw1l1qhFlsf964Qd%2BNqT6qq5Kv8DCFEQABoMNjM3NDIzMTgzODA1IgyFXmFGoE1GqebPDG4q3AN33QYWVIzKFakTWOg1m28IRtZYvLX8E2z4ETBNKWCEhwp203BXuekdGtgVA8g%2FmLtQZ6rfYQWKYZ%2FoFaWivRY9xVXj67c3z%2B0OR94IKpYlzcA2Xn92THHBiiokrSOhjawLXZcPCnPyy8QBd3tdj7mREgrf6ebWB%2BSbgNucLCupHl52jgn67g1Gkf0RVVzwjyTtVe3rqr1PA6bEb5r%2BLapMvTWktENHnSwsyS7z0mFhRXnBnyJleZ7NIEuFP0D%2F2KxJ8sCacFuE9C6MAFl29Iw3vSI5oZZtRBoll1cQxRDp2Sm0oBY9yAMEV7OYR3sdoV89T7bLlX3erYz8D2Rf5vn0Mz5tmjbnYFfLWM1cCOzq6SGJ25RSin9DyN%2FdGpQNEsHdZd2KP404WPQXlhVRZPQ8Ox1wB5i8Y4XOqWGjDYVPDAW0oTvaJMsasxmKya6XIaDMuE2wlpKJMa0UpAnoZtExLo2zOA%2FQZMQ67VGanOgPUU0UveQ5YsLzE6VLAUcucaKR%2BprUQkt%2Ff4Uqk5DrvJ5pajLnN3QbppM6D7T961wGsR97nncur1nW0sPAnE%2FKiqFFrAAqSLuk0pzwnMP9w7e%2F99yWR2wAyjFbmSO10jKm2mLskoqTJWseUPIv4DDU6o%2B9BjqkAZED6iF2q3r8HGih8RdCP9tq6qyZYxS4FMsNmi41fKJLoFEVaNVBmykorINoR8EelDchner9%2FBrXns9SekPRSrj50G00Ae1TjD4EdL7g4b%2BcodfQwYmZs9yY%2BXdoHBUGfSbazrdFh%2FoPwVc4IR1kfWt6TZzFB2I0%2BiMtrluRCrGMGJQ1NJxHqd%2FwaiT%2FthYqHimXpJwVRyUaRcOZsWl02%2B%2BdZztG&X-Amz-Signature=1f2e7c0134217ec33102a4f0f0aaf56eb1c218f4bd45f0fe9b3e5675abefc11c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JRWEZH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAsrCNEw2sytmS2%2BdQ%2B9s6gNe9mJysT5PvYFd%2B%2ByYoGqAiEAimo9S2nEQItJsXJfxFXFmxh3Rsy1%2F5QHGF6D5Yrlgqgq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDBsBjlq0JVPOtWY2DSrcAyLkL1L9gnciAOZXgJIsl1Apw8XPK%2F1Vv610zFSNcV44Bg6Ed%2BrOQuIluyNLrHAIPkKulZIjjPsuIIbSpIm%2F%2FioYZ%2B%2FKeboiSm%2Fo0KAEV5hY1zatatAzentXyF7crWhcoGdJa06WUl%2B2XmtSIIFd30Kf09zmq7VqX5YXzULp%2FcV%2FoIRxFf2LroYBAPC9Hs2MFo%2BawdUX18nUSuzvpMTpa%2BU%2F33nlY19uICFaMEbVy52QmHaJkq7wSjab1GWay%2BwkjRh5h5AjpaC4Jbj82YWgc%2FyGYvIOm2BA6FEUf2TWytcNDdkKncie%2BjWRGmW8VjcGnBbh0rgpdHMg8nYOsdUFyDaUH668%2FbWlrHJfg3AY1PeiHZRkC9Cx6uSUIeu0q8GpIZ9vQXuwF8L48bYQBMjoXPvVmxKNpAXjb%2BfUzy%2BzE49LYFxrNcDhfsA%2FrhRZysREpwW5EN60VxevvLIhJeWtC2nn5MeFXzb%2BIWrI7q5JmD%2BzXQj9zckV3Xb%2BEMYbEFWZfsXqaLKAtzsYunNRRNCG0fmZiE6%2FA%2BYetEn%2Fomp4667k2joTNFoL%2FQNrlrV2rB3IplOPD72pa445njSOscesxG%2Fj8Dk8iSgTEn%2BE8aF61f20K5mcDR7keU8GDb8JMKDrj70GOqUBy3skJaxJDH2bwjEfV%2FBbJoLTN5djXh2yoKTMpFmEUaOjlTomG4fH%2BJn12ovGuzWT0Yv7FfL4fQgSVHRhjyab7mRHopnvfE6T0Y3euIZh2vXAxBotp0wfYBJjuas2opOi1vTBIjxQrzB9FKf2HHs7fkLMEwZGEMpnWHoGqONCuv0BZAa%2FOAzFPQQb%2Bi9yMd%2BRbcHD%2BBU1WNUs%2Fd7t9SEAt1RLfbKP&X-Amz-Signature=b986084f31612628b0aa534c6c5aebe636d34b91c0a75ec3f5c58cadaed6e0e9&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R232ZC4Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGdmGmN%2FAidmWJvI23hs%2FsEi1%2Bcw8Yxoq5bMcuY39kIPAiBc0oyf9OSQdeC9T8Rduq2ORoe%2BSm9JFHzZSHV8WY%2FK1yr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMAw0eMIW0bX7rNZr0KtwD6EcFwDOljEljNZTajudIZVW0xkVkX%2FjWoqUVO6BVZ8ArrHGGcSchLrLzQxhUwupH6co9B0O2kSmKHkpy1uo0uwAgLf3L%2FTEq8dzEQ1C7jQvTb19Vpakc57reiEDiHqHd8qNXy48MOMCY8qPk9SLd8dHk7Gys9Wo%2FUNel2kuWUuyCwVMhKjw3jfeEY37Hu8kRhv6MackIbf5kykeXazk0ClAdEkTuE8OHg46d%2FnFxpVtWBpqerxm0VKklb626yt2jrHeWnIRG%2BiFwTQ3J91L1eR%2Bl%2F%2BcgVIzlGaPwLwrs2SAud35%2Fa6cY4D468okBLEP8t2t2aEGLVGOcmOeyax5xubLtg6RGK6Y2RiEuVl8AS41wERfxj%2FSTBwv1WPwVqkBfgI4KMjBi3XSEAM578cOwFuvnHt7mg%2BUNmYkB14qAopT%2FIDNVTabdNEsW8fCm0XO4%2BFmR6oRezmPkToQXoUzjzS1cXRLkbb4l4ibrz3RV5mwFJvQPGxkZtUzwT6ObtoJrZZSV7Vjn9sfXIFNb4P5zbBBHtVvgHg%2F27M%2BBpMy9vdNMVC8hFyP7tEkUMz%2FMqWd6eA0bHmCj5v0AWFWBTFa6E3q7pjqwnQ9e5eafinD%2BTUgnucBt3AiWK2FxE%2FkwpuuPvQY6pgGNaTxNnNAoNT0VGxderSXcEvaAMmOFxdsP%2FEqF1d%2B7SsKdr9y1iPI5IghfhsGva3P5TaNMDi5YhMkmtccvADF5MYIj%2BUnoQk2kdFEkzh3o6G1WgdgMh4qjqsPUf8WyqtFhgRvzeG%2BiYQKxNxVv6c9NarLky%2FAG8OZAh88%2BzZdEB6i14KgRFSFQr3QNCDdX%2B7D%2FmtViKO17s3XWa8mf6TGza1Ds09G7&X-Amz-Signature=677843dda5b0fdcfe4cb05de75626b0ad4361809a389e64dcc192a926732a2e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUX62OGL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD2ap6o9T0pApij%2BvGoIbYMt%2F9ICKpXM%2FnoTno1MgH1JgIhAJVNe4xV5e87IO8AllZZHw1l1qhFlsf964Qd%2BNqT6qq5Kv8DCFEQABoMNjM3NDIzMTgzODA1IgyFXmFGoE1GqebPDG4q3AN33QYWVIzKFakTWOg1m28IRtZYvLX8E2z4ETBNKWCEhwp203BXuekdGtgVA8g%2FmLtQZ6rfYQWKYZ%2FoFaWivRY9xVXj67c3z%2B0OR94IKpYlzcA2Xn92THHBiiokrSOhjawLXZcPCnPyy8QBd3tdj7mREgrf6ebWB%2BSbgNucLCupHl52jgn67g1Gkf0RVVzwjyTtVe3rqr1PA6bEb5r%2BLapMvTWktENHnSwsyS7z0mFhRXnBnyJleZ7NIEuFP0D%2F2KxJ8sCacFuE9C6MAFl29Iw3vSI5oZZtRBoll1cQxRDp2Sm0oBY9yAMEV7OYR3sdoV89T7bLlX3erYz8D2Rf5vn0Mz5tmjbnYFfLWM1cCOzq6SGJ25RSin9DyN%2FdGpQNEsHdZd2KP404WPQXlhVRZPQ8Ox1wB5i8Y4XOqWGjDYVPDAW0oTvaJMsasxmKya6XIaDMuE2wlpKJMa0UpAnoZtExLo2zOA%2FQZMQ67VGanOgPUU0UveQ5YsLzE6VLAUcucaKR%2BprUQkt%2Ff4Uqk5DrvJ5pajLnN3QbppM6D7T961wGsR97nncur1nW0sPAnE%2FKiqFFrAAqSLuk0pzwnMP9w7e%2F99yWR2wAyjFbmSO10jKm2mLskoqTJWseUPIv4DDU6o%2B9BjqkAZED6iF2q3r8HGih8RdCP9tq6qyZYxS4FMsNmi41fKJLoFEVaNVBmykorINoR8EelDchner9%2FBrXns9SekPRSrj50G00Ae1TjD4EdL7g4b%2BcodfQwYmZs9yY%2BXdoHBUGfSbazrdFh%2FoPwVc4IR1kfWt6TZzFB2I0%2BiMtrluRCrGMGJQ1NJxHqd%2FwaiT%2FthYqHimXpJwVRyUaRcOZsWl02%2B%2BdZztG&X-Amz-Signature=0d7225b4f3903a546b9188288c2dfc72271a05a0eca3c7b1cfec39dcb3e7e2a6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUX62OGL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD2ap6o9T0pApij%2BvGoIbYMt%2F9ICKpXM%2FnoTno1MgH1JgIhAJVNe4xV5e87IO8AllZZHw1l1qhFlsf964Qd%2BNqT6qq5Kv8DCFEQABoMNjM3NDIzMTgzODA1IgyFXmFGoE1GqebPDG4q3AN33QYWVIzKFakTWOg1m28IRtZYvLX8E2z4ETBNKWCEhwp203BXuekdGtgVA8g%2FmLtQZ6rfYQWKYZ%2FoFaWivRY9xVXj67c3z%2B0OR94IKpYlzcA2Xn92THHBiiokrSOhjawLXZcPCnPyy8QBd3tdj7mREgrf6ebWB%2BSbgNucLCupHl52jgn67g1Gkf0RVVzwjyTtVe3rqr1PA6bEb5r%2BLapMvTWktENHnSwsyS7z0mFhRXnBnyJleZ7NIEuFP0D%2F2KxJ8sCacFuE9C6MAFl29Iw3vSI5oZZtRBoll1cQxRDp2Sm0oBY9yAMEV7OYR3sdoV89T7bLlX3erYz8D2Rf5vn0Mz5tmjbnYFfLWM1cCOzq6SGJ25RSin9DyN%2FdGpQNEsHdZd2KP404WPQXlhVRZPQ8Ox1wB5i8Y4XOqWGjDYVPDAW0oTvaJMsasxmKya6XIaDMuE2wlpKJMa0UpAnoZtExLo2zOA%2FQZMQ67VGanOgPUU0UveQ5YsLzE6VLAUcucaKR%2BprUQkt%2Ff4Uqk5DrvJ5pajLnN3QbppM6D7T961wGsR97nncur1nW0sPAnE%2FKiqFFrAAqSLuk0pzwnMP9w7e%2F99yWR2wAyjFbmSO10jKm2mLskoqTJWseUPIv4DDU6o%2B9BjqkAZED6iF2q3r8HGih8RdCP9tq6qyZYxS4FMsNmi41fKJLoFEVaNVBmykorINoR8EelDchner9%2FBrXns9SekPRSrj50G00Ae1TjD4EdL7g4b%2BcodfQwYmZs9yY%2BXdoHBUGfSbazrdFh%2FoPwVc4IR1kfWt6TZzFB2I0%2BiMtrluRCrGMGJQ1NJxHqd%2FwaiT%2FthYqHimXpJwVRyUaRcOZsWl02%2B%2BdZztG&X-Amz-Signature=d110ef3cc38e162b0659cd426a5dfc71544f521c6ad5486868464bd0d5da9f9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUX62OGL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQD2ap6o9T0pApij%2BvGoIbYMt%2F9ICKpXM%2FnoTno1MgH1JgIhAJVNe4xV5e87IO8AllZZHw1l1qhFlsf964Qd%2BNqT6qq5Kv8DCFEQABoMNjM3NDIzMTgzODA1IgyFXmFGoE1GqebPDG4q3AN33QYWVIzKFakTWOg1m28IRtZYvLX8E2z4ETBNKWCEhwp203BXuekdGtgVA8g%2FmLtQZ6rfYQWKYZ%2FoFaWivRY9xVXj67c3z%2B0OR94IKpYlzcA2Xn92THHBiiokrSOhjawLXZcPCnPyy8QBd3tdj7mREgrf6ebWB%2BSbgNucLCupHl52jgn67g1Gkf0RVVzwjyTtVe3rqr1PA6bEb5r%2BLapMvTWktENHnSwsyS7z0mFhRXnBnyJleZ7NIEuFP0D%2F2KxJ8sCacFuE9C6MAFl29Iw3vSI5oZZtRBoll1cQxRDp2Sm0oBY9yAMEV7OYR3sdoV89T7bLlX3erYz8D2Rf5vn0Mz5tmjbnYFfLWM1cCOzq6SGJ25RSin9DyN%2FdGpQNEsHdZd2KP404WPQXlhVRZPQ8Ox1wB5i8Y4XOqWGjDYVPDAW0oTvaJMsasxmKya6XIaDMuE2wlpKJMa0UpAnoZtExLo2zOA%2FQZMQ67VGanOgPUU0UveQ5YsLzE6VLAUcucaKR%2BprUQkt%2Ff4Uqk5DrvJ5pajLnN3QbppM6D7T961wGsR97nncur1nW0sPAnE%2FKiqFFrAAqSLuk0pzwnMP9w7e%2F99yWR2wAyjFbmSO10jKm2mLskoqTJWseUPIv4DDU6o%2B9BjqkAZED6iF2q3r8HGih8RdCP9tq6qyZYxS4FMsNmi41fKJLoFEVaNVBmykorINoR8EelDchner9%2FBrXns9SekPRSrj50G00Ae1TjD4EdL7g4b%2BcodfQwYmZs9yY%2BXdoHBUGfSbazrdFh%2FoPwVc4IR1kfWt6TZzFB2I0%2BiMtrluRCrGMGJQ1NJxHqd%2FwaiT%2FthYqHimXpJwVRyUaRcOZsWl02%2B%2BdZztG&X-Amz-Signature=fe5a7168639acd70d566f5e3e8c002a85e6d6c1b179c2871845154b54adf3389&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AS3CPDP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBoNd8bXynNtdq1YrL8vY4lvudrdrEqOxhb3FJrc5ZQEAiEAx7DCv%2BTzZ63fd9RbbFQwYU45uG7U7Pi3iIxwKXkHyEoq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDLM4S9ZXTIhHTOJc5ircA1A6R9DmQWEOltAW3nJ1qSbQ%2BqZe7t511FJQa%2F5cywis28w8lLVrwgjSTgut0W4OP2LeQ55i4Sfg8%2B1IBpnaavd13wuS9jTcnxaEXDtrvcU6kl5mVh%2B22Vm5xCX3GzEyJ7bOB3Svrt3%2Fpd4ggZdyROahI3UpEp4VMKuCyB%2Bso17KA8peX%2FcOODpoTBnoKMBspzLhl%2BA24xPg%2BkoTVpukwmVenO3HPr5vi1hs0fqms8ixQGfCViikBDSBlTPZ8%2F%2F0EJdSL9Pq9NV5jZIKICbIL6PhxrbO2xxxz0vj30XZRNTsigueqvPmXm%2B6di6FnHh6as69ztaZVsiMhSWZFkQCQXm9MzOr1sRI3BmrQ0oKlnFB%2BsL1xFhhe%2BoVMB82kkkCOBlpgTaFg3BpDVquUnjiOiUgZ%2FesWZIW23jU1Wks%2BWSufgHW8jP6%2Bz2hgz%2FTEkzkNkg3os3FJqG3oBlLc1EHGIX6ev%2FzZ5DHOqkV0ZK20Aad7O9i6qg6LhvsIxT1xlvg3XS5xODNAs67%2BMNzkErbAmp71nlEMQE2MYqU0eEAkiGsTu3osNGmYFkF60wTtdCCcnZWDSJ6kCGSTAQI%2F%2BfXJgwehGt6NZb5MZKJR09LOla1ZDHCBXk469KLw2OiMPHqj70GOqUBKFXtkAzUMOBU9symTrNSHHzKFU92YEtzUH3MUJx%2FcCzBRfjwBx3wLFtknv27wCW99nSXJYnGn4%2B92BZj5Um6OnmWaNxCW5jLRdCGoQ207JvLK376%2BT0pz5x6DeYVPJHu7Jxb%2FsBpJ9XFH1UoEAZ0ETuPd7fzZWm9fWcUYwil4dbV7RxeTJsXyG4VINyTeX7rEfazwcSnFP1k4GTKGfMU4ce9BMOb&X-Amz-Signature=266322df1dbd7d3159701d75841a48ed361831a63c2657e0497e71618ecba503&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664F4OVTEX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCICM08Z%2BQDz065Rtn0O4SRrKwvF5QI%2F2XISNbGg49DRWlAiAKyQFq5kSgVmEe%2B3wGB2eZU0cp1wIQMVW9DAEmDgJM8ir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMF3vgMJuRiUu4B3m2KtwDMJpm2z%2BTGWqp%2FvXP7LR63jyczLzeCrnCsh9jf4a136zEfA3hWTyHn%2F8ltoy4v97HET1KzcPqjDp9%2BnykmI3nJvzaQI%2FyYcSme9VVWwiB9%2B6f3LHmdPpVtOt41phpuE6ssumrO2jGwcSqa42dnhxbzmSWvS0ULTTsHdUAvCCodpEDwRsBkrgHJ2MhPtFuBmeSbGnST3X9wvrO5XrxK%2FGS84GlPAPnpTujLc3wZdVSICIb5NLv7X6ErlR%2FHlw6SjpWrBIG0AXjZa4ItaJYbciLlADi0ZwsGEsTscf8KbVa6bxzDqn1mSeIZ8MrIp14KzIsWk40m4ICXriJnquotTzt5Vh0F3Sh40FP8hh744IC4bWi4bUWjG7eEFwLZgVhAx1D42BqqFjK9f3%2FWPfxnl4no2a8BIobXAOym1dxYDTJHgZkZGY7F%2F80CsNn1PnWfRwbnQ2Ap%2BRbjVU%2FdXeepxt5FRr4tkPIhJC4UFWOra2aaSQ8CDN1U09DZuxb0%2BDmZU19MfWOxxsTQ1puBO3GesHNFD3QWXYxXWLSlWKOJ0OEyzbWLAM4dw4N914aCkgngoUVh07qYWqlJ39yvqQeCqqwjc4RbVM779%2F9gsUIHWY0XgvY00TFm8VmKFdk850w%2FOqPvQY6pgHHCzJs3SdIYSCxsKIO8aaIgm78MzbaWZQ6vycmW6W%2FQgAI5WGb%2BEmC4vOo9LUVnFjdEb%2Fl03Wu2kBk9%2Fr26l0Aq634397cCnUai71ww0Bhdqeh3gtdHkynSa4LoR2f1B%2BzGwI0uABTTthJHN1GtrqkmGSHuqevcT1fdC9aWvzWBkwxqNxwX91xNEhpwj8M8WYqOcUXYdhrxD%2FF6VyUa0bjmO9tSL32&X-Amz-Signature=0bf8107f961c42b072edcaf57d1433a6e031b40691e570ce51c287854d74fa7e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCNW7NE6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIH9rAQaY4Fn1xJ6H5Xh%2BJSTplAcfYTV5JKrKIE%2Fmc5boAiEAz5MgSlf8R6g%2F88VQ%2Fl5HqK0%2F5fV4dxrDtmHlYlQ8Ttcq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDG2Ffc4dNXj5CfyzRircA%2FGSHEwqlnfgxCWQ4hfcwcNn4WJ024opW3gI7AObx0XZ5Q4QYOAlpvf1ipqVVVQwl4lkJTLGQMeTqyWoEGtvMTEtFQDlOPE99zZ5KXaO%2Bp1WUoQIGNkF4iTTYNszXEmIKIAawLUsGaJfIV4qy3SI8FHrxqfx2LJ9b2BO%2FdN43GOco0IrzpC4LJ5LD%2BJ0LOhtD9dp%2FP0a8ICNRdvqbBwCt1CzrTmeAw0SL7SRuVZHdiO77TU4EY4uqwtkdAqLGHSKiQ%2FoQC3VTVcgYN%2Ftm8Nsc%2Bj8ZztG6iuSSP%2BTQG7QRUZZskj%2B8uQK0%2B1vakLM4ft2eNpkcLy9QKQWsAHvb0USW2DyEKpv1MsUJTWE%2F9dNe%2BZ3F5C0rov1P3AuI5cXA3ije6tk73PVQ9cFv4mXm9BsXYeKPPvsd9oYAL9hrwHreU05A1nhpe28HGmsoiTqHvfDnPn9hv3xT5i4Zt%2FOe1MQGnkfuEGpZ%2BQG4gfcb7fczYfoFqMwL8qkizLDsKdW6%2B5TY685ZczYnhan5dc6v9EZoWbujoXdM8vRwVEfC2OaBZ0dkTGhZYXaTseQWS7YGT4kBD5nj5siYsrETW0UEt5pxlAYJhuvUT0%2B8LIJGTNJGr%2BYC%2BmlTdtVtUd1uWYdMIbrj70GOqUBfPeMUeIZj8OtMX7OiwaqOJUYUerCz2ZYacVJ4PauybT2exPHepUWELIjC3ccx3HQUA%2FSWpDIEfokN2wxfPPaNeZVA%2FPqtFGsXx2rd3udjAvoOQAQpxFVYqrxxsVBAn%2FK4x6jWaFeKVU%2F4jlrItacAH%2FK0lifi%2BuqOp3UoMOCluQY2Vh8VCergeWJQgO5MYcrm4m3scJJzC7mRoN3FhOShVZ3Evkk&X-Amz-Signature=031ee0b6f0aac50558d89766084391add9f3775b3367ae6b52c51ed533932dd2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4WB7XAQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDYwKEn6NnmzDfvxD15yVbYros9IdoyREXDQlkR%2FaEO8AIhAKy%2BBipLEmjNEkp%2FCDe%2BksjRtllaX1AazJPTheUqfqw3Kv8DCFEQABoMNjM3NDIzMTgzODA1IgwLBueAR686FVjrp4oq3AOpH9NH94j1gH%2FKAnhhSVONny9cs%2Fz1%2FwgIuwTpie6heNBhojUjxd6vOgfLb%2BA7FHqdJM1cAMcRh2yn1SkMakPghXVkavX5I0QtjMhw0%2Fak5BQB2OKlH3skS53AcAn3ynYqdPDWuuMXNyOuINpJgpG8o0mpOUd7%2FIKNmBgpD64bJq6R1r%2Fg4Fiu3UiguC8tkUH4IF2e4qtNRR%2BiS39I42xOEhwbe6LmSlkWqKBqHAbdvLCNeIE8DZ%2F9w8nws7BtISSZU1uQn2ZRVmZIe3uuHQ5%2BnkJ8DC5H4OygFm3Q9ffdBbN3n3p09rbr20OuJnc4WT3EtqwLbNdgNHoEek6wAEsdITidvH0QySXIHNMWhkbWeYKRyIIG3zkaEMYYFaP20HMkhBtF9td8Fw4AIeWZEdHN4%2F49bSMwoQKpjakOM9dyDGN%2B3GEJ8%2FAg8QI0HOkeCKQ5dNct0hUNZln%2BeQOkyARhFNo7%2BMhjl8wx4YRbBw2TEdLlAQNeuSZXkKK5v%2FmEtmxRfhEu6f1Rkj%2Bv%2FzN2o3ZdzC5GjFwt%2FCzljDH%2B5aNAMad3A7M5xELn%2BBDcpuGXePGtMuB4VPruPJWYlXITQ3QS6jpJgpKszwiATXTHUE0gXjYFcXc3c%2FOqSI%2FOfjDy6o%2B9BjqkAYMu7yGTJz5T91Y4z072M2vcPw3BDgIRRCfm%2F8e83Pb58grG%2FyWWGk%2FpG5UEO%2FWIH6YmUx020n50Ln6tcRqBcnexrO%2B8%2FlVbkQ%2FRzwSs3ZRo%2B9cZ0QTErj1e7PeRuQ1zeOf4DK2mOxC0R12oCWmKL7JY1sREU1KibpIMwPDt3fDraK00ASFKQ8CQPgSBpy70jOgTAJzUlDq0nYQXDem%2BlHkHyZeO&X-Amz-Signature=98ec2cf027bda407a1dc85ec5c21e7fd629ab97d7876ec232fe855631ed2ebb5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4WB7XAQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDYwKEn6NnmzDfvxD15yVbYros9IdoyREXDQlkR%2FaEO8AIhAKy%2BBipLEmjNEkp%2FCDe%2BksjRtllaX1AazJPTheUqfqw3Kv8DCFEQABoMNjM3NDIzMTgzODA1IgwLBueAR686FVjrp4oq3AOpH9NH94j1gH%2FKAnhhSVONny9cs%2Fz1%2FwgIuwTpie6heNBhojUjxd6vOgfLb%2BA7FHqdJM1cAMcRh2yn1SkMakPghXVkavX5I0QtjMhw0%2Fak5BQB2OKlH3skS53AcAn3ynYqdPDWuuMXNyOuINpJgpG8o0mpOUd7%2FIKNmBgpD64bJq6R1r%2Fg4Fiu3UiguC8tkUH4IF2e4qtNRR%2BiS39I42xOEhwbe6LmSlkWqKBqHAbdvLCNeIE8DZ%2F9w8nws7BtISSZU1uQn2ZRVmZIe3uuHQ5%2BnkJ8DC5H4OygFm3Q9ffdBbN3n3p09rbr20OuJnc4WT3EtqwLbNdgNHoEek6wAEsdITidvH0QySXIHNMWhkbWeYKRyIIG3zkaEMYYFaP20HMkhBtF9td8Fw4AIeWZEdHN4%2F49bSMwoQKpjakOM9dyDGN%2B3GEJ8%2FAg8QI0HOkeCKQ5dNct0hUNZln%2BeQOkyARhFNo7%2BMhjl8wx4YRbBw2TEdLlAQNeuSZXkKK5v%2FmEtmxRfhEu6f1Rkj%2Bv%2FzN2o3ZdzC5GjFwt%2FCzljDH%2B5aNAMad3A7M5xELn%2BBDcpuGXePGtMuB4VPruPJWYlXITQ3QS6jpJgpKszwiATXTHUE0gXjYFcXc3c%2FOqSI%2FOfjDy6o%2B9BjqkAYMu7yGTJz5T91Y4z072M2vcPw3BDgIRRCfm%2F8e83Pb58grG%2FyWWGk%2FpG5UEO%2FWIH6YmUx020n50Ln6tcRqBcnexrO%2B8%2FlVbkQ%2FRzwSs3ZRo%2B9cZ0QTErj1e7PeRuQ1zeOf4DK2mOxC0R12oCWmKL7JY1sREU1KibpIMwPDt3fDraK00ASFKQ8CQPgSBpy70jOgTAJzUlDq0nYQXDem%2BlHkHyZeO&X-Amz-Signature=2ee2894aea9b0889e81d564ea87ae576354739fc3fecdcc513f07ea38743000c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
