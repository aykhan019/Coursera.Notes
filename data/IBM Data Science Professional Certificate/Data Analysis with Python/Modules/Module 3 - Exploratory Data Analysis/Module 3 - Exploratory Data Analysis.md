

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R25PWZL5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDc9K7bIGXQz1NWI1su%2BkDoURtNxzqS6vI2BFgwnuo66AIgEH4B%2BU%2BZUmY8h1Qzmfqp6qkzqXiu1QsRiLBo0wZCBvYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHiKtGgAbhC6hzfucCrcA5tnElarLMHy4GjhbVTpD6J6wawUmS%2B0JEPEX%2Fcx0u%2FgbTZ%2FLVmRgSfg8mDdPVA76%2BhUfrs38ULG3YWWof1LfeZvlCgBh3J5vPLdBxM81tXqKNTJdFcrAA95aSnE2CfioTEFzHRcY9zdyd%2FsG84Wrxvk%2BLjdTPg6EBLqpcbZmcpkcgxbKL%2BLQyGWZXpNP0P5%2BchQbuWNBZTpvF1EQpbUiuKpBLNFdJr2BMhcn927RqmAGtrsfWzfIkwJY%2FQmb0wwnKXNE6CXFDzv7ZCTqUhBGGE%2BsvYgp873Ul8exxswRdY4xsKcCd12NYli%2FQ9hEzYk4boeGxIPtZj26fpXgchvkqxmUqQd0Qi2%2Fzm4VdUV3qvbT4XN49ZD86OuW4HSsFlmDH9%2BXDzbKu2f2jBh%2FkYOAuGD%2FCqHZpO3FdxYudPCLinj2%2BPVypWE6NdaboGPluqbrYV06jsa1L%2BOB3x1lb5RD1pIMPhFGIjI9X1QbmdnXav3Oj%2FALHSCa5hWc51xJZbzBC945hI9pgGqPjQ825vj9TdY3%2B1Jvm%2B6Z186BEaVQvBxi9XV%2F4GkO2AWmO9dRHAn81vJ1nlmqj%2B0ymT9n6Urzt0BYoqARtPGgDCWl2BbwkLFnH4r%2Br7JnWcHEE9cMNu8%2FbwGOqUBxgzZ89cD2Ywt6ArPcX5igGhcC0ESuusrrKGzDHK0L14DXlr7cpDewJS02w6OHgpDtl6UGegBN16g3%2B32WuQN6zK4FdBL1g5HkVYSgoqsr4zbiDAAQeqsnfIIP4wgB3zozpBzX99ksGYFBuXFu0voNT7J0quHpRQITPP%2F5G2N%2FnwOPfoZa77bMGTTCQPAk2VyfML2wMVbUFKtRF7GOC4fJZ72ILQL&X-Amz-Signature=192b70bf56d6ac37eb0a984a6158696dd446c53404db8cc9f70e57e2103d8924&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R25PWZL5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDc9K7bIGXQz1NWI1su%2BkDoURtNxzqS6vI2BFgwnuo66AIgEH4B%2BU%2BZUmY8h1Qzmfqp6qkzqXiu1QsRiLBo0wZCBvYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHiKtGgAbhC6hzfucCrcA5tnElarLMHy4GjhbVTpD6J6wawUmS%2B0JEPEX%2Fcx0u%2FgbTZ%2FLVmRgSfg8mDdPVA76%2BhUfrs38ULG3YWWof1LfeZvlCgBh3J5vPLdBxM81tXqKNTJdFcrAA95aSnE2CfioTEFzHRcY9zdyd%2FsG84Wrxvk%2BLjdTPg6EBLqpcbZmcpkcgxbKL%2BLQyGWZXpNP0P5%2BchQbuWNBZTpvF1EQpbUiuKpBLNFdJr2BMhcn927RqmAGtrsfWzfIkwJY%2FQmb0wwnKXNE6CXFDzv7ZCTqUhBGGE%2BsvYgp873Ul8exxswRdY4xsKcCd12NYli%2FQ9hEzYk4boeGxIPtZj26fpXgchvkqxmUqQd0Qi2%2Fzm4VdUV3qvbT4XN49ZD86OuW4HSsFlmDH9%2BXDzbKu2f2jBh%2FkYOAuGD%2FCqHZpO3FdxYudPCLinj2%2BPVypWE6NdaboGPluqbrYV06jsa1L%2BOB3x1lb5RD1pIMPhFGIjI9X1QbmdnXav3Oj%2FALHSCa5hWc51xJZbzBC945hI9pgGqPjQ825vj9TdY3%2B1Jvm%2B6Z186BEaVQvBxi9XV%2F4GkO2AWmO9dRHAn81vJ1nlmqj%2B0ymT9n6Urzt0BYoqARtPGgDCWl2BbwkLFnH4r%2Br7JnWcHEE9cMNu8%2FbwGOqUBxgzZ89cD2Ywt6ArPcX5igGhcC0ESuusrrKGzDHK0L14DXlr7cpDewJS02w6OHgpDtl6UGegBN16g3%2B32WuQN6zK4FdBL1g5HkVYSgoqsr4zbiDAAQeqsnfIIP4wgB3zozpBzX99ksGYFBuXFu0voNT7J0quHpRQITPP%2F5G2N%2FnwOPfoZa77bMGTTCQPAk2VyfML2wMVbUFKtRF7GOC4fJZ72ILQL&X-Amz-Signature=693663f976b26fd1c5a30e1954a9bac9ef4a4db0312199bce9eca0141d1d2ad8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R25PWZL5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDc9K7bIGXQz1NWI1su%2BkDoURtNxzqS6vI2BFgwnuo66AIgEH4B%2BU%2BZUmY8h1Qzmfqp6qkzqXiu1QsRiLBo0wZCBvYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHiKtGgAbhC6hzfucCrcA5tnElarLMHy4GjhbVTpD6J6wawUmS%2B0JEPEX%2Fcx0u%2FgbTZ%2FLVmRgSfg8mDdPVA76%2BhUfrs38ULG3YWWof1LfeZvlCgBh3J5vPLdBxM81tXqKNTJdFcrAA95aSnE2CfioTEFzHRcY9zdyd%2FsG84Wrxvk%2BLjdTPg6EBLqpcbZmcpkcgxbKL%2BLQyGWZXpNP0P5%2BchQbuWNBZTpvF1EQpbUiuKpBLNFdJr2BMhcn927RqmAGtrsfWzfIkwJY%2FQmb0wwnKXNE6CXFDzv7ZCTqUhBGGE%2BsvYgp873Ul8exxswRdY4xsKcCd12NYli%2FQ9hEzYk4boeGxIPtZj26fpXgchvkqxmUqQd0Qi2%2Fzm4VdUV3qvbT4XN49ZD86OuW4HSsFlmDH9%2BXDzbKu2f2jBh%2FkYOAuGD%2FCqHZpO3FdxYudPCLinj2%2BPVypWE6NdaboGPluqbrYV06jsa1L%2BOB3x1lb5RD1pIMPhFGIjI9X1QbmdnXav3Oj%2FALHSCa5hWc51xJZbzBC945hI9pgGqPjQ825vj9TdY3%2B1Jvm%2B6Z186BEaVQvBxi9XV%2F4GkO2AWmO9dRHAn81vJ1nlmqj%2B0ymT9n6Urzt0BYoqARtPGgDCWl2BbwkLFnH4r%2Br7JnWcHEE9cMNu8%2FbwGOqUBxgzZ89cD2Ywt6ArPcX5igGhcC0ESuusrrKGzDHK0L14DXlr7cpDewJS02w6OHgpDtl6UGegBN16g3%2B32WuQN6zK4FdBL1g5HkVYSgoqsr4zbiDAAQeqsnfIIP4wgB3zozpBzX99ksGYFBuXFu0voNT7J0quHpRQITPP%2F5G2N%2FnwOPfoZa77bMGTTCQPAk2VyfML2wMVbUFKtRF7GOC4fJZ72ILQL&X-Amz-Signature=a8d5ed251cb84c8e91493aacc13cbec01b0f573ac52a3ffe0e0a05ec7fa44390&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y75L7M2U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhMpOKCCyMRkD%2FR%2FhVD%2BtBGcOqlCd1PM9c4Ft5DFMQWAiEA%2FegS0i9jjkCmTdE5rpGdhnnVaWDc0VUyDp%2BdTQxtGuUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlMleJj4Eb0Ypya5SrcA%2BmInK8I%2FRMN%2FuROtaaGhhs3F1iHx3uhKiHKJSsNbViTNOJuiBewDzjSmanka8YGywHi9LKn4rOSEKoD%2FAheroTyO0repYUahko0JPdhRhNFAIiJVjM4UWPKdnM8P3y8F9yzHkHtSqQdufkY42b1VBZOeiVkS%2B%2BTHMTMF9XpoQXtQ691W8vGh44lVQ5liA4AlSRZtTbShwnG%2BCHfeFFfpngxc0UEIkmSnNfDgtWvhMW%2Bs1dbSCjPS1r4wpkl4Nw3xwGB7OdBgSs66%2BZeDaZanCD78ncBJ1foo%2BgdDzbSeRakwtyoubsQ4pVa00%2Bg0Dy%2BROeoLLkDFFfgAsHcGHr7at%2FwAaRv236RGJTk7ZLCVai69KWwsi6ll3NHRqfujP482X6CGxFyvsaqcukdjQlOmJSyIDv7p4c6jcha3%2FCwoLrGOcYxWq3ZLnmWrFNemQacc58ENXUMGWicuDu%2B%2Fe%2Fq96xBq79DSh4cFDIAD%2BtzF%2Bh4ficvlCHZBsQLR8nvZPjd13mamMusGPGDq%2Fd105O4FjxPxQ%2F9B6kg2lkCm1VCb4ybOY6gSqbOo0xUyQMYdaQtBv%2FX9Aahv%2F5KWRl%2FT8%2BeIcxNRYi00wr7mV3OYU3IIYksJa5NsBaeDfeAY08FMLu5%2FbwGOqUBuwIkBhx8nwmPzHieobgbzlypVwaAvVm7A9FZAuOKFRzUwkiESA6MwwDlpcJVmaVT5J53moJK4Hj%2BgJEHd7G2EDxYbgFIG5IuIXupDYvS71vsT7pv2YjDxQH%2BprMyfdzke9f90HD70cfR8vTwbu087GLEHdZQc3cHvjwbnafme7c80ny74OzDMn8S2wa2ELBsfDqRfJSAY%2BMg5bJ%2BpchA4OtS9pwx&X-Amz-Signature=b06f033886a66ca96bf8caf32a58c07d690192d049f2e426961873331bc6b1c9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y75L7M2U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhMpOKCCyMRkD%2FR%2FhVD%2BtBGcOqlCd1PM9c4Ft5DFMQWAiEA%2FegS0i9jjkCmTdE5rpGdhnnVaWDc0VUyDp%2BdTQxtGuUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlMleJj4Eb0Ypya5SrcA%2BmInK8I%2FRMN%2FuROtaaGhhs3F1iHx3uhKiHKJSsNbViTNOJuiBewDzjSmanka8YGywHi9LKn4rOSEKoD%2FAheroTyO0repYUahko0JPdhRhNFAIiJVjM4UWPKdnM8P3y8F9yzHkHtSqQdufkY42b1VBZOeiVkS%2B%2BTHMTMF9XpoQXtQ691W8vGh44lVQ5liA4AlSRZtTbShwnG%2BCHfeFFfpngxc0UEIkmSnNfDgtWvhMW%2Bs1dbSCjPS1r4wpkl4Nw3xwGB7OdBgSs66%2BZeDaZanCD78ncBJ1foo%2BgdDzbSeRakwtyoubsQ4pVa00%2Bg0Dy%2BROeoLLkDFFfgAsHcGHr7at%2FwAaRv236RGJTk7ZLCVai69KWwsi6ll3NHRqfujP482X6CGxFyvsaqcukdjQlOmJSyIDv7p4c6jcha3%2FCwoLrGOcYxWq3ZLnmWrFNemQacc58ENXUMGWicuDu%2B%2Fe%2Fq96xBq79DSh4cFDIAD%2BtzF%2Bh4ficvlCHZBsQLR8nvZPjd13mamMusGPGDq%2Fd105O4FjxPxQ%2F9B6kg2lkCm1VCb4ybOY6gSqbOo0xUyQMYdaQtBv%2FX9Aahv%2F5KWRl%2FT8%2BeIcxNRYi00wr7mV3OYU3IIYksJa5NsBaeDfeAY08FMLu5%2FbwGOqUBuwIkBhx8nwmPzHieobgbzlypVwaAvVm7A9FZAuOKFRzUwkiESA6MwwDlpcJVmaVT5J53moJK4Hj%2BgJEHd7G2EDxYbgFIG5IuIXupDYvS71vsT7pv2YjDxQH%2BprMyfdzke9f90HD70cfR8vTwbu087GLEHdZQc3cHvjwbnafme7c80ny74OzDMn8S2wa2ELBsfDqRfJSAY%2BMg5bJ%2BpchA4OtS9pwx&X-Amz-Signature=3e99de98f9ea3cf1a07676f063b6772747e1413405ee63703f61d6742cecc7e3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y75L7M2U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhMpOKCCyMRkD%2FR%2FhVD%2BtBGcOqlCd1PM9c4Ft5DFMQWAiEA%2FegS0i9jjkCmTdE5rpGdhnnVaWDc0VUyDp%2BdTQxtGuUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlMleJj4Eb0Ypya5SrcA%2BmInK8I%2FRMN%2FuROtaaGhhs3F1iHx3uhKiHKJSsNbViTNOJuiBewDzjSmanka8YGywHi9LKn4rOSEKoD%2FAheroTyO0repYUahko0JPdhRhNFAIiJVjM4UWPKdnM8P3y8F9yzHkHtSqQdufkY42b1VBZOeiVkS%2B%2BTHMTMF9XpoQXtQ691W8vGh44lVQ5liA4AlSRZtTbShwnG%2BCHfeFFfpngxc0UEIkmSnNfDgtWvhMW%2Bs1dbSCjPS1r4wpkl4Nw3xwGB7OdBgSs66%2BZeDaZanCD78ncBJ1foo%2BgdDzbSeRakwtyoubsQ4pVa00%2Bg0Dy%2BROeoLLkDFFfgAsHcGHr7at%2FwAaRv236RGJTk7ZLCVai69KWwsi6ll3NHRqfujP482X6CGxFyvsaqcukdjQlOmJSyIDv7p4c6jcha3%2FCwoLrGOcYxWq3ZLnmWrFNemQacc58ENXUMGWicuDu%2B%2Fe%2Fq96xBq79DSh4cFDIAD%2BtzF%2Bh4ficvlCHZBsQLR8nvZPjd13mamMusGPGDq%2Fd105O4FjxPxQ%2F9B6kg2lkCm1VCb4ybOY6gSqbOo0xUyQMYdaQtBv%2FX9Aahv%2F5KWRl%2FT8%2BeIcxNRYi00wr7mV3OYU3IIYksJa5NsBaeDfeAY08FMLu5%2FbwGOqUBuwIkBhx8nwmPzHieobgbzlypVwaAvVm7A9FZAuOKFRzUwkiESA6MwwDlpcJVmaVT5J53moJK4Hj%2BgJEHd7G2EDxYbgFIG5IuIXupDYvS71vsT7pv2YjDxQH%2BprMyfdzke9f90HD70cfR8vTwbu087GLEHdZQc3cHvjwbnafme7c80ny74OzDMn8S2wa2ELBsfDqRfJSAY%2BMg5bJ%2BpchA4OtS9pwx&X-Amz-Signature=b2258216566f26cb5467697af2feb4c6f12246d239719dd4cf78ee38d1c3f354&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y75L7M2U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhMpOKCCyMRkD%2FR%2FhVD%2BtBGcOqlCd1PM9c4Ft5DFMQWAiEA%2FegS0i9jjkCmTdE5rpGdhnnVaWDc0VUyDp%2BdTQxtGuUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlMleJj4Eb0Ypya5SrcA%2BmInK8I%2FRMN%2FuROtaaGhhs3F1iHx3uhKiHKJSsNbViTNOJuiBewDzjSmanka8YGywHi9LKn4rOSEKoD%2FAheroTyO0repYUahko0JPdhRhNFAIiJVjM4UWPKdnM8P3y8F9yzHkHtSqQdufkY42b1VBZOeiVkS%2B%2BTHMTMF9XpoQXtQ691W8vGh44lVQ5liA4AlSRZtTbShwnG%2BCHfeFFfpngxc0UEIkmSnNfDgtWvhMW%2Bs1dbSCjPS1r4wpkl4Nw3xwGB7OdBgSs66%2BZeDaZanCD78ncBJ1foo%2BgdDzbSeRakwtyoubsQ4pVa00%2Bg0Dy%2BROeoLLkDFFfgAsHcGHr7at%2FwAaRv236RGJTk7ZLCVai69KWwsi6ll3NHRqfujP482X6CGxFyvsaqcukdjQlOmJSyIDv7p4c6jcha3%2FCwoLrGOcYxWq3ZLnmWrFNemQacc58ENXUMGWicuDu%2B%2Fe%2Fq96xBq79DSh4cFDIAD%2BtzF%2Bh4ficvlCHZBsQLR8nvZPjd13mamMusGPGDq%2Fd105O4FjxPxQ%2F9B6kg2lkCm1VCb4ybOY6gSqbOo0xUyQMYdaQtBv%2FX9Aahv%2F5KWRl%2FT8%2BeIcxNRYi00wr7mV3OYU3IIYksJa5NsBaeDfeAY08FMLu5%2FbwGOqUBuwIkBhx8nwmPzHieobgbzlypVwaAvVm7A9FZAuOKFRzUwkiESA6MwwDlpcJVmaVT5J53moJK4Hj%2BgJEHd7G2EDxYbgFIG5IuIXupDYvS71vsT7pv2YjDxQH%2BprMyfdzke9f90HD70cfR8vTwbu087GLEHdZQc3cHvjwbnafme7c80ny74OzDMn8S2wa2ELBsfDqRfJSAY%2BMg5bJ%2BpchA4OtS9pwx&X-Amz-Signature=fa5f8f95cf555586c6dbaf43d0fa2ecf853beaadfb7c4530277d0bacd5facf64&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y75L7M2U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhMpOKCCyMRkD%2FR%2FhVD%2BtBGcOqlCd1PM9c4Ft5DFMQWAiEA%2FegS0i9jjkCmTdE5rpGdhnnVaWDc0VUyDp%2BdTQxtGuUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlMleJj4Eb0Ypya5SrcA%2BmInK8I%2FRMN%2FuROtaaGhhs3F1iHx3uhKiHKJSsNbViTNOJuiBewDzjSmanka8YGywHi9LKn4rOSEKoD%2FAheroTyO0repYUahko0JPdhRhNFAIiJVjM4UWPKdnM8P3y8F9yzHkHtSqQdufkY42b1VBZOeiVkS%2B%2BTHMTMF9XpoQXtQ691W8vGh44lVQ5liA4AlSRZtTbShwnG%2BCHfeFFfpngxc0UEIkmSnNfDgtWvhMW%2Bs1dbSCjPS1r4wpkl4Nw3xwGB7OdBgSs66%2BZeDaZanCD78ncBJ1foo%2BgdDzbSeRakwtyoubsQ4pVa00%2Bg0Dy%2BROeoLLkDFFfgAsHcGHr7at%2FwAaRv236RGJTk7ZLCVai69KWwsi6ll3NHRqfujP482X6CGxFyvsaqcukdjQlOmJSyIDv7p4c6jcha3%2FCwoLrGOcYxWq3ZLnmWrFNemQacc58ENXUMGWicuDu%2B%2Fe%2Fq96xBq79DSh4cFDIAD%2BtzF%2Bh4ficvlCHZBsQLR8nvZPjd13mamMusGPGDq%2Fd105O4FjxPxQ%2F9B6kg2lkCm1VCb4ybOY6gSqbOo0xUyQMYdaQtBv%2FX9Aahv%2F5KWRl%2FT8%2BeIcxNRYi00wr7mV3OYU3IIYksJa5NsBaeDfeAY08FMLu5%2FbwGOqUBuwIkBhx8nwmPzHieobgbzlypVwaAvVm7A9FZAuOKFRzUwkiESA6MwwDlpcJVmaVT5J53moJK4Hj%2BgJEHd7G2EDxYbgFIG5IuIXupDYvS71vsT7pv2YjDxQH%2BprMyfdzke9f90HD70cfR8vTwbu087GLEHdZQc3cHvjwbnafme7c80ny74OzDMn8S2wa2ELBsfDqRfJSAY%2BMg5bJ%2BpchA4OtS9pwx&X-Amz-Signature=8970e55132f1d11dff8351b9671f022182931da6bef99dc0f3d2393ef50e388d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y75L7M2U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhMpOKCCyMRkD%2FR%2FhVD%2BtBGcOqlCd1PM9c4Ft5DFMQWAiEA%2FegS0i9jjkCmTdE5rpGdhnnVaWDc0VUyDp%2BdTQxtGuUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlMleJj4Eb0Ypya5SrcA%2BmInK8I%2FRMN%2FuROtaaGhhs3F1iHx3uhKiHKJSsNbViTNOJuiBewDzjSmanka8YGywHi9LKn4rOSEKoD%2FAheroTyO0repYUahko0JPdhRhNFAIiJVjM4UWPKdnM8P3y8F9yzHkHtSqQdufkY42b1VBZOeiVkS%2B%2BTHMTMF9XpoQXtQ691W8vGh44lVQ5liA4AlSRZtTbShwnG%2BCHfeFFfpngxc0UEIkmSnNfDgtWvhMW%2Bs1dbSCjPS1r4wpkl4Nw3xwGB7OdBgSs66%2BZeDaZanCD78ncBJ1foo%2BgdDzbSeRakwtyoubsQ4pVa00%2Bg0Dy%2BROeoLLkDFFfgAsHcGHr7at%2FwAaRv236RGJTk7ZLCVai69KWwsi6ll3NHRqfujP482X6CGxFyvsaqcukdjQlOmJSyIDv7p4c6jcha3%2FCwoLrGOcYxWq3ZLnmWrFNemQacc58ENXUMGWicuDu%2B%2Fe%2Fq96xBq79DSh4cFDIAD%2BtzF%2Bh4ficvlCHZBsQLR8nvZPjd13mamMusGPGDq%2Fd105O4FjxPxQ%2F9B6kg2lkCm1VCb4ybOY6gSqbOo0xUyQMYdaQtBv%2FX9Aahv%2F5KWRl%2FT8%2BeIcxNRYi00wr7mV3OYU3IIYksJa5NsBaeDfeAY08FMLu5%2FbwGOqUBuwIkBhx8nwmPzHieobgbzlypVwaAvVm7A9FZAuOKFRzUwkiESA6MwwDlpcJVmaVT5J53moJK4Hj%2BgJEHd7G2EDxYbgFIG5IuIXupDYvS71vsT7pv2YjDxQH%2BprMyfdzke9f90HD70cfR8vTwbu087GLEHdZQc3cHvjwbnafme7c80ny74OzDMn8S2wa2ELBsfDqRfJSAY%2BMg5bJ%2BpchA4OtS9pwx&X-Amz-Signature=5eedc56ed5ff1d24ed6cb7399dfd2e72e7a522a39058aa530548a770f82d2e48&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVB6EQAP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYt2RtNjkNRBK6ElDdmG23sMEg7JZQ%2BskYZiFmnzX6WAiEA9b9EH0pEX8Xcgy7ujSLcVk%2Fem62l%2F5UJJAuyMX3p07oqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPohrEJ4pHA3wV8yqSrcAxtYuA%2FgIRmDHjC9Rf8Hn6bn%2FxmyKrbkAPjj01WOojaXr0TcdlnVGcyStjLMxXU4HmxCkV27jUhmNjAQwxmI0JZz3ss6yn82rHhwNNpiTMHccl4AzzGbbP4qM%2Bho5MPF7oxSVEAmtxLodVEPtqzZUI9vr6EyCboSxRFR3DIOlfOyFycsmGccqpiCL9Xi0B5uDzmvyY44osCiOEeADdlwX1xgERayAajOjMVEf6HEPq4%2BJCnhlZOeonjEttuCipHcksQy74OTKYk3KVd4HSpqkZ2WRo%2FVW%2BPnn3Wav9iszCosfh7PIO2Yzer42s543nFlOImpdXspcHICQv%2Bsjy4arj7OvsWwDIO0zonMTyhjpFa2NhMc2ADwykj9m5mXYtVK6PBbwwSgZxNa5OODvOnXBwbx6ofKSitKWXnxMpJFGBxIuhxxOnIETXWGdj3Wc2q1EWmJVQL%2BhYTIHQpJFUd2TOPraVdF6WZ22%2Bw%2BPi9v3UVTdFui%2FPKgX0kjStQaXzT3n14%2FaK1zj7%2FV0yQoe%2BXcVAG7fuCVHp31vbGMMlqcldAO2y0WXc5TJKrzpSrBKTgkfuiOp%2B1wSSN%2BhItRDiU53yJl7N%2B5JCicQIeot5ZEgUO1ySg5mSeVIHrP27ZgMNm4%2FbwGOqUBCXsIz5gLDxwkLKjjJ2GW8abKjID2wJIFN6r2tODzN5npdlhMnY68wMIcC3H4LdQXDQ0dekv8gGJyltQhoJxwl8pvuCT74NBtglbDKNpJlneo4Dn80y3JeCdo2gdq8ujYl8Uw%2FwxRLbmqgbGcPAQC1kuit%2F23xqOyjYLXnxBWGcHk1u1euhbKHH2C%2FqLoMGhczTpzmDJkQuTFvqGP3kDp%2BPR6Ycga&X-Amz-Signature=be0c3e83c41a07d6f3f39bb49188785c439e9732fd65d549ac317ce572d11f67&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466527IV65K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOByJ8olVoJyOFmz99%2FmnhGsYu4y4%2FKOrsDWca6m722wIgErhrGZDjf9p5iRx2aqFxfm1XJftGjNNXNxkHu8Y8Xg8qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPHbz8DllAKH8AX4BSrcA9y%2FdhinobrDJpNlyHZXLodLRmk4UK6ujzlXSjknUNyKxIQ2YBqnbp1tE9OnTuZpXcvUZpR0OvljtXrlv8SbDj4vCC7tsE%2FLnx%2FWbkfrVr5J5R4pRIlBobT%2FgQ%2B2bbl2CQnYeZXO5%2B%2BtEm9WuN2PNbPH3JD%2BBpVRk0rz6thTwcRHy8x3cdN%2F2bcn8dJWNHq2RvDAGCWEKr7khIXmJQPcRwBY4yhFa6HCvZqbDD3TsHvbPatZXedB8CmdJHrXV%2BNLmrsUhf1%2F5mJtdfS3opAEmLybgV0i8tUNwD4c8HqhwkndeaXc336ojCcqzv0Qz%2FbUmknfEaSKsmZG%2F68yO9%2FcGFuwmBb1lFJ6gKAnWihWGnngd7N5%2FOTViK0%2FOMDoxR16gh%2FtAU4sk%2F8J06V%2FRGeG%2FrXay933N805iyx02bq3%2BEtZLOYRvPddlJZc18VlNg97Ae35qYGh5ad%2BZrkXBzq4AEsOV9YCn6lkZYvhlmMbbZzIIEH2yZfWlOkq10xZgS8SMd1MW7AsCGOgAnquw%2BFYe%2FI7rAAerlfGUaGbDoAjyffLdhO3fP%2BRzf9fYmBIrJD8zxCDgVLZAe35Jyj0b4pRLmASR4NQdfvo1XJ9ZP0QXZ8IarKY0y2maQow%2BpAKMMG%2F%2FbwGOqUBx2r1cX60DxzQJ5AWfWGawv4Q%2ByyqcwqGn2nHxbGEInT%2FiZMRMteCPaOzHdsSkBlAsc73DlVzesnOTFlT81FEyNNauveJJK%2BPml09X1Ea9EeNr1%2BagNENZlGtlwtyiCgrr0YvVKLy7H1cWSqXfgTUDHmoPzM23Q%2FBr53dSwfeArXjITU%2Bua0ys57PAT1cE%2BSvOa9cWeMiXlUr8CHObcqYQfCoconi&X-Amz-Signature=ae8681dafbf024c7d8f9181589bea544797d61a918848806b68cd150a9c62bd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y75L7M2U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhMpOKCCyMRkD%2FR%2FhVD%2BtBGcOqlCd1PM9c4Ft5DFMQWAiEA%2FegS0i9jjkCmTdE5rpGdhnnVaWDc0VUyDp%2BdTQxtGuUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlMleJj4Eb0Ypya5SrcA%2BmInK8I%2FRMN%2FuROtaaGhhs3F1iHx3uhKiHKJSsNbViTNOJuiBewDzjSmanka8YGywHi9LKn4rOSEKoD%2FAheroTyO0repYUahko0JPdhRhNFAIiJVjM4UWPKdnM8P3y8F9yzHkHtSqQdufkY42b1VBZOeiVkS%2B%2BTHMTMF9XpoQXtQ691W8vGh44lVQ5liA4AlSRZtTbShwnG%2BCHfeFFfpngxc0UEIkmSnNfDgtWvhMW%2Bs1dbSCjPS1r4wpkl4Nw3xwGB7OdBgSs66%2BZeDaZanCD78ncBJ1foo%2BgdDzbSeRakwtyoubsQ4pVa00%2Bg0Dy%2BROeoLLkDFFfgAsHcGHr7at%2FwAaRv236RGJTk7ZLCVai69KWwsi6ll3NHRqfujP482X6CGxFyvsaqcukdjQlOmJSyIDv7p4c6jcha3%2FCwoLrGOcYxWq3ZLnmWrFNemQacc58ENXUMGWicuDu%2B%2Fe%2Fq96xBq79DSh4cFDIAD%2BtzF%2Bh4ficvlCHZBsQLR8nvZPjd13mamMusGPGDq%2Fd105O4FjxPxQ%2F9B6kg2lkCm1VCb4ybOY6gSqbOo0xUyQMYdaQtBv%2FX9Aahv%2F5KWRl%2FT8%2BeIcxNRYi00wr7mV3OYU3IIYksJa5NsBaeDfeAY08FMLu5%2FbwGOqUBuwIkBhx8nwmPzHieobgbzlypVwaAvVm7A9FZAuOKFRzUwkiESA6MwwDlpcJVmaVT5J53moJK4Hj%2BgJEHd7G2EDxYbgFIG5IuIXupDYvS71vsT7pv2YjDxQH%2BprMyfdzke9f90HD70cfR8vTwbu087GLEHdZQc3cHvjwbnafme7c80ny74OzDMn8S2wa2ELBsfDqRfJSAY%2BMg5bJ%2BpchA4OtS9pwx&X-Amz-Signature=190f7c9da8fa26ef63c2a043161b6ecdcc398251c24d716081d1481ca5595497&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y75L7M2U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhMpOKCCyMRkD%2FR%2FhVD%2BtBGcOqlCd1PM9c4Ft5DFMQWAiEA%2FegS0i9jjkCmTdE5rpGdhnnVaWDc0VUyDp%2BdTQxtGuUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlMleJj4Eb0Ypya5SrcA%2BmInK8I%2FRMN%2FuROtaaGhhs3F1iHx3uhKiHKJSsNbViTNOJuiBewDzjSmanka8YGywHi9LKn4rOSEKoD%2FAheroTyO0repYUahko0JPdhRhNFAIiJVjM4UWPKdnM8P3y8F9yzHkHtSqQdufkY42b1VBZOeiVkS%2B%2BTHMTMF9XpoQXtQ691W8vGh44lVQ5liA4AlSRZtTbShwnG%2BCHfeFFfpngxc0UEIkmSnNfDgtWvhMW%2Bs1dbSCjPS1r4wpkl4Nw3xwGB7OdBgSs66%2BZeDaZanCD78ncBJ1foo%2BgdDzbSeRakwtyoubsQ4pVa00%2Bg0Dy%2BROeoLLkDFFfgAsHcGHr7at%2FwAaRv236RGJTk7ZLCVai69KWwsi6ll3NHRqfujP482X6CGxFyvsaqcukdjQlOmJSyIDv7p4c6jcha3%2FCwoLrGOcYxWq3ZLnmWrFNemQacc58ENXUMGWicuDu%2B%2Fe%2Fq96xBq79DSh4cFDIAD%2BtzF%2Bh4ficvlCHZBsQLR8nvZPjd13mamMusGPGDq%2Fd105O4FjxPxQ%2F9B6kg2lkCm1VCb4ybOY6gSqbOo0xUyQMYdaQtBv%2FX9Aahv%2F5KWRl%2FT8%2BeIcxNRYi00wr7mV3OYU3IIYksJa5NsBaeDfeAY08FMLu5%2FbwGOqUBuwIkBhx8nwmPzHieobgbzlypVwaAvVm7A9FZAuOKFRzUwkiESA6MwwDlpcJVmaVT5J53moJK4Hj%2BgJEHd7G2EDxYbgFIG5IuIXupDYvS71vsT7pv2YjDxQH%2BprMyfdzke9f90HD70cfR8vTwbu087GLEHdZQc3cHvjwbnafme7c80ny74OzDMn8S2wa2ELBsfDqRfJSAY%2BMg5bJ%2BpchA4OtS9pwx&X-Amz-Signature=6c8c50899609ce6bde234a15fae766ef26fb3f469db1280c6d478eb0dd2d4aad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y75L7M2U%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhMpOKCCyMRkD%2FR%2FhVD%2BtBGcOqlCd1PM9c4Ft5DFMQWAiEA%2FegS0i9jjkCmTdE5rpGdhnnVaWDc0VUyDp%2BdTQxtGuUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAlMleJj4Eb0Ypya5SrcA%2BmInK8I%2FRMN%2FuROtaaGhhs3F1iHx3uhKiHKJSsNbViTNOJuiBewDzjSmanka8YGywHi9LKn4rOSEKoD%2FAheroTyO0repYUahko0JPdhRhNFAIiJVjM4UWPKdnM8P3y8F9yzHkHtSqQdufkY42b1VBZOeiVkS%2B%2BTHMTMF9XpoQXtQ691W8vGh44lVQ5liA4AlSRZtTbShwnG%2BCHfeFFfpngxc0UEIkmSnNfDgtWvhMW%2Bs1dbSCjPS1r4wpkl4Nw3xwGB7OdBgSs66%2BZeDaZanCD78ncBJ1foo%2BgdDzbSeRakwtyoubsQ4pVa00%2Bg0Dy%2BROeoLLkDFFfgAsHcGHr7at%2FwAaRv236RGJTk7ZLCVai69KWwsi6ll3NHRqfujP482X6CGxFyvsaqcukdjQlOmJSyIDv7p4c6jcha3%2FCwoLrGOcYxWq3ZLnmWrFNemQacc58ENXUMGWicuDu%2B%2Fe%2Fq96xBq79DSh4cFDIAD%2BtzF%2Bh4ficvlCHZBsQLR8nvZPjd13mamMusGPGDq%2Fd105O4FjxPxQ%2F9B6kg2lkCm1VCb4ybOY6gSqbOo0xUyQMYdaQtBv%2FX9Aahv%2F5KWRl%2FT8%2BeIcxNRYi00wr7mV3OYU3IIYksJa5NsBaeDfeAY08FMLu5%2FbwGOqUBuwIkBhx8nwmPzHieobgbzlypVwaAvVm7A9FZAuOKFRzUwkiESA6MwwDlpcJVmaVT5J53moJK4Hj%2BgJEHd7G2EDxYbgFIG5IuIXupDYvS71vsT7pv2YjDxQH%2BprMyfdzke9f90HD70cfR8vTwbu087GLEHdZQc3cHvjwbnafme7c80ny74OzDMn8S2wa2ELBsfDqRfJSAY%2BMg5bJ%2BpchA4OtS9pwx&X-Amz-Signature=963e465f00cd0872298d6d308a458d3ce0007baef19545c5112bd19559da3aaa&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHZ7PRVP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1h%2BHIHWtDRAgbjnOaPOPr6Hz%2Bu7OJn3pjwjUlQNSI0gIhAPhqd4nzfEiUxeKIf9dUxkKN33HPRS%2BhPYH5qG3vVD5QKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2FpDnHHOmJaIjM66kq3APTLWMEmRiMVlgwAee%2BXq80fU33hDZR%2FNygIReEfoCuGJWEKjlzyvwoSQB4FTehgNhgNPpRoE4vD5XkP2usYC%2Bjw552vRRvPnLKTca6n9L8BpyIBs%2Burt7UecCl%2F99FbpIHcR1c7dcSdDj0Zx%2B%2FqzSjdQS5W5SFouam5cm3kacVrv2Wf2Og%2FDU6OF3AIhuvEYkj5%2FdOsBOsK08BwmP%2B3vGyueIf9zJBo47irmrF41tw6yVu3gy95sEWeZw0HVnjt%2B425TQH1KZI9xND1wWqgw%2BELJo%2FHJWs4DNzInYsQZ4B%2FRj2ztrDWc5FNjDw%2FvH1szkFH6NhyKnBiRap6hNCyv3CQY36%2F%2FYmwa7%2BwUQ1A0%2Blk0pvwheW%2BDGBS9SHKdIzJsdBpLLlc2PQnrB1dMHcKgK%2FrJp%2BlpVYoZ%2FE4oWdrHfYeE88KjAvNXzWvVYZjedLg2h9oHOrw7xC7eJ0sgxKYpEKkSLbxDEsnQc1kL%2F9C8hY7LHVhJ%2Ff7UaLe7thkTvBCXubftqcVlFoJoyi1tfP%2FuDnya3PV7DoMMfqFFFitZVNfpTCcZ%2FEuqG4%2Bt6X%2F9BFLIQvO1i%2FtlvObehvYujBKARY2XzsguXFD%2BWdHA4cD1IekDCtbLefCJWwpLoSRjCPv%2F28BjqkAePvKwiKP7BbK0l7UylkOJuQI8dV3mTI32ig921aPx%2B4VZBVX%2FKy0FNbk7le1hKLomNexlaYHD%2F75wDL52qyQTG7jL%2BaK6kid2Cofi9BEbUh26YA5AzYqrOoER7sL%2BalcOPwnqb0Pk0AqhkUsX%2Fr%2FspicwSXg%2FF%2BRJbn3OXC%2BxSkwdNkzZWCi17e16cROdQ4TcAbWthJDsF9F6oJNiATNSNNuQ5M&X-Amz-Signature=c4f903a114e59fbce44ea8aebc44e9250b61b4e1eda35d932038e8cf60290723&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4CPWJZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2F4aIwso96zJ4IYB3MkQCkUxIMdQC7PYdkKz1Tr4L0VAiBSkwGLRvLxcOdrISNnbkG9rZXa5aYZr%2FteAuA7qGUKTSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHzfFFDjswSuAz88KtwDIiyQbSH4Xo2s4neayo%2FbxK%2Fyf%2BRdWNYpL9oMgKBxb6XhbJ3KdYzgR1nlKK4F3ygkEydUTWduYqjzi4o%2BQpsNec3Hbp0h7ki%2Bb7YgsxjIy9mu3LfatOWlhBDd6M1aJEChRTd5GG4Ik8UyK2wua%2BBBHU%2FwUkx5CTBzyAv%2BHFEMXV1CI5P%2FovfHxXJW6W6hAcEKif9JBwB9spSoQfU3etCVLTaPj%2BSp7Dm%2BqcaJlxxyg5Mb8wGumrHkd8ONSRQTjSkuKmGsBwDS%2FghN3Rrfbjm7l7eHXGETGdEXrmZg%2F7HVjJtOQDq4SYF4FvxMEpXb0t750Ut20JMk2lxzPMA6XKQxf9aWziOSAKDk8EAjK8MAiCnqN1DOiS5smeVUinD4iOofyPe9GU8ZMCsxIfwDhQ2BFdnxhBvQT2cPpPYRYoB%2BlVyWD1zySc81M7NBfEw%2FNQo1BEXAQLgHzVOz45rtouYGnNGlFFvPcP4YSSZNOCtF2Dk1JtmNsplHoGXuznLYJEpdLcWFvWSmqDtwUofHIh8Wde0fLze061HajXhp2OUMcpWNTGf%2BV4fippyT3h0SONlpaGlkT78fZVqeTeqN0OJdkpsPVfqgtDMMeaQtm7ON3qPj%2Bqi2xbWnzPkcBcww87r9vAY6pgGqMviZQmzyQaoyKOK%2Fl%2FkJ41xnpv0HbJQbNDnID6IIYyz1Odnt%2Fg5wV5FsuiVuuZZ25ild%2FHg3YukmXTuqlK8D2d%2FdeFegnM1%2B1UGLf2EbYNOKaS7LdsnC17U0XngDOMtmjRtFMDjL49jpKBrDLE3nsoHQ%2F%2FmsntaCEfsN7WEY%2Fig8jMZxvwTnseCFaBjiAJpQQhSnjOveg80d9b0DGKEFoM7Cde1w&X-Amz-Signature=9fc2e0a3b2463f594718220821f417a7efce6499cbd7f93916a7d8fb57f1ffd7&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KIAFUMU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8b6Iy6faPcRpxZS7wPZrz9csY3aY9iln%2FlCyAduPCqwIhAM9icwPTXqyZmUgv0%2B%2FKmU1k8cRLfcPLtr4N68IqdKfTKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgysJ44H7zFsgbmBAIoq3AMvUcve2KiaeR8tmRL2%2FcUyYlMNeOy2suJsnVak05kU%2FTrs2AU0A6ZKpuj5WevzOyT97s2tPAqC5PBhixu%2F5BhwAB5RGoa3Pi72sImBilfVBLVd66riJgl%2BQ7AlkW7lg7AwFexsVylL7LVHsFhcE8mULKrGw9B8Tv9Pyqb8ORCBnXUc3j5fugZGV%2FAeM86Eu4pt7JWcTQgdBGHefR4zLcbqZ48TdZLRQjvUpcYKiVQ5hVM6yh%2B8OicKSpbqZBQ7LeBtEZBaYisUZp%2FjEM%2BKBFjsrsNnjbxWRzpeqRS8%2B6WczKHfJsAX0mhWVuVceasHoPvohIMh9P3hmwSBbwW2vtP9o0cU5giOWEq%2FKBt6NT6nYHjhDckNhYR6DgefI%2Fn%2F5D8AVWxeEtxpFwS8k2ut73AnbWX3ruNBpE7zlfsfntQjInG8%2BOG1b6NUQbVSPA2%2BV5QyVLpRVMjnBJ%2F2HAdqAPKTjfgB%2FrEmxXbY39BOCOFwNlx%2FCH5NZMiNzCGe9w8UWnQW5UoK29qURrvPTY8VpiXR%2B%2FPqTkZh%2FHJ8dd3kc%2B3qkdUjm8%2BSesbBiquDyW5nCcTWV5Zf%2B9RFd%2BJ6dvmlUPqCwa2F9K%2Bs4ccXLI750qLw9OdBxOemv7TqOax7yjCEwf28BjqkAedb1PhLoEde39fGUcph%2B8akBKn%2FjflGJ1os0MjzWNtipBOc2uXVkzW6PW2HYWwZuz%2F6q6hYsOxNSeh5eX%2BxNFy0SvaZ1VGoFoweWh4KKFUYGUNk41yYRizk5rjIwNBrrpOn%2FQ7kC1Wjasrf4MoPUeP5qRpLJKQLYJKl2Y8WrEjbgDxQIejNkGv8EwG9GR%2BYDQgO7wgMep0z9UtJ8qDZGLPSDxDd&X-Amz-Signature=897f7d3c53e52668c83f33d4e4f2d5666be73b39799c383c65da9016060bced8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CJG2MW2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFvJuuUBasOjVkt57cv1hEcCd60p%2BTdnoED3xtKNxWSAAiEAtC3FDuvFr7DEas%2FLpWtcpdVtEZzgIjiQX85LwNytRJcqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBWsyxwn70V9QspmiCrcA0qOacPhhZ%2F5%2F08CqD9DvFoSiya2BO6QOSCrNp7VyAiSw9gVDpw7c9sUcugv6PWFsMPUfD8ZFXkP9eQ641eeozcf62b6Tx3jGG20YDw0VzHXp3WAWgD4nQTQN911y8u0W%2BVvMlSTiFky5sI3nk%2Fgme9oEew8lkBXF9DJi9DrCsOGYEzphSzuG3fPxwJKy8XkHQ6K0H116kecfmj8%2Bb3w%2FNf3Gd%2BDFo0auDT1jOtZWIbH%2BbVtNu2uWwj0utEcHq%2FRD8578PaN6J5fI4KmVddLLHUyLFFXa7HQzttkhfRBywaHiNG5EQm2SjRCZ9maJp8ilPbxnJbjQvKlwWZSeEoj0mC6bwbRyPCiYVr6j0uRDLHVcni431BT5So7JlSBOGApGlikyWUK%2BEPEZHrJ3O1bZ6%2BX6Avgz1GV0c%2BERXksYAUEkL4l7rKKk0armOKz9VnWr%2FNJYPEqUITfsqcdJ3KzoujDKrIdRy%2BEtd95w%2BkXkU0RRwaEZGA0pdJpCBH2h2imyj0Y64Ci20f%2BwCcNpTPjxvldDqMDstgQHD2Bf9kqLZO%2BIA4P5xkMDZIk0OaLW2q9rDtGTQXFl7x0JO%2FIPqiD1mFAkpuU2HxCpB2D4hUUj2ntYDaO1pi8ghnH6SdOMNy7%2FbwGOqUBs0GaVuhGTZG6B6fqAiA6rrNdu08rHsV08OCJeVl1G7Y1GRqQcoDBCho03JmddqIkQcvct9vkA52ObX0tDX7d%2Fp0q8N%2FG6QCyR%2BqWPTWjXybz1VWs20twbF0RA%2FLFgnzZXGj13IvZaqz2tVOsEIaLEjEN%2BK9Sagf3NCA6Zk7OdWSHoEx%2BmqfD3Oz0KWNkX2SNwdnsK4FWX1z10OVlon7Ax3aPliua&X-Amz-Signature=00b2f95415d78eb56c87c972a93cbeeb67e7bffdd9c0db6239b5420cf380a8ec&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CJG2MW2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFvJuuUBasOjVkt57cv1hEcCd60p%2BTdnoED3xtKNxWSAAiEAtC3FDuvFr7DEas%2FLpWtcpdVtEZzgIjiQX85LwNytRJcqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBWsyxwn70V9QspmiCrcA0qOacPhhZ%2F5%2F08CqD9DvFoSiya2BO6QOSCrNp7VyAiSw9gVDpw7c9sUcugv6PWFsMPUfD8ZFXkP9eQ641eeozcf62b6Tx3jGG20YDw0VzHXp3WAWgD4nQTQN911y8u0W%2BVvMlSTiFky5sI3nk%2Fgme9oEew8lkBXF9DJi9DrCsOGYEzphSzuG3fPxwJKy8XkHQ6K0H116kecfmj8%2Bb3w%2FNf3Gd%2BDFo0auDT1jOtZWIbH%2BbVtNu2uWwj0utEcHq%2FRD8578PaN6J5fI4KmVddLLHUyLFFXa7HQzttkhfRBywaHiNG5EQm2SjRCZ9maJp8ilPbxnJbjQvKlwWZSeEoj0mC6bwbRyPCiYVr6j0uRDLHVcni431BT5So7JlSBOGApGlikyWUK%2BEPEZHrJ3O1bZ6%2BX6Avgz1GV0c%2BERXksYAUEkL4l7rKKk0armOKz9VnWr%2FNJYPEqUITfsqcdJ3KzoujDKrIdRy%2BEtd95w%2BkXkU0RRwaEZGA0pdJpCBH2h2imyj0Y64Ci20f%2BwCcNpTPjxvldDqMDstgQHD2Bf9kqLZO%2BIA4P5xkMDZIk0OaLW2q9rDtGTQXFl7x0JO%2FIPqiD1mFAkpuU2HxCpB2D4hUUj2ntYDaO1pi8ghnH6SdOMNy7%2FbwGOqUBs0GaVuhGTZG6B6fqAiA6rrNdu08rHsV08OCJeVl1G7Y1GRqQcoDBCho03JmddqIkQcvct9vkA52ObX0tDX7d%2Fp0q8N%2FG6QCyR%2BqWPTWjXybz1VWs20twbF0RA%2FLFgnzZXGj13IvZaqz2tVOsEIaLEjEN%2BK9Sagf3NCA6Zk7OdWSHoEx%2BmqfD3Oz0KWNkX2SNwdnsK4FWX1z10OVlon7Ax3aPliua&X-Amz-Signature=37b5ad76ffc53e1a82a9cbd673e69cd6a665c7a65d573e0a4d68170ee29b4657&X-Amz-SignedHeaders=host&x-id=GetObject)

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
