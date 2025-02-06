

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T2PDS33%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCICerwM1wych16JQM5ylEHElA1pp1l5t5hMfBHFeCwgpOAiAFRH9KVtvwSZxq8nx1C51ufyrYW5191kro6PxoW6Mh2ir%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIM0EeNUMYmzClxEh1yKtwDnwGr10UjIGKA8IiGuCTJw1KwHh3%2FeSvfp8r8WxSqDq6Dhqw48WotYaayrJsq2SIBYkIvIFW77bb3BGTz5u3Nom3XuNxy63%2FNZ5Wj99S6KN%2F9kZd6RKkTGPastRpL0JPDSKP9BSpniM1JLh5hkj9BVTWNz133AGmrkWn4GMEnokS3rQJYMmw0mX1U9UOpEuF7c2xSkPzWVdrWNo8VqBvD2eMRVtz%2Fa3hhNvyfC9Myw%2BuKwzDKmArVfUiJm%2F3J5wxxevBmjwLPhBJhEewrHlWo6luUYkEPDHXAT9gXyJVyQ70RXVvYQCg1r8d3EQlR4LytZRDlu84rOb23RFxzDVOH9ckDc%2FsZUaBpIghJTrokjMNZoqGXxv9qWtDrH38yZiDpPXo9llwBTPcqXH3XavDM1thR%2Bb36cz6Y%2BsQOmocEXTF5inUaW0EMXXzC5TQnJ3M5igEOQVRbBaSnrefjZcHoH%2BLOvdSa6IvEyhh0lz3sW1BYsw7p8ZzoJeLcPYxM4guoyIFUR5%2ByIiMFepZ0CPOesYGxfTwZfId2U9GVnm1gzCNFuTbSI07o%2BQoncmRUDZnFBHjor5TGxKlj%2BtNJbOEx7dnrnX%2FWg%2FlnG3hjSNDmeVtlKDv7XemvitviKZ0w0baRvQY6pgH1ksrbA8MV5VvHV8wH0OVJ%2F%2FBbCpq1uTN%2BfvtnZG2QEkxb5yKELtK8EtOEm1y4pDeZxBx48cP49P2Yh6%2BV%2FfcCaspnSGps6se5l%2Ff6zBpcYk5KShQbjoRh8oRn4vvwGlCW7M0vvsBaT9tF%2BVDaidRM7jgY%2BxARVc88tuWBKb7J%2FNcRw6OsL0xU5u%2Fp8lPyT2Lbu0LI8REcTdsNjmHpPWObXPgacHrU&X-Amz-Signature=4e85dee2fa293b2520a8e47cf1ec7fdad3972f2c74164d420bec8641f2cc3b28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T2PDS33%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCICerwM1wych16JQM5ylEHElA1pp1l5t5hMfBHFeCwgpOAiAFRH9KVtvwSZxq8nx1C51ufyrYW5191kro6PxoW6Mh2ir%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIM0EeNUMYmzClxEh1yKtwDnwGr10UjIGKA8IiGuCTJw1KwHh3%2FeSvfp8r8WxSqDq6Dhqw48WotYaayrJsq2SIBYkIvIFW77bb3BGTz5u3Nom3XuNxy63%2FNZ5Wj99S6KN%2F9kZd6RKkTGPastRpL0JPDSKP9BSpniM1JLh5hkj9BVTWNz133AGmrkWn4GMEnokS3rQJYMmw0mX1U9UOpEuF7c2xSkPzWVdrWNo8VqBvD2eMRVtz%2Fa3hhNvyfC9Myw%2BuKwzDKmArVfUiJm%2F3J5wxxevBmjwLPhBJhEewrHlWo6luUYkEPDHXAT9gXyJVyQ70RXVvYQCg1r8d3EQlR4LytZRDlu84rOb23RFxzDVOH9ckDc%2FsZUaBpIghJTrokjMNZoqGXxv9qWtDrH38yZiDpPXo9llwBTPcqXH3XavDM1thR%2Bb36cz6Y%2BsQOmocEXTF5inUaW0EMXXzC5TQnJ3M5igEOQVRbBaSnrefjZcHoH%2BLOvdSa6IvEyhh0lz3sW1BYsw7p8ZzoJeLcPYxM4guoyIFUR5%2ByIiMFepZ0CPOesYGxfTwZfId2U9GVnm1gzCNFuTbSI07o%2BQoncmRUDZnFBHjor5TGxKlj%2BtNJbOEx7dnrnX%2FWg%2FlnG3hjSNDmeVtlKDv7XemvitviKZ0w0baRvQY6pgH1ksrbA8MV5VvHV8wH0OVJ%2F%2FBbCpq1uTN%2BfvtnZG2QEkxb5yKELtK8EtOEm1y4pDeZxBx48cP49P2Yh6%2BV%2FfcCaspnSGps6se5l%2Ff6zBpcYk5KShQbjoRh8oRn4vvwGlCW7M0vvsBaT9tF%2BVDaidRM7jgY%2BxARVc88tuWBKb7J%2FNcRw6OsL0xU5u%2Fp8lPyT2Lbu0LI8REcTdsNjmHpPWObXPgacHrU&X-Amz-Signature=cfcb0b528755c6128bc1aec7e623526d37271c6f23a6cd43bcbbb1e55f746de1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T2PDS33%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCICerwM1wych16JQM5ylEHElA1pp1l5t5hMfBHFeCwgpOAiAFRH9KVtvwSZxq8nx1C51ufyrYW5191kro6PxoW6Mh2ir%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIM0EeNUMYmzClxEh1yKtwDnwGr10UjIGKA8IiGuCTJw1KwHh3%2FeSvfp8r8WxSqDq6Dhqw48WotYaayrJsq2SIBYkIvIFW77bb3BGTz5u3Nom3XuNxy63%2FNZ5Wj99S6KN%2F9kZd6RKkTGPastRpL0JPDSKP9BSpniM1JLh5hkj9BVTWNz133AGmrkWn4GMEnokS3rQJYMmw0mX1U9UOpEuF7c2xSkPzWVdrWNo8VqBvD2eMRVtz%2Fa3hhNvyfC9Myw%2BuKwzDKmArVfUiJm%2F3J5wxxevBmjwLPhBJhEewrHlWo6luUYkEPDHXAT9gXyJVyQ70RXVvYQCg1r8d3EQlR4LytZRDlu84rOb23RFxzDVOH9ckDc%2FsZUaBpIghJTrokjMNZoqGXxv9qWtDrH38yZiDpPXo9llwBTPcqXH3XavDM1thR%2Bb36cz6Y%2BsQOmocEXTF5inUaW0EMXXzC5TQnJ3M5igEOQVRbBaSnrefjZcHoH%2BLOvdSa6IvEyhh0lz3sW1BYsw7p8ZzoJeLcPYxM4guoyIFUR5%2ByIiMFepZ0CPOesYGxfTwZfId2U9GVnm1gzCNFuTbSI07o%2BQoncmRUDZnFBHjor5TGxKlj%2BtNJbOEx7dnrnX%2FWg%2FlnG3hjSNDmeVtlKDv7XemvitviKZ0w0baRvQY6pgH1ksrbA8MV5VvHV8wH0OVJ%2F%2FBbCpq1uTN%2BfvtnZG2QEkxb5yKELtK8EtOEm1y4pDeZxBx48cP49P2Yh6%2BV%2FfcCaspnSGps6se5l%2Ff6zBpcYk5KShQbjoRh8oRn4vvwGlCW7M0vvsBaT9tF%2BVDaidRM7jgY%2BxARVc88tuWBKb7J%2FNcRw6OsL0xU5u%2Fp8lPyT2Lbu0LI8REcTdsNjmHpPWObXPgacHrU&X-Amz-Signature=4067e69c3acb10895b365aab9b06d0ab7ff849f42cfeab72c4a32542a2008483&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLG2ZXAH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIFTvwdY3INGGr0cBbhBnE%2F%2BELXKViasRAywtPLTXJk1CAiEA0W09RGcbaWJzOgdDcBO1AC%2FfvWMLOLkNHPMe0Zt1kXEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDJqTkvx%2BjnSX5Isv%2FSrcA%2FpS6RaGkib6w6yf55nbX%2F3ogxxFU7ZnaDp0s4OlG82E5NfEUpt7I99Ip9dxPVCbPU9C5rxjIXYGHmp%2ByvW5WESuwfzsJyO1cbSnjaDMb10idcC4QSlfk0mpagP8kmnhH6CIRdOhOOt1QAaJ42hNUAXEBX2gmSOqGN1w4pxntYM2BMU5clplwD9fjF3VzZuKoz7f3m1Oz6A4a1OBEusoDS3AGdRXxLxni%2BVL0u6GoKAXZHIgVkJ6%2BUnMl1Gs0cJVxI6m6Avkm1BR8MqGHwT5NHcITM3ZNoS5290nu4Ckn0sXk99zrZOITE78hlFKTi2hZDkvxyzMSObddm7fs%2FRQiEEn1wnFpE7J4lvOCpheZ7ACz2gTxrGg3svg6sHsG%2B9YddM8kqRORZubc%2FmFragxMeBsSVhhZJY27DupknCrSkC25DUQSXYEDj3YVj5zBuYovVnzouWbxAZTiMspchsS2Wovjot%2FCas4VuVNp6hjVjjw10dvdTUKPQA8sHDWYqcRO8HaOp4pgukysSq5c94yP0PS8RhK4mbZ8d8BLzI2zjW99asn4dT3u9HoW2bHdT%2B84PQ3Vq%2B8TerAnOqiEj9mpgG3fLJuzkDbS0wUH7PPo3QzjGo%2FwG2RiDqqFZceMJy1kb0GOqUBOKIUSzEh9VpSsWmZ0HtL%2BdoX9G0uY14Wi7em%2BLIgDqoDL1IBMhkE50VAzJ1iqCMOiuqHWlXOF8Q4g2Cp6ojENJoL3yIrD1rqBV8tufOsYJ%2BhoYBHBUavDleI4Tf8hOm6LKIseoSHu5saj7U%2FjDsdY%2F4iMHR%2BPj2tbP05VAzI8kM62qxiSqe6NKyMw6t%2B3EYQAOOGJDXPm%2FlIxOkoTWAa7liVf0xJ&X-Amz-Signature=effecdee138151248eed760182c4590d98efe0584c102c639cb22b64c19d4266&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLG2ZXAH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIFTvwdY3INGGr0cBbhBnE%2F%2BELXKViasRAywtPLTXJk1CAiEA0W09RGcbaWJzOgdDcBO1AC%2FfvWMLOLkNHPMe0Zt1kXEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDJqTkvx%2BjnSX5Isv%2FSrcA%2FpS6RaGkib6w6yf55nbX%2F3ogxxFU7ZnaDp0s4OlG82E5NfEUpt7I99Ip9dxPVCbPU9C5rxjIXYGHmp%2ByvW5WESuwfzsJyO1cbSnjaDMb10idcC4QSlfk0mpagP8kmnhH6CIRdOhOOt1QAaJ42hNUAXEBX2gmSOqGN1w4pxntYM2BMU5clplwD9fjF3VzZuKoz7f3m1Oz6A4a1OBEusoDS3AGdRXxLxni%2BVL0u6GoKAXZHIgVkJ6%2BUnMl1Gs0cJVxI6m6Avkm1BR8MqGHwT5NHcITM3ZNoS5290nu4Ckn0sXk99zrZOITE78hlFKTi2hZDkvxyzMSObddm7fs%2FRQiEEn1wnFpE7J4lvOCpheZ7ACz2gTxrGg3svg6sHsG%2B9YddM8kqRORZubc%2FmFragxMeBsSVhhZJY27DupknCrSkC25DUQSXYEDj3YVj5zBuYovVnzouWbxAZTiMspchsS2Wovjot%2FCas4VuVNp6hjVjjw10dvdTUKPQA8sHDWYqcRO8HaOp4pgukysSq5c94yP0PS8RhK4mbZ8d8BLzI2zjW99asn4dT3u9HoW2bHdT%2B84PQ3Vq%2B8TerAnOqiEj9mpgG3fLJuzkDbS0wUH7PPo3QzjGo%2FwG2RiDqqFZceMJy1kb0GOqUBOKIUSzEh9VpSsWmZ0HtL%2BdoX9G0uY14Wi7em%2BLIgDqoDL1IBMhkE50VAzJ1iqCMOiuqHWlXOF8Q4g2Cp6ojENJoL3yIrD1rqBV8tufOsYJ%2BhoYBHBUavDleI4Tf8hOm6LKIseoSHu5saj7U%2FjDsdY%2F4iMHR%2BPj2tbP05VAzI8kM62qxiSqe6NKyMw6t%2B3EYQAOOGJDXPm%2FlIxOkoTWAa7liVf0xJ&X-Amz-Signature=c43ac601ba39cfbe5d2b7c8aca0edb627fe4818dc0ae9e530a0ee61159067ce8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLG2ZXAH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIFTvwdY3INGGr0cBbhBnE%2F%2BELXKViasRAywtPLTXJk1CAiEA0W09RGcbaWJzOgdDcBO1AC%2FfvWMLOLkNHPMe0Zt1kXEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDJqTkvx%2BjnSX5Isv%2FSrcA%2FpS6RaGkib6w6yf55nbX%2F3ogxxFU7ZnaDp0s4OlG82E5NfEUpt7I99Ip9dxPVCbPU9C5rxjIXYGHmp%2ByvW5WESuwfzsJyO1cbSnjaDMb10idcC4QSlfk0mpagP8kmnhH6CIRdOhOOt1QAaJ42hNUAXEBX2gmSOqGN1w4pxntYM2BMU5clplwD9fjF3VzZuKoz7f3m1Oz6A4a1OBEusoDS3AGdRXxLxni%2BVL0u6GoKAXZHIgVkJ6%2BUnMl1Gs0cJVxI6m6Avkm1BR8MqGHwT5NHcITM3ZNoS5290nu4Ckn0sXk99zrZOITE78hlFKTi2hZDkvxyzMSObddm7fs%2FRQiEEn1wnFpE7J4lvOCpheZ7ACz2gTxrGg3svg6sHsG%2B9YddM8kqRORZubc%2FmFragxMeBsSVhhZJY27DupknCrSkC25DUQSXYEDj3YVj5zBuYovVnzouWbxAZTiMspchsS2Wovjot%2FCas4VuVNp6hjVjjw10dvdTUKPQA8sHDWYqcRO8HaOp4pgukysSq5c94yP0PS8RhK4mbZ8d8BLzI2zjW99asn4dT3u9HoW2bHdT%2B84PQ3Vq%2B8TerAnOqiEj9mpgG3fLJuzkDbS0wUH7PPo3QzjGo%2FwG2RiDqqFZceMJy1kb0GOqUBOKIUSzEh9VpSsWmZ0HtL%2BdoX9G0uY14Wi7em%2BLIgDqoDL1IBMhkE50VAzJ1iqCMOiuqHWlXOF8Q4g2Cp6ojENJoL3yIrD1rqBV8tufOsYJ%2BhoYBHBUavDleI4Tf8hOm6LKIseoSHu5saj7U%2FjDsdY%2F4iMHR%2BPj2tbP05VAzI8kM62qxiSqe6NKyMw6t%2B3EYQAOOGJDXPm%2FlIxOkoTWAa7liVf0xJ&X-Amz-Signature=440517900690539f85d120d64673f4dc9077ad492abefdac07d31b2d44a4a5ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLG2ZXAH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIFTvwdY3INGGr0cBbhBnE%2F%2BELXKViasRAywtPLTXJk1CAiEA0W09RGcbaWJzOgdDcBO1AC%2FfvWMLOLkNHPMe0Zt1kXEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDJqTkvx%2BjnSX5Isv%2FSrcA%2FpS6RaGkib6w6yf55nbX%2F3ogxxFU7ZnaDp0s4OlG82E5NfEUpt7I99Ip9dxPVCbPU9C5rxjIXYGHmp%2ByvW5WESuwfzsJyO1cbSnjaDMb10idcC4QSlfk0mpagP8kmnhH6CIRdOhOOt1QAaJ42hNUAXEBX2gmSOqGN1w4pxntYM2BMU5clplwD9fjF3VzZuKoz7f3m1Oz6A4a1OBEusoDS3AGdRXxLxni%2BVL0u6GoKAXZHIgVkJ6%2BUnMl1Gs0cJVxI6m6Avkm1BR8MqGHwT5NHcITM3ZNoS5290nu4Ckn0sXk99zrZOITE78hlFKTi2hZDkvxyzMSObddm7fs%2FRQiEEn1wnFpE7J4lvOCpheZ7ACz2gTxrGg3svg6sHsG%2B9YddM8kqRORZubc%2FmFragxMeBsSVhhZJY27DupknCrSkC25DUQSXYEDj3YVj5zBuYovVnzouWbxAZTiMspchsS2Wovjot%2FCas4VuVNp6hjVjjw10dvdTUKPQA8sHDWYqcRO8HaOp4pgukysSq5c94yP0PS8RhK4mbZ8d8BLzI2zjW99asn4dT3u9HoW2bHdT%2B84PQ3Vq%2B8TerAnOqiEj9mpgG3fLJuzkDbS0wUH7PPo3QzjGo%2FwG2RiDqqFZceMJy1kb0GOqUBOKIUSzEh9VpSsWmZ0HtL%2BdoX9G0uY14Wi7em%2BLIgDqoDL1IBMhkE50VAzJ1iqCMOiuqHWlXOF8Q4g2Cp6ojENJoL3yIrD1rqBV8tufOsYJ%2BhoYBHBUavDleI4Tf8hOm6LKIseoSHu5saj7U%2FjDsdY%2F4iMHR%2BPj2tbP05VAzI8kM62qxiSqe6NKyMw6t%2B3EYQAOOGJDXPm%2FlIxOkoTWAa7liVf0xJ&X-Amz-Signature=c68996e6201304460c55d28db4906de1506611fb6dd93dd2c3ce4ff07004c0cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLG2ZXAH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIFTvwdY3INGGr0cBbhBnE%2F%2BELXKViasRAywtPLTXJk1CAiEA0W09RGcbaWJzOgdDcBO1AC%2FfvWMLOLkNHPMe0Zt1kXEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDJqTkvx%2BjnSX5Isv%2FSrcA%2FpS6RaGkib6w6yf55nbX%2F3ogxxFU7ZnaDp0s4OlG82E5NfEUpt7I99Ip9dxPVCbPU9C5rxjIXYGHmp%2ByvW5WESuwfzsJyO1cbSnjaDMb10idcC4QSlfk0mpagP8kmnhH6CIRdOhOOt1QAaJ42hNUAXEBX2gmSOqGN1w4pxntYM2BMU5clplwD9fjF3VzZuKoz7f3m1Oz6A4a1OBEusoDS3AGdRXxLxni%2BVL0u6GoKAXZHIgVkJ6%2BUnMl1Gs0cJVxI6m6Avkm1BR8MqGHwT5NHcITM3ZNoS5290nu4Ckn0sXk99zrZOITE78hlFKTi2hZDkvxyzMSObddm7fs%2FRQiEEn1wnFpE7J4lvOCpheZ7ACz2gTxrGg3svg6sHsG%2B9YddM8kqRORZubc%2FmFragxMeBsSVhhZJY27DupknCrSkC25DUQSXYEDj3YVj5zBuYovVnzouWbxAZTiMspchsS2Wovjot%2FCas4VuVNp6hjVjjw10dvdTUKPQA8sHDWYqcRO8HaOp4pgukysSq5c94yP0PS8RhK4mbZ8d8BLzI2zjW99asn4dT3u9HoW2bHdT%2B84PQ3Vq%2B8TerAnOqiEj9mpgG3fLJuzkDbS0wUH7PPo3QzjGo%2FwG2RiDqqFZceMJy1kb0GOqUBOKIUSzEh9VpSsWmZ0HtL%2BdoX9G0uY14Wi7em%2BLIgDqoDL1IBMhkE50VAzJ1iqCMOiuqHWlXOF8Q4g2Cp6ojENJoL3yIrD1rqBV8tufOsYJ%2BhoYBHBUavDleI4Tf8hOm6LKIseoSHu5saj7U%2FjDsdY%2F4iMHR%2BPj2tbP05VAzI8kM62qxiSqe6NKyMw6t%2B3EYQAOOGJDXPm%2FlIxOkoTWAa7liVf0xJ&X-Amz-Signature=d1caff20bede247e370866f82bb2a13b941a4c0cddc44d6c4505c9b04ac9d9b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLG2ZXAH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIFTvwdY3INGGr0cBbhBnE%2F%2BELXKViasRAywtPLTXJk1CAiEA0W09RGcbaWJzOgdDcBO1AC%2FfvWMLOLkNHPMe0Zt1kXEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDJqTkvx%2BjnSX5Isv%2FSrcA%2FpS6RaGkib6w6yf55nbX%2F3ogxxFU7ZnaDp0s4OlG82E5NfEUpt7I99Ip9dxPVCbPU9C5rxjIXYGHmp%2ByvW5WESuwfzsJyO1cbSnjaDMb10idcC4QSlfk0mpagP8kmnhH6CIRdOhOOt1QAaJ42hNUAXEBX2gmSOqGN1w4pxntYM2BMU5clplwD9fjF3VzZuKoz7f3m1Oz6A4a1OBEusoDS3AGdRXxLxni%2BVL0u6GoKAXZHIgVkJ6%2BUnMl1Gs0cJVxI6m6Avkm1BR8MqGHwT5NHcITM3ZNoS5290nu4Ckn0sXk99zrZOITE78hlFKTi2hZDkvxyzMSObddm7fs%2FRQiEEn1wnFpE7J4lvOCpheZ7ACz2gTxrGg3svg6sHsG%2B9YddM8kqRORZubc%2FmFragxMeBsSVhhZJY27DupknCrSkC25DUQSXYEDj3YVj5zBuYovVnzouWbxAZTiMspchsS2Wovjot%2FCas4VuVNp6hjVjjw10dvdTUKPQA8sHDWYqcRO8HaOp4pgukysSq5c94yP0PS8RhK4mbZ8d8BLzI2zjW99asn4dT3u9HoW2bHdT%2B84PQ3Vq%2B8TerAnOqiEj9mpgG3fLJuzkDbS0wUH7PPo3QzjGo%2FwG2RiDqqFZceMJy1kb0GOqUBOKIUSzEh9VpSsWmZ0HtL%2BdoX9G0uY14Wi7em%2BLIgDqoDL1IBMhkE50VAzJ1iqCMOiuqHWlXOF8Q4g2Cp6ojENJoL3yIrD1rqBV8tufOsYJ%2BhoYBHBUavDleI4Tf8hOm6LKIseoSHu5saj7U%2FjDsdY%2F4iMHR%2BPj2tbP05VAzI8kM62qxiSqe6NKyMw6t%2B3EYQAOOGJDXPm%2FlIxOkoTWAa7liVf0xJ&X-Amz-Signature=ff6630d8ea3e9fca1a70574064430feea41a72a7496795f0799e54c2fba8197c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6N3Z2QT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIBFlcxyUjBmCiDKs%2B4WHR2nPcI2UgP609AAZgZqx%2FR94AiB1GGKcBNcbq2C9aMOAyfQA1CeiQbKnxd%2BddU%2BNO%2FTj7Cr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMowYnTsiNolmKi96jKtwD4n8fxbugBLDdUc1AHXMlRYbWkAVhLL5yAohX0Belrm5I3Qu%2FcE0DvzPOZ3kONltPbeuohlnk86TlU5W0iUtVDEtsvuJQFJC0VCtBUWZ7gN19gmz9Qf%2BmHixuOjDcqiaD68wS46liCIERz2tSBEQk2ON7IXd6ceWf0TNmaN3bUpg472vY8jyFeqDBeqrRLiFw%2B2H%2FFDzu91wgxh68m9nYIzUEE6Ed%2FDruyuo7DuRDdmH8cUag%2FQoTgxZehxan9TY%2ByRTHPlmU3wZi%2BTHyBo2nznWpB6cUnqU1Dc6DeVdq9SbG0kXqjKidY1runYyLcTgxdVgZRKZmurpDCqGjnH3x9gMP3ppm6vz3U1x1sd83sph%2FAfot%2FyHG69bfrz8vVD06QW7bppd%2BBrxVnbAfGNtH3zYSN7mn%2F3MRyj%2BAH12jkFkPQXgQpRUE6hMU8oXtHxw6n4TUUAtjzKvL0QeeCFWA%2BpREZ3kt1tP42DuE6C9luJbKxlJkZQnCiDAeJ6SeATSBXDsncyCLym8UHCk8lAvoxhfP1Gq5lWQOrig80FHYXmM%2F4ZpExrHnkEqrOqB9n34ZngHDqAG3e5zkggbHusov%2BE8zpGIT38fF8BuqTHF7ADTvEwjisaH%2F7m7754AwwraRvQY6pgHnHqaAmANFLeBh0BH7Iyhy6Q3Phj83Qai0NCNdcD97xYBUONrChZNHzf%2FJocuoz2%2B4oVuhQwdRb2QpjW%2BJp7OSmTFRWKlXpFiB1m2Lp5GwgAKq%2FtDsPiUvrxeLiCI8GLzsbDbIyMPUmIzRe6ImbWtL2Ik0STT9XblwFxosdHLpJalhcs6mnhuXWbagqVmUxU8JqVeOtXBpT9iKsHhNm6xkMh4Advxq&X-Amz-Signature=f553f03997bda3a515a633a176f3b167b81c893490477ea2a7d2cc89a2739eb7&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZSYKFD2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIFF%2BiebRIS6pkZqZddKoV5LvRRKMwTuafMI6DiU9KKpyAiEAg0WP0J%2BTgPfyioXFL%2B1kA2%2BgI9Vyg4%2FC2qUwwNdeJn8q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDN7Rj7D17j41cBExCSrcA2l7cN1Hp2BocUYdiI6ag%2F7BCSyYbT%2BnXXmTdEi%2BCNjJmnl3ZlrpdqNOaGl7UXBx7W5JRIFNA6gDyR3QXBgpsxtu1lOsIxmO98S5BqiTq4q0nEw%2BMH%2F4wVlQ1WYqhhzuCY4uNZpHzQDpU9iqieU2YLI39JilR3xqiLgqTeKkM%2F6xLxWRik9KRq2CaCt8oMZdiC73Mer%2B%2FqjonY26vERcIr0MqahTZ3IvKJMzOdEUflqkLGRua2ks32Fe%2Fl5XF%2FDgiHyuANlT2OCml%2B%2FjDoKmEEaiFPlQ1gQL7woR2d%2FVSvOdjv8zo4aYO9RLGtNvdMUzradVgBWmeS%2BDJcnQMZZ0TBq%2FKxh9RmujWYgnK%2F3qbyk6qkCB%2Bo%2Fef29rtfnromOvtUfVXY0ln5%2FBTXNeCtQSd82NXhlnyydiYXPednawLKYEX0P73%2Be96GCGObjgwuXfPT0%2Bw32lyDrd265a8VjDdsRcmyADmHd%2BpbOSthF7JDlefdxCj6IV0xcAJqTNtdcsCfBaqy8HUfhGb6fd4uhf6jg1quFlFZcfb3jdyJEPMaHn2bVKEyeUNecsVa9wmfCnlb7I8vE3E3MDy4MNxpHybK3Qjl%2FYZKgTOlnZ2VVsd8rwLCejGpRkLyR0dVmoMIq1kb0GOqUBDj9JmiSGI7b4%2F2O5lC9FeE3jge1nAoC7ubfO6WQsghy%2Fzoqtj%2B5QWLhkUvv1JAv49hyf1oIitR0MGuIqFIql1IWwXosyOogjGxURx5Wipy0%2BaN2rQvTvjDnzKEAOrMeMR%2BYSfeS1qunp13Rmadkjl6EFKUfqFinGhA08jypuyvXKL7VoBuoYjLg1XXIpTSbByl%2ByBekDPiyodz0buXdh19WaHa0h&X-Amz-Signature=40463c6346beeaec6ad6179e9dfe868ff4361ab90508f286a1615e643db2da31&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLG2ZXAH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIFTvwdY3INGGr0cBbhBnE%2F%2BELXKViasRAywtPLTXJk1CAiEA0W09RGcbaWJzOgdDcBO1AC%2FfvWMLOLkNHPMe0Zt1kXEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDJqTkvx%2BjnSX5Isv%2FSrcA%2FpS6RaGkib6w6yf55nbX%2F3ogxxFU7ZnaDp0s4OlG82E5NfEUpt7I99Ip9dxPVCbPU9C5rxjIXYGHmp%2ByvW5WESuwfzsJyO1cbSnjaDMb10idcC4QSlfk0mpagP8kmnhH6CIRdOhOOt1QAaJ42hNUAXEBX2gmSOqGN1w4pxntYM2BMU5clplwD9fjF3VzZuKoz7f3m1Oz6A4a1OBEusoDS3AGdRXxLxni%2BVL0u6GoKAXZHIgVkJ6%2BUnMl1Gs0cJVxI6m6Avkm1BR8MqGHwT5NHcITM3ZNoS5290nu4Ckn0sXk99zrZOITE78hlFKTi2hZDkvxyzMSObddm7fs%2FRQiEEn1wnFpE7J4lvOCpheZ7ACz2gTxrGg3svg6sHsG%2B9YddM8kqRORZubc%2FmFragxMeBsSVhhZJY27DupknCrSkC25DUQSXYEDj3YVj5zBuYovVnzouWbxAZTiMspchsS2Wovjot%2FCas4VuVNp6hjVjjw10dvdTUKPQA8sHDWYqcRO8HaOp4pgukysSq5c94yP0PS8RhK4mbZ8d8BLzI2zjW99asn4dT3u9HoW2bHdT%2B84PQ3Vq%2B8TerAnOqiEj9mpgG3fLJuzkDbS0wUH7PPo3QzjGo%2FwG2RiDqqFZceMJy1kb0GOqUBOKIUSzEh9VpSsWmZ0HtL%2BdoX9G0uY14Wi7em%2BLIgDqoDL1IBMhkE50VAzJ1iqCMOiuqHWlXOF8Q4g2Cp6ojENJoL3yIrD1rqBV8tufOsYJ%2BhoYBHBUavDleI4Tf8hOm6LKIseoSHu5saj7U%2FjDsdY%2F4iMHR%2BPj2tbP05VAzI8kM62qxiSqe6NKyMw6t%2B3EYQAOOGJDXPm%2FlIxOkoTWAa7liVf0xJ&X-Amz-Signature=2ff8c4fd4a3a53214700be982ca36bf4cccf24a3e0b38f25a9ae6b4de585d978&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLG2ZXAH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIFTvwdY3INGGr0cBbhBnE%2F%2BELXKViasRAywtPLTXJk1CAiEA0W09RGcbaWJzOgdDcBO1AC%2FfvWMLOLkNHPMe0Zt1kXEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDJqTkvx%2BjnSX5Isv%2FSrcA%2FpS6RaGkib6w6yf55nbX%2F3ogxxFU7ZnaDp0s4OlG82E5NfEUpt7I99Ip9dxPVCbPU9C5rxjIXYGHmp%2ByvW5WESuwfzsJyO1cbSnjaDMb10idcC4QSlfk0mpagP8kmnhH6CIRdOhOOt1QAaJ42hNUAXEBX2gmSOqGN1w4pxntYM2BMU5clplwD9fjF3VzZuKoz7f3m1Oz6A4a1OBEusoDS3AGdRXxLxni%2BVL0u6GoKAXZHIgVkJ6%2BUnMl1Gs0cJVxI6m6Avkm1BR8MqGHwT5NHcITM3ZNoS5290nu4Ckn0sXk99zrZOITE78hlFKTi2hZDkvxyzMSObddm7fs%2FRQiEEn1wnFpE7J4lvOCpheZ7ACz2gTxrGg3svg6sHsG%2B9YddM8kqRORZubc%2FmFragxMeBsSVhhZJY27DupknCrSkC25DUQSXYEDj3YVj5zBuYovVnzouWbxAZTiMspchsS2Wovjot%2FCas4VuVNp6hjVjjw10dvdTUKPQA8sHDWYqcRO8HaOp4pgukysSq5c94yP0PS8RhK4mbZ8d8BLzI2zjW99asn4dT3u9HoW2bHdT%2B84PQ3Vq%2B8TerAnOqiEj9mpgG3fLJuzkDbS0wUH7PPo3QzjGo%2FwG2RiDqqFZceMJy1kb0GOqUBOKIUSzEh9VpSsWmZ0HtL%2BdoX9G0uY14Wi7em%2BLIgDqoDL1IBMhkE50VAzJ1iqCMOiuqHWlXOF8Q4g2Cp6ojENJoL3yIrD1rqBV8tufOsYJ%2BhoYBHBUavDleI4Tf8hOm6LKIseoSHu5saj7U%2FjDsdY%2F4iMHR%2BPj2tbP05VAzI8kM62qxiSqe6NKyMw6t%2B3EYQAOOGJDXPm%2FlIxOkoTWAa7liVf0xJ&X-Amz-Signature=c3af6f2909b9e45530ee67e9dc36a9cf057071ac675ee72720c74593a02e57ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLG2ZXAH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIFTvwdY3INGGr0cBbhBnE%2F%2BELXKViasRAywtPLTXJk1CAiEA0W09RGcbaWJzOgdDcBO1AC%2FfvWMLOLkNHPMe0Zt1kXEq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDJqTkvx%2BjnSX5Isv%2FSrcA%2FpS6RaGkib6w6yf55nbX%2F3ogxxFU7ZnaDp0s4OlG82E5NfEUpt7I99Ip9dxPVCbPU9C5rxjIXYGHmp%2ByvW5WESuwfzsJyO1cbSnjaDMb10idcC4QSlfk0mpagP8kmnhH6CIRdOhOOt1QAaJ42hNUAXEBX2gmSOqGN1w4pxntYM2BMU5clplwD9fjF3VzZuKoz7f3m1Oz6A4a1OBEusoDS3AGdRXxLxni%2BVL0u6GoKAXZHIgVkJ6%2BUnMl1Gs0cJVxI6m6Avkm1BR8MqGHwT5NHcITM3ZNoS5290nu4Ckn0sXk99zrZOITE78hlFKTi2hZDkvxyzMSObddm7fs%2FRQiEEn1wnFpE7J4lvOCpheZ7ACz2gTxrGg3svg6sHsG%2B9YddM8kqRORZubc%2FmFragxMeBsSVhhZJY27DupknCrSkC25DUQSXYEDj3YVj5zBuYovVnzouWbxAZTiMspchsS2Wovjot%2FCas4VuVNp6hjVjjw10dvdTUKPQA8sHDWYqcRO8HaOp4pgukysSq5c94yP0PS8RhK4mbZ8d8BLzI2zjW99asn4dT3u9HoW2bHdT%2B84PQ3Vq%2B8TerAnOqiEj9mpgG3fLJuzkDbS0wUH7PPo3QzjGo%2FwG2RiDqqFZceMJy1kb0GOqUBOKIUSzEh9VpSsWmZ0HtL%2BdoX9G0uY14Wi7em%2BLIgDqoDL1IBMhkE50VAzJ1iqCMOiuqHWlXOF8Q4g2Cp6ojENJoL3yIrD1rqBV8tufOsYJ%2BhoYBHBUavDleI4Tf8hOm6LKIseoSHu5saj7U%2FjDsdY%2F4iMHR%2BPj2tbP05VAzI8kM62qxiSqe6NKyMw6t%2B3EYQAOOGJDXPm%2FlIxOkoTWAa7liVf0xJ&X-Amz-Signature=21e225704cac0f56ddb67d061029c3f22025bc2d3f7f85e0cf138791c78a18fe&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQGJ2WDY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDhVBwaMpN0UJudjC2tPVVB0R4ZqGSWmC2mcZi38hg6wAIhANYLI3uoI5I7DZq8fOBvBJ%2F%2F0trO1qtIYFXY3hUW4%2BFRKv8DCFgQABoMNjM3NDIzMTgzODA1IgwFpbpaWv5a6ISukYEq3AOVJfXwo1Bb0z2D04cbffNs2qpWW27hd%2BGkLOnGHrZgtAsFZIvSEBoG5kCoAmD%2FJNIrPv5yr9ZRs4mfX8afiyki8xeCmQc2W0FdQdZ13UYMt6T8BTz2RCAC9wA1NHXNuiPCEqzCjihEt%2Fi%2BPE47Yv329U%2Bbc9jpUaKY3J8QZGLts2OlI1GQ0Xb%2BwjEiQKU%2BEeSTrtKW1BlZoueT5bkPi1LbW9lD35%2BmdkpPDJHeOSNeU3G0r%2FPNQR12U%2B48wxeD8abchEMzBPsXvLCdHbIQ3gjRExqDTPsXVzAXFjfsUAHH21MHTAj8tP3PMHm%2BYtynbWqpZyI5YttgHdcMOgke73yfXDHmbe1Qi9KLUyD4s0Pd4CooSZaC29YsMeIPvCRhFoCGDreJQ7iFIc%2FzGuVWYSZmo7YkQ0KlnC0sz6MDr2PO%2BPIiZFc0TXAv6M2UO9KdtvIIuMhliGMkN0TUXRsH9g0281Y%2FDwXwucf4K80VMKBiiPAB5ESquAtWd7liBhGRWQXPiLmMEvRRTlVaCMzNEYtiPVBkU29hxiSejCq7ca5w1h1J3PwlztQeSg4MoTc6PB9%2BroNDUAm8x1%2BP8lXvDDnqUbkoo3%2BtXwt2lg7%2F77In%2BqhvxDF3V5H0guFi0TDVtJG9BjqkAaZK0eBiD3Ysj81jE%2BZXCIzuTqvASXE9hqYxmzrE4IK5%2FSrG6N%2BoBzuI1M144qce0sN4aBgm%2BcfgZ2pRYZumoFcoxk5GBadZapozL9nH6kdi8glr6jItcWsDDSeAMvGW8lLW%2Fav2evX27BASS5X7VE5n6t8vNoWc05s9D9J5S1eQx7UpfUU4k9P4VJwC5Qtm1aXhiSYXyixJDEJbcajhEYE6vIGH&X-Amz-Signature=d756bbfd022494666270c795ca177cf51e188fe69255e9c774d0e6fe02dca952&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5MDEDSZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQC1FG5AjPoW9g0%2FKCec5Kti0EFv8HSmSbtJKH8x0YqcowIhAO8FZePYM6s8vxd1r2P3DsjSXpBd7TWpWHOz29DhcbZhKv8DCFgQABoMNjM3NDIzMTgzODA1IgxqbUlg0N2h6ZSKNFAq3APp%2FhRlLNxd7no%2FQKK0urUEA97XnITqTN0SMD3dMhd2utBkVuMvCyKE%2B6IjHiS54%2FF17MMtkvrzD12s%2FLfoZ%2F37M%2Fk8h0E1n5k9rzWkLYC6AvWal0ykn%2FYEmf8zx6dg08Ou1d2k7E0sogQs1RWhlpUnUD6OalhGXQv%2F8nVBgNj5jriMm21uU8yafRjcdicMl%2FfDJglngCYi1T9VzgQYxYo9vEo0tPRd7K0dZQgzvjl5yysC2cTLlb1Z1zr%2F9ZKRyBUjiit76q4B%2B%2BsCuG09SrasgnFgSTIjBHT4t4ZlFo0jute%2FPP80jujn6fo53woUIOBFP%2FeEgx3J4oS%2BRytwByfLxMi6QYjHIrCOr5xf96nKZMTu%2F20pHyE1OaV3qSGZD0%2FcSnkNeFQNN2qr0TV%2FGERb676qVudDQzSXx0%2BlfFgOuxbTlpnmkkPqHvXfxMPcwhn7jk95d%2FPH8Et%2BiFqGqa0t5EC8h51oRQDIKvurqe%2BPJD2HOJalhQCvB%2FasF73rNr0j%2BIJYddHCeCN7ME4TuMSUkInky0Vw%2FOepbIAdxd%2F2tZ2t0BzO7Mr3%2FlEiKm2pBpMNEH6Kkd0ufjMxykUa01Z4bciGUFTCOyitMZ%2FBnWdyv26sL97cSASZJBbgJzCDtZG9BjqkAYATqET7q2u0NuAprdmZgzW8po9klpasXpvkhIU%2Bo6WoSLxnxnaydsQU47e7ohtP34v%2FiYFZZlcdkWz4EzzeZOKVeHfBf1DP8GwGaEfQYFBl45rw%2F30%2FyR59GCz8F7yH%2BV4hmKNpRf2hCbhtzPsedRanbOFMOv9yryBG1kSycV%2FxpiR3vNSkJtbZvVzU5pHl0K2t7vpunM7I3ms6tsTx4NQYFKtF&X-Amz-Signature=2af97feb089c9b4ff6d1831dd7f25a7cfee54d248e607ae88b8b04f1b0890ce3&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBDMOB7G%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDmmUHXsoAZrROT1ZioSnnBGe6ijj8c6KHMLMpglBe4CAIhAIvRQXhs0aipU2XDa9zEyMJk18I7u3sIctNkhIhqjpbpKv8DCFgQABoMNjM3NDIzMTgzODA1Igye%2Fe%2BnN5Hn%2F80ccVkq3AO3qavMixmcL9mX32TuG%2Bbl6lTmOh0WFedyUdU4wzn4ygcZK3kc1cnZbRwf4pm7xnWJEq4D4zuBYIThnoSCE3kJ7zer5bZVQJJwlLyz6AaTcX6Pyu5BLxCTn6YTIuPlXUogFC45szF6%2FuhWEJ6PC%2FBBJmK5Pbkpu65n8OKcggHGqMmTBjEGuKKO%2FcP2a6ZgKq%2Fv8rUXokfVJg8ll1Czeelcg4hcWbS6HWWpO1mr7fgiyABw4JqgfD0r%2F0hhUDhXXz3j9ZBKVHSLvQEkR9imsHjjF%2BuPHI%2BBxn9UyBfrG%2F9apaxFwFsuSK%2F3Z6iuCb97fx9KGBJIlIQGRv4h0jT%2BLth98ZiW5L94tkANvmH2QDRsRUkGDQP3xloC54AkTjb3ZZdfrNUwtn%2BJC267P9rg%2BnEuP6G02UoVhcMmYxC5XuNMfkMPu06%2FFSLullSTPlm1CMCrjZBlmztDiWFDTlePtue6yXhSTcqwUxtReF138q0cFi1e5cAcY1L2qNnYkOc%2FhhIfXPROUkPn%2BE5i1cX%2FRQ88%2FhsDlhxEu%2B7lb6F7siwC8Z26qJ%2F%2B%2BiiLHaHscNlyeFLRxklwClfT%2BXlITMfoJjlGsq%2FCrs%2FJ7jdBG7aUm3OO6aYnyjXG7DzPFX%2BR9DD3tJG9BjqkAVRg8TJrA2mj30%2B2gicC7AXETmqixcXorIvWYVzMsH7ZDBZS8F4hgTBeUM%2F%2BevJhy%2Buo2T6i7K%2FaHSEif0weHpHQqLamAKm28dOhWFRk5n%2FbyRT5sz5cqLG0KZSIuN2QkB6dCuZNTh45ybLZyL4ayOWEHHLEZU6a5teSHKZnVU0B08paqVovMQpGPqQqxc2W9uEIngrFXVLh28kgg0mI3Ldw72Ru&X-Amz-Signature=32e939548d47f4387b3293bf719385000809c0f42de44cc6ea911d8942d66fd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GL32CHL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDP7X1wqdZEzhqoHYyUVbGX1JsfuWqREfeHqgLwWrhtFwIgW9wa1yYOKGKmkXNfnOSo6xzpr4AA%2BFkyO0t7%2FVH73skq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDCs5%2FsjNQeK8TvZMQCrcA1fi8XOzLw8t6vWayaa%2B27q2eL6W87EMiuuOeCe0i%2BCguEo7jGpHhFeB899untPjnFun334X1mxUk3uVCMeiSGReFVN9iHtlJ7EGisOG%2F3t%2FnAaPnXgYRZMpLgRwz%2Flxdwn83fbF4dE6oWwzdy%2F9luIRMxFnHHeVLO%2Bxw51QHHXwJvIsVtef4guvrviIF6oUlRTCivcHj8dlbJe8ewyZAtvyYPzPewDgqtmy%2FosOJfNe1ti7vPihTCfxQGaU%2BAacJTkSSiMO%2FR8lVWvxKGY2ePkNv6EcQyoYGR0ZVNg0e4IYxTbvPftbutTcFLFfYKjf1Q4XpvDGRK9ZuaKN6dDvHr6hpTvf2mgc%2BTo7UcgfBnUG94IsNF7r32Lzp%2BnWXG%2FhjZvynhyUtpWi5iM3TzYUL3cJPMnF8qwYrgTmBj3OXvEH5%2FimTJCEZ3DKLX2nX1GV6Nw9qdzeDo1WfrxONJqrgUiMCVwz%2FdHa%2BJLab3FCeuMq0R9cm34fjwVOOVbQOdTQ73qvtsQFit1HazCqY1MC7iaj5djTo3DkZ83i%2Buw4bxTGj%2B%2FVpw2OAfcw3SI6JHeWq%2FIJIjI6hKvwqtE4z5f%2BH7PRz05GLlj63MNGIpnTNfYdfdxwf6uBXJXpicJcMKC1kb0GOqUB2GjIziVYHenPNzLb%2FaiO8pNM8fXcSnd92QfhxhcrvFC%2F%2FPUppNnuyqri23VzLpdJFCHJquewJGwFTn%2B8OsXamoU24D8RNYE4Nv0SYHvnqcBQtM6LYQkuhv6jRyHsyb2lBCNRwLvPoIzFo%2FEiUFYrg%2FaGbhXbHkVt1vinRrF1TeddxT%2B0WlH9cBBHmfYy3TBLH%2Bujau%2BkkjBXYDQbXogK5ikjWGQB&X-Amz-Signature=b538d7c61d005121c07756e6a0fe6edfd12e2230287f941707f23155d405b965&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GL32CHL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDP7X1wqdZEzhqoHYyUVbGX1JsfuWqREfeHqgLwWrhtFwIgW9wa1yYOKGKmkXNfnOSo6xzpr4AA%2BFkyO0t7%2FVH73skq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDCs5%2FsjNQeK8TvZMQCrcA1fi8XOzLw8t6vWayaa%2B27q2eL6W87EMiuuOeCe0i%2BCguEo7jGpHhFeB899untPjnFun334X1mxUk3uVCMeiSGReFVN9iHtlJ7EGisOG%2F3t%2FnAaPnXgYRZMpLgRwz%2Flxdwn83fbF4dE6oWwzdy%2F9luIRMxFnHHeVLO%2Bxw51QHHXwJvIsVtef4guvrviIF6oUlRTCivcHj8dlbJe8ewyZAtvyYPzPewDgqtmy%2FosOJfNe1ti7vPihTCfxQGaU%2BAacJTkSSiMO%2FR8lVWvxKGY2ePkNv6EcQyoYGR0ZVNg0e4IYxTbvPftbutTcFLFfYKjf1Q4XpvDGRK9ZuaKN6dDvHr6hpTvf2mgc%2BTo7UcgfBnUG94IsNF7r32Lzp%2BnWXG%2FhjZvynhyUtpWi5iM3TzYUL3cJPMnF8qwYrgTmBj3OXvEH5%2FimTJCEZ3DKLX2nX1GV6Nw9qdzeDo1WfrxONJqrgUiMCVwz%2FdHa%2BJLab3FCeuMq0R9cm34fjwVOOVbQOdTQ73qvtsQFit1HazCqY1MC7iaj5djTo3DkZ83i%2Buw4bxTGj%2B%2FVpw2OAfcw3SI6JHeWq%2FIJIjI6hKvwqtE4z5f%2BH7PRz05GLlj63MNGIpnTNfYdfdxwf6uBXJXpicJcMKC1kb0GOqUB2GjIziVYHenPNzLb%2FaiO8pNM8fXcSnd92QfhxhcrvFC%2F%2FPUppNnuyqri23VzLpdJFCHJquewJGwFTn%2B8OsXamoU24D8RNYE4Nv0SYHvnqcBQtM6LYQkuhv6jRyHsyb2lBCNRwLvPoIzFo%2FEiUFYrg%2FaGbhXbHkVt1vinRrF1TeddxT%2B0WlH9cBBHmfYy3TBLH%2Bujau%2BkkjBXYDQbXogK5ikjWGQB&X-Amz-Signature=4645f364b65d62e40106c2108ebe8af75a154a619583fb4920532c36bda09610&X-Amz-SignedHeaders=host&x-id=GetObject)

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
