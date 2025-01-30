

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466565U7XPD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1P9FxmL32xFQwFCuhEoXXw%2FttFFFjej05%2BWSMWiqBLwIgcbzrCPH%2FzLCKKfA%2FAYSu106wZ3SzhbTk4o3pnEv4CVoqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJoH2Vh21I%2FcZM518SrcA7QfUtDDhd59JejrGUkwPaCQuSifNiYuxODYc4bKImDLJjIP8sTpeaO954yjQH3LndlSUVEqpamslJ6oGeZIIoU1EnRcF3bvGlg3rSttLFWIpQIXPL0UgTG%2Bl91OpkbVCKlICWKIL9cR9WkvRzl1WwZymVtL6%2BlcDTqev%2FIfsZlk%2BHYVm%2F2n4OuDNjeOPxzq9eDXDKCDfLLUSBPqy4waP%2F1ESG3yMPStGXUi2eAQk53vkpcK%2FLYetIoAlUdVBJFj%2B9o1D6lhglNG7OVN4SLkzpt1mPt4QwNRtMPHhOXBTV1MENoyD9YgPQhFVZ%2FAic1Thm8dvbOicQUbM%2BMxr4g0iZQWlZI6adjlKuUrQaC5k2yncGnHNuzAGUvv6aXpVdGqiz6CenlQdIm3VrsNK8lzADQyA%2F7mIcQJsxVdpWPayNt%2FQUcMQhLmcgIMVD%2B6BW1QDZ9GxE1AUCtGDQgNmh7XQjAegEqnaLpuWuIDqdaRL0KHUQZg9NBON2p%2B5Xf9CQ09s5U1U8Q539ixu511OiON8%2Byn3ZtCnQkIBuLPX2jz1HALaIEpAZbj5%2F4OiFNEb92468zG1O9aUPRBCqidd%2FM5qNHEBD5Zngq9CBSyA%2FijpkkwlKOumQswkw7ZleYBMJGq77wGOqUBVh%2FGK4G%2BXaZa8hcj1Bgc3ZSscM%2FWj71%2F0CDV80A%2BzLsgBAt7N57wgSpZx697gTEpPR%2BhqeQyqmxvoYFM8uK9NFfllQJ5jYSKqLFqgm69WUKOeDGsExKBBjirBUD%2FzvjywqAU09tEhUC118VjeImJos0UZ8awf92wlUXdIymYV5FoAV3NSz4h5XU3sSweiQuXXoAH7D9t9bc9seUpy3MihvIXnUub&X-Amz-Signature=6e43e1bb113c891144393517bf198f930cf5536626e889285f65aacb0233f1e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466565U7XPD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1P9FxmL32xFQwFCuhEoXXw%2FttFFFjej05%2BWSMWiqBLwIgcbzrCPH%2FzLCKKfA%2FAYSu106wZ3SzhbTk4o3pnEv4CVoqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJoH2Vh21I%2FcZM518SrcA7QfUtDDhd59JejrGUkwPaCQuSifNiYuxODYc4bKImDLJjIP8sTpeaO954yjQH3LndlSUVEqpamslJ6oGeZIIoU1EnRcF3bvGlg3rSttLFWIpQIXPL0UgTG%2Bl91OpkbVCKlICWKIL9cR9WkvRzl1WwZymVtL6%2BlcDTqev%2FIfsZlk%2BHYVm%2F2n4OuDNjeOPxzq9eDXDKCDfLLUSBPqy4waP%2F1ESG3yMPStGXUi2eAQk53vkpcK%2FLYetIoAlUdVBJFj%2B9o1D6lhglNG7OVN4SLkzpt1mPt4QwNRtMPHhOXBTV1MENoyD9YgPQhFVZ%2FAic1Thm8dvbOicQUbM%2BMxr4g0iZQWlZI6adjlKuUrQaC5k2yncGnHNuzAGUvv6aXpVdGqiz6CenlQdIm3VrsNK8lzADQyA%2F7mIcQJsxVdpWPayNt%2FQUcMQhLmcgIMVD%2B6BW1QDZ9GxE1AUCtGDQgNmh7XQjAegEqnaLpuWuIDqdaRL0KHUQZg9NBON2p%2B5Xf9CQ09s5U1U8Q539ixu511OiON8%2Byn3ZtCnQkIBuLPX2jz1HALaIEpAZbj5%2F4OiFNEb92468zG1O9aUPRBCqidd%2FM5qNHEBD5Zngq9CBSyA%2FijpkkwlKOumQswkw7ZleYBMJGq77wGOqUBVh%2FGK4G%2BXaZa8hcj1Bgc3ZSscM%2FWj71%2F0CDV80A%2BzLsgBAt7N57wgSpZx697gTEpPR%2BhqeQyqmxvoYFM8uK9NFfllQJ5jYSKqLFqgm69WUKOeDGsExKBBjirBUD%2FzvjywqAU09tEhUC118VjeImJos0UZ8awf92wlUXdIymYV5FoAV3NSz4h5XU3sSweiQuXXoAH7D9t9bc9seUpy3MihvIXnUub&X-Amz-Signature=0993b180f7f521addc8f6c3c28406a06e41498b766c201972c3db97b44713033&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466565U7XPD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1P9FxmL32xFQwFCuhEoXXw%2FttFFFjej05%2BWSMWiqBLwIgcbzrCPH%2FzLCKKfA%2FAYSu106wZ3SzhbTk4o3pnEv4CVoqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJoH2Vh21I%2FcZM518SrcA7QfUtDDhd59JejrGUkwPaCQuSifNiYuxODYc4bKImDLJjIP8sTpeaO954yjQH3LndlSUVEqpamslJ6oGeZIIoU1EnRcF3bvGlg3rSttLFWIpQIXPL0UgTG%2Bl91OpkbVCKlICWKIL9cR9WkvRzl1WwZymVtL6%2BlcDTqev%2FIfsZlk%2BHYVm%2F2n4OuDNjeOPxzq9eDXDKCDfLLUSBPqy4waP%2F1ESG3yMPStGXUi2eAQk53vkpcK%2FLYetIoAlUdVBJFj%2B9o1D6lhglNG7OVN4SLkzpt1mPt4QwNRtMPHhOXBTV1MENoyD9YgPQhFVZ%2FAic1Thm8dvbOicQUbM%2BMxr4g0iZQWlZI6adjlKuUrQaC5k2yncGnHNuzAGUvv6aXpVdGqiz6CenlQdIm3VrsNK8lzADQyA%2F7mIcQJsxVdpWPayNt%2FQUcMQhLmcgIMVD%2B6BW1QDZ9GxE1AUCtGDQgNmh7XQjAegEqnaLpuWuIDqdaRL0KHUQZg9NBON2p%2B5Xf9CQ09s5U1U8Q539ixu511OiON8%2Byn3ZtCnQkIBuLPX2jz1HALaIEpAZbj5%2F4OiFNEb92468zG1O9aUPRBCqidd%2FM5qNHEBD5Zngq9CBSyA%2FijpkkwlKOumQswkw7ZleYBMJGq77wGOqUBVh%2FGK4G%2BXaZa8hcj1Bgc3ZSscM%2FWj71%2F0CDV80A%2BzLsgBAt7N57wgSpZx697gTEpPR%2BhqeQyqmxvoYFM8uK9NFfllQJ5jYSKqLFqgm69WUKOeDGsExKBBjirBUD%2FzvjywqAU09tEhUC118VjeImJos0UZ8awf92wlUXdIymYV5FoAV3NSz4h5XU3sSweiQuXXoAH7D9t9bc9seUpy3MihvIXnUub&X-Amz-Signature=4fd9d71152e3136a11cc3002faac00977d538e03108196e16dee84f6a937b138&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4UV54JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEnZ1FQuCHXggjJ6Y376EK9%2FojOxISOubcP3hKt55PYQIgfG%2B2YhEMKgTSZxQJJFtI%2BbfKAF51%2FgvMXZDkcsQ7KIcqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz2xAN6MM82OtCD2yrcA2t5d13YZ9DzRGfA0Tmd9SXy1HFs5RxrPL9cxBtB9evRjng%2FBR2ljGNyX3XYeZZ1Wk7%2Be353MY9dzksb%2BkBzeAg1qzEOJ%2BA149Gl1HpOFdPRO3Nz17fI8YWxa7CEIO5XAOQgBFdKHqA9qntnsj%2B1N1bU2AjeZ93Pg%2BKpqx%2FWSyxSP1IUCyNLpoX4XD9aa87iPDjryLyxWxShz9JREBLnygcgr9aYSCcbNzOp5i2mYN%2Bvm0fEfUKD5hDBVCj%2BrExDVTfAaGDKyiNnT3nGsBymt77clm%2BUu8aZwYNq%2BeW9JWke3b4z%2BYEn1EiWqYe5qnbFXWfnh9JeRm9RebZ%2FmYTU1cZKPWQ5XPhEFEfswLbh0g%2F5vHOx5vxuGeuMqUwVwjD1%2BaIYOrVwovd1Wwo%2FQyOkGVtJklsweG%2BVfxFppu8XPIWd9NpJUK89aiJ85y4OOzYwTs1sN3cDex3WnstetTMZQ%2FlUckSnn0iVwX3bzO1RYAK8OLyTI2T0hYw959xn8O9zLcGL2%2BJFZx%2BgA%2FtHDB4JRoREqHSQMs3GiQmoTOsaTphV18XLm%2BiBLTw0ew%2FZbiKaiSEYaZaD8GkLAVRNuMXpysV1fEQNSG5iAgekvAI9lchWNL1CcN%2BoBkB3R64xMO2p77wGOqUBbmV76OtXklJ2OM99WLccG8pJ6msBAH%2BsVlZd1DT2EIbWCotiZouN5O5%2F3h4xvT7LlsqLOM96NSvwoSnVEGw9Y%2FqDTj3bJwZGIrvefJcEPYLG%2FW93pIVu%2FcpTZ6a1oJwoHRYCIqUN0nzgmzXHo34qb3jrT9j%2FGq44ZCY%2FPeBXx9Ao5yNstiYPGSrgBdkG0rVzdyR6jca%2BONfOnDIp3IqKdbQDsPI8&X-Amz-Signature=926ea08a13e5c2e812a371b4212294e91177354a7d2e9c2659270cc2556c1a91&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4UV54JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEnZ1FQuCHXggjJ6Y376EK9%2FojOxISOubcP3hKt55PYQIgfG%2B2YhEMKgTSZxQJJFtI%2BbfKAF51%2FgvMXZDkcsQ7KIcqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz2xAN6MM82OtCD2yrcA2t5d13YZ9DzRGfA0Tmd9SXy1HFs5RxrPL9cxBtB9evRjng%2FBR2ljGNyX3XYeZZ1Wk7%2Be353MY9dzksb%2BkBzeAg1qzEOJ%2BA149Gl1HpOFdPRO3Nz17fI8YWxa7CEIO5XAOQgBFdKHqA9qntnsj%2B1N1bU2AjeZ93Pg%2BKpqx%2FWSyxSP1IUCyNLpoX4XD9aa87iPDjryLyxWxShz9JREBLnygcgr9aYSCcbNzOp5i2mYN%2Bvm0fEfUKD5hDBVCj%2BrExDVTfAaGDKyiNnT3nGsBymt77clm%2BUu8aZwYNq%2BeW9JWke3b4z%2BYEn1EiWqYe5qnbFXWfnh9JeRm9RebZ%2FmYTU1cZKPWQ5XPhEFEfswLbh0g%2F5vHOx5vxuGeuMqUwVwjD1%2BaIYOrVwovd1Wwo%2FQyOkGVtJklsweG%2BVfxFppu8XPIWd9NpJUK89aiJ85y4OOzYwTs1sN3cDex3WnstetTMZQ%2FlUckSnn0iVwX3bzO1RYAK8OLyTI2T0hYw959xn8O9zLcGL2%2BJFZx%2BgA%2FtHDB4JRoREqHSQMs3GiQmoTOsaTphV18XLm%2BiBLTw0ew%2FZbiKaiSEYaZaD8GkLAVRNuMXpysV1fEQNSG5iAgekvAI9lchWNL1CcN%2BoBkB3R64xMO2p77wGOqUBbmV76OtXklJ2OM99WLccG8pJ6msBAH%2BsVlZd1DT2EIbWCotiZouN5O5%2F3h4xvT7LlsqLOM96NSvwoSnVEGw9Y%2FqDTj3bJwZGIrvefJcEPYLG%2FW93pIVu%2FcpTZ6a1oJwoHRYCIqUN0nzgmzXHo34qb3jrT9j%2FGq44ZCY%2FPeBXx9Ao5yNstiYPGSrgBdkG0rVzdyR6jca%2BONfOnDIp3IqKdbQDsPI8&X-Amz-Signature=9c3bf2b7192d9614d35fa3255573f1fa7d98262c5b6bfd787fdbd39e6f620fc2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4UV54JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEnZ1FQuCHXggjJ6Y376EK9%2FojOxISOubcP3hKt55PYQIgfG%2B2YhEMKgTSZxQJJFtI%2BbfKAF51%2FgvMXZDkcsQ7KIcqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz2xAN6MM82OtCD2yrcA2t5d13YZ9DzRGfA0Tmd9SXy1HFs5RxrPL9cxBtB9evRjng%2FBR2ljGNyX3XYeZZ1Wk7%2Be353MY9dzksb%2BkBzeAg1qzEOJ%2BA149Gl1HpOFdPRO3Nz17fI8YWxa7CEIO5XAOQgBFdKHqA9qntnsj%2B1N1bU2AjeZ93Pg%2BKpqx%2FWSyxSP1IUCyNLpoX4XD9aa87iPDjryLyxWxShz9JREBLnygcgr9aYSCcbNzOp5i2mYN%2Bvm0fEfUKD5hDBVCj%2BrExDVTfAaGDKyiNnT3nGsBymt77clm%2BUu8aZwYNq%2BeW9JWke3b4z%2BYEn1EiWqYe5qnbFXWfnh9JeRm9RebZ%2FmYTU1cZKPWQ5XPhEFEfswLbh0g%2F5vHOx5vxuGeuMqUwVwjD1%2BaIYOrVwovd1Wwo%2FQyOkGVtJklsweG%2BVfxFppu8XPIWd9NpJUK89aiJ85y4OOzYwTs1sN3cDex3WnstetTMZQ%2FlUckSnn0iVwX3bzO1RYAK8OLyTI2T0hYw959xn8O9zLcGL2%2BJFZx%2BgA%2FtHDB4JRoREqHSQMs3GiQmoTOsaTphV18XLm%2BiBLTw0ew%2FZbiKaiSEYaZaD8GkLAVRNuMXpysV1fEQNSG5iAgekvAI9lchWNL1CcN%2BoBkB3R64xMO2p77wGOqUBbmV76OtXklJ2OM99WLccG8pJ6msBAH%2BsVlZd1DT2EIbWCotiZouN5O5%2F3h4xvT7LlsqLOM96NSvwoSnVEGw9Y%2FqDTj3bJwZGIrvefJcEPYLG%2FW93pIVu%2FcpTZ6a1oJwoHRYCIqUN0nzgmzXHo34qb3jrT9j%2FGq44ZCY%2FPeBXx9Ao5yNstiYPGSrgBdkG0rVzdyR6jca%2BONfOnDIp3IqKdbQDsPI8&X-Amz-Signature=3808df09c67332d48b6acf5203553883506a226e6e59a48784211643495adff3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4UV54JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEnZ1FQuCHXggjJ6Y376EK9%2FojOxISOubcP3hKt55PYQIgfG%2B2YhEMKgTSZxQJJFtI%2BbfKAF51%2FgvMXZDkcsQ7KIcqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz2xAN6MM82OtCD2yrcA2t5d13YZ9DzRGfA0Tmd9SXy1HFs5RxrPL9cxBtB9evRjng%2FBR2ljGNyX3XYeZZ1Wk7%2Be353MY9dzksb%2BkBzeAg1qzEOJ%2BA149Gl1HpOFdPRO3Nz17fI8YWxa7CEIO5XAOQgBFdKHqA9qntnsj%2B1N1bU2AjeZ93Pg%2BKpqx%2FWSyxSP1IUCyNLpoX4XD9aa87iPDjryLyxWxShz9JREBLnygcgr9aYSCcbNzOp5i2mYN%2Bvm0fEfUKD5hDBVCj%2BrExDVTfAaGDKyiNnT3nGsBymt77clm%2BUu8aZwYNq%2BeW9JWke3b4z%2BYEn1EiWqYe5qnbFXWfnh9JeRm9RebZ%2FmYTU1cZKPWQ5XPhEFEfswLbh0g%2F5vHOx5vxuGeuMqUwVwjD1%2BaIYOrVwovd1Wwo%2FQyOkGVtJklsweG%2BVfxFppu8XPIWd9NpJUK89aiJ85y4OOzYwTs1sN3cDex3WnstetTMZQ%2FlUckSnn0iVwX3bzO1RYAK8OLyTI2T0hYw959xn8O9zLcGL2%2BJFZx%2BgA%2FtHDB4JRoREqHSQMs3GiQmoTOsaTphV18XLm%2BiBLTw0ew%2FZbiKaiSEYaZaD8GkLAVRNuMXpysV1fEQNSG5iAgekvAI9lchWNL1CcN%2BoBkB3R64xMO2p77wGOqUBbmV76OtXklJ2OM99WLccG8pJ6msBAH%2BsVlZd1DT2EIbWCotiZouN5O5%2F3h4xvT7LlsqLOM96NSvwoSnVEGw9Y%2FqDTj3bJwZGIrvefJcEPYLG%2FW93pIVu%2FcpTZ6a1oJwoHRYCIqUN0nzgmzXHo34qb3jrT9j%2FGq44ZCY%2FPeBXx9Ao5yNstiYPGSrgBdkG0rVzdyR6jca%2BONfOnDIp3IqKdbQDsPI8&X-Amz-Signature=b5deb22e0fa902b8769639a8dcbc2f0b4627fbd16c4a0618bc86c1bbeb823963&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4UV54JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEnZ1FQuCHXggjJ6Y376EK9%2FojOxISOubcP3hKt55PYQIgfG%2B2YhEMKgTSZxQJJFtI%2BbfKAF51%2FgvMXZDkcsQ7KIcqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz2xAN6MM82OtCD2yrcA2t5d13YZ9DzRGfA0Tmd9SXy1HFs5RxrPL9cxBtB9evRjng%2FBR2ljGNyX3XYeZZ1Wk7%2Be353MY9dzksb%2BkBzeAg1qzEOJ%2BA149Gl1HpOFdPRO3Nz17fI8YWxa7CEIO5XAOQgBFdKHqA9qntnsj%2B1N1bU2AjeZ93Pg%2BKpqx%2FWSyxSP1IUCyNLpoX4XD9aa87iPDjryLyxWxShz9JREBLnygcgr9aYSCcbNzOp5i2mYN%2Bvm0fEfUKD5hDBVCj%2BrExDVTfAaGDKyiNnT3nGsBymt77clm%2BUu8aZwYNq%2BeW9JWke3b4z%2BYEn1EiWqYe5qnbFXWfnh9JeRm9RebZ%2FmYTU1cZKPWQ5XPhEFEfswLbh0g%2F5vHOx5vxuGeuMqUwVwjD1%2BaIYOrVwovd1Wwo%2FQyOkGVtJklsweG%2BVfxFppu8XPIWd9NpJUK89aiJ85y4OOzYwTs1sN3cDex3WnstetTMZQ%2FlUckSnn0iVwX3bzO1RYAK8OLyTI2T0hYw959xn8O9zLcGL2%2BJFZx%2BgA%2FtHDB4JRoREqHSQMs3GiQmoTOsaTphV18XLm%2BiBLTw0ew%2FZbiKaiSEYaZaD8GkLAVRNuMXpysV1fEQNSG5iAgekvAI9lchWNL1CcN%2BoBkB3R64xMO2p77wGOqUBbmV76OtXklJ2OM99WLccG8pJ6msBAH%2BsVlZd1DT2EIbWCotiZouN5O5%2F3h4xvT7LlsqLOM96NSvwoSnVEGw9Y%2FqDTj3bJwZGIrvefJcEPYLG%2FW93pIVu%2FcpTZ6a1oJwoHRYCIqUN0nzgmzXHo34qb3jrT9j%2FGq44ZCY%2FPeBXx9Ao5yNstiYPGSrgBdkG0rVzdyR6jca%2BONfOnDIp3IqKdbQDsPI8&X-Amz-Signature=a85b7d20f3e023437d4e988eab19acc5df44ddd70837cc970c56c6fb1d5b4585&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4UV54JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEnZ1FQuCHXggjJ6Y376EK9%2FojOxISOubcP3hKt55PYQIgfG%2B2YhEMKgTSZxQJJFtI%2BbfKAF51%2FgvMXZDkcsQ7KIcqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz2xAN6MM82OtCD2yrcA2t5d13YZ9DzRGfA0Tmd9SXy1HFs5RxrPL9cxBtB9evRjng%2FBR2ljGNyX3XYeZZ1Wk7%2Be353MY9dzksb%2BkBzeAg1qzEOJ%2BA149Gl1HpOFdPRO3Nz17fI8YWxa7CEIO5XAOQgBFdKHqA9qntnsj%2B1N1bU2AjeZ93Pg%2BKpqx%2FWSyxSP1IUCyNLpoX4XD9aa87iPDjryLyxWxShz9JREBLnygcgr9aYSCcbNzOp5i2mYN%2Bvm0fEfUKD5hDBVCj%2BrExDVTfAaGDKyiNnT3nGsBymt77clm%2BUu8aZwYNq%2BeW9JWke3b4z%2BYEn1EiWqYe5qnbFXWfnh9JeRm9RebZ%2FmYTU1cZKPWQ5XPhEFEfswLbh0g%2F5vHOx5vxuGeuMqUwVwjD1%2BaIYOrVwovd1Wwo%2FQyOkGVtJklsweG%2BVfxFppu8XPIWd9NpJUK89aiJ85y4OOzYwTs1sN3cDex3WnstetTMZQ%2FlUckSnn0iVwX3bzO1RYAK8OLyTI2T0hYw959xn8O9zLcGL2%2BJFZx%2BgA%2FtHDB4JRoREqHSQMs3GiQmoTOsaTphV18XLm%2BiBLTw0ew%2FZbiKaiSEYaZaD8GkLAVRNuMXpysV1fEQNSG5iAgekvAI9lchWNL1CcN%2BoBkB3R64xMO2p77wGOqUBbmV76OtXklJ2OM99WLccG8pJ6msBAH%2BsVlZd1DT2EIbWCotiZouN5O5%2F3h4xvT7LlsqLOM96NSvwoSnVEGw9Y%2FqDTj3bJwZGIrvefJcEPYLG%2FW93pIVu%2FcpTZ6a1oJwoHRYCIqUN0nzgmzXHo34qb3jrT9j%2FGq44ZCY%2FPeBXx9Ao5yNstiYPGSrgBdkG0rVzdyR6jca%2BONfOnDIp3IqKdbQDsPI8&X-Amz-Signature=d092d618e6af0bf691e3c01629647d445fcacad9e9e79d44628fd3b19b0faa0b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCXJNTOU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBBsBrKIqqgjc3qJtMzpfJD%2BcQHeN99pOXja2yF1NeNzAiBLT7HhjVRdasVx995tjzVcX9L9jgUFADZTF3ZbQHMqkyqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmXaNJDC21wKGRCGyKtwD46kvZWREDUWqZTzHGiRuf5LZURmJGM%2BF51N4jZq%2BvYeh6JHEh6OM3RLH7LkDdSOsUvGXKGbo1ncYCn2Bu%2BbBaDFrV8F383gzv4Oi07MtD7QfNC4XL1gRYlFazQTAdKZE2BUeK9PaPPphhXqrpVAUgKKvZ%2BYFva6NgSU97I8PZt%2BHEN0sWE4cOf%2FGbZb0%2FTfrAiJ0GUj1avhxQS%2BcJwuOgnMADxrtU4sgEXO4eL29fbiRKlLN7jMbxUE4Q7aBFmr7tE2oGzeHtB9GKX42e%2BjyMZ0hDqQwhojyNb4Hyih%2FyvQS%2Fp6%2F9tYLq%2BrRGUkyT9nP5TNZXc6lDAA1oUm0yyoSNQ9Gn7XmxLYuwTBHnEmbf8FEkPKkeJze4RLb%2FJ5DKwwBPhm%2FP0fEqopKdh424%2FO5Tqe%2FH%2FTqfpsdeg%2F6aWyr7aEs2BWeq8rqb4Smz9R3t3WA0O86cWDhIEoiQrwCnWjRULYxNCidivS0mD962QOZDumfkD3BLTPr9gLadNfmBRja0TPC75KfMBp8KfvkMtVHlYsr5wG0aRloCt3%2FCIpKg23dfS1PNLh9Dddv5wc%2FPKaq0zJcgZDBDQbvKRMkgDiBV3CNM68vVuJZomcq5TTZmqBZ3lb5MMtEyFUGc7ow2qnvvAY6pgGYiMGGcN0fg%2FHCXN0J6G8dkmuDB91EEd%2F0p7NfEXGv2kBMBiEdp00CZ%2BoSnSjutLWHgMM5GVV5Ycrli%2FCzwjLPs2sfAHgzdgLecPZyAfVrafJwiCiPZDP5uuaY7Zm2H35OK%2B%2FaM9WPOsommvsa9sHKirBBMhqG8Bt8HddUk8SzoAlaX8dUDjuqsWspr8Hl5naYLqkzSw9vgZqtWyi5e1O9LOGXm4zI&X-Amz-Signature=8f1f20d52c513b54497dca13d104bd385c79dd1f46f0417b126c9e56933e81b9&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7OAET3U%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD46h0%2BjmfNS5uJQvwif0O5zow%2Fh%2Fro9fY3xF7Cdkb%2FQQIhAP1LUrGycKYx9r6pIL1eyH9XMe%2FGfUVCo1CoBjBhScBOKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0CcP0cDjabKpbpUIq3AM2pwg8WFD4WWW1mwGmnHNBEFjN87BFHaUV63FkE9V%2FSjQrJRWoS7FHJ8Ln5bKdQ9d4HJO21G%2Farhx5ZlBMtctFGxkr%2FtOhoqKls8x6NIOcMWBeis2dsk4d2blkYhYeaRFPRMzYeJfuMk2IKgT248lu5UcBdrM2d2PhzdmPcZm8wGsVfSABHEJdm6GdMpXwqOzxc%2BiMOmcfoQe5wWXt6zdOz3uRKgl5WnrAu864PuujRHepfp7vzJs9iSp9p3z4At1KPxKr7HbaSsoyCyxrF%2FW1G3A9gHEVMAseonAqx7PLk7A2sATOucvSFSUnJJyGieOBZzPW6FYZ6j%2B0cT%2F6R2fxqBfyXHRChEMhR09yhbHtaEdEG3lb%2BQE%2BuLoo4Md4odJndTc1Y9fJzrYzytMP2%2F496%2BvH54pZvMocg4zQ1GqKhSVRrKWIObi0qmFeDGiluBlRY6lXSmQhKVY1Zfrn44xCs9JR49EiS3CzNTrWPmHMSI58Gm126IvU2nmZqggcoSDxxTv6GaDPfN4jyNAS4fjmeQVbAUq3fhncCB0OjYgg8y9k4N50qV77u3LiDf0atbNqN%2BEoFO5NpgZ2VepnN%2F0TmoUbHwBsSTlUH2zuOCzpahh8LaLZPPWYLZ8VJDCbqu%2B8BjqkAR8JkHy65UlphvFIkNIN%2BN4Cz3q3hpPCUcWioarxLLdwMp0CVnSir7kMANfHm7MZ4u8ll821MwIPjhx%2FxR548CAdr2ZgIbHFZVP6uFcXgnOnyKlmdxp2%2B0Cprpp2TEYGaNZCIxNViuxgFKQTIeyAJAcnUIfzqKim50vRw9JViZQJasiOuqbzVvLEodH5wRk7dC4lF3F3MCgsfRwso75btdTM%2BtOI&X-Amz-Signature=04c09c9efc11229e0ace489e12669725b3383c966013f3b967829d8c65d7e500&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4UV54JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEnZ1FQuCHXggjJ6Y376EK9%2FojOxISOubcP3hKt55PYQIgfG%2B2YhEMKgTSZxQJJFtI%2BbfKAF51%2FgvMXZDkcsQ7KIcqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz2xAN6MM82OtCD2yrcA2t5d13YZ9DzRGfA0Tmd9SXy1HFs5RxrPL9cxBtB9evRjng%2FBR2ljGNyX3XYeZZ1Wk7%2Be353MY9dzksb%2BkBzeAg1qzEOJ%2BA149Gl1HpOFdPRO3Nz17fI8YWxa7CEIO5XAOQgBFdKHqA9qntnsj%2B1N1bU2AjeZ93Pg%2BKpqx%2FWSyxSP1IUCyNLpoX4XD9aa87iPDjryLyxWxShz9JREBLnygcgr9aYSCcbNzOp5i2mYN%2Bvm0fEfUKD5hDBVCj%2BrExDVTfAaGDKyiNnT3nGsBymt77clm%2BUu8aZwYNq%2BeW9JWke3b4z%2BYEn1EiWqYe5qnbFXWfnh9JeRm9RebZ%2FmYTU1cZKPWQ5XPhEFEfswLbh0g%2F5vHOx5vxuGeuMqUwVwjD1%2BaIYOrVwovd1Wwo%2FQyOkGVtJklsweG%2BVfxFppu8XPIWd9NpJUK89aiJ85y4OOzYwTs1sN3cDex3WnstetTMZQ%2FlUckSnn0iVwX3bzO1RYAK8OLyTI2T0hYw959xn8O9zLcGL2%2BJFZx%2BgA%2FtHDB4JRoREqHSQMs3GiQmoTOsaTphV18XLm%2BiBLTw0ew%2FZbiKaiSEYaZaD8GkLAVRNuMXpysV1fEQNSG5iAgekvAI9lchWNL1CcN%2BoBkB3R64xMO2p77wGOqUBbmV76OtXklJ2OM99WLccG8pJ6msBAH%2BsVlZd1DT2EIbWCotiZouN5O5%2F3h4xvT7LlsqLOM96NSvwoSnVEGw9Y%2FqDTj3bJwZGIrvefJcEPYLG%2FW93pIVu%2FcpTZ6a1oJwoHRYCIqUN0nzgmzXHo34qb3jrT9j%2FGq44ZCY%2FPeBXx9Ao5yNstiYPGSrgBdkG0rVzdyR6jca%2BONfOnDIp3IqKdbQDsPI8&X-Amz-Signature=66070ea025047840f67ab30709a83bf3f29d3d7c5ed9c6c4d23a0b4e69393afe&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4UV54JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEnZ1FQuCHXggjJ6Y376EK9%2FojOxISOubcP3hKt55PYQIgfG%2B2YhEMKgTSZxQJJFtI%2BbfKAF51%2FgvMXZDkcsQ7KIcqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz2xAN6MM82OtCD2yrcA2t5d13YZ9DzRGfA0Tmd9SXy1HFs5RxrPL9cxBtB9evRjng%2FBR2ljGNyX3XYeZZ1Wk7%2Be353MY9dzksb%2BkBzeAg1qzEOJ%2BA149Gl1HpOFdPRO3Nz17fI8YWxa7CEIO5XAOQgBFdKHqA9qntnsj%2B1N1bU2AjeZ93Pg%2BKpqx%2FWSyxSP1IUCyNLpoX4XD9aa87iPDjryLyxWxShz9JREBLnygcgr9aYSCcbNzOp5i2mYN%2Bvm0fEfUKD5hDBVCj%2BrExDVTfAaGDKyiNnT3nGsBymt77clm%2BUu8aZwYNq%2BeW9JWke3b4z%2BYEn1EiWqYe5qnbFXWfnh9JeRm9RebZ%2FmYTU1cZKPWQ5XPhEFEfswLbh0g%2F5vHOx5vxuGeuMqUwVwjD1%2BaIYOrVwovd1Wwo%2FQyOkGVtJklsweG%2BVfxFppu8XPIWd9NpJUK89aiJ85y4OOzYwTs1sN3cDex3WnstetTMZQ%2FlUckSnn0iVwX3bzO1RYAK8OLyTI2T0hYw959xn8O9zLcGL2%2BJFZx%2BgA%2FtHDB4JRoREqHSQMs3GiQmoTOsaTphV18XLm%2BiBLTw0ew%2FZbiKaiSEYaZaD8GkLAVRNuMXpysV1fEQNSG5iAgekvAI9lchWNL1CcN%2BoBkB3R64xMO2p77wGOqUBbmV76OtXklJ2OM99WLccG8pJ6msBAH%2BsVlZd1DT2EIbWCotiZouN5O5%2F3h4xvT7LlsqLOM96NSvwoSnVEGw9Y%2FqDTj3bJwZGIrvefJcEPYLG%2FW93pIVu%2FcpTZ6a1oJwoHRYCIqUN0nzgmzXHo34qb3jrT9j%2FGq44ZCY%2FPeBXx9Ao5yNstiYPGSrgBdkG0rVzdyR6jca%2BONfOnDIp3IqKdbQDsPI8&X-Amz-Signature=c26ec78ff94695c7eb967147756886761bce2f3bec6f600102e504070e655e1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4UV54JW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEnZ1FQuCHXggjJ6Y376EK9%2FojOxISOubcP3hKt55PYQIgfG%2B2YhEMKgTSZxQJJFtI%2BbfKAF51%2FgvMXZDkcsQ7KIcqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz2xAN6MM82OtCD2yrcA2t5d13YZ9DzRGfA0Tmd9SXy1HFs5RxrPL9cxBtB9evRjng%2FBR2ljGNyX3XYeZZ1Wk7%2Be353MY9dzksb%2BkBzeAg1qzEOJ%2BA149Gl1HpOFdPRO3Nz17fI8YWxa7CEIO5XAOQgBFdKHqA9qntnsj%2B1N1bU2AjeZ93Pg%2BKpqx%2FWSyxSP1IUCyNLpoX4XD9aa87iPDjryLyxWxShz9JREBLnygcgr9aYSCcbNzOp5i2mYN%2Bvm0fEfUKD5hDBVCj%2BrExDVTfAaGDKyiNnT3nGsBymt77clm%2BUu8aZwYNq%2BeW9JWke3b4z%2BYEn1EiWqYe5qnbFXWfnh9JeRm9RebZ%2FmYTU1cZKPWQ5XPhEFEfswLbh0g%2F5vHOx5vxuGeuMqUwVwjD1%2BaIYOrVwovd1Wwo%2FQyOkGVtJklsweG%2BVfxFppu8XPIWd9NpJUK89aiJ85y4OOzYwTs1sN3cDex3WnstetTMZQ%2FlUckSnn0iVwX3bzO1RYAK8OLyTI2T0hYw959xn8O9zLcGL2%2BJFZx%2BgA%2FtHDB4JRoREqHSQMs3GiQmoTOsaTphV18XLm%2BiBLTw0ew%2FZbiKaiSEYaZaD8GkLAVRNuMXpysV1fEQNSG5iAgekvAI9lchWNL1CcN%2BoBkB3R64xMO2p77wGOqUBbmV76OtXklJ2OM99WLccG8pJ6msBAH%2BsVlZd1DT2EIbWCotiZouN5O5%2F3h4xvT7LlsqLOM96NSvwoSnVEGw9Y%2FqDTj3bJwZGIrvefJcEPYLG%2FW93pIVu%2FcpTZ6a1oJwoHRYCIqUN0nzgmzXHo34qb3jrT9j%2FGq44ZCY%2FPeBXx9Ao5yNstiYPGSrgBdkG0rVzdyR6jca%2BONfOnDIp3IqKdbQDsPI8&X-Amz-Signature=a4563bc1f0cb44c7821505583c30461db4f0193eea7f2fdec569a48e38d26661&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCOBMHJT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjJRfBTHY64kUV%2BLJDR0o5mzITzI9msgxJtl8amllZIQIgD8z8hvVVRJXiIWfqNhjqwD3boJ2%2BY%2B1peZ1%2FFX98hnYqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIfYonmkEdRMmXFqkCrcA%2FEruoqiBdFsJBP6wvSJb9dTLlCwMlayGb6hVvRV5JXy2lYJMK59L4DNfklcHv%2Fl3TguuXW%2BVEHrGA16tZ15INZdUdos6NfrysibLYRcCQE1vhA1eAUjYBeIiJ7hhQ8nQ7tR%2B23SYpdNTnpkjeERDPmjd3RyO7Xu67QU%2BS8mPD6NJuXKR3jHY5r1VQh4CjG9V%2B%2BcHuZHeJfIP0%2FQmGo9xvykzSjzKZtbdnObB9s3ZJ4%2BGHrtmBxXIm4QkzRm3s1yauPLjeqQkqiavHZuqbHC%2BW0ZrJ%2BMRX77nNmAlMFM54Nzf4ea6d139N9QLnbDWciTVjJfQLBMvvDS3qo6MLBUBUPYFX182wqO4C9%2FHLdhBP%2FLxEnbqG6z6U1Z9NiETcyiag%2FuZACaL6CGg0zY%2Bd9kHfG9TnL4loDHsIsGH5s%2FkfrgT0GAFLm%2F31Qv6YAzSX71YQ1C7acvCL9lMG5a%2F1sgF7q51RiqwrwNaTbweI9%2FAVve1Cwy7utB0yWYq%2BqLfuMWK0pdycapO8kYGwdbGkY6slcNoTEJm3JEa19pK38NUmOk%2BMPSS9MOx8bhMl3GZaGgcy7CkWRks9w1rh9eiHUTqzv6Tq2ARMiMoLt6iJL0L0GBHGsqbAlpjH4cGCLlMIOq77wGOqUBOT5ZBLtJJ6X33Bb9QaDBNMif2kuXwqoEiBG%2FtKklUOsme0u0F%2FnM1%2FEHvgjzxE88ZW%2FFrm9XO097yZyMkIrDUvVurXn7SCRaLVc4aq7u3P4pQjsgKNkrQTdDJW6ccfoD%2FMshXxG9pAzJtFdFxLHqsHW2rxypz8U2vFZZ5fETER4roy1LQcd%2FTBF2pgZ5HNritHIKA8TuP0dRNubYJDHRLl3FYVdt&X-Amz-Signature=b49a3e83619be6743aa330a86412684d3dc4eae6d40de76edec23af3147c1ae8&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MGGZA5D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJaks8MoSCD%2FFlV7FhcK5%2BlMfZM1zn48eHEnH6c9evqwIhALYyWNZ2RHqVZE8YbJS%2BPHrnbav6WBwMvsYzVGOxuqefKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYxgnHLN%2BL0Mb28eYq3ANVzYnn1ttMxafxlrVuhCCCt0StGFcpqwB576ON2VcuX6Bck05t518qAuC7Pqjef8FklMweW7jN0wp5bPPAulzC%2B3pWCcm6Zj%2BPMuP2dX1tlmF8%2F03GLrLqnvTAXUIsuv5maQ9eqpodtrVQx4kOZeSHjX6FNIxM4c9Sfz4aQcbXB87iM%2FoJixOfGsjz2FPmW1Kx0V9Nk4nbhIeC9Gi7I2RYOLXOSuwAomaUx4LOFOSxCVeIe9tOktPKiPIAvq6L5dJc3aks17dsW7jskWptw%2B5j5NZw%2BBus7A%2FpMRZfisffTs98UsXHhxowqAqGmRq1NC8QNi%2FBmF21Ad3Bi5EKLNbIUm1bvpzv%2FiK%2Fgaql%2B6RCDaGu1Gk%2B2YujT5i728cHqDbcuKMtn6%2FTy14c9T2gr%2Fxo3O0xSyrBqr6mEeK8%2FHgCwB56Bg8MjDd0b71GStjoNJi51lXnpBtZWJByFQgb%2BNNGvgO7Y%2BciFtZaN0Y2IYQlQSj3%2Bo5HBqmzq4nBIfZ87o8fuOHK24Q609qs8EDcJpz1wWNHYYbkDVHtNO1Bg6RGN95Q64OTurSfKue%2BzJrh0C8RrIxnnfSqPJZU%2Fp0NkZNLznmuSbAaWpiuOX0wnNcYBmAIrco%2BxyjoX1PFZDDZqe%2B8BjqkAQc2arHt0%2BGfPCpAJ%2B%2BpfE48SRW%2FTQlj0AngjE04kBUojowKYl39JuDacal8u7sr8uzlQFNLxQX38MG%2FSu1BqGufKvhorVlLGyOn1H063PZwiZcS%2BEocBHxyBZSA0AEbOYZWDK%2BQO7xYdO6TClwhTkCYKvv0Qrz51lih2mxL2fwCQ869ErWiAUtM3OY%2FevNEbEK5Fn%2FJL7rfZ%2FuyF3H96eBF36Cn&X-Amz-Signature=6f2402d9daacad042c669a8b2daaedbd11fbbd06986a8db6f8660307fcf2cc05&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YARXRNPN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVBdcSSBip2inkLqH5%2F7Od0lhJUaXRnisthFDvT6DvtwIgKdvTCdLqHIvV9JZM0bpuPbBlFviceL1jJy3ZFc6ZsSkqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI1QPGNiwftwXt2m%2FCrcA6egNX5IXbdiMWS7jfw%2FybsfscqmQX8hPcHMINjb1zcehXGaj6CYrm5FggeD4QnaazeJest9XyIVH6M7nZUgRJUnGev%2BxoMjxeuw3zWKA6wecf6J%2FF3T1CMDsXlEgJ610XAx3M7w19rbQscYlY7lYZ2yPV7mxoE%2FdwCK6qxzNC4E4b6YRd%2FAmM7FFr5XxVKleE3yFXBHCrrYhGQv2TQy%2Blfk6%2B%2B6RpKHrxEhYvZXHhRJ3nI9Id3CgOuLYYqLLeaeFARkFQdcFfsH8QaRLOGVYwlWobVgIKhCZxRTrFzwAc0kQVWgrybK2Nd5aWiQjPL7CNyged86WFAmZNBxwClpXfjWGexBVB1YiVSug1RZ32%2FbJzQCqPoXTkuc78zJVp11zjYQspYo48B6J43f6tLCOOC4RIAyhDVUP7lk6jtbT5jpnTB6z79zkPvrsBWWuofCUeANfee4PWfXUS9Rm7tsMdYs1Wa6%2FLO4Y348FRdFB8P%2FQwkYFQ2rOhQHZdK6fxwEC0fi%2BXJaOU15vaSo2nEqtJ9c9AvwYDK45t8mIA8mlPQVXKNAIPvQOAk0U9w5O3NSlpyVOruUFcu1fi39vXtat9lBqguURfP2Ir%2Fud9XOfM70o1lf1D1SFeymzRy6MMap77wGOqUB19VDNFON%2BKhTuliKxG0QrFtl5q7Uus%2BlGU%2BckBfSl1TrlXSkmfbWtvDlWaOn%2Bsk13NAj29FCphSO8%2FQa74J8twNdkneemZyh%2FHAOFSj26ZFNZYZK1NXuLJUJullf2m3%2BDnj2K%2FcH0tS2ZDtGCjy9VvqnRPZcKUJwF6LD00azqOmv893PIHLVsx8GA3pStX8w4vkGkqtJMYlK%2B5F8QPD5P41SINaP&X-Amz-Signature=e3ac8ad0e7c2e255db7412a1d9b24add800e0d9a8baec676d9dc68d69ac6a53f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OPVFLD3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA9%2FZZLoq54SvD0wwqyTGDtb%2FtLHT2Gj6BFk6SwTBYmTAiB5ubioeeDHNj5Cj2ulVFqJGPRnxwQapmSXNtmAd%2BcytyqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUZawZK1lfzwZqpqrKtwDHyUz9C%2BnlhYfnH9A1uKO5umFeGDWFpla%2B3xkl7VpGjWloZdMOkgPPp2B77jK8mJLIInoED6fEwlByBpOJhRi%2BFJG%2F0UFZBewPmj4PV9hB0K1I4TgPqurx%2BrWECvLxJPFwDzQ1hnEz7n1%2FKtm83YNtJ%2F4Tz3j%2F0WP2RHBlDplzuPmDeXe0mPDiuAozcJ%2Bnl4iavPfiTu21JaQ228EEpDLmm6rg3az9Qt55%2FJ%2BCqSidY0oiK%2Fx1brbuOgLj6HMEgW9GSmKDd8rS22rrLECQ6mS7YlXvVsFxwFLyQ85B%2BU3RSCsAt42o7JBPm2%2FbpyffHBzB3Zl07i4%2BbsKslquK%2FU71p%2FipZp4n0ALIbas3NcShvc9fGV6e4HZTCe9pnXFS4EfOdM4xb2tjR93X7ajc28CH6aTjREHv6aJndDzVzHPGefsGI%2FrwlfBDHvzEI43Q053YAQMs7Yb94sHL%2BSIZGIhSDHD0VhR8yrT68kgE%2F6f7oXK6lE4TZmxezLTx162F2penactaaEpep8Fyc8osbtnDEU508AttgO9qIAsJdB21IHdy3OgVTHnlZGtkL%2BUg1fJBHKNo8GATXkTW%2BlSFkySxW4c3hKhWgrqYet3mlXZjM2umhxEUf67o2OZB28w16nvvAY6pgE1pTksr4u2WRN%2BOYAIPbFvApDKQsy9cZoj5rI5jYxuGLJLuMvDUCnHDybtIMp98vH%2FH0PAw3x9O8KRUoH5C2CBwCgEAi1630L86MlYQPpbVnqJO%2F7j7fOmOh44kc0mF4%2BkODGiqpq3NShfUUq%2FiXdec1OWAj0qf22iSVRuYfoNW4ZsEWrTZun8er0hRbHT7FhlT%2FeiH%2FxX8fMnZH5KwJ5RAkOF39iU&X-Amz-Signature=88e1d6fb95564c0f90623adb910c0a93dc66bbad608a06a7567f49f8af258293&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OPVFLD3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA9%2FZZLoq54SvD0wwqyTGDtb%2FtLHT2Gj6BFk6SwTBYmTAiB5ubioeeDHNj5Cj2ulVFqJGPRnxwQapmSXNtmAd%2BcytyqIBAit%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUZawZK1lfzwZqpqrKtwDHyUz9C%2BnlhYfnH9A1uKO5umFeGDWFpla%2B3xkl7VpGjWloZdMOkgPPp2B77jK8mJLIInoED6fEwlByBpOJhRi%2BFJG%2F0UFZBewPmj4PV9hB0K1I4TgPqurx%2BrWECvLxJPFwDzQ1hnEz7n1%2FKtm83YNtJ%2F4Tz3j%2F0WP2RHBlDplzuPmDeXe0mPDiuAozcJ%2Bnl4iavPfiTu21JaQ228EEpDLmm6rg3az9Qt55%2FJ%2BCqSidY0oiK%2Fx1brbuOgLj6HMEgW9GSmKDd8rS22rrLECQ6mS7YlXvVsFxwFLyQ85B%2BU3RSCsAt42o7JBPm2%2FbpyffHBzB3Zl07i4%2BbsKslquK%2FU71p%2FipZp4n0ALIbas3NcShvc9fGV6e4HZTCe9pnXFS4EfOdM4xb2tjR93X7ajc28CH6aTjREHv6aJndDzVzHPGefsGI%2FrwlfBDHvzEI43Q053YAQMs7Yb94sHL%2BSIZGIhSDHD0VhR8yrT68kgE%2F6f7oXK6lE4TZmxezLTx162F2penactaaEpep8Fyc8osbtnDEU508AttgO9qIAsJdB21IHdy3OgVTHnlZGtkL%2BUg1fJBHKNo8GATXkTW%2BlSFkySxW4c3hKhWgrqYet3mlXZjM2umhxEUf67o2OZB28w16nvvAY6pgE1pTksr4u2WRN%2BOYAIPbFvApDKQsy9cZoj5rI5jYxuGLJLuMvDUCnHDybtIMp98vH%2FH0PAw3x9O8KRUoH5C2CBwCgEAi1630L86MlYQPpbVnqJO%2F7j7fOmOh44kc0mF4%2BkODGiqpq3NShfUUq%2FiXdec1OWAj0qf22iSVRuYfoNW4ZsEWrTZun8er0hRbHT7FhlT%2FeiH%2FxX8fMnZH5KwJ5RAkOF39iU&X-Amz-Signature=c4b0cda95b2e84a328d3046fab8283a8a5594cc8d4834c44fb5fed9e803bf440&X-Amz-SignedHeaders=host&x-id=GetObject)

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
