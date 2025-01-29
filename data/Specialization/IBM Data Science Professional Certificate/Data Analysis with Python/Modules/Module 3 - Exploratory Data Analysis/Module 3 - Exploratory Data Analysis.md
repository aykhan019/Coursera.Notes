

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662N4ZDJ75%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BhZPFpiCmfCzBB8pxCcJ3E31OLUKmq9%2BKfI1SaUO28gIhAOoCUZB4TSxLqJTfGLrDzoQ2ko05xfnEXqSkB%2BwrXbEFKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZP3uU5LCV3dLAIcwq3ANePD8bAzS%2B6zscUOghR5Kp%2BbNZswBwzSeQYE4im5H27ItDUAN%2BzjXl62a%2FlhcXiqbJTpunB8qG7TmTZE9D54AvG3fsvl9qiMFZFBWWVlys7Csyq16c4UD6heuHcP6fX2fAnzYv6GpdSXnqMYdGD4bU7JGqMd9m9b7A0ZbDTUVZ1RwjF2U6eOEi49TFjocY3FHv%2BdhpNZUJKDHeex1Lj3%2BkBeiVnKzaFPZK9n6%2FwDqh9R%2BPpnA5k8SzLeOxJRG0D%2BqWRQbxpEOxRRaP6%2BGnbeH3%2BG2eZ9ZYLHrQJ3sv9JfAiqe7tmWnkwsEhHNs2TiMLwRG0ljZaYPDPIzmqdF2%2BL8WlK8Z21gvMyQshTYf19igwOVXPJr33WggKtFLfczL1vd%2Bso726VrLwOGZvp6i3KYzO2XF300oayZ%2FHNFz7g9jQ%2Fe6rln24%2BOEK2IMP3ItIY2FzJ9IzzJSSNYXYBw35PiO8JkoQ9KbsNihhR8truRaZ8Nh%2BllQGZXKQfeKJzEc%2FMdENJ524OYOS7P2gttVMjgdLvnWH4IGfJinUCpSBJKVwoMLX%2B4eK9ml6j7cS8IBkS0%2BMms13QCfXfNlRsCeb1CGdkAmTOBDwx9%2BjTPgix8K89J4Xhdv99dOCz4pRTDtxeq8BjqkAUXFwMkhE7AFIZi0DFogMwc4B%2B6qJhFO6qGY0RWQi0H9Yxe0trZpS2Rch9hKH%2Fh5n3OeY1zBNHj2BwYWzEmM8HCWZa0VJiSjlXGNskuFce1LTpk6wu0QFO8Sm%2FH7Nrfaz2PH5Zm9I7DMZyS5yec5ksc%2FMXG0nmjQFejZy0RMm8AED7bX%2BZXnnJXHS5ahpZ7ySWO4z3S0dQ%2BRF1l9TBF6U6%2B4zz7u&X-Amz-Signature=b0cec0fcb3b4dfc3b5c4b81e7089a6c5792335b7119e68c9c8e1b7319149b8a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662N4ZDJ75%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BhZPFpiCmfCzBB8pxCcJ3E31OLUKmq9%2BKfI1SaUO28gIhAOoCUZB4TSxLqJTfGLrDzoQ2ko05xfnEXqSkB%2BwrXbEFKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZP3uU5LCV3dLAIcwq3ANePD8bAzS%2B6zscUOghR5Kp%2BbNZswBwzSeQYE4im5H27ItDUAN%2BzjXl62a%2FlhcXiqbJTpunB8qG7TmTZE9D54AvG3fsvl9qiMFZFBWWVlys7Csyq16c4UD6heuHcP6fX2fAnzYv6GpdSXnqMYdGD4bU7JGqMd9m9b7A0ZbDTUVZ1RwjF2U6eOEi49TFjocY3FHv%2BdhpNZUJKDHeex1Lj3%2BkBeiVnKzaFPZK9n6%2FwDqh9R%2BPpnA5k8SzLeOxJRG0D%2BqWRQbxpEOxRRaP6%2BGnbeH3%2BG2eZ9ZYLHrQJ3sv9JfAiqe7tmWnkwsEhHNs2TiMLwRG0ljZaYPDPIzmqdF2%2BL8WlK8Z21gvMyQshTYf19igwOVXPJr33WggKtFLfczL1vd%2Bso726VrLwOGZvp6i3KYzO2XF300oayZ%2FHNFz7g9jQ%2Fe6rln24%2BOEK2IMP3ItIY2FzJ9IzzJSSNYXYBw35PiO8JkoQ9KbsNihhR8truRaZ8Nh%2BllQGZXKQfeKJzEc%2FMdENJ524OYOS7P2gttVMjgdLvnWH4IGfJinUCpSBJKVwoMLX%2B4eK9ml6j7cS8IBkS0%2BMms13QCfXfNlRsCeb1CGdkAmTOBDwx9%2BjTPgix8K89J4Xhdv99dOCz4pRTDtxeq8BjqkAUXFwMkhE7AFIZi0DFogMwc4B%2B6qJhFO6qGY0RWQi0H9Yxe0trZpS2Rch9hKH%2Fh5n3OeY1zBNHj2BwYWzEmM8HCWZa0VJiSjlXGNskuFce1LTpk6wu0QFO8Sm%2FH7Nrfaz2PH5Zm9I7DMZyS5yec5ksc%2FMXG0nmjQFejZy0RMm8AED7bX%2BZXnnJXHS5ahpZ7ySWO4z3S0dQ%2BRF1l9TBF6U6%2B4zz7u&X-Amz-Signature=a233aac90e251b62ebe5e8e82361a9382bfa3d686fc7d4a9d7dc59edead7eb80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662N4ZDJ75%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BhZPFpiCmfCzBB8pxCcJ3E31OLUKmq9%2BKfI1SaUO28gIhAOoCUZB4TSxLqJTfGLrDzoQ2ko05xfnEXqSkB%2BwrXbEFKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZP3uU5LCV3dLAIcwq3ANePD8bAzS%2B6zscUOghR5Kp%2BbNZswBwzSeQYE4im5H27ItDUAN%2BzjXl62a%2FlhcXiqbJTpunB8qG7TmTZE9D54AvG3fsvl9qiMFZFBWWVlys7Csyq16c4UD6heuHcP6fX2fAnzYv6GpdSXnqMYdGD4bU7JGqMd9m9b7A0ZbDTUVZ1RwjF2U6eOEi49TFjocY3FHv%2BdhpNZUJKDHeex1Lj3%2BkBeiVnKzaFPZK9n6%2FwDqh9R%2BPpnA5k8SzLeOxJRG0D%2BqWRQbxpEOxRRaP6%2BGnbeH3%2BG2eZ9ZYLHrQJ3sv9JfAiqe7tmWnkwsEhHNs2TiMLwRG0ljZaYPDPIzmqdF2%2BL8WlK8Z21gvMyQshTYf19igwOVXPJr33WggKtFLfczL1vd%2Bso726VrLwOGZvp6i3KYzO2XF300oayZ%2FHNFz7g9jQ%2Fe6rln24%2BOEK2IMP3ItIY2FzJ9IzzJSSNYXYBw35PiO8JkoQ9KbsNihhR8truRaZ8Nh%2BllQGZXKQfeKJzEc%2FMdENJ524OYOS7P2gttVMjgdLvnWH4IGfJinUCpSBJKVwoMLX%2B4eK9ml6j7cS8IBkS0%2BMms13QCfXfNlRsCeb1CGdkAmTOBDwx9%2BjTPgix8K89J4Xhdv99dOCz4pRTDtxeq8BjqkAUXFwMkhE7AFIZi0DFogMwc4B%2B6qJhFO6qGY0RWQi0H9Yxe0trZpS2Rch9hKH%2Fh5n3OeY1zBNHj2BwYWzEmM8HCWZa0VJiSjlXGNskuFce1LTpk6wu0QFO8Sm%2FH7Nrfaz2PH5Zm9I7DMZyS5yec5ksc%2FMXG0nmjQFejZy0RMm8AED7bX%2BZXnnJXHS5ahpZ7ySWO4z3S0dQ%2BRF1l9TBF6U6%2B4zz7u&X-Amz-Signature=1d1e4c559e344702174912b77023bb987e5c52312d576aba075531acb09a92f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TKAEGWO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhx%2F33fUOwrWNnD69wFsk%2F%2BLg2cktCdFd4rvxZjlugOgIgIMLiBxqrv0qy1XePOPJ3YXkZoN0l1tsaMEt%2FqL4%2B0ioqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGYgxvg%2BG3PAJLV8CrcA8aTjoNSMB4C1npiW8dlW8jSuzTiBFUEeAwT%2FbZ5Cwk%2BPEj0kQQYVTcgmrWpjpxgPi%2FwxktC4qTPzZKcsjIl6v71GX6JR6k7KQW7bUBOdFt6UaFNCOK4kYrZ7BNw4EFsBC4f%2BX0JyMVbWf6YyrphuEQDg07IH3Qfjk0QwuVRLKJtAASKsjiijFEcGox6lebB3zJz6OM5O3ZT44PM1R1RIbnalqlLmayTPG%2FVdssqH72y5JSN3rKBXmBUBxoQTTQoB01SbjEbHprgIps1prTfJ%2BTZIXD8sTOHM%2BB7xIN55URR7v6Xw0j8Cspq6c34lPCPAwaMO%2Fa6s%2Bs3S5d9Zr%2FuduOv%2B0i0xtbgxtiKPRLyV85msQ00cN9ulB%2Fwy%2FVrMNy63EqIKwEiNFSzJPpkeU6hr9JKGyXKqb7B%2FbqE3yJixu8WkzqqzL47s%2FQlk0Xs%2BCY2j9e6pciT3j3hMd6b1dQYaagaWH1q7oxYW2nZ7fnBjRxLsGgNrWWnUVrk8mlvNoGHbN5gBkO5lnbhPYKxzaRP%2B28RQOjrBbq6%2B3tpx19qPWsf%2B1rXoJgRnCmzMC5ugk04t1OrInLASoiqciipmWcBd7kuRJccALAmbN7AkfYTVgvXU2SqrRq3dKn9RBYUMOrF6rwGOqUBmI8dK99utL76WQw%2BUsbnwZ32UYqWoxNpTSh8TvN5vphjX7nIy8lzlktkf01oz3kxoNGh4dkJYmp2GiBxM4pthxLgKFgoDr0HKf3SxCj1lNXUtFCK8y09OREl%2BPUooL8jC%2F0c7EmWDMskTeVOHSDMGM%2B6wJZFiVWf2c25lh71NPsTU%2BkqZCi1KplEKzPdMJ2oTo2aHU63j3eBzoPuftKwaCNIbfpl&X-Amz-Signature=f441e617b2dabd9cd217a283849c3ddd9fe811f0732382c9bd062e455f9d7984&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TKAEGWO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhx%2F33fUOwrWNnD69wFsk%2F%2BLg2cktCdFd4rvxZjlugOgIgIMLiBxqrv0qy1XePOPJ3YXkZoN0l1tsaMEt%2FqL4%2B0ioqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGYgxvg%2BG3PAJLV8CrcA8aTjoNSMB4C1npiW8dlW8jSuzTiBFUEeAwT%2FbZ5Cwk%2BPEj0kQQYVTcgmrWpjpxgPi%2FwxktC4qTPzZKcsjIl6v71GX6JR6k7KQW7bUBOdFt6UaFNCOK4kYrZ7BNw4EFsBC4f%2BX0JyMVbWf6YyrphuEQDg07IH3Qfjk0QwuVRLKJtAASKsjiijFEcGox6lebB3zJz6OM5O3ZT44PM1R1RIbnalqlLmayTPG%2FVdssqH72y5JSN3rKBXmBUBxoQTTQoB01SbjEbHprgIps1prTfJ%2BTZIXD8sTOHM%2BB7xIN55URR7v6Xw0j8Cspq6c34lPCPAwaMO%2Fa6s%2Bs3S5d9Zr%2FuduOv%2B0i0xtbgxtiKPRLyV85msQ00cN9ulB%2Fwy%2FVrMNy63EqIKwEiNFSzJPpkeU6hr9JKGyXKqb7B%2FbqE3yJixu8WkzqqzL47s%2FQlk0Xs%2BCY2j9e6pciT3j3hMd6b1dQYaagaWH1q7oxYW2nZ7fnBjRxLsGgNrWWnUVrk8mlvNoGHbN5gBkO5lnbhPYKxzaRP%2B28RQOjrBbq6%2B3tpx19qPWsf%2B1rXoJgRnCmzMC5ugk04t1OrInLASoiqciipmWcBd7kuRJccALAmbN7AkfYTVgvXU2SqrRq3dKn9RBYUMOrF6rwGOqUBmI8dK99utL76WQw%2BUsbnwZ32UYqWoxNpTSh8TvN5vphjX7nIy8lzlktkf01oz3kxoNGh4dkJYmp2GiBxM4pthxLgKFgoDr0HKf3SxCj1lNXUtFCK8y09OREl%2BPUooL8jC%2F0c7EmWDMskTeVOHSDMGM%2B6wJZFiVWf2c25lh71NPsTU%2BkqZCi1KplEKzPdMJ2oTo2aHU63j3eBzoPuftKwaCNIbfpl&X-Amz-Signature=8c736ad81018dc487417e030732ec49e3ca713a89e1440f2a6a7a8052d03965a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TKAEGWO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhx%2F33fUOwrWNnD69wFsk%2F%2BLg2cktCdFd4rvxZjlugOgIgIMLiBxqrv0qy1XePOPJ3YXkZoN0l1tsaMEt%2FqL4%2B0ioqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGYgxvg%2BG3PAJLV8CrcA8aTjoNSMB4C1npiW8dlW8jSuzTiBFUEeAwT%2FbZ5Cwk%2BPEj0kQQYVTcgmrWpjpxgPi%2FwxktC4qTPzZKcsjIl6v71GX6JR6k7KQW7bUBOdFt6UaFNCOK4kYrZ7BNw4EFsBC4f%2BX0JyMVbWf6YyrphuEQDg07IH3Qfjk0QwuVRLKJtAASKsjiijFEcGox6lebB3zJz6OM5O3ZT44PM1R1RIbnalqlLmayTPG%2FVdssqH72y5JSN3rKBXmBUBxoQTTQoB01SbjEbHprgIps1prTfJ%2BTZIXD8sTOHM%2BB7xIN55URR7v6Xw0j8Cspq6c34lPCPAwaMO%2Fa6s%2Bs3S5d9Zr%2FuduOv%2B0i0xtbgxtiKPRLyV85msQ00cN9ulB%2Fwy%2FVrMNy63EqIKwEiNFSzJPpkeU6hr9JKGyXKqb7B%2FbqE3yJixu8WkzqqzL47s%2FQlk0Xs%2BCY2j9e6pciT3j3hMd6b1dQYaagaWH1q7oxYW2nZ7fnBjRxLsGgNrWWnUVrk8mlvNoGHbN5gBkO5lnbhPYKxzaRP%2B28RQOjrBbq6%2B3tpx19qPWsf%2B1rXoJgRnCmzMC5ugk04t1OrInLASoiqciipmWcBd7kuRJccALAmbN7AkfYTVgvXU2SqrRq3dKn9RBYUMOrF6rwGOqUBmI8dK99utL76WQw%2BUsbnwZ32UYqWoxNpTSh8TvN5vphjX7nIy8lzlktkf01oz3kxoNGh4dkJYmp2GiBxM4pthxLgKFgoDr0HKf3SxCj1lNXUtFCK8y09OREl%2BPUooL8jC%2F0c7EmWDMskTeVOHSDMGM%2B6wJZFiVWf2c25lh71NPsTU%2BkqZCi1KplEKzPdMJ2oTo2aHU63j3eBzoPuftKwaCNIbfpl&X-Amz-Signature=663fccbc3e6bee5691a9a675038f8735ad247e5fe49e6e26965693b171843420&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TKAEGWO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhx%2F33fUOwrWNnD69wFsk%2F%2BLg2cktCdFd4rvxZjlugOgIgIMLiBxqrv0qy1XePOPJ3YXkZoN0l1tsaMEt%2FqL4%2B0ioqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGYgxvg%2BG3PAJLV8CrcA8aTjoNSMB4C1npiW8dlW8jSuzTiBFUEeAwT%2FbZ5Cwk%2BPEj0kQQYVTcgmrWpjpxgPi%2FwxktC4qTPzZKcsjIl6v71GX6JR6k7KQW7bUBOdFt6UaFNCOK4kYrZ7BNw4EFsBC4f%2BX0JyMVbWf6YyrphuEQDg07IH3Qfjk0QwuVRLKJtAASKsjiijFEcGox6lebB3zJz6OM5O3ZT44PM1R1RIbnalqlLmayTPG%2FVdssqH72y5JSN3rKBXmBUBxoQTTQoB01SbjEbHprgIps1prTfJ%2BTZIXD8sTOHM%2BB7xIN55URR7v6Xw0j8Cspq6c34lPCPAwaMO%2Fa6s%2Bs3S5d9Zr%2FuduOv%2B0i0xtbgxtiKPRLyV85msQ00cN9ulB%2Fwy%2FVrMNy63EqIKwEiNFSzJPpkeU6hr9JKGyXKqb7B%2FbqE3yJixu8WkzqqzL47s%2FQlk0Xs%2BCY2j9e6pciT3j3hMd6b1dQYaagaWH1q7oxYW2nZ7fnBjRxLsGgNrWWnUVrk8mlvNoGHbN5gBkO5lnbhPYKxzaRP%2B28RQOjrBbq6%2B3tpx19qPWsf%2B1rXoJgRnCmzMC5ugk04t1OrInLASoiqciipmWcBd7kuRJccALAmbN7AkfYTVgvXU2SqrRq3dKn9RBYUMOrF6rwGOqUBmI8dK99utL76WQw%2BUsbnwZ32UYqWoxNpTSh8TvN5vphjX7nIy8lzlktkf01oz3kxoNGh4dkJYmp2GiBxM4pthxLgKFgoDr0HKf3SxCj1lNXUtFCK8y09OREl%2BPUooL8jC%2F0c7EmWDMskTeVOHSDMGM%2B6wJZFiVWf2c25lh71NPsTU%2BkqZCi1KplEKzPdMJ2oTo2aHU63j3eBzoPuftKwaCNIbfpl&X-Amz-Signature=d02ce8b47e1b9fbe1b10298313aaf8e7db532c0a95156f12a8ba8cd28e09be6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TKAEGWO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhx%2F33fUOwrWNnD69wFsk%2F%2BLg2cktCdFd4rvxZjlugOgIgIMLiBxqrv0qy1XePOPJ3YXkZoN0l1tsaMEt%2FqL4%2B0ioqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGYgxvg%2BG3PAJLV8CrcA8aTjoNSMB4C1npiW8dlW8jSuzTiBFUEeAwT%2FbZ5Cwk%2BPEj0kQQYVTcgmrWpjpxgPi%2FwxktC4qTPzZKcsjIl6v71GX6JR6k7KQW7bUBOdFt6UaFNCOK4kYrZ7BNw4EFsBC4f%2BX0JyMVbWf6YyrphuEQDg07IH3Qfjk0QwuVRLKJtAASKsjiijFEcGox6lebB3zJz6OM5O3ZT44PM1R1RIbnalqlLmayTPG%2FVdssqH72y5JSN3rKBXmBUBxoQTTQoB01SbjEbHprgIps1prTfJ%2BTZIXD8sTOHM%2BB7xIN55URR7v6Xw0j8Cspq6c34lPCPAwaMO%2Fa6s%2Bs3S5d9Zr%2FuduOv%2B0i0xtbgxtiKPRLyV85msQ00cN9ulB%2Fwy%2FVrMNy63EqIKwEiNFSzJPpkeU6hr9JKGyXKqb7B%2FbqE3yJixu8WkzqqzL47s%2FQlk0Xs%2BCY2j9e6pciT3j3hMd6b1dQYaagaWH1q7oxYW2nZ7fnBjRxLsGgNrWWnUVrk8mlvNoGHbN5gBkO5lnbhPYKxzaRP%2B28RQOjrBbq6%2B3tpx19qPWsf%2B1rXoJgRnCmzMC5ugk04t1OrInLASoiqciipmWcBd7kuRJccALAmbN7AkfYTVgvXU2SqrRq3dKn9RBYUMOrF6rwGOqUBmI8dK99utL76WQw%2BUsbnwZ32UYqWoxNpTSh8TvN5vphjX7nIy8lzlktkf01oz3kxoNGh4dkJYmp2GiBxM4pthxLgKFgoDr0HKf3SxCj1lNXUtFCK8y09OREl%2BPUooL8jC%2F0c7EmWDMskTeVOHSDMGM%2B6wJZFiVWf2c25lh71NPsTU%2BkqZCi1KplEKzPdMJ2oTo2aHU63j3eBzoPuftKwaCNIbfpl&X-Amz-Signature=41da3e009e291e349f3cb06f1884e53ceb43217819121e71dacd0e3fdeb92f20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TKAEGWO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhx%2F33fUOwrWNnD69wFsk%2F%2BLg2cktCdFd4rvxZjlugOgIgIMLiBxqrv0qy1XePOPJ3YXkZoN0l1tsaMEt%2FqL4%2B0ioqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGYgxvg%2BG3PAJLV8CrcA8aTjoNSMB4C1npiW8dlW8jSuzTiBFUEeAwT%2FbZ5Cwk%2BPEj0kQQYVTcgmrWpjpxgPi%2FwxktC4qTPzZKcsjIl6v71GX6JR6k7KQW7bUBOdFt6UaFNCOK4kYrZ7BNw4EFsBC4f%2BX0JyMVbWf6YyrphuEQDg07IH3Qfjk0QwuVRLKJtAASKsjiijFEcGox6lebB3zJz6OM5O3ZT44PM1R1RIbnalqlLmayTPG%2FVdssqH72y5JSN3rKBXmBUBxoQTTQoB01SbjEbHprgIps1prTfJ%2BTZIXD8sTOHM%2BB7xIN55URR7v6Xw0j8Cspq6c34lPCPAwaMO%2Fa6s%2Bs3S5d9Zr%2FuduOv%2B0i0xtbgxtiKPRLyV85msQ00cN9ulB%2Fwy%2FVrMNy63EqIKwEiNFSzJPpkeU6hr9JKGyXKqb7B%2FbqE3yJixu8WkzqqzL47s%2FQlk0Xs%2BCY2j9e6pciT3j3hMd6b1dQYaagaWH1q7oxYW2nZ7fnBjRxLsGgNrWWnUVrk8mlvNoGHbN5gBkO5lnbhPYKxzaRP%2B28RQOjrBbq6%2B3tpx19qPWsf%2B1rXoJgRnCmzMC5ugk04t1OrInLASoiqciipmWcBd7kuRJccALAmbN7AkfYTVgvXU2SqrRq3dKn9RBYUMOrF6rwGOqUBmI8dK99utL76WQw%2BUsbnwZ32UYqWoxNpTSh8TvN5vphjX7nIy8lzlktkf01oz3kxoNGh4dkJYmp2GiBxM4pthxLgKFgoDr0HKf3SxCj1lNXUtFCK8y09OREl%2BPUooL8jC%2F0c7EmWDMskTeVOHSDMGM%2B6wJZFiVWf2c25lh71NPsTU%2BkqZCi1KplEKzPdMJ2oTo2aHU63j3eBzoPuftKwaCNIbfpl&X-Amz-Signature=d042561ec1188cddbb3b783e5b120becf11ef8c4ec4aee45bd729ed3b259aa65&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QCHYBTM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID8%2FfF7m9%2Bz3sgzwh4urulhvMeeQ%2BIRam0iJLQSCQR4qAiEA6FdDspjNgcKegTKgEl51KN3lzj9pZkmt8Y%2FIXX5uXs0qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMMJk8NpSzl0w%2BaJoSrcAwAzCN05wcJmTAxyXy72I8n7VQlp%2FCIOLNYnxNoKrGlQGVlIIRdYqbi%2BIeFDCaNfQw9ntYw4Gq3ihSMy4SK%2BIzSLJXLiz4mE9OqSprAw8H3tbKZnWf%2BQiy40Ow172IhKGUlU6XYd9TUlprPmMQGCOqXhcqOeaxGBirS3CcPr8PYH21MmGWtp5HIDMMxModM59T%2BA56kG7Mv463Pfy0exXa6TeRfWkmL7KCIDeDzfv5aJQWh1CEXZ05%2BPZqmVe7vzG6FtetsKcSI%2FXpbTjEAinpe4txlYgwhhOUMFdQeOj4Fx5FTyS7Ug4tOwuo0KMGsvk%2F49EOV3ekcUbcjuBcAa30tv0MA6HxutNy8WNOQ3n6kqBTPsIZx96FotLVauKcofwIWJC7D5sq%2BdZxekHGWWZRy7uEurra6%2Foija2NBMrMr7zG7pWGccait469B00BJ5%2B7JvVUG41fMqT1UMNeTIl%2BCtmsgycbpEYUoVlDlth9isg48y75WBzTVUdn%2FOUID2wjxnHeyH5Sn4QU2Wiq6R1uI53HCFu8l%2BUH4frT8wlVlBYP1xTqZvDY7oQ7HL1SjbSs3nmW0adfGeTIX1Mm%2BaUjyJajhy19WxqwNaJWefWj%2FZu2fVSmao2WevA3yiMNLF6rwGOqUBdpQZEOnJJZCrqPqm%2Fnn60DaLdFmbDa1yXom0F4KKzmNK%2BAwYpoGNnEFQonTinDbV5iihQFXLXp5kEbqWCwDGpOuE6Usy7cfJLIUdMQ%2BE8Dz4bb7%2F9WGdh5GWNBLTXE5JOFbjzuc2josrl7QGXHN0sg4EceMDOP4v8XGDuDXZO1HKlwepmuaXME5oDHX1zyyDA4Q8DDpKwLt6e%2B1u5Iapkk0Ru8uC&X-Amz-Signature=bf3bc64603c53c77f47b821a44ebbc57aef3eca4fe6ab71f13cb5f85a002f13b&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Y7P537O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuO4k3BnO5y63%2F5%2Fe0VIsxzJS4ivoOndmAyE92G8VxwgIgemHBiKB19Aea3EqUb0Objocjd0ViXw4I2VBXtN%2B45hAqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhC24opMN9tCTFWGCrcA%2BTPGc93wNOZjmd4USuEsNGyoFd%2F7gLJm3KLCLKsEkeeScr2JPkqOGyN0OZbL9U2vA7cJPI6qMkwwarESJXBlGLHd%2Fs8ZrbHaC9ItKWsKIz%2FB9n4ZKZAeKnWKtRJ60lsijrGBkhwHrf1fOFEGkIMctwbZr2udT11e919j1y5Gobfu%2B8MzaGZiXNodRIH4Q1xgFVNRsmyAhoTSiNIDS69iCuDpXiz3XBZLTvZSgsEDIWVEhlAMkZx87pmlJFrBXUWa4%2B5xzCNi1do09yX8FKiapNLoSiJuxqdv904v4Hk1hZmBVTno6a8P9%2BugkNb3C5M1SSJ5e9aDep5rB2ZfPx3eIhssPJuwWKFJKZYfNvWgmLjUyyzedahIs4WZU9ZdzD6%2BaPX6pi7pZViwfgadM72uC7OBKoV4C3oJNl6O2towhGG5dme3nRovTXRatcOzpFh0j5EKKbwwrYdpuQyJfZBpfQXlsQoDJjCcwAXeH4ygUtKZh5nYKppTmz4Es%2FEtja3Yt5353%2Bz6Qzbomsrdzpc00d0ZXV6kGP3cqJ4qE%2FU07%2BBW%2BKl082Ndhb965TH3lY%2Ba8xYdjXxbCVIOzqDIz1HCUh46EBazccGjit0LxvpLQJ%2FeOdpmPAdkq%2F%2BdDhUML%2FF6rwGOqUBwkHKxtx30SgrXYCcNMBKrfFsscx0WGfAJ1wcgz%2FGSdVzo%2FA6PKMezo845u5ci5S8MwPzB9495yBIZhGL5RnA9xnl65w5TCa%2BAx5LVLYaJVNQ2DSyfURk375AGJZhOI36jBn%2FhjQnvvZyagn395%2BX3BcKcf%2F6r3qFCcmLiPD80eAvnYfZptm5%2BBxu%2FIgJy9ljURXUc1kgkirUhpSWs%2BGxlER5EoQT&X-Amz-Signature=27a151d69f1a7eb49fcc5ed913ba95855dd62b57610afc655a1f342d023b884c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TKAEGWO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhx%2F33fUOwrWNnD69wFsk%2F%2BLg2cktCdFd4rvxZjlugOgIgIMLiBxqrv0qy1XePOPJ3YXkZoN0l1tsaMEt%2FqL4%2B0ioqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGYgxvg%2BG3PAJLV8CrcA8aTjoNSMB4C1npiW8dlW8jSuzTiBFUEeAwT%2FbZ5Cwk%2BPEj0kQQYVTcgmrWpjpxgPi%2FwxktC4qTPzZKcsjIl6v71GX6JR6k7KQW7bUBOdFt6UaFNCOK4kYrZ7BNw4EFsBC4f%2BX0JyMVbWf6YyrphuEQDg07IH3Qfjk0QwuVRLKJtAASKsjiijFEcGox6lebB3zJz6OM5O3ZT44PM1R1RIbnalqlLmayTPG%2FVdssqH72y5JSN3rKBXmBUBxoQTTQoB01SbjEbHprgIps1prTfJ%2BTZIXD8sTOHM%2BB7xIN55URR7v6Xw0j8Cspq6c34lPCPAwaMO%2Fa6s%2Bs3S5d9Zr%2FuduOv%2B0i0xtbgxtiKPRLyV85msQ00cN9ulB%2Fwy%2FVrMNy63EqIKwEiNFSzJPpkeU6hr9JKGyXKqb7B%2FbqE3yJixu8WkzqqzL47s%2FQlk0Xs%2BCY2j9e6pciT3j3hMd6b1dQYaagaWH1q7oxYW2nZ7fnBjRxLsGgNrWWnUVrk8mlvNoGHbN5gBkO5lnbhPYKxzaRP%2B28RQOjrBbq6%2B3tpx19qPWsf%2B1rXoJgRnCmzMC5ugk04t1OrInLASoiqciipmWcBd7kuRJccALAmbN7AkfYTVgvXU2SqrRq3dKn9RBYUMOrF6rwGOqUBmI8dK99utL76WQw%2BUsbnwZ32UYqWoxNpTSh8TvN5vphjX7nIy8lzlktkf01oz3kxoNGh4dkJYmp2GiBxM4pthxLgKFgoDr0HKf3SxCj1lNXUtFCK8y09OREl%2BPUooL8jC%2F0c7EmWDMskTeVOHSDMGM%2B6wJZFiVWf2c25lh71NPsTU%2BkqZCi1KplEKzPdMJ2oTo2aHU63j3eBzoPuftKwaCNIbfpl&X-Amz-Signature=8fc76c335d5d7332b5ea9f44a66b5eb107b627b90e03f3a751430016f914771b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TKAEGWO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhx%2F33fUOwrWNnD69wFsk%2F%2BLg2cktCdFd4rvxZjlugOgIgIMLiBxqrv0qy1XePOPJ3YXkZoN0l1tsaMEt%2FqL4%2B0ioqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGYgxvg%2BG3PAJLV8CrcA8aTjoNSMB4C1npiW8dlW8jSuzTiBFUEeAwT%2FbZ5Cwk%2BPEj0kQQYVTcgmrWpjpxgPi%2FwxktC4qTPzZKcsjIl6v71GX6JR6k7KQW7bUBOdFt6UaFNCOK4kYrZ7BNw4EFsBC4f%2BX0JyMVbWf6YyrphuEQDg07IH3Qfjk0QwuVRLKJtAASKsjiijFEcGox6lebB3zJz6OM5O3ZT44PM1R1RIbnalqlLmayTPG%2FVdssqH72y5JSN3rKBXmBUBxoQTTQoB01SbjEbHprgIps1prTfJ%2BTZIXD8sTOHM%2BB7xIN55URR7v6Xw0j8Cspq6c34lPCPAwaMO%2Fa6s%2Bs3S5d9Zr%2FuduOv%2B0i0xtbgxtiKPRLyV85msQ00cN9ulB%2Fwy%2FVrMNy63EqIKwEiNFSzJPpkeU6hr9JKGyXKqb7B%2FbqE3yJixu8WkzqqzL47s%2FQlk0Xs%2BCY2j9e6pciT3j3hMd6b1dQYaagaWH1q7oxYW2nZ7fnBjRxLsGgNrWWnUVrk8mlvNoGHbN5gBkO5lnbhPYKxzaRP%2B28RQOjrBbq6%2B3tpx19qPWsf%2B1rXoJgRnCmzMC5ugk04t1OrInLASoiqciipmWcBd7kuRJccALAmbN7AkfYTVgvXU2SqrRq3dKn9RBYUMOrF6rwGOqUBmI8dK99utL76WQw%2BUsbnwZ32UYqWoxNpTSh8TvN5vphjX7nIy8lzlktkf01oz3kxoNGh4dkJYmp2GiBxM4pthxLgKFgoDr0HKf3SxCj1lNXUtFCK8y09OREl%2BPUooL8jC%2F0c7EmWDMskTeVOHSDMGM%2B6wJZFiVWf2c25lh71NPsTU%2BkqZCi1KplEKzPdMJ2oTo2aHU63j3eBzoPuftKwaCNIbfpl&X-Amz-Signature=983c41957c789eec9d745e641ad8295d290788157c5fe8392b3c6d66802eecac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TKAEGWO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhx%2F33fUOwrWNnD69wFsk%2F%2BLg2cktCdFd4rvxZjlugOgIgIMLiBxqrv0qy1XePOPJ3YXkZoN0l1tsaMEt%2FqL4%2B0ioqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGYgxvg%2BG3PAJLV8CrcA8aTjoNSMB4C1npiW8dlW8jSuzTiBFUEeAwT%2FbZ5Cwk%2BPEj0kQQYVTcgmrWpjpxgPi%2FwxktC4qTPzZKcsjIl6v71GX6JR6k7KQW7bUBOdFt6UaFNCOK4kYrZ7BNw4EFsBC4f%2BX0JyMVbWf6YyrphuEQDg07IH3Qfjk0QwuVRLKJtAASKsjiijFEcGox6lebB3zJz6OM5O3ZT44PM1R1RIbnalqlLmayTPG%2FVdssqH72y5JSN3rKBXmBUBxoQTTQoB01SbjEbHprgIps1prTfJ%2BTZIXD8sTOHM%2BB7xIN55URR7v6Xw0j8Cspq6c34lPCPAwaMO%2Fa6s%2Bs3S5d9Zr%2FuduOv%2B0i0xtbgxtiKPRLyV85msQ00cN9ulB%2Fwy%2FVrMNy63EqIKwEiNFSzJPpkeU6hr9JKGyXKqb7B%2FbqE3yJixu8WkzqqzL47s%2FQlk0Xs%2BCY2j9e6pciT3j3hMd6b1dQYaagaWH1q7oxYW2nZ7fnBjRxLsGgNrWWnUVrk8mlvNoGHbN5gBkO5lnbhPYKxzaRP%2B28RQOjrBbq6%2B3tpx19qPWsf%2B1rXoJgRnCmzMC5ugk04t1OrInLASoiqciipmWcBd7kuRJccALAmbN7AkfYTVgvXU2SqrRq3dKn9RBYUMOrF6rwGOqUBmI8dK99utL76WQw%2BUsbnwZ32UYqWoxNpTSh8TvN5vphjX7nIy8lzlktkf01oz3kxoNGh4dkJYmp2GiBxM4pthxLgKFgoDr0HKf3SxCj1lNXUtFCK8y09OREl%2BPUooL8jC%2F0c7EmWDMskTeVOHSDMGM%2B6wJZFiVWf2c25lh71NPsTU%2BkqZCi1KplEKzPdMJ2oTo2aHU63j3eBzoPuftKwaCNIbfpl&X-Amz-Signature=e8c9cdf800d1fae5c4023e2c1a309dedda0cfb53085f1d76a9d1db0efa18072c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4UOPO7I%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFoeBtx15kEE8IXyt1xp6W4Z0sEiOOgzF20va2YJPu1%2BAiAS3iCRHJ5eL0%2BwG2ulrzXxAL9wutH0Dr8LbScmzgf%2BNSqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMspWql1TB29mHtCB6KtwDJwWWVG00b8yl3kO4w6PMsNF4sffJ7KLVsOP8oDams9490FOJK%2F8%2F%2FWiFhlPp%2FjbnGS00NPKZrelInC3uIG2MweDVRS96WBmvUUHbyWZ0Ro24R%2B6cdUPgaeq7iF4nvL%2BQlixEVMsSnZlOfdiHe6Uh1G66O6dQBDpl6ShCq%2BVKJfyWYAw2%2Bh2vsqFIKqyPX8JdIQE8tIQsWOZ6ugpf4zACq6XSOyuFbKi87wCRqvZrAykkPd6o0yhdWyMfMBhR%2FxyrxvBICsJJhbVZiq3146%2FgWYCugIEY0o5FRaQ928U5bSeAsoSvvEg5ng5G7F2OkxCcuKtSTbB3hRwsMlyjTIFI%2BcxUzkdTeqLtkT1iVoq5cBGfNseELobViAuxSc8zSSxPXWYTlE1w5m9mZFGUtHpIeMYlrKBKdpyZF1g0SMkWFkGJ2rr%2B5ZiXEufMyEgPIHdJqRdLZgM7WwU7iOKVXn55y%2B4Hk5hXWaGnyFwxf9L93zJtwex7bcHSON6qsoLkn1oAKP08S7wfJo9Yd%2F6GT%2FhQqQxGXTu4znKyBrHzy61aNMNFSgGz%2BpJF9boixG5QGhOtDA30BhXI%2FKB6SOU6KP0jl%2BC62hlOVOfw3GSEMeSc%2FGtKchmVac4CqJ9XqeMwrcbqvAY6pgEsWI%2FanHgvTHA5esRIDQiJwhAZdv%2BNj%2BxqxkeCtiy1wisEJH%2BZOlFNBtPVw%2Bsiq%2FiPSPd2HoORxH4LjtuzkNf%2BjqtwM41ZyrI4roakJE5NUOwQurMI%2B1sRmkFAQ7Ow2jDGlZPGjPa8ehZ2MP0g9u635bBrxEsYF6pXbX4ArA%2Bumt2UknH6Vs2J8dZjuk9sogQx%2FG7sSX9Ye1MtrMXB05VEkvg00W%2BK&X-Amz-Signature=374af80fcdb722ebaf8cb0aa431b6c4a3824d4f98be47735ab89d5cdce76b68b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y4ZKPWL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWSzr1HjECdwmTw8sV6R%2FTo26VNRufMqnBI%2FWlwDiwzQIhAJbRkTg%2FDh%2BVd%2B1VPZUmHY92NKJ4pUmwbJFSd%2BdQAms3KogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B5ZQJdihJOujd%2F8wq3ANjKozJekmuVTXYSRiRcQ2c%2BZ9ttvUS3KcvWf4MFN6kBplpGeSQ11GgIrz4WzDBTPKDekDiSzHtb6ZJG0Mm9LsFZMN5H9Eox9oB4cNf7GFLMfLy4V3sLkcD50w1LRzYdGebhdFNrVJgT1E%2B7WCRUO3qEaK9nddtLnPmjjj5EP6APw7X6CkEJ6prJCLpPL4e21BQEtTHFR%2Fi2LFHpCTPS0Zx2ycIz08WvLTec5g55NCnqzcyAdxC77QtUMRtmDsEGc%2BPSWj0zPnr7BjYbh9LMzAP0vb%2FyK%2BfMnmPF2NXLSWAQEdhds2GUHVdxPOp0a45oDi4w%2BmS%2BOG9Ua5dskopUb4mO7NpAHv9qvjpMqzBGqdQzRqbuzpJ1V82nUmSgjUx5HpIuN0y3YZ%2BcQ5s15Z7QlQLDF3aBpitHmCZ0ohuGwcTbcxr%2FOZm6OucunlP3kCG4YPQVYBkYUj3Ju6l6IuKFL%2BWCcOLnCxAHd8fyanA9M4iUUGhV3UzG%2FXnSudlEwpoP9OjWy33ptPiItYM544ya6iwNijIQPIAQA7TigTcuU7WU75cJF%2FUQNJNhHRgy%2BorbPM6CHDjttmi1LSF7axKCqasdYVVvg9gXr12RwoPdPGUL2jcwiy%2BHyub3q9mXDDhxeq8BjqkAYRIfgiAAdzNS5m2sRjWvR8vxFsnqKQbWSI9nIrDrRWJHsecI6qDs%2B2lUTHy8dtRFRKddmugRflcxt6y1598nxi7BDcc%2B2sUnmNqTEtKf2VDevcZUxFik1Isq0hdZGLFRkv3g2lwcHxARp57qT9YCMFlyqldS0QGPoEOxatr5BLpaxqRxAR0rgpksxNdgIhsSMt7lY4%2Bfxl%2FxJUG2%2FKbxaew70Od&X-Amz-Signature=067a16fe0c77e84c1eeee73f0943b84bf14d7c275ead24f598f993519d602632&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636HW3CQ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDjqGGwIPtzkSbYTmF3ho1SsM1D50Zbus4bdR%2Bvm8Y%2FRAiEA5ENdqSEpSehu0XUZhSkGaHmBl7jfGxgp5Re9A4OLVjAqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHH7frCyQBkKv1JvQircA9Orfs873ExHrt5kwz4qflXvm6l523Lf3CIm3Mp%2Bjlk8YUFmZTSnGCAk78rQ3WaLkZOQYWS%2FMXYRN1vIZlFnQ%2Bxx0QkTMbPZEA9diRWneX50lMDa5A9jEEZivy1PYB2HZU8G%2BdNOpVYg%2B1AQkBD8YeJmJ21DWLK9e92%2FRaITtqkK3s7qibL40H0T0mdzLsTzlhHJelmhCYmBeNh%2B%2FWepzwHkRryDREZPMghpgh4tCaJWCXKvC%2BvPGOcgDi6mc1152lE1i%2BdzFleEqo4ReBYv1bPLGNWEupr%2BcvtvKpUluUbDLPJZQ7XjVkrsmmOEoBrkDZgYZtDzR4Tj1540265qq0dKj6mfnk%2BUospnK1kIfXAt86zQ700qIIGte4xj9R9hz1BttdUyKBdOwwWns56C%2BAzL%2FShK%2Bv6zNv7eI94RDq7gNpOSXay4Aet9m%2BH1Jveh22CQnbxFIbLpqT0sdUfprSTILQNvVYQi%2FUppNwBZPNNUZkcea4lP4Cwn2%2BUY67gK8KK2VrOb8upWPknXf8Ynhdr3P9EGxFOzoEToK9FRAZ8l5%2FZ%2F1RjV%2FgUp%2FYapR7lF%2BFXUUs1QQHbdqxuwurUOqJe%2FojT0hfgDz8w25JDPwVoyNOR7wmfAxnIc6HwwMJfG6rwGOqUB1eomXixvAsPc7%2BhMkJZYNTYdjdVkrO6bUGhh5XjQFBbymR35MCbo0vSY9RWNp7i9TwYyw%2FRtMgqQXMPBN%2Fl7%2FcvaXmZnEgkx8eNsAxB5yqlyzkunMdeBZi6OpRR14wrXbIShErYkA75XEsJdM4pRbqDs%2F2yHHLnMN0WsMH9g1BxkdRBlTu2BTfaBQl8IwWpiQw58wK3Bikje5JpHOE8lcpAk8Wk6&X-Amz-Signature=7677ce25b5e2bb6e48b5a15004408bd4139057a98280aa8a678619f91b2bca7f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2MJNSPF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDie5jOZVI5saUVD4CKQoPffv93exJtxCL7qEs%2B3MmI7wIgXlCd2QEsoxmpIm%2BX8yRnatxP%2BsUzUbwdhapmRFxWBpEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML1iYo%2F5rp5h1vTaSrcA3EjLLQDhzToedFhp3ZfIF3FhEE0pxwe%2F16zG%2Bb0aNN%2B7yqOHU%2Bk0oxt47q7E5OoTkeRDVFA%2BzZ2Ca5fGxCOzEw%2FGwej1ZXo4UudQNkm%2FDXKijzPlwYZCxxO2Wtd45fcKcMeSUcv53uXztBaABiFECds7xftWEwWVLXpZWXS6baN2kqOl0lCiMljDn7cZLG3QKoWwdosZt7BhovUi6mVq3kbxO3XzBFQiA1Lu6b5UOqVjfPrU%2BC7XHozGW4TprI0cAadu0zrGiEBMVUXyPcFc58OhGQ%2BCuPpZyt9d4lnPRqR9cdCDraGKCnj2DIZj3lOJJxR34cWqnz44Ao%2Fe33E0c6oR4zyVhnmrn6c8mwMPbe2vClS%2BMKNV0RrF65u6z1lgNaVghNlFOzjTriU%2FU52yjJlhow9Uh0jTGC0iuTvfwar9LJfYUlJ31Zns7BuBxXeb1YCnOzKX6GKpRj3wsQDB%2Fdm8SoIJX2BBC1oFUivz57dH%2B%2FTzDExjZf%2FNiI%2FYYe6t%2F7qOicP9Bm9HStpCTaIyZfqu2nx9u75PtFIbR6HQwfBdJUoccsJp3wJQ2svvN2tc7GFqtZ7j%2BJyDyWEqOdPxM5NHl02SPtDcNMtAnqbLrqbgRYYxM5gs9B%2Bw7YkMN3F6rwGOqUB%2F3aqQC5ORl7iFQapGCqZ5MIQ%2FUZWRarQwuEqT9FPrMGnLWQspp1pVx82820Gm7kTPfD6Fn7LBXseZ65erLNDiqH1NLfeV1xyjggPOXq8AJmNxFKnoxVQUnCw7fE432HiNK0BYSQeZNGNlVpz9eJJBZnNFkILxo8MMnBSt86YazA9EzWVNfGzFSDdO4nSR4d6HB3xSi%2Fk2MTobKGZu8SHwHvvj9Bw&X-Amz-Signature=f8bad89255a35480fe356f84cbae8a0501c8c226130105b5c90e6a50d05c1ada&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2MJNSPF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDie5jOZVI5saUVD4CKQoPffv93exJtxCL7qEs%2B3MmI7wIgXlCd2QEsoxmpIm%2BX8yRnatxP%2BsUzUbwdhapmRFxWBpEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML1iYo%2F5rp5h1vTaSrcA3EjLLQDhzToedFhp3ZfIF3FhEE0pxwe%2F16zG%2Bb0aNN%2B7yqOHU%2Bk0oxt47q7E5OoTkeRDVFA%2BzZ2Ca5fGxCOzEw%2FGwej1ZXo4UudQNkm%2FDXKijzPlwYZCxxO2Wtd45fcKcMeSUcv53uXztBaABiFECds7xftWEwWVLXpZWXS6baN2kqOl0lCiMljDn7cZLG3QKoWwdosZt7BhovUi6mVq3kbxO3XzBFQiA1Lu6b5UOqVjfPrU%2BC7XHozGW4TprI0cAadu0zrGiEBMVUXyPcFc58OhGQ%2BCuPpZyt9d4lnPRqR9cdCDraGKCnj2DIZj3lOJJxR34cWqnz44Ao%2Fe33E0c6oR4zyVhnmrn6c8mwMPbe2vClS%2BMKNV0RrF65u6z1lgNaVghNlFOzjTriU%2FU52yjJlhow9Uh0jTGC0iuTvfwar9LJfYUlJ31Zns7BuBxXeb1YCnOzKX6GKpRj3wsQDB%2Fdm8SoIJX2BBC1oFUivz57dH%2B%2FTzDExjZf%2FNiI%2FYYe6t%2F7qOicP9Bm9HStpCTaIyZfqu2nx9u75PtFIbR6HQwfBdJUoccsJp3wJQ2svvN2tc7GFqtZ7j%2BJyDyWEqOdPxM5NHl02SPtDcNMtAnqbLrqbgRYYxM5gs9B%2Bw7YkMN3F6rwGOqUB%2F3aqQC5ORl7iFQapGCqZ5MIQ%2FUZWRarQwuEqT9FPrMGnLWQspp1pVx82820Gm7kTPfD6Fn7LBXseZ65erLNDiqH1NLfeV1xyjggPOXq8AJmNxFKnoxVQUnCw7fE432HiNK0BYSQeZNGNlVpz9eJJBZnNFkILxo8MMnBSt86YazA9EzWVNfGzFSDdO4nSR4d6HB3xSi%2Fk2MTobKGZu8SHwHvvj9Bw&X-Amz-Signature=d9ae2cd15ce23e57a4baaa705b391779c49fa7cba10c5470d0d0864917743c47&X-Amz-SignedHeaders=host&x-id=GetObject)

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
