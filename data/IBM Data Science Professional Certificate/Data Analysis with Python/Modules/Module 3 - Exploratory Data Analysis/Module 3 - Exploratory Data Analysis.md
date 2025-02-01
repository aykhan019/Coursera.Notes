

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMMKQCUX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BG0UPJRBMYsOHITHqPdaECf46v9mN468OIzpr8c03OAIhALmFad5MV2e%2BBOZpmh9IDHWc7t1eDi8hwDA4UDh2P23bKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyt0vG05e1EogXoc3Eq3ANxwyAonmBDHCXG2sc4WYenyrqb8fGbaWxcdIEtnY1nKCOlJ%2B4lq5AeuJTW6Jhv0ibKxiM6hBZY3MkmCM%2BlfX%2BwZGowYFBsYg8rRzkojo%2FH%2BQu1VMx%2BODqfVfEY7Nk%2FB0LkNqgZaYruLLX6kmErV7b%2BLhpgMIe8LZNJ5bihVFidmpIxI5sDCQjlVz6A9gnxgMdfx%2BeKlAz%2FexCXVrojHOYYIiJVn8hMheqhfijs8A7rJRLhvws4%2BsQyE1%2B9g6k9J3AmE917xZ7t9lW42tKUSZd36PRYZNoSafW6BwnIK6U8J78oWqEyRmpnxjvGljv0CWE2gKbe4%2Fxk0wU7kylB1pCCRgDE6EQDEhqwQRa20Epu8c1p2RruTyriXEcZeF9DmyGgejxH%2FwiSxVgEs4b0v6jLmHtEx2S2%2BXk4U6QiWfqrLhuaRmKfq24Xfv2E%2FJI4o3Vvb0ICWqMcsfmnlwhmDvj888ZCNuw8MF4a6xUKXjMZCVkZRmWqFXwS9QRoBCO4p15uH87%2FMs9bajugSL02ww0JXadCW4vBOvoTtAijwJ%2FeLnwGj1a63FavBi9pN1hk0ODYTr7ittUAvKdBIGOQntr6FfuAgufD1rzwgmasd7cieVH1BCXwXRpzLoSulDCyyPi8BjqkASoYPfaG4rS5KEHMBd8FWeRAFqcHiXT8cXjSzBFh8JdlbDwCIF9akFs%2FGNK244Oub9oHs9sHGp2cAJCH7btBTLEoAHsMcCg%2FDQuf517Qo2DldbyDE%2FBDl%2FITMJEAL0UCPW3sjMeCcgZUKiI8ZZUy1NeVztNBGnvq9d%2FGs1xj6O%2BYkwWEvNXr4plvfkLzSqN2BT5Jv3hrHUvMz4LPR%2BxEhCzZYGbv&X-Amz-Signature=96bbc27c5a8f59e48c2b9cb455a167ebedb4376588bee25aa5d6aebeba05258b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMMKQCUX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BG0UPJRBMYsOHITHqPdaECf46v9mN468OIzpr8c03OAIhALmFad5MV2e%2BBOZpmh9IDHWc7t1eDi8hwDA4UDh2P23bKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyt0vG05e1EogXoc3Eq3ANxwyAonmBDHCXG2sc4WYenyrqb8fGbaWxcdIEtnY1nKCOlJ%2B4lq5AeuJTW6Jhv0ibKxiM6hBZY3MkmCM%2BlfX%2BwZGowYFBsYg8rRzkojo%2FH%2BQu1VMx%2BODqfVfEY7Nk%2FB0LkNqgZaYruLLX6kmErV7b%2BLhpgMIe8LZNJ5bihVFidmpIxI5sDCQjlVz6A9gnxgMdfx%2BeKlAz%2FexCXVrojHOYYIiJVn8hMheqhfijs8A7rJRLhvws4%2BsQyE1%2B9g6k9J3AmE917xZ7t9lW42tKUSZd36PRYZNoSafW6BwnIK6U8J78oWqEyRmpnxjvGljv0CWE2gKbe4%2Fxk0wU7kylB1pCCRgDE6EQDEhqwQRa20Epu8c1p2RruTyriXEcZeF9DmyGgejxH%2FwiSxVgEs4b0v6jLmHtEx2S2%2BXk4U6QiWfqrLhuaRmKfq24Xfv2E%2FJI4o3Vvb0ICWqMcsfmnlwhmDvj888ZCNuw8MF4a6xUKXjMZCVkZRmWqFXwS9QRoBCO4p15uH87%2FMs9bajugSL02ww0JXadCW4vBOvoTtAijwJ%2FeLnwGj1a63FavBi9pN1hk0ODYTr7ittUAvKdBIGOQntr6FfuAgufD1rzwgmasd7cieVH1BCXwXRpzLoSulDCyyPi8BjqkASoYPfaG4rS5KEHMBd8FWeRAFqcHiXT8cXjSzBFh8JdlbDwCIF9akFs%2FGNK244Oub9oHs9sHGp2cAJCH7btBTLEoAHsMcCg%2FDQuf517Qo2DldbyDE%2FBDl%2FITMJEAL0UCPW3sjMeCcgZUKiI8ZZUy1NeVztNBGnvq9d%2FGs1xj6O%2BYkwWEvNXr4plvfkLzSqN2BT5Jv3hrHUvMz4LPR%2BxEhCzZYGbv&X-Amz-Signature=d8ac959cc8b7f5be43c7377e4db144bf9cd7e064109ce09619546013eefc9655&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMMKQCUX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BG0UPJRBMYsOHITHqPdaECf46v9mN468OIzpr8c03OAIhALmFad5MV2e%2BBOZpmh9IDHWc7t1eDi8hwDA4UDh2P23bKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyt0vG05e1EogXoc3Eq3ANxwyAonmBDHCXG2sc4WYenyrqb8fGbaWxcdIEtnY1nKCOlJ%2B4lq5AeuJTW6Jhv0ibKxiM6hBZY3MkmCM%2BlfX%2BwZGowYFBsYg8rRzkojo%2FH%2BQu1VMx%2BODqfVfEY7Nk%2FB0LkNqgZaYruLLX6kmErV7b%2BLhpgMIe8LZNJ5bihVFidmpIxI5sDCQjlVz6A9gnxgMdfx%2BeKlAz%2FexCXVrojHOYYIiJVn8hMheqhfijs8A7rJRLhvws4%2BsQyE1%2B9g6k9J3AmE917xZ7t9lW42tKUSZd36PRYZNoSafW6BwnIK6U8J78oWqEyRmpnxjvGljv0CWE2gKbe4%2Fxk0wU7kylB1pCCRgDE6EQDEhqwQRa20Epu8c1p2RruTyriXEcZeF9DmyGgejxH%2FwiSxVgEs4b0v6jLmHtEx2S2%2BXk4U6QiWfqrLhuaRmKfq24Xfv2E%2FJI4o3Vvb0ICWqMcsfmnlwhmDvj888ZCNuw8MF4a6xUKXjMZCVkZRmWqFXwS9QRoBCO4p15uH87%2FMs9bajugSL02ww0JXadCW4vBOvoTtAijwJ%2FeLnwGj1a63FavBi9pN1hk0ODYTr7ittUAvKdBIGOQntr6FfuAgufD1rzwgmasd7cieVH1BCXwXRpzLoSulDCyyPi8BjqkASoYPfaG4rS5KEHMBd8FWeRAFqcHiXT8cXjSzBFh8JdlbDwCIF9akFs%2FGNK244Oub9oHs9sHGp2cAJCH7btBTLEoAHsMcCg%2FDQuf517Qo2DldbyDE%2FBDl%2FITMJEAL0UCPW3sjMeCcgZUKiI8ZZUy1NeVztNBGnvq9d%2FGs1xj6O%2BYkwWEvNXr4plvfkLzSqN2BT5Jv3hrHUvMz4LPR%2BxEhCzZYGbv&X-Amz-Signature=8a466e2c00ad1fd810aa23db7cbf61e87e9024220841b1af1ba82df01252ff58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667ZK6P4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3kxAnjDfGuRACgYV92a0SJGgKzblfPduRgQzS689SfAiEAgFBHBaODZGCl%2FovQZKGXDovg6GK5u9Kn9e2LnByM5wQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEu7beJ%2FAXcVMadGyrcA1t0NspalrwZbqWGpYg%2BSo9wFqWQadfkrkzdgBNoR19kSK96tFUf7Ps02Y4mGes4qs0OyxpjMeLi9SQoReIWIA23aqx2jD4dDsH8o4c%2BXoapSN8u76eNiBJHvCg6H2p%2BiQr6KSNKkrGYRm5V%2BndiHPU9Zf8iydVKD%2BfWtFXeNiVRhPJyZvdGgs%2FpOqm8jRA4%2BVXQYwvX%2F0ANtmsEhbnrIM2mS6ZX3FOwI8zhprEV%2FXR%2BFiLY3fj00GWlbOSG4yLH8DcjbVKtXjmvaiZAjLuxfi1kszRdeFgCY1ncp%2B9mSxMeq%2FpQbYRpp7ueJWpizV72T9zBO%2FUzOSxokbR1hDrBFJEc%2Bfr7PWodCOVVlTI%2FIMwoq57T%2FMeX3O96vZwhxY0hdZZ0lmKlFyBUGFGnG%2BiUCQM%2FLqx2MmR%2FILcpDxoSfk52hyjLntII0j5uZVbqwqbvCpIp2Ewr%2FYcqBuXC%2FEu8Upucj4cyyJg8KYAXBdLAQZw1D9c4T9Hl%2FQrwsVq2uX%2Fby8Z7t%2FKPb1Px3VTVAEO5f2R1dkoZlV7jWpJd3SVbxqbM3e%2BWYrU3FLSVwHT4BPHxxJhMO4Umm2XMDVQ7yY0UKw7ClhHGdvm0WUL48M3sHmCYDgb%2BJKYsyuYXJqoCMJLJ%2BLwGOqUBxVc4GN7EUJmSzYzytmWogix6gugwj1W05cImSuP3ReZh4m50ZLzGeTLEYApEEhJbWToPR1shj%2Fa6Vs17nk6frXce%2FCTcj4iVWo9iG%2B3IEXRxovsjZl3dE%2Bzc1oH2LdWYxs9A1ybUs%2B7nS5GPvp313UstpHeQvnqI712V7gXqW%2FgYXwbpO9dqgZqaFyROBdUGWslTvCiUO%2BTnv777%2BO%2BZ2JLW9OBA&X-Amz-Signature=93897b50453f25f695269e5c0d65f2a65718a4bce56b8db4d6a2aea3d0a7bca5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667ZK6P4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3kxAnjDfGuRACgYV92a0SJGgKzblfPduRgQzS689SfAiEAgFBHBaODZGCl%2FovQZKGXDovg6GK5u9Kn9e2LnByM5wQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEu7beJ%2FAXcVMadGyrcA1t0NspalrwZbqWGpYg%2BSo9wFqWQadfkrkzdgBNoR19kSK96tFUf7Ps02Y4mGes4qs0OyxpjMeLi9SQoReIWIA23aqx2jD4dDsH8o4c%2BXoapSN8u76eNiBJHvCg6H2p%2BiQr6KSNKkrGYRm5V%2BndiHPU9Zf8iydVKD%2BfWtFXeNiVRhPJyZvdGgs%2FpOqm8jRA4%2BVXQYwvX%2F0ANtmsEhbnrIM2mS6ZX3FOwI8zhprEV%2FXR%2BFiLY3fj00GWlbOSG4yLH8DcjbVKtXjmvaiZAjLuxfi1kszRdeFgCY1ncp%2B9mSxMeq%2FpQbYRpp7ueJWpizV72T9zBO%2FUzOSxokbR1hDrBFJEc%2Bfr7PWodCOVVlTI%2FIMwoq57T%2FMeX3O96vZwhxY0hdZZ0lmKlFyBUGFGnG%2BiUCQM%2FLqx2MmR%2FILcpDxoSfk52hyjLntII0j5uZVbqwqbvCpIp2Ewr%2FYcqBuXC%2FEu8Upucj4cyyJg8KYAXBdLAQZw1D9c4T9Hl%2FQrwsVq2uX%2Fby8Z7t%2FKPb1Px3VTVAEO5f2R1dkoZlV7jWpJd3SVbxqbM3e%2BWYrU3FLSVwHT4BPHxxJhMO4Umm2XMDVQ7yY0UKw7ClhHGdvm0WUL48M3sHmCYDgb%2BJKYsyuYXJqoCMJLJ%2BLwGOqUBxVc4GN7EUJmSzYzytmWogix6gugwj1W05cImSuP3ReZh4m50ZLzGeTLEYApEEhJbWToPR1shj%2Fa6Vs17nk6frXce%2FCTcj4iVWo9iG%2B3IEXRxovsjZl3dE%2Bzc1oH2LdWYxs9A1ybUs%2B7nS5GPvp313UstpHeQvnqI712V7gXqW%2FgYXwbpO9dqgZqaFyROBdUGWslTvCiUO%2BTnv777%2BO%2BZ2JLW9OBA&X-Amz-Signature=fbb2ef733436d49794a42268880ace2b1e4cd145bf78ba43de64527d40cc700d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667ZK6P4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3kxAnjDfGuRACgYV92a0SJGgKzblfPduRgQzS689SfAiEAgFBHBaODZGCl%2FovQZKGXDovg6GK5u9Kn9e2LnByM5wQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEu7beJ%2FAXcVMadGyrcA1t0NspalrwZbqWGpYg%2BSo9wFqWQadfkrkzdgBNoR19kSK96tFUf7Ps02Y4mGes4qs0OyxpjMeLi9SQoReIWIA23aqx2jD4dDsH8o4c%2BXoapSN8u76eNiBJHvCg6H2p%2BiQr6KSNKkrGYRm5V%2BndiHPU9Zf8iydVKD%2BfWtFXeNiVRhPJyZvdGgs%2FpOqm8jRA4%2BVXQYwvX%2F0ANtmsEhbnrIM2mS6ZX3FOwI8zhprEV%2FXR%2BFiLY3fj00GWlbOSG4yLH8DcjbVKtXjmvaiZAjLuxfi1kszRdeFgCY1ncp%2B9mSxMeq%2FpQbYRpp7ueJWpizV72T9zBO%2FUzOSxokbR1hDrBFJEc%2Bfr7PWodCOVVlTI%2FIMwoq57T%2FMeX3O96vZwhxY0hdZZ0lmKlFyBUGFGnG%2BiUCQM%2FLqx2MmR%2FILcpDxoSfk52hyjLntII0j5uZVbqwqbvCpIp2Ewr%2FYcqBuXC%2FEu8Upucj4cyyJg8KYAXBdLAQZw1D9c4T9Hl%2FQrwsVq2uX%2Fby8Z7t%2FKPb1Px3VTVAEO5f2R1dkoZlV7jWpJd3SVbxqbM3e%2BWYrU3FLSVwHT4BPHxxJhMO4Umm2XMDVQ7yY0UKw7ClhHGdvm0WUL48M3sHmCYDgb%2BJKYsyuYXJqoCMJLJ%2BLwGOqUBxVc4GN7EUJmSzYzytmWogix6gugwj1W05cImSuP3ReZh4m50ZLzGeTLEYApEEhJbWToPR1shj%2Fa6Vs17nk6frXce%2FCTcj4iVWo9iG%2B3IEXRxovsjZl3dE%2Bzc1oH2LdWYxs9A1ybUs%2B7nS5GPvp313UstpHeQvnqI712V7gXqW%2FgYXwbpO9dqgZqaFyROBdUGWslTvCiUO%2BTnv777%2BO%2BZ2JLW9OBA&X-Amz-Signature=1dfa521aeff4c19d04b564bfede1ecbef87c53d30f3f45c9a2ca3a945d3905c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667ZK6P4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3kxAnjDfGuRACgYV92a0SJGgKzblfPduRgQzS689SfAiEAgFBHBaODZGCl%2FovQZKGXDovg6GK5u9Kn9e2LnByM5wQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEu7beJ%2FAXcVMadGyrcA1t0NspalrwZbqWGpYg%2BSo9wFqWQadfkrkzdgBNoR19kSK96tFUf7Ps02Y4mGes4qs0OyxpjMeLi9SQoReIWIA23aqx2jD4dDsH8o4c%2BXoapSN8u76eNiBJHvCg6H2p%2BiQr6KSNKkrGYRm5V%2BndiHPU9Zf8iydVKD%2BfWtFXeNiVRhPJyZvdGgs%2FpOqm8jRA4%2BVXQYwvX%2F0ANtmsEhbnrIM2mS6ZX3FOwI8zhprEV%2FXR%2BFiLY3fj00GWlbOSG4yLH8DcjbVKtXjmvaiZAjLuxfi1kszRdeFgCY1ncp%2B9mSxMeq%2FpQbYRpp7ueJWpizV72T9zBO%2FUzOSxokbR1hDrBFJEc%2Bfr7PWodCOVVlTI%2FIMwoq57T%2FMeX3O96vZwhxY0hdZZ0lmKlFyBUGFGnG%2BiUCQM%2FLqx2MmR%2FILcpDxoSfk52hyjLntII0j5uZVbqwqbvCpIp2Ewr%2FYcqBuXC%2FEu8Upucj4cyyJg8KYAXBdLAQZw1D9c4T9Hl%2FQrwsVq2uX%2Fby8Z7t%2FKPb1Px3VTVAEO5f2R1dkoZlV7jWpJd3SVbxqbM3e%2BWYrU3FLSVwHT4BPHxxJhMO4Umm2XMDVQ7yY0UKw7ClhHGdvm0WUL48M3sHmCYDgb%2BJKYsyuYXJqoCMJLJ%2BLwGOqUBxVc4GN7EUJmSzYzytmWogix6gugwj1W05cImSuP3ReZh4m50ZLzGeTLEYApEEhJbWToPR1shj%2Fa6Vs17nk6frXce%2FCTcj4iVWo9iG%2B3IEXRxovsjZl3dE%2Bzc1oH2LdWYxs9A1ybUs%2B7nS5GPvp313UstpHeQvnqI712V7gXqW%2FgYXwbpO9dqgZqaFyROBdUGWslTvCiUO%2BTnv777%2BO%2BZ2JLW9OBA&X-Amz-Signature=98bbf4ba56861e7ed0fe368133f980c72064c5ba99446ee186d9efd767ab6e40&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667ZK6P4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3kxAnjDfGuRACgYV92a0SJGgKzblfPduRgQzS689SfAiEAgFBHBaODZGCl%2FovQZKGXDovg6GK5u9Kn9e2LnByM5wQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEu7beJ%2FAXcVMadGyrcA1t0NspalrwZbqWGpYg%2BSo9wFqWQadfkrkzdgBNoR19kSK96tFUf7Ps02Y4mGes4qs0OyxpjMeLi9SQoReIWIA23aqx2jD4dDsH8o4c%2BXoapSN8u76eNiBJHvCg6H2p%2BiQr6KSNKkrGYRm5V%2BndiHPU9Zf8iydVKD%2BfWtFXeNiVRhPJyZvdGgs%2FpOqm8jRA4%2BVXQYwvX%2F0ANtmsEhbnrIM2mS6ZX3FOwI8zhprEV%2FXR%2BFiLY3fj00GWlbOSG4yLH8DcjbVKtXjmvaiZAjLuxfi1kszRdeFgCY1ncp%2B9mSxMeq%2FpQbYRpp7ueJWpizV72T9zBO%2FUzOSxokbR1hDrBFJEc%2Bfr7PWodCOVVlTI%2FIMwoq57T%2FMeX3O96vZwhxY0hdZZ0lmKlFyBUGFGnG%2BiUCQM%2FLqx2MmR%2FILcpDxoSfk52hyjLntII0j5uZVbqwqbvCpIp2Ewr%2FYcqBuXC%2FEu8Upucj4cyyJg8KYAXBdLAQZw1D9c4T9Hl%2FQrwsVq2uX%2Fby8Z7t%2FKPb1Px3VTVAEO5f2R1dkoZlV7jWpJd3SVbxqbM3e%2BWYrU3FLSVwHT4BPHxxJhMO4Umm2XMDVQ7yY0UKw7ClhHGdvm0WUL48M3sHmCYDgb%2BJKYsyuYXJqoCMJLJ%2BLwGOqUBxVc4GN7EUJmSzYzytmWogix6gugwj1W05cImSuP3ReZh4m50ZLzGeTLEYApEEhJbWToPR1shj%2Fa6Vs17nk6frXce%2FCTcj4iVWo9iG%2B3IEXRxovsjZl3dE%2Bzc1oH2LdWYxs9A1ybUs%2B7nS5GPvp313UstpHeQvnqI712V7gXqW%2FgYXwbpO9dqgZqaFyROBdUGWslTvCiUO%2BTnv777%2BO%2BZ2JLW9OBA&X-Amz-Signature=926581d0a1ddebda6b49e603bd1e89bc2601ecf6e3db8e90ee9568cf200d3b23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667ZK6P4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3kxAnjDfGuRACgYV92a0SJGgKzblfPduRgQzS689SfAiEAgFBHBaODZGCl%2FovQZKGXDovg6GK5u9Kn9e2LnByM5wQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEu7beJ%2FAXcVMadGyrcA1t0NspalrwZbqWGpYg%2BSo9wFqWQadfkrkzdgBNoR19kSK96tFUf7Ps02Y4mGes4qs0OyxpjMeLi9SQoReIWIA23aqx2jD4dDsH8o4c%2BXoapSN8u76eNiBJHvCg6H2p%2BiQr6KSNKkrGYRm5V%2BndiHPU9Zf8iydVKD%2BfWtFXeNiVRhPJyZvdGgs%2FpOqm8jRA4%2BVXQYwvX%2F0ANtmsEhbnrIM2mS6ZX3FOwI8zhprEV%2FXR%2BFiLY3fj00GWlbOSG4yLH8DcjbVKtXjmvaiZAjLuxfi1kszRdeFgCY1ncp%2B9mSxMeq%2FpQbYRpp7ueJWpizV72T9zBO%2FUzOSxokbR1hDrBFJEc%2Bfr7PWodCOVVlTI%2FIMwoq57T%2FMeX3O96vZwhxY0hdZZ0lmKlFyBUGFGnG%2BiUCQM%2FLqx2MmR%2FILcpDxoSfk52hyjLntII0j5uZVbqwqbvCpIp2Ewr%2FYcqBuXC%2FEu8Upucj4cyyJg8KYAXBdLAQZw1D9c4T9Hl%2FQrwsVq2uX%2Fby8Z7t%2FKPb1Px3VTVAEO5f2R1dkoZlV7jWpJd3SVbxqbM3e%2BWYrU3FLSVwHT4BPHxxJhMO4Umm2XMDVQ7yY0UKw7ClhHGdvm0WUL48M3sHmCYDgb%2BJKYsyuYXJqoCMJLJ%2BLwGOqUBxVc4GN7EUJmSzYzytmWogix6gugwj1W05cImSuP3ReZh4m50ZLzGeTLEYApEEhJbWToPR1shj%2Fa6Vs17nk6frXce%2FCTcj4iVWo9iG%2B3IEXRxovsjZl3dE%2Bzc1oH2LdWYxs9A1ybUs%2B7nS5GPvp313UstpHeQvnqI712V7gXqW%2FgYXwbpO9dqgZqaFyROBdUGWslTvCiUO%2BTnv777%2BO%2BZ2JLW9OBA&X-Amz-Signature=1baaee07003df512f7b70be7b71feef6a43283f999ce19ac8e8808cc9d0dd101&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN4DSMBN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF23gQTxhCDq5xfokvlhxHT1RhbIIYgCm0Xfi%2BZKiW%2FRAiAcTtlCEWyclBlkPvGLb%2BEb0pYFacQreg%2B5Avrci7DyqCqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr9Gzpc6OIIU25yVOKtwD1EEUG375hPhL3L%2BfdwSXeU9rV7ppj4KcQEO4nvM%2BRsuhIoEsSrChkrVo5JgG5fwMGtlz27zq83kO3po81%2FTfdqMBFPhfbiAZH7XB3KeolV0cT6tbHNAtNqE9YorprmlLH4%2F3%2F6C%2FG2oYQqD2HU%2BRL2Tcrt7JwQqgoIaOmKSdUsPcGoN9i7DiUZrQpXlq5lWQJqLYA%2BpK%2B27BNYq%2FgLO6y697J4VQ%2Fqz2ILO1fJezJLa0OCP8Ls9%2Fv3YV3CgfPhD%2F6OPmmQbkukDB%2Fx17DCS5rpE87TTnp6aYy4rZW0GUqS44wtRLAwNytSLDUJJWBhaxWXNyiHSC2liI%2FuIn8SQy3AXQFBfSG534EJjz1sRzqKSuPtbRMeRfGWV2TCbI9Ra4ai3mghOJ3r8rfCkbYk4%2BchXW3gqTJksLe0P8ZA9ABYWsQho6OJXos5a5P49J%2FcP4qxdKk3BD1ObiYRz5qEBkMWjnuBfJxVsuFI89nnhT0%2BFlUhQ0H1xoe2wvUkSvI1vNApC9mUEHRa%2Br34PLtmy8wNqAlatImZLRW1BRI9hFAf2rDWyMTtSNVwxN4IrgCveAqWoT37cXhJePgcv4VNb6e8zyWB9xnbs7SwVcHM235A7vUvBR8hyFyupM6KIwscD4vAY6pgGdEPilrVr53BaqvDbfEla7DMUZTv%2FRgrq00qA8bcMhGzF%2BI1yWm%2FRE5hWt0GZkjFBYRQRYNe8TCx9srLFJ6TdEQywGAuyWdW6JsraHecuBD%2F87hFQKPuTzkuaemTCfl4LFy4gnTJCoQR5M%2FAv%2B0RPUES0WDtoxvVHeH47kGhpOygd1VPqqs7qllXnxSMCMR%2B%2FFYfxowSixmrAPSC0yzj%2F%2BUCWXVEGy&X-Amz-Signature=e911ed19b835bfd16a0a88bbc1767b29366102de21cce89aa25b40890889f8a1&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSJPH7ID%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDTl%2FjBgfNZ9rgMloRLkUDmQRYqMW%2B45oOi73%2F1yLwwXAiAZ36HaGwF8TpHXm47DmcLXxHXt0zX3qtE5KCGHu9mkXSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv4d3GcRTvrSjQzXpKtwDedNbDo8ENcWzDVQlZf7rU%2FG4gsSeXPMX7xBPwjDE90%2Bb2p8fKTlckD9X3zxJmwwzqSBMnOvVKV4Gq8QYnXrp%2BcRztmwHJPwe9n%2FDpTRIeYFJ2Z3u9zt%2BV4gtkKFd01r8oiRVn13%2BJuMnsClh7ZNE4xqhcQ%2BBC4%2Bro01chtypZ7pMEDCH%2F6F9gXfHu%2FzSw6ZEFhPe%2BmQ1JU6weTmds3c7agW2%2F%2BbDnWq%2Fkv7xpRjf3cWnomY6yustlKEsGQTc6bo5iyf%2BZrw%2F%2B9Kh30c7U9J%2Bpa9%2FWSFGMY9%2BYrJMRWqcF%2BqBlpL8fZFsQMGgawOLj%2FlCGOJ9Lk1TziJhrngWp4aZk0GDW40XeAShx9LjxpGKJ0%2BFSgfa9xBkKUNbw5KgTl7FeRpF0Xf4ggwxsOtHq4RmNCeR%2BAx2c9GjgaRdya6a6dLeWGq0kjTyvs2FyyETzgm4PH1DmLvon6mFGI8cPkTxssqzAu63UBrw9iM3rO1vehnEbYvUOj3QAn%2FbFo9Wf1fivk49hv8O8olrQIlms6mu%2F5GbVYU62cfv3AzrsXgzpntSsGdaI3fKYx68TwnG59juyONaj3VV%2BiFqcVWqQ3s4hC3D1Vr3dkEul%2BPyZE6GMf87hO8dYdbMhMZW94Uw%2Bsr4vAY6pgEO3w9C6LMaKnYIq5kpSYwFqPPpHEf7lZb35clrWKAwzZQJ7kCbY9K6lAKvKnjIVeU4yhlXSiNxGuACdvrAAYhN4iEXAxEDHtzXyA9RV49844zx9V5hjE5eSs%2B%2B0YFSdWtQ93q7N%2BEGLESMkp5ugqCEnMZe%2FNjioUfqpdWBmrEeFCGVpn1hCm%2B1Oxl%2FZSa%2BWUdK1k8fX4QZYrJpxACz8eMjS4jXcKdO&X-Amz-Signature=187373f5d63eee8d7ccf41d28ef3fa71ab5e8d3d2f40a0aeda87b3bf3274431c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667ZK6P4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3kxAnjDfGuRACgYV92a0SJGgKzblfPduRgQzS689SfAiEAgFBHBaODZGCl%2FovQZKGXDovg6GK5u9Kn9e2LnByM5wQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEu7beJ%2FAXcVMadGyrcA1t0NspalrwZbqWGpYg%2BSo9wFqWQadfkrkzdgBNoR19kSK96tFUf7Ps02Y4mGes4qs0OyxpjMeLi9SQoReIWIA23aqx2jD4dDsH8o4c%2BXoapSN8u76eNiBJHvCg6H2p%2BiQr6KSNKkrGYRm5V%2BndiHPU9Zf8iydVKD%2BfWtFXeNiVRhPJyZvdGgs%2FpOqm8jRA4%2BVXQYwvX%2F0ANtmsEhbnrIM2mS6ZX3FOwI8zhprEV%2FXR%2BFiLY3fj00GWlbOSG4yLH8DcjbVKtXjmvaiZAjLuxfi1kszRdeFgCY1ncp%2B9mSxMeq%2FpQbYRpp7ueJWpizV72T9zBO%2FUzOSxokbR1hDrBFJEc%2Bfr7PWodCOVVlTI%2FIMwoq57T%2FMeX3O96vZwhxY0hdZZ0lmKlFyBUGFGnG%2BiUCQM%2FLqx2MmR%2FILcpDxoSfk52hyjLntII0j5uZVbqwqbvCpIp2Ewr%2FYcqBuXC%2FEu8Upucj4cyyJg8KYAXBdLAQZw1D9c4T9Hl%2FQrwsVq2uX%2Fby8Z7t%2FKPb1Px3VTVAEO5f2R1dkoZlV7jWpJd3SVbxqbM3e%2BWYrU3FLSVwHT4BPHxxJhMO4Umm2XMDVQ7yY0UKw7ClhHGdvm0WUL48M3sHmCYDgb%2BJKYsyuYXJqoCMJLJ%2BLwGOqUBxVc4GN7EUJmSzYzytmWogix6gugwj1W05cImSuP3ReZh4m50ZLzGeTLEYApEEhJbWToPR1shj%2Fa6Vs17nk6frXce%2FCTcj4iVWo9iG%2B3IEXRxovsjZl3dE%2Bzc1oH2LdWYxs9A1ybUs%2B7nS5GPvp313UstpHeQvnqI712V7gXqW%2FgYXwbpO9dqgZqaFyROBdUGWslTvCiUO%2BTnv777%2BO%2BZ2JLW9OBA&X-Amz-Signature=431fe96e6db1b66e9e9161ea3414b752859ff5ab02282daa018f7325212bf69c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667ZK6P4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3kxAnjDfGuRACgYV92a0SJGgKzblfPduRgQzS689SfAiEAgFBHBaODZGCl%2FovQZKGXDovg6GK5u9Kn9e2LnByM5wQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEu7beJ%2FAXcVMadGyrcA1t0NspalrwZbqWGpYg%2BSo9wFqWQadfkrkzdgBNoR19kSK96tFUf7Ps02Y4mGes4qs0OyxpjMeLi9SQoReIWIA23aqx2jD4dDsH8o4c%2BXoapSN8u76eNiBJHvCg6H2p%2BiQr6KSNKkrGYRm5V%2BndiHPU9Zf8iydVKD%2BfWtFXeNiVRhPJyZvdGgs%2FpOqm8jRA4%2BVXQYwvX%2F0ANtmsEhbnrIM2mS6ZX3FOwI8zhprEV%2FXR%2BFiLY3fj00GWlbOSG4yLH8DcjbVKtXjmvaiZAjLuxfi1kszRdeFgCY1ncp%2B9mSxMeq%2FpQbYRpp7ueJWpizV72T9zBO%2FUzOSxokbR1hDrBFJEc%2Bfr7PWodCOVVlTI%2FIMwoq57T%2FMeX3O96vZwhxY0hdZZ0lmKlFyBUGFGnG%2BiUCQM%2FLqx2MmR%2FILcpDxoSfk52hyjLntII0j5uZVbqwqbvCpIp2Ewr%2FYcqBuXC%2FEu8Upucj4cyyJg8KYAXBdLAQZw1D9c4T9Hl%2FQrwsVq2uX%2Fby8Z7t%2FKPb1Px3VTVAEO5f2R1dkoZlV7jWpJd3SVbxqbM3e%2BWYrU3FLSVwHT4BPHxxJhMO4Umm2XMDVQ7yY0UKw7ClhHGdvm0WUL48M3sHmCYDgb%2BJKYsyuYXJqoCMJLJ%2BLwGOqUBxVc4GN7EUJmSzYzytmWogix6gugwj1W05cImSuP3ReZh4m50ZLzGeTLEYApEEhJbWToPR1shj%2Fa6Vs17nk6frXce%2FCTcj4iVWo9iG%2B3IEXRxovsjZl3dE%2Bzc1oH2LdWYxs9A1ybUs%2B7nS5GPvp313UstpHeQvnqI712V7gXqW%2FgYXwbpO9dqgZqaFyROBdUGWslTvCiUO%2BTnv777%2BO%2BZ2JLW9OBA&X-Amz-Signature=28831d016674a80874f33b0ef07216e983ef0b09e12c68dd797e0be0631b8d9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667ZK6P4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3kxAnjDfGuRACgYV92a0SJGgKzblfPduRgQzS689SfAiEAgFBHBaODZGCl%2FovQZKGXDovg6GK5u9Kn9e2LnByM5wQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEu7beJ%2FAXcVMadGyrcA1t0NspalrwZbqWGpYg%2BSo9wFqWQadfkrkzdgBNoR19kSK96tFUf7Ps02Y4mGes4qs0OyxpjMeLi9SQoReIWIA23aqx2jD4dDsH8o4c%2BXoapSN8u76eNiBJHvCg6H2p%2BiQr6KSNKkrGYRm5V%2BndiHPU9Zf8iydVKD%2BfWtFXeNiVRhPJyZvdGgs%2FpOqm8jRA4%2BVXQYwvX%2F0ANtmsEhbnrIM2mS6ZX3FOwI8zhprEV%2FXR%2BFiLY3fj00GWlbOSG4yLH8DcjbVKtXjmvaiZAjLuxfi1kszRdeFgCY1ncp%2B9mSxMeq%2FpQbYRpp7ueJWpizV72T9zBO%2FUzOSxokbR1hDrBFJEc%2Bfr7PWodCOVVlTI%2FIMwoq57T%2FMeX3O96vZwhxY0hdZZ0lmKlFyBUGFGnG%2BiUCQM%2FLqx2MmR%2FILcpDxoSfk52hyjLntII0j5uZVbqwqbvCpIp2Ewr%2FYcqBuXC%2FEu8Upucj4cyyJg8KYAXBdLAQZw1D9c4T9Hl%2FQrwsVq2uX%2Fby8Z7t%2FKPb1Px3VTVAEO5f2R1dkoZlV7jWpJd3SVbxqbM3e%2BWYrU3FLSVwHT4BPHxxJhMO4Umm2XMDVQ7yY0UKw7ClhHGdvm0WUL48M3sHmCYDgb%2BJKYsyuYXJqoCMJLJ%2BLwGOqUBxVc4GN7EUJmSzYzytmWogix6gugwj1W05cImSuP3ReZh4m50ZLzGeTLEYApEEhJbWToPR1shj%2Fa6Vs17nk6frXce%2FCTcj4iVWo9iG%2B3IEXRxovsjZl3dE%2Bzc1oH2LdWYxs9A1ybUs%2B7nS5GPvp313UstpHeQvnqI712V7gXqW%2FgYXwbpO9dqgZqaFyROBdUGWslTvCiUO%2BTnv777%2BO%2BZ2JLW9OBA&X-Amz-Signature=f3a3c65501fc9776dc522084bab91dc12bd049cffe8e5683526d4f6d6043d201&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXOQ7O2K%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpfNTIOESdBfEFEXfQmJUDmFde%2BWcG50nYpcIK9YynXAiBpaa0zCHxA7WLS2Uzs%2BvyywbYAJgRrak7krViW5BPAESqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBxN72rXQWMCrt43XKtwDx5%2BX2Q8xARnjnVj3N0zdPQbDm89cjl4mJI7SpnC4Kufcr1INoGO8HFZfCX9swOh4gwPXUJHHTL7HXgNEqMBbjDmoI5sqWzpvDtx5m4M2f4GlAD9V6i8m4h%2Fm7sYCUxe1BTOFVd5AxdYNfMAbTwIFqd8PZjao1Qgb6DPFqy%2Bhdk2l%2B3lybSv0srCB8jZMZcdQXI9wp6SODTQG3kXg%2BFUXnxbCXEJR9MPrFxU96gXvgygrzZVDzoqbPWGJGqDUc0uAKCplnf5UHmJ%2BNtMEcNj67J1aD8VFl2QTwfPOk8Ij0pR0HZjD3iA0nsAg16Xm2ire0TxbBV0EmRZA72GvHGIfkeAQd%2FyGz2IRZQTY36R6VlKnxOpdyO2RBNBx7YFcVYLowRxbQ6%2FTcowYN%2Bkx0%2Bt8cr1JQXp53KDSC%2BL2W8zYj%2FKjOKAnzAeI5XCH14uNl1Bup9Ezi0E5P6vHK8bYic7uz5xoUsYwNkfCOYTvwdsb0y0%2B4%2Fnszpy8lIf38MExMlN4OX0O1GEzrnSqkJmSF82Nf2BMh8n6YGRbsYj09fYi28iwlsUJFaFQOGoFbiB51CTyP94u0L2wuA2TNBNNBimTfQx50Gk%2ByVJakRSiSy4IfRLNkI1BeXXr3%2FGMqKsw9sD4vAY6pgHcEzopdDFbxA9UbKSGtvwUIyvYwgDSJThCiHwr%2BSh%2B5gM2yMwO%2F8T5L4vtOMn%2F%2BKYA3VG15TVLoyuOGsj5BcmtnwSmGJSQVkscpImnNiuCA45tHYH0h%2BJdxChwm%2BzlV9UKmBrc4XRBm8OfJzw1hSbY7q6DVMDdBJIg%2FaycSySSpM0S6qp797kSqRy4%2FLiSs2SPXPsrpjDe0rStqDwnJFPfE4%2FoAUMw&X-Amz-Signature=94ad9e0485f336b5f342dd9628a1a6322ab6213dc85d26ac25adcaf47262bbec&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYDQHBEV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZL8BPrSaAPmEwu6fn%2FYR58Cx%2BNLVyFHFUHcItbjsCoAiA17iDuKQeE6e20mSaxo8V7bK09%2B5OltPPuH5qVYttiSSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWRkdNe9XraaSV1R4KtwDydhhuRVZwXPQJaZtzhhIcTBR8R7yvm09pNJxJ6ZJieCwAe3YT6L5syYWAVzQx6DZisvB76qOdM9DeNQM2Se%2FwtY3iWUO%2FkzcpxnHqJ9s%2B6uo8lESCsk%2FSOWiHALgJvfERnKfrUDUxfycqCnfI%2B6laPFn2JI96mE1TJTXdJineh9g3uaxEdEI6HkCr4dTPs3nd5rDxqIDE3nI5iItgpFJ89TLWKo6oFnGotRuRF8BeQcRVosjgh0akOMVxy1rbbUZv6uQ0Ysep6mkSU07L2Jkt%2F3jbPc9peH4oSoS0GtHiRxXnkavUJrQRdA0ihAjm8HisI8EykoJ7LxdY1oAC4myyiBiX4xwdPiPDWJzb7EN5q4fowBimmcNSQATo9JK3NEG%2FAGEhuGW7ieaN2uUwDIp5YpMy5fqTuv%2FWg4JPwnqN1ECwfJ0JFWXfP5O8FkacWERLtpJfLm4UKXMORnMBXyeEVC%2FaDx94mBaN3PVr4nIn%2B1T9KyteHtU%2BO%2BGE4IpWsN93mNx6aOp6pyb7hEiGkyepOu7cf%2B3GvxYvtk8GLRQgoGVGcOWru3wX3znSVJ%2BdQPfkWW9arQleLCQqM63u1QI1qbFJr9axVp%2F%2FMUtTPl5p3scaPAEWeSK9pJ3qskwr8b4vAY6pgFy2ZtUlsVjKTVBMEOcX06jE117wW0hNTBaH%2BOEuLABfxftxWRp%2BLMnux2%2B%2B8GI3ox3olxpOrusnv8KauOFqwtAx9I%2B%2FPr88IKk3Gg0OHm%2B%2Fo91W%2BVIR47%2Bx5pxx78jnZlRx5C3EaGeCbVuIhxqxsI9GtMQe63NqJHJt66cog8rp2BhL3XkoPnJtWVbMasxy%2B0T43y7TgQaqZMK6h7AIe0KIptt3hKy&X-Amz-Signature=7b6f015f2b6457fcd12dd9e36314a27a7f7317479b55a4ea91734ebeb4e20d84&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26PDAH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGGg7T6k7OAoi%2BdnVIwO0ewMxoT6unwF6HR%2BP0kF6FIlAiBb1pXzSLBcluYBvFkfPBmioA2HgPUYaLFF6UF2WOiK1SqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPdzNMm1ExYg9%2BhXBKtwDr3IFwEk2QSccuZZd2ExlC%2Fn7SJs53DrNXAbE9gHngowIJ6%2BmIRdK0dQ1GhY9AsCaIHwO2VCst5NwhKbpW91%2Bh6SDjkG00O%2FO7s74te1xTEg73XhPr3a14O7HU%2FYwSBova1SGjf%2FeRH3l1hB4PeeitdfDTX7WTVxBpHSfNg37XXgp2uailVuGf3jAQ6vL%2F0EhJRt73UXe%2FcZErPcvsMMC86Q00U7eo6w7Zu%2FcOP83%2BEfmndJM0R0JD1YmzYzPXGEGU0Gk7fN%2BKeceMZiK%2BzgfCasSfwLfe94%2BgRGo7Ocs4M4FNj94HBp7d4bisbHaG3nz42Bufo0H6trZodBb9X5MlKJmMv3fG3xGqpJapj6LYorsFUDGglQWm5OktEO8MbdCYOOpWNnQulqJhsd5aUFFyhYTaqpD6YrTMS9g%2FrQmNUOfhN09Zg%2B%2Bcyi9BizsyCPZ3hKwXj9fgPSlaaHiAc8LQsdgZHFoVfHz47mNWMCe%2FH1dNfUtk%2Bys0X7qUJ8KgORn7SP3NQKaJ%2BMzbH9C5GXhJMGgtyHE7OehV1OqImm4BRZZndr8qKN8T2h8xTZZECNPFXlyAkI4bpulmEFTal0tizvz1EsTmEJlpA5yO8Z1ORleE0rbGORQcAChraYwhcP4vAY6pgFOO6K%2FBtjrQEUiAAXGzMbivj1vFrpnsUQz3fLY1HyAUJeyEudpXsJ1o7OnVFpPpC2FsB5iOYfBEMxZFbx0cFpqB%2BzuhvhpjbzQUrBAdYF4%2BVCWJ4iykpbkL80UXhyeDKtXeoqKL%2Fne6TIL17QzwjeejGk6s4NWVKB1cokq0hvirIwXoGSXLwlcFWVK54q7SHVLr6uD0LHnAfnimacPHtjZ%2FfoIzqcc&X-Amz-Signature=39486b695ff1f496260b820f2bac0ec5c0ce19beeb482bc7345d34cd7bef5981&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466657UFQUE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BCR3ZGX3mKFpTbrhOkSFJM6fntjz6lan40kPhcuh2nwIhAMDwZRMEWpogwSEVhQfcEAwZ0k2%2BVYNcdaKutdbcXe12KogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxT%2BOVXbRPw4lIO7Ksq3AMM3Gc47FDKkn8wNTPPTy%2FHu0664kG3LdxTCsY4pMMI3Ggm%2FXymLeketDgWPUemx8bp7ebTeP%2FzRuotF4vdw4zvmqa5cVnuIDMOzjudpNHiB1vZsrwNyNrQINDQfj1kD7cBQExH%2FH2tfs%2FcHhUgxcNDDTiTL0k9VZr73qXrJeiteAS2NFoJv1GOEbCZzuQ7JheG4DilB%2BAJDCH5kOD3qeitHED0TtklCLQk4eH%2FeEnq83h%2B9yeYkrGYt8eCozhteDXyigHvAut0TOXsQShfd5zsCVGq%2BvDUc5WvXim6ISvwyIPvv3NPWr1h0L%2FIQvnlMa2HAHgKajrzI1TSpzIygKbdjqX07pdnZ%2FA0BLCKJyLqvW4X4OFlj3enh53zUKv35dMVVF8VQdad4IVL9WjP6GPtAFAuBH777rYHXoEMyjbKcwQuMQ5rSXmRTo2HdhUQi96KiLLskoLHOaohQxJbeGO%2FzDLQHrKXl5gSPCpz0RqutBDJPsopSc0rfeqJdFzJGhiGQQYhT9E2Y%2BcsjeXimpYhpLU0TWuYha5PM62zr3FxL2%2Bm1H9%2Bzqmlpwpvw%2Fm9BzkKFC7pPFKpDSKT5OeIiQUqvNqR2mLr5xH1XJc929S2oTg8FCPCX9neL5D%2FGDDZx%2Fi8BjqkAZIHBMcsL0Uc8GrtncbqCXbjBOZlLnhSwbm%2FU3zGJrZqcNeVI5Zye7f4944AcKGaPy%2Fbt2pyp%2F6pXWu%2BjOfYU1%2BsMhZ49Kmy%2F14ELljDYVI%2BHfvsdT2BPf1HfMFb3UDEjQ7gb0o5AsFtsFIJgkpIYN7NmKs8xPOzry%2Bof0ED0g28%2BPg0bzL9dSslYBNWc0G01kA3pV8H9w9NOn3FnB0zZjegDjSB&X-Amz-Signature=230f557fb29b856d1dcfa255ff4418b89cf63f0dfa8c8d87520d3d303647b53d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466657UFQUE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BCR3ZGX3mKFpTbrhOkSFJM6fntjz6lan40kPhcuh2nwIhAMDwZRMEWpogwSEVhQfcEAwZ0k2%2BVYNcdaKutdbcXe12KogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxT%2BOVXbRPw4lIO7Ksq3AMM3Gc47FDKkn8wNTPPTy%2FHu0664kG3LdxTCsY4pMMI3Ggm%2FXymLeketDgWPUemx8bp7ebTeP%2FzRuotF4vdw4zvmqa5cVnuIDMOzjudpNHiB1vZsrwNyNrQINDQfj1kD7cBQExH%2FH2tfs%2FcHhUgxcNDDTiTL0k9VZr73qXrJeiteAS2NFoJv1GOEbCZzuQ7JheG4DilB%2BAJDCH5kOD3qeitHED0TtklCLQk4eH%2FeEnq83h%2B9yeYkrGYt8eCozhteDXyigHvAut0TOXsQShfd5zsCVGq%2BvDUc5WvXim6ISvwyIPvv3NPWr1h0L%2FIQvnlMa2HAHgKajrzI1TSpzIygKbdjqX07pdnZ%2FA0BLCKJyLqvW4X4OFlj3enh53zUKv35dMVVF8VQdad4IVL9WjP6GPtAFAuBH777rYHXoEMyjbKcwQuMQ5rSXmRTo2HdhUQi96KiLLskoLHOaohQxJbeGO%2FzDLQHrKXl5gSPCpz0RqutBDJPsopSc0rfeqJdFzJGhiGQQYhT9E2Y%2BcsjeXimpYhpLU0TWuYha5PM62zr3FxL2%2Bm1H9%2Bzqmlpwpvw%2Fm9BzkKFC7pPFKpDSKT5OeIiQUqvNqR2mLr5xH1XJc929S2oTg8FCPCX9neL5D%2FGDDZx%2Fi8BjqkAZIHBMcsL0Uc8GrtncbqCXbjBOZlLnhSwbm%2FU3zGJrZqcNeVI5Zye7f4944AcKGaPy%2Fbt2pyp%2F6pXWu%2BjOfYU1%2BsMhZ49Kmy%2F14ELljDYVI%2BHfvsdT2BPf1HfMFb3UDEjQ7gb0o5AsFtsFIJgkpIYN7NmKs8xPOzry%2Bof0ED0g28%2BPg0bzL9dSslYBNWc0G01kA3pV8H9w9NOn3FnB0zZjegDjSB&X-Amz-Signature=ea84e3d30b60a202f1c4a3261015e8213fd1a3cba6530662585c2669b413851c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
