

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N2RCIWX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICTAhE%2FS1Bh6SWEpVp0ZBlcerl85xRWxchMqDBdj5OEhAiEA3%2FB9KitY7X5Uwl%2BTOtI9u%2F%2BWRIOZ6NgVI7H0hjS6j%2FAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDueATV69YtXrGVfSCrcA%2F7cMQOMLXHA7w1Q%2BNeP%2BlOBUNLcOSOx%2Btjt9lHs%2FCfaOIKj8K%2FwKC8pDc6MExTlqtqHeZakImxyRL7lJ%2FlqVuv58pim98ZFcu4NNQuFwgxzRVU2w8feutigSWOyPOHykJX6MsCII8eJctZ87BkND418VXVcI0ON1fKtpHuXMfZzSdqYYVT3VBJFejs3kw55y8qxpp4PshaE%2FC3EyFteFuovTNzlHK2pvHQYh%2FQeVdItF5dtqZSEB%2Bqr6bV2CAI0vYSkGb8wdYaqWb2TOkuHiazh3ayazVUKU2j6iRy0i8XN3Y%2BQDtC29jVFJpGuO5%2FkR4LjerYQqRH%2FylwrGM3OOmMdfAKku9onXH7YjXQsURMyhukfMULGS318DanB9DQA1KbizhTh%2BIxfd9Bskm4FRnmmc%2FYI6heHT761omS0ikqabsE9jZO2KNQ8SsCT2uKK0qqUgab64m0UgFtIjkDyjX3mqsUA6Fy3vKVQSPpyaV%2FXxmAiInm9aGNOGQzFXHstyhwZRgjGZkbqu%2FcpzOr5t0ccick0VLOeAGF4R5eGrw7JBtvlnn3%2FLC8Uo7U9fVeGlvHaeHaPbFobKJD3mHs24J7OWZYNHURbR4%2FA0A1zFpZ2VHRGeBgoKf7xInxfMM%2B%2B%2FbwGOqUBu%2F81S2ZSlu3mYj6t359rPbdZvUdyeTyTUfdetpQyHk4lEO8QV998I%2F4wuChL9eOn0DH1IAi87xlP2LZvarO6kDIbPVn3xuXSnSoww74oH2ntVGDSV3bq49N463HvosuUXEewJ8Q4kP0LGl8FPGMt84CMnsis7c%2FrkgBADpHeaWyNt78szqHxKCPD6SAlbGt3qAKGpLTAb89CbeRvqz9Iel%2FrE88u&X-Amz-Signature=f48a9e9861e91778567e321e4b3708848bf97c671e04599b51bcb2e58c532f14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N2RCIWX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICTAhE%2FS1Bh6SWEpVp0ZBlcerl85xRWxchMqDBdj5OEhAiEA3%2FB9KitY7X5Uwl%2BTOtI9u%2F%2BWRIOZ6NgVI7H0hjS6j%2FAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDueATV69YtXrGVfSCrcA%2F7cMQOMLXHA7w1Q%2BNeP%2BlOBUNLcOSOx%2Btjt9lHs%2FCfaOIKj8K%2FwKC8pDc6MExTlqtqHeZakImxyRL7lJ%2FlqVuv58pim98ZFcu4NNQuFwgxzRVU2w8feutigSWOyPOHykJX6MsCII8eJctZ87BkND418VXVcI0ON1fKtpHuXMfZzSdqYYVT3VBJFejs3kw55y8qxpp4PshaE%2FC3EyFteFuovTNzlHK2pvHQYh%2FQeVdItF5dtqZSEB%2Bqr6bV2CAI0vYSkGb8wdYaqWb2TOkuHiazh3ayazVUKU2j6iRy0i8XN3Y%2BQDtC29jVFJpGuO5%2FkR4LjerYQqRH%2FylwrGM3OOmMdfAKku9onXH7YjXQsURMyhukfMULGS318DanB9DQA1KbizhTh%2BIxfd9Bskm4FRnmmc%2FYI6heHT761omS0ikqabsE9jZO2KNQ8SsCT2uKK0qqUgab64m0UgFtIjkDyjX3mqsUA6Fy3vKVQSPpyaV%2FXxmAiInm9aGNOGQzFXHstyhwZRgjGZkbqu%2FcpzOr5t0ccick0VLOeAGF4R5eGrw7JBtvlnn3%2FLC8Uo7U9fVeGlvHaeHaPbFobKJD3mHs24J7OWZYNHURbR4%2FA0A1zFpZ2VHRGeBgoKf7xInxfMM%2B%2B%2FbwGOqUBu%2F81S2ZSlu3mYj6t359rPbdZvUdyeTyTUfdetpQyHk4lEO8QV998I%2F4wuChL9eOn0DH1IAi87xlP2LZvarO6kDIbPVn3xuXSnSoww74oH2ntVGDSV3bq49N463HvosuUXEewJ8Q4kP0LGl8FPGMt84CMnsis7c%2FrkgBADpHeaWyNt78szqHxKCPD6SAlbGt3qAKGpLTAb89CbeRvqz9Iel%2FrE88u&X-Amz-Signature=a5d8fc0c7ddc80c765196fd12d7bf97d132f7463bd44fcc9ed0d8b4a0adc5432&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665N2RCIWX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICTAhE%2FS1Bh6SWEpVp0ZBlcerl85xRWxchMqDBdj5OEhAiEA3%2FB9KitY7X5Uwl%2BTOtI9u%2F%2BWRIOZ6NgVI7H0hjS6j%2FAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDueATV69YtXrGVfSCrcA%2F7cMQOMLXHA7w1Q%2BNeP%2BlOBUNLcOSOx%2Btjt9lHs%2FCfaOIKj8K%2FwKC8pDc6MExTlqtqHeZakImxyRL7lJ%2FlqVuv58pim98ZFcu4NNQuFwgxzRVU2w8feutigSWOyPOHykJX6MsCII8eJctZ87BkND418VXVcI0ON1fKtpHuXMfZzSdqYYVT3VBJFejs3kw55y8qxpp4PshaE%2FC3EyFteFuovTNzlHK2pvHQYh%2FQeVdItF5dtqZSEB%2Bqr6bV2CAI0vYSkGb8wdYaqWb2TOkuHiazh3ayazVUKU2j6iRy0i8XN3Y%2BQDtC29jVFJpGuO5%2FkR4LjerYQqRH%2FylwrGM3OOmMdfAKku9onXH7YjXQsURMyhukfMULGS318DanB9DQA1KbizhTh%2BIxfd9Bskm4FRnmmc%2FYI6heHT761omS0ikqabsE9jZO2KNQ8SsCT2uKK0qqUgab64m0UgFtIjkDyjX3mqsUA6Fy3vKVQSPpyaV%2FXxmAiInm9aGNOGQzFXHstyhwZRgjGZkbqu%2FcpzOr5t0ccick0VLOeAGF4R5eGrw7JBtvlnn3%2FLC8Uo7U9fVeGlvHaeHaPbFobKJD3mHs24J7OWZYNHURbR4%2FA0A1zFpZ2VHRGeBgoKf7xInxfMM%2B%2B%2FbwGOqUBu%2F81S2ZSlu3mYj6t359rPbdZvUdyeTyTUfdetpQyHk4lEO8QV998I%2F4wuChL9eOn0DH1IAi87xlP2LZvarO6kDIbPVn3xuXSnSoww74oH2ntVGDSV3bq49N463HvosuUXEewJ8Q4kP0LGl8FPGMt84CMnsis7c%2FrkgBADpHeaWyNt78szqHxKCPD6SAlbGt3qAKGpLTAb89CbeRvqz9Iel%2FrE88u&X-Amz-Signature=a0d4fb32c6ba83a90b392de4cf1931db3df98d2f0612d1b62caba7c634a69913&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7GQHJ6Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7wId9NQc4AxTB9bVs38HjuZeq4pZaObbPbvcCsXHIxAiEArEQylJWrxoY49fiMq%2FPECZ3a3HNyyCvnLlNj5UMuY7kqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMDXJyX%2F%2BMN9QqZhKircA1hcd5uj1v9CoENHy0GUwHMY4XshA1uW50tvGYuOJ1CCUtDfOT9uQiMzdbP1xKHixNndi2QDiK%2BVORBiuSKo3nCRsNFD%2FSDFdO0DimNJRLPw656xdZxNzx93fjNzf4J6VwIkgANPU6xQ8jptXPz%2FYyYT%2F6Ub4jn7mChYyxdD5q64NEqeUPJoiNTwuRAD03vnTkc7PCpETPyfNyrWaZKCD5tFLAr5m7C23zmBhVr82yMhPOuyjIin%2FiWl3r5pn25m6478eof2uDaAU%2BPQIJhjbJL%2Fi5L%2BYWDxAaZjsAYk0zqoC7p4iqEwhdUGKu7T9qwtqkWgI7cQklP%2FnUDDjolM5bQGXQbW3sYuiQMxCrOy5Fk8JOHRoL5zDPWRMbK93gcugwV5ejjiU%2BTxjBlF8pm0GMvLJJfSlWQcAr%2BaQSCqbMzdjfKMdJtsN%2Fm4ivq7v0deBLtK3NRPBKLNchus9SmaLceZUTEzjQcmnVMCpS1B8v%2FEy5uSCLj4%2BpKDM1j6koL%2BALafI2phHZY4Ai1CsAdpwL5V927PVaMeo3VmsUAINcc1vEhNEeXV9j6IgSg8wL28BznxjtnlZKbyTUeWomOBvBfdu%2FPzoaw8CbquxOFkc%2BCz5Aa3v14Koh8VJ%2Bc6MNju%2FLwGOqUBXFfztU4vQxMmRarCXb7l3aj0n%2FjRQcI69BPHjsypCplneRDknJ4l6ctdI8HuSdd9cCfALANHnSAiUckLTl4pKapBMsUS%2BnwrIFgr%2BDY9CzXqLZf%2BxDVj1USXQx22rJbBg6%2BVG0mYSRYVNGeyVyIz7wkHDJIgze30LZljEqsHUiehI7izxz3Wy2i2aydF1fFcMAR2XgFzaR7rlBtizM3payFVmQKV&X-Amz-Signature=f1669b5d2a96e26f1333fcc8db534be4b51a6c2d59d0dfb06bca4b5345e0ea9b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7GQHJ6Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7wId9NQc4AxTB9bVs38HjuZeq4pZaObbPbvcCsXHIxAiEArEQylJWrxoY49fiMq%2FPECZ3a3HNyyCvnLlNj5UMuY7kqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMDXJyX%2F%2BMN9QqZhKircA1hcd5uj1v9CoENHy0GUwHMY4XshA1uW50tvGYuOJ1CCUtDfOT9uQiMzdbP1xKHixNndi2QDiK%2BVORBiuSKo3nCRsNFD%2FSDFdO0DimNJRLPw656xdZxNzx93fjNzf4J6VwIkgANPU6xQ8jptXPz%2FYyYT%2F6Ub4jn7mChYyxdD5q64NEqeUPJoiNTwuRAD03vnTkc7PCpETPyfNyrWaZKCD5tFLAr5m7C23zmBhVr82yMhPOuyjIin%2FiWl3r5pn25m6478eof2uDaAU%2BPQIJhjbJL%2Fi5L%2BYWDxAaZjsAYk0zqoC7p4iqEwhdUGKu7T9qwtqkWgI7cQklP%2FnUDDjolM5bQGXQbW3sYuiQMxCrOy5Fk8JOHRoL5zDPWRMbK93gcugwV5ejjiU%2BTxjBlF8pm0GMvLJJfSlWQcAr%2BaQSCqbMzdjfKMdJtsN%2Fm4ivq7v0deBLtK3NRPBKLNchus9SmaLceZUTEzjQcmnVMCpS1B8v%2FEy5uSCLj4%2BpKDM1j6koL%2BALafI2phHZY4Ai1CsAdpwL5V927PVaMeo3VmsUAINcc1vEhNEeXV9j6IgSg8wL28BznxjtnlZKbyTUeWomOBvBfdu%2FPzoaw8CbquxOFkc%2BCz5Aa3v14Koh8VJ%2Bc6MNju%2FLwGOqUBXFfztU4vQxMmRarCXb7l3aj0n%2FjRQcI69BPHjsypCplneRDknJ4l6ctdI8HuSdd9cCfALANHnSAiUckLTl4pKapBMsUS%2BnwrIFgr%2BDY9CzXqLZf%2BxDVj1USXQx22rJbBg6%2BVG0mYSRYVNGeyVyIz7wkHDJIgze30LZljEqsHUiehI7izxz3Wy2i2aydF1fFcMAR2XgFzaR7rlBtizM3payFVmQKV&X-Amz-Signature=42f3164d9440fda33f1d400b65a0c3aabfdf3ee5c0d7640a194a00f8c3c8d54d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7GQHJ6Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7wId9NQc4AxTB9bVs38HjuZeq4pZaObbPbvcCsXHIxAiEArEQylJWrxoY49fiMq%2FPECZ3a3HNyyCvnLlNj5UMuY7kqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMDXJyX%2F%2BMN9QqZhKircA1hcd5uj1v9CoENHy0GUwHMY4XshA1uW50tvGYuOJ1CCUtDfOT9uQiMzdbP1xKHixNndi2QDiK%2BVORBiuSKo3nCRsNFD%2FSDFdO0DimNJRLPw656xdZxNzx93fjNzf4J6VwIkgANPU6xQ8jptXPz%2FYyYT%2F6Ub4jn7mChYyxdD5q64NEqeUPJoiNTwuRAD03vnTkc7PCpETPyfNyrWaZKCD5tFLAr5m7C23zmBhVr82yMhPOuyjIin%2FiWl3r5pn25m6478eof2uDaAU%2BPQIJhjbJL%2Fi5L%2BYWDxAaZjsAYk0zqoC7p4iqEwhdUGKu7T9qwtqkWgI7cQklP%2FnUDDjolM5bQGXQbW3sYuiQMxCrOy5Fk8JOHRoL5zDPWRMbK93gcugwV5ejjiU%2BTxjBlF8pm0GMvLJJfSlWQcAr%2BaQSCqbMzdjfKMdJtsN%2Fm4ivq7v0deBLtK3NRPBKLNchus9SmaLceZUTEzjQcmnVMCpS1B8v%2FEy5uSCLj4%2BpKDM1j6koL%2BALafI2phHZY4Ai1CsAdpwL5V927PVaMeo3VmsUAINcc1vEhNEeXV9j6IgSg8wL28BznxjtnlZKbyTUeWomOBvBfdu%2FPzoaw8CbquxOFkc%2BCz5Aa3v14Koh8VJ%2Bc6MNju%2FLwGOqUBXFfztU4vQxMmRarCXb7l3aj0n%2FjRQcI69BPHjsypCplneRDknJ4l6ctdI8HuSdd9cCfALANHnSAiUckLTl4pKapBMsUS%2BnwrIFgr%2BDY9CzXqLZf%2BxDVj1USXQx22rJbBg6%2BVG0mYSRYVNGeyVyIz7wkHDJIgze30LZljEqsHUiehI7izxz3Wy2i2aydF1fFcMAR2XgFzaR7rlBtizM3payFVmQKV&X-Amz-Signature=b7eb7b2c769f8adcaeefb5ce340ff99018e84efa8d020299ce1f6883f42b7fe8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7GQHJ6Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7wId9NQc4AxTB9bVs38HjuZeq4pZaObbPbvcCsXHIxAiEArEQylJWrxoY49fiMq%2FPECZ3a3HNyyCvnLlNj5UMuY7kqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMDXJyX%2F%2BMN9QqZhKircA1hcd5uj1v9CoENHy0GUwHMY4XshA1uW50tvGYuOJ1CCUtDfOT9uQiMzdbP1xKHixNndi2QDiK%2BVORBiuSKo3nCRsNFD%2FSDFdO0DimNJRLPw656xdZxNzx93fjNzf4J6VwIkgANPU6xQ8jptXPz%2FYyYT%2F6Ub4jn7mChYyxdD5q64NEqeUPJoiNTwuRAD03vnTkc7PCpETPyfNyrWaZKCD5tFLAr5m7C23zmBhVr82yMhPOuyjIin%2FiWl3r5pn25m6478eof2uDaAU%2BPQIJhjbJL%2Fi5L%2BYWDxAaZjsAYk0zqoC7p4iqEwhdUGKu7T9qwtqkWgI7cQklP%2FnUDDjolM5bQGXQbW3sYuiQMxCrOy5Fk8JOHRoL5zDPWRMbK93gcugwV5ejjiU%2BTxjBlF8pm0GMvLJJfSlWQcAr%2BaQSCqbMzdjfKMdJtsN%2Fm4ivq7v0deBLtK3NRPBKLNchus9SmaLceZUTEzjQcmnVMCpS1B8v%2FEy5uSCLj4%2BpKDM1j6koL%2BALafI2phHZY4Ai1CsAdpwL5V927PVaMeo3VmsUAINcc1vEhNEeXV9j6IgSg8wL28BznxjtnlZKbyTUeWomOBvBfdu%2FPzoaw8CbquxOFkc%2BCz5Aa3v14Koh8VJ%2Bc6MNju%2FLwGOqUBXFfztU4vQxMmRarCXb7l3aj0n%2FjRQcI69BPHjsypCplneRDknJ4l6ctdI8HuSdd9cCfALANHnSAiUckLTl4pKapBMsUS%2BnwrIFgr%2BDY9CzXqLZf%2BxDVj1USXQx22rJbBg6%2BVG0mYSRYVNGeyVyIz7wkHDJIgze30LZljEqsHUiehI7izxz3Wy2i2aydF1fFcMAR2XgFzaR7rlBtizM3payFVmQKV&X-Amz-Signature=350f7eadde13e82862f88cbb0d85c13774d1b6658a586926224238fea35b8350&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7GQHJ6Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7wId9NQc4AxTB9bVs38HjuZeq4pZaObbPbvcCsXHIxAiEArEQylJWrxoY49fiMq%2FPECZ3a3HNyyCvnLlNj5UMuY7kqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMDXJyX%2F%2BMN9QqZhKircA1hcd5uj1v9CoENHy0GUwHMY4XshA1uW50tvGYuOJ1CCUtDfOT9uQiMzdbP1xKHixNndi2QDiK%2BVORBiuSKo3nCRsNFD%2FSDFdO0DimNJRLPw656xdZxNzx93fjNzf4J6VwIkgANPU6xQ8jptXPz%2FYyYT%2F6Ub4jn7mChYyxdD5q64NEqeUPJoiNTwuRAD03vnTkc7PCpETPyfNyrWaZKCD5tFLAr5m7C23zmBhVr82yMhPOuyjIin%2FiWl3r5pn25m6478eof2uDaAU%2BPQIJhjbJL%2Fi5L%2BYWDxAaZjsAYk0zqoC7p4iqEwhdUGKu7T9qwtqkWgI7cQklP%2FnUDDjolM5bQGXQbW3sYuiQMxCrOy5Fk8JOHRoL5zDPWRMbK93gcugwV5ejjiU%2BTxjBlF8pm0GMvLJJfSlWQcAr%2BaQSCqbMzdjfKMdJtsN%2Fm4ivq7v0deBLtK3NRPBKLNchus9SmaLceZUTEzjQcmnVMCpS1B8v%2FEy5uSCLj4%2BpKDM1j6koL%2BALafI2phHZY4Ai1CsAdpwL5V927PVaMeo3VmsUAINcc1vEhNEeXV9j6IgSg8wL28BznxjtnlZKbyTUeWomOBvBfdu%2FPzoaw8CbquxOFkc%2BCz5Aa3v14Koh8VJ%2Bc6MNju%2FLwGOqUBXFfztU4vQxMmRarCXb7l3aj0n%2FjRQcI69BPHjsypCplneRDknJ4l6ctdI8HuSdd9cCfALANHnSAiUckLTl4pKapBMsUS%2BnwrIFgr%2BDY9CzXqLZf%2BxDVj1USXQx22rJbBg6%2BVG0mYSRYVNGeyVyIz7wkHDJIgze30LZljEqsHUiehI7izxz3Wy2i2aydF1fFcMAR2XgFzaR7rlBtizM3payFVmQKV&X-Amz-Signature=136e67f49c7772b9ad1dd92c3ab5b11704e0d352da062c90216576d7896e2ac0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7GQHJ6Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7wId9NQc4AxTB9bVs38HjuZeq4pZaObbPbvcCsXHIxAiEArEQylJWrxoY49fiMq%2FPECZ3a3HNyyCvnLlNj5UMuY7kqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMDXJyX%2F%2BMN9QqZhKircA1hcd5uj1v9CoENHy0GUwHMY4XshA1uW50tvGYuOJ1CCUtDfOT9uQiMzdbP1xKHixNndi2QDiK%2BVORBiuSKo3nCRsNFD%2FSDFdO0DimNJRLPw656xdZxNzx93fjNzf4J6VwIkgANPU6xQ8jptXPz%2FYyYT%2F6Ub4jn7mChYyxdD5q64NEqeUPJoiNTwuRAD03vnTkc7PCpETPyfNyrWaZKCD5tFLAr5m7C23zmBhVr82yMhPOuyjIin%2FiWl3r5pn25m6478eof2uDaAU%2BPQIJhjbJL%2Fi5L%2BYWDxAaZjsAYk0zqoC7p4iqEwhdUGKu7T9qwtqkWgI7cQklP%2FnUDDjolM5bQGXQbW3sYuiQMxCrOy5Fk8JOHRoL5zDPWRMbK93gcugwV5ejjiU%2BTxjBlF8pm0GMvLJJfSlWQcAr%2BaQSCqbMzdjfKMdJtsN%2Fm4ivq7v0deBLtK3NRPBKLNchus9SmaLceZUTEzjQcmnVMCpS1B8v%2FEy5uSCLj4%2BpKDM1j6koL%2BALafI2phHZY4Ai1CsAdpwL5V927PVaMeo3VmsUAINcc1vEhNEeXV9j6IgSg8wL28BznxjtnlZKbyTUeWomOBvBfdu%2FPzoaw8CbquxOFkc%2BCz5Aa3v14Koh8VJ%2Bc6MNju%2FLwGOqUBXFfztU4vQxMmRarCXb7l3aj0n%2FjRQcI69BPHjsypCplneRDknJ4l6ctdI8HuSdd9cCfALANHnSAiUckLTl4pKapBMsUS%2BnwrIFgr%2BDY9CzXqLZf%2BxDVj1USXQx22rJbBg6%2BVG0mYSRYVNGeyVyIz7wkHDJIgze30LZljEqsHUiehI7izxz3Wy2i2aydF1fFcMAR2XgFzaR7rlBtizM3payFVmQKV&X-Amz-Signature=7e9db40726ae8985fb4aafecc791d5f9f085cf92658dafd59b7081cdb1317912&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNQOJUVH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBXA6mjNt0sXmsz4OTikBEk1a1dGmAr9H99VM%2FObWO8oAiA09KfogdSOdhVD%2FcQLgJnQvYXR2JRp1mQBMDeFmIHmOiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBHvCMsK5Zff7FunYKtwDtc0woxa1akw9y08aRWNGmW9zCr6eYawojEbWXaxdpu1OdVVVpUnVFmiaZ%2BzCYco73YqUz9fqwWJDR88Z2lZKAdqMHUeFjrXN2jWShifXVq8AK9JUrRxzYzWszzvXLPVfk0wR%2BikRCaSTZzcjbuZqafWnGeavH2AJDeQM%2Bc3j5665CCC540i73w%2BhuR7nMfCL9Sb8Q6wxTXW%2BvKOQi1PhYBrxbwYwL0zjmIxEL6fKQGzrMpyk6ZVksthITf3MYu5wMVrRoIg6iShOrNxtNG0H4fsw07cdboJtlDW74w4k4JsQMD7umnYWisIL1nt3U%2B5gYs5w4%2BG2M9kTzhjPkTNBcos0EJwGqsIgtoKmMCVcgCvihRLAm2diNtu9spDxZMQlJuJ0mhf%2FKwHxUvLvdbRLOOAT9Y%2BTy3IMzROSrpzv1zCt3tSb184MDJxQjCY6wlpPgG2wHOI0R5AVz4TRuRATwPE9%2BtNprJgRQaVPLXAPFeRxHMtL%2FIlq0VKZtVSwdgvFs4gHh91niBqGi9ycawT9u1PA8uCcoYfzAUbLpc0yotSnEe0puBoa7zTsaqM4SzQyRn4%2F2X6hJN4ipmqsK5TJ7D5koR7CD06Nm1LTY9%2FI45dCdHOLFlXQ3b5q3MMwqsH9vAY6pgFQ4I%2FqOKIr82C779lsDkA2fjjJRqAc28WeAlGIeFJWvN3XAQ9V67EjF6EF2Q3TcktMO74Xl%2FIj2w3iEE7jCyILF93LT8YMhuihvp1eESgjUlSPahTbskJq6%2BwO7eXufreO434OBq4Hlaupl8g7uBOwJKqdr5Zdbvr%2FJHG9zi8ZGb5CgOqxSA%2FLzl1W%2FTAH1Vu6qQxGM6B0ITPIFzKH5W%2FNvB3FOKMG&X-Amz-Signature=e03ae070db2935fd90eee2014aab4dcaf7674c8491da1f242f24b3024ee1d988&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMXWFEYC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDETKi6gPfTQjmXIi5tOOMbXs4TCKIQRnAIFpsyKjfKfAIgSD%2BwVlgzCqsGGydFiDiWNi4sxalUvMcRTpFaotCyOrgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEqS%2FkKwA0KV%2Bch2ICrcA4QG4tDLJO4ZTIBHNiw66Dh2ELeaMCxEWiJI6wmNVUzKfVHcgx1TKuD4JSW2kBLRk09VTbQnnez8%2Br%2B4xS1Aorvzc5WYkbFKnTGespEReZPivfHxvIH66cHmHLR9UAC1KqwQOsyBzNHMowfZnshd85MlPRk2jgpd5VJl%2BC1hs%2Bh%2BAtZgx9DQqkkEs%2Fez992yxsE206afL%2B9%2FQCjUqMpj%2B8k2l0zls1OYxkbhJuxCbxeXLTk0K%2BJ5l6ZGTGLDXgZaVIV85BRe%2FD0Wlt2tgDvu09RrcDmCDnu8WLbv1YPd84oMPWiGJ2reEH6wjJj4qj0kD05T%2FLKyYCZS9pzhKP4uz%2FKEZyhcwOz3%2BaJJDYL3W3ZrQKDWj02NTMu6tNxGPApgYY8xscfFT%2F8OTMchFfC9euCMpjA%2FcD8Ncab5JV2seWXDOYuQ8EK9iaeAxPZwFIYHaaGjPmhnWNxMCrP4T2bdzYNaQOK5J6ISQr1OFxW0dJFImbNP%2BZG18Q14Y%2FdfRuRn9%2FW%2Ffu%2Bn%2BMM3q6G2%2FaJqC3P1fteloc2rjXWh9ZP2Gm08e18YJRIB1SU%2FMJaQdLqkG3%2B2d8fYF3y6KkDRVZMGMz6yApICQuVDpxvqqYIBQwY1SggsWUVU3CBgHbc%2FMJHC%2FbwGOqUBIf9MQDqG7AW%2Fx3%2BlfkwtBb%2FO46WnKl19nOIfdAEBTXjC08vglBA2GwC51yK1Lrq%2FMYVvYqk4%2FXyZXFFB9dd53h9B8Zyb9Cs2XcYU4v2hcMc%2FIYGEdXqvb0AVvCZKy3U5rF7GEPg58B5Sx4bpYv8ZR0GC8WXeUjWEcNyXogzpG0u5nw56vv5Z5lxjEvppq0EfTb400MQAPTlbCT89KyvxetxA2nSE&X-Amz-Signature=a1267364eebc96d28a917f104118574aee9172d1d9d89d7843732ac13a2792b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7GQHJ6Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7wId9NQc4AxTB9bVs38HjuZeq4pZaObbPbvcCsXHIxAiEArEQylJWrxoY49fiMq%2FPECZ3a3HNyyCvnLlNj5UMuY7kqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMDXJyX%2F%2BMN9QqZhKircA1hcd5uj1v9CoENHy0GUwHMY4XshA1uW50tvGYuOJ1CCUtDfOT9uQiMzdbP1xKHixNndi2QDiK%2BVORBiuSKo3nCRsNFD%2FSDFdO0DimNJRLPw656xdZxNzx93fjNzf4J6VwIkgANPU6xQ8jptXPz%2FYyYT%2F6Ub4jn7mChYyxdD5q64NEqeUPJoiNTwuRAD03vnTkc7PCpETPyfNyrWaZKCD5tFLAr5m7C23zmBhVr82yMhPOuyjIin%2FiWl3r5pn25m6478eof2uDaAU%2BPQIJhjbJL%2Fi5L%2BYWDxAaZjsAYk0zqoC7p4iqEwhdUGKu7T9qwtqkWgI7cQklP%2FnUDDjolM5bQGXQbW3sYuiQMxCrOy5Fk8JOHRoL5zDPWRMbK93gcugwV5ejjiU%2BTxjBlF8pm0GMvLJJfSlWQcAr%2BaQSCqbMzdjfKMdJtsN%2Fm4ivq7v0deBLtK3NRPBKLNchus9SmaLceZUTEzjQcmnVMCpS1B8v%2FEy5uSCLj4%2BpKDM1j6koL%2BALafI2phHZY4Ai1CsAdpwL5V927PVaMeo3VmsUAINcc1vEhNEeXV9j6IgSg8wL28BznxjtnlZKbyTUeWomOBvBfdu%2FPzoaw8CbquxOFkc%2BCz5Aa3v14Koh8VJ%2Bc6MNju%2FLwGOqUBXFfztU4vQxMmRarCXb7l3aj0n%2FjRQcI69BPHjsypCplneRDknJ4l6ctdI8HuSdd9cCfALANHnSAiUckLTl4pKapBMsUS%2BnwrIFgr%2BDY9CzXqLZf%2BxDVj1USXQx22rJbBg6%2BVG0mYSRYVNGeyVyIz7wkHDJIgze30LZljEqsHUiehI7izxz3Wy2i2aydF1fFcMAR2XgFzaR7rlBtizM3payFVmQKV&X-Amz-Signature=d97c454abfe8ef319e106879f2dc76e8f0353363907c67649cb59a7d64c982fd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7GQHJ6Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7wId9NQc4AxTB9bVs38HjuZeq4pZaObbPbvcCsXHIxAiEArEQylJWrxoY49fiMq%2FPECZ3a3HNyyCvnLlNj5UMuY7kqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMDXJyX%2F%2BMN9QqZhKircA1hcd5uj1v9CoENHy0GUwHMY4XshA1uW50tvGYuOJ1CCUtDfOT9uQiMzdbP1xKHixNndi2QDiK%2BVORBiuSKo3nCRsNFD%2FSDFdO0DimNJRLPw656xdZxNzx93fjNzf4J6VwIkgANPU6xQ8jptXPz%2FYyYT%2F6Ub4jn7mChYyxdD5q64NEqeUPJoiNTwuRAD03vnTkc7PCpETPyfNyrWaZKCD5tFLAr5m7C23zmBhVr82yMhPOuyjIin%2FiWl3r5pn25m6478eof2uDaAU%2BPQIJhjbJL%2Fi5L%2BYWDxAaZjsAYk0zqoC7p4iqEwhdUGKu7T9qwtqkWgI7cQklP%2FnUDDjolM5bQGXQbW3sYuiQMxCrOy5Fk8JOHRoL5zDPWRMbK93gcugwV5ejjiU%2BTxjBlF8pm0GMvLJJfSlWQcAr%2BaQSCqbMzdjfKMdJtsN%2Fm4ivq7v0deBLtK3NRPBKLNchus9SmaLceZUTEzjQcmnVMCpS1B8v%2FEy5uSCLj4%2BpKDM1j6koL%2BALafI2phHZY4Ai1CsAdpwL5V927PVaMeo3VmsUAINcc1vEhNEeXV9j6IgSg8wL28BznxjtnlZKbyTUeWomOBvBfdu%2FPzoaw8CbquxOFkc%2BCz5Aa3v14Koh8VJ%2Bc6MNju%2FLwGOqUBXFfztU4vQxMmRarCXb7l3aj0n%2FjRQcI69BPHjsypCplneRDknJ4l6ctdI8HuSdd9cCfALANHnSAiUckLTl4pKapBMsUS%2BnwrIFgr%2BDY9CzXqLZf%2BxDVj1USXQx22rJbBg6%2BVG0mYSRYVNGeyVyIz7wkHDJIgze30LZljEqsHUiehI7izxz3Wy2i2aydF1fFcMAR2XgFzaR7rlBtizM3payFVmQKV&X-Amz-Signature=97f673380bc4fcd425d85893a7e5a66ee1469166ff9f76e887f7884e74b3a2ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7GQHJ6Q%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7wId9NQc4AxTB9bVs38HjuZeq4pZaObbPbvcCsXHIxAiEArEQylJWrxoY49fiMq%2FPECZ3a3HNyyCvnLlNj5UMuY7kqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMDXJyX%2F%2BMN9QqZhKircA1hcd5uj1v9CoENHy0GUwHMY4XshA1uW50tvGYuOJ1CCUtDfOT9uQiMzdbP1xKHixNndi2QDiK%2BVORBiuSKo3nCRsNFD%2FSDFdO0DimNJRLPw656xdZxNzx93fjNzf4J6VwIkgANPU6xQ8jptXPz%2FYyYT%2F6Ub4jn7mChYyxdD5q64NEqeUPJoiNTwuRAD03vnTkc7PCpETPyfNyrWaZKCD5tFLAr5m7C23zmBhVr82yMhPOuyjIin%2FiWl3r5pn25m6478eof2uDaAU%2BPQIJhjbJL%2Fi5L%2BYWDxAaZjsAYk0zqoC7p4iqEwhdUGKu7T9qwtqkWgI7cQklP%2FnUDDjolM5bQGXQbW3sYuiQMxCrOy5Fk8JOHRoL5zDPWRMbK93gcugwV5ejjiU%2BTxjBlF8pm0GMvLJJfSlWQcAr%2BaQSCqbMzdjfKMdJtsN%2Fm4ivq7v0deBLtK3NRPBKLNchus9SmaLceZUTEzjQcmnVMCpS1B8v%2FEy5uSCLj4%2BpKDM1j6koL%2BALafI2phHZY4Ai1CsAdpwL5V927PVaMeo3VmsUAINcc1vEhNEeXV9j6IgSg8wL28BznxjtnlZKbyTUeWomOBvBfdu%2FPzoaw8CbquxOFkc%2BCz5Aa3v14Koh8VJ%2Bc6MNju%2FLwGOqUBXFfztU4vQxMmRarCXb7l3aj0n%2FjRQcI69BPHjsypCplneRDknJ4l6ctdI8HuSdd9cCfALANHnSAiUckLTl4pKapBMsUS%2BnwrIFgr%2BDY9CzXqLZf%2BxDVj1USXQx22rJbBg6%2BVG0mYSRYVNGeyVyIz7wkHDJIgze30LZljEqsHUiehI7izxz3Wy2i2aydF1fFcMAR2XgFzaR7rlBtizM3payFVmQKV&X-Amz-Signature=29befce504d3c489530e8a9cae7fc076cc3dedf1b9f525a9c54810299c2d96f6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NZIBYS6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFQnxL48erEktmUWLfnCq1OUPR2E1eGwmOWs1Sr1VKHoAiEA1qEe1KKDUxAVbtBG9RzH5NXmsV3ksfGkOegdslRph3wqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9u6csaDtHQGdXypyrcA0ZQp%2FIirntcoAfaqvEmY8kaaK%2F59lWOCPkHygesDdG8tAHrMhocF6TTi0fLxugUuhjsHZTM%2BJkq86NHZYBk%2FeYc0ZioN%2BEimjxYMGjjw7X0nJTODTm%2FSvuB47WP6eBDnju00fT%2BYX2xmcWiQn6sp%2FiOunJwGVkK2pPfhqyJMzH9k8OlctMpqd6UZetATfpRTUSRk7fxBSKP%2FSPbQR5FtLgyw1dF1ysqNjM7KTg1FFkZ0BC0bb1VBYx%2B7wvc1lQJmJp95Wm7P409LHnZ96fS98qfH76VQt0u%2BOfAB25Q65yFzvzXB7guB0ypwx%2FgF6idaINd7Diwm8Y1Qy3uoyjfbOtV%2Fv0deWBnwkJuiSuu4D%2Bxp%2Bg2xs0%2F%2BC9AVVf5IQkjp1oofCLKsaTxsNS0tsjMliyA8R0mwFzAFESKUSKEAov1CJG6Niy739N5vpkjETkGc8qXbI9jZYidvvdgvyPftb7fPnvWIVFxuu%2B0BoU0v6dPKGgHQ%2BZjeJa%2BDF%2B7cWPal7PEOqZqxGcdz%2BOQhR83ANipVEAyGsum76P7RvO%2BRh23Mh7u44kRzzvCQ1sDdvap1n04yGVuPhM3tdRgZTpu%2BtNNUTHntTWj0pOSqQ30S%2Ba%2FyLAiWZQIKZnLB%2FUSMJHC%2FbwGOqUBN5kmI1jsy%2BPld9MbrhKR7pJ90dQ4FsCDUQWSc%2F6vv3UOrryV2GTaSnLfmadjiCj9vXEOSefmtUpu8gmYk9nIDmU9R5QkMH5GDxuEFJSEVxz6vsafCa3r2wifGBx5seeIJOoBDFt3wkN0YsF6L2Vut6S%2BShI4ub5DdXtNjIxfGlS0ZFnE5kMyj0ZAq0ZOOmOzAiR8SO%2B%2Bv9j8SBqxW1Ww3xWm1MUi&X-Amz-Signature=c54c99f4f7f3253768a1e64ce1a1adf2682fc9e31b003022badc6930d8e1bd38&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WABLYIP6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHcQZa2Rwkga%2FVq3geo2FgY99fUBlD%2B3HnZFgqBrgaVyAiEAifQ517UefAeOOc%2FkpyMInxlHnGJDg77ops9kAPRt2YYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGrUHHGfzQKWTo55VCrcAwOAaGrGyka9gL0JrLRGB0cmqEmtXHTxhqGmPMJLxpUsntm%2BzDLNbNfOeWnu%2FGUrqlAemmBzaDP40hEPnSOrXkcZeogQUN1BRRFGm64KbUdO5eZhh%2FxIGTZqQD8HWm4V9SjDexpOJTeu3xVuWc8N7JUs4hnc9N00VMUsA3Mq1l%2BG6snmXlnAURWH3v4clCuRx7lmU22KbIhrL4S6pIgxolV3zN7TGdOM6tnPtxJMMufD3IXnjr1k8L%2Fm%2FX1HFZ%2F%2Foe9xl7Z%2BeDBaXyJCp4ObYSlkorizCvEHQHlzozoiwJY1Gv%2FovJUMQ1ZyL5ONv%2BuPMWkDcaKIo5JeTOZI7pSsFIUk9GdlrcTx9QNWaroB2cTcWei6oAX6AFKtLy0cKxYIQb%2Bwk48ffccuXiCeoiJFLSrGhcjQW1dSBJaVCebniWJbkdUIT96l0MsCO9QS7AsCW5iidXY3%2BEKTOAwoQkKc%2B5ULKvhCVAw%2FjFugp%2FhRIhRAypxZKLHnPPkk8fZ%2F9M6Mjs%2BBYpX5t%2B0GDUwRVQv%2Fh7G7RA5TaNfKKEfM%2Bld6g7%2FyuWMVur1KneD05p3fgSyX%2BRc3AMNwJTitSv6wnx8iHXtsJ10CMKHCPfV2jZnsp43%2FR%2B8y3aahYun2NKmUMOG7%2FbwGOqUBpGa7ByFb8C6FNZ1i%2Bk7UN8INH1WNE21j47qkOQ%2FHtK9CGerpR6l6jATk2BIgO1uD3kmDqTs1mKEorrelvt%2BhriWIb%2B8PyHNjfFbDJNtPRkwWDrhX9dv7VmOSSU4ntU6XGKymZLxRp6EhcvHxXUua7HU2jNMomFRLzhM%2BbLfLDX3UC35KRIHaGlhyVITMq3E7dmAeHMQgClyQw196XB3O0mINI5S2&X-Amz-Signature=dba623d5caa8611c508032a643f994d62ca761a11bd6774a718e0a8db4bbfad6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR5CWRSU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICgaNXabuEyXUgcjJ7RGjVN5pd100Iw%2BGFQ5pNKNQQoXAiBk12gL4xcvdO1wvWfVTp2dGswNL9I7lEvAjJCe5FEDfCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqgzemHCmfilffmueKtwDYLdKT9ebrFuA4n9CiroSkWkbS7SZk25GlKl%2FWHlHMC5ovro9sSVjWJiWysq9Ey3tIRBMPJlytMaMFkLQC%2Bf4i5F0GTRhkZoQb5t63nP2WB6meifXHifEjQQeMURw79XlHue7Q2wDuk4p%2FGPRXjt%2Fxio4gu%2BRFxX5BdNkr9R1VvnXHGWj5nGwe3F2VBF5M1F%2BYm9TVWrEntvQE3eJq8aGVjIyvcbtEBvhXetHNmyJCXICJznUlxc4CVxuBUgf%2FdPqtG4ppF6NT848GDLibQRsKq1AXwnHjzrDbcakaXcMqtBf2Via3U6O0hdvHKwLLHTT%2B%2FqEFphB%2BAvzEZvFT0cKUZl6rhZcZzL2QZm8eExw017xYQeVw%2FmAdFymyw776B7cesDTqV765jM9u%2F%2Byfi6g0MGFP4fhIP2zLEYrvUUuuLLLhJYSW7O5z93KuYG%2Fdcbr28RebAL83nGRC7iBGY1d4v6SGYfwg%2BiNed%2BDCeXc7USmhyVucA7vCvqUfC89Mi4DtIKDOApjXEYOa%2FnYm2CpjetwbV8Rh5pUsur%2Fjku4wlK83pF7h%2BxaAcb%2FTIfdLyEM0FZLZPy4bwzubQUI2vWn7twicBv7h9BYcLf725VoJG3xick2FzJXgV5HnZMw37T9vAY6pgGRg%2B0eymmA0Ppnt2AcpwHQ%2BO7XcXW2qDC9ZXWFe%2FxiuYekAlOBq6icVoqkOuKf9VB32P5WfYxxHGVPkknhSL8wMr4eGNMaGKEm212qv5W0rB%2BLgUlj9eWGBGnZaXLfMzNtGtQU47vNg53%2BYrkwG7r2NL3CkzTNkwD6A6yYSVXX9rd%2FVq%2FqVhkOK3zLdbygj3Q%2BOsjXcUZYirXko4o1xTcthu%2FmP0Dh&X-Amz-Signature=57809923b0febf062670c5e4daa1e3a9fec95c971cdf71118d4065b7a983e99c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665THSZ7IM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2BWahjSmS3vnM6IvxebfXo5kcEhDFNIUhKGaA7%2B%2F%2FuBAiBsrjvqhgHHiayTMjkkZszsWnBq2ZEGqZKaJS2w8Uw3hSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8NkCUnE1IeNNDSBwKtwDth%2BAwa2jMnZpxQ1fFvbzcTakaTs0JiRtGWOl9g6CqKSucyK1zQAPvDziv3JZtuuiRmEam1jNaQzvnUg5oHL6ct4ohB%2F8iGOx0EB6%2BrQhssmEdhwoc0OVfiTZ9KPe9NibsUy1947Pi1q%2Bsf8r9isSlVyTnUE%2BVdbMLH1%2BsafNZIyDS1jREE1Qz7z3z3KEeu0MZ3TBkf6HNEYK2QYviQBnNPYrg0krl0FZYi90BYD0%2BZ0wqlmQisaw91OpJzQjDpw%2FJQ9tdZ%2BhBdiX%2BJFNGf%2F7Flan%2FqQsQXeQl%2FfnFB00p4ssOQJs14jvnOG5z7ERm7IyZOG5%2BrPNRskuW2CKflRkcOwFc1d6AYRM9L8rE7aSvGOAxB2epR9hhbB2Z%2FRmaNDmn4ovTLrt%2BiMNPTCRjQ7dbWcB4PhxsMoq1XdJIwAb%2FSFZVbzERS8%2FnfRGSGnuvggYG7YcUbyxiDp8NMybkhqnMb6YEy2gSKcWpYKmrNT0lbW%2F2OjBEyIWx1i9HMqwbc0H4Zir5yCuvKNoTd6dYLVyb%2BG%2BF%2Fs70UUeCdVno9SZ1hXyXbggn8Gd5WuIHlk6YkMnPBUZAXVzUvTC2G7kFVEiBTK6QK835UGoXSNbIzasfB3hfZLjFAZIsVrGGv8wqcH9vAY6pgELTCwvV%2B7l%2BfuOlU2W6DCPz4fGNFtA9xvldNdUYfpsCwM1ZqgaD5N9diZdzmUxNT%2FpIJTTN8fpQEkO%2FQocUc%2BHMlQtoT9Wfv2Re%2B6Xq0AlHo3%2BiwafBzIyU%2F%2FpRKCKKEUAlZQiPVVpOA3Zoku%2BOpPXMTne76c2YZI1bXiUMkBRe60IYs1rp6wtGSbRhYb1GTqWS%2BT8jv0OlkOqKozVbGdICMmU15yq&X-Amz-Signature=bca953b241637e1e81b7b8bea0dd359492c7ccffc19a5e500729ec8f7d7728e2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665THSZ7IM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2BWahjSmS3vnM6IvxebfXo5kcEhDFNIUhKGaA7%2B%2F%2FuBAiBsrjvqhgHHiayTMjkkZszsWnBq2ZEGqZKaJS2w8Uw3hSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8NkCUnE1IeNNDSBwKtwDth%2BAwa2jMnZpxQ1fFvbzcTakaTs0JiRtGWOl9g6CqKSucyK1zQAPvDziv3JZtuuiRmEam1jNaQzvnUg5oHL6ct4ohB%2F8iGOx0EB6%2BrQhssmEdhwoc0OVfiTZ9KPe9NibsUy1947Pi1q%2Bsf8r9isSlVyTnUE%2BVdbMLH1%2BsafNZIyDS1jREE1Qz7z3z3KEeu0MZ3TBkf6HNEYK2QYviQBnNPYrg0krl0FZYi90BYD0%2BZ0wqlmQisaw91OpJzQjDpw%2FJQ9tdZ%2BhBdiX%2BJFNGf%2F7Flan%2FqQsQXeQl%2FfnFB00p4ssOQJs14jvnOG5z7ERm7IyZOG5%2BrPNRskuW2CKflRkcOwFc1d6AYRM9L8rE7aSvGOAxB2epR9hhbB2Z%2FRmaNDmn4ovTLrt%2BiMNPTCRjQ7dbWcB4PhxsMoq1XdJIwAb%2FSFZVbzERS8%2FnfRGSGnuvggYG7YcUbyxiDp8NMybkhqnMb6YEy2gSKcWpYKmrNT0lbW%2F2OjBEyIWx1i9HMqwbc0H4Zir5yCuvKNoTd6dYLVyb%2BG%2BF%2Fs70UUeCdVno9SZ1hXyXbggn8Gd5WuIHlk6YkMnPBUZAXVzUvTC2G7kFVEiBTK6QK835UGoXSNbIzasfB3hfZLjFAZIsVrGGv8wqcH9vAY6pgELTCwvV%2B7l%2BfuOlU2W6DCPz4fGNFtA9xvldNdUYfpsCwM1ZqgaD5N9diZdzmUxNT%2FpIJTTN8fpQEkO%2FQocUc%2BHMlQtoT9Wfv2Re%2B6Xq0AlHo3%2BiwafBzIyU%2F%2FpRKCKKEUAlZQiPVVpOA3Zoku%2BOpPXMTne76c2YZI1bXiUMkBRe60IYs1rp6wtGSbRhYb1GTqWS%2BT8jv0OlkOqKozVbGdICMmU15yq&X-Amz-Signature=cfd7204004c03bf3563968f5d6ecc1ecbba46b5619627a710282a792746c3681&X-Amz-SignedHeaders=host&x-id=GetObject)

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
