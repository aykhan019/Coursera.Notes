

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2TMQWG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCb%2BZ4CGtLtsgGU2%2BM7L2AVwTfucbUN28w0KUFVXh5cdAIhANsAd2jiXqWAc4wh83X%2Feo5Nf4fAkyo7ACZUhUo3EmZ%2BKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzX85w6ALqG4SaDTJMq3AOphQaBBj9enwTkgh6a7%2FP7IQGOtdpZCd7FmvwT30Z9xX4yzmEoDqCW7%2FISchtQKtWTvTk%2B51AqNq5JHmvQmKSCSjhbMvnod0NWA4JAO%2FEBPPBwnQomDPsuQcAXki71Eu2iURTPNVRrPYeRaqgzb7jiDdNGNj3zieAICB9K1lSP8yYhhsowxv%2BuFE6aZJ88MxJKunuOJDzVn6z%2FxclBGUiXq7HWOBMsj0Phjrq8uU22qj8MoQOK0snaAoygNFzVLNuWFsgrVVit9QXCvlCMxnc5%2Fry7BzTXHln5SaBUc3AXXKnjxDZjwClmuLJqJdR7xIShMJ9z2IQQ8V74GucP5OUdg0BrEED3PY47eJWUMkFch%2Bq7omDcmIvquLhjWL%2FWFzeqeboLeeSrtWG4dxSwY2m%2F8uwUwm4ueBcdGwy0lsN68l%2BEX7lwoI85CySh2zSOq9MTfVtQArDAJMJaob52Mi4rl34NewfP9GdG4dxBzEvBOgG8GZ6WBuyW%2B%2B%2B40EhOykA7F7Xs%2Brr6KZwgkwf2wF6OAoFeMR1exqy224BTgH2Q%2Fp3xCBGlU24rwZwqBmzZRwnM74kyLeUspRBUofF4u4c6Dhdt6MRWnYsZQOQM3dXEugqYA6Rrob5Oi9xKfTCe0PC8BjqkAVjOKTySzZ1Lx8EPp84BnFvjDdZqjQ1CKY3HNLQjTl0vpVwqhEZ9OiUZgXjKnWqWMdvr8zuksvT6b%2BNfM3doVdDttyNeASHG59MNw4k34Qbe%2FfbKHwHYmwx%2BoJ%2FftI3zsLawMLF4WUHZ%2BTLYXkZAKYF4sqEz6q6wcR68ZwZHxR%2FWS2UAt%2FPTERiS82dDNMzQpbziP77sg0o85LY4klk5ZksvpWOJ&X-Amz-Signature=c183022149d2d4a0a2a94de0d289ef32b25e6aacd34a94274d3cdc64c61b0c75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2TMQWG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCb%2BZ4CGtLtsgGU2%2BM7L2AVwTfucbUN28w0KUFVXh5cdAIhANsAd2jiXqWAc4wh83X%2Feo5Nf4fAkyo7ACZUhUo3EmZ%2BKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzX85w6ALqG4SaDTJMq3AOphQaBBj9enwTkgh6a7%2FP7IQGOtdpZCd7FmvwT30Z9xX4yzmEoDqCW7%2FISchtQKtWTvTk%2B51AqNq5JHmvQmKSCSjhbMvnod0NWA4JAO%2FEBPPBwnQomDPsuQcAXki71Eu2iURTPNVRrPYeRaqgzb7jiDdNGNj3zieAICB9K1lSP8yYhhsowxv%2BuFE6aZJ88MxJKunuOJDzVn6z%2FxclBGUiXq7HWOBMsj0Phjrq8uU22qj8MoQOK0snaAoygNFzVLNuWFsgrVVit9QXCvlCMxnc5%2Fry7BzTXHln5SaBUc3AXXKnjxDZjwClmuLJqJdR7xIShMJ9z2IQQ8V74GucP5OUdg0BrEED3PY47eJWUMkFch%2Bq7omDcmIvquLhjWL%2FWFzeqeboLeeSrtWG4dxSwY2m%2F8uwUwm4ueBcdGwy0lsN68l%2BEX7lwoI85CySh2zSOq9MTfVtQArDAJMJaob52Mi4rl34NewfP9GdG4dxBzEvBOgG8GZ6WBuyW%2B%2B%2B40EhOykA7F7Xs%2Brr6KZwgkwf2wF6OAoFeMR1exqy224BTgH2Q%2Fp3xCBGlU24rwZwqBmzZRwnM74kyLeUspRBUofF4u4c6Dhdt6MRWnYsZQOQM3dXEugqYA6Rrob5Oi9xKfTCe0PC8BjqkAVjOKTySzZ1Lx8EPp84BnFvjDdZqjQ1CKY3HNLQjTl0vpVwqhEZ9OiUZgXjKnWqWMdvr8zuksvT6b%2BNfM3doVdDttyNeASHG59MNw4k34Qbe%2FfbKHwHYmwx%2BoJ%2FftI3zsLawMLF4WUHZ%2BTLYXkZAKYF4sqEz6q6wcR68ZwZHxR%2FWS2UAt%2FPTERiS82dDNMzQpbziP77sg0o85LY4klk5ZksvpWOJ&X-Amz-Signature=7c1235e117258bd2e72c3d8bf09a4ef7091a82239f840ac7906731acd56ed66d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2TMQWG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCb%2BZ4CGtLtsgGU2%2BM7L2AVwTfucbUN28w0KUFVXh5cdAIhANsAd2jiXqWAc4wh83X%2Feo5Nf4fAkyo7ACZUhUo3EmZ%2BKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzX85w6ALqG4SaDTJMq3AOphQaBBj9enwTkgh6a7%2FP7IQGOtdpZCd7FmvwT30Z9xX4yzmEoDqCW7%2FISchtQKtWTvTk%2B51AqNq5JHmvQmKSCSjhbMvnod0NWA4JAO%2FEBPPBwnQomDPsuQcAXki71Eu2iURTPNVRrPYeRaqgzb7jiDdNGNj3zieAICB9K1lSP8yYhhsowxv%2BuFE6aZJ88MxJKunuOJDzVn6z%2FxclBGUiXq7HWOBMsj0Phjrq8uU22qj8MoQOK0snaAoygNFzVLNuWFsgrVVit9QXCvlCMxnc5%2Fry7BzTXHln5SaBUc3AXXKnjxDZjwClmuLJqJdR7xIShMJ9z2IQQ8V74GucP5OUdg0BrEED3PY47eJWUMkFch%2Bq7omDcmIvquLhjWL%2FWFzeqeboLeeSrtWG4dxSwY2m%2F8uwUwm4ueBcdGwy0lsN68l%2BEX7lwoI85CySh2zSOq9MTfVtQArDAJMJaob52Mi4rl34NewfP9GdG4dxBzEvBOgG8GZ6WBuyW%2B%2B%2B40EhOykA7F7Xs%2Brr6KZwgkwf2wF6OAoFeMR1exqy224BTgH2Q%2Fp3xCBGlU24rwZwqBmzZRwnM74kyLeUspRBUofF4u4c6Dhdt6MRWnYsZQOQM3dXEugqYA6Rrob5Oi9xKfTCe0PC8BjqkAVjOKTySzZ1Lx8EPp84BnFvjDdZqjQ1CKY3HNLQjTl0vpVwqhEZ9OiUZgXjKnWqWMdvr8zuksvT6b%2BNfM3doVdDttyNeASHG59MNw4k34Qbe%2FfbKHwHYmwx%2BoJ%2FftI3zsLawMLF4WUHZ%2BTLYXkZAKYF4sqEz6q6wcR68ZwZHxR%2FWS2UAt%2FPTERiS82dDNMzQpbziP77sg0o85LY4klk5ZksvpWOJ&X-Amz-Signature=32c2cb47453ce319d4f2c38ff7303eba09fa9a56bcaca2a11b8535762b35a23a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=481f692dc04e999d794d5c7b441898c2ecdd3401ca01b16c9cf9611753bae261&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=d268990d07d491d4c271d815a87cee8f2eaa9eda87108e234fb9cb0df982181f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=161150ec9025f99004c241a3749198d4acbacda615834c443bb8c28cf61e43e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=8f888cf1d08d0a0dab36e2e03febee2e500e3046c89f1e5a1a00402b78490c41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=84b3d06c336c4bd7a9989eff92b043583921aeb3793895c0609b8b9aa0126c97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=3a5b358cde86b11eb03c3c2e03d4a619728595929ce17aa9e75e03c6156ca3af&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZZVTCWW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBK3NIJ9vyYtd%2FPjXW5l4Hka9J4QAU9BZQHiDecr5DSIAiEA4TwezBFYPxu%2Blui5uv%2BRZS%2BSy4Nn9XrV925tt1UyNKMqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDRN88LFd4LpzdzYyircA4lvw3zn%2FVbQbZljXh7vpzAhCAJ3ZkkUHwxyvc9RohRVYYR8MCD9SSZ0iV1vql9%2BwfqpdMpUDECdvgHwoHpk3fAydszgHQ8qA3T%2FSGG9qZTEhmOZ32t1sXYP7Wf98GkEb8fKTuLe4ia2ulQAeAecwGbL%2F1WmCzMhzlLSIVyo4IK8a1eAQxVymLAte6M32kE5M0iUPZvJptUn%2F8PL1wPaqEftI7c9uYpXVQxg1FM2qh5BuevlZsO0FF9dzUdyzpju7VQoZ36sTzBFwLNmHqIuo8O0PiGJ0w3PYMwZ9xPmpElv3HCB%2BbKiD20uWQIRujNDCo5LMOLF3szV8lKEvpiQhEtsBJwwD7IQskOXhRKxQntOcQIFcPmG5Wq1UvUGN%2BOzKjnsDmfsiB6EYJ4alruOGz9aoMjz7DezaE5FFXUHASU5lnaFXdb%2FIVrsZbStU9A28%2FFLJoq%2FMVEQKa%2BsbPSO4w5b2cfq2wfyObemeW%2FZAFeWXTH7xke1W4yxIcccmmapX67zE5YXIAQGppvYx6TwqCCR2w7eTYeu%2B59gAHbxgfqlXQR8eCIelWuB4m%2FKLaUTHszIajtQkAhcoW9xvi%2FxirsvrKoo3A4remliQ1opXL5uUkHO5PgJ%2F1eZ6qDeMJHQ8LwGOqUBQe5ucLOAatGdV8D6%2F5lWlY%2F0Du2gNPCwlEz2D3hVUXXOGAowBN58c1HiGKSGMIAMVwqBhrZuw%2BI30UnrdXZ59DbAoEP5RKoKupJidRWoKcpx6Ve5G21S3wYDGR5MuL5vYS2vFXU9EXrdZWHYAyiiEVFblLb4LeoSHEHRKkVZ5pMJgEUUxRU0Wfxc2YWeR5nSDZulqXVR%2BaIcf8ht%2FWkMCPPZzI5S&X-Amz-Signature=00ef6ff33793ac8d6b01c68f794d6e10d373845218cc06cb6aa81b7d06ddb8cd&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D24UIIY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8A%2B%2ByxmKXFecqUwwrigteIMGMqyP1VIte6xIvpnJDZgIhAMB38U%2Fc64e%2BdzsEpPYkzlTsNCwFiwRSl7DGa5UqnMxQKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwzG2PDLQleuWBKMq8q3AOxLIHoxr8vYXpVdtZBnsrYB9BAQ1Wv2jAtlkoIIpznpxx%2FvpQDoErC0Ak3QTmty3SK17mG%2FzNoESv%2BvPylBeBV5Otalf5RJla8XCj67owPPjeFJmhk1UFoYW972YOvOUNwbwQjx%2FIXR1L%2BjO8ffplHqbeh8QQ84icxzpveIrKDfdbnp6u%2FdqdLS0t7bkX613nADg%2B4ssIzNmd6jgkQRNu2J9TzVka6zZXbKqynwiFbRUGx8oN%2FIQJS63xWUKjwyR2kqFNa%2FudrDbAgSGlWn7ZsoVlnYMVzxb40BQWcf%2FD6FU1bLOoMY2oxO5hR4UgKDnv9JYc%2FdnM3EqS896NVq4OtQdtct89tD11nexjc%2FUdZp8AhRfANGCk5fifz3QJeWQYYGwTkmRqDqE8HkX3WdwgCxrNXIA%2BhtZCkx%2BRDPp1foT0nfB6GXI8W9YVLGLw2hAUZ1T8CzE24r3l0eCapgMIyvu2F7AadZQbiyzX90ym22lP1WngySMmVEBhOBdogXXIo2YnnKgwzzCl5QI7CoB6pdy%2BDLl3auD%2F%2FbQDzzeim5028y3rbENicXRlhhYWxwSaB2gbLtAkmhWNShUgGySVWhldZHMHbUrD7xBYc%2Bh3NenKTGTEzGxj747xwYDDJ0PC8BjqkAbRieeqcUoTd5dugNzAQvX%2Fvte%2FQ%2Fm6D2KKJUUBI2xgWSXwWgIw54rESzP0%2FTY6VS8I%2FDUE%2Fh1Te8sUI8loVEL2GKcxX9ArXwxVOwfIEzRAvQNrsCpNiYuePpS%2BAdBihLTOo%2FPGtYBYRM%2F8zeeKEptM2e%2FJaJYWzA5RBYAOgODruw8niA5qVvDF96dLRZjcrcFsFRpLebppv3uM5hBbOCfvoNx9u&X-Amz-Signature=fb3b0c6d770ef5c0cf0e0eb215eb98f1a0f4ad40c3f8aa8a5c7fcc697af5f829&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=41b73854cbb6da83b3c988f18bcbfed0066a403f3ded82a883dbc835c7214f54&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=57db41a73f5d99734cf02316b577f4450387c66b8a1dbae84ad3432b5ac3f5ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVL3VU4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDOlZ%2BTNJ%2FfhG%2BP1zlt4mnUyhGf%2BEYhY1%2FdCBexFi%2FVgIgDc0qk3sWk%2FWiE2Z1OhT9eIZ3x2hGQbiqjocwhc%2BzPaAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA3aXNEXIlE6WiEJCrcA5AUzLghyz%2BueWZ2ZJBuMT0FcgyHPbCdyDZ4IsLy2PMeUlVjhLv5iqX8%2BqF1dVpBH13Wfrb3AeB%2BvOuw%2FGj6FmBv19m5LBSlPz5IOO8KIwHSyaQEVTl9WuR0FdaqXoxnL9d6laP4S2MrX82DYsxc%2BQ7SMbAWkPu6a2hATne7%2BedxrxeOo7PYkGvVbAj8SN5knXmxYSmWfkDRNIqhVZj%2B4WUxsASQZ5PQSnp8xI7ixINtVMs1eRxt8eCdshQHnJ061uc3JMaA03T48GZNAUDgTiteicgVOvwXEwCartszLdPYufpF0Qq8HBmuTazJrX5%2B0u7iNNV0LIxf4ndjuw341lEvbqbBSUXmnvKSVpjsZOpYG7y0KyOEGnJMw4Ngq3NOqzUucfYkslz62RRQ6ge%2F7BPExTKfLRuTxSzwBgHfPn%2Bv7%2Fmttm1fm45vwwjQBugIidOXyi%2BwWuiiAduDx8n0%2BOVNRRCA8SnTh1NveJbMmF3KzwIRMUFtfNB6nkj6I5JnDvfcx7H6rOupKUTOq3Wj6wPDzx%2BlUVUch7yP5CWrO99ppAL6nzIDWDKEl9s8TkMSNdL%2F6nABdb3kH0%2BWDEhhdA%2Fpm6FgTTZgRWDE8fxo68BBQGsztGScpMkTUGqKML7Q8LwGOqUBCGEZ3sk%2BUIJMyH4qL3%2FEPb0vZr933eZoDJltxhQYPGPFWZkOtGI9y999dyXy3rGaByvsNxBasEKOmpjr%2B0KhUzwz7n%2FCdj0VJFNfH8Il4GE5Wx8nfMaxg9PkwRdtWDwLFy84aYXxC90PAont8yVZehuuwsR2UC6x4o0KN5t%2BceLgp2k5u46%2F1%2FZmlXbsoMAZ7PV2T02g70ZJrN66OzKYTDoCls7h&X-Amz-Signature=76bb69e3011f79d3157c2a98012d50cc0ab9ac30f83ed3a336c009e7a1cb1d67&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCVZNHPZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEDbg%2BMRa9qoMyybYh21s8ugk9oA8Q08Jdo8pqo2FiFXAiAVYYMkJKyv3NIh6eWGZ4%2Fhj81QDUC26uWrMwbfiFUCQCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1ewimAdXNYy%2F4Xv4KtwDW%2FZAIbEk5Zd5KFM64FVDRIWcDpwjCSdQkO1xJSSWhtFEaUJ1FqchO04ylOKcUp6j2tP3C3YbGJMAhovRMI9ForR06YNXyXwjFWwev7HKjtlCznRPRvBdeV0AkK%2FYe0pCuOYrxohpIh5lfrfh8sijt1aGi0VMIY%2B0VopzDhd7VeMhb0GMAO4GDsQ%2FhvhtMtql8mDPaz1Weq2vwTA0SRszKEZVcu1xS104Ele0cex8utUTqRnp9LWcRgi4RRLa4jq7rVNRvMJBG9i%2FNNn7Mo0ETv0HSNG2Pc8ZkQbvJUfKgL1YZ11sc64ahRk79WUo%2F0l2bfy3jHv1YA7bQfIHnSoJjnzJzdNMLsvK3VNyFyW31NkUGzjeMe%2BNbz4KIBYDIgFAeVeC%2F54tMAiUo3KfdZPqHwJ2o5P6YNzVSxbkWVVkwb0fl4zT0ei%2Be3WOXPOryUsTad3rrEtdN%2F4rwQoxleMsZ%2BDjw8GbF4SUX0Fg1pUszQS33uHg5IHzqkm%2FU6TgbS0Id%2BOcFJ7T4C2KyisCngWnwcDDP1pEOTRYGm0chHEjwz2suSbQ1pj9LofFwaCcKNEVHVek6w5zLtuazaUvYDmjjcqNpJh0%2BPAfeSD6Og6v%2FnZfF2bIZGKCBvzC36cw4tDwvAY6pgGiKGfWkbmCcyu6mw8uSU4ZYuCSIrk0axD1fwb274hf2Uoi3xfxUs%2F1wAoUX%2B4pOfMQyneIQjhNiU6jOi30LwPr9wsL1PbpSxfE%2F%2FhZCKKz4e5dAojm%2FIygEck7PWPjqKZgJ7Fuef6fTdcOPU8EoRxhIK8VxtfSIregOK066w%2FwTyDK8wtuR18wmoAx5yB8leOPBm3xtVHDd88RL2pGGEy%2FM24oa6Fm&X-Amz-Signature=cd5ab8e7e637aa449dfb039badd74c149369629c1f5e6d980100d3723ce44461&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LRVCPMC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnfbE9DnQg8T4CO158VWFST3ZkiLCxlXZ1wj6Tg0dPBwIgDgFcH0z1mSFgRT93dXc08EU%2FPvFILfrKysvmRT9vaoMqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNNOZwCb33ktiraQvSrcA2beCrDx6Gly07%2FKZCRUMMczFEooAyTFvtOv%2FR2EmI%2BkunlGPxEq%2FZNDgd9aqeX7IIRWRBBuZNSwD4HaWvWE1fFJCmrKik8rUz9%2Fj1p6a0WFhnbG0iTcVf5z7DHE9clcxp11VbjCABhD4fcocYPlE9x0FOFWBGhCWqGr7kvbj5QGf1d5tgCfjfBxMwCdBVU9Ujv5U7Nr0a63RQXqhzwFGPZCh7%2BuMvVrXH9SbTDxK6mXKP0R5OT1y8mV0adchwgElNgIMd6Pkhm9Vl86q5bK5fgtOfIBy%2F%2F9C6AwZjg3LqXP4AZwGLUN%2BEn5q2ok9Wcyya3ojvqL7cWtFkGWXYS7rhk40OoBVJQWRpi4sVyX0ZND4o21i2CI%2FHcMW5HloRU82qXh5SbFvUULpNezikI%2BbK6m%2FiFEvdIZSdHCHj%2FPJLKk0RaeSMA2JLuVQvlkTMOZYGq%2FM5pFblzjNSP7Cjtv%2FXH%2FgeSsB6nNM9x%2FMuc0G0z%2FubFfwTQ2wrdwkxX0RTdIKqnqrU61m%2B8GwHX8GT3gaZ8big%2FlTQ29saYPeeuyDZ8d0sPM%2BD8Zplmce7NpkedEw7i%2FvHS1zKR7SyhcpV7sKJY1NDUL4Wdhaun2wReEgIToxEaIpGUn1xj3K2AyMM7Q8LwGOqUBF88tOWd4K0hsU7vRugoAFgcMNn%2BAPkFzhNp37eHkfYnRovf7ljVUclKwLrlmvbWIH8qnvwjRd%2FaoXifG8iXyJIWCcGUZI9TWLBipn%2F9YjWLr4NcsFZIdfXBOgInh7brQ9VWryXZ040KPfCvlUCxxaRhSfWrsys0BU%2BdTLPplcm5O639TG0f9stILICEWUh6sz%2FUe8gWDWCsmnQV3X9XX%2FFaVEovv&X-Amz-Signature=09b2fac2ea1658d7c48cca2c3a996c8db408597acefb3b248ae4fb9b3d88290e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAIICPLC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiazoFOsQ6x5CFnKdliCSNTX9IbNWl7LRvv4VT8hX0ZwIhAM6Qx%2FtEmvOIn4DfY%2BOIVQh8ncioEqom5ofrcxq%2BSi%2BUKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2eEvsyJ%2Bjy6Eh%2FoQq3AOWA0ggs3yQ6AtDyqh1kKIJQLcDLYKkphX7NbpES4ZwNKf2WmKrU7pq67vdNrREXP3nIPgnQXYk1EnqaVfa8oOnwq8TXOAh%2Bepq0pfmDbs6QpU%2F%2ByejI0CqqPTHwoIUCfkw4wogRC2os2S5OVZGh9R7KM7QIx8BU7EBxB06267rbbPjHaPoSEqxJSluA0Z3wm6OectZFWdsSxQqu5EN4B9iDvTM3cHfqfYeq95nCyGZZfM5X8SkDU21EJUSizsVfhV13X0VqScbmIYvlGhLpT0YmtVgVW7x185mLjWE5Lvxtwmy6psJqSb2MTmVpS3KCTSLeWy7b4S8by8pTLOuzaDWrmfbj2tbTl69%2FlohQyDAFLyLeVwxJph7hIl%2B318IP4EujWl6mbblnh5UmeWrs26rwRuhNyA0J24%2FZyz2vVZfB8EIbuuCtcGK%2BPHslthwrBkbXNKRaWbi5gszzMzl9uGC1XrHEgEjY7kE2WmItDtAoTQuvJG2ThXzwKzqMB%2BRBWreXmQqIe7%2Be%2FVScgAl1csEGyDtU0%2BHJfgaF5voQqU1czYiXYcLk51AA9JkhFXBMkZilEdW6yNzB7Q71oAcX7US77Uci%2BfX8EEhIUAq3ApO72KmC2HOpur8LWsMXzCA0fC8BjqkAeogXV7eX7k7pxPVg6wjqx8rusv8GH9LncNbJBa1BL7ZbqrfXBjYhf2xEPYIl8TswY9g9yNz%2F6GF3jIXGUJIdRnYTS%2FdHCz38wLRqawVP3PXioh%2FT5tcMy%2FtRw3EgHKTw7wNrSWR65SqgMnOeD0Vss6hvBHBDKXuAyfLOjNndsKCNN%2FP2SidfavK3oDfo7iwZPt3aWhH8ao5%2Bp2qiXqWE0T8bHCd&X-Amz-Signature=06de9d109d77ad5535c2df8848818a51f8a7aa7c2901d3d8b612010fc5c4ede8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4PRSCTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOjm56ccvyxHlEojq2hQduGLR3PWZd8ACb05oIcVe%2BagIhANzsIUX4vIY0%2BJK8RBhbfkVTPxRJ%2FIq4x6xqHxCIo9MuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDmCTAMfhdyyJnv7sq3AOzygbjLtwzNbYdXPgzMtzR5PD9EfVVtdOK9MR%2FLReXAb5WbEOeNgWHF%2B0Qfbhs0WjQ1nzCLYHU3Z9r8fsQTI77jGPWxhkDV69b8KAPGg6g0vK3%2F%2BXdcysjSGTZbgS5zNw6ylO66DCfTZlgeRJDplFBUuw2IkR797K%2FhlXjErE3YwtuFrgQEXVqLe2Bxc3b%2B9toEHgW9KBXwqhIUJjbRJhPmSs6rCaq4hAqLxAVU9PoJR0b3PlY%2B%2FE75blgeAyfiz%2Bx%2BahqoG1%2F4f%2FJJD5x3ElF4SBePwMbxxPbL%2FiDn%2BuUCRsx7gM6WlQTiHK2GSDYOBxjWDhhegvag8XT7hST4FtK6SP%2BDy%2FZ9PsRTS5fRzwg%2BYf9M0GG4pxJmNoJXRCpj5xMfuekMHrOMhiRHflLpz8xxBJcNb0%2Fj3ZXwu269ysp4VE%2Byj5Qm6rAqfKGE0KjqE%2F77CVPnPxH102qydrErFaLPer4iMuDRUMdyANQPP7PWUhZvAnWkyLP%2F%2FHUHpTYgCC5N1%2BHQpsaHvviTqApIbCu27drzED%2Bu41XKCBM0vMTVAM9uouIoBrR%2FY%2B5B8M6fkhi0XdefgfecK9ShU4KlixSX%2B2J6C9WhC8kxoALFd81UOMbaIuoCEBXUb6%2FOTDc0fC8BjqkAc89vX3%2BesDxu%2F6VIN7Z%2FS2tlozECMbztTqN5yMSRaVrrHFrBjpq2bKWNesN0cHw%2BX7ucUnfJcHy8jv0JWyqmBk%2BPyjUBVcZCMMoKlXTMs4U0s7b88uACWcP1%2B49psO6YzPWHls8mNgwNoIHYUpVDlAJFPwLjFLBgq08FLepx97f1ue0DSIDnhsvVdGu4ZgYm%2B%2FMfiHOjYG9e7k8EQHfWuSBrRAL&X-Amz-Signature=45f2a9231563775efe38b3c46647fa425aef23e7c18398bc4364e707f24075da&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4PRSCTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOjm56ccvyxHlEojq2hQduGLR3PWZd8ACb05oIcVe%2BagIhANzsIUX4vIY0%2BJK8RBhbfkVTPxRJ%2FIq4x6xqHxCIo9MuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDmCTAMfhdyyJnv7sq3AOzygbjLtwzNbYdXPgzMtzR5PD9EfVVtdOK9MR%2FLReXAb5WbEOeNgWHF%2B0Qfbhs0WjQ1nzCLYHU3Z9r8fsQTI77jGPWxhkDV69b8KAPGg6g0vK3%2F%2BXdcysjSGTZbgS5zNw6ylO66DCfTZlgeRJDplFBUuw2IkR797K%2FhlXjErE3YwtuFrgQEXVqLe2Bxc3b%2B9toEHgW9KBXwqhIUJjbRJhPmSs6rCaq4hAqLxAVU9PoJR0b3PlY%2B%2FE75blgeAyfiz%2Bx%2BahqoG1%2F4f%2FJJD5x3ElF4SBePwMbxxPbL%2FiDn%2BuUCRsx7gM6WlQTiHK2GSDYOBxjWDhhegvag8XT7hST4FtK6SP%2BDy%2FZ9PsRTS5fRzwg%2BYf9M0GG4pxJmNoJXRCpj5xMfuekMHrOMhiRHflLpz8xxBJcNb0%2Fj3ZXwu269ysp4VE%2Byj5Qm6rAqfKGE0KjqE%2F77CVPnPxH102qydrErFaLPer4iMuDRUMdyANQPP7PWUhZvAnWkyLP%2F%2FHUHpTYgCC5N1%2BHQpsaHvviTqApIbCu27drzED%2Bu41XKCBM0vMTVAM9uouIoBrR%2FY%2B5B8M6fkhi0XdefgfecK9ShU4KlixSX%2B2J6C9WhC8kxoALFd81UOMbaIuoCEBXUb6%2FOTDc0fC8BjqkAc89vX3%2BesDxu%2F6VIN7Z%2FS2tlozECMbztTqN5yMSRaVrrHFrBjpq2bKWNesN0cHw%2BX7ucUnfJcHy8jv0JWyqmBk%2BPyjUBVcZCMMoKlXTMs4U0s7b88uACWcP1%2B49psO6YzPWHls8mNgwNoIHYUpVDlAJFPwLjFLBgq08FLepx97f1ue0DSIDnhsvVdGu4ZgYm%2B%2FMfiHOjYG9e7k8EQHfWuSBrRAL&X-Amz-Signature=d39e1c4c5709f7e57b367c1fb32e44a341b354f634786b5c996bc6b8c495775c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
