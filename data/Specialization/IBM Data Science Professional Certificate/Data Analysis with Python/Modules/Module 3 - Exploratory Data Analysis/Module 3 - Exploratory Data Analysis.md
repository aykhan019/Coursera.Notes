

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6S5YKHG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC05cO9cgpI92OA%2FLwWpKy9A0Wx2z%2Bs1IRPhbMXyr99%2BAiEAnqNOJzJ8MVWRcRt%2FplBeuiRrao5ZvcCwa9TLaiyuJ88qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJbaNynvpC4H8fipxircA%2BssI98RNsgMyI9XoUqioqcj3JE%2BVEyQihWhpmqhkbOyvEBTtWFzn9Eai9p0Wk7XiQXOfDMcuWqYLlxWUXxgjhwJpb5tISXc1Y4R9kGCUE1y1owBTAk5cpqSICVtPZh7pjPX0AJYDcs4i0LNo149qMhtuu1swcNisS%2F%2BjTiQslOk9HtWkzURBvnxusSOLQDbO69Y4vQQe5gJZ8bRcurlLL1pnvwJLVjM%2Fzrm%2FUljMrnS5h1Zmt3TaheGX9FypXNiNxmYf5Sbqe5%2B%2F7cZiy7u153qGwFVMaCotohk2x65iW4i4gxul58KtWNsX6JRTyZBlQSj4XikiyaCD%2Bc7uyr%2BStukEFG0fxy4SXKCIE2TpkAGgUqv1pS3tJmgEAWq%2BkQfN2QVseFWaESVwcmioVNoVn5MXOgMZO0MeMseOBxTCkdfCGOXpmFVOLM2ZP6xKBhHP1H1f4Wf%2FgJ04Ze3ngtrlKwlpsvHoAM3myNNDNj41vIUz79e%2B0VzYLMcXxRUNaEAP23W9aCm6W5lvDqghJuQkopJwqxhI46jZwKBNkuP6AQ9EVZqdxa2h7swloHtpzu62pYUWzmHB5bN38sM%2BQHV98Udk%2B3pDvPMd1%2BSvbwxeOKZogNlnZyX515mfjSXMPrZ6bwGOqUBMC3DkK8uDzZLl8RLbQu0i5sISKFqKLuKiyX%2B3KDkrWNDELVs9x74yFLqvIKbEbPMfiYtURNorDRhiIVWiiso3omcKj3tpHhnZW0LL4s6lRcCx7IT7v0TVXJ03NA6b6OR7s1ZxJQfUIajaPV1jmiBeqFrabAs2FtvSAvAFckfUP0RRiEpQVNgN4ZgfqE%2FbYNVKtiGA1LrlbVxsVR9xLym66RfL829&X-Amz-Signature=9e021a04fad53c8ad7df829c513dab28c0cbef1e9c3d759bf0670da935ca885b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6S5YKHG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC05cO9cgpI92OA%2FLwWpKy9A0Wx2z%2Bs1IRPhbMXyr99%2BAiEAnqNOJzJ8MVWRcRt%2FplBeuiRrao5ZvcCwa9TLaiyuJ88qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJbaNynvpC4H8fipxircA%2BssI98RNsgMyI9XoUqioqcj3JE%2BVEyQihWhpmqhkbOyvEBTtWFzn9Eai9p0Wk7XiQXOfDMcuWqYLlxWUXxgjhwJpb5tISXc1Y4R9kGCUE1y1owBTAk5cpqSICVtPZh7pjPX0AJYDcs4i0LNo149qMhtuu1swcNisS%2F%2BjTiQslOk9HtWkzURBvnxusSOLQDbO69Y4vQQe5gJZ8bRcurlLL1pnvwJLVjM%2Fzrm%2FUljMrnS5h1Zmt3TaheGX9FypXNiNxmYf5Sbqe5%2B%2F7cZiy7u153qGwFVMaCotohk2x65iW4i4gxul58KtWNsX6JRTyZBlQSj4XikiyaCD%2Bc7uyr%2BStukEFG0fxy4SXKCIE2TpkAGgUqv1pS3tJmgEAWq%2BkQfN2QVseFWaESVwcmioVNoVn5MXOgMZO0MeMseOBxTCkdfCGOXpmFVOLM2ZP6xKBhHP1H1f4Wf%2FgJ04Ze3ngtrlKwlpsvHoAM3myNNDNj41vIUz79e%2B0VzYLMcXxRUNaEAP23W9aCm6W5lvDqghJuQkopJwqxhI46jZwKBNkuP6AQ9EVZqdxa2h7swloHtpzu62pYUWzmHB5bN38sM%2BQHV98Udk%2B3pDvPMd1%2BSvbwxeOKZogNlnZyX515mfjSXMPrZ6bwGOqUBMC3DkK8uDzZLl8RLbQu0i5sISKFqKLuKiyX%2B3KDkrWNDELVs9x74yFLqvIKbEbPMfiYtURNorDRhiIVWiiso3omcKj3tpHhnZW0LL4s6lRcCx7IT7v0TVXJ03NA6b6OR7s1ZxJQfUIajaPV1jmiBeqFrabAs2FtvSAvAFckfUP0RRiEpQVNgN4ZgfqE%2FbYNVKtiGA1LrlbVxsVR9xLym66RfL829&X-Amz-Signature=f116fbf3e298f53ef71a5dfc9811d80de093735bc21d6efe53361151a8af5268&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6S5YKHG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC05cO9cgpI92OA%2FLwWpKy9A0Wx2z%2Bs1IRPhbMXyr99%2BAiEAnqNOJzJ8MVWRcRt%2FplBeuiRrao5ZvcCwa9TLaiyuJ88qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJbaNynvpC4H8fipxircA%2BssI98RNsgMyI9XoUqioqcj3JE%2BVEyQihWhpmqhkbOyvEBTtWFzn9Eai9p0Wk7XiQXOfDMcuWqYLlxWUXxgjhwJpb5tISXc1Y4R9kGCUE1y1owBTAk5cpqSICVtPZh7pjPX0AJYDcs4i0LNo149qMhtuu1swcNisS%2F%2BjTiQslOk9HtWkzURBvnxusSOLQDbO69Y4vQQe5gJZ8bRcurlLL1pnvwJLVjM%2Fzrm%2FUljMrnS5h1Zmt3TaheGX9FypXNiNxmYf5Sbqe5%2B%2F7cZiy7u153qGwFVMaCotohk2x65iW4i4gxul58KtWNsX6JRTyZBlQSj4XikiyaCD%2Bc7uyr%2BStukEFG0fxy4SXKCIE2TpkAGgUqv1pS3tJmgEAWq%2BkQfN2QVseFWaESVwcmioVNoVn5MXOgMZO0MeMseOBxTCkdfCGOXpmFVOLM2ZP6xKBhHP1H1f4Wf%2FgJ04Ze3ngtrlKwlpsvHoAM3myNNDNj41vIUz79e%2B0VzYLMcXxRUNaEAP23W9aCm6W5lvDqghJuQkopJwqxhI46jZwKBNkuP6AQ9EVZqdxa2h7swloHtpzu62pYUWzmHB5bN38sM%2BQHV98Udk%2B3pDvPMd1%2BSvbwxeOKZogNlnZyX515mfjSXMPrZ6bwGOqUBMC3DkK8uDzZLl8RLbQu0i5sISKFqKLuKiyX%2B3KDkrWNDELVs9x74yFLqvIKbEbPMfiYtURNorDRhiIVWiiso3omcKj3tpHhnZW0LL4s6lRcCx7IT7v0TVXJ03NA6b6OR7s1ZxJQfUIajaPV1jmiBeqFrabAs2FtvSAvAFckfUP0RRiEpQVNgN4ZgfqE%2FbYNVKtiGA1LrlbVxsVR9xLym66RfL829&X-Amz-Signature=6bcd08b0ae116d1fa0bedab0e41832f973368ed5c0971c9e8002a452589fed0e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZRN3LYO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDePzX5WgGgOgZpuxICIyfAzos8nLtoMs%2F57yI2XlN6kAiBkXWQiI3yMJFvrqJDALG3s83rCI1sha3UOddrndOFugCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY6T8hq1KZTT3Vi6LKtwDOOHrRtScBYgouVlGay9cv0i6vOmce2XPuIEDBrafdnD26imB4VdvnuaJ6YCsCHrHp%2B4h10Sxck9M1l2ntK86ts7bJUnS3ffQyBTATD8qO%2BL5CtGqCxkRjLVM1JsjCsXdrLM%2ByGsKG0uNFrLvbYffZxvNQMVN6vI2pwifh64Y4R02CYWT6E0tys%2B0tClrB27hGqdVFXrUAImiA%2BJsoNIFSht0wvMw%2By3bs%2FUPti8QX1NdIOXZvpvsqL0TQIe3gzlPTIFral2nyaD9wIfkkqD%2FXGZe5hOPBeGsEcO%2BOwmUxDHIPKTbUBzok8bHjyB8xQg0G2z8pqKiC5okWfMememgGX3%2BwXKupI8suzcuwVHfeMKyGR9ufskQWItzzRIyVpkpwvGIdLSDS5fdrF%2BBxcRyXFDCWdcLHaBfV7goriDu3WrPHBs2PTXLvSFRrtshJy6M5XJ2XdTzfBvuj9ZRy6hi5aDSNpcTAvkah9WlduHb1EIGHBX1q3BShyS7FnFvfxFbpWptEFtC0L0YHPCcvn%2BuHZUlj0YYeuq%2BowFva8p%2FBNE4RID72t%2FUFPxLfbrO04jKaj1958wN%2BbAP1pMHKvGO9zVe1Ykvj0OxD8fkJUn%2Fa6qPmQgahthamW76IfgwjdjpvAY6pgGUvsF4JSrJ4iKlTywZHPfWDkXtAVlIcdRMyXH%2FUWt6IT%2B3OvJgbEM4kYXHCwu3M0xJyVSls3kNP6bI6wyBCS7fa1yXCcjcm5oJ%2FKX5PzyC%2Fwm9Ls0l2TpiTzTuYLzrgZAuJG4iIY0XgnMVMW4Jr%2BAz0udwJarY4RvvdvPn%2Bnzt%2FxcTzi6AT20zySsa3s02%2Fnco4AhSDVFqEM%2BQKf8%2FnbWcaLwKLGs3&X-Amz-Signature=6d873f89dd2fb24b53dae53ad9eec958b384373a5045656c97b99278aadaeac2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZRN3LYO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDePzX5WgGgOgZpuxICIyfAzos8nLtoMs%2F57yI2XlN6kAiBkXWQiI3yMJFvrqJDALG3s83rCI1sha3UOddrndOFugCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY6T8hq1KZTT3Vi6LKtwDOOHrRtScBYgouVlGay9cv0i6vOmce2XPuIEDBrafdnD26imB4VdvnuaJ6YCsCHrHp%2B4h10Sxck9M1l2ntK86ts7bJUnS3ffQyBTATD8qO%2BL5CtGqCxkRjLVM1JsjCsXdrLM%2ByGsKG0uNFrLvbYffZxvNQMVN6vI2pwifh64Y4R02CYWT6E0tys%2B0tClrB27hGqdVFXrUAImiA%2BJsoNIFSht0wvMw%2By3bs%2FUPti8QX1NdIOXZvpvsqL0TQIe3gzlPTIFral2nyaD9wIfkkqD%2FXGZe5hOPBeGsEcO%2BOwmUxDHIPKTbUBzok8bHjyB8xQg0G2z8pqKiC5okWfMememgGX3%2BwXKupI8suzcuwVHfeMKyGR9ufskQWItzzRIyVpkpwvGIdLSDS5fdrF%2BBxcRyXFDCWdcLHaBfV7goriDu3WrPHBs2PTXLvSFRrtshJy6M5XJ2XdTzfBvuj9ZRy6hi5aDSNpcTAvkah9WlduHb1EIGHBX1q3BShyS7FnFvfxFbpWptEFtC0L0YHPCcvn%2BuHZUlj0YYeuq%2BowFva8p%2FBNE4RID72t%2FUFPxLfbrO04jKaj1958wN%2BbAP1pMHKvGO9zVe1Ykvj0OxD8fkJUn%2Fa6qPmQgahthamW76IfgwjdjpvAY6pgGUvsF4JSrJ4iKlTywZHPfWDkXtAVlIcdRMyXH%2FUWt6IT%2B3OvJgbEM4kYXHCwu3M0xJyVSls3kNP6bI6wyBCS7fa1yXCcjcm5oJ%2FKX5PzyC%2Fwm9Ls0l2TpiTzTuYLzrgZAuJG4iIY0XgnMVMW4Jr%2BAz0udwJarY4RvvdvPn%2Bnzt%2FxcTzi6AT20zySsa3s02%2Fnco4AhSDVFqEM%2BQKf8%2FnbWcaLwKLGs3&X-Amz-Signature=71b5874b4178fc2e8ac5246a99eb22df6cdb5aa2f51d9cb43244b6286ba0ec0c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZRN3LYO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDePzX5WgGgOgZpuxICIyfAzos8nLtoMs%2F57yI2XlN6kAiBkXWQiI3yMJFvrqJDALG3s83rCI1sha3UOddrndOFugCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY6T8hq1KZTT3Vi6LKtwDOOHrRtScBYgouVlGay9cv0i6vOmce2XPuIEDBrafdnD26imB4VdvnuaJ6YCsCHrHp%2B4h10Sxck9M1l2ntK86ts7bJUnS3ffQyBTATD8qO%2BL5CtGqCxkRjLVM1JsjCsXdrLM%2ByGsKG0uNFrLvbYffZxvNQMVN6vI2pwifh64Y4R02CYWT6E0tys%2B0tClrB27hGqdVFXrUAImiA%2BJsoNIFSht0wvMw%2By3bs%2FUPti8QX1NdIOXZvpvsqL0TQIe3gzlPTIFral2nyaD9wIfkkqD%2FXGZe5hOPBeGsEcO%2BOwmUxDHIPKTbUBzok8bHjyB8xQg0G2z8pqKiC5okWfMememgGX3%2BwXKupI8suzcuwVHfeMKyGR9ufskQWItzzRIyVpkpwvGIdLSDS5fdrF%2BBxcRyXFDCWdcLHaBfV7goriDu3WrPHBs2PTXLvSFRrtshJy6M5XJ2XdTzfBvuj9ZRy6hi5aDSNpcTAvkah9WlduHb1EIGHBX1q3BShyS7FnFvfxFbpWptEFtC0L0YHPCcvn%2BuHZUlj0YYeuq%2BowFva8p%2FBNE4RID72t%2FUFPxLfbrO04jKaj1958wN%2BbAP1pMHKvGO9zVe1Ykvj0OxD8fkJUn%2Fa6qPmQgahthamW76IfgwjdjpvAY6pgGUvsF4JSrJ4iKlTywZHPfWDkXtAVlIcdRMyXH%2FUWt6IT%2B3OvJgbEM4kYXHCwu3M0xJyVSls3kNP6bI6wyBCS7fa1yXCcjcm5oJ%2FKX5PzyC%2Fwm9Ls0l2TpiTzTuYLzrgZAuJG4iIY0XgnMVMW4Jr%2BAz0udwJarY4RvvdvPn%2Bnzt%2FxcTzi6AT20zySsa3s02%2Fnco4AhSDVFqEM%2BQKf8%2FnbWcaLwKLGs3&X-Amz-Signature=5c014f10cd02664b0b3e748cd28f46d5dd151010b5f70d004988f20b6308acd3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZRN3LYO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDePzX5WgGgOgZpuxICIyfAzos8nLtoMs%2F57yI2XlN6kAiBkXWQiI3yMJFvrqJDALG3s83rCI1sha3UOddrndOFugCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY6T8hq1KZTT3Vi6LKtwDOOHrRtScBYgouVlGay9cv0i6vOmce2XPuIEDBrafdnD26imB4VdvnuaJ6YCsCHrHp%2B4h10Sxck9M1l2ntK86ts7bJUnS3ffQyBTATD8qO%2BL5CtGqCxkRjLVM1JsjCsXdrLM%2ByGsKG0uNFrLvbYffZxvNQMVN6vI2pwifh64Y4R02CYWT6E0tys%2B0tClrB27hGqdVFXrUAImiA%2BJsoNIFSht0wvMw%2By3bs%2FUPti8QX1NdIOXZvpvsqL0TQIe3gzlPTIFral2nyaD9wIfkkqD%2FXGZe5hOPBeGsEcO%2BOwmUxDHIPKTbUBzok8bHjyB8xQg0G2z8pqKiC5okWfMememgGX3%2BwXKupI8suzcuwVHfeMKyGR9ufskQWItzzRIyVpkpwvGIdLSDS5fdrF%2BBxcRyXFDCWdcLHaBfV7goriDu3WrPHBs2PTXLvSFRrtshJy6M5XJ2XdTzfBvuj9ZRy6hi5aDSNpcTAvkah9WlduHb1EIGHBX1q3BShyS7FnFvfxFbpWptEFtC0L0YHPCcvn%2BuHZUlj0YYeuq%2BowFva8p%2FBNE4RID72t%2FUFPxLfbrO04jKaj1958wN%2BbAP1pMHKvGO9zVe1Ykvj0OxD8fkJUn%2Fa6qPmQgahthamW76IfgwjdjpvAY6pgGUvsF4JSrJ4iKlTywZHPfWDkXtAVlIcdRMyXH%2FUWt6IT%2B3OvJgbEM4kYXHCwu3M0xJyVSls3kNP6bI6wyBCS7fa1yXCcjcm5oJ%2FKX5PzyC%2Fwm9Ls0l2TpiTzTuYLzrgZAuJG4iIY0XgnMVMW4Jr%2BAz0udwJarY4RvvdvPn%2Bnzt%2FxcTzi6AT20zySsa3s02%2Fnco4AhSDVFqEM%2BQKf8%2FnbWcaLwKLGs3&X-Amz-Signature=fc0817cd51d8c1e974b632566b52e99c7a5835192bfc1913e069a414e95eaa44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZRN3LYO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDePzX5WgGgOgZpuxICIyfAzos8nLtoMs%2F57yI2XlN6kAiBkXWQiI3yMJFvrqJDALG3s83rCI1sha3UOddrndOFugCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY6T8hq1KZTT3Vi6LKtwDOOHrRtScBYgouVlGay9cv0i6vOmce2XPuIEDBrafdnD26imB4VdvnuaJ6YCsCHrHp%2B4h10Sxck9M1l2ntK86ts7bJUnS3ffQyBTATD8qO%2BL5CtGqCxkRjLVM1JsjCsXdrLM%2ByGsKG0uNFrLvbYffZxvNQMVN6vI2pwifh64Y4R02CYWT6E0tys%2B0tClrB27hGqdVFXrUAImiA%2BJsoNIFSht0wvMw%2By3bs%2FUPti8QX1NdIOXZvpvsqL0TQIe3gzlPTIFral2nyaD9wIfkkqD%2FXGZe5hOPBeGsEcO%2BOwmUxDHIPKTbUBzok8bHjyB8xQg0G2z8pqKiC5okWfMememgGX3%2BwXKupI8suzcuwVHfeMKyGR9ufskQWItzzRIyVpkpwvGIdLSDS5fdrF%2BBxcRyXFDCWdcLHaBfV7goriDu3WrPHBs2PTXLvSFRrtshJy6M5XJ2XdTzfBvuj9ZRy6hi5aDSNpcTAvkah9WlduHb1EIGHBX1q3BShyS7FnFvfxFbpWptEFtC0L0YHPCcvn%2BuHZUlj0YYeuq%2BowFva8p%2FBNE4RID72t%2FUFPxLfbrO04jKaj1958wN%2BbAP1pMHKvGO9zVe1Ykvj0OxD8fkJUn%2Fa6qPmQgahthamW76IfgwjdjpvAY6pgGUvsF4JSrJ4iKlTywZHPfWDkXtAVlIcdRMyXH%2FUWt6IT%2B3OvJgbEM4kYXHCwu3M0xJyVSls3kNP6bI6wyBCS7fa1yXCcjcm5oJ%2FKX5PzyC%2Fwm9Ls0l2TpiTzTuYLzrgZAuJG4iIY0XgnMVMW4Jr%2BAz0udwJarY4RvvdvPn%2Bnzt%2FxcTzi6AT20zySsa3s02%2Fnco4AhSDVFqEM%2BQKf8%2FnbWcaLwKLGs3&X-Amz-Signature=dc0ef7b4ec5df6590cc3748e44a0f83df27b920280f9540d89bfeab90edd1656&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZRN3LYO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDePzX5WgGgOgZpuxICIyfAzos8nLtoMs%2F57yI2XlN6kAiBkXWQiI3yMJFvrqJDALG3s83rCI1sha3UOddrndOFugCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY6T8hq1KZTT3Vi6LKtwDOOHrRtScBYgouVlGay9cv0i6vOmce2XPuIEDBrafdnD26imB4VdvnuaJ6YCsCHrHp%2B4h10Sxck9M1l2ntK86ts7bJUnS3ffQyBTATD8qO%2BL5CtGqCxkRjLVM1JsjCsXdrLM%2ByGsKG0uNFrLvbYffZxvNQMVN6vI2pwifh64Y4R02CYWT6E0tys%2B0tClrB27hGqdVFXrUAImiA%2BJsoNIFSht0wvMw%2By3bs%2FUPti8QX1NdIOXZvpvsqL0TQIe3gzlPTIFral2nyaD9wIfkkqD%2FXGZe5hOPBeGsEcO%2BOwmUxDHIPKTbUBzok8bHjyB8xQg0G2z8pqKiC5okWfMememgGX3%2BwXKupI8suzcuwVHfeMKyGR9ufskQWItzzRIyVpkpwvGIdLSDS5fdrF%2BBxcRyXFDCWdcLHaBfV7goriDu3WrPHBs2PTXLvSFRrtshJy6M5XJ2XdTzfBvuj9ZRy6hi5aDSNpcTAvkah9WlduHb1EIGHBX1q3BShyS7FnFvfxFbpWptEFtC0L0YHPCcvn%2BuHZUlj0YYeuq%2BowFva8p%2FBNE4RID72t%2FUFPxLfbrO04jKaj1958wN%2BbAP1pMHKvGO9zVe1Ykvj0OxD8fkJUn%2Fa6qPmQgahthamW76IfgwjdjpvAY6pgGUvsF4JSrJ4iKlTywZHPfWDkXtAVlIcdRMyXH%2FUWt6IT%2B3OvJgbEM4kYXHCwu3M0xJyVSls3kNP6bI6wyBCS7fa1yXCcjcm5oJ%2FKX5PzyC%2Fwm9Ls0l2TpiTzTuYLzrgZAuJG4iIY0XgnMVMW4Jr%2BAz0udwJarY4RvvdvPn%2Bnzt%2FxcTzi6AT20zySsa3s02%2Fnco4AhSDVFqEM%2BQKf8%2FnbWcaLwKLGs3&X-Amz-Signature=251eed4845ab248aa2297316ab1c569138bfe0ddfee1918608129836ada409ce&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYFCL5IV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHPg%2F4jdOAZIqIcEA7PYqsbwk3pJ7oYMvBku5gMTNsyKAiEA4q6H98hLUhoLwULMr53JVqx01LMcjx8YNblyDYBnxmMqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFKuYBrvodsY%2Fw4c7yrcA4Bza5JKW8c0KkpOVpTupESj0m2Bcv4dl%2FHijdE20PAZHPhCSxiIaf98ReeRUQcokA72MRw9iMulBLCPgt2xPZ4fQQAIXkVGYkp1cRkJUaWzD7G9BVv62SB60JiPJOncTdqo8NLoK9GUUOVnHBTaknQqhRYnp1ffuR9YhxkbZZLamcOWb2GQVbllxQh9ZG7ALSbV2eluf3RSIDGabuY%2B4ROsiBJzPmdMM73LCJ57hrN5a2qYPZYqS%2FwbL6E0%2B6X%2FMkC9hVXKqIiaYHEms7ZaRcMfJAtufvpwf0KCparFvqbDHSbjEJHb7MtHVqDln0GVO1spsK%2F0RgtRfmVkgNhncUc4%2F2QIOMvA1dllPSHm9nUYzHCjrfT6ubjQAb9ZB5BtU90FeTHPYZdYaV92MxUTq8cxc5ThwPfDc5bConm%2FmtF6tUndH%2B%2BUpmJuHjVDDGuP8bkFbKqkJ23sO828auMhfZpILKmjfPEXRR6C9PUTKIw9mZi1rXvqafr118dK1ECtmAVi8PpFpa1JAzjpgmJHkefnJc%2B5cv5PClP6mv4CKPzFrqY5fGkcH14M1j2UjP4u5qA2WaLhv%2B5TfY8sPXf752qNbWbIh0NHkxhTpBxSEiWausZ1Y63iuE4Qp0GqMOTY6bwGOqUBTIWpZJQ2pj9Ob1HFLQr48138LfE47M4W%2BmNSKZSnw3sXdNFwQfbEJYAhYwFdipdrUMZNyoRW85TVDtYhzbkNjXi9jZEd%2FRHpgeFIAjQ6a%2Fy0SxkQVcMOR5tBkX%2BRETYPlO0dowis5WRaIA9DDvOCiCCkxEWjjMfWO5SBEqqiBWujuGWOfFrov%2FqnHlTCn7mTCYz5n14hgxHL0cGcQu32DGztYywY&X-Amz-Signature=d705354eb25fdd14a7cc6a68e97f3f3dbf30b30abcb0154952ca8315b88553d7&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUMIJIVR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCo%2BEraw3V9%2B0lh0ybJy6D%2F4gDCGtB%2BpQ6Z7Nq%2BgxDCvgIhANxiMnfKga6kV1RFi7twygdiFByB3Ru88h9S6RSRdPK%2BKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3w3bU9MTOa9ss6Tkq3AMbVb5r7YL3QpAZ8kw%2B6Yt7bu5JSQYDWogF6JAAMCK05bQIJsmgHK1o86ffFAOiHoo2QeZVHXQ2nN4q9ueQhP6%2Bji1LF0vD4aJV9MzmOvAKfBZz9wtWDvTtD%2BO57je54CY63marSrwFN%2FdV9EPg2wPVSSCGyxNiSlXp69cV1OV93sNU%2BTIq%2FhZOKq0Hb5tTfxsxEI7GpePKsZAUDJR6FHnPpwlU8hl39FZN3sR%2FQ6QHLBxEKHTD9I9zcSU55cXFvUweC59q%2F%2FkdsTOXJ1E00o27gUch9enjsTVIzsGPO41I5lgG%2BAn4NjOIZ9zLQz6uCF3QgDErrcDvG4MEAjINHUkEZgZKjplsbLRpLPftAep2DTMOl3kxqtX%2BNw1zOwJHeK3nuH%2F7vx23tESSrG8905YB96f124QlDQCI8ZjF2agIjCS0%2FrtI%2B9%2BaVpxAd43G2%2FU%2BV6YrxEl3noGiaO6bVCx4EPXXNCADx%2BVQiR%2Fmc9Td4WyqwtgYOyYT49GCo84A5%2B4tNextNXcpEZdR9AbQ6iTaQNUAcOq%2B8E6pIrcyhtSjvIaLPSnjcVE7C%2BiEoLFLaAWBUaL2OgyTrlub9PZrGB%2BYSQmovP4EwTK4td8tEeea6%2FnUfm4c6GJZAdn%2F7DCu2Om8BjqkAag8AF606sHBjAieDIVmGlsfdwLERnkCE%2FCp7%2BEZzu8bhXYvYNqMAmhYoIVJLp%2FsibO1fMOWX44sagcZylfKMGZsjmJsSYLH%2F%2BM%2FBqh%2FPN02yeB1%2FTwH6mf%2F7HKftdhURzRcRUsFMMyAFMODsLb1bC88LA1EF%2FsRwJdnS9YFsbyr2LawSWrbwpy7TyGeV2vHkZVelehQSBhr5HI0VFMzxajZr8Xf&X-Amz-Signature=021efbb048943e03b466d0a4fd22ec1ae5ad598d07f69e809248800ddeb2fdfd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZRN3LYO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDePzX5WgGgOgZpuxICIyfAzos8nLtoMs%2F57yI2XlN6kAiBkXWQiI3yMJFvrqJDALG3s83rCI1sha3UOddrndOFugCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY6T8hq1KZTT3Vi6LKtwDOOHrRtScBYgouVlGay9cv0i6vOmce2XPuIEDBrafdnD26imB4VdvnuaJ6YCsCHrHp%2B4h10Sxck9M1l2ntK86ts7bJUnS3ffQyBTATD8qO%2BL5CtGqCxkRjLVM1JsjCsXdrLM%2ByGsKG0uNFrLvbYffZxvNQMVN6vI2pwifh64Y4R02CYWT6E0tys%2B0tClrB27hGqdVFXrUAImiA%2BJsoNIFSht0wvMw%2By3bs%2FUPti8QX1NdIOXZvpvsqL0TQIe3gzlPTIFral2nyaD9wIfkkqD%2FXGZe5hOPBeGsEcO%2BOwmUxDHIPKTbUBzok8bHjyB8xQg0G2z8pqKiC5okWfMememgGX3%2BwXKupI8suzcuwVHfeMKyGR9ufskQWItzzRIyVpkpwvGIdLSDS5fdrF%2BBxcRyXFDCWdcLHaBfV7goriDu3WrPHBs2PTXLvSFRrtshJy6M5XJ2XdTzfBvuj9ZRy6hi5aDSNpcTAvkah9WlduHb1EIGHBX1q3BShyS7FnFvfxFbpWptEFtC0L0YHPCcvn%2BuHZUlj0YYeuq%2BowFva8p%2FBNE4RID72t%2FUFPxLfbrO04jKaj1958wN%2BbAP1pMHKvGO9zVe1Ykvj0OxD8fkJUn%2Fa6qPmQgahthamW76IfgwjdjpvAY6pgGUvsF4JSrJ4iKlTywZHPfWDkXtAVlIcdRMyXH%2FUWt6IT%2B3OvJgbEM4kYXHCwu3M0xJyVSls3kNP6bI6wyBCS7fa1yXCcjcm5oJ%2FKX5PzyC%2Fwm9Ls0l2TpiTzTuYLzrgZAuJG4iIY0XgnMVMW4Jr%2BAz0udwJarY4RvvdvPn%2Bnzt%2FxcTzi6AT20zySsa3s02%2Fnco4AhSDVFqEM%2BQKf8%2FnbWcaLwKLGs3&X-Amz-Signature=3c73764c57577b08fee4a224d8fcb80d3fa19c3e59f7f36bc2b755202c54d0d8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZRN3LYO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDePzX5WgGgOgZpuxICIyfAzos8nLtoMs%2F57yI2XlN6kAiBkXWQiI3yMJFvrqJDALG3s83rCI1sha3UOddrndOFugCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY6T8hq1KZTT3Vi6LKtwDOOHrRtScBYgouVlGay9cv0i6vOmce2XPuIEDBrafdnD26imB4VdvnuaJ6YCsCHrHp%2B4h10Sxck9M1l2ntK86ts7bJUnS3ffQyBTATD8qO%2BL5CtGqCxkRjLVM1JsjCsXdrLM%2ByGsKG0uNFrLvbYffZxvNQMVN6vI2pwifh64Y4R02CYWT6E0tys%2B0tClrB27hGqdVFXrUAImiA%2BJsoNIFSht0wvMw%2By3bs%2FUPti8QX1NdIOXZvpvsqL0TQIe3gzlPTIFral2nyaD9wIfkkqD%2FXGZe5hOPBeGsEcO%2BOwmUxDHIPKTbUBzok8bHjyB8xQg0G2z8pqKiC5okWfMememgGX3%2BwXKupI8suzcuwVHfeMKyGR9ufskQWItzzRIyVpkpwvGIdLSDS5fdrF%2BBxcRyXFDCWdcLHaBfV7goriDu3WrPHBs2PTXLvSFRrtshJy6M5XJ2XdTzfBvuj9ZRy6hi5aDSNpcTAvkah9WlduHb1EIGHBX1q3BShyS7FnFvfxFbpWptEFtC0L0YHPCcvn%2BuHZUlj0YYeuq%2BowFva8p%2FBNE4RID72t%2FUFPxLfbrO04jKaj1958wN%2BbAP1pMHKvGO9zVe1Ykvj0OxD8fkJUn%2Fa6qPmQgahthamW76IfgwjdjpvAY6pgGUvsF4JSrJ4iKlTywZHPfWDkXtAVlIcdRMyXH%2FUWt6IT%2B3OvJgbEM4kYXHCwu3M0xJyVSls3kNP6bI6wyBCS7fa1yXCcjcm5oJ%2FKX5PzyC%2Fwm9Ls0l2TpiTzTuYLzrgZAuJG4iIY0XgnMVMW4Jr%2BAz0udwJarY4RvvdvPn%2Bnzt%2FxcTzi6AT20zySsa3s02%2Fnco4AhSDVFqEM%2BQKf8%2FnbWcaLwKLGs3&X-Amz-Signature=7cd53310a51d953ebe1c310310fd860508a5a5664be35f4281c0c90faec3de55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZRN3LYO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDePzX5WgGgOgZpuxICIyfAzos8nLtoMs%2F57yI2XlN6kAiBkXWQiI3yMJFvrqJDALG3s83rCI1sha3UOddrndOFugCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY6T8hq1KZTT3Vi6LKtwDOOHrRtScBYgouVlGay9cv0i6vOmce2XPuIEDBrafdnD26imB4VdvnuaJ6YCsCHrHp%2B4h10Sxck9M1l2ntK86ts7bJUnS3ffQyBTATD8qO%2BL5CtGqCxkRjLVM1JsjCsXdrLM%2ByGsKG0uNFrLvbYffZxvNQMVN6vI2pwifh64Y4R02CYWT6E0tys%2B0tClrB27hGqdVFXrUAImiA%2BJsoNIFSht0wvMw%2By3bs%2FUPti8QX1NdIOXZvpvsqL0TQIe3gzlPTIFral2nyaD9wIfkkqD%2FXGZe5hOPBeGsEcO%2BOwmUxDHIPKTbUBzok8bHjyB8xQg0G2z8pqKiC5okWfMememgGX3%2BwXKupI8suzcuwVHfeMKyGR9ufskQWItzzRIyVpkpwvGIdLSDS5fdrF%2BBxcRyXFDCWdcLHaBfV7goriDu3WrPHBs2PTXLvSFRrtshJy6M5XJ2XdTzfBvuj9ZRy6hi5aDSNpcTAvkah9WlduHb1EIGHBX1q3BShyS7FnFvfxFbpWptEFtC0L0YHPCcvn%2BuHZUlj0YYeuq%2BowFva8p%2FBNE4RID72t%2FUFPxLfbrO04jKaj1958wN%2BbAP1pMHKvGO9zVe1Ykvj0OxD8fkJUn%2Fa6qPmQgahthamW76IfgwjdjpvAY6pgGUvsF4JSrJ4iKlTywZHPfWDkXtAVlIcdRMyXH%2FUWt6IT%2B3OvJgbEM4kYXHCwu3M0xJyVSls3kNP6bI6wyBCS7fa1yXCcjcm5oJ%2FKX5PzyC%2Fwm9Ls0l2TpiTzTuYLzrgZAuJG4iIY0XgnMVMW4Jr%2BAz0udwJarY4RvvdvPn%2Bnzt%2FxcTzi6AT20zySsa3s02%2Fnco4AhSDVFqEM%2BQKf8%2FnbWcaLwKLGs3&X-Amz-Signature=d00c9947f4053f2f664a74d16be1a04cd7e0592d11a0fde704112f44cdfb2602&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUXRNOZI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIPnOFFClOw6iKN0FnnKnpKfYoOOfW4q9cP0nWOka2NAIhAOApgkmKAZKSxDCsQg4AlAB6wLb52zlKm20p8zGCpLySKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyqkKEK4Hl5kloSB8cq3AO8dB%2FRslFz5U3JY3cFjQSdVTVdNSaCKpQpfKfmwKc36X%2Bm3WLB2PKdiPNXSzzpWMTnDbmb40ZjScCxIC%2ByMg%2BgGgTyav1v9eXQfF74eEFDQ3i4FIGcxmC4%2B8WAdqCZ%2Bxjuc2iZ7x3JZg9mhCeFW6SD4M%2FXUr8zWJ4CEc9B4C5QO3rBsznr7yhmCvQ2Vz%2FNM3APesd2mqzNssCjyew8JZpRZf2L%2Bi%2BaMeJMAU7zVo9JcJLt%2BJxxJ%2FKouWB3xZfT7Xig2RQe35azGRoKrXTisSoflKRETorHwfzWogX1HybgukjhiNOEavlgWp1ivLg4Q4AjZMHvQPWV6f3OHSYZXSWjYmVUIhLW39MoJaQrhuxwOqViVgYQ34uACkQRPVLvMewX8bpa4P7rQCahaAZ01ZdbN5c5C6WiPg2Jw7vzU15Vg0q%2B9ibvAFyeCDnXIwjYSoqbm53lPBQqXagv9EJWrjSU%2FFDXfVIoaY%2BIFjlljcBydUGKxU3nzq0nysJbV4yUoSmGYQiWOuqxqQgJP5HLPlgyehlnw%2BCyJhBdwTFmecHxkSIsAeAcuxpP1uRFZgtX8oB8ISXlX%2BQfUWMCICrjxneWw0Cz2AOpAP%2Bthr2RTxAIEZzqVJwPEcoNkmH52zDg2Om8BjqkAW9vyj2EgNWRf6fKeB%2FlB6YICP8XfbdLaRAlMHePOb%2BunfrrjEZdM8NIELj%2BWgAGOJoo2LylbKKmBiROuCxhiJ4AQWH04SywIbCPYh7sHVgXledN6mspTAO4iBjcRO4HljQGhajwWsf3EeWIWTuFBbPyTGOMKJ70wFYQvUP2VQ8%2Fje3dVP8T0yml%2B4PTaW%2BD8dznwhGk9IKgi6tRKlarR4t7hwTc&X-Amz-Signature=5b3b6244702ff1598942721ccee8a72f95e63de25ecdc3448bdcf3ba33511a57&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PDDRRMO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2B511nd6slltlTEHwWGLxMcZW1enTa4wgZTpB8DbG83gIgFcmsfgaUXA5w9hMfKms%2F%2F0LnbGknPgv6hI9XkTwcSm8qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDESDnilksupQ7yLx2yrcA5J1%2BXEFZz4qj4GF59F9bH1jv%2BdJemOrTUJGXinUu%2BCt9nt0PXiZvWV2Ps9B4QnxMJhasPfkS8lp1e2sT%2BOGDdd5se63haHWU9tKxfSLtlNZyby08mFHkB0gyBbuLEQ4uZrlU%2BH2xzFgPq20XBw1RVdk7G3h2INlPAV8uDVL77sEzkp4d2YI%2BojvHE0kwQgRf9LeZ4l6BJemfohfs00wiGEXvSnCNJK8sZY%2BnzUD59iME%2BQcxJX%2F4mVD5YHrKYi5eTe9sv0TtVCEN7rF1%2FxOc3HBgaHdItftzU1xQReCUlSp6ai5qeeBJpt1Vp4dIQMtSyzFMUv%2FxLBbhnZjsZUxQ9P%2BbTdgry08rhoYqrZ%2FiLgEBQ71ff%2BQ3zwcR8tuN3D9RslxK0yUfM1KqRCNnau5M164vGmHRz8Wrn3PU8cRYUjl82AF3DbUvVmGzebfAjCaf3zN3oNQ8dQnk3k95EnBAiotTzSCGN%2BrHb0IEtcm0%2FxhRWZqxVcryR3ixAMdFd20lYPFBDS32ApvraRfzRtb9bh6FoUTxpcn6cd4EeOJ%2FAFL4qeoho%2BgS1BOu8utpo395%2BPyMdWbBY15WIvUfis1tOyyJtBiRNEo1UTZ3qWNWdgKq97B3N7TDEv780pcMLjY6bwGOqUBVEOUHK0WQSBz90zI%2F2YcZpqb9UAf7aoVnq5KHstfLHx8bYzTqs8NnzbsbA%2Bi83b88yHEWw6Yhd8g9EEr3KKSZpyJjxYBjc5xHHV7aBdWv3PTiVnzqHwfwtLiqCnzvBjTv0TjsO8NdX6vYM1WKrBggZPnCRFqQQO5rvEI0Be2xqWq9HK%2FMAmE4mrF91qLPX7RkytlyI24YADFQ2JBoU%2FkOlSMjaHF&X-Amz-Signature=dda26b7c3325d9d0fcbb0abea86de8a8e95975d1eda7298b9b720542062e7a68&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VV7UHHMB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCE%2BbSak8gVuYSUy54baGqfMK7c9YvpBvkcThScmTwm%2FQIgP237NT2roch8cvnOvP7kB%2FW3uXL%2ByBo4Fn%2BANLYft2MqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCCInXRNmH5bBSCEhCrcA9NfzXlH3LUljD3aYN7%2BYqITNIb3U0k1O5CH3Ja3FcmR%2FO0st3FYISROhLFgPFhcKfxbRihvOCwT11jHAebT%2B4zb0YBWN%2FAqe1O7Y3WdhvWvNEagOKqe2F2f3kDI33Ax7osw%2FqZF%2BDnWnnheQWZXSzwvJADANUEwMHzKhJnKi4JMlPSnafFC0sPt3MYKkFptiF2L4Ejh3WWYyZG9PGJ9W9hofgn26Udt4Aa4TXnFiCZwT7Q2MVzveud5V5TMwSrnpLE33jFidaYVVkS84jCCGGnCfyZVvqScM%2B1EXJ%2Fue%2Bptk46d7BP9yhx9728uZgCmvgmDg%2B3dx%2FqQLrAWk3hQ%2FSJL8cdbAXklbMGB%2BStN6fPlndEnYPrhuapJWECRWaJUes%2FCTEqHUxxmAUfo%2FDZx8WEuZWowb%2BbA2TvzkYXbCjyo%2FZcWSf6SO09dMtn2jqEGU0oi8rEgDgDvqBwv%2Bze2GIJj6g3hL3hkhDXIErCT0mF7Nye0vSCIx3035rWxRgvC565ccesvkslWhfWfCp1SDkaFd61lzguPGjEZ3oChbKUS1LZx5gtDp74FboXim%2Bg465I4WcJ7aqBMMiCa%2FyknDp49ot88Gi24iRWuykAWmrbotP3FnPoWeBs9ghkOMK%2FY6bwGOqUBJ8AT0EZ4yitY1xuiUJXHSvnRYEDNHqX98lU8dChMWDBONaC7FqX6m11lt16GJARovFgSVeu5lkW3Zozu32YB38JNam8Om%2BI%2FL%2BxgkuumuYXriQ6r%2FOsQ2Dtlp3KspryB4nTRtm1knzWNcf1vZzZptNdAr1oFSR8jkijzB9jOSCY%2FLlrVpWvyVC2p6Tt5bT%2FPq3PrHbKjvcBFXMSN24QgYhhrYp2C&X-Amz-Signature=77db4ee3a63fc99dda50a207e4d1283ffb9281292b2861ec587d0e6609f0cda1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIYG53O6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFRGhJuN7RTVzA%2FStNkk%2FnJ56KyOL%2FtddA6tdOf33lbiAiBRMELCE5yuVTPBWBcpe01zPdEKPC5%2BiSK3TNGIXrWJxyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM36p4KVJaqMHkw0bVKtwDbQXDXwVAZLkZlVTz%2B0n9cPA84x08GNgXf4uaECTmlmZg2i4p6DIXT53b1c3jcgZFWwLvHF9ccBE8LEKBFbyfqQKkmMjMbvYALJ%2BLS4GicjcKkZttGRBKFKxBcxJQfICtNdCJOxzHthRxLYLPfk1p1SH5%2FZCjnj375EvhB%2FearOEkKiwwh5ODdO6HHLJqW6AHdD7PR1ot%2BEnOaBSGNIIN44TPXofyXOMCBHMIP5sVcRwGnEFz%2F8eLrNReVDJKWdHWjZWnelr5Q8O2aOCwhIIb%2FfBCmzlTbNPEqDYzIQdmo7TSf8vsGyHx%2FSYjtA99fY6HMa0UXBvzee5%2FLnsa08eXmCKS1tQ683B6WldURm56BM2W0PgwnaUoK0x4pQpczLGxRe3G02hsPDrMfdornhN5WmFIn%2BHz3Rk0rnRL5XM79dFjw4SNZ1yRgP0aMElDQ6%2Bt%2BTn3UmpdPQjWlFBU40%2BhX04iKmYY1XsdsWhpFpUGk7MdXPHKKNn78L91XXffJapEMepa00TC6TABMCux%2FbSyNObY06Dm2prJ4%2FwfTZUqZMoPyHfQQkS2UOw7wJ0npqCKgGCp66d23EMN2ZN5V%2F5zhO%2BvaQstU9hqRyUn9UpvAfcyc%2FuK4RQsLbXWuicw79jpvAY6pgHJoXqKm3E4jeRDot4bcHG70NtSnFxjhzi7b8HtlVyb35Bzax7Myz90aapBebRCWekjKrenNzzBDEROmIOvvjedwqsbeLGnhkAIAtz1OW%2FoD1i3gYvJX2OkyR5W9CpBWuDHekYwPYSJYyzTx7gA1Yt0OByqzo%2Ba3z9RbgLvEDoWVftWsbqL0VgHNQ4W5we4obhUyqVp7Mjo0ye5A5gTGH8KqEFmeVOq&X-Amz-Signature=d8aac156b51c41f3f649899a87d0dba4015e0640b80cf987c7c5c6e6fc44a492&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIYG53O6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFRGhJuN7RTVzA%2FStNkk%2FnJ56KyOL%2FtddA6tdOf33lbiAiBRMELCE5yuVTPBWBcpe01zPdEKPC5%2BiSK3TNGIXrWJxyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM36p4KVJaqMHkw0bVKtwDbQXDXwVAZLkZlVTz%2B0n9cPA84x08GNgXf4uaECTmlmZg2i4p6DIXT53b1c3jcgZFWwLvHF9ccBE8LEKBFbyfqQKkmMjMbvYALJ%2BLS4GicjcKkZttGRBKFKxBcxJQfICtNdCJOxzHthRxLYLPfk1p1SH5%2FZCjnj375EvhB%2FearOEkKiwwh5ODdO6HHLJqW6AHdD7PR1ot%2BEnOaBSGNIIN44TPXofyXOMCBHMIP5sVcRwGnEFz%2F8eLrNReVDJKWdHWjZWnelr5Q8O2aOCwhIIb%2FfBCmzlTbNPEqDYzIQdmo7TSf8vsGyHx%2FSYjtA99fY6HMa0UXBvzee5%2FLnsa08eXmCKS1tQ683B6WldURm56BM2W0PgwnaUoK0x4pQpczLGxRe3G02hsPDrMfdornhN5WmFIn%2BHz3Rk0rnRL5XM79dFjw4SNZ1yRgP0aMElDQ6%2Bt%2BTn3UmpdPQjWlFBU40%2BhX04iKmYY1XsdsWhpFpUGk7MdXPHKKNn78L91XXffJapEMepa00TC6TABMCux%2FbSyNObY06Dm2prJ4%2FwfTZUqZMoPyHfQQkS2UOw7wJ0npqCKgGCp66d23EMN2ZN5V%2F5zhO%2BvaQstU9hqRyUn9UpvAfcyc%2FuK4RQsLbXWuicw79jpvAY6pgHJoXqKm3E4jeRDot4bcHG70NtSnFxjhzi7b8HtlVyb35Bzax7Myz90aapBebRCWekjKrenNzzBDEROmIOvvjedwqsbeLGnhkAIAtz1OW%2FoD1i3gYvJX2OkyR5W9CpBWuDHekYwPYSJYyzTx7gA1Yt0OByqzo%2Ba3z9RbgLvEDoWVftWsbqL0VgHNQ4W5we4obhUyqVp7Mjo0ye5A5gTGH8KqEFmeVOq&X-Amz-Signature=dae0683699a370c1d9916a031626821f43bca01e256b0d99400dcd84985aec01&X-Amz-SignedHeaders=host&x-id=GetObject)

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
