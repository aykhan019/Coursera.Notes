

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGKLRIWF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDcZbsQcWPuayfoza%2Fl%2F8RrE1r6ri0I5i0q69%2FZKRkAhwIgUOQDaUjzaErQE00XWp8m%2F9aTD0uTnuMIuDRHcjExRtMq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDKXAQS14DD73bmb4wircAyHZWUoZjoud28SR6Wgh6XbqBJyCwX91NV0RN2ZJiq9o%2Fg4DPKmB%2FPmoMpKQgglcVX2fwEn7rt8L3aYMMGStqkqmI7HVvC71ZaNkLVPStGHVQyBUTUZNIHe7MqKiZaCXtjIWtZF972hao6oEiV0BL6GlR8HMyHgIaNKgUefyozqz4oAPKboheE67mP9TmxSQGj2vi8lhsPq3ZgVX5i1HhhqUJYqBW%2FapITcW7BbrL56IMIE4qw4xnrHL8B9ee8om2ZxbUoXv6ZTJrYC7%2BGIIIZ0voo%2BJIl6S%2Fwlrft3pvXAW6gJLgPs3sdvTtpSGeCf0KqstIKa5MPbgE67BC%2F%2BUY%2BHVhC79xflaznXRvjeKQTQ0zS7y0W1WyV8xtTNq%2B03JxU9BDiJdawwY4Y5g0nwpFJkz3iQqEgMZy5Iu7HW%2FFUMuzhVUoEOOSirPhIT3uGhlEK8kLzkRySM4E3xpWdaPCd4F77pdsjK0hsfH9ejKwLfk8huUaEXV6GJB93fe7EKVm728LcJPm281%2BNvnJqtyw6xSp511ndPvFuNW23UIPmFGXiE7DKtlPI%2BN53IpMCiRYmw17ZcU8OxFXzdoOi67avQWcWq9KWpqeD47cTkmUzickP1yn%2BewREz2g77MMJ%2B9hL0GOqUB%2FotC5sVxm7Y7Q3yv2gjmPyIz0l5MUi%2BYMyNpnYqyYgtn9QTt4kudcE91Bz08%2FeA1johyE7fdDTX0Y9mxpTqaQe8RffaFAeRl%2FLwkWGP17%2BIGRss76PSlTUGx3X5AcJgMleSTBQ86QzHck2TjkOW8Wo5EhSLbVPAShXYA54NCS6AAUSZCWq4U1C768QFZs0%2BKZ3nSJMjyq46DGUE%2Be9KO2N3hKDin&X-Amz-Signature=3cee038371d1306749614b956908e2237196086daea84f965efe278640557343&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGKLRIWF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDcZbsQcWPuayfoza%2Fl%2F8RrE1r6ri0I5i0q69%2FZKRkAhwIgUOQDaUjzaErQE00XWp8m%2F9aTD0uTnuMIuDRHcjExRtMq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDKXAQS14DD73bmb4wircAyHZWUoZjoud28SR6Wgh6XbqBJyCwX91NV0RN2ZJiq9o%2Fg4DPKmB%2FPmoMpKQgglcVX2fwEn7rt8L3aYMMGStqkqmI7HVvC71ZaNkLVPStGHVQyBUTUZNIHe7MqKiZaCXtjIWtZF972hao6oEiV0BL6GlR8HMyHgIaNKgUefyozqz4oAPKboheE67mP9TmxSQGj2vi8lhsPq3ZgVX5i1HhhqUJYqBW%2FapITcW7BbrL56IMIE4qw4xnrHL8B9ee8om2ZxbUoXv6ZTJrYC7%2BGIIIZ0voo%2BJIl6S%2Fwlrft3pvXAW6gJLgPs3sdvTtpSGeCf0KqstIKa5MPbgE67BC%2F%2BUY%2BHVhC79xflaznXRvjeKQTQ0zS7y0W1WyV8xtTNq%2B03JxU9BDiJdawwY4Y5g0nwpFJkz3iQqEgMZy5Iu7HW%2FFUMuzhVUoEOOSirPhIT3uGhlEK8kLzkRySM4E3xpWdaPCd4F77pdsjK0hsfH9ejKwLfk8huUaEXV6GJB93fe7EKVm728LcJPm281%2BNvnJqtyw6xSp511ndPvFuNW23UIPmFGXiE7DKtlPI%2BN53IpMCiRYmw17ZcU8OxFXzdoOi67avQWcWq9KWpqeD47cTkmUzickP1yn%2BewREz2g77MMJ%2B9hL0GOqUB%2FotC5sVxm7Y7Q3yv2gjmPyIz0l5MUi%2BYMyNpnYqyYgtn9QTt4kudcE91Bz08%2FeA1johyE7fdDTX0Y9mxpTqaQe8RffaFAeRl%2FLwkWGP17%2BIGRss76PSlTUGx3X5AcJgMleSTBQ86QzHck2TjkOW8Wo5EhSLbVPAShXYA54NCS6AAUSZCWq4U1C768QFZs0%2BKZ3nSJMjyq46DGUE%2Be9KO2N3hKDin&X-Amz-Signature=0813a06114fe98521977fed450c05b3d19f48d5ab62ed207e4edd2b835077fe0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGKLRIWF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDcZbsQcWPuayfoza%2Fl%2F8RrE1r6ri0I5i0q69%2FZKRkAhwIgUOQDaUjzaErQE00XWp8m%2F9aTD0uTnuMIuDRHcjExRtMq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDKXAQS14DD73bmb4wircAyHZWUoZjoud28SR6Wgh6XbqBJyCwX91NV0RN2ZJiq9o%2Fg4DPKmB%2FPmoMpKQgglcVX2fwEn7rt8L3aYMMGStqkqmI7HVvC71ZaNkLVPStGHVQyBUTUZNIHe7MqKiZaCXtjIWtZF972hao6oEiV0BL6GlR8HMyHgIaNKgUefyozqz4oAPKboheE67mP9TmxSQGj2vi8lhsPq3ZgVX5i1HhhqUJYqBW%2FapITcW7BbrL56IMIE4qw4xnrHL8B9ee8om2ZxbUoXv6ZTJrYC7%2BGIIIZ0voo%2BJIl6S%2Fwlrft3pvXAW6gJLgPs3sdvTtpSGeCf0KqstIKa5MPbgE67BC%2F%2BUY%2BHVhC79xflaznXRvjeKQTQ0zS7y0W1WyV8xtTNq%2B03JxU9BDiJdawwY4Y5g0nwpFJkz3iQqEgMZy5Iu7HW%2FFUMuzhVUoEOOSirPhIT3uGhlEK8kLzkRySM4E3xpWdaPCd4F77pdsjK0hsfH9ejKwLfk8huUaEXV6GJB93fe7EKVm728LcJPm281%2BNvnJqtyw6xSp511ndPvFuNW23UIPmFGXiE7DKtlPI%2BN53IpMCiRYmw17ZcU8OxFXzdoOi67avQWcWq9KWpqeD47cTkmUzickP1yn%2BewREz2g77MMJ%2B9hL0GOqUB%2FotC5sVxm7Y7Q3yv2gjmPyIz0l5MUi%2BYMyNpnYqyYgtn9QTt4kudcE91Bz08%2FeA1johyE7fdDTX0Y9mxpTqaQe8RffaFAeRl%2FLwkWGP17%2BIGRss76PSlTUGx3X5AcJgMleSTBQ86QzHck2TjkOW8Wo5EhSLbVPAShXYA54NCS6AAUSZCWq4U1C768QFZs0%2BKZ3nSJMjyq46DGUE%2Be9KO2N3hKDin&X-Amz-Signature=64cc65b413ef2edf00c060bc99dbbb01a6d4844b62de5a737b1234b50c8efcb5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUNGUAL2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEoNDdVAGKp%2B25LSZwx%2B5kNKrdgzx5Ty3gLz4a7rQ0LsAiAO2BcfooWhP95u%2BSEHoMNKbmVlj4yYqCWGBssKgV3RyCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMi43wByRtjPpnqU89KtwDvZdgy5pbz4OHO4rRUQ55fOcJIQKFdJs5xhMmY6%2F9uN8vm59xrcYqeavZMUrKFoGVfVoDwc7bezDOdUr1NA%2B8XkZz29QAD1W5R7xbYg2%2B2pHW6yqtZVhKz3NXCs2oy8M%2F0JGcCL2Fa9QNBveXMXcDpC78BaEkFZcl%2BrfCzAdR%2FzZY%2BJlfzqKhFkKXO1WCkbA0cwKpQzxxnO6D5Da%2BtqWGK%2FeGMbZVBSc%2B9Zw0PSR2SBgyFzR9XVK3fWpmpiCyDlI0Wj%2BQ3LNMiUBqdV%2BZ0vE%2BXkmaMK2F%2BQb3jQJmZ6hateCet705VlvozO777jN4Z6q%2BdC%2BQb%2BKSVOa%2F6UpwtQr3Dpwq48iecuVXFe9bkE101RezC%2F8hP%2BQeZDczuPh5TNYvM7EWPp6goGI%2FMQg4njckHHw28fUkhn15sfDHgF4It0FZPc0SjZWxaZ6CjD8fdnrnulDlNDBfy8ImwStHjgJbkYW0CgcuMfan6PIwdgIk%2FqKkAxt6OVhuRQRKdQFTYYd2ifDieEbgv4ca1Qf%2F9uRFcG%2FTCt8CZaBmyOnfXOLajiJrH5NKZdp%2B6VFnaeUa1eiEQdNnNvfW%2FaG2I0y%2BTmL173AsKst4ZYEiC4SMcM1g9bdOdjkRHCczg%2BQoaxkwl72EvQY6pgFxCrMeMEH7ZCZbqPzY1Z%2F023nc%2F1Dci0g5ECVREcrKE9QOFGCFACm3WD8T%2Facw1qbeIPdOMl10SMGuSCeav5O%2BUHkyai%2BUVjI4D2rcgRWqMYWMrFy4WowAzF0Cx6%2Fb4VVZq%2F%2FcLG%2F5E24DUBFN%2Be7xrkC5ssMVQ09cRkRH2yZGaTJ6rksw9w0ubvpM83DI4mFIhJtQgFF2%2B4VRdLqojsuKkWR3eylD&X-Amz-Signature=bc56c76592a1518ef35e70a39d1d03703cff2f7c3ce7e831d27c4f2e90a0f879&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUNGUAL2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEoNDdVAGKp%2B25LSZwx%2B5kNKrdgzx5Ty3gLz4a7rQ0LsAiAO2BcfooWhP95u%2BSEHoMNKbmVlj4yYqCWGBssKgV3RyCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMi43wByRtjPpnqU89KtwDvZdgy5pbz4OHO4rRUQ55fOcJIQKFdJs5xhMmY6%2F9uN8vm59xrcYqeavZMUrKFoGVfVoDwc7bezDOdUr1NA%2B8XkZz29QAD1W5R7xbYg2%2B2pHW6yqtZVhKz3NXCs2oy8M%2F0JGcCL2Fa9QNBveXMXcDpC78BaEkFZcl%2BrfCzAdR%2FzZY%2BJlfzqKhFkKXO1WCkbA0cwKpQzxxnO6D5Da%2BtqWGK%2FeGMbZVBSc%2B9Zw0PSR2SBgyFzR9XVK3fWpmpiCyDlI0Wj%2BQ3LNMiUBqdV%2BZ0vE%2BXkmaMK2F%2BQb3jQJmZ6hateCet705VlvozO777jN4Z6q%2BdC%2BQb%2BKSVOa%2F6UpwtQr3Dpwq48iecuVXFe9bkE101RezC%2F8hP%2BQeZDczuPh5TNYvM7EWPp6goGI%2FMQg4njckHHw28fUkhn15sfDHgF4It0FZPc0SjZWxaZ6CjD8fdnrnulDlNDBfy8ImwStHjgJbkYW0CgcuMfan6PIwdgIk%2FqKkAxt6OVhuRQRKdQFTYYd2ifDieEbgv4ca1Qf%2F9uRFcG%2FTCt8CZaBmyOnfXOLajiJrH5NKZdp%2B6VFnaeUa1eiEQdNnNvfW%2FaG2I0y%2BTmL173AsKst4ZYEiC4SMcM1g9bdOdjkRHCczg%2BQoaxkwl72EvQY6pgFxCrMeMEH7ZCZbqPzY1Z%2F023nc%2F1Dci0g5ECVREcrKE9QOFGCFACm3WD8T%2Facw1qbeIPdOMl10SMGuSCeav5O%2BUHkyai%2BUVjI4D2rcgRWqMYWMrFy4WowAzF0Cx6%2Fb4VVZq%2F%2FcLG%2F5E24DUBFN%2Be7xrkC5ssMVQ09cRkRH2yZGaTJ6rksw9w0ubvpM83DI4mFIhJtQgFF2%2B4VRdLqojsuKkWR3eylD&X-Amz-Signature=38a327f638c9d709a841b27f1fe9d1e6d64d7d134cd3b5f1c40ddd004420b92c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUNGUAL2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEoNDdVAGKp%2B25LSZwx%2B5kNKrdgzx5Ty3gLz4a7rQ0LsAiAO2BcfooWhP95u%2BSEHoMNKbmVlj4yYqCWGBssKgV3RyCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMi43wByRtjPpnqU89KtwDvZdgy5pbz4OHO4rRUQ55fOcJIQKFdJs5xhMmY6%2F9uN8vm59xrcYqeavZMUrKFoGVfVoDwc7bezDOdUr1NA%2B8XkZz29QAD1W5R7xbYg2%2B2pHW6yqtZVhKz3NXCs2oy8M%2F0JGcCL2Fa9QNBveXMXcDpC78BaEkFZcl%2BrfCzAdR%2FzZY%2BJlfzqKhFkKXO1WCkbA0cwKpQzxxnO6D5Da%2BtqWGK%2FeGMbZVBSc%2B9Zw0PSR2SBgyFzR9XVK3fWpmpiCyDlI0Wj%2BQ3LNMiUBqdV%2BZ0vE%2BXkmaMK2F%2BQb3jQJmZ6hateCet705VlvozO777jN4Z6q%2BdC%2BQb%2BKSVOa%2F6UpwtQr3Dpwq48iecuVXFe9bkE101RezC%2F8hP%2BQeZDczuPh5TNYvM7EWPp6goGI%2FMQg4njckHHw28fUkhn15sfDHgF4It0FZPc0SjZWxaZ6CjD8fdnrnulDlNDBfy8ImwStHjgJbkYW0CgcuMfan6PIwdgIk%2FqKkAxt6OVhuRQRKdQFTYYd2ifDieEbgv4ca1Qf%2F9uRFcG%2FTCt8CZaBmyOnfXOLajiJrH5NKZdp%2B6VFnaeUa1eiEQdNnNvfW%2FaG2I0y%2BTmL173AsKst4ZYEiC4SMcM1g9bdOdjkRHCczg%2BQoaxkwl72EvQY6pgFxCrMeMEH7ZCZbqPzY1Z%2F023nc%2F1Dci0g5ECVREcrKE9QOFGCFACm3WD8T%2Facw1qbeIPdOMl10SMGuSCeav5O%2BUHkyai%2BUVjI4D2rcgRWqMYWMrFy4WowAzF0Cx6%2Fb4VVZq%2F%2FcLG%2F5E24DUBFN%2Be7xrkC5ssMVQ09cRkRH2yZGaTJ6rksw9w0ubvpM83DI4mFIhJtQgFF2%2B4VRdLqojsuKkWR3eylD&X-Amz-Signature=ae8eb5e52c2a547b25c6f6f21d51ed520035198cc3c63c2390f82ea8322ad00d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUNGUAL2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEoNDdVAGKp%2B25LSZwx%2B5kNKrdgzx5Ty3gLz4a7rQ0LsAiAO2BcfooWhP95u%2BSEHoMNKbmVlj4yYqCWGBssKgV3RyCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMi43wByRtjPpnqU89KtwDvZdgy5pbz4OHO4rRUQ55fOcJIQKFdJs5xhMmY6%2F9uN8vm59xrcYqeavZMUrKFoGVfVoDwc7bezDOdUr1NA%2B8XkZz29QAD1W5R7xbYg2%2B2pHW6yqtZVhKz3NXCs2oy8M%2F0JGcCL2Fa9QNBveXMXcDpC78BaEkFZcl%2BrfCzAdR%2FzZY%2BJlfzqKhFkKXO1WCkbA0cwKpQzxxnO6D5Da%2BtqWGK%2FeGMbZVBSc%2B9Zw0PSR2SBgyFzR9XVK3fWpmpiCyDlI0Wj%2BQ3LNMiUBqdV%2BZ0vE%2BXkmaMK2F%2BQb3jQJmZ6hateCet705VlvozO777jN4Z6q%2BdC%2BQb%2BKSVOa%2F6UpwtQr3Dpwq48iecuVXFe9bkE101RezC%2F8hP%2BQeZDczuPh5TNYvM7EWPp6goGI%2FMQg4njckHHw28fUkhn15sfDHgF4It0FZPc0SjZWxaZ6CjD8fdnrnulDlNDBfy8ImwStHjgJbkYW0CgcuMfan6PIwdgIk%2FqKkAxt6OVhuRQRKdQFTYYd2ifDieEbgv4ca1Qf%2F9uRFcG%2FTCt8CZaBmyOnfXOLajiJrH5NKZdp%2B6VFnaeUa1eiEQdNnNvfW%2FaG2I0y%2BTmL173AsKst4ZYEiC4SMcM1g9bdOdjkRHCczg%2BQoaxkwl72EvQY6pgFxCrMeMEH7ZCZbqPzY1Z%2F023nc%2F1Dci0g5ECVREcrKE9QOFGCFACm3WD8T%2Facw1qbeIPdOMl10SMGuSCeav5O%2BUHkyai%2BUVjI4D2rcgRWqMYWMrFy4WowAzF0Cx6%2Fb4VVZq%2F%2FcLG%2F5E24DUBFN%2Be7xrkC5ssMVQ09cRkRH2yZGaTJ6rksw9w0ubvpM83DI4mFIhJtQgFF2%2B4VRdLqojsuKkWR3eylD&X-Amz-Signature=ced3235e025a37c6d43c68d0403b6504d2d4180d3e4d5e834e3ba61f0c6416af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUNGUAL2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEoNDdVAGKp%2B25LSZwx%2B5kNKrdgzx5Ty3gLz4a7rQ0LsAiAO2BcfooWhP95u%2BSEHoMNKbmVlj4yYqCWGBssKgV3RyCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMi43wByRtjPpnqU89KtwDvZdgy5pbz4OHO4rRUQ55fOcJIQKFdJs5xhMmY6%2F9uN8vm59xrcYqeavZMUrKFoGVfVoDwc7bezDOdUr1NA%2B8XkZz29QAD1W5R7xbYg2%2B2pHW6yqtZVhKz3NXCs2oy8M%2F0JGcCL2Fa9QNBveXMXcDpC78BaEkFZcl%2BrfCzAdR%2FzZY%2BJlfzqKhFkKXO1WCkbA0cwKpQzxxnO6D5Da%2BtqWGK%2FeGMbZVBSc%2B9Zw0PSR2SBgyFzR9XVK3fWpmpiCyDlI0Wj%2BQ3LNMiUBqdV%2BZ0vE%2BXkmaMK2F%2BQb3jQJmZ6hateCet705VlvozO777jN4Z6q%2BdC%2BQb%2BKSVOa%2F6UpwtQr3Dpwq48iecuVXFe9bkE101RezC%2F8hP%2BQeZDczuPh5TNYvM7EWPp6goGI%2FMQg4njckHHw28fUkhn15sfDHgF4It0FZPc0SjZWxaZ6CjD8fdnrnulDlNDBfy8ImwStHjgJbkYW0CgcuMfan6PIwdgIk%2FqKkAxt6OVhuRQRKdQFTYYd2ifDieEbgv4ca1Qf%2F9uRFcG%2FTCt8CZaBmyOnfXOLajiJrH5NKZdp%2B6VFnaeUa1eiEQdNnNvfW%2FaG2I0y%2BTmL173AsKst4ZYEiC4SMcM1g9bdOdjkRHCczg%2BQoaxkwl72EvQY6pgFxCrMeMEH7ZCZbqPzY1Z%2F023nc%2F1Dci0g5ECVREcrKE9QOFGCFACm3WD8T%2Facw1qbeIPdOMl10SMGuSCeav5O%2BUHkyai%2BUVjI4D2rcgRWqMYWMrFy4WowAzF0Cx6%2Fb4VVZq%2F%2FcLG%2F5E24DUBFN%2Be7xrkC5ssMVQ09cRkRH2yZGaTJ6rksw9w0ubvpM83DI4mFIhJtQgFF2%2B4VRdLqojsuKkWR3eylD&X-Amz-Signature=bbd65603949ebd8fabf358a138e83ffbe7a6c0371bb3b1cbccb7022c02801aaa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUNGUAL2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEoNDdVAGKp%2B25LSZwx%2B5kNKrdgzx5Ty3gLz4a7rQ0LsAiAO2BcfooWhP95u%2BSEHoMNKbmVlj4yYqCWGBssKgV3RyCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMi43wByRtjPpnqU89KtwDvZdgy5pbz4OHO4rRUQ55fOcJIQKFdJs5xhMmY6%2F9uN8vm59xrcYqeavZMUrKFoGVfVoDwc7bezDOdUr1NA%2B8XkZz29QAD1W5R7xbYg2%2B2pHW6yqtZVhKz3NXCs2oy8M%2F0JGcCL2Fa9QNBveXMXcDpC78BaEkFZcl%2BrfCzAdR%2FzZY%2BJlfzqKhFkKXO1WCkbA0cwKpQzxxnO6D5Da%2BtqWGK%2FeGMbZVBSc%2B9Zw0PSR2SBgyFzR9XVK3fWpmpiCyDlI0Wj%2BQ3LNMiUBqdV%2BZ0vE%2BXkmaMK2F%2BQb3jQJmZ6hateCet705VlvozO777jN4Z6q%2BdC%2BQb%2BKSVOa%2F6UpwtQr3Dpwq48iecuVXFe9bkE101RezC%2F8hP%2BQeZDczuPh5TNYvM7EWPp6goGI%2FMQg4njckHHw28fUkhn15sfDHgF4It0FZPc0SjZWxaZ6CjD8fdnrnulDlNDBfy8ImwStHjgJbkYW0CgcuMfan6PIwdgIk%2FqKkAxt6OVhuRQRKdQFTYYd2ifDieEbgv4ca1Qf%2F9uRFcG%2FTCt8CZaBmyOnfXOLajiJrH5NKZdp%2B6VFnaeUa1eiEQdNnNvfW%2FaG2I0y%2BTmL173AsKst4ZYEiC4SMcM1g9bdOdjkRHCczg%2BQoaxkwl72EvQY6pgFxCrMeMEH7ZCZbqPzY1Z%2F023nc%2F1Dci0g5ECVREcrKE9QOFGCFACm3WD8T%2Facw1qbeIPdOMl10SMGuSCeav5O%2BUHkyai%2BUVjI4D2rcgRWqMYWMrFy4WowAzF0Cx6%2Fb4VVZq%2F%2FcLG%2F5E24DUBFN%2Be7xrkC5ssMVQ09cRkRH2yZGaTJ6rksw9w0ubvpM83DI4mFIhJtQgFF2%2B4VRdLqojsuKkWR3eylD&X-Amz-Signature=054b2ae50a624499fdb6fbdd1d6f4bc7d1a711353fb488fc117064c55e40bdf4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M6RJEGH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQCzNEN3zKLjRS4%2BKqpY68ihC8HVAiCPWTDouek%2BGil2iAIhANvLDB74jEXHe6gWyhUzkWhsYHNXLb2iD8abSkAe5HzdKv8DCB0QABoMNjM3NDIzMTgzODA1Igxas%2BdU1w9hX56gOpkq3AMdJNavLr0ZaH9afO7aBMXLP%2FCxI2K3iF7zEXujXwtl1lj93KQBe57AtOhV%2FOuwr0NNySoXGatMsyzXspIwiU2FpwqCpi5iZkCo0htHhnnCnmW8SN9em0FW%2F7y6K8jDPShI2EY5IBsuLFoFiu5wXFABSVySBms0ximhoMXa5UUl84BJrpV4EndawLdfbG%2FAyFI9DW1zeLSVKcUhf9rsHIj0UdssFaYkCAk25sLULdcaXDpr2DqM8EmrgHh3d%2BVji%2BgQ6aU2tidKAKf93yD6YvMFnBMxxIfSe9B10oW9Gof%2FkLnb1D%2Bvv0%2FSII99pcdjxdcsOkdRWjgSFU%2FPF6Ai77PpQJvg9RoxZfZbLKrR12RRphhITvdHqbrTPw5i8G12%2BnQKQrIyq8i2ws1kXnb3%2BamERHJBlcR28egODX%2FC0FBMklznI2JoPJFpNYUIiiy6d1ek08An6NjBMt%2FlfepNWyy%2FsGZa7%2BXTWLc8DYrJ5z2ws74o94H9v4FThh7ZPAAr%2BymwZ6HjMDyz3CTDqynnL4QMFTiOBh2GSCcFmTtk9tZ1cvvVRkan7xjtFAJPp%2BEpX8EKgdmZOEmq4ha%2FcOR2nsyf%2B7j4UaOZee7w1GmR5FWwsZ9uGxHYzGLy4s1KqDDzvIS9BjqkAaIN56i8Nj7V%2B%2FsWEonGNPMyD8VjkEnJVAmsXMt%2BS3aH7WfsPN0F5TF4eXldX8hYn8D5FgrZV0CCvt7uoWt8mo30TEgXu5gOpQBtT3LXy0w58%2Bz%2BZOHS8uNsbvSRNSZQ4EXZRrE%2BTQ4tmWdWcNtSORn9M3aGAMFOWjEESRmMwtn9gpmyZCvlZvKqAhm4yeOSRCSZjrGBY%2B8I24mYPgvR%2Fnj%2BLckE&X-Amz-Signature=de6d5b32c0eda33ca629c7095e3006445425c0dd2af3dc085183dca8dea35d38&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZ3WAV4F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIGKT2Ay4SSmtD6SzPifVKjGdkxQe8uHv6v3fNkWhVTBaAiEA2ZGuWeuPpQzazVCaIsskylQiMdTKGamt5hqyQUyQe9wq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDBt3VstIC0vuC8oedyrcA2x0Aqj6l9QPF2b9AZxB%2BWaDHZQYuB%2BeGrT9vwBADqHDa0935EqBBZZk4tjyXNm9uLd2mLqa5l8eb8K05Zh3y745ArWntl1d4UAbqXXmCoHOb%2BrYPBX2mCfLbHlTR8rkO46rSuUZU3GCiT90hgFNbO6N3CKHGtjt511aMkRDeCwJdPTYV5Hbjypd8sr6u25T2cQ5fhvDQke3HuQkb7RrClBEJ3kJQIR8bIT7ic11SUKXq2xtM94z7xzu5qj0T4o99UHPQEyCl%2BPvxnldL1CX8qbomsG2IW3zvWiF%2BISK1ZKwyuj4HuzG0508R5HtdOnvIwdPfo45%2BqOXMmIOpM9r3hNGHMgvqSajkckCLq04E1gGG3K%2BK264Q8iou499aoWb%2FrBs8Do4Jw0vUW9yb3O%2F9sP2hWenQpp1EGg0XJA2lVp3oGfabUE4apyFtjEP%2BiV6fEpjNEatk%2FeV8JxwwYHk265zL5choV%2F2H1u0KLYtUXCoxTZyGqlWnp1MHGfUcDNKPyKbyZNlNP2Q1j7LvI%2B2BI3BgBqMWLg6AXupSXGceHY%2Bu8NLhTIZIlmxlFXdgzMOW%2FVdpTufj8WwCBSk1d3SZUzyfhcaUhu6DHPvIbY3PHHjsShenpP5G0M8mMBvMKC9hL0GOqUB7D83jHz5KXGtzZKA7nsX4oCmGN7o9PJOsofy1Y9ynF8H%2Bu2Ombvlob1AxaZp08P6FT9Lm5aCnpmi8ZpZr%2Fw3Z4ESrpDW9Oorv6peeORcIm5HcOMIRdiRNDzlgTDfNHVse9f90Vgj9onfO1G8eCZtnaTt7zXAcqEfrHPBd6gwusuyLDRMTlEKvo97G%2FtzbZv6z9H9MefefvFX0lnzV6YD3o%2FQmQky&X-Amz-Signature=d59529620d7f9495c9c7bb1862f35ec78ee3e6244114759fc94a5e7f61b2acce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUNGUAL2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEoNDdVAGKp%2B25LSZwx%2B5kNKrdgzx5Ty3gLz4a7rQ0LsAiAO2BcfooWhP95u%2BSEHoMNKbmVlj4yYqCWGBssKgV3RyCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMi43wByRtjPpnqU89KtwDvZdgy5pbz4OHO4rRUQ55fOcJIQKFdJs5xhMmY6%2F9uN8vm59xrcYqeavZMUrKFoGVfVoDwc7bezDOdUr1NA%2B8XkZz29QAD1W5R7xbYg2%2B2pHW6yqtZVhKz3NXCs2oy8M%2F0JGcCL2Fa9QNBveXMXcDpC78BaEkFZcl%2BrfCzAdR%2FzZY%2BJlfzqKhFkKXO1WCkbA0cwKpQzxxnO6D5Da%2BtqWGK%2FeGMbZVBSc%2B9Zw0PSR2SBgyFzR9XVK3fWpmpiCyDlI0Wj%2BQ3LNMiUBqdV%2BZ0vE%2BXkmaMK2F%2BQb3jQJmZ6hateCet705VlvozO777jN4Z6q%2BdC%2BQb%2BKSVOa%2F6UpwtQr3Dpwq48iecuVXFe9bkE101RezC%2F8hP%2BQeZDczuPh5TNYvM7EWPp6goGI%2FMQg4njckHHw28fUkhn15sfDHgF4It0FZPc0SjZWxaZ6CjD8fdnrnulDlNDBfy8ImwStHjgJbkYW0CgcuMfan6PIwdgIk%2FqKkAxt6OVhuRQRKdQFTYYd2ifDieEbgv4ca1Qf%2F9uRFcG%2FTCt8CZaBmyOnfXOLajiJrH5NKZdp%2B6VFnaeUa1eiEQdNnNvfW%2FaG2I0y%2BTmL173AsKst4ZYEiC4SMcM1g9bdOdjkRHCczg%2BQoaxkwl72EvQY6pgFxCrMeMEH7ZCZbqPzY1Z%2F023nc%2F1Dci0g5ECVREcrKE9QOFGCFACm3WD8T%2Facw1qbeIPdOMl10SMGuSCeav5O%2BUHkyai%2BUVjI4D2rcgRWqMYWMrFy4WowAzF0Cx6%2Fb4VVZq%2F%2FcLG%2F5E24DUBFN%2Be7xrkC5ssMVQ09cRkRH2yZGaTJ6rksw9w0ubvpM83DI4mFIhJtQgFF2%2B4VRdLqojsuKkWR3eylD&X-Amz-Signature=7a2b86fd16e3f257614e981f0a2a5514596c336c77a39f7f06c551b4cfc63c20&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUNGUAL2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEoNDdVAGKp%2B25LSZwx%2B5kNKrdgzx5Ty3gLz4a7rQ0LsAiAO2BcfooWhP95u%2BSEHoMNKbmVlj4yYqCWGBssKgV3RyCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMi43wByRtjPpnqU89KtwDvZdgy5pbz4OHO4rRUQ55fOcJIQKFdJs5xhMmY6%2F9uN8vm59xrcYqeavZMUrKFoGVfVoDwc7bezDOdUr1NA%2B8XkZz29QAD1W5R7xbYg2%2B2pHW6yqtZVhKz3NXCs2oy8M%2F0JGcCL2Fa9QNBveXMXcDpC78BaEkFZcl%2BrfCzAdR%2FzZY%2BJlfzqKhFkKXO1WCkbA0cwKpQzxxnO6D5Da%2BtqWGK%2FeGMbZVBSc%2B9Zw0PSR2SBgyFzR9XVK3fWpmpiCyDlI0Wj%2BQ3LNMiUBqdV%2BZ0vE%2BXkmaMK2F%2BQb3jQJmZ6hateCet705VlvozO777jN4Z6q%2BdC%2BQb%2BKSVOa%2F6UpwtQr3Dpwq48iecuVXFe9bkE101RezC%2F8hP%2BQeZDczuPh5TNYvM7EWPp6goGI%2FMQg4njckHHw28fUkhn15sfDHgF4It0FZPc0SjZWxaZ6CjD8fdnrnulDlNDBfy8ImwStHjgJbkYW0CgcuMfan6PIwdgIk%2FqKkAxt6OVhuRQRKdQFTYYd2ifDieEbgv4ca1Qf%2F9uRFcG%2FTCt8CZaBmyOnfXOLajiJrH5NKZdp%2B6VFnaeUa1eiEQdNnNvfW%2FaG2I0y%2BTmL173AsKst4ZYEiC4SMcM1g9bdOdjkRHCczg%2BQoaxkwl72EvQY6pgFxCrMeMEH7ZCZbqPzY1Z%2F023nc%2F1Dci0g5ECVREcrKE9QOFGCFACm3WD8T%2Facw1qbeIPdOMl10SMGuSCeav5O%2BUHkyai%2BUVjI4D2rcgRWqMYWMrFy4WowAzF0Cx6%2Fb4VVZq%2F%2FcLG%2F5E24DUBFN%2Be7xrkC5ssMVQ09cRkRH2yZGaTJ6rksw9w0ubvpM83DI4mFIhJtQgFF2%2B4VRdLqojsuKkWR3eylD&X-Amz-Signature=3db3e986d38b19ec496a8a4dc5f283c1e7715b4c5055d20ef2a70f49879f6a96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUNGUAL2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEoNDdVAGKp%2B25LSZwx%2B5kNKrdgzx5Ty3gLz4a7rQ0LsAiAO2BcfooWhP95u%2BSEHoMNKbmVlj4yYqCWGBssKgV3RyCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMi43wByRtjPpnqU89KtwDvZdgy5pbz4OHO4rRUQ55fOcJIQKFdJs5xhMmY6%2F9uN8vm59xrcYqeavZMUrKFoGVfVoDwc7bezDOdUr1NA%2B8XkZz29QAD1W5R7xbYg2%2B2pHW6yqtZVhKz3NXCs2oy8M%2F0JGcCL2Fa9QNBveXMXcDpC78BaEkFZcl%2BrfCzAdR%2FzZY%2BJlfzqKhFkKXO1WCkbA0cwKpQzxxnO6D5Da%2BtqWGK%2FeGMbZVBSc%2B9Zw0PSR2SBgyFzR9XVK3fWpmpiCyDlI0Wj%2BQ3LNMiUBqdV%2BZ0vE%2BXkmaMK2F%2BQb3jQJmZ6hateCet705VlvozO777jN4Z6q%2BdC%2BQb%2BKSVOa%2F6UpwtQr3Dpwq48iecuVXFe9bkE101RezC%2F8hP%2BQeZDczuPh5TNYvM7EWPp6goGI%2FMQg4njckHHw28fUkhn15sfDHgF4It0FZPc0SjZWxaZ6CjD8fdnrnulDlNDBfy8ImwStHjgJbkYW0CgcuMfan6PIwdgIk%2FqKkAxt6OVhuRQRKdQFTYYd2ifDieEbgv4ca1Qf%2F9uRFcG%2FTCt8CZaBmyOnfXOLajiJrH5NKZdp%2B6VFnaeUa1eiEQdNnNvfW%2FaG2I0y%2BTmL173AsKst4ZYEiC4SMcM1g9bdOdjkRHCczg%2BQoaxkwl72EvQY6pgFxCrMeMEH7ZCZbqPzY1Z%2F023nc%2F1Dci0g5ECVREcrKE9QOFGCFACm3WD8T%2Facw1qbeIPdOMl10SMGuSCeav5O%2BUHkyai%2BUVjI4D2rcgRWqMYWMrFy4WowAzF0Cx6%2Fb4VVZq%2F%2FcLG%2F5E24DUBFN%2Be7xrkC5ssMVQ09cRkRH2yZGaTJ6rksw9w0ubvpM83DI4mFIhJtQgFF2%2B4VRdLqojsuKkWR3eylD&X-Amz-Signature=1148b26c29deb1df929ff56aaa6d5e8329098282c5051448fea74fc532d19bcf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSOYGL2U%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCID7JsxnmQ6hS21WswcqVgo6tsl2J5dvfnGHme0Nu1jxeAiACf3WZmtAh%2Bq2G%2B4WC4%2BVdESZOzmsm8YfzxrTNjJdndir%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIM%2FpELNmpKJdtjgsDVKtwDgQTCofEqs%2FKSXF61%2F2yi7kCDY94s4ZaNlhtN0lTg2fjESwJtO4LFrxqCmis2KrLvQBJwwwdkvKu9EEJ6%2Ff%2F6pWvbCrPKzUO1PsPj%2BCVnZFW0IHSVeskgFid5fFLWFcUeJbVBKYcCL%2BlXGZ6hC6N56On8w4AAxAoPh0vHZBOlk6z%2BoOBVnug3YcTy11ICHopUufRRr%2B2Cy9h%2BjrdaKYJPBTdtn1v0CeorFzVDqTlgWzPdmW6MSPR0GG%2B0iBjVV5W6ORG3g1xP9QpYYgX2ulQC8CwKPl52JtWyY%2FQsFlq35VKj%2BEs3JnfLV8UEkd8pCGsUMf1D7N4EL5jlo%2F%2BHjKYiAfPrTBYfNf9ylOcX7HfXAluoUx3CZKKQIboUF1L7h0rBb1f%2Bm34av8W9boc6cfA95Iht5Gh7QTZs0FTG%2FbjSyAmCDf9Ohc0Qw8ncNCbcydyA9wzdstm3587Nen0v0W%2BXHwV9o8mitqFRWb3zhmxco54TrR3LjurnhFh11TcztusUOJuswFnQnFXRJxHQ9hY8DmUqlM6vHdOGfweJLDNb0hLxk0XRZswWGzfcF%2FnIpEUcKnaKpuUnkTt1cK3WXjoNjy3DJuYPzqCzi%2FFkw%2BOMfSRE%2F3Hfagx4FqXBHzgw%2FbyEvQY6pgF70ZYXlV5snf9oT0qF8E3Sf%2BlsIVJGh9YaQKQqCSL0r2P1ELiSwyYE90LG3fzgdyz7c5H08v2DQfgTgZKaaAwipGENLLzZaifpjJd2B7TfBB8xnieLHUANdrqzU6TCVWD2tBL0TTM4l9tNg558v8NGBk6t3T7EIajFw4bntCPUUVaDIlPk9%2F6HGx1UFKn1%2FhqDa2jmWkBrK7mqshIltbJ1lvurHGjh&X-Amz-Signature=dc6bba1b05c47ef5da3ca007ad4dc6c38fa02327827c5d62fc1d4f740a7597c6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMAFEC5K%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIH69VVgaacCXcI4UAppzPRShNH7KwVfsOCbmMJHFWXFfAiEAk7zVnKnvt5gdBmsvzNaKI5P2GzsGXiaxsDRZCISgzLgq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDJLcIGLCC2ukzpj8QSrcA9SOyU0wglkmq3oGJurFOsokOT8T6wH4EWEL3m3gZq8TRlUfCzPwgIA5nyRnVRosqhlTdruB0zW55YSGFTfGzp2llMOeWW9hyZs%2BdzkQlf8wveqKvfU6Ba8XXJk9F8iItHfxLcuuohXLYXkcWzN7faBE80AUSf3MTkEMa3igEnzJjpmtKEQSxEHSZiFGmJqemsIq%2BqJrWaZMfbvSxmnQRLsI%2B6hROSjLS712PVi5j5PVMk%2BKy5gBBMAYAE4NrKOuG7%2Ft%2BBybf3eqHtanWvbzThyoOF1%2BzQt0Y7XJHYWQs71IvCuUqkoPyAvfeNyArtXEcnDMHCWDmA9GT14S%2B6PFtne81Gg9Ztt2hwyPxW4KxaeJMgaNj57mSpiYVqBRY%2Fr0SrAK83jROJ84B7ePe65biSHVipuDgCVsXLYShzc02xAghbTW8LAvR5743DkJbft6vj29KdVOpMnPVucjBRnh6pmuHUx94pCDorpbthakhdqTs0JAiIaVkmkTKF7o%2BiA5exUBEAwXERX24CNuU3XdpcT8p2TdHDTmxDml%2Bp35ix8CsMZqHxPd6GJNVxzJcSLdxJFQRDCjq0Aap3R3cysvzT28rEC3jbpoj5TzyKg7km4llCPeUsd%2Be%2Bs4IZy1MJC9hL0GOqUB1Zf3QZArrbTjXzezxiel963HRIGj1Bm4uLe%2BnDy5uGZXLzWBQeZtNbb%2B3PgxRoidStWkLWbKFT7fGuSxu9FUuom4GxT3CvosOrw3G7Jcu0BK%2BjxdlZvGmU9WfZy7F2gzZ0m2was5lYd49M%2Fr%2BEoxAssQV17f%2BMpqCLHxKp0xibUAHPKJ4%2F54a6rvcmqIXqqs5bs88RhRLv5%2FGPuvBCyrOtjau6G%2B&X-Amz-Signature=3beac66a47aec65bd6c54556bac2c1e07db9ccd10c70df8182a7a6736ebc6e1e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3V4BKJU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDzyCDifFQKC6juO1d5qlEZ9yxN0lUz7OGwjhixSYC%2BVAIhAKqW3PxxEO9w2iz2XKEwxe5rzj%2BbbzSeTzcanasyV6DYKv8DCB0QABoMNjM3NDIzMTgzODA1Igz7xc1pxhN9e5sbGPUq3AM3WtRkbsngTiKzD5XM%2FLdhbSvQQRUDLcLosgJoACzZGDlnzw2m3nbHxsta3PJoW2uz38goWQ%2F2AUnCcUexwKWujhqfm969YE%2BESCTRDIixNP0FqR0XN8WjMG4GFInW7KO6j1vNDC%2FBDb5sjr1s9oLVI4Hs%2BPhsalL%2BsiJZ5KHGeJFdZlmf%2Bj1r8GC7vJRRlxR3fQI9xu4qVjGjUTujGoenj7gVZEpmy8RvRk9JNETup9ItOygFTeL8bTkC2mlTD6uyDbnBfhXoN8vnJqIf50F%2FbEQTAx9iWNntB4a4G3rwc3U1FVLoqeU4igrWzugM21713rEfnz%2FgpGGQEEOS9Tm6s6zsGWUjfzfRUtCmmgMaDgoWm%2Ba%2FSaNnFKfKE0c%2BCOJOW%2Br4UCE0YAufqH59jkP1XeHzVnocYZ0QLWZwjwy1oMxBiFueDrtnYP1mv0CW7eH9K%2BVEkj%2BvgGam8FHWc7Gr2UiTJ7556wjPBHaKuTSfD0nJSH274QgTT6K00Ny3Wc%2F96XaA6QQ%2F0t4xWow8e2%2B1ARBOBqCbKAEB4b9AjxHtf3atgtIPKP9hTHa7XGGAszRWc4uKek1oLk28osFAh7l9GlMLthJftV95RmyrywCay5nQom%2FC2qe7QrBPRzDSvIS9BjqkAWhneC4Nk6Ddo9e1A%2BuTa31ZrbmC3Liee1VkbpZJ3E4j96RbGKU4qewKrhpzfwvchcraH31cB3K0srUPto2bYLoozf8IoKx9qQmZIaPwecmsoqZcl%2B9M%2FHLI9WJxRjNU%2Fcbjgu8VBVXsL0%2F51SIW%2FjJZu5AyXkTw71onX5g%2FVAhYhK1ZT2p39am%2BRY4ww%2Fj3MHJdMtttUWpv8TUGly0MhRKYQWps&X-Amz-Signature=05c49cec4b434525669d9cf4369161648c7bfd575a8c3049f94acb6c5e28966a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O6UFBJS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDw3IlaHkppJ8FzsA9TXLRHkje0zx0u9lwpAMgaM0LO0AIgMRKs7TMc3%2BSRBKyt3S5kgrOWAN9%2Bn0sdEWfHqzer8KIq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDClCPplVG2n85oPGzCrcA3i2PO6pYyJw7nuPgatRTiFNvBzI9nfN5A%2FsOhTSAI%2BdV7ZWtQFkYBB2Qr2DIwlw9fAxp3A%2BhYWau3A3kT5Oq6O4daZ%2FvV9Q9QNpklTvsiRq8%2FK3RIaQeyJm0i5yEvZoxcsaWlVbcPOHYctMagUOOlTJ1c54Ce25Z4wyNjpun9JyBewteh0n1ND0hAXZ0GE2D71xAM1h%2BL9QLc21bEEIB4f%2BSseWbwDTEqx4JTuh548qUZfH4KQ96ymD58nPDAWu2YCz917ugkD3wllXdE4LydLWJqMTHkJt%2FTRpE2Da9yw7pccUQVbuUV%2B2MUqK49Nl6iZjfAL59nYe3mJDSHZz3rfyEoy7MQL8CEGbX79MI67QuU1aZNqzJ8u4sqZLWgVnXcYwBXd3FT6hqNOGkEQNnPhoqhVP5EsuqZ0yTt%2BWreZPXE8%2BzY3WUrHdLtuUuR5IQlKR10q3wyjNgUruNDxem5T3WfPn3RIWUSYkRHWpfRgymBdr26gp0Xkj0wge67TH4CJ3kimCcpFRvTcMeyiWoxh%2FUaCJ0sgtc%2FdJqmuZ6kI5cDz1UoWZuVklb5y7Be0Gw5rI6xZ0bKLknlv09wTWvh5xk3h7GGLXhwdiK8Z1Qsy4OczpP3kbYXWl7Fn9MOu9hL0GOqUBZKoWxxy4pxm9EnphEAPogYYyhNwFqQuVhPxk1cpkvVmpu9ORsSZMsVBdvBdPD8lBGtFeAI%2FRPaNJTbllA8lvuk%2B%2Fkt2jauacNtMinXZD%2Fg10Azberwi2KPrhe6oCLtF5JKjb3%2BOMbedU2Jr6ZS54oavuStWIPW6YU4tZ47k8mx37a5Opt0zZ%2FAAKv57mjdfpP2C%2Fxu1otAv6bfzeP%2FURJvTn6X65&X-Amz-Signature=6cce0585a170ac0f8e5480ef12702e603fa4472b244732a5b85a09634ca73080&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O6UFBJS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDw3IlaHkppJ8FzsA9TXLRHkje0zx0u9lwpAMgaM0LO0AIgMRKs7TMc3%2BSRBKyt3S5kgrOWAN9%2Bn0sdEWfHqzer8KIq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDClCPplVG2n85oPGzCrcA3i2PO6pYyJw7nuPgatRTiFNvBzI9nfN5A%2FsOhTSAI%2BdV7ZWtQFkYBB2Qr2DIwlw9fAxp3A%2BhYWau3A3kT5Oq6O4daZ%2FvV9Q9QNpklTvsiRq8%2FK3RIaQeyJm0i5yEvZoxcsaWlVbcPOHYctMagUOOlTJ1c54Ce25Z4wyNjpun9JyBewteh0n1ND0hAXZ0GE2D71xAM1h%2BL9QLc21bEEIB4f%2BSseWbwDTEqx4JTuh548qUZfH4KQ96ymD58nPDAWu2YCz917ugkD3wllXdE4LydLWJqMTHkJt%2FTRpE2Da9yw7pccUQVbuUV%2B2MUqK49Nl6iZjfAL59nYe3mJDSHZz3rfyEoy7MQL8CEGbX79MI67QuU1aZNqzJ8u4sqZLWgVnXcYwBXd3FT6hqNOGkEQNnPhoqhVP5EsuqZ0yTt%2BWreZPXE8%2BzY3WUrHdLtuUuR5IQlKR10q3wyjNgUruNDxem5T3WfPn3RIWUSYkRHWpfRgymBdr26gp0Xkj0wge67TH4CJ3kimCcpFRvTcMeyiWoxh%2FUaCJ0sgtc%2FdJqmuZ6kI5cDz1UoWZuVklb5y7Be0Gw5rI6xZ0bKLknlv09wTWvh5xk3h7GGLXhwdiK8Z1Qsy4OczpP3kbYXWl7Fn9MOu9hL0GOqUBZKoWxxy4pxm9EnphEAPogYYyhNwFqQuVhPxk1cpkvVmpu9ORsSZMsVBdvBdPD8lBGtFeAI%2FRPaNJTbllA8lvuk%2B%2Fkt2jauacNtMinXZD%2Fg10Azberwi2KPrhe6oCLtF5JKjb3%2BOMbedU2Jr6ZS54oavuStWIPW6YU4tZ47k8mx37a5Opt0zZ%2FAAKv57mjdfpP2C%2Fxu1otAv6bfzeP%2FURJvTn6X65&X-Amz-Signature=eaf5b2e9becd5e87dca1688059b96fbdeaffb749bc40925f264ffa27746634db&X-Amz-SignedHeaders=host&x-id=GetObject)

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
