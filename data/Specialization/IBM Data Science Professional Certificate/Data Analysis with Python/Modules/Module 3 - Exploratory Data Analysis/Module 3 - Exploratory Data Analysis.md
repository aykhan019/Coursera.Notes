

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URKDUQMT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDI1xXx1xBpNxW4KqR2YUpdMNW242RDc8kyh%2FmLYtH03gIhAPjHjeHBGbgJFzWX9fplzubXx1WRRSEs7rQ9mN7YvmuAKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxvxYBDJ1Ta2Eppi8q3AN6ojhyHXOsAAXVn1Fn7WXFP7VhYQ798V7xYe5451wi50qQO68bL2Mnb8SYQMUMdMAh7W9KhRatMRdEm%2FUV8s%2BskOtIPW2YjMzZ3xJZJXBu9cI9SSldwrfAsPp%2BtU7WU3YQJcd%2FmcJy6%2BW5WtnZyvUiqyXOhBOxsjukP2qzZVwLZ7hfqVP%2BtCIUcB05Pm6aGFoDHweBw%2B5ir%2BST3qz3pBJabrO5c6sAw7lgdMB1MAIHL2A7aXtlzG5OSIjqRm%2BAOK1oQEnWpOyvo9g0C9P%2B91gZ9q0Ld0kaQqwSI3Ye53citkLpbe4aqPwkuDWkk1M4v9lGZwWhqTrhHz3aSPp%2FVUfyGxWxBQ9TFKAzwCI8nH%2FDX3v3SzowOPqM8YiUmwNaqXwdxeNBu9dwu5fz5z9AhH3GfrpjiiNlvrKO5t9Za6t%2B%2FbTOYidZcdNAIig5lTdC86gneg%2FYvR8UPk2k%2Bp5l0BzI8lgX%2BYKxNS6Bz4rSZMUfzbDKNe7vsElMN1C0t7S4nLwxCj8j%2BUE64M2iqiWEvBJ2TwQP6HiXEKSz4jM6Riy12BpS3xcLWQPMaBjFYhPzP06GKoxNeOs7Jao1s1mDU4YparFUNcMeDFSsq1HaGNYopKjoJ9qBHR6EeLTWTjDf0PC8BjqkAcZ%2B9BQUyntl1t6n720x%2Fz%2FO%2F%2Bkp4dTPky%2FG68msCoklQ8BHh23iFc2uOTa3yG9zoLkuI5ZW73axNUh%2BJwni8KjzwBmJtGga%2BjzW9a7cflEsnhH7KuVcCOgSntltnIZS6Z%2B4iBazSYnxN78q%2BLXOXSKapc2cPny1ZMnTX66yk%2Bw1IDGVSKpoDfwSNbWHCSPtn7NY%2B7t72MW%2FAyhrzN0jUzJ%2FEj6d&X-Amz-Signature=7e9256542c4460493b173ac67742d915d3afec73ecf055c97ba152ab191151e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URKDUQMT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDI1xXx1xBpNxW4KqR2YUpdMNW242RDc8kyh%2FmLYtH03gIhAPjHjeHBGbgJFzWX9fplzubXx1WRRSEs7rQ9mN7YvmuAKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxvxYBDJ1Ta2Eppi8q3AN6ojhyHXOsAAXVn1Fn7WXFP7VhYQ798V7xYe5451wi50qQO68bL2Mnb8SYQMUMdMAh7W9KhRatMRdEm%2FUV8s%2BskOtIPW2YjMzZ3xJZJXBu9cI9SSldwrfAsPp%2BtU7WU3YQJcd%2FmcJy6%2BW5WtnZyvUiqyXOhBOxsjukP2qzZVwLZ7hfqVP%2BtCIUcB05Pm6aGFoDHweBw%2B5ir%2BST3qz3pBJabrO5c6sAw7lgdMB1MAIHL2A7aXtlzG5OSIjqRm%2BAOK1oQEnWpOyvo9g0C9P%2B91gZ9q0Ld0kaQqwSI3Ye53citkLpbe4aqPwkuDWkk1M4v9lGZwWhqTrhHz3aSPp%2FVUfyGxWxBQ9TFKAzwCI8nH%2FDX3v3SzowOPqM8YiUmwNaqXwdxeNBu9dwu5fz5z9AhH3GfrpjiiNlvrKO5t9Za6t%2B%2FbTOYidZcdNAIig5lTdC86gneg%2FYvR8UPk2k%2Bp5l0BzI8lgX%2BYKxNS6Bz4rSZMUfzbDKNe7vsElMN1C0t7S4nLwxCj8j%2BUE64M2iqiWEvBJ2TwQP6HiXEKSz4jM6Riy12BpS3xcLWQPMaBjFYhPzP06GKoxNeOs7Jao1s1mDU4YparFUNcMeDFSsq1HaGNYopKjoJ9qBHR6EeLTWTjDf0PC8BjqkAcZ%2B9BQUyntl1t6n720x%2Fz%2FO%2F%2Bkp4dTPky%2FG68msCoklQ8BHh23iFc2uOTa3yG9zoLkuI5ZW73axNUh%2BJwni8KjzwBmJtGga%2BjzW9a7cflEsnhH7KuVcCOgSntltnIZS6Z%2B4iBazSYnxN78q%2BLXOXSKapc2cPny1ZMnTX66yk%2Bw1IDGVSKpoDfwSNbWHCSPtn7NY%2B7t72MW%2FAyhrzN0jUzJ%2FEj6d&X-Amz-Signature=ffe16346e33c2290adff7ef956a536bfedab142b755f23b5ffa9c2e31155c23a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URKDUQMT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDI1xXx1xBpNxW4KqR2YUpdMNW242RDc8kyh%2FmLYtH03gIhAPjHjeHBGbgJFzWX9fplzubXx1WRRSEs7rQ9mN7YvmuAKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxvxYBDJ1Ta2Eppi8q3AN6ojhyHXOsAAXVn1Fn7WXFP7VhYQ798V7xYe5451wi50qQO68bL2Mnb8SYQMUMdMAh7W9KhRatMRdEm%2FUV8s%2BskOtIPW2YjMzZ3xJZJXBu9cI9SSldwrfAsPp%2BtU7WU3YQJcd%2FmcJy6%2BW5WtnZyvUiqyXOhBOxsjukP2qzZVwLZ7hfqVP%2BtCIUcB05Pm6aGFoDHweBw%2B5ir%2BST3qz3pBJabrO5c6sAw7lgdMB1MAIHL2A7aXtlzG5OSIjqRm%2BAOK1oQEnWpOyvo9g0C9P%2B91gZ9q0Ld0kaQqwSI3Ye53citkLpbe4aqPwkuDWkk1M4v9lGZwWhqTrhHz3aSPp%2FVUfyGxWxBQ9TFKAzwCI8nH%2FDX3v3SzowOPqM8YiUmwNaqXwdxeNBu9dwu5fz5z9AhH3GfrpjiiNlvrKO5t9Za6t%2B%2FbTOYidZcdNAIig5lTdC86gneg%2FYvR8UPk2k%2Bp5l0BzI8lgX%2BYKxNS6Bz4rSZMUfzbDKNe7vsElMN1C0t7S4nLwxCj8j%2BUE64M2iqiWEvBJ2TwQP6HiXEKSz4jM6Riy12BpS3xcLWQPMaBjFYhPzP06GKoxNeOs7Jao1s1mDU4YparFUNcMeDFSsq1HaGNYopKjoJ9qBHR6EeLTWTjDf0PC8BjqkAcZ%2B9BQUyntl1t6n720x%2Fz%2FO%2F%2Bkp4dTPky%2FG68msCoklQ8BHh23iFc2uOTa3yG9zoLkuI5ZW73axNUh%2BJwni8KjzwBmJtGga%2BjzW9a7cflEsnhH7KuVcCOgSntltnIZS6Z%2B4iBazSYnxN78q%2BLXOXSKapc2cPny1ZMnTX66yk%2Bw1IDGVSKpoDfwSNbWHCSPtn7NY%2B7t72MW%2FAyhrzN0jUzJ%2FEj6d&X-Amz-Signature=dd3331a12c8921c4c3d91c5c0d76a83971dec67c434a90c94033e70d5655af8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4PRSCTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOjm56ccvyxHlEojq2hQduGLR3PWZd8ACb05oIcVe%2BagIhANzsIUX4vIY0%2BJK8RBhbfkVTPxRJ%2FIq4x6xqHxCIo9MuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDmCTAMfhdyyJnv7sq3AOzygbjLtwzNbYdXPgzMtzR5PD9EfVVtdOK9MR%2FLReXAb5WbEOeNgWHF%2B0Qfbhs0WjQ1nzCLYHU3Z9r8fsQTI77jGPWxhkDV69b8KAPGg6g0vK3%2F%2BXdcysjSGTZbgS5zNw6ylO66DCfTZlgeRJDplFBUuw2IkR797K%2FhlXjErE3YwtuFrgQEXVqLe2Bxc3b%2B9toEHgW9KBXwqhIUJjbRJhPmSs6rCaq4hAqLxAVU9PoJR0b3PlY%2B%2FE75blgeAyfiz%2Bx%2BahqoG1%2F4f%2FJJD5x3ElF4SBePwMbxxPbL%2FiDn%2BuUCRsx7gM6WlQTiHK2GSDYOBxjWDhhegvag8XT7hST4FtK6SP%2BDy%2FZ9PsRTS5fRzwg%2BYf9M0GG4pxJmNoJXRCpj5xMfuekMHrOMhiRHflLpz8xxBJcNb0%2Fj3ZXwu269ysp4VE%2Byj5Qm6rAqfKGE0KjqE%2F77CVPnPxH102qydrErFaLPer4iMuDRUMdyANQPP7PWUhZvAnWkyLP%2F%2FHUHpTYgCC5N1%2BHQpsaHvviTqApIbCu27drzED%2Bu41XKCBM0vMTVAM9uouIoBrR%2FY%2B5B8M6fkhi0XdefgfecK9ShU4KlixSX%2B2J6C9WhC8kxoALFd81UOMbaIuoCEBXUb6%2FOTDc0fC8BjqkAc89vX3%2BesDxu%2F6VIN7Z%2FS2tlozECMbztTqN5yMSRaVrrHFrBjpq2bKWNesN0cHw%2BX7ucUnfJcHy8jv0JWyqmBk%2BPyjUBVcZCMMoKlXTMs4U0s7b88uACWcP1%2B49psO6YzPWHls8mNgwNoIHYUpVDlAJFPwLjFLBgq08FLepx97f1ue0DSIDnhsvVdGu4ZgYm%2B%2FMfiHOjYG9e7k8EQHfWuSBrRAL&X-Amz-Signature=1109325221dfadd48535a284996dd9f51d29257704d56ef0d97518b918acce12&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4PRSCTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOjm56ccvyxHlEojq2hQduGLR3PWZd8ACb05oIcVe%2BagIhANzsIUX4vIY0%2BJK8RBhbfkVTPxRJ%2FIq4x6xqHxCIo9MuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDmCTAMfhdyyJnv7sq3AOzygbjLtwzNbYdXPgzMtzR5PD9EfVVtdOK9MR%2FLReXAb5WbEOeNgWHF%2B0Qfbhs0WjQ1nzCLYHU3Z9r8fsQTI77jGPWxhkDV69b8KAPGg6g0vK3%2F%2BXdcysjSGTZbgS5zNw6ylO66DCfTZlgeRJDplFBUuw2IkR797K%2FhlXjErE3YwtuFrgQEXVqLe2Bxc3b%2B9toEHgW9KBXwqhIUJjbRJhPmSs6rCaq4hAqLxAVU9PoJR0b3PlY%2B%2FE75blgeAyfiz%2Bx%2BahqoG1%2F4f%2FJJD5x3ElF4SBePwMbxxPbL%2FiDn%2BuUCRsx7gM6WlQTiHK2GSDYOBxjWDhhegvag8XT7hST4FtK6SP%2BDy%2FZ9PsRTS5fRzwg%2BYf9M0GG4pxJmNoJXRCpj5xMfuekMHrOMhiRHflLpz8xxBJcNb0%2Fj3ZXwu269ysp4VE%2Byj5Qm6rAqfKGE0KjqE%2F77CVPnPxH102qydrErFaLPer4iMuDRUMdyANQPP7PWUhZvAnWkyLP%2F%2FHUHpTYgCC5N1%2BHQpsaHvviTqApIbCu27drzED%2Bu41XKCBM0vMTVAM9uouIoBrR%2FY%2B5B8M6fkhi0XdefgfecK9ShU4KlixSX%2B2J6C9WhC8kxoALFd81UOMbaIuoCEBXUb6%2FOTDc0fC8BjqkAc89vX3%2BesDxu%2F6VIN7Z%2FS2tlozECMbztTqN5yMSRaVrrHFrBjpq2bKWNesN0cHw%2BX7ucUnfJcHy8jv0JWyqmBk%2BPyjUBVcZCMMoKlXTMs4U0s7b88uACWcP1%2B49psO6YzPWHls8mNgwNoIHYUpVDlAJFPwLjFLBgq08FLepx97f1ue0DSIDnhsvVdGu4ZgYm%2B%2FMfiHOjYG9e7k8EQHfWuSBrRAL&X-Amz-Signature=81df749c596ebea513a90ca0f968fa0511bdf88d11e06e44e183b3431bc5e84c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4PRSCTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOjm56ccvyxHlEojq2hQduGLR3PWZd8ACb05oIcVe%2BagIhANzsIUX4vIY0%2BJK8RBhbfkVTPxRJ%2FIq4x6xqHxCIo9MuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDmCTAMfhdyyJnv7sq3AOzygbjLtwzNbYdXPgzMtzR5PD9EfVVtdOK9MR%2FLReXAb5WbEOeNgWHF%2B0Qfbhs0WjQ1nzCLYHU3Z9r8fsQTI77jGPWxhkDV69b8KAPGg6g0vK3%2F%2BXdcysjSGTZbgS5zNw6ylO66DCfTZlgeRJDplFBUuw2IkR797K%2FhlXjErE3YwtuFrgQEXVqLe2Bxc3b%2B9toEHgW9KBXwqhIUJjbRJhPmSs6rCaq4hAqLxAVU9PoJR0b3PlY%2B%2FE75blgeAyfiz%2Bx%2BahqoG1%2F4f%2FJJD5x3ElF4SBePwMbxxPbL%2FiDn%2BuUCRsx7gM6WlQTiHK2GSDYOBxjWDhhegvag8XT7hST4FtK6SP%2BDy%2FZ9PsRTS5fRzwg%2BYf9M0GG4pxJmNoJXRCpj5xMfuekMHrOMhiRHflLpz8xxBJcNb0%2Fj3ZXwu269ysp4VE%2Byj5Qm6rAqfKGE0KjqE%2F77CVPnPxH102qydrErFaLPer4iMuDRUMdyANQPP7PWUhZvAnWkyLP%2F%2FHUHpTYgCC5N1%2BHQpsaHvviTqApIbCu27drzED%2Bu41XKCBM0vMTVAM9uouIoBrR%2FY%2B5B8M6fkhi0XdefgfecK9ShU4KlixSX%2B2J6C9WhC8kxoALFd81UOMbaIuoCEBXUb6%2FOTDc0fC8BjqkAc89vX3%2BesDxu%2F6VIN7Z%2FS2tlozECMbztTqN5yMSRaVrrHFrBjpq2bKWNesN0cHw%2BX7ucUnfJcHy8jv0JWyqmBk%2BPyjUBVcZCMMoKlXTMs4U0s7b88uACWcP1%2B49psO6YzPWHls8mNgwNoIHYUpVDlAJFPwLjFLBgq08FLepx97f1ue0DSIDnhsvVdGu4ZgYm%2B%2FMfiHOjYG9e7k8EQHfWuSBrRAL&X-Amz-Signature=5f3c75aeef084984bd8777abbc6be46fad92ae88d492a59b2699c16e0047f5bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4PRSCTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOjm56ccvyxHlEojq2hQduGLR3PWZd8ACb05oIcVe%2BagIhANzsIUX4vIY0%2BJK8RBhbfkVTPxRJ%2FIq4x6xqHxCIo9MuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDmCTAMfhdyyJnv7sq3AOzygbjLtwzNbYdXPgzMtzR5PD9EfVVtdOK9MR%2FLReXAb5WbEOeNgWHF%2B0Qfbhs0WjQ1nzCLYHU3Z9r8fsQTI77jGPWxhkDV69b8KAPGg6g0vK3%2F%2BXdcysjSGTZbgS5zNw6ylO66DCfTZlgeRJDplFBUuw2IkR797K%2FhlXjErE3YwtuFrgQEXVqLe2Bxc3b%2B9toEHgW9KBXwqhIUJjbRJhPmSs6rCaq4hAqLxAVU9PoJR0b3PlY%2B%2FE75blgeAyfiz%2Bx%2BahqoG1%2F4f%2FJJD5x3ElF4SBePwMbxxPbL%2FiDn%2BuUCRsx7gM6WlQTiHK2GSDYOBxjWDhhegvag8XT7hST4FtK6SP%2BDy%2FZ9PsRTS5fRzwg%2BYf9M0GG4pxJmNoJXRCpj5xMfuekMHrOMhiRHflLpz8xxBJcNb0%2Fj3ZXwu269ysp4VE%2Byj5Qm6rAqfKGE0KjqE%2F77CVPnPxH102qydrErFaLPer4iMuDRUMdyANQPP7PWUhZvAnWkyLP%2F%2FHUHpTYgCC5N1%2BHQpsaHvviTqApIbCu27drzED%2Bu41XKCBM0vMTVAM9uouIoBrR%2FY%2B5B8M6fkhi0XdefgfecK9ShU4KlixSX%2B2J6C9WhC8kxoALFd81UOMbaIuoCEBXUb6%2FOTDc0fC8BjqkAc89vX3%2BesDxu%2F6VIN7Z%2FS2tlozECMbztTqN5yMSRaVrrHFrBjpq2bKWNesN0cHw%2BX7ucUnfJcHy8jv0JWyqmBk%2BPyjUBVcZCMMoKlXTMs4U0s7b88uACWcP1%2B49psO6YzPWHls8mNgwNoIHYUpVDlAJFPwLjFLBgq08FLepx97f1ue0DSIDnhsvVdGu4ZgYm%2B%2FMfiHOjYG9e7k8EQHfWuSBrRAL&X-Amz-Signature=082b1d21789a1319739532e5b24a0dc101315a5ff8e9cd65421e4f9984be9f40&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4PRSCTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOjm56ccvyxHlEojq2hQduGLR3PWZd8ACb05oIcVe%2BagIhANzsIUX4vIY0%2BJK8RBhbfkVTPxRJ%2FIq4x6xqHxCIo9MuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDmCTAMfhdyyJnv7sq3AOzygbjLtwzNbYdXPgzMtzR5PD9EfVVtdOK9MR%2FLReXAb5WbEOeNgWHF%2B0Qfbhs0WjQ1nzCLYHU3Z9r8fsQTI77jGPWxhkDV69b8KAPGg6g0vK3%2F%2BXdcysjSGTZbgS5zNw6ylO66DCfTZlgeRJDplFBUuw2IkR797K%2FhlXjErE3YwtuFrgQEXVqLe2Bxc3b%2B9toEHgW9KBXwqhIUJjbRJhPmSs6rCaq4hAqLxAVU9PoJR0b3PlY%2B%2FE75blgeAyfiz%2Bx%2BahqoG1%2F4f%2FJJD5x3ElF4SBePwMbxxPbL%2FiDn%2BuUCRsx7gM6WlQTiHK2GSDYOBxjWDhhegvag8XT7hST4FtK6SP%2BDy%2FZ9PsRTS5fRzwg%2BYf9M0GG4pxJmNoJXRCpj5xMfuekMHrOMhiRHflLpz8xxBJcNb0%2Fj3ZXwu269ysp4VE%2Byj5Qm6rAqfKGE0KjqE%2F77CVPnPxH102qydrErFaLPer4iMuDRUMdyANQPP7PWUhZvAnWkyLP%2F%2FHUHpTYgCC5N1%2BHQpsaHvviTqApIbCu27drzED%2Bu41XKCBM0vMTVAM9uouIoBrR%2FY%2B5B8M6fkhi0XdefgfecK9ShU4KlixSX%2B2J6C9WhC8kxoALFd81UOMbaIuoCEBXUb6%2FOTDc0fC8BjqkAc89vX3%2BesDxu%2F6VIN7Z%2FS2tlozECMbztTqN5yMSRaVrrHFrBjpq2bKWNesN0cHw%2BX7ucUnfJcHy8jv0JWyqmBk%2BPyjUBVcZCMMoKlXTMs4U0s7b88uACWcP1%2B49psO6YzPWHls8mNgwNoIHYUpVDlAJFPwLjFLBgq08FLepx97f1ue0DSIDnhsvVdGu4ZgYm%2B%2FMfiHOjYG9e7k8EQHfWuSBrRAL&X-Amz-Signature=f48d2d4d5f72f46ebb979999dce6aa69806ef85b808851bfccd03ab16f5b6540&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4PRSCTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOjm56ccvyxHlEojq2hQduGLR3PWZd8ACb05oIcVe%2BagIhANzsIUX4vIY0%2BJK8RBhbfkVTPxRJ%2FIq4x6xqHxCIo9MuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDmCTAMfhdyyJnv7sq3AOzygbjLtwzNbYdXPgzMtzR5PD9EfVVtdOK9MR%2FLReXAb5WbEOeNgWHF%2B0Qfbhs0WjQ1nzCLYHU3Z9r8fsQTI77jGPWxhkDV69b8KAPGg6g0vK3%2F%2BXdcysjSGTZbgS5zNw6ylO66DCfTZlgeRJDplFBUuw2IkR797K%2FhlXjErE3YwtuFrgQEXVqLe2Bxc3b%2B9toEHgW9KBXwqhIUJjbRJhPmSs6rCaq4hAqLxAVU9PoJR0b3PlY%2B%2FE75blgeAyfiz%2Bx%2BahqoG1%2F4f%2FJJD5x3ElF4SBePwMbxxPbL%2FiDn%2BuUCRsx7gM6WlQTiHK2GSDYOBxjWDhhegvag8XT7hST4FtK6SP%2BDy%2FZ9PsRTS5fRzwg%2BYf9M0GG4pxJmNoJXRCpj5xMfuekMHrOMhiRHflLpz8xxBJcNb0%2Fj3ZXwu269ysp4VE%2Byj5Qm6rAqfKGE0KjqE%2F77CVPnPxH102qydrErFaLPer4iMuDRUMdyANQPP7PWUhZvAnWkyLP%2F%2FHUHpTYgCC5N1%2BHQpsaHvviTqApIbCu27drzED%2Bu41XKCBM0vMTVAM9uouIoBrR%2FY%2B5B8M6fkhi0XdefgfecK9ShU4KlixSX%2B2J6C9WhC8kxoALFd81UOMbaIuoCEBXUb6%2FOTDc0fC8BjqkAc89vX3%2BesDxu%2F6VIN7Z%2FS2tlozECMbztTqN5yMSRaVrrHFrBjpq2bKWNesN0cHw%2BX7ucUnfJcHy8jv0JWyqmBk%2BPyjUBVcZCMMoKlXTMs4U0s7b88uACWcP1%2B49psO6YzPWHls8mNgwNoIHYUpVDlAJFPwLjFLBgq08FLepx97f1ue0DSIDnhsvVdGu4ZgYm%2B%2FMfiHOjYG9e7k8EQHfWuSBrRAL&X-Amz-Signature=f7f2ccb686085d11ad06dfb6701eefa5b901f521d7ad05c6163dd8a48a518887&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ECJMUEL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDv8fuLKqoN3DECTGZ53tpWZ23v4Pb8bH%2Bf%2B1ooE%2Fx2QgIhANfwYp8vmk%2BE%2F5GLzHojTvzOqz4%2F2kB%2F9KdjcUNARRkpKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyHFd2Ubb2YGKq40tMq3AM5BYrdtaBInYc6xr0%2FvtKFOqwtBt05DXpyi1jc%2B%2BZwDw5DZnpFQCzr7WNKuWZUky7Il0noZmnJzskj96dEmt1CTUYApQhGXhC5SVDYXxWQqw%2FGFewqBrXXgyD4ybF7OP46VQi%2FpRjmy8jMqSqifON%2F3zwT9uI73DBx07gMxDMUx5k%2FGwiDtm6LKNy%2FCGEXtGd%2FmofG6iSFKzADgEN8hw77ICbYEovgojdY1sT81%2FV3b3ZlsgFd9SpSIKAvFuSTSz%2FYFtwis2JYDV56SoAgm5%2BbmxXvuQJ8YaQaR3ZW9sYcyrVJjN2q5EH3KaYhSqUy7lil3wpf1CRNJ6ojvR4iCrs%2BuxIy0eQjWAlIFxKBwT4HWOH75Fpbj3wkgGJleXrl0mbbS4A%2Be0UZ8fVX2IS9ozP4CKlk9CukL54KrH7Z1GASb6mrM2M2eNZu3HliawkZqrG8%2BXZEwZULyQNcYIw5YJd1iQ7fejegp%2B0lg9EpQBsd8Gj3RYq31spJr6Q1JSt7juGX4mBZb67uqgxOupLdCZG%2F9YQrAobiISNKPoJHcGOtFjhRBLCb9GTh6xsfzD1D62XyxC0MDrD5sNC4%2FL89EipTHlQhv9BA1lROYBzqvJGmLSm17CcezlKqtSJMvDDy0PC8BjqkAZr7HncghUc5xvPQ27lJn6kaBahrf%2B4k0gQQWRd0RNM0NZnrNg%2BsHpXra7o4FgjSTd0BAb85nvgRjeootExIhi%2Bn1DIRz8iWRSH89nfgJqJmFmUeWQByNPZNtCeUteHeqfa8RcNlpuuRiBXrZjKFAUX5GXYJkvx6eY9%2Fq2scBByrpSBn9y85iHGsFHlZCjn3nQ2pd3juVuwRlkOPxKwJPAGzUKJr&X-Amz-Signature=db490cbd69bed1d33867d1870de1473467ee2b2db3ac0023e4ef63c8a937d61f&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Y6F7FSM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNID34qzg1eckxr5Rh%2BaKK4nWNYjNUr%2FJOI20tnh90CQIgHUJU%2BmgGIFaH%2BP51IdpyMMPjh5eJHiKbl9avJXJdocIqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDC7wF77Cw%2BiGae5kCrcA25kuuAErcZnO52tw2TCOb0c8KMEiXiytrZTGTvyjpGIQg3841uNuvpsNp5rHDF3lA0xVcFpK3u3VCry7wO1lpzWA7k6NfuzVBOsDggj8xEMbmcArLggiSeimlBSzGUJEKK3ASql8fGuMuaMvQXn4WACXz0sKUGv5gmKpixeM7e%2B8as%2BnF30EBoFhxHtMULjte4cn6UZSc9VGY3h38ZDxmvb6IYjFKzvmBuxAtphamVsFsT7th6o2Yxg%2BtXucyRIsRF6kUu5d34lX9dJGlrXt7QyHTmQ9xV1cYEefPm9hTl2g2Yz4t7gHq5BzPJtbo2PP1l4KbsL0ltgbCgtakWJIYjc0WAx4IhoJg3pTYcYRqI5K5l9xB03fyeKLnm%2FVbVn1m%2FbukpK5e6jLTa3X9HOQLGHmpqZiEILxgllzpZr4Ds1mgMKbou4f3TagICoME4Q7JA30VxXFDqFzphaTDmnVI%2FbDOfaPMLjiig3RkSAZWxExyfeYmc%2Bzjluo0qdJeI52Ev85cUO%2BOWrESWz00OM%2BUFz30jjzDzfIBcFxHFaLClmDtNYwJ%2FA6CiyQkS7Jipr6LOXT4TqiXEbC%2F1nLLe9Q5Kj9u15dPoUpcrDsVC9Qtvico4911qPvxZ2gELUMJTR8LwGOqUBIll452mOQb8ogK%2BL%2BOaPWHJqGrStkCMsOi4TU9V76pYCIGCTi5Uf%2Ba%2F14O9bXjUseFO%2F2TvexZGgWQJ%2BVQgWHeraRM%2FLMYIuLJA5Utc4v%2FFHPsbVkoC2V4qCYZsyqTuRe9ADvhLwzXvw4Br54Z05mSeC%2FdEofPbxX5ZrudNKYfNtuY%2BDYoJIbkVuphvRfA3j8DIWj8QaiiKxuoAX%2F1cKISlxgeJE&X-Amz-Signature=a26f15b62d9e9ea18eae8fb7a00f70535a99a08236552f037f1352e6186ed84f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4PRSCTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOjm56ccvyxHlEojq2hQduGLR3PWZd8ACb05oIcVe%2BagIhANzsIUX4vIY0%2BJK8RBhbfkVTPxRJ%2FIq4x6xqHxCIo9MuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDmCTAMfhdyyJnv7sq3AOzygbjLtwzNbYdXPgzMtzR5PD9EfVVtdOK9MR%2FLReXAb5WbEOeNgWHF%2B0Qfbhs0WjQ1nzCLYHU3Z9r8fsQTI77jGPWxhkDV69b8KAPGg6g0vK3%2F%2BXdcysjSGTZbgS5zNw6ylO66DCfTZlgeRJDplFBUuw2IkR797K%2FhlXjErE3YwtuFrgQEXVqLe2Bxc3b%2B9toEHgW9KBXwqhIUJjbRJhPmSs6rCaq4hAqLxAVU9PoJR0b3PlY%2B%2FE75blgeAyfiz%2Bx%2BahqoG1%2F4f%2FJJD5x3ElF4SBePwMbxxPbL%2FiDn%2BuUCRsx7gM6WlQTiHK2GSDYOBxjWDhhegvag8XT7hST4FtK6SP%2BDy%2FZ9PsRTS5fRzwg%2BYf9M0GG4pxJmNoJXRCpj5xMfuekMHrOMhiRHflLpz8xxBJcNb0%2Fj3ZXwu269ysp4VE%2Byj5Qm6rAqfKGE0KjqE%2F77CVPnPxH102qydrErFaLPer4iMuDRUMdyANQPP7PWUhZvAnWkyLP%2F%2FHUHpTYgCC5N1%2BHQpsaHvviTqApIbCu27drzED%2Bu41XKCBM0vMTVAM9uouIoBrR%2FY%2B5B8M6fkhi0XdefgfecK9ShU4KlixSX%2B2J6C9WhC8kxoALFd81UOMbaIuoCEBXUb6%2FOTDc0fC8BjqkAc89vX3%2BesDxu%2F6VIN7Z%2FS2tlozECMbztTqN5yMSRaVrrHFrBjpq2bKWNesN0cHw%2BX7ucUnfJcHy8jv0JWyqmBk%2BPyjUBVcZCMMoKlXTMs4U0s7b88uACWcP1%2B49psO6YzPWHls8mNgwNoIHYUpVDlAJFPwLjFLBgq08FLepx97f1ue0DSIDnhsvVdGu4ZgYm%2B%2FMfiHOjYG9e7k8EQHfWuSBrRAL&X-Amz-Signature=00c4fb8a45e3bee9ce805447985820bc626d8ba5373ca44452aeece42aedf6dd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4PRSCTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOjm56ccvyxHlEojq2hQduGLR3PWZd8ACb05oIcVe%2BagIhANzsIUX4vIY0%2BJK8RBhbfkVTPxRJ%2FIq4x6xqHxCIo9MuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDmCTAMfhdyyJnv7sq3AOzygbjLtwzNbYdXPgzMtzR5PD9EfVVtdOK9MR%2FLReXAb5WbEOeNgWHF%2B0Qfbhs0WjQ1nzCLYHU3Z9r8fsQTI77jGPWxhkDV69b8KAPGg6g0vK3%2F%2BXdcysjSGTZbgS5zNw6ylO66DCfTZlgeRJDplFBUuw2IkR797K%2FhlXjErE3YwtuFrgQEXVqLe2Bxc3b%2B9toEHgW9KBXwqhIUJjbRJhPmSs6rCaq4hAqLxAVU9PoJR0b3PlY%2B%2FE75blgeAyfiz%2Bx%2BahqoG1%2F4f%2FJJD5x3ElF4SBePwMbxxPbL%2FiDn%2BuUCRsx7gM6WlQTiHK2GSDYOBxjWDhhegvag8XT7hST4FtK6SP%2BDy%2FZ9PsRTS5fRzwg%2BYf9M0GG4pxJmNoJXRCpj5xMfuekMHrOMhiRHflLpz8xxBJcNb0%2Fj3ZXwu269ysp4VE%2Byj5Qm6rAqfKGE0KjqE%2F77CVPnPxH102qydrErFaLPer4iMuDRUMdyANQPP7PWUhZvAnWkyLP%2F%2FHUHpTYgCC5N1%2BHQpsaHvviTqApIbCu27drzED%2Bu41XKCBM0vMTVAM9uouIoBrR%2FY%2B5B8M6fkhi0XdefgfecK9ShU4KlixSX%2B2J6C9WhC8kxoALFd81UOMbaIuoCEBXUb6%2FOTDc0fC8BjqkAc89vX3%2BesDxu%2F6VIN7Z%2FS2tlozECMbztTqN5yMSRaVrrHFrBjpq2bKWNesN0cHw%2BX7ucUnfJcHy8jv0JWyqmBk%2BPyjUBVcZCMMoKlXTMs4U0s7b88uACWcP1%2B49psO6YzPWHls8mNgwNoIHYUpVDlAJFPwLjFLBgq08FLepx97f1ue0DSIDnhsvVdGu4ZgYm%2B%2FMfiHOjYG9e7k8EQHfWuSBrRAL&X-Amz-Signature=dc79909369d265f5a137c2e768ed84bea4a86bd9845dbc2d714dd30073a308aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4PRSCTA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOjm56ccvyxHlEojq2hQduGLR3PWZd8ACb05oIcVe%2BagIhANzsIUX4vIY0%2BJK8RBhbfkVTPxRJ%2FIq4x6xqHxCIo9MuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDmCTAMfhdyyJnv7sq3AOzygbjLtwzNbYdXPgzMtzR5PD9EfVVtdOK9MR%2FLReXAb5WbEOeNgWHF%2B0Qfbhs0WjQ1nzCLYHU3Z9r8fsQTI77jGPWxhkDV69b8KAPGg6g0vK3%2F%2BXdcysjSGTZbgS5zNw6ylO66DCfTZlgeRJDplFBUuw2IkR797K%2FhlXjErE3YwtuFrgQEXVqLe2Bxc3b%2B9toEHgW9KBXwqhIUJjbRJhPmSs6rCaq4hAqLxAVU9PoJR0b3PlY%2B%2FE75blgeAyfiz%2Bx%2BahqoG1%2F4f%2FJJD5x3ElF4SBePwMbxxPbL%2FiDn%2BuUCRsx7gM6WlQTiHK2GSDYOBxjWDhhegvag8XT7hST4FtK6SP%2BDy%2FZ9PsRTS5fRzwg%2BYf9M0GG4pxJmNoJXRCpj5xMfuekMHrOMhiRHflLpz8xxBJcNb0%2Fj3ZXwu269ysp4VE%2Byj5Qm6rAqfKGE0KjqE%2F77CVPnPxH102qydrErFaLPer4iMuDRUMdyANQPP7PWUhZvAnWkyLP%2F%2FHUHpTYgCC5N1%2BHQpsaHvviTqApIbCu27drzED%2Bu41XKCBM0vMTVAM9uouIoBrR%2FY%2B5B8M6fkhi0XdefgfecK9ShU4KlixSX%2B2J6C9WhC8kxoALFd81UOMbaIuoCEBXUb6%2FOTDc0fC8BjqkAc89vX3%2BesDxu%2F6VIN7Z%2FS2tlozECMbztTqN5yMSRaVrrHFrBjpq2bKWNesN0cHw%2BX7ucUnfJcHy8jv0JWyqmBk%2BPyjUBVcZCMMoKlXTMs4U0s7b88uACWcP1%2B49psO6YzPWHls8mNgwNoIHYUpVDlAJFPwLjFLBgq08FLepx97f1ue0DSIDnhsvVdGu4ZgYm%2B%2FMfiHOjYG9e7k8EQHfWuSBrRAL&X-Amz-Signature=5a16d14e8cb2ce4b7cabfba4eef99ebfbb0f4a24ad5efa4e5ae75145a8858e59&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LIGEVKR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCy9uHZ9ZBQinf%2B1sG2zl1da%2FZyFwzYannjINRpGyHvGAIhAPx1z4Mc2LjWpR5GkwLxLn%2BoDCpxmCKnZUcilWAHKUv7KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRF6vuYsH8f7JZ0HAq3APfANijVd7Qvh9RHlwhbf607mi9ukhbpDc%2Bwyljnmv0kATsvGXOl3B%2FfyWpdQ6hBsvuJSbpHWulgSHwmWY05y5zFQhXM21zVDHzJl2Ervx1umeSlRnDSweAtdQ77qJDsRweq72tAKw9QD%2FGGIsV5diXMlNbmCK4sPKZ8SOl1vjhFS1bWGbiUU%2FjonTaZTnXjv%2BeKTir59NpoKzPF3M3dzyYnl08o0pqFQzrk6e5BXEQg46ssnV25v%2Fz4fBH9ZhHASd4DnJJ0CnCbfkOsbNpETm3etnywtLcirm6wg%2BxBnwpBUX0lQSKzkmAmtD1%2FaqMwYYmIKWMuX2sbytQzwYCIImo460%2BcYsb5KUrMd70yGgsx%2FIlhXZk8b9FoV3psiZOyK2%2Bi%2BdWmusQw%2BPqiitTemZhS2W1pog8DFzJEWIObcPHaRzb%2BO%2B9d3a1jWv%2BP2Hm3htld%2BHBLruR9h4LREnvt5Z9ob8yYso9%2BwsCssfY6gIq%2F0WaJQiBoyIYW4BaMK8W7xEDD5yscQYQZccGq2h5DmxmwDOgIfA2lt%2F8zDPo7vC2vvyYYpdKjW8LvNj9XXZ6hZ0ffppcQOnwFkYBcvYWsO85TROdXUXERV4bk%2FjWVFdoUL%2Br4jrOvxnARsLIKDCI0PC8BjqkAYSiZR6B3fvkLxX%2BYSgpcRejOl3k%2FaOgFHGut6iJHrPmY9qs22I72%2Bj61rv76WA19TK4d4gYBER%2FoC0%2FIos2V3duzkkQBUc%2FFRBC1D%2BWEndH5t6nU7Iq459kiXPmjih%2BbL69vwCa3DSbiVPuUEDj7Aq6Ub4YnKlNVaj%2BC%2F3HfZ0ikIJSg26Z1mc%2FxkGWHNYDZwkzcY7bm03QuwzAO3GSQ%2BefsSNF&X-Amz-Signature=f66991897830cb08ff36beee75dc04442b74377044da63abecd3837a49cb3636&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657SWCM6Z%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwbloJWGPMWJOjjML2FoEY4%2B17PBzOvVS1npGGFrmYMgIgWjyl%2B2X5jtcctcLTN2%2FIMbkSy8C3V681gMc9oxeknfUqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEVpqaN5GP08bRv9oyrcAyoE33VtJLQiJFBOBryxZfAHgnJwMNj7JjUZOGNazqF0E3VNrSYYh6MHnS8vj3KcfvVNKnPqkxb%2FAUvV081bx2zES2ltkyAGh%2BwO52Qd%2BAhgpGzD7zLyFmi%2FzVyMBypp6aEH%2Fvs2wjjpMDIL5jat6ZHmf4FX%2B0N1B9HKUz0NRJf3j4s3H%2FmMt2DbqL8b7djlE3%2Bb5EE34ESBoTZ6tS9byZwVo6Qi1VOdaJA5ortT98FgJaaRthPLLa2hC29GtiWz0Gytb376%2BBXrZMP9H1gAr6ATeWjp4X5rshx0bbTMTvTMQ05%2FjJvG2XhRacp2DY18n49hwjMRszX62zgGC4p2WVTeJRNVMhCCY0Wo1ZebkwdQqkDozJL%2BFl9QdTR%2F1B8Ekysny3weQsZEIN0EeKZkquEJtmygju4gubS1eBDYZdJw9%2Fqde93B7G8qdVdACTDqHp%2F7CEGmyA7FbPAgvHUJiNgB7AeXIdHTsJWk%2FUW9OzhYC2hNsQgY5W7DQD2Ne8gfZrsCLIU2N2WD%2BeDxqNVqdbB5grw1clDHPpeO%2BVJ0z75ZbVKD4lrYnq2FFAQJGjRgmezkL73Zgbh6ag1MqAza0%2BeI%2FgjTbDR%2F%2B84WIOQ3s6BncPBJEcoQhgo4RpoIMIjQ8LwGOqUB5NskvTGibRw043qh8tbmX38XtYhZuN74Pi6O5GfEv0YCvNSEpMBGJP5r3IgvAiQPgVWmL8zoE1UQg%2FO54xftqzN3IkhN0rv70hXIw8M%2FQg3oarIWKLFsL9WKWhsI5OtlBGslfwlRWOOe9pyInmsnVI%2FvdDwvLyc%2BJQrtet%2F9SaD6nKzGWMrdTtnAl2vWa6Ph0Bl%2BoH7HHcPh3KjqLy8HFrQ8hZIB&X-Amz-Signature=6e69d8c7721757a2ca9c36d99826bb59a55e18a0cdfca8bb7228f8ac0e9647e8&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AA5B3DH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCd7bu3hhMNeNkTRj4UxqlWPdA9o1YSnEyJgJ0mo38l%2BQIhAK0ZLJdedzeaOcN6t6go6Mz%2Fvju8P6r0jNqKkp72wnlwKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmMpSJsvh3DkrLxugq3APjaI3N0k6jGJ9GnN3hu9Bc8yVN1swKKPRqfhDRgSg557%2FrvnP%2FHT1S847guQO47EM1Es2yfvaByWZXFyr4V3IgH6y4RVH6isiffZb0Pj%2B997Dx%2BbRN33SNxrrHP9l2y769xsvYgEP4t3SlRmXV%2BVyysoIw3y9XQ69xExTQvUICQNvlBpESn%2FDRDsqcfEVS74IumL0TjCTOoNX5BErFdTLG3zladt84gsE6E38cm8Led3wzmFHdk8HGmWQyJmzsgxpjv1jpHEo8ksR9yrm4MogMc2W76mDx9QHBvSa%2BU0Ov2xrmPTXPN7TIVZmNyCIZXhqwFb1%2F0e57heHf5uexp%2B4oD93UP8Ty1Lqxn0BgBK1Wl4txOXX9zpJN6%2FnvEOPfkGM8OP47T90VePHyWzN7ZHlKIg6OTPPYykE0HkTNK40ZCCgWSBlMCy3gMerV%2BMw7dOQ8HNECOvG1rcJ5bWBHi%2B%2BvuuPw88U7RWQqupEYg3W9pXmO4HRFaYHs6Mhl42woGutcIxbUZ82jmdaVaGdwYItgtaOlplU0PGrzqNbfVIfpuKUQyfT6DHLUuJy%2FFyvsDoLsFJwmmlcojmHjH10mvnGhq5g2zPkpvbhOqnimjOicxUMWKFK6UA1RNCdsZzCu0PC8BjqkAVs744K6xva0qESP41my9GnOIItuQszpC5AfFyHnmz5VG89bymdRgWzFwb18klmlFoXHNSfkd0njpJU8ASRQazt0FYb4BQnpJIrRKV%2BYQBL5LC7%2B85Pzufb8hj6giGvv%2Bbl1weJYrP1Q1i3tfui%2BpmuxWtKA0Wuu69j2AIjvAsR1kkTCfj1myGus5uB2oA98CkG%2F%2BGfjCC%2BwKzhsqUdlI%2Fg1XSwX&X-Amz-Signature=520dee97d0dabbca099c99a3021e7abb83957c866ede3ab1aa5127603a1beb14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STDDVQHV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE67qh%2BRut7EajXbUB%2F2tuoWwHkwAnIq7XIJGch0ZSmtAiBVbwRPwH97B6m0vaXiQJ6E9rxdCQudJol2XJAPjblvSyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZ4PXGAKzVQForUGHKtwDcgzysrKQvct%2Bnd4gsjjAxbT1NQ6iSOj6jWPCDj42TWqVhRj%2BYi0EBAlCVjND5g3zeQxQTCGlSzGYJIAFLZ5N7Mmv8syGyFjFn1aByUx1e5jXm1UbwLqha9f8No2Fbotf4DJlMts3%2FImf7teHCrCHI662KPitrb3NhEr03dEiH%2BTqH53pO6cYB4DMU9RZpc5HFWl1BbO4Sy5HJ4sQ7CxKx%2BFmZdIsQgZZ%2Bcefpo7oEEYUmWPVr0ZC8Y2L5XcZgih%2FoLjsQb4uP6yOcD1uOeoLYdfoUziuWJlYXlo3lNi7ppFIwr0d67otlbJGMzclBXONX4Us67S61%2B8TGtifucSrVV2VJh6hOzEfl2UlJXc3Ike67eDmFVrhc%2FM9Ig4RJ4k16kYnDXYUojIWwLzgdGM3e8KpmUyk%2FfknpOYvu3yOJWWRgY%2BjvzHX3JjoSm9HfI75%2BegCAMf7FzMwSOM8U8sRk%2FTNFlx1DkKhp%2BUTHaIITVCDm27oJ1UF7mNgS%2Fo%2BoX8v%2FBEk8pDwYYtLVoRrS9SJ22n9RmrEq%2BYF4xc7eIRpWcFzb%2Fid6%2B2%2F3Lm1xAPPrcwFF%2F4wOUqKfqW%2FlhtBNt0lVdHtFhEdzGRjEJ79Gi5184cTYkz7KZh%2Fn5HuTlQwqNDwvAY6pgHQhgyDDD2%2BNk44oPnkGEfIBGT24sfQmB2bZYtbFQRkL%2B6wXlXI%2FVLq48OitNvgaBwVkcCEdw2zM%2Fk8qazaaLRTYgu4QZf3rXPOZHuKbafOD1BkkdUfgL9fqxJ0nvsTHPzoo9OqrE0odJ0crcba0OYs6HCUNR0rNedsPgt7ceHe1y86ycFuccGifldb9V%2FihBcy5BNLaDZGHw8pojbGAE1R6YNu9UoV&X-Amz-Signature=b7182255650e451518ef95def7fc4be4b11dd4e1bc3d811b2ad13571245e4cda&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STDDVQHV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE67qh%2BRut7EajXbUB%2F2tuoWwHkwAnIq7XIJGch0ZSmtAiBVbwRPwH97B6m0vaXiQJ6E9rxdCQudJol2XJAPjblvSyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZ4PXGAKzVQForUGHKtwDcgzysrKQvct%2Bnd4gsjjAxbT1NQ6iSOj6jWPCDj42TWqVhRj%2BYi0EBAlCVjND5g3zeQxQTCGlSzGYJIAFLZ5N7Mmv8syGyFjFn1aByUx1e5jXm1UbwLqha9f8No2Fbotf4DJlMts3%2FImf7teHCrCHI662KPitrb3NhEr03dEiH%2BTqH53pO6cYB4DMU9RZpc5HFWl1BbO4Sy5HJ4sQ7CxKx%2BFmZdIsQgZZ%2Bcefpo7oEEYUmWPVr0ZC8Y2L5XcZgih%2FoLjsQb4uP6yOcD1uOeoLYdfoUziuWJlYXlo3lNi7ppFIwr0d67otlbJGMzclBXONX4Us67S61%2B8TGtifucSrVV2VJh6hOzEfl2UlJXc3Ike67eDmFVrhc%2FM9Ig4RJ4k16kYnDXYUojIWwLzgdGM3e8KpmUyk%2FfknpOYvu3yOJWWRgY%2BjvzHX3JjoSm9HfI75%2BegCAMf7FzMwSOM8U8sRk%2FTNFlx1DkKhp%2BUTHaIITVCDm27oJ1UF7mNgS%2Fo%2BoX8v%2FBEk8pDwYYtLVoRrS9SJ22n9RmrEq%2BYF4xc7eIRpWcFzb%2Fid6%2B2%2F3Lm1xAPPrcwFF%2F4wOUqKfqW%2FlhtBNt0lVdHtFhEdzGRjEJ79Gi5184cTYkz7KZh%2Fn5HuTlQwqNDwvAY6pgHQhgyDDD2%2BNk44oPnkGEfIBGT24sfQmB2bZYtbFQRkL%2B6wXlXI%2FVLq48OitNvgaBwVkcCEdw2zM%2Fk8qazaaLRTYgu4QZf3rXPOZHuKbafOD1BkkdUfgL9fqxJ0nvsTHPzoo9OqrE0odJ0crcba0OYs6HCUNR0rNedsPgt7ceHe1y86ycFuccGifldb9V%2FihBcy5BNLaDZGHw8pojbGAE1R6YNu9UoV&X-Amz-Signature=53aa598cea583b00317b1cc91b232feacd728775b0070247fd709383e52bac3b&X-Amz-SignedHeaders=host&x-id=GetObject)

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
