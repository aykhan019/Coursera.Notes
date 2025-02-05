

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667QTQUCO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIER8c2e2kodTMekhUfwIoTAtKLxZ38JHEawag7xhK7sKAiAKVOg5ro9jrWAOgMnkOBNPs3UhFYxE6k3ojZ0pHDvaOyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM6bStUY976h9iIlu5KtwDsRaZUQLpO0HW4yMd%2BbmrjVqTXai0xhOwJ%2FqSpcqzW3ZLaToE6mjUuv4gHM3x%2FFUYNSPHutmXDlsNWOfFRzqHDHfHamh%2FpD0mTSmP%2BEN6PCgDeLHadO4shHp99WpA8kqd3t5Tc5Jn0Ng7%2FWxB%2BM4fkO%2F%2Bdws72u4ZWxjoUPGHKEp0SXBuS6VEv18qLZdgxp92OEYH3ejmDaitCmpk2mYyyOTaoBIyFH7GYpyVAwsxKzOfHTTdarXpmmqH1G1yeebND9eEgSXNIgjbzt6v4ySki2YOGexzJr41XCE%2F8t48vBXBnuAWDNJ13xHKHEUB%2BddN385Glt%2FXdLJwT1qyLqfbTBTRsHGzU9aBbs1SgmTfvpBjDrr6rXHD9SGsRud3keDrCR6%2FJVBMHK586MJ8Sjqs9bHOF%2FJGe%2FHif7wefcJmMwU3Vz3dATcDcdE6e%2B8xetbiQgEqT1YZVl8FJSW%2B%2FVpdnhuLsFnZHLSQMqW7Q01WrRekY9bbLZp591RrVlnX%2FwX2mo0KYGYR1m5cSO7Dk2q004uVqKrw9kI3FDrRpQNgvTlo7uWDfAmDjXYIxeaSh1AK6PHc%2BESdpsm7H7or12Ha9uvNr%2FScVF8%2B%2B2KUxbQBAOgRrbNyfSMo%2FJDkO4Iwk82KvQY6pgEp62deIBGiBZ4BO641wcXgCnm5OaXdfw4Q1A4IfqCAESg%2BIPCMjMzCblXVfePXJ4NZDOd7M4TI%2FM6SfUHbd9U64oGPtD7wyDIrL%2Blygi4NrRC7Am6F%2FqgOhhTrmbxhO67KgYzoHj3iMi6UrTAfciU8xGBlahtWKA7f4RvzyA3hUBdO2h7UqH7G%2F5itR28vbhBN%2BGB2abEFjbFjRH2NjqtVXQbPz%2FRb&X-Amz-Signature=7eabedc5b35b83809b12c307239169226df236e8c58c639aaf3436aecbe083a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667QTQUCO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIER8c2e2kodTMekhUfwIoTAtKLxZ38JHEawag7xhK7sKAiAKVOg5ro9jrWAOgMnkOBNPs3UhFYxE6k3ojZ0pHDvaOyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM6bStUY976h9iIlu5KtwDsRaZUQLpO0HW4yMd%2BbmrjVqTXai0xhOwJ%2FqSpcqzW3ZLaToE6mjUuv4gHM3x%2FFUYNSPHutmXDlsNWOfFRzqHDHfHamh%2FpD0mTSmP%2BEN6PCgDeLHadO4shHp99WpA8kqd3t5Tc5Jn0Ng7%2FWxB%2BM4fkO%2F%2Bdws72u4ZWxjoUPGHKEp0SXBuS6VEv18qLZdgxp92OEYH3ejmDaitCmpk2mYyyOTaoBIyFH7GYpyVAwsxKzOfHTTdarXpmmqH1G1yeebND9eEgSXNIgjbzt6v4ySki2YOGexzJr41XCE%2F8t48vBXBnuAWDNJ13xHKHEUB%2BddN385Glt%2FXdLJwT1qyLqfbTBTRsHGzU9aBbs1SgmTfvpBjDrr6rXHD9SGsRud3keDrCR6%2FJVBMHK586MJ8Sjqs9bHOF%2FJGe%2FHif7wefcJmMwU3Vz3dATcDcdE6e%2B8xetbiQgEqT1YZVl8FJSW%2B%2FVpdnhuLsFnZHLSQMqW7Q01WrRekY9bbLZp591RrVlnX%2FwX2mo0KYGYR1m5cSO7Dk2q004uVqKrw9kI3FDrRpQNgvTlo7uWDfAmDjXYIxeaSh1AK6PHc%2BESdpsm7H7or12Ha9uvNr%2FScVF8%2B%2B2KUxbQBAOgRrbNyfSMo%2FJDkO4Iwk82KvQY6pgEp62deIBGiBZ4BO641wcXgCnm5OaXdfw4Q1A4IfqCAESg%2BIPCMjMzCblXVfePXJ4NZDOd7M4TI%2FM6SfUHbd9U64oGPtD7wyDIrL%2Blygi4NrRC7Am6F%2FqgOhhTrmbxhO67KgYzoHj3iMi6UrTAfciU8xGBlahtWKA7f4RvzyA3hUBdO2h7UqH7G%2F5itR28vbhBN%2BGB2abEFjbFjRH2NjqtVXQbPz%2FRb&X-Amz-Signature=496e6abedda0d33d64ba1e5797e701a2b77b5814dfbc431c42378529b6ee9c19&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667QTQUCO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIER8c2e2kodTMekhUfwIoTAtKLxZ38JHEawag7xhK7sKAiAKVOg5ro9jrWAOgMnkOBNPs3UhFYxE6k3ojZ0pHDvaOyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM6bStUY976h9iIlu5KtwDsRaZUQLpO0HW4yMd%2BbmrjVqTXai0xhOwJ%2FqSpcqzW3ZLaToE6mjUuv4gHM3x%2FFUYNSPHutmXDlsNWOfFRzqHDHfHamh%2FpD0mTSmP%2BEN6PCgDeLHadO4shHp99WpA8kqd3t5Tc5Jn0Ng7%2FWxB%2BM4fkO%2F%2Bdws72u4ZWxjoUPGHKEp0SXBuS6VEv18qLZdgxp92OEYH3ejmDaitCmpk2mYyyOTaoBIyFH7GYpyVAwsxKzOfHTTdarXpmmqH1G1yeebND9eEgSXNIgjbzt6v4ySki2YOGexzJr41XCE%2F8t48vBXBnuAWDNJ13xHKHEUB%2BddN385Glt%2FXdLJwT1qyLqfbTBTRsHGzU9aBbs1SgmTfvpBjDrr6rXHD9SGsRud3keDrCR6%2FJVBMHK586MJ8Sjqs9bHOF%2FJGe%2FHif7wefcJmMwU3Vz3dATcDcdE6e%2B8xetbiQgEqT1YZVl8FJSW%2B%2FVpdnhuLsFnZHLSQMqW7Q01WrRekY9bbLZp591RrVlnX%2FwX2mo0KYGYR1m5cSO7Dk2q004uVqKrw9kI3FDrRpQNgvTlo7uWDfAmDjXYIxeaSh1AK6PHc%2BESdpsm7H7or12Ha9uvNr%2FScVF8%2B%2B2KUxbQBAOgRrbNyfSMo%2FJDkO4Iwk82KvQY6pgEp62deIBGiBZ4BO641wcXgCnm5OaXdfw4Q1A4IfqCAESg%2BIPCMjMzCblXVfePXJ4NZDOd7M4TI%2FM6SfUHbd9U64oGPtD7wyDIrL%2Blygi4NrRC7Am6F%2FqgOhhTrmbxhO67KgYzoHj3iMi6UrTAfciU8xGBlahtWKA7f4RvzyA3hUBdO2h7UqH7G%2F5itR28vbhBN%2BGB2abEFjbFjRH2NjqtVXQbPz%2FRb&X-Amz-Signature=a1a7b306388ceb8858e077e455bc14544553493041d71891202e413541b384bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2Q45FFZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCArX%2BnV4K%2BO3StkRmoeYnNiGMkjHxI2JxQYBdm998PMwIhALjhjCxxN80ihr6gmqdO3Ao0jh11iDLAIPjnyVNQYHNMKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BhfFJM5EabYrR0EMq3AMS06GG17OnsaDEg%2BeI55nafLseGNfaGuYs2wFKmUZGIfs1G%2F%2B8KsFf9of2%2BvbQ8ECFZi31oIaCf1n1PQA%2FdSy6HqcT4FftNKFDKQ%2BTTA8L6NuK7h01btfIBBjkvm4TYK47zCBr3JXkjIbKGJjHK9eYaImN1Cj8wG8ph%2B87NRpaDBjN7uTBUpg0zOGvyy3%2BtxGQJ7oZladpy417x%2Fb4FFebnudlllWkRXcWYDcVQ1h1kAzilS6TxfKz3r35C81d5k4cBVPi9oVsBWBtfLb%2FfaDpqkFMJc0EGNVGpeyLh6TrBnhBAgKbQAEX698a1%2Fj4oX00yPZoBJWcyrYIeDaxf%2FW0CleEkD4fVOXhLSyP5xSIbcRR59dZtaj59Rps2mtUziVLlhX%2B9up%2B4hpTRoSmvXfI7LI8%2FiCa0KMyz%2F6Rwiv8imsfKzmFEDXykO1GnTGVSkl35%2F%2F4NLkEzMdyon8x6eshX82qFIRoZuSyWsp2nsNMJnMjgvXZ5BxCZMmi3Jw3wF1ZBEj5zJ1JDUOTB8CwQJmVHuT7r%2BkSPKlVK%2F7WvlTAyMc914jmZjMWU1JWF5NcslPv8RCb6o52IRJSTP97SUsquOklGMMo1Qnldcf1F2iIdGrz5gIprsYNxAlTOjC9zYq9BjqkAVAr%2FmYXKnW9nH%2F24XkyNFFpQF1j8jTB1Rc68zyW2whvzfYyfDyMxUk6QHfiVsyAroAIDyWeWZnq4Abn85uS2mLI5wZ%2BNG9hQNUkcza7nCPDFw89d3AHjho7WnwZBrkWFxUOGnhRJUiLDo7ygxoAhzjUB1hueBja79KoykZ3Ha0LxX05CB00ytnzWXT1%2FNdALtfjrJyrtxfnv4ByngimmE0VFdiu&X-Amz-Signature=0b40e7226e789290cbc7282bf79bd2874e2be9dae141d50e7ba7a0ebda813bfb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2Q45FFZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCArX%2BnV4K%2BO3StkRmoeYnNiGMkjHxI2JxQYBdm998PMwIhALjhjCxxN80ihr6gmqdO3Ao0jh11iDLAIPjnyVNQYHNMKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BhfFJM5EabYrR0EMq3AMS06GG17OnsaDEg%2BeI55nafLseGNfaGuYs2wFKmUZGIfs1G%2F%2B8KsFf9of2%2BvbQ8ECFZi31oIaCf1n1PQA%2FdSy6HqcT4FftNKFDKQ%2BTTA8L6NuK7h01btfIBBjkvm4TYK47zCBr3JXkjIbKGJjHK9eYaImN1Cj8wG8ph%2B87NRpaDBjN7uTBUpg0zOGvyy3%2BtxGQJ7oZladpy417x%2Fb4FFebnudlllWkRXcWYDcVQ1h1kAzilS6TxfKz3r35C81d5k4cBVPi9oVsBWBtfLb%2FfaDpqkFMJc0EGNVGpeyLh6TrBnhBAgKbQAEX698a1%2Fj4oX00yPZoBJWcyrYIeDaxf%2FW0CleEkD4fVOXhLSyP5xSIbcRR59dZtaj59Rps2mtUziVLlhX%2B9up%2B4hpTRoSmvXfI7LI8%2FiCa0KMyz%2F6Rwiv8imsfKzmFEDXykO1GnTGVSkl35%2F%2F4NLkEzMdyon8x6eshX82qFIRoZuSyWsp2nsNMJnMjgvXZ5BxCZMmi3Jw3wF1ZBEj5zJ1JDUOTB8CwQJmVHuT7r%2BkSPKlVK%2F7WvlTAyMc914jmZjMWU1JWF5NcslPv8RCb6o52IRJSTP97SUsquOklGMMo1Qnldcf1F2iIdGrz5gIprsYNxAlTOjC9zYq9BjqkAVAr%2FmYXKnW9nH%2F24XkyNFFpQF1j8jTB1Rc68zyW2whvzfYyfDyMxUk6QHfiVsyAroAIDyWeWZnq4Abn85uS2mLI5wZ%2BNG9hQNUkcza7nCPDFw89d3AHjho7WnwZBrkWFxUOGnhRJUiLDo7ygxoAhzjUB1hueBja79KoykZ3Ha0LxX05CB00ytnzWXT1%2FNdALtfjrJyrtxfnv4ByngimmE0VFdiu&X-Amz-Signature=e7dbd00edebcc02217e5a7105adc3fcf1f5306d4e772e36ae158955f2d4d350a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2Q45FFZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCArX%2BnV4K%2BO3StkRmoeYnNiGMkjHxI2JxQYBdm998PMwIhALjhjCxxN80ihr6gmqdO3Ao0jh11iDLAIPjnyVNQYHNMKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BhfFJM5EabYrR0EMq3AMS06GG17OnsaDEg%2BeI55nafLseGNfaGuYs2wFKmUZGIfs1G%2F%2B8KsFf9of2%2BvbQ8ECFZi31oIaCf1n1PQA%2FdSy6HqcT4FftNKFDKQ%2BTTA8L6NuK7h01btfIBBjkvm4TYK47zCBr3JXkjIbKGJjHK9eYaImN1Cj8wG8ph%2B87NRpaDBjN7uTBUpg0zOGvyy3%2BtxGQJ7oZladpy417x%2Fb4FFebnudlllWkRXcWYDcVQ1h1kAzilS6TxfKz3r35C81d5k4cBVPi9oVsBWBtfLb%2FfaDpqkFMJc0EGNVGpeyLh6TrBnhBAgKbQAEX698a1%2Fj4oX00yPZoBJWcyrYIeDaxf%2FW0CleEkD4fVOXhLSyP5xSIbcRR59dZtaj59Rps2mtUziVLlhX%2B9up%2B4hpTRoSmvXfI7LI8%2FiCa0KMyz%2F6Rwiv8imsfKzmFEDXykO1GnTGVSkl35%2F%2F4NLkEzMdyon8x6eshX82qFIRoZuSyWsp2nsNMJnMjgvXZ5BxCZMmi3Jw3wF1ZBEj5zJ1JDUOTB8CwQJmVHuT7r%2BkSPKlVK%2F7WvlTAyMc914jmZjMWU1JWF5NcslPv8RCb6o52IRJSTP97SUsquOklGMMo1Qnldcf1F2iIdGrz5gIprsYNxAlTOjC9zYq9BjqkAVAr%2FmYXKnW9nH%2F24XkyNFFpQF1j8jTB1Rc68zyW2whvzfYyfDyMxUk6QHfiVsyAroAIDyWeWZnq4Abn85uS2mLI5wZ%2BNG9hQNUkcza7nCPDFw89d3AHjho7WnwZBrkWFxUOGnhRJUiLDo7ygxoAhzjUB1hueBja79KoykZ3Ha0LxX05CB00ytnzWXT1%2FNdALtfjrJyrtxfnv4ByngimmE0VFdiu&X-Amz-Signature=edbf7104b6d9de678629456fe7b8b92dda354def83853863200cdd8f85e20e0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2Q45FFZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCArX%2BnV4K%2BO3StkRmoeYnNiGMkjHxI2JxQYBdm998PMwIhALjhjCxxN80ihr6gmqdO3Ao0jh11iDLAIPjnyVNQYHNMKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BhfFJM5EabYrR0EMq3AMS06GG17OnsaDEg%2BeI55nafLseGNfaGuYs2wFKmUZGIfs1G%2F%2B8KsFf9of2%2BvbQ8ECFZi31oIaCf1n1PQA%2FdSy6HqcT4FftNKFDKQ%2BTTA8L6NuK7h01btfIBBjkvm4TYK47zCBr3JXkjIbKGJjHK9eYaImN1Cj8wG8ph%2B87NRpaDBjN7uTBUpg0zOGvyy3%2BtxGQJ7oZladpy417x%2Fb4FFebnudlllWkRXcWYDcVQ1h1kAzilS6TxfKz3r35C81d5k4cBVPi9oVsBWBtfLb%2FfaDpqkFMJc0EGNVGpeyLh6TrBnhBAgKbQAEX698a1%2Fj4oX00yPZoBJWcyrYIeDaxf%2FW0CleEkD4fVOXhLSyP5xSIbcRR59dZtaj59Rps2mtUziVLlhX%2B9up%2B4hpTRoSmvXfI7LI8%2FiCa0KMyz%2F6Rwiv8imsfKzmFEDXykO1GnTGVSkl35%2F%2F4NLkEzMdyon8x6eshX82qFIRoZuSyWsp2nsNMJnMjgvXZ5BxCZMmi3Jw3wF1ZBEj5zJ1JDUOTB8CwQJmVHuT7r%2BkSPKlVK%2F7WvlTAyMc914jmZjMWU1JWF5NcslPv8RCb6o52IRJSTP97SUsquOklGMMo1Qnldcf1F2iIdGrz5gIprsYNxAlTOjC9zYq9BjqkAVAr%2FmYXKnW9nH%2F24XkyNFFpQF1j8jTB1Rc68zyW2whvzfYyfDyMxUk6QHfiVsyAroAIDyWeWZnq4Abn85uS2mLI5wZ%2BNG9hQNUkcza7nCPDFw89d3AHjho7WnwZBrkWFxUOGnhRJUiLDo7ygxoAhzjUB1hueBja79KoykZ3Ha0LxX05CB00ytnzWXT1%2FNdALtfjrJyrtxfnv4ByngimmE0VFdiu&X-Amz-Signature=46f6f820d75c03c8b08bd9fad54154c3028ed5e8092bceab213bc6402080fdea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2Q45FFZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCArX%2BnV4K%2BO3StkRmoeYnNiGMkjHxI2JxQYBdm998PMwIhALjhjCxxN80ihr6gmqdO3Ao0jh11iDLAIPjnyVNQYHNMKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BhfFJM5EabYrR0EMq3AMS06GG17OnsaDEg%2BeI55nafLseGNfaGuYs2wFKmUZGIfs1G%2F%2B8KsFf9of2%2BvbQ8ECFZi31oIaCf1n1PQA%2FdSy6HqcT4FftNKFDKQ%2BTTA8L6NuK7h01btfIBBjkvm4TYK47zCBr3JXkjIbKGJjHK9eYaImN1Cj8wG8ph%2B87NRpaDBjN7uTBUpg0zOGvyy3%2BtxGQJ7oZladpy417x%2Fb4FFebnudlllWkRXcWYDcVQ1h1kAzilS6TxfKz3r35C81d5k4cBVPi9oVsBWBtfLb%2FfaDpqkFMJc0EGNVGpeyLh6TrBnhBAgKbQAEX698a1%2Fj4oX00yPZoBJWcyrYIeDaxf%2FW0CleEkD4fVOXhLSyP5xSIbcRR59dZtaj59Rps2mtUziVLlhX%2B9up%2B4hpTRoSmvXfI7LI8%2FiCa0KMyz%2F6Rwiv8imsfKzmFEDXykO1GnTGVSkl35%2F%2F4NLkEzMdyon8x6eshX82qFIRoZuSyWsp2nsNMJnMjgvXZ5BxCZMmi3Jw3wF1ZBEj5zJ1JDUOTB8CwQJmVHuT7r%2BkSPKlVK%2F7WvlTAyMc914jmZjMWU1JWF5NcslPv8RCb6o52IRJSTP97SUsquOklGMMo1Qnldcf1F2iIdGrz5gIprsYNxAlTOjC9zYq9BjqkAVAr%2FmYXKnW9nH%2F24XkyNFFpQF1j8jTB1Rc68zyW2whvzfYyfDyMxUk6QHfiVsyAroAIDyWeWZnq4Abn85uS2mLI5wZ%2BNG9hQNUkcza7nCPDFw89d3AHjho7WnwZBrkWFxUOGnhRJUiLDo7ygxoAhzjUB1hueBja79KoykZ3Ha0LxX05CB00ytnzWXT1%2FNdALtfjrJyrtxfnv4ByngimmE0VFdiu&X-Amz-Signature=bf4a99b9a756bc87575b3a9f8bfd163de8a4143648a1b7cd93a1758bb72c0220&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2Q45FFZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCArX%2BnV4K%2BO3StkRmoeYnNiGMkjHxI2JxQYBdm998PMwIhALjhjCxxN80ihr6gmqdO3Ao0jh11iDLAIPjnyVNQYHNMKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BhfFJM5EabYrR0EMq3AMS06GG17OnsaDEg%2BeI55nafLseGNfaGuYs2wFKmUZGIfs1G%2F%2B8KsFf9of2%2BvbQ8ECFZi31oIaCf1n1PQA%2FdSy6HqcT4FftNKFDKQ%2BTTA8L6NuK7h01btfIBBjkvm4TYK47zCBr3JXkjIbKGJjHK9eYaImN1Cj8wG8ph%2B87NRpaDBjN7uTBUpg0zOGvyy3%2BtxGQJ7oZladpy417x%2Fb4FFebnudlllWkRXcWYDcVQ1h1kAzilS6TxfKz3r35C81d5k4cBVPi9oVsBWBtfLb%2FfaDpqkFMJc0EGNVGpeyLh6TrBnhBAgKbQAEX698a1%2Fj4oX00yPZoBJWcyrYIeDaxf%2FW0CleEkD4fVOXhLSyP5xSIbcRR59dZtaj59Rps2mtUziVLlhX%2B9up%2B4hpTRoSmvXfI7LI8%2FiCa0KMyz%2F6Rwiv8imsfKzmFEDXykO1GnTGVSkl35%2F%2F4NLkEzMdyon8x6eshX82qFIRoZuSyWsp2nsNMJnMjgvXZ5BxCZMmi3Jw3wF1ZBEj5zJ1JDUOTB8CwQJmVHuT7r%2BkSPKlVK%2F7WvlTAyMc914jmZjMWU1JWF5NcslPv8RCb6o52IRJSTP97SUsquOklGMMo1Qnldcf1F2iIdGrz5gIprsYNxAlTOjC9zYq9BjqkAVAr%2FmYXKnW9nH%2F24XkyNFFpQF1j8jTB1Rc68zyW2whvzfYyfDyMxUk6QHfiVsyAroAIDyWeWZnq4Abn85uS2mLI5wZ%2BNG9hQNUkcza7nCPDFw89d3AHjho7WnwZBrkWFxUOGnhRJUiLDo7ygxoAhzjUB1hueBja79KoykZ3Ha0LxX05CB00ytnzWXT1%2FNdALtfjrJyrtxfnv4ByngimmE0VFdiu&X-Amz-Signature=2fe0d721777564162896585f80dc27f4ae80f66014cb7d4f3617652f3f4e0906&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXJI2QBM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDu69jfSRwL3e2CmO%2BOOOtQFq1%2BiIW6eLMHRkkc%2FQYoNAIgcgn0SpL1guM2ljZLZuhtKMr5MVGGvHLbQJVNo%2BsS4BUq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCKM8vB2rs05INShsyrcA6tOl476tT2uDYzU3krSUHc7a2zTkmtCT5NemGaMlF6CO381lHJlIau3CJlmEwLVsSvh%2F6nS5CTjZvw%2B%2BaUjipn4YiQ6Evm3PUvcUW58i6OZEhKQn8tHeT6mnQI7rIK2G2zMkUfoGoptSk%2FxgsTDWKOTikI6G5eThwlYNLxkP8wTRnVeGPCTpLlrz1WTtMxnJzkP3PO7x833Lk8xlFU7Bz9HO4IFt%2FY5nOTlZju8ZSh0GIso4I55vkzrLR6LxJlJKVHkXidB8H5i3xR8xvFQV2WapIpMLvM9NafSXPqfFLNJP%2B4YVO%2B6Z9qq4gLTL%2Bt35Ag8bagt3RsxgytUjiXkATlXrGyktePq7LDIh5Q6QjpokvsaVaCVhCwModT8UkBM3ft1tICl2EB3xCY1N%2FLga0R5WUUTAAv%2BziNBSKlh9s6kivXAaokQ3o7C%2FZkGLB38HdTAkOE%2F9zMmk0jRe5YM5g7gttNxARPwIY%2BqqFk1RLPQMblt7wL0%2BQCrrVKTjYGCiY%2Bwp9ZviD4gr06ZkfeZ31cUH6lAW6Zw2NM0Wpwlje3InekvryVAt1GVQJm0LzMe4gTq9CQ9jRxL1irfegtabgFTAKTSTZzEdSnueZvp6HQaVZfDd%2BFhkufrgaw6MPHMir0GOqUBaG8SDGWoiQ0%2Fzw%2FBZPqoVFnCrkTNx5lynoNCaLVrPVyBs1pKnCxFNPT3Rb6bnl6TEc0J74ZNPRLmGGbHdpASENkczfKxyTbbpjzYPjEl6rejwb68%2BWQzxlub4yBxW4zrU5EK5wCresmxf3hGv885aWMplkB%2FtW9YAD4NsNVxUDU1f%2Fypoytmtqha1JsMr3F87yJ20xeJVaUh6nwdjK4XiBUoIhRc&X-Amz-Signature=e82dc6549a383ecb83715ffc84569912d097c079d989252c572f4be4da71c489&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667U6YFVYY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBWkzemoNq6XRe41vE5qEUWaf%2Fxi%2FgdaXuCl25DQ%2BdCBAiEA%2FoOONd2ZDHWHCNH2Yu1mC%2Bl8cS7BFIG7zvLOkggmK%2BYq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDA66gzP7uDYb0RZm2CrcA6x33jHBUrAERc36QrTO5cozxZjyCwPlv%2BteTCean2C0J6txGmySxaWOovzU6uJ2yRyiz%2BFCRHAImDce8xQt2Kc%2FiIGuEvDnvRATeWwUFYPAmryjiwGC2ZcEkVxTz1lS3O7SNX%2BKJCiO%2Bdi%2BvgTZ2%2BjBqfbjM7TeviqI6FyJlLFZOciMcbXXVgZdrCJVwRgjgm6jKDKVTOqKr2TcQ%2F%2Be0wzmFFVWXqJQ64DIZN8Lzhos2G52iH%2BhkU4Cxrq02dj9j0hvrgxp60yZwYZIYAZiZtwEm7qwGZKd3kkQ0TAaDOfkXo97tBJaFJYt4u5V%2FLM%2Byfhtp0lzBFwQ9LqIRMo8%2B1qwJ09RHaeydJfTXFaLWCMfaXcTdGlymRRJfKKA0HaderpCiHLLOtZr54goSKh0j1Dtk5cT2ENGi7MrWGXW3ICRel13m2sHFR3pf6e%2FstJWNvB%2FQNNZwawvREvX2MR%2B5QDz%2FsucFmWsEaCMzmelki5IzulroC5HEzdMEHBaBKs2NeV5zVpY3cJ2tuAAaUhMRQ3QDqToOyMqwnMq6LlDwxJU%2FVj770n7PQ9q9%2Feh5myw9Pplr9cb76II%2FOmF7q6%2BA02iBp9KlIqmnDMqaQs0%2FCyxKCAcFuhu3sRvHvpZMNDNir0GOqUBSsHBbQwO6%2FqZo5DNQ1lswO%2BSKLHA%2F4VXdZIlzpvDe%2FuG3PGLrfSIPizVwcVcfynTDsXHEJqLP65xj8tPnmAWH4xp2hibyGZx2cRo5Q5CRcNWafjiFiIpyPvGVbn%2BPIJiYCL5MrZXete6iI7ExUIuVui4xwof%2BjOje5xSgJpC0zMZDU9iK2THgCMWI3RjmDdbiLPD2fAz%2BkI0VDc0uF%2BYUiI6hvF2&X-Amz-Signature=4e500668edd47bf6415c3174d9a74d6c592673207ccc0aec110b624d563a03c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2Q45FFZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCArX%2BnV4K%2BO3StkRmoeYnNiGMkjHxI2JxQYBdm998PMwIhALjhjCxxN80ihr6gmqdO3Ao0jh11iDLAIPjnyVNQYHNMKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BhfFJM5EabYrR0EMq3AMS06GG17OnsaDEg%2BeI55nafLseGNfaGuYs2wFKmUZGIfs1G%2F%2B8KsFf9of2%2BvbQ8ECFZi31oIaCf1n1PQA%2FdSy6HqcT4FftNKFDKQ%2BTTA8L6NuK7h01btfIBBjkvm4TYK47zCBr3JXkjIbKGJjHK9eYaImN1Cj8wG8ph%2B87NRpaDBjN7uTBUpg0zOGvyy3%2BtxGQJ7oZladpy417x%2Fb4FFebnudlllWkRXcWYDcVQ1h1kAzilS6TxfKz3r35C81d5k4cBVPi9oVsBWBtfLb%2FfaDpqkFMJc0EGNVGpeyLh6TrBnhBAgKbQAEX698a1%2Fj4oX00yPZoBJWcyrYIeDaxf%2FW0CleEkD4fVOXhLSyP5xSIbcRR59dZtaj59Rps2mtUziVLlhX%2B9up%2B4hpTRoSmvXfI7LI8%2FiCa0KMyz%2F6Rwiv8imsfKzmFEDXykO1GnTGVSkl35%2F%2F4NLkEzMdyon8x6eshX82qFIRoZuSyWsp2nsNMJnMjgvXZ5BxCZMmi3Jw3wF1ZBEj5zJ1JDUOTB8CwQJmVHuT7r%2BkSPKlVK%2F7WvlTAyMc914jmZjMWU1JWF5NcslPv8RCb6o52IRJSTP97SUsquOklGMMo1Qnldcf1F2iIdGrz5gIprsYNxAlTOjC9zYq9BjqkAVAr%2FmYXKnW9nH%2F24XkyNFFpQF1j8jTB1Rc68zyW2whvzfYyfDyMxUk6QHfiVsyAroAIDyWeWZnq4Abn85uS2mLI5wZ%2BNG9hQNUkcza7nCPDFw89d3AHjho7WnwZBrkWFxUOGnhRJUiLDo7ygxoAhzjUB1hueBja79KoykZ3Ha0LxX05CB00ytnzWXT1%2FNdALtfjrJyrtxfnv4ByngimmE0VFdiu&X-Amz-Signature=d8ccd757aafa61b08444d7505cbc83135866482af3289119edece75996e992cd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2Q45FFZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCArX%2BnV4K%2BO3StkRmoeYnNiGMkjHxI2JxQYBdm998PMwIhALjhjCxxN80ihr6gmqdO3Ao0jh11iDLAIPjnyVNQYHNMKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BhfFJM5EabYrR0EMq3AMS06GG17OnsaDEg%2BeI55nafLseGNfaGuYs2wFKmUZGIfs1G%2F%2B8KsFf9of2%2BvbQ8ECFZi31oIaCf1n1PQA%2FdSy6HqcT4FftNKFDKQ%2BTTA8L6NuK7h01btfIBBjkvm4TYK47zCBr3JXkjIbKGJjHK9eYaImN1Cj8wG8ph%2B87NRpaDBjN7uTBUpg0zOGvyy3%2BtxGQJ7oZladpy417x%2Fb4FFebnudlllWkRXcWYDcVQ1h1kAzilS6TxfKz3r35C81d5k4cBVPi9oVsBWBtfLb%2FfaDpqkFMJc0EGNVGpeyLh6TrBnhBAgKbQAEX698a1%2Fj4oX00yPZoBJWcyrYIeDaxf%2FW0CleEkD4fVOXhLSyP5xSIbcRR59dZtaj59Rps2mtUziVLlhX%2B9up%2B4hpTRoSmvXfI7LI8%2FiCa0KMyz%2F6Rwiv8imsfKzmFEDXykO1GnTGVSkl35%2F%2F4NLkEzMdyon8x6eshX82qFIRoZuSyWsp2nsNMJnMjgvXZ5BxCZMmi3Jw3wF1ZBEj5zJ1JDUOTB8CwQJmVHuT7r%2BkSPKlVK%2F7WvlTAyMc914jmZjMWU1JWF5NcslPv8RCb6o52IRJSTP97SUsquOklGMMo1Qnldcf1F2iIdGrz5gIprsYNxAlTOjC9zYq9BjqkAVAr%2FmYXKnW9nH%2F24XkyNFFpQF1j8jTB1Rc68zyW2whvzfYyfDyMxUk6QHfiVsyAroAIDyWeWZnq4Abn85uS2mLI5wZ%2BNG9hQNUkcza7nCPDFw89d3AHjho7WnwZBrkWFxUOGnhRJUiLDo7ygxoAhzjUB1hueBja79KoykZ3Ha0LxX05CB00ytnzWXT1%2FNdALtfjrJyrtxfnv4ByngimmE0VFdiu&X-Amz-Signature=03cc75cda613e072c70dc7ed896506f0c000371a47f754c30269173fb6c370b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2Q45FFZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCArX%2BnV4K%2BO3StkRmoeYnNiGMkjHxI2JxQYBdm998PMwIhALjhjCxxN80ihr6gmqdO3Ao0jh11iDLAIPjnyVNQYHNMKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BhfFJM5EabYrR0EMq3AMS06GG17OnsaDEg%2BeI55nafLseGNfaGuYs2wFKmUZGIfs1G%2F%2B8KsFf9of2%2BvbQ8ECFZi31oIaCf1n1PQA%2FdSy6HqcT4FftNKFDKQ%2BTTA8L6NuK7h01btfIBBjkvm4TYK47zCBr3JXkjIbKGJjHK9eYaImN1Cj8wG8ph%2B87NRpaDBjN7uTBUpg0zOGvyy3%2BtxGQJ7oZladpy417x%2Fb4FFebnudlllWkRXcWYDcVQ1h1kAzilS6TxfKz3r35C81d5k4cBVPi9oVsBWBtfLb%2FfaDpqkFMJc0EGNVGpeyLh6TrBnhBAgKbQAEX698a1%2Fj4oX00yPZoBJWcyrYIeDaxf%2FW0CleEkD4fVOXhLSyP5xSIbcRR59dZtaj59Rps2mtUziVLlhX%2B9up%2B4hpTRoSmvXfI7LI8%2FiCa0KMyz%2F6Rwiv8imsfKzmFEDXykO1GnTGVSkl35%2F%2F4NLkEzMdyon8x6eshX82qFIRoZuSyWsp2nsNMJnMjgvXZ5BxCZMmi3Jw3wF1ZBEj5zJ1JDUOTB8CwQJmVHuT7r%2BkSPKlVK%2F7WvlTAyMc914jmZjMWU1JWF5NcslPv8RCb6o52IRJSTP97SUsquOklGMMo1Qnldcf1F2iIdGrz5gIprsYNxAlTOjC9zYq9BjqkAVAr%2FmYXKnW9nH%2F24XkyNFFpQF1j8jTB1Rc68zyW2whvzfYyfDyMxUk6QHfiVsyAroAIDyWeWZnq4Abn85uS2mLI5wZ%2BNG9hQNUkcza7nCPDFw89d3AHjho7WnwZBrkWFxUOGnhRJUiLDo7ygxoAhzjUB1hueBja79KoykZ3Ha0LxX05CB00ytnzWXT1%2FNdALtfjrJyrtxfnv4ByngimmE0VFdiu&X-Amz-Signature=75d0003d6f9c319bc19b9b43b4e62ed3fbe09deb082effe3c96355e7e006e1cb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6LC2E42%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDECRxqha4eygH0Pd7pG3p%2F5dVJ2r1ZcHPSXjqyS45ywAIhAMA9Xi9KuNrGNbWaZNrbgw4ViYry9am2QRIIlVdhYMrlKv8DCDkQABoMNjM3NDIzMTgzODA1Igx1ozvXYJY4A948ZEAq3APXNzzyLg8v5L39HNuTv44FBdmHf8cv086DGdV8DxPliLSLWJ5OzFwDVo3K3RbyeWsaCERQ2sRRDRg%2FCKL9%2F6iQjRTUcZMW0UcPL%2Fv11UOSXXXVEe%2FnS4x3bdivOoR9k3%2F9eG1JeB3j1wNPmNht92ih8C0nAmwqQr%2BSZYZBz%2FI0LXE7gBULvvuVdlJIBY2jqzdWSvCSmy2VLaCY1NZPLBEVAsdxZDtKErmO0gq%2BjRI%2FWMwV2jpTFXvllKY%2BydcElFribz%2F2nw6NhX4ro5%2FixGTACWeO4o8sI6ATKOZUgtsjDZn930swYaNB6%2BFltaRnmLWEx8CUdq5xyiAUW8%2Bbw5rRik6bBb4GZwr6UJQQtMZWtzg5FmxXmy4VbPig3TqtvA%2FBaN0O9njFPruKim2dz1Eb2DZdue7FQ1JrkHWAyFeb7qDVjiU9NCCeiEqVpeD7DjnNYOOFiX8ElTo0MW%2Bs7vnl0uscHSrdWZozmrDdRgv0eAR87VyFUXBaHVvbJo4Dr4jl2OTdz8RBbM6KXQm2wuZbnK%2BcNLYbMOofxDoD3XovC0X8ifTtODqIh2FmUE973Ne3Pdy9TtdpVgh1jpx5l32qa4Ci5ETRhqtYGMx2oUDALAhu7EvUujvA%2BzoFazDlzIq9BjqkAUV29oRVWpC7Hr2kxIQ0aTTIpXMJ3GVN2Ka1R5iVdy%2BfJy9AUCtOwxWmudWCtH2kq%2FpM9NHGHd167tIJRM7Zj7vTjJYEl8F4ECW5rcNq0eQHRWyzdbzTrQSNpz7oy%2ByPb5iLsatdCIFNEuXjPIhTsDLcWL%2FU17F56BoqFarMG40xaW%2B5vucdjU%2BKAtymkd4HyInXEHyfCXLDIm1Kb8Rdr%2B1j8yGY&X-Amz-Signature=7c29fbb7525026b65fc98ed893b4d271dcc5272b9522bc9eef9cc20a691695fd&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUUPBIVR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCaRfBGvKOhxGmq2pUrIZ%2F2MSz9Ug6HECXTPvcmnz9tewIhAMcIB5Sau7IiuLVjL0sFQ%2BuzJHY5UTXv8SJud9H%2FYeBSKv8DCDkQABoMNjM3NDIzMTgzODA1IgzIS0uDgtboj%2BxUMKsq3APkpmURpbURnTr6QH%2FJKCgDLfhpER%2Bea64t748r5btA3cvYHbqB8ysHnHc9St%2BZORJJRqW1Ruho%2BLe%2Fxx1wbDN2UH%2BtiffVixaT0zAzJcGOqwERMc406ifY8eMeddJ0lch3n0FFy%2BFVsbM1eOAVTjmdY4vBEGj0Shi3KV2zTZodkcALwihjIC%2Bru0VM%2FyDpHR%2F4qxeSD8xCbkxLPumwd6V85C6lxYASaZSFdzh%2BZc2tmn94VoPvp%2BNg7%2FFHPXCaOtX35Rll%2FtFwZo1x4hsCn6kUMUxKjDq%2BI8LSOXHOJmq5CLI0da6UP4qA0YfBoG6yavhdQGAQIY2E7pjnMgwX1qhtni9wZcYARqhIS67ZN7OlnLWND8nScGW%2F6k%2FIAOhhjXi%2BIrHLnQlgsFL1LaqKDnEfHrL38xtmCg6KR8TpyGhd3de5LJyqHRiHwy3Qe1zdLfEvq3T1tA9e3MHPcaZvbDvQs1pUCkzMIF4KAtSB6uN4riTEHtHO0f10kdHgbZi5drsaiO%2Bkui3KO9UlkCm1hBaYsFSAM2q%2Bo4SiwgmHBZCkf2XIKjTKCpIdgVI4dBBqVyEX9coRxwMdTtK3PF%2BZUMBUZJTAU2AbWelueMyOTuFmAMxvHDc7PUSMqpcvuDCZzYq9BjqkAZwiYGqBljwH%2BZZlL6vPJKV0an2Yo9pcyYyHaCZuzCP8Qa9ifPwkmjIdGnGCoxALNX2%2FY%2FFDDfYw4WXcjPE9EWdiLXW5a8YDPPXSdi6O4JeWf9b8rOVli1zikaPfZXuz5HW1DWWbGb62UFFdDiJpaW8bc9eOMjehOMiVgcnlAORF%2BlCYqGJ9R9kF99Lat90n3gwU8KuXtNQOV5cH5R7iXc837mS%2B&X-Amz-Signature=4cf3e84ddcf8172e33209ae26d0d6aa80068defc2fbf35a5e09bc1ac3c79404d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XK5QBFP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCC4cm4M5P9IIQOs0vv%2F%2F6C5GJP4B8whMmvCH5A1uc%2FugIgUF20gVC%2B7MwOXt45BgVnf3541HqrEX54XLkLqfs1IS4q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDFgqK1XaNAOWh7fLmyrcA9BntvgupSpxEFcx53K10G%2BuuVvYniJsx%2BFVvVGlZZz17TQ%2BwPMbdPP6sAFd6JXBD8rtskSjaR6KI6PtROhnkQjIoPGPNV1lYjdjT3jree%2BLTNZOR%2Beqq6BFWd6e4%2FUDO3o1j9Vlflw59KfFfLzwigWkM%2FPmS7Us%2FZW8K6AngmFoIv%2BieuKNpO2SIZ4nUDhcJbCH9WPJ%2FlA0WQNBRSbSFr9DGCfyaCWOrHxklKsW4Bk1ulbrpVH0W6qpuSw%2BJk4FLfY5Zi5sVDreruTo%2FoS47P7yQqR3PilMUhRn2%2B0GJeaukgB7ChC8DaYnWX9vmlJl5EnwyxJU0S8TdQBE5PQOw9jHc9ZTVo4xnA9HChGwjxGYLcr1ea8ji64017EbyTUgEgVieCdNEFs2ZFevXQbJwBHOIagJ%2B6T6mGVr%2FUYVTcPvMgv7isaBLpq4YtBCMHE%2B18l8chjJLjSmbafzzeuTX6A5kDeuuFYfQPFBEGJyAm%2FMsr2I5LkSHvbxetffHUTiRZWrl7NK9tMuxHTT8w67SgqGcb8msbuRkD8ADfYoRp2ferUEa%2BNfsLf3xSHyvJx9rGW%2FNB2qGezTOkU0UfufqXUtTx035b8pZ8lB334xK%2FqRtCBrSJdIHWfIhtQVMK7Nir0GOqUBk7iQcRgH9VfMNzvQzLgCi17aDxEkb2vHkih85qLJNKdQ3Sbwn8Wvb%2FzOs%2ByO51IqVMjcZymd2%2BBltLXcGlwaRFKmcX6j89l6MO%2BepTrAzlZb4IWQndjvNAP4xTfJGJhpUe26byM0eTXIbleMMxONQZfMNQxHTY9MUmkG4E%2BnAlf%2FMibMcWrRv8nZD%2BbAv%2Fe6C9htUXokCVUgze03qcOxrs4pei8z&X-Amz-Signature=66bb05cee15e885b741ac9d6034b57ca53a26e28e8760efa066721b365401ccd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSMW2BTE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCaChLQbEKlNHh5OaqYTcQV53yU1vrl8f34qrYEIV0GeAIhAMSQ%2F5Rb1x4R%2BWSLUSXyAokPhXpEdsrLf9zh6t9XQan1Kv8DCDkQABoMNjM3NDIzMTgzODA1IgwslX44FPp841su2fMq3APfOtamO0hGo%2FSB7B0mfzPB9oQDCEnFSIV8cyR0KM8h7O4ZyEOw0Xk9SN2neOI9irUtEhBH%2F0DFzk9tmV52pP8FT8DoUZ1QdaSGyGBM68k66EnSDEZ%2BPzIFxnKdeE56%2BNI8A5Z2itCxVkWWU9gP0VD5UTVgIr%2BCk6HIJGE4DLCd8DfJp85UBs8zsui5%2FRsJed9yRhAipqHergTmEZ%2FOQ0Fpo%2Fx4Z4MaX4dT3iFuVlMjqT6eGDZt1BIyiq12HW3tubXzOafDivX50ydGw9NcgkETyy7x1mwC0g6l18r7%2BhAXXHBGUjPgqGqYbnNsmNpcSL30Nw4JHDOOHQsn%2Frbv9cJY1oBmOxPMRWIcVGoBhjTpStgy02BuY650ERcMkvHz2i2eY1IzQ%2BU3NaIyRO9P2SHzFGZuZyyoYnOLGnO3QwX15e9xmWmrZox3KhWB%2F%2BeP2TmaXk1lvbANQlXNune8BAW7rHiOIhjsvPu29%2B23vIoC2%2FPWXjHcsveZYF%2FFUhnKQvTNhHUuF7GX33ARBJixg%2FbVW9Ges5QluakQHZxRoDjmOb1%2FZ5JWp10%2FATb%2Fqvy%2FjT621U5b%2FSESrtuNO28LCwmdhmJ2HDXSUL0ZuQpMZqjeOaf9Fz0NVX2gCDPP3DDzzIq9BjqkAbqyfYt9yDxm2lTJxKriNnhGjuCuHL5bz0sO81OTsEcs5UfjpjYiUjm2Oc6HlOQ7R30CWVVEDx5yOejDpjfJxb094sEpVum5LZH9WX1f0gVni9JEIobFWEem0XpCLtkmqN1V4dj%2BDQM%2BtLGrTi2hGCBpSDgbEA%2Foghain9Izhy6wVIvaNNqZvjoYDJr7sbPsvb23tlG0MOZnIKJpF7hTVyz9m1J4&X-Amz-Signature=8659a0ba2e40c620c8fa49a3dc07105479ad486f05d24309e836415619e492f5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSMW2BTE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCaChLQbEKlNHh5OaqYTcQV53yU1vrl8f34qrYEIV0GeAIhAMSQ%2F5Rb1x4R%2BWSLUSXyAokPhXpEdsrLf9zh6t9XQan1Kv8DCDkQABoMNjM3NDIzMTgzODA1IgwslX44FPp841su2fMq3APfOtamO0hGo%2FSB7B0mfzPB9oQDCEnFSIV8cyR0KM8h7O4ZyEOw0Xk9SN2neOI9irUtEhBH%2F0DFzk9tmV52pP8FT8DoUZ1QdaSGyGBM68k66EnSDEZ%2BPzIFxnKdeE56%2BNI8A5Z2itCxVkWWU9gP0VD5UTVgIr%2BCk6HIJGE4DLCd8DfJp85UBs8zsui5%2FRsJed9yRhAipqHergTmEZ%2FOQ0Fpo%2Fx4Z4MaX4dT3iFuVlMjqT6eGDZt1BIyiq12HW3tubXzOafDivX50ydGw9NcgkETyy7x1mwC0g6l18r7%2BhAXXHBGUjPgqGqYbnNsmNpcSL30Nw4JHDOOHQsn%2Frbv9cJY1oBmOxPMRWIcVGoBhjTpStgy02BuY650ERcMkvHz2i2eY1IzQ%2BU3NaIyRO9P2SHzFGZuZyyoYnOLGnO3QwX15e9xmWmrZox3KhWB%2F%2BeP2TmaXk1lvbANQlXNune8BAW7rHiOIhjsvPu29%2B23vIoC2%2FPWXjHcsveZYF%2FFUhnKQvTNhHUuF7GX33ARBJixg%2FbVW9Ges5QluakQHZxRoDjmOb1%2FZ5JWp10%2FATb%2Fqvy%2FjT621U5b%2FSESrtuNO28LCwmdhmJ2HDXSUL0ZuQpMZqjeOaf9Fz0NVX2gCDPP3DDzzIq9BjqkAbqyfYt9yDxm2lTJxKriNnhGjuCuHL5bz0sO81OTsEcs5UfjpjYiUjm2Oc6HlOQ7R30CWVVEDx5yOejDpjfJxb094sEpVum5LZH9WX1f0gVni9JEIobFWEem0XpCLtkmqN1V4dj%2BDQM%2BtLGrTi2hGCBpSDgbEA%2Foghain9Izhy6wVIvaNNqZvjoYDJr7sbPsvb23tlG0MOZnIKJpF7hTVyz9m1J4&X-Amz-Signature=672c9950c61e1b84b5f730c04b49c2c67a30a5c8ecba791aa4f9e414acbdbbb6&X-Amz-SignedHeaders=host&x-id=GetObject)

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
