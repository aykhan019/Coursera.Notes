

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662APBNVSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQPI6eJYz%2BdHF8WBRKVp0AbDq1evy1xRtbwpuFw%2FCkwwIgATPRLMo%2BKtMmS8k99RbX1tYKW6t67yNorKXyesDX27QqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhrN9HwumNzEVBeXCrcA73W6R%2FqsDlOLXGBmM9OwiQnhHbebbdtW42H8tL%2BHKy3cJ8Cyg1AUQlhyUmdh7GQYlwQj8JbzgfWvwFTpAYbz4K08KZ95MD0IdRXVDtcCI4s5FaRkf14vHx4N59orODfMOH2HkF5Z11c8txcziBaceXk0rv%2FkNHdVN9TkbWiEvAdDs1Cl4uiYpiAgJ7ZsUqBTfWanxgVvDMzPyjHrZ82il6yX2In3P0WQZvCVKqW9y6oL%2F70fLnzISu1l%2BisQUtWG7it%2FW7lvnriQ1K0LW9GdTnN7tQ7da9DA09BLBm8sIexCknCGWzeeDEluH9hHOCY1tlNZTJ5UzRFc91wIRI%2Biy%2BE1VbEnAtV8ei04ZN2EkijQPEDMrw8%2FATEc6E%2F%2BDp%2BklNlgOXvvjrY7ip47EgYb9lga2DcvEf2Cw4oZy4l47DtPK430Aoh%2B5aSps1%2B4ntmRNp8Tw6sTTcsB%2F%2F16Q%2BKfmZPuyP1x7ckbSrt4uGikpFAFF4A0XfIKkmm1mkEwOqzKjB4XX6kQMcXLHGO9Ms3Iyrcm0TXYkXK19EAyVQD4y%2BcSAMFpvqDn54Yo2PsjsDeqBrH5OmrlKtzUi3Jtdi6%2FIFSP8yvlx5V6RPAz1huQ3bbQw7EHip8k0FkKzYVMJac%2FLwGOqUB0YVIgMPqleK%2FG3lGXmM%2BAlx3mZd%2FRCUrnO9h1UHhp5SoC3AOI9QTHzsqyIlONCaU1hrRhbhqFZGvu5%2FNOauWbokd153l0CnInoWWGzuyRuwivp%2FyPUD7z7f%2Ba7pSyMnKnIbBOUQyG99XdQ1SjLTNArUkG8HDFU0s1cwmK1JmQCChAE1EqORvZIYWy0%2BI%2BoDfS8l0u5BL7nQQESw63nJRKhQWKHoc&X-Amz-Signature=2f46ea76bad8d4de700e8ea61a0cde89d93c2b371815b908cdefea7b10d6b313&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662APBNVSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQPI6eJYz%2BdHF8WBRKVp0AbDq1evy1xRtbwpuFw%2FCkwwIgATPRLMo%2BKtMmS8k99RbX1tYKW6t67yNorKXyesDX27QqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhrN9HwumNzEVBeXCrcA73W6R%2FqsDlOLXGBmM9OwiQnhHbebbdtW42H8tL%2BHKy3cJ8Cyg1AUQlhyUmdh7GQYlwQj8JbzgfWvwFTpAYbz4K08KZ95MD0IdRXVDtcCI4s5FaRkf14vHx4N59orODfMOH2HkF5Z11c8txcziBaceXk0rv%2FkNHdVN9TkbWiEvAdDs1Cl4uiYpiAgJ7ZsUqBTfWanxgVvDMzPyjHrZ82il6yX2In3P0WQZvCVKqW9y6oL%2F70fLnzISu1l%2BisQUtWG7it%2FW7lvnriQ1K0LW9GdTnN7tQ7da9DA09BLBm8sIexCknCGWzeeDEluH9hHOCY1tlNZTJ5UzRFc91wIRI%2Biy%2BE1VbEnAtV8ei04ZN2EkijQPEDMrw8%2FATEc6E%2F%2BDp%2BklNlgOXvvjrY7ip47EgYb9lga2DcvEf2Cw4oZy4l47DtPK430Aoh%2B5aSps1%2B4ntmRNp8Tw6sTTcsB%2F%2F16Q%2BKfmZPuyP1x7ckbSrt4uGikpFAFF4A0XfIKkmm1mkEwOqzKjB4XX6kQMcXLHGO9Ms3Iyrcm0TXYkXK19EAyVQD4y%2BcSAMFpvqDn54Yo2PsjsDeqBrH5OmrlKtzUi3Jtdi6%2FIFSP8yvlx5V6RPAz1huQ3bbQw7EHip8k0FkKzYVMJac%2FLwGOqUB0YVIgMPqleK%2FG3lGXmM%2BAlx3mZd%2FRCUrnO9h1UHhp5SoC3AOI9QTHzsqyIlONCaU1hrRhbhqFZGvu5%2FNOauWbokd153l0CnInoWWGzuyRuwivp%2FyPUD7z7f%2Ba7pSyMnKnIbBOUQyG99XdQ1SjLTNArUkG8HDFU0s1cwmK1JmQCChAE1EqORvZIYWy0%2BI%2BoDfS8l0u5BL7nQQESw63nJRKhQWKHoc&X-Amz-Signature=42c2dac8e48fbfcc2a46e8d399fd80fc32d40e33c3ae31c9180f5db1057f6b87&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662APBNVSB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQPI6eJYz%2BdHF8WBRKVp0AbDq1evy1xRtbwpuFw%2FCkwwIgATPRLMo%2BKtMmS8k99RbX1tYKW6t67yNorKXyesDX27QqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhrN9HwumNzEVBeXCrcA73W6R%2FqsDlOLXGBmM9OwiQnhHbebbdtW42H8tL%2BHKy3cJ8Cyg1AUQlhyUmdh7GQYlwQj8JbzgfWvwFTpAYbz4K08KZ95MD0IdRXVDtcCI4s5FaRkf14vHx4N59orODfMOH2HkF5Z11c8txcziBaceXk0rv%2FkNHdVN9TkbWiEvAdDs1Cl4uiYpiAgJ7ZsUqBTfWanxgVvDMzPyjHrZ82il6yX2In3P0WQZvCVKqW9y6oL%2F70fLnzISu1l%2BisQUtWG7it%2FW7lvnriQ1K0LW9GdTnN7tQ7da9DA09BLBm8sIexCknCGWzeeDEluH9hHOCY1tlNZTJ5UzRFc91wIRI%2Biy%2BE1VbEnAtV8ei04ZN2EkijQPEDMrw8%2FATEc6E%2F%2BDp%2BklNlgOXvvjrY7ip47EgYb9lga2DcvEf2Cw4oZy4l47DtPK430Aoh%2B5aSps1%2B4ntmRNp8Tw6sTTcsB%2F%2F16Q%2BKfmZPuyP1x7ckbSrt4uGikpFAFF4A0XfIKkmm1mkEwOqzKjB4XX6kQMcXLHGO9Ms3Iyrcm0TXYkXK19EAyVQD4y%2BcSAMFpvqDn54Yo2PsjsDeqBrH5OmrlKtzUi3Jtdi6%2FIFSP8yvlx5V6RPAz1huQ3bbQw7EHip8k0FkKzYVMJac%2FLwGOqUB0YVIgMPqleK%2FG3lGXmM%2BAlx3mZd%2FRCUrnO9h1UHhp5SoC3AOI9QTHzsqyIlONCaU1hrRhbhqFZGvu5%2FNOauWbokd153l0CnInoWWGzuyRuwivp%2FyPUD7z7f%2Ba7pSyMnKnIbBOUQyG99XdQ1SjLTNArUkG8HDFU0s1cwmK1JmQCChAE1EqORvZIYWy0%2BI%2BoDfS8l0u5BL7nQQESw63nJRKhQWKHoc&X-Amz-Signature=f8c2ff95589538c4f909cf1a2a65250cf42098cc95df3a137732e918dd2aca15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNT2PGVL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCm%2BfJBTsyHMIrqFhi1lKaIhKE%2FH8GlqcXZoNjxenycAiEAlhFM%2BnbxlH4Tsr3w87MwDYU8%2BeGMkrZLFFsMPYhuI5kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDd41eybCV2B24otyrcA2%2BUQA3Ozo26rowSJPD2eAbMseDW8mD%2BEIEyk7V99x296mT9Bvz44o5Yj6enSN1hXXmKbtZC2qExuhUvh%2BIwRdFgyk%2FxfT3JhLYT8N7MhwuxvCCv%2F%2FaXNWhpFDFWGAJRRyKsikfmFu2h%2BRL%2FdjGbEiWAeWl9h1UeehdAXXkVm1Hmq8eXL3fQSNIAsiqCieGieEboUshSDC%2FxsX83WV%2FehKte9ui8UfAyyZuOeSqy0sxFeZWsK3graIKXaSQ%2Bus0aDQZSKK5J4CHI3MxYMwp1fKuQXE%2Fm48kwlFYDZS7Z6mZl1WrYD6RBs377tMlRv3VBIlJAvKlZ9BsLqBkIDZrIzVzaLZ4uT5z2O4DSHrVNd0IOKjfXzgco1Lasi5rKp40HJAm4r6yglWOJwiPKkkzPulHDI9ZOczgfh09x%2BP2G%2FwsUd%2FzdJo%2BhBlm7nO%2BFdwfFbUMJME0qOADFKXcyMUHAChrLxpU7lLPS701X%2FOOoK1yG9UNsG%2FoGF9Dai5my4A1vE1Rl8mJF6pnuSQ61Jiol%2Flcs3iOyHlxcCZVqyHHhmVrEGoqoIyL3Oqj3r20TRtbm2cwjGW12jpU%2BYH%2FuQX3hl01xsZU8AgnlOXSRZNiouCr09p91qj4q4DCu9qmeMOWb%2FLwGOqUBEJE6wTvT%2BeuQGf8K7k1t6CjblH2O8TJ0s%2BlkwYXj%2FDUgavZnmPfp4EpKe0CImcwS4jbXhdkClcXVZZF5luTy9R3PgdWqmq9HLWruM9uv5YMgHwEfjTpSzovHHCRf91EiUHaf5xov%2BjRNIhGOaOZaI7s2xiHzbLa%2FBi83zVOndqh%2BDH%2FPZ086GwiWqmUY8rg6vgGzc4J6YXOsAJb9EBAFTnOV2zbf&X-Amz-Signature=71b1e2f9213c561177d707ebc47fa89fcf1099fbf68a883f86949d24a1a957f8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNT2PGVL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCm%2BfJBTsyHMIrqFhi1lKaIhKE%2FH8GlqcXZoNjxenycAiEAlhFM%2BnbxlH4Tsr3w87MwDYU8%2BeGMkrZLFFsMPYhuI5kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDd41eybCV2B24otyrcA2%2BUQA3Ozo26rowSJPD2eAbMseDW8mD%2BEIEyk7V99x296mT9Bvz44o5Yj6enSN1hXXmKbtZC2qExuhUvh%2BIwRdFgyk%2FxfT3JhLYT8N7MhwuxvCCv%2F%2FaXNWhpFDFWGAJRRyKsikfmFu2h%2BRL%2FdjGbEiWAeWl9h1UeehdAXXkVm1Hmq8eXL3fQSNIAsiqCieGieEboUshSDC%2FxsX83WV%2FehKte9ui8UfAyyZuOeSqy0sxFeZWsK3graIKXaSQ%2Bus0aDQZSKK5J4CHI3MxYMwp1fKuQXE%2Fm48kwlFYDZS7Z6mZl1WrYD6RBs377tMlRv3VBIlJAvKlZ9BsLqBkIDZrIzVzaLZ4uT5z2O4DSHrVNd0IOKjfXzgco1Lasi5rKp40HJAm4r6yglWOJwiPKkkzPulHDI9ZOczgfh09x%2BP2G%2FwsUd%2FzdJo%2BhBlm7nO%2BFdwfFbUMJME0qOADFKXcyMUHAChrLxpU7lLPS701X%2FOOoK1yG9UNsG%2FoGF9Dai5my4A1vE1Rl8mJF6pnuSQ61Jiol%2Flcs3iOyHlxcCZVqyHHhmVrEGoqoIyL3Oqj3r20TRtbm2cwjGW12jpU%2BYH%2FuQX3hl01xsZU8AgnlOXSRZNiouCr09p91qj4q4DCu9qmeMOWb%2FLwGOqUBEJE6wTvT%2BeuQGf8K7k1t6CjblH2O8TJ0s%2BlkwYXj%2FDUgavZnmPfp4EpKe0CImcwS4jbXhdkClcXVZZF5luTy9R3PgdWqmq9HLWruM9uv5YMgHwEfjTpSzovHHCRf91EiUHaf5xov%2BjRNIhGOaOZaI7s2xiHzbLa%2FBi83zVOndqh%2BDH%2FPZ086GwiWqmUY8rg6vgGzc4J6YXOsAJb9EBAFTnOV2zbf&X-Amz-Signature=c7f5dce72efa7e0c29cd7d766bb8e94c8b91b39ae650cf1fc5dfc4945efbf8b1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNT2PGVL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCm%2BfJBTsyHMIrqFhi1lKaIhKE%2FH8GlqcXZoNjxenycAiEAlhFM%2BnbxlH4Tsr3w87MwDYU8%2BeGMkrZLFFsMPYhuI5kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDd41eybCV2B24otyrcA2%2BUQA3Ozo26rowSJPD2eAbMseDW8mD%2BEIEyk7V99x296mT9Bvz44o5Yj6enSN1hXXmKbtZC2qExuhUvh%2BIwRdFgyk%2FxfT3JhLYT8N7MhwuxvCCv%2F%2FaXNWhpFDFWGAJRRyKsikfmFu2h%2BRL%2FdjGbEiWAeWl9h1UeehdAXXkVm1Hmq8eXL3fQSNIAsiqCieGieEboUshSDC%2FxsX83WV%2FehKte9ui8UfAyyZuOeSqy0sxFeZWsK3graIKXaSQ%2Bus0aDQZSKK5J4CHI3MxYMwp1fKuQXE%2Fm48kwlFYDZS7Z6mZl1WrYD6RBs377tMlRv3VBIlJAvKlZ9BsLqBkIDZrIzVzaLZ4uT5z2O4DSHrVNd0IOKjfXzgco1Lasi5rKp40HJAm4r6yglWOJwiPKkkzPulHDI9ZOczgfh09x%2BP2G%2FwsUd%2FzdJo%2BhBlm7nO%2BFdwfFbUMJME0qOADFKXcyMUHAChrLxpU7lLPS701X%2FOOoK1yG9UNsG%2FoGF9Dai5my4A1vE1Rl8mJF6pnuSQ61Jiol%2Flcs3iOyHlxcCZVqyHHhmVrEGoqoIyL3Oqj3r20TRtbm2cwjGW12jpU%2BYH%2FuQX3hl01xsZU8AgnlOXSRZNiouCr09p91qj4q4DCu9qmeMOWb%2FLwGOqUBEJE6wTvT%2BeuQGf8K7k1t6CjblH2O8TJ0s%2BlkwYXj%2FDUgavZnmPfp4EpKe0CImcwS4jbXhdkClcXVZZF5luTy9R3PgdWqmq9HLWruM9uv5YMgHwEfjTpSzovHHCRf91EiUHaf5xov%2BjRNIhGOaOZaI7s2xiHzbLa%2FBi83zVOndqh%2BDH%2FPZ086GwiWqmUY8rg6vgGzc4J6YXOsAJb9EBAFTnOV2zbf&X-Amz-Signature=e7eecdb75a2898f17a88af1e9a888accad4a84ab3fb2fd5ebf5dadc3926d7dd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNT2PGVL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCm%2BfJBTsyHMIrqFhi1lKaIhKE%2FH8GlqcXZoNjxenycAiEAlhFM%2BnbxlH4Tsr3w87MwDYU8%2BeGMkrZLFFsMPYhuI5kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDd41eybCV2B24otyrcA2%2BUQA3Ozo26rowSJPD2eAbMseDW8mD%2BEIEyk7V99x296mT9Bvz44o5Yj6enSN1hXXmKbtZC2qExuhUvh%2BIwRdFgyk%2FxfT3JhLYT8N7MhwuxvCCv%2F%2FaXNWhpFDFWGAJRRyKsikfmFu2h%2BRL%2FdjGbEiWAeWl9h1UeehdAXXkVm1Hmq8eXL3fQSNIAsiqCieGieEboUshSDC%2FxsX83WV%2FehKte9ui8UfAyyZuOeSqy0sxFeZWsK3graIKXaSQ%2Bus0aDQZSKK5J4CHI3MxYMwp1fKuQXE%2Fm48kwlFYDZS7Z6mZl1WrYD6RBs377tMlRv3VBIlJAvKlZ9BsLqBkIDZrIzVzaLZ4uT5z2O4DSHrVNd0IOKjfXzgco1Lasi5rKp40HJAm4r6yglWOJwiPKkkzPulHDI9ZOczgfh09x%2BP2G%2FwsUd%2FzdJo%2BhBlm7nO%2BFdwfFbUMJME0qOADFKXcyMUHAChrLxpU7lLPS701X%2FOOoK1yG9UNsG%2FoGF9Dai5my4A1vE1Rl8mJF6pnuSQ61Jiol%2Flcs3iOyHlxcCZVqyHHhmVrEGoqoIyL3Oqj3r20TRtbm2cwjGW12jpU%2BYH%2FuQX3hl01xsZU8AgnlOXSRZNiouCr09p91qj4q4DCu9qmeMOWb%2FLwGOqUBEJE6wTvT%2BeuQGf8K7k1t6CjblH2O8TJ0s%2BlkwYXj%2FDUgavZnmPfp4EpKe0CImcwS4jbXhdkClcXVZZF5luTy9R3PgdWqmq9HLWruM9uv5YMgHwEfjTpSzovHHCRf91EiUHaf5xov%2BjRNIhGOaOZaI7s2xiHzbLa%2FBi83zVOndqh%2BDH%2FPZ086GwiWqmUY8rg6vgGzc4J6YXOsAJb9EBAFTnOV2zbf&X-Amz-Signature=d86c038c7f9f6fa529cb24585bfd76b46fc24e5a1409cff1d7af2ecef025efd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNT2PGVL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCm%2BfJBTsyHMIrqFhi1lKaIhKE%2FH8GlqcXZoNjxenycAiEAlhFM%2BnbxlH4Tsr3w87MwDYU8%2BeGMkrZLFFsMPYhuI5kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDd41eybCV2B24otyrcA2%2BUQA3Ozo26rowSJPD2eAbMseDW8mD%2BEIEyk7V99x296mT9Bvz44o5Yj6enSN1hXXmKbtZC2qExuhUvh%2BIwRdFgyk%2FxfT3JhLYT8N7MhwuxvCCv%2F%2FaXNWhpFDFWGAJRRyKsikfmFu2h%2BRL%2FdjGbEiWAeWl9h1UeehdAXXkVm1Hmq8eXL3fQSNIAsiqCieGieEboUshSDC%2FxsX83WV%2FehKte9ui8UfAyyZuOeSqy0sxFeZWsK3graIKXaSQ%2Bus0aDQZSKK5J4CHI3MxYMwp1fKuQXE%2Fm48kwlFYDZS7Z6mZl1WrYD6RBs377tMlRv3VBIlJAvKlZ9BsLqBkIDZrIzVzaLZ4uT5z2O4DSHrVNd0IOKjfXzgco1Lasi5rKp40HJAm4r6yglWOJwiPKkkzPulHDI9ZOczgfh09x%2BP2G%2FwsUd%2FzdJo%2BhBlm7nO%2BFdwfFbUMJME0qOADFKXcyMUHAChrLxpU7lLPS701X%2FOOoK1yG9UNsG%2FoGF9Dai5my4A1vE1Rl8mJF6pnuSQ61Jiol%2Flcs3iOyHlxcCZVqyHHhmVrEGoqoIyL3Oqj3r20TRtbm2cwjGW12jpU%2BYH%2FuQX3hl01xsZU8AgnlOXSRZNiouCr09p91qj4q4DCu9qmeMOWb%2FLwGOqUBEJE6wTvT%2BeuQGf8K7k1t6CjblH2O8TJ0s%2BlkwYXj%2FDUgavZnmPfp4EpKe0CImcwS4jbXhdkClcXVZZF5luTy9R3PgdWqmq9HLWruM9uv5YMgHwEfjTpSzovHHCRf91EiUHaf5xov%2BjRNIhGOaOZaI7s2xiHzbLa%2FBi83zVOndqh%2BDH%2FPZ086GwiWqmUY8rg6vgGzc4J6YXOsAJb9EBAFTnOV2zbf&X-Amz-Signature=a02159ebc5bf638c17c50eb4839fb1c3c77a8a799e7d844b2b0da8693ec06339&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNT2PGVL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCm%2BfJBTsyHMIrqFhi1lKaIhKE%2FH8GlqcXZoNjxenycAiEAlhFM%2BnbxlH4Tsr3w87MwDYU8%2BeGMkrZLFFsMPYhuI5kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDd41eybCV2B24otyrcA2%2BUQA3Ozo26rowSJPD2eAbMseDW8mD%2BEIEyk7V99x296mT9Bvz44o5Yj6enSN1hXXmKbtZC2qExuhUvh%2BIwRdFgyk%2FxfT3JhLYT8N7MhwuxvCCv%2F%2FaXNWhpFDFWGAJRRyKsikfmFu2h%2BRL%2FdjGbEiWAeWl9h1UeehdAXXkVm1Hmq8eXL3fQSNIAsiqCieGieEboUshSDC%2FxsX83WV%2FehKte9ui8UfAyyZuOeSqy0sxFeZWsK3graIKXaSQ%2Bus0aDQZSKK5J4CHI3MxYMwp1fKuQXE%2Fm48kwlFYDZS7Z6mZl1WrYD6RBs377tMlRv3VBIlJAvKlZ9BsLqBkIDZrIzVzaLZ4uT5z2O4DSHrVNd0IOKjfXzgco1Lasi5rKp40HJAm4r6yglWOJwiPKkkzPulHDI9ZOczgfh09x%2BP2G%2FwsUd%2FzdJo%2BhBlm7nO%2BFdwfFbUMJME0qOADFKXcyMUHAChrLxpU7lLPS701X%2FOOoK1yG9UNsG%2FoGF9Dai5my4A1vE1Rl8mJF6pnuSQ61Jiol%2Flcs3iOyHlxcCZVqyHHhmVrEGoqoIyL3Oqj3r20TRtbm2cwjGW12jpU%2BYH%2FuQX3hl01xsZU8AgnlOXSRZNiouCr09p91qj4q4DCu9qmeMOWb%2FLwGOqUBEJE6wTvT%2BeuQGf8K7k1t6CjblH2O8TJ0s%2BlkwYXj%2FDUgavZnmPfp4EpKe0CImcwS4jbXhdkClcXVZZF5luTy9R3PgdWqmq9HLWruM9uv5YMgHwEfjTpSzovHHCRf91EiUHaf5xov%2BjRNIhGOaOZaI7s2xiHzbLa%2FBi83zVOndqh%2BDH%2FPZ086GwiWqmUY8rg6vgGzc4J6YXOsAJb9EBAFTnOV2zbf&X-Amz-Signature=74ce04bedf309d4132a72dec766c0f5aefc01b6aea50c362430b0bb1921dec5f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLGN5SVY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGx%2Bty%2BTFUKJkx%2FpeGxPX78wl9YQebgbEgo1lxWoI32tAiAKSC4HXollb6cefvURMlz3IEC0REUw0JJLt2NpZIZT%2FiqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMu6hPdv03mfyx%2B%2BvSKtwDnR8J49z4h8m3gDYM2znbp9sq0%2BcnHtX7q6Rd3yq2xok73%2BsqXeArWmQdp68phHogX2SFxAQ8RS%2BczPIxxOQSvqxv32L0%2FjaexixUXRb6oqkw%2Bl2GdU5bWbw1rg8ZeHILnKBxBGAoItN9FzmOd3dAv%2BtjJUIy9dM1ijisFgE1cSoJimDp51OypB%2FuGBm0MhtZF9Xq2B%2B7vCc14wFfwM%2F0PKKHwTt1f3qEZLys5lZ9Q3iuRJL3lsyehPKhniR%2B7f1S83945bGQsoAeL34kUr6pxVgiNJMThcMVrK9oRJnqHxEv9%2Bin6tm8jnXramASyg8BP2tX1PDKrfNYuaG3x15o9ALUzMFxc5awot6kI0xzGE%2BNWZmLSnqzyHdMelpQbdoBwTPj6BM5uMZo9SoMXifsN0iiMZ3l3ZRGDbj4AjFzJ9JcbCpeKgbxW1F1yIvroRFjvCXAL0nh%2B%2Bjox6XplmhxlYygmyPgVZxEbXtWGC8t8ePVpeUAcNxlwiXnNxM3l%2BlIE2WyoGU9SL0o7sl1Hn%2BD3JRWLgImhx2GCrFpImWwBFgQRcX4E6QxM0NIFfg4b%2FjTUQzuRFqdJ%2FF7O%2FNM8jGfPNCvekuZ9SotN3VgU6iPRQq4Zq0VJvMFGYhM9gowlpz8vAY6pgGCNmlPRShwMhWP6BYS28c6ehmrraRhTOBhb4zL9g%2BCkLXfwtk%2Bh5HtH3yHfYVEdIUp0OL29KcypnxmnHlmoFxie7tYbHVHc30SMzN%2FkPWX%2BoGEGlTLiHNo%2BpcSkYJPd8BwEenKkCyfnGOz4drL%2Fdoztd4s9R55itm9Bw%2FrVD%2B2p0BaX7WYbgv2X5askqFUi3WBakS0LKuLeewLkVTl6iHOGt12bUy0&X-Amz-Signature=d2642abf0cc528423e3944439ccbbcd2da528746635ae4c68a64633c80965ea4&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2UHPETS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHgkIc8YRTYTqd7cUDC5NoQHrq5HaENBwxXvp2SwR3EhAiEA2aGA6wF6r4AUN84aIRPI%2Bca%2FFa%2Fzv5llstNK7Da0sVgqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB8IJpX%2FZxP1Dt2O%2BCrcA6HJ9h3asj2ttgQJDgkeix3QpSRN0Mx1a%2BKjHIGdSbtPv0xyEIwOn0dH2MFINwQUoKthp9BKWRxbvVqEkN87s5VvJ3q%2FRhQFwOZT3wVv8KIZscMQS3QMeHl1KCvbyx8%2Bhp3kh%2FdNCKNdD48%2FOptGdN%2FJfki3WWSGkKUXD9OMNPZsTRn7FnN9KcZvfp7xUR4x24h4SDghFe6GYveaBnuAreCLrtjrJIL2tSsNrnfl5xfnJYTQiQoMWlUXJhV2aiEkzV%2FUyy1%2Fai1Umt0Ucftf34P9aR3%2FY%2FWyjYF6wdb07ilBsKz5YPPiR%2FpEtJ%2FLJYSymlBguiUA84Nw6PpdF%2BCNzfUC2zqdPNPpl951YGbpivFB1rUMhyr14x231l14WtNUjpCqn1hpHfH3fj03rFaPrHNUIE8zwpKLwmSK5xhs4ZQBYSJ%2FaG1AhgReLa1VBhfgXfJN7F0TvQP9Ks9I22TWgtn%2FWj1FgCeGiWVhAiaD53LGg86UJkGobXTRFEoRzqn2BjWbVtCHu8XG6P6LGdoSdUOAMU%2BCn06opajDv0DnSiX%2F2gucEYNnm6uPFNDbzXxzUYeBY%2BZUZ8pntJi1rH17jQa6zVoRR2H02rx1VCwetc8OOOkB0L5VTCqe5WvXMKqc%2FLwGOqUBrI17J0CjwtNMrSPt2zoINCfmiCbskFBhl9y2IE3ZQsK5%2F7GFBSinQI7ud7JuGab3CqPqYFH6EB85bCh0VlG3RGWcSHKG5ww0mMebga5gEdOHje28OssBIaLCsYabDdDN0pOjAlpDcS4uDliSqC2ClycutsnHib%2F6jOn%2FYeSPS9uE0PuyCNz789qdxNZXJCIEH0tEZ36DqlQLF9ljeNEzgtCA21kp&X-Amz-Signature=6a74e811f91af5ebf8c77580152a8e735f369a37b10a1a34fdacd83a01b3cabb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNT2PGVL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCm%2BfJBTsyHMIrqFhi1lKaIhKE%2FH8GlqcXZoNjxenycAiEAlhFM%2BnbxlH4Tsr3w87MwDYU8%2BeGMkrZLFFsMPYhuI5kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDd41eybCV2B24otyrcA2%2BUQA3Ozo26rowSJPD2eAbMseDW8mD%2BEIEyk7V99x296mT9Bvz44o5Yj6enSN1hXXmKbtZC2qExuhUvh%2BIwRdFgyk%2FxfT3JhLYT8N7MhwuxvCCv%2F%2FaXNWhpFDFWGAJRRyKsikfmFu2h%2BRL%2FdjGbEiWAeWl9h1UeehdAXXkVm1Hmq8eXL3fQSNIAsiqCieGieEboUshSDC%2FxsX83WV%2FehKte9ui8UfAyyZuOeSqy0sxFeZWsK3graIKXaSQ%2Bus0aDQZSKK5J4CHI3MxYMwp1fKuQXE%2Fm48kwlFYDZS7Z6mZl1WrYD6RBs377tMlRv3VBIlJAvKlZ9BsLqBkIDZrIzVzaLZ4uT5z2O4DSHrVNd0IOKjfXzgco1Lasi5rKp40HJAm4r6yglWOJwiPKkkzPulHDI9ZOczgfh09x%2BP2G%2FwsUd%2FzdJo%2BhBlm7nO%2BFdwfFbUMJME0qOADFKXcyMUHAChrLxpU7lLPS701X%2FOOoK1yG9UNsG%2FoGF9Dai5my4A1vE1Rl8mJF6pnuSQ61Jiol%2Flcs3iOyHlxcCZVqyHHhmVrEGoqoIyL3Oqj3r20TRtbm2cwjGW12jpU%2BYH%2FuQX3hl01xsZU8AgnlOXSRZNiouCr09p91qj4q4DCu9qmeMOWb%2FLwGOqUBEJE6wTvT%2BeuQGf8K7k1t6CjblH2O8TJ0s%2BlkwYXj%2FDUgavZnmPfp4EpKe0CImcwS4jbXhdkClcXVZZF5luTy9R3PgdWqmq9HLWruM9uv5YMgHwEfjTpSzovHHCRf91EiUHaf5xov%2BjRNIhGOaOZaI7s2xiHzbLa%2FBi83zVOndqh%2BDH%2FPZ086GwiWqmUY8rg6vgGzc4J6YXOsAJb9EBAFTnOV2zbf&X-Amz-Signature=0e22b64352e198fc7cbcf70d537fa706702e58235b46ae41b6cc9b1e1678a647&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNT2PGVL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCm%2BfJBTsyHMIrqFhi1lKaIhKE%2FH8GlqcXZoNjxenycAiEAlhFM%2BnbxlH4Tsr3w87MwDYU8%2BeGMkrZLFFsMPYhuI5kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDd41eybCV2B24otyrcA2%2BUQA3Ozo26rowSJPD2eAbMseDW8mD%2BEIEyk7V99x296mT9Bvz44o5Yj6enSN1hXXmKbtZC2qExuhUvh%2BIwRdFgyk%2FxfT3JhLYT8N7MhwuxvCCv%2F%2FaXNWhpFDFWGAJRRyKsikfmFu2h%2BRL%2FdjGbEiWAeWl9h1UeehdAXXkVm1Hmq8eXL3fQSNIAsiqCieGieEboUshSDC%2FxsX83WV%2FehKte9ui8UfAyyZuOeSqy0sxFeZWsK3graIKXaSQ%2Bus0aDQZSKK5J4CHI3MxYMwp1fKuQXE%2Fm48kwlFYDZS7Z6mZl1WrYD6RBs377tMlRv3VBIlJAvKlZ9BsLqBkIDZrIzVzaLZ4uT5z2O4DSHrVNd0IOKjfXzgco1Lasi5rKp40HJAm4r6yglWOJwiPKkkzPulHDI9ZOczgfh09x%2BP2G%2FwsUd%2FzdJo%2BhBlm7nO%2BFdwfFbUMJME0qOADFKXcyMUHAChrLxpU7lLPS701X%2FOOoK1yG9UNsG%2FoGF9Dai5my4A1vE1Rl8mJF6pnuSQ61Jiol%2Flcs3iOyHlxcCZVqyHHhmVrEGoqoIyL3Oqj3r20TRtbm2cwjGW12jpU%2BYH%2FuQX3hl01xsZU8AgnlOXSRZNiouCr09p91qj4q4DCu9qmeMOWb%2FLwGOqUBEJE6wTvT%2BeuQGf8K7k1t6CjblH2O8TJ0s%2BlkwYXj%2FDUgavZnmPfp4EpKe0CImcwS4jbXhdkClcXVZZF5luTy9R3PgdWqmq9HLWruM9uv5YMgHwEfjTpSzovHHCRf91EiUHaf5xov%2BjRNIhGOaOZaI7s2xiHzbLa%2FBi83zVOndqh%2BDH%2FPZ086GwiWqmUY8rg6vgGzc4J6YXOsAJb9EBAFTnOV2zbf&X-Amz-Signature=5f1331d5230f58e0d56e3570e688ffa5e54a043d6c8b9e2e76826593cbbaf680&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNT2PGVL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCm%2BfJBTsyHMIrqFhi1lKaIhKE%2FH8GlqcXZoNjxenycAiEAlhFM%2BnbxlH4Tsr3w87MwDYU8%2BeGMkrZLFFsMPYhuI5kqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDd41eybCV2B24otyrcA2%2BUQA3Ozo26rowSJPD2eAbMseDW8mD%2BEIEyk7V99x296mT9Bvz44o5Yj6enSN1hXXmKbtZC2qExuhUvh%2BIwRdFgyk%2FxfT3JhLYT8N7MhwuxvCCv%2F%2FaXNWhpFDFWGAJRRyKsikfmFu2h%2BRL%2FdjGbEiWAeWl9h1UeehdAXXkVm1Hmq8eXL3fQSNIAsiqCieGieEboUshSDC%2FxsX83WV%2FehKte9ui8UfAyyZuOeSqy0sxFeZWsK3graIKXaSQ%2Bus0aDQZSKK5J4CHI3MxYMwp1fKuQXE%2Fm48kwlFYDZS7Z6mZl1WrYD6RBs377tMlRv3VBIlJAvKlZ9BsLqBkIDZrIzVzaLZ4uT5z2O4DSHrVNd0IOKjfXzgco1Lasi5rKp40HJAm4r6yglWOJwiPKkkzPulHDI9ZOczgfh09x%2BP2G%2FwsUd%2FzdJo%2BhBlm7nO%2BFdwfFbUMJME0qOADFKXcyMUHAChrLxpU7lLPS701X%2FOOoK1yG9UNsG%2FoGF9Dai5my4A1vE1Rl8mJF6pnuSQ61Jiol%2Flcs3iOyHlxcCZVqyHHhmVrEGoqoIyL3Oqj3r20TRtbm2cwjGW12jpU%2BYH%2FuQX3hl01xsZU8AgnlOXSRZNiouCr09p91qj4q4DCu9qmeMOWb%2FLwGOqUBEJE6wTvT%2BeuQGf8K7k1t6CjblH2O8TJ0s%2BlkwYXj%2FDUgavZnmPfp4EpKe0CImcwS4jbXhdkClcXVZZF5luTy9R3PgdWqmq9HLWruM9uv5YMgHwEfjTpSzovHHCRf91EiUHaf5xov%2BjRNIhGOaOZaI7s2xiHzbLa%2FBi83zVOndqh%2BDH%2FPZ086GwiWqmUY8rg6vgGzc4J6YXOsAJb9EBAFTnOV2zbf&X-Amz-Signature=0a03b9bc5f84979fa4b626a01f4d3e537c1b5978b7c747311bbd80e4123f36f7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667D7XY3YV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDG53YYukD%2B01fj5h%2BLS%2BQmVgFSI1HHkNFZ7vYfeVhTdQIhAKffEA6H1OVSmiwfFymWBunVtXV3McSxbmu%2B03KQnTUcKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgytT3YFwPTu3b90C80q3AO%2FhEPDuPwfNJ5sDcxKCIon%2FicTaM8jRl%2FmKtyO6J8v6mXEhYkYVbCFe0vsdvAeNaixQmUNMA%2B8TRW6XwMKPOBRsENsQL5wVlNMJIylWXoI7QFZAWjG2EneQo6rQTOOe9hgVhh6jmsjB75G8fFqVUvi5LBNlGvT1lG2nn7RTZTsNScNLs1YDQHOk81YnjJ269nZZjBhKw9OgpVg07%2FIXNqSU%2BTlOdKLCrOVKjEmH3csKz0GIBH3rmXH%2B%2B%2BwquxfZtYQ4gszLWBLlc2qerAkVLmHxanBk7H0NE%2FNgl6Dp2NNOGj9y1t4O2DjaV%2Bxb7rtoAorPynwBnKoLVlowM9Cm3jJ0S7IuVU2nq%2Fp6nzAyq4dMJvDxr0EkSnbt7%2BdwJ%2FenKhKtqW7mYaO%2FCuA%2BTTnlxsFJXmsYUvIHcBTgjC2sfEdboo%2BwbSRDo%2FRjgbitSgHKfKUHiE%2BeVfXG8E3PfEqxd%2FnpgtYO5VocU2q%2Bj2BvW7EUpb%2FIuIN5M00q93DGUukQtvMTXGejNwuexXeOr991xAYDbhWOt7wecEJGivUjFWQ%2FblLLIsCIbPT13cUps3nS4g5uHco3xyQn3UWKSwnkCzxWMZnbG8%2B2sT9E83jm6jo7rEHnah9STfeIpq5hTDum%2Fy8BjqkAZXzj3DThJR%2FcVzw8hdsZ7pjDhAJL2p3Eh6R9tG4wIe0Wv628JAqJLfcqn%2BRNjzHTf59OBEPIetXepUAJoESevBgs6F99Rcsl%2FSQ43fdP5ffbo480YE1t1RbkJhqM%2F%2FwNeheszi%2BsvskKYTOTG83y5TTujpwFmHhjHAlgA6c35aaL3r0Qa5iwJMCG64ICmWMhzCYpGsr2DhwrOAC07KOcnD6J4vT&X-Amz-Signature=39cf369fb305a726e0af264c0eafc1350a01c49adaa55f5717167add89e5121d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXUBOINS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiGLMVqBSsGzNNPaFZGPha3QFiSSILeLJIJNlgRBixcQIgD%2FQbStqgqmnOtHwiNWAenl5gPYFXXPuLYVdokEVPM1UqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPVvroXV1jOh7qHYbyrcA51f28gCHMlin7dzh%2BbbK80atEnnDu9qZbhPXWns%2FkhvHV9vTkFzJNoixD%2B9%2BzTHcxlzDQjAfFR3yt2eStRm7Qnygu1irkQ594DrQ%2Fyrk05sp%2FpnqmIMlQ0PtEEIFGGcOq1S4mpav9OYYiIBlzpaWeHsnHF5A%2FDH%2FsAipSqX%2B0MqDEK9H1xlEgy3tYR1yimhqs49up5feEnvNOSk9PFEzc6RHt3cO6RuFop9kGzPOI2sMMwwTSbXTlR3TJy3KYMMkiTaOSXDxcyGg5eoWtUQD05U1J%2BSomQgkabjBAgZfeUDT3%2F0iD9BJx74ixYEETR3mCkOe9t05HmsMmQpRQdQDIcJaUa7%2Fgi1usR0zfSKn%2FITRIWSpXIJdYkfuoSuUwZadAvl4wy3PnPGyhILGu6t%2F9qApRBdMN65eqwkgoQmNn4B3FfFjS930M9J8Fsp8qY7aJ7NYGzMWI2NZCTZc3BxF0oj9ghh1Wa%2BPgJMrUrXdgTjQvQ2S1cTc9ihI%2F%2BlMUkjhQ67V2zw7VvSgatyHASUElaztac35jb1EvjeqEXGeWwG2vs42a%2FeFckkFb8%2Bg3GpzktU0s%2FZhpTkF2j%2BkommevcaYlIv4OSyn5tIpn3W9XqEY4EDtbGqrsyNODz7MKGc%2FLwGOqUBvgyBAWnhPZ5383eXffGD8mdqRJfgr8uC27HSJq7MC2XpmMgVEwO65p0Lww3YdSgjxw1d94hEiUqmV0JgWSjEH5qlq6w79uWfp4PtooZJHW49AIDwQyaCRLjWgVN6xckKMAXZvoekAMU2g1pJYkQ50Sj0IjdvPGudKe%2FqmZBFQWMlG6kgcl7mvSHwyuoQ09p9xuITGFrUo8dau6FRahwNX23AyEJe&X-Amz-Signature=78f9fd58525ace159d6f72d97cd11b55b0427d63ced9a7e5ccb2f1e7dc89758c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSGBKC4U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIE0F4OMZWQIyUBk8Q0DfIXMr%2BNhYA7TkrBYdUTSEmSHaAh8bYQH8kIdzdHb3wsS5eSbi0PByjoRJlY%2FUZhb5ZtqEKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6Uo0wmweqwTtdKzwq3AMY1k%2BS%2FdcgakjppWp4BrmW8miXwnKRuYQ9hQVx3V5IWSsMuizLu8%2BuqMdbs4W8mBz1Yz6t2hhnqYUxig0UY002sAYD245wFkiEMDMCJdgaShcEQJBdAIsiBFsbTBJYtTuVCmKYAWXaqV1aUnjJf47chvuFMea5XTrhJuwY09KzdluQS7cDK9HCa2NJGymfXEoRHYoUhGgshC24UMIIxjGdbi3BGIRoU7f7Xq8qjqSpZPFYSrXzPrEk8zi%2B%2FjZq%2FJNESknPLbPLQp9eI2BQbnKe62Ovrw1ExyvHHv%2Fuc9ZsGKIrh4hyXzK9GESsOAF2l3xxwZ0vqCpu3bW8U%2F11xWZjeri5Kl%2FxIp%2BnLmPVZROpSpzaqO5jALzZ8NJ0KL75tfGIr6CzYDrvrCXvfmxGTKh8dusv0n%2F0sZyBGkexd42l%2BXVPXBJ4VFa1tG7R2DsRNFnzeVXZu36ECAkRzL4C6eERgLJ4qo8Z9w%2Fb2HHlfJk0Owc9DUAw%2B6GNYXvRIs994RVdYutDjBXGsibJ6TyQLr6dxEvS1Rm3rnPTdBnb1c0xebhdSnDBejJ1EiUtmbrASd64vjsKETg9K6LiMACqZfmX6SILOhvnBLu4Sx9fPLLpfqKT6T2gR%2BXhiwatmzD3m%2Fy8BjqnATvZwfeZbwTFdB27nTsfwqOWtY%2BxV%2BWKiDwxyIL0AKPrZr39rj28T3rz0Tjx2wDwbhHmyng%2Fu73Lb%2FLdvEvwJ4wZ2Xsi%2BLQb94ymLUV5kP4B4BoVyl75HgJV1Wk4j%2Bhd55Z1ZNz4S5usQIDAp%2BUTZC0cL4pIhFadmTYnNz6E9EXIOZTzndF%2BJ6xM5YzQdhnrlMVy%2FuFrAL1%2BqoXYxaFHzWMXxe9%2F8WA1&X-Amz-Signature=0c79b755b59899c67413e9735d6585d95886f4e039c1c2a04d1300b4dc5b48cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7UVPFPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDVmvCmkCa2j1l%2ByIBsR68zIZ48hI4D72jox%2BCIs2ELtAiEArpQFlC1bRGQWKQj2p0JOJ6%2BEYdQontLu6LI4OxtyhDEqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1Bb%2FOjH2svIfhJeyrcAwzlgVrA5dJSvsZnWd0ooWnYEI7RLN7%2FpaJ0WGff1odPYT6Z3tM%2Fs%2BH1XxYj1aRJYCcRu7uEs7zct4oapdo37pJXQI0Z4PID0tWTibSHf%2FGsKepWrg4lZ5NIMxjzH2e0EeX0Gh17oX%2BcCiunYFrv5mb4az%2BiMVYgLPskNkAeCk46iHUhKMdyfN8XJZnAZgVEL59OqpSEE4CJ1XdBvQdKKi0WTwWijsc1kUuiQnH7vtXQnqYVVc1zGX6gT9AtSjPU4Rf50cyRS8nSplhGkKF%2BB8WVh5tL87%2FHudhP9%2FQPCit%2FI6jzw59uahQ88u82Nw6tALNAY7lA5T9ITXYdPda1BfjmloYZv%2BffSGb%2FMe9V24fBSCHYNVFT7T1WpWZXUlGZ3iimxd58VCYMITkYafhOiyr9hiQhQKiyVLH71%2BQ5RYX6gGvdmdkH4%2Fod9hbYV0BeQ8TPau5oQTw%2FSf33YfBP%2BvaPBAYxizYfm9RKfLgCfT2ZmL9e3FVrTkE2OIF7ojlho%2BYeixBMPwUMVkZzsrLd%2BfXe41s%2FndIFMLiXAdfNhKxceBUIy6wMuoqWaGVIcCekp3%2FigNU7l59er4yKixrUG8oXsJ8MGy3BdsSzd9pkK2WC4vVtUjfzNNSjUJizMNac%2FLwGOqUBKc8o4M9hPvd3Qr51w1wfYVzBdlD5Hybfj9zNuogpsIsvWKsLIdSEeioiMj22TpBFO2eT5Ln8VCVxOmM6gl9Xml%2FgXyRPdBj5C0Dqiy3S58ZMGqpvZliv6HGPyrBeO%2FGC%2BCJOCLXZX8juu73LpYwMWLPI00n%2B09YZ19rLbcb69%2FbqM5CWpa1SkQqad%2FJtz3zw81YcrOzR94PGVuhhM6tmNEcYSTbF&X-Amz-Signature=b6df5318b367d1d016e82806c60d3ebc76630c91598f9bd7543c8799325434f8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7UVPFPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDVmvCmkCa2j1l%2ByIBsR68zIZ48hI4D72jox%2BCIs2ELtAiEArpQFlC1bRGQWKQj2p0JOJ6%2BEYdQontLu6LI4OxtyhDEqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1Bb%2FOjH2svIfhJeyrcAwzlgVrA5dJSvsZnWd0ooWnYEI7RLN7%2FpaJ0WGff1odPYT6Z3tM%2Fs%2BH1XxYj1aRJYCcRu7uEs7zct4oapdo37pJXQI0Z4PID0tWTibSHf%2FGsKepWrg4lZ5NIMxjzH2e0EeX0Gh17oX%2BcCiunYFrv5mb4az%2BiMVYgLPskNkAeCk46iHUhKMdyfN8XJZnAZgVEL59OqpSEE4CJ1XdBvQdKKi0WTwWijsc1kUuiQnH7vtXQnqYVVc1zGX6gT9AtSjPU4Rf50cyRS8nSplhGkKF%2BB8WVh5tL87%2FHudhP9%2FQPCit%2FI6jzw59uahQ88u82Nw6tALNAY7lA5T9ITXYdPda1BfjmloYZv%2BffSGb%2FMe9V24fBSCHYNVFT7T1WpWZXUlGZ3iimxd58VCYMITkYafhOiyr9hiQhQKiyVLH71%2BQ5RYX6gGvdmdkH4%2Fod9hbYV0BeQ8TPau5oQTw%2FSf33YfBP%2BvaPBAYxizYfm9RKfLgCfT2ZmL9e3FVrTkE2OIF7ojlho%2BYeixBMPwUMVkZzsrLd%2BfXe41s%2FndIFMLiXAdfNhKxceBUIy6wMuoqWaGVIcCekp3%2FigNU7l59er4yKixrUG8oXsJ8MGy3BdsSzd9pkK2WC4vVtUjfzNNSjUJizMNac%2FLwGOqUBKc8o4M9hPvd3Qr51w1wfYVzBdlD5Hybfj9zNuogpsIsvWKsLIdSEeioiMj22TpBFO2eT5Ln8VCVxOmM6gl9Xml%2FgXyRPdBj5C0Dqiy3S58ZMGqpvZliv6HGPyrBeO%2FGC%2BCJOCLXZX8juu73LpYwMWLPI00n%2B09YZ19rLbcb69%2FbqM5CWpa1SkQqad%2FJtz3zw81YcrOzR94PGVuhhM6tmNEcYSTbF&X-Amz-Signature=a6492938e449ada97e079613580a88f05f6759f7f652d3d948486559ecc076e4&X-Amz-SignedHeaders=host&x-id=GetObject)

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
