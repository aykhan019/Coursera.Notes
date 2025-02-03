

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DHNMXHV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9rFEHZtQ%2FG7KinNLNAXtluzLJ20Rwopqj7K0U3ij%2BAAiBOhgrQ5xUUwZdvRklYgVuFiFYVZmFHc7Rh9ujvv4VWDCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMPktkowyAAHbwuddKtwDH5bG5Q7ZYuLtIrPgkwtN28ANI6BdRwg%2Fdj6ZceMS82kchqYiQZi0RZNM2Bigl3auzs4CdvANB%2Fh4krBunLbu4WIs7bM21uaIa4l7F%2B0gMwc4%2BLX3wivkL4kgc0VWpTjymICQ%2BOmZHL5adSnKGyFMqtIZxsT4s62k6cTY%2B5squo2SOtj2vsxHhkxE1bO5XT108j55Bl5AKdXos9pqUtVGRwvwdJNcQejJz0OLsgKWBZEYRrViItMePtDyuOMXQ4yVnNfeTvLKA0tE0W1GfLhPYNBQWLc5F9r2B6j14hDqAHSJJfBuNecAlqa67NnQtMh868VNWXLA8tOEcMILKYmBRwUXW%2FXOFaAqejLzKVBFZBG7898oBEbfaJVU3yEocZC7J9jrDqjLu3eptdTVIKJYG6fh975wk9Xlj4mxAE4O1jcwR%2B%2BW9iHA3Vm2G2nZoKVwVYaIuJJ0iEakuvY%2FN4etdg58%2FwKbRB6rQyjwM%2FcLIAS%2BkVY6JnF3ZVFZCaUc5GSem75LBujtE1lH3bTuKe5HqmZGAzLDTjw%2FveUv%2B54Df1cijxX878vcDQk3ZBl%2FCoxpv8IwquVecPXpxeBLOzzv82IDnWi%2B074H5y4HYmKY8rToJB7TUOvB%2BOqOyvowj8CAvQY6pgGjLbN3ZHQNfYBl5RYz%2FLICrxE6fK2A18xTTs5h87E%2BfgpPWlEJ0jPWB4cIknhu07Ptf%2FhMbdNXwYrq6De4KmN0HOZvf3k%2BdqZZgp%2FZxGZ0ZQEuWoVnJjbHpyMFOO5Tu2GW4GgpAoMH9Bb%2BraKbErQONkZuBYd8yTUQWcY83KKUrCZEuQhJTXttdLJghkrFagVjitEff2FreiGc%2BwY2SzmdrxYk7vIJ&X-Amz-Signature=87aad063175e6b7623d844f2bc3151a97c5cb87e996e6ec32aa8d4d2b3c31113&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DHNMXHV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9rFEHZtQ%2FG7KinNLNAXtluzLJ20Rwopqj7K0U3ij%2BAAiBOhgrQ5xUUwZdvRklYgVuFiFYVZmFHc7Rh9ujvv4VWDCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMPktkowyAAHbwuddKtwDH5bG5Q7ZYuLtIrPgkwtN28ANI6BdRwg%2Fdj6ZceMS82kchqYiQZi0RZNM2Bigl3auzs4CdvANB%2Fh4krBunLbu4WIs7bM21uaIa4l7F%2B0gMwc4%2BLX3wivkL4kgc0VWpTjymICQ%2BOmZHL5adSnKGyFMqtIZxsT4s62k6cTY%2B5squo2SOtj2vsxHhkxE1bO5XT108j55Bl5AKdXos9pqUtVGRwvwdJNcQejJz0OLsgKWBZEYRrViItMePtDyuOMXQ4yVnNfeTvLKA0tE0W1GfLhPYNBQWLc5F9r2B6j14hDqAHSJJfBuNecAlqa67NnQtMh868VNWXLA8tOEcMILKYmBRwUXW%2FXOFaAqejLzKVBFZBG7898oBEbfaJVU3yEocZC7J9jrDqjLu3eptdTVIKJYG6fh975wk9Xlj4mxAE4O1jcwR%2B%2BW9iHA3Vm2G2nZoKVwVYaIuJJ0iEakuvY%2FN4etdg58%2FwKbRB6rQyjwM%2FcLIAS%2BkVY6JnF3ZVFZCaUc5GSem75LBujtE1lH3bTuKe5HqmZGAzLDTjw%2FveUv%2B54Df1cijxX878vcDQk3ZBl%2FCoxpv8IwquVecPXpxeBLOzzv82IDnWi%2B074H5y4HYmKY8rToJB7TUOvB%2BOqOyvowj8CAvQY6pgGjLbN3ZHQNfYBl5RYz%2FLICrxE6fK2A18xTTs5h87E%2BfgpPWlEJ0jPWB4cIknhu07Ptf%2FhMbdNXwYrq6De4KmN0HOZvf3k%2BdqZZgp%2FZxGZ0ZQEuWoVnJjbHpyMFOO5Tu2GW4GgpAoMH9Bb%2BraKbErQONkZuBYd8yTUQWcY83KKUrCZEuQhJTXttdLJghkrFagVjitEff2FreiGc%2BwY2SzmdrxYk7vIJ&X-Amz-Signature=596667cec1ab04d055a1bec4a348ea38aa4875dda741b8c5e183b60b22292226&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DHNMXHV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9rFEHZtQ%2FG7KinNLNAXtluzLJ20Rwopqj7K0U3ij%2BAAiBOhgrQ5xUUwZdvRklYgVuFiFYVZmFHc7Rh9ujvv4VWDCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMPktkowyAAHbwuddKtwDH5bG5Q7ZYuLtIrPgkwtN28ANI6BdRwg%2Fdj6ZceMS82kchqYiQZi0RZNM2Bigl3auzs4CdvANB%2Fh4krBunLbu4WIs7bM21uaIa4l7F%2B0gMwc4%2BLX3wivkL4kgc0VWpTjymICQ%2BOmZHL5adSnKGyFMqtIZxsT4s62k6cTY%2B5squo2SOtj2vsxHhkxE1bO5XT108j55Bl5AKdXos9pqUtVGRwvwdJNcQejJz0OLsgKWBZEYRrViItMePtDyuOMXQ4yVnNfeTvLKA0tE0W1GfLhPYNBQWLc5F9r2B6j14hDqAHSJJfBuNecAlqa67NnQtMh868VNWXLA8tOEcMILKYmBRwUXW%2FXOFaAqejLzKVBFZBG7898oBEbfaJVU3yEocZC7J9jrDqjLu3eptdTVIKJYG6fh975wk9Xlj4mxAE4O1jcwR%2B%2BW9iHA3Vm2G2nZoKVwVYaIuJJ0iEakuvY%2FN4etdg58%2FwKbRB6rQyjwM%2FcLIAS%2BkVY6JnF3ZVFZCaUc5GSem75LBujtE1lH3bTuKe5HqmZGAzLDTjw%2FveUv%2B54Df1cijxX878vcDQk3ZBl%2FCoxpv8IwquVecPXpxeBLOzzv82IDnWi%2B074H5y4HYmKY8rToJB7TUOvB%2BOqOyvowj8CAvQY6pgGjLbN3ZHQNfYBl5RYz%2FLICrxE6fK2A18xTTs5h87E%2BfgpPWlEJ0jPWB4cIknhu07Ptf%2FhMbdNXwYrq6De4KmN0HOZvf3k%2BdqZZgp%2FZxGZ0ZQEuWoVnJjbHpyMFOO5Tu2GW4GgpAoMH9Bb%2BraKbErQONkZuBYd8yTUQWcY83KKUrCZEuQhJTXttdLJghkrFagVjitEff2FreiGc%2BwY2SzmdrxYk7vIJ&X-Amz-Signature=4e971cfa99b55b1cc6480b761ec5a719b087f3a1733cd614fc7e10482371976b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVXECEH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDETOWtIKtkw6wf0CljLEPAL20YFHn3x7UghGa3dXJyvAIgTygc3hPqN1Np1RhJptGuRPLA8DyW8IAD3Hf6V5eEy%2FwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNX%2FdFpMtEEtLHNEKCrcA84tNjI%2FqgeVqwsYLnvbm0PVFWSa9FDXt5jU8sVt5TsKpTAwz05FAaVlEPP4qMag6UT5gHV4seClXOEwURniJ83yxI%2FuksXuJG7gKxiz0ZtJLrdGGWTE9aEmoSAoQPX%2FKsGUMDYcaQRyXG34x33kZmtRxZED3L76xRn8dKH9L5zj4RPnbSjNHLTgjQ7qwPhTvrjIDMnxe%2FfMYMj%2F0Jgl5Y42wyYwEhxTGH5xkzYjDjEpHTCc%2FGp%2FS0dAgIfBOkgDxoxibfC07p334MlszQBBODRwWwyqtMf1fcGZA3cU6n%2BVbkIXSEI0MU54MN09%2FKAQXHFU7afXEqjISyRp2ewMGgfm892QAOdyA5717em2hiuJtlm2Uq1PkwexZhXQT6E%2BE5840uczg9hI4QdigOS7LtLmXhBaUtHYj9CZrQAAGxu5xxsFuMqWKHCCkcOop%2FX9nYKIkpeBdzXnvuG1G%2FJTf9Bc36pwYLvG%2FyqOVA0Uw9l4tg2RNht26Dc1yvyXFymAIeEmW9Y22ojjrSwmS82O9hwhNhvWusYkSsErTTiGJtL3US99UAqEtTGC9t5oMXYfgCeCMPlDM%2F%2BOZPnVXBYHwyMHtGpY%2B%2FjdJ1fyVwfUrvGfHfjZLEnzxiY835mTMIq%2FgL0GOqUBYUOl723wzx02Vb04ZTsG3PKAD4rPNniJu7DwMsqTKdgaoZ4aMHffhwtWSHKc5XGNGDGeH4%2Fep%2BkjELUTGbhN9T%2FBljxBF6dSgmwR0QrSsdZUpFIpCUxE8rrGGf%2B4RMGDGeKLopom47dZwohH%2FhU8tnqlTtSytmbz4bL14lbJ%2F0M9G%2BN%2BYt1weVB9UL%2By9QSXDjuKtaBUBmfop7Wmj%2Brn%2F087wpje&X-Amz-Signature=2e7788a76adf84413f4c9d5ea5bebb5632cc77c3cb947903436516e5d861ffc9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVXECEH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDETOWtIKtkw6wf0CljLEPAL20YFHn3x7UghGa3dXJyvAIgTygc3hPqN1Np1RhJptGuRPLA8DyW8IAD3Hf6V5eEy%2FwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNX%2FdFpMtEEtLHNEKCrcA84tNjI%2FqgeVqwsYLnvbm0PVFWSa9FDXt5jU8sVt5TsKpTAwz05FAaVlEPP4qMag6UT5gHV4seClXOEwURniJ83yxI%2FuksXuJG7gKxiz0ZtJLrdGGWTE9aEmoSAoQPX%2FKsGUMDYcaQRyXG34x33kZmtRxZED3L76xRn8dKH9L5zj4RPnbSjNHLTgjQ7qwPhTvrjIDMnxe%2FfMYMj%2F0Jgl5Y42wyYwEhxTGH5xkzYjDjEpHTCc%2FGp%2FS0dAgIfBOkgDxoxibfC07p334MlszQBBODRwWwyqtMf1fcGZA3cU6n%2BVbkIXSEI0MU54MN09%2FKAQXHFU7afXEqjISyRp2ewMGgfm892QAOdyA5717em2hiuJtlm2Uq1PkwexZhXQT6E%2BE5840uczg9hI4QdigOS7LtLmXhBaUtHYj9CZrQAAGxu5xxsFuMqWKHCCkcOop%2FX9nYKIkpeBdzXnvuG1G%2FJTf9Bc36pwYLvG%2FyqOVA0Uw9l4tg2RNht26Dc1yvyXFymAIeEmW9Y22ojjrSwmS82O9hwhNhvWusYkSsErTTiGJtL3US99UAqEtTGC9t5oMXYfgCeCMPlDM%2F%2BOZPnVXBYHwyMHtGpY%2B%2FjdJ1fyVwfUrvGfHfjZLEnzxiY835mTMIq%2FgL0GOqUBYUOl723wzx02Vb04ZTsG3PKAD4rPNniJu7DwMsqTKdgaoZ4aMHffhwtWSHKc5XGNGDGeH4%2Fep%2BkjELUTGbhN9T%2FBljxBF6dSgmwR0QrSsdZUpFIpCUxE8rrGGf%2B4RMGDGeKLopom47dZwohH%2FhU8tnqlTtSytmbz4bL14lbJ%2F0M9G%2BN%2BYt1weVB9UL%2By9QSXDjuKtaBUBmfop7Wmj%2Brn%2F087wpje&X-Amz-Signature=e36535bd706728179d205d85ff26ff2588dfb7b439b29968a8283357b2dd000d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVXECEH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDETOWtIKtkw6wf0CljLEPAL20YFHn3x7UghGa3dXJyvAIgTygc3hPqN1Np1RhJptGuRPLA8DyW8IAD3Hf6V5eEy%2FwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNX%2FdFpMtEEtLHNEKCrcA84tNjI%2FqgeVqwsYLnvbm0PVFWSa9FDXt5jU8sVt5TsKpTAwz05FAaVlEPP4qMag6UT5gHV4seClXOEwURniJ83yxI%2FuksXuJG7gKxiz0ZtJLrdGGWTE9aEmoSAoQPX%2FKsGUMDYcaQRyXG34x33kZmtRxZED3L76xRn8dKH9L5zj4RPnbSjNHLTgjQ7qwPhTvrjIDMnxe%2FfMYMj%2F0Jgl5Y42wyYwEhxTGH5xkzYjDjEpHTCc%2FGp%2FS0dAgIfBOkgDxoxibfC07p334MlszQBBODRwWwyqtMf1fcGZA3cU6n%2BVbkIXSEI0MU54MN09%2FKAQXHFU7afXEqjISyRp2ewMGgfm892QAOdyA5717em2hiuJtlm2Uq1PkwexZhXQT6E%2BE5840uczg9hI4QdigOS7LtLmXhBaUtHYj9CZrQAAGxu5xxsFuMqWKHCCkcOop%2FX9nYKIkpeBdzXnvuG1G%2FJTf9Bc36pwYLvG%2FyqOVA0Uw9l4tg2RNht26Dc1yvyXFymAIeEmW9Y22ojjrSwmS82O9hwhNhvWusYkSsErTTiGJtL3US99UAqEtTGC9t5oMXYfgCeCMPlDM%2F%2BOZPnVXBYHwyMHtGpY%2B%2FjdJ1fyVwfUrvGfHfjZLEnzxiY835mTMIq%2FgL0GOqUBYUOl723wzx02Vb04ZTsG3PKAD4rPNniJu7DwMsqTKdgaoZ4aMHffhwtWSHKc5XGNGDGeH4%2Fep%2BkjELUTGbhN9T%2FBljxBF6dSgmwR0QrSsdZUpFIpCUxE8rrGGf%2B4RMGDGeKLopom47dZwohH%2FhU8tnqlTtSytmbz4bL14lbJ%2F0M9G%2BN%2BYt1weVB9UL%2By9QSXDjuKtaBUBmfop7Wmj%2Brn%2F087wpje&X-Amz-Signature=ef427f0d30a19b35c63cae28a6907f5baf1a7e1fbabdda54300b7a51f11c64cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVXECEH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDETOWtIKtkw6wf0CljLEPAL20YFHn3x7UghGa3dXJyvAIgTygc3hPqN1Np1RhJptGuRPLA8DyW8IAD3Hf6V5eEy%2FwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNX%2FdFpMtEEtLHNEKCrcA84tNjI%2FqgeVqwsYLnvbm0PVFWSa9FDXt5jU8sVt5TsKpTAwz05FAaVlEPP4qMag6UT5gHV4seClXOEwURniJ83yxI%2FuksXuJG7gKxiz0ZtJLrdGGWTE9aEmoSAoQPX%2FKsGUMDYcaQRyXG34x33kZmtRxZED3L76xRn8dKH9L5zj4RPnbSjNHLTgjQ7qwPhTvrjIDMnxe%2FfMYMj%2F0Jgl5Y42wyYwEhxTGH5xkzYjDjEpHTCc%2FGp%2FS0dAgIfBOkgDxoxibfC07p334MlszQBBODRwWwyqtMf1fcGZA3cU6n%2BVbkIXSEI0MU54MN09%2FKAQXHFU7afXEqjISyRp2ewMGgfm892QAOdyA5717em2hiuJtlm2Uq1PkwexZhXQT6E%2BE5840uczg9hI4QdigOS7LtLmXhBaUtHYj9CZrQAAGxu5xxsFuMqWKHCCkcOop%2FX9nYKIkpeBdzXnvuG1G%2FJTf9Bc36pwYLvG%2FyqOVA0Uw9l4tg2RNht26Dc1yvyXFymAIeEmW9Y22ojjrSwmS82O9hwhNhvWusYkSsErTTiGJtL3US99UAqEtTGC9t5oMXYfgCeCMPlDM%2F%2BOZPnVXBYHwyMHtGpY%2B%2FjdJ1fyVwfUrvGfHfjZLEnzxiY835mTMIq%2FgL0GOqUBYUOl723wzx02Vb04ZTsG3PKAD4rPNniJu7DwMsqTKdgaoZ4aMHffhwtWSHKc5XGNGDGeH4%2Fep%2BkjELUTGbhN9T%2FBljxBF6dSgmwR0QrSsdZUpFIpCUxE8rrGGf%2B4RMGDGeKLopom47dZwohH%2FhU8tnqlTtSytmbz4bL14lbJ%2F0M9G%2BN%2BYt1weVB9UL%2By9QSXDjuKtaBUBmfop7Wmj%2Brn%2F087wpje&X-Amz-Signature=a2d40a7025a7de9617c99cb5b437fa0fd5663d588f3c46706acaf0188cc6569e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVXECEH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDETOWtIKtkw6wf0CljLEPAL20YFHn3x7UghGa3dXJyvAIgTygc3hPqN1Np1RhJptGuRPLA8DyW8IAD3Hf6V5eEy%2FwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNX%2FdFpMtEEtLHNEKCrcA84tNjI%2FqgeVqwsYLnvbm0PVFWSa9FDXt5jU8sVt5TsKpTAwz05FAaVlEPP4qMag6UT5gHV4seClXOEwURniJ83yxI%2FuksXuJG7gKxiz0ZtJLrdGGWTE9aEmoSAoQPX%2FKsGUMDYcaQRyXG34x33kZmtRxZED3L76xRn8dKH9L5zj4RPnbSjNHLTgjQ7qwPhTvrjIDMnxe%2FfMYMj%2F0Jgl5Y42wyYwEhxTGH5xkzYjDjEpHTCc%2FGp%2FS0dAgIfBOkgDxoxibfC07p334MlszQBBODRwWwyqtMf1fcGZA3cU6n%2BVbkIXSEI0MU54MN09%2FKAQXHFU7afXEqjISyRp2ewMGgfm892QAOdyA5717em2hiuJtlm2Uq1PkwexZhXQT6E%2BE5840uczg9hI4QdigOS7LtLmXhBaUtHYj9CZrQAAGxu5xxsFuMqWKHCCkcOop%2FX9nYKIkpeBdzXnvuG1G%2FJTf9Bc36pwYLvG%2FyqOVA0Uw9l4tg2RNht26Dc1yvyXFymAIeEmW9Y22ojjrSwmS82O9hwhNhvWusYkSsErTTiGJtL3US99UAqEtTGC9t5oMXYfgCeCMPlDM%2F%2BOZPnVXBYHwyMHtGpY%2B%2FjdJ1fyVwfUrvGfHfjZLEnzxiY835mTMIq%2FgL0GOqUBYUOl723wzx02Vb04ZTsG3PKAD4rPNniJu7DwMsqTKdgaoZ4aMHffhwtWSHKc5XGNGDGeH4%2Fep%2BkjELUTGbhN9T%2FBljxBF6dSgmwR0QrSsdZUpFIpCUxE8rrGGf%2B4RMGDGeKLopom47dZwohH%2FhU8tnqlTtSytmbz4bL14lbJ%2F0M9G%2BN%2BYt1weVB9UL%2By9QSXDjuKtaBUBmfop7Wmj%2Brn%2F087wpje&X-Amz-Signature=fb504f455ef1f3b2cc299728483e35a189b2406a26edbee74bba1ca4656d43f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVXECEH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDETOWtIKtkw6wf0CljLEPAL20YFHn3x7UghGa3dXJyvAIgTygc3hPqN1Np1RhJptGuRPLA8DyW8IAD3Hf6V5eEy%2FwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNX%2FdFpMtEEtLHNEKCrcA84tNjI%2FqgeVqwsYLnvbm0PVFWSa9FDXt5jU8sVt5TsKpTAwz05FAaVlEPP4qMag6UT5gHV4seClXOEwURniJ83yxI%2FuksXuJG7gKxiz0ZtJLrdGGWTE9aEmoSAoQPX%2FKsGUMDYcaQRyXG34x33kZmtRxZED3L76xRn8dKH9L5zj4RPnbSjNHLTgjQ7qwPhTvrjIDMnxe%2FfMYMj%2F0Jgl5Y42wyYwEhxTGH5xkzYjDjEpHTCc%2FGp%2FS0dAgIfBOkgDxoxibfC07p334MlszQBBODRwWwyqtMf1fcGZA3cU6n%2BVbkIXSEI0MU54MN09%2FKAQXHFU7afXEqjISyRp2ewMGgfm892QAOdyA5717em2hiuJtlm2Uq1PkwexZhXQT6E%2BE5840uczg9hI4QdigOS7LtLmXhBaUtHYj9CZrQAAGxu5xxsFuMqWKHCCkcOop%2FX9nYKIkpeBdzXnvuG1G%2FJTf9Bc36pwYLvG%2FyqOVA0Uw9l4tg2RNht26Dc1yvyXFymAIeEmW9Y22ojjrSwmS82O9hwhNhvWusYkSsErTTiGJtL3US99UAqEtTGC9t5oMXYfgCeCMPlDM%2F%2BOZPnVXBYHwyMHtGpY%2B%2FjdJ1fyVwfUrvGfHfjZLEnzxiY835mTMIq%2FgL0GOqUBYUOl723wzx02Vb04ZTsG3PKAD4rPNniJu7DwMsqTKdgaoZ4aMHffhwtWSHKc5XGNGDGeH4%2Fep%2BkjELUTGbhN9T%2FBljxBF6dSgmwR0QrSsdZUpFIpCUxE8rrGGf%2B4RMGDGeKLopom47dZwohH%2FhU8tnqlTtSytmbz4bL14lbJ%2F0M9G%2BN%2BYt1weVB9UL%2By9QSXDjuKtaBUBmfop7Wmj%2Brn%2F087wpje&X-Amz-Signature=6749fee7fcc0082391565794ca3519a9eaa4e4fb8d8b67800705bc81cbd16830&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSRMKYBM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNgd%2FoTdhILw8NsuazMS8zfMv6eYGZVPVwcGv1A3Fr0wIgG1tSzMM3K5XD%2BwyBByKOP3CJBEgXxNSj9ofywmtv%2FqUqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO1ZP%2BQsryVU8On8gircA9pGu3CpHsjt77Xgf3rKxEcXcSA0JYH42fyCzmjUrZEOWOj5QjuLenNb%2FxvS9Zi0Voj2FgaG5xHs70fm7rUmHAXpM2KleR77123jmN%2BFf4cXnb1MyeuFsfG4IRSFYAaJ8FN9z72Jsrf45%2FTMGxdl2NU%2FJWv634YzhCDOAAsxfMvnAnTHJjoeJRnsRXT65P6RWENUCI76tRbxS03Pz5v%2BCpRpcWy00Est9%2Fov6B6Bm92Mtrc2rP1Td8ytZPM%2BHvLZCshhHizDpi8Uk7BNrWFrNKoEm2CT83J919DUWSefOVNmar44GqrB570SW1b7XkmyEGmyChkVCXZNItEXcNTZfEWfIcQ6jJQ%2BmfI07zO5GHliytoStFQhcO23gDy%2FCbjxoL9%2BtzzHY%2FTvX54YdAo5zaDQ69VJTSVTgacSJ7nHRvwKCyrfocVYsKrc7TshPpYrY6EPIYk5gS2Rno%2F2n%2Fzh5Voe9cS%2BP6iPmKzGeMlLA6WT4ouWqzmskP5hZQvlEs9k%2Ffimf5fBkLPDPhCkIE%2FqFWPoGsoJ1PQnhf%2FVZYHkjCQ1mTLreWRhSxpI7p6MJVHR%2FrEWhTDT2lQgf51Fl1Y%2F7e3zar3tMlZ59UDwZKLkcpbSsuOEkPPTJGL%2Fq8y1MLa%2FgL0GOqUBMnrLe8wBGIzMvAfem1tjaacgb0KaWDyfKXIdNc2NZet1CtYUo2YXr4OT1p4Ai7t0saydVeJ3pIavsW2CmeN%2BxiLmo1RbYPLzg3NK8yBYA0TQ%2FPOVbYaNiEmkcxfF5ZxEDHgILWGYn1BZVYmF76oZx8vHO%2FdD4jkqfkA4gMCHeHVUxQMbmlz2JkhaEQkce%2FnrrEwFRmgb%2BRRq6jXJwCsIeGkBO0S3&X-Amz-Signature=fdd6894878febf8ef4226d9cc46b712daf3d0a796b030f99b379f206e2d39b0f&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQD7JPCP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOU8Pr7KoijjArTVgW6faez9AFCSADApGpzEXG89vHvgIgFgr28Ka7GkUMiVahHbB%2B4iW1fcfWKmEG87%2B9Zg88pzsqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNU7tk2rzSsjoLLxLSrcAzM2KkSy1KSbeIiqIgxbn7GS7TobL5biiqwuk7a95jWEMxowGIrQ3UDvb2r9eNeCxLPzMkEX2JVen6nnCfQFjic%2BxCVK8LkLn66qZgyfXZGPOjyflikYWJ3S8pZPsdIJhKH7elPpIpqN6MZFwnxa6szHg3WwX9ArdZVIBGcZMYlltvjmHb862VM6PH2qk9bo378rb0ru4%2BjvBLYkJVBjXw0zX1VZVg8doo8cIhZkZHEknZ5PDM38D7kG8%2BcM7r%2FYnzcwLw1%2Be489lw%2BvKujAnRJzAFNMrB%2FOp3MKBOZrkLkBAfYhxhyfyOFsTHJ4GLyjZaKLwmMopZzI%2BC66%2FHcaMklSctLakwl%2B3f26FO07RaVqnbFM%2BvwibLsGOQINr%2FoLBmEELSR1NGuFw4690n0AuYrsA87t9r4TxsRK2NpgJzerTLmm9w26SjC7%2FrLmeNINt7PNBtgDFsO6qYa0O5DXENdG2bNdZDVgVMTa0a%2BGlWM6bs%2FKDmsw3GTBzOw2m95%2BvMjuqnniBTwlCuVc%2FT74%2BJihYeTmaBDC5Lugvd5xW1YfL6K0PanQaRLtcX6yIyKbF7uSUwRyoswUPTy36f5toUZwkjmEJjE6NoUX9GJV0Yx72nRQ6%2F%2FuUjFd%2B4B2MNW%2FgL0GOqUBLgGUdwobbTiXxmFv75sLVstDBEko%2B7SRBGTjL%2F9s4fum6e8MyMkJbEN63jW9zCkhme%2Bz1Fbt454YkBJgDAL9UQXkH9%2Fo2KgTik88AVOQXSRAfTo7rphFyo44idrkDDtK0WZIxId8j06UNzIcuP%2B6I8pTt5sBmOQZWJLl%2FxDJYpGlzurAbIXaNzqB8lIxcOPepPdDQ01VSIAfR1ceiq%2Bf9bCqThB3&X-Amz-Signature=1c9f0fdad292edcda247616cebad235c9c5af679da72015ef19d7fc60378deaa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVXECEH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDETOWtIKtkw6wf0CljLEPAL20YFHn3x7UghGa3dXJyvAIgTygc3hPqN1Np1RhJptGuRPLA8DyW8IAD3Hf6V5eEy%2FwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNX%2FdFpMtEEtLHNEKCrcA84tNjI%2FqgeVqwsYLnvbm0PVFWSa9FDXt5jU8sVt5TsKpTAwz05FAaVlEPP4qMag6UT5gHV4seClXOEwURniJ83yxI%2FuksXuJG7gKxiz0ZtJLrdGGWTE9aEmoSAoQPX%2FKsGUMDYcaQRyXG34x33kZmtRxZED3L76xRn8dKH9L5zj4RPnbSjNHLTgjQ7qwPhTvrjIDMnxe%2FfMYMj%2F0Jgl5Y42wyYwEhxTGH5xkzYjDjEpHTCc%2FGp%2FS0dAgIfBOkgDxoxibfC07p334MlszQBBODRwWwyqtMf1fcGZA3cU6n%2BVbkIXSEI0MU54MN09%2FKAQXHFU7afXEqjISyRp2ewMGgfm892QAOdyA5717em2hiuJtlm2Uq1PkwexZhXQT6E%2BE5840uczg9hI4QdigOS7LtLmXhBaUtHYj9CZrQAAGxu5xxsFuMqWKHCCkcOop%2FX9nYKIkpeBdzXnvuG1G%2FJTf9Bc36pwYLvG%2FyqOVA0Uw9l4tg2RNht26Dc1yvyXFymAIeEmW9Y22ojjrSwmS82O9hwhNhvWusYkSsErTTiGJtL3US99UAqEtTGC9t5oMXYfgCeCMPlDM%2F%2BOZPnVXBYHwyMHtGpY%2B%2FjdJ1fyVwfUrvGfHfjZLEnzxiY835mTMIq%2FgL0GOqUBYUOl723wzx02Vb04ZTsG3PKAD4rPNniJu7DwMsqTKdgaoZ4aMHffhwtWSHKc5XGNGDGeH4%2Fep%2BkjELUTGbhN9T%2FBljxBF6dSgmwR0QrSsdZUpFIpCUxE8rrGGf%2B4RMGDGeKLopom47dZwohH%2FhU8tnqlTtSytmbz4bL14lbJ%2F0M9G%2BN%2BYt1weVB9UL%2By9QSXDjuKtaBUBmfop7Wmj%2Brn%2F087wpje&X-Amz-Signature=eec4dc51471bce87131d1615df5c1a4527bcd4b226d2b1732109af601cbe4e2f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVXECEH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDETOWtIKtkw6wf0CljLEPAL20YFHn3x7UghGa3dXJyvAIgTygc3hPqN1Np1RhJptGuRPLA8DyW8IAD3Hf6V5eEy%2FwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNX%2FdFpMtEEtLHNEKCrcA84tNjI%2FqgeVqwsYLnvbm0PVFWSa9FDXt5jU8sVt5TsKpTAwz05FAaVlEPP4qMag6UT5gHV4seClXOEwURniJ83yxI%2FuksXuJG7gKxiz0ZtJLrdGGWTE9aEmoSAoQPX%2FKsGUMDYcaQRyXG34x33kZmtRxZED3L76xRn8dKH9L5zj4RPnbSjNHLTgjQ7qwPhTvrjIDMnxe%2FfMYMj%2F0Jgl5Y42wyYwEhxTGH5xkzYjDjEpHTCc%2FGp%2FS0dAgIfBOkgDxoxibfC07p334MlszQBBODRwWwyqtMf1fcGZA3cU6n%2BVbkIXSEI0MU54MN09%2FKAQXHFU7afXEqjISyRp2ewMGgfm892QAOdyA5717em2hiuJtlm2Uq1PkwexZhXQT6E%2BE5840uczg9hI4QdigOS7LtLmXhBaUtHYj9CZrQAAGxu5xxsFuMqWKHCCkcOop%2FX9nYKIkpeBdzXnvuG1G%2FJTf9Bc36pwYLvG%2FyqOVA0Uw9l4tg2RNht26Dc1yvyXFymAIeEmW9Y22ojjrSwmS82O9hwhNhvWusYkSsErTTiGJtL3US99UAqEtTGC9t5oMXYfgCeCMPlDM%2F%2BOZPnVXBYHwyMHtGpY%2B%2FjdJ1fyVwfUrvGfHfjZLEnzxiY835mTMIq%2FgL0GOqUBYUOl723wzx02Vb04ZTsG3PKAD4rPNniJu7DwMsqTKdgaoZ4aMHffhwtWSHKc5XGNGDGeH4%2Fep%2BkjELUTGbhN9T%2FBljxBF6dSgmwR0QrSsdZUpFIpCUxE8rrGGf%2B4RMGDGeKLopom47dZwohH%2FhU8tnqlTtSytmbz4bL14lbJ%2F0M9G%2BN%2BYt1weVB9UL%2By9QSXDjuKtaBUBmfop7Wmj%2Brn%2F087wpje&X-Amz-Signature=850fbbce01389d8f2f26ea783ff94ab0a3728fce686a431fe9736a972009bcbe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVXECEH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDETOWtIKtkw6wf0CljLEPAL20YFHn3x7UghGa3dXJyvAIgTygc3hPqN1Np1RhJptGuRPLA8DyW8IAD3Hf6V5eEy%2FwqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNX%2FdFpMtEEtLHNEKCrcA84tNjI%2FqgeVqwsYLnvbm0PVFWSa9FDXt5jU8sVt5TsKpTAwz05FAaVlEPP4qMag6UT5gHV4seClXOEwURniJ83yxI%2FuksXuJG7gKxiz0ZtJLrdGGWTE9aEmoSAoQPX%2FKsGUMDYcaQRyXG34x33kZmtRxZED3L76xRn8dKH9L5zj4RPnbSjNHLTgjQ7qwPhTvrjIDMnxe%2FfMYMj%2F0Jgl5Y42wyYwEhxTGH5xkzYjDjEpHTCc%2FGp%2FS0dAgIfBOkgDxoxibfC07p334MlszQBBODRwWwyqtMf1fcGZA3cU6n%2BVbkIXSEI0MU54MN09%2FKAQXHFU7afXEqjISyRp2ewMGgfm892QAOdyA5717em2hiuJtlm2Uq1PkwexZhXQT6E%2BE5840uczg9hI4QdigOS7LtLmXhBaUtHYj9CZrQAAGxu5xxsFuMqWKHCCkcOop%2FX9nYKIkpeBdzXnvuG1G%2FJTf9Bc36pwYLvG%2FyqOVA0Uw9l4tg2RNht26Dc1yvyXFymAIeEmW9Y22ojjrSwmS82O9hwhNhvWusYkSsErTTiGJtL3US99UAqEtTGC9t5oMXYfgCeCMPlDM%2F%2BOZPnVXBYHwyMHtGpY%2B%2FjdJ1fyVwfUrvGfHfjZLEnzxiY835mTMIq%2FgL0GOqUBYUOl723wzx02Vb04ZTsG3PKAD4rPNniJu7DwMsqTKdgaoZ4aMHffhwtWSHKc5XGNGDGeH4%2Fep%2BkjELUTGbhN9T%2FBljxBF6dSgmwR0QrSsdZUpFIpCUxE8rrGGf%2B4RMGDGeKLopom47dZwohH%2FhU8tnqlTtSytmbz4bL14lbJ%2F0M9G%2BN%2BYt1weVB9UL%2By9QSXDjuKtaBUBmfop7Wmj%2Brn%2F087wpje&X-Amz-Signature=b38ab39c0f659a1454d2236e1eb453cb46d14c16b7835ab259fad6df6fa1065c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TEU7E5Q%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCD48Wv68dgnk12sWjYScf0cnGg7b2SzJ8usZ6z%2BOTmMAIhAOyOcFsu9WB5o1CQUcMDjERe4PmE3MhH2fkO8VJhEeBNKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0kkIWCa9ZBOzc6VAq3AOgRUWzj0t6mNIWn%2BzkeBajLyZ%2FlbSH7OhPlrf6TsPOxYW195cWuPlsuhpMSPvg%2BM91RWJLCUykGru6Gp7PjaUluZloDuSeQoeVHwdSipI9MzfWpIpa6fjjV%2FZhssSqTmPQYmaUd1QjJjRUahymB2kIHUzg0R9Gj5jAJSuRXW3UsfdYFWk5zXaI10RcQMZllt%2B8zSAheHfL%2B7HhnVpdI9pcEiatYuuGby%2BHwXTOJe6mbOmGnBTeg8FbhwdXeupIxS6lhzvsh1%2Bvfw0o4QEHF43jW2oTXySVXWoAKMx11zJE8wvDdaRqjvXHSp%2FN8RG0JTxPOBQETVNzoCDcb8kQO0R1%2BzZ9lLKPKlGJVJD6QwcbvQ0aqZWi%2FobbVJ%2BisVCqFGIQbIOIgp0LmKHmFWozmBP00%2FPCk2zYfkkFODewioCemc5bDbt6qKgfao7IaABkrSBHh0oQZMHrgT%2Fa6JRD3jSPg6xGyMr%2BMdjIPwHh6FhMOfHE3JcUUZMZkrYaAyT4qwQPXh5T9cuO72veIw4XzVgZvWf2Ot5HlHoiCKVlCZhEhvLDwCJ%2B2llEwYtPBLl4H5Btl6h%2BKMiUzF9ySZSIr2eOQC2TgX9xhi%2FfYxsiR2E4PnmISLnH6gpzjD2pyTCRv4C9BjqkARZO94WCfkREnDpXYTXUoeEwgHeK2HgcppFd2u1V8CdCrt2aAUDirnSimgTx1P3%2BKOMepGVkQQbJqGYd5UGGy1PlCg%2BTP7ArKWbMU%2Bd29tDCbNueP1ePCa3Dp5p0PRqPF9N4LClmbjdB%2FoYzCRNW%2B4MfYEWGvoB5cSxukOeZxpXm0PccZ3gSHHpiB8QzTmOLSzQwHE2gwReCMmmM5sX3pgiqydPd&X-Amz-Signature=cfa55471afe9299163bfe2ff0c8ce528a9028570ad5d9ec32c70a2dd5bd3a2eb&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPZXNXLX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJhcf1Hjw1gYNB5IzkKEnQ%2BaOGKqFJT4LUVnW4Z3ADnwIhAMGx18Z2EYER%2FxRRqsLForquweRTC4Cf79%2BDXAc1CCBzKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYBCwJWIutZemNnBEq3AMtsNSOcrjHX70lJyNvVh%2BCWsBZPDemy8VV12lAcPJSqyeTS%2FHPp%2Byqn40FQ%2Bk4SySE8YjszJEzwmhsPw2UDKKU%2FLjSy%2Bwn4u1lFFec1uPaxzfu9mW3MoAqHKjo55jW5xVOcJhQCeDr7mChxCom1mGWXbVOCEeJcdkTMNjhk9lru8hED4nz7Bim7QJK0aR1pamSygqYYAUtEf1w6rgmLcZRnjKqQeStpsllyIcH5F4Zoh6FmvYkLTCPc%2FwSbDXN5G7UKyX7abxZBQwcuh1f6unPNbf64mN5Fb4Sj0hp7zgK9sM5v2q97Q9wC5oQVLNA2syEoQM4yF%2FXaeo%2FLxRLEzzoAuKoWdkKKQaQRszmL8WJHeqmIIVbFnE5XdD8BKJLG3K6CElqs1%2BvEkOqLZe3%2BPnIWqmTD%2F%2B5%2BjeNw2Bo7qlb003xEGUKeJTlkDaI4Xh2DoEjOUd5q048LYltlRGEmaoPOEHRdJiLVDtMMr2dx8lYwfw2mIhBZfjIMesUUbLPenhN9C1V38IZ0OPo6bhx%2B9eBxufQ%2BQRWrd0QMfEVBMcZ9cYe3Rc67qnICmu0fqb%2Ft1kaudwUBkQCJqCB18U8YwlfYWEU0sR6lppBvkOBY0s8hIluiGOj%2B4S8u5jfHTCSv4C9BjqkAUy%2BiogLXFTmNPoVvFiUwryfHhnR6UAwWH0do8%2FODLsyhXqbGSKf%2FYBrAG2Luq0HekFjBVrp2T%2Fa9rXEnOWLdCd3AsJOeDc8TkpQCC0KAvXLzvMMZH8Lrdjj7ut14yVJqz%2BhjskGayn2OIiiIEhcEqaHGUgUAAVxNmixtflT%2Brho%2FCYjHmdE%2B4E1PB1zT%2BU5EcHI3MZVAQejOT4neobcE%2BgMfiGZ&X-Amz-Signature=0cc5d3f8e893bdc591c2969eecc80de06036e8907ac4a8833cd4362cb56d7760&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UYJNDS3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtSivnqLg3QuHnlIiRsVxUQ7Pejgo8ZVh38Z%2BJYpdIUQIhAPu5mPDrAPkF2T8qU%2FGbXL%2FVZN0QqwOi3msf5MPNuqg3KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx83X2VN7CnpR6PLhQq3AMfOqBEAykfNCPK%2BDsUZWtfKJbnSe%2Fb7MUI7QLqqDF0FaGRrqXisHi9XVwduTX6C7nE0TYzn9ynuU20wfw5Lr47PS0pMExjDKFeEkGjnOeY7Xa9UJnmqz2bk2J5Nny48y%2BrB0u2ca3DannlVqW6qj48QHAyQf6ye2sNlWLVivHf3EGMxtw8Rss8sXpCUEARR5I1LU1%2BJVU0wSgawznOAxWRNgRg7FfBVx4xfYmequX4Yn%2FZHpxb9dqk4x4y7ILdgTKdpo6y07Z2fB4RWNXtx6sBmtS3LFuGTKQ%2BEV28FI7GKUmHJajHf8SYFoBQrT4X%2BCpFenmTSCf%2F71rwHeRnKrc9Wt%2B0ykgVjLoaOZ4gv%2BjR8qF6K9eRGo0XlezDzZjkfH3Nvrt1kSI9x6SZlZZBhlkbEH%2FwVmyiDNUvA83xL19gYpTfd0nbicXj5w9i4wRubyNVGycKnact11%2FM3RaLJyZ2WjB0pRXFciRiVpaVT1ODsXF%2Bat1dEitO6Qlz0bJpn4hk8x8SB1VdKJbkSWetUSR9Cp1142thWGQXtPpD8dMpxV5vARdQfnk9w8%2FycH%2FAMqBIyebWE4iOv7bCKkqjaF%2BT9sb5PqcRrdM9k2iQaIeDTzre%2BWO5M7SOG4FdhDC%2BwIC9BjqkAYMXqkM%2BGAvdzzkXwAMhpq8muBnX6L3rrUZAdg7w%2BgacRap%2F79cFGjbWXxZspKWWc9%2F2eKXSiDo%2Bv28g%2BvVIX8UQRAXzblORre2cCSAKGlE%2Bn%2FGiLmHdY4YvufmBENl7Zgy9DsOQ1rFmWjCTiJAPn7KAr6qcKpIfkBC%2BUJURTeXq2JW0T8WFIgkrriOWh%2FEXMFJS7nqdCMZGtGfDaJlOJksEfyqv&X-Amz-Signature=0895b52dba36a904186ec385fca512489d1a48a2773c8145589b2f91e79e2112&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDINN7T2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYrZy7RpZtBkHlB2AU7pGAMHI37G%2FoyG%2FnP3srP3uwUQIhAPK7ErGPVs7j0qJ7%2FErWIOwztlCnpzHp%2BWnBOitdhoE2KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzO73LCLhQ1xplL6fQq3AON%2Bc16SEnRnPnQjGXSlfU7zTdTOea8rfI%2FjCSLymr1okaSgQtCGnm5CLnseEnkRGCrpwIAPQ8wR5T6rdJ3uOrztqSR%2B2iPtw5hFZNi10JUvKk%2FIr9lFf6fhc9%2BD8EHdHtjzE3f6MKvAQK1q2KpAgjaKBpjsIa4UpEK9toaGiexRJIpe2UpnP9357%2FzvsEPPtqjLe3ndChSMrOKbH3KQjqYGE30ylcSpqFDsETRTRKSULp%2BfIpiAYrrgWyNtHumehzIieSuXhzWgy%2FPoeCmGgkiLnQAul2MknretjY5lERj0jsrSQBAaZ%2FnZqCVwOyxHjSdSje8o28nB2m7M1H06y4cKicjOKc5O3GZ8TuIuFCjlsdIOsOsWe3tqsYVNyVKwCt68RolUYeLKw3cg79I25KPvk%2FPe9NYM9ViFwgAimHsjADhjuRkfJGOTABnElLUjjHEmez8jxH36UMFpMK6fSP5HntSZ4CMa250KgWnjS2YgoODD1zmB5KSKEMQeeRcXppylffJ4%2BAOGdBP6Jh6H6vgckYLJpbL%2FOnSAm40PHrjseFQYYMn6AxjMA5%2Fy7DbNU%2BibmYuQPCp%2Bb2JHejnbJmo1LCCjQuT6rrWYY%2B%2Bb%2F8uGOKAtYOk%2FZeTIxVcpzDWv4C9BjqkAe4p2v48PC5wAkmjK4ThIZiHL5RXW%2FVcMgjxCEXjXiORqJMKCdZDJpRsalKe5qgh4F8%2BRAj52GaS7mksnumG%2B1or4f1DX3jsJiQx2OuExcrmfbM%2Bew%2BuVJ5clY5pKLSU2ovenp0iMfgNKse1CxKwXnOFgecp16%2BUl%2BMF%2BPVIlMS146uyb4%2B%2B%2FIBP3IDkGrtZZpJarmypVT8YV51C31rgLfWenxvb&X-Amz-Signature=dad25f54a0f3728b62e30aa715d55d315470a0bb1118ae6cf3483e51c40e37cc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDINN7T2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYrZy7RpZtBkHlB2AU7pGAMHI37G%2FoyG%2FnP3srP3uwUQIhAPK7ErGPVs7j0qJ7%2FErWIOwztlCnpzHp%2BWnBOitdhoE2KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzO73LCLhQ1xplL6fQq3AON%2Bc16SEnRnPnQjGXSlfU7zTdTOea8rfI%2FjCSLymr1okaSgQtCGnm5CLnseEnkRGCrpwIAPQ8wR5T6rdJ3uOrztqSR%2B2iPtw5hFZNi10JUvKk%2FIr9lFf6fhc9%2BD8EHdHtjzE3f6MKvAQK1q2KpAgjaKBpjsIa4UpEK9toaGiexRJIpe2UpnP9357%2FzvsEPPtqjLe3ndChSMrOKbH3KQjqYGE30ylcSpqFDsETRTRKSULp%2BfIpiAYrrgWyNtHumehzIieSuXhzWgy%2FPoeCmGgkiLnQAul2MknretjY5lERj0jsrSQBAaZ%2FnZqCVwOyxHjSdSje8o28nB2m7M1H06y4cKicjOKc5O3GZ8TuIuFCjlsdIOsOsWe3tqsYVNyVKwCt68RolUYeLKw3cg79I25KPvk%2FPe9NYM9ViFwgAimHsjADhjuRkfJGOTABnElLUjjHEmez8jxH36UMFpMK6fSP5HntSZ4CMa250KgWnjS2YgoODD1zmB5KSKEMQeeRcXppylffJ4%2BAOGdBP6Jh6H6vgckYLJpbL%2FOnSAm40PHrjseFQYYMn6AxjMA5%2Fy7DbNU%2BibmYuQPCp%2Bb2JHejnbJmo1LCCjQuT6rrWYY%2B%2Bb%2F8uGOKAtYOk%2FZeTIxVcpzDWv4C9BjqkAe4p2v48PC5wAkmjK4ThIZiHL5RXW%2FVcMgjxCEXjXiORqJMKCdZDJpRsalKe5qgh4F8%2BRAj52GaS7mksnumG%2B1or4f1DX3jsJiQx2OuExcrmfbM%2Bew%2BuVJ5clY5pKLSU2ovenp0iMfgNKse1CxKwXnOFgecp16%2BUl%2BMF%2BPVIlMS146uyb4%2B%2B%2FIBP3IDkGrtZZpJarmypVT8YV51C31rgLfWenxvb&X-Amz-Signature=4eacb71abc57323002be1d5556f39b659c967bb1c3fe989dc7367a1c095d3697&X-Amz-SignedHeaders=host&x-id=GetObject)

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
