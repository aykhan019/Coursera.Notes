

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYAOARLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQDVSmOWY8nQXwIL4kFmFh0PJWaaeRVlkbZvMN0hiR%2B9fQIhAMU5Ups8TjFH3v4ZkvPCP5J8XBbVTGv7CAXDOcmmg5tUKv8DCEEQABoMNjM3NDIzMTgzODA1IgyNJBx6MoDomTJMwgcq3AOdTTmw55V91XwZRFHFhn0kbPu9vgMs89P%2F%2Fcxn%2FK19PHLWz6GXEQBUOuhc59bHJbr0rl%2FU0Hc%2BEETJ7b%2B%2FFlMRZGV3H0Cirf%2FEpx%2FxUhq1VxWp6a%2Fz4n7LbfzmZ%2Fy7SAInFmyylKEub1nw5SmmsKgS4iGTXzdFIEVbPuyMNGvHYxuirJ2kQyffIz8w5jY%2FG%2BEkuNla79sJ3LTsQZHI6cQclMjuCEnsbZq58g4QdmsdL4UcpG5P%2FcgzRWPfjvbbogVkF%2FRrxOWerOr2H1VAWzOABOAEV6K6C99w0ktbxkaEAUWRqh30m2KNdCNduheWvgNqqyhpSyM%2FW8pgsjizIL6npf8JyEdXCMli%2B50iGfC1%2BEaErLwBWjQQNUUdEKTR0r7dDsE0QxH5vrDzSvt4J%2F3ev9SwOU3LMNZd7i64L%2FvZcI63JVh29DTTA48kzwpAXtg0ImN1ymgnrhrBCcjjJNa8D4qSleS8k06z71Qyib29xTAr5JxZsYJ6%2B1B2hbRaJZU03cfuM1mGMYFTcaHAS89exmgoh80h2r8DUGvvoVSpZ8U523KGIMoVZp5uCeqn%2BsR2naSp1DkuftwZgOtiBer3IB3r3OY2IqyF%2FeBZNo9ScBHVuyX4V2Z3yxPoHTDjs4y9BjqkAQM7goKKTT8Bu9qdMvNmNnasKu%2BNAIS339hoM%2FlLmhRu19nFRuy%2Baj2Fr2q6fPDSrtUCmjaEs5Sp9ySU6st2bjM4C1EdAIyOB19kyoe9txO61lwU2u7jl6Lnd8HgrbkXF8gqspgAwdjHSSLCjDg14XcPQfsRlzdx9nAUnsNW8zNugicPIsTDXSdrnciu5tQlzwk1dm%2BZkDBMlYhGBPB%2BBKEADsAO&X-Amz-Signature=9f6d26625494f09c0ef6b11d90eb543a5642bf808bc8f432264d6cc93df8d3e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYAOARLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQDVSmOWY8nQXwIL4kFmFh0PJWaaeRVlkbZvMN0hiR%2B9fQIhAMU5Ups8TjFH3v4ZkvPCP5J8XBbVTGv7CAXDOcmmg5tUKv8DCEEQABoMNjM3NDIzMTgzODA1IgyNJBx6MoDomTJMwgcq3AOdTTmw55V91XwZRFHFhn0kbPu9vgMs89P%2F%2Fcxn%2FK19PHLWz6GXEQBUOuhc59bHJbr0rl%2FU0Hc%2BEETJ7b%2B%2FFlMRZGV3H0Cirf%2FEpx%2FxUhq1VxWp6a%2Fz4n7LbfzmZ%2Fy7SAInFmyylKEub1nw5SmmsKgS4iGTXzdFIEVbPuyMNGvHYxuirJ2kQyffIz8w5jY%2FG%2BEkuNla79sJ3LTsQZHI6cQclMjuCEnsbZq58g4QdmsdL4UcpG5P%2FcgzRWPfjvbbogVkF%2FRrxOWerOr2H1VAWzOABOAEV6K6C99w0ktbxkaEAUWRqh30m2KNdCNduheWvgNqqyhpSyM%2FW8pgsjizIL6npf8JyEdXCMli%2B50iGfC1%2BEaErLwBWjQQNUUdEKTR0r7dDsE0QxH5vrDzSvt4J%2F3ev9SwOU3LMNZd7i64L%2FvZcI63JVh29DTTA48kzwpAXtg0ImN1ymgnrhrBCcjjJNa8D4qSleS8k06z71Qyib29xTAr5JxZsYJ6%2B1B2hbRaJZU03cfuM1mGMYFTcaHAS89exmgoh80h2r8DUGvvoVSpZ8U523KGIMoVZp5uCeqn%2BsR2naSp1DkuftwZgOtiBer3IB3r3OY2IqyF%2FeBZNo9ScBHVuyX4V2Z3yxPoHTDjs4y9BjqkAQM7goKKTT8Bu9qdMvNmNnasKu%2BNAIS339hoM%2FlLmhRu19nFRuy%2Baj2Fr2q6fPDSrtUCmjaEs5Sp9ySU6st2bjM4C1EdAIyOB19kyoe9txO61lwU2u7jl6Lnd8HgrbkXF8gqspgAwdjHSSLCjDg14XcPQfsRlzdx9nAUnsNW8zNugicPIsTDXSdrnciu5tQlzwk1dm%2BZkDBMlYhGBPB%2BBKEADsAO&X-Amz-Signature=7364f5e8c2848241c39844768d0092adf15c0e5c5630bf3b5b60340b2b8f8aad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYAOARLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQDVSmOWY8nQXwIL4kFmFh0PJWaaeRVlkbZvMN0hiR%2B9fQIhAMU5Ups8TjFH3v4ZkvPCP5J8XBbVTGv7CAXDOcmmg5tUKv8DCEEQABoMNjM3NDIzMTgzODA1IgyNJBx6MoDomTJMwgcq3AOdTTmw55V91XwZRFHFhn0kbPu9vgMs89P%2F%2Fcxn%2FK19PHLWz6GXEQBUOuhc59bHJbr0rl%2FU0Hc%2BEETJ7b%2B%2FFlMRZGV3H0Cirf%2FEpx%2FxUhq1VxWp6a%2Fz4n7LbfzmZ%2Fy7SAInFmyylKEub1nw5SmmsKgS4iGTXzdFIEVbPuyMNGvHYxuirJ2kQyffIz8w5jY%2FG%2BEkuNla79sJ3LTsQZHI6cQclMjuCEnsbZq58g4QdmsdL4UcpG5P%2FcgzRWPfjvbbogVkF%2FRrxOWerOr2H1VAWzOABOAEV6K6C99w0ktbxkaEAUWRqh30m2KNdCNduheWvgNqqyhpSyM%2FW8pgsjizIL6npf8JyEdXCMli%2B50iGfC1%2BEaErLwBWjQQNUUdEKTR0r7dDsE0QxH5vrDzSvt4J%2F3ev9SwOU3LMNZd7i64L%2FvZcI63JVh29DTTA48kzwpAXtg0ImN1ymgnrhrBCcjjJNa8D4qSleS8k06z71Qyib29xTAr5JxZsYJ6%2B1B2hbRaJZU03cfuM1mGMYFTcaHAS89exmgoh80h2r8DUGvvoVSpZ8U523KGIMoVZp5uCeqn%2BsR2naSp1DkuftwZgOtiBer3IB3r3OY2IqyF%2FeBZNo9ScBHVuyX4V2Z3yxPoHTDjs4y9BjqkAQM7goKKTT8Bu9qdMvNmNnasKu%2BNAIS339hoM%2FlLmhRu19nFRuy%2Baj2Fr2q6fPDSrtUCmjaEs5Sp9ySU6st2bjM4C1EdAIyOB19kyoe9txO61lwU2u7jl6Lnd8HgrbkXF8gqspgAwdjHSSLCjDg14XcPQfsRlzdx9nAUnsNW8zNugicPIsTDXSdrnciu5tQlzwk1dm%2BZkDBMlYhGBPB%2BBKEADsAO&X-Amz-Signature=8e1881ac15a71042e7587c9f643f6ab89224929d84d10896b87e6ddf319f2632&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBD77QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIEyPlKiWFX%2F9o5f8jiIJiVpH0rr2%2FVaGAi0n41QoTEBQAiBvOq54f1z%2BbNhNOlsG%2F0gCozM2n2PPeXUUsWlpEjNl4Cr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMnhRprMGspudQDKrzKtwDZPYBTd0HlGCN0U%2FfU7LmXvApdSmpqtrcUHrkqxtX7PbAGFXyl8EgsAdq%2BwaHTQJ0U5jvDOt1YhOgrbCgt9Yd3xUbFaHUq%2FwJZpAa6Zv4quUmfiRabRtuQ2kptzxwSJhDZpudOdR%2FMoBsSthsO1IWZuYaYCbLKJutOqK3VKGOfvpZd%2FFpoc7uEsBHWHu1wmLpNr58zF26d%2FzsUMGtCbrMPFMus7z3TMFtC0ntL6UDWcNx4Jg7%2F4PNsFt%2B9tfDyCcv70fev3NtjjtGNMewbty%2FrO9lb4aVaFmVCca7gH9G1JB3DIlyqoKqBbHEHxO0RWCePuxTAiRsG1gkvhWJ6tFrWgl4jFMYEatjTDL9n66toTz1XeVsYRpJKyz86CT%2FQrIaMzoqqf5faOYUpaAvBNGfaoHNo6AIzTTaGoBWfDiFNRHcB9KebpnE%2Fjd7cMEUkJRNzghuFlT4zqiN1RLOD1LM3daLeeM%2BnFd5wle0Y1PQ6EiDvnPHnyEyn%2FqTdZ8qV4bA7QBqUu0ktgeO47o0sdMNv1O%2F9RkqSnnZNUN23OjihXgMHwvmiFcmVcvauxz7xUEIxs%2FhkJR1f%2FQXziReSZeN1vAb6UeNYGHIStwLu%2Fp%2FBjR1VZGn%2FQsyhMOxfzYw4bOMvQY6pgGrSiHxIr2Ty93xvODFNfwGIqtmhub1mWJBq9friQSxMNNZ9jBWenkLURADCHaIvUMWWu2TqoMyrJ3rA81aOHX3K1hp8T7cDmauG%2F%2Fzueo0%2BNfGv0BaaqKuj5nUQMV%2FFB5ZWXJiksJh1z2OTpPRXPbgq9RQCqvRa9xlPUxQprtCiQngy8V7LOcXGsLt7F3NMKQS58dKfVjqMyYNXoKF0CS4iDOLOApG&X-Amz-Signature=044783820392f87aa63b491eb2e7021ed82e27c6fa2b71a8e3d99f4d5511371a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBD77QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIEyPlKiWFX%2F9o5f8jiIJiVpH0rr2%2FVaGAi0n41QoTEBQAiBvOq54f1z%2BbNhNOlsG%2F0gCozM2n2PPeXUUsWlpEjNl4Cr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMnhRprMGspudQDKrzKtwDZPYBTd0HlGCN0U%2FfU7LmXvApdSmpqtrcUHrkqxtX7PbAGFXyl8EgsAdq%2BwaHTQJ0U5jvDOt1YhOgrbCgt9Yd3xUbFaHUq%2FwJZpAa6Zv4quUmfiRabRtuQ2kptzxwSJhDZpudOdR%2FMoBsSthsO1IWZuYaYCbLKJutOqK3VKGOfvpZd%2FFpoc7uEsBHWHu1wmLpNr58zF26d%2FzsUMGtCbrMPFMus7z3TMFtC0ntL6UDWcNx4Jg7%2F4PNsFt%2B9tfDyCcv70fev3NtjjtGNMewbty%2FrO9lb4aVaFmVCca7gH9G1JB3DIlyqoKqBbHEHxO0RWCePuxTAiRsG1gkvhWJ6tFrWgl4jFMYEatjTDL9n66toTz1XeVsYRpJKyz86CT%2FQrIaMzoqqf5faOYUpaAvBNGfaoHNo6AIzTTaGoBWfDiFNRHcB9KebpnE%2Fjd7cMEUkJRNzghuFlT4zqiN1RLOD1LM3daLeeM%2BnFd5wle0Y1PQ6EiDvnPHnyEyn%2FqTdZ8qV4bA7QBqUu0ktgeO47o0sdMNv1O%2F9RkqSnnZNUN23OjihXgMHwvmiFcmVcvauxz7xUEIxs%2FhkJR1f%2FQXziReSZeN1vAb6UeNYGHIStwLu%2Fp%2FBjR1VZGn%2FQsyhMOxfzYw4bOMvQY6pgGrSiHxIr2Ty93xvODFNfwGIqtmhub1mWJBq9friQSxMNNZ9jBWenkLURADCHaIvUMWWu2TqoMyrJ3rA81aOHX3K1hp8T7cDmauG%2F%2Fzueo0%2BNfGv0BaaqKuj5nUQMV%2FFB5ZWXJiksJh1z2OTpPRXPbgq9RQCqvRa9xlPUxQprtCiQngy8V7LOcXGsLt7F3NMKQS58dKfVjqMyYNXoKF0CS4iDOLOApG&X-Amz-Signature=22f692fdb96db07f56f01b132c5bfb088ddb50c636bf7b4f752bdfcdd8dc7d81&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBD77QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIEyPlKiWFX%2F9o5f8jiIJiVpH0rr2%2FVaGAi0n41QoTEBQAiBvOq54f1z%2BbNhNOlsG%2F0gCozM2n2PPeXUUsWlpEjNl4Cr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMnhRprMGspudQDKrzKtwDZPYBTd0HlGCN0U%2FfU7LmXvApdSmpqtrcUHrkqxtX7PbAGFXyl8EgsAdq%2BwaHTQJ0U5jvDOt1YhOgrbCgt9Yd3xUbFaHUq%2FwJZpAa6Zv4quUmfiRabRtuQ2kptzxwSJhDZpudOdR%2FMoBsSthsO1IWZuYaYCbLKJutOqK3VKGOfvpZd%2FFpoc7uEsBHWHu1wmLpNr58zF26d%2FzsUMGtCbrMPFMus7z3TMFtC0ntL6UDWcNx4Jg7%2F4PNsFt%2B9tfDyCcv70fev3NtjjtGNMewbty%2FrO9lb4aVaFmVCca7gH9G1JB3DIlyqoKqBbHEHxO0RWCePuxTAiRsG1gkvhWJ6tFrWgl4jFMYEatjTDL9n66toTz1XeVsYRpJKyz86CT%2FQrIaMzoqqf5faOYUpaAvBNGfaoHNo6AIzTTaGoBWfDiFNRHcB9KebpnE%2Fjd7cMEUkJRNzghuFlT4zqiN1RLOD1LM3daLeeM%2BnFd5wle0Y1PQ6EiDvnPHnyEyn%2FqTdZ8qV4bA7QBqUu0ktgeO47o0sdMNv1O%2F9RkqSnnZNUN23OjihXgMHwvmiFcmVcvauxz7xUEIxs%2FhkJR1f%2FQXziReSZeN1vAb6UeNYGHIStwLu%2Fp%2FBjR1VZGn%2FQsyhMOxfzYw4bOMvQY6pgGrSiHxIr2Ty93xvODFNfwGIqtmhub1mWJBq9friQSxMNNZ9jBWenkLURADCHaIvUMWWu2TqoMyrJ3rA81aOHX3K1hp8T7cDmauG%2F%2Fzueo0%2BNfGv0BaaqKuj5nUQMV%2FFB5ZWXJiksJh1z2OTpPRXPbgq9RQCqvRa9xlPUxQprtCiQngy8V7LOcXGsLt7F3NMKQS58dKfVjqMyYNXoKF0CS4iDOLOApG&X-Amz-Signature=3e7c6f7e0337a2ae5989e5d95a38a17bcb992dc87cce2e1e2a06106fa7a485bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBD77QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIEyPlKiWFX%2F9o5f8jiIJiVpH0rr2%2FVaGAi0n41QoTEBQAiBvOq54f1z%2BbNhNOlsG%2F0gCozM2n2PPeXUUsWlpEjNl4Cr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMnhRprMGspudQDKrzKtwDZPYBTd0HlGCN0U%2FfU7LmXvApdSmpqtrcUHrkqxtX7PbAGFXyl8EgsAdq%2BwaHTQJ0U5jvDOt1YhOgrbCgt9Yd3xUbFaHUq%2FwJZpAa6Zv4quUmfiRabRtuQ2kptzxwSJhDZpudOdR%2FMoBsSthsO1IWZuYaYCbLKJutOqK3VKGOfvpZd%2FFpoc7uEsBHWHu1wmLpNr58zF26d%2FzsUMGtCbrMPFMus7z3TMFtC0ntL6UDWcNx4Jg7%2F4PNsFt%2B9tfDyCcv70fev3NtjjtGNMewbty%2FrO9lb4aVaFmVCca7gH9G1JB3DIlyqoKqBbHEHxO0RWCePuxTAiRsG1gkvhWJ6tFrWgl4jFMYEatjTDL9n66toTz1XeVsYRpJKyz86CT%2FQrIaMzoqqf5faOYUpaAvBNGfaoHNo6AIzTTaGoBWfDiFNRHcB9KebpnE%2Fjd7cMEUkJRNzghuFlT4zqiN1RLOD1LM3daLeeM%2BnFd5wle0Y1PQ6EiDvnPHnyEyn%2FqTdZ8qV4bA7QBqUu0ktgeO47o0sdMNv1O%2F9RkqSnnZNUN23OjihXgMHwvmiFcmVcvauxz7xUEIxs%2FhkJR1f%2FQXziReSZeN1vAb6UeNYGHIStwLu%2Fp%2FBjR1VZGn%2FQsyhMOxfzYw4bOMvQY6pgGrSiHxIr2Ty93xvODFNfwGIqtmhub1mWJBq9friQSxMNNZ9jBWenkLURADCHaIvUMWWu2TqoMyrJ3rA81aOHX3K1hp8T7cDmauG%2F%2Fzueo0%2BNfGv0BaaqKuj5nUQMV%2FFB5ZWXJiksJh1z2OTpPRXPbgq9RQCqvRa9xlPUxQprtCiQngy8V7LOcXGsLt7F3NMKQS58dKfVjqMyYNXoKF0CS4iDOLOApG&X-Amz-Signature=8e55fcc4ce5b722c932b836afa5bcdee484b4c2327ff5fd66cc1819c2f0de5d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBD77QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIEyPlKiWFX%2F9o5f8jiIJiVpH0rr2%2FVaGAi0n41QoTEBQAiBvOq54f1z%2BbNhNOlsG%2F0gCozM2n2PPeXUUsWlpEjNl4Cr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMnhRprMGspudQDKrzKtwDZPYBTd0HlGCN0U%2FfU7LmXvApdSmpqtrcUHrkqxtX7PbAGFXyl8EgsAdq%2BwaHTQJ0U5jvDOt1YhOgrbCgt9Yd3xUbFaHUq%2FwJZpAa6Zv4quUmfiRabRtuQ2kptzxwSJhDZpudOdR%2FMoBsSthsO1IWZuYaYCbLKJutOqK3VKGOfvpZd%2FFpoc7uEsBHWHu1wmLpNr58zF26d%2FzsUMGtCbrMPFMus7z3TMFtC0ntL6UDWcNx4Jg7%2F4PNsFt%2B9tfDyCcv70fev3NtjjtGNMewbty%2FrO9lb4aVaFmVCca7gH9G1JB3DIlyqoKqBbHEHxO0RWCePuxTAiRsG1gkvhWJ6tFrWgl4jFMYEatjTDL9n66toTz1XeVsYRpJKyz86CT%2FQrIaMzoqqf5faOYUpaAvBNGfaoHNo6AIzTTaGoBWfDiFNRHcB9KebpnE%2Fjd7cMEUkJRNzghuFlT4zqiN1RLOD1LM3daLeeM%2BnFd5wle0Y1PQ6EiDvnPHnyEyn%2FqTdZ8qV4bA7QBqUu0ktgeO47o0sdMNv1O%2F9RkqSnnZNUN23OjihXgMHwvmiFcmVcvauxz7xUEIxs%2FhkJR1f%2FQXziReSZeN1vAb6UeNYGHIStwLu%2Fp%2FBjR1VZGn%2FQsyhMOxfzYw4bOMvQY6pgGrSiHxIr2Ty93xvODFNfwGIqtmhub1mWJBq9friQSxMNNZ9jBWenkLURADCHaIvUMWWu2TqoMyrJ3rA81aOHX3K1hp8T7cDmauG%2F%2Fzueo0%2BNfGv0BaaqKuj5nUQMV%2FFB5ZWXJiksJh1z2OTpPRXPbgq9RQCqvRa9xlPUxQprtCiQngy8V7LOcXGsLt7F3NMKQS58dKfVjqMyYNXoKF0CS4iDOLOApG&X-Amz-Signature=5a8056b539eb6e62f7df6d7ee8d8381474bed96e875d071b0ef56661ae98af15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBD77QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIEyPlKiWFX%2F9o5f8jiIJiVpH0rr2%2FVaGAi0n41QoTEBQAiBvOq54f1z%2BbNhNOlsG%2F0gCozM2n2PPeXUUsWlpEjNl4Cr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMnhRprMGspudQDKrzKtwDZPYBTd0HlGCN0U%2FfU7LmXvApdSmpqtrcUHrkqxtX7PbAGFXyl8EgsAdq%2BwaHTQJ0U5jvDOt1YhOgrbCgt9Yd3xUbFaHUq%2FwJZpAa6Zv4quUmfiRabRtuQ2kptzxwSJhDZpudOdR%2FMoBsSthsO1IWZuYaYCbLKJutOqK3VKGOfvpZd%2FFpoc7uEsBHWHu1wmLpNr58zF26d%2FzsUMGtCbrMPFMus7z3TMFtC0ntL6UDWcNx4Jg7%2F4PNsFt%2B9tfDyCcv70fev3NtjjtGNMewbty%2FrO9lb4aVaFmVCca7gH9G1JB3DIlyqoKqBbHEHxO0RWCePuxTAiRsG1gkvhWJ6tFrWgl4jFMYEatjTDL9n66toTz1XeVsYRpJKyz86CT%2FQrIaMzoqqf5faOYUpaAvBNGfaoHNo6AIzTTaGoBWfDiFNRHcB9KebpnE%2Fjd7cMEUkJRNzghuFlT4zqiN1RLOD1LM3daLeeM%2BnFd5wle0Y1PQ6EiDvnPHnyEyn%2FqTdZ8qV4bA7QBqUu0ktgeO47o0sdMNv1O%2F9RkqSnnZNUN23OjihXgMHwvmiFcmVcvauxz7xUEIxs%2FhkJR1f%2FQXziReSZeN1vAb6UeNYGHIStwLu%2Fp%2FBjR1VZGn%2FQsyhMOxfzYw4bOMvQY6pgGrSiHxIr2Ty93xvODFNfwGIqtmhub1mWJBq9friQSxMNNZ9jBWenkLURADCHaIvUMWWu2TqoMyrJ3rA81aOHX3K1hp8T7cDmauG%2F%2Fzueo0%2BNfGv0BaaqKuj5nUQMV%2FFB5ZWXJiksJh1z2OTpPRXPbgq9RQCqvRa9xlPUxQprtCiQngy8V7LOcXGsLt7F3NMKQS58dKfVjqMyYNXoKF0CS4iDOLOApG&X-Amz-Signature=0c5663cceceef2f3ecc24d9833eabc81d090197ce8a360167e9f98ff3bd4ed3d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ALFGLZV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCICTtoCZRQ4cxEk2B4lwePKYLGn7p736KDfI5QKis%2BYNYAiEA6IZyo12ONsdt4sHK0RJuI%2BhvNgeHG3ulxLOmpbRter4q%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDCw%2BvLIbGevZu61hKSrcA8kFqRceHBi2y8qo0dC%2B9d%2BtWOVR%2F64MaxF71x7pYZfTGvgrBjvIRsz%2Fd%2FMiG5yrbye9EEIdXKTgMLuZLBTFdcoSryO%2BUTfQ3jAAhEPuW17qqtp5AyjdDcpH8omrHHjzgvvDVszVdIcBNxYLErCKGKWjXYia7BKA6U9QIav48Y23HQzoHdu%2BzIqmQGqRoYSCo7RgOV9ATMfKCVxjk2h82zriqfu%2FZ5%2BW8%2Bp48e60qU3w8T2KyLHQCGGhq5yCkj%2FAmhyDEcoSbmmx%2BAU%2BCziPP05sl3jhhxPDIfzg8e6R3DU07wEMyS%2FE%2FHNksNo9B%2FFFVILYdnEa19JFwItMRS4%2BR1PafsappXUkYKVgHTfIy6xn1PxHtWdNwcpG%2FEo8ixZG06GnLhscjVxrHJk5kwWMG00dyNDpJ%2BOoPOl%2FlvNg%2BFaTYCp1nWB%2Bz65j6gvVTW%2Fcs3bGh0sfC4CbN41vxesK0N8v0IUnJcGkbWH0HDwx6Hs%2BC%2FoYe4NaPaOoLxfgORr6AOaThL9F238S4UEUeBx6tleTnjOKiEfLsen7OWCVGArWdSxfuOAHiq3JHScZitqILTnbahAzqwrmrTiGQ6Up81vnlQTgusy5BZ%2F2RvSh61kC4Ko9K6UfANAz9OE%2FMNmzjL0GOqUBV3Jg%2FLuPDbJdF%2BnEW4WVUEOf1PcJ9CBtSb2g206h3zs%2FGuv7T1hw9HapHMB1Iq1y0ENEpZQaY0pN4cqte5zN59CiR21oP7edCxi0Is9LGkqDNPfbKU6ZcVeuuIGjg9bF1a43n4vwB%2FSaX4M8y4fPnEJF6swZGWrNObWvQThjOsyDpludRYU9P1l5qDI2p0Vni3KmX922yu6g%2BHb28%2FQywwqNePc9&X-Amz-Signature=ab91e64d5aa5f72f531ce43b1586a43d36bf1a0da5d3aedbfa6a4c6b51d61693&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMGHOHPQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQDUddrNBOS3Ck1Pc%2BctJ1n78yYCyepM9tWl%2BiINFF8EqwIgYzM0wapMEA3cbgnOM5KuL%2FQPTJoo8rl2tFJhV6jzDhUq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDJ8YLAq5jytzIWJsDircA8h%2FMZi2gTRcxtItjHZHjz2fE5Y1thQZR%2BSKTRGqO65xSoN3mLBuFZTc42xWdUjg0UFp1Sceb%2FGtUXigCz9XdE75n0AJ8A%2BBZi1ZOt6UBsM5yarUPNtlOa6cPSgmB5G9eaB%2Bhi46H0zEerJs%2F2WDCERJLbyLDSE%2Bm4XDcA6%2FlDNr5%2FgRAZiXHQOlyEyHB9bN4JnzbkProg5ouTV8z4NbyySisUTz8jW1xgkC15YuddP13cz1n1aZ5jNJ5tjrJQc36UsZQ3MTFCIdo0K7M4%2FVDNqAIO3wOJywmQjZAEZLf46mvrgFRTP7tDOTYORNoMK%2FBS8IhRh2OUcK0lusp%2BKwEmbW%2FEKaXsdfTJP3Fept4HZq%2BBPZsEgFMkHmQ%2FPqOzAi9unGkObGJ4XX42rdTeW9xM9n6vR%2BPo9QqRMRAQ3H0UOcETdS992BUGht8M1hMuvFSQ2%2Bp3AoLSr4Wet92uAL9YcbNvRV0zL9%2BSOfiP%2FAXeysXBOmV9lae5PGMQ%2B524PdC52fBaIk0lzKZPAM9i8An4C3JKu3PpCDNl2xtwBwPuelk3I4zL9VRpe2BvTc%2FOM2Ls5c5AFasw%2FgwzQrA8g6uecs06w024HpdCw6NCOVy0aa1uGJ9%2FwvO8RzpBZ%2BMJe1jL0GOqUBvkN5Dn5qCK0sUGyRlafy5sw4%2FyGGpSgo7efvFGKoaB1xN8AitDUVGwNbSuYdNUNqbkg%2FrQm7EpkfAgScRX%2Ftzgjib%2BGk7za0Iqwsn3wakikAtyPzo5mweUflyFHjLkzAiP3bmnqWzPJCgkIXXSjPpnYnl8akApYepKn5YGjGpU3zLTVD5aV44nQAtpPF8iVeXf6JLHD3NDuMhC%2BW%2FDJ%2FHs7%2BcYsa&X-Amz-Signature=189d4dcd4817a6c40964100f74cedda06f84f22906073d580e6b0ad7a80cd531&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBD77QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIEyPlKiWFX%2F9o5f8jiIJiVpH0rr2%2FVaGAi0n41QoTEBQAiBvOq54f1z%2BbNhNOlsG%2F0gCozM2n2PPeXUUsWlpEjNl4Cr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMnhRprMGspudQDKrzKtwDZPYBTd0HlGCN0U%2FfU7LmXvApdSmpqtrcUHrkqxtX7PbAGFXyl8EgsAdq%2BwaHTQJ0U5jvDOt1YhOgrbCgt9Yd3xUbFaHUq%2FwJZpAa6Zv4quUmfiRabRtuQ2kptzxwSJhDZpudOdR%2FMoBsSthsO1IWZuYaYCbLKJutOqK3VKGOfvpZd%2FFpoc7uEsBHWHu1wmLpNr58zF26d%2FzsUMGtCbrMPFMus7z3TMFtC0ntL6UDWcNx4Jg7%2F4PNsFt%2B9tfDyCcv70fev3NtjjtGNMewbty%2FrO9lb4aVaFmVCca7gH9G1JB3DIlyqoKqBbHEHxO0RWCePuxTAiRsG1gkvhWJ6tFrWgl4jFMYEatjTDL9n66toTz1XeVsYRpJKyz86CT%2FQrIaMzoqqf5faOYUpaAvBNGfaoHNo6AIzTTaGoBWfDiFNRHcB9KebpnE%2Fjd7cMEUkJRNzghuFlT4zqiN1RLOD1LM3daLeeM%2BnFd5wle0Y1PQ6EiDvnPHnyEyn%2FqTdZ8qV4bA7QBqUu0ktgeO47o0sdMNv1O%2F9RkqSnnZNUN23OjihXgMHwvmiFcmVcvauxz7xUEIxs%2FhkJR1f%2FQXziReSZeN1vAb6UeNYGHIStwLu%2Fp%2FBjR1VZGn%2FQsyhMOxfzYw4bOMvQY6pgGrSiHxIr2Ty93xvODFNfwGIqtmhub1mWJBq9friQSxMNNZ9jBWenkLURADCHaIvUMWWu2TqoMyrJ3rA81aOHX3K1hp8T7cDmauG%2F%2Fzueo0%2BNfGv0BaaqKuj5nUQMV%2FFB5ZWXJiksJh1z2OTpPRXPbgq9RQCqvRa9xlPUxQprtCiQngy8V7LOcXGsLt7F3NMKQS58dKfVjqMyYNXoKF0CS4iDOLOApG&X-Amz-Signature=21e2fd5b03f48e9b81d9be236d3f386776001863b593d7fd4b3c346904106471&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBD77QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIEyPlKiWFX%2F9o5f8jiIJiVpH0rr2%2FVaGAi0n41QoTEBQAiBvOq54f1z%2BbNhNOlsG%2F0gCozM2n2PPeXUUsWlpEjNl4Cr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMnhRprMGspudQDKrzKtwDZPYBTd0HlGCN0U%2FfU7LmXvApdSmpqtrcUHrkqxtX7PbAGFXyl8EgsAdq%2BwaHTQJ0U5jvDOt1YhOgrbCgt9Yd3xUbFaHUq%2FwJZpAa6Zv4quUmfiRabRtuQ2kptzxwSJhDZpudOdR%2FMoBsSthsO1IWZuYaYCbLKJutOqK3VKGOfvpZd%2FFpoc7uEsBHWHu1wmLpNr58zF26d%2FzsUMGtCbrMPFMus7z3TMFtC0ntL6UDWcNx4Jg7%2F4PNsFt%2B9tfDyCcv70fev3NtjjtGNMewbty%2FrO9lb4aVaFmVCca7gH9G1JB3DIlyqoKqBbHEHxO0RWCePuxTAiRsG1gkvhWJ6tFrWgl4jFMYEatjTDL9n66toTz1XeVsYRpJKyz86CT%2FQrIaMzoqqf5faOYUpaAvBNGfaoHNo6AIzTTaGoBWfDiFNRHcB9KebpnE%2Fjd7cMEUkJRNzghuFlT4zqiN1RLOD1LM3daLeeM%2BnFd5wle0Y1PQ6EiDvnPHnyEyn%2FqTdZ8qV4bA7QBqUu0ktgeO47o0sdMNv1O%2F9RkqSnnZNUN23OjihXgMHwvmiFcmVcvauxz7xUEIxs%2FhkJR1f%2FQXziReSZeN1vAb6UeNYGHIStwLu%2Fp%2FBjR1VZGn%2FQsyhMOxfzYw4bOMvQY6pgGrSiHxIr2Ty93xvODFNfwGIqtmhub1mWJBq9friQSxMNNZ9jBWenkLURADCHaIvUMWWu2TqoMyrJ3rA81aOHX3K1hp8T7cDmauG%2F%2Fzueo0%2BNfGv0BaaqKuj5nUQMV%2FFB5ZWXJiksJh1z2OTpPRXPbgq9RQCqvRa9xlPUxQprtCiQngy8V7LOcXGsLt7F3NMKQS58dKfVjqMyYNXoKF0CS4iDOLOApG&X-Amz-Signature=65443266dce9f636e01d9b6e262113b32be95f038ffeef39bdda8da2b052edab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBD77QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIEyPlKiWFX%2F9o5f8jiIJiVpH0rr2%2FVaGAi0n41QoTEBQAiBvOq54f1z%2BbNhNOlsG%2F0gCozM2n2PPeXUUsWlpEjNl4Cr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMnhRprMGspudQDKrzKtwDZPYBTd0HlGCN0U%2FfU7LmXvApdSmpqtrcUHrkqxtX7PbAGFXyl8EgsAdq%2BwaHTQJ0U5jvDOt1YhOgrbCgt9Yd3xUbFaHUq%2FwJZpAa6Zv4quUmfiRabRtuQ2kptzxwSJhDZpudOdR%2FMoBsSthsO1IWZuYaYCbLKJutOqK3VKGOfvpZd%2FFpoc7uEsBHWHu1wmLpNr58zF26d%2FzsUMGtCbrMPFMus7z3TMFtC0ntL6UDWcNx4Jg7%2F4PNsFt%2B9tfDyCcv70fev3NtjjtGNMewbty%2FrO9lb4aVaFmVCca7gH9G1JB3DIlyqoKqBbHEHxO0RWCePuxTAiRsG1gkvhWJ6tFrWgl4jFMYEatjTDL9n66toTz1XeVsYRpJKyz86CT%2FQrIaMzoqqf5faOYUpaAvBNGfaoHNo6AIzTTaGoBWfDiFNRHcB9KebpnE%2Fjd7cMEUkJRNzghuFlT4zqiN1RLOD1LM3daLeeM%2BnFd5wle0Y1PQ6EiDvnPHnyEyn%2FqTdZ8qV4bA7QBqUu0ktgeO47o0sdMNv1O%2F9RkqSnnZNUN23OjihXgMHwvmiFcmVcvauxz7xUEIxs%2FhkJR1f%2FQXziReSZeN1vAb6UeNYGHIStwLu%2Fp%2FBjR1VZGn%2FQsyhMOxfzYw4bOMvQY6pgGrSiHxIr2Ty93xvODFNfwGIqtmhub1mWJBq9friQSxMNNZ9jBWenkLURADCHaIvUMWWu2TqoMyrJ3rA81aOHX3K1hp8T7cDmauG%2F%2Fzueo0%2BNfGv0BaaqKuj5nUQMV%2FFB5ZWXJiksJh1z2OTpPRXPbgq9RQCqvRa9xlPUxQprtCiQngy8V7LOcXGsLt7F3NMKQS58dKfVjqMyYNXoKF0CS4iDOLOApG&X-Amz-Signature=97d04a9c8feb1bbae1ec871954ebb58701275d1b352ff409f54847e1204ea004&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635MLNZXO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQDIcdZORw7sriPE8lSHMptTVO2pT4O53C240svrVh5glAIgGGeqi7ag0Fu%2FNKXzY1Bv97TYIsIfduhKDc%2FsWrPLJdwq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDPgDnswzCa94gsb%2BkircA1bpqSeasImskzLDvMoZBdhGL8pIb6fpero1o3MQw%2BDbeyNwkSYCS0ZcM4dE4Dp0MFjtloXokC2NTQk62HG58v031GU8DGuR2cvm7DzNZpVLoHa7TZ9AikkHm7pjYEEaGIoEUUsOTAphX5T5TUp9%2ByZ1waHDUVySYkp8FUa4yqfeVJRkz51bMQp9Dhr8mHnm5037jMnoAHB37BynUBWv%2Fj00npHtpwYQLDckNAqcSzPQNR4qZoxm3Kcjd7lx5eEMNgezxiPgU1reUix4oN93UOFPwOz%2BLJ3Vk6fZgcjEI0EEYS8CtVu2x3yfEK2UWgQizz3Dol9nxrJUbEKJjWNLDamil0XDUrTlOZkF3h09jOLV6%2FRWz6GMNrSHctYRN8zY5xjybxIi7Eep0TDoYcs9FKhFA0KPtKGDm1vklEPqdNMErrQOBGXDXewmksi8guLqob25Efju8I%2FK2YfuRA98Mi8kL7ZdS0JfNBm40Y5Lr5XRAy5O0gVUR9G0QzihMvZS66aIpsECcWAZhtABYRv0dsczqXI1%2BLHtw0xilLOjzVHKToV8KSR7zVAAjNYPDjYSfb7E0Jz%2FFAzAYtKb%2BZg%2B%2FUEDeUrPVqJiZZy2IexOe9I5ot3nxC4owG%2B%2FzWuLMOOzjL0GOqUBrnFQOGZTlmKAHC2knZf6IIhjm%2FoK4A5nzblmykNQT%2FMFkOQhfarO%2FhEvG%2FRZBqGl8XxIKCXgchuloyV%2BOlG%2F76YW6E86JWmte4dmmD4DVEhIojQpVJgju7tGtgSS4cT2nk78MsoHh9HqNRdrR7qOa%2Fyjtf3uGyGuS9wCv4ckVW7ZenJokRbxF1EsIl2UhH9uSpU4izhvGMAC4XCvvA9A6H6v6JyR&X-Amz-Signature=a311e238b5ffe4da1ee3e749e9768e34e5942c2c2abdcef08a97752169b6fd61&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBUVNU6V%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQDiU2n5Nw%2Ft7zWO%2FmURRB%2BEfGB15S%2FNGj71QU4PUxOYoQIgDMPs%2B60SF5hOIOf8IjuLeGE0AmE6iecpxzvjUQsKbzMq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDFd1girzl6dFTfJLUyrcA7BoESzVXaWNXsNERWLTkBLEVQA4rEqDQ%2B23skAAYmOrWI7eSoKL%2FCV7fJ%2FMJuJAbxTkk64IQH8xlTzSBkktIC%2Fv6i%2BCF2DjoGLecw7%2ByyFVqgWjWxrbRhomvK%2BRIcA4BuYx7h2y6ho6L6Ha%2F5Hfi6%2BSQq%2Fuslz34eiGJaFigPKF44jwKWIuTHk9NVq1hMYwnwj%2FBYr%2BO%2F7w8zJb%2ButIy0GGpuG5s0dBvEQMLifehv8z%2BePRPBZBNeme%2FJHF0izSO8augoAdP8A9JwA54D5y3tw9Ho0utPNRrZWE24KR99chmSmChAwwOqciqeICa%2FZgMyXr1p1oaeIzi4nzEwbyOUKIdjSh0uVwZsUghngVpp0l9U9wxXgawVuFKsj9GiJKwh2n2LuRNaKjp7ZRRrWBFrRiN2UlReXltyo7ketUuNcCXVN464BvMR95RJZ7t6pGTIj8aoqDwGJvrJbWgoVGjbYRERKAX82%2FjewiRoxFH4exQNV1HKaZ0NreyLTNS5aN4liiV3L4D7K%2FKwSvB%2B0IHrmyZeU7qmMdDxIXkkCQc7LUDfHn5znHoWGmmLwARswn35AumOJkuxXzYtmCSHroIQeUKHt0yNPguX4rUMSADovpCJ5%2FutmvsOi7Rt0kMOizjL0GOqUBJ9piHiubpBHKnEdxF8n2anzBwvCNorsMvNsMqYzrudVXYQ9tj8beeCiCe6sKkLKXKuaK878t940gPuXNkmltUkzJEZGUbWiNy4pT%2FzJunpXaNSoIKNOW37i3W9CBT8WDxVy8t0bILtic3dtPUWNhvI9dWprqw9wjzypsdU6fgjkK2euvtxd7Nv3%2B8LjxpEKsKRh4SSdwc12Rcplh9xVkGurjuyhq&X-Amz-Signature=ef98a6e582125489f34d46c2b1a5653dad7674d23591632259dc2811b168f0a9&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4DGDCBH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQCl7veK9xw8Obkrbil0uAJtHVWKTlAmYhg1Bn4x9SOrkgIgV2TBSKXLfJ%2BzExg0gJEB1%2BbptDLWq7sSvFXjo71%2Bfncq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDCo5ZUUPpuRbCvC0oCrcA%2FZP5MbhWiMrGqVMxLJCUEVnS5wL8zfMu2jrZ6%2FcnndCUL%2FUcw%2FxN1AxV%2Fqtfiz%2FppDp6W8pGmL5Iq7g7JE2TVBCDhYgqGRIiR%2BC2jEOOG%2BmbcjScS34723JuJJoNYY8xICFz8irHBfE9IepSxsOkQsyTpYcUtp6XA5pqXExyMzkvrJTZyXkdah6c9SKum12nZNtci%2BXyK%2F4H%2F2G6WpNFQ3hHBwXbR4AWW2MxCW5CoTd3t1KFfk3Nwh82SGsb4yEeCTLrqu%2FMsMSw5twimghAyVvEZhKOLnsymmNvO3dh1SSNLo5m5169Dd4wea4BHFRXmHU%2BPi2jIuUg9w4%2FPVuDK8N97cWvpeBmDVQF3niB2fTAGXK8UPdUOeAcFJaeVJRoVmTYTge%2FASHdYC1vfpQP18gSKNNIKT8uDcoT7F7cS2UlkS9v%2FyBALYblI414W44WN1cEEUtMGSgu6pKd%2BUFfrdcYA5Oy70ewXHoo2KkmHg6FvT3GWJh8AW%2B8HAYPuAjQ5V%2BN7uuQOfVDTeYEL3JDPjKhqZOAhj6CdtaWGniCgKJ11SFbKlIQpbEjWDrcduQ6EN6eD5vWc%2BItGc6QIHvAVgAt6BBx6Ek0MsguWMyXXvALVh9HpgFkpfIVin0MMazjL0GOqUB%2Bou2V%2BRk7hk8gqoAJtUWRHraVIxAVqvT8VZexwiLoJayjysvRmzsdieWLKxAAvdcm2ILn9Lw0%2FTCY8GPjmNamBCGPcrPFKg2vNj4TUEfy3KNXUXkKvtNNb17pj6h4%2B3iQB9yiqHe502vj5XBoNsamJwCDMaP499IByRDUL5cUcfvdFMu6vsY6dZw0aCkNWuwYYiEltJSpil1gfzX4QfF9tp28WNh&X-Amz-Signature=90cca5194cad3de060a80c077acd3f0c038b554f998c8bfcaaa3017d1cda900c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2NCJUY7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIGuc6s23FRXnkGONeLC%2F9rvokL3D4WUYx6GJ6rZAFbLwAiBc0wCzKHThPGhEY0f0Y2nGx9Umi0lXQNQtAYC6Lse9ZSr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMrbty4CLL%2Fi%2Bz5P%2FYKtwD12KeHw6E2hIlS0NL1%2BvFLdIyd5xLtLKMqulqfkqGYKOHmUpaTwPizvjxZeHMvzoqEhaiK7mna4CBf3pWHQ5RnPbCsXUwRorXko8UDCoKFfzq263%2BBpgqXeXOQRHLqmgZwZql2KOqrkpFTg4x9QDEFjW4n61VxdeyUfLK3NmZ37WUMT3MQVA5dqsxbydoty6L9d8RFepAFKiPt53sfvG2O%2BEcNZ%2Fx%2Fq%2FNbOYEG3H3U0PUyMRmZcA9Tl3yW35YakKKw9jq8Ufp10t8LEWqOrpYXkZjZ4%2F6%2Bqis5ZsWnfBt%2Fl6a8dyDvxw3i%2F3QEbeQa6B4E8P%2BosyY%2FbcYSrBkwsvfirJp0wGi9J2pkhpyvauoZ0qPPNRThi1zEh1xNvDtUPtA3XJDBpOrodoAEIPm6VOMrgR9Fyn9hSPf5MYRq6PkLAU2P1wvYLtRe6uU5J7lDCiFEbASiLGyM6eubHvbsvsq7k8ojkM5Y5EHqYrEyx68haY9U%2F37Fa0yyBFuk8Phk%2B24WwXZo8BEy%2B9jCyG1Ga8V1JMzVYDTtoEQwx5tKwjQw%2BKjS2Y8iMXtI2WuZcVT6Xu2DlPfRce5Jbrt6kQ4n1p5%2F9rTjYaoyHcJCG1te0S4GWd9DgpXHwL8xYcoWmkwlrWMvQY6pgFLOEiD58kV67J8lXhfPinO85XNzB%2Fx2zlY530%2F%2FjeDi%2FdU9AGWNRQvJ93GrKtHENUbYsx%2FeyifARaNntU2rhYNZz%2Bt%2BgOoHhi13xKujhK673ydvFQiMegSak0b963nMLqWERNRMknsC206YvEtkgo93YwhipX%2BLrpjWz%2B1ZRWDf2r%2FBPNVZywicKOboucLu%2FpUpf9twc8%2Bop3twW2hNHlMbuWj9uMR&X-Amz-Signature=5c5b37830c3b90669f952ffcf76cfd773f837fba3b7103bcfbe9a0737e9ff81d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2NCJUY7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCIGuc6s23FRXnkGONeLC%2F9rvokL3D4WUYx6GJ6rZAFbLwAiBc0wCzKHThPGhEY0f0Y2nGx9Umi0lXQNQtAYC6Lse9ZSr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMrbty4CLL%2Fi%2Bz5P%2FYKtwD12KeHw6E2hIlS0NL1%2BvFLdIyd5xLtLKMqulqfkqGYKOHmUpaTwPizvjxZeHMvzoqEhaiK7mna4CBf3pWHQ5RnPbCsXUwRorXko8UDCoKFfzq263%2BBpgqXeXOQRHLqmgZwZql2KOqrkpFTg4x9QDEFjW4n61VxdeyUfLK3NmZ37WUMT3MQVA5dqsxbydoty6L9d8RFepAFKiPt53sfvG2O%2BEcNZ%2Fx%2Fq%2FNbOYEG3H3U0PUyMRmZcA9Tl3yW35YakKKw9jq8Ufp10t8LEWqOrpYXkZjZ4%2F6%2Bqis5ZsWnfBt%2Fl6a8dyDvxw3i%2F3QEbeQa6B4E8P%2BosyY%2FbcYSrBkwsvfirJp0wGi9J2pkhpyvauoZ0qPPNRThi1zEh1xNvDtUPtA3XJDBpOrodoAEIPm6VOMrgR9Fyn9hSPf5MYRq6PkLAU2P1wvYLtRe6uU5J7lDCiFEbASiLGyM6eubHvbsvsq7k8ojkM5Y5EHqYrEyx68haY9U%2F37Fa0yyBFuk8Phk%2B24WwXZo8BEy%2B9jCyG1Ga8V1JMzVYDTtoEQwx5tKwjQw%2BKjS2Y8iMXtI2WuZcVT6Xu2DlPfRce5Jbrt6kQ4n1p5%2F9rTjYaoyHcJCG1te0S4GWd9DgpXHwL8xYcoWmkwlrWMvQY6pgFLOEiD58kV67J8lXhfPinO85XNzB%2Fx2zlY530%2F%2FjeDi%2FdU9AGWNRQvJ93GrKtHENUbYsx%2FeyifARaNntU2rhYNZz%2Bt%2BgOoHhi13xKujhK673ydvFQiMegSak0b963nMLqWERNRMknsC206YvEtkgo93YwhipX%2BLrpjWz%2B1ZRWDf2r%2FBPNVZywicKOboucLu%2FpUpf9twc8%2Bop3twW2hNHlMbuWj9uMR&X-Amz-Signature=d187fbd00840d859c987ef2cad02662d3dd9a44143b686dd149e2b59c12f5dd5&X-Amz-SignedHeaders=host&x-id=GetObject)

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
