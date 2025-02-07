

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHNTL6XX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCrhpIIdYP7VepAn11kkrana06xrOVvBKNylvM8FOvrJgIhAMJk0TYGQ41Pw2wu5JjFVq5OYktBOsVan8QnQpGV2iqxKv8DCHUQABoMNjM3NDIzMTgzODA1Igw3OkD%2Bx9TEjbSE8egq3AOXr33C5J8i33KdSF0ofDTsQba%2F1IM3g4j%2FDkp1wHUXJbJkTKVIkb8ZpOd5Mq%2BytVBkK2TyoFDVKalGsr1mmUbM4u4g25wUwQ8uPPLrzrB9UkXugzSOWAn1XL29YCJTtPgIGyiozZMMtgXVUmApDRhGUDzHKsQh405FwWaj0u87Y2DS4D4OF%2BKQGMinrkm53tSc3B1gjeVZJMNRrD%2BtijcpHyC%2FsvbliJ%2Bz7%2FQGIx9SivknHPI8p6x6i%2BBkD4Rv8xJYeLEqsqt7DTvnUSNpGL0YIDem1Gquyh4sbTsK6XOA8GurWaUMuwsek6pZt8DL3RvV11%2FlMme5ey297KVNz7ndapvuz6edtr%2BCw4eDCqpD6%2BLMGGP41ghbBnxYjxf3Nnr2bw0WsNmsf3hLZlxZH6R1BZ7sOwIqDe2iilwNl3nlfaRW2j7nEnbnONTXByt8ObIBWsOZ2ReV9kEh%2BAYJym5Sgl8LN9%2F9JK%2F1xDP0dymlgMSopEGyvHkfi5RQ2J0WeQOJH8i7e0NyX5uPW3M8SwT4Q5n1pVndWrQacR1FJxRYICN0kkA5g2sg%2BEcHy4xVTu5bKLIhwU4%2BviiW0f0PqNG4h0hDTHgo9JkJ92EowofTD9kOMD3QRpXXTAkxsDCn8Je9BjqkAXCu5AD%2FP3s9tElKbrntcRf24cDyT2t5D5lXkJPvbKlZAI6og%2FrfRwcS%2B%2B1rRHgd7wslyb2%2BMhvTpWohY87b1MFGef1N5GktWAaGpnqRl4cTJjBYeyGzmOBuRGEmH9Yssw%2BywzCXOF1IozUbWTtdrP%2B91MF26wOcXC8JFh%2FGI6dinCK6S4OuCI4L4ZiVtJ5VW2S%2BH%2FmK5ILNhFpZTTFREAtQ%2F6Ic&X-Amz-Signature=de76313b5f42e4afd5f60adad9a42ad9e1f342d0c063fe5ecad859dc37fa65f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHNTL6XX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCrhpIIdYP7VepAn11kkrana06xrOVvBKNylvM8FOvrJgIhAMJk0TYGQ41Pw2wu5JjFVq5OYktBOsVan8QnQpGV2iqxKv8DCHUQABoMNjM3NDIzMTgzODA1Igw3OkD%2Bx9TEjbSE8egq3AOXr33C5J8i33KdSF0ofDTsQba%2F1IM3g4j%2FDkp1wHUXJbJkTKVIkb8ZpOd5Mq%2BytVBkK2TyoFDVKalGsr1mmUbM4u4g25wUwQ8uPPLrzrB9UkXugzSOWAn1XL29YCJTtPgIGyiozZMMtgXVUmApDRhGUDzHKsQh405FwWaj0u87Y2DS4D4OF%2BKQGMinrkm53tSc3B1gjeVZJMNRrD%2BtijcpHyC%2FsvbliJ%2Bz7%2FQGIx9SivknHPI8p6x6i%2BBkD4Rv8xJYeLEqsqt7DTvnUSNpGL0YIDem1Gquyh4sbTsK6XOA8GurWaUMuwsek6pZt8DL3RvV11%2FlMme5ey297KVNz7ndapvuz6edtr%2BCw4eDCqpD6%2BLMGGP41ghbBnxYjxf3Nnr2bw0WsNmsf3hLZlxZH6R1BZ7sOwIqDe2iilwNl3nlfaRW2j7nEnbnONTXByt8ObIBWsOZ2ReV9kEh%2BAYJym5Sgl8LN9%2F9JK%2F1xDP0dymlgMSopEGyvHkfi5RQ2J0WeQOJH8i7e0NyX5uPW3M8SwT4Q5n1pVndWrQacR1FJxRYICN0kkA5g2sg%2BEcHy4xVTu5bKLIhwU4%2BviiW0f0PqNG4h0hDTHgo9JkJ92EowofTD9kOMD3QRpXXTAkxsDCn8Je9BjqkAXCu5AD%2FP3s9tElKbrntcRf24cDyT2t5D5lXkJPvbKlZAI6og%2FrfRwcS%2B%2B1rRHgd7wslyb2%2BMhvTpWohY87b1MFGef1N5GktWAaGpnqRl4cTJjBYeyGzmOBuRGEmH9Yssw%2BywzCXOF1IozUbWTtdrP%2B91MF26wOcXC8JFh%2FGI6dinCK6S4OuCI4L4ZiVtJ5VW2S%2BH%2FmK5ILNhFpZTTFREAtQ%2F6Ic&X-Amz-Signature=02cbbf866ef8c026c080585c525e3bfcb054da7b86c88b814d301d969f8e00df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHNTL6XX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCrhpIIdYP7VepAn11kkrana06xrOVvBKNylvM8FOvrJgIhAMJk0TYGQ41Pw2wu5JjFVq5OYktBOsVan8QnQpGV2iqxKv8DCHUQABoMNjM3NDIzMTgzODA1Igw3OkD%2Bx9TEjbSE8egq3AOXr33C5J8i33KdSF0ofDTsQba%2F1IM3g4j%2FDkp1wHUXJbJkTKVIkb8ZpOd5Mq%2BytVBkK2TyoFDVKalGsr1mmUbM4u4g25wUwQ8uPPLrzrB9UkXugzSOWAn1XL29YCJTtPgIGyiozZMMtgXVUmApDRhGUDzHKsQh405FwWaj0u87Y2DS4D4OF%2BKQGMinrkm53tSc3B1gjeVZJMNRrD%2BtijcpHyC%2FsvbliJ%2Bz7%2FQGIx9SivknHPI8p6x6i%2BBkD4Rv8xJYeLEqsqt7DTvnUSNpGL0YIDem1Gquyh4sbTsK6XOA8GurWaUMuwsek6pZt8DL3RvV11%2FlMme5ey297KVNz7ndapvuz6edtr%2BCw4eDCqpD6%2BLMGGP41ghbBnxYjxf3Nnr2bw0WsNmsf3hLZlxZH6R1BZ7sOwIqDe2iilwNl3nlfaRW2j7nEnbnONTXByt8ObIBWsOZ2ReV9kEh%2BAYJym5Sgl8LN9%2F9JK%2F1xDP0dymlgMSopEGyvHkfi5RQ2J0WeQOJH8i7e0NyX5uPW3M8SwT4Q5n1pVndWrQacR1FJxRYICN0kkA5g2sg%2BEcHy4xVTu5bKLIhwU4%2BviiW0f0PqNG4h0hDTHgo9JkJ92EowofTD9kOMD3QRpXXTAkxsDCn8Je9BjqkAXCu5AD%2FP3s9tElKbrntcRf24cDyT2t5D5lXkJPvbKlZAI6og%2FrfRwcS%2B%2B1rRHgd7wslyb2%2BMhvTpWohY87b1MFGef1N5GktWAaGpnqRl4cTJjBYeyGzmOBuRGEmH9Yssw%2BywzCXOF1IozUbWTtdrP%2B91MF26wOcXC8JFh%2FGI6dinCK6S4OuCI4L4ZiVtJ5VW2S%2BH%2FmK5ILNhFpZTTFREAtQ%2F6Ic&X-Amz-Signature=5ba1408a3b0019aba6509e754004807fc47b0ac0b4018498e4769faa268866df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQUFEJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQC5frH0qJNhSnKXuNsJBMe%2FmlYCsH7gId1OB267PliWqAIhAKbXxlveecEQbGNUbsUDai72VJ3SExyWIUsx5y7JVfk7Kv8DCHUQABoMNjM3NDIzMTgzODA1Igxt9q4PQYT4NZlqCDMq3ANJ7WrGtTvQ13dlMFBdBuXW6MN02%2FUK5OEuvenV%2FGyQZFz5BRpIR0K%2BjJq4oT38NL43ve%2BFQA6TV5FnZERFIrcZ1My9QYHdUvvGhYNYkj6tjJ2WZbpYE4MfWNEkBOTIxwBR74apeQN0hjxrzwQLt6j4var1%2Bti5UcyJxiGZGmNMUKeGp5w%2BGPmQtWTZdJfSC9GwwwdYhPd1oQv66dV1gs3Vw3vRBuhE68gKQldmMTfEaEy0iXrOzMejjAc7w0ATOAHPKxwXJ%2BRQpN3JO17oYbH6D1AteXTyElBOViyJMVEGggFbMRnSaWneoAztcobD2fJ6ckP%2FbUQdyL6TfptTDOMSWkhu6k9YP15iseRM3nav5cXED%2FyPP%2FTP7wq7PPne4NbVJjERQN6MjafLOFBju28E%2FSDPPw5Ul3Wsw%2Blwv9SaoahUfo0JJsJs1lD17yQdkxDYjJnDEBFmTlxUvsltmwM4xVLAPYWST6XVM1ylFRj9EHhCbvVAr53V7r8khzlXzcrM1NoJnjQUPKTt%2Fy47s6lMOky1%2FacUdvICbtP4qUsAKUKwdlPki7HDJwe3Q1%2FGTUUFjuGK95O%2BoQSxlU09uLisUNEiUgI3CCvD6kGmEKQdlhUkyWMBqOb3NdYoAzCB8Je9BjqkAQQcYfG9rFTbaxZCrpJKzjhSGB2DIQvuI5NgsBNi7M9%2B1a7BTj2m%2BU%2BvU%2FilX4MuWmaB%2BuhfCFJH34E8xONlkr%2FFlqsZc4Bmsixg%2Ffuk8PCp1PLny5lT5Drh%2FG29X6Sd%2BmIosoZCYCinGt%2BsTjtl4O71op%2Bgj8eJCJZUrTRgx1aFJ8d8Gs6FHqGZjH01t26JQ54MxwytbmZlm0PIxwLd%2B8CC%2F%2FKL&X-Amz-Signature=e47e79a8e32aa88ee22ffc02e8ae564e939e9e48ad3531787ed946db8f42ca5d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQUFEJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQC5frH0qJNhSnKXuNsJBMe%2FmlYCsH7gId1OB267PliWqAIhAKbXxlveecEQbGNUbsUDai72VJ3SExyWIUsx5y7JVfk7Kv8DCHUQABoMNjM3NDIzMTgzODA1Igxt9q4PQYT4NZlqCDMq3ANJ7WrGtTvQ13dlMFBdBuXW6MN02%2FUK5OEuvenV%2FGyQZFz5BRpIR0K%2BjJq4oT38NL43ve%2BFQA6TV5FnZERFIrcZ1My9QYHdUvvGhYNYkj6tjJ2WZbpYE4MfWNEkBOTIxwBR74apeQN0hjxrzwQLt6j4var1%2Bti5UcyJxiGZGmNMUKeGp5w%2BGPmQtWTZdJfSC9GwwwdYhPd1oQv66dV1gs3Vw3vRBuhE68gKQldmMTfEaEy0iXrOzMejjAc7w0ATOAHPKxwXJ%2BRQpN3JO17oYbH6D1AteXTyElBOViyJMVEGggFbMRnSaWneoAztcobD2fJ6ckP%2FbUQdyL6TfptTDOMSWkhu6k9YP15iseRM3nav5cXED%2FyPP%2FTP7wq7PPne4NbVJjERQN6MjafLOFBju28E%2FSDPPw5Ul3Wsw%2Blwv9SaoahUfo0JJsJs1lD17yQdkxDYjJnDEBFmTlxUvsltmwM4xVLAPYWST6XVM1ylFRj9EHhCbvVAr53V7r8khzlXzcrM1NoJnjQUPKTt%2Fy47s6lMOky1%2FacUdvICbtP4qUsAKUKwdlPki7HDJwe3Q1%2FGTUUFjuGK95O%2BoQSxlU09uLisUNEiUgI3CCvD6kGmEKQdlhUkyWMBqOb3NdYoAzCB8Je9BjqkAQQcYfG9rFTbaxZCrpJKzjhSGB2DIQvuI5NgsBNi7M9%2B1a7BTj2m%2BU%2BvU%2FilX4MuWmaB%2BuhfCFJH34E8xONlkr%2FFlqsZc4Bmsixg%2Ffuk8PCp1PLny5lT5Drh%2FG29X6Sd%2BmIosoZCYCinGt%2BsTjtl4O71op%2Bgj8eJCJZUrTRgx1aFJ8d8Gs6FHqGZjH01t26JQ54MxwytbmZlm0PIxwLd%2B8CC%2F%2FKL&X-Amz-Signature=bd4e244b68724e260ed9973b1fe29194ca4a022ee6697b05053ab7a81c4bcbdd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQUFEJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQC5frH0qJNhSnKXuNsJBMe%2FmlYCsH7gId1OB267PliWqAIhAKbXxlveecEQbGNUbsUDai72VJ3SExyWIUsx5y7JVfk7Kv8DCHUQABoMNjM3NDIzMTgzODA1Igxt9q4PQYT4NZlqCDMq3ANJ7WrGtTvQ13dlMFBdBuXW6MN02%2FUK5OEuvenV%2FGyQZFz5BRpIR0K%2BjJq4oT38NL43ve%2BFQA6TV5FnZERFIrcZ1My9QYHdUvvGhYNYkj6tjJ2WZbpYE4MfWNEkBOTIxwBR74apeQN0hjxrzwQLt6j4var1%2Bti5UcyJxiGZGmNMUKeGp5w%2BGPmQtWTZdJfSC9GwwwdYhPd1oQv66dV1gs3Vw3vRBuhE68gKQldmMTfEaEy0iXrOzMejjAc7w0ATOAHPKxwXJ%2BRQpN3JO17oYbH6D1AteXTyElBOViyJMVEGggFbMRnSaWneoAztcobD2fJ6ckP%2FbUQdyL6TfptTDOMSWkhu6k9YP15iseRM3nav5cXED%2FyPP%2FTP7wq7PPne4NbVJjERQN6MjafLOFBju28E%2FSDPPw5Ul3Wsw%2Blwv9SaoahUfo0JJsJs1lD17yQdkxDYjJnDEBFmTlxUvsltmwM4xVLAPYWST6XVM1ylFRj9EHhCbvVAr53V7r8khzlXzcrM1NoJnjQUPKTt%2Fy47s6lMOky1%2FacUdvICbtP4qUsAKUKwdlPki7HDJwe3Q1%2FGTUUFjuGK95O%2BoQSxlU09uLisUNEiUgI3CCvD6kGmEKQdlhUkyWMBqOb3NdYoAzCB8Je9BjqkAQQcYfG9rFTbaxZCrpJKzjhSGB2DIQvuI5NgsBNi7M9%2B1a7BTj2m%2BU%2BvU%2FilX4MuWmaB%2BuhfCFJH34E8xONlkr%2FFlqsZc4Bmsixg%2Ffuk8PCp1PLny5lT5Drh%2FG29X6Sd%2BmIosoZCYCinGt%2BsTjtl4O71op%2Bgj8eJCJZUrTRgx1aFJ8d8Gs6FHqGZjH01t26JQ54MxwytbmZlm0PIxwLd%2B8CC%2F%2FKL&X-Amz-Signature=fe5db6eed9be3cab0263a056ee7d47c9011c4341fffc2478605c85ef95b76da6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQUFEJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQC5frH0qJNhSnKXuNsJBMe%2FmlYCsH7gId1OB267PliWqAIhAKbXxlveecEQbGNUbsUDai72VJ3SExyWIUsx5y7JVfk7Kv8DCHUQABoMNjM3NDIzMTgzODA1Igxt9q4PQYT4NZlqCDMq3ANJ7WrGtTvQ13dlMFBdBuXW6MN02%2FUK5OEuvenV%2FGyQZFz5BRpIR0K%2BjJq4oT38NL43ve%2BFQA6TV5FnZERFIrcZ1My9QYHdUvvGhYNYkj6tjJ2WZbpYE4MfWNEkBOTIxwBR74apeQN0hjxrzwQLt6j4var1%2Bti5UcyJxiGZGmNMUKeGp5w%2BGPmQtWTZdJfSC9GwwwdYhPd1oQv66dV1gs3Vw3vRBuhE68gKQldmMTfEaEy0iXrOzMejjAc7w0ATOAHPKxwXJ%2BRQpN3JO17oYbH6D1AteXTyElBOViyJMVEGggFbMRnSaWneoAztcobD2fJ6ckP%2FbUQdyL6TfptTDOMSWkhu6k9YP15iseRM3nav5cXED%2FyPP%2FTP7wq7PPne4NbVJjERQN6MjafLOFBju28E%2FSDPPw5Ul3Wsw%2Blwv9SaoahUfo0JJsJs1lD17yQdkxDYjJnDEBFmTlxUvsltmwM4xVLAPYWST6XVM1ylFRj9EHhCbvVAr53V7r8khzlXzcrM1NoJnjQUPKTt%2Fy47s6lMOky1%2FacUdvICbtP4qUsAKUKwdlPki7HDJwe3Q1%2FGTUUFjuGK95O%2BoQSxlU09uLisUNEiUgI3CCvD6kGmEKQdlhUkyWMBqOb3NdYoAzCB8Je9BjqkAQQcYfG9rFTbaxZCrpJKzjhSGB2DIQvuI5NgsBNi7M9%2B1a7BTj2m%2BU%2BvU%2FilX4MuWmaB%2BuhfCFJH34E8xONlkr%2FFlqsZc4Bmsixg%2Ffuk8PCp1PLny5lT5Drh%2FG29X6Sd%2BmIosoZCYCinGt%2BsTjtl4O71op%2Bgj8eJCJZUrTRgx1aFJ8d8Gs6FHqGZjH01t26JQ54MxwytbmZlm0PIxwLd%2B8CC%2F%2FKL&X-Amz-Signature=7b3a590795e347cadcb0b0f2589d62888bc870f59cd8a1bc6d4e4592bc962e6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQUFEJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQC5frH0qJNhSnKXuNsJBMe%2FmlYCsH7gId1OB267PliWqAIhAKbXxlveecEQbGNUbsUDai72VJ3SExyWIUsx5y7JVfk7Kv8DCHUQABoMNjM3NDIzMTgzODA1Igxt9q4PQYT4NZlqCDMq3ANJ7WrGtTvQ13dlMFBdBuXW6MN02%2FUK5OEuvenV%2FGyQZFz5BRpIR0K%2BjJq4oT38NL43ve%2BFQA6TV5FnZERFIrcZ1My9QYHdUvvGhYNYkj6tjJ2WZbpYE4MfWNEkBOTIxwBR74apeQN0hjxrzwQLt6j4var1%2Bti5UcyJxiGZGmNMUKeGp5w%2BGPmQtWTZdJfSC9GwwwdYhPd1oQv66dV1gs3Vw3vRBuhE68gKQldmMTfEaEy0iXrOzMejjAc7w0ATOAHPKxwXJ%2BRQpN3JO17oYbH6D1AteXTyElBOViyJMVEGggFbMRnSaWneoAztcobD2fJ6ckP%2FbUQdyL6TfptTDOMSWkhu6k9YP15iseRM3nav5cXED%2FyPP%2FTP7wq7PPne4NbVJjERQN6MjafLOFBju28E%2FSDPPw5Ul3Wsw%2Blwv9SaoahUfo0JJsJs1lD17yQdkxDYjJnDEBFmTlxUvsltmwM4xVLAPYWST6XVM1ylFRj9EHhCbvVAr53V7r8khzlXzcrM1NoJnjQUPKTt%2Fy47s6lMOky1%2FacUdvICbtP4qUsAKUKwdlPki7HDJwe3Q1%2FGTUUFjuGK95O%2BoQSxlU09uLisUNEiUgI3CCvD6kGmEKQdlhUkyWMBqOb3NdYoAzCB8Je9BjqkAQQcYfG9rFTbaxZCrpJKzjhSGB2DIQvuI5NgsBNi7M9%2B1a7BTj2m%2BU%2BvU%2FilX4MuWmaB%2BuhfCFJH34E8xONlkr%2FFlqsZc4Bmsixg%2Ffuk8PCp1PLny5lT5Drh%2FG29X6Sd%2BmIosoZCYCinGt%2BsTjtl4O71op%2Bgj8eJCJZUrTRgx1aFJ8d8Gs6FHqGZjH01t26JQ54MxwytbmZlm0PIxwLd%2B8CC%2F%2FKL&X-Amz-Signature=c8caf476ce11f2721ef61d245a960055621cb101b24f48bc6825e64d90af4833&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQUFEJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQC5frH0qJNhSnKXuNsJBMe%2FmlYCsH7gId1OB267PliWqAIhAKbXxlveecEQbGNUbsUDai72VJ3SExyWIUsx5y7JVfk7Kv8DCHUQABoMNjM3NDIzMTgzODA1Igxt9q4PQYT4NZlqCDMq3ANJ7WrGtTvQ13dlMFBdBuXW6MN02%2FUK5OEuvenV%2FGyQZFz5BRpIR0K%2BjJq4oT38NL43ve%2BFQA6TV5FnZERFIrcZ1My9QYHdUvvGhYNYkj6tjJ2WZbpYE4MfWNEkBOTIxwBR74apeQN0hjxrzwQLt6j4var1%2Bti5UcyJxiGZGmNMUKeGp5w%2BGPmQtWTZdJfSC9GwwwdYhPd1oQv66dV1gs3Vw3vRBuhE68gKQldmMTfEaEy0iXrOzMejjAc7w0ATOAHPKxwXJ%2BRQpN3JO17oYbH6D1AteXTyElBOViyJMVEGggFbMRnSaWneoAztcobD2fJ6ckP%2FbUQdyL6TfptTDOMSWkhu6k9YP15iseRM3nav5cXED%2FyPP%2FTP7wq7PPne4NbVJjERQN6MjafLOFBju28E%2FSDPPw5Ul3Wsw%2Blwv9SaoahUfo0JJsJs1lD17yQdkxDYjJnDEBFmTlxUvsltmwM4xVLAPYWST6XVM1ylFRj9EHhCbvVAr53V7r8khzlXzcrM1NoJnjQUPKTt%2Fy47s6lMOky1%2FacUdvICbtP4qUsAKUKwdlPki7HDJwe3Q1%2FGTUUFjuGK95O%2BoQSxlU09uLisUNEiUgI3CCvD6kGmEKQdlhUkyWMBqOb3NdYoAzCB8Je9BjqkAQQcYfG9rFTbaxZCrpJKzjhSGB2DIQvuI5NgsBNi7M9%2B1a7BTj2m%2BU%2BvU%2FilX4MuWmaB%2BuhfCFJH34E8xONlkr%2FFlqsZc4Bmsixg%2Ffuk8PCp1PLny5lT5Drh%2FG29X6Sd%2BmIosoZCYCinGt%2BsTjtl4O71op%2Bgj8eJCJZUrTRgx1aFJ8d8Gs6FHqGZjH01t26JQ54MxwytbmZlm0PIxwLd%2B8CC%2F%2FKL&X-Amz-Signature=2540b96119908a303c11959be47a538ed28ed508ec786b725fc81ff47cb7d837&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6WG6FMS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIGsBv0WHZ3y5xHig4VB60eBVO%2FR7YDfZl8tjtEkvUGITAiBsG4J68764%2BaVdFeu7yzZF7B3SprIS67UiqWVuos63yyr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMCDlijQxczq9bm7nOKtwD0KOHn76zwXfTZjwQt6PoKdPijvJxPiEcJ60CYDL%2BXRirp%2B%2FE8sXq38pIfPYY3pl7qMQ%2FMe9WpmHxbqGQgwubKIla71gRT6%2FZWBd2skC2wiZzNOWp%2FVfrZmE4CiJvOUuoJT6fmOaSII%2FPZlzAKyQKeiWz3m8LBkby%2BN7GrmqmP3kLkXM2L%2B7AX%2ByV3xaDij4rb5Qch5i8iARAO8ohgy5FA0VIhzkkY2%2BsqMaX1TEJ%2FL2TwfLbjO5JC2HGad3%2F4BW23QSE2g3tR6xFLywrAJLUYWIUb%2BGrLU77qoPbzqam%2FaTNvsavzqiV44uNKQ502RvdRzF4nILs1CmayzgxFgFUDkRAh%2FmEc0jMhE9uL%2BYNF4mK8aRk1UXlQuhYkU14T3F1Ht6zo7aqzPPNbvMUuUzOqcaNbReAgkCBnPQQVe1ILT7R%2BWMLYLIRyBjzcx007QrcMvBuIJfsDAEVVcvX3MT%2BCkd9fTxYx1dqonufBfpwLOFXlh7xG5fAHyZ806ZcdgN9iU3mSPPpQWKXPmdKaq5%2Bd1YQexHEIqfcsvPFTMxxr98Wd8ZyV2ITV5QVcjfemJ%2F99AgFlHG80KVyKmvpu%2ByuspOI%2FrjCKh3g%2FcEMHJE1%2FBJ87JH6Y4sH0TfG6cownPCXvQY6pgF1LQn8jq4DTxaTEwUoUCAoMiLVO7qn%2FP%2FCjhC4DcQ408QzV3baWFFgtKKTFK2VkDhF95igsqQFENphwi4eUMeDgyII6up3pYGX1%2FR9wdv75nmRoYDexp6ScqMIaBMTcFqT8%2BY7NJnt%2BkMUEOG6C8wrJ%2BOe2KXP0f7gZjMbi8Kx0fv6NQEqrBrt0oVVHP4ZgLsL9%2BJBznCKCffgOIPVElqTNEdBUr%2Bv&X-Amz-Signature=92d2829a4fdea1b7125efe85e3b2d790b0a7e94b56faab61d622872fa019cde4&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SRWJ7DH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIB2rryEg2cx70%2ByTlTTYt636XMBvo%2FoPGhqXFsAk5TzYAiEAj0tEzlqbnoEBn5hp3sf9B2G3TMCQFql5Cd4jenufUgAq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDAnhIGU28vbAaLDOwCrcAy5I5QFcsDjGl%2BjLnSAjp9lRc0xQcwykW41G4Ipd%2BM25KhckNzl46bNwzMT3cQek5mlQ6ajL9ESwmBesQttErePBSB69XitJyEfGLZwBHiX04pxhtuxiJQs%2FHIq0okHCa2n5a%2FqxJp23XIY3DZI%2FzQuOojXW2tbayviZUL28X18tI1WGEMnkvTedau2ht7Mu3%2BuFhfC2NwQEveSaMPilGuW%2B%2FInNfzCXINR63utcTBwlQjSHiH1VsZGF%2BFrZd5mv0ymQrQA8IUiJXrFXWF794OidH1sC81f3vT12wpAdi0IkteVga6kwLd49ZmWp%2BnxFZb20UeXgasrMAne7F2paLmsQsIQZhcWH%2F%2FHq7QvUtGcM4KiGtYQCFvVFEjqU3w04%2FqgqDFWFApDcJj4XbvYV%2BidzIRbT3QWpHplTjl1LGfyN0OFpj3sBz5K2IYgf6OM%2F9ccMPIC4PdOb%2F5ph94RC7DtHOlQS9Iwf0vgHjpT05OpWkI7HD3oT5AIKvJiG5pGp8w6T0HZEozx0lobZhW9aZEW%2FOuY61kHkPB7D57Vbvp21epo3SNhdHLf2MJQqbDvHs5V3iDY4aGGidn%2B7g4QV2Z9qqb%2BNSSLpRdwcyScWzvVIiUotYngKKzvFkARqMLvvl70GOqUB8mEtkaIAwLRZ7Kg3lXyvnkXSQftgSAkZj6DPB5ij8jowx3PT%2FkPjV8dWoUwLO0PUtfPJQssc9WmeQAs3R95iXPUajPll5qcopEKmdh9wnqX6%2FnQOKCVJ4xdzimZ8yE3I8AyDvZdwOLza674WteqmVBNXCHznujye8QHTDcJjmGk4UUs0lLlpbh9w3266UYfPBFaoGe3BZw3X1e%2FFBM3aXLs9FkS7&X-Amz-Signature=789c0b46786d85e5894cbe6aa8631b9e9bb9a1c69b576fade6a82b5cfd45bf57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQUFEJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQC5frH0qJNhSnKXuNsJBMe%2FmlYCsH7gId1OB267PliWqAIhAKbXxlveecEQbGNUbsUDai72VJ3SExyWIUsx5y7JVfk7Kv8DCHUQABoMNjM3NDIzMTgzODA1Igxt9q4PQYT4NZlqCDMq3ANJ7WrGtTvQ13dlMFBdBuXW6MN02%2FUK5OEuvenV%2FGyQZFz5BRpIR0K%2BjJq4oT38NL43ve%2BFQA6TV5FnZERFIrcZ1My9QYHdUvvGhYNYkj6tjJ2WZbpYE4MfWNEkBOTIxwBR74apeQN0hjxrzwQLt6j4var1%2Bti5UcyJxiGZGmNMUKeGp5w%2BGPmQtWTZdJfSC9GwwwdYhPd1oQv66dV1gs3Vw3vRBuhE68gKQldmMTfEaEy0iXrOzMejjAc7w0ATOAHPKxwXJ%2BRQpN3JO17oYbH6D1AteXTyElBOViyJMVEGggFbMRnSaWneoAztcobD2fJ6ckP%2FbUQdyL6TfptTDOMSWkhu6k9YP15iseRM3nav5cXED%2FyPP%2FTP7wq7PPne4NbVJjERQN6MjafLOFBju28E%2FSDPPw5Ul3Wsw%2Blwv9SaoahUfo0JJsJs1lD17yQdkxDYjJnDEBFmTlxUvsltmwM4xVLAPYWST6XVM1ylFRj9EHhCbvVAr53V7r8khzlXzcrM1NoJnjQUPKTt%2Fy47s6lMOky1%2FacUdvICbtP4qUsAKUKwdlPki7HDJwe3Q1%2FGTUUFjuGK95O%2BoQSxlU09uLisUNEiUgI3CCvD6kGmEKQdlhUkyWMBqOb3NdYoAzCB8Je9BjqkAQQcYfG9rFTbaxZCrpJKzjhSGB2DIQvuI5NgsBNi7M9%2B1a7BTj2m%2BU%2BvU%2FilX4MuWmaB%2BuhfCFJH34E8xONlkr%2FFlqsZc4Bmsixg%2Ffuk8PCp1PLny5lT5Drh%2FG29X6Sd%2BmIosoZCYCinGt%2BsTjtl4O71op%2Bgj8eJCJZUrTRgx1aFJ8d8Gs6FHqGZjH01t26JQ54MxwytbmZlm0PIxwLd%2B8CC%2F%2FKL&X-Amz-Signature=47158bbbe8aa4e06d93866e304556de18988c70259036c774b78f104cbe74f9d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQUFEJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQC5frH0qJNhSnKXuNsJBMe%2FmlYCsH7gId1OB267PliWqAIhAKbXxlveecEQbGNUbsUDai72VJ3SExyWIUsx5y7JVfk7Kv8DCHUQABoMNjM3NDIzMTgzODA1Igxt9q4PQYT4NZlqCDMq3ANJ7WrGtTvQ13dlMFBdBuXW6MN02%2FUK5OEuvenV%2FGyQZFz5BRpIR0K%2BjJq4oT38NL43ve%2BFQA6TV5FnZERFIrcZ1My9QYHdUvvGhYNYkj6tjJ2WZbpYE4MfWNEkBOTIxwBR74apeQN0hjxrzwQLt6j4var1%2Bti5UcyJxiGZGmNMUKeGp5w%2BGPmQtWTZdJfSC9GwwwdYhPd1oQv66dV1gs3Vw3vRBuhE68gKQldmMTfEaEy0iXrOzMejjAc7w0ATOAHPKxwXJ%2BRQpN3JO17oYbH6D1AteXTyElBOViyJMVEGggFbMRnSaWneoAztcobD2fJ6ckP%2FbUQdyL6TfptTDOMSWkhu6k9YP15iseRM3nav5cXED%2FyPP%2FTP7wq7PPne4NbVJjERQN6MjafLOFBju28E%2FSDPPw5Ul3Wsw%2Blwv9SaoahUfo0JJsJs1lD17yQdkxDYjJnDEBFmTlxUvsltmwM4xVLAPYWST6XVM1ylFRj9EHhCbvVAr53V7r8khzlXzcrM1NoJnjQUPKTt%2Fy47s6lMOky1%2FacUdvICbtP4qUsAKUKwdlPki7HDJwe3Q1%2FGTUUFjuGK95O%2BoQSxlU09uLisUNEiUgI3CCvD6kGmEKQdlhUkyWMBqOb3NdYoAzCB8Je9BjqkAQQcYfG9rFTbaxZCrpJKzjhSGB2DIQvuI5NgsBNi7M9%2B1a7BTj2m%2BU%2BvU%2FilX4MuWmaB%2BuhfCFJH34E8xONlkr%2FFlqsZc4Bmsixg%2Ffuk8PCp1PLny5lT5Drh%2FG29X6Sd%2BmIosoZCYCinGt%2BsTjtl4O71op%2Bgj8eJCJZUrTRgx1aFJ8d8Gs6FHqGZjH01t26JQ54MxwytbmZlm0PIxwLd%2B8CC%2F%2FKL&X-Amz-Signature=1c5dcb868ffe4d5fbbddf109d1cfa77f9b0186c6a4952685bb42a3898c11a19b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQUFEJW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQC5frH0qJNhSnKXuNsJBMe%2FmlYCsH7gId1OB267PliWqAIhAKbXxlveecEQbGNUbsUDai72VJ3SExyWIUsx5y7JVfk7Kv8DCHUQABoMNjM3NDIzMTgzODA1Igxt9q4PQYT4NZlqCDMq3ANJ7WrGtTvQ13dlMFBdBuXW6MN02%2FUK5OEuvenV%2FGyQZFz5BRpIR0K%2BjJq4oT38NL43ve%2BFQA6TV5FnZERFIrcZ1My9QYHdUvvGhYNYkj6tjJ2WZbpYE4MfWNEkBOTIxwBR74apeQN0hjxrzwQLt6j4var1%2Bti5UcyJxiGZGmNMUKeGp5w%2BGPmQtWTZdJfSC9GwwwdYhPd1oQv66dV1gs3Vw3vRBuhE68gKQldmMTfEaEy0iXrOzMejjAc7w0ATOAHPKxwXJ%2BRQpN3JO17oYbH6D1AteXTyElBOViyJMVEGggFbMRnSaWneoAztcobD2fJ6ckP%2FbUQdyL6TfptTDOMSWkhu6k9YP15iseRM3nav5cXED%2FyPP%2FTP7wq7PPne4NbVJjERQN6MjafLOFBju28E%2FSDPPw5Ul3Wsw%2Blwv9SaoahUfo0JJsJs1lD17yQdkxDYjJnDEBFmTlxUvsltmwM4xVLAPYWST6XVM1ylFRj9EHhCbvVAr53V7r8khzlXzcrM1NoJnjQUPKTt%2Fy47s6lMOky1%2FacUdvICbtP4qUsAKUKwdlPki7HDJwe3Q1%2FGTUUFjuGK95O%2BoQSxlU09uLisUNEiUgI3CCvD6kGmEKQdlhUkyWMBqOb3NdYoAzCB8Je9BjqkAQQcYfG9rFTbaxZCrpJKzjhSGB2DIQvuI5NgsBNi7M9%2B1a7BTj2m%2BU%2BvU%2FilX4MuWmaB%2BuhfCFJH34E8xONlkr%2FFlqsZc4Bmsixg%2Ffuk8PCp1PLny5lT5Drh%2FG29X6Sd%2BmIosoZCYCinGt%2BsTjtl4O71op%2Bgj8eJCJZUrTRgx1aFJ8d8Gs6FHqGZjH01t26JQ54MxwytbmZlm0PIxwLd%2B8CC%2F%2FKL&X-Amz-Signature=2a8d4192802edc74f72f20374cae2f86f9f2a0c4fa52fb1a3088b50129a1726b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QX2EEA6E%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDhxvynKdIX6xTPeJ9GOqqEq508BrIIS5wXrwT%2FvF0AAwIgIjwBIph8IEbPJSmldqOibXunKU1TrdTOcvLm5flpT5Yq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDHCobehqIObuX%2BXGrCrcAzFwflgjfO9tut1NChnMprgwMkR27tWfA5Fk5%2FhcqiivoLJIChi5l9yIFuB6ZBa%2BZ%2B1Cyq8bXagrtwBFXY4P3fk4nz3VjQxHmmNGCUvzk6Nn05NHgSKrTDPFuYcv33o2jpd%2BWhWSPv5uG4gIv7fZGadAbOLH9uWp2asNvgQXZ1MeWmvb2j8O6fXYLKYDHgqKFck8nfuQ6PSWMgBgoUL2g55pHsgK6nKIWidoS2Ys2YU616P7keeg3CuOxhSymwzWkP83%2Bi6%2BJcZRKkiPwP6afFrU9FFS3qoFQHzZR84rx6K6ErAO8CcnWPHNnTHILOy1U3ir8HjgjJnY7s4Zc5vyLb%2B49rPHIahTcjSDew5NadrRExBipI7PuBuaShbcKEEcEhA%2BED4wXXt8p0LPCFZd1PT2SF5es80FzjpX9PkZbey%2FaGP1nwZQPUF4FlWCq3chKRH%2BhGZMEJXZRJ3TJoQZk0xm4yt%2FY5HnxDaZ94qZhszUmoAkc2rIQ1bIDYk%2FCk90CBa4LL%2BkZWeI6KiTKS8Xztvzdh%2FYy%2BEb4ZVaIpfkD7Yx4nysPtI8NkYrH94CLfIzHjEY1%2Bz8iwsItXaTDykE7DRSULIM%2FfInJl2oYQcTVbU%2FVkRKMSnraveJV9qAMOnvl70GOqUBF0nRBf0kmpFyAaafEiuzzuHdK2qgdAUfWgsXFLd6KawwzyAh0yUYrcHZrY8AnzqqigZfHS2AasikO2KPFfWKpLHBm5N%2FguQzS3sZ2sIM8i9eHmCWhjxMsfxuKyn9c8yt%2FbXDNuwOooeMZAj85alwssYbqbRjgteoGMRUgfVUVq53eFSiqVaBjTugV7D60HC0oE3EHcD%2FRtadOjFOF9gS7qZMjU95&X-Amz-Signature=c5e1d38bd4954a1f99f582462c2cfb6105d5c392247f53be2a8a5999dd9df081&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627HTC3QA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQCvlfgHL1dyKwismDarVn4nROtwA48kc%2B5ypdz12RWAugIgPOmCfs5JF39B7UlJfeWwYgKy377hGXy4DxI%2FY8Ni00kq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDPZBox3pHQDUx2qP5CrcA%2FJsQtRhHiUeH%2FPYwI4yMr6XFoNH%2FObcyVxb%2BDcfMdCJkFVaSmYQxM9Z5%2BQ4OYFTzO7HS7R%2F0vbF5qd5C%2B3VKffPTV6b3n%2Fu1Iq4ut11oWEV8NSJ%2BU3h5Z5XudlaqfhMYwJZpwminVVidZk9ZdDjfgIr7XjqcyxfFv%2FqiOcf%2FOhBk8PBw%2BrkUhj7qaOZ3%2BneD8zEtqLq4Xl1w4N4JF46aJJ%2FmF2kJsqk%2FlznPIy8OR0tqCo9T06mzAdr97H%2FcU4HFfNrWc17a7PSqkYx1IjXUElVhk9VZAePx3m98TVG2RxTiYErT7TE0qCEpqG5QYTEl41UFPfeZpdjhQARBlvoKmGFn3%2FzoTnNyRQ9nbtVxeQi2mLVrxnS1KrL%2FI6sXvjBPX3gieCKshCDSdf6fwU3nftsbLgYc5eCBlVaYFKhRF%2BBB4On%2BspbbRyD1jKWbDx6IGFamXztVfO4O8YoDhia6I%2BC1%2BF22PzK8sVvFa%2FDJjexdTh5ziBg94njIukH8rTlVjxTxYIVegTUJhM23hrNResOOQbxSzt%2F3slrMxmTcn3RjhbXrItOQiiM2xljB5%2FR3uacEl6DPTXJi3LYZB6hEDu2xvnc%2Fm63ZbMqiJc2LJx5ighEBrlVDwK1fioFMKTwl70GOqUBTnqpB8hQsHJiU5C1kS%2BloZy6nsg5Z3u1YFl8ENA58jBufE0bYTlE6iueOym%2FcwS%2B3KQIstyFqmzQxImQDloIAVnMYL7XtgcbRPavxr1Q2gTfvNMc2Xfpyw0VvibqYk0N3vTrGv%2F2NQME5SKOtSt%2FgRTDxAgeR1EdfGI69TtDFLQsCYxUW5U%2BLLrCIN6kPTs3Zy21fnc3%2FcazgkF59uoQANRRlsRC&X-Amz-Signature=cdf0c623d85b576f68a4a9bb20da587e7114e88c12ac8d7070684859673fb710&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JXSTB7V%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCICT0OA9zKmeOdyURC8VLys2wCABXnrUlHm8d9IP%2Fc2%2FiAiEA83KDtfgx3%2ByfMBPK5hGofpnuKjHyx%2F1sawWNsnZDEFQq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDACtlCT3Llqpfg9C5yrcA3OvDn1v4F3g6dKD48RR3WMkuCgAFu6FRKm1ZDn4m3gLES0nmxkBKxRzQ9Np%2FNn%2BXurqyfQPREFXPSiF7Xg%2FWcvbw2ATzVuqryYP6TP0E1E7lOVhl%2BusujLQ1gOYLQDPBB7yK6C6zyAb0omdJ6JMmVCOUXF3FutQbF%2BUzRk5g%2FX%2FQLyzBu3WkiqDKk%2Bb2%2FmlDt0nbJMxxZp4ymFy%2FN9lkLl1MCG6EI9f1YhdErVlw%2F2EBJaMXy6NDUZGp6oLPXUqK6BND67ZCz02iIkZqlnfxp%2F%2BkZsD6Yuer9KvyS9ASaHg1%2B7rlSJLimkdEBPQeD1%2Bg%2F7oG01RS2EHOfC00R%2BMKG7%2BkCfgaj0gfkG0QJwzACsUaWVGGPiekRYv6fp6nY4mxIzCo2iOie1%2Bj480Cy83SeAUGEXpX9oD%2BS4YuXEEIOKsHMwkfPcic0HpJXiPl61M1FkzcsLebDJFRSVVOtcNWQzLYRZjjKYAqQ5D6ASbkQSln51PXL5a9t1j%2FMvSHNk7rqnQfo8xdW5S2Y%2BzD8jth6zE5PeOgnbpJGcW%2FCzyexYY5drxAqgLQqnQHrsNMWYAVjXTupBGKv8%2Fm%2BNYXEL4Ncm6rhFJpBivIz%2BABkRNjCBrAsVUyMrGPF61VbUmMIzvl70GOqUBuEWq1ieMg073hmqWekzw09%2B7R21FQ9WZ%2FIS3HjIVPvvM4PKoFQzyj0MYWw3B5j1iNcgsSmhNm862kcZhLJIe580ihpuqm5ovMu7F3A1JnTeBNL%2FjZtftgQlhEGnS%2FF0G5kc%2FdS50L2wOdYAypD4DZ0rE9fOWBHHUYw0gQjngkIPMDcVCBZyozInIeHqTSCjNgpSWQuozG%2BV%2FZIm4gJYWvNy1fvQl&X-Amz-Signature=4e6244f6be4646ec6c301987de4854269cf3b4884e3b467854ef1df056af6e66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5FINQAR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCAVM%2BBaLJRZJv9RAaRPVKfOe%2BrzfCaxfoGdQAK1s3PiwIhAOt5R2b05UugyxY2Q182sYINJCHdu7onXlbg4VvcfE1rKv8DCHUQABoMNjM3NDIzMTgzODA1IgxmQPWwhgya9b9pgbQq3AOyKm5f8n969qzUw4tN9sWYLDmLgPpacbSM1bOaLNy6sIidG%2Fi1XggsvWYlrq1p38XHBnCbCctrNTJUMln0cT30m%2F9grE1MDub%2FkAt1GpqzsmDOyyiXggJwjRsKCa%2B1y49a0GgzQ4Tqr%2BV219XKSNd0Sz5TvLHhSgytEgY28kUF2LNDab%2BkdRx%2FGFDtsO7ojMhULMs0wLzZ4bI%2FgV6eGoK9TVwPLqheNIEHjg7WA%2Fdig0FQKvJy0qlZL9awK4fz3fzdAiTNbearntxD1krL9MlVO0MqvQOm%2Fp7BDo5VR0uv2bchH0ap5pen10jYwPR2jVzVgBaHQVaKHbGB6iNc0T%2FlZ%2FsBWS4DaP03zSeVsNJpmdCPOrI%2FuD6uMh5lP6mJzn5tTPLHYfp42KgJqzOf3SltSPB0ykLovD80b3w1vly5kSumPkj0krqCswEqx7gyCqZsu6RoCSFLOTELWZQ4K2hlyURBhI4KecLMbn8gtqZYrPWWX%2BGq1rcA%2F%2Fn4YjLzF1O1K6RVOJSst1g6VOrkrAO80dtJLbS6piAgJJTz4b7t1rIa5Q0w%2Fy%2BB9hB%2BjxEnPScC%2FClNRWb2xTPUrEJY%2Fw3IlEAqzWPtuJEV7qa1S4F%2FMxDFC%2BWng8PBjPpkPjC475e9BjqkAZKb7kmN4Qe7L8CrvB4EU2qlrx%2BlW48t8HH6064vnD7yYCukMtEG1CWS873yDXksaQMUv2YVidoFdvJe7UcVIWAZqhU81ciZXmHafomzq1nPi1SF8ATaJOdJaXNyDQGeLPs2KRA69rr32dfKPDmj9BMe95z6eaQs4l3zR8D7cPNlZIILMsJ7cD3Yir7Rcehhd8ks5bRlnAJOxZBu0CtTEel%2BnvLM&X-Amz-Signature=442f877819692018d4a4856ebe81bc7735fb8c83d36c528d5c16b829c8532b18&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5FINQAR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCAVM%2BBaLJRZJv9RAaRPVKfOe%2BrzfCaxfoGdQAK1s3PiwIhAOt5R2b05UugyxY2Q182sYINJCHdu7onXlbg4VvcfE1rKv8DCHUQABoMNjM3NDIzMTgzODA1IgxmQPWwhgya9b9pgbQq3AOyKm5f8n969qzUw4tN9sWYLDmLgPpacbSM1bOaLNy6sIidG%2Fi1XggsvWYlrq1p38XHBnCbCctrNTJUMln0cT30m%2F9grE1MDub%2FkAt1GpqzsmDOyyiXggJwjRsKCa%2B1y49a0GgzQ4Tqr%2BV219XKSNd0Sz5TvLHhSgytEgY28kUF2LNDab%2BkdRx%2FGFDtsO7ojMhULMs0wLzZ4bI%2FgV6eGoK9TVwPLqheNIEHjg7WA%2Fdig0FQKvJy0qlZL9awK4fz3fzdAiTNbearntxD1krL9MlVO0MqvQOm%2Fp7BDo5VR0uv2bchH0ap5pen10jYwPR2jVzVgBaHQVaKHbGB6iNc0T%2FlZ%2FsBWS4DaP03zSeVsNJpmdCPOrI%2FuD6uMh5lP6mJzn5tTPLHYfp42KgJqzOf3SltSPB0ykLovD80b3w1vly5kSumPkj0krqCswEqx7gyCqZsu6RoCSFLOTELWZQ4K2hlyURBhI4KecLMbn8gtqZYrPWWX%2BGq1rcA%2F%2Fn4YjLzF1O1K6RVOJSst1g6VOrkrAO80dtJLbS6piAgJJTz4b7t1rIa5Q0w%2Fy%2BB9hB%2BjxEnPScC%2FClNRWb2xTPUrEJY%2Fw3IlEAqzWPtuJEV7qa1S4F%2FMxDFC%2BWng8PBjPpkPjC475e9BjqkAZKb7kmN4Qe7L8CrvB4EU2qlrx%2BlW48t8HH6064vnD7yYCukMtEG1CWS873yDXksaQMUv2YVidoFdvJe7UcVIWAZqhU81ciZXmHafomzq1nPi1SF8ATaJOdJaXNyDQGeLPs2KRA69rr32dfKPDmj9BMe95z6eaQs4l3zR8D7cPNlZIILMsJ7cD3Yir7Rcehhd8ks5bRlnAJOxZBu0CtTEel%2BnvLM&X-Amz-Signature=0349b95b6455ee269be55fae21ecb86c46fcb1e4dee1fdd238146dafcb85a729&X-Amz-SignedHeaders=host&x-id=GetObject)

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
