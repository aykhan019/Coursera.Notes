

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BB663UP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIGirA%2B9%2FUy2fc5xgVobXO8rGTL%2BkFalS2y2Bn7E4PvoYAiEAlzxG2p7B%2Bivxy9kXkEH0e3LsINGFSAJU2xEIniMygnwq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDP4XRRQJaJL%2FKOLLHSrcAyqBwDvBYFxAXApWDpNn8JTNIOTiPRxUgtgpCjLZn9ABKBohd6ZSBXfFhzwMlMPiYje1vcJzb77N5h33Qxe1IqfW9EEhqdv3P8AK6%2FAJmInwlpWbpLOfPtFOwiEFmYLf66cwaVhrTSYvUiQNO%2FxUP4s4qcXzf2VCbnLpeYWJBZ29Ife87Hfwwq1F5z60FYlstXEhS1faUF5V%2B9YIZxk7gRelosJDgDfHxvSEry2UyR7tuyKq2nC8agnCy2rX8FybvwkcR1wLlloizPAeoc9Nq%2FFPTpm%2ByprsxmizJXJ7SKcYo4XgmJkZI5dFO0T7o1dr%2FwiMyn4yMaGM%2BltqrwiLcnzkOFZa8E9Wyy4hdSX9tmqi5pCdhiIU4ApE0AcUFoeFoVNoPcC5KbnrEJcm4twegROdjZlv3zSY8XHitf7rDQ5lAHhkpnBKHqcKesX3ItfSMCa93vSmNzGgB4nTmqFWB7Z6Fkwj42wCxpNiYzacLYUcvOHlKemuqGYx3kNE%2FH9J1eUGk7yGYr4QdbYfV%2FnNT1jg9HG%2ByE%2BFcajppOUCZPNnr9y6AfSYSNFe651fsWekxWeaN9XcZgciYa09et5m6uFcDBXeKYNLB8XrAE2DmyNPUqFLOzVWntsCGhwJMP6BiL0GOqUBkI94rfZuwMxMOZKzFs%2BOg03uHtRQeXxy%2FNrc2Po3rqSnMfA5rbZ%2BUw4ov8KlSILBPoxtfNZYn%2BP9sZqcbnhZ5tITDmMVq3WMGxI%2Fy41Mnrkx%2BOq4uwYIkjbk93rcx8UyzlPraxGiykodvDRYxylacITtRygPcp86TOKZ0LP3b%2BUWAVZ%2BNQfH6a53mNJtY7WeYHs8CO83XAPxRIj3UrDwrk%2BP%2FuRG&X-Amz-Signature=8a9696f30c2d475517b2ecd41a58302e8c1bd03fe239f76a5321e0a4641c8346&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BB663UP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIGirA%2B9%2FUy2fc5xgVobXO8rGTL%2BkFalS2y2Bn7E4PvoYAiEAlzxG2p7B%2Bivxy9kXkEH0e3LsINGFSAJU2xEIniMygnwq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDP4XRRQJaJL%2FKOLLHSrcAyqBwDvBYFxAXApWDpNn8JTNIOTiPRxUgtgpCjLZn9ABKBohd6ZSBXfFhzwMlMPiYje1vcJzb77N5h33Qxe1IqfW9EEhqdv3P8AK6%2FAJmInwlpWbpLOfPtFOwiEFmYLf66cwaVhrTSYvUiQNO%2FxUP4s4qcXzf2VCbnLpeYWJBZ29Ife87Hfwwq1F5z60FYlstXEhS1faUF5V%2B9YIZxk7gRelosJDgDfHxvSEry2UyR7tuyKq2nC8agnCy2rX8FybvwkcR1wLlloizPAeoc9Nq%2FFPTpm%2ByprsxmizJXJ7SKcYo4XgmJkZI5dFO0T7o1dr%2FwiMyn4yMaGM%2BltqrwiLcnzkOFZa8E9Wyy4hdSX9tmqi5pCdhiIU4ApE0AcUFoeFoVNoPcC5KbnrEJcm4twegROdjZlv3zSY8XHitf7rDQ5lAHhkpnBKHqcKesX3ItfSMCa93vSmNzGgB4nTmqFWB7Z6Fkwj42wCxpNiYzacLYUcvOHlKemuqGYx3kNE%2FH9J1eUGk7yGYr4QdbYfV%2FnNT1jg9HG%2ByE%2BFcajppOUCZPNnr9y6AfSYSNFe651fsWekxWeaN9XcZgciYa09et5m6uFcDBXeKYNLB8XrAE2DmyNPUqFLOzVWntsCGhwJMP6BiL0GOqUBkI94rfZuwMxMOZKzFs%2BOg03uHtRQeXxy%2FNrc2Po3rqSnMfA5rbZ%2BUw4ov8KlSILBPoxtfNZYn%2BP9sZqcbnhZ5tITDmMVq3WMGxI%2Fy41Mnrkx%2BOq4uwYIkjbk93rcx8UyzlPraxGiykodvDRYxylacITtRygPcp86TOKZ0LP3b%2BUWAVZ%2BNQfH6a53mNJtY7WeYHs8CO83XAPxRIj3UrDwrk%2BP%2FuRG&X-Amz-Signature=0321ef7adfea8bfd28dba666449945070c468867e8ac966e70c2c5e0d3ca2721&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BB663UP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIGirA%2B9%2FUy2fc5xgVobXO8rGTL%2BkFalS2y2Bn7E4PvoYAiEAlzxG2p7B%2Bivxy9kXkEH0e3LsINGFSAJU2xEIniMygnwq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDP4XRRQJaJL%2FKOLLHSrcAyqBwDvBYFxAXApWDpNn8JTNIOTiPRxUgtgpCjLZn9ABKBohd6ZSBXfFhzwMlMPiYje1vcJzb77N5h33Qxe1IqfW9EEhqdv3P8AK6%2FAJmInwlpWbpLOfPtFOwiEFmYLf66cwaVhrTSYvUiQNO%2FxUP4s4qcXzf2VCbnLpeYWJBZ29Ife87Hfwwq1F5z60FYlstXEhS1faUF5V%2B9YIZxk7gRelosJDgDfHxvSEry2UyR7tuyKq2nC8agnCy2rX8FybvwkcR1wLlloizPAeoc9Nq%2FFPTpm%2ByprsxmizJXJ7SKcYo4XgmJkZI5dFO0T7o1dr%2FwiMyn4yMaGM%2BltqrwiLcnzkOFZa8E9Wyy4hdSX9tmqi5pCdhiIU4ApE0AcUFoeFoVNoPcC5KbnrEJcm4twegROdjZlv3zSY8XHitf7rDQ5lAHhkpnBKHqcKesX3ItfSMCa93vSmNzGgB4nTmqFWB7Z6Fkwj42wCxpNiYzacLYUcvOHlKemuqGYx3kNE%2FH9J1eUGk7yGYr4QdbYfV%2FnNT1jg9HG%2ByE%2BFcajppOUCZPNnr9y6AfSYSNFe651fsWekxWeaN9XcZgciYa09et5m6uFcDBXeKYNLB8XrAE2DmyNPUqFLOzVWntsCGhwJMP6BiL0GOqUBkI94rfZuwMxMOZKzFs%2BOg03uHtRQeXxy%2FNrc2Po3rqSnMfA5rbZ%2BUw4ov8KlSILBPoxtfNZYn%2BP9sZqcbnhZ5tITDmMVq3WMGxI%2Fy41Mnrkx%2BOq4uwYIkjbk93rcx8UyzlPraxGiykodvDRYxylacITtRygPcp86TOKZ0LP3b%2BUWAVZ%2BNQfH6a53mNJtY7WeYHs8CO83XAPxRIj3UrDwrk%2BP%2FuRG&X-Amz-Signature=35d0af7287c4461b7425fcacafb61959d47914e87fa57e47a898377369c62f11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C45UB2N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDN0CrL%2F6XCPXLLcsVyQ4fj5pjgGLJDtagQpflLrXIy4wIhAKudmd3O2T1rq%2BJOT0d1x3r0Yb0zyNJiLOMScfJ%2FK5tIKv8DCC0QABoMNjM3NDIzMTgzODA1Igw6epMi4Ce2bRfsN9Qq3AOffhCdxXaaXFl%2FYOxEGwLcUt292XYgb%2B2z4QNf6KQUdRrQybPXwiHPtiDst%2BaPJwgLvXBElcaC8PGJo4d4gBH8Y6Upy2qvKmvlsCEPPHFs%2F5ZZvlhy35lC%2F5R8RjeQjR0JFjbek%2BLLuXISegIcT4cMUX3BeXNQpd%2FJU%2F3G%2F3nuafBxppYrJuViBLMrwhJ%2FxAVd1DFV%2F%2Fwn3X6vuVkYftYHWZen%2BvrMeh1vridMaL9R4aO3DXIjDTVD0EScXKIAJOvJnixl5PsFK2U0iYw3hwho2YhEVpfQxSTFxMQk%2FAEu2148V4HvAUpyEgYtlt8%2FddBKZV4d8gB99VMDlOHiWUcD1mqOWuYj2kuCj4LlVMjxFSe8XlvfOT9szICp2b3V2jg9rCdg2TndguNrcGjbnLvcoTzXWf57e8EoNvEahw9ZlurizCPGM1vTwHgLiXXG4sHRbj98trIWFGRbTgiNdTQ%2FNCqQQYTgPEJGfKX1Y46to1sITRwr3fO4CASj%2BItKqQKR57JXrt%2BRBsnjAGTLV5fMIP4nkOIHeNjYh%2FA4wVPt0Rr5aafFEFweVi%2FCjIyHG%2BDGvG0eKnpfGRs8FOGYwDQDS6XhK2dkVTi3Cu%2Fa0lYdNWIxFBZ01vwU2FhwWTCagoi9BjqkAdRXFva8jZHt%2BXo0aFMh2w2hByro%2FQASh0aav%2FKxsuhnnkdaDKvsrxgVM1TTVUdu88fK9nkz7n2JqGNVGutqFxi1%2BrdR8S6bjLBsLY4JXbrJk0G8hrtxZG671i6GLijdK26Hfvjlh0qOZmJNxkofE7hVBn5E4krUep8OGiaznElmPMJXu9zWgtT%2F2p8vQ7RNzo%2FhLEbVIVuoVI1Ntd6OJm85w3hK&X-Amz-Signature=44a6e5c93ead9a65dd73e7cbb747bd86581ba5e85c799b00289084c350b809ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C45UB2N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDN0CrL%2F6XCPXLLcsVyQ4fj5pjgGLJDtagQpflLrXIy4wIhAKudmd3O2T1rq%2BJOT0d1x3r0Yb0zyNJiLOMScfJ%2FK5tIKv8DCC0QABoMNjM3NDIzMTgzODA1Igw6epMi4Ce2bRfsN9Qq3AOffhCdxXaaXFl%2FYOxEGwLcUt292XYgb%2B2z4QNf6KQUdRrQybPXwiHPtiDst%2BaPJwgLvXBElcaC8PGJo4d4gBH8Y6Upy2qvKmvlsCEPPHFs%2F5ZZvlhy35lC%2F5R8RjeQjR0JFjbek%2BLLuXISegIcT4cMUX3BeXNQpd%2FJU%2F3G%2F3nuafBxppYrJuViBLMrwhJ%2FxAVd1DFV%2F%2Fwn3X6vuVkYftYHWZen%2BvrMeh1vridMaL9R4aO3DXIjDTVD0EScXKIAJOvJnixl5PsFK2U0iYw3hwho2YhEVpfQxSTFxMQk%2FAEu2148V4HvAUpyEgYtlt8%2FddBKZV4d8gB99VMDlOHiWUcD1mqOWuYj2kuCj4LlVMjxFSe8XlvfOT9szICp2b3V2jg9rCdg2TndguNrcGjbnLvcoTzXWf57e8EoNvEahw9ZlurizCPGM1vTwHgLiXXG4sHRbj98trIWFGRbTgiNdTQ%2FNCqQQYTgPEJGfKX1Y46to1sITRwr3fO4CASj%2BItKqQKR57JXrt%2BRBsnjAGTLV5fMIP4nkOIHeNjYh%2FA4wVPt0Rr5aafFEFweVi%2FCjIyHG%2BDGvG0eKnpfGRs8FOGYwDQDS6XhK2dkVTi3Cu%2Fa0lYdNWIxFBZ01vwU2FhwWTCagoi9BjqkAdRXFva8jZHt%2BXo0aFMh2w2hByro%2FQASh0aav%2FKxsuhnnkdaDKvsrxgVM1TTVUdu88fK9nkz7n2JqGNVGutqFxi1%2BrdR8S6bjLBsLY4JXbrJk0G8hrtxZG671i6GLijdK26Hfvjlh0qOZmJNxkofE7hVBn5E4krUep8OGiaznElmPMJXu9zWgtT%2F2p8vQ7RNzo%2FhLEbVIVuoVI1Ntd6OJm85w3hK&X-Amz-Signature=ad97759cf36afa8a3825291c507b0ae7a76e8ac8ca5c759f2442ea8314c5f873&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C45UB2N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDN0CrL%2F6XCPXLLcsVyQ4fj5pjgGLJDtagQpflLrXIy4wIhAKudmd3O2T1rq%2BJOT0d1x3r0Yb0zyNJiLOMScfJ%2FK5tIKv8DCC0QABoMNjM3NDIzMTgzODA1Igw6epMi4Ce2bRfsN9Qq3AOffhCdxXaaXFl%2FYOxEGwLcUt292XYgb%2B2z4QNf6KQUdRrQybPXwiHPtiDst%2BaPJwgLvXBElcaC8PGJo4d4gBH8Y6Upy2qvKmvlsCEPPHFs%2F5ZZvlhy35lC%2F5R8RjeQjR0JFjbek%2BLLuXISegIcT4cMUX3BeXNQpd%2FJU%2F3G%2F3nuafBxppYrJuViBLMrwhJ%2FxAVd1DFV%2F%2Fwn3X6vuVkYftYHWZen%2BvrMeh1vridMaL9R4aO3DXIjDTVD0EScXKIAJOvJnixl5PsFK2U0iYw3hwho2YhEVpfQxSTFxMQk%2FAEu2148V4HvAUpyEgYtlt8%2FddBKZV4d8gB99VMDlOHiWUcD1mqOWuYj2kuCj4LlVMjxFSe8XlvfOT9szICp2b3V2jg9rCdg2TndguNrcGjbnLvcoTzXWf57e8EoNvEahw9ZlurizCPGM1vTwHgLiXXG4sHRbj98trIWFGRbTgiNdTQ%2FNCqQQYTgPEJGfKX1Y46to1sITRwr3fO4CASj%2BItKqQKR57JXrt%2BRBsnjAGTLV5fMIP4nkOIHeNjYh%2FA4wVPt0Rr5aafFEFweVi%2FCjIyHG%2BDGvG0eKnpfGRs8FOGYwDQDS6XhK2dkVTi3Cu%2Fa0lYdNWIxFBZ01vwU2FhwWTCagoi9BjqkAdRXFva8jZHt%2BXo0aFMh2w2hByro%2FQASh0aav%2FKxsuhnnkdaDKvsrxgVM1TTVUdu88fK9nkz7n2JqGNVGutqFxi1%2BrdR8S6bjLBsLY4JXbrJk0G8hrtxZG671i6GLijdK26Hfvjlh0qOZmJNxkofE7hVBn5E4krUep8OGiaznElmPMJXu9zWgtT%2F2p8vQ7RNzo%2FhLEbVIVuoVI1Ntd6OJm85w3hK&X-Amz-Signature=5b061aebe43a721a99a9104552691b5a00d568891e824e7a711b4f530d521d2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C45UB2N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDN0CrL%2F6XCPXLLcsVyQ4fj5pjgGLJDtagQpflLrXIy4wIhAKudmd3O2T1rq%2BJOT0d1x3r0Yb0zyNJiLOMScfJ%2FK5tIKv8DCC0QABoMNjM3NDIzMTgzODA1Igw6epMi4Ce2bRfsN9Qq3AOffhCdxXaaXFl%2FYOxEGwLcUt292XYgb%2B2z4QNf6KQUdRrQybPXwiHPtiDst%2BaPJwgLvXBElcaC8PGJo4d4gBH8Y6Upy2qvKmvlsCEPPHFs%2F5ZZvlhy35lC%2F5R8RjeQjR0JFjbek%2BLLuXISegIcT4cMUX3BeXNQpd%2FJU%2F3G%2F3nuafBxppYrJuViBLMrwhJ%2FxAVd1DFV%2F%2Fwn3X6vuVkYftYHWZen%2BvrMeh1vridMaL9R4aO3DXIjDTVD0EScXKIAJOvJnixl5PsFK2U0iYw3hwho2YhEVpfQxSTFxMQk%2FAEu2148V4HvAUpyEgYtlt8%2FddBKZV4d8gB99VMDlOHiWUcD1mqOWuYj2kuCj4LlVMjxFSe8XlvfOT9szICp2b3V2jg9rCdg2TndguNrcGjbnLvcoTzXWf57e8EoNvEahw9ZlurizCPGM1vTwHgLiXXG4sHRbj98trIWFGRbTgiNdTQ%2FNCqQQYTgPEJGfKX1Y46to1sITRwr3fO4CASj%2BItKqQKR57JXrt%2BRBsnjAGTLV5fMIP4nkOIHeNjYh%2FA4wVPt0Rr5aafFEFweVi%2FCjIyHG%2BDGvG0eKnpfGRs8FOGYwDQDS6XhK2dkVTi3Cu%2Fa0lYdNWIxFBZ01vwU2FhwWTCagoi9BjqkAdRXFva8jZHt%2BXo0aFMh2w2hByro%2FQASh0aav%2FKxsuhnnkdaDKvsrxgVM1TTVUdu88fK9nkz7n2JqGNVGutqFxi1%2BrdR8S6bjLBsLY4JXbrJk0G8hrtxZG671i6GLijdK26Hfvjlh0qOZmJNxkofE7hVBn5E4krUep8OGiaznElmPMJXu9zWgtT%2F2p8vQ7RNzo%2FhLEbVIVuoVI1Ntd6OJm85w3hK&X-Amz-Signature=6a002a00c3bcfa98b38ae681472547b72bd3824b9d3b84aafe434d2b8d1d8d48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C45UB2N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDN0CrL%2F6XCPXLLcsVyQ4fj5pjgGLJDtagQpflLrXIy4wIhAKudmd3O2T1rq%2BJOT0d1x3r0Yb0zyNJiLOMScfJ%2FK5tIKv8DCC0QABoMNjM3NDIzMTgzODA1Igw6epMi4Ce2bRfsN9Qq3AOffhCdxXaaXFl%2FYOxEGwLcUt292XYgb%2B2z4QNf6KQUdRrQybPXwiHPtiDst%2BaPJwgLvXBElcaC8PGJo4d4gBH8Y6Upy2qvKmvlsCEPPHFs%2F5ZZvlhy35lC%2F5R8RjeQjR0JFjbek%2BLLuXISegIcT4cMUX3BeXNQpd%2FJU%2F3G%2F3nuafBxppYrJuViBLMrwhJ%2FxAVd1DFV%2F%2Fwn3X6vuVkYftYHWZen%2BvrMeh1vridMaL9R4aO3DXIjDTVD0EScXKIAJOvJnixl5PsFK2U0iYw3hwho2YhEVpfQxSTFxMQk%2FAEu2148V4HvAUpyEgYtlt8%2FddBKZV4d8gB99VMDlOHiWUcD1mqOWuYj2kuCj4LlVMjxFSe8XlvfOT9szICp2b3V2jg9rCdg2TndguNrcGjbnLvcoTzXWf57e8EoNvEahw9ZlurizCPGM1vTwHgLiXXG4sHRbj98trIWFGRbTgiNdTQ%2FNCqQQYTgPEJGfKX1Y46to1sITRwr3fO4CASj%2BItKqQKR57JXrt%2BRBsnjAGTLV5fMIP4nkOIHeNjYh%2FA4wVPt0Rr5aafFEFweVi%2FCjIyHG%2BDGvG0eKnpfGRs8FOGYwDQDS6XhK2dkVTi3Cu%2Fa0lYdNWIxFBZ01vwU2FhwWTCagoi9BjqkAdRXFva8jZHt%2BXo0aFMh2w2hByro%2FQASh0aav%2FKxsuhnnkdaDKvsrxgVM1TTVUdu88fK9nkz7n2JqGNVGutqFxi1%2BrdR8S6bjLBsLY4JXbrJk0G8hrtxZG671i6GLijdK26Hfvjlh0qOZmJNxkofE7hVBn5E4krUep8OGiaznElmPMJXu9zWgtT%2F2p8vQ7RNzo%2FhLEbVIVuoVI1Ntd6OJm85w3hK&X-Amz-Signature=47e13e25debd136c313f1a51c551e98ddec059f8a86ba1ddad0447f0655a5e7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C45UB2N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDN0CrL%2F6XCPXLLcsVyQ4fj5pjgGLJDtagQpflLrXIy4wIhAKudmd3O2T1rq%2BJOT0d1x3r0Yb0zyNJiLOMScfJ%2FK5tIKv8DCC0QABoMNjM3NDIzMTgzODA1Igw6epMi4Ce2bRfsN9Qq3AOffhCdxXaaXFl%2FYOxEGwLcUt292XYgb%2B2z4QNf6KQUdRrQybPXwiHPtiDst%2BaPJwgLvXBElcaC8PGJo4d4gBH8Y6Upy2qvKmvlsCEPPHFs%2F5ZZvlhy35lC%2F5R8RjeQjR0JFjbek%2BLLuXISegIcT4cMUX3BeXNQpd%2FJU%2F3G%2F3nuafBxppYrJuViBLMrwhJ%2FxAVd1DFV%2F%2Fwn3X6vuVkYftYHWZen%2BvrMeh1vridMaL9R4aO3DXIjDTVD0EScXKIAJOvJnixl5PsFK2U0iYw3hwho2YhEVpfQxSTFxMQk%2FAEu2148V4HvAUpyEgYtlt8%2FddBKZV4d8gB99VMDlOHiWUcD1mqOWuYj2kuCj4LlVMjxFSe8XlvfOT9szICp2b3V2jg9rCdg2TndguNrcGjbnLvcoTzXWf57e8EoNvEahw9ZlurizCPGM1vTwHgLiXXG4sHRbj98trIWFGRbTgiNdTQ%2FNCqQQYTgPEJGfKX1Y46to1sITRwr3fO4CASj%2BItKqQKR57JXrt%2BRBsnjAGTLV5fMIP4nkOIHeNjYh%2FA4wVPt0Rr5aafFEFweVi%2FCjIyHG%2BDGvG0eKnpfGRs8FOGYwDQDS6XhK2dkVTi3Cu%2Fa0lYdNWIxFBZ01vwU2FhwWTCagoi9BjqkAdRXFva8jZHt%2BXo0aFMh2w2hByro%2FQASh0aav%2FKxsuhnnkdaDKvsrxgVM1TTVUdu88fK9nkz7n2JqGNVGutqFxi1%2BrdR8S6bjLBsLY4JXbrJk0G8hrtxZG671i6GLijdK26Hfvjlh0qOZmJNxkofE7hVBn5E4krUep8OGiaznElmPMJXu9zWgtT%2F2p8vQ7RNzo%2FhLEbVIVuoVI1Ntd6OJm85w3hK&X-Amz-Signature=fd4da0ba9af7316a871d3bb03e9d7dfbcc96ec4359b8628db970809f21139494&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7LVKOFD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIF4aj0OAlH6WK9UAvyMzRFLMuEQ3tpXemDI5aa661%2FgeAiEA5oaQnH7VV7DR3R4YgZQC%2FAel5ADWg3vMYT2qJ7gVXBIq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDJy0LYNSAWroIn1KbircA8XtuYdMEsskotLi5NckokNXhy83y8tN5YLLU4FLyg8Ei%2BJ6Aiixakc1CmDjYAmW1EVcXOpWou0rMarHpJJwnWu7XXNVZP8DuP7W4SCfxQlx2mcWMpmrFAu7OYAzsrGuqRvMlfzi%2FtfEZ%2FOkr1OY78HiZsYUnl00NHZCjSI4MsVNnaeD0lZl56tzuuA4Sv0%2BekE0HZ%2FKSrj%2BlG9I5YWssiEkOPrboi3WYC9mSIGce7Xw08pGEmRQhmj2jDeYWs2Le%2BuOIb4MfwlPwrfUZvMjG1J6yrxtOdBixXCyVlUzT4bOejLj6BYLFV2tVE9N7ZSGAT0DPNHQ9CTctJELEv1aYBq2uGzhsJD1loMt7WCXAU7ARfBS4NadgsKn5pngsA9dvcp%2BPf47NrS9udymsr4Dyijkr%2BB819nTPQrriQsBiELSMO5cKP0qqHWtf8%2FZrz8zSZ%2Blcznsvv2PSA1WnUOsGJeD29n9Q%2BFUddB4GzpClhA7kUFKqfmyWQQ3lFY7%2FSn9TJTPotWa64UvCr28dg4Kr5G2j35Dii1kBbz0SED88KOmE5vITuGuEV0gwaGcWi4wjFeLEuCdKccVmLHs%2BcTEQ1WffZxqO99bqNyOC6f9zsZ7txfT0jc%2FmeSUD1pzMOqBiL0GOqUBjJa9%2F1vUpgtgp8kGSgAb%2Fae3wpViANX016zrv2B8eVxxxlQmqXvtELlyj%2FngzdgxgNPLa%2B%2Bv6aqb0BezcjeC2CqtGk7hSwWaAQhOpm0X5907tqqBNXqlGgUx4Ak9G0AjJgPMmDhLbMRMoyDG4sqeiz4agUkPMb6mrJizyIxygcryCgu9%2F9SKrM0eSzayp%2BlEC13XmqIC5%2F%2Fzjv7qGs0nF%2BDJnV2N&X-Amz-Signature=c86abae8538c5075d72f44b5f57ef0538ac672f9f1a2a46bc29bc748144a8aff&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLERC7L4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIA6LzYDaHKyP7tG7KqqD7AWhIoRAS6yww3qVIvUQCRVVAiEA%2BFJQCjhGwJ88v5UA9us3t6IXNzH3LpztDmDgxBmwIhwq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDCd6cY6uJ00KchIpjSrcA4h7qzHfLBgFzbyOuYvYk5Rf6%2BVDrK69RRIEKrKUmFa4kilkBPdVeyt0appqCmnDtJFn3qtGPtD6fIZwOKAS0o5l2rsKFm%2Fy5QJw7klY%2BGh3MCnMrbNpPMXG19tttZnktmtbaEzzPUQO2l98v48L029nXcSBSAiCivbPd%2FWe5GlQa1%2F096i4y2Muy2olWsUtOvcszu6eYwgMZezhLsgucO6r2bBA3x%2FM0zLhSAsCb8nwAiX0DaqbNQ2v6fpTyaRw96aHFf7Gz8egvkPOUJK7VpGeSt3yaMCChLDsXWeURXJvtvBdtCPZXJX8gFPHrFO8PRpw3WSgJfZSn%2BbX90kLSV%2FAblE0wJb2GoJF4%2F%2F0E65axn1swUzwMBAKdUwFVVE2%2F7I6Mn%2ByvFwLJxZ6fUFS0PR6mLZFNh%2FI0W%2BbuLsBmE9WgNF0QR%2FUpHMqim7iUfIUvnnAXU3DUnnbF6DAGAqEkLA1YSRuv4FZz9DqWth31eGbmQIaZk6MZyFnha7gn4QivYNCYehICOmN0OnVH%2BLFdUyMcHgO6DCKYElaKUyFeagG%2F1gQEoAt2FzPTU3Jys2aOouI3XzIv%2FUIESZRW6RQPWDmSl46uUvrb4sxf%2BtwcwAetNgxg3CWlQT0Y3NdMIeCiL0GOqUB4XZEZTPx%2BlHmvoPXL5qQjgNtqdBVYzFOsZsu5mZMVmhbfqcYmqUr8UlGBy4mfq1XDBLJlSQrBWA2Ny2q2Bn5daNSyt6h97k3GFp0mDT%2F%2BEOiFmL1CtWoL%2F3xcIZbnwv2PHYO%2FIkbiQpXq6gldxXwLT2KPFno4D9OYtbll%2FH%2FqxQZI9NTOBPE6WdTpQG%2BtDYh6DilOoCq26L7z6lArcwS%2F8IcVpv4&X-Amz-Signature=a4e72a9cb0bda7752ec14d9c8945c17d479c4306654e6b0631e1a80eaa5d4c8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C45UB2N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDN0CrL%2F6XCPXLLcsVyQ4fj5pjgGLJDtagQpflLrXIy4wIhAKudmd3O2T1rq%2BJOT0d1x3r0Yb0zyNJiLOMScfJ%2FK5tIKv8DCC0QABoMNjM3NDIzMTgzODA1Igw6epMi4Ce2bRfsN9Qq3AOffhCdxXaaXFl%2FYOxEGwLcUt292XYgb%2B2z4QNf6KQUdRrQybPXwiHPtiDst%2BaPJwgLvXBElcaC8PGJo4d4gBH8Y6Upy2qvKmvlsCEPPHFs%2F5ZZvlhy35lC%2F5R8RjeQjR0JFjbek%2BLLuXISegIcT4cMUX3BeXNQpd%2FJU%2F3G%2F3nuafBxppYrJuViBLMrwhJ%2FxAVd1DFV%2F%2Fwn3X6vuVkYftYHWZen%2BvrMeh1vridMaL9R4aO3DXIjDTVD0EScXKIAJOvJnixl5PsFK2U0iYw3hwho2YhEVpfQxSTFxMQk%2FAEu2148V4HvAUpyEgYtlt8%2FddBKZV4d8gB99VMDlOHiWUcD1mqOWuYj2kuCj4LlVMjxFSe8XlvfOT9szICp2b3V2jg9rCdg2TndguNrcGjbnLvcoTzXWf57e8EoNvEahw9ZlurizCPGM1vTwHgLiXXG4sHRbj98trIWFGRbTgiNdTQ%2FNCqQQYTgPEJGfKX1Y46to1sITRwr3fO4CASj%2BItKqQKR57JXrt%2BRBsnjAGTLV5fMIP4nkOIHeNjYh%2FA4wVPt0Rr5aafFEFweVi%2FCjIyHG%2BDGvG0eKnpfGRs8FOGYwDQDS6XhK2dkVTi3Cu%2Fa0lYdNWIxFBZ01vwU2FhwWTCagoi9BjqkAdRXFva8jZHt%2BXo0aFMh2w2hByro%2FQASh0aav%2FKxsuhnnkdaDKvsrxgVM1TTVUdu88fK9nkz7n2JqGNVGutqFxi1%2BrdR8S6bjLBsLY4JXbrJk0G8hrtxZG671i6GLijdK26Hfvjlh0qOZmJNxkofE7hVBn5E4krUep8OGiaznElmPMJXu9zWgtT%2F2p8vQ7RNzo%2FhLEbVIVuoVI1Ntd6OJm85w3hK&X-Amz-Signature=f02383c7ac2a0ca2f4bc7caaf4cdac26786b43dc68938711a8b2287f5b5cdd74&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C45UB2N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDN0CrL%2F6XCPXLLcsVyQ4fj5pjgGLJDtagQpflLrXIy4wIhAKudmd3O2T1rq%2BJOT0d1x3r0Yb0zyNJiLOMScfJ%2FK5tIKv8DCC0QABoMNjM3NDIzMTgzODA1Igw6epMi4Ce2bRfsN9Qq3AOffhCdxXaaXFl%2FYOxEGwLcUt292XYgb%2B2z4QNf6KQUdRrQybPXwiHPtiDst%2BaPJwgLvXBElcaC8PGJo4d4gBH8Y6Upy2qvKmvlsCEPPHFs%2F5ZZvlhy35lC%2F5R8RjeQjR0JFjbek%2BLLuXISegIcT4cMUX3BeXNQpd%2FJU%2F3G%2F3nuafBxppYrJuViBLMrwhJ%2FxAVd1DFV%2F%2Fwn3X6vuVkYftYHWZen%2BvrMeh1vridMaL9R4aO3DXIjDTVD0EScXKIAJOvJnixl5PsFK2U0iYw3hwho2YhEVpfQxSTFxMQk%2FAEu2148V4HvAUpyEgYtlt8%2FddBKZV4d8gB99VMDlOHiWUcD1mqOWuYj2kuCj4LlVMjxFSe8XlvfOT9szICp2b3V2jg9rCdg2TndguNrcGjbnLvcoTzXWf57e8EoNvEahw9ZlurizCPGM1vTwHgLiXXG4sHRbj98trIWFGRbTgiNdTQ%2FNCqQQYTgPEJGfKX1Y46to1sITRwr3fO4CASj%2BItKqQKR57JXrt%2BRBsnjAGTLV5fMIP4nkOIHeNjYh%2FA4wVPt0Rr5aafFEFweVi%2FCjIyHG%2BDGvG0eKnpfGRs8FOGYwDQDS6XhK2dkVTi3Cu%2Fa0lYdNWIxFBZ01vwU2FhwWTCagoi9BjqkAdRXFva8jZHt%2BXo0aFMh2w2hByro%2FQASh0aav%2FKxsuhnnkdaDKvsrxgVM1TTVUdu88fK9nkz7n2JqGNVGutqFxi1%2BrdR8S6bjLBsLY4JXbrJk0G8hrtxZG671i6GLijdK26Hfvjlh0qOZmJNxkofE7hVBn5E4krUep8OGiaznElmPMJXu9zWgtT%2F2p8vQ7RNzo%2FhLEbVIVuoVI1Ntd6OJm85w3hK&X-Amz-Signature=3cbae70a212cfac45501dddfebfe3fd1d8078941fcb309d562e9f5c3969e5164&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C45UB2N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDN0CrL%2F6XCPXLLcsVyQ4fj5pjgGLJDtagQpflLrXIy4wIhAKudmd3O2T1rq%2BJOT0d1x3r0Yb0zyNJiLOMScfJ%2FK5tIKv8DCC0QABoMNjM3NDIzMTgzODA1Igw6epMi4Ce2bRfsN9Qq3AOffhCdxXaaXFl%2FYOxEGwLcUt292XYgb%2B2z4QNf6KQUdRrQybPXwiHPtiDst%2BaPJwgLvXBElcaC8PGJo4d4gBH8Y6Upy2qvKmvlsCEPPHFs%2F5ZZvlhy35lC%2F5R8RjeQjR0JFjbek%2BLLuXISegIcT4cMUX3BeXNQpd%2FJU%2F3G%2F3nuafBxppYrJuViBLMrwhJ%2FxAVd1DFV%2F%2Fwn3X6vuVkYftYHWZen%2BvrMeh1vridMaL9R4aO3DXIjDTVD0EScXKIAJOvJnixl5PsFK2U0iYw3hwho2YhEVpfQxSTFxMQk%2FAEu2148V4HvAUpyEgYtlt8%2FddBKZV4d8gB99VMDlOHiWUcD1mqOWuYj2kuCj4LlVMjxFSe8XlvfOT9szICp2b3V2jg9rCdg2TndguNrcGjbnLvcoTzXWf57e8EoNvEahw9ZlurizCPGM1vTwHgLiXXG4sHRbj98trIWFGRbTgiNdTQ%2FNCqQQYTgPEJGfKX1Y46to1sITRwr3fO4CASj%2BItKqQKR57JXrt%2BRBsnjAGTLV5fMIP4nkOIHeNjYh%2FA4wVPt0Rr5aafFEFweVi%2FCjIyHG%2BDGvG0eKnpfGRs8FOGYwDQDS6XhK2dkVTi3Cu%2Fa0lYdNWIxFBZ01vwU2FhwWTCagoi9BjqkAdRXFva8jZHt%2BXo0aFMh2w2hByro%2FQASh0aav%2FKxsuhnnkdaDKvsrxgVM1TTVUdu88fK9nkz7n2JqGNVGutqFxi1%2BrdR8S6bjLBsLY4JXbrJk0G8hrtxZG671i6GLijdK26Hfvjlh0qOZmJNxkofE7hVBn5E4krUep8OGiaznElmPMJXu9zWgtT%2F2p8vQ7RNzo%2FhLEbVIVuoVI1Ntd6OJm85w3hK&X-Amz-Signature=15d10cffdf760047911b3039d65d8d5f2d75073c5500b6728bf840ff0401028c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6TOJROY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCGdQ9kc8fKtGAUuaeAQNi6LFhNzZPCIA43ZXKR5KdTDwIgavcWIySDWCKn2egLgjhGmvjaxWQNPLHBzmehV4Eo9O8q%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDNqDlrHjlceiMQ38eSrcAwYjCKmmtqhjRLCRC0XdbzqXZShS6x8GWY9UWeRLg%2FWzltjbisPo9zCksgTYGBfSkywcW5dhCN4RvDJBGkcANVdkjFW1rQfVzIiaQfWPX96t47PnG%2B52o5uYIlFS286r0W1LkneauseaHGM6Ml1XoQl%2FtaOjCC%2FaeujAyc88xkG%2BZ1lxfTGq5oxgfxskpWh%2FpPdKBepdia5Y6j9S2CGiGMr6SmIrJzKfmQqxG%2B4m8qqTUe9VgqaPDhPrjHRES2OZX24Qdyek2GuZXDRkpLnNFFgVuJP6kQs51s7bpk3yxx32sGYQINsTfzeqLTVobmgQmwlbB4Cwpk5e%2FwrLVkS8%2FYx9MVH1cg8Jtd5lGVo3UUn6t0VP%2Fw6ShNk%2F%2B1%2F4sUizOPPIGULfAc8j%2FIgaZg5c%2FSOL%2BMFWPySRErqlcnoAfaK1oYv%2BWZApzNKIYlNWr8VM0MRNTlVNjNvhnGTvbQjQzJo6k4PzwlXseJ3ARlmbVRg3W8XhMsEaR%2FJOmOPH34VQAu5ofhezU3o3fFVI1C8%2BZrkamqCnaQXY7r%2B8b1FqZK5NTHzHAJUlCBXoht3yVif8FS9rmjrIjXq22w8OJNQG35wnxAVVYwKwTHKPHMt4%2FeK0rVHiQ%2FbxxdAa9MqZMIqCiL0GOqUBjsWzYkrP7zxJ2MQHvMhaxxw1hQ5FgH86S%2Bl%2FhM4PmnpqMfvnl4qr7qU09bhf3aV4CFYYtVBkil%2BwEhR67351H%2B72qs5WkNRE3CLmat4pQ1%2BH5a8%2FQ%2BmBoNYwgSJA3%2ByK34HtCRAJHw0rwIiHYxmKKW7xUvi0pMXrxxYIOBC8a%2BmF5Cv7lc6Y2mvPKLgEj%2BAlgT1ClIOlLD%2BxPJ3GihuxUtihoco7&X-Amz-Signature=2be1be118617d0b215df2f8830971c5bad8a448d99bb2e591490c04b4b6748aa&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBSW4UZG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQCvE4EaPi%2BuS9MaCLS2JtB%2FkDEAw1QveS1zx9nHi2KP5QIhAKLf7YrAfbNXa49VmDE%2FioQ8VnPbhuw%2BGR3qxBl5WN%2BDKv8DCC0QABoMNjM3NDIzMTgzODA1IgxGBHe%2BfDfH6HMscc8q3APuwibCiT3pVM0lj1OIVupswf3WmPbxRJibgBW00xjc72Uzqu7exc%2B7tKyl7SqItiwboiOwEjdhZLW2uCGLU73FOCmg7eBAXqJephgEzfRRAJieFejxHdrobJCBfwmtKWDpRN%2B8pKq8JybzojiYs%2BVZ%2FffL2uanGh7IBSI9%2BfF6QF3EkYfje0aXGWJIl24esf0rrcLscuaKeA%2FBvNs0EQs5hW1H92aSh9TtRLlKtBJm1cPqWDApEaThx2WuVChtwZwpbBkLg0mHU0y%2FF5ZQhhla%2BkEroLyHKbr8szy0JUWLogvAKRcMgxl4LrWANhc30qMs4P4x3zMywd3l4LUjpES7Z19IhrHmaGlhFLxdcEADv8WBuLrFTCAUyOb1s5jLgtn1jkOEORBODreLofPb4w5KWElz9kO8e%2F8FfqPDblUQECuOvRmbmkRSbQv5tHxZkBmfxjtZbbaulpCOMthKofImhyuIuCVOg%2FDrcfNT4o%2Bq0VRNwCgxd4Ux1ztvW6MSqC0dn0X3ZLrBC49Qb3K4xFfzea5w%2BeC8nDCiZCDr%2FqQ60pEntomRrgZ4XzC%2FcnafUMv9YQrCB6q5IL75w33eK7arr2viuk0AI4zRT3PXMpdv6e5v3r674U829P6IjTCngoi9BjqkAYhnuNb0lF2HQevgpQyZjLucjn4MFbWjgTAfmLPQX0aHkMMZZ9B1U9Xnj3iA1IN0sEjwhx%2FM2YAGoDHsyO2cp8rqv3ZeHYSFw8hPzsvC%2FGyDz%2Bl3SMiUxNvWI29ZX0C7kLNhLe8d8QdfoG9LSD5nSIvlg6KCHvRRtmUzxp1Y67IZTdBOiciIMrAXMLO6DbXjIyx8%2BaI4AVN%2Fsjgt%2Fo96oMPV16v8&X-Amz-Signature=4ce6d8a70841152bd412299974c13d96163371d20469272c6b7e9201885dc0f4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RIJLFBH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIDXpBfVM9QVhVx4zKGLV%2FEL2SqVmOLDBnSokVWAXNrdXAiAo9aG7Ehl6brLNEtxKAtcQfzYu42Q3nrx%2FI3Pub3Q%2B8yr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMfQ%2B3WHPbbATuDy6bKtwDB4yMaHACrsOzxqOZWUlb89GFkCWgNgbpqkIinScGIFzuAk%2Bef4iB4rFKh1N3cJjqhI9IvWEr51xMnmcOrfbWUlj97lwRbHzpRUHoToxf9qHnh6Tq1r1k6jOpIhSBVQtCsC4%2BBIQ%2FcorfHowIy1i5q3cyR5SnVZUM4TFgh%2FbOjMkJZqwCLIOpgICvateB7WLYYra2PtuPTkJ6cPVMpIboxX6RTiyB86T5rM22cdLb5RAya4e2xUSfoSU2SGrTzqJStoNXeSMHicht9Ev3Ie7pksCTTz%2F8Tsy1%2B4YXtwuyCTV82TfaSKE1iBJ9O%2FIl0UHuHmj4lCrsJ9031PlY4VAhLrIRCiOSVsSfWq6Lb%2B%2BlooOKsP62YeXOhH85f18U9V%2BOBd%2BVQFiPlW0YIgUce56Eppc4Rz%2F%2F%2BfeBT%2FuUgmUKDpbqTO0YwKLF9HAIDXMyg7IBfjoTkSzzWiRFrs7iKBsOBqfzU0UPXTyVO8fpSdL4zjg%2Fg7XUZAXAoLkAio2DcgJ%2Fbv1oJI%2FDscHELs12tUZ6x%2BzzX60iNCsHQ3jVQzhgXEUre8KyITiANr8J11R%2F5jX69dsnY%2BiXVwy5%2BD8RbUpVsi9EdhD6%2BX5yQO6M8udaeEvJhrde%2FWcIjAvsLq4w6YGIvQY6pgHGhePZOtJUit2y42TlsgVSUk2DDbEJ4xvIGsxBRHKLPGkSxYj8TE6QI0ooJ66qXgfAxS4K1v6yxxH8NtX6PwXCrF8O1bGhiC6JmOzbdHk93g%2B8JhDD5i7V3IikwfnPwLX8CCSnvC80Lw1CWw9casi39orWlYWIW36dlc8TFdXxMx1i2RcbEVqEr4bwuPL%2BoLkrY3fe7jwbzfWieT7It79ZWb1ssyit&X-Amz-Signature=88a30d7175666850cfe7d65746054009dbe4ead66c1dd50c71b65c6c687a10ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCQVBJC4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIGd0t3y7RCZohfjQg%2FSHz3hWe6w01t4lh3qBwjLTRARsAiEA5ATTi92TLYMugYKootLMCykDymOfWu9jdcNcWiXjT0sq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDF4sG3Z4hVHj2Xh%2FlSrcA6dbBS5J6x1TlSnARwU7OBAxCpdxDwJqHbc%2Bmey0QXeYTjxsEbTJdqOFCUQhmcC15lwS9N2MovXb4omwFTkvhfGipCzyip2npAmFkd7996uHZb7AjCORFIkDS1GQG4%2BTM3RooukYEA9DPz0MoooHdcLhcjcfBqA6kBd9u0wjNJJu%2Bd8uY1I9ZY5p98HXEszQczfwQs%2BUcBOEzEJc8T%2BKX1I61WlQIcCnVdQIhTD9LUTbYyz5YBu3NcwnlT0CXbNb2NW6T7xXkLs40GsUW08xKhTOwHeyOrMdKOWOXPuP61zSqInx2r1pYwxtVMGrAg6wa21xE%2Bb90axpXnEJuR3bJmT1ODKlVO8SB8%2BctJyEpCQX4donUXjA4tQivdY7ThUNzQ%2BIi7eJuoCpbFRlnRL8OAghXwKn7FcSIf7pOgMQCTFi4jIXlbxAInC1YbyEeK8S4ZPq6Fo4K%2FVFI40%2B6n5yYGnR0jscq%2BY1tnW0KAfInN4WJFq888inxzWDoUqQ7iqs9l%2BipKXS7izZZeIoi9bHO2XAcOU5Ut%2F1qULrDwgr%2BbCK48l156wSBT5iTa7z0q8M8QDb9m91IYZq4a8ekLgJAYn95FZ6me5vV1%2FkxzQGHyKlHKHQtqJ5auGrCHpAMP2BiL0GOqUBJo6ZasIFM65SMq%2BftdJKvbdGuuTGP8dp%2BuMHezyIGm1y6e0%2BGAGca97RNIcNTJQRxSooxvEhYjtJpCp9E%2BH0%2Fbr0xA6hM9lioQkuY7w4PZMx9wb7lQtmv7Xvn%2BSxN%2BO%2F9WFDSHQQynegNp%2FQxfBSJsXadQPMZg%2FA0eTh5ZLOnrGHWNR%2BFX4m95qVs5DezJnMaxiieFwJXMXuMNyt9A2JCwAKrDUu&X-Amz-Signature=0eafa9ecfbd980b29b83b988f38279f9923cff8e056eed373291984fc46b38e2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCQVBJC4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIGd0t3y7RCZohfjQg%2FSHz3hWe6w01t4lh3qBwjLTRARsAiEA5ATTi92TLYMugYKootLMCykDymOfWu9jdcNcWiXjT0sq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDF4sG3Z4hVHj2Xh%2FlSrcA6dbBS5J6x1TlSnARwU7OBAxCpdxDwJqHbc%2Bmey0QXeYTjxsEbTJdqOFCUQhmcC15lwS9N2MovXb4omwFTkvhfGipCzyip2npAmFkd7996uHZb7AjCORFIkDS1GQG4%2BTM3RooukYEA9DPz0MoooHdcLhcjcfBqA6kBd9u0wjNJJu%2Bd8uY1I9ZY5p98HXEszQczfwQs%2BUcBOEzEJc8T%2BKX1I61WlQIcCnVdQIhTD9LUTbYyz5YBu3NcwnlT0CXbNb2NW6T7xXkLs40GsUW08xKhTOwHeyOrMdKOWOXPuP61zSqInx2r1pYwxtVMGrAg6wa21xE%2Bb90axpXnEJuR3bJmT1ODKlVO8SB8%2BctJyEpCQX4donUXjA4tQivdY7ThUNzQ%2BIi7eJuoCpbFRlnRL8OAghXwKn7FcSIf7pOgMQCTFi4jIXlbxAInC1YbyEeK8S4ZPq6Fo4K%2FVFI40%2B6n5yYGnR0jscq%2BY1tnW0KAfInN4WJFq888inxzWDoUqQ7iqs9l%2BipKXS7izZZeIoi9bHO2XAcOU5Ut%2F1qULrDwgr%2BbCK48l156wSBT5iTa7z0q8M8QDb9m91IYZq4a8ekLgJAYn95FZ6me5vV1%2FkxzQGHyKlHKHQtqJ5auGrCHpAMP2BiL0GOqUBJo6ZasIFM65SMq%2BftdJKvbdGuuTGP8dp%2BuMHezyIGm1y6e0%2BGAGca97RNIcNTJQRxSooxvEhYjtJpCp9E%2BH0%2Fbr0xA6hM9lioQkuY7w4PZMx9wb7lQtmv7Xvn%2BSxN%2BO%2F9WFDSHQQynegNp%2FQxfBSJsXadQPMZg%2FA0eTh5ZLOnrGHWNR%2BFX4m95qVs5DezJnMaxiieFwJXMXuMNyt9A2JCwAKrDUu&X-Amz-Signature=04e09a864c81dd9eda77d8e3ff8b696a67062da79bdbc6e10c80746c81f93d8d&X-Amz-SignedHeaders=host&x-id=GetObject)

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
