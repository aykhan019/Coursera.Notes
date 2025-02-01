

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZITJPIT4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1hE1VuZg0VN7xPteSbUWl7n2G6sLqytON45geyJM14wIgVhsXLyUR12zTLuOGWPN8H3AFalqiJwzJ8kOUAfvjzqwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHj7mUuwze7BzyFLYyrcA9xpC1TXg1DqDu1%2Fxj%2FMNEkRsCyMQvQSUDDSsRaMK%2B9zCV4sqTTruU4jdgTdxlmElX3FsJVcEswRENr91SUF%2FBR6IK1ZAeGUeD0%2BjtQaurrPBIZ3EPM5um2n8pxLKWqdKMIdCo0WyYNw4Njh8A%2BOFK1UihbjWRoVGcGTFpXT9ezHGyPqe0T2I7MzoPg4iaxUTkipxL7eG5NAHvZvTZH2CkuEupZ0nY5AfvuFLDx203QrJ4YW2MH1oe3rKTHqxGAPfl%2F0ztuUOM3Hq6vWNPbknOX9U4c8z896kKY0DbsOD3p4Ek%2BocvKNeGVTZPWPzt4%2FjS1kSoOIK79%2BP9yUqVY2niAA0%2BWqlRSOOZcIItI8QdmnmUdNe%2Fv4eRIrVf8bbzf66vCVrfymLM7zGzjHQ3%2BSoVVwAUCK%2FfRpPV0OSP48J17AUYnBjDNbMhiYnvT7l2YDOSR5rWQqGsfAi3VPFfK%2FLp0TSGeiLnQHZaMmQzW2t%2BWqfeZ4M5rfYftCSDKv47hTSK5LI2xbbIjev1SOPD3Sq5i0WRcyvJF1NTKpAGCw9jarb7VdycGOm0AeTOS96dt9RmB06qnurjEBPP2Zw0Cl9ZakJd1CjZOjYjyJuMFQ3wQ6jy8DDnphXACXJOftMK3G%2BLwGOqUBtUnOLbYhkah8cNyc9BH35gmL%2FPQZ0qvbkZeZxF2a%2BIV5kvoQNB1XUL94mAPK5ORxGos3aBYEfU7rrNdMzzLEzkgpcdi0k7QjzzlX%2BKAPFTZ%2FW36IRS5CW%2BL%2FAVaufyl0IujeFMo2TgeMl%2BgBScBX54rw4S%2FWYdiITyFJx7hw7%2BxIaAeb0Wg0rUpvRKqZUtE83n7ElGoDqvJLm7q5s22Obm3%2F2UMH&X-Amz-Signature=4880c046c16b43799740f5791053f8bd8bf216146c696315c4eda30f35bca28a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZITJPIT4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1hE1VuZg0VN7xPteSbUWl7n2G6sLqytON45geyJM14wIgVhsXLyUR12zTLuOGWPN8H3AFalqiJwzJ8kOUAfvjzqwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHj7mUuwze7BzyFLYyrcA9xpC1TXg1DqDu1%2Fxj%2FMNEkRsCyMQvQSUDDSsRaMK%2B9zCV4sqTTruU4jdgTdxlmElX3FsJVcEswRENr91SUF%2FBR6IK1ZAeGUeD0%2BjtQaurrPBIZ3EPM5um2n8pxLKWqdKMIdCo0WyYNw4Njh8A%2BOFK1UihbjWRoVGcGTFpXT9ezHGyPqe0T2I7MzoPg4iaxUTkipxL7eG5NAHvZvTZH2CkuEupZ0nY5AfvuFLDx203QrJ4YW2MH1oe3rKTHqxGAPfl%2F0ztuUOM3Hq6vWNPbknOX9U4c8z896kKY0DbsOD3p4Ek%2BocvKNeGVTZPWPzt4%2FjS1kSoOIK79%2BP9yUqVY2niAA0%2BWqlRSOOZcIItI8QdmnmUdNe%2Fv4eRIrVf8bbzf66vCVrfymLM7zGzjHQ3%2BSoVVwAUCK%2FfRpPV0OSP48J17AUYnBjDNbMhiYnvT7l2YDOSR5rWQqGsfAi3VPFfK%2FLp0TSGeiLnQHZaMmQzW2t%2BWqfeZ4M5rfYftCSDKv47hTSK5LI2xbbIjev1SOPD3Sq5i0WRcyvJF1NTKpAGCw9jarb7VdycGOm0AeTOS96dt9RmB06qnurjEBPP2Zw0Cl9ZakJd1CjZOjYjyJuMFQ3wQ6jy8DDnphXACXJOftMK3G%2BLwGOqUBtUnOLbYhkah8cNyc9BH35gmL%2FPQZ0qvbkZeZxF2a%2BIV5kvoQNB1XUL94mAPK5ORxGos3aBYEfU7rrNdMzzLEzkgpcdi0k7QjzzlX%2BKAPFTZ%2FW36IRS5CW%2BL%2FAVaufyl0IujeFMo2TgeMl%2BgBScBX54rw4S%2FWYdiITyFJx7hw7%2BxIaAeb0Wg0rUpvRKqZUtE83n7ElGoDqvJLm7q5s22Obm3%2F2UMH&X-Amz-Signature=f7f29c5d4174db0a42b5a5d128cfd6a1c0cbde25eff97deaa877ff45a84cf6ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZITJPIT4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1hE1VuZg0VN7xPteSbUWl7n2G6sLqytON45geyJM14wIgVhsXLyUR12zTLuOGWPN8H3AFalqiJwzJ8kOUAfvjzqwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHj7mUuwze7BzyFLYyrcA9xpC1TXg1DqDu1%2Fxj%2FMNEkRsCyMQvQSUDDSsRaMK%2B9zCV4sqTTruU4jdgTdxlmElX3FsJVcEswRENr91SUF%2FBR6IK1ZAeGUeD0%2BjtQaurrPBIZ3EPM5um2n8pxLKWqdKMIdCo0WyYNw4Njh8A%2BOFK1UihbjWRoVGcGTFpXT9ezHGyPqe0T2I7MzoPg4iaxUTkipxL7eG5NAHvZvTZH2CkuEupZ0nY5AfvuFLDx203QrJ4YW2MH1oe3rKTHqxGAPfl%2F0ztuUOM3Hq6vWNPbknOX9U4c8z896kKY0DbsOD3p4Ek%2BocvKNeGVTZPWPzt4%2FjS1kSoOIK79%2BP9yUqVY2niAA0%2BWqlRSOOZcIItI8QdmnmUdNe%2Fv4eRIrVf8bbzf66vCVrfymLM7zGzjHQ3%2BSoVVwAUCK%2FfRpPV0OSP48J17AUYnBjDNbMhiYnvT7l2YDOSR5rWQqGsfAi3VPFfK%2FLp0TSGeiLnQHZaMmQzW2t%2BWqfeZ4M5rfYftCSDKv47hTSK5LI2xbbIjev1SOPD3Sq5i0WRcyvJF1NTKpAGCw9jarb7VdycGOm0AeTOS96dt9RmB06qnurjEBPP2Zw0Cl9ZakJd1CjZOjYjyJuMFQ3wQ6jy8DDnphXACXJOftMK3G%2BLwGOqUBtUnOLbYhkah8cNyc9BH35gmL%2FPQZ0qvbkZeZxF2a%2BIV5kvoQNB1XUL94mAPK5ORxGos3aBYEfU7rrNdMzzLEzkgpcdi0k7QjzzlX%2BKAPFTZ%2FW36IRS5CW%2BL%2FAVaufyl0IujeFMo2TgeMl%2BgBScBX54rw4S%2FWYdiITyFJx7hw7%2BxIaAeb0Wg0rUpvRKqZUtE83n7ElGoDqvJLm7q5s22Obm3%2F2UMH&X-Amz-Signature=7acd34866ffb5824a66e08c9f401ef2011554c34d499c72021579b8446016758&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB33XFL2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4PZmvWUQ%2B%2BLH0soiIMolUD3tjd42perEH%2B5YeoI7wsQIgYqWyT3LsKD9gvtMiKjXOloC7cjJEjV9pFX%2BNFQdOVT4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNb82hKYai8BYIRahCrcAw8GL0qUVn7CabTO9ARbLnoiev%2FSIR%2B88W9rNlwg%2FclWw6HNg5h%2BGmdnMUnFtRrdrqyKm8XzOxeJZq52m1Ape3O4dPQV3EkbXi1P%2F9%2FlhqTTEJ4KUKDS59HJ53o83npZKEqQUx%2FaPhqFnf1VWFLWoAXJ%2FyFC%2B4GqGB5roTQTNlLllYdAu%2FOfMtxWrPJpmI0lj1g9oRxtwAp%2BeYBSjqeHh%2FmWaCViwWyxlPVvzUed7ujRs2UcrVUGYDZwRx1IPM0bYc9WFFvul6kf6Wzn%2FKM7sB%2B1yQFkhRYDwel5XB3bjDOXxER6osiQSaMEyNPTdJDdCkmGQWexcN0oURp%2BAxgvdYJWThbHbUMg7tgcMGheeK7i7iaChiQsFIfCxs6svrHrkpVQcZcjVxyYUDuOoXjSWZ1CqPugXh55kfDOCvAts%2FwvI%2BLMW68KZ9gCVtBpGKc7BExYiY%2FHhsz%2BkzXt%2Fpfll7KEptTZ1N8fuo2vuUM4ZZx%2FN7vD5nAPU0SQbUKzwnIxqPBSPHDBL8%2FLfcDbEERArwwV7UuxP5I7K%2FtQP36%2FFqIGWZpAYZMD6vrnpyMEXffDD%2FNs0sVKpdBhSUhGjMITRxOzJcjbK7ckYGy6vxfNZT4k2ilWtfnKPf8Ebm0eMMnB%2BLwGOqUB2lFMSMdqyNjfCAsmtC%2FOFilPhVa8T6QkJvmw%2FebLl%2Bf%2FEfr5d7EZK9C%2F41GNd2Eac%2FqgBKkkuq5N7RXRFySutv9RK2txuIwONuVN23XqPyjvOdhw4ySyLB2bzF9wavGGn4EYteob6B%2FtimeIu2O%2B8%2FWWzvJ2H%2FyQu3VocfkodVNuEwl5wwb5tn2DHWZ3ijXGUEwRmOCmz9WMlxS9ISCxQ01GthpR&X-Amz-Signature=db124fcf9f897a24fd5dce8baa2b43e2bcd6bebff62d774b5f0edead4ca88a45&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB33XFL2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4PZmvWUQ%2B%2BLH0soiIMolUD3tjd42perEH%2B5YeoI7wsQIgYqWyT3LsKD9gvtMiKjXOloC7cjJEjV9pFX%2BNFQdOVT4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNb82hKYai8BYIRahCrcAw8GL0qUVn7CabTO9ARbLnoiev%2FSIR%2B88W9rNlwg%2FclWw6HNg5h%2BGmdnMUnFtRrdrqyKm8XzOxeJZq52m1Ape3O4dPQV3EkbXi1P%2F9%2FlhqTTEJ4KUKDS59HJ53o83npZKEqQUx%2FaPhqFnf1VWFLWoAXJ%2FyFC%2B4GqGB5roTQTNlLllYdAu%2FOfMtxWrPJpmI0lj1g9oRxtwAp%2BeYBSjqeHh%2FmWaCViwWyxlPVvzUed7ujRs2UcrVUGYDZwRx1IPM0bYc9WFFvul6kf6Wzn%2FKM7sB%2B1yQFkhRYDwel5XB3bjDOXxER6osiQSaMEyNPTdJDdCkmGQWexcN0oURp%2BAxgvdYJWThbHbUMg7tgcMGheeK7i7iaChiQsFIfCxs6svrHrkpVQcZcjVxyYUDuOoXjSWZ1CqPugXh55kfDOCvAts%2FwvI%2BLMW68KZ9gCVtBpGKc7BExYiY%2FHhsz%2BkzXt%2Fpfll7KEptTZ1N8fuo2vuUM4ZZx%2FN7vD5nAPU0SQbUKzwnIxqPBSPHDBL8%2FLfcDbEERArwwV7UuxP5I7K%2FtQP36%2FFqIGWZpAYZMD6vrnpyMEXffDD%2FNs0sVKpdBhSUhGjMITRxOzJcjbK7ckYGy6vxfNZT4k2ilWtfnKPf8Ebm0eMMnB%2BLwGOqUB2lFMSMdqyNjfCAsmtC%2FOFilPhVa8T6QkJvmw%2FebLl%2Bf%2FEfr5d7EZK9C%2F41GNd2Eac%2FqgBKkkuq5N7RXRFySutv9RK2txuIwONuVN23XqPyjvOdhw4ySyLB2bzF9wavGGn4EYteob6B%2FtimeIu2O%2B8%2FWWzvJ2H%2FyQu3VocfkodVNuEwl5wwb5tn2DHWZ3ijXGUEwRmOCmz9WMlxS9ISCxQ01GthpR&X-Amz-Signature=524dd66b07da50f625310c47d371bb36aef85aab56b23600e69b37296cd10377&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB33XFL2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4PZmvWUQ%2B%2BLH0soiIMolUD3tjd42perEH%2B5YeoI7wsQIgYqWyT3LsKD9gvtMiKjXOloC7cjJEjV9pFX%2BNFQdOVT4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNb82hKYai8BYIRahCrcAw8GL0qUVn7CabTO9ARbLnoiev%2FSIR%2B88W9rNlwg%2FclWw6HNg5h%2BGmdnMUnFtRrdrqyKm8XzOxeJZq52m1Ape3O4dPQV3EkbXi1P%2F9%2FlhqTTEJ4KUKDS59HJ53o83npZKEqQUx%2FaPhqFnf1VWFLWoAXJ%2FyFC%2B4GqGB5roTQTNlLllYdAu%2FOfMtxWrPJpmI0lj1g9oRxtwAp%2BeYBSjqeHh%2FmWaCViwWyxlPVvzUed7ujRs2UcrVUGYDZwRx1IPM0bYc9WFFvul6kf6Wzn%2FKM7sB%2B1yQFkhRYDwel5XB3bjDOXxER6osiQSaMEyNPTdJDdCkmGQWexcN0oURp%2BAxgvdYJWThbHbUMg7tgcMGheeK7i7iaChiQsFIfCxs6svrHrkpVQcZcjVxyYUDuOoXjSWZ1CqPugXh55kfDOCvAts%2FwvI%2BLMW68KZ9gCVtBpGKc7BExYiY%2FHhsz%2BkzXt%2Fpfll7KEptTZ1N8fuo2vuUM4ZZx%2FN7vD5nAPU0SQbUKzwnIxqPBSPHDBL8%2FLfcDbEERArwwV7UuxP5I7K%2FtQP36%2FFqIGWZpAYZMD6vrnpyMEXffDD%2FNs0sVKpdBhSUhGjMITRxOzJcjbK7ckYGy6vxfNZT4k2ilWtfnKPf8Ebm0eMMnB%2BLwGOqUB2lFMSMdqyNjfCAsmtC%2FOFilPhVa8T6QkJvmw%2FebLl%2Bf%2FEfr5d7EZK9C%2F41GNd2Eac%2FqgBKkkuq5N7RXRFySutv9RK2txuIwONuVN23XqPyjvOdhw4ySyLB2bzF9wavGGn4EYteob6B%2FtimeIu2O%2B8%2FWWzvJ2H%2FyQu3VocfkodVNuEwl5wwb5tn2DHWZ3ijXGUEwRmOCmz9WMlxS9ISCxQ01GthpR&X-Amz-Signature=937a21c1bdfda4df8cc3e9ba7f841bf88f8edbe60705ea8e4bc88596a5e5ec79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB33XFL2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4PZmvWUQ%2B%2BLH0soiIMolUD3tjd42perEH%2B5YeoI7wsQIgYqWyT3LsKD9gvtMiKjXOloC7cjJEjV9pFX%2BNFQdOVT4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNb82hKYai8BYIRahCrcAw8GL0qUVn7CabTO9ARbLnoiev%2FSIR%2B88W9rNlwg%2FclWw6HNg5h%2BGmdnMUnFtRrdrqyKm8XzOxeJZq52m1Ape3O4dPQV3EkbXi1P%2F9%2FlhqTTEJ4KUKDS59HJ53o83npZKEqQUx%2FaPhqFnf1VWFLWoAXJ%2FyFC%2B4GqGB5roTQTNlLllYdAu%2FOfMtxWrPJpmI0lj1g9oRxtwAp%2BeYBSjqeHh%2FmWaCViwWyxlPVvzUed7ujRs2UcrVUGYDZwRx1IPM0bYc9WFFvul6kf6Wzn%2FKM7sB%2B1yQFkhRYDwel5XB3bjDOXxER6osiQSaMEyNPTdJDdCkmGQWexcN0oURp%2BAxgvdYJWThbHbUMg7tgcMGheeK7i7iaChiQsFIfCxs6svrHrkpVQcZcjVxyYUDuOoXjSWZ1CqPugXh55kfDOCvAts%2FwvI%2BLMW68KZ9gCVtBpGKc7BExYiY%2FHhsz%2BkzXt%2Fpfll7KEptTZ1N8fuo2vuUM4ZZx%2FN7vD5nAPU0SQbUKzwnIxqPBSPHDBL8%2FLfcDbEERArwwV7UuxP5I7K%2FtQP36%2FFqIGWZpAYZMD6vrnpyMEXffDD%2FNs0sVKpdBhSUhGjMITRxOzJcjbK7ckYGy6vxfNZT4k2ilWtfnKPf8Ebm0eMMnB%2BLwGOqUB2lFMSMdqyNjfCAsmtC%2FOFilPhVa8T6QkJvmw%2FebLl%2Bf%2FEfr5d7EZK9C%2F41GNd2Eac%2FqgBKkkuq5N7RXRFySutv9RK2txuIwONuVN23XqPyjvOdhw4ySyLB2bzF9wavGGn4EYteob6B%2FtimeIu2O%2B8%2FWWzvJ2H%2FyQu3VocfkodVNuEwl5wwb5tn2DHWZ3ijXGUEwRmOCmz9WMlxS9ISCxQ01GthpR&X-Amz-Signature=969ab7026000b7e124a0d39bfd2fbc2e11b4f920cf9deef23f33f86296941440&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB33XFL2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4PZmvWUQ%2B%2BLH0soiIMolUD3tjd42perEH%2B5YeoI7wsQIgYqWyT3LsKD9gvtMiKjXOloC7cjJEjV9pFX%2BNFQdOVT4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNb82hKYai8BYIRahCrcAw8GL0qUVn7CabTO9ARbLnoiev%2FSIR%2B88W9rNlwg%2FclWw6HNg5h%2BGmdnMUnFtRrdrqyKm8XzOxeJZq52m1Ape3O4dPQV3EkbXi1P%2F9%2FlhqTTEJ4KUKDS59HJ53o83npZKEqQUx%2FaPhqFnf1VWFLWoAXJ%2FyFC%2B4GqGB5roTQTNlLllYdAu%2FOfMtxWrPJpmI0lj1g9oRxtwAp%2BeYBSjqeHh%2FmWaCViwWyxlPVvzUed7ujRs2UcrVUGYDZwRx1IPM0bYc9WFFvul6kf6Wzn%2FKM7sB%2B1yQFkhRYDwel5XB3bjDOXxER6osiQSaMEyNPTdJDdCkmGQWexcN0oURp%2BAxgvdYJWThbHbUMg7tgcMGheeK7i7iaChiQsFIfCxs6svrHrkpVQcZcjVxyYUDuOoXjSWZ1CqPugXh55kfDOCvAts%2FwvI%2BLMW68KZ9gCVtBpGKc7BExYiY%2FHhsz%2BkzXt%2Fpfll7KEptTZ1N8fuo2vuUM4ZZx%2FN7vD5nAPU0SQbUKzwnIxqPBSPHDBL8%2FLfcDbEERArwwV7UuxP5I7K%2FtQP36%2FFqIGWZpAYZMD6vrnpyMEXffDD%2FNs0sVKpdBhSUhGjMITRxOzJcjbK7ckYGy6vxfNZT4k2ilWtfnKPf8Ebm0eMMnB%2BLwGOqUB2lFMSMdqyNjfCAsmtC%2FOFilPhVa8T6QkJvmw%2FebLl%2Bf%2FEfr5d7EZK9C%2F41GNd2Eac%2FqgBKkkuq5N7RXRFySutv9RK2txuIwONuVN23XqPyjvOdhw4ySyLB2bzF9wavGGn4EYteob6B%2FtimeIu2O%2B8%2FWWzvJ2H%2FyQu3VocfkodVNuEwl5wwb5tn2DHWZ3ijXGUEwRmOCmz9WMlxS9ISCxQ01GthpR&X-Amz-Signature=6d58e809d6794792202a7eec5784eb2c10bbe05bc48695c68e5532aace7ffb6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB33XFL2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4PZmvWUQ%2B%2BLH0soiIMolUD3tjd42perEH%2B5YeoI7wsQIgYqWyT3LsKD9gvtMiKjXOloC7cjJEjV9pFX%2BNFQdOVT4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNb82hKYai8BYIRahCrcAw8GL0qUVn7CabTO9ARbLnoiev%2FSIR%2B88W9rNlwg%2FclWw6HNg5h%2BGmdnMUnFtRrdrqyKm8XzOxeJZq52m1Ape3O4dPQV3EkbXi1P%2F9%2FlhqTTEJ4KUKDS59HJ53o83npZKEqQUx%2FaPhqFnf1VWFLWoAXJ%2FyFC%2B4GqGB5roTQTNlLllYdAu%2FOfMtxWrPJpmI0lj1g9oRxtwAp%2BeYBSjqeHh%2FmWaCViwWyxlPVvzUed7ujRs2UcrVUGYDZwRx1IPM0bYc9WFFvul6kf6Wzn%2FKM7sB%2B1yQFkhRYDwel5XB3bjDOXxER6osiQSaMEyNPTdJDdCkmGQWexcN0oURp%2BAxgvdYJWThbHbUMg7tgcMGheeK7i7iaChiQsFIfCxs6svrHrkpVQcZcjVxyYUDuOoXjSWZ1CqPugXh55kfDOCvAts%2FwvI%2BLMW68KZ9gCVtBpGKc7BExYiY%2FHhsz%2BkzXt%2Fpfll7KEptTZ1N8fuo2vuUM4ZZx%2FN7vD5nAPU0SQbUKzwnIxqPBSPHDBL8%2FLfcDbEERArwwV7UuxP5I7K%2FtQP36%2FFqIGWZpAYZMD6vrnpyMEXffDD%2FNs0sVKpdBhSUhGjMITRxOzJcjbK7ckYGy6vxfNZT4k2ilWtfnKPf8Ebm0eMMnB%2BLwGOqUB2lFMSMdqyNjfCAsmtC%2FOFilPhVa8T6QkJvmw%2FebLl%2Bf%2FEfr5d7EZK9C%2F41GNd2Eac%2FqgBKkkuq5N7RXRFySutv9RK2txuIwONuVN23XqPyjvOdhw4ySyLB2bzF9wavGGn4EYteob6B%2FtimeIu2O%2B8%2FWWzvJ2H%2FyQu3VocfkodVNuEwl5wwb5tn2DHWZ3ijXGUEwRmOCmz9WMlxS9ISCxQ01GthpR&X-Amz-Signature=a98c14ca4e246ba93517dff703b2a68d11ec075d29ea3dd235432a331fc09a67&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPB7U5LG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHzMtmOgFoVp73HtEXaaYLZpQpOFwBSctgpLBvMR9vhgCIFuE53UDkHBiTdf8ugKVafVUVJ8KRl%2F88LI3Jq2TAltEKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydZPhpfO7kUYeSuU0q3APeg3LIsWIiEI2tqMr5TAULbevh2QDDK96nApnBmfJseJWluRKmg%2BjiACuizKxk7kRE4VlPQ7WO6MRHM9xIhE6kN757ET5IyvcEd9LmJS9L6fWjN%2BNuq58gizke5G%2BxoAo78iDzJ1bmH0UyAOeP5U4ZWsDfdXYaAe5sQd5QBHijkZrhAOXyPCrKX7uoGpQ0KIneK3wpMonAr7mYoTb6UMUmWQ0krKoTE0Fl%2FASosE4fC5JmLB7dzhtQhhAYX%2F6XAraHmIuYfRxiktIwgFLsE2aSLb5IJ0FGkcusk1ErCXq01Wc2f1cVONiqyBrRIvxcQkkbFH9jByYmFAvA3aDHkaD9BTzwtc7Ggxhr26tcNbTD0TAQlZJixCaBnj4w%2FOgOpEED2j6IdJYjWqS3pgyv6JYnXkRqwCeXtsskmyHlFIHC1h6JV5xFsZu0H%2FdYnjuKBtcRPDjmohxeFOcN7cjWN23UjxSYE7KU6RAHuMh3FOwBYvEbiIZhJxy3fLXOZK6nAJCIb%2FXomwzgx9Q0OZaXB2hqhT2nUb90g%2FbvvknMPvdcuCJkkUUpYmRdzpgIcNGdBszvNIrG0AhGKXcfn9ht4Lc5e9QlwFl06eJot695ZQUv1fuf1eklSVm0Q3eRpTDaq%2Fi8BjqnASAhztZWiCIYhVslyM6iPy4vdADCvFh3heLUvjFGJDeF7%2B0SdnQHbiYXDVjocoYs%2FExHNKBwifpDGIsNSskWwjmft8KLoFpg2ySKIlvNz5GrzyRcfwtVLF6biAqukpaOtr4LBOiJQT9M2yB6z%2Fp4X2sKGM0engKsXhVBRmZAwaU%2FtUkwXhgP3OeIw2SlxC0MERKMGnbusupqMSx5%2FUnahwa5LEASFON0&X-Amz-Signature=0793d01ac939468eacc19a939a64de5a8606435923a8e66d9f8b4cf218af6cd9&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K7Y5Q7R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDTzQWUgValSj%2FiPrvaC6OxKUUZ%2Ftpo5VmKTQ013CiZMAiBGIxaHxqqPKK4D%2BsSj5BZCR1KBmhKMtvE0ql2Bfn2o%2BSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5HuYJGSER7jD9ev7KtwDfiFMhvG6V5f2KK9p74ursZTOUK7sSNxXqaoCOK%2BsQtf%2B5XoABM7%2Fn%2BV1wNZGpTK5TzL1GYy1PhoTv7RtlNugfEjgDiBuifV76HGkWRrqUCi51N66eWr05qUurV%2FZrMQ22%2FXkdPgPNUBmLoDErP2p0cJ1vXEAjNu5caLHPwKg%2FUNCiBaMUbv2NQ1D3S4gP9ffUx%2FGo1FaYsBWBVDuMjLo15YKQ%2F1qvjSt9XhJ6WdU%2FxTqvT%2BT8SelckxqK%2Bh%2BjbBUMyzibTvnDfMm6TYM63Vf%2FMXzs5HiQxl4XJ0g1jGTA74h2I15ZLJ%2FqO92%2BOS0ITfEcyisl6GQ%2FcS8h967h7yGLDihb%2Fg%2F34xImsVDzImTOwg1RbWsLQkV%2BWikAbrg%2BGdtej9yzAC%2BGknFoPs8dXozBcWNxZpm8gyhhV8vpAByLfhou0lTWI303Kq0%2FN1LH4fKiOyTh%2F9nURKMiH0MuJ47piBRKDpz96yQrKleMiXt1EBnyROTUTv084unpYQVg7aulXbAx1gILS4peErXwcaaKBg2H2nzlOLZPmDCeO0APNluP7V40yityEd6yflYaW7rE4OIuBpDX18XCgNHD8lYe%2B1lYDa5aGjRdMRtFihtdXnqMuO33HmZZCoXyYIwjsj4vAY6pgHCleOGyJGbangcfzNLR43rM%2BmnXX%2FvS2FzLf4v813MAr08Kz4YiFdEJbeY9UFYkduy2JakmRwVdBk3qlxnH%2BGKO9ozAemcLrRlBDg%2FeevmGkyj81aJSYh%2BYv6lNbJBvyzm8Of2BNfk8n7aMTB%2FOIOkSb6JN1QcUaPqJt4X0za3YRrHPBULq0y7oeLx%2BAAiK2p9UjwvzKvmZvmQCHaCbnW1jhe9QSSm&X-Amz-Signature=8456314d0db07b018f7629c0114fa7b025d2eebec96ef04677d5f9c5e678103a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB33XFL2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4PZmvWUQ%2B%2BLH0soiIMolUD3tjd42perEH%2B5YeoI7wsQIgYqWyT3LsKD9gvtMiKjXOloC7cjJEjV9pFX%2BNFQdOVT4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNb82hKYai8BYIRahCrcAw8GL0qUVn7CabTO9ARbLnoiev%2FSIR%2B88W9rNlwg%2FclWw6HNg5h%2BGmdnMUnFtRrdrqyKm8XzOxeJZq52m1Ape3O4dPQV3EkbXi1P%2F9%2FlhqTTEJ4KUKDS59HJ53o83npZKEqQUx%2FaPhqFnf1VWFLWoAXJ%2FyFC%2B4GqGB5roTQTNlLllYdAu%2FOfMtxWrPJpmI0lj1g9oRxtwAp%2BeYBSjqeHh%2FmWaCViwWyxlPVvzUed7ujRs2UcrVUGYDZwRx1IPM0bYc9WFFvul6kf6Wzn%2FKM7sB%2B1yQFkhRYDwel5XB3bjDOXxER6osiQSaMEyNPTdJDdCkmGQWexcN0oURp%2BAxgvdYJWThbHbUMg7tgcMGheeK7i7iaChiQsFIfCxs6svrHrkpVQcZcjVxyYUDuOoXjSWZ1CqPugXh55kfDOCvAts%2FwvI%2BLMW68KZ9gCVtBpGKc7BExYiY%2FHhsz%2BkzXt%2Fpfll7KEptTZ1N8fuo2vuUM4ZZx%2FN7vD5nAPU0SQbUKzwnIxqPBSPHDBL8%2FLfcDbEERArwwV7UuxP5I7K%2FtQP36%2FFqIGWZpAYZMD6vrnpyMEXffDD%2FNs0sVKpdBhSUhGjMITRxOzJcjbK7ckYGy6vxfNZT4k2ilWtfnKPf8Ebm0eMMnB%2BLwGOqUB2lFMSMdqyNjfCAsmtC%2FOFilPhVa8T6QkJvmw%2FebLl%2Bf%2FEfr5d7EZK9C%2F41GNd2Eac%2FqgBKkkuq5N7RXRFySutv9RK2txuIwONuVN23XqPyjvOdhw4ySyLB2bzF9wavGGn4EYteob6B%2FtimeIu2O%2B8%2FWWzvJ2H%2FyQu3VocfkodVNuEwl5wwb5tn2DHWZ3ijXGUEwRmOCmz9WMlxS9ISCxQ01GthpR&X-Amz-Signature=c9a5cfe40fa92258aa79e562b10e41f7b2318ad9e0df0662920332e95544c966&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB33XFL2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4PZmvWUQ%2B%2BLH0soiIMolUD3tjd42perEH%2B5YeoI7wsQIgYqWyT3LsKD9gvtMiKjXOloC7cjJEjV9pFX%2BNFQdOVT4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNb82hKYai8BYIRahCrcAw8GL0qUVn7CabTO9ARbLnoiev%2FSIR%2B88W9rNlwg%2FclWw6HNg5h%2BGmdnMUnFtRrdrqyKm8XzOxeJZq52m1Ape3O4dPQV3EkbXi1P%2F9%2FlhqTTEJ4KUKDS59HJ53o83npZKEqQUx%2FaPhqFnf1VWFLWoAXJ%2FyFC%2B4GqGB5roTQTNlLllYdAu%2FOfMtxWrPJpmI0lj1g9oRxtwAp%2BeYBSjqeHh%2FmWaCViwWyxlPVvzUed7ujRs2UcrVUGYDZwRx1IPM0bYc9WFFvul6kf6Wzn%2FKM7sB%2B1yQFkhRYDwel5XB3bjDOXxER6osiQSaMEyNPTdJDdCkmGQWexcN0oURp%2BAxgvdYJWThbHbUMg7tgcMGheeK7i7iaChiQsFIfCxs6svrHrkpVQcZcjVxyYUDuOoXjSWZ1CqPugXh55kfDOCvAts%2FwvI%2BLMW68KZ9gCVtBpGKc7BExYiY%2FHhsz%2BkzXt%2Fpfll7KEptTZ1N8fuo2vuUM4ZZx%2FN7vD5nAPU0SQbUKzwnIxqPBSPHDBL8%2FLfcDbEERArwwV7UuxP5I7K%2FtQP36%2FFqIGWZpAYZMD6vrnpyMEXffDD%2FNs0sVKpdBhSUhGjMITRxOzJcjbK7ckYGy6vxfNZT4k2ilWtfnKPf8Ebm0eMMnB%2BLwGOqUB2lFMSMdqyNjfCAsmtC%2FOFilPhVa8T6QkJvmw%2FebLl%2Bf%2FEfr5d7EZK9C%2F41GNd2Eac%2FqgBKkkuq5N7RXRFySutv9RK2txuIwONuVN23XqPyjvOdhw4ySyLB2bzF9wavGGn4EYteob6B%2FtimeIu2O%2B8%2FWWzvJ2H%2FyQu3VocfkodVNuEwl5wwb5tn2DHWZ3ijXGUEwRmOCmz9WMlxS9ISCxQ01GthpR&X-Amz-Signature=d8e4749858883c384b8debc5ef9401d912693f963631a701ff277b49a2fa2f89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB33XFL2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4PZmvWUQ%2B%2BLH0soiIMolUD3tjd42perEH%2B5YeoI7wsQIgYqWyT3LsKD9gvtMiKjXOloC7cjJEjV9pFX%2BNFQdOVT4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNb82hKYai8BYIRahCrcAw8GL0qUVn7CabTO9ARbLnoiev%2FSIR%2B88W9rNlwg%2FclWw6HNg5h%2BGmdnMUnFtRrdrqyKm8XzOxeJZq52m1Ape3O4dPQV3EkbXi1P%2F9%2FlhqTTEJ4KUKDS59HJ53o83npZKEqQUx%2FaPhqFnf1VWFLWoAXJ%2FyFC%2B4GqGB5roTQTNlLllYdAu%2FOfMtxWrPJpmI0lj1g9oRxtwAp%2BeYBSjqeHh%2FmWaCViwWyxlPVvzUed7ujRs2UcrVUGYDZwRx1IPM0bYc9WFFvul6kf6Wzn%2FKM7sB%2B1yQFkhRYDwel5XB3bjDOXxER6osiQSaMEyNPTdJDdCkmGQWexcN0oURp%2BAxgvdYJWThbHbUMg7tgcMGheeK7i7iaChiQsFIfCxs6svrHrkpVQcZcjVxyYUDuOoXjSWZ1CqPugXh55kfDOCvAts%2FwvI%2BLMW68KZ9gCVtBpGKc7BExYiY%2FHhsz%2BkzXt%2Fpfll7KEptTZ1N8fuo2vuUM4ZZx%2FN7vD5nAPU0SQbUKzwnIxqPBSPHDBL8%2FLfcDbEERArwwV7UuxP5I7K%2FtQP36%2FFqIGWZpAYZMD6vrnpyMEXffDD%2FNs0sVKpdBhSUhGjMITRxOzJcjbK7ckYGy6vxfNZT4k2ilWtfnKPf8Ebm0eMMnB%2BLwGOqUB2lFMSMdqyNjfCAsmtC%2FOFilPhVa8T6QkJvmw%2FebLl%2Bf%2FEfr5d7EZK9C%2F41GNd2Eac%2FqgBKkkuq5N7RXRFySutv9RK2txuIwONuVN23XqPyjvOdhw4ySyLB2bzF9wavGGn4EYteob6B%2FtimeIu2O%2B8%2FWWzvJ2H%2FyQu3VocfkodVNuEwl5wwb5tn2DHWZ3ijXGUEwRmOCmz9WMlxS9ISCxQ01GthpR&X-Amz-Signature=77fa6b7f273d0f50d954daf5bc63eccb4dad86611dc337c62f01cf92b97f5c9c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663L7O4US4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfJkxBJH7TtA4kJ2Kz%2Fa2br%2Fbon1WajG1wv17kSnPZCgIhAOfezBn3Li5zpC%2BZjchb0X%2FqOhTUY4xbSzaydU%2BsxQs6KogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FQgFsPLH%2F%2Fxtd4WUq3APZa91gN2vIxZkaYZnMUq21uPolykJMniC074e8zwFOqevfxJmAZd7ifRV%2BP3WuOm1fpg5aHmyNWTq%2BBFwvTPpEgDnlXn%2FpyVsQpJQ3hVD%2BvQVacSuwKrNt0fmpqKSEw3%2FFG1Xe6lRrGyrKS964PNQvkArd6afVcaRkASUBQ4vMLARVSvT%2BvJ3d8v2XQhXbiVCXf8UbeYWElpMCr0FPZeNSdvRuCyhEjAOOTFZdy9O4NJ7lUaZDzzvzmdTlYLsMhaCTpAgq191NEGd08DYxKbyXgvGmyVn1MX0cSo6LdhevcbbjRHh4UVVBVWrM8YOAj7j6CoXc5ZPqz4vbIbBXhwr9dRzSIN3atLLq5d%2B2crv3GprI2EYznxKJDjZej5WdPC804dcKIxbXtV0ojVhsitUJ3gXuAfofwy2Eya8MvvDS8YesyH8%2BqGjTdEPuYl9FVSDd6Q1csB8DjQfrvpOHIwZEoaF0Iv%2BvsAXPj3gbarRyOSPz7BGAWgGWjnmRkYB5Y%2BVWH2NielX0NNIb0gqQ19gq1pGFqnZuXyjTLLGiGM5YOdrPelfhm4qNKU0QUz7CrSUZOiwmMuysfLjTXHmyki42Vscsmc0U%2BsXhpzI2KDkeB%2FGVFwNWZw43u8S92zDzwvi8BjqkAer6S11LdcfGRhYomeyH56ui69BxvdzmsaJmx0FrCXufZ99bkjDSj8M5nzWFX6I82iD9D8IC%2B8RDzkdwT19E71ZBjMwD1IPGa%2F2oRblB8A8mhSGBw3%2BjgYDOtjB%2Bcca3Z%2FzBM%2Fp6JJJKCk7%2FLt%2FeECClhkpfoorC4t%2BG5jXLBM8%2FT5msIsyXTtIocKl88dcmf9YK3GEqBRusBCbqfe1Y95EhC2J2&X-Amz-Signature=207f4a76ae829b21b4cba7d32188f03ad06308d6834b7d14d437f7835cd495bc&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZ6M3727%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTfPbb%2FjKtBHunPgTAxnlpOgrGio0bP4t%2B9xtBoPU%2FpAIhAJ5v%2BfomGgjyJZ6SbwA4ciicJq6gvkt2nBIxo5luZheZKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZRWj9Fu644uSPKQoq3ANXAlcVm%2BoJnrGQw1hsA3oPt%2BIc8wNYQJb8yNBarRp5fcFT%2FHCf%2B%2Flc1TKDyJTZFi705k88wMKPlhtMAan%2BaP6CWiixX%2BmYlLK9uLHT39McsTT3Pjepi%2FC5jZnFR%2BQ2ukC3GzcnfE0%2Fl0Wlgl9F35S2NdozI9yxF12vZMbeaUmgCJjjVbPTgycO3RXIwBZsGk160SykG3dm5t41XE4UenIA63RWZpZy0VGk0Xig0eBYc1rhjseoBlN2Eo3mEh5BBVMEZvqUfkXDN%2FrHEN4R%2B5dWieGqNhuHbwok1MlY%2BhRWnceMMju9cOjqZtAk3Mf6hkubHBXNKj%2Fd9HdlfrhnR62dyBaCZOIn%2FSvzrnJ%2BewX8QJfG8Psl7CKK8Q2zwnqF6z0r3GXBWb6MZ7XJZkGtx0%2BAwY%2FjJ2z8EV38caF%2B2IZ1KJd1OMVdrS0P2jYbVQ3QTwIZhHGc5SQ%2FmyMxR2VsESuRxnGzJhuhxQTnkY1XxOQFBNnBkt6GHgzu1QhejsaP5mLH%2FlRpowsZ73MLCgsq05rZUyZUpyb8iFzUbdgJZb6fdbo%2BPHWW4a38e900op0nDzygRx9gGyPA8ynRPBO%2Fnl%2Bxor9r66njrVq1C%2FHsAxI9JoUXWjyf8S9C0laCRDDoyvi8BjqkAUGHzLOjQkD7Xr%2BfLVdN%2BOF128UERl0wWkLPv9QXmmgGjyFUz%2FHxKdc1XRo0KkxJkbR2vXkMSWxG%2F17bVQb73MrnWFFomqlOLFeiE%2Fm82TiXBCjoIf%2B1EAXGn53Nt%2BCu3vnilyQlPx7Qqn5b6X4LPVHI6oDtL%2F0xvQxyWtNJ3vQ%2BjIrlTHxiDlPMLLiJELmqwTtKASruUj5FO9Dn3tnodhcEHM1e&X-Amz-Signature=61ffcfa3b33238dcd091a46932ea4eed26182ef486af46f4697e95feee9bd0ab&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633TYUWUR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCaZcuiB3C1dG2lyiYf8smpjJj2bzVbttDA1afN1vqFWwIhAP9qIIyBGBMLonYhvoUdckGI%2BPzW723t2tIIIboFntNMKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzV0x%2FccYp9dMzQ0QMq3AOKOW73Yal%2BPOvsAdPlfEkIBSlB5bxFQn2fih6ZaVZqjIe0KAHf4L3pQP9F8ZC5hZge6pNnmTcNVmUMnd%2FrG0UbI0pW7FrNnLXsOnHD%2Fto3u9fGAkvj6yjAACzs8CMK%2FFz4Nji%2FuPL2OxVs5vEb%2F9fQkV%2FN8eH7JCE7P3gc%2Bof1QrbDgP2ixpSSAUVGAGQ33oGmkF%2B%2F46AucoTVaiA%2BzJIaig5nXuN76oc%2BkEOU9v%2Fne02prEKC%2B7yhYQSj%2BBeNZDGsU7GWNIbuZIg3dYJ0sJEwWMu17Yy2V5xYi7ApKtFQobHOfheL%2BiDsx8Jwu7zq8rNYyzj3IFrxptdwOiAoG84gOZyCH1bP0gfuOeDqVibumCgHaaS8bqz%2FXN%2FngKnEJA%2FXl9j6tNGNdhTHb4%2BqpF5l%2BQYLToOl0nMJu4GxIoF5DIc8Wly30q6RkjhEDGxjPibKnQGyWZ469WmUD%2FHp6tvQttX%2Frvv4diDJhOi8TFVYU5GUkrR6RCrQo7LWZO2iP0vh89jbfMUGXlSdW1DVdjSV3TVo5Sk7ulxraeRRsnSGam6SeWhhUC7EOWO7xb8oDML3GA2MtGFeqZer8tm7mcxnM6UtJR%2FfK1hY4LxPdgvLnheqvTwvmSurx8nt%2FTDJxvi8BjqkAdzKF1BChac6tsK65ZaNHrOjKWt%2Blq1l%2FolwTL%2BHcg%2BIVMr25oYXf5iH9hrfYRtIOhSM5zuMn%2BPRx02bX4%2BnV4gf95rXreIwesrIwmN5OtiFV7vUAE5DMZRvqMi9r9os2GVIbWXlmmvKv1S9GC%2BwDD6Uk9Q9k%2Bova29fkWN2itIxNAazYfa7wk7wJx3i23RLMc2YaQ%2Bbys0AoLnz8mfWoSxpw0ug&X-Amz-Signature=ed2406fba8d6dd3412d84000d256be7546538d0b477e028da6be73d9ef9a0abb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MUOUN2Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHPQyBRtX029VYDUXgcILRkAHhYUQZzlGtDIhipwnzU8AiAesmzJ1FghT5nWPPNN7aZuHFn39nchNvGlj%2F86C1p4ciqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrFgawwVcdpKRxoxFKtwDQcbKXwViLgBjRwBTxnCW7r5qD5MPdQuCF1XJAKV%2B%2FTIFMvl0YTwOqE6lMTnFvh%2FbfFalZJtxpz6vC5tTWhxErTJ4lWtXhq8zkCpLa3Q9SEwSBdUZ55VwJSY3qFVL%2BYEN0SdlhdU3hlOszIIvx8yZXX%2BP640BBDty25Rig57WehNklz5phnzYEE0jVdKzUMRh%2BlR8NjEhJmga8mYT54MaeBOSCGgAfEouUbeI0TtlN4yee1BUQz%2BcGMR4LVmryTSQL2bi%2FAovbbQLhGuO2pqIC2MiVnf%2B5DoLEz%2FOkVGTGgsQifL99WpReG90M8w8IvRaymZKSlbonqS%2F%2BI4R8PLYeaa7rhRwFeOTQejfVlUAPnux2N1q5wiGJ9S%2FPsOPdrdpD2tXJbxW%2FLVUcaMRWOA75wPI4lyLz47gf2H%2FpUTAR0o1G44sLaKjhbuhJ2kahTlos5wZ4ZMDl0gUxootPoqSytr22NMZHZHMZ%2FgnXvFaEdjdVwh7EyDtrb%2FtyxLdUBzcHY7kiHCbU3IL2g4rjNGVaNfWsEf5mNwLOtfuw%2B1G0JeWzGB9zYfcRaW484cP2DlIffPNkicqThbYzmhwoHhVdIrOK9ltXiWaBIHnPg0Tq%2BeE71g6tdfr0pDTBrQwjsD4vAY6pgEYhvPgoIT2Aljmt1OJTBcPYKEkcR8I9PZqIVy4IgmBzUWqJ%2BFfwGsKfbVHPy8Np1fIVNZuDfz2ROEfpsbzNE1eh%2BKfa0Rar9ZsGxAIoltF5r%2Bgde2xZAoilyUlPRcNGqs1CqoNjxYY11%2FuR7lWRUIQgPwvlQ2XE2zA%2FeD%2BRShFJBNn%2FeawCJrOv0hd3SdTFNZfy%2BRfVZ6fmfvCiOgNsWjW4tPf6s9M&X-Amz-Signature=bc04070f871aceb1da637cf4de7a3f53d88fe493dbcab4347c801776ba88f43f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MUOUN2Q%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHPQyBRtX029VYDUXgcILRkAHhYUQZzlGtDIhipwnzU8AiAesmzJ1FghT5nWPPNN7aZuHFn39nchNvGlj%2F86C1p4ciqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrFgawwVcdpKRxoxFKtwDQcbKXwViLgBjRwBTxnCW7r5qD5MPdQuCF1XJAKV%2B%2FTIFMvl0YTwOqE6lMTnFvh%2FbfFalZJtxpz6vC5tTWhxErTJ4lWtXhq8zkCpLa3Q9SEwSBdUZ55VwJSY3qFVL%2BYEN0SdlhdU3hlOszIIvx8yZXX%2BP640BBDty25Rig57WehNklz5phnzYEE0jVdKzUMRh%2BlR8NjEhJmga8mYT54MaeBOSCGgAfEouUbeI0TtlN4yee1BUQz%2BcGMR4LVmryTSQL2bi%2FAovbbQLhGuO2pqIC2MiVnf%2B5DoLEz%2FOkVGTGgsQifL99WpReG90M8w8IvRaymZKSlbonqS%2F%2BI4R8PLYeaa7rhRwFeOTQejfVlUAPnux2N1q5wiGJ9S%2FPsOPdrdpD2tXJbxW%2FLVUcaMRWOA75wPI4lyLz47gf2H%2FpUTAR0o1G44sLaKjhbuhJ2kahTlos5wZ4ZMDl0gUxootPoqSytr22NMZHZHMZ%2FgnXvFaEdjdVwh7EyDtrb%2FtyxLdUBzcHY7kiHCbU3IL2g4rjNGVaNfWsEf5mNwLOtfuw%2B1G0JeWzGB9zYfcRaW484cP2DlIffPNkicqThbYzmhwoHhVdIrOK9ltXiWaBIHnPg0Tq%2BeE71g6tdfr0pDTBrQwjsD4vAY6pgEYhvPgoIT2Aljmt1OJTBcPYKEkcR8I9PZqIVy4IgmBzUWqJ%2BFfwGsKfbVHPy8Np1fIVNZuDfz2ROEfpsbzNE1eh%2BKfa0Rar9ZsGxAIoltF5r%2Bgde2xZAoilyUlPRcNGqs1CqoNjxYY11%2FuR7lWRUIQgPwvlQ2XE2zA%2FeD%2BRShFJBNn%2FeawCJrOv0hd3SdTFNZfy%2BRfVZ6fmfvCiOgNsWjW4tPf6s9M&X-Amz-Signature=69e9d299fdf4e5675502fca57b62301d1945d8ae406806c427a73a5b2c839ab6&X-Amz-SignedHeaders=host&x-id=GetObject)

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
