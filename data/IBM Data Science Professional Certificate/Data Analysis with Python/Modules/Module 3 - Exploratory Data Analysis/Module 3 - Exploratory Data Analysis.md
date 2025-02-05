

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBBCKJJL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQCkEwxE%2ByxI6b83xPIxp490aUFweb2Lb5Qm9r4f%2BEUsxQIgOblD%2FzrA8zuItBEBPkikzB%2B4P1TwA46o9vwbSzqhUssq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDDN7xdUIZZyuaYNYuyrcA9MdSQGF0JOS7UiYFiaFRi5tlVMvTKMa%2FsNCHl8Dulk%2BYtK9LQPy9DG%2BWV%2BR9A9ZN7RFhYOZN%2Fu9i3MSVKwXxXin8WwyIs83PL6noWqYotGaKDTaHpPLrM3lco4JiOTU26Wosbv4ATkH%2Bi8UOne6%2FeTC7Yn1WK%2B7XPyih%2BKpvxS8jxV8pIvD0nGRImws4l3bR%2BM%2FoDGFZsQA8cjUT20%2FXVynoIQZ%2FqM591HV7s2%2Fuk%2BoXyvyf02gBLJxuBaJEanu1IJjkgUalF9lt85eV9oKQg3BQWcgbtF1op%2FAjFwuce9hWDgKZ0LhcPIG2TrKV%2FxsCrsf6dQRxC%2FTI8LSyLduP3LraT0piWvUzvTje0KxJpcf7ThSRkbvGyJtPCFiWXmqJBeH%2BeOXuP2qvATfroAHUs5S6oMOoX%2Bk%2BmkUp2rP1ie8OB6q8c5o8NV9z3r40LTCkGE5h9dlzgfC9txaJUjp9GaRSje8HkJ1faWc9032%2BCbHE9IDj9DVHWQujsT0s1612PO3GcLiHVa7PKO9LtrZmTCsBgiGJjHUdQ0I59pkZLDIY29vfj%2F3a1SzSJm%2B75WXMjW1c1n1XqcXvk7OrrdPQxCPAdieSdUDY8ugbxgC4i66xVM0Gup98AJ0mqrsMNDvjL0GOqUBRwL5utNClsT3Fp%2FCpIQwN0HfADRd74e2von4lmBfKM%2FZkhZLEdxyei32mwqI3NCTJtc5xPHC1TMhjzvzV5yucpSPu%2BMxF3EcIndQDXv9bFlhozBzmDBUKQr3b2Vv3Y5MtcaaYe09knWemGsAF3KxyhoqXkjrGJc7pf3dN4ARkb9UX3TxVMB203KiUIs%2BP9lUSYDW515quy7FvdWe7Z5luXroxq%2Fy&X-Amz-Signature=e6b942bd765d329208edd10842208332e4d65309c42e28e2127e9bcd1d2988e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBBCKJJL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQCkEwxE%2ByxI6b83xPIxp490aUFweb2Lb5Qm9r4f%2BEUsxQIgOblD%2FzrA8zuItBEBPkikzB%2B4P1TwA46o9vwbSzqhUssq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDDN7xdUIZZyuaYNYuyrcA9MdSQGF0JOS7UiYFiaFRi5tlVMvTKMa%2FsNCHl8Dulk%2BYtK9LQPy9DG%2BWV%2BR9A9ZN7RFhYOZN%2Fu9i3MSVKwXxXin8WwyIs83PL6noWqYotGaKDTaHpPLrM3lco4JiOTU26Wosbv4ATkH%2Bi8UOne6%2FeTC7Yn1WK%2B7XPyih%2BKpvxS8jxV8pIvD0nGRImws4l3bR%2BM%2FoDGFZsQA8cjUT20%2FXVynoIQZ%2FqM591HV7s2%2Fuk%2BoXyvyf02gBLJxuBaJEanu1IJjkgUalF9lt85eV9oKQg3BQWcgbtF1op%2FAjFwuce9hWDgKZ0LhcPIG2TrKV%2FxsCrsf6dQRxC%2FTI8LSyLduP3LraT0piWvUzvTje0KxJpcf7ThSRkbvGyJtPCFiWXmqJBeH%2BeOXuP2qvATfroAHUs5S6oMOoX%2Bk%2BmkUp2rP1ie8OB6q8c5o8NV9z3r40LTCkGE5h9dlzgfC9txaJUjp9GaRSje8HkJ1faWc9032%2BCbHE9IDj9DVHWQujsT0s1612PO3GcLiHVa7PKO9LtrZmTCsBgiGJjHUdQ0I59pkZLDIY29vfj%2F3a1SzSJm%2B75WXMjW1c1n1XqcXvk7OrrdPQxCPAdieSdUDY8ugbxgC4i66xVM0Gup98AJ0mqrsMNDvjL0GOqUBRwL5utNClsT3Fp%2FCpIQwN0HfADRd74e2von4lmBfKM%2FZkhZLEdxyei32mwqI3NCTJtc5xPHC1TMhjzvzV5yucpSPu%2BMxF3EcIndQDXv9bFlhozBzmDBUKQr3b2Vv3Y5MtcaaYe09knWemGsAF3KxyhoqXkjrGJc7pf3dN4ARkb9UX3TxVMB203KiUIs%2BP9lUSYDW515quy7FvdWe7Z5luXroxq%2Fy&X-Amz-Signature=c6c539fa7d93e0cf58340de472f31fcf56c46c763cf0e849d97d9700af47d9ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBBCKJJL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQCkEwxE%2ByxI6b83xPIxp490aUFweb2Lb5Qm9r4f%2BEUsxQIgOblD%2FzrA8zuItBEBPkikzB%2B4P1TwA46o9vwbSzqhUssq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDDN7xdUIZZyuaYNYuyrcA9MdSQGF0JOS7UiYFiaFRi5tlVMvTKMa%2FsNCHl8Dulk%2BYtK9LQPy9DG%2BWV%2BR9A9ZN7RFhYOZN%2Fu9i3MSVKwXxXin8WwyIs83PL6noWqYotGaKDTaHpPLrM3lco4JiOTU26Wosbv4ATkH%2Bi8UOne6%2FeTC7Yn1WK%2B7XPyih%2BKpvxS8jxV8pIvD0nGRImws4l3bR%2BM%2FoDGFZsQA8cjUT20%2FXVynoIQZ%2FqM591HV7s2%2Fuk%2BoXyvyf02gBLJxuBaJEanu1IJjkgUalF9lt85eV9oKQg3BQWcgbtF1op%2FAjFwuce9hWDgKZ0LhcPIG2TrKV%2FxsCrsf6dQRxC%2FTI8LSyLduP3LraT0piWvUzvTje0KxJpcf7ThSRkbvGyJtPCFiWXmqJBeH%2BeOXuP2qvATfroAHUs5S6oMOoX%2Bk%2BmkUp2rP1ie8OB6q8c5o8NV9z3r40LTCkGE5h9dlzgfC9txaJUjp9GaRSje8HkJ1faWc9032%2BCbHE9IDj9DVHWQujsT0s1612PO3GcLiHVa7PKO9LtrZmTCsBgiGJjHUdQ0I59pkZLDIY29vfj%2F3a1SzSJm%2B75WXMjW1c1n1XqcXvk7OrrdPQxCPAdieSdUDY8ugbxgC4i66xVM0Gup98AJ0mqrsMNDvjL0GOqUBRwL5utNClsT3Fp%2FCpIQwN0HfADRd74e2von4lmBfKM%2FZkhZLEdxyei32mwqI3NCTJtc5xPHC1TMhjzvzV5yucpSPu%2BMxF3EcIndQDXv9bFlhozBzmDBUKQr3b2Vv3Y5MtcaaYe09knWemGsAF3KxyhoqXkjrGJc7pf3dN4ARkb9UX3TxVMB203KiUIs%2BP9lUSYDW515quy7FvdWe7Z5luXroxq%2Fy&X-Amz-Signature=0884f48e37755ace15bd2e9d368a7e7ab47fbe2ec12f95e4b9d4431ba2dd42fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH67ZX7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDAimYgAwcZcxk4Kdl82jkp4XZfPTltn4iTu70EiwSH2AIgMJlYC3TEFvy%2BUYkmtfzhdEJu4LR%2BUVwimn5aTgsYG0cq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKzF6%2FT6aRlR5NeF2CrcA4J%2B%2FzmTouPmMSR%2Bi1KIz%2BD1Hv6M4JSQWE4wvFxsju%2FdvYG9oIKuA0JT524ZnIWj4fyUhacnvSRCNLSG6D2ziSB5JfrzZnlUVU067hOEiqu%2BjvuLLboJIh2BdR5yVztkeOSzJiXmHQJIvjoTq5hRLUVaPwGiVA%2BgUuYIxb0upEJCby3dyNTcmNaozOZixtq00yOeYK%2F6XbbwneTZeY6tszhxD4cWHFHR%2FvZQDrx%2FKNmvzQwHcYWRh%2FPm%2B69FT76oIWWjT32OYS%2FHhrfp9tIbA4XhV4Uxvz32yQu%2Ff88k05TICuJkr%2FLvGUNWlDaxYxnhtMUPGGpii7ySr8Twd7tGd9hFzDgdf3w5LHpqoeBcpickU4sBmnVfAdbNzD4j2Mcfq34z7TJNTFmwqmQ68yqkugvzDjymBfQXbXkpORlvVOkmt3zo6z%2FYyxjqv0x%2FdX%2FevXwCEStZYtTsVLTl58KnrFuipl5SI9714RtngAA4foavLQ2TQLPz7h12u1eoJ6yf43qDY4DZ4T%2B8L2SqQgCg%2Bi%2B0vjzZPK1X5spm6hrKTCkUsznAnYHxZKFoCUB3SQeQanNB3hf7YMb%2Fuak%2BlCDXjhXFN%2BglgvS%2Bbwf4khB1Zjc0PnQRLT%2BD7r0xv2v3MI%2FzjL0GOqUBkY%2Feh7g8r%2FO3ohwDeRGXF67VqU6zG4zaWqWPT4q6QaLHj2W1%2B6v4BzkWTWwwgYFWPOiBCp5fuz419kEfoiGUU%2BgZ4ioSbzL5nEO0HkwVGln1fpT0S7fqOTeAeU4BIUsbj2s9dp8JEo4Zf4Ez2iIZhDlLv0pNH3lzyjZJ3UD6EW0ccp4rdWVonInZHA54XlDQNXojbYuOe%2BdWS1Ey4LvWv1MiofQu&X-Amz-Signature=e89c3a69fa1596e05af230861172b26c95b3399df4bf7fe38e2487b1311261bb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH67ZX7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDAimYgAwcZcxk4Kdl82jkp4XZfPTltn4iTu70EiwSH2AIgMJlYC3TEFvy%2BUYkmtfzhdEJu4LR%2BUVwimn5aTgsYG0cq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKzF6%2FT6aRlR5NeF2CrcA4J%2B%2FzmTouPmMSR%2Bi1KIz%2BD1Hv6M4JSQWE4wvFxsju%2FdvYG9oIKuA0JT524ZnIWj4fyUhacnvSRCNLSG6D2ziSB5JfrzZnlUVU067hOEiqu%2BjvuLLboJIh2BdR5yVztkeOSzJiXmHQJIvjoTq5hRLUVaPwGiVA%2BgUuYIxb0upEJCby3dyNTcmNaozOZixtq00yOeYK%2F6XbbwneTZeY6tszhxD4cWHFHR%2FvZQDrx%2FKNmvzQwHcYWRh%2FPm%2B69FT76oIWWjT32OYS%2FHhrfp9tIbA4XhV4Uxvz32yQu%2Ff88k05TICuJkr%2FLvGUNWlDaxYxnhtMUPGGpii7ySr8Twd7tGd9hFzDgdf3w5LHpqoeBcpickU4sBmnVfAdbNzD4j2Mcfq34z7TJNTFmwqmQ68yqkugvzDjymBfQXbXkpORlvVOkmt3zo6z%2FYyxjqv0x%2FdX%2FevXwCEStZYtTsVLTl58KnrFuipl5SI9714RtngAA4foavLQ2TQLPz7h12u1eoJ6yf43qDY4DZ4T%2B8L2SqQgCg%2Bi%2B0vjzZPK1X5spm6hrKTCkUsznAnYHxZKFoCUB3SQeQanNB3hf7YMb%2Fuak%2BlCDXjhXFN%2BglgvS%2Bbwf4khB1Zjc0PnQRLT%2BD7r0xv2v3MI%2FzjL0GOqUBkY%2Feh7g8r%2FO3ohwDeRGXF67VqU6zG4zaWqWPT4q6QaLHj2W1%2B6v4BzkWTWwwgYFWPOiBCp5fuz419kEfoiGUU%2BgZ4ioSbzL5nEO0HkwVGln1fpT0S7fqOTeAeU4BIUsbj2s9dp8JEo4Zf4Ez2iIZhDlLv0pNH3lzyjZJ3UD6EW0ccp4rdWVonInZHA54XlDQNXojbYuOe%2BdWS1Ey4LvWv1MiofQu&X-Amz-Signature=c4394618357ec183fb51c304f16ed865e054231bf1374c3675872538a23eced6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH67ZX7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDAimYgAwcZcxk4Kdl82jkp4XZfPTltn4iTu70EiwSH2AIgMJlYC3TEFvy%2BUYkmtfzhdEJu4LR%2BUVwimn5aTgsYG0cq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKzF6%2FT6aRlR5NeF2CrcA4J%2B%2FzmTouPmMSR%2Bi1KIz%2BD1Hv6M4JSQWE4wvFxsju%2FdvYG9oIKuA0JT524ZnIWj4fyUhacnvSRCNLSG6D2ziSB5JfrzZnlUVU067hOEiqu%2BjvuLLboJIh2BdR5yVztkeOSzJiXmHQJIvjoTq5hRLUVaPwGiVA%2BgUuYIxb0upEJCby3dyNTcmNaozOZixtq00yOeYK%2F6XbbwneTZeY6tszhxD4cWHFHR%2FvZQDrx%2FKNmvzQwHcYWRh%2FPm%2B69FT76oIWWjT32OYS%2FHhrfp9tIbA4XhV4Uxvz32yQu%2Ff88k05TICuJkr%2FLvGUNWlDaxYxnhtMUPGGpii7ySr8Twd7tGd9hFzDgdf3w5LHpqoeBcpickU4sBmnVfAdbNzD4j2Mcfq34z7TJNTFmwqmQ68yqkugvzDjymBfQXbXkpORlvVOkmt3zo6z%2FYyxjqv0x%2FdX%2FevXwCEStZYtTsVLTl58KnrFuipl5SI9714RtngAA4foavLQ2TQLPz7h12u1eoJ6yf43qDY4DZ4T%2B8L2SqQgCg%2Bi%2B0vjzZPK1X5spm6hrKTCkUsznAnYHxZKFoCUB3SQeQanNB3hf7YMb%2Fuak%2BlCDXjhXFN%2BglgvS%2Bbwf4khB1Zjc0PnQRLT%2BD7r0xv2v3MI%2FzjL0GOqUBkY%2Feh7g8r%2FO3ohwDeRGXF67VqU6zG4zaWqWPT4q6QaLHj2W1%2B6v4BzkWTWwwgYFWPOiBCp5fuz419kEfoiGUU%2BgZ4ioSbzL5nEO0HkwVGln1fpT0S7fqOTeAeU4BIUsbj2s9dp8JEo4Zf4Ez2iIZhDlLv0pNH3lzyjZJ3UD6EW0ccp4rdWVonInZHA54XlDQNXojbYuOe%2BdWS1Ey4LvWv1MiofQu&X-Amz-Signature=697f91c42e79982de35e5ab850395bba6f0d05c805fea635819883e999a941bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH67ZX7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDAimYgAwcZcxk4Kdl82jkp4XZfPTltn4iTu70EiwSH2AIgMJlYC3TEFvy%2BUYkmtfzhdEJu4LR%2BUVwimn5aTgsYG0cq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKzF6%2FT6aRlR5NeF2CrcA4J%2B%2FzmTouPmMSR%2Bi1KIz%2BD1Hv6M4JSQWE4wvFxsju%2FdvYG9oIKuA0JT524ZnIWj4fyUhacnvSRCNLSG6D2ziSB5JfrzZnlUVU067hOEiqu%2BjvuLLboJIh2BdR5yVztkeOSzJiXmHQJIvjoTq5hRLUVaPwGiVA%2BgUuYIxb0upEJCby3dyNTcmNaozOZixtq00yOeYK%2F6XbbwneTZeY6tszhxD4cWHFHR%2FvZQDrx%2FKNmvzQwHcYWRh%2FPm%2B69FT76oIWWjT32OYS%2FHhrfp9tIbA4XhV4Uxvz32yQu%2Ff88k05TICuJkr%2FLvGUNWlDaxYxnhtMUPGGpii7ySr8Twd7tGd9hFzDgdf3w5LHpqoeBcpickU4sBmnVfAdbNzD4j2Mcfq34z7TJNTFmwqmQ68yqkugvzDjymBfQXbXkpORlvVOkmt3zo6z%2FYyxjqv0x%2FdX%2FevXwCEStZYtTsVLTl58KnrFuipl5SI9714RtngAA4foavLQ2TQLPz7h12u1eoJ6yf43qDY4DZ4T%2B8L2SqQgCg%2Bi%2B0vjzZPK1X5spm6hrKTCkUsznAnYHxZKFoCUB3SQeQanNB3hf7YMb%2Fuak%2BlCDXjhXFN%2BglgvS%2Bbwf4khB1Zjc0PnQRLT%2BD7r0xv2v3MI%2FzjL0GOqUBkY%2Feh7g8r%2FO3ohwDeRGXF67VqU6zG4zaWqWPT4q6QaLHj2W1%2B6v4BzkWTWwwgYFWPOiBCp5fuz419kEfoiGUU%2BgZ4ioSbzL5nEO0HkwVGln1fpT0S7fqOTeAeU4BIUsbj2s9dp8JEo4Zf4Ez2iIZhDlLv0pNH3lzyjZJ3UD6EW0ccp4rdWVonInZHA54XlDQNXojbYuOe%2BdWS1Ey4LvWv1MiofQu&X-Amz-Signature=2ff8d128fc8d17d5834f578da9ac33ace0ec6b0d2c22fb3210b88e640186cda2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH67ZX7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDAimYgAwcZcxk4Kdl82jkp4XZfPTltn4iTu70EiwSH2AIgMJlYC3TEFvy%2BUYkmtfzhdEJu4LR%2BUVwimn5aTgsYG0cq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKzF6%2FT6aRlR5NeF2CrcA4J%2B%2FzmTouPmMSR%2Bi1KIz%2BD1Hv6M4JSQWE4wvFxsju%2FdvYG9oIKuA0JT524ZnIWj4fyUhacnvSRCNLSG6D2ziSB5JfrzZnlUVU067hOEiqu%2BjvuLLboJIh2BdR5yVztkeOSzJiXmHQJIvjoTq5hRLUVaPwGiVA%2BgUuYIxb0upEJCby3dyNTcmNaozOZixtq00yOeYK%2F6XbbwneTZeY6tszhxD4cWHFHR%2FvZQDrx%2FKNmvzQwHcYWRh%2FPm%2B69FT76oIWWjT32OYS%2FHhrfp9tIbA4XhV4Uxvz32yQu%2Ff88k05TICuJkr%2FLvGUNWlDaxYxnhtMUPGGpii7ySr8Twd7tGd9hFzDgdf3w5LHpqoeBcpickU4sBmnVfAdbNzD4j2Mcfq34z7TJNTFmwqmQ68yqkugvzDjymBfQXbXkpORlvVOkmt3zo6z%2FYyxjqv0x%2FdX%2FevXwCEStZYtTsVLTl58KnrFuipl5SI9714RtngAA4foavLQ2TQLPz7h12u1eoJ6yf43qDY4DZ4T%2B8L2SqQgCg%2Bi%2B0vjzZPK1X5spm6hrKTCkUsznAnYHxZKFoCUB3SQeQanNB3hf7YMb%2Fuak%2BlCDXjhXFN%2BglgvS%2Bbwf4khB1Zjc0PnQRLT%2BD7r0xv2v3MI%2FzjL0GOqUBkY%2Feh7g8r%2FO3ohwDeRGXF67VqU6zG4zaWqWPT4q6QaLHj2W1%2B6v4BzkWTWwwgYFWPOiBCp5fuz419kEfoiGUU%2BgZ4ioSbzL5nEO0HkwVGln1fpT0S7fqOTeAeU4BIUsbj2s9dp8JEo4Zf4Ez2iIZhDlLv0pNH3lzyjZJ3UD6EW0ccp4rdWVonInZHA54XlDQNXojbYuOe%2BdWS1Ey4LvWv1MiofQu&X-Amz-Signature=41dfab8e61c316b779d5936142a60ade32a2366332f07a26c97a86fc31068535&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH67ZX7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDAimYgAwcZcxk4Kdl82jkp4XZfPTltn4iTu70EiwSH2AIgMJlYC3TEFvy%2BUYkmtfzhdEJu4LR%2BUVwimn5aTgsYG0cq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKzF6%2FT6aRlR5NeF2CrcA4J%2B%2FzmTouPmMSR%2Bi1KIz%2BD1Hv6M4JSQWE4wvFxsju%2FdvYG9oIKuA0JT524ZnIWj4fyUhacnvSRCNLSG6D2ziSB5JfrzZnlUVU067hOEiqu%2BjvuLLboJIh2BdR5yVztkeOSzJiXmHQJIvjoTq5hRLUVaPwGiVA%2BgUuYIxb0upEJCby3dyNTcmNaozOZixtq00yOeYK%2F6XbbwneTZeY6tszhxD4cWHFHR%2FvZQDrx%2FKNmvzQwHcYWRh%2FPm%2B69FT76oIWWjT32OYS%2FHhrfp9tIbA4XhV4Uxvz32yQu%2Ff88k05TICuJkr%2FLvGUNWlDaxYxnhtMUPGGpii7ySr8Twd7tGd9hFzDgdf3w5LHpqoeBcpickU4sBmnVfAdbNzD4j2Mcfq34z7TJNTFmwqmQ68yqkugvzDjymBfQXbXkpORlvVOkmt3zo6z%2FYyxjqv0x%2FdX%2FevXwCEStZYtTsVLTl58KnrFuipl5SI9714RtngAA4foavLQ2TQLPz7h12u1eoJ6yf43qDY4DZ4T%2B8L2SqQgCg%2Bi%2B0vjzZPK1X5spm6hrKTCkUsznAnYHxZKFoCUB3SQeQanNB3hf7YMb%2Fuak%2BlCDXjhXFN%2BglgvS%2Bbwf4khB1Zjc0PnQRLT%2BD7r0xv2v3MI%2FzjL0GOqUBkY%2Feh7g8r%2FO3ohwDeRGXF67VqU6zG4zaWqWPT4q6QaLHj2W1%2B6v4BzkWTWwwgYFWPOiBCp5fuz419kEfoiGUU%2BgZ4ioSbzL5nEO0HkwVGln1fpT0S7fqOTeAeU4BIUsbj2s9dp8JEo4Zf4Ez2iIZhDlLv0pNH3lzyjZJ3UD6EW0ccp4rdWVonInZHA54XlDQNXojbYuOe%2BdWS1Ey4LvWv1MiofQu&X-Amz-Signature=9f78a2f49f348e67196fb3947dc54e654a241e2098d4ebae564cd0e5d030f844&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AVDFBOU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIFAwEduOzm%2Bcm%2FRngbBiTjBkdcQNHLWVtM3ZeV%2F4bfyoAiBeT7iBuf4jcdCI6hjrFmpeWtwPKjLqn2Yw2NYCEU%2FkYir%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMVNraoo1Gd0Olco1OKtwDM4XAHz%2BGmnfciLYPTdw0WxNjt8sQQ5W7vAx7PmxdRX4K7q3HL26dNvwrSrTKKZzzyOs%2Blrxcv3Mjdqnp0gnmqCoqexVTBj3ttFbrgzFFa6EFZxl3E9AXNDrQvzW6nZc%2FhMw2TQ0Uq7tbfjSiRxp6C5GTbuSA8g1nrnHOxgHWrjEzeIFjQ9YbdptFDmOYNFHn%2FDpX0A%2BTs53H00FaB22YWCNjfLYakGA%2Ff%2FV7xkq7%2Bl6ypVKdAlPq3SII5t30QWabMiq6vTAbokE66%2BP1XwxSSeSr39%2Bt6wbmiTk6Caq%2B%2BINsqgNfZ5cSCNb5dQG3aO4X7WBN8%2FRFpTiGgFd7UKqIa9tBpZ5NNadOF8qcq0dDnNnffFxLjRYarQyvSCo77Tj01%2BfJqtRE%2BeE7Bs%2BX2rgutQ6fdHwSb49eoSIX2s57OI%2Bt%2FFQTk25VuWC4mnJN4taA31kKQcZQ2d4ILHbrKqyCfLUa%2FTefNggk2wZAdcnDjBipM3fwY9Iuc3Iy%2BTtzL1lDP7Pvq3ayPUKLDXvjBtOTcDNHicch%2FllQDta7QZxilRSGydvTfRKXsl1Fi89qGEpmDDdt8cC2YA37WZTRdVSic7tNGFVSNjovHPP%2Bb3XmKI49eTRpCwvyyRkiuPYw1u%2BMvQY6pgGwECWuCogrB05Bo1iBOsVl9q0fJt0iWiFJNPaQxNqZ3lXBxuq3uT4d%2FShmoNUXwK%2FhcbtJ1Vi0WzHH90yrq%2BkOAKLa6NxbRnRwUUvqhZadp0uka1em%2FpsmVdhjdXB8ITNvWr1iO1aZtyfk6bcuutoRojcPByqss0k3bjckN3g3x%2FM3vexiDEFocLN0BSxSB6wqi6ivZkY0TPKib0YpEWyHD6R3Mkc5&X-Amz-Signature=a1992d16cd06222f5e4c34315a24a1bf8cb0f66a6828d6065614eb957a3e8464&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOLUJTBY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCICd5Qidp00y4TwmPK7rjctGIAzHmDGvssObKF1R39bw%2BAiAJPQn%2BLS3BuNKSdWprl72o%2FCXsg9Z8wjQLELBPVx9CgCr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMUcWdcL8u4Hx78VDqKtwDA%2BHqw%2BC1DiP7tdM%2FawbP1X3XnYn5tZb7%2BuoIDT51xq%2FHbgS7Cw9Z2wLSIPdjCnDv7hTdBbxyKXSvw08%2BylDWEWssepRQqJ1i111gs2Lpq6peRKiu5cs1jwPQKwYsLFrgzLWYqzhFf6gxL0x%2F3K2Tccl4Of44t%2FfUkF3j3Z9xagGPlmUqwyibnX51YRBE%2F8hSx%2FtxEZblTCiDLBj92WQuS6FPuMAvk7FkauSXFidGgkg1GV1jMsjTTrCu%2BMLcjyyAULzQVMJD7l5Mmw3JhPKWqXQbuV7dw430o96%2FhIo9ofqFGxfe%2FtF0QzPQ%2ByajpuZKzgr0SrQMEqE2oZi2ePcj1ew8gH6rmiA0nlADlYvKeQKUF%2BP5Xxku3MkvzCvPh75rEkCHQWBMo0QtX7v8htRyTnxYEAmuDtGKyodQjqSSN5kTv76h6Y2gB1ssVKiPy1rrnQdS78Kk40Sj0Pfe7wJPL4VLuAVxC7ZiIBKRwZc3hKf2xTT8T%2B9M40RxAYY9Nzp1skehq03QmEDEd6xGM42pMSQSK6tDFChD1YtHOavoHzPoXl%2BdEoNJovI0bII67K8%2FM7ezBB3lkwNyiR8s6ms1MREHKbVcr6XWfLh18ahZjWLWzyHVpFqoZelBQFcw1%2B%2BMvQY6pgH6JwWB4%2FulXBfzCK9Xt49FJO7dOHXxBMEljCfpL%2FDXKr4bEUXJ7yRLZuR6iqDeCwgE1XGpaMVq2cK0%2BrO7j6tVV4DYxfjIukaOiumzNBApCOS5WIMXFjth2E3jXUREY%2F2UUpT%2BUBquuFWQINz5sZoKt0nuBrr4hgAijOfgS30AafKyoQfPzdZqSdIuuoDuj0l4y3cmhYVpYhPB5FPi9b33QtSdK1tK&X-Amz-Signature=ec1cf82611f92636812c48437050aa657509d6a9fd7665785eb40b86eebb6c7d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH67ZX7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDAimYgAwcZcxk4Kdl82jkp4XZfPTltn4iTu70EiwSH2AIgMJlYC3TEFvy%2BUYkmtfzhdEJu4LR%2BUVwimn5aTgsYG0cq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKzF6%2FT6aRlR5NeF2CrcA4J%2B%2FzmTouPmMSR%2Bi1KIz%2BD1Hv6M4JSQWE4wvFxsju%2FdvYG9oIKuA0JT524ZnIWj4fyUhacnvSRCNLSG6D2ziSB5JfrzZnlUVU067hOEiqu%2BjvuLLboJIh2BdR5yVztkeOSzJiXmHQJIvjoTq5hRLUVaPwGiVA%2BgUuYIxb0upEJCby3dyNTcmNaozOZixtq00yOeYK%2F6XbbwneTZeY6tszhxD4cWHFHR%2FvZQDrx%2FKNmvzQwHcYWRh%2FPm%2B69FT76oIWWjT32OYS%2FHhrfp9tIbA4XhV4Uxvz32yQu%2Ff88k05TICuJkr%2FLvGUNWlDaxYxnhtMUPGGpii7ySr8Twd7tGd9hFzDgdf3w5LHpqoeBcpickU4sBmnVfAdbNzD4j2Mcfq34z7TJNTFmwqmQ68yqkugvzDjymBfQXbXkpORlvVOkmt3zo6z%2FYyxjqv0x%2FdX%2FevXwCEStZYtTsVLTl58KnrFuipl5SI9714RtngAA4foavLQ2TQLPz7h12u1eoJ6yf43qDY4DZ4T%2B8L2SqQgCg%2Bi%2B0vjzZPK1X5spm6hrKTCkUsznAnYHxZKFoCUB3SQeQanNB3hf7YMb%2Fuak%2BlCDXjhXFN%2BglgvS%2Bbwf4khB1Zjc0PnQRLT%2BD7r0xv2v3MI%2FzjL0GOqUBkY%2Feh7g8r%2FO3ohwDeRGXF67VqU6zG4zaWqWPT4q6QaLHj2W1%2B6v4BzkWTWwwgYFWPOiBCp5fuz419kEfoiGUU%2BgZ4ioSbzL5nEO0HkwVGln1fpT0S7fqOTeAeU4BIUsbj2s9dp8JEo4Zf4Ez2iIZhDlLv0pNH3lzyjZJ3UD6EW0ccp4rdWVonInZHA54XlDQNXojbYuOe%2BdWS1Ey4LvWv1MiofQu&X-Amz-Signature=d901813366f0100736a386348691b63fbc4f13248a13341a7da336629712fd97&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH67ZX7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDAimYgAwcZcxk4Kdl82jkp4XZfPTltn4iTu70EiwSH2AIgMJlYC3TEFvy%2BUYkmtfzhdEJu4LR%2BUVwimn5aTgsYG0cq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKzF6%2FT6aRlR5NeF2CrcA4J%2B%2FzmTouPmMSR%2Bi1KIz%2BD1Hv6M4JSQWE4wvFxsju%2FdvYG9oIKuA0JT524ZnIWj4fyUhacnvSRCNLSG6D2ziSB5JfrzZnlUVU067hOEiqu%2BjvuLLboJIh2BdR5yVztkeOSzJiXmHQJIvjoTq5hRLUVaPwGiVA%2BgUuYIxb0upEJCby3dyNTcmNaozOZixtq00yOeYK%2F6XbbwneTZeY6tszhxD4cWHFHR%2FvZQDrx%2FKNmvzQwHcYWRh%2FPm%2B69FT76oIWWjT32OYS%2FHhrfp9tIbA4XhV4Uxvz32yQu%2Ff88k05TICuJkr%2FLvGUNWlDaxYxnhtMUPGGpii7ySr8Twd7tGd9hFzDgdf3w5LHpqoeBcpickU4sBmnVfAdbNzD4j2Mcfq34z7TJNTFmwqmQ68yqkugvzDjymBfQXbXkpORlvVOkmt3zo6z%2FYyxjqv0x%2FdX%2FevXwCEStZYtTsVLTl58KnrFuipl5SI9714RtngAA4foavLQ2TQLPz7h12u1eoJ6yf43qDY4DZ4T%2B8L2SqQgCg%2Bi%2B0vjzZPK1X5spm6hrKTCkUsznAnYHxZKFoCUB3SQeQanNB3hf7YMb%2Fuak%2BlCDXjhXFN%2BglgvS%2Bbwf4khB1Zjc0PnQRLT%2BD7r0xv2v3MI%2FzjL0GOqUBkY%2Feh7g8r%2FO3ohwDeRGXF67VqU6zG4zaWqWPT4q6QaLHj2W1%2B6v4BzkWTWwwgYFWPOiBCp5fuz419kEfoiGUU%2BgZ4ioSbzL5nEO0HkwVGln1fpT0S7fqOTeAeU4BIUsbj2s9dp8JEo4Zf4Ez2iIZhDlLv0pNH3lzyjZJ3UD6EW0ccp4rdWVonInZHA54XlDQNXojbYuOe%2BdWS1Ey4LvWv1MiofQu&X-Amz-Signature=4d6bfc54c2c35614d686e290bab5978b4d538fc39c7999bc8c1022703fa83617&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH67ZX7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDAimYgAwcZcxk4Kdl82jkp4XZfPTltn4iTu70EiwSH2AIgMJlYC3TEFvy%2BUYkmtfzhdEJu4LR%2BUVwimn5aTgsYG0cq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKzF6%2FT6aRlR5NeF2CrcA4J%2B%2FzmTouPmMSR%2Bi1KIz%2BD1Hv6M4JSQWE4wvFxsju%2FdvYG9oIKuA0JT524ZnIWj4fyUhacnvSRCNLSG6D2ziSB5JfrzZnlUVU067hOEiqu%2BjvuLLboJIh2BdR5yVztkeOSzJiXmHQJIvjoTq5hRLUVaPwGiVA%2BgUuYIxb0upEJCby3dyNTcmNaozOZixtq00yOeYK%2F6XbbwneTZeY6tszhxD4cWHFHR%2FvZQDrx%2FKNmvzQwHcYWRh%2FPm%2B69FT76oIWWjT32OYS%2FHhrfp9tIbA4XhV4Uxvz32yQu%2Ff88k05TICuJkr%2FLvGUNWlDaxYxnhtMUPGGpii7ySr8Twd7tGd9hFzDgdf3w5LHpqoeBcpickU4sBmnVfAdbNzD4j2Mcfq34z7TJNTFmwqmQ68yqkugvzDjymBfQXbXkpORlvVOkmt3zo6z%2FYyxjqv0x%2FdX%2FevXwCEStZYtTsVLTl58KnrFuipl5SI9714RtngAA4foavLQ2TQLPz7h12u1eoJ6yf43qDY4DZ4T%2B8L2SqQgCg%2Bi%2B0vjzZPK1X5spm6hrKTCkUsznAnYHxZKFoCUB3SQeQanNB3hf7YMb%2Fuak%2BlCDXjhXFN%2BglgvS%2Bbwf4khB1Zjc0PnQRLT%2BD7r0xv2v3MI%2FzjL0GOqUBkY%2Feh7g8r%2FO3ohwDeRGXF67VqU6zG4zaWqWPT4q6QaLHj2W1%2B6v4BzkWTWwwgYFWPOiBCp5fuz419kEfoiGUU%2BgZ4ioSbzL5nEO0HkwVGln1fpT0S7fqOTeAeU4BIUsbj2s9dp8JEo4Zf4Ez2iIZhDlLv0pNH3lzyjZJ3UD6EW0ccp4rdWVonInZHA54XlDQNXojbYuOe%2BdWS1Ey4LvWv1MiofQu&X-Amz-Signature=d322fa11d5a5c917d1a3ea06ec74ece1ecb6b669e13c79f78edca87cd379e1f4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXFLIHAX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQD78kNDgld8rSVL8dSh8Q%2FQb%2BBVC4jZg%2FMcUoC5Hq%2FucwIgHHbkpeC2F7n9EJdxjHNePEgXhCnomdjaQgLkkzTOcigq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKzbdXFVtQP2WFxTTSrcA%2By3yc70Lw20tgyBN6PFNnxXLBvu56ClfNDT0Do%2FXPGwSX0HM0wM83YozCLsMPIANa1YL6WXQrEFmWh6QRYpDKfw8yyig8kFa0vb8E76rVFRG3N%2FiwPWuZ2MNxiWByMbbUv9%2B%2FXVYZuEM9hWpUkt1w%2F5bOX%2BRGAwWULLHNlt5BM2XQWTGR5blEmdegSz0v2r147kgL9PVpIGsQEhOkmzkmhuon1u6JSMMZcZXLWNEUjFF2C7baJgLQgFkup%2F8IUPL%2BHpbFu2k%2FhBoWedO7IDl8lniIVaM%2BgWKI5laILgzv%2BPnfMmiI1IMUTKxlivw0jMBNeF8u6zGe9f31FYI0V%2BQ%2Fa0ZXVUVAB6rwPFAZg935iP6%2F4RJmz7%2FyeC7KDwCwUrR7PHZPPZiIu9kXqPKEaxxA7%2F0EZtlUeUJfsxDTvwBFmiDh4B2B7vFx1N4vkf8pe0OoA1A0D%2FjTl8mP9DXxmsrPBGO%2F1BeOgS3efEX5f1jJRccxZle6ORUsUUXk4aDbXOTI2nU9Ju53%2FUVomQ5q0lWFWIZ3s2OFc3U3YxAHQ%2F7FMZhlEgoGcLffdlK5zzd5mnIGmOvZYaqCYjGXrhnHnlh49phVYxQV7K8dhtpNxRCtDB25z67QaYpc2wNySmMILvjL0GOqUBmlqQ%2BMXJ%2FPbPtuH%2ButIJqICo6apNnXcGct4GjwaC94r3D6aZqHzhOOh1bAhPkgf%2FGvYQ6dtHWLNVB2I3d9hQKPM0T2BtAhiE2IQtZYvoFMoDtGj3fCWYNNbN71BgxNVOTk81x6UkqXq8Z063r5UCeZXIgz4ja0%2FZqRUThfmscTe0uXLVPMMlGgdtJXz%2F%2FXVvBuTvz5HQyDMA7jzFzuTD%2Bl5gOPiw&X-Amz-Signature=12c4c436b4fae3630791ddc69fd5eeeda56710bb3b1a7cddf7ab8452cc90e47f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T6LPWDV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQC9RH9OnLLj%2BblJ212Aiob6Qh5sTYMFgCoC92xWm%2BiYZQIgPQJrNNmOUnKKAyhWx3PF%2F0UPUqSQJoVQeeGXuwCtgPQq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDIRRG7Uu1FDfOPnVSSrcA6PQRYkjQW1BL0myZjrtJtDmb%2BJRvgd6aGkAfCa15bNHLhK3lJe4mLHaOzdWg33xMkaNK%2BefJdaUDLbfG3CFgS0pj%2Ffv546J2%2B4nO6TtinOY4WZjBkwdOU75EWO3q1ATUYoM1ma9vCLl7KBWyU015FnMxwvZk3P2hvt5Vl8qwetvD00WqzkVFb38mhheAXWB2cywOJ3Q7FFNZj%2BcC%2BTdpO39lNMN3vsqU6j2Hefp0GSFVGknwdje%2FMMcxQPh3dyA9iDOldkJwuvMY4dCJJGviqG2Ba80AzJsR1oocMYYu3JtqJj6yOqBQSzu7wO49BKxUxXGbCIO4vZOhS2sAAyZ059gK6CjBvYGXN2zA4qkHUC4kRwWM8OjrNCbNWDb%2Bzms1a8vznGGH8Hv8l8Qb36DbO2jUFRaT%2FDKAqpYvXfBc%2BN2j5Z4SmP7WgZb5CwAewTZLFwZNLSIUWeN3LvbRigFOCfHNSquGlOm2HKOrYrTqF58zJvCEbt00Civ%2FKoaLNPwmmRldpPAct35p1FXCiGCmSiuPU6P1IquPCc3FqeD5YVvBBoRpwZ2bEU4wpt0yFfYzghFxCL93UFFSeGMD2KGr%2FqWbis77O9gbSG54wVGdkA%2BdoS8H8KGXOQuQW4LMK%2FvjL0GOqUBlw2tQrVJT1NmCo8uM5ll09YY08tdIcr0m3tTerYce3wHqNjDtmS%2Bc6sxwY81frI0z%2FOARgTLBd%2F28bqPVsfaTNPwuQA7unBEonNI9gQBirWs%2FEDIB5oJ8fWuj8vt%2Bdps5vXmJqB17kU2IYSo%2FA%2Bnya9gBwBAiWmW0jWPPaO%2B580qmhU1g7c4O4BOoKFbqGUMy0skfHHFgb6KGmHTuIqUppkfk1Dn&X-Amz-Signature=843e072a838be76d5ab77543b1172b0bd3206b2b057426d333907a1098498abd&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YP7OHMUL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIHFjCNC12rtdAqIy55pbPYXchNNcnSo5CXZmteJXkPKPAiAF8puZm%2FcEgk7nn%2BBVVlgckx0vRh9pjRsCGZcsimRZXSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMhCvKOkXel7mNhU%2B%2BKtwDQbzsxEt6%2BCLUKcbNADnVhJJM8vbCyiPz%2B92U%2B2fOkCO5CXWUBg319kcFq0PctDpM8icTHwNACF2RBNma%2BGTzpIIR3%2FfrYk3%2FLUYCx4tLzrrGCACVVoMboknjCwjYbA4fwymsWOYXSW7C0v81SY9rkA31UWo1b7SRLMASO3amSADR7fPFnnm6hp6tuHdQWgRDQemHOnkKSk7%2FxC86nRghizM0R2kgCeFyKPD90qdw5%2BfXcBSLXxLlQJ3qwdop5nZP%2ButcwG6KHV6UwPEfMq7ejL%2Fb%2Fd3S7YM1g5Hi1Sfah3fJpxPT17%2BgW%2BdYEOp5Aoe6fraoofDaJcfQILqkUCzMV0NlSWRhFI7TGwiNCM5XvEu2lLivhwi28GheG1F7YOskf39xrLBXVcD6lqBHvPxER80b5PqWt5Nf1ge4dp8c%2BL5bGoi90PWvEzNv2bD%2B6okJhumQ%2FpuLF6bocLHFBO7vCydsO9Gpq%2Fn2b0R%2Fh1YsKS0cEfmH40jiV5DfYS2cq4oXsx%2FD%2F7z2laqEz7of9tWdIF4applXybCPxK1Mggcy1z3bTW%2BBkslthA%2BzMtj1x2S993L%2B6pHU6iawscSe2Yqh9hmEFy5EboTQL8G6WTyqSPjdQ4uUn6sFx59pDbowxO%2BMvQY6pgEUmx64i5AteX%2FDSBVii9TlfzP%2B15IufFONI1AVebXVNXNPizT4DutupLUABi%2FjV7xobaoA3GOF9BIoTlHNSVJkvPZvQpdpQKc5HATHSKhQCAoEc%2BGFXjW9CNSK9R9Eiy3wrKtVCdTSlS1jvbMdzkStRjpwCqDH1zWuYqbRquv5VytB2%2F3M7bSpmRrdHdm1QdoBEFRY2Pb0P4e4Ur3AN4Pz5m8KQHn9&X-Amz-Signature=cb6057abba720c82ea7ea2c5768ec072c9589e302f046742e82cb9f65923c1ba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNCJPRH7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCID%2FyA5ny16vvwpbI7ChSXZ14MwKsHO2ttxZVCcG6o7a7AiEAm9QGyhmQ2VJe%2B4gb4orGmqHP6xvv30lLT8Hk6L6gneoq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDP63NYXnzUnXdBwmtircAz7FN%2B4MMt%2B10WS9qdd4OUaxD9Sd%2FE22aG9w1vdtejPfsgl525v7d9zzSJ%2FsulkiKCFaIDUMuoPAGICvaRZrvdHcLymM1RiehpiE7p9KnipijLubKY9zmRPhYz5n%2BMr5hUk9mHi6AHFQ0Gnlc17gPshjPLIyx5tcYRem6gVMVppGM%2F0io%2FcAKAmUR4jLLbnS3FhsrS3WiY6yPQxNoMBVG%2FTy7WEkkJsOJes3iKwN2tPnVeDlXDtLjv34EmJGnjeUfJZp7SEkdPo3GLDCEDk7QD%2F%2FxOTu%2FcBTEGhsh%2FgBaN9EN93VpcGfH8AGxV4CmdmB6UlKh%2Fjwp%2F5MrO88XEycBAjl0K550S5KvtqZH5JG8Jw0NqXgWPXrBTWmduhMzEKBUfHt7nDiZx%2BfHznvlFZcZjwbuXawSQCM7%2B5KQEtlkQHmzk0JAKt2lVNwO%2Bv5Qdk0xwNQvg06QCo6JQotPFqhKI9b6cvxlDEE4XIrReTFhMR5L7iyz27Sft4gKFPYCZOfNL5kohqvmjE3hsGOIcL%2Bi3fabVoIb5TB7%2B4GXx13PSaMcROVdMe6%2F%2FSxS0PJmlymnNJfyLeww%2F2oVeaUzJHIe5ysklW4XkE8t5PgnBYvlO1XCusQHzi9wu5UCHAXMKPvjL0GOqUBtSndNiH2FRDUOmtDZnY9ydFevO6pMJ1hXn11XfCUjkNVNIuYHWHHHOaNssjex5XJR%2B08ctSblo5TfksWcyCHDQ%2BoJc2JFxPoCAUX5Buh%2Fz4PQmwKAPSaYK4f5yvc2M%2BVtw0in82o4c175SZnONb%2BTjmkxVxDG79Da4GoDgSlurs5IWteIWNseVdQEK8tphh3oiMk%2Fg7Pzr0bsLZNXOKg0m2%2FHoGA&X-Amz-Signature=b68a1482921a32198e13d0ff1233751005702d77c2f5d8fccbeab554d30ac8cf&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNCJPRH7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCID%2FyA5ny16vvwpbI7ChSXZ14MwKsHO2ttxZVCcG6o7a7AiEAm9QGyhmQ2VJe%2B4gb4orGmqHP6xvv30lLT8Hk6L6gneoq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDP63NYXnzUnXdBwmtircAz7FN%2B4MMt%2B10WS9qdd4OUaxD9Sd%2FE22aG9w1vdtejPfsgl525v7d9zzSJ%2FsulkiKCFaIDUMuoPAGICvaRZrvdHcLymM1RiehpiE7p9KnipijLubKY9zmRPhYz5n%2BMr5hUk9mHi6AHFQ0Gnlc17gPshjPLIyx5tcYRem6gVMVppGM%2F0io%2FcAKAmUR4jLLbnS3FhsrS3WiY6yPQxNoMBVG%2FTy7WEkkJsOJes3iKwN2tPnVeDlXDtLjv34EmJGnjeUfJZp7SEkdPo3GLDCEDk7QD%2F%2FxOTu%2FcBTEGhsh%2FgBaN9EN93VpcGfH8AGxV4CmdmB6UlKh%2Fjwp%2F5MrO88XEycBAjl0K550S5KvtqZH5JG8Jw0NqXgWPXrBTWmduhMzEKBUfHt7nDiZx%2BfHznvlFZcZjwbuXawSQCM7%2B5KQEtlkQHmzk0JAKt2lVNwO%2Bv5Qdk0xwNQvg06QCo6JQotPFqhKI9b6cvxlDEE4XIrReTFhMR5L7iyz27Sft4gKFPYCZOfNL5kohqvmjE3hsGOIcL%2Bi3fabVoIb5TB7%2B4GXx13PSaMcROVdMe6%2F%2FSxS0PJmlymnNJfyLeww%2F2oVeaUzJHIe5ysklW4XkE8t5PgnBYvlO1XCusQHzi9wu5UCHAXMKPvjL0GOqUBtSndNiH2FRDUOmtDZnY9ydFevO6pMJ1hXn11XfCUjkNVNIuYHWHHHOaNssjex5XJR%2B08ctSblo5TfksWcyCHDQ%2BoJc2JFxPoCAUX5Buh%2Fz4PQmwKAPSaYK4f5yvc2M%2BVtw0in82o4c175SZnONb%2BTjmkxVxDG79Da4GoDgSlurs5IWteIWNseVdQEK8tphh3oiMk%2Fg7Pzr0bsLZNXOKg0m2%2FHoGA&X-Amz-Signature=edf1d3f64d605fc06b9b5e4a4f136ea9b6c29a8c15edce4a2e568ca57be004e6&X-Amz-SignedHeaders=host&x-id=GetObject)

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
