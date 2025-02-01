

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JHJRVOJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFPtLZPm%2FGAnR53fglJa2XbhINMuQQwvkt3u1noUQM%2FoAiEAw6dCUmr8%2B2lB9xmo4X8yhQA102GbvQdr7JlgjnPZUqgqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB4B4ecagTPruykeeCrcA3OZUIUlBrQD73IC0sqwd%2BIHfkVVlMk0l4RhzrPzlEmcdtGBh91o1q5SnIP2wUoZWoprq%2FUkJWsBlAg0FQbNqu9ous72Vs1t%2BQkJPFZ19O7VNaYCDNbSvZky54vMvPyPqY6GvCW4A%2BstzezoORWhX7b2hWor6aD4UKTInFOaqqYn7ST6kjG63bsrsGKkf59BWSn1ys%2Ft7S44nOb3U9Sd1%2BkSn0oAh3y55kP9HeKCtSGtT6sbzNEzKSj0BedFqbY1%2FNze%2FR6NijqT1Fg9v6GxRSd5rU2qZjUCTQKU2nhIBxEoTuUxx45jtE37sdqu2oy4Sbm5VUU%2BzSt%2FxEwZUE6m4SdIIPq50BYnTgpFNHlEJ4onyToVSn29UOz9qeqOaCZCbVww42JNrUSGq%2FiYwf08zu6DO4bnQM4kitkUGQvyrtGBn3SI44s09u2%2FlCDXjy9gl3qxLiiK6Z%2BrkJBb9vN4icFnULYzSCHNh2zDQxE7Tpg1zGLplCD7Csc0elbGbqeH3Jb64Cb%2BkjjHyUpv79Wstpq0XCxHzV57CGAWzD23jZQmFe5zmFKOzhHM0HzG93DBMt%2FtQL2%2Fz84jGSXiVvpVEiIOGGu7XIelTMaj496bw%2B1CnrP54dqVQ36t3piaMM3F%2BLwGOqUB82uByoOEX%2B0arevMYMVEf7%2BmNF9SMI8F9385hAKtavWuykYKeSfiOChlBt2EXYJjYIUmxRCUTAr9KIr7FjIy32FWbe7C8sE3gNKUIZBRUV7yYMz8Rq5U%2Fc8SZMpPeyao493%2F6QUJjWmO0crk5d3uekAQn6ING86gq5C1XJiq3sEI7WallZrVk6LA12aSMNwjO5%2BTD97Gg0Wv5QcDL4888Er2Ukws&X-Amz-Signature=2b041f20209cc2a230ed472d011a1df1a607005733b4a62a6a71af6479273705&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JHJRVOJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFPtLZPm%2FGAnR53fglJa2XbhINMuQQwvkt3u1noUQM%2FoAiEAw6dCUmr8%2B2lB9xmo4X8yhQA102GbvQdr7JlgjnPZUqgqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB4B4ecagTPruykeeCrcA3OZUIUlBrQD73IC0sqwd%2BIHfkVVlMk0l4RhzrPzlEmcdtGBh91o1q5SnIP2wUoZWoprq%2FUkJWsBlAg0FQbNqu9ous72Vs1t%2BQkJPFZ19O7VNaYCDNbSvZky54vMvPyPqY6GvCW4A%2BstzezoORWhX7b2hWor6aD4UKTInFOaqqYn7ST6kjG63bsrsGKkf59BWSn1ys%2Ft7S44nOb3U9Sd1%2BkSn0oAh3y55kP9HeKCtSGtT6sbzNEzKSj0BedFqbY1%2FNze%2FR6NijqT1Fg9v6GxRSd5rU2qZjUCTQKU2nhIBxEoTuUxx45jtE37sdqu2oy4Sbm5VUU%2BzSt%2FxEwZUE6m4SdIIPq50BYnTgpFNHlEJ4onyToVSn29UOz9qeqOaCZCbVww42JNrUSGq%2FiYwf08zu6DO4bnQM4kitkUGQvyrtGBn3SI44s09u2%2FlCDXjy9gl3qxLiiK6Z%2BrkJBb9vN4icFnULYzSCHNh2zDQxE7Tpg1zGLplCD7Csc0elbGbqeH3Jb64Cb%2BkjjHyUpv79Wstpq0XCxHzV57CGAWzD23jZQmFe5zmFKOzhHM0HzG93DBMt%2FtQL2%2Fz84jGSXiVvpVEiIOGGu7XIelTMaj496bw%2B1CnrP54dqVQ36t3piaMM3F%2BLwGOqUB82uByoOEX%2B0arevMYMVEf7%2BmNF9SMI8F9385hAKtavWuykYKeSfiOChlBt2EXYJjYIUmxRCUTAr9KIr7FjIy32FWbe7C8sE3gNKUIZBRUV7yYMz8Rq5U%2Fc8SZMpPeyao493%2F6QUJjWmO0crk5d3uekAQn6ING86gq5C1XJiq3sEI7WallZrVk6LA12aSMNwjO5%2BTD97Gg0Wv5QcDL4888Er2Ukws&X-Amz-Signature=30faac58f0c07ef56873a5884a6a0029919f75ba61a136f59a49c6496285586a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JHJRVOJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFPtLZPm%2FGAnR53fglJa2XbhINMuQQwvkt3u1noUQM%2FoAiEAw6dCUmr8%2B2lB9xmo4X8yhQA102GbvQdr7JlgjnPZUqgqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB4B4ecagTPruykeeCrcA3OZUIUlBrQD73IC0sqwd%2BIHfkVVlMk0l4RhzrPzlEmcdtGBh91o1q5SnIP2wUoZWoprq%2FUkJWsBlAg0FQbNqu9ous72Vs1t%2BQkJPFZ19O7VNaYCDNbSvZky54vMvPyPqY6GvCW4A%2BstzezoORWhX7b2hWor6aD4UKTInFOaqqYn7ST6kjG63bsrsGKkf59BWSn1ys%2Ft7S44nOb3U9Sd1%2BkSn0oAh3y55kP9HeKCtSGtT6sbzNEzKSj0BedFqbY1%2FNze%2FR6NijqT1Fg9v6GxRSd5rU2qZjUCTQKU2nhIBxEoTuUxx45jtE37sdqu2oy4Sbm5VUU%2BzSt%2FxEwZUE6m4SdIIPq50BYnTgpFNHlEJ4onyToVSn29UOz9qeqOaCZCbVww42JNrUSGq%2FiYwf08zu6DO4bnQM4kitkUGQvyrtGBn3SI44s09u2%2FlCDXjy9gl3qxLiiK6Z%2BrkJBb9vN4icFnULYzSCHNh2zDQxE7Tpg1zGLplCD7Csc0elbGbqeH3Jb64Cb%2BkjjHyUpv79Wstpq0XCxHzV57CGAWzD23jZQmFe5zmFKOzhHM0HzG93DBMt%2FtQL2%2Fz84jGSXiVvpVEiIOGGu7XIelTMaj496bw%2B1CnrP54dqVQ36t3piaMM3F%2BLwGOqUB82uByoOEX%2B0arevMYMVEf7%2BmNF9SMI8F9385hAKtavWuykYKeSfiOChlBt2EXYJjYIUmxRCUTAr9KIr7FjIy32FWbe7C8sE3gNKUIZBRUV7yYMz8Rq5U%2Fc8SZMpPeyao493%2F6QUJjWmO0crk5d3uekAQn6ING86gq5C1XJiq3sEI7WallZrVk6LA12aSMNwjO5%2BTD97Gg0Wv5QcDL4888Er2Ukws&X-Amz-Signature=c22fb785bff2a98a63848efbeb3faea9b4ed1b3f2c9c8f4e7b508d957df48ddc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IH27PZM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEV6LCPOszavmg21R3mloTxR24As7V4Oq76%2F6Ft0zSOyAiA8LyG%2BfZ0XyaRNtNtdPQpnxqNgEQvbgU8%2F45EyGNnjPiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeKm9CsDV%2BigbtFCwKtwDmdCH5NixI1AXcxvgbmgVzCF9rHsNUziald38495Al16KqAz0ZAlBjIthSY0Bq%2B6I%2F5OPzIyg4zJ5%2Fvjofd7D6she27EjH30%2BA74buBpYKmjE1SYA2mCSJ1D7uFZmTx3qPgt4p%2FqNQdPMEk8bui90xc9tDj%2BUj2acA%2B8emQaKPczgnu0JAgecUFS3Yw8k876D3xSjaRDkAb91R%2BVyP9xtyuMhSqwvAoIAdLFzHFX0SHCX6x2TMxYOvF545KP8bNy0aANHqyz%2B3me7zntWjO4FmzfPCIeOLdMAf9xPqoO0uDHsYs%2B2a%2B64dUFLAWBr%2F0DMlzvCS0pDBoXyDzpZhWgji4yqgUVcAMdjJ8a0lJKyIGr0yKwf5SnqdRHg7z7scj5%2Fu7yW4Ks3%2Fr8ZTkR7yAZ98YM8L9e7QjqS2LNRbhnaHY9qmfwC80cUvHnMhVjYZ6F76AioyyDSy%2BXAEdnHgmldRCA4ZMIHEf2dw9TF7ZZY51fyNELHz0EaEUaGFlB4nWizvTklMKAiwwl4cQ%2F7ufngEhZfnLzG8ahArHHSE%2Fpo1rDZVqCaiKf%2BPFC7%2FCeWiINXYB7TiAHImGahnRWiiRV3xCHcAKORXBijGN51pzUcLPIk2J%2F%2BVx8%2BhKsfKO4w%2B8n4vAY6pgEHsFBcsnUDYKAiNFXviNls0yasQKU9d3nAgd9nA48ozxfOT21lwzQYznvqAm3eM8zK0CsjCH1gSxDYJXQvbGArZox8rNhScbIETXUKeZsACgpWY%2BDzHyYND%2FkUE%2BmouF8ZcDRe2RN6l7bNENieaqG9ZQAtZLnpoJKzT%2FFvjJR0Bq4s58aiPnOcNh%2BLHUPxbtlb90seWW%2BPy7OSa8B%2FD%2FrM%2FZuMrvi1&X-Amz-Signature=361ba910ccb4e15853325f13044fc3d8f2c1333857b2e82721ba3b7ec0ff6267&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IH27PZM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEV6LCPOszavmg21R3mloTxR24As7V4Oq76%2F6Ft0zSOyAiA8LyG%2BfZ0XyaRNtNtdPQpnxqNgEQvbgU8%2F45EyGNnjPiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeKm9CsDV%2BigbtFCwKtwDmdCH5NixI1AXcxvgbmgVzCF9rHsNUziald38495Al16KqAz0ZAlBjIthSY0Bq%2B6I%2F5OPzIyg4zJ5%2Fvjofd7D6she27EjH30%2BA74buBpYKmjE1SYA2mCSJ1D7uFZmTx3qPgt4p%2FqNQdPMEk8bui90xc9tDj%2BUj2acA%2B8emQaKPczgnu0JAgecUFS3Yw8k876D3xSjaRDkAb91R%2BVyP9xtyuMhSqwvAoIAdLFzHFX0SHCX6x2TMxYOvF545KP8bNy0aANHqyz%2B3me7zntWjO4FmzfPCIeOLdMAf9xPqoO0uDHsYs%2B2a%2B64dUFLAWBr%2F0DMlzvCS0pDBoXyDzpZhWgji4yqgUVcAMdjJ8a0lJKyIGr0yKwf5SnqdRHg7z7scj5%2Fu7yW4Ks3%2Fr8ZTkR7yAZ98YM8L9e7QjqS2LNRbhnaHY9qmfwC80cUvHnMhVjYZ6F76AioyyDSy%2BXAEdnHgmldRCA4ZMIHEf2dw9TF7ZZY51fyNELHz0EaEUaGFlB4nWizvTklMKAiwwl4cQ%2F7ufngEhZfnLzG8ahArHHSE%2Fpo1rDZVqCaiKf%2BPFC7%2FCeWiINXYB7TiAHImGahnRWiiRV3xCHcAKORXBijGN51pzUcLPIk2J%2F%2BVx8%2BhKsfKO4w%2B8n4vAY6pgEHsFBcsnUDYKAiNFXviNls0yasQKU9d3nAgd9nA48ozxfOT21lwzQYznvqAm3eM8zK0CsjCH1gSxDYJXQvbGArZox8rNhScbIETXUKeZsACgpWY%2BDzHyYND%2FkUE%2BmouF8ZcDRe2RN6l7bNENieaqG9ZQAtZLnpoJKzT%2FFvjJR0Bq4s58aiPnOcNh%2BLHUPxbtlb90seWW%2BPy7OSa8B%2FD%2FrM%2FZuMrvi1&X-Amz-Signature=15f818425ccb91b4eff83b142fb5197b6eeff2d4325ee8821370a0c6cfc9d0db&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IH27PZM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEV6LCPOszavmg21R3mloTxR24As7V4Oq76%2F6Ft0zSOyAiA8LyG%2BfZ0XyaRNtNtdPQpnxqNgEQvbgU8%2F45EyGNnjPiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeKm9CsDV%2BigbtFCwKtwDmdCH5NixI1AXcxvgbmgVzCF9rHsNUziald38495Al16KqAz0ZAlBjIthSY0Bq%2B6I%2F5OPzIyg4zJ5%2Fvjofd7D6she27EjH30%2BA74buBpYKmjE1SYA2mCSJ1D7uFZmTx3qPgt4p%2FqNQdPMEk8bui90xc9tDj%2BUj2acA%2B8emQaKPczgnu0JAgecUFS3Yw8k876D3xSjaRDkAb91R%2BVyP9xtyuMhSqwvAoIAdLFzHFX0SHCX6x2TMxYOvF545KP8bNy0aANHqyz%2B3me7zntWjO4FmzfPCIeOLdMAf9xPqoO0uDHsYs%2B2a%2B64dUFLAWBr%2F0DMlzvCS0pDBoXyDzpZhWgji4yqgUVcAMdjJ8a0lJKyIGr0yKwf5SnqdRHg7z7scj5%2Fu7yW4Ks3%2Fr8ZTkR7yAZ98YM8L9e7QjqS2LNRbhnaHY9qmfwC80cUvHnMhVjYZ6F76AioyyDSy%2BXAEdnHgmldRCA4ZMIHEf2dw9TF7ZZY51fyNELHz0EaEUaGFlB4nWizvTklMKAiwwl4cQ%2F7ufngEhZfnLzG8ahArHHSE%2Fpo1rDZVqCaiKf%2BPFC7%2FCeWiINXYB7TiAHImGahnRWiiRV3xCHcAKORXBijGN51pzUcLPIk2J%2F%2BVx8%2BhKsfKO4w%2B8n4vAY6pgEHsFBcsnUDYKAiNFXviNls0yasQKU9d3nAgd9nA48ozxfOT21lwzQYznvqAm3eM8zK0CsjCH1gSxDYJXQvbGArZox8rNhScbIETXUKeZsACgpWY%2BDzHyYND%2FkUE%2BmouF8ZcDRe2RN6l7bNENieaqG9ZQAtZLnpoJKzT%2FFvjJR0Bq4s58aiPnOcNh%2BLHUPxbtlb90seWW%2BPy7OSa8B%2FD%2FrM%2FZuMrvi1&X-Amz-Signature=25a5d89c24bcecc6ff71e11688184c493488a7fbbd0f3922800ad9263936d3aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IH27PZM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEV6LCPOszavmg21R3mloTxR24As7V4Oq76%2F6Ft0zSOyAiA8LyG%2BfZ0XyaRNtNtdPQpnxqNgEQvbgU8%2F45EyGNnjPiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeKm9CsDV%2BigbtFCwKtwDmdCH5NixI1AXcxvgbmgVzCF9rHsNUziald38495Al16KqAz0ZAlBjIthSY0Bq%2B6I%2F5OPzIyg4zJ5%2Fvjofd7D6she27EjH30%2BA74buBpYKmjE1SYA2mCSJ1D7uFZmTx3qPgt4p%2FqNQdPMEk8bui90xc9tDj%2BUj2acA%2B8emQaKPczgnu0JAgecUFS3Yw8k876D3xSjaRDkAb91R%2BVyP9xtyuMhSqwvAoIAdLFzHFX0SHCX6x2TMxYOvF545KP8bNy0aANHqyz%2B3me7zntWjO4FmzfPCIeOLdMAf9xPqoO0uDHsYs%2B2a%2B64dUFLAWBr%2F0DMlzvCS0pDBoXyDzpZhWgji4yqgUVcAMdjJ8a0lJKyIGr0yKwf5SnqdRHg7z7scj5%2Fu7yW4Ks3%2Fr8ZTkR7yAZ98YM8L9e7QjqS2LNRbhnaHY9qmfwC80cUvHnMhVjYZ6F76AioyyDSy%2BXAEdnHgmldRCA4ZMIHEf2dw9TF7ZZY51fyNELHz0EaEUaGFlB4nWizvTklMKAiwwl4cQ%2F7ufngEhZfnLzG8ahArHHSE%2Fpo1rDZVqCaiKf%2BPFC7%2FCeWiINXYB7TiAHImGahnRWiiRV3xCHcAKORXBijGN51pzUcLPIk2J%2F%2BVx8%2BhKsfKO4w%2B8n4vAY6pgEHsFBcsnUDYKAiNFXviNls0yasQKU9d3nAgd9nA48ozxfOT21lwzQYznvqAm3eM8zK0CsjCH1gSxDYJXQvbGArZox8rNhScbIETXUKeZsACgpWY%2BDzHyYND%2FkUE%2BmouF8ZcDRe2RN6l7bNENieaqG9ZQAtZLnpoJKzT%2FFvjJR0Bq4s58aiPnOcNh%2BLHUPxbtlb90seWW%2BPy7OSa8B%2FD%2FrM%2FZuMrvi1&X-Amz-Signature=367c8e5844143c8874fcdd5bdd7f023226f26c0e1c353b3dc374eb54b743ac8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IH27PZM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEV6LCPOszavmg21R3mloTxR24As7V4Oq76%2F6Ft0zSOyAiA8LyG%2BfZ0XyaRNtNtdPQpnxqNgEQvbgU8%2F45EyGNnjPiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeKm9CsDV%2BigbtFCwKtwDmdCH5NixI1AXcxvgbmgVzCF9rHsNUziald38495Al16KqAz0ZAlBjIthSY0Bq%2B6I%2F5OPzIyg4zJ5%2Fvjofd7D6she27EjH30%2BA74buBpYKmjE1SYA2mCSJ1D7uFZmTx3qPgt4p%2FqNQdPMEk8bui90xc9tDj%2BUj2acA%2B8emQaKPczgnu0JAgecUFS3Yw8k876D3xSjaRDkAb91R%2BVyP9xtyuMhSqwvAoIAdLFzHFX0SHCX6x2TMxYOvF545KP8bNy0aANHqyz%2B3me7zntWjO4FmzfPCIeOLdMAf9xPqoO0uDHsYs%2B2a%2B64dUFLAWBr%2F0DMlzvCS0pDBoXyDzpZhWgji4yqgUVcAMdjJ8a0lJKyIGr0yKwf5SnqdRHg7z7scj5%2Fu7yW4Ks3%2Fr8ZTkR7yAZ98YM8L9e7QjqS2LNRbhnaHY9qmfwC80cUvHnMhVjYZ6F76AioyyDSy%2BXAEdnHgmldRCA4ZMIHEf2dw9TF7ZZY51fyNELHz0EaEUaGFlB4nWizvTklMKAiwwl4cQ%2F7ufngEhZfnLzG8ahArHHSE%2Fpo1rDZVqCaiKf%2BPFC7%2FCeWiINXYB7TiAHImGahnRWiiRV3xCHcAKORXBijGN51pzUcLPIk2J%2F%2BVx8%2BhKsfKO4w%2B8n4vAY6pgEHsFBcsnUDYKAiNFXviNls0yasQKU9d3nAgd9nA48ozxfOT21lwzQYznvqAm3eM8zK0CsjCH1gSxDYJXQvbGArZox8rNhScbIETXUKeZsACgpWY%2BDzHyYND%2FkUE%2BmouF8ZcDRe2RN6l7bNENieaqG9ZQAtZLnpoJKzT%2FFvjJR0Bq4s58aiPnOcNh%2BLHUPxbtlb90seWW%2BPy7OSa8B%2FD%2FrM%2FZuMrvi1&X-Amz-Signature=5322c86fc6f967b2e267c6fab050fe950081b6f5ca9dacc2f31aaebdf1a22217&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IH27PZM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEV6LCPOszavmg21R3mloTxR24As7V4Oq76%2F6Ft0zSOyAiA8LyG%2BfZ0XyaRNtNtdPQpnxqNgEQvbgU8%2F45EyGNnjPiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeKm9CsDV%2BigbtFCwKtwDmdCH5NixI1AXcxvgbmgVzCF9rHsNUziald38495Al16KqAz0ZAlBjIthSY0Bq%2B6I%2F5OPzIyg4zJ5%2Fvjofd7D6she27EjH30%2BA74buBpYKmjE1SYA2mCSJ1D7uFZmTx3qPgt4p%2FqNQdPMEk8bui90xc9tDj%2BUj2acA%2B8emQaKPczgnu0JAgecUFS3Yw8k876D3xSjaRDkAb91R%2BVyP9xtyuMhSqwvAoIAdLFzHFX0SHCX6x2TMxYOvF545KP8bNy0aANHqyz%2B3me7zntWjO4FmzfPCIeOLdMAf9xPqoO0uDHsYs%2B2a%2B64dUFLAWBr%2F0DMlzvCS0pDBoXyDzpZhWgji4yqgUVcAMdjJ8a0lJKyIGr0yKwf5SnqdRHg7z7scj5%2Fu7yW4Ks3%2Fr8ZTkR7yAZ98YM8L9e7QjqS2LNRbhnaHY9qmfwC80cUvHnMhVjYZ6F76AioyyDSy%2BXAEdnHgmldRCA4ZMIHEf2dw9TF7ZZY51fyNELHz0EaEUaGFlB4nWizvTklMKAiwwl4cQ%2F7ufngEhZfnLzG8ahArHHSE%2Fpo1rDZVqCaiKf%2BPFC7%2FCeWiINXYB7TiAHImGahnRWiiRV3xCHcAKORXBijGN51pzUcLPIk2J%2F%2BVx8%2BhKsfKO4w%2B8n4vAY6pgEHsFBcsnUDYKAiNFXviNls0yasQKU9d3nAgd9nA48ozxfOT21lwzQYznvqAm3eM8zK0CsjCH1gSxDYJXQvbGArZox8rNhScbIETXUKeZsACgpWY%2BDzHyYND%2FkUE%2BmouF8ZcDRe2RN6l7bNENieaqG9ZQAtZLnpoJKzT%2FFvjJR0Bq4s58aiPnOcNh%2BLHUPxbtlb90seWW%2BPy7OSa8B%2FD%2FrM%2FZuMrvi1&X-Amz-Signature=e290554dcc4f4b5a20fdde86f150bdb805dee8224ca33985e85b1c1c1f4052ae&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4DCDNOI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FNXMTl9ErDEN%2BbhJhK3vsFb7RdHPD5zcc7aY1EJqJ2AIgWJ2AdNzM7wCQ5LSDofcpgX2uYhkBu15qyHjOu%2BQ50QUqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLACIHvEeMr%2FA%2F%2Fp0CrcA9Td5AM7P64%2F2j3Y461Lx%2FlrodEERpnAteKhVkHeFtQWVs5FbTRCjyveKtkFDJZ1ZsHP3R%2BufG%2Byph3OE1i%2Bmtmz5EYQDNExcq6F0dTvwSnAW9r64BIYOKawjS1jF5qIR6ufMprNhwjjHPRKmxXoylFd59PW2dEyy6A2dqLxXfV1FSF6FxyhiI0V1lDofhFT0c93kRToD590CQkveHOKk3iNRYJdJY8Wt0QFV97dANkw%2BzOMRYTARyCBHp6T9JAuAMdqqjztaB0gWI%2FoWm2WMnjaCbWOGg2TEeQKfaTewSlLG9V1sLzE2swBkx39NO1kMLwk3O148GSsXX%2FvRNb%2BExIOB5QJJTsF4S%2Fiwzrgq3DAKMu90nEr4ATRiNeH6GN987vRp7QpX60R46uy2Rtk2x9SE6lVDDnyiUzOkoCOt0zs1R%2B5vQj8UXHAEMUh%2FdKg29cEQVslSxK3DkST%2FnV83I7yuAEC0NR%2FQrIzcot7cR0q3mzBWXSWFfp8yrKo4HJQfBGSzRPLXzXVw5LuYFJDLjk7%2BwVB4bv98ZCQueuJvSnKjn4LYLKtrrFIOacFL3iCUJVoeFFs31REzW%2BGJPmBEjyJjJijPPPrFo6n%2Ff%2B9L0OIbAqJ1Ywkh6PvZqKfMNHF%2BLwGOqUBtbyBeTZPdGwmOe7wz1tbo%2FyyqsAY8L2V9WIYmLmpbXGbCakVPOn8E%2BblWxvFqF3RGIpYVa7q9%2FF1HCGhRMcWCgFio0BLeL0vp2wcQwHI4EX3ySztTCI3dydrQcrL1Ayo2UzSPNJ5i2sp32jtExfl9abA%2BNjPI4k7BIAvo0s5oczNU7RX7QBhcapIrlXpelxSbmZ82jA802%2BDyMKomhEqcjvUfmDs&X-Amz-Signature=8fc167a0194d19334f1b16f5b3d7cb9c3e5bd53160b8668cd928161d0693a99e&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RVLFT2I%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEgBMb7mQmz4qD7YEsdp78A9w1WCroC6EoKro76tXJ6zAiEA4btLYeY%2Bemg2BxHo%2Brz2ht%2BrC0RedP72TRBTnwrUuyYqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOmCpkOab1wlwWe0CrcAyfEQ5YIfn0ojPsi2jAmiRhJ8GLyNbbtLRMFgIYyIiYiFd4D3Hmtx4oDK%2B8QEIfCTOS%2Fr4f51ns3jXn%2FXeWAroVrzOmLbrOd3AsXxzVrNL59vnsagGaWNdb%2BSKKYJ6XFbtbwQzZo5ZszMRpZlhKdJeBUdL3vut1c5kAcGZLQqNcyn%2BZqRxbYGpZGgSjzoVcPifo4x1pG4F3SEjE50gZaiLuRK%2F2lKCjy08cw7kBneXgpDqHyD6MLChHtAHwyjo7jXkovJTt6YHMMm6bpqwKRkHMHsMI9zLzdIy5LcyQOe5JnsNYqQklawu97B8AFB765tDc7ysRqrhUmc0qrMCuByaBX5xRL%2BhvvDlWC%2FHg%2FlxqC23BOU6lWRmBO9U3zkJ15WUAnTSBFplud%2Foc6dIQ0KmbPS83QlfK2N6MX%2BzSLQqkgb%2BD549ExrY1TFj%2BpokHY8xSxv81GYrRKsq5eKvKFwS2FzQTTFGBfKnuvCBI2ae5RAEzDBgWLmtcHRNur6%2Fe8y7fRDku%2BjBLN043%2BKKcB3RevYwfmu94iEeGy18ZnBiG%2FIMjSVb04dzOcsLRea18Iihsg7jEoYhOcWM%2FbL9NVQ9ilBr4M3h15UdUWNFCULVBJFRHQ%2FImHSpP5Cl4MMKvE%2BLwGOqUBxL7KC78K7kCQdIlI7rboIbJ7ZfJaknWvHel9ne3RVs7J%2BvpAAuOeY2PEPB0yxD4Pbhu2Y3o9SqoiIfUGJMquGavFuKP7C2Hfm6ucgUDP%2B%2BO6eWRG8f4Xw%2FTdhMY5tkG2JEViFVqaA2eZRcLbkqMb9OpuDwjsktcR5zsS0Ol%2FPLr8DpLStUo6VPNNudIgdu85gv6ac4gyuSLEBAtZXJ5cUEHDVLTA&X-Amz-Signature=b4e5f74da0d204071bb14dfc9a195334ee17e3ce65cc4437fea924ebbfb1cef3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IH27PZM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEV6LCPOszavmg21R3mloTxR24As7V4Oq76%2F6Ft0zSOyAiA8LyG%2BfZ0XyaRNtNtdPQpnxqNgEQvbgU8%2F45EyGNnjPiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeKm9CsDV%2BigbtFCwKtwDmdCH5NixI1AXcxvgbmgVzCF9rHsNUziald38495Al16KqAz0ZAlBjIthSY0Bq%2B6I%2F5OPzIyg4zJ5%2Fvjofd7D6she27EjH30%2BA74buBpYKmjE1SYA2mCSJ1D7uFZmTx3qPgt4p%2FqNQdPMEk8bui90xc9tDj%2BUj2acA%2B8emQaKPczgnu0JAgecUFS3Yw8k876D3xSjaRDkAb91R%2BVyP9xtyuMhSqwvAoIAdLFzHFX0SHCX6x2TMxYOvF545KP8bNy0aANHqyz%2B3me7zntWjO4FmzfPCIeOLdMAf9xPqoO0uDHsYs%2B2a%2B64dUFLAWBr%2F0DMlzvCS0pDBoXyDzpZhWgji4yqgUVcAMdjJ8a0lJKyIGr0yKwf5SnqdRHg7z7scj5%2Fu7yW4Ks3%2Fr8ZTkR7yAZ98YM8L9e7QjqS2LNRbhnaHY9qmfwC80cUvHnMhVjYZ6F76AioyyDSy%2BXAEdnHgmldRCA4ZMIHEf2dw9TF7ZZY51fyNELHz0EaEUaGFlB4nWizvTklMKAiwwl4cQ%2F7ufngEhZfnLzG8ahArHHSE%2Fpo1rDZVqCaiKf%2BPFC7%2FCeWiINXYB7TiAHImGahnRWiiRV3xCHcAKORXBijGN51pzUcLPIk2J%2F%2BVx8%2BhKsfKO4w%2B8n4vAY6pgEHsFBcsnUDYKAiNFXviNls0yasQKU9d3nAgd9nA48ozxfOT21lwzQYznvqAm3eM8zK0CsjCH1gSxDYJXQvbGArZox8rNhScbIETXUKeZsACgpWY%2BDzHyYND%2FkUE%2BmouF8ZcDRe2RN6l7bNENieaqG9ZQAtZLnpoJKzT%2FFvjJR0Bq4s58aiPnOcNh%2BLHUPxbtlb90seWW%2BPy7OSa8B%2FD%2FrM%2FZuMrvi1&X-Amz-Signature=269da0f53edbf1e800ae7227a8a5a06d6f165e5e624ef62dba6a6649a88180de&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IH27PZM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEV6LCPOszavmg21R3mloTxR24As7V4Oq76%2F6Ft0zSOyAiA8LyG%2BfZ0XyaRNtNtdPQpnxqNgEQvbgU8%2F45EyGNnjPiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeKm9CsDV%2BigbtFCwKtwDmdCH5NixI1AXcxvgbmgVzCF9rHsNUziald38495Al16KqAz0ZAlBjIthSY0Bq%2B6I%2F5OPzIyg4zJ5%2Fvjofd7D6she27EjH30%2BA74buBpYKmjE1SYA2mCSJ1D7uFZmTx3qPgt4p%2FqNQdPMEk8bui90xc9tDj%2BUj2acA%2B8emQaKPczgnu0JAgecUFS3Yw8k876D3xSjaRDkAb91R%2BVyP9xtyuMhSqwvAoIAdLFzHFX0SHCX6x2TMxYOvF545KP8bNy0aANHqyz%2B3me7zntWjO4FmzfPCIeOLdMAf9xPqoO0uDHsYs%2B2a%2B64dUFLAWBr%2F0DMlzvCS0pDBoXyDzpZhWgji4yqgUVcAMdjJ8a0lJKyIGr0yKwf5SnqdRHg7z7scj5%2Fu7yW4Ks3%2Fr8ZTkR7yAZ98YM8L9e7QjqS2LNRbhnaHY9qmfwC80cUvHnMhVjYZ6F76AioyyDSy%2BXAEdnHgmldRCA4ZMIHEf2dw9TF7ZZY51fyNELHz0EaEUaGFlB4nWizvTklMKAiwwl4cQ%2F7ufngEhZfnLzG8ahArHHSE%2Fpo1rDZVqCaiKf%2BPFC7%2FCeWiINXYB7TiAHImGahnRWiiRV3xCHcAKORXBijGN51pzUcLPIk2J%2F%2BVx8%2BhKsfKO4w%2B8n4vAY6pgEHsFBcsnUDYKAiNFXviNls0yasQKU9d3nAgd9nA48ozxfOT21lwzQYznvqAm3eM8zK0CsjCH1gSxDYJXQvbGArZox8rNhScbIETXUKeZsACgpWY%2BDzHyYND%2FkUE%2BmouF8ZcDRe2RN6l7bNENieaqG9ZQAtZLnpoJKzT%2FFvjJR0Bq4s58aiPnOcNh%2BLHUPxbtlb90seWW%2BPy7OSa8B%2FD%2FrM%2FZuMrvi1&X-Amz-Signature=5e33fbdad5f1812948e78eab1ed04856535017584bf50e923bddddc8df657634&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IH27PZM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEV6LCPOszavmg21R3mloTxR24As7V4Oq76%2F6Ft0zSOyAiA8LyG%2BfZ0XyaRNtNtdPQpnxqNgEQvbgU8%2F45EyGNnjPiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeKm9CsDV%2BigbtFCwKtwDmdCH5NixI1AXcxvgbmgVzCF9rHsNUziald38495Al16KqAz0ZAlBjIthSY0Bq%2B6I%2F5OPzIyg4zJ5%2Fvjofd7D6she27EjH30%2BA74buBpYKmjE1SYA2mCSJ1D7uFZmTx3qPgt4p%2FqNQdPMEk8bui90xc9tDj%2BUj2acA%2B8emQaKPczgnu0JAgecUFS3Yw8k876D3xSjaRDkAb91R%2BVyP9xtyuMhSqwvAoIAdLFzHFX0SHCX6x2TMxYOvF545KP8bNy0aANHqyz%2B3me7zntWjO4FmzfPCIeOLdMAf9xPqoO0uDHsYs%2B2a%2B64dUFLAWBr%2F0DMlzvCS0pDBoXyDzpZhWgji4yqgUVcAMdjJ8a0lJKyIGr0yKwf5SnqdRHg7z7scj5%2Fu7yW4Ks3%2Fr8ZTkR7yAZ98YM8L9e7QjqS2LNRbhnaHY9qmfwC80cUvHnMhVjYZ6F76AioyyDSy%2BXAEdnHgmldRCA4ZMIHEf2dw9TF7ZZY51fyNELHz0EaEUaGFlB4nWizvTklMKAiwwl4cQ%2F7ufngEhZfnLzG8ahArHHSE%2Fpo1rDZVqCaiKf%2BPFC7%2FCeWiINXYB7TiAHImGahnRWiiRV3xCHcAKORXBijGN51pzUcLPIk2J%2F%2BVx8%2BhKsfKO4w%2B8n4vAY6pgEHsFBcsnUDYKAiNFXviNls0yasQKU9d3nAgd9nA48ozxfOT21lwzQYznvqAm3eM8zK0CsjCH1gSxDYJXQvbGArZox8rNhScbIETXUKeZsACgpWY%2BDzHyYND%2FkUE%2BmouF8ZcDRe2RN6l7bNENieaqG9ZQAtZLnpoJKzT%2FFvjJR0Bq4s58aiPnOcNh%2BLHUPxbtlb90seWW%2BPy7OSa8B%2FD%2FrM%2FZuMrvi1&X-Amz-Signature=89da23d9b7343598d2c5cfc55ffb3fc7445c0f3a5df02195f91e38fe4d144e34&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CN3O7L4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC91i2JghtaILhFo566DPiz1Tny97OEDMPybNDeAYMjgwIhAMBS09M9Mard4WFXB%2FgkK8xv88RHetzgg6kxth%2FBca%2FfKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0hYLmq1prYX1k9Bgq3AMtt8HOE95jAD3uKp5q%2BQSv8%2Fv2J73yp86kq1YA44atr3Y9FgY5YX3ZSIgAlrKdiUYGnv5qnW6sFQanKPLClS%2F0ZMRW7PXoqNpML25d6tXn43bi0BBNhOKluMRJtwTL3kYPXEn6bxDJOEkxhigqs8h4tPo03g%2FxxFiEj6O1KKc2g5u9gXfNHPuqt%2FRI%2BVRUwusZ4xSE%2FJw4EAfNAdbggLwmHDh7lJv9Y7z9A1%2FJ70Ly29v%2FIkLwfSGTqZmLcBSp%2BqbqgnE5o8odppOkHgGrt4d0r%2BhbhVyht0S55lPHXbmqE1%2Fskzmh3bwLSWRG9T0ZISrr8ESlhF6gLt4haTVlt6IBxlMrq3XU2cUgdn8rI%2B14tHMZJIDkFYXfd%2BPe3VHtAglbSPtAswurO7MYh1cYhuqUZbT2ksx7RXQT%2F4iWHwyxR%2FmkNGQFxwph1ukXBdtsOFgOqLlmYRLoQdImPrKNYs64lr1xUnlB4eJR1%2BcVcTdChyRLj1KbHvbwHr7hm6YVfscORePbEzMcZ5WlrLDi%2FVHJV%2BmmRY%2FPI24AZfZnPnqqk1ou0g0SYgfgDuuH0OaQuWzoH3dU37xwfuIfeD4JYJzbrp3go5MsEwJirI2h4jonUi8nsbJGqieOBSzpVDCOyPi8BjqkAT5%2Bp84VFeXOV43XfHvvNczUaDZbBZY71Xvf7qMaqpPqxrTsPIlMMnXYyrvZBYrvTaGMxau%2F6IoG4qLWa1BnjQUcocmrUCmnaJKoW%2F2UGBO6JaWHikWkB796L1MbgQLZNinCp0I8bSVS0ADU9O6B5aRB9WLvq6uHFUIlse6v0Kt6g9LmCdkn1jL%2FInVk01cVgDCHjGux2FbPSSkoPmivclHHhYch&X-Amz-Signature=0347da6b3170b17e0a4b479cf9a267001a9af70c5f1c54976ef467456655cb75&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DGCY4RH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHahh2RoGulu2zR7H5vhz0gaoeMa3jLP4oC8a%2BPZFPEJAiBGd6XEucTC35lvTtixkvnDEINjUL%2F36CsrbXTEKRk0XiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvXNKuSjnyUq8QTLUKtwDYE6738zN01%2FyKTuaBdZrjJFQE%2Bk%2F%2BqMFKnxl5FRZ15ombjt%2B6pap6o%2Fl7E5G7KKS%2Bq2jfrqE0Mw5j5rO35X4ZNn9VnvEevGtHhlR%2FD9ooLywp1HYs1rgFIMWBRJvrGWvL2oEdc%2FuXnvnR7PbBba9OdSXSWOb1MBLiE5XBJGsMvlni60g4ceDclEH9So%2BNUtdzh37X3xMMouTNZ05Ra%2FLHVFaDRoozD2Z1CtXuaQRRa7j%2F%2BanEyMaHDSJ6wPyjYqVBO8PQX0GrSm3ZUgrIQdHZVTSJQQBZjIiaK40upUxfQUzBcab8sAdNqiz6rZsP3t0eH0AuVqvzxG3%2F3DuqBNHozI9fWYEQLlnHgEYeL%2BFvWRsZffHoYBLRDih0KnYMeRYPXjWAN5PD20sATJfAD7%2F90QxdnqH3EEmys7ZZzTVMhi9uySWV6tOjbrV3q%2F%2F6txLKY2dtSm5F6iRhQszSL1Q68MtpTwISYyMhI9qO0yjh1q7Us5gFwSobSZn%2Bl2qJa0Xzpj0cXeHy5qUFl1Y%2B8etjF7vJpvy%2BA0y9cVSUewkRiM5v%2BgOLNIOcxTe6gUxvCJO%2F%2FZ9z49Q6JriK2yClaf2leKHGD1B%2FY3RWQt8LLnjwPEcmvj2mUGt2mKvVOIwssP4vAY6pgFrlDrr9dldtDRE5wQPzKsBuCRR0kJ805cmEOLOb5%2BEfD3t61OX3nUsU%2FZhViKvEs3eOHXofdb9gBsf3ppVwrVUJ444BLwNFx1BFPgujjTzG64GyJaVnTwzXtPBWGHfz7woaSbb9uLCi1jptIiKt6P%2BCysgQ%2ByRTAAe4RMnDAxVD8fRGOoZFPvGdR8mrvu%2FDzBFPGJCA%2BmBFGmaX8bQY0lU0jNhjGPN&X-Amz-Signature=e6084e130cfe26a2afe775152335710a309895dc4cfcf9a22bc49095bed5aadd&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JYA47SW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBJAeWroXdDxBpiuEx%2F%2Bt9U9o%2BwgRVNPxJSBxZ2lKlVSAiA2LGE69zrbTt%2BxXIVYpnVsM%2Fss1lvVmyU5119PttoFvyqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyBaUBd%2Br4bCLbbBOKtwD0v8Kgj4qPIVJXD6UlhrqHL2AFvJQpLofAOnhFYklX%2BoUtgE9SZ973J9XpsMvMcOLb8EYn6erw2zLQvkCM%2B%2B38aQhAxvkdHkSC1htEmfpOvBO3so6eDjiH5rcjMFvAOnim6hfannPxCVox0wdDUpBOg9tdmJC8Hz2yooomYopS2rioja%2BfPOglBR%2FRMFPX9NFtsqTLwYex1aTWvWcAdbaWOOhArZgSo0npPWkVCB9D0JuPJRfMPIyE8LAyeYz5TVShbrcjZgaCZS6L040vc7V48hE76DDD0NHDfaO3syzkQSTx12KBHshNl0urBhdDctzE7JlC6rKDVXUvuXgpsgDZ2k4ordQh3VwIzQibfJH837zbtTbPD8TgOU2pRAXqABXTmCRbLndrYSVWHwgPXLsblGeWtc7Ym8r8J4FWXADgl32%2Fsd2FyyjiYibk8%2Bk9y18lwkOMYaaFOuSZakkCNb9L8tpzcE3dz%2FLjlGdYundyWQBpfaz00uM0vscG3JCionHDCsYoPVgQ7q%2Ff70w%2B0pOsZMsSvlAxbXnDxZUsN1P%2FrfgJFgeO9h3Gmks1ggc2w2pnZSDNPdWzrxxGthqvoovWxiyuDtajq8%2FmusZvKI0pHgDTk8LcDW4CKPni9cw7r34vAY6pgGZnBC%2BdX8gCShR3OHbznHl5eAsMscaSFlDyTFxjdCOSxxXOhrDp%2F2tPlKakDY49UZ7J1sNYXELuLA4g5x09pUlxxtmkvoLrsxZ5f2%2FF9Rp9MptviTe7Si%2Bp6RA2Jbrzn7FS8Hdk451MUk22HGqO2MKYB0e6bGeEE9yQtsZLdph0iEz9%2Fi0uO%2B6jAcshwJTNAYLUGrpxBdxCMVLGkBsYrfxUCcI4mop&X-Amz-Signature=f7d6b6cdd81c8875c59923b83c6b73968d66ce2de7178d368c9038d852a3c8b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIC62F2I%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTTd8Sdvx6qCQCGafmz%2F6Ka2%2BNA4g501JP%2Bmhs7pXtbwIgIyf2vzPuZuSR%2BiWbZOcDkiVhjdx%2Bvz3LCJTi7xcQE1oqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIx0akAp7Kf%2FHx5XvSrcA2r%2F3VHb8UF%2B2gQWjAJa4kJ%2F%2Bmhkv%2FeFbVsUa5nXZMxih98PTNz7hWMo7IWu50HYlwFZzyn3KOyaohyQ0Epsy0AmmWpd2eYdkKOQaodqAU18pOyawWoIjMMPIp0jG161C2SPB0Z3PNLCD854PuMtacfIWSnD%2BRFlVOS%2Fnv0%2FzpuwaYkxNcU%2BSwFfDnAcB86tR232wcnNcNr5amjqwLUiufwCY8GHJ8Zl%2F46f54LxyZDL1mAZL2Ay7gt1xrlUjtSVUbuarA4KXL8Vow7Eq%2B%2FLZWR4GIT0DaaWxDx8qTM%2F40dIULU5h7DHvoKj5PIee83YkPopNPIN2qQBODXkKWcEVpCTbbd%2FqRiTAZep%2Fw%2FJHii%2F283fkzUeHgeHmshbfV%2FnlbpQNTBIeI7L7Ma2KHMvBe44fnMXO%2BMHLzgrdtTUFlwLyf6xbJdS3mVf0WyS9PiLHRqYNm9EgOJOGiXXzcFT7cTvOkvDfKGarQmSTvTUVQ1TF2gfYCM%2FglvP1HQ0hf%2B9qzuNuGCAP0ySIZgrHfVYQUHhmXp9yB0CYzVnQVqMmYw%2FXkHSeTkfMHQF4jDVWhqufxFLFrwc6B90Pnf5xBMGXWM8MHtz7%2FDCywptfTsXLAeX4HxrgA8FT8w11B21MJzC%2BLwGOqUByTIZsshAt1P99U%2FkIL0kxI42F44WwanxamovYvf5gdiff25fEqzrVaG6k0x5QSAfyOHJykazyEehgd%2BKhXc20vYBGFRV43ozU9rtCBq9KQxW0SD3zMn8OgqD2L8M7gHc1QL73G85b7%2BxwegKm6RJH3fKlqky0%2FhQj3nBWp5MWreR%2FrOwKviARHPJA2gNCPJ%2BVQ%2BM870H44i2%2B74Tsji6LW6Y1URo&X-Amz-Signature=b284d6a44707fc3a2998acc674dcd0550a0a889752d0f1c061b3ccfcd914e8ab&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIC62F2I%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTTd8Sdvx6qCQCGafmz%2F6Ka2%2BNA4g501JP%2Bmhs7pXtbwIgIyf2vzPuZuSR%2BiWbZOcDkiVhjdx%2Bvz3LCJTi7xcQE1oqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIx0akAp7Kf%2FHx5XvSrcA2r%2F3VHb8UF%2B2gQWjAJa4kJ%2F%2Bmhkv%2FeFbVsUa5nXZMxih98PTNz7hWMo7IWu50HYlwFZzyn3KOyaohyQ0Epsy0AmmWpd2eYdkKOQaodqAU18pOyawWoIjMMPIp0jG161C2SPB0Z3PNLCD854PuMtacfIWSnD%2BRFlVOS%2Fnv0%2FzpuwaYkxNcU%2BSwFfDnAcB86tR232wcnNcNr5amjqwLUiufwCY8GHJ8Zl%2F46f54LxyZDL1mAZL2Ay7gt1xrlUjtSVUbuarA4KXL8Vow7Eq%2B%2FLZWR4GIT0DaaWxDx8qTM%2F40dIULU5h7DHvoKj5PIee83YkPopNPIN2qQBODXkKWcEVpCTbbd%2FqRiTAZep%2Fw%2FJHii%2F283fkzUeHgeHmshbfV%2FnlbpQNTBIeI7L7Ma2KHMvBe44fnMXO%2BMHLzgrdtTUFlwLyf6xbJdS3mVf0WyS9PiLHRqYNm9EgOJOGiXXzcFT7cTvOkvDfKGarQmSTvTUVQ1TF2gfYCM%2FglvP1HQ0hf%2B9qzuNuGCAP0ySIZgrHfVYQUHhmXp9yB0CYzVnQVqMmYw%2FXkHSeTkfMHQF4jDVWhqufxFLFrwc6B90Pnf5xBMGXWM8MHtz7%2FDCywptfTsXLAeX4HxrgA8FT8w11B21MJzC%2BLwGOqUByTIZsshAt1P99U%2FkIL0kxI42F44WwanxamovYvf5gdiff25fEqzrVaG6k0x5QSAfyOHJykazyEehgd%2BKhXc20vYBGFRV43ozU9rtCBq9KQxW0SD3zMn8OgqD2L8M7gHc1QL73G85b7%2BxwegKm6RJH3fKlqky0%2FhQj3nBWp5MWreR%2FrOwKviARHPJA2gNCPJ%2BVQ%2BM870H44i2%2B74Tsji6LW6Y1URo&X-Amz-Signature=91591ebbb76a529c731b14e8e0697584d40c99dc310fd8fee23e89d44c25c2ec&X-Amz-SignedHeaders=host&x-id=GetObject)

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
