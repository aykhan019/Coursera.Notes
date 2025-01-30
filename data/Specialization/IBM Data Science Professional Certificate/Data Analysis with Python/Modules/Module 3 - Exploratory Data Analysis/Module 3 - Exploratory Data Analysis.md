

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R56RI6RX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICmxns1enC6eMTqXnZJh%2Fvy5PM1kfF3WVuz2wAXbAprTAiEA0a9r90lEI1Dod9GH6O6gsPp40S1EpPmecHLP0c69bdEqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJUq1%2Bq%2BckbNS%2FaKpSrcA28mh6W%2FHPftR56AgalWMsE%2Fjtr1BwvOJ9B%2BnI%2BirekyIqsveoUI%2FjOuRjhfK9RVT225danAlxrY9iaW%2Bz3NACdgm3zW9%2BTQg7yZ5QsOYR9ALZZBZE%2BIPIoERtxypHCNyxu91cb8EsOi%2FcFW13DY1md%2BhxeNF79gu990hCVc2suOr%2FvLt%2BIZGe2k1fwnfdZRjm2nUjrusSs0wrleVq0evOpkptackrNEC6y6Dn4TTtaZOqPBDP3uNHaw2U3EgPPq0wk3OS41psTZQtcUYosS9jxgO24JDmR353f6dC8QsBQc0bZedvH2fN1Zi4OWX7tLp6l9EwWC3ZseNydQSgSav8XNdUD4t1rt18nwiRcraAuytaEeIfyvFcluRQl4qqNlzwbFvU7gy4rgJasbXO0BryigliCvGY0TgzyEEPRxpyNhjKREPKXHEcs66S6m4AqJdNToO70ciXR2AHX9oXka14%2BZOw8rAzVoTK6Azuq8p8aPzMhZBfxPmge4D1AHdKm0xep6ztydMlKH0tgABWC9ZguisMdOwWBaFKRwzDmy5Dq7ymbjUQ1MEVp9Djm5lAveEyvT%2Fqgxo1Jsu69FZyKDx%2BKm0juLjd6cDYig2QnnnK5Tpj%2FERg463H4GdNfQMJqj7LwGOqUBDntuwbKLlnIE2H8FK3iq%2FbC%2Fu1qysmiRKl09R0X%2F9YoY7wuYSMuyGZJ8OiCR4mnbq7H1JZsOQTQV%2BIq9c0iuo0rU5w4EgEXhN%2FJGsUQwhJNVb37gn%2F7LSLaZ1RjD%2FJbfD8lRavcLdheDNzQHOumSYAR2L96Yc3MjokN3ynKptgm%2F%2Fs7MVENNrJIDwFU0Conf1gK0MLactLbL2m3rk5CXxUBKhz4t&X-Amz-Signature=f7b6e691659c970bff7276cf0fe7c6104f47f97f388eae76df0ff00bae06a55f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R56RI6RX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICmxns1enC6eMTqXnZJh%2Fvy5PM1kfF3WVuz2wAXbAprTAiEA0a9r90lEI1Dod9GH6O6gsPp40S1EpPmecHLP0c69bdEqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJUq1%2Bq%2BckbNS%2FaKpSrcA28mh6W%2FHPftR56AgalWMsE%2Fjtr1BwvOJ9B%2BnI%2BirekyIqsveoUI%2FjOuRjhfK9RVT225danAlxrY9iaW%2Bz3NACdgm3zW9%2BTQg7yZ5QsOYR9ALZZBZE%2BIPIoERtxypHCNyxu91cb8EsOi%2FcFW13DY1md%2BhxeNF79gu990hCVc2suOr%2FvLt%2BIZGe2k1fwnfdZRjm2nUjrusSs0wrleVq0evOpkptackrNEC6y6Dn4TTtaZOqPBDP3uNHaw2U3EgPPq0wk3OS41psTZQtcUYosS9jxgO24JDmR353f6dC8QsBQc0bZedvH2fN1Zi4OWX7tLp6l9EwWC3ZseNydQSgSav8XNdUD4t1rt18nwiRcraAuytaEeIfyvFcluRQl4qqNlzwbFvU7gy4rgJasbXO0BryigliCvGY0TgzyEEPRxpyNhjKREPKXHEcs66S6m4AqJdNToO70ciXR2AHX9oXka14%2BZOw8rAzVoTK6Azuq8p8aPzMhZBfxPmge4D1AHdKm0xep6ztydMlKH0tgABWC9ZguisMdOwWBaFKRwzDmy5Dq7ymbjUQ1MEVp9Djm5lAveEyvT%2Fqgxo1Jsu69FZyKDx%2BKm0juLjd6cDYig2QnnnK5Tpj%2FERg463H4GdNfQMJqj7LwGOqUBDntuwbKLlnIE2H8FK3iq%2FbC%2Fu1qysmiRKl09R0X%2F9YoY7wuYSMuyGZJ8OiCR4mnbq7H1JZsOQTQV%2BIq9c0iuo0rU5w4EgEXhN%2FJGsUQwhJNVb37gn%2F7LSLaZ1RjD%2FJbfD8lRavcLdheDNzQHOumSYAR2L96Yc3MjokN3ynKptgm%2F%2Fs7MVENNrJIDwFU0Conf1gK0MLactLbL2m3rk5CXxUBKhz4t&X-Amz-Signature=4aa7932306acd0c3ca837240dd035e676182c2b27ba402aa48a1ee03c9907756&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R56RI6RX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICmxns1enC6eMTqXnZJh%2Fvy5PM1kfF3WVuz2wAXbAprTAiEA0a9r90lEI1Dod9GH6O6gsPp40S1EpPmecHLP0c69bdEqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJUq1%2Bq%2BckbNS%2FaKpSrcA28mh6W%2FHPftR56AgalWMsE%2Fjtr1BwvOJ9B%2BnI%2BirekyIqsveoUI%2FjOuRjhfK9RVT225danAlxrY9iaW%2Bz3NACdgm3zW9%2BTQg7yZ5QsOYR9ALZZBZE%2BIPIoERtxypHCNyxu91cb8EsOi%2FcFW13DY1md%2BhxeNF79gu990hCVc2suOr%2FvLt%2BIZGe2k1fwnfdZRjm2nUjrusSs0wrleVq0evOpkptackrNEC6y6Dn4TTtaZOqPBDP3uNHaw2U3EgPPq0wk3OS41psTZQtcUYosS9jxgO24JDmR353f6dC8QsBQc0bZedvH2fN1Zi4OWX7tLp6l9EwWC3ZseNydQSgSav8XNdUD4t1rt18nwiRcraAuytaEeIfyvFcluRQl4qqNlzwbFvU7gy4rgJasbXO0BryigliCvGY0TgzyEEPRxpyNhjKREPKXHEcs66S6m4AqJdNToO70ciXR2AHX9oXka14%2BZOw8rAzVoTK6Azuq8p8aPzMhZBfxPmge4D1AHdKm0xep6ztydMlKH0tgABWC9ZguisMdOwWBaFKRwzDmy5Dq7ymbjUQ1MEVp9Djm5lAveEyvT%2Fqgxo1Jsu69FZyKDx%2BKm0juLjd6cDYig2QnnnK5Tpj%2FERg463H4GdNfQMJqj7LwGOqUBDntuwbKLlnIE2H8FK3iq%2FbC%2Fu1qysmiRKl09R0X%2F9YoY7wuYSMuyGZJ8OiCR4mnbq7H1JZsOQTQV%2BIq9c0iuo0rU5w4EgEXhN%2FJGsUQwhJNVb37gn%2F7LSLaZ1RjD%2FJbfD8lRavcLdheDNzQHOumSYAR2L96Yc3MjokN3ynKptgm%2F%2Fs7MVENNrJIDwFU0Conf1gK0MLactLbL2m3rk5CXxUBKhz4t&X-Amz-Signature=9f6f51fe5b00ecabee026f1e650c7d0a5a80a02e9ea1469c87c2559aea59ee92&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNJV4I6G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFF%2BvKSiQTJqjuiaaQGP6%2BF357oHzm8Y6d4Y0xXINzxgIgATD7SF6AIpaNJjZitOepUUJ06TgRy4irYcKGJisiEjsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH884j0IKrC9GrF8kCrcA5O5rnH1eW%2BUGymJwnRbzr1Gzo0QF%2BUuJ79ZIi4NGcd%2FRLR5BkHxIsR87zftnq3v5uc4csMxhNhU4cTCm1r69O%2B14CeB0e1nZ1NSTY0uqFklT2Ivlm5kd%2BJPftEi2LOs%2BqO9QPAokrPTx4WHhceTxt0gdxzXiAGj%2BXrrAPgckcWE5Ofm6jBiAyAPN6vB1PWdnouLUAxz4EXCW73ze6Hz2B7yJeGpLS7odwG2BBnNIfc9a7lV6bgVFauI%2FsY%2BQ9h6GAFCdfAQ0oC%2Fbs12YFsi0z%2Bi5iFPgh6T9Ff%2BGrAFHdkoV9D8mcSUttFp%2FwAtU%2FeGpopFac0ETzLgfw5GABmmp9uRI09Dg9bT1MmiWLz4ca8IJNN9gJbINVvHUkcuiaDHLbfatptBmUt2nljl1EGkWhsceirq2VfN3BwU2pQu%2FjtLuc5jQuwH0p%2BO3B7S%2B0X18TwV3bUSL3OwgOTYtSSAYFB%2FD94Tp%2B9Yl20%2FuKZz9bXWuzP591VQuKthIuMCMem1aVfCwD8HgQJ5e6AbHMvLW0Ka3gELY7QGleeQiOTQBx7T%2F8%2BgPHabaN2EH1EmdcaVasqp6aUY6T1DPm2CaN2j1ZzSeigExIuLOCo98ahw4KlMRa3hDeJiNgW8g%2FwzMNKi7LwGOqUBtO1169vN8mkhLsjmtqeJrbZlZtPaxvLGiGvbcX54hhViwBUYftPktOGElM7ILSj7Nl%2F28Dy%2FDJgOh%2F20ld7VgovB4TmTtvyYKNPJmV7NN8tkk7cXNXH5QDU9FBuRXfka4cO04eg9lgIY8KG5%2BLgdKOx09lGQXiC6WCvu%2FXEu7HuLGA8%2FadTZpp8GQAurOwjk%2FRQzS2a42tAT6lAZN50PZ%2Fy%2BGpBc&X-Amz-Signature=03a54ab1edffb48e9775e5e4f5aeea9e569b8d08506156b9103f9894c2076d0c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNJV4I6G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFF%2BvKSiQTJqjuiaaQGP6%2BF357oHzm8Y6d4Y0xXINzxgIgATD7SF6AIpaNJjZitOepUUJ06TgRy4irYcKGJisiEjsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH884j0IKrC9GrF8kCrcA5O5rnH1eW%2BUGymJwnRbzr1Gzo0QF%2BUuJ79ZIi4NGcd%2FRLR5BkHxIsR87zftnq3v5uc4csMxhNhU4cTCm1r69O%2B14CeB0e1nZ1NSTY0uqFklT2Ivlm5kd%2BJPftEi2LOs%2BqO9QPAokrPTx4WHhceTxt0gdxzXiAGj%2BXrrAPgckcWE5Ofm6jBiAyAPN6vB1PWdnouLUAxz4EXCW73ze6Hz2B7yJeGpLS7odwG2BBnNIfc9a7lV6bgVFauI%2FsY%2BQ9h6GAFCdfAQ0oC%2Fbs12YFsi0z%2Bi5iFPgh6T9Ff%2BGrAFHdkoV9D8mcSUttFp%2FwAtU%2FeGpopFac0ETzLgfw5GABmmp9uRI09Dg9bT1MmiWLz4ca8IJNN9gJbINVvHUkcuiaDHLbfatptBmUt2nljl1EGkWhsceirq2VfN3BwU2pQu%2FjtLuc5jQuwH0p%2BO3B7S%2B0X18TwV3bUSL3OwgOTYtSSAYFB%2FD94Tp%2B9Yl20%2FuKZz9bXWuzP591VQuKthIuMCMem1aVfCwD8HgQJ5e6AbHMvLW0Ka3gELY7QGleeQiOTQBx7T%2F8%2BgPHabaN2EH1EmdcaVasqp6aUY6T1DPm2CaN2j1ZzSeigExIuLOCo98ahw4KlMRa3hDeJiNgW8g%2FwzMNKi7LwGOqUBtO1169vN8mkhLsjmtqeJrbZlZtPaxvLGiGvbcX54hhViwBUYftPktOGElM7ILSj7Nl%2F28Dy%2FDJgOh%2F20ld7VgovB4TmTtvyYKNPJmV7NN8tkk7cXNXH5QDU9FBuRXfka4cO04eg9lgIY8KG5%2BLgdKOx09lGQXiC6WCvu%2FXEu7HuLGA8%2FadTZpp8GQAurOwjk%2FRQzS2a42tAT6lAZN50PZ%2Fy%2BGpBc&X-Amz-Signature=0813f62b815f84904d27eeb63be37b67d8defc8d52e5e01b8c2c8718954456e3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNJV4I6G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFF%2BvKSiQTJqjuiaaQGP6%2BF357oHzm8Y6d4Y0xXINzxgIgATD7SF6AIpaNJjZitOepUUJ06TgRy4irYcKGJisiEjsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH884j0IKrC9GrF8kCrcA5O5rnH1eW%2BUGymJwnRbzr1Gzo0QF%2BUuJ79ZIi4NGcd%2FRLR5BkHxIsR87zftnq3v5uc4csMxhNhU4cTCm1r69O%2B14CeB0e1nZ1NSTY0uqFklT2Ivlm5kd%2BJPftEi2LOs%2BqO9QPAokrPTx4WHhceTxt0gdxzXiAGj%2BXrrAPgckcWE5Ofm6jBiAyAPN6vB1PWdnouLUAxz4EXCW73ze6Hz2B7yJeGpLS7odwG2BBnNIfc9a7lV6bgVFauI%2FsY%2BQ9h6GAFCdfAQ0oC%2Fbs12YFsi0z%2Bi5iFPgh6T9Ff%2BGrAFHdkoV9D8mcSUttFp%2FwAtU%2FeGpopFac0ETzLgfw5GABmmp9uRI09Dg9bT1MmiWLz4ca8IJNN9gJbINVvHUkcuiaDHLbfatptBmUt2nljl1EGkWhsceirq2VfN3BwU2pQu%2FjtLuc5jQuwH0p%2BO3B7S%2B0X18TwV3bUSL3OwgOTYtSSAYFB%2FD94Tp%2B9Yl20%2FuKZz9bXWuzP591VQuKthIuMCMem1aVfCwD8HgQJ5e6AbHMvLW0Ka3gELY7QGleeQiOTQBx7T%2F8%2BgPHabaN2EH1EmdcaVasqp6aUY6T1DPm2CaN2j1ZzSeigExIuLOCo98ahw4KlMRa3hDeJiNgW8g%2FwzMNKi7LwGOqUBtO1169vN8mkhLsjmtqeJrbZlZtPaxvLGiGvbcX54hhViwBUYftPktOGElM7ILSj7Nl%2F28Dy%2FDJgOh%2F20ld7VgovB4TmTtvyYKNPJmV7NN8tkk7cXNXH5QDU9FBuRXfka4cO04eg9lgIY8KG5%2BLgdKOx09lGQXiC6WCvu%2FXEu7HuLGA8%2FadTZpp8GQAurOwjk%2FRQzS2a42tAT6lAZN50PZ%2Fy%2BGpBc&X-Amz-Signature=0b24d5c49cfa3727ec35890ab6cd845544ef04717e24442b6589b1e833258bb7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNJV4I6G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFF%2BvKSiQTJqjuiaaQGP6%2BF357oHzm8Y6d4Y0xXINzxgIgATD7SF6AIpaNJjZitOepUUJ06TgRy4irYcKGJisiEjsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH884j0IKrC9GrF8kCrcA5O5rnH1eW%2BUGymJwnRbzr1Gzo0QF%2BUuJ79ZIi4NGcd%2FRLR5BkHxIsR87zftnq3v5uc4csMxhNhU4cTCm1r69O%2B14CeB0e1nZ1NSTY0uqFklT2Ivlm5kd%2BJPftEi2LOs%2BqO9QPAokrPTx4WHhceTxt0gdxzXiAGj%2BXrrAPgckcWE5Ofm6jBiAyAPN6vB1PWdnouLUAxz4EXCW73ze6Hz2B7yJeGpLS7odwG2BBnNIfc9a7lV6bgVFauI%2FsY%2BQ9h6GAFCdfAQ0oC%2Fbs12YFsi0z%2Bi5iFPgh6T9Ff%2BGrAFHdkoV9D8mcSUttFp%2FwAtU%2FeGpopFac0ETzLgfw5GABmmp9uRI09Dg9bT1MmiWLz4ca8IJNN9gJbINVvHUkcuiaDHLbfatptBmUt2nljl1EGkWhsceirq2VfN3BwU2pQu%2FjtLuc5jQuwH0p%2BO3B7S%2B0X18TwV3bUSL3OwgOTYtSSAYFB%2FD94Tp%2B9Yl20%2FuKZz9bXWuzP591VQuKthIuMCMem1aVfCwD8HgQJ5e6AbHMvLW0Ka3gELY7QGleeQiOTQBx7T%2F8%2BgPHabaN2EH1EmdcaVasqp6aUY6T1DPm2CaN2j1ZzSeigExIuLOCo98ahw4KlMRa3hDeJiNgW8g%2FwzMNKi7LwGOqUBtO1169vN8mkhLsjmtqeJrbZlZtPaxvLGiGvbcX54hhViwBUYftPktOGElM7ILSj7Nl%2F28Dy%2FDJgOh%2F20ld7VgovB4TmTtvyYKNPJmV7NN8tkk7cXNXH5QDU9FBuRXfka4cO04eg9lgIY8KG5%2BLgdKOx09lGQXiC6WCvu%2FXEu7HuLGA8%2FadTZpp8GQAurOwjk%2FRQzS2a42tAT6lAZN50PZ%2Fy%2BGpBc&X-Amz-Signature=d3806d0666969c9a1fffd2ecb18b08d308d24d7ae84951e1c7d582dc26459764&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNJV4I6G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFF%2BvKSiQTJqjuiaaQGP6%2BF357oHzm8Y6d4Y0xXINzxgIgATD7SF6AIpaNJjZitOepUUJ06TgRy4irYcKGJisiEjsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH884j0IKrC9GrF8kCrcA5O5rnH1eW%2BUGymJwnRbzr1Gzo0QF%2BUuJ79ZIi4NGcd%2FRLR5BkHxIsR87zftnq3v5uc4csMxhNhU4cTCm1r69O%2B14CeB0e1nZ1NSTY0uqFklT2Ivlm5kd%2BJPftEi2LOs%2BqO9QPAokrPTx4WHhceTxt0gdxzXiAGj%2BXrrAPgckcWE5Ofm6jBiAyAPN6vB1PWdnouLUAxz4EXCW73ze6Hz2B7yJeGpLS7odwG2BBnNIfc9a7lV6bgVFauI%2FsY%2BQ9h6GAFCdfAQ0oC%2Fbs12YFsi0z%2Bi5iFPgh6T9Ff%2BGrAFHdkoV9D8mcSUttFp%2FwAtU%2FeGpopFac0ETzLgfw5GABmmp9uRI09Dg9bT1MmiWLz4ca8IJNN9gJbINVvHUkcuiaDHLbfatptBmUt2nljl1EGkWhsceirq2VfN3BwU2pQu%2FjtLuc5jQuwH0p%2BO3B7S%2B0X18TwV3bUSL3OwgOTYtSSAYFB%2FD94Tp%2B9Yl20%2FuKZz9bXWuzP591VQuKthIuMCMem1aVfCwD8HgQJ5e6AbHMvLW0Ka3gELY7QGleeQiOTQBx7T%2F8%2BgPHabaN2EH1EmdcaVasqp6aUY6T1DPm2CaN2j1ZzSeigExIuLOCo98ahw4KlMRa3hDeJiNgW8g%2FwzMNKi7LwGOqUBtO1169vN8mkhLsjmtqeJrbZlZtPaxvLGiGvbcX54hhViwBUYftPktOGElM7ILSj7Nl%2F28Dy%2FDJgOh%2F20ld7VgovB4TmTtvyYKNPJmV7NN8tkk7cXNXH5QDU9FBuRXfka4cO04eg9lgIY8KG5%2BLgdKOx09lGQXiC6WCvu%2FXEu7HuLGA8%2FadTZpp8GQAurOwjk%2FRQzS2a42tAT6lAZN50PZ%2Fy%2BGpBc&X-Amz-Signature=89b5e5053bfb17d39094c3ab53dc9845e282534d1134e1c67ff9066bb991f4b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNJV4I6G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFF%2BvKSiQTJqjuiaaQGP6%2BF357oHzm8Y6d4Y0xXINzxgIgATD7SF6AIpaNJjZitOepUUJ06TgRy4irYcKGJisiEjsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH884j0IKrC9GrF8kCrcA5O5rnH1eW%2BUGymJwnRbzr1Gzo0QF%2BUuJ79ZIi4NGcd%2FRLR5BkHxIsR87zftnq3v5uc4csMxhNhU4cTCm1r69O%2B14CeB0e1nZ1NSTY0uqFklT2Ivlm5kd%2BJPftEi2LOs%2BqO9QPAokrPTx4WHhceTxt0gdxzXiAGj%2BXrrAPgckcWE5Ofm6jBiAyAPN6vB1PWdnouLUAxz4EXCW73ze6Hz2B7yJeGpLS7odwG2BBnNIfc9a7lV6bgVFauI%2FsY%2BQ9h6GAFCdfAQ0oC%2Fbs12YFsi0z%2Bi5iFPgh6T9Ff%2BGrAFHdkoV9D8mcSUttFp%2FwAtU%2FeGpopFac0ETzLgfw5GABmmp9uRI09Dg9bT1MmiWLz4ca8IJNN9gJbINVvHUkcuiaDHLbfatptBmUt2nljl1EGkWhsceirq2VfN3BwU2pQu%2FjtLuc5jQuwH0p%2BO3B7S%2B0X18TwV3bUSL3OwgOTYtSSAYFB%2FD94Tp%2B9Yl20%2FuKZz9bXWuzP591VQuKthIuMCMem1aVfCwD8HgQJ5e6AbHMvLW0Ka3gELY7QGleeQiOTQBx7T%2F8%2BgPHabaN2EH1EmdcaVasqp6aUY6T1DPm2CaN2j1ZzSeigExIuLOCo98ahw4KlMRa3hDeJiNgW8g%2FwzMNKi7LwGOqUBtO1169vN8mkhLsjmtqeJrbZlZtPaxvLGiGvbcX54hhViwBUYftPktOGElM7ILSj7Nl%2F28Dy%2FDJgOh%2F20ld7VgovB4TmTtvyYKNPJmV7NN8tkk7cXNXH5QDU9FBuRXfka4cO04eg9lgIY8KG5%2BLgdKOx09lGQXiC6WCvu%2FXEu7HuLGA8%2FadTZpp8GQAurOwjk%2FRQzS2a42tAT6lAZN50PZ%2Fy%2BGpBc&X-Amz-Signature=32d27f8fcd870864c85d03395fe8648a6f45d8cc81a9831bfaf7712794da83e7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675BEBYB6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG5UCFOb%2FfTPORtCzDmmD53tXFCoqpvQfRXo53fVE%2BYGAiEA%2BP%2Fzfc5r9E2yEg9JTSiOyj7R%2BlWQN0GUj3ltLqrozVIqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKxubuYylNffoPXGKircA6ena8BdUsxDon%2FxDKxmNYRiLNaR1MC%2FIJMPtZ32PK6HHHkYzYBsGVbMVaWMzwQcMlGba485jeL3hmq%2FM3B6SfJpV8bcv2WBG8mQJFQusv1LxXp%2BuG6vJ1dmWu29zwPeaeTsRJYcV2coOFciwh7ibuGOFkGrb7EH9yxGPr48%2FjLsqgNJscOExLbbWTApTfo82Fg70h7WNNcsQ%2FHvxB3rLafBUkDw5GKz9y9Hg0RKwbycPtsy%2BtsDC7IwLqfXHccMnIo9QIqtdKYqd3qoBX98zv2xloovg%2Fnt5ilj%2BJO3UUWBpwlfTbmI4kLo%2B7a3Ux7cJqhyfnyeG18Y1NPlJQfFdMorSpN8tMm2T3GObeSlpAKKjP6th5%2BcFXehEtK%2BPm%2FkMvztSwd4lZAcqBNGD0BbA1y5XrSzNQ%2BkVRdqyPmz7T1TCNecT1s2C8WF8DOdoD3tR5FIltni%2FTw%2FoKPW5hMkr9mzTuJD1BjbYYsl1bRtqWHcq2m%2BayjpOfK4JAdPBPex%2BL%2FqijWs%2BpnhaphKSqA%2F82aYjoGp6BHp49HOv4A7GjhObtV2131kaT9K8ZI7YsmNn6ahNc4832Y7ARzp12IzeiuHg1rkNPhvqnYn%2Fa2kwuY0nvriVRJ994M3pCyjMOWi7LwGOqUBUqPVbQKoJTUfiWcsWxQ%2BZkzHGxsrjyazvhvL1oebxbz2XEwyVlG97NSfavQhp9ZkTd%2BsXmfhC7jQ8plLHL%2BJTs7oNNQAXbWLsaDZowY28WjbxHDY2cGm1ka7L7gUU3wU9WMfBi1uwAWydYKpII7ZJA9mln1ivLKKcnCAssOmMYjc2lLP7eeRWgLSxCkHEimoaXXVOmcJ%2Bv31CWCs0keVCjh4EHFm&X-Amz-Signature=60cc57cfbf0ea773c4c2ab285dd9bfe175feacda90ac074bb3ae4d88dcae7504&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4D3BW5A%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNUUzTX8SPnWZ8QUpR%2F4B8liaH3EZODzWPPX0eO00GlAiA4tAdrdAZEGtnsIJdFlbcKyznAiO5sdaP78O4DrSGwaiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHyf5Y2%2FopE80nR73KtwD%2BEQdZOG8OttMO7%2BPbZ7U4RGSbu64zeieebUSz22pkei%2FOPqgB7YXa0ZiaVYCQEWfyEyn%2Bw%2B3YQSerKc34NxjhC4GlxjsbCjcMydQMQYaIZ0w4lXF1I72uRzIjOeJEVPJv3Rkc0taRv8hEHnb%2FKyX8zPUHqSR2Otp4kg42rHi35tBQjsvp9GY6ycHSi3DDaWvMS3JzrkOVmD8%2FVkUgJLMauOBroB4YKZq2MBOJFKpqye69fD7J3VK7AcEFZm%2BO%2B1cfMZ2cYo7tiGkxq%2Bt43Eo3%2FX1kEPzA9L3RmKclcQ1Shyi5tbG0kadzOpuKjX6IqdRv0NQvwHqBdTYGoB6hICQfmsDSsqXwyuIBbkQRXG3njJR8leNJe%2BXguppwj16amwta1RN5NPcMJnniiopsdVKkf5VIBEAIM%2FFpNgs%2FFgkGIN5wfTey77AbgdtBC%2FpVoa3TdBDO3cUvvM2vzhbtDgu9iJ%2FAZQm%2F8oaJP780UT4IUuFWqR4sTOLmqrLFh0BMdTI9G93kbX7D1n2Npqpmhy%2BlAnNS%2FsT%2FcIpEeZ6ScEGKSJ8cnag6lCNVY4ns5BuGtzXngUfXGfY5jAg3PoF1w0fE6IWdHLUmBacI1O%2BFPG3ildeHlwcDFw%2F%2FvDJG6wwlqPsvAY6pgHkp9e3m31PPu06bO79dBjh55KEUG8NjT3YOXzqoZm0yuUm1OvsMbaz2SqPbiolD%2F8aoB8RU19ELKeyJHWwYDIC%2FYB3gk8yd8aFBnzvMMB%2FW%2BUHVk%2B2VRewspslv3qKZefAIGcvAm0AsLsmBqUJvzOV6N8FLfjP%2BoVDjEEUFAlI1rW4PKJWsW6FiabIF9kJge9afpCTLLoBMX7AdAoJFjB%2BLRvRBQAy&X-Amz-Signature=728897ee9a1c25bfcdfb6fe88ad7d946ffe070aca08327514b55e99b0e545180&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNJV4I6G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFF%2BvKSiQTJqjuiaaQGP6%2BF357oHzm8Y6d4Y0xXINzxgIgATD7SF6AIpaNJjZitOepUUJ06TgRy4irYcKGJisiEjsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH884j0IKrC9GrF8kCrcA5O5rnH1eW%2BUGymJwnRbzr1Gzo0QF%2BUuJ79ZIi4NGcd%2FRLR5BkHxIsR87zftnq3v5uc4csMxhNhU4cTCm1r69O%2B14CeB0e1nZ1NSTY0uqFklT2Ivlm5kd%2BJPftEi2LOs%2BqO9QPAokrPTx4WHhceTxt0gdxzXiAGj%2BXrrAPgckcWE5Ofm6jBiAyAPN6vB1PWdnouLUAxz4EXCW73ze6Hz2B7yJeGpLS7odwG2BBnNIfc9a7lV6bgVFauI%2FsY%2BQ9h6GAFCdfAQ0oC%2Fbs12YFsi0z%2Bi5iFPgh6T9Ff%2BGrAFHdkoV9D8mcSUttFp%2FwAtU%2FeGpopFac0ETzLgfw5GABmmp9uRI09Dg9bT1MmiWLz4ca8IJNN9gJbINVvHUkcuiaDHLbfatptBmUt2nljl1EGkWhsceirq2VfN3BwU2pQu%2FjtLuc5jQuwH0p%2BO3B7S%2B0X18TwV3bUSL3OwgOTYtSSAYFB%2FD94Tp%2B9Yl20%2FuKZz9bXWuzP591VQuKthIuMCMem1aVfCwD8HgQJ5e6AbHMvLW0Ka3gELY7QGleeQiOTQBx7T%2F8%2BgPHabaN2EH1EmdcaVasqp6aUY6T1DPm2CaN2j1ZzSeigExIuLOCo98ahw4KlMRa3hDeJiNgW8g%2FwzMNKi7LwGOqUBtO1169vN8mkhLsjmtqeJrbZlZtPaxvLGiGvbcX54hhViwBUYftPktOGElM7ILSj7Nl%2F28Dy%2FDJgOh%2F20ld7VgovB4TmTtvyYKNPJmV7NN8tkk7cXNXH5QDU9FBuRXfka4cO04eg9lgIY8KG5%2BLgdKOx09lGQXiC6WCvu%2FXEu7HuLGA8%2FadTZpp8GQAurOwjk%2FRQzS2a42tAT6lAZN50PZ%2Fy%2BGpBc&X-Amz-Signature=5ac17428bc38b4b64142afe030cc7e9ccbc1b51c05ec10000b5cbe195a8b4917&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNJV4I6G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFF%2BvKSiQTJqjuiaaQGP6%2BF357oHzm8Y6d4Y0xXINzxgIgATD7SF6AIpaNJjZitOepUUJ06TgRy4irYcKGJisiEjsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH884j0IKrC9GrF8kCrcA5O5rnH1eW%2BUGymJwnRbzr1Gzo0QF%2BUuJ79ZIi4NGcd%2FRLR5BkHxIsR87zftnq3v5uc4csMxhNhU4cTCm1r69O%2B14CeB0e1nZ1NSTY0uqFklT2Ivlm5kd%2BJPftEi2LOs%2BqO9QPAokrPTx4WHhceTxt0gdxzXiAGj%2BXrrAPgckcWE5Ofm6jBiAyAPN6vB1PWdnouLUAxz4EXCW73ze6Hz2B7yJeGpLS7odwG2BBnNIfc9a7lV6bgVFauI%2FsY%2BQ9h6GAFCdfAQ0oC%2Fbs12YFsi0z%2Bi5iFPgh6T9Ff%2BGrAFHdkoV9D8mcSUttFp%2FwAtU%2FeGpopFac0ETzLgfw5GABmmp9uRI09Dg9bT1MmiWLz4ca8IJNN9gJbINVvHUkcuiaDHLbfatptBmUt2nljl1EGkWhsceirq2VfN3BwU2pQu%2FjtLuc5jQuwH0p%2BO3B7S%2B0X18TwV3bUSL3OwgOTYtSSAYFB%2FD94Tp%2B9Yl20%2FuKZz9bXWuzP591VQuKthIuMCMem1aVfCwD8HgQJ5e6AbHMvLW0Ka3gELY7QGleeQiOTQBx7T%2F8%2BgPHabaN2EH1EmdcaVasqp6aUY6T1DPm2CaN2j1ZzSeigExIuLOCo98ahw4KlMRa3hDeJiNgW8g%2FwzMNKi7LwGOqUBtO1169vN8mkhLsjmtqeJrbZlZtPaxvLGiGvbcX54hhViwBUYftPktOGElM7ILSj7Nl%2F28Dy%2FDJgOh%2F20ld7VgovB4TmTtvyYKNPJmV7NN8tkk7cXNXH5QDU9FBuRXfka4cO04eg9lgIY8KG5%2BLgdKOx09lGQXiC6WCvu%2FXEu7HuLGA8%2FadTZpp8GQAurOwjk%2FRQzS2a42tAT6lAZN50PZ%2Fy%2BGpBc&X-Amz-Signature=2ef0240cafd1712c801c7ad2643e0dadb5047bb6979bb34d9e01a5fb109082f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNJV4I6G%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFF%2BvKSiQTJqjuiaaQGP6%2BF357oHzm8Y6d4Y0xXINzxgIgATD7SF6AIpaNJjZitOepUUJ06TgRy4irYcKGJisiEjsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH884j0IKrC9GrF8kCrcA5O5rnH1eW%2BUGymJwnRbzr1Gzo0QF%2BUuJ79ZIi4NGcd%2FRLR5BkHxIsR87zftnq3v5uc4csMxhNhU4cTCm1r69O%2B14CeB0e1nZ1NSTY0uqFklT2Ivlm5kd%2BJPftEi2LOs%2BqO9QPAokrPTx4WHhceTxt0gdxzXiAGj%2BXrrAPgckcWE5Ofm6jBiAyAPN6vB1PWdnouLUAxz4EXCW73ze6Hz2B7yJeGpLS7odwG2BBnNIfc9a7lV6bgVFauI%2FsY%2BQ9h6GAFCdfAQ0oC%2Fbs12YFsi0z%2Bi5iFPgh6T9Ff%2BGrAFHdkoV9D8mcSUttFp%2FwAtU%2FeGpopFac0ETzLgfw5GABmmp9uRI09Dg9bT1MmiWLz4ca8IJNN9gJbINVvHUkcuiaDHLbfatptBmUt2nljl1EGkWhsceirq2VfN3BwU2pQu%2FjtLuc5jQuwH0p%2BO3B7S%2B0X18TwV3bUSL3OwgOTYtSSAYFB%2FD94Tp%2B9Yl20%2FuKZz9bXWuzP591VQuKthIuMCMem1aVfCwD8HgQJ5e6AbHMvLW0Ka3gELY7QGleeQiOTQBx7T%2F8%2BgPHabaN2EH1EmdcaVasqp6aUY6T1DPm2CaN2j1ZzSeigExIuLOCo98ahw4KlMRa3hDeJiNgW8g%2FwzMNKi7LwGOqUBtO1169vN8mkhLsjmtqeJrbZlZtPaxvLGiGvbcX54hhViwBUYftPktOGElM7ILSj7Nl%2F28Dy%2FDJgOh%2F20ld7VgovB4TmTtvyYKNPJmV7NN8tkk7cXNXH5QDU9FBuRXfka4cO04eg9lgIY8KG5%2BLgdKOx09lGQXiC6WCvu%2FXEu7HuLGA8%2FadTZpp8GQAurOwjk%2FRQzS2a42tAT6lAZN50PZ%2Fy%2BGpBc&X-Amz-Signature=5e891e66e89ba13001c93e5aed15d0bf25be4c70e552223779a2ba986c5da1ba&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AAJOOXI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Ft7p9inClJoLoa5MSTJ2x0bJZBdMkzK6YavQFnPYYYQIgeD5Wvo9JpqEdAzd3%2F47RGt%2F2vwatReLqbyWWxKEKuHgqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF4kxAyl73JHYC5ZSrcAxAtTqoqh1BEA3Er5HirIzpC3nP%2BquaAA5Mgzi%2BRKrniQ9D7UNEb1jUlKlsq4ZiqlHcUinUGYx%2Fm87bIqJ0Kv3vwrBp5EWnnyqrdHCnAI97seuRWfD2kZ6Dh%2FH0cWlSPEzHkBm54Ugi5oGGbzCBOy0WtegEo%2BwVX7lHnbBwv5wA9x%2BEkOMdHtMiAm8q0CEvTv78NO%2BVC5VUqKB4yNpof41y2t1iouFJMgEuU5ukaUxj%2Fc7bIo5%2ByGV0krBbHdr%2Ff4G%2B8pwq10lLIASU3pBkAknXaxgCUXeAOgw2R5476iom5nvg9ROuieSy868H9nzdXTDwwJep4rg1WTB8AC6EpkHMhL%2FZsqfpIwGVfm14Z%2BbJTqPwW69u9HXkxzn8vydZrDY3vzec00JvEXT3v%2B1iIfi1IGqTfnDK5Wcnjv9jtR05VozmQW541bzvmjVBgTHJ4N1paD0s41SAP7KLAjQmDTKFxMh6jqFTj4%2F3UnRM9U365MmJ9%2FSV3530HVR6qcPqDMp%2F7vWZ3rsc7z0ZsR9m4TgBrtOhabIi8tGAwGwReFwTQ45mEXWclay8kLw4F32r0rVJT5G4HI2OvuIsyNa7PesWGptcaH6cCQ9hA%2F3XQrIrtgmsnvouDttGdPkWOMJyj7LwGOqUBXk301ndcGL0uYN%2Be9CDoTbTuZCJWyY0Gpviy6H5e9zC8d1GIPJYZCNLgz9gtpgDTFF5JUUWJyi0px980gJDsr1qNDjCpN7AQ3uIuyyfCbDTW%2B8F60IFwjzB0z0v8GKwZ42oqNETlcdkuS%2BxVnYWt4Bw%2F944oHSafJsVxCLpZE%2FdWZo%2FXZutVJ7QN7wEzs1CRYzGoHcyjD0j5P3cHoBqiQ6V2grT%2B&X-Amz-Signature=f7d902aa75f4ea91f4ba53e16a8e339a63870a4678ce169c56f86bfb0cf66e91&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHZ2XKOI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFJqJXGPYxWvkWZP21cdoqCjZdXp1kC2vAq3xvr5b%2FguAiA2J0akJu0%2BIZq7xLpoNd49Psos%2F%2B2JEvKD3x3l2knz1iqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBR8AVIWKjer3VTvlKtwD8ei%2FboW4pNYGNfq%2BrYwE4Kfr42U61J5y%2B9EJPgfXDocMmtRLVRAfNpovp53%2FByx2BYuch1jqEbjKl5SP8EzPxWkipTZ6RJVZ2RMmnljnJEsJmHD8TcvCJy9sMxEpkN5blRCYAJHgWVMRr5YBWbT%2FSKFduj0dwaf54oiDy4MxUMe336IG3%2BKfgwiFpIEXr%2BE%2FESJtpfH6eaB6gec2sVai%2F9oKfx%2FWnWqYtHWd2AbJsTMQCani8P6vcpgTkceprZLsDK5KTXm%2BkGfGnACYBFs9QHou9MswnjNS%2BSc%2FOcyIntE4iTkSZqppnuhKcE3NIlfW4WH%2Bo5VWiD2nkErT439v3okMA2aTYftnVdIBgxMXf0buqlYmTQc1r6NUFtSsSmAhJ0SqqlZzj9nYwRMcl5WpYvMlYgh%2BzMFqu%2Fe17bGec8WdknqQt%2F478tbmYzQWIQwxsUnsBS92hIJkKahxDxzlrd53KvCnmV%2BVkeIMSkt1Xh9P7ulud%2BmQt1bAJU765rtPr6jJyKBL3WTMbyAuuN7wMpFUYIG0upQzSobkdldreL%2BHXvX2vlFDImYA4bFCnH6qqYab9JxgdsDsb0XKQQUmr1PMlXGDtiRzzWtakkUJRmiRgcQqbvnxjFWbGPswj6PsvAY6pgGKLjKIW476U2jxXqabx3%2FxAtw7CNzZM1Td512uqDkGWWstIaSNQN9FNZ6uCkhpWjqsmXYIu3KVCvh1m66kBgtxzTkz%2Fe7TMrjux0SBQ1rvI42aXgM%2B%2FHgCIEwWSPxizYZq45qkbhSn1samPZGHVOiLGBEmWPwKubR93c1KabABK3cyPbop0FLH4W15hcCTOEJTzwyzImhGxHqO3UQQqHRePxMpHwQw&X-Amz-Signature=826b7320b8917efada2f9eac1d88d21113ddd5dbffe2198e68b5bc2d41639b08&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RIMPFJ5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGS8pwXi8JkRS4SH3l%2Bf4QTK810ZgBy%2F8u4tEE%2BdyG2DAiEAiagCAZIvVPm6ywnL3d2Lu5WVf0XsPSZ9BUda5XEQBXIqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPq61qyuKyMbuIoY7CrcA3wOd%2FJXTU96ePgR%2Fovyjyu43kLxZuuKGDRYmpASg07mAfXvaZvKSRh0h1H3KJKrAsxhUa7Q%2F%2BaDFKGA4czmxJ%2FDORSd3cp4eejGNJ0V2RKxiJssMDwQ4Wv3ynNepTvbIGDdE3PsVkD1ZJrM6YnWdz7roNENgWaNkQU8ElfsnwqeeR5WEP7khbhXkl6LiCmR50VWvhzICWCrchcboniuva9nZUSmcJDpkkXu23rmtnpAN%2Bfz%2FhsQDbHtpQk0rGh%2F4BmDobgN1x1S%2Fp1GTEBhEGqH%2BHWxGbSyJKs8RLFT7AXqO7zh3vWHcfkGlj1KmzLOxjCXddsUHUN%2B3%2Fv1zkqAL0slvsnwBX1lLkBIt2CikIw998NsDozfT5uaOdR9TaJcR%2BCKTGmwVXPvgYELRrJzeWDmShiWYYd9a7HZvmUjldSbPDgjh3bTp%2BQE3DNlm935wH6Xm0Y5JGinB3J0pek6RB3hqGWydg4sl3ccMBAblRj7gbVqfrEufe%2Fe0AC68uz%2BZexqlFeQrGZV0qwgiwdxmXRmmQjrjqDWszkJd68CuNqCFZkxoBQnuKnmcm1QQFkFtxIWKLXCxPyXrdB2RBfI%2BIYr9H%2B0920r3mbq4s90Jx6w3TvSafI8Af2nUfYSMM6i7LwGOqUBoISAbCoK29Qrjb8UM8tVQ4b1sZHqpI9R%2FgU3e6i4XiqZWPVpkm9nB1Ynu707JWg55TsmbNz69ZtBtPFafAc19W5Wj4aizPpR58vfEI7nYT4ltoDAVFaamPVBvolTYM%2FO83syu%2FGtwz9v%2FlvNMo8qLvVN4huBHips29Bhjhdq%2Bs%2BrmiJjARQ2LD3phBZvxMLS9hD9ozA8oW3BKNKx8UBpaP0MqP6B&X-Amz-Signature=073c51b9334a2e643543c5015d45ed800980a444b45f15fa6dd8b2f949924e93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VE5RUMDO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWZWADonMuPO0Am0gEDgPYsVhwyKliHx3dIaDU%2FBN20gIhAOchVJQ8QRPLqDW4FVOCQvMKg5epLFozbAIUXXNfZuj5KogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzKf726Pijv76p7JvQq3APUNKq9Zqkleaz8tXfH%2Bd1ylzJYb6kNGhjvMuA5g8LGf2nOFsZew9F5NhnV2RyE5mXviJfoNVUG81bYL2soNdUp%2F%2F8QDe6XctrAqR1QQvt3dfpFMzbx0u%2ByznC5iKKOXmD4%2Bg3WPnA1dIn%2FATwQSjShS6RjfnWVUi2Kvp%2BSRTmQbA3Lh7l39MEehWLHuM3Fd2Hvx0WhzKJsKTQXUzy8wi2jdR3w8K8n1HkC0XJeniOhIDiUrQaFKqeD5e%2BFv51XqCqlid5H72OMYfUp%2BlFx9pbkUli57V%2B12GH1QsPd%2B%2BeZ8Yq74dxcgfXQfUps1nyFhhXF%2F0i9DlSDxklq%2BR4TeFT1R5iEab5xYwZkcN8cpqfppSVtmcwtcBFdft1rOBBWQ86X7tnf8XO09IiFZiQsYykjpYjwap490trjk8NyiktzMm2%2FWoyqOH5PPrn2Gwi1BxudPe0eoVXvssAfM1aIsLYtDqJq7ktPTfIlvqQqcy7l70G7mHP%2BhiZgfiixHOyZRtMyzzwS%2B57dhD%2Bf8DHX87ndUFF%2BGOkBhkyXvE8kA%2B5UBN%2F0z9H2NPHvl8ZKmyt4Ai3f%2FRKT%2Bya9v4xLqSEKx0W8tHpXe00ZWmbjW9ZIyWehsTQiqQjGaeTPMjEpuDCco%2By8BjqkARkRtRCU0q2HBRccGW40qyJDctuEEteQ%2B5vaB1UEYoOPrdPZYGTkddXEn7CVovkcjtCA3mrHFfzkOtQ%2BZ7AUbp4n0nSHgg8YBJsGdaW6J%2F0Di6cSn%2Bm5zxXKMz%2FUc3vN5b8T46O9mA5wd1yynFLB9f9cQKYSmMI9cYoWjJpJeBz2Kn1wVbYW%2BG7%2BMiRtWRf4fWj8ZesQKYAQZ6grdiIJS%2B5OxnYz&X-Amz-Signature=057a590f10412e6c38758235437a2e2dcec51981469abfc592072ffa8a0b8ee5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VE5RUMDO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWZWADonMuPO0Am0gEDgPYsVhwyKliHx3dIaDU%2FBN20gIhAOchVJQ8QRPLqDW4FVOCQvMKg5epLFozbAIUXXNfZuj5KogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzKf726Pijv76p7JvQq3APUNKq9Zqkleaz8tXfH%2Bd1ylzJYb6kNGhjvMuA5g8LGf2nOFsZew9F5NhnV2RyE5mXviJfoNVUG81bYL2soNdUp%2F%2F8QDe6XctrAqR1QQvt3dfpFMzbx0u%2ByznC5iKKOXmD4%2Bg3WPnA1dIn%2FATwQSjShS6RjfnWVUi2Kvp%2BSRTmQbA3Lh7l39MEehWLHuM3Fd2Hvx0WhzKJsKTQXUzy8wi2jdR3w8K8n1HkC0XJeniOhIDiUrQaFKqeD5e%2BFv51XqCqlid5H72OMYfUp%2BlFx9pbkUli57V%2B12GH1QsPd%2B%2BeZ8Yq74dxcgfXQfUps1nyFhhXF%2F0i9DlSDxklq%2BR4TeFT1R5iEab5xYwZkcN8cpqfppSVtmcwtcBFdft1rOBBWQ86X7tnf8XO09IiFZiQsYykjpYjwap490trjk8NyiktzMm2%2FWoyqOH5PPrn2Gwi1BxudPe0eoVXvssAfM1aIsLYtDqJq7ktPTfIlvqQqcy7l70G7mHP%2BhiZgfiixHOyZRtMyzzwS%2B57dhD%2Bf8DHX87ndUFF%2BGOkBhkyXvE8kA%2B5UBN%2F0z9H2NPHvl8ZKmyt4Ai3f%2FRKT%2Bya9v4xLqSEKx0W8tHpXe00ZWmbjW9ZIyWehsTQiqQjGaeTPMjEpuDCco%2By8BjqkARkRtRCU0q2HBRccGW40qyJDctuEEteQ%2B5vaB1UEYoOPrdPZYGTkddXEn7CVovkcjtCA3mrHFfzkOtQ%2BZ7AUbp4n0nSHgg8YBJsGdaW6J%2F0Di6cSn%2Bm5zxXKMz%2FUc3vN5b8T46O9mA5wd1yynFLB9f9cQKYSmMI9cYoWjJpJeBz2Kn1wVbYW%2BG7%2BMiRtWRf4fWj8ZesQKYAQZ6grdiIJS%2B5OxnYz&X-Amz-Signature=6160a97e1a151ae80536ad9d584d67acbed689871c03ac3f8ba43b61bc60a3c4&X-Amz-SignedHeaders=host&x-id=GetObject)

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
