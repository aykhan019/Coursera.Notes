

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6VZSSSX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPqOKWi1wP%2FMhakR6HvFtH2JWc7K2F3mFgzn8569FHGQIgQmdKidYU6UdLjM1hq6THL%2BbqDkfDcgWd2q1N3sAWyuYq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDKlQ7APWvItXmdQpXCrcA6%2FdV%2BPh0F70SJLgxG5CFkDE3gzbJZqZg5HvkybvYrFqLFYWswZSCG2hN5P2xV%2FbAJrjUkMprqCwyE4WvxdH%2FiqPwdPm981%2B7CwbC5vRI8T6Fot%2F18gmgle5i57p5hJ4JvNjfBCJHwN8WiHS1ZudwQ0ufjITdfaVfotYKx%2BQNhyh8jYVxaqHvO1JkYDdTPYdUueu9yzL88tLcPQecXYAeBSjgiAeR3sNVNLywk2FWss2SU7PWyVc%2BdxONrm%2FeyzCUdCWjDV1k51sXVpyIvusist5Rzsm6vKQKILE%2FDuBinDIAyBFQuiIySukhzjj0Mf4JSrt6BLFsS0Rrf69mPCN4i8hoBmRFcWm8DiZWvD5C7cJvGegCX8Uk1dZsX%2FN1RK0KHdl6VB3387ot5KNMr5Br741tcYXp40cc3GYBYhAZgIP%2BTfQjsZprTRkpvP9QUVquojWYrF5KyeoD7DelTpE1YtywtSiNGHjJhPadL9Skvrl4Kp%2BMkpV8MuhYpz7vU%2F0KLdIsiw8ydOXJ17iSJrOMADzq7mMZ1%2BxPKlw47yXHR4FHApth77AFTzHNJPE%2F11XKN6rinotMdnUfuRFUjPO1pE4jvirKuVeqKTwcGIKnxD0FHRv6UK8b%2BUhtZjIMO20gr0GOqUBt2zDQF0akGjUAclWeZmA5dpaXu5Aon%2FliCuf5Ug%2BdUQ2OoNeghj1vqXCRkQyTwq2rLr0baCFSm3sA%2BSCPb5MvRirRauFR3JHA6SAWYkmtN8sd1YNayF94NNiZBkxgdihK3OQcWzA3HVtGF8ELeWXHIzvKab7P1IKmyJ1yhkmEnfl6qNTAz%2Bto7Kb3QAk0KgabyKg9CZwahaVm6D%2Bigxwj5ycfhwC&X-Amz-Signature=426a5d8e08a653567f7b3f51a3c1df6bfda90917339ff413128a40b45ff10ef1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6VZSSSX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPqOKWi1wP%2FMhakR6HvFtH2JWc7K2F3mFgzn8569FHGQIgQmdKidYU6UdLjM1hq6THL%2BbqDkfDcgWd2q1N3sAWyuYq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDKlQ7APWvItXmdQpXCrcA6%2FdV%2BPh0F70SJLgxG5CFkDE3gzbJZqZg5HvkybvYrFqLFYWswZSCG2hN5P2xV%2FbAJrjUkMprqCwyE4WvxdH%2FiqPwdPm981%2B7CwbC5vRI8T6Fot%2F18gmgle5i57p5hJ4JvNjfBCJHwN8WiHS1ZudwQ0ufjITdfaVfotYKx%2BQNhyh8jYVxaqHvO1JkYDdTPYdUueu9yzL88tLcPQecXYAeBSjgiAeR3sNVNLywk2FWss2SU7PWyVc%2BdxONrm%2FeyzCUdCWjDV1k51sXVpyIvusist5Rzsm6vKQKILE%2FDuBinDIAyBFQuiIySukhzjj0Mf4JSrt6BLFsS0Rrf69mPCN4i8hoBmRFcWm8DiZWvD5C7cJvGegCX8Uk1dZsX%2FN1RK0KHdl6VB3387ot5KNMr5Br741tcYXp40cc3GYBYhAZgIP%2BTfQjsZprTRkpvP9QUVquojWYrF5KyeoD7DelTpE1YtywtSiNGHjJhPadL9Skvrl4Kp%2BMkpV8MuhYpz7vU%2F0KLdIsiw8ydOXJ17iSJrOMADzq7mMZ1%2BxPKlw47yXHR4FHApth77AFTzHNJPE%2F11XKN6rinotMdnUfuRFUjPO1pE4jvirKuVeqKTwcGIKnxD0FHRv6UK8b%2BUhtZjIMO20gr0GOqUBt2zDQF0akGjUAclWeZmA5dpaXu5Aon%2FliCuf5Ug%2BdUQ2OoNeghj1vqXCRkQyTwq2rLr0baCFSm3sA%2BSCPb5MvRirRauFR3JHA6SAWYkmtN8sd1YNayF94NNiZBkxgdihK3OQcWzA3HVtGF8ELeWXHIzvKab7P1IKmyJ1yhkmEnfl6qNTAz%2Bto7Kb3QAk0KgabyKg9CZwahaVm6D%2Bigxwj5ycfhwC&X-Amz-Signature=fa93433c8042100f9f9505c19f5a5bdff410aab79c50cf20429d3f04536ea446&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6VZSSSX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPqOKWi1wP%2FMhakR6HvFtH2JWc7K2F3mFgzn8569FHGQIgQmdKidYU6UdLjM1hq6THL%2BbqDkfDcgWd2q1N3sAWyuYq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDKlQ7APWvItXmdQpXCrcA6%2FdV%2BPh0F70SJLgxG5CFkDE3gzbJZqZg5HvkybvYrFqLFYWswZSCG2hN5P2xV%2FbAJrjUkMprqCwyE4WvxdH%2FiqPwdPm981%2B7CwbC5vRI8T6Fot%2F18gmgle5i57p5hJ4JvNjfBCJHwN8WiHS1ZudwQ0ufjITdfaVfotYKx%2BQNhyh8jYVxaqHvO1JkYDdTPYdUueu9yzL88tLcPQecXYAeBSjgiAeR3sNVNLywk2FWss2SU7PWyVc%2BdxONrm%2FeyzCUdCWjDV1k51sXVpyIvusist5Rzsm6vKQKILE%2FDuBinDIAyBFQuiIySukhzjj0Mf4JSrt6BLFsS0Rrf69mPCN4i8hoBmRFcWm8DiZWvD5C7cJvGegCX8Uk1dZsX%2FN1RK0KHdl6VB3387ot5KNMr5Br741tcYXp40cc3GYBYhAZgIP%2BTfQjsZprTRkpvP9QUVquojWYrF5KyeoD7DelTpE1YtywtSiNGHjJhPadL9Skvrl4Kp%2BMkpV8MuhYpz7vU%2F0KLdIsiw8ydOXJ17iSJrOMADzq7mMZ1%2BxPKlw47yXHR4FHApth77AFTzHNJPE%2F11XKN6rinotMdnUfuRFUjPO1pE4jvirKuVeqKTwcGIKnxD0FHRv6UK8b%2BUhtZjIMO20gr0GOqUBt2zDQF0akGjUAclWeZmA5dpaXu5Aon%2FliCuf5Ug%2BdUQ2OoNeghj1vqXCRkQyTwq2rLr0baCFSm3sA%2BSCPb5MvRirRauFR3JHA6SAWYkmtN8sd1YNayF94NNiZBkxgdihK3OQcWzA3HVtGF8ELeWXHIzvKab7P1IKmyJ1yhkmEnfl6qNTAz%2Bto7Kb3QAk0KgabyKg9CZwahaVm6D%2Bigxwj5ycfhwC&X-Amz-Signature=9abb997f8f5085d574a243472c725e771e5092cc464f593d4a34bad11ce7f87d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665226ZWEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8zEgsIBpZRdfZoh1mtnGv7mKM3wPmyQtYkG7U1MRNGAiEAv%2FtwqzhDtBR3vgHYQndnsFZWkfRlVXQDq2vHbNXM9XUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG7sqwJCTMjst4qoVircA2cFp2qrNGIcS3hIq2zuXP0YQy7g411pmorhDcJq2eg2CUpjk7gfITQHSBrxoz27qR%2FndCdihsXsNnLe44DwreSWSzLlfCcJwgAQS%2FmOI03EybOjaNtZC6o2rUIuUnx8LbBGTU9bzC7%2FhUH74%2Ft1ZoGWVWhliXRRv%2FKEx5WIwPWWzjEz%2B425hMCEhf01A2wi%2FLRfGenA5Quj6tGZ04CS3cfIGVnp0i6878AIIKNsjAZt%2FDjMItpgbe3ANFlOCuPU%2FgBn0Z5eu9wlzSl5nQEAPUR35M2WeiY3uLOMFBHo9ldaLh%2FOXr%2BvDPjY2B5Lq2kxjmmxMV3rqqrdvV9SShqHbdsZaiPvZYPN05os2CWKuWRNoRmEKxv8qvH0bhUwKV1VyLD0TKwjLU9JRu8xCC%2BevGjN07FdnrVNoyWiEqG%2BKL4VnEMaRKOxtdtvK2npvR8nH0cIn73hmZv4R9O18vYjyBi9l9RvuFrSaBcBSbYGewMl8gdSmTTsW4N7tYTT%2FqcA%2BbaXrNcdRCfGinmjP9fBcAEJyyjqU2AfAzMp0LGuXQ2UoNKy7nJkLJ5pjQ9bj5swce4ixAqiE7e6uQjLqAyNOv1hUA417AwftW9jW5ePl6UknseCp53ScT3uFAiOMLO1gr0GOqUBRjFdAHut2%2FqqL1ST%2B0ir4mYq3geAt13Ydc1GuUrUcv%2BE8ycOAOm%2FtVSC6m3fG1%2BmP1KUHnQ4ld1W3IqJnc8YoN5UGBGoBu0bLwdxc%2BRY2Drfl%2BLCLzbBaKpepmC5XDsPh6mt0%2FnjW1AXrF%2Flz3c3Hlhg2lneydRayh7GJpkN6qjpE1wTb5Dt2RmITm4agnWDLMqaJDQmRjSUm429d4JT4Wc%2Fj6qf&X-Amz-Signature=69850ebca430dccd7df5b13547f126b2c62c9d390770f4c54093a644df7ae671&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665226ZWEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8zEgsIBpZRdfZoh1mtnGv7mKM3wPmyQtYkG7U1MRNGAiEAv%2FtwqzhDtBR3vgHYQndnsFZWkfRlVXQDq2vHbNXM9XUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG7sqwJCTMjst4qoVircA2cFp2qrNGIcS3hIq2zuXP0YQy7g411pmorhDcJq2eg2CUpjk7gfITQHSBrxoz27qR%2FndCdihsXsNnLe44DwreSWSzLlfCcJwgAQS%2FmOI03EybOjaNtZC6o2rUIuUnx8LbBGTU9bzC7%2FhUH74%2Ft1ZoGWVWhliXRRv%2FKEx5WIwPWWzjEz%2B425hMCEhf01A2wi%2FLRfGenA5Quj6tGZ04CS3cfIGVnp0i6878AIIKNsjAZt%2FDjMItpgbe3ANFlOCuPU%2FgBn0Z5eu9wlzSl5nQEAPUR35M2WeiY3uLOMFBHo9ldaLh%2FOXr%2BvDPjY2B5Lq2kxjmmxMV3rqqrdvV9SShqHbdsZaiPvZYPN05os2CWKuWRNoRmEKxv8qvH0bhUwKV1VyLD0TKwjLU9JRu8xCC%2BevGjN07FdnrVNoyWiEqG%2BKL4VnEMaRKOxtdtvK2npvR8nH0cIn73hmZv4R9O18vYjyBi9l9RvuFrSaBcBSbYGewMl8gdSmTTsW4N7tYTT%2FqcA%2BbaXrNcdRCfGinmjP9fBcAEJyyjqU2AfAzMp0LGuXQ2UoNKy7nJkLJ5pjQ9bj5swce4ixAqiE7e6uQjLqAyNOv1hUA417AwftW9jW5ePl6UknseCp53ScT3uFAiOMLO1gr0GOqUBRjFdAHut2%2FqqL1ST%2B0ir4mYq3geAt13Ydc1GuUrUcv%2BE8ycOAOm%2FtVSC6m3fG1%2BmP1KUHnQ4ld1W3IqJnc8YoN5UGBGoBu0bLwdxc%2BRY2Drfl%2BLCLzbBaKpepmC5XDsPh6mt0%2FnjW1AXrF%2Flz3c3Hlhg2lneydRayh7GJpkN6qjpE1wTb5Dt2RmITm4agnWDLMqaJDQmRjSUm429d4JT4Wc%2Fj6qf&X-Amz-Signature=d9de0da15a8b21241cbe31ae8b95e5d0e861da52ca6a62baca2178e5ab265f16&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665226ZWEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8zEgsIBpZRdfZoh1mtnGv7mKM3wPmyQtYkG7U1MRNGAiEAv%2FtwqzhDtBR3vgHYQndnsFZWkfRlVXQDq2vHbNXM9XUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG7sqwJCTMjst4qoVircA2cFp2qrNGIcS3hIq2zuXP0YQy7g411pmorhDcJq2eg2CUpjk7gfITQHSBrxoz27qR%2FndCdihsXsNnLe44DwreSWSzLlfCcJwgAQS%2FmOI03EybOjaNtZC6o2rUIuUnx8LbBGTU9bzC7%2FhUH74%2Ft1ZoGWVWhliXRRv%2FKEx5WIwPWWzjEz%2B425hMCEhf01A2wi%2FLRfGenA5Quj6tGZ04CS3cfIGVnp0i6878AIIKNsjAZt%2FDjMItpgbe3ANFlOCuPU%2FgBn0Z5eu9wlzSl5nQEAPUR35M2WeiY3uLOMFBHo9ldaLh%2FOXr%2BvDPjY2B5Lq2kxjmmxMV3rqqrdvV9SShqHbdsZaiPvZYPN05os2CWKuWRNoRmEKxv8qvH0bhUwKV1VyLD0TKwjLU9JRu8xCC%2BevGjN07FdnrVNoyWiEqG%2BKL4VnEMaRKOxtdtvK2npvR8nH0cIn73hmZv4R9O18vYjyBi9l9RvuFrSaBcBSbYGewMl8gdSmTTsW4N7tYTT%2FqcA%2BbaXrNcdRCfGinmjP9fBcAEJyyjqU2AfAzMp0LGuXQ2UoNKy7nJkLJ5pjQ9bj5swce4ixAqiE7e6uQjLqAyNOv1hUA417AwftW9jW5ePl6UknseCp53ScT3uFAiOMLO1gr0GOqUBRjFdAHut2%2FqqL1ST%2B0ir4mYq3geAt13Ydc1GuUrUcv%2BE8ycOAOm%2FtVSC6m3fG1%2BmP1KUHnQ4ld1W3IqJnc8YoN5UGBGoBu0bLwdxc%2BRY2Drfl%2BLCLzbBaKpepmC5XDsPh6mt0%2FnjW1AXrF%2Flz3c3Hlhg2lneydRayh7GJpkN6qjpE1wTb5Dt2RmITm4agnWDLMqaJDQmRjSUm429d4JT4Wc%2Fj6qf&X-Amz-Signature=1507e2386b2bee9c4c7d5363be99c2298362c057850cf4a724bfbe16f0273a27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665226ZWEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8zEgsIBpZRdfZoh1mtnGv7mKM3wPmyQtYkG7U1MRNGAiEAv%2FtwqzhDtBR3vgHYQndnsFZWkfRlVXQDq2vHbNXM9XUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG7sqwJCTMjst4qoVircA2cFp2qrNGIcS3hIq2zuXP0YQy7g411pmorhDcJq2eg2CUpjk7gfITQHSBrxoz27qR%2FndCdihsXsNnLe44DwreSWSzLlfCcJwgAQS%2FmOI03EybOjaNtZC6o2rUIuUnx8LbBGTU9bzC7%2FhUH74%2Ft1ZoGWVWhliXRRv%2FKEx5WIwPWWzjEz%2B425hMCEhf01A2wi%2FLRfGenA5Quj6tGZ04CS3cfIGVnp0i6878AIIKNsjAZt%2FDjMItpgbe3ANFlOCuPU%2FgBn0Z5eu9wlzSl5nQEAPUR35M2WeiY3uLOMFBHo9ldaLh%2FOXr%2BvDPjY2B5Lq2kxjmmxMV3rqqrdvV9SShqHbdsZaiPvZYPN05os2CWKuWRNoRmEKxv8qvH0bhUwKV1VyLD0TKwjLU9JRu8xCC%2BevGjN07FdnrVNoyWiEqG%2BKL4VnEMaRKOxtdtvK2npvR8nH0cIn73hmZv4R9O18vYjyBi9l9RvuFrSaBcBSbYGewMl8gdSmTTsW4N7tYTT%2FqcA%2BbaXrNcdRCfGinmjP9fBcAEJyyjqU2AfAzMp0LGuXQ2UoNKy7nJkLJ5pjQ9bj5swce4ixAqiE7e6uQjLqAyNOv1hUA417AwftW9jW5ePl6UknseCp53ScT3uFAiOMLO1gr0GOqUBRjFdAHut2%2FqqL1ST%2B0ir4mYq3geAt13Ydc1GuUrUcv%2BE8ycOAOm%2FtVSC6m3fG1%2BmP1KUHnQ4ld1W3IqJnc8YoN5UGBGoBu0bLwdxc%2BRY2Drfl%2BLCLzbBaKpepmC5XDsPh6mt0%2FnjW1AXrF%2Flz3c3Hlhg2lneydRayh7GJpkN6qjpE1wTb5Dt2RmITm4agnWDLMqaJDQmRjSUm429d4JT4Wc%2Fj6qf&X-Amz-Signature=cfd984e65890d4a773df1d56cc397f7295536dc4f6651f650245507b6fb98683&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665226ZWEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8zEgsIBpZRdfZoh1mtnGv7mKM3wPmyQtYkG7U1MRNGAiEAv%2FtwqzhDtBR3vgHYQndnsFZWkfRlVXQDq2vHbNXM9XUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG7sqwJCTMjst4qoVircA2cFp2qrNGIcS3hIq2zuXP0YQy7g411pmorhDcJq2eg2CUpjk7gfITQHSBrxoz27qR%2FndCdihsXsNnLe44DwreSWSzLlfCcJwgAQS%2FmOI03EybOjaNtZC6o2rUIuUnx8LbBGTU9bzC7%2FhUH74%2Ft1ZoGWVWhliXRRv%2FKEx5WIwPWWzjEz%2B425hMCEhf01A2wi%2FLRfGenA5Quj6tGZ04CS3cfIGVnp0i6878AIIKNsjAZt%2FDjMItpgbe3ANFlOCuPU%2FgBn0Z5eu9wlzSl5nQEAPUR35M2WeiY3uLOMFBHo9ldaLh%2FOXr%2BvDPjY2B5Lq2kxjmmxMV3rqqrdvV9SShqHbdsZaiPvZYPN05os2CWKuWRNoRmEKxv8qvH0bhUwKV1VyLD0TKwjLU9JRu8xCC%2BevGjN07FdnrVNoyWiEqG%2BKL4VnEMaRKOxtdtvK2npvR8nH0cIn73hmZv4R9O18vYjyBi9l9RvuFrSaBcBSbYGewMl8gdSmTTsW4N7tYTT%2FqcA%2BbaXrNcdRCfGinmjP9fBcAEJyyjqU2AfAzMp0LGuXQ2UoNKy7nJkLJ5pjQ9bj5swce4ixAqiE7e6uQjLqAyNOv1hUA417AwftW9jW5ePl6UknseCp53ScT3uFAiOMLO1gr0GOqUBRjFdAHut2%2FqqL1ST%2B0ir4mYq3geAt13Ydc1GuUrUcv%2BE8ycOAOm%2FtVSC6m3fG1%2BmP1KUHnQ4ld1W3IqJnc8YoN5UGBGoBu0bLwdxc%2BRY2Drfl%2BLCLzbBaKpepmC5XDsPh6mt0%2FnjW1AXrF%2Flz3c3Hlhg2lneydRayh7GJpkN6qjpE1wTb5Dt2RmITm4agnWDLMqaJDQmRjSUm429d4JT4Wc%2Fj6qf&X-Amz-Signature=ffd71e395d9d4931998c880c7000620fde8d71d915c2079a3822fe78e002f266&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665226ZWEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8zEgsIBpZRdfZoh1mtnGv7mKM3wPmyQtYkG7U1MRNGAiEAv%2FtwqzhDtBR3vgHYQndnsFZWkfRlVXQDq2vHbNXM9XUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG7sqwJCTMjst4qoVircA2cFp2qrNGIcS3hIq2zuXP0YQy7g411pmorhDcJq2eg2CUpjk7gfITQHSBrxoz27qR%2FndCdihsXsNnLe44DwreSWSzLlfCcJwgAQS%2FmOI03EybOjaNtZC6o2rUIuUnx8LbBGTU9bzC7%2FhUH74%2Ft1ZoGWVWhliXRRv%2FKEx5WIwPWWzjEz%2B425hMCEhf01A2wi%2FLRfGenA5Quj6tGZ04CS3cfIGVnp0i6878AIIKNsjAZt%2FDjMItpgbe3ANFlOCuPU%2FgBn0Z5eu9wlzSl5nQEAPUR35M2WeiY3uLOMFBHo9ldaLh%2FOXr%2BvDPjY2B5Lq2kxjmmxMV3rqqrdvV9SShqHbdsZaiPvZYPN05os2CWKuWRNoRmEKxv8qvH0bhUwKV1VyLD0TKwjLU9JRu8xCC%2BevGjN07FdnrVNoyWiEqG%2BKL4VnEMaRKOxtdtvK2npvR8nH0cIn73hmZv4R9O18vYjyBi9l9RvuFrSaBcBSbYGewMl8gdSmTTsW4N7tYTT%2FqcA%2BbaXrNcdRCfGinmjP9fBcAEJyyjqU2AfAzMp0LGuXQ2UoNKy7nJkLJ5pjQ9bj5swce4ixAqiE7e6uQjLqAyNOv1hUA417AwftW9jW5ePl6UknseCp53ScT3uFAiOMLO1gr0GOqUBRjFdAHut2%2FqqL1ST%2B0ir4mYq3geAt13Ydc1GuUrUcv%2BE8ycOAOm%2FtVSC6m3fG1%2BmP1KUHnQ4ld1W3IqJnc8YoN5UGBGoBu0bLwdxc%2BRY2Drfl%2BLCLzbBaKpepmC5XDsPh6mt0%2FnjW1AXrF%2Flz3c3Hlhg2lneydRayh7GJpkN6qjpE1wTb5Dt2RmITm4agnWDLMqaJDQmRjSUm429d4JT4Wc%2Fj6qf&X-Amz-Signature=d20d4bb496d0fe1027969dfdaa6b0f31a4e52c9511bf7bfe681dd970cf73933e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OZZQBUS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDaO%2FzApWJQVPsDqzlnRrgMIkRJKZITY2%2FfDz5w7ClhyAiAHDDxodPN9pmjmL3TI9NiGG4ClFwmOuTCUoehUd%2B6VyCr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FezA889Myf0gffAKtwD2cKCCs%2BJUC8QlBJa8bd3Qi7%2Bsw%2BlvBaU8k77kBh6rWOaQPzDg6tvDQcEHqkXyPegIGo8DFAP5Pak5Qb2nP3EGvh61ZnbS8LTJjhVDqu4eFn%2Bozy49nvrMk4O0cJ0Bd6rIpOloOv8pLSF0%2BXmR2G%2BSJtY%2BFwaZniqJO3aQoJ4MJcoyoi2nSQ0qXa4gUktH15ClOhX5Sa537rx3iJPWJFAe6U%2FiSFRmmBjgUW0SSOj5Rr966aLrsfbSJTw%2BAnC7RBBu3PtEFKeZMo5AVw7d6yU4o9%2Bb7%2FpZniG5h0Xt9nJm3NUxGMiOpCpS7vkW%2BRwtXNkjNmX8pzdVo%2BgT4gkLcxiz7TSvQFPl2Br6eOukRpTILj2skj4%2BSvkPx9IYgClsEBKWbCcO6bLqp7Id21SaE6Puk31WIp8dJimjwnx41NhFf9eWCTRb3wepE%2BfJf3y%2BYL%2B86V7Vmt60TKQHlbMo7JFEXB1WqCZOOmDcASxR8fvQvpsEQRbTxRgxe8PlXuvyv4SZpI8YbW6KDn4XencbFlxivo6b1Kw7VulCkFUbpbq8%2FYlpvpQ4LIv82kP9W%2BmwjXdjD%2BFuAHunzPrSqHKAEl2INAsxLK6vR5fkZ1J4KY2v%2BHvPyzPy0xiUz3Ifv8ww7SCvQY6pgFGKUCVJQfUvqcgjy%2B4W1UylJKuT8giu03Mz2euAgpYane72qSEPGRD%2Fn%2B3sfM82iQZVBVtAMpPGUc8Tixo6iVxagZFjoLLbZ7E%2FV%2BiccpyKCDDU7C6fsct2yCLjWdmzlJbKWGv4tX6ChiN0x0SBeqwy0z7Ys7FyVTjRImeCs282s%2BK%2BZBztXQxTNcVqFB5p2KF%2FCIq%2FLsBw2LjhtJX7jhClRLrddlr&X-Amz-Signature=fbbc51bf1b3fd02f04a9d24117affd6d6dcb97a46da72f6fd841cb9a06bb7e05&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZZBNUQ6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEbgEtIELciLWfr4HHSp978UB38PaKZSyGusii%2BdTf3aAiEAoTOYVikZbhXZwvwutBNy13w0qgyVGn4m2dAdIkeEtOoq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDCdsNiplksuH0jyewCrcAwHSxdYG7Cla67%2BbFD2IL1pKa2tkB0CAUn3Psa50XhdVN59qRmrjobW1K2yCuW0kY070VfN8Gzqbaj3N4Tn%2FrpjvagcwQFsa19fi%2FwmIkNmED3drlalr5x%2Bq%2FYsQSaRFfz3PPO7dNIxSJScXwZ8nJVfBD9BlZugsNnVFkov3IzJn%2Byu2dbfeZ1rm6YcmSvYpTnIWpGhDgRRhiqTf%2BY%2FiBWepEp83GceldVO3wngupgDXwSd7oyTzYCJaYTPu2x6hTvBBfWvYdT%2FFkKxE0ZcguK%2BqtJ0hPqMUN7yH6A1uN677drylx1YGljPLr7ksHfACgDBzd293Kp6S8EAIZrGMqU9Izqzsgirv%2BMeloVwvPbsYUD77UsxezV11j5ikZDVrNxXxmAyhFofI7GDjMC%2FOG5%2BeN%2BRamHSKn%2BFI5DOLDsX28cPAxZEhRypZDTeELU8hDwUeEj25MHdDmhl58wKWM1tPjO4AWqOlN9Xoui17T6mJgH%2BnlH2zpPtoJFT04EXSeWtGjaZq4S3AK%2BV0DzuHWt3NMMCXVzD9ic1XdGflOHvQWt6hNuebfGtW%2F9ZpBQWm3DN1mDwx3dIdL0MvMAmsoqeaiW3o3zK9j%2B3iq%2BbFTePbTWI7FhXrK%2FQ3EN6tMMi0gr0GOqUBB1q%2F2FVy9Fb5Ncm2bu%2FVCqC07clz8gD%2FBYY4mNv1%2FhCRZpYrkIBoRbuaer4nuir3p318HHj8kSmKl44XTy%2Ff3YlQO2eV7fwMIGGtP819ww300Tizobx%2FQeUSR6cz0o7ar2at8PoBZDV%2BCk3dggly8DhydSBXG3t6hd0qbhYEBiBsUguvMPPLEuqTbAyKIBhIXIFB1DvavBQwDSvgy671qffAYb7J&X-Amz-Signature=20163e18aacd2f10428388fe4aa3ad4e0c5569094bfc6e565898658060dba830&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665226ZWEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8zEgsIBpZRdfZoh1mtnGv7mKM3wPmyQtYkG7U1MRNGAiEAv%2FtwqzhDtBR3vgHYQndnsFZWkfRlVXQDq2vHbNXM9XUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG7sqwJCTMjst4qoVircA2cFp2qrNGIcS3hIq2zuXP0YQy7g411pmorhDcJq2eg2CUpjk7gfITQHSBrxoz27qR%2FndCdihsXsNnLe44DwreSWSzLlfCcJwgAQS%2FmOI03EybOjaNtZC6o2rUIuUnx8LbBGTU9bzC7%2FhUH74%2Ft1ZoGWVWhliXRRv%2FKEx5WIwPWWzjEz%2B425hMCEhf01A2wi%2FLRfGenA5Quj6tGZ04CS3cfIGVnp0i6878AIIKNsjAZt%2FDjMItpgbe3ANFlOCuPU%2FgBn0Z5eu9wlzSl5nQEAPUR35M2WeiY3uLOMFBHo9ldaLh%2FOXr%2BvDPjY2B5Lq2kxjmmxMV3rqqrdvV9SShqHbdsZaiPvZYPN05os2CWKuWRNoRmEKxv8qvH0bhUwKV1VyLD0TKwjLU9JRu8xCC%2BevGjN07FdnrVNoyWiEqG%2BKL4VnEMaRKOxtdtvK2npvR8nH0cIn73hmZv4R9O18vYjyBi9l9RvuFrSaBcBSbYGewMl8gdSmTTsW4N7tYTT%2FqcA%2BbaXrNcdRCfGinmjP9fBcAEJyyjqU2AfAzMp0LGuXQ2UoNKy7nJkLJ5pjQ9bj5swce4ixAqiE7e6uQjLqAyNOv1hUA417AwftW9jW5ePl6UknseCp53ScT3uFAiOMLO1gr0GOqUBRjFdAHut2%2FqqL1ST%2B0ir4mYq3geAt13Ydc1GuUrUcv%2BE8ycOAOm%2FtVSC6m3fG1%2BmP1KUHnQ4ld1W3IqJnc8YoN5UGBGoBu0bLwdxc%2BRY2Drfl%2BLCLzbBaKpepmC5XDsPh6mt0%2FnjW1AXrF%2Flz3c3Hlhg2lneydRayh7GJpkN6qjpE1wTb5Dt2RmITm4agnWDLMqaJDQmRjSUm429d4JT4Wc%2Fj6qf&X-Amz-Signature=e783caa0fe78408fbe8aabb773b067303e2116299d48e4e1cbd51b71dd74e673&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665226ZWEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8zEgsIBpZRdfZoh1mtnGv7mKM3wPmyQtYkG7U1MRNGAiEAv%2FtwqzhDtBR3vgHYQndnsFZWkfRlVXQDq2vHbNXM9XUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG7sqwJCTMjst4qoVircA2cFp2qrNGIcS3hIq2zuXP0YQy7g411pmorhDcJq2eg2CUpjk7gfITQHSBrxoz27qR%2FndCdihsXsNnLe44DwreSWSzLlfCcJwgAQS%2FmOI03EybOjaNtZC6o2rUIuUnx8LbBGTU9bzC7%2FhUH74%2Ft1ZoGWVWhliXRRv%2FKEx5WIwPWWzjEz%2B425hMCEhf01A2wi%2FLRfGenA5Quj6tGZ04CS3cfIGVnp0i6878AIIKNsjAZt%2FDjMItpgbe3ANFlOCuPU%2FgBn0Z5eu9wlzSl5nQEAPUR35M2WeiY3uLOMFBHo9ldaLh%2FOXr%2BvDPjY2B5Lq2kxjmmxMV3rqqrdvV9SShqHbdsZaiPvZYPN05os2CWKuWRNoRmEKxv8qvH0bhUwKV1VyLD0TKwjLU9JRu8xCC%2BevGjN07FdnrVNoyWiEqG%2BKL4VnEMaRKOxtdtvK2npvR8nH0cIn73hmZv4R9O18vYjyBi9l9RvuFrSaBcBSbYGewMl8gdSmTTsW4N7tYTT%2FqcA%2BbaXrNcdRCfGinmjP9fBcAEJyyjqU2AfAzMp0LGuXQ2UoNKy7nJkLJ5pjQ9bj5swce4ixAqiE7e6uQjLqAyNOv1hUA417AwftW9jW5ePl6UknseCp53ScT3uFAiOMLO1gr0GOqUBRjFdAHut2%2FqqL1ST%2B0ir4mYq3geAt13Ydc1GuUrUcv%2BE8ycOAOm%2FtVSC6m3fG1%2BmP1KUHnQ4ld1W3IqJnc8YoN5UGBGoBu0bLwdxc%2BRY2Drfl%2BLCLzbBaKpepmC5XDsPh6mt0%2FnjW1AXrF%2Flz3c3Hlhg2lneydRayh7GJpkN6qjpE1wTb5Dt2RmITm4agnWDLMqaJDQmRjSUm429d4JT4Wc%2Fj6qf&X-Amz-Signature=2bbf3d9e3d4d0bb6150a2b87e614fa1de8d01fd762de7ed1b358f84ffb01f36a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665226ZWEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8zEgsIBpZRdfZoh1mtnGv7mKM3wPmyQtYkG7U1MRNGAiEAv%2FtwqzhDtBR3vgHYQndnsFZWkfRlVXQDq2vHbNXM9XUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG7sqwJCTMjst4qoVircA2cFp2qrNGIcS3hIq2zuXP0YQy7g411pmorhDcJq2eg2CUpjk7gfITQHSBrxoz27qR%2FndCdihsXsNnLe44DwreSWSzLlfCcJwgAQS%2FmOI03EybOjaNtZC6o2rUIuUnx8LbBGTU9bzC7%2FhUH74%2Ft1ZoGWVWhliXRRv%2FKEx5WIwPWWzjEz%2B425hMCEhf01A2wi%2FLRfGenA5Quj6tGZ04CS3cfIGVnp0i6878AIIKNsjAZt%2FDjMItpgbe3ANFlOCuPU%2FgBn0Z5eu9wlzSl5nQEAPUR35M2WeiY3uLOMFBHo9ldaLh%2FOXr%2BvDPjY2B5Lq2kxjmmxMV3rqqrdvV9SShqHbdsZaiPvZYPN05os2CWKuWRNoRmEKxv8qvH0bhUwKV1VyLD0TKwjLU9JRu8xCC%2BevGjN07FdnrVNoyWiEqG%2BKL4VnEMaRKOxtdtvK2npvR8nH0cIn73hmZv4R9O18vYjyBi9l9RvuFrSaBcBSbYGewMl8gdSmTTsW4N7tYTT%2FqcA%2BbaXrNcdRCfGinmjP9fBcAEJyyjqU2AfAzMp0LGuXQ2UoNKy7nJkLJ5pjQ9bj5swce4ixAqiE7e6uQjLqAyNOv1hUA417AwftW9jW5ePl6UknseCp53ScT3uFAiOMLO1gr0GOqUBRjFdAHut2%2FqqL1ST%2B0ir4mYq3geAt13Ydc1GuUrUcv%2BE8ycOAOm%2FtVSC6m3fG1%2BmP1KUHnQ4ld1W3IqJnc8YoN5UGBGoBu0bLwdxc%2BRY2Drfl%2BLCLzbBaKpepmC5XDsPh6mt0%2FnjW1AXrF%2Flz3c3Hlhg2lneydRayh7GJpkN6qjpE1wTb5Dt2RmITm4agnWDLMqaJDQmRjSUm429d4JT4Wc%2Fj6qf&X-Amz-Signature=c352a65b87f7d279246e95352f7b35d33681b3602d83e7c1145e3ac46c511c66&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTEBOOUW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9LOex3SgNIfVbq8c4NTkIMlXHm9UW1iP2m5%2BCwGAhaQIgAPHFmgFTSmcinbMWoKV%2B5kTfxYwc2A3ydnadErFzSgkq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDMcwKGruWQyFGS9o5ircAw2NvzQWZcv6pKXDRVZZDaWtdThcq3lJAGtIntD3LP9bhOYfQE64F6EShj2fmnJ0pnlHMaKCRp6J1kefEQOfzufJc2Wn%2FSZCc4KRZxPYmF5RFzsGUAkeeIeP9wdgz7XcpF58h4LImcA0pyRP2MlOQ9PVuMsvtG0QBP1c5VxorxZzpaXPnTj1TZMDIG1qbAlV1btXSLce%2F%2B7spMP79J8KYlgcTpX5Rx%2BIfsF%2Bq30PfjozO6i436UTwMnXHbFWFDVih87XZD9dGdaIT8weCLd1qN0VbHNynKswmKb9XJ7QCCYKdSjOZtSwjyvBcb6ux5YsQQxEPJTE6nYtoHdw%2FrPsF4DBWHICKzmaiMm1aSAizt7YwuGGOyIfkzfhJhek8CXieJ%2BqTeZpETKXWRNstzKETvohrgg%2BhD8r54PneAOOsariRDp3I%2FZs7NL%2F9wJNFKYGfK6aoTIWHnmyS769RyrACKJo3BxocLVYs3j89niR9vhD%2Ffr2RGgMc6L3VjGK7ZmnpVNzX5Tb73OrB1Q0J%2FkfQodmVMQpz17W0B%2FwMmis1ZedBV8vKw0AJYeuTx9%2BzcXxU6%2FLTHJfKXQ54oV6lp1lzS9jsGVCZfCmQ48EwZ4KClPpoUjz4p1dn9iyxOBMMJO1gr0GOqUBnYgy8mIKUhPgpy5BAAvc9MizpYDkONQJXsQHquDQ1gEbR3prSgPYDk1drH3ReVNEWXfR0MhlxXF3Akf%2BFlm4RVOoyX7gpskWAsIgxBo8uu8c7OP1pMY2XCEG401LbqSCCpBcfN2nY0m14w6GKUeCKCJAQT%2B9VC3EcbaxIgyqJNXHtaghe1KegOguAaoD6UcXJNnWwf6ZRc9LlkXwMWinyI82iVIF&X-Amz-Signature=1cfe67f935ae7e6af29d7d1a5cd0e8d7b69cbc1a51ccede1b5b1fe3884b7b23f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X72D5OHB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2F2DqkFdk2SvZxVQkNHG%2BhfSndUwwXxdaP%2Fon8%2FYab9AiByE929ue5khZhVHITHVZ32E3Ucz3ZRsHG%2FRFM5yla%2BuCr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMfO3%2BkzFkoWQ7k2o7KtwDUjPuVk33dDBhpJX%2BUufkqZ6DE5K4jT1dp3yfNii%2FPtFMev3L%2BjnBKGUVE554wRK1ApxBIoEgYnO8kzeaKkHqKdQZSl5LoaT3CQWWdyzGf0ScP8VRoWHjh5F0Vlm5ol9ZvRQ88gP3mkMF9E%2FZYy0pEyBfU2r0O06HgWDRm7jiScxHlD%2BblOzss23dnletjdjRpzP6HN9VYFLGFIUBVuoyCe62ZIdylnQazN69yZDYMmOUP5wX3yHPL48VWT7QChXndOQ5PqqBMkD0lgaD94o5W93p4qIXjT%2BC6v4f2l%2B%2BnKBiB3V371cWmV6UoOsNFOoSbiUFlb%2BFN0kqRhX84huWGTrRKk3YCfU09BErSmwweu6UrJ3tUevavBObjbW7UeQ35OQ8NviVNW3%2BJC2OyDnwlReRO0Q5TLMSUDdCiI6Tt88aZPcDVNQ7ojC9vg4uipKl%2FhzBuU5hge8sIiZ6Dwel2rEGbmAw4%2FbOrnHABdMfOlGzNTjAEyJqZKJSw4RJq3tjauL8pPzEx4KUCdlLsN6lHfKT9NT3Y8z0v3fzIoz8Dcqz3Imb54zOYX1DSwZkIRzHX5jBfIgfoTCtUqNLewQb4Q2ASOmsRSuAlmPUf1ArzRjMbeMLoIMs5PMy%2B2Iw8bSCvQY6pgFIvFSr0NNFuQHVBUcZ3JOkIKbE6xmREKBP2lvYheTaXIwxcRx9ENsPXbsf4K2FOBgRZOYgYo95luRTuG3aoPkSXrh7dJ7f1K8y4aVJtUcw3ddvzobFc5zw0Q16eFTuF5vcMlDx4tpkDHmLtaa7dOs9XgVt15YPd3N25LqKOrx4eoMYopLl0Zw3NTI9Uzz3m5So3yZo702%2FShdPCpmLWV40CCmJxfhO&X-Amz-Signature=a9bbf51c88fdae06ead9935030e75038ab95155d124eb7650b23d18170db6b18&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CUG5GKA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7PvzR0edATmK94QuKOaY1PUsI%2BOiZiK4rjI6CaDJAnAiBA35ZRQ%2F1yPljioiTpU5SnNtadWeXWWqyxkJjhkh7Kfyr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMZVjSjrNNZ0hUJ8MmKtwDS4B%2BhujmmsnJ3WVFtZ6C%2BUEbkyLZnhSmLI4LTdMs7qF0nXSalgFw7E1MG9ILUu3j1I3GJNuMfWND4WCswqbX6oQ4hunEwWAl1GgCR5vuCYj28ytjSnTGEL5m2DF3HvVAWk4OW%2B7jW1MIZY6RBZcRggd93AwfphqxSUMUsy%2BRCUbJK%2Bx4c8Ms0ZBG75uRft3IBC6hFFLdTDGI9Z%2BRPvkjExLLSYcmP%2BSf%2BYXVU7oZBBkHzgXAngKAxsPEvp9bqYbYRLP4gadg4QIluBhfE5rqC%2BMo38R7khDFa%2B1nXmKhatY%2FlDi1SBFfK80%2ByPI6WOrWk0IPQj5NAInDR8iYILb439EGYGBBKTE2o1qGN%2BBI6IvPjiK4JgJSoKqi%2FpTORwvqujdpMoZXgcLipyDK3D%2BB%2BusDta6lklUx3coUKvoruTPvOVuHmowvEdj2487fre3V9jhOesk8t2D5EbFQ9swgfAXcYwnFBNfuHXNbz4YNA2Nzu7wlwlsCADpfqzNOkKSzrFq9BM12YedJ1qLE08jSECATpeGy78KXZFjr1EXUMQ29yftWncgxeSJYV81SG1hS5q7LBhGQF1GQm5VieZ0TJhnvIK6%2FABwv5DHx446RJs8g32M3EUYj5sd7Dy8wx7SCvQY6pgFJj19INJrntFDSrN869Eo7cpsbDF7ei2V2sBc7iKccSdAstwRJCrZnqhODLfBk2Ckhv9HIgnGu1dkoL27n01h8zFf1lyQB9ODeOMzSYUwls9lOQQQz6Pj5qDi%2Ffx6f2yy2jV4YPk%2F7pJGNGrJoeQR6Wu3jxxURh2kntj6jMXEmv5yNyOeHn4iNhoCJDidytGjSiENDNjwuMceKzC%2FK2cpP2aGq1S48&X-Amz-Signature=686f793416392d94f58fe0ab7905a6228a654121975484f9a3726cbae688cd22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPWQVBCX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDipMFmVGZlte0GKoRMrfVkLJOzTe6aEI644lDXwLREOgIgV7ZtoGP5SHv5%2BrnwRPY%2BQPutuOwCNXKm5Z4jduVTh8Aq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDLv71VGonTMSFkJvoircA6oabYOm1rPaciy0AiZzzb4T4N2QDNqj2UM6qRwjrbzuc9kjnMWQO8N20rpHU%2BVBoeLV2Z7HQtFNe74aLEK6E1cqfgl5VWd7nyJAaNL3iPjYJyakN%2BNaNLo84HrqoQUq8GJ90MM0oQ0oouh1t2OB%2FZHtLNukxUUuqbOOVm7f79691jJ2k7ip799KNIg3WQgr5gq4PcdcV38s3ORaEqGQvLqdW7Cv0LftM%2Bj7kQgzVarAWDqhv2CWBjc8Kh02r9NhzS9jtNQ%2FexsuFxB2%2FWqyAM6j2dmshqWqyxsHQdlu5yalWTqQGmxZ1CS91%2FNe772L2icUp34BywnK%2FRXhDmANPk3g%2B5qkab%2BWdOo%2BSQoHrp7mP0Jtf6R23ugUD1HJZX%2FvuEFr%2FZgHCG10cPQCgclsYM5Z%2Fqu%2Ffe5wzKEqXJbpk5cUmfcjtt768xTsPOr8Qw0HbXzptYNn1%2FXSKCbVZmKxaPDO9qUxhpPI%2B1PRank9mS77wcXwgqIknxx4IWxEr8XjueZxbKTLi8sml2%2FLnGSQOe%2FJCZw9b6GeAb3kI9SohjxeE%2BeLQ7taDOV%2FQnrzwz7qPHGHnRhKNZxca52Xr2%2B69wU6tmqdmzYvsS%2BmS5%2FQAE9dpkQOEnfvZtRhXtg9MLi1gr0GOqUBdKATfnrx%2FF16KrnGvlPKYiuBh044Zk2Qfb%2Fe09tqGu2AWwR2r%2FkRae%2FuIV56f05xA7nan8B2yP2MpPiRJ39PXUxCPSpyhk2NnwK7qNYWDHK3SEwI5pVWFVyY38wawixmDBUEdiWjok%2BJKEYVkjG5LC9iUgVwgdshM67%2BXEs3RJfqsV1epzrk2PGohbhcojiidbHC2Zu2zcoWOGvs1KNZbe8jpTMe&X-Amz-Signature=697a5e84b27aff82159630e004e8a0a03cea758dc5145728d1175506dafced8b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPWQVBCX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDipMFmVGZlte0GKoRMrfVkLJOzTe6aEI644lDXwLREOgIgV7ZtoGP5SHv5%2BrnwRPY%2BQPutuOwCNXKm5Z4jduVTh8Aq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDLv71VGonTMSFkJvoircA6oabYOm1rPaciy0AiZzzb4T4N2QDNqj2UM6qRwjrbzuc9kjnMWQO8N20rpHU%2BVBoeLV2Z7HQtFNe74aLEK6E1cqfgl5VWd7nyJAaNL3iPjYJyakN%2BNaNLo84HrqoQUq8GJ90MM0oQ0oouh1t2OB%2FZHtLNukxUUuqbOOVm7f79691jJ2k7ip799KNIg3WQgr5gq4PcdcV38s3ORaEqGQvLqdW7Cv0LftM%2Bj7kQgzVarAWDqhv2CWBjc8Kh02r9NhzS9jtNQ%2FexsuFxB2%2FWqyAM6j2dmshqWqyxsHQdlu5yalWTqQGmxZ1CS91%2FNe772L2icUp34BywnK%2FRXhDmANPk3g%2B5qkab%2BWdOo%2BSQoHrp7mP0Jtf6R23ugUD1HJZX%2FvuEFr%2FZgHCG10cPQCgclsYM5Z%2Fqu%2Ffe5wzKEqXJbpk5cUmfcjtt768xTsPOr8Qw0HbXzptYNn1%2FXSKCbVZmKxaPDO9qUxhpPI%2B1PRank9mS77wcXwgqIknxx4IWxEr8XjueZxbKTLi8sml2%2FLnGSQOe%2FJCZw9b6GeAb3kI9SohjxeE%2BeLQ7taDOV%2FQnrzwz7qPHGHnRhKNZxca52Xr2%2B69wU6tmqdmzYvsS%2BmS5%2FQAE9dpkQOEnfvZtRhXtg9MLi1gr0GOqUBdKATfnrx%2FF16KrnGvlPKYiuBh044Zk2Qfb%2Fe09tqGu2AWwR2r%2FkRae%2FuIV56f05xA7nan8B2yP2MpPiRJ39PXUxCPSpyhk2NnwK7qNYWDHK3SEwI5pVWFVyY38wawixmDBUEdiWjok%2BJKEYVkjG5LC9iUgVwgdshM67%2BXEs3RJfqsV1epzrk2PGohbhcojiidbHC2Zu2zcoWOGvs1KNZbe8jpTMe&X-Amz-Signature=93a996d71cded412c11c926adc5515092c9127a86dcb4dfc39573178041734a4&X-Amz-SignedHeaders=host&x-id=GetObject)

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
