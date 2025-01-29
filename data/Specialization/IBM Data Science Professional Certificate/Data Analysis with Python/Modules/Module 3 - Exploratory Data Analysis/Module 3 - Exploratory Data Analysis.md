

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666CMROKF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYPmZp1D647KJNuUqgGDagyQ3z2B1e2Ku%2B54WSNTCa2QIgTpA0ojBbDMsU90vAlrwZDjfgLgh1lrcwvoSXFvNevCgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG66%2FrWt3kFAeQpDNSrcA3gUvtjEl8koEg4uRT%2FC%2BP9q5x84C9saXHEg0gM8YGJu%2FmfLoMl8%2BlZ2nsZtBdm9zrgXwAN3%2BZsqHhXZlNuBvDf3oXcZUEQ0SjDrut%2B4x3RLBpEqvjU4ATgA1Ya0jaA0nkzRJNfNv4agkGxMsq%2F92qOaLjLbscOtMIqOV3BszSL6etfsuGaOMYvuoOAnTRbqBtDqj4V9KoGiTl3Hs40%2BVlPhCMk%2F6INHMVRZxZMC6ahA7foHHcIS3fpihn4tsQ%2BgNnQ19YMENvfMBmsabM0eQD%2BPlNFIpyaT9jm13xc40zsc7cS5poZS7u%2FdFXqDh%2Fy2467UZlskT%2BKdhuZSebmKWGP6hPmHXdUJmxcVmTx4JhX1rt6r0YymzYfJ2Z%2FpAGkIbhQ%2Bck1Mzml7QptB%2FKFsYN9LTs5ybRYoqhKL5KmGKNQ%2B%2BZ8%2FRC6j9wB3GMmxDuFQ7CWVOs7lC7U1wkDftvVSwhx5%2FlgBNj%2FEbLV7E4mserqnbLKO1R%2BfyP1QTXnlxlKHgOPV7%2FpFRd8oR69WMdPIK32WHfDkKUlXHEcGVaXbneoDbn7mAjG3dXOy4zzoADNMMBBJIKYTGVgunucqotwz52NJYo65m2OC9%2FaKpu88f0rLvyRMp5TAlLje9XpMMLuD6bwGOqUBpzkPYMwR9Mjhg3SAdb8BJkUxWXilxmL7N54uOMM02bKpSuUXxE%2BEnZE4uhC0uaBKNZSDP7315XxsHODTPBgLe9BR0cXyqnz%2B9%2Bo0mDGB4Rgni1DPBcS1WSYUxGmwzjVWGyAJ7eCn2HdvQEwHer25jhmxK8CaYDvPbW6N2XV2F5j3udtsUHbamMqpnpcWvt3Wn0kmxzN6orSdrFkDzSgwWe%2FWSPAi&X-Amz-Signature=cafc1cc87636219780f937ca01abcac54d6ee2e4c6ab71a6d5f67d2502c99942&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666CMROKF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYPmZp1D647KJNuUqgGDagyQ3z2B1e2Ku%2B54WSNTCa2QIgTpA0ojBbDMsU90vAlrwZDjfgLgh1lrcwvoSXFvNevCgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG66%2FrWt3kFAeQpDNSrcA3gUvtjEl8koEg4uRT%2FC%2BP9q5x84C9saXHEg0gM8YGJu%2FmfLoMl8%2BlZ2nsZtBdm9zrgXwAN3%2BZsqHhXZlNuBvDf3oXcZUEQ0SjDrut%2B4x3RLBpEqvjU4ATgA1Ya0jaA0nkzRJNfNv4agkGxMsq%2F92qOaLjLbscOtMIqOV3BszSL6etfsuGaOMYvuoOAnTRbqBtDqj4V9KoGiTl3Hs40%2BVlPhCMk%2F6INHMVRZxZMC6ahA7foHHcIS3fpihn4tsQ%2BgNnQ19YMENvfMBmsabM0eQD%2BPlNFIpyaT9jm13xc40zsc7cS5poZS7u%2FdFXqDh%2Fy2467UZlskT%2BKdhuZSebmKWGP6hPmHXdUJmxcVmTx4JhX1rt6r0YymzYfJ2Z%2FpAGkIbhQ%2Bck1Mzml7QptB%2FKFsYN9LTs5ybRYoqhKL5KmGKNQ%2B%2BZ8%2FRC6j9wB3GMmxDuFQ7CWVOs7lC7U1wkDftvVSwhx5%2FlgBNj%2FEbLV7E4mserqnbLKO1R%2BfyP1QTXnlxlKHgOPV7%2FpFRd8oR69WMdPIK32WHfDkKUlXHEcGVaXbneoDbn7mAjG3dXOy4zzoADNMMBBJIKYTGVgunucqotwz52NJYo65m2OC9%2FaKpu88f0rLvyRMp5TAlLje9XpMMLuD6bwGOqUBpzkPYMwR9Mjhg3SAdb8BJkUxWXilxmL7N54uOMM02bKpSuUXxE%2BEnZE4uhC0uaBKNZSDP7315XxsHODTPBgLe9BR0cXyqnz%2B9%2Bo0mDGB4Rgni1DPBcS1WSYUxGmwzjVWGyAJ7eCn2HdvQEwHer25jhmxK8CaYDvPbW6N2XV2F5j3udtsUHbamMqpnpcWvt3Wn0kmxzN6orSdrFkDzSgwWe%2FWSPAi&X-Amz-Signature=bec7dea23dfb2c0c3ee40c747b4a51ccdb8e8b7ae5d360e4a87909c139b1a741&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666CMROKF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYPmZp1D647KJNuUqgGDagyQ3z2B1e2Ku%2B54WSNTCa2QIgTpA0ojBbDMsU90vAlrwZDjfgLgh1lrcwvoSXFvNevCgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG66%2FrWt3kFAeQpDNSrcA3gUvtjEl8koEg4uRT%2FC%2BP9q5x84C9saXHEg0gM8YGJu%2FmfLoMl8%2BlZ2nsZtBdm9zrgXwAN3%2BZsqHhXZlNuBvDf3oXcZUEQ0SjDrut%2B4x3RLBpEqvjU4ATgA1Ya0jaA0nkzRJNfNv4agkGxMsq%2F92qOaLjLbscOtMIqOV3BszSL6etfsuGaOMYvuoOAnTRbqBtDqj4V9KoGiTl3Hs40%2BVlPhCMk%2F6INHMVRZxZMC6ahA7foHHcIS3fpihn4tsQ%2BgNnQ19YMENvfMBmsabM0eQD%2BPlNFIpyaT9jm13xc40zsc7cS5poZS7u%2FdFXqDh%2Fy2467UZlskT%2BKdhuZSebmKWGP6hPmHXdUJmxcVmTx4JhX1rt6r0YymzYfJ2Z%2FpAGkIbhQ%2Bck1Mzml7QptB%2FKFsYN9LTs5ybRYoqhKL5KmGKNQ%2B%2BZ8%2FRC6j9wB3GMmxDuFQ7CWVOs7lC7U1wkDftvVSwhx5%2FlgBNj%2FEbLV7E4mserqnbLKO1R%2BfyP1QTXnlxlKHgOPV7%2FpFRd8oR69WMdPIK32WHfDkKUlXHEcGVaXbneoDbn7mAjG3dXOy4zzoADNMMBBJIKYTGVgunucqotwz52NJYo65m2OC9%2FaKpu88f0rLvyRMp5TAlLje9XpMMLuD6bwGOqUBpzkPYMwR9Mjhg3SAdb8BJkUxWXilxmL7N54uOMM02bKpSuUXxE%2BEnZE4uhC0uaBKNZSDP7315XxsHODTPBgLe9BR0cXyqnz%2B9%2Bo0mDGB4Rgni1DPBcS1WSYUxGmwzjVWGyAJ7eCn2HdvQEwHer25jhmxK8CaYDvPbW6N2XV2F5j3udtsUHbamMqpnpcWvt3Wn0kmxzN6orSdrFkDzSgwWe%2FWSPAi&X-Amz-Signature=48d664f4f33a537da94d38c89ebb2e7070a4adb360a237bac55b41af61ba5cf4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHT3GZC4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaDnQBJGKS0e5K145uSAQjUv8CDJ5vpT4Xm5aK4F7NTQIgVDNNug1LtQTab4aina8f8YJ7ArSGe51Dfe4V64eoB7wqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRXowj%2F7mz%2BlEYPASrcA4NkQ6iiyDCsVlo51SjJ3toMK1TcI8ULGKpyzAL6xN7sYEsEV%2FpkZFPYq%2BR2DIjYcyfoeeEdH3UD%2BMShZYxeCUOJEeluGKjPlY1UozPKH3Q44Hi%2FveeEKjpWpl9g9cIMkgJXmV71dO%2Bz1wkiVxWwmmuOI5ESkiQVth%2F0wvEAis7iAF%2FvBCOIjT265gHKH0tAYh0pw1yccACDVO%2BWQV3jJoREUNYdsSgjzd5aF3gEMZbbiPr5P%2BaKrrjZSRW8TxEYyp90NbmbGPCn5FzZVNMRnaR%2FE5YbhWNK5peBxRVrPURjjiU%2Fdi6sjnxwXTircMNgLKqn0N70n8vmRUk5bTTuopTFGle4wHDOC88y9bOu4Zi9PBpCj12MfZr%2BoqFn9%2FypbHWHzLVBvaA%2BvId1ne3BoQMGhuetSq6nzrkq%2FfO6ipfJzwRATbHo2tIg1SP4fulH03DKSoHJ1XTwSD1hynqSdXWERFWowV9fg6QUQmoPnSfZjMvJG%2F7RYFLWlrDEV5msas1XbI82eAxNWvdDJioAXtpDkPp9ANR7MQRnWxa8iO2UBwD7ivSLEOHv4WU43kfk9zGaS3LMStPm3a3jPcKdYWi1o%2BaF1jJqruuRKPqi1iYYNKPdBp3m14vwWjkmMJKE6bwGOqUBdy4yri%2Bsobxez7yRJQ7noFDzgCi4Lk2jqzxpUINSoO5MTknAnFrqR6VsKvIUD2DTOQT%2FxfK9lfXfmz6e94YRl4S5Q1PuBjquBgq%2B4nUZ1UxMxpl%2F013lLz4aXinHpBRh4gp14hPFweyjPJUsTU92lFx3L5HJi5ij7xm9rkIfk1wSIcI2IZBvpwG46Pm%2FPjuehZDXxTb4heTWNYg7g2S%2BjRS%2B5E53&X-Amz-Signature=02ee0b75c78a82272049585153d5674e950beca91df31b7ab909676834e2b3fb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHT3GZC4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaDnQBJGKS0e5K145uSAQjUv8CDJ5vpT4Xm5aK4F7NTQIgVDNNug1LtQTab4aina8f8YJ7ArSGe51Dfe4V64eoB7wqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRXowj%2F7mz%2BlEYPASrcA4NkQ6iiyDCsVlo51SjJ3toMK1TcI8ULGKpyzAL6xN7sYEsEV%2FpkZFPYq%2BR2DIjYcyfoeeEdH3UD%2BMShZYxeCUOJEeluGKjPlY1UozPKH3Q44Hi%2FveeEKjpWpl9g9cIMkgJXmV71dO%2Bz1wkiVxWwmmuOI5ESkiQVth%2F0wvEAis7iAF%2FvBCOIjT265gHKH0tAYh0pw1yccACDVO%2BWQV3jJoREUNYdsSgjzd5aF3gEMZbbiPr5P%2BaKrrjZSRW8TxEYyp90NbmbGPCn5FzZVNMRnaR%2FE5YbhWNK5peBxRVrPURjjiU%2Fdi6sjnxwXTircMNgLKqn0N70n8vmRUk5bTTuopTFGle4wHDOC88y9bOu4Zi9PBpCj12MfZr%2BoqFn9%2FypbHWHzLVBvaA%2BvId1ne3BoQMGhuetSq6nzrkq%2FfO6ipfJzwRATbHo2tIg1SP4fulH03DKSoHJ1XTwSD1hynqSdXWERFWowV9fg6QUQmoPnSfZjMvJG%2F7RYFLWlrDEV5msas1XbI82eAxNWvdDJioAXtpDkPp9ANR7MQRnWxa8iO2UBwD7ivSLEOHv4WU43kfk9zGaS3LMStPm3a3jPcKdYWi1o%2BaF1jJqruuRKPqi1iYYNKPdBp3m14vwWjkmMJKE6bwGOqUBdy4yri%2Bsobxez7yRJQ7noFDzgCi4Lk2jqzxpUINSoO5MTknAnFrqR6VsKvIUD2DTOQT%2FxfK9lfXfmz6e94YRl4S5Q1PuBjquBgq%2B4nUZ1UxMxpl%2F013lLz4aXinHpBRh4gp14hPFweyjPJUsTU92lFx3L5HJi5ij7xm9rkIfk1wSIcI2IZBvpwG46Pm%2FPjuehZDXxTb4heTWNYg7g2S%2BjRS%2B5E53&X-Amz-Signature=958e01ea4fa6877730ca8272a0fa29b4242bca518d04d6904786245eaf4c7d56&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHT3GZC4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaDnQBJGKS0e5K145uSAQjUv8CDJ5vpT4Xm5aK4F7NTQIgVDNNug1LtQTab4aina8f8YJ7ArSGe51Dfe4V64eoB7wqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRXowj%2F7mz%2BlEYPASrcA4NkQ6iiyDCsVlo51SjJ3toMK1TcI8ULGKpyzAL6xN7sYEsEV%2FpkZFPYq%2BR2DIjYcyfoeeEdH3UD%2BMShZYxeCUOJEeluGKjPlY1UozPKH3Q44Hi%2FveeEKjpWpl9g9cIMkgJXmV71dO%2Bz1wkiVxWwmmuOI5ESkiQVth%2F0wvEAis7iAF%2FvBCOIjT265gHKH0tAYh0pw1yccACDVO%2BWQV3jJoREUNYdsSgjzd5aF3gEMZbbiPr5P%2BaKrrjZSRW8TxEYyp90NbmbGPCn5FzZVNMRnaR%2FE5YbhWNK5peBxRVrPURjjiU%2Fdi6sjnxwXTircMNgLKqn0N70n8vmRUk5bTTuopTFGle4wHDOC88y9bOu4Zi9PBpCj12MfZr%2BoqFn9%2FypbHWHzLVBvaA%2BvId1ne3BoQMGhuetSq6nzrkq%2FfO6ipfJzwRATbHo2tIg1SP4fulH03DKSoHJ1XTwSD1hynqSdXWERFWowV9fg6QUQmoPnSfZjMvJG%2F7RYFLWlrDEV5msas1XbI82eAxNWvdDJioAXtpDkPp9ANR7MQRnWxa8iO2UBwD7ivSLEOHv4WU43kfk9zGaS3LMStPm3a3jPcKdYWi1o%2BaF1jJqruuRKPqi1iYYNKPdBp3m14vwWjkmMJKE6bwGOqUBdy4yri%2Bsobxez7yRJQ7noFDzgCi4Lk2jqzxpUINSoO5MTknAnFrqR6VsKvIUD2DTOQT%2FxfK9lfXfmz6e94YRl4S5Q1PuBjquBgq%2B4nUZ1UxMxpl%2F013lLz4aXinHpBRh4gp14hPFweyjPJUsTU92lFx3L5HJi5ij7xm9rkIfk1wSIcI2IZBvpwG46Pm%2FPjuehZDXxTb4heTWNYg7g2S%2BjRS%2B5E53&X-Amz-Signature=13b79c7f16d76138cdf15a742ce7336f0fbc1b71351c375dc16987cb847a10f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHT3GZC4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaDnQBJGKS0e5K145uSAQjUv8CDJ5vpT4Xm5aK4F7NTQIgVDNNug1LtQTab4aina8f8YJ7ArSGe51Dfe4V64eoB7wqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRXowj%2F7mz%2BlEYPASrcA4NkQ6iiyDCsVlo51SjJ3toMK1TcI8ULGKpyzAL6xN7sYEsEV%2FpkZFPYq%2BR2DIjYcyfoeeEdH3UD%2BMShZYxeCUOJEeluGKjPlY1UozPKH3Q44Hi%2FveeEKjpWpl9g9cIMkgJXmV71dO%2Bz1wkiVxWwmmuOI5ESkiQVth%2F0wvEAis7iAF%2FvBCOIjT265gHKH0tAYh0pw1yccACDVO%2BWQV3jJoREUNYdsSgjzd5aF3gEMZbbiPr5P%2BaKrrjZSRW8TxEYyp90NbmbGPCn5FzZVNMRnaR%2FE5YbhWNK5peBxRVrPURjjiU%2Fdi6sjnxwXTircMNgLKqn0N70n8vmRUk5bTTuopTFGle4wHDOC88y9bOu4Zi9PBpCj12MfZr%2BoqFn9%2FypbHWHzLVBvaA%2BvId1ne3BoQMGhuetSq6nzrkq%2FfO6ipfJzwRATbHo2tIg1SP4fulH03DKSoHJ1XTwSD1hynqSdXWERFWowV9fg6QUQmoPnSfZjMvJG%2F7RYFLWlrDEV5msas1XbI82eAxNWvdDJioAXtpDkPp9ANR7MQRnWxa8iO2UBwD7ivSLEOHv4WU43kfk9zGaS3LMStPm3a3jPcKdYWi1o%2BaF1jJqruuRKPqi1iYYNKPdBp3m14vwWjkmMJKE6bwGOqUBdy4yri%2Bsobxez7yRJQ7noFDzgCi4Lk2jqzxpUINSoO5MTknAnFrqR6VsKvIUD2DTOQT%2FxfK9lfXfmz6e94YRl4S5Q1PuBjquBgq%2B4nUZ1UxMxpl%2F013lLz4aXinHpBRh4gp14hPFweyjPJUsTU92lFx3L5HJi5ij7xm9rkIfk1wSIcI2IZBvpwG46Pm%2FPjuehZDXxTb4heTWNYg7g2S%2BjRS%2B5E53&X-Amz-Signature=42d06ff3eed691c777c9af634b1b61b554b2e7f2d179925217c877593656c68c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHT3GZC4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaDnQBJGKS0e5K145uSAQjUv8CDJ5vpT4Xm5aK4F7NTQIgVDNNug1LtQTab4aina8f8YJ7ArSGe51Dfe4V64eoB7wqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRXowj%2F7mz%2BlEYPASrcA4NkQ6iiyDCsVlo51SjJ3toMK1TcI8ULGKpyzAL6xN7sYEsEV%2FpkZFPYq%2BR2DIjYcyfoeeEdH3UD%2BMShZYxeCUOJEeluGKjPlY1UozPKH3Q44Hi%2FveeEKjpWpl9g9cIMkgJXmV71dO%2Bz1wkiVxWwmmuOI5ESkiQVth%2F0wvEAis7iAF%2FvBCOIjT265gHKH0tAYh0pw1yccACDVO%2BWQV3jJoREUNYdsSgjzd5aF3gEMZbbiPr5P%2BaKrrjZSRW8TxEYyp90NbmbGPCn5FzZVNMRnaR%2FE5YbhWNK5peBxRVrPURjjiU%2Fdi6sjnxwXTircMNgLKqn0N70n8vmRUk5bTTuopTFGle4wHDOC88y9bOu4Zi9PBpCj12MfZr%2BoqFn9%2FypbHWHzLVBvaA%2BvId1ne3BoQMGhuetSq6nzrkq%2FfO6ipfJzwRATbHo2tIg1SP4fulH03DKSoHJ1XTwSD1hynqSdXWERFWowV9fg6QUQmoPnSfZjMvJG%2F7RYFLWlrDEV5msas1XbI82eAxNWvdDJioAXtpDkPp9ANR7MQRnWxa8iO2UBwD7ivSLEOHv4WU43kfk9zGaS3LMStPm3a3jPcKdYWi1o%2BaF1jJqruuRKPqi1iYYNKPdBp3m14vwWjkmMJKE6bwGOqUBdy4yri%2Bsobxez7yRJQ7noFDzgCi4Lk2jqzxpUINSoO5MTknAnFrqR6VsKvIUD2DTOQT%2FxfK9lfXfmz6e94YRl4S5Q1PuBjquBgq%2B4nUZ1UxMxpl%2F013lLz4aXinHpBRh4gp14hPFweyjPJUsTU92lFx3L5HJi5ij7xm9rkIfk1wSIcI2IZBvpwG46Pm%2FPjuehZDXxTb4heTWNYg7g2S%2BjRS%2B5E53&X-Amz-Signature=3d119e126c6342e6c013d4e5334678352e46aaf29357a5b884edd42e33319eb7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHT3GZC4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaDnQBJGKS0e5K145uSAQjUv8CDJ5vpT4Xm5aK4F7NTQIgVDNNug1LtQTab4aina8f8YJ7ArSGe51Dfe4V64eoB7wqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRXowj%2F7mz%2BlEYPASrcA4NkQ6iiyDCsVlo51SjJ3toMK1TcI8ULGKpyzAL6xN7sYEsEV%2FpkZFPYq%2BR2DIjYcyfoeeEdH3UD%2BMShZYxeCUOJEeluGKjPlY1UozPKH3Q44Hi%2FveeEKjpWpl9g9cIMkgJXmV71dO%2Bz1wkiVxWwmmuOI5ESkiQVth%2F0wvEAis7iAF%2FvBCOIjT265gHKH0tAYh0pw1yccACDVO%2BWQV3jJoREUNYdsSgjzd5aF3gEMZbbiPr5P%2BaKrrjZSRW8TxEYyp90NbmbGPCn5FzZVNMRnaR%2FE5YbhWNK5peBxRVrPURjjiU%2Fdi6sjnxwXTircMNgLKqn0N70n8vmRUk5bTTuopTFGle4wHDOC88y9bOu4Zi9PBpCj12MfZr%2BoqFn9%2FypbHWHzLVBvaA%2BvId1ne3BoQMGhuetSq6nzrkq%2FfO6ipfJzwRATbHo2tIg1SP4fulH03DKSoHJ1XTwSD1hynqSdXWERFWowV9fg6QUQmoPnSfZjMvJG%2F7RYFLWlrDEV5msas1XbI82eAxNWvdDJioAXtpDkPp9ANR7MQRnWxa8iO2UBwD7ivSLEOHv4WU43kfk9zGaS3LMStPm3a3jPcKdYWi1o%2BaF1jJqruuRKPqi1iYYNKPdBp3m14vwWjkmMJKE6bwGOqUBdy4yri%2Bsobxez7yRJQ7noFDzgCi4Lk2jqzxpUINSoO5MTknAnFrqR6VsKvIUD2DTOQT%2FxfK9lfXfmz6e94YRl4S5Q1PuBjquBgq%2B4nUZ1UxMxpl%2F013lLz4aXinHpBRh4gp14hPFweyjPJUsTU92lFx3L5HJi5ij7xm9rkIfk1wSIcI2IZBvpwG46Pm%2FPjuehZDXxTb4heTWNYg7g2S%2BjRS%2B5E53&X-Amz-Signature=0832909d790eb13738c4e66caf62bb5d8f28ff6cce9928319cda630bdd9ab491&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFAHMMAK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FwRg6rzvykwk9pyGHXQ%2BgswfrBAQHsr%2B3vU0S0Ox9XAIgNsR1QkUjOTIwSVwmJEq0BvGhi1%2F26EY7PAWnt%2Bngo%2BMqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFlCc5oMSgefUnZNrCrcA%2Blmp1lyDS3LSDtVPBuYJqMJZ4z4sI2zwctBjaOwZw29mgCPwKVyU7TC%2FBv8XeTo5AEi2egtoZtrvRXEXCSXLKFDvrgEK5ajo85Es2bxbb8HsIl1YF2iI4DzQByWD%2B7jzFgcKWJlJBlBR%2FGf50QfB%2F%2FcE7kWPw6PVWij%2Fk9xNaESoo5fm%2BpKldTYyULdHofuhPUndx21PKkhgHvhwrKmY1xs7ipz2K13RWoo0D4YZMMx2gQcgT4ZXBw2iN6vklp5daayyO8jkk2tk1nQ0D%2FRUhJm4MItcCMVkuMIT65qI76VBcRbtuTCBYL%2BTvz4ixrAXRvBSGJkDytf2wkAECCrSFyAlQwB7%2Bk7Z4j5EqmMJWqdE8IbErXHf%2BuCDDMoEAlpI8NG6GXWWPNnneEa3TnzZm1vlhTEFlDAttheVPj%2FwVaEBiZPauCzrHS8cSwpQfZO7M3NSrAB0YZgzLf%2FouI%2F5MUF7v97qOs9zEf5JT9xIlAyuTZHGCRtSk829E%2BEdJ3ZGX2iv3JiKD%2FhumdSzyWa6kTRY3BykRLQemss6FPUbh%2FrCLxfACV01Vu2jNZEwN%2BcFPNP37CNFT4slm2tCisXKTSy2PJ0ACdpsJwBJLJ2ePSnhfI8G0lSNiUVN1jVMNeD6bwGOqUB0IXqCkjZFKvr9BH07hiEmL4LmjO7jUedRWq9R3h7D4aAFDuU9K9E%2F0SY%2FP1wwfKFoxo3AozpilA9kDH5qjh8iSn9IGdj4Qh%2BxCLv2O%2F6%2FW%2BzsSwv4zrdca0%2B%2Bot8qL%2BboOaQlu46lwEGcdxeOwSYmqh5vybVOnZ8zyy1sNUljNJZJ893BRgXdlPeFDsjn0AJqe1DCxe3nGEO%2Bb3184C%2BSzB%2Bvp1x&X-Amz-Signature=080e2031b777fbcc172cd23e72ada2c5c191ac44481d6475a7df7030993fcbfb&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO6TQSLT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDt6C2u%2FaxafYltO6ALhKCOVA3ULw3XKcMvTaPiHiRrnwIhAPG5DhmTuS1q6K3zfW%2BId%2FMsMOhZPeVXBGgltlqnx4b6KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxweagAW1N1l6CeYAQq3APowt%2FxRAFBY8AEHeej6xiWx4ODioNs%2FW1b2oJlEzzP9G6kS3eDv1WLbWRDGlm4bGFxBa9WxVxMizM8St5XP6OUezaOLQHUtIkvd%2FJJLmnt%2BBA4qcn7HEdTId5t7dmH6jAqRvqW1NKw9%2F5fTZI7sj5kp42y1ECbF%2FfRPSe92owQHSFNvn0Kk9EVA9zYDPX4DJbV13P5IGb2xmln2U79EGVvngch200byDBnwW8ammPa0gR1UCp2nZlHpcxsMjS3%2FrOa6e9N7UuaNKLCDzy8g0HObEAlgzH9g96pqkTN7mfV9lG1mdsKiuZQLv52k2SlkhMfEbtyvBL3BwbyzDY8Fs%2FJdBcLJzIT%2FhMrU7cHqDQFShczDsO7v52J3sZVLEJ5PDoIRSpNkhxZKM8BnHhXLc6%2BchnYCA6YdWadvS2fstT1vo7vK3yv2C6c9Vf6DGVm0RtBjN723Gym0pmgKWOk2y5QrvWZFhxgsdcF5jUN8XjJdR1JidxBxS4f1qfPP06PSVmKXElkxFFtslzmru3Bf83yyC4SGXl5YcdxQjaSUoAZKD%2BRfMxfJFBfteYZW6iGG40Cm42yGwFNTMiwgvrzDA00ABXtM1zvAJideEyG%2B95NtfFOBUbQR7vtBCCSfjDCg%2Bm8BjqkAdYRne8aK9a6rqFu%2BL8LExoto9oDZekmQX5bPhs7kAGPBwPKLw9GIBLQbbpA6AV5kR8g%2BmtgDbqaB6seHht4654dSBdnxByxaHXq6hvzC4bXrJSGB3i1UN%2FCgiY2%2Bwf%2F01IwIZ%2Fk%2BMGvzrEiE12zMa0zuGxlm5e%2F%2FAEhdtu6hF6g27qepsxD9%2B7vIkxyJL6Nm403gcUxvjNfvX8oUVqC75%2BKNXkn&X-Amz-Signature=d6549b857be60b0f4904774f5ddf50a899766fa51ee40d64d61b6d28dc30f7e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHT3GZC4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaDnQBJGKS0e5K145uSAQjUv8CDJ5vpT4Xm5aK4F7NTQIgVDNNug1LtQTab4aina8f8YJ7ArSGe51Dfe4V64eoB7wqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRXowj%2F7mz%2BlEYPASrcA4NkQ6iiyDCsVlo51SjJ3toMK1TcI8ULGKpyzAL6xN7sYEsEV%2FpkZFPYq%2BR2DIjYcyfoeeEdH3UD%2BMShZYxeCUOJEeluGKjPlY1UozPKH3Q44Hi%2FveeEKjpWpl9g9cIMkgJXmV71dO%2Bz1wkiVxWwmmuOI5ESkiQVth%2F0wvEAis7iAF%2FvBCOIjT265gHKH0tAYh0pw1yccACDVO%2BWQV3jJoREUNYdsSgjzd5aF3gEMZbbiPr5P%2BaKrrjZSRW8TxEYyp90NbmbGPCn5FzZVNMRnaR%2FE5YbhWNK5peBxRVrPURjjiU%2Fdi6sjnxwXTircMNgLKqn0N70n8vmRUk5bTTuopTFGle4wHDOC88y9bOu4Zi9PBpCj12MfZr%2BoqFn9%2FypbHWHzLVBvaA%2BvId1ne3BoQMGhuetSq6nzrkq%2FfO6ipfJzwRATbHo2tIg1SP4fulH03DKSoHJ1XTwSD1hynqSdXWERFWowV9fg6QUQmoPnSfZjMvJG%2F7RYFLWlrDEV5msas1XbI82eAxNWvdDJioAXtpDkPp9ANR7MQRnWxa8iO2UBwD7ivSLEOHv4WU43kfk9zGaS3LMStPm3a3jPcKdYWi1o%2BaF1jJqruuRKPqi1iYYNKPdBp3m14vwWjkmMJKE6bwGOqUBdy4yri%2Bsobxez7yRJQ7noFDzgCi4Lk2jqzxpUINSoO5MTknAnFrqR6VsKvIUD2DTOQT%2FxfK9lfXfmz6e94YRl4S5Q1PuBjquBgq%2B4nUZ1UxMxpl%2F013lLz4aXinHpBRh4gp14hPFweyjPJUsTU92lFx3L5HJi5ij7xm9rkIfk1wSIcI2IZBvpwG46Pm%2FPjuehZDXxTb4heTWNYg7g2S%2BjRS%2B5E53&X-Amz-Signature=b8fba305e7f0a1e88ab6caecf309edcf454509090f0b866f763ac6c3db5a83cd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHT3GZC4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaDnQBJGKS0e5K145uSAQjUv8CDJ5vpT4Xm5aK4F7NTQIgVDNNug1LtQTab4aina8f8YJ7ArSGe51Dfe4V64eoB7wqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRXowj%2F7mz%2BlEYPASrcA4NkQ6iiyDCsVlo51SjJ3toMK1TcI8ULGKpyzAL6xN7sYEsEV%2FpkZFPYq%2BR2DIjYcyfoeeEdH3UD%2BMShZYxeCUOJEeluGKjPlY1UozPKH3Q44Hi%2FveeEKjpWpl9g9cIMkgJXmV71dO%2Bz1wkiVxWwmmuOI5ESkiQVth%2F0wvEAis7iAF%2FvBCOIjT265gHKH0tAYh0pw1yccACDVO%2BWQV3jJoREUNYdsSgjzd5aF3gEMZbbiPr5P%2BaKrrjZSRW8TxEYyp90NbmbGPCn5FzZVNMRnaR%2FE5YbhWNK5peBxRVrPURjjiU%2Fdi6sjnxwXTircMNgLKqn0N70n8vmRUk5bTTuopTFGle4wHDOC88y9bOu4Zi9PBpCj12MfZr%2BoqFn9%2FypbHWHzLVBvaA%2BvId1ne3BoQMGhuetSq6nzrkq%2FfO6ipfJzwRATbHo2tIg1SP4fulH03DKSoHJ1XTwSD1hynqSdXWERFWowV9fg6QUQmoPnSfZjMvJG%2F7RYFLWlrDEV5msas1XbI82eAxNWvdDJioAXtpDkPp9ANR7MQRnWxa8iO2UBwD7ivSLEOHv4WU43kfk9zGaS3LMStPm3a3jPcKdYWi1o%2BaF1jJqruuRKPqi1iYYNKPdBp3m14vwWjkmMJKE6bwGOqUBdy4yri%2Bsobxez7yRJQ7noFDzgCi4Lk2jqzxpUINSoO5MTknAnFrqR6VsKvIUD2DTOQT%2FxfK9lfXfmz6e94YRl4S5Q1PuBjquBgq%2B4nUZ1UxMxpl%2F013lLz4aXinHpBRh4gp14hPFweyjPJUsTU92lFx3L5HJi5ij7xm9rkIfk1wSIcI2IZBvpwG46Pm%2FPjuehZDXxTb4heTWNYg7g2S%2BjRS%2B5E53&X-Amz-Signature=c5b65a18c44a77b7733e5d9723e727822c9ab918f6b2eee3099fbb502ba453d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHT3GZC4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaDnQBJGKS0e5K145uSAQjUv8CDJ5vpT4Xm5aK4F7NTQIgVDNNug1LtQTab4aina8f8YJ7ArSGe51Dfe4V64eoB7wqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRXowj%2F7mz%2BlEYPASrcA4NkQ6iiyDCsVlo51SjJ3toMK1TcI8ULGKpyzAL6xN7sYEsEV%2FpkZFPYq%2BR2DIjYcyfoeeEdH3UD%2BMShZYxeCUOJEeluGKjPlY1UozPKH3Q44Hi%2FveeEKjpWpl9g9cIMkgJXmV71dO%2Bz1wkiVxWwmmuOI5ESkiQVth%2F0wvEAis7iAF%2FvBCOIjT265gHKH0tAYh0pw1yccACDVO%2BWQV3jJoREUNYdsSgjzd5aF3gEMZbbiPr5P%2BaKrrjZSRW8TxEYyp90NbmbGPCn5FzZVNMRnaR%2FE5YbhWNK5peBxRVrPURjjiU%2Fdi6sjnxwXTircMNgLKqn0N70n8vmRUk5bTTuopTFGle4wHDOC88y9bOu4Zi9PBpCj12MfZr%2BoqFn9%2FypbHWHzLVBvaA%2BvId1ne3BoQMGhuetSq6nzrkq%2FfO6ipfJzwRATbHo2tIg1SP4fulH03DKSoHJ1XTwSD1hynqSdXWERFWowV9fg6QUQmoPnSfZjMvJG%2F7RYFLWlrDEV5msas1XbI82eAxNWvdDJioAXtpDkPp9ANR7MQRnWxa8iO2UBwD7ivSLEOHv4WU43kfk9zGaS3LMStPm3a3jPcKdYWi1o%2BaF1jJqruuRKPqi1iYYNKPdBp3m14vwWjkmMJKE6bwGOqUBdy4yri%2Bsobxez7yRJQ7noFDzgCi4Lk2jqzxpUINSoO5MTknAnFrqR6VsKvIUD2DTOQT%2FxfK9lfXfmz6e94YRl4S5Q1PuBjquBgq%2B4nUZ1UxMxpl%2F013lLz4aXinHpBRh4gp14hPFweyjPJUsTU92lFx3L5HJi5ij7xm9rkIfk1wSIcI2IZBvpwG46Pm%2FPjuehZDXxTb4heTWNYg7g2S%2BjRS%2B5E53&X-Amz-Signature=21b761b1d67726922cb1d2b989ed77ee3286c253786f7ba7ab24cf51a2a99a70&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R56P7WL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDlaGWoNG%2Bmz7yXm7rjijA5mIqgDOYqr2udXAa8%2F564nAiEAv3BAOMuYzC1BP%2BKrhxpcnI7MqLaDyUn57tqa3LKkVfwqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOtWObG7ECbkymCWsCrcA1XZ771zuneuBgUAnxOEGoypN4ec3NWFpsZqObg3mglnlGo1hbtybOVJIDyCmR1NkRfp0dU0qMfk49VleYfarrBX5vt1yas4FrIXTNCKqy7OLsiOcnlBPBs9vs3ZSyCV0%2Fwq7UUhkk%2F5PU47Vf3W5Y4U%2FM2%2Bb4QDUsFE95oRkpCoRRoRxa%2Fc9ntEdrZn30cUX4EPdJ5egKJnsoZAeJKV6euEWk57ijVb0eJbSvNTyu1%2FsjobYQuq7fAbgo0HSiLjM3JxnUOoksPou7namsX49HM6OVUjjcnb0oUMHdFnpQ3yXi1JIQYV22GorZSUqcqIWVtffhgPrsmBucIE5%2FCBbYiQJqx6JUeNeo7eDInFajI0PkSiAJNfRef8rntguN8z7HMQVygPokMy990VcPAtDE1nUbp%2BgEASc9EmwvQCiN0dxn9NjFN0xENm5SjT0YD8mnmtGI87yClLP9%2FKcbsDENZi%2FknZWIaT1dDjV%2BEUhf0h%2B%2FFlzk9KoqcYWNLuXIrUzOnl95IiPHav5s%2F5k6JX2fcT8eucSeQtKfMyJxzGDfO7%2FVJhWbwpMHFCwGC52CqqIPu%2BtY9F397%2Bp6cX7C4ixtnli1Ak2XcUaFEoJEMUZnmcwA7D1Qu%2B9hEkZ6b%2FMLSD6bwGOqUBGC6vdiAn6qks8cdUrGW9Eqdt0tbj5VeRupP3MOdOtH8rYpaM4R1rNvnmJVYw%2Fn5neXwfp8ZUq%2B05L1wDHMdtlF6fytT7H%2ByQLs2DRK276B9pejniKL69uDVYSkIXE0%2Fpa%2FQ4k%2Fw4ALQAMzOhIwk9uCtC1MwoW0C3cq0pxCP0%2BAWe5FcSrmgoZOGUDCGihInRlCZ%2Bhr5dLzglTb3u%2FYWtHcadQrm%2B&X-Amz-Signature=f4df3c02ba0b14644b743b132599428a3bc57546c95260bbcbd1b90649a635b4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTNULG4W%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICCEXS45A3cZ9KRZbWxynVjLbPy68ddGVtBysAPBn9nUAiEAqZAMeTuHrhP9wSTlXr656R8m6U5kzytQ9PRBUc5XbuMqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPuaAJ2QUJKMFN%2FBhCrcA4A9%2F1mLNi%2Fc%2B6NplyjezDPhJtgtj5gfECW7zBF0AKQK8aw7iDFiYRmbW1QvLb05WOXqvjudRGqJz2MZI0PjzItUX8Fyg7bUpcGQwE9LZ2CwHphmzs%2F%2Bo6MblL6yJ%2FUWneiq%2Fw2n%2F4EKD1U8Hr8V9qoAs0AiqwsNotUpQYmSSpkYIX0u76%2BZFJmz37zTrxpbQZ6FAbC%2BrdZ%2FmBMsx8uMw%2F3p90fgVLAKmgnVJRgllceP1z8PlQ5L3mtscR90JNBIzfKTQk0v4Vbyx2Rdpbp3LvrTQf7tabTov0zCxNKGfUSiKSdblQ44izWLDHQOu2XbtDsUwvns9rPGLiP7oPCsTw702TNH5dyZsKqNFBtyb2P347bZnpc5mCmofB%2FxglIh5n6hPWvQoIyTCUeoFIUTuk7iXNVYoGgrfUSJ8q3uBOYrHGUwt0WEgs315GAwNznSSNO9oIqs9WM4ksPbH9aw86lNjLQx88Y0TzFPibJOkNn6uL396avsH5BEdiSj8MK3V867XYpCkl6IElYO0VB7Uch0rsO1NUCbE9DJu2SeBVv75CtwASsxosTDAr53mWu8rMu9Y3Ta9B7LgtuiuH3cfvOZEOiywlT7cJbLrUl0QJowfXuxUDYWmWRPpw04MNeD6bwGOqUB1ZyCh19qPPceX2T4zXJiN%2BFRPaZS40sLo9L%2FDognfsM%2FpP4JFfu9fvhVy6m02FqA3JDvV6LfO9wQjHbBqVyRordDYGXPq12hZMF1T9E2gc%2B334hw19B9yUYouSq6hAAXJi8CC6hSWChFkQ2HjySuaiJEOEGFywzzJoZR4P7SkeSrjxRCHRJ%2BRDRwSx%2BeFB3VODZij34ERsXScyNbwQFBox6EsFDR&X-Amz-Signature=4f60a62e2dc6a13203a8477ac5e277c449f37cce27b1d456e5b3c76b4705b69b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHAXCEFV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BPnBHifWRMt1t1PuCmk27lzwVcW9uCdAs%2FGudCR0ndwIhAMvuoLB2iFIZJ6QYqFFnUQ%2BKsWpKlN6DspzUvixhNRuGKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz4mEJmEbDZnExxiHEq3APbNmN6oGfAZv577N9tpRQY3HnzEfFprBNPXyo6o1Qo25tXz%2BD3ElXfzDG%2FO9oN%2B03QOxLQEFn4Bhy%2BKN4UlUXyyYgrIY8OpHGvKBmQzxQTHZqO5ssz2Hw1dHBVlOFYtHF4noxS%2FnNpBEN7jZkhSZqJoC42Oi8RWx3Zrz3Je%2BS%2FwTN3bb%2FWDxnR5svw7%2BXMBMjw463vqn6bWiYxtrZXkyCSO%2BEjW33P3spKM%2FXse4NgY8%2FKbwubrBNH1y3%2B4gJ3mIZJF%2BQGInlDFxOmLAC3M6rd%2BaxDqT5jMpPhtvytIsJKph%2F1hRwX5hf2VRgzYM2FC%2FU0hD0knZIjDFd8j4n78kv5%2FchTcaMH9zPKRwMhIxoQR%2BxZQHlcKyfipc84Ut40lBvDKOfQAyM3v8TAz3LPs%2FfcYS7AhcYi65kN4gcMlhrU2nTLBUs6QLKVWnp9Sp1njkT5o0L268ZVCj%2FIEJuv4GZXWtC1HkwlABpKj%2ByfOrAiJNIcyfiPda5%2FYNux9sn8cQnIsUxjeHvJAyY6mbUqVF8EPgEbhyiORm8FxM00A5d%2BaoPywe%2B6Zt%2BHX%2F7pBYG0u%2BUgh2EfMJhnhkGc2pgiEGVF6L%2BgipvGdvZeKNwzUrd5RPghfIcBJcn6qPmt8DCGhOm8BjqkAXRCeOKuKrZm2kwMztIemDMLaVA4hlyZ8s5ysCvrUNbRfwL7tFFR245M1lpGYphg2uRFm%2B6ESgFXjtKkavst2pqgEAcKyCOCKs0pQImTitOFEEv4k7LeUjLE1FIC0iOVwNPSeUwq3KXKbZO%2FID7d5P%2BanY1NoMSqVLAXSAOVtGoe4CzzKEzrXqLgUYXj8HXOxmhDug%2BZ0jfI69l1YWvC6r1ZmAs2&X-Amz-Signature=35147bc3d6d5b20e0a92a89c6d4b7cacec67f63f8f9ecf56a0d704dcb6282273&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLDNKKG7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClPnxZD3TkHS2ummr7UQfBjAsSUoPoDfeXYokxTbKxkAiEAzJ6LDHLWzMB6SviU6WWkdiBt6kU7k4CEuxDyVT3BHd8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHadvkxMZcll06VWbircA3lNLnqftjl9nkJiRp4vYw%2BmUlAI1htVg%2BOR5iSTsZjQftH%2FEpX6sOc1oPHymmmwG9v42ilNTVPhp83m%2Byr%2FJqbL63I5p8HccWOETQjkrMhrj0PDe9hNbCTLRoM4GpLPohBPRbSqIBAj1iNyMlCa%2FlUlv25mydoqdmDer76iR0%2FE7MpXzxfSbUE2lSzwDFipZAg%2BMpnCq8LOZJs9l75rkyFsSOCvvAu8%2FGO8uIQ1jKSmHITA2IflLVyPI6TUtSECylvc5A%2BknxiXqIhl7tr1ULlfj4691JzKJ7Lc%2FaskQ0gbqpM%2FjC%2Fhh0OkNOytfc%2B2njYKgQ1g6kRlTfE63Nv4eXhAlE%2FofCzpuhVoKtfpE3NCfYr3WHq3uWby8mv5THIQ0XMNxoSfmM40MEpDTMr5FjVwoDkuPs17t1RM7wec0VKdWNDjYb7jhC6knSRCJppEVO4HfBv6I5wBtTuL1aSXeRY5OZgrN1hVyXGacNA1nAObKnAPikDlxPeXX69dFwvHQJfsTP2TLwoY%2FPXd0WfoMdKxKP5dLkVatg1W8kAPyn5lNrHrfJsLlLG%2BqhXoh9XJZR5g4sKmDYThMQ%2BTwNiVhoQt4Ks%2B4MPuHkwgU4GcL1ni2SdDhRD7n5hnPNwtMOCD6bwGOqUBiJec%2FIZwNSkUADNeF7doZgU7rS%2BLTkXsYAAZzuHOP%2FFQ2kt1Ki9yzVQhRyPer0VUEgkfByU7OHlTjEk48VSVF2JrYLPHiPO6s1m%2F6dxxORD0UgWN%2BHfALduvIQtCgOUSVXo7RNUKr0TK2h5jT5GmV1ERrxnqI%2BmfVFOtahdobq3nzuBuU552amm3KVKg6YmHIXhJWHKvus85MpdSGGC3pAMOqfb7&X-Amz-Signature=e6518eb8a79899fcc189a3411cb381ab5f741b2f22f363624d2e833818d24fd5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLDNKKG7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIClPnxZD3TkHS2ummr7UQfBjAsSUoPoDfeXYokxTbKxkAiEAzJ6LDHLWzMB6SviU6WWkdiBt6kU7k4CEuxDyVT3BHd8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHadvkxMZcll06VWbircA3lNLnqftjl9nkJiRp4vYw%2BmUlAI1htVg%2BOR5iSTsZjQftH%2FEpX6sOc1oPHymmmwG9v42ilNTVPhp83m%2Byr%2FJqbL63I5p8HccWOETQjkrMhrj0PDe9hNbCTLRoM4GpLPohBPRbSqIBAj1iNyMlCa%2FlUlv25mydoqdmDer76iR0%2FE7MpXzxfSbUE2lSzwDFipZAg%2BMpnCq8LOZJs9l75rkyFsSOCvvAu8%2FGO8uIQ1jKSmHITA2IflLVyPI6TUtSECylvc5A%2BknxiXqIhl7tr1ULlfj4691JzKJ7Lc%2FaskQ0gbqpM%2FjC%2Fhh0OkNOytfc%2B2njYKgQ1g6kRlTfE63Nv4eXhAlE%2FofCzpuhVoKtfpE3NCfYr3WHq3uWby8mv5THIQ0XMNxoSfmM40MEpDTMr5FjVwoDkuPs17t1RM7wec0VKdWNDjYb7jhC6knSRCJppEVO4HfBv6I5wBtTuL1aSXeRY5OZgrN1hVyXGacNA1nAObKnAPikDlxPeXX69dFwvHQJfsTP2TLwoY%2FPXd0WfoMdKxKP5dLkVatg1W8kAPyn5lNrHrfJsLlLG%2BqhXoh9XJZR5g4sKmDYThMQ%2BTwNiVhoQt4Ks%2B4MPuHkwgU4GcL1ni2SdDhRD7n5hnPNwtMOCD6bwGOqUBiJec%2FIZwNSkUADNeF7doZgU7rS%2BLTkXsYAAZzuHOP%2FFQ2kt1Ki9yzVQhRyPer0VUEgkfByU7OHlTjEk48VSVF2JrYLPHiPO6s1m%2F6dxxORD0UgWN%2BHfALduvIQtCgOUSVXo7RNUKr0TK2h5jT5GmV1ERrxnqI%2BmfVFOtahdobq3nzuBuU552amm3KVKg6YmHIXhJWHKvus85MpdSGGC3pAMOqfb7&X-Amz-Signature=ebf53a041c80b0b538146de606d2197b88e1b23c4ce2c9edb47b171df30cbc42&X-Amz-SignedHeaders=host&x-id=GetObject)

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
