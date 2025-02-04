

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5U3EGYO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIHHghrMLvIYywDvmprRr7JPjBkXfXFkWvBC%2Bm5aVZUAGAiBKHPm0eI%2B8GGZjze5s4Z2%2BcH8d20nADOBrtJuL7hPG7Sr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIM0jfLgrRIn920pZFVKtwD4N718VLywt6ZGV2B6F%2B0lpFtABIArIZXlTOvxuPShcFKaxvpEVk7K2nYdAGDl31o%2FdCdgFoKhE%2F61QjzZax4BZ%2F2X9LlgQj7ZxB9S9d3H3yPJ2pJd6m%2FfD5pk13qlqpASA6mu8ePyVMGrvl1lTJx%2FNci4juqal3%2BxfN6eNZTPA78%2BFKIe4QV%2FvWklXWrnmpmvhwVrcm3ydvhC8nJc0Tr6cuzgoOUrUtnSoiNHnlZN2ejOl2MR1rURXqjcLLgBfvgNsNBydbyLae5v3clbeHztxA3VcAXvBEaZRAqXnY7ENHzAMuRxStoLatBqgtHKjzOFwjttE3%2FxCLNACGUgYQhBrbuGSRLewyKFXFyjFkHkSW6R7GEZI2kYz0fuYDZbnzzTOkmxRnPH1mLzl9O0meZiMrGV9pgc1yjo%2FtFYon4Ll0OwlNgi5nfUSoCEieXdPjgTwTW1%2FIbyAwyMmrOioQ5t3QZJTZKmCpefqB%2BSAHnG0sn9lFvVY2d5hGt%2F2RzWBskLfypLNkB3jIuH71LDKTnKB2IR70nDxyYq0A0uhTjyuFAUXkHMR3TkRLL0XDe%2Bsxa697YPljsxNJbi630CEEhBvVLva7nxWScYotaIPbC1%2Br3wHhtm2jdPiSYULQwm4SJvQY6pgErMfU07S7jxg%2FbZNA31UjOCEpsuwn0v72cEY%2FNstI4YxK0e9gwSOHs0hdNvCkUCT0KyIImnwLpY1nGTdKwByeqN0JK71Q8US4rkrHCgDx4jiMr0Cyqm4o%2BCDTnyW7qE6zse7jwB6huOpfI4%2FnDdyLizPSqv7028cel44W00uZKQmqXVOsYhhcJzQf0t4ycq7t%2FHalfcVWK5VK2g0HiSsnd2Buatqxb&X-Amz-Signature=1c1568ef8708044666885fbfcba6903d54d956c564a3d0c7036eeb5304d72b5c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5U3EGYO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIHHghrMLvIYywDvmprRr7JPjBkXfXFkWvBC%2Bm5aVZUAGAiBKHPm0eI%2B8GGZjze5s4Z2%2BcH8d20nADOBrtJuL7hPG7Sr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIM0jfLgrRIn920pZFVKtwD4N718VLywt6ZGV2B6F%2B0lpFtABIArIZXlTOvxuPShcFKaxvpEVk7K2nYdAGDl31o%2FdCdgFoKhE%2F61QjzZax4BZ%2F2X9LlgQj7ZxB9S9d3H3yPJ2pJd6m%2FfD5pk13qlqpASA6mu8ePyVMGrvl1lTJx%2FNci4juqal3%2BxfN6eNZTPA78%2BFKIe4QV%2FvWklXWrnmpmvhwVrcm3ydvhC8nJc0Tr6cuzgoOUrUtnSoiNHnlZN2ejOl2MR1rURXqjcLLgBfvgNsNBydbyLae5v3clbeHztxA3VcAXvBEaZRAqXnY7ENHzAMuRxStoLatBqgtHKjzOFwjttE3%2FxCLNACGUgYQhBrbuGSRLewyKFXFyjFkHkSW6R7GEZI2kYz0fuYDZbnzzTOkmxRnPH1mLzl9O0meZiMrGV9pgc1yjo%2FtFYon4Ll0OwlNgi5nfUSoCEieXdPjgTwTW1%2FIbyAwyMmrOioQ5t3QZJTZKmCpefqB%2BSAHnG0sn9lFvVY2d5hGt%2F2RzWBskLfypLNkB3jIuH71LDKTnKB2IR70nDxyYq0A0uhTjyuFAUXkHMR3TkRLL0XDe%2Bsxa697YPljsxNJbi630CEEhBvVLva7nxWScYotaIPbC1%2Br3wHhtm2jdPiSYULQwm4SJvQY6pgErMfU07S7jxg%2FbZNA31UjOCEpsuwn0v72cEY%2FNstI4YxK0e9gwSOHs0hdNvCkUCT0KyIImnwLpY1nGTdKwByeqN0JK71Q8US4rkrHCgDx4jiMr0Cyqm4o%2BCDTnyW7qE6zse7jwB6huOpfI4%2FnDdyLizPSqv7028cel44W00uZKQmqXVOsYhhcJzQf0t4ycq7t%2FHalfcVWK5VK2g0HiSsnd2Buatqxb&X-Amz-Signature=6fb4454fcdf0fa19769fabb620c157f24c15cb917ccc99e9e0f182630d7dc773&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5U3EGYO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIHHghrMLvIYywDvmprRr7JPjBkXfXFkWvBC%2Bm5aVZUAGAiBKHPm0eI%2B8GGZjze5s4Z2%2BcH8d20nADOBrtJuL7hPG7Sr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIM0jfLgrRIn920pZFVKtwD4N718VLywt6ZGV2B6F%2B0lpFtABIArIZXlTOvxuPShcFKaxvpEVk7K2nYdAGDl31o%2FdCdgFoKhE%2F61QjzZax4BZ%2F2X9LlgQj7ZxB9S9d3H3yPJ2pJd6m%2FfD5pk13qlqpASA6mu8ePyVMGrvl1lTJx%2FNci4juqal3%2BxfN6eNZTPA78%2BFKIe4QV%2FvWklXWrnmpmvhwVrcm3ydvhC8nJc0Tr6cuzgoOUrUtnSoiNHnlZN2ejOl2MR1rURXqjcLLgBfvgNsNBydbyLae5v3clbeHztxA3VcAXvBEaZRAqXnY7ENHzAMuRxStoLatBqgtHKjzOFwjttE3%2FxCLNACGUgYQhBrbuGSRLewyKFXFyjFkHkSW6R7GEZI2kYz0fuYDZbnzzTOkmxRnPH1mLzl9O0meZiMrGV9pgc1yjo%2FtFYon4Ll0OwlNgi5nfUSoCEieXdPjgTwTW1%2FIbyAwyMmrOioQ5t3QZJTZKmCpefqB%2BSAHnG0sn9lFvVY2d5hGt%2F2RzWBskLfypLNkB3jIuH71LDKTnKB2IR70nDxyYq0A0uhTjyuFAUXkHMR3TkRLL0XDe%2Bsxa697YPljsxNJbi630CEEhBvVLva7nxWScYotaIPbC1%2Br3wHhtm2jdPiSYULQwm4SJvQY6pgErMfU07S7jxg%2FbZNA31UjOCEpsuwn0v72cEY%2FNstI4YxK0e9gwSOHs0hdNvCkUCT0KyIImnwLpY1nGTdKwByeqN0JK71Q8US4rkrHCgDx4jiMr0Cyqm4o%2BCDTnyW7qE6zse7jwB6huOpfI4%2FnDdyLizPSqv7028cel44W00uZKQmqXVOsYhhcJzQf0t4ycq7t%2FHalfcVWK5VK2g0HiSsnd2Buatqxb&X-Amz-Signature=c9db5a39aa523b9d6a9f9d35a8aaafa2962c04d6d524dc076a2ae229ab3e17ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MAN5PQW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDG%2FPjGKJLDoBCy96%2F3H5Feb%2Bw9hzr3l2QHl6RHuHzK9gIhAOqYixNJG2H1mrdYy7X3rCNtH4F4ieSMhC5l2xwdsPnrKv8DCDIQABoMNjM3NDIzMTgzODA1IgxtBKVUQ73iXaTFCr0q3AM1AWCslZg93C3FRydvGKNEdzvdyqi%2BRBaDgbU%2FOPaf2lALmlya%2B6AtOMkD5xSpbfCRkfArjBj3ljtSFIRNXc%2BTRmsce1iIdJe9PzGaFP%2Bcght6VwIk8k%2Bts%2BOYOAWddNDmhBTZzwoEIvf5cPxpFnvgRu7YBZYeyZLf5YB3dfBBZcWF2VQAV3vMyeHfJ%2FiHYxHWVR8sFYKjmh9ggXhwMGimVR%2F%2BBfxClbjDYOUc7OC6HAMQztsl7nW%2FFDrKBQT5dhptX8QceTf2hDZxxAFKkltYDulJDriyl9hItS0QiAGXzzAUE4vtmpcsNGnqsDPDipiQjLDA3g8HK1QX6w3zc5lyVGgUu2TuybR1pU4Ip1CdklQ4uEj9JOF5RjcukXbGNjg2mP8NGBum2ePqltiKlGko%2BTSB1Qn1eNlx2d53BuCy2p36H1DTY4LlwANHIt4gRQvj%2BDZJgKwdZhBw2%2FWlMJabbklfigTMSEPYMDt%2Bft9pRpu8DYSa51Q%2FwTrP94HkvPlyXKYF%2Fl5KepyhQsUGkUbFflOhpfSSZDSZzgmluLPj4aranh1epDuWmIvGg9P%2Fv5ttZtbNE4XqK0ZDhFw3YiHuHSVYsRlpGckUGMnIO44CWZCPtq%2FGsrJiUIloSjC0hYm9BjqkASNy2QrFoWv8IfoSqC9FiGTtCH1c8C1f%2FIMROhjeSdznG9vIpPMhut%2FSFJeZGsCNJTZi0OY89gtwwJAYAAEd8TwnvHR5t%2Fm4XFu9PgnnSLTc0GYkd3WDzd8PLYp2bmNE0CqzQlNkXUMIpzCpCSeAQIjhUYfSNR%2FL0y7RcUDbkVWhSaDWMo%2F2WsbY9aDQqX8UfoKT4W3vJ3oDmxok7M20T6SXgx4j&X-Amz-Signature=8e6fea0ee53717148357c6fc31eb38a1723ec062c0ddd794f26987fe76552650&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MAN5PQW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDG%2FPjGKJLDoBCy96%2F3H5Feb%2Bw9hzr3l2QHl6RHuHzK9gIhAOqYixNJG2H1mrdYy7X3rCNtH4F4ieSMhC5l2xwdsPnrKv8DCDIQABoMNjM3NDIzMTgzODA1IgxtBKVUQ73iXaTFCr0q3AM1AWCslZg93C3FRydvGKNEdzvdyqi%2BRBaDgbU%2FOPaf2lALmlya%2B6AtOMkD5xSpbfCRkfArjBj3ljtSFIRNXc%2BTRmsce1iIdJe9PzGaFP%2Bcght6VwIk8k%2Bts%2BOYOAWddNDmhBTZzwoEIvf5cPxpFnvgRu7YBZYeyZLf5YB3dfBBZcWF2VQAV3vMyeHfJ%2FiHYxHWVR8sFYKjmh9ggXhwMGimVR%2F%2BBfxClbjDYOUc7OC6HAMQztsl7nW%2FFDrKBQT5dhptX8QceTf2hDZxxAFKkltYDulJDriyl9hItS0QiAGXzzAUE4vtmpcsNGnqsDPDipiQjLDA3g8HK1QX6w3zc5lyVGgUu2TuybR1pU4Ip1CdklQ4uEj9JOF5RjcukXbGNjg2mP8NGBum2ePqltiKlGko%2BTSB1Qn1eNlx2d53BuCy2p36H1DTY4LlwANHIt4gRQvj%2BDZJgKwdZhBw2%2FWlMJabbklfigTMSEPYMDt%2Bft9pRpu8DYSa51Q%2FwTrP94HkvPlyXKYF%2Fl5KepyhQsUGkUbFflOhpfSSZDSZzgmluLPj4aranh1epDuWmIvGg9P%2Fv5ttZtbNE4XqK0ZDhFw3YiHuHSVYsRlpGckUGMnIO44CWZCPtq%2FGsrJiUIloSjC0hYm9BjqkASNy2QrFoWv8IfoSqC9FiGTtCH1c8C1f%2FIMROhjeSdznG9vIpPMhut%2FSFJeZGsCNJTZi0OY89gtwwJAYAAEd8TwnvHR5t%2Fm4XFu9PgnnSLTc0GYkd3WDzd8PLYp2bmNE0CqzQlNkXUMIpzCpCSeAQIjhUYfSNR%2FL0y7RcUDbkVWhSaDWMo%2F2WsbY9aDQqX8UfoKT4W3vJ3oDmxok7M20T6SXgx4j&X-Amz-Signature=e55a581d2f33d47e9fcfeae9622bd0cedb99458e907850b2545ac5db52d2d956&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MAN5PQW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDG%2FPjGKJLDoBCy96%2F3H5Feb%2Bw9hzr3l2QHl6RHuHzK9gIhAOqYixNJG2H1mrdYy7X3rCNtH4F4ieSMhC5l2xwdsPnrKv8DCDIQABoMNjM3NDIzMTgzODA1IgxtBKVUQ73iXaTFCr0q3AM1AWCslZg93C3FRydvGKNEdzvdyqi%2BRBaDgbU%2FOPaf2lALmlya%2B6AtOMkD5xSpbfCRkfArjBj3ljtSFIRNXc%2BTRmsce1iIdJe9PzGaFP%2Bcght6VwIk8k%2Bts%2BOYOAWddNDmhBTZzwoEIvf5cPxpFnvgRu7YBZYeyZLf5YB3dfBBZcWF2VQAV3vMyeHfJ%2FiHYxHWVR8sFYKjmh9ggXhwMGimVR%2F%2BBfxClbjDYOUc7OC6HAMQztsl7nW%2FFDrKBQT5dhptX8QceTf2hDZxxAFKkltYDulJDriyl9hItS0QiAGXzzAUE4vtmpcsNGnqsDPDipiQjLDA3g8HK1QX6w3zc5lyVGgUu2TuybR1pU4Ip1CdklQ4uEj9JOF5RjcukXbGNjg2mP8NGBum2ePqltiKlGko%2BTSB1Qn1eNlx2d53BuCy2p36H1DTY4LlwANHIt4gRQvj%2BDZJgKwdZhBw2%2FWlMJabbklfigTMSEPYMDt%2Bft9pRpu8DYSa51Q%2FwTrP94HkvPlyXKYF%2Fl5KepyhQsUGkUbFflOhpfSSZDSZzgmluLPj4aranh1epDuWmIvGg9P%2Fv5ttZtbNE4XqK0ZDhFw3YiHuHSVYsRlpGckUGMnIO44CWZCPtq%2FGsrJiUIloSjC0hYm9BjqkASNy2QrFoWv8IfoSqC9FiGTtCH1c8C1f%2FIMROhjeSdznG9vIpPMhut%2FSFJeZGsCNJTZi0OY89gtwwJAYAAEd8TwnvHR5t%2Fm4XFu9PgnnSLTc0GYkd3WDzd8PLYp2bmNE0CqzQlNkXUMIpzCpCSeAQIjhUYfSNR%2FL0y7RcUDbkVWhSaDWMo%2F2WsbY9aDQqX8UfoKT4W3vJ3oDmxok7M20T6SXgx4j&X-Amz-Signature=75d1759faec4cc2fc7803d78a0d5cdb16a9bcad7b7e8ac16028ee8a8e53135b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MAN5PQW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDG%2FPjGKJLDoBCy96%2F3H5Feb%2Bw9hzr3l2QHl6RHuHzK9gIhAOqYixNJG2H1mrdYy7X3rCNtH4F4ieSMhC5l2xwdsPnrKv8DCDIQABoMNjM3NDIzMTgzODA1IgxtBKVUQ73iXaTFCr0q3AM1AWCslZg93C3FRydvGKNEdzvdyqi%2BRBaDgbU%2FOPaf2lALmlya%2B6AtOMkD5xSpbfCRkfArjBj3ljtSFIRNXc%2BTRmsce1iIdJe9PzGaFP%2Bcght6VwIk8k%2Bts%2BOYOAWddNDmhBTZzwoEIvf5cPxpFnvgRu7YBZYeyZLf5YB3dfBBZcWF2VQAV3vMyeHfJ%2FiHYxHWVR8sFYKjmh9ggXhwMGimVR%2F%2BBfxClbjDYOUc7OC6HAMQztsl7nW%2FFDrKBQT5dhptX8QceTf2hDZxxAFKkltYDulJDriyl9hItS0QiAGXzzAUE4vtmpcsNGnqsDPDipiQjLDA3g8HK1QX6w3zc5lyVGgUu2TuybR1pU4Ip1CdklQ4uEj9JOF5RjcukXbGNjg2mP8NGBum2ePqltiKlGko%2BTSB1Qn1eNlx2d53BuCy2p36H1DTY4LlwANHIt4gRQvj%2BDZJgKwdZhBw2%2FWlMJabbklfigTMSEPYMDt%2Bft9pRpu8DYSa51Q%2FwTrP94HkvPlyXKYF%2Fl5KepyhQsUGkUbFflOhpfSSZDSZzgmluLPj4aranh1epDuWmIvGg9P%2Fv5ttZtbNE4XqK0ZDhFw3YiHuHSVYsRlpGckUGMnIO44CWZCPtq%2FGsrJiUIloSjC0hYm9BjqkASNy2QrFoWv8IfoSqC9FiGTtCH1c8C1f%2FIMROhjeSdznG9vIpPMhut%2FSFJeZGsCNJTZi0OY89gtwwJAYAAEd8TwnvHR5t%2Fm4XFu9PgnnSLTc0GYkd3WDzd8PLYp2bmNE0CqzQlNkXUMIpzCpCSeAQIjhUYfSNR%2FL0y7RcUDbkVWhSaDWMo%2F2WsbY9aDQqX8UfoKT4W3vJ3oDmxok7M20T6SXgx4j&X-Amz-Signature=1a36206c2392f336d1bf880e41a9773a2a58bacaae206227af727ca9af0edd1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MAN5PQW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDG%2FPjGKJLDoBCy96%2F3H5Feb%2Bw9hzr3l2QHl6RHuHzK9gIhAOqYixNJG2H1mrdYy7X3rCNtH4F4ieSMhC5l2xwdsPnrKv8DCDIQABoMNjM3NDIzMTgzODA1IgxtBKVUQ73iXaTFCr0q3AM1AWCslZg93C3FRydvGKNEdzvdyqi%2BRBaDgbU%2FOPaf2lALmlya%2B6AtOMkD5xSpbfCRkfArjBj3ljtSFIRNXc%2BTRmsce1iIdJe9PzGaFP%2Bcght6VwIk8k%2Bts%2BOYOAWddNDmhBTZzwoEIvf5cPxpFnvgRu7YBZYeyZLf5YB3dfBBZcWF2VQAV3vMyeHfJ%2FiHYxHWVR8sFYKjmh9ggXhwMGimVR%2F%2BBfxClbjDYOUc7OC6HAMQztsl7nW%2FFDrKBQT5dhptX8QceTf2hDZxxAFKkltYDulJDriyl9hItS0QiAGXzzAUE4vtmpcsNGnqsDPDipiQjLDA3g8HK1QX6w3zc5lyVGgUu2TuybR1pU4Ip1CdklQ4uEj9JOF5RjcukXbGNjg2mP8NGBum2ePqltiKlGko%2BTSB1Qn1eNlx2d53BuCy2p36H1DTY4LlwANHIt4gRQvj%2BDZJgKwdZhBw2%2FWlMJabbklfigTMSEPYMDt%2Bft9pRpu8DYSa51Q%2FwTrP94HkvPlyXKYF%2Fl5KepyhQsUGkUbFflOhpfSSZDSZzgmluLPj4aranh1epDuWmIvGg9P%2Fv5ttZtbNE4XqK0ZDhFw3YiHuHSVYsRlpGckUGMnIO44CWZCPtq%2FGsrJiUIloSjC0hYm9BjqkASNy2QrFoWv8IfoSqC9FiGTtCH1c8C1f%2FIMROhjeSdznG9vIpPMhut%2FSFJeZGsCNJTZi0OY89gtwwJAYAAEd8TwnvHR5t%2Fm4XFu9PgnnSLTc0GYkd3WDzd8PLYp2bmNE0CqzQlNkXUMIpzCpCSeAQIjhUYfSNR%2FL0y7RcUDbkVWhSaDWMo%2F2WsbY9aDQqX8UfoKT4W3vJ3oDmxok7M20T6SXgx4j&X-Amz-Signature=dcc866a231ae21c35e175bf54ca2acbac63b327420033e76bfe7cac73eba2652&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MAN5PQW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDG%2FPjGKJLDoBCy96%2F3H5Feb%2Bw9hzr3l2QHl6RHuHzK9gIhAOqYixNJG2H1mrdYy7X3rCNtH4F4ieSMhC5l2xwdsPnrKv8DCDIQABoMNjM3NDIzMTgzODA1IgxtBKVUQ73iXaTFCr0q3AM1AWCslZg93C3FRydvGKNEdzvdyqi%2BRBaDgbU%2FOPaf2lALmlya%2B6AtOMkD5xSpbfCRkfArjBj3ljtSFIRNXc%2BTRmsce1iIdJe9PzGaFP%2Bcght6VwIk8k%2Bts%2BOYOAWddNDmhBTZzwoEIvf5cPxpFnvgRu7YBZYeyZLf5YB3dfBBZcWF2VQAV3vMyeHfJ%2FiHYxHWVR8sFYKjmh9ggXhwMGimVR%2F%2BBfxClbjDYOUc7OC6HAMQztsl7nW%2FFDrKBQT5dhptX8QceTf2hDZxxAFKkltYDulJDriyl9hItS0QiAGXzzAUE4vtmpcsNGnqsDPDipiQjLDA3g8HK1QX6w3zc5lyVGgUu2TuybR1pU4Ip1CdklQ4uEj9JOF5RjcukXbGNjg2mP8NGBum2ePqltiKlGko%2BTSB1Qn1eNlx2d53BuCy2p36H1DTY4LlwANHIt4gRQvj%2BDZJgKwdZhBw2%2FWlMJabbklfigTMSEPYMDt%2Bft9pRpu8DYSa51Q%2FwTrP94HkvPlyXKYF%2Fl5KepyhQsUGkUbFflOhpfSSZDSZzgmluLPj4aranh1epDuWmIvGg9P%2Fv5ttZtbNE4XqK0ZDhFw3YiHuHSVYsRlpGckUGMnIO44CWZCPtq%2FGsrJiUIloSjC0hYm9BjqkASNy2QrFoWv8IfoSqC9FiGTtCH1c8C1f%2FIMROhjeSdznG9vIpPMhut%2FSFJeZGsCNJTZi0OY89gtwwJAYAAEd8TwnvHR5t%2Fm4XFu9PgnnSLTc0GYkd3WDzd8PLYp2bmNE0CqzQlNkXUMIpzCpCSeAQIjhUYfSNR%2FL0y7RcUDbkVWhSaDWMo%2F2WsbY9aDQqX8UfoKT4W3vJ3oDmxok7M20T6SXgx4j&X-Amz-Signature=3f4271ab17be54ecbdd7758b402cbcefcd0a23ac0161dc034be216fbc8a81e16&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RSDZ7OW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCID%2BF6YFdQmtCw%2BNC%2B3H774TvJ%2FTZE09Um7xLtPOxc6elAiBN9GUoLlwmAj3HufWxe6LFNKwFSk0TophzVEWrig7mvyr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIM%2BwqlTlXnCokBtQ12KtwDgVilvpe5QdgaiIy%2FPfZPMBVzaIZdJNXje4GO67epKjIq308nP%2FXslMF6d7fADdKlDYGjLbaFd8D7gfbB2bO8jlblH2aoYYLumJDEaz10XuI6kHgT7hAtbCUewzbh%2BJXHz9u4cfi9exgDraeqmqejUiQxSgFzcSW3Nk195GWUKMhGThHKRaKmgsn%2Fhbwkj4xkEMv8geeUBzFJsfyoq%2FLulNt6wFTGKAqM9860tM%2FQf0r20H5SSctUBNENo%2FnUuS8iBZN6KZ7Pj78RzszO39Gf%2BoAQGvkJjhgPhi7YdvkQcN3unLp9yE%2F%2FEzUXMH4XnUv1nSjJh0gnqKPHcPqfXe6XMgsIRDztKiNj1pDLYZiJg0FoCFP2DYQqtNKPDQH%2BVCxzy4l0hLDCrtZM9j%2BKDsdEkA%2FBFlmXypRc%2BkVFAtjYjWywGEY6v%2BPd8x4vQaN3ZaZLCyA3xt2qmGleuTxziIB0WeaqzsZl83DFoyRJsstIl4NLF4NMf8%2FIeiKfXpkxoO1vJ6q347594w61%2BDnZGv26CQC0iOW0nVH%2Fwc8bIhEIYmKsN5LBun0KjpJjrHoW5H76wGkIkEk8lw9wCtf1rDAEW8Z644e45NiPJm6qVwRq3tvcrAb9Ppxo%2FRmzAM4wkYWJvQY6pgGLk9NMlA4rWUFdGKRi%2BWsdZDGE0AT3D4ZOaTG5OPyIWW2BMKW6U1VfNkMp1XG4LsSmvdgp6Zs%2FZ%2BLPF6Z%2BDemsl6KnI4qiorUshStUObXmReR1NjG%2BMSeKJiWyiE68VCtiX%2FZhbs%2ByHy63jF2zieyOFyHbZpNcdWWv%2BWToNwksrmOLXxIJiDEy%2BhiiYAzaVRE%2F7thk6yphxl%2BMdHOe9FprXyrVCLwI&X-Amz-Signature=a34039a5ea5ad3b1ab20d1d268c416a3e1cd60981a09204f50e8606fdabe1858&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ3GLBIG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQDlia9DBLCd4od5sbp2UvPiTc4UFfj2bfWS5cSKoOJVrAIgKcVgpbwJ3nXYAOapHkg%2B%2FgYoWC42RGwsD4UIahGcgEEq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDPS5FA1PLwx%2Fh8LUZSrcAxMEkr%2FtY%2FlAoHvXEB0ZQx5wy%2FkWqSBNlbS19UbJu%2BQHMIqYQMxN6wbsn4wr7JzooYub7DxVFUBBiAS0uabN7a%2Fwdh%2FXEZkR2n8EYmYZTLKTUDF%2B8PKcNRskpvO78UN9t1s3NwaLzxqJzRO7vNHqWXAQA6Gvnftu%2F2%2BxqSAna%2FZgZVZx5RuW9eo%2FkvpO0%2Fydg0sNr36HRXRzuuzWhF%2Fu2ApEV8ofxB8ZO8CTkr1XNnMQCQIDghy3PT6lFG6K5%2FEmQ0Cn14o6cpI2%2FZx6ghm9sRV8JTJYJu4By6xARnfl5rLo%2BewzDdhh0qOLxjg8rtqdO0SfuEX%2FezTrx0fF5vEfr0vcu2ucXGw%2B%2BIZqTK%2B4nsf2X4x6nfozLRAMVowVOM3f6RB3kXErFUGcLg2fESiTpDoo%2BIOT5FEvhsj69kmfsFYEbBZUn6uN7J8m12uDfR5hq8BhprmcjdazedDHNSnot6iHeSx9P5G5VDXgA4aTujWpyH5jK3ViQOiSItecH7EHnNz7A3MYJRs5lFIPs6DOXOaBCtbT8eNCnBwhQpJwbwcQEHiEl7ARO%2BjyIlQ%2FyLRG7fXPkzIivm%2FS6zQFIcI2KwLaAJmctXRNQsOQq9iJwg8EmgGEhbTXAnAnJT3XMPWDib0GOqUBSZCLSIvZbD%2F3Py%2BGaDMPOChHRMX7lWzkTLGgVwq9nQ5bJkTHJTgJPsx1nN8%2B4lit%2F1K3uz9hXcphL7kt6FiehPdXDzwktRIetVEGL0T3dPQWcA3hUVIZpnm%2FfyEbITIZYsyL71ujquqywhsj8OvBF4Dl9WfYd2Xbl3ZH3KaS2oxcFsscAUCdOX9%2FBGIiZOdnVf4H78E5KE1AF3bqK1Tc0UT7n5PE&X-Amz-Signature=1ec0878d526ca366abb88fe9bbeadde6a02e281450c302f7cd4002761adebdff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MAN5PQW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDG%2FPjGKJLDoBCy96%2F3H5Feb%2Bw9hzr3l2QHl6RHuHzK9gIhAOqYixNJG2H1mrdYy7X3rCNtH4F4ieSMhC5l2xwdsPnrKv8DCDIQABoMNjM3NDIzMTgzODA1IgxtBKVUQ73iXaTFCr0q3AM1AWCslZg93C3FRydvGKNEdzvdyqi%2BRBaDgbU%2FOPaf2lALmlya%2B6AtOMkD5xSpbfCRkfArjBj3ljtSFIRNXc%2BTRmsce1iIdJe9PzGaFP%2Bcght6VwIk8k%2Bts%2BOYOAWddNDmhBTZzwoEIvf5cPxpFnvgRu7YBZYeyZLf5YB3dfBBZcWF2VQAV3vMyeHfJ%2FiHYxHWVR8sFYKjmh9ggXhwMGimVR%2F%2BBfxClbjDYOUc7OC6HAMQztsl7nW%2FFDrKBQT5dhptX8QceTf2hDZxxAFKkltYDulJDriyl9hItS0QiAGXzzAUE4vtmpcsNGnqsDPDipiQjLDA3g8HK1QX6w3zc5lyVGgUu2TuybR1pU4Ip1CdklQ4uEj9JOF5RjcukXbGNjg2mP8NGBum2ePqltiKlGko%2BTSB1Qn1eNlx2d53BuCy2p36H1DTY4LlwANHIt4gRQvj%2BDZJgKwdZhBw2%2FWlMJabbklfigTMSEPYMDt%2Bft9pRpu8DYSa51Q%2FwTrP94HkvPlyXKYF%2Fl5KepyhQsUGkUbFflOhpfSSZDSZzgmluLPj4aranh1epDuWmIvGg9P%2Fv5ttZtbNE4XqK0ZDhFw3YiHuHSVYsRlpGckUGMnIO44CWZCPtq%2FGsrJiUIloSjC0hYm9BjqkASNy2QrFoWv8IfoSqC9FiGTtCH1c8C1f%2FIMROhjeSdznG9vIpPMhut%2FSFJeZGsCNJTZi0OY89gtwwJAYAAEd8TwnvHR5t%2Fm4XFu9PgnnSLTc0GYkd3WDzd8PLYp2bmNE0CqzQlNkXUMIpzCpCSeAQIjhUYfSNR%2FL0y7RcUDbkVWhSaDWMo%2F2WsbY9aDQqX8UfoKT4W3vJ3oDmxok7M20T6SXgx4j&X-Amz-Signature=9705827a3d1063a6d4711f0aa9b48d21decaba5f9a929f8fed7637f1a09ebad2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MAN5PQW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDG%2FPjGKJLDoBCy96%2F3H5Feb%2Bw9hzr3l2QHl6RHuHzK9gIhAOqYixNJG2H1mrdYy7X3rCNtH4F4ieSMhC5l2xwdsPnrKv8DCDIQABoMNjM3NDIzMTgzODA1IgxtBKVUQ73iXaTFCr0q3AM1AWCslZg93C3FRydvGKNEdzvdyqi%2BRBaDgbU%2FOPaf2lALmlya%2B6AtOMkD5xSpbfCRkfArjBj3ljtSFIRNXc%2BTRmsce1iIdJe9PzGaFP%2Bcght6VwIk8k%2Bts%2BOYOAWddNDmhBTZzwoEIvf5cPxpFnvgRu7YBZYeyZLf5YB3dfBBZcWF2VQAV3vMyeHfJ%2FiHYxHWVR8sFYKjmh9ggXhwMGimVR%2F%2BBfxClbjDYOUc7OC6HAMQztsl7nW%2FFDrKBQT5dhptX8QceTf2hDZxxAFKkltYDulJDriyl9hItS0QiAGXzzAUE4vtmpcsNGnqsDPDipiQjLDA3g8HK1QX6w3zc5lyVGgUu2TuybR1pU4Ip1CdklQ4uEj9JOF5RjcukXbGNjg2mP8NGBum2ePqltiKlGko%2BTSB1Qn1eNlx2d53BuCy2p36H1DTY4LlwANHIt4gRQvj%2BDZJgKwdZhBw2%2FWlMJabbklfigTMSEPYMDt%2Bft9pRpu8DYSa51Q%2FwTrP94HkvPlyXKYF%2Fl5KepyhQsUGkUbFflOhpfSSZDSZzgmluLPj4aranh1epDuWmIvGg9P%2Fv5ttZtbNE4XqK0ZDhFw3YiHuHSVYsRlpGckUGMnIO44CWZCPtq%2FGsrJiUIloSjC0hYm9BjqkASNy2QrFoWv8IfoSqC9FiGTtCH1c8C1f%2FIMROhjeSdznG9vIpPMhut%2FSFJeZGsCNJTZi0OY89gtwwJAYAAEd8TwnvHR5t%2Fm4XFu9PgnnSLTc0GYkd3WDzd8PLYp2bmNE0CqzQlNkXUMIpzCpCSeAQIjhUYfSNR%2FL0y7RcUDbkVWhSaDWMo%2F2WsbY9aDQqX8UfoKT4W3vJ3oDmxok7M20T6SXgx4j&X-Amz-Signature=cc6ccc5927827879d0abc6a759b4876910491aa561d8103a6f7bceab8553b2fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MAN5PQW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDG%2FPjGKJLDoBCy96%2F3H5Feb%2Bw9hzr3l2QHl6RHuHzK9gIhAOqYixNJG2H1mrdYy7X3rCNtH4F4ieSMhC5l2xwdsPnrKv8DCDIQABoMNjM3NDIzMTgzODA1IgxtBKVUQ73iXaTFCr0q3AM1AWCslZg93C3FRydvGKNEdzvdyqi%2BRBaDgbU%2FOPaf2lALmlya%2B6AtOMkD5xSpbfCRkfArjBj3ljtSFIRNXc%2BTRmsce1iIdJe9PzGaFP%2Bcght6VwIk8k%2Bts%2BOYOAWddNDmhBTZzwoEIvf5cPxpFnvgRu7YBZYeyZLf5YB3dfBBZcWF2VQAV3vMyeHfJ%2FiHYxHWVR8sFYKjmh9ggXhwMGimVR%2F%2BBfxClbjDYOUc7OC6HAMQztsl7nW%2FFDrKBQT5dhptX8QceTf2hDZxxAFKkltYDulJDriyl9hItS0QiAGXzzAUE4vtmpcsNGnqsDPDipiQjLDA3g8HK1QX6w3zc5lyVGgUu2TuybR1pU4Ip1CdklQ4uEj9JOF5RjcukXbGNjg2mP8NGBum2ePqltiKlGko%2BTSB1Qn1eNlx2d53BuCy2p36H1DTY4LlwANHIt4gRQvj%2BDZJgKwdZhBw2%2FWlMJabbklfigTMSEPYMDt%2Bft9pRpu8DYSa51Q%2FwTrP94HkvPlyXKYF%2Fl5KepyhQsUGkUbFflOhpfSSZDSZzgmluLPj4aranh1epDuWmIvGg9P%2Fv5ttZtbNE4XqK0ZDhFw3YiHuHSVYsRlpGckUGMnIO44CWZCPtq%2FGsrJiUIloSjC0hYm9BjqkASNy2QrFoWv8IfoSqC9FiGTtCH1c8C1f%2FIMROhjeSdznG9vIpPMhut%2FSFJeZGsCNJTZi0OY89gtwwJAYAAEd8TwnvHR5t%2Fm4XFu9PgnnSLTc0GYkd3WDzd8PLYp2bmNE0CqzQlNkXUMIpzCpCSeAQIjhUYfSNR%2FL0y7RcUDbkVWhSaDWMo%2F2WsbY9aDQqX8UfoKT4W3vJ3oDmxok7M20T6SXgx4j&X-Amz-Signature=8c13d41118f2ccb9d0f67c7d098568d396306cf0ca51be13968699e13671c9ea&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RPH3EM2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIBAjl3lck%2BsCok3l0IE4ZQirHwi3CX%2Ft3UN%2BqJ1HOwFoAiAsIDsXPOqheXOJAP7PKVM9%2BeyTanxIyWysvtCSXALlpir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMyqK25b8CvTkwukUXKtwD4r%2BvL4%2FaWvBtRD3qoB8XcD7vIRpzscoE%2F%2BIBKxO365%2BQK58FVLT1uiu4lNVhybyx86VzSJGMQDS6tjtwFTZ5jcERRWzr%2Fh%2F40cXlezB61VKzM4EAxoPV%2BRwfc%2BwpCM0QdApLnZVCPg15megIqYZV1SwWnd7YZAGK7i%2FXuaE6rvTQ9k0fpuNzIhG5hdUKAzwXXB%2BMaR43IY6%2B8TxUlM9PH58ycEH9B%2BdYh4I%2BGQ3KmI%2FabGm8xfdzKBc5WlKP0x8QLQiYaDa4zB29uqV1b9vfe0m0TzY%2FyjVSM%2Bkxw3MBi4et2ulxrD%2B8oeDDxfVpKpPM9JdRhhAH25rV08ckZG%2FSySejqhiyU5rU%2BZjZfd6csD9GgbYAGSDFgU53DgB9IKUHLORH0szes3GKxclgnPbZS2Mu6O5UpiTgDIv14o4rmfx%2FmNJG387KmiIs5vg5hJ72IByfHRy6e6qAMGQY6JVHk2QQifki3AD8%2BT5bKwp9IvHlihldwBxa%2BYWW1uiq3%2BbDTEoGWYkiQKVwsqEBdzDVqufP5geE4FVQXRO5vFQsGUmFcRENr9AxjjDvtR7pY8KXdhlC5%2FAqqrQ1ddBgGm7knDSNJMsn3ggCBl2CjdDKVyV8HoLWEMd%2Bn5VrcBUwk4SJvQY6pgG0e3zTJ5LRqfWYW1nlLThhbBb%2BUNpyvSK408X39vBihVbMCS0hwSIEdEBouBTjSe8A8NMyGs53S7NNOhQISN3rugX%2B2d3kCgPdk6b4BWoZMa6tmCyrGKJDLM0jl53w4K7LjwUg8zn6c2Kxahu%2Fz9jY5wQ9jjsUIMz0RNQIR%2FqIWg04rC15nPQEf%2Bnx6MRRSWESTDxOtXC4T8bDxmgA7VExiOKfZCjS&X-Amz-Signature=7f78fba87113e0a3c398c0094adf60195f46206a81c6068fd22f2e836abaddfb&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SX5Q6KJS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQD84%2BSOGHnGRhXsC6RbyWaebBzlBN3IXeL3A0Wvu70kiAIgQ6WUQIzixvXIwLGZGzIMpPfz6FL30k9%2B11rFL61p9XEq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDHei50kIIrT7ti%2BU1CrcA7rbeeV9y4Zltw1crY8KSlZV%2FcKYjRXAllyILsHiBxQ23BJoY6LG6zCfI%2FsxdXsNAe%2Ft8b8QboVLsH4ikVbiJjAohRk2dGoKO%2BkruAqEmNOqwePar6jDluhA1C0DLpN2e2E2EDSVvisGS9HfmmjQ0ALhr7jX55geHEfG9Z20yTLJP4usESzxf3gXGL%2FjqeWf4Pt72Nh6zoZSK8rt0FQZ2hOSS6r9iOzEGC110X8YyREQAlV1QI7OkzrcKPnfBMGrbvvHHcHYU5U7%2BZiOqLtYllZSjPQUT6EKxx7t5Ipxgt6qRgV8OwuHQuZmvcA78t2NaFXwnSxp%2BiGn1foOkP3ZZmunanxnPcDbVTQYTrOaekLxTXF46FpmFXZBX5pGN2%2BDV6eXKgrwgqLOxyHd8vr8xnjeLwgBUUJrh%2BrHZHt%2BHHIyO5hNrUOxoOcYpxHMi6%2BaM7KNsU4K%2BJzLbuSqw32MP%2BML%2FrexW6QlP0CQkj7tjhmMnV%2F1QyAtWB9tl883UBbIjFzqvqWMs3GPTvgAyGlGy9TRgbIJHeLa87u3anyGBuacV3NlcC7yTSZGd%2Feg7Sj5yLm52nTfsJjRmzxTKBTF4jtNuR1873O2JMOQqjHyz5I%2BH%2B%2BnomXqljyOyIeZMMiEib0GOqUBORVJV9nSqqoFVV7b9JKmA5OI2D628n6v9FCR3va3bdhH3KYlvzD9rGedK5qBKF6PbUQEl8qAZJvY1d1DSd1LVj%2Bi70yU1WygAHFFqdwlpjkS4etGWoLr78iqFkwso6Iq7heCMUxKzaD67S42sMg9FvRubjwjlDkZ%2BR91GAvxxMo8fgDvFoIS7AiGKDEoqB6cVgB7wtiDD6ivf63cgIjbJQNrL8DO&X-Amz-Signature=96dba87cc009910bf3a701ed32c29f3602562679919b03cb66d1c8c99f19675d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOREDQLR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCWp9l3TKE4TW9ag6ltCzCPnqznjHAkaMhDyE%2Bn87VNWgIhAPqd7iIkPeds%2FXCPXyga7poNGXur3f8tL60VJ08cRcL6Kv8DCDIQABoMNjM3NDIzMTgzODA1IgwYPU7VzWL%2Fj5ZWYqIq3AMvUqD1NwEvVn1ciXfCaxcn77hNcJ3pxit1PmfSah6VgEMe1KK%2Fa%2F0ZDmgHkDJaqHsc%2FMt6Is0aU8aHi8tO5Ipj1whwUwWk0hWLxRIsyQmiT6r52nYgtWlKF7iT4wrqkOmt6QG472yhRtoDO%2BYCl0sqlSdZ%2BZAjEUC2g%2FKjkU5wD2XDOUKWy%2FmZygaId0Hc%2Bi7gWGKxNbCUtlLhq5PlVdJnCBTUJjWBGkf0JsXP9BHunDwwndfMRTnpaMbAK37Y02jj5FCn2UgnQ04GGKGhTx18imato5L%2BWLEU6OJLRMMarwwpiwvwFs%2B24fL8%2BcoBfyIX6mR0i2XMuwY%2BPb%2F69H%2FxFe1s7RdlqCaSYvcfh533K4PXmokN3F2YMQZSXMO7Kw415RkB9luJW5ndOn%2Ba0QQYsB6UtGHinxtRivt565EH5TG8eBWpW6eBZLtf1DiDg0Hsy9T5V1KPuVaVbG01zQaiWPe2YW3neLQf%2F%2FJxgHzDY9z41OL%2B5z3k3XWZn2l0o8DrW%2BSfwAsPj1u92BkAfPOH5D8%2BfiG22ni%2B5KYutLcQFWeUqJXoaqb7x%2FpEvmwfEQGbed7eiZHffC0fGaqOe3pH2KYmAeUONmugeF53lJlySOr9GZAYqKZeq9kVazD3g4m9BjqkAb3dEETqxr4idEgcbfJG%2BfJfIyFYQGaT5uXXo0qVbRm2aLgnQuSmYgeYq9DtALz8hxzPts3ox4vGvqCbYzzrUZNv%2FRZ8krd8K%2Bkw1zgfd3qqXjfnDnRL2ZkTaDr5DqFw0zWpkajlxoxVZ12RqfPIYjR7kNtHefv3qSsn5PohgmvXAsN2yRjev9DyIylL1D8g8VoGWHChKkUONEFhdmpSWj%2FmkmJg&X-Amz-Signature=b0331c1c7d6e1bf85966b4be26f688559115b43a06c6e13ba3b65f5606ce7c29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQYYFHWQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDg4LuH2tJ5pcRCBxkGG3Nl%2BLugtW5qBOUa%2BixA0GOAEAiBUseh1coHzLuOJeDTu5KcMgIeLBE8bauvvCeIcIXuumSr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMGvbhHpnERU4CJ5CTKtwDb9gvJO1YWjBX%2B8DM8TWGYYEivyMVDea%2FXACRqHI5%2F65qUXr32o%2BSlu7OFFDJjMorHTa9k5d29kb2eEl7rXLQQ5a%2FTXipk%2FnQNJN6ucfOY0pP0YuwVfdtcdZoUMO15fjIejB8PkP6wm7rGp7%2BtKBDIB7dpi%2Be%2Ft8Vh%2B0ceHzzwDFUAXVEBZiXzjbMXQcCtNe2Z%2BYUYyRCLKR3GrHhM%2FswOf51AqIlGVW%2BtQkyI7bQTJlZSCxzxkUkMVu%2Fmjxr4n58%2FQ9pI2rlOfLSgPTYPtGi%2BLyzmGn3lArvdwnygu8fp3tHanGXyRIo0KKesuNb2BdfYTPGGy%2FvdUzD%2BrkHMi0YrCLweS1Fp2O%2BmzWDvDVPjHVU%2FRp94lmTyMRD08yD8TNFxOEj4x4zcr1lAdBoYEL6ni7DqN4oL4jk9sNWkqJ6%2Fo1jFpUMZhFXqIspZZBGLcEo5r0cGFDhoiKCZUTqnWGTOAWnWZvUNIQA049Uih2xrUQXvFucGYfggbsTc6Zlk9XKxgoyUR%2BSdCr%2BEI1omM2wOpHRlbMfS31%2BPkBqpNI0ULQEH5RZytOH5gGJTTKs67HU%2FWDadJTJ5n7WrfxmdgUDg0oItP4YyzF690rM7JbmFQyGRDX%2FDzRhwMc3cUgw4oOJvQY6pgGwaeHeLDovCMna3hn5ZLRO9QaAhpwFFCgutopW828muNVT%2FcaK%2FBDCcd398%2BpZgb76orpZO%2BeDx9jdZIN%2FpuIKO3TRs8cwRFndc2nV2YtkDEH4AZNY%2Bb9%2FSQdBZ3SmuAhdCPFnUFN2GK7FmxJTLCD1P70KjJEUyS7lm4Pk198ZvtuaQUWIUcThVMOryVGbFQovIG4RW8gsc7%2FPC0Wr8qmfpDF7591x&X-Amz-Signature=89915f2e3fba1d796b8931bc19e22fd87bad5778539e8423949311da74a3168d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQYYFHWQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDg4LuH2tJ5pcRCBxkGG3Nl%2BLugtW5qBOUa%2BixA0GOAEAiBUseh1coHzLuOJeDTu5KcMgIeLBE8bauvvCeIcIXuumSr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMGvbhHpnERU4CJ5CTKtwDb9gvJO1YWjBX%2B8DM8TWGYYEivyMVDea%2FXACRqHI5%2F65qUXr32o%2BSlu7OFFDJjMorHTa9k5d29kb2eEl7rXLQQ5a%2FTXipk%2FnQNJN6ucfOY0pP0YuwVfdtcdZoUMO15fjIejB8PkP6wm7rGp7%2BtKBDIB7dpi%2Be%2Ft8Vh%2B0ceHzzwDFUAXVEBZiXzjbMXQcCtNe2Z%2BYUYyRCLKR3GrHhM%2FswOf51AqIlGVW%2BtQkyI7bQTJlZSCxzxkUkMVu%2Fmjxr4n58%2FQ9pI2rlOfLSgPTYPtGi%2BLyzmGn3lArvdwnygu8fp3tHanGXyRIo0KKesuNb2BdfYTPGGy%2FvdUzD%2BrkHMi0YrCLweS1Fp2O%2BmzWDvDVPjHVU%2FRp94lmTyMRD08yD8TNFxOEj4x4zcr1lAdBoYEL6ni7DqN4oL4jk9sNWkqJ6%2Fo1jFpUMZhFXqIspZZBGLcEo5r0cGFDhoiKCZUTqnWGTOAWnWZvUNIQA049Uih2xrUQXvFucGYfggbsTc6Zlk9XKxgoyUR%2BSdCr%2BEI1omM2wOpHRlbMfS31%2BPkBqpNI0ULQEH5RZytOH5gGJTTKs67HU%2FWDadJTJ5n7WrfxmdgUDg0oItP4YyzF690rM7JbmFQyGRDX%2FDzRhwMc3cUgw4oOJvQY6pgGwaeHeLDovCMna3hn5ZLRO9QaAhpwFFCgutopW828muNVT%2FcaK%2FBDCcd398%2BpZgb76orpZO%2BeDx9jdZIN%2FpuIKO3TRs8cwRFndc2nV2YtkDEH4AZNY%2Bb9%2FSQdBZ3SmuAhdCPFnUFN2GK7FmxJTLCD1P70KjJEUyS7lm4Pk198ZvtuaQUWIUcThVMOryVGbFQovIG4RW8gsc7%2FPC0Wr8qmfpDF7591x&X-Amz-Signature=6b2b16bf77b819f6d38057f6d4cbee73164170f3063bad84902c38a13de64373&X-Amz-SignedHeaders=host&x-id=GetObject)

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
