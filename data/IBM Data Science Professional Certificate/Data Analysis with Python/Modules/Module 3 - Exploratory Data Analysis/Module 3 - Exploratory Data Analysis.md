

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656KTJHXT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIA5WOzWCTX5WhYRr1r7%2FNrVp94eALQfH4EQ44gNTENxbAiEAjT%2BBzqpImWsfpnRL3POY%2B1MfYfRvZ0VPl1m%2FB5V9llEqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPXRgxu6s1YH9JkzaCrcA00hExxil7XzK1d25N7CZzFDYNtEvd54HvGymlvK2f2BLwEQX8htfHOWL2oi2xRhtnN0NAvjFpn4xXhWmxpTj%2BgIWhebvgi3RTdqVdL87a8Dpa385h16Glqb8QLYmA3R1UnZNV3HRMpCNd%2FPb2rD54CDtKLm3MJ5BC%2F9ocWUdrOyTLdZTZvF2ZNoGTLfOWBpn68%2F4aN1Euf2VT%2FNLMdIDypnrwjWWjlldrsF8M6CL8RLwFuAOUPdmaFOcgywjtfff7gcs%2BXsfs2jfZfY0O85fJEKb3CTDZaDGVOZ4DO8lss9Wsl%2B46DOQW5keqjf3XxOJ3Poyv%2FsWUGeAQqF3pVM2lJcYWtyapAjjsU78PaH7UMhWjCJ1WCesROZyVYTu1Oz6CH40kE3MhIlHsHjIAzMa1pi7b2iD1JIxDzlxTYHOXCMfF5O0HTZ0k%2BC2NGF4zYr%2Bk7JtMZLtlGznSKof12A9a3gBMOI3BVXN%2Boaz6gOqDrNT6cZWNFgvJPSSMRC7NIcyhq8ZCJdfp%2B6HZRDocPyeOK380L0Jz09YG24Pamd%2BK8BoLdFbSiJ8VHrVQgraV9QaXTEgByvWtEc8f08%2FLMXPlOnb%2BRg0NcmzRiHqmhn%2BYkctHgddQU9yJ2XGK32MM7Um70GOqUBy7%2BG5sXF6EMmSMEcvNSxZBjXQ7eMFSTpQCuAiHDv6MnY43pRlKcgtzFQRE0HJg6p5vNMpqURrF2YvzUbd9deHKkbKIy9CXJqilyV1w0EQVeefOL5MbhCtzTWC18zyEuzZjAHuYHSRyAXsWUpbjhUCd93e6TGZQNoktBkGY6E2rUI2RG4dyIxpGMwfZ6cIIWHKWOC0w4bO%2F7Pb53wzwoIZdPgN3DT&X-Amz-Signature=92c5dd3a31cf30563d03750171b5be6fb3f8d10ffdcbc4887e3e66b649389358&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656KTJHXT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIA5WOzWCTX5WhYRr1r7%2FNrVp94eALQfH4EQ44gNTENxbAiEAjT%2BBzqpImWsfpnRL3POY%2B1MfYfRvZ0VPl1m%2FB5V9llEqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPXRgxu6s1YH9JkzaCrcA00hExxil7XzK1d25N7CZzFDYNtEvd54HvGymlvK2f2BLwEQX8htfHOWL2oi2xRhtnN0NAvjFpn4xXhWmxpTj%2BgIWhebvgi3RTdqVdL87a8Dpa385h16Glqb8QLYmA3R1UnZNV3HRMpCNd%2FPb2rD54CDtKLm3MJ5BC%2F9ocWUdrOyTLdZTZvF2ZNoGTLfOWBpn68%2F4aN1Euf2VT%2FNLMdIDypnrwjWWjlldrsF8M6CL8RLwFuAOUPdmaFOcgywjtfff7gcs%2BXsfs2jfZfY0O85fJEKb3CTDZaDGVOZ4DO8lss9Wsl%2B46DOQW5keqjf3XxOJ3Poyv%2FsWUGeAQqF3pVM2lJcYWtyapAjjsU78PaH7UMhWjCJ1WCesROZyVYTu1Oz6CH40kE3MhIlHsHjIAzMa1pi7b2iD1JIxDzlxTYHOXCMfF5O0HTZ0k%2BC2NGF4zYr%2Bk7JtMZLtlGznSKof12A9a3gBMOI3BVXN%2Boaz6gOqDrNT6cZWNFgvJPSSMRC7NIcyhq8ZCJdfp%2B6HZRDocPyeOK380L0Jz09YG24Pamd%2BK8BoLdFbSiJ8VHrVQgraV9QaXTEgByvWtEc8f08%2FLMXPlOnb%2BRg0NcmzRiHqmhn%2BYkctHgddQU9yJ2XGK32MM7Um70GOqUBy7%2BG5sXF6EMmSMEcvNSxZBjXQ7eMFSTpQCuAiHDv6MnY43pRlKcgtzFQRE0HJg6p5vNMpqURrF2YvzUbd9deHKkbKIy9CXJqilyV1w0EQVeefOL5MbhCtzTWC18zyEuzZjAHuYHSRyAXsWUpbjhUCd93e6TGZQNoktBkGY6E2rUI2RG4dyIxpGMwfZ6cIIWHKWOC0w4bO%2F7Pb53wzwoIZdPgN3DT&X-Amz-Signature=b6b447cec101b8465d454d2177c2689f7dc99ab3e5082868b45447194d74681c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656KTJHXT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIA5WOzWCTX5WhYRr1r7%2FNrVp94eALQfH4EQ44gNTENxbAiEAjT%2BBzqpImWsfpnRL3POY%2B1MfYfRvZ0VPl1m%2FB5V9llEqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPXRgxu6s1YH9JkzaCrcA00hExxil7XzK1d25N7CZzFDYNtEvd54HvGymlvK2f2BLwEQX8htfHOWL2oi2xRhtnN0NAvjFpn4xXhWmxpTj%2BgIWhebvgi3RTdqVdL87a8Dpa385h16Glqb8QLYmA3R1UnZNV3HRMpCNd%2FPb2rD54CDtKLm3MJ5BC%2F9ocWUdrOyTLdZTZvF2ZNoGTLfOWBpn68%2F4aN1Euf2VT%2FNLMdIDypnrwjWWjlldrsF8M6CL8RLwFuAOUPdmaFOcgywjtfff7gcs%2BXsfs2jfZfY0O85fJEKb3CTDZaDGVOZ4DO8lss9Wsl%2B46DOQW5keqjf3XxOJ3Poyv%2FsWUGeAQqF3pVM2lJcYWtyapAjjsU78PaH7UMhWjCJ1WCesROZyVYTu1Oz6CH40kE3MhIlHsHjIAzMa1pi7b2iD1JIxDzlxTYHOXCMfF5O0HTZ0k%2BC2NGF4zYr%2Bk7JtMZLtlGznSKof12A9a3gBMOI3BVXN%2Boaz6gOqDrNT6cZWNFgvJPSSMRC7NIcyhq8ZCJdfp%2B6HZRDocPyeOK380L0Jz09YG24Pamd%2BK8BoLdFbSiJ8VHrVQgraV9QaXTEgByvWtEc8f08%2FLMXPlOnb%2BRg0NcmzRiHqmhn%2BYkctHgddQU9yJ2XGK32MM7Um70GOqUBy7%2BG5sXF6EMmSMEcvNSxZBjXQ7eMFSTpQCuAiHDv6MnY43pRlKcgtzFQRE0HJg6p5vNMpqURrF2YvzUbd9deHKkbKIy9CXJqilyV1w0EQVeefOL5MbhCtzTWC18zyEuzZjAHuYHSRyAXsWUpbjhUCd93e6TGZQNoktBkGY6E2rUI2RG4dyIxpGMwfZ6cIIWHKWOC0w4bO%2F7Pb53wzwoIZdPgN3DT&X-Amz-Signature=8df17f899ce54ca49bd2e71f48de5d2e09156417a2e646a18765820860767548&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EX62XHX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQC0HgimzEddoFU5bXS8boa9AvM%2Fc3uTTKJ4%2Bx5zhUQgAQIhAJcIN2XLWkANmFE%2BxqHMbdH0MGtIOw2waMYDTpXeXh29KogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEx5G2r9Zf9D1zSGIq3AM%2Bdiab8%2B2KR9ddpcBKgHQyzdyL6MyOYKFPZs6pJC2mX5%2FbICWd54j00svOdyCJJBtdps7MO5EswQ%2FIPXgGkcHwch6mFtRZ%2BlppDyP%2FXcTV3oloXgV36HI%2FLkhkje8sgvQHvCN2JBWc4pikUzI76%2FMiRlgZGgWPi55QvWPCgse8GSrGDUKMxhUPOVJv2ZfmeqfyilH24vVb5ZVWV722rAGwvQA22IoeiMKG%2BeId%2FiLxK6OsPDQqEVc1R6hIc%2FJFrennjhMWRxGCHq4qt4c9%2FznLowskB5WN7zLnI86LLkJ%2FbTFDW7EXFSqtSPKiKHoi3sTZ67mkuNc4nfPLyUj%2FXZvCT2dur0BzrQPEj6NCAhjo1LECwp1OT1vUM7ZNZPpJ40bgCLz8H9EOHE%2BcfIYbDVOnxOPo2NlDKhyKr6ZY3eMq2vcrkQ4JhlWsMQi2UHtBO%2FuqxGmVslm%2FvEo812GIqhbxqqa5tyLUT2VbYWiVFU7Bz1Rt6vIuWqKf%2FCtxVt5ZLi1iJweNrpXOwaR3uQuUYLXwIg1xNxDTHEsvdt1fC2yQGHQPJsMQ%2F4hZ83FeUvu%2FAh00LEVgdRcyhwL2wVHiyonRR7yovSUgp824DtOIBXhka6I3M2Ks5BqzgesBNzCJ1Ju9BjqkAfvla4YzxOGr6dezGe1QXCWyjhIfvO%2FI8BeiW2vjrXXnh%2F7JE3B5vgKyIdSKTsUyGkEAuw1iQo1Ydepk2RkQUww%2B2Ffhz8M6Vt8qz7Q6BzvKrzyZx1nCHFL54MZkysfos%2FynINE1AbWN9vTJsjH7SVsPv%2BUBIjHjryUpydmvUPoNquhNi4Dcvj3L31lzGgupL6bMbbzP2su8yCSSN9WpUNzt9MCG&X-Amz-Signature=fbe92aa42203069280688a4cc2b237390729bea885325b5945bccb094e0f90b6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EX62XHX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQC0HgimzEddoFU5bXS8boa9AvM%2Fc3uTTKJ4%2Bx5zhUQgAQIhAJcIN2XLWkANmFE%2BxqHMbdH0MGtIOw2waMYDTpXeXh29KogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEx5G2r9Zf9D1zSGIq3AM%2Bdiab8%2B2KR9ddpcBKgHQyzdyL6MyOYKFPZs6pJC2mX5%2FbICWd54j00svOdyCJJBtdps7MO5EswQ%2FIPXgGkcHwch6mFtRZ%2BlppDyP%2FXcTV3oloXgV36HI%2FLkhkje8sgvQHvCN2JBWc4pikUzI76%2FMiRlgZGgWPi55QvWPCgse8GSrGDUKMxhUPOVJv2ZfmeqfyilH24vVb5ZVWV722rAGwvQA22IoeiMKG%2BeId%2FiLxK6OsPDQqEVc1R6hIc%2FJFrennjhMWRxGCHq4qt4c9%2FznLowskB5WN7zLnI86LLkJ%2FbTFDW7EXFSqtSPKiKHoi3sTZ67mkuNc4nfPLyUj%2FXZvCT2dur0BzrQPEj6NCAhjo1LECwp1OT1vUM7ZNZPpJ40bgCLz8H9EOHE%2BcfIYbDVOnxOPo2NlDKhyKr6ZY3eMq2vcrkQ4JhlWsMQi2UHtBO%2FuqxGmVslm%2FvEo812GIqhbxqqa5tyLUT2VbYWiVFU7Bz1Rt6vIuWqKf%2FCtxVt5ZLi1iJweNrpXOwaR3uQuUYLXwIg1xNxDTHEsvdt1fC2yQGHQPJsMQ%2F4hZ83FeUvu%2FAh00LEVgdRcyhwL2wVHiyonRR7yovSUgp824DtOIBXhka6I3M2Ks5BqzgesBNzCJ1Ju9BjqkAfvla4YzxOGr6dezGe1QXCWyjhIfvO%2FI8BeiW2vjrXXnh%2F7JE3B5vgKyIdSKTsUyGkEAuw1iQo1Ydepk2RkQUww%2B2Ffhz8M6Vt8qz7Q6BzvKrzyZx1nCHFL54MZkysfos%2FynINE1AbWN9vTJsjH7SVsPv%2BUBIjHjryUpydmvUPoNquhNi4Dcvj3L31lzGgupL6bMbbzP2su8yCSSN9WpUNzt9MCG&X-Amz-Signature=4066e6ed33d1307f9fd7328dd2ecf73afc053d387edca507b6572e2542202901&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EX62XHX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQC0HgimzEddoFU5bXS8boa9AvM%2Fc3uTTKJ4%2Bx5zhUQgAQIhAJcIN2XLWkANmFE%2BxqHMbdH0MGtIOw2waMYDTpXeXh29KogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEx5G2r9Zf9D1zSGIq3AM%2Bdiab8%2B2KR9ddpcBKgHQyzdyL6MyOYKFPZs6pJC2mX5%2FbICWd54j00svOdyCJJBtdps7MO5EswQ%2FIPXgGkcHwch6mFtRZ%2BlppDyP%2FXcTV3oloXgV36HI%2FLkhkje8sgvQHvCN2JBWc4pikUzI76%2FMiRlgZGgWPi55QvWPCgse8GSrGDUKMxhUPOVJv2ZfmeqfyilH24vVb5ZVWV722rAGwvQA22IoeiMKG%2BeId%2FiLxK6OsPDQqEVc1R6hIc%2FJFrennjhMWRxGCHq4qt4c9%2FznLowskB5WN7zLnI86LLkJ%2FbTFDW7EXFSqtSPKiKHoi3sTZ67mkuNc4nfPLyUj%2FXZvCT2dur0BzrQPEj6NCAhjo1LECwp1OT1vUM7ZNZPpJ40bgCLz8H9EOHE%2BcfIYbDVOnxOPo2NlDKhyKr6ZY3eMq2vcrkQ4JhlWsMQi2UHtBO%2FuqxGmVslm%2FvEo812GIqhbxqqa5tyLUT2VbYWiVFU7Bz1Rt6vIuWqKf%2FCtxVt5ZLi1iJweNrpXOwaR3uQuUYLXwIg1xNxDTHEsvdt1fC2yQGHQPJsMQ%2F4hZ83FeUvu%2FAh00LEVgdRcyhwL2wVHiyonRR7yovSUgp824DtOIBXhka6I3M2Ks5BqzgesBNzCJ1Ju9BjqkAfvla4YzxOGr6dezGe1QXCWyjhIfvO%2FI8BeiW2vjrXXnh%2F7JE3B5vgKyIdSKTsUyGkEAuw1iQo1Ydepk2RkQUww%2B2Ffhz8M6Vt8qz7Q6BzvKrzyZx1nCHFL54MZkysfos%2FynINE1AbWN9vTJsjH7SVsPv%2BUBIjHjryUpydmvUPoNquhNi4Dcvj3L31lzGgupL6bMbbzP2su8yCSSN9WpUNzt9MCG&X-Amz-Signature=916f10609271eef118b17a786d28ff24f91d14898699aff1ab6ab9a556797181&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EX62XHX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQC0HgimzEddoFU5bXS8boa9AvM%2Fc3uTTKJ4%2Bx5zhUQgAQIhAJcIN2XLWkANmFE%2BxqHMbdH0MGtIOw2waMYDTpXeXh29KogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEx5G2r9Zf9D1zSGIq3AM%2Bdiab8%2B2KR9ddpcBKgHQyzdyL6MyOYKFPZs6pJC2mX5%2FbICWd54j00svOdyCJJBtdps7MO5EswQ%2FIPXgGkcHwch6mFtRZ%2BlppDyP%2FXcTV3oloXgV36HI%2FLkhkje8sgvQHvCN2JBWc4pikUzI76%2FMiRlgZGgWPi55QvWPCgse8GSrGDUKMxhUPOVJv2ZfmeqfyilH24vVb5ZVWV722rAGwvQA22IoeiMKG%2BeId%2FiLxK6OsPDQqEVc1R6hIc%2FJFrennjhMWRxGCHq4qt4c9%2FznLowskB5WN7zLnI86LLkJ%2FbTFDW7EXFSqtSPKiKHoi3sTZ67mkuNc4nfPLyUj%2FXZvCT2dur0BzrQPEj6NCAhjo1LECwp1OT1vUM7ZNZPpJ40bgCLz8H9EOHE%2BcfIYbDVOnxOPo2NlDKhyKr6ZY3eMq2vcrkQ4JhlWsMQi2UHtBO%2FuqxGmVslm%2FvEo812GIqhbxqqa5tyLUT2VbYWiVFU7Bz1Rt6vIuWqKf%2FCtxVt5ZLi1iJweNrpXOwaR3uQuUYLXwIg1xNxDTHEsvdt1fC2yQGHQPJsMQ%2F4hZ83FeUvu%2FAh00LEVgdRcyhwL2wVHiyonRR7yovSUgp824DtOIBXhka6I3M2Ks5BqzgesBNzCJ1Ju9BjqkAfvla4YzxOGr6dezGe1QXCWyjhIfvO%2FI8BeiW2vjrXXnh%2F7JE3B5vgKyIdSKTsUyGkEAuw1iQo1Ydepk2RkQUww%2B2Ffhz8M6Vt8qz7Q6BzvKrzyZx1nCHFL54MZkysfos%2FynINE1AbWN9vTJsjH7SVsPv%2BUBIjHjryUpydmvUPoNquhNi4Dcvj3L31lzGgupL6bMbbzP2su8yCSSN9WpUNzt9MCG&X-Amz-Signature=00df6e8478af922d2c9ebd8411cfb487150ffdeec7ce95a81dc54282c25f0315&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EX62XHX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQC0HgimzEddoFU5bXS8boa9AvM%2Fc3uTTKJ4%2Bx5zhUQgAQIhAJcIN2XLWkANmFE%2BxqHMbdH0MGtIOw2waMYDTpXeXh29KogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEx5G2r9Zf9D1zSGIq3AM%2Bdiab8%2B2KR9ddpcBKgHQyzdyL6MyOYKFPZs6pJC2mX5%2FbICWd54j00svOdyCJJBtdps7MO5EswQ%2FIPXgGkcHwch6mFtRZ%2BlppDyP%2FXcTV3oloXgV36HI%2FLkhkje8sgvQHvCN2JBWc4pikUzI76%2FMiRlgZGgWPi55QvWPCgse8GSrGDUKMxhUPOVJv2ZfmeqfyilH24vVb5ZVWV722rAGwvQA22IoeiMKG%2BeId%2FiLxK6OsPDQqEVc1R6hIc%2FJFrennjhMWRxGCHq4qt4c9%2FznLowskB5WN7zLnI86LLkJ%2FbTFDW7EXFSqtSPKiKHoi3sTZ67mkuNc4nfPLyUj%2FXZvCT2dur0BzrQPEj6NCAhjo1LECwp1OT1vUM7ZNZPpJ40bgCLz8H9EOHE%2BcfIYbDVOnxOPo2NlDKhyKr6ZY3eMq2vcrkQ4JhlWsMQi2UHtBO%2FuqxGmVslm%2FvEo812GIqhbxqqa5tyLUT2VbYWiVFU7Bz1Rt6vIuWqKf%2FCtxVt5ZLi1iJweNrpXOwaR3uQuUYLXwIg1xNxDTHEsvdt1fC2yQGHQPJsMQ%2F4hZ83FeUvu%2FAh00LEVgdRcyhwL2wVHiyonRR7yovSUgp824DtOIBXhka6I3M2Ks5BqzgesBNzCJ1Ju9BjqkAfvla4YzxOGr6dezGe1QXCWyjhIfvO%2FI8BeiW2vjrXXnh%2F7JE3B5vgKyIdSKTsUyGkEAuw1iQo1Ydepk2RkQUww%2B2Ffhz8M6Vt8qz7Q6BzvKrzyZx1nCHFL54MZkysfos%2FynINE1AbWN9vTJsjH7SVsPv%2BUBIjHjryUpydmvUPoNquhNi4Dcvj3L31lzGgupL6bMbbzP2su8yCSSN9WpUNzt9MCG&X-Amz-Signature=bd36945222402cc5c6bf081d1ab046d123dbda08f2fb37aa47f769b5f06d1ec6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EX62XHX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQC0HgimzEddoFU5bXS8boa9AvM%2Fc3uTTKJ4%2Bx5zhUQgAQIhAJcIN2XLWkANmFE%2BxqHMbdH0MGtIOw2waMYDTpXeXh29KogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEx5G2r9Zf9D1zSGIq3AM%2Bdiab8%2B2KR9ddpcBKgHQyzdyL6MyOYKFPZs6pJC2mX5%2FbICWd54j00svOdyCJJBtdps7MO5EswQ%2FIPXgGkcHwch6mFtRZ%2BlppDyP%2FXcTV3oloXgV36HI%2FLkhkje8sgvQHvCN2JBWc4pikUzI76%2FMiRlgZGgWPi55QvWPCgse8GSrGDUKMxhUPOVJv2ZfmeqfyilH24vVb5ZVWV722rAGwvQA22IoeiMKG%2BeId%2FiLxK6OsPDQqEVc1R6hIc%2FJFrennjhMWRxGCHq4qt4c9%2FznLowskB5WN7zLnI86LLkJ%2FbTFDW7EXFSqtSPKiKHoi3sTZ67mkuNc4nfPLyUj%2FXZvCT2dur0BzrQPEj6NCAhjo1LECwp1OT1vUM7ZNZPpJ40bgCLz8H9EOHE%2BcfIYbDVOnxOPo2NlDKhyKr6ZY3eMq2vcrkQ4JhlWsMQi2UHtBO%2FuqxGmVslm%2FvEo812GIqhbxqqa5tyLUT2VbYWiVFU7Bz1Rt6vIuWqKf%2FCtxVt5ZLi1iJweNrpXOwaR3uQuUYLXwIg1xNxDTHEsvdt1fC2yQGHQPJsMQ%2F4hZ83FeUvu%2FAh00LEVgdRcyhwL2wVHiyonRR7yovSUgp824DtOIBXhka6I3M2Ks5BqzgesBNzCJ1Ju9BjqkAfvla4YzxOGr6dezGe1QXCWyjhIfvO%2FI8BeiW2vjrXXnh%2F7JE3B5vgKyIdSKTsUyGkEAuw1iQo1Ydepk2RkQUww%2B2Ffhz8M6Vt8qz7Q6BzvKrzyZx1nCHFL54MZkysfos%2FynINE1AbWN9vTJsjH7SVsPv%2BUBIjHjryUpydmvUPoNquhNi4Dcvj3L31lzGgupL6bMbbzP2su8yCSSN9WpUNzt9MCG&X-Amz-Signature=b90a9cefea1b03e884a9f77d0a00245b5c61ed82ef2baf6b81659954db931c97&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M7JGWPP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQCcDhzTP1md9aQigQTuSXJueACggnXjbgvnZNraN%2FFofQIgZAEFBdzo%2F0aprij4HYysfZDAuqmUMkPaldItSXkiogcqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzKfhDlol1uaUJHACrcAzg3DpTh5R%2BeFJZo1a7RsWSlX%2B3tVMfr1Bx6fE7X0B3ZE5QGIvizdpt3wYE7RC5KNrDdmLNcmTDzLiCwgIgX0uf0LjRjZXa3o3zXW2O7%2FjHqaq%2BF09hMEZwf8DWmUcLBU854UbSsdMKzkNFpa7zYme6fiiLL34BIs1icafn%2BFAPA6HVRrWQ72MZ39Y5KtaP09B%2FZtiFuliErA2M81rv3s2a1B2vO5gbv4f2AuSiIs%2FVGuRQWzjCVguK%2BIsgbjethE%2Fy9eBnJwO%2BkMRgCFNhHpGPr6xbNuAeOLQSFsCAti6FmisactFjw63eG3zpoaJcDR73ImxloVqmnmCp5u1BdL%2FMJbNxlVVH8PuCMoA7Fs9o8%2FaC58nkOGui6zMVqY8O7d1Lr%2BlS4Y%2BSR0HlMgTsdEofKptzOv%2BnhONj6Kk3bApeqUUnwbnB%2Fe7R3ThnQ3MK0ArFa1S4%2BLinFfqTvWV8N9TFKk2Ahsekj%2FyVoC5b3x8G75wT8XFshD047Ep44eDG%2B%2Fy2tv3iBL0LUL%2F11hWasJahWYy2skM799cjwnoCioq4VzjWS%2FCn9qgSszxO2tL7QMx9BRGLM7JmKsrUdIlWOXastv4LJMt0wuUSbNhNboPZ7zYNWJDHxpKCEqbZOMLrUm70GOqUBrqG5jw30BdksCM9dJz%2B0RlLa%2FirvONe4OrfOlsDus8MlBygxWuyzisYuugEeI7fRlnVqIJ%2FrIU6Vj%2F1RAMebmOcAG1Nssq%2BCcrFgJUevW9UIv7%2BQ3MpB97E3COv%2BKgWH7yU2D9ZFgLR%2Fp10DQLfEUfc2LDjMc28G%2FQwJSoKYswiNYlZmvBvVf1zAaUJtWYiiQpegOn02Sz0oiRSwIFZd%2BjUXlg2s&X-Amz-Signature=b019636595f34ec4f29e173037dcfc9c82316f091fb74fc9fc64b2920e87e6ee&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVQVL5R3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQC0xtDv%2B8t3pDp3BdWYUPbiwZvc8KWtDFco6Kn2%2FLxJnAIgci%2FjTg7HA6T6FjNDM2MA0QyEU7sPauLAdF1yRmjjcTsqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9YR6LcpxIjPVzeHyrcA29%2Fn7FqQX5POlK3TOAIsYNjghapOHZv3EN2hHkwGrneRyaJLHO%2BHm8kBo00h34jraWd8kPf8Z1KI6Ohyx5riwOKJ7ZUmCS9Drgzyo4e%2Brxmf9ZTcBqeV2bK7MoyPDU8yegxObzjwHmJnt%2F%2BPjciri%2BPM6%2FSYN8CfsJMZimO4Lxf930mlVo6p4G2l3BeSvVbTrVBnDZawrSw7fBrchjvlZke6db4aFxghJen33KTwPZuAzgFw3PzvB1ESGR7O5dvxRrAIAFmRQNyr7W7PTUeIupG2FhDGdf5kCVg8vqEZ%2FKauByyzACBjhgaGT0Ye3ORczd7d307kKYaB1pXV39xBbwTVB%2FG6c%2FkqzfXKPlho25Ol%2FUm2ZwPX5KuXkujlHM6jDI6fiL9q3bAOF84zaB0h0%2F1vdr5pM2xUWrCiNV9WA4m27x34PTySde2vY8vcLsrKjveUw%2FRhqd8sBx3eX3LPLPPSB4grnogBQ7CcnfcPkvYqRLXuwRbRL5yx2B5LOEzYKbWFe5V7eLErQ8uMSnVmQBRk9uHdSt0qCihXur%2FTIQnRFcpG8vA0YUpFM9JRtaLZUsKdIJOBhduc99zdQTXikdeu%2B7UywC3CaV1yx%2BAYN6GlBrVr7tNesuALr95ML7Um70GOqUBV0uAkWyHYlUaPNNhjYUxmH3s3050AXpn1ff2fBjTVjCqWkK%2Fck3DNKC9dDmGl9cRwB3h6TQrAPUjBX87ZblFhds9L%2BsSkdWODGOOVauZaJp84dceYE%2FoGuXW%2FkEi9dsK8wlEqbVv7wU%2FP69df2CY9M6AtUeKAKJefU2Rd7WDnxrrnfCFmxnXNJ045xGJM1Xq2cC8oZ2rhBjfyEpzptRTl2cKJZRV&X-Amz-Signature=26ab56973967093d62e560099ac541b0248a178b13f452a66a272a33ab4de2c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EX62XHX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQC0HgimzEddoFU5bXS8boa9AvM%2Fc3uTTKJ4%2Bx5zhUQgAQIhAJcIN2XLWkANmFE%2BxqHMbdH0MGtIOw2waMYDTpXeXh29KogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEx5G2r9Zf9D1zSGIq3AM%2Bdiab8%2B2KR9ddpcBKgHQyzdyL6MyOYKFPZs6pJC2mX5%2FbICWd54j00svOdyCJJBtdps7MO5EswQ%2FIPXgGkcHwch6mFtRZ%2BlppDyP%2FXcTV3oloXgV36HI%2FLkhkje8sgvQHvCN2JBWc4pikUzI76%2FMiRlgZGgWPi55QvWPCgse8GSrGDUKMxhUPOVJv2ZfmeqfyilH24vVb5ZVWV722rAGwvQA22IoeiMKG%2BeId%2FiLxK6OsPDQqEVc1R6hIc%2FJFrennjhMWRxGCHq4qt4c9%2FznLowskB5WN7zLnI86LLkJ%2FbTFDW7EXFSqtSPKiKHoi3sTZ67mkuNc4nfPLyUj%2FXZvCT2dur0BzrQPEj6NCAhjo1LECwp1OT1vUM7ZNZPpJ40bgCLz8H9EOHE%2BcfIYbDVOnxOPo2NlDKhyKr6ZY3eMq2vcrkQ4JhlWsMQi2UHtBO%2FuqxGmVslm%2FvEo812GIqhbxqqa5tyLUT2VbYWiVFU7Bz1Rt6vIuWqKf%2FCtxVt5ZLi1iJweNrpXOwaR3uQuUYLXwIg1xNxDTHEsvdt1fC2yQGHQPJsMQ%2F4hZ83FeUvu%2FAh00LEVgdRcyhwL2wVHiyonRR7yovSUgp824DtOIBXhka6I3M2Ks5BqzgesBNzCJ1Ju9BjqkAfvla4YzxOGr6dezGe1QXCWyjhIfvO%2FI8BeiW2vjrXXnh%2F7JE3B5vgKyIdSKTsUyGkEAuw1iQo1Ydepk2RkQUww%2B2Ffhz8M6Vt8qz7Q6BzvKrzyZx1nCHFL54MZkysfos%2FynINE1AbWN9vTJsjH7SVsPv%2BUBIjHjryUpydmvUPoNquhNi4Dcvj3L31lzGgupL6bMbbzP2su8yCSSN9WpUNzt9MCG&X-Amz-Signature=fd6c57596b187268f3057c8c0b9d69ee43eb9797479f2221b0d08081107b9467&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EX62XHX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQC0HgimzEddoFU5bXS8boa9AvM%2Fc3uTTKJ4%2Bx5zhUQgAQIhAJcIN2XLWkANmFE%2BxqHMbdH0MGtIOw2waMYDTpXeXh29KogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEx5G2r9Zf9D1zSGIq3AM%2Bdiab8%2B2KR9ddpcBKgHQyzdyL6MyOYKFPZs6pJC2mX5%2FbICWd54j00svOdyCJJBtdps7MO5EswQ%2FIPXgGkcHwch6mFtRZ%2BlppDyP%2FXcTV3oloXgV36HI%2FLkhkje8sgvQHvCN2JBWc4pikUzI76%2FMiRlgZGgWPi55QvWPCgse8GSrGDUKMxhUPOVJv2ZfmeqfyilH24vVb5ZVWV722rAGwvQA22IoeiMKG%2BeId%2FiLxK6OsPDQqEVc1R6hIc%2FJFrennjhMWRxGCHq4qt4c9%2FznLowskB5WN7zLnI86LLkJ%2FbTFDW7EXFSqtSPKiKHoi3sTZ67mkuNc4nfPLyUj%2FXZvCT2dur0BzrQPEj6NCAhjo1LECwp1OT1vUM7ZNZPpJ40bgCLz8H9EOHE%2BcfIYbDVOnxOPo2NlDKhyKr6ZY3eMq2vcrkQ4JhlWsMQi2UHtBO%2FuqxGmVslm%2FvEo812GIqhbxqqa5tyLUT2VbYWiVFU7Bz1Rt6vIuWqKf%2FCtxVt5ZLi1iJweNrpXOwaR3uQuUYLXwIg1xNxDTHEsvdt1fC2yQGHQPJsMQ%2F4hZ83FeUvu%2FAh00LEVgdRcyhwL2wVHiyonRR7yovSUgp824DtOIBXhka6I3M2Ks5BqzgesBNzCJ1Ju9BjqkAfvla4YzxOGr6dezGe1QXCWyjhIfvO%2FI8BeiW2vjrXXnh%2F7JE3B5vgKyIdSKTsUyGkEAuw1iQo1Ydepk2RkQUww%2B2Ffhz8M6Vt8qz7Q6BzvKrzyZx1nCHFL54MZkysfos%2FynINE1AbWN9vTJsjH7SVsPv%2BUBIjHjryUpydmvUPoNquhNi4Dcvj3L31lzGgupL6bMbbzP2su8yCSSN9WpUNzt9MCG&X-Amz-Signature=9be075a4d1f7a8cb7de19c4ce6b7613c247dbecee0fbfa37f26dbbdb2a857171&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EX62XHX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQC0HgimzEddoFU5bXS8boa9AvM%2Fc3uTTKJ4%2Bx5zhUQgAQIhAJcIN2XLWkANmFE%2BxqHMbdH0MGtIOw2waMYDTpXeXh29KogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzEx5G2r9Zf9D1zSGIq3AM%2Bdiab8%2B2KR9ddpcBKgHQyzdyL6MyOYKFPZs6pJC2mX5%2FbICWd54j00svOdyCJJBtdps7MO5EswQ%2FIPXgGkcHwch6mFtRZ%2BlppDyP%2FXcTV3oloXgV36HI%2FLkhkje8sgvQHvCN2JBWc4pikUzI76%2FMiRlgZGgWPi55QvWPCgse8GSrGDUKMxhUPOVJv2ZfmeqfyilH24vVb5ZVWV722rAGwvQA22IoeiMKG%2BeId%2FiLxK6OsPDQqEVc1R6hIc%2FJFrennjhMWRxGCHq4qt4c9%2FznLowskB5WN7zLnI86LLkJ%2FbTFDW7EXFSqtSPKiKHoi3sTZ67mkuNc4nfPLyUj%2FXZvCT2dur0BzrQPEj6NCAhjo1LECwp1OT1vUM7ZNZPpJ40bgCLz8H9EOHE%2BcfIYbDVOnxOPo2NlDKhyKr6ZY3eMq2vcrkQ4JhlWsMQi2UHtBO%2FuqxGmVslm%2FvEo812GIqhbxqqa5tyLUT2VbYWiVFU7Bz1Rt6vIuWqKf%2FCtxVt5ZLi1iJweNrpXOwaR3uQuUYLXwIg1xNxDTHEsvdt1fC2yQGHQPJsMQ%2F4hZ83FeUvu%2FAh00LEVgdRcyhwL2wVHiyonRR7yovSUgp824DtOIBXhka6I3M2Ks5BqzgesBNzCJ1Ju9BjqkAfvla4YzxOGr6dezGe1QXCWyjhIfvO%2FI8BeiW2vjrXXnh%2F7JE3B5vgKyIdSKTsUyGkEAuw1iQo1Ydepk2RkQUww%2B2Ffhz8M6Vt8qz7Q6BzvKrzyZx1nCHFL54MZkysfos%2FynINE1AbWN9vTJsjH7SVsPv%2BUBIjHjryUpydmvUPoNquhNi4Dcvj3L31lzGgupL6bMbbzP2su8yCSSN9WpUNzt9MCG&X-Amz-Signature=0d0490c2a5905fffcfa06987ecab9fd6000a16abea41974f37969d5fb390aa41&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3OBHK5F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIEkwQdbX9s2oMOj6ZxYVQ0mFiFyLdU8eYYQBv7zVgpbtAiBiK6RdP7wnQ1sZsrSOA6C47cMJ57TtuaH%2BbAUXuH93WSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoNfuxEERjKaTc2AeKtwDf3XeqZXgtSeoudqiSTCSgl1uoJSngzx0ZJWjECHnXu1JvM%2Bq2k%2BtKC7NPZ9BczxOe%2BwqBjtJHEPsD1%2F7%2FDmIgRP9ZHIoE9oY1G1ucAAU0XX%2FAjin3a5uNrQhU8Mrp7CH4SEqENjZyM%2FffL33wRpznASUGH0ZGKTX484IzLkRBPFX%2BIB4ubR2xLPGAQviYynetfswGRFGImj7SoT86HwentLZqVSiNKmdXGA3snJPrVfZwGl6QS8Ul7WjnBl%2B1N2DrbIyo9o49gTeNOhe2Kn9DPUEjJWwgFjIxuDnee0G9eJ7kZRGbdSEMfjIBUYUueQZWMiyJb2K1nAj9CQvVPC51BkJpnKo9G%2B%2FWM6Mj5h1LL2xa%2FgvYb05jwkBtJ%2B%2FSqfJBSmNcP7epiI6FPLKIhgj1OJQBjgfo9r1vFVwtGuxUhJlg1rzPxh5ibg2Nj%2Ba6QGu23bm5GjLHnCLJi1M7%2FOVdigFqm8v8txY3d%2FtMDWv%2BMsxk5u6qx8OGzMuY1UipIvGzc3spFio0Xt6J5O5JpbEfAoVobODfuT7Zym2rdJKLz5jDS7mdQ3EPNI2S3%2Fhn4BTUHJErd%2B9U1DKdMR923%2BNqr7Dbpr9u4vbYggaUJOyrMWZZWa6hfz4CFxg4ugwj9SbvQY6pgEyUwaQp3q8BYeHWpudSdlgQ3P%2FuuEhEAv1SoBRCuKZ29sl7t3%2BX0g%2FSbT07hjx34rMfMxJ0lo6SdE%2BMfeYxn0tiRpN4NBpj6Fd8ttI%2BMVTmbHRed7EzeMAxmRQ3r23rlPguAGXEsuIsKLh2h2NtJKjR1mMrgNju4JsS%2BQRCO4hTI3QEsyrETaBbxUAj%2BTvf8HwkE1Z4dfzfRH0P9R%2BrCiigCz8jgOF&X-Amz-Signature=fa845e9259c0d67d059cf0e2c44265ed8a085c77038cbd0b6567512ac632ba24&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDQTBYOJ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIA4myJ9lIwnXO1ulDJjjhaZKF5SpDCQqUuQDE0Mq1QYuAiAoRWv4xFeRDY%2FUg9oenS1XP%2FN2XBWvHEWcjiRiGK3jLyqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMg4YwzirNHHIpldozKtwDq5opmYmD9Ajzb4T2mH1ummPNHDuQb28yKMuGCp6sqgXb6%2BWulqufsa0vMUzsNZgfFDa3W7Xd8kU7Zh4%2BuVyB42WLdiqLr2sgITOgS%2Bw66HuPpbOqaB8cfkWpiE3aP540hteh1ygeID79U1b0jgbv5Zta7e6Or4C%2BhefWDkyjs3%2Ba25kJlcy9DWxMwtiS2VXHi90stQHuHMJSeCiLXgZPfwlagySbF9LzgRuk6wYwNd6pjk9XyJtXgY6hgsDsM2pjO8fVGjWL8bGJdEAeItC7bL7cny3KywmUGxhhg85vYdi6QHrP4UgLxwKaF9v1nqSUjnO%2FeFamGWtodG%2F56EoDgAXANCbtwKNn3mGt1lIoPapNa2NJr7X9AMxBF1UQ0Wtar34CMrOrYdgUKF3I4ae7c0uZESsJ0ZBwnNA4Uv8H%2FoqeqvGTOfLCW%2BZEJ5mXN5Rlrnxige0dkaWc0zt4KFRTRiu4KWaa%2Bs5CoiWIG%2BQP4xkq7AVH74vIGb1glwTtMCKAgz4Ols4ZyjPxVTawQUiFXI9vNqY%2F7vRQfZ7HsRXPz9P1ZEmMDBYcmt6HCXna14sFXb6xNB8UYbcSmPQkhBCzwa8m%2B1I9WKWhEp4YtbPsY1gemZz%2FFXrFxO1t%2F%2F4wwNSbvQY6pgFxF99EynNJCxxx71drjemAnKAgYwUd1lhmTEcxBxifj9CYm95Jt9wgMyMKkfFzazBZRMiClknBQJ5jYxxCZDCvmiKAi%2FFmfpkX0dQp6sl7%2BFuvO5%2FTkQOrmBgdF0JRxhfcqr99qAEPUdX0LhybjeFtDrZDECyfc4Pl4FWDfrwznDtacSrQwwt26W5czZ6erLp1EU56DH3e2XESJQJDt7J7h5ZEz%2B4p&X-Amz-Signature=5ebcb58cb54cc8f042988f942071a8127d6e1b7e51d0b337f366d202c318d526&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFKH6SXJ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIG1bogNGafFWLi1IO8%2FNlJTrV4%2FSQJ%2BEyamKNeC1hz%2BuAiEAy%2Fa8EKTW0sUgMli%2B3I6CF8MwMwfJg2xvsWtJLN%2FBeeYqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDqjyU90scVXXtG0WSrcAzsX5B3mSOxmFirbcyIZCB%2FAEIeD2RsLyaUbRKHIUVSq%2FiVGKt6S%2Ba1%2BrT1P59vrlwZqyyfxIdrDX53ceDWMK88asPVuZSbGsvYFQRcpK3mrV8fkN0QGzk95PUnkZAV6bAMy9zKPBOjfMQHCt3pyV%2BHLD5VM3qak8vMesyFVmaTkJj9m9MBL0mmu4SnAsSDmVMHXbc4%2BcKnwWHNQnuxYkR9kR%2FT9tDaO9D5ybPLN%2B3OgQ6GH53orQszIIH%2BIf8gazaLy9%2BMqnZFR868U1%2FIapHcISsxOE%2BvO5PlFxPqdGGW4xNf1s0k2ec8jCRSPWMT%2BNnXQpaU8OZ9ox2kBGyQorF%2Ftyzh2R0D6CR%2F6bVFdexxxPPuCClG7OorqrPD6QhRAOx1GSadDnAtlnKNsLqieMlESsuBHSO4Btl6CRA%2FYHdDol0VSvo1zyz1qTlKAzWS4jPJVHTPnC3UfoaC8bwynxQbrTPc4iGix7AQFdU9AJNUUVIgfbTe2mCz72NqukNu7d11DLsLptHqNbrgSCQajX8C6xAMTw7v4edFq8ycvraDu%2BsOjp04yhpoiQMlcx5R46O%2B17akmlZjkksU4VSHJunHWLEx5QTMzmk3ZO9%2B658v5lGKCL934gk7I9Oc0MOXUm70GOqUBOdjnNPOh4Wce96YA990w94ogBTWWDWCpQycucedAwcAMdVgr8jbrIMVI%2BNWTv2pypcSs4fHGfDzcgNm7jPgSV75u4dNPJJAkh9pOi60XD3elxbyGWL4JTnrXMT%2F%2B1x07j%2FEavi1eUnNN%2BPFVZHYz82RonZiU9ScB5SdU5EGAMFyWPVXjmxXC42m0%2B1gNRolz1B0kWuU8WmSupYUz3A2sUGL4G3Qz&X-Amz-Signature=44ad6159646f3001c119532cffc3d853500d344abbf816f8d9528390e75f97a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2QRKJKC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQD%2B03nXyLsQ8kveR4N2nc%2BW5c7YF6p8VFV6t0OXV5e8FAIgRS%2Fk5mmG5ppFsPFzJF60xZ2itn8sXEhD2FHXr%2FfaDiAqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMHO3Fexy7UM6md9VyrcA5dKVg2rUJU6B7TzM4rl2YMlq8Lm9wVprRqAtloI9NooPPBY%2FpHimFHs1pCltsBtmnCMWP8XfNWKEB4d9X3sW%2F35VnDvEjOwvjZY7c4neOcFZE8B0RlIsCoXKkhy%2BxJFjpFQk27LXfm8ViXTzQgGCmRFPZjuOqmEMfPpZi7OABc5%2FYeD8zQHs8DCL0ZYOWTnfYPrJvaIqo5iUCx9D7zew6K2OIwrsbwnEFm1iJKri5x3s%2F86M54HgzWLSTNXnJ1dou4GuVbhlw8lyKSINvoOkft6aTBrYtDI8XoEInTZACtMXi%2FdsFg9SgWljQDftGmEa2EVFUkDudZV%2Fm0JaATDMJ9n0mbQiBzNmLJO0SX3fz85cJYNKCDjHSebFpamgNqB7BUQUXP8A49PuwpTkLAsXcOU7DGDklBA%2FBCnF6bXxCjPNSiXTgZ5I6V25LFj2reARGm4YOlcvBwRtVMUBOTF%2BavovebXtupJBmVGmitBI28nX0hHgGydhRtBZ25M9GSoRi3XlN52%2Fx0qd8I2Uj7AWyeU6ij2414hjrHJP5V%2FtOC3FLjeTGpK4z1AwDUgUjeqj4rQfEDERLKilGy0qHegE9UnD6J%2BgOFpDM6Ohbio5DYNq7Gs5zSQtldjOP%2FwMMPUm70GOqUBejpW8mzDzQezsFZUxwHmqCugAUVaVz4QIVe%2BTLr4k9O8I5Q5IvlN8%2BBE9tFUC2K3HBiXcCAjw1WfG09V%2BXVbDAqd8PndVMiznBmMrpBsErBPkzWZtghkxJWFi5WwXiMLYEXAMHUThz0aK2sL%2BsAgveW7MYPkjcbS31wWfRGn69zu1uadeehMWY5W1nYR1m5WWO8%2Fxz2gb%2FFfzktV%2F5HEl264g2HD&X-Amz-Signature=4711f1c03d9f927439c7fe250b0e17049b69de1a329ec84ed24c86a8980db3f2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2QRKJKC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQD%2B03nXyLsQ8kveR4N2nc%2BW5c7YF6p8VFV6t0OXV5e8FAIgRS%2Fk5mmG5ppFsPFzJF60xZ2itn8sXEhD2FHXr%2FfaDiAqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMHO3Fexy7UM6md9VyrcA5dKVg2rUJU6B7TzM4rl2YMlq8Lm9wVprRqAtloI9NooPPBY%2FpHimFHs1pCltsBtmnCMWP8XfNWKEB4d9X3sW%2F35VnDvEjOwvjZY7c4neOcFZE8B0RlIsCoXKkhy%2BxJFjpFQk27LXfm8ViXTzQgGCmRFPZjuOqmEMfPpZi7OABc5%2FYeD8zQHs8DCL0ZYOWTnfYPrJvaIqo5iUCx9D7zew6K2OIwrsbwnEFm1iJKri5x3s%2F86M54HgzWLSTNXnJ1dou4GuVbhlw8lyKSINvoOkft6aTBrYtDI8XoEInTZACtMXi%2FdsFg9SgWljQDftGmEa2EVFUkDudZV%2Fm0JaATDMJ9n0mbQiBzNmLJO0SX3fz85cJYNKCDjHSebFpamgNqB7BUQUXP8A49PuwpTkLAsXcOU7DGDklBA%2FBCnF6bXxCjPNSiXTgZ5I6V25LFj2reARGm4YOlcvBwRtVMUBOTF%2BavovebXtupJBmVGmitBI28nX0hHgGydhRtBZ25M9GSoRi3XlN52%2Fx0qd8I2Uj7AWyeU6ij2414hjrHJP5V%2FtOC3FLjeTGpK4z1AwDUgUjeqj4rQfEDERLKilGy0qHegE9UnD6J%2BgOFpDM6Ohbio5DYNq7Gs5zSQtldjOP%2FwMMPUm70GOqUBejpW8mzDzQezsFZUxwHmqCugAUVaVz4QIVe%2BTLr4k9O8I5Q5IvlN8%2BBE9tFUC2K3HBiXcCAjw1WfG09V%2BXVbDAqd8PndVMiznBmMrpBsErBPkzWZtghkxJWFi5WwXiMLYEXAMHUThz0aK2sL%2BsAgveW7MYPkjcbS31wWfRGn69zu1uadeehMWY5W1nYR1m5WWO8%2Fxz2gb%2FFfzktV%2F5HEl264g2HD&X-Amz-Signature=d45ae8d126ab9537e3dff630e48473e03e520a0e718bdefe5170c5a6fad05243&X-Amz-SignedHeaders=host&x-id=GetObject)

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
