

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZO536SF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQChNumdVn9kczJ8qqHMi7248AQVC%2FgTLZNRsNs7ZO%2Bw%2FwIhANVKeZjvdzwpAVpDDN3DmRGmjJCCVRr%2ByZ7vCbzbfgSAKv8DCF8QABoMNjM3NDIzMTgzODA1Igw%2FOxkVhpCArgPiKrIq3AOigWeym0phx65eEkDSnoti9cqDPWW8Cooox48xPpZVwOvgIv%2BJZ8ERGIvQJ7ecECTMX0%2B1Yvobo3vVAkq0nCjLQ5u1E%2BBBsasvw7%2FeTinnvlxucwrwZ3a2BZU3byBlxm4XOM8UAtdRVee%2FluCuPWixM%2FvIhBi9QAe18Oyswg%2BYv54iz8JT%2B6%2BwdkkSKKAbEm5h8pA8oJbIQgMvNCgbIMknESbX287jiOKEMb6%2Briqmt9%2FO5pj%2F5fEmjeRfqTvzgjNIaa%2Fqy0nf6%2BvBFQShCZLq6EGx2mxDOHQHhCffUGoWPsaOE9rdTuouxsGLIDM71KXK0uoiZDi5R%2FGBc79MXixNXo42blUQxplFCLYQ30gMsutl6gHXiHScj%2BOwZ5bQRN%2FqO5DrULH6QczwrZlSz2PVGivzuWXDiWz4ntP%2FV8q8VTGf%2Fc360XvNxHml31IneQbJYV08grHV%2FsMyl1OcVR9v5iUc4rFAnl6a9uwnap6bp4%2FOr%2B7lHPzPOkDWh5kNaQ0bbIpoA%2BrHS1bEz8bqwVZM5c32MlUZmrE%2F90iN1mGzGqBL76YvfJThHiMSPLfR7%2BgBzCQBxMs%2BSPpg0jt5PJ0jHc5js%2FN0tgIawThKwt8B6vBqgh0pDV6c6OroWTDQ%2BZK9BjqkAVUnR5frrRIaeiL0JiQO5ytE%2BQu3luIihh%2BDp5QXhCMBlh4B%2FhTZTuzd%2FwarJCgBe1EvasZ9%2FCjGS4oPd63%2BeXI2szl3Z%2FC%2BV7L1ZTf8Yojdgkga7XYUUEJXzUwXg97NGjX1%2B7oXbB2lArGsStseNpSF4nNRBeRhSvRp7p5oAEXO3nqbaegc9F%2FXfbwFwyQ5Cjm2usgA8hq%2FUd7OnJjNKK8GIHzB&X-Amz-Signature=977022bfa76852b2ffb433080267e973aa9bed6a5d76a328e3294f96eccfeca0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZO536SF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQChNumdVn9kczJ8qqHMi7248AQVC%2FgTLZNRsNs7ZO%2Bw%2FwIhANVKeZjvdzwpAVpDDN3DmRGmjJCCVRr%2ByZ7vCbzbfgSAKv8DCF8QABoMNjM3NDIzMTgzODA1Igw%2FOxkVhpCArgPiKrIq3AOigWeym0phx65eEkDSnoti9cqDPWW8Cooox48xPpZVwOvgIv%2BJZ8ERGIvQJ7ecECTMX0%2B1Yvobo3vVAkq0nCjLQ5u1E%2BBBsasvw7%2FeTinnvlxucwrwZ3a2BZU3byBlxm4XOM8UAtdRVee%2FluCuPWixM%2FvIhBi9QAe18Oyswg%2BYv54iz8JT%2B6%2BwdkkSKKAbEm5h8pA8oJbIQgMvNCgbIMknESbX287jiOKEMb6%2Briqmt9%2FO5pj%2F5fEmjeRfqTvzgjNIaa%2Fqy0nf6%2BvBFQShCZLq6EGx2mxDOHQHhCffUGoWPsaOE9rdTuouxsGLIDM71KXK0uoiZDi5R%2FGBc79MXixNXo42blUQxplFCLYQ30gMsutl6gHXiHScj%2BOwZ5bQRN%2FqO5DrULH6QczwrZlSz2PVGivzuWXDiWz4ntP%2FV8q8VTGf%2Fc360XvNxHml31IneQbJYV08grHV%2FsMyl1OcVR9v5iUc4rFAnl6a9uwnap6bp4%2FOr%2B7lHPzPOkDWh5kNaQ0bbIpoA%2BrHS1bEz8bqwVZM5c32MlUZmrE%2F90iN1mGzGqBL76YvfJThHiMSPLfR7%2BgBzCQBxMs%2BSPpg0jt5PJ0jHc5js%2FN0tgIawThKwt8B6vBqgh0pDV6c6OroWTDQ%2BZK9BjqkAVUnR5frrRIaeiL0JiQO5ytE%2BQu3luIihh%2BDp5QXhCMBlh4B%2FhTZTuzd%2FwarJCgBe1EvasZ9%2FCjGS4oPd63%2BeXI2szl3Z%2FC%2BV7L1ZTf8Yojdgkga7XYUUEJXzUwXg97NGjX1%2B7oXbB2lArGsStseNpSF4nNRBeRhSvRp7p5oAEXO3nqbaegc9F%2FXfbwFwyQ5Cjm2usgA8hq%2FUd7OnJjNKK8GIHzB&X-Amz-Signature=bd120ab95e621b2849ddbfb1263f00f16a8a13749664f08939cce19377d15170&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZO536SF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQChNumdVn9kczJ8qqHMi7248AQVC%2FgTLZNRsNs7ZO%2Bw%2FwIhANVKeZjvdzwpAVpDDN3DmRGmjJCCVRr%2ByZ7vCbzbfgSAKv8DCF8QABoMNjM3NDIzMTgzODA1Igw%2FOxkVhpCArgPiKrIq3AOigWeym0phx65eEkDSnoti9cqDPWW8Cooox48xPpZVwOvgIv%2BJZ8ERGIvQJ7ecECTMX0%2B1Yvobo3vVAkq0nCjLQ5u1E%2BBBsasvw7%2FeTinnvlxucwrwZ3a2BZU3byBlxm4XOM8UAtdRVee%2FluCuPWixM%2FvIhBi9QAe18Oyswg%2BYv54iz8JT%2B6%2BwdkkSKKAbEm5h8pA8oJbIQgMvNCgbIMknESbX287jiOKEMb6%2Briqmt9%2FO5pj%2F5fEmjeRfqTvzgjNIaa%2Fqy0nf6%2BvBFQShCZLq6EGx2mxDOHQHhCffUGoWPsaOE9rdTuouxsGLIDM71KXK0uoiZDi5R%2FGBc79MXixNXo42blUQxplFCLYQ30gMsutl6gHXiHScj%2BOwZ5bQRN%2FqO5DrULH6QczwrZlSz2PVGivzuWXDiWz4ntP%2FV8q8VTGf%2Fc360XvNxHml31IneQbJYV08grHV%2FsMyl1OcVR9v5iUc4rFAnl6a9uwnap6bp4%2FOr%2B7lHPzPOkDWh5kNaQ0bbIpoA%2BrHS1bEz8bqwVZM5c32MlUZmrE%2F90iN1mGzGqBL76YvfJThHiMSPLfR7%2BgBzCQBxMs%2BSPpg0jt5PJ0jHc5js%2FN0tgIawThKwt8B6vBqgh0pDV6c6OroWTDQ%2BZK9BjqkAVUnR5frrRIaeiL0JiQO5ytE%2BQu3luIihh%2BDp5QXhCMBlh4B%2FhTZTuzd%2FwarJCgBe1EvasZ9%2FCjGS4oPd63%2BeXI2szl3Z%2FC%2BV7L1ZTf8Yojdgkga7XYUUEJXzUwXg97NGjX1%2B7oXbB2lArGsStseNpSF4nNRBeRhSvRp7p5oAEXO3nqbaegc9F%2FXfbwFwyQ5Cjm2usgA8hq%2FUd7OnJjNKK8GIHzB&X-Amz-Signature=c6978ca4bd256b2d8b0f0a00287cd519f3a6feffe18b939d54ecc3b78b088919&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFCJCLP2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCZxvgbwK7pfUN2DD3paphqGnUYvV%2Fp267o5C1K%2FVOAkQIhAMh5WowAhVfT1ajrKzEF6AtUwQGQIrEMROw0DtmqAtCPKv8DCF8QABoMNjM3NDIzMTgzODA1Igz9lstxKQbT1XT3%2Bx8q3APsAm%2FI0tDvO%2FW3A55zJCKIx4HAzHzYP423i8pSQXTxWjwiUJ6Gbk4wE9i0A0VW8v3Vhi6GMEergmVLRPFq8YLdQGvkm1KTIpnI7LvsFyat%2FK7Xf0yoI%2FKz23NEj4gSGupY1tllB6yjv08yF5ES2SQKNNCvW6Ezj23tRkHoLwtulDrzlLZbXvQ3KvMMJZByfU0PVwv%2F2v3vxwaQ6o%2FQRXeDfBEYzJYu4ekeJSodbJVAIiyU2rwVFudFQOeDBHzHJFoZpaTtxhiK%2FdTzg61Kb8ff46KQlaRzACjmDUrqPTSjIs2u%2FgDxucxYI0mAI6o3bqMjrAMjjybcj3hvoaGmAf%2BPU7CsLwj0DmXsuh2sAGWuzjouIHPVYLPEs143CiqMaRhWK1FE1SC1mvI9P7dgiv5Wp%2FlQiFhh6lzqQkm%2FpGYliDEEHzPqQ7WcCTOkvXCHwvioy0zAuF5C2D8fTgrdelQnNEN5UAFhIkfxLcg5M1anncX6dyayhPesoL7SS0nwHzVoyItUtA70SPOpYFUOONjCcZwQAjHfNA%2FmZ1bqzL65cYpLkAl%2FQfjFsNiI%2FA5cghYevNfPL3L%2FIy4KQZUX7n3H9kILclgBslHVv%2FCQx%2B4D%2BkO97LAEADUlcwpD8jC6%2BZK9BjqkAfaBGQECstJC2rpzfllyYV2faRWas%2FrwLa17Sdhze6S0ngUfJHlTqpOYEbAv%2F5n8dCTlnVwMebTeJQTNFspk0suHdALBTFBHPWcCIPiqlD2ChUKORf25En5%2BHGdVemezu4exyGRKbQALC1u9RxUI9avtesGDGpdo67pnxqcdaL5LJxqpKX4gzl4Igw5RnwIr83OG9g73oF%2FzXDeu1HNwNT%2F%2Buihx&X-Amz-Signature=66ae572baee7d7ca55585a81d3d287483bfd7680c37d6c6dccb895838ab1cc9e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFCJCLP2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCZxvgbwK7pfUN2DD3paphqGnUYvV%2Fp267o5C1K%2FVOAkQIhAMh5WowAhVfT1ajrKzEF6AtUwQGQIrEMROw0DtmqAtCPKv8DCF8QABoMNjM3NDIzMTgzODA1Igz9lstxKQbT1XT3%2Bx8q3APsAm%2FI0tDvO%2FW3A55zJCKIx4HAzHzYP423i8pSQXTxWjwiUJ6Gbk4wE9i0A0VW8v3Vhi6GMEergmVLRPFq8YLdQGvkm1KTIpnI7LvsFyat%2FK7Xf0yoI%2FKz23NEj4gSGupY1tllB6yjv08yF5ES2SQKNNCvW6Ezj23tRkHoLwtulDrzlLZbXvQ3KvMMJZByfU0PVwv%2F2v3vxwaQ6o%2FQRXeDfBEYzJYu4ekeJSodbJVAIiyU2rwVFudFQOeDBHzHJFoZpaTtxhiK%2FdTzg61Kb8ff46KQlaRzACjmDUrqPTSjIs2u%2FgDxucxYI0mAI6o3bqMjrAMjjybcj3hvoaGmAf%2BPU7CsLwj0DmXsuh2sAGWuzjouIHPVYLPEs143CiqMaRhWK1FE1SC1mvI9P7dgiv5Wp%2FlQiFhh6lzqQkm%2FpGYliDEEHzPqQ7WcCTOkvXCHwvioy0zAuF5C2D8fTgrdelQnNEN5UAFhIkfxLcg5M1anncX6dyayhPesoL7SS0nwHzVoyItUtA70SPOpYFUOONjCcZwQAjHfNA%2FmZ1bqzL65cYpLkAl%2FQfjFsNiI%2FA5cghYevNfPL3L%2FIy4KQZUX7n3H9kILclgBslHVv%2FCQx%2B4D%2BkO97LAEADUlcwpD8jC6%2BZK9BjqkAfaBGQECstJC2rpzfllyYV2faRWas%2FrwLa17Sdhze6S0ngUfJHlTqpOYEbAv%2F5n8dCTlnVwMebTeJQTNFspk0suHdALBTFBHPWcCIPiqlD2ChUKORf25En5%2BHGdVemezu4exyGRKbQALC1u9RxUI9avtesGDGpdo67pnxqcdaL5LJxqpKX4gzl4Igw5RnwIr83OG9g73oF%2FzXDeu1HNwNT%2F%2Buihx&X-Amz-Signature=e6923b1335c38167e3449c5517e46739676286f0179ed2f4d90c116594e3f61a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFCJCLP2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCZxvgbwK7pfUN2DD3paphqGnUYvV%2Fp267o5C1K%2FVOAkQIhAMh5WowAhVfT1ajrKzEF6AtUwQGQIrEMROw0DtmqAtCPKv8DCF8QABoMNjM3NDIzMTgzODA1Igz9lstxKQbT1XT3%2Bx8q3APsAm%2FI0tDvO%2FW3A55zJCKIx4HAzHzYP423i8pSQXTxWjwiUJ6Gbk4wE9i0A0VW8v3Vhi6GMEergmVLRPFq8YLdQGvkm1KTIpnI7LvsFyat%2FK7Xf0yoI%2FKz23NEj4gSGupY1tllB6yjv08yF5ES2SQKNNCvW6Ezj23tRkHoLwtulDrzlLZbXvQ3KvMMJZByfU0PVwv%2F2v3vxwaQ6o%2FQRXeDfBEYzJYu4ekeJSodbJVAIiyU2rwVFudFQOeDBHzHJFoZpaTtxhiK%2FdTzg61Kb8ff46KQlaRzACjmDUrqPTSjIs2u%2FgDxucxYI0mAI6o3bqMjrAMjjybcj3hvoaGmAf%2BPU7CsLwj0DmXsuh2sAGWuzjouIHPVYLPEs143CiqMaRhWK1FE1SC1mvI9P7dgiv5Wp%2FlQiFhh6lzqQkm%2FpGYliDEEHzPqQ7WcCTOkvXCHwvioy0zAuF5C2D8fTgrdelQnNEN5UAFhIkfxLcg5M1anncX6dyayhPesoL7SS0nwHzVoyItUtA70SPOpYFUOONjCcZwQAjHfNA%2FmZ1bqzL65cYpLkAl%2FQfjFsNiI%2FA5cghYevNfPL3L%2FIy4KQZUX7n3H9kILclgBslHVv%2FCQx%2B4D%2BkO97LAEADUlcwpD8jC6%2BZK9BjqkAfaBGQECstJC2rpzfllyYV2faRWas%2FrwLa17Sdhze6S0ngUfJHlTqpOYEbAv%2F5n8dCTlnVwMebTeJQTNFspk0suHdALBTFBHPWcCIPiqlD2ChUKORf25En5%2BHGdVemezu4exyGRKbQALC1u9RxUI9avtesGDGpdo67pnxqcdaL5LJxqpKX4gzl4Igw5RnwIr83OG9g73oF%2FzXDeu1HNwNT%2F%2Buihx&X-Amz-Signature=7e99cd370e30b7e53ee8db6c68501f17a9fe8ae6a72b2d1d339bf02144fc224f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFCJCLP2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCZxvgbwK7pfUN2DD3paphqGnUYvV%2Fp267o5C1K%2FVOAkQIhAMh5WowAhVfT1ajrKzEF6AtUwQGQIrEMROw0DtmqAtCPKv8DCF8QABoMNjM3NDIzMTgzODA1Igz9lstxKQbT1XT3%2Bx8q3APsAm%2FI0tDvO%2FW3A55zJCKIx4HAzHzYP423i8pSQXTxWjwiUJ6Gbk4wE9i0A0VW8v3Vhi6GMEergmVLRPFq8YLdQGvkm1KTIpnI7LvsFyat%2FK7Xf0yoI%2FKz23NEj4gSGupY1tllB6yjv08yF5ES2SQKNNCvW6Ezj23tRkHoLwtulDrzlLZbXvQ3KvMMJZByfU0PVwv%2F2v3vxwaQ6o%2FQRXeDfBEYzJYu4ekeJSodbJVAIiyU2rwVFudFQOeDBHzHJFoZpaTtxhiK%2FdTzg61Kb8ff46KQlaRzACjmDUrqPTSjIs2u%2FgDxucxYI0mAI6o3bqMjrAMjjybcj3hvoaGmAf%2BPU7CsLwj0DmXsuh2sAGWuzjouIHPVYLPEs143CiqMaRhWK1FE1SC1mvI9P7dgiv5Wp%2FlQiFhh6lzqQkm%2FpGYliDEEHzPqQ7WcCTOkvXCHwvioy0zAuF5C2D8fTgrdelQnNEN5UAFhIkfxLcg5M1anncX6dyayhPesoL7SS0nwHzVoyItUtA70SPOpYFUOONjCcZwQAjHfNA%2FmZ1bqzL65cYpLkAl%2FQfjFsNiI%2FA5cghYevNfPL3L%2FIy4KQZUX7n3H9kILclgBslHVv%2FCQx%2B4D%2BkO97LAEADUlcwpD8jC6%2BZK9BjqkAfaBGQECstJC2rpzfllyYV2faRWas%2FrwLa17Sdhze6S0ngUfJHlTqpOYEbAv%2F5n8dCTlnVwMebTeJQTNFspk0suHdALBTFBHPWcCIPiqlD2ChUKORf25En5%2BHGdVemezu4exyGRKbQALC1u9RxUI9avtesGDGpdo67pnxqcdaL5LJxqpKX4gzl4Igw5RnwIr83OG9g73oF%2FzXDeu1HNwNT%2F%2Buihx&X-Amz-Signature=30a5caee99e2da3c7341b82a99233edd217de293ebfd3b99878c0072a3d81647&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFCJCLP2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCZxvgbwK7pfUN2DD3paphqGnUYvV%2Fp267o5C1K%2FVOAkQIhAMh5WowAhVfT1ajrKzEF6AtUwQGQIrEMROw0DtmqAtCPKv8DCF8QABoMNjM3NDIzMTgzODA1Igz9lstxKQbT1XT3%2Bx8q3APsAm%2FI0tDvO%2FW3A55zJCKIx4HAzHzYP423i8pSQXTxWjwiUJ6Gbk4wE9i0A0VW8v3Vhi6GMEergmVLRPFq8YLdQGvkm1KTIpnI7LvsFyat%2FK7Xf0yoI%2FKz23NEj4gSGupY1tllB6yjv08yF5ES2SQKNNCvW6Ezj23tRkHoLwtulDrzlLZbXvQ3KvMMJZByfU0PVwv%2F2v3vxwaQ6o%2FQRXeDfBEYzJYu4ekeJSodbJVAIiyU2rwVFudFQOeDBHzHJFoZpaTtxhiK%2FdTzg61Kb8ff46KQlaRzACjmDUrqPTSjIs2u%2FgDxucxYI0mAI6o3bqMjrAMjjybcj3hvoaGmAf%2BPU7CsLwj0DmXsuh2sAGWuzjouIHPVYLPEs143CiqMaRhWK1FE1SC1mvI9P7dgiv5Wp%2FlQiFhh6lzqQkm%2FpGYliDEEHzPqQ7WcCTOkvXCHwvioy0zAuF5C2D8fTgrdelQnNEN5UAFhIkfxLcg5M1anncX6dyayhPesoL7SS0nwHzVoyItUtA70SPOpYFUOONjCcZwQAjHfNA%2FmZ1bqzL65cYpLkAl%2FQfjFsNiI%2FA5cghYevNfPL3L%2FIy4KQZUX7n3H9kILclgBslHVv%2FCQx%2B4D%2BkO97LAEADUlcwpD8jC6%2BZK9BjqkAfaBGQECstJC2rpzfllyYV2faRWas%2FrwLa17Sdhze6S0ngUfJHlTqpOYEbAv%2F5n8dCTlnVwMebTeJQTNFspk0suHdALBTFBHPWcCIPiqlD2ChUKORf25En5%2BHGdVemezu4exyGRKbQALC1u9RxUI9avtesGDGpdo67pnxqcdaL5LJxqpKX4gzl4Igw5RnwIr83OG9g73oF%2FzXDeu1HNwNT%2F%2Buihx&X-Amz-Signature=486879b9ac93cfad7c6761f8eb26fff4b0013ad45fdbb99b357c92b61c11d0ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFCJCLP2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCZxvgbwK7pfUN2DD3paphqGnUYvV%2Fp267o5C1K%2FVOAkQIhAMh5WowAhVfT1ajrKzEF6AtUwQGQIrEMROw0DtmqAtCPKv8DCF8QABoMNjM3NDIzMTgzODA1Igz9lstxKQbT1XT3%2Bx8q3APsAm%2FI0tDvO%2FW3A55zJCKIx4HAzHzYP423i8pSQXTxWjwiUJ6Gbk4wE9i0A0VW8v3Vhi6GMEergmVLRPFq8YLdQGvkm1KTIpnI7LvsFyat%2FK7Xf0yoI%2FKz23NEj4gSGupY1tllB6yjv08yF5ES2SQKNNCvW6Ezj23tRkHoLwtulDrzlLZbXvQ3KvMMJZByfU0PVwv%2F2v3vxwaQ6o%2FQRXeDfBEYzJYu4ekeJSodbJVAIiyU2rwVFudFQOeDBHzHJFoZpaTtxhiK%2FdTzg61Kb8ff46KQlaRzACjmDUrqPTSjIs2u%2FgDxucxYI0mAI6o3bqMjrAMjjybcj3hvoaGmAf%2BPU7CsLwj0DmXsuh2sAGWuzjouIHPVYLPEs143CiqMaRhWK1FE1SC1mvI9P7dgiv5Wp%2FlQiFhh6lzqQkm%2FpGYliDEEHzPqQ7WcCTOkvXCHwvioy0zAuF5C2D8fTgrdelQnNEN5UAFhIkfxLcg5M1anncX6dyayhPesoL7SS0nwHzVoyItUtA70SPOpYFUOONjCcZwQAjHfNA%2FmZ1bqzL65cYpLkAl%2FQfjFsNiI%2FA5cghYevNfPL3L%2FIy4KQZUX7n3H9kILclgBslHVv%2FCQx%2B4D%2BkO97LAEADUlcwpD8jC6%2BZK9BjqkAfaBGQECstJC2rpzfllyYV2faRWas%2FrwLa17Sdhze6S0ngUfJHlTqpOYEbAv%2F5n8dCTlnVwMebTeJQTNFspk0suHdALBTFBHPWcCIPiqlD2ChUKORf25En5%2BHGdVemezu4exyGRKbQALC1u9RxUI9avtesGDGpdo67pnxqcdaL5LJxqpKX4gzl4Igw5RnwIr83OG9g73oF%2FzXDeu1HNwNT%2F%2Buihx&X-Amz-Signature=34a82ced06a95ac03b9d60337b9438be4b1947054e2af12aa97843691f69b240&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SV3SLUWV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIEkTnOEi33N4xkYvJhu0vi1Ro5pIfv%2BX4XNyoWMTSbaxAiAtzioWofV4gvsSObL7u2Pw1tRBOVngzD7zZxxtEDCRFyr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMqdjdDeU3TsFISRsOKtwDgcCBJABBH2ORfB1FzSTMu5caFlPK5BCbNSdtrQC1pD4OveU9Gy58NI7MdYGL33AAs9Pr4l%2Bt3sMLuYmeYgKQFHe6LuzQsx%2FLFPTafDsIIZm18cXOZxPnHb29VDXLl127QISDvJEFekJj%2FvegFDHXwS7U2PFxnCJW3OOKI2BIkgiDD4mtK6zjyKr%2BM83Jq%2Bgu2HQOZA58UTbNQA3osOYf95FazlCdiURczHprk39QmQMVdLuqk7MN4SPAdo1iIDP3uiQ%2Bhq4dMOXyE0PgP02ZG2TVADFzTMFduFhh2tLvEI%2FzxHxTWD9kAg6qy6af52ohIFaN6%2B0Z603yysRip%2FByoWiy0gSgSKMfYpm5EZU95ytmM1RHxJEx1CbQruGUJ25RprXs7rh1A2jDptPR%2BUkuRwFegyTEfWSpH2Yk5nGzehJ3XkTK1uypIY8keqDlcdA6Wi%2FuLMXgtNQ0zJlrnlGd1hbv3mHx62m7OVNwEMYaQayS40Drr0jpCgYjsBWot6SVHCKD6syznBfHUHS05CgAnsxPnuYlq5EqmBuei8mhG6YTpK97XoAU%2Bb%2Bq1eKXG3Nkwmb74GQGKp%2B6HtU9QyHtn7W%2FLnDwI45o2ssPUWlPkQjIMbP6WOS9sSE%2B4gww8%2FiSvQY6pgG65VAVr1CwGj9XZKzt5vu5yVY%2FRwkTCwaMdrq9MTV40cR3HEu3qRJYfatQq3ks2KfyA7mXqT0GhxC59jzB%2FwEAROfzwCVSCszz%2BOFwe6dysQ%2BvZcoq8%2FqlEQC1ej9JHhOapTkAwN8q1l7m1XyKLdV8UtGR3RxMGoNg6cuMGzb4BuN2uQJwHq%2Fte6SJ4Q8cHrIc8shbxzuei%2BzCy%2BxDe7kcEWICKaND&X-Amz-Signature=5914469d032a4534f42cf9c06e7a3f9a123009eb4107c5356cfaa1c1c59ff24c&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJOFSOLF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIDcQuP38csx2wp7GLAYS13TeG8%2B5jv7Zo9DUKnyIYAmSAiBlnuuWn2VsFic1HGpsFPCWOHNCh241XKvQSA0G0CsmYyr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMmP91i%2FmhxO7OvbHBKtwDEuLrUsccNZNqKROIFHbMD0%2Fz%2F3wsWkSY8y4e5jOl7EoJbV0XDaO0jnonKniUHKp%2FE4ow1U%2BXU5H72oF7oInVmNSVnVgAMf6P%2F8Kihrvf8GNjMY0CE1OM9zRR%2Bb270hW128ihrI84fkRqsSnffbde2CiNHH2xv3OWrLQKAvrp8ADhfd6HXDOIdQHGauOgeiBDzBK5bKbusVdcl4nThPwobL7qXnUbdfBCjpGVyHF8hHubOkgrB2nN06EfAcweelJR%2BSrvvSFaGY0Tr0fRDXUL7i6%2Fk3WRQwMr9S%2B4mCWQOaZMSWyAJAX4lpgU4JSoWqSRp%2BIo48E8uGo9yDrhlxvINeqtV4aCzfZ%2BQpj91JJrJefNc%2FEi9T0CU0Tf4kque%2FPOx%2FTIkhvodRGUtdvzyx0YXr9aK6QZ1GdOYig1B6Sj0fMM4A2WhUsfh3JNdnGnBIOtDm8lcJsqxOaYnfjAfBedF2TiOCf%2FFeaSmQ2arCIh%2B5ejFtSvmPdKy629I6sxuc8RV36CSxUflROqYmlWKNVuYLnuS1cy%2FZQrBFiOHuKbceA8SH2%2FI1BpBAM3KO1mXsRsdUoDNXWpaI5HYnx%2F9MtywZRPVEVeuh3w4r4RfdaoPeoIyn8uCgn7pk6WIXIwjfmSvQY6pgFEwKfb9EAGsnzQr1L%2FPIzUAOwTh5ec6FvkP%2ByZKNHOrOxlm90u%2BeMUIYy30SADXskjJezARm3W3s4G5oMkRMqr6%2Bh9cuTHM2DyRQp85VYKRjqqcMet2owXJcMSxBGoF1txt6DimJw4YbpHIlSF%2B2kMmJySF803k5yq67YMtdiOlLZCnCAbAnlxyVlYPVKPtwIvSyoseBFmjICKofpV%2FyqcmwwLIhz3&X-Amz-Signature=427a6f8482b8db14a4a5dce3845e0063434e7ae8bd1e149ebda298daf8a255c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFCJCLP2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCZxvgbwK7pfUN2DD3paphqGnUYvV%2Fp267o5C1K%2FVOAkQIhAMh5WowAhVfT1ajrKzEF6AtUwQGQIrEMROw0DtmqAtCPKv8DCF8QABoMNjM3NDIzMTgzODA1Igz9lstxKQbT1XT3%2Bx8q3APsAm%2FI0tDvO%2FW3A55zJCKIx4HAzHzYP423i8pSQXTxWjwiUJ6Gbk4wE9i0A0VW8v3Vhi6GMEergmVLRPFq8YLdQGvkm1KTIpnI7LvsFyat%2FK7Xf0yoI%2FKz23NEj4gSGupY1tllB6yjv08yF5ES2SQKNNCvW6Ezj23tRkHoLwtulDrzlLZbXvQ3KvMMJZByfU0PVwv%2F2v3vxwaQ6o%2FQRXeDfBEYzJYu4ekeJSodbJVAIiyU2rwVFudFQOeDBHzHJFoZpaTtxhiK%2FdTzg61Kb8ff46KQlaRzACjmDUrqPTSjIs2u%2FgDxucxYI0mAI6o3bqMjrAMjjybcj3hvoaGmAf%2BPU7CsLwj0DmXsuh2sAGWuzjouIHPVYLPEs143CiqMaRhWK1FE1SC1mvI9P7dgiv5Wp%2FlQiFhh6lzqQkm%2FpGYliDEEHzPqQ7WcCTOkvXCHwvioy0zAuF5C2D8fTgrdelQnNEN5UAFhIkfxLcg5M1anncX6dyayhPesoL7SS0nwHzVoyItUtA70SPOpYFUOONjCcZwQAjHfNA%2FmZ1bqzL65cYpLkAl%2FQfjFsNiI%2FA5cghYevNfPL3L%2FIy4KQZUX7n3H9kILclgBslHVv%2FCQx%2B4D%2BkO97LAEADUlcwpD8jC6%2BZK9BjqkAfaBGQECstJC2rpzfllyYV2faRWas%2FrwLa17Sdhze6S0ngUfJHlTqpOYEbAv%2F5n8dCTlnVwMebTeJQTNFspk0suHdALBTFBHPWcCIPiqlD2ChUKORf25En5%2BHGdVemezu4exyGRKbQALC1u9RxUI9avtesGDGpdo67pnxqcdaL5LJxqpKX4gzl4Igw5RnwIr83OG9g73oF%2FzXDeu1HNwNT%2F%2Buihx&X-Amz-Signature=a7cff765bab9ce2059a3ff8f0d419bcae56b6ebf9c3f5fdfd701e03219a924c0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFCJCLP2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCZxvgbwK7pfUN2DD3paphqGnUYvV%2Fp267o5C1K%2FVOAkQIhAMh5WowAhVfT1ajrKzEF6AtUwQGQIrEMROw0DtmqAtCPKv8DCF8QABoMNjM3NDIzMTgzODA1Igz9lstxKQbT1XT3%2Bx8q3APsAm%2FI0tDvO%2FW3A55zJCKIx4HAzHzYP423i8pSQXTxWjwiUJ6Gbk4wE9i0A0VW8v3Vhi6GMEergmVLRPFq8YLdQGvkm1KTIpnI7LvsFyat%2FK7Xf0yoI%2FKz23NEj4gSGupY1tllB6yjv08yF5ES2SQKNNCvW6Ezj23tRkHoLwtulDrzlLZbXvQ3KvMMJZByfU0PVwv%2F2v3vxwaQ6o%2FQRXeDfBEYzJYu4ekeJSodbJVAIiyU2rwVFudFQOeDBHzHJFoZpaTtxhiK%2FdTzg61Kb8ff46KQlaRzACjmDUrqPTSjIs2u%2FgDxucxYI0mAI6o3bqMjrAMjjybcj3hvoaGmAf%2BPU7CsLwj0DmXsuh2sAGWuzjouIHPVYLPEs143CiqMaRhWK1FE1SC1mvI9P7dgiv5Wp%2FlQiFhh6lzqQkm%2FpGYliDEEHzPqQ7WcCTOkvXCHwvioy0zAuF5C2D8fTgrdelQnNEN5UAFhIkfxLcg5M1anncX6dyayhPesoL7SS0nwHzVoyItUtA70SPOpYFUOONjCcZwQAjHfNA%2FmZ1bqzL65cYpLkAl%2FQfjFsNiI%2FA5cghYevNfPL3L%2FIy4KQZUX7n3H9kILclgBslHVv%2FCQx%2B4D%2BkO97LAEADUlcwpD8jC6%2BZK9BjqkAfaBGQECstJC2rpzfllyYV2faRWas%2FrwLa17Sdhze6S0ngUfJHlTqpOYEbAv%2F5n8dCTlnVwMebTeJQTNFspk0suHdALBTFBHPWcCIPiqlD2ChUKORf25En5%2BHGdVemezu4exyGRKbQALC1u9RxUI9avtesGDGpdo67pnxqcdaL5LJxqpKX4gzl4Igw5RnwIr83OG9g73oF%2FzXDeu1HNwNT%2F%2Buihx&X-Amz-Signature=9abc2b9b5e21d9be18e7c5cb9c9c7c0804bcbbbbe2a45148af296d90eb862e1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFCJCLP2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCZxvgbwK7pfUN2DD3paphqGnUYvV%2Fp267o5C1K%2FVOAkQIhAMh5WowAhVfT1ajrKzEF6AtUwQGQIrEMROw0DtmqAtCPKv8DCF8QABoMNjM3NDIzMTgzODA1Igz9lstxKQbT1XT3%2Bx8q3APsAm%2FI0tDvO%2FW3A55zJCKIx4HAzHzYP423i8pSQXTxWjwiUJ6Gbk4wE9i0A0VW8v3Vhi6GMEergmVLRPFq8YLdQGvkm1KTIpnI7LvsFyat%2FK7Xf0yoI%2FKz23NEj4gSGupY1tllB6yjv08yF5ES2SQKNNCvW6Ezj23tRkHoLwtulDrzlLZbXvQ3KvMMJZByfU0PVwv%2F2v3vxwaQ6o%2FQRXeDfBEYzJYu4ekeJSodbJVAIiyU2rwVFudFQOeDBHzHJFoZpaTtxhiK%2FdTzg61Kb8ff46KQlaRzACjmDUrqPTSjIs2u%2FgDxucxYI0mAI6o3bqMjrAMjjybcj3hvoaGmAf%2BPU7CsLwj0DmXsuh2sAGWuzjouIHPVYLPEs143CiqMaRhWK1FE1SC1mvI9P7dgiv5Wp%2FlQiFhh6lzqQkm%2FpGYliDEEHzPqQ7WcCTOkvXCHwvioy0zAuF5C2D8fTgrdelQnNEN5UAFhIkfxLcg5M1anncX6dyayhPesoL7SS0nwHzVoyItUtA70SPOpYFUOONjCcZwQAjHfNA%2FmZ1bqzL65cYpLkAl%2FQfjFsNiI%2FA5cghYevNfPL3L%2FIy4KQZUX7n3H9kILclgBslHVv%2FCQx%2B4D%2BkO97LAEADUlcwpD8jC6%2BZK9BjqkAfaBGQECstJC2rpzfllyYV2faRWas%2FrwLa17Sdhze6S0ngUfJHlTqpOYEbAv%2F5n8dCTlnVwMebTeJQTNFspk0suHdALBTFBHPWcCIPiqlD2ChUKORf25En5%2BHGdVemezu4exyGRKbQALC1u9RxUI9avtesGDGpdo67pnxqcdaL5LJxqpKX4gzl4Igw5RnwIr83OG9g73oF%2FzXDeu1HNwNT%2F%2Buihx&X-Amz-Signature=284cc9aad972c4cd29f3c84368d641d86780c4f5cd1497dbd6fa148260375d74&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSLVS3LS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIBVFvtxmtH76g33GIFJcHaLnkZGfkh2rwu8J6xv74ZvUAiEA003yc%2BZW%2Bx1IXLN3nbRnAZg68WpGm7dBjYUFSXft3IMq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDCwg0eF7H66fV2ilKSrcA9m93U2gkfWa8rInKCmcyBOPJvRWqplTi7yKcbHrL2XQ8rWmPrva8TEYtIfeKwwbSoki9dJEz0%2FXNDKAwR8ZtEfG6vVRh19ybTpVR9L562IV64HgwEbaJtSj%2Bp5gQDUMuMf8bw%2B0YnVXmbVVUi5tHUrQ5c9ooLK3yVWLQC%2FDxRohu%2Bmjz%2BbMQvT9Sv01SeWTpzooyT164vEsMVYpNyUdfAtoYW5XcDfcTcfEOfX2cgr8SQXShKEbUBoLMd2bcw2WhmIuBeABXjWar92TCcXhIJPXkoRD2RmLcmopkg3w1XK8xl8aKLYaRJwz4DmCmQ2j%2FfwN43iVJ9dx7DMFQXWLEK0tW%2FSFvwJ5AssKm84o%2BPJQSEAsOTTs2VvFB87kNu6ECIIdCO09UmnjaVYrfNobPwrmZSGj6IDzPvsElhhD1kCvRYyNq4o7sQB4urlWEqKbW%2FX82ypTsSun8r6NxgQS3VHM3RpODT2leL4TfvqlA%2FcSzcIh4DItXilAfdPTgG7BLUMw4bAuNRy%2Fo13KYkyatpJLDf%2FxmNg0Zql2hTlblkfzN81RIQ%2BpqCtPXWaUG5pBoI8dol%2BG8laZiUatZnuwr625u%2BENWLC9ERhXUaDwMqMm5pDL%2FG6P7cbVc2CXMIT5kr0GOqUBsBHQHjbXhojNYSS5MV6gcEVApKHFKK6V1h69dzOZbsLIglZtDhGBQ3NIxnQoAy70%2BTVbMItdkmhLzFduPp8csR%2FMg%2B%2F2Kas5jgIZ7fLmG2BywxocJgTvP%2F0dbydCQhQ6VJyQEmf14Q%2Fft7roY6EEwOQMmg2cHOtVWriaI%2Bhq39kGHh04T42FBkd8sAfNcTZgHzdf50mdwiTr6XBL3wyN5ioJ%2BYxa&X-Amz-Signature=5114ecdabfd8015dc7437a820df80b6e74f0fdac831bc733f5ebb7d659cbbee8&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA6QEOPB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIBBx%2B4rbTvs9cXIeGaRQAmI7IrVOLfNSpeOwAdNZMch2AiBsdruaiekQSBnD0EJRLL1Dn2Ura1zWw%2BGr81K9sjaYEir%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIML%2BiwWlzCkhv7i%2F7MKtwDDbX23FGPUQiTRxlr7nbQNYv2RPhhL3NUS%2BI29QCUq1oTNZ82Zryb9Fj%2Fg5lyh4NiVm32HUQ%2FwZ2h%2FvR77%2BpMZXenfEACyB%2BpTp79RqgVrbRKDnxIY2VOMqKouI3aqXUiBC1efgGNrdzmoAp1b%2BLvW59lvmT5eIQUHZcyYzm7FhcUi62wVoOVYcUqim0MqNPAujeoz0DoUbO%2Fum%2FLD%2FH3ujt4hjnmdRpX3DUu0X0ptityw0LZbvasCgNBgc2d%2FsMiJelSJzuxAXgBGfPrsfyfl3v0LlvoN1Sk9Vgynvodv5%2BDqafqPFCp8%2B6V2iD3HgEr%2FZ6JLLm2GnJElbR1sWAnuGJqESwtR2G3ZbPmAyt9uusKSVI%2BgFHSdHXOz2n4Qd7yvtq8dFQSCq%2FPCGWISoKOWD91s7hBTkJVR90WGe1NIL6vio1gI4SeZvzQdZDFRGxcgVWlSSRF8K%2BmG2g8tIvHvhjJXInypIv72lGFOp6UKTJ2P5mvQI80Y70hhFyQOHEN30BNjbc3s%2FUWyQfhPSLexJ0341%2Bfqgmy8%2F6hoNZPX2hPZvI6vaL7IVPuyZzJl6fsLqAlGLPFOsH3mv9RdrEog4ZTQgbZr63JVC9PifAdiQ3bEkvNMxLKNNvEsdsw1vmSvQY6pgEKa0591Y54iUD0GSldlLvPfOIQZRub%2BVze%2Byw%2B6woINVZo09LsNfQZfXXi7PwduscuIu71aoiAcmfNJF6PJl9T4xxdTOYFupbDOquWbfYms2uX3JZfec1hZfGEdoP9Kw4c%2B%2BQgbJcWpm5I2z03ze5yNhPn3U%2B0EBSUqY5%2F7M5FAP%2FNbf7sAPqXL%2FigtDTnaZXW6l%2BAoj9kw9GbHCjjMRQf%2FOhNhQPX&X-Amz-Signature=f988c26ecce45c41ac1c614862c7f6c5d29ff92be6f957341bafbc8d58b46ae8&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVC4H75B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIF1V9MlYWhwgqD0DN1zofVK2dtqzYyzroUXN0FgimtmMAiBshxgWwByGS5kcTqm9LHLsUTvYp1w6QCDmQphqy0zbCSr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMZyWpegZrAhtK7jxjKtwDjLxIJ2SXwPzSUWG4Fl3HB6qTd94PMIKdMYbXCO4n8SIUKxJUvXjtovcyE%2FfbOmoAZrRkmKNHnWPMzRUsyZE%2FC4ljIxmrLwnEjROWFwHFDy4bKHINeCMNDQVBklGxD2KtsnlCc2zp9Zq%2BW0CUfhtnLfLsV4P9VBBczvbbFnOPptNwU%2BpSGB3ELFKPlRl8iFJslTeybRipqNmpvkAnr8hhaMXL%2BR2JFr%2BqcxDxxlBvF%2FaNWA8vo%2F%2BL3WTOzx2mJzDuLo1sOu0DGv6dOTsRse2KFnJuS9p2Kv9IvXWHtJ46akneKtFZzoE1F3IG%2FVgux6D%2F0uqrIuozRNwxxklsrng92ZJpLRTYdzG5mL1RqKZ5Z%2FOc%2FAumLQJQGqT9gwjfwtDXNDHvH9QMHcMrD6%2BQnvwkXjSnZqyH5v0%2F3dtYZseD%2B7m9i66jyvx02kMRSwOz19JtKACm6GokpN7aeYQ5YuaspiTPb14TuUSZ1gzvuMVONffMEIMXE18KtiQTlLJMql4ueai7PkGR7LrNvaMiCZDDsSGK%2BVHKOMLV8vrNtnUbdxuaPDkKl5jbpYIcV8BjK6p5Q5tyfrIhRiT0mx8yhxp%2BBTkmyNCSExzKhXwg1X3RJfFWV7ubXzKOXanJJD4w7viSvQY6pgGOSZ0ml5pNyJgJrMuMysejnxVl%2FN7xY2%2FpDWrnJaEJv1%2B%2BTyKSVbSixQeLek3iZwSM2TD1bd2mHR4l9DFWebD5HwT%2FQ9cQdhF6bwTMqwr5tvNBs57xAbk4DbfhZwjLkGsDwQ%2FSqJXJl1C0lIOMryjmFaFQ4jCjVWHEpDlRIBSO7%2F2QAV6c%2B9w%2F6DykSD%2Bp3jxi9m%2Bx2exCMm2OLQx8uM%2B6%2F2EwpJHi&X-Amz-Signature=31079d42c28d1a3524f6b0b4983ea2c6651096754d6191b66ff46ab4121ad1a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642Y37JXY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIEyTybmXklEh7FqSWMMRaE3yhloH2i%2FUCupi6yKFIx28AiEAxKjtZ7zWC1BM3VsxrcjQrRoGjxtO3aaUUYYvo222ukUq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDPnEM%2BqKLDVKy0RHtCrcA4am9NtLAK8IWWtKPZb4W0fg97W%2FsSeyPiT4mfg0u02k4TrSPhRYG4KJWvH0ak%2FSDcpZ8w6HGEBQkvKxzG%2FrScKtxCMr4Hgjjg1Ti8MX1Lp5TYM7gSKfVafaDRsaZz8V7wgq%2BjZh1m33uKxNTcPj8nrIkM8jhSxFOuvx0ZplxF%2BFM%2FXNIGHMYa8HCDQL5aL1%2FsMvPptUYA4hDe1cykw9kQceSzYbWxhg4TSDkWoiQfycsPLvqUmf5bjNAPCGPUGtFRLUa1QryA%2B5VKySFoybgxzalsNHwEiwXmXrIuFZyMcb3YFZZv3hlwQP0KyS9c%2BkKto5Gb1O9rz8dT24rqJxeFOYQmlZrOjb2Rs%2BAlvp2Su8WCYoz%2BJsdXSvrV3lW2o7M3NAxYB3g5OS30T881daPYP1QVFR%2BAK3kDmyfFECb946sg%2BvSy%2BCYo7i8TO8U%2FGj%2F3%2BN1aLov9P03OW188K7SF3Z7nfw643gKk6eXiJ8zfuKHKgN035xLfIozTXuYL%2F%2BFJ2Li%2BKARXfknlWzsznK4nw9S2j8nMzaaQYNRcz7Va%2FJJLUGmC7nHHBe4GUAUc6STusrjY3I%2FYjR2cTDGA3kFT63D5OE5KPIXgMM0mK3K2oQmO2WhTqcwotXLgV3MPv4kr0GOqUB64l1v3yeuIi%2B9FJz%2BaGr%2F1CzJfd3Kd51HZ2Alp8IidXhKAxhiblRdg4KKdA8zFlRDw9xKbDyWASM%2BVlKhoA7Yx%2Fk22gjWk4WuocwDzioa7fb5Sh3b8kkJ89dboWt%2BqPevgP5X6ez13VonL8pXdmStbCZP3w938sP%2BRNSRnFSiV8%2B%2BSvBBHylx2Th73OB7AWCaMMp2c8kIgNKszsolqz2%2BVMc8ffh&X-Amz-Signature=67eba7c7ec099fd00dc17494b40b7976d80847c170ed27c251293876a17382d6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642Y37JXY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIEyTybmXklEh7FqSWMMRaE3yhloH2i%2FUCupi6yKFIx28AiEAxKjtZ7zWC1BM3VsxrcjQrRoGjxtO3aaUUYYvo222ukUq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDPnEM%2BqKLDVKy0RHtCrcA4am9NtLAK8IWWtKPZb4W0fg97W%2FsSeyPiT4mfg0u02k4TrSPhRYG4KJWvH0ak%2FSDcpZ8w6HGEBQkvKxzG%2FrScKtxCMr4Hgjjg1Ti8MX1Lp5TYM7gSKfVafaDRsaZz8V7wgq%2BjZh1m33uKxNTcPj8nrIkM8jhSxFOuvx0ZplxF%2BFM%2FXNIGHMYa8HCDQL5aL1%2FsMvPptUYA4hDe1cykw9kQceSzYbWxhg4TSDkWoiQfycsPLvqUmf5bjNAPCGPUGtFRLUa1QryA%2B5VKySFoybgxzalsNHwEiwXmXrIuFZyMcb3YFZZv3hlwQP0KyS9c%2BkKto5Gb1O9rz8dT24rqJxeFOYQmlZrOjb2Rs%2BAlvp2Su8WCYoz%2BJsdXSvrV3lW2o7M3NAxYB3g5OS30T881daPYP1QVFR%2BAK3kDmyfFECb946sg%2BvSy%2BCYo7i8TO8U%2FGj%2F3%2BN1aLov9P03OW188K7SF3Z7nfw643gKk6eXiJ8zfuKHKgN035xLfIozTXuYL%2F%2BFJ2Li%2BKARXfknlWzsznK4nw9S2j8nMzaaQYNRcz7Va%2FJJLUGmC7nHHBe4GUAUc6STusrjY3I%2FYjR2cTDGA3kFT63D5OE5KPIXgMM0mK3K2oQmO2WhTqcwotXLgV3MPv4kr0GOqUB64l1v3yeuIi%2B9FJz%2BaGr%2F1CzJfd3Kd51HZ2Alp8IidXhKAxhiblRdg4KKdA8zFlRDw9xKbDyWASM%2BVlKhoA7Yx%2Fk22gjWk4WuocwDzioa7fb5Sh3b8kkJ89dboWt%2BqPevgP5X6ez13VonL8pXdmStbCZP3w938sP%2BRNSRnFSiV8%2B%2BSvBBHylx2Th73OB7AWCaMMp2c8kIgNKszsolqz2%2BVMc8ffh&X-Amz-Signature=f9697b95f8d072a9fcc26f384d4408778fafcf212f46bd575f47c4ee20b0361c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
