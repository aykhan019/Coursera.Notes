

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LBGKDSG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIFZ%2FYWp9WdClec46v%2BkGBEemil0zD452Zp1wSLrf7SgsAiBwT8NX%2FlnaVo64Gm0ETCuJP1zd2whKR2zncJlnR5mtiir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMBZ4mUax262xuYub%2BKtwDCqqCfQgwnQ9JgphtFinCGfhUxshEKAmr4t5bg56aJS5y377nqBggVMFf5Zloag1mGjqV0IEVjrjwSbiFNGyaofdkhu0%2Bv1E41Ea0L9NFwWg7aOY1OtIUg6LukXGaec1uuvetI5QP0nDn4nNdRJxM8jzBmjfkvW1sEbEEITQjdA5BLRxhKAUMbMHZDclaWFkbQSHKrFeoatOnYRNJCm1op2YVLwEq4q%2B34%2BYpHEXjmrr%2FrFDZgGdpxBIt5xFqbmPb5Y0S1LWpOf5JwuYD6HuhaLn3pg1dz%2BJujeyUf3dvqxsBlkasTezOEZ8RHUv2aHWhuuAzd2ZJSzgq6ck4mFUap94aLTSJCC7sLmn%2Fk1yadyTEsJMWQUJE9Fy5wI9C5tR9IpsYBHwOrMKdmQd9x6dPF1EdiJxRSIfnNgtnfgWFJ6CCR025JXkmiZ1Q7pfgsrJx10CeqhMbZIdD0uuUK9mGldIrbNsQgQBj49HcR48JSsulnTI8a2%2B2IdeRDUrf0egUAONuCza8j59aauRKo6vh6j72%2FNaIo09d45FridlFQIt%2FkyeNoTGC1rb7hnO9vYmPM4Xp3zbpj0xNuL6YmDmQSnDb2Y8rlIRj%2F%2Bt7%2BkTrUqcR7FYnbEYEbfdnOWQw6OeIvQY6pgEdPG%2BOybmxFSB%2BMxoZDjOT84GcT0fJ0%2BLHGvvm%2F%2Bo2yKW9TxQix8eRIkoDw60AtW1eF5kcJXHySQT%2FHilAkVlKdYMhBgi1SRnlky3QxuQ7I%2B24FdfMBymIXscyTyiZGtts2EcQ0AACmx2BBJq9bYddHuCisgVld1xM%2BrzURg%2B%2BLq2hztHlaKNR4%2F7%2BfTQltJiGSaxMdW5BuDW9Rf35p%2BRZkpM5rJvI&X-Amz-Signature=c7b6087f1e75f2ef3032d2800793bd99c0ac8be69c8a3e5c66dcd31c586aac3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LBGKDSG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIFZ%2FYWp9WdClec46v%2BkGBEemil0zD452Zp1wSLrf7SgsAiBwT8NX%2FlnaVo64Gm0ETCuJP1zd2whKR2zncJlnR5mtiir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMBZ4mUax262xuYub%2BKtwDCqqCfQgwnQ9JgphtFinCGfhUxshEKAmr4t5bg56aJS5y377nqBggVMFf5Zloag1mGjqV0IEVjrjwSbiFNGyaofdkhu0%2Bv1E41Ea0L9NFwWg7aOY1OtIUg6LukXGaec1uuvetI5QP0nDn4nNdRJxM8jzBmjfkvW1sEbEEITQjdA5BLRxhKAUMbMHZDclaWFkbQSHKrFeoatOnYRNJCm1op2YVLwEq4q%2B34%2BYpHEXjmrr%2FrFDZgGdpxBIt5xFqbmPb5Y0S1LWpOf5JwuYD6HuhaLn3pg1dz%2BJujeyUf3dvqxsBlkasTezOEZ8RHUv2aHWhuuAzd2ZJSzgq6ck4mFUap94aLTSJCC7sLmn%2Fk1yadyTEsJMWQUJE9Fy5wI9C5tR9IpsYBHwOrMKdmQd9x6dPF1EdiJxRSIfnNgtnfgWFJ6CCR025JXkmiZ1Q7pfgsrJx10CeqhMbZIdD0uuUK9mGldIrbNsQgQBj49HcR48JSsulnTI8a2%2B2IdeRDUrf0egUAONuCza8j59aauRKo6vh6j72%2FNaIo09d45FridlFQIt%2FkyeNoTGC1rb7hnO9vYmPM4Xp3zbpj0xNuL6YmDmQSnDb2Y8rlIRj%2F%2Bt7%2BkTrUqcR7FYnbEYEbfdnOWQw6OeIvQY6pgEdPG%2BOybmxFSB%2BMxoZDjOT84GcT0fJ0%2BLHGvvm%2F%2Bo2yKW9TxQix8eRIkoDw60AtW1eF5kcJXHySQT%2FHilAkVlKdYMhBgi1SRnlky3QxuQ7I%2B24FdfMBymIXscyTyiZGtts2EcQ0AACmx2BBJq9bYddHuCisgVld1xM%2BrzURg%2B%2BLq2hztHlaKNR4%2F7%2BfTQltJiGSaxMdW5BuDW9Rf35p%2BRZkpM5rJvI&X-Amz-Signature=55a264f2bc92995e0cbdf69e5879be6ef03c309a091c0f3558a0b308edf59987&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LBGKDSG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIFZ%2FYWp9WdClec46v%2BkGBEemil0zD452Zp1wSLrf7SgsAiBwT8NX%2FlnaVo64Gm0ETCuJP1zd2whKR2zncJlnR5mtiir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMBZ4mUax262xuYub%2BKtwDCqqCfQgwnQ9JgphtFinCGfhUxshEKAmr4t5bg56aJS5y377nqBggVMFf5Zloag1mGjqV0IEVjrjwSbiFNGyaofdkhu0%2Bv1E41Ea0L9NFwWg7aOY1OtIUg6LukXGaec1uuvetI5QP0nDn4nNdRJxM8jzBmjfkvW1sEbEEITQjdA5BLRxhKAUMbMHZDclaWFkbQSHKrFeoatOnYRNJCm1op2YVLwEq4q%2B34%2BYpHEXjmrr%2FrFDZgGdpxBIt5xFqbmPb5Y0S1LWpOf5JwuYD6HuhaLn3pg1dz%2BJujeyUf3dvqxsBlkasTezOEZ8RHUv2aHWhuuAzd2ZJSzgq6ck4mFUap94aLTSJCC7sLmn%2Fk1yadyTEsJMWQUJE9Fy5wI9C5tR9IpsYBHwOrMKdmQd9x6dPF1EdiJxRSIfnNgtnfgWFJ6CCR025JXkmiZ1Q7pfgsrJx10CeqhMbZIdD0uuUK9mGldIrbNsQgQBj49HcR48JSsulnTI8a2%2B2IdeRDUrf0egUAONuCza8j59aauRKo6vh6j72%2FNaIo09d45FridlFQIt%2FkyeNoTGC1rb7hnO9vYmPM4Xp3zbpj0xNuL6YmDmQSnDb2Y8rlIRj%2F%2Bt7%2BkTrUqcR7FYnbEYEbfdnOWQw6OeIvQY6pgEdPG%2BOybmxFSB%2BMxoZDjOT84GcT0fJ0%2BLHGvvm%2F%2Bo2yKW9TxQix8eRIkoDw60AtW1eF5kcJXHySQT%2FHilAkVlKdYMhBgi1SRnlky3QxuQ7I%2B24FdfMBymIXscyTyiZGtts2EcQ0AACmx2BBJq9bYddHuCisgVld1xM%2BrzURg%2B%2BLq2hztHlaKNR4%2F7%2BfTQltJiGSaxMdW5BuDW9Rf35p%2BRZkpM5rJvI&X-Amz-Signature=09fdcd5d5db8cccda3f2d30ca5f56197c6524eeeb274d2c8149e9e18335c9406&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656QN5H7B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICu31RDdT%2FMihi82mKGAeuMzkOT8jrFentlt3Y1HAy3UAiEApTrHsb5HNMc%2FjjL8m5K1Cd2Kskf%2FGgwDTRAq04OhBrQq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDC4vobGGXRI%2Fj5FT1SrcA3HdEP0o%2Bt5z3vVjC1nrKovtKugJwaRKbnDmfSTO9GOM3Wij8pImV9%2FRbBXV6k56s4EqhHPUD9voNhEym4Co%2BrGfS3m%2BE%2B0jsDQ6YxZD7aeIYmuCpCvnokoLWDyBKy7phJYYGaL%2FbO2ApeaMVt7USn7fldKujq%2FWlyPcc0aaWGD4fQceplnoc4J2hqEHkg40HGpgJhkkubRhL8MnyUn3s97tpCDZmo4o42UBoX7t1yZ7gPypBMH7x%2B4VdQhB1LJ9XgvaurJiZDxszjyA7E2KQbE%2BCzSmeJV7bK7iem3PRDOPoVNLpTiuA4eB0AIs%2B4JZ1m003fM%2B%2BHQ4Rw2R6tiO2VEyIQPPtWsiRFuneFh7%2FSd39znBjMXAWbJhD0UowsFX%2Fb5UKQOQ0IUG5RVINkQa%2F%2FoZzEad0o6SVLathNlabGigBVcFkcnrNFhYfU9hYyWEDApsnbDD%2FJb0Ze8plncv%2FfyXB3J9xiJaWgQHYosux0thaA3vjqQAOl0LxIcEXz34jwElE4DbO8nLR3JZ3v7jeZNX0b0hrw9XOT5LzCDfHT6oHVjoit72sXro%2FC2hg0GtWKJJZO0u610nz47TI2tsUiPL2eQc%2FBzxdW2FjHIa85wahU7h7geFEej1IP%2BdMMbmiL0GOqUBBgpigQBqRGee93g7qiDcyxw2rGhWtJU826omdvz3LisCiwMlDy7qEDgwwwE8gsXEdfXI%2BHWwJp1pDUKUy4WdYIx7APGhP50oK6INw%2Bu9LqNllSBYIzTCAhwz3MCB80p7q4huuhRIKMLlN%2FwVEH7YS7sEdytDzMjhWOHaOfyZC8dh8TUik7oWQmzhrd50v5yWAwO%2F0H6123WWude0yNXZRl%2FpemKl&X-Amz-Signature=a2b45d46f91d91f37801cc3b0f0618386313bb5dbc1e86fe9ce0caa751a357d9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656QN5H7B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICu31RDdT%2FMihi82mKGAeuMzkOT8jrFentlt3Y1HAy3UAiEApTrHsb5HNMc%2FjjL8m5K1Cd2Kskf%2FGgwDTRAq04OhBrQq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDC4vobGGXRI%2Fj5FT1SrcA3HdEP0o%2Bt5z3vVjC1nrKovtKugJwaRKbnDmfSTO9GOM3Wij8pImV9%2FRbBXV6k56s4EqhHPUD9voNhEym4Co%2BrGfS3m%2BE%2B0jsDQ6YxZD7aeIYmuCpCvnokoLWDyBKy7phJYYGaL%2FbO2ApeaMVt7USn7fldKujq%2FWlyPcc0aaWGD4fQceplnoc4J2hqEHkg40HGpgJhkkubRhL8MnyUn3s97tpCDZmo4o42UBoX7t1yZ7gPypBMH7x%2B4VdQhB1LJ9XgvaurJiZDxszjyA7E2KQbE%2BCzSmeJV7bK7iem3PRDOPoVNLpTiuA4eB0AIs%2B4JZ1m003fM%2B%2BHQ4Rw2R6tiO2VEyIQPPtWsiRFuneFh7%2FSd39znBjMXAWbJhD0UowsFX%2Fb5UKQOQ0IUG5RVINkQa%2F%2FoZzEad0o6SVLathNlabGigBVcFkcnrNFhYfU9hYyWEDApsnbDD%2FJb0Ze8plncv%2FfyXB3J9xiJaWgQHYosux0thaA3vjqQAOl0LxIcEXz34jwElE4DbO8nLR3JZ3v7jeZNX0b0hrw9XOT5LzCDfHT6oHVjoit72sXro%2FC2hg0GtWKJJZO0u610nz47TI2tsUiPL2eQc%2FBzxdW2FjHIa85wahU7h7geFEej1IP%2BdMMbmiL0GOqUBBgpigQBqRGee93g7qiDcyxw2rGhWtJU826omdvz3LisCiwMlDy7qEDgwwwE8gsXEdfXI%2BHWwJp1pDUKUy4WdYIx7APGhP50oK6INw%2Bu9LqNllSBYIzTCAhwz3MCB80p7q4huuhRIKMLlN%2FwVEH7YS7sEdytDzMjhWOHaOfyZC8dh8TUik7oWQmzhrd50v5yWAwO%2F0H6123WWude0yNXZRl%2FpemKl&X-Amz-Signature=4090ed546a90603fa8f3426a9de173f868ae2b80fe058c4ef676872033625a46&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656QN5H7B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICu31RDdT%2FMihi82mKGAeuMzkOT8jrFentlt3Y1HAy3UAiEApTrHsb5HNMc%2FjjL8m5K1Cd2Kskf%2FGgwDTRAq04OhBrQq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDC4vobGGXRI%2Fj5FT1SrcA3HdEP0o%2Bt5z3vVjC1nrKovtKugJwaRKbnDmfSTO9GOM3Wij8pImV9%2FRbBXV6k56s4EqhHPUD9voNhEym4Co%2BrGfS3m%2BE%2B0jsDQ6YxZD7aeIYmuCpCvnokoLWDyBKy7phJYYGaL%2FbO2ApeaMVt7USn7fldKujq%2FWlyPcc0aaWGD4fQceplnoc4J2hqEHkg40HGpgJhkkubRhL8MnyUn3s97tpCDZmo4o42UBoX7t1yZ7gPypBMH7x%2B4VdQhB1LJ9XgvaurJiZDxszjyA7E2KQbE%2BCzSmeJV7bK7iem3PRDOPoVNLpTiuA4eB0AIs%2B4JZ1m003fM%2B%2BHQ4Rw2R6tiO2VEyIQPPtWsiRFuneFh7%2FSd39znBjMXAWbJhD0UowsFX%2Fb5UKQOQ0IUG5RVINkQa%2F%2FoZzEad0o6SVLathNlabGigBVcFkcnrNFhYfU9hYyWEDApsnbDD%2FJb0Ze8plncv%2FfyXB3J9xiJaWgQHYosux0thaA3vjqQAOl0LxIcEXz34jwElE4DbO8nLR3JZ3v7jeZNX0b0hrw9XOT5LzCDfHT6oHVjoit72sXro%2FC2hg0GtWKJJZO0u610nz47TI2tsUiPL2eQc%2FBzxdW2FjHIa85wahU7h7geFEej1IP%2BdMMbmiL0GOqUBBgpigQBqRGee93g7qiDcyxw2rGhWtJU826omdvz3LisCiwMlDy7qEDgwwwE8gsXEdfXI%2BHWwJp1pDUKUy4WdYIx7APGhP50oK6INw%2Bu9LqNllSBYIzTCAhwz3MCB80p7q4huuhRIKMLlN%2FwVEH7YS7sEdytDzMjhWOHaOfyZC8dh8TUik7oWQmzhrd50v5yWAwO%2F0H6123WWude0yNXZRl%2FpemKl&X-Amz-Signature=1bb96e5775c02885d154b28d79b36b0be9195d12d565366afbdd8db073e23be6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656QN5H7B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICu31RDdT%2FMihi82mKGAeuMzkOT8jrFentlt3Y1HAy3UAiEApTrHsb5HNMc%2FjjL8m5K1Cd2Kskf%2FGgwDTRAq04OhBrQq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDC4vobGGXRI%2Fj5FT1SrcA3HdEP0o%2Bt5z3vVjC1nrKovtKugJwaRKbnDmfSTO9GOM3Wij8pImV9%2FRbBXV6k56s4EqhHPUD9voNhEym4Co%2BrGfS3m%2BE%2B0jsDQ6YxZD7aeIYmuCpCvnokoLWDyBKy7phJYYGaL%2FbO2ApeaMVt7USn7fldKujq%2FWlyPcc0aaWGD4fQceplnoc4J2hqEHkg40HGpgJhkkubRhL8MnyUn3s97tpCDZmo4o42UBoX7t1yZ7gPypBMH7x%2B4VdQhB1LJ9XgvaurJiZDxszjyA7E2KQbE%2BCzSmeJV7bK7iem3PRDOPoVNLpTiuA4eB0AIs%2B4JZ1m003fM%2B%2BHQ4Rw2R6tiO2VEyIQPPtWsiRFuneFh7%2FSd39znBjMXAWbJhD0UowsFX%2Fb5UKQOQ0IUG5RVINkQa%2F%2FoZzEad0o6SVLathNlabGigBVcFkcnrNFhYfU9hYyWEDApsnbDD%2FJb0Ze8plncv%2FfyXB3J9xiJaWgQHYosux0thaA3vjqQAOl0LxIcEXz34jwElE4DbO8nLR3JZ3v7jeZNX0b0hrw9XOT5LzCDfHT6oHVjoit72sXro%2FC2hg0GtWKJJZO0u610nz47TI2tsUiPL2eQc%2FBzxdW2FjHIa85wahU7h7geFEej1IP%2BdMMbmiL0GOqUBBgpigQBqRGee93g7qiDcyxw2rGhWtJU826omdvz3LisCiwMlDy7qEDgwwwE8gsXEdfXI%2BHWwJp1pDUKUy4WdYIx7APGhP50oK6INw%2Bu9LqNllSBYIzTCAhwz3MCB80p7q4huuhRIKMLlN%2FwVEH7YS7sEdytDzMjhWOHaOfyZC8dh8TUik7oWQmzhrd50v5yWAwO%2F0H6123WWude0yNXZRl%2FpemKl&X-Amz-Signature=323bcb898ac0e176b324365ef9ad5f6ff5de1847c5864c5a443a34bd812cb6c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656QN5H7B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICu31RDdT%2FMihi82mKGAeuMzkOT8jrFentlt3Y1HAy3UAiEApTrHsb5HNMc%2FjjL8m5K1Cd2Kskf%2FGgwDTRAq04OhBrQq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDC4vobGGXRI%2Fj5FT1SrcA3HdEP0o%2Bt5z3vVjC1nrKovtKugJwaRKbnDmfSTO9GOM3Wij8pImV9%2FRbBXV6k56s4EqhHPUD9voNhEym4Co%2BrGfS3m%2BE%2B0jsDQ6YxZD7aeIYmuCpCvnokoLWDyBKy7phJYYGaL%2FbO2ApeaMVt7USn7fldKujq%2FWlyPcc0aaWGD4fQceplnoc4J2hqEHkg40HGpgJhkkubRhL8MnyUn3s97tpCDZmo4o42UBoX7t1yZ7gPypBMH7x%2B4VdQhB1LJ9XgvaurJiZDxszjyA7E2KQbE%2BCzSmeJV7bK7iem3PRDOPoVNLpTiuA4eB0AIs%2B4JZ1m003fM%2B%2BHQ4Rw2R6tiO2VEyIQPPtWsiRFuneFh7%2FSd39znBjMXAWbJhD0UowsFX%2Fb5UKQOQ0IUG5RVINkQa%2F%2FoZzEad0o6SVLathNlabGigBVcFkcnrNFhYfU9hYyWEDApsnbDD%2FJb0Ze8plncv%2FfyXB3J9xiJaWgQHYosux0thaA3vjqQAOl0LxIcEXz34jwElE4DbO8nLR3JZ3v7jeZNX0b0hrw9XOT5LzCDfHT6oHVjoit72sXro%2FC2hg0GtWKJJZO0u610nz47TI2tsUiPL2eQc%2FBzxdW2FjHIa85wahU7h7geFEej1IP%2BdMMbmiL0GOqUBBgpigQBqRGee93g7qiDcyxw2rGhWtJU826omdvz3LisCiwMlDy7qEDgwwwE8gsXEdfXI%2BHWwJp1pDUKUy4WdYIx7APGhP50oK6INw%2Bu9LqNllSBYIzTCAhwz3MCB80p7q4huuhRIKMLlN%2FwVEH7YS7sEdytDzMjhWOHaOfyZC8dh8TUik7oWQmzhrd50v5yWAwO%2F0H6123WWude0yNXZRl%2FpemKl&X-Amz-Signature=32315ff638e1efb195c035286b15c8bacc1f0859c98a422fd29c722aec63728c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656QN5H7B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICu31RDdT%2FMihi82mKGAeuMzkOT8jrFentlt3Y1HAy3UAiEApTrHsb5HNMc%2FjjL8m5K1Cd2Kskf%2FGgwDTRAq04OhBrQq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDC4vobGGXRI%2Fj5FT1SrcA3HdEP0o%2Bt5z3vVjC1nrKovtKugJwaRKbnDmfSTO9GOM3Wij8pImV9%2FRbBXV6k56s4EqhHPUD9voNhEym4Co%2BrGfS3m%2BE%2B0jsDQ6YxZD7aeIYmuCpCvnokoLWDyBKy7phJYYGaL%2FbO2ApeaMVt7USn7fldKujq%2FWlyPcc0aaWGD4fQceplnoc4J2hqEHkg40HGpgJhkkubRhL8MnyUn3s97tpCDZmo4o42UBoX7t1yZ7gPypBMH7x%2B4VdQhB1LJ9XgvaurJiZDxszjyA7E2KQbE%2BCzSmeJV7bK7iem3PRDOPoVNLpTiuA4eB0AIs%2B4JZ1m003fM%2B%2BHQ4Rw2R6tiO2VEyIQPPtWsiRFuneFh7%2FSd39znBjMXAWbJhD0UowsFX%2Fb5UKQOQ0IUG5RVINkQa%2F%2FoZzEad0o6SVLathNlabGigBVcFkcnrNFhYfU9hYyWEDApsnbDD%2FJb0Ze8plncv%2FfyXB3J9xiJaWgQHYosux0thaA3vjqQAOl0LxIcEXz34jwElE4DbO8nLR3JZ3v7jeZNX0b0hrw9XOT5LzCDfHT6oHVjoit72sXro%2FC2hg0GtWKJJZO0u610nz47TI2tsUiPL2eQc%2FBzxdW2FjHIa85wahU7h7geFEej1IP%2BdMMbmiL0GOqUBBgpigQBqRGee93g7qiDcyxw2rGhWtJU826omdvz3LisCiwMlDy7qEDgwwwE8gsXEdfXI%2BHWwJp1pDUKUy4WdYIx7APGhP50oK6INw%2Bu9LqNllSBYIzTCAhwz3MCB80p7q4huuhRIKMLlN%2FwVEH7YS7sEdytDzMjhWOHaOfyZC8dh8TUik7oWQmzhrd50v5yWAwO%2F0H6123WWude0yNXZRl%2FpemKl&X-Amz-Signature=afde63cb694943df4dacda04e7608c61d575a2d4c1f68de310abf3c5b361aeec&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QE4ZUEFX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHJ94Vn5UbONclb1gQTlVsEqyEzZdDjC9FUEQMcdRG1UAiBJZuJ%2BC6RA1BY6pQTRy9KMrCZgKB5X5D%2FDl%2F0Tc4q%2Bfir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMXfiyKtG65s9MEIzyKtwDs1BrIf4w4Jbbv4ccmC68P1mltS11e2aY9%2FMf8kKEnMs2pskHvWt%2F55xW%2Bhrsr5w4phAqPT%2BBZt%2FD0wdYfCwmnpUw20LvWel1bEZCNYydoZ4haayCc8rUNfJxpyQQOGRJLRM4bWjHBTTjXM7xR4zVypl%2Fvl88X9lIHkt2EFkM%2FprqFM6y4w3ga5oHbtYVIrUcVsfM9TsKHEsk5NfYR5XnhbG86MvGEIoxyLgLhAH86ED4Sw5gd6cBgrqVTDk7EL2p3BzS0xWhkVY8wRhrYtBnHAzl1yZNWT3STSwUKsQFXbJhTfpbM75vdCC0sU43Ljkb%2BCSy6X3ofSZcMG0hQPIIdbV4opFcMmnP2Ys1tlPRuSI8CSB0sP5bUIGnPEiQJWl3IKE8OESzfVnXUFOZNZZFjFbLgRsXe2Inl97Upem%2FEaA28%2Fu%2FUpBd18NWpyYdu1fBRNsxaG%2F6XwCJAYHDkNtZWfBgPi0rqmkenZivcdFqePWdQnw0JPzZ2UFE3aSi1enyoZ4ruzc%2FzL%2BECvLcKaPxgIK7QJsfSbJAsBibn9tF7CeeL0qe2oygv8TJw0fGi7lnhlFN88MWhzs41Eck0%2FkZeTAYC1bNx1kSBwsEXzI9gJZ1au80S2ePYAJlSZowgOeIvQY6pgFjsKqszJQtyRA7gckl%2B5UjGOuEuqcAydUWClCAW%2FsecNlt1Cfg7aeY2N9oqwrzjj2sUfIa3qfsFdAiSiz%2FDuhhn%2BXgTOyNz34XICkwJS7LkeQUWOVNYbrLIOjN3sX6ewsXXossnVRdRIEM5ZdFINkjbxnJw3AKXt7A8ls3%2BtLh8SMGb7%2BuaJSnTCXRRJ1TnZwaMpW153SOZnAjlsZ4uV4AEph31WK%2B&X-Amz-Signature=8bd1bd577a6cf8a60e6a025aedd06b71fd84af2d95b93248bb10637a78322b9d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTB4C7WL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDAr%2F5BhZkZIpkyqmxebHdD2UBRAxsn0aDlT9KXFX1vIQIgFyLm3Re8sxSANwGWO0%2FLVF3VGcPOzenkGOZEscEqfGYq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDF42LhSu2jafGvNJhyrcA962XEzKRMwQ0t5A%2F12NbXP9FbGg98gVEVoZW%2FKqUu0BhdBFNm%2F9isRd6bhlqqPdoyfX5RNqIh4gT1bTh1aQsprfMcUzhrkSXw95axu%2BYNbP5TU2HrkfGbdh%2BKi5glw%2ByKa2PqulyOWqf%2BljSDr4aHaYsS4AiXE04hie3kKIMc0OG6jMzzEv9LuqsCBp5TnySjXZHt7LW2IDMmYCgFXue3ldNlCfvndqy6%2Fc%2BF4Ugq6hoSUMQ6UEdH%2F5QGkdeYE0uwaRG1kPTD4ORlRFoqXGazXxl5Fur7KzFOEoeEaPBwohK18%2Fmj6Zx90sIEqz5%2Fs1s915Ywr%2FKFZoBA89qhP%2B8pANBntXZI3xB9Hl%2FcnaRdN1HAABj9DiXpUByCbRhfLKmSkQ411KLuGuWGvN2%2FpzffTXDUHOm2nP0%2FltvP8S3g8ZyYhzLmDbmLBKDpLne8x8iAnBSr%2BVEdSXr0prUb7vLl9qaMbtYXCEvod1E2r3PIGTGO%2F0m2IthGM2Fkr6HHE8mWrATHCdrz442eY66ZF%2B2Q%2BwJmObU4TUA1uP4ts1XRP9s5OqQ6duoFBSOsFgbgRz8QRjw2GMaZxClaxjgcU1x4Bpv%2BaXXMCL7qleLPy6BUwjeRieBvUAhAzBmJ10MJnniL0GOqUBilzo%2BDbm9hbSevE0lUUaWldalMHmFn9nz%2FUzvDc%2FUV%2BoWebg0gSTz%2BMOc2MyhQ6rnd9prtyaQD3lIL22nICZaL71GgqcBWTL2qhOYNDDzF4MrulMhHdG2xUj0PBV8nqgFJ1FJoVb6KJMv6QoE%2BYiyFLTLY0LD79sBuOHwduPt0RMJ52mmAgJWmRptfeRGOO8qlpYNhx7CISuNK4jO%2FmQPbvrekLc&X-Amz-Signature=cf655bb161f272ba511c6ae86f80784c7b15da686f8238e79c8f0f2b650ad04e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656QN5H7B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICu31RDdT%2FMihi82mKGAeuMzkOT8jrFentlt3Y1HAy3UAiEApTrHsb5HNMc%2FjjL8m5K1Cd2Kskf%2FGgwDTRAq04OhBrQq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDC4vobGGXRI%2Fj5FT1SrcA3HdEP0o%2Bt5z3vVjC1nrKovtKugJwaRKbnDmfSTO9GOM3Wij8pImV9%2FRbBXV6k56s4EqhHPUD9voNhEym4Co%2BrGfS3m%2BE%2B0jsDQ6YxZD7aeIYmuCpCvnokoLWDyBKy7phJYYGaL%2FbO2ApeaMVt7USn7fldKujq%2FWlyPcc0aaWGD4fQceplnoc4J2hqEHkg40HGpgJhkkubRhL8MnyUn3s97tpCDZmo4o42UBoX7t1yZ7gPypBMH7x%2B4VdQhB1LJ9XgvaurJiZDxszjyA7E2KQbE%2BCzSmeJV7bK7iem3PRDOPoVNLpTiuA4eB0AIs%2B4JZ1m003fM%2B%2BHQ4Rw2R6tiO2VEyIQPPtWsiRFuneFh7%2FSd39znBjMXAWbJhD0UowsFX%2Fb5UKQOQ0IUG5RVINkQa%2F%2FoZzEad0o6SVLathNlabGigBVcFkcnrNFhYfU9hYyWEDApsnbDD%2FJb0Ze8plncv%2FfyXB3J9xiJaWgQHYosux0thaA3vjqQAOl0LxIcEXz34jwElE4DbO8nLR3JZ3v7jeZNX0b0hrw9XOT5LzCDfHT6oHVjoit72sXro%2FC2hg0GtWKJJZO0u610nz47TI2tsUiPL2eQc%2FBzxdW2FjHIa85wahU7h7geFEej1IP%2BdMMbmiL0GOqUBBgpigQBqRGee93g7qiDcyxw2rGhWtJU826omdvz3LisCiwMlDy7qEDgwwwE8gsXEdfXI%2BHWwJp1pDUKUy4WdYIx7APGhP50oK6INw%2Bu9LqNllSBYIzTCAhwz3MCB80p7q4huuhRIKMLlN%2FwVEH7YS7sEdytDzMjhWOHaOfyZC8dh8TUik7oWQmzhrd50v5yWAwO%2F0H6123WWude0yNXZRl%2FpemKl&X-Amz-Signature=44e9a08d673384bf3178541a2bcdedbb5c06e3a633c86dadcb42d6765adc7254&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656QN5H7B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICu31RDdT%2FMihi82mKGAeuMzkOT8jrFentlt3Y1HAy3UAiEApTrHsb5HNMc%2FjjL8m5K1Cd2Kskf%2FGgwDTRAq04OhBrQq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDC4vobGGXRI%2Fj5FT1SrcA3HdEP0o%2Bt5z3vVjC1nrKovtKugJwaRKbnDmfSTO9GOM3Wij8pImV9%2FRbBXV6k56s4EqhHPUD9voNhEym4Co%2BrGfS3m%2BE%2B0jsDQ6YxZD7aeIYmuCpCvnokoLWDyBKy7phJYYGaL%2FbO2ApeaMVt7USn7fldKujq%2FWlyPcc0aaWGD4fQceplnoc4J2hqEHkg40HGpgJhkkubRhL8MnyUn3s97tpCDZmo4o42UBoX7t1yZ7gPypBMH7x%2B4VdQhB1LJ9XgvaurJiZDxszjyA7E2KQbE%2BCzSmeJV7bK7iem3PRDOPoVNLpTiuA4eB0AIs%2B4JZ1m003fM%2B%2BHQ4Rw2R6tiO2VEyIQPPtWsiRFuneFh7%2FSd39znBjMXAWbJhD0UowsFX%2Fb5UKQOQ0IUG5RVINkQa%2F%2FoZzEad0o6SVLathNlabGigBVcFkcnrNFhYfU9hYyWEDApsnbDD%2FJb0Ze8plncv%2FfyXB3J9xiJaWgQHYosux0thaA3vjqQAOl0LxIcEXz34jwElE4DbO8nLR3JZ3v7jeZNX0b0hrw9XOT5LzCDfHT6oHVjoit72sXro%2FC2hg0GtWKJJZO0u610nz47TI2tsUiPL2eQc%2FBzxdW2FjHIa85wahU7h7geFEej1IP%2BdMMbmiL0GOqUBBgpigQBqRGee93g7qiDcyxw2rGhWtJU826omdvz3LisCiwMlDy7qEDgwwwE8gsXEdfXI%2BHWwJp1pDUKUy4WdYIx7APGhP50oK6INw%2Bu9LqNllSBYIzTCAhwz3MCB80p7q4huuhRIKMLlN%2FwVEH7YS7sEdytDzMjhWOHaOfyZC8dh8TUik7oWQmzhrd50v5yWAwO%2F0H6123WWude0yNXZRl%2FpemKl&X-Amz-Signature=94ecd6fddafa14fd5efebe834159684d8310cb38457547a9d49c5120dcbcf958&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656QN5H7B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICu31RDdT%2FMihi82mKGAeuMzkOT8jrFentlt3Y1HAy3UAiEApTrHsb5HNMc%2FjjL8m5K1Cd2Kskf%2FGgwDTRAq04OhBrQq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDC4vobGGXRI%2Fj5FT1SrcA3HdEP0o%2Bt5z3vVjC1nrKovtKugJwaRKbnDmfSTO9GOM3Wij8pImV9%2FRbBXV6k56s4EqhHPUD9voNhEym4Co%2BrGfS3m%2BE%2B0jsDQ6YxZD7aeIYmuCpCvnokoLWDyBKy7phJYYGaL%2FbO2ApeaMVt7USn7fldKujq%2FWlyPcc0aaWGD4fQceplnoc4J2hqEHkg40HGpgJhkkubRhL8MnyUn3s97tpCDZmo4o42UBoX7t1yZ7gPypBMH7x%2B4VdQhB1LJ9XgvaurJiZDxszjyA7E2KQbE%2BCzSmeJV7bK7iem3PRDOPoVNLpTiuA4eB0AIs%2B4JZ1m003fM%2B%2BHQ4Rw2R6tiO2VEyIQPPtWsiRFuneFh7%2FSd39znBjMXAWbJhD0UowsFX%2Fb5UKQOQ0IUG5RVINkQa%2F%2FoZzEad0o6SVLathNlabGigBVcFkcnrNFhYfU9hYyWEDApsnbDD%2FJb0Ze8plncv%2FfyXB3J9xiJaWgQHYosux0thaA3vjqQAOl0LxIcEXz34jwElE4DbO8nLR3JZ3v7jeZNX0b0hrw9XOT5LzCDfHT6oHVjoit72sXro%2FC2hg0GtWKJJZO0u610nz47TI2tsUiPL2eQc%2FBzxdW2FjHIa85wahU7h7geFEej1IP%2BdMMbmiL0GOqUBBgpigQBqRGee93g7qiDcyxw2rGhWtJU826omdvz3LisCiwMlDy7qEDgwwwE8gsXEdfXI%2BHWwJp1pDUKUy4WdYIx7APGhP50oK6INw%2Bu9LqNllSBYIzTCAhwz3MCB80p7q4huuhRIKMLlN%2FwVEH7YS7sEdytDzMjhWOHaOfyZC8dh8TUik7oWQmzhrd50v5yWAwO%2F0H6123WWude0yNXZRl%2FpemKl&X-Amz-Signature=949590d82458c602c46a6fb066bb671f1d7ec3d879a01a4ab53da0fac073f9ea&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQPQXVKV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIFGRkrXMbR67abIbcDgyKPmdOjXEKAFahIMOfO3o6dScAiEAorkGncxtckav8KQZM8Bp%2FTCRsMCWLwOUMkyHyJHGwlcq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDIMbY%2BSeUHRoiLauNyrcA9IFrdvNDVLOiYg2ewlutBtBhnZALLlY1%2F1KY68gRskRCvBgkMoLUdeE5pxvN6vJ%2Bi8haoLhGzjof7odKNFYXV7F%2FCrcHx%2FZdeO%2BkZUGvyqINnfaIkCtwJm%2FAFly4EMH%2BAIj4iAzK8CxIdIlZ7PuXVxO%2B%2FvR28tEuozhGHEolnL7A6B3jSrvwUZc2GmO3K5j3TXHaqG2AX0PswzKJnyBr4HQ5Yv%2Fb2oM4jBZs686FbLK0hwtnl25KJ9Cq%2F2cTjSh3qSq3R6Ox3eBN7975WQVPrB6L2jDg1k9uW32DyyReC36DaMK7tY5jfE1%2FvJS0TvEZm%2Fgrug2vhFMXAXPFqNqtcU9UXKNTg6DXghh%2BwQ9%2Fn4Vy0xc9yfUAaUsn8W5OIlKmxI2rMat1Aeo1NjpCUQmW9iGDFWzOgp1jtRZrbxdApsjESopl0tE827p5ElYzJr2rsH5wcgXPnYLlOrksY%2FA%2FrFocCM5TtoNAoltiW%2FhhezWOgGlIkeEOLxr2L5IHMkNOIG6YBsOUqb5meFboth8TgEsSvgo8HygkjWv82hzn7r1hKFuUaiyaE2FFeS%2BZ4b%2B2e3Y0d8RT%2FCnkWx4wZiMbSanW9LvH6AKHNLwp%2FVL3HE4reQEzIBgSf5NVWXWMI%2FoiL0GOqUBB%2BcIUwVIoyUYmOH23LLyZoqqnQbyVM30XAuQHNmXdGw4SMuowx53j9jmtyJOtSndgRirqaDMvexydO5c8gqo9Q1uemZKVtIz7iGx8SrZBoJmQvQE5qnB8%2FrBtJh151EQ%2BXl%2B08iU3CfKDLtd8Zy3CoLQju7ECFqmReCkSycNZKBpm9TfhcH5bnedeV6p9IuD94QNIP7PX6tCcjqsi6thEb%2FG%2B3e8&X-Amz-Signature=6941ad828db672a240a2336fbe001fb0f15942e48bfc4e1dd0fff9daf0b0a55c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAS5L3HA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQCnRhvaS2loLjxNnx1Cwtz2wSuEGR2XGzGRRuJQcEMiLgIgbWkRurdapE1dzHszgXx2BoYiokDsMEfZrNrzpXfWFr8q%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDEsgJzE1Y0IEQ4xI2SrcA4sStarF7ZOoW9O5vrAA5rEXDhc44X4Chao0XWhmEApCmKMukOgOME6n%2BABBiqPhnPYu3d3bWlB73Mh%2Fxx5R9w7he3%2F07jfqpTr2NaPvqxyuFDA%2BNc7A8Xu691A%2FJRD5XXHG1YI3h12G12m1Ql1kUj7C0mhr%2BJGV81PbAwrbRLIugzh6MX5f0O%2ByKDOt%2FfNdpPRFzpq11nOlPQUFH6qjBYtQKjsrKLeYMSRrJkJnqQ7b6zj%2F0z2Ikuyft7fjWtGkWk4bpUtRu5%2FoiDC5Hwo84F5G2jrObK0FLNCFNFsfdrazcvWigJshvl%2Bwm4WALEL63bXftawiakTOfWnUqyOcNuKMweaRqdSqrJIkmRuDVSF2WWDgQeM2m1ftFaGpdF9NAi%2Faa4lBjlBSZJWe%2F%2FzcnHQbcpZHIO4Pueg%2BwGzStGKJlxtqN8Ho93MkA7wz1SVCYN53rurhHf6do4pm2O6LIlNyyo7LmN6G1OnzmV%2Ba4%2BsWJ0kYPYf0BUa6jegJ0QdEyb9A%2F11gcKJ65ljTbDu000teNBjH9GHFab8Db8H6hvU6LJkw1fr1%2F%2B7f%2F96sq9wHUQMKx15xLOYhDLwCzqmUhGJY1AuntE9FKya7H4u8xdKyvpNyTt0%2F%2BxoCllrxMIDniL0GOqUBiTVFfK%2BEyAUZyOykxRxWg0hHHAGNhXLxq7yxp%2B6B7VARwOE6o9UEbyKObLeD2vKSOEfARHplDwfhQsFKY1MD0JYMA2YcK6o3rbqDyudBzQ6cz5xTWIyj87Wgvs7dGUniW3x6ILXljMqH7cRrqbv%2BcW%2BMLX%2FyUa5EYn1US9%2BLf7fHEcwsxhGlMepxu6B88jqcl7ix51y7K475b7GLqcuNLpCTQw0D&X-Amz-Signature=4fe2f3cadc07506dcee570d493826216aec480dcb48793fa9ec2e59b5d72924e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ANAAPMH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIDTDviRV37SeEV3M%2BtdPRZaeqTejEpRX9U14PL%2FGzWmgAiBv2vmC5mUKx2TY8G9eZ9HLCHOnFsA8Ij4FXGCWESuDWSr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMntRhFmTKt81cIBsmKtwDA%2FxHNZ9h7gmw8sN%2BEpe09T73fb9Isj7liIs9HQ08NgFjPpQQDuqOeKFBYQi4uDfXtVySVuLxhDUzx6GSX2ZhHfFkOropni92TMglY7EIHRrParNKMLwRrZm13PSccSTpoMyFsnRAeBuBI8k%2BNB5UTmcSGoZDRQTUJYpH5G%2BWPLhWRytguHEfpBPDfGJzok5PpRD%2BYM1nnl7DhvQCkUhVnoz3kk5MIpK161dZFk3oMNr51lGzTKCiP2OXvciJRLIb7kTbRFZcxo5FYgb3WHfBCshpgzsKHwyW%2FwKlrY9Z31rrPIpxWdauKUWQK15RN4FGm7YzH88gZhPLQ974GP7UubzuDMoWQ2akxdaaJtXDYFQCOvX7BPJv38%2BnqDNxH%2FU%2BgP7bwRSLNrGfWITDR0jQ3T4zSWf8VTuro0dgI3vqhkPhWlqIdDg3G1kxkGU6hlK5OhQt7QegiQVn4SM3Bo1Krxay82J4K5mDX2X1wo9zOnYULjpkMOd8jdUsKs8dOInE29Df9bNzlHrmN%2FxAXYstRlZe7HUaLok1z2HJuy1dvIBK4VkWkU2GCT5pM%2Bt7BAU1u2jevaWs7VbDj2qyHu1RiRsLEy72QiKO391cl8RV6zAdP5n%2BRmgMyxcyvBwws%2BeIvQY6pgHkOyfVYAV%2BhhcP9mcB0SjYLRjG%2BLXTqgnHs3GmfF7uVVmyRJ1JwFri0bjzaN4wv1gkipCC5cjuCANzxQ7T1jeYfb2wrBlVqm%2FnvXsmxlGQ511Uo%2B%2FdBc5ozLzvMfi7hICfSuj1kaZvmeBiqHb4UKSuCY5x4A9sAjvwbxz7QbnBvKTkFg8WzFGRD36Bu0HcyrpVu2cekwm9U%2F7bKdueXzaLr8gfS3Q4&X-Amz-Signature=5a863083050a32d4f4c5f574ee2a950ea0a1cca010a4fba9677e03f76fd5e8f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664G5MQSD6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIDGUkn8GLLCKkebKlf%2BvFhY3qVdzjuxnDQsXADb4hwwdAiEAlB5lTJWv%2FaGv%2BzWVAANC1kPYfp69%2BdyU2k2umikh094q%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDM1hmxIf6dbAB5s2aSrcAw047Qg1xeAFY%2BQbbUlxO%2F5zm307nlajBRP2VbnYBK5K6JchZxoXLkdp3CCj5x%2BPkkavlm6PCPG2Llz%2FHgmzz8QJIKNrgzg4G72qjXYxqNY5eGxtPs1WdOOPN91Atf26A2kUncORYf3tp70xo4RW8mypJI5QFjOS%2FDAP7IRTcgE3n3o38rSiuYAVRMvZoZ35TsZTULVrp5YLoweGTmhNEz47ZylEca8jWJ9LjJo57EY7zq32w12eLMXY4g%2FGqbNz%2BT%2FjLOtslfbVQaLIcLPjpG0w2Q8m6pGsusDvc%2BOUsydoVyBurFYhfi%2Fsovb4RvHLsoKwo8wDcGjGEc2zmua%2BtacWwMMzLgpx7NrNubk5a7YgVyI%2BWY2wSHhaHvqBUob8dAXrOpPuKbbE2DYOnuY%2B4R8cwJlDAX8xRmaHCUzRuxrxqiub%2B7nMbaHKysjB8TeYywT3qae4kfdyj%2BFt1EIY9AGLyTtvqxrITWbdu6jxNpfsUOu%2FQWzyJg51yJnBwE6RFXTIA68yeSBtAOj%2FQgKfYQzwxGcUB46oi0jk3DEs1NYwHP%2BHiR9snLFVAoAdZA0nA%2Fs8a8io6PkZKhaM3co260KDCchoA%2F7IP6Oagkmpc2RDQHDR2Gbi2I7rPzb0MO3niL0GOqUBltLyQ75dGYsx1daYX9dVEJEuQ09zq8uGLE1VRMxG07pEjULvmoVtl6WvCMVmEmMasoJ8dKbH%2FY6rkpcWU9CNOY3Sh22nAYPu4iKCymcrU6bg4SKy%2FO7FEm%2FMfbVplRcEp0h5uqlBzaqLZZ%2Fgxdm0%2Ftm9B3cDXmoRkI6rLSYxhthFdRyWe5jLHjGw2dPOvjlyLFPFa1w2AMF0N6Epiip9NJP%2B%2FzdG&X-Amz-Signature=c06c5423a0c3aed5d428f34831f81c76da9553b80d97f97969f51d7d6f6fa2bc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664G5MQSD6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIDGUkn8GLLCKkebKlf%2BvFhY3qVdzjuxnDQsXADb4hwwdAiEAlB5lTJWv%2FaGv%2BzWVAANC1kPYfp69%2BdyU2k2umikh094q%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDM1hmxIf6dbAB5s2aSrcAw047Qg1xeAFY%2BQbbUlxO%2F5zm307nlajBRP2VbnYBK5K6JchZxoXLkdp3CCj5x%2BPkkavlm6PCPG2Llz%2FHgmzz8QJIKNrgzg4G72qjXYxqNY5eGxtPs1WdOOPN91Atf26A2kUncORYf3tp70xo4RW8mypJI5QFjOS%2FDAP7IRTcgE3n3o38rSiuYAVRMvZoZ35TsZTULVrp5YLoweGTmhNEz47ZylEca8jWJ9LjJo57EY7zq32w12eLMXY4g%2FGqbNz%2BT%2FjLOtslfbVQaLIcLPjpG0w2Q8m6pGsusDvc%2BOUsydoVyBurFYhfi%2Fsovb4RvHLsoKwo8wDcGjGEc2zmua%2BtacWwMMzLgpx7NrNubk5a7YgVyI%2BWY2wSHhaHvqBUob8dAXrOpPuKbbE2DYOnuY%2B4R8cwJlDAX8xRmaHCUzRuxrxqiub%2B7nMbaHKysjB8TeYywT3qae4kfdyj%2BFt1EIY9AGLyTtvqxrITWbdu6jxNpfsUOu%2FQWzyJg51yJnBwE6RFXTIA68yeSBtAOj%2FQgKfYQzwxGcUB46oi0jk3DEs1NYwHP%2BHiR9snLFVAoAdZA0nA%2Fs8a8io6PkZKhaM3co260KDCchoA%2F7IP6Oagkmpc2RDQHDR2Gbi2I7rPzb0MO3niL0GOqUBltLyQ75dGYsx1daYX9dVEJEuQ09zq8uGLE1VRMxG07pEjULvmoVtl6WvCMVmEmMasoJ8dKbH%2FY6rkpcWU9CNOY3Sh22nAYPu4iKCymcrU6bg4SKy%2FO7FEm%2FMfbVplRcEp0h5uqlBzaqLZZ%2Fgxdm0%2Ftm9B3cDXmoRkI6rLSYxhthFdRyWe5jLHjGw2dPOvjlyLFPFa1w2AMF0N6Epiip9NJP%2B%2FzdG&X-Amz-Signature=80c3de5aee3cae25588f106c22e27ca500b0320332ad0aa81091e5dfe67501bd&X-Amz-SignedHeaders=host&x-id=GetObject)

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
