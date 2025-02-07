

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665V3L6LRG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIBk7iKXR0LdGL%2FuDqD6FRlP0zgI1%2BBuOdO0mauIidNGJAiEAw7JebST6E9X5nFYf4cJpt457xRlVKX7oLd40oGJa%2B88q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDNhJPrzBJR8AYnHcPSrcA1ZTUj0yFyxolLf0eF7jiO0WzaSbDWoEqb8bYDTNJX2UyzB2c1ZPauiLD%2BcszXsyTmXAg%2FZZ8AJSZgd2cZtGtLH0Bz6ikS0%2BAb1goNRg1sA3F22nRD%2BeQRLIPd8mlutaFhOQc2ruwwtZqUpHX70UW6RigEbQctNT8R9whfcFQyl3uULNM3Z7mjICcFNbPZmYNFBl9SHDZSGB08MRppYmwNS%2F%2BJo0WzTvZPv9pZ4eTxpA%2FkEEo2diN9E8ISRCMigr9pjtPZ6HACR4YnFMAeY70OhgKEZhakbILHo8y5fuQsV0y0wF3MyN0B5TkwXqxUvoRhI%2B%2BxXGmFTDL8pOHwZhltNnL4023ZRkuhC5RhaYF4zjr23CgR%2FI5Z7JmXfhmWkNyukKPQAvQFgN%2F2bBIByfKR0yGeko5qrVvQhFQ6xaBjDSSoagNVLl11Yt48XlnQDClRAvFkkVuLMsvemWJRthbT4IMrc3u9MxbPNLP1KWWdED%2Ft9lrTvpVXPGB%2Fi8mRwYxS1szoPYJUBDLI1c%2FPBiFY89kdr8RvKCAHjQFOSTuTjQNDZ%2F29PM%2FN8OzennZ70%2FIR8amFJuf7i%2BcfG4VDjpKoBn0vd0z4zRFE61DtY0T%2Bv%2FwuZMP5ZCNbUgoW6%2BMJzgmL0GOqUBkwaGSAZ4F2EnVNyO8yraovUKrmjZehoFvglNwhnHqd464mFySIUFFd0wcmzQMJ7KfT4b3pLADNixmz8rK2Qjhi9NbVMBG0xHY3ouyx%2BRekVaXlC2Vh6BzJmtuOdWdE6Rdslu9xQ56x%2FElZlSbUeQ1ORGuo3fCirxGK1Z4K%2BXdKrBlnXVW1QPF%2BblHi5wGQN5d7Weh1F%2FDJZvknRfV5UMDZ8AESlO&X-Amz-Signature=7815897e7d01787d20dc0e7f4bbe589b1e4ebe250d4ca147f3cf664ae57cb929&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665V3L6LRG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIBk7iKXR0LdGL%2FuDqD6FRlP0zgI1%2BBuOdO0mauIidNGJAiEAw7JebST6E9X5nFYf4cJpt457xRlVKX7oLd40oGJa%2B88q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDNhJPrzBJR8AYnHcPSrcA1ZTUj0yFyxolLf0eF7jiO0WzaSbDWoEqb8bYDTNJX2UyzB2c1ZPauiLD%2BcszXsyTmXAg%2FZZ8AJSZgd2cZtGtLH0Bz6ikS0%2BAb1goNRg1sA3F22nRD%2BeQRLIPd8mlutaFhOQc2ruwwtZqUpHX70UW6RigEbQctNT8R9whfcFQyl3uULNM3Z7mjICcFNbPZmYNFBl9SHDZSGB08MRppYmwNS%2F%2BJo0WzTvZPv9pZ4eTxpA%2FkEEo2diN9E8ISRCMigr9pjtPZ6HACR4YnFMAeY70OhgKEZhakbILHo8y5fuQsV0y0wF3MyN0B5TkwXqxUvoRhI%2B%2BxXGmFTDL8pOHwZhltNnL4023ZRkuhC5RhaYF4zjr23CgR%2FI5Z7JmXfhmWkNyukKPQAvQFgN%2F2bBIByfKR0yGeko5qrVvQhFQ6xaBjDSSoagNVLl11Yt48XlnQDClRAvFkkVuLMsvemWJRthbT4IMrc3u9MxbPNLP1KWWdED%2Ft9lrTvpVXPGB%2Fi8mRwYxS1szoPYJUBDLI1c%2FPBiFY89kdr8RvKCAHjQFOSTuTjQNDZ%2F29PM%2FN8OzennZ70%2FIR8amFJuf7i%2BcfG4VDjpKoBn0vd0z4zRFE61DtY0T%2Bv%2FwuZMP5ZCNbUgoW6%2BMJzgmL0GOqUBkwaGSAZ4F2EnVNyO8yraovUKrmjZehoFvglNwhnHqd464mFySIUFFd0wcmzQMJ7KfT4b3pLADNixmz8rK2Qjhi9NbVMBG0xHY3ouyx%2BRekVaXlC2Vh6BzJmtuOdWdE6Rdslu9xQ56x%2FElZlSbUeQ1ORGuo3fCirxGK1Z4K%2BXdKrBlnXVW1QPF%2BblHi5wGQN5d7Weh1F%2FDJZvknRfV5UMDZ8AESlO&X-Amz-Signature=be4acdcf24e5b922f7ab5839407b200e20b58d0afad918a45e8a3aeb40d91214&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665V3L6LRG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIBk7iKXR0LdGL%2FuDqD6FRlP0zgI1%2BBuOdO0mauIidNGJAiEAw7JebST6E9X5nFYf4cJpt457xRlVKX7oLd40oGJa%2B88q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDNhJPrzBJR8AYnHcPSrcA1ZTUj0yFyxolLf0eF7jiO0WzaSbDWoEqb8bYDTNJX2UyzB2c1ZPauiLD%2BcszXsyTmXAg%2FZZ8AJSZgd2cZtGtLH0Bz6ikS0%2BAb1goNRg1sA3F22nRD%2BeQRLIPd8mlutaFhOQc2ruwwtZqUpHX70UW6RigEbQctNT8R9whfcFQyl3uULNM3Z7mjICcFNbPZmYNFBl9SHDZSGB08MRppYmwNS%2F%2BJo0WzTvZPv9pZ4eTxpA%2FkEEo2diN9E8ISRCMigr9pjtPZ6HACR4YnFMAeY70OhgKEZhakbILHo8y5fuQsV0y0wF3MyN0B5TkwXqxUvoRhI%2B%2BxXGmFTDL8pOHwZhltNnL4023ZRkuhC5RhaYF4zjr23CgR%2FI5Z7JmXfhmWkNyukKPQAvQFgN%2F2bBIByfKR0yGeko5qrVvQhFQ6xaBjDSSoagNVLl11Yt48XlnQDClRAvFkkVuLMsvemWJRthbT4IMrc3u9MxbPNLP1KWWdED%2Ft9lrTvpVXPGB%2Fi8mRwYxS1szoPYJUBDLI1c%2FPBiFY89kdr8RvKCAHjQFOSTuTjQNDZ%2F29PM%2FN8OzennZ70%2FIR8amFJuf7i%2BcfG4VDjpKoBn0vd0z4zRFE61DtY0T%2Bv%2FwuZMP5ZCNbUgoW6%2BMJzgmL0GOqUBkwaGSAZ4F2EnVNyO8yraovUKrmjZehoFvglNwhnHqd464mFySIUFFd0wcmzQMJ7KfT4b3pLADNixmz8rK2Qjhi9NbVMBG0xHY3ouyx%2BRekVaXlC2Vh6BzJmtuOdWdE6Rdslu9xQ56x%2FElZlSbUeQ1ORGuo3fCirxGK1Z4K%2BXdKrBlnXVW1QPF%2BblHi5wGQN5d7Weh1F%2FDJZvknRfV5UMDZ8AESlO&X-Amz-Signature=327ba37f81ff656da44bdd98d5e0fe2e7bc90a441d1a26b4ab247812606ace8e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=17ba2ae1261a37f23b93c1cd447319ec83ea2101c8b70bb3c72a7179da96cbe9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=8d7a8062bec0a101cc955b0c24bd4efdcce3616ec59a14c4c750c0293d971e7c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=2ac0a4ec27a9afc5c222c9f0315a68412f88b15c15dd33deb2f91119dccd9152&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=f6271aab62465edb713d409d3553315f2cfdd9cf4352a13bc5ca2e70698a3fe8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=d6ddce6ad81cc5b63bc273f87d47365a765840e8e21246dfbd2b2af3f30bb7d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=e538564c5293be1b4cc19c4d39452f2154ae9994976b539473b1d452ae210d50&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666R7BT7TH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCUXGokgTsUtyzy4eumH0hWElkOe1DwEHl1W%2FXlM3nxfwIhAOd2xZ8pJ8frlRbL1mXUuDVr3bQtML0NkI7Ak4OMb4qdKv8DCHkQABoMNjM3NDIzMTgzODA1Igzr0nQLAjRuj2GCUGgq3AP%2BKTp6RnOt%2FmgYUrHmXLRSzBxHMO5fdiy5WjX4ZXGql5zVq%2Bpxu%2BOw%2BGeUXcMw7z75qI9nyfNbQ2JT39i2rlBkFczzCLzB%2Bhc4boDxO8%2BHDIrt%2F1YddkSrY2X1yTPLGfHeieWWVGHDgGO2Wlnb9v1Z18uT1rsSOAT%2BT3gHadIKMmulXUFNMV9gUcx982CPezQYe37SduHB2TZ5mpD09p15%2F5WrbXPAMMlqYXrCQjBzA4X32F4f3JVrQSgqh0qyXzLKiI7u6GkLwbJRzyGpMNDRNgDDaFtzDnXWZqoYxM5tfa%2BPPGKkTSy0UlS4Y%2B8fKmxJGEdBXOyzRhjtPepPmF9hAFWrg3Vsyuftr7GBLFtMmf5heCJRFej9pODumK4TTtetyjq2IP1cCpB4xCAWgIYj7itJF%2FwuJg7n2%2BWwbHcB1r7C9hCC8IxVcTD%2FlOd27MZHvTO43lz0IdcFdGpSNSUGU%2Fnv7HjjCpVbgHnalpwGVBvT1aqweajSrXv1qR4KQIOoTEGhL0c7wWFwBO3xySbJqEQgzX7LpVWJrgzC1hNfJHCUn4fCNdyaRdhW2IrZ0uE0e%2FyVtg8q4D2qukbRnNB5r7AMgLOqgR0kEIo9xHawiI6e4xH82Iyu4unX0jDz35i9BjqkAT%2B3uENnyhFgDORVdKZmoKZsO1pSg2D%2Fkdw2UqaAonqhP%2B4Ymzk6sVKGjQESZ37h%2B%2BAw33PGGnJz6pLciJKcobcPl%2F9SqL7aCr1N69WAMHp6l2NnLEnXuSvTTrIz2YbApdKZzDa9Jn4fy4ApMBvtQm2SPZ%2BADNfo3y4lSvCtROl%2BCVr6ZCeZ2e%2B5xW4OIzM1BSqk819N2A8IFdDuZUJT%2FTpiqzog&X-Amz-Signature=7288959465c912648cd8701783a0139d2e2f4d6c1b85962a812522a6a1b1d1ac&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTZOKQCA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCJ0IhXihQ38M6XIFfwKbIvuECC4Bx1haKPKkm2tFSWcQIhAPnaPyEStZX9Z8sHRS%2BEOau1WvY1dd%2F%2BNBhHsidMPHqvKv8DCHkQABoMNjM3NDIzMTgzODA1Igwx9fJDCplNjRQWoKwq3AN74TxDgtF%2FANFaOiHJt8vnLLp%2F5SNwMqDvwcMxWBherBX23zuCz%2FcNzF1BTXJpQsh0QJKzt2MDgNDUp4lYZLZ1ZGjydvANNxaFomV9DZM8f6ENQcAYc0Rfckum9Fmraqmi5v65gGsFtfLFYfTuA%2FBIQoH7I5yCQDmJdKkgCanqZtogNszkjUMHQtSjvC6oAtFig1tDav2udIbp5eJZvNXhTbc7NcQS2xd8fDc1RziAi4u5mXCDTvFq7qVNYr8saXFMprbF0D7sZizajbXFQiO1O6nS9hqmGGwx4zJA2h8OFmNA%2FrKme%2BweNmZGx59Z0%2F8inLokBF5S2PvZV4Cq4vDJtrEzNuf5Ge8E15zEenbDSr2Joc3ifgI7WhhTft023k%2FVNbm%2B2l%2FYJiT4LgHNUB9APl4QrXgxbHhidzMdFmKFPVGHpHzTQmLMdDhvhdKBMM9dMaTujc%2Fxwp2a8Jk1km8c6CizAKW%2BHvM1bxjdao8x0xjpUckf0DVIRTx7%2FU%2Bcy53yHtznis4AbarMxCNRd6d1urwEY5f3Q4%2F69cqqMXTlxb39YmJV5tbgEyRSfwXDEbnXYFf4KXdNDhpyclTIWDXzA6bAcDZGyVxrUHQHB%2FKauJoL9CRmhRpjXu6cYTD735i9BjqkAWeZHSerUweL3yGD5dPt1zbeCkkEGRP3ubftMusL%2B%2BFdIWW1uNN%2BTu8qRilBxFal9gR01pfsVTrJWUPlUW4tnBsdATMn9Vs%2B6v6cGEXPGmzvsS08b1iiVoQFUyPbdyNisb5KnG6gZEhq7ygrm1BqaBr54ccIoxtYCVJ0Xi7TkrDn%2Ba0rV3VHjOdJtOLUkVIBO1jOfxuG9pHiw7jVTGFUsa2YQqjQ&X-Amz-Signature=b84b179b66c34574524a21d96af4d981350f1bbcd757df49ba6256ea44554cd4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=7a6308bd2305e0e9a868db4f1586a2e43f5ee8feb59f53b4bb9eab429612083c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=2e242c18a0a24270503e2473004a337a3c24c5315847deb86078c57b9a8c8297&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GSOBSRC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDOnxcGOZrFutye15u%2FlIDToIsvRJigVqyYcE%2FLNkt%2FawIgfpmhLR8WoYj5nc2UD52ks8XCzTdXrOgeJusrocY057Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDDw%2BqvFQpcbRlHxkQSrcA4Cs4NTJ7LYR6oNDPxXkQC3cL2EdrJZuQQ7CPudM7wwRyE5Z41hPlznV6pPQHTAU0lLgfuUj3lISHJXURD7DunHqnwz2VZJz1uQrt5UrOYpjy%2B%2FVGeimw%2B9rGgvExpSaVH7zBkbxbNy7AjLQSEI3z1r8IMR73nNXsXHF60BAMFHxWt%2BOlW5HSyfhPFd46%2F09Hl%2FN5mKZxkzKHNYI1t0zDARKHFKRoTU%2BM29SLTsH3OrQNV6%2FCBNk3Fnu6rkiuljsxt6TMEkxNS8SACcXhKofDHEYXBbJ2OLmheX75TwrjoFF8EXKhyeCcvxuM3ajcUkjInAiwZXPEStODkb0qoXuR%2BgQrPHEj2u3Bf1q5weRh%2F7MnGhxzleIUiJzpls%2BYttrwgsMqiBvAvYlVmT4YqdrAn4OBnBpExZsY5eSd1qt7ASj32HmD6gntlsj8LXwgjugrSQspU9m7dhGe7HeAbrvARqi6J6CIX2q31cr7Jd8p%2F3Ml5Okh0G5Un1cAHp0hFfdZw0jvr9FMbPL%2FB2Q53wLHUT%2BLKXg2Qk1%2B%2FhbKc7SPGejmJ3msP4EEIpyqvjuzD2wxeJDV0Zx8Ey8zXL5je0YyE0OzxZqKjkFnj3QAFycikitnG%2Bf8my7iqIF3MckMKzgmL0GOqUBQVBm60hRhyVHXjsr0A%2BBEbDvDnBsTiAEr7W5Wb%2BZxjU%2BjxjKDD4xzqdb6SZU2MGNyIXWJ%2BWCM4Z8D4g3MTOvOjnzqUZbl2NGMOLdxB4qpgzIuCHtEKP%2BdqeVD%2BRwn746RkppnyizQL5L7rfpJUZpvIucLAn%2FfF1ck1SiCE4n8TyZJUIy9nsA8BVygCckLojeLupEhIMtMZ0ncO5ngXvj%2BC4dpiL3&X-Amz-Signature=0e134b433245e55585094fe33b615bd9ed10e551f5702ea21eea7fbf03ac4e80&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RWVJGOF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIGmiHiL3%2FnoI1av94ftyRN9PWEAgvBXZAaa8u%2BKTJnApAiEA%2BtdwAE4JAzvtf95sU9zz9xtHCv4Qpbq9M4j50u1%2B2psq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDGVqfp4AiCMT4BbXjyrcAzA27ii4XgbjovBHd5xUU0qzZJ2qKClN4a8LEH90rgaJUkSn%2FHR%2BAEuPqv7PbkNmd7oGGj2Yqlcd66vDoOrAz6zM2GceeI7YJ7Fvx6FQj3OqVid7N7V59dj8cHctp9GHw4Dp4Z0vD3vVSg4BtMQEb7yM1E74h5u%2BXr%2B5J%2BsqOouTlxIV40r0K7Vd6ohW7MQ2NIoPIST4s7V5nupujatzv0%2F1avFtFAn2puRZODVJL2qxfagw4ADGFZqFzRf6xmGg5MC4WthTFj6zxs5xvbBfX8pnrlYTLNpg%2F4Zt%2FK2p3LR99Nqvc%2Fd147F93CCUpNaJjb%2BpPU%2FEFci81RZ5NWukahHlWRq%2FeEFvnoEPZ3bLW1Za%2BQ94DHynLOkIUZj6DrbODEdy1vAxQToqgsWHLt5F9Q%2FgxO1sypa15bR1xn9MHrTnOlTajkf811BTLDeLh0qUBGb%2FVcMKJkQIm99USqVWAnTbkmS4nUcgLtkITXINE9v1XXCqSWZURBpBcmnKEVUfw0lrWd27noVdqcuImqIddwUVgx3CE%2Ffho%2FC3dOIahdndDKKS%2BpXTSRstpGDWT2NF%2FAGAUmU76GYVXhJjLY5TNBr%2FnSEJFEH3QPccGZSXN1MpK0V2NXIdcrirJEAzMLDgmL0GOqUBAS9pmZIbNfOg9enhBlwsvnvg%2B9bb65VrYp2pgNSI%2Bl9R%2BYU4Tc5W2g03zEXoL4Ic0besuZmfT2xnor%2FB%2FYF0sScOmCFm6snM37uZXjGMmM5lqhYbBu02IYhQx8%2FjQi9XBZxdYpXNpz3xBCYVaJu6swGEoS4rQqq%2FmL%2FD9HliLas0JxoxMh8ClLIZ7ZoBrC0hkzJ%2BRhbf1Assje%2BcCCSxU0MSTRWG&X-Amz-Signature=5529c7ace403a5cceaf8af9e53209d9a2b95398f83bfa36e8edd72e48ee76569&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLS2PPGJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCvlwtE88trX8zi%2BLcgwz0Dt1sxS6awEXApucDLAjmEuQIgOsQR9RYNiZ3vTf0s%2F6exl9P5xGzTCWCFJ8bAMKSEfrAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDFU7dhN6Mj1HhRBXPircA7GyuWqThR6IczBOsrqwTnu9X5R20bkOor7pm2DSDjZFDwex5F3MN%2BE3DNTYyvHHh00g55dtdjpN%2FFX8Uz2sihfoXyxWLtniE8QNt7s4kSHBhW%2BRHhxj5QnL3gNjYqUzPGF99F3rZMhokj8YMqptMC2%2FoLfBxNAvIC4srenkiJkLNrqjcHrWO0qCaZbY6UAYbIW6O6x7TI4b8Ro4cUPjRzpRfRMrgqzwUUD30ZUFvaAk3XoQFc8bzpSTdC3YuykLZu9bSah31enNaHzRzQV3DQLIsjFM0FFhaw7z490JqVy5JVfkWF3EiWQnSWD5rUJydkhe15Q2U9dXeO%2BoRHFDWoQjYBj4Dn3bRkPBnZUVxoagr8iFnEyUx1Dntu0jiVrkhIhyhZWZuTAH492CinktklOpeGDW%2Bs%2BM9pog0H78cht9M95RO%2BTk1ZJwA2hxE4NYhzVAVb4HrImsXJ%2BythYaNnEHoHDN9ZaYC1fI9M7bTHGh1B7mPWxzdTsR9S01WhEiZcEsMIsGi0FZrQGSVk5QKfa4lEZio5tRNpVYahkugDDKAhML9VED0sLvyopJY0I0dKOqtNKCqg5gs5xVXVRvdEPA0NgUpTfNDHiYS8EOpwSvDnhYJoC48sqsMdiPMM3gmL0GOqUBrdad9RDm5fmuFhQpCsBPVdJ91F9XOVZsvof0AkMu0dnwaWgDgerlOehcO4k31v7SdmnBcvM2EDPnkXKe4dLS%2FKRj8FFNdqe31COs8qKhlca4xwRWxBP4c6%2F3vbRWNUo8sfqbmlXEkqOKLgxz%2B%2BiRcnmfTW%2BF5CvmH654rj7jEb1RBCthMGqTMWjW%2BMjp5odb7YiQAlMQ3wPvzckEjvb5%2BZx8n2Kd&X-Amz-Signature=f9121afa5687b8a07048335f34425accd4c7cf608b51daec6aac74b54c5cb73f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD55MUQI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCxUz6R3%2BhuNAjPZnqFcRRVcsgj%2Fe5P%2Bv2T%2F0xz8g2R7wIgW48KJIL84prWo2icEZ6KwOXoLk0loqHPPQgA3i44Ndsq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDK6aLdpfSjy%2BHVlSuyrcA3oXDWPxAb9VI82bUdt7Yyi9p4cBxCn2jmAuAf9bYWo0UVLIak6yB7x%2Bx6ZpqTqV%2FxbA7wX8nOR1zMrWfMRB%2FZRqAuamL2pnjjEp3mrCZkxzQQLqP105K7DEWg%2BQas7%2BlLDy4jWpa5bdOOJH7MZZM8bcbmE%2BvMdH0oSjJUmAMivgUx3u2FrYyd6GyjHFvLAoB18SN%2F1WFw21IpaZytYWzoiVoGGp73LxYukJcSbn1UtqbefvvpCxcj155ixzK%2FqQQSssDmGoWmbJie40SGKVkBu6D2Si9pdfVnRzkJxeNrXSmwD1I1QUXnsTtFn3tUalM68CxdoKcQkOlzvAlQz4oQD8iJFgib3TrZlrN1ZaHYjvK8znSyosl47wJP%2BBD1FUCNJpaxdzwvA0dp5Iu3QzEr646t0sfP6dWJ4pPSGndb0mU2Rc%2Fm7vJt2u1AXIYxATAVK8ZRp9EkkfaZdYd2bgLU4MXDrqWYDi2ZMvmBaxtQkRKEecuMud57vjY4NLuN43hJDyJdcrsA%2B%2BRJnzF%2BeJHprx1HBjNj3DYu7ku1jX9pF30VrQxQ6HpEimKxXbiBQugJkr99qUBGlnx6ClmxCxjuDcj9FL3RoqK88n5SF2TJ60tv3M72vfPQcyyrOfMOXgmL0GOqUBOz5cXU5aXzzI2NMoeDFfEWVLGS5NpOORvpfVHMd2o6IGxJRdzqkJhUa1zQRzJLJS6C%2BwlQTjDdJrmKuL88elAzh8JTwIeYjzFgkL%2FX%2F%2FmTjxlTB7kf9SVItm5u%2BZxDLnueUl1T%2BXw2kFAAP00pB7GMpHlZK8sMAnTNoD4og%2Bn3q0eB9PXa31%2BJQQ9lW%2BUEx1m7n8kdeN9u95wEMRf%2BjRljJSRRFV&X-Amz-Signature=75c9ee07e6c132a2fa171bd888320d5ecc021137a5439a6eb0c63d142b6a87eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7TIJ7R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCVd%2Bq2S6qZCB6aQzRarU88Vs3raw9VRTFCEVbC3EDsMwIhAKAtMMewG9D0SyStW6Um5J7hws3dgCFdfQ1RSjOBkzhhKv8DCHkQABoMNjM3NDIzMTgzODA1IgwskpvqFjq7bLzVXmYq3AP7A%2BV07MNG69N6aINGWpUZyqbwwu%2B6uPoK0ZI3FXCKQ1YL280cs5ilubCI%2FlOtYAkrjyq%2FdElWUUE9qMhGE0ClJ2XY2%2FuztGKbEFovqPFy1uXL29D6OXW2zHVMrirdH%2Br6uPlnreBYk59S5Yn1IIVb3rFOUmYoQya0LkPndzGgrc50zmgChU9orV1CRWE4bPa2M72Vbha6QGN3S12YLZ4GmkHrgquHA6ud7hWRCFv7sohVDJCHgaydqrJhXhpVE4hNjn1oR07W7RFuhW3x%2FfW7cJXziKPmxYWG50nQquY36Ex16hCbxPdXzkMR2Qh%2FaTbMuBp7Ut2frAlAWbFauSozFNaIu6VkP%2BrjlCn1AVgaBYjTNciOB72%2BWxw5wRAgioiQjRpaEHRRWgTNcT4cAJWpMxvJ3UGjqim%2FM7ssSNqkSRVbYAdPGwcl9nOI5SoiJRC7V8yqvZxNjsFe%2BRZnPd6cUmNFOdEoxj1D%2B2IVmCZyfeVc08XTz56kNdaGWN4msPcWEfXBJBbHT32pLrVaE1KG2g%2BhXiZvTHas7mP0fZKhqrbe%2BE9V3TlW866djgdhZOPcThHzIAy2NfMKV9bwgof3LqMnZIrcP%2Bion1jFJMCnwerCORcH7b3m23iCmjDI4Ji9BjqkAX0IG73b6SCJ4E0cY4XGs%2FStnxDirc2rTLHCa6cnPNfveukaiYOP2lXDi8YgsbOR0gROqfkEcCe96af8ggRJgy6%2BXydWUe3Eu4s9Q5HpmuIPvKEmTm6V6LlpVBe2bY7ZSui3IkFngz7XrGUJ3ZiU5SXuRe6pDup9Jyxkh1Qrvuw7JB%2Fkb7V8kmGqCMhk%2FvKXhCmbRc4usDpGjXAbCHM%2BMh%2FBYciV&X-Amz-Signature=085e412325a1929270e0ff90d8c58d5d305af640483a71e4d3d189b2fa82b9a0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7TIJ7R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCVd%2Bq2S6qZCB6aQzRarU88Vs3raw9VRTFCEVbC3EDsMwIhAKAtMMewG9D0SyStW6Um5J7hws3dgCFdfQ1RSjOBkzhhKv8DCHkQABoMNjM3NDIzMTgzODA1IgwskpvqFjq7bLzVXmYq3AP7A%2BV07MNG69N6aINGWpUZyqbwwu%2B6uPoK0ZI3FXCKQ1YL280cs5ilubCI%2FlOtYAkrjyq%2FdElWUUE9qMhGE0ClJ2XY2%2FuztGKbEFovqPFy1uXL29D6OXW2zHVMrirdH%2Br6uPlnreBYk59S5Yn1IIVb3rFOUmYoQya0LkPndzGgrc50zmgChU9orV1CRWE4bPa2M72Vbha6QGN3S12YLZ4GmkHrgquHA6ud7hWRCFv7sohVDJCHgaydqrJhXhpVE4hNjn1oR07W7RFuhW3x%2FfW7cJXziKPmxYWG50nQquY36Ex16hCbxPdXzkMR2Qh%2FaTbMuBp7Ut2frAlAWbFauSozFNaIu6VkP%2BrjlCn1AVgaBYjTNciOB72%2BWxw5wRAgioiQjRpaEHRRWgTNcT4cAJWpMxvJ3UGjqim%2FM7ssSNqkSRVbYAdPGwcl9nOI5SoiJRC7V8yqvZxNjsFe%2BRZnPd6cUmNFOdEoxj1D%2B2IVmCZyfeVc08XTz56kNdaGWN4msPcWEfXBJBbHT32pLrVaE1KG2g%2BhXiZvTHas7mP0fZKhqrbe%2BE9V3TlW866djgdhZOPcThHzIAy2NfMKV9bwgof3LqMnZIrcP%2Bion1jFJMCnwerCORcH7b3m23iCmjDI4Ji9BjqkAX0IG73b6SCJ4E0cY4XGs%2FStnxDirc2rTLHCa6cnPNfveukaiYOP2lXDi8YgsbOR0gROqfkEcCe96af8ggRJgy6%2BXydWUe3Eu4s9Q5HpmuIPvKEmTm6V6LlpVBe2bY7ZSui3IkFngz7XrGUJ3ZiU5SXuRe6pDup9Jyxkh1Qrvuw7JB%2Fkb7V8kmGqCMhk%2FvKXhCmbRc4usDpGjXAbCHM%2BMh%2FBYciV&X-Amz-Signature=817c71a4d1dbb7df1482500450325f693f3d2dbd1471b596d88f6dc0aeac9e51&X-Amz-SignedHeaders=host&x-id=GetObject)

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
