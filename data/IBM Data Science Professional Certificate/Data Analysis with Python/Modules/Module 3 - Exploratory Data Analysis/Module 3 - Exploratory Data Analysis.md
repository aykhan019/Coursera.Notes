

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YV4SYGWZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDI8mWxGzRwzawkqkUsa7bpLpVWYfQiZTsq1RGofsfOIAiByuhOSE2jAOAg6MNkfkvXdNzoDn9fKA9blv5%2FDRXvAiSqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLBgcHusCmZPDSSk3KtwDU00q1mgit51%2FAwqD2iTG0C2SpmaG2GX47ddQIsWgcoQ9K9SDQYP3yw0iOWT%2BvCo7Fh%2F3mMZuOLxitqPA53LvBSXewWrkfRCY6si6a1oPGdxBoYlghCwElk2qutLrR3VonWomJ5fs1RKvguOfCWT9XcetCU0NypLkvO0giqwVriyeU6pDEmvHnSQRThKOPxQrr86rBD1KtwRpp1kUC%2B4v81JVqUBFZQUzZgb2p%2BloZH3RHzXAk1NKBumcZvH0YVtgPsf8GAZ4ppzQak6Pw4see%2BALdiQYGiiMjANE1lafkDrj1s9M8YzQqSnIskwaGT7tX%2FWDKt0cfXHIf%2F2psQNuEopmLIoF78wCtv0W8cAhvfJIVpj29HDUxuwkIdJ6BjCjINfi%2FrB4xi6iIsVfTAnPqURtg6CS1ABEw%2Fw3QSU41jes3d2Vj5fCZy%2BYCdrXW%2BDI6LW2zBouNaO%2Fz%2BDYG7JHtljfY9YW1YiY2Xd%2F9pciyJgxffOkEiSCVwBYzM3fTsGmVJ0KkMBz%2BEteeZVU9uSlUF3ZQhCJkk3p82%2BtONnzxXlZR3XaAluo1SiIA458So9aNMZDHHslmteXcbp4N%2FHXNXMA1oCDMP0Zl%2FC%2BS6OmrcNhh9%2FtzJfxh3kmmMIwisD0vAY6pgG8auUmDmsbWJF82kRMD9ZB6x6solym1pdY6Dy28ej1Z7qZR9PXqA8KQdBTWn0zPzlCELHZSQati2LXW%2B6cMGqxUV41s%2B8VAmWqefWraj2y3hEIohXc2h1craAmb%2FZ2dgnpqZXvGjqNYqFSFGiMMu7bwfdK91JlN75llzChJFrewhwNsshVLNiaUx2FqWley38VUaUHzFTT5Wv12ZqnaQcPSKpLVNah&X-Amz-Signature=61c9a418c66c373c3b3ffd3af72f816aef4a369c2c189f2b775e238d74fcd491&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YV4SYGWZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDI8mWxGzRwzawkqkUsa7bpLpVWYfQiZTsq1RGofsfOIAiByuhOSE2jAOAg6MNkfkvXdNzoDn9fKA9blv5%2FDRXvAiSqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLBgcHusCmZPDSSk3KtwDU00q1mgit51%2FAwqD2iTG0C2SpmaG2GX47ddQIsWgcoQ9K9SDQYP3yw0iOWT%2BvCo7Fh%2F3mMZuOLxitqPA53LvBSXewWrkfRCY6si6a1oPGdxBoYlghCwElk2qutLrR3VonWomJ5fs1RKvguOfCWT9XcetCU0NypLkvO0giqwVriyeU6pDEmvHnSQRThKOPxQrr86rBD1KtwRpp1kUC%2B4v81JVqUBFZQUzZgb2p%2BloZH3RHzXAk1NKBumcZvH0YVtgPsf8GAZ4ppzQak6Pw4see%2BALdiQYGiiMjANE1lafkDrj1s9M8YzQqSnIskwaGT7tX%2FWDKt0cfXHIf%2F2psQNuEopmLIoF78wCtv0W8cAhvfJIVpj29HDUxuwkIdJ6BjCjINfi%2FrB4xi6iIsVfTAnPqURtg6CS1ABEw%2Fw3QSU41jes3d2Vj5fCZy%2BYCdrXW%2BDI6LW2zBouNaO%2Fz%2BDYG7JHtljfY9YW1YiY2Xd%2F9pciyJgxffOkEiSCVwBYzM3fTsGmVJ0KkMBz%2BEteeZVU9uSlUF3ZQhCJkk3p82%2BtONnzxXlZR3XaAluo1SiIA458So9aNMZDHHslmteXcbp4N%2FHXNXMA1oCDMP0Zl%2FC%2BS6OmrcNhh9%2FtzJfxh3kmmMIwisD0vAY6pgG8auUmDmsbWJF82kRMD9ZB6x6solym1pdY6Dy28ej1Z7qZR9PXqA8KQdBTWn0zPzlCELHZSQati2LXW%2B6cMGqxUV41s%2B8VAmWqefWraj2y3hEIohXc2h1craAmb%2FZ2dgnpqZXvGjqNYqFSFGiMMu7bwfdK91JlN75llzChJFrewhwNsshVLNiaUx2FqWley38VUaUHzFTT5Wv12ZqnaQcPSKpLVNah&X-Amz-Signature=78560b319e89f25f0b5b954cd36560e1eb30d9a8b712aee1b1aaa866bbca24a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YV4SYGWZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDI8mWxGzRwzawkqkUsa7bpLpVWYfQiZTsq1RGofsfOIAiByuhOSE2jAOAg6MNkfkvXdNzoDn9fKA9blv5%2FDRXvAiSqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLBgcHusCmZPDSSk3KtwDU00q1mgit51%2FAwqD2iTG0C2SpmaG2GX47ddQIsWgcoQ9K9SDQYP3yw0iOWT%2BvCo7Fh%2F3mMZuOLxitqPA53LvBSXewWrkfRCY6si6a1oPGdxBoYlghCwElk2qutLrR3VonWomJ5fs1RKvguOfCWT9XcetCU0NypLkvO0giqwVriyeU6pDEmvHnSQRThKOPxQrr86rBD1KtwRpp1kUC%2B4v81JVqUBFZQUzZgb2p%2BloZH3RHzXAk1NKBumcZvH0YVtgPsf8GAZ4ppzQak6Pw4see%2BALdiQYGiiMjANE1lafkDrj1s9M8YzQqSnIskwaGT7tX%2FWDKt0cfXHIf%2F2psQNuEopmLIoF78wCtv0W8cAhvfJIVpj29HDUxuwkIdJ6BjCjINfi%2FrB4xi6iIsVfTAnPqURtg6CS1ABEw%2Fw3QSU41jes3d2Vj5fCZy%2BYCdrXW%2BDI6LW2zBouNaO%2Fz%2BDYG7JHtljfY9YW1YiY2Xd%2F9pciyJgxffOkEiSCVwBYzM3fTsGmVJ0KkMBz%2BEteeZVU9uSlUF3ZQhCJkk3p82%2BtONnzxXlZR3XaAluo1SiIA458So9aNMZDHHslmteXcbp4N%2FHXNXMA1oCDMP0Zl%2FC%2BS6OmrcNhh9%2FtzJfxh3kmmMIwisD0vAY6pgG8auUmDmsbWJF82kRMD9ZB6x6solym1pdY6Dy28ej1Z7qZR9PXqA8KQdBTWn0zPzlCELHZSQati2LXW%2B6cMGqxUV41s%2B8VAmWqefWraj2y3hEIohXc2h1craAmb%2FZ2dgnpqZXvGjqNYqFSFGiMMu7bwfdK91JlN75llzChJFrewhwNsshVLNiaUx2FqWley38VUaUHzFTT5Wv12ZqnaQcPSKpLVNah&X-Amz-Signature=ac7fdd0721d8b306483563cde9b75485589f2f747c82793cabda67a0c2246df9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663264TFPE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDP97%2BNyznBU5cOMpStKcN%2BXBVoPZNSBnCugAjPFGk8twIhANbhLQF%2BpXAz%2FkeKjM35NIvco0iOaevuBjsFABhAoqZDKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpEi1SxlgZyCLB0nMq3AO25Y2P%2BQtxF%2F6NABwIe5Vn6PLssNRipIebHNnd0MwiFoISPdCtC9PQfuSxQGkzUz1s7mDFfoB%2BqXGouN6K5ew3f59fWcwHQT8fvTb0qTDhY%2BaPU%2FgZZ1VDfCa8xDgclk2A%2F3zjeauRetc0UKjfli1bjeoXCrDTD%2BdqjPndxMBG1Od%2BXkew8z6eNNgk4RUsqvT0lrWYsCYAFYULoBGrnU6H7dGu7kMfnqjid8ExTbd9Kc03kZjOZlvvfUC2KUxpGPdxCguaiBXZaC4zAlJCAyG44QPZOF08ggAg9Vm%2FVmyN2cNC0fu5lqmDcRxvvr6OoVqxFCuNlAZtJnOA9CaZRH1%2FDCmO1iD8fsDfq%2BXeucZphHuwjwjSeNR%2BQ21yQYgyJCKjd%2BXaXTK2sYOiHj4p35kltnvv%2Fpri2yqkf%2F1TMgbNpfySymcS7eCt11njqpApsMvuz00mVwu8%2FfSKmjmINEDrygCHanh%2BNOtWN0HGoSPeoWwMnmJk8I00MUjBUyKmI3g64AAe8A5K8ZxnXM5GyCS8kMyvNU%2FV4FPgiwFjuzcGAgUZ4PUX3yFIouiwXbc9qhPbx7UdD0565ZCvVgTpR75PkhGnw8tuEBxWZcGf7Ly737KCsYVC3UiwoM9DSjCMpPS8BjqkAZDZrjxADLDvIScXOzKuOUlsK70ZwP0E5o0cs4ZjotDm9oJ5lcPIovjV7EWcCAqNf1pXw7UtlcR2n3OkWphDgVDUNtzKTVkKHoc1zNGC5iTK7AO787ooJgDQbu5%2FeP3oVNeooWQI83hHtMPwAFO%2FqeZQWfsj7RSvz%2FtEIL1pCrvhcmH2S5ip6%2FBuJrTy5KiS5%2FfPUlWB8gTYldomZA3MvezGLcFU&X-Amz-Signature=6e07a10e2c88ba21d9728f56374d265726ed1132601840acbe45a0a868961e96&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663264TFPE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDP97%2BNyznBU5cOMpStKcN%2BXBVoPZNSBnCugAjPFGk8twIhANbhLQF%2BpXAz%2FkeKjM35NIvco0iOaevuBjsFABhAoqZDKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpEi1SxlgZyCLB0nMq3AO25Y2P%2BQtxF%2F6NABwIe5Vn6PLssNRipIebHNnd0MwiFoISPdCtC9PQfuSxQGkzUz1s7mDFfoB%2BqXGouN6K5ew3f59fWcwHQT8fvTb0qTDhY%2BaPU%2FgZZ1VDfCa8xDgclk2A%2F3zjeauRetc0UKjfli1bjeoXCrDTD%2BdqjPndxMBG1Od%2BXkew8z6eNNgk4RUsqvT0lrWYsCYAFYULoBGrnU6H7dGu7kMfnqjid8ExTbd9Kc03kZjOZlvvfUC2KUxpGPdxCguaiBXZaC4zAlJCAyG44QPZOF08ggAg9Vm%2FVmyN2cNC0fu5lqmDcRxvvr6OoVqxFCuNlAZtJnOA9CaZRH1%2FDCmO1iD8fsDfq%2BXeucZphHuwjwjSeNR%2BQ21yQYgyJCKjd%2BXaXTK2sYOiHj4p35kltnvv%2Fpri2yqkf%2F1TMgbNpfySymcS7eCt11njqpApsMvuz00mVwu8%2FfSKmjmINEDrygCHanh%2BNOtWN0HGoSPeoWwMnmJk8I00MUjBUyKmI3g64AAe8A5K8ZxnXM5GyCS8kMyvNU%2FV4FPgiwFjuzcGAgUZ4PUX3yFIouiwXbc9qhPbx7UdD0565ZCvVgTpR75PkhGnw8tuEBxWZcGf7Ly737KCsYVC3UiwoM9DSjCMpPS8BjqkAZDZrjxADLDvIScXOzKuOUlsK70ZwP0E5o0cs4ZjotDm9oJ5lcPIovjV7EWcCAqNf1pXw7UtlcR2n3OkWphDgVDUNtzKTVkKHoc1zNGC5iTK7AO787ooJgDQbu5%2FeP3oVNeooWQI83hHtMPwAFO%2FqeZQWfsj7RSvz%2FtEIL1pCrvhcmH2S5ip6%2FBuJrTy5KiS5%2FfPUlWB8gTYldomZA3MvezGLcFU&X-Amz-Signature=de88c053a897428082a722951d106907534171d0655abc6685a5753e974cd079&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663264TFPE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDP97%2BNyznBU5cOMpStKcN%2BXBVoPZNSBnCugAjPFGk8twIhANbhLQF%2BpXAz%2FkeKjM35NIvco0iOaevuBjsFABhAoqZDKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpEi1SxlgZyCLB0nMq3AO25Y2P%2BQtxF%2F6NABwIe5Vn6PLssNRipIebHNnd0MwiFoISPdCtC9PQfuSxQGkzUz1s7mDFfoB%2BqXGouN6K5ew3f59fWcwHQT8fvTb0qTDhY%2BaPU%2FgZZ1VDfCa8xDgclk2A%2F3zjeauRetc0UKjfli1bjeoXCrDTD%2BdqjPndxMBG1Od%2BXkew8z6eNNgk4RUsqvT0lrWYsCYAFYULoBGrnU6H7dGu7kMfnqjid8ExTbd9Kc03kZjOZlvvfUC2KUxpGPdxCguaiBXZaC4zAlJCAyG44QPZOF08ggAg9Vm%2FVmyN2cNC0fu5lqmDcRxvvr6OoVqxFCuNlAZtJnOA9CaZRH1%2FDCmO1iD8fsDfq%2BXeucZphHuwjwjSeNR%2BQ21yQYgyJCKjd%2BXaXTK2sYOiHj4p35kltnvv%2Fpri2yqkf%2F1TMgbNpfySymcS7eCt11njqpApsMvuz00mVwu8%2FfSKmjmINEDrygCHanh%2BNOtWN0HGoSPeoWwMnmJk8I00MUjBUyKmI3g64AAe8A5K8ZxnXM5GyCS8kMyvNU%2FV4FPgiwFjuzcGAgUZ4PUX3yFIouiwXbc9qhPbx7UdD0565ZCvVgTpR75PkhGnw8tuEBxWZcGf7Ly737KCsYVC3UiwoM9DSjCMpPS8BjqkAZDZrjxADLDvIScXOzKuOUlsK70ZwP0E5o0cs4ZjotDm9oJ5lcPIovjV7EWcCAqNf1pXw7UtlcR2n3OkWphDgVDUNtzKTVkKHoc1zNGC5iTK7AO787ooJgDQbu5%2FeP3oVNeooWQI83hHtMPwAFO%2FqeZQWfsj7RSvz%2FtEIL1pCrvhcmH2S5ip6%2FBuJrTy5KiS5%2FfPUlWB8gTYldomZA3MvezGLcFU&X-Amz-Signature=6b9e78dcb2c33298661a5b6632508a247cec60e5fa4d5c90444111a187f759e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663264TFPE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDP97%2BNyznBU5cOMpStKcN%2BXBVoPZNSBnCugAjPFGk8twIhANbhLQF%2BpXAz%2FkeKjM35NIvco0iOaevuBjsFABhAoqZDKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpEi1SxlgZyCLB0nMq3AO25Y2P%2BQtxF%2F6NABwIe5Vn6PLssNRipIebHNnd0MwiFoISPdCtC9PQfuSxQGkzUz1s7mDFfoB%2BqXGouN6K5ew3f59fWcwHQT8fvTb0qTDhY%2BaPU%2FgZZ1VDfCa8xDgclk2A%2F3zjeauRetc0UKjfli1bjeoXCrDTD%2BdqjPndxMBG1Od%2BXkew8z6eNNgk4RUsqvT0lrWYsCYAFYULoBGrnU6H7dGu7kMfnqjid8ExTbd9Kc03kZjOZlvvfUC2KUxpGPdxCguaiBXZaC4zAlJCAyG44QPZOF08ggAg9Vm%2FVmyN2cNC0fu5lqmDcRxvvr6OoVqxFCuNlAZtJnOA9CaZRH1%2FDCmO1iD8fsDfq%2BXeucZphHuwjwjSeNR%2BQ21yQYgyJCKjd%2BXaXTK2sYOiHj4p35kltnvv%2Fpri2yqkf%2F1TMgbNpfySymcS7eCt11njqpApsMvuz00mVwu8%2FfSKmjmINEDrygCHanh%2BNOtWN0HGoSPeoWwMnmJk8I00MUjBUyKmI3g64AAe8A5K8ZxnXM5GyCS8kMyvNU%2FV4FPgiwFjuzcGAgUZ4PUX3yFIouiwXbc9qhPbx7UdD0565ZCvVgTpR75PkhGnw8tuEBxWZcGf7Ly737KCsYVC3UiwoM9DSjCMpPS8BjqkAZDZrjxADLDvIScXOzKuOUlsK70ZwP0E5o0cs4ZjotDm9oJ5lcPIovjV7EWcCAqNf1pXw7UtlcR2n3OkWphDgVDUNtzKTVkKHoc1zNGC5iTK7AO787ooJgDQbu5%2FeP3oVNeooWQI83hHtMPwAFO%2FqeZQWfsj7RSvz%2FtEIL1pCrvhcmH2S5ip6%2FBuJrTy5KiS5%2FfPUlWB8gTYldomZA3MvezGLcFU&X-Amz-Signature=2e85be97a48ed81370d57351d51e701a977d032acce3ced985f51b4137e84c74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663264TFPE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDP97%2BNyznBU5cOMpStKcN%2BXBVoPZNSBnCugAjPFGk8twIhANbhLQF%2BpXAz%2FkeKjM35NIvco0iOaevuBjsFABhAoqZDKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpEi1SxlgZyCLB0nMq3AO25Y2P%2BQtxF%2F6NABwIe5Vn6PLssNRipIebHNnd0MwiFoISPdCtC9PQfuSxQGkzUz1s7mDFfoB%2BqXGouN6K5ew3f59fWcwHQT8fvTb0qTDhY%2BaPU%2FgZZ1VDfCa8xDgclk2A%2F3zjeauRetc0UKjfli1bjeoXCrDTD%2BdqjPndxMBG1Od%2BXkew8z6eNNgk4RUsqvT0lrWYsCYAFYULoBGrnU6H7dGu7kMfnqjid8ExTbd9Kc03kZjOZlvvfUC2KUxpGPdxCguaiBXZaC4zAlJCAyG44QPZOF08ggAg9Vm%2FVmyN2cNC0fu5lqmDcRxvvr6OoVqxFCuNlAZtJnOA9CaZRH1%2FDCmO1iD8fsDfq%2BXeucZphHuwjwjSeNR%2BQ21yQYgyJCKjd%2BXaXTK2sYOiHj4p35kltnvv%2Fpri2yqkf%2F1TMgbNpfySymcS7eCt11njqpApsMvuz00mVwu8%2FfSKmjmINEDrygCHanh%2BNOtWN0HGoSPeoWwMnmJk8I00MUjBUyKmI3g64AAe8A5K8ZxnXM5GyCS8kMyvNU%2FV4FPgiwFjuzcGAgUZ4PUX3yFIouiwXbc9qhPbx7UdD0565ZCvVgTpR75PkhGnw8tuEBxWZcGf7Ly737KCsYVC3UiwoM9DSjCMpPS8BjqkAZDZrjxADLDvIScXOzKuOUlsK70ZwP0E5o0cs4ZjotDm9oJ5lcPIovjV7EWcCAqNf1pXw7UtlcR2n3OkWphDgVDUNtzKTVkKHoc1zNGC5iTK7AO787ooJgDQbu5%2FeP3oVNeooWQI83hHtMPwAFO%2FqeZQWfsj7RSvz%2FtEIL1pCrvhcmH2S5ip6%2FBuJrTy5KiS5%2FfPUlWB8gTYldomZA3MvezGLcFU&X-Amz-Signature=098a6cdf0ac1a43a7423b830234c468f6e156faed20074f98a301bccb6eeef2c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663264TFPE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDP97%2BNyznBU5cOMpStKcN%2BXBVoPZNSBnCugAjPFGk8twIhANbhLQF%2BpXAz%2FkeKjM35NIvco0iOaevuBjsFABhAoqZDKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpEi1SxlgZyCLB0nMq3AO25Y2P%2BQtxF%2F6NABwIe5Vn6PLssNRipIebHNnd0MwiFoISPdCtC9PQfuSxQGkzUz1s7mDFfoB%2BqXGouN6K5ew3f59fWcwHQT8fvTb0qTDhY%2BaPU%2FgZZ1VDfCa8xDgclk2A%2F3zjeauRetc0UKjfli1bjeoXCrDTD%2BdqjPndxMBG1Od%2BXkew8z6eNNgk4RUsqvT0lrWYsCYAFYULoBGrnU6H7dGu7kMfnqjid8ExTbd9Kc03kZjOZlvvfUC2KUxpGPdxCguaiBXZaC4zAlJCAyG44QPZOF08ggAg9Vm%2FVmyN2cNC0fu5lqmDcRxvvr6OoVqxFCuNlAZtJnOA9CaZRH1%2FDCmO1iD8fsDfq%2BXeucZphHuwjwjSeNR%2BQ21yQYgyJCKjd%2BXaXTK2sYOiHj4p35kltnvv%2Fpri2yqkf%2F1TMgbNpfySymcS7eCt11njqpApsMvuz00mVwu8%2FfSKmjmINEDrygCHanh%2BNOtWN0HGoSPeoWwMnmJk8I00MUjBUyKmI3g64AAe8A5K8ZxnXM5GyCS8kMyvNU%2FV4FPgiwFjuzcGAgUZ4PUX3yFIouiwXbc9qhPbx7UdD0565ZCvVgTpR75PkhGnw8tuEBxWZcGf7Ly737KCsYVC3UiwoM9DSjCMpPS8BjqkAZDZrjxADLDvIScXOzKuOUlsK70ZwP0E5o0cs4ZjotDm9oJ5lcPIovjV7EWcCAqNf1pXw7UtlcR2n3OkWphDgVDUNtzKTVkKHoc1zNGC5iTK7AO787ooJgDQbu5%2FeP3oVNeooWQI83hHtMPwAFO%2FqeZQWfsj7RSvz%2FtEIL1pCrvhcmH2S5ip6%2FBuJrTy5KiS5%2FfPUlWB8gTYldomZA3MvezGLcFU&X-Amz-Signature=fc9bb7b3b65a1bae15d8baefa327d88d0fd8ad40f0600a6c5e5bc2ac9870b827&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HMCIKQ3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG%2BseWSDCLU5Wxa9q6bg0hI%2FVoZ9ECaLDRzA2Zkw18DoAiB4GPR4msmey4or2mdAAgQq32MzKSjfpRcZAhg5A5XbiiqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH8X4fbj30DnwqZCtKtwDW1bBkSgxbLOFX%2B%2BLLQfuYH54q4knJB%2F9%2Fvw3exhgTHX5n1%2BPUbeeIfNwaUpryHIjbyaQrFPiI9rFVOzf0H8cnduDWwNmXPvtdTl3BVyN4fTQwkoUL9UKG%2Bhaobt%2FsoF715lhVd6mXhgY%2BOn0epeuIaYIjFFbfy27EH96DuhIloZcCAaAnwVEbmeM2KVtbZwLOoRbKRJDh%2B13g6rO8Nd0vyfbDodYNP8ncC0dwdXhki1NJrdpls9W4WZzp4TMhMeoDk7dJq62eEjPjbf01SyPRzpMnv7JQe4qp6Y785BC4WMcqwZZflU9jAeA1H7rMUGoCw1peqEW1cBEgAKs7Jo%2FVbA2Hy0v3lpqeiI24hrTnTcup43vJVJL3YawKPANE6u44FJOVI4di%2BujyLb4h7h5QTvTPABLZYibmifn%2B510zgQxg0c1XHLhpXUC4XuoxRGfv13xnT6QKAoide81a5OM49XxBkA0GDqHabD5Rpy4f1TxLM5Zf54Nr152EaBxAgBZOQyk6cr2RtRtvkuYo3ICv3Dm9X9aFBKy5df5Y5nzIP5EkDA05jLsz%2FBW4TcE030IdM4Yb1tUBIDhvi4m6YSLyASXfz8ug%2BoFqLo93Mv%2FAKDX%2FSnaB1nliqGN9ywwnMD0vAY6pgFzTsEJwIhBK3U5VUH4z8CHFQBrIJrG15xmpItGWQJdQP3Up4LzrEND%2FBuvo1i9R3vqChEUUCU8uX7T%2BSviyic9epLl76qm8UhwYeFvKxNtjxdEK%2BHxt4opcTWFhR9wOjIJgqfpGk0j%2B5vw%2FtPL8vfMOU760pzG8qEqmFns61EuQrckDghJYVTDgRJ%2B8IVVpH1Ae8AZqBodbrTs9dhHs7sKUbXbfCru&X-Amz-Signature=86d76ef75cb291f6dbd56f36a4dbe6b82cbd447368e66a89295737c7f80c1b41&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEN7QASL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOp2YVSDPMo7WP8TziR48LIslEVAr0E9%2FPQ993YjwYAwIhAJzzRLXVFsT7c66NYBi0ebEExbcmJ7Kd365EyGyCnfHLKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFqjae2qrJRDcblQYq3AOJ%2BKdqm11wEmuojDvMxJVuOjjW2izvkULgDUdbItF09Gdp4athqVhInV4OtiE5dlDCwOuGvDiZwr6mVLup8Q515gRrL9X6TL9i1EnEWlUHxgB6aJIOsVsp%2F7IyX8dpkxpHpOA1DpewYSNH5C7y1FW9fYSH07Bp%2BwxnvCf1uUYvVdyzMTiS3v2931j1t6dywa0SrEb1g62oIGpHW1Hdx9Pzxp08%2FnEKRi9pwl%2BvrB%2BAISLZarBQ08VnoRU87%2BYFaVHhLyKBEBSnajO8F8XZSS3XuRH1vOqd%2BpkKHgUxaF7RU5aiV6j%2BnjdIVYZEXm%2Bl4JyBQVrxlOCPE8gvG65Ghxnr8dmpNpTnbmcuhGV8pSwaJ8Ric29o%2Ba9vtkl7mElkwAap8t1Y4bqlSmC2NzNGGutUlBwW6x0EsduAbJUgGcjnxP78zZ7mtlkqIkq9Z9mZSukR3exKQCFpKHcU1ezDJkURKsemQCnwq70zrBzWNrvvUpgKJN5dHqnO64g4nxTERmYdtk9r2Gm3iU29KmR6bt6vCdK4de4F%2Bv%2F1z4U9%2F9ewTZgPPpguMQvEyCDsgTvuU73GNODurOeKk4HQXp%2BRqhkJnqJrE4TDH6jhx7SmVesKWZGloNWiqgZOmgBGGDDPo%2FS8BjqkAfosa833uk04Fe8PYVQWf77ZOag0Bwo1Z19OSHoBm6k2Y6svRBbgYqliG2dMnNX%2BFQyxP26BYtzXDv%2FSO%2FrXm%2FLD0lFUn0HTRG17dgmlmroTdVdOfjSvU5Y6ZoFH3cvMIT08V8jwx5pHwQlg3yIJO%2F5jq82s2sETAS4eTokyxC2MbL2cYjJRGI98p30ZAFSJMZqqIcsANcjuThgAHMv9jCnEWK7u&X-Amz-Signature=230e138b667d6e9025e70741e0dd547c3c160a9b36f8d0a47ba228df49cb1d44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663264TFPE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDP97%2BNyznBU5cOMpStKcN%2BXBVoPZNSBnCugAjPFGk8twIhANbhLQF%2BpXAz%2FkeKjM35NIvco0iOaevuBjsFABhAoqZDKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpEi1SxlgZyCLB0nMq3AO25Y2P%2BQtxF%2F6NABwIe5Vn6PLssNRipIebHNnd0MwiFoISPdCtC9PQfuSxQGkzUz1s7mDFfoB%2BqXGouN6K5ew3f59fWcwHQT8fvTb0qTDhY%2BaPU%2FgZZ1VDfCa8xDgclk2A%2F3zjeauRetc0UKjfli1bjeoXCrDTD%2BdqjPndxMBG1Od%2BXkew8z6eNNgk4RUsqvT0lrWYsCYAFYULoBGrnU6H7dGu7kMfnqjid8ExTbd9Kc03kZjOZlvvfUC2KUxpGPdxCguaiBXZaC4zAlJCAyG44QPZOF08ggAg9Vm%2FVmyN2cNC0fu5lqmDcRxvvr6OoVqxFCuNlAZtJnOA9CaZRH1%2FDCmO1iD8fsDfq%2BXeucZphHuwjwjSeNR%2BQ21yQYgyJCKjd%2BXaXTK2sYOiHj4p35kltnvv%2Fpri2yqkf%2F1TMgbNpfySymcS7eCt11njqpApsMvuz00mVwu8%2FfSKmjmINEDrygCHanh%2BNOtWN0HGoSPeoWwMnmJk8I00MUjBUyKmI3g64AAe8A5K8ZxnXM5GyCS8kMyvNU%2FV4FPgiwFjuzcGAgUZ4PUX3yFIouiwXbc9qhPbx7UdD0565ZCvVgTpR75PkhGnw8tuEBxWZcGf7Ly737KCsYVC3UiwoM9DSjCMpPS8BjqkAZDZrjxADLDvIScXOzKuOUlsK70ZwP0E5o0cs4ZjotDm9oJ5lcPIovjV7EWcCAqNf1pXw7UtlcR2n3OkWphDgVDUNtzKTVkKHoc1zNGC5iTK7AO787ooJgDQbu5%2FeP3oVNeooWQI83hHtMPwAFO%2FqeZQWfsj7RSvz%2FtEIL1pCrvhcmH2S5ip6%2FBuJrTy5KiS5%2FfPUlWB8gTYldomZA3MvezGLcFU&X-Amz-Signature=9c007c91a7ef48e6b1e334adb4f0a850bc8bb41a25d133ec37bdea4d65fc8bab&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663264TFPE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDP97%2BNyznBU5cOMpStKcN%2BXBVoPZNSBnCugAjPFGk8twIhANbhLQF%2BpXAz%2FkeKjM35NIvco0iOaevuBjsFABhAoqZDKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpEi1SxlgZyCLB0nMq3AO25Y2P%2BQtxF%2F6NABwIe5Vn6PLssNRipIebHNnd0MwiFoISPdCtC9PQfuSxQGkzUz1s7mDFfoB%2BqXGouN6K5ew3f59fWcwHQT8fvTb0qTDhY%2BaPU%2FgZZ1VDfCa8xDgclk2A%2F3zjeauRetc0UKjfli1bjeoXCrDTD%2BdqjPndxMBG1Od%2BXkew8z6eNNgk4RUsqvT0lrWYsCYAFYULoBGrnU6H7dGu7kMfnqjid8ExTbd9Kc03kZjOZlvvfUC2KUxpGPdxCguaiBXZaC4zAlJCAyG44QPZOF08ggAg9Vm%2FVmyN2cNC0fu5lqmDcRxvvr6OoVqxFCuNlAZtJnOA9CaZRH1%2FDCmO1iD8fsDfq%2BXeucZphHuwjwjSeNR%2BQ21yQYgyJCKjd%2BXaXTK2sYOiHj4p35kltnvv%2Fpri2yqkf%2F1TMgbNpfySymcS7eCt11njqpApsMvuz00mVwu8%2FfSKmjmINEDrygCHanh%2BNOtWN0HGoSPeoWwMnmJk8I00MUjBUyKmI3g64AAe8A5K8ZxnXM5GyCS8kMyvNU%2FV4FPgiwFjuzcGAgUZ4PUX3yFIouiwXbc9qhPbx7UdD0565ZCvVgTpR75PkhGnw8tuEBxWZcGf7Ly737KCsYVC3UiwoM9DSjCMpPS8BjqkAZDZrjxADLDvIScXOzKuOUlsK70ZwP0E5o0cs4ZjotDm9oJ5lcPIovjV7EWcCAqNf1pXw7UtlcR2n3OkWphDgVDUNtzKTVkKHoc1zNGC5iTK7AO787ooJgDQbu5%2FeP3oVNeooWQI83hHtMPwAFO%2FqeZQWfsj7RSvz%2FtEIL1pCrvhcmH2S5ip6%2FBuJrTy5KiS5%2FfPUlWB8gTYldomZA3MvezGLcFU&X-Amz-Signature=bc56fbe027d16e229a37a4c60f4d22191abefbcfa267b21cff6c8190285ea02c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663264TFPE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDP97%2BNyznBU5cOMpStKcN%2BXBVoPZNSBnCugAjPFGk8twIhANbhLQF%2BpXAz%2FkeKjM35NIvco0iOaevuBjsFABhAoqZDKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwpEi1SxlgZyCLB0nMq3AO25Y2P%2BQtxF%2F6NABwIe5Vn6PLssNRipIebHNnd0MwiFoISPdCtC9PQfuSxQGkzUz1s7mDFfoB%2BqXGouN6K5ew3f59fWcwHQT8fvTb0qTDhY%2BaPU%2FgZZ1VDfCa8xDgclk2A%2F3zjeauRetc0UKjfli1bjeoXCrDTD%2BdqjPndxMBG1Od%2BXkew8z6eNNgk4RUsqvT0lrWYsCYAFYULoBGrnU6H7dGu7kMfnqjid8ExTbd9Kc03kZjOZlvvfUC2KUxpGPdxCguaiBXZaC4zAlJCAyG44QPZOF08ggAg9Vm%2FVmyN2cNC0fu5lqmDcRxvvr6OoVqxFCuNlAZtJnOA9CaZRH1%2FDCmO1iD8fsDfq%2BXeucZphHuwjwjSeNR%2BQ21yQYgyJCKjd%2BXaXTK2sYOiHj4p35kltnvv%2Fpri2yqkf%2F1TMgbNpfySymcS7eCt11njqpApsMvuz00mVwu8%2FfSKmjmINEDrygCHanh%2BNOtWN0HGoSPeoWwMnmJk8I00MUjBUyKmI3g64AAe8A5K8ZxnXM5GyCS8kMyvNU%2FV4FPgiwFjuzcGAgUZ4PUX3yFIouiwXbc9qhPbx7UdD0565ZCvVgTpR75PkhGnw8tuEBxWZcGf7Ly737KCsYVC3UiwoM9DSjCMpPS8BjqkAZDZrjxADLDvIScXOzKuOUlsK70ZwP0E5o0cs4ZjotDm9oJ5lcPIovjV7EWcCAqNf1pXw7UtlcR2n3OkWphDgVDUNtzKTVkKHoc1zNGC5iTK7AO787ooJgDQbu5%2FeP3oVNeooWQI83hHtMPwAFO%2FqeZQWfsj7RSvz%2FtEIL1pCrvhcmH2S5ip6%2FBuJrTy5KiS5%2FfPUlWB8gTYldomZA3MvezGLcFU&X-Amz-Signature=19071b90ab872e9bd1a4ce41e1ff4e1abea244f10ce6c680d5a94b25c86f7e99&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPISUUS7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjk3m7%2FoV172jz2sH8TDU2dLaDLwUn5I%2FJjI2e8CSB6gIgGpGqMlAez0EG7tdzz0CYDrRwyRylgs1gUKSjRUO0jM0qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMmkPp%2F50GgMJYBkGircA4Oemt%2FK76cLUFK5sIxc1af6ReJKwLa1TjRRa%2FlVCRRqct9e7l%2BgFgu4JPqaWanQ9Le%2BUdw%2Fkh5RTtZWpLbAgoVfK1sg44ek21EWUQjA%2BK8nQtRh%2FgzBGiXiRStQ97cHZR9YbYTxQ6gMh3Iv80MyIaWZbwC1j80X03S4sDWnv7xf9uBEJn1UzkzAcg9asQDDgWqTcckA8bD6BoM42%2FOZZyMa%2BWcBbEoQd%2FLLaIHiiYqlaxXQ2rqxkqzej5Oa5dBWapk6%2BOsok%2BCsxjPQQkSjDbDo6bivRMdeblMNJPPOoq7tPNRDLKHFBFBK86lhoC971QP3ItcrGYV20MwDPjwWi%2FBD30NC0hbPrNPQLMbKgyz%2BUa5yo7edn349ngHyK7an%2BpBF3I7th9FlohrMhNNKQUgwNZ9KLM2jwx1NKg2w%2FsTGVGSo5%2FzYMitpf2%2Bh3IApf098nYs1IK1KQPn3SE9FWMUx%2FZm0iQRSlAPxQTFHCWh16YlbuLBNQLeX0LvW2OvNdu5ycoloGqIZuvh2X1%2Bd2NypMdtmNp5utNhCKMe5Ij6QUcjMZ%2BkE8sItQmvxVkQcc3HEVef0mSB5o%2FncG9AsOnDw9UrKebk9dAZbhoQ4EA018FjAvS6k0e8QSURCMKCk9LwGOqUBvoVgSSFttV3q0%2Fgduoi6d%2FqOhYXWBqcI1OI%2F3W3lLe8%2BYsHozdXRgu13SyZhBjx24MgkeWoeH3Tl9YZLd%2FXuFceg5goL8Ls4NWdM%2Bjs9V%2FW0KuV8bAgUK98nEDk7Y2DTieGc1OfoQ9mzmuFD7WXGtBYlSEzKWPGJE%2B6pYH1DOEsx6RUucW87VMddG8YX7pIYl1vQ40cOYcN2ckw%2BS5O244Gbd6Xo&X-Amz-Signature=51b64b6d8e93d2060178ac44cfa11f3c130dbc3698a11d508a34f7513417a337&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQW37SN6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNc5yCryFwgu6%2FXVo731rJEuNzoRMEySLZypCK7b9czAIgAP5h21Q87GYqW4wA2ZGjG2ZWIq61X%2FCvJJgWDHo0hm0qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0A6QM%2F5tAuD%2FAFYCrcAyEpU4uOqVex0BWi6ifAOkXWuO2tu0Fpb05vmDo5oL4NzmGF9zP0MBzCgWs%2FWy1D2urckdpwt3ar%2FWogtZb2cIJDAIJ0nUh5T11PddfCDm5CsFE%2B6GSrYUo3vANC%2F4ulNC0z%2F3NhUCOXSWQSnI1wVCCm%2BILEBgRmy1XyqO4R7IAniqHHWqDH0QtiF9sWHn5kfRcBfBJk%2FHOQh5GQbg5a7Z4sJ2MrM7opCzXXE13BUSZ6fJmft8%2BPUxm0vQLvTvHyRFmQgVAH4ZtKOTZ2tLXezmXva0BaA3D76tW0aqBh3AV0GtS1RALVG%2B9NkyfhbfROlaFE571NsJa2EVVB%2FyE5LVvyKII4PvWUjEFRAB2Nq7n6OocstYQovA8iGQJTa3oKdeGQm1UjOkPqhk5CKkhFfSMW8SGthV6sdYb3c78RxwTXnH%2FU%2FJUN3VPRAg%2Bmw2BwazVQlLrngoZIarx6U4IGjXo1hIY3o6RPSIfcnqh%2Ft4oD%2FP1OUrhkvML5cOeKSZzXmIVlNpXIW8A2bVamMXytexdiSpX8%2BsqWRhiLX6IJGzJieBQZKX0qNq3MVAEIfteJ3qNxasktKzX9ruGfwZaLPrRcAZMlORhYQ0Ww3sloSdMvS8lvunM8r4UEFoPJMOSj9LwGOqUBs%2BSbG6fYRGt6oEbM8JJ5n74oHWX9YhfuzbH8GBjX1QijqFbu1ZuJ95e%2BPYjQfWATVpqw962YFSb2%2F%2FklTtwz2PsNlhlvIk%2F3QSFvlrI2kq5pTifEAhkSoFHg7OZOdEO%2BnUKR7rv4IT0TwoSTfceD07kpMxh1QY6%2FlZyApqTF6IpLm6TeZmVNxrEwyUfiNIhy%2FweUxN4ud26yUfZyoPGiBzZFE5og&X-Amz-Signature=885244b48bad757a22c165cf9b1f0a58d12724c23db593f849685cfc1515642f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF7VGIXX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC28YeNGNr14kvzVcOwxGbeCDOVBIcJAhPPgPNzvmI4qAiAIIG7q9WgoZNRCnK2TSkJbWRULk2O4BJWlM0tdWVvH%2FyqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmfbH70MdAPj0e9WDKtwDK0IcA7BQCES%2Fbsizlofcy47pAxBKyTaJAqKaubMwnI6wEOQp2e73MKEdO%2FjFb0rELoNx4WvHUPsr%2BNldcIfsUSVjRXiis1DPvh8SSZL6nytW%2F%2BwkuzgrUfNPZnC8ZvwL3uMhOHvL%2BTkkg323U16C7t74nkc%2F2VTEw0hyG8LaY4rFcDdlguuIa2It%2FcU9Ry%2FSsVcHxa00m6ldzu4%2FEIy%2BYq2ei2hvszI6TKKi6TmHkZf1FWinf3qbh5L7NKhly5I3fuPd4Ln2zdXykvNPDhMqp%2Bdb%2BSS%2BMM0ja3vhTebA9qtCSvma5naXEI7Rysq4U3mvz4Uwn9UjthnWfiolGZqPrJ04b4nA7tb8%2F2gj3SFGg4U5RqtS6FyYiqfBAt0HYaylmC%2FILPOhIwGcIUmqhzaSJ54d%2F3Oc1ni2R8NY8Gh%2F4V6YyehYeborphvXwcuG%2BHiR5JXWeMg1nxFaKEKhhdgI40x18nxHozMDuVzaWWuzbcksepnj6KBsAVdMFbXqhyjoCJ6u7LYK3KASQlT4%2BiYGZsTk4%2Bo%2BcqBpMgtFbChwEVRp9gJ0YKKzaTW79Z8W5H9vfTGUmUH1EnHNHPLU%2BaXdd5HcbuYcf7mnfrrR%2BU7KIT48VtHhEt7ht1KR4v0wraT0vAY6pgF6zCnGOp5b4ywMQdqHnq9ul%2BrC72aNBOc2ymQkMjPKX%2FBu3o1wTCb3X%2F9IWa0YLNH%2FKSSMtIxSbGvYjG%2B8nKjrzmdziwU2qGAEjLu6A8l5cXxfWoi5ep%2BVc6%2FRwBD0eZtwAnmrwJbDZc0kTJWVVCaLMy7gAnDeVee6%2BT%2BStIL1DZe%2FIkiEkyiXkDEERblm7ouqAef84jaonCdXOEPL9MYG9AEZoqk2&X-Amz-Signature=af64d570a37f9bd03d615ac386496bb0102b7a56f2a087586bceb28c7e2377a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGUBK2LX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyMMG9QU%2FUGqEXZJTbte%2FJJWMLQVi38rG7dnLRKVvSUQIgZNR9VtDrwipeu7L5nyE6aYyjJztdR%2BF1OLxzgdvcCigqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLf0Sl9gkkJ%2Bfkn%2BECrcA8dfDuFaUeJRzW%2BtYFSDR18cl2HLLFOl06Wvn5MPiDdEkYUhPEzk7eSs2zROtaE2s4Lq5dqTrvPhUbgh2opzKZZiBYDdSas0rpUKKm8b0CrFLx5GeJZGSSOP0ntx0wc9AbjQVyJyoSpzQofmxZk7SyEgmbv5bOnKnGCxkK3kOfh5dzgk31wHNt6H10G6npxCDWJnrOJ4kscfZsR%2FgWW8K7D%2Bu1N3Fop5sXZJpyAHHTKn9AV9F5ycpn542qV8IiNm%2F48fNmj5WF1NSm%2FmGLT6DN8FxruNQX2BirdaHXDQWXp4zKGo%2BmLBBG1ZPM8iULFVZtZhDpTlVl0XUHTGIkP7q9%2FSZQ%2FTOhX08dh1RybggAz9Gri6c9Jko%2BIdPY99G5XISp%2BgVGSHmrMnkRYFBJ3IDPs0TKgNgXcpAIqVGWe8PTDt0ONcKRuCo%2B4pxvPS8Wc1TEh8QD7SZf8Qs7fe%2BhFNsrNNXJryr4xNYPwUnw9l0ecxhy%2BECXaJr7NssRFZ%2F2Jmdb%2Fw4HhGqhflAiDl%2FMF%2BDQmQuwBzpxGBxRknGG3iZvlBh1O74G107EGvFBESIINF0conppuVD1t3lmMYUmT7oEHovf70ICON5ALtRP1HxS6oNe7hC51vDgCu3avtMPij9LwGOqUBy%2FwuM8B3iKvURNiJechFgc53kLqbORlhS9sOEqToPCjniG2LHiApOu3sxDacE1eY%2FAoD1ChFgoP3ZK0tq1cAZiaWLStr4%2BUGW2KiYRwOe%2FWSe%2FOOzOxuLkZMRlvUJnzWP8MmO2kuh0EpOTqZ3%2Flut%2FsdYEXlthsI%2BzaXhC1TB9T4xpvFpcIuczsIY%2BJYk5t0UuAB5cQa2otv9Y4tepm3ZD3aIKlP&X-Amz-Signature=01647f567680b43b9de747b2306c5a5eb135b1bd8570a0d64378fad85e9a4e48&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGUBK2LX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyMMG9QU%2FUGqEXZJTbte%2FJJWMLQVi38rG7dnLRKVvSUQIgZNR9VtDrwipeu7L5nyE6aYyjJztdR%2BF1OLxzgdvcCigqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLf0Sl9gkkJ%2Bfkn%2BECrcA8dfDuFaUeJRzW%2BtYFSDR18cl2HLLFOl06Wvn5MPiDdEkYUhPEzk7eSs2zROtaE2s4Lq5dqTrvPhUbgh2opzKZZiBYDdSas0rpUKKm8b0CrFLx5GeJZGSSOP0ntx0wc9AbjQVyJyoSpzQofmxZk7SyEgmbv5bOnKnGCxkK3kOfh5dzgk31wHNt6H10G6npxCDWJnrOJ4kscfZsR%2FgWW8K7D%2Bu1N3Fop5sXZJpyAHHTKn9AV9F5ycpn542qV8IiNm%2F48fNmj5WF1NSm%2FmGLT6DN8FxruNQX2BirdaHXDQWXp4zKGo%2BmLBBG1ZPM8iULFVZtZhDpTlVl0XUHTGIkP7q9%2FSZQ%2FTOhX08dh1RybggAz9Gri6c9Jko%2BIdPY99G5XISp%2BgVGSHmrMnkRYFBJ3IDPs0TKgNgXcpAIqVGWe8PTDt0ONcKRuCo%2B4pxvPS8Wc1TEh8QD7SZf8Qs7fe%2BhFNsrNNXJryr4xNYPwUnw9l0ecxhy%2BECXaJr7NssRFZ%2F2Jmdb%2Fw4HhGqhflAiDl%2FMF%2BDQmQuwBzpxGBxRknGG3iZvlBh1O74G107EGvFBESIINF0conppuVD1t3lmMYUmT7oEHovf70ICON5ALtRP1HxS6oNe7hC51vDgCu3avtMPij9LwGOqUBy%2FwuM8B3iKvURNiJechFgc53kLqbORlhS9sOEqToPCjniG2LHiApOu3sxDacE1eY%2FAoD1ChFgoP3ZK0tq1cAZiaWLStr4%2BUGW2KiYRwOe%2FWSe%2FOOzOxuLkZMRlvUJnzWP8MmO2kuh0EpOTqZ3%2Flut%2FsdYEXlthsI%2BzaXhC1TB9T4xpvFpcIuczsIY%2BJYk5t0UuAB5cQa2otv9Y4tepm3ZD3aIKlP&X-Amz-Signature=44dcc78575bb8c0ee73f58c3114e529dd2c7710ca3b6fed7603ad5b155a48cf3&X-Amz-SignedHeaders=host&x-id=GetObject)

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
