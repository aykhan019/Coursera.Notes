

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBGPEMPD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCICVuDCmfhzs1TSw23UvgcKDxEW%2BUrbVit9yQS4hX9WLbAiBz1LRCiF5fjhMQePbjfYwuqoeG68x72ZV5SyWPD9kx%2Bir%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMOQ6sGn4zfpRveKNIKtwDel66gscJcrGtPVOLtkmDn6qaf%2FvFZP6MBtRYPRo2gDQqxor2o052MjCyXJUYb9VNkXMKqlDRDF9XXfWyQiTX6PGnqk7NdIix1Z06u623YSrfVXOBLp4MTG%2BpGxXmtKOYlCWVA%2F3aFY0w22sbbNLBXiloUzkVYD6Ii5FNQ5qWLRrLwVFXYvBiv%2BvYyS3NynxB08KrVr0J9%2FqVOxgtTI7UPjY9HdN5tahnBj3%2F%2Bal3wDfpL5EFtC8EMfXvXWxHnKgGu%2FlspDtYpUGSkozoTcHnDzhP6eW7hSFzcGQw0M9VeciBlwvI9gtXqgj%2FJCoak4vtuQJul3n%2BUfBAWf5qoNw9hG9KsFOksREmfr0SBTpLFH1R0tcgrFoFVV8jAVqaSbU0XOHfil11w1Me2QGaiSvjDKZGxD%2FO2hA9lSGxxsv2CCQqFx2SkJj1qLzqhqr4ecrifw5qoIPe62WsLhEaF0eSddnmdeqDiR19Y8u0u%2Biu3Yycy2SBYcmV3%2BkJYyFxRvefaf2ccPDqOKRP5aunim%2FT8vmw3%2FnA%2Be7gYFZJ74XtjyzJnRrxnDkUxVYrQA1yPeDhmzZYboJD0B5czVgwwx9YjrxtViMjRFmE8v4sAIksccA4qoIGYdMTwmGgzjgwzOONvQY6pgF05z5stnKDTn2K%2F5qeYGkRWf47rJ4bZCOMnCVnJ8xvydL2YCqvOrMOeF71iYmnoGCbR4aWwy2VTAFi3uGHatUBSmJ6E3wrWqGE0UlZLmijMFRU8W4vBAIGwH9jM5O7G2q%2BDYh09K89pRwMCb3eT4Y4kwMhjpjbz7VZsw%2BKugyRbxAFM9IeeXEbR0D1n2WZWsA%2BQiEYs6SaVu5NysvPBiguDxaCPWn8&X-Amz-Signature=67bffaee0e9caea1a87590ae2e45e61805350a22599e741a6443d626e307c9e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBGPEMPD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCICVuDCmfhzs1TSw23UvgcKDxEW%2BUrbVit9yQS4hX9WLbAiBz1LRCiF5fjhMQePbjfYwuqoeG68x72ZV5SyWPD9kx%2Bir%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMOQ6sGn4zfpRveKNIKtwDel66gscJcrGtPVOLtkmDn6qaf%2FvFZP6MBtRYPRo2gDQqxor2o052MjCyXJUYb9VNkXMKqlDRDF9XXfWyQiTX6PGnqk7NdIix1Z06u623YSrfVXOBLp4MTG%2BpGxXmtKOYlCWVA%2F3aFY0w22sbbNLBXiloUzkVYD6Ii5FNQ5qWLRrLwVFXYvBiv%2BvYyS3NynxB08KrVr0J9%2FqVOxgtTI7UPjY9HdN5tahnBj3%2F%2Bal3wDfpL5EFtC8EMfXvXWxHnKgGu%2FlspDtYpUGSkozoTcHnDzhP6eW7hSFzcGQw0M9VeciBlwvI9gtXqgj%2FJCoak4vtuQJul3n%2BUfBAWf5qoNw9hG9KsFOksREmfr0SBTpLFH1R0tcgrFoFVV8jAVqaSbU0XOHfil11w1Me2QGaiSvjDKZGxD%2FO2hA9lSGxxsv2CCQqFx2SkJj1qLzqhqr4ecrifw5qoIPe62WsLhEaF0eSddnmdeqDiR19Y8u0u%2Biu3Yycy2SBYcmV3%2BkJYyFxRvefaf2ccPDqOKRP5aunim%2FT8vmw3%2FnA%2Be7gYFZJ74XtjyzJnRrxnDkUxVYrQA1yPeDhmzZYboJD0B5czVgwwx9YjrxtViMjRFmE8v4sAIksccA4qoIGYdMTwmGgzjgwzOONvQY6pgF05z5stnKDTn2K%2F5qeYGkRWf47rJ4bZCOMnCVnJ8xvydL2YCqvOrMOeF71iYmnoGCbR4aWwy2VTAFi3uGHatUBSmJ6E3wrWqGE0UlZLmijMFRU8W4vBAIGwH9jM5O7G2q%2BDYh09K89pRwMCb3eT4Y4kwMhjpjbz7VZsw%2BKugyRbxAFM9IeeXEbR0D1n2WZWsA%2BQiEYs6SaVu5NysvPBiguDxaCPWn8&X-Amz-Signature=74fcf9209047df3f77d9d5cb3bb78db68a637cbd8c7f11b8625c9a8291870624&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBGPEMPD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCICVuDCmfhzs1TSw23UvgcKDxEW%2BUrbVit9yQS4hX9WLbAiBz1LRCiF5fjhMQePbjfYwuqoeG68x72ZV5SyWPD9kx%2Bir%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMOQ6sGn4zfpRveKNIKtwDel66gscJcrGtPVOLtkmDn6qaf%2FvFZP6MBtRYPRo2gDQqxor2o052MjCyXJUYb9VNkXMKqlDRDF9XXfWyQiTX6PGnqk7NdIix1Z06u623YSrfVXOBLp4MTG%2BpGxXmtKOYlCWVA%2F3aFY0w22sbbNLBXiloUzkVYD6Ii5FNQ5qWLRrLwVFXYvBiv%2BvYyS3NynxB08KrVr0J9%2FqVOxgtTI7UPjY9HdN5tahnBj3%2F%2Bal3wDfpL5EFtC8EMfXvXWxHnKgGu%2FlspDtYpUGSkozoTcHnDzhP6eW7hSFzcGQw0M9VeciBlwvI9gtXqgj%2FJCoak4vtuQJul3n%2BUfBAWf5qoNw9hG9KsFOksREmfr0SBTpLFH1R0tcgrFoFVV8jAVqaSbU0XOHfil11w1Me2QGaiSvjDKZGxD%2FO2hA9lSGxxsv2CCQqFx2SkJj1qLzqhqr4ecrifw5qoIPe62WsLhEaF0eSddnmdeqDiR19Y8u0u%2Biu3Yycy2SBYcmV3%2BkJYyFxRvefaf2ccPDqOKRP5aunim%2FT8vmw3%2FnA%2Be7gYFZJ74XtjyzJnRrxnDkUxVYrQA1yPeDhmzZYboJD0B5czVgwwx9YjrxtViMjRFmE8v4sAIksccA4qoIGYdMTwmGgzjgwzOONvQY6pgF05z5stnKDTn2K%2F5qeYGkRWf47rJ4bZCOMnCVnJ8xvydL2YCqvOrMOeF71iYmnoGCbR4aWwy2VTAFi3uGHatUBSmJ6E3wrWqGE0UlZLmijMFRU8W4vBAIGwH9jM5O7G2q%2BDYh09K89pRwMCb3eT4Y4kwMhjpjbz7VZsw%2BKugyRbxAFM9IeeXEbR0D1n2WZWsA%2BQiEYs6SaVu5NysvPBiguDxaCPWn8&X-Amz-Signature=9510472b49944649b44248284f3c61e6d7e4917cf3bcd2223ecae2b3639f5aa7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IU2KHM2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIHRl7vizigTHQKps5dCJUoagIg0heEH2SwQk792FKtwzAiBGaWiq4B5Z8eus38HpzHAgOuIuIVd9nh5K4Wq54b4xwyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIM8cVyN581XUj0yKieKtwDAbmNimrXTf2lBsGyQo1MV6M7ytX8zmRvpVS%2Bolqv0yZXAXdO54Az4%2Bndr5c8zB%2BIABSgXa0DNsn%2FOLK7zHPeZKnO0wtdqrUOWLZc1je6C2rgGJEP0IM8GjgJ3vgMcYbW1bYpXqHMne8Mfb7AHQuLDRRHDrj%2F5EbQgfaERRjSGXU6EhvLf9Fr2jnII%2FRmYFRgBlcMrRDaMX2myAkiZWuS9h6b971w1StwfGTtEFCvtBS6r9bkusKJg75rcnrGFxtS7%2FBhXVJH6%2FDfcQPRmdyDWBZZonv4Zu614iqiUNqUMvjZdZIkob28pzHZfIv6lKfXDQjtKLa5gW%2BkPSariV3oHPWShawmedHqglOEhoRPXTstSxHbI1hxbHrvtEApmwnO0wu%2Fc5DEoF8Era4H3uNqPFShxmbPcDtC4ixkjv%2FFvT9UYYc5wCb2AxvRXhMi7kvPeep0d9cqngB8LUWytos0Z4mlMvhdtcVcwMH13G7mJXjD1Ky3lpWvRtEU2kdUU53I6nrDWKt6mF87Y0TZcmkk9HDnggXKkPS9SBl1mlnEe2sCBMx6vjCw5cMzsCwBFK8PDUc%2B45LjjsWSAY7xc%2FNDcIlk0yCwHimXqrW1nblxMX%2BARqwgRoyn6SpST94wxOONvQY6pgHjDJsO3QN%2B4QG%2FpPfuCr4DQ3uf7ZDKz10TkcS01MHs8JPl%2FNvLw95zPEUBEDs43Ytl33ud0TlrK07zXW51QjJ3hKKbym0Nz75BOxjffh92E8XlVpHF7VKZhR9jbKaDsg4yORjY%2FWOTIolRWVeWN%2FaJ8JqxA2yILp9ZIg5gM%2BjPXk%2B%2B7cYLBxvyKEKzuuV7MG4tWLbLeFWGRfGaovtsqEmeNU5xEqly&X-Amz-Signature=e9d31053b5a7d99b3a294b2ce2844f35e5b18e1ad8145d8f7f647b6a73b77a53&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IU2KHM2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIHRl7vizigTHQKps5dCJUoagIg0heEH2SwQk792FKtwzAiBGaWiq4B5Z8eus38HpzHAgOuIuIVd9nh5K4Wq54b4xwyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIM8cVyN581XUj0yKieKtwDAbmNimrXTf2lBsGyQo1MV6M7ytX8zmRvpVS%2Bolqv0yZXAXdO54Az4%2Bndr5c8zB%2BIABSgXa0DNsn%2FOLK7zHPeZKnO0wtdqrUOWLZc1je6C2rgGJEP0IM8GjgJ3vgMcYbW1bYpXqHMne8Mfb7AHQuLDRRHDrj%2F5EbQgfaERRjSGXU6EhvLf9Fr2jnII%2FRmYFRgBlcMrRDaMX2myAkiZWuS9h6b971w1StwfGTtEFCvtBS6r9bkusKJg75rcnrGFxtS7%2FBhXVJH6%2FDfcQPRmdyDWBZZonv4Zu614iqiUNqUMvjZdZIkob28pzHZfIv6lKfXDQjtKLa5gW%2BkPSariV3oHPWShawmedHqglOEhoRPXTstSxHbI1hxbHrvtEApmwnO0wu%2Fc5DEoF8Era4H3uNqPFShxmbPcDtC4ixkjv%2FFvT9UYYc5wCb2AxvRXhMi7kvPeep0d9cqngB8LUWytos0Z4mlMvhdtcVcwMH13G7mJXjD1Ky3lpWvRtEU2kdUU53I6nrDWKt6mF87Y0TZcmkk9HDnggXKkPS9SBl1mlnEe2sCBMx6vjCw5cMzsCwBFK8PDUc%2B45LjjsWSAY7xc%2FNDcIlk0yCwHimXqrW1nblxMX%2BARqwgRoyn6SpST94wxOONvQY6pgHjDJsO3QN%2B4QG%2FpPfuCr4DQ3uf7ZDKz10TkcS01MHs8JPl%2FNvLw95zPEUBEDs43Ytl33ud0TlrK07zXW51QjJ3hKKbym0Nz75BOxjffh92E8XlVpHF7VKZhR9jbKaDsg4yORjY%2FWOTIolRWVeWN%2FaJ8JqxA2yILp9ZIg5gM%2BjPXk%2B%2B7cYLBxvyKEKzuuV7MG4tWLbLeFWGRfGaovtsqEmeNU5xEqly&X-Amz-Signature=02d13226140ce73950074ff2e68743a49d22eb2424574b662a12ce5c10ce544b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IU2KHM2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIHRl7vizigTHQKps5dCJUoagIg0heEH2SwQk792FKtwzAiBGaWiq4B5Z8eus38HpzHAgOuIuIVd9nh5K4Wq54b4xwyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIM8cVyN581XUj0yKieKtwDAbmNimrXTf2lBsGyQo1MV6M7ytX8zmRvpVS%2Bolqv0yZXAXdO54Az4%2Bndr5c8zB%2BIABSgXa0DNsn%2FOLK7zHPeZKnO0wtdqrUOWLZc1je6C2rgGJEP0IM8GjgJ3vgMcYbW1bYpXqHMne8Mfb7AHQuLDRRHDrj%2F5EbQgfaERRjSGXU6EhvLf9Fr2jnII%2FRmYFRgBlcMrRDaMX2myAkiZWuS9h6b971w1StwfGTtEFCvtBS6r9bkusKJg75rcnrGFxtS7%2FBhXVJH6%2FDfcQPRmdyDWBZZonv4Zu614iqiUNqUMvjZdZIkob28pzHZfIv6lKfXDQjtKLa5gW%2BkPSariV3oHPWShawmedHqglOEhoRPXTstSxHbI1hxbHrvtEApmwnO0wu%2Fc5DEoF8Era4H3uNqPFShxmbPcDtC4ixkjv%2FFvT9UYYc5wCb2AxvRXhMi7kvPeep0d9cqngB8LUWytos0Z4mlMvhdtcVcwMH13G7mJXjD1Ky3lpWvRtEU2kdUU53I6nrDWKt6mF87Y0TZcmkk9HDnggXKkPS9SBl1mlnEe2sCBMx6vjCw5cMzsCwBFK8PDUc%2B45LjjsWSAY7xc%2FNDcIlk0yCwHimXqrW1nblxMX%2BARqwgRoyn6SpST94wxOONvQY6pgHjDJsO3QN%2B4QG%2FpPfuCr4DQ3uf7ZDKz10TkcS01MHs8JPl%2FNvLw95zPEUBEDs43Ytl33ud0TlrK07zXW51QjJ3hKKbym0Nz75BOxjffh92E8XlVpHF7VKZhR9jbKaDsg4yORjY%2FWOTIolRWVeWN%2FaJ8JqxA2yILp9ZIg5gM%2BjPXk%2B%2B7cYLBxvyKEKzuuV7MG4tWLbLeFWGRfGaovtsqEmeNU5xEqly&X-Amz-Signature=9a7e5c2d9e5975c9f7fa59dffd871b8fb8f2d9be04364caa303ef7c82f7eb27b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IU2KHM2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIHRl7vizigTHQKps5dCJUoagIg0heEH2SwQk792FKtwzAiBGaWiq4B5Z8eus38HpzHAgOuIuIVd9nh5K4Wq54b4xwyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIM8cVyN581XUj0yKieKtwDAbmNimrXTf2lBsGyQo1MV6M7ytX8zmRvpVS%2Bolqv0yZXAXdO54Az4%2Bndr5c8zB%2BIABSgXa0DNsn%2FOLK7zHPeZKnO0wtdqrUOWLZc1je6C2rgGJEP0IM8GjgJ3vgMcYbW1bYpXqHMne8Mfb7AHQuLDRRHDrj%2F5EbQgfaERRjSGXU6EhvLf9Fr2jnII%2FRmYFRgBlcMrRDaMX2myAkiZWuS9h6b971w1StwfGTtEFCvtBS6r9bkusKJg75rcnrGFxtS7%2FBhXVJH6%2FDfcQPRmdyDWBZZonv4Zu614iqiUNqUMvjZdZIkob28pzHZfIv6lKfXDQjtKLa5gW%2BkPSariV3oHPWShawmedHqglOEhoRPXTstSxHbI1hxbHrvtEApmwnO0wu%2Fc5DEoF8Era4H3uNqPFShxmbPcDtC4ixkjv%2FFvT9UYYc5wCb2AxvRXhMi7kvPeep0d9cqngB8LUWytos0Z4mlMvhdtcVcwMH13G7mJXjD1Ky3lpWvRtEU2kdUU53I6nrDWKt6mF87Y0TZcmkk9HDnggXKkPS9SBl1mlnEe2sCBMx6vjCw5cMzsCwBFK8PDUc%2B45LjjsWSAY7xc%2FNDcIlk0yCwHimXqrW1nblxMX%2BARqwgRoyn6SpST94wxOONvQY6pgHjDJsO3QN%2B4QG%2FpPfuCr4DQ3uf7ZDKz10TkcS01MHs8JPl%2FNvLw95zPEUBEDs43Ytl33ud0TlrK07zXW51QjJ3hKKbym0Nz75BOxjffh92E8XlVpHF7VKZhR9jbKaDsg4yORjY%2FWOTIolRWVeWN%2FaJ8JqxA2yILp9ZIg5gM%2BjPXk%2B%2B7cYLBxvyKEKzuuV7MG4tWLbLeFWGRfGaovtsqEmeNU5xEqly&X-Amz-Signature=38fe80c60cd88533bd00099cb503620d18f8d40d4d312f2c0adea6fc0ef8eaaa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IU2KHM2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIHRl7vizigTHQKps5dCJUoagIg0heEH2SwQk792FKtwzAiBGaWiq4B5Z8eus38HpzHAgOuIuIVd9nh5K4Wq54b4xwyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIM8cVyN581XUj0yKieKtwDAbmNimrXTf2lBsGyQo1MV6M7ytX8zmRvpVS%2Bolqv0yZXAXdO54Az4%2Bndr5c8zB%2BIABSgXa0DNsn%2FOLK7zHPeZKnO0wtdqrUOWLZc1je6C2rgGJEP0IM8GjgJ3vgMcYbW1bYpXqHMne8Mfb7AHQuLDRRHDrj%2F5EbQgfaERRjSGXU6EhvLf9Fr2jnII%2FRmYFRgBlcMrRDaMX2myAkiZWuS9h6b971w1StwfGTtEFCvtBS6r9bkusKJg75rcnrGFxtS7%2FBhXVJH6%2FDfcQPRmdyDWBZZonv4Zu614iqiUNqUMvjZdZIkob28pzHZfIv6lKfXDQjtKLa5gW%2BkPSariV3oHPWShawmedHqglOEhoRPXTstSxHbI1hxbHrvtEApmwnO0wu%2Fc5DEoF8Era4H3uNqPFShxmbPcDtC4ixkjv%2FFvT9UYYc5wCb2AxvRXhMi7kvPeep0d9cqngB8LUWytos0Z4mlMvhdtcVcwMH13G7mJXjD1Ky3lpWvRtEU2kdUU53I6nrDWKt6mF87Y0TZcmkk9HDnggXKkPS9SBl1mlnEe2sCBMx6vjCw5cMzsCwBFK8PDUc%2B45LjjsWSAY7xc%2FNDcIlk0yCwHimXqrW1nblxMX%2BARqwgRoyn6SpST94wxOONvQY6pgHjDJsO3QN%2B4QG%2FpPfuCr4DQ3uf7ZDKz10TkcS01MHs8JPl%2FNvLw95zPEUBEDs43Ytl33ud0TlrK07zXW51QjJ3hKKbym0Nz75BOxjffh92E8XlVpHF7VKZhR9jbKaDsg4yORjY%2FWOTIolRWVeWN%2FaJ8JqxA2yILp9ZIg5gM%2BjPXk%2B%2B7cYLBxvyKEKzuuV7MG4tWLbLeFWGRfGaovtsqEmeNU5xEqly&X-Amz-Signature=7a2fdd0080f072215e645dcd354a792038deebbd1055f29c2fe2bbf44df21235&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IU2KHM2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIHRl7vizigTHQKps5dCJUoagIg0heEH2SwQk792FKtwzAiBGaWiq4B5Z8eus38HpzHAgOuIuIVd9nh5K4Wq54b4xwyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIM8cVyN581XUj0yKieKtwDAbmNimrXTf2lBsGyQo1MV6M7ytX8zmRvpVS%2Bolqv0yZXAXdO54Az4%2Bndr5c8zB%2BIABSgXa0DNsn%2FOLK7zHPeZKnO0wtdqrUOWLZc1je6C2rgGJEP0IM8GjgJ3vgMcYbW1bYpXqHMne8Mfb7AHQuLDRRHDrj%2F5EbQgfaERRjSGXU6EhvLf9Fr2jnII%2FRmYFRgBlcMrRDaMX2myAkiZWuS9h6b971w1StwfGTtEFCvtBS6r9bkusKJg75rcnrGFxtS7%2FBhXVJH6%2FDfcQPRmdyDWBZZonv4Zu614iqiUNqUMvjZdZIkob28pzHZfIv6lKfXDQjtKLa5gW%2BkPSariV3oHPWShawmedHqglOEhoRPXTstSxHbI1hxbHrvtEApmwnO0wu%2Fc5DEoF8Era4H3uNqPFShxmbPcDtC4ixkjv%2FFvT9UYYc5wCb2AxvRXhMi7kvPeep0d9cqngB8LUWytos0Z4mlMvhdtcVcwMH13G7mJXjD1Ky3lpWvRtEU2kdUU53I6nrDWKt6mF87Y0TZcmkk9HDnggXKkPS9SBl1mlnEe2sCBMx6vjCw5cMzsCwBFK8PDUc%2B45LjjsWSAY7xc%2FNDcIlk0yCwHimXqrW1nblxMX%2BARqwgRoyn6SpST94wxOONvQY6pgHjDJsO3QN%2B4QG%2FpPfuCr4DQ3uf7ZDKz10TkcS01MHs8JPl%2FNvLw95zPEUBEDs43Ytl33ud0TlrK07zXW51QjJ3hKKbym0Nz75BOxjffh92E8XlVpHF7VKZhR9jbKaDsg4yORjY%2FWOTIolRWVeWN%2FaJ8JqxA2yILp9ZIg5gM%2BjPXk%2B%2B7cYLBxvyKEKzuuV7MG4tWLbLeFWGRfGaovtsqEmeNU5xEqly&X-Amz-Signature=c239344396c04aa501a9ddab5ca72f07ffa639d88196bda5e72b1181394ecc75&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZF7WAN5Q%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCID6ZQ5wxZdt0cx3aJC%2F3IfW8HmKNRBOg71KfU1g3MdmfAiBizofBh5EcncBworA4y%2Bz9EidZVERyTAGIl4q06mCpXCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMYSWBYC8Kh6VUf1nnKtwDKuMpELTrLcMH8kpda%2BOk2jmcndalmt3%2BYFnXt%2BaN%2FtH34xGXRGtms3119emgYPj5M8R7qA5Ejgg6bKIK9aIlwtBDWhUjZDGEmvCWVlbUjTP%2FbVoSS1SfWyYULo1291sii4gjq7WHLgYZXkB8P6%2BXVJI928ZtWoyTJetzjz%2BHbgNlhIYcfAKGMCF9gXsejGT69GopfO0N2YVR7j0zStFASe%2FhWzEaM85n%2FUHjqF%2FFD1W31HyiSZddPby00bz8PwU0WwjTdxWqVbfhfKyd4h0gQqMoqPGHgQOCorqtKUph%2BdcYhtNv6Ddu58g5aIc3rlmeovR5H9%2FnlvpledpYVjgR1G0%2Fj%2F3YWBd4VPTL3oSfVB8MiamEb4EgJ1weQ0XrhqDtLmW%2BReWapyt7sg3XSaZpZ9EDp5oih4L95NFYJbp%2FxyJhRmXzo2MHCmjbirj2KNWh8NZZxs3ntxnJRLjjZJcGMEl6LxZZbVV4SOND%2FnFDKLDnNV7xa4XH6GmldzrwgUSPSf2xUTlr3BKNjyYP5cZW%2F12MoupBhd4a7V0ihl7dd0ZWfaFtF1zyCF87Sf2SNP%2FjNIEjLSxSYOzWAhkJEHz40nYAy2LF5zsAUIDHxMRK9pg43CTmWaresOjB7i4wy%2BONvQY6pgFCJNGYOlXAGlXf%2BOzMfVA%2F14AGyUFxQCj4u%2FyPnpiSTpTur%2FiV8DEjFvqqsblU7YSHdFyEW%2FeP0MU%2BxxTzpcMSBN%2FL60K%2BRJFLcJuqr3X%2FayhdMS7UnyBvtYL76mpNPyvfo9LAfRZ4RPLQuWWmXX7ZZGQI1gmmIrw9J6aBF7BcSgGfi2MmcMNm6z9KNlBbuKTy2puntBA1BGeT9MncsBBx9g8Es35T&X-Amz-Signature=a434e1f1b54b3bc6684246f182027bf857ab1c6a8385818b5f3d866a3adb5a29&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QE4EXO7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCt%2F%2FdQk2rHhpPrRiBNbcYyj9sM2wnvDlvLWun0GPXv8wIhAMlFkh%2B4njBGJ5Wsmfd7P7juOSBKYPCgyep1HDz5HkqxKv8DCEQQABoMNjM3NDIzMTgzODA1IgxZC7g2ArUtyYN8w28q3APD5HZ%2Fxtb4mjunDLDzglq0xghAjTXRei0RxfjfxpSqpp0zplIE9uHeUz2JTHifspeL9maG81VhPnJLvX%2FxDD40cFYwktJfxvb%2FuYamfTfDa5M%2BiJekmPMs3quKIcdCyBxe%2BvSiEuVNki1oBHrMcEhoEZXheAfncNz8wdGxPxCiotT3N1hneu%2BMrxSleGHdgGMJjRegCeJrKe%2FgHnDRyAGaomEpjHX7HoZI2vLQoT3jh2VK%2BegLUV7v%2Fgn8XdKAostYIBD0khmng0ZWNR9hOHQPUYl3KweUmBognXZBL4KceWsBT6CTuLU9dlvL%2FG58Im6X34%2B5pOei2OULJ5pwysw4rwDYE7F0JdUYs8KDcgU%2FETWm3LZUzYFALM3qVqfpl1VK6Y9p%2BRPnKRjhEDeO59DHnnq5yPdhUETdA3TXvkOMMqg0Y9EmNpjg8e0FS28BS3cXK%2BEIwdd33pugM7Y7eCgeliqWnfLzMhS1QQ7Rc07NWLqlk5St8pJgqbnmAowpavL3U9rv5Ta9htscnhheNxaTxYowevh7b5YlOWWsqYST3xLYaZYR6AF%2FSdaA2ZCf07%2Fu%2BgZpU3lVBQuFlK4MfSgOPDJKCFJcT3SpW7dhcnc5h7au8S1rotXRAHTNlTCRi429BjqkAda6TTbK6laLP8FpzALrBxUWaCbpMLcVhqAurS2Dc7%2B2iGnEecNlDgaXFlFXek74nLSChynWBVw2nOLvqRaNolxqbR7HmU00CX6g3IQM%2FXYZf8eqGoMQ%2BANuSNa4aDCpGIKg%2F%2Ba%2Bal6FApBUuqs4MHqnRIEcWtq8o%2BC1nNU02XdUR79XhGiLw9vpefIz8dwTZTCSeZQ8Uf4BP%2FvQEqeBdnStQGVO&X-Amz-Signature=3117324436ae7b81ea471eeb83b177da0366e45b0f247ad5968f0938a356c385&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IU2KHM2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIHRl7vizigTHQKps5dCJUoagIg0heEH2SwQk792FKtwzAiBGaWiq4B5Z8eus38HpzHAgOuIuIVd9nh5K4Wq54b4xwyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIM8cVyN581XUj0yKieKtwDAbmNimrXTf2lBsGyQo1MV6M7ytX8zmRvpVS%2Bolqv0yZXAXdO54Az4%2Bndr5c8zB%2BIABSgXa0DNsn%2FOLK7zHPeZKnO0wtdqrUOWLZc1je6C2rgGJEP0IM8GjgJ3vgMcYbW1bYpXqHMne8Mfb7AHQuLDRRHDrj%2F5EbQgfaERRjSGXU6EhvLf9Fr2jnII%2FRmYFRgBlcMrRDaMX2myAkiZWuS9h6b971w1StwfGTtEFCvtBS6r9bkusKJg75rcnrGFxtS7%2FBhXVJH6%2FDfcQPRmdyDWBZZonv4Zu614iqiUNqUMvjZdZIkob28pzHZfIv6lKfXDQjtKLa5gW%2BkPSariV3oHPWShawmedHqglOEhoRPXTstSxHbI1hxbHrvtEApmwnO0wu%2Fc5DEoF8Era4H3uNqPFShxmbPcDtC4ixkjv%2FFvT9UYYc5wCb2AxvRXhMi7kvPeep0d9cqngB8LUWytos0Z4mlMvhdtcVcwMH13G7mJXjD1Ky3lpWvRtEU2kdUU53I6nrDWKt6mF87Y0TZcmkk9HDnggXKkPS9SBl1mlnEe2sCBMx6vjCw5cMzsCwBFK8PDUc%2B45LjjsWSAY7xc%2FNDcIlk0yCwHimXqrW1nblxMX%2BARqwgRoyn6SpST94wxOONvQY6pgHjDJsO3QN%2B4QG%2FpPfuCr4DQ3uf7ZDKz10TkcS01MHs8JPl%2FNvLw95zPEUBEDs43Ytl33ud0TlrK07zXW51QjJ3hKKbym0Nz75BOxjffh92E8XlVpHF7VKZhR9jbKaDsg4yORjY%2FWOTIolRWVeWN%2FaJ8JqxA2yILp9ZIg5gM%2BjPXk%2B%2B7cYLBxvyKEKzuuV7MG4tWLbLeFWGRfGaovtsqEmeNU5xEqly&X-Amz-Signature=3f15ba474023b6db35392e58ded26d272ea81218a2341f93355843c9c4ccaca3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IU2KHM2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIHRl7vizigTHQKps5dCJUoagIg0heEH2SwQk792FKtwzAiBGaWiq4B5Z8eus38HpzHAgOuIuIVd9nh5K4Wq54b4xwyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIM8cVyN581XUj0yKieKtwDAbmNimrXTf2lBsGyQo1MV6M7ytX8zmRvpVS%2Bolqv0yZXAXdO54Az4%2Bndr5c8zB%2BIABSgXa0DNsn%2FOLK7zHPeZKnO0wtdqrUOWLZc1je6C2rgGJEP0IM8GjgJ3vgMcYbW1bYpXqHMne8Mfb7AHQuLDRRHDrj%2F5EbQgfaERRjSGXU6EhvLf9Fr2jnII%2FRmYFRgBlcMrRDaMX2myAkiZWuS9h6b971w1StwfGTtEFCvtBS6r9bkusKJg75rcnrGFxtS7%2FBhXVJH6%2FDfcQPRmdyDWBZZonv4Zu614iqiUNqUMvjZdZIkob28pzHZfIv6lKfXDQjtKLa5gW%2BkPSariV3oHPWShawmedHqglOEhoRPXTstSxHbI1hxbHrvtEApmwnO0wu%2Fc5DEoF8Era4H3uNqPFShxmbPcDtC4ixkjv%2FFvT9UYYc5wCb2AxvRXhMi7kvPeep0d9cqngB8LUWytos0Z4mlMvhdtcVcwMH13G7mJXjD1Ky3lpWvRtEU2kdUU53I6nrDWKt6mF87Y0TZcmkk9HDnggXKkPS9SBl1mlnEe2sCBMx6vjCw5cMzsCwBFK8PDUc%2B45LjjsWSAY7xc%2FNDcIlk0yCwHimXqrW1nblxMX%2BARqwgRoyn6SpST94wxOONvQY6pgHjDJsO3QN%2B4QG%2FpPfuCr4DQ3uf7ZDKz10TkcS01MHs8JPl%2FNvLw95zPEUBEDs43Ytl33ud0TlrK07zXW51QjJ3hKKbym0Nz75BOxjffh92E8XlVpHF7VKZhR9jbKaDsg4yORjY%2FWOTIolRWVeWN%2FaJ8JqxA2yILp9ZIg5gM%2BjPXk%2B%2B7cYLBxvyKEKzuuV7MG4tWLbLeFWGRfGaovtsqEmeNU5xEqly&X-Amz-Signature=e07b80d429998cfd7728d2a69f586c688f9572b2a49d8240547b45cff65cf88a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IU2KHM2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIHRl7vizigTHQKps5dCJUoagIg0heEH2SwQk792FKtwzAiBGaWiq4B5Z8eus38HpzHAgOuIuIVd9nh5K4Wq54b4xwyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIM8cVyN581XUj0yKieKtwDAbmNimrXTf2lBsGyQo1MV6M7ytX8zmRvpVS%2Bolqv0yZXAXdO54Az4%2Bndr5c8zB%2BIABSgXa0DNsn%2FOLK7zHPeZKnO0wtdqrUOWLZc1je6C2rgGJEP0IM8GjgJ3vgMcYbW1bYpXqHMne8Mfb7AHQuLDRRHDrj%2F5EbQgfaERRjSGXU6EhvLf9Fr2jnII%2FRmYFRgBlcMrRDaMX2myAkiZWuS9h6b971w1StwfGTtEFCvtBS6r9bkusKJg75rcnrGFxtS7%2FBhXVJH6%2FDfcQPRmdyDWBZZonv4Zu614iqiUNqUMvjZdZIkob28pzHZfIv6lKfXDQjtKLa5gW%2BkPSariV3oHPWShawmedHqglOEhoRPXTstSxHbI1hxbHrvtEApmwnO0wu%2Fc5DEoF8Era4H3uNqPFShxmbPcDtC4ixkjv%2FFvT9UYYc5wCb2AxvRXhMi7kvPeep0d9cqngB8LUWytos0Z4mlMvhdtcVcwMH13G7mJXjD1Ky3lpWvRtEU2kdUU53I6nrDWKt6mF87Y0TZcmkk9HDnggXKkPS9SBl1mlnEe2sCBMx6vjCw5cMzsCwBFK8PDUc%2B45LjjsWSAY7xc%2FNDcIlk0yCwHimXqrW1nblxMX%2BARqwgRoyn6SpST94wxOONvQY6pgHjDJsO3QN%2B4QG%2FpPfuCr4DQ3uf7ZDKz10TkcS01MHs8JPl%2FNvLw95zPEUBEDs43Ytl33ud0TlrK07zXW51QjJ3hKKbym0Nz75BOxjffh92E8XlVpHF7VKZhR9jbKaDsg4yORjY%2FWOTIolRWVeWN%2FaJ8JqxA2yILp9ZIg5gM%2BjPXk%2B%2B7cYLBxvyKEKzuuV7MG4tWLbLeFWGRfGaovtsqEmeNU5xEqly&X-Amz-Signature=fed310d40edad6d4b40b21ab3a808deaa43e83fb43774fd0eb5c7621fc714eb7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHXML7U%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDCUXVzrzwRLGjrFpLsve3et%2FL2d0h3VXtauKpXE6GUEwIgIJHI7dNM1krUK%2F1SpNNVgeExis0nQOZt001xLH8ycqIq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDvm4KxNCbrf8RZCBSrcA57hbqC6zOTtvbaJhC0h3WDDulClPflk60p5RsM3B2Otygz%2BRlhRrPKCdiYiAeGkdEkaZYMNJ%2Fz1NvA5q%2B7wvZlAo11czOwWZTSLI%2Fr%2BnazmVPBvKxEyF3POCGv1JJ4nLvy8PGWcL9o4Zfayi3%2B2goHp3IKC%2FQqorxmxeZfshAIXtYNzgMuYUNZWlk%2F%2FIwwghsrrQIjndxph1PdAb3D4fuD86BmtL5CQDQGA%2B9OcVJRQFWaAesY5lPD9U9lgGsS4b35V6yJUW8HDoVhGPemZPxanCtfHVQ5hWvIGW1oae%2FoSFBzU%2F5wtdDj3%2F2loH8lC2p5d2qGVs2VU5gRVoz92pt6mJ4mjhqkWBOceegt0frElpKKkWptCnxkxL73LlsGVJQJ6liKISRUvcSzAioeU1UxQiomuqdxLF%2Fu9QtZ61HqmMRp7vvJV9CFe5OZjSRW3UHBlG7XfJsMjZ8IH3UeshAb4UJHLiHj1WslJMPIyWFSiCiZjTIaA8u6Rdf77wcqiqgFs0rKvyGfjZzxNSUl0NY%2FssFXsMXzp3EVVCSXRhMAnlT1mbq5fzGW3tpB7BBj%2B3xIwYC%2Fpxd3tzushSPNhpGHZanHQAbroS027BiRr%2F8hTgQq4noeTlUtg2ly%2FMIOLjb0GOqUBQrUsbeeEm4aUJg%2FEnQSF6MjtTtGhc3bl6VxEjvRXbNgULtd3ZR0kAHycLgQtOLm8HmImWJbIkaT%2BaUgC9nfERrXzWWhirJBL2scz3dOu8vanlCCPEZSe4nIYL9ldKUxqduvkirNV%2BXkxeWsW0LkxnHaL9PFwSbgwilYxg0NcPWeNjhFkh4Ai4c1vnuF3WqAxFAQQkKiIZo9CBc%2F26rP1t9KL6wr1&X-Amz-Signature=31098793a7e8217b572159b1a9b61a3683b2a2c0904ea8877c109ded2ef866df&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2J73T64%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQD4BM3%2F9c47uVQ7IfHYtvBuRc0TEeDQB8QtLP1Qs9G%2BJAIgK5%2FRPjqe7o%2BYwAQfSbfOxje90%2Bw2n0kjCz%2FIjf4ZcAcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDD6GrWQlHB0EGBGkwSrcA4t7YGcGeT6TBpRVn4HTxcsBtR3YQ3C7HXYsEVOI4aU9rkbTmvA%2Bm4lcBMxBdPJXHXT%2BX9IMuTxYMCmhM1Oy31xxuLQGKWw9m22Mr%2F3eBkIKIP4ss3gMHHEXUFhwaYt6royQuOuHvTTA0DeU4bseM7IQudW5zQX3dt%2B0xsv%2F2Ag1LGSU9Bx22NXKfFHvkAme7K9qv3ZZhpJcjPLjN3yF%2BGoeTxP8nwaGpHUmEmYIHmparevFchM7wc79NxoiR5BcyoQfjLYO6KUY9jVb%2FHp0YWAdah4MjTf9CiPKMoTsFyAl0%2F6Fj3zW2OwFYU2leatuZHYGcPiPKC2aKCw%2F2sm8yLY6bPMg7PigeXQQ2%2Bti2JUj0YStw2DDuk3%2Bof1MJWOJDxQqMY3EQCTgWp7scNV6y8E%2F8kwycgEk8GvZYktw1QeTqcKYdD3asfBUzdRAE9N44A%2FTpmlXX4TrYZFVLlXLhNhqrWFCNkGQftZvV96DxdxYKGoawpcsVrFTKZ8KWFr4ZrQtsW%2BScm5kXw765Bz%2Fi%2BElx%2Bfx5cMUQdwIA1pUhJqz28lvN6dJDtfNh5o0x0AZ4%2BuPd8DmocBj6tyzHJi8jtCWLY9FANMLhovlfYjBqLLP0GF%2F3HkRbJsHkbD9MJmLjb0GOqUB3y6msOv77z6jUUqW4tj9DbxnGgrmuB4ECJXaKOJazmee3JYfOy5KIHHrhv9v4AM51iY9%2Falw973T2vDDHgwi0OIm3KDboak3rtkflz34DhfVPQq3GGd2PQLU9gJa%2FGulxtv24FqWQ32lmvwQ1E8aXK4At6q06qJvq34FL7k95MNri1lVMHHrrANAGep8D96ooXg9aUZkcfe4NAn5BDQN2%2BnVMgpj&X-Amz-Signature=95c7a2a68a976b0d817fc16bd10a708d3f1a70dfcf2a37a40c149ff573e4df20&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PKZAFXT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQDN7OCIEram8ito%2FN4ROOfrZBUlQHDRZByL7IcHlfVS9QIgLcLG%2F4EOpzRc9PAcpuIkcNwe130h6VVwS%2BKdYzuG74Aq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDEnBT%2FQsDOGuaxD87CrcA0TU%2BSRH%2FlVRYtGeVpv2aqAW7fXpfk3sQvtnmDJelUx0NS3sv0%2FeSCs25RXbN1tRxhH%2Ff8Vr2aHqGF8Maz1CfSOIOImP%2B5rS0KC7%2B7CI5cDbq3%2F1%2FQGC4GZbNDbnZTqc7difXQA6DcrEKZFAOOD7rNrKKdii9091aMPz6sY71KcK2Fa1HBW4Y5yaDQOyjzSlOp0tJCRB5WGxGCsVju3aUWkXR9JLqOVPKRzPrPkYeaFM2uib609JBEU8udeMdo%2B%2Btv0oK8oUJVgfrlT64vcirM5K6ki96ISlo9nJCZfzu8nX2SKk6Ho1nP9gUpQfOHmxCD1oTndQkEPKWZl2eixOX5xEWd3YEuL04FYwNkR%2B1qsg45xFTa4LNiM3oWfL5c0loIIn2%2Bb8FOPamxMjhMOKPccdLKZMbLR0HIsPQjXkw2Z0zPNSkb1SfIL0N3agD1EKhbagCVtV18J1%2BK9pM2ds6etak%2FDxBFZS%2Bq8%2BDxzhlSAG3ohCkeCU4%2BpMKbB4s8mnRldFpnMBTJjiNXRuuV5zKpsbAsSMWw2K5d8Ok5A5kfaKAn6ZdPp0%2Bdmv%2FG8fyoOJFJkE97GNBBzxtufNomsYmvUGdgk6w%2FNYEzIfeGxBNN1%2FrzMEjQOgefOLodNUMLjjjb0GOqUBQStBvqm6bUUmnn%2FPmlpJay%2FGWyZiCALXL9M8MqIDc%2BYNjP1zqNXWsCWRgNWzs39gPL%2FY1hRD5lG4ApR3tUAXBtfQWvckKAnq7xfCV%2FuOPkIdlcmpzcTwYh5S8dvSSJcV8N44D0z7eSkmsX4ecmR0MW292OPRDFcGUgjlE1hw7fG3nOYLyDam1Pvv8WRHin037HRzg5lLzrRKFWG32LcYADRATAb5&X-Amz-Signature=8aaa4bcba8b2e5b1306d66c7b852b3f1417f021c5eace90b4b37061e0b0e1a2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7L7OOFF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCTbqc8XeU8NE3mqDP227DPsT%2FtjTcLeYb0gXM5NbMgyAIgeyERQ16i2IGFL7TVWORHS803AyLw5A0DI1xj%2BY%2FILKgq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDL0NmoT8xOQmQBwT1CrcA%2BCtgSjoHhQcX0PLwncsgu7sGp0NTxxlIQ%2FDwNCyC%2BSZtNlg0MIN1jdSS9Ouv7tVrj6ixKSUN9lpbDVLlWgXsqx%2F7jqkAKWHdozZJjowJOoxFuhgpDbzvcvqWuAtDLXr7ty82WX28DQ%2Bx1UHbb5AdB8fXCHOtP2oa7AIk%2FQP%2Bc5K4vGEkCqlF0Rjzi9K%2FRxrudaWHtrSATrMFnAQ7LJCQEkU4jaQdwVSj%2Fbtd8S%2F3E%2FIm81fYXpzV4u%2BOdGKKuEjIf47FGgMtmfeKhZMOO5KVRIrRdczaPjJPhNRBtWJVapPEx8tI5kOzQvsWMlET4Q64jROa%2FMYYYbkw2EDab7FXZbO%2BW7Ke0YDJMp3%2FzzKyBvwhwxSEpvauWGUrg9ifjgEFdZW2ew7vFMiV8esMMb%2BF5xwXbYJxSTCvbT8rOBGngHHxelxPJoAz9TfBveCo2EduWRrbUPSy14ts9BBkx5RcNbCmgcWf1f0qqyZCXHJS4p6OAYC2OID03%2FUKwMI%2Bsey7DXd43U2iOittogWqHLWt9lj7Xzg6NnHVIXnpLdH0BUZ6tO7DR3O44f9H6hnHCHb8im9vSSN2Hv%2BSmiazTEDnBUeySpGIPd5%2FOoTVHp5z20RrWliC5RNgJUDyVCcMNWKjb0GOqUBlZdlivxHtohYgh69YBsHWLdQUKpiC0aLRFsy%2FwFL8FjVqzrTjoRto3Qb389o%2FC%2F%2FoCHOpH74oCsstecDmDgueJiJbCvtMkUD%2ByXd3SUTXgZMF5NFm%2BJYh0lGt911g2yxILNnV%2FBgNpZZKnk%2FbRFq5RaF4zNSGkKp2sisqfXakUnPv33r%2F9Rt8yWEvABctqRNgSZyXUkYbhv3KnWodygpfYylYqm%2B&X-Amz-Signature=d7899a353e60f317f8adab4a4257f2761d055b3f13ad93b82e7b5b99c3addc1e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7L7OOFF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCTbqc8XeU8NE3mqDP227DPsT%2FtjTcLeYb0gXM5NbMgyAIgeyERQ16i2IGFL7TVWORHS803AyLw5A0DI1xj%2BY%2FILKgq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDL0NmoT8xOQmQBwT1CrcA%2BCtgSjoHhQcX0PLwncsgu7sGp0NTxxlIQ%2FDwNCyC%2BSZtNlg0MIN1jdSS9Ouv7tVrj6ixKSUN9lpbDVLlWgXsqx%2F7jqkAKWHdozZJjowJOoxFuhgpDbzvcvqWuAtDLXr7ty82WX28DQ%2Bx1UHbb5AdB8fXCHOtP2oa7AIk%2FQP%2Bc5K4vGEkCqlF0Rjzi9K%2FRxrudaWHtrSATrMFnAQ7LJCQEkU4jaQdwVSj%2Fbtd8S%2F3E%2FIm81fYXpzV4u%2BOdGKKuEjIf47FGgMtmfeKhZMOO5KVRIrRdczaPjJPhNRBtWJVapPEx8tI5kOzQvsWMlET4Q64jROa%2FMYYYbkw2EDab7FXZbO%2BW7Ke0YDJMp3%2FzzKyBvwhwxSEpvauWGUrg9ifjgEFdZW2ew7vFMiV8esMMb%2BF5xwXbYJxSTCvbT8rOBGngHHxelxPJoAz9TfBveCo2EduWRrbUPSy14ts9BBkx5RcNbCmgcWf1f0qqyZCXHJS4p6OAYC2OID03%2FUKwMI%2Bsey7DXd43U2iOittogWqHLWt9lj7Xzg6NnHVIXnpLdH0BUZ6tO7DR3O44f9H6hnHCHb8im9vSSN2Hv%2BSmiazTEDnBUeySpGIPd5%2FOoTVHp5z20RrWliC5RNgJUDyVCcMNWKjb0GOqUBlZdlivxHtohYgh69YBsHWLdQUKpiC0aLRFsy%2FwFL8FjVqzrTjoRto3Qb389o%2FC%2F%2FoCHOpH74oCsstecDmDgueJiJbCvtMkUD%2ByXd3SUTXgZMF5NFm%2BJYh0lGt911g2yxILNnV%2FBgNpZZKnk%2FbRFq5RaF4zNSGkKp2sisqfXakUnPv33r%2F9Rt8yWEvABctqRNgSZyXUkYbhv3KnWodygpfYylYqm%2B&X-Amz-Signature=9550fc474a0fecf71ebff70800e8e298fd466fcc8ea2e1128684f105a78663cc&X-Amz-SignedHeaders=host&x-id=GetObject)

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
