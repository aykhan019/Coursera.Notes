

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665O52CDL4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCYsnm7q4V7G3Mk8Jlcr%2FmuAxkhZMiV80ZQqDv3QiqL4QIhALKTNKQP2x0YSfaYJVxDDtyqq7OQ7vsJhJGu4sm4uJW5Kv8DCHEQABoMNjM3NDIzMTgzODA1IgxjR8q3KYkEItgUgzoq3AMVNYdP50dbbcMKIfptCXfTNfnRltMwhR1X%2B5cELsj957o30PPJK9mYiDfwskjs6LCCYkY4q97DZzGxgZxnt7s73MtNBEwkjCre%2BLXlYWPEqOnPz94tL2Vkm%2FS94559KNn3qWuJ73VBZIrGDBrYSu%2FmF%2B5nhBtn2fwNsBBfDkbVobEcsU9MkPQCwwXHzypYrCL0Sz21NeZWke8XwnIaYMrJCE95W6OmPkeONFTXN3bNNKocKFzODJj%2FNuavZH%2FDgUOWdkajRMiI8cZFJo4qXiXIbJQFp7hCUKMsP6JT6ngsvr4bqHXrfiBkdqfDKrX60w9uTdZUym0HBNzRXz20nJ1XtPfSwB%2B8OltgQ5HbyCUrImZcL9xfKs4R2%2BmvEAUM4OKrjbusvEK4lNFCFnCucr5f0Xg%2Fi478RW7OYdN22UN8C2acs8xFv1bbf0cocmHs6IswgfpkeantueXCPmDlxdW36GxX4aI6hpVjqMi9KbvIbLNKyotpfJ3R1rD6UbJjHbXyR%2FPNYVnb%2FPcHiCD1hUwCW2YJJbeywDef6iurF%2BfxOJJI%2Bp3qixvzq9fvhNV1RLYz6KTNK64wflHsVd9SjdFS5pu938XqSH3Hl7KcaZlsl6i2I9jlNopqttjkrDDL%2BZa9BjqkASDIdhHMC%2BG1YkLYv6EQKwbr9jFGLYZyQVF1u7QHsM%2FGMlz0YH65wOp1cPDgOJoqre6o2vZkEyyu6PWU8yHeFZajXzCCm4a7jZXNUEoS%2BuKpGIlePxXQSMHHe1%2Fz0FsFpKw22pVeeL%2FnACSLnzGWlCKMM3sz3aZxq3wPkhYn%2Bw%2B0KPyoVsAKF1zJRAEjNxPOcKG4awwhBnAWu3G%2FWJLMlzjKtEiW&X-Amz-Signature=182b5c121fb78c989aa5eb1d149a87e6d55f524a5da905f4388e4286abf469d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665O52CDL4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCYsnm7q4V7G3Mk8Jlcr%2FmuAxkhZMiV80ZQqDv3QiqL4QIhALKTNKQP2x0YSfaYJVxDDtyqq7OQ7vsJhJGu4sm4uJW5Kv8DCHEQABoMNjM3NDIzMTgzODA1IgxjR8q3KYkEItgUgzoq3AMVNYdP50dbbcMKIfptCXfTNfnRltMwhR1X%2B5cELsj957o30PPJK9mYiDfwskjs6LCCYkY4q97DZzGxgZxnt7s73MtNBEwkjCre%2BLXlYWPEqOnPz94tL2Vkm%2FS94559KNn3qWuJ73VBZIrGDBrYSu%2FmF%2B5nhBtn2fwNsBBfDkbVobEcsU9MkPQCwwXHzypYrCL0Sz21NeZWke8XwnIaYMrJCE95W6OmPkeONFTXN3bNNKocKFzODJj%2FNuavZH%2FDgUOWdkajRMiI8cZFJo4qXiXIbJQFp7hCUKMsP6JT6ngsvr4bqHXrfiBkdqfDKrX60w9uTdZUym0HBNzRXz20nJ1XtPfSwB%2B8OltgQ5HbyCUrImZcL9xfKs4R2%2BmvEAUM4OKrjbusvEK4lNFCFnCucr5f0Xg%2Fi478RW7OYdN22UN8C2acs8xFv1bbf0cocmHs6IswgfpkeantueXCPmDlxdW36GxX4aI6hpVjqMi9KbvIbLNKyotpfJ3R1rD6UbJjHbXyR%2FPNYVnb%2FPcHiCD1hUwCW2YJJbeywDef6iurF%2BfxOJJI%2Bp3qixvzq9fvhNV1RLYz6KTNK64wflHsVd9SjdFS5pu938XqSH3Hl7KcaZlsl6i2I9jlNopqttjkrDDL%2BZa9BjqkASDIdhHMC%2BG1YkLYv6EQKwbr9jFGLYZyQVF1u7QHsM%2FGMlz0YH65wOp1cPDgOJoqre6o2vZkEyyu6PWU8yHeFZajXzCCm4a7jZXNUEoS%2BuKpGIlePxXQSMHHe1%2Fz0FsFpKw22pVeeL%2FnACSLnzGWlCKMM3sz3aZxq3wPkhYn%2Bw%2B0KPyoVsAKF1zJRAEjNxPOcKG4awwhBnAWu3G%2FWJLMlzjKtEiW&X-Amz-Signature=ea8cb99441724e4a58f4347bd741f941a7ab47b79003bbaee616dd509ed53954&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665O52CDL4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCYsnm7q4V7G3Mk8Jlcr%2FmuAxkhZMiV80ZQqDv3QiqL4QIhALKTNKQP2x0YSfaYJVxDDtyqq7OQ7vsJhJGu4sm4uJW5Kv8DCHEQABoMNjM3NDIzMTgzODA1IgxjR8q3KYkEItgUgzoq3AMVNYdP50dbbcMKIfptCXfTNfnRltMwhR1X%2B5cELsj957o30PPJK9mYiDfwskjs6LCCYkY4q97DZzGxgZxnt7s73MtNBEwkjCre%2BLXlYWPEqOnPz94tL2Vkm%2FS94559KNn3qWuJ73VBZIrGDBrYSu%2FmF%2B5nhBtn2fwNsBBfDkbVobEcsU9MkPQCwwXHzypYrCL0Sz21NeZWke8XwnIaYMrJCE95W6OmPkeONFTXN3bNNKocKFzODJj%2FNuavZH%2FDgUOWdkajRMiI8cZFJo4qXiXIbJQFp7hCUKMsP6JT6ngsvr4bqHXrfiBkdqfDKrX60w9uTdZUym0HBNzRXz20nJ1XtPfSwB%2B8OltgQ5HbyCUrImZcL9xfKs4R2%2BmvEAUM4OKrjbusvEK4lNFCFnCucr5f0Xg%2Fi478RW7OYdN22UN8C2acs8xFv1bbf0cocmHs6IswgfpkeantueXCPmDlxdW36GxX4aI6hpVjqMi9KbvIbLNKyotpfJ3R1rD6UbJjHbXyR%2FPNYVnb%2FPcHiCD1hUwCW2YJJbeywDef6iurF%2BfxOJJI%2Bp3qixvzq9fvhNV1RLYz6KTNK64wflHsVd9SjdFS5pu938XqSH3Hl7KcaZlsl6i2I9jlNopqttjkrDDL%2BZa9BjqkASDIdhHMC%2BG1YkLYv6EQKwbr9jFGLYZyQVF1u7QHsM%2FGMlz0YH65wOp1cPDgOJoqre6o2vZkEyyu6PWU8yHeFZajXzCCm4a7jZXNUEoS%2BuKpGIlePxXQSMHHe1%2Fz0FsFpKw22pVeeL%2FnACSLnzGWlCKMM3sz3aZxq3wPkhYn%2Bw%2B0KPyoVsAKF1zJRAEjNxPOcKG4awwhBnAWu3G%2FWJLMlzjKtEiW&X-Amz-Signature=c7775e4afa5024f92fd463958cadb7e27c8d4e986fbb9701460ef1442c3349ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSCN2G7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCEqE4I3IRBRiksJnacdNsr4D0bgPZF4FCzYhDNDa3I%2FQIgP9laDM7i4TAFfrmbKDE74ggF5sVGMiRoITRBgkM0cVUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEVqgW1g7Vblaf3qWSrcA5XwoBjS6onuS9oo3s7M9rPNCHKNQUa9JMQDMeNJr3zVsKdwNLRxzImYZvVqj7evbbkn8HZJ16FNnJdPtQzpkxgoTIZnhKQdLgM666vsU76cpBNjwufmP2Cy548PbFUDQYtF%2FmnExThArGs5q0l45ZQke80VnUbtPsOmNsGVCYLiO36SRjYCerTDHgBVmDsB%2F2ZyZNrQW9C89Ed4PoxTKRBCx2Nnj94lLerDSlRlQ8kM%2BzpBKVhObS3mDZPiLq78SyfZdmlnNz0T%2BsdSFLQ7MCB0bqwfHw8BEIL2UYGlIk11VFKp0xB2z9l6Z5vQzywIClCljdt4TvViBHSaJQ5uo7SGQhlGFLCK1%2FF38dk9U3w5Sc9loayishUy%2Fcs6f8Tp2ZnSFBcHbIY%2BKS%2Fv83v5XkfrOBWrbcVhbw48ZlKvBawpOp0LPmSZcAhel%2FVa%2BUmjINbt8YdaVQlAOUOOOmUfJhhFyE21iZ2twl1o13XkuzrEtbkgk7oK6Id74DthuiF%2BkCJGM4rfQjf7V1dZxwaDkh0TRppJ8vJRkcqnXSxQAfmPuu4sopuoQ7QouwzRxiHOG5ftmQsZXGaMAOOWNz8Rnfxkn3RQbB15xPJ7g1mi46at%2FfQgB%2Fmu7cpcJTxiMNb5lr0GOqUBm9rFzSia73VZEVcX80fbbTwpKEBf%2FJ8HS7OIL9RmydSpsMDTsG5lSdgQrQ1ZStslZ%2BxwMHrFT1NxJVwuclGz1vKtqwyvQCA0fyNNJCzNZtKRUMflBrvYx52mfs5zCpPOIUN57RC3lNxyHEFc0j4nz4mRA3XubdZlqtstMPWv9QDCUPlmrLFJOxwyWQS6GNk5KN02uN4acf4jCOPr7VtfGJPQ3Sun&X-Amz-Signature=973cff544c5223ecafd4148f0b9f926508be9ab8221ece05c7dcfe570d4a41dc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSCN2G7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCEqE4I3IRBRiksJnacdNsr4D0bgPZF4FCzYhDNDa3I%2FQIgP9laDM7i4TAFfrmbKDE74ggF5sVGMiRoITRBgkM0cVUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEVqgW1g7Vblaf3qWSrcA5XwoBjS6onuS9oo3s7M9rPNCHKNQUa9JMQDMeNJr3zVsKdwNLRxzImYZvVqj7evbbkn8HZJ16FNnJdPtQzpkxgoTIZnhKQdLgM666vsU76cpBNjwufmP2Cy548PbFUDQYtF%2FmnExThArGs5q0l45ZQke80VnUbtPsOmNsGVCYLiO36SRjYCerTDHgBVmDsB%2F2ZyZNrQW9C89Ed4PoxTKRBCx2Nnj94lLerDSlRlQ8kM%2BzpBKVhObS3mDZPiLq78SyfZdmlnNz0T%2BsdSFLQ7MCB0bqwfHw8BEIL2UYGlIk11VFKp0xB2z9l6Z5vQzywIClCljdt4TvViBHSaJQ5uo7SGQhlGFLCK1%2FF38dk9U3w5Sc9loayishUy%2Fcs6f8Tp2ZnSFBcHbIY%2BKS%2Fv83v5XkfrOBWrbcVhbw48ZlKvBawpOp0LPmSZcAhel%2FVa%2BUmjINbt8YdaVQlAOUOOOmUfJhhFyE21iZ2twl1o13XkuzrEtbkgk7oK6Id74DthuiF%2BkCJGM4rfQjf7V1dZxwaDkh0TRppJ8vJRkcqnXSxQAfmPuu4sopuoQ7QouwzRxiHOG5ftmQsZXGaMAOOWNz8Rnfxkn3RQbB15xPJ7g1mi46at%2FfQgB%2Fmu7cpcJTxiMNb5lr0GOqUBm9rFzSia73VZEVcX80fbbTwpKEBf%2FJ8HS7OIL9RmydSpsMDTsG5lSdgQrQ1ZStslZ%2BxwMHrFT1NxJVwuclGz1vKtqwyvQCA0fyNNJCzNZtKRUMflBrvYx52mfs5zCpPOIUN57RC3lNxyHEFc0j4nz4mRA3XubdZlqtstMPWv9QDCUPlmrLFJOxwyWQS6GNk5KN02uN4acf4jCOPr7VtfGJPQ3Sun&X-Amz-Signature=062c9fc9d56625336f9d33160a7ad96bbda0eb8132c24be41cfd090f77b809e8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSCN2G7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCEqE4I3IRBRiksJnacdNsr4D0bgPZF4FCzYhDNDa3I%2FQIgP9laDM7i4TAFfrmbKDE74ggF5sVGMiRoITRBgkM0cVUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEVqgW1g7Vblaf3qWSrcA5XwoBjS6onuS9oo3s7M9rPNCHKNQUa9JMQDMeNJr3zVsKdwNLRxzImYZvVqj7evbbkn8HZJ16FNnJdPtQzpkxgoTIZnhKQdLgM666vsU76cpBNjwufmP2Cy548PbFUDQYtF%2FmnExThArGs5q0l45ZQke80VnUbtPsOmNsGVCYLiO36SRjYCerTDHgBVmDsB%2F2ZyZNrQW9C89Ed4PoxTKRBCx2Nnj94lLerDSlRlQ8kM%2BzpBKVhObS3mDZPiLq78SyfZdmlnNz0T%2BsdSFLQ7MCB0bqwfHw8BEIL2UYGlIk11VFKp0xB2z9l6Z5vQzywIClCljdt4TvViBHSaJQ5uo7SGQhlGFLCK1%2FF38dk9U3w5Sc9loayishUy%2Fcs6f8Tp2ZnSFBcHbIY%2BKS%2Fv83v5XkfrOBWrbcVhbw48ZlKvBawpOp0LPmSZcAhel%2FVa%2BUmjINbt8YdaVQlAOUOOOmUfJhhFyE21iZ2twl1o13XkuzrEtbkgk7oK6Id74DthuiF%2BkCJGM4rfQjf7V1dZxwaDkh0TRppJ8vJRkcqnXSxQAfmPuu4sopuoQ7QouwzRxiHOG5ftmQsZXGaMAOOWNz8Rnfxkn3RQbB15xPJ7g1mi46at%2FfQgB%2Fmu7cpcJTxiMNb5lr0GOqUBm9rFzSia73VZEVcX80fbbTwpKEBf%2FJ8HS7OIL9RmydSpsMDTsG5lSdgQrQ1ZStslZ%2BxwMHrFT1NxJVwuclGz1vKtqwyvQCA0fyNNJCzNZtKRUMflBrvYx52mfs5zCpPOIUN57RC3lNxyHEFc0j4nz4mRA3XubdZlqtstMPWv9QDCUPlmrLFJOxwyWQS6GNk5KN02uN4acf4jCOPr7VtfGJPQ3Sun&X-Amz-Signature=8a50c296a90bccb060b3c6f130ef9cd74bca8da84878eab0b9cb62791bb8b2ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSCN2G7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCEqE4I3IRBRiksJnacdNsr4D0bgPZF4FCzYhDNDa3I%2FQIgP9laDM7i4TAFfrmbKDE74ggF5sVGMiRoITRBgkM0cVUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEVqgW1g7Vblaf3qWSrcA5XwoBjS6onuS9oo3s7M9rPNCHKNQUa9JMQDMeNJr3zVsKdwNLRxzImYZvVqj7evbbkn8HZJ16FNnJdPtQzpkxgoTIZnhKQdLgM666vsU76cpBNjwufmP2Cy548PbFUDQYtF%2FmnExThArGs5q0l45ZQke80VnUbtPsOmNsGVCYLiO36SRjYCerTDHgBVmDsB%2F2ZyZNrQW9C89Ed4PoxTKRBCx2Nnj94lLerDSlRlQ8kM%2BzpBKVhObS3mDZPiLq78SyfZdmlnNz0T%2BsdSFLQ7MCB0bqwfHw8BEIL2UYGlIk11VFKp0xB2z9l6Z5vQzywIClCljdt4TvViBHSaJQ5uo7SGQhlGFLCK1%2FF38dk9U3w5Sc9loayishUy%2Fcs6f8Tp2ZnSFBcHbIY%2BKS%2Fv83v5XkfrOBWrbcVhbw48ZlKvBawpOp0LPmSZcAhel%2FVa%2BUmjINbt8YdaVQlAOUOOOmUfJhhFyE21iZ2twl1o13XkuzrEtbkgk7oK6Id74DthuiF%2BkCJGM4rfQjf7V1dZxwaDkh0TRppJ8vJRkcqnXSxQAfmPuu4sopuoQ7QouwzRxiHOG5ftmQsZXGaMAOOWNz8Rnfxkn3RQbB15xPJ7g1mi46at%2FfQgB%2Fmu7cpcJTxiMNb5lr0GOqUBm9rFzSia73VZEVcX80fbbTwpKEBf%2FJ8HS7OIL9RmydSpsMDTsG5lSdgQrQ1ZStslZ%2BxwMHrFT1NxJVwuclGz1vKtqwyvQCA0fyNNJCzNZtKRUMflBrvYx52mfs5zCpPOIUN57RC3lNxyHEFc0j4nz4mRA3XubdZlqtstMPWv9QDCUPlmrLFJOxwyWQS6GNk5KN02uN4acf4jCOPr7VtfGJPQ3Sun&X-Amz-Signature=8b3cc826525fb0685201be5e396f0833bdeef22bc261d620f4ebe966b85278e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSCN2G7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCEqE4I3IRBRiksJnacdNsr4D0bgPZF4FCzYhDNDa3I%2FQIgP9laDM7i4TAFfrmbKDE74ggF5sVGMiRoITRBgkM0cVUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEVqgW1g7Vblaf3qWSrcA5XwoBjS6onuS9oo3s7M9rPNCHKNQUa9JMQDMeNJr3zVsKdwNLRxzImYZvVqj7evbbkn8HZJ16FNnJdPtQzpkxgoTIZnhKQdLgM666vsU76cpBNjwufmP2Cy548PbFUDQYtF%2FmnExThArGs5q0l45ZQke80VnUbtPsOmNsGVCYLiO36SRjYCerTDHgBVmDsB%2F2ZyZNrQW9C89Ed4PoxTKRBCx2Nnj94lLerDSlRlQ8kM%2BzpBKVhObS3mDZPiLq78SyfZdmlnNz0T%2BsdSFLQ7MCB0bqwfHw8BEIL2UYGlIk11VFKp0xB2z9l6Z5vQzywIClCljdt4TvViBHSaJQ5uo7SGQhlGFLCK1%2FF38dk9U3w5Sc9loayishUy%2Fcs6f8Tp2ZnSFBcHbIY%2BKS%2Fv83v5XkfrOBWrbcVhbw48ZlKvBawpOp0LPmSZcAhel%2FVa%2BUmjINbt8YdaVQlAOUOOOmUfJhhFyE21iZ2twl1o13XkuzrEtbkgk7oK6Id74DthuiF%2BkCJGM4rfQjf7V1dZxwaDkh0TRppJ8vJRkcqnXSxQAfmPuu4sopuoQ7QouwzRxiHOG5ftmQsZXGaMAOOWNz8Rnfxkn3RQbB15xPJ7g1mi46at%2FfQgB%2Fmu7cpcJTxiMNb5lr0GOqUBm9rFzSia73VZEVcX80fbbTwpKEBf%2FJ8HS7OIL9RmydSpsMDTsG5lSdgQrQ1ZStslZ%2BxwMHrFT1NxJVwuclGz1vKtqwyvQCA0fyNNJCzNZtKRUMflBrvYx52mfs5zCpPOIUN57RC3lNxyHEFc0j4nz4mRA3XubdZlqtstMPWv9QDCUPlmrLFJOxwyWQS6GNk5KN02uN4acf4jCOPr7VtfGJPQ3Sun&X-Amz-Signature=6967f7d21ebdd60a2cad14c79ae3bc34b3ae032a6373f5056be6b72f3b17571b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSCN2G7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCEqE4I3IRBRiksJnacdNsr4D0bgPZF4FCzYhDNDa3I%2FQIgP9laDM7i4TAFfrmbKDE74ggF5sVGMiRoITRBgkM0cVUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEVqgW1g7Vblaf3qWSrcA5XwoBjS6onuS9oo3s7M9rPNCHKNQUa9JMQDMeNJr3zVsKdwNLRxzImYZvVqj7evbbkn8HZJ16FNnJdPtQzpkxgoTIZnhKQdLgM666vsU76cpBNjwufmP2Cy548PbFUDQYtF%2FmnExThArGs5q0l45ZQke80VnUbtPsOmNsGVCYLiO36SRjYCerTDHgBVmDsB%2F2ZyZNrQW9C89Ed4PoxTKRBCx2Nnj94lLerDSlRlQ8kM%2BzpBKVhObS3mDZPiLq78SyfZdmlnNz0T%2BsdSFLQ7MCB0bqwfHw8BEIL2UYGlIk11VFKp0xB2z9l6Z5vQzywIClCljdt4TvViBHSaJQ5uo7SGQhlGFLCK1%2FF38dk9U3w5Sc9loayishUy%2Fcs6f8Tp2ZnSFBcHbIY%2BKS%2Fv83v5XkfrOBWrbcVhbw48ZlKvBawpOp0LPmSZcAhel%2FVa%2BUmjINbt8YdaVQlAOUOOOmUfJhhFyE21iZ2twl1o13XkuzrEtbkgk7oK6Id74DthuiF%2BkCJGM4rfQjf7V1dZxwaDkh0TRppJ8vJRkcqnXSxQAfmPuu4sopuoQ7QouwzRxiHOG5ftmQsZXGaMAOOWNz8Rnfxkn3RQbB15xPJ7g1mi46at%2FfQgB%2Fmu7cpcJTxiMNb5lr0GOqUBm9rFzSia73VZEVcX80fbbTwpKEBf%2FJ8HS7OIL9RmydSpsMDTsG5lSdgQrQ1ZStslZ%2BxwMHrFT1NxJVwuclGz1vKtqwyvQCA0fyNNJCzNZtKRUMflBrvYx52mfs5zCpPOIUN57RC3lNxyHEFc0j4nz4mRA3XubdZlqtstMPWv9QDCUPlmrLFJOxwyWQS6GNk5KN02uN4acf4jCOPr7VtfGJPQ3Sun&X-Amz-Signature=3f2955539da5849131502a9d3b9a7b5b3fb9a34875c6e2a48ef547396c35bfbf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666H24APU7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDHcJelIwZYkeKeSF22nF6N2JfUo034xWrgRB70%2BhnrgAiA%2FGQVkS5t9335zIEB66ebpNXdo4hB5L6EHxdvoRLGcMyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM%2Fh3RRL%2FBXY5Xghx0KtwDfYEKdlP9pxgv%2F%2FU4kJFi%2BR1RiFJeAC7ovL0wC2ydFhdMYaPF30jZjI6oWS5Yks8FLQruuAGWaerWO%2B4SPS9kIdonDP%2FT%2F1SIRjfAI%2FWlYUgMZLKsRiMumtGydBAH6vJ6nyYPLA3HKBDDJsHQOdH0caoHiBiGUANUtscxABcpnDTYwHX3hmr%2F3AQA19NYiIRdkoVF0J7LoJdNXybL9fo538dII%2FXP1EXukZHHI%2FbhLMgVOS4JI%2F2NXXSs3h8D5L91c2SSAweT0XIeF%2FW6uFjiQMqX%2BKqyJP1xjm0zB4pEWuHiOkelNHBiQM9kmz2VhXUPdo7vU4WVMx4lK2AKqiEk0oufLiS9VKojodkRvndE%2Bn0u3fdM%2FjqRzJJW6L9RVQcqzsH%2FDHmoEOyPg5pruX1jJDVu57L31maNjqTE8ZM6rIjOIZNx%2B8OPlN6ni8%2FtzGsPE957k8NFOW35kq1FVudoEw4SP3KKwjh27qcvR%2BR0GgniQaJODhohlbcGQVJKhuszY2dpePT1WYy4GVjMJzoZy8YNmlsujo46CUF40te2mjGHpAj9Lq7krWbHcyHcLpauoSZgaHrvepFrR9pT5cLSp%2B04XYwr3XU6FG%2B1hJEgmJ1KhhfD9yd8bRExraAwgvqWvQY6pgFRpU9YOd7%2BvXw%2FDDCXknL8do7ZlcFuJFA6XOPa4yrqHJL3SeG04ZiRB24Mz0w4z52i8xac7JycZ%2B2cv5Lz2Qb%2Bh7XuvYwD8PtdrvvIJ7160xKRFKsHHcm%2Fsdf9vfueiXpVVavrBHD9AATuu70s7Nz5fs041Ggow9FYdCAcR31SxODAZsBHY2f6DKL95ehwSLbr093GiRPZGbiKjkhEYpTE27bNXGWC&X-Amz-Signature=e0d553c5e6ae5b010c42613a90f395dfaf1ceff09e09102036226bfef82ba6ca&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U2WD6Y4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCcZxXQdWqCBRfR8EBNJZryQvPQoZRXJu6wnoGdtxb6ZAIhAJv5M1PY4WPMQCldqgdBztSIqJqYPlWb1LeUhxELkZhYKv8DCHEQABoMNjM3NDIzMTgzODA1IgwjHUoemsKbuSVje%2F4q3AP5GoNJuLDvG%2BUfkjQ%2B1nNPXolEQ8yyTK4CnCAVVBeAC1W7TovN7L4ubTpl0s%2Bb1Crc9se9EiARfmiOTkybIBPvqlSkScC9%2B8Hegfhd5UWFAh258jfpTdGLgRCYCFOOBBYzYswyFyq1rrZN7su%2Bq0uFJ1qqi49KA37R0JP%2Bs4F6%2BEEShoSYMAtaPFRGMw2jHnsXZ0iG0A6aFIOuvnWbDduMkW0RLpS5IRfmg75yiIYHCw2aV3sCNMs4VcfHs3UmKbhlNwcycGZHAGmVmCVS17Cu0WKiUxYLVm3rmU7e3atnxR6eSZ5ibJ5uISco5bdnkpLtzRgJxRFkEsLK5D8N%2FgY3O5JZX5hKknYj6U9O0qrmK1yBSUCT9F34%2BKF75nbBum7F2t61X%2BK%2B4W5qQGR%2BII1ZuSUOrot14%2F%2Bx3%2Fr3S512fOYXwF8Jgle5C3SPHwsJOSXZY2BI2ZWmFtPIvvI%2F3Pv%2FZwka5eNClaczFC9JkEeG2KRYKkMBaL5GU9%2FeM2yqmdUO2wckvv8ryrinehhh8wdIrPIM8HMpgEGiTkYPDFdZ3EWb5JAHWKDX7ZzUU7IxcZwRLglytv93Amy9s7Wdc1LaU8CE%2FjeWopokhBw89YH3GLNygGHMAhw1sVWEvDCC%2Bpa9BjqkASYrKZtmDymXg0B2sdntgRCEzh5I1C4qSCl%2BGp7BnxZVp%2F3HFBSZEt3d9Z5yagO%2FocRJMrxGKmpDQ1T6feo8Y5b%2B7TclREG3ydei%2BJy7wUcck2z4CziJjydk6Jpo%2Flfynsfeh4tVCwVfYGQVG7zHhQkWbq18Qb3sFcjZuxL6KfepdNpAKFGO7kTohpoFoG40d6Uipg%2Bm7OAvRKa9ujzjI0a1xm6Y&X-Amz-Signature=15b053edc65eb94460a200e47eac5069f67a794eea363d131417bc66cae49509&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSCN2G7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCEqE4I3IRBRiksJnacdNsr4D0bgPZF4FCzYhDNDa3I%2FQIgP9laDM7i4TAFfrmbKDE74ggF5sVGMiRoITRBgkM0cVUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEVqgW1g7Vblaf3qWSrcA5XwoBjS6onuS9oo3s7M9rPNCHKNQUa9JMQDMeNJr3zVsKdwNLRxzImYZvVqj7evbbkn8HZJ16FNnJdPtQzpkxgoTIZnhKQdLgM666vsU76cpBNjwufmP2Cy548PbFUDQYtF%2FmnExThArGs5q0l45ZQke80VnUbtPsOmNsGVCYLiO36SRjYCerTDHgBVmDsB%2F2ZyZNrQW9C89Ed4PoxTKRBCx2Nnj94lLerDSlRlQ8kM%2BzpBKVhObS3mDZPiLq78SyfZdmlnNz0T%2BsdSFLQ7MCB0bqwfHw8BEIL2UYGlIk11VFKp0xB2z9l6Z5vQzywIClCljdt4TvViBHSaJQ5uo7SGQhlGFLCK1%2FF38dk9U3w5Sc9loayishUy%2Fcs6f8Tp2ZnSFBcHbIY%2BKS%2Fv83v5XkfrOBWrbcVhbw48ZlKvBawpOp0LPmSZcAhel%2FVa%2BUmjINbt8YdaVQlAOUOOOmUfJhhFyE21iZ2twl1o13XkuzrEtbkgk7oK6Id74DthuiF%2BkCJGM4rfQjf7V1dZxwaDkh0TRppJ8vJRkcqnXSxQAfmPuu4sopuoQ7QouwzRxiHOG5ftmQsZXGaMAOOWNz8Rnfxkn3RQbB15xPJ7g1mi46at%2FfQgB%2Fmu7cpcJTxiMNb5lr0GOqUBm9rFzSia73VZEVcX80fbbTwpKEBf%2FJ8HS7OIL9RmydSpsMDTsG5lSdgQrQ1ZStslZ%2BxwMHrFT1NxJVwuclGz1vKtqwyvQCA0fyNNJCzNZtKRUMflBrvYx52mfs5zCpPOIUN57RC3lNxyHEFc0j4nz4mRA3XubdZlqtstMPWv9QDCUPlmrLFJOxwyWQS6GNk5KN02uN4acf4jCOPr7VtfGJPQ3Sun&X-Amz-Signature=e32ac7c417caf95a4c5097bd71a17691036a9e5af9826749a3ab40e89ef22686&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSCN2G7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCEqE4I3IRBRiksJnacdNsr4D0bgPZF4FCzYhDNDa3I%2FQIgP9laDM7i4TAFfrmbKDE74ggF5sVGMiRoITRBgkM0cVUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEVqgW1g7Vblaf3qWSrcA5XwoBjS6onuS9oo3s7M9rPNCHKNQUa9JMQDMeNJr3zVsKdwNLRxzImYZvVqj7evbbkn8HZJ16FNnJdPtQzpkxgoTIZnhKQdLgM666vsU76cpBNjwufmP2Cy548PbFUDQYtF%2FmnExThArGs5q0l45ZQke80VnUbtPsOmNsGVCYLiO36SRjYCerTDHgBVmDsB%2F2ZyZNrQW9C89Ed4PoxTKRBCx2Nnj94lLerDSlRlQ8kM%2BzpBKVhObS3mDZPiLq78SyfZdmlnNz0T%2BsdSFLQ7MCB0bqwfHw8BEIL2UYGlIk11VFKp0xB2z9l6Z5vQzywIClCljdt4TvViBHSaJQ5uo7SGQhlGFLCK1%2FF38dk9U3w5Sc9loayishUy%2Fcs6f8Tp2ZnSFBcHbIY%2BKS%2Fv83v5XkfrOBWrbcVhbw48ZlKvBawpOp0LPmSZcAhel%2FVa%2BUmjINbt8YdaVQlAOUOOOmUfJhhFyE21iZ2twl1o13XkuzrEtbkgk7oK6Id74DthuiF%2BkCJGM4rfQjf7V1dZxwaDkh0TRppJ8vJRkcqnXSxQAfmPuu4sopuoQ7QouwzRxiHOG5ftmQsZXGaMAOOWNz8Rnfxkn3RQbB15xPJ7g1mi46at%2FfQgB%2Fmu7cpcJTxiMNb5lr0GOqUBm9rFzSia73VZEVcX80fbbTwpKEBf%2FJ8HS7OIL9RmydSpsMDTsG5lSdgQrQ1ZStslZ%2BxwMHrFT1NxJVwuclGz1vKtqwyvQCA0fyNNJCzNZtKRUMflBrvYx52mfs5zCpPOIUN57RC3lNxyHEFc0j4nz4mRA3XubdZlqtstMPWv9QDCUPlmrLFJOxwyWQS6GNk5KN02uN4acf4jCOPr7VtfGJPQ3Sun&X-Amz-Signature=efe434f162571abc2161aca5604480dcfd4cbdc78321643128e3a74bacdb55d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSCN2G7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCEqE4I3IRBRiksJnacdNsr4D0bgPZF4FCzYhDNDa3I%2FQIgP9laDM7i4TAFfrmbKDE74ggF5sVGMiRoITRBgkM0cVUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEVqgW1g7Vblaf3qWSrcA5XwoBjS6onuS9oo3s7M9rPNCHKNQUa9JMQDMeNJr3zVsKdwNLRxzImYZvVqj7evbbkn8HZJ16FNnJdPtQzpkxgoTIZnhKQdLgM666vsU76cpBNjwufmP2Cy548PbFUDQYtF%2FmnExThArGs5q0l45ZQke80VnUbtPsOmNsGVCYLiO36SRjYCerTDHgBVmDsB%2F2ZyZNrQW9C89Ed4PoxTKRBCx2Nnj94lLerDSlRlQ8kM%2BzpBKVhObS3mDZPiLq78SyfZdmlnNz0T%2BsdSFLQ7MCB0bqwfHw8BEIL2UYGlIk11VFKp0xB2z9l6Z5vQzywIClCljdt4TvViBHSaJQ5uo7SGQhlGFLCK1%2FF38dk9U3w5Sc9loayishUy%2Fcs6f8Tp2ZnSFBcHbIY%2BKS%2Fv83v5XkfrOBWrbcVhbw48ZlKvBawpOp0LPmSZcAhel%2FVa%2BUmjINbt8YdaVQlAOUOOOmUfJhhFyE21iZ2twl1o13XkuzrEtbkgk7oK6Id74DthuiF%2BkCJGM4rfQjf7V1dZxwaDkh0TRppJ8vJRkcqnXSxQAfmPuu4sopuoQ7QouwzRxiHOG5ftmQsZXGaMAOOWNz8Rnfxkn3RQbB15xPJ7g1mi46at%2FfQgB%2Fmu7cpcJTxiMNb5lr0GOqUBm9rFzSia73VZEVcX80fbbTwpKEBf%2FJ8HS7OIL9RmydSpsMDTsG5lSdgQrQ1ZStslZ%2BxwMHrFT1NxJVwuclGz1vKtqwyvQCA0fyNNJCzNZtKRUMflBrvYx52mfs5zCpPOIUN57RC3lNxyHEFc0j4nz4mRA3XubdZlqtstMPWv9QDCUPlmrLFJOxwyWQS6GNk5KN02uN4acf4jCOPr7VtfGJPQ3Sun&X-Amz-Signature=805ef0d998e58315dbd1cd02f99bfd42753540193e94543f2c7817f04e676f02&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UALWFJ3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIC%2Bp7Jtga2NXhsY%2Fx%2BG60i3AoSy%2BhYd4353hc25E2LHjAiAsYZJmKmTfeFPDqlufEt3XZYyq8jBhSQLraCVEc%2B90vCr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM5VNWsfnkKfZODX8CKtwDes28ALuyTwwaX1tQhxcpYIL36L1VJ2kt4itazOMKJHdAgCsjNAUeir8%2F8JGiX9EHOVODbH2U3s2OJVozJ1ImNynVqnJ1y%2BzAiRABb7i28PWXFuCxw37VSkvmsyrgvnyu7CraDL7g4ZAuhYpRtnb9SEcpvf%2B1GOB4aJXWmPF%2FO5ZXw7AMEFouaigtb8thMrNY%2BiAEZ%2BOup4C97WefoTqAUuYMs4HHEl1HU7NRv%2BVZIhnTSY3XJdoYlaRK44Znv%2B%2FFbZWYV8KTOwBeQW6KjwaStaqRecqGRQ6rfo%2BQitw8emQKIuznK%2B8DbTjFKseUWAPvhrhLfv8WZWEUUCMfTpQ8Fiez42wZG9mxdyGtovsVqFlOEO7VWpiJtWeh%2BgwgLw4kNT2RUqEkOs5buOSx2AQirF55WZr%2BEXDnsdvEv%2BUzPHEi6BXwAHmXBqwZbvrGpHSG4pJDG%2FEq1ubjbQVzvkHO%2FyNKcLGnA82ndM3DOtY3hmPcdYyIR2MtCj3FcDBxu11ZOYgl5Smf0e12Lmk5aRsGUwyqdONRiTFi%2FsHYIYPtlBFc0DmGD6nJENW5alsmKNuUvRCne8XlOs69P%2BW0l6kZBCH8NDZUOro%2Brd%2FZhYBCm1Oaq2RdqQritwKu7kkwkvqWvQY6pgHxUwjeYmAn1nkvkNJq9rP6MlMi2M%2BYx5ixorkwskFVAEHesgNihpuYlm8CKgX8ddB528YG8C6vMMgXrkJcjF1A8eo2RqNlLh77TmBAjl95pa3Lzw0iugNHmG%2FWx9G%2F15H8upKDnoCyTGVmL2geF5WSdiL1Fjnjj3%2BbXsLp5DeGfp0X7q29GHh8qCDH%2By6mszp8axKRnIxi0EOenW0iZrJcZzXPHFtk&X-Amz-Signature=491f0bd49f47fb75c9d4f128fd2111f983dbb18199397d82ef76aa55eec4eb1e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LSCN2G7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCEqE4I3IRBRiksJnacdNsr4D0bgPZF4FCzYhDNDa3I%2FQIgP9laDM7i4TAFfrmbKDE74ggF5sVGMiRoITRBgkM0cVUq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDEVqgW1g7Vblaf3qWSrcA5XwoBjS6onuS9oo3s7M9rPNCHKNQUa9JMQDMeNJr3zVsKdwNLRxzImYZvVqj7evbbkn8HZJ16FNnJdPtQzpkxgoTIZnhKQdLgM666vsU76cpBNjwufmP2Cy548PbFUDQYtF%2FmnExThArGs5q0l45ZQke80VnUbtPsOmNsGVCYLiO36SRjYCerTDHgBVmDsB%2F2ZyZNrQW9C89Ed4PoxTKRBCx2Nnj94lLerDSlRlQ8kM%2BzpBKVhObS3mDZPiLq78SyfZdmlnNz0T%2BsdSFLQ7MCB0bqwfHw8BEIL2UYGlIk11VFKp0xB2z9l6Z5vQzywIClCljdt4TvViBHSaJQ5uo7SGQhlGFLCK1%2FF38dk9U3w5Sc9loayishUy%2Fcs6f8Tp2ZnSFBcHbIY%2BKS%2Fv83v5XkfrOBWrbcVhbw48ZlKvBawpOp0LPmSZcAhel%2FVa%2BUmjINbt8YdaVQlAOUOOOmUfJhhFyE21iZ2twl1o13XkuzrEtbkgk7oK6Id74DthuiF%2BkCJGM4rfQjf7V1dZxwaDkh0TRppJ8vJRkcqnXSxQAfmPuu4sopuoQ7QouwzRxiHOG5ftmQsZXGaMAOOWNz8Rnfxkn3RQbB15xPJ7g1mi46at%2FfQgB%2Fmu7cpcJTxiMNb5lr0GOqUBm9rFzSia73VZEVcX80fbbTwpKEBf%2FJ8HS7OIL9RmydSpsMDTsG5lSdgQrQ1ZStslZ%2BxwMHrFT1NxJVwuclGz1vKtqwyvQCA0fyNNJCzNZtKRUMflBrvYx52mfs5zCpPOIUN57RC3lNxyHEFc0j4nz4mRA3XubdZlqtstMPWv9QDCUPlmrLFJOxwyWQS6GNk5KN02uN4acf4jCOPr7VtfGJPQ3Sun&X-Amz-Signature=13fb64f24956cb63698e9d4dab4bd3df3a9f6659ce4047e0abe53c66623a77d5&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OOBGKS6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQD4nqvIL5lJzM8QtktG5C7iWk35GL9ALSVeH2oFCpcl2AIgbiZQl4aFR7GyDE8BbBqRZi857IleKyetDzVaeyl3tQkq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDJLnu9OHfBTKIc4fuircA5MQAhs6sTsBsXzwG3K1g0qzh2AV0zm1bY%2F8nWcYE4nQspWtAdAGbCAxgF546nz6X9knVXhTMQOF7FavfO26PzrMyEyqruMKSI8QmCSZEh47rpdzA6eS9ROyrb3%2BYHN56JSU8WTtyM8pxr%2Bobm4Z35yLH3vFaXsHwZvb6QiDLvxEc1xcZ5Ykk5qL5%2F%2FDPA%2BGNJpiVqTcWYqJOwYqDcFZ3sK2PePeOAJVaKEUdxKlmOr3s2DkCcG6GJkNELlyetfkcoeWTHTtCcitA7vOw0nNSeLQParsJraZAZaSbaXkPVaqNylYyHqjye%2Fr9LL1EXjxracESH65vLFzNdEyFWcQXJtPnZ24LoY%2BtuH9VCp8dn9yn4e1bkUdhn5SNvs%2F7B%2BbL%2FVmXS%2F2A72r1LZWuEYRk%2FJvQI%2ByZRUlIE7EcgZrdfAuI7v%2BuU13FxKDkyKbfqhkmZ1FM7nOZ%2FhIVA0k1IBB0J2dt8USvc9YBUTZl2okNbRKUyE%2FLuZA%2BT7uqIGWdpxZL7zCKwFcKH6mZGH%2FXUhXoKi4sbaNIyxE8c%2FE6NID3L5uRkoEqi1PocdgE1Xs3XpH7ByTrgpN7u2JEVWfhyiib4SNVd%2B0YPJpdpLZBvXonWHbJX7Kh8KnKKi3u2QlMIP6lr0GOqUB%2BPYvP92MX8MOV%2B2NfQdKHmwI6ZEL5hcg8u28aBPbS72aBtkHCe57MR8buLr5cIT%2B5rK2iLTm%2BTeUPXYchaTn7EdAQEfHyKspnuj02rrUglEC0nASxJMYcfVx4c3I7APTHPjFuqgvDwDMWbCbyFXUAMbdtLwW4cAsK3i%2FLETj43yOZWzB9lBcjM%2BbJGy640bENO3bmRMeIkH4jkUbm60lwV5gdFcf&X-Amz-Signature=65daeaf7413c216290b40679f74a004801630d3ba7af0662de32c8f44292d133&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW7RZOZK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDHGTyRtYxCjZqa18GEmTpdz97vMC4iPJTBxZRXxyDCdAIgd76QpLG73utmF3kowYe2EmKW%2BlXqOEPcvQ01jhkbmwoq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBuyku0F585N%2FHExbSrcA7BxOlWZp%2F2dtN2QJLnNi8LN1X%2BlNAoBB0SI%2FoWu%2FRnDb83lvay88O8UdoATUYiJaFMda7M%2BwxV0hoCf4YP%2B2ox%2B8geMr7zwKvFQeWPWawCRsYVxUZCTH%2BGCgaUgoSgb1CeNNZjE8PtFwmBqu6tusD1i8DXptJg0xCX8m3pWIpE6t1VXKnP5pU4pv8o07E7AbYIVYJ1KCuO4PKA4VChnCP7iPDN%2BPbiM%2FTJFPRGZqdrHE0TvdLu5tx1aSvqgwEyvXPle%2BryeLrUZeQecouex%2FwXqqNmUBPre%2FnreaBhsyNXXUm5OT0o9DDjp1KzJZfJlT8QM%2FSPOREL1sAbALzp9RLoN6KLkKS6hjcR0C1f%2FTFCdGwoTTlHXJE9PIzL9aVRT9VbeLEJs3TiiDaYuhd%2BXefhkOWpOpskp08YqRlrh0RLIWPn%2BqOWly%2B0o%2F9CMUAWN9FHuQ1KQBFv2JYr5mWkqVlz4ibPAhqjoIgNomIRK0i474uLGcnoH7dVqVC3YHzK0vVGqRNtAUGy%2BJEZWJo15Is94LgH%2Fx9kF8pY4gmWrDFCtt%2Belp4fCEAl73vSE%2BNUJPr0G5s8DnD4pEXMth4JZYC9%2BKpvg8mQyHvi9QwKCLgx3Zc3g4ZXU3AixCQVZMMv5lr0GOqUBaS3e8RiGCi0cI9NsKl%2FF5eNl%2FeBuJVTar7zlSmOypncGAK3tNft9WP1l8TT9FhqOiJv2B7uKDu3NTCwxyQRq3SOmGBBlkRa540bhaMGp%2BLzhJR8yWU9sfQV6jHDFK0Ox8%2FmNhcGtPgRTA5YTHA2846ZyYaOQ45tS4wliC5ke1slf5%2Brgdo7L37g2%2BLCKS1kZ51WGSaELZBFCVyCSWFWDXZ4CD402&X-Amz-Signature=6ea536a36e0db55e748a0465dd8527b17dd277cd153853afae4e6cdab7d8a534&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW7RZOZK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDHGTyRtYxCjZqa18GEmTpdz97vMC4iPJTBxZRXxyDCdAIgd76QpLG73utmF3kowYe2EmKW%2BlXqOEPcvQ01jhkbmwoq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBuyku0F585N%2FHExbSrcA7BxOlWZp%2F2dtN2QJLnNi8LN1X%2BlNAoBB0SI%2FoWu%2FRnDb83lvay88O8UdoATUYiJaFMda7M%2BwxV0hoCf4YP%2B2ox%2B8geMr7zwKvFQeWPWawCRsYVxUZCTH%2BGCgaUgoSgb1CeNNZjE8PtFwmBqu6tusD1i8DXptJg0xCX8m3pWIpE6t1VXKnP5pU4pv8o07E7AbYIVYJ1KCuO4PKA4VChnCP7iPDN%2BPbiM%2FTJFPRGZqdrHE0TvdLu5tx1aSvqgwEyvXPle%2BryeLrUZeQecouex%2FwXqqNmUBPre%2FnreaBhsyNXXUm5OT0o9DDjp1KzJZfJlT8QM%2FSPOREL1sAbALzp9RLoN6KLkKS6hjcR0C1f%2FTFCdGwoTTlHXJE9PIzL9aVRT9VbeLEJs3TiiDaYuhd%2BXefhkOWpOpskp08YqRlrh0RLIWPn%2BqOWly%2B0o%2F9CMUAWN9FHuQ1KQBFv2JYr5mWkqVlz4ibPAhqjoIgNomIRK0i474uLGcnoH7dVqVC3YHzK0vVGqRNtAUGy%2BJEZWJo15Is94LgH%2Fx9kF8pY4gmWrDFCtt%2Belp4fCEAl73vSE%2BNUJPr0G5s8DnD4pEXMth4JZYC9%2BKpvg8mQyHvi9QwKCLgx3Zc3g4ZXU3AixCQVZMMv5lr0GOqUBaS3e8RiGCi0cI9NsKl%2FF5eNl%2FeBuJVTar7zlSmOypncGAK3tNft9WP1l8TT9FhqOiJv2B7uKDu3NTCwxyQRq3SOmGBBlkRa540bhaMGp%2BLzhJR8yWU9sfQV6jHDFK0Ox8%2FmNhcGtPgRTA5YTHA2846ZyYaOQ45tS4wliC5ke1slf5%2Brgdo7L37g2%2BLCKS1kZ51WGSaELZBFCVyCSWFWDXZ4CD402&X-Amz-Signature=0187320ede0e4ebea79965bd0cea750d899682d0fc3fedbb424d3953908df769&X-Amz-SignedHeaders=host&x-id=GetObject)

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
