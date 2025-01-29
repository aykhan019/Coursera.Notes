

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PKI24EX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIEoLq3O8ZC9v8CUutnNM9sznqJ59tpU8Jb%2B0ehfyyrppAiEAy9FS3i5HY0e1pIdhAcM1Cmg1aCpOcYheQxsRdu0k2%2BsqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOdugh7Rqa8sJSpnyrcA5XKrKoh3S53Lj6HH8dKUH1b%2Bfr7O%2BOlB08poGxcBIjfUd8TcFmA199zjzOpFLMuGQmLFIK6aO%2F%2BheSgGFqS%2F42vPgqPDMGaodrvofEdcJYYP%2FZFo6gcLiMo2yW3eNydY4OLKyMVMDx%2B0y%2BYva7I6QSB2ai5Wi5MdFBTE80Zo%2FHj9yUraM0BfSu5IG%2BfbvDNBQ%2FuuOxmuPd9y2VoOR0AT9NUP2iqxxIQ9YC0EjL6Cuhb5AoaKIDiOcmqMZNUph1udRfLoW62fx64TqJd%2FrjsvYaQ1jA567gud3mjq2JhcHYcqSd0WJMNPuhpPRvpoTjjJj%2FhibDEWDExdm%2FrJca%2BLrfSm8poJNfYblPYK%2BcC%2FB1e30qWB55OGbOiTYRrwlSTE9DycYhvsgfDJ4RHWO%2BE5N0IdA%2FjOr1h%2F5ADN%2Bx8xp%2FTUnbVs9ZlkRnZ%2F1w6m8iDmsNhh%2Bj27NMbegENrBKDgA8%2BSOeB4raLrLL2mXCz8itfAKVqOPZxHJJDki%2FBSmg9StgG0XzUfywEIcP0UJjTSfpGNjTBERDal7zhxOj7ly2rySlOtpKvOj%2BIovx4LFbgntstQsqq73UrlPgz%2ByXoUAKKTHmPGfypM6v%2FtkAjtHwWH1vj4L6dtq5W33kNMNmf5rwGOqUBjmFoTUhTAFBo8BflvehS%2BIMF6lUHjB%2Fui9munSJkikHUwEv9F%2FUoYSwbGQtXjsSJJLj%2BpTQLLRMc5bIySE9mHzFBZGCg1WlpjAkyRcG6psMvjmErYEOeXpOcJuc9OdBfDsgloGX5CnjSbjiR%2BOUvr0cmLNVUNNtc8KTmuvuB9RFndpexEXDeWQXMXzYelRUdEPr6HWaIFGdbJ38ccVEgcayjHzaP&X-Amz-Signature=3d507a9caa553ab7b7a1f0e63632e7bd729bbfa675802d0ca7087a275c7e4429&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PKI24EX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIEoLq3O8ZC9v8CUutnNM9sznqJ59tpU8Jb%2B0ehfyyrppAiEAy9FS3i5HY0e1pIdhAcM1Cmg1aCpOcYheQxsRdu0k2%2BsqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOdugh7Rqa8sJSpnyrcA5XKrKoh3S53Lj6HH8dKUH1b%2Bfr7O%2BOlB08poGxcBIjfUd8TcFmA199zjzOpFLMuGQmLFIK6aO%2F%2BheSgGFqS%2F42vPgqPDMGaodrvofEdcJYYP%2FZFo6gcLiMo2yW3eNydY4OLKyMVMDx%2B0y%2BYva7I6QSB2ai5Wi5MdFBTE80Zo%2FHj9yUraM0BfSu5IG%2BfbvDNBQ%2FuuOxmuPd9y2VoOR0AT9NUP2iqxxIQ9YC0EjL6Cuhb5AoaKIDiOcmqMZNUph1udRfLoW62fx64TqJd%2FrjsvYaQ1jA567gud3mjq2JhcHYcqSd0WJMNPuhpPRvpoTjjJj%2FhibDEWDExdm%2FrJca%2BLrfSm8poJNfYblPYK%2BcC%2FB1e30qWB55OGbOiTYRrwlSTE9DycYhvsgfDJ4RHWO%2BE5N0IdA%2FjOr1h%2F5ADN%2Bx8xp%2FTUnbVs9ZlkRnZ%2F1w6m8iDmsNhh%2Bj27NMbegENrBKDgA8%2BSOeB4raLrLL2mXCz8itfAKVqOPZxHJJDki%2FBSmg9StgG0XzUfywEIcP0UJjTSfpGNjTBERDal7zhxOj7ly2rySlOtpKvOj%2BIovx4LFbgntstQsqq73UrlPgz%2ByXoUAKKTHmPGfypM6v%2FtkAjtHwWH1vj4L6dtq5W33kNMNmf5rwGOqUBjmFoTUhTAFBo8BflvehS%2BIMF6lUHjB%2Fui9munSJkikHUwEv9F%2FUoYSwbGQtXjsSJJLj%2BpTQLLRMc5bIySE9mHzFBZGCg1WlpjAkyRcG6psMvjmErYEOeXpOcJuc9OdBfDsgloGX5CnjSbjiR%2BOUvr0cmLNVUNNtc8KTmuvuB9RFndpexEXDeWQXMXzYelRUdEPr6HWaIFGdbJ38ccVEgcayjHzaP&X-Amz-Signature=3800796a5c39478d8c67c1fac48d9c754145dbff718f65612ad850599db93ec7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PKI24EX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIEoLq3O8ZC9v8CUutnNM9sznqJ59tpU8Jb%2B0ehfyyrppAiEAy9FS3i5HY0e1pIdhAcM1Cmg1aCpOcYheQxsRdu0k2%2BsqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOdugh7Rqa8sJSpnyrcA5XKrKoh3S53Lj6HH8dKUH1b%2Bfr7O%2BOlB08poGxcBIjfUd8TcFmA199zjzOpFLMuGQmLFIK6aO%2F%2BheSgGFqS%2F42vPgqPDMGaodrvofEdcJYYP%2FZFo6gcLiMo2yW3eNydY4OLKyMVMDx%2B0y%2BYva7I6QSB2ai5Wi5MdFBTE80Zo%2FHj9yUraM0BfSu5IG%2BfbvDNBQ%2FuuOxmuPd9y2VoOR0AT9NUP2iqxxIQ9YC0EjL6Cuhb5AoaKIDiOcmqMZNUph1udRfLoW62fx64TqJd%2FrjsvYaQ1jA567gud3mjq2JhcHYcqSd0WJMNPuhpPRvpoTjjJj%2FhibDEWDExdm%2FrJca%2BLrfSm8poJNfYblPYK%2BcC%2FB1e30qWB55OGbOiTYRrwlSTE9DycYhvsgfDJ4RHWO%2BE5N0IdA%2FjOr1h%2F5ADN%2Bx8xp%2FTUnbVs9ZlkRnZ%2F1w6m8iDmsNhh%2Bj27NMbegENrBKDgA8%2BSOeB4raLrLL2mXCz8itfAKVqOPZxHJJDki%2FBSmg9StgG0XzUfywEIcP0UJjTSfpGNjTBERDal7zhxOj7ly2rySlOtpKvOj%2BIovx4LFbgntstQsqq73UrlPgz%2ByXoUAKKTHmPGfypM6v%2FtkAjtHwWH1vj4L6dtq5W33kNMNmf5rwGOqUBjmFoTUhTAFBo8BflvehS%2BIMF6lUHjB%2Fui9munSJkikHUwEv9F%2FUoYSwbGQtXjsSJJLj%2BpTQLLRMc5bIySE9mHzFBZGCg1WlpjAkyRcG6psMvjmErYEOeXpOcJuc9OdBfDsgloGX5CnjSbjiR%2BOUvr0cmLNVUNNtc8KTmuvuB9RFndpexEXDeWQXMXzYelRUdEPr6HWaIFGdbJ38ccVEgcayjHzaP&X-Amz-Signature=2663df237ead36b02c614d068f539e9bdfe991d576d24b540d50464ae9a3cf90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVEO54G3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFUWNF37Y5KYi42ldSDHAKrMpv9LchRyHcH0I%2FsH6b9qAiArVMc%2Fz9luMS2potVCw30jFx61uKaYAmoZnzQKtdz1vCqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgjI5A%2Fmnqw277NjBKtwDtMHJwXsPWC75ZfYuzQYi6VV7tc%2BTBFCOlhuZkcrh6duvFX2W5GOAF0Jnb%2FsKemJInArpkzkq58fCW1cySUuYyKf12Qm%2BI4ICyC2BqNnQaKL%2FQrwhoQK0My3q60QfrrzR%2FkPRMcOfoBOSac6b34X%2FOn6kMDD4eKPyl6Dxi%2FIAmcTcwOmnMsWNb2ZDKEhDfdGsOCM0Lyvj%2FdE6Olz7psgRILRBhAVLlYd5H8V56I6TNCPKrfxFbAs5nb9E78LIu%2BzcxT0u4O%2FdLQh%2FRiVOr%2Fy6B4StnECf1MibgbVaXy4deaowdo8VSKuP%2BKyuhK0kBde%2BSndK%2FxX6dKxWQaft3Z%2F5LLIGLErzhoiBYOkjAXmR8odo1xvJa8ajn%2BPehZFKofvjQhlBwSdAXr8TAixMhWlWJI2xuK7sddPoxAIhFwhoWn9TdpkyYuz6VscGME5DyPDPafEyda%2FRp9CFvVQA5K9JccrvWNvSRGVVuMs20DSO1bujIKP2H8%2FY1C8WNma5Ry4%2FLAgT%2FdaVrHwn1dagUMAK0p08Kw10WtESbOo6EdnMZ4YR%2FiE68XgxB30Eg%2FoQT3n76Ly0UANy%2BjL9ytxT8FRUY3ZmEfjcCvyMdWvntEGV5ltJnwLejvq3sVvXxSkw55%2FmvAY6pgF8YSo%2F3wtiUDqLtrmKdnUaQ49hz2c%2FQalM1GLoAcP5Wm5m4lIaYYi11wO2WRglXXwSvyE8Tsn%2BjhVBByjKGeixCyH8LXUYYVApsxgIiq82z5923683tfoXWiA4QFw0q4YcUkwi3eNlJOicllmiLMC2phcTtojPpMNiiNSYU1gu3m1ShdehMsc8Wu509FJqwSCgwyeV4mEaG1xqINCFAWkTevFBh9F%2F&X-Amz-Signature=7358a07eb3f91fc96cbbcc7717115e561fc66999bf926da16969d417a159d9cb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVEO54G3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFUWNF37Y5KYi42ldSDHAKrMpv9LchRyHcH0I%2FsH6b9qAiArVMc%2Fz9luMS2potVCw30jFx61uKaYAmoZnzQKtdz1vCqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgjI5A%2Fmnqw277NjBKtwDtMHJwXsPWC75ZfYuzQYi6VV7tc%2BTBFCOlhuZkcrh6duvFX2W5GOAF0Jnb%2FsKemJInArpkzkq58fCW1cySUuYyKf12Qm%2BI4ICyC2BqNnQaKL%2FQrwhoQK0My3q60QfrrzR%2FkPRMcOfoBOSac6b34X%2FOn6kMDD4eKPyl6Dxi%2FIAmcTcwOmnMsWNb2ZDKEhDfdGsOCM0Lyvj%2FdE6Olz7psgRILRBhAVLlYd5H8V56I6TNCPKrfxFbAs5nb9E78LIu%2BzcxT0u4O%2FdLQh%2FRiVOr%2Fy6B4StnECf1MibgbVaXy4deaowdo8VSKuP%2BKyuhK0kBde%2BSndK%2FxX6dKxWQaft3Z%2F5LLIGLErzhoiBYOkjAXmR8odo1xvJa8ajn%2BPehZFKofvjQhlBwSdAXr8TAixMhWlWJI2xuK7sddPoxAIhFwhoWn9TdpkyYuz6VscGME5DyPDPafEyda%2FRp9CFvVQA5K9JccrvWNvSRGVVuMs20DSO1bujIKP2H8%2FY1C8WNma5Ry4%2FLAgT%2FdaVrHwn1dagUMAK0p08Kw10WtESbOo6EdnMZ4YR%2FiE68XgxB30Eg%2FoQT3n76Ly0UANy%2BjL9ytxT8FRUY3ZmEfjcCvyMdWvntEGV5ltJnwLejvq3sVvXxSkw55%2FmvAY6pgF8YSo%2F3wtiUDqLtrmKdnUaQ49hz2c%2FQalM1GLoAcP5Wm5m4lIaYYi11wO2WRglXXwSvyE8Tsn%2BjhVBByjKGeixCyH8LXUYYVApsxgIiq82z5923683tfoXWiA4QFw0q4YcUkwi3eNlJOicllmiLMC2phcTtojPpMNiiNSYU1gu3m1ShdehMsc8Wu509FJqwSCgwyeV4mEaG1xqINCFAWkTevFBh9F%2F&X-Amz-Signature=321fde5bda86927951967464397a3997562c99197ec22eb08bc26caa2b001dd1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVEO54G3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFUWNF37Y5KYi42ldSDHAKrMpv9LchRyHcH0I%2FsH6b9qAiArVMc%2Fz9luMS2potVCw30jFx61uKaYAmoZnzQKtdz1vCqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgjI5A%2Fmnqw277NjBKtwDtMHJwXsPWC75ZfYuzQYi6VV7tc%2BTBFCOlhuZkcrh6duvFX2W5GOAF0Jnb%2FsKemJInArpkzkq58fCW1cySUuYyKf12Qm%2BI4ICyC2BqNnQaKL%2FQrwhoQK0My3q60QfrrzR%2FkPRMcOfoBOSac6b34X%2FOn6kMDD4eKPyl6Dxi%2FIAmcTcwOmnMsWNb2ZDKEhDfdGsOCM0Lyvj%2FdE6Olz7psgRILRBhAVLlYd5H8V56I6TNCPKrfxFbAs5nb9E78LIu%2BzcxT0u4O%2FdLQh%2FRiVOr%2Fy6B4StnECf1MibgbVaXy4deaowdo8VSKuP%2BKyuhK0kBde%2BSndK%2FxX6dKxWQaft3Z%2F5LLIGLErzhoiBYOkjAXmR8odo1xvJa8ajn%2BPehZFKofvjQhlBwSdAXr8TAixMhWlWJI2xuK7sddPoxAIhFwhoWn9TdpkyYuz6VscGME5DyPDPafEyda%2FRp9CFvVQA5K9JccrvWNvSRGVVuMs20DSO1bujIKP2H8%2FY1C8WNma5Ry4%2FLAgT%2FdaVrHwn1dagUMAK0p08Kw10WtESbOo6EdnMZ4YR%2FiE68XgxB30Eg%2FoQT3n76Ly0UANy%2BjL9ytxT8FRUY3ZmEfjcCvyMdWvntEGV5ltJnwLejvq3sVvXxSkw55%2FmvAY6pgF8YSo%2F3wtiUDqLtrmKdnUaQ49hz2c%2FQalM1GLoAcP5Wm5m4lIaYYi11wO2WRglXXwSvyE8Tsn%2BjhVBByjKGeixCyH8LXUYYVApsxgIiq82z5923683tfoXWiA4QFw0q4YcUkwi3eNlJOicllmiLMC2phcTtojPpMNiiNSYU1gu3m1ShdehMsc8Wu509FJqwSCgwyeV4mEaG1xqINCFAWkTevFBh9F%2F&X-Amz-Signature=67867c0fd4549ac4bd4eeee9d54d72bb987540b8fcff76a2a6d0d7b74a23f466&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVEO54G3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFUWNF37Y5KYi42ldSDHAKrMpv9LchRyHcH0I%2FsH6b9qAiArVMc%2Fz9luMS2potVCw30jFx61uKaYAmoZnzQKtdz1vCqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgjI5A%2Fmnqw277NjBKtwDtMHJwXsPWC75ZfYuzQYi6VV7tc%2BTBFCOlhuZkcrh6duvFX2W5GOAF0Jnb%2FsKemJInArpkzkq58fCW1cySUuYyKf12Qm%2BI4ICyC2BqNnQaKL%2FQrwhoQK0My3q60QfrrzR%2FkPRMcOfoBOSac6b34X%2FOn6kMDD4eKPyl6Dxi%2FIAmcTcwOmnMsWNb2ZDKEhDfdGsOCM0Lyvj%2FdE6Olz7psgRILRBhAVLlYd5H8V56I6TNCPKrfxFbAs5nb9E78LIu%2BzcxT0u4O%2FdLQh%2FRiVOr%2Fy6B4StnECf1MibgbVaXy4deaowdo8VSKuP%2BKyuhK0kBde%2BSndK%2FxX6dKxWQaft3Z%2F5LLIGLErzhoiBYOkjAXmR8odo1xvJa8ajn%2BPehZFKofvjQhlBwSdAXr8TAixMhWlWJI2xuK7sddPoxAIhFwhoWn9TdpkyYuz6VscGME5DyPDPafEyda%2FRp9CFvVQA5K9JccrvWNvSRGVVuMs20DSO1bujIKP2H8%2FY1C8WNma5Ry4%2FLAgT%2FdaVrHwn1dagUMAK0p08Kw10WtESbOo6EdnMZ4YR%2FiE68XgxB30Eg%2FoQT3n76Ly0UANy%2BjL9ytxT8FRUY3ZmEfjcCvyMdWvntEGV5ltJnwLejvq3sVvXxSkw55%2FmvAY6pgF8YSo%2F3wtiUDqLtrmKdnUaQ49hz2c%2FQalM1GLoAcP5Wm5m4lIaYYi11wO2WRglXXwSvyE8Tsn%2BjhVBByjKGeixCyH8LXUYYVApsxgIiq82z5923683tfoXWiA4QFw0q4YcUkwi3eNlJOicllmiLMC2phcTtojPpMNiiNSYU1gu3m1ShdehMsc8Wu509FJqwSCgwyeV4mEaG1xqINCFAWkTevFBh9F%2F&X-Amz-Signature=ce59e35f6182361f6ece58f23eb92de7233b9ec62486b89c97b99ddbc1911388&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVEO54G3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFUWNF37Y5KYi42ldSDHAKrMpv9LchRyHcH0I%2FsH6b9qAiArVMc%2Fz9luMS2potVCw30jFx61uKaYAmoZnzQKtdz1vCqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgjI5A%2Fmnqw277NjBKtwDtMHJwXsPWC75ZfYuzQYi6VV7tc%2BTBFCOlhuZkcrh6duvFX2W5GOAF0Jnb%2FsKemJInArpkzkq58fCW1cySUuYyKf12Qm%2BI4ICyC2BqNnQaKL%2FQrwhoQK0My3q60QfrrzR%2FkPRMcOfoBOSac6b34X%2FOn6kMDD4eKPyl6Dxi%2FIAmcTcwOmnMsWNb2ZDKEhDfdGsOCM0Lyvj%2FdE6Olz7psgRILRBhAVLlYd5H8V56I6TNCPKrfxFbAs5nb9E78LIu%2BzcxT0u4O%2FdLQh%2FRiVOr%2Fy6B4StnECf1MibgbVaXy4deaowdo8VSKuP%2BKyuhK0kBde%2BSndK%2FxX6dKxWQaft3Z%2F5LLIGLErzhoiBYOkjAXmR8odo1xvJa8ajn%2BPehZFKofvjQhlBwSdAXr8TAixMhWlWJI2xuK7sddPoxAIhFwhoWn9TdpkyYuz6VscGME5DyPDPafEyda%2FRp9CFvVQA5K9JccrvWNvSRGVVuMs20DSO1bujIKP2H8%2FY1C8WNma5Ry4%2FLAgT%2FdaVrHwn1dagUMAK0p08Kw10WtESbOo6EdnMZ4YR%2FiE68XgxB30Eg%2FoQT3n76Ly0UANy%2BjL9ytxT8FRUY3ZmEfjcCvyMdWvntEGV5ltJnwLejvq3sVvXxSkw55%2FmvAY6pgF8YSo%2F3wtiUDqLtrmKdnUaQ49hz2c%2FQalM1GLoAcP5Wm5m4lIaYYi11wO2WRglXXwSvyE8Tsn%2BjhVBByjKGeixCyH8LXUYYVApsxgIiq82z5923683tfoXWiA4QFw0q4YcUkwi3eNlJOicllmiLMC2phcTtojPpMNiiNSYU1gu3m1ShdehMsc8Wu509FJqwSCgwyeV4mEaG1xqINCFAWkTevFBh9F%2F&X-Amz-Signature=05affff1c953af19fdfffe26449dfc661c3a3ee79a4e132bc94ce8ef2369a738&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVEO54G3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFUWNF37Y5KYi42ldSDHAKrMpv9LchRyHcH0I%2FsH6b9qAiArVMc%2Fz9luMS2potVCw30jFx61uKaYAmoZnzQKtdz1vCqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgjI5A%2Fmnqw277NjBKtwDtMHJwXsPWC75ZfYuzQYi6VV7tc%2BTBFCOlhuZkcrh6duvFX2W5GOAF0Jnb%2FsKemJInArpkzkq58fCW1cySUuYyKf12Qm%2BI4ICyC2BqNnQaKL%2FQrwhoQK0My3q60QfrrzR%2FkPRMcOfoBOSac6b34X%2FOn6kMDD4eKPyl6Dxi%2FIAmcTcwOmnMsWNb2ZDKEhDfdGsOCM0Lyvj%2FdE6Olz7psgRILRBhAVLlYd5H8V56I6TNCPKrfxFbAs5nb9E78LIu%2BzcxT0u4O%2FdLQh%2FRiVOr%2Fy6B4StnECf1MibgbVaXy4deaowdo8VSKuP%2BKyuhK0kBde%2BSndK%2FxX6dKxWQaft3Z%2F5LLIGLErzhoiBYOkjAXmR8odo1xvJa8ajn%2BPehZFKofvjQhlBwSdAXr8TAixMhWlWJI2xuK7sddPoxAIhFwhoWn9TdpkyYuz6VscGME5DyPDPafEyda%2FRp9CFvVQA5K9JccrvWNvSRGVVuMs20DSO1bujIKP2H8%2FY1C8WNma5Ry4%2FLAgT%2FdaVrHwn1dagUMAK0p08Kw10WtESbOo6EdnMZ4YR%2FiE68XgxB30Eg%2FoQT3n76Ly0UANy%2BjL9ytxT8FRUY3ZmEfjcCvyMdWvntEGV5ltJnwLejvq3sVvXxSkw55%2FmvAY6pgF8YSo%2F3wtiUDqLtrmKdnUaQ49hz2c%2FQalM1GLoAcP5Wm5m4lIaYYi11wO2WRglXXwSvyE8Tsn%2BjhVBByjKGeixCyH8LXUYYVApsxgIiq82z5923683tfoXWiA4QFw0q4YcUkwi3eNlJOicllmiLMC2phcTtojPpMNiiNSYU1gu3m1ShdehMsc8Wu509FJqwSCgwyeV4mEaG1xqINCFAWkTevFBh9F%2F&X-Amz-Signature=220ffc806b81e7ba590eb91db59723b764c60afeee1c7b75a0abb09e2b4ce0e6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VOW65U6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCRXLn2TM4jw7h6KAgZpiy4%2BvZvSsNRqxhoYx0w5jrxfgIgUpOQsSJHfucqK2xBgrv%2Buhaziz2viAl6cwvqzGiodO4qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKILKu1zgBtn5Qd2gyrcA%2F0zA%2B3kSU32rnrdNYxqZzJFs0MkCtqxNDLELgUjYeRlKKgoWlKlJbPwNEamQ%2BeX4gRwHQAFDOHA9WVGBLz13YRIVtvDWLab47den0rN8nOLAc6jpq9fBNQP4doeu1DDL9w%2FXuYTmnP3E3AK1bbDdNvTcyV7IpBBz7eIPEwnRuR77JTlw650pbczSDJk2S31oxSjCVXR05cu3FUywr0NBXDHvjZtBkMypU2XV8724wGBdecpYQDrdgx8v7WHeLnmwLAjio%2FqT%2FXilKMOlJXmYj%2FkQ1mbJUfHrZoorV5ehRtArSGWigUm7XgXMv9WNrG8DmoMbtWLMqYCsspAg%2FF8WcAnAO%2BC6Ainak4pgPRDcMNedGCPs8tn7Cmio6hJAfAAQWSJ4C8ULO%2BfLA%2BcNBurLZkxWAistBKYHFWkf0XZQyL1d%2BzrLKjjNbSoxDIkWIQ%2FzC1z6uOVCTPeK3L5cH79xHMzBkrUpAYHc%2FfD2dDrdg9bmcCwuTZnDpWVKOO47StYGxqXiEUDU3dhng3LBRH7X2RZeyQYCLzQaQmzJOhfXcwL9jrgMp4u9TB1G5E%2FGLMHPz%2FpIVsIUQ09wwJASJ5mVHAOlk7S7nHtAmTGv2fwWKK3JrKgfyvwD0MYh1a3MNOf5rwGOqUBy4BqeIzbIwejVdanzEoUVRZ3nclrefX8EzWC092tJMBxvsvI2EJIN487s6RBwsoQBws%2Foj5%2B%2BtxmO%2FWPw1OOP9VASFkSFuAyRxKyVZDfMmxUZ4AKDFD9K7V%2FDMEUAm0TzGzov50Rzu7ieo2ic5wpSerAyZwwrrY2GIT9cOMRXgo0LCkJottfZ0NnMuSVV4FelEHUMYuyjXwutxb1LEQ3%2BeBjcbNv&X-Amz-Signature=0856c0d5600dbdc5913ec3bf16b21a299de23d001f23500a222353b83d51cac5&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TGRXLES%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIATJffr34t97TNM5TBVyCyaByM%2BPmnO%2FmK0M8h1JJfVcAiAv4x%2FsuUkAQjTHm61RoTzB5WqV90RCX4N%2BWIYLSqh32yqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWAxLKmvujPJwMQOOKtwDw0Dp9i6BaA8Ah2zE7ZZqZu%2FdAPUqI4q%2Fh%2B9vuBmFd%2Fqf9fwQuXcVvpMIkKhtLYL2jTPMsr%2FmZ0i%2F4ff2A%2BdDm7nDI67nL0wOda9Thpol2Ve1Ie6dB7BMD0yP%2BDNfJtQ1%2FwAPyL1Ss2JXpAhB%2F9OwGt7C0NGt8gIPhssu%2BKsIUlI%2Fm1Gp2ay%2F3xiVtlzObDxITPnto3Jco530c7yqWx%2FbPKPHM81yqIoMTFx0m9zjIO5U9TBYa2uYmlxcC6SqxKcE6pUtGYTNyOuhETpWIQd9XTr4h%2B5e%2FD8t01Mz2d7m3VC7h1Z62yRbXzony5xsS0c5dH4bk1Cf6xeFwPIx0SPk1wAR%2Bi4LQoD1p9XioVU%2FB7RqgBkuQRbsjUJULLr9kHtmku%2FKyJOPCpKBE5%2FTgBHcZnpgsQfy3u4huTSU2xBM5JHXVF7qKEB5P8eWdR6d0%2BcposdtKUA1C5y65OAMMBTr3w0q60H%2FCXY98h9EIP0Rk6SOuMHTNSRcfHO%2BnA0rDtX8rhCejcEfpIHfOwTr7zH6%2BtVRY2nCZ42MwR5Y%2BUI6gsaSbfrpRf7dJl7Gr4md3HANQDiCgKkhLKqLkjm6gzQroYjxn%2Fi4me045L4aJUPtjMiQdAHlg5tPf5QBWaIwqp%2FmvAY6pgHqplespCWDoM209D3yDpnMY4B%2BdQMO%2BtCn1NOY5znNv0%2F3Lym3IrjME9tYuEUoybL9j1DfzBTos1xLVBeoHj%2FWTUvax%2BaQopGyN%2BdhReH4eczjMlWGTQ89KmPWKde52ak68c%2FzA%2FnBGwUsfCPqjhE5nbailVJpGP4er42DmsiZVEWbHeP2D8ZvENdqB7ycCatxmD1MqP7OBZUnVpPTm0APWymGtBKa&X-Amz-Signature=24558371002f858284b38306def2712d2a4df778faf6eb4087e9bb67d70a5867&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVEO54G3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFUWNF37Y5KYi42ldSDHAKrMpv9LchRyHcH0I%2FsH6b9qAiArVMc%2Fz9luMS2potVCw30jFx61uKaYAmoZnzQKtdz1vCqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgjI5A%2Fmnqw277NjBKtwDtMHJwXsPWC75ZfYuzQYi6VV7tc%2BTBFCOlhuZkcrh6duvFX2W5GOAF0Jnb%2FsKemJInArpkzkq58fCW1cySUuYyKf12Qm%2BI4ICyC2BqNnQaKL%2FQrwhoQK0My3q60QfrrzR%2FkPRMcOfoBOSac6b34X%2FOn6kMDD4eKPyl6Dxi%2FIAmcTcwOmnMsWNb2ZDKEhDfdGsOCM0Lyvj%2FdE6Olz7psgRILRBhAVLlYd5H8V56I6TNCPKrfxFbAs5nb9E78LIu%2BzcxT0u4O%2FdLQh%2FRiVOr%2Fy6B4StnECf1MibgbVaXy4deaowdo8VSKuP%2BKyuhK0kBde%2BSndK%2FxX6dKxWQaft3Z%2F5LLIGLErzhoiBYOkjAXmR8odo1xvJa8ajn%2BPehZFKofvjQhlBwSdAXr8TAixMhWlWJI2xuK7sddPoxAIhFwhoWn9TdpkyYuz6VscGME5DyPDPafEyda%2FRp9CFvVQA5K9JccrvWNvSRGVVuMs20DSO1bujIKP2H8%2FY1C8WNma5Ry4%2FLAgT%2FdaVrHwn1dagUMAK0p08Kw10WtESbOo6EdnMZ4YR%2FiE68XgxB30Eg%2FoQT3n76Ly0UANy%2BjL9ytxT8FRUY3ZmEfjcCvyMdWvntEGV5ltJnwLejvq3sVvXxSkw55%2FmvAY6pgF8YSo%2F3wtiUDqLtrmKdnUaQ49hz2c%2FQalM1GLoAcP5Wm5m4lIaYYi11wO2WRglXXwSvyE8Tsn%2BjhVBByjKGeixCyH8LXUYYVApsxgIiq82z5923683tfoXWiA4QFw0q4YcUkwi3eNlJOicllmiLMC2phcTtojPpMNiiNSYU1gu3m1ShdehMsc8Wu509FJqwSCgwyeV4mEaG1xqINCFAWkTevFBh9F%2F&X-Amz-Signature=23fcaa5d587119aac077549cb240161661a1ee7cd3cd85fb9ec2761e240d88fd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVEO54G3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFUWNF37Y5KYi42ldSDHAKrMpv9LchRyHcH0I%2FsH6b9qAiArVMc%2Fz9luMS2potVCw30jFx61uKaYAmoZnzQKtdz1vCqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgjI5A%2Fmnqw277NjBKtwDtMHJwXsPWC75ZfYuzQYi6VV7tc%2BTBFCOlhuZkcrh6duvFX2W5GOAF0Jnb%2FsKemJInArpkzkq58fCW1cySUuYyKf12Qm%2BI4ICyC2BqNnQaKL%2FQrwhoQK0My3q60QfrrzR%2FkPRMcOfoBOSac6b34X%2FOn6kMDD4eKPyl6Dxi%2FIAmcTcwOmnMsWNb2ZDKEhDfdGsOCM0Lyvj%2FdE6Olz7psgRILRBhAVLlYd5H8V56I6TNCPKrfxFbAs5nb9E78LIu%2BzcxT0u4O%2FdLQh%2FRiVOr%2Fy6B4StnECf1MibgbVaXy4deaowdo8VSKuP%2BKyuhK0kBde%2BSndK%2FxX6dKxWQaft3Z%2F5LLIGLErzhoiBYOkjAXmR8odo1xvJa8ajn%2BPehZFKofvjQhlBwSdAXr8TAixMhWlWJI2xuK7sddPoxAIhFwhoWn9TdpkyYuz6VscGME5DyPDPafEyda%2FRp9CFvVQA5K9JccrvWNvSRGVVuMs20DSO1bujIKP2H8%2FY1C8WNma5Ry4%2FLAgT%2FdaVrHwn1dagUMAK0p08Kw10WtESbOo6EdnMZ4YR%2FiE68XgxB30Eg%2FoQT3n76Ly0UANy%2BjL9ytxT8FRUY3ZmEfjcCvyMdWvntEGV5ltJnwLejvq3sVvXxSkw55%2FmvAY6pgF8YSo%2F3wtiUDqLtrmKdnUaQ49hz2c%2FQalM1GLoAcP5Wm5m4lIaYYi11wO2WRglXXwSvyE8Tsn%2BjhVBByjKGeixCyH8LXUYYVApsxgIiq82z5923683tfoXWiA4QFw0q4YcUkwi3eNlJOicllmiLMC2phcTtojPpMNiiNSYU1gu3m1ShdehMsc8Wu509FJqwSCgwyeV4mEaG1xqINCFAWkTevFBh9F%2F&X-Amz-Signature=be6bf3ae27f7e748c4740a0f32c95916d5cc75d614852fd925de79751ca850bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVEO54G3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFUWNF37Y5KYi42ldSDHAKrMpv9LchRyHcH0I%2FsH6b9qAiArVMc%2Fz9luMS2potVCw30jFx61uKaYAmoZnzQKtdz1vCqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgjI5A%2Fmnqw277NjBKtwDtMHJwXsPWC75ZfYuzQYi6VV7tc%2BTBFCOlhuZkcrh6duvFX2W5GOAF0Jnb%2FsKemJInArpkzkq58fCW1cySUuYyKf12Qm%2BI4ICyC2BqNnQaKL%2FQrwhoQK0My3q60QfrrzR%2FkPRMcOfoBOSac6b34X%2FOn6kMDD4eKPyl6Dxi%2FIAmcTcwOmnMsWNb2ZDKEhDfdGsOCM0Lyvj%2FdE6Olz7psgRILRBhAVLlYd5H8V56I6TNCPKrfxFbAs5nb9E78LIu%2BzcxT0u4O%2FdLQh%2FRiVOr%2Fy6B4StnECf1MibgbVaXy4deaowdo8VSKuP%2BKyuhK0kBde%2BSndK%2FxX6dKxWQaft3Z%2F5LLIGLErzhoiBYOkjAXmR8odo1xvJa8ajn%2BPehZFKofvjQhlBwSdAXr8TAixMhWlWJI2xuK7sddPoxAIhFwhoWn9TdpkyYuz6VscGME5DyPDPafEyda%2FRp9CFvVQA5K9JccrvWNvSRGVVuMs20DSO1bujIKP2H8%2FY1C8WNma5Ry4%2FLAgT%2FdaVrHwn1dagUMAK0p08Kw10WtESbOo6EdnMZ4YR%2FiE68XgxB30Eg%2FoQT3n76Ly0UANy%2BjL9ytxT8FRUY3ZmEfjcCvyMdWvntEGV5ltJnwLejvq3sVvXxSkw55%2FmvAY6pgF8YSo%2F3wtiUDqLtrmKdnUaQ49hz2c%2FQalM1GLoAcP5Wm5m4lIaYYi11wO2WRglXXwSvyE8Tsn%2BjhVBByjKGeixCyH8LXUYYVApsxgIiq82z5923683tfoXWiA4QFw0q4YcUkwi3eNlJOicllmiLMC2phcTtojPpMNiiNSYU1gu3m1ShdehMsc8Wu509FJqwSCgwyeV4mEaG1xqINCFAWkTevFBh9F%2F&X-Amz-Signature=5c8fe4f18439dac0b39f3496f483cf3fb64af86c9d5c20e4debe002bfcd56e9b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXPCAXVD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCFhw6DTwf9zih766I6YkbW082oR3mnz%2FbI9TIylbMLcgIgPCYqgg%2BdXD%2B1SxzWZFLtb3ovdJZ6CNc0b0fnInh%2Fb8oqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMHG2ZPDqihy%2FyfNqCrcA49qKa7Frd1rFZ%2Bjl0V%2FbmZ74i5hZz7W9QiihIfsBs5Rfhn9gE5xU8%2BJ59dc530dF6kqHVVQTbU6SOtA1dMcPp1UIJ%2FwDPnBT5SmutUK0zEEqvSbsVEZQ1CM6mrxftd5COqREhAEtIGYN76aPTUzFYuFjlnNnFgsKAHEZKibUBTLwtCvM3NCDBK8lih5xwr9b9NRJVRGEQ87AqPfeBPOkBIqr%2F%2FvIFOLYfvVBOdSDfL%2FdCKQmB7NQTMdgxkDI4R1Yeu5d822Z2NvaQsHdcqWwe1DG%2B9gaVpwzZNGJapBtC79AfGgHKqo9BVj%2Bpgcu0565fOULRM6mo6x%2BqltgG5KqGBeh%2BfvYEYXo0P7%2FKVAUcM%2FlPR4gXv75sqb7E76uWU4psI7pCOyfxfrnUVg4tdK33lQNU5ChHJfF1xXdmGjFtJRYVY1SOI6IUj7PzWgVYD2jLtz2CgNE3c%2B%2BAFfvkllk%2FLnD6JzXHp7tqZEoRf0FAwJ4r09CpDJeHg9zHgA4sgrO634PsbGo6gV1SL%2F4nJInDQ0jl5xdXTEJ%2BaXtrCXR27kVS4oMzAhwWZAsRrAW0lAEde9fZVDgNqoHkyLIr9Lnv4pMxeTCRtmkcaXkqlZPBQLKfuxJxp4xzN4kaFRMN265rwGOqUBko7YD8Aph%2BCEUFhSC1Gv%2BY5%2FvkFsoWPhFG8fpUBo%2BdEkH2CavJdD52m4tl6vp3%2BPgzZMj0FhfFxLzURRvwMLxILqf%2FxKsiZztqePLxy90yGhO8G29v%2FPoQVw4Nn2oK9cys%2FUBG0kaoYQFAYbGgF1QX%2BeIgg9IlEjCTjY1HdeuLNpKlT3KRjZh8rN%2F3MODdFgicZiO83UXhiG%2BtcsDiU%2Fdo9IUEvi&X-Amz-Signature=812411ca5e9bca7810499f30754639826cb18fa5054b830ac0bbf3de4faf9b08&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7LS36JO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCID%2Bb%2BasqhNs6Wks0u15sU8ZhtuyAzuOfD8qgwu3wdmvGAiBIbt4rJCE4v6zUqJ97sR3vqjvgrc4%2FcDLrC%2BeRClfF3iqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3tK8Mgo27noNqrSnKtwDFvXd%2BmLwT5c62gok0OqZw9gnBtnXfoGAgMrNwxngcHAuO%2FBdsLvyANh30uTNiPc0eq51RMPbTeQcOBZYib2wp3ygmX29UQWOnMAj2IGzbAz2dpeolzfDRKO%2BlX8HRs%2FyyfZXx4%2FRUKuAZV9Dj2u%2FHNonzdbEb%2Fme4%2Biv07tVWJYEF22LP8UTg7Co2l7NeIT7UlnPu1GJwNLLHcUmH9%2BgdX%2BHXoJ7ywhujsoxizjUlEGnRHir5H7TH6w1bQzZ6LZd%2BGwhHc1rRBHZAfbibTvvg4vYyrq3k2KJ%2BiITV5DNyI84BbQiXv6qd6CJ58JJPxiV5XbhXIN7WZgKqJFcrjw%2FKaZ1SoD86vItt7g7xY%2FUpMYF5NY9JjbdfXcyRuscTk%2FjmA8C%2Bo64Bf6RcexqREOTy%2FV%2FNXbWhJ7stEFWL6izyBxju2nZYvfFew43AbSnrm%2FhCmG4Fd5e4f%2FiaklT0a1GwmENSAYGOb22NutU%2Fa20fiIIys4IaQCal0Ei8gCFwK7fcDhYa07wPeTI4WOv91X77TqpBKXKK1p%2FjF3r4zw6txvzF4QERd8n4tbFyFF6z4WbN15s5ecF5n2QVTyvEKwx9EIUZNnnGfHhONO24rz8k%2BiDaiTX2F%2BkjUHsgEkwwZ%2FmvAY6pgHfjbQ4sU1zXDDvsSeVTiQKYHm0Ck7puQA%2BWSn4WedrZTKkZ5dQGOZgLIKQoxvA%2BzoDPyTiQkVLWZYoiDOguqADf06SVH8ws%2FHnWu9G59gE4RJbePHIB2IFM8XS4oMxAFVcDG9Fn5R3mQ%2B7TuOfulxfyC0FfjDr75FR591qMHawktjosAfMhzksEDKLnLujhDp6dZnwRw%2FTWVDKD7AKhGVEGYDIHcVf&X-Amz-Signature=7fbed4a5938ce42a5bf3daedb30696a0665636604bcb01a10312f5e43aa9c3b0&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHC3VFFJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDuHyarJKck8AucuUbtWS%2FtqolGAWy3nPxnVPMQ0M55qQIgb2GRJ7xY8mK6D6hGqedHB5s8CIOKfnJzoqnaenUrNVYqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDENhjGOHaEHgaL%2BlBCrcA8NPv%2BX7%2Bb8aco1LTTJ94vQuko1htRcSdIgnTgn6Yyy0iIFWD%2Bm7zii1tcqzVXNKbzRUiZap7jHGWHk03Ix%2FT77pCm%2BHh1QGQXKJa4OJjyLRmhSYV6ya7wsilFGwsWWMjgtPLu9zD4fgfGWCjleA29quU%2BOHXo54VcIulZoL5BWcvDg3IwZ9AXZcA0QimEb3dk1iqjeN45DQIxXyWVftFQOstugm1v59Ptks2nMLDGrVjgjHuVh3mv6eqqyEaFKi%2B%2FZRG786OvHHnl8ZfsvoUpUjsSO%2BVFQmNbHiwLiwVWlGJ24mIoUjykrlXrAp7qpKKz1lyNDiYPAUmallgUcXU2ZKpGfucd4EPEHkNPameB%2FcFio90BBaXicR3dHQBy8JIbQsywsZEumyfVFJjhE0gVLUlG2UHjnIuisxy5QFjGzJARj1HAsVpUe%2Bgu5fGQkN2x16vdYFFCVFngY6jR94TTPmmdKKOQLmHtqyXX%2BrTr9IMnjR23JxDdO84FpZPN4ZKNODtrnbGjlIUxSLA5OtKgOpkNxILE5IJtiFfhO4xjSKqXdNLBiDH9ZsM5C4KsbQhfBMgfrs2RCxDHBKUQUa19pDipPYHqMqzIwNc7sGlx17ioHtaETlXgYjzTQrML6f5rwGOqUBVzbqaPGZLDNx8mckZTOTJv11Ye2uRY%2FWJdok8otradmakrBrOaU8c765a1up9R4wu%2FGsY98gKCsVAL0LW1XEHCmUxfybrXYHR%2FY162TLBh6Aqsl7eEPMxg228hEHKx7rbC3iAQFWVztVP%2BJX7KD9bZTPv1R1dSGEkyk9Y7LlGMoiKOPJ1U6O1enducHwMvp1KPQdXT03hww8kMAhIR4qRf8flwon&X-Amz-Signature=8c800706e7a62a980bcd4e90e6de290c089b3bd07c6655e3f3b9e94941de3b66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VC7B6OHC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIGGvZ50lag6AnM6NX%2Fu8EurX1dURghNwjEVP6O6BTujmAiEAg1w2cC8heXSlKwgITqe1EV4bRKEZuAN8leqTkpPs8WkqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8KKGzMMbJmhacksyrcAyla868oq6Wd0wdRi7qe7tZoG6C3hYDwjlaIMAn%2FvHNNI2g3SIzRqyigMwF7FyLeq6H095KTCQDXmMAd9HupeQ68OrzxI6NphvfZ4WomdGBelDvYFo2ud1Q7qrkTWBMI4r4CkYF7W0CPutMbi9%2B%2BrMDTaVZaeKyVcPV8tpyhYz0iMunsHHEtria2FAfwVhMAqASA12Opk6g1h%2B5sRUMG%2BSrJP5yeTkT0o6KTvEeCuC%2FsRaozU2p6lF4D6RuEuX33CqO4JlloQl8F4xY9VADlUR9E2mpFsPVKef%2Fz3fbsAoOx31Ax6nGp%2Bh7d3ojHtTa%2FeY4Hcov5Eic%2BFsXlKN62Y94k7lMQLSUQs0%2FH9CtWPz%2Fs9nGjFAFLWjI0z9FBqyGkTyRd8e0v%2FV2GsiWNJYsT9wEAjhhyxi%2B81WclfLNyoI0qS9BxykZyiZimd3oHbKVpXefrHQ4baDxyfPeChlcESZ%2Fudu0miZa%2FMP4gPbmcrJtrrjge%2Fa77xAUlFcu9ChcE4zOtDCnVx9UvtP18n5cjQfJAKeOChhn19HO%2BuNC1k2Q7UUhem8AUCAguqT5P1suso2OVZH91RJJzK1eyLsPau8g9V62z5%2BK3rLNgkvVz%2BJYjecRY0hj%2FvDPabN%2FFMKSf5rwGOqUBvYjyDtCZDrH5jPq7NHJMMLqj%2FL8uH56gnvL365x679UYvFHRLeliMjnqQ%2BKYDhoc2OK0grlvQ6ZQhDqgIJpLGaI4gipO8B7Wbzmp0Hotzfcrncc7M8blcLfod4D8atOdq89rB1YG9BrXUSXVD7kMRW%2BgvWEUiuWWWfXXC91%2FrTGpfwgMBqF0kKXXdG4JlMOwc2aDbEpaQ258Eg8EIqVfj%2F78ufc1&X-Amz-Signature=78c6c0aa080bdc85c3c4685884b324ce16b221b1dfe2f7a7871e7b4487c8da0a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VC7B6OHC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIGGvZ50lag6AnM6NX%2Fu8EurX1dURghNwjEVP6O6BTujmAiEAg1w2cC8heXSlKwgITqe1EV4bRKEZuAN8leqTkpPs8WkqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8KKGzMMbJmhacksyrcAyla868oq6Wd0wdRi7qe7tZoG6C3hYDwjlaIMAn%2FvHNNI2g3SIzRqyigMwF7FyLeq6H095KTCQDXmMAd9HupeQ68OrzxI6NphvfZ4WomdGBelDvYFo2ud1Q7qrkTWBMI4r4CkYF7W0CPutMbi9%2B%2BrMDTaVZaeKyVcPV8tpyhYz0iMunsHHEtria2FAfwVhMAqASA12Opk6g1h%2B5sRUMG%2BSrJP5yeTkT0o6KTvEeCuC%2FsRaozU2p6lF4D6RuEuX33CqO4JlloQl8F4xY9VADlUR9E2mpFsPVKef%2Fz3fbsAoOx31Ax6nGp%2Bh7d3ojHtTa%2FeY4Hcov5Eic%2BFsXlKN62Y94k7lMQLSUQs0%2FH9CtWPz%2Fs9nGjFAFLWjI0z9FBqyGkTyRd8e0v%2FV2GsiWNJYsT9wEAjhhyxi%2B81WclfLNyoI0qS9BxykZyiZimd3oHbKVpXefrHQ4baDxyfPeChlcESZ%2Fudu0miZa%2FMP4gPbmcrJtrrjge%2Fa77xAUlFcu9ChcE4zOtDCnVx9UvtP18n5cjQfJAKeOChhn19HO%2BuNC1k2Q7UUhem8AUCAguqT5P1suso2OVZH91RJJzK1eyLsPau8g9V62z5%2BK3rLNgkvVz%2BJYjecRY0hj%2FvDPabN%2FFMKSf5rwGOqUBvYjyDtCZDrH5jPq7NHJMMLqj%2FL8uH56gnvL365x679UYvFHRLeliMjnqQ%2BKYDhoc2OK0grlvQ6ZQhDqgIJpLGaI4gipO8B7Wbzmp0Hotzfcrncc7M8blcLfod4D8atOdq89rB1YG9BrXUSXVD7kMRW%2BgvWEUiuWWWfXXC91%2FrTGpfwgMBqF0kKXXdG4JlMOwc2aDbEpaQ258Eg8EIqVfj%2F78ufc1&X-Amz-Signature=ab62d09befeca8ce329a8825e43f44f88f2305c78168670ef30240eafd03728b&X-Amz-SignedHeaders=host&x-id=GetObject)

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
