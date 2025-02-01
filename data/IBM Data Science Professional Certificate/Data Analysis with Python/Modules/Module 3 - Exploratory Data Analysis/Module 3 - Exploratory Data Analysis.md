

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKISAJAT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPD7qGrgFKN04%2BL3LUSzdaJuJ9blzl36fdPrnMVTTQaQIgNh9DTbLC2NnGLziEZwsCifPthvjcgRBS4m%2BVeTbh%2FR0qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEtJ%2BKxsvbfHmK%2FtCrcA%2F%2FMTlKWwy%2FfY0VjR9%2FNmdVc%2FeC11YlzsBZ3Dhr57i7zcPWxoFktlLGmoBQlriYQzuVe14JN5hGUTGwOeb9wvw1hE8oxTSpB8CI4o%2FUT%2BZjeFTzkB0brcWU0VhAcgKaENGAFQNRqhZxB5z5SEykWpYJcNyXgNcUXiFNn5ux2NOjlHLayTuaSCbfALcvZMJ43PtFrZ43exa0BAGyNDGL8ZjDrfd4H9zR5%2FYFOL1yZQksRBbxzBYT%2BV36udlg%2FMjJQMIz%2FnkRlMaN2YoDmUtwzEIrajY%2BAqKixHCtyfYh9FCjRYEwsy%2FksA7W6hMIGb%2FhCy9zJyUmXefr0e%2Bj26a4bvSNRZPV45NnD9QYxyuxFPedMV8AIZzDLmEByQSAZ2sZdORpI3lQi8kskXdVfuXhJfhCrUuxSex9h5ZFdw1khtUj8T%2BATQvfFjcS4yEb8%2FyyAOVv%2BWba8dghNcWgOWM5%2FUcpX%2BgqwhQulzfNvuSh3g4UpYIU%2B6RHmOjD3vkmuM8y9N%2BRvbU1cLUluN7CBVeKkp%2BCCRZtY956DmJseKrymoSf2acCJxJ%2FQRwB5IQkqIMDw4reTu5T1tm0yPT1P5ZfW338Ch2Ru7fjSOc%2Bk58QgOTSdEyrQ%2BzZXbHvhhCVxMKiU%2BrwGOqUBhhNyeMPBhGxnH56%2BG6JGNKSs2GNb6LT1jwEW8zxQgTUP6xmbqgwtbrQBTH8%2BYcYfeQ%2Fhicw93EYLzEh69hkdAjsoC2f%2BZxGPK2G6MBwygI6E9hV8PPT2j88ZqXemgtrFVHoX0I1Yu1TG3DXMxIAGyr8OkbrZQVdqo8hfIUnAKgKwLjH2DXCjeyQZgpooenfRo5%2FFjIbpLFoOPLhgfjfTPhJ%2FM%2Bdx&X-Amz-Signature=ae865546d317c30cf50274ff9a9eea8025f482c3e92ea6fd3195a3a2c7a105c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKISAJAT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPD7qGrgFKN04%2BL3LUSzdaJuJ9blzl36fdPrnMVTTQaQIgNh9DTbLC2NnGLziEZwsCifPthvjcgRBS4m%2BVeTbh%2FR0qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEtJ%2BKxsvbfHmK%2FtCrcA%2F%2FMTlKWwy%2FfY0VjR9%2FNmdVc%2FeC11YlzsBZ3Dhr57i7zcPWxoFktlLGmoBQlriYQzuVe14JN5hGUTGwOeb9wvw1hE8oxTSpB8CI4o%2FUT%2BZjeFTzkB0brcWU0VhAcgKaENGAFQNRqhZxB5z5SEykWpYJcNyXgNcUXiFNn5ux2NOjlHLayTuaSCbfALcvZMJ43PtFrZ43exa0BAGyNDGL8ZjDrfd4H9zR5%2FYFOL1yZQksRBbxzBYT%2BV36udlg%2FMjJQMIz%2FnkRlMaN2YoDmUtwzEIrajY%2BAqKixHCtyfYh9FCjRYEwsy%2FksA7W6hMIGb%2FhCy9zJyUmXefr0e%2Bj26a4bvSNRZPV45NnD9QYxyuxFPedMV8AIZzDLmEByQSAZ2sZdORpI3lQi8kskXdVfuXhJfhCrUuxSex9h5ZFdw1khtUj8T%2BATQvfFjcS4yEb8%2FyyAOVv%2BWba8dghNcWgOWM5%2FUcpX%2BgqwhQulzfNvuSh3g4UpYIU%2B6RHmOjD3vkmuM8y9N%2BRvbU1cLUluN7CBVeKkp%2BCCRZtY956DmJseKrymoSf2acCJxJ%2FQRwB5IQkqIMDw4reTu5T1tm0yPT1P5ZfW338Ch2Ru7fjSOc%2Bk58QgOTSdEyrQ%2BzZXbHvhhCVxMKiU%2BrwGOqUBhhNyeMPBhGxnH56%2BG6JGNKSs2GNb6LT1jwEW8zxQgTUP6xmbqgwtbrQBTH8%2BYcYfeQ%2Fhicw93EYLzEh69hkdAjsoC2f%2BZxGPK2G6MBwygI6E9hV8PPT2j88ZqXemgtrFVHoX0I1Yu1TG3DXMxIAGyr8OkbrZQVdqo8hfIUnAKgKwLjH2DXCjeyQZgpooenfRo5%2FFjIbpLFoOPLhgfjfTPhJ%2FM%2Bdx&X-Amz-Signature=a6e51766d1e104d54bccd822fb68d647623c9a3c26e61fedff1edc122d425339&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKISAJAT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPD7qGrgFKN04%2BL3LUSzdaJuJ9blzl36fdPrnMVTTQaQIgNh9DTbLC2NnGLziEZwsCifPthvjcgRBS4m%2BVeTbh%2FR0qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEEtJ%2BKxsvbfHmK%2FtCrcA%2F%2FMTlKWwy%2FfY0VjR9%2FNmdVc%2FeC11YlzsBZ3Dhr57i7zcPWxoFktlLGmoBQlriYQzuVe14JN5hGUTGwOeb9wvw1hE8oxTSpB8CI4o%2FUT%2BZjeFTzkB0brcWU0VhAcgKaENGAFQNRqhZxB5z5SEykWpYJcNyXgNcUXiFNn5ux2NOjlHLayTuaSCbfALcvZMJ43PtFrZ43exa0BAGyNDGL8ZjDrfd4H9zR5%2FYFOL1yZQksRBbxzBYT%2BV36udlg%2FMjJQMIz%2FnkRlMaN2YoDmUtwzEIrajY%2BAqKixHCtyfYh9FCjRYEwsy%2FksA7W6hMIGb%2FhCy9zJyUmXefr0e%2Bj26a4bvSNRZPV45NnD9QYxyuxFPedMV8AIZzDLmEByQSAZ2sZdORpI3lQi8kskXdVfuXhJfhCrUuxSex9h5ZFdw1khtUj8T%2BATQvfFjcS4yEb8%2FyyAOVv%2BWba8dghNcWgOWM5%2FUcpX%2BgqwhQulzfNvuSh3g4UpYIU%2B6RHmOjD3vkmuM8y9N%2BRvbU1cLUluN7CBVeKkp%2BCCRZtY956DmJseKrymoSf2acCJxJ%2FQRwB5IQkqIMDw4reTu5T1tm0yPT1P5ZfW338Ch2Ru7fjSOc%2Bk58QgOTSdEyrQ%2BzZXbHvhhCVxMKiU%2BrwGOqUBhhNyeMPBhGxnH56%2BG6JGNKSs2GNb6LT1jwEW8zxQgTUP6xmbqgwtbrQBTH8%2BYcYfeQ%2Fhicw93EYLzEh69hkdAjsoC2f%2BZxGPK2G6MBwygI6E9hV8PPT2j88ZqXemgtrFVHoX0I1Yu1TG3DXMxIAGyr8OkbrZQVdqo8hfIUnAKgKwLjH2DXCjeyQZgpooenfRo5%2FFjIbpLFoOPLhgfjfTPhJ%2FM%2Bdx&X-Amz-Signature=6a1d88b01b7736600dae3e007dd2a42db6a17654b1022a4c8d987ba670d46b27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQO2EZNY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq5IhDa8rTHxhK%2Bjek30vqrRGWHFOrl1i1o0%2F5%2F0IagAiEA1C%2B6Z1sk91m%2Fqsix3IPdzUyuylHECjdRxWUKC8hafx4qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB17m%2FfGwkZSV6M5dyrcAzM5J9I7%2BV23AXuVs2pk474%2FuiSSelyRIgA8XzNC%2FovZ3mh%2Bz8eSMbFu1f7yrN2QQWXxzwf%2FRsAWaumu9Ac4VdRLEe%2Bedo7rc6bmjUrDrHwqNXO9vTNIqJ8KfHa441Xd7nGG3XxMjO0LDGzQmYzEClBtQ4WR6TWCXUlpzyECVsemC3PhVtthGz%2Fz9Mamc1rs7ZxrBk4vQvmq6YvqvMJnj%2Fe%2ByqYhapNr0sth5VZ973viRfVfAFtu2Zki%2BWw%2BIU%2FA1JKXNARQw7B4IkCdbNbcydnq8FxgbjyG%2FR86BROD68%2FgVNG41r2xR36qhNsbYLbCoE29eD2wPvCV%2FFoXNRTgiKQosIrAmjBSYDrJbL3UsuGinUfpsH4wSEjaKotH63m6sEVwD0snVMnKJO32oyGC3%2BGZFdv0fjBiKHeObJPxBS79qa8tSbYDrhytgankxv3sAHufhjFgLsu3IUWCRxBHnKGk2VVXmbNQEoDuNoluM3O9Nn15R%2BBMh5cYg9q7S0TvYIP97t74UirBJMALEglFvqsB%2FRoIYCNhUf0s7c3lLlvjv%2FUU2LKlK%2FZw%2FQGZCtelS2x4c%2FKAmKOS%2FfOGuKx83P5shSUOyzO%2B%2Bs1OuU9cWYv5rrFGPEX%2FzOhc4pv8MJ2U%2BrwGOqUBAQ7Gb7FramiH%2BaBRxLjlUh3medk9%2FasF5Owzyj9A2otIXgMeqm2r9qvYjiUCMtWxPCUW7hySMQrlE8CX0KYHv00pxsW5HW8kydQmq2qoEkPcgpBOpgwC6X%2BMq1oxAVkWmKuyKio4kCUTq9ijbXTjsRl7hiWVaypugMM4vSL%2BahNJh55VDzNbaSDaw8Wq4rgAZbiy%2Bj4MVRp6cTq1GVul3UZlzg1b&X-Amz-Signature=74c01391033226246f3c1c810d923178c9c4f1572d3832380ad0aab760132554&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQO2EZNY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq5IhDa8rTHxhK%2Bjek30vqrRGWHFOrl1i1o0%2F5%2F0IagAiEA1C%2B6Z1sk91m%2Fqsix3IPdzUyuylHECjdRxWUKC8hafx4qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB17m%2FfGwkZSV6M5dyrcAzM5J9I7%2BV23AXuVs2pk474%2FuiSSelyRIgA8XzNC%2FovZ3mh%2Bz8eSMbFu1f7yrN2QQWXxzwf%2FRsAWaumu9Ac4VdRLEe%2Bedo7rc6bmjUrDrHwqNXO9vTNIqJ8KfHa441Xd7nGG3XxMjO0LDGzQmYzEClBtQ4WR6TWCXUlpzyECVsemC3PhVtthGz%2Fz9Mamc1rs7ZxrBk4vQvmq6YvqvMJnj%2Fe%2ByqYhapNr0sth5VZ973viRfVfAFtu2Zki%2BWw%2BIU%2FA1JKXNARQw7B4IkCdbNbcydnq8FxgbjyG%2FR86BROD68%2FgVNG41r2xR36qhNsbYLbCoE29eD2wPvCV%2FFoXNRTgiKQosIrAmjBSYDrJbL3UsuGinUfpsH4wSEjaKotH63m6sEVwD0snVMnKJO32oyGC3%2BGZFdv0fjBiKHeObJPxBS79qa8tSbYDrhytgankxv3sAHufhjFgLsu3IUWCRxBHnKGk2VVXmbNQEoDuNoluM3O9Nn15R%2BBMh5cYg9q7S0TvYIP97t74UirBJMALEglFvqsB%2FRoIYCNhUf0s7c3lLlvjv%2FUU2LKlK%2FZw%2FQGZCtelS2x4c%2FKAmKOS%2FfOGuKx83P5shSUOyzO%2B%2Bs1OuU9cWYv5rrFGPEX%2FzOhc4pv8MJ2U%2BrwGOqUBAQ7Gb7FramiH%2BaBRxLjlUh3medk9%2FasF5Owzyj9A2otIXgMeqm2r9qvYjiUCMtWxPCUW7hySMQrlE8CX0KYHv00pxsW5HW8kydQmq2qoEkPcgpBOpgwC6X%2BMq1oxAVkWmKuyKio4kCUTq9ijbXTjsRl7hiWVaypugMM4vSL%2BahNJh55VDzNbaSDaw8Wq4rgAZbiy%2Bj4MVRp6cTq1GVul3UZlzg1b&X-Amz-Signature=c2657dd9ce67000042ed3f4e4cc0632dcfaa27275f0d38b5b773d21920ae6a31&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQO2EZNY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq5IhDa8rTHxhK%2Bjek30vqrRGWHFOrl1i1o0%2F5%2F0IagAiEA1C%2B6Z1sk91m%2Fqsix3IPdzUyuylHECjdRxWUKC8hafx4qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB17m%2FfGwkZSV6M5dyrcAzM5J9I7%2BV23AXuVs2pk474%2FuiSSelyRIgA8XzNC%2FovZ3mh%2Bz8eSMbFu1f7yrN2QQWXxzwf%2FRsAWaumu9Ac4VdRLEe%2Bedo7rc6bmjUrDrHwqNXO9vTNIqJ8KfHa441Xd7nGG3XxMjO0LDGzQmYzEClBtQ4WR6TWCXUlpzyECVsemC3PhVtthGz%2Fz9Mamc1rs7ZxrBk4vQvmq6YvqvMJnj%2Fe%2ByqYhapNr0sth5VZ973viRfVfAFtu2Zki%2BWw%2BIU%2FA1JKXNARQw7B4IkCdbNbcydnq8FxgbjyG%2FR86BROD68%2FgVNG41r2xR36qhNsbYLbCoE29eD2wPvCV%2FFoXNRTgiKQosIrAmjBSYDrJbL3UsuGinUfpsH4wSEjaKotH63m6sEVwD0snVMnKJO32oyGC3%2BGZFdv0fjBiKHeObJPxBS79qa8tSbYDrhytgankxv3sAHufhjFgLsu3IUWCRxBHnKGk2VVXmbNQEoDuNoluM3O9Nn15R%2BBMh5cYg9q7S0TvYIP97t74UirBJMALEglFvqsB%2FRoIYCNhUf0s7c3lLlvjv%2FUU2LKlK%2FZw%2FQGZCtelS2x4c%2FKAmKOS%2FfOGuKx83P5shSUOyzO%2B%2Bs1OuU9cWYv5rrFGPEX%2FzOhc4pv8MJ2U%2BrwGOqUBAQ7Gb7FramiH%2BaBRxLjlUh3medk9%2FasF5Owzyj9A2otIXgMeqm2r9qvYjiUCMtWxPCUW7hySMQrlE8CX0KYHv00pxsW5HW8kydQmq2qoEkPcgpBOpgwC6X%2BMq1oxAVkWmKuyKio4kCUTq9ijbXTjsRl7hiWVaypugMM4vSL%2BahNJh55VDzNbaSDaw8Wq4rgAZbiy%2Bj4MVRp6cTq1GVul3UZlzg1b&X-Amz-Signature=ef2ad2bd7bba6d154996561c14fec6865fb9ad608f3aa51b0b660b2f91103b4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQO2EZNY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq5IhDa8rTHxhK%2Bjek30vqrRGWHFOrl1i1o0%2F5%2F0IagAiEA1C%2B6Z1sk91m%2Fqsix3IPdzUyuylHECjdRxWUKC8hafx4qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB17m%2FfGwkZSV6M5dyrcAzM5J9I7%2BV23AXuVs2pk474%2FuiSSelyRIgA8XzNC%2FovZ3mh%2Bz8eSMbFu1f7yrN2QQWXxzwf%2FRsAWaumu9Ac4VdRLEe%2Bedo7rc6bmjUrDrHwqNXO9vTNIqJ8KfHa441Xd7nGG3XxMjO0LDGzQmYzEClBtQ4WR6TWCXUlpzyECVsemC3PhVtthGz%2Fz9Mamc1rs7ZxrBk4vQvmq6YvqvMJnj%2Fe%2ByqYhapNr0sth5VZ973viRfVfAFtu2Zki%2BWw%2BIU%2FA1JKXNARQw7B4IkCdbNbcydnq8FxgbjyG%2FR86BROD68%2FgVNG41r2xR36qhNsbYLbCoE29eD2wPvCV%2FFoXNRTgiKQosIrAmjBSYDrJbL3UsuGinUfpsH4wSEjaKotH63m6sEVwD0snVMnKJO32oyGC3%2BGZFdv0fjBiKHeObJPxBS79qa8tSbYDrhytgankxv3sAHufhjFgLsu3IUWCRxBHnKGk2VVXmbNQEoDuNoluM3O9Nn15R%2BBMh5cYg9q7S0TvYIP97t74UirBJMALEglFvqsB%2FRoIYCNhUf0s7c3lLlvjv%2FUU2LKlK%2FZw%2FQGZCtelS2x4c%2FKAmKOS%2FfOGuKx83P5shSUOyzO%2B%2Bs1OuU9cWYv5rrFGPEX%2FzOhc4pv8MJ2U%2BrwGOqUBAQ7Gb7FramiH%2BaBRxLjlUh3medk9%2FasF5Owzyj9A2otIXgMeqm2r9qvYjiUCMtWxPCUW7hySMQrlE8CX0KYHv00pxsW5HW8kydQmq2qoEkPcgpBOpgwC6X%2BMq1oxAVkWmKuyKio4kCUTq9ijbXTjsRl7hiWVaypugMM4vSL%2BahNJh55VDzNbaSDaw8Wq4rgAZbiy%2Bj4MVRp6cTq1GVul3UZlzg1b&X-Amz-Signature=609a54d5d6ed187edaf6d35ce07dc629960fda3610354c63424983c4326c6b00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQO2EZNY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq5IhDa8rTHxhK%2Bjek30vqrRGWHFOrl1i1o0%2F5%2F0IagAiEA1C%2B6Z1sk91m%2Fqsix3IPdzUyuylHECjdRxWUKC8hafx4qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB17m%2FfGwkZSV6M5dyrcAzM5J9I7%2BV23AXuVs2pk474%2FuiSSelyRIgA8XzNC%2FovZ3mh%2Bz8eSMbFu1f7yrN2QQWXxzwf%2FRsAWaumu9Ac4VdRLEe%2Bedo7rc6bmjUrDrHwqNXO9vTNIqJ8KfHa441Xd7nGG3XxMjO0LDGzQmYzEClBtQ4WR6TWCXUlpzyECVsemC3PhVtthGz%2Fz9Mamc1rs7ZxrBk4vQvmq6YvqvMJnj%2Fe%2ByqYhapNr0sth5VZ973viRfVfAFtu2Zki%2BWw%2BIU%2FA1JKXNARQw7B4IkCdbNbcydnq8FxgbjyG%2FR86BROD68%2FgVNG41r2xR36qhNsbYLbCoE29eD2wPvCV%2FFoXNRTgiKQosIrAmjBSYDrJbL3UsuGinUfpsH4wSEjaKotH63m6sEVwD0snVMnKJO32oyGC3%2BGZFdv0fjBiKHeObJPxBS79qa8tSbYDrhytgankxv3sAHufhjFgLsu3IUWCRxBHnKGk2VVXmbNQEoDuNoluM3O9Nn15R%2BBMh5cYg9q7S0TvYIP97t74UirBJMALEglFvqsB%2FRoIYCNhUf0s7c3lLlvjv%2FUU2LKlK%2FZw%2FQGZCtelS2x4c%2FKAmKOS%2FfOGuKx83P5shSUOyzO%2B%2Bs1OuU9cWYv5rrFGPEX%2FzOhc4pv8MJ2U%2BrwGOqUBAQ7Gb7FramiH%2BaBRxLjlUh3medk9%2FasF5Owzyj9A2otIXgMeqm2r9qvYjiUCMtWxPCUW7hySMQrlE8CX0KYHv00pxsW5HW8kydQmq2qoEkPcgpBOpgwC6X%2BMq1oxAVkWmKuyKio4kCUTq9ijbXTjsRl7hiWVaypugMM4vSL%2BahNJh55VDzNbaSDaw8Wq4rgAZbiy%2Bj4MVRp6cTq1GVul3UZlzg1b&X-Amz-Signature=0b2677a62748a812abce243a2e735dd109fd4277059fdcb24152d3cd19eef92a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQO2EZNY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq5IhDa8rTHxhK%2Bjek30vqrRGWHFOrl1i1o0%2F5%2F0IagAiEA1C%2B6Z1sk91m%2Fqsix3IPdzUyuylHECjdRxWUKC8hafx4qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB17m%2FfGwkZSV6M5dyrcAzM5J9I7%2BV23AXuVs2pk474%2FuiSSelyRIgA8XzNC%2FovZ3mh%2Bz8eSMbFu1f7yrN2QQWXxzwf%2FRsAWaumu9Ac4VdRLEe%2Bedo7rc6bmjUrDrHwqNXO9vTNIqJ8KfHa441Xd7nGG3XxMjO0LDGzQmYzEClBtQ4WR6TWCXUlpzyECVsemC3PhVtthGz%2Fz9Mamc1rs7ZxrBk4vQvmq6YvqvMJnj%2Fe%2ByqYhapNr0sth5VZ973viRfVfAFtu2Zki%2BWw%2BIU%2FA1JKXNARQw7B4IkCdbNbcydnq8FxgbjyG%2FR86BROD68%2FgVNG41r2xR36qhNsbYLbCoE29eD2wPvCV%2FFoXNRTgiKQosIrAmjBSYDrJbL3UsuGinUfpsH4wSEjaKotH63m6sEVwD0snVMnKJO32oyGC3%2BGZFdv0fjBiKHeObJPxBS79qa8tSbYDrhytgankxv3sAHufhjFgLsu3IUWCRxBHnKGk2VVXmbNQEoDuNoluM3O9Nn15R%2BBMh5cYg9q7S0TvYIP97t74UirBJMALEglFvqsB%2FRoIYCNhUf0s7c3lLlvjv%2FUU2LKlK%2FZw%2FQGZCtelS2x4c%2FKAmKOS%2FfOGuKx83P5shSUOyzO%2B%2Bs1OuU9cWYv5rrFGPEX%2FzOhc4pv8MJ2U%2BrwGOqUBAQ7Gb7FramiH%2BaBRxLjlUh3medk9%2FasF5Owzyj9A2otIXgMeqm2r9qvYjiUCMtWxPCUW7hySMQrlE8CX0KYHv00pxsW5HW8kydQmq2qoEkPcgpBOpgwC6X%2BMq1oxAVkWmKuyKio4kCUTq9ijbXTjsRl7hiWVaypugMM4vSL%2BahNJh55VDzNbaSDaw8Wq4rgAZbiy%2Bj4MVRp6cTq1GVul3UZlzg1b&X-Amz-Signature=597975d5bba7905597ee294befe8bc70deb5abb061e3e87c577d266b59cc29e3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZD4YIHL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0g2KtATa1xdulnbUeP6rOelkANftIxtl8nGB18upiwwIhAKFjtVjJk%2Bfq64NRPoqA9mLAnELzaR%2BqEqZrmh70tgORKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjeEP2E3RGdtGFR3oq3AP6M5Xz6gSGsCBoXaZTXaQp690hgr1jmGPkLUm1cGrQS2kFevnF8ehT%2FJ53Z1LeqLRj7wzKwmPXHRFOjG2LIDDSh%2B1NExeSBC9bfIy5Dk6QV6%2B2ySNMHGG1nCFAfTLmSk7NjWw9sXC1RYPAsRMXbpNpAA414V%2FHB6YTYtTk2Qf9NH9xaX1gfvgCwgdezDUGVSnF9lA1iM980nwKNMkfQZvHFJ6okApr%2FaVrq1OYiELoYgMr6ETg5BjzdfGl4Mt0qFN0bFCqmfjqsSski3qdxEE1zk%2FVHVW56YxYxZvVoQzTykMDAXthlo0zoLOP7IhX%2BHyP84hS1NACLDagOFezaDwteRAlzbxx5x%2BEt9HgVVWkvDO2JH1IVwBG0yEW6d0jSYPHh7W6eTnwOlsDKKMza%2BN47tPzR%2FvrpQOFP5KNUr96vos1UcENljEVeWybrIukZVUC01SER0bfBeSzdLHjPldm%2F0eH%2B3nlsP6DYuOr7v4KIffMXjG9T0XF5R3yW28bz%2FFopotHqJQOu7xLhEBH1rEo2LM%2FWPC0Up3fejuxP4gdufPiMeVjqqx1wejGx13cZ%2BuF6pdsPyVEnr931FkVQbmRE6oJT2NrVSWmmGw8dgkuuBResT214OGvchAvnDCelPq8BjqkAU5YHBVOOTeN1W3Jc%2FRbIyl1vTmR6OwsmOhULeqFW3GXK1B%2Fme0d4pv7M9j5eT%2FaaQ9qlgM9zM6ZVeLEZSPZEMuE6nMFAyV6EctDol3oklaSZOpZeyh70EyWCozBG7mLqMSDYStlG79KbPRBZXyKMN8joX2vOPwnNNlPQGVdgHlgDXzMfaOdr5jXx3gShY2CpLgkVT%2B5ZhfXB5xZTFCZ11FYmg7P&X-Amz-Signature=13657c5be5496be0fe4313c27faf77594d1ec42cac87a1f448ef8dd588fd7b48&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNTVTKS7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF3dnmENs3cHZL1ZL20IBdBvHSeDOPdUhWLJ0mQ7bk0JAiBezgnzpinLs7WLaBI9QSlwf6Rg55NhsiSP5kc6mKNCZCqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiA1SvPELFWbyW%2F07KtwDQe827aHiXiHCiUSYKn2wYOBRY7nsM0Bb9DamIm0Ia51hGO7ywB6sgCvaK9Yck0szBbBwojKM%2F7dCtmitItqBIBx46i6HOfeWG4GXrf9yqaQzec86LSoVqMSLDU6yOR55YJZU%2F7SN2sUYFLLfjYb3pjs8Uky2HxV6pLAeXPTJQWgXBUQsIWFWBlzWtvUEFuxgdU%2F1z3Q5qsL5g26z7%2FtgNv1YVqn%2Fwe0BQtv5KHwzLUBNnCkgHMTvjOCo46LdlvCu1LNoow4QBGLCXmx%2FSCAKJRMyOYd%2F4lmas%2FBM2kEOLo4crDwL7A%2BA%2FhUIp5TjX00%2BLiCl3Xn38He4TmVkr8mCifaNvKHEDJkkyRk%2BaJ43Vix5e%2BPAoohUkTy%2F5ewtYKlfTeWxYT4Cd9qkh8hiw8S52K32lcEX%2Ba8wRzP8YxJnPc6rfHQBEGaxsUvG%2BxxycqS7fLTwgy%2FNDRvUqZHEd76oPqV9U4RUE%2BBF%2B6z1zc8kgEldS3eQA%2F%2Fu9eqa%2Bj1ahxJqhl8%2FwvR9ycFnMjkQQR9DHB3x737wq6QpW18427%2FaR%2FvairHdb7J%2BEfSSNi0hSGiTR4VCVT77icNkDkXh1izUgAvQar5ulW9Qmv8jllP2HTDXbMWXxZOHINzBu7swoJT6vAY6pgFXiVFUH8aBb%2FFKKdFWac3xJ983ajHog9n%2BW%2FFc2ZHtzQaJHV8eMhPP1p8SDku0A3feAcJt24YHmaPY2CIvR0jireg6wiCriNDKM4xAQRj85jFurElA9fcq30pezArFXoXV2tgWEQvmKgA%2By2ZgkFHT0oFP%2BqDJPk9HHQbi3B6qQarWm%2BlooMnqO7EzrntmFIOMzJGx%2Fho9WlNw3VI5VElKNgHamDOP&X-Amz-Signature=683e6022d4a8194c05f14a1e8b7ffff13a98b75857abe7bb949f1db1d5ce1323&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQO2EZNY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq5IhDa8rTHxhK%2Bjek30vqrRGWHFOrl1i1o0%2F5%2F0IagAiEA1C%2B6Z1sk91m%2Fqsix3IPdzUyuylHECjdRxWUKC8hafx4qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB17m%2FfGwkZSV6M5dyrcAzM5J9I7%2BV23AXuVs2pk474%2FuiSSelyRIgA8XzNC%2FovZ3mh%2Bz8eSMbFu1f7yrN2QQWXxzwf%2FRsAWaumu9Ac4VdRLEe%2Bedo7rc6bmjUrDrHwqNXO9vTNIqJ8KfHa441Xd7nGG3XxMjO0LDGzQmYzEClBtQ4WR6TWCXUlpzyECVsemC3PhVtthGz%2Fz9Mamc1rs7ZxrBk4vQvmq6YvqvMJnj%2Fe%2ByqYhapNr0sth5VZ973viRfVfAFtu2Zki%2BWw%2BIU%2FA1JKXNARQw7B4IkCdbNbcydnq8FxgbjyG%2FR86BROD68%2FgVNG41r2xR36qhNsbYLbCoE29eD2wPvCV%2FFoXNRTgiKQosIrAmjBSYDrJbL3UsuGinUfpsH4wSEjaKotH63m6sEVwD0snVMnKJO32oyGC3%2BGZFdv0fjBiKHeObJPxBS79qa8tSbYDrhytgankxv3sAHufhjFgLsu3IUWCRxBHnKGk2VVXmbNQEoDuNoluM3O9Nn15R%2BBMh5cYg9q7S0TvYIP97t74UirBJMALEglFvqsB%2FRoIYCNhUf0s7c3lLlvjv%2FUU2LKlK%2FZw%2FQGZCtelS2x4c%2FKAmKOS%2FfOGuKx83P5shSUOyzO%2B%2Bs1OuU9cWYv5rrFGPEX%2FzOhc4pv8MJ2U%2BrwGOqUBAQ7Gb7FramiH%2BaBRxLjlUh3medk9%2FasF5Owzyj9A2otIXgMeqm2r9qvYjiUCMtWxPCUW7hySMQrlE8CX0KYHv00pxsW5HW8kydQmq2qoEkPcgpBOpgwC6X%2BMq1oxAVkWmKuyKio4kCUTq9ijbXTjsRl7hiWVaypugMM4vSL%2BahNJh55VDzNbaSDaw8Wq4rgAZbiy%2Bj4MVRp6cTq1GVul3UZlzg1b&X-Amz-Signature=791916a3fc9a7c6cdbcfada3f0581e2c4013cb8f1899b2164857e14b4d9ea45f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQO2EZNY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq5IhDa8rTHxhK%2Bjek30vqrRGWHFOrl1i1o0%2F5%2F0IagAiEA1C%2B6Z1sk91m%2Fqsix3IPdzUyuylHECjdRxWUKC8hafx4qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB17m%2FfGwkZSV6M5dyrcAzM5J9I7%2BV23AXuVs2pk474%2FuiSSelyRIgA8XzNC%2FovZ3mh%2Bz8eSMbFu1f7yrN2QQWXxzwf%2FRsAWaumu9Ac4VdRLEe%2Bedo7rc6bmjUrDrHwqNXO9vTNIqJ8KfHa441Xd7nGG3XxMjO0LDGzQmYzEClBtQ4WR6TWCXUlpzyECVsemC3PhVtthGz%2Fz9Mamc1rs7ZxrBk4vQvmq6YvqvMJnj%2Fe%2ByqYhapNr0sth5VZ973viRfVfAFtu2Zki%2BWw%2BIU%2FA1JKXNARQw7B4IkCdbNbcydnq8FxgbjyG%2FR86BROD68%2FgVNG41r2xR36qhNsbYLbCoE29eD2wPvCV%2FFoXNRTgiKQosIrAmjBSYDrJbL3UsuGinUfpsH4wSEjaKotH63m6sEVwD0snVMnKJO32oyGC3%2BGZFdv0fjBiKHeObJPxBS79qa8tSbYDrhytgankxv3sAHufhjFgLsu3IUWCRxBHnKGk2VVXmbNQEoDuNoluM3O9Nn15R%2BBMh5cYg9q7S0TvYIP97t74UirBJMALEglFvqsB%2FRoIYCNhUf0s7c3lLlvjv%2FUU2LKlK%2FZw%2FQGZCtelS2x4c%2FKAmKOS%2FfOGuKx83P5shSUOyzO%2B%2Bs1OuU9cWYv5rrFGPEX%2FzOhc4pv8MJ2U%2BrwGOqUBAQ7Gb7FramiH%2BaBRxLjlUh3medk9%2FasF5Owzyj9A2otIXgMeqm2r9qvYjiUCMtWxPCUW7hySMQrlE8CX0KYHv00pxsW5HW8kydQmq2qoEkPcgpBOpgwC6X%2BMq1oxAVkWmKuyKio4kCUTq9ijbXTjsRl7hiWVaypugMM4vSL%2BahNJh55VDzNbaSDaw8Wq4rgAZbiy%2Bj4MVRp6cTq1GVul3UZlzg1b&X-Amz-Signature=d3373b7e5d13d6e830ded81ad8c67a49899bed8b61e4ba06f1f2642ef3ff8ab8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQO2EZNY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEq5IhDa8rTHxhK%2Bjek30vqrRGWHFOrl1i1o0%2F5%2F0IagAiEA1C%2B6Z1sk91m%2Fqsix3IPdzUyuylHECjdRxWUKC8hafx4qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB17m%2FfGwkZSV6M5dyrcAzM5J9I7%2BV23AXuVs2pk474%2FuiSSelyRIgA8XzNC%2FovZ3mh%2Bz8eSMbFu1f7yrN2QQWXxzwf%2FRsAWaumu9Ac4VdRLEe%2Bedo7rc6bmjUrDrHwqNXO9vTNIqJ8KfHa441Xd7nGG3XxMjO0LDGzQmYzEClBtQ4WR6TWCXUlpzyECVsemC3PhVtthGz%2Fz9Mamc1rs7ZxrBk4vQvmq6YvqvMJnj%2Fe%2ByqYhapNr0sth5VZ973viRfVfAFtu2Zki%2BWw%2BIU%2FA1JKXNARQw7B4IkCdbNbcydnq8FxgbjyG%2FR86BROD68%2FgVNG41r2xR36qhNsbYLbCoE29eD2wPvCV%2FFoXNRTgiKQosIrAmjBSYDrJbL3UsuGinUfpsH4wSEjaKotH63m6sEVwD0snVMnKJO32oyGC3%2BGZFdv0fjBiKHeObJPxBS79qa8tSbYDrhytgankxv3sAHufhjFgLsu3IUWCRxBHnKGk2VVXmbNQEoDuNoluM3O9Nn15R%2BBMh5cYg9q7S0TvYIP97t74UirBJMALEglFvqsB%2FRoIYCNhUf0s7c3lLlvjv%2FUU2LKlK%2FZw%2FQGZCtelS2x4c%2FKAmKOS%2FfOGuKx83P5shSUOyzO%2B%2Bs1OuU9cWYv5rrFGPEX%2FzOhc4pv8MJ2U%2BrwGOqUBAQ7Gb7FramiH%2BaBRxLjlUh3medk9%2FasF5Owzyj9A2otIXgMeqm2r9qvYjiUCMtWxPCUW7hySMQrlE8CX0KYHv00pxsW5HW8kydQmq2qoEkPcgpBOpgwC6X%2BMq1oxAVkWmKuyKio4kCUTq9ijbXTjsRl7hiWVaypugMM4vSL%2BahNJh55VDzNbaSDaw8Wq4rgAZbiy%2Bj4MVRp6cTq1GVul3UZlzg1b&X-Amz-Signature=24dd1ead54ee672d4a25847e52c9b834679466c2d9f34de0b5f1d664ee519dc6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663D7SJSG2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCDeTsYdW5azcXPIo8NVSpTpiqnlCWao2lhSgP%2FMHnE5AIhAMOprirdM2we0iDHH2Vnpq6ESRvUYVifkngZiTSAIb%2F7KogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFi%2BBHZgEhKpSFfBQq3AOiPVPh6g%2F4qgp4qCWQ1QxRLWYB3eQbbf5iXXO1ZQci4N5GDFnJ1etsST%2FtXBbttpZ5rIagCdV%2F3pUU4vo5qWYTucf%2BuDspVZY8tORjGmUzhNEiCma%2BKWoHAc2vy93intMZQebNJ%2FNEwHyDFBjvND3vUpkhpME6%2F6gcrxyF%2BJ5cD%2BSLjWDCK4gu7tnhjYCuOxyZ1R38QBqaAQU%2BHscJ147TQhFzR5qcOB1j%2Fza%2F0oQNsdvHgItupknidXSCJJQquZj%2Bi04S1qKdeE8FOfezC%2BpXGkv1xLD803xx7KICiLvuc0vCa3QhhVnFyvJWETDKoYXtt3OCQSO3yi5j9Wjot%2BAxhMRF5r63jMlw5nTDbR2His3nalMGNu%2Bo77q00f1daO7Hk0Ed8cD8GxYoB%2F2Nouai1sbikd674Ib32ZnGPzXaKmtAgw2PjUvfWXVGpZeUREm1BXe1EcbttR6Bi388sdZCrlLUGskvMUvPj2VehqU3p5N99ORbJ%2BoFuXuhvst0%2F%2FYs8IpqweEa%2BXnd%2FkLAl33w7CKeczL4DW17PeIW5%2FxuQHh3c4VcIui4f3cRcokIH9wsUuDs2sswEqZvojSvj5ZdtoO3B52oIfXqPrkyiCLIYwaSfvYnjM79VZvP4jD1k%2Fq8BjqkAWblGM3Tlkyi6hei0vX6EQiBWB5pB5rlUsJBeWQvBo3wVVvBkXG8yPrZUyh9mCJjenaVl%2FA9sOINcE%2F1j%2B72IAT1wp312HM5soBMvOuvs75uXJ0ior4VkZkeKluZAMyGSstlM9zOD7n%2FLjZHsSk9%2FJmrQWBsdIsiz60O0U9OxSoxbBBed9cFyspf9JcQgFm5fOA1n%2B%2BU9zaRJJKVfTIZ3qzAOzRT&X-Amz-Signature=bda9a9c0b004f50f28abe34383599a84fdee45a31cdd9d767a349bbdd01f7606&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUNVY2VI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7UzPQxYyXEtqenZcaytOwvaJAgG%2BQQxAhINA3SEo3CwIhAJvTpgsLVft%2BLJ422yS1QoNHRRnkK7d%2BkztJ62m6rJEOKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfmqgAdBOaIyuJZWcq3ANl3rCRcjwLN4N8BuoGhgVePwqKso%2BLZERAegNzDXgWS%2B1qMn9UWEl9xVszTTZJCUIFpXwmVh%2BMwitBqPuaNA0Z6iWrPzaOVRa1d4WTRuY2E9GJlGyn5cKR4scH7JNJV5aqww72%2FixrqF%2Fd7g8kNYciWOtmEMSangoeNf3HNdJ%2Bwfnb1XOHBtT4HV0Drjcmeglug%2BIzslBBarTez9fUCF%2BrmeP53Snxbu5LX8EwNT%2BsQF5pkN4W4QFadk0zQyvhy6J6X2nXYtJCLFLSnbwKgZQVcyFtK2SVYUBlPERmUTpg6jPxIB72xEydf9G3WojOU5RskmQ67sfQDed7eZ4VjQSYPcyaW8wnnBG1vu%2FePQ3cVYD6is%2FPAq2GxxIEG9OOEi%2FOpJAbbKpFCPuQmm9wJuzG9JdBISio7naRNSE4y19nNmDXcDYf0wzi8qBOjs%2BboO2HUruNwQsNQ6piWJrKXAZkN7j4MzzMA%2BhYz%2BkxrnGvEsM3puCkZ1lweWrXGMR%2BnfRivaINjpmzn0XBvUSe%2BlQfs%2FPcGRtc1Ty2mPwBgPJA4sVWbIHgpA8An%2BFU0wg6qGj4TVtROj%2BOKLGqn%2BPhszLzFgRpBzOQGvPwpmxKGy6CWVAbzWcu9SE52oVg3TDYk%2Fq8BjqkAXO6Uh85vdSSkBhYfv0DrCveiIEhWDlUqnGONriRlZv3Abc5lCaP4EhWz8PfVKwfcyu7Usd57xOn8kB%2FFy8rgfuj3%2Fjeh5qApPhqGYKPLGjWyl8oqVKg74jQKwNs7%2BxbOhehZECT23%2FLf8OO7bnR3qFeR3tPbalDiB6Q7jd61P7IxvfWnOsnlj98ny3TOdRIpyeSpWq%2FgcJp6pj10FiIaFccnMh4&X-Amz-Signature=60a117cdcfb5ec202702c82cdfde3404bcac3f22200f928ca3d2e67f22ac67ad&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRID3OTW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDq4za6ot2ngEjdc9h6A3VTs0vciWNmjDDDBkf32D%2BnPwIhAJi5i46jjGUvrqGM5pzL4wZqK%2BZas%2B2WJtoz8ME3LopSKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRumcU1ffRTqsSrLoq3AP1CkYWpAUAaWSEprV4GmKrMTfUi4zR%2FPLjWedaKc4lZJ80CpQ9xL9%2FKhXsigSvG3r8aNRmVT3wGW5XrcHGCfSYLJrubRxZOpIT9Xd0%2BwlaThs3ONpaUdfL52HNMnVV6ByrlJrLrcuIycEC0qWx0HYo8C%2FRd0zBzQD1l6SNocBbftCqdlxdGFdHPqkvr8wgPmTTMTN%2F5%2FrxxzFUJ8WwFuwTVD3dzeyXgET8NOj9MXwfACkdnCnYcoR2JZNwfb75vCJA2P%2BO1wvYH%2F1HC7lszdzeox%2BGxvOtVcYdbka0GV6dJXo6%2Bt4ZbYyttAgX9hSgdal1RsprGOBdoxT%2BNy72K9ZbmXRRT0%2B4ynXKzOzBO8y%2BXvltkzSyZIHflsYzPxfu%2Fg0kFGqKeuudJ%2F6l6iTNiq0TIik72TwQAZC116AD8aqZAyct%2FZzACNbkGtekHtVRSgRB8TwXIkN3X04t6cZ8Tj064lwvGuv%2FBPHgLg82ttL%2BtoFSB%2FV%2BbP3fCUBxfpH2lxZhOEgecAO%2Fc5JXKrq%2BxtyhVUAE2KujHhgpcc72W4VRvjhxiZ%2BTjkZX%2BbIGQiO%2FYQYTu4buW3hEKOB3uZyzegjKg47y0aKlmc1CUziv2sV9H97d46ckKXubDZy9rzCHlPq8BjqkAQESbtUF%2BqtwEyCEPsCHc2TwEH3qUchzX6Fptbvj5gtAl%2Bexc3KQ7SzqLqhOgLf%2FuXTxNgkWoxd2slAoPqsqQhNNxU625ft7LAu68PDfGtkcRoYLW07ioOAhURa4sfA8ZrX2ojCDVm%2FfrENTwONdSBj7iMr0LHmNHsn5L%2FWt9bUxi0nUmJQlXWwfON9gAmyCem7stQnJnpKm09IlVaBdpEfi%2FYfB&X-Amz-Signature=44bb83c0293b05a7af35789fcdfd01ef7188a6e91a020e79d6ef708c5d9197e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VG2N32H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEterHKQPe%2F%2BlGtNSOx9aJBAjeBIVyqDRzpkGDt6LUvAIgK4CeJgWsX7kd6MG%2BSHbiO%2BDwWzq7bJCclEshTCjCU%2F0qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNq8yGkZYa%2BfhItH1ircA1hi40L%2BFAnGP8CmNHZT3A8aqHGwcZirWSZhp0AILx8cHpgKCx0CtyszrmAfUGEm3clXm3tXx%2FANkHIVy%2FneuBMs1u%2BDuoVdeBnzGUM3jfs1TT7zrQq7I3ajcikVorUBDeadXixBKEDLvlnmRBb3TYsg%2FhPSBIJHRnjdBqkRtIZMveL1yPmLn%2F37TxsiAzmRBTVMlz3w31CLsAaS2fARk82uLduhwlg02t%2BwMs3gnoD%2F27cypOAVBZvUKFFWJ%2Fa%2By6WFVbyMBFTjU8B85MAEm549Eha62rVKpGSe4kyldsaZaoMRPeuwcIK5%2FBu%2BstbvEm1lDkpVH%2Fg2mE4HkOkpBauiA%2BcS8GdeebBlVMOwwR9%2FMP1KRHZX8QZK4PH%2BIFDw3oZANuwrDYcxkNCnWYnhlQsDgIS9HMtv89bPtp5zZilLQVOi6hiEz1Lu32EunO8RCV3jQwRbhTSH7BB62zwkXtDs2cRIws%2B31dTkILjaXYHlmqhsZ%2Frl9dK6yyWH40Do9jDkcY9VfReNc5Z9oXnXGcuHN9IdrQe0Y%2BpaldhOJyIgG8uuf%2FWYQ9gRSHpzse367xTYPJENk7WKDEyOI%2B3bpR4pFz7T5x2qXclA%2Bix4QbFAkVbPNE7I0B33wdV9MJ2U%2BrwGOqUBiyeXGITP25pnuIJ1ET5G7FtIKMGtKDn9ZL7L79MCCZCNxs%2BbW7TVfLp5HEvV1FCKtrCpO3SnKBybM4SUJmJ8J73kXGeIA7HF4%2BHxlYJz7%2FoeydOy29CIIcHEw4%2BG8h%2BPPhVyWMILfJamnRr6iYK6GhNuaIoE%2B7x9m7hB5T6diHUga09vnEsQCWevNbeADFrNWqJHUclO9seangb%2Fv9VP5n%2FG2ukl&X-Amz-Signature=b93e2128c007fcaf040f67371782780276c93dbb0d9d5c5c44f5ff226e738698&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VG2N32H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEterHKQPe%2F%2BlGtNSOx9aJBAjeBIVyqDRzpkGDt6LUvAIgK4CeJgWsX7kd6MG%2BSHbiO%2BDwWzq7bJCclEshTCjCU%2F0qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNq8yGkZYa%2BfhItH1ircA1hi40L%2BFAnGP8CmNHZT3A8aqHGwcZirWSZhp0AILx8cHpgKCx0CtyszrmAfUGEm3clXm3tXx%2FANkHIVy%2FneuBMs1u%2BDuoVdeBnzGUM3jfs1TT7zrQq7I3ajcikVorUBDeadXixBKEDLvlnmRBb3TYsg%2FhPSBIJHRnjdBqkRtIZMveL1yPmLn%2F37TxsiAzmRBTVMlz3w31CLsAaS2fARk82uLduhwlg02t%2BwMs3gnoD%2F27cypOAVBZvUKFFWJ%2Fa%2By6WFVbyMBFTjU8B85MAEm549Eha62rVKpGSe4kyldsaZaoMRPeuwcIK5%2FBu%2BstbvEm1lDkpVH%2Fg2mE4HkOkpBauiA%2BcS8GdeebBlVMOwwR9%2FMP1KRHZX8QZK4PH%2BIFDw3oZANuwrDYcxkNCnWYnhlQsDgIS9HMtv89bPtp5zZilLQVOi6hiEz1Lu32EunO8RCV3jQwRbhTSH7BB62zwkXtDs2cRIws%2B31dTkILjaXYHlmqhsZ%2Frl9dK6yyWH40Do9jDkcY9VfReNc5Z9oXnXGcuHN9IdrQe0Y%2BpaldhOJyIgG8uuf%2FWYQ9gRSHpzse367xTYPJENk7WKDEyOI%2B3bpR4pFz7T5x2qXclA%2Bix4QbFAkVbPNE7I0B33wdV9MJ2U%2BrwGOqUBiyeXGITP25pnuIJ1ET5G7FtIKMGtKDn9ZL7L79MCCZCNxs%2BbW7TVfLp5HEvV1FCKtrCpO3SnKBybM4SUJmJ8J73kXGeIA7HF4%2BHxlYJz7%2FoeydOy29CIIcHEw4%2BG8h%2BPPhVyWMILfJamnRr6iYK6GhNuaIoE%2B7x9m7hB5T6diHUga09vnEsQCWevNbeADFrNWqJHUclO9seangb%2Fv9VP5n%2FG2ukl&X-Amz-Signature=a723a65881db93d382739430977bdc391cd2ef54b80e82d1f0b72673e58bbf80&X-Amz-SignedHeaders=host&x-id=GetObject)

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
