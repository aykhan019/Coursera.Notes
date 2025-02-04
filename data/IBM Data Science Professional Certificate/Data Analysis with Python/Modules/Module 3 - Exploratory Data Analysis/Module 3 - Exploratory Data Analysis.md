

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPL6MM6W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQDgtoz%2FdyV2rx4KjKEwB%2BL2rUr7XeLC4QBTbb1Qhvb%2FlwIgBvDoprh6pUony3xahvSKC1SOkWgVpf3Yj3k51PE21hAq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDBbj%2F6wge4vXjQ1XPSrcA%2FJd%2B%2BKxGQa1bjnlq5FO0O1H1Ms%2BeEQENKIqB1wi2hsudgq%2Byu8ddu02VZ6YRwd0y8yi7kfnvL1EIUpIEGPybMb%2BwouzusWfOfCHa85GjcT8mmRv2qzodyuupikRlXF5Ab%2BTLandt2TgX%2FB%2Fl3J8oVoRVo%2Bz6%2FahHAAev7B8AHPSGad5DhnrqnRogeRnGl6UOfntfCSTGZZ8WnDGm0M0nGV3jkMHgeOyURAwzJLqOgZlObdZoKz9BVKyfMwMQycwzAKixndnSP0QDEIXlffd8j0mmj%2BDZKd1UhguHXpMQRlqnB4xiYwZk9J5t6X0RyaDqZu7CSEvVQtS7gHOhv7vcWN8OgoU2s9zhmyxVp1t8vLvnv7Z6kDKYXjfSY3wsmL7tLgNDtH9fnFWGkMraBFBNDhYuUvIt2OYtUXh9D7%2B9CdeLrCP9i39SNkB6OqiO3wd63K6M4FAFR5l%2F7SOKkDpUCJNjMjs6%2Bjh7h3gdPhoeNbCLN%2BuyIItvB3RE%2BKYBdE%2BauNxoY5ocCbd%2BP8UmMKo7irFvv%2BYYVba7TugZdKUb9ldlQxXy1GXj3uLpEfMWxdyZ%2FnMy5c3w08WzNkzEqNh8L%2Fl%2BBpaII4YZSYymMWPFaVCPSD2ib9FqR207%2FNtML6Fhr0GOqUB12x8oeQ3Dot2BB2HEDiVMfxJ8XNq4Lda%2FLbtHUpJffXE3Qnpsifky%2FpAhr8Y%2Byw1GPHJxWip6SICGYcy5dkWCI15gZOWMZV9qvCs%2F2dLCm0rV7q4BllrUhw9X0MeeBk1Ain%2BYGCDW9Ku5tEwemrrwHFCoMw%2B5ir1Pe0SvTVfvGrzAXONWXecVqgvbBT6ajMTNgUpvZCMxPfG4eQ1GqkRInYbC9iz&X-Amz-Signature=bc1b3ce96aa073480fc7365b355ba4a48e4d9bdf3709cd83b9a85fc9fef8a7d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPL6MM6W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQDgtoz%2FdyV2rx4KjKEwB%2BL2rUr7XeLC4QBTbb1Qhvb%2FlwIgBvDoprh6pUony3xahvSKC1SOkWgVpf3Yj3k51PE21hAq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDBbj%2F6wge4vXjQ1XPSrcA%2FJd%2B%2BKxGQa1bjnlq5FO0O1H1Ms%2BeEQENKIqB1wi2hsudgq%2Byu8ddu02VZ6YRwd0y8yi7kfnvL1EIUpIEGPybMb%2BwouzusWfOfCHa85GjcT8mmRv2qzodyuupikRlXF5Ab%2BTLandt2TgX%2FB%2Fl3J8oVoRVo%2Bz6%2FahHAAev7B8AHPSGad5DhnrqnRogeRnGl6UOfntfCSTGZZ8WnDGm0M0nGV3jkMHgeOyURAwzJLqOgZlObdZoKz9BVKyfMwMQycwzAKixndnSP0QDEIXlffd8j0mmj%2BDZKd1UhguHXpMQRlqnB4xiYwZk9J5t6X0RyaDqZu7CSEvVQtS7gHOhv7vcWN8OgoU2s9zhmyxVp1t8vLvnv7Z6kDKYXjfSY3wsmL7tLgNDtH9fnFWGkMraBFBNDhYuUvIt2OYtUXh9D7%2B9CdeLrCP9i39SNkB6OqiO3wd63K6M4FAFR5l%2F7SOKkDpUCJNjMjs6%2Bjh7h3gdPhoeNbCLN%2BuyIItvB3RE%2BKYBdE%2BauNxoY5ocCbd%2BP8UmMKo7irFvv%2BYYVba7TugZdKUb9ldlQxXy1GXj3uLpEfMWxdyZ%2FnMy5c3w08WzNkzEqNh8L%2Fl%2BBpaII4YZSYymMWPFaVCPSD2ib9FqR207%2FNtML6Fhr0GOqUB12x8oeQ3Dot2BB2HEDiVMfxJ8XNq4Lda%2FLbtHUpJffXE3Qnpsifky%2FpAhr8Y%2Byw1GPHJxWip6SICGYcy5dkWCI15gZOWMZV9qvCs%2F2dLCm0rV7q4BllrUhw9X0MeeBk1Ain%2BYGCDW9Ku5tEwemrrwHFCoMw%2B5ir1Pe0SvTVfvGrzAXONWXecVqgvbBT6ajMTNgUpvZCMxPfG4eQ1GqkRInYbC9iz&X-Amz-Signature=b01cc8beba4fb0f73dfe2e19ad1948b01eb2f3f6e6fb1ec81d74354fbea34e39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPL6MM6W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQDgtoz%2FdyV2rx4KjKEwB%2BL2rUr7XeLC4QBTbb1Qhvb%2FlwIgBvDoprh6pUony3xahvSKC1SOkWgVpf3Yj3k51PE21hAq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDBbj%2F6wge4vXjQ1XPSrcA%2FJd%2B%2BKxGQa1bjnlq5FO0O1H1Ms%2BeEQENKIqB1wi2hsudgq%2Byu8ddu02VZ6YRwd0y8yi7kfnvL1EIUpIEGPybMb%2BwouzusWfOfCHa85GjcT8mmRv2qzodyuupikRlXF5Ab%2BTLandt2TgX%2FB%2Fl3J8oVoRVo%2Bz6%2FahHAAev7B8AHPSGad5DhnrqnRogeRnGl6UOfntfCSTGZZ8WnDGm0M0nGV3jkMHgeOyURAwzJLqOgZlObdZoKz9BVKyfMwMQycwzAKixndnSP0QDEIXlffd8j0mmj%2BDZKd1UhguHXpMQRlqnB4xiYwZk9J5t6X0RyaDqZu7CSEvVQtS7gHOhv7vcWN8OgoU2s9zhmyxVp1t8vLvnv7Z6kDKYXjfSY3wsmL7tLgNDtH9fnFWGkMraBFBNDhYuUvIt2OYtUXh9D7%2B9CdeLrCP9i39SNkB6OqiO3wd63K6M4FAFR5l%2F7SOKkDpUCJNjMjs6%2Bjh7h3gdPhoeNbCLN%2BuyIItvB3RE%2BKYBdE%2BauNxoY5ocCbd%2BP8UmMKo7irFvv%2BYYVba7TugZdKUb9ldlQxXy1GXj3uLpEfMWxdyZ%2FnMy5c3w08WzNkzEqNh8L%2Fl%2BBpaII4YZSYymMWPFaVCPSD2ib9FqR207%2FNtML6Fhr0GOqUB12x8oeQ3Dot2BB2HEDiVMfxJ8XNq4Lda%2FLbtHUpJffXE3Qnpsifky%2FpAhr8Y%2Byw1GPHJxWip6SICGYcy5dkWCI15gZOWMZV9qvCs%2F2dLCm0rV7q4BllrUhw9X0MeeBk1Ain%2BYGCDW9Ku5tEwemrrwHFCoMw%2B5ir1Pe0SvTVfvGrzAXONWXecVqgvbBT6ajMTNgUpvZCMxPfG4eQ1GqkRInYbC9iz&X-Amz-Signature=1df0d81ebe7e0f0ec9b48455f0b6c1527f4459ac505f9306f9351c3981e7f87e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6GDC7H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIFFl6bN1%2BZuujYa88%2FRz7AxKi9Sw88A3VuvU1xIkBGUaAiBnuDk5FNWTEkSzjrSTmzUjrheUvz84O7FmynhqzNfLsir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMXQ9fo7iYSAZNKOqRKtwDebjcYyXcOPeY2iWOlcAueeK9Z%2BwAaioG7JVES00lzdi0QA%2F%2FcsXuj4G1K7VRosJAxIX8KdlFIsJwl3yDuTdEeAI5FMNTCT2vH9G1oSCTl89EWqUA5o8SgcB%2BVve1n2O8B0Hdg%2B9gu6y%2BIQnTN1vW%2B0DmEzN1pZOhWlQxuJ1YAwESkXBUGqBMXAbyjdYtKZOWJtuwEwbs7TERJhpFu%2BmaUS0vJakDHdEd2zYqqNzc1G4PsVgf2XHP7R0ZlC0noRgAXEzc1Kfh4yFMkBqPXDpWJ8gRhlvPAMc%2F70lKXhFfYo8EmTDoCGi%2FwYmlWuHOJVikovKQMBk612GYag%2BH15Z5%2BF%2FU9xMGtvutGEh4b6Jy31Z8Ly12Ch3ULBrrqxBLSb805UBS7q6%2FNUIOY9JvVtdngmp99v1zjTX%2FTh%2BTlki3wWzEwyVMd1MBCX5CVfh5SoZA4O2EOWYv6aQVHhESj7psGYpSXc%2B7I7qC2RLy%2BJv7%2FMhqfXOpvA%2BbrvPzLbTGQ2jlt2YaqDrlgD86wito6PabppMBDvHwyug9ubePkdH0QlHqqCTFknWvDk9NumvTB2zpzbMLWy7pV6dVN4DJxPIYvspf5%2FceVjZ0hCUE4s40ScAe8w2FEBAj6MgoHD8wyoWGvQY6pgH3FnBsBQUKEWwewswr%2BuRMmDA%2Ff7x0U5atPHh6s2%2FYWyeKE9xu9OuoRkOCdfcEAJAM%2FBiSZxoyzGX6JC3%2Fn00FNmZY1dNFS6CIv9StMKg0BMwEekUJcHLHhmMAGCl9DWlrvA4wMk2OHW5ma0faDZLDyi3Po%2FA67bQO14FCy7PzD1mfSD21VsW4Oqm32f38dpX5Cc%2B%2BgX%2BCXkAUI7yHVT661%2B6pGFbB&X-Amz-Signature=651238b1e537d86eea0311db879e7e12cdc7bb0319842e4720ab19ed80f26035&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6GDC7H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIFFl6bN1%2BZuujYa88%2FRz7AxKi9Sw88A3VuvU1xIkBGUaAiBnuDk5FNWTEkSzjrSTmzUjrheUvz84O7FmynhqzNfLsir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMXQ9fo7iYSAZNKOqRKtwDebjcYyXcOPeY2iWOlcAueeK9Z%2BwAaioG7JVES00lzdi0QA%2F%2FcsXuj4G1K7VRosJAxIX8KdlFIsJwl3yDuTdEeAI5FMNTCT2vH9G1oSCTl89EWqUA5o8SgcB%2BVve1n2O8B0Hdg%2B9gu6y%2BIQnTN1vW%2B0DmEzN1pZOhWlQxuJ1YAwESkXBUGqBMXAbyjdYtKZOWJtuwEwbs7TERJhpFu%2BmaUS0vJakDHdEd2zYqqNzc1G4PsVgf2XHP7R0ZlC0noRgAXEzc1Kfh4yFMkBqPXDpWJ8gRhlvPAMc%2F70lKXhFfYo8EmTDoCGi%2FwYmlWuHOJVikovKQMBk612GYag%2BH15Z5%2BF%2FU9xMGtvutGEh4b6Jy31Z8Ly12Ch3ULBrrqxBLSb805UBS7q6%2FNUIOY9JvVtdngmp99v1zjTX%2FTh%2BTlki3wWzEwyVMd1MBCX5CVfh5SoZA4O2EOWYv6aQVHhESj7psGYpSXc%2B7I7qC2RLy%2BJv7%2FMhqfXOpvA%2BbrvPzLbTGQ2jlt2YaqDrlgD86wito6PabppMBDvHwyug9ubePkdH0QlHqqCTFknWvDk9NumvTB2zpzbMLWy7pV6dVN4DJxPIYvspf5%2FceVjZ0hCUE4s40ScAe8w2FEBAj6MgoHD8wyoWGvQY6pgH3FnBsBQUKEWwewswr%2BuRMmDA%2Ff7x0U5atPHh6s2%2FYWyeKE9xu9OuoRkOCdfcEAJAM%2FBiSZxoyzGX6JC3%2Fn00FNmZY1dNFS6CIv9StMKg0BMwEekUJcHLHhmMAGCl9DWlrvA4wMk2OHW5ma0faDZLDyi3Po%2FA67bQO14FCy7PzD1mfSD21VsW4Oqm32f38dpX5Cc%2B%2BgX%2BCXkAUI7yHVT661%2B6pGFbB&X-Amz-Signature=2e57c9b22455685c78018b4061991449593bb9e615fa4e10c5083dfd60bbe7f8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6GDC7H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIFFl6bN1%2BZuujYa88%2FRz7AxKi9Sw88A3VuvU1xIkBGUaAiBnuDk5FNWTEkSzjrSTmzUjrheUvz84O7FmynhqzNfLsir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMXQ9fo7iYSAZNKOqRKtwDebjcYyXcOPeY2iWOlcAueeK9Z%2BwAaioG7JVES00lzdi0QA%2F%2FcsXuj4G1K7VRosJAxIX8KdlFIsJwl3yDuTdEeAI5FMNTCT2vH9G1oSCTl89EWqUA5o8SgcB%2BVve1n2O8B0Hdg%2B9gu6y%2BIQnTN1vW%2B0DmEzN1pZOhWlQxuJ1YAwESkXBUGqBMXAbyjdYtKZOWJtuwEwbs7TERJhpFu%2BmaUS0vJakDHdEd2zYqqNzc1G4PsVgf2XHP7R0ZlC0noRgAXEzc1Kfh4yFMkBqPXDpWJ8gRhlvPAMc%2F70lKXhFfYo8EmTDoCGi%2FwYmlWuHOJVikovKQMBk612GYag%2BH15Z5%2BF%2FU9xMGtvutGEh4b6Jy31Z8Ly12Ch3ULBrrqxBLSb805UBS7q6%2FNUIOY9JvVtdngmp99v1zjTX%2FTh%2BTlki3wWzEwyVMd1MBCX5CVfh5SoZA4O2EOWYv6aQVHhESj7psGYpSXc%2B7I7qC2RLy%2BJv7%2FMhqfXOpvA%2BbrvPzLbTGQ2jlt2YaqDrlgD86wito6PabppMBDvHwyug9ubePkdH0QlHqqCTFknWvDk9NumvTB2zpzbMLWy7pV6dVN4DJxPIYvspf5%2FceVjZ0hCUE4s40ScAe8w2FEBAj6MgoHD8wyoWGvQY6pgH3FnBsBQUKEWwewswr%2BuRMmDA%2Ff7x0U5atPHh6s2%2FYWyeKE9xu9OuoRkOCdfcEAJAM%2FBiSZxoyzGX6JC3%2Fn00FNmZY1dNFS6CIv9StMKg0BMwEekUJcHLHhmMAGCl9DWlrvA4wMk2OHW5ma0faDZLDyi3Po%2FA67bQO14FCy7PzD1mfSD21VsW4Oqm32f38dpX5Cc%2B%2BgX%2BCXkAUI7yHVT661%2B6pGFbB&X-Amz-Signature=f917280a77dee65be94e9925457c056f4602b6ed4b252815c406f9ff937d65fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6GDC7H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIFFl6bN1%2BZuujYa88%2FRz7AxKi9Sw88A3VuvU1xIkBGUaAiBnuDk5FNWTEkSzjrSTmzUjrheUvz84O7FmynhqzNfLsir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMXQ9fo7iYSAZNKOqRKtwDebjcYyXcOPeY2iWOlcAueeK9Z%2BwAaioG7JVES00lzdi0QA%2F%2FcsXuj4G1K7VRosJAxIX8KdlFIsJwl3yDuTdEeAI5FMNTCT2vH9G1oSCTl89EWqUA5o8SgcB%2BVve1n2O8B0Hdg%2B9gu6y%2BIQnTN1vW%2B0DmEzN1pZOhWlQxuJ1YAwESkXBUGqBMXAbyjdYtKZOWJtuwEwbs7TERJhpFu%2BmaUS0vJakDHdEd2zYqqNzc1G4PsVgf2XHP7R0ZlC0noRgAXEzc1Kfh4yFMkBqPXDpWJ8gRhlvPAMc%2F70lKXhFfYo8EmTDoCGi%2FwYmlWuHOJVikovKQMBk612GYag%2BH15Z5%2BF%2FU9xMGtvutGEh4b6Jy31Z8Ly12Ch3ULBrrqxBLSb805UBS7q6%2FNUIOY9JvVtdngmp99v1zjTX%2FTh%2BTlki3wWzEwyVMd1MBCX5CVfh5SoZA4O2EOWYv6aQVHhESj7psGYpSXc%2B7I7qC2RLy%2BJv7%2FMhqfXOpvA%2BbrvPzLbTGQ2jlt2YaqDrlgD86wito6PabppMBDvHwyug9ubePkdH0QlHqqCTFknWvDk9NumvTB2zpzbMLWy7pV6dVN4DJxPIYvspf5%2FceVjZ0hCUE4s40ScAe8w2FEBAj6MgoHD8wyoWGvQY6pgH3FnBsBQUKEWwewswr%2BuRMmDA%2Ff7x0U5atPHh6s2%2FYWyeKE9xu9OuoRkOCdfcEAJAM%2FBiSZxoyzGX6JC3%2Fn00FNmZY1dNFS6CIv9StMKg0BMwEekUJcHLHhmMAGCl9DWlrvA4wMk2OHW5ma0faDZLDyi3Po%2FA67bQO14FCy7PzD1mfSD21VsW4Oqm32f38dpX5Cc%2B%2BgX%2BCXkAUI7yHVT661%2B6pGFbB&X-Amz-Signature=ae6958cd4e91b7cd7e9e66295fe1dd956779bcd79fd3b40c6e37ab928c8ca92c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6GDC7H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIFFl6bN1%2BZuujYa88%2FRz7AxKi9Sw88A3VuvU1xIkBGUaAiBnuDk5FNWTEkSzjrSTmzUjrheUvz84O7FmynhqzNfLsir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMXQ9fo7iYSAZNKOqRKtwDebjcYyXcOPeY2iWOlcAueeK9Z%2BwAaioG7JVES00lzdi0QA%2F%2FcsXuj4G1K7VRosJAxIX8KdlFIsJwl3yDuTdEeAI5FMNTCT2vH9G1oSCTl89EWqUA5o8SgcB%2BVve1n2O8B0Hdg%2B9gu6y%2BIQnTN1vW%2B0DmEzN1pZOhWlQxuJ1YAwESkXBUGqBMXAbyjdYtKZOWJtuwEwbs7TERJhpFu%2BmaUS0vJakDHdEd2zYqqNzc1G4PsVgf2XHP7R0ZlC0noRgAXEzc1Kfh4yFMkBqPXDpWJ8gRhlvPAMc%2F70lKXhFfYo8EmTDoCGi%2FwYmlWuHOJVikovKQMBk612GYag%2BH15Z5%2BF%2FU9xMGtvutGEh4b6Jy31Z8Ly12Ch3ULBrrqxBLSb805UBS7q6%2FNUIOY9JvVtdngmp99v1zjTX%2FTh%2BTlki3wWzEwyVMd1MBCX5CVfh5SoZA4O2EOWYv6aQVHhESj7psGYpSXc%2B7I7qC2RLy%2BJv7%2FMhqfXOpvA%2BbrvPzLbTGQ2jlt2YaqDrlgD86wito6PabppMBDvHwyug9ubePkdH0QlHqqCTFknWvDk9NumvTB2zpzbMLWy7pV6dVN4DJxPIYvspf5%2FceVjZ0hCUE4s40ScAe8w2FEBAj6MgoHD8wyoWGvQY6pgH3FnBsBQUKEWwewswr%2BuRMmDA%2Ff7x0U5atPHh6s2%2FYWyeKE9xu9OuoRkOCdfcEAJAM%2FBiSZxoyzGX6JC3%2Fn00FNmZY1dNFS6CIv9StMKg0BMwEekUJcHLHhmMAGCl9DWlrvA4wMk2OHW5ma0faDZLDyi3Po%2FA67bQO14FCy7PzD1mfSD21VsW4Oqm32f38dpX5Cc%2B%2BgX%2BCXkAUI7yHVT661%2B6pGFbB&X-Amz-Signature=e9bfd773c27f67efa9875c72d80b0875c3d8b87fb33919640309f53b9f45b714&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6GDC7H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIFFl6bN1%2BZuujYa88%2FRz7AxKi9Sw88A3VuvU1xIkBGUaAiBnuDk5FNWTEkSzjrSTmzUjrheUvz84O7FmynhqzNfLsir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMXQ9fo7iYSAZNKOqRKtwDebjcYyXcOPeY2iWOlcAueeK9Z%2BwAaioG7JVES00lzdi0QA%2F%2FcsXuj4G1K7VRosJAxIX8KdlFIsJwl3yDuTdEeAI5FMNTCT2vH9G1oSCTl89EWqUA5o8SgcB%2BVve1n2O8B0Hdg%2B9gu6y%2BIQnTN1vW%2B0DmEzN1pZOhWlQxuJ1YAwESkXBUGqBMXAbyjdYtKZOWJtuwEwbs7TERJhpFu%2BmaUS0vJakDHdEd2zYqqNzc1G4PsVgf2XHP7R0ZlC0noRgAXEzc1Kfh4yFMkBqPXDpWJ8gRhlvPAMc%2F70lKXhFfYo8EmTDoCGi%2FwYmlWuHOJVikovKQMBk612GYag%2BH15Z5%2BF%2FU9xMGtvutGEh4b6Jy31Z8Ly12Ch3ULBrrqxBLSb805UBS7q6%2FNUIOY9JvVtdngmp99v1zjTX%2FTh%2BTlki3wWzEwyVMd1MBCX5CVfh5SoZA4O2EOWYv6aQVHhESj7psGYpSXc%2B7I7qC2RLy%2BJv7%2FMhqfXOpvA%2BbrvPzLbTGQ2jlt2YaqDrlgD86wito6PabppMBDvHwyug9ubePkdH0QlHqqCTFknWvDk9NumvTB2zpzbMLWy7pV6dVN4DJxPIYvspf5%2FceVjZ0hCUE4s40ScAe8w2FEBAj6MgoHD8wyoWGvQY6pgH3FnBsBQUKEWwewswr%2BuRMmDA%2Ff7x0U5atPHh6s2%2FYWyeKE9xu9OuoRkOCdfcEAJAM%2FBiSZxoyzGX6JC3%2Fn00FNmZY1dNFS6CIv9StMKg0BMwEekUJcHLHhmMAGCl9DWlrvA4wMk2OHW5ma0faDZLDyi3Po%2FA67bQO14FCy7PzD1mfSD21VsW4Oqm32f38dpX5Cc%2B%2BgX%2BCXkAUI7yHVT661%2B6pGFbB&X-Amz-Signature=768e75882b517b6b080b21ca5d5888eca623db3614eff47955bc4731797676a7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPL6MM6W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQDgtoz%2FdyV2rx4KjKEwB%2BL2rUr7XeLC4QBTbb1Qhvb%2FlwIgBvDoprh6pUony3xahvSKC1SOkWgVpf3Yj3k51PE21hAq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDBbj%2F6wge4vXjQ1XPSrcA%2FJd%2B%2BKxGQa1bjnlq5FO0O1H1Ms%2BeEQENKIqB1wi2hsudgq%2Byu8ddu02VZ6YRwd0y8yi7kfnvL1EIUpIEGPybMb%2BwouzusWfOfCHa85GjcT8mmRv2qzodyuupikRlXF5Ab%2BTLandt2TgX%2FB%2Fl3J8oVoRVo%2Bz6%2FahHAAev7B8AHPSGad5DhnrqnRogeRnGl6UOfntfCSTGZZ8WnDGm0M0nGV3jkMHgeOyURAwzJLqOgZlObdZoKz9BVKyfMwMQycwzAKixndnSP0QDEIXlffd8j0mmj%2BDZKd1UhguHXpMQRlqnB4xiYwZk9J5t6X0RyaDqZu7CSEvVQtS7gHOhv7vcWN8OgoU2s9zhmyxVp1t8vLvnv7Z6kDKYXjfSY3wsmL7tLgNDtH9fnFWGkMraBFBNDhYuUvIt2OYtUXh9D7%2B9CdeLrCP9i39SNkB6OqiO3wd63K6M4FAFR5l%2F7SOKkDpUCJNjMjs6%2Bjh7h3gdPhoeNbCLN%2BuyIItvB3RE%2BKYBdE%2BauNxoY5ocCbd%2BP8UmMKo7irFvv%2BYYVba7TugZdKUb9ldlQxXy1GXj3uLpEfMWxdyZ%2FnMy5c3w08WzNkzEqNh8L%2Fl%2BBpaII4YZSYymMWPFaVCPSD2ib9FqR207%2FNtML6Fhr0GOqUB12x8oeQ3Dot2BB2HEDiVMfxJ8XNq4Lda%2FLbtHUpJffXE3Qnpsifky%2FpAhr8Y%2Byw1GPHJxWip6SICGYcy5dkWCI15gZOWMZV9qvCs%2F2dLCm0rV7q4BllrUhw9X0MeeBk1Ain%2BYGCDW9Ku5tEwemrrwHFCoMw%2B5ir1Pe0SvTVfvGrzAXONWXecVqgvbBT6ajMTNgUpvZCMxPfG4eQ1GqkRInYbC9iz&X-Amz-Signature=9a67205e58ad2a6016faf094412ab2612cdcce337d3c2d9d461c55aec33eab79&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVOUQ5P6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIAimlC%2BO6LZPdzHZiPkcDrOShEILbKFW0Fc1MAROttZHAiEAiMNO0p2qEXzDjPxU4rPK%2BtASZS4t0OoWjpKQMLJN%2FXsq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDOxEdiLVJSU%2FBuzAnircA%2Bc11SYdKuq44rCT6qYES6RctQf%2FBbPkJFzgOL1auyVAUyAcGyY6vOT9zb50pd0QPf5FTqET2MXlISL4wPxPOpJUEM9B5jrwaB3ZONu28TaTD%2F3RtOqXQAMkzO%2BzLAV4sh6JcHxVaDXcd1nWWgVGwgPUJurTNodqD84eZqDGfZUrqRSVxlVijcE0hFv5XuXmvTs5BvMiJevA6MDzrYaumHtJxlLdQiuysmVLIjQVwRbhx6hQu472cCiX7hEPmVPolUI2x%2B2VHQjGu044iHF7fFt%2BNsaZvP%2BS8eGV6CIICDRkrNGRF3YibNwGaWbQEHjm5RTcHYCiJAvNjy5P%2FtEBNiKGjb%2B3qAhcOAZg2Sg1eoEEDqzRKDMomPcZGGRKfMMNs7CHT7LojzWyDfmlBx7evaxFqvfuBAAeW1m4G6%2Bj20kjH9OT2fFMHUfe6mUirLJ4CDmHgXwHwO5NPq%2F2FMxLanI0jTvM%2BAb4wqoq9cDPA4oiVv4CsZLKKNhD3VtdJuwENL4%2BP9CDcNYhm9gA878CKjblBmJIgXeNlHIwJOrIf1Yh1r15dWfHoKZu6mNq0u%2BR%2BHRbKOR8OWwcg6Ab65iTtoxaw%2By0dAWcgmuIYMLriVCC2Ustig03p5vLq3rPMOuEhr0GOqUB9cCf0o9NMby84jS0a%2BvKJae%2BfydRVoQgI7KT1yPl7otJ1SkxV7ms3I5SheP%2BSmH6RFz1ysv6r26csEOAlQH1tL1L067UWo%2Bj4FNfu1hhHDOkkCy7s%2Fpqei%2FC1xA4n6yHDGUSWMrN3YX7uk4cOozK0lSSZESu33GvglN9ujn0%2FYyFb%2FsC8BHvi8MP57kAE9huL98ZowM3ivZKgUSjNm64CBNk4l1%2B&X-Amz-Signature=ac8427f91737a36b696cfdc345004aa15e5df31bb5ab9e5385dc814960f96c83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6GDC7H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIFFl6bN1%2BZuujYa88%2FRz7AxKi9Sw88A3VuvU1xIkBGUaAiBnuDk5FNWTEkSzjrSTmzUjrheUvz84O7FmynhqzNfLsir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMXQ9fo7iYSAZNKOqRKtwDebjcYyXcOPeY2iWOlcAueeK9Z%2BwAaioG7JVES00lzdi0QA%2F%2FcsXuj4G1K7VRosJAxIX8KdlFIsJwl3yDuTdEeAI5FMNTCT2vH9G1oSCTl89EWqUA5o8SgcB%2BVve1n2O8B0Hdg%2B9gu6y%2BIQnTN1vW%2B0DmEzN1pZOhWlQxuJ1YAwESkXBUGqBMXAbyjdYtKZOWJtuwEwbs7TERJhpFu%2BmaUS0vJakDHdEd2zYqqNzc1G4PsVgf2XHP7R0ZlC0noRgAXEzc1Kfh4yFMkBqPXDpWJ8gRhlvPAMc%2F70lKXhFfYo8EmTDoCGi%2FwYmlWuHOJVikovKQMBk612GYag%2BH15Z5%2BF%2FU9xMGtvutGEh4b6Jy31Z8Ly12Ch3ULBrrqxBLSb805UBS7q6%2FNUIOY9JvVtdngmp99v1zjTX%2FTh%2BTlki3wWzEwyVMd1MBCX5CVfh5SoZA4O2EOWYv6aQVHhESj7psGYpSXc%2B7I7qC2RLy%2BJv7%2FMhqfXOpvA%2BbrvPzLbTGQ2jlt2YaqDrlgD86wito6PabppMBDvHwyug9ubePkdH0QlHqqCTFknWvDk9NumvTB2zpzbMLWy7pV6dVN4DJxPIYvspf5%2FceVjZ0hCUE4s40ScAe8w2FEBAj6MgoHD8wyoWGvQY6pgH3FnBsBQUKEWwewswr%2BuRMmDA%2Ff7x0U5atPHh6s2%2FYWyeKE9xu9OuoRkOCdfcEAJAM%2FBiSZxoyzGX6JC3%2Fn00FNmZY1dNFS6CIv9StMKg0BMwEekUJcHLHhmMAGCl9DWlrvA4wMk2OHW5ma0faDZLDyi3Po%2FA67bQO14FCy7PzD1mfSD21VsW4Oqm32f38dpX5Cc%2B%2BgX%2BCXkAUI7yHVT661%2B6pGFbB&X-Amz-Signature=0e8049605a754f492ad5757382cb087e70b7793cbb3cda89d22e92ce173a91db&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6GDC7H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIFFl6bN1%2BZuujYa88%2FRz7AxKi9Sw88A3VuvU1xIkBGUaAiBnuDk5FNWTEkSzjrSTmzUjrheUvz84O7FmynhqzNfLsir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMXQ9fo7iYSAZNKOqRKtwDebjcYyXcOPeY2iWOlcAueeK9Z%2BwAaioG7JVES00lzdi0QA%2F%2FcsXuj4G1K7VRosJAxIX8KdlFIsJwl3yDuTdEeAI5FMNTCT2vH9G1oSCTl89EWqUA5o8SgcB%2BVve1n2O8B0Hdg%2B9gu6y%2BIQnTN1vW%2B0DmEzN1pZOhWlQxuJ1YAwESkXBUGqBMXAbyjdYtKZOWJtuwEwbs7TERJhpFu%2BmaUS0vJakDHdEd2zYqqNzc1G4PsVgf2XHP7R0ZlC0noRgAXEzc1Kfh4yFMkBqPXDpWJ8gRhlvPAMc%2F70lKXhFfYo8EmTDoCGi%2FwYmlWuHOJVikovKQMBk612GYag%2BH15Z5%2BF%2FU9xMGtvutGEh4b6Jy31Z8Ly12Ch3ULBrrqxBLSb805UBS7q6%2FNUIOY9JvVtdngmp99v1zjTX%2FTh%2BTlki3wWzEwyVMd1MBCX5CVfh5SoZA4O2EOWYv6aQVHhESj7psGYpSXc%2B7I7qC2RLy%2BJv7%2FMhqfXOpvA%2BbrvPzLbTGQ2jlt2YaqDrlgD86wito6PabppMBDvHwyug9ubePkdH0QlHqqCTFknWvDk9NumvTB2zpzbMLWy7pV6dVN4DJxPIYvspf5%2FceVjZ0hCUE4s40ScAe8w2FEBAj6MgoHD8wyoWGvQY6pgH3FnBsBQUKEWwewswr%2BuRMmDA%2Ff7x0U5atPHh6s2%2FYWyeKE9xu9OuoRkOCdfcEAJAM%2FBiSZxoyzGX6JC3%2Fn00FNmZY1dNFS6CIv9StMKg0BMwEekUJcHLHhmMAGCl9DWlrvA4wMk2OHW5ma0faDZLDyi3Po%2FA67bQO14FCy7PzD1mfSD21VsW4Oqm32f38dpX5Cc%2B%2BgX%2BCXkAUI7yHVT661%2B6pGFbB&X-Amz-Signature=151f3e4d3b217889ab980acef62e64d4e77715445038a054d4bdb3364b275743&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6GDC7H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIFFl6bN1%2BZuujYa88%2FRz7AxKi9Sw88A3VuvU1xIkBGUaAiBnuDk5FNWTEkSzjrSTmzUjrheUvz84O7FmynhqzNfLsir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMXQ9fo7iYSAZNKOqRKtwDebjcYyXcOPeY2iWOlcAueeK9Z%2BwAaioG7JVES00lzdi0QA%2F%2FcsXuj4G1K7VRosJAxIX8KdlFIsJwl3yDuTdEeAI5FMNTCT2vH9G1oSCTl89EWqUA5o8SgcB%2BVve1n2O8B0Hdg%2B9gu6y%2BIQnTN1vW%2B0DmEzN1pZOhWlQxuJ1YAwESkXBUGqBMXAbyjdYtKZOWJtuwEwbs7TERJhpFu%2BmaUS0vJakDHdEd2zYqqNzc1G4PsVgf2XHP7R0ZlC0noRgAXEzc1Kfh4yFMkBqPXDpWJ8gRhlvPAMc%2F70lKXhFfYo8EmTDoCGi%2FwYmlWuHOJVikovKQMBk612GYag%2BH15Z5%2BF%2FU9xMGtvutGEh4b6Jy31Z8Ly12Ch3ULBrrqxBLSb805UBS7q6%2FNUIOY9JvVtdngmp99v1zjTX%2FTh%2BTlki3wWzEwyVMd1MBCX5CVfh5SoZA4O2EOWYv6aQVHhESj7psGYpSXc%2B7I7qC2RLy%2BJv7%2FMhqfXOpvA%2BbrvPzLbTGQ2jlt2YaqDrlgD86wito6PabppMBDvHwyug9ubePkdH0QlHqqCTFknWvDk9NumvTB2zpzbMLWy7pV6dVN4DJxPIYvspf5%2FceVjZ0hCUE4s40ScAe8w2FEBAj6MgoHD8wyoWGvQY6pgH3FnBsBQUKEWwewswr%2BuRMmDA%2Ff7x0U5atPHh6s2%2FYWyeKE9xu9OuoRkOCdfcEAJAM%2FBiSZxoyzGX6JC3%2Fn00FNmZY1dNFS6CIv9StMKg0BMwEekUJcHLHhmMAGCl9DWlrvA4wMk2OHW5ma0faDZLDyi3Po%2FA67bQO14FCy7PzD1mfSD21VsW4Oqm32f38dpX5Cc%2B%2BgX%2BCXkAUI7yHVT661%2B6pGFbB&X-Amz-Signature=640db85328ba2d370397bfca8b93bf788236247c2e628cd6c6f3b773717ff393&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TH6GZ4EB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIBv2RUl8kubwZxSX2WYrFdaF9NcGZoOKDvs%2FsZkheWxeAiBQCfiqAuODsuoNiEmiyScvuTb1Vjot%2B%2FGCNw9zsGKfdyr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMSz7byG9B6kw1%2FGyAKtwDKpo8XFAUaDPG8TrIoS3UmM1xY8nAZSiZWszvIvfS4J8HLRRALi%2FvdxWzUaUhaVDAs2YgPdPY24pAi5bNLv6e4C3rLcr6hQFbUK5Oa9XmOb7MRihvsF9slLrFFsTG2DI%2FNOj9i3WDbFvKAahQ8OltQ%2BbXcli4LWYvjyzLAScQMIEYpEK%2F7d1uGrpYEDlBYf4pjJnFlaQzEJ2NOg27%2FpQw8qzi2VDt4ULMaukDhj1%2FguE72taGDDrCAZ5w%2Fr6agIxHf7UkF7Afe9UIOzvn1zS1oHBesUEVe%2FGnEg711gZ8vDcclR5h%2FPO272nr4AxBdYLu%2FYGv%2FNSAZDpf%2F8QPbgLkYFiV7iTb%2FpgCylCcQLvMmiUubVsygSC66gpVYhGoKUfm8AA9Qe%2BTh2mWMOJz3HeHbsMVFa53GrT2H1BlTXNKIDSU7gcvEPkTDgB87W0vX%2Bvi7lCINEIE8BTsmT%2B3Lq2Nf4eLcLrv7xhADKxtOn%2Fgxxc3fHdkUzulpcAxs%2BRpfCgdGHlEMGXdN2lZTW5ULi7Z690WC48Z3dmjmZXnnbYqIGGReyM7bejygpzGCad06TeB2HasfXql6vvrP91bn08yCCqBhKUeoOS0dnLFlUDVVZYWX0eJA9Q4HAyIr4gwloWGvQY6pgHuTgAqZ1QSAogbmCZ85%2B8q6FHkETdnFOSt%2FGlPWq1QmdQAukCzCvamQTU%2F5GfKOTCM9tEaxIVO1yaA5ElYrauOwzUqkYJ4fRJNJSrqHveHaCMfwqGfrTV76spBi%2BVjK7Pg8YSmVH2QTnBGL8PuyjZIxTimLpGsokRc7S9rBzyXaBiX%2FHTsnpr65jwUxMgCFjV5qRoGMPrFKO%2FbV2azMLWbHWxo3jRG&X-Amz-Signature=d11074397ba7b1d6d0fadcf872780b909e51e8521b42dd96d67a5992099571d0&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZV7VU2KI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIBUxiA%2FzzPX2jTxL3l8OW1RnNsB%2FZirFYuqZIhdSsYRhAiB0lkK4KfM7y%2FNsG67aWbVi9BMnNZZRgWKqf7OOMk6S0ir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMI5dTXdX7M3IC4%2F78KtwDpnGwIyA7UxvcdpAukyKS1CDVRAhPmqujQEKKDdx6i9Cu3xLFkSV8rZ1gV8tzpbHi5bKb%2BPUk8vghiadaBYdYTqx51T0AwN69A%2FMyOR4nS8eNbPS28pDVHcLTV0jzEG8CdTEcefLRQvh73OtHBp2r7OphAdN0qnUF7gqedjIaTYE4QV9DorJ1el8Pc1ZHTFs8aErhUcCR74yTHVDSEjWxqMASnAJWiSWzNwVrybj85Rd1RvXRMo%2B5jakweL6jUfeFF35DEACAFNlXVM8pKGzSMip4qGW6b6LRDG7i9SvIemyrnSm4FjYLMF%2Fz5R85VSTxxPj%2F81%2BwO%2FcTZs7Jw23kuSpYllfht6GKGn6Qtfmi2oXjou8CBqeXzZY7ZYoRmcAmDe57O%2BenW20I7zJI3VSe0zEvL8hgvQUN9D%2F%2FRHXrGf2VgRMZShmHBzy%2Fv3AHySFE1%2BPkzKTS4BLIken1yHOHjrQSTJDsTiOchZV%2B0TIftSvfX9S1NSPsfwDJEZtZXmYMc5uV0dLB%2B%2F6O8HSzorF51TsyPTSSA6jjHT4ppHiPVZHxNtUCQ2BFvXOVt5hD1HmUZdRdZh2v%2Fiuhq%2F%2FhEwKxRtx9FEPHi5cgbYgbuRAVkBiK4bhXF6aAKU9cGtIwlIWGvQY6pgEK2qC%2FMMsEj04WScaHo6y5YD4sCkCiYjNIBhBNhcC2OpOl873yFvO47lYlw9k4JW1eBu%2BIwAjcTeFeu000jvYsaGk9u0oTHhj5XYBOjuG8%2BQ810uWuY%2BL1in57lBDIvgjqq4gKjVWwknGfHSDMQ7HsfSQVviHcnNRwJwIZW%2FF4lFqBZvWKtIeuOnakiiN678dK9eNKgDBKSmsb6qBH4kGffhzK1ytU&X-Amz-Signature=81b9c6dd8d4e89487ba60279c9813bc0a05be52c5de8fcf02d56b819a48753c6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCRYXDBN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQCOSMRQJgszLWyt8AwtS4zJ4WlFlLVJIA1sDTz%2FFqRkVQIgYuXXa3kYq%2B7K7lMz5rlOiMT9wOLPBxXW1IfB3sJ9QFwq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDHRznIQWG1WDXFSGtCrcAyuSv3ua2genH0hXSJTYlqIa7ZnB4nZg7slzUkBbkqysMxS3%2Fe2qNPs4InyKN6gbrqjrm48EJ6%2B0dHG3Rg1iFmP45XkzJqzb%2ByUfn0DrADeGwTNMVl3qJO8OkaQUWBC8hao5owN0RGEfDkyFfvZAuDObFpCYm6DULPRSgzdjb%2FEqfeRCKkDsLQ7rRfRMIFypEjgj%2Bk9nfIn35bGmbHVTUGinwZO0fTtn%2BuwO3v6p6Dsico%2Br%2BcqvTVuz4uXHian%2FUxGPjeTft%2BoklDBCTF9DWa%2FcHg7xmuELv%2BBpyxaqbSAf%2F94MD3eKauxRieQLLgYOKFj5%2FNROMCUsAeI2s6G%2BBUqWOajY0J2ZjBduMRBvZa5r899FB7ynGiovhalGo6HvOy%2B%2FeJ5MRf%2FC3AWfjyqCZ4QPZ3HhZiur0ubS7Qu%2B9IEPoopSXpzwWcVY8VDz9Gy33%2Bnpaghn79z5rJ%2BpiHblWtFJ9q47zJ1T4to14LKEygdjSQlURi9PA3hXGuIoA6VxVUkdZhdpXM8Q1eVnu8ezXO7bXOAyWDZqyc4%2Br7vONtC%2B2SDL1Qjp5%2Bs409x2de9Wos4DMA%2FMsrPVuT8ZiGGNkNOIon%2BViUGKJ6UOmfy18OjZ66Am2bXUQrHmMdFDMImFhr0GOqUB13izAZAKWMQflEiCRA9qS16j2GFCARFAxm0ZgA%2Br7r5MdOJLkth6oLxyQXnA4b5h4kCSJmJz1RxdfADSbOhXopLPmF4HvGnGJ8xb50WR3CQgztZQqwKPjMp8prd22cWhadRI6xfxqU%2FJ7iAlYDjH5lysyskAOPUmHqecpns61xVeCwdLygQThTmvKlyQZiLRmLJeTVgzzX28yejmiabTz5yUIKlF&X-Amz-Signature=aa75d52caf6bb688f6e49417a460553ca23359d4f359a0d5aad7c530965f01f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664G3DMT4Y%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQCN2jL7nq1wdejLYKjTHdHsfjicNQMD9BO%2B1t%2B77rad8gIgFQ4LERG3k9u4uiaUnzxib%2F1sMxUMiFhMJ2t4kncNZyAq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDPQ7dq059%2BZrue9PjircA0Y8HWNhzC5Sn1hYTxKDwLktUOAX7NSpN41b8rwjR2C%2BnLDprZLnnkL2AhP5HeQv1pgd8ElRo23qtEM4nzrDOUbqo5dJBR66%2BWJBAWOBVDw0%2FswNUmsrtoFQ4WJei%2FqdF4zTl%2FR2A65QUSJpoyNlxb1ZgmgyhfUMmmT%2BchOS18NCyMtQwRS30KteDTjIpf7mlcmoZZfcHU4v1C30y3kP09oPPPROO5mjHDHsyA4dJxT9ClP8VabR3DfVkeawq8cu1uolxY%2FM8GhEsK2zK%2BjMVSdJOMedIDqhh8nLflhUWro9YJ77QgH0c3OvEJfR4qlVAlkq5QHdyLRHmkRlyo7lrybJKmk0CUYdDLIZqillGJ31HaFX8BY8e2HcGPaC7X53aW2aMtqD0pug4BXJB5T9wdIbApRO1dwKYtawB%2B%2Bofbh3StM2rII4g2kfCYzCntKAudur%2BSy%2B2vC%2FaLuJh7%2Fii1%2FuuSVj7ulTyRK1gIzQID8Q4gJ1uMJMCIrdh43rL9sMSA%2B0VJVR33alrr3TrjHgBMAIU5dc1QFe982LMF80nMwepCVBm%2F2aBZvBWsXM%2BEb%2B98qTVnpMSCHzPJIxXY03dUriUPVfuU0Jmw94zIXgFkXptlKRXSlmqAewXrTYMKCFhr0GOqUBKv6nw6FAsEY43Ribbgol%2FWbIASZS2oeHGCnBQL%2BCbcitpIqbovmoZIby5i5tGJttlqx%2FhrIdcgXxLy%2FvQvwz5V5L7nFBaPlQszVJXd0ipV1qkDRKv1MwQrw2n2bA%2FlW%2FTEPKX2OoFNcdwJ2jUYz7BiUnCMZYj4RRQC19lhe2MLgK2zoSN5cK%2BQkW17cwSOut67XwOGy33eLPn2g%2B1Y4bUmAWRB1m&X-Amz-Signature=11d18f09ce2600d56114b491e51f34f54a74a3c8cb05505d0302dfdb4bd9dd52&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664G3DMT4Y%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQCN2jL7nq1wdejLYKjTHdHsfjicNQMD9BO%2B1t%2B77rad8gIgFQ4LERG3k9u4uiaUnzxib%2F1sMxUMiFhMJ2t4kncNZyAq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDPQ7dq059%2BZrue9PjircA0Y8HWNhzC5Sn1hYTxKDwLktUOAX7NSpN41b8rwjR2C%2BnLDprZLnnkL2AhP5HeQv1pgd8ElRo23qtEM4nzrDOUbqo5dJBR66%2BWJBAWOBVDw0%2FswNUmsrtoFQ4WJei%2FqdF4zTl%2FR2A65QUSJpoyNlxb1ZgmgyhfUMmmT%2BchOS18NCyMtQwRS30KteDTjIpf7mlcmoZZfcHU4v1C30y3kP09oPPPROO5mjHDHsyA4dJxT9ClP8VabR3DfVkeawq8cu1uolxY%2FM8GhEsK2zK%2BjMVSdJOMedIDqhh8nLflhUWro9YJ77QgH0c3OvEJfR4qlVAlkq5QHdyLRHmkRlyo7lrybJKmk0CUYdDLIZqillGJ31HaFX8BY8e2HcGPaC7X53aW2aMtqD0pug4BXJB5T9wdIbApRO1dwKYtawB%2B%2Bofbh3StM2rII4g2kfCYzCntKAudur%2BSy%2B2vC%2FaLuJh7%2Fii1%2FuuSVj7ulTyRK1gIzQID8Q4gJ1uMJMCIrdh43rL9sMSA%2B0VJVR33alrr3TrjHgBMAIU5dc1QFe982LMF80nMwepCVBm%2F2aBZvBWsXM%2BEb%2B98qTVnpMSCHzPJIxXY03dUriUPVfuU0Jmw94zIXgFkXptlKRXSlmqAewXrTYMKCFhr0GOqUBKv6nw6FAsEY43Ribbgol%2FWbIASZS2oeHGCnBQL%2BCbcitpIqbovmoZIby5i5tGJttlqx%2FhrIdcgXxLy%2FvQvwz5V5L7nFBaPlQszVJXd0ipV1qkDRKv1MwQrw2n2bA%2FlW%2FTEPKX2OoFNcdwJ2jUYz7BiUnCMZYj4RRQC19lhe2MLgK2zoSN5cK%2BQkW17cwSOut67XwOGy33eLPn2g%2B1Y4bUmAWRB1m&X-Amz-Signature=d0f48f7504dea658c84b0a4c2dd45b9bad7db0d379f0fb5a583d3bc84af58cd9&X-Amz-SignedHeaders=host&x-id=GetObject)

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
