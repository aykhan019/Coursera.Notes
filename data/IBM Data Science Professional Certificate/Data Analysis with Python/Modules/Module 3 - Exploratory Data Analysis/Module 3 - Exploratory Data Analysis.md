

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E77U7LO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQDXkbKgQAlXFw00O943DHQ9XpYIMJhFIra28i8J%2ByM1fwIhALwbvGMFGw93wbGPhcgiTGlCQKLbBg5c5VnI7scuTq9cKv8DCF0QABoMNjM3NDIzMTgzODA1Igxto4L37zIeTwC7zRwq3AOTdJLotWCttJo5yf%2FlwNQJLBIn5yYISXWSGA63eerVSSgCKZE1jCn7CgkrYWS4lobvflzBNpnMceAzMg1aNBFeTVTCMkArsysbUlzl59btCzqdQD9iBC8sB1ZoV%2FILJKzbiaZYyQsN1ROnBGsafEy4HmyTmJs8%2BS440HX%2BtLVzPPcbOch3rezklks5gqWEvO9o9tEDNfZqQy2RFh77FD3x08OkkOucuIle39OQeCLdiUTDPTFEq6IozNaLjkQkFmT2CAp8ErQXK9MTFI3VHsqMpPNrlfpjAHd%2F5iLHG2pzsqezEiaWLBBVw3N2VtZSThdiffh3bGGP53R1d9%2FOB%2Bhm1NF8iKw6zI6lhBbcL2MJDQfUOLLCQgny8GY%2BULzS019651bVJXWbG9z0wyBgLXgZRC%2FVAH1CJeuHZx4RbdWIrDnSd5nTRQ3QHAFwugLaB1te%2BBCgL5Bt2IENE6yaJ1%2FmU1osK4hjuzE7pmttOKr%2FS0Nn%2B10Ji7nP2pETln3qHQ0Zrd0fdSdCDIC%2FmGLWrHNYyjbOtuZ0hC71KBN%2F8YPCNM9NjIF7FqOFghb5lpNc7dCUuTPE8FWr7e4z4C1LjLd0w4wh4mX7NFS3uCm5d0nhjPX3RTbZZcTrFSwqMDDCw5K9BjqkARuHWttVl5RnV1wlgkYlKbToO%2Bm4ilj5oDEPBiywpcrqYOPIWwyJ4WsGA1%2BcxpQ2TGFxELspBcXZkijtkFMnNymVekdMomQJjAMSegoZysSxnax07tBc5GbtCzU3vdP8kbUZtwFPmEzvXDs%2BVRwGaRaOjE0c0ORuevkBg2Q1ZPigu7ujY0wdNH%2Bf381VagQKOi35Zoi5KL%2FLq7uB6zUnK%2BFYQ08F&X-Amz-Signature=b600aa719680ed6622d8c7df1475887d6146b0daed2cc075197d773f0702d271&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E77U7LO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQDXkbKgQAlXFw00O943DHQ9XpYIMJhFIra28i8J%2ByM1fwIhALwbvGMFGw93wbGPhcgiTGlCQKLbBg5c5VnI7scuTq9cKv8DCF0QABoMNjM3NDIzMTgzODA1Igxto4L37zIeTwC7zRwq3AOTdJLotWCttJo5yf%2FlwNQJLBIn5yYISXWSGA63eerVSSgCKZE1jCn7CgkrYWS4lobvflzBNpnMceAzMg1aNBFeTVTCMkArsysbUlzl59btCzqdQD9iBC8sB1ZoV%2FILJKzbiaZYyQsN1ROnBGsafEy4HmyTmJs8%2BS440HX%2BtLVzPPcbOch3rezklks5gqWEvO9o9tEDNfZqQy2RFh77FD3x08OkkOucuIle39OQeCLdiUTDPTFEq6IozNaLjkQkFmT2CAp8ErQXK9MTFI3VHsqMpPNrlfpjAHd%2F5iLHG2pzsqezEiaWLBBVw3N2VtZSThdiffh3bGGP53R1d9%2FOB%2Bhm1NF8iKw6zI6lhBbcL2MJDQfUOLLCQgny8GY%2BULzS019651bVJXWbG9z0wyBgLXgZRC%2FVAH1CJeuHZx4RbdWIrDnSd5nTRQ3QHAFwugLaB1te%2BBCgL5Bt2IENE6yaJ1%2FmU1osK4hjuzE7pmttOKr%2FS0Nn%2B10Ji7nP2pETln3qHQ0Zrd0fdSdCDIC%2FmGLWrHNYyjbOtuZ0hC71KBN%2F8YPCNM9NjIF7FqOFghb5lpNc7dCUuTPE8FWr7e4z4C1LjLd0w4wh4mX7NFS3uCm5d0nhjPX3RTbZZcTrFSwqMDDCw5K9BjqkARuHWttVl5RnV1wlgkYlKbToO%2Bm4ilj5oDEPBiywpcrqYOPIWwyJ4WsGA1%2BcxpQ2TGFxELspBcXZkijtkFMnNymVekdMomQJjAMSegoZysSxnax07tBc5GbtCzU3vdP8kbUZtwFPmEzvXDs%2BVRwGaRaOjE0c0ORuevkBg2Q1ZPigu7ujY0wdNH%2Bf381VagQKOi35Zoi5KL%2FLq7uB6zUnK%2BFYQ08F&X-Amz-Signature=2c742aefb847a7fc3180aa3769faef30a723a2987a8ea6ccf9c0d2d3cb53feb6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E77U7LO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQDXkbKgQAlXFw00O943DHQ9XpYIMJhFIra28i8J%2ByM1fwIhALwbvGMFGw93wbGPhcgiTGlCQKLbBg5c5VnI7scuTq9cKv8DCF0QABoMNjM3NDIzMTgzODA1Igxto4L37zIeTwC7zRwq3AOTdJLotWCttJo5yf%2FlwNQJLBIn5yYISXWSGA63eerVSSgCKZE1jCn7CgkrYWS4lobvflzBNpnMceAzMg1aNBFeTVTCMkArsysbUlzl59btCzqdQD9iBC8sB1ZoV%2FILJKzbiaZYyQsN1ROnBGsafEy4HmyTmJs8%2BS440HX%2BtLVzPPcbOch3rezklks5gqWEvO9o9tEDNfZqQy2RFh77FD3x08OkkOucuIle39OQeCLdiUTDPTFEq6IozNaLjkQkFmT2CAp8ErQXK9MTFI3VHsqMpPNrlfpjAHd%2F5iLHG2pzsqezEiaWLBBVw3N2VtZSThdiffh3bGGP53R1d9%2FOB%2Bhm1NF8iKw6zI6lhBbcL2MJDQfUOLLCQgny8GY%2BULzS019651bVJXWbG9z0wyBgLXgZRC%2FVAH1CJeuHZx4RbdWIrDnSd5nTRQ3QHAFwugLaB1te%2BBCgL5Bt2IENE6yaJ1%2FmU1osK4hjuzE7pmttOKr%2FS0Nn%2B10Ji7nP2pETln3qHQ0Zrd0fdSdCDIC%2FmGLWrHNYyjbOtuZ0hC71KBN%2F8YPCNM9NjIF7FqOFghb5lpNc7dCUuTPE8FWr7e4z4C1LjLd0w4wh4mX7NFS3uCm5d0nhjPX3RTbZZcTrFSwqMDDCw5K9BjqkARuHWttVl5RnV1wlgkYlKbToO%2Bm4ilj5oDEPBiywpcrqYOPIWwyJ4WsGA1%2BcxpQ2TGFxELspBcXZkijtkFMnNymVekdMomQJjAMSegoZysSxnax07tBc5GbtCzU3vdP8kbUZtwFPmEzvXDs%2BVRwGaRaOjE0c0ORuevkBg2Q1ZPigu7ujY0wdNH%2Bf381VagQKOi35Zoi5KL%2FLq7uB6zUnK%2BFYQ08F&X-Amz-Signature=0a0612060e0c6dff1cb24598087d78abce14f11fc37392edb8672de763f9a2ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT2X6L5M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIAvIYLu3%2BvsBjPwFRABQ9%2FxY%2B%2B4X0WfU84If%2B63PAohQAiAeBd92Afbei6t%2F1DrLwJTMo7TsgIM5yfdXGO9Vj5UNair%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMdVDUNrBew9VdxWQBKtwDXArnaKD5vRQWC3Qpn7qRY1fOrpt2bkwfrafSrXyrocFXnW3abncanHlhCOVX2Ml9gAllCj2aC5yedRxqRzUnGXND2Ikf9f4r%2FA7E6u30cialJM359zLbxT0UB1MAONFZCwW9za%2FvtbotJcXUQCxpeDcqvQ4AE%2BdC3yZ5xgJ36Zl5wYU3SPitqDALUtuQ410RJlUGg0MBj5sHGZqfclR6zeFrp5kkkL%2FyYpkasfeYzhvqxgWJx7%2F9MY4ZNwL4X3hnNy2f37DaAD8CYdJGzxXADPMGFlQQrPrgwgKg1tbQgsEJRl6Cf2Q8cuDxuZk2%2FoV%2FOdk1lnnCeAnFZUerfNILa0lDQ715fDg3bD01hlkC7LjqRL%2Fad%2FruC%2FWFLzzfY3e9kUgrpi7PT8aFkaXMcLUFrE12tku6BVDe1xbIRhDhmhtnZhx7V5jyy%2BlVIGzXmnkbve58XAoaB%2BiMQMo4hECrhP9B2CRUI711o%2F7J4j9HO%2BzvaqC81QkGFtXs%2BN24BeRxD6KWyyXEjnN5AcHFJvSpsZ99zAmphOt%2BN7NPr7%2F0ecpZ7Zm61J32sbTDYmgZNvSsKqJ7RMXo0aASNlgaR2o9%2BvTpVijmFX3RVn7y7iEllzBF5E3KmXP%2B1UxaW8wwlMSSvQY6pgEgxkmkyG6lfuj%2FKF3i4%2BaZS67YLBRWA%2FOOEe5kPaJL27MK6ZYDHDhUikKX%2FXbjj0he0tr84av0JiPp9yVpF6IgXHTbYf%2F082w7k%2Fe%2Buq23TWtIFJDHWwb3SY7YmDpLYgMKvYJOA2zFuSLyNfMIsfbgPYhnSlxMbcE5Co6Rnf5oabBsZHfw2Pd9BQYbhFzN6qsPWAi1q2GewSfPpv5Q6HwGUhOTjhEW&X-Amz-Signature=db8c21db92d8f29567b45076e203bdf604e9f9300f35ca89bb0c21ce0a5210a8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT2X6L5M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIAvIYLu3%2BvsBjPwFRABQ9%2FxY%2B%2B4X0WfU84If%2B63PAohQAiAeBd92Afbei6t%2F1DrLwJTMo7TsgIM5yfdXGO9Vj5UNair%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMdVDUNrBew9VdxWQBKtwDXArnaKD5vRQWC3Qpn7qRY1fOrpt2bkwfrafSrXyrocFXnW3abncanHlhCOVX2Ml9gAllCj2aC5yedRxqRzUnGXND2Ikf9f4r%2FA7E6u30cialJM359zLbxT0UB1MAONFZCwW9za%2FvtbotJcXUQCxpeDcqvQ4AE%2BdC3yZ5xgJ36Zl5wYU3SPitqDALUtuQ410RJlUGg0MBj5sHGZqfclR6zeFrp5kkkL%2FyYpkasfeYzhvqxgWJx7%2F9MY4ZNwL4X3hnNy2f37DaAD8CYdJGzxXADPMGFlQQrPrgwgKg1tbQgsEJRl6Cf2Q8cuDxuZk2%2FoV%2FOdk1lnnCeAnFZUerfNILa0lDQ715fDg3bD01hlkC7LjqRL%2Fad%2FruC%2FWFLzzfY3e9kUgrpi7PT8aFkaXMcLUFrE12tku6BVDe1xbIRhDhmhtnZhx7V5jyy%2BlVIGzXmnkbve58XAoaB%2BiMQMo4hECrhP9B2CRUI711o%2F7J4j9HO%2BzvaqC81QkGFtXs%2BN24BeRxD6KWyyXEjnN5AcHFJvSpsZ99zAmphOt%2BN7NPr7%2F0ecpZ7Zm61J32sbTDYmgZNvSsKqJ7RMXo0aASNlgaR2o9%2BvTpVijmFX3RVn7y7iEllzBF5E3KmXP%2B1UxaW8wwlMSSvQY6pgEgxkmkyG6lfuj%2FKF3i4%2BaZS67YLBRWA%2FOOEe5kPaJL27MK6ZYDHDhUikKX%2FXbjj0he0tr84av0JiPp9yVpF6IgXHTbYf%2F082w7k%2Fe%2Buq23TWtIFJDHWwb3SY7YmDpLYgMKvYJOA2zFuSLyNfMIsfbgPYhnSlxMbcE5Co6Rnf5oabBsZHfw2Pd9BQYbhFzN6qsPWAi1q2GewSfPpv5Q6HwGUhOTjhEW&X-Amz-Signature=4ca6cc00a6325796522b2ac9ca7285d9ea4d0437efe9a093be6b4f272b4b4d72&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT2X6L5M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIAvIYLu3%2BvsBjPwFRABQ9%2FxY%2B%2B4X0WfU84If%2B63PAohQAiAeBd92Afbei6t%2F1DrLwJTMo7TsgIM5yfdXGO9Vj5UNair%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMdVDUNrBew9VdxWQBKtwDXArnaKD5vRQWC3Qpn7qRY1fOrpt2bkwfrafSrXyrocFXnW3abncanHlhCOVX2Ml9gAllCj2aC5yedRxqRzUnGXND2Ikf9f4r%2FA7E6u30cialJM359zLbxT0UB1MAONFZCwW9za%2FvtbotJcXUQCxpeDcqvQ4AE%2BdC3yZ5xgJ36Zl5wYU3SPitqDALUtuQ410RJlUGg0MBj5sHGZqfclR6zeFrp5kkkL%2FyYpkasfeYzhvqxgWJx7%2F9MY4ZNwL4X3hnNy2f37DaAD8CYdJGzxXADPMGFlQQrPrgwgKg1tbQgsEJRl6Cf2Q8cuDxuZk2%2FoV%2FOdk1lnnCeAnFZUerfNILa0lDQ715fDg3bD01hlkC7LjqRL%2Fad%2FruC%2FWFLzzfY3e9kUgrpi7PT8aFkaXMcLUFrE12tku6BVDe1xbIRhDhmhtnZhx7V5jyy%2BlVIGzXmnkbve58XAoaB%2BiMQMo4hECrhP9B2CRUI711o%2F7J4j9HO%2BzvaqC81QkGFtXs%2BN24BeRxD6KWyyXEjnN5AcHFJvSpsZ99zAmphOt%2BN7NPr7%2F0ecpZ7Zm61J32sbTDYmgZNvSsKqJ7RMXo0aASNlgaR2o9%2BvTpVijmFX3RVn7y7iEllzBF5E3KmXP%2B1UxaW8wwlMSSvQY6pgEgxkmkyG6lfuj%2FKF3i4%2BaZS67YLBRWA%2FOOEe5kPaJL27MK6ZYDHDhUikKX%2FXbjj0he0tr84av0JiPp9yVpF6IgXHTbYf%2F082w7k%2Fe%2Buq23TWtIFJDHWwb3SY7YmDpLYgMKvYJOA2zFuSLyNfMIsfbgPYhnSlxMbcE5Co6Rnf5oabBsZHfw2Pd9BQYbhFzN6qsPWAi1q2GewSfPpv5Q6HwGUhOTjhEW&X-Amz-Signature=43a51dedb923122cfa6009844756e7b957405f6a17b61ed6f7cc77e7245415c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT2X6L5M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIAvIYLu3%2BvsBjPwFRABQ9%2FxY%2B%2B4X0WfU84If%2B63PAohQAiAeBd92Afbei6t%2F1DrLwJTMo7TsgIM5yfdXGO9Vj5UNair%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMdVDUNrBew9VdxWQBKtwDXArnaKD5vRQWC3Qpn7qRY1fOrpt2bkwfrafSrXyrocFXnW3abncanHlhCOVX2Ml9gAllCj2aC5yedRxqRzUnGXND2Ikf9f4r%2FA7E6u30cialJM359zLbxT0UB1MAONFZCwW9za%2FvtbotJcXUQCxpeDcqvQ4AE%2BdC3yZ5xgJ36Zl5wYU3SPitqDALUtuQ410RJlUGg0MBj5sHGZqfclR6zeFrp5kkkL%2FyYpkasfeYzhvqxgWJx7%2F9MY4ZNwL4X3hnNy2f37DaAD8CYdJGzxXADPMGFlQQrPrgwgKg1tbQgsEJRl6Cf2Q8cuDxuZk2%2FoV%2FOdk1lnnCeAnFZUerfNILa0lDQ715fDg3bD01hlkC7LjqRL%2Fad%2FruC%2FWFLzzfY3e9kUgrpi7PT8aFkaXMcLUFrE12tku6BVDe1xbIRhDhmhtnZhx7V5jyy%2BlVIGzXmnkbve58XAoaB%2BiMQMo4hECrhP9B2CRUI711o%2F7J4j9HO%2BzvaqC81QkGFtXs%2BN24BeRxD6KWyyXEjnN5AcHFJvSpsZ99zAmphOt%2BN7NPr7%2F0ecpZ7Zm61J32sbTDYmgZNvSsKqJ7RMXo0aASNlgaR2o9%2BvTpVijmFX3RVn7y7iEllzBF5E3KmXP%2B1UxaW8wwlMSSvQY6pgEgxkmkyG6lfuj%2FKF3i4%2BaZS67YLBRWA%2FOOEe5kPaJL27MK6ZYDHDhUikKX%2FXbjj0he0tr84av0JiPp9yVpF6IgXHTbYf%2F082w7k%2Fe%2Buq23TWtIFJDHWwb3SY7YmDpLYgMKvYJOA2zFuSLyNfMIsfbgPYhnSlxMbcE5Co6Rnf5oabBsZHfw2Pd9BQYbhFzN6qsPWAi1q2GewSfPpv5Q6HwGUhOTjhEW&X-Amz-Signature=55d2da9393113314c6950b64af3daf973dcd5a5935cc2f6a77d0e26665dbf117&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT2X6L5M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIAvIYLu3%2BvsBjPwFRABQ9%2FxY%2B%2B4X0WfU84If%2B63PAohQAiAeBd92Afbei6t%2F1DrLwJTMo7TsgIM5yfdXGO9Vj5UNair%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMdVDUNrBew9VdxWQBKtwDXArnaKD5vRQWC3Qpn7qRY1fOrpt2bkwfrafSrXyrocFXnW3abncanHlhCOVX2Ml9gAllCj2aC5yedRxqRzUnGXND2Ikf9f4r%2FA7E6u30cialJM359zLbxT0UB1MAONFZCwW9za%2FvtbotJcXUQCxpeDcqvQ4AE%2BdC3yZ5xgJ36Zl5wYU3SPitqDALUtuQ410RJlUGg0MBj5sHGZqfclR6zeFrp5kkkL%2FyYpkasfeYzhvqxgWJx7%2F9MY4ZNwL4X3hnNy2f37DaAD8CYdJGzxXADPMGFlQQrPrgwgKg1tbQgsEJRl6Cf2Q8cuDxuZk2%2FoV%2FOdk1lnnCeAnFZUerfNILa0lDQ715fDg3bD01hlkC7LjqRL%2Fad%2FruC%2FWFLzzfY3e9kUgrpi7PT8aFkaXMcLUFrE12tku6BVDe1xbIRhDhmhtnZhx7V5jyy%2BlVIGzXmnkbve58XAoaB%2BiMQMo4hECrhP9B2CRUI711o%2F7J4j9HO%2BzvaqC81QkGFtXs%2BN24BeRxD6KWyyXEjnN5AcHFJvSpsZ99zAmphOt%2BN7NPr7%2F0ecpZ7Zm61J32sbTDYmgZNvSsKqJ7RMXo0aASNlgaR2o9%2BvTpVijmFX3RVn7y7iEllzBF5E3KmXP%2B1UxaW8wwlMSSvQY6pgEgxkmkyG6lfuj%2FKF3i4%2BaZS67YLBRWA%2FOOEe5kPaJL27MK6ZYDHDhUikKX%2FXbjj0he0tr84av0JiPp9yVpF6IgXHTbYf%2F082w7k%2Fe%2Buq23TWtIFJDHWwb3SY7YmDpLYgMKvYJOA2zFuSLyNfMIsfbgPYhnSlxMbcE5Co6Rnf5oabBsZHfw2Pd9BQYbhFzN6qsPWAi1q2GewSfPpv5Q6HwGUhOTjhEW&X-Amz-Signature=a1247263688fb7638e465bcedf502013b547b0b1701a2ef104fdc0dd7241b7bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT2X6L5M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIAvIYLu3%2BvsBjPwFRABQ9%2FxY%2B%2B4X0WfU84If%2B63PAohQAiAeBd92Afbei6t%2F1DrLwJTMo7TsgIM5yfdXGO9Vj5UNair%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMdVDUNrBew9VdxWQBKtwDXArnaKD5vRQWC3Qpn7qRY1fOrpt2bkwfrafSrXyrocFXnW3abncanHlhCOVX2Ml9gAllCj2aC5yedRxqRzUnGXND2Ikf9f4r%2FA7E6u30cialJM359zLbxT0UB1MAONFZCwW9za%2FvtbotJcXUQCxpeDcqvQ4AE%2BdC3yZ5xgJ36Zl5wYU3SPitqDALUtuQ410RJlUGg0MBj5sHGZqfclR6zeFrp5kkkL%2FyYpkasfeYzhvqxgWJx7%2F9MY4ZNwL4X3hnNy2f37DaAD8CYdJGzxXADPMGFlQQrPrgwgKg1tbQgsEJRl6Cf2Q8cuDxuZk2%2FoV%2FOdk1lnnCeAnFZUerfNILa0lDQ715fDg3bD01hlkC7LjqRL%2Fad%2FruC%2FWFLzzfY3e9kUgrpi7PT8aFkaXMcLUFrE12tku6BVDe1xbIRhDhmhtnZhx7V5jyy%2BlVIGzXmnkbve58XAoaB%2BiMQMo4hECrhP9B2CRUI711o%2F7J4j9HO%2BzvaqC81QkGFtXs%2BN24BeRxD6KWyyXEjnN5AcHFJvSpsZ99zAmphOt%2BN7NPr7%2F0ecpZ7Zm61J32sbTDYmgZNvSsKqJ7RMXo0aASNlgaR2o9%2BvTpVijmFX3RVn7y7iEllzBF5E3KmXP%2B1UxaW8wwlMSSvQY6pgEgxkmkyG6lfuj%2FKF3i4%2BaZS67YLBRWA%2FOOEe5kPaJL27MK6ZYDHDhUikKX%2FXbjj0he0tr84av0JiPp9yVpF6IgXHTbYf%2F082w7k%2Fe%2Buq23TWtIFJDHWwb3SY7YmDpLYgMKvYJOA2zFuSLyNfMIsfbgPYhnSlxMbcE5Co6Rnf5oabBsZHfw2Pd9BQYbhFzN6qsPWAi1q2GewSfPpv5Q6HwGUhOTjhEW&X-Amz-Signature=4b1afffb5c7c336e04f4ea52ce0ce837fb6aeb3a3184084c14a9b3e360516b48&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5ZGJRL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQD3yorAjLcRgAB%2BjIh593e5T6QZQJEdyEXrRYIWgeETigIgB78DlXYF0mnzD8xAxeP0%2FHmQijrufF1DAD5QYRjTP4Iq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDMCFd2dDB4Eop%2FU9OCrcAymB9uRLha2YTE5XPsaTQ1KzGazsd7BH%2FOYkvCtWpM2xtxlyGDt4gcLZqhhkingmx5YLevOqnsZVNQzD%2F0NVjf%2BqNEngiWe3VClBnevpS1rSAJgUJHyr3jqtli1G1kGV4FsR1bgHYdQVgLKA%2F6RFqBdNHpyc5quvrZdY%2F53%2BFSDKQ5153X4X5%2BJmRXbArfUm2XY1fxn8t%2Bjb53zYrs3FApW7cDCKV%2BpxLYY0fAT%2ByxTi2qQ0oDekwk2OYfeAu0aSM4ayM%2B82ntBYUOHmh2NsA16qdNgrFTPW36SYzNInNwQu1Ifq9ovV1IsmZx1PCdacfKIg%2Bd3F0gcsQqT9EQ9JunUVEN9OFQCUvJcKyVor8osdkYqvkEFZzkgq8XqF0UElWnN0Z%2Bde5rmakF8utPGxVe5UALGyGBIu0gMESSGLmgHMoS9oUqr8d%2BCbNkiQZpHimdNFOYcXd4AtygqfjwCoCsqgRyBJcNXa8MjpkCEiCeUEYVpilgKNLffOdsvScgIDNWX0ezMvdHnjV0uWEt9eNr%2FNzpolxLFwpJkeqfDr4puwXpd2vgBc1cWILM%2BCpbtmJyQxwW%2FKJ%2BB7oLZPHSA9LVxtlFXFbKt%2BXai6bBKPfPBrmaUKP9Gg2G2MdgHmMIzEkr0GOqUBBxl3ffEIqQonDA6iZfztarXlPUEwDUzSlktEg6w3earA9vejtQ8qDy4QeL6ExwuolDZzKbCbB4CqkRyR92th8SNJ3fXsM9M61lKL92j7BcA3mxomYz2vOIaJwYvQyqWU6Ct5IcfBPKjf1Pka8wu9OyKGAklVNdG%2F8cp3T6%2FRtZHcxhZB4kJNr8S1rV93kBm0lEVWhZHmMkKjOmNaY6Ve8hy0aaxE&X-Amz-Signature=de6e98e2fd11aeb0c46f023df9bd462e188989098d947451f6990fc1b9e50d1f&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZAQHYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIERxUxvXGgxEUKP5Di4Qs85PCnCY4uBwC%2FyphBGx4J9KAiAd7USQ7VKrtjXHDu5Auy%2B6J7JVBgzaYSBkW4u3VPbO%2Fir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMQ3R9zg9VrzKZeeXrKtwD%2FLgbCZD%2FQqb82PMcMU2hp6QWTr2m7v7nsU5aU68cqij9ib48nsWRUk6%2FjC3uZQ%2FWGElmdLylIcYjIrOTxC2C48KW04D61Xgtn4p91sUsfbBgBQCAtlYk8p5oGiu7f2bA43y7XaZOQlTTz75hXtIVnYM3Gd%2B44YI31OK%2BUQNveyKeQ8RWIz1ptW5EWBRB%2FjklPAAslHe0VEo5V0foj%2Bg3k6n5EyQKOasWPK6HGQUe07dW1J6VITEEZuw5FoI2rVS0DP1cxxPNI9ueCZZtujmV5tA65sEk5f0wl3OiYDpEiJlzsdqeU1qowo%2FAFy%2FJylU8jVqztoF4UtMrI7%2B9chfC0jxvT63dpu5mQ%2B%2BOA5BH7blqbHKbA7534ioklSiHEGetMVuSwWchjaD8jxE8yvRrE6JA8t%2F4AZZ0WW9CTP6kYpuMmEEtF2vIomB5%2BYS0TLl5IIVObFhaRXFUTM9QdptD9z7l8la93JGSHwqtQ49GxjNjjcSBpHeRyKZYQHDapAbzsAeUSo3QlqKyph6%2B9MOS%2BSjED6JVKRMeBj8ZFnSiVjyfFU1cQ8%2BpKslBMKrEKeBtMrNp9hr0xD7C%2BoA4V2HSMD1LhRevrmnLeRgACfZDcpiNM1%2BAwc%2B6k1B5jYkw5cOSvQY6pgHGpfPrJ%2FDXeLp%2F2Z26t8iO3CERCXBdY5neGWCx0HwyaMEA5H6gyO8DPCpsyHaU41AETYJzBN%2FPqT33WWGWXYjT7yiFInv%2BqLcAtmq33sf6ank8XEM8%2FBdsYqj2L7WF7M76h9uMzFSlstlhMhu295ERugCeG93aT%2B%2BoPaWnc6TQtXWkZXwGPlya%2B%2Bsz0A2e0Kz9SP6bsTYXa4QtrHsaPxQ%2F7nbB59Wu&X-Amz-Signature=a370b9a5e4f43acba5cf597bc22a96ef12c1394896ac7f1e5d8ca47d30d8cbed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT2X6L5M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIAvIYLu3%2BvsBjPwFRABQ9%2FxY%2B%2B4X0WfU84If%2B63PAohQAiAeBd92Afbei6t%2F1DrLwJTMo7TsgIM5yfdXGO9Vj5UNair%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMdVDUNrBew9VdxWQBKtwDXArnaKD5vRQWC3Qpn7qRY1fOrpt2bkwfrafSrXyrocFXnW3abncanHlhCOVX2Ml9gAllCj2aC5yedRxqRzUnGXND2Ikf9f4r%2FA7E6u30cialJM359zLbxT0UB1MAONFZCwW9za%2FvtbotJcXUQCxpeDcqvQ4AE%2BdC3yZ5xgJ36Zl5wYU3SPitqDALUtuQ410RJlUGg0MBj5sHGZqfclR6zeFrp5kkkL%2FyYpkasfeYzhvqxgWJx7%2F9MY4ZNwL4X3hnNy2f37DaAD8CYdJGzxXADPMGFlQQrPrgwgKg1tbQgsEJRl6Cf2Q8cuDxuZk2%2FoV%2FOdk1lnnCeAnFZUerfNILa0lDQ715fDg3bD01hlkC7LjqRL%2Fad%2FruC%2FWFLzzfY3e9kUgrpi7PT8aFkaXMcLUFrE12tku6BVDe1xbIRhDhmhtnZhx7V5jyy%2BlVIGzXmnkbve58XAoaB%2BiMQMo4hECrhP9B2CRUI711o%2F7J4j9HO%2BzvaqC81QkGFtXs%2BN24BeRxD6KWyyXEjnN5AcHFJvSpsZ99zAmphOt%2BN7NPr7%2F0ecpZ7Zm61J32sbTDYmgZNvSsKqJ7RMXo0aASNlgaR2o9%2BvTpVijmFX3RVn7y7iEllzBF5E3KmXP%2B1UxaW8wwlMSSvQY6pgEgxkmkyG6lfuj%2FKF3i4%2BaZS67YLBRWA%2FOOEe5kPaJL27MK6ZYDHDhUikKX%2FXbjj0he0tr84av0JiPp9yVpF6IgXHTbYf%2F082w7k%2Fe%2Buq23TWtIFJDHWwb3SY7YmDpLYgMKvYJOA2zFuSLyNfMIsfbgPYhnSlxMbcE5Co6Rnf5oabBsZHfw2Pd9BQYbhFzN6qsPWAi1q2GewSfPpv5Q6HwGUhOTjhEW&X-Amz-Signature=3e5733c41de5b272aa1dec612c07cb9a94c0a9c9996b56084785534a6d8c7305&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT2X6L5M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIAvIYLu3%2BvsBjPwFRABQ9%2FxY%2B%2B4X0WfU84If%2B63PAohQAiAeBd92Afbei6t%2F1DrLwJTMo7TsgIM5yfdXGO9Vj5UNair%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMdVDUNrBew9VdxWQBKtwDXArnaKD5vRQWC3Qpn7qRY1fOrpt2bkwfrafSrXyrocFXnW3abncanHlhCOVX2Ml9gAllCj2aC5yedRxqRzUnGXND2Ikf9f4r%2FA7E6u30cialJM359zLbxT0UB1MAONFZCwW9za%2FvtbotJcXUQCxpeDcqvQ4AE%2BdC3yZ5xgJ36Zl5wYU3SPitqDALUtuQ410RJlUGg0MBj5sHGZqfclR6zeFrp5kkkL%2FyYpkasfeYzhvqxgWJx7%2F9MY4ZNwL4X3hnNy2f37DaAD8CYdJGzxXADPMGFlQQrPrgwgKg1tbQgsEJRl6Cf2Q8cuDxuZk2%2FoV%2FOdk1lnnCeAnFZUerfNILa0lDQ715fDg3bD01hlkC7LjqRL%2Fad%2FruC%2FWFLzzfY3e9kUgrpi7PT8aFkaXMcLUFrE12tku6BVDe1xbIRhDhmhtnZhx7V5jyy%2BlVIGzXmnkbve58XAoaB%2BiMQMo4hECrhP9B2CRUI711o%2F7J4j9HO%2BzvaqC81QkGFtXs%2BN24BeRxD6KWyyXEjnN5AcHFJvSpsZ99zAmphOt%2BN7NPr7%2F0ecpZ7Zm61J32sbTDYmgZNvSsKqJ7RMXo0aASNlgaR2o9%2BvTpVijmFX3RVn7y7iEllzBF5E3KmXP%2B1UxaW8wwlMSSvQY6pgEgxkmkyG6lfuj%2FKF3i4%2BaZS67YLBRWA%2FOOEe5kPaJL27MK6ZYDHDhUikKX%2FXbjj0he0tr84av0JiPp9yVpF6IgXHTbYf%2F082w7k%2Fe%2Buq23TWtIFJDHWwb3SY7YmDpLYgMKvYJOA2zFuSLyNfMIsfbgPYhnSlxMbcE5Co6Rnf5oabBsZHfw2Pd9BQYbhFzN6qsPWAi1q2GewSfPpv5Q6HwGUhOTjhEW&X-Amz-Signature=f80ab0b33f8c31c58d974e9340a94daaa9d2481f6a359b445548916167faecee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT2X6L5M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIAvIYLu3%2BvsBjPwFRABQ9%2FxY%2B%2B4X0WfU84If%2B63PAohQAiAeBd92Afbei6t%2F1DrLwJTMo7TsgIM5yfdXGO9Vj5UNair%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMdVDUNrBew9VdxWQBKtwDXArnaKD5vRQWC3Qpn7qRY1fOrpt2bkwfrafSrXyrocFXnW3abncanHlhCOVX2Ml9gAllCj2aC5yedRxqRzUnGXND2Ikf9f4r%2FA7E6u30cialJM359zLbxT0UB1MAONFZCwW9za%2FvtbotJcXUQCxpeDcqvQ4AE%2BdC3yZ5xgJ36Zl5wYU3SPitqDALUtuQ410RJlUGg0MBj5sHGZqfclR6zeFrp5kkkL%2FyYpkasfeYzhvqxgWJx7%2F9MY4ZNwL4X3hnNy2f37DaAD8CYdJGzxXADPMGFlQQrPrgwgKg1tbQgsEJRl6Cf2Q8cuDxuZk2%2FoV%2FOdk1lnnCeAnFZUerfNILa0lDQ715fDg3bD01hlkC7LjqRL%2Fad%2FruC%2FWFLzzfY3e9kUgrpi7PT8aFkaXMcLUFrE12tku6BVDe1xbIRhDhmhtnZhx7V5jyy%2BlVIGzXmnkbve58XAoaB%2BiMQMo4hECrhP9B2CRUI711o%2F7J4j9HO%2BzvaqC81QkGFtXs%2BN24BeRxD6KWyyXEjnN5AcHFJvSpsZ99zAmphOt%2BN7NPr7%2F0ecpZ7Zm61J32sbTDYmgZNvSsKqJ7RMXo0aASNlgaR2o9%2BvTpVijmFX3RVn7y7iEllzBF5E3KmXP%2B1UxaW8wwlMSSvQY6pgEgxkmkyG6lfuj%2FKF3i4%2BaZS67YLBRWA%2FOOEe5kPaJL27MK6ZYDHDhUikKX%2FXbjj0he0tr84av0JiPp9yVpF6IgXHTbYf%2F082w7k%2Fe%2Buq23TWtIFJDHWwb3SY7YmDpLYgMKvYJOA2zFuSLyNfMIsfbgPYhnSlxMbcE5Co6Rnf5oabBsZHfw2Pd9BQYbhFzN6qsPWAi1q2GewSfPpv5Q6HwGUhOTjhEW&X-Amz-Signature=4a5ecbb07e2285eb00c2f8cad6390e65cd44c99b43c065a807020df9a7f43204&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TMCHS5Y%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQDk%2FkTkHtKjSaxUcw3AGrQplqc6%2FNNMZfFt%2BQeuZ2uf1wIhAKChOSeB0WmIDyae%2Few%2FtYBcs9x0y7UjfDyd9ltBqqK8Kv8DCF0QABoMNjM3NDIzMTgzODA1IgyRpAAghs5glg3uEsYq3APDpF1kHPfevxbi2I0Lpw8lvJl2GomGnvhYzAcbxW7orBWrq9Y%2FtBl5O%2BJvFnNmZgzZuMihUXOmSBU9Osu56ZF8n7CpsNLBVhwGfpy6uFEQfa9QUwwteZsDcnlNAVP4yfK9%2BAdYxsjyrnT9ZQRnKb7uir20gAY3rj4QslLv%2BCGtdHlBRaSUqeI3upSyFSwMsO8DiNRvKKjITD%2Fq9LhJnDvbVOSfN0HngN%2Fm5PVw8qM8XPk%2FSGr%2F9Xb%2Bi8JqXVHN2vAyAvcHa6wrUvAyGQM44vrTKxpwpN5CK85DaLyVqosMUCTbeiRh7IdqSpr2qpmD%2F8f5ooKd4a6Vf9edIfdIcFL%2FRKWRtAuYdjTrEvlQICy0aZlBPGl%2B55yT%2BPkBwSZ8Sb%2FaFDPINR%2F9sP%2Ffg%2BYlaNHbXMAPDcQkjClKda6dhH9DLycbaIIX1jx9BvCo2fxq%2B%2B92%2BIl08xSXjtpjMbevt4ZNPmyvoeCtbIhyrWIwTdqge58oar6le8jGV8EKq452CSAAcxuGZNRNOo5vUa8rBFGrQtUc3JHsPFcE3AHhNbSYw37qlLGG2EpTUVxD57SwerbGcPMtTKRtgxelVjfKPbssaWKdShcuk2lk9LT%2BnGKJWpmNSwpDz07AytMSKjD5w5K9BjqkAQYCh5rmR5YZk64Yc0oDCWGRVGyChKsUd3rdP%2F11a85XedmAOTOpQZRHpC9CKeSXZcjwXYik6pvnL4CjC1pXC1L3d9PFfC32zT5xxDEBEiJMJ9AwQ7roqlHdPH0Dz8ZHlEyC%2BhR%2FHFRtRPoVay4QT%2FsxujGJMYHUUHomxGO%2BGRHAFoU%2BYig0uY5J1xGIx%2BEX7Y%2FZVWmRu%2Bsb4mqeXby5XB0Jkfow&X-Amz-Signature=911d61d5a28bc72f2cc202c2635e827527b77dcd8bc43021b4ec64e68fdec80d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA7K3UXV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQD1mk0PWCvOquXKrgnSXph98HKX6T1miutk8bq%2BpJ793QIhALZTJcJ73q5YSICE8sCI%2BE2ccUY3DdQmNRhcbhdEoiM1Kv8DCF0QABoMNjM3NDIzMTgzODA1IgwjCedr%2B60v%2FeNtMnAq3AOLy8euTx4iHbs2hXEvT42XuUehMg2h8JRcci9eyhOgx5DfeMNUgKuZLSXNSZK4jPwzKDTilziBfmoKDock82KhcXDjAPCqpXeO%2F627d4Yf%2FpnHHAToVOCspqa4dVzf9hKEnDDkCYj8HsAd50iWvt%2FvXZUAvt9dTesnSNdwg1sxQPM%2FSta6BlG2GRf4qndG0Ln214SBfu%2FNdp8ZatoCd1MEfz2ADJupCYeAEO4HIsEQZFAdhJtncv7ERxkOuAs4Xj%2FgKOGL6zLQObXvOGDURUxKMuwxEwHNmQl%2Fb9gcP8ybXgPUBj%2Bf41GATaLYdQ%2FjicI34vQFCXvlyiWXCezeaoi6lW9Z3%2BgalaNF724L71cEkcnSLDvUECwlQyy9BmuSN7pmwL8K%2Ful7XMtgywFkg%2FDBW3zwrqRT3WxxAM%2BL%2BhqvXtVUvHBkHQcKvsNv2ipPbdJ%2B3bESnOO3mgbc%2FYPsTVBIUnidMnBe4t4UDixSim6mXSml%2FPwWFmU4GvU%2BFu%2BLanwR0JsmjjaFfmNgQX5WV2rnCH4ub%2B1RlDBRQaQxL4jRQVaOkX9ct5Eu0f9D2PRpyDWs3zM3eWWmVOkP9LlPfMlYvbiPJSsv7FY6PVxMahu8Jt1yuAj3JqGlI8Pl4jD5w5K9BjqkAVlVzVDhRQhHiP5OkDyigLOlYQwUSCM6IuRJ3dSmuAhhevOcwAbz2vC3zqhPt%2F%2FzxvwTnTKfe%2FQm%2FdrGHJMxZaMXka6eZztneXDkAGb5PzAlhcf94kZ0aSSKoqTtq8574B5sd3HBA5YOAv7vOY5KF280WCOZjhmi1KoBesGLQCZ0V4T2nSrgofCIZyEBSMMvOEeM3tcWDXwp7vou5GrLLq1eoRdK&X-Amz-Signature=6f6a8782b2ba86831d42e2f53a78fc10e14605d0177f3cf130b841ca88590b1d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z4G3VAG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIBPSOkxEKrxPPpYb0zm9DYvwOi70JWOiIMuoy%2FrLmUOrAiEA2rw7BiLmT7oUZAWk5ih%2BoE1s652x%2F5cKe7%2BQxfP%2Buygq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDArs%2FGrA0aPnqvBXsSrcA%2BCkGNfv%2B3pzIk1V%2FHWt5Sai3Xk4i6DDZ9OUg%2BN6Xtn9mwk1ie1iU6uyRPRyv%2FduMrPrzK1QVGm5IW2E5i48Z4O7pW7RoGzr0oUcPti0XW%2FEEg36kCMdn2aWVctD2MWcr%2BK03lwzp1flipCZX0AHmVlVMedtH0Zxn3CKjVlEgsx5dGlmrARRMLlkrPzx6DJX39muNn28HQQWoRmb9tXTc0g1V4HVa8IXL3ilqSoeUr%2B9mQGKgmK%2Fyd5SVE6BaCvlpAU9g2DO%2F09pzm3OxNVhdyENVKaY2868a0UUcD2Q3V2KvB%2BjCw5ersF6S%2FYtSS1clUKsgg6%2BkdbN3JvjgXUWDbem%2FJ2kVLx9DlaHcpWfOnMD%2FCW8lzKta1F8WWDWdWfrXfU05dw5eTIIm8U3RzJkw674AA1C3aRXTsvKcIULHBdq88umEfrHxn6e9LV%2BAZgvv5ZieCR9OBx2bz1aFsGVm30xa8uxt5muF2pWvP3yaw82PX0OfqDKNbHvKlGPu3tCp8ml6QHC5TwKpal4GprSIvrjqeUQnRd5EQZXGav0mkHvX%2FJusVME3F2cWugVFehbRyX5ioNwYVj%2Bl7N5AaF3e3VxmbiobKBwM1fsJCPlAOh7FKasFoXIcbfwh3QdMPbDkr0GOqUBEKboH8vfTLMDgRWcvWSFXFm7W6p6RUMTjxLl6n6mC%2Bd1hQfToXUF2g2T0cZG6Syd%2FjkT9x%2Baq0sPTCDKqBuWdmZOEFBTWHUVqFF%2B2jlj0pXbZs%2B%2FYeqLMr2o2AGUggZB1tqQIZ3tCjMIjLmGZArmfdxo9r2dWGcuVFJOl2I981AOMZp2zZGtf20fy2IdU4Yf%2F6RRdoM6xKR4cFiIbiAiDTRlhdtL&X-Amz-Signature=83b031b33eda3a2caaee092eb2ecfa687033f358d02de8c845c93b558be954a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5ZQTHT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIDhDwL%2BlIoR5rYla3S34ASsl2aIXIen3oIAPrTWwaULOAiEA%2FYA8X5%2FmsKeYcUMXeKJRW5rtsk4vcanKfeRfuSHGLpIq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDONG7XoL9xpIaleiJSrcA6z15XyVT6lE8VZ3SwKgkvf83bVuZvzohSXB9e9iyEEJeDwC3azlB%2BRxzMDcOAO1QnZxBAE6CVn%2BmFrytfsDaBbm3T3Fpb%2FJkpnq0PImxyixe5schBz1nTS5bhkiqBVN63OQfq1XqD5m7kI3niw4%2BGW7hQHr6QAR4ppPMzyF4hhmm98jhtYAEpTJw8FvkaVybb%2BlmDcHYE3uRT%2FSECZ%2FqkNHqedU%2BzZFaGbATJMzlc86Z%2Frmhrem8vh9rGge%2F0ym%2BftayAr2d8zbu%2Fo31VXdGPMyUVgNKo3%2F4BEIhIb%2BMrJDLv%2Fcd8zieeMURK0rdH7NmMCnSttVtluLTAdaXWWvjn1oH76DsJzgtv%2FCbeMBHGwkOeNSTMd10HnHu3jm%2BZ5pyvdVlGCihMywD5Ke7e7%2Bepe3iN3cwQP%2BzUkKCFM%2BYrRHzymbNHqS6up43uPHuJBlFhnmfkHhdYZMl2BfxSYA3olTb4aQ%2B7AnN60Gxietw6X3%2Bl73cOTezw%2FzsjMCUIqWwsVVpkWghur3uaiUnzYuBAW6xuOouNp48%2BOsDRCVrpoFffvAHMF2s3eC%2F6sdXskYHQsSQA5%2FBa1JmaxHVS2DTH8NY7fJV9uIE2AXbmmZZUHCnlwYMFRlwkCz2Qs%2FMPbDkr0GOqUBh5DChi9NjoMg18bYSKPLC7SAvIbklNIguKXjfNvOdXweQvJ9UMuDY6A%2FXCxHzWdNnSygD%2Fe%2BYZOLoPoFPi%2BdRurfEg0Juu%2BiH0C%2BqSTyepOTv940N99N3FvURBMJ8zjnMgsrSGRIbGGNMAfs42NskfrbfP529kD2eXagV%2Ba7lHuBrnXRV3yF3XBsg5sTPQcCL1jyShJbluyXRbPdjSe8U2p1WybM&X-Amz-Signature=9aef3c98ba03e0ff76c3a149d67a671bacd8ae471a7c05cc5cab32e713853c55&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5ZQTHT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIDhDwL%2BlIoR5rYla3S34ASsl2aIXIen3oIAPrTWwaULOAiEA%2FYA8X5%2FmsKeYcUMXeKJRW5rtsk4vcanKfeRfuSHGLpIq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDONG7XoL9xpIaleiJSrcA6z15XyVT6lE8VZ3SwKgkvf83bVuZvzohSXB9e9iyEEJeDwC3azlB%2BRxzMDcOAO1QnZxBAE6CVn%2BmFrytfsDaBbm3T3Fpb%2FJkpnq0PImxyixe5schBz1nTS5bhkiqBVN63OQfq1XqD5m7kI3niw4%2BGW7hQHr6QAR4ppPMzyF4hhmm98jhtYAEpTJw8FvkaVybb%2BlmDcHYE3uRT%2FSECZ%2FqkNHqedU%2BzZFaGbATJMzlc86Z%2Frmhrem8vh9rGge%2F0ym%2BftayAr2d8zbu%2Fo31VXdGPMyUVgNKo3%2F4BEIhIb%2BMrJDLv%2Fcd8zieeMURK0rdH7NmMCnSttVtluLTAdaXWWvjn1oH76DsJzgtv%2FCbeMBHGwkOeNSTMd10HnHu3jm%2BZ5pyvdVlGCihMywD5Ke7e7%2Bepe3iN3cwQP%2BzUkKCFM%2BYrRHzymbNHqS6up43uPHuJBlFhnmfkHhdYZMl2BfxSYA3olTb4aQ%2B7AnN60Gxietw6X3%2Bl73cOTezw%2FzsjMCUIqWwsVVpkWghur3uaiUnzYuBAW6xuOouNp48%2BOsDRCVrpoFffvAHMF2s3eC%2F6sdXskYHQsSQA5%2FBa1JmaxHVS2DTH8NY7fJV9uIE2AXbmmZZUHCnlwYMFRlwkCz2Qs%2FMPbDkr0GOqUBh5DChi9NjoMg18bYSKPLC7SAvIbklNIguKXjfNvOdXweQvJ9UMuDY6A%2FXCxHzWdNnSygD%2Fe%2BYZOLoPoFPi%2BdRurfEg0Juu%2BiH0C%2BqSTyepOTv940N99N3FvURBMJ8zjnMgsrSGRIbGGNMAfs42NskfrbfP529kD2eXagV%2Ba7lHuBrnXRV3yF3XBsg5sTPQcCL1jyShJbluyXRbPdjSe8U2p1WybM&X-Amz-Signature=37a4db0c5f5afc3684083c28a486ebb51592acc9a9e2f69f89a37807bb3e1979&X-Amz-SignedHeaders=host&x-id=GetObject)

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
