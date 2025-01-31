

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OQQW7HX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn%2Fzcv5WZzBeNIwSTFqel1JtIrQQ34Tdp8xoztNJ%2FmtAIgc%2B9b1u0B1h1sqkJVfCcPgpra3foC14w39kQk1QascKcqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGLl46DdystHr9kI%2FircA6Yy5TToS2HlJYgVWCwtyxyj2BV7jZ68rKfNB2o6vAH5i6Yw0GwvtU5cofrXrbm3Aw4S7yonPXwoSWIpp4wkHOFrGRM49EtvPkLjdmQzvybrTCqoG1LaGOzLOYtMoNd9Ap5muOjMjmmIyP1eHK8lRC4wWX2BBnFXWF%2Bt9uXCFPsHro9YerrnJeFF43Dw7jtaXy%2BjurmLPeEZWWB%2FTfXn477rat32qUYyuWyUWc9Q82LRC%2BZz1kci7krv5O7Q4fIKwV6AjAPFIJjps7GIbVZ%2FcXZ9dy4qskhG6iDt2nbeyfNMCVHbp9iP%2BATcW1n6leKODLXqtXMvL3JTciXn2h6HKL6gudW2v6AwQg2fg5RfPk%2F3N0Gri%2Fxux0AfxARiRC%2BnnasKQGNNPl8G0RmcBR9vnv2%2BSP5pmPSeJfoK3pL5Ejlg%2Bbetmy2v4p1Xq6GO%2FEw%2BSD0d4eItTBJ7laQJtDmiNPK3T0ddeVnUhhbMw9jFGiO9hMd3EtUQYKZwMOZ4qkev53QinWUcbphXdgZfOWkm%2BnaDHSrkedQxnu2ZsWDPpHqsDVFnmpnqFd%2BxI75K8klW2YCLpOypK4%2Fw0RpNPDtDhqeOoN9oc1WQeZzLYkjOVZchxjnFDHUZ7PHIiwC4MO398bwGOqUBLicqs951TtTY%2F35PZQHt3QUTe4PW0MA9TiFhxJP1KV3GajciSifnpKfBG7CaOoivQsKXIfZC%2Fx5ypy7khgdSiLval%2Byzo4o4kUaGVPXpMfYGWPCNanofTDkNBCQV2632LGMLQgZYPVKAV9XQjHZQqYIoZfvYgypQNipODLswnP7%2BnlZj9BEH%2Bg%2BLi3wuBPPIiO04rbi8%2B562MwkCxCv5R0%2BCPXca&X-Amz-Signature=40817e33c3820b016851168694cb245e825e872d35a9d2574c6fc13862ad4648&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OQQW7HX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn%2Fzcv5WZzBeNIwSTFqel1JtIrQQ34Tdp8xoztNJ%2FmtAIgc%2B9b1u0B1h1sqkJVfCcPgpra3foC14w39kQk1QascKcqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGLl46DdystHr9kI%2FircA6Yy5TToS2HlJYgVWCwtyxyj2BV7jZ68rKfNB2o6vAH5i6Yw0GwvtU5cofrXrbm3Aw4S7yonPXwoSWIpp4wkHOFrGRM49EtvPkLjdmQzvybrTCqoG1LaGOzLOYtMoNd9Ap5muOjMjmmIyP1eHK8lRC4wWX2BBnFXWF%2Bt9uXCFPsHro9YerrnJeFF43Dw7jtaXy%2BjurmLPeEZWWB%2FTfXn477rat32qUYyuWyUWc9Q82LRC%2BZz1kci7krv5O7Q4fIKwV6AjAPFIJjps7GIbVZ%2FcXZ9dy4qskhG6iDt2nbeyfNMCVHbp9iP%2BATcW1n6leKODLXqtXMvL3JTciXn2h6HKL6gudW2v6AwQg2fg5RfPk%2F3N0Gri%2Fxux0AfxARiRC%2BnnasKQGNNPl8G0RmcBR9vnv2%2BSP5pmPSeJfoK3pL5Ejlg%2Bbetmy2v4p1Xq6GO%2FEw%2BSD0d4eItTBJ7laQJtDmiNPK3T0ddeVnUhhbMw9jFGiO9hMd3EtUQYKZwMOZ4qkev53QinWUcbphXdgZfOWkm%2BnaDHSrkedQxnu2ZsWDPpHqsDVFnmpnqFd%2BxI75K8klW2YCLpOypK4%2Fw0RpNPDtDhqeOoN9oc1WQeZzLYkjOVZchxjnFDHUZ7PHIiwC4MO398bwGOqUBLicqs951TtTY%2F35PZQHt3QUTe4PW0MA9TiFhxJP1KV3GajciSifnpKfBG7CaOoivQsKXIfZC%2Fx5ypy7khgdSiLval%2Byzo4o4kUaGVPXpMfYGWPCNanofTDkNBCQV2632LGMLQgZYPVKAV9XQjHZQqYIoZfvYgypQNipODLswnP7%2BnlZj9BEH%2Bg%2BLi3wuBPPIiO04rbi8%2B562MwkCxCv5R0%2BCPXca&X-Amz-Signature=a5c486c30a1e01a13d5c69b13d37025ae26ab707202a135d0b1386262fcd982c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OQQW7HX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn%2Fzcv5WZzBeNIwSTFqel1JtIrQQ34Tdp8xoztNJ%2FmtAIgc%2B9b1u0B1h1sqkJVfCcPgpra3foC14w39kQk1QascKcqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGLl46DdystHr9kI%2FircA6Yy5TToS2HlJYgVWCwtyxyj2BV7jZ68rKfNB2o6vAH5i6Yw0GwvtU5cofrXrbm3Aw4S7yonPXwoSWIpp4wkHOFrGRM49EtvPkLjdmQzvybrTCqoG1LaGOzLOYtMoNd9Ap5muOjMjmmIyP1eHK8lRC4wWX2BBnFXWF%2Bt9uXCFPsHro9YerrnJeFF43Dw7jtaXy%2BjurmLPeEZWWB%2FTfXn477rat32qUYyuWyUWc9Q82LRC%2BZz1kci7krv5O7Q4fIKwV6AjAPFIJjps7GIbVZ%2FcXZ9dy4qskhG6iDt2nbeyfNMCVHbp9iP%2BATcW1n6leKODLXqtXMvL3JTciXn2h6HKL6gudW2v6AwQg2fg5RfPk%2F3N0Gri%2Fxux0AfxARiRC%2BnnasKQGNNPl8G0RmcBR9vnv2%2BSP5pmPSeJfoK3pL5Ejlg%2Bbetmy2v4p1Xq6GO%2FEw%2BSD0d4eItTBJ7laQJtDmiNPK3T0ddeVnUhhbMw9jFGiO9hMd3EtUQYKZwMOZ4qkev53QinWUcbphXdgZfOWkm%2BnaDHSrkedQxnu2ZsWDPpHqsDVFnmpnqFd%2BxI75K8klW2YCLpOypK4%2Fw0RpNPDtDhqeOoN9oc1WQeZzLYkjOVZchxjnFDHUZ7PHIiwC4MO398bwGOqUBLicqs951TtTY%2F35PZQHt3QUTe4PW0MA9TiFhxJP1KV3GajciSifnpKfBG7CaOoivQsKXIfZC%2Fx5ypy7khgdSiLval%2Byzo4o4kUaGVPXpMfYGWPCNanofTDkNBCQV2632LGMLQgZYPVKAV9XQjHZQqYIoZfvYgypQNipODLswnP7%2BnlZj9BEH%2Bg%2BLi3wuBPPIiO04rbi8%2B562MwkCxCv5R0%2BCPXca&X-Amz-Signature=4a63793f07eabbaa541e6a6abb9460028366887583366093d6a17ddb98058a0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WQY6BDX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4rv5ZCAc1i%2Bt7lrDFwIYdDb1pAmbAEAGMmeYLP0CAAAIgF1HLRqFZ9OXL2Wua%2BZtE%2Fg7BIqxw3UbC96FwLb%2FXN2UqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7N%2Fi7t6ok17AzT8ircA50UkC%2FOylqyuwhSPc41AwlNPp4EsDjhU2aMUf9cr6kaUI99JRBb6%2Ff2DEMopZ8t81oQIJuRqFw1mBWnn0SLcdTfsM8SDKmVL4xdGi%2B5UpPga54niKNrW1K1u3%2BeiEhiYV4bgJMkZ65zX9vqY0vIWHVI0XQ170MwMXGcWQdS7KgQW7scKD6TW8H%2Fa9PnlE5SyXscTsQnSkuTz8XCNaTgAed%2FmBIrgGPKTkz%2B4K%2FKul%2BBUZwDxM5lbw6INZCrNKfpLyh9xZlKQvQ%2BhXvXpx8WpSkOQowxRx3vDL0%2BtpwJKP6meT9Cl8SDC29RgX65W5M6oQi8dCP54FjRmi8peSB9BJ8M2lfEzeMrTgcJHpl4dezoMIf5pq4Klp4kkj92DiAhZIoP0Jm2XkYl%2B%2B5QxYzmoxdSAHGAhiTIcaCMJvVvPNpvy5NEjAisvqQGegCPr2fiyhQS%2FKlWRrnOzTKp6EMFBiWLqyPu63lq%2FsDD3OErYb%2FaA71%2FM2WWSV1BAiqjcHLV9Lyxj3CRE7NsNNL%2BhuvhGk89lo6AdMjtqWWOC8v1g%2Bt%2BqOBVmC%2FwWedjrVyeT1m9zFr6BYdgB%2BT56z3PrRdUGWYgqLK0LWq11q3vlDgNIJNb48Gsvq1rsvrhrycuMNj98bwGOqUBYSNlMYYjhKDuV2FGOR%2BdXoGQE6akRViph69KqhPCTFhl6J37lSGoLGki%2FdMey7Fxr9NxVp59q4IlM0zOfWh594En8LKPx9SjX6SvJCKOxCFqDFXBasszZGQG0nN6GUYyCWcA0K%2Bf23JVHQQiTK0PLOxjHIgWlytft%2BedkdkbHh4Dj63o1PoFi9R5JYRB37wZHghd%2BlKQtmuw2mJWh4oX%2B6VQysl8&X-Amz-Signature=1a29ea8953b49302b32d75909431e49cb28c3fc73940a0fbad88390fc8961a5c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WQY6BDX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4rv5ZCAc1i%2Bt7lrDFwIYdDb1pAmbAEAGMmeYLP0CAAAIgF1HLRqFZ9OXL2Wua%2BZtE%2Fg7BIqxw3UbC96FwLb%2FXN2UqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7N%2Fi7t6ok17AzT8ircA50UkC%2FOylqyuwhSPc41AwlNPp4EsDjhU2aMUf9cr6kaUI99JRBb6%2Ff2DEMopZ8t81oQIJuRqFw1mBWnn0SLcdTfsM8SDKmVL4xdGi%2B5UpPga54niKNrW1K1u3%2BeiEhiYV4bgJMkZ65zX9vqY0vIWHVI0XQ170MwMXGcWQdS7KgQW7scKD6TW8H%2Fa9PnlE5SyXscTsQnSkuTz8XCNaTgAed%2FmBIrgGPKTkz%2B4K%2FKul%2BBUZwDxM5lbw6INZCrNKfpLyh9xZlKQvQ%2BhXvXpx8WpSkOQowxRx3vDL0%2BtpwJKP6meT9Cl8SDC29RgX65W5M6oQi8dCP54FjRmi8peSB9BJ8M2lfEzeMrTgcJHpl4dezoMIf5pq4Klp4kkj92DiAhZIoP0Jm2XkYl%2B%2B5QxYzmoxdSAHGAhiTIcaCMJvVvPNpvy5NEjAisvqQGegCPr2fiyhQS%2FKlWRrnOzTKp6EMFBiWLqyPu63lq%2FsDD3OErYb%2FaA71%2FM2WWSV1BAiqjcHLV9Lyxj3CRE7NsNNL%2BhuvhGk89lo6AdMjtqWWOC8v1g%2Bt%2BqOBVmC%2FwWedjrVyeT1m9zFr6BYdgB%2BT56z3PrRdUGWYgqLK0LWq11q3vlDgNIJNb48Gsvq1rsvrhrycuMNj98bwGOqUBYSNlMYYjhKDuV2FGOR%2BdXoGQE6akRViph69KqhPCTFhl6J37lSGoLGki%2FdMey7Fxr9NxVp59q4IlM0zOfWh594En8LKPx9SjX6SvJCKOxCFqDFXBasszZGQG0nN6GUYyCWcA0K%2Bf23JVHQQiTK0PLOxjHIgWlytft%2BedkdkbHh4Dj63o1PoFi9R5JYRB37wZHghd%2BlKQtmuw2mJWh4oX%2B6VQysl8&X-Amz-Signature=ea3144736e937f10c18dacd48774a5fb745730533a5128b4467910abf317f8e6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WQY6BDX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4rv5ZCAc1i%2Bt7lrDFwIYdDb1pAmbAEAGMmeYLP0CAAAIgF1HLRqFZ9OXL2Wua%2BZtE%2Fg7BIqxw3UbC96FwLb%2FXN2UqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7N%2Fi7t6ok17AzT8ircA50UkC%2FOylqyuwhSPc41AwlNPp4EsDjhU2aMUf9cr6kaUI99JRBb6%2Ff2DEMopZ8t81oQIJuRqFw1mBWnn0SLcdTfsM8SDKmVL4xdGi%2B5UpPga54niKNrW1K1u3%2BeiEhiYV4bgJMkZ65zX9vqY0vIWHVI0XQ170MwMXGcWQdS7KgQW7scKD6TW8H%2Fa9PnlE5SyXscTsQnSkuTz8XCNaTgAed%2FmBIrgGPKTkz%2B4K%2FKul%2BBUZwDxM5lbw6INZCrNKfpLyh9xZlKQvQ%2BhXvXpx8WpSkOQowxRx3vDL0%2BtpwJKP6meT9Cl8SDC29RgX65W5M6oQi8dCP54FjRmi8peSB9BJ8M2lfEzeMrTgcJHpl4dezoMIf5pq4Klp4kkj92DiAhZIoP0Jm2XkYl%2B%2B5QxYzmoxdSAHGAhiTIcaCMJvVvPNpvy5NEjAisvqQGegCPr2fiyhQS%2FKlWRrnOzTKp6EMFBiWLqyPu63lq%2FsDD3OErYb%2FaA71%2FM2WWSV1BAiqjcHLV9Lyxj3CRE7NsNNL%2BhuvhGk89lo6AdMjtqWWOC8v1g%2Bt%2BqOBVmC%2FwWedjrVyeT1m9zFr6BYdgB%2BT56z3PrRdUGWYgqLK0LWq11q3vlDgNIJNb48Gsvq1rsvrhrycuMNj98bwGOqUBYSNlMYYjhKDuV2FGOR%2BdXoGQE6akRViph69KqhPCTFhl6J37lSGoLGki%2FdMey7Fxr9NxVp59q4IlM0zOfWh594En8LKPx9SjX6SvJCKOxCFqDFXBasszZGQG0nN6GUYyCWcA0K%2Bf23JVHQQiTK0PLOxjHIgWlytft%2BedkdkbHh4Dj63o1PoFi9R5JYRB37wZHghd%2BlKQtmuw2mJWh4oX%2B6VQysl8&X-Amz-Signature=b86bd9fe9236cb8bf5b7bb2d4d025e92e0a8f78f5c3211eef4593ab56456a735&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WQY6BDX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4rv5ZCAc1i%2Bt7lrDFwIYdDb1pAmbAEAGMmeYLP0CAAAIgF1HLRqFZ9OXL2Wua%2BZtE%2Fg7BIqxw3UbC96FwLb%2FXN2UqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7N%2Fi7t6ok17AzT8ircA50UkC%2FOylqyuwhSPc41AwlNPp4EsDjhU2aMUf9cr6kaUI99JRBb6%2Ff2DEMopZ8t81oQIJuRqFw1mBWnn0SLcdTfsM8SDKmVL4xdGi%2B5UpPga54niKNrW1K1u3%2BeiEhiYV4bgJMkZ65zX9vqY0vIWHVI0XQ170MwMXGcWQdS7KgQW7scKD6TW8H%2Fa9PnlE5SyXscTsQnSkuTz8XCNaTgAed%2FmBIrgGPKTkz%2B4K%2FKul%2BBUZwDxM5lbw6INZCrNKfpLyh9xZlKQvQ%2BhXvXpx8WpSkOQowxRx3vDL0%2BtpwJKP6meT9Cl8SDC29RgX65W5M6oQi8dCP54FjRmi8peSB9BJ8M2lfEzeMrTgcJHpl4dezoMIf5pq4Klp4kkj92DiAhZIoP0Jm2XkYl%2B%2B5QxYzmoxdSAHGAhiTIcaCMJvVvPNpvy5NEjAisvqQGegCPr2fiyhQS%2FKlWRrnOzTKp6EMFBiWLqyPu63lq%2FsDD3OErYb%2FaA71%2FM2WWSV1BAiqjcHLV9Lyxj3CRE7NsNNL%2BhuvhGk89lo6AdMjtqWWOC8v1g%2Bt%2BqOBVmC%2FwWedjrVyeT1m9zFr6BYdgB%2BT56z3PrRdUGWYgqLK0LWq11q3vlDgNIJNb48Gsvq1rsvrhrycuMNj98bwGOqUBYSNlMYYjhKDuV2FGOR%2BdXoGQE6akRViph69KqhPCTFhl6J37lSGoLGki%2FdMey7Fxr9NxVp59q4IlM0zOfWh594En8LKPx9SjX6SvJCKOxCFqDFXBasszZGQG0nN6GUYyCWcA0K%2Bf23JVHQQiTK0PLOxjHIgWlytft%2BedkdkbHh4Dj63o1PoFi9R5JYRB37wZHghd%2BlKQtmuw2mJWh4oX%2B6VQysl8&X-Amz-Signature=28f77f36739ffb3cf4fc931b29d61e3d48563a0a15ed545a9297d2b528c6325a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WQY6BDX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4rv5ZCAc1i%2Bt7lrDFwIYdDb1pAmbAEAGMmeYLP0CAAAIgF1HLRqFZ9OXL2Wua%2BZtE%2Fg7BIqxw3UbC96FwLb%2FXN2UqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7N%2Fi7t6ok17AzT8ircA50UkC%2FOylqyuwhSPc41AwlNPp4EsDjhU2aMUf9cr6kaUI99JRBb6%2Ff2DEMopZ8t81oQIJuRqFw1mBWnn0SLcdTfsM8SDKmVL4xdGi%2B5UpPga54niKNrW1K1u3%2BeiEhiYV4bgJMkZ65zX9vqY0vIWHVI0XQ170MwMXGcWQdS7KgQW7scKD6TW8H%2Fa9PnlE5SyXscTsQnSkuTz8XCNaTgAed%2FmBIrgGPKTkz%2B4K%2FKul%2BBUZwDxM5lbw6INZCrNKfpLyh9xZlKQvQ%2BhXvXpx8WpSkOQowxRx3vDL0%2BtpwJKP6meT9Cl8SDC29RgX65W5M6oQi8dCP54FjRmi8peSB9BJ8M2lfEzeMrTgcJHpl4dezoMIf5pq4Klp4kkj92DiAhZIoP0Jm2XkYl%2B%2B5QxYzmoxdSAHGAhiTIcaCMJvVvPNpvy5NEjAisvqQGegCPr2fiyhQS%2FKlWRrnOzTKp6EMFBiWLqyPu63lq%2FsDD3OErYb%2FaA71%2FM2WWSV1BAiqjcHLV9Lyxj3CRE7NsNNL%2BhuvhGk89lo6AdMjtqWWOC8v1g%2Bt%2BqOBVmC%2FwWedjrVyeT1m9zFr6BYdgB%2BT56z3PrRdUGWYgqLK0LWq11q3vlDgNIJNb48Gsvq1rsvrhrycuMNj98bwGOqUBYSNlMYYjhKDuV2FGOR%2BdXoGQE6akRViph69KqhPCTFhl6J37lSGoLGki%2FdMey7Fxr9NxVp59q4IlM0zOfWh594En8LKPx9SjX6SvJCKOxCFqDFXBasszZGQG0nN6GUYyCWcA0K%2Bf23JVHQQiTK0PLOxjHIgWlytft%2BedkdkbHh4Dj63o1PoFi9R5JYRB37wZHghd%2BlKQtmuw2mJWh4oX%2B6VQysl8&X-Amz-Signature=cdc046c42d088a34f396b2d066177477879337aa68d0fc31173a2862cc3e1d9b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WQY6BDX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4rv5ZCAc1i%2Bt7lrDFwIYdDb1pAmbAEAGMmeYLP0CAAAIgF1HLRqFZ9OXL2Wua%2BZtE%2Fg7BIqxw3UbC96FwLb%2FXN2UqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7N%2Fi7t6ok17AzT8ircA50UkC%2FOylqyuwhSPc41AwlNPp4EsDjhU2aMUf9cr6kaUI99JRBb6%2Ff2DEMopZ8t81oQIJuRqFw1mBWnn0SLcdTfsM8SDKmVL4xdGi%2B5UpPga54niKNrW1K1u3%2BeiEhiYV4bgJMkZ65zX9vqY0vIWHVI0XQ170MwMXGcWQdS7KgQW7scKD6TW8H%2Fa9PnlE5SyXscTsQnSkuTz8XCNaTgAed%2FmBIrgGPKTkz%2B4K%2FKul%2BBUZwDxM5lbw6INZCrNKfpLyh9xZlKQvQ%2BhXvXpx8WpSkOQowxRx3vDL0%2BtpwJKP6meT9Cl8SDC29RgX65W5M6oQi8dCP54FjRmi8peSB9BJ8M2lfEzeMrTgcJHpl4dezoMIf5pq4Klp4kkj92DiAhZIoP0Jm2XkYl%2B%2B5QxYzmoxdSAHGAhiTIcaCMJvVvPNpvy5NEjAisvqQGegCPr2fiyhQS%2FKlWRrnOzTKp6EMFBiWLqyPu63lq%2FsDD3OErYb%2FaA71%2FM2WWSV1BAiqjcHLV9Lyxj3CRE7NsNNL%2BhuvhGk89lo6AdMjtqWWOC8v1g%2Bt%2BqOBVmC%2FwWedjrVyeT1m9zFr6BYdgB%2BT56z3PrRdUGWYgqLK0LWq11q3vlDgNIJNb48Gsvq1rsvrhrycuMNj98bwGOqUBYSNlMYYjhKDuV2FGOR%2BdXoGQE6akRViph69KqhPCTFhl6J37lSGoLGki%2FdMey7Fxr9NxVp59q4IlM0zOfWh594En8LKPx9SjX6SvJCKOxCFqDFXBasszZGQG0nN6GUYyCWcA0K%2Bf23JVHQQiTK0PLOxjHIgWlytft%2BedkdkbHh4Dj63o1PoFi9R5JYRB37wZHghd%2BlKQtmuw2mJWh4oX%2B6VQysl8&X-Amz-Signature=f7a66834e5c4d9d0cee4ff2963173dc248bc9eb1e9dd7fef71240a5e0a75d255&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVCVNFWE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHeGvCtgFd%2F1ShDaQU04JTLiQidTUB6mVvc6dJV1x52DAiEAkQWGg9Lfr0%2FZpP%2FARwWQymR0NlqdDk%2B8A8qaA81laD8qiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIfvVg87YqmiE6qTbircAyDR9j0ClW6ziBzaPlKl3nVlcwK7Edb%2FYI5tx88hew9lZzdnQoruquhXYzGDHFTMIBrKaKw%2Fh%2B3Z5fDWvqiixOOd6LtMthm%2B700hq5Dwbc5x2aeh4zbopNljHirrQjXgDpi%2BSNALZtpkQvXhVdv1Zu0NA4yY5Pp8cucres7idNWRnhumXSriyJduwrVZ%2ByjOgsk3nzho2WdVLvgp5TVYFo9I%2FxMGCMdhBcY%2B9w1%2B4rfl1oLKiP%2FtD%2FrKh3ElGACw1BrieBSz41WGFgo%2FciWr03Yi1UVN%2BzVGW0N7o6v5LzXzi42kmpp5IzwkMh5arYlT64MD2oiiU66ihlLMVoVDiB6AaxRa2m7oPCNNW1tVz5nwNyiJvuNNOe8Ue6Gk0uWOGbxOnw%2BSNDK%2F50NkG8Mcd8ei20C4nVMclkahJsGsgXr0mq%2BUAThCkCFmm7HGO0rlRT5803wVmT%2B48tw5Z9PbrtOqmXxbn6tTYAHxPLB8TpZuBHMp8nKlXVxZgMzK51uM5GiQ65GNwOViY%2BUMj30dpzVffEwhj%2BPueyuh1QD%2FpTau%2FC9Wq4w4jLhxzqOQHaI5ADC4ifMinOAuilA%2F%2FkqALjsBy8N%2F8xeNgOl0ZwRT5X26uF7rDVwCRQY6y0oFMM%2F98bwGOqUBSoRx5yec317aiPI%2BdtcavwDMM3SAh%2BRIozmW1X4IL3wNA%2Fs0tYWq26aGggf%2BboglDkUW5eB6bJqqhQ2k5cyn1EEvCudn8bjRSLfC9GI0t1RwrzimzkCglC580RstVikjesRSBsA52lxc7gZxPO%2B%2Bb2iaMaSIJpH5CdJWIR8AA1WsooZuXwEtKeMUAp3oJegiFpnA%2F%2BYCXIO1WPlsymH1ON6RprzG&X-Amz-Signature=bec3c30d2483c579c6bc848ed3cdc9cdfba2d1b97f5f604a1b952e6417ec8740&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XS3LNP7A%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAc2dEtR4%2BWVpt6b9oN%2BqHocQqiw82ttwFwdk46AVlypAiB%2Bz%2BL9yXxqu2xW8PWfXjRYS45EsHT0qVTsMKEjy0E%2F5iqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBVN%2BH8SvRg41RTYdKtwDSkKYLYMMJrJyXdy0m18laf70LjoWYzbyBGsXqf8R9RzJTo4una%2F0gc1LRKTxdyljxGlhIfBcSw5VA2oVAg4vHd6VHpuDGSU63xkpTtXfRmViB3hnOViraU2YurxWF7bvFCxtgghoZvziGiH5Jwwm1FH4FMJQwlPcuzp0zgbRx%2Bht5I4Lj1ZzfJ9JPVl2v0aNkSPjuUkqztrIz5kA65RA8cch8Q8tBUM7Rlr7aHcWC91Ov4k9dNYvyFpbDISjMvuMGgD59ookrJlVXGQj9%2FETBZdXCH5DaSOUpr%2FJ1ZGUxG12FUNYsffTdcrqrBytxdjUiz79E4%2BrsfJFunk2HQp0hHNwRNZVRbUptr6QCtwuzAukPNutm8wpjUYsq6yh3ASpPgjf2%2FNJ%2FrZcjTl7TDNHZ7QuR6GehaFAp04KX8SxDHJHikpHt4DCxvb%2FJNwSaBxAjZIr7d7mFeqOuHyof59BASV1776t4Bw3gGst1LEikkMvfPFESc9Z9E3Cw1yXv%2FVD6EfeI9%2B26QtqJ0K43ZcUiQON5PzJN1V%2BH6WYPp%2F%2FJ74tXcf7%2F136gYH%2BDNbouXL5OJuV0LDmKhpwnolMmi2GqirP151xEbqFHFMWUp2tdjhy2K0qp6x3u%2B%2Fq4cUwkP7xvAY6pgF9qIX8VVq7wqyORqdvCRhAaLVtUjfZauUtnryXzXV1x1XnHu%2FHLnguDa8hEAOq6mmUBQ4g7QUc6G%2BV0JmZh9ztQTNHIAGW9QxZQ036FLm0LhEl%2B4PjCGdzTI7jHu1IDZ9XKIhm3xLRJTT0Uau0LXgcw02adqVPtpOJo6%2FJHZjE1mylvBsDuLs9K%2BIvbEG6a7ic%2BGMee3hvoMdgL2mVSOfxOik4XnYq&X-Amz-Signature=40cccb79fc8093c87bdd2b084e75de3d339192c9cc07e482ac5d5d412f73bccb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WQY6BDX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4rv5ZCAc1i%2Bt7lrDFwIYdDb1pAmbAEAGMmeYLP0CAAAIgF1HLRqFZ9OXL2Wua%2BZtE%2Fg7BIqxw3UbC96FwLb%2FXN2UqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7N%2Fi7t6ok17AzT8ircA50UkC%2FOylqyuwhSPc41AwlNPp4EsDjhU2aMUf9cr6kaUI99JRBb6%2Ff2DEMopZ8t81oQIJuRqFw1mBWnn0SLcdTfsM8SDKmVL4xdGi%2B5UpPga54niKNrW1K1u3%2BeiEhiYV4bgJMkZ65zX9vqY0vIWHVI0XQ170MwMXGcWQdS7KgQW7scKD6TW8H%2Fa9PnlE5SyXscTsQnSkuTz8XCNaTgAed%2FmBIrgGPKTkz%2B4K%2FKul%2BBUZwDxM5lbw6INZCrNKfpLyh9xZlKQvQ%2BhXvXpx8WpSkOQowxRx3vDL0%2BtpwJKP6meT9Cl8SDC29RgX65W5M6oQi8dCP54FjRmi8peSB9BJ8M2lfEzeMrTgcJHpl4dezoMIf5pq4Klp4kkj92DiAhZIoP0Jm2XkYl%2B%2B5QxYzmoxdSAHGAhiTIcaCMJvVvPNpvy5NEjAisvqQGegCPr2fiyhQS%2FKlWRrnOzTKp6EMFBiWLqyPu63lq%2FsDD3OErYb%2FaA71%2FM2WWSV1BAiqjcHLV9Lyxj3CRE7NsNNL%2BhuvhGk89lo6AdMjtqWWOC8v1g%2Bt%2BqOBVmC%2FwWedjrVyeT1m9zFr6BYdgB%2BT56z3PrRdUGWYgqLK0LWq11q3vlDgNIJNb48Gsvq1rsvrhrycuMNj98bwGOqUBYSNlMYYjhKDuV2FGOR%2BdXoGQE6akRViph69KqhPCTFhl6J37lSGoLGki%2FdMey7Fxr9NxVp59q4IlM0zOfWh594En8LKPx9SjX6SvJCKOxCFqDFXBasszZGQG0nN6GUYyCWcA0K%2Bf23JVHQQiTK0PLOxjHIgWlytft%2BedkdkbHh4Dj63o1PoFi9R5JYRB37wZHghd%2BlKQtmuw2mJWh4oX%2B6VQysl8&X-Amz-Signature=98a15a141fba9ad9cd1968c174e43e7641331202269174804e3a14955c8acf72&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WQY6BDX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4rv5ZCAc1i%2Bt7lrDFwIYdDb1pAmbAEAGMmeYLP0CAAAIgF1HLRqFZ9OXL2Wua%2BZtE%2Fg7BIqxw3UbC96FwLb%2FXN2UqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7N%2Fi7t6ok17AzT8ircA50UkC%2FOylqyuwhSPc41AwlNPp4EsDjhU2aMUf9cr6kaUI99JRBb6%2Ff2DEMopZ8t81oQIJuRqFw1mBWnn0SLcdTfsM8SDKmVL4xdGi%2B5UpPga54niKNrW1K1u3%2BeiEhiYV4bgJMkZ65zX9vqY0vIWHVI0XQ170MwMXGcWQdS7KgQW7scKD6TW8H%2Fa9PnlE5SyXscTsQnSkuTz8XCNaTgAed%2FmBIrgGPKTkz%2B4K%2FKul%2BBUZwDxM5lbw6INZCrNKfpLyh9xZlKQvQ%2BhXvXpx8WpSkOQowxRx3vDL0%2BtpwJKP6meT9Cl8SDC29RgX65W5M6oQi8dCP54FjRmi8peSB9BJ8M2lfEzeMrTgcJHpl4dezoMIf5pq4Klp4kkj92DiAhZIoP0Jm2XkYl%2B%2B5QxYzmoxdSAHGAhiTIcaCMJvVvPNpvy5NEjAisvqQGegCPr2fiyhQS%2FKlWRrnOzTKp6EMFBiWLqyPu63lq%2FsDD3OErYb%2FaA71%2FM2WWSV1BAiqjcHLV9Lyxj3CRE7NsNNL%2BhuvhGk89lo6AdMjtqWWOC8v1g%2Bt%2BqOBVmC%2FwWedjrVyeT1m9zFr6BYdgB%2BT56z3PrRdUGWYgqLK0LWq11q3vlDgNIJNb48Gsvq1rsvrhrycuMNj98bwGOqUBYSNlMYYjhKDuV2FGOR%2BdXoGQE6akRViph69KqhPCTFhl6J37lSGoLGki%2FdMey7Fxr9NxVp59q4IlM0zOfWh594En8LKPx9SjX6SvJCKOxCFqDFXBasszZGQG0nN6GUYyCWcA0K%2Bf23JVHQQiTK0PLOxjHIgWlytft%2BedkdkbHh4Dj63o1PoFi9R5JYRB37wZHghd%2BlKQtmuw2mJWh4oX%2B6VQysl8&X-Amz-Signature=a47650abbe1ffeb9178c82523c36199ec60cb7876c7474620be431f08472c405&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WQY6BDX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4rv5ZCAc1i%2Bt7lrDFwIYdDb1pAmbAEAGMmeYLP0CAAAIgF1HLRqFZ9OXL2Wua%2BZtE%2Fg7BIqxw3UbC96FwLb%2FXN2UqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7N%2Fi7t6ok17AzT8ircA50UkC%2FOylqyuwhSPc41AwlNPp4EsDjhU2aMUf9cr6kaUI99JRBb6%2Ff2DEMopZ8t81oQIJuRqFw1mBWnn0SLcdTfsM8SDKmVL4xdGi%2B5UpPga54niKNrW1K1u3%2BeiEhiYV4bgJMkZ65zX9vqY0vIWHVI0XQ170MwMXGcWQdS7KgQW7scKD6TW8H%2Fa9PnlE5SyXscTsQnSkuTz8XCNaTgAed%2FmBIrgGPKTkz%2B4K%2FKul%2BBUZwDxM5lbw6INZCrNKfpLyh9xZlKQvQ%2BhXvXpx8WpSkOQowxRx3vDL0%2BtpwJKP6meT9Cl8SDC29RgX65W5M6oQi8dCP54FjRmi8peSB9BJ8M2lfEzeMrTgcJHpl4dezoMIf5pq4Klp4kkj92DiAhZIoP0Jm2XkYl%2B%2B5QxYzmoxdSAHGAhiTIcaCMJvVvPNpvy5NEjAisvqQGegCPr2fiyhQS%2FKlWRrnOzTKp6EMFBiWLqyPu63lq%2FsDD3OErYb%2FaA71%2FM2WWSV1BAiqjcHLV9Lyxj3CRE7NsNNL%2BhuvhGk89lo6AdMjtqWWOC8v1g%2Bt%2BqOBVmC%2FwWedjrVyeT1m9zFr6BYdgB%2BT56z3PrRdUGWYgqLK0LWq11q3vlDgNIJNb48Gsvq1rsvrhrycuMNj98bwGOqUBYSNlMYYjhKDuV2FGOR%2BdXoGQE6akRViph69KqhPCTFhl6J37lSGoLGki%2FdMey7Fxr9NxVp59q4IlM0zOfWh594En8LKPx9SjX6SvJCKOxCFqDFXBasszZGQG0nN6GUYyCWcA0K%2Bf23JVHQQiTK0PLOxjHIgWlytft%2BedkdkbHh4Dj63o1PoFi9R5JYRB37wZHghd%2BlKQtmuw2mJWh4oX%2B6VQysl8&X-Amz-Signature=490df518d1219054b82f75c28fe92a18225e28bc7b1938a72a94f3408aa26e1d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VJFGA3B%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCyV33%2FyMms9UuhyVedTHujbexaMwjvYo7Wugsr5ohEQIhALAY2BFV1ERZDqQIL54KnZ%2BEP8DuDhewbUcInorD6umlKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBpuPpTwBxoJIF1hgq3APj5Tjee4eRWn62Vbb%2BuF3bSk%2FJp97CYFO2BI0AqxxOsRd0tWWxV8V1U%2B84evEKqLwLm4uBBgUGjSDNSGMIAebqQqpxkGgt4x%2BiMXAJm6vxqM0Xw1GJu%2FiNWLoqPWIpgNMlXupc%2FYTv1qyD3k5OEyvpETBep1SAYXHGoHl7EGdXCbgaoah00DKmrrYHN7G2DdKsQAYFL4tRCBdKTqs4H4yaNovOw%2FSTJk9brANFZgn8GWJoKQEo%2Bvoaet64jv4RLqXH2IRXDro%2FAmsbCpxpjTlYpxMFL23vFUpPgtmU8LFT%2Bsz9O1Jr0vpVRLuIgL1qUraqnXbpA8RdFXLZmusBZIihnNv8f2lr9nolp6IF19hkVhKP4MfXNEB1uQt7jl7T1XFK449RoIRACK%2BGcDKzUekdpjGYG94Zj7IV7aos2NTq5XZUcM7wnhH5C29vasZy0KAM1OVCGRsY1TnYeTBSUqUg1xgPc18GXkZ%2F%2Fcf%2BBD6t0i%2FS0QRmxeju0bY1zNCLjXzd0dzQTwucM%2FokBkLWyq5o%2BsF%2FQv9xbBziqsUhTbQ1RltyDt%2BswByWVJEmwhOha2bi4rItCk7nJlgVNI5QkZK5wVH5hhJCyTm2laRMBlaRmuxwsbOnvCxZrrU2YjCH%2FvG8BjqkAUthMAp3Ku1Nb5yrJNbIrL0lmWAWzabfdaEDGlfXXIzu2kfAycBuZCyviXPR2ftcZQvc7TaIAT%2BmaTwhFfdgxpSM79fYdGoqLaaxvezEztempRIPbTOhab7trhPaXMUnylw8R7IJjw7y9tYJvhGBL87icTyaOmT3pvmur0Em3HtodN22xUOEj%2BRJymvndPyNPFeWuqi%2Fp50i51Xpcel1KU0gC18u&X-Amz-Signature=d7aecdeae71f989c893aac33a4aee17ed68c4de1a4fa856f8980dac6627033c6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXJYM237%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPgUpeQZZD%2BXRq6NkpgbGZaHg31vLmCHFbW6YrC56C0wIgccxMj0yXFzF2ie%2FH7ApscC%2BYjYqr1E%2BjwrUlYe93oW0qiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDAu42IiuLcTpRSQOyrcAz59BZlFdLILEqLWPAsPOIae64GiCUn5MOPfXZjUIuDWMSZOoHldeUf0lSe4NWhd99DbfM3mZgKr83wB76aBeu3o5MWtKB2TUn1fMbunlQknThlQGrLLK9kQ1oceEg%2B8q9gBv8Cw6ZQDUtIlGYPVVo82%2Fc3Mc%2BNOF35GfdI5DfkVZPq0ULieWwGjQQpJYOyj5%2FhBnt1cOXXHjP0MJMLBvPKrRPH6pwHyRfYMCNi6ExGgLYPHT93cXlnDp5XyIvE0H5sEiTvbYVDM%2BSb8XmOXk35GMaY1OTUjgejM08LX%2FU3E5MMr9A0s3%2FdTctDWKsktjZBn6ImhgRdAD2tvshwOY993guCioA56uF62oKLYX%2FFa7Cyeja3RNI0L0zO5tTVOwLQBg0x%2F2MtmXCsQNOfq2Ggv4ufNH3paqHjkP9bx1c2jN1oecCWal%2BdMBElZ0bwUiAJ2qtqa1O1XpXPKO8mV6fo7sG%2BBs%2BVu6bEM%2BqwCGoF1AIKt2j0kErgoZnKP1d4WElf1fjev57%2BaqB7lxF1KmuJL1CZ08QCM07l%2FaBjx0qPJc0%2B9xJM22pAIXWVJorSctROW6IAWvr6FCFAMyy0JlJgvVbrd0P1%2BZh7aVN8BQXQdSqkGmoQbs3bLvWcZMPT98bwGOqUBxitBGfuiPfgmi1hXTJ6T7EJ33RcsKhsVsJYUaKx8qvRTheEE8simhfYWhrfsQ%2F%2BTHIw6NeDRpxHoXUXD0avyQ2YFMrojQUnNsgagDrz9q0t0wnGh5aVH8%2BHY%2Fcl29aK0uO9qFn%2Folv7HnFoSZYuqDFu4FRBYeWvrJd4Kgsals1jrzgK%2BNP0wHoJn0Tx3C7gH8UrSRbp98r2u%2FOyyWpS9kOb%2BFdvd&X-Amz-Signature=71e050f52f1ed1649e9173d5947fefd0d1592be77e934cd0f7d75d25e476e646&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ANW2H3O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkFE%2FP41twU%2BjuH%2FfMqTosh46Pw9BYP%2BsphVcAiXHMrAIhAI8rJqGet5JfxPZ2gkG7MjTj%2FIc97nhVRE80nozPrAfdKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRDU9JfMoSW%2BSeYDAq3AOiZlaApuIfCgadKOcM47yBHFQMVUolPGOSomXjP7t5mUdfhMhPgXz2l9JI7CAr%2FsSOeL2pU0RuonF2WJ7%2Frqc0QUWStc73%2BFlEcNo3loUwli%2FBBgvn2M5yDoqtK04LxGwayev8%2FK6TIOdibRNfsUP3%2B2Cl7kc3w9%2BUz2eIbyC5lXmPvF2g%2BB7nY2%2BetE47r3LYjcAqhlK765Z%2BIUzBxv5ANQMG%2Bd7en5cH9Yv8paK7I6C6vRe3SiEfPrXAmtKxJQoGIenhQuFxU5HgnOnvGipQVMB240Wt9jmKZDJhdsESt9v%2Bk0Kz9EJLRQMkDWGKEExoyxVG4zG%2BBdIP53I4PhKqPRgD483OZNTSpeEJ8NkKTiwXZvl1sNd%2BDlRsOZf6XCTcqEBsQEBXqSmul%2FwUdR2NgPz4estSNtqtPrRyV3RdKpTOYfO4%2BLGHlT3hEa%2By5raHTzTG5tRKZ88U142aB56ffI1zGSBSIZJfe8PznDxAJq6Lci%2FelsffMXSj1%2BABA0whD9euwRgKVkj6bZHeScEKu02pBDZkejMxUQxjgFl4IUuGRi9PEI9y1reumh5fapZaq5pZwqE9uPU8Sv85QG3mylfc6d1P5MjhmwbYSRUdaf6pT8xEmjdUpfDntDD1%2FfG8BjqkASuDA%2FZZjqEFxZUyIbT1QKdAQSGsKHJiVVuSpPvJq4QIQCt61ZsdH%2FDBCjg5vEhnnf89UPZPYNnY9rENKqT1od06PqnUtA8dd3qqxHD6yW0mPjkdH9ZLJilJz0Th3k%2F%2Fw9VHBzeXpQSfgHwcIDOSCbr7zOJ5nfKZtiP7j8OKcL0CDqXCea4%2Fnf6jA8%2BdSHlm7FIxIAAArs20SK9vJWKh6zpqTdtz&X-Amz-Signature=4c22ca76caf1396fbea9506b2235dc697fe67577f73a25af6a73e466d3c72a58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Y2DK6RA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJQ%2F%2BjkzU%2FNIdpc1mh%2FOE3NHkDAki6GBtZ53foXRP3vQIgcNOSrd8noSaou9ue778U9DuvAuvumYNfHZvhrM6WSRQqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSFEur8Cd1ddYKELSrcA8QKbPRQfFXiKCl6WGOE3TJAtgluB6fjxlsmQQz23kpMAWMhjfAjpXyNLepgeQyzrs67C7ioMT712hzKWnW4pMvq7vDziuqYYTKrcAJDfwWDLkQtZuQMm5VdJztiyKp4Z%2FY%2BO8oI%2FEsA9oNppQS5Fsqxac8Bvlwj5ajftqZn8oCwX8BttVKyF8PQM%2F%2FE9xLY1116zOVdST7AbyXcRTqKONyTd0o%2FaqYm7EDpZIBCXvgyv7LeUSQTMLdTnqi1Ds20N7XqYvMgSgEcUFPOlJJ%2F6JpswNcrHpslW87yHMc7jJVSE9xNnIpcLAVs6z7RWPHUkWrRgeWrTl6AGixgeks3eoF70EsFpFUcZJBuvwL%2FU7HtLXVDlcNz6H3qtcQfpMruRIXWD3nKDbWdtzkG9KPXyddas0cupW%2BvULmnjhmUs7xZiacFKk4Ds80w8R8vhSSMaa79QPpyoRomu399LcXp6QS5vrqWjofMMN48hB%2BxBzqvA6yrFgyDgVv%2FKnJ9DkNRXeNn%2FUyaAhwwTN5iJP9MwYaw2F48wEOwomp7%2B8Yp%2BloHEJUx6LB5jirWRl1OixKVYdFJAOqvc2uHxEvONHWjwqCvpMHnEFuJ%2F6R1j4m8pZzaNKD4f3V1E7aH6RpMMPz98bwGOqUBL7ytBDh%2BrtAtPSDqw%2FSNJI27TE42aSh5PfvG7Bxe5x4NFgSBy%2B3Itcwv%2FZBW9aT4%2BA%2Bcw4CkFvf5Ssbdv%2BpddZGP9ZhzWSyfJyWCL%2F7uqAuZu%2BGCyylQ3qToSpGEU8TuJHhHyGXgeRHG%2FIqvMNVJ%2FuXHPXoVhfZ0DVM9ErnC1B%2FAIt9jodDF%2B7YpkmQK9uSosohhtFG5qpMF62t9Fe6o%2Fp7M4xGO&X-Amz-Signature=07b149f189b5140083bd20f4f3abd870acf12fa734ac1ac86bd065ce1ce21da8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Y2DK6RA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJQ%2F%2BjkzU%2FNIdpc1mh%2FOE3NHkDAki6GBtZ53foXRP3vQIgcNOSrd8noSaou9ue778U9DuvAuvumYNfHZvhrM6WSRQqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSFEur8Cd1ddYKELSrcA8QKbPRQfFXiKCl6WGOE3TJAtgluB6fjxlsmQQz23kpMAWMhjfAjpXyNLepgeQyzrs67C7ioMT712hzKWnW4pMvq7vDziuqYYTKrcAJDfwWDLkQtZuQMm5VdJztiyKp4Z%2FY%2BO8oI%2FEsA9oNppQS5Fsqxac8Bvlwj5ajftqZn8oCwX8BttVKyF8PQM%2F%2FE9xLY1116zOVdST7AbyXcRTqKONyTd0o%2FaqYm7EDpZIBCXvgyv7LeUSQTMLdTnqi1Ds20N7XqYvMgSgEcUFPOlJJ%2F6JpswNcrHpslW87yHMc7jJVSE9xNnIpcLAVs6z7RWPHUkWrRgeWrTl6AGixgeks3eoF70EsFpFUcZJBuvwL%2FU7HtLXVDlcNz6H3qtcQfpMruRIXWD3nKDbWdtzkG9KPXyddas0cupW%2BvULmnjhmUs7xZiacFKk4Ds80w8R8vhSSMaa79QPpyoRomu399LcXp6QS5vrqWjofMMN48hB%2BxBzqvA6yrFgyDgVv%2FKnJ9DkNRXeNn%2FUyaAhwwTN5iJP9MwYaw2F48wEOwomp7%2B8Yp%2BloHEJUx6LB5jirWRl1OixKVYdFJAOqvc2uHxEvONHWjwqCvpMHnEFuJ%2F6R1j4m8pZzaNKD4f3V1E7aH6RpMMPz98bwGOqUBL7ytBDh%2BrtAtPSDqw%2FSNJI27TE42aSh5PfvG7Bxe5x4NFgSBy%2B3Itcwv%2FZBW9aT4%2BA%2Bcw4CkFvf5Ssbdv%2BpddZGP9ZhzWSyfJyWCL%2F7uqAuZu%2BGCyylQ3qToSpGEU8TuJHhHyGXgeRHG%2FIqvMNVJ%2FuXHPXoVhfZ0DVM9ErnC1B%2FAIt9jodDF%2B7YpkmQK9uSosohhtFG5qpMF62t9Fe6o%2Fp7M4xGO&X-Amz-Signature=6139df135194055e9965dee643772b94803c62063f3c35f8b89ffde414c0f4ce&X-Amz-SignedHeaders=host&x-id=GetObject)

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
