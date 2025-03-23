

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z64LERKL%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDiaQpgmL2Lz4NwSe8UsHFTlwmMAJzvwpwCpupHUnulSwIgHjsW2h5yWkd2N8GoUq1dLEe32WL2uPfO8y3FpaXOXG8qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCpSCrJIqFMdVCbE%2FCrcAy7Gjb6zX6OtGoTB6s4keMwqaYiN3J1pK2m0JvRra8mhLuhvY3X79Zw8MJpPgx2YCFv5fnefoH7NlspaP1UhU0U%2BIesQFW%2FSeZ18oTocS%2F3RHTRTQNreBz7d4Es6JrVPIJolZaH2UY8JPN7XuDjcbZwsXiq%2FPvHlQjHP%2B0DHCWhtiv20sLNVXUk3jhsCN5iVPh0CZt3d7P2JcIZXvPUgBJcI1FpFncR2PFn5JpFD8mWNAoqoIQsGFoQDen0X%2BYqS9uUyKDqYLX7nekVTjLQWfFlR4wfCIktchk4txyjugBVdSdI%2BqVErpKv41rNXPfpsUX4u3r5pInLCcEUzlhJxNFihzElkEMRmp2pDdj%2B3qUW0YJSZUcDaRZqD9X3ji%2FeRoiHL7%2B%2B3cEsscRfqCvZjzFeRdi%2FjVuBTXY8F7huQ5pE%2BWvhN1BkRuMvdjGJl95GCfGgA0sVNnSOAEOkEWLnR%2Bxav5tFgCa%2BPsDRn6mi%2Ff9tKMYt0%2BlGHrGLMPwWPwioUNdsPLn6J8SzHwx5C2pFeYYNtaa7BdgOWmEJ3DLZhcLPDFL0hLCrq%2FwPO%2F0vZM8tjdmzt4%2BdikirWkfBonHHA2Y1456P8m0Gw9UBE9xV1go35RhlSBXvuopRf2666MI%2B1%2FL4GOqUB1WYCV3BBO5v3Ld4DGKAxqWwF8ATbhc%2FtmAHJCTh0Ox5BpUOmukA901cBBhiv%2Bm2VNvvLPA%2FNSPMSJ%2FdAfx%2BPAiMf4Sa%2Bvw0n3vn%2BFOC4C94H%2FozP%2BpfMRG6yAqvARZPxGDBfRwsl8W71R1C99fsdVdSPa6nLa2etlWARdjR9l71pGEFQd8XCYlcNEAhj6ahE3CSVix9KEU%2BfLbVDtcXbUVoNwjEQ&X-Amz-Signature=5fe750553fe85fa88e035a7084c79e4c2a9c1d4824e0c9bc34479866d7ba80a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z64LERKL%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDiaQpgmL2Lz4NwSe8UsHFTlwmMAJzvwpwCpupHUnulSwIgHjsW2h5yWkd2N8GoUq1dLEe32WL2uPfO8y3FpaXOXG8qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCpSCrJIqFMdVCbE%2FCrcAy7Gjb6zX6OtGoTB6s4keMwqaYiN3J1pK2m0JvRra8mhLuhvY3X79Zw8MJpPgx2YCFv5fnefoH7NlspaP1UhU0U%2BIesQFW%2FSeZ18oTocS%2F3RHTRTQNreBz7d4Es6JrVPIJolZaH2UY8JPN7XuDjcbZwsXiq%2FPvHlQjHP%2B0DHCWhtiv20sLNVXUk3jhsCN5iVPh0CZt3d7P2JcIZXvPUgBJcI1FpFncR2PFn5JpFD8mWNAoqoIQsGFoQDen0X%2BYqS9uUyKDqYLX7nekVTjLQWfFlR4wfCIktchk4txyjugBVdSdI%2BqVErpKv41rNXPfpsUX4u3r5pInLCcEUzlhJxNFihzElkEMRmp2pDdj%2B3qUW0YJSZUcDaRZqD9X3ji%2FeRoiHL7%2B%2B3cEsscRfqCvZjzFeRdi%2FjVuBTXY8F7huQ5pE%2BWvhN1BkRuMvdjGJl95GCfGgA0sVNnSOAEOkEWLnR%2Bxav5tFgCa%2BPsDRn6mi%2Ff9tKMYt0%2BlGHrGLMPwWPwioUNdsPLn6J8SzHwx5C2pFeYYNtaa7BdgOWmEJ3DLZhcLPDFL0hLCrq%2FwPO%2F0vZM8tjdmzt4%2BdikirWkfBonHHA2Y1456P8m0Gw9UBE9xV1go35RhlSBXvuopRf2666MI%2B1%2FL4GOqUB1WYCV3BBO5v3Ld4DGKAxqWwF8ATbhc%2FtmAHJCTh0Ox5BpUOmukA901cBBhiv%2Bm2VNvvLPA%2FNSPMSJ%2FdAfx%2BPAiMf4Sa%2Bvw0n3vn%2BFOC4C94H%2FozP%2BpfMRG6yAqvARZPxGDBfRwsl8W71R1C99fsdVdSPa6nLa2etlWARdjR9l71pGEFQd8XCYlcNEAhj6ahE3CSVix9KEU%2BfLbVDtcXbUVoNwjEQ&X-Amz-Signature=2b54272bb94f06f86c1f4b490b6a7392828469120766b132b34dc3b33fb6609d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z64LERKL%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDiaQpgmL2Lz4NwSe8UsHFTlwmMAJzvwpwCpupHUnulSwIgHjsW2h5yWkd2N8GoUq1dLEe32WL2uPfO8y3FpaXOXG8qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCpSCrJIqFMdVCbE%2FCrcAy7Gjb6zX6OtGoTB6s4keMwqaYiN3J1pK2m0JvRra8mhLuhvY3X79Zw8MJpPgx2YCFv5fnefoH7NlspaP1UhU0U%2BIesQFW%2FSeZ18oTocS%2F3RHTRTQNreBz7d4Es6JrVPIJolZaH2UY8JPN7XuDjcbZwsXiq%2FPvHlQjHP%2B0DHCWhtiv20sLNVXUk3jhsCN5iVPh0CZt3d7P2JcIZXvPUgBJcI1FpFncR2PFn5JpFD8mWNAoqoIQsGFoQDen0X%2BYqS9uUyKDqYLX7nekVTjLQWfFlR4wfCIktchk4txyjugBVdSdI%2BqVErpKv41rNXPfpsUX4u3r5pInLCcEUzlhJxNFihzElkEMRmp2pDdj%2B3qUW0YJSZUcDaRZqD9X3ji%2FeRoiHL7%2B%2B3cEsscRfqCvZjzFeRdi%2FjVuBTXY8F7huQ5pE%2BWvhN1BkRuMvdjGJl95GCfGgA0sVNnSOAEOkEWLnR%2Bxav5tFgCa%2BPsDRn6mi%2Ff9tKMYt0%2BlGHrGLMPwWPwioUNdsPLn6J8SzHwx5C2pFeYYNtaa7BdgOWmEJ3DLZhcLPDFL0hLCrq%2FwPO%2F0vZM8tjdmzt4%2BdikirWkfBonHHA2Y1456P8m0Gw9UBE9xV1go35RhlSBXvuopRf2666MI%2B1%2FL4GOqUB1WYCV3BBO5v3Ld4DGKAxqWwF8ATbhc%2FtmAHJCTh0Ox5BpUOmukA901cBBhiv%2Bm2VNvvLPA%2FNSPMSJ%2FdAfx%2BPAiMf4Sa%2Bvw0n3vn%2BFOC4C94H%2FozP%2BpfMRG6yAqvARZPxGDBfRwsl8W71R1C99fsdVdSPa6nLa2etlWARdjR9l71pGEFQd8XCYlcNEAhj6ahE3CSVix9KEU%2BfLbVDtcXbUVoNwjEQ&X-Amz-Signature=262f97e3d15fdc6f010d632608b39925ef5e9ce735b45f23a98fb6bb40cf1dff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VHVP7SA%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIEALo%2FxdMhY6mkJKk%2FR9XgC29MLu3lAU2TwTheAMEAvwAiBNE5A7MHtSqTpXFej4BraEqCcmw21%2FOQhh%2FDMMXAInGCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX2g9S%2BDhov2IdgETKtwDHcxG8IUkG9FX2dIZVRutKey6q80yHdvFhWImnXMxfPORwYgURniEqLmETGNCHTBcFAGiwWY%2Beoi6kUE9yebYsspXZ%2Bq0Rv2G8hn%2FUhTB5CqY3eoU0vZBMafg4PAy0eClpTTYPG7vD41WxZkOERIBeNRejzNuGyynM9mUsEcowYyV6Ho7DkdiAle5SRwGif1tlp0bRLrr1pfB46TA%2FQyETQ5e69WqPUgXOsekDKcshM8AgHJUwJQIk5yQ%2BwnsWRKwPkXv%2FB2ari2udeEamm7HlH9hcZZ9gg2MaJrCPxc2spx83NlEy2SewPoRTgUDj5Ud%2FaZIix%2ByK9S3Hsvc3ON6%2BIkGcTJ1T%2Badn9Aa%2FUhuONoIGC8KuZ25%2BuaIx%2Fx%2F8od7orNCJwlu%2B6nT%2Bmcxe32OUto9EFwGmQ19hBKHPmiSlAwt1nfr9swQB6uzIO9CVyp770NYMn11%2BMog%2BDCM0O%2BA4cVBv7hxFAdd19o4d3OO2JKxMuveWGQSdgkG2jc4UblwGxeSQtyhePTmg0fbGI96WtmeVBbG0LorXtywReYLz5fBm%2BCuH8j%2B9cXXu0Qqts8iQmtchC8YPEMVGRCjzpJ1BtlMR90mQgxxeiCkROf5Ep0T4PPiHQ%2B23DnZYVcws4L9vgY6pgEQvA8JZL8S%2Bl%2F766pplGFIqE63cGXw5y7zmzhFMdpl5N2Xq0FpFDgCnE74piK5YBQ%2FN6YPyVK5m68faan0a2u%2Fa9TVVzmLQYVK%2Fb8M6ybi9%2FVBhwtYhbcXazKSzLoYG0NFRPbK1b678VridF%2F04da%2FkWA3FEM2928Z58oY7WOO5EwC%2FXB9aWq8fyJZuFBjMYLegMV99M69M%2Bh5nW0k6kqkn4QENovk&X-Amz-Signature=64b3df769f687061976cf94d3add6f9de38bcbe74f42b4e8c51bc564e1a6595e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VHVP7SA%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIEALo%2FxdMhY6mkJKk%2FR9XgC29MLu3lAU2TwTheAMEAvwAiBNE5A7MHtSqTpXFej4BraEqCcmw21%2FOQhh%2FDMMXAInGCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX2g9S%2BDhov2IdgETKtwDHcxG8IUkG9FX2dIZVRutKey6q80yHdvFhWImnXMxfPORwYgURniEqLmETGNCHTBcFAGiwWY%2Beoi6kUE9yebYsspXZ%2Bq0Rv2G8hn%2FUhTB5CqY3eoU0vZBMafg4PAy0eClpTTYPG7vD41WxZkOERIBeNRejzNuGyynM9mUsEcowYyV6Ho7DkdiAle5SRwGif1tlp0bRLrr1pfB46TA%2FQyETQ5e69WqPUgXOsekDKcshM8AgHJUwJQIk5yQ%2BwnsWRKwPkXv%2FB2ari2udeEamm7HlH9hcZZ9gg2MaJrCPxc2spx83NlEy2SewPoRTgUDj5Ud%2FaZIix%2ByK9S3Hsvc3ON6%2BIkGcTJ1T%2Badn9Aa%2FUhuONoIGC8KuZ25%2BuaIx%2Fx%2F8od7orNCJwlu%2B6nT%2Bmcxe32OUto9EFwGmQ19hBKHPmiSlAwt1nfr9swQB6uzIO9CVyp770NYMn11%2BMog%2BDCM0O%2BA4cVBv7hxFAdd19o4d3OO2JKxMuveWGQSdgkG2jc4UblwGxeSQtyhePTmg0fbGI96WtmeVBbG0LorXtywReYLz5fBm%2BCuH8j%2B9cXXu0Qqts8iQmtchC8YPEMVGRCjzpJ1BtlMR90mQgxxeiCkROf5Ep0T4PPiHQ%2B23DnZYVcws4L9vgY6pgEQvA8JZL8S%2Bl%2F766pplGFIqE63cGXw5y7zmzhFMdpl5N2Xq0FpFDgCnE74piK5YBQ%2FN6YPyVK5m68faan0a2u%2Fa9TVVzmLQYVK%2Fb8M6ybi9%2FVBhwtYhbcXazKSzLoYG0NFRPbK1b678VridF%2F04da%2FkWA3FEM2928Z58oY7WOO5EwC%2FXB9aWq8fyJZuFBjMYLegMV99M69M%2Bh5nW0k6kqkn4QENovk&X-Amz-Signature=ed3992c36bf02c60bb82bd35bd46f20652a4eaa2d74a0948b1804fbff903c927&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VHVP7SA%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIEALo%2FxdMhY6mkJKk%2FR9XgC29MLu3lAU2TwTheAMEAvwAiBNE5A7MHtSqTpXFej4BraEqCcmw21%2FOQhh%2FDMMXAInGCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX2g9S%2BDhov2IdgETKtwDHcxG8IUkG9FX2dIZVRutKey6q80yHdvFhWImnXMxfPORwYgURniEqLmETGNCHTBcFAGiwWY%2Beoi6kUE9yebYsspXZ%2Bq0Rv2G8hn%2FUhTB5CqY3eoU0vZBMafg4PAy0eClpTTYPG7vD41WxZkOERIBeNRejzNuGyynM9mUsEcowYyV6Ho7DkdiAle5SRwGif1tlp0bRLrr1pfB46TA%2FQyETQ5e69WqPUgXOsekDKcshM8AgHJUwJQIk5yQ%2BwnsWRKwPkXv%2FB2ari2udeEamm7HlH9hcZZ9gg2MaJrCPxc2spx83NlEy2SewPoRTgUDj5Ud%2FaZIix%2ByK9S3Hsvc3ON6%2BIkGcTJ1T%2Badn9Aa%2FUhuONoIGC8KuZ25%2BuaIx%2Fx%2F8od7orNCJwlu%2B6nT%2Bmcxe32OUto9EFwGmQ19hBKHPmiSlAwt1nfr9swQB6uzIO9CVyp770NYMn11%2BMog%2BDCM0O%2BA4cVBv7hxFAdd19o4d3OO2JKxMuveWGQSdgkG2jc4UblwGxeSQtyhePTmg0fbGI96WtmeVBbG0LorXtywReYLz5fBm%2BCuH8j%2B9cXXu0Qqts8iQmtchC8YPEMVGRCjzpJ1BtlMR90mQgxxeiCkROf5Ep0T4PPiHQ%2B23DnZYVcws4L9vgY6pgEQvA8JZL8S%2Bl%2F766pplGFIqE63cGXw5y7zmzhFMdpl5N2Xq0FpFDgCnE74piK5YBQ%2FN6YPyVK5m68faan0a2u%2Fa9TVVzmLQYVK%2Fb8M6ybi9%2FVBhwtYhbcXazKSzLoYG0NFRPbK1b678VridF%2F04da%2FkWA3FEM2928Z58oY7WOO5EwC%2FXB9aWq8fyJZuFBjMYLegMV99M69M%2Bh5nW0k6kqkn4QENovk&X-Amz-Signature=1ad32ad9cf183b7000856c39199e3411fbaee00d52db0f576744643d4d76418e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VHVP7SA%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIEALo%2FxdMhY6mkJKk%2FR9XgC29MLu3lAU2TwTheAMEAvwAiBNE5A7MHtSqTpXFej4BraEqCcmw21%2FOQhh%2FDMMXAInGCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX2g9S%2BDhov2IdgETKtwDHcxG8IUkG9FX2dIZVRutKey6q80yHdvFhWImnXMxfPORwYgURniEqLmETGNCHTBcFAGiwWY%2Beoi6kUE9yebYsspXZ%2Bq0Rv2G8hn%2FUhTB5CqY3eoU0vZBMafg4PAy0eClpTTYPG7vD41WxZkOERIBeNRejzNuGyynM9mUsEcowYyV6Ho7DkdiAle5SRwGif1tlp0bRLrr1pfB46TA%2FQyETQ5e69WqPUgXOsekDKcshM8AgHJUwJQIk5yQ%2BwnsWRKwPkXv%2FB2ari2udeEamm7HlH9hcZZ9gg2MaJrCPxc2spx83NlEy2SewPoRTgUDj5Ud%2FaZIix%2ByK9S3Hsvc3ON6%2BIkGcTJ1T%2Badn9Aa%2FUhuONoIGC8KuZ25%2BuaIx%2Fx%2F8od7orNCJwlu%2B6nT%2Bmcxe32OUto9EFwGmQ19hBKHPmiSlAwt1nfr9swQB6uzIO9CVyp770NYMn11%2BMog%2BDCM0O%2BA4cVBv7hxFAdd19o4d3OO2JKxMuveWGQSdgkG2jc4UblwGxeSQtyhePTmg0fbGI96WtmeVBbG0LorXtywReYLz5fBm%2BCuH8j%2B9cXXu0Qqts8iQmtchC8YPEMVGRCjzpJ1BtlMR90mQgxxeiCkROf5Ep0T4PPiHQ%2B23DnZYVcws4L9vgY6pgEQvA8JZL8S%2Bl%2F766pplGFIqE63cGXw5y7zmzhFMdpl5N2Xq0FpFDgCnE74piK5YBQ%2FN6YPyVK5m68faan0a2u%2Fa9TVVzmLQYVK%2Fb8M6ybi9%2FVBhwtYhbcXazKSzLoYG0NFRPbK1b678VridF%2F04da%2FkWA3FEM2928Z58oY7WOO5EwC%2FXB9aWq8fyJZuFBjMYLegMV99M69M%2Bh5nW0k6kqkn4QENovk&X-Amz-Signature=016969999fb9021c0527b64492d4c9f79193b41fcb1758a9bbccface42560e1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VHVP7SA%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIEALo%2FxdMhY6mkJKk%2FR9XgC29MLu3lAU2TwTheAMEAvwAiBNE5A7MHtSqTpXFej4BraEqCcmw21%2FOQhh%2FDMMXAInGCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX2g9S%2BDhov2IdgETKtwDHcxG8IUkG9FX2dIZVRutKey6q80yHdvFhWImnXMxfPORwYgURniEqLmETGNCHTBcFAGiwWY%2Beoi6kUE9yebYsspXZ%2Bq0Rv2G8hn%2FUhTB5CqY3eoU0vZBMafg4PAy0eClpTTYPG7vD41WxZkOERIBeNRejzNuGyynM9mUsEcowYyV6Ho7DkdiAle5SRwGif1tlp0bRLrr1pfB46TA%2FQyETQ5e69WqPUgXOsekDKcshM8AgHJUwJQIk5yQ%2BwnsWRKwPkXv%2FB2ari2udeEamm7HlH9hcZZ9gg2MaJrCPxc2spx83NlEy2SewPoRTgUDj5Ud%2FaZIix%2ByK9S3Hsvc3ON6%2BIkGcTJ1T%2Badn9Aa%2FUhuONoIGC8KuZ25%2BuaIx%2Fx%2F8od7orNCJwlu%2B6nT%2Bmcxe32OUto9EFwGmQ19hBKHPmiSlAwt1nfr9swQB6uzIO9CVyp770NYMn11%2BMog%2BDCM0O%2BA4cVBv7hxFAdd19o4d3OO2JKxMuveWGQSdgkG2jc4UblwGxeSQtyhePTmg0fbGI96WtmeVBbG0LorXtywReYLz5fBm%2BCuH8j%2B9cXXu0Qqts8iQmtchC8YPEMVGRCjzpJ1BtlMR90mQgxxeiCkROf5Ep0T4PPiHQ%2B23DnZYVcws4L9vgY6pgEQvA8JZL8S%2Bl%2F766pplGFIqE63cGXw5y7zmzhFMdpl5N2Xq0FpFDgCnE74piK5YBQ%2FN6YPyVK5m68faan0a2u%2Fa9TVVzmLQYVK%2Fb8M6ybi9%2FVBhwtYhbcXazKSzLoYG0NFRPbK1b678VridF%2F04da%2FkWA3FEM2928Z58oY7WOO5EwC%2FXB9aWq8fyJZuFBjMYLegMV99M69M%2Bh5nW0k6kqkn4QENovk&X-Amz-Signature=ec40df88e78b87a58aa506b518755377aceda42d5cbedf36b6828135607ac378&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VHVP7SA%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIEALo%2FxdMhY6mkJKk%2FR9XgC29MLu3lAU2TwTheAMEAvwAiBNE5A7MHtSqTpXFej4BraEqCcmw21%2FOQhh%2FDMMXAInGCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX2g9S%2BDhov2IdgETKtwDHcxG8IUkG9FX2dIZVRutKey6q80yHdvFhWImnXMxfPORwYgURniEqLmETGNCHTBcFAGiwWY%2Beoi6kUE9yebYsspXZ%2Bq0Rv2G8hn%2FUhTB5CqY3eoU0vZBMafg4PAy0eClpTTYPG7vD41WxZkOERIBeNRejzNuGyynM9mUsEcowYyV6Ho7DkdiAle5SRwGif1tlp0bRLrr1pfB46TA%2FQyETQ5e69WqPUgXOsekDKcshM8AgHJUwJQIk5yQ%2BwnsWRKwPkXv%2FB2ari2udeEamm7HlH9hcZZ9gg2MaJrCPxc2spx83NlEy2SewPoRTgUDj5Ud%2FaZIix%2ByK9S3Hsvc3ON6%2BIkGcTJ1T%2Badn9Aa%2FUhuONoIGC8KuZ25%2BuaIx%2Fx%2F8od7orNCJwlu%2B6nT%2Bmcxe32OUto9EFwGmQ19hBKHPmiSlAwt1nfr9swQB6uzIO9CVyp770NYMn11%2BMog%2BDCM0O%2BA4cVBv7hxFAdd19o4d3OO2JKxMuveWGQSdgkG2jc4UblwGxeSQtyhePTmg0fbGI96WtmeVBbG0LorXtywReYLz5fBm%2BCuH8j%2B9cXXu0Qqts8iQmtchC8YPEMVGRCjzpJ1BtlMR90mQgxxeiCkROf5Ep0T4PPiHQ%2B23DnZYVcws4L9vgY6pgEQvA8JZL8S%2Bl%2F766pplGFIqE63cGXw5y7zmzhFMdpl5N2Xq0FpFDgCnE74piK5YBQ%2FN6YPyVK5m68faan0a2u%2Fa9TVVzmLQYVK%2Fb8M6ybi9%2FVBhwtYhbcXazKSzLoYG0NFRPbK1b678VridF%2F04da%2FkWA3FEM2928Z58oY7WOO5EwC%2FXB9aWq8fyJZuFBjMYLegMV99M69M%2Bh5nW0k6kqkn4QENovk&X-Amz-Signature=ea9d47afa81a889fe68b0d62da4aedcc8ca6f652c517c4df5528de2e2570ee77&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675K2IJ72%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAtiDkYnvWxARC2C3quHhnXGMYhMO9GXtw9TUeZ85kmHAiAUNlZeh%2BvrtD962dye5aJPRUqvOT4hoUfbcWfQgk9IWCqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLI7IddptxyjgPcwSKtwD76Em0V3RsJhWy3uf87SEQUYc8BVoYamB1bJf0Me6EGGrAybzJpbTiXAuPTAJ%2F48avegw%2BjpZ2b8trlcwgfeWPN%2B%2FBpKIxDxXaLl6GSMdbMlgEGBnfzWPsrX29ERvBxqpyTI%2FoTsK9gAlhgf1RavIzI%2BCubmZqCHIcMJSbaSWrkU3J5ax7htfbbvXkxB97rMpMUtVLwykqG8%2FFW8ZNmypGzChAKe7zmSqFwn7tuvxtH8mzJoOb86xhxV3Eg%2BSaFzd%2B2wUtLyhYKWoeig4EfKKwQ0ce4tYDOwdxxGhClPhpQcwlsXm5GmmXJN2Ns1nVp5g2QYAyhZ3vGubwVg5Q43KQ3uotETzLpx4aiHAw%2F1dzq9fWXnJoEXqGmIZ5QL49CQ4vi1Hqhep7UH0zQp%2BpjSv%2BYrSAQLAtR0zeKMRlnlW472rvr%2BUuGx2GOwXXtJZMITYxyHFKUWUCDHhTRcg6FGxMzc9nLP%2FOZnUfUzLUPlH15YyuZv%2B1Vp2hZhUY5FKkX9wIq4hfNdvm1YnfK%2Fy2eZRfCJYKKT2zKq5rV%2BImCKNfJft033TTDgd78S3ixOuZpLr%2FBauXuBt8BsMpo9FZkav4t3FjrzIZCVJaPzQeQvLERuZwJs6oVQlPT7yi4gwz6H9vgY6pgFxSLk4UtdNxq766w2Xws0SLda9pXiEkLTqD65U2VowiI2bt8T%2FiPeYE1GbhOhlLLq4TTOWKvvfrOQLRUU3P2kq9%2FBPI4emYvIfL2aOXucRW3PuviS%2B%2FJRYaWlGmQj2C0AiqSZDedgc5M37S7GZhS9%2FXshWgr2sOhVqrS1F0TZxuOnF4cV0KsKcaQL9%2FGlMmNp25rv3otJk7eI4vMI0VNfOFwmNWsWj&X-Amz-Signature=f173b3dabb1d9145db7176e3cd116f1c205f515576a8522f84fef8cb8baf77e1&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USX2CFTM%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIEd3yzUUVNLlwWMAL28LqX4lhk8n%2FyQY1Acb79qZHXYKAiEA84YmE62eKdgdfl%2BSh7%2FR%2FdOZocCn73hrKoKn%2FKbVLAoqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXKISzr2z5whTsurSrcA1e9HuV4WWR68Pw3trktRH5y0jToJrs3wJVowr5ZpN4ZoDCzHZJBcz7nT4ANtJpsTS4huPFEMnbwLITR1KmtxBtBu4ZouZSZiqUrIvJP6ez3Te1ByPjH0BQRkZHAPHeQ1lX2J9SOw3LKkvGHhOkF5psFCT%2B2hzoNgCio4aWzIAsMbH30ZYyGH2a93rYAIkCk9e%2BQ1h8i1o%2BUPdmV26artJ5XfjReFa0OCdjZHaMB%2B2celFh8wa65PJ1u%2FoCVYJn2wx%2B7O10hsIKmSiSiZA9aTdV3dQJNuFywMCMh50iOqQwjM1%2F%2BfXCgZNmXt55vGOGvprp2K6EcBR4BMUBcOVJkvJUSRMCugN58da5AS%2BrRWk9F3I%2Bqkjjsr92zef1Tjsz3q52cC%2FgvLtDjzEbOoaOtOkaeBj3IqfSHCS9jPjq%2FI%2BOgL7FkpeEZHraEU%2F%2BgUiQEdUobh97OTBaOV5iTk4hWVkI7OiZ%2BkCljKwTuiWg0kkQZ7kI2vhiwZW0bqD%2BBR0Fvj6zmFUAUBa1UE3hsq%2Bj5WNWneO7Z1fhvg%2FS0hhB6AGbOK89xZTAevZw%2BQFL2%2BhHkDm3IJhPqwgREBJujzKr3X%2Fdfxhv0EiDh%2F1scg2eRYJZXTcPI4I%2F8AJulTlBbMIi1%2FL4GOqUBXWAlImaroeORqGOeCvp4%2FH0%2FOOgaSvRW3EXK2wbxP0L4724w%2FGERU5MP4Ib23EkLfAM%2B531bnzAEBS1rCI921VOuYpq9pN%2Bd4g%2Fmn5XH1NCkAnlryLYG780%2FYu2STRj6Zi8smf2%2BxZScw%2FtAd%2FEag3nVxpVKb0%2BEM2wUlpfEFdiyCD%2BPWhSdRtcz8Mbysv%2BVuKJxGRB%2FmIe6hLpitoVp9jy2UiWD&X-Amz-Signature=32dcede6590e3baae2feca03bfdcded22bb5bd92fef1f91c4d67d1bcd3c375f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VHVP7SA%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIEALo%2FxdMhY6mkJKk%2FR9XgC29MLu3lAU2TwTheAMEAvwAiBNE5A7MHtSqTpXFej4BraEqCcmw21%2FOQhh%2FDMMXAInGCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX2g9S%2BDhov2IdgETKtwDHcxG8IUkG9FX2dIZVRutKey6q80yHdvFhWImnXMxfPORwYgURniEqLmETGNCHTBcFAGiwWY%2Beoi6kUE9yebYsspXZ%2Bq0Rv2G8hn%2FUhTB5CqY3eoU0vZBMafg4PAy0eClpTTYPG7vD41WxZkOERIBeNRejzNuGyynM9mUsEcowYyV6Ho7DkdiAle5SRwGif1tlp0bRLrr1pfB46TA%2FQyETQ5e69WqPUgXOsekDKcshM8AgHJUwJQIk5yQ%2BwnsWRKwPkXv%2FB2ari2udeEamm7HlH9hcZZ9gg2MaJrCPxc2spx83NlEy2SewPoRTgUDj5Ud%2FaZIix%2ByK9S3Hsvc3ON6%2BIkGcTJ1T%2Badn9Aa%2FUhuONoIGC8KuZ25%2BuaIx%2Fx%2F8od7orNCJwlu%2B6nT%2Bmcxe32OUto9EFwGmQ19hBKHPmiSlAwt1nfr9swQB6uzIO9CVyp770NYMn11%2BMog%2BDCM0O%2BA4cVBv7hxFAdd19o4d3OO2JKxMuveWGQSdgkG2jc4UblwGxeSQtyhePTmg0fbGI96WtmeVBbG0LorXtywReYLz5fBm%2BCuH8j%2B9cXXu0Qqts8iQmtchC8YPEMVGRCjzpJ1BtlMR90mQgxxeiCkROf5Ep0T4PPiHQ%2B23DnZYVcws4L9vgY6pgEQvA8JZL8S%2Bl%2F766pplGFIqE63cGXw5y7zmzhFMdpl5N2Xq0FpFDgCnE74piK5YBQ%2FN6YPyVK5m68faan0a2u%2Fa9TVVzmLQYVK%2Fb8M6ybi9%2FVBhwtYhbcXazKSzLoYG0NFRPbK1b678VridF%2F04da%2FkWA3FEM2928Z58oY7WOO5EwC%2FXB9aWq8fyJZuFBjMYLegMV99M69M%2Bh5nW0k6kqkn4QENovk&X-Amz-Signature=161b6130b1c9d88201602d35100ff0b9b29bbf86a90bd634950a3165d3ac5613&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VHVP7SA%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIEALo%2FxdMhY6mkJKk%2FR9XgC29MLu3lAU2TwTheAMEAvwAiBNE5A7MHtSqTpXFej4BraEqCcmw21%2FOQhh%2FDMMXAInGCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX2g9S%2BDhov2IdgETKtwDHcxG8IUkG9FX2dIZVRutKey6q80yHdvFhWImnXMxfPORwYgURniEqLmETGNCHTBcFAGiwWY%2Beoi6kUE9yebYsspXZ%2Bq0Rv2G8hn%2FUhTB5CqY3eoU0vZBMafg4PAy0eClpTTYPG7vD41WxZkOERIBeNRejzNuGyynM9mUsEcowYyV6Ho7DkdiAle5SRwGif1tlp0bRLrr1pfB46TA%2FQyETQ5e69WqPUgXOsekDKcshM8AgHJUwJQIk5yQ%2BwnsWRKwPkXv%2FB2ari2udeEamm7HlH9hcZZ9gg2MaJrCPxc2spx83NlEy2SewPoRTgUDj5Ud%2FaZIix%2ByK9S3Hsvc3ON6%2BIkGcTJ1T%2Badn9Aa%2FUhuONoIGC8KuZ25%2BuaIx%2Fx%2F8od7orNCJwlu%2B6nT%2Bmcxe32OUto9EFwGmQ19hBKHPmiSlAwt1nfr9swQB6uzIO9CVyp770NYMn11%2BMog%2BDCM0O%2BA4cVBv7hxFAdd19o4d3OO2JKxMuveWGQSdgkG2jc4UblwGxeSQtyhePTmg0fbGI96WtmeVBbG0LorXtywReYLz5fBm%2BCuH8j%2B9cXXu0Qqts8iQmtchC8YPEMVGRCjzpJ1BtlMR90mQgxxeiCkROf5Ep0T4PPiHQ%2B23DnZYVcws4L9vgY6pgEQvA8JZL8S%2Bl%2F766pplGFIqE63cGXw5y7zmzhFMdpl5N2Xq0FpFDgCnE74piK5YBQ%2FN6YPyVK5m68faan0a2u%2Fa9TVVzmLQYVK%2Fb8M6ybi9%2FVBhwtYhbcXazKSzLoYG0NFRPbK1b678VridF%2F04da%2FkWA3FEM2928Z58oY7WOO5EwC%2FXB9aWq8fyJZuFBjMYLegMV99M69M%2Bh5nW0k6kqkn4QENovk&X-Amz-Signature=8aeeb7ac042a24ec6203b5dfb99d36024b15f1f259e9cdb7dc1aaf31f7689757&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VHVP7SA%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIEALo%2FxdMhY6mkJKk%2FR9XgC29MLu3lAU2TwTheAMEAvwAiBNE5A7MHtSqTpXFej4BraEqCcmw21%2FOQhh%2FDMMXAInGCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX2g9S%2BDhov2IdgETKtwDHcxG8IUkG9FX2dIZVRutKey6q80yHdvFhWImnXMxfPORwYgURniEqLmETGNCHTBcFAGiwWY%2Beoi6kUE9yebYsspXZ%2Bq0Rv2G8hn%2FUhTB5CqY3eoU0vZBMafg4PAy0eClpTTYPG7vD41WxZkOERIBeNRejzNuGyynM9mUsEcowYyV6Ho7DkdiAle5SRwGif1tlp0bRLrr1pfB46TA%2FQyETQ5e69WqPUgXOsekDKcshM8AgHJUwJQIk5yQ%2BwnsWRKwPkXv%2FB2ari2udeEamm7HlH9hcZZ9gg2MaJrCPxc2spx83NlEy2SewPoRTgUDj5Ud%2FaZIix%2ByK9S3Hsvc3ON6%2BIkGcTJ1T%2Badn9Aa%2FUhuONoIGC8KuZ25%2BuaIx%2Fx%2F8od7orNCJwlu%2B6nT%2Bmcxe32OUto9EFwGmQ19hBKHPmiSlAwt1nfr9swQB6uzIO9CVyp770NYMn11%2BMog%2BDCM0O%2BA4cVBv7hxFAdd19o4d3OO2JKxMuveWGQSdgkG2jc4UblwGxeSQtyhePTmg0fbGI96WtmeVBbG0LorXtywReYLz5fBm%2BCuH8j%2B9cXXu0Qqts8iQmtchC8YPEMVGRCjzpJ1BtlMR90mQgxxeiCkROf5Ep0T4PPiHQ%2B23DnZYVcws4L9vgY6pgEQvA8JZL8S%2Bl%2F766pplGFIqE63cGXw5y7zmzhFMdpl5N2Xq0FpFDgCnE74piK5YBQ%2FN6YPyVK5m68faan0a2u%2Fa9TVVzmLQYVK%2Fb8M6ybi9%2FVBhwtYhbcXazKSzLoYG0NFRPbK1b678VridF%2F04da%2FkWA3FEM2928Z58oY7WOO5EwC%2FXB9aWq8fyJZuFBjMYLegMV99M69M%2Bh5nW0k6kqkn4QENovk&X-Amz-Signature=40efab702211c2fd96b3de8d5dbb678d6cfdbfa9f18a6ff2d5bb5ebf99cb1c58&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYB2G3E%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAoKs70F7xc1F4An1dyIRTU5cl%2B61GZU%2BI0c9%2FbQBT7TAiBuyOmZK9sv4LbSGEcNcyUaUM6F9oRqj9zL1FoFx4bGcyqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdAVzw5GkOWUYEHbtKtwD63CiDibaTIsU9VbSw3IxIoBIBDSgjF1Q4skcKOI%2FBak4JIRwVHNqlsHYgd1SSfNvyNG7NSIjcyH%2BfGY4SascAOWT64mNT4qIDFRrjxsScKtbhIThQvlRchFtl5I2UBDb8cla7SXyxfdkrzBWnvoEMylI4hAOXFglR3fyPnDLSnhKr8VlqpJLm3DoY7680i4TJ91gF7KMp8H3Sv2KNkN0nQonUeS%2FHz9ONoC8%2BUCBspLTlPsCbFHrmYQnPjwAXk01haSTK6Vah4nHgs7kh%2BrseMwIpg0hGlR1YClMXg4GtF%2Fc2bmIoKaBfq0sIDtbzBYQusKYsTltSQOZhV78%2FN%2FGJA33mO9gAkq4%2FNc8NlPwdNtVO54F8qWzIKBgfiG3i5Qm0bQlorvgrUt9Aomhz2R4GW7TXu0NEOvN3dBZU9pdUhapXH7rM4s8JsJDpKmSEakJHHNBydlEcggqbcWkoT5lGRcrQGbuKkghBLeJaXzt6EX3u7CTjKtT1EqPGRQCsjKiOmc53wk9%2BCaq83ghv2DEryOqP1yd5FXOw6dhj2KAjQDdxxRgXenF%2BFocv3KiQDhDm1vpWS9dFFnwSc9SQzWA%2B5rO1tIC6F3QjmJIaiQk02ZlJCvFVgWoIdN%2FXVYw5bT8vgY6pgH6h0Db6j80KPDiz8ABYiVG2h8ojDK2t6tsZmd1y2PEeO2xbHV9P99sJTLRd6GY0Zj2x0MUS%2BYHxg%2B12Bqwg9pP9MkzD8CNPjne0xG%2Fe%2FibNnyLltbTurIKYh0M8QBgM9aUApufdtPzOE3tv%2FiQ8149SqeZ6l9t09XnI2FebPRZaiO9AZiCNDCs%2BfhQ%2Ff5eD7w9H74BihykdFEChOOx9GALCLYn%2FGKo&X-Amz-Signature=f91b1f1dfb0f38685c7b05ae553219f20a1e52851c9309248c18a2e17bc2f190&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVEXPWND%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQDeXL7nyCxzWa8GClgbSZF8Cl97jkZl%2BErJlJxYMSv58wIgU1TD6QqTus%2BKiiz4RBy95JtxXzmnLCNVV2GT7xCNGWMqiAQIyP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDYFa%2BWd1l1FwnPFWCrcA4PTXFn6Zl6Z8EpwijGNjC01zlH6Sq5oHfeb4bWMBcyH0ivjptp6HOawadtQPWcFG%2B94pAzssg4sJIEJQTADhlJAukbzV1Mv4n4Rmk%2BfcmDeBCpgLM8YeqFYbe66OpUd2fpxMtd7nL1JTNofJhKfgUjZ9BMEcu0%2Fv%2BKDPQWDodOH9WGXcix%2BsFBVuTxV3Yfeah1mGm%2FVVoojYurv2voixmDOzrDGsvbWsmsIwYXhXzGjO4SNOXicW64qcj5Z152sz2Y87FOSPe8HNJmzkp8ae7V3jpL9P1gXtzntd%2FydwU4RktqcWeJGdSEXdwwO4JabeKzfAj7fB8lc6ht8IHjm6we%2FB5s7sY0%2BDhhqDFQ1F8u1eqxGVdQwMTFw4Kt0LKJQFaM2qvEdSBXJ6YW6m2%2FpODG4gIW0wzWASLDOmOY5XdwzIMI8zzAlITtwQm8MtzzGe5laWsohzR2%2F2bd0ftOvgqMZ2Wq3hQ6Iv4wYyIrfNRBcajBAmZeXg5oXNfZAL3CjPas9%2BkTHdoEHyGF6LHlPn0pqk5iYV%2Bm%2FXLrAh7Ji05eNPJbpOtHrHw1E9MjVRQJSVWE0VlJ%2F%2FeJyebP6B7qEDlnH7Qg4mFpV2O4ylm0fkWIS73CPNo9dlUSZ9ykrMO%2Fz%2FL4GOqUBASlHmnUac0UfW3EXn1%2FNy1fmck8rsSn0GbYvhWOJjyqtZTrAHsxYfU5W7gNnMvUbSt4%2BB3n1ar70Hp3KRfx3k%2FUlG0horcNdc%2BJe9%2BEugE3NjbFLXo5LcKFWiBfcZiMsk8us8RdG1E%2BKhU9uPt2eqRiMsiXsSQ%2F%2BME8n0oXVh1KaOjH02ns1h07yV2bniCm6n6lReHGKFE%2BHxlNAI0EPm5c2aGCO&X-Amz-Signature=a6c7fbd6d4fae5b5b5ac3889cc1ab5b8f98e35470a06c587554247d096efb4e5&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UXQIRYN%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIC%2BV%2BIDQs4aRM%2FDshozkHDBnWi5xT7EKJW6KordxfPxKAiEAyHEsOXuBVWczsn6b6vsKDGlfakuq2FBjCVQYqPBBG5gqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLjune3N9TcDyh96XircA58yTD9dbOL4WKcnGxnvsEFdi7N1HRro%2FE3n5Y5MiUCP8KNskhFxAw27i%2B9RqdyBULX9ayV%2FTA9KVhov1IPt7d28k%2BInDDQsoTKFPORARp22%2BMMG54xyHkct60ISfuijYT5QUSZARuFyJg93a00EP2OABFP96VLkq9bcV4HqpkxCDtc7PdJ5%2BWhWUsnMnRQNW5x9PesKgN2ukef77NQ2gCO7EYyKh7qql%2Fa032Yu%2FeaO6bSxug6nBSZVkEgIqkP9s8gfmm2sIGGy0Fd2cs5dcNktDgHfA2uqDW%2FFG79FNT0BmBO%2F05r%2FNOLqvrRirtpotePb%2BiKz7vYTspd1YvOI%2FFWiJTW7muzZcqqzt03lBeht3un%2FeZt9R6F0wc1aBcI2omf%2BHOa5S%2BDMXPmaWSZSCQcLOMUJasMd6B3pvSGCI2KV4TKtnrICvZJc6KsRYnzP8jrJ2I15OWpFRwlP7jqK3CXDjzSnl8tIqrmU%2F5P%2FJOdBluXS1lJoXKIQ%2FtpU%2BgiJ9NJiMCbNKKLb4tIaV7oEHkTREhJyhM6rz2POqQzGPFRlta7kFNKhMLzD%2Buoqb5H8e68JxSyc414Ke5H9JtTtN1Mo2guReimVIe86Pr%2FIyVvf4StWCTkC3kpLCVFMMI%2B1%2FL4GOqUBG7xCipuFhjdAZelokAac95ULDXkaVOgJ6%2BIWhImgVR61ZK2oStnyJI7gXxmTlNJqIKjVeDFNIYF5FNq3xsdo%2FyiHyF7FW64dYEnjLsd%2F5HrdVMKtAyisI6qzc58CHf0B6FGYrqjTiNHnXIm4KRKNdxQRaBMY5tTQjKnmaRpcAu9AS4pfdd%2FXfKD4vAXgyqaiM6eH0J1ah42XHn5EI%2FZc4qFhipje&X-Amz-Signature=3dea9294b61186e260856e370d64151d3ff811a15f00728672302f04fee2bfee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YJXBUQY%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIDE3qzjh9H%2F7dxaNi4xbyEdkUlur6zz9bsw2bONOCLCfAiEA9mIr%2FTozlt9zfrkqkSPEQKl%2BEQpWtXax%2FvofJfBj44MqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGZFYRkDQQWheH9hnircAyTLvkWM4Joh0KLDRb2uYmvGkghNKppl9SmNDl9x3ZTVVSv2S7C5Qz8MTYh1YXv%2BPEPKuKOtV5mEEw1UH079%2FJom2jMdXPDbrtOhWnCiZYCHwSfQmGFC2JSsVSH8SoN1JsvvaGo9HOwbNbxsE2ydb%2FJ5KgvYpzJAHhuEOM5hXdoCkOVHND4rjLc7TRaI7ed3iIBU%2B4qgEE7Ew4CK5NxaxRiGG%2FdI4L3Zsx205rIfNPiwC0wmeDoYYz2W53xjFZfk3VHbU%2BVWGqp3h078RoKCyqy%2FMRzZ8a%2B5hHDiChUPP6w3YZKMmwaqDfgme6QZyiI1D6Qxq9KSif0NsspOm0pUVL1Z3b%2BxOER%2BXUQiSeTJKEzXsAvS%2Bu8Xp8jsYWmmgKI0lJnRcfsUbd95OsUWX6FVI%2FdFbfy9kJV%2BOGxV1nP5l9TMFmJlq8%2BN6qvL1henMsda52GJ%2Fzktzdg6SRppFBHRXiryDt2ByJrRFktXKK9WFzh2%2Fz0Na2hgBw83s1b1YMuW%2BRnYK6rLHHF7v9z7T8FpISU%2Fk7cZThvbSinZUjjCFqH2etq%2Bi1IM5szyU0fxNWbuoqRC8F5XsZ4INGHMmq9DXRIJYmS6Y9d%2BOGJY%2FdkmXWdSK6rREGVmJOu20%2B9YMOG0%2FL4GOqUBKIkHCSpaNse%2BOWSSDs%2FYPLq%2BOFNTNcxjsJURnQxY74VvDNCu78Y9CHEjI%2B5JHwCa43HiFAiBbbuNb6Okid%2BF%2BnUV5FCYJQ%2Fr9njG8YfsZ9ry7S2c7LjIvyxoAFgxbyqfYrHQ4D2FtMAnA3HAYETpQLUngou4m9ShY6mt57PadkRCZxWoAbEKywyiS4O0pSP8AK4Laan9TXtNcSW%2BUmA9EP0HLsjd&X-Amz-Signature=fd7a5d89668bb10b55671fa851d3a2ebec87bf7a39bfacfb2980b6e2d224db44&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YJXBUQY%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIDE3qzjh9H%2F7dxaNi4xbyEdkUlur6zz9bsw2bONOCLCfAiEA9mIr%2FTozlt9zfrkqkSPEQKl%2BEQpWtXax%2FvofJfBj44MqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGZFYRkDQQWheH9hnircAyTLvkWM4Joh0KLDRb2uYmvGkghNKppl9SmNDl9x3ZTVVSv2S7C5Qz8MTYh1YXv%2BPEPKuKOtV5mEEw1UH079%2FJom2jMdXPDbrtOhWnCiZYCHwSfQmGFC2JSsVSH8SoN1JsvvaGo9HOwbNbxsE2ydb%2FJ5KgvYpzJAHhuEOM5hXdoCkOVHND4rjLc7TRaI7ed3iIBU%2B4qgEE7Ew4CK5NxaxRiGG%2FdI4L3Zsx205rIfNPiwC0wmeDoYYz2W53xjFZfk3VHbU%2BVWGqp3h078RoKCyqy%2FMRzZ8a%2B5hHDiChUPP6w3YZKMmwaqDfgme6QZyiI1D6Qxq9KSif0NsspOm0pUVL1Z3b%2BxOER%2BXUQiSeTJKEzXsAvS%2Bu8Xp8jsYWmmgKI0lJnRcfsUbd95OsUWX6FVI%2FdFbfy9kJV%2BOGxV1nP5l9TMFmJlq8%2BN6qvL1henMsda52GJ%2Fzktzdg6SRppFBHRXiryDt2ByJrRFktXKK9WFzh2%2Fz0Na2hgBw83s1b1YMuW%2BRnYK6rLHHF7v9z7T8FpISU%2Fk7cZThvbSinZUjjCFqH2etq%2Bi1IM5szyU0fxNWbuoqRC8F5XsZ4INGHMmq9DXRIJYmS6Y9d%2BOGJY%2FdkmXWdSK6rREGVmJOu20%2B9YMOG0%2FL4GOqUBKIkHCSpaNse%2BOWSSDs%2FYPLq%2BOFNTNcxjsJURnQxY74VvDNCu78Y9CHEjI%2B5JHwCa43HiFAiBbbuNb6Okid%2BF%2BnUV5FCYJQ%2Fr9njG8YfsZ9ry7S2c7LjIvyxoAFgxbyqfYrHQ4D2FtMAnA3HAYETpQLUngou4m9ShY6mt57PadkRCZxWoAbEKywyiS4O0pSP8AK4Laan9TXtNcSW%2BUmA9EP0HLsjd&X-Amz-Signature=11d09a467acf8fbd6893a13c9844283fc9f5a55a74d5109cc93f3ea12dcf441a&X-Amz-SignedHeaders=host&x-id=GetObject)

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
