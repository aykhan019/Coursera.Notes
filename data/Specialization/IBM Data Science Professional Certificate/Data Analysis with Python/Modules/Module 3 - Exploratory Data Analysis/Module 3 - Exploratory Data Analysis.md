

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662H2G7UYU%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIAhpkhIni390QEgx7YMfTGbmPBnjFNs4vGX9aOPthjpTAiABhyIJdjQsdnemD9pLs0%2FyLn%2FRD4FiR07RWy4vUesxYyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMhrj%2FORc%2Fvo1qlNxoKtwDxHTvE6bY95prrlb6bLyl%2BiZf7PA4DIzW82sVprXbEw1OYCmKV8UqJQPNMaqKXI4NzvDITf7a%2B0TWKC4ycFP69DxKnep0wVl9BKOKl2ihDVVCB10pVfWOQdQL6j8KnLkULnSmYjNvm4JXE2Ei84qknx7NDioJwcOkhs5oVJNAyz%2Fv4TP22ASaNiDjuFphOGpjKc0o3WJ9J8YT8tl%2F2n9e6j25E3V%2BKse%2BWlOv%2BJpSnJu5Yxv5%2BnmrUIPONwyjsKyuaWG9xhSDZN98bboUGP0V2uxzPj6BHHFrQfAlyrRTRVKGBee55jIbo7lt350VxGTJhvalBqVAspHsC007ODxa5Czh%2BH1pky2zitbVQFFTpSSR%2FKK3ZeqFh%2B6DPK2aqaDU%2BmuNsmSQ3OyZBTssh%2BqC1DXq8aO%2FOSD9MkUY36%2BIqoFyT%2FfL%2Fapsss4IhjRlHD76hwHhVYyyybCsblRJbkdi9oNU5N00s%2Bi3LkUdDamszpZhRKXsVmw8U1pyHEJoRPYfDIKnYfyV1GSBzFJHue7dTdtbooayxD2yEv%2FQ2PiTuVa0XwzjPUZT%2FmYIyANdiTu4WSunInm4LNbiBunvuJ5nEKexw6Jdnuz02Gp8L9v7DJCd8OFWxE4ShEaHDXww7bDlvAY6pgFSH%2Fe9WAJ%2BGb%2B51lA384%2FEI5WqiguFMNS5Rw5UdYk9OHGFVzosapVqKo7STp4BNP0C5cOUs7lx0jNQ4V828QGdRbavS9zyfYEflgZa84weft%2Fy8hcQNz9OPvWdbJxEF6Pv%2FAb8Z7sbXKL3CdxVi5r8G%2FCuX0ykLHqkz2rwVLMqrmaEKc%2FhvRMhvIVHjUYxMMMEDJMDHQSsIFrc3TARwWC5%2FhmejW69&X-Amz-Signature=76e6cf2eeeff3bdc86240243f5837b9e1750d705694c0e22c5eb12720b59ce6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662H2G7UYU%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIAhpkhIni390QEgx7YMfTGbmPBnjFNs4vGX9aOPthjpTAiABhyIJdjQsdnemD9pLs0%2FyLn%2FRD4FiR07RWy4vUesxYyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMhrj%2FORc%2Fvo1qlNxoKtwDxHTvE6bY95prrlb6bLyl%2BiZf7PA4DIzW82sVprXbEw1OYCmKV8UqJQPNMaqKXI4NzvDITf7a%2B0TWKC4ycFP69DxKnep0wVl9BKOKl2ihDVVCB10pVfWOQdQL6j8KnLkULnSmYjNvm4JXE2Ei84qknx7NDioJwcOkhs5oVJNAyz%2Fv4TP22ASaNiDjuFphOGpjKc0o3WJ9J8YT8tl%2F2n9e6j25E3V%2BKse%2BWlOv%2BJpSnJu5Yxv5%2BnmrUIPONwyjsKyuaWG9xhSDZN98bboUGP0V2uxzPj6BHHFrQfAlyrRTRVKGBee55jIbo7lt350VxGTJhvalBqVAspHsC007ODxa5Czh%2BH1pky2zitbVQFFTpSSR%2FKK3ZeqFh%2B6DPK2aqaDU%2BmuNsmSQ3OyZBTssh%2BqC1DXq8aO%2FOSD9MkUY36%2BIqoFyT%2FfL%2Fapsss4IhjRlHD76hwHhVYyyybCsblRJbkdi9oNU5N00s%2Bi3LkUdDamszpZhRKXsVmw8U1pyHEJoRPYfDIKnYfyV1GSBzFJHue7dTdtbooayxD2yEv%2FQ2PiTuVa0XwzjPUZT%2FmYIyANdiTu4WSunInm4LNbiBunvuJ5nEKexw6Jdnuz02Gp8L9v7DJCd8OFWxE4ShEaHDXww7bDlvAY6pgFSH%2Fe9WAJ%2BGb%2B51lA384%2FEI5WqiguFMNS5Rw5UdYk9OHGFVzosapVqKo7STp4BNP0C5cOUs7lx0jNQ4V828QGdRbavS9zyfYEflgZa84weft%2Fy8hcQNz9OPvWdbJxEF6Pv%2FAb8Z7sbXKL3CdxVi5r8G%2FCuX0ykLHqkz2rwVLMqrmaEKc%2FhvRMhvIVHjUYxMMMEDJMDHQSsIFrc3TARwWC5%2FhmejW69&X-Amz-Signature=87411b3d28cdceb9fbbe0d1128d67d5c9cc8c8e065861e3be0246e8294cbd190&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662H2G7UYU%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIAhpkhIni390QEgx7YMfTGbmPBnjFNs4vGX9aOPthjpTAiABhyIJdjQsdnemD9pLs0%2FyLn%2FRD4FiR07RWy4vUesxYyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMhrj%2FORc%2Fvo1qlNxoKtwDxHTvE6bY95prrlb6bLyl%2BiZf7PA4DIzW82sVprXbEw1OYCmKV8UqJQPNMaqKXI4NzvDITf7a%2B0TWKC4ycFP69DxKnep0wVl9BKOKl2ihDVVCB10pVfWOQdQL6j8KnLkULnSmYjNvm4JXE2Ei84qknx7NDioJwcOkhs5oVJNAyz%2Fv4TP22ASaNiDjuFphOGpjKc0o3WJ9J8YT8tl%2F2n9e6j25E3V%2BKse%2BWlOv%2BJpSnJu5Yxv5%2BnmrUIPONwyjsKyuaWG9xhSDZN98bboUGP0V2uxzPj6BHHFrQfAlyrRTRVKGBee55jIbo7lt350VxGTJhvalBqVAspHsC007ODxa5Czh%2BH1pky2zitbVQFFTpSSR%2FKK3ZeqFh%2B6DPK2aqaDU%2BmuNsmSQ3OyZBTssh%2BqC1DXq8aO%2FOSD9MkUY36%2BIqoFyT%2FfL%2Fapsss4IhjRlHD76hwHhVYyyybCsblRJbkdi9oNU5N00s%2Bi3LkUdDamszpZhRKXsVmw8U1pyHEJoRPYfDIKnYfyV1GSBzFJHue7dTdtbooayxD2yEv%2FQ2PiTuVa0XwzjPUZT%2FmYIyANdiTu4WSunInm4LNbiBunvuJ5nEKexw6Jdnuz02Gp8L9v7DJCd8OFWxE4ShEaHDXww7bDlvAY6pgFSH%2Fe9WAJ%2BGb%2B51lA384%2FEI5WqiguFMNS5Rw5UdYk9OHGFVzosapVqKo7STp4BNP0C5cOUs7lx0jNQ4V828QGdRbavS9zyfYEflgZa84weft%2Fy8hcQNz9OPvWdbJxEF6Pv%2FAb8Z7sbXKL3CdxVi5r8G%2FCuX0ykLHqkz2rwVLMqrmaEKc%2FhvRMhvIVHjUYxMMMEDJMDHQSsIFrc3TARwWC5%2FhmejW69&X-Amz-Signature=a00b9df3b8cb980f66e9ff58ae480990ab69c7c1b447511187569e9d418c1032&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635WYJFTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICknYbgnHTo493PKTNL0zT2EhRRu2Gl0pGPUoMsKNk9AAiBtsRQbd8xv1tMV%2Bs0KD1QOxsvLstwIaITy7jA9Sn5%2FgCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM%2Bu%2BaSsUnFFcZ9t56KtwDa0Gp6O81LCNhNtC3iu8BpAYSL8dBuVT8CdNlaKs8XQl1b8LMc29LrO5ymg5LU2f8SgKV46PhBEYVtD9fwe1kqWg6UoBY%2BLc2YdhtjU%2FcGsoKlcwZ91ReTzz4ZNQvByrML4TviR4yWb0UrJ8iNBNiihgBmT6vWSqAM6sZqDm2JO1z9xOh0gBAHSyqae4PLDvXSHt78JfnFJKxS0qvefhIn7uTQHv8348UqBToZ85P3gmJX4HZ0F1i99zmFetxtOJzjEtn8DAV887GQEZDMJtphtgN15b1JMPyW7265PFmPhsVlve3IWmHBkdn4gp3FbKQKuWEcMEQ0Z5cr9PXehEeGZAtGbcN40sJ%2FSlhhXFloTnfdI%2FIF5OP1JkrzVnqOzUsSPx9cUy0Cam9zzPbZDBiSAqpE8XO2xQHC8CpkZZBszLzRcdSre0H8BXfBtWRPBVI0cjZ%2FAl1K30codg1Af7Eq4GSxbulkjSVfc2L7d2Tqmg1t9l%2Fcs42UQeV7QBFslBm3YHwnpw5clCy9YUKf7JsZ7NYztviajXzPeqOwdjpsZIkKS%2BruCZWbvKGXEj7C95AsucJpfpoKTbCuq6597pwKpb35EFhsVvwW7naaNYjWlnkrAKWDyuvx3J0mnAwxrHlvAY6pgETB7SVdM4HFNVBLyUeb%2FB1oAeCF%2B6NXbgHmwl9vzfkNAN5Y9pmtJ2RkyxICOAWK5eYfCJkUnfCue2or7e16Lq37f7i0vsZ4IihkEO1gSiH6gRssRNqr9XI74R%2FbWFLPojYpAsVEN0xuj1OqZgbTR73ZlAU81t7niTmv7LQHp4WOW1IVqNmjQC7MnfxYhF2qHfng0c%2FY8X5bGk9KqOqJHUQ7tXx5Dyt&X-Amz-Signature=84834115217780e7c35fecebd3a80b0cf63642607e864ab73ec0c58d029541ca&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635WYJFTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICknYbgnHTo493PKTNL0zT2EhRRu2Gl0pGPUoMsKNk9AAiBtsRQbd8xv1tMV%2Bs0KD1QOxsvLstwIaITy7jA9Sn5%2FgCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM%2Bu%2BaSsUnFFcZ9t56KtwDa0Gp6O81LCNhNtC3iu8BpAYSL8dBuVT8CdNlaKs8XQl1b8LMc29LrO5ymg5LU2f8SgKV46PhBEYVtD9fwe1kqWg6UoBY%2BLc2YdhtjU%2FcGsoKlcwZ91ReTzz4ZNQvByrML4TviR4yWb0UrJ8iNBNiihgBmT6vWSqAM6sZqDm2JO1z9xOh0gBAHSyqae4PLDvXSHt78JfnFJKxS0qvefhIn7uTQHv8348UqBToZ85P3gmJX4HZ0F1i99zmFetxtOJzjEtn8DAV887GQEZDMJtphtgN15b1JMPyW7265PFmPhsVlve3IWmHBkdn4gp3FbKQKuWEcMEQ0Z5cr9PXehEeGZAtGbcN40sJ%2FSlhhXFloTnfdI%2FIF5OP1JkrzVnqOzUsSPx9cUy0Cam9zzPbZDBiSAqpE8XO2xQHC8CpkZZBszLzRcdSre0H8BXfBtWRPBVI0cjZ%2FAl1K30codg1Af7Eq4GSxbulkjSVfc2L7d2Tqmg1t9l%2Fcs42UQeV7QBFslBm3YHwnpw5clCy9YUKf7JsZ7NYztviajXzPeqOwdjpsZIkKS%2BruCZWbvKGXEj7C95AsucJpfpoKTbCuq6597pwKpb35EFhsVvwW7naaNYjWlnkrAKWDyuvx3J0mnAwxrHlvAY6pgETB7SVdM4HFNVBLyUeb%2FB1oAeCF%2B6NXbgHmwl9vzfkNAN5Y9pmtJ2RkyxICOAWK5eYfCJkUnfCue2or7e16Lq37f7i0vsZ4IihkEO1gSiH6gRssRNqr9XI74R%2FbWFLPojYpAsVEN0xuj1OqZgbTR73ZlAU81t7niTmv7LQHp4WOW1IVqNmjQC7MnfxYhF2qHfng0c%2FY8X5bGk9KqOqJHUQ7tXx5Dyt&X-Amz-Signature=c2be9b592724e00c75fc221672bcd9de4d76cbee05d119e57b65f7b0284bc1ca&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635WYJFTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICknYbgnHTo493PKTNL0zT2EhRRu2Gl0pGPUoMsKNk9AAiBtsRQbd8xv1tMV%2Bs0KD1QOxsvLstwIaITy7jA9Sn5%2FgCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM%2Bu%2BaSsUnFFcZ9t56KtwDa0Gp6O81LCNhNtC3iu8BpAYSL8dBuVT8CdNlaKs8XQl1b8LMc29LrO5ymg5LU2f8SgKV46PhBEYVtD9fwe1kqWg6UoBY%2BLc2YdhtjU%2FcGsoKlcwZ91ReTzz4ZNQvByrML4TviR4yWb0UrJ8iNBNiihgBmT6vWSqAM6sZqDm2JO1z9xOh0gBAHSyqae4PLDvXSHt78JfnFJKxS0qvefhIn7uTQHv8348UqBToZ85P3gmJX4HZ0F1i99zmFetxtOJzjEtn8DAV887GQEZDMJtphtgN15b1JMPyW7265PFmPhsVlve3IWmHBkdn4gp3FbKQKuWEcMEQ0Z5cr9PXehEeGZAtGbcN40sJ%2FSlhhXFloTnfdI%2FIF5OP1JkrzVnqOzUsSPx9cUy0Cam9zzPbZDBiSAqpE8XO2xQHC8CpkZZBszLzRcdSre0H8BXfBtWRPBVI0cjZ%2FAl1K30codg1Af7Eq4GSxbulkjSVfc2L7d2Tqmg1t9l%2Fcs42UQeV7QBFslBm3YHwnpw5clCy9YUKf7JsZ7NYztviajXzPeqOwdjpsZIkKS%2BruCZWbvKGXEj7C95AsucJpfpoKTbCuq6597pwKpb35EFhsVvwW7naaNYjWlnkrAKWDyuvx3J0mnAwxrHlvAY6pgETB7SVdM4HFNVBLyUeb%2FB1oAeCF%2B6NXbgHmwl9vzfkNAN5Y9pmtJ2RkyxICOAWK5eYfCJkUnfCue2or7e16Lq37f7i0vsZ4IihkEO1gSiH6gRssRNqr9XI74R%2FbWFLPojYpAsVEN0xuj1OqZgbTR73ZlAU81t7niTmv7LQHp4WOW1IVqNmjQC7MnfxYhF2qHfng0c%2FY8X5bGk9KqOqJHUQ7tXx5Dyt&X-Amz-Signature=d9ad1093ef6a7339abac7579c050ac64dd61981abb5489e8c92c36c79ff265b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635WYJFTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICknYbgnHTo493PKTNL0zT2EhRRu2Gl0pGPUoMsKNk9AAiBtsRQbd8xv1tMV%2Bs0KD1QOxsvLstwIaITy7jA9Sn5%2FgCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM%2Bu%2BaSsUnFFcZ9t56KtwDa0Gp6O81LCNhNtC3iu8BpAYSL8dBuVT8CdNlaKs8XQl1b8LMc29LrO5ymg5LU2f8SgKV46PhBEYVtD9fwe1kqWg6UoBY%2BLc2YdhtjU%2FcGsoKlcwZ91ReTzz4ZNQvByrML4TviR4yWb0UrJ8iNBNiihgBmT6vWSqAM6sZqDm2JO1z9xOh0gBAHSyqae4PLDvXSHt78JfnFJKxS0qvefhIn7uTQHv8348UqBToZ85P3gmJX4HZ0F1i99zmFetxtOJzjEtn8DAV887GQEZDMJtphtgN15b1JMPyW7265PFmPhsVlve3IWmHBkdn4gp3FbKQKuWEcMEQ0Z5cr9PXehEeGZAtGbcN40sJ%2FSlhhXFloTnfdI%2FIF5OP1JkrzVnqOzUsSPx9cUy0Cam9zzPbZDBiSAqpE8XO2xQHC8CpkZZBszLzRcdSre0H8BXfBtWRPBVI0cjZ%2FAl1K30codg1Af7Eq4GSxbulkjSVfc2L7d2Tqmg1t9l%2Fcs42UQeV7QBFslBm3YHwnpw5clCy9YUKf7JsZ7NYztviajXzPeqOwdjpsZIkKS%2BruCZWbvKGXEj7C95AsucJpfpoKTbCuq6597pwKpb35EFhsVvwW7naaNYjWlnkrAKWDyuvx3J0mnAwxrHlvAY6pgETB7SVdM4HFNVBLyUeb%2FB1oAeCF%2B6NXbgHmwl9vzfkNAN5Y9pmtJ2RkyxICOAWK5eYfCJkUnfCue2or7e16Lq37f7i0vsZ4IihkEO1gSiH6gRssRNqr9XI74R%2FbWFLPojYpAsVEN0xuj1OqZgbTR73ZlAU81t7niTmv7LQHp4WOW1IVqNmjQC7MnfxYhF2qHfng0c%2FY8X5bGk9KqOqJHUQ7tXx5Dyt&X-Amz-Signature=1f8cfe715fb65071fbc12fc85a40739a80b8052048f23ebc8d6887ec3d1c2991&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635WYJFTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICknYbgnHTo493PKTNL0zT2EhRRu2Gl0pGPUoMsKNk9AAiBtsRQbd8xv1tMV%2Bs0KD1QOxsvLstwIaITy7jA9Sn5%2FgCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM%2Bu%2BaSsUnFFcZ9t56KtwDa0Gp6O81LCNhNtC3iu8BpAYSL8dBuVT8CdNlaKs8XQl1b8LMc29LrO5ymg5LU2f8SgKV46PhBEYVtD9fwe1kqWg6UoBY%2BLc2YdhtjU%2FcGsoKlcwZ91ReTzz4ZNQvByrML4TviR4yWb0UrJ8iNBNiihgBmT6vWSqAM6sZqDm2JO1z9xOh0gBAHSyqae4PLDvXSHt78JfnFJKxS0qvefhIn7uTQHv8348UqBToZ85P3gmJX4HZ0F1i99zmFetxtOJzjEtn8DAV887GQEZDMJtphtgN15b1JMPyW7265PFmPhsVlve3IWmHBkdn4gp3FbKQKuWEcMEQ0Z5cr9PXehEeGZAtGbcN40sJ%2FSlhhXFloTnfdI%2FIF5OP1JkrzVnqOzUsSPx9cUy0Cam9zzPbZDBiSAqpE8XO2xQHC8CpkZZBszLzRcdSre0H8BXfBtWRPBVI0cjZ%2FAl1K30codg1Af7Eq4GSxbulkjSVfc2L7d2Tqmg1t9l%2Fcs42UQeV7QBFslBm3YHwnpw5clCy9YUKf7JsZ7NYztviajXzPeqOwdjpsZIkKS%2BruCZWbvKGXEj7C95AsucJpfpoKTbCuq6597pwKpb35EFhsVvwW7naaNYjWlnkrAKWDyuvx3J0mnAwxrHlvAY6pgETB7SVdM4HFNVBLyUeb%2FB1oAeCF%2B6NXbgHmwl9vzfkNAN5Y9pmtJ2RkyxICOAWK5eYfCJkUnfCue2or7e16Lq37f7i0vsZ4IihkEO1gSiH6gRssRNqr9XI74R%2FbWFLPojYpAsVEN0xuj1OqZgbTR73ZlAU81t7niTmv7LQHp4WOW1IVqNmjQC7MnfxYhF2qHfng0c%2FY8X5bGk9KqOqJHUQ7tXx5Dyt&X-Amz-Signature=351a35d1ee11600f82ef92c801b75a0eaff1614861f91e02f629390ede59d0b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635WYJFTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICknYbgnHTo493PKTNL0zT2EhRRu2Gl0pGPUoMsKNk9AAiBtsRQbd8xv1tMV%2Bs0KD1QOxsvLstwIaITy7jA9Sn5%2FgCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM%2Bu%2BaSsUnFFcZ9t56KtwDa0Gp6O81LCNhNtC3iu8BpAYSL8dBuVT8CdNlaKs8XQl1b8LMc29LrO5ymg5LU2f8SgKV46PhBEYVtD9fwe1kqWg6UoBY%2BLc2YdhtjU%2FcGsoKlcwZ91ReTzz4ZNQvByrML4TviR4yWb0UrJ8iNBNiihgBmT6vWSqAM6sZqDm2JO1z9xOh0gBAHSyqae4PLDvXSHt78JfnFJKxS0qvefhIn7uTQHv8348UqBToZ85P3gmJX4HZ0F1i99zmFetxtOJzjEtn8DAV887GQEZDMJtphtgN15b1JMPyW7265PFmPhsVlve3IWmHBkdn4gp3FbKQKuWEcMEQ0Z5cr9PXehEeGZAtGbcN40sJ%2FSlhhXFloTnfdI%2FIF5OP1JkrzVnqOzUsSPx9cUy0Cam9zzPbZDBiSAqpE8XO2xQHC8CpkZZBszLzRcdSre0H8BXfBtWRPBVI0cjZ%2FAl1K30codg1Af7Eq4GSxbulkjSVfc2L7d2Tqmg1t9l%2Fcs42UQeV7QBFslBm3YHwnpw5clCy9YUKf7JsZ7NYztviajXzPeqOwdjpsZIkKS%2BruCZWbvKGXEj7C95AsucJpfpoKTbCuq6597pwKpb35EFhsVvwW7naaNYjWlnkrAKWDyuvx3J0mnAwxrHlvAY6pgETB7SVdM4HFNVBLyUeb%2FB1oAeCF%2B6NXbgHmwl9vzfkNAN5Y9pmtJ2RkyxICOAWK5eYfCJkUnfCue2or7e16Lq37f7i0vsZ4IihkEO1gSiH6gRssRNqr9XI74R%2FbWFLPojYpAsVEN0xuj1OqZgbTR73ZlAU81t7niTmv7LQHp4WOW1IVqNmjQC7MnfxYhF2qHfng0c%2FY8X5bGk9KqOqJHUQ7tXx5Dyt&X-Amz-Signature=275b6abc6364e3f145db5613c844aacc0ca6c8c6ce2bcd85754d423bd96f691a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TASIA2Z7%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQCca%2B%2BKLIH%2B0amigks7XXE91SmZeYEphW8rMu088xODbgIgFPdaNvqA6XjYPvVvRsGO0oSRuL%2B3yZKUChR2qeRCZAcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIVeTVuh3uY5Qus%2FMyrcA2vPmjA6ngydWqSCWR7wPZekTE1NX4MXy4iHDSiszgQZhHGbE2lVZCB9dRdgFqVBqXoUFue%2Bpxm1XpXG27GUK0ZG5zDBD9oUAN%2FdJiR7yK38flEJMam7T1XsoFZWc82%2FslrbHRfQqPwmXhqGdaWi8ydGamkBjOHt9E36xZZPN%2BownyLbSg475vePnQf2Fhh1Q5j%2BbQccW8GIBwcf0SsU1IY8O8bOYClY8%2FYva40LdYMgEca6YCx6sFioqLs0dNZcqrYcay6FbPiDkz4%2FoLpCMXIqV%2BW%2BljDByobD2qITXGCL4okP2hnVFCOybSlqewI%2B5v4q5BYzJgpTax4EGZGyP3SZQA2a7%2BxR8o5GKegLDAdGyKlBE6lhh44JxdeCuMm4GBqe%2FxhW5C%2FwZ4U5%2BMtNRi5LYlKwsnFmboRTdi1Inr2eWbdnKJGtacDR%2FmqQSBn2W9hHBhKea%2BRCqgLhQkehPPo4g1znv%2BusqvZVVI5VtD%2FlCkECJ%2BUi5%2B7COTCeFQdOImMGaHwqO5ZlYSQ%2Fh69zEUzx3y5rIz4Xx9Xp4NT5RBqNtGUQjEoG2mQ3STHRGnfcX7VISIXQeFDwP52n8PgDIqRogP02rFIk688eQT0d5U8IBfwWLcfSHMVMmJeEMLOw5bwGOqUBLOT4GwG7wX0tQjpVMXObgj%2FtytP2xENpW09SpykCS%2BeOwwYGOO8HsSqtcgKDRi7jeVuAM3x9AT7O533kImYgUAQKzhsykE%2BDjsN1ohE2AX%2F1F5A8Gu8401FefxMAJtz9XcdCOL9W%2B3k2E9eH1bL3r9u1NQ0TaDCktUmN%2F0yWiFyPt7qZGrp4fpcqROdGwWJEB10x1wpLQuB0iChawf0REatAJ0aw&X-Amz-Signature=ed173159c938dc6ecc0e98d74a0e13db54f9c2b1bbe541a049d387110ddd7cca&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XFQBJVB%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIANbpMCOBDC8jkrfkJY9o%2FF0kCm8QO9Dyf95k5FPVYVgAiEAufW%2BfUrDYjp%2FAxV7K5FEvgP9n%2BQPboCcesYu%2FrzYHtkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDAdmBfsFC0sV88cs8ircAyfO3tQvg155JxpZq5uWr2Xy3JcIt5%2FUfF9zxMDUCI4GZ7LgCsox4qXVBdWotbUUo4dSDtncrDq4f%2BDuUox29pLYnTmdoTaznri1u%2FMGzmhNn5Nh9ttyCorbXDpDxmksVr4tqE%2B3y3Im61yba7IKgzUTULxU5S7lqPX%2FKtad9dSHjtE0IapIyv%2FSd64NH%2FLKEYs9JnVQwYR7teU4qe6lht%2FVZIPDv4NNiSowYpN%2FyzUC%2BrCQtI6Tz1K5i5Xq40SChdsnqGZODpt95uVJMeR7aUJhxtZebeCjYn963vgFQhznL40mGmtSkC7KevfnDOjETvXrpYRVFKUslJF7oZKGPXb6ga4gQYWHKmsrYBPb9BpkpLkrE2ivmWT4%2FuGQBC0m7lJ9s8gk2hjmC1ndQ%2BPf5Tt5hbUgwaYbfFR7C5HPY%2BWKJIT7n82SzBJc32TAHZAnWsSknqQJIfJPWza1pbcUkMa62fXkE7hZGG%2FrCISfXE64PeJSygHE%2B3gAtSy8waNo62KoE8T86nJqBQoOJmARNMBhH%2Fu%2F3F%2BtYuEVyUJgKti49j4XvkjCQoUKsqlaf61GdrTMwu4wApxpdXq9RJaOAAHSE4%2FDon12S80opPB2gnGHLco%2BFT3ceoa9Z40WMNuw5bwGOqUBHavQtFhUH6yW1PuZ53otNsAAjnQxObsJZuL5302r0zwFLXyq%2BQeoUfCtO63lD2%2F2BEywPSdhkRF5NQXpTIsmzZMZsX48dK3Q7w3rlQjmpPYl8%2BMiy9dnp%2FMQsiVSCPLrzbsn62%2ByDLML2BNhTf3HUge8u%2B5yJeRHtC1PjGXkUa1DZtkO2Y4ALl%2BuU5twudLpRoafVXrShupiTa5FeJ2LXYgIuCbU&X-Amz-Signature=f4a3299ec388633c46c630cf95a5b602b1b7bafcf2a77887562a2a6ee375d0df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635WYJFTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICknYbgnHTo493PKTNL0zT2EhRRu2Gl0pGPUoMsKNk9AAiBtsRQbd8xv1tMV%2Bs0KD1QOxsvLstwIaITy7jA9Sn5%2FgCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM%2Bu%2BaSsUnFFcZ9t56KtwDa0Gp6O81LCNhNtC3iu8BpAYSL8dBuVT8CdNlaKs8XQl1b8LMc29LrO5ymg5LU2f8SgKV46PhBEYVtD9fwe1kqWg6UoBY%2BLc2YdhtjU%2FcGsoKlcwZ91ReTzz4ZNQvByrML4TviR4yWb0UrJ8iNBNiihgBmT6vWSqAM6sZqDm2JO1z9xOh0gBAHSyqae4PLDvXSHt78JfnFJKxS0qvefhIn7uTQHv8348UqBToZ85P3gmJX4HZ0F1i99zmFetxtOJzjEtn8DAV887GQEZDMJtphtgN15b1JMPyW7265PFmPhsVlve3IWmHBkdn4gp3FbKQKuWEcMEQ0Z5cr9PXehEeGZAtGbcN40sJ%2FSlhhXFloTnfdI%2FIF5OP1JkrzVnqOzUsSPx9cUy0Cam9zzPbZDBiSAqpE8XO2xQHC8CpkZZBszLzRcdSre0H8BXfBtWRPBVI0cjZ%2FAl1K30codg1Af7Eq4GSxbulkjSVfc2L7d2Tqmg1t9l%2Fcs42UQeV7QBFslBm3YHwnpw5clCy9YUKf7JsZ7NYztviajXzPeqOwdjpsZIkKS%2BruCZWbvKGXEj7C95AsucJpfpoKTbCuq6597pwKpb35EFhsVvwW7naaNYjWlnkrAKWDyuvx3J0mnAwxrHlvAY6pgETB7SVdM4HFNVBLyUeb%2FB1oAeCF%2B6NXbgHmwl9vzfkNAN5Y9pmtJ2RkyxICOAWK5eYfCJkUnfCue2or7e16Lq37f7i0vsZ4IihkEO1gSiH6gRssRNqr9XI74R%2FbWFLPojYpAsVEN0xuj1OqZgbTR73ZlAU81t7niTmv7LQHp4WOW1IVqNmjQC7MnfxYhF2qHfng0c%2FY8X5bGk9KqOqJHUQ7tXx5Dyt&X-Amz-Signature=4ed67d67f6246aef9eb1fde7e27f6ffe50b02a4515ba60d252b5b526c1850d32&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635WYJFTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICknYbgnHTo493PKTNL0zT2EhRRu2Gl0pGPUoMsKNk9AAiBtsRQbd8xv1tMV%2Bs0KD1QOxsvLstwIaITy7jA9Sn5%2FgCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM%2Bu%2BaSsUnFFcZ9t56KtwDa0Gp6O81LCNhNtC3iu8BpAYSL8dBuVT8CdNlaKs8XQl1b8LMc29LrO5ymg5LU2f8SgKV46PhBEYVtD9fwe1kqWg6UoBY%2BLc2YdhtjU%2FcGsoKlcwZ91ReTzz4ZNQvByrML4TviR4yWb0UrJ8iNBNiihgBmT6vWSqAM6sZqDm2JO1z9xOh0gBAHSyqae4PLDvXSHt78JfnFJKxS0qvefhIn7uTQHv8348UqBToZ85P3gmJX4HZ0F1i99zmFetxtOJzjEtn8DAV887GQEZDMJtphtgN15b1JMPyW7265PFmPhsVlve3IWmHBkdn4gp3FbKQKuWEcMEQ0Z5cr9PXehEeGZAtGbcN40sJ%2FSlhhXFloTnfdI%2FIF5OP1JkrzVnqOzUsSPx9cUy0Cam9zzPbZDBiSAqpE8XO2xQHC8CpkZZBszLzRcdSre0H8BXfBtWRPBVI0cjZ%2FAl1K30codg1Af7Eq4GSxbulkjSVfc2L7d2Tqmg1t9l%2Fcs42UQeV7QBFslBm3YHwnpw5clCy9YUKf7JsZ7NYztviajXzPeqOwdjpsZIkKS%2BruCZWbvKGXEj7C95AsucJpfpoKTbCuq6597pwKpb35EFhsVvwW7naaNYjWlnkrAKWDyuvx3J0mnAwxrHlvAY6pgETB7SVdM4HFNVBLyUeb%2FB1oAeCF%2B6NXbgHmwl9vzfkNAN5Y9pmtJ2RkyxICOAWK5eYfCJkUnfCue2or7e16Lq37f7i0vsZ4IihkEO1gSiH6gRssRNqr9XI74R%2FbWFLPojYpAsVEN0xuj1OqZgbTR73ZlAU81t7niTmv7LQHp4WOW1IVqNmjQC7MnfxYhF2qHfng0c%2FY8X5bGk9KqOqJHUQ7tXx5Dyt&X-Amz-Signature=f41874365566aada54bc4ba9b06ed18b403679a62e4bce65312801b2d4b9b558&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635WYJFTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICknYbgnHTo493PKTNL0zT2EhRRu2Gl0pGPUoMsKNk9AAiBtsRQbd8xv1tMV%2Bs0KD1QOxsvLstwIaITy7jA9Sn5%2FgCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM%2Bu%2BaSsUnFFcZ9t56KtwDa0Gp6O81LCNhNtC3iu8BpAYSL8dBuVT8CdNlaKs8XQl1b8LMc29LrO5ymg5LU2f8SgKV46PhBEYVtD9fwe1kqWg6UoBY%2BLc2YdhtjU%2FcGsoKlcwZ91ReTzz4ZNQvByrML4TviR4yWb0UrJ8iNBNiihgBmT6vWSqAM6sZqDm2JO1z9xOh0gBAHSyqae4PLDvXSHt78JfnFJKxS0qvefhIn7uTQHv8348UqBToZ85P3gmJX4HZ0F1i99zmFetxtOJzjEtn8DAV887GQEZDMJtphtgN15b1JMPyW7265PFmPhsVlve3IWmHBkdn4gp3FbKQKuWEcMEQ0Z5cr9PXehEeGZAtGbcN40sJ%2FSlhhXFloTnfdI%2FIF5OP1JkrzVnqOzUsSPx9cUy0Cam9zzPbZDBiSAqpE8XO2xQHC8CpkZZBszLzRcdSre0H8BXfBtWRPBVI0cjZ%2FAl1K30codg1Af7Eq4GSxbulkjSVfc2L7d2Tqmg1t9l%2Fcs42UQeV7QBFslBm3YHwnpw5clCy9YUKf7JsZ7NYztviajXzPeqOwdjpsZIkKS%2BruCZWbvKGXEj7C95AsucJpfpoKTbCuq6597pwKpb35EFhsVvwW7naaNYjWlnkrAKWDyuvx3J0mnAwxrHlvAY6pgETB7SVdM4HFNVBLyUeb%2FB1oAeCF%2B6NXbgHmwl9vzfkNAN5Y9pmtJ2RkyxICOAWK5eYfCJkUnfCue2or7e16Lq37f7i0vsZ4IihkEO1gSiH6gRssRNqr9XI74R%2FbWFLPojYpAsVEN0xuj1OqZgbTR73ZlAU81t7niTmv7LQHp4WOW1IVqNmjQC7MnfxYhF2qHfng0c%2FY8X5bGk9KqOqJHUQ7tXx5Dyt&X-Amz-Signature=a642c36bf3d3f215dd292d4f1de00748d41cbdba7441f82e20730d8c6de86a4f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGAYQDDJ%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCICOdHPpAf3ddsdsDUPjSNsJ7Csqqh5GNnd5bvAjf1c0VAiEAs7VSEnEpg99TlGQAqdtTIzxGsOE4XCyg3h8yGMs64j8q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHxRxI2hewXlaQXQ1SrcA3xetXJzk7Kk55sG3ab6WQSxZadG79z1FzD01sMT2DMB8ZzFUGd2zMpVOhWRDzIW82zkl9r1cqdnR3wm32P0Uxj5vTt7A43I05Iq8%2FUsUwB1GqVuJdGLpihujQZTcKzR3knCD3hEMe%2Bnfg7fqtdLyUVx16QwFpgriCLe0sVqBbwDYPd4n9YCj3IGv%2FgLudv1LhZWy3Sv0%2Bh%2F%2BbrrBLs5ZN%2F9Lc%2BTA0kjljEh28uv6pBU6kHW2BylbVqaHwD%2B0DcVCEYqIssPYuw3xOlhkFhlI2HSiKuX1oAVep7OFt8afN%2B0ybC03IA2h8V%2FtyO7TF6H%2FlX50ooTb02IJpfw1MyC%2BcxqTteGnfG8JDZHhEf4SmGx0B%2BfkkMgP8h%2B3Lg8TxvzIdKQ6ZBcdOziSGeyuWe3OoA%2B4kSx1Ejt5%2BbIpwmcO5C0h0Mfd6TEN92QBh%2F8oSGxU1GZK0FuyLFUTmOGfGAcWOoOFKlW%2FDfkdvznAnyZI2gmWP6hOClyb6o6HOaM130TYSTNkH1iZg%2BqnyRHZJUuVggF2zRUHXh5dSovpSLTSotm19DpEon2a2GBHWlgbmSX9yjVdb5bO56TAwsS1zyhChdxIjTYalunMaUkLqBkGwP8YCKM1GB1ockDImzaMO%2Bw5bwGOqUBhYTI3wPBxXJDmv2LGFlql2IQdrAsMVdPIGi7YjcpyWZXykANvJEtx725DMl6d7MLFokrLDDrNxw4wExyJLYLdB2Sl%2Fe36wgXjhaXkWveujk0pUqrLDMg6eay%2FktjEVg0ZZqBUa4ms2pjmYvcIqQYPP8AUqMs6m7IAaI6FdxY%2BT%2FpLcn28eEfSKT%2Bouy9%2FU6hvPw%2B3q3tfNYCUS9p%2BF0IpvUQkC1g&X-Amz-Signature=e143ab0aab460c0623e44a66175205032f549eb6dc7ba5c40eb67ee3f77e9246&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYFYAGFO%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIF6Fx6DsVlJ88emQbGeFQXf38DwaV4zNiehG%2FgaHcdeUAiEA3m1ss%2FxBmqyyZXD0HbFRVbHDB7GqdwqBiEZpTmETPlYq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPj1LtJahUyLfWwkHCrcA8%2B1bwj%2Fr8juoSQHr6p1PHtFBvK3TC6Plpo%2F%2BB7lFO22BH5QeKo7%2B2dusXdClVhHal%2F26aa0iapnPONW%2Bj%2Fp1BHc63QLCjSyLA28JqTt4oIikd%2FC7%2BYKogFgw3R86PZBTIKvJHS0qdYF60RiBRyIfxAb8pPqx4xzcnAYSapkUUGiZmD8f2Xz7QyUN9fI7sHY9tfgu2dWdtwN6fNUaH9TbsyGQ5rQle0vR4r%2FxEl5DisEJ012Y2RnBgdEMVYmXpwHmoO1MUvlGTAhjzxzH0fWVUNiuGAjto6QEYKwhPg%2BdG82WCNBxnI%2FMR1rSODkywNmpQBbSCpZOtuwMrIS2SzeQMBNxXeknITsN5VkE52e%2FMApOXbCz9qnEAShGt13uGlh7nRRoJ1gJcEw2pNdhcPTObFm9MhsK%2B9f9jV5OuMdV1UHjvLXRDfey9B9ant7Xv7Mgvl%2BGGFF8GRvUhSbH8dTUO0u2tsI7LkcteDRVPj0l%2FIqEVBjKX0JfqAOlP8OYfT2xheBUKspKorkcJ0vuSEh2taDcFaWWzgBYQcrvV5THTRVOYThcwsoxnT7c%2FxffKAQ5mrnN351Z7w5Pt6XhizKv3PXXSXEycKc4yDOniWunK2D1GzSD4fl5%2Fa9ONUJMNWw5bwGOqUBgB2YuBhXr8fEyYFTxLKlfE1TSx1OXUFRx7tXVZes%2ByM%2FmGsa7gOF1sR2glkQbKWCoO41TCkXU%2BK%2BqeHDlZzUsKpstXc%2FSz%2B76XsuBKAWe5fjiJX7opGh79K9n6lMJd5hx2129IEqIBRtagCu63VpQK%2BjSKaXdrZ%2BINaV%2F8K0apStEfAnpR0vqLkju1CUu3oksGGzcqYr3GEWKCNaUbmTxl8jjie5&X-Amz-Signature=e501b2053e80e942be7763ac09999be391ca66d004e710500c979ec25268a5ed&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YP5DVPA5%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDBetucReNnCe7WilY0WwqnTTAjq84RNtpKloJ7VKf4xAIhAL7CJqWGBraQmb3NFNnjLAqzdtUIpA0zMt5%2B4TpyqdpsKv8DCH8QABoMNjM3NDIzMTgzODA1IgxDMMUZiwKSNjTWDj4q3AOOIhkmaZVCOHN3FDl%2Fc2xRqPEDz%2FbEkCb9DU7fwnkvwFUkvjCGK%2F6RkhQD4klo%2F4PVC0NEOJJAEgKT6qBpTxbkNnov6iLasf7ofPUPQYhDC9sAf1R%2FIndh0SKdFygNO9weZyTdFBNH7QJtg0PpMfiBFAtx5FBniS9ZBsVP3mViQiouXCbRc0lQmF0rQ2xuiqzT6NK2goJ7qBf1egJEwbD06jSrVi7fb5FwXupZc3Hol2vhAfJWkvndX2r0RMupUYAc%2BsM%2Fhyzfv3KLxW8X2MQZ5LtHmOiWKhHYAoWihxL958sr3EgJcjdq1OfsxtNGvoykDexSd%2BeU4y5N8B70OtYLAnsX1OKGUwDYqKVYuqqx0H52Gt40fpNe9evcDMsmOTteZsXOa8Yc6YkCF36PqNu%2BwTIPHLVKYMqEjtbVuskLNG4BSQ368pKCmnRgGoGnFtTzGmGZmoyq6oaJgt2QgGTJFvG4VokpuJ0MrIP5wCcOpNo%2FKd0HUfFZzktAiHa%2Fyf%2BzxKmwmKtjW4NCQ7XzyhSzlob324ABg2PaiWfMb17aW2PYBIpF0imPktTZZK%2BrYo6ln3BKQ%2BmobUb1VolqCjjhVRkQdZnKLyx0r2c2DXvV0QWhlbNjS6rKOjJlBzDGseW8BjqkAd8cml2%2F9VOY4DciJy8x5ztPVuEAB%2B6B9k7OCdDHeQ8mPHMRbbJKagHFzOpgynIpS2NdaMLBw96ElaAcepwNDVZTBS4%2FQdk%2BEJy3%2BtIhCNh1ipiwnaqlLnJ0CyVBPLN%2BRhx83KLhqAsTTy8Fcazn6Kt84hQIPkjDX%2Fsfi%2FsIPmN2oL3MLpzJUU1tJYh9z0Fy3F3NskKEEhs6pPueASgQ9BTRzxra&X-Amz-Signature=556ea924b87bbfa2e6a8f730e073b2b6baec3f2ca0e7100f4088a935823fef72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634RYX2JA%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCbqfF2pRPh5XaPCLUmXoMJP5OI3HXCnKNa1AK7kjWOFQIhAMN9vjB5bRxwVPGYv2Fgj3oZITY3S%2FGTYn6KfxslfDSIKv8DCH8QABoMNjM3NDIzMTgzODA1IgwwL6gu64xHxQ4kujIq3AOHYCFywChLvUykjyClfOr84gUU6MQ%2BMIP2nRjfuoDomtUMmeWZNMDa2oxuU4m6WS46EuyeojY5aJP00ed7yXkq5VWeC%2Fg6nu%2FLuui%2BsMnSw5lH99%2FBS3f%2FK5%2BPKKzIzCpidUbUqBS1nW9UfcuZme7A4D3gMUeXSfRklQdEUrPPdTiOY3ScN0%2BXXpU5TwoZ3cJpYiJ4nxXOER%2F%2BrSui1wm1pA0xzu%2BcoBfZxqFr6V5EQpcR6aOmuPTg0QiWm33iiZzNZX3ck8KB0hZYl%2FncMnL33gmfQuEwc%2F3ARp3tOCHibIYg7ramJjv7q2h%2Ff96N%2B4rsYzhzTdmeA0KxG4zT%2B1ijYRutvT1%2FdCt8WD0Yab%2Bx8rO3KyIHuuuIldjjbJOjgMoysktt7ixKwoAkT7KXHabXcjuNglgG5xWt7xC%2B5AKu7xIwxMXPKbzs29Sgdi2%2BPHLKsCtcJLvh4II6ddg76tTi4X4fGI0wrwO1PcX70hfk1IViZOE6fITF3gWLBKFkGKQWIsmBQTjx1XYMWXoP8V9c7Lw8SgaWOYhGT0hQCfD75SW8MclzIL3cgpS6U%2FnHb471NdQPmhSqYAa06mr%2BXPPy5XYYCo3mqc1g78mPCnAHzDOEi9ykLbMbYG8q2jCzsOW8BjqkAY6sY7yQdnQosHVwoHRFicIT9DV3khqLy6stH%2BHSNYAoxcKESvg%2FVlUcwM2FpdB05jjXMuqS%2B%2FuIiHOyPGdl6lAdRDznNsAGSUqbuFVGBtQiLfvSmmjelBv%2Fbz%2FXAnHaDOtWH%2F%2FmGfIT%2BBtk9U47IKyiKQltvidF2gveywlEg6ZryL%2B37QdMETy43ev724GjSvNGX34V0L21rj%2FYVorrz8iB9mu7&X-Amz-Signature=cc2dab4ebfaa09bae2ade7f63a265047f9632e6d5139cec6772e736260e9ad3c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634RYX2JA%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQCbqfF2pRPh5XaPCLUmXoMJP5OI3HXCnKNa1AK7kjWOFQIhAMN9vjB5bRxwVPGYv2Fgj3oZITY3S%2FGTYn6KfxslfDSIKv8DCH8QABoMNjM3NDIzMTgzODA1IgwwL6gu64xHxQ4kujIq3AOHYCFywChLvUykjyClfOr84gUU6MQ%2BMIP2nRjfuoDomtUMmeWZNMDa2oxuU4m6WS46EuyeojY5aJP00ed7yXkq5VWeC%2Fg6nu%2FLuui%2BsMnSw5lH99%2FBS3f%2FK5%2BPKKzIzCpidUbUqBS1nW9UfcuZme7A4D3gMUeXSfRklQdEUrPPdTiOY3ScN0%2BXXpU5TwoZ3cJpYiJ4nxXOER%2F%2BrSui1wm1pA0xzu%2BcoBfZxqFr6V5EQpcR6aOmuPTg0QiWm33iiZzNZX3ck8KB0hZYl%2FncMnL33gmfQuEwc%2F3ARp3tOCHibIYg7ramJjv7q2h%2Ff96N%2B4rsYzhzTdmeA0KxG4zT%2B1ijYRutvT1%2FdCt8WD0Yab%2Bx8rO3KyIHuuuIldjjbJOjgMoysktt7ixKwoAkT7KXHabXcjuNglgG5xWt7xC%2B5AKu7xIwxMXPKbzs29Sgdi2%2BPHLKsCtcJLvh4II6ddg76tTi4X4fGI0wrwO1PcX70hfk1IViZOE6fITF3gWLBKFkGKQWIsmBQTjx1XYMWXoP8V9c7Lw8SgaWOYhGT0hQCfD75SW8MclzIL3cgpS6U%2FnHb471NdQPmhSqYAa06mr%2BXPPy5XYYCo3mqc1g78mPCnAHzDOEi9ykLbMbYG8q2jCzsOW8BjqkAY6sY7yQdnQosHVwoHRFicIT9DV3khqLy6stH%2BHSNYAoxcKESvg%2FVlUcwM2FpdB05jjXMuqS%2B%2FuIiHOyPGdl6lAdRDznNsAGSUqbuFVGBtQiLfvSmmjelBv%2Fbz%2FXAnHaDOtWH%2F%2FmGfIT%2BBtk9U47IKyiKQltvidF2gveywlEg6ZryL%2B37QdMETy43ev724GjSvNGX34V0L21rj%2FYVorrz8iB9mu7&X-Amz-Signature=86486178448ebd1aac7d49601dd0b0f02217ed7bfdae39dc38a1075948eb7340&X-Amz-SignedHeaders=host&x-id=GetObject)

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
