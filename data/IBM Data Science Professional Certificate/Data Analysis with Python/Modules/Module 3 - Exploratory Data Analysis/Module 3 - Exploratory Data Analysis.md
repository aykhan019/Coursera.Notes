

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G7HO3WT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDmmjgODWvoXxJY278OR3baVSdmDG%2B2Bvb18nCqgAnSfQIhAPAfRyBYVlPSrbnP74RRfQbp5y5%2Bfut9YHd5%2BF9me5HoKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzeB8QvthKtdvqapQMq3AOrcMrZdBSSkGpZkmtDo0KE3KnG%2F2tFB3HBqkGVdvQvT7yRg5qDCR81c4Y8NrWiCtnBEjFt2mMLinnwBA0r6gHKTG%2ByTrngUKp4d5QH2d2cIty3w7fpq7UFYX4cnt9vWwyuUFd%2FPND2dfwQKgoTxJ58r8Igqwha94JDf%2FGSlHJZf9LSgijkiZihmbC8VuMWDU3nFcxpzpdo0bZGuDfttBE6v7HQwfXBUrqthgyZsBmmd88ElDfmfaaO8cq99hQzoVmd9YhCiAxjPDVVRRG01%2BWuzo00pXxJSnw239gpkkFBz8uFa%2BJA7BiCldClJLjXBxusWRDsrcg0bYuUKr9RyTxGpUGBqB%2Fwfz1RVGHljXqmOP5fx4uc2UNmk4wiT%2FfS3GD6fHRTIspoJ%2FbHJJ2MRj%2BewSi1LDgxQvht75DjrhlBsZXAKxsm31%2BywYjezg%2Fj2%2F7JhiYwyhGDlDAgXdLbSHhr%2Bd9wNf7kTDjJFKoKtICryLdWaztW6vxaY6DUDHisOywnOvr5MwuzU3uILO5L3CAkSDjUKeH%2FeaBqGDbiLt4Sk%2B90N0wTxZtw0VtlTH%2FopW4bwhGPE%2BrxKClT9PturmZzN%2BsprKPuct4Ryd11atmVh0cN49lH3%2FNaoNB15TCf3fa8BjqkAT%2BbsBuy2kcQny9PjTTeHBEXgnQQ7QcpRmJt19jcgG2KQskgLAtCbmFI7WrFsR2l%2BjmgtWK1OodHL6Qj%2Bc9J211VTYfSmY7cO7p7r%2FgQVVpJN9j8gSVW35Oc865Rwz36%2Bc6W%2BCQl5UOvcy0kBhGLaN5v1e5kkt3CfZKOozFmd7ApG7oKARGJIgXU8G%2FpE%2FUDKUD49LR0alodpHVhFVZkCav2R54o&X-Amz-Signature=282fd74c66f1da85d069e972a9fde1d5d17dc15e70a9675dcc5ca88d6745564c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G7HO3WT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDmmjgODWvoXxJY278OR3baVSdmDG%2B2Bvb18nCqgAnSfQIhAPAfRyBYVlPSrbnP74RRfQbp5y5%2Bfut9YHd5%2BF9me5HoKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzeB8QvthKtdvqapQMq3AOrcMrZdBSSkGpZkmtDo0KE3KnG%2F2tFB3HBqkGVdvQvT7yRg5qDCR81c4Y8NrWiCtnBEjFt2mMLinnwBA0r6gHKTG%2ByTrngUKp4d5QH2d2cIty3w7fpq7UFYX4cnt9vWwyuUFd%2FPND2dfwQKgoTxJ58r8Igqwha94JDf%2FGSlHJZf9LSgijkiZihmbC8VuMWDU3nFcxpzpdo0bZGuDfttBE6v7HQwfXBUrqthgyZsBmmd88ElDfmfaaO8cq99hQzoVmd9YhCiAxjPDVVRRG01%2BWuzo00pXxJSnw239gpkkFBz8uFa%2BJA7BiCldClJLjXBxusWRDsrcg0bYuUKr9RyTxGpUGBqB%2Fwfz1RVGHljXqmOP5fx4uc2UNmk4wiT%2FfS3GD6fHRTIspoJ%2FbHJJ2MRj%2BewSi1LDgxQvht75DjrhlBsZXAKxsm31%2BywYjezg%2Fj2%2F7JhiYwyhGDlDAgXdLbSHhr%2Bd9wNf7kTDjJFKoKtICryLdWaztW6vxaY6DUDHisOywnOvr5MwuzU3uILO5L3CAkSDjUKeH%2FeaBqGDbiLt4Sk%2B90N0wTxZtw0VtlTH%2FopW4bwhGPE%2BrxKClT9PturmZzN%2BsprKPuct4Ryd11atmVh0cN49lH3%2FNaoNB15TCf3fa8BjqkAT%2BbsBuy2kcQny9PjTTeHBEXgnQQ7QcpRmJt19jcgG2KQskgLAtCbmFI7WrFsR2l%2BjmgtWK1OodHL6Qj%2Bc9J211VTYfSmY7cO7p7r%2FgQVVpJN9j8gSVW35Oc865Rwz36%2Bc6W%2BCQl5UOvcy0kBhGLaN5v1e5kkt3CfZKOozFmd7ApG7oKARGJIgXU8G%2FpE%2FUDKUD49LR0alodpHVhFVZkCav2R54o&X-Amz-Signature=9966a22a6d5c5b1e162e546719128d794d2f0fa40d2961d4d23b78a19f107294&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G7HO3WT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDmmjgODWvoXxJY278OR3baVSdmDG%2B2Bvb18nCqgAnSfQIhAPAfRyBYVlPSrbnP74RRfQbp5y5%2Bfut9YHd5%2BF9me5HoKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzeB8QvthKtdvqapQMq3AOrcMrZdBSSkGpZkmtDo0KE3KnG%2F2tFB3HBqkGVdvQvT7yRg5qDCR81c4Y8NrWiCtnBEjFt2mMLinnwBA0r6gHKTG%2ByTrngUKp4d5QH2d2cIty3w7fpq7UFYX4cnt9vWwyuUFd%2FPND2dfwQKgoTxJ58r8Igqwha94JDf%2FGSlHJZf9LSgijkiZihmbC8VuMWDU3nFcxpzpdo0bZGuDfttBE6v7HQwfXBUrqthgyZsBmmd88ElDfmfaaO8cq99hQzoVmd9YhCiAxjPDVVRRG01%2BWuzo00pXxJSnw239gpkkFBz8uFa%2BJA7BiCldClJLjXBxusWRDsrcg0bYuUKr9RyTxGpUGBqB%2Fwfz1RVGHljXqmOP5fx4uc2UNmk4wiT%2FfS3GD6fHRTIspoJ%2FbHJJ2MRj%2BewSi1LDgxQvht75DjrhlBsZXAKxsm31%2BywYjezg%2Fj2%2F7JhiYwyhGDlDAgXdLbSHhr%2Bd9wNf7kTDjJFKoKtICryLdWaztW6vxaY6DUDHisOywnOvr5MwuzU3uILO5L3CAkSDjUKeH%2FeaBqGDbiLt4Sk%2B90N0wTxZtw0VtlTH%2FopW4bwhGPE%2BrxKClT9PturmZzN%2BsprKPuct4Ryd11atmVh0cN49lH3%2FNaoNB15TCf3fa8BjqkAT%2BbsBuy2kcQny9PjTTeHBEXgnQQ7QcpRmJt19jcgG2KQskgLAtCbmFI7WrFsR2l%2BjmgtWK1OodHL6Qj%2Bc9J211VTYfSmY7cO7p7r%2FgQVVpJN9j8gSVW35Oc865Rwz36%2Bc6W%2BCQl5UOvcy0kBhGLaN5v1e5kkt3CfZKOozFmd7ApG7oKARGJIgXU8G%2FpE%2FUDKUD49LR0alodpHVhFVZkCav2R54o&X-Amz-Signature=270245a807e9724e66dbb97b9848afe38832d4d367890013266c799a9c858f32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5UU4ZP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdQ11hctu%2Ffgg4SzNc7xxWzbp3sB1XAOOv%2ByEbCXjrLAiAGVQUAudgneFD%2FQhXAmzbFC7p5ZZlj5mxfe%2BNZP9kbIyqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTg8oyXwp%2Bs4Xx%2FasKtwD5i1ufIjbO1ycoKJplYG4hUtIFbAbUCQg8ReSC6BEfooMW%2FKTyKXTVN6Cqo9Ynxsexq4MnTKIBkf1UiDrTpctsuMkTo9YcFHU%2BoQ6nl1gKDLAkUi3iWZiIpeO3aIYxDXbz0MGlUzCX8Ek9NJhCo7vF1%2B6P%2BZ7%2BqNcRhhiD3mxeRsvqTIHqr1FLLXPk0LgLNxbRrTDPtKfbWzwwRoZGf%2B0X4lFGp0xhp8DLosaBn%2FKRhY6oqhF8buyRXmaMfcwENwRc7WFwyF%2FJ7xFyyy2I2E5GTzOd%2Bu3tNsF54ypH4AZSDUBl4XzfEPtC3LZNM7t%2FAUgPIq5851Q%2BCTnicEJeOmDn3VpUT3AM203m3heraWyb9dCgFfqewyc55IuR0OL3%2B%2B0pRoS62nsx7QWpX7jp8%2BnMrm4hU3OQoFMdQj%2FHPZcPY75MLObBi7OmmI1qv9uV9azKHZTQ9aIqNbK2uiOTO2y%2FVvPLddEuNJEuqf9OcC7TfWg%2FqzFJgJObaapdBuDhUiNfQCyZazKu9%2BollCXVEk%2BnChnSHPZsyCVUCsULoeWFj4PVzXXA%2B%2BnHU90HPGvKntU61wVpqrQHE3fxvERxK4moHmZZWCZaQiaK4f2JsQ1S%2F7OGyag%2BRO79GUpQKcwyd32vAY6pgE%2FsHxa3XGMF3smQRSfTJ3D7obHVsgLPUZWvMy5rf7q%2FiJiUvc0tsNjeG5nzVXp2QcConszghf9Om1BrFl0LpFQ%2Bm1qwfsb0sK4hy9cEsdycluj3o7J1nc2ULkMEDee1XT4FDmBva8igJqAfXOdJpEsF4EtfsrE3YUN2VW%2FdmjmIX173HlbkJlrpCHF2gB06LnyRrKCDpos%2F4gE0IGdcM5FSm17iQEf&X-Amz-Signature=1200db97864fcc8dad87dd6a97b933ddd4ab4d0c331ff2a6657a419469a0cd9b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5UU4ZP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdQ11hctu%2Ffgg4SzNc7xxWzbp3sB1XAOOv%2ByEbCXjrLAiAGVQUAudgneFD%2FQhXAmzbFC7p5ZZlj5mxfe%2BNZP9kbIyqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTg8oyXwp%2Bs4Xx%2FasKtwD5i1ufIjbO1ycoKJplYG4hUtIFbAbUCQg8ReSC6BEfooMW%2FKTyKXTVN6Cqo9Ynxsexq4MnTKIBkf1UiDrTpctsuMkTo9YcFHU%2BoQ6nl1gKDLAkUi3iWZiIpeO3aIYxDXbz0MGlUzCX8Ek9NJhCo7vF1%2B6P%2BZ7%2BqNcRhhiD3mxeRsvqTIHqr1FLLXPk0LgLNxbRrTDPtKfbWzwwRoZGf%2B0X4lFGp0xhp8DLosaBn%2FKRhY6oqhF8buyRXmaMfcwENwRc7WFwyF%2FJ7xFyyy2I2E5GTzOd%2Bu3tNsF54ypH4AZSDUBl4XzfEPtC3LZNM7t%2FAUgPIq5851Q%2BCTnicEJeOmDn3VpUT3AM203m3heraWyb9dCgFfqewyc55IuR0OL3%2B%2B0pRoS62nsx7QWpX7jp8%2BnMrm4hU3OQoFMdQj%2FHPZcPY75MLObBi7OmmI1qv9uV9azKHZTQ9aIqNbK2uiOTO2y%2FVvPLddEuNJEuqf9OcC7TfWg%2FqzFJgJObaapdBuDhUiNfQCyZazKu9%2BollCXVEk%2BnChnSHPZsyCVUCsULoeWFj4PVzXXA%2B%2BnHU90HPGvKntU61wVpqrQHE3fxvERxK4moHmZZWCZaQiaK4f2JsQ1S%2F7OGyag%2BRO79GUpQKcwyd32vAY6pgE%2FsHxa3XGMF3smQRSfTJ3D7obHVsgLPUZWvMy5rf7q%2FiJiUvc0tsNjeG5nzVXp2QcConszghf9Om1BrFl0LpFQ%2Bm1qwfsb0sK4hy9cEsdycluj3o7J1nc2ULkMEDee1XT4FDmBva8igJqAfXOdJpEsF4EtfsrE3YUN2VW%2FdmjmIX173HlbkJlrpCHF2gB06LnyRrKCDpos%2F4gE0IGdcM5FSm17iQEf&X-Amz-Signature=f327104db5ae44a51cafb6ea8fc618a9984e8c3d285d555578fab0ccaaabb169&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5UU4ZP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdQ11hctu%2Ffgg4SzNc7xxWzbp3sB1XAOOv%2ByEbCXjrLAiAGVQUAudgneFD%2FQhXAmzbFC7p5ZZlj5mxfe%2BNZP9kbIyqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTg8oyXwp%2Bs4Xx%2FasKtwD5i1ufIjbO1ycoKJplYG4hUtIFbAbUCQg8ReSC6BEfooMW%2FKTyKXTVN6Cqo9Ynxsexq4MnTKIBkf1UiDrTpctsuMkTo9YcFHU%2BoQ6nl1gKDLAkUi3iWZiIpeO3aIYxDXbz0MGlUzCX8Ek9NJhCo7vF1%2B6P%2BZ7%2BqNcRhhiD3mxeRsvqTIHqr1FLLXPk0LgLNxbRrTDPtKfbWzwwRoZGf%2B0X4lFGp0xhp8DLosaBn%2FKRhY6oqhF8buyRXmaMfcwENwRc7WFwyF%2FJ7xFyyy2I2E5GTzOd%2Bu3tNsF54ypH4AZSDUBl4XzfEPtC3LZNM7t%2FAUgPIq5851Q%2BCTnicEJeOmDn3VpUT3AM203m3heraWyb9dCgFfqewyc55IuR0OL3%2B%2B0pRoS62nsx7QWpX7jp8%2BnMrm4hU3OQoFMdQj%2FHPZcPY75MLObBi7OmmI1qv9uV9azKHZTQ9aIqNbK2uiOTO2y%2FVvPLddEuNJEuqf9OcC7TfWg%2FqzFJgJObaapdBuDhUiNfQCyZazKu9%2BollCXVEk%2BnChnSHPZsyCVUCsULoeWFj4PVzXXA%2B%2BnHU90HPGvKntU61wVpqrQHE3fxvERxK4moHmZZWCZaQiaK4f2JsQ1S%2F7OGyag%2BRO79GUpQKcwyd32vAY6pgE%2FsHxa3XGMF3smQRSfTJ3D7obHVsgLPUZWvMy5rf7q%2FiJiUvc0tsNjeG5nzVXp2QcConszghf9Om1BrFl0LpFQ%2Bm1qwfsb0sK4hy9cEsdycluj3o7J1nc2ULkMEDee1XT4FDmBva8igJqAfXOdJpEsF4EtfsrE3YUN2VW%2FdmjmIX173HlbkJlrpCHF2gB06LnyRrKCDpos%2F4gE0IGdcM5FSm17iQEf&X-Amz-Signature=17f71a00dcd6b14a978b4cb2ecb730d154b31f7e22516b6640a37619a6538640&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5UU4ZP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdQ11hctu%2Ffgg4SzNc7xxWzbp3sB1XAOOv%2ByEbCXjrLAiAGVQUAudgneFD%2FQhXAmzbFC7p5ZZlj5mxfe%2BNZP9kbIyqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTg8oyXwp%2Bs4Xx%2FasKtwD5i1ufIjbO1ycoKJplYG4hUtIFbAbUCQg8ReSC6BEfooMW%2FKTyKXTVN6Cqo9Ynxsexq4MnTKIBkf1UiDrTpctsuMkTo9YcFHU%2BoQ6nl1gKDLAkUi3iWZiIpeO3aIYxDXbz0MGlUzCX8Ek9NJhCo7vF1%2B6P%2BZ7%2BqNcRhhiD3mxeRsvqTIHqr1FLLXPk0LgLNxbRrTDPtKfbWzwwRoZGf%2B0X4lFGp0xhp8DLosaBn%2FKRhY6oqhF8buyRXmaMfcwENwRc7WFwyF%2FJ7xFyyy2I2E5GTzOd%2Bu3tNsF54ypH4AZSDUBl4XzfEPtC3LZNM7t%2FAUgPIq5851Q%2BCTnicEJeOmDn3VpUT3AM203m3heraWyb9dCgFfqewyc55IuR0OL3%2B%2B0pRoS62nsx7QWpX7jp8%2BnMrm4hU3OQoFMdQj%2FHPZcPY75MLObBi7OmmI1qv9uV9azKHZTQ9aIqNbK2uiOTO2y%2FVvPLddEuNJEuqf9OcC7TfWg%2FqzFJgJObaapdBuDhUiNfQCyZazKu9%2BollCXVEk%2BnChnSHPZsyCVUCsULoeWFj4PVzXXA%2B%2BnHU90HPGvKntU61wVpqrQHE3fxvERxK4moHmZZWCZaQiaK4f2JsQ1S%2F7OGyag%2BRO79GUpQKcwyd32vAY6pgE%2FsHxa3XGMF3smQRSfTJ3D7obHVsgLPUZWvMy5rf7q%2FiJiUvc0tsNjeG5nzVXp2QcConszghf9Om1BrFl0LpFQ%2Bm1qwfsb0sK4hy9cEsdycluj3o7J1nc2ULkMEDee1XT4FDmBva8igJqAfXOdJpEsF4EtfsrE3YUN2VW%2FdmjmIX173HlbkJlrpCHF2gB06LnyRrKCDpos%2F4gE0IGdcM5FSm17iQEf&X-Amz-Signature=a3d7793c79e3c6bdd42fc852588fec43a86e64e64b1a318f165fe0aabb5b810c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5UU4ZP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdQ11hctu%2Ffgg4SzNc7xxWzbp3sB1XAOOv%2ByEbCXjrLAiAGVQUAudgneFD%2FQhXAmzbFC7p5ZZlj5mxfe%2BNZP9kbIyqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTg8oyXwp%2Bs4Xx%2FasKtwD5i1ufIjbO1ycoKJplYG4hUtIFbAbUCQg8ReSC6BEfooMW%2FKTyKXTVN6Cqo9Ynxsexq4MnTKIBkf1UiDrTpctsuMkTo9YcFHU%2BoQ6nl1gKDLAkUi3iWZiIpeO3aIYxDXbz0MGlUzCX8Ek9NJhCo7vF1%2B6P%2BZ7%2BqNcRhhiD3mxeRsvqTIHqr1FLLXPk0LgLNxbRrTDPtKfbWzwwRoZGf%2B0X4lFGp0xhp8DLosaBn%2FKRhY6oqhF8buyRXmaMfcwENwRc7WFwyF%2FJ7xFyyy2I2E5GTzOd%2Bu3tNsF54ypH4AZSDUBl4XzfEPtC3LZNM7t%2FAUgPIq5851Q%2BCTnicEJeOmDn3VpUT3AM203m3heraWyb9dCgFfqewyc55IuR0OL3%2B%2B0pRoS62nsx7QWpX7jp8%2BnMrm4hU3OQoFMdQj%2FHPZcPY75MLObBi7OmmI1qv9uV9azKHZTQ9aIqNbK2uiOTO2y%2FVvPLddEuNJEuqf9OcC7TfWg%2FqzFJgJObaapdBuDhUiNfQCyZazKu9%2BollCXVEk%2BnChnSHPZsyCVUCsULoeWFj4PVzXXA%2B%2BnHU90HPGvKntU61wVpqrQHE3fxvERxK4moHmZZWCZaQiaK4f2JsQ1S%2F7OGyag%2BRO79GUpQKcwyd32vAY6pgE%2FsHxa3XGMF3smQRSfTJ3D7obHVsgLPUZWvMy5rf7q%2FiJiUvc0tsNjeG5nzVXp2QcConszghf9Om1BrFl0LpFQ%2Bm1qwfsb0sK4hy9cEsdycluj3o7J1nc2ULkMEDee1XT4FDmBva8igJqAfXOdJpEsF4EtfsrE3YUN2VW%2FdmjmIX173HlbkJlrpCHF2gB06LnyRrKCDpos%2F4gE0IGdcM5FSm17iQEf&X-Amz-Signature=62405232c662b071572cf00fefe5bbed4cf579fd3a37c75d1e31342c8a408bf6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5UU4ZP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdQ11hctu%2Ffgg4SzNc7xxWzbp3sB1XAOOv%2ByEbCXjrLAiAGVQUAudgneFD%2FQhXAmzbFC7p5ZZlj5mxfe%2BNZP9kbIyqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTg8oyXwp%2Bs4Xx%2FasKtwD5i1ufIjbO1ycoKJplYG4hUtIFbAbUCQg8ReSC6BEfooMW%2FKTyKXTVN6Cqo9Ynxsexq4MnTKIBkf1UiDrTpctsuMkTo9YcFHU%2BoQ6nl1gKDLAkUi3iWZiIpeO3aIYxDXbz0MGlUzCX8Ek9NJhCo7vF1%2B6P%2BZ7%2BqNcRhhiD3mxeRsvqTIHqr1FLLXPk0LgLNxbRrTDPtKfbWzwwRoZGf%2B0X4lFGp0xhp8DLosaBn%2FKRhY6oqhF8buyRXmaMfcwENwRc7WFwyF%2FJ7xFyyy2I2E5GTzOd%2Bu3tNsF54ypH4AZSDUBl4XzfEPtC3LZNM7t%2FAUgPIq5851Q%2BCTnicEJeOmDn3VpUT3AM203m3heraWyb9dCgFfqewyc55IuR0OL3%2B%2B0pRoS62nsx7QWpX7jp8%2BnMrm4hU3OQoFMdQj%2FHPZcPY75MLObBi7OmmI1qv9uV9azKHZTQ9aIqNbK2uiOTO2y%2FVvPLddEuNJEuqf9OcC7TfWg%2FqzFJgJObaapdBuDhUiNfQCyZazKu9%2BollCXVEk%2BnChnSHPZsyCVUCsULoeWFj4PVzXXA%2B%2BnHU90HPGvKntU61wVpqrQHE3fxvERxK4moHmZZWCZaQiaK4f2JsQ1S%2F7OGyag%2BRO79GUpQKcwyd32vAY6pgE%2FsHxa3XGMF3smQRSfTJ3D7obHVsgLPUZWvMy5rf7q%2FiJiUvc0tsNjeG5nzVXp2QcConszghf9Om1BrFl0LpFQ%2Bm1qwfsb0sK4hy9cEsdycluj3o7J1nc2ULkMEDee1XT4FDmBva8igJqAfXOdJpEsF4EtfsrE3YUN2VW%2FdmjmIX173HlbkJlrpCHF2gB06LnyRrKCDpos%2F4gE0IGdcM5FSm17iQEf&X-Amz-Signature=1eff3980197a9b1a2d788ed11f223eb534399a8ba1d69713ec8c43523940718d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEVUDPKS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK55FfsXaao1XCwfyR1lWRSimMX2JiGG%2BwnluZU%2FF16AIgcFZlOe1uBg69GnXILLDUCXXV6Ud6bb2qT1UW%2F9zt41cqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNA7Z99i9%2BSc2ULCVyrcAyK2ezvQxB0389Y0wG3IbuTrtXfvV5kPaxTJyyDX9KRCCrWqdEP81XqSzdntFZvEmvRU%2F%2FvkM5occkYNtZrG7%2FS8mPvLA03JFlzFOF2DnR%2BeJt2dkJ0NfMRjujk6aUBKTxPoHBMel9r1CChl%2Fsf31uRqmcyWbrKsndCzT%2B2Q1%2FV2p%2FmalxHXYB3bDSH%2B5%2Ba8Ix3KrQNyLp7w6Sf7u2vLwQahJgDk2Nkt5aR%2BsoJE%2BomT9RWUVtR4fvPvYUsy5Esowjz9mk6rTNxX%2B2TqqeMh2R2lXSjW4T4TSjb%2B7VWEQkip5Ty8ftUg0dmTaLH4eOYlOsHujsY92iPLZ0G6AgHtzO9A%2F5fIc8e0mQGKMuqHDDIPy3NlJ%2FkrDtl3cLJa0%2BeM0jiGVgHUf1o4d8ZBRPnEDnvr%2FLC1%2FziDnq2KeoTjEPcm0ln%2F66tES%2FXRiGliyHJCjDkE4oZE5eFlbsmaqY3JV7DjtRw2ktv4ycfQZVw%2FEuqrfSZb2sfzz14x52lA1P3oty2JPi8WTrkzuek%2BKvlmGzpgGYkdHQLLSuvqovENc7Z5vDlE%2BMpeTQXCANv626UV%2BEoGmrlxX9zApQ8RRZZQve5RdA71eljugbDH37L2B%2FLM%2FiOgLeAPEI8FYJUYMLzd9rwGOqUBV7HoPokVPwD%2Bs3F3h26GX87S2otMkXE7Wi6Etl9C5pvwOEOWvQqaE3HolKSJNcMIQGonSHzdeFi8wRomi8RDSzz3fjwlyH1wfKGrd3R6RH3p3AQodoZchqE8ggePmmqX5xcO1vosl%2B3xkQRIp8P2kF0g9qkDwYUMLChzxdu7%2BYm4AxnKpBGEUACz0ezy5SFJlfckX9Shx2%2BO2lS1T4AujQ9D48Qb&X-Amz-Signature=e282bedb7285085b40131b03816773ab0381487b87c8c9190e5e8a0a5ded8553&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TARER2V5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWDkec2hecl61iLpZP870hwF%2B3TLaIf34XUhO6v2vnDQIgHMbotzUtCsku1hG7oTwtTc%2FEt%2F8NBfeXnYpDEp2bO5oqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0rF4FN%2BGW98xaHCrcA3MAAQnMxhPtuhsUwDpSU1xlBmsaaC8xaZO8TYvVzED9vVcOvR8UgTeA1%2FReO3knqc9S3%2FqEcF6JAo%2Bk9XtTgw2VfRoheRtojdkqmNdWhql4a1%2BZ%2FY%2BrT8g%2BIn8iuBlTuRFTsOWcDyOP5zSreR9sPbhGLV8RQlFlVj0Rh7nV%2BIzwFG79E3odZII7JezFYrs%2BVcLeOQemeV2yef4f%2Fdj9kRVrgj2jtD%2BWVCNm3s%2BaY4L9o47uRhL%2BbY%2Bt03EfNVL8iqV63vv%2FY4F5h6dkpAM3LNuNBZs63xk7OExl%2Fyi3C1Yt9WZ%2BNvhaFYQijimiJUnWJK8LbQZjeayLOzCinhlyx63oUbafTUG9sMHICVRzYun5tiqN%2B5pWsPUaSads9dezKajvhqdV21ltqlzXYe%2FPkhgkjpCp1jxjLW%2F4IVc8%2F4VutACo%2FeVrW85iqYrbYpeNM5Rv%2BsuKnhoAX0%2FmmJVoa6L%2FDZ8dNZbIFb9ZgEVsBejFMTkv2kq8ly7kggduXkZlo3%2BZtr4UK8hEes4ZTQIJXXtuhDmwtT9VNGoHzuiTXPz3NWK%2FaGL2pOyH0eteksyXeZE3RjDqGoKKmR4UFrSyWhhpXBulPZesrH9z%2FIXq71bDP0fPwMpIN2JfcA6iMKLd9rwGOqUBGMvgpF6L7BNQnHomRn0s%2BJjA7h6J%2Fs0LdbZNPjMgf0IwxtSGiyAEdm1aURD4nGxA6%2BIJKsHPSjUOV8ChRJ%2FudA%2F04PGKsdSJGorD6A%2BHq7bv0LHYamkX4jbUsa88UQmxzyKTbfcFKoRYo5CKS8D7cCkPSETDXTLGmBhZksj3wDZI%2B%2FhS39Wh9hgnJnt%2BLfqhxazlpFqY7t4qmwSE243ySV57h2jz&X-Amz-Signature=aaddf52b80aa153f2309ce6bf0a084d3dfdf0d8a407635a8eab3e3317d7ae658&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5UU4ZP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdQ11hctu%2Ffgg4SzNc7xxWzbp3sB1XAOOv%2ByEbCXjrLAiAGVQUAudgneFD%2FQhXAmzbFC7p5ZZlj5mxfe%2BNZP9kbIyqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTg8oyXwp%2Bs4Xx%2FasKtwD5i1ufIjbO1ycoKJplYG4hUtIFbAbUCQg8ReSC6BEfooMW%2FKTyKXTVN6Cqo9Ynxsexq4MnTKIBkf1UiDrTpctsuMkTo9YcFHU%2BoQ6nl1gKDLAkUi3iWZiIpeO3aIYxDXbz0MGlUzCX8Ek9NJhCo7vF1%2B6P%2BZ7%2BqNcRhhiD3mxeRsvqTIHqr1FLLXPk0LgLNxbRrTDPtKfbWzwwRoZGf%2B0X4lFGp0xhp8DLosaBn%2FKRhY6oqhF8buyRXmaMfcwENwRc7WFwyF%2FJ7xFyyy2I2E5GTzOd%2Bu3tNsF54ypH4AZSDUBl4XzfEPtC3LZNM7t%2FAUgPIq5851Q%2BCTnicEJeOmDn3VpUT3AM203m3heraWyb9dCgFfqewyc55IuR0OL3%2B%2B0pRoS62nsx7QWpX7jp8%2BnMrm4hU3OQoFMdQj%2FHPZcPY75MLObBi7OmmI1qv9uV9azKHZTQ9aIqNbK2uiOTO2y%2FVvPLddEuNJEuqf9OcC7TfWg%2FqzFJgJObaapdBuDhUiNfQCyZazKu9%2BollCXVEk%2BnChnSHPZsyCVUCsULoeWFj4PVzXXA%2B%2BnHU90HPGvKntU61wVpqrQHE3fxvERxK4moHmZZWCZaQiaK4f2JsQ1S%2F7OGyag%2BRO79GUpQKcwyd32vAY6pgE%2FsHxa3XGMF3smQRSfTJ3D7obHVsgLPUZWvMy5rf7q%2FiJiUvc0tsNjeG5nzVXp2QcConszghf9Om1BrFl0LpFQ%2Bm1qwfsb0sK4hy9cEsdycluj3o7J1nc2ULkMEDee1XT4FDmBva8igJqAfXOdJpEsF4EtfsrE3YUN2VW%2FdmjmIX173HlbkJlrpCHF2gB06LnyRrKCDpos%2F4gE0IGdcM5FSm17iQEf&X-Amz-Signature=9f68b7877003a33aad89849ffc2de6655d1b04ab4231fd1b6b3589cc3703aafa&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5UU4ZP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdQ11hctu%2Ffgg4SzNc7xxWzbp3sB1XAOOv%2ByEbCXjrLAiAGVQUAudgneFD%2FQhXAmzbFC7p5ZZlj5mxfe%2BNZP9kbIyqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTg8oyXwp%2Bs4Xx%2FasKtwD5i1ufIjbO1ycoKJplYG4hUtIFbAbUCQg8ReSC6BEfooMW%2FKTyKXTVN6Cqo9Ynxsexq4MnTKIBkf1UiDrTpctsuMkTo9YcFHU%2BoQ6nl1gKDLAkUi3iWZiIpeO3aIYxDXbz0MGlUzCX8Ek9NJhCo7vF1%2B6P%2BZ7%2BqNcRhhiD3mxeRsvqTIHqr1FLLXPk0LgLNxbRrTDPtKfbWzwwRoZGf%2B0X4lFGp0xhp8DLosaBn%2FKRhY6oqhF8buyRXmaMfcwENwRc7WFwyF%2FJ7xFyyy2I2E5GTzOd%2Bu3tNsF54ypH4AZSDUBl4XzfEPtC3LZNM7t%2FAUgPIq5851Q%2BCTnicEJeOmDn3VpUT3AM203m3heraWyb9dCgFfqewyc55IuR0OL3%2B%2B0pRoS62nsx7QWpX7jp8%2BnMrm4hU3OQoFMdQj%2FHPZcPY75MLObBi7OmmI1qv9uV9azKHZTQ9aIqNbK2uiOTO2y%2FVvPLddEuNJEuqf9OcC7TfWg%2FqzFJgJObaapdBuDhUiNfQCyZazKu9%2BollCXVEk%2BnChnSHPZsyCVUCsULoeWFj4PVzXXA%2B%2BnHU90HPGvKntU61wVpqrQHE3fxvERxK4moHmZZWCZaQiaK4f2JsQ1S%2F7OGyag%2BRO79GUpQKcwyd32vAY6pgE%2FsHxa3XGMF3smQRSfTJ3D7obHVsgLPUZWvMy5rf7q%2FiJiUvc0tsNjeG5nzVXp2QcConszghf9Om1BrFl0LpFQ%2Bm1qwfsb0sK4hy9cEsdycluj3o7J1nc2ULkMEDee1XT4FDmBva8igJqAfXOdJpEsF4EtfsrE3YUN2VW%2FdmjmIX173HlbkJlrpCHF2gB06LnyRrKCDpos%2F4gE0IGdcM5FSm17iQEf&X-Amz-Signature=e7193831e95f1fa649ac26312e3fe9db560954f3903b55bc08de6014f7ef2184&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5UU4ZP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdQ11hctu%2Ffgg4SzNc7xxWzbp3sB1XAOOv%2ByEbCXjrLAiAGVQUAudgneFD%2FQhXAmzbFC7p5ZZlj5mxfe%2BNZP9kbIyqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTg8oyXwp%2Bs4Xx%2FasKtwD5i1ufIjbO1ycoKJplYG4hUtIFbAbUCQg8ReSC6BEfooMW%2FKTyKXTVN6Cqo9Ynxsexq4MnTKIBkf1UiDrTpctsuMkTo9YcFHU%2BoQ6nl1gKDLAkUi3iWZiIpeO3aIYxDXbz0MGlUzCX8Ek9NJhCo7vF1%2B6P%2BZ7%2BqNcRhhiD3mxeRsvqTIHqr1FLLXPk0LgLNxbRrTDPtKfbWzwwRoZGf%2B0X4lFGp0xhp8DLosaBn%2FKRhY6oqhF8buyRXmaMfcwENwRc7WFwyF%2FJ7xFyyy2I2E5GTzOd%2Bu3tNsF54ypH4AZSDUBl4XzfEPtC3LZNM7t%2FAUgPIq5851Q%2BCTnicEJeOmDn3VpUT3AM203m3heraWyb9dCgFfqewyc55IuR0OL3%2B%2B0pRoS62nsx7QWpX7jp8%2BnMrm4hU3OQoFMdQj%2FHPZcPY75MLObBi7OmmI1qv9uV9azKHZTQ9aIqNbK2uiOTO2y%2FVvPLddEuNJEuqf9OcC7TfWg%2FqzFJgJObaapdBuDhUiNfQCyZazKu9%2BollCXVEk%2BnChnSHPZsyCVUCsULoeWFj4PVzXXA%2B%2BnHU90HPGvKntU61wVpqrQHE3fxvERxK4moHmZZWCZaQiaK4f2JsQ1S%2F7OGyag%2BRO79GUpQKcwyd32vAY6pgE%2FsHxa3XGMF3smQRSfTJ3D7obHVsgLPUZWvMy5rf7q%2FiJiUvc0tsNjeG5nzVXp2QcConszghf9Om1BrFl0LpFQ%2Bm1qwfsb0sK4hy9cEsdycluj3o7J1nc2ULkMEDee1XT4FDmBva8igJqAfXOdJpEsF4EtfsrE3YUN2VW%2FdmjmIX173HlbkJlrpCHF2gB06LnyRrKCDpos%2F4gE0IGdcM5FSm17iQEf&X-Amz-Signature=b52714f8df99b7f259d779f06f5228c6eaa5e984cdd02fed74496ae26d31946d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVVB6HGF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvMW8HzSyNKYyD2OltDknnZkIJ7x02KsmN1DBTMgUh8QIgYrnketwsS9eGnoto8TT262WXP3dUfxS5%2BYactMmypwYqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPySEUKmYuGYcpzQmSrcA%2F2Uxt0%2BHt5QAiTEJX1%2FAtS2A%2FFs2Qtci5UlQEkepFw5eRa%2FZmXpJlYELzTy0%2B0vRM1WQRJ%2Fz7HKmoMv15WOYSEKwL0ZGyF4uFfBA2XsTIrRPUE8vyN7H%2FPNBZ1so0D9MRuCQIrvXpx5Rc5pxWWwLb7uqsbAI0aSdRxGUJGJRSm22Ura1H7jpB8pA9cgjDuE%2Bb%2F8YMrBcCTX7WHkZS97Rg2HtI4%2Fg5V3YtWbjlJnH9jInSRfBV4lkLpvVaO%2Fm9Hjs%2FTL8qdrQqzmE%2FSavl3sMLn%2BVspASyl7UYV9ermOYW5VQ1bJ5NZvqeM38SmE%2FxB3gPnbdVLhst2D2TOq%2FEIO9ajThU4ZSzUrJNmegq7IgF0tgWyS1TH%2B3zE6lD2%2FgJFDB8Emnflt1ETUEulPbTFJI3AuIwnV38GfgENupmtWAe%2BMgFIjBwY8hDR9ZWX8WR8XUSsETBgaoCmGZqvNEnQh27N61Kro5f69BBKcDBd%2BOJiByn6bMAk9VFrzTF6myqmP2NqPmgn1HGTMTTXJpucekQnXvEv0P0i05WrjGOuj8yoS198h1n4uikum2ga%2Fpl2jfVhZRCJ8%2BTft1%2FW9jpIYxi640WxnFGgpP5h6PX9I42JG%2F%2Fxl5KeNi8yBKUwgMJ%2Fd9rwGOqUBIjH6JHJzSj5QGNjbITyCP9WX44ai5J5pSn95bMwXLWHbC9ZNer8TN5OAuE9ARINxnRkAzgiZ4lCmHVX2mBTz%2BIx0a7ojckTMeRFw4C%2FHix9PWQAYiql6K4o8l9oNSEPGtIQx%2F7xJzoYzvTmoDrLChYD6oMc1VnINvqokflu%2Bwp6m%2BGREjl4t1I%2Bc9FwS6ghIlDfnfv3lKs9HVefstwYb2t7pKwtf&X-Amz-Signature=235a83e61f4ea373e95ad11333de9605193b28d4070ac2149c68eed339c709da&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M4OZTWJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNasDbbP5B5uW6vTHVkQFBaaL6w8bFU0%2BTZ9vfgfeLgQIgbKUIay4x2hZ4kLZfiy8GsCbJ9miZelfGrSw8EP6gQ2kqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLKL4OmScCIW%2FrOCjircA52Wf%2Bd1PCxX5RGRytppuzQLhorugtlMmOLrb5VRdv6fCi3KBltolYGDVXdnDs8jbdQ%2BKaIX5j0QhOMAjOJsu5P1O1H5M4B%2BWGhp9LuvGbkwin0T6bmBiRywsyPdOGDskcHg4pENAlW1pXlFi%2BtQI%2B2cO4OdcpuUA7X1Na86LLKEfSmEG8FYLxTS17gIW9hPZRmV4Nqb8APcqpvjtgbPUnDrewVlFvqsOO%2FhAZ9ddGoVvmeLy%2FrwKqrvAaeyQaXUvSUQ5PzXxCDQPrASTBc2d3AtGXxL2u8tdzfkPSd68keNJJqG5gBot5oPlL1NfDpyAFqd6fHJ9WJu52IQPcyQUTOUByKk5t51G%2FGfmD8PYz%2FX0jTc77bjPvudGvRbgg51cTRqLKOMjo%2BkeTTAVWTH%2B2EcqNECdpRiLHnpFPY%2FpUt3WCe3GNIf5vv1MzF15twhEoYN23sAq8uT7ZcYSbD8Gg3KlwCnsSKkhRg6%2FK2oo291f6%2BGTcEab6sK3inw4w8sffVeFmJdK9M1JYKqpsubia2mB4ouaVbfni3Ym%2B2M1LVzBuHP3ObzkRot%2Fz5Wx8PeJHkBvUedmHGrJI1%2FFuTaePvEExt1gUKtyi1fGnCK4OIY7sLBpLbZCVl%2F3xY%2FMJ%2Fd9rwGOqUB5SMCoD%2B8DYEYZjSCwicojanF7tMfH%2FPf0nVw0fDkKjtIgV5oCmClZLQLq%2B25ZYcTOjuzS0dBdusjxpN7zyFPCxxuYz6yEu%2F6XV3uJgl1qOzDuvTYQRqiQMfw1%2BkqdEU2zJ4g%2FVh%2F9IbLL40uautnBvAxkddYBqXejfVL1yxsEtpXEOu1yfkQIyvBsCmuN1oBqPra1mUfq57628wuz3SNz2IznWtj&X-Amz-Signature=cadda36de3aadd27d145a1224ff01e4f501e9f4af6ea754f4125917b8c628f18&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662635GOWK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDG0JlBQ4elLMleRtOvuefnMg%2FFJfbrPIDy9oHmRy7szQIgf7jWYD%2BuSxiA%2Bmrtaj20d4Ldzbh3%2B%2BFcAY2wMyJaPH4qiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGfVSvtitll8lL0ILCrcA3opydPxMgHsrOEzvP%2B7iCNbeA%2Fx2xz0wzw4ux5hYOSLMrmTiGfe59PdvG82FVTpF9LLUO6upPb4wJbLYCcdHBomrr2CZxGsMoRR10CaVo%2B%2FruxQIZLHuNbvj5nMeCkzMWVl1zTyIWa9jaFEFkNwbpd13kRB2aGC1Q83iGXM%2BxtP1llwvRd1xGJmZAbD%2Bgym3VK2B2c1MVeowccMSRdVnz3lQNn2QiBWUQ4UozbY7snN4FMu3j%2FFa68%2BZtd%2BSTYuIINF7pijM8W05R8osm%2BQJewXHQMBWw8iWGvpgHxdKjp6Yqo%2BIUBlYaVrf8n8RQ4fYh0jjzuEpX4mY0CNrViWhLuCWlnw62F9ZbR0LhWlBFFT5bJ5Zi%2FQaYVSI%2FEfjQcH4fuKQl4cg8CNZ1p699FvwFMSm2BHsj5uKLJb3eR%2FqcRAZNSM%2BaDGYfGA7l%2BcJbLp3sw1cUdED6TwMz%2FyzD5WN3qDadExlIty6Iml9RD0P2HgqD4cJXPhfDiKZaw0XUFxIiwynxukv2PM%2BDNLJmgr5jbBGzRXw8C2DK%2Bdy5Xl%2B278QLwQpHDxqBnfjEp2kAcl%2F2eU11sABRC8Kv8IAqksKIDOGa60W2EVf%2BPB22ivAKi3oNyNQMxDB%2F7aJyocMLP59rwGOqUBLteyx12vOl8CkKbxaU4Mhboo%2BHwZj23XJBrxLnmMH0y0jVvRE%2FvUFvkdWcJyVPVEHn7%2FxdCO8f%2BdKerIZXNhScQSkprDHzQQanEmBF4KgmBDzRf9%2Fq8opl%2BZzZ0HgAvgTDet3mnyU9hwJyJ78Asw5j13ji0NI1bzX%2BdYW1YyxHnxEkV9%2FXktsladLj5fHIyTn7QrJCTpwXoOMA%2F81WcRRqW1C8Dq&X-Amz-Signature=d99fd25f3663c005d2a4c230b4206a752483c154bc7a8b1d80880db3a8e08aac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPOINPAU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHrZTLXQh9%2FKj5AIAp491mvtwB2cK8gEVzEzy%2FTYlIqAIgajQQien1O%2BvjgLpH1NMb2jQ9SLb8BGs3cypVGGY1d40qiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBF%2B5QN%2B79N76YI%2F1SrcA%2FZtI5d6V%2F132uusvh4ff48R6V1uh%2FynFzVYnszv4HXe93d9VHOYd3w%2FHLU6tjjfpCHBgLIpX6YLEjNWsC2OUX4F64%2Fk8nlXtouI1fKi0hI4k3JNMJsiz1KBtAAsXIh2P0BaRl4ZRPOv3H3c%2F19JYnXEv0u3O5hazbxfq9HfFhj2U2kD%2BDVyV5UHeuKtyvrFYWMaYq9INWsm%2FUxYLjPwmzSXesKoeout272Mww7B%2FLjmZcePm9WzRlojTQQJ49fCJoK4hQ730jWyskNcTuVjcrJ%2Bg1pkwIb77pLN1DG5dtfApzHwEuatH6YyvqBMry67p%2FWWCxv5ujluG%2B6Vh6nu7Bw5ykmLyJLZ9fczjBVbbSWGgsuBtMZUq3kyUs1%2Fu21WKeP61X7JJ7xpZLo48LoAzbh%2FkKkFEwdF8oTHd%2BCf7%2BT3guTe6xpYVrHYEG5AsNic35TYoXScwLU7MRIVPTYw8CT%2BD59n3hJJ5qov6Jm6R%2FVXreygWvHH81HstbADqWJz6v23k6NXQZWK5zqyjj49vDcYwNlX3XixvQUjm3xCNClU5GgAqB1B%2BzoimIdpsJ1512DkBn8fj4qQiyhw0fYOTwWwz9aP3JlC5PwHCYpn0FW4OXe13FCY8TWZBWPDMLT59rwGOqUBIf7n53HZ5yWeMCZ6UPLCZvpQSDeyV9gjW3COliS9RVO8omGNyM3X0recSUEDsTwuWnpPJQrIjBLYGuqhQBWSSF8EO97WSGb46K4q4P044Kt4zg3yuDfvJaZ1267jySkgfN8%2FeJfHhwRst6BSMQqS0r2S%2F6bbc5texIo5EKFD7q7MLkKU%2Fq1Mu2OqqaEZ4WG19OSZjic4SvFQWN5TggEOrECAgVrt&X-Amz-Signature=a847416500eb4e18cef565c735617005b8f5e57a6b41059710f586e511d9a183&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPOINPAU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHrZTLXQh9%2FKj5AIAp491mvtwB2cK8gEVzEzy%2FTYlIqAIgajQQien1O%2BvjgLpH1NMb2jQ9SLb8BGs3cypVGGY1d40qiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBF%2B5QN%2B79N76YI%2F1SrcA%2FZtI5d6V%2F132uusvh4ff48R6V1uh%2FynFzVYnszv4HXe93d9VHOYd3w%2FHLU6tjjfpCHBgLIpX6YLEjNWsC2OUX4F64%2Fk8nlXtouI1fKi0hI4k3JNMJsiz1KBtAAsXIh2P0BaRl4ZRPOv3H3c%2F19JYnXEv0u3O5hazbxfq9HfFhj2U2kD%2BDVyV5UHeuKtyvrFYWMaYq9INWsm%2FUxYLjPwmzSXesKoeout272Mww7B%2FLjmZcePm9WzRlojTQQJ49fCJoK4hQ730jWyskNcTuVjcrJ%2Bg1pkwIb77pLN1DG5dtfApzHwEuatH6YyvqBMry67p%2FWWCxv5ujluG%2B6Vh6nu7Bw5ykmLyJLZ9fczjBVbbSWGgsuBtMZUq3kyUs1%2Fu21WKeP61X7JJ7xpZLo48LoAzbh%2FkKkFEwdF8oTHd%2BCf7%2BT3guTe6xpYVrHYEG5AsNic35TYoXScwLU7MRIVPTYw8CT%2BD59n3hJJ5qov6Jm6R%2FVXreygWvHH81HstbADqWJz6v23k6NXQZWK5zqyjj49vDcYwNlX3XixvQUjm3xCNClU5GgAqB1B%2BzoimIdpsJ1512DkBn8fj4qQiyhw0fYOTwWwz9aP3JlC5PwHCYpn0FW4OXe13FCY8TWZBWPDMLT59rwGOqUBIf7n53HZ5yWeMCZ6UPLCZvpQSDeyV9gjW3COliS9RVO8omGNyM3X0recSUEDsTwuWnpPJQrIjBLYGuqhQBWSSF8EO97WSGb46K4q4P044Kt4zg3yuDfvJaZ1267jySkgfN8%2FeJfHhwRst6BSMQqS0r2S%2F6bbc5texIo5EKFD7q7MLkKU%2Fq1Mu2OqqaEZ4WG19OSZjic4SvFQWN5TggEOrECAgVrt&X-Amz-Signature=2607237b8d44d8a8f8ccb2aa1f0f248fa41a70749513092712413694c8aeba61&X-Amz-SignedHeaders=host&x-id=GetObject)

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
