

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7CGYWG2%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDUx9%2BQMIGFX3n9pVotofYHN6Bx0XNbetyRSRmCdA0DmwIhAKQBnG5cs0MLb0YZhlcukvXT%2FRqkIQy37FWyqivG983HKv8DCFIQABoMNjM3NDIzMTgzODA1IgwF0NP7XI3WeiGhbs4q3AOYmd7UPApqXOyNg5BPvgH4uV%2Fo8rphHZ8hLms1DVglfdQ7vcsaqRCOFIsIenoJBLaw8Z9Po53bKl93GItX1aJpcRBapzja5byLenxthPRRKeJKAIeaGowcj2c0YjMpT4e9V5ZUenjSCuuOVa1iocpV2m82y%2FhNEWrS7Zr%2B2L7Q0Xu6AqgrGnclefAMNVzYs9L0ZpG4RfnLBVSAdbOG4Ytmm5csZUDbgKeFUu63bPmyLRcHKrhPtnZ8UiGVj2LSpAKw52GJAiS%2F5V2chnIeuvb5KMh%2BqRqG3cLfpvPvyHPKq3hBFWzBPiJKyVvztqwNUXuB3Vrw%2BMgrMC%2FvQHrjXNNxSQ5tWaQ6iFDg5m8m8tnFk8MQhgLMNu%2FTzQm1NGWi9AltnrKQkYt1q0bW9QYqM24hdYynMCjjDOm%2Fijdbzg4XB62h5z15ZBfWy%2BjF6WJH185qGC25FHsKily%2Fv1qR8SKXo4%2BH2eaEHJVYq1GNUEdHTL95PDU5dWAmHsM%2BE3G2SBoUGdwtkEbDeDtf2T%2BNzjLVxgDy777uqLZLzNVmSgjxulDVwZ0ZtzUQeWCHH7v4lDgu00xkLQO22brTcLQhcBX5%2BmWIFRJGXihx4AYUuSFq6YKHo7DEqnmCxqBW6TCz5cS9BjqkASkatzkGRyuW8DTA%2BxOHyAkqx47osGd9oo6CSKs7y0G6rXy4sSjczQEb9kKpJGbOBTeCGTV7rxxtXMNNc5OJ9Z%2BzgbjuRN%2BvYUS1sZmREIY1Timc2Vpm9xL2kbewPI5B6ghcLOth%2B5E1Yf4ao1%2B3LCq0mm1dkb1nZ2pg2RPg2tvdSSssjGJKvPlyqzzfJRgwLnGol049obF1dDmgnbicjinzdHqB&X-Amz-Signature=c76aced7ee30209f048e849445416fbe258bdcc6a1dc2cf1b41c2c9aca49502a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7CGYWG2%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDUx9%2BQMIGFX3n9pVotofYHN6Bx0XNbetyRSRmCdA0DmwIhAKQBnG5cs0MLb0YZhlcukvXT%2FRqkIQy37FWyqivG983HKv8DCFIQABoMNjM3NDIzMTgzODA1IgwF0NP7XI3WeiGhbs4q3AOYmd7UPApqXOyNg5BPvgH4uV%2Fo8rphHZ8hLms1DVglfdQ7vcsaqRCOFIsIenoJBLaw8Z9Po53bKl93GItX1aJpcRBapzja5byLenxthPRRKeJKAIeaGowcj2c0YjMpT4e9V5ZUenjSCuuOVa1iocpV2m82y%2FhNEWrS7Zr%2B2L7Q0Xu6AqgrGnclefAMNVzYs9L0ZpG4RfnLBVSAdbOG4Ytmm5csZUDbgKeFUu63bPmyLRcHKrhPtnZ8UiGVj2LSpAKw52GJAiS%2F5V2chnIeuvb5KMh%2BqRqG3cLfpvPvyHPKq3hBFWzBPiJKyVvztqwNUXuB3Vrw%2BMgrMC%2FvQHrjXNNxSQ5tWaQ6iFDg5m8m8tnFk8MQhgLMNu%2FTzQm1NGWi9AltnrKQkYt1q0bW9QYqM24hdYynMCjjDOm%2Fijdbzg4XB62h5z15ZBfWy%2BjF6WJH185qGC25FHsKily%2Fv1qR8SKXo4%2BH2eaEHJVYq1GNUEdHTL95PDU5dWAmHsM%2BE3G2SBoUGdwtkEbDeDtf2T%2BNzjLVxgDy777uqLZLzNVmSgjxulDVwZ0ZtzUQeWCHH7v4lDgu00xkLQO22brTcLQhcBX5%2BmWIFRJGXihx4AYUuSFq6YKHo7DEqnmCxqBW6TCz5cS9BjqkASkatzkGRyuW8DTA%2BxOHyAkqx47osGd9oo6CSKs7y0G6rXy4sSjczQEb9kKpJGbOBTeCGTV7rxxtXMNNc5OJ9Z%2BzgbjuRN%2BvYUS1sZmREIY1Timc2Vpm9xL2kbewPI5B6ghcLOth%2B5E1Yf4ao1%2B3LCq0mm1dkb1nZ2pg2RPg2tvdSSssjGJKvPlyqzzfJRgwLnGol049obF1dDmgnbicjinzdHqB&X-Amz-Signature=171e4b066a02897e4018e3648b2334ceae2b911f0b10044eaaaed16d903ce6c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7CGYWG2%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDUx9%2BQMIGFX3n9pVotofYHN6Bx0XNbetyRSRmCdA0DmwIhAKQBnG5cs0MLb0YZhlcukvXT%2FRqkIQy37FWyqivG983HKv8DCFIQABoMNjM3NDIzMTgzODA1IgwF0NP7XI3WeiGhbs4q3AOYmd7UPApqXOyNg5BPvgH4uV%2Fo8rphHZ8hLms1DVglfdQ7vcsaqRCOFIsIenoJBLaw8Z9Po53bKl93GItX1aJpcRBapzja5byLenxthPRRKeJKAIeaGowcj2c0YjMpT4e9V5ZUenjSCuuOVa1iocpV2m82y%2FhNEWrS7Zr%2B2L7Q0Xu6AqgrGnclefAMNVzYs9L0ZpG4RfnLBVSAdbOG4Ytmm5csZUDbgKeFUu63bPmyLRcHKrhPtnZ8UiGVj2LSpAKw52GJAiS%2F5V2chnIeuvb5KMh%2BqRqG3cLfpvPvyHPKq3hBFWzBPiJKyVvztqwNUXuB3Vrw%2BMgrMC%2FvQHrjXNNxSQ5tWaQ6iFDg5m8m8tnFk8MQhgLMNu%2FTzQm1NGWi9AltnrKQkYt1q0bW9QYqM24hdYynMCjjDOm%2Fijdbzg4XB62h5z15ZBfWy%2BjF6WJH185qGC25FHsKily%2Fv1qR8SKXo4%2BH2eaEHJVYq1GNUEdHTL95PDU5dWAmHsM%2BE3G2SBoUGdwtkEbDeDtf2T%2BNzjLVxgDy777uqLZLzNVmSgjxulDVwZ0ZtzUQeWCHH7v4lDgu00xkLQO22brTcLQhcBX5%2BmWIFRJGXihx4AYUuSFq6YKHo7DEqnmCxqBW6TCz5cS9BjqkASkatzkGRyuW8DTA%2BxOHyAkqx47osGd9oo6CSKs7y0G6rXy4sSjczQEb9kKpJGbOBTeCGTV7rxxtXMNNc5OJ9Z%2BzgbjuRN%2BvYUS1sZmREIY1Timc2Vpm9xL2kbewPI5B6ghcLOth%2B5E1Yf4ao1%2B3LCq0mm1dkb1nZ2pg2RPg2tvdSSssjGJKvPlyqzzfJRgwLnGol049obF1dDmgnbicjinzdHqB&X-Amz-Signature=6726792bfcd3cd539239754c3d5c35f90d6f65496cc5d9d7999aa0d1ef71d8b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCRWKKC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICyaJogsqxOMXOp27ekMdj7hHADx9v1cwXY4MAvqdDNwAiB6A8AwsNiWYmt6%2BPGxmdI3iaw1fdlxbPZFsNzV%2BwWb5ir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMr%2BCRyKltF7s1ms1fKtwD3H77M%2B4H79DCN%2BrOIeRndkB6wjKW%2BSLXVuvaKv0Eio1o3mQz8UQA8P9HCfwfm%2B25HeT91x1k1nMyJ73tIa23ckshWKtyxb7pMoxn9zlwS5LyO4x3rRL%2F%2B8Qy7p4K3OQNlJtOS6dLD%2BXtI8UsTQfY8UZ%2FM00hkWxQy%2BkusxJ9Z8tN0XHDuFOoSbVP6s8hi100zi1AEkevV%2FkAFenXU4k1YBMVBv1qQAkLeDEa349via9m6yzyyIy0F5ow13NxrkgU8aMsmtO1u4YPu7BnB%2FA3KG%2Bq7czTu8wrmNNlgletNw39ssw77S9SrFxoJ%2F0e%2FW2aLOztieZKAR%2FvfEpMx5400gQscgqTImG6ZDmDbdyMTMXa7SmBXbrrL0jqjws4kexUjyYlvgJ17PZ2TVxXoXVbt9cCdg78A4VX49vHHu%2Bw5%2FaigknY3iGq9Tfbuw36RnBrN6xAb8zsmHsyJlImq92QUMC4mMqSAgQsqqiynhF46JDzvC3bKPCCizCkRgiZCtwvNi7BLJbStcgp9cN%2FpIP7qJTr0XVjsvGE5OcyhDMXFjquNzNK1xE3gc6g5gPHNuyLJcOBYAAvLv1fpa%2BaNAXlyiZZtiRIieF3SR%2BXzuzKjLBozrRDgkRpnM7vfjEwzuTEvQY6pgFX%2Bwrj19m%2BDsAYfWdso%2Bm9GPvsVA4Sok5TmfGG%2B1yDGIlapMTEqcM4lDwv1tjDJTjf6sDVZKnVo3c%2F%2F75gJnb%2Fd%2Fe4mDKswWgLBAMDeZ%2BSp4pMraAYCa68kQMB1eBz6iFaP4zY4%2F6O4Bn1EA7Z4AarROSWJoaiNNTEsnO8SBg%2BRG3j1THMJp8UJGlGD38BdcCk8eYD0GKkPPsJVY0fzvQ1Wpa6Bjos&X-Amz-Signature=afbe7f26c41fdd8e7cd9c01f08a353110d4f068b7c3f7ede048e4424d921ae8e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCRWKKC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICyaJogsqxOMXOp27ekMdj7hHADx9v1cwXY4MAvqdDNwAiB6A8AwsNiWYmt6%2BPGxmdI3iaw1fdlxbPZFsNzV%2BwWb5ir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMr%2BCRyKltF7s1ms1fKtwD3H77M%2B4H79DCN%2BrOIeRndkB6wjKW%2BSLXVuvaKv0Eio1o3mQz8UQA8P9HCfwfm%2B25HeT91x1k1nMyJ73tIa23ckshWKtyxb7pMoxn9zlwS5LyO4x3rRL%2F%2B8Qy7p4K3OQNlJtOS6dLD%2BXtI8UsTQfY8UZ%2FM00hkWxQy%2BkusxJ9Z8tN0XHDuFOoSbVP6s8hi100zi1AEkevV%2FkAFenXU4k1YBMVBv1qQAkLeDEa349via9m6yzyyIy0F5ow13NxrkgU8aMsmtO1u4YPu7BnB%2FA3KG%2Bq7czTu8wrmNNlgletNw39ssw77S9SrFxoJ%2F0e%2FW2aLOztieZKAR%2FvfEpMx5400gQscgqTImG6ZDmDbdyMTMXa7SmBXbrrL0jqjws4kexUjyYlvgJ17PZ2TVxXoXVbt9cCdg78A4VX49vHHu%2Bw5%2FaigknY3iGq9Tfbuw36RnBrN6xAb8zsmHsyJlImq92QUMC4mMqSAgQsqqiynhF46JDzvC3bKPCCizCkRgiZCtwvNi7BLJbStcgp9cN%2FpIP7qJTr0XVjsvGE5OcyhDMXFjquNzNK1xE3gc6g5gPHNuyLJcOBYAAvLv1fpa%2BaNAXlyiZZtiRIieF3SR%2BXzuzKjLBozrRDgkRpnM7vfjEwzuTEvQY6pgFX%2Bwrj19m%2BDsAYfWdso%2Bm9GPvsVA4Sok5TmfGG%2B1yDGIlapMTEqcM4lDwv1tjDJTjf6sDVZKnVo3c%2F%2F75gJnb%2Fd%2Fe4mDKswWgLBAMDeZ%2BSp4pMraAYCa68kQMB1eBz6iFaP4zY4%2F6O4Bn1EA7Z4AarROSWJoaiNNTEsnO8SBg%2BRG3j1THMJp8UJGlGD38BdcCk8eYD0GKkPPsJVY0fzvQ1Wpa6Bjos&X-Amz-Signature=2de5a7b4d98d9337a354a8ac48b97d058bbcd3e254fe31e06412b4dd28956d4c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCRWKKC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICyaJogsqxOMXOp27ekMdj7hHADx9v1cwXY4MAvqdDNwAiB6A8AwsNiWYmt6%2BPGxmdI3iaw1fdlxbPZFsNzV%2BwWb5ir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMr%2BCRyKltF7s1ms1fKtwD3H77M%2B4H79DCN%2BrOIeRndkB6wjKW%2BSLXVuvaKv0Eio1o3mQz8UQA8P9HCfwfm%2B25HeT91x1k1nMyJ73tIa23ckshWKtyxb7pMoxn9zlwS5LyO4x3rRL%2F%2B8Qy7p4K3OQNlJtOS6dLD%2BXtI8UsTQfY8UZ%2FM00hkWxQy%2BkusxJ9Z8tN0XHDuFOoSbVP6s8hi100zi1AEkevV%2FkAFenXU4k1YBMVBv1qQAkLeDEa349via9m6yzyyIy0F5ow13NxrkgU8aMsmtO1u4YPu7BnB%2FA3KG%2Bq7czTu8wrmNNlgletNw39ssw77S9SrFxoJ%2F0e%2FW2aLOztieZKAR%2FvfEpMx5400gQscgqTImG6ZDmDbdyMTMXa7SmBXbrrL0jqjws4kexUjyYlvgJ17PZ2TVxXoXVbt9cCdg78A4VX49vHHu%2Bw5%2FaigknY3iGq9Tfbuw36RnBrN6xAb8zsmHsyJlImq92QUMC4mMqSAgQsqqiynhF46JDzvC3bKPCCizCkRgiZCtwvNi7BLJbStcgp9cN%2FpIP7qJTr0XVjsvGE5OcyhDMXFjquNzNK1xE3gc6g5gPHNuyLJcOBYAAvLv1fpa%2BaNAXlyiZZtiRIieF3SR%2BXzuzKjLBozrRDgkRpnM7vfjEwzuTEvQY6pgFX%2Bwrj19m%2BDsAYfWdso%2Bm9GPvsVA4Sok5TmfGG%2B1yDGIlapMTEqcM4lDwv1tjDJTjf6sDVZKnVo3c%2F%2F75gJnb%2Fd%2Fe4mDKswWgLBAMDeZ%2BSp4pMraAYCa68kQMB1eBz6iFaP4zY4%2F6O4Bn1EA7Z4AarROSWJoaiNNTEsnO8SBg%2BRG3j1THMJp8UJGlGD38BdcCk8eYD0GKkPPsJVY0fzvQ1Wpa6Bjos&X-Amz-Signature=db5022dd7cff8b49f8d0d1e677d1ac0c36517706959909f45cbb1ee5beb78671&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCRWKKC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICyaJogsqxOMXOp27ekMdj7hHADx9v1cwXY4MAvqdDNwAiB6A8AwsNiWYmt6%2BPGxmdI3iaw1fdlxbPZFsNzV%2BwWb5ir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMr%2BCRyKltF7s1ms1fKtwD3H77M%2B4H79DCN%2BrOIeRndkB6wjKW%2BSLXVuvaKv0Eio1o3mQz8UQA8P9HCfwfm%2B25HeT91x1k1nMyJ73tIa23ckshWKtyxb7pMoxn9zlwS5LyO4x3rRL%2F%2B8Qy7p4K3OQNlJtOS6dLD%2BXtI8UsTQfY8UZ%2FM00hkWxQy%2BkusxJ9Z8tN0XHDuFOoSbVP6s8hi100zi1AEkevV%2FkAFenXU4k1YBMVBv1qQAkLeDEa349via9m6yzyyIy0F5ow13NxrkgU8aMsmtO1u4YPu7BnB%2FA3KG%2Bq7czTu8wrmNNlgletNw39ssw77S9SrFxoJ%2F0e%2FW2aLOztieZKAR%2FvfEpMx5400gQscgqTImG6ZDmDbdyMTMXa7SmBXbrrL0jqjws4kexUjyYlvgJ17PZ2TVxXoXVbt9cCdg78A4VX49vHHu%2Bw5%2FaigknY3iGq9Tfbuw36RnBrN6xAb8zsmHsyJlImq92QUMC4mMqSAgQsqqiynhF46JDzvC3bKPCCizCkRgiZCtwvNi7BLJbStcgp9cN%2FpIP7qJTr0XVjsvGE5OcyhDMXFjquNzNK1xE3gc6g5gPHNuyLJcOBYAAvLv1fpa%2BaNAXlyiZZtiRIieF3SR%2BXzuzKjLBozrRDgkRpnM7vfjEwzuTEvQY6pgFX%2Bwrj19m%2BDsAYfWdso%2Bm9GPvsVA4Sok5TmfGG%2B1yDGIlapMTEqcM4lDwv1tjDJTjf6sDVZKnVo3c%2F%2F75gJnb%2Fd%2Fe4mDKswWgLBAMDeZ%2BSp4pMraAYCa68kQMB1eBz6iFaP4zY4%2F6O4Bn1EA7Z4AarROSWJoaiNNTEsnO8SBg%2BRG3j1THMJp8UJGlGD38BdcCk8eYD0GKkPPsJVY0fzvQ1Wpa6Bjos&X-Amz-Signature=5d10a03808e7513e6cac81c9f98f8d2b4af1c61cc884fae2b41ac35794ef74dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCRWKKC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICyaJogsqxOMXOp27ekMdj7hHADx9v1cwXY4MAvqdDNwAiB6A8AwsNiWYmt6%2BPGxmdI3iaw1fdlxbPZFsNzV%2BwWb5ir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMr%2BCRyKltF7s1ms1fKtwD3H77M%2B4H79DCN%2BrOIeRndkB6wjKW%2BSLXVuvaKv0Eio1o3mQz8UQA8P9HCfwfm%2B25HeT91x1k1nMyJ73tIa23ckshWKtyxb7pMoxn9zlwS5LyO4x3rRL%2F%2B8Qy7p4K3OQNlJtOS6dLD%2BXtI8UsTQfY8UZ%2FM00hkWxQy%2BkusxJ9Z8tN0XHDuFOoSbVP6s8hi100zi1AEkevV%2FkAFenXU4k1YBMVBv1qQAkLeDEa349via9m6yzyyIy0F5ow13NxrkgU8aMsmtO1u4YPu7BnB%2FA3KG%2Bq7czTu8wrmNNlgletNw39ssw77S9SrFxoJ%2F0e%2FW2aLOztieZKAR%2FvfEpMx5400gQscgqTImG6ZDmDbdyMTMXa7SmBXbrrL0jqjws4kexUjyYlvgJ17PZ2TVxXoXVbt9cCdg78A4VX49vHHu%2Bw5%2FaigknY3iGq9Tfbuw36RnBrN6xAb8zsmHsyJlImq92QUMC4mMqSAgQsqqiynhF46JDzvC3bKPCCizCkRgiZCtwvNi7BLJbStcgp9cN%2FpIP7qJTr0XVjsvGE5OcyhDMXFjquNzNK1xE3gc6g5gPHNuyLJcOBYAAvLv1fpa%2BaNAXlyiZZtiRIieF3SR%2BXzuzKjLBozrRDgkRpnM7vfjEwzuTEvQY6pgFX%2Bwrj19m%2BDsAYfWdso%2Bm9GPvsVA4Sok5TmfGG%2B1yDGIlapMTEqcM4lDwv1tjDJTjf6sDVZKnVo3c%2F%2F75gJnb%2Fd%2Fe4mDKswWgLBAMDeZ%2BSp4pMraAYCa68kQMB1eBz6iFaP4zY4%2F6O4Bn1EA7Z4AarROSWJoaiNNTEsnO8SBg%2BRG3j1THMJp8UJGlGD38BdcCk8eYD0GKkPPsJVY0fzvQ1Wpa6Bjos&X-Amz-Signature=8f7486d93cea5126f98686e6108ca52852e9e57366e8b607b7f50097ecebc494&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCRWKKC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICyaJogsqxOMXOp27ekMdj7hHADx9v1cwXY4MAvqdDNwAiB6A8AwsNiWYmt6%2BPGxmdI3iaw1fdlxbPZFsNzV%2BwWb5ir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMr%2BCRyKltF7s1ms1fKtwD3H77M%2B4H79DCN%2BrOIeRndkB6wjKW%2BSLXVuvaKv0Eio1o3mQz8UQA8P9HCfwfm%2B25HeT91x1k1nMyJ73tIa23ckshWKtyxb7pMoxn9zlwS5LyO4x3rRL%2F%2B8Qy7p4K3OQNlJtOS6dLD%2BXtI8UsTQfY8UZ%2FM00hkWxQy%2BkusxJ9Z8tN0XHDuFOoSbVP6s8hi100zi1AEkevV%2FkAFenXU4k1YBMVBv1qQAkLeDEa349via9m6yzyyIy0F5ow13NxrkgU8aMsmtO1u4YPu7BnB%2FA3KG%2Bq7czTu8wrmNNlgletNw39ssw77S9SrFxoJ%2F0e%2FW2aLOztieZKAR%2FvfEpMx5400gQscgqTImG6ZDmDbdyMTMXa7SmBXbrrL0jqjws4kexUjyYlvgJ17PZ2TVxXoXVbt9cCdg78A4VX49vHHu%2Bw5%2FaigknY3iGq9Tfbuw36RnBrN6xAb8zsmHsyJlImq92QUMC4mMqSAgQsqqiynhF46JDzvC3bKPCCizCkRgiZCtwvNi7BLJbStcgp9cN%2FpIP7qJTr0XVjsvGE5OcyhDMXFjquNzNK1xE3gc6g5gPHNuyLJcOBYAAvLv1fpa%2BaNAXlyiZZtiRIieF3SR%2BXzuzKjLBozrRDgkRpnM7vfjEwzuTEvQY6pgFX%2Bwrj19m%2BDsAYfWdso%2Bm9GPvsVA4Sok5TmfGG%2B1yDGIlapMTEqcM4lDwv1tjDJTjf6sDVZKnVo3c%2F%2F75gJnb%2Fd%2Fe4mDKswWgLBAMDeZ%2BSp4pMraAYCa68kQMB1eBz6iFaP4zY4%2F6O4Bn1EA7Z4AarROSWJoaiNNTEsnO8SBg%2BRG3j1THMJp8UJGlGD38BdcCk8eYD0GKkPPsJVY0fzvQ1Wpa6Bjos&X-Amz-Signature=003b5ca2b01e8a905edc29175e97e89d6338b48a5a9ad74057cb783ee542bae5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBKI7XRE%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCQgRhtiqKvTyh26c2GGmtZlouqDPLs4sdUH2XhFdHX5wIhAOwy2YoxeTxXuEEG9ODRnC%2B4ZL6AoczejmF2bRuaH1ORKv8DCFIQABoMNjM3NDIzMTgzODA1IgwHrVl48isgWn3Jph8q3AOwBY8GGyMGa%2FNlSKKYrrC%2F1F1WRqtHCeFVk1kAPh%2BDRAing%2BzRN7ym1bZJd%2BpeCR%2BNIV0rjwuo4LMBEP4BsVF8LeK7Z2v8142Qg0wIRMQRWiyeTRzfjWJtQ%2BAoLMSXeNZY7Tcbt4kgpN0zP6IGH1tCNzVIC6JuGoZ6bp1VMhpy%2BbbVz0rGgrzgrdS%2BumfdKoNYyL6BGYyrGP5odVJK7O%2B0E25o5mbCmOwf3XAXD9e247puSz2kRrZ5uRY%2FCMBJ%2Ft6IWnX%2FQMoVKPnOyJdsDTLDq5ky%2B4Kd3Pr2Wx9cbLov1MdSC%2BqpBhRGoGLCk%2FGkmyEiLUHAjy1ohDW94xOLs6Ji55Jom1VhqKR1i%2BZ0MNODKc%2FfIX27auYSc0FaavkoSo%2FPtu%2FMvacrTCPLLsdcsYc7fVTpuNJlH5k%2F00eXx%2BlHl1QoqrDEAFZ6SShvQSrtLvQZnzBUPWA0%2FD1ji98m26wgy0%2FA5dFII%2FeEmMa6Ku5c74KDSAJx6P6LDlfuiPjraGhZgtb8uUnkoVJLSt7%2BkAhjA6dlI89f9hspLlyLxtYurCVtVl%2FrySYqivWNnwWgLGWBD52nCMJgvPbMFjmx976q0jdY8o56C8RvPr8SUUUjHCM8kunHg%2BLX2dUagzDS5cS9BjqkAZh14IFllwJ1O6YPyQNS6yackmgVsVP%2FNEmh7J1DMh1BNjCxNCarhcvQ7z%2BqK77daI%2F5Y8GWiWbYJ8MN3QWeVgiNVi7fPVbVWAXfnAVK95SgmoALv0TLDN20HoxymvCE%2BytczDXqgkRpYLda0cVuLFqs%2BA9s5bRpZ%2FOAHpRLKzjpzBgNv5wKjUOtWSatM2zJO7yGVHKmVmpWgipk3IxkAN18QmIa&X-Amz-Signature=257f97d4705f3a6cb69ee360f48b93b6c86c49b7753c6e32820be5a600477a9f&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JYFLC3C%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDdNqaFTpbVaLjyMs%2FaHY66h7BVlz8mW4n2t1CwzSr38AIgDlMgq4tCs9VLdjIvA%2FVP6%2BSUbou%2BRJOclLdm67NQXGUq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDKHasA9CHLMJkMONOyrcA4zmdb6l%2BUKqCwUVz09gc%2FP%2Bxws84SBAT%2F5yCVPKbj6LV3QC1FaXuVvfThC0GtZ6uSaIBebP40FvvJc40956YW3ha%2ByDTjoa1v3tP%2FTynSyr44PvheUPIgvrPtCx%2FWLrYd3nku7NG2NlNL3qKnKn6Y99mWdnafO0h6Gj0zYiSWJ38bBHU%2BaoIyicJb9MKP9exosuanAJ75vJ6FUI%2FDVExExyNEBvInOWu1Ztx3l9IgM5c8wEwcBG0Mims4UZT2E4R%2Br%2BsqLuueuc%2BgV35diJkPZ5aOmutejU2YOfj0XitLNgSpVtn5isg9fIbjz1McqKj5NXsL6GaLd3MldzYZenmeSgUAg6TAA%2FcfniIHte%2B04366JFrqt7VlWi4CCh%2FClu1tsXm3sXctzeOlNUxrgp3TuV0CGPm5eaLDXV5vtiGResIoWC8g0GPbyv2Jzm%2BwxnV1qt8UgNhVA9mJBChoDa4Rhf0ilnaabBWxeVEWcgrq0v89YO7msjGs7SchgbmVNXiU4VtgYaKeyjvkUk7AXBuTT5uSo4TieFdzKkuoJxsxCL3ga8m0UiXPIxAL4SMfDY391MJPbnaq5AGoICSBV1WmMOsx7NEdTZDOLzx5TmT%2F0jG44tEHF%2F0vtOlbWDMMzkxL0GOqUB6pLHUtWwOwst%2Fofo0vaZRmQ%2BK%2FK6F6rVJWdRbKRVuubDhizyb821nIlrQ4i5896L4JVxLObzzwUBaassPwrM53v1%2FF1bJbh8Jg1v0a1d5%2FKkCr5xDzFey9iVePreWbpCwp2ClQREnBJJRuLqLvkYc4jLbQmGnu5xbVkpmlB1IfCh0ofHpN4fyn%2FZRWPcHnj85vNFjYcRtKNHM6KEUoJmWO7oA5P5&X-Amz-Signature=95857f269e3f16da50655e416c9d38147a55670ef894c864b030a685a78e4a3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCRWKKC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICyaJogsqxOMXOp27ekMdj7hHADx9v1cwXY4MAvqdDNwAiB6A8AwsNiWYmt6%2BPGxmdI3iaw1fdlxbPZFsNzV%2BwWb5ir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMr%2BCRyKltF7s1ms1fKtwD3H77M%2B4H79DCN%2BrOIeRndkB6wjKW%2BSLXVuvaKv0Eio1o3mQz8UQA8P9HCfwfm%2B25HeT91x1k1nMyJ73tIa23ckshWKtyxb7pMoxn9zlwS5LyO4x3rRL%2F%2B8Qy7p4K3OQNlJtOS6dLD%2BXtI8UsTQfY8UZ%2FM00hkWxQy%2BkusxJ9Z8tN0XHDuFOoSbVP6s8hi100zi1AEkevV%2FkAFenXU4k1YBMVBv1qQAkLeDEa349via9m6yzyyIy0F5ow13NxrkgU8aMsmtO1u4YPu7BnB%2FA3KG%2Bq7czTu8wrmNNlgletNw39ssw77S9SrFxoJ%2F0e%2FW2aLOztieZKAR%2FvfEpMx5400gQscgqTImG6ZDmDbdyMTMXa7SmBXbrrL0jqjws4kexUjyYlvgJ17PZ2TVxXoXVbt9cCdg78A4VX49vHHu%2Bw5%2FaigknY3iGq9Tfbuw36RnBrN6xAb8zsmHsyJlImq92QUMC4mMqSAgQsqqiynhF46JDzvC3bKPCCizCkRgiZCtwvNi7BLJbStcgp9cN%2FpIP7qJTr0XVjsvGE5OcyhDMXFjquNzNK1xE3gc6g5gPHNuyLJcOBYAAvLv1fpa%2BaNAXlyiZZtiRIieF3SR%2BXzuzKjLBozrRDgkRpnM7vfjEwzuTEvQY6pgFX%2Bwrj19m%2BDsAYfWdso%2Bm9GPvsVA4Sok5TmfGG%2B1yDGIlapMTEqcM4lDwv1tjDJTjf6sDVZKnVo3c%2F%2F75gJnb%2Fd%2Fe4mDKswWgLBAMDeZ%2BSp4pMraAYCa68kQMB1eBz6iFaP4zY4%2F6O4Bn1EA7Z4AarROSWJoaiNNTEsnO8SBg%2BRG3j1THMJp8UJGlGD38BdcCk8eYD0GKkPPsJVY0fzvQ1Wpa6Bjos&X-Amz-Signature=b58f2ded5bdadcf1efe70056ac8cd2fc0d040ee35d588dfb297a8c460b060e9f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCRWKKC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICyaJogsqxOMXOp27ekMdj7hHADx9v1cwXY4MAvqdDNwAiB6A8AwsNiWYmt6%2BPGxmdI3iaw1fdlxbPZFsNzV%2BwWb5ir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMr%2BCRyKltF7s1ms1fKtwD3H77M%2B4H79DCN%2BrOIeRndkB6wjKW%2BSLXVuvaKv0Eio1o3mQz8UQA8P9HCfwfm%2B25HeT91x1k1nMyJ73tIa23ckshWKtyxb7pMoxn9zlwS5LyO4x3rRL%2F%2B8Qy7p4K3OQNlJtOS6dLD%2BXtI8UsTQfY8UZ%2FM00hkWxQy%2BkusxJ9Z8tN0XHDuFOoSbVP6s8hi100zi1AEkevV%2FkAFenXU4k1YBMVBv1qQAkLeDEa349via9m6yzyyIy0F5ow13NxrkgU8aMsmtO1u4YPu7BnB%2FA3KG%2Bq7czTu8wrmNNlgletNw39ssw77S9SrFxoJ%2F0e%2FW2aLOztieZKAR%2FvfEpMx5400gQscgqTImG6ZDmDbdyMTMXa7SmBXbrrL0jqjws4kexUjyYlvgJ17PZ2TVxXoXVbt9cCdg78A4VX49vHHu%2Bw5%2FaigknY3iGq9Tfbuw36RnBrN6xAb8zsmHsyJlImq92QUMC4mMqSAgQsqqiynhF46JDzvC3bKPCCizCkRgiZCtwvNi7BLJbStcgp9cN%2FpIP7qJTr0XVjsvGE5OcyhDMXFjquNzNK1xE3gc6g5gPHNuyLJcOBYAAvLv1fpa%2BaNAXlyiZZtiRIieF3SR%2BXzuzKjLBozrRDgkRpnM7vfjEwzuTEvQY6pgFX%2Bwrj19m%2BDsAYfWdso%2Bm9GPvsVA4Sok5TmfGG%2B1yDGIlapMTEqcM4lDwv1tjDJTjf6sDVZKnVo3c%2F%2F75gJnb%2Fd%2Fe4mDKswWgLBAMDeZ%2BSp4pMraAYCa68kQMB1eBz6iFaP4zY4%2F6O4Bn1EA7Z4AarROSWJoaiNNTEsnO8SBg%2BRG3j1THMJp8UJGlGD38BdcCk8eYD0GKkPPsJVY0fzvQ1Wpa6Bjos&X-Amz-Signature=fffce4b899918be30e7d23b0809ae5a92dadd525448ef7c5ac66a3c031c483f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWCRWKKC%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCICyaJogsqxOMXOp27ekMdj7hHADx9v1cwXY4MAvqdDNwAiB6A8AwsNiWYmt6%2BPGxmdI3iaw1fdlxbPZFsNzV%2BwWb5ir%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMr%2BCRyKltF7s1ms1fKtwD3H77M%2B4H79DCN%2BrOIeRndkB6wjKW%2BSLXVuvaKv0Eio1o3mQz8UQA8P9HCfwfm%2B25HeT91x1k1nMyJ73tIa23ckshWKtyxb7pMoxn9zlwS5LyO4x3rRL%2F%2B8Qy7p4K3OQNlJtOS6dLD%2BXtI8UsTQfY8UZ%2FM00hkWxQy%2BkusxJ9Z8tN0XHDuFOoSbVP6s8hi100zi1AEkevV%2FkAFenXU4k1YBMVBv1qQAkLeDEa349via9m6yzyyIy0F5ow13NxrkgU8aMsmtO1u4YPu7BnB%2FA3KG%2Bq7czTu8wrmNNlgletNw39ssw77S9SrFxoJ%2F0e%2FW2aLOztieZKAR%2FvfEpMx5400gQscgqTImG6ZDmDbdyMTMXa7SmBXbrrL0jqjws4kexUjyYlvgJ17PZ2TVxXoXVbt9cCdg78A4VX49vHHu%2Bw5%2FaigknY3iGq9Tfbuw36RnBrN6xAb8zsmHsyJlImq92QUMC4mMqSAgQsqqiynhF46JDzvC3bKPCCizCkRgiZCtwvNi7BLJbStcgp9cN%2FpIP7qJTr0XVjsvGE5OcyhDMXFjquNzNK1xE3gc6g5gPHNuyLJcOBYAAvLv1fpa%2BaNAXlyiZZtiRIieF3SR%2BXzuzKjLBozrRDgkRpnM7vfjEwzuTEvQY6pgFX%2Bwrj19m%2BDsAYfWdso%2Bm9GPvsVA4Sok5TmfGG%2B1yDGIlapMTEqcM4lDwv1tjDJTjf6sDVZKnVo3c%2F%2F75gJnb%2Fd%2Fe4mDKswWgLBAMDeZ%2BSp4pMraAYCa68kQMB1eBz6iFaP4zY4%2F6O4Bn1EA7Z4AarROSWJoaiNNTEsnO8SBg%2BRG3j1THMJp8UJGlGD38BdcCk8eYD0GKkPPsJVY0fzvQ1Wpa6Bjos&X-Amz-Signature=88ff94bcd2b770a0fd69a2453a49e07e78a3d058f83051a404879f3687bc4df2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRY2NGH4%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQD0Au2RUsoqI7s1fC6FLZvjvEntb9akkOOb4t8hVlJt8wIgSBYptc53mcmwxROl9nvDcmgc%2FwQ89EoGbe%2F7W%2Bll7kMq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDNBjdtN35iZjnol8YircA0cpYHXVxj6%2FEv2R261w1Hp9Ve%2FdC%2BwPU7wmA7083fFXi4dmXfEI6zd%2BGXWTYUglOujl25TKTrvygOq7jA%2F%2B2YSrF6EmUKpMttVb1v8cqgVq0QUykONsClCF9gSbaQ7XK9N3EaqCrrdMUhIzM1QdVXA%2BvHMV6pDmmBMSgcJcCHT0XruZ47XXYarV8XS1E1aZ2EepjQExm7%2BLZdLTV5AFPDkwwZHpMz%2FlWk918f7unwd47t0D7cMwmT3QOy3xl32hfpdYip8u6F27vxOMKBWnUW%2FIDLZ5zqCpBmPWaAoy%2BdIApASe60jgw7wybM5TaSL%2FsW8Usgjd40vG4zZkt%2Fuwlg1wmt3wdhFpALXYwQISw%2F6AneDY%2BWQZQ%2BdUV6AIX89L3lcKDY5sii%2B2gYLxU%2B9IRNjl14EEMK7Uz1zLiT12VyDkwFCHlaYyBZTNIKWW8uhxU8o3iyResZT%2FJVYWPUBXEfUlZMMq8QCxS%2FlbBgJ%2B%2B6wEcbTVjllYydBhWwnem1uTNdnndWEKZPbmr977FtWFK5p0mqOEbX3PgrugkSIYmon5IRQ8BtLIcUpfaS15hAlsswziTZUA5WEU1%2FroyXY0%2BKQ7zZkgXK6Q6CwWkW1soXFF86jYSy1jzuq6ck96MOnkxL0GOqUB%2B93EatnQqk51ICKo9R8p%2BOkk6Ta6AJkdqckWqzo6Yw8pbEr3k%2FgIfyHtDD1SSFb%2FBF9cNR8y690OTMp%2BHmSgDU04FrnxC4pSa82AHQKV1NnPyNx45AexwqpHEMxIFvVbKz2EpIksDf7s4MkfFUbio2ig1UfgmKgrb4xrsy4epNJrIbo4jNKBPL47%2Fjfu3RlpzIi0PdaOkMfP%2FWIhGb9deje6VI1o&X-Amz-Signature=5664f1c73667bde1b9e4c129b6807e330345ca3b50f19a8c9ede6d6b1706c3b9&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663E7OGMRM%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDTWQLzCUGIJsr%2BfAJkXhLpr3djbUo6N5BmQZzZD4HqawIgWyXcEhakbg62U6aeVD8A%2BhTRxwPvKv1HDQoPJifcqXwq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDLWdL7jEezlinoBKJyrcAyXshJjXbCXU9xOh8SUxE1ldHHh1OaL70PJ%2BxX2y3PtuWXZgkE8TFBRC0Uysuo%2F4repqJRW0yRfHqVgnXiWSWM%2FRRAM%2FlHNNCDhLoGw8MiOUcYUnRmqmavf6iaAJPUeB7y2TBC8m7p1TCSjtHu7CPZfWV9qZRkzISRsV0RVFPbeBfepAYn890VMGspkU%2BnpPVGw8BbI4Irkk85i%2FpF5TVWdtXZdXSGSD3dDIJH1B0eW2IZbR14v9918I8vL%2BC5J5P9CcRoi1z9vdzmRiVanft0%2BKFyzu32%2F1xjAXt0jna5rQkv%2F3VScDKRpWV5Uurk0pDoMLsXRdu%2Ble9VOBQlpAMNUUBWO9TGWkveQsW0oUP4IJz502%2BuxNYAIc1FnAb2NWMgyx1Tf9AQktzVnQrrl0jbToo4Wq3jPXjEMZhebOZuhLlgzaFaeSZu1w9jCPzgZrkYxsbBVRFsrrI%2BnfIW0jrj%2BBFQ04QICL%2BPQC4Gqmu7elkN%2Fg4CgqMl7Lf8RXC7ELJLdJgnsxWNdgMufxoFNZwTuO%2FyiWG68MnUXG%2FyTTCc9OwMT2Qbmt8ftO%2FBIbo0oa8EFE9u4I603%2F9hr1L8aEkPzgagU0kfUQ%2BcWoj1eqJvA4VHJoQH%2BTQSRpbcaiMPTlxL0GOqUBTUFuhDSV17CTZOYhKoG439aM6KqZsKDzZFxG3Xo8GD7JETH3qpzvg3V3lUNQInj3Byv0NnhtJFlpm9gvKcQf2Vlsb3JxX97E22WMIrlUTYXkUvfC63FH3dubwKfjD4HcjQ5fdmH1L4QSnweLkbkOBJSyn%2FA2Jvv1SmBS84c%2B2u8t9%2FKDi2n4huXuL3HJUymlr51FygGW4okO%2FTEMaMjXD1o9SLFs&X-Amz-Signature=20b4d12c280acb9977fb976e4076fbc913a493486407dbdd78904ddc3e707e0f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOMBO6EZ%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCAlu0JuI4SmWCO9iHH%2Fd7E9Llhpllsm4CJsUlohC70JgIhAJFxTGlAPHMfnUewzwwIaYhWY37nF66c85lN5zt0oVjRKv8DCFIQABoMNjM3NDIzMTgzODA1IgwgaGjHMhLc90WqZucq3AOfgzcwvZlrosSjyI48JZbGTsr7IZlXpXujTC4wlETkzQkYrfpTyfRJ8VIqo1FPzhuXOjoGDOODPrDanPZSciLw6CXQgjPcfQ0rmBaSJAg8n7eyRpDJWHwtmTUtA54ql0hNJZk7mLYhNGLbedU9M%2Ft8AOVFr%2FuAlTifcXPdd8PiSdWNksK6YQWAnauAGpE67rLdO2TozT9cZYZAX%2FE2sKZI0d5xZ1vJsG7CWBcBvF8lcDO9k208fuzDnRDgnXN4s77ioUjCUDvnSd5uDrCN%2BFLPSJJeGMbv9oSzSzJ7LxiUTtBBfYW4r983gBYBw2W%2B33H9ENNmhTblMoFs5iWI45iO4ec2WFUyGoHQLu4raizZaxnKLUtzEWO%2B%2BnvFzt3xl6xPaMGcvIsEuStxch%2F5SwTk845wouLenWPn%2BCSXdhe3NCyM%2BTYuO2bz%2Bx5X9lVN%2BgKyBYdJE6ZMa8zzRtYi6IAQtIghOQpiTNAaE1KT43JVL2KgUa4mVW0hLUDOr0BracylM9v4Gs5wmHpJXILC41%2FURDTpbECwCM%2FycDtt2ME03e88MKx2%2FuS6ID%2Bjg%2BC4mnnp6L8artsiQf6Xa6c2Q4yJ2cAigr6x9lSCZW7aEk3XpIvDpe2jVhPpyB6JlzD65MS9BjqkAZn9Kf1z14vulj9LWE91Y%2BpL8ItTEfyZNn8hskNF5hKIEC8iUFqtIqqL%2FP92IV%2FkzToI4zXJXAUARWri7bU9fQ7iSuriYS0ADAF5ha%2F1RBNPCILgR7bRgYnSgZLpGGPwqEat2H3OJsnJbQqZsM%2Bqa208mtI3B97UO2jMi0KcyV2Ywqns0Lun3K5HsZuSPxy%2Fj9l2bAF8asISTH%2FIJSLyvHotL3kP&X-Amz-Signature=79b9d8a410d6b4c1123c75ac5cefbcdf44252ebb93daaa29c3e00f8a48d7e0f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652O3WF5K%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDOucN2JsLJpeykV73%2F%2BvYiM7Eou4cGiSNXjQw5%2FPpbzQIgMacJJE3zYZBudB9YX4FurFPe9gPlg5Pr0iBa9tbmE9kq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDLWcaPcw03ckwURQ1CrcA5n8OqXilD%2FKowcFN7i9rm8hve7FOilqGjt5B%2FMuIiRpTCjj18de3BJMbzeSxAR9uBfmjoiTc1DTBF6pHR5y%2F9H3%2BobCbxn1V9aHL%2FTXJDteCdlV8fvccMpN0PpSFHn%2B9LBdl0ldR8SIOdZh598uhTXCrji5UnrdoC%2B0MHjwxQMFV7ZPZpwx8JsuyKrzfaE%2FdJeyhOiy4%2Bk94Zq%2B%2FsQzm7Z6vZpmfYyQxfLhd1C4f5NuFtVfhzwLNi4zJHYgr2i3bE%2Fu2t91jI3t5bJQYq4S286UqTqyQBWjUWojLnegbzoKhwsm5ZKkb097n5JWb25wDK2p829lQGiVn0phBLtUpZfMCPGlqHPzMT561DKLwTV%2BXW7gsyAo05DxTEOTHzmD8jUCxzDSKET2tsWOGKFLpfYziCv8rjj32O%2Bkc0iP6DKvc2gM3BWPRb1n97YRXXVCkvEhz9VWei08UgDty8mCfNKjLPk5SoAUASeO6PwOxXD%2BafBYsiIuyuo12hh9OCz8zkjrRlzdSBb2yd0pAGt%2FqdNeOpYpvLFU6EW3WrDPz5WVwH2Nvl1tbFzJiFqRL%2FK6Mh7XAHsrtXEcbTnAr5wp0MK0dWNAzR%2B2xTOTD2mQeeZb8r9E%2F4%2BMp%2FU45EsjMO%2FkxL0GOqUBoO%2FCpZU2qQQ5Wff%2FoN1Y5JO03zq7iy%2BEBOMbGQLzykgZHDUKosSjBp6guj5mobxti8Cbh6%2BgWmiWSrwPZDg8OF0tFyRxjsguXbkWV4LbN%2FzJqn2J2jo78j%2FDzZCGLVbwPf9T7uSKaNf0NHc63JNpWSLuzGt8qjU145OMJrOezvk7oiHH%2BE5UxiJN7wLin5qe7hV4PVEKR5ghFjLWW59aEzU2zgPy&X-Amz-Signature=cac936be797ee5c049fbb466bc95bdf4cc2d60f685b89277f9e3096260ddbe96&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652O3WF5K%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDOucN2JsLJpeykV73%2F%2BvYiM7Eou4cGiSNXjQw5%2FPpbzQIgMacJJE3zYZBudB9YX4FurFPe9gPlg5Pr0iBa9tbmE9kq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDLWcaPcw03ckwURQ1CrcA5n8OqXilD%2FKowcFN7i9rm8hve7FOilqGjt5B%2FMuIiRpTCjj18de3BJMbzeSxAR9uBfmjoiTc1DTBF6pHR5y%2F9H3%2BobCbxn1V9aHL%2FTXJDteCdlV8fvccMpN0PpSFHn%2B9LBdl0ldR8SIOdZh598uhTXCrji5UnrdoC%2B0MHjwxQMFV7ZPZpwx8JsuyKrzfaE%2FdJeyhOiy4%2Bk94Zq%2B%2FsQzm7Z6vZpmfYyQxfLhd1C4f5NuFtVfhzwLNi4zJHYgr2i3bE%2Fu2t91jI3t5bJQYq4S286UqTqyQBWjUWojLnegbzoKhwsm5ZKkb097n5JWb25wDK2p829lQGiVn0phBLtUpZfMCPGlqHPzMT561DKLwTV%2BXW7gsyAo05DxTEOTHzmD8jUCxzDSKET2tsWOGKFLpfYziCv8rjj32O%2Bkc0iP6DKvc2gM3BWPRb1n97YRXXVCkvEhz9VWei08UgDty8mCfNKjLPk5SoAUASeO6PwOxXD%2BafBYsiIuyuo12hh9OCz8zkjrRlzdSBb2yd0pAGt%2FqdNeOpYpvLFU6EW3WrDPz5WVwH2Nvl1tbFzJiFqRL%2FK6Mh7XAHsrtXEcbTnAr5wp0MK0dWNAzR%2B2xTOTD2mQeeZb8r9E%2F4%2BMp%2FU45EsjMO%2FkxL0GOqUBoO%2FCpZU2qQQ5Wff%2FoN1Y5JO03zq7iy%2BEBOMbGQLzykgZHDUKosSjBp6guj5mobxti8Cbh6%2BgWmiWSrwPZDg8OF0tFyRxjsguXbkWV4LbN%2FzJqn2J2jo78j%2FDzZCGLVbwPf9T7uSKaNf0NHc63JNpWSLuzGt8qjU145OMJrOezvk7oiHH%2BE5UxiJN7wLin5qe7hV4PVEKR5ghFjLWW59aEzU2zgPy&X-Amz-Signature=d1abeb1f0144d47e2f44f198b8c9c190260f1065baec90e405f1ca9a6f2d3100&X-Amz-SignedHeaders=host&x-id=GetObject)

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
