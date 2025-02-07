

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4CFP57X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIFbQ%2B7ttdhWIKxplDTP05WApTkB85O7lYvMD20dIBTBfAiBE1tRCI%2BdsCGqa6Sw6l49si3sIepx4wm89CeIJSyxC5Cr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMrtbmd9clEKuRiWZFKtwDsjT5SwUPhQTvqatZtpyM96xNulL0FMQvEpIHWRpwK6Y7hqd47VQ8hPsNXCzNBD%2F%2FnPaWL1JecsrDm1eG7lTQaUR9PTtpNX55ncqf6u3BSw%2Bo7f3YQQTPFtLeDLVhJ1X8n6nfKdYnF1YLuf%2FEFaBm6N2z3hd4Jm1Yp484uecHKS2qiVAiGI99z6PLcWU3x420cE5aDuCjHG9f%2BlVQy1oj9qkIm%2BBKGzlSMEQ1kUr2lcwyhIfSKBYL67lI%2BcyKr7cqKtDb9sz05qGqA5mEBdXyqNXQOuict6Lue5uE%2FOVy2io%2B60ep3qYWb%2BR3hNYksyRncUqVMLsepjneIRN%2BK9Rv1IABRLeVvEavJaWj98mbE7QaDh7J7W8tXifvgNXL6AtXvsxMB4%2Bwh0OMG0XNUTYT9zyHZRQ1KNQcXzqraXR%2Fdop8jm2luiVcQld1uxjaIsDevFSYI91mSYi9wtQExrzhtUrM%2FV69aUBq9phZisLDWLA4xR2jjZFY6Jc798hQ9bgR1q9VDXOalPO%2FL6fvQwl6vrlu8JxSEpGGcpuEbMoORAR%2BJHx%2FpTT14XQT8ynRKsC9K5zBm0e%2FmR%2BZM9ig%2Bbah%2F2ubjqszzFr6yfEXf1PW8mNZQUxKH7TU8XZfTNwwgvqWvQY6pgG%2FAbT2OXQ%2F3%2F8iVx5rgAZrstERi8ZZQIBQ2KF9uT2Rr5p3NNESU1bM539nWR%2FiVkNifk9%2FbJZZ0AnYBVfK8%2Fe%2BDIuAr%2Bq0RnJ1VP01%2Bx8wmJjdlTxwSpo%2Flabaurj%2F4LC24ltBpvlgr7peSlblaDx35EH80860tAQ%2FrS0vmgatxQXN%2B1k89G%2FQvL97SKmQNNAHts%2F9FOyaCiLfAw5s7F4fl49%2BMSrx&X-Amz-Signature=be20fd52fcc977583c23a6112498995b074f27b26418bddae20b848b6b771f15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4CFP57X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIFbQ%2B7ttdhWIKxplDTP05WApTkB85O7lYvMD20dIBTBfAiBE1tRCI%2BdsCGqa6Sw6l49si3sIepx4wm89CeIJSyxC5Cr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMrtbmd9clEKuRiWZFKtwDsjT5SwUPhQTvqatZtpyM96xNulL0FMQvEpIHWRpwK6Y7hqd47VQ8hPsNXCzNBD%2F%2FnPaWL1JecsrDm1eG7lTQaUR9PTtpNX55ncqf6u3BSw%2Bo7f3YQQTPFtLeDLVhJ1X8n6nfKdYnF1YLuf%2FEFaBm6N2z3hd4Jm1Yp484uecHKS2qiVAiGI99z6PLcWU3x420cE5aDuCjHG9f%2BlVQy1oj9qkIm%2BBKGzlSMEQ1kUr2lcwyhIfSKBYL67lI%2BcyKr7cqKtDb9sz05qGqA5mEBdXyqNXQOuict6Lue5uE%2FOVy2io%2B60ep3qYWb%2BR3hNYksyRncUqVMLsepjneIRN%2BK9Rv1IABRLeVvEavJaWj98mbE7QaDh7J7W8tXifvgNXL6AtXvsxMB4%2Bwh0OMG0XNUTYT9zyHZRQ1KNQcXzqraXR%2Fdop8jm2luiVcQld1uxjaIsDevFSYI91mSYi9wtQExrzhtUrM%2FV69aUBq9phZisLDWLA4xR2jjZFY6Jc798hQ9bgR1q9VDXOalPO%2FL6fvQwl6vrlu8JxSEpGGcpuEbMoORAR%2BJHx%2FpTT14XQT8ynRKsC9K5zBm0e%2FmR%2BZM9ig%2Bbah%2F2ubjqszzFr6yfEXf1PW8mNZQUxKH7TU8XZfTNwwgvqWvQY6pgG%2FAbT2OXQ%2F3%2F8iVx5rgAZrstERi8ZZQIBQ2KF9uT2Rr5p3NNESU1bM539nWR%2FiVkNifk9%2FbJZZ0AnYBVfK8%2Fe%2BDIuAr%2Bq0RnJ1VP01%2Bx8wmJjdlTxwSpo%2Flabaurj%2F4LC24ltBpvlgr7peSlblaDx35EH80860tAQ%2FrS0vmgatxQXN%2B1k89G%2FQvL97SKmQNNAHts%2F9FOyaCiLfAw5s7F4fl49%2BMSrx&X-Amz-Signature=f909f76c388150d160b2eed5b2732202b661c156439a40ed09be771e2949256a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4CFP57X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIFbQ%2B7ttdhWIKxplDTP05WApTkB85O7lYvMD20dIBTBfAiBE1tRCI%2BdsCGqa6Sw6l49si3sIepx4wm89CeIJSyxC5Cr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMrtbmd9clEKuRiWZFKtwDsjT5SwUPhQTvqatZtpyM96xNulL0FMQvEpIHWRpwK6Y7hqd47VQ8hPsNXCzNBD%2F%2FnPaWL1JecsrDm1eG7lTQaUR9PTtpNX55ncqf6u3BSw%2Bo7f3YQQTPFtLeDLVhJ1X8n6nfKdYnF1YLuf%2FEFaBm6N2z3hd4Jm1Yp484uecHKS2qiVAiGI99z6PLcWU3x420cE5aDuCjHG9f%2BlVQy1oj9qkIm%2BBKGzlSMEQ1kUr2lcwyhIfSKBYL67lI%2BcyKr7cqKtDb9sz05qGqA5mEBdXyqNXQOuict6Lue5uE%2FOVy2io%2B60ep3qYWb%2BR3hNYksyRncUqVMLsepjneIRN%2BK9Rv1IABRLeVvEavJaWj98mbE7QaDh7J7W8tXifvgNXL6AtXvsxMB4%2Bwh0OMG0XNUTYT9zyHZRQ1KNQcXzqraXR%2Fdop8jm2luiVcQld1uxjaIsDevFSYI91mSYi9wtQExrzhtUrM%2FV69aUBq9phZisLDWLA4xR2jjZFY6Jc798hQ9bgR1q9VDXOalPO%2FL6fvQwl6vrlu8JxSEpGGcpuEbMoORAR%2BJHx%2FpTT14XQT8ynRKsC9K5zBm0e%2FmR%2BZM9ig%2Bbah%2F2ubjqszzFr6yfEXf1PW8mNZQUxKH7TU8XZfTNwwgvqWvQY6pgG%2FAbT2OXQ%2F3%2F8iVx5rgAZrstERi8ZZQIBQ2KF9uT2Rr5p3NNESU1bM539nWR%2FiVkNifk9%2FbJZZ0AnYBVfK8%2Fe%2BDIuAr%2Bq0RnJ1VP01%2Bx8wmJjdlTxwSpo%2Flabaurj%2F4LC24ltBpvlgr7peSlblaDx35EH80860tAQ%2FrS0vmgatxQXN%2B1k89G%2FQvL97SKmQNNAHts%2F9FOyaCiLfAw5s7F4fl49%2BMSrx&X-Amz-Signature=97ff019aed3550fe1d494d03d9b9cceee54611f2489d82d9e5755a8ea270a423&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O6HS37O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIEyd2nsmyGYSj4q7QrZZET7efKnqY4zzYpxtHO0FX2rJAiB2Y4KGOo9rY8OVhR0OZQpSr0yq4yDFiJv%2BUbZ3UbVbBSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMXR%2FSPLSsT9LQIkI1KtwD4U3hzzsajDw7XZK%2FFA9EGk8m4lfDKMSLJkk%2FEnJKR0Mm%2Fe8jMR%2FuVkPYrm0vxR6394w5nHXJpjX%2B6HkXmgY4i5IKrK8ZthCY1OwgPowV9oDPzPMANXDTEG5Rif0M2OJspi1WZArt0IJ%2BuGIYtQTROehjUuyCTPoFY84AMTO2IhJ3X9EDQkM1sgkX3oVFC0xf4xp5kB%2F5DEKQS0GVjL4ucaJs3KPtQTQrcGQ%2Ff8fkSvrYYi3sOr10LMb5KWTMtQr8M4smMnXISCzA%2BYcLk2mS3aXI7DstUPTfT4fUjFWttHVjoSgdcUB866v%2BJbCXUgoJu04jCyTNWuCvAyB1V9OG4E0b2PonbiLkC23jnOE%2FjJQ750BU8%2FlOyi%2Bhn4U6PjY1uE%2F%2BGX514DWT7Q09u7eKRgLYq5RtpROYGlWHX0DMC8COcv1ONBxxZFO5l8Jq4Pv3lWEVLDL7Wc125ulnlwX8RvkhMYu1e4Kw%2BCp2%2BTxKSTa67GE00ZMw2k01udD%2FBIZwSoLBTscqbrhLAfinW9ji2c%2FnKep%2F56eLeoHwqIeNcK8lYyx4JbiKd%2BbRTXwRQJ7LvycUG5h1SYGk5fKuHNMtuzjrTYhjWv0GsCzj0CB9404fVpa1APwXwiasECgwgfqWvQY6pgFVdCZnBDn3rvdTdMH5ZvzBE2pfwhKEsukwRWMGqKvJyM%2FWDR75JFbwPR6rscupJXfT97JAk5OOTbv39SWvUTWML7uVlZZ3eFQD1ECmH61ol7MbXEffRU0TZnI1mphxJ053Jy2JGN31oMIpDqCgzFk8qHxNpd%2BqaQggd1dugsNpfw2kFrwo41w6uKBme%2BuPsuP5TWmOeeZ%2FkT1DkZ%2FAEwiRqxF2lDbc&X-Amz-Signature=9d68dddde6206c26043e5e62df96336ebdde276b18ccbdfd66fcf0fcc6a22270&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O6HS37O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIEyd2nsmyGYSj4q7QrZZET7efKnqY4zzYpxtHO0FX2rJAiB2Y4KGOo9rY8OVhR0OZQpSr0yq4yDFiJv%2BUbZ3UbVbBSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMXR%2FSPLSsT9LQIkI1KtwD4U3hzzsajDw7XZK%2FFA9EGk8m4lfDKMSLJkk%2FEnJKR0Mm%2Fe8jMR%2FuVkPYrm0vxR6394w5nHXJpjX%2B6HkXmgY4i5IKrK8ZthCY1OwgPowV9oDPzPMANXDTEG5Rif0M2OJspi1WZArt0IJ%2BuGIYtQTROehjUuyCTPoFY84AMTO2IhJ3X9EDQkM1sgkX3oVFC0xf4xp5kB%2F5DEKQS0GVjL4ucaJs3KPtQTQrcGQ%2Ff8fkSvrYYi3sOr10LMb5KWTMtQr8M4smMnXISCzA%2BYcLk2mS3aXI7DstUPTfT4fUjFWttHVjoSgdcUB866v%2BJbCXUgoJu04jCyTNWuCvAyB1V9OG4E0b2PonbiLkC23jnOE%2FjJQ750BU8%2FlOyi%2Bhn4U6PjY1uE%2F%2BGX514DWT7Q09u7eKRgLYq5RtpROYGlWHX0DMC8COcv1ONBxxZFO5l8Jq4Pv3lWEVLDL7Wc125ulnlwX8RvkhMYu1e4Kw%2BCp2%2BTxKSTa67GE00ZMw2k01udD%2FBIZwSoLBTscqbrhLAfinW9ji2c%2FnKep%2F56eLeoHwqIeNcK8lYyx4JbiKd%2BbRTXwRQJ7LvycUG5h1SYGk5fKuHNMtuzjrTYhjWv0GsCzj0CB9404fVpa1APwXwiasECgwgfqWvQY6pgFVdCZnBDn3rvdTdMH5ZvzBE2pfwhKEsukwRWMGqKvJyM%2FWDR75JFbwPR6rscupJXfT97JAk5OOTbv39SWvUTWML7uVlZZ3eFQD1ECmH61ol7MbXEffRU0TZnI1mphxJ053Jy2JGN31oMIpDqCgzFk8qHxNpd%2BqaQggd1dugsNpfw2kFrwo41w6uKBme%2BuPsuP5TWmOeeZ%2FkT1DkZ%2FAEwiRqxF2lDbc&X-Amz-Signature=1cc39a2d31188f5500d888f80696ef95fb83b26b281158399653c576eb19f160&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O6HS37O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIEyd2nsmyGYSj4q7QrZZET7efKnqY4zzYpxtHO0FX2rJAiB2Y4KGOo9rY8OVhR0OZQpSr0yq4yDFiJv%2BUbZ3UbVbBSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMXR%2FSPLSsT9LQIkI1KtwD4U3hzzsajDw7XZK%2FFA9EGk8m4lfDKMSLJkk%2FEnJKR0Mm%2Fe8jMR%2FuVkPYrm0vxR6394w5nHXJpjX%2B6HkXmgY4i5IKrK8ZthCY1OwgPowV9oDPzPMANXDTEG5Rif0M2OJspi1WZArt0IJ%2BuGIYtQTROehjUuyCTPoFY84AMTO2IhJ3X9EDQkM1sgkX3oVFC0xf4xp5kB%2F5DEKQS0GVjL4ucaJs3KPtQTQrcGQ%2Ff8fkSvrYYi3sOr10LMb5KWTMtQr8M4smMnXISCzA%2BYcLk2mS3aXI7DstUPTfT4fUjFWttHVjoSgdcUB866v%2BJbCXUgoJu04jCyTNWuCvAyB1V9OG4E0b2PonbiLkC23jnOE%2FjJQ750BU8%2FlOyi%2Bhn4U6PjY1uE%2F%2BGX514DWT7Q09u7eKRgLYq5RtpROYGlWHX0DMC8COcv1ONBxxZFO5l8Jq4Pv3lWEVLDL7Wc125ulnlwX8RvkhMYu1e4Kw%2BCp2%2BTxKSTa67GE00ZMw2k01udD%2FBIZwSoLBTscqbrhLAfinW9ji2c%2FnKep%2F56eLeoHwqIeNcK8lYyx4JbiKd%2BbRTXwRQJ7LvycUG5h1SYGk5fKuHNMtuzjrTYhjWv0GsCzj0CB9404fVpa1APwXwiasECgwgfqWvQY6pgFVdCZnBDn3rvdTdMH5ZvzBE2pfwhKEsukwRWMGqKvJyM%2FWDR75JFbwPR6rscupJXfT97JAk5OOTbv39SWvUTWML7uVlZZ3eFQD1ECmH61ol7MbXEffRU0TZnI1mphxJ053Jy2JGN31oMIpDqCgzFk8qHxNpd%2BqaQggd1dugsNpfw2kFrwo41w6uKBme%2BuPsuP5TWmOeeZ%2FkT1DkZ%2FAEwiRqxF2lDbc&X-Amz-Signature=053f16cf74d1d50a5989d8eda118b4dc0edec102f7bd873fa3c66da58a9097f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O6HS37O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIEyd2nsmyGYSj4q7QrZZET7efKnqY4zzYpxtHO0FX2rJAiB2Y4KGOo9rY8OVhR0OZQpSr0yq4yDFiJv%2BUbZ3UbVbBSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMXR%2FSPLSsT9LQIkI1KtwD4U3hzzsajDw7XZK%2FFA9EGk8m4lfDKMSLJkk%2FEnJKR0Mm%2Fe8jMR%2FuVkPYrm0vxR6394w5nHXJpjX%2B6HkXmgY4i5IKrK8ZthCY1OwgPowV9oDPzPMANXDTEG5Rif0M2OJspi1WZArt0IJ%2BuGIYtQTROehjUuyCTPoFY84AMTO2IhJ3X9EDQkM1sgkX3oVFC0xf4xp5kB%2F5DEKQS0GVjL4ucaJs3KPtQTQrcGQ%2Ff8fkSvrYYi3sOr10LMb5KWTMtQr8M4smMnXISCzA%2BYcLk2mS3aXI7DstUPTfT4fUjFWttHVjoSgdcUB866v%2BJbCXUgoJu04jCyTNWuCvAyB1V9OG4E0b2PonbiLkC23jnOE%2FjJQ750BU8%2FlOyi%2Bhn4U6PjY1uE%2F%2BGX514DWT7Q09u7eKRgLYq5RtpROYGlWHX0DMC8COcv1ONBxxZFO5l8Jq4Pv3lWEVLDL7Wc125ulnlwX8RvkhMYu1e4Kw%2BCp2%2BTxKSTa67GE00ZMw2k01udD%2FBIZwSoLBTscqbrhLAfinW9ji2c%2FnKep%2F56eLeoHwqIeNcK8lYyx4JbiKd%2BbRTXwRQJ7LvycUG5h1SYGk5fKuHNMtuzjrTYhjWv0GsCzj0CB9404fVpa1APwXwiasECgwgfqWvQY6pgFVdCZnBDn3rvdTdMH5ZvzBE2pfwhKEsukwRWMGqKvJyM%2FWDR75JFbwPR6rscupJXfT97JAk5OOTbv39SWvUTWML7uVlZZ3eFQD1ECmH61ol7MbXEffRU0TZnI1mphxJ053Jy2JGN31oMIpDqCgzFk8qHxNpd%2BqaQggd1dugsNpfw2kFrwo41w6uKBme%2BuPsuP5TWmOeeZ%2FkT1DkZ%2FAEwiRqxF2lDbc&X-Amz-Signature=04fb483ab591a1dd720815ab8ab16a4dc0158482da7e74bb607a3f8657643213&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O6HS37O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIEyd2nsmyGYSj4q7QrZZET7efKnqY4zzYpxtHO0FX2rJAiB2Y4KGOo9rY8OVhR0OZQpSr0yq4yDFiJv%2BUbZ3UbVbBSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMXR%2FSPLSsT9LQIkI1KtwD4U3hzzsajDw7XZK%2FFA9EGk8m4lfDKMSLJkk%2FEnJKR0Mm%2Fe8jMR%2FuVkPYrm0vxR6394w5nHXJpjX%2B6HkXmgY4i5IKrK8ZthCY1OwgPowV9oDPzPMANXDTEG5Rif0M2OJspi1WZArt0IJ%2BuGIYtQTROehjUuyCTPoFY84AMTO2IhJ3X9EDQkM1sgkX3oVFC0xf4xp5kB%2F5DEKQS0GVjL4ucaJs3KPtQTQrcGQ%2Ff8fkSvrYYi3sOr10LMb5KWTMtQr8M4smMnXISCzA%2BYcLk2mS3aXI7DstUPTfT4fUjFWttHVjoSgdcUB866v%2BJbCXUgoJu04jCyTNWuCvAyB1V9OG4E0b2PonbiLkC23jnOE%2FjJQ750BU8%2FlOyi%2Bhn4U6PjY1uE%2F%2BGX514DWT7Q09u7eKRgLYq5RtpROYGlWHX0DMC8COcv1ONBxxZFO5l8Jq4Pv3lWEVLDL7Wc125ulnlwX8RvkhMYu1e4Kw%2BCp2%2BTxKSTa67GE00ZMw2k01udD%2FBIZwSoLBTscqbrhLAfinW9ji2c%2FnKep%2F56eLeoHwqIeNcK8lYyx4JbiKd%2BbRTXwRQJ7LvycUG5h1SYGk5fKuHNMtuzjrTYhjWv0GsCzj0CB9404fVpa1APwXwiasECgwgfqWvQY6pgFVdCZnBDn3rvdTdMH5ZvzBE2pfwhKEsukwRWMGqKvJyM%2FWDR75JFbwPR6rscupJXfT97JAk5OOTbv39SWvUTWML7uVlZZ3eFQD1ECmH61ol7MbXEffRU0TZnI1mphxJ053Jy2JGN31oMIpDqCgzFk8qHxNpd%2BqaQggd1dugsNpfw2kFrwo41w6uKBme%2BuPsuP5TWmOeeZ%2FkT1DkZ%2FAEwiRqxF2lDbc&X-Amz-Signature=82db52781549759f34201c21e7ab5e8d5c24f87b12f28e52fa705f9dbf37354f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O6HS37O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIEyd2nsmyGYSj4q7QrZZET7efKnqY4zzYpxtHO0FX2rJAiB2Y4KGOo9rY8OVhR0OZQpSr0yq4yDFiJv%2BUbZ3UbVbBSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMXR%2FSPLSsT9LQIkI1KtwD4U3hzzsajDw7XZK%2FFA9EGk8m4lfDKMSLJkk%2FEnJKR0Mm%2Fe8jMR%2FuVkPYrm0vxR6394w5nHXJpjX%2B6HkXmgY4i5IKrK8ZthCY1OwgPowV9oDPzPMANXDTEG5Rif0M2OJspi1WZArt0IJ%2BuGIYtQTROehjUuyCTPoFY84AMTO2IhJ3X9EDQkM1sgkX3oVFC0xf4xp5kB%2F5DEKQS0GVjL4ucaJs3KPtQTQrcGQ%2Ff8fkSvrYYi3sOr10LMb5KWTMtQr8M4smMnXISCzA%2BYcLk2mS3aXI7DstUPTfT4fUjFWttHVjoSgdcUB866v%2BJbCXUgoJu04jCyTNWuCvAyB1V9OG4E0b2PonbiLkC23jnOE%2FjJQ750BU8%2FlOyi%2Bhn4U6PjY1uE%2F%2BGX514DWT7Q09u7eKRgLYq5RtpROYGlWHX0DMC8COcv1ONBxxZFO5l8Jq4Pv3lWEVLDL7Wc125ulnlwX8RvkhMYu1e4Kw%2BCp2%2BTxKSTa67GE00ZMw2k01udD%2FBIZwSoLBTscqbrhLAfinW9ji2c%2FnKep%2F56eLeoHwqIeNcK8lYyx4JbiKd%2BbRTXwRQJ7LvycUG5h1SYGk5fKuHNMtuzjrTYhjWv0GsCzj0CB9404fVpa1APwXwiasECgwgfqWvQY6pgFVdCZnBDn3rvdTdMH5ZvzBE2pfwhKEsukwRWMGqKvJyM%2FWDR75JFbwPR6rscupJXfT97JAk5OOTbv39SWvUTWML7uVlZZ3eFQD1ECmH61ol7MbXEffRU0TZnI1mphxJ053Jy2JGN31oMIpDqCgzFk8qHxNpd%2BqaQggd1dugsNpfw2kFrwo41w6uKBme%2BuPsuP5TWmOeeZ%2FkT1DkZ%2FAEwiRqxF2lDbc&X-Amz-Signature=295d62d41d592979234b53b79a5e16bb4f397a693879611909852d54dd0e4e08&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QOSC54L%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC7VMupRu2F1c%2FBc47ghJb87S7pXNXl652YwVaAXudQYgIhAOeZsZbCwWhh%2F0z0nwVsQp1ohE1TF5wQmEeyrNY77REHKv8DCHEQABoMNjM3NDIzMTgzODA1IgxiVSVmpOJeaf1Y%2BeEq3AMbb%2FDW1n06J749%2B6mYJ1dauykUyuAC0g4VlE8%2Fd%2Fi2zzI57%2BSMUCjFjgCHL3j16klwiux6U2nCDknFzaI4wvtnCoCXHNWwxMI5ya9vBL5vxo5571aydoEUvcVf4CHFWc%2Fx7UVscHI05qLJ5ges73W2hudv2PNGu7yruH21qi5wVLmaOqsc66WOb%2FVhY6Jz7ElzCWmu%2Fq6XWpRHuTJCEqP4h42IXsenyQF%2FuWRArfEUtoT4wxZzqGwMnKv5U7JNTSL13GN6NP1O5VHslpuUt446XtJwUHKVKmw5gk5TFuq%2B5gf7kpw42GbuXx15YpnwiPgCe67Zjt2zEedC0hCqX4T1LsJjIWqbXIBtaXSzB%2FkTOaFM1LrxbgFD2J7mrE3EgVsqF8tUlAQyfgx6y6DhoFFFAmwcxynZNMGxLglOfBi5tWctYOOFO9TwkQXbbzdMjb84%2FZ3GhcbFpTX0D%2ByRg%2F%2FgSzVeyQdFmmIk3oY2EZaKpfCgUeSeiEG2Ce67TPRkfgv06NSIjx7hLv2Om6VWl5OKEefse87LHDf%2Fv2DXu569zHWGqmannmwFIHzQ%2BkXxMsO3cFHbuhRWXPZpZ3AYiFeyGF4DZM%2FT56ngjRHDpgxXxNW%2FalwXSqhcsWqwYzCG%2Bpa9BjqkAXfAEuQVamA4G%2BP1zzM%2BqYiNZuNx6VyHCUF7uVkbEbtxJa6txuPDAEVKQTyFDEw%2FWKN4Bg6yXmOnTN4A5k%2BK6hOd%2BKyzhigYb%2BJB6pzrZpZLRbzLItDP8fMU2JN53Takgn6Q8IBZQRmJ%2FSj1WTrQ2xlT8hTcubCvVRHcwBx1AUSWqgFibNmTtFKdAzUaJae6PDLTwMVL6zSji6Flkuloh6jjZqmj&X-Amz-Signature=a3511045e0b964b1330ff9f5e6e04b49df2745fa3d70b04ea31282415049eb4f&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZ22YMV6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHNzbaPYQ8nWUnhcwykDXMSQ5bmPkEVm47i3ZM5GMi81AiBpy0u5nNPbRhumYtm5leF1j0tc9mGbNtVJuUWXmy8joir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM8xaXCQxJGIJ6l0YKKtwD1zrHedkOOU9%2FzB10x2geQ8yzZVp6D6PBTfmTD1s3PcB8ghjux1mUg7fCMhsbWzghPX2cxeDvZyVUMqyPX9%2BSfaG%2F7kNAUJnPWXzD6PpR4Mrf3Yr3JOyBAZz60PRBE5m5FP%2FyzWZDxZBwQfFaWr%2BRqYONYxKBktje%2BYUjROtyuRAXdWIA7uzanfMekYvEEhit3METBfiXrdlCYaI5mp6%2BiXGmImwakc8SEseBhyAMmOBV9yuy9bvU76j7mmkqUxDSf9D24aoeQQYVeLGrxKOVRgxvqomduSdZ1JeCO9Tw6DHEFN9KR0SP0axsdViVPnN22ZRyksARGAdwYgxq%2FB3tUt7WKR430YjbVQNU86Bvw2t58IHiYYMpptXKEVGMB5pMTTkQ%2B3tTPoXuV3nGMy52YxBr%2B6yAhgdYrUBKPa77qHua6Hu9q8hLv%2BSKHPYn6honroWh2h%2BH%2Bky85PjQquRc2In2UpRBOzuz6tIxri8OC2cy4rWZgwUkLjfpkM%2B47bE2HgtXeQEWH3jdii2XCrwErpZTQHhfrNtzwwMBpQPvKc2kSdSnH9eLjRK0bsRB0bLYSL3ulVYncwIMursDmU158G7sqQ1G2ktw6ISs23JPwEGBN9HkcA5O86m96Uwwy%2FmWvQY6pgG755qlVccFVYUpkr8DnBBrD8XqOjgcLcqg5BzOKznKOaTfyeMuTF3zKQp7nJ9kNH6neOq1NvbG%2F7Gy%2F629eaRcpcI0BBoj%2B3iav8Ll%2FmT1kWxUV2byNiD8AbOVO2eBNvIcK%2F5x66xemq9vf7C3jvLtYoYEAPrXiMNw5e0F%2B4W8%2F3rifF0gLiJZI1o38vuCvLxyySZIANXFECKA7ttffBvWIV2WQNod&X-Amz-Signature=a1598bc188d153c5067c48f600720766bfa5970da21f25ec16cfc00e2a8f8cf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O6HS37O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIEyd2nsmyGYSj4q7QrZZET7efKnqY4zzYpxtHO0FX2rJAiB2Y4KGOo9rY8OVhR0OZQpSr0yq4yDFiJv%2BUbZ3UbVbBSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMXR%2FSPLSsT9LQIkI1KtwD4U3hzzsajDw7XZK%2FFA9EGk8m4lfDKMSLJkk%2FEnJKR0Mm%2Fe8jMR%2FuVkPYrm0vxR6394w5nHXJpjX%2B6HkXmgY4i5IKrK8ZthCY1OwgPowV9oDPzPMANXDTEG5Rif0M2OJspi1WZArt0IJ%2BuGIYtQTROehjUuyCTPoFY84AMTO2IhJ3X9EDQkM1sgkX3oVFC0xf4xp5kB%2F5DEKQS0GVjL4ucaJs3KPtQTQrcGQ%2Ff8fkSvrYYi3sOr10LMb5KWTMtQr8M4smMnXISCzA%2BYcLk2mS3aXI7DstUPTfT4fUjFWttHVjoSgdcUB866v%2BJbCXUgoJu04jCyTNWuCvAyB1V9OG4E0b2PonbiLkC23jnOE%2FjJQ750BU8%2FlOyi%2Bhn4U6PjY1uE%2F%2BGX514DWT7Q09u7eKRgLYq5RtpROYGlWHX0DMC8COcv1ONBxxZFO5l8Jq4Pv3lWEVLDL7Wc125ulnlwX8RvkhMYu1e4Kw%2BCp2%2BTxKSTa67GE00ZMw2k01udD%2FBIZwSoLBTscqbrhLAfinW9ji2c%2FnKep%2F56eLeoHwqIeNcK8lYyx4JbiKd%2BbRTXwRQJ7LvycUG5h1SYGk5fKuHNMtuzjrTYhjWv0GsCzj0CB9404fVpa1APwXwiasECgwgfqWvQY6pgFVdCZnBDn3rvdTdMH5ZvzBE2pfwhKEsukwRWMGqKvJyM%2FWDR75JFbwPR6rscupJXfT97JAk5OOTbv39SWvUTWML7uVlZZ3eFQD1ECmH61ol7MbXEffRU0TZnI1mphxJ053Jy2JGN31oMIpDqCgzFk8qHxNpd%2BqaQggd1dugsNpfw2kFrwo41w6uKBme%2BuPsuP5TWmOeeZ%2FkT1DkZ%2FAEwiRqxF2lDbc&X-Amz-Signature=3b374116b7ba43ed5eda54bac1f3625d2ba0b67a8d805af1a1624486ca912621&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O6HS37O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIEyd2nsmyGYSj4q7QrZZET7efKnqY4zzYpxtHO0FX2rJAiB2Y4KGOo9rY8OVhR0OZQpSr0yq4yDFiJv%2BUbZ3UbVbBSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMXR%2FSPLSsT9LQIkI1KtwD4U3hzzsajDw7XZK%2FFA9EGk8m4lfDKMSLJkk%2FEnJKR0Mm%2Fe8jMR%2FuVkPYrm0vxR6394w5nHXJpjX%2B6HkXmgY4i5IKrK8ZthCY1OwgPowV9oDPzPMANXDTEG5Rif0M2OJspi1WZArt0IJ%2BuGIYtQTROehjUuyCTPoFY84AMTO2IhJ3X9EDQkM1sgkX3oVFC0xf4xp5kB%2F5DEKQS0GVjL4ucaJs3KPtQTQrcGQ%2Ff8fkSvrYYi3sOr10LMb5KWTMtQr8M4smMnXISCzA%2BYcLk2mS3aXI7DstUPTfT4fUjFWttHVjoSgdcUB866v%2BJbCXUgoJu04jCyTNWuCvAyB1V9OG4E0b2PonbiLkC23jnOE%2FjJQ750BU8%2FlOyi%2Bhn4U6PjY1uE%2F%2BGX514DWT7Q09u7eKRgLYq5RtpROYGlWHX0DMC8COcv1ONBxxZFO5l8Jq4Pv3lWEVLDL7Wc125ulnlwX8RvkhMYu1e4Kw%2BCp2%2BTxKSTa67GE00ZMw2k01udD%2FBIZwSoLBTscqbrhLAfinW9ji2c%2FnKep%2F56eLeoHwqIeNcK8lYyx4JbiKd%2BbRTXwRQJ7LvycUG5h1SYGk5fKuHNMtuzjrTYhjWv0GsCzj0CB9404fVpa1APwXwiasECgwgfqWvQY6pgFVdCZnBDn3rvdTdMH5ZvzBE2pfwhKEsukwRWMGqKvJyM%2FWDR75JFbwPR6rscupJXfT97JAk5OOTbv39SWvUTWML7uVlZZ3eFQD1ECmH61ol7MbXEffRU0TZnI1mphxJ053Jy2JGN31oMIpDqCgzFk8qHxNpd%2BqaQggd1dugsNpfw2kFrwo41w6uKBme%2BuPsuP5TWmOeeZ%2FkT1DkZ%2FAEwiRqxF2lDbc&X-Amz-Signature=68eebf7bed2e2b21debe5d5012ddb89720fc50a8ec7ebc70b792136dfdbb92f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O6HS37O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIEyd2nsmyGYSj4q7QrZZET7efKnqY4zzYpxtHO0FX2rJAiB2Y4KGOo9rY8OVhR0OZQpSr0yq4yDFiJv%2BUbZ3UbVbBSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMXR%2FSPLSsT9LQIkI1KtwD4U3hzzsajDw7XZK%2FFA9EGk8m4lfDKMSLJkk%2FEnJKR0Mm%2Fe8jMR%2FuVkPYrm0vxR6394w5nHXJpjX%2B6HkXmgY4i5IKrK8ZthCY1OwgPowV9oDPzPMANXDTEG5Rif0M2OJspi1WZArt0IJ%2BuGIYtQTROehjUuyCTPoFY84AMTO2IhJ3X9EDQkM1sgkX3oVFC0xf4xp5kB%2F5DEKQS0GVjL4ucaJs3KPtQTQrcGQ%2Ff8fkSvrYYi3sOr10LMb5KWTMtQr8M4smMnXISCzA%2BYcLk2mS3aXI7DstUPTfT4fUjFWttHVjoSgdcUB866v%2BJbCXUgoJu04jCyTNWuCvAyB1V9OG4E0b2PonbiLkC23jnOE%2FjJQ750BU8%2FlOyi%2Bhn4U6PjY1uE%2F%2BGX514DWT7Q09u7eKRgLYq5RtpROYGlWHX0DMC8COcv1ONBxxZFO5l8Jq4Pv3lWEVLDL7Wc125ulnlwX8RvkhMYu1e4Kw%2BCp2%2BTxKSTa67GE00ZMw2k01udD%2FBIZwSoLBTscqbrhLAfinW9ji2c%2FnKep%2F56eLeoHwqIeNcK8lYyx4JbiKd%2BbRTXwRQJ7LvycUG5h1SYGk5fKuHNMtuzjrTYhjWv0GsCzj0CB9404fVpa1APwXwiasECgwgfqWvQY6pgFVdCZnBDn3rvdTdMH5ZvzBE2pfwhKEsukwRWMGqKvJyM%2FWDR75JFbwPR6rscupJXfT97JAk5OOTbv39SWvUTWML7uVlZZ3eFQD1ECmH61ol7MbXEffRU0TZnI1mphxJ053Jy2JGN31oMIpDqCgzFk8qHxNpd%2BqaQggd1dugsNpfw2kFrwo41w6uKBme%2BuPsuP5TWmOeeZ%2FkT1DkZ%2FAEwiRqxF2lDbc&X-Amz-Signature=9b6d3d5be2fbf785847302f27a79dffb626105b4c210eddaa99eecc951688bf4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT732MZD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIEhMxgLFh1fhf2My78XJO7WYqnJeZAB6UUJ0XSmkHncpAiEA7Lpg5IL5RLGh0G6sOLlw5Ree53K2JJ0GCaqOvnOrkSQq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDCJ4YaP%2FEMpFPK7nYSrcA0xsR3mwxH6kBbN9XiuHC9HxPM1jP%2FE6bV1Z%2Bj1TMkdvoJqCg5LnG1qAOg3zCuiv4tzrmTLqhqHNclAuprITFf93cp0z6os0ygew2%2FhrlIjc8mt7tqYgec4v%2BbiIRogRnnUN7HibPG6JupwVbdKVjyCdpOJW943zsw8dgsGG8wbER33uSA%2Fj7PnarJ1vsyTyK5kRZuNGDqxzkpt1eyKr1WU5bLnZWZlPeU0y83kTCo%2BYLSShkmNF1xMd%2FU6VX%2BGnJN4Qjs%2FL8jq3H07j0mXDQH9qCIpKfxeelCU24OnMmUAOWLaja5XlnDyDrtMvzwRJlOQuw1r5xlZas%2FbAgmMA71cDakMnjtYA5qLz2PfGyfOlSW37iGBdBVqOtP90%2BDN0bOygFWjFKnFVRwjgNZGQOHcJEUQLg9HtV4qexFLShcFGZH43L%2FHN3SKGBuY5CYhVguiu%2BsVNiEqSdn2bnUxZYRpQzICtS4KSc9woArT2uRAl01CeDpCpwx4%2BspZ6HtPscaEWzuzAsl9O%2BvduuSLzwSQEwu7zt5RNX4CM173cqv0TTjuwCy2EW%2BzrRRP821%2BfvIMnNPGsF9ZbYTHWI8qtHg3p7xFRGd%2Bqf%2FMIAD83MHbBjFwWAglJl5k3E4bkMPj5lr0GOqUBvs34BQ4U8uBWl4OI0HSD6QC0YeffRA5AB%2FVSvUuT0TN%2BSzyHUVwdfxRlFwOP34Us2JSkPS3GCdlEWJnuC8PO1WV5Z7w002yduzSEhtuaYDBTQ7jVeeREEoToQUgmm7iBNzjeF40ge%2FgKoB7Q0SlosCHtQT%2BoMxl2zHbOMqfSFk7QWuLt0eM0BRq8Po28pIJFwszPZcsR6fied9y1pKHBG7FFU%2B%2BV&X-Amz-Signature=599231ac4b97f7b6263ea0ef4d09de953007687d3ec6f1ac795ae0c8e8d11460&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTQZYQ6J%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCtx7hDPte99GqA1rdVjcBOwI2APb9zPzweWyl5ucfZ4wIhAOp%2F48cmrvvnhE3oZ60ATtGRQ3ZqhaucJEftzEi7pjr7Kv8DCHEQABoMNjM3NDIzMTgzODA1Igxet1o6TN%2B8hKLyanUq3ANELs9slqSdNPVMAyvnhz1tBpQSdtCBLLiA9JpIqHt4r5HkH33rkMxE3PMg7%2Bsj598TE6ow4Wt%2BBMRZYDHZMUxBGO%2FS0KAgSOmEXpWvJEMIw2gHhMVzh2jmscplpkc59TEymPax5%2FXz3cL9S1s8zwU7gLiox2GW7Z7FeGb4L9h7NatziAr%2FPgCFjvbuxruS%2FfmNhOU4So%2BD2mZAHYvJcvNz%2B%2FyjVIHPLihTo3jxjHSc5Vm1rU0lzzGK1WwdaQbA2K2v%2Bu1rckZLrUFBYvBiyDQwFgt3rvbZex166vjua%2Ba28w2xI%2FNmgH%2BshU85YZH%2BhJqPtIsd1rz4KwT91ohZN6I015xuL4FTBlGzMGTN3kKs5FFSogKSRezbegOhytf1kRPTkCqCwUSMCRMgwwdZdnfmAKoXZrrPoEf6LfB9L6YcmMdMcoIRABdlxtvQc2MtAjy0oIDTFtiRuYrqqj4cqxvtAuVdhp8XKfxtaoOh640Qb93iPAzk7Es6bMHsx19f%2B%2BwOMpPLjy0onhY0PDssql66c0AlhU52WpJ9tZ8RJO6pRblHQmBCwrvD%2FjRwQANugT05VbLJDUO7bo6pQe6LRJh1orY4yQJl1ZU%2FWGTjTRa71EK2H6s3rDN9rO4DxzD8%2BZa9BjqkAU8sbyrop4KbfKThrGCUti2uL21TGNtbuD%2F%2B7M0iAyh7MxHtcQd6taYgB8Dht8%2FfN5K2j09IiSvnjWbi%2FzYYYhNVOHiA0%2By6K71ahgrdaH%2F5RprK8SFNaem5DBAXnyhK3R4iIsWLnpduk6wXuYddwg83A3CoJCKjpIeafd%2B0TG7Y1wvKOSX%2F6%2Fbg7OO99K%2BMuIIxFbvT%2FPQzXdbm6bqZzcWb5jTf&X-Amz-Signature=3bf2bf1b0429b9be68818a8d8d9ec754bcd66a93aa49ab673fc769a1eb08b2bf&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQL2HJFI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCICBtu7YeL0Ly1aNa5kJesqIHxGN8hqZbzNCfBxR8x%2FbDAiANW%2BzKoba34UzNBM1f9OfLy2YhdU0u0s3nL%2Fal88viHCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMIrjvJwHDJ%2FgyqcAUKtwD%2FedDoJbMqxYMZtqtaTAgkE8%2B0N0QlgviAky9P7Ewd9Q15kEpmkAiYSbJbKUhsLNCm%2Be8d79NZct777b0fdiYce2qk7fOnZxz0COWs3JpUjbl9jzTEYDcI89Qg8xELgeF9mWW%2BelQmzNXEObpOGRC8S1aId3YDCfd4wyhKeyllO7yvB817mSalm3GRvwdi3JspFetzEQoXKfW2EKWl0FJYhwbXrcat%2BEE3uZrGiniN%2BLyys%2FDNRQudR4DRl%2FJvuung1wf8dPW4i8WR8ZvOT6V5S3NvkwiitQ2hEhEfsMyk0BUv1mjQxPDgBrQ6RT4jGULPnMcnm0bZB0Xy3hFem3juxC%2F2luF16FKE%2FK0p%2FT7oR0Q7IjV4p8HOIt6uvqfOvyv%2BYtg2A%2B7jLvjBLc0bcLZ2%2BJcivS4IiFTAn%2Bq%2FofVmeB4%2F2VWZHejEKb8u1i2ks6LfMPpEQQoM2Ncy9rQtbxlq9%2BfoSI7hBWjvco9L4z4r5YKeZTmmkAZhSZ5jRSJJjmB522K3XaspHOkOFn6%2F8eRy0lcN0kmf5h%2FgKPTD6pqPmNAezLVtG%2FEmjs5B3Ddr7yyL%2BOrgnM6rtvn8eqZz1yl32jIw1IZOK1LkEdAj9yEHS%2Fik3hvhz%2FMRgHHTOswwPmWvQY6pgHVR9zuKVePtjX1OqXcnlarDUSXE8QFMlfLYJXqsZQ8X%2B0RA3KmrAFzAeyTZeZrb6IY8m3kdA4WAmYSzJo7GjYF6crduUkdnw1JCCC4xJE%2Fw4Vg2UsKHC7vPkK3JqLa%2FJwPNHHQg1QajmE14vz7UIUMQ55HaZmT6LKle%2B8Yx6uZGNBNXTl3uPw0J15y5MEZfP2CTqnUnxCWtyCi9IAzP8aE0qbtbTN7&X-Amz-Signature=d8d59e5572cce5089b0589a953cb963d699a8dba8f2c7defe8e434bb633f4a01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VEJTSCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDfJeGuYfq%2BHOCM7HKlbophIQOej0k5sC%2BvX2txgZVyygIgM3YZZBqHXcATscDmIUd9sXsjQ7L0YipZEOxrHrSaJ9Uq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDF%2FNAeK51%2BLquBB8oyrcA0ezRuPxNtr7WyiU6x%2B3SJpPGTeyY2mkEOsVpYeAjSqAZiVTFUk%2FdJ4yF2AKW3VP3EsTpA%2B%2B7m7lRrJE02aFb9XF6CSzAXyhXdnYGCJYa5u4DwbiYwCYtflPGhKAeIIdnKWxMOu0OzeHRAYPWnUJHT2T6RW7Bsvv8lbCIAPN2rR%2BSh4JDgB6YzT1lIf0G8Q%2FlzANB4%2FRdJiBBaAfWUiwQhmaRBh83moWwh7Xf1dET%2BxNFry9a3EE79pT3kDO0h5QL6x%2FJMzXeL1QhEox58oYp12EHf5uugx%2FVmUPKM7a7RTUOzzXPIFIYn7Rw37vtUGwZT%2BEK3hlxO7kIR4zryWML6upO%2FDJMoNTxIF7SIWuiTtkObaxCK2U%2FqN1e4cNB%2F%2FQLu6StsmetqvKPgZL3j2X79qIzHxdoYnlxIp4jWLb76Qq%2FttltIRGTF4zYBMRR8nXLMYbAWHN4B7xcQ03c%2FrI7xOgSDUd6d3gXFSHkPFAa%2B0d8jA3JdR3wSE6RMfxxPCeWLyacZCb%2BnFo3wIbD8lzEV%2Bzx%2BSS8B55eaxVbecSaLMkrPCGEJ5PAGU56Ia2hWwZ1iXANfqKNkOFme8J7AEOdaALnSXg%2FJL8%2BsjHg0mvyj%2BPMySaHMgQoXztcTekMNj5lr0GOqUBbFyqjmLJ7iaBLqxFhm8ocxC9f4tTCM%2FlZtdazXtzXf6IzLVILgO3X0lwxjyDzsVyVTyX7FU3fpvcAjcZbrzp4cyUDVJapLzUqFmunfOa991uH9%2Fuj9OUdy1io0KCEsKE5FgcLdIdcjhb9Z5K2VIRaewC4toq6VLj2c0kDEsgZHMpZl%2B%2FRnFen7uxwnairV2RQhbJwuVML65IHDQ7bE%2FvQg10ODLw&X-Amz-Signature=ee440c8fe2636ba484a6a9fd7daa818e7b197edcf4514c9e07992fec5e02fbf6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VEJTSCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDfJeGuYfq%2BHOCM7HKlbophIQOej0k5sC%2BvX2txgZVyygIgM3YZZBqHXcATscDmIUd9sXsjQ7L0YipZEOxrHrSaJ9Uq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDF%2FNAeK51%2BLquBB8oyrcA0ezRuPxNtr7WyiU6x%2B3SJpPGTeyY2mkEOsVpYeAjSqAZiVTFUk%2FdJ4yF2AKW3VP3EsTpA%2B%2B7m7lRrJE02aFb9XF6CSzAXyhXdnYGCJYa5u4DwbiYwCYtflPGhKAeIIdnKWxMOu0OzeHRAYPWnUJHT2T6RW7Bsvv8lbCIAPN2rR%2BSh4JDgB6YzT1lIf0G8Q%2FlzANB4%2FRdJiBBaAfWUiwQhmaRBh83moWwh7Xf1dET%2BxNFry9a3EE79pT3kDO0h5QL6x%2FJMzXeL1QhEox58oYp12EHf5uugx%2FVmUPKM7a7RTUOzzXPIFIYn7Rw37vtUGwZT%2BEK3hlxO7kIR4zryWML6upO%2FDJMoNTxIF7SIWuiTtkObaxCK2U%2FqN1e4cNB%2F%2FQLu6StsmetqvKPgZL3j2X79qIzHxdoYnlxIp4jWLb76Qq%2FttltIRGTF4zYBMRR8nXLMYbAWHN4B7xcQ03c%2FrI7xOgSDUd6d3gXFSHkPFAa%2B0d8jA3JdR3wSE6RMfxxPCeWLyacZCb%2BnFo3wIbD8lzEV%2Bzx%2BSS8B55eaxVbecSaLMkrPCGEJ5PAGU56Ia2hWwZ1iXANfqKNkOFme8J7AEOdaALnSXg%2FJL8%2BsjHg0mvyj%2BPMySaHMgQoXztcTekMNj5lr0GOqUBbFyqjmLJ7iaBLqxFhm8ocxC9f4tTCM%2FlZtdazXtzXf6IzLVILgO3X0lwxjyDzsVyVTyX7FU3fpvcAjcZbrzp4cyUDVJapLzUqFmunfOa991uH9%2Fuj9OUdy1io0KCEsKE5FgcLdIdcjhb9Z5K2VIRaewC4toq6VLj2c0kDEsgZHMpZl%2B%2FRnFen7uxwnairV2RQhbJwuVML65IHDQ7bE%2FvQg10ODLw&X-Amz-Signature=8940ea90c213b420d946d1799233a484e83948684e02f162ec93080cfb590332&X-Amz-SignedHeaders=host&x-id=GetObject)

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
