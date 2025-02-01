

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EMS6ZPV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGtGTbyQH017DfO%2BhHPkIGokR5rVzjMpvCnA9fw8Z5vlAiAzyVkFXBfqP0j6GacZ8dypA41C%2BXjhOGUSyVMSIWPE3SqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6sfRKyL%2Fe7E2Ia6mKtwDSlotOOVYb6SHhJ7l59xIn6MhP0FgVvz98YUSkSHgB%2BlmwEBUUXdTvBRUkGUh%2FN1TG1UbK3hy792mAZCwuCcRaGjLYnn9CSu8%2BNqcHwx8Rtw1535fFJLfnRe7IgNRJnnbymDbMWXiXJc4imU75JdW%2BNWeoA4ciR5dN1pgSN7%2F1uU03lIoHv1MUUegBKUHBJVwBm1Uqh6S6eLlX%2F8ZjdmTIPruDcKXEZcC2qC0QxwrShxvXyN15k%2FCI0NFZPTbL%2B3UpJJNtcRjY%2FoJTEf%2FAqbgZjq5FO%2Fi1W8iaXcH19E%2FaEDmse90uk%2FpEv2sIgYLQFV8EyY6AS6eQYEdqNf%2B9mNv5gnpMnUnI16BS8BIT8qo7nHRgKPhS2PrNBbOCJF5KzMtNPzvz0FFEGlC0vyeHM3CWRahgnoq4xJgBvHoVg0m8gzQrOdIXXPUe%2FZNWqKyw6IgOGEcSbRlT%2BoetRMUDh8XZWZJBHoaBgo7BkB2eNdWG8cs9lRXJpytUhUCDdfi%2FOgm9Kz6VLs8Gz29ZgMJiIRRDErkVgrwI3FucPcAG5HVPCIax2D98JjELQk9MTsl3CyDcJF7JnzIoIr1mc8Fq4RYBQSK4h%2FeqMKO36M0j7LuW0%2B%2BMYtxtH0Wi4RGGn0w96T3vAY6pgGARg3WhukFZIDcKmdiC1r5p2tPrpLa7Cac75QiD5296pElQrcaMfmmGdvpDjPFH17AQ5hQz7IQiVA21fAnxQsmbHWSsjRqWcTU1RB70rRloFZuv0unha53P00%2F0uw5Q%2F79JzRlmkpHhtknbZbcaBUUF7X%2FleNXCQbUBZiI1wvy8ajV8VHHfvL6glzijeqSIK9%2BzhyyrBEzrz%2FHA1M253JulqnPAdzE&X-Amz-Signature=57d01c6ecdee2c13cfd5166662335394f5976c456963796551f34c1113433d52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EMS6ZPV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGtGTbyQH017DfO%2BhHPkIGokR5rVzjMpvCnA9fw8Z5vlAiAzyVkFXBfqP0j6GacZ8dypA41C%2BXjhOGUSyVMSIWPE3SqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6sfRKyL%2Fe7E2Ia6mKtwDSlotOOVYb6SHhJ7l59xIn6MhP0FgVvz98YUSkSHgB%2BlmwEBUUXdTvBRUkGUh%2FN1TG1UbK3hy792mAZCwuCcRaGjLYnn9CSu8%2BNqcHwx8Rtw1535fFJLfnRe7IgNRJnnbymDbMWXiXJc4imU75JdW%2BNWeoA4ciR5dN1pgSN7%2F1uU03lIoHv1MUUegBKUHBJVwBm1Uqh6S6eLlX%2F8ZjdmTIPruDcKXEZcC2qC0QxwrShxvXyN15k%2FCI0NFZPTbL%2B3UpJJNtcRjY%2FoJTEf%2FAqbgZjq5FO%2Fi1W8iaXcH19E%2FaEDmse90uk%2FpEv2sIgYLQFV8EyY6AS6eQYEdqNf%2B9mNv5gnpMnUnI16BS8BIT8qo7nHRgKPhS2PrNBbOCJF5KzMtNPzvz0FFEGlC0vyeHM3CWRahgnoq4xJgBvHoVg0m8gzQrOdIXXPUe%2FZNWqKyw6IgOGEcSbRlT%2BoetRMUDh8XZWZJBHoaBgo7BkB2eNdWG8cs9lRXJpytUhUCDdfi%2FOgm9Kz6VLs8Gz29ZgMJiIRRDErkVgrwI3FucPcAG5HVPCIax2D98JjELQk9MTsl3CyDcJF7JnzIoIr1mc8Fq4RYBQSK4h%2FeqMKO36M0j7LuW0%2B%2BMYtxtH0Wi4RGGn0w96T3vAY6pgGARg3WhukFZIDcKmdiC1r5p2tPrpLa7Cac75QiD5296pElQrcaMfmmGdvpDjPFH17AQ5hQz7IQiVA21fAnxQsmbHWSsjRqWcTU1RB70rRloFZuv0unha53P00%2F0uw5Q%2F79JzRlmkpHhtknbZbcaBUUF7X%2FleNXCQbUBZiI1wvy8ajV8VHHfvL6glzijeqSIK9%2BzhyyrBEzrz%2FHA1M253JulqnPAdzE&X-Amz-Signature=4c489c2c79c0635c3790ab358f5898f4c13733232ffb84c611ee2cafdcfe82b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EMS6ZPV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGtGTbyQH017DfO%2BhHPkIGokR5rVzjMpvCnA9fw8Z5vlAiAzyVkFXBfqP0j6GacZ8dypA41C%2BXjhOGUSyVMSIWPE3SqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6sfRKyL%2Fe7E2Ia6mKtwDSlotOOVYb6SHhJ7l59xIn6MhP0FgVvz98YUSkSHgB%2BlmwEBUUXdTvBRUkGUh%2FN1TG1UbK3hy792mAZCwuCcRaGjLYnn9CSu8%2BNqcHwx8Rtw1535fFJLfnRe7IgNRJnnbymDbMWXiXJc4imU75JdW%2BNWeoA4ciR5dN1pgSN7%2F1uU03lIoHv1MUUegBKUHBJVwBm1Uqh6S6eLlX%2F8ZjdmTIPruDcKXEZcC2qC0QxwrShxvXyN15k%2FCI0NFZPTbL%2B3UpJJNtcRjY%2FoJTEf%2FAqbgZjq5FO%2Fi1W8iaXcH19E%2FaEDmse90uk%2FpEv2sIgYLQFV8EyY6AS6eQYEdqNf%2B9mNv5gnpMnUnI16BS8BIT8qo7nHRgKPhS2PrNBbOCJF5KzMtNPzvz0FFEGlC0vyeHM3CWRahgnoq4xJgBvHoVg0m8gzQrOdIXXPUe%2FZNWqKyw6IgOGEcSbRlT%2BoetRMUDh8XZWZJBHoaBgo7BkB2eNdWG8cs9lRXJpytUhUCDdfi%2FOgm9Kz6VLs8Gz29ZgMJiIRRDErkVgrwI3FucPcAG5HVPCIax2D98JjELQk9MTsl3CyDcJF7JnzIoIr1mc8Fq4RYBQSK4h%2FeqMKO36M0j7LuW0%2B%2BMYtxtH0Wi4RGGn0w96T3vAY6pgGARg3WhukFZIDcKmdiC1r5p2tPrpLa7Cac75QiD5296pElQrcaMfmmGdvpDjPFH17AQ5hQz7IQiVA21fAnxQsmbHWSsjRqWcTU1RB70rRloFZuv0unha53P00%2F0uw5Q%2F79JzRlmkpHhtknbZbcaBUUF7X%2FleNXCQbUBZiI1wvy8ajV8VHHfvL6glzijeqSIK9%2BzhyyrBEzrz%2FHA1M253JulqnPAdzE&X-Amz-Signature=7a75c340699935c6246ac3622789b100b6162568284edfae2b197cca6e429ce1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNFJQNFZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWMotpXSQfCTck%2Bk1fj1G0Nig%2Fby0MLxYyyzvdhE1k7QIhAKIEgwOLF2hpTj9SSZWs%2FzEoAKNb4wmq%2FEBP4E7ZqA1RKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHs4BrhHJ13wyYQBUq3AOp%2FtivYZCL4KGTPk%2F2eo22bJw0l4eOwwhl8BC3Sd2GmbvyAg7Tdjlm5sVV6UxmQdCPr8lv12eVY%2Fwk%2BX68N084JDlBcazzQ9z2s5SKtFIgGU5vV9xU9sgCOzSHmLV3Zg6JIelSMvvQOidvNhhs2PE0BTwPwyo4t2FuJZPYy%2BeRZEJPecuZ9%2BtluyZwKcnbDGz2hUmU0H98G3NsZBJSwWzK67%2FIifZrDNs3OXKnPEwZ4mui5mJGps86w1DGBK7vvxZkKDMCxiWWbZFpZkko2%2BtzKt7vIYop5dVsjur2M7Gl9WTTNhrALmxlvRf3kf0SmLmaGMOIwPXxhj7FGILQFQkCN9PLAvGV03fgSo0CTrsc6buk%2FUM3wJyo1KFNIj9PM02yQjro8AXOf9ogV%2F0BHl5vFoRazchQ1HhNeHbfRzujExw7OR9qzBG9CoKwYqcpKDozvoxPXZHqjABdC3jqhu40dcpkr3JQ9rYgQkGXot4rXM88sdAIcvEDIK7FBEEBDZSBvz%2FLv7PdiXp4tahjUuK0egAT8BEEgc%2FSvvTdkukhgz80Ghq6pffUp%2FVbXf%2FLTcxUE6ix8QOjltLYM7J7zIZfvJF2VWSA602zF19Jh4QpQurvsPu8Wle2kfdqKDCOzPe8BjqkAa45PSZOf0Z%2B0wqY3onxg3%2FSKru1tPAdnK52fnLyKOUfxfCyzfmcD4%2FnFK5m2KrIZl0wfYlPMmli5RN1G8xL9qhr3RZzi8kjRLFP0Lt%2FZ7kBx%2Fg6XtFTmcTXBZ5%2BNTwljmwkmBu1sULGkxvGweDXAeTRKv2EoPWM%2BblYJ7Q%2B57OVO6kKv470lpG1pEedEnqxRMFVgxU6fTyXlKieYvTXlQZPFk6R&X-Amz-Signature=bd5367cc053a12248f5f7738d0e35e388a8603fe10090f0bc9f76ef0a4e5cb1d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNFJQNFZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWMotpXSQfCTck%2Bk1fj1G0Nig%2Fby0MLxYyyzvdhE1k7QIhAKIEgwOLF2hpTj9SSZWs%2FzEoAKNb4wmq%2FEBP4E7ZqA1RKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHs4BrhHJ13wyYQBUq3AOp%2FtivYZCL4KGTPk%2F2eo22bJw0l4eOwwhl8BC3Sd2GmbvyAg7Tdjlm5sVV6UxmQdCPr8lv12eVY%2Fwk%2BX68N084JDlBcazzQ9z2s5SKtFIgGU5vV9xU9sgCOzSHmLV3Zg6JIelSMvvQOidvNhhs2PE0BTwPwyo4t2FuJZPYy%2BeRZEJPecuZ9%2BtluyZwKcnbDGz2hUmU0H98G3NsZBJSwWzK67%2FIifZrDNs3OXKnPEwZ4mui5mJGps86w1DGBK7vvxZkKDMCxiWWbZFpZkko2%2BtzKt7vIYop5dVsjur2M7Gl9WTTNhrALmxlvRf3kf0SmLmaGMOIwPXxhj7FGILQFQkCN9PLAvGV03fgSo0CTrsc6buk%2FUM3wJyo1KFNIj9PM02yQjro8AXOf9ogV%2F0BHl5vFoRazchQ1HhNeHbfRzujExw7OR9qzBG9CoKwYqcpKDozvoxPXZHqjABdC3jqhu40dcpkr3JQ9rYgQkGXot4rXM88sdAIcvEDIK7FBEEBDZSBvz%2FLv7PdiXp4tahjUuK0egAT8BEEgc%2FSvvTdkukhgz80Ghq6pffUp%2FVbXf%2FLTcxUE6ix8QOjltLYM7J7zIZfvJF2VWSA602zF19Jh4QpQurvsPu8Wle2kfdqKDCOzPe8BjqkAa45PSZOf0Z%2B0wqY3onxg3%2FSKru1tPAdnK52fnLyKOUfxfCyzfmcD4%2FnFK5m2KrIZl0wfYlPMmli5RN1G8xL9qhr3RZzi8kjRLFP0Lt%2FZ7kBx%2Fg6XtFTmcTXBZ5%2BNTwljmwkmBu1sULGkxvGweDXAeTRKv2EoPWM%2BblYJ7Q%2B57OVO6kKv470lpG1pEedEnqxRMFVgxU6fTyXlKieYvTXlQZPFk6R&X-Amz-Signature=3b6f1cf4dc043703717a827d11c96f20a98a14e84683422862c5109690fd2efe&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNFJQNFZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWMotpXSQfCTck%2Bk1fj1G0Nig%2Fby0MLxYyyzvdhE1k7QIhAKIEgwOLF2hpTj9SSZWs%2FzEoAKNb4wmq%2FEBP4E7ZqA1RKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHs4BrhHJ13wyYQBUq3AOp%2FtivYZCL4KGTPk%2F2eo22bJw0l4eOwwhl8BC3Sd2GmbvyAg7Tdjlm5sVV6UxmQdCPr8lv12eVY%2Fwk%2BX68N084JDlBcazzQ9z2s5SKtFIgGU5vV9xU9sgCOzSHmLV3Zg6JIelSMvvQOidvNhhs2PE0BTwPwyo4t2FuJZPYy%2BeRZEJPecuZ9%2BtluyZwKcnbDGz2hUmU0H98G3NsZBJSwWzK67%2FIifZrDNs3OXKnPEwZ4mui5mJGps86w1DGBK7vvxZkKDMCxiWWbZFpZkko2%2BtzKt7vIYop5dVsjur2M7Gl9WTTNhrALmxlvRf3kf0SmLmaGMOIwPXxhj7FGILQFQkCN9PLAvGV03fgSo0CTrsc6buk%2FUM3wJyo1KFNIj9PM02yQjro8AXOf9ogV%2F0BHl5vFoRazchQ1HhNeHbfRzujExw7OR9qzBG9CoKwYqcpKDozvoxPXZHqjABdC3jqhu40dcpkr3JQ9rYgQkGXot4rXM88sdAIcvEDIK7FBEEBDZSBvz%2FLv7PdiXp4tahjUuK0egAT8BEEgc%2FSvvTdkukhgz80Ghq6pffUp%2FVbXf%2FLTcxUE6ix8QOjltLYM7J7zIZfvJF2VWSA602zF19Jh4QpQurvsPu8Wle2kfdqKDCOzPe8BjqkAa45PSZOf0Z%2B0wqY3onxg3%2FSKru1tPAdnK52fnLyKOUfxfCyzfmcD4%2FnFK5m2KrIZl0wfYlPMmli5RN1G8xL9qhr3RZzi8kjRLFP0Lt%2FZ7kBx%2Fg6XtFTmcTXBZ5%2BNTwljmwkmBu1sULGkxvGweDXAeTRKv2EoPWM%2BblYJ7Q%2B57OVO6kKv470lpG1pEedEnqxRMFVgxU6fTyXlKieYvTXlQZPFk6R&X-Amz-Signature=df4372afb8f70a917ee8f82517a5dd5d6fe9d9f172876e070fecc2190624a624&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNFJQNFZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWMotpXSQfCTck%2Bk1fj1G0Nig%2Fby0MLxYyyzvdhE1k7QIhAKIEgwOLF2hpTj9SSZWs%2FzEoAKNb4wmq%2FEBP4E7ZqA1RKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHs4BrhHJ13wyYQBUq3AOp%2FtivYZCL4KGTPk%2F2eo22bJw0l4eOwwhl8BC3Sd2GmbvyAg7Tdjlm5sVV6UxmQdCPr8lv12eVY%2Fwk%2BX68N084JDlBcazzQ9z2s5SKtFIgGU5vV9xU9sgCOzSHmLV3Zg6JIelSMvvQOidvNhhs2PE0BTwPwyo4t2FuJZPYy%2BeRZEJPecuZ9%2BtluyZwKcnbDGz2hUmU0H98G3NsZBJSwWzK67%2FIifZrDNs3OXKnPEwZ4mui5mJGps86w1DGBK7vvxZkKDMCxiWWbZFpZkko2%2BtzKt7vIYop5dVsjur2M7Gl9WTTNhrALmxlvRf3kf0SmLmaGMOIwPXxhj7FGILQFQkCN9PLAvGV03fgSo0CTrsc6buk%2FUM3wJyo1KFNIj9PM02yQjro8AXOf9ogV%2F0BHl5vFoRazchQ1HhNeHbfRzujExw7OR9qzBG9CoKwYqcpKDozvoxPXZHqjABdC3jqhu40dcpkr3JQ9rYgQkGXot4rXM88sdAIcvEDIK7FBEEBDZSBvz%2FLv7PdiXp4tahjUuK0egAT8BEEgc%2FSvvTdkukhgz80Ghq6pffUp%2FVbXf%2FLTcxUE6ix8QOjltLYM7J7zIZfvJF2VWSA602zF19Jh4QpQurvsPu8Wle2kfdqKDCOzPe8BjqkAa45PSZOf0Z%2B0wqY3onxg3%2FSKru1tPAdnK52fnLyKOUfxfCyzfmcD4%2FnFK5m2KrIZl0wfYlPMmli5RN1G8xL9qhr3RZzi8kjRLFP0Lt%2FZ7kBx%2Fg6XtFTmcTXBZ5%2BNTwljmwkmBu1sULGkxvGweDXAeTRKv2EoPWM%2BblYJ7Q%2B57OVO6kKv470lpG1pEedEnqxRMFVgxU6fTyXlKieYvTXlQZPFk6R&X-Amz-Signature=725a348e6ca929aed1874f5d80360da947d0b170cf7eaadf16e1a2688bb2e796&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNFJQNFZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWMotpXSQfCTck%2Bk1fj1G0Nig%2Fby0MLxYyyzvdhE1k7QIhAKIEgwOLF2hpTj9SSZWs%2FzEoAKNb4wmq%2FEBP4E7ZqA1RKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHs4BrhHJ13wyYQBUq3AOp%2FtivYZCL4KGTPk%2F2eo22bJw0l4eOwwhl8BC3Sd2GmbvyAg7Tdjlm5sVV6UxmQdCPr8lv12eVY%2Fwk%2BX68N084JDlBcazzQ9z2s5SKtFIgGU5vV9xU9sgCOzSHmLV3Zg6JIelSMvvQOidvNhhs2PE0BTwPwyo4t2FuJZPYy%2BeRZEJPecuZ9%2BtluyZwKcnbDGz2hUmU0H98G3NsZBJSwWzK67%2FIifZrDNs3OXKnPEwZ4mui5mJGps86w1DGBK7vvxZkKDMCxiWWbZFpZkko2%2BtzKt7vIYop5dVsjur2M7Gl9WTTNhrALmxlvRf3kf0SmLmaGMOIwPXxhj7FGILQFQkCN9PLAvGV03fgSo0CTrsc6buk%2FUM3wJyo1KFNIj9PM02yQjro8AXOf9ogV%2F0BHl5vFoRazchQ1HhNeHbfRzujExw7OR9qzBG9CoKwYqcpKDozvoxPXZHqjABdC3jqhu40dcpkr3JQ9rYgQkGXot4rXM88sdAIcvEDIK7FBEEBDZSBvz%2FLv7PdiXp4tahjUuK0egAT8BEEgc%2FSvvTdkukhgz80Ghq6pffUp%2FVbXf%2FLTcxUE6ix8QOjltLYM7J7zIZfvJF2VWSA602zF19Jh4QpQurvsPu8Wle2kfdqKDCOzPe8BjqkAa45PSZOf0Z%2B0wqY3onxg3%2FSKru1tPAdnK52fnLyKOUfxfCyzfmcD4%2FnFK5m2KrIZl0wfYlPMmli5RN1G8xL9qhr3RZzi8kjRLFP0Lt%2FZ7kBx%2Fg6XtFTmcTXBZ5%2BNTwljmwkmBu1sULGkxvGweDXAeTRKv2EoPWM%2BblYJ7Q%2B57OVO6kKv470lpG1pEedEnqxRMFVgxU6fTyXlKieYvTXlQZPFk6R&X-Amz-Signature=7f2bb438d5fa6a47cda54ccb0280463d1a1bc38666302c3f33b7239f11a11414&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNFJQNFZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWMotpXSQfCTck%2Bk1fj1G0Nig%2Fby0MLxYyyzvdhE1k7QIhAKIEgwOLF2hpTj9SSZWs%2FzEoAKNb4wmq%2FEBP4E7ZqA1RKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHs4BrhHJ13wyYQBUq3AOp%2FtivYZCL4KGTPk%2F2eo22bJw0l4eOwwhl8BC3Sd2GmbvyAg7Tdjlm5sVV6UxmQdCPr8lv12eVY%2Fwk%2BX68N084JDlBcazzQ9z2s5SKtFIgGU5vV9xU9sgCOzSHmLV3Zg6JIelSMvvQOidvNhhs2PE0BTwPwyo4t2FuJZPYy%2BeRZEJPecuZ9%2BtluyZwKcnbDGz2hUmU0H98G3NsZBJSwWzK67%2FIifZrDNs3OXKnPEwZ4mui5mJGps86w1DGBK7vvxZkKDMCxiWWbZFpZkko2%2BtzKt7vIYop5dVsjur2M7Gl9WTTNhrALmxlvRf3kf0SmLmaGMOIwPXxhj7FGILQFQkCN9PLAvGV03fgSo0CTrsc6buk%2FUM3wJyo1KFNIj9PM02yQjro8AXOf9ogV%2F0BHl5vFoRazchQ1HhNeHbfRzujExw7OR9qzBG9CoKwYqcpKDozvoxPXZHqjABdC3jqhu40dcpkr3JQ9rYgQkGXot4rXM88sdAIcvEDIK7FBEEBDZSBvz%2FLv7PdiXp4tahjUuK0egAT8BEEgc%2FSvvTdkukhgz80Ghq6pffUp%2FVbXf%2FLTcxUE6ix8QOjltLYM7J7zIZfvJF2VWSA602zF19Jh4QpQurvsPu8Wle2kfdqKDCOzPe8BjqkAa45PSZOf0Z%2B0wqY3onxg3%2FSKru1tPAdnK52fnLyKOUfxfCyzfmcD4%2FnFK5m2KrIZl0wfYlPMmli5RN1G8xL9qhr3RZzi8kjRLFP0Lt%2FZ7kBx%2Fg6XtFTmcTXBZ5%2BNTwljmwkmBu1sULGkxvGweDXAeTRKv2EoPWM%2BblYJ7Q%2B57OVO6kKv470lpG1pEedEnqxRMFVgxU6fTyXlKieYvTXlQZPFk6R&X-Amz-Signature=1f2c60986bcbf722f39dae3243663c0998a13a979e5044bd739eeaff7ab31705&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K66U6CX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA22yzpQn9jHJYjAW6%2Bo8k7lGAhFhLqe35jmCsRw6fEvAiEAh5LZz94y%2BsjTxl2lBHHKtkHXEfSOUhgiXund82APabAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1JeCbxJlRXrxwZUyrcA7dU4hdd7%2BmN%2FLlXM0dqXI8x1U0R1oAJJQaS6lhLFBSNl5RIoJPdP4Uy%2BmL6wSLAUUat8KmTIIADtc%2FRgHAVsbrsYycpD9mI6D%2F%2Fpy7B5WdIS6vjqMlM%2FqMoFbjiKStGcVQ85U%2BNSSN4TXwJ6Aj0%2FdJOSH%2BxvgIQ5ZHk0yh0%2BwT0uhtSUTwPy6yoSeFpK7yzWf%2BH1%2B44NKR7TCtJXNo%2BtH%2BcFZiod3rpBR1HmidGcvbmZVhZhFt6xUdi%2FzTi0x7SyX7pDEK%2BuLBx1y8DMbYUQdF5hj1vZtH8gJmyNQH1XgVpuQ9JUTItmMVGx93sDLT4Mfa2ECmYc%2FrB3BZsCtWblhzLozZOCDnPVdByo%2BNaJxPNQ9lRXw1n6i%2BhVjSGHUVJjuePqHMt33JKdVrYImfA%2FfSlFEUq5mTYCO7WR14NGv8jKWTy3RFtUml6MlSMWquawyEnLVBBJF2fadEvdIq51vyPXZCssRXodbNbrcuqJ9OwYjv5tQlqtDf0dGJPiSkZU304bvmbH1Lk7g%2FwJvEDWDY5Z5JG8f%2Bf%2FE0txH0wAMtR0hZwYbzK3Epx6wkZcFNlNZApq2TAS20cay9C8oGyNEootl%2BdqP3hPYv6voyWr9T2DGsL%2FUe%2Fpqyrao8pMKKk97wGOqUBBjKVktUweOJ3aiGBwZsxdOPtGzeFxhBXla5M9gduVFc3qd2YRDIhOgLQXPpydTrCXIG5IPX51CVLA8Vl5UdXygM%2BGw3ciptI617EAPhQ6GFiUe5IlWNQWOrGCwyIFNluoxSsqnCD%2FZKt3OmGGqMiWtlp6TA7L90Xo%2FYNIOALz6QamShLAIgtD6nac1Uiykp9LSG7MVkoE51sRugfHgeGnWKdn5Pj&X-Amz-Signature=53e26e33594527210714cc6fccde68fa93fd4468623e575fb4dbd535862fbc9e&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJQZLBA4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEMJ2ON8BmQSCD8NTx%2Fv%2BnjuZNn1CGwizn0XMgpX0dv5AiBLirifUB3sBHwiQHjruC8ENHH3k0IVkCRTr6M%2BTNwoqCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMk5uc4bTKgD%2FKuVhAKtwDQbFwlB12Obs6S9zkbRRw13BMquZA9eRH%2B9veU3Uc4Y%2BNbD4n74osWgCKsx%2FCRZHf%2BlgeDyHUtP%2BkhVHZ7SvBcjqxcZsQawKrZnITGgEC1DwZjJFt3OZq%2BrJQG7Qu6ltEAPMrUFIoO1aNM0K%2BIHIcJ3z3GMCdviWKT50Neq3L4G0NtXVWcjY3gSR71H0WuDzMzsLrr2tk1yVkZpHEPXJfF8TjK1cA08GW0zzg%2FxToCw0gOcum%2BFziKD1Lg3%2Fvwc5Tqvhyf09V6B%2BPIqDtykqaGDN83CNF4ksNmHlaixmH9TY8gDVoYsw%2BfY5QU2DAtCfMPiu34oi2v5C%2BY4DXNtknrGFcn5T4HKSYl80IYX06ek1Ao1MROWOv3XspPQLRFFiMNXbAlczj7LqJ1FQOOw79at2XiQUeapyMF3E9VGS5kMNxJu0%2B1rAH7SGloBbt3Yg45%2FYNw%2FsJoHxwg2WZ2gEKzep%2FGdXPFPzuqvIIvyF9urOdBgXuJP7ma%2BwfFwjELVaK0LyAiDI055OEnVo%2FJbseVpJxroGYTlvQZF%2BBhbGc5j70agOGDre%2Bjlg3WAwL8W6DI7Z849xZRHGkdNtxZF489D5OdEHO%2F3fqaZVjY7iqPdogGl6x5mqdh%2FaaB4Aw26T3vAY6pgGb5oUDYpYu8smjK5tjoNV%2BWwWNckzkzJ4R8jO%2FXNJ88CjxPDdOoWo9mvj4NWMY7pVXVlR2iuFxtpyEQ%2BuOn2s7yVa7az9r1WtQaj2LW8LczIBtySPKYjUmopKJoIBSfU57fpkT39ekiZOqigM3nugGOC1SusqSXSJmDXeUcnTBGk6ulUlBg%2Btq8cGmzs2LhGiryy1W3QcCrNhvjx76vneKzn1EqhI3&X-Amz-Signature=bebfd34bd0bf7e3c8336dfb288e2e7e6f731636bc04653328366a5c5c0b56f61&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNFJQNFZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWMotpXSQfCTck%2Bk1fj1G0Nig%2Fby0MLxYyyzvdhE1k7QIhAKIEgwOLF2hpTj9SSZWs%2FzEoAKNb4wmq%2FEBP4E7ZqA1RKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHs4BrhHJ13wyYQBUq3AOp%2FtivYZCL4KGTPk%2F2eo22bJw0l4eOwwhl8BC3Sd2GmbvyAg7Tdjlm5sVV6UxmQdCPr8lv12eVY%2Fwk%2BX68N084JDlBcazzQ9z2s5SKtFIgGU5vV9xU9sgCOzSHmLV3Zg6JIelSMvvQOidvNhhs2PE0BTwPwyo4t2FuJZPYy%2BeRZEJPecuZ9%2BtluyZwKcnbDGz2hUmU0H98G3NsZBJSwWzK67%2FIifZrDNs3OXKnPEwZ4mui5mJGps86w1DGBK7vvxZkKDMCxiWWbZFpZkko2%2BtzKt7vIYop5dVsjur2M7Gl9WTTNhrALmxlvRf3kf0SmLmaGMOIwPXxhj7FGILQFQkCN9PLAvGV03fgSo0CTrsc6buk%2FUM3wJyo1KFNIj9PM02yQjro8AXOf9ogV%2F0BHl5vFoRazchQ1HhNeHbfRzujExw7OR9qzBG9CoKwYqcpKDozvoxPXZHqjABdC3jqhu40dcpkr3JQ9rYgQkGXot4rXM88sdAIcvEDIK7FBEEBDZSBvz%2FLv7PdiXp4tahjUuK0egAT8BEEgc%2FSvvTdkukhgz80Ghq6pffUp%2FVbXf%2FLTcxUE6ix8QOjltLYM7J7zIZfvJF2VWSA602zF19Jh4QpQurvsPu8Wle2kfdqKDCOzPe8BjqkAa45PSZOf0Z%2B0wqY3onxg3%2FSKru1tPAdnK52fnLyKOUfxfCyzfmcD4%2FnFK5m2KrIZl0wfYlPMmli5RN1G8xL9qhr3RZzi8kjRLFP0Lt%2FZ7kBx%2Fg6XtFTmcTXBZ5%2BNTwljmwkmBu1sULGkxvGweDXAeTRKv2EoPWM%2BblYJ7Q%2B57OVO6kKv470lpG1pEedEnqxRMFVgxU6fTyXlKieYvTXlQZPFk6R&X-Amz-Signature=ba6e8c6de015f4abfdf92003f0dd7b19585cadcfbe39bd4d5f8b61910fcc7761&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNFJQNFZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWMotpXSQfCTck%2Bk1fj1G0Nig%2Fby0MLxYyyzvdhE1k7QIhAKIEgwOLF2hpTj9SSZWs%2FzEoAKNb4wmq%2FEBP4E7ZqA1RKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHs4BrhHJ13wyYQBUq3AOp%2FtivYZCL4KGTPk%2F2eo22bJw0l4eOwwhl8BC3Sd2GmbvyAg7Tdjlm5sVV6UxmQdCPr8lv12eVY%2Fwk%2BX68N084JDlBcazzQ9z2s5SKtFIgGU5vV9xU9sgCOzSHmLV3Zg6JIelSMvvQOidvNhhs2PE0BTwPwyo4t2FuJZPYy%2BeRZEJPecuZ9%2BtluyZwKcnbDGz2hUmU0H98G3NsZBJSwWzK67%2FIifZrDNs3OXKnPEwZ4mui5mJGps86w1DGBK7vvxZkKDMCxiWWbZFpZkko2%2BtzKt7vIYop5dVsjur2M7Gl9WTTNhrALmxlvRf3kf0SmLmaGMOIwPXxhj7FGILQFQkCN9PLAvGV03fgSo0CTrsc6buk%2FUM3wJyo1KFNIj9PM02yQjro8AXOf9ogV%2F0BHl5vFoRazchQ1HhNeHbfRzujExw7OR9qzBG9CoKwYqcpKDozvoxPXZHqjABdC3jqhu40dcpkr3JQ9rYgQkGXot4rXM88sdAIcvEDIK7FBEEBDZSBvz%2FLv7PdiXp4tahjUuK0egAT8BEEgc%2FSvvTdkukhgz80Ghq6pffUp%2FVbXf%2FLTcxUE6ix8QOjltLYM7J7zIZfvJF2VWSA602zF19Jh4QpQurvsPu8Wle2kfdqKDCOzPe8BjqkAa45PSZOf0Z%2B0wqY3onxg3%2FSKru1tPAdnK52fnLyKOUfxfCyzfmcD4%2FnFK5m2KrIZl0wfYlPMmli5RN1G8xL9qhr3RZzi8kjRLFP0Lt%2FZ7kBx%2Fg6XtFTmcTXBZ5%2BNTwljmwkmBu1sULGkxvGweDXAeTRKv2EoPWM%2BblYJ7Q%2B57OVO6kKv470lpG1pEedEnqxRMFVgxU6fTyXlKieYvTXlQZPFk6R&X-Amz-Signature=e7df0ade5b4d9a0a80770f011fa3775e5787c34cc5a9b62c31b79f60ce415873&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNFJQNFZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWMotpXSQfCTck%2Bk1fj1G0Nig%2Fby0MLxYyyzvdhE1k7QIhAKIEgwOLF2hpTj9SSZWs%2FzEoAKNb4wmq%2FEBP4E7ZqA1RKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHs4BrhHJ13wyYQBUq3AOp%2FtivYZCL4KGTPk%2F2eo22bJw0l4eOwwhl8BC3Sd2GmbvyAg7Tdjlm5sVV6UxmQdCPr8lv12eVY%2Fwk%2BX68N084JDlBcazzQ9z2s5SKtFIgGU5vV9xU9sgCOzSHmLV3Zg6JIelSMvvQOidvNhhs2PE0BTwPwyo4t2FuJZPYy%2BeRZEJPecuZ9%2BtluyZwKcnbDGz2hUmU0H98G3NsZBJSwWzK67%2FIifZrDNs3OXKnPEwZ4mui5mJGps86w1DGBK7vvxZkKDMCxiWWbZFpZkko2%2BtzKt7vIYop5dVsjur2M7Gl9WTTNhrALmxlvRf3kf0SmLmaGMOIwPXxhj7FGILQFQkCN9PLAvGV03fgSo0CTrsc6buk%2FUM3wJyo1KFNIj9PM02yQjro8AXOf9ogV%2F0BHl5vFoRazchQ1HhNeHbfRzujExw7OR9qzBG9CoKwYqcpKDozvoxPXZHqjABdC3jqhu40dcpkr3JQ9rYgQkGXot4rXM88sdAIcvEDIK7FBEEBDZSBvz%2FLv7PdiXp4tahjUuK0egAT8BEEgc%2FSvvTdkukhgz80Ghq6pffUp%2FVbXf%2FLTcxUE6ix8QOjltLYM7J7zIZfvJF2VWSA602zF19Jh4QpQurvsPu8Wle2kfdqKDCOzPe8BjqkAa45PSZOf0Z%2B0wqY3onxg3%2FSKru1tPAdnK52fnLyKOUfxfCyzfmcD4%2FnFK5m2KrIZl0wfYlPMmli5RN1G8xL9qhr3RZzi8kjRLFP0Lt%2FZ7kBx%2Fg6XtFTmcTXBZ5%2BNTwljmwkmBu1sULGkxvGweDXAeTRKv2EoPWM%2BblYJ7Q%2B57OVO6kKv470lpG1pEedEnqxRMFVgxU6fTyXlKieYvTXlQZPFk6R&X-Amz-Signature=343eb7ab02ed49e191b0c9e47690c52e9830099aa9d3e3e13e5cecebdbbb6321&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEGA3QRA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAk5u8Xl0uyctCRFCg2X6yp1bdHFUD8gBNtrY5yVJCnAAiBoskAbS5NkmUVJg8gT2zzMeii6tshM0hU2Ej5dNaFcdSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZhFnYZrCn%2FFhU5vOKtwDIes1u6%2F6un9PWLEtAR7nYJ59EelfDm8P1UuH6hqexl0EdrDhcYWMHbzX4IlQApamp75oeObQMbGpMECC%2Fg%2Fi06rUmPKXH0gZ4aC16vd5DgSHGsfeTiPQE3fSsjt0QwOiV%2B3TPJDi0WMYz%2B30L0GL7pQYa5TdIUfDQ5%2F4FzPkavj4XQD9ekytIGi7L9diZUPkGcvsE3s8aIGhkf8MZ2O9ybMgmtANffqBPNjYGBRJRlggeAdrLX1%2FyPmL1LkTrZDdBrKNvsHQTbxA5L1GEAvWwj76sgE9PTgMSXuGGAIm%2BNekYOMBV%2F1sDdzYcaRZzDSO9%2FQeISOxGV3nn69Icqxqb55150s9sd9B6HxDypgoZw9nZO0uPZN0XS2arC%2Bzbrb8%2B0JudjpAly0BPmAviUX3yHpM0pBYc%2B947mkMnHUjVlmsC7oBrDEwzbo5ul08uk%2F8umbfyqaYg7BqpeRfF5rvU3i42nLy9Z%2FVqx6fFhA%2FRVPVESeKcUp%2FJHWEz1Ll6jr%2BfrmYC%2BPKpyRMYQUmtseVXx2BdcLrTn9d9lQbn8XKkRAlruoyjl3iziVL0oDTYTLDa4BIhIDpyeo0am7SVnGyBV6tQmVIQxDjW6cCrNXmVL9jSy8mlWI7QLKzA%2B4ws6T3vAY6pgHunqPi00RyDNT1iLaNR4j9iDqQPaC3eUJG5HSEAgTLiUbEFmSaBILYk41eI6tGcuAKIxndat24v4c0GV9qkFr4RnAHEP10dELUT9k7oSzg02vHP0zrzL91QrNGIr%2FRGgKlQXxm%2B%2BLuF1zVFzr56ztGdqiT1LjSk59rekmlZVfkuM0QiwngfWnQ4SCubckWhGlsFpn%2BNwJmpWVWaZlywroWz%2BgdDnZR&X-Amz-Signature=9891a4fcc6b7a5144a18fe6cdbdcc2ce859e84fb7b2e4ffd29f512e987efb138&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3NZLKQ5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq72q4KBLlPECOVjhho1mMtHVT3OVI2VYfIuPCieNOuAiEAieIRnYNNSbUjD14IQN%2FjcPINAltFv4TQGg0PWiuIUHIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPsV7c%2BXIJtOjXjY9SrcA4f4RDjsRqggZJOqM5Jbf5j%2FzzQtZaA575tEz821JVsJU%2BqCzxaILtqp4n6N4RXsJNgvIm7vtIKf8miMK7eaYP6VXA61g2ZkuOZLSsBZjhPOwPCGHlGfTo2twF6bc88nxrDt2TXQEfJAq53IsLocKv6Wm6XwMxXD777HbAgZWuYTXmYep%2BRxSERB7cG%2BJePLdQ832Uuq0YhcCVpS4yDzouMzIfS%2BuzOJRS0OxS%2B1YYjqKlD%2BigD89B%2F%2BLIvOGbVysF3RlN9Yi%2BVonmubslWgvoVMX4IMfnxkpWLKlKq6%2BqRClvk7aBdeBrykZyFFm1PU0MfRqT0qZ1kYIR29Bwn63CrWjdZZDAMsFtmOutHJxb9%2FwQULJDPc4NlTGbHPNTDZJg0Ev1K3xYZvu79X%2BStw%2FQ4jWckT96Q1F0up%2FqNBxIAHrA4IjjbXnKmkQSDwesDp81kDpdda4WktJFSFWzF0%2FoYNZBXlyV2dMKNNqL9GAqoYEr5G2bAF851y1qKLLFScZZAeuwr7WZ0q0kpWh6sam4Hj59wfPo6du%2BJ2O%2FuKPVTCWaE6adVy8hRhXejCZpfcJrtt38Cnw82KuVHwBXKinxN%2FyLrku1OIfMz6nAPHkxUzr81iLdUj39jiCxPkMMCk97wGOqUByPqU24w6qlO%2Bq6HgVbvVxu1Q3ZyyDDY25cPWNbaqdikaEhRjj6wukMOPZCR7j9ekFt68IBchDWwP8qnL54gb0Dq%2FKymponUAqJBKw9YOiZ8pIEbVjtbHXQ4hSfUhTelxQUiut0lWgenxcsk9%2BJcMfUfrxw6XJa%2BkLcvxdVs6Umvi0ppGcVUKpqni%2Fiat0y%2FNWLJVyhsg%2B9IpxWpwz63eOfMqHP9D&X-Amz-Signature=4d72a92941b33c70ad263eba0a2096c67bd34ce3b58c4f294521d0b55f9830b0&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DXTG7VW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUwhicX5cs7LHZDvd6JBYB5ZQ91PcS6WpZYF%2BfM%2BLwxQIhAPT6sOw5xGbHZ%2BEk9Uo4Mh09f%2BEUkS0tNut8tAPAdu9mKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgylI2qS8T7MVEJAGAYq3AOfyQfhdfKbjKfolYOnCKLC8rFeC4w6x%2FiSwmj6QqTEXW0S2L7%2FmnJBpEfjBvIjiLI1Yvw5G0UiXySw7eoWQ%2BB6IKSmujn2EN49nHlpTc6HYRlg9Cak39oyoe334xJZREsZcf1yqmEH6hwCLwDlDcNjHvfIMMPtfVxLastKc4WrqKnRlxG3VcG0wPEk0KtEr6QPzqg%2B0flp8HiDzOcdVpi6tqNh8%2FTBx%2FxB%2BEGuyRhyZVArAnMDN%2FXhev0EBPPqwyATnEAani7Nw6O%2FC3fsFJ5%2B3TGcQ4mMU%2FyAXGtJleHJMnYb9pp333FBpdfUjaFY388XaXq9U42MuhOx%2FmOUXKU0l4RBeoBlhNw3au6KVegFiWUnIQfmAq6A7wVeDTgdxrkdZMuys9Qo7XUH0eV2Zy4jbrdBQTy9rBNYTvukM3IJUcoCPZIR7mmv3vCbvDXRcrJ9okeiCzc1I%2BBVPBeTDfcOxtSF890FqCsuvlZjz2QqhAkNh4cGErsMRXiMYJwYXzj7xbfCMq8hkPFHgoZEMVOe%2BRy71mGjH6qg68uqstdbChQuMnTimVxcU6f4AHp9ZRjkf9MXR3A4jjZZ4GS286O9c%2F44tJAzKqGPPXiecfX5vfYo2erHeixqoFbHuTCXpfe8BjqkAUhcP1IDp6uMrXDOjH3WbBfy02%2BPRhML6r6HcrgRKGRUbKSX7fXyl%2FhUprAqz9UPQ1SssujCn0paoeefSJp%2FEM%2BiKm74UEs3C6%2BrUrcwTrBefA2HcCQO%2BBmeetWv2DUhFkOFXO6ZHP3eKzqW5s8DYTP%2BME8HaoT9RePf10Gs2MGaWfYv31%2BUdqIKVeDXbe8BwTFUZXd7HRXJhq43%2FughwshFdK6o&X-Amz-Signature=bc1d3f0202bf33b34401268f7b2dbe143035cd29e67a05e90f0e25fab4047299&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCTEKUJL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA06J0%2B6WxISNJHgcXGrY3uxdH0CGX4pSqg8MOQ9exhPAiAyJ49tyJ%2BgdRTVNlTKePMgeyIGKCKkt%2FWQ8yrn%2FpiNfiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGC9hgjJgFhr4NMBBKtwD0WGW%2BQzTEzMCkukLGiG2C%2B30xjBLUwnyUmzVfgcw9p7I%2F1YXEyMi2%2BPPlwO6CanO0oUtlrnvoAxEoT0ijCcwKUlaUvq0gQaaVhlUWK9qDezLyFS5KibKuOfFgJjXALxVcUKHxWoeTrJazBAPm5in%2Bl8CU8YrqQZDS0%2B6qxeuelHGFE20vZYOESK5pSL4C4VwQaetA9TAyY3ohu2GB8PSLLqmiPdk6yjCbJ7y6HxOWhXR9egQsZLfNBE5I7KgTYlB8D%2BSx99%2B5o11pmayKiDtkUAG9ZRiewMykpuJ7yDxmw%2FlF3c6tjJj5eioPo02OTJr2%2BDF%2BJtxhQdmT4FWUjLtzanmr%2BcMuZ1DyMzTOaLl3OK2wlU6AoS1iLxTYrRlA4y%2B6eCFUKmBUxGSUPqwBEgH22JNKdIIhrJx7pKNKLw%2Fjk%2Fq1TrMhghHdWKiML2Cftv9hNvUDPnS8tEiokjOUzMduLjMFVbwagLgmxLppgSiPS%2F527BuY3dFAshzDfZDJvgvncEEZ76nrFJEuumo7z%2F%2BRHawX5%2FPK7dl%2F1BfN6KFYrv9lTm0yOrdfZXz6wxvRbKxVE%2BaYOPnmB19HRNboVElOJS2uTqh0%2BbZJDPxZnM94Ry0O0tkRClw9xngAvQw3aT3vAY6pgEm8CukLS5W8Uf5hnYzl1yfkD5BRkRGLuPTK%2BFU5wP7zpB5HXHBbBlHXhBZidRzQTN9I%2BBLh5t%2FURTOC%2BnQ5p9kLEZ3eoOiJS5lEg%2B7%2FQQntPg%2BvmV%2FetV1RV5AHVutZ5g%2FswlwAnk48fwhnT%2Ba7GMiuhK%2BHdvkx6Pzs3usDsZftsL1AdcpzRu9f6hmrDOAiPR49%2BJG1p1aPh1ZDYgaYR62l9s4WNyY&X-Amz-Signature=8947d3f07bfd94e91f9e9c30e828dd397a125026e6e15002c1466a2a3a5188c9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCTEKUJL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA06J0%2B6WxISNJHgcXGrY3uxdH0CGX4pSqg8MOQ9exhPAiAyJ49tyJ%2BgdRTVNlTKePMgeyIGKCKkt%2FWQ8yrn%2FpiNfiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGC9hgjJgFhr4NMBBKtwD0WGW%2BQzTEzMCkukLGiG2C%2B30xjBLUwnyUmzVfgcw9p7I%2F1YXEyMi2%2BPPlwO6CanO0oUtlrnvoAxEoT0ijCcwKUlaUvq0gQaaVhlUWK9qDezLyFS5KibKuOfFgJjXALxVcUKHxWoeTrJazBAPm5in%2Bl8CU8YrqQZDS0%2B6qxeuelHGFE20vZYOESK5pSL4C4VwQaetA9TAyY3ohu2GB8PSLLqmiPdk6yjCbJ7y6HxOWhXR9egQsZLfNBE5I7KgTYlB8D%2BSx99%2B5o11pmayKiDtkUAG9ZRiewMykpuJ7yDxmw%2FlF3c6tjJj5eioPo02OTJr2%2BDF%2BJtxhQdmT4FWUjLtzanmr%2BcMuZ1DyMzTOaLl3OK2wlU6AoS1iLxTYrRlA4y%2B6eCFUKmBUxGSUPqwBEgH22JNKdIIhrJx7pKNKLw%2Fjk%2Fq1TrMhghHdWKiML2Cftv9hNvUDPnS8tEiokjOUzMduLjMFVbwagLgmxLppgSiPS%2F527BuY3dFAshzDfZDJvgvncEEZ76nrFJEuumo7z%2F%2BRHawX5%2FPK7dl%2F1BfN6KFYrv9lTm0yOrdfZXz6wxvRbKxVE%2BaYOPnmB19HRNboVElOJS2uTqh0%2BbZJDPxZnM94Ry0O0tkRClw9xngAvQw3aT3vAY6pgEm8CukLS5W8Uf5hnYzl1yfkD5BRkRGLuPTK%2BFU5wP7zpB5HXHBbBlHXhBZidRzQTN9I%2BBLh5t%2FURTOC%2BnQ5p9kLEZ3eoOiJS5lEg%2B7%2FQQntPg%2BvmV%2FetV1RV5AHVutZ5g%2FswlwAnk48fwhnT%2Ba7GMiuhK%2BHdvkx6Pzs3usDsZftsL1AdcpzRu9f6hmrDOAiPR49%2BJG1p1aPh1ZDYgaYR62l9s4WNyY&X-Amz-Signature=1ca382b7b95dc1513791f0d51bb9ed69927675fc3c5bf9b3505d6345bb0eb224&X-Amz-SignedHeaders=host&x-id=GetObject)

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
