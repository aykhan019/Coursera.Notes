

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDI7FLI3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvULpEs2y5PTV%2B%2BabiObr1uO1%2Beyt2v7zKoAgbZeYewQIhAJApY8eF48L75AszekYcl1Bgxcsdafq%2BJhojBpA1ontJKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCNIeEkOxY2H0ZATEq3AOYLaLWHGseTet0tGYgQL7yRFSx74nkUjzzimAh9jkNSRcMFf4fC9bCrM%2BQVC6wpDA0ETbGwA4wd6aLxF%2B9tsAdk630kxo8hyiRBJzYAsoBv5OoMxpv3dY78SB1XmIAnNj5JoQDTp5Z2JzSvhzhXkBLt3As3hB6y3vNjNwV8Bva%2FgBuEJAtd7SQNWq%2FfCv%2FdC31XM4PYdBKGCHPUmQ7F5mJx33viJfTDuPot2oXrNDLG%2B5yjZy5Eb%2BlWtAXAd7szgus5vuS37LjIZkp5qlGVh3%2FdKpCUumL1beHS6Z9e4tkLQqTdyj8I1UgER07VIo0isI2LnRnaoH4ClRSHUZsQLv3McLsWJD%2BmrChwsMUAXzYXITpUg5i6l2%2BFA8IEVWqhd1cgZL1YrnRszp%2BJUC7cmVQTbpQ5EfA4vKXou3cidCifbsonzSaYoIVx3AveUo11Z%2F%2FQAoi9Rv0vtE2CMA99YFq5L7BDLBY%2FfjdMGXMFfNa0ZgwLhkpafI0r7iWu4Gs3MDd8Rh9fcTlYdnIreoDDqOizlOU1YgmjOZbzLTCGE%2B23Xzb8Mj%2FMEvz0EIGL9rxPZez%2FXqI%2F5zOZfoa0ONdpKB63En84iGe%2FKzAZiNUgC7a6y2gVWHxyIDacZlS7TDnnvu8BjqkARKucsF8jHRO0FLCc7pZAOsyPL309INfecqJrb%2B05InJkIvr3YwO%2B%2FD1vaJ%2By72PvzxRmrMwqjHLyJhR0TJ%2BcOSRQCk%2BiqpYWA2WtxWlEb0g%2F7DKgwW%2BE8CCfWL%2BKBdhgDMML4ZrICpZCbPlSGGlLNmEbGwDsgOJaXRxKnfkCsvSFLRfiM8zraVpC2NmoexFzEkuaWn8cJeUODZmC2D%2By2lbtaPk&X-Amz-Signature=6626e3d43d63fdc16e2da6acec9f09f60859f10ba15c90de271b4c4217d0af7f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDI7FLI3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvULpEs2y5PTV%2B%2BabiObr1uO1%2Beyt2v7zKoAgbZeYewQIhAJApY8eF48L75AszekYcl1Bgxcsdafq%2BJhojBpA1ontJKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCNIeEkOxY2H0ZATEq3AOYLaLWHGseTet0tGYgQL7yRFSx74nkUjzzimAh9jkNSRcMFf4fC9bCrM%2BQVC6wpDA0ETbGwA4wd6aLxF%2B9tsAdk630kxo8hyiRBJzYAsoBv5OoMxpv3dY78SB1XmIAnNj5JoQDTp5Z2JzSvhzhXkBLt3As3hB6y3vNjNwV8Bva%2FgBuEJAtd7SQNWq%2FfCv%2FdC31XM4PYdBKGCHPUmQ7F5mJx33viJfTDuPot2oXrNDLG%2B5yjZy5Eb%2BlWtAXAd7szgus5vuS37LjIZkp5qlGVh3%2FdKpCUumL1beHS6Z9e4tkLQqTdyj8I1UgER07VIo0isI2LnRnaoH4ClRSHUZsQLv3McLsWJD%2BmrChwsMUAXzYXITpUg5i6l2%2BFA8IEVWqhd1cgZL1YrnRszp%2BJUC7cmVQTbpQ5EfA4vKXou3cidCifbsonzSaYoIVx3AveUo11Z%2F%2FQAoi9Rv0vtE2CMA99YFq5L7BDLBY%2FfjdMGXMFfNa0ZgwLhkpafI0r7iWu4Gs3MDd8Rh9fcTlYdnIreoDDqOizlOU1YgmjOZbzLTCGE%2B23Xzb8Mj%2FMEvz0EIGL9rxPZez%2FXqI%2F5zOZfoa0ONdpKB63En84iGe%2FKzAZiNUgC7a6y2gVWHxyIDacZlS7TDnnvu8BjqkARKucsF8jHRO0FLCc7pZAOsyPL309INfecqJrb%2B05InJkIvr3YwO%2B%2FD1vaJ%2By72PvzxRmrMwqjHLyJhR0TJ%2BcOSRQCk%2BiqpYWA2WtxWlEb0g%2F7DKgwW%2BE8CCfWL%2BKBdhgDMML4ZrICpZCbPlSGGlLNmEbGwDsgOJaXRxKnfkCsvSFLRfiM8zraVpC2NmoexFzEkuaWn8cJeUODZmC2D%2By2lbtaPk&X-Amz-Signature=3683afe4144e357b5db89f68ad41cc0704fa80ccff6d196f7de004e91dbe6ff6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDI7FLI3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvULpEs2y5PTV%2B%2BabiObr1uO1%2Beyt2v7zKoAgbZeYewQIhAJApY8eF48L75AszekYcl1Bgxcsdafq%2BJhojBpA1ontJKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCNIeEkOxY2H0ZATEq3AOYLaLWHGseTet0tGYgQL7yRFSx74nkUjzzimAh9jkNSRcMFf4fC9bCrM%2BQVC6wpDA0ETbGwA4wd6aLxF%2B9tsAdk630kxo8hyiRBJzYAsoBv5OoMxpv3dY78SB1XmIAnNj5JoQDTp5Z2JzSvhzhXkBLt3As3hB6y3vNjNwV8Bva%2FgBuEJAtd7SQNWq%2FfCv%2FdC31XM4PYdBKGCHPUmQ7F5mJx33viJfTDuPot2oXrNDLG%2B5yjZy5Eb%2BlWtAXAd7szgus5vuS37LjIZkp5qlGVh3%2FdKpCUumL1beHS6Z9e4tkLQqTdyj8I1UgER07VIo0isI2LnRnaoH4ClRSHUZsQLv3McLsWJD%2BmrChwsMUAXzYXITpUg5i6l2%2BFA8IEVWqhd1cgZL1YrnRszp%2BJUC7cmVQTbpQ5EfA4vKXou3cidCifbsonzSaYoIVx3AveUo11Z%2F%2FQAoi9Rv0vtE2CMA99YFq5L7BDLBY%2FfjdMGXMFfNa0ZgwLhkpafI0r7iWu4Gs3MDd8Rh9fcTlYdnIreoDDqOizlOU1YgmjOZbzLTCGE%2B23Xzb8Mj%2FMEvz0EIGL9rxPZez%2FXqI%2F5zOZfoa0ONdpKB63En84iGe%2FKzAZiNUgC7a6y2gVWHxyIDacZlS7TDnnvu8BjqkARKucsF8jHRO0FLCc7pZAOsyPL309INfecqJrb%2B05InJkIvr3YwO%2B%2FD1vaJ%2By72PvzxRmrMwqjHLyJhR0TJ%2BcOSRQCk%2BiqpYWA2WtxWlEb0g%2F7DKgwW%2BE8CCfWL%2BKBdhgDMML4ZrICpZCbPlSGGlLNmEbGwDsgOJaXRxKnfkCsvSFLRfiM8zraVpC2NmoexFzEkuaWn8cJeUODZmC2D%2By2lbtaPk&X-Amz-Signature=05d1a92056ba5dd7403350534f05cc8f9775da1b39d7a610c4342110ba797f90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MFFTB7S%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAXsfJrT5nB4oHj0QK75U7Sk4hWeG%2Fk3lEhHijZJItjQIgRCOQaps9jpBaObzcY7sOBbfDkVuVRVHGY9MwP%2B4xFT8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGM9NjeEoQt1HZTcjCrcA6bknEBTN0608XJ7sNGqSXMILcO0%2F6veiVJr3CW%2FsETQ4UpxEYP%2ByeduA0L8GhLJBuZSmqnofsOHwtbYrAIhHNdxM9hXvAHTP7qEgpPYcc5pHiIgiE%2FOAIK4j9cIjwHxpbAckXPZC18fxGjl07H%2F46fDiT5KjC6IUFGsOZvHRsr0LX0uOWLILdv1JgdKHq7XGxEvmKiN3FaPCQGwYdTolFyDeyRtMI3vFTva0pEnnCtUZmdtAifo%2F6XzfTSrV03RTF%2BU8nMHhzFhJoDD3oziI6xvc9KoYo%2F3Fpp5Y44WNsw5HkCXDut%2FdSxwfbmu7CQBDydcSRT76EiJtmzspfubGCuXe810N8az5t3E22OBQKA2ya%2FE5mNsWlti2uiieP%2BkVFWdsIxnVIrQkaAkxzYdR7%2Br1xG73GmczthZYoZTT4zcfVHDK1KKi6KYYIS2E8TBThPG%2FCDYFiRIUlEnsNpNoDOrA514Byz4WMybP8tc%2BrjGv4imOl9BIP%2FOR4BlbWoFkWCPpkD0reeP66lMkTrV%2B8t9iFsMLyp6mLUG78To1Xu%2Fstcbm6WF0JU5i%2BnlkSiuAocTqUtq%2BQKrM2mA%2BvHhnVG8gxESp2ugLlGsxAxANu57YPJmct2SXgFo5rpeMIef%2B7wGOqUB3%2FOp%2BUYoxR0NSyZ3Ts%2FMfVyagjUVsMtvieqCZn2ZeXZuIRRnR9Axyz3A1KG4T9eOsxZEOi6DJXCpnHRCihd6WfKWubSxNp7rGR%2FInGvWcedTnN49uZ7gDnJYuRl0Bvm96JffICglVJG4m4Op%2BoCm1c2OXHcHxrW2jeUj3J1dKmTsK1OLzkHeOSOqmGKMRTcDcuuqoHboRwB4kXKwVUu0oJmgyvnR&X-Amz-Signature=448a837a1e9f486cc887e391957d5b8875ab78dd0fe54c0927f21c0134dfe036&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MFFTB7S%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAXsfJrT5nB4oHj0QK75U7Sk4hWeG%2Fk3lEhHijZJItjQIgRCOQaps9jpBaObzcY7sOBbfDkVuVRVHGY9MwP%2B4xFT8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGM9NjeEoQt1HZTcjCrcA6bknEBTN0608XJ7sNGqSXMILcO0%2F6veiVJr3CW%2FsETQ4UpxEYP%2ByeduA0L8GhLJBuZSmqnofsOHwtbYrAIhHNdxM9hXvAHTP7qEgpPYcc5pHiIgiE%2FOAIK4j9cIjwHxpbAckXPZC18fxGjl07H%2F46fDiT5KjC6IUFGsOZvHRsr0LX0uOWLILdv1JgdKHq7XGxEvmKiN3FaPCQGwYdTolFyDeyRtMI3vFTva0pEnnCtUZmdtAifo%2F6XzfTSrV03RTF%2BU8nMHhzFhJoDD3oziI6xvc9KoYo%2F3Fpp5Y44WNsw5HkCXDut%2FdSxwfbmu7CQBDydcSRT76EiJtmzspfubGCuXe810N8az5t3E22OBQKA2ya%2FE5mNsWlti2uiieP%2BkVFWdsIxnVIrQkaAkxzYdR7%2Br1xG73GmczthZYoZTT4zcfVHDK1KKi6KYYIS2E8TBThPG%2FCDYFiRIUlEnsNpNoDOrA514Byz4WMybP8tc%2BrjGv4imOl9BIP%2FOR4BlbWoFkWCPpkD0reeP66lMkTrV%2B8t9iFsMLyp6mLUG78To1Xu%2Fstcbm6WF0JU5i%2BnlkSiuAocTqUtq%2BQKrM2mA%2BvHhnVG8gxESp2ugLlGsxAxANu57YPJmct2SXgFo5rpeMIef%2B7wGOqUB3%2FOp%2BUYoxR0NSyZ3Ts%2FMfVyagjUVsMtvieqCZn2ZeXZuIRRnR9Axyz3A1KG4T9eOsxZEOi6DJXCpnHRCihd6WfKWubSxNp7rGR%2FInGvWcedTnN49uZ7gDnJYuRl0Bvm96JffICglVJG4m4Op%2BoCm1c2OXHcHxrW2jeUj3J1dKmTsK1OLzkHeOSOqmGKMRTcDcuuqoHboRwB4kXKwVUu0oJmgyvnR&X-Amz-Signature=bcb83f39d279827b90642d3c24717f93f16d9388debf2a19f47cdb5ff1e9b901&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MFFTB7S%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAXsfJrT5nB4oHj0QK75U7Sk4hWeG%2Fk3lEhHijZJItjQIgRCOQaps9jpBaObzcY7sOBbfDkVuVRVHGY9MwP%2B4xFT8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGM9NjeEoQt1HZTcjCrcA6bknEBTN0608XJ7sNGqSXMILcO0%2F6veiVJr3CW%2FsETQ4UpxEYP%2ByeduA0L8GhLJBuZSmqnofsOHwtbYrAIhHNdxM9hXvAHTP7qEgpPYcc5pHiIgiE%2FOAIK4j9cIjwHxpbAckXPZC18fxGjl07H%2F46fDiT5KjC6IUFGsOZvHRsr0LX0uOWLILdv1JgdKHq7XGxEvmKiN3FaPCQGwYdTolFyDeyRtMI3vFTva0pEnnCtUZmdtAifo%2F6XzfTSrV03RTF%2BU8nMHhzFhJoDD3oziI6xvc9KoYo%2F3Fpp5Y44WNsw5HkCXDut%2FdSxwfbmu7CQBDydcSRT76EiJtmzspfubGCuXe810N8az5t3E22OBQKA2ya%2FE5mNsWlti2uiieP%2BkVFWdsIxnVIrQkaAkxzYdR7%2Br1xG73GmczthZYoZTT4zcfVHDK1KKi6KYYIS2E8TBThPG%2FCDYFiRIUlEnsNpNoDOrA514Byz4WMybP8tc%2BrjGv4imOl9BIP%2FOR4BlbWoFkWCPpkD0reeP66lMkTrV%2B8t9iFsMLyp6mLUG78To1Xu%2Fstcbm6WF0JU5i%2BnlkSiuAocTqUtq%2BQKrM2mA%2BvHhnVG8gxESp2ugLlGsxAxANu57YPJmct2SXgFo5rpeMIef%2B7wGOqUB3%2FOp%2BUYoxR0NSyZ3Ts%2FMfVyagjUVsMtvieqCZn2ZeXZuIRRnR9Axyz3A1KG4T9eOsxZEOi6DJXCpnHRCihd6WfKWubSxNp7rGR%2FInGvWcedTnN49uZ7gDnJYuRl0Bvm96JffICglVJG4m4Op%2BoCm1c2OXHcHxrW2jeUj3J1dKmTsK1OLzkHeOSOqmGKMRTcDcuuqoHboRwB4kXKwVUu0oJmgyvnR&X-Amz-Signature=10fd00da1f3f3c840a701d8c64fe0c3656cff992b3408c8e0e13aab715a6f159&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MFFTB7S%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAXsfJrT5nB4oHj0QK75U7Sk4hWeG%2Fk3lEhHijZJItjQIgRCOQaps9jpBaObzcY7sOBbfDkVuVRVHGY9MwP%2B4xFT8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGM9NjeEoQt1HZTcjCrcA6bknEBTN0608XJ7sNGqSXMILcO0%2F6veiVJr3CW%2FsETQ4UpxEYP%2ByeduA0L8GhLJBuZSmqnofsOHwtbYrAIhHNdxM9hXvAHTP7qEgpPYcc5pHiIgiE%2FOAIK4j9cIjwHxpbAckXPZC18fxGjl07H%2F46fDiT5KjC6IUFGsOZvHRsr0LX0uOWLILdv1JgdKHq7XGxEvmKiN3FaPCQGwYdTolFyDeyRtMI3vFTva0pEnnCtUZmdtAifo%2F6XzfTSrV03RTF%2BU8nMHhzFhJoDD3oziI6xvc9KoYo%2F3Fpp5Y44WNsw5HkCXDut%2FdSxwfbmu7CQBDydcSRT76EiJtmzspfubGCuXe810N8az5t3E22OBQKA2ya%2FE5mNsWlti2uiieP%2BkVFWdsIxnVIrQkaAkxzYdR7%2Br1xG73GmczthZYoZTT4zcfVHDK1KKi6KYYIS2E8TBThPG%2FCDYFiRIUlEnsNpNoDOrA514Byz4WMybP8tc%2BrjGv4imOl9BIP%2FOR4BlbWoFkWCPpkD0reeP66lMkTrV%2B8t9iFsMLyp6mLUG78To1Xu%2Fstcbm6WF0JU5i%2BnlkSiuAocTqUtq%2BQKrM2mA%2BvHhnVG8gxESp2ugLlGsxAxANu57YPJmct2SXgFo5rpeMIef%2B7wGOqUB3%2FOp%2BUYoxR0NSyZ3Ts%2FMfVyagjUVsMtvieqCZn2ZeXZuIRRnR9Axyz3A1KG4T9eOsxZEOi6DJXCpnHRCihd6WfKWubSxNp7rGR%2FInGvWcedTnN49uZ7gDnJYuRl0Bvm96JffICglVJG4m4Op%2BoCm1c2OXHcHxrW2jeUj3J1dKmTsK1OLzkHeOSOqmGKMRTcDcuuqoHboRwB4kXKwVUu0oJmgyvnR&X-Amz-Signature=46955b23e63415e48cd536d91db76467abc7e11614e8a69b482c3f376e30ffa9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MFFTB7S%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAXsfJrT5nB4oHj0QK75U7Sk4hWeG%2Fk3lEhHijZJItjQIgRCOQaps9jpBaObzcY7sOBbfDkVuVRVHGY9MwP%2B4xFT8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGM9NjeEoQt1HZTcjCrcA6bknEBTN0608XJ7sNGqSXMILcO0%2F6veiVJr3CW%2FsETQ4UpxEYP%2ByeduA0L8GhLJBuZSmqnofsOHwtbYrAIhHNdxM9hXvAHTP7qEgpPYcc5pHiIgiE%2FOAIK4j9cIjwHxpbAckXPZC18fxGjl07H%2F46fDiT5KjC6IUFGsOZvHRsr0LX0uOWLILdv1JgdKHq7XGxEvmKiN3FaPCQGwYdTolFyDeyRtMI3vFTva0pEnnCtUZmdtAifo%2F6XzfTSrV03RTF%2BU8nMHhzFhJoDD3oziI6xvc9KoYo%2F3Fpp5Y44WNsw5HkCXDut%2FdSxwfbmu7CQBDydcSRT76EiJtmzspfubGCuXe810N8az5t3E22OBQKA2ya%2FE5mNsWlti2uiieP%2BkVFWdsIxnVIrQkaAkxzYdR7%2Br1xG73GmczthZYoZTT4zcfVHDK1KKi6KYYIS2E8TBThPG%2FCDYFiRIUlEnsNpNoDOrA514Byz4WMybP8tc%2BrjGv4imOl9BIP%2FOR4BlbWoFkWCPpkD0reeP66lMkTrV%2B8t9iFsMLyp6mLUG78To1Xu%2Fstcbm6WF0JU5i%2BnlkSiuAocTqUtq%2BQKrM2mA%2BvHhnVG8gxESp2ugLlGsxAxANu57YPJmct2SXgFo5rpeMIef%2B7wGOqUB3%2FOp%2BUYoxR0NSyZ3Ts%2FMfVyagjUVsMtvieqCZn2ZeXZuIRRnR9Axyz3A1KG4T9eOsxZEOi6DJXCpnHRCihd6WfKWubSxNp7rGR%2FInGvWcedTnN49uZ7gDnJYuRl0Bvm96JffICglVJG4m4Op%2BoCm1c2OXHcHxrW2jeUj3J1dKmTsK1OLzkHeOSOqmGKMRTcDcuuqoHboRwB4kXKwVUu0oJmgyvnR&X-Amz-Signature=454f4e5ce78350d7e0c6924a9c96a3d9d5493291379a77595c38229bc5f4d06c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MFFTB7S%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAXsfJrT5nB4oHj0QK75U7Sk4hWeG%2Fk3lEhHijZJItjQIgRCOQaps9jpBaObzcY7sOBbfDkVuVRVHGY9MwP%2B4xFT8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGM9NjeEoQt1HZTcjCrcA6bknEBTN0608XJ7sNGqSXMILcO0%2F6veiVJr3CW%2FsETQ4UpxEYP%2ByeduA0L8GhLJBuZSmqnofsOHwtbYrAIhHNdxM9hXvAHTP7qEgpPYcc5pHiIgiE%2FOAIK4j9cIjwHxpbAckXPZC18fxGjl07H%2F46fDiT5KjC6IUFGsOZvHRsr0LX0uOWLILdv1JgdKHq7XGxEvmKiN3FaPCQGwYdTolFyDeyRtMI3vFTva0pEnnCtUZmdtAifo%2F6XzfTSrV03RTF%2BU8nMHhzFhJoDD3oziI6xvc9KoYo%2F3Fpp5Y44WNsw5HkCXDut%2FdSxwfbmu7CQBDydcSRT76EiJtmzspfubGCuXe810N8az5t3E22OBQKA2ya%2FE5mNsWlti2uiieP%2BkVFWdsIxnVIrQkaAkxzYdR7%2Br1xG73GmczthZYoZTT4zcfVHDK1KKi6KYYIS2E8TBThPG%2FCDYFiRIUlEnsNpNoDOrA514Byz4WMybP8tc%2BrjGv4imOl9BIP%2FOR4BlbWoFkWCPpkD0reeP66lMkTrV%2B8t9iFsMLyp6mLUG78To1Xu%2Fstcbm6WF0JU5i%2BnlkSiuAocTqUtq%2BQKrM2mA%2BvHhnVG8gxESp2ugLlGsxAxANu57YPJmct2SXgFo5rpeMIef%2B7wGOqUB3%2FOp%2BUYoxR0NSyZ3Ts%2FMfVyagjUVsMtvieqCZn2ZeXZuIRRnR9Axyz3A1KG4T9eOsxZEOi6DJXCpnHRCihd6WfKWubSxNp7rGR%2FInGvWcedTnN49uZ7gDnJYuRl0Bvm96JffICglVJG4m4Op%2BoCm1c2OXHcHxrW2jeUj3J1dKmTsK1OLzkHeOSOqmGKMRTcDcuuqoHboRwB4kXKwVUu0oJmgyvnR&X-Amz-Signature=5f01b187cdffb576368a921d420afd7ce306b5526fbd87d9484768bc24d1d856&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636FS4IK4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI6cT3ZGYVZKAlESze87aNpyOSxgr6FYuQDE2wt45zKgIhAMz12zabMbNo60484hufWVvBIf%2FR9i0WJm2XHibV82KiKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuPFeSqxFV0HygSWYq3AMreHxZWq9qKd6KXM1iRfBbc2a%2BjQPyO6cEYaQU6km7twiAs6xo3odkYE66tE5gI2NQJvaetk0dFUmOYEg1k%2BGLY9aOvJqEFoko0C7pLbNLgg14%2F5AanyhYZWfc%2FFQprjCNQjznLBtVYEjLC9JNVyofWFYCKbBjUjwC58NF9yeJnHBkHqmwCJeAKS0Rf47jIbZ%2FHD0DPuT2DpQ0MN3XBO0atFbhVs2HI3y5q57cqKMEX%2Fl8ekVn5ce0xAhxlowK8ZXe6P3eQ%2FI5pchPgtS%2FvgX%2FWm%2BvLXEfnaJT1o8RqmtJ5U5jF43dWhy0su%2BWbvKckihCCsr%2BNqE%2BxqBbNRdnyKOnR2SV0MtOpjcOnCz%2BnxOURxqRa54UXIn17TQLsHVE4K86T%2BVfLC14DCcxsCtpSNJLeYEIYuQ%2Fq3J%2FNkDtcgS23kMfQ32%2FxmezQKfork4qF%2BtmHl2K8WnCk3oRvOYjyEetGWo14uzCMFO6ke2uak4mTw5O2sSSz2rwoRjaGEx1o4BFatmPfpBr7fcCx5jf6At%2BFGxt6oHQpoMkEj9iWb%2FMqhMR3g5zxKLKxDwHgliYQQazLyHPx0TCYUi7fASQYzUBxAKReGiH0evoC6gZWH0TzPMM%2FxmnVV3j5SBQBDCQn%2Fu8BjqkATHnnXaUfNU0%2FbrQxrj3OF3Ec%2FMmEFpk9akjHS7W9pvW0%2BTeM4o9SiSFYaaoSmjNpkT6QdQ74rwuoKIVmPs6mBo9ihT5MwK6ahNRciidX8CL%2FOfH8MkJsQIb1wP2iPEX49YYI03LSjsCkukxJD3urWd2CBEEJqeVpSyXq%2F%2Bb2PY6bCe8EIzeyKCbQOGRMTzOXs3A%2FeDd3f%2BN%2FSoEWSOuJvtJwHyt&X-Amz-Signature=3eba0ad380400ffc5e042ed0c6f457bd9cd77173bff55c8d1db0bc175aa7b6a8&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HSGQP7H%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAjXtDXxN2DKU3ZcnqtevQy4sLqYXbiQYCc0Te8TQdP5AiBb7K7Tf3GLKda4qDFnJybVyieEKj9fi7z0GngrlQIg7SqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyQLs1VwSBW1DlRKqKtwD1dRGNthbta0WByayCAX%2BL13dbvFl1jC16SXtNLCI08G4TLJFpBSONvkQUkDpYWm4AyuXpjqnUVIWp8vaZiUlcvrMiktJ82IBmdJ3nGjZmQQIZjotmpiU%2FPLjTVEbyLA%2FCv8p%2B479xa5IAxDiGxSxXHhU6oiMW0r0r%2Fo%2BWDndPh99iJ0Dpwoex3NMIY7VBSCd2430ht%2Fu7Rp%2Bio%2BnZ6L3TVYoTY5NOfzwJaMfH7AHTHbGedaU6xod6bwTL5Gz5QYCP0IbPZ%2BVhqKrANY7FGZ9qG%2B44Pr%2F5t5T6%2BN3mL6hzuTl8XgcFo%2FD8%2FH%2BQ0%2Fd7vD3FVW7sm0qvgWGM4Uu%2Bz00jhRuBINAjalSkNIHLwPPGwc7WboWtZ49eMYNVEKgLwj9AUOYjc1B7SL%2BFeHNjM4bl%2Bq1i3LDH%2BGOCBhUvX79AFXn%2F6mpW%2BJT6A9mDtDGPL%2FESnyfYCyP8EpMczsMvy544Yns6OxxERAzQtbe2m3q7NNGYWUC%2FZiNuJrADnqIPAbV%2FBacwEsK%2FDRtOz9s0%2BkM0iPfyS2WzTGnaAxQ0tgTFtGRpmJAeS7h7H9yg9Reu5%2FMygzg9Mh95h37Oi5enwBQcD2mg%2BY5gooq7%2BymRy0ssJ%2BPXSpGVCpIyG6Goeow%2Fp77vAY6pgFT3vBNr5ueCBi18V7U2CWfi2YEK08JUi5F8QspZA6oqLqF5RnnScXMAxowdG8VfgL%2F8SYdQ4S0uIB0cAMrTYnqpp%2FQRCtbgPRUBG59uVioRg4EJcsEyUzbs0pJNqPmUCdapqf8v%2FkpFjF9OsqWnBoyuaUmlSZk4WKkUPnUE46BslC7d9c22MxKRH2NoeNKgFWE7dwsqkz4YiW%2Bqn3NUir5J0Obqnab&X-Amz-Signature=e0010fe4969df3e964d0626dd7aedaa15ae50efa0de3d0fb6ee8ebf0975fd56b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MFFTB7S%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAXsfJrT5nB4oHj0QK75U7Sk4hWeG%2Fk3lEhHijZJItjQIgRCOQaps9jpBaObzcY7sOBbfDkVuVRVHGY9MwP%2B4xFT8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGM9NjeEoQt1HZTcjCrcA6bknEBTN0608XJ7sNGqSXMILcO0%2F6veiVJr3CW%2FsETQ4UpxEYP%2ByeduA0L8GhLJBuZSmqnofsOHwtbYrAIhHNdxM9hXvAHTP7qEgpPYcc5pHiIgiE%2FOAIK4j9cIjwHxpbAckXPZC18fxGjl07H%2F46fDiT5KjC6IUFGsOZvHRsr0LX0uOWLILdv1JgdKHq7XGxEvmKiN3FaPCQGwYdTolFyDeyRtMI3vFTva0pEnnCtUZmdtAifo%2F6XzfTSrV03RTF%2BU8nMHhzFhJoDD3oziI6xvc9KoYo%2F3Fpp5Y44WNsw5HkCXDut%2FdSxwfbmu7CQBDydcSRT76EiJtmzspfubGCuXe810N8az5t3E22OBQKA2ya%2FE5mNsWlti2uiieP%2BkVFWdsIxnVIrQkaAkxzYdR7%2Br1xG73GmczthZYoZTT4zcfVHDK1KKi6KYYIS2E8TBThPG%2FCDYFiRIUlEnsNpNoDOrA514Byz4WMybP8tc%2BrjGv4imOl9BIP%2FOR4BlbWoFkWCPpkD0reeP66lMkTrV%2B8t9iFsMLyp6mLUG78To1Xu%2Fstcbm6WF0JU5i%2BnlkSiuAocTqUtq%2BQKrM2mA%2BvHhnVG8gxESp2ugLlGsxAxANu57YPJmct2SXgFo5rpeMIef%2B7wGOqUB3%2FOp%2BUYoxR0NSyZ3Ts%2FMfVyagjUVsMtvieqCZn2ZeXZuIRRnR9Axyz3A1KG4T9eOsxZEOi6DJXCpnHRCihd6WfKWubSxNp7rGR%2FInGvWcedTnN49uZ7gDnJYuRl0Bvm96JffICglVJG4m4Op%2BoCm1c2OXHcHxrW2jeUj3J1dKmTsK1OLzkHeOSOqmGKMRTcDcuuqoHboRwB4kXKwVUu0oJmgyvnR&X-Amz-Signature=ebccee8691e797dceb741aab418ce02d91bdbbed33c9b21187a27a588140f2e6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MFFTB7S%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAXsfJrT5nB4oHj0QK75U7Sk4hWeG%2Fk3lEhHijZJItjQIgRCOQaps9jpBaObzcY7sOBbfDkVuVRVHGY9MwP%2B4xFT8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGM9NjeEoQt1HZTcjCrcA6bknEBTN0608XJ7sNGqSXMILcO0%2F6veiVJr3CW%2FsETQ4UpxEYP%2ByeduA0L8GhLJBuZSmqnofsOHwtbYrAIhHNdxM9hXvAHTP7qEgpPYcc5pHiIgiE%2FOAIK4j9cIjwHxpbAckXPZC18fxGjl07H%2F46fDiT5KjC6IUFGsOZvHRsr0LX0uOWLILdv1JgdKHq7XGxEvmKiN3FaPCQGwYdTolFyDeyRtMI3vFTva0pEnnCtUZmdtAifo%2F6XzfTSrV03RTF%2BU8nMHhzFhJoDD3oziI6xvc9KoYo%2F3Fpp5Y44WNsw5HkCXDut%2FdSxwfbmu7CQBDydcSRT76EiJtmzspfubGCuXe810N8az5t3E22OBQKA2ya%2FE5mNsWlti2uiieP%2BkVFWdsIxnVIrQkaAkxzYdR7%2Br1xG73GmczthZYoZTT4zcfVHDK1KKi6KYYIS2E8TBThPG%2FCDYFiRIUlEnsNpNoDOrA514Byz4WMybP8tc%2BrjGv4imOl9BIP%2FOR4BlbWoFkWCPpkD0reeP66lMkTrV%2B8t9iFsMLyp6mLUG78To1Xu%2Fstcbm6WF0JU5i%2BnlkSiuAocTqUtq%2BQKrM2mA%2BvHhnVG8gxESp2ugLlGsxAxANu57YPJmct2SXgFo5rpeMIef%2B7wGOqUB3%2FOp%2BUYoxR0NSyZ3Ts%2FMfVyagjUVsMtvieqCZn2ZeXZuIRRnR9Axyz3A1KG4T9eOsxZEOi6DJXCpnHRCihd6WfKWubSxNp7rGR%2FInGvWcedTnN49uZ7gDnJYuRl0Bvm96JffICglVJG4m4Op%2BoCm1c2OXHcHxrW2jeUj3J1dKmTsK1OLzkHeOSOqmGKMRTcDcuuqoHboRwB4kXKwVUu0oJmgyvnR&X-Amz-Signature=6da8cbab996b07b270fd00e768f37f11cb931184bfde111d41f2b5f3328c10c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MFFTB7S%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAXsfJrT5nB4oHj0QK75U7Sk4hWeG%2Fk3lEhHijZJItjQIgRCOQaps9jpBaObzcY7sOBbfDkVuVRVHGY9MwP%2B4xFT8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGM9NjeEoQt1HZTcjCrcA6bknEBTN0608XJ7sNGqSXMILcO0%2F6veiVJr3CW%2FsETQ4UpxEYP%2ByeduA0L8GhLJBuZSmqnofsOHwtbYrAIhHNdxM9hXvAHTP7qEgpPYcc5pHiIgiE%2FOAIK4j9cIjwHxpbAckXPZC18fxGjl07H%2F46fDiT5KjC6IUFGsOZvHRsr0LX0uOWLILdv1JgdKHq7XGxEvmKiN3FaPCQGwYdTolFyDeyRtMI3vFTva0pEnnCtUZmdtAifo%2F6XzfTSrV03RTF%2BU8nMHhzFhJoDD3oziI6xvc9KoYo%2F3Fpp5Y44WNsw5HkCXDut%2FdSxwfbmu7CQBDydcSRT76EiJtmzspfubGCuXe810N8az5t3E22OBQKA2ya%2FE5mNsWlti2uiieP%2BkVFWdsIxnVIrQkaAkxzYdR7%2Br1xG73GmczthZYoZTT4zcfVHDK1KKi6KYYIS2E8TBThPG%2FCDYFiRIUlEnsNpNoDOrA514Byz4WMybP8tc%2BrjGv4imOl9BIP%2FOR4BlbWoFkWCPpkD0reeP66lMkTrV%2B8t9iFsMLyp6mLUG78To1Xu%2Fstcbm6WF0JU5i%2BnlkSiuAocTqUtq%2BQKrM2mA%2BvHhnVG8gxESp2ugLlGsxAxANu57YPJmct2SXgFo5rpeMIef%2B7wGOqUB3%2FOp%2BUYoxR0NSyZ3Ts%2FMfVyagjUVsMtvieqCZn2ZeXZuIRRnR9Axyz3A1KG4T9eOsxZEOi6DJXCpnHRCihd6WfKWubSxNp7rGR%2FInGvWcedTnN49uZ7gDnJYuRl0Bvm96JffICglVJG4m4Op%2BoCm1c2OXHcHxrW2jeUj3J1dKmTsK1OLzkHeOSOqmGKMRTcDcuuqoHboRwB4kXKwVUu0oJmgyvnR&X-Amz-Signature=aa3fa056c1cf94bf3de1f6d77a6ab28ef7088a47c3cb945921a6874a97800529&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCX6GJBA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCon6LqVP5lMQaU7FJf2QHAlXM6kQvkW0gJqewWx1LKSwIhAMF3C86kWzmLX4NX6C618J8SOvS3PlqBXqVlzHBSDKm5KogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySDmDMbR3GE%2B34GN0q3AMCTjc9C0iw2OdIGrp%2F69DwLLOzWHpQCuxBo5FF%2FApsJtXN00xNHTu1S8qiMl2MT7Ve8oOkEjn9FOGzKKquOLQkI5PIpkCYmvjkqkirYryWT6aCNPF4QQzBV18WCouJRj9N54iEJceb3%2B8GKEYarxx7fZQlfpHf5vHnT%2BdaZhg4UHjFxxLMyURGt05XHovbuWXgAagwyPalD6CXfKtBHKrOuh1A1yeByij2LnzrImg%2BMrrDDtTY%2BLzXg5D8%2BMti6mO5FUhEgkWuAgXZPyQdykFnV0qZP7Z8a8CKfJmVHb0h3iOvAGajwU77QhltazMCaDa1vQ4R58DLa73SiD8aJWXYY7ITSt%2BpSrXd8YbihU23D7dnhnLcvqAWKUh2r%2FO%2Fep%2BHtvFNqyzomJBtyjZGLK1k5KcwPUbKjfD%2BQh1VsQTNiDJ4r20QRiG0169dGhF6hHMackvzTbsiCjMTxI4Ac2en%2FPs%2FBAe0RCp2%2BlXN3T2b5%2FFJv60pJbsArb8moI%2B%2BsW5EUWHX7VrI9McjWnDOgjbNoNYHjN37RkWvzNuoiH8lW2OuyXPRwIc1WQVQA3bEnSUjMumVhpY2rgAiQkhEKJA07yovfIRtdfJq%2FrLlaAM6WpS%2FcuPyjSu5x5fOdDDdnvu8BjqkAX0BKQvGulhrYerqR5qagNbNQR7ecBF4Umbaelm9l9ppwhgUZRZmBF9delRc4%2F%2BYqqQ7SjZfnC%2B3SeMOB94Q2snwvAain%2FEkEw%2BY3hyQ8qvAPjJBJ4vwBc0vyJxGG%2BEIjSUZ9t3fvjw6MmlgS%2Bw%2B9rbR1emq0tNWI5Ler499FdVOlZyAqhBjn6MTbMkvEO09O0uA%2B5Zz5R7HMfwpQbU8Edc8i0no&X-Amz-Signature=3eab1ceebbe87d1318c73bfdd6fd778f1a4c810ae300e7149a012e960095b792&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG3WMQJ7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6qwezUllR5BFIs%2B5GU8rexOy%2F7CG2h4PU%2FXrdPfak%2BQIgHvMWlMjlfHT7aOyodeiYLZu3iyJgXGlYxVhS3xpCw8gqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAGKls3LzR6BN1k47ircA%2FvqDB9Z2qHJ9bo2D6ghakDFtMEfatxrL6teMQ3TQFoq2txWRugdUECuPOfv8mbN8H%2BYFKw2iyOIiwT8RJKSvCEadPgSiqp9IFHImzR7EhjYkvgMENoDsq04RLpvE7o9omGSjLNYlkye%2B2Of7uQcpsf9kRhoA5qhEhMP234CgRyz2kDusz0xhqUkvuzpr4ozvNa2J8yEcTtvLJFHL2Rs2yFpMiTBs3R3sPxE5HLVlKCPZKQRpZDx0mao5ifSmwGGfN66cmMQK9db5afVspjYtuFHfmtz9W7IrLwSU0Ubq8Hy%2FuyXbGWp6a%2F44b%2BCixNNLGWQuEuMlIvpaWWLFd27739xLechNpKB%2BHDz2NAYNGoAi9xXevH8hw5Gyf4mA78eVsBXf1YpaNS%2FsQP2qkenldmxOJ4DIQJQKlhlv5Z6MXxKW6UUnCoXAUddBjCUxREzLOIf8UE1sHpR5YUaKEqnWph809DJRP9gm1k3061NDjoK2MZKDw4pe1RqKWaVezKBZ5b7uevBNzB53mo30Er4KDANjAoUZO%2BGy7D7lzV0o85hSl8i2oXX3BI6%2FbkhbiHX2GlCKKve1OBhF6EMqYE2V8a4eaDYXQvG51yR8gY1tOWY9FSWdpzKWFeHgUm1MNue%2B7wGOqUBxo%2BvXDSIvzLbSamsLTx0Pb2JXPEbIoI%2BxiB9RDrVLugmURIjcxIyk%2FBveVm8kghhWThcC806wk6Ld0ovhL48YUChcHXy17tXdIwy9cQC47Y%2B4TIrkWcEo3nDZniSquTq45AO7CbatXkF6IaCEf%2BSvdkW4Qe5LNn0nr2SCnw%2BVRZCiidxHV6XCWP2NcDa8Q5HiF5BZ6hA9MfEXk2ZLwfzT%2FxJbJ5j&X-Amz-Signature=42ba764c2d7e26009fb080cb53319f6d8326439ee23fa1bec57e384ad7da590f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ2MQS7K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8FSyeb7grrVPVhoS36Kxogacw24%2FoEOMtnkRuL7R9WwIgOqx4sF2OExxW55%2FXJOOhbuCAGdvaTnn7lKyYXRD%2BzdoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8Yy%2FNd2RSNl3ftjCrcA84l7xm8veg2yZqWvEFyiiEZf8oKkbcrof1MA3ds8zYG1vTbNBwQo4Ol0BY8NAUWo1FcTHYSEubgzzJax4r867Xrpj1I7KVj8nQF8rbh8CGYHMzzhWkAioyCYwii%2BzkjyPOy2%2FXYfMhbUC0fUKHDq5pGvD%2BH1dWBDO7vBDX3NC9yuvC6F9WzFYvbvdHEWw%2BAcwTxqlIJGAzGZy4rURYZ7e3D75Cwu7WbrvYuh7%2B4tD6VwNTgNjH1IjAB974FodQo5pEHlrvEDqaZKAzMfbesl8yrNza4A3k5O2CAa0AcDwGxAeEGRvFSekBfXueWJ3VFumUp6SvMLXkDTQ%2FbV%2BbHoBpsogzrDEuXuSt2ydUubsXAekVfL80pSDgnNvqAYbADs4qqNngKSrUhP8RE1Sr%2FdfGE5CE4LOmMjl8fWhxoxcSP9%2BnI4oCH8fq9w1CBRqPDWnhRp2Sj4fgKfme0YDlJgdRWecMSVvBG8e4TeTMVQEdFfpUW8zd8xnZjwbkBSd6dU3bU6phMIdCEtGNtqBityLfAk9g7SlDBDeKqjljOvqAuZNuX6Pt6IGvYtx9XxiJJ0NlgMwGEjYHr1xpTA56dPlMRMxPLldLBhwfK%2Bu0CmmNlGjPYj%2BtfHOGMKA%2BqMLGf%2B7wGOqUBh7bJPiDB8fXYRrm%2FHibOdyeUJP1pAWZpLswnwCkXQJP6xA52fPId1w7TlmW7W1oIj8iy1hTK8wAIN3vxtr8Z6K86sK9dBiFOGZXiaB%2BKJSmCN1ulRUTEv3jF8nB2v5aVbXgPyKUvCzcox%2FptKU0C7i%2F9jH3DgU2xa1TEHXct9HMghO%2B5BRHSpBydgC7FxLuUz4eb2hM2t7zOvmbhhRhqVFvnoJfW&X-Amz-Signature=3e8980c55d42353cb78a36faecb1d1f9e2ace5242505c3388fed4ad55d72ce78&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UUVRALG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBHVlFGhCsZdmeF9bpcg%2F4O0ScIGfxCIZjEItn1OTmaOAiEAnOuUL8BkfTJHXtrlMbg8Eljh2EoFvNRCmrvhBjP3%2BlcqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMyom5Ay0C2rO6NYASrcA0426829YqVY3CG6r97dVA6u472SlWmmE9SHSV46T0fGDOKbmkZYurMcEpaprRN73PG7FPEUpvQ%2BDABO7YuJJjUsdf8%2F2aBm1wlF9aegCskXx1mOk4QFzmSMZtGNQsc3QzmrC9qx0EEQLOeDU1TEmwTlrMv%2BOLIfFZAgQmrCM58hqo%2FNNqT7L%2BPCVEK6S9y7o0JOlrMw1G5jNlCSGiwIsOI5CAnYNRwEQUPKgIMKO8d0%2B%2Fory4Hapf7rfOiejndts6LbITYh%2BsfEH8lQfEEi4USIr7n%2BoxNuc065GVkvSA4wvJiUQBjSjXovJztPJE2ug0ZxpY360bSb6thK%2FC0Ch45mJXEKy%2BoU4GkaUzsFYi%2F0%2BA0kp8FqhyhWZmHeiviF6nXou5N0fv4CVT3GjYScS2wWYa%2FnJbp7C2%2FcA85D7i1TjaZb3kAE2Tc4I6t%2Bl3vQRQCf6lv2j%2Ftxh4rBjQ50ix2oz5XLDAYk9PhV4lMZ2TH6T3aEckBL%2BWUqWDtUXAWtTh%2B68V77fuvmlzmKBHcu5%2Bfu43GHh1Fd8EwPx9V%2BDVCnxN3zunVGzEeEmlW3yma9niHoQvQn1lyVs%2Bd7jqfEdc6LAOOtDDeETEhT0agKqSUVvQ9vpJgsVavUc503MKqf%2B7wGOqUBcficBJ%2FPKkLXlOAsnZTvngXL3%2FgL1xzyaoIY1vrg6SO3MpzNGIFvry22MRtNwMGe87e8mAMnM8XbZ5Y24hV22NdiZQt7jH9tiBJ%2FsR8AJe3loYP9Y6DrMHrekC4MQRjBTy%2BviuVAxeftd2H9psXW5HojhH3GxZvK76v7JS6O7X6unF2zUEwIvtVwoL1OirC0kUuxQKst4nXjvgxkmuX%2BCwyWriRH&X-Amz-Signature=ed876f10d75d7d9083b56c167b48e670eab34e1399fb905ef4d486a0c9f085bd&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UUVRALG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBHVlFGhCsZdmeF9bpcg%2F4O0ScIGfxCIZjEItn1OTmaOAiEAnOuUL8BkfTJHXtrlMbg8Eljh2EoFvNRCmrvhBjP3%2BlcqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMyom5Ay0C2rO6NYASrcA0426829YqVY3CG6r97dVA6u472SlWmmE9SHSV46T0fGDOKbmkZYurMcEpaprRN73PG7FPEUpvQ%2BDABO7YuJJjUsdf8%2F2aBm1wlF9aegCskXx1mOk4QFzmSMZtGNQsc3QzmrC9qx0EEQLOeDU1TEmwTlrMv%2BOLIfFZAgQmrCM58hqo%2FNNqT7L%2BPCVEK6S9y7o0JOlrMw1G5jNlCSGiwIsOI5CAnYNRwEQUPKgIMKO8d0%2B%2Fory4Hapf7rfOiejndts6LbITYh%2BsfEH8lQfEEi4USIr7n%2BoxNuc065GVkvSA4wvJiUQBjSjXovJztPJE2ug0ZxpY360bSb6thK%2FC0Ch45mJXEKy%2BoU4GkaUzsFYi%2F0%2BA0kp8FqhyhWZmHeiviF6nXou5N0fv4CVT3GjYScS2wWYa%2FnJbp7C2%2FcA85D7i1TjaZb3kAE2Tc4I6t%2Bl3vQRQCf6lv2j%2Ftxh4rBjQ50ix2oz5XLDAYk9PhV4lMZ2TH6T3aEckBL%2BWUqWDtUXAWtTh%2B68V77fuvmlzmKBHcu5%2Bfu43GHh1Fd8EwPx9V%2BDVCnxN3zunVGzEeEmlW3yma9niHoQvQn1lyVs%2Bd7jqfEdc6LAOOtDDeETEhT0agKqSUVvQ9vpJgsVavUc503MKqf%2B7wGOqUBcficBJ%2FPKkLXlOAsnZTvngXL3%2FgL1xzyaoIY1vrg6SO3MpzNGIFvry22MRtNwMGe87e8mAMnM8XbZ5Y24hV22NdiZQt7jH9tiBJ%2FsR8AJe3loYP9Y6DrMHrekC4MQRjBTy%2BviuVAxeftd2H9psXW5HojhH3GxZvK76v7JS6O7X6unF2zUEwIvtVwoL1OirC0kUuxQKst4nXjvgxkmuX%2BCwyWriRH&X-Amz-Signature=07480425403444389daa893cc6f4cbf13eb1348ab07fc43278d0fec9da9a32ee&X-Amz-SignedHeaders=host&x-id=GetObject)

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
