

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLZNDNAV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIGAp8Ec1WyMl5pAT9iOOSrsStMoVUICxaZtfVpMwGCqiAiBtdaCuMRgGKp%2FmUtq1FWVEOIko%2BUmj9Xno0gQtOdTLWSr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMeFOFJ%2BKW1eL%2BYrIZKtwDr7WN8qTNl9MiyzTCZWQm7bG6cgAPSTlJsFUuOJrTg5S2Z7CXA7q6mrpgMZNrCQeSJTXwjiZR5HrSA5J9HyoXZJzUBj8XuF1TJH48%2F4Lx8SoKp2JuyoAZNWt66j%2BHkIfOkTZ6C10xG3VWb%2FqJtJnpGcOUdNvzIGoJETaWCb%2Ft1h%2FFiBsYQKj7DL%2FFpOu2JRalMB0VpD%2FuBOR1urthywWnbdGxG6icfsQqEsoK%2BkdMUBX4Ft2RgGblFRqkc2Rcuevxu7qeYCj22I6Anaq86uSUkF2a%2Foi8cF5VvvMTVheFL3QMBzp%2FrJq3ehwErYw2clnviqrHBd%2F8oVMRuxR1p55tJaelOwpV5uzbpe%2FprnDrCuQzqAtJYhfLGcfyeDKKCIsg1b7U1bbDauTs1PVMksmOFhhllI1kRuto76OxJ2k%2B4lVodxUj9LFqcxHghKiiiPjlyjcuU%2BC1huXQZ%2F3oc0lhQRDNpxeS4ov%2FNYUnMkFksfNB9ftklYBWZkFlbr8ntZqTHQpssHzsgtSc%2FUA%2FcpAAHkJ38Wq2UU1lbhalfH7kz6yE%2FBfza%2B2sbtWqZ0HidRwGQH2T13HkRfVZsgxW5cJog82ziISq2IcqKEvbmOQ5cyiEH1arv1sEqeK5V0Aw%2F9yWvQY6pgG4VvQNkoYUzQeRPNUG8CFQBg%2FHsTDx5y%2Bxh61Bz2QEWYsRQeKfItP3wMCCz%2BYTZWB9M6FV29yrcHeoSZ5iWoW88JTWMkG6jOPVtXszq3xn%2BvKGILBZmEvGgUByrxl%2B6JGXupJr71YFnIX9td73RUsT8m%2FJmnGW98H2QNu2I%2FL3xPjnqEqtBg35BBLri6FR7W1RvoGgfz7C5CToHUncMLHeHJvs3PjL&X-Amz-Signature=0a2e301b2b4e28600362150267e985995d43db57ebf426eddfeab7c1e80ac536&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLZNDNAV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIGAp8Ec1WyMl5pAT9iOOSrsStMoVUICxaZtfVpMwGCqiAiBtdaCuMRgGKp%2FmUtq1FWVEOIko%2BUmj9Xno0gQtOdTLWSr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMeFOFJ%2BKW1eL%2BYrIZKtwDr7WN8qTNl9MiyzTCZWQm7bG6cgAPSTlJsFUuOJrTg5S2Z7CXA7q6mrpgMZNrCQeSJTXwjiZR5HrSA5J9HyoXZJzUBj8XuF1TJH48%2F4Lx8SoKp2JuyoAZNWt66j%2BHkIfOkTZ6C10xG3VWb%2FqJtJnpGcOUdNvzIGoJETaWCb%2Ft1h%2FFiBsYQKj7DL%2FFpOu2JRalMB0VpD%2FuBOR1urthywWnbdGxG6icfsQqEsoK%2BkdMUBX4Ft2RgGblFRqkc2Rcuevxu7qeYCj22I6Anaq86uSUkF2a%2Foi8cF5VvvMTVheFL3QMBzp%2FrJq3ehwErYw2clnviqrHBd%2F8oVMRuxR1p55tJaelOwpV5uzbpe%2FprnDrCuQzqAtJYhfLGcfyeDKKCIsg1b7U1bbDauTs1PVMksmOFhhllI1kRuto76OxJ2k%2B4lVodxUj9LFqcxHghKiiiPjlyjcuU%2BC1huXQZ%2F3oc0lhQRDNpxeS4ov%2FNYUnMkFksfNB9ftklYBWZkFlbr8ntZqTHQpssHzsgtSc%2FUA%2FcpAAHkJ38Wq2UU1lbhalfH7kz6yE%2FBfza%2B2sbtWqZ0HidRwGQH2T13HkRfVZsgxW5cJog82ziISq2IcqKEvbmOQ5cyiEH1arv1sEqeK5V0Aw%2F9yWvQY6pgG4VvQNkoYUzQeRPNUG8CFQBg%2FHsTDx5y%2Bxh61Bz2QEWYsRQeKfItP3wMCCz%2BYTZWB9M6FV29yrcHeoSZ5iWoW88JTWMkG6jOPVtXszq3xn%2BvKGILBZmEvGgUByrxl%2B6JGXupJr71YFnIX9td73RUsT8m%2FJmnGW98H2QNu2I%2FL3xPjnqEqtBg35BBLri6FR7W1RvoGgfz7C5CToHUncMLHeHJvs3PjL&X-Amz-Signature=160347b213391c126a29abe6ee9965eaae2d875648a2ceb98585683766ccd59c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLZNDNAV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIGAp8Ec1WyMl5pAT9iOOSrsStMoVUICxaZtfVpMwGCqiAiBtdaCuMRgGKp%2FmUtq1FWVEOIko%2BUmj9Xno0gQtOdTLWSr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMeFOFJ%2BKW1eL%2BYrIZKtwDr7WN8qTNl9MiyzTCZWQm7bG6cgAPSTlJsFUuOJrTg5S2Z7CXA7q6mrpgMZNrCQeSJTXwjiZR5HrSA5J9HyoXZJzUBj8XuF1TJH48%2F4Lx8SoKp2JuyoAZNWt66j%2BHkIfOkTZ6C10xG3VWb%2FqJtJnpGcOUdNvzIGoJETaWCb%2Ft1h%2FFiBsYQKj7DL%2FFpOu2JRalMB0VpD%2FuBOR1urthywWnbdGxG6icfsQqEsoK%2BkdMUBX4Ft2RgGblFRqkc2Rcuevxu7qeYCj22I6Anaq86uSUkF2a%2Foi8cF5VvvMTVheFL3QMBzp%2FrJq3ehwErYw2clnviqrHBd%2F8oVMRuxR1p55tJaelOwpV5uzbpe%2FprnDrCuQzqAtJYhfLGcfyeDKKCIsg1b7U1bbDauTs1PVMksmOFhhllI1kRuto76OxJ2k%2B4lVodxUj9LFqcxHghKiiiPjlyjcuU%2BC1huXQZ%2F3oc0lhQRDNpxeS4ov%2FNYUnMkFksfNB9ftklYBWZkFlbr8ntZqTHQpssHzsgtSc%2FUA%2FcpAAHkJ38Wq2UU1lbhalfH7kz6yE%2FBfza%2B2sbtWqZ0HidRwGQH2T13HkRfVZsgxW5cJog82ziISq2IcqKEvbmOQ5cyiEH1arv1sEqeK5V0Aw%2F9yWvQY6pgG4VvQNkoYUzQeRPNUG8CFQBg%2FHsTDx5y%2Bxh61Bz2QEWYsRQeKfItP3wMCCz%2BYTZWB9M6FV29yrcHeoSZ5iWoW88JTWMkG6jOPVtXszq3xn%2BvKGILBZmEvGgUByrxl%2B6JGXupJr71YFnIX9td73RUsT8m%2FJmnGW98H2QNu2I%2FL3xPjnqEqtBg35BBLri6FR7W1RvoGgfz7C5CToHUncMLHeHJvs3PjL&X-Amz-Signature=2f1fc791c7caec6e06d8252e54c1df05769679f0721ff07bf8215f6e2cd7a39b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RC3SWW2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIADQnFTF3cJY%2FytDp0fyPkLNWKhJ%2F%2Fe8azNCnb%2FcG7VDAiBnEr8fuLWdSKY0vn5zMaS4%2FLuAnHYIY2PFnOhPOuia%2Bir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMafV8iO6LFPGUFFwyKtwDUutrYm8A4BZa9CWHfpxK6aJ0mLux5tWvw7Kt894riAdfr%2F3nLFq3v7NqFnDQNkKjEU7NOiv8hYwFmeXD%2FwOu1fRsoCD1bNcZrkQc2k%2FhLBif6vCdDz06xzHUeIphtf4jjtSljIPM6WRoBrvGtlRlWkP7DhDXL0N3GtKEqRcq5JACoKdw2L0IXhjKJhSKURn2IQPCkHyaFz63yAJY5TBXIJHYesBGLZq6ZQwC5TPOWfsoOgjoBglTw%2FVCIEzO6a2Thd6v%2BJF5%2BR5T9t%2FsUSxYvxS07yRP6nJh8L%2BOHPEd7wuRKFyLRIueBFzd3amqkLFKXoPKLri%2B8zPwjeBTbwm%2B%2BYUDbwrXqEsJSmGH3Nv4liDWk8d7dajnE1yT4ZB%2BdtvAq8j3gEROTxywT9F8PaVHH70ui7HBIqsAWiZl5f5ZnbFVZeBwUILaBARFk3svGkE277mpJyjs6ZPJbVbL2mYum4JBccBG0clp%2Btl0tP8jQMKEoz3of1XndIC5znekju%2FC89cgQhFrY1ibS0MPdXLN3jzSKQf1hge%2BeDbQY7yg9RWvTHsqK9bFrR%2ByfjiqBUJrhsvkqThcKNlg0v3lgzYae3xVWAf4u95Vlff9g6No3ZEqncPSyr0GXQyU5Bwwhd2WvQY6pgGNZw%2BSxUJDRciAvzD92QxnSZk5WeCIzESWgbO6E5Y%2FyWz9MvEG%2FYQJB%2B9hGafnPjIOakAAK9mdAEvrs2IG%2B%2F84ZjgucVb5RdW9gfbqjPHcoPZIMYYrdjYF2%2FkbnQCXLZbbv47AxeOvqkZuZUdKZl2XpFShsFrbRVqcesol6wObf2sf8JPKWSrc6yybJnQ4DmsIc3M3TYzuf6UQ7Y1k9%2FCsCPcfM6qy&X-Amz-Signature=1672fbcf4b2c43e126acd1f618c6f2f59b2e91d90752d6c5a0138e36df0e9453&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RC3SWW2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIADQnFTF3cJY%2FytDp0fyPkLNWKhJ%2F%2Fe8azNCnb%2FcG7VDAiBnEr8fuLWdSKY0vn5zMaS4%2FLuAnHYIY2PFnOhPOuia%2Bir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMafV8iO6LFPGUFFwyKtwDUutrYm8A4BZa9CWHfpxK6aJ0mLux5tWvw7Kt894riAdfr%2F3nLFq3v7NqFnDQNkKjEU7NOiv8hYwFmeXD%2FwOu1fRsoCD1bNcZrkQc2k%2FhLBif6vCdDz06xzHUeIphtf4jjtSljIPM6WRoBrvGtlRlWkP7DhDXL0N3GtKEqRcq5JACoKdw2L0IXhjKJhSKURn2IQPCkHyaFz63yAJY5TBXIJHYesBGLZq6ZQwC5TPOWfsoOgjoBglTw%2FVCIEzO6a2Thd6v%2BJF5%2BR5T9t%2FsUSxYvxS07yRP6nJh8L%2BOHPEd7wuRKFyLRIueBFzd3amqkLFKXoPKLri%2B8zPwjeBTbwm%2B%2BYUDbwrXqEsJSmGH3Nv4liDWk8d7dajnE1yT4ZB%2BdtvAq8j3gEROTxywT9F8PaVHH70ui7HBIqsAWiZl5f5ZnbFVZeBwUILaBARFk3svGkE277mpJyjs6ZPJbVbL2mYum4JBccBG0clp%2Btl0tP8jQMKEoz3of1XndIC5znekju%2FC89cgQhFrY1ibS0MPdXLN3jzSKQf1hge%2BeDbQY7yg9RWvTHsqK9bFrR%2ByfjiqBUJrhsvkqThcKNlg0v3lgzYae3xVWAf4u95Vlff9g6No3ZEqncPSyr0GXQyU5Bwwhd2WvQY6pgGNZw%2BSxUJDRciAvzD92QxnSZk5WeCIzESWgbO6E5Y%2FyWz9MvEG%2FYQJB%2B9hGafnPjIOakAAK9mdAEvrs2IG%2B%2F84ZjgucVb5RdW9gfbqjPHcoPZIMYYrdjYF2%2FkbnQCXLZbbv47AxeOvqkZuZUdKZl2XpFShsFrbRVqcesol6wObf2sf8JPKWSrc6yybJnQ4DmsIc3M3TYzuf6UQ7Y1k9%2FCsCPcfM6qy&X-Amz-Signature=03635e02e0cdd2b2e64b68a5a93cfe4b351f95b97192ad8438175f15b939db1e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RC3SWW2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIADQnFTF3cJY%2FytDp0fyPkLNWKhJ%2F%2Fe8azNCnb%2FcG7VDAiBnEr8fuLWdSKY0vn5zMaS4%2FLuAnHYIY2PFnOhPOuia%2Bir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMafV8iO6LFPGUFFwyKtwDUutrYm8A4BZa9CWHfpxK6aJ0mLux5tWvw7Kt894riAdfr%2F3nLFq3v7NqFnDQNkKjEU7NOiv8hYwFmeXD%2FwOu1fRsoCD1bNcZrkQc2k%2FhLBif6vCdDz06xzHUeIphtf4jjtSljIPM6WRoBrvGtlRlWkP7DhDXL0N3GtKEqRcq5JACoKdw2L0IXhjKJhSKURn2IQPCkHyaFz63yAJY5TBXIJHYesBGLZq6ZQwC5TPOWfsoOgjoBglTw%2FVCIEzO6a2Thd6v%2BJF5%2BR5T9t%2FsUSxYvxS07yRP6nJh8L%2BOHPEd7wuRKFyLRIueBFzd3amqkLFKXoPKLri%2B8zPwjeBTbwm%2B%2BYUDbwrXqEsJSmGH3Nv4liDWk8d7dajnE1yT4ZB%2BdtvAq8j3gEROTxywT9F8PaVHH70ui7HBIqsAWiZl5f5ZnbFVZeBwUILaBARFk3svGkE277mpJyjs6ZPJbVbL2mYum4JBccBG0clp%2Btl0tP8jQMKEoz3of1XndIC5znekju%2FC89cgQhFrY1ibS0MPdXLN3jzSKQf1hge%2BeDbQY7yg9RWvTHsqK9bFrR%2ByfjiqBUJrhsvkqThcKNlg0v3lgzYae3xVWAf4u95Vlff9g6No3ZEqncPSyr0GXQyU5Bwwhd2WvQY6pgGNZw%2BSxUJDRciAvzD92QxnSZk5WeCIzESWgbO6E5Y%2FyWz9MvEG%2FYQJB%2B9hGafnPjIOakAAK9mdAEvrs2IG%2B%2F84ZjgucVb5RdW9gfbqjPHcoPZIMYYrdjYF2%2FkbnQCXLZbbv47AxeOvqkZuZUdKZl2XpFShsFrbRVqcesol6wObf2sf8JPKWSrc6yybJnQ4DmsIc3M3TYzuf6UQ7Y1k9%2FCsCPcfM6qy&X-Amz-Signature=6e6dd4bda15da89b95a4ec55e969f916a86581f3eb97074903563b280191e8f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RC3SWW2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIADQnFTF3cJY%2FytDp0fyPkLNWKhJ%2F%2Fe8azNCnb%2FcG7VDAiBnEr8fuLWdSKY0vn5zMaS4%2FLuAnHYIY2PFnOhPOuia%2Bir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMafV8iO6LFPGUFFwyKtwDUutrYm8A4BZa9CWHfpxK6aJ0mLux5tWvw7Kt894riAdfr%2F3nLFq3v7NqFnDQNkKjEU7NOiv8hYwFmeXD%2FwOu1fRsoCD1bNcZrkQc2k%2FhLBif6vCdDz06xzHUeIphtf4jjtSljIPM6WRoBrvGtlRlWkP7DhDXL0N3GtKEqRcq5JACoKdw2L0IXhjKJhSKURn2IQPCkHyaFz63yAJY5TBXIJHYesBGLZq6ZQwC5TPOWfsoOgjoBglTw%2FVCIEzO6a2Thd6v%2BJF5%2BR5T9t%2FsUSxYvxS07yRP6nJh8L%2BOHPEd7wuRKFyLRIueBFzd3amqkLFKXoPKLri%2B8zPwjeBTbwm%2B%2BYUDbwrXqEsJSmGH3Nv4liDWk8d7dajnE1yT4ZB%2BdtvAq8j3gEROTxywT9F8PaVHH70ui7HBIqsAWiZl5f5ZnbFVZeBwUILaBARFk3svGkE277mpJyjs6ZPJbVbL2mYum4JBccBG0clp%2Btl0tP8jQMKEoz3of1XndIC5znekju%2FC89cgQhFrY1ibS0MPdXLN3jzSKQf1hge%2BeDbQY7yg9RWvTHsqK9bFrR%2ByfjiqBUJrhsvkqThcKNlg0v3lgzYae3xVWAf4u95Vlff9g6No3ZEqncPSyr0GXQyU5Bwwhd2WvQY6pgGNZw%2BSxUJDRciAvzD92QxnSZk5WeCIzESWgbO6E5Y%2FyWz9MvEG%2FYQJB%2B9hGafnPjIOakAAK9mdAEvrs2IG%2B%2F84ZjgucVb5RdW9gfbqjPHcoPZIMYYrdjYF2%2FkbnQCXLZbbv47AxeOvqkZuZUdKZl2XpFShsFrbRVqcesol6wObf2sf8JPKWSrc6yybJnQ4DmsIc3M3TYzuf6UQ7Y1k9%2FCsCPcfM6qy&X-Amz-Signature=c69de8bfb86a315be527bed476683822f99b8dfaf2af49671a507275113d6ccc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RC3SWW2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIADQnFTF3cJY%2FytDp0fyPkLNWKhJ%2F%2Fe8azNCnb%2FcG7VDAiBnEr8fuLWdSKY0vn5zMaS4%2FLuAnHYIY2PFnOhPOuia%2Bir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMafV8iO6LFPGUFFwyKtwDUutrYm8A4BZa9CWHfpxK6aJ0mLux5tWvw7Kt894riAdfr%2F3nLFq3v7NqFnDQNkKjEU7NOiv8hYwFmeXD%2FwOu1fRsoCD1bNcZrkQc2k%2FhLBif6vCdDz06xzHUeIphtf4jjtSljIPM6WRoBrvGtlRlWkP7DhDXL0N3GtKEqRcq5JACoKdw2L0IXhjKJhSKURn2IQPCkHyaFz63yAJY5TBXIJHYesBGLZq6ZQwC5TPOWfsoOgjoBglTw%2FVCIEzO6a2Thd6v%2BJF5%2BR5T9t%2FsUSxYvxS07yRP6nJh8L%2BOHPEd7wuRKFyLRIueBFzd3amqkLFKXoPKLri%2B8zPwjeBTbwm%2B%2BYUDbwrXqEsJSmGH3Nv4liDWk8d7dajnE1yT4ZB%2BdtvAq8j3gEROTxywT9F8PaVHH70ui7HBIqsAWiZl5f5ZnbFVZeBwUILaBARFk3svGkE277mpJyjs6ZPJbVbL2mYum4JBccBG0clp%2Btl0tP8jQMKEoz3of1XndIC5znekju%2FC89cgQhFrY1ibS0MPdXLN3jzSKQf1hge%2BeDbQY7yg9RWvTHsqK9bFrR%2ByfjiqBUJrhsvkqThcKNlg0v3lgzYae3xVWAf4u95Vlff9g6No3ZEqncPSyr0GXQyU5Bwwhd2WvQY6pgGNZw%2BSxUJDRciAvzD92QxnSZk5WeCIzESWgbO6E5Y%2FyWz9MvEG%2FYQJB%2B9hGafnPjIOakAAK9mdAEvrs2IG%2B%2F84ZjgucVb5RdW9gfbqjPHcoPZIMYYrdjYF2%2FkbnQCXLZbbv47AxeOvqkZuZUdKZl2XpFShsFrbRVqcesol6wObf2sf8JPKWSrc6yybJnQ4DmsIc3M3TYzuf6UQ7Y1k9%2FCsCPcfM6qy&X-Amz-Signature=998b5703621ebc720d9f6acc9828565ba51815892e5e122812339899462b5b17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RC3SWW2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIADQnFTF3cJY%2FytDp0fyPkLNWKhJ%2F%2Fe8azNCnb%2FcG7VDAiBnEr8fuLWdSKY0vn5zMaS4%2FLuAnHYIY2PFnOhPOuia%2Bir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMafV8iO6LFPGUFFwyKtwDUutrYm8A4BZa9CWHfpxK6aJ0mLux5tWvw7Kt894riAdfr%2F3nLFq3v7NqFnDQNkKjEU7NOiv8hYwFmeXD%2FwOu1fRsoCD1bNcZrkQc2k%2FhLBif6vCdDz06xzHUeIphtf4jjtSljIPM6WRoBrvGtlRlWkP7DhDXL0N3GtKEqRcq5JACoKdw2L0IXhjKJhSKURn2IQPCkHyaFz63yAJY5TBXIJHYesBGLZq6ZQwC5TPOWfsoOgjoBglTw%2FVCIEzO6a2Thd6v%2BJF5%2BR5T9t%2FsUSxYvxS07yRP6nJh8L%2BOHPEd7wuRKFyLRIueBFzd3amqkLFKXoPKLri%2B8zPwjeBTbwm%2B%2BYUDbwrXqEsJSmGH3Nv4liDWk8d7dajnE1yT4ZB%2BdtvAq8j3gEROTxywT9F8PaVHH70ui7HBIqsAWiZl5f5ZnbFVZeBwUILaBARFk3svGkE277mpJyjs6ZPJbVbL2mYum4JBccBG0clp%2Btl0tP8jQMKEoz3of1XndIC5znekju%2FC89cgQhFrY1ibS0MPdXLN3jzSKQf1hge%2BeDbQY7yg9RWvTHsqK9bFrR%2ByfjiqBUJrhsvkqThcKNlg0v3lgzYae3xVWAf4u95Vlff9g6No3ZEqncPSyr0GXQyU5Bwwhd2WvQY6pgGNZw%2BSxUJDRciAvzD92QxnSZk5WeCIzESWgbO6E5Y%2FyWz9MvEG%2FYQJB%2B9hGafnPjIOakAAK9mdAEvrs2IG%2B%2F84ZjgucVb5RdW9gfbqjPHcoPZIMYYrdjYF2%2FkbnQCXLZbbv47AxeOvqkZuZUdKZl2XpFShsFrbRVqcesol6wObf2sf8JPKWSrc6yybJnQ4DmsIc3M3TYzuf6UQ7Y1k9%2FCsCPcfM6qy&X-Amz-Signature=7b10dc1a31ca883f97b7ff81a88d8c1ee0eb0693c3b395d181ee9a796d4f5c69&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RC3SWW2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIADQnFTF3cJY%2FytDp0fyPkLNWKhJ%2F%2Fe8azNCnb%2FcG7VDAiBnEr8fuLWdSKY0vn5zMaS4%2FLuAnHYIY2PFnOhPOuia%2Bir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMafV8iO6LFPGUFFwyKtwDUutrYm8A4BZa9CWHfpxK6aJ0mLux5tWvw7Kt894riAdfr%2F3nLFq3v7NqFnDQNkKjEU7NOiv8hYwFmeXD%2FwOu1fRsoCD1bNcZrkQc2k%2FhLBif6vCdDz06xzHUeIphtf4jjtSljIPM6WRoBrvGtlRlWkP7DhDXL0N3GtKEqRcq5JACoKdw2L0IXhjKJhSKURn2IQPCkHyaFz63yAJY5TBXIJHYesBGLZq6ZQwC5TPOWfsoOgjoBglTw%2FVCIEzO6a2Thd6v%2BJF5%2BR5T9t%2FsUSxYvxS07yRP6nJh8L%2BOHPEd7wuRKFyLRIueBFzd3amqkLFKXoPKLri%2B8zPwjeBTbwm%2B%2BYUDbwrXqEsJSmGH3Nv4liDWk8d7dajnE1yT4ZB%2BdtvAq8j3gEROTxywT9F8PaVHH70ui7HBIqsAWiZl5f5ZnbFVZeBwUILaBARFk3svGkE277mpJyjs6ZPJbVbL2mYum4JBccBG0clp%2Btl0tP8jQMKEoz3of1XndIC5znekju%2FC89cgQhFrY1ibS0MPdXLN3jzSKQf1hge%2BeDbQY7yg9RWvTHsqK9bFrR%2ByfjiqBUJrhsvkqThcKNlg0v3lgzYae3xVWAf4u95Vlff9g6No3ZEqncPSyr0GXQyU5Bwwhd2WvQY6pgGNZw%2BSxUJDRciAvzD92QxnSZk5WeCIzESWgbO6E5Y%2FyWz9MvEG%2FYQJB%2B9hGafnPjIOakAAK9mdAEvrs2IG%2B%2F84ZjgucVb5RdW9gfbqjPHcoPZIMYYrdjYF2%2FkbnQCXLZbbv47AxeOvqkZuZUdKZl2XpFShsFrbRVqcesol6wObf2sf8JPKWSrc6yybJnQ4DmsIc3M3TYzuf6UQ7Y1k9%2FCsCPcfM6qy&X-Amz-Signature=114a29f5c3ad6f48ca9e8fffa96c7dee7f7241d0133d29c4e4d2b3cd9bb4aba8&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642JEXCCI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQD56xxNA5cHCBw0D9aiTGYKeLHRsGAs%2Fq3LsMXGZC4g6gIhAJKeeh2BRe6SD5QJCxzvKzozbVYeSSVyYjEmqfjEPZcmKv8DCHAQABoMNjM3NDIzMTgzODA1IgxvSJhaUsu%2B4L2CS4Qq3AMpu2tB4FfeOBRgHfm84gtWCuVEK16NQO8yIAo%2FiU67o5X%2BXfoOBzQMyBijvL1at1d%2FHff0iBjuKC1d1ezsXBsG6WItIHQljHtc6f5XwFKMaa4ZNDHONpM%2B3hphP1bIp9I%2Fcphu4o0PhcXCk%2FcLxrqvx7esmMJ55lxqHw4W%2Bk8t%2FyNP4EAct0%2BRO6k%2BaMAGyqpuiTaUZyz4xHLK7QuqM2FxGahdQJXBD5wh2T8oLrtMHZVs2a8LcZfLFBEFt%2FUlu2An%2BHJ4QsbK9E7syA2kDEprJZpZOG1h%2BtOjrV7WKuC335QbvW%2BDwIX1qCIAFHXJV3Cu9rkxKLJblcm%2BAoQDbBXx2fRm9HmvJRjHjLRclvAnmPeJBFPLCAfloE%2BDMe8rtG4mKNPqICqvrlC2F8sCyWhjImDtXNOIEc0QNAat8NhPhghZoAd7qAnV1fdhD%2Bm9d2HTJNAhjVlN0tyFBa6JN7Ce%2F6PKd8cr7FF4jZJKQh2nd6neHewTpDkJSUQEAnDvTBAhpi7T%2BmcqpDo0Eo4iMXLAaIExQ%2F4MpZcaLqpxtWTqzC3uUBZcGtjXHZGf%2BgHGl22ZWnTuDjFoQIBhIzAbAdKxfrYegHWpBaWaWnkSIgY%2BI5PW0%2BCujOxm2L0zAzD73Za9BjqkAaTv5hHi5VYDUFf7Twe0W9sxj1efkcn%2FMrksSnBWi4cYbV8%2Bd8SeXRScIhcoPilxp3hhFMZI8y3%2B94vtmLlTcoUgk2qA87sENn38hVmsn8g66COS%2BEEwbh1Jzw9s8Tjs7NaeneBEWp2Vv9wds90s0efV5QJDmp%2FTdBFf6Kg4pCASSirZaEeeuLZygzy8IRaphmXETerowfOP2vYisjOn5%2Ft2ecb%2B&X-Amz-Signature=22d33314d25387ed6dafb16c3bc79cad0b0e2965fa52e8d422355eea3404ff22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RC3SWW2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIADQnFTF3cJY%2FytDp0fyPkLNWKhJ%2F%2Fe8azNCnb%2FcG7VDAiBnEr8fuLWdSKY0vn5zMaS4%2FLuAnHYIY2PFnOhPOuia%2Bir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMafV8iO6LFPGUFFwyKtwDUutrYm8A4BZa9CWHfpxK6aJ0mLux5tWvw7Kt894riAdfr%2F3nLFq3v7NqFnDQNkKjEU7NOiv8hYwFmeXD%2FwOu1fRsoCD1bNcZrkQc2k%2FhLBif6vCdDz06xzHUeIphtf4jjtSljIPM6WRoBrvGtlRlWkP7DhDXL0N3GtKEqRcq5JACoKdw2L0IXhjKJhSKURn2IQPCkHyaFz63yAJY5TBXIJHYesBGLZq6ZQwC5TPOWfsoOgjoBglTw%2FVCIEzO6a2Thd6v%2BJF5%2BR5T9t%2FsUSxYvxS07yRP6nJh8L%2BOHPEd7wuRKFyLRIueBFzd3amqkLFKXoPKLri%2B8zPwjeBTbwm%2B%2BYUDbwrXqEsJSmGH3Nv4liDWk8d7dajnE1yT4ZB%2BdtvAq8j3gEROTxywT9F8PaVHH70ui7HBIqsAWiZl5f5ZnbFVZeBwUILaBARFk3svGkE277mpJyjs6ZPJbVbL2mYum4JBccBG0clp%2Btl0tP8jQMKEoz3of1XndIC5znekju%2FC89cgQhFrY1ibS0MPdXLN3jzSKQf1hge%2BeDbQY7yg9RWvTHsqK9bFrR%2ByfjiqBUJrhsvkqThcKNlg0v3lgzYae3xVWAf4u95Vlff9g6No3ZEqncPSyr0GXQyU5Bwwhd2WvQY6pgGNZw%2BSxUJDRciAvzD92QxnSZk5WeCIzESWgbO6E5Y%2FyWz9MvEG%2FYQJB%2B9hGafnPjIOakAAK9mdAEvrs2IG%2B%2F84ZjgucVb5RdW9gfbqjPHcoPZIMYYrdjYF2%2FkbnQCXLZbbv47AxeOvqkZuZUdKZl2XpFShsFrbRVqcesol6wObf2sf8JPKWSrc6yybJnQ4DmsIc3M3TYzuf6UQ7Y1k9%2FCsCPcfM6qy&X-Amz-Signature=3bac632ad949fd09fad792e0f3ac36f83df4649a00cdf5615c39cd4860829e50&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RC3SWW2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIADQnFTF3cJY%2FytDp0fyPkLNWKhJ%2F%2Fe8azNCnb%2FcG7VDAiBnEr8fuLWdSKY0vn5zMaS4%2FLuAnHYIY2PFnOhPOuia%2Bir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMafV8iO6LFPGUFFwyKtwDUutrYm8A4BZa9CWHfpxK6aJ0mLux5tWvw7Kt894riAdfr%2F3nLFq3v7NqFnDQNkKjEU7NOiv8hYwFmeXD%2FwOu1fRsoCD1bNcZrkQc2k%2FhLBif6vCdDz06xzHUeIphtf4jjtSljIPM6WRoBrvGtlRlWkP7DhDXL0N3GtKEqRcq5JACoKdw2L0IXhjKJhSKURn2IQPCkHyaFz63yAJY5TBXIJHYesBGLZq6ZQwC5TPOWfsoOgjoBglTw%2FVCIEzO6a2Thd6v%2BJF5%2BR5T9t%2FsUSxYvxS07yRP6nJh8L%2BOHPEd7wuRKFyLRIueBFzd3amqkLFKXoPKLri%2B8zPwjeBTbwm%2B%2BYUDbwrXqEsJSmGH3Nv4liDWk8d7dajnE1yT4ZB%2BdtvAq8j3gEROTxywT9F8PaVHH70ui7HBIqsAWiZl5f5ZnbFVZeBwUILaBARFk3svGkE277mpJyjs6ZPJbVbL2mYum4JBccBG0clp%2Btl0tP8jQMKEoz3of1XndIC5znekju%2FC89cgQhFrY1ibS0MPdXLN3jzSKQf1hge%2BeDbQY7yg9RWvTHsqK9bFrR%2ByfjiqBUJrhsvkqThcKNlg0v3lgzYae3xVWAf4u95Vlff9g6No3ZEqncPSyr0GXQyU5Bwwhd2WvQY6pgGNZw%2BSxUJDRciAvzD92QxnSZk5WeCIzESWgbO6E5Y%2FyWz9MvEG%2FYQJB%2B9hGafnPjIOakAAK9mdAEvrs2IG%2B%2F84ZjgucVb5RdW9gfbqjPHcoPZIMYYrdjYF2%2FkbnQCXLZbbv47AxeOvqkZuZUdKZl2XpFShsFrbRVqcesol6wObf2sf8JPKWSrc6yybJnQ4DmsIc3M3TYzuf6UQ7Y1k9%2FCsCPcfM6qy&X-Amz-Signature=01f4894d6674d7b68db264a9c10e80e72fc69765d56cdf3220200c2644a2106f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RC3SWW2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIADQnFTF3cJY%2FytDp0fyPkLNWKhJ%2F%2Fe8azNCnb%2FcG7VDAiBnEr8fuLWdSKY0vn5zMaS4%2FLuAnHYIY2PFnOhPOuia%2Bir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMafV8iO6LFPGUFFwyKtwDUutrYm8A4BZa9CWHfpxK6aJ0mLux5tWvw7Kt894riAdfr%2F3nLFq3v7NqFnDQNkKjEU7NOiv8hYwFmeXD%2FwOu1fRsoCD1bNcZrkQc2k%2FhLBif6vCdDz06xzHUeIphtf4jjtSljIPM6WRoBrvGtlRlWkP7DhDXL0N3GtKEqRcq5JACoKdw2L0IXhjKJhSKURn2IQPCkHyaFz63yAJY5TBXIJHYesBGLZq6ZQwC5TPOWfsoOgjoBglTw%2FVCIEzO6a2Thd6v%2BJF5%2BR5T9t%2FsUSxYvxS07yRP6nJh8L%2BOHPEd7wuRKFyLRIueBFzd3amqkLFKXoPKLri%2B8zPwjeBTbwm%2B%2BYUDbwrXqEsJSmGH3Nv4liDWk8d7dajnE1yT4ZB%2BdtvAq8j3gEROTxywT9F8PaVHH70ui7HBIqsAWiZl5f5ZnbFVZeBwUILaBARFk3svGkE277mpJyjs6ZPJbVbL2mYum4JBccBG0clp%2Btl0tP8jQMKEoz3of1XndIC5znekju%2FC89cgQhFrY1ibS0MPdXLN3jzSKQf1hge%2BeDbQY7yg9RWvTHsqK9bFrR%2ByfjiqBUJrhsvkqThcKNlg0v3lgzYae3xVWAf4u95Vlff9g6No3ZEqncPSyr0GXQyU5Bwwhd2WvQY6pgGNZw%2BSxUJDRciAvzD92QxnSZk5WeCIzESWgbO6E5Y%2FyWz9MvEG%2FYQJB%2B9hGafnPjIOakAAK9mdAEvrs2IG%2B%2F84ZjgucVb5RdW9gfbqjPHcoPZIMYYrdjYF2%2FkbnQCXLZbbv47AxeOvqkZuZUdKZl2XpFShsFrbRVqcesol6wObf2sf8JPKWSrc6yybJnQ4DmsIc3M3TYzuf6UQ7Y1k9%2FCsCPcfM6qy&X-Amz-Signature=de65fbcf6b01c27f3dbd0df52b0e49ded2e2941dc682305a69f110acf130eb22&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTH7YQEM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQDE4KBgIbGWJv4ZchFCQ6BH%2BoZbudAE9zj%2FWFEnCSskNgIgY5ADLMdFPKmShi7zolLkofo2%2FxiQV6Ff2mPdyk6gnW4q%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDIUy%2FGW8qmnoSkaAxSrcA16oTsiHKg2%2F8y9kAivZKd09NFfwAoJsu8q0NTFu9YjpMGVvsq7Muq9lPqSYRRfiwWYk29wrNwl3qaIG3PjGJe4jA5hAeTegd3X5HgATHohhqmsqS%2F7nbpj9bd1LE1kKLnAhUkvjvssS8YRZQtrdBN9aiM9O5vA10PnutwnEzMZwTyts%2Bfga7RgTf3qOIhzRndBLVfqi1%2FT%2BcJFIKVHJMXtAxMkb7SZS2u3vNrJ1M7g8DKEGRKLIDhO7iDk1dWB8MHQPhO1KyKtBD4WxrozSURtyoRWWd1cB8y3Bz1hK%2BGXx3VgPWHohgrGCH6ez2XbuE4RNOBQzJtGrdWMfGUm3FPzX%2FL%2BL1ADP7qZxn1MDUp4YgKQoo4zuL0g6N9TxLpFzNGAc4h5lOx5U%2BZDfdg5LqIrL91TXJnBbcNZOLKTEOgWVjodTtebze1GbKdU7zjh4jZi5es3ybRgCk6H2S%2BdDIuNURuwH%2Fr8G1530siNdZSmIS2b5M2hashKmOqLm%2FHRJe3zRxbVypKoc4qUNxmDzu%2BOmuF6UUbJhXnh5LiMsqqJ6ThRs5QOnHDdSDrrS%2Fwmf9VZzEkXHM4F%2Fmjrv0veRN3Q%2Fkahu78a4TVsos4PjsKskb9fpSjqypqE1NQygMN%2Fclr0GOqUBLbjhC56fXobj3y3naHkzgzS8fewRjJw3HZdJE3pQSRafwC%2FBKFN6Lcex0ZFlm%2BNVlcbF5w61ggLc8%2BWz7T97mh0FAVGQkqTexzyr5uFGxaiR2Ah3msY4JIWNDUElPqpo6e3VT%2B1Nv1rbg30RAZlJIrC92GA3ml5J0%2FHTx1a%2BYKFMaUOZM1yNigIyQgRU%2F8g%2FZ8hjz1J68wy5a7EMHFDLZq8mnKjS&X-Amz-Signature=bca4b6c7d6b105aab25173af4ca640f02806cd811011d6155098a70fe0a00d4e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5JN7TI6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQDRMkYpk0bsD70MFPfkIJ%2B%2BkB3mlkvXjY6G2w2q9dF2SwIgc8F8bhIej%2BOcUdkag0qBA93fqVx%2BxQW82Ar28RvC7tYq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDIxpKAUW42n%2BXqVLYyrcA9uFOAege6oK%2BH9ctypS9GwO%2FLKiETVL669Gc8vvEGJbH5j%2BHihzHqVgVYPUkhJR0QBAikhPfq3h0ewOydUgDTCT1ur4DtjD0dTaZ%2FNcN8n8aY0L2l1%2Bh4vrIaCjZXL5%2BsqeFxxLyhKL%2FT7LtbMLXES64yOu%2FGzd%2BLDew3qQsduoG6nWCcU8m8UctG53ENS2EuKWtj81c4do56BbkuF81j6L2GX%2B6suiMCPbGClHw32nz6phn3Rkju9eFu0eeJLObewA3WXlK3b1IouBYViIRDYdKBqe7eJzyDZjKlzCok37N2nhfuJ%2Fp1ZKK25wGBv7iEFk0rV6ZEAR9R8BkuiA9ibKPJuIA1sw%2FGseSVRZHYin548F5S0Lntxq4hNMPhNYrbpOjThQo%2BShhNJSq2ohzNljBFciHsnztbPQn6SAqMBvJRcusfWBTgeumP%2F3jSbcT47sG4zosUo5HH5aQ2NluJErKvJYw2WT76acQQqXOrUzVwiyFOYSkFS7Yr620UHXYLLYXTUHC%2BSjQSvnQbW32Z9X0bJVCWdCj9y2BEtYeHgPaqSZLF5ewWS5bLEgnAf2nA35HyRghPdR319ZLufzN6M12OgSXKt%2FG%2BD7xtvs42elI3DdQIoRHUq9iA6KMLbdlr0GOqUBUHRmlWmvBGMJGXFWyoHimCdY8XekkiKoQwTChqkVP4%2F%2BuF0h7KPvD8xd6%2Bf8KeL9DHB3mlzf0yw%2F9oWrACX4eKliaNkS6phA2RXjeobHO%2FKtXgMf2TYMu6rePN%2FlzigOSdsl82VJaihQFW%2BjQPZDeTPcmJHQS9N3%2F3yPEUqzPsVBPtx%2BoFrqEY4KBm9RkYxn6jeAXwdc6DdMl3JtAPriDQJqKaj4&X-Amz-Signature=a58c7138898b98f65628cab6055e2500bfbc18f6c7dad18ef518eb81fc62438c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW6TM7IJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQD6CbgW3KGLdNNRHXQ2te5%2BieTOBlZd4cbRwPGQA%2BXCZwIhAKBrjALUymRd%2FcvllBbGRwurImQGkKoovXycS3N%2Fw1a4Kv8DCHAQABoMNjM3NDIzMTgzODA1Igx0QDND7FNX22NgSI8q3AOrEgNH5S08EtsZ7UTYrXto901TP%2B21738cTlXuk9c4K1tCOl4ddvoXMc7kKbXAahooQXjZ1HWK2to7DlbaIes7%2FFyhM%2F%2BPPJzeySZwLQiI%2B5y0xYIaHHa5GqTqYMRhaF0ZyW75m7r%2BmlM97EuFK8E%2FvmycgXhDeK2jKs6XFHuoMv5rNCMPFhOuj6a%2BYM77owYEreO5n%2FMRwFkgPBGLhCbAzl8GxLTirA2F478uNxymxVteOO51xdWce0lkQeMGc1WY5C1ggOtoPt5RBgVBRGFXcqJ62iiRDJdPXarlCGgkUB8%2B0TRO%2FVbKGA95r%2BMMukWjuGx9b%2BSdm5R%2F3CsNnppQSdGRMpFlt5P9K5ePgtjd8nvIj12vYorQQh0hPyqoTqhYpUTTOhvdxEQUiuXsP1y663YrhC9CHSwgrZLjCrh%2F4eYcuZBmi2aTiEX8M%2FmdlB16E765CfXfX8H3ngSzXXJBK7VwaMhTXwXa1A%2FNaFi1svj7KJUX0jJVYJdhMcVZYEdy0FLuEF%2Bt0pVaeZ%2FV56r3AzOWGpvbaI64omqVMKRxBlBXMs0gjR9QP1fVIGsasVYDkyVE8nQ9andkO7H883ouoRBHqF59r8nSHqwZ6XR3hQjjKo9MmuoEjxejeDDU3Ja9BjqkAeBrWfwutbNnKaCkmO%2B4%2FqpQSpeIFEQUVmig1URaFzxa9w6fB9tRwEoC7H%2FfYdTGzetc7ao%2Fmr6AKfOk3%2BjZRch1PsxKcezQel6D0so7dyeWB%2BF1svepZmVkhNMznyL0RX0LQFR3goS79oPhW9OYSClo%2F54IiskYqXQ3qzn5oFvJqCR6r5W%2FFkqXqioAIDmGpZClovv%2FCUsqdV3rXgn%2BFrTASdNu&X-Amz-Signature=7aed43fabe9ea63ba24db5820c3e339ce74847cb3fb14f473b224774b9dd7915&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPIFLIR3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCpMYbj8O%2F1POs3yHB7GG8mBI%2B8gEqjgiG3Ke89ro2S4gIgCwns6KIaPsLSlE3e%2FKSCSqflxtlXQGG56ynl5OaRRvIq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDEmWPHnYLV8Prl6caSrcAxFf8CtacRGyiQHRsxPCveCmFBRs2%2BKe4AXcnBUJG7VJkkpsFSeRUx9rugr42hMS4VpAuua%2FhwTLGltLiCA2K8tBsgcF7UEZ1k2SOOhb%2FGEVYX7rtmnWXA%2FIJ4TTFaM%2Fab%2BgZ5Yl%2FRCgWw0eHqJsaKOW3Ueth2sQrPy%2Bvs0PWrm1n7%2F1VkuKLlb%2BdstSsvyE4mtdBJ7pasZaAyVuodwQ4i53%2FbdXAGGINQXlk5fra1oZ7TioOXfc%2FT0hTNsGclbs1gFA8xtfpbE%2BTc4hodPmdAvCb2IsGdya2ts5cUPVMXIx82ODf6r%2BUzannNBaxU%2Bj4zOXHP0SiNmuYtKFBvg13V71ON2nlBjE2Tq8LfgpCXdYnPszqlHXGav05fDx9hue4m%2F70niUyzHF81IK9EDVgILWoBddLkdgypP1JytUj0vSnC59cb%2B3FnQ%2BEv9n6v0eXksYcEtXNsfrcGeL3ddE9jufiKh7Fh35cEvZGGy%2FYBC8jxKQVTFy6X6ADJkVOR5C%2F%2F9IG38zjBRjL5I1e7dRyBRoUf4AIgXH2iHGGgk77OrH5iIXYB6EpfJ5DOaIOoRA7%2FEMBxHfL8vO6MOIQ2N%2F%2B%2F0Loff%2FORy5vvi%2FeUwkgRdxS%2BtU3Zn0WpS%2BrtixMIHdlr0GOqUBpnAxI%2FElxbfPx5elP6VEfBrvV2FBy%2BppD37FNoLCFQsOLWZzOYacTNJbsP7YLywFgLGZUt30Y%2Fim1oiUJgnm5O5vfP4ZSa9k%2BrZ9sikc4Gqlw5B9bqo6hS%2BAnDHlqPs2EJytd%2Fl%2BYLmBbkBK6ow83OqTUmInSoKwlKUji%2Fy%2F1LwScVJjyWXo98NVrCeceZz%2BzrwxIYicH5tc0Twhr0amsOb9k4kF&X-Amz-Signature=7e7c0fc050f7d3bf1c104a7047ae7fbddfd38ddb7a82086bc2227af0f4713cb8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPIFLIR3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCpMYbj8O%2F1POs3yHB7GG8mBI%2B8gEqjgiG3Ke89ro2S4gIgCwns6KIaPsLSlE3e%2FKSCSqflxtlXQGG56ynl5OaRRvIq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDEmWPHnYLV8Prl6caSrcAxFf8CtacRGyiQHRsxPCveCmFBRs2%2BKe4AXcnBUJG7VJkkpsFSeRUx9rugr42hMS4VpAuua%2FhwTLGltLiCA2K8tBsgcF7UEZ1k2SOOhb%2FGEVYX7rtmnWXA%2FIJ4TTFaM%2Fab%2BgZ5Yl%2FRCgWw0eHqJsaKOW3Ueth2sQrPy%2Bvs0PWrm1n7%2F1VkuKLlb%2BdstSsvyE4mtdBJ7pasZaAyVuodwQ4i53%2FbdXAGGINQXlk5fra1oZ7TioOXfc%2FT0hTNsGclbs1gFA8xtfpbE%2BTc4hodPmdAvCb2IsGdya2ts5cUPVMXIx82ODf6r%2BUzannNBaxU%2Bj4zOXHP0SiNmuYtKFBvg13V71ON2nlBjE2Tq8LfgpCXdYnPszqlHXGav05fDx9hue4m%2F70niUyzHF81IK9EDVgILWoBddLkdgypP1JytUj0vSnC59cb%2B3FnQ%2BEv9n6v0eXksYcEtXNsfrcGeL3ddE9jufiKh7Fh35cEvZGGy%2FYBC8jxKQVTFy6X6ADJkVOR5C%2F%2F9IG38zjBRjL5I1e7dRyBRoUf4AIgXH2iHGGgk77OrH5iIXYB6EpfJ5DOaIOoRA7%2FEMBxHfL8vO6MOIQ2N%2F%2B%2F0Loff%2FORy5vvi%2FeUwkgRdxS%2BtU3Zn0WpS%2BrtixMIHdlr0GOqUBpnAxI%2FElxbfPx5elP6VEfBrvV2FBy%2BppD37FNoLCFQsOLWZzOYacTNJbsP7YLywFgLGZUt30Y%2Fim1oiUJgnm5O5vfP4ZSa9k%2BrZ9sikc4Gqlw5B9bqo6hS%2BAnDHlqPs2EJytd%2Fl%2BYLmBbkBK6ow83OqTUmInSoKwlKUji%2Fy%2F1LwScVJjyWXo98NVrCeceZz%2BzrwxIYicH5tc0Twhr0amsOb9k4kF&X-Amz-Signature=d7751b61cbbffc40a97bf5b88d1325cd392fdc36da61d90cabfc4e723e25e991&X-Amz-SignedHeaders=host&x-id=GetObject)

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
