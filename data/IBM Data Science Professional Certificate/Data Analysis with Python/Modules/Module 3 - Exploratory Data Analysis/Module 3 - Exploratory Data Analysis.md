

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7D4M5GJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCFfI%2FljFRtei2VamrONYyptEmSG3%2B6Se6FDq64FDlp%2BwIhAJzhEdfm71Qfl7%2BIzM%2BvkK%2FfUIBOdWi4cwWPj0U7AaXmKv8DCDMQABoMNjM3NDIzMTgzODA1IgzmLM5vTOqUb3xH6WEq3ANnblTtW6g%2BcFKtBGIKeTNJ70Pj%2Bdw8%2BErGvdqjgQaxR4%2Bs4mzw%2Bgh%2FM2fOIzzsmgbgrse9z0SScxi8CoYdpTRbO%2Bg7QcksEY%2FWa7xiQQsp70ooDQfnKh7JbRnB4SII1Su02ytmIg1YRiHyXjOraIBKTvzZzw17XjhgElFTM8ghUyMkHBQCKmWdK%2F1cF3QdvIQnZHyhMhc4xPRLBdNfRnXj85Ozje5eNncmvhtsmXiWnM9lzRHUm4QOE6og%2BfJVsnXAYnmTCqPaXXPAzAjjNW3lRzWK754drfucDPQGOnD6XbYkfMNs7yRUmEgMAywx7q8fY%2Bbjd%2Bi43Ba6mRj1N6Y929XtGXv9ymC4oa4Ua%2BhQoMXWZa%2FbtJj6poBs%2FoKLa%2FCfKXGdK6dy2t66NPzFTdHiJlxO82OH6pUEw00zYbDfgUvMQkFpZB5IAMFa9kc1QYRv1jxaaHyq3%2B6%2B0aUO0bmv6nFhFeM82D%2Bk9dTgnU3kr4esoONxSZAHW4Spjtp7ffUEAiLH5E1cKEoNlGiEGOnoG4wld8jmv3bXu0aLSOgROzv%2BemKfX2r7jUOL%2BdnEKY%2BQOrzobskWR83K06c4K9LBrJ3cDwz9KX2oEe2wDAzmKER0wfbeJ9loP6YqHDCQoYm9BjqkAUlr%2FfCltOmeCV8d58WVp%2B37CnpIfYIwPv%2FcjHLMFTOqFf1M3117SM%2FPRX%2BWJkuucBGO0pNHurUnxmKA3lwLXxo2Pbf%2FbV2s47Obo2zcDnFCXpjavuI0DkQVS9BsGTRiIdpSdRZRJ7ONIvh8TZV2wlJgkmsXnpRe0e8BHj79qUZd71gGUOwz99k2qRQjmI0q6f2oJMC7yg42OdoQNALMcHucn2vv&X-Amz-Signature=4bb2baa2eb46c8c0e5c6c92d0e60ef6450637b0984f6996d79a079071442d0a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7D4M5GJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCFfI%2FljFRtei2VamrONYyptEmSG3%2B6Se6FDq64FDlp%2BwIhAJzhEdfm71Qfl7%2BIzM%2BvkK%2FfUIBOdWi4cwWPj0U7AaXmKv8DCDMQABoMNjM3NDIzMTgzODA1IgzmLM5vTOqUb3xH6WEq3ANnblTtW6g%2BcFKtBGIKeTNJ70Pj%2Bdw8%2BErGvdqjgQaxR4%2Bs4mzw%2Bgh%2FM2fOIzzsmgbgrse9z0SScxi8CoYdpTRbO%2Bg7QcksEY%2FWa7xiQQsp70ooDQfnKh7JbRnB4SII1Su02ytmIg1YRiHyXjOraIBKTvzZzw17XjhgElFTM8ghUyMkHBQCKmWdK%2F1cF3QdvIQnZHyhMhc4xPRLBdNfRnXj85Ozje5eNncmvhtsmXiWnM9lzRHUm4QOE6og%2BfJVsnXAYnmTCqPaXXPAzAjjNW3lRzWK754drfucDPQGOnD6XbYkfMNs7yRUmEgMAywx7q8fY%2Bbjd%2Bi43Ba6mRj1N6Y929XtGXv9ymC4oa4Ua%2BhQoMXWZa%2FbtJj6poBs%2FoKLa%2FCfKXGdK6dy2t66NPzFTdHiJlxO82OH6pUEw00zYbDfgUvMQkFpZB5IAMFa9kc1QYRv1jxaaHyq3%2B6%2B0aUO0bmv6nFhFeM82D%2Bk9dTgnU3kr4esoONxSZAHW4Spjtp7ffUEAiLH5E1cKEoNlGiEGOnoG4wld8jmv3bXu0aLSOgROzv%2BemKfX2r7jUOL%2BdnEKY%2BQOrzobskWR83K06c4K9LBrJ3cDwz9KX2oEe2wDAzmKER0wfbeJ9loP6YqHDCQoYm9BjqkAUlr%2FfCltOmeCV8d58WVp%2B37CnpIfYIwPv%2FcjHLMFTOqFf1M3117SM%2FPRX%2BWJkuucBGO0pNHurUnxmKA3lwLXxo2Pbf%2FbV2s47Obo2zcDnFCXpjavuI0DkQVS9BsGTRiIdpSdRZRJ7ONIvh8TZV2wlJgkmsXnpRe0e8BHj79qUZd71gGUOwz99k2qRQjmI0q6f2oJMC7yg42OdoQNALMcHucn2vv&X-Amz-Signature=006b66c9b94532455cad8024228f0d63b266326c665c9112d60343295be81c7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7D4M5GJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCFfI%2FljFRtei2VamrONYyptEmSG3%2B6Se6FDq64FDlp%2BwIhAJzhEdfm71Qfl7%2BIzM%2BvkK%2FfUIBOdWi4cwWPj0U7AaXmKv8DCDMQABoMNjM3NDIzMTgzODA1IgzmLM5vTOqUb3xH6WEq3ANnblTtW6g%2BcFKtBGIKeTNJ70Pj%2Bdw8%2BErGvdqjgQaxR4%2Bs4mzw%2Bgh%2FM2fOIzzsmgbgrse9z0SScxi8CoYdpTRbO%2Bg7QcksEY%2FWa7xiQQsp70ooDQfnKh7JbRnB4SII1Su02ytmIg1YRiHyXjOraIBKTvzZzw17XjhgElFTM8ghUyMkHBQCKmWdK%2F1cF3QdvIQnZHyhMhc4xPRLBdNfRnXj85Ozje5eNncmvhtsmXiWnM9lzRHUm4QOE6og%2BfJVsnXAYnmTCqPaXXPAzAjjNW3lRzWK754drfucDPQGOnD6XbYkfMNs7yRUmEgMAywx7q8fY%2Bbjd%2Bi43Ba6mRj1N6Y929XtGXv9ymC4oa4Ua%2BhQoMXWZa%2FbtJj6poBs%2FoKLa%2FCfKXGdK6dy2t66NPzFTdHiJlxO82OH6pUEw00zYbDfgUvMQkFpZB5IAMFa9kc1QYRv1jxaaHyq3%2B6%2B0aUO0bmv6nFhFeM82D%2Bk9dTgnU3kr4esoONxSZAHW4Spjtp7ffUEAiLH5E1cKEoNlGiEGOnoG4wld8jmv3bXu0aLSOgROzv%2BemKfX2r7jUOL%2BdnEKY%2BQOrzobskWR83K06c4K9LBrJ3cDwz9KX2oEe2wDAzmKER0wfbeJ9loP6YqHDCQoYm9BjqkAUlr%2FfCltOmeCV8d58WVp%2B37CnpIfYIwPv%2FcjHLMFTOqFf1M3117SM%2FPRX%2BWJkuucBGO0pNHurUnxmKA3lwLXxo2Pbf%2FbV2s47Obo2zcDnFCXpjavuI0DkQVS9BsGTRiIdpSdRZRJ7ONIvh8TZV2wlJgkmsXnpRe0e8BHj79qUZd71gGUOwz99k2qRQjmI0q6f2oJMC7yg42OdoQNALMcHucn2vv&X-Amz-Signature=a22ab40ff314e94356ab88ee4b0b32e4dc34bec50ab0e8f7593f1973e4292806&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUWKWFWH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQD2V6iDMUMekLJTi4wGEkAHWA2lNWNstkrl9xkf0TR4MgIhAI4wtVkZXDygKCZjUICmEmNZJQifgWJ028%2BkE0u8CHoaKv8DCDMQABoMNjM3NDIzMTgzODA1IgwAU2w1MK6SEqE%2F3qYq3AMU1KLqR6BT3gfF%2BgwptKZxO0i2JjFN8CR6oEqcnctsSeKvtKfl8vrr0KU3GTYkWgeKE8309oaW33eNohVKs7G80TJPru%2Bf%2FL9LFlhf82LU%2B87xqovgYyi5jJvWOmjUnekfA223wsYEfPx1nmtLvsYeWSjVnjv36kexJMKa64Dh995Juhe4CaQZeRVcPbOKWZ%2F10GAXlre5bb6IAZ%2B1OMn4hLTqiUvHsXPFxOm9LpKsgFt9Az%2F8rFSLUy62VJWU9cnebuVanKSVoEgHvqBHw%2Bqp2r0ZmsO5zswAI0Wk4Q8Z0G58LJxeatNFRdNZkQEIECviOHuSTGyhGflPcgUbF1XZnb%2FPM%2BNFqvlT50GBILuyY6FRBaOmIHEBfnRzlZwq2doc8smSpIvJaK3Zr2Pp6jUrPyeNXFqGVPFBaCFd1BTPsdQuk%2B6yiWpsLDtVHsJKViFHFwV69ll1NXAG%2BWD%2FvXGB74UwUzTBUDwOJfP%2BYYYkj7PTbr2yHCXBBU3W5Fh15Jq9y7l4jaaLxtD9dqkKzSaMmpAKVWP8LlRGhA2kw%2FTt7DtWcaGp8nMbu6PmGi84lA1mfHdoowic660C7m%2BCvb7RK4pNpFD5KfxZaatLrdhGfSKNN5FQ431NwIqV3TCVoYm9BjqkAYlsH6zxe8XLmZ9GLoT8kV2PLc9Tt6jVHAQaaurLNY7l2H%2BPRLS5tWQTymP1%2FN72N1JTYwzySLKKohtunZyUSEUKfp0WhkUkhibFVllYxT%2FhDes8h4foaGqRe%2BoElh58Tm%2FlOMdZC3kqJpwNtV3PQ68DDtx739rf40pnyR1JEyqvkYwvglmz%2F7lIqXHpeWdPtZ2uvawqHymKSloUrsssTCBTnU6a&X-Amz-Signature=7174f9d7b0d611b7448f4b3a25d91aad778ddfb428acd90e679ad8f67d4075b5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUWKWFWH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQD2V6iDMUMekLJTi4wGEkAHWA2lNWNstkrl9xkf0TR4MgIhAI4wtVkZXDygKCZjUICmEmNZJQifgWJ028%2BkE0u8CHoaKv8DCDMQABoMNjM3NDIzMTgzODA1IgwAU2w1MK6SEqE%2F3qYq3AMU1KLqR6BT3gfF%2BgwptKZxO0i2JjFN8CR6oEqcnctsSeKvtKfl8vrr0KU3GTYkWgeKE8309oaW33eNohVKs7G80TJPru%2Bf%2FL9LFlhf82LU%2B87xqovgYyi5jJvWOmjUnekfA223wsYEfPx1nmtLvsYeWSjVnjv36kexJMKa64Dh995Juhe4CaQZeRVcPbOKWZ%2F10GAXlre5bb6IAZ%2B1OMn4hLTqiUvHsXPFxOm9LpKsgFt9Az%2F8rFSLUy62VJWU9cnebuVanKSVoEgHvqBHw%2Bqp2r0ZmsO5zswAI0Wk4Q8Z0G58LJxeatNFRdNZkQEIECviOHuSTGyhGflPcgUbF1XZnb%2FPM%2BNFqvlT50GBILuyY6FRBaOmIHEBfnRzlZwq2doc8smSpIvJaK3Zr2Pp6jUrPyeNXFqGVPFBaCFd1BTPsdQuk%2B6yiWpsLDtVHsJKViFHFwV69ll1NXAG%2BWD%2FvXGB74UwUzTBUDwOJfP%2BYYYkj7PTbr2yHCXBBU3W5Fh15Jq9y7l4jaaLxtD9dqkKzSaMmpAKVWP8LlRGhA2kw%2FTt7DtWcaGp8nMbu6PmGi84lA1mfHdoowic660C7m%2BCvb7RK4pNpFD5KfxZaatLrdhGfSKNN5FQ431NwIqV3TCVoYm9BjqkAYlsH6zxe8XLmZ9GLoT8kV2PLc9Tt6jVHAQaaurLNY7l2H%2BPRLS5tWQTymP1%2FN72N1JTYwzySLKKohtunZyUSEUKfp0WhkUkhibFVllYxT%2FhDes8h4foaGqRe%2BoElh58Tm%2FlOMdZC3kqJpwNtV3PQ68DDtx739rf40pnyR1JEyqvkYwvglmz%2F7lIqXHpeWdPtZ2uvawqHymKSloUrsssTCBTnU6a&X-Amz-Signature=7c0c57227da297a86307f5b44cfb26def32ccb0527adc1e88875635408526bda&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUWKWFWH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQD2V6iDMUMekLJTi4wGEkAHWA2lNWNstkrl9xkf0TR4MgIhAI4wtVkZXDygKCZjUICmEmNZJQifgWJ028%2BkE0u8CHoaKv8DCDMQABoMNjM3NDIzMTgzODA1IgwAU2w1MK6SEqE%2F3qYq3AMU1KLqR6BT3gfF%2BgwptKZxO0i2JjFN8CR6oEqcnctsSeKvtKfl8vrr0KU3GTYkWgeKE8309oaW33eNohVKs7G80TJPru%2Bf%2FL9LFlhf82LU%2B87xqovgYyi5jJvWOmjUnekfA223wsYEfPx1nmtLvsYeWSjVnjv36kexJMKa64Dh995Juhe4CaQZeRVcPbOKWZ%2F10GAXlre5bb6IAZ%2B1OMn4hLTqiUvHsXPFxOm9LpKsgFt9Az%2F8rFSLUy62VJWU9cnebuVanKSVoEgHvqBHw%2Bqp2r0ZmsO5zswAI0Wk4Q8Z0G58LJxeatNFRdNZkQEIECviOHuSTGyhGflPcgUbF1XZnb%2FPM%2BNFqvlT50GBILuyY6FRBaOmIHEBfnRzlZwq2doc8smSpIvJaK3Zr2Pp6jUrPyeNXFqGVPFBaCFd1BTPsdQuk%2B6yiWpsLDtVHsJKViFHFwV69ll1NXAG%2BWD%2FvXGB74UwUzTBUDwOJfP%2BYYYkj7PTbr2yHCXBBU3W5Fh15Jq9y7l4jaaLxtD9dqkKzSaMmpAKVWP8LlRGhA2kw%2FTt7DtWcaGp8nMbu6PmGi84lA1mfHdoowic660C7m%2BCvb7RK4pNpFD5KfxZaatLrdhGfSKNN5FQ431NwIqV3TCVoYm9BjqkAYlsH6zxe8XLmZ9GLoT8kV2PLc9Tt6jVHAQaaurLNY7l2H%2BPRLS5tWQTymP1%2FN72N1JTYwzySLKKohtunZyUSEUKfp0WhkUkhibFVllYxT%2FhDes8h4foaGqRe%2BoElh58Tm%2FlOMdZC3kqJpwNtV3PQ68DDtx739rf40pnyR1JEyqvkYwvglmz%2F7lIqXHpeWdPtZ2uvawqHymKSloUrsssTCBTnU6a&X-Amz-Signature=5b9767253b79774f327c2d073567e22ebdac81cce08e18f9b1d4dc8f3ae716e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUWKWFWH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQD2V6iDMUMekLJTi4wGEkAHWA2lNWNstkrl9xkf0TR4MgIhAI4wtVkZXDygKCZjUICmEmNZJQifgWJ028%2BkE0u8CHoaKv8DCDMQABoMNjM3NDIzMTgzODA1IgwAU2w1MK6SEqE%2F3qYq3AMU1KLqR6BT3gfF%2BgwptKZxO0i2JjFN8CR6oEqcnctsSeKvtKfl8vrr0KU3GTYkWgeKE8309oaW33eNohVKs7G80TJPru%2Bf%2FL9LFlhf82LU%2B87xqovgYyi5jJvWOmjUnekfA223wsYEfPx1nmtLvsYeWSjVnjv36kexJMKa64Dh995Juhe4CaQZeRVcPbOKWZ%2F10GAXlre5bb6IAZ%2B1OMn4hLTqiUvHsXPFxOm9LpKsgFt9Az%2F8rFSLUy62VJWU9cnebuVanKSVoEgHvqBHw%2Bqp2r0ZmsO5zswAI0Wk4Q8Z0G58LJxeatNFRdNZkQEIECviOHuSTGyhGflPcgUbF1XZnb%2FPM%2BNFqvlT50GBILuyY6FRBaOmIHEBfnRzlZwq2doc8smSpIvJaK3Zr2Pp6jUrPyeNXFqGVPFBaCFd1BTPsdQuk%2B6yiWpsLDtVHsJKViFHFwV69ll1NXAG%2BWD%2FvXGB74UwUzTBUDwOJfP%2BYYYkj7PTbr2yHCXBBU3W5Fh15Jq9y7l4jaaLxtD9dqkKzSaMmpAKVWP8LlRGhA2kw%2FTt7DtWcaGp8nMbu6PmGi84lA1mfHdoowic660C7m%2BCvb7RK4pNpFD5KfxZaatLrdhGfSKNN5FQ431NwIqV3TCVoYm9BjqkAYlsH6zxe8XLmZ9GLoT8kV2PLc9Tt6jVHAQaaurLNY7l2H%2BPRLS5tWQTymP1%2FN72N1JTYwzySLKKohtunZyUSEUKfp0WhkUkhibFVllYxT%2FhDes8h4foaGqRe%2BoElh58Tm%2FlOMdZC3kqJpwNtV3PQ68DDtx739rf40pnyR1JEyqvkYwvglmz%2F7lIqXHpeWdPtZ2uvawqHymKSloUrsssTCBTnU6a&X-Amz-Signature=48800cc3a1ff4f165ac171955ba8fced19d99ef96c69f89d9c9a0b70cbd6f0d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUWKWFWH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQD2V6iDMUMekLJTi4wGEkAHWA2lNWNstkrl9xkf0TR4MgIhAI4wtVkZXDygKCZjUICmEmNZJQifgWJ028%2BkE0u8CHoaKv8DCDMQABoMNjM3NDIzMTgzODA1IgwAU2w1MK6SEqE%2F3qYq3AMU1KLqR6BT3gfF%2BgwptKZxO0i2JjFN8CR6oEqcnctsSeKvtKfl8vrr0KU3GTYkWgeKE8309oaW33eNohVKs7G80TJPru%2Bf%2FL9LFlhf82LU%2B87xqovgYyi5jJvWOmjUnekfA223wsYEfPx1nmtLvsYeWSjVnjv36kexJMKa64Dh995Juhe4CaQZeRVcPbOKWZ%2F10GAXlre5bb6IAZ%2B1OMn4hLTqiUvHsXPFxOm9LpKsgFt9Az%2F8rFSLUy62VJWU9cnebuVanKSVoEgHvqBHw%2Bqp2r0ZmsO5zswAI0Wk4Q8Z0G58LJxeatNFRdNZkQEIECviOHuSTGyhGflPcgUbF1XZnb%2FPM%2BNFqvlT50GBILuyY6FRBaOmIHEBfnRzlZwq2doc8smSpIvJaK3Zr2Pp6jUrPyeNXFqGVPFBaCFd1BTPsdQuk%2B6yiWpsLDtVHsJKViFHFwV69ll1NXAG%2BWD%2FvXGB74UwUzTBUDwOJfP%2BYYYkj7PTbr2yHCXBBU3W5Fh15Jq9y7l4jaaLxtD9dqkKzSaMmpAKVWP8LlRGhA2kw%2FTt7DtWcaGp8nMbu6PmGi84lA1mfHdoowic660C7m%2BCvb7RK4pNpFD5KfxZaatLrdhGfSKNN5FQ431NwIqV3TCVoYm9BjqkAYlsH6zxe8XLmZ9GLoT8kV2PLc9Tt6jVHAQaaurLNY7l2H%2BPRLS5tWQTymP1%2FN72N1JTYwzySLKKohtunZyUSEUKfp0WhkUkhibFVllYxT%2FhDes8h4foaGqRe%2BoElh58Tm%2FlOMdZC3kqJpwNtV3PQ68DDtx739rf40pnyR1JEyqvkYwvglmz%2F7lIqXHpeWdPtZ2uvawqHymKSloUrsssTCBTnU6a&X-Amz-Signature=51b582bdbef190caff0a0d6fa114f3a068bbe2392741dceb69d247027b0bb209&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUWKWFWH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQD2V6iDMUMekLJTi4wGEkAHWA2lNWNstkrl9xkf0TR4MgIhAI4wtVkZXDygKCZjUICmEmNZJQifgWJ028%2BkE0u8CHoaKv8DCDMQABoMNjM3NDIzMTgzODA1IgwAU2w1MK6SEqE%2F3qYq3AMU1KLqR6BT3gfF%2BgwptKZxO0i2JjFN8CR6oEqcnctsSeKvtKfl8vrr0KU3GTYkWgeKE8309oaW33eNohVKs7G80TJPru%2Bf%2FL9LFlhf82LU%2B87xqovgYyi5jJvWOmjUnekfA223wsYEfPx1nmtLvsYeWSjVnjv36kexJMKa64Dh995Juhe4CaQZeRVcPbOKWZ%2F10GAXlre5bb6IAZ%2B1OMn4hLTqiUvHsXPFxOm9LpKsgFt9Az%2F8rFSLUy62VJWU9cnebuVanKSVoEgHvqBHw%2Bqp2r0ZmsO5zswAI0Wk4Q8Z0G58LJxeatNFRdNZkQEIECviOHuSTGyhGflPcgUbF1XZnb%2FPM%2BNFqvlT50GBILuyY6FRBaOmIHEBfnRzlZwq2doc8smSpIvJaK3Zr2Pp6jUrPyeNXFqGVPFBaCFd1BTPsdQuk%2B6yiWpsLDtVHsJKViFHFwV69ll1NXAG%2BWD%2FvXGB74UwUzTBUDwOJfP%2BYYYkj7PTbr2yHCXBBU3W5Fh15Jq9y7l4jaaLxtD9dqkKzSaMmpAKVWP8LlRGhA2kw%2FTt7DtWcaGp8nMbu6PmGi84lA1mfHdoowic660C7m%2BCvb7RK4pNpFD5KfxZaatLrdhGfSKNN5FQ431NwIqV3TCVoYm9BjqkAYlsH6zxe8XLmZ9GLoT8kV2PLc9Tt6jVHAQaaurLNY7l2H%2BPRLS5tWQTymP1%2FN72N1JTYwzySLKKohtunZyUSEUKfp0WhkUkhibFVllYxT%2FhDes8h4foaGqRe%2BoElh58Tm%2FlOMdZC3kqJpwNtV3PQ68DDtx739rf40pnyR1JEyqvkYwvglmz%2F7lIqXHpeWdPtZ2uvawqHymKSloUrsssTCBTnU6a&X-Amz-Signature=b51485d199626bafd521e42ac6398029ffde1b03be0ef1f356bbb0741749fb78&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2IIXA64%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBE25oLfJJ8KfxYgjjhT4yT%2F2N%2BoqUxMWuPQn4JworC5AiEAjAuHKdO3Y4aVs8I%2Fe%2Fo6HpZP0nLywldcA7S170jbmUMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDFH%2FQz0cLthtcUVGqircA4OR6vU3Xzikf9O0rpDGBegSZgC1UPTgaKCx7LxLVP6Gf5J1MiNbHOZx%2FkuwHnR7n2Apb8mti9%2FbOOLlHPTlMs1aeSUTJwZTWbNSiifFY9AG0iPz1IkZjw3LCkcrOUjZFqvN54s5amdCXdvbpwW%2BPZtDrwez3qD9TWC%2F8TjRn90fZImijfIyTb03Xo2J5jYFYWY50Uuif6coKqGpsrzXjM4QIe0dSjA5lr3hQTRQTAFpKrrBgt%2BrDgoALedVSq4oh0fckT68BLnGflMQ0FzCzktbaM6EAvwfiDPdy%2BZCJfxl1DOqCjuJpzjonS0wWqD8LzusFT2rUZi%2BiKiB57rTT0TtO1CxnqDf2IX8ufnVfBVG7busoqZewkb25UEed2024me4OYZ%2FP5DVDSAnfq4nrfjNkQwS%2BTWOd9Y3jGJyWcGYDt21zwdkKf%2F6jtQYJx2%2BGnv7tysH35KUe5T4809U9ikiSUbx1RyTmxFHsAkcgw8A%2BhCaMAh3ROz1ljIwd8%2BJGw0fVJXOE0EDTvgGJwytl93%2BaRH%2BnwHkWcqsLNylC62oSYiE59oCrU8wmMWZ1bQjVtU2QSnzL%2B9d1lOJvJLLGMCn0C8vqcrL%2BNZAQVqbMpdt9Bh0a2bqosEg2dXlMKqiib0GOqUBcGZ477hqh%2BQBTzFOZdUBB3f%2F6pbbX9L5G%2FuijHYfJuNzLhHnI1abqvoiUGlVArlccth%2FspvEnNUeU3VVpfl54cy73HeDKg2N3OCmR%2FjzOgYnIQCTeeGy7dwxjaP6XXCJQMIcdfHZEjYAYQgfr4zntJbiXZzamrp7KAyqqT1FIxSSwfPOhzHhcf2%2F250NOU4KcstW4TA6coeWq9aHMRPlYOooksd0&X-Amz-Signature=df97f3237a50a33b62bc677f25cc611dd958d0d1f9feaed70129713a7d9a1d26&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUU5FKMZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDRFujipyI%2FTD1NwODIRspHgpY1HZz90JToOLmqxUlzIQIgZixqILrM7oZ9H2QO1AXACEzMDAMgqIjoHZ2Bb1K%2Fiskq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDIppdxGU3z5jaN1T9CrcA%2BIgkjLXYzJx9ai1mpsiKr%2FX1T8MZ2jcUqxpuGD51QPvE0pB%2F3%2FpFbUkhnQLg8zYcNQgIH36U3pNrQ1LDA7xVX4pUBfob11JfVz%2B5uYuIzTKrlTmSp8lhDdaoQJNd86%2BYfLaupI4oMVuMc%2BTzbPMvgylHl%2BYoqxlsXeVa7lJJ%2BSjps0i5avnOGcP75ipOpondEv7ShpCS69TwwU8391Ar%2BLxoHpYtCgiV6IMcR0np5Xl9IrUOYi3nx3ZlTHmf6ldKOLSbnfQj8dT0dTwB6eGuoZIwcR13Q4Ds8p6Ih5kQ53faqz65uEEcpfIyk9yzXDOkU8wZtAthPbcWtV2t%2Be7tvBj%2BKoBAzQjd%2BrdIhklOoqeF9xhqQQhOQFee7DLUUyTyS2F0hvQuDTxRgmVSxdjBOQ5dqitj%2BH3IGgrNDxF%2FUU7gZHqGcDkQWvvmQPR%2BTZLzhDeJSawnADpx%2ByrZG0F9Yz4Q6WDBhVnQrFTBF%2BCNcLWKBpMyx%2FgmJs%2FKNZJkt9DiV7DEMRdVYejdzKRZDgvII38xzZ%2FlCHR1QhGvrqSgBwsCt8WHjuqprpNEWkLxYIAEjKi5%2FY9iIjGDM62aeP15bPtd0ees91lUwbmNpx2PoIA7FSOon6Byl%2BpR5u0MJmhib0GOqUBM93VOf54Pb1OnCkJfG7LCZBUb67yjwf0n9leeLQjHzY0zm9Oz5JEFbcmhWSig%2BJHWM%2FvzJQnG8w3oTyehnNauqsQD6C1oYaU6GRGtqks5lCdZkAtB4mu7u0hxjWKva88Dr3sqQ3Bc6wpjinQon35jqS894zQaEJ2GNtqwiKGu9tZ5O12PO8%2FWV18SitJdXi73oqgbPzVIc4BHaarmMltLDXcGDTJ&X-Amz-Signature=f92a425f683956998588fc63e4d59e1aab57163fd22b5e3c6ce7bcf63b6a4b00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUWKWFWH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQD2V6iDMUMekLJTi4wGEkAHWA2lNWNstkrl9xkf0TR4MgIhAI4wtVkZXDygKCZjUICmEmNZJQifgWJ028%2BkE0u8CHoaKv8DCDMQABoMNjM3NDIzMTgzODA1IgwAU2w1MK6SEqE%2F3qYq3AMU1KLqR6BT3gfF%2BgwptKZxO0i2JjFN8CR6oEqcnctsSeKvtKfl8vrr0KU3GTYkWgeKE8309oaW33eNohVKs7G80TJPru%2Bf%2FL9LFlhf82LU%2B87xqovgYyi5jJvWOmjUnekfA223wsYEfPx1nmtLvsYeWSjVnjv36kexJMKa64Dh995Juhe4CaQZeRVcPbOKWZ%2F10GAXlre5bb6IAZ%2B1OMn4hLTqiUvHsXPFxOm9LpKsgFt9Az%2F8rFSLUy62VJWU9cnebuVanKSVoEgHvqBHw%2Bqp2r0ZmsO5zswAI0Wk4Q8Z0G58LJxeatNFRdNZkQEIECviOHuSTGyhGflPcgUbF1XZnb%2FPM%2BNFqvlT50GBILuyY6FRBaOmIHEBfnRzlZwq2doc8smSpIvJaK3Zr2Pp6jUrPyeNXFqGVPFBaCFd1BTPsdQuk%2B6yiWpsLDtVHsJKViFHFwV69ll1NXAG%2BWD%2FvXGB74UwUzTBUDwOJfP%2BYYYkj7PTbr2yHCXBBU3W5Fh15Jq9y7l4jaaLxtD9dqkKzSaMmpAKVWP8LlRGhA2kw%2FTt7DtWcaGp8nMbu6PmGi84lA1mfHdoowic660C7m%2BCvb7RK4pNpFD5KfxZaatLrdhGfSKNN5FQ431NwIqV3TCVoYm9BjqkAYlsH6zxe8XLmZ9GLoT8kV2PLc9Tt6jVHAQaaurLNY7l2H%2BPRLS5tWQTymP1%2FN72N1JTYwzySLKKohtunZyUSEUKfp0WhkUkhibFVllYxT%2FhDes8h4foaGqRe%2BoElh58Tm%2FlOMdZC3kqJpwNtV3PQ68DDtx739rf40pnyR1JEyqvkYwvglmz%2F7lIqXHpeWdPtZ2uvawqHymKSloUrsssTCBTnU6a&X-Amz-Signature=5faa2cb310929a31918312fa1991343ed927ba448f2979f5cc9aef6ebc9cae40&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUWKWFWH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQD2V6iDMUMekLJTi4wGEkAHWA2lNWNstkrl9xkf0TR4MgIhAI4wtVkZXDygKCZjUICmEmNZJQifgWJ028%2BkE0u8CHoaKv8DCDMQABoMNjM3NDIzMTgzODA1IgwAU2w1MK6SEqE%2F3qYq3AMU1KLqR6BT3gfF%2BgwptKZxO0i2JjFN8CR6oEqcnctsSeKvtKfl8vrr0KU3GTYkWgeKE8309oaW33eNohVKs7G80TJPru%2Bf%2FL9LFlhf82LU%2B87xqovgYyi5jJvWOmjUnekfA223wsYEfPx1nmtLvsYeWSjVnjv36kexJMKa64Dh995Juhe4CaQZeRVcPbOKWZ%2F10GAXlre5bb6IAZ%2B1OMn4hLTqiUvHsXPFxOm9LpKsgFt9Az%2F8rFSLUy62VJWU9cnebuVanKSVoEgHvqBHw%2Bqp2r0ZmsO5zswAI0Wk4Q8Z0G58LJxeatNFRdNZkQEIECviOHuSTGyhGflPcgUbF1XZnb%2FPM%2BNFqvlT50GBILuyY6FRBaOmIHEBfnRzlZwq2doc8smSpIvJaK3Zr2Pp6jUrPyeNXFqGVPFBaCFd1BTPsdQuk%2B6yiWpsLDtVHsJKViFHFwV69ll1NXAG%2BWD%2FvXGB74UwUzTBUDwOJfP%2BYYYkj7PTbr2yHCXBBU3W5Fh15Jq9y7l4jaaLxtD9dqkKzSaMmpAKVWP8LlRGhA2kw%2FTt7DtWcaGp8nMbu6PmGi84lA1mfHdoowic660C7m%2BCvb7RK4pNpFD5KfxZaatLrdhGfSKNN5FQ431NwIqV3TCVoYm9BjqkAYlsH6zxe8XLmZ9GLoT8kV2PLc9Tt6jVHAQaaurLNY7l2H%2BPRLS5tWQTymP1%2FN72N1JTYwzySLKKohtunZyUSEUKfp0WhkUkhibFVllYxT%2FhDes8h4foaGqRe%2BoElh58Tm%2FlOMdZC3kqJpwNtV3PQ68DDtx739rf40pnyR1JEyqvkYwvglmz%2F7lIqXHpeWdPtZ2uvawqHymKSloUrsssTCBTnU6a&X-Amz-Signature=dfeb31e3f851b94bd1670fadc4e4d6d7c70be9c620c4fb625de15949d4b1f471&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUWKWFWH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQD2V6iDMUMekLJTi4wGEkAHWA2lNWNstkrl9xkf0TR4MgIhAI4wtVkZXDygKCZjUICmEmNZJQifgWJ028%2BkE0u8CHoaKv8DCDMQABoMNjM3NDIzMTgzODA1IgwAU2w1MK6SEqE%2F3qYq3AMU1KLqR6BT3gfF%2BgwptKZxO0i2JjFN8CR6oEqcnctsSeKvtKfl8vrr0KU3GTYkWgeKE8309oaW33eNohVKs7G80TJPru%2Bf%2FL9LFlhf82LU%2B87xqovgYyi5jJvWOmjUnekfA223wsYEfPx1nmtLvsYeWSjVnjv36kexJMKa64Dh995Juhe4CaQZeRVcPbOKWZ%2F10GAXlre5bb6IAZ%2B1OMn4hLTqiUvHsXPFxOm9LpKsgFt9Az%2F8rFSLUy62VJWU9cnebuVanKSVoEgHvqBHw%2Bqp2r0ZmsO5zswAI0Wk4Q8Z0G58LJxeatNFRdNZkQEIECviOHuSTGyhGflPcgUbF1XZnb%2FPM%2BNFqvlT50GBILuyY6FRBaOmIHEBfnRzlZwq2doc8smSpIvJaK3Zr2Pp6jUrPyeNXFqGVPFBaCFd1BTPsdQuk%2B6yiWpsLDtVHsJKViFHFwV69ll1NXAG%2BWD%2FvXGB74UwUzTBUDwOJfP%2BYYYkj7PTbr2yHCXBBU3W5Fh15Jq9y7l4jaaLxtD9dqkKzSaMmpAKVWP8LlRGhA2kw%2FTt7DtWcaGp8nMbu6PmGi84lA1mfHdoowic660C7m%2BCvb7RK4pNpFD5KfxZaatLrdhGfSKNN5FQ431NwIqV3TCVoYm9BjqkAYlsH6zxe8XLmZ9GLoT8kV2PLc9Tt6jVHAQaaurLNY7l2H%2BPRLS5tWQTymP1%2FN72N1JTYwzySLKKohtunZyUSEUKfp0WhkUkhibFVllYxT%2FhDes8h4foaGqRe%2BoElh58Tm%2FlOMdZC3kqJpwNtV3PQ68DDtx739rf40pnyR1JEyqvkYwvglmz%2F7lIqXHpeWdPtZ2uvawqHymKSloUrsssTCBTnU6a&X-Amz-Signature=e7dd10d9322f14de3109b3776be3b0858f0afa4a3c3179485d749362ea402d08&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUSVCUQ2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIAwt5HRLCXu8moBrOe8S%2B293FM1Tog%2FcMcxH%2FbR6UoVkAiB54bJWnhL5I969LBWqJsT%2FWwg%2FMmkdwYIq09Hv2c6KrCr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMxaJCNn10Gx00o1vyKtwD8kEPibRkQS0mhIq5OqWfv3xhoQzZpq9mIg%2BQycyx5%2FrecGvjejNcGUmr3m4sVxhpysVZ44lObhbT481OZgDInD53lQdGZr4VkMUWCw5Vb%2Ft6CtQcAv2a16pesiq7szi1U0jCEM%2FyFb4yBYtBqYSFF9gW4S0GxzvXlR7QWWEa2iC7EQ0o%2FQwZAM0BBNDmP8AVEivVDdOrMfTcV4kyC85uRTvfrndEWniS2qAhA2xIIf9gpE06x%2B%2F90jsSr4Br%2B%2Bf%2B8pWqQCTmp7V42P5rjJUaAANWniHHBIBnWsP6nxnEbAOgnFWlzMuOTqqdOayohwbjas8g7M9ahKGWQVLYPtsgShrBfeK51a3UwQm%2FLtz75KaHavrPfrJAmTcCpg2udNEbt%2FP59ZI48301NyhPBVgRZYIQUFg9YJ4Qdatcqm1xuvG3K1UA5092sT5SB5j9q5%2FhX%2B09I0NchJt5ApDcZWJQR52PeqMu9nuM2OV7Wsb224fRL2ykwjdqs%2BL5%2BaRBIVgA%2FKc17kUJqfthwm2TxEGaI%2BIH4cbHxpH2GSKUuXyP7g69yLnF6ZOBBn6jbOaVMROmHFBH1a7MWnGScJh2v8ZA4vU9nbCfvcB%2FdQDzQYebmy8ArZgs%2FtLC5%2FuMse8w8aCJvQY6pgE2R%2Fhc6itMzDuAeHr9j%2F6thOnWoihtJQbLf3rd54z%2BO%2BYAuaUQwISAIS9bwiqfie%2F%2FTwkTe2mYoel1rXmVP7Tznm2eE8MfgN%2F9SZQS0oxrQOh0t3qeDE6SbNqZheDjCZ%2Bk8qRXfUZlCs9YU9K0b4RZQM%2Fswe5R8gq2ihpFLd4d27pWRyJtXcZS6sTxYgKObc0RKMcCv8gaxmA%2FjR2ZiAyVN4vTZskH&X-Amz-Signature=3ed5419b4606000c546011d4d8f56e91100e3ce84f9397416f05c07c234f5003&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ANHUBU3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQCS%2FYZ3beWl4NQfAJnz%2FmwN9Cpr3Nmr2s%2BiOnM7g%2Fzi8AIgc4v6B4OBjtQwGav636UfckORmPga56HO8jS%2F%2BjuwsBMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDNp06qN0%2Fjf1qfAf9ircA8u54FzrCDY%2BH2c08OWYWlg51OjAycvfo6ZKvvqJcBvdJKy8jx4SV5cN0AvCZcqwQcqz2iCTUEriNh7kPecJoOQupIWbnJnpQqTUMCSKlVtmdtCKFfizCxmNMS5C4jznfAkDjLootVmmXs6jAsR%2FUB19m3fmxsqG4rizUQ%2Bg%2Fkj4KrgZfzF5PpC8RnpTN49VPlC9qTiOnayRoV9c8YZi6p6A7MJ1r5H%2FFOSLJF%2FAVqnnn0TwAP%2Bw%2BqBhHmQ1bxi%2B%2BuKdQMNlRpnnl%2FmB5dBRFUEf1GhjLFRhXui8Davi6Vnz%2Fgi%2B7IVw0PPXs5SaduiUlJc3FcbwCQeqlkjLEaJ7NcTqI4%2FwrL6fDzETa6eBRYhaJLhSLo28ofPXoreOnrRAT4SeI2XaYZfb%2FA8YqHlCnFmub%2B9BvUo43dC0tBo0FF2yHHlqmJn4GxgICXe9RfRI2wXoLDFlvvlk7ab5wdL7B4GkGogCkQKsaodfaxhS0V7BV0tpHIyMEwdF0x2lPZ%2FaWt0JQpBhV673mkxzYlMawQ3YRjfVhQ63xGA4ux%2FP3MeWSYR8lAxopMQHO%2Be%2BycuotheZmcaFqKrQPoAGqLEcrVUkm673jC1zhloorsi4E61fHK6xxuOaTjlaym1tMKOhib0GOqUBU4q0lz%2Bdu%2Fsx7S579Ll9QrJrP2UEfULsCrj41QGtntiw1Yzr1Sy4RCoR5QRK%2BMq6KBessWpfUC7zOsmMbUpG36UeNxNEfFL9qZVUTk1A2k8xrNeaTJjcPVg%2FTQeBVk7%2Bcs5OECOdgG9dpq%2Fq6noUNUe%2FcyN7oyoGAqgoRw4GHyPjJ%2FByQIqYqv2G4btKpCQeBwN3EvSOATnBZw9ow4U%2FWhhzAuYL&X-Amz-Signature=261cfb0b261df5a0b0dfa2dc07e4ac3b820f809123c8d90870ed1ae1991ed511&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAROF4GU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDdPmlY%2FMFhMr7G5uYvEF%2FUebnGeXzU4TQWUdOmZ2f%2BKAIgU9f%2BT2a6vboGHQYvF9a4IFbTTKxc02ey0ChtUhDZCl0q%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDNyEgv2HjoJ1GfKa%2FyrcA%2Fgv1B5LF%2FWYuiScSTPr7ZY5UEYYWz9YVvfCYyYSRglyQfvHmUNsvY0yBXE8qpKZFe2LkvEY679vJn649B42wHTyF9KqsXyW8ALVSoccKFy2X6%2BDTAbU54%2BfGMDDBKpBZPT1c73YwuphTnJDdLPLOSejP1WwRpXXkMbG%2BdYNi7z5gKxw0flvS43a%2FrXwoQPY5kGQBQ%2BmyrVyThobF8MUrYr1bM1bpDoWSv6lFozaLnuGRa%2F7PdYJAovmkuItszxVIpOj7Xbl0PjTnDeApzaYRNoeBn%2FMSBko5PYoFzNnD1BwcwAan4aS4vJmetLlBT7JCohRUmNB8CyvDBmXdzr%2F9FWHDe1QxDJQo8pJ74ZEO6YvpiZttW1KjuQ0qALimefEjQT54oNCgUQs9aUlDalczZnS84ixDHrMxJb1oxudP5JOUOT4%2FH5xeOP1ZtbFy%2BkShvwj9qExC3ELSv0%2F%2BSdfdiOCgvRiDhvtntlmfzR52TuvdQ77Jo5malw3cCv3DzVB%2FyrCiqgiY3B5oRgPBWMAX5te29yzFkiFcPkG6a%2BYvOvQiOGaJVgAeohGZgD3H2q8VARzmwYmHBA0NGn3p4GUJ%2FcYS%2FXkMYzTUahtU9ZqDwxmnOpYtd%2BBqrMe2PQEMO%2Bgib0GOqUBITgLulPlAl2rt8w9KQlz%2FKcBhAXiDehJQ20DeMDyice0p59dI3F%2Fv%2BzAmzCUGqU1kK3NZ2QPjLBA5fq%2BeqfQPRYXs80NglCkPJ5cBx6L5kIj%2FTJTTq4TyvCUa%2FRDuZbxLTRR%2BtlqNwyJ8WHTrhx%2BJDzXfmhm9Ust9ykNt1ZkOdOe9okQzYxFGtW5beSeQ30zj%2Fg4M9jh7uESn6rLPEoCcA7p3KjD&X-Amz-Signature=450d85392423c0a66fddf0527d47dbb3774e459b21902ff62dc62a9ab1a75673&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646MZUJ35%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC8JT0oLkP5qC0P%2Fl2PT9hqJJ0YNr4l9DpNwOKdIM6JYAiBU%2B%2F8o%2BRIHBo5jYgX4dTnE39Eq1aH4RfG%2BA83X3fn38ir%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMAkGpFPeJLEsVHk03KtwDNLjtFQD8Lgcz4WcqQxVrP9A5H87CKPc9Q0K4TLGaAMK4%2Fuf8tFEoTebeUvqieQYLp89LJ91Q2gpApnGQb3uoFPXPT9iyxNXA7468lbkxTGh58fHAhZ1z5GRV2Mh4Q4IiIp5Y1BEnirv%2FyWPuL297eTuoa8NSuLo8wuV27wV8dUcqTSSiFiI%2F6oPIqSV7FYzG8hm25I04jOmRmAUFeblwhgqUBOHiIfBwv7MgyzOpwrX8dMEFEGmCCSGaozMw%2BdcniXo9p5B9tsDDz3FGV2FWboLVxR%2BqpTQXU2AQxZLMrYc4cSfecUn1Ji0%2FGDuxPI9d1LE7YT73ephFTfSlLU0ElOhw3O1wJXpCCFo99gF7njBsZCbMAwrwbBEzxMGoHbXbY%2Fg2V5floQYa%2FCc7n%2FPMQ6ojYytc6gPjX3OwMZp%2BKtTSwFQs9%2BjAq%2BtkTREvu8BldtY0KcxQLpZayA%2FKfcb11n9jws%2Bn5w1%2BvUZxQJUuGYJ%2FQXi0nvnPrl0O0FKbOTKvSVlDXcIBQYUbGu5H8WsuPOkQbsR5w0jNbqY9EQTdnB1jvb71P2opgitpeywnobLEy6MQCu8XIImmusy35Xex9FskpvkWwvq98C%2BW4XOhRzfDsgToRNwDOdOa%2FAAw%2BaCJvQY6pgEDehnnDoyuCtUp5b18Hn3K8va185AzGXwT1Gii4itKMu4HUZ%2BW%2BppGpUCoPpTrOj981fhWUULCxnKp3Aly1IYJo2q5Q%2BMXLiFjXcNVwexbrFkqnKx%2FZSb9%2BERBMk0RhlaECPnKpxESKBokC2PkT8frLvqfoSBqcdk%2BE9phUMrP2zrRRr7YiNyFsjjGu1bOTGd3T7n0QQtgW%2B9UNhdE1hGeHI%2BvguNo&X-Amz-Signature=b1bd927753c6dadda62616b6e8672c2384fcfb02b1f2ed8807c80da8fa917b1b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646MZUJ35%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC8JT0oLkP5qC0P%2Fl2PT9hqJJ0YNr4l9DpNwOKdIM6JYAiBU%2B%2F8o%2BRIHBo5jYgX4dTnE39Eq1aH4RfG%2BA83X3fn38ir%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMAkGpFPeJLEsVHk03KtwDNLjtFQD8Lgcz4WcqQxVrP9A5H87CKPc9Q0K4TLGaAMK4%2Fuf8tFEoTebeUvqieQYLp89LJ91Q2gpApnGQb3uoFPXPT9iyxNXA7468lbkxTGh58fHAhZ1z5GRV2Mh4Q4IiIp5Y1BEnirv%2FyWPuL297eTuoa8NSuLo8wuV27wV8dUcqTSSiFiI%2F6oPIqSV7FYzG8hm25I04jOmRmAUFeblwhgqUBOHiIfBwv7MgyzOpwrX8dMEFEGmCCSGaozMw%2BdcniXo9p5B9tsDDz3FGV2FWboLVxR%2BqpTQXU2AQxZLMrYc4cSfecUn1Ji0%2FGDuxPI9d1LE7YT73ephFTfSlLU0ElOhw3O1wJXpCCFo99gF7njBsZCbMAwrwbBEzxMGoHbXbY%2Fg2V5floQYa%2FCc7n%2FPMQ6ojYytc6gPjX3OwMZp%2BKtTSwFQs9%2BjAq%2BtkTREvu8BldtY0KcxQLpZayA%2FKfcb11n9jws%2Bn5w1%2BvUZxQJUuGYJ%2FQXi0nvnPrl0O0FKbOTKvSVlDXcIBQYUbGu5H8WsuPOkQbsR5w0jNbqY9EQTdnB1jvb71P2opgitpeywnobLEy6MQCu8XIImmusy35Xex9FskpvkWwvq98C%2BW4XOhRzfDsgToRNwDOdOa%2FAAw%2BaCJvQY6pgEDehnnDoyuCtUp5b18Hn3K8va185AzGXwT1Gii4itKMu4HUZ%2BW%2BppGpUCoPpTrOj981fhWUULCxnKp3Aly1IYJo2q5Q%2BMXLiFjXcNVwexbrFkqnKx%2FZSb9%2BERBMk0RhlaECPnKpxESKBokC2PkT8frLvqfoSBqcdk%2BE9phUMrP2zrRRr7YiNyFsjjGu1bOTGd3T7n0QQtgW%2B9UNhdE1hGeHI%2BvguNo&X-Amz-Signature=44faadc42d7babb01c3398a189fff0fd24beb03a09e0a2cde3dec4cf0e9fc98b&X-Amz-SignedHeaders=host&x-id=GetObject)

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
