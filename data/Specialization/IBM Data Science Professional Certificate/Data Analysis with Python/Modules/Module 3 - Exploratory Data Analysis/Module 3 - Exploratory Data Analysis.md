

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJTZNGG3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGURCWlPF6dYOf4DtbN5y7PTBLr5eoLmoR77oLEkYOzGAiBLtANqK71pok9sdIUtPAPRI052Obs1qlhFZ05Dd6nESiqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnVgHd6GfbePdZF4JKtwDY%2FAmrlpsVdwEMgKYLVVDywFWvMHYC6DvDobtOnP5u4jEcKVKcaqsif5NA%2BLwthzO9yaKniajpR3GPdnBV3pKazWhAH%2B7R1XYTAqKYt787gS%2FXO%2BZWtZ135b2%2FqGNd0b9go0TxTepjwR4m3bE2JjOVBkFRMG4eqBft1NN6oYVT9sju%2FXmAJmDdZA0HvwB5FZwqKqFIkOVCUBX%2FwI7VeTu5IeXtaIZB3h4RMUGPr%2BhDVcTY9CKpM5G9qVENPleH9edOHAH0oBznkNgAYxiBVAu%2Bf8OCJ1RHNULBfGTA8%2B%2BVA4SUOKLq7M3P%2FvxjzJ03tjc8T5v4SRnHGnKBgp%2FajOVWTpBFllsjunF1PaGM3P%2BJePWb9mKauJpigAmo8RVSoyEx74XLyVaCvKhrSG89S1Gim0INX2YDYBvL0axLEHOACWz5YZH1jPlSBHJ4%2BSVBIcN34E4TymoENkg6BdTfHvUtAFb8F1j%2FrJpFxjtRm8CyokwuXJrjZ%2BOUqc2rEWJSlKnKvWz8z2jaBFfZq3VgnOOxO%2BH3pW1Iv4FICWWXleKqAQyEfN8ILT7FZ2I7FQXOYsRg6DhxFGkTvs50IooN0cuNRwVK9JxVcyZm58o82rj8BV0GNbZyhIu%2B6xQD0EwoLXwvAY6pgHGmWWWdCj3RgUSIBHWBbtO9BlD7QBvQBeeVWVe33azlROmXEeOC05VScCRTdEJjmGVLcp69g%2Fh7%2BxAbqiQE%2FUesaxEcRagDrin24jzlIMvCXB8m%2F%2BUupAs4H%2Fyzf02m9jhjkKvmaDuK3xEb5M5ViqsQFFdsv%2BoElJgOhY21yaYTb245mwLSv%2BdynV9Aid3fjKve9Q%2FrU%2BXaL4vT%2BjE%2FR5lumPtQAss&X-Amz-Signature=f35297cccb7e003a9e31b2766da28b58a23a213b18218456f80918374acc649e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJTZNGG3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGURCWlPF6dYOf4DtbN5y7PTBLr5eoLmoR77oLEkYOzGAiBLtANqK71pok9sdIUtPAPRI052Obs1qlhFZ05Dd6nESiqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnVgHd6GfbePdZF4JKtwDY%2FAmrlpsVdwEMgKYLVVDywFWvMHYC6DvDobtOnP5u4jEcKVKcaqsif5NA%2BLwthzO9yaKniajpR3GPdnBV3pKazWhAH%2B7R1XYTAqKYt787gS%2FXO%2BZWtZ135b2%2FqGNd0b9go0TxTepjwR4m3bE2JjOVBkFRMG4eqBft1NN6oYVT9sju%2FXmAJmDdZA0HvwB5FZwqKqFIkOVCUBX%2FwI7VeTu5IeXtaIZB3h4RMUGPr%2BhDVcTY9CKpM5G9qVENPleH9edOHAH0oBznkNgAYxiBVAu%2Bf8OCJ1RHNULBfGTA8%2B%2BVA4SUOKLq7M3P%2FvxjzJ03tjc8T5v4SRnHGnKBgp%2FajOVWTpBFllsjunF1PaGM3P%2BJePWb9mKauJpigAmo8RVSoyEx74XLyVaCvKhrSG89S1Gim0INX2YDYBvL0axLEHOACWz5YZH1jPlSBHJ4%2BSVBIcN34E4TymoENkg6BdTfHvUtAFb8F1j%2FrJpFxjtRm8CyokwuXJrjZ%2BOUqc2rEWJSlKnKvWz8z2jaBFfZq3VgnOOxO%2BH3pW1Iv4FICWWXleKqAQyEfN8ILT7FZ2I7FQXOYsRg6DhxFGkTvs50IooN0cuNRwVK9JxVcyZm58o82rj8BV0GNbZyhIu%2B6xQD0EwoLXwvAY6pgHGmWWWdCj3RgUSIBHWBbtO9BlD7QBvQBeeVWVe33azlROmXEeOC05VScCRTdEJjmGVLcp69g%2Fh7%2BxAbqiQE%2FUesaxEcRagDrin24jzlIMvCXB8m%2F%2BUupAs4H%2Fyzf02m9jhjkKvmaDuK3xEb5M5ViqsQFFdsv%2BoElJgOhY21yaYTb245mwLSv%2BdynV9Aid3fjKve9Q%2FrU%2BXaL4vT%2BjE%2FR5lumPtQAss&X-Amz-Signature=b9595c834310912583e062ecee20e98aa11341dd0212fe8e91b085457a123939&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJTZNGG3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGURCWlPF6dYOf4DtbN5y7PTBLr5eoLmoR77oLEkYOzGAiBLtANqK71pok9sdIUtPAPRI052Obs1qlhFZ05Dd6nESiqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnVgHd6GfbePdZF4JKtwDY%2FAmrlpsVdwEMgKYLVVDywFWvMHYC6DvDobtOnP5u4jEcKVKcaqsif5NA%2BLwthzO9yaKniajpR3GPdnBV3pKazWhAH%2B7R1XYTAqKYt787gS%2FXO%2BZWtZ135b2%2FqGNd0b9go0TxTepjwR4m3bE2JjOVBkFRMG4eqBft1NN6oYVT9sju%2FXmAJmDdZA0HvwB5FZwqKqFIkOVCUBX%2FwI7VeTu5IeXtaIZB3h4RMUGPr%2BhDVcTY9CKpM5G9qVENPleH9edOHAH0oBznkNgAYxiBVAu%2Bf8OCJ1RHNULBfGTA8%2B%2BVA4SUOKLq7M3P%2FvxjzJ03tjc8T5v4SRnHGnKBgp%2FajOVWTpBFllsjunF1PaGM3P%2BJePWb9mKauJpigAmo8RVSoyEx74XLyVaCvKhrSG89S1Gim0INX2YDYBvL0axLEHOACWz5YZH1jPlSBHJ4%2BSVBIcN34E4TymoENkg6BdTfHvUtAFb8F1j%2FrJpFxjtRm8CyokwuXJrjZ%2BOUqc2rEWJSlKnKvWz8z2jaBFfZq3VgnOOxO%2BH3pW1Iv4FICWWXleKqAQyEfN8ILT7FZ2I7FQXOYsRg6DhxFGkTvs50IooN0cuNRwVK9JxVcyZm58o82rj8BV0GNbZyhIu%2B6xQD0EwoLXwvAY6pgHGmWWWdCj3RgUSIBHWBbtO9BlD7QBvQBeeVWVe33azlROmXEeOC05VScCRTdEJjmGVLcp69g%2Fh7%2BxAbqiQE%2FUesaxEcRagDrin24jzlIMvCXB8m%2F%2BUupAs4H%2Fyzf02m9jhjkKvmaDuK3xEb5M5ViqsQFFdsv%2BoElJgOhY21yaYTb245mwLSv%2BdynV9Aid3fjKve9Q%2FrU%2BXaL4vT%2BjE%2FR5lumPtQAss&X-Amz-Signature=811fe68192924a9d256eea4f614c193fbb62ea1082bd585b90a65b4294e8e0d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXDQ27IJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEVe9lgliPljrTkG4TczqDnUIubuQFI9Zxpuy%2FuPXrAIhAPON5zv6odMVkq0EZFOerzSmXenUHaNsXAv4XkgJpc2PKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVCA9dPTqER1XcM2Aq3APmBxo4dlVRU6PAcAlj1bGKe3PRRCI8zb%2BLX%2BRZJR2cfha1tMY7rpCB3U2YQNK%2BlcmKYNYjP%2FNSv6vcRRmbhyMd8mna1a89IlWcVwe9kVdym5%2BzWhEd2kU1A0b%2BHwFELF62omUQRjO7PhGK88eT2%2BMJs6lVneM6ttuDVBL1gkDMiKmln5TLVBZoiPl7gn1WPVJHx0B9NeiIL222FptS3fGVSQzxGk%2BGNNI9mBO6a9fuBZbfp8hRJHhM4Rl4K4kcPDhIN1zHLwsmLtqydyaqjCwpB637eCO7lDXC%2FWJD7tVyo%2B4%2BfKH%2Bl0wnW%2BZiV2LCVZjAdXkh7AV2RU07q0%2F89TQ%2F8mtXN6HEHhTkmGoHOW8tEcR%2FNsz9HnxhrtKEbepYO2jy6HE9YqYp4P%2BBXjC0R8OcOnynsY9W1IVZUSK5RfPWm48mamdm5nUs1vzgYHal6X7QY7I5eXk9RmGZ5pPUxDu%2FeVcmZRnifENgQBzJgw%2B89hfk7lMdJ9K%2BST%2B3fGYXY0ahWMX1z%2FlCrScLHgKhX%2Fr5%2BLAuYuYi6feXdHimwUKrSZeIybJfcvyS%2BdQ5mtMOeibmsegR5AtyEVOPhd%2BnoCTp3zaiOP8O0ViamT5ooE7IvBGlum5uKR6hFw84DTCStfC8BjqkAc3wl076ivXWkab1yVV9Jj54Mj2uldwjlBhc%2BNfboZlz5AhXMhUJMGwmYYK4qf4OfFxiuGJzNAOA0Nia54ycHQ1e8in50wu3TU2MZtGgUV9bcq1zSbT5cweJIxD85gV8uHt7r8AViTzTfsomNcGz59T2hUQ%2FSR6rqVc7YdA0y1sxjj5dhBZb7DV4pLOR84g7mMHeMvBcIaaRB5LRyMoxRIa6cIgC&X-Amz-Signature=09c599d47fc17c882e112e8aa714e775b7d7af48eb4c6102e861e52db9c10c87&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXDQ27IJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEVe9lgliPljrTkG4TczqDnUIubuQFI9Zxpuy%2FuPXrAIhAPON5zv6odMVkq0EZFOerzSmXenUHaNsXAv4XkgJpc2PKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVCA9dPTqER1XcM2Aq3APmBxo4dlVRU6PAcAlj1bGKe3PRRCI8zb%2BLX%2BRZJR2cfha1tMY7rpCB3U2YQNK%2BlcmKYNYjP%2FNSv6vcRRmbhyMd8mna1a89IlWcVwe9kVdym5%2BzWhEd2kU1A0b%2BHwFELF62omUQRjO7PhGK88eT2%2BMJs6lVneM6ttuDVBL1gkDMiKmln5TLVBZoiPl7gn1WPVJHx0B9NeiIL222FptS3fGVSQzxGk%2BGNNI9mBO6a9fuBZbfp8hRJHhM4Rl4K4kcPDhIN1zHLwsmLtqydyaqjCwpB637eCO7lDXC%2FWJD7tVyo%2B4%2BfKH%2Bl0wnW%2BZiV2LCVZjAdXkh7AV2RU07q0%2F89TQ%2F8mtXN6HEHhTkmGoHOW8tEcR%2FNsz9HnxhrtKEbepYO2jy6HE9YqYp4P%2BBXjC0R8OcOnynsY9W1IVZUSK5RfPWm48mamdm5nUs1vzgYHal6X7QY7I5eXk9RmGZ5pPUxDu%2FeVcmZRnifENgQBzJgw%2B89hfk7lMdJ9K%2BST%2B3fGYXY0ahWMX1z%2FlCrScLHgKhX%2Fr5%2BLAuYuYi6feXdHimwUKrSZeIybJfcvyS%2BdQ5mtMOeibmsegR5AtyEVOPhd%2BnoCTp3zaiOP8O0ViamT5ooE7IvBGlum5uKR6hFw84DTCStfC8BjqkAc3wl076ivXWkab1yVV9Jj54Mj2uldwjlBhc%2BNfboZlz5AhXMhUJMGwmYYK4qf4OfFxiuGJzNAOA0Nia54ycHQ1e8in50wu3TU2MZtGgUV9bcq1zSbT5cweJIxD85gV8uHt7r8AViTzTfsomNcGz59T2hUQ%2FSR6rqVc7YdA0y1sxjj5dhBZb7DV4pLOR84g7mMHeMvBcIaaRB5LRyMoxRIa6cIgC&X-Amz-Signature=01656cf5772a035f510ab1eefb84802220836c6d38cb63dfbf306c8d9f523538&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXDQ27IJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEVe9lgliPljrTkG4TczqDnUIubuQFI9Zxpuy%2FuPXrAIhAPON5zv6odMVkq0EZFOerzSmXenUHaNsXAv4XkgJpc2PKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVCA9dPTqER1XcM2Aq3APmBxo4dlVRU6PAcAlj1bGKe3PRRCI8zb%2BLX%2BRZJR2cfha1tMY7rpCB3U2YQNK%2BlcmKYNYjP%2FNSv6vcRRmbhyMd8mna1a89IlWcVwe9kVdym5%2BzWhEd2kU1A0b%2BHwFELF62omUQRjO7PhGK88eT2%2BMJs6lVneM6ttuDVBL1gkDMiKmln5TLVBZoiPl7gn1WPVJHx0B9NeiIL222FptS3fGVSQzxGk%2BGNNI9mBO6a9fuBZbfp8hRJHhM4Rl4K4kcPDhIN1zHLwsmLtqydyaqjCwpB637eCO7lDXC%2FWJD7tVyo%2B4%2BfKH%2Bl0wnW%2BZiV2LCVZjAdXkh7AV2RU07q0%2F89TQ%2F8mtXN6HEHhTkmGoHOW8tEcR%2FNsz9HnxhrtKEbepYO2jy6HE9YqYp4P%2BBXjC0R8OcOnynsY9W1IVZUSK5RfPWm48mamdm5nUs1vzgYHal6X7QY7I5eXk9RmGZ5pPUxDu%2FeVcmZRnifENgQBzJgw%2B89hfk7lMdJ9K%2BST%2B3fGYXY0ahWMX1z%2FlCrScLHgKhX%2Fr5%2BLAuYuYi6feXdHimwUKrSZeIybJfcvyS%2BdQ5mtMOeibmsegR5AtyEVOPhd%2BnoCTp3zaiOP8O0ViamT5ooE7IvBGlum5uKR6hFw84DTCStfC8BjqkAc3wl076ivXWkab1yVV9Jj54Mj2uldwjlBhc%2BNfboZlz5AhXMhUJMGwmYYK4qf4OfFxiuGJzNAOA0Nia54ycHQ1e8in50wu3TU2MZtGgUV9bcq1zSbT5cweJIxD85gV8uHt7r8AViTzTfsomNcGz59T2hUQ%2FSR6rqVc7YdA0y1sxjj5dhBZb7DV4pLOR84g7mMHeMvBcIaaRB5LRyMoxRIa6cIgC&X-Amz-Signature=c0eb4a5d16bdd674192c48719906459659cb50af777bc0be0850881e5dc5e2fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXDQ27IJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEVe9lgliPljrTkG4TczqDnUIubuQFI9Zxpuy%2FuPXrAIhAPON5zv6odMVkq0EZFOerzSmXenUHaNsXAv4XkgJpc2PKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVCA9dPTqER1XcM2Aq3APmBxo4dlVRU6PAcAlj1bGKe3PRRCI8zb%2BLX%2BRZJR2cfha1tMY7rpCB3U2YQNK%2BlcmKYNYjP%2FNSv6vcRRmbhyMd8mna1a89IlWcVwe9kVdym5%2BzWhEd2kU1A0b%2BHwFELF62omUQRjO7PhGK88eT2%2BMJs6lVneM6ttuDVBL1gkDMiKmln5TLVBZoiPl7gn1WPVJHx0B9NeiIL222FptS3fGVSQzxGk%2BGNNI9mBO6a9fuBZbfp8hRJHhM4Rl4K4kcPDhIN1zHLwsmLtqydyaqjCwpB637eCO7lDXC%2FWJD7tVyo%2B4%2BfKH%2Bl0wnW%2BZiV2LCVZjAdXkh7AV2RU07q0%2F89TQ%2F8mtXN6HEHhTkmGoHOW8tEcR%2FNsz9HnxhrtKEbepYO2jy6HE9YqYp4P%2BBXjC0R8OcOnynsY9W1IVZUSK5RfPWm48mamdm5nUs1vzgYHal6X7QY7I5eXk9RmGZ5pPUxDu%2FeVcmZRnifENgQBzJgw%2B89hfk7lMdJ9K%2BST%2B3fGYXY0ahWMX1z%2FlCrScLHgKhX%2Fr5%2BLAuYuYi6feXdHimwUKrSZeIybJfcvyS%2BdQ5mtMOeibmsegR5AtyEVOPhd%2BnoCTp3zaiOP8O0ViamT5ooE7IvBGlum5uKR6hFw84DTCStfC8BjqkAc3wl076ivXWkab1yVV9Jj54Mj2uldwjlBhc%2BNfboZlz5AhXMhUJMGwmYYK4qf4OfFxiuGJzNAOA0Nia54ycHQ1e8in50wu3TU2MZtGgUV9bcq1zSbT5cweJIxD85gV8uHt7r8AViTzTfsomNcGz59T2hUQ%2FSR6rqVc7YdA0y1sxjj5dhBZb7DV4pLOR84g7mMHeMvBcIaaRB5LRyMoxRIa6cIgC&X-Amz-Signature=4122db7fcb19e661696123bec5a1e41e57718f8dfe42938520592c6d8cc6daf4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXDQ27IJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEVe9lgliPljrTkG4TczqDnUIubuQFI9Zxpuy%2FuPXrAIhAPON5zv6odMVkq0EZFOerzSmXenUHaNsXAv4XkgJpc2PKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVCA9dPTqER1XcM2Aq3APmBxo4dlVRU6PAcAlj1bGKe3PRRCI8zb%2BLX%2BRZJR2cfha1tMY7rpCB3U2YQNK%2BlcmKYNYjP%2FNSv6vcRRmbhyMd8mna1a89IlWcVwe9kVdym5%2BzWhEd2kU1A0b%2BHwFELF62omUQRjO7PhGK88eT2%2BMJs6lVneM6ttuDVBL1gkDMiKmln5TLVBZoiPl7gn1WPVJHx0B9NeiIL222FptS3fGVSQzxGk%2BGNNI9mBO6a9fuBZbfp8hRJHhM4Rl4K4kcPDhIN1zHLwsmLtqydyaqjCwpB637eCO7lDXC%2FWJD7tVyo%2B4%2BfKH%2Bl0wnW%2BZiV2LCVZjAdXkh7AV2RU07q0%2F89TQ%2F8mtXN6HEHhTkmGoHOW8tEcR%2FNsz9HnxhrtKEbepYO2jy6HE9YqYp4P%2BBXjC0R8OcOnynsY9W1IVZUSK5RfPWm48mamdm5nUs1vzgYHal6X7QY7I5eXk9RmGZ5pPUxDu%2FeVcmZRnifENgQBzJgw%2B89hfk7lMdJ9K%2BST%2B3fGYXY0ahWMX1z%2FlCrScLHgKhX%2Fr5%2BLAuYuYi6feXdHimwUKrSZeIybJfcvyS%2BdQ5mtMOeibmsegR5AtyEVOPhd%2BnoCTp3zaiOP8O0ViamT5ooE7IvBGlum5uKR6hFw84DTCStfC8BjqkAc3wl076ivXWkab1yVV9Jj54Mj2uldwjlBhc%2BNfboZlz5AhXMhUJMGwmYYK4qf4OfFxiuGJzNAOA0Nia54ycHQ1e8in50wu3TU2MZtGgUV9bcq1zSbT5cweJIxD85gV8uHt7r8AViTzTfsomNcGz59T2hUQ%2FSR6rqVc7YdA0y1sxjj5dhBZb7DV4pLOR84g7mMHeMvBcIaaRB5LRyMoxRIa6cIgC&X-Amz-Signature=a057d229cfc97dc71f9805ff8bdbbdea8a5abee1b51487b72b9cacad3b61ebbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXDQ27IJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEVe9lgliPljrTkG4TczqDnUIubuQFI9Zxpuy%2FuPXrAIhAPON5zv6odMVkq0EZFOerzSmXenUHaNsXAv4XkgJpc2PKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVCA9dPTqER1XcM2Aq3APmBxo4dlVRU6PAcAlj1bGKe3PRRCI8zb%2BLX%2BRZJR2cfha1tMY7rpCB3U2YQNK%2BlcmKYNYjP%2FNSv6vcRRmbhyMd8mna1a89IlWcVwe9kVdym5%2BzWhEd2kU1A0b%2BHwFELF62omUQRjO7PhGK88eT2%2BMJs6lVneM6ttuDVBL1gkDMiKmln5TLVBZoiPl7gn1WPVJHx0B9NeiIL222FptS3fGVSQzxGk%2BGNNI9mBO6a9fuBZbfp8hRJHhM4Rl4K4kcPDhIN1zHLwsmLtqydyaqjCwpB637eCO7lDXC%2FWJD7tVyo%2B4%2BfKH%2Bl0wnW%2BZiV2LCVZjAdXkh7AV2RU07q0%2F89TQ%2F8mtXN6HEHhTkmGoHOW8tEcR%2FNsz9HnxhrtKEbepYO2jy6HE9YqYp4P%2BBXjC0R8OcOnynsY9W1IVZUSK5RfPWm48mamdm5nUs1vzgYHal6X7QY7I5eXk9RmGZ5pPUxDu%2FeVcmZRnifENgQBzJgw%2B89hfk7lMdJ9K%2BST%2B3fGYXY0ahWMX1z%2FlCrScLHgKhX%2Fr5%2BLAuYuYi6feXdHimwUKrSZeIybJfcvyS%2BdQ5mtMOeibmsegR5AtyEVOPhd%2BnoCTp3zaiOP8O0ViamT5ooE7IvBGlum5uKR6hFw84DTCStfC8BjqkAc3wl076ivXWkab1yVV9Jj54Mj2uldwjlBhc%2BNfboZlz5AhXMhUJMGwmYYK4qf4OfFxiuGJzNAOA0Nia54ycHQ1e8in50wu3TU2MZtGgUV9bcq1zSbT5cweJIxD85gV8uHt7r8AViTzTfsomNcGz59T2hUQ%2FSR6rqVc7YdA0y1sxjj5dhBZb7DV4pLOR84g7mMHeMvBcIaaRB5LRyMoxRIa6cIgC&X-Amz-Signature=4b5a486648765e939b0ac5638086d216f78ea2041b9c248a4e0b2824913ca7a7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RH5XZUMH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHewarfgdlK559PK7j2rSgo%2FO0C0EWNoRyUIuLRev9rOAiBsV8li8B%2BbpzTW1nLk4atz6w%2BTkIQRXdc1wZa%2FZMOAnSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLp%2BGJMhaIG5ojh3wKtwDxIWmtcBVpH0rVtRdmSLz55TTXsTtHQotJszmVu7%2FyhofLAKNqKzf8SiWYhvNhHcvn296uDWbs3epMVtrTdqLP5zB0So2UrYKgS%2BX1S2PEFyNUnvBkg1mwvz1aV1NcSgmsMHzG5nMIDFmLZ4rk53Ej3lYH9hxYKRSxhlHH%2F8tirdagBYTkfUgMPHRLOYRdrTv4hFv9R0q3aA89NogR5HFhx%2BfJWtjId6hvDfkiqNbeTUtq8ZgUHhmuTwwRHg9Keno3n%2BWmE%2Fs8zlCVmHiP6nZmO44cdUmh3qrQAdwSuTvmPeUkD2m1nNONizbMQawlJPqTVvGlGCRAdlW82px%2Fgbq5xxsbG6Dvtf4FpBI%2BjeejT6ZK7SiPg6gdZHN3SpPYoW4E4eMStF8VGVC1NMGkPcTWC0J%2BwUBvmZSsIK5kXeD4%2BFT4McK4yZ%2BNfhQFEWyHUWUxeUp64byiNnc8y3q5N5SrTRL%2FDarW02iIcIehAPQloFd%2F4xc5l%2F%2BfqGUfj49Vt0yG%2FS%2FK11CrzgJTax1uYW%2FbHcsmhJF5U6FJ6TUkM7HJKfnq1Eq5MDb4OhHTuTVE4FkDkRlKxqoONvH4nook9n5wOwCfNhyTcvCcY2t51qnmG8nyELurCBDsSPMgfkwl7XwvAY6pgF4HqsaZzs93gsIZpMdmSRBOyfFu%2BSpTaAhvIS3xagpVkZnp48II3CCIyA8djtwtKT%2BJzIaTO7Yg4Oz25KJhuiw1hP1m9eQ8Hvq5txz2OcI41RoO0tcPTJ6hbXNF4gY9iYq3yZASKYHqqW23N3gO4Q%2FMipko8etazpY6xEAkSmGAoL%2FihBBqJjbvO9fP8K6kj3yDhZpjfZSZhKKBC7gHP%2B%2Fi4eJGFNF&X-Amz-Signature=28220bec722d46525bd352154304425df51acc515c7518776cae2e725b72b505&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGDOLG2G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIARPqOm5SOB1I51jnd4zvmFcJw8PUUCI7c0QMOHHUT%2FwAiEAgsw%2BdcGIHX%2BUHaxmJe4KrOmQoj8GLGKXLkWiz7QD5JAqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN07EfA0VZ0B%2BWMuJCrcA3ToJKKRnTPLlGYpMXsOEqGXFRCzgv1wh1ROdi0qLqf2SMauphg3t8fuRRljS9KoY051smL8tDhXq79VmyMt%2B3RTnStzLhZ0XFt1gRLN35yiPqZxBQE5Y3kKwgVb0e3Ijm2dYXNMdGTJ3DfbqL7745pYKLOoBWdN0tLvHK4f3vkINzixu%2B6%2Bl0HGV0aZrEG3JvdjLNkd472JUlo12%2Bye3zPJuv5ohiadFAZlX%2BwipS3iArRI%2FKVgerC%2FbHVWuVTuc3WzFUvz7Urv0EtbFzDqDMwBDwFsVbKolXlK1BKG2OhiD2cjwFwaNx9L634lGi8EuxmYDMm4%2F6Kfvct61%2BkRF45O2Kbg5MCgpX61CNBWWb%2Bd8lElFE7RfMvvizEmL9z0fqxWRXLmzOkk03N6YEjTm15dWqkGq2qgyz5Kf5aHYp3i91NeWeijQWySLvEBpxVZglOiumZ0Osf84FNYA3WLLbNj%2FNxS1sxifR2GEU5gDkPS6Bt1XTk8%2F9Uncm184pHv51CmoAmw01aN%2Bnk1LN6XTwKGs6E9IGzb8tT%2B2BIlENX8W85W%2F9N7Ur12KznacJZlfxFvZ6%2BZ0d5k%2BT0Y4u67dKqk0epg0vQIQ7FZFi%2FqBopwfGvEoGCkFbchRpKsMKK18LwGOqUBbhIBxBg%2BpMWgxBGas32JazVsRyY8%2FjEplSy7MocBYiTav0RkCU15j%2BsZYcnrmOK37EhjEw6sBKj2RmN2JtHk6PIfj6bxy%2BCvzx5OlDLFjw9bwm%2BYLuK6HkZcoNPVbK20zxsWlyM%2BbOApMq%2Bevsg5%2BXoJf2zhhBa0nwdUbreEm5LwBEdKuBkZnvRLZ7lJC8df2S8Jl8j1gWP3faDLfq1IRmiw%2FOxb&X-Amz-Signature=daebdd52344b84d71fb09841d5725f45b4ddd45197e386b627f6663fecc5dc71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXDQ27IJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEVe9lgliPljrTkG4TczqDnUIubuQFI9Zxpuy%2FuPXrAIhAPON5zv6odMVkq0EZFOerzSmXenUHaNsXAv4XkgJpc2PKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVCA9dPTqER1XcM2Aq3APmBxo4dlVRU6PAcAlj1bGKe3PRRCI8zb%2BLX%2BRZJR2cfha1tMY7rpCB3U2YQNK%2BlcmKYNYjP%2FNSv6vcRRmbhyMd8mna1a89IlWcVwe9kVdym5%2BzWhEd2kU1A0b%2BHwFELF62omUQRjO7PhGK88eT2%2BMJs6lVneM6ttuDVBL1gkDMiKmln5TLVBZoiPl7gn1WPVJHx0B9NeiIL222FptS3fGVSQzxGk%2BGNNI9mBO6a9fuBZbfp8hRJHhM4Rl4K4kcPDhIN1zHLwsmLtqydyaqjCwpB637eCO7lDXC%2FWJD7tVyo%2B4%2BfKH%2Bl0wnW%2BZiV2LCVZjAdXkh7AV2RU07q0%2F89TQ%2F8mtXN6HEHhTkmGoHOW8tEcR%2FNsz9HnxhrtKEbepYO2jy6HE9YqYp4P%2BBXjC0R8OcOnynsY9W1IVZUSK5RfPWm48mamdm5nUs1vzgYHal6X7QY7I5eXk9RmGZ5pPUxDu%2FeVcmZRnifENgQBzJgw%2B89hfk7lMdJ9K%2BST%2B3fGYXY0ahWMX1z%2FlCrScLHgKhX%2Fr5%2BLAuYuYi6feXdHimwUKrSZeIybJfcvyS%2BdQ5mtMOeibmsegR5AtyEVOPhd%2BnoCTp3zaiOP8O0ViamT5ooE7IvBGlum5uKR6hFw84DTCStfC8BjqkAc3wl076ivXWkab1yVV9Jj54Mj2uldwjlBhc%2BNfboZlz5AhXMhUJMGwmYYK4qf4OfFxiuGJzNAOA0Nia54ycHQ1e8in50wu3TU2MZtGgUV9bcq1zSbT5cweJIxD85gV8uHt7r8AViTzTfsomNcGz59T2hUQ%2FSR6rqVc7YdA0y1sxjj5dhBZb7DV4pLOR84g7mMHeMvBcIaaRB5LRyMoxRIa6cIgC&X-Amz-Signature=4f67166746b756056bc2dda20e2852dae6d0e573e9137de10e9a080a4bbd6a01&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXDQ27IJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEVe9lgliPljrTkG4TczqDnUIubuQFI9Zxpuy%2FuPXrAIhAPON5zv6odMVkq0EZFOerzSmXenUHaNsXAv4XkgJpc2PKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVCA9dPTqER1XcM2Aq3APmBxo4dlVRU6PAcAlj1bGKe3PRRCI8zb%2BLX%2BRZJR2cfha1tMY7rpCB3U2YQNK%2BlcmKYNYjP%2FNSv6vcRRmbhyMd8mna1a89IlWcVwe9kVdym5%2BzWhEd2kU1A0b%2BHwFELF62omUQRjO7PhGK88eT2%2BMJs6lVneM6ttuDVBL1gkDMiKmln5TLVBZoiPl7gn1WPVJHx0B9NeiIL222FptS3fGVSQzxGk%2BGNNI9mBO6a9fuBZbfp8hRJHhM4Rl4K4kcPDhIN1zHLwsmLtqydyaqjCwpB637eCO7lDXC%2FWJD7tVyo%2B4%2BfKH%2Bl0wnW%2BZiV2LCVZjAdXkh7AV2RU07q0%2F89TQ%2F8mtXN6HEHhTkmGoHOW8tEcR%2FNsz9HnxhrtKEbepYO2jy6HE9YqYp4P%2BBXjC0R8OcOnynsY9W1IVZUSK5RfPWm48mamdm5nUs1vzgYHal6X7QY7I5eXk9RmGZ5pPUxDu%2FeVcmZRnifENgQBzJgw%2B89hfk7lMdJ9K%2BST%2B3fGYXY0ahWMX1z%2FlCrScLHgKhX%2Fr5%2BLAuYuYi6feXdHimwUKrSZeIybJfcvyS%2BdQ5mtMOeibmsegR5AtyEVOPhd%2BnoCTp3zaiOP8O0ViamT5ooE7IvBGlum5uKR6hFw84DTCStfC8BjqkAc3wl076ivXWkab1yVV9Jj54Mj2uldwjlBhc%2BNfboZlz5AhXMhUJMGwmYYK4qf4OfFxiuGJzNAOA0Nia54ycHQ1e8in50wu3TU2MZtGgUV9bcq1zSbT5cweJIxD85gV8uHt7r8AViTzTfsomNcGz59T2hUQ%2FSR6rqVc7YdA0y1sxjj5dhBZb7DV4pLOR84g7mMHeMvBcIaaRB5LRyMoxRIa6cIgC&X-Amz-Signature=c084b92f692a7cdc70c3c18e3f8d05877acaa822073ef6fa0515cdf8995bf1f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXDQ27IJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEVe9lgliPljrTkG4TczqDnUIubuQFI9Zxpuy%2FuPXrAIhAPON5zv6odMVkq0EZFOerzSmXenUHaNsXAv4XkgJpc2PKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVCA9dPTqER1XcM2Aq3APmBxo4dlVRU6PAcAlj1bGKe3PRRCI8zb%2BLX%2BRZJR2cfha1tMY7rpCB3U2YQNK%2BlcmKYNYjP%2FNSv6vcRRmbhyMd8mna1a89IlWcVwe9kVdym5%2BzWhEd2kU1A0b%2BHwFELF62omUQRjO7PhGK88eT2%2BMJs6lVneM6ttuDVBL1gkDMiKmln5TLVBZoiPl7gn1WPVJHx0B9NeiIL222FptS3fGVSQzxGk%2BGNNI9mBO6a9fuBZbfp8hRJHhM4Rl4K4kcPDhIN1zHLwsmLtqydyaqjCwpB637eCO7lDXC%2FWJD7tVyo%2B4%2BfKH%2Bl0wnW%2BZiV2LCVZjAdXkh7AV2RU07q0%2F89TQ%2F8mtXN6HEHhTkmGoHOW8tEcR%2FNsz9HnxhrtKEbepYO2jy6HE9YqYp4P%2BBXjC0R8OcOnynsY9W1IVZUSK5RfPWm48mamdm5nUs1vzgYHal6X7QY7I5eXk9RmGZ5pPUxDu%2FeVcmZRnifENgQBzJgw%2B89hfk7lMdJ9K%2BST%2B3fGYXY0ahWMX1z%2FlCrScLHgKhX%2Fr5%2BLAuYuYi6feXdHimwUKrSZeIybJfcvyS%2BdQ5mtMOeibmsegR5AtyEVOPhd%2BnoCTp3zaiOP8O0ViamT5ooE7IvBGlum5uKR6hFw84DTCStfC8BjqkAc3wl076ivXWkab1yVV9Jj54Mj2uldwjlBhc%2BNfboZlz5AhXMhUJMGwmYYK4qf4OfFxiuGJzNAOA0Nia54ycHQ1e8in50wu3TU2MZtGgUV9bcq1zSbT5cweJIxD85gV8uHt7r8AViTzTfsomNcGz59T2hUQ%2FSR6rqVc7YdA0y1sxjj5dhBZb7DV4pLOR84g7mMHeMvBcIaaRB5LRyMoxRIa6cIgC&X-Amz-Signature=27f795558e5a0770f6b470682a16dec74d1fea4e0679355fc79a25706fe57cfd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466657OA6LK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNmJl2wSQ01ZVAX22oxe3DtPbPWWhqeZ1IHDdKcqM6ZwIgXczXLFdDcuRAio6P%2FeJnqqP3GvjFH2DYTmiPbqZbyaAqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDoOqsb5oZN80GFHsSrcA%2F%2FqOYD%2FWZ9jGZ9XCWYtaFiI38k8uuOni%2FA319vRvCM8ATWdcujNauSIZTaPERCjHwCgCaQwhkXt3PlmFIArGiIxIgds3fBtPNej03XTVVzah5BfLlmGX%2FKEOPSnAr240Zb%2F5iDVyhW8ewrkGOTG0gi58MX7p%2FjfsAIDI6v%2Fo%2Fk6qFIbAUEEqXXkvoxnjf8aVkWPENBk5HTy9jZlC%2F0dgg7UFr8RCGV%2F7q10t267waSK3%2FhnklX7StWnF85Ar5jndAsGhwgX4PurbDE5Tnhwl7K%2F4xU7X7bVHMK8%2Fgwd6cxzlFtt54TrQwqCYFkosiJUcGih8EtcgO6zVAO83opXLs6kjvU8w5s52v%2Fn7oZP7ct%2FCu81eBZxfPtHUjKBm9gCWYcSP0Nzr68fymCKzCmQUtv5dsYK7%2FWfVdVzgmaujaz9JFIxjdqeQPALEK%2F5OlNsxqpwJCmiQrweI4VDdGhobhXoguLHWAJ2pD3E60tzQcak3MqGqTiCoG%2BYfDcBamYXZnZw9wEiAtJJqKNkumSJ2QZURb3ZvSTrfHrCN1%2BWazSylu3MJt8m8VbaXqhFUM21jsXzECziUjHMzpKUq8gaKJWRocIjb9X5LHoFx4ZivG2FrirIT8TnZ9OUgDaNMNG18LwGOqUBhMY1dtJe20%2FTdGzju8%2BpBeovhMkmJINvPQnGKQerJSdT%2Fbs%2BOZgu6Uxe%2BQoNdY%2BXdH4rOt1lAUwSQaNq%2FfH4mmWzZOFbtZLL2DXUPwOJtSKsEcgF7fdt5kd8%2BmDuIR2Hvg8GMk1aLlkV2lytsb4%2Fbcu2gyEmYOyJLwbfllRFNPsQ7l5nEA8M8LC%2Bcyq0ll5KE%2Fkom1A3qXIfW6A5harE3N13v3bE&X-Amz-Signature=bee40bfb5eec645de1e943daf96c215074644a52b5739d3f6123fa18497df2e4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662BEJQGU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmM7j7aLZrbWlwkDbuy3m8t0YyyhSPtkhhhAgTIdnYBAIgM%2BpOoqz9rZH%2FYbyE1qs0L4pApXTc%2FGpQVu9fJBkb%2FsEqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB7uE99LSaM5gyOcKSrcA8RO1rM5jLs3cit6jOKWeRkXcT5pf4mqa8Vx3HoIqYBws3%2F3ZF%2BVSLXQceUiGuvE6oOa2Mt7nvc799LLexrQA0vChIoiHIRbLxg6ChM1qHKBj0hNJoe5q4XMQsTln4MR4%2Fxi%2BXBHPlGRSBw5tTbYJC0HvaI9IDFFClTcsiXNwlafInCguoNsGbr3ec3MFkXpNzVtYwJtlqeHrhAnTxwDClI8yJQzZkokxW1uaOWImJOld3XYEefcha%2F7TqSrOtE71c0EFIoNVLtNX8aJTPBELF%2BH09cQA2RqYvtb%2Fy9AIriDeNXGZzqk48B3zik5g2peik9csMuRLihyd4DLNf%2FfvRAyfxaVj6grchBwxpsDrNFggM3ONAwRPEoEPlLlTKQJM5ROQyRKcfmHjzmxDbcXnE8DTLsnRTA364XDHxrtYBQPJoWg2IX1sb1GLiyx0ENRIG76EQmVM%2FKwx4jW06wE11zrDJesZ1x9PlX%2BQmzjQrBiS3MXGxwWaE3ragfVaBLKMC5SbzrOv5%2BLXM4Boiy0AzWQh19Sp32omBVgxy9O1t36euhX2SI78Gyk5gn8aBkL5naVg19LEHTr5L5z77%2B%2FpOsv6DEIqLxsRYyPFDSnr7UyGXaTEInK%2BpAWcJ5%2FMJG18LwGOqUB%2FWMCT5PPU5tl867dl4LjyNjjlgob20ULyBn%2FE8QvFnEQNGzlOrKKFVrokmGSLYL88HZvhglpKXnBnOegw0hke1dnTJwtO5Qm7PsJIIrgyTqiD%2Br7OMKiB0eILN7nLrBSn%2F0cy7iBtV7aQMHNHBdWnzKHm%2Fe8nRSmFQ5GRdheXKIT7ZBic%2FLOYvBSEPRY%2B4WGqRjq48egqfstZbGXpx1YnUAkTCAl&X-Amz-Signature=0531490301243f5225260a7c73b44e2b35f0272e4e288b071727771003636c35&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NWPHA6L%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfDIBjMUVXqZFdDb0%2FYOviBGUYRYfVeTXYKKMY2pR%2BKAiBnajrJZI386v5dFGUUSyilev0YcKXX6Pd2CWI6tEZriSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeAF1CG%2FhHIlVwHSbKtwDFVvFHwfAyQF4ApxRoc7crB4fEQqA9KM6TvJgUxAxqvUHUFIDoBYzRyxaJg%2FFqCuqzdYupxP11Qm9TrrNyVjGRVMAc17mCQop%2BEvzLX2%2FIXOC%2FSlSGIyqRiySd6cuOsMQUdc17bl6baEqckvQl25OqfgkUVA%2FR2qRzvwVWXyShk%2FXZrIXedMpBXLTc41K0z1%2FGozuPYiyoPZQh8GFU%2BexPaMOtXw7tymvvO1M9lk74Yi%2B8Qj0T6A9Q%2BCEXjUWWe62jrXio7e6VLwOiQ8XXxAMAEBYD5XnREkOr%2F%2BGWRhFjV%2ByVR5MzAbjZqb7ScibCWLy89WG3W2nlLY0U8D7gfP8A019j007Hf06Zm1OWQPqQnaZfERIHUJjqcWOJTQzm7%2ByIf40TZLDF90bVr4jW4clbdF7cr7inLAaiL4TPgCzJmXFW6G6sxOe60Oc8R9YfyerVYFtUrqS6CyvQcvUagx0RwoJS9I%2F3pyEp8gafk6IjBTdijI8YZYKMKhxPC%2Fsxw6e2n42Nd0GIu1TZv1glcfZ%2FZBbKQ0mRGZxqeSTejx%2Fz2bTqGbMcih27zDpTeVNPU4KtexsPwvPJyvg9MZVrdKwUjGPCxSKw2KTT5li9gJIWYUfiNxK99nvr9y9vPkwqLXwvAY6pgHQ62tjtZXbhx0G7Wm4TrmyJ%2FKM5vzz%2BXVYoRdi%2BVVDoUK3neVj5BxuTRdTKqPkvYUqcvAD0RZNpZOhB8YO5BF2uxb0kQhcKd9VjC0szp61ps1WqDZS20m%2BG%2Be3MArbS%2FvAvUej4UVoasN9IlpFM%2FnoeUf1zBWHaBT%2BaqX%2Bo5OGXmbHHmYL3BfgIREYSoTiAXlc3XeG9RGhTKEOoUCdIh%2BhoeeNe3NF&X-Amz-Signature=8ed54bfa1741ac4ce16a8068bb9daf775e0f2bb5ec15f7a12b6782e3748c3b72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DPRQ7ZH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICgKY0aPUVJFSDZ1m%2FMwuey%2BEnnlRPQsK125KxjFbF9OAiEApaQZ%2FavbDzbkoNTNr6AFugVvnGqd2GS11AVWGNE%2Bk9YqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRpY4avuJip5tEbJircA2rHrbfTgGsAishPRDjAXWyJ1E7WIE1t1XCkDCPKelZkqIYqGL9Oc09ELPVDa%2BgEbCVjnVCc9hl8xhyo%2BTNDQSVYb4ridM3Izbp73w07aLvLzvae6haYXU%2BsqCZSCu8UyHo91mKjYLTEHJIlzZa2ZkwzUNZnuBtf%2B9nnnrGlBDDu8malHza4xPeYxKbheCEQeZ6L4742hjYwfgt%2BKqckIGhdkETnOK21I2u4M8qsHnAS%2FPwxKGWzzZRD83pSjXnKnY7qKYigImxS0xNV3IUQ9ujWGCwb5QBWuZb%2BMk1r2zvXqPT7FAouZZdn2pmSfpXaRa53TfPpb2QEQPXi%2Bse83gVHpC8Xn2NKBmvRl6xvR9esbL6On%2Bgy75ofI50fw5jdp6KCHzXdosjrmpUI5FsmgKlTEZQ03p2WHAPHUQyVoZnP%2BqZhxJzH2PU2d55jtOzzYIobI2R4miIzxIK49ju9zFBlJi8KPuDEdTMohShcxNshRAFrD2wmbt3hM5pfyWXmmVxyBv5yAuQhUiNraHwa2bXknpoOgOWOg9DFDgvBMCYK60yw90ZJXMhOrgFb8oMxSXLiL2V%2FAmJZuKaafSoa96Rw3sRJ%2Fr%2BJz5xjTmJZ2LIZUhoQK6EDOyGRAdh%2BMM608LwGOqUBVJ0jV8xO2FKwmaiovoK6bK92tgJjxIzScv%2Fcj9%2BuzThden1aSj0QFgyfEgU%2BDeHyslD50oA1TtG%2FbTO5w4FcdiXdsa9tDyq0YvU1cX4VSqQzFnUVPy0xTFoLpyU0uWJKxB8xQjRzvBPhiE4JH74VPX5vTO55A9WPj9t8hUa4w3rIP0yIzU4mEF5xYryP24hZvSTTOmWhOQyx7kQtcORWt85pKDpV&X-Amz-Signature=d80315f073ee79150e127ae9eb576b82a528dec309dfda58202ff122dd7c0cbc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DPRQ7ZH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICgKY0aPUVJFSDZ1m%2FMwuey%2BEnnlRPQsK125KxjFbF9OAiEApaQZ%2FavbDzbkoNTNr6AFugVvnGqd2GS11AVWGNE%2Bk9YqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRpY4avuJip5tEbJircA2rHrbfTgGsAishPRDjAXWyJ1E7WIE1t1XCkDCPKelZkqIYqGL9Oc09ELPVDa%2BgEbCVjnVCc9hl8xhyo%2BTNDQSVYb4ridM3Izbp73w07aLvLzvae6haYXU%2BsqCZSCu8UyHo91mKjYLTEHJIlzZa2ZkwzUNZnuBtf%2B9nnnrGlBDDu8malHza4xPeYxKbheCEQeZ6L4742hjYwfgt%2BKqckIGhdkETnOK21I2u4M8qsHnAS%2FPwxKGWzzZRD83pSjXnKnY7qKYigImxS0xNV3IUQ9ujWGCwb5QBWuZb%2BMk1r2zvXqPT7FAouZZdn2pmSfpXaRa53TfPpb2QEQPXi%2Bse83gVHpC8Xn2NKBmvRl6xvR9esbL6On%2Bgy75ofI50fw5jdp6KCHzXdosjrmpUI5FsmgKlTEZQ03p2WHAPHUQyVoZnP%2BqZhxJzH2PU2d55jtOzzYIobI2R4miIzxIK49ju9zFBlJi8KPuDEdTMohShcxNshRAFrD2wmbt3hM5pfyWXmmVxyBv5yAuQhUiNraHwa2bXknpoOgOWOg9DFDgvBMCYK60yw90ZJXMhOrgFb8oMxSXLiL2V%2FAmJZuKaafSoa96Rw3sRJ%2Fr%2BJz5xjTmJZ2LIZUhoQK6EDOyGRAdh%2BMM608LwGOqUBVJ0jV8xO2FKwmaiovoK6bK92tgJjxIzScv%2Fcj9%2BuzThden1aSj0QFgyfEgU%2BDeHyslD50oA1TtG%2FbTO5w4FcdiXdsa9tDyq0YvU1cX4VSqQzFnUVPy0xTFoLpyU0uWJKxB8xQjRzvBPhiE4JH74VPX5vTO55A9WPj9t8hUa4w3rIP0yIzU4mEF5xYryP24hZvSTTOmWhOQyx7kQtcORWt85pKDpV&X-Amz-Signature=556869b63f0fd69c924a22ee77d949f561b403fcd5e5d5973bd40d65820a4a06&X-Amz-SignedHeaders=host&x-id=GetObject)

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
