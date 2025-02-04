

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTU2HXPN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQDzS8ZLdYxcelbl%2BVvduHzJoM9Cy7QYBPPYf0DU2ILovQIgUjzv4DpNp7x%2FOwwP0gzlE9tR%2BgZqcG9cqhbCn95C6GAq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDJGhzYoYHiz3lKzsmCrcA1acUjvi5n%2FWbjoZpcrXTPVdKIUaGaaR0Hw9SPYeylCNr%2B4NHU%2BrYijwWosQs8QrBcYBdDBS5OZLhDCAVghEYxqjKdYtCNuLos%2B4zQOkYPFiO3%2BXtLOdRHDoNKBRrOW19D9suEM3tHUrVi5w1VXLAkFalBYslxTlttD1WKCzXro%2FGUq4gQLg6VSYURv5rj5ekrImOCtpyybi1FjrFDaKu2bD3tDnARulELcrFa%2FHTNiJuTCae%2FxEcN64xUgREE2Y2cEUj%2BqOgFpP%2Fy2%2FP459FQRMgSAyV0%2BEmcSP0s8bEzn3dz0oIcpFKaguNvbFQIkGWzZvoSRuwHodl8M5Yrnb1KOWRE3UQPwoUgPjbZnQ7ST8klxpuW7U3hY%2FMNFZoKYiFvQElJyx2Qu3tbn7r%2FXuViFIu4XK38y3%2BZgHsSyBGG9ReElGgWamUom8USt6y109KuI7Zks5mubLI563WqcA2OkUug5SHen7TK%2FqBN011A02%2FErDtQDYTmI4ShphwDUsakCrr0f3ELYHDRe9oULFT65LQWwBEsgFqGFyO2LL6aIZlQfeiObgqZqI3ar2nHs2Kq4cvZaews8XqErroGhYu04iBtQ6suVAXidj5Au6Y1yJfYKNEts0Itg4W6C2ML%2B8iL0GOqUBz6VhJ25tdTYi112sfDzJTtHn1%2BY4Lck5iIw4tEri6q8M8AFjeQZPTxlnzlpsgdOBmU2r1ZYH132%2FveTQD1n4HeYC1bbZRCqbYUm5%2F8T3wQh6uDVW9B0lZyLYEx1CjccLyC3JXIJQqysrJBpVwKkCGoz1YhwKcs0ss%2BOCvsLeG0i05xfWGHZuHufUPkskYsSe7HX71z2UIojv5YRBvGqBxBBI1SrY&X-Amz-Signature=374f54672b2a85f87dad548df95c8d2224f580748560168f77d7492bb960105a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTU2HXPN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQDzS8ZLdYxcelbl%2BVvduHzJoM9Cy7QYBPPYf0DU2ILovQIgUjzv4DpNp7x%2FOwwP0gzlE9tR%2BgZqcG9cqhbCn95C6GAq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDJGhzYoYHiz3lKzsmCrcA1acUjvi5n%2FWbjoZpcrXTPVdKIUaGaaR0Hw9SPYeylCNr%2B4NHU%2BrYijwWosQs8QrBcYBdDBS5OZLhDCAVghEYxqjKdYtCNuLos%2B4zQOkYPFiO3%2BXtLOdRHDoNKBRrOW19D9suEM3tHUrVi5w1VXLAkFalBYslxTlttD1WKCzXro%2FGUq4gQLg6VSYURv5rj5ekrImOCtpyybi1FjrFDaKu2bD3tDnARulELcrFa%2FHTNiJuTCae%2FxEcN64xUgREE2Y2cEUj%2BqOgFpP%2Fy2%2FP459FQRMgSAyV0%2BEmcSP0s8bEzn3dz0oIcpFKaguNvbFQIkGWzZvoSRuwHodl8M5Yrnb1KOWRE3UQPwoUgPjbZnQ7ST8klxpuW7U3hY%2FMNFZoKYiFvQElJyx2Qu3tbn7r%2FXuViFIu4XK38y3%2BZgHsSyBGG9ReElGgWamUom8USt6y109KuI7Zks5mubLI563WqcA2OkUug5SHen7TK%2FqBN011A02%2FErDtQDYTmI4ShphwDUsakCrr0f3ELYHDRe9oULFT65LQWwBEsgFqGFyO2LL6aIZlQfeiObgqZqI3ar2nHs2Kq4cvZaews8XqErroGhYu04iBtQ6suVAXidj5Au6Y1yJfYKNEts0Itg4W6C2ML%2B8iL0GOqUBz6VhJ25tdTYi112sfDzJTtHn1%2BY4Lck5iIw4tEri6q8M8AFjeQZPTxlnzlpsgdOBmU2r1ZYH132%2FveTQD1n4HeYC1bbZRCqbYUm5%2F8T3wQh6uDVW9B0lZyLYEx1CjccLyC3JXIJQqysrJBpVwKkCGoz1YhwKcs0ss%2BOCvsLeG0i05xfWGHZuHufUPkskYsSe7HX71z2UIojv5YRBvGqBxBBI1SrY&X-Amz-Signature=0d6b0dccd8afb5aeb13e4630d0dc830716dc066b1f025836c7b830c54e434033&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTU2HXPN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQDzS8ZLdYxcelbl%2BVvduHzJoM9Cy7QYBPPYf0DU2ILovQIgUjzv4DpNp7x%2FOwwP0gzlE9tR%2BgZqcG9cqhbCn95C6GAq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDJGhzYoYHiz3lKzsmCrcA1acUjvi5n%2FWbjoZpcrXTPVdKIUaGaaR0Hw9SPYeylCNr%2B4NHU%2BrYijwWosQs8QrBcYBdDBS5OZLhDCAVghEYxqjKdYtCNuLos%2B4zQOkYPFiO3%2BXtLOdRHDoNKBRrOW19D9suEM3tHUrVi5w1VXLAkFalBYslxTlttD1WKCzXro%2FGUq4gQLg6VSYURv5rj5ekrImOCtpyybi1FjrFDaKu2bD3tDnARulELcrFa%2FHTNiJuTCae%2FxEcN64xUgREE2Y2cEUj%2BqOgFpP%2Fy2%2FP459FQRMgSAyV0%2BEmcSP0s8bEzn3dz0oIcpFKaguNvbFQIkGWzZvoSRuwHodl8M5Yrnb1KOWRE3UQPwoUgPjbZnQ7ST8klxpuW7U3hY%2FMNFZoKYiFvQElJyx2Qu3tbn7r%2FXuViFIu4XK38y3%2BZgHsSyBGG9ReElGgWamUom8USt6y109KuI7Zks5mubLI563WqcA2OkUug5SHen7TK%2FqBN011A02%2FErDtQDYTmI4ShphwDUsakCrr0f3ELYHDRe9oULFT65LQWwBEsgFqGFyO2LL6aIZlQfeiObgqZqI3ar2nHs2Kq4cvZaews8XqErroGhYu04iBtQ6suVAXidj5Au6Y1yJfYKNEts0Itg4W6C2ML%2B8iL0GOqUBz6VhJ25tdTYi112sfDzJTtHn1%2BY4Lck5iIw4tEri6q8M8AFjeQZPTxlnzlpsgdOBmU2r1ZYH132%2FveTQD1n4HeYC1bbZRCqbYUm5%2F8T3wQh6uDVW9B0lZyLYEx1CjccLyC3JXIJQqysrJBpVwKkCGoz1YhwKcs0ss%2BOCvsLeG0i05xfWGHZuHufUPkskYsSe7HX71z2UIojv5YRBvGqBxBBI1SrY&X-Amz-Signature=8f755eda84a7edaac32a8e0647e4c8f14188fd4ff23531f8f990af2ae1c97022&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDR643IO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCzpcg1Z5T9N6Rhf5IDivoKkRLB3IIuEGmPMotDZ3dyEwIhAPXuSIWPwE%2FS%2BI7Wk7nFmqUq70Zhh20hHk62LAQM8LNbKv8DCC8QABoMNjM3NDIzMTgzODA1IgwMiOKhkM3cZNJiJakq3ANMpTNYQU%2FusTqe9s5n%2BGUPd%2FKyvZLqBEVTE27CkCF3HaF3MSV97GF3WaDJo3INNoQnYt1H3YovMzyEUMJBI9AajBK5OjffYvVybTG2Q1rlglG5c6%2FD9IcFcoizML7hoBofFrPhKvvs5238SLdKphcayw8raDStQRhCmXh6mA1zUNrqDvSlqKMLhq6pq6GVW%2BqIKvc0cBjhf0yAYpnsvebOS5jh6PWALVXXRTrvE6wvY8zS6XbScJz1aBnCkxOSxoZXzNGIitZPBXheeDl1yy2RKcNJjbrY9bSo0ur%2FrQxeWOoxRLtu5SisdRXmFSimBEG1NeGMzPo0Hppmk7mDaf14CAqWvYkL6ww%2B%2FkjgNB%2FZxeOSMmAFI3YPBJJD6oCJLEmuPYISqNmS%2FeZgSACIzUuIsxqbzTBVfyQy%2FFAnOfIopwRpuoGlrj%2FYTtVqfSdTgytRydpOfwQn0z1BHv%2BLw9xr5qT9WxoXV7WYkb%2BaOA%2BdVBG4JBanc8%2FkYffaytGM52rOHWQoIN689c4bwF28zIYtVx94PpTXgrR9OwYi6nL7SbyqAulwOSoPwFi6nZk5lAwqoBwJRT0oARVrlENuJzp2FmH8MCCtY0W4UTLtNqYZeRQfpFX7cE2ecM0FjDDfvIi9BjqkAd79kWO%2FLsr6ANqjQykH1EGtrxsqt7emIfJbWECXpogUGyaqWM9IdZIVMKBDKS5Z9up1gPqXP%2FLTM9EpRCHxsl2yHT6D4w9ztjA%2FNHdicpOrsYcwfoC0%2BdOMyZhPGe%2BeHavdzaErVxF1UWC%2B1ITGECcPMVFz%2FbbekdfDZ1PtTRIF1Uqaw7On%2Bj32Cctoso1c188qmQyBo%2FD4xtbYA9YPnF35Y%2F1B&X-Amz-Signature=4615b2ee69af1cbea300b1283693fc9338b599a21933c4c4bae513e5112f84be&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDR643IO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCzpcg1Z5T9N6Rhf5IDivoKkRLB3IIuEGmPMotDZ3dyEwIhAPXuSIWPwE%2FS%2BI7Wk7nFmqUq70Zhh20hHk62LAQM8LNbKv8DCC8QABoMNjM3NDIzMTgzODA1IgwMiOKhkM3cZNJiJakq3ANMpTNYQU%2FusTqe9s5n%2BGUPd%2FKyvZLqBEVTE27CkCF3HaF3MSV97GF3WaDJo3INNoQnYt1H3YovMzyEUMJBI9AajBK5OjffYvVybTG2Q1rlglG5c6%2FD9IcFcoizML7hoBofFrPhKvvs5238SLdKphcayw8raDStQRhCmXh6mA1zUNrqDvSlqKMLhq6pq6GVW%2BqIKvc0cBjhf0yAYpnsvebOS5jh6PWALVXXRTrvE6wvY8zS6XbScJz1aBnCkxOSxoZXzNGIitZPBXheeDl1yy2RKcNJjbrY9bSo0ur%2FrQxeWOoxRLtu5SisdRXmFSimBEG1NeGMzPo0Hppmk7mDaf14CAqWvYkL6ww%2B%2FkjgNB%2FZxeOSMmAFI3YPBJJD6oCJLEmuPYISqNmS%2FeZgSACIzUuIsxqbzTBVfyQy%2FFAnOfIopwRpuoGlrj%2FYTtVqfSdTgytRydpOfwQn0z1BHv%2BLw9xr5qT9WxoXV7WYkb%2BaOA%2BdVBG4JBanc8%2FkYffaytGM52rOHWQoIN689c4bwF28zIYtVx94PpTXgrR9OwYi6nL7SbyqAulwOSoPwFi6nZk5lAwqoBwJRT0oARVrlENuJzp2FmH8MCCtY0W4UTLtNqYZeRQfpFX7cE2ecM0FjDDfvIi9BjqkAd79kWO%2FLsr6ANqjQykH1EGtrxsqt7emIfJbWECXpogUGyaqWM9IdZIVMKBDKS5Z9up1gPqXP%2FLTM9EpRCHxsl2yHT6D4w9ztjA%2FNHdicpOrsYcwfoC0%2BdOMyZhPGe%2BeHavdzaErVxF1UWC%2B1ITGECcPMVFz%2FbbekdfDZ1PtTRIF1Uqaw7On%2Bj32Cctoso1c188qmQyBo%2FD4xtbYA9YPnF35Y%2F1B&X-Amz-Signature=754ff0558126350068a56e43e4ab78b2f1bdc21946545605857a664a35b9bfa8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDR643IO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCzpcg1Z5T9N6Rhf5IDivoKkRLB3IIuEGmPMotDZ3dyEwIhAPXuSIWPwE%2FS%2BI7Wk7nFmqUq70Zhh20hHk62LAQM8LNbKv8DCC8QABoMNjM3NDIzMTgzODA1IgwMiOKhkM3cZNJiJakq3ANMpTNYQU%2FusTqe9s5n%2BGUPd%2FKyvZLqBEVTE27CkCF3HaF3MSV97GF3WaDJo3INNoQnYt1H3YovMzyEUMJBI9AajBK5OjffYvVybTG2Q1rlglG5c6%2FD9IcFcoizML7hoBofFrPhKvvs5238SLdKphcayw8raDStQRhCmXh6mA1zUNrqDvSlqKMLhq6pq6GVW%2BqIKvc0cBjhf0yAYpnsvebOS5jh6PWALVXXRTrvE6wvY8zS6XbScJz1aBnCkxOSxoZXzNGIitZPBXheeDl1yy2RKcNJjbrY9bSo0ur%2FrQxeWOoxRLtu5SisdRXmFSimBEG1NeGMzPo0Hppmk7mDaf14CAqWvYkL6ww%2B%2FkjgNB%2FZxeOSMmAFI3YPBJJD6oCJLEmuPYISqNmS%2FeZgSACIzUuIsxqbzTBVfyQy%2FFAnOfIopwRpuoGlrj%2FYTtVqfSdTgytRydpOfwQn0z1BHv%2BLw9xr5qT9WxoXV7WYkb%2BaOA%2BdVBG4JBanc8%2FkYffaytGM52rOHWQoIN689c4bwF28zIYtVx94PpTXgrR9OwYi6nL7SbyqAulwOSoPwFi6nZk5lAwqoBwJRT0oARVrlENuJzp2FmH8MCCtY0W4UTLtNqYZeRQfpFX7cE2ecM0FjDDfvIi9BjqkAd79kWO%2FLsr6ANqjQykH1EGtrxsqt7emIfJbWECXpogUGyaqWM9IdZIVMKBDKS5Z9up1gPqXP%2FLTM9EpRCHxsl2yHT6D4w9ztjA%2FNHdicpOrsYcwfoC0%2BdOMyZhPGe%2BeHavdzaErVxF1UWC%2B1ITGECcPMVFz%2FbbekdfDZ1PtTRIF1Uqaw7On%2Bj32Cctoso1c188qmQyBo%2FD4xtbYA9YPnF35Y%2F1B&X-Amz-Signature=c087aa1ab37179e1515cbe64f194d9a8c570064517e9f269b9acf2802a718b96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDR643IO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCzpcg1Z5T9N6Rhf5IDivoKkRLB3IIuEGmPMotDZ3dyEwIhAPXuSIWPwE%2FS%2BI7Wk7nFmqUq70Zhh20hHk62LAQM8LNbKv8DCC8QABoMNjM3NDIzMTgzODA1IgwMiOKhkM3cZNJiJakq3ANMpTNYQU%2FusTqe9s5n%2BGUPd%2FKyvZLqBEVTE27CkCF3HaF3MSV97GF3WaDJo3INNoQnYt1H3YovMzyEUMJBI9AajBK5OjffYvVybTG2Q1rlglG5c6%2FD9IcFcoizML7hoBofFrPhKvvs5238SLdKphcayw8raDStQRhCmXh6mA1zUNrqDvSlqKMLhq6pq6GVW%2BqIKvc0cBjhf0yAYpnsvebOS5jh6PWALVXXRTrvE6wvY8zS6XbScJz1aBnCkxOSxoZXzNGIitZPBXheeDl1yy2RKcNJjbrY9bSo0ur%2FrQxeWOoxRLtu5SisdRXmFSimBEG1NeGMzPo0Hppmk7mDaf14CAqWvYkL6ww%2B%2FkjgNB%2FZxeOSMmAFI3YPBJJD6oCJLEmuPYISqNmS%2FeZgSACIzUuIsxqbzTBVfyQy%2FFAnOfIopwRpuoGlrj%2FYTtVqfSdTgytRydpOfwQn0z1BHv%2BLw9xr5qT9WxoXV7WYkb%2BaOA%2BdVBG4JBanc8%2FkYffaytGM52rOHWQoIN689c4bwF28zIYtVx94PpTXgrR9OwYi6nL7SbyqAulwOSoPwFi6nZk5lAwqoBwJRT0oARVrlENuJzp2FmH8MCCtY0W4UTLtNqYZeRQfpFX7cE2ecM0FjDDfvIi9BjqkAd79kWO%2FLsr6ANqjQykH1EGtrxsqt7emIfJbWECXpogUGyaqWM9IdZIVMKBDKS5Z9up1gPqXP%2FLTM9EpRCHxsl2yHT6D4w9ztjA%2FNHdicpOrsYcwfoC0%2BdOMyZhPGe%2BeHavdzaErVxF1UWC%2B1ITGECcPMVFz%2FbbekdfDZ1PtTRIF1Uqaw7On%2Bj32Cctoso1c188qmQyBo%2FD4xtbYA9YPnF35Y%2F1B&X-Amz-Signature=4ebad6007e1904a2fa60b31e2c266eab7482a887e752ef83d6590c21415eb472&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDR643IO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCzpcg1Z5T9N6Rhf5IDivoKkRLB3IIuEGmPMotDZ3dyEwIhAPXuSIWPwE%2FS%2BI7Wk7nFmqUq70Zhh20hHk62LAQM8LNbKv8DCC8QABoMNjM3NDIzMTgzODA1IgwMiOKhkM3cZNJiJakq3ANMpTNYQU%2FusTqe9s5n%2BGUPd%2FKyvZLqBEVTE27CkCF3HaF3MSV97GF3WaDJo3INNoQnYt1H3YovMzyEUMJBI9AajBK5OjffYvVybTG2Q1rlglG5c6%2FD9IcFcoizML7hoBofFrPhKvvs5238SLdKphcayw8raDStQRhCmXh6mA1zUNrqDvSlqKMLhq6pq6GVW%2BqIKvc0cBjhf0yAYpnsvebOS5jh6PWALVXXRTrvE6wvY8zS6XbScJz1aBnCkxOSxoZXzNGIitZPBXheeDl1yy2RKcNJjbrY9bSo0ur%2FrQxeWOoxRLtu5SisdRXmFSimBEG1NeGMzPo0Hppmk7mDaf14CAqWvYkL6ww%2B%2FkjgNB%2FZxeOSMmAFI3YPBJJD6oCJLEmuPYISqNmS%2FeZgSACIzUuIsxqbzTBVfyQy%2FFAnOfIopwRpuoGlrj%2FYTtVqfSdTgytRydpOfwQn0z1BHv%2BLw9xr5qT9WxoXV7WYkb%2BaOA%2BdVBG4JBanc8%2FkYffaytGM52rOHWQoIN689c4bwF28zIYtVx94PpTXgrR9OwYi6nL7SbyqAulwOSoPwFi6nZk5lAwqoBwJRT0oARVrlENuJzp2FmH8MCCtY0W4UTLtNqYZeRQfpFX7cE2ecM0FjDDfvIi9BjqkAd79kWO%2FLsr6ANqjQykH1EGtrxsqt7emIfJbWECXpogUGyaqWM9IdZIVMKBDKS5Z9up1gPqXP%2FLTM9EpRCHxsl2yHT6D4w9ztjA%2FNHdicpOrsYcwfoC0%2BdOMyZhPGe%2BeHavdzaErVxF1UWC%2B1ITGECcPMVFz%2FbbekdfDZ1PtTRIF1Uqaw7On%2Bj32Cctoso1c188qmQyBo%2FD4xtbYA9YPnF35Y%2F1B&X-Amz-Signature=4f077389088c4515cc612d0b20b04b1405a013a1b98bc34148a65ffd47231e45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDR643IO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCzpcg1Z5T9N6Rhf5IDivoKkRLB3IIuEGmPMotDZ3dyEwIhAPXuSIWPwE%2FS%2BI7Wk7nFmqUq70Zhh20hHk62LAQM8LNbKv8DCC8QABoMNjM3NDIzMTgzODA1IgwMiOKhkM3cZNJiJakq3ANMpTNYQU%2FusTqe9s5n%2BGUPd%2FKyvZLqBEVTE27CkCF3HaF3MSV97GF3WaDJo3INNoQnYt1H3YovMzyEUMJBI9AajBK5OjffYvVybTG2Q1rlglG5c6%2FD9IcFcoizML7hoBofFrPhKvvs5238SLdKphcayw8raDStQRhCmXh6mA1zUNrqDvSlqKMLhq6pq6GVW%2BqIKvc0cBjhf0yAYpnsvebOS5jh6PWALVXXRTrvE6wvY8zS6XbScJz1aBnCkxOSxoZXzNGIitZPBXheeDl1yy2RKcNJjbrY9bSo0ur%2FrQxeWOoxRLtu5SisdRXmFSimBEG1NeGMzPo0Hppmk7mDaf14CAqWvYkL6ww%2B%2FkjgNB%2FZxeOSMmAFI3YPBJJD6oCJLEmuPYISqNmS%2FeZgSACIzUuIsxqbzTBVfyQy%2FFAnOfIopwRpuoGlrj%2FYTtVqfSdTgytRydpOfwQn0z1BHv%2BLw9xr5qT9WxoXV7WYkb%2BaOA%2BdVBG4JBanc8%2FkYffaytGM52rOHWQoIN689c4bwF28zIYtVx94PpTXgrR9OwYi6nL7SbyqAulwOSoPwFi6nZk5lAwqoBwJRT0oARVrlENuJzp2FmH8MCCtY0W4UTLtNqYZeRQfpFX7cE2ecM0FjDDfvIi9BjqkAd79kWO%2FLsr6ANqjQykH1EGtrxsqt7emIfJbWECXpogUGyaqWM9IdZIVMKBDKS5Z9up1gPqXP%2FLTM9EpRCHxsl2yHT6D4w9ztjA%2FNHdicpOrsYcwfoC0%2BdOMyZhPGe%2BeHavdzaErVxF1UWC%2B1ITGECcPMVFz%2FbbekdfDZ1PtTRIF1Uqaw7On%2Bj32Cctoso1c188qmQyBo%2FD4xtbYA9YPnF35Y%2F1B&X-Amz-Signature=dc0c6e04011e4cbc2deef1f396065fca060da1411554aa3dc28c966ea6a23dd9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OXC7UHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQDJhagAWqe24esWM4l4f%2BgLzbWjWp4KsLw%2BEo8%2FR3oJ1AIgJjZjyrDthL0zM0LGrciVg7VW3Ffc%2BtVrR9bB33%2BPH%2Fkq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDOUrOVspnIhbLeXnGircAwWkqQbtZJpEkRPXPlP8lg%2FCFbrKOhMhI0VSDK7bvYSjgGWLjz7BlNNbyQj3qI8nZIC%2BtJdQkB8TIKMp1Ei5ZKsJFDzZvopa7H1l9vsc60%2FKsCuX%2FD0PdlZxdS1VGIkdgKpDV3ZpWpaerP3FfoJvLLkPAJIaBk3AtkphWcjO2Y5lZeibQS5u%2BuPkyBZU0CCG3dt443pSweOVkIV%2BgW59BoqzyYLy%2BY%2BDmqfGrmBRzRutT%2FOHSsoLMgf86TN3TPOriGj5BBLmCsnF19S3DAH94A36UVPTTfJtZ1FQ8ot7r5aNvaEVehqxQD1tn%2BzszBfDCetQsDnzCM79TFRxmP8%2BDRC5Ni4hTF28OqBhNXeRT%2BU%2FY1RSYlDQLSZ9wsrLozkLaKNiAfRwHd3A6mMZ%2FHscMAZIM5pvw6LwJRy1Y9OM1yK51pYIPmKEfelHGj%2F%2FZh7glBtuALPVRecmRn7V5hI%2BfBm4aRzUPFWAlRLfS5jtQaV1kwCsaI3SAsiO%2BO0zcLJRU5fI8vV5t7HslJQSBjb8m872sVmZO8aU6a0bk%2BmLYN3lSJzNseqpaX2x8DrZAHQI3%2FIFjfV5p9hLBWIU%2B6r7QDuCpynxNEWCee8yG3fSIjc03OEzsCC1OkuVNwY9MN68iL0GOqUBOxxHP2uQ9t7CIBi1GQW2k7sDP8QYD3B2%2Bbpco8B67eWd0p8vKIL3tdVYF9zqRnfbnOMoVvs7OQFfjmrcKlMPY1qYlGnRdANehfKbYr0eo2t5jhpt9wxfNZSTwgD4SVZR%2FFp8S232f9lrP339k9xaPVEQ5vVftqPV4w9GpTAykaENNHn72rrxEh85ZUyvWIW%2F%2F7X7VogOqzOJj29Mw4alUFMELRTe&X-Amz-Signature=5be6fb22f532f6319c3a3884bf60652369beebbe5557f131b77a8bded2b445a7&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5V2QFOW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQDr09fXF%2Bb8R2MmNLHFDVVvgqFsnZCClWo0kW7iZKfsrwIgYueTwUaKRa2kmF5HabBn1vzwA25Bw23oPLcrIey3w10q%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDAB9XzOzR8ThorKxgCrcA6ywimjZ3nzf25u9EBlAHBCfY%2BoOqBb8sG%2Bt6JpkLZiSbiu9nxHllgktR7WvRZ%2BoDj864kzb6MaUmc2X43W4msJbqvhHvXz5a4A0aD0tEwH9HS9kzBpW0CUWLj4sKAqWQTMa2wZsua878hA4FTWs0zj2YgrtfArEyYES9p8fkQl%2FRJ529CXSLG5FDiKjRc6ANJ%2FzTTqcuX8FUmpbDo%2BSGvbQ0qCC35lnDFSkcGi0%2BuhkGuyGsnWKc1hzz9FvNly4xctVcrqsszSKoEi0Ad1qB1Z4M1Bsn4Yi0ah24tT%2FA91LD7MUNKHcLTmcg%2BxgGAIrpsA60LNfyZ4bNLpMx4yVEQF%2ByloDiDUFpXuzas0BuSORcd%2FOUMi31P39kUkdGZWaVjuqtCaADIWsTdFG9Yi6GU88ebtegVbtg6sUwynkKcdl6%2FAovG7vu64wvhyCdkPL3N9qifvTHu2N%2FCnc5c2R8DoZejgSLU9dLzpB6Xm0tDnAZNLx1Ln7I7BmYVN4bJcvdL1GDRiRoq5dKxCENr2gxLK5Ah5MpaLcxa7PsyEeBszqHk%2Bxd9krf9Jj9x%2BlPOl7gTT9Yvkb6KqqeNLgddvKiN5FxwnTBTKS6f9P%2FlW7OqHRZNG17ksegbpuafbYMIG9iL0GOqUBqhdAUfLKUqQ%2Bt7jIwyWADh9fQVaY3%2FGD56l0b75NmuYAzDKUPGScGQRC5853Zew%2BNAgvdc6e1%2BZsnRthi%2B3KIk6Jr9RWoKN4Jln5MwYyI71I8RKgdkLNFy60rwh4yBoarccMrPvf1A7rihVdKn9qnG8EkGxS9mzL2LvO197okTJjDX%2BexSbDqpHB246%2B25bXwK2R5L0M6lfQij41Ftft1WYcD7ar&X-Amz-Signature=dd4bcd1be8efe84f6171e197032907c50ef2ffb8da4fc3b7d086698e1f7729f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDR643IO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCzpcg1Z5T9N6Rhf5IDivoKkRLB3IIuEGmPMotDZ3dyEwIhAPXuSIWPwE%2FS%2BI7Wk7nFmqUq70Zhh20hHk62LAQM8LNbKv8DCC8QABoMNjM3NDIzMTgzODA1IgwMiOKhkM3cZNJiJakq3ANMpTNYQU%2FusTqe9s5n%2BGUPd%2FKyvZLqBEVTE27CkCF3HaF3MSV97GF3WaDJo3INNoQnYt1H3YovMzyEUMJBI9AajBK5OjffYvVybTG2Q1rlglG5c6%2FD9IcFcoizML7hoBofFrPhKvvs5238SLdKphcayw8raDStQRhCmXh6mA1zUNrqDvSlqKMLhq6pq6GVW%2BqIKvc0cBjhf0yAYpnsvebOS5jh6PWALVXXRTrvE6wvY8zS6XbScJz1aBnCkxOSxoZXzNGIitZPBXheeDl1yy2RKcNJjbrY9bSo0ur%2FrQxeWOoxRLtu5SisdRXmFSimBEG1NeGMzPo0Hppmk7mDaf14CAqWvYkL6ww%2B%2FkjgNB%2FZxeOSMmAFI3YPBJJD6oCJLEmuPYISqNmS%2FeZgSACIzUuIsxqbzTBVfyQy%2FFAnOfIopwRpuoGlrj%2FYTtVqfSdTgytRydpOfwQn0z1BHv%2BLw9xr5qT9WxoXV7WYkb%2BaOA%2BdVBG4JBanc8%2FkYffaytGM52rOHWQoIN689c4bwF28zIYtVx94PpTXgrR9OwYi6nL7SbyqAulwOSoPwFi6nZk5lAwqoBwJRT0oARVrlENuJzp2FmH8MCCtY0W4UTLtNqYZeRQfpFX7cE2ecM0FjDDfvIi9BjqkAd79kWO%2FLsr6ANqjQykH1EGtrxsqt7emIfJbWECXpogUGyaqWM9IdZIVMKBDKS5Z9up1gPqXP%2FLTM9EpRCHxsl2yHT6D4w9ztjA%2FNHdicpOrsYcwfoC0%2BdOMyZhPGe%2BeHavdzaErVxF1UWC%2B1ITGECcPMVFz%2FbbekdfDZ1PtTRIF1Uqaw7On%2Bj32Cctoso1c188qmQyBo%2FD4xtbYA9YPnF35Y%2F1B&X-Amz-Signature=5c945ace3e3978356d56397d0b5472e6abadf3550e9e36ea3b0b1a618d0827cd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDR643IO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCzpcg1Z5T9N6Rhf5IDivoKkRLB3IIuEGmPMotDZ3dyEwIhAPXuSIWPwE%2FS%2BI7Wk7nFmqUq70Zhh20hHk62LAQM8LNbKv8DCC8QABoMNjM3NDIzMTgzODA1IgwMiOKhkM3cZNJiJakq3ANMpTNYQU%2FusTqe9s5n%2BGUPd%2FKyvZLqBEVTE27CkCF3HaF3MSV97GF3WaDJo3INNoQnYt1H3YovMzyEUMJBI9AajBK5OjffYvVybTG2Q1rlglG5c6%2FD9IcFcoizML7hoBofFrPhKvvs5238SLdKphcayw8raDStQRhCmXh6mA1zUNrqDvSlqKMLhq6pq6GVW%2BqIKvc0cBjhf0yAYpnsvebOS5jh6PWALVXXRTrvE6wvY8zS6XbScJz1aBnCkxOSxoZXzNGIitZPBXheeDl1yy2RKcNJjbrY9bSo0ur%2FrQxeWOoxRLtu5SisdRXmFSimBEG1NeGMzPo0Hppmk7mDaf14CAqWvYkL6ww%2B%2FkjgNB%2FZxeOSMmAFI3YPBJJD6oCJLEmuPYISqNmS%2FeZgSACIzUuIsxqbzTBVfyQy%2FFAnOfIopwRpuoGlrj%2FYTtVqfSdTgytRydpOfwQn0z1BHv%2BLw9xr5qT9WxoXV7WYkb%2BaOA%2BdVBG4JBanc8%2FkYffaytGM52rOHWQoIN689c4bwF28zIYtVx94PpTXgrR9OwYi6nL7SbyqAulwOSoPwFi6nZk5lAwqoBwJRT0oARVrlENuJzp2FmH8MCCtY0W4UTLtNqYZeRQfpFX7cE2ecM0FjDDfvIi9BjqkAd79kWO%2FLsr6ANqjQykH1EGtrxsqt7emIfJbWECXpogUGyaqWM9IdZIVMKBDKS5Z9up1gPqXP%2FLTM9EpRCHxsl2yHT6D4w9ztjA%2FNHdicpOrsYcwfoC0%2BdOMyZhPGe%2BeHavdzaErVxF1UWC%2B1ITGECcPMVFz%2FbbekdfDZ1PtTRIF1Uqaw7On%2Bj32Cctoso1c188qmQyBo%2FD4xtbYA9YPnF35Y%2F1B&X-Amz-Signature=ac78c84fe5dbc12cf25f3601d9b3d53221b24b93b658baf7bd2671a7fa7a868e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDR643IO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCzpcg1Z5T9N6Rhf5IDivoKkRLB3IIuEGmPMotDZ3dyEwIhAPXuSIWPwE%2FS%2BI7Wk7nFmqUq70Zhh20hHk62LAQM8LNbKv8DCC8QABoMNjM3NDIzMTgzODA1IgwMiOKhkM3cZNJiJakq3ANMpTNYQU%2FusTqe9s5n%2BGUPd%2FKyvZLqBEVTE27CkCF3HaF3MSV97GF3WaDJo3INNoQnYt1H3YovMzyEUMJBI9AajBK5OjffYvVybTG2Q1rlglG5c6%2FD9IcFcoizML7hoBofFrPhKvvs5238SLdKphcayw8raDStQRhCmXh6mA1zUNrqDvSlqKMLhq6pq6GVW%2BqIKvc0cBjhf0yAYpnsvebOS5jh6PWALVXXRTrvE6wvY8zS6XbScJz1aBnCkxOSxoZXzNGIitZPBXheeDl1yy2RKcNJjbrY9bSo0ur%2FrQxeWOoxRLtu5SisdRXmFSimBEG1NeGMzPo0Hppmk7mDaf14CAqWvYkL6ww%2B%2FkjgNB%2FZxeOSMmAFI3YPBJJD6oCJLEmuPYISqNmS%2FeZgSACIzUuIsxqbzTBVfyQy%2FFAnOfIopwRpuoGlrj%2FYTtVqfSdTgytRydpOfwQn0z1BHv%2BLw9xr5qT9WxoXV7WYkb%2BaOA%2BdVBG4JBanc8%2FkYffaytGM52rOHWQoIN689c4bwF28zIYtVx94PpTXgrR9OwYi6nL7SbyqAulwOSoPwFi6nZk5lAwqoBwJRT0oARVrlENuJzp2FmH8MCCtY0W4UTLtNqYZeRQfpFX7cE2ecM0FjDDfvIi9BjqkAd79kWO%2FLsr6ANqjQykH1EGtrxsqt7emIfJbWECXpogUGyaqWM9IdZIVMKBDKS5Z9up1gPqXP%2FLTM9EpRCHxsl2yHT6D4w9ztjA%2FNHdicpOrsYcwfoC0%2BdOMyZhPGe%2BeHavdzaErVxF1UWC%2B1ITGECcPMVFz%2FbbekdfDZ1PtTRIF1Uqaw7On%2Bj32Cctoso1c188qmQyBo%2FD4xtbYA9YPnF35Y%2F1B&X-Amz-Signature=bcf43606a3187dfa316c5277a04211cefcfafb9fedd49137bc95119940001ab5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5JEBJWE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIB1Jaxzh%2B8a5dL9Sz2DC6Q%2BurHvlGUgfPkKF4Z9kRYFxAiEAtaQarcGnYOZRSO9avvkwuJqLTxYrn9ZFyYfqtPi9dRMq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDN8ebNAxLqd1wfWwkSrcAxrjnxIcDHgPXvaJ6I2jaMgxU8qhUFpX2JDbeTn86V%2BY1TZNfT%2F8XCAx388Ub6CZyQPQUkHnz%2B5%2F%2FIHv%2FOmCepYXXfp9uUTm2Sii4tCFz5h4iVdN%2BJLm0bbhf82AsP4kUWixPuGGhvL1jla9eyuvkLnyN%2FrpFDTmyAQODMk%2B02fDSm4p6MsiWDPigMcKNpBOyXymeOywH9aNtsP39PqaNEwapGWrmoz1duOjbhIcutym1AhlMkY5H9Yi59pfrDiTxBvTEwmbrC7dckX80IUjSJ%2BEzVHZmqnBEKYnqfz3BGnzjwM%2FMjw0X5v3XAXZySBXYfDbx%2BrDzjFyv%2FM77gw4GNUFoGgvpFyv8ZfTuT2AFbDX7GF4Q9n%2BsIiivLTYy%2BKVnEhCXhQviJSmN6cn9Xb3pl%2BCB2YTv7xf5jchK41I5ksFIUV5iRp74CeYs%2BAj53lJCJLSNV8HQ33fmdku9xWkbiyJNTGutKrlGEP1vpgR%2FV9JzbHAoRLuQR%2BUftpaapLUPCPWDoBAyHiUXyut75ixECyitqAQMkbOvgYB5ryvwtdR0Nt9queUFD5Vf0%2FlL4HxvyAwv990M6d9bimB9Xeos4IqKoZIEreLYQg0Xy4m%2FOZtQGpOcJI32tGo3hqTMLW8iL0GOqUBwwY7KPw064MnD5wmoocTxHYAYaG02t%2B%2Fd3MCeVqesjtbvqF9ix6qBzIAblUCpdFBu8WtSOz%2FV1Q38UsXl7o20N1D%2FmmwC64MPNSQFCE%2FwxUt%2F9CHmtSl8o7ck5C6MZtwEvlFlZaIuoeAetJcc2OXd6SRKQm5z8LsO6jbPN1XQ1nbVaCgnYbqvpXO5e8Zh1yUXEl6fwU7QsluOadeecLnE8G1ekRJ&X-Amz-Signature=b859dab71a1b12cc157198d7400a571396d437e103e78cff511353f528a7e283&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RIY5QEE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIHBbbO1rxVWdt%2FvfsDsDY94suV%2BCdnsMFqXuBHubL%2FdqAiBtNlP3W2nRJOwSsHvOauD1oq9tzLmSV%2BE3W4zRbTuqsir%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMm9f4o129CCfCarNVKtwDXw%2FIyXXBWd5WfaWF424sNV7zYF4imGFKm7zyZoJfuslWcFfwEJcRIrZXcFM4k0c3ZrT0mippnaa8LZXhOuJOqqIUOIWK0%2BzCduEIY59cWS90FQO3epeIkkASIRhZ%2Fhb0UBhdqsceWhp9yrDCt6pKn08pKrfKEIa87C2J1ZAvywlEUJONhq2I%2FFnT8zDbXHe2vhhLu%2FbuuYNu86KuvueqTS4B8bzuqE6CPeAEVuOWvnoIA%2FPppu8fAaGuhF%2Bol9Nk9hvKWgcQuD0P8L5LlamNvDNVKdePrzkq9DpVP8Gao8%2BuwURHEPFTZFtiBIKjMWHDrMMZjssZxKp8Z%2F6%2BdQ17s1KrK4R%2Fnwa%2BgfM%2BH432UJ7tFmTA2SG1wICipoKleY3SryE1T52wdqWNslxG3hqFiV2Bhw36ILuk9%2FH6SVAw9fZx49GDh9WlrtTc%2FXizVPQf%2FmvS0esmfHsYq4bs8fSVSATlxlE1%2BlaG963YA4IgLgdyYSRMp9Bf%2BmvKO%2BNR6ZgYfi3p47BKGMK1FwgFYAtRrRr8%2FDslzxYLkwiQfLbwL305CrLCWOkhrm7qaO2d5IIDyAKCuQjbvjSe2%2BXW9YPMCMO8n2qvOVvUBA7izMaHJvbK215wl8uoRRZo0Mowmr2IvQY6pgGiK4TwqaJP3LWD5LlOHnRDeSIx65AfZ%2B6VQb%2FeereHL03DTgDkZBPyyDM%2FLxHwpa2zmlLopdpRmDQ7xKtX9Cn0jXAFSIPYXgb0K%2FsFSw7K4b2QldSCD%2Fb1qFTy4b08QULXXLB814y4sDA7y15t5AGk680U3BYUOtYnDjqfM6xJr8gCAgCUKp5dRQTE19tAAhhbVbl21ntqsHw0SUIvaLCFtxDIvxDX&X-Amz-Signature=27c5c7ae34a7e420b72545309c5db5825914360f2e2e2c454193c9709ce6f45a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTWSMR3W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCt7qzkjnWJioQqys9vK%2FsYN6NHp%2BWTRgSqJpJ4eMqcXwIhAKwDPmWyMmcKSl0kNv%2FcyeVLQ9%2FN%2FQHCQo0uKtT2YZVbKv8DCC8QABoMNjM3NDIzMTgzODA1IgxxqwMYgF8WMoVUItQq3AOKjPPwdar0eu%2FYYS8YVSYEAWP3YwDurqZh6eHINJk%2BQCa0qnAcPufxYl7R2XnM%2BcflTPpFUuI6FCeYIeWs5P6kghCSymaL6dTDrrnn6qaxoRhFZrdqrYa8J%2BOtME7BARmRNK%2F%2BVVLzQFMlqPZ1VKF7ElYjW8X1rdFf7E8r%2FN15nvE48o6qrHXAlHl9Le9dXd5vudLanA6yXwzVimK0gJgfPoPuGKVR8GJ9p%2B4e0MeLUZ7Ilh4mLLKz4FODf0iaHObunpimMZ%2BEuC6xmYKDdGF91bx80C89ZYvOOHZfRCyqqUEvNAKC0d%2FlVBkpawFsSEtWRHoF9%2F0%2BqEoohNyAAfjccyViWMfzDyvy%2BUoKv96X%2BWAIdMT4aUw9xCvlJkPn0I5ZLbFBi%2FYowIb%2B%2FAcV9I2QMshUnPHneXcrhsWX02Oj9zdmiM4WUbWuBdzrOsBqlh%2FV3ioycwksDhnqawvwL0D0RnnzE%2F7Tnu6Dk4ZVaW3uqFehg%2F9Sd4oziX071jHbe0iu0w1CSc55%2BGEdCcllm85JSpd52FYJy3i45Kpib7S8rqP4nXHYEHcHbnahsjSQd7%2FyVIGN%2FQVxbiNhWz1K2k7tstkZ1uz1gVHSbj4XYgSJhhzf8xrxO%2FM4idN%2FnjDKvIi9BjqkATo1of9umtkh1JY4dW1tBd8GTYNy3LD7NuJHZ8d7ExgJb130xhWOP6q1ZnPVyOFxyuTBUAKqnQEGPrX6%2BPB3qf55MyrwrM0Rho8dtgBL7LCEASfXASYv8RhLuTnHJWXvxTZk0apdDFGK819Kx6sjtDtV94Sf9mg%2B2YcRfeW75EXvgNUKvkU30URrFOfrmRZbq%2F2Ykr5Vwze5Q7D5NTziDVMy9nVn&X-Amz-Signature=c68860e5b459037d4435999d2d1cc85df2c13e6a0820e8bb385cb52f71bba243&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZFW6F2I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCsro%2FLVaHRlZtjT0cn3XbFzVAnItMSefYf8sjPaZ638wIhAInHtLscVUpkyLDRu0rNXPgYiW9I4gUQZuR0wy5LOTDhKv8DCC8QABoMNjM3NDIzMTgzODA1IgzIP%2FKJ2Howzs%2FjC84q3AOGnTSb54pLVFEz4VQLWoS2JNNXueZFTyY4Y8B8Ya8J7sdN1U1qw3%2Bs2iRyvHvSg8ZzgnQPxOiZcb8BqHp8E0K4lBS8UTKtRp1jqzP3aD2tLgsC0Xj6HnCMBviYGqb%2BLazpipzHRD9TsZ38HD%2FH2jIz0JV3%2Bv8C7dUCxX4%2FI64qrbfq3PZwMGNZqWKikLHo0ns%2BZGCLMIDdCrk4%2BNqCQ9II1SsMAq1afC3TrnOqluZ%2FdHweIV1M9EJdpYGzuRC7IWfYV%2BirpNo1KFznzRdbYj9AzR5pIkL%2B2efB%2FSWyorLXpRq8ZrOVYkc5znn%2F%2Fmm%2FmG8CuNiBFqeuY0NJFpJ0AtSTYjQkquZtq%2FQcfCQiDenkl%2FhmXNlmKXEY6t%2BO0Z3UbgRzQFBrCjhMc%2BuP7stLWn46pWqikRib0LmyZPr6dywSTavXASc%2B8A0szwmO2Rv94IQf74Lg%2B59oA3B0V05BXKP7osgWmGb3iPg5XQ2oCHQzYfmkWyzoG9c6FbsyN6YoCWnv0nz4F6P3VH2Vvpx30vVVpG96eOKpJOrBGovlil7dHeTBwC28htxcGAFjyOLxrHM4pZNQ3oNuXrAiMKQ%2By2zmR9ghjk3hLREzZAogooUCjsUOoyDTowXl%2BNas%2BTCZvYi9BjqkAcSmiOmjk3FOBcGH76BM6xPibqmCO8eZP%2BNZ9hp7r1POYRO0DPPrnyT1QDAFj2Tp6QPMGxeTxYG1oAlfs50Bpn%2BIJAV%2BRbk1%2BAfw8cSTvtp1XC9iZlr3sHweNRiYRacHu1p2Y00yxdYu7ugzf0XjTUQqkGB2tveJrWTvidQ2xK4G5X2ZoH%2F22MvCOI1buuyGPb%2F%2Bg7v5ij%2FJuZS5%2B1qcyl0%2BQEkL&X-Amz-Signature=cc105bc651fb15f444322347949a5a44ab77f90d444394f30483bf99b70bf9e4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZFW6F2I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCsro%2FLVaHRlZtjT0cn3XbFzVAnItMSefYf8sjPaZ638wIhAInHtLscVUpkyLDRu0rNXPgYiW9I4gUQZuR0wy5LOTDhKv8DCC8QABoMNjM3NDIzMTgzODA1IgzIP%2FKJ2Howzs%2FjC84q3AOGnTSb54pLVFEz4VQLWoS2JNNXueZFTyY4Y8B8Ya8J7sdN1U1qw3%2Bs2iRyvHvSg8ZzgnQPxOiZcb8BqHp8E0K4lBS8UTKtRp1jqzP3aD2tLgsC0Xj6HnCMBviYGqb%2BLazpipzHRD9TsZ38HD%2FH2jIz0JV3%2Bv8C7dUCxX4%2FI64qrbfq3PZwMGNZqWKikLHo0ns%2BZGCLMIDdCrk4%2BNqCQ9II1SsMAq1afC3TrnOqluZ%2FdHweIV1M9EJdpYGzuRC7IWfYV%2BirpNo1KFznzRdbYj9AzR5pIkL%2B2efB%2FSWyorLXpRq8ZrOVYkc5znn%2F%2Fmm%2FmG8CuNiBFqeuY0NJFpJ0AtSTYjQkquZtq%2FQcfCQiDenkl%2FhmXNlmKXEY6t%2BO0Z3UbgRzQFBrCjhMc%2BuP7stLWn46pWqikRib0LmyZPr6dywSTavXASc%2B8A0szwmO2Rv94IQf74Lg%2B59oA3B0V05BXKP7osgWmGb3iPg5XQ2oCHQzYfmkWyzoG9c6FbsyN6YoCWnv0nz4F6P3VH2Vvpx30vVVpG96eOKpJOrBGovlil7dHeTBwC28htxcGAFjyOLxrHM4pZNQ3oNuXrAiMKQ%2By2zmR9ghjk3hLREzZAogooUCjsUOoyDTowXl%2BNas%2BTCZvYi9BjqkAcSmiOmjk3FOBcGH76BM6xPibqmCO8eZP%2BNZ9hp7r1POYRO0DPPrnyT1QDAFj2Tp6QPMGxeTxYG1oAlfs50Bpn%2BIJAV%2BRbk1%2BAfw8cSTvtp1XC9iZlr3sHweNRiYRacHu1p2Y00yxdYu7ugzf0XjTUQqkGB2tveJrWTvidQ2xK4G5X2ZoH%2F22MvCOI1buuyGPb%2F%2Bg7v5ij%2FJuZS5%2B1qcyl0%2BQEkL&X-Amz-Signature=00d216f1a1a5d620eb26aae47d18a72d4cd7ae52d1553b2f4bec289b2f092f60&X-Amz-SignedHeaders=host&x-id=GetObject)

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
