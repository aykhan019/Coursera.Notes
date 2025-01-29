

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MARZGPO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuqeNRXvPi701JBZ6SJjSRzQm0yIPzhB0zde43EP02AiEAnQPy4BXeuLjq4MVeCV9%2BRYOxdVcB%2B2v6raW9MSffvWwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOI2wSu4jnKesg3WhSrcA1EPsPhhTbIx30CSoIKrmKFnxOicBod0kVdld7CEqzEo%2B%2BQNyuGvh1ks%2FRMyux23szufsC1Z%2FS1gwcPXOYs%2FX8Jmyp8rvNiVRRnbbsuGJO0mzibXJDxsb%2B55jIWUdAOoYumBs%2BRbNwUf9yImOHFo7xvutBXtSQbl8VAbHXx7rvmP0j66SMZAoAeszK%2FTx5A%2FivIFDxfg4sSsb%2FcILGA1PDNRp1NPxG0Phkr15%2FX1Ba5ircvKt0tZXr06cTZmEM0WtNWhQo3kawvrMwj%2BEPyLs2a2BmH08f%2FbplvQCRuuVwFqwwZkMZyAOTdYB5O5xLzJVfzOqpBPryTKLBXnWNQqED9weGwAB4dhDRAR36uxzlF%2Bu1Sx15TESF0dKWNeQXzHdFQEgHrBAW3O9Frl0xgxKSX6vbcFjEmuI0x2fJjqlnSI%2B7Nttp%2FNKTbTDZxcwGYTOM73UkpCluv3Z7s8euXResiTaRlK6CGEHiQrkqEmJPQjG6rsBerZyTEdok0yukWkW3JTUgTlA02zHcXfjuTt02A6LoIFkrrBn1jCphx1rWUW9effe%2F3Emg6tR7d7Jd2mTbl%2FYc054UpwqlBjRps1vdxHulG3lQqQ%2BBovMqR2sWVFolTOzWxoCiaMkbfNMKTH57wGOqUBYqo8jmmoYR6Cw4KPLUV9qNOPUwXKEZBvx96D7deiFB8MoALjcXlnUkpmAHr9%2FC8DgO%2Bw0QYKnn9VV2YSjT8a3AH%2BvTRXOmzm8Xmqec40PUPtUQ16mk2Ighn8XH4eTCa1TvttL4fkW9NAgBDHJIO1Db0EryjUboiUi%2FrzKAhTaXO76sG4yo3SivCqqWTTs31mJ9Yhu6Y0ZTus%2BtP2P8UGm3av59kf&X-Amz-Signature=850714cb34ac441df2b8170e34bce60b1b211fd6f14656d0c8c11f7041430075&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MARZGPO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuqeNRXvPi701JBZ6SJjSRzQm0yIPzhB0zde43EP02AiEAnQPy4BXeuLjq4MVeCV9%2BRYOxdVcB%2B2v6raW9MSffvWwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOI2wSu4jnKesg3WhSrcA1EPsPhhTbIx30CSoIKrmKFnxOicBod0kVdld7CEqzEo%2B%2BQNyuGvh1ks%2FRMyux23szufsC1Z%2FS1gwcPXOYs%2FX8Jmyp8rvNiVRRnbbsuGJO0mzibXJDxsb%2B55jIWUdAOoYumBs%2BRbNwUf9yImOHFo7xvutBXtSQbl8VAbHXx7rvmP0j66SMZAoAeszK%2FTx5A%2FivIFDxfg4sSsb%2FcILGA1PDNRp1NPxG0Phkr15%2FX1Ba5ircvKt0tZXr06cTZmEM0WtNWhQo3kawvrMwj%2BEPyLs2a2BmH08f%2FbplvQCRuuVwFqwwZkMZyAOTdYB5O5xLzJVfzOqpBPryTKLBXnWNQqED9weGwAB4dhDRAR36uxzlF%2Bu1Sx15TESF0dKWNeQXzHdFQEgHrBAW3O9Frl0xgxKSX6vbcFjEmuI0x2fJjqlnSI%2B7Nttp%2FNKTbTDZxcwGYTOM73UkpCluv3Z7s8euXResiTaRlK6CGEHiQrkqEmJPQjG6rsBerZyTEdok0yukWkW3JTUgTlA02zHcXfjuTt02A6LoIFkrrBn1jCphx1rWUW9effe%2F3Emg6tR7d7Jd2mTbl%2FYc054UpwqlBjRps1vdxHulG3lQqQ%2BBovMqR2sWVFolTOzWxoCiaMkbfNMKTH57wGOqUBYqo8jmmoYR6Cw4KPLUV9qNOPUwXKEZBvx96D7deiFB8MoALjcXlnUkpmAHr9%2FC8DgO%2Bw0QYKnn9VV2YSjT8a3AH%2BvTRXOmzm8Xmqec40PUPtUQ16mk2Ighn8XH4eTCa1TvttL4fkW9NAgBDHJIO1Db0EryjUboiUi%2FrzKAhTaXO76sG4yo3SivCqqWTTs31mJ9Yhu6Y0ZTus%2BtP2P8UGm3av59kf&X-Amz-Signature=2c638034506d074b251dc94d0e88d4cacb31162343120aa912098142a6fa6b1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MARZGPO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuqeNRXvPi701JBZ6SJjSRzQm0yIPzhB0zde43EP02AiEAnQPy4BXeuLjq4MVeCV9%2BRYOxdVcB%2B2v6raW9MSffvWwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOI2wSu4jnKesg3WhSrcA1EPsPhhTbIx30CSoIKrmKFnxOicBod0kVdld7CEqzEo%2B%2BQNyuGvh1ks%2FRMyux23szufsC1Z%2FS1gwcPXOYs%2FX8Jmyp8rvNiVRRnbbsuGJO0mzibXJDxsb%2B55jIWUdAOoYumBs%2BRbNwUf9yImOHFo7xvutBXtSQbl8VAbHXx7rvmP0j66SMZAoAeszK%2FTx5A%2FivIFDxfg4sSsb%2FcILGA1PDNRp1NPxG0Phkr15%2FX1Ba5ircvKt0tZXr06cTZmEM0WtNWhQo3kawvrMwj%2BEPyLs2a2BmH08f%2FbplvQCRuuVwFqwwZkMZyAOTdYB5O5xLzJVfzOqpBPryTKLBXnWNQqED9weGwAB4dhDRAR36uxzlF%2Bu1Sx15TESF0dKWNeQXzHdFQEgHrBAW3O9Frl0xgxKSX6vbcFjEmuI0x2fJjqlnSI%2B7Nttp%2FNKTbTDZxcwGYTOM73UkpCluv3Z7s8euXResiTaRlK6CGEHiQrkqEmJPQjG6rsBerZyTEdok0yukWkW3JTUgTlA02zHcXfjuTt02A6LoIFkrrBn1jCphx1rWUW9effe%2F3Emg6tR7d7Jd2mTbl%2FYc054UpwqlBjRps1vdxHulG3lQqQ%2BBovMqR2sWVFolTOzWxoCiaMkbfNMKTH57wGOqUBYqo8jmmoYR6Cw4KPLUV9qNOPUwXKEZBvx96D7deiFB8MoALjcXlnUkpmAHr9%2FC8DgO%2Bw0QYKnn9VV2YSjT8a3AH%2BvTRXOmzm8Xmqec40PUPtUQ16mk2Ighn8XH4eTCa1TvttL4fkW9NAgBDHJIO1Db0EryjUboiUi%2FrzKAhTaXO76sG4yo3SivCqqWTTs31mJ9Yhu6Y0ZTus%2BtP2P8UGm3av59kf&X-Amz-Signature=325c038b9bcdf4f301a267e0410254e343674d069fc99fc1c6d44e2f3b3b9a4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB5ZFAWP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3k6EWlLmnoyA6LXk3%2FRQI9S73ypp6yWmDrSnrT%2FMR1wIhAKZjmKx2ObbnPRL5nNUV1wWHj%2FDmZYSwzigLihtN12RqKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8gt%2FfCng180hn9qMq3AODAHPwonW%2FmIA70oAK0F02EIbecZJTCh1tLujoc25fOOGjDP0ZGCBmFu6B8cdudsBeE2Y9JBcRlflEVCAnPpypQFtt%2FSi9JI%2BtJuW3bvIp09g1rGEcMKJ8MFq0M1Z86RjQhwD37YcYyRb%2FsTXK1AxQJLpiMfNC8eVRgekHsodfNbW2mZr9EImnj8wClFH%2FF8t1xRhS8MKO4nl2rQ4jS5itGbBqFaaJ4voN3s%2ByWhyRG5P58EXPiY7i2PRGFhfQwA8EALKfn79eOztqe%2FJabxPEfqWLVp26mS0TXutsAVdDM3lOEKnIV6Dp3t4C6nFfO%2FZKEWketBJu4x6BD%2FbmR7Pqm%2FuKoxeXNWEofUcNUcM5ocf6PxtTe7hokaQJcnPhpWHag4Smwj5xq2J%2FXCrcr2T1v9siLL3BKxkfRWxUFrSuYfUB%2FtotKYcHPfml%2B5CAwtKi1m%2Bg48LTe96CKpcM0bRTR66h6oWVdTaopy93r7R4B5SBE5Zg9ioS5ZwPsYSqxnvUf%2FWx2gOQG1D7N5ahuF59h1UOX9LtGqB1SNnwrSbmy4HEfJofW%2B%2FJU5WqEP4OQwiF0gqfVxBzn1BY9CqKtNidQqy3oF2c4n5BC1WdOxsLemJ059sEWlGhHjSnwTDpx%2Be8BjqkAZlmOTbCNvRlP1HGmvMHN7ArSj6As8m%2Bom292V0vxNEllaSZp9AuOLuixGWm6Eo8H2G%2BAx3GOmHHrQ5XQbrMEOq45WJ3ewBE3cIPtXlZyzrSLwBRwT2DiZEvYga%2BTeT1vyhIQ626tJP0lGUpe5SPVlRg0CokB5GS4wthVJwmAMr%2FKGE5rCiYb%2FppUAyl%2F8dadmNow2ohjOFf3mxfkLvt%2BDXKOz5K&X-Amz-Signature=a04519590b8cc466e50875cd985a4bdb6e75c30d1b85aa9466c90c57bbe0dd8d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB5ZFAWP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3k6EWlLmnoyA6LXk3%2FRQI9S73ypp6yWmDrSnrT%2FMR1wIhAKZjmKx2ObbnPRL5nNUV1wWHj%2FDmZYSwzigLihtN12RqKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8gt%2FfCng180hn9qMq3AODAHPwonW%2FmIA70oAK0F02EIbecZJTCh1tLujoc25fOOGjDP0ZGCBmFu6B8cdudsBeE2Y9JBcRlflEVCAnPpypQFtt%2FSi9JI%2BtJuW3bvIp09g1rGEcMKJ8MFq0M1Z86RjQhwD37YcYyRb%2FsTXK1AxQJLpiMfNC8eVRgekHsodfNbW2mZr9EImnj8wClFH%2FF8t1xRhS8MKO4nl2rQ4jS5itGbBqFaaJ4voN3s%2ByWhyRG5P58EXPiY7i2PRGFhfQwA8EALKfn79eOztqe%2FJabxPEfqWLVp26mS0TXutsAVdDM3lOEKnIV6Dp3t4C6nFfO%2FZKEWketBJu4x6BD%2FbmR7Pqm%2FuKoxeXNWEofUcNUcM5ocf6PxtTe7hokaQJcnPhpWHag4Smwj5xq2J%2FXCrcr2T1v9siLL3BKxkfRWxUFrSuYfUB%2FtotKYcHPfml%2B5CAwtKi1m%2Bg48LTe96CKpcM0bRTR66h6oWVdTaopy93r7R4B5SBE5Zg9ioS5ZwPsYSqxnvUf%2FWx2gOQG1D7N5ahuF59h1UOX9LtGqB1SNnwrSbmy4HEfJofW%2B%2FJU5WqEP4OQwiF0gqfVxBzn1BY9CqKtNidQqy3oF2c4n5BC1WdOxsLemJ059sEWlGhHjSnwTDpx%2Be8BjqkAZlmOTbCNvRlP1HGmvMHN7ArSj6As8m%2Bom292V0vxNEllaSZp9AuOLuixGWm6Eo8H2G%2BAx3GOmHHrQ5XQbrMEOq45WJ3ewBE3cIPtXlZyzrSLwBRwT2DiZEvYga%2BTeT1vyhIQ626tJP0lGUpe5SPVlRg0CokB5GS4wthVJwmAMr%2FKGE5rCiYb%2FppUAyl%2F8dadmNow2ohjOFf3mxfkLvt%2BDXKOz5K&X-Amz-Signature=e0ad6a050c94ab998fd002300b0ba5d5e1d124adc891eac98a8cfd030f555ae8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB5ZFAWP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3k6EWlLmnoyA6LXk3%2FRQI9S73ypp6yWmDrSnrT%2FMR1wIhAKZjmKx2ObbnPRL5nNUV1wWHj%2FDmZYSwzigLihtN12RqKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8gt%2FfCng180hn9qMq3AODAHPwonW%2FmIA70oAK0F02EIbecZJTCh1tLujoc25fOOGjDP0ZGCBmFu6B8cdudsBeE2Y9JBcRlflEVCAnPpypQFtt%2FSi9JI%2BtJuW3bvIp09g1rGEcMKJ8MFq0M1Z86RjQhwD37YcYyRb%2FsTXK1AxQJLpiMfNC8eVRgekHsodfNbW2mZr9EImnj8wClFH%2FF8t1xRhS8MKO4nl2rQ4jS5itGbBqFaaJ4voN3s%2ByWhyRG5P58EXPiY7i2PRGFhfQwA8EALKfn79eOztqe%2FJabxPEfqWLVp26mS0TXutsAVdDM3lOEKnIV6Dp3t4C6nFfO%2FZKEWketBJu4x6BD%2FbmR7Pqm%2FuKoxeXNWEofUcNUcM5ocf6PxtTe7hokaQJcnPhpWHag4Smwj5xq2J%2FXCrcr2T1v9siLL3BKxkfRWxUFrSuYfUB%2FtotKYcHPfml%2B5CAwtKi1m%2Bg48LTe96CKpcM0bRTR66h6oWVdTaopy93r7R4B5SBE5Zg9ioS5ZwPsYSqxnvUf%2FWx2gOQG1D7N5ahuF59h1UOX9LtGqB1SNnwrSbmy4HEfJofW%2B%2FJU5WqEP4OQwiF0gqfVxBzn1BY9CqKtNidQqy3oF2c4n5BC1WdOxsLemJ059sEWlGhHjSnwTDpx%2Be8BjqkAZlmOTbCNvRlP1HGmvMHN7ArSj6As8m%2Bom292V0vxNEllaSZp9AuOLuixGWm6Eo8H2G%2BAx3GOmHHrQ5XQbrMEOq45WJ3ewBE3cIPtXlZyzrSLwBRwT2DiZEvYga%2BTeT1vyhIQ626tJP0lGUpe5SPVlRg0CokB5GS4wthVJwmAMr%2FKGE5rCiYb%2FppUAyl%2F8dadmNow2ohjOFf3mxfkLvt%2BDXKOz5K&X-Amz-Signature=a91fd6ae7fcfaf3a49aab75e6ce896aa0e757742badcbbe6d785d3d24b44062d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB5ZFAWP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3k6EWlLmnoyA6LXk3%2FRQI9S73ypp6yWmDrSnrT%2FMR1wIhAKZjmKx2ObbnPRL5nNUV1wWHj%2FDmZYSwzigLihtN12RqKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8gt%2FfCng180hn9qMq3AODAHPwonW%2FmIA70oAK0F02EIbecZJTCh1tLujoc25fOOGjDP0ZGCBmFu6B8cdudsBeE2Y9JBcRlflEVCAnPpypQFtt%2FSi9JI%2BtJuW3bvIp09g1rGEcMKJ8MFq0M1Z86RjQhwD37YcYyRb%2FsTXK1AxQJLpiMfNC8eVRgekHsodfNbW2mZr9EImnj8wClFH%2FF8t1xRhS8MKO4nl2rQ4jS5itGbBqFaaJ4voN3s%2ByWhyRG5P58EXPiY7i2PRGFhfQwA8EALKfn79eOztqe%2FJabxPEfqWLVp26mS0TXutsAVdDM3lOEKnIV6Dp3t4C6nFfO%2FZKEWketBJu4x6BD%2FbmR7Pqm%2FuKoxeXNWEofUcNUcM5ocf6PxtTe7hokaQJcnPhpWHag4Smwj5xq2J%2FXCrcr2T1v9siLL3BKxkfRWxUFrSuYfUB%2FtotKYcHPfml%2B5CAwtKi1m%2Bg48LTe96CKpcM0bRTR66h6oWVdTaopy93r7R4B5SBE5Zg9ioS5ZwPsYSqxnvUf%2FWx2gOQG1D7N5ahuF59h1UOX9LtGqB1SNnwrSbmy4HEfJofW%2B%2FJU5WqEP4OQwiF0gqfVxBzn1BY9CqKtNidQqy3oF2c4n5BC1WdOxsLemJ059sEWlGhHjSnwTDpx%2Be8BjqkAZlmOTbCNvRlP1HGmvMHN7ArSj6As8m%2Bom292V0vxNEllaSZp9AuOLuixGWm6Eo8H2G%2BAx3GOmHHrQ5XQbrMEOq45WJ3ewBE3cIPtXlZyzrSLwBRwT2DiZEvYga%2BTeT1vyhIQ626tJP0lGUpe5SPVlRg0CokB5GS4wthVJwmAMr%2FKGE5rCiYb%2FppUAyl%2F8dadmNow2ohjOFf3mxfkLvt%2BDXKOz5K&X-Amz-Signature=60e6f279483ca76bb5530f8de19845d24d207414eed606e7420844aec3171569&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB5ZFAWP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3k6EWlLmnoyA6LXk3%2FRQI9S73ypp6yWmDrSnrT%2FMR1wIhAKZjmKx2ObbnPRL5nNUV1wWHj%2FDmZYSwzigLihtN12RqKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8gt%2FfCng180hn9qMq3AODAHPwonW%2FmIA70oAK0F02EIbecZJTCh1tLujoc25fOOGjDP0ZGCBmFu6B8cdudsBeE2Y9JBcRlflEVCAnPpypQFtt%2FSi9JI%2BtJuW3bvIp09g1rGEcMKJ8MFq0M1Z86RjQhwD37YcYyRb%2FsTXK1AxQJLpiMfNC8eVRgekHsodfNbW2mZr9EImnj8wClFH%2FF8t1xRhS8MKO4nl2rQ4jS5itGbBqFaaJ4voN3s%2ByWhyRG5P58EXPiY7i2PRGFhfQwA8EALKfn79eOztqe%2FJabxPEfqWLVp26mS0TXutsAVdDM3lOEKnIV6Dp3t4C6nFfO%2FZKEWketBJu4x6BD%2FbmR7Pqm%2FuKoxeXNWEofUcNUcM5ocf6PxtTe7hokaQJcnPhpWHag4Smwj5xq2J%2FXCrcr2T1v9siLL3BKxkfRWxUFrSuYfUB%2FtotKYcHPfml%2B5CAwtKi1m%2Bg48LTe96CKpcM0bRTR66h6oWVdTaopy93r7R4B5SBE5Zg9ioS5ZwPsYSqxnvUf%2FWx2gOQG1D7N5ahuF59h1UOX9LtGqB1SNnwrSbmy4HEfJofW%2B%2FJU5WqEP4OQwiF0gqfVxBzn1BY9CqKtNidQqy3oF2c4n5BC1WdOxsLemJ059sEWlGhHjSnwTDpx%2Be8BjqkAZlmOTbCNvRlP1HGmvMHN7ArSj6As8m%2Bom292V0vxNEllaSZp9AuOLuixGWm6Eo8H2G%2BAx3GOmHHrQ5XQbrMEOq45WJ3ewBE3cIPtXlZyzrSLwBRwT2DiZEvYga%2BTeT1vyhIQ626tJP0lGUpe5SPVlRg0CokB5GS4wthVJwmAMr%2FKGE5rCiYb%2FppUAyl%2F8dadmNow2ohjOFf3mxfkLvt%2BDXKOz5K&X-Amz-Signature=81c167a84929ad23437f3732b3ed432500fcfb0d378a3fb71e99f50931c50435&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB5ZFAWP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3k6EWlLmnoyA6LXk3%2FRQI9S73ypp6yWmDrSnrT%2FMR1wIhAKZjmKx2ObbnPRL5nNUV1wWHj%2FDmZYSwzigLihtN12RqKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8gt%2FfCng180hn9qMq3AODAHPwonW%2FmIA70oAK0F02EIbecZJTCh1tLujoc25fOOGjDP0ZGCBmFu6B8cdudsBeE2Y9JBcRlflEVCAnPpypQFtt%2FSi9JI%2BtJuW3bvIp09g1rGEcMKJ8MFq0M1Z86RjQhwD37YcYyRb%2FsTXK1AxQJLpiMfNC8eVRgekHsodfNbW2mZr9EImnj8wClFH%2FF8t1xRhS8MKO4nl2rQ4jS5itGbBqFaaJ4voN3s%2ByWhyRG5P58EXPiY7i2PRGFhfQwA8EALKfn79eOztqe%2FJabxPEfqWLVp26mS0TXutsAVdDM3lOEKnIV6Dp3t4C6nFfO%2FZKEWketBJu4x6BD%2FbmR7Pqm%2FuKoxeXNWEofUcNUcM5ocf6PxtTe7hokaQJcnPhpWHag4Smwj5xq2J%2FXCrcr2T1v9siLL3BKxkfRWxUFrSuYfUB%2FtotKYcHPfml%2B5CAwtKi1m%2Bg48LTe96CKpcM0bRTR66h6oWVdTaopy93r7R4B5SBE5Zg9ioS5ZwPsYSqxnvUf%2FWx2gOQG1D7N5ahuF59h1UOX9LtGqB1SNnwrSbmy4HEfJofW%2B%2FJU5WqEP4OQwiF0gqfVxBzn1BY9CqKtNidQqy3oF2c4n5BC1WdOxsLemJ059sEWlGhHjSnwTDpx%2Be8BjqkAZlmOTbCNvRlP1HGmvMHN7ArSj6As8m%2Bom292V0vxNEllaSZp9AuOLuixGWm6Eo8H2G%2BAx3GOmHHrQ5XQbrMEOq45WJ3ewBE3cIPtXlZyzrSLwBRwT2DiZEvYga%2BTeT1vyhIQ626tJP0lGUpe5SPVlRg0CokB5GS4wthVJwmAMr%2FKGE5rCiYb%2FppUAyl%2F8dadmNow2ohjOFf3mxfkLvt%2BDXKOz5K&X-Amz-Signature=5ba00c02b9e2d4f827c03daa48fe13ffbae9f7421826df3f4ea2421f82076315&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJIFZG4B%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEwyVwJ4e%2BwEXfB6qG7cokez9yc1HpBefuMwXNDV930IAiA3P7vuSqxcb2AHmZ225CRm7%2FVG1QoSEG775Qe51aOYkSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME3ee5RqIZd9ArDZTKtwDHdf%2B6st4nM2D0mmVtfLDRBkXPhFZyy0JNvvm4tREfOERlcWfPZ8W%2Fvg0yPctEqO5ibLl7KVqIcjn7iQkLuwZTxP3omFKUS1D2w3nvbEUkyueBxRVcF6%2FmLMhJJJeDZLCwfmT38hBtsypK0Pq8Pcu9gQvr1MjOiRRaPyX77VFCAXI25oKM%2FlpdodKEBXESw%2B64KJC2bcM62cBe%2BlEjWpJG8JDn%2FiztpxbU%2FQkexXwVIvXlURXehKCSQX8z3P%2BCE8VZsnpjMdXD9S0fxZhRBN%2Fhz5AD5h7RX8io9mHv1GDUNeggUIkeUIKwYkDFqwYNvBT%2BTtI1fU8Yb0pXLj6o5hHdCGr2EwyRcgnjdgpGSiEdm5iC3IFew%2BnqOuAeC0LGcSezNF9cUMS%2FlTrX%2BiADnYoziFmakgTUXaVd3Gi1ff7eOxHeDemcL8JFtb2x8WghOw%2BtboIPAhOPUkdAidykao2GQoXQEQ9a2dsnpyB3GWxffqQmLRnR1bPRbyhgOkprgZ1BGLfGpIIk2JOFAwyJzJ2KHk%2FHu7WGHndl9HkitbtzfATvOxqnRPnMbaq5uNYDTIS3MIzXxp03sHSzbVQLgfPv3H%2BEcAnBtrdbeXUXWQKZuSHXVC0KAyR0%2FEbVIMw9cfnvAY6pgF%2FsUbMRxMopFyAHopbBJnRICu7LFqCxCy9uCQ8qNBAD1AUCfJ6fbymcXBgKc9l%2FCWibiBqB9yTyyn1585bIPtf9j3PpO6xzseYdnMw3GNky3zDSVmqM5LgIWaY3zevweco1JJbNG0vlaFOornMCSs3rllCOQ7ygg51ZKfLDMhHduib%2BRZuHMlS%2FTzZTjdXHh5DRYW9vcWJqsFvlaePtqsBfIW%2BVr%2Bh&X-Amz-Signature=831f88d07554ab7ef5601708b9f7372f0fd8c9e18ac1d9bd8491644b26b9e26d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJUCICDM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHmd78yjmaTXNR%2FxvUP%2FwKnwR2JmAG3LQjU8wWJogAGFAiA5mCRbhCIur7uuehb2Jwpb9SOUoefDfrKdxSRVmpjFEyqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDByE1rlVClbP8wNfKtwD4TqgLtHDo%2BYjnMkMdl4kxIlqa%2BMBpU0X%2F6DhWQLhoLFU46N8nJeuAttn9edth8eF1%2BY4YjTg2e%2Bjor5jdFPDFjTpy2Y57O1cRO2CP9s5LBbHo1KIA0aV%2FXL%2Be24jfHZJ36UB6Ivq39qnptIdiWSr%2FzsFbBFLUhwa9NzT4RqChoy4L3zQGyRSaUU2xs1hxnqWtMyrl7IlEHbRe0XjFIlxiIRjONKRr9Ko6M8tJrAIdDYTMv5XbTlzPWKBmoF5saFgNNIgtsm5fEinByUiwS6jbNv7Mcy70kjrvlqcIuNH5QpXw8UdvTjiHPi4gNLOGU6SmFmwzshw21PbQSNq01XvcWgEjJ6xziHnNBA1YH2YEqPAOQ7ooqn89w6%2BxDq0qu4Ap6CVQlMwq7f3ix%2Bcyfe27kDEsbyEVOkHiW%2Btj8ZfQzvvr6QeI5M2pDxwjUoHyNEJ4ZOTqutGchYgiF1BMVn%2FkctBYpjgE8pVV8SU2Ef0kFWwp8RpNFsBTq6N6%2BUL9EPGZ4Le5Fi6EXytONDX8dFIGlkrQH0okxUT%2Bqz9tW4%2BU6gfNMxokRrTelubE8UzjmThGq%2BgHG9bcfLsk21GDyKbiljRyZojpatdqTuEcvaAeQryNdl3Sb9jvu54ZiYw%2BKznvAY6pgEL1JvC1Hev%2BII%2Bnmk85DIXffE%2F7TeYVJH5w%2BQa%2BnrE1oPdr7vea%2B%2FgRLFMWZ4rdKm%2F8XAjh31yk%2Fxx9lNIf1F1oOpo7gOpXIuW0cSFYJgWtxl1C4DTK24KvUvk6jkSjwP68AQgM7MW9XUlxJCi6MkCLkqKKofKLLlz%2FN7bVcfhcH2idNy40kyWnBMADM3at%2Bw4Ny%2F6gAhxh%2BOz9Y0%2BcM63OATku3xV&X-Amz-Signature=c6246f5dd20acdbd62951ae4ef4e535d7922f99c5453dac7215741925dbe9ebe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB5ZFAWP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3k6EWlLmnoyA6LXk3%2FRQI9S73ypp6yWmDrSnrT%2FMR1wIhAKZjmKx2ObbnPRL5nNUV1wWHj%2FDmZYSwzigLihtN12RqKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8gt%2FfCng180hn9qMq3AODAHPwonW%2FmIA70oAK0F02EIbecZJTCh1tLujoc25fOOGjDP0ZGCBmFu6B8cdudsBeE2Y9JBcRlflEVCAnPpypQFtt%2FSi9JI%2BtJuW3bvIp09g1rGEcMKJ8MFq0M1Z86RjQhwD37YcYyRb%2FsTXK1AxQJLpiMfNC8eVRgekHsodfNbW2mZr9EImnj8wClFH%2FF8t1xRhS8MKO4nl2rQ4jS5itGbBqFaaJ4voN3s%2ByWhyRG5P58EXPiY7i2PRGFhfQwA8EALKfn79eOztqe%2FJabxPEfqWLVp26mS0TXutsAVdDM3lOEKnIV6Dp3t4C6nFfO%2FZKEWketBJu4x6BD%2FbmR7Pqm%2FuKoxeXNWEofUcNUcM5ocf6PxtTe7hokaQJcnPhpWHag4Smwj5xq2J%2FXCrcr2T1v9siLL3BKxkfRWxUFrSuYfUB%2FtotKYcHPfml%2B5CAwtKi1m%2Bg48LTe96CKpcM0bRTR66h6oWVdTaopy93r7R4B5SBE5Zg9ioS5ZwPsYSqxnvUf%2FWx2gOQG1D7N5ahuF59h1UOX9LtGqB1SNnwrSbmy4HEfJofW%2B%2FJU5WqEP4OQwiF0gqfVxBzn1BY9CqKtNidQqy3oF2c4n5BC1WdOxsLemJ059sEWlGhHjSnwTDpx%2Be8BjqkAZlmOTbCNvRlP1HGmvMHN7ArSj6As8m%2Bom292V0vxNEllaSZp9AuOLuixGWm6Eo8H2G%2BAx3GOmHHrQ5XQbrMEOq45WJ3ewBE3cIPtXlZyzrSLwBRwT2DiZEvYga%2BTeT1vyhIQ626tJP0lGUpe5SPVlRg0CokB5GS4wthVJwmAMr%2FKGE5rCiYb%2FppUAyl%2F8dadmNow2ohjOFf3mxfkLvt%2BDXKOz5K&X-Amz-Signature=a895e7e2ffd408d91902ebf1f5d2feb598effadbccf9d2b0bab7e87e47b47c60&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB5ZFAWP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3k6EWlLmnoyA6LXk3%2FRQI9S73ypp6yWmDrSnrT%2FMR1wIhAKZjmKx2ObbnPRL5nNUV1wWHj%2FDmZYSwzigLihtN12RqKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8gt%2FfCng180hn9qMq3AODAHPwonW%2FmIA70oAK0F02EIbecZJTCh1tLujoc25fOOGjDP0ZGCBmFu6B8cdudsBeE2Y9JBcRlflEVCAnPpypQFtt%2FSi9JI%2BtJuW3bvIp09g1rGEcMKJ8MFq0M1Z86RjQhwD37YcYyRb%2FsTXK1AxQJLpiMfNC8eVRgekHsodfNbW2mZr9EImnj8wClFH%2FF8t1xRhS8MKO4nl2rQ4jS5itGbBqFaaJ4voN3s%2ByWhyRG5P58EXPiY7i2PRGFhfQwA8EALKfn79eOztqe%2FJabxPEfqWLVp26mS0TXutsAVdDM3lOEKnIV6Dp3t4C6nFfO%2FZKEWketBJu4x6BD%2FbmR7Pqm%2FuKoxeXNWEofUcNUcM5ocf6PxtTe7hokaQJcnPhpWHag4Smwj5xq2J%2FXCrcr2T1v9siLL3BKxkfRWxUFrSuYfUB%2FtotKYcHPfml%2B5CAwtKi1m%2Bg48LTe96CKpcM0bRTR66h6oWVdTaopy93r7R4B5SBE5Zg9ioS5ZwPsYSqxnvUf%2FWx2gOQG1D7N5ahuF59h1UOX9LtGqB1SNnwrSbmy4HEfJofW%2B%2FJU5WqEP4OQwiF0gqfVxBzn1BY9CqKtNidQqy3oF2c4n5BC1WdOxsLemJ059sEWlGhHjSnwTDpx%2Be8BjqkAZlmOTbCNvRlP1HGmvMHN7ArSj6As8m%2Bom292V0vxNEllaSZp9AuOLuixGWm6Eo8H2G%2BAx3GOmHHrQ5XQbrMEOq45WJ3ewBE3cIPtXlZyzrSLwBRwT2DiZEvYga%2BTeT1vyhIQ626tJP0lGUpe5SPVlRg0CokB5GS4wthVJwmAMr%2FKGE5rCiYb%2FppUAyl%2F8dadmNow2ohjOFf3mxfkLvt%2BDXKOz5K&X-Amz-Signature=c9aeb4e5dc00a1c91a7112303473c69d940da02e1712859d61bc2bd74869f1d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB5ZFAWP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3k6EWlLmnoyA6LXk3%2FRQI9S73ypp6yWmDrSnrT%2FMR1wIhAKZjmKx2ObbnPRL5nNUV1wWHj%2FDmZYSwzigLihtN12RqKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8gt%2FfCng180hn9qMq3AODAHPwonW%2FmIA70oAK0F02EIbecZJTCh1tLujoc25fOOGjDP0ZGCBmFu6B8cdudsBeE2Y9JBcRlflEVCAnPpypQFtt%2FSi9JI%2BtJuW3bvIp09g1rGEcMKJ8MFq0M1Z86RjQhwD37YcYyRb%2FsTXK1AxQJLpiMfNC8eVRgekHsodfNbW2mZr9EImnj8wClFH%2FF8t1xRhS8MKO4nl2rQ4jS5itGbBqFaaJ4voN3s%2ByWhyRG5P58EXPiY7i2PRGFhfQwA8EALKfn79eOztqe%2FJabxPEfqWLVp26mS0TXutsAVdDM3lOEKnIV6Dp3t4C6nFfO%2FZKEWketBJu4x6BD%2FbmR7Pqm%2FuKoxeXNWEofUcNUcM5ocf6PxtTe7hokaQJcnPhpWHag4Smwj5xq2J%2FXCrcr2T1v9siLL3BKxkfRWxUFrSuYfUB%2FtotKYcHPfml%2B5CAwtKi1m%2Bg48LTe96CKpcM0bRTR66h6oWVdTaopy93r7R4B5SBE5Zg9ioS5ZwPsYSqxnvUf%2FWx2gOQG1D7N5ahuF59h1UOX9LtGqB1SNnwrSbmy4HEfJofW%2B%2FJU5WqEP4OQwiF0gqfVxBzn1BY9CqKtNidQqy3oF2c4n5BC1WdOxsLemJ059sEWlGhHjSnwTDpx%2Be8BjqkAZlmOTbCNvRlP1HGmvMHN7ArSj6As8m%2Bom292V0vxNEllaSZp9AuOLuixGWm6Eo8H2G%2BAx3GOmHHrQ5XQbrMEOq45WJ3ewBE3cIPtXlZyzrSLwBRwT2DiZEvYga%2BTeT1vyhIQ626tJP0lGUpe5SPVlRg0CokB5GS4wthVJwmAMr%2FKGE5rCiYb%2FppUAyl%2F8dadmNow2ohjOFf3mxfkLvt%2BDXKOz5K&X-Amz-Signature=2a63954cdfda8acd162eac62e87bf10fcdea131de7085151d2474fa2ce2c94c3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NYHF5L3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcXXIelH3jYIobMBXFU4L0OhqjYUPcD9ZcPC1Bkpv3dgIhAKQ6FJ8%2FYcTAyfO%2BqZOiqxKZAlQcOSxO64qZptLAF8gbKogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfiqN58IjceyzjZm4q3AP1fsyuEiAdroW46Fh%2F6tfYV1U9eERpUGBmZv3mvGx8OWSru8JbCjnA8GQZsnCs%2FPX2VSAYvq3FLGkHRBAA5uF2aLW85BYbUpfogKjCL8HpkbNohrkihFMEBxs1IifwHGzSIVxKp4DokeKWMPVxR%2FhaLX0K5wGR6PdULVYWUS4GJ%2BsLQ2t22BneO7WQm%2FbG5p8F5rZRA4P7A9ZvHmZy1oRZCaNCF%2Fw3p%2FKc8mQdk6kABAiZYOQJ6%2BEE3MEEUq9bfREpyJfvz7HmekRNHI6hN714juSVyRO6oENbnB6DkPWuyTwc62STDij4URi91JbGJSVRqGDObtzZREs6dBkA4IK1nTF%2BZFLfL9nMk37T52tRVHcnE5sUT0RwK43RRluj0cIA07h%2BDTvQL9y8pHAlw8HTcjBvppNaLh9M5z9toZC48St6pbIFsXO79XxSEV0K7eg5tEq2aJ%2FT1a1OmHazCLnfKmARXQBFl27ZHCh0drol6kT7NBzKNu6mqJrmAsXeEIpun2rpg%2B8Ee3D991UGEyLfc4%2FgxSlJ%2BWgnS3c1EnvbLyRQfBPvilzfqCwBdxa7tqLYqrjdGFeMy9oDdrf60ztpLOKCm00sfit8YiTfnPjpczPwh8rJCrB1mPgvFDDmrOe8BjqkATyl1%2FbQEQiQ9cL0qzxdBs31EO06HT7vVolOWBv%2BX4op3wH%2BA37Hoix0uhSo0B%2FZJ45tJiLZPThP0iJo%2FY%2BQ6FmLehFUB%2FhqrIboUE6sQRsDBP3lkijMwXDJXlfDQUrrsasDBRkjabxIHCzwMBdXZql%2BTYXdLnadMvFVOZ226qQkp5euaBoDrlPaMgCkW7tufJgzMHsLjY5kdCXYzPuDsaNltxmc&X-Amz-Signature=501dec99f795de199cc0342832704a8c86e75d1f562c8e9088904869a96f3521&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZFSIB2P%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOmuzkj7ah8bIzgo7EeOEbB5GMmdKlNxdJMEUy0gYkiAiAYHTGFr5S0fj7G6hTVv9FWc7iBSdZjmPdw6RDRNI%2Ft9CqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7ZKtZovcQG9aSGBwKtwDaaZ%2FJH%2FWo4g76erfUAEDVqX3egCIS7mCjTxnD4rM5u42d4Z2uPHBP7MTvgEMo85cMg2gInWCZdIqyEUeCcTYHfIIoqTr44%2B5ddTPfOvq45Mkr5P9pZMrQtsP3%2BmtaUEmFmX3v2uRqlCZHtcmw1YquS7Wd1oZd42XZC5tHxgYNnVH%2Fq8lz3iqDm%2BxBbxuQthC7iMJ0bcj4BWalH3YUvBa5aidSHomoqk8STO8SCvhfCv0TwgzytXb%2F%2BgXFrUtwd2bqsekAgBdLXFnMV9hVYO%2BNBIV4noAHJsGLx5DZW4Wo84Wdy8WkYt%2FcBlKDuvbLOylHoS7%2BhbP2V%2B8ibLXA%2F%2B2Dy1Mn2o%2BpmvdzDtGZ4ep%2FHxZ%2B25pG%2BsDVN%2BG6nSn66Ji0M1ZkxkM481Su1qJMHDlTKu6upSpIivfXPhFkeVeKkH9ahIRNXnHkwP54j3srSCBPE9WKG15ZSzYiHjv8zpcKkQSXIJUA%2BHTLXYKmpwp8YEgiryATe1pLm09k2zc%2FDdyRjubKSzzr3szp9kF9%2FD9LsbsDgoYsQH7bPmkf0FGvzmGEqvtd8ienAoCvwcw9hpqkj9cr4E5FEthR7tf5mwcnzFalYzFfuqw778rb9RIu2UDsH8EP%2FusnNb637wwo8fnvAY6pgFJrnhwredTu7vS9m406U3MHQk5iqxlXYGwkGenrCF6kaG6A19yDu%2Bs3tI3sZUl7lW4wkiDDHXDIN0I%2B4JtAUlasAmysk76%2BZXro8JmCWJVCk6uypyWDbKFMEKOfdFr9cGcx5tqqXdO14c1SvD3wntizBTIxwcAdTlTT%2F0AHcta9kzrhFsV5lBlt0vhpktEfSPiUF%2BAAt0%2Fl%2FejJcYHVgpYhRqlhQNw&X-Amz-Signature=3d60aa519cb59923eaf52e6ddab335d14160e55f891902a8323a71d3b18b95c5&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD2RDFZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDUM5tIMcfCVT4ngvRJYVxe7TpgM3i%2BZlHWOStMD8%2FJQAiAtHwrkwTJqYpQzYxdU7t6peAeCrTiG82tVUZX0P9k1IiqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHjKUfSMdqD0YWtUIKtwDQkuWRXNodSEkfl7WQ3bleZH98B6yljZqGNL08MiAiBFN0YjIo04XHOrBjDMLEGyImmQtIsCph6VfsGDrydF4HYjmh%2Fv5XnrQ4FJGwRYmtJ4WzUTWCYvkhQoJ0fFLC9br1tSFUTFhSznPR8nMyFcrw%2Ftq%2FnxG%2BnaIT4UEnmpqkgoTZlRhqhXI0tDHeZn1KgVcyAcpswMe2E380ZG6uR7vxaS1bvYI6uI492gy%2BlDPNeWpP6qoAo%2BGIPCWPDkUk4DoW853E801w55dufolJ1jhplYfrAXn2ijzuhl9L54uVNCfFBmfz5DBPBujnA9pboNRk6HpY5Q1m%2Bj%2Fm17cAI35DWY8dZ0Sv%2BFQ3CJDLnuUwMQWkzh9FEe3wL19gdq0%2Ficd%2FlLv6IM8swPN%2BP00GbH1nvGyheu6TucbUaiZV1OtSn1e2TOhRd6Y0cAgF9NbI17gTjuGEqdFf3NDlZiA7kWK50qiZvOnjQ3aj9GvofzYBwxrTgGDqjdTVWfu3NE%2BmcllEOcsG%2Bayh1NjeI0L2aypvrVUfZAeGgXYbMmsYFdEFZ6jSUxMiMeBEO%2BVo4YLuYaERuVOyMvLonqGj8%2BmlAwI61INgD9Pg5DwBQFmmP4OHWY9nsu2ZN4xgkuVGVEw06znvAY6pgEk09vfgXf%2BFGMethp9HtW6RF2L9n4VkYwALhGyQdwCG6YslLPZpFz5GKoYq%2BWcBsuL6Nc7JvGZIy8d5aEhLEQyNp8ggSg7gVC%2BHsYLo5yyZ0M%2F29JgNrKTFxF%2F96b%2BkSi1OpW%2F%2BrWzhgkqa0fJlY9%2BQPYqyN5LO8Rf76zHOybkNKgo3G%2FwZrDyy7P2SUVUlLwIsmM5IxXaqqiMRnBEyArp40D%2FsaEQ&X-Amz-Signature=047630901c3d513767af969a4c4d952ccf1bf0ff14302f5356e2a77ca96928c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA5NYRYV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjAKG2EYpGV%2FVIiBeIZ78vbM39LBC%2FA5Yh0R9ZNz3MAAIhAOryrI7eWWNjNdtB4MDAJ19Xp4HsD6SbZqV%2FRPZoAAR3KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2FJmkJfwaTa9I2BoYq3AOE4sVg0k4B0J90IHy0X5bMtef1%2FKPJo9UewH5lmoCrdK3rVTHQbCoSrf%2FeWhFUQ8cDL2bGuE7hNT9J4FGf2plYmCeVHajD6sgwkpGq%2Blqfew3p0gZG71kkbHYdY0RXnbdwWUk5IQmCz2vh5R27y1szPtw4xp9sb42f1rOwsKwFPmoVOxggFsM2dszxvHzWl96d8Yyjc0S53OEpwDkFqaS0I4quIYCNU%2BmQwOU8TU4xIiqNIVWzO7Hbgg5arYAoYaSZ%2FSbxl3aVSY%2B1ZW%2Bw%2BXvT9Z%2FJLnbNS9wgLtUUm6%2FNCHuW8rCKPGUOUMut7fMIp8hjcdpnj%2BU8aq9MYX5unU%2F5lK9eWpMpNB7l4TwjzHgUDDxfeyQi7bXo2BYFXasX6qP245yf4sbGVzNoJdT5Yz8QGNJc336mMjRzWZID9wW2NV2b%2BT3lWSxIY6xR6ZPcj0559yty7VTTXqv3BSU6jE2peay3COw%2BGmAC7NFV9ktC%2FSScdErvGFejlRqpl24A2yYLvwpTgJy2asZ31biLjhTSpIhi9HvepsacMLeGKFRXN34W0hX0BPBuh%2BEfWnuxs8vBU5cn4kooKWeUrsvlZvMcZ%2FuwdhLQsEY1%2Bi9IwACILyY%2FEzfuXY%2F%2BYWrMtDClx%2Be8BjqkAY6XNlAb1bzSFOHu9ndrJ8il2nb9QvYPcO9QbuovYKtbKwipEC2cC%2B6i0wqn1woZUIHv1EtTsPa4MGRcN6vRT6Lpdg9SzVZOGIcQk79WWcKOnmb4dt0Nir2bnz4D1nBBJ2UF%2BsDozxU7%2FXGj9t3BUkjY58wBOY3%2F0%2F15Mq6kGdNbsPs%2B0sCg5KrTK5JPTlKEyYncMzP67CZfSMzQMdXIZmUMydTD&X-Amz-Signature=f754aadbeafa799acbfd1fbd6b02a44740166db55cf587c06e9e56e5caa32c06&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA5NYRYV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjAKG2EYpGV%2FVIiBeIZ78vbM39LBC%2FA5Yh0R9ZNz3MAAIhAOryrI7eWWNjNdtB4MDAJ19Xp4HsD6SbZqV%2FRPZoAAR3KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2FJmkJfwaTa9I2BoYq3AOE4sVg0k4B0J90IHy0X5bMtef1%2FKPJo9UewH5lmoCrdK3rVTHQbCoSrf%2FeWhFUQ8cDL2bGuE7hNT9J4FGf2plYmCeVHajD6sgwkpGq%2Blqfew3p0gZG71kkbHYdY0RXnbdwWUk5IQmCz2vh5R27y1szPtw4xp9sb42f1rOwsKwFPmoVOxggFsM2dszxvHzWl96d8Yyjc0S53OEpwDkFqaS0I4quIYCNU%2BmQwOU8TU4xIiqNIVWzO7Hbgg5arYAoYaSZ%2FSbxl3aVSY%2B1ZW%2Bw%2BXvT9Z%2FJLnbNS9wgLtUUm6%2FNCHuW8rCKPGUOUMut7fMIp8hjcdpnj%2BU8aq9MYX5unU%2F5lK9eWpMpNB7l4TwjzHgUDDxfeyQi7bXo2BYFXasX6qP245yf4sbGVzNoJdT5Yz8QGNJc336mMjRzWZID9wW2NV2b%2BT3lWSxIY6xR6ZPcj0559yty7VTTXqv3BSU6jE2peay3COw%2BGmAC7NFV9ktC%2FSScdErvGFejlRqpl24A2yYLvwpTgJy2asZ31biLjhTSpIhi9HvepsacMLeGKFRXN34W0hX0BPBuh%2BEfWnuxs8vBU5cn4kooKWeUrsvlZvMcZ%2FuwdhLQsEY1%2Bi9IwACILyY%2FEzfuXY%2F%2BYWrMtDClx%2Be8BjqkAY6XNlAb1bzSFOHu9ndrJ8il2nb9QvYPcO9QbuovYKtbKwipEC2cC%2B6i0wqn1woZUIHv1EtTsPa4MGRcN6vRT6Lpdg9SzVZOGIcQk79WWcKOnmb4dt0Nir2bnz4D1nBBJ2UF%2BsDozxU7%2FXGj9t3BUkjY58wBOY3%2F0%2F15Mq6kGdNbsPs%2B0sCg5KrTK5JPTlKEyYncMzP67CZfSMzQMdXIZmUMydTD&X-Amz-Signature=37e4215658906f8f6778b466ff24bbbeee16db781e9bba191440057b11f04a12&X-Amz-SignedHeaders=host&x-id=GetObject)

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
