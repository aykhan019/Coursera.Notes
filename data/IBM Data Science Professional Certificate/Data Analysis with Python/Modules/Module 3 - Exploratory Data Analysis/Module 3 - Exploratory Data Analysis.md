

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTC6DXKR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDJ0IDfB%2FXL0FvOe6cH5RAfHnkeARTQZNFIlfq6A6eVVgIhAOOVUgRrfbHrHsAsMdL4i1gnedW0TT3Z4K37zgH3AR4pKv8DCGkQABoMNjM3NDIzMTgzODA1Igx%2B5AN8%2B%2FpuFFRO2mMq3ANg9pzYgXDPCwl3jg8psziE93dE4jVCIIJxQxtGa5QLJLLpkho07arAqULkN3Xi5Yb7nbvYaRkehQtIuWknn3ZBcfzN56M8ndYQsWEtMwL1wj1%2FQyDMLHnfh8JJDJi9nWIrWV3fwd9l64X7WnJE2uwU1PWnJiA9ze3LwZUa%2Bm3jaHneUTQi3inqCDtTqtUOekJW7xcVSQ%2BJfiO7rIENB1T6uqxxq4Fd6%2BOcpn8jrgbMJFhma2mi4fbe2CKCzeCptoGKCA2ZHcqxH%2FE17ETF27Ik4OFb%2BL6hZ%2Bs4uCk4bQpBPyL0PjXPM7K7MHCsLtcVviLuhCMP5DC5g72rNnV5zrg71Va%2Fsdpxf3asTrg%2F39A3qVZ4v7j3q3J%2BquTKmhhlx%2FFlB%2F3F%2BHxXj7ui9fUGb%2F3pPq5nfhJanhSE4W4Tz5kPOR4LipB4xYZQ6CfyBav8zNG0faJ4VT4iXcwIG5wD%2FAWVSpiD0vtXwYEJCP%2Bt8RrSXeAaQfNYntbCM8dxqQa3C0MUXoYtqy%2BviFYbKWhW1oopQerGyAL%2BDilsysNgMTeBqXJRSIpHn9%2FCSCorl3VnlD87z9PZ%2BajLQqkVvt4Ol8kw7ckoPTxamKmB435RprFXJgsevGpZtNFfSWOZlTCRmpW9BjqkAXeqgPMoeCaO0FdLVkOwZoCCmyy0fZe8hd962nZUn9pzzBlvigVTZaDxzrs9OqrLq1Px%2FoxsFOhI0cSimTnihHmFCHIpWkfkFsdHNaGe8StH2DQ3obM5Mrwx9EYwOwpEnzw6fd3PioRywlXaYAGvg7RgnETHrHlm2ytEsgRpH0jqTqpCGH5DBp5zOsC0O7TOmVtANTBO1Z%2FUiexZ0oEOhnfqyXgS&X-Amz-Signature=c20e79a31dafac2fcccb64d6c36ca288319f4d9337ad521d101e492eba923214&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTC6DXKR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDJ0IDfB%2FXL0FvOe6cH5RAfHnkeARTQZNFIlfq6A6eVVgIhAOOVUgRrfbHrHsAsMdL4i1gnedW0TT3Z4K37zgH3AR4pKv8DCGkQABoMNjM3NDIzMTgzODA1Igx%2B5AN8%2B%2FpuFFRO2mMq3ANg9pzYgXDPCwl3jg8psziE93dE4jVCIIJxQxtGa5QLJLLpkho07arAqULkN3Xi5Yb7nbvYaRkehQtIuWknn3ZBcfzN56M8ndYQsWEtMwL1wj1%2FQyDMLHnfh8JJDJi9nWIrWV3fwd9l64X7WnJE2uwU1PWnJiA9ze3LwZUa%2Bm3jaHneUTQi3inqCDtTqtUOekJW7xcVSQ%2BJfiO7rIENB1T6uqxxq4Fd6%2BOcpn8jrgbMJFhma2mi4fbe2CKCzeCptoGKCA2ZHcqxH%2FE17ETF27Ik4OFb%2BL6hZ%2Bs4uCk4bQpBPyL0PjXPM7K7MHCsLtcVviLuhCMP5DC5g72rNnV5zrg71Va%2Fsdpxf3asTrg%2F39A3qVZ4v7j3q3J%2BquTKmhhlx%2FFlB%2F3F%2BHxXj7ui9fUGb%2F3pPq5nfhJanhSE4W4Tz5kPOR4LipB4xYZQ6CfyBav8zNG0faJ4VT4iXcwIG5wD%2FAWVSpiD0vtXwYEJCP%2Bt8RrSXeAaQfNYntbCM8dxqQa3C0MUXoYtqy%2BviFYbKWhW1oopQerGyAL%2BDilsysNgMTeBqXJRSIpHn9%2FCSCorl3VnlD87z9PZ%2BajLQqkVvt4Ol8kw7ckoPTxamKmB435RprFXJgsevGpZtNFfSWOZlTCRmpW9BjqkAXeqgPMoeCaO0FdLVkOwZoCCmyy0fZe8hd962nZUn9pzzBlvigVTZaDxzrs9OqrLq1Px%2FoxsFOhI0cSimTnihHmFCHIpWkfkFsdHNaGe8StH2DQ3obM5Mrwx9EYwOwpEnzw6fd3PioRywlXaYAGvg7RgnETHrHlm2ytEsgRpH0jqTqpCGH5DBp5zOsC0O7TOmVtANTBO1Z%2FUiexZ0oEOhnfqyXgS&X-Amz-Signature=9b95b962b7d3897ca56219337b846de1d07cdc0f680e994ef546e0089a4bcee0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTC6DXKR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDJ0IDfB%2FXL0FvOe6cH5RAfHnkeARTQZNFIlfq6A6eVVgIhAOOVUgRrfbHrHsAsMdL4i1gnedW0TT3Z4K37zgH3AR4pKv8DCGkQABoMNjM3NDIzMTgzODA1Igx%2B5AN8%2B%2FpuFFRO2mMq3ANg9pzYgXDPCwl3jg8psziE93dE4jVCIIJxQxtGa5QLJLLpkho07arAqULkN3Xi5Yb7nbvYaRkehQtIuWknn3ZBcfzN56M8ndYQsWEtMwL1wj1%2FQyDMLHnfh8JJDJi9nWIrWV3fwd9l64X7WnJE2uwU1PWnJiA9ze3LwZUa%2Bm3jaHneUTQi3inqCDtTqtUOekJW7xcVSQ%2BJfiO7rIENB1T6uqxxq4Fd6%2BOcpn8jrgbMJFhma2mi4fbe2CKCzeCptoGKCA2ZHcqxH%2FE17ETF27Ik4OFb%2BL6hZ%2Bs4uCk4bQpBPyL0PjXPM7K7MHCsLtcVviLuhCMP5DC5g72rNnV5zrg71Va%2Fsdpxf3asTrg%2F39A3qVZ4v7j3q3J%2BquTKmhhlx%2FFlB%2F3F%2BHxXj7ui9fUGb%2F3pPq5nfhJanhSE4W4Tz5kPOR4LipB4xYZQ6CfyBav8zNG0faJ4VT4iXcwIG5wD%2FAWVSpiD0vtXwYEJCP%2Bt8RrSXeAaQfNYntbCM8dxqQa3C0MUXoYtqy%2BviFYbKWhW1oopQerGyAL%2BDilsysNgMTeBqXJRSIpHn9%2FCSCorl3VnlD87z9PZ%2BajLQqkVvt4Ol8kw7ckoPTxamKmB435RprFXJgsevGpZtNFfSWOZlTCRmpW9BjqkAXeqgPMoeCaO0FdLVkOwZoCCmyy0fZe8hd962nZUn9pzzBlvigVTZaDxzrs9OqrLq1Px%2FoxsFOhI0cSimTnihHmFCHIpWkfkFsdHNaGe8StH2DQ3obM5Mrwx9EYwOwpEnzw6fd3PioRywlXaYAGvg7RgnETHrHlm2ytEsgRpH0jqTqpCGH5DBp5zOsC0O7TOmVtANTBO1Z%2FUiexZ0oEOhnfqyXgS&X-Amz-Signature=56bd3a61edb41cbd39f8732bc6773c3acadb9c80fd4c7fd438c1ff99bf3b8835&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KCIH2H2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCID8c6ffcNIeM5P3qfsWdLP56lleZqYiME0sAJJ4dIqY1AiEA44uqNqxvEkUKT9qxRdGlrPVaRpQLjhPV%2BHv5x0Tuwq8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2Fx939LMP0buTBOQSrcA%2Bin1wvs38vClaBDsZ8eZtg7bC3URZcHQinCjXOCnOy%2Bp4nKImYtmuWhbIVishtHzUTtRauolwhv76Z%2FWeqsjDhWqQSLCEaYlyIrlxz2AExmH4R%2FFlgWm%2FPP65aAE4DgL%2Ftq1Atj565DVlohjHaLeWZfnc5vWRTKOgz2Rw%2Fhw9PK5DQw9Bi38k%2BCEFTRrVRRR%2FVDGaTCdT50J%2BK5ngc1joyIEurWUrA7%2Bap0GQin%2Bq1B%2FUU6VUriVnskm9LEW5L0%2BraVLv1kADHeXu4Dc3GlqnvPrrsqhK%2B5ibuzAlWlONcpqEgTNEI9GMAk991XHhOg%2F6G4eZl28JGVwWkW78ovVac7PRytdiFxs%2BDa79I837zBm3E%2BGYDs9jThh%2BCxY0TYQPP8MbT4%2FBYAb3trjZjMNbyFrlKda8likejZ%2BBVDW7ZciYcfaRvOuOogfjFYPffhzwlYCwk0i1t%2BjWOKOP%2F%2FsU3MxWK%2FWAxIjX5XLA9Ovu8czm7BuJDz6iNvCISVEEo%2BFDETI5FSQkOnCQZ0ka8MDo9%2BjXGKTrkpC9e%2Fc4Yo3qnRDGJHQtoxD5h9dmSaKFC56RQ9tGSNRKyWTOamYEgOXcRVjXe6me9yCcdnbnfsV5qRpTb%2Fqvp%2Bar9xmj8aMNqZlb0GOqUBAhJqxA6bOntfOzY%2BGOpjGynIy9OkrRiXxDfRa4Q4rxVv0Y6ucB0QtjCkWij5Iz8%2FFNesw6l3qi0PFlEW7JH8Wb8BlHdJQTnmaUXlm9qjFWO%2Fwt8Ah5iRpgTuyAfA0BEZXkDujCdkmXw2qGr9TGoZFgvIlY3yplZ4A6AwmL9adB8mB%2BskW1CK2Uptdm%2BDT1BUB%2FrFmQxDo1KgOeqmxqT%2F4omKmwMe&X-Amz-Signature=39ddd66e2163946e026cb70afe5f57a9f0a2fb07f0219fde4187563c38a283c7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KCIH2H2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCID8c6ffcNIeM5P3qfsWdLP56lleZqYiME0sAJJ4dIqY1AiEA44uqNqxvEkUKT9qxRdGlrPVaRpQLjhPV%2BHv5x0Tuwq8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2Fx939LMP0buTBOQSrcA%2Bin1wvs38vClaBDsZ8eZtg7bC3URZcHQinCjXOCnOy%2Bp4nKImYtmuWhbIVishtHzUTtRauolwhv76Z%2FWeqsjDhWqQSLCEaYlyIrlxz2AExmH4R%2FFlgWm%2FPP65aAE4DgL%2Ftq1Atj565DVlohjHaLeWZfnc5vWRTKOgz2Rw%2Fhw9PK5DQw9Bi38k%2BCEFTRrVRRR%2FVDGaTCdT50J%2BK5ngc1joyIEurWUrA7%2Bap0GQin%2Bq1B%2FUU6VUriVnskm9LEW5L0%2BraVLv1kADHeXu4Dc3GlqnvPrrsqhK%2B5ibuzAlWlONcpqEgTNEI9GMAk991XHhOg%2F6G4eZl28JGVwWkW78ovVac7PRytdiFxs%2BDa79I837zBm3E%2BGYDs9jThh%2BCxY0TYQPP8MbT4%2FBYAb3trjZjMNbyFrlKda8likejZ%2BBVDW7ZciYcfaRvOuOogfjFYPffhzwlYCwk0i1t%2BjWOKOP%2F%2FsU3MxWK%2FWAxIjX5XLA9Ovu8czm7BuJDz6iNvCISVEEo%2BFDETI5FSQkOnCQZ0ka8MDo9%2BjXGKTrkpC9e%2Fc4Yo3qnRDGJHQtoxD5h9dmSaKFC56RQ9tGSNRKyWTOamYEgOXcRVjXe6me9yCcdnbnfsV5qRpTb%2Fqvp%2Bar9xmj8aMNqZlb0GOqUBAhJqxA6bOntfOzY%2BGOpjGynIy9OkrRiXxDfRa4Q4rxVv0Y6ucB0QtjCkWij5Iz8%2FFNesw6l3qi0PFlEW7JH8Wb8BlHdJQTnmaUXlm9qjFWO%2Fwt8Ah5iRpgTuyAfA0BEZXkDujCdkmXw2qGr9TGoZFgvIlY3yplZ4A6AwmL9adB8mB%2BskW1CK2Uptdm%2BDT1BUB%2FrFmQxDo1KgOeqmxqT%2F4omKmwMe&X-Amz-Signature=eadf35deccdf750ef6ff47d54f816d4d51fc5ca994c15489c53c1b6368947a55&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KCIH2H2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCID8c6ffcNIeM5P3qfsWdLP56lleZqYiME0sAJJ4dIqY1AiEA44uqNqxvEkUKT9qxRdGlrPVaRpQLjhPV%2BHv5x0Tuwq8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2Fx939LMP0buTBOQSrcA%2Bin1wvs38vClaBDsZ8eZtg7bC3URZcHQinCjXOCnOy%2Bp4nKImYtmuWhbIVishtHzUTtRauolwhv76Z%2FWeqsjDhWqQSLCEaYlyIrlxz2AExmH4R%2FFlgWm%2FPP65aAE4DgL%2Ftq1Atj565DVlohjHaLeWZfnc5vWRTKOgz2Rw%2Fhw9PK5DQw9Bi38k%2BCEFTRrVRRR%2FVDGaTCdT50J%2BK5ngc1joyIEurWUrA7%2Bap0GQin%2Bq1B%2FUU6VUriVnskm9LEW5L0%2BraVLv1kADHeXu4Dc3GlqnvPrrsqhK%2B5ibuzAlWlONcpqEgTNEI9GMAk991XHhOg%2F6G4eZl28JGVwWkW78ovVac7PRytdiFxs%2BDa79I837zBm3E%2BGYDs9jThh%2BCxY0TYQPP8MbT4%2FBYAb3trjZjMNbyFrlKda8likejZ%2BBVDW7ZciYcfaRvOuOogfjFYPffhzwlYCwk0i1t%2BjWOKOP%2F%2FsU3MxWK%2FWAxIjX5XLA9Ovu8czm7BuJDz6iNvCISVEEo%2BFDETI5FSQkOnCQZ0ka8MDo9%2BjXGKTrkpC9e%2Fc4Yo3qnRDGJHQtoxD5h9dmSaKFC56RQ9tGSNRKyWTOamYEgOXcRVjXe6me9yCcdnbnfsV5qRpTb%2Fqvp%2Bar9xmj8aMNqZlb0GOqUBAhJqxA6bOntfOzY%2BGOpjGynIy9OkrRiXxDfRa4Q4rxVv0Y6ucB0QtjCkWij5Iz8%2FFNesw6l3qi0PFlEW7JH8Wb8BlHdJQTnmaUXlm9qjFWO%2Fwt8Ah5iRpgTuyAfA0BEZXkDujCdkmXw2qGr9TGoZFgvIlY3yplZ4A6AwmL9adB8mB%2BskW1CK2Uptdm%2BDT1BUB%2FrFmQxDo1KgOeqmxqT%2F4omKmwMe&X-Amz-Signature=2da9ff683fce88473fb1be655473e59da34f287907ff7f22d7178e6079d68593&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KCIH2H2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCID8c6ffcNIeM5P3qfsWdLP56lleZqYiME0sAJJ4dIqY1AiEA44uqNqxvEkUKT9qxRdGlrPVaRpQLjhPV%2BHv5x0Tuwq8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2Fx939LMP0buTBOQSrcA%2Bin1wvs38vClaBDsZ8eZtg7bC3URZcHQinCjXOCnOy%2Bp4nKImYtmuWhbIVishtHzUTtRauolwhv76Z%2FWeqsjDhWqQSLCEaYlyIrlxz2AExmH4R%2FFlgWm%2FPP65aAE4DgL%2Ftq1Atj565DVlohjHaLeWZfnc5vWRTKOgz2Rw%2Fhw9PK5DQw9Bi38k%2BCEFTRrVRRR%2FVDGaTCdT50J%2BK5ngc1joyIEurWUrA7%2Bap0GQin%2Bq1B%2FUU6VUriVnskm9LEW5L0%2BraVLv1kADHeXu4Dc3GlqnvPrrsqhK%2B5ibuzAlWlONcpqEgTNEI9GMAk991XHhOg%2F6G4eZl28JGVwWkW78ovVac7PRytdiFxs%2BDa79I837zBm3E%2BGYDs9jThh%2BCxY0TYQPP8MbT4%2FBYAb3trjZjMNbyFrlKda8likejZ%2BBVDW7ZciYcfaRvOuOogfjFYPffhzwlYCwk0i1t%2BjWOKOP%2F%2FsU3MxWK%2FWAxIjX5XLA9Ovu8czm7BuJDz6iNvCISVEEo%2BFDETI5FSQkOnCQZ0ka8MDo9%2BjXGKTrkpC9e%2Fc4Yo3qnRDGJHQtoxD5h9dmSaKFC56RQ9tGSNRKyWTOamYEgOXcRVjXe6me9yCcdnbnfsV5qRpTb%2Fqvp%2Bar9xmj8aMNqZlb0GOqUBAhJqxA6bOntfOzY%2BGOpjGynIy9OkrRiXxDfRa4Q4rxVv0Y6ucB0QtjCkWij5Iz8%2FFNesw6l3qi0PFlEW7JH8Wb8BlHdJQTnmaUXlm9qjFWO%2Fwt8Ah5iRpgTuyAfA0BEZXkDujCdkmXw2qGr9TGoZFgvIlY3yplZ4A6AwmL9adB8mB%2BskW1CK2Uptdm%2BDT1BUB%2FrFmQxDo1KgOeqmxqT%2F4omKmwMe&X-Amz-Signature=1a6330de0e1412d09cd7c019b4c9906ec25432a2d22a30b48ae5a076780d19f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KCIH2H2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCID8c6ffcNIeM5P3qfsWdLP56lleZqYiME0sAJJ4dIqY1AiEA44uqNqxvEkUKT9qxRdGlrPVaRpQLjhPV%2BHv5x0Tuwq8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2Fx939LMP0buTBOQSrcA%2Bin1wvs38vClaBDsZ8eZtg7bC3URZcHQinCjXOCnOy%2Bp4nKImYtmuWhbIVishtHzUTtRauolwhv76Z%2FWeqsjDhWqQSLCEaYlyIrlxz2AExmH4R%2FFlgWm%2FPP65aAE4DgL%2Ftq1Atj565DVlohjHaLeWZfnc5vWRTKOgz2Rw%2Fhw9PK5DQw9Bi38k%2BCEFTRrVRRR%2FVDGaTCdT50J%2BK5ngc1joyIEurWUrA7%2Bap0GQin%2Bq1B%2FUU6VUriVnskm9LEW5L0%2BraVLv1kADHeXu4Dc3GlqnvPrrsqhK%2B5ibuzAlWlONcpqEgTNEI9GMAk991XHhOg%2F6G4eZl28JGVwWkW78ovVac7PRytdiFxs%2BDa79I837zBm3E%2BGYDs9jThh%2BCxY0TYQPP8MbT4%2FBYAb3trjZjMNbyFrlKda8likejZ%2BBVDW7ZciYcfaRvOuOogfjFYPffhzwlYCwk0i1t%2BjWOKOP%2F%2FsU3MxWK%2FWAxIjX5XLA9Ovu8czm7BuJDz6iNvCISVEEo%2BFDETI5FSQkOnCQZ0ka8MDo9%2BjXGKTrkpC9e%2Fc4Yo3qnRDGJHQtoxD5h9dmSaKFC56RQ9tGSNRKyWTOamYEgOXcRVjXe6me9yCcdnbnfsV5qRpTb%2Fqvp%2Bar9xmj8aMNqZlb0GOqUBAhJqxA6bOntfOzY%2BGOpjGynIy9OkrRiXxDfRa4Q4rxVv0Y6ucB0QtjCkWij5Iz8%2FFNesw6l3qi0PFlEW7JH8Wb8BlHdJQTnmaUXlm9qjFWO%2Fwt8Ah5iRpgTuyAfA0BEZXkDujCdkmXw2qGr9TGoZFgvIlY3yplZ4A6AwmL9adB8mB%2BskW1CK2Uptdm%2BDT1BUB%2FrFmQxDo1KgOeqmxqT%2F4omKmwMe&X-Amz-Signature=cf9c729d002904a6f0bf332e260eee616e628f10438aaa9bb7985b49beeb841a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KCIH2H2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCID8c6ffcNIeM5P3qfsWdLP56lleZqYiME0sAJJ4dIqY1AiEA44uqNqxvEkUKT9qxRdGlrPVaRpQLjhPV%2BHv5x0Tuwq8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2Fx939LMP0buTBOQSrcA%2Bin1wvs38vClaBDsZ8eZtg7bC3URZcHQinCjXOCnOy%2Bp4nKImYtmuWhbIVishtHzUTtRauolwhv76Z%2FWeqsjDhWqQSLCEaYlyIrlxz2AExmH4R%2FFlgWm%2FPP65aAE4DgL%2Ftq1Atj565DVlohjHaLeWZfnc5vWRTKOgz2Rw%2Fhw9PK5DQw9Bi38k%2BCEFTRrVRRR%2FVDGaTCdT50J%2BK5ngc1joyIEurWUrA7%2Bap0GQin%2Bq1B%2FUU6VUriVnskm9LEW5L0%2BraVLv1kADHeXu4Dc3GlqnvPrrsqhK%2B5ibuzAlWlONcpqEgTNEI9GMAk991XHhOg%2F6G4eZl28JGVwWkW78ovVac7PRytdiFxs%2BDa79I837zBm3E%2BGYDs9jThh%2BCxY0TYQPP8MbT4%2FBYAb3trjZjMNbyFrlKda8likejZ%2BBVDW7ZciYcfaRvOuOogfjFYPffhzwlYCwk0i1t%2BjWOKOP%2F%2FsU3MxWK%2FWAxIjX5XLA9Ovu8czm7BuJDz6iNvCISVEEo%2BFDETI5FSQkOnCQZ0ka8MDo9%2BjXGKTrkpC9e%2Fc4Yo3qnRDGJHQtoxD5h9dmSaKFC56RQ9tGSNRKyWTOamYEgOXcRVjXe6me9yCcdnbnfsV5qRpTb%2Fqvp%2Bar9xmj8aMNqZlb0GOqUBAhJqxA6bOntfOzY%2BGOpjGynIy9OkrRiXxDfRa4Q4rxVv0Y6ucB0QtjCkWij5Iz8%2FFNesw6l3qi0PFlEW7JH8Wb8BlHdJQTnmaUXlm9qjFWO%2Fwt8Ah5iRpgTuyAfA0BEZXkDujCdkmXw2qGr9TGoZFgvIlY3yplZ4A6AwmL9adB8mB%2BskW1CK2Uptdm%2BDT1BUB%2FrFmQxDo1KgOeqmxqT%2F4omKmwMe&X-Amz-Signature=01d038b9344b073f82b988c8a7a2b470c5ad4f439ff3f6bda76b7f7375770415&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662GQGLLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQD1XAFxCX7UYYBEF4gZ1FzkiGxQursrcb1dBGkGxA8ZuwIhAL4vfzAj8naq2M9w76gtLPqWAR3AZ8djbFSIQVQ1ehzOKv8DCGkQABoMNjM3NDIzMTgzODA1IgxWQ4SIi%2BLbrejhd3sq3AMsfj4JGT60dNMoiQ4IHxMryzbKtARRkJDSEX2n4K1854ubT0r9OoQSld7nNRSXxKJmZaPK35X6KVDUm6mx%2F1HEFwdYi%2BLx0UFbbyBpve7J0jv%2FrPiW%2F%2BNAv%2BZGjyuabzhDTKAbgLH0R6KtcUo%2FTDkeRPj1eOx0RQMCUd0GqkVsgt5wMA2c9p1KgC4wfQ%2BE2Cq7bZ2KmJJbpyxXEncxL4SIU1yGo%2F9vbeBtpIxINm%2FNbwDifIygu5brJn4x4%2Bma1CkjRLFiIsIjrmahUEAcarcxcOKHtvJPEn6eg1IqCIGnc6IMrYvyjX1oCTC9pa7fcerrR%2FT58sU34DzPBxV5QnVuvKvohxQL6CgBjrI0xrfjkpzDRaM%2FkSu7G6kDgwsCVseRyc6acMXvHv20RbFpr8jOOGnwfJ1IXb4KSfwZnMb%2BwTuYJA2fktkHlIJWPpGHZl3KGkdA%2Fx3J%2FiJ%2BMdcxTmonjS%2FKOOm0jUi0ZLGA7bIXg57EIoHbndPmuV9lq3rpbiwKwTqMNRR9Gv3pMlxQKZkLbo0cAd9FwV1F41hvaXgPWbncyJAQbeP4rRUeUCXRi7dM%2B5TLrM8Apg1Y6w1KCOMIFrhO%2FNqdRS5Mb6%2BiQKahmmWUBPGjR7f7CAsGbTCmmpW9BjqkAVYoDSLyxgNmCH5%2FmY4NQ7FceV6jpXIDvlE0bgMGNHvVzfaj%2FGhZ79iVZj0o03Std%2BaQehbSY%2BYM3WHZIZJP%2Bqazbqin35BHURREzc%2BRfFW0ceDVWYcTFv%2FijlVO%2FMQYenFUmEyJL3ZOk9mpicVyJvu6txzlVTY6wDGWlEDjVKuZpcXINeHx9yRkBaSI29EBQMp5f%2FNEOyY4opwwvMv3iz%2BBF%2B3E&X-Amz-Signature=247f07497bbc85c844e59f33047d30896c59aa3cc9e7fa07b6394f6eaa6ab922&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVHPAGF4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIHwIWn6%2BdNAyQkVjh%2FQIuLlpJHlCHAdFrFvP%2BWUZ9IJBAiBTAKh7wqlxIlL5ICYA3TXsZy8DOk1ZR2kt%2FbXXg0XQEyr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMPeeiMJ2QV22WRg2EKtwDSNS%2FkhAJ0u5wYw%2F6M517D0OUSlnOwBw3RibFWzsI3apkbainMFNRI7RDLkdRpBKEUwD3o6iBN9CiEWGi6DA0ecMScqCl5EsqG9ZEiR22UN1P3Yq%2BL%2FqpFOv1YAkw2aJe9Uqtd5s37fmqbC9ebgK7ucPBtTfKedo1PeXzWXCsWQszCgNHUKSIAqVQBX07%2BS3wMJI0X1V0J%2F8jsm9nulfPBbE2Vt%2BjSTy9cyfZaJhneQvZzQv3%2FHF%2Fwc9%2B8C2MWAkvcPKYlMB4SS5P4PhtL2oizCxC6DefelLKI7kGQlZTCGaivm9eECTII2mq3yYIsXfOis5BSfkcnkB%2B373b1l2OyjsVqYLQ3lgl1lzAwA2acL%2BBtlt5vL7s%2BFCfnDDLqyzoLH5eXr4nC4kOxSzChtqeYixKm9cw9qgdhMXPOrDXRVdsiGGkUtbWOC2OVgpOi9gwGthbA0y4sLZFVeM0zWcom83n3r6Jt08W43mz3dmF0HSCjNkpH%2BjUzkj4VyPRUUftbeuGrz0%2BaSB3NF4p9q8uVkd4mMxu378xBPZOcr1tdCU8bujXLQk7z6MrrQZc4Fx4cmYi5ooLlu4HW2t3sktBAnz04puCKXECNatLpq88DmF8kTDz3g3EPWsiXP4w2ZqVvQY6pgEFwSUP8KQ0%2BRZ0Wfzjp635DGVQvbo6%2B26mWVnqhEdrjra8vnAbsouEI7CxbGIAM0iiZHNbEleo16agbDbej%2B%2BrEcsrn9YRsZE7QcP6mjjQUO5NZ5hXgDpLQVIWJt8gvc1o%2FTcp3tNV5LkyYb%2FQwwv9Yv008eLhYUFJh21C995J5igYX9VTVBh0EFBQw3ynqrgi4MrYtIXPZIGaZ4gKpnBdu2%2BUCS5l&X-Amz-Signature=00c75b6cefe398b51afbcf37a4941be2f7989d0636362b02ed2d5ea71a0a92fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KCIH2H2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCID8c6ffcNIeM5P3qfsWdLP56lleZqYiME0sAJJ4dIqY1AiEA44uqNqxvEkUKT9qxRdGlrPVaRpQLjhPV%2BHv5x0Tuwq8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2Fx939LMP0buTBOQSrcA%2Bin1wvs38vClaBDsZ8eZtg7bC3URZcHQinCjXOCnOy%2Bp4nKImYtmuWhbIVishtHzUTtRauolwhv76Z%2FWeqsjDhWqQSLCEaYlyIrlxz2AExmH4R%2FFlgWm%2FPP65aAE4DgL%2Ftq1Atj565DVlohjHaLeWZfnc5vWRTKOgz2Rw%2Fhw9PK5DQw9Bi38k%2BCEFTRrVRRR%2FVDGaTCdT50J%2BK5ngc1joyIEurWUrA7%2Bap0GQin%2Bq1B%2FUU6VUriVnskm9LEW5L0%2BraVLv1kADHeXu4Dc3GlqnvPrrsqhK%2B5ibuzAlWlONcpqEgTNEI9GMAk991XHhOg%2F6G4eZl28JGVwWkW78ovVac7PRytdiFxs%2BDa79I837zBm3E%2BGYDs9jThh%2BCxY0TYQPP8MbT4%2FBYAb3trjZjMNbyFrlKda8likejZ%2BBVDW7ZciYcfaRvOuOogfjFYPffhzwlYCwk0i1t%2BjWOKOP%2F%2FsU3MxWK%2FWAxIjX5XLA9Ovu8czm7BuJDz6iNvCISVEEo%2BFDETI5FSQkOnCQZ0ka8MDo9%2BjXGKTrkpC9e%2Fc4Yo3qnRDGJHQtoxD5h9dmSaKFC56RQ9tGSNRKyWTOamYEgOXcRVjXe6me9yCcdnbnfsV5qRpTb%2Fqvp%2Bar9xmj8aMNqZlb0GOqUBAhJqxA6bOntfOzY%2BGOpjGynIy9OkrRiXxDfRa4Q4rxVv0Y6ucB0QtjCkWij5Iz8%2FFNesw6l3qi0PFlEW7JH8Wb8BlHdJQTnmaUXlm9qjFWO%2Fwt8Ah5iRpgTuyAfA0BEZXkDujCdkmXw2qGr9TGoZFgvIlY3yplZ4A6AwmL9adB8mB%2BskW1CK2Uptdm%2BDT1BUB%2FrFmQxDo1KgOeqmxqT%2F4omKmwMe&X-Amz-Signature=acfc5af090217e097fecba5843c100ee69212f20056debcc1c8c5fb0de3cc35a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KCIH2H2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCID8c6ffcNIeM5P3qfsWdLP56lleZqYiME0sAJJ4dIqY1AiEA44uqNqxvEkUKT9qxRdGlrPVaRpQLjhPV%2BHv5x0Tuwq8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2Fx939LMP0buTBOQSrcA%2Bin1wvs38vClaBDsZ8eZtg7bC3URZcHQinCjXOCnOy%2Bp4nKImYtmuWhbIVishtHzUTtRauolwhv76Z%2FWeqsjDhWqQSLCEaYlyIrlxz2AExmH4R%2FFlgWm%2FPP65aAE4DgL%2Ftq1Atj565DVlohjHaLeWZfnc5vWRTKOgz2Rw%2Fhw9PK5DQw9Bi38k%2BCEFTRrVRRR%2FVDGaTCdT50J%2BK5ngc1joyIEurWUrA7%2Bap0GQin%2Bq1B%2FUU6VUriVnskm9LEW5L0%2BraVLv1kADHeXu4Dc3GlqnvPrrsqhK%2B5ibuzAlWlONcpqEgTNEI9GMAk991XHhOg%2F6G4eZl28JGVwWkW78ovVac7PRytdiFxs%2BDa79I837zBm3E%2BGYDs9jThh%2BCxY0TYQPP8MbT4%2FBYAb3trjZjMNbyFrlKda8likejZ%2BBVDW7ZciYcfaRvOuOogfjFYPffhzwlYCwk0i1t%2BjWOKOP%2F%2FsU3MxWK%2FWAxIjX5XLA9Ovu8czm7BuJDz6iNvCISVEEo%2BFDETI5FSQkOnCQZ0ka8MDo9%2BjXGKTrkpC9e%2Fc4Yo3qnRDGJHQtoxD5h9dmSaKFC56RQ9tGSNRKyWTOamYEgOXcRVjXe6me9yCcdnbnfsV5qRpTb%2Fqvp%2Bar9xmj8aMNqZlb0GOqUBAhJqxA6bOntfOzY%2BGOpjGynIy9OkrRiXxDfRa4Q4rxVv0Y6ucB0QtjCkWij5Iz8%2FFNesw6l3qi0PFlEW7JH8Wb8BlHdJQTnmaUXlm9qjFWO%2Fwt8Ah5iRpgTuyAfA0BEZXkDujCdkmXw2qGr9TGoZFgvIlY3yplZ4A6AwmL9adB8mB%2BskW1CK2Uptdm%2BDT1BUB%2FrFmQxDo1KgOeqmxqT%2F4omKmwMe&X-Amz-Signature=8a6dd3cf1cf08f6a4305caa3b5c411961944cfdffb84c4aa810740695011f95c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KCIH2H2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCID8c6ffcNIeM5P3qfsWdLP56lleZqYiME0sAJJ4dIqY1AiEA44uqNqxvEkUKT9qxRdGlrPVaRpQLjhPV%2BHv5x0Tuwq8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2Fx939LMP0buTBOQSrcA%2Bin1wvs38vClaBDsZ8eZtg7bC3URZcHQinCjXOCnOy%2Bp4nKImYtmuWhbIVishtHzUTtRauolwhv76Z%2FWeqsjDhWqQSLCEaYlyIrlxz2AExmH4R%2FFlgWm%2FPP65aAE4DgL%2Ftq1Atj565DVlohjHaLeWZfnc5vWRTKOgz2Rw%2Fhw9PK5DQw9Bi38k%2BCEFTRrVRRR%2FVDGaTCdT50J%2BK5ngc1joyIEurWUrA7%2Bap0GQin%2Bq1B%2FUU6VUriVnskm9LEW5L0%2BraVLv1kADHeXu4Dc3GlqnvPrrsqhK%2B5ibuzAlWlONcpqEgTNEI9GMAk991XHhOg%2F6G4eZl28JGVwWkW78ovVac7PRytdiFxs%2BDa79I837zBm3E%2BGYDs9jThh%2BCxY0TYQPP8MbT4%2FBYAb3trjZjMNbyFrlKda8likejZ%2BBVDW7ZciYcfaRvOuOogfjFYPffhzwlYCwk0i1t%2BjWOKOP%2F%2FsU3MxWK%2FWAxIjX5XLA9Ovu8czm7BuJDz6iNvCISVEEo%2BFDETI5FSQkOnCQZ0ka8MDo9%2BjXGKTrkpC9e%2Fc4Yo3qnRDGJHQtoxD5h9dmSaKFC56RQ9tGSNRKyWTOamYEgOXcRVjXe6me9yCcdnbnfsV5qRpTb%2Fqvp%2Bar9xmj8aMNqZlb0GOqUBAhJqxA6bOntfOzY%2BGOpjGynIy9OkrRiXxDfRa4Q4rxVv0Y6ucB0QtjCkWij5Iz8%2FFNesw6l3qi0PFlEW7JH8Wb8BlHdJQTnmaUXlm9qjFWO%2Fwt8Ah5iRpgTuyAfA0BEZXkDujCdkmXw2qGr9TGoZFgvIlY3yplZ4A6AwmL9adB8mB%2BskW1CK2Uptdm%2BDT1BUB%2FrFmQxDo1KgOeqmxqT%2F4omKmwMe&X-Amz-Signature=ddec9aaabed15b6540559c3b1a6aa9fbba77fed7d6b2196fd944a466d86f0ebb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ4HDPJD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBOsF3m%2B7Zy%2FLFzr73FvMBxuTGfEyh%2FUT5%2BhqsisDAzEAiEAt7fvcLKCetZDjjRn%2B5bjt2ngsxyhjAEWU2Rc2Hopg08q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDNunTX8NgcwErmQKiircA%2Bl37%2BIwmvt7H9O94vqbL7%2ByuaQFoHD6kyRJNhdMYobosAygF%2Fjkcyxm2fWTNPU7MxiwUZmqX6Nfro7Bm1n33ES09MaYv%2FAcB4MwMG2rGF9Y5D2q0OIWIH9G11BzjnkN6bNoPOnyNjQBGBQ9UFvYNUvbDHxp2LjOKfZ2qCInY5lSJg9RftiZTp%2FiH98%2FpSFbW7EBl4WnpimByIgKnZqVf%2FMRDC4k9Us8nGfspEKq03yccKqB9acOlmg73R8QQV0vnQR2Ea9sq0sPAAZoE1ZDsFE%2B3PmWo135L%2FPqVY040AXG0T%2BlkaqKjAMSuLhWw1Fl7OUG2Kuiy%2B%2BdfOnD1Vy7yMBqZehJa%2FBEp3%2FIqDxfBKxdj987Nz0NpXZqG1ocRO3n3PQkdwMKdAgnCVTNH8TxY5Rrfz%2FRGRqGxa%2FkgzGWY72qPAGu6Zsfl7J8LFAGUNLFPyouhg2QioLo%2FQpjOw%2FqkTuohL9LnA9bR6CyndrZImbSlImXA1RPvrHNf62c6RYyehB%2FqCSjX3DZLb90ZxlkJDeu%2B6cK3MjEW0aYwpBF%2FTxXUBquemcC%2FJSowgjt0hFiOAVNqNEPUZxfYT%2BM17TMYVlq00WMmve3DR5Rj4oirE9eMFJM1vfQ2HId7Ww2MLSalb0GOqUBijWKzYPOhH5mmbi4%2FlZ2k8BFjc1XXs1OLl9VfhRv5UogixtsC7Gz0Fni0uYVURSHMWYGu7aCKCEMrcyJU4NBBCfw8zd48NmJ8gNJX7ZFKH2auBylGGt2WUdq2brfQy0Ee7oFHPHLTNKnfIi5j2nRFOiQ121idXxSu8l3qTgC0ZFbxTyu9UEI9S5fpNNyNvpjR2m0NSDj5cF0OMpDBehgyv7shhVS&X-Amz-Signature=04a08bc7591d3df54b4280f5b9db5fb5800725a319e0eea7861a0b8def268b0f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5KCDS6J%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBpeVf8FkpbAekPFv0AagOTZZN5VnD0q67WPxOp%2FCXqgAiEAhyVYWN%2BZnKTpGUv1rChrRhPDqor6nKb1qXbcnBuMvyEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDC%2BNkQ5qbUIgMWzP6yrcA1%2BREOpDatw%2F2qXfmrQ4cLrSQo5AVKMH1vH8eElDGO6ofnK9yzkpzMg6o6rYZtGiK8AeTVd6xCUbBR%2BXLD4%2FSfchMt7HlkONoKzr%2F%2FhWgJEm1aNAQh6xaJgD0lc4pGITRGbeqhMyYtNs%2Blkii7yvmU%2BCevP56p3ET89X3lr2yym5HEA2o5JKxrOGLhn9YcSQnWUvUjx5V6nMuCna3Tpq6krxrBKvzQhfGWvbu%2FKCSBQIFG6Eka4pAf4BLFsjR%2F5ICWp9b%2F21%2BuhadhShKESnGETSZaTUX0fVIo1Zros%2FMIG7LXzjIJ%2F1coS9dTkDE96MSWAGJzafm0qaNk2TC%2F%2F1iptFZEgsHbwMBU%2Frn3CDRC7wZD2X9aL9ajBXa7eInwN%2FAK5BmY9sPXeMIy2K7Xq6PEkczCuP3LVh%2FcQ%2FKkRcIvNJljXtKYcXLfvHLL1kgHR05fdDCA4y%2BItfVaBqkCuzWcYXr1RghIjJ5tOUeHIMrttynVMnTR%2FKsAfNLLXqu3gvo9dddB%2FzfsDJgIQhFCA%2BCywA7gvnwInvnYY0gsgntbeleAjJogbFaq4u7CNfnH3%2BLlNnpc696xBbvQVGHaCjGcH2ymbwix79vocnGQccU57FUeRJaPiHFbdZeLA9MJOalb0GOqUB1rckTnYORceKNY76Rgd3Tx8t22kLiOjb37FGJJVGunhiYzuVuu38e7WESaYTGxooXrn%2FAv2X9W7K6NbSi%2BIZq3SD2NAqbypzJaadsjcXiKhbitqhtrG0ptty98wY933LRqpltl6CWYW01s%2FIxec4ijW3WSA6u%2BuMi7%2BE6MtcKmMqmnsRE3bPsg%2FGIWndQeDORCMDIE5CKZr36e3V1MyAEjVIKG6j&X-Amz-Signature=ac36ef550e4818d1abdd70d98f9fa711ccf9e6d87bc0a8bbb1d6e608caceae81&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PUP3FZB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHcslKZ9%2BpNd2dgWUnzB2AI%2BebStEc2zaUyq%2B7yGR%2Bf%2FAiEAhE9VllcDZBmh3MuOzzNtCfLooFak3f9fASSP6Xy0X08q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDHYzxY8gnbyajzs3NyrcA3xlYyS0pNBrkQUAgAWHf76Fv7MG%2B6S7QKAPiYw%2FIdAwYMgx4Dj1fRflOJY%2BICBIV2QkQ%2BGEMA933254PcH3EcE2OLUzWcl%2FjspUi25RaZVwUxEngcsrH97olL1vXieUN25n8NE%2Fp7jHJgiy%2FtrZ6cPEUIofhpLBw4sTD2w%2BABXI5FY%2F4zM89CCzEx5tzySIaqC7dRMs8L%2FolHbIuZdmXk5EFLTeYNghcum%2BM92brU1Ttg9ixA8ql7knC5gMLjkqyrVr1D4ZckmBogxAyMOxvKW3iAWZWI41tfvC7FI%2Fa6ruxx%2B2bk3QMES9cnVM28%2FUDRqu7Yc6rKKQwvCzRhS98r%2BddLp2un%2Bb%2F05KsI0keCJaLA3OKSgwQ2KhabBeZCDxfGFWECIWnufUmSdEruT6a3Pe3WjlsmCTG4h9SfPs3wPqcrl82bSb0zVO0SjU0PmHZYXXDTjtwv8TEYurChLD21nXG%2BUdnnmJo44v1731DuIdsQs5ee07XRIvG%2Brfbn8FM2FGboEf8zKjqQ5f2Wll8lc1WoruPsXebnpq3zoaw68LUE9BX48Vyz9BfNeO59Mz50n8mLu1gH9TbcDVEwvOww4AAhkGoYqYED3V1AfD4wCtapGFqdgp0S4gFx8lMMCalb0GOqUBYs80H3et3aXx1VvcZV7UN3PUtdO4%2Fhl9aPYI9E5P28qQGlrJ2e37iHz9HSHtSZardwKA3Pj33y26%2Bcp03Dg9%2BqxwCLIYNKv93Efqg%2BX8Ei3jZ%2FrHcPDGkO97SRek5jrlE%2FusSCyDUQveP1yGAjXIU%2FpcJKAoB8gE51ga2iKESw0vgkW6SEFyllyswWGieeUxMM7weiODJYFcVGPJLwTZn1mGdZMu&X-Amz-Signature=d686fad4d621631026c714f9c429234608031b9337b8610e29fe7de8b2ea0cf3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXKYSWND%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDSKjNyI%2BJfL1X5JaaR7GToRtkXBtjRv3ybTUYYtrqdewIgG7d4USYvrXV6awwtj1daSLy3xaLvNCFL6oknYnQVtTcq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDHfVN2zBUNqQLJoBvyrcA33kpSAXMc%2FUadrY%2FkT5uDwEb%2BrOxSSqXmtVsnVZqIAmcRCscQcSsA%2Fa29msbfQscMpE5UYkB9IXmJKyT9P1z6MLnU9aApvlnYcPvmCzzO5OnzSZTlkpUsc4LfY3cPh9CsFNn1jojWTRzChPL%2BfGhWrQkqxFOANDgKcktCANLBh4ROv7xI4wAnq%2BgN73HLH38VBRDcGqsiZC01LzF1bzN3ba3XRxyqg74PgVtN2czMZcIIHcxVvVyVntArGI12Z%2FfXIixgl5wZQNNB2%2FGe3SnhJe7ImzoT1KA1b%2BxHVo18CvSelKPc40pn0uAnMH7Ba2g7OXmrCEI3oaNQxvDtdi53L1JOg%2FF%2BXNwBQDyTjrh0xAmb0HkHxb0at2mmLwJF6DKh2XdsnLsjYlF6POO3T07wp4SHJ7%2FZ%2FWmQdWsTQvhWHxzLAiHajXKFjYG6f3%2BtpzA5JUw8Bf9mdgfHjSrkTeWxWFWRPVB%2Bf%2BpWpl5KGwO0sYpA0vPW03l0h5yVoa0rqFBnmbSjyxipBpXigUZs7fUY75UK41zDnkS8ETe78OzrIyQFpOz0fBUw2MmkkyhIhynfH2pClI%2F0XRgrKOEWBa3nYXZFDgiC65onAbKAoW64ZVDw6Q2PT4Nh6H8GqEMNmZlb0GOqUBqOb3V212kuwnGQTQagizuOWVvjWEVExDSq3Czc2mWZtJbLsqLSnXSnzFQTaMnx%2FeSnMyLgYP6MFRQLNciYJpPlJVea9lYtpI75iDOIiPm%2FPtVZrZ2YMWDI2L3o6YjuQn6nT290gq0luI2O%2F9GU5WIKNKmVGzhV5VecGFeb%2BfumzmkkJgx3fPR2%2FzI%2FbHP0ZtLCLNauokyndFE6Go8i5njXe8ugJJ&X-Amz-Signature=ac5e3796b81c070874b2cf1234676995b74bcd3a4d302768927291d8b7ab5dc4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXKYSWND%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDSKjNyI%2BJfL1X5JaaR7GToRtkXBtjRv3ybTUYYtrqdewIgG7d4USYvrXV6awwtj1daSLy3xaLvNCFL6oknYnQVtTcq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDHfVN2zBUNqQLJoBvyrcA33kpSAXMc%2FUadrY%2FkT5uDwEb%2BrOxSSqXmtVsnVZqIAmcRCscQcSsA%2Fa29msbfQscMpE5UYkB9IXmJKyT9P1z6MLnU9aApvlnYcPvmCzzO5OnzSZTlkpUsc4LfY3cPh9CsFNn1jojWTRzChPL%2BfGhWrQkqxFOANDgKcktCANLBh4ROv7xI4wAnq%2BgN73HLH38VBRDcGqsiZC01LzF1bzN3ba3XRxyqg74PgVtN2czMZcIIHcxVvVyVntArGI12Z%2FfXIixgl5wZQNNB2%2FGe3SnhJe7ImzoT1KA1b%2BxHVo18CvSelKPc40pn0uAnMH7Ba2g7OXmrCEI3oaNQxvDtdi53L1JOg%2FF%2BXNwBQDyTjrh0xAmb0HkHxb0at2mmLwJF6DKh2XdsnLsjYlF6POO3T07wp4SHJ7%2FZ%2FWmQdWsTQvhWHxzLAiHajXKFjYG6f3%2BtpzA5JUw8Bf9mdgfHjSrkTeWxWFWRPVB%2Bf%2BpWpl5KGwO0sYpA0vPW03l0h5yVoa0rqFBnmbSjyxipBpXigUZs7fUY75UK41zDnkS8ETe78OzrIyQFpOz0fBUw2MmkkyhIhynfH2pClI%2F0XRgrKOEWBa3nYXZFDgiC65onAbKAoW64ZVDw6Q2PT4Nh6H8GqEMNmZlb0GOqUBqOb3V212kuwnGQTQagizuOWVvjWEVExDSq3Czc2mWZtJbLsqLSnXSnzFQTaMnx%2FeSnMyLgYP6MFRQLNciYJpPlJVea9lYtpI75iDOIiPm%2FPtVZrZ2YMWDI2L3o6YjuQn6nT290gq0luI2O%2F9GU5WIKNKmVGzhV5VecGFeb%2BfumzmkkJgx3fPR2%2FzI%2FbHP0ZtLCLNauokyndFE6Go8i5njXe8ugJJ&X-Amz-Signature=197a56c0cf2e3ea641294616fc02ce29483907c788dd32b85e59705eff728d24&X-Amz-SignedHeaders=host&x-id=GetObject)

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
