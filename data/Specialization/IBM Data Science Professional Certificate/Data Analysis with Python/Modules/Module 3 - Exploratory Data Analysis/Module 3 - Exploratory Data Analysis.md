

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624KUJJFJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDWjk%2FR4JsNLgsagHTPsj6WZv8lNbsxBdHEb3W13gRUPgIgbWzuwklK4M0Hx7NmC1NUyC79IJ61Qtdz3dlWweHHdDoqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBkLENc%2B6Ezp8H3KQSrcA%2F5oo1nbtWo3%2Fpan0Aty3GfKwNtV9JhssOxserSKmIBGi%2F1qp7ZGs8OIXJbg7NerSXC9dsnf9UWYKv3Z%2FxTN0Ep%2F2C3m%2FsbQMuffcaPSxs74pF3yCSlF9W%2BSrIMxAs6t2sE9MOCQPrXFgE4VH0eGCuVm66QZkVS0q8JbNCxO48TQxtKVi%2FJXIQbNjcs9pU2FcEiv7i%2Bw%2Fj%2BZhgfWYkvBkrVHKvrH4UaasLf4pewfKG97N43ifd9R3EAu3LbWSO1Jga0KzWmh821KkSTSVM4paRv%2Fq6rf65Fw3iPu9H%2B4WEzBBN7hYiGYUgLrMpkc0XbdMR6x8ihlrjKm4mXATkdRVoalX6mU8NXgwhk%2FH6Jn3veiNyzLYA0wBfbpeklgbnBzzrZPoONEz35Q93BIwlz%2Fa4B7FmgynFtvfA6jneSJxp201WJgnitKPtLDuZiVgwyKR7PcpjCwyE7KXAD8Uf1GdjzcVu9H4%2BNdsKiGNwEq0CCRZahewBvJt%2BTZ2O48LNLFkmBw6383wrvMZNDN09G89q%2F2XKPiA%2FFUXLVTWwR2r7fE%2BW1x%2BiJ8LHLxFegKv8Z7xcTEUnT7DoCNIjoRTtMjDOi%2BhXNYrajwJ2QUUYn%2FykY9h%2FqDK5AQvtl%2BEbkmMMy65rwGOqUBhX3jvTWdYihsN7SMPeH8%2F5nhmpburAuysLacQ%2BZnsYsuHVc%2FbOWwXyyKFXcPYHFBLoKZazI5wVxEVqPGCk9GRETatWbTd0GZpA3bUDy43RYFEusKQRJuOwJGKf9dr8KiCg24YYhp%2FrYcW4sOJlGSxtBRon5ZCnOAYAP%2F%2FriskEqn60tfmYwVMfe5miO4pzzLHQGfgsMGwqCmFTo5eCOZuIrjgVRq&X-Amz-Signature=5958f74c8fb32054cc4fc3f2d93367741aaabef0425efe9e860c2fda6a011081&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624KUJJFJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDWjk%2FR4JsNLgsagHTPsj6WZv8lNbsxBdHEb3W13gRUPgIgbWzuwklK4M0Hx7NmC1NUyC79IJ61Qtdz3dlWweHHdDoqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBkLENc%2B6Ezp8H3KQSrcA%2F5oo1nbtWo3%2Fpan0Aty3GfKwNtV9JhssOxserSKmIBGi%2F1qp7ZGs8OIXJbg7NerSXC9dsnf9UWYKv3Z%2FxTN0Ep%2F2C3m%2FsbQMuffcaPSxs74pF3yCSlF9W%2BSrIMxAs6t2sE9MOCQPrXFgE4VH0eGCuVm66QZkVS0q8JbNCxO48TQxtKVi%2FJXIQbNjcs9pU2FcEiv7i%2Bw%2Fj%2BZhgfWYkvBkrVHKvrH4UaasLf4pewfKG97N43ifd9R3EAu3LbWSO1Jga0KzWmh821KkSTSVM4paRv%2Fq6rf65Fw3iPu9H%2B4WEzBBN7hYiGYUgLrMpkc0XbdMR6x8ihlrjKm4mXATkdRVoalX6mU8NXgwhk%2FH6Jn3veiNyzLYA0wBfbpeklgbnBzzrZPoONEz35Q93BIwlz%2Fa4B7FmgynFtvfA6jneSJxp201WJgnitKPtLDuZiVgwyKR7PcpjCwyE7KXAD8Uf1GdjzcVu9H4%2BNdsKiGNwEq0CCRZahewBvJt%2BTZ2O48LNLFkmBw6383wrvMZNDN09G89q%2F2XKPiA%2FFUXLVTWwR2r7fE%2BW1x%2BiJ8LHLxFegKv8Z7xcTEUnT7DoCNIjoRTtMjDOi%2BhXNYrajwJ2QUUYn%2FykY9h%2FqDK5AQvtl%2BEbkmMMy65rwGOqUBhX3jvTWdYihsN7SMPeH8%2F5nhmpburAuysLacQ%2BZnsYsuHVc%2FbOWwXyyKFXcPYHFBLoKZazI5wVxEVqPGCk9GRETatWbTd0GZpA3bUDy43RYFEusKQRJuOwJGKf9dr8KiCg24YYhp%2FrYcW4sOJlGSxtBRon5ZCnOAYAP%2F%2FriskEqn60tfmYwVMfe5miO4pzzLHQGfgsMGwqCmFTo5eCOZuIrjgVRq&X-Amz-Signature=08f74eed7f5c7419e1b30121e67e8771d4227370ce5431f436673a778edd59bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624KUJJFJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDWjk%2FR4JsNLgsagHTPsj6WZv8lNbsxBdHEb3W13gRUPgIgbWzuwklK4M0Hx7NmC1NUyC79IJ61Qtdz3dlWweHHdDoqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBkLENc%2B6Ezp8H3KQSrcA%2F5oo1nbtWo3%2Fpan0Aty3GfKwNtV9JhssOxserSKmIBGi%2F1qp7ZGs8OIXJbg7NerSXC9dsnf9UWYKv3Z%2FxTN0Ep%2F2C3m%2FsbQMuffcaPSxs74pF3yCSlF9W%2BSrIMxAs6t2sE9MOCQPrXFgE4VH0eGCuVm66QZkVS0q8JbNCxO48TQxtKVi%2FJXIQbNjcs9pU2FcEiv7i%2Bw%2Fj%2BZhgfWYkvBkrVHKvrH4UaasLf4pewfKG97N43ifd9R3EAu3LbWSO1Jga0KzWmh821KkSTSVM4paRv%2Fq6rf65Fw3iPu9H%2B4WEzBBN7hYiGYUgLrMpkc0XbdMR6x8ihlrjKm4mXATkdRVoalX6mU8NXgwhk%2FH6Jn3veiNyzLYA0wBfbpeklgbnBzzrZPoONEz35Q93BIwlz%2Fa4B7FmgynFtvfA6jneSJxp201WJgnitKPtLDuZiVgwyKR7PcpjCwyE7KXAD8Uf1GdjzcVu9H4%2BNdsKiGNwEq0CCRZahewBvJt%2BTZ2O48LNLFkmBw6383wrvMZNDN09G89q%2F2XKPiA%2FFUXLVTWwR2r7fE%2BW1x%2BiJ8LHLxFegKv8Z7xcTEUnT7DoCNIjoRTtMjDOi%2BhXNYrajwJ2QUUYn%2FykY9h%2FqDK5AQvtl%2BEbkmMMy65rwGOqUBhX3jvTWdYihsN7SMPeH8%2F5nhmpburAuysLacQ%2BZnsYsuHVc%2FbOWwXyyKFXcPYHFBLoKZazI5wVxEVqPGCk9GRETatWbTd0GZpA3bUDy43RYFEusKQRJuOwJGKf9dr8KiCg24YYhp%2FrYcW4sOJlGSxtBRon5ZCnOAYAP%2F%2FriskEqn60tfmYwVMfe5miO4pzzLHQGfgsMGwqCmFTo5eCOZuIrjgVRq&X-Amz-Signature=91c714531290f5317f345749e028ee7a21126e897c258bccb47ad9a9b2b71ba9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EHYGPBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFs2%2Fuc6jJ6tapQDkgjDXf%2BLv7gzl6OEii7q1aDdX%2FP%2BAiEA6JUzl0nyutecHoPj7d8haInvyZuDaUsakjpQ4AnjIuUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHnPWt9G4l7ljLkeVSrcA630GNkxCPOc%2FKMLTtfimhSYdzoRyIG%2BnYsAZtw8arkyck244AGtmTSOidIEGiy45Gg6gw3QKBWihoNz1tmQ4G5So1lSc3GerOtIDKcVto7p6QR5zKhblXpA%2BwX%2FX9io%2F6%2BdKK%2FYLY9rMP9cywJW0QUskItWKAPiJTnxGOL%2FT0pSRlP2F3dBqKU25ZEc8fuGX92VtjHVukp6FsmRJ%2BXvLjDu3OM8qL2cMGZKDgKPBmjR5yNZX7jkly%2FGM47AEBwDKyvjXcHDMEZPBcjgnqJrk8PEbf3Dl8B5lRSqNts6YazWvgqpJww1vV2Gv8ABiuqAZTQ4G2lyM1VGv9DpWhSV9DfKoxa%2FLEcEy2jGMHsAU6ir23J8F%2FvLGQ%2Fj3BH7dtm2MHKw0Pe5mEKP1%2BMFQ8J3%2Fyiyfb8PC8s78uJDmbBjsR5Af%2FfGpBwkh6bw2%2BxKwov6kj2kWE7ORkT94neRrMR1KtoNvMrHCVJUp5O2L6wEG4oiAWha7h0HcTOHUp1cv%2Fq3Zme5Quo%2F37TD6kF55P511DEjw5yzEa49ICljOcczoSTNRV0KsKbzcN2pbkHXh3O9UU699ihp80j%2BTVX2aS%2BSvwWq7ZSlK0oFnIOuGDDKnNGhmevkvv8F1eiKXGqeMN265rwGOqUBLn7qnOVEn9W1cHeeDCcrtA4VAnLCfm5MacW2mAmgM%2Bn8VmC2ojsD7Ua4yUuqbRYvVrWtjqeaf36JTu4guPH4WIFvUadxWhusehA2ZeJytZssZxUhbI8FLjVdlsXW4VyUfLIZRWBqg7tWgJSONTSy23FKj%2BubI1oLjmKesQUNwu7jD9pz%2FMqD%2FLPjyiFKztp3knrPF5xsR1Ywzbe33Ov868zVq8lv&X-Amz-Signature=0b961fd09d35fe392aaabe8a4117606cd2527cd628ed5eaa3a6faf018d36f017&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EHYGPBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFs2%2Fuc6jJ6tapQDkgjDXf%2BLv7gzl6OEii7q1aDdX%2FP%2BAiEA6JUzl0nyutecHoPj7d8haInvyZuDaUsakjpQ4AnjIuUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHnPWt9G4l7ljLkeVSrcA630GNkxCPOc%2FKMLTtfimhSYdzoRyIG%2BnYsAZtw8arkyck244AGtmTSOidIEGiy45Gg6gw3QKBWihoNz1tmQ4G5So1lSc3GerOtIDKcVto7p6QR5zKhblXpA%2BwX%2FX9io%2F6%2BdKK%2FYLY9rMP9cywJW0QUskItWKAPiJTnxGOL%2FT0pSRlP2F3dBqKU25ZEc8fuGX92VtjHVukp6FsmRJ%2BXvLjDu3OM8qL2cMGZKDgKPBmjR5yNZX7jkly%2FGM47AEBwDKyvjXcHDMEZPBcjgnqJrk8PEbf3Dl8B5lRSqNts6YazWvgqpJww1vV2Gv8ABiuqAZTQ4G2lyM1VGv9DpWhSV9DfKoxa%2FLEcEy2jGMHsAU6ir23J8F%2FvLGQ%2Fj3BH7dtm2MHKw0Pe5mEKP1%2BMFQ8J3%2Fyiyfb8PC8s78uJDmbBjsR5Af%2FfGpBwkh6bw2%2BxKwov6kj2kWE7ORkT94neRrMR1KtoNvMrHCVJUp5O2L6wEG4oiAWha7h0HcTOHUp1cv%2Fq3Zme5Quo%2F37TD6kF55P511DEjw5yzEa49ICljOcczoSTNRV0KsKbzcN2pbkHXh3O9UU699ihp80j%2BTVX2aS%2BSvwWq7ZSlK0oFnIOuGDDKnNGhmevkvv8F1eiKXGqeMN265rwGOqUBLn7qnOVEn9W1cHeeDCcrtA4VAnLCfm5MacW2mAmgM%2Bn8VmC2ojsD7Ua4yUuqbRYvVrWtjqeaf36JTu4guPH4WIFvUadxWhusehA2ZeJytZssZxUhbI8FLjVdlsXW4VyUfLIZRWBqg7tWgJSONTSy23FKj%2BubI1oLjmKesQUNwu7jD9pz%2FMqD%2FLPjyiFKztp3knrPF5xsR1Ywzbe33Ov868zVq8lv&X-Amz-Signature=255e016de66c8d89ab3506fb581fb8ea0821f6b2c2148e7584a6cdce0e1d7311&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EHYGPBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFs2%2Fuc6jJ6tapQDkgjDXf%2BLv7gzl6OEii7q1aDdX%2FP%2BAiEA6JUzl0nyutecHoPj7d8haInvyZuDaUsakjpQ4AnjIuUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHnPWt9G4l7ljLkeVSrcA630GNkxCPOc%2FKMLTtfimhSYdzoRyIG%2BnYsAZtw8arkyck244AGtmTSOidIEGiy45Gg6gw3QKBWihoNz1tmQ4G5So1lSc3GerOtIDKcVto7p6QR5zKhblXpA%2BwX%2FX9io%2F6%2BdKK%2FYLY9rMP9cywJW0QUskItWKAPiJTnxGOL%2FT0pSRlP2F3dBqKU25ZEc8fuGX92VtjHVukp6FsmRJ%2BXvLjDu3OM8qL2cMGZKDgKPBmjR5yNZX7jkly%2FGM47AEBwDKyvjXcHDMEZPBcjgnqJrk8PEbf3Dl8B5lRSqNts6YazWvgqpJww1vV2Gv8ABiuqAZTQ4G2lyM1VGv9DpWhSV9DfKoxa%2FLEcEy2jGMHsAU6ir23J8F%2FvLGQ%2Fj3BH7dtm2MHKw0Pe5mEKP1%2BMFQ8J3%2Fyiyfb8PC8s78uJDmbBjsR5Af%2FfGpBwkh6bw2%2BxKwov6kj2kWE7ORkT94neRrMR1KtoNvMrHCVJUp5O2L6wEG4oiAWha7h0HcTOHUp1cv%2Fq3Zme5Quo%2F37TD6kF55P511DEjw5yzEa49ICljOcczoSTNRV0KsKbzcN2pbkHXh3O9UU699ihp80j%2BTVX2aS%2BSvwWq7ZSlK0oFnIOuGDDKnNGhmevkvv8F1eiKXGqeMN265rwGOqUBLn7qnOVEn9W1cHeeDCcrtA4VAnLCfm5MacW2mAmgM%2Bn8VmC2ojsD7Ua4yUuqbRYvVrWtjqeaf36JTu4guPH4WIFvUadxWhusehA2ZeJytZssZxUhbI8FLjVdlsXW4VyUfLIZRWBqg7tWgJSONTSy23FKj%2BubI1oLjmKesQUNwu7jD9pz%2FMqD%2FLPjyiFKztp3knrPF5xsR1Ywzbe33Ov868zVq8lv&X-Amz-Signature=f11b541ce22ecf1b75570cd33e709c002c91a68018736025c88cb0079f348fd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EHYGPBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFs2%2Fuc6jJ6tapQDkgjDXf%2BLv7gzl6OEii7q1aDdX%2FP%2BAiEA6JUzl0nyutecHoPj7d8haInvyZuDaUsakjpQ4AnjIuUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHnPWt9G4l7ljLkeVSrcA630GNkxCPOc%2FKMLTtfimhSYdzoRyIG%2BnYsAZtw8arkyck244AGtmTSOidIEGiy45Gg6gw3QKBWihoNz1tmQ4G5So1lSc3GerOtIDKcVto7p6QR5zKhblXpA%2BwX%2FX9io%2F6%2BdKK%2FYLY9rMP9cywJW0QUskItWKAPiJTnxGOL%2FT0pSRlP2F3dBqKU25ZEc8fuGX92VtjHVukp6FsmRJ%2BXvLjDu3OM8qL2cMGZKDgKPBmjR5yNZX7jkly%2FGM47AEBwDKyvjXcHDMEZPBcjgnqJrk8PEbf3Dl8B5lRSqNts6YazWvgqpJww1vV2Gv8ABiuqAZTQ4G2lyM1VGv9DpWhSV9DfKoxa%2FLEcEy2jGMHsAU6ir23J8F%2FvLGQ%2Fj3BH7dtm2MHKw0Pe5mEKP1%2BMFQ8J3%2Fyiyfb8PC8s78uJDmbBjsR5Af%2FfGpBwkh6bw2%2BxKwov6kj2kWE7ORkT94neRrMR1KtoNvMrHCVJUp5O2L6wEG4oiAWha7h0HcTOHUp1cv%2Fq3Zme5Quo%2F37TD6kF55P511DEjw5yzEa49ICljOcczoSTNRV0KsKbzcN2pbkHXh3O9UU699ihp80j%2BTVX2aS%2BSvwWq7ZSlK0oFnIOuGDDKnNGhmevkvv8F1eiKXGqeMN265rwGOqUBLn7qnOVEn9W1cHeeDCcrtA4VAnLCfm5MacW2mAmgM%2Bn8VmC2ojsD7Ua4yUuqbRYvVrWtjqeaf36JTu4guPH4WIFvUadxWhusehA2ZeJytZssZxUhbI8FLjVdlsXW4VyUfLIZRWBqg7tWgJSONTSy23FKj%2BubI1oLjmKesQUNwu7jD9pz%2FMqD%2FLPjyiFKztp3knrPF5xsR1Ywzbe33Ov868zVq8lv&X-Amz-Signature=a9166e1c849953904044d0f2bef9a9d4f6d8db64c17843232fbddd12826289f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EHYGPBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFs2%2Fuc6jJ6tapQDkgjDXf%2BLv7gzl6OEii7q1aDdX%2FP%2BAiEA6JUzl0nyutecHoPj7d8haInvyZuDaUsakjpQ4AnjIuUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHnPWt9G4l7ljLkeVSrcA630GNkxCPOc%2FKMLTtfimhSYdzoRyIG%2BnYsAZtw8arkyck244AGtmTSOidIEGiy45Gg6gw3QKBWihoNz1tmQ4G5So1lSc3GerOtIDKcVto7p6QR5zKhblXpA%2BwX%2FX9io%2F6%2BdKK%2FYLY9rMP9cywJW0QUskItWKAPiJTnxGOL%2FT0pSRlP2F3dBqKU25ZEc8fuGX92VtjHVukp6FsmRJ%2BXvLjDu3OM8qL2cMGZKDgKPBmjR5yNZX7jkly%2FGM47AEBwDKyvjXcHDMEZPBcjgnqJrk8PEbf3Dl8B5lRSqNts6YazWvgqpJww1vV2Gv8ABiuqAZTQ4G2lyM1VGv9DpWhSV9DfKoxa%2FLEcEy2jGMHsAU6ir23J8F%2FvLGQ%2Fj3BH7dtm2MHKw0Pe5mEKP1%2BMFQ8J3%2Fyiyfb8PC8s78uJDmbBjsR5Af%2FfGpBwkh6bw2%2BxKwov6kj2kWE7ORkT94neRrMR1KtoNvMrHCVJUp5O2L6wEG4oiAWha7h0HcTOHUp1cv%2Fq3Zme5Quo%2F37TD6kF55P511DEjw5yzEa49ICljOcczoSTNRV0KsKbzcN2pbkHXh3O9UU699ihp80j%2BTVX2aS%2BSvwWq7ZSlK0oFnIOuGDDKnNGhmevkvv8F1eiKXGqeMN265rwGOqUBLn7qnOVEn9W1cHeeDCcrtA4VAnLCfm5MacW2mAmgM%2Bn8VmC2ojsD7Ua4yUuqbRYvVrWtjqeaf36JTu4guPH4WIFvUadxWhusehA2ZeJytZssZxUhbI8FLjVdlsXW4VyUfLIZRWBqg7tWgJSONTSy23FKj%2BubI1oLjmKesQUNwu7jD9pz%2FMqD%2FLPjyiFKztp3knrPF5xsR1Ywzbe33Ov868zVq8lv&X-Amz-Signature=c004a7dfea83db1a71b7f797952197cf933afc07ef34edc8a0656f5467a8054e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EHYGPBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFs2%2Fuc6jJ6tapQDkgjDXf%2BLv7gzl6OEii7q1aDdX%2FP%2BAiEA6JUzl0nyutecHoPj7d8haInvyZuDaUsakjpQ4AnjIuUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHnPWt9G4l7ljLkeVSrcA630GNkxCPOc%2FKMLTtfimhSYdzoRyIG%2BnYsAZtw8arkyck244AGtmTSOidIEGiy45Gg6gw3QKBWihoNz1tmQ4G5So1lSc3GerOtIDKcVto7p6QR5zKhblXpA%2BwX%2FX9io%2F6%2BdKK%2FYLY9rMP9cywJW0QUskItWKAPiJTnxGOL%2FT0pSRlP2F3dBqKU25ZEc8fuGX92VtjHVukp6FsmRJ%2BXvLjDu3OM8qL2cMGZKDgKPBmjR5yNZX7jkly%2FGM47AEBwDKyvjXcHDMEZPBcjgnqJrk8PEbf3Dl8B5lRSqNts6YazWvgqpJww1vV2Gv8ABiuqAZTQ4G2lyM1VGv9DpWhSV9DfKoxa%2FLEcEy2jGMHsAU6ir23J8F%2FvLGQ%2Fj3BH7dtm2MHKw0Pe5mEKP1%2BMFQ8J3%2Fyiyfb8PC8s78uJDmbBjsR5Af%2FfGpBwkh6bw2%2BxKwov6kj2kWE7ORkT94neRrMR1KtoNvMrHCVJUp5O2L6wEG4oiAWha7h0HcTOHUp1cv%2Fq3Zme5Quo%2F37TD6kF55P511DEjw5yzEa49ICljOcczoSTNRV0KsKbzcN2pbkHXh3O9UU699ihp80j%2BTVX2aS%2BSvwWq7ZSlK0oFnIOuGDDKnNGhmevkvv8F1eiKXGqeMN265rwGOqUBLn7qnOVEn9W1cHeeDCcrtA4VAnLCfm5MacW2mAmgM%2Bn8VmC2ojsD7Ua4yUuqbRYvVrWtjqeaf36JTu4guPH4WIFvUadxWhusehA2ZeJytZssZxUhbI8FLjVdlsXW4VyUfLIZRWBqg7tWgJSONTSy23FKj%2BubI1oLjmKesQUNwu7jD9pz%2FMqD%2FLPjyiFKztp3knrPF5xsR1Ywzbe33Ov868zVq8lv&X-Amz-Signature=6828a1a4b1c2c898904040887c8a3ada822b8a8bfbbc788aee1fb55b682cebb4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCI7IJHD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFSu7chdbsizVbAI4yEZWyHDrD3kprc91JaSA48W6hLZAiEAp%2F8y6awrq84eyBD5DfyrFb1Kr1Et6%2B%2BsZZOpcbf4ZZkqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCAQeTZ8eeNEYbrFLircA4oLxznu5NglWbHnXvtedTUXMyKTwB4%2BnyCnXz8A%2FKPBsc68yppMJS98QCb3OzXUpL5ojbdD0BFUK6K8IK6wD9HMBQPdCwtKSOy1nspRuxqyKOVKrN%2BhcHZ70xIYQE2qvfA%2B9Gb4cXUQYvRH9iLthdrK2opIwyTZnbFhoGdoCNJISOIgAn6cHGQMB%2FFxMOYwOKWA7G8vr8W2gD6KOrfWmH1cZw5GAa5fDIa8d4dIaCaw1oLt56IPKG3eHAvMekiw3kKJwmWhIPXydpRLqydJsMttX9zZ9X7BUjvwcUs8pnXN2Hvil8606PvFsxk2hJN57VJ5WYI3rqIy9VF9nDkOigVRAkcqw9oXxl107gx4bNp8SaGYxuy75IjU1M4BiAKGLXUsuw%2FpTeyUUnC01tWtuHtNzD9FyhTyv6ZXCpcePPCkVPCqi5wnpIBD0G%2FnoWUTux45tj13ix35KhQF7MGV6idv%2FTiv3QIBPFFP%2Bl716LfSuOzV%2FPO6SZBJe9yM52%2F9AsYI1hbzvs69K7i0AChVxU%2FZodQZ8oWre4Xy%2BbXkeWYC9ii3VJoDTg8jGLGj157WoHmoSMXI0bOMPfLtYOO5lDvDM0YeDs8c3%2FnQ6YdNlB4iEq5Sc06w7d%2B5TxxOMI675rwGOqUBNxpO08QzYNvCCnHQHSlfTbgeBgYPXlyYtWepZyPnSnvitvRTRg0f7bKZ%2FEUYGu%2BrYUPupJVNGL%2BZb%2FJEsg456W1Jx9WfFDRm7nqexBnhQQeW%2BSoQD8zJidHTXQ4eRScm%2BxFiyvJRJs5ZBksU67Dvk6kW9d%2FV1qqwnmOlolYerJ2koiXdfxP%2Fz%2FBr80rWY9Ev%2FQ5xpV6ALFUq670iwhpSy%2BS9EnjM&X-Amz-Signature=d8adb19d5541241f1a67b9be3545698ef035b5b6713c826c8989d5f2369559cc&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTW3WEDS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCpndUZPXnsL9VzeXD3ucnPGoMpxGfvPUCY%2B8mEqyBvuwIgYqeuL15tbGMj%2BbLapZnyj%2B%2Bb7RHNisJGfUk2izMahM4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB83mrpbWq3ovc0PDyrcA604i0Vxudg6SzfITrt4WHSOZIclQFtDwb3EkUdlNaTTYXvL%2BNWvNG%2BDov2qwePD%2F8xiOlhBzuW7HILs1Z8JHI3XDW11bdY0rQsDQxfW%2FXo1cB%2BygPTLNngjR%2BV0nmTBPKcB9FX1yUYwQ6jbv5sI566DKGP1X%2FLJUpine2dOjWBQv%2BNOnun5OT%2B%2B3oHMNpZJGc9wpVDhLGMNoA6K8GwJiwdAY0ziyDb7k9QC5U9fMQtm3t62innHVcKBYE%2BVa%2Fa6c3obdvk5gfy3bfCd3vQyzcNrwjdnWWoD%2F2nNAOzlAVc2FEZd6ZasWN8suK8Eyx1%2FZl3%2FacANe1QUdDKcTQsUe%2BNOW%2B851DQwdMr1FXIm0DuFdXDx6msTflEETgUVI4idcNFNyOs2NR9DaGn4MPQwVDoyAGZSfIAenXoTg5KkIkzu%2FoB0w596ESMY0cKV8Xamyp1cV0rDZaNTthCn%2FbBHLHR12TXJIhvNCJ%2F6qBMlNgcOX6rgHhT1DY7RTfLu8hoClSzsmiidfQ25irmNOZqgQf1hdGt54Ek1pfxv2DldojQxLdE2zghnFLjjIsobWIrz6vybmjayeDng2rAvq0NZiSTImEjPHEpuzVdvcyCXw1GR1pdviMdUCl7LdhRHMJG75rwGOqUBjwAQH6%2BdAst5JDOArTNhjDQA7F6UvUyqArakr%2Bd2r3H0X9o1FwD8lUmogdAxN1hZ2RAtl28pYZ4SjkCSrrUDwx7HOGQr%2F5nNQrpMxFVmUx6KEIyJH6Gd8vITGKz%2FBO5RI7ZBVOl%2FYJIdIptH6yTOWEg6GNWTQ8RDnvZ2Pa4mCI7F26ctWqHNXLTxkyGTXibSuGJ9qjo3WpcoP5waZ456V5GfQTRK&X-Amz-Signature=625b783b8fa607f8b5e03bc4903e86442acd43f144320f17f4a8a4b386e30dd9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EHYGPBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFs2%2Fuc6jJ6tapQDkgjDXf%2BLv7gzl6OEii7q1aDdX%2FP%2BAiEA6JUzl0nyutecHoPj7d8haInvyZuDaUsakjpQ4AnjIuUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHnPWt9G4l7ljLkeVSrcA630GNkxCPOc%2FKMLTtfimhSYdzoRyIG%2BnYsAZtw8arkyck244AGtmTSOidIEGiy45Gg6gw3QKBWihoNz1tmQ4G5So1lSc3GerOtIDKcVto7p6QR5zKhblXpA%2BwX%2FX9io%2F6%2BdKK%2FYLY9rMP9cywJW0QUskItWKAPiJTnxGOL%2FT0pSRlP2F3dBqKU25ZEc8fuGX92VtjHVukp6FsmRJ%2BXvLjDu3OM8qL2cMGZKDgKPBmjR5yNZX7jkly%2FGM47AEBwDKyvjXcHDMEZPBcjgnqJrk8PEbf3Dl8B5lRSqNts6YazWvgqpJww1vV2Gv8ABiuqAZTQ4G2lyM1VGv9DpWhSV9DfKoxa%2FLEcEy2jGMHsAU6ir23J8F%2FvLGQ%2Fj3BH7dtm2MHKw0Pe5mEKP1%2BMFQ8J3%2Fyiyfb8PC8s78uJDmbBjsR5Af%2FfGpBwkh6bw2%2BxKwov6kj2kWE7ORkT94neRrMR1KtoNvMrHCVJUp5O2L6wEG4oiAWha7h0HcTOHUp1cv%2Fq3Zme5Quo%2F37TD6kF55P511DEjw5yzEa49ICljOcczoSTNRV0KsKbzcN2pbkHXh3O9UU699ihp80j%2BTVX2aS%2BSvwWq7ZSlK0oFnIOuGDDKnNGhmevkvv8F1eiKXGqeMN265rwGOqUBLn7qnOVEn9W1cHeeDCcrtA4VAnLCfm5MacW2mAmgM%2Bn8VmC2ojsD7Ua4yUuqbRYvVrWtjqeaf36JTu4guPH4WIFvUadxWhusehA2ZeJytZssZxUhbI8FLjVdlsXW4VyUfLIZRWBqg7tWgJSONTSy23FKj%2BubI1oLjmKesQUNwu7jD9pz%2FMqD%2FLPjyiFKztp3knrPF5xsR1Ywzbe33Ov868zVq8lv&X-Amz-Signature=6de82ff621f040df2adc3198698a63b02db7ee8b50fa2142eac44688c3b52a42&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EHYGPBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFs2%2Fuc6jJ6tapQDkgjDXf%2BLv7gzl6OEii7q1aDdX%2FP%2BAiEA6JUzl0nyutecHoPj7d8haInvyZuDaUsakjpQ4AnjIuUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHnPWt9G4l7ljLkeVSrcA630GNkxCPOc%2FKMLTtfimhSYdzoRyIG%2BnYsAZtw8arkyck244AGtmTSOidIEGiy45Gg6gw3QKBWihoNz1tmQ4G5So1lSc3GerOtIDKcVto7p6QR5zKhblXpA%2BwX%2FX9io%2F6%2BdKK%2FYLY9rMP9cywJW0QUskItWKAPiJTnxGOL%2FT0pSRlP2F3dBqKU25ZEc8fuGX92VtjHVukp6FsmRJ%2BXvLjDu3OM8qL2cMGZKDgKPBmjR5yNZX7jkly%2FGM47AEBwDKyvjXcHDMEZPBcjgnqJrk8PEbf3Dl8B5lRSqNts6YazWvgqpJww1vV2Gv8ABiuqAZTQ4G2lyM1VGv9DpWhSV9DfKoxa%2FLEcEy2jGMHsAU6ir23J8F%2FvLGQ%2Fj3BH7dtm2MHKw0Pe5mEKP1%2BMFQ8J3%2Fyiyfb8PC8s78uJDmbBjsR5Af%2FfGpBwkh6bw2%2BxKwov6kj2kWE7ORkT94neRrMR1KtoNvMrHCVJUp5O2L6wEG4oiAWha7h0HcTOHUp1cv%2Fq3Zme5Quo%2F37TD6kF55P511DEjw5yzEa49ICljOcczoSTNRV0KsKbzcN2pbkHXh3O9UU699ihp80j%2BTVX2aS%2BSvwWq7ZSlK0oFnIOuGDDKnNGhmevkvv8F1eiKXGqeMN265rwGOqUBLn7qnOVEn9W1cHeeDCcrtA4VAnLCfm5MacW2mAmgM%2Bn8VmC2ojsD7Ua4yUuqbRYvVrWtjqeaf36JTu4guPH4WIFvUadxWhusehA2ZeJytZssZxUhbI8FLjVdlsXW4VyUfLIZRWBqg7tWgJSONTSy23FKj%2BubI1oLjmKesQUNwu7jD9pz%2FMqD%2FLPjyiFKztp3knrPF5xsR1Ywzbe33Ov868zVq8lv&X-Amz-Signature=2a8dbd68acfa191e0a3c2c9b2e55e96c302656e81c3cf9b0d29e4cd35c6dc572&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EHYGPBD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFs2%2Fuc6jJ6tapQDkgjDXf%2BLv7gzl6OEii7q1aDdX%2FP%2BAiEA6JUzl0nyutecHoPj7d8haInvyZuDaUsakjpQ4AnjIuUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHnPWt9G4l7ljLkeVSrcA630GNkxCPOc%2FKMLTtfimhSYdzoRyIG%2BnYsAZtw8arkyck244AGtmTSOidIEGiy45Gg6gw3QKBWihoNz1tmQ4G5So1lSc3GerOtIDKcVto7p6QR5zKhblXpA%2BwX%2FX9io%2F6%2BdKK%2FYLY9rMP9cywJW0QUskItWKAPiJTnxGOL%2FT0pSRlP2F3dBqKU25ZEc8fuGX92VtjHVukp6FsmRJ%2BXvLjDu3OM8qL2cMGZKDgKPBmjR5yNZX7jkly%2FGM47AEBwDKyvjXcHDMEZPBcjgnqJrk8PEbf3Dl8B5lRSqNts6YazWvgqpJww1vV2Gv8ABiuqAZTQ4G2lyM1VGv9DpWhSV9DfKoxa%2FLEcEy2jGMHsAU6ir23J8F%2FvLGQ%2Fj3BH7dtm2MHKw0Pe5mEKP1%2BMFQ8J3%2Fyiyfb8PC8s78uJDmbBjsR5Af%2FfGpBwkh6bw2%2BxKwov6kj2kWE7ORkT94neRrMR1KtoNvMrHCVJUp5O2L6wEG4oiAWha7h0HcTOHUp1cv%2Fq3Zme5Quo%2F37TD6kF55P511DEjw5yzEa49ICljOcczoSTNRV0KsKbzcN2pbkHXh3O9UU699ihp80j%2BTVX2aS%2BSvwWq7ZSlK0oFnIOuGDDKnNGhmevkvv8F1eiKXGqeMN265rwGOqUBLn7qnOVEn9W1cHeeDCcrtA4VAnLCfm5MacW2mAmgM%2Bn8VmC2ojsD7Ua4yUuqbRYvVrWtjqeaf36JTu4guPH4WIFvUadxWhusehA2ZeJytZssZxUhbI8FLjVdlsXW4VyUfLIZRWBqg7tWgJSONTSy23FKj%2BubI1oLjmKesQUNwu7jD9pz%2FMqD%2FLPjyiFKztp3knrPF5xsR1Ywzbe33Ov868zVq8lv&X-Amz-Signature=1e66b3d13434d81470ee6473040728e7a71d9794a66e290e120b15e9303d6087&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HXDB4F5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCfYtf4UK5stJIy7Fsgo6QbcWcQG%2BXUucYBCxPFINUWrgIhAMckJ5kWJqoVClz%2F98mblXqSBZKuy6HV54NbLgYOkZU8KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwHg0Vi43HhvYZlYYsq3AOTGF6KIdQSJxmFa49be3TA95keR2ETLUlxIDzl5s%2B9ByTuDSNO5rA5YK%2BGl0I%2FTEi3T5EC7AHK1%2FpPSgIHQ9rDkTquAJ5mKbeL3cqC9aeLThLf9wfOUTc6q2nK99PDo85M9YLB%2BgYSNpKC24gVgTnOuBQeVWa00DRTaYT2e37ll77daVpUQZBXAI%2BBi%2FNEUoSD0I7cMj6Ebxi0gkuLZEEpurpEjan%2FYuoqy5dUr1FWpgQj75waXlcQk5vkDHHZo0Fr6ecDFMkL%2BGIQOF%2FuRVth%2Fp%2FaXU1KX5Rp97FAPCy6JInGHMg2%2F6x3%2FNci9Sm6rEwkKUGiZvUTGMOkPR9dcRPktqktEGF5b6DeWjHVKhxzYv%2FXptlScQ8O9aHFr7GHZbtZRVhf1gW1h%2BjLYqib59o7Z5G1PID318HYDNLBHfwHzMzT3g5iYB2D6rAO9dbhfpNLNad5jaTSEfwO3sfAU0g%2BckpfM187dcvx%2FXn%2Fq6qHNaes9KzaPxIyd6XYIrLKlanl6F2Mj77%2FMHm%2FEGd1m189l8nhqN64ioWo8BORRBczWyhAajRrkj4gMVvtmGlsw%2BdyyJ9FTOxYOVZlD23MO7GcEBdlinRIEWCge4eWneFbxesNqKpiTNJOGNvOODCGu%2Ba8BjqkAZKMqKrTYaD2AAIFVa8KfT9%2BqMbQYO5k8YW8TGGmP1cn4sOjyhkz8MyQIGkKGbYnz1n5fL7NbYUjY27RYWt9BJFGq7nNvwmnGkhTfm52NgTj3GEy6Y5YQZqVnPVGlWUHRh6vZmzaSLso4Who7DkazqegAxggT4%2FB737gaNsQHPZCW%2FLgiWlsJExHWTQPuEq4jlvl795Pfl3RTgmov%2B%2FmCZ7zLxXR&X-Amz-Signature=5022f1e11ae2349c5a0e153b4c931040c621fda0dbd922b4a236ba6408ae2cca&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643WRXICL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICz4SlwtJOTT%2Fib0%2FGQK9df%2ByngV4fDoMMJLmutX%2FprQAiEAhpCz3Dy%2FylYYNT8jHXSg1XVLwRoQBJINn6EeULitE2YqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDASug7LkhVvtOyr6lircA3hetcR7vtNI1Phe7CGJ7ms3mA%2FgjZ0Dl%2Beujrtx6nd7wJqdOR3dj0rPdG%2Fn1PHoFy2gaA5vA9CJYSW9CZMmtMmb2m6j4Vm3Bj0HKdrB6zATOsp2ara2atV%2FnqxT7PRiiTUbGt0vLDLBYo2DQqf0tTbvDYRVINoMyMvlGPghbin5MBmrM5ipH%2FZWGiy4UhDiry6ysHFZwpHq7V0W39zRVdvGFfG%2BD7odYCPJMCKqC46b5Ve2rQe5h54CQgIqSjUR9agYw%2BfbTI6HB951sExs9ZFmdIHzm5y%2BAfh2wZJGrQ6m1PkTRE%2B01Rqy0P3Xpi25TOYlNGHRHiFkUxFclLLd8kvZQKSrRrXRsbPJmBy75VTUx%2BK9lxrT5Xy1AZsr9xMhPmuFPYE1rHipLJftF2gCCMaFO15ibbgyCWtPK6v5qA3lZHjQ%2FheuB2HT5Q1H9%2B5sMz6PLNjvjvtI8Qzf6FCSMVAqeN8qHNC4u8P4ooBXLbJQKAdfRQyG7luBqjPDthgX2K05R4oXPCpuKtV3FfjiDY7HnRlEEW3jQ9e1%2Fdyooo5EUHq18bb8qLyxln5GSE6Yn8gnHTOc67Zggq9GkGAzefCEtIhNaZxneexHUYLpLiu4bYRBUEwWG8y%2FYy26MNO65rwGOqUBZ9MvMQbwGY36HKLuvqr1jxU8R3bITIVr9ULNGM85Ll5V7k3PMcSO4hn5GQsFMIoDWFJ6gLQEaXy7CZsKZrg5guMqgO5Wken%2BpsYWeSZvY1f5fecrSQMovKhoWRFWeHn8LReK%2BrnCCITxl%2F45XLRstmbjaOx4FhJZnh77RggvOdXwXJjjKeQhxOm8riUJ1pobraQf9EykEg5eXg%2F0eI9bnYlsLbXr&X-Amz-Signature=2633a93d9d0cbbfd5636d4e2279278a87d47fb60c5cb9623398f89d3e6217dc6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUQK7ARV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDEzHiiFOH1y4Wn2%2FX5r5zj4ymnNOL9aaFw0%2F274EwrmAIgDzpROrpVtRQ2QUzBfg4iLmCrFKT7uF0KFTF1rZ7IkQgqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG9c%2B%2BLra4CtQeN0OSrcA%2FhV41%2FNuvxLqALHI9Fk92FMPkjTS%2F%2FGvpVlnCx4uZ0ozGGMUeKsvalbHfRcWY%2BMOn2pM4spXSL6zmqI7KC7CIVxZxEA0p3VRKnYKcxsqYSC5KSq5Tg00uy%2Bwrrfvzg89wJ90Ukyph39S62LQgr3CNJoLML91FL2Fv%2FWWxfeSCg9ey1f9H%2B2zDwEyEHAiZ%2FUgygSSE2WysvwNafVrKgU%2F1%2FxNiv7bymglsvcdATjCte5ykRugLa1Tg1biK1Vjs4fQZq1cdXUiL%2BB7GFubNw%2FocdatVemMryu8TDHxDbqXM2WI7EzhPSKG8ipZN6abuOdoxXtCfKpbdRqxsUnHq%2BUZ4zErT2gezXvebBNPrgcK1NSkIQ%2BJ8R7Kcmoc5NP%2BrdbcvuEbFrbJ7jukwACMA510uz01sFIHlIc%2BSsz%2BDNc0bF48aRCdFrNfdy9WC6ghRtDE8aoYZruKODtRME2F5KrymKLqPQPXxvUkO0FwGSGFTH7ZwZuPFsJuFgwbCMVPPmjJwL4PY6lbc%2Fe7BUDxyMSICSTKaNCJQiWrZwnhk7vdvj7zSSCzQzZLqdXhNLAtG3Rfq1BjPs1x2MmpzhK9c5rakao5qe7UqFcNWfq0W7v1UDOlU6JQa48j1H0iKF0MP665rwGOqUBkPe6wwnql1yR0jRJAC%2Fe7oDBiVLtv9Eq1QGtPc8yDwU%2BZ%2Fh87O4wMlNFu1HAGhGmvAH9%2BbRSjLYM03wAl0ggOLQXuNvXVQLg7uOP9%2FY%2BYr8sILDkbvh15jzmYZ%2BPjVol6rQrDcPB99aqqD2S%2BuOmVV6SDf8ebyZCfHI%2FCAE4EDFVE4bIAi63xL3DO4ED4NleNiYYNnGkRdWUv2vY%2FAwMglIWYWod&X-Amz-Signature=229026773eb1ff629da4cee75df4fa6a1e2d19e86c7dd66743c4bda702508e5b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z6DKAGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIAfbs9r9748vLVLLGaFoqfKggkcR2EHlRoGPoX%2BqZHXgAiAOsEKloKGc0gy%2FUFrT%2FQVRtZDSX4GENFEqlcvRHL6TFyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMEArKyrxHJNKo8O8KtwDF9M5otZD7MGFWNBVwN03X45vVzptxC7SduB8khvWe91iKQ3IuW6lXgX9UJUbx%2BOnSdg3eQEmayly7Kx3lLQdNG27qJouyWeJZWQNe2wmyyYUX%2Fy1vtEQpDNMQsIHKenxsX0DqRFTzqkxuROVppTuw2vjrWD3Kz5uZ7Y6bUUns1UgumxOqgo1FZrC34T%2F1EZo%2BEDjaoLRI%2FLrOVIu3RenuLQwNcB3T66RWBPN1008eOHTQtFfgH56l5n61dPEPkEra7pJ75qKAqBlqZF6O0MU%2B260n3J2e%2F3Row6OpDC%2Fqx5GLIfUizFqk6A1vw1%2FniYO1bNk%2B6krotJQkpACSrUtZmGXUyinBR2oJkMj1eoq9DesOKgDxV3YBLThzwbBoh0ibWWE63hSCMdQuyw1rviXRh%2B3CUqc%2FJk6fo3ReoaLEQSaAigQ6JBNtHuWsxsdU5TK89U%2BSm5%2B8qGgEbWYjNRIBg%2Bo2IY2n8krCWlTVZFlsuInaYTJU%2Fl2r9UzVtLk30G202YCJDn%2B%2BKAqImozRtpZwbEBC26vZmlA1o%2Fn6wS0ovalwzNxd89oEBmyFLCcKddL2FggsA%2B3H1t0buHE0O2sweyv%2Fb60Q6623vqD%2BSkd4qpHqUOf6%2Fi9lL7zDwYwmrvmvAY6pgHf%2BxDKS7D5UyMvlcSxznPjDvI1Rlw1RjRC57FHSuJ3rsi6azCs9VM3U79B3oq5j0lIJeQX7ANO1jjaShsTevjIUvr8TBFL0QtOQUigPDtl6BbZRt12T%2BTWzwlk5tgB%2FeU2x39pmFMxJcXdP%2BCaKVXqmlevZiVEd%2FUzqsnjJhJpVOrI0JVjPb7v%2BqDds1Etb%2Bg%2FPDisc1OTAS%2Fy0%2FYR5NcPq6eSIFl3&X-Amz-Signature=645c2a76e9bc924abb332fd9d2126a1f3753dae7a76d7a6ddfb566e8aa60978d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z6DKAGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIAfbs9r9748vLVLLGaFoqfKggkcR2EHlRoGPoX%2BqZHXgAiAOsEKloKGc0gy%2FUFrT%2FQVRtZDSX4GENFEqlcvRHL6TFyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMEArKyrxHJNKo8O8KtwDF9M5otZD7MGFWNBVwN03X45vVzptxC7SduB8khvWe91iKQ3IuW6lXgX9UJUbx%2BOnSdg3eQEmayly7Kx3lLQdNG27qJouyWeJZWQNe2wmyyYUX%2Fy1vtEQpDNMQsIHKenxsX0DqRFTzqkxuROVppTuw2vjrWD3Kz5uZ7Y6bUUns1UgumxOqgo1FZrC34T%2F1EZo%2BEDjaoLRI%2FLrOVIu3RenuLQwNcB3T66RWBPN1008eOHTQtFfgH56l5n61dPEPkEra7pJ75qKAqBlqZF6O0MU%2B260n3J2e%2F3Row6OpDC%2Fqx5GLIfUizFqk6A1vw1%2FniYO1bNk%2B6krotJQkpACSrUtZmGXUyinBR2oJkMj1eoq9DesOKgDxV3YBLThzwbBoh0ibWWE63hSCMdQuyw1rviXRh%2B3CUqc%2FJk6fo3ReoaLEQSaAigQ6JBNtHuWsxsdU5TK89U%2BSm5%2B8qGgEbWYjNRIBg%2Bo2IY2n8krCWlTVZFlsuInaYTJU%2Fl2r9UzVtLk30G202YCJDn%2B%2BKAqImozRtpZwbEBC26vZmlA1o%2Fn6wS0ovalwzNxd89oEBmyFLCcKddL2FggsA%2B3H1t0buHE0O2sweyv%2Fb60Q6623vqD%2BSkd4qpHqUOf6%2Fi9lL7zDwYwmrvmvAY6pgHf%2BxDKS7D5UyMvlcSxznPjDvI1Rlw1RjRC57FHSuJ3rsi6azCs9VM3U79B3oq5j0lIJeQX7ANO1jjaShsTevjIUvr8TBFL0QtOQUigPDtl6BbZRt12T%2BTWzwlk5tgB%2FeU2x39pmFMxJcXdP%2BCaKVXqmlevZiVEd%2FUzqsnjJhJpVOrI0JVjPb7v%2BqDds1Etb%2Bg%2FPDisc1OTAS%2Fy0%2FYR5NcPq6eSIFl3&X-Amz-Signature=db781dbfbf176330ce832a78a3c727042592b164eab779bf0dbd925f4a902bab&X-Amz-SignedHeaders=host&x-id=GetObject)

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
