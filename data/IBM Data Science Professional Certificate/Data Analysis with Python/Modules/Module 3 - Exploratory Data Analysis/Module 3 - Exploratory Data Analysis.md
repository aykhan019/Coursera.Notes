

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TQZ2CVH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIGPIT%2BnLlhlj97xmwNEesgry%2FX8TgUEDIpOdYT4ZutYnAiEA4TpYy1cUqBq82AdKsHkZdQvZ6Lps6Whrb9gexmk4ufQq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOhy5XG7nYv5Gna%2B5CrcAw7xGJ2q%2BOV1hRvwyHV65bkm%2BlB5pPjAsylbEYjK1FoLuqwu2u1PXtwAtiRrR0HtLCMKxrOGpp6abtZNCFj0mZCCBDPgSmpv9cP3o3yuJB4AhsWn12RBUpiOS9eJhqUdJo%2Flv8L%2FwyIEn2ON%2BQe5YGljJWEeniNjbrvdQ%2ByM9uK0McA%2F3rnMk%2Fs8jPYZ8MwD6rvnK6peqCSREvDY%2BBUdQjbDiUtlp0AuhnQIC4x2AGt63L5MYBwcU7wtYN0j8LMBBQK0Bjy%2BWWMScH9PIeifatFEGpbWVlPei7uYZZssqj%2FKWb3A6Ao%2FoLOnV6ps2XZX7ZrjoIYfXLJaYN2u7IG9fNACd1KSgOql0ZucG3PuMvztXsHUV3FE2M1V4cC64DgN07iLovTbw5Fh572sCkTdKuK92IyOiCOI6hh17H0t%2BChiydnPuoqUzRPjxO5syarmGYA%2BSaIFcsqBtNCEaGoBApOP0ZUOg%2BbhE3KXNjWavK20UxStKDAqjtkKy9JpWfhrcDV%2F02qV%2BPHoAkxZuLti7DUT1yMKleztaI5kjPNVapn11NrnO2nz4%2B6piQl%2FO6%2Bppz2SEUEaF16Shpy4RQ4MG41zjraCS6UQXJuYl7kLDreTORI8hl89s07Yij9rMJH%2Bmb0GOqUBqnglZtavUtxaa5eqNJ%2FgvQUDzhj4rr953l0Tt2VnlxHHsJCtYEQaMn5BrFRmqp3b8V%2F6RUhsj6Y%2BRsj9pnH9AaYmaOH6%2F2UNucWoYaDABwwiybcW3oRFKuR8GU4hsTZ8ZmDmRoEag%2Bnq1VxXLRC62UVYL2fhXyAD1g4QtPIDGZTCK%2F5nf1srn8zyCYuO908UynmwAeUeX%2BS4pTHGQa9NrXtN%2BuHs&X-Amz-Signature=c502df1fec1c77930920dc2131df992cd53d0ed683079f8c77275f6f6cd6d393&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TQZ2CVH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIGPIT%2BnLlhlj97xmwNEesgry%2FX8TgUEDIpOdYT4ZutYnAiEA4TpYy1cUqBq82AdKsHkZdQvZ6Lps6Whrb9gexmk4ufQq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOhy5XG7nYv5Gna%2B5CrcAw7xGJ2q%2BOV1hRvwyHV65bkm%2BlB5pPjAsylbEYjK1FoLuqwu2u1PXtwAtiRrR0HtLCMKxrOGpp6abtZNCFj0mZCCBDPgSmpv9cP3o3yuJB4AhsWn12RBUpiOS9eJhqUdJo%2Flv8L%2FwyIEn2ON%2BQe5YGljJWEeniNjbrvdQ%2ByM9uK0McA%2F3rnMk%2Fs8jPYZ8MwD6rvnK6peqCSREvDY%2BBUdQjbDiUtlp0AuhnQIC4x2AGt63L5MYBwcU7wtYN0j8LMBBQK0Bjy%2BWWMScH9PIeifatFEGpbWVlPei7uYZZssqj%2FKWb3A6Ao%2FoLOnV6ps2XZX7ZrjoIYfXLJaYN2u7IG9fNACd1KSgOql0ZucG3PuMvztXsHUV3FE2M1V4cC64DgN07iLovTbw5Fh572sCkTdKuK92IyOiCOI6hh17H0t%2BChiydnPuoqUzRPjxO5syarmGYA%2BSaIFcsqBtNCEaGoBApOP0ZUOg%2BbhE3KXNjWavK20UxStKDAqjtkKy9JpWfhrcDV%2F02qV%2BPHoAkxZuLti7DUT1yMKleztaI5kjPNVapn11NrnO2nz4%2B6piQl%2FO6%2Bppz2SEUEaF16Shpy4RQ4MG41zjraCS6UQXJuYl7kLDreTORI8hl89s07Yij9rMJH%2Bmb0GOqUBqnglZtavUtxaa5eqNJ%2FgvQUDzhj4rr953l0Tt2VnlxHHsJCtYEQaMn5BrFRmqp3b8V%2F6RUhsj6Y%2BRsj9pnH9AaYmaOH6%2F2UNucWoYaDABwwiybcW3oRFKuR8GU4hsTZ8ZmDmRoEag%2Bnq1VxXLRC62UVYL2fhXyAD1g4QtPIDGZTCK%2F5nf1srn8zyCYuO908UynmwAeUeX%2BS4pTHGQa9NrXtN%2BuHs&X-Amz-Signature=978a9ffefadc35c43c9c6cd31b10863fe6276b5533766d1592a0b66ca8d49bf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TQZ2CVH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIGPIT%2BnLlhlj97xmwNEesgry%2FX8TgUEDIpOdYT4ZutYnAiEA4TpYy1cUqBq82AdKsHkZdQvZ6Lps6Whrb9gexmk4ufQq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOhy5XG7nYv5Gna%2B5CrcAw7xGJ2q%2BOV1hRvwyHV65bkm%2BlB5pPjAsylbEYjK1FoLuqwu2u1PXtwAtiRrR0HtLCMKxrOGpp6abtZNCFj0mZCCBDPgSmpv9cP3o3yuJB4AhsWn12RBUpiOS9eJhqUdJo%2Flv8L%2FwyIEn2ON%2BQe5YGljJWEeniNjbrvdQ%2ByM9uK0McA%2F3rnMk%2Fs8jPYZ8MwD6rvnK6peqCSREvDY%2BBUdQjbDiUtlp0AuhnQIC4x2AGt63L5MYBwcU7wtYN0j8LMBBQK0Bjy%2BWWMScH9PIeifatFEGpbWVlPei7uYZZssqj%2FKWb3A6Ao%2FoLOnV6ps2XZX7ZrjoIYfXLJaYN2u7IG9fNACd1KSgOql0ZucG3PuMvztXsHUV3FE2M1V4cC64DgN07iLovTbw5Fh572sCkTdKuK92IyOiCOI6hh17H0t%2BChiydnPuoqUzRPjxO5syarmGYA%2BSaIFcsqBtNCEaGoBApOP0ZUOg%2BbhE3KXNjWavK20UxStKDAqjtkKy9JpWfhrcDV%2F02qV%2BPHoAkxZuLti7DUT1yMKleztaI5kjPNVapn11NrnO2nz4%2B6piQl%2FO6%2Bppz2SEUEaF16Shpy4RQ4MG41zjraCS6UQXJuYl7kLDreTORI8hl89s07Yij9rMJH%2Bmb0GOqUBqnglZtavUtxaa5eqNJ%2FgvQUDzhj4rr953l0Tt2VnlxHHsJCtYEQaMn5BrFRmqp3b8V%2F6RUhsj6Y%2BRsj9pnH9AaYmaOH6%2F2UNucWoYaDABwwiybcW3oRFKuR8GU4hsTZ8ZmDmRoEag%2Bnq1VxXLRC62UVYL2fhXyAD1g4QtPIDGZTCK%2F5nf1srn8zyCYuO908UynmwAeUeX%2BS4pTHGQa9NrXtN%2BuHs&X-Amz-Signature=778d4de36a9708655247c9b31add08c8eb5d4dc20a4daa5a242b6b9c4a1abe1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TEYNLIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCqafut5rDdN9Dgzfm7S7%2Fxy0FX5vBBsLgJDQpdKRd6AwIgdGw0JGpVAIdwgYId0URUxcJ6cAJgszj%2BMsjrXSTaeGkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDgmofn5J%2BIW7cgQyyrcA1z3legq3K00sKXO0T%2FMpvxdOSIFF1bpoRP3vm8IkuM4ojHm6B2ELYOl9xDZPasJgaBvOaWdSHW1qBoFnSaSIh3oVQvA1zkztUJxdKPTygQM4sbo65%2ByfmlIzXJ4NLSb%2FV1sFXz7fxhwe70iZBvp%2BYvqFxpdFJ83rmJlAtCFtw1%2FFoOxHHj7lUud%2B32XOSgPCg0hSlbjOCmHbETEKh8XNcSZUkjkhMIvYd5a8fJ3Mhf8r4nDGQOLC%2FDxOB5ZaFgAc6vybg9Q48EqhChQMC%2FIbBWmh6mw5A5m7Q2vA9zj6zwWPT3lrG2UrC2o3J2Oy4QclHdbD4qZdA6gZVCeIrfmTQOEvR96HMW0owMBcnbeJUCK0iDaa%2B6XrhdsJ6Du1%2FYEO0NNCJ6Bkg3SVdADO6CcMfNFanACPic0mw9EPAlvuHF9eJMaop9lTq9vXgBMCiyvov5RnA5ahoHFyTVUFqv62Ctm6Mes1g3hVoOs8dHTLgQMzNr2o0W%2FNeBJ1LfNEoqn5WG8B6NUal6A6jS7ep7vnNW0KzBBKzJ9vKpFtZVxUmIFxyxyjk3t6bg5xCDVf5ptjoJcfbarODOI79dUXVjClfWsuAJ5TpGbm%2BUXTSlK4wjO1LfJPWc9aKvB0Vp%2BML7%2Bmb0GOqUBm%2FhepWcVfrwF3n8dyGfNSBXRLk85Ds4yY5xhbRnFODyvLvrkvryffJ9uS3qb2tAILQYqTxU2VfIBbimd0okbw8WMB9PrF2O%2FLZqs7XqGbXex84JrFLLhNFPQeKwzrA9zxVvl9sCA24kOwcpGMgI0VZrSn9WMaIX6ch5JZg95rhLaYcVaED4P%2BYIc8ZgPPW0sfGyEzTUDZRg3RlwZ0NFD6vA9Yya3&X-Amz-Signature=a368e5dc87d8155863102f78824de1619941da19f42ddf097fcb004ac6954743&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TEYNLIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCqafut5rDdN9Dgzfm7S7%2Fxy0FX5vBBsLgJDQpdKRd6AwIgdGw0JGpVAIdwgYId0URUxcJ6cAJgszj%2BMsjrXSTaeGkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDgmofn5J%2BIW7cgQyyrcA1z3legq3K00sKXO0T%2FMpvxdOSIFF1bpoRP3vm8IkuM4ojHm6B2ELYOl9xDZPasJgaBvOaWdSHW1qBoFnSaSIh3oVQvA1zkztUJxdKPTygQM4sbo65%2ByfmlIzXJ4NLSb%2FV1sFXz7fxhwe70iZBvp%2BYvqFxpdFJ83rmJlAtCFtw1%2FFoOxHHj7lUud%2B32XOSgPCg0hSlbjOCmHbETEKh8XNcSZUkjkhMIvYd5a8fJ3Mhf8r4nDGQOLC%2FDxOB5ZaFgAc6vybg9Q48EqhChQMC%2FIbBWmh6mw5A5m7Q2vA9zj6zwWPT3lrG2UrC2o3J2Oy4QclHdbD4qZdA6gZVCeIrfmTQOEvR96HMW0owMBcnbeJUCK0iDaa%2B6XrhdsJ6Du1%2FYEO0NNCJ6Bkg3SVdADO6CcMfNFanACPic0mw9EPAlvuHF9eJMaop9lTq9vXgBMCiyvov5RnA5ahoHFyTVUFqv62Ctm6Mes1g3hVoOs8dHTLgQMzNr2o0W%2FNeBJ1LfNEoqn5WG8B6NUal6A6jS7ep7vnNW0KzBBKzJ9vKpFtZVxUmIFxyxyjk3t6bg5xCDVf5ptjoJcfbarODOI79dUXVjClfWsuAJ5TpGbm%2BUXTSlK4wjO1LfJPWc9aKvB0Vp%2BML7%2Bmb0GOqUBm%2FhepWcVfrwF3n8dyGfNSBXRLk85Ds4yY5xhbRnFODyvLvrkvryffJ9uS3qb2tAILQYqTxU2VfIBbimd0okbw8WMB9PrF2O%2FLZqs7XqGbXex84JrFLLhNFPQeKwzrA9zxVvl9sCA24kOwcpGMgI0VZrSn9WMaIX6ch5JZg95rhLaYcVaED4P%2BYIc8ZgPPW0sfGyEzTUDZRg3RlwZ0NFD6vA9Yya3&X-Amz-Signature=fc5912ed01e44e4fa8aa581241f8c5743b2813420a497629ebed0e0c43e7dc1d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TEYNLIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCqafut5rDdN9Dgzfm7S7%2Fxy0FX5vBBsLgJDQpdKRd6AwIgdGw0JGpVAIdwgYId0URUxcJ6cAJgszj%2BMsjrXSTaeGkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDgmofn5J%2BIW7cgQyyrcA1z3legq3K00sKXO0T%2FMpvxdOSIFF1bpoRP3vm8IkuM4ojHm6B2ELYOl9xDZPasJgaBvOaWdSHW1qBoFnSaSIh3oVQvA1zkztUJxdKPTygQM4sbo65%2ByfmlIzXJ4NLSb%2FV1sFXz7fxhwe70iZBvp%2BYvqFxpdFJ83rmJlAtCFtw1%2FFoOxHHj7lUud%2B32XOSgPCg0hSlbjOCmHbETEKh8XNcSZUkjkhMIvYd5a8fJ3Mhf8r4nDGQOLC%2FDxOB5ZaFgAc6vybg9Q48EqhChQMC%2FIbBWmh6mw5A5m7Q2vA9zj6zwWPT3lrG2UrC2o3J2Oy4QclHdbD4qZdA6gZVCeIrfmTQOEvR96HMW0owMBcnbeJUCK0iDaa%2B6XrhdsJ6Du1%2FYEO0NNCJ6Bkg3SVdADO6CcMfNFanACPic0mw9EPAlvuHF9eJMaop9lTq9vXgBMCiyvov5RnA5ahoHFyTVUFqv62Ctm6Mes1g3hVoOs8dHTLgQMzNr2o0W%2FNeBJ1LfNEoqn5WG8B6NUal6A6jS7ep7vnNW0KzBBKzJ9vKpFtZVxUmIFxyxyjk3t6bg5xCDVf5ptjoJcfbarODOI79dUXVjClfWsuAJ5TpGbm%2BUXTSlK4wjO1LfJPWc9aKvB0Vp%2BML7%2Bmb0GOqUBm%2FhepWcVfrwF3n8dyGfNSBXRLk85Ds4yY5xhbRnFODyvLvrkvryffJ9uS3qb2tAILQYqTxU2VfIBbimd0okbw8WMB9PrF2O%2FLZqs7XqGbXex84JrFLLhNFPQeKwzrA9zxVvl9sCA24kOwcpGMgI0VZrSn9WMaIX6ch5JZg95rhLaYcVaED4P%2BYIc8ZgPPW0sfGyEzTUDZRg3RlwZ0NFD6vA9Yya3&X-Amz-Signature=6972da68e5f16b09da72f7379b44ddd8b7e318650ccbdbdf545c874f259bd38c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TEYNLIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCqafut5rDdN9Dgzfm7S7%2Fxy0FX5vBBsLgJDQpdKRd6AwIgdGw0JGpVAIdwgYId0URUxcJ6cAJgszj%2BMsjrXSTaeGkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDgmofn5J%2BIW7cgQyyrcA1z3legq3K00sKXO0T%2FMpvxdOSIFF1bpoRP3vm8IkuM4ojHm6B2ELYOl9xDZPasJgaBvOaWdSHW1qBoFnSaSIh3oVQvA1zkztUJxdKPTygQM4sbo65%2ByfmlIzXJ4NLSb%2FV1sFXz7fxhwe70iZBvp%2BYvqFxpdFJ83rmJlAtCFtw1%2FFoOxHHj7lUud%2B32XOSgPCg0hSlbjOCmHbETEKh8XNcSZUkjkhMIvYd5a8fJ3Mhf8r4nDGQOLC%2FDxOB5ZaFgAc6vybg9Q48EqhChQMC%2FIbBWmh6mw5A5m7Q2vA9zj6zwWPT3lrG2UrC2o3J2Oy4QclHdbD4qZdA6gZVCeIrfmTQOEvR96HMW0owMBcnbeJUCK0iDaa%2B6XrhdsJ6Du1%2FYEO0NNCJ6Bkg3SVdADO6CcMfNFanACPic0mw9EPAlvuHF9eJMaop9lTq9vXgBMCiyvov5RnA5ahoHFyTVUFqv62Ctm6Mes1g3hVoOs8dHTLgQMzNr2o0W%2FNeBJ1LfNEoqn5WG8B6NUal6A6jS7ep7vnNW0KzBBKzJ9vKpFtZVxUmIFxyxyjk3t6bg5xCDVf5ptjoJcfbarODOI79dUXVjClfWsuAJ5TpGbm%2BUXTSlK4wjO1LfJPWc9aKvB0Vp%2BML7%2Bmb0GOqUBm%2FhepWcVfrwF3n8dyGfNSBXRLk85Ds4yY5xhbRnFODyvLvrkvryffJ9uS3qb2tAILQYqTxU2VfIBbimd0okbw8WMB9PrF2O%2FLZqs7XqGbXex84JrFLLhNFPQeKwzrA9zxVvl9sCA24kOwcpGMgI0VZrSn9WMaIX6ch5JZg95rhLaYcVaED4P%2BYIc8ZgPPW0sfGyEzTUDZRg3RlwZ0NFD6vA9Yya3&X-Amz-Signature=47cd41269188480982b25ba1bf6889e79dc1a115ba24ae13b247fd568d556271&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TEYNLIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCqafut5rDdN9Dgzfm7S7%2Fxy0FX5vBBsLgJDQpdKRd6AwIgdGw0JGpVAIdwgYId0URUxcJ6cAJgszj%2BMsjrXSTaeGkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDgmofn5J%2BIW7cgQyyrcA1z3legq3K00sKXO0T%2FMpvxdOSIFF1bpoRP3vm8IkuM4ojHm6B2ELYOl9xDZPasJgaBvOaWdSHW1qBoFnSaSIh3oVQvA1zkztUJxdKPTygQM4sbo65%2ByfmlIzXJ4NLSb%2FV1sFXz7fxhwe70iZBvp%2BYvqFxpdFJ83rmJlAtCFtw1%2FFoOxHHj7lUud%2B32XOSgPCg0hSlbjOCmHbETEKh8XNcSZUkjkhMIvYd5a8fJ3Mhf8r4nDGQOLC%2FDxOB5ZaFgAc6vybg9Q48EqhChQMC%2FIbBWmh6mw5A5m7Q2vA9zj6zwWPT3lrG2UrC2o3J2Oy4QclHdbD4qZdA6gZVCeIrfmTQOEvR96HMW0owMBcnbeJUCK0iDaa%2B6XrhdsJ6Du1%2FYEO0NNCJ6Bkg3SVdADO6CcMfNFanACPic0mw9EPAlvuHF9eJMaop9lTq9vXgBMCiyvov5RnA5ahoHFyTVUFqv62Ctm6Mes1g3hVoOs8dHTLgQMzNr2o0W%2FNeBJ1LfNEoqn5WG8B6NUal6A6jS7ep7vnNW0KzBBKzJ9vKpFtZVxUmIFxyxyjk3t6bg5xCDVf5ptjoJcfbarODOI79dUXVjClfWsuAJ5TpGbm%2BUXTSlK4wjO1LfJPWc9aKvB0Vp%2BML7%2Bmb0GOqUBm%2FhepWcVfrwF3n8dyGfNSBXRLk85Ds4yY5xhbRnFODyvLvrkvryffJ9uS3qb2tAILQYqTxU2VfIBbimd0okbw8WMB9PrF2O%2FLZqs7XqGbXex84JrFLLhNFPQeKwzrA9zxVvl9sCA24kOwcpGMgI0VZrSn9WMaIX6ch5JZg95rhLaYcVaED4P%2BYIc8ZgPPW0sfGyEzTUDZRg3RlwZ0NFD6vA9Yya3&X-Amz-Signature=e07d73d4161610f4d747884f51eab33c4f90080a5c828361bf09239395f02c63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TEYNLIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCqafut5rDdN9Dgzfm7S7%2Fxy0FX5vBBsLgJDQpdKRd6AwIgdGw0JGpVAIdwgYId0URUxcJ6cAJgszj%2BMsjrXSTaeGkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDgmofn5J%2BIW7cgQyyrcA1z3legq3K00sKXO0T%2FMpvxdOSIFF1bpoRP3vm8IkuM4ojHm6B2ELYOl9xDZPasJgaBvOaWdSHW1qBoFnSaSIh3oVQvA1zkztUJxdKPTygQM4sbo65%2ByfmlIzXJ4NLSb%2FV1sFXz7fxhwe70iZBvp%2BYvqFxpdFJ83rmJlAtCFtw1%2FFoOxHHj7lUud%2B32XOSgPCg0hSlbjOCmHbETEKh8XNcSZUkjkhMIvYd5a8fJ3Mhf8r4nDGQOLC%2FDxOB5ZaFgAc6vybg9Q48EqhChQMC%2FIbBWmh6mw5A5m7Q2vA9zj6zwWPT3lrG2UrC2o3J2Oy4QclHdbD4qZdA6gZVCeIrfmTQOEvR96HMW0owMBcnbeJUCK0iDaa%2B6XrhdsJ6Du1%2FYEO0NNCJ6Bkg3SVdADO6CcMfNFanACPic0mw9EPAlvuHF9eJMaop9lTq9vXgBMCiyvov5RnA5ahoHFyTVUFqv62Ctm6Mes1g3hVoOs8dHTLgQMzNr2o0W%2FNeBJ1LfNEoqn5WG8B6NUal6A6jS7ep7vnNW0KzBBKzJ9vKpFtZVxUmIFxyxyjk3t6bg5xCDVf5ptjoJcfbarODOI79dUXVjClfWsuAJ5TpGbm%2BUXTSlK4wjO1LfJPWc9aKvB0Vp%2BML7%2Bmb0GOqUBm%2FhepWcVfrwF3n8dyGfNSBXRLk85Ds4yY5xhbRnFODyvLvrkvryffJ9uS3qb2tAILQYqTxU2VfIBbimd0okbw8WMB9PrF2O%2FLZqs7XqGbXex84JrFLLhNFPQeKwzrA9zxVvl9sCA24kOwcpGMgI0VZrSn9WMaIX6ch5JZg95rhLaYcVaED4P%2BYIc8ZgPPW0sfGyEzTUDZRg3RlwZ0NFD6vA9Yya3&X-Amz-Signature=f2956bbb18db4aa2c5427e5ec1f8555098a34b83a55a918ec180996d9a73f38e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662THXT7RY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAFYmtX9sIlkuo1lk3d%2BoIslNrjHOsEX3f%2FdvVhnuVwsAiEApuVRYyNeJvhwjq3l3IiA6UE6FKIfPqooE7La9xo0KzYq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDJGNWv53R%2FLNLJJmJircA2RxaV4hxMqZ1I%2B03mvFvsUMSlhcbt3JSumU5xtd0NwSDTueI9tUq81RjzfRGF9xPXK1Xe5MCoOTxIVE6DL8jCE2I9dlBin%2FCJcJH34fcFOB9RVXwQxM%2B7edx1kWaK%2FgKA%2BAdtRvpz7dF2WzoUwJ8r70Cji7oQhPJx4nbHBy%2Fr6mGh7W2lhLWXW%2B2R56uLkGmD7ewlgsFrx1l043xjSjs6hzh0qQaD6i0%2FP35wBm2gPIwPNt9C0eNsU0cvxy6WFzJEMzpk6YGqjWJprJmj0%2B8sdAcQxZ2Wh9SpXeTYjVvU78MnV7B8xi9klQ8zhL45INBJLI5lT7pL%2BtYgosDfKZuYTVLFYiHRfVkmAxWM50IQvjQrqzt7Jkkcd5J3ovjpnOPDBYzQvPjR4m%2FU4m%2BD6nZ0bNZHudy6%2BhV5FeOug83l8NaQD7xtzEr%2BHmfJUH4xtkcrccBc8Jvy5GMOieT273qbg49a1nZhr7Y0BoyEjTL%2BptlqCYVEwqF8DVyS6eaLAK8frE7AKE5boU%2F4T440%2BIPYec%2BzWIlmuq%2FgWEIG1NiZROF2Lg3wk0U4qtpt%2FB6%2F3fNclODhIX3FNg%2B6Al4XXuC%2FXKok45Mj82t8B87xSmhgkhegKmZNFoJQ525kE1MNr%2Bmb0GOqUBRAV%2FgJgeTDsQ0NPRL%2FYxTzDH262lkLLlpfWfN9jvG0GdfItGnFh%2BDDtd9Nid8T0DnTKFpc4X%2BIxtKefnFjXwn4ircmjr8xnvRavBGs10Ve16LEENsCEmuYpdX0K7tmYIoESIQUXEy6MYlcTd9aaUant6yxF8mD%2Ffq4ZzCWSixB0am99MeE8pyZ8T8YUJGRzDUuhuumh5AxzCXdh%2BrQpKqfR5DuFv&X-Amz-Signature=0dba572caeef285c3df0410bfb7eb55eaa7aa7046c4987322d3993e77a5072fe&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZID5GZJL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQD1GIiyVlye%2FZ0hjPcl10BRw3cdFPsGh%2Fr1SubcT0L2XwIhAPI5uhnD%2Bs4TCznS%2FCskVDVo7DFUk%2FqaJyNHbRbz1vzIKv8DCH8QABoMNjM3NDIzMTgzODA1Igy7lXTXCxFxa0SANyQq3AN%2BGgdcKzThn2ZENVjUsCVRP2Yi2cxqdz8dQO3hGKIr6NiuBHdP6NPlaoAEvd1QbGyN6eZpOj8umy0hACzSL8%2FNtc%2BLSeS75flEhfIQQUrUmipl6AMuL95a9E69ZKYYYrDI%2FZwr4jCjX7VIzkQMTbFCkbDizUfmVI%2F5O2ZoE4wzB7o4d4BfI%2Fymsc5hI9nOQ2Po%2BR%2BdMXf1YyfpI4Dkpo2ItLYtnTaPPf1Pf39F4i1aEZkcjClj0aW6RBsQuQwRyt%2Frnu9uDSUGGusJirlyY%2FF75SqTJ74vTKZyc4cipiGikOctZmQtsANpf80vv56j9Op6Qx488kkzjxPl%2BDpCYm5TnCtcpX4qbTy8PfhYuKaRPPGxz%2FVkv9fusW8Y8bFbeV3hf6AjazdS%2Bv02RV86xklVJw%2FiCKWsmpq3QOjH01HV5pIXEolFw%2FNYyMXHvGdPLlqppaEECkYUJAvtLbocsy0UP%2BcUoZXyQzfRtRCBpe6MFQCsXKdLBus7yB%2B2ULDDeLGWSieARqp4aNi9SMXGixWqGBcLa54MLEaKRzh2JmJp3nKdYf9ND78i7d5HfUQ4a%2B0gGvERxqKVENy3wOEqH7C%2BCjjM8xz%2FKokW7D5VJ5KXFlZzhqGDwqrgnGS2RTCU%2Fpm9BjqkAd1rJ%2BOKmBsbWGYt3DouIYDuKsyi%2BoU%2BXUZmcn%2F9P6O%2B%2FUI4gRv%2FT77aP6PIANSEereXSQyCxjQkUGzDzrRXhsJi1m%2BTM4Z4YnmvyfsnuzhaTBN293YP%2FSxa8H1ed4HvrbC7HipbZG7XxxPwVHdTYi%2Fj4F4WXpgostXO%2BLNhZe9l4BcC2zVIXGr%2FzDAyAWyaavlASK6V3EFDDJ0GQMabjntWt2QE&X-Amz-Signature=91eea296fcec81f339e87af0580230bdb179a921a8dbc05cb7abaea146d5d915&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TEYNLIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCqafut5rDdN9Dgzfm7S7%2Fxy0FX5vBBsLgJDQpdKRd6AwIgdGw0JGpVAIdwgYId0URUxcJ6cAJgszj%2BMsjrXSTaeGkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDgmofn5J%2BIW7cgQyyrcA1z3legq3K00sKXO0T%2FMpvxdOSIFF1bpoRP3vm8IkuM4ojHm6B2ELYOl9xDZPasJgaBvOaWdSHW1qBoFnSaSIh3oVQvA1zkztUJxdKPTygQM4sbo65%2ByfmlIzXJ4NLSb%2FV1sFXz7fxhwe70iZBvp%2BYvqFxpdFJ83rmJlAtCFtw1%2FFoOxHHj7lUud%2B32XOSgPCg0hSlbjOCmHbETEKh8XNcSZUkjkhMIvYd5a8fJ3Mhf8r4nDGQOLC%2FDxOB5ZaFgAc6vybg9Q48EqhChQMC%2FIbBWmh6mw5A5m7Q2vA9zj6zwWPT3lrG2UrC2o3J2Oy4QclHdbD4qZdA6gZVCeIrfmTQOEvR96HMW0owMBcnbeJUCK0iDaa%2B6XrhdsJ6Du1%2FYEO0NNCJ6Bkg3SVdADO6CcMfNFanACPic0mw9EPAlvuHF9eJMaop9lTq9vXgBMCiyvov5RnA5ahoHFyTVUFqv62Ctm6Mes1g3hVoOs8dHTLgQMzNr2o0W%2FNeBJ1LfNEoqn5WG8B6NUal6A6jS7ep7vnNW0KzBBKzJ9vKpFtZVxUmIFxyxyjk3t6bg5xCDVf5ptjoJcfbarODOI79dUXVjClfWsuAJ5TpGbm%2BUXTSlK4wjO1LfJPWc9aKvB0Vp%2BML7%2Bmb0GOqUBm%2FhepWcVfrwF3n8dyGfNSBXRLk85Ds4yY5xhbRnFODyvLvrkvryffJ9uS3qb2tAILQYqTxU2VfIBbimd0okbw8WMB9PrF2O%2FLZqs7XqGbXex84JrFLLhNFPQeKwzrA9zxVvl9sCA24kOwcpGMgI0VZrSn9WMaIX6ch5JZg95rhLaYcVaED4P%2BYIc8ZgPPW0sfGyEzTUDZRg3RlwZ0NFD6vA9Yya3&X-Amz-Signature=e01e70828bfda2f71d15b21162e02edf73a9fa2d0f0e1012c75e273739467050&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TEYNLIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCqafut5rDdN9Dgzfm7S7%2Fxy0FX5vBBsLgJDQpdKRd6AwIgdGw0JGpVAIdwgYId0URUxcJ6cAJgszj%2BMsjrXSTaeGkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDgmofn5J%2BIW7cgQyyrcA1z3legq3K00sKXO0T%2FMpvxdOSIFF1bpoRP3vm8IkuM4ojHm6B2ELYOl9xDZPasJgaBvOaWdSHW1qBoFnSaSIh3oVQvA1zkztUJxdKPTygQM4sbo65%2ByfmlIzXJ4NLSb%2FV1sFXz7fxhwe70iZBvp%2BYvqFxpdFJ83rmJlAtCFtw1%2FFoOxHHj7lUud%2B32XOSgPCg0hSlbjOCmHbETEKh8XNcSZUkjkhMIvYd5a8fJ3Mhf8r4nDGQOLC%2FDxOB5ZaFgAc6vybg9Q48EqhChQMC%2FIbBWmh6mw5A5m7Q2vA9zj6zwWPT3lrG2UrC2o3J2Oy4QclHdbD4qZdA6gZVCeIrfmTQOEvR96HMW0owMBcnbeJUCK0iDaa%2B6XrhdsJ6Du1%2FYEO0NNCJ6Bkg3SVdADO6CcMfNFanACPic0mw9EPAlvuHF9eJMaop9lTq9vXgBMCiyvov5RnA5ahoHFyTVUFqv62Ctm6Mes1g3hVoOs8dHTLgQMzNr2o0W%2FNeBJ1LfNEoqn5WG8B6NUal6A6jS7ep7vnNW0KzBBKzJ9vKpFtZVxUmIFxyxyjk3t6bg5xCDVf5ptjoJcfbarODOI79dUXVjClfWsuAJ5TpGbm%2BUXTSlK4wjO1LfJPWc9aKvB0Vp%2BML7%2Bmb0GOqUBm%2FhepWcVfrwF3n8dyGfNSBXRLk85Ds4yY5xhbRnFODyvLvrkvryffJ9uS3qb2tAILQYqTxU2VfIBbimd0okbw8WMB9PrF2O%2FLZqs7XqGbXex84JrFLLhNFPQeKwzrA9zxVvl9sCA24kOwcpGMgI0VZrSn9WMaIX6ch5JZg95rhLaYcVaED4P%2BYIc8ZgPPW0sfGyEzTUDZRg3RlwZ0NFD6vA9Yya3&X-Amz-Signature=6ce77cca715b67fd17db58c1879fcec605a053be34bdd1f3417692f9b6a9e22b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TEYNLIY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCqafut5rDdN9Dgzfm7S7%2Fxy0FX5vBBsLgJDQpdKRd6AwIgdGw0JGpVAIdwgYId0URUxcJ6cAJgszj%2BMsjrXSTaeGkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDgmofn5J%2BIW7cgQyyrcA1z3legq3K00sKXO0T%2FMpvxdOSIFF1bpoRP3vm8IkuM4ojHm6B2ELYOl9xDZPasJgaBvOaWdSHW1qBoFnSaSIh3oVQvA1zkztUJxdKPTygQM4sbo65%2ByfmlIzXJ4NLSb%2FV1sFXz7fxhwe70iZBvp%2BYvqFxpdFJ83rmJlAtCFtw1%2FFoOxHHj7lUud%2B32XOSgPCg0hSlbjOCmHbETEKh8XNcSZUkjkhMIvYd5a8fJ3Mhf8r4nDGQOLC%2FDxOB5ZaFgAc6vybg9Q48EqhChQMC%2FIbBWmh6mw5A5m7Q2vA9zj6zwWPT3lrG2UrC2o3J2Oy4QclHdbD4qZdA6gZVCeIrfmTQOEvR96HMW0owMBcnbeJUCK0iDaa%2B6XrhdsJ6Du1%2FYEO0NNCJ6Bkg3SVdADO6CcMfNFanACPic0mw9EPAlvuHF9eJMaop9lTq9vXgBMCiyvov5RnA5ahoHFyTVUFqv62Ctm6Mes1g3hVoOs8dHTLgQMzNr2o0W%2FNeBJ1LfNEoqn5WG8B6NUal6A6jS7ep7vnNW0KzBBKzJ9vKpFtZVxUmIFxyxyjk3t6bg5xCDVf5ptjoJcfbarODOI79dUXVjClfWsuAJ5TpGbm%2BUXTSlK4wjO1LfJPWc9aKvB0Vp%2BML7%2Bmb0GOqUBm%2FhepWcVfrwF3n8dyGfNSBXRLk85Ds4yY5xhbRnFODyvLvrkvryffJ9uS3qb2tAILQYqTxU2VfIBbimd0okbw8WMB9PrF2O%2FLZqs7XqGbXex84JrFLLhNFPQeKwzrA9zxVvl9sCA24kOwcpGMgI0VZrSn9WMaIX6ch5JZg95rhLaYcVaED4P%2BYIc8ZgPPW0sfGyEzTUDZRg3RlwZ0NFD6vA9Yya3&X-Amz-Signature=c40f77b650d57850b57953f2be1cf02d94a66840723dc37d6194935086cd9462&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NQF5HDY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIB8%2FAQV2pAgrBwTIdC6V7J%2BPwLmtTC%2Fat6u%2BSNkjdDxtAiAm2NnUHydC74qPo%2BMLwN4YDoxKGPzOXmOFIv%2Fpfs0Y1Sr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMFYDnO%2B9MVziCzxStKtwDJzxBpRkOPlV5jwHv%2BetAfugr8lssESdf72C7agWmL4zyWHdkTAcharWKVyLIqUMKDDDbDY1sBNRXmRBHIfSa0nKP4fHqt6omnUbhNDLuVj6xM0MbCJC%2BmNxRz2yqFLUZ%2B7d0%2Fmhp%2Bbvr6arBMojzDGE5ybaf89dsVobRPXcRx280vBSG8L7TvmJJtTm439aszeIm1%2BWpd4RuPTK16JMyySH7FOMTLfXrQqJpNbsQBjIySjzJLMRT61fYvB6MV6JsKPEsR7zGfLHlVk%2FDr0vK3MDet6V0d%2FnrgBaoPBIqeuCiDmXkMxakbd%2BQW798SHr0IVn%2BcB6uWbfPkW%2F4WW%2BHE%2BaKZTzjQSGaUhtqxIrvw%2FwcpAhHcBwkMaBM2Koqfvwn12QKMzVMS6QM6vw8bfBZaoFDm2AfONXgpyMLNCZXIYPt0P3mWMYjOr5lM9cun3Tj7EcCcdTdwccqRimyd3mLjVZrNohREQ%2B7vTAFoZ8dqUX3mj2UM6f9eIcQXWddY7VG3oRZeKkcwzsBgwLFBHzRoZgsJL0aiJRfPlVPc38u6pcTm1v%2B9Psu7APongDDfTuq%2FR0kkiTyNySGMbMhU6TRGIxcxdvkebbaCBc9l6xztwXyWTvw2MQqXb3ndjkw5P6ZvQY6pgHhEem2Zq1y6xvKnOXAraN%2FkAxPtTGVsTS%2BjDMLYZuAab2qRCsD07gvsMnrkrYK2vbib1tdm%2BhvNTGaZ9NwiJ7P77Ymu%2F0%2Be3rPvI0p3muI8SfXmMvQ1pYv2gwdmzE3glGQ2zCi7DeqHGo7BotV%2Frkzc1owok193IeON%2B1cdmL3kMtWnZQRaZmiLBFgrXcwBdYal46rMQvHYX9NmAN2VtiBg%2BMNlbNZ&X-Amz-Signature=74a21f4433454acd86866757a455bbdb83870ba19698c822a20cf0b3234bcca8&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IHYPZV6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIBa44Ps1lEM3j8ERnyjDfgy4K5Kezyy4pwSNYBu%2FKbRlAiA90CbZr4eJr59cJIzxc0uzjrsn%2FfcemvA%2B7au%2F5WybPyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMtzmgcm%2FYXkWhG0KyKtwDP%2Fh9GmjMMfKAEMKgN53%2FD0EyHzO5eoLgviEKhw8nyPVCPOpX7ba96XOaQwrx1YY%2F5oD%2BSkx%2BPktUVepUsGIkmTMzoGWnz%2FGvVOQnSXOlnrbsgO6ThcufrsDd9pbXXqsNyTjhfIubr8AodeES0qrHXSA8RSWM41UQXf72UH9RkKPVUxZt9bveI259lZ1PT%2B2nEBBtETCKmXaOGJHR5jXGPIqNy8ugbLt1c5jmyH4sX40ioHWnOq8b4ElwtjFPY2kaUGvWU1SmUBv07s4TsquL3AkXBpQUBq8Rl%2FTneggisTNfSCGgzD8aInlo%2BHSpTAmjwthRlBpTbx8MaQJogHybrxygf318qtEAKg6DT2wUiJwUPRE4K4SRCkbYdKzK9Qf6lkvcQY7Jge2jxrh6DQSxOU5nBvropPYsRAzhyO8%2FgNcAQS2X5iA3naxEA7sfL11KE6ohVqu8uUauM0vzVLGsfnpSmRpNtauF009Cu%2FZ0bANAO3JLR5ZbBiujJdXlduRRL3JlGlrAxai3eAdhnYr5D0G22MWwzSV%2BBQUQjoU51ws1dL8c%2Bfe6jsBU5k4AhblBMRx7SxY7rWSHlcZUYlgreOgPBK6jw0hzx3NsZWVrWWkXa0mqi9vY9Zwa9iYwvP6ZvQY6pgFDnzR9K2V57YjcyTbhusXNnHBP6UXTkmf3gvW07Kds3zz2G%2BfcJfn7mLC%2F76SAojzLxk365S%2BxNvz02anq7Qdh9l%2FLZVhFwI60EWPVtKPSrF1Gni233VUP1KYRBXZ4YKO2vCk0jBnqwVFBEP9W1HH1o9jXCV8tcG2ucbO1M9wGELAyE3U39wQD4idSRAbn3n5jZkhHMZqZNSSleGyNyfAYo8N%2FGdQj&X-Amz-Signature=ba4c9e95f969ad1e1acf8b01d1419e86514f570c7ca6edad0ad038dff5a45b58&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RS64P5I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCsfgCQHUWWo7KVeocvFLESvjZJIvdtFjLQMFIm6h%2BKbwIgGBvkO3RXI8C6attrBaSIQIPlIySQZHv78%2FvX1EChmJAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLk1t%2BqsKxqyQskF%2FyrcA%2BulosWNJYvAxY3a2y4Ulo2wKjNlqJxW2aoGongu5%2BfZTTzWYkQPFJEU9I5YRKuoIIADbsk2Nxau7a5yWkIStbCPzhB7rcaoMUdPwn8fn7Poz3QYighP%2BAk7m54andD6%2BIPvHWvqeK%2FLwwYN4k5IbO88SVRXXZKQ1woSxy6B%2B16iO59oKi%2BVZ9s8m9lcGJ%2FfFQElIivetZgEBFI%2FEQx3XrzH1SPMK2yE52MvWO0QaoAYL8pRnsQ7P%2FR1av3YcB7%2F71MLmgklDj8Miu1lmNxv8yOIQq9y9mDsVJwdOe4efqgXgbgs0PU8VAjeLszLv1MXuRyRSUVwyOFkPhWGq4NRsZddlx4nxUVTImZulhazke%2BodWge2rr8QAHv4COb52wNMBh1ATLFeJyN4qBvcHZmpyKnrBkdDgNX2y48b5w5DqInozX%2BcTH2gdZ%2BtpeSC7y%2FK1Zrp1WUv58ojfFu4n7fGoPx6YS3VO%2FWrCiLiYn%2F6Jj3uE3Y3AfuLlDLVCox8cF9bu%2FbNqfwiajQ5aAff1oKgKOoi12RDZXLqfpLwCXR9%2BQvCznV0PTuDXUzia0LK8KsGpmzAH13LAraRoP1yynwBX1KIS8uTJRVURwA4cM6oqCrbGXCWTYJb3RM9qHQML%2F%2Bmb0GOqUBpKFIEOoMdWM9KKi6JVUnGmGkLaCj0EsY5Nrn6Ae3UI9iJMpQ%2BONzQ2kenBcvadYm9PV6b%2FIA4wtVNQRdidJXbypINWXanAgLij9MEbXsHoiUqQd4vciMHsJG1CJepAE%2B0uyJQgfQnymxUCVjQYkii%2FF3QrigbhyAWLohrbsVW6Lz3KhmSsLC5gky%2FlOLhB0WHl4E0Ztu02WZ8EUCE1kfgiQq7IaE&X-Amz-Signature=18ed197e4e1a13e7a1e3b4ef8de792494d611f91ef549bda987d65c194a464b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466455O4UIZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIALHU5BywEMVqjIRTnBIGDEK9kfgBwcSrBJZyW%2BGJF4UAiAAsC81emacojMU6cPR%2Fh6BYmtMRRtWU6o9UHTli%2BvZ1yr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMsOU3pOoN%2BusQsiFwKtwDUZ6LdGk5yofYJKUOiYfsOjFEm6JaC9%2FNp%2BLQN%2FPsNvMdCDn%2B%2F9LRrSnv%2FKMpqOrywPCP%2Btd79HPyrHY3DC87V5Qdgcz80sCBEVCcR1M%2FmZZczBG7BH9xi1zSAI2w5abmzjq40I2Ml9YgB3NwBYlwqo%2FbFFw4gjucK9hdSRiWegp9QPbZIL3XLkDGp2u12wKPcFtBhkEJ3ljZAXnRcxzg2WM6l4uaMhJ20CzIqc7Zruw9vfIQ9h9SSdHnmDKHULwn7wHPV9tY%2FlpjQRVGvw5ZuRFkdG8eGMZmoB0c%2BapKM7W3AEWux1XROIw9qpJY%2BFqH14YtNOEONZ0ABOX6%2FI%2Ftfkpasbbsl2Jgw%2FymuAVxCobOZPXbXPS5%2FwHIrwi9mcJU6GgFlV6duvrjMq015LOMXmeaavpikev5wgQhve%2FQcrf7gq59drJY0vGuUKDmKw6oVJfialocrCUGsbM4TmSFZBe1tWfzGsKHGU29JYfvZYvEZAWiDLyNxlXa28g3SEUBLxfujVEk7Vllp9l8lqnCsCM7Zf0I%2BPVq69ym9XBqr5a3tWvtwbN45NfcEjc5ozQXq%2BR97OZTuOI6wI9pMLD6itdUJkPt0FnOGP1m6pXKEpLI0sAdPUC3uPGz66Awxv6ZvQY6pgFVcDeU5TPi2DSq6swGTycKcMUrF70XIHnC9vOO0nC8QQdpzNDyww8qA0PE47uWhj%2FX%2BAzONgnFhI%2FBJfECTazpAbXznhbZunOSzaw%2Foe%2BYLFkBr8%2F5UH%2FoWzPB3h1BfO82%2BKqw8%2B3uSyqvBr6JYbMI7xBV58Usb54CRcwqF1UV7v2Z%2BYBiYyAh7bA2pXg42J%2B205HVcPanUFH5vZwg2IJzTBeDQc4%2B&X-Amz-Signature=656468b7980dd1b6033e515c2cd6b24a17d8b7ba3581e5de96850c2dff148a05&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466455O4UIZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIALHU5BywEMVqjIRTnBIGDEK9kfgBwcSrBJZyW%2BGJF4UAiAAsC81emacojMU6cPR%2Fh6BYmtMRRtWU6o9UHTli%2BvZ1yr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMsOU3pOoN%2BusQsiFwKtwDUZ6LdGk5yofYJKUOiYfsOjFEm6JaC9%2FNp%2BLQN%2FPsNvMdCDn%2B%2F9LRrSnv%2FKMpqOrywPCP%2Btd79HPyrHY3DC87V5Qdgcz80sCBEVCcR1M%2FmZZczBG7BH9xi1zSAI2w5abmzjq40I2Ml9YgB3NwBYlwqo%2FbFFw4gjucK9hdSRiWegp9QPbZIL3XLkDGp2u12wKPcFtBhkEJ3ljZAXnRcxzg2WM6l4uaMhJ20CzIqc7Zruw9vfIQ9h9SSdHnmDKHULwn7wHPV9tY%2FlpjQRVGvw5ZuRFkdG8eGMZmoB0c%2BapKM7W3AEWux1XROIw9qpJY%2BFqH14YtNOEONZ0ABOX6%2FI%2Ftfkpasbbsl2Jgw%2FymuAVxCobOZPXbXPS5%2FwHIrwi9mcJU6GgFlV6duvrjMq015LOMXmeaavpikev5wgQhve%2FQcrf7gq59drJY0vGuUKDmKw6oVJfialocrCUGsbM4TmSFZBe1tWfzGsKHGU29JYfvZYvEZAWiDLyNxlXa28g3SEUBLxfujVEk7Vllp9l8lqnCsCM7Zf0I%2BPVq69ym9XBqr5a3tWvtwbN45NfcEjc5ozQXq%2BR97OZTuOI6wI9pMLD6itdUJkPt0FnOGP1m6pXKEpLI0sAdPUC3uPGz66Awxv6ZvQY6pgFVcDeU5TPi2DSq6swGTycKcMUrF70XIHnC9vOO0nC8QQdpzNDyww8qA0PE47uWhj%2FX%2BAzONgnFhI%2FBJfECTazpAbXznhbZunOSzaw%2Foe%2BYLFkBr8%2F5UH%2FoWzPB3h1BfO82%2BKqw8%2B3uSyqvBr6JYbMI7xBV58Usb54CRcwqF1UV7v2Z%2BYBiYyAh7bA2pXg42J%2B205HVcPanUFH5vZwg2IJzTBeDQc4%2B&X-Amz-Signature=714af7921c55c117ceacf0f89b408065cc8096c4e22b343b676061560a2d9245&X-Amz-SignedHeaders=host&x-id=GetObject)

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
