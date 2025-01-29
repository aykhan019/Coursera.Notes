

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TC2PWQ7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHN8EBHKfLfBIurvH8n214UTSiFOYuu2%2FDgw0FMxk%2BsJAiEArRuZvaV04FkadulVYCO%2F7WHUl9pJ3Sgr4Y1VpWgpBrsqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzR4utkuPgrRUXyoCrcA59wWxEpjk5XOEk0N1OPH%2FyrVBfH94dQv0YqgM5DmKcPWk%2FrFw2MKLLB4EaQtEv4rYhVWQY8u1w910Ew%2FQgFGCK8nPc2JLjjh5HLjB8%2F3GZ3apKPfNAWJuXMPycmu6hQ6cjDRQqF07yHnFuhJo8XKUsxKOpg4TY8RcFTDYVbxWgZ5QZaULOb3KPQNXLrno9hAdvKRNbJxM1KmiI8GhYP%2BmWokSf6FO78r%2Bhqfy40N7oRxf3IDZaudvA4%2F29qtSbrfw7%2F7EJqI2b4xe7Lo%2FHBYaHDm2KGRfPILoaxaD8nvC%2BWsLhukZ4Y%2BYa%2Fk7yAqXnQ8JAaTSguKGgH8PKpZivPoXGzw%2FzFg0cckbMUIjGMpWs1lET1M0woBGAgc4PSyohZuh2iJqA7WEYnSg%2BlpMyusJlDfbQtCUQLKqWRltrlrQlMGyrOYn51vsrcV7MJvy4Nag4TdR6%2F6lL%2BZNUIBK3nTRbPZ9HDJIiycUiM8cdbJCEJpdUEG4Yp5d2vUJ9jNzRhk0pY0asOrFMIU8iE5DsJ8sjKXT6F4vhCRwd2AZTA3qPjtVF4wd8EjFUCnjvL75XzePAHKj9zL6TosA%2B7%2FexXQvrsngNYG3kvBH8xUJtu3BuYpxws4S53CvrlkL2WMI6g5rwGOqUB9IxEPDKXSO2Ln%2FIHrpjFOAq%2B67OAwdWqZ6Obiy2OnydvVommEFOFQ%2B%2BpoCYWznOw4ODOzukYMfymheGbVawfCQv3i49d6Rpii6HG447EbFNg6FBrKm7ykvsyAufBaluqqoc6twleAxvWH%2F%2BUZAwLGK5pgE%2FN6JDTvkTJelgK8QYWaVksSU2n7NBK7RPcFkF03sQ6i%2F%2FeP9pb%2BWXBrNxd0%2F9kFlZ2&X-Amz-Signature=160c88d05801504c96ecb8e512b8e4952ef8ddb8b270a4e3f9fd9c7b02ebe3ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TC2PWQ7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHN8EBHKfLfBIurvH8n214UTSiFOYuu2%2FDgw0FMxk%2BsJAiEArRuZvaV04FkadulVYCO%2F7WHUl9pJ3Sgr4Y1VpWgpBrsqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzR4utkuPgrRUXyoCrcA59wWxEpjk5XOEk0N1OPH%2FyrVBfH94dQv0YqgM5DmKcPWk%2FrFw2MKLLB4EaQtEv4rYhVWQY8u1w910Ew%2FQgFGCK8nPc2JLjjh5HLjB8%2F3GZ3apKPfNAWJuXMPycmu6hQ6cjDRQqF07yHnFuhJo8XKUsxKOpg4TY8RcFTDYVbxWgZ5QZaULOb3KPQNXLrno9hAdvKRNbJxM1KmiI8GhYP%2BmWokSf6FO78r%2Bhqfy40N7oRxf3IDZaudvA4%2F29qtSbrfw7%2F7EJqI2b4xe7Lo%2FHBYaHDm2KGRfPILoaxaD8nvC%2BWsLhukZ4Y%2BYa%2Fk7yAqXnQ8JAaTSguKGgH8PKpZivPoXGzw%2FzFg0cckbMUIjGMpWs1lET1M0woBGAgc4PSyohZuh2iJqA7WEYnSg%2BlpMyusJlDfbQtCUQLKqWRltrlrQlMGyrOYn51vsrcV7MJvy4Nag4TdR6%2F6lL%2BZNUIBK3nTRbPZ9HDJIiycUiM8cdbJCEJpdUEG4Yp5d2vUJ9jNzRhk0pY0asOrFMIU8iE5DsJ8sjKXT6F4vhCRwd2AZTA3qPjtVF4wd8EjFUCnjvL75XzePAHKj9zL6TosA%2B7%2FexXQvrsngNYG3kvBH8xUJtu3BuYpxws4S53CvrlkL2WMI6g5rwGOqUB9IxEPDKXSO2Ln%2FIHrpjFOAq%2B67OAwdWqZ6Obiy2OnydvVommEFOFQ%2B%2BpoCYWznOw4ODOzukYMfymheGbVawfCQv3i49d6Rpii6HG447EbFNg6FBrKm7ykvsyAufBaluqqoc6twleAxvWH%2F%2BUZAwLGK5pgE%2FN6JDTvkTJelgK8QYWaVksSU2n7NBK7RPcFkF03sQ6i%2F%2FeP9pb%2BWXBrNxd0%2F9kFlZ2&X-Amz-Signature=054c6d8a4004b2b526bb66a1e15bff1804ba7ddab0d6f0798ea8345a6ecc9cc8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TC2PWQ7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHN8EBHKfLfBIurvH8n214UTSiFOYuu2%2FDgw0FMxk%2BsJAiEArRuZvaV04FkadulVYCO%2F7WHUl9pJ3Sgr4Y1VpWgpBrsqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzR4utkuPgrRUXyoCrcA59wWxEpjk5XOEk0N1OPH%2FyrVBfH94dQv0YqgM5DmKcPWk%2FrFw2MKLLB4EaQtEv4rYhVWQY8u1w910Ew%2FQgFGCK8nPc2JLjjh5HLjB8%2F3GZ3apKPfNAWJuXMPycmu6hQ6cjDRQqF07yHnFuhJo8XKUsxKOpg4TY8RcFTDYVbxWgZ5QZaULOb3KPQNXLrno9hAdvKRNbJxM1KmiI8GhYP%2BmWokSf6FO78r%2Bhqfy40N7oRxf3IDZaudvA4%2F29qtSbrfw7%2F7EJqI2b4xe7Lo%2FHBYaHDm2KGRfPILoaxaD8nvC%2BWsLhukZ4Y%2BYa%2Fk7yAqXnQ8JAaTSguKGgH8PKpZivPoXGzw%2FzFg0cckbMUIjGMpWs1lET1M0woBGAgc4PSyohZuh2iJqA7WEYnSg%2BlpMyusJlDfbQtCUQLKqWRltrlrQlMGyrOYn51vsrcV7MJvy4Nag4TdR6%2F6lL%2BZNUIBK3nTRbPZ9HDJIiycUiM8cdbJCEJpdUEG4Yp5d2vUJ9jNzRhk0pY0asOrFMIU8iE5DsJ8sjKXT6F4vhCRwd2AZTA3qPjtVF4wd8EjFUCnjvL75XzePAHKj9zL6TosA%2B7%2FexXQvrsngNYG3kvBH8xUJtu3BuYpxws4S53CvrlkL2WMI6g5rwGOqUB9IxEPDKXSO2Ln%2FIHrpjFOAq%2B67OAwdWqZ6Obiy2OnydvVommEFOFQ%2B%2BpoCYWznOw4ODOzukYMfymheGbVawfCQv3i49d6Rpii6HG447EbFNg6FBrKm7ykvsyAufBaluqqoc6twleAxvWH%2F%2BUZAwLGK5pgE%2FN6JDTvkTJelgK8QYWaVksSU2n7NBK7RPcFkF03sQ6i%2F%2FeP9pb%2BWXBrNxd0%2F9kFlZ2&X-Amz-Signature=70130bab9e3971d1a48ba3267410c7a3d0aa682b6e6aa269e1c275347096b839&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6RR2HS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICqHcywVCVedZAsZhjMi9QqpvTW%2B%2BhyfIKHxJb13WpJ5AiAj47lJHyOXCNoX3rfgmm3lQCm3O5vukivbk%2FjlKA5zKSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2d1%2B%2F4rs1yJuM46PKtwDFFXgcKcv2d0oFprUKB%2BtA4DHJS4Uvi26aSyTvFFpiVPMLTEQ7V2zpIXDOmOPfcN2%2FD%2FMcJvIksEAJHoP5nP4N8mE3tCCfeAm2H0mDmUX%2FG9rhq%2Frhe4ek4%2FPwgY2z0fX3STGXHOoLn2J2uMX5u6CkWyb1P6fwD0ZHx1dwLkVLh6QNsAd%2F3o%2B3qQQTM3gO3xq8YuKY6WwKb0rceSgfkv%2FKV9G1V0wsWs4LQayPrWDfPUdZB%2BLfGgZBYl0S9bHOyt0bfywL8rqEvkoA6eZYpbnSj1ENwijU6ncipazxy%2B08iyyzHnRy17NzEn1YkMuXIr8reCczEMxAV1G4PKRutDkGJLbVIY1kaoTGQR8RUSaV5yuDDLmwSN1%2FluWwkZ5tbl%2BtrTNXGDYEtFF5LlvXKftcKEqCegWv027w%2BO9NCZ3N5EPOnXjUId%2BMsjruffM77sp7od3iXvysN07JifL1HJM6uKY9iWpRF5TnxABjCHtThnG2aJN2x3%2B6W%2BaS1NUG%2B7CHuP1wYtLo89%2BRs6VbGnCqpGEuQ9lAO8PvzmJwWzW%2Fi9M9F%2FfxQUlCO4V70ssyVEKjS%2F9pdfo9ioXFeIwo0FWn4IOt9VAxXXtMC7Tzpbvp9MyefvCv2vAC8El8U4wmqDmvAY6pgGcflXRtiwx%2BuyvKaHXwAVPBjb7bGEYLatTIskJp%2F9NkzTsTYM4XU%2FhCkuiony5SJAgRj55wfSHNgLipxWquSaNPLLNxVmeyg02sSnrtw7NmIxC4zS6FUlP%2Fh962rQ%2FBkTiOAUKhHbqn1CHFHar44KxHhjPqXLNaGjGa6D6Ac%2BhK5RPL4QRY8xQKgaruEIBAt3zmQHnl7Mg98MYgSAWpnYm6H2OIshi&X-Amz-Signature=8bbf1d5db6682a57440ad0c2cf01e662b30e94ea128779080164340347ad58b5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6RR2HS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICqHcywVCVedZAsZhjMi9QqpvTW%2B%2BhyfIKHxJb13WpJ5AiAj47lJHyOXCNoX3rfgmm3lQCm3O5vukivbk%2FjlKA5zKSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2d1%2B%2F4rs1yJuM46PKtwDFFXgcKcv2d0oFprUKB%2BtA4DHJS4Uvi26aSyTvFFpiVPMLTEQ7V2zpIXDOmOPfcN2%2FD%2FMcJvIksEAJHoP5nP4N8mE3tCCfeAm2H0mDmUX%2FG9rhq%2Frhe4ek4%2FPwgY2z0fX3STGXHOoLn2J2uMX5u6CkWyb1P6fwD0ZHx1dwLkVLh6QNsAd%2F3o%2B3qQQTM3gO3xq8YuKY6WwKb0rceSgfkv%2FKV9G1V0wsWs4LQayPrWDfPUdZB%2BLfGgZBYl0S9bHOyt0bfywL8rqEvkoA6eZYpbnSj1ENwijU6ncipazxy%2B08iyyzHnRy17NzEn1YkMuXIr8reCczEMxAV1G4PKRutDkGJLbVIY1kaoTGQR8RUSaV5yuDDLmwSN1%2FluWwkZ5tbl%2BtrTNXGDYEtFF5LlvXKftcKEqCegWv027w%2BO9NCZ3N5EPOnXjUId%2BMsjruffM77sp7od3iXvysN07JifL1HJM6uKY9iWpRF5TnxABjCHtThnG2aJN2x3%2B6W%2BaS1NUG%2B7CHuP1wYtLo89%2BRs6VbGnCqpGEuQ9lAO8PvzmJwWzW%2Fi9M9F%2FfxQUlCO4V70ssyVEKjS%2F9pdfo9ioXFeIwo0FWn4IOt9VAxXXtMC7Tzpbvp9MyefvCv2vAC8El8U4wmqDmvAY6pgGcflXRtiwx%2BuyvKaHXwAVPBjb7bGEYLatTIskJp%2F9NkzTsTYM4XU%2FhCkuiony5SJAgRj55wfSHNgLipxWquSaNPLLNxVmeyg02sSnrtw7NmIxC4zS6FUlP%2Fh962rQ%2FBkTiOAUKhHbqn1CHFHar44KxHhjPqXLNaGjGa6D6Ac%2BhK5RPL4QRY8xQKgaruEIBAt3zmQHnl7Mg98MYgSAWpnYm6H2OIshi&X-Amz-Signature=1cde2ac85911f01a29bb9f59e67dc20490681a03977c0ff0bd7ac57f60f3a989&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6RR2HS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICqHcywVCVedZAsZhjMi9QqpvTW%2B%2BhyfIKHxJb13WpJ5AiAj47lJHyOXCNoX3rfgmm3lQCm3O5vukivbk%2FjlKA5zKSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2d1%2B%2F4rs1yJuM46PKtwDFFXgcKcv2d0oFprUKB%2BtA4DHJS4Uvi26aSyTvFFpiVPMLTEQ7V2zpIXDOmOPfcN2%2FD%2FMcJvIksEAJHoP5nP4N8mE3tCCfeAm2H0mDmUX%2FG9rhq%2Frhe4ek4%2FPwgY2z0fX3STGXHOoLn2J2uMX5u6CkWyb1P6fwD0ZHx1dwLkVLh6QNsAd%2F3o%2B3qQQTM3gO3xq8YuKY6WwKb0rceSgfkv%2FKV9G1V0wsWs4LQayPrWDfPUdZB%2BLfGgZBYl0S9bHOyt0bfywL8rqEvkoA6eZYpbnSj1ENwijU6ncipazxy%2B08iyyzHnRy17NzEn1YkMuXIr8reCczEMxAV1G4PKRutDkGJLbVIY1kaoTGQR8RUSaV5yuDDLmwSN1%2FluWwkZ5tbl%2BtrTNXGDYEtFF5LlvXKftcKEqCegWv027w%2BO9NCZ3N5EPOnXjUId%2BMsjruffM77sp7od3iXvysN07JifL1HJM6uKY9iWpRF5TnxABjCHtThnG2aJN2x3%2B6W%2BaS1NUG%2B7CHuP1wYtLo89%2BRs6VbGnCqpGEuQ9lAO8PvzmJwWzW%2Fi9M9F%2FfxQUlCO4V70ssyVEKjS%2F9pdfo9ioXFeIwo0FWn4IOt9VAxXXtMC7Tzpbvp9MyefvCv2vAC8El8U4wmqDmvAY6pgGcflXRtiwx%2BuyvKaHXwAVPBjb7bGEYLatTIskJp%2F9NkzTsTYM4XU%2FhCkuiony5SJAgRj55wfSHNgLipxWquSaNPLLNxVmeyg02sSnrtw7NmIxC4zS6FUlP%2Fh962rQ%2FBkTiOAUKhHbqn1CHFHar44KxHhjPqXLNaGjGa6D6Ac%2BhK5RPL4QRY8xQKgaruEIBAt3zmQHnl7Mg98MYgSAWpnYm6H2OIshi&X-Amz-Signature=61f98efbcb3eebcb6e733b69ed3d1a8eb8cf250dc1bd6ce4d6d6cacedbb70f1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6RR2HS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICqHcywVCVedZAsZhjMi9QqpvTW%2B%2BhyfIKHxJb13WpJ5AiAj47lJHyOXCNoX3rfgmm3lQCm3O5vukivbk%2FjlKA5zKSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2d1%2B%2F4rs1yJuM46PKtwDFFXgcKcv2d0oFprUKB%2BtA4DHJS4Uvi26aSyTvFFpiVPMLTEQ7V2zpIXDOmOPfcN2%2FD%2FMcJvIksEAJHoP5nP4N8mE3tCCfeAm2H0mDmUX%2FG9rhq%2Frhe4ek4%2FPwgY2z0fX3STGXHOoLn2J2uMX5u6CkWyb1P6fwD0ZHx1dwLkVLh6QNsAd%2F3o%2B3qQQTM3gO3xq8YuKY6WwKb0rceSgfkv%2FKV9G1V0wsWs4LQayPrWDfPUdZB%2BLfGgZBYl0S9bHOyt0bfywL8rqEvkoA6eZYpbnSj1ENwijU6ncipazxy%2B08iyyzHnRy17NzEn1YkMuXIr8reCczEMxAV1G4PKRutDkGJLbVIY1kaoTGQR8RUSaV5yuDDLmwSN1%2FluWwkZ5tbl%2BtrTNXGDYEtFF5LlvXKftcKEqCegWv027w%2BO9NCZ3N5EPOnXjUId%2BMsjruffM77sp7od3iXvysN07JifL1HJM6uKY9iWpRF5TnxABjCHtThnG2aJN2x3%2B6W%2BaS1NUG%2B7CHuP1wYtLo89%2BRs6VbGnCqpGEuQ9lAO8PvzmJwWzW%2Fi9M9F%2FfxQUlCO4V70ssyVEKjS%2F9pdfo9ioXFeIwo0FWn4IOt9VAxXXtMC7Tzpbvp9MyefvCv2vAC8El8U4wmqDmvAY6pgGcflXRtiwx%2BuyvKaHXwAVPBjb7bGEYLatTIskJp%2F9NkzTsTYM4XU%2FhCkuiony5SJAgRj55wfSHNgLipxWquSaNPLLNxVmeyg02sSnrtw7NmIxC4zS6FUlP%2Fh962rQ%2FBkTiOAUKhHbqn1CHFHar44KxHhjPqXLNaGjGa6D6Ac%2BhK5RPL4QRY8xQKgaruEIBAt3zmQHnl7Mg98MYgSAWpnYm6H2OIshi&X-Amz-Signature=7100394f478ee682e0ec4d08bbc555bb4da84e39eae99f24af10df5bb3ac77cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6RR2HS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICqHcywVCVedZAsZhjMi9QqpvTW%2B%2BhyfIKHxJb13WpJ5AiAj47lJHyOXCNoX3rfgmm3lQCm3O5vukivbk%2FjlKA5zKSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2d1%2B%2F4rs1yJuM46PKtwDFFXgcKcv2d0oFprUKB%2BtA4DHJS4Uvi26aSyTvFFpiVPMLTEQ7V2zpIXDOmOPfcN2%2FD%2FMcJvIksEAJHoP5nP4N8mE3tCCfeAm2H0mDmUX%2FG9rhq%2Frhe4ek4%2FPwgY2z0fX3STGXHOoLn2J2uMX5u6CkWyb1P6fwD0ZHx1dwLkVLh6QNsAd%2F3o%2B3qQQTM3gO3xq8YuKY6WwKb0rceSgfkv%2FKV9G1V0wsWs4LQayPrWDfPUdZB%2BLfGgZBYl0S9bHOyt0bfywL8rqEvkoA6eZYpbnSj1ENwijU6ncipazxy%2B08iyyzHnRy17NzEn1YkMuXIr8reCczEMxAV1G4PKRutDkGJLbVIY1kaoTGQR8RUSaV5yuDDLmwSN1%2FluWwkZ5tbl%2BtrTNXGDYEtFF5LlvXKftcKEqCegWv027w%2BO9NCZ3N5EPOnXjUId%2BMsjruffM77sp7od3iXvysN07JifL1HJM6uKY9iWpRF5TnxABjCHtThnG2aJN2x3%2B6W%2BaS1NUG%2B7CHuP1wYtLo89%2BRs6VbGnCqpGEuQ9lAO8PvzmJwWzW%2Fi9M9F%2FfxQUlCO4V70ssyVEKjS%2F9pdfo9ioXFeIwo0FWn4IOt9VAxXXtMC7Tzpbvp9MyefvCv2vAC8El8U4wmqDmvAY6pgGcflXRtiwx%2BuyvKaHXwAVPBjb7bGEYLatTIskJp%2F9NkzTsTYM4XU%2FhCkuiony5SJAgRj55wfSHNgLipxWquSaNPLLNxVmeyg02sSnrtw7NmIxC4zS6FUlP%2Fh962rQ%2FBkTiOAUKhHbqn1CHFHar44KxHhjPqXLNaGjGa6D6Ac%2BhK5RPL4QRY8xQKgaruEIBAt3zmQHnl7Mg98MYgSAWpnYm6H2OIshi&X-Amz-Signature=c4148616e52e9f9f9e4ede6e8b65fac5e98084bae30830b465b86d901260c3ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6RR2HS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICqHcywVCVedZAsZhjMi9QqpvTW%2B%2BhyfIKHxJb13WpJ5AiAj47lJHyOXCNoX3rfgmm3lQCm3O5vukivbk%2FjlKA5zKSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2d1%2B%2F4rs1yJuM46PKtwDFFXgcKcv2d0oFprUKB%2BtA4DHJS4Uvi26aSyTvFFpiVPMLTEQ7V2zpIXDOmOPfcN2%2FD%2FMcJvIksEAJHoP5nP4N8mE3tCCfeAm2H0mDmUX%2FG9rhq%2Frhe4ek4%2FPwgY2z0fX3STGXHOoLn2J2uMX5u6CkWyb1P6fwD0ZHx1dwLkVLh6QNsAd%2F3o%2B3qQQTM3gO3xq8YuKY6WwKb0rceSgfkv%2FKV9G1V0wsWs4LQayPrWDfPUdZB%2BLfGgZBYl0S9bHOyt0bfywL8rqEvkoA6eZYpbnSj1ENwijU6ncipazxy%2B08iyyzHnRy17NzEn1YkMuXIr8reCczEMxAV1G4PKRutDkGJLbVIY1kaoTGQR8RUSaV5yuDDLmwSN1%2FluWwkZ5tbl%2BtrTNXGDYEtFF5LlvXKftcKEqCegWv027w%2BO9NCZ3N5EPOnXjUId%2BMsjruffM77sp7od3iXvysN07JifL1HJM6uKY9iWpRF5TnxABjCHtThnG2aJN2x3%2B6W%2BaS1NUG%2B7CHuP1wYtLo89%2BRs6VbGnCqpGEuQ9lAO8PvzmJwWzW%2Fi9M9F%2FfxQUlCO4V70ssyVEKjS%2F9pdfo9ioXFeIwo0FWn4IOt9VAxXXtMC7Tzpbvp9MyefvCv2vAC8El8U4wmqDmvAY6pgGcflXRtiwx%2BuyvKaHXwAVPBjb7bGEYLatTIskJp%2F9NkzTsTYM4XU%2FhCkuiony5SJAgRj55wfSHNgLipxWquSaNPLLNxVmeyg02sSnrtw7NmIxC4zS6FUlP%2Fh962rQ%2FBkTiOAUKhHbqn1CHFHar44KxHhjPqXLNaGjGa6D6Ac%2BhK5RPL4QRY8xQKgaruEIBAt3zmQHnl7Mg98MYgSAWpnYm6H2OIshi&X-Amz-Signature=3edadeab460c809bd026828a468d0e9a31a21ee129507176317b4fa15f41e721&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYXLMMFI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFM2EK%2BZKrcYUd20VqgQmpzBeHaY85W4hV8jNWfF1dEVAiEAoUTEf8%2BM8XZvoxfymcc0G4hRYLiQS3Znt%2FsBslrhXZMqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLQy0kIcu6PsLjEmfSrcAyOGYF0BDmpLUyJD9sT051zeqAeiUtPQfvlHahK%2BQtdljozLHQk3G3kzsT4OkueZWISx%2BtrW5qlPLjFwTY6iOFAlKtyYKcLgstLmNlw4KLwDFs2EbUyzXT0FAasHTwGlo0UD96GFw%2BsrGcJg5qC%2FEJmyb4s%2FMEY%2BqwcZQHWrmbGojtIgrlgref0pAPXMZVk%2Foz86QxYQChSrH34VBFAeBQXTyQUZb3tmOHK7rRud2Hmf7V7H8fXC%2BDEXwRbtMhLn3%2FO09A%2BR4puQwKBpEUAnJGFDRdMaWTlx4PG5sCG5VU7p0Nu2useeCD%2F4QUJm4yRtThz2wdcX1SsnN5GyuNPk3rEVXsuXH8Pydtc%2FS2OVmhpzWL4awaQ9uEN3IzciyElIpHFzThqQkFh6IXxEP2wFDvI8mb0%2FAul7pWuRB56HfpPJzA8QRXuQl0g5tEPrHzCagGezUT%2FgB007%2FYCcsFqp7fJX5aI9jWiPkdA1gPyTc%2F6RqVgLqPPpsTW5lDcOGLOL%2FxbLSWUrqt1tG9NtdjKIBsIHWvSB86jsFipHBih0W65MYUNgdgp4OxvKxh8YmLUbukpJLN81HsJgym2RXxO6ATRob686X%2Bzql3GUxOQ2BwtlOUSOgc1o8M83EBIsMMug5rwGOqUBbBtStFDKm2SSGfaKiVqKQ6KB7wuFaWq%2FAFExr0sAdFuAZFdlupDXASfc3ug%2Bc9Ptl%2B0LlQf3IpDCqjSMqfwyBCEjRnsm0nftwwl8KJLfd82mkIlZjmytM3RhaVrOZY4YBWxSzX0GSnUZujlz0Kgbrplg7cfmtPJzy7vfRm75e7ohrIpcNR93htbXdhiVX%2FHnQR4ev%2FjjFMLrhx7BhfV%2Fu7w6bJ7l&X-Amz-Signature=8b1ff5a4ddd0402221265a7577538ebf9a7175e028c62e04c1f28dc28dd8a7b3&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RRTV5SS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQD9BiXoTbM4Hoe4fCThXgcqLbhGTBt8vs1ZfrF40mDkbgIgAZ%2BbwHLPLD9OmGbHowzc8vUG1KrcHNxgOmPKVwEN5Z0qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO1fdRc1QUSkBkQifSrcA7DzqPpCggs6QSHzB4i8Tgc9vboUrU3wfzAkQH0OPZKyEi0aSPJOCjd9Az4RSIFsBCOqC7U8T1f1TibB4NteguFem5v4SqRv9fqd9psKZYgqSAtrk%2FOwpcQW8ibHSvwIdscVu%2F51KxxthJUmEGh2rIFz9H6wcvg6m99GIV%2BaRDFzYbPQTNfez9xihQdlhZW2F4HKaruSY1G%2BiguybhEWs59tMLNUexev6QPBGRDXdUhjxtH7fLhRQV4LEuOIkeq7U9eEquaWm2iXcHRkDP8OZ54mLmD%2BKgsuinxujUWvL2ssL3tc91rau5Z%2FXmK%2FI78XX%2BUY6SfgL702bQ%2BzdqddlaY5kuyTWn1G2SP5ZEVU3DFkodtHOQV5YMIKSiro88U3TOUNS5i4teDYOSmQsa10DP1K%2FPDPRgQcUJQLqXy5SO80oFY5AQ4aZJQ%2FjIBG%2F6DqhX1fqQpTcEyJOVBPpEGSFe%2BktJJ6QKN8Sg8nZJXE2RbJH9ewtLWHXZELT4xYDzHV2qwjku%2BHxYGBrYOQ5Zf62T%2BDqJvIY7NacxWnF21D1z7WUygvDyP%2BUgXla8Oa1m0zL5gRZgjl1h%2BsuU1%2BJ%2FJ5d9zTzhwbXXGRdjt94teN1es0VjWJ4l%2BHVwB7XLFBMOef5rwGOqUBIb%2F4OwfEjvCccF1qwAtAnK2Q1X8hwYnE3FRztlwiw7nN5naVdkqwVlnz9a6su0rXSRTKnD2g%2FJbaq1AmnN4Nsq0zcVw6G3eH7sefwEFx1Bv9VfaRKgsuXb0NKcZclJfLEB8VnPXWDKUxdqkMhqlz%2FxJX%2BnYF9ic7vcmz7kBtsd9EX0yxjkJhWPS6R24q3iwV3DCSKFXqcrdlaIQgkhA4F%2BRlFqwd&X-Amz-Signature=bcdd2d4ac50bddc7632a29ac04071d916615fcc78df78ef08d813514953d9a6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6RR2HS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICqHcywVCVedZAsZhjMi9QqpvTW%2B%2BhyfIKHxJb13WpJ5AiAj47lJHyOXCNoX3rfgmm3lQCm3O5vukivbk%2FjlKA5zKSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2d1%2B%2F4rs1yJuM46PKtwDFFXgcKcv2d0oFprUKB%2BtA4DHJS4Uvi26aSyTvFFpiVPMLTEQ7V2zpIXDOmOPfcN2%2FD%2FMcJvIksEAJHoP5nP4N8mE3tCCfeAm2H0mDmUX%2FG9rhq%2Frhe4ek4%2FPwgY2z0fX3STGXHOoLn2J2uMX5u6CkWyb1P6fwD0ZHx1dwLkVLh6QNsAd%2F3o%2B3qQQTM3gO3xq8YuKY6WwKb0rceSgfkv%2FKV9G1V0wsWs4LQayPrWDfPUdZB%2BLfGgZBYl0S9bHOyt0bfywL8rqEvkoA6eZYpbnSj1ENwijU6ncipazxy%2B08iyyzHnRy17NzEn1YkMuXIr8reCczEMxAV1G4PKRutDkGJLbVIY1kaoTGQR8RUSaV5yuDDLmwSN1%2FluWwkZ5tbl%2BtrTNXGDYEtFF5LlvXKftcKEqCegWv027w%2BO9NCZ3N5EPOnXjUId%2BMsjruffM77sp7od3iXvysN07JifL1HJM6uKY9iWpRF5TnxABjCHtThnG2aJN2x3%2B6W%2BaS1NUG%2B7CHuP1wYtLo89%2BRs6VbGnCqpGEuQ9lAO8PvzmJwWzW%2Fi9M9F%2FfxQUlCO4V70ssyVEKjS%2F9pdfo9ioXFeIwo0FWn4IOt9VAxXXtMC7Tzpbvp9MyefvCv2vAC8El8U4wmqDmvAY6pgGcflXRtiwx%2BuyvKaHXwAVPBjb7bGEYLatTIskJp%2F9NkzTsTYM4XU%2FhCkuiony5SJAgRj55wfSHNgLipxWquSaNPLLNxVmeyg02sSnrtw7NmIxC4zS6FUlP%2Fh962rQ%2FBkTiOAUKhHbqn1CHFHar44KxHhjPqXLNaGjGa6D6Ac%2BhK5RPL4QRY8xQKgaruEIBAt3zmQHnl7Mg98MYgSAWpnYm6H2OIshi&X-Amz-Signature=02539194f9d725b83dbee9289dd68f5c0677c2542493ea066f5d708d8c0c7146&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6RR2HS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICqHcywVCVedZAsZhjMi9QqpvTW%2B%2BhyfIKHxJb13WpJ5AiAj47lJHyOXCNoX3rfgmm3lQCm3O5vukivbk%2FjlKA5zKSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2d1%2B%2F4rs1yJuM46PKtwDFFXgcKcv2d0oFprUKB%2BtA4DHJS4Uvi26aSyTvFFpiVPMLTEQ7V2zpIXDOmOPfcN2%2FD%2FMcJvIksEAJHoP5nP4N8mE3tCCfeAm2H0mDmUX%2FG9rhq%2Frhe4ek4%2FPwgY2z0fX3STGXHOoLn2J2uMX5u6CkWyb1P6fwD0ZHx1dwLkVLh6QNsAd%2F3o%2B3qQQTM3gO3xq8YuKY6WwKb0rceSgfkv%2FKV9G1V0wsWs4LQayPrWDfPUdZB%2BLfGgZBYl0S9bHOyt0bfywL8rqEvkoA6eZYpbnSj1ENwijU6ncipazxy%2B08iyyzHnRy17NzEn1YkMuXIr8reCczEMxAV1G4PKRutDkGJLbVIY1kaoTGQR8RUSaV5yuDDLmwSN1%2FluWwkZ5tbl%2BtrTNXGDYEtFF5LlvXKftcKEqCegWv027w%2BO9NCZ3N5EPOnXjUId%2BMsjruffM77sp7od3iXvysN07JifL1HJM6uKY9iWpRF5TnxABjCHtThnG2aJN2x3%2B6W%2BaS1NUG%2B7CHuP1wYtLo89%2BRs6VbGnCqpGEuQ9lAO8PvzmJwWzW%2Fi9M9F%2FfxQUlCO4V70ssyVEKjS%2F9pdfo9ioXFeIwo0FWn4IOt9VAxXXtMC7Tzpbvp9MyefvCv2vAC8El8U4wmqDmvAY6pgGcflXRtiwx%2BuyvKaHXwAVPBjb7bGEYLatTIskJp%2F9NkzTsTYM4XU%2FhCkuiony5SJAgRj55wfSHNgLipxWquSaNPLLNxVmeyg02sSnrtw7NmIxC4zS6FUlP%2Fh962rQ%2FBkTiOAUKhHbqn1CHFHar44KxHhjPqXLNaGjGa6D6Ac%2BhK5RPL4QRY8xQKgaruEIBAt3zmQHnl7Mg98MYgSAWpnYm6H2OIshi&X-Amz-Signature=bab7fdf7bae06f31ce4b642de5a370f4315cd483ed5fd575b736fd89827a4115&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6RR2HS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICqHcywVCVedZAsZhjMi9QqpvTW%2B%2BhyfIKHxJb13WpJ5AiAj47lJHyOXCNoX3rfgmm3lQCm3O5vukivbk%2FjlKA5zKSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2d1%2B%2F4rs1yJuM46PKtwDFFXgcKcv2d0oFprUKB%2BtA4DHJS4Uvi26aSyTvFFpiVPMLTEQ7V2zpIXDOmOPfcN2%2FD%2FMcJvIksEAJHoP5nP4N8mE3tCCfeAm2H0mDmUX%2FG9rhq%2Frhe4ek4%2FPwgY2z0fX3STGXHOoLn2J2uMX5u6CkWyb1P6fwD0ZHx1dwLkVLh6QNsAd%2F3o%2B3qQQTM3gO3xq8YuKY6WwKb0rceSgfkv%2FKV9G1V0wsWs4LQayPrWDfPUdZB%2BLfGgZBYl0S9bHOyt0bfywL8rqEvkoA6eZYpbnSj1ENwijU6ncipazxy%2B08iyyzHnRy17NzEn1YkMuXIr8reCczEMxAV1G4PKRutDkGJLbVIY1kaoTGQR8RUSaV5yuDDLmwSN1%2FluWwkZ5tbl%2BtrTNXGDYEtFF5LlvXKftcKEqCegWv027w%2BO9NCZ3N5EPOnXjUId%2BMsjruffM77sp7od3iXvysN07JifL1HJM6uKY9iWpRF5TnxABjCHtThnG2aJN2x3%2B6W%2BaS1NUG%2B7CHuP1wYtLo89%2BRs6VbGnCqpGEuQ9lAO8PvzmJwWzW%2Fi9M9F%2FfxQUlCO4V70ssyVEKjS%2F9pdfo9ioXFeIwo0FWn4IOt9VAxXXtMC7Tzpbvp9MyefvCv2vAC8El8U4wmqDmvAY6pgGcflXRtiwx%2BuyvKaHXwAVPBjb7bGEYLatTIskJp%2F9NkzTsTYM4XU%2FhCkuiony5SJAgRj55wfSHNgLipxWquSaNPLLNxVmeyg02sSnrtw7NmIxC4zS6FUlP%2Fh962rQ%2FBkTiOAUKhHbqn1CHFHar44KxHhjPqXLNaGjGa6D6Ac%2BhK5RPL4QRY8xQKgaruEIBAt3zmQHnl7Mg98MYgSAWpnYm6H2OIshi&X-Amz-Signature=f3f603198b67bc4764ab7e4215adab153d0ecbd6cd06a7725e20a563666a903e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6RR2HS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICqHcywVCVedZAsZhjMi9QqpvTW%2B%2BhyfIKHxJb13WpJ5AiAj47lJHyOXCNoX3rfgmm3lQCm3O5vukivbk%2FjlKA5zKSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2d1%2B%2F4rs1yJuM46PKtwDFFXgcKcv2d0oFprUKB%2BtA4DHJS4Uvi26aSyTvFFpiVPMLTEQ7V2zpIXDOmOPfcN2%2FD%2FMcJvIksEAJHoP5nP4N8mE3tCCfeAm2H0mDmUX%2FG9rhq%2Frhe4ek4%2FPwgY2z0fX3STGXHOoLn2J2uMX5u6CkWyb1P6fwD0ZHx1dwLkVLh6QNsAd%2F3o%2B3qQQTM3gO3xq8YuKY6WwKb0rceSgfkv%2FKV9G1V0wsWs4LQayPrWDfPUdZB%2BLfGgZBYl0S9bHOyt0bfywL8rqEvkoA6eZYpbnSj1ENwijU6ncipazxy%2B08iyyzHnRy17NzEn1YkMuXIr8reCczEMxAV1G4PKRutDkGJLbVIY1kaoTGQR8RUSaV5yuDDLmwSN1%2FluWwkZ5tbl%2BtrTNXGDYEtFF5LlvXKftcKEqCegWv027w%2BO9NCZ3N5EPOnXjUId%2BMsjruffM77sp7od3iXvysN07JifL1HJM6uKY9iWpRF5TnxABjCHtThnG2aJN2x3%2B6W%2BaS1NUG%2B7CHuP1wYtLo89%2BRs6VbGnCqpGEuQ9lAO8PvzmJwWzW%2Fi9M9F%2FfxQUlCO4V70ssyVEKjS%2F9pdfo9ioXFeIwo0FWn4IOt9VAxXXtMC7Tzpbvp9MyefvCv2vAC8El8U4wmqDmvAY6pgGcflXRtiwx%2BuyvKaHXwAVPBjb7bGEYLatTIskJp%2F9NkzTsTYM4XU%2FhCkuiony5SJAgRj55wfSHNgLipxWquSaNPLLNxVmeyg02sSnrtw7NmIxC4zS6FUlP%2Fh962rQ%2FBkTiOAUKhHbqn1CHFHar44KxHhjPqXLNaGjGa6D6Ac%2BhK5RPL4QRY8xQKgaruEIBAt3zmQHnl7Mg98MYgSAWpnYm6H2OIshi&X-Amz-Signature=d6ba492a3aa3d0858118c75bb2f8923796000cddd02e1a662869737ad2a76ddc&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5ASWOAU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCiBxrMLBt4lQdDACPukgYIHwYi7uYtwLaN2%2B337vWvdwIhAM15AFWSNs8qf2R7z5BCMFg4P6%2FwN7oFtdX3Qf8QcWbNKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwtDnrHi1%2F%2F1tvmbr0q3AOF6cMQpeIvBW7ZbraJUU62zvbFjZPCGl7pts33vCzxPL4%2FcCF1SsWFHmsITJRdRZJmyGA3XvVJ%2FeLflFEPm78oNZiE48WojosWMLvJkqYpxyP1tZCjpdXwv6YtbfXygjWy1NjhtoJTXJKCk8c6bUtiEUX41mDhxIoS3P00ob9b%2Fkrv%2BRzqW6dzoCzP599bkvs3J%2B8FxW2y4FGyvZmWbkkEHWnh%2Bo6rZVVmZmKT2Uwsbbu4mOMkoS%2B1eTurQOy584zgqyVNZdZHvSswusLOhG6AOW%2F3WPaDLC00mwcgQxvdJ1RpP4da5ZDCO52cJ0Q1Wl65IRbg7By%2BStPqQVS3Rz8cA8Y5gWlxw0NVq5giK7%2FM0Yso%2Fghiqhid2F4qNuK3xeEjS8No9TYiGr1mEhnW9u79%2B7mntfLQ7uum59jV55qrMo9HvWmvxsxMBS1xPq4anuJjt%2BJxHqBryET8r4A3tmmBKDS%2BveJszktJszhbFZD6GTDDMqiGQ8ZE4J%2BKs0R7o897DzILjDTT1mOsxYp2OSqRbdweB1ESo1VHNlpQURjqhfVm0EMnzIILrm8S1vThhFGI1iXFQz8BGH8I%2FYdWR1fITSY6FpVoWh0b23StkUy7tl8iJg5Vvfb9fTgGUDDSn%2Ba8BjqkAecorlT8tP8bu%2F4pLwy8Xoi%2B1%2BbqdSyHyFVNul3JQMXcYCHN1mb9q2MOrMFoL00r6Ygb7vVBT5TnkBLvIkCVfsCxJ4SC3uGp5xd3%2BebNHVusQALds2XrB2JknyZIoJD6JJR6w2%2BZDdA98hacgj%2FhOQWofabmO7r0vWkxSwuUOJz6iDDvD4opC5nWBZxhu6cD63ssEFUns%2BszqzxZzDLcESd3hpYD&X-Amz-Signature=0ba9f74a97f83636fb0eab02c9dd8baf90e74c5ce70e961ecf6cf8cc21f784e0&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QL2GZDFY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDg2plx2MD1n5KtQXQ9mFkSdqsx1OHPY57NyPMcmzwq0AIhALra50eTdv%2B9fNDnkDCL5hwP03swRRvOwVnR7gilnIjRKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz8w5eiUE0YJ1Id5Qq3AOBGfHYpqXpLpmxOlUmtFeXgPro0SaFQozVIg%2B%2BanGJPJi8ydiq%2Bw9T%2FDZDRr3g40lMSnPe3f5aLgR%2BQ3tq2yZuUNl52lmDaVP7uUGn0tiCTwo7bKgwq%2FGftCBUW85FPkJUbsKKpkCDG5J6wpRl%2BlMZzxPB7MmNaqiAPpxnn3w7C6WYEi03hmIOg23AzxA5Zue6MFjceiN1OhmwsJ2uF1FmLt739tCo3sM3RPKqQc17DZ9D1aOfsil5xT0E3m9tF9Esm%2BqUpFnmEzYUfYyF8%2Fo%2FD9lQmdSPdXUg6UZcpaFpZDHNvwkYYxOZ5rCsUrxhEviZhv7xID9kz1JCeqy5na2X8P4g3noDgelQ2Xks3BC5le%2FcH5BwyUFOiQRKPr%2FqlFp90pvkO3TI7wZvyOmfVoeNSBgXv7toNlDYq1yQc%2FY72vHAcigygVuCQCn70TgWLk26VgwiHNixqLyn16ZmVGwFxJF2C4tW6gepAQqa6teIhjItweHUSyOXKVecdBeBBFkB5miOwzgmEirOxAz9eMeQIyj%2FX7quTByWY%2Bn8ujwU%2FD0LTeIHuIPCQpT5YypGddKjqJleskTqtKKo6emaiFn5KkSkzkZO278bZEZZ3SZqzuYryfXL1PBkBHVl5jDLoOa8BjqkAWy4nH89k5kSI%2FIrmz6SjRMM3A%2BY%2FewXCzd7N263Hbm%2F71INfwxuyUKT9JF1qp05eOFVy8SIICngXvMYVd8W54ytqGSQWsL3l2LG%2BqjzLGoMeBbSHJBXXqkJuS1G8dPeOTWgavM6UzxTtCMmtIb0ItzD%2BBQArjd5JH3VN29A407WF%2BxRyYooCiwT8Fo4i1KuBHRHsWF2gzxpYmDDF1DTWXIyIeAx&X-Amz-Signature=e8383976cf39b69a714a2fe247042d80b087cc705f7f2aee45e62cc9366890f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UE5NPAE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIAw8QDoHCfCixGpq4CJN8X7DvZnogk746Ble%2F4dgAbI%2BAiBhmVT0x7x7vAveC5osMLytKOsom495GACIrFRM%2FOsoXiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKLu%2BmlERRe2iyTqCKtwDb6BHEoqYSoGlAoV%2FXk82kSVoHd5Cu3ajf%2BcEmVVXeBVGzP%2BDdqXAq2gttoPrpL%2BUts7WJCdRO46VGnRaJTiEnQWDBQb0AiGLJ3tV2K9xEbsvN0yWFFAT7kx69bSPdaySi0tI2aQpOMjqO1JxDB7ZEchUjB8xDDPxDRmNIVrEvDgpVvK8AHRGnyGct4LdU34a75qhDwdYRTD%2FculUrtKFVx17YJdNPmmwPAXW3QjyXdbTwKmfjzzlSXzZxX4CJwTZMGVcBwLo2Q82qnokt44pOmI0TaiLiqY8gAhb1uyYt0p8oZg0r6gXO0aiAMYFTKKhB9EEqjYkfo7tipEkzDu6W1ySMlXjlllKut%2BFMTCq%2BJqrrqtXqpF8cWy%2FH9U15N%2FzpcVpKcahYmoEkgLbgawRledX7BFo25JVSfK3wHq0v28EOqYE%2FaSGC4tOZi5MR2J8Fv%2BsG4xuK1mDXKWFYMtWla4hz3NXJEEeMVPQxQ03xo7QMdyXw7rGxDNGpAR%2Fgb69cuNZWji6XqlOo0btU%2Bydh7OB7uHfT3pIFaVvmVYfhq3a7aVVS9wpz%2Bo%2FOyTjUNCUtGtH6hiDQQYicQ8F0g%2Fv8LjiM2NgOj0J%2F6mFshpavStwJuI8DxqA0D9BPZYw1Z%2FmvAY6pgHhFTIgogPTwP23HpEet3cYJQJK%2FxMp6RinZAJgCda2%2BE8Y%2F%2B8O8LpmUWRrj%2BEQQTEGkdlZmXU7rFQDrYFl1%2Bb730R74S9isDwIjaqAG0p180ONlbv7m%2FDtb5DSlqSgP6Era2zoJ%2B7oDf%2FjYdiEZswFMlF5%2FBje0im%2BF0degU8T%2F8FTtqWlUlW2qbq63zBaWI%2B43ngkC88SpBWOmZ8N87xMqGKapshW&X-Amz-Signature=095bceccbfd21f438c98e2a6fae09e04332af4ebaddb84b075b2366f39aa99ce&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UE5NPAE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIAw8QDoHCfCixGpq4CJN8X7DvZnogk746Ble%2F4dgAbI%2BAiBhmVT0x7x7vAveC5osMLytKOsom495GACIrFRM%2FOsoXiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKLu%2BmlERRe2iyTqCKtwDb6BHEoqYSoGlAoV%2FXk82kSVoHd5Cu3ajf%2BcEmVVXeBVGzP%2BDdqXAq2gttoPrpL%2BUts7WJCdRO46VGnRaJTiEnQWDBQb0AiGLJ3tV2K9xEbsvN0yWFFAT7kx69bSPdaySi0tI2aQpOMjqO1JxDB7ZEchUjB8xDDPxDRmNIVrEvDgpVvK8AHRGnyGct4LdU34a75qhDwdYRTD%2FculUrtKFVx17YJdNPmmwPAXW3QjyXdbTwKmfjzzlSXzZxX4CJwTZMGVcBwLo2Q82qnokt44pOmI0TaiLiqY8gAhb1uyYt0p8oZg0r6gXO0aiAMYFTKKhB9EEqjYkfo7tipEkzDu6W1ySMlXjlllKut%2BFMTCq%2BJqrrqtXqpF8cWy%2FH9U15N%2FzpcVpKcahYmoEkgLbgawRledX7BFo25JVSfK3wHq0v28EOqYE%2FaSGC4tOZi5MR2J8Fv%2BsG4xuK1mDXKWFYMtWla4hz3NXJEEeMVPQxQ03xo7QMdyXw7rGxDNGpAR%2Fgb69cuNZWji6XqlOo0btU%2Bydh7OB7uHfT3pIFaVvmVYfhq3a7aVVS9wpz%2Bo%2FOyTjUNCUtGtH6hiDQQYicQ8F0g%2Fv8LjiM2NgOj0J%2F6mFshpavStwJuI8DxqA0D9BPZYw1Z%2FmvAY6pgHhFTIgogPTwP23HpEet3cYJQJK%2FxMp6RinZAJgCda2%2BE8Y%2F%2B8O8LpmUWRrj%2BEQQTEGkdlZmXU7rFQDrYFl1%2Bb730R74S9isDwIjaqAG0p180ONlbv7m%2FDtb5DSlqSgP6Era2zoJ%2B7oDf%2FjYdiEZswFMlF5%2FBje0im%2BF0degU8T%2F8FTtqWlUlW2qbq63zBaWI%2B43ngkC88SpBWOmZ8N87xMqGKapshW&X-Amz-Signature=4ab339100e94daf5dd066ca05e0edb5047cae77fd7b4dbcb3b233c728550c85e&X-Amz-SignedHeaders=host&x-id=GetObject)

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
